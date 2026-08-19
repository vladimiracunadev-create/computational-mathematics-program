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
    "use_role",
    "use_note",
    "class_block",
    "load_registry",
    "dump_registry",
    "entries_by_key",
    "registry_stats",
    "leading_work",
    "stage_of_part",
]

REGISTRY_PATH = ROOT / "sources" / "bibliography.json"
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

# Documentación de las herramientas que ejecutan los laboratorios.
DOC_HOSTS = frozenset({
    "docs.python.org",
    "docs.scipy.org",
    "docs.sympy.org",
    "docs.jax.dev",
    "numpy.org",
    "pytorch.org",
    "peps.python.org",
})

# Cursos abiertos, notas de clase y divulgación: exposición alternativa del tema.
COURSE_HOSTS = frozenset({
    "projects.iq.harvard.edu",
    "math.mit.edu",
    "dspace.mit.edu",
    "www.3blue1brown.com",
    "www.mathpop.com",
    "distill.pub",
    "colah.github.io",
    "jalammar.github.io",
    "karpathy.ai",
    "neuralnetworksanddeeplearning.com",
    "mathworld.wolfram.com",
    "encyclopediaofmath.org",
    "mathshistory.st-andrews.ac.uk",
    "oeis.org",
    "transformer-circuits.pub",
    "rockt.ai",
    "0.30000000000000004.com",
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

    return {"doi": doi, "isbn13": isbn}


DOI_IN_TEXT_RE = re.compile(r"10\.\d{4,9}/[^\s\"'<>\]]+")


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
# Uso declarado en cada clase
# --------------------------------------------------------------------------- #


def _host(url: str) -> str:
    return url.split("//", 1)[-1].split("/", 1)[0].lower()


def use_role(url: str, label: str = "") -> str:
    """Papel que la clase asigna a la fuente, deducido de su naturaleza.

    Se decide con lo que la cita ya contiene —sede, identificador y forma de la
    etiqueta— y nunca con una suposición sobre el contenido de la obra.
    """
    host = _host(url)
    ids = derive_identifiers(url)
    if host in DOC_HOSTS:
        return "documentación de la herramienta que ejecuta el laboratorio"
    if host in STANDARD_HOSTS:
        return "referencia normativa consultada"
    if host in COURSE_HOSTS:
        return "exposición alternativa del tema"
    if ids["isbn13"]:
        return "desarrollo formal del tema"
    if ids["doi"]:
        return "artículo de origen consultado"
    if "*" in label:  # la etiqueta cita una obra con título propio
        return "obra de referencia consultada"
    return "lectura de apoyo"


def use_note(url: str, class_title: str, label: str = "") -> str:
    """Frase que declara **el uso que esta clase hace** de esta fuente."""
    return f"{use_role(url, label)} en «{class_title}»"


def reference_line(raw: str, class_title: str) -> str:
    """Línea de referencia tal y como se publica en la clase, con su uso."""
    match = REF_RE.match(raw.strip())
    if not match:
        return raw.strip()
    uso = use_note(match.group("url"), class_title, match.group("label"))
    return f"{raw.strip()} — *uso:* {uso}."


def class_block(class_id: str, class_title: str) -> List[str]:
    """Bloque de fuentes completo de una clase, con el uso de cada obra."""
    registro = content.class_content(class_id)
    return [reference_line(r, class_title) for r in (registro.get("referencias") or [])]


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

    return {
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
