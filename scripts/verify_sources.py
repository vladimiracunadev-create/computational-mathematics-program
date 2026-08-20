"""Verificador **offline** del registro de fuentes. Corre en CI y bloquea.

No toca la red: solo compara el registro con lo que las clases citan de verdad.
Un verificador que depende de la red es un verificador que acaba ignorándose.

Comprueba que:

- ``sources/bibliography.json`` parsea y cumple el esquema declarado;
- todo ``book`` lleva ISBN-13 con dígito de control válido, y todo ``paper``, DOI;
- el ``locator`` coincide con la forma canónica de su tipo;
- toda obra usada en una clase existe en el registro, y todo DOI escrito en el cuerpo
  de una clase también;
- ninguna entrada del registro queda sin usar;
- **cada obra declara qué áreas cubre** y esas áreas existen en `sources/areas.yaml`;
- **cada clase se ancla**: cita al menos una obra del área que la clase enseña;
- **ninguna cita queda fuera de tema**: toda obra citada cubre el área de la parte o
  una de sus conexiones declaradas, salvo la documentación de la herramienta;
- las cifras que publica el README coinciden con el recuento del registro.

    python scripts/verify_sources.py           # verifica (modo CI)
    python scripts/verify_sources.py --sync     # recalcula usos y cifras del README
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import content, curriculum, sources  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

README = ROOT / "README.md"
MARCA_INICIO = "<!-- fuentes:inicio -->"
MARCA_FIN = "<!-- fuentes:fin -->"
FECHA_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

CAMPOS_OBLIGATORIOS = ("id", "key", "type", "title", "locator", "authority", "used_in", "status")

# Quién responde por cada localizador cuando no es un ISBN ni un DOI.
AUTORIDADES = {
    "standards.ieee.org": "IEEE Standards Association",
    "ieeexplore.ieee.org": "IEEE Xplore",
    "www.bipm.org": "Bureau International des Poids et Mesures",
    "www.nist.gov": "National Institute of Standards and Technology",
    "pages.nist.gov": "National Institute of Standards and Technology",
    "cwe.mitre.org": "MITRE Corporation",
    "peps.python.org": "Python Software Foundation",
    "docs.python.org": "Python Software Foundation",
    "docs.scipy.org": "SciPy developers",
    "docs.sympy.org": "SymPy Development Team",
    "docs.jax.dev": "JAX developers",
    "numpy.org": "NumPy developers",
    "pytorch.org": "PyTorch Foundation",
    "arxiv.org": "arXiv (Cornell University)",
    "jmlr.org": "Journal of Machine Learning Research",
    "proceedings.mlr.press": "Proceedings of Machine Learning Research",
    "projects.iq.harvard.edu": "Harvard University",
    "math.mit.edu": "Massachusetts Institute of Technology",
    "dspace.mit.edu": "MIT Libraries",
    "mitpress.mit.edu": "The MIT Press",
    "web.stanford.edu": "Stanford University",
    "www-cs-faculty.stanford.edu": "Stanford University",
    "oeis.org": "OEIS Foundation",
    "encyclopediaofmath.org": "European Mathematical Society",
    "mathworld.wolfram.com": "Wolfram Research",
    "mathshistory.st-andrews.ac.uk": "University of St Andrews",
    "www.deeplearningbook.org": "sitio oficial de los autores",
    "hastie.su.domains": "sitio oficial de los autores",
    "linear.axler.net": "sitio oficial del autor",
    "gaussianprocess.org": "sitio oficial de los autores",
    "probml.github.io": "sitio oficial del autor",
    "otexts.com": "sitio oficial de los autores",
    "numerical.recipes": "Numerical Recipes Software",
}


def _host(url: str) -> str:
    return url.split("//", 1)[-1].split("/", 1)[0].lower()


def _authority(entry: Dict[str, Any]) -> str:
    if entry.get("isbn13"):
        return "International ISBN Agency (comprobado vía Open Library)"
    if entry.get("doi"):
        return "Agencia de registro DOI (comprobada vía doi.org)"
    host = _host(entry.get("url") or entry.get("locator") or "")
    return AUTORIDADES.get(host, host or "desconocida")


def _tipo(ficha: Dict[str, Any]) -> str:
    ids = sources.derive_identifiers(ficha["urls"][0])
    if ids["isbn13"]:
        return "book"
    if ids["doi"]:
        return "paper"
    if _host(ficha["urls"][0]) in sources.STANDARD_HOSTS:
        return "standard"
    return "reference"


def esqueleto(ficha: Dict[str, Any], tomados: set, hoy: str) -> Dict[str, Any]:
    """Entrada nueva a partir de lo que la propia cita ya contiene.

    Nace ``pendiente``: nada se da por bueno hasta que ``refresh-sources``
    resuelve el localizador contra su autoridad.
    """
    etiqueta = max(ficha["labels"], key=len)
    datos = sources.parse_label(etiqueta)
    ids = sources.derive_identifiers(ficha["urls"][0])
    entrada: Dict[str, Any] = {
        "id": sources.make_id(ficha, tomados),
        "key": ficha["key"],
        "type": _tipo(ficha),
        "authors": datos["authors"],
        "title": datos["title"],
        "published": datos["published"],
        "url": ficha["urls"][0],
    }
    if ids["isbn13"]:
        entrada["isbn13"] = ids["isbn13"]
    if ids["doi"]:
        entrada["doi"] = ids["doi"]
    entrada["locator"] = sources.canonical_locator(entrada) or ficha["urls"][0]
    entrada["authority"] = _authority(entrada)
    entrada["accessed"] = hoy
    entrada["used_in"] = list(ficha["used_in"])
    entrada["covers"] = []
    entrada["status"] = "pendiente"
    entrada["note"] = "sin resolver todavía: ejecuta `python scripts/refresh_sources.py`"
    return entrada


# --------------------------------------------------------------------------- #
# Bloque del README
# --------------------------------------------------------------------------- #


def obra_rectora(registry: Dict[str, Any], part_id: str):
    """Obra más citada por una parte **como fuente de su propio tema**.

    Se descartan las citas de conexión y la documentación de la herramienta: la
    obra rectora de una parte es la que sostiene lo que la parte enseña.
    """
    conteo: Dict[str, int] = {}
    for uso in sources.usages():
        if uso.part_id != part_id:
            continue
        if sources.citation_fit(uso.class_id, uso.key, registry).role != "ancla":
            continue
        conteo[uso.key] = conteo.get(uso.key, 0) + 1
    catalogo = sources.entries_by_key(registry)
    for clave, veces in sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0])):
        if clave in catalogo:
            return catalogo[clave], veces
    return None, 0


def _firma(entrada: Dict[str, Any]) -> str:
    autores = entrada.get("authors") or []
    if not autores:
        return entrada.get("authority", "").split(" (")[0]
    firma = autores[0].split(",")[0]
    return f"{firma} et al." if len(autores) > 1 else firma


def bloque_readme(registry: Dict[str, Any]) -> str:
    cifras = sources.registry_stats(registry)
    fecha = cifras["verified_on"] or "sin resolver"
    tipos = cifras["tipos"]

    lineas = [
        MARCA_INICIO,
        "",
        "> Bloque generado por `python scripts/verify_sources.py --sync` a partir de las "
        "citas de las clases. No se escribe a mano.",
        "",
        f"**{cifras['obras']} obras reales** —{tipos['book']} libros, {tipos['paper']} "
        f"artículos, {tipos['standard']} normas y {tipos['reference']} referencias— "
        f"sostienen las **{cifras['usos']} citas** de las {cifras['clases']} clases. "
        f"Las **{cifras['clases_ancladas']} de {cifras['clases']}** clases citan al menos "
        f"una obra del área que enseñan. De los localizadores, {cifras['verificadas']} "
        f"están resueltos contra su autoridad y {cifras['pendientes']} siguen pendientes "
        f"(última resolución en red: {fecha}).",
        "",
        "Así se ve la bibliografía de una clase —"
        "[028 · IEEE 754: estructura de un float]"
        "(classes/part-01-aritmetica-computacional-y-representacion-numerica/"
        "028-ieee-754-estructura-de-un-float/README.md)—, "
        "generada con el porqué de cada obra y el estado de su localizador:",
        "",
    ]
    for linea in sources.class_block("028"):
        lineas.append(f"> - {linea}")
    lineas += [
        "",
        "| Parte | Lo que enseña | Obra rectora de la parte | Citas |",
        "|---|---|---|---:|",
    ]
    for parte in curriculum.parts():
        areas = sources.part_areas(parte["id"])
        entrada, veces = obra_rectora(registry, parte["id"])
        rectora = (
            f"{_firma(entrada)} — *{entrada['title']}* [↗]({entrada['locator']})"
            if entrada else "—"
        )
        citas = sum(1 for uso in sources.usages() if uso.part_id == parte["id"])
        ensena = " · ".join(sources.area_label(a) for a in areas["nucleo"])
        lineas.append(
            f"| **{parte['id']}** {parte['title']} | {ensena} | {rectora} | {citas} |"
        )
    lineas += [
        "",
        f"Detalle clase por clase en [docs/BIBLIOGRAPHY.md](docs/BIBLIOGRAPHY.md) · "
        f"localizador y estado de cada obra en "
        f"[sources/bibliography.json](sources/bibliography.json) · "
        f"vocabulario de las {cifras['areas']} áreas en "
        f"[sources/areas.yaml](sources/areas.yaml).",
        "",
        MARCA_FIN,
    ]
    return "\n".join(lineas)


def _reemplaza_bloque(texto: str, bloque: str) -> str:
    inicio = texto.index(MARCA_INICIO)
    fin = texto.index(MARCA_FIN) + len(MARCA_FIN)
    return texto[:inicio] + bloque + texto[fin:]


# --------------------------------------------------------------------------- #
# Comprobaciones
# --------------------------------------------------------------------------- #


def comprueba(registry: Dict[str, Any], errores: List[str]) -> None:
    if registry.get("schema_version") != sources.SCHEMA_VERSION:
        errores.append(f"schema_version debe ser {sources.SCHEMA_VERSION}")
    if not registry.get("policy"):
        errores.append("el registro no declara su política")
    verified_on = registry.get("verified_on")
    if verified_on is not None and not FECHA_RE.match(str(verified_on)):
        errores.append(f"verified_on no es una fecha AAAA-MM-DD: {verified_on!r}")

    entradas = registry.get("entries", [])
    if not entradas:
        errores.append("el registro no tiene entradas")
        return

    ids, claves = set(), set()
    for entrada in entradas:
        etiqueta = entrada.get("id", "<sin id>")
        for campo in CAMPOS_OBLIGATORIOS:
            if not entrada.get(campo):
                errores.append(f"{etiqueta}: falta el campo obligatorio {campo}")
        if not ID_RE.match(str(entrada.get("id", ""))):
            errores.append(f"{etiqueta}: el id no es kebab-case")
        if entrada.get("id") in ids:
            errores.append(f"{etiqueta}: id duplicado")
        ids.add(entrada.get("id"))
        if entrada.get("key") in claves:
            errores.append(f"{etiqueta}: clave canónica duplicada ({entrada.get('key')})")
        claves.add(entrada.get("key"))

        tipo = entrada.get("type")
        if tipo not in sources.TIPOS:
            errores.append(f"{etiqueta}: tipo inválido {tipo!r}")
        if entrada.get("status") not in sources.ESTADOS:
            errores.append(f"{etiqueta}: estado inválido {entrada.get('status')!r}")
        if not FECHA_RE.match(str(entrada.get("accessed", ""))):
            errores.append(f"{etiqueta}: accessed no es una fecha AAAA-MM-DD")

        if tipo == "book" and not sources.isbn13_valid(entrada.get("isbn13") or ""):
            errores.append(f"{etiqueta}: libro sin ISBN-13 con dígito de control válido")
        if tipo == "paper" and not (entrada.get("doi") or "").strip():
            errores.append(f"{etiqueta}: artículo sin DOI")
        if entrada.get("isbn13") and not sources.isbn13_valid(entrada["isbn13"]):
            errores.append(f"{etiqueta}: ISBN-13 con dígito de control inválido")

        canonico = sources.canonical_locator(entrada)
        if canonico is None:
            errores.append(f"{etiqueta}: no se puede formar un localizador canónico")
        elif entrada.get("locator") != canonico:
            errores.append(
                f"{etiqueta}: el locator no es canónico "
                f"({entrada.get('locator')!r} debería ser {canonico!r})"
            )
        locator = str(entrada.get("locator", ""))
        if not locator.startswith("https://"):
            # Excepción declarada, nunca silenciosa: si la fuente primaria no
            # sirve https, la entrada se queda pendiente y lo dice por escrito.
            if not locator.startswith("http://"):
                errores.append(f"{etiqueta}: el locator no es una URL")
            elif entrada.get("status") != "pendiente" or "https" not in (entrada.get("note") or ""):
                errores.append(
                    f"{etiqueta}: locator sin https; debe quedar 'pendiente' y explicarlo en note"
                )

    usadas = sources.sources_used()
    sin_declarar = sorted(set(usadas) - claves)
    if sin_declarar:
        errores.append(
            f"{len(sin_declarar)} obra(s) citadas en clase y ausentes del registro: "
            f"{sin_declarar[:5]}"
        )
    sin_usar = sorted(claves - set(usadas))
    if sin_usar:
        errores.append(f"{len(sin_usar)} entrada(s) del registro sin uso en ninguna clase: {sin_usar[:5]}")

    for entrada in entradas:
        ficha = usadas.get(entrada.get("key"))
        if ficha and sorted(entrada.get("used_in", [])) != sorted(ficha["used_in"]):
            errores.append(
                f"{entrada['id']}: used_in desfasado "
                f"({len(entrada.get('used_in', []))} rutas frente a {len(ficha['used_in'])} usos reales)"
            )


def comprueba_areas(errores: List[str]) -> None:
    """El vocabulario de áreas y lo que declara cada parte."""
    datos = sources.load_areas()
    if datos.get("schema_version") != sources.SCHEMA_VERSION:
        errores.append(f"areas.yaml: schema_version debe ser {sources.SCHEMA_VERSION}")
    if not datos.get("politica"):
        errores.append("areas.yaml: no declara su política")

    vocabulario = datos.get("areas") or {}
    if not vocabulario:
        errores.append("areas.yaml: no define ningún área")
    for slug, ficha in vocabulario.items():
        if not ID_RE.match(slug):
            errores.append(f"areas.yaml: el área {slug!r} no es kebab-case")
        if not (ficha or {}).get("nombre") or not (ficha or {}).get("definicion"):
            errores.append(f"areas.yaml: el área {slug!r} no declara nombre y definición")

    transversales = set(datos.get("transversales") or ())
    for slug in sorted(transversales - set(vocabulario)):
        errores.append(f"areas.yaml: área transversal desconocida {slug!r}")

    partes = datos.get("partes") or {}
    for parte in curriculum.parts():
        ficha = partes.get(parte["id"])
        if not ficha:
            errores.append(f"areas.yaml: la parte {parte['id']} no declara sus áreas")
            continue
        nucleo, conexiones = set(ficha.get("nucleo") or ()), set(ficha.get("conexiones") or ())
        if not nucleo:
            errores.append(f"areas.yaml: la parte {parte['id']} no declara núcleo")
        if nucleo <= transversales:
            errores.append(f"areas.yaml: el núcleo de la parte {parte['id']} solo tiene áreas transversales")
        for slug in sorted((nucleo | conexiones) - set(vocabulario)):
            errores.append(f"areas.yaml: la parte {parte['id']} declara un área desconocida: {slug}")
        for slug in sorted(nucleo & conexiones):
            errores.append(f"areas.yaml: la parte {parte['id']} repite {slug} en núcleo y conexiones")

    for clase in curriculum.classes():
        propias = content.class_content(clase["id"]).get("areas") or ()
        for slug in propias:
            if slug not in vocabulario:
                errores.append(f"la clase {clase['id']} declara un área desconocida: {slug}")
        if propias and set(propias) <= transversales:
            errores.append(f"la clase {clase['id']} solo declara áreas transversales")


def comprueba_covers(registry: Dict[str, Any], errores: List[str]) -> None:
    """Toda obra dice de qué trata, y lo dice con el vocabulario común."""
    vocabulario = set((sources.load_areas().get("areas") or {}))
    for entrada in registry.get("entries", []):
        cubre = entrada.get("covers") or []
        if not cubre:
            errores.append(f"{entrada['id']}: no declara qué áreas cubre (campo covers)")
            continue
        if not isinstance(cubre, list):
            errores.append(f"{entrada['id']}: covers debe ser una lista de áreas")
            continue
        for slug in cubre:
            if slug not in vocabulario:
                errores.append(f"{entrada['id']}: área desconocida en covers: {slug}")
        if len(set(cubre)) != len(cubre):
            errores.append(f"{entrada['id']}: covers repite un área")


def comprueba_pertinencia(registry: Dict[str, Any], errores: List[str]) -> None:
    """El cruce que sostiene la bibliografía: la obra trata lo que la clase enseña."""
    sin_bloque: List[str] = []
    sin_ancla: List[str] = []
    for clase in curriculum.classes():
        citas = content.class_content(clase["id"]).get("referencias") or []
        if not citas:
            sin_bloque.append(clase["id"])
            continue
        anclada = False
        for cruda in citas:
            match = sources.REF_RE.match(cruda.strip())
            if not match:
                errores.append(f"la clase {clase['id']} tiene una referencia sin enlace: {cruda[:60]}")
                continue
            clave = sources.source_key(match.group("url"))
            encaje = sources.citation_fit(clase["id"], clave, registry)
            anclada = anclada or encaje.role == "ancla"
            if encaje.role == "fuera-de-tema":
                errores.append(
                    f"la clase {clase['id']} cita una obra fuera de tema: "
                    f"{sources.parse_label(match.group('label'))['title']!r} "
                    f"cubre [{', '.join(encaje.areas) or 'nada'}] y la parte "
                    f"{clase['part']} no declara ninguna de esas áreas"
                )
        if not anclada:
            sin_ancla.append(clase["id"])
    if sin_bloque:
        errores.append(f"{len(sin_bloque)} clase(s) sin bibliografía: {sin_bloque[:5]}")
    if sin_ancla:
        errores.append(
            f"{len(sin_ancla)} clase(s) sin ninguna obra del área que enseñan "
            f"(añade una fuente del tema, no vale la documentación de la herramienta): {sin_ancla[:5]}"
        )


def comprueba_dois_del_cuerpo(registry: Dict[str, Any], errores: List[str]) -> None:
    """Todo DOI que aparece escrito en una clase tiene que estar en el registro."""
    registrados = {
        sources.normalise_doi(e["doi"]) for e in registry.get("entries", []) if e.get("doi")
    }
    huerfanos: Dict[str, str] = {}
    for archivo in sorted((ROOT / "classes").rglob("*.md")):
        texto = archivo.read_text(encoding="utf-8")
        for doi in sources.dois_in_text(texto):
            if doi not in registrados:
                huerfanos.setdefault(doi, archivo.relative_to(ROOT).as_posix())
    for doi, donde in sorted(huerfanos.items()):
        errores.append(f"DOI citado en {donde} y ausente del registro: {doi}")


def comprueba_readme(registry: Dict[str, Any], errores: List[str]) -> None:
    texto = README.read_text(encoding="utf-8")
    if MARCA_INICIO not in texto or MARCA_FIN not in texto:
        errores.append("README.md no tiene el bloque generado de fuentes")
        return
    esperado = bloque_readme(registry)
    actual = texto[texto.index(MARCA_INICIO) : texto.index(MARCA_FIN) + len(MARCA_FIN)]
    if actual != esperado:
        errores.append(
            "las cifras de fuentes del README no coinciden con el registro "
            "(ejecuta `python scripts/verify_sources.py --sync`)"
        )
    if "sources/bibliography.json" not in texto:
        errores.append("README.md no enlaza el registro de fuentes")


# --------------------------------------------------------------------------- #


def sincroniza(registry: Dict[str, Any]) -> Dict[str, Any]:
    hoy = date.today().isoformat()
    usadas = sources.sources_used()
    catalogo = sources.entries_by_key(registry)
    tomados = {e["id"] for e in registry.get("entries", [])}
    nuevas = 0
    for clave, ficha in usadas.items():
        entrada = catalogo.get(clave)
        if entrada is None:
            registry.setdefault("entries", []).append(esqueleto(ficha, tomados, hoy))
            nuevas += 1
        else:
            # Los campos bibliográficos se derivan de la cita de la clase; la
            # resolución en red solo escribe estado, nota, localizador y fechas.
            datos = sources.parse_label(max(ficha["labels"], key=len))
            entrada["authors"] = datos["authors"]
            entrada["title"] = datos["title"]
            entrada["published"] = datos["published"]
            entrada["used_in"] = list(ficha["used_in"])
    # Una obra que ya no cita ninguna clase sale del registro: el registro describe
    # lo que el programa usa hoy, no lo que usó alguna vez.
    sobrantes = [e for e in registry.get("entries", []) if e["key"] not in usadas]
    if sobrantes:
        registry["entries"] = [e for e in registry["entries"] if e["key"] in usadas]
        for entrada in sobrantes:
            print(f"  · retirada del registro (ya no se cita): {entrada['id']}")
    registry.setdefault("schema_version", sources.SCHEMA_VERSION)
    registry.setdefault("verified_on", None)
    registry["policy"] = sources.POLICY
    print(f"  · {nuevas} entrada(s) nuevas, {len(usadas)} obras usadas en total")
    sources.dump_registry(registry)

    texto = README.read_text(encoding="utf-8")
    if MARCA_INICIO in texto and MARCA_FIN in texto:
        nuevo = _reemplaza_bloque(texto, bloque_readme(registry))
        if nuevo != texto:
            README.write_text(nuevo, encoding="utf-8", newline="\n")
            print("  · README.md actualizado con las cifras del registro")
    else:
        print("  ! README.md todavía no tiene las marcas <!-- fuentes:inicio --> / <!-- fuentes:fin -->")
    return registry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync", action="store_true",
                        help="recalcula used_in y las cifras del README a partir de las clases")
    parser.add_argument("--json", action="store_true", help="imprime las cifras en JSON")
    args = parser.parse_args()

    if not sources.REGISTRY_PATH.exists() and not args.sync:
        print(f"✗ falta {sources.REGISTRY_PATH.relative_to(ROOT)} "
              f"(créalo con `python scripts/verify_sources.py --sync`)")
        return 1

    registry = sources.load_registry()
    if args.sync:
        print("Sincronizando el registro de fuentes con las clases…")
        registry = sincroniza(registry)
        registry = sources.load_registry()

    errores: List[str] = []
    print("Verificando el registro de fuentes (offline)…")
    comprueba(registry, errores)
    comprueba_areas(errores)
    comprueba_covers(registry, errores)
    comprueba_pertinencia(registry, errores)
    comprueba_dois_del_cuerpo(registry, errores)
    comprueba_readme(registry, errores)

    cifras = sources.registry_stats(registry)
    if args.json:
        print(json.dumps(cifras, ensure_ascii=False, indent=2))

    if errores:
        print(f"\n{len(errores)} problema(s):\n")
        for problema in errores[:60]:
            print(f"  ✗ {problema}")
        if len(errores) > 60:
            print(f"  … y {len(errores) - 60} más")
        return 1

    total_clases = len(list(curriculum.classes()))
    print(
        f"\nOK: {cifras['obras']} obras registradas para {cifras['usos']} citas en "
        f"{total_clases} clases · cobertura {cifras['cobertura_%']} % · "
        f"{cifras['verificadas']} verificadas / {cifras['pendientes']} pendientes · "
        f"{cifras['bloques_distintos']} bloques de fuentes distintos."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
