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
- ningún bloque de fuentes se repite entre clases;
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

from computational_math import curriculum, sources  # noqa: E402

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
    entrada["status"] = "pendiente"
    entrada["note"] = "sin resolver todavía: ejecuta `python scripts/refresh_sources.py`"
    return entrada


# --------------------------------------------------------------------------- #
# Bloque del README
# --------------------------------------------------------------------------- #


def bloque_readme(registry: Dict[str, Any]) -> str:
    cifras = sources.registry_stats(registry)
    fecha = cifras["verified_on"] or "sin resolver"
    lineas = [
        MARCA_INICIO,
        "",
        "> Cifras generadas por `python scripts/verify_sources.py --sync`. No se escriben a mano.",
        "",
        "| Métrica | Valor |",
        "|---|---:|",
        f"| Obras en el registro | **{cifras['obras']}** |",
        f"| Citas en las clases | {cifras['usos']} |",
        f"| Clases con bloque de fuentes | {cifras['clases_con_bloque']} de {cifras['clases']} |",
        f"| Bloques de fuentes distintos | {cifras['bloques_distintos']} |",
        f"| Cobertura del registro | **{cifras['cobertura_%']} %** |",
        f"| Localizador resuelto contra su autoridad | {cifras['verificadas']} "
        f"({cifras['verificadas_%']} %) |",
        f"| Pendientes de resolver | {cifras['pendientes']} |",
        f"| Entradas con DOI | {cifras['con_doi']} |",
        f"| Entradas con ISBN-13 | {cifras['con_isbn13']} |",
        f"| Última resolución en red | {fecha} |",
        "",
        "| Etapa | Obra rectora | Citas en la etapa | Localizador |",
        "|---|---|---:|---|",
    ]
    for numero, nombre, partes in sources.STAGES:
        rectora = sources.leading_work(registry, partes)
        if not rectora:
            continue
        entrada = rectora["entry"]
        autores = entrada.get("authors") or []
        firma = autores[0].split(",")[0] if autores else entrada.get("authority", "")
        if len(autores) > 1:
            firma = f"{firma} et al."
        lineas.append(
            f"| **{numero} — {nombre}** | {firma} — *{entrada['title']}* | "
            f"{rectora['count']} | [{entrada['type']}]({entrada['locator']}) |"
        )
    lineas += [
        "",
        f"Registro completo en [`sources/bibliography.json`](sources/bibliography.json): "
        f"{cifras['obras']} obras, "
        f"{cifras['tipos']['book']} libros, {cifras['tipos']['paper']} artículos, "
        f"{cifras['tipos']['standard']} normas y {cifras['tipos']['reference']} referencias.",
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


def comprueba_bloques(errores: List[str]) -> None:
    vistos: Dict[tuple, str] = {}
    sin_bloque: List[str] = []
    for class_id, bloque in sources.iter_class_blocks():
        if not bloque:
            sin_bloque.append(class_id)
            continue
        if bloque in vistos:
            errores.append(f"la clase {class_id} repite el bloque de fuentes de la clase {vistos[bloque]}")
        else:
            vistos[bloque] = class_id
    if sin_bloque:
        errores.append(f"{len(sin_bloque)} clase(s) sin bloque de fuentes: {sin_bloque[:5]}")


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
    comprueba_bloques(errores)
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
