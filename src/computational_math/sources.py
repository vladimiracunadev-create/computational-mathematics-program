"""Registro de fuentes: trazabilidad verificable de toda obra citada.

El programa cita obras en las 360 clases. Este módulo es la capa que convierte
esas citas en algo **comprobable**: cada obra usada tiene una entrada en
``sources/bibliography.json`` con un localizador resoluble —ISBN-13, DOI o URL
de la fuente primaria— y un estado que dice si ese localizador se comprobó
contra su autoridad o si sigue pendiente.

Reglas que no se negocian:

- una obra sin localizador verificable se marca ``pendiente``, nunca se inventa;
- una obra que deja de resolver se marca, nunca se borra;
- las cifras que publica el README las produce el verificador, no la mano.

Dos capas usan este módulo:

``scripts/verify_sources.py``
    offline y determinista. Corre en CI y bloquea.

``scripts/refresh_sources.py``
    en red. Resuelve contra Open Library, Crossref y DataCite. No bloquea.
"""

from __future__ import annotations

import functools
import json
import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterator, List, NamedTuple, Optional, Set, Tuple

from . import content, curriculum
from .curriculum import ROOT

__all__ = [
    "REGISTRY_PATH",
    "SCHEMA_VERSION",
    "TIPOS",
    "ESTADOS",
    "POLICY",
    "STAGES",
    "Usage",
    "isbn13_valid",
    "normalise_isbn",
    "normalise_doi",
    "normalise_title",
    "canonical_locator",
    "derive_identifiers",
    "dois_in_text",
    "parse_label",
    "source_key",
    "make_id",
    "usages",
    "sources_used",
    "reference_line",
    "AREAS_PATH",
    "load_areas",
    "area_label",
    "part_areas",
    "class_areas",
    "work_areas",
    "citation_fit",
    "class_block",
    "load_registry",
    "dump_registry",
    "entries_by_key",
    "registry_stats",
    "leading_work",
    "stage_of_part",
]

REGISTRY_PATH = ROOT / "sources" / "bibliography.json"
AREAS_PATH = ROOT / "sources" / "areas.yaml"
SCHEMA_VERSION = 1
TIPOS = ("book", "paper", "standard", "reference", "dataset")
ESTADOS = ("verificada", "pendiente")

POLICY = (
    "Toda afirmación del programa se apoya en una entrada de este registro. "
    "Ninguna entrada se acepta sin localizador verificable."
)

REF_RE = re.compile(r"^\[(?P<label>.+)\]\((?P<url>https?://\S+)\)$")
DOI_IN_URL_RE = re.compile(r"(10\.\d{4,9}/[^\s?#]+)", re.IGNORECASE)
ISBN13_IN_TEXT_RE = re.compile(r"97[89][- ]?(?:\d[- ]?){9}\d")
CHAPTER_DOI_RE = re.compile(r"_\d+$")
ARXIV_RE = re.compile(r"^https?://arxiv\.org/abs/(?P<id>.+?)(?:v\d+)?/?$", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(1[6-9]\d{2}|20\d{2})\b")
INITIALS_RE = re.compile(r"^(?:[A-ZÁÉÍÓÚÑ]\.?[- ]?){1,4}(?:et al\.?)?$")

# Sedes que publican normas o documentación oficial: su localizador es la URL.
STANDARD_HOSTS = frozenset({
    "standards.ieee.org",
    "ieeexplore.ieee.org",
    "www.bipm.org",
    "www.nist.gov",
    "pages.nist.gov",
    "cwe.mitre.org",
    "peps.python.org",
})

# Las cinco etapas del programa, por identificador de parte.
STAGES: Tuple[Tuple[str, str, Tuple[str, ...]], ...] = (
    ("1", "Cimientos", ("00", "01", "02", "03", "04")),
    ("2", "El lenguaje de los modelos", ("05", "06", "07", "08")),
    ("3", "Incertidumbre y cómputo", ("09", "10", "11", "12", "13")),
    ("4", "La matemática de la IA", ("14", "15", "16")),
    ("5", "Frontera e investigación", ("17",)),
)


class Usage(NamedTuple):
    """Una cita concreta: qué clase usa qué obra y con qué etiqueta."""

    part_id: str
    class_id: str
    class_path: str
    class_title: str
    index: int
    label: str
    url: str
    key: str


# --------------------------------------------------------------------------- #
# Identificadores
# --------------------------------------------------------------------------- #


def isbn13_valid(isbn: str) -> bool:
    """Dígito de control de un ISBN-13 (norma ISO 2108)."""
    digits = re.sub(r"[^0-9]", "", isbn or "")
    if len(digits) != 13 or not digits.startswith(("978", "979")):
        return False
    total = sum(int(d) * (1 if i % 2 == 0 else 3) for i, d in enumerate(digits[:12]))
    return (10 - total % 10) % 10 == int(digits[12])


def normalise_isbn(raw: str) -> str:
    """ISBN sin guiones ni espacios."""
    return re.sub(r"[^0-9]", "", raw or "")


def normalise_doi(raw: str) -> str:
    """DOI en minúsculas y sin prefijos de resolución ni puntuación final."""
    doi = (raw or "").strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:", "", doi, flags=re.IGNORECASE)
    doi = doi.rstrip(").,;")
    return doi.lower()


def canonical_locator(entry: Dict[str, Any]) -> Optional[str]:
    """Forma canónica del localizador según el tipo de la entrada."""
    tipo = entry.get("type")
    if tipo == "book":
        isbn = normalise_isbn(entry.get("isbn13") or "")
        return f"https://openlibrary.org/isbn/{isbn}" if isbn else None
    if tipo == "paper":
        doi = normalise_doi(entry.get("doi") or "")
        return f"https://doi.org/{doi}" if doi else None
    url = entry.get("url") or entry.get("locator") or ""
    return url if url.startswith(("https://", "http://")) else None


def derive_identifiers(url: str) -> Dict[str, Optional[str]]:
    """Extrae DOI e ISBN-13 que ya viajan dentro de la propia URL citada.

    No inventa nada: solo lee lo que la URL ya contiene. Un DOI de Springer o de
    SIAM lleva el ISBN-13 en el sufijo; una ficha de editorial suele llevarlo en
    la ruta; un identificador de arXiv tiene DOI canónico asignado por DataCite.
    """
    doi: Optional[str] = None
    isbn: Optional[str] = None

    arxiv = ARXIV_RE.match(url)
    if arxiv:
        doi = normalise_doi(f"10.48550/arXiv.{arxiv.group('id')}")
    else:
        found = DOI_IN_URL_RE.search(url)
        if found:
            doi = normalise_doi(found.group(1))

    for match in ISBN13_IN_TEXT_RE.finditer(url):
        if isbn13_valid(match.group(0)):
            isbn = normalise_isbn(match.group(0))
            break

    if isbn is None and doi:
        for match in ISBN13_IN_TEXT_RE.finditer(doi):
            if isbn13_valid(match.group(0)):
                isbn = normalise_isbn(match.group(0))
                break

    # Un DOI de capítulo (…_28) lleva el ISBN del **libro que lo contiene**, no el de la
    # obra citada: adoptarlo mandaría al lector a otro título. El capítulo se identifica
    # por su DOI y nada más.
    if doi and CHAPTER_DOI_RE.search(doi):
        isbn = None

    return {"doi": doi, "isbn13": isbn}


DOI_IN_TEXT_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>\]`]+")


def dois_in_text(text: str) -> List[str]:
    """DOI que aparecen en un texto, con la puntuación final recortada.

    Los paréntesis forman parte de algunos DOI (``10.1016/0041-5553(64)90137-5``),
    así que solo se recorta el paréntesis de cierre cuando queda desemparejado.
    """
    encontrados = []
    for bruto in DOI_IN_TEXT_RE.findall(text):
        candidato = bruto.rstrip(".,;:")
        while candidato.endswith(")") and candidato.count(")") > candidato.count("("):
            candidato = candidato[:-1].rstrip(".,;:")
        if candidato:
            encontrados.append(normalise_doi(candidato))
    return encontrados


def source_key(url: str) -> str:
    """Clave estable que agrupa las URLs que apuntan a la misma obra."""
    ids = derive_identifiers(url)
    if ids["isbn13"]:
        return f"isbn:{ids['isbn13']}"
    if ids["doi"]:
        return f"doi:{ids['doi']}"
    return f"url:{url.rstrip('/')}"


# --------------------------------------------------------------------------- #
# Etiquetas bibliográficas
# --------------------------------------------------------------------------- #


def _strip_accents(text: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def slugify(text: str, limit: int = 60) -> str:
    """Texto reducido a kebab-case ASCII."""
    base = _strip_accents(text.lower())
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    if len(base) > limit:
        base = base[:limit].rsplit("-", 1)[0]
    return base or "fuente"


def _trim_final_dot(autor: str) -> str:
    """Quita el punto final solo si no es el punto de una inicial.

    «Strang, G.» conserva el punto; «… & Patashnik.» lo pierde, porque ahí el
    punto era el que cerraba la frase de la cita.
    """
    if not autor.endswith("."):
        return autor
    ultimo = autor.rsplit(",", 1)[-1].strip()
    return autor if INITIALS_RE.match(ultimo) else autor[:-1].strip()


def _split_authors(raw: str) -> List[str]:
    """Separa autores respetando «Apellido, N.» como una sola persona."""
    raw = raw.strip()
    if not raw:
        return []
    autores: List[str] = []
    for trozo in re.split(r";|\s&\s|\sy\s|\sand\s", raw):
        trozo = trozo.strip().strip(",").strip()
        if not trozo:
            continue
        acumulado: List[str] = []
        for parte in [p.strip() for p in trozo.split(",") if p.strip()]:
            if acumulado and INITIALS_RE.match(parte):
                acumulado[-1] = f"{acumulado[-1]}, {parte}"
            else:
                acumulado.append(parte)
        autores.extend(acumulado)
    return [_trim_final_dot(a) for a in autores if a]


def parse_label(label: str) -> Dict[str, Any]:
    """Descompone la etiqueta de una cita en autores, título y año.

    Es un análisis de la cadena que ya escribieron las clases; la metadata
    definitiva la fija la autoridad cuando ``refresh-sources`` la resuelve.
    """
    texto = label.strip()
    años = YEAR_RE.findall(texto)
    año = años[-1] if años else None

    cursiva = re.search(r"\*(?P<t>[^*]+)\*", texto)
    if cursiva:
        titulo = cursiva.group("t").strip()
        autores = _split_authors(texto[: cursiva.start()].strip().rstrip(",").strip())
    else:
        titulo = re.split(r"\s+—\s+|\s+–\s+", texto)[0].strip()
        autores = []
    return {"authors": autores, "title": titulo.strip().rstrip(".").strip(), "published": año}


def normalise_title(title: str) -> str:
    """Título comparable: sin acentos, sin puntuación y en minúsculas."""
    base = _strip_accents((title or "").lower())
    base = re.sub(r"[^a-z0-9]+", " ", base)
    return " ".join(base.split())


# --------------------------------------------------------------------------- #
# Áreas: el puente entre la obra y la clase que la cita
# --------------------------------------------------------------------------- #


def _host(url: str) -> str:
    return url.split("//", 1)[-1].split("/", 1)[0].lower()


@functools.lru_cache(maxsize=1)
def load_areas() -> Dict[str, Any]:
    """Vocabulario de áreas y lo que declara cada parte."""
    import yaml

    with AREAS_PATH.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def area_label(slug: str) -> str:
    """Nombre legible de un área; el propio identificador si no está definida."""
    ficha = (load_areas().get("areas") or {}).get(slug) or {}
    return ficha.get("nombre") or slug


def transversal_areas() -> Tuple[str, ...]:
    """Áreas admitidas en cualquier parte (la documentación de la herramienta)."""
    return tuple(load_areas().get("transversales") or ())


def part_areas(part_id: str) -> Dict[str, Tuple[str, ...]]:
    """Área que enseña la parte (``nucleo``) y áreas con las que conecta."""
    ficha = (load_areas().get("partes") or {}).get(part_id) or {}
    return {
        "nucleo": tuple(ficha.get("nucleo") or ()),
        "conexiones": tuple(ficha.get("conexiones") or ()),
    }


def class_areas(class_id: str) -> Tuple[str, ...]:
    """Área que enseña la clase: la que declara, o el núcleo de su parte."""
    propias = content.class_content(class_id).get("areas")
    if propias:
        return tuple(propias)
    part_id = f"{(int(class_id) - 1) // 20:02d}"
    return part_areas(part_id)["nucleo"]


def work_areas(key: str, registry: Optional[Dict[str, Any]] = None) -> Tuple[str, ...]:
    """Áreas que declara cubrir la obra registrada bajo esa clave canónica."""
    registry = registry if registry is not None else load_registry()
    entrada = entries_by_key(registry).get(key) or {}
    return tuple(entrada.get("covers") or ())


class Fit(NamedTuple):
    """Encaje comprobado entre una obra y la clase que la cita."""

    role: str                   # ancla | conexion | herramienta | fuera-de-tema
    areas: Tuple[str, ...]      # áreas que justifican ese encaje
    reason: str                 # frase que se publica en la clase


def citation_fit(class_id: str, key: str, registry: Optional[Dict[str, Any]] = None) -> Fit:
    """Compara el tema de la obra con el de la clase y el de su parte.

    Es la comprobación que sostiene la bibliografía: una obra solo se admite si
    trata el tema de la clase (**ancla**), una conexión que la parte declara, o
    es la documentación de la herramienta que ejecuta el laboratorio.
    """
    part_id = f"{(int(class_id) - 1) // 20:02d}"
    cubre = set(work_areas(key, registry))
    transversales = set(transversal_areas())
    propias = set(class_areas(class_id)) - transversales
    parte = part_areas(part_id)
    conexiones = (set(parte["nucleo"]) | set(parte["conexiones"])) - transversales

    ancla = sorted(cubre & propias)
    if ancla:
        temas = " y ".join(area_label(a) for a in ancla)
        return Fit("ancla", tuple(ancla), f"{temas}: el tema de esta clase")

    enlace = sorted(cubre & conexiones)
    if enlace:
        temas = " y ".join(area_label(a) for a in enlace)
        return Fit("conexion", tuple(enlace), f"{temas}: conexión declarada de esta parte")

    if cubre & transversales:
        return Fit(
            "herramienta",
            tuple(sorted(cubre & transversales)),
            "documentación de la herramienta que ejecuta el laboratorio",
        )

    temas = ", ".join(area_label(a) for a in sorted(cubre)) or "sin tema declarado"
    return Fit("fuera-de-tema", tuple(sorted(cubre)), f"{temas}: fuera del tema de esta parte")


def locator_note(key: str, registry: Optional[Dict[str, Any]] = None) -> str:
    """Estado del localizador de la obra, tal y como lo dejó la resolución en red."""
    registry = registry if registry is not None else load_registry()
    entrada = entries_by_key(registry).get(key)
    if not entrada:
        return "sin entrada en el registro"
    if entrada.get("isbn13"):
        localizador, participio = f"ISBN-13 `{entrada['isbn13']}`", "verificado"
    elif entrada.get("doi"):
        localizador, participio = f"DOI `{entrada['doi']}`", "verificado"
    else:
        localizador, participio = "URL de la fuente primaria", "comprobada"
    if entrada.get("status") != "verificada":
        return f"{localizador}, pendiente de resolver"
    autoridad = (entrada.get("authority") or "su autoridad").split(" (")[0]
    return f"{localizador} {participio} en {autoridad} ({entrada.get('accessed')})"


def reference_line(raw: str, class_id: str, registry: Optional[Dict[str, Any]] = None) -> str:
    """Línea de referencia tal y como se publica en la clase.

    Declara **por qué esa obra está en esa clase** —el área que comparten— y en
    qué estado quedó su localizador. Nada de eso se escribe a mano: sale del
    registro y del vocabulario de áreas.
    """
    match = REF_RE.match(raw.strip())
    if not match:
        return raw.strip()
    key = source_key(match.group("url"))
    fit = citation_fit(class_id, key, registry)
    return f"{raw.strip()} — {fit.reason} · {locator_note(key, registry)}."


def class_block(class_id: str, class_title: str = "") -> List[str]:
    """Bloque de bibliografía de una clase, con el porqué de cada obra."""
    registro = content.class_content(class_id)
    registry = load_registry() if REGISTRY_PATH.exists() else {"entries": []}
    return [reference_line(r, class_id, registry) for r in (registro.get("referencias") or [])]


# --------------------------------------------------------------------------- #
# Usos reales en el repositorio
# --------------------------------------------------------------------------- #


@functools.lru_cache(maxsize=1)
def usages() -> Tuple[Usage, ...]:
    """Todas las citas del programa, en orden de clase."""
    salida: List[Usage] = []
    for clase in curriculum.classes():
        registro = content.class_content(clase["id"])
        ruta = curriculum.class_dir(clase).relative_to(ROOT).as_posix()
        for indice, cruda in enumerate(registro.get("referencias") or []):
            match = REF_RE.match(cruda.strip())
            if not match:
                raise ValueError(f"referencia sin enlace en la clase {clase['id']}: {cruda}")
            url = match.group("url")
            salida.append(
                Usage(
                    part_id=clase["part"],
                    class_id=clase["id"],
                    class_path=ruta,
                    class_title=clase["title"],
                    index=indice,
                    label=match.group("label").strip(),
                    url=url,
                    key=source_key(url),
                )
            )
    return tuple(salida)


def sources_used() -> Dict[str, Dict[str, Any]]:
    """Obras distintas usadas por las clases, agrupadas por clave canónica."""
    agrupadas: Dict[str, Dict[str, Any]] = {}
    for uso in usages():
        ficha = agrupadas.setdefault(
            uso.key,
            {"key": uso.key, "urls": [], "labels": [], "used_in": [], "classes": [], "parts": []},
        )
        if uso.url not in ficha["urls"]:
            ficha["urls"].append(uso.url)
        if uso.label not in ficha["labels"]:
            ficha["labels"].append(uso.label)
        if uso.class_path not in ficha["used_in"]:
            ficha["used_in"].append(uso.class_path)
            ficha["classes"].append(uso.class_id)
        if uso.part_id not in ficha["parts"]:
            ficha["parts"].append(uso.part_id)
    return agrupadas


def make_id(ficha: Dict[str, Any], tomados: Optional[Set[str]] = None) -> str:
    """Identificador kebab-case estable a partir de la cita más completa."""
    tomados = tomados if tomados is not None else set()
    etiqueta = max(ficha["labels"], key=len)
    datos = parse_label(etiqueta)
    apellido = datos["authors"][0].split(",")[0] if datos["authors"] else ""
    partes = [slugify(apellido, 24) if apellido.strip() else "", slugify(datos["title"], 48)]
    base = "-".join(p for p in partes if p) or slugify(ficha["urls"][0], 40)
    candidato = base
    sufijo = 2
    while candidato in tomados:
        candidato = f"{base}-{sufijo}"
        sufijo += 1
    tomados.add(candidato)
    return candidato


# --------------------------------------------------------------------------- #
# Registro
# --------------------------------------------------------------------------- #


def load_registry(path: Path = REGISTRY_PATH) -> Dict[str, Any]:
    """Carga ``sources/bibliography.json`` (o un registro vacío si no existe)."""
    if not path.exists():
        return {
            "schema_version": SCHEMA_VERSION,
            "verified_on": None,
            "policy": POLICY,
            "entries": [],
        }
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def dump_registry(registry: Dict[str, Any], path: Path = REGISTRY_PATH) -> None:
    """Escribe el registro con las entradas ordenadas por identificador."""
    path.parent.mkdir(parents=True, exist_ok=True)
    registry["entries"] = sorted(registry.get("entries", []), key=lambda e: e["id"])
    texto = json.dumps(registry, ensure_ascii=False, indent=2)
    path.write_text(texto + "\n", encoding="utf-8", newline="\n")


def entries_by_key(registry: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Entradas del registro indexadas por su clave canónica."""
    return {e["key"]: e for e in registry.get("entries", [])}


def stage_of_part(part_id: str) -> Optional[Tuple[str, str]]:
    """Etapa a la que pertenece una parte."""
    for numero, nombre, partes in STAGES:
        if part_id in partes:
            return numero, nombre
    return None


def iter_class_blocks() -> Iterator[Tuple[str, Tuple[str, ...]]]:
    """Bloque de fuentes de cada clase, en orden de programa."""
    for clase in curriculum.classes():
        yield clase["id"], tuple(class_block(clase["id"], clase["title"]))


def registry_stats(registry: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Cifras del registro. **Estas** son las que publica el README."""
    registry = registry if registry is not None else load_registry()
    entradas = registry.get("entries", [])
    usos = usages()
    bloques = [bloque for _, bloque in iter_class_blocks()]
    verificadas = sum(1 for e in entradas if e.get("status") == "verificada")
    en_registro = set(entries_by_key(registry))
    usadas = set(sources_used())

    papeles: Dict[str, int] = {"ancla": 0, "conexion": 0, "herramienta": 0, "fuera-de-tema": 0}
    ancladas: Set[str] = set()
    for uso in usos:
        encaje = citation_fit(uso.class_id, uso.key, registry)
        papeles[encaje.role] = papeles.get(encaje.role, 0) + 1
        if encaje.role == "ancla":
            ancladas.add(uso.class_id)

    return {
        "papeles": papeles,
        "clases_ancladas": len(ancladas),
        "areas": len((load_areas().get("areas") or {})),
        "obras": len(entradas),
        "usos": len(usos),
        "clases": len(bloques),
        "clases_con_bloque": sum(1 for b in bloques if b),
        "bloques_distintos": len(set(bloques)),
        "obras_usadas": len(usadas),
        "cobertura_%": round(100 * len(usadas & en_registro) / len(usadas), 1) if usadas else 0.0,
        "verificadas": verificadas,
        "pendientes": len(entradas) - verificadas,
        "verificadas_%": round(100 * verificadas / len(entradas), 1) if entradas else 0.0,
        "con_doi": sum(1 for e in entradas if e.get("doi")),
        "con_isbn13": sum(1 for e in entradas if e.get("isbn13")),
        "tipos": {t: sum(1 for e in entradas if e.get("type") == t) for t in TIPOS},
        "verified_on": registry.get("verified_on"),
    }


def leading_work(registry: Dict[str, Any], part_ids: Tuple[str, ...]) -> Optional[Dict[str, Any]]:
    """Obra rectora de una etapa: la más citada por sus clases."""
    conteo: Dict[str, int] = {}
    for uso in usages():
        if uso.part_id in part_ids:
            conteo[uso.key] = conteo.get(uso.key, 0) + 1
    if not conteo:
        return None
    catalogo = entries_by_key(registry)
    for clave, veces in sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0])):
        entrada = catalogo.get(clave)
        if entrada:
            return {"entry": entrada, "count": veces}
    return None
