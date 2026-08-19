"""Resolutor **en red** del registro de fuentes. Manual o programado. NO bloquea.

Deliberadamente separado de `verify_sources.py`: si la red entra en el CI, el CI
se vuelve inestable y se acaba ignorando. Aquí se acepta la inestabilidad a
cambio de comprobar de verdad que cada localizador resuelve.

Qué hace con cada entrada:

- ``isbn13``  → ``https://openlibrary.org/isbn/{isbn}.json`` y compara el título;
- ``doi``     → ``api.crossref.org`` y, si no está, ``api.datacite.org``;
- ``url``     → GET y registra el estado devuelto;
- libro sin ISBN → lo busca en Open Library y solo adopta el ISBN de **la edición
  que cita la clase**: título, apellido y año tienen que coincidir los tres.

Lo que deja de resolver **se marca, no se borra**. Lo que no se puede resolver
sin inventar se queda ``pendiente`` con la razón escrita en ``note``.

    python scripts/refresh_sources.py                 # resuelve todo el registro
    python scripts/refresh_sources.py --only pendiente # solo las pendientes
    python scripts/refresh_sources.py --limit 20       # prueba corta
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import sources  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CONTACTO = "vladimir.acuna.dev@gmail.com"
REPO = "https://github.com/vladimiracunadev-create/computational-mathematics-program"
UA = f"computational-mathematics-program/0.2 (+{REPO}; mailto:{CONTACTO})"
CABECERAS = {"User-Agent": UA, "Accept": "*/*"}
PAUSA = 0.15
ESPERA = 30          # segundos de espera por peticion (Open Library es lento)
UMBRAL_TITULO = 0.82
COBERTURA_TOKENS = 0.8
INTENTOS = 2
ESPERA_REINTENTO = 1.0
GUARDA_CADA = 20     # entradas entre guardados incrementales
AÑO_RE = re.compile(r"\b(1[6-9]\d{2}|20\d{2})\b")


def _abre(url: str, timeout: int = ESPERA, method: str = "GET"):
    peticion = urllib.request.Request(url, headers=CABECERAS, method=method)
    return urllib.request.urlopen(peticion, timeout=timeout)


def _con_reintentos(accion, intentos: int = INTENTOS):
    """Reintenta ante fallos de transporte. Un 404 no se reintenta: es respuesta.

    Sin esto, una red doméstica con un par de tiempos de espera agotados produce
    decenas de «pendiente» falsos, y un registro que miente por pesimismo es tan
    inútil como uno que miente por optimismo.
    """
    ultimo = ""
    for intento in range(intentos):
        try:
            return accion(), "200"
        except urllib.error.HTTPError as exc:
            return None, f"HTTP {exc.code}"
        except (urllib.error.URLError, ssl.SSLError, TimeoutError, OSError) as exc:
            ultimo = f"{type(exc).__name__}: {exc}"
            time.sleep(ESPERA_REINTENTO * (intento + 1))
    return None, ultimo


def pide_json(url: str) -> Tuple[Optional[Any], str]:
    """Devuelve ``(json, motivo)``. ``motivo`` describe el fallo si lo hubo."""
    def leer():
        with _abre(url) as respuesta:
            return json.loads(respuesta.read().decode("utf-8", "replace"))

    try:
        return _con_reintentos(leer)
    except json.JSONDecodeError:
        return None, "respuesta no es JSON"


def toca(url: str) -> str:
    """GET a una URL. Devuelve el estado en texto (``200``, ``HTTP 403``, …)."""
    def leer():
        with _abre(url) as respuesta:
            return str(respuesta.status)

    valor, motivo = _con_reintentos(leer)
    return valor if valor else motivo


def _limpia_titulo(texto: str) -> str:
    """Quita etiquetas HTML y paréntesis: Crossref devuelve «<i>p</i>-Values»."""
    sin_html = re.sub(r"<[^>]+>", " ", texto or "")
    return re.sub(r"\([^)]*\)", " ", sin_html)


ARTICULOS = frozenset({"the", "a", "an", "el", "la", "los", "las", "un", "una"})


def _sin_articulo(tokens: List[str]) -> List[str]:
    return tokens[1:] if tokens and tokens[0] in ARTICULOS else tokens


def _subsecuencia_comun(corto: List[str], largo: List[str]) -> int:
    """Longitud de la subsecuencia común más larga, respetando el orden.

    El orden importa: «Categorical Data Analysis» y «Analysis of Ordinal
    Categorical Data» comparten todas las palabras y son libros distintos.
    """
    previa = [0] * (len(largo) + 1)
    for palabra in corto:
        actual = [0]
        for j, otra in enumerate(largo):
            actual.append(previa[j] + 1 if palabra == otra else max(actual[j], previa[j + 1]))
        previa = actual
    return previa[-1]


def parecido(a: str, b: str) -> float:
    """Cuánto se parecen dos títulos, de 0 a 1, sin dejarse engañar por prefijos.

    Compara palabras, no cadenas: así «Calculus» no se hace pasar por
    «Precalculus» ni «Algebra» por «Linear Algebra Done Right», y una cita
    abreviada («…through SDEs») sí reconoce a la obra cuyo título completo
    desarrolla la abreviatura.
    """
    x = sources.normalise_title(_limpia_titulo(a))
    y = sources.normalise_title(_limpia_titulo(b))
    if not x or not y:
        return 0.0
    if x == y:
        return 1.0
    tx, ty = x.split(), y.split()
    corto, largo = (tx, ty) if len(tx) <= len(ty) else (ty, tx)
    if len(corto) <= 2:
        # Un título de una o dos palabras solo se acepta si encabeza al otro.
        cabeza, resto = _sin_articulo(corto), _sin_articulo(largo)
        return 1.0 if resto[: len(cabeza)] == cabeza else 0.0
    cobertura = _subsecuencia_comun(corto, largo) / len(corto)
    if cobertura >= COBERTURA_TOKENS:
        return 1.0
    return min(cobertura, SequenceMatcher(None, x, y).ratio())


def apellidos(autores: List[str]) -> List[str]:
    return [sources.normalise_title(a.split(",")[0]).strip() for a in autores if a]


def coincide_autor(citados: List[str], resueltos: List[str]) -> bool:
    if not citados or not resueltos:
        return True  # sin autores citados no hay nada que contradecir
    dados = " ".join(sources.normalise_title(a) for a in resueltos)
    return any(apellido and apellido in dados for apellido in apellidos(citados))


# --------------------------------------------------------------------------- #
# Autoridades
# --------------------------------------------------------------------------- #


def resuelve_isbn(isbn: str) -> Tuple[Optional[Dict[str, Any]], str]:
    datos, motivo = pide_json(f"https://openlibrary.org/isbn/{isbn}.json")
    if datos is None:
        return None, motivo
    publicado = str(datos.get("publish_date", ""))
    años = AÑO_RE.findall(publicado)
    return {
        "title": datos.get("title", ""),
        "published": publicado,
        "year": años[-1] if años else None,
    }, "200"


def resuelve_doi(doi: str) -> Tuple[Optional[Dict[str, Any]], str]:
    ruta = urllib.parse.quote(doi, safe="")
    datos, motivo = pide_json(f"https://api.crossref.org/works/{ruta}")
    if datos and isinstance(datos, dict) and "message" in datos:
        mensaje = datos["message"]
        titulos = mensaje.get("title") or []
        autores = [
            " ".join(filter(None, [a.get("family"), a.get("given")]))
            for a in mensaje.get("author", [])
        ]
        año = None
        emitido = (mensaje.get("issued") or {}).get("date-parts") or [[]]
        if emitido and emitido[0]:
            año = str(emitido[0][0])
        return {
            "title": titulos[0] if titulos else "",
            "authors": autores,
            "published": año,
            "isbn": [i.replace("-", "") for i in mensaje.get("ISBN", [])],
            "agency": "Crossref",
            "type": mensaje.get("type", ""),
        }, "200"

    datos, motivo_dc = pide_json(f"https://api.datacite.org/dois/{ruta}")
    if datos and isinstance(datos, dict) and "data" in datos:
        atributos = datos["data"]["attributes"]
        titulos = atributos.get("titles") or []
        return {
            "title": titulos[0].get("title", "") if titulos else "",
            "authors": [c.get("name", "") for c in atributos.get("creators", [])],
            "published": str(atributos.get("publicationYear") or ""),
            "isbn": [],
            "agency": "DataCite",
            "type": (atributos.get("types") or {}).get("resourceTypeGeneral", ""),
        }, "200"
    return None, f"crossref {motivo} · datacite {motivo_dc}"


def _ediciones(work_key: str) -> List[Dict[str, Any]]:
    """Todas las ediciones de una obra de Open Library, en una sola petición."""
    datos, _ = pide_json(f"https://openlibrary.org{work_key}/editions.json?limit=100")
    if not isinstance(datos, dict):
        return []
    salida = []
    for edicion in datos.get("entries", []):
        isbns = [
            sources.normalise_isbn(i)
            for i in (edicion.get("isbn_13") or [])
            if sources.isbn13_valid(i)
        ]
        if not isbns:
            continue
        años = AÑO_RE.findall(str(edicion.get("publish_date", "")))
        salida.append({
            "isbn": sorted(isbns)[0],
            "title": edicion.get("title", ""),
            "year": años[-1] if años else None,
        })
    return salida


def busca_isbn(titulo: str, autores: List[str], año: Optional[str]) -> Tuple[Optional[str], str]:
    """Busca en Open Library el ISBN-13 de **la edición que cita la clase**.

    Nunca devuelve un ISBN «probable». Exige tres coincidencias: título, apellido
    del primer autor y **año de edición**. Una edición distinta de la citada no es
    la fuente que la clase usó, así que no se adopta: se anota y queda pendiente.
    """
    if not titulo:
        return None, "sin título que buscar"
    consulta = {"title": titulo, "limit": "5", "fields": "key,title,author_name"}
    if autores:
        consulta["author"] = autores[0].split(",")[0]
    url = "https://openlibrary.org/search.json?" + urllib.parse.urlencode(consulta)
    datos, motivo = pide_json(url)
    if datos is None:
        return None, motivo

    for documento in datos.get("docs", []):
        if parecido(titulo, documento.get("title", "")) < UMBRAL_TITULO:
            continue
        if not coincide_autor(autores, documento.get("author_name") or []):
            continue
        ediciones = [
            e for e in _ediciones(documento.get("key", ""))
            if parecido(titulo, e["title"]) >= UMBRAL_TITULO
        ]
        if not ediciones:
            continue
        if not año:
            elegida = ediciones[0]
            return elegida["isbn"], (
                f"ISBN confirmado en Open Library como «{elegida['title']}» "
                f"(la cita no declara año)"
            )
        for edicion in ediciones:
            if edicion["year"] == año:
                return edicion["isbn"], (
                    f"ISBN de la edición citada ({año}) confirmado en Open Library "
                    f"como «{edicion['title']}»"
                )
        vistos = ", ".join(sorted({e["year"] or "s. f." for e in ediciones}))
        return None, (
            f"Open Library tiene la obra pero no la edición citada ({año}); "
            f"ediciones disponibles: {vistos}"
        )
    return None, "sin coincidencia de título y autor en Open Library"


# --------------------------------------------------------------------------- #
# Resolución de una entrada
# --------------------------------------------------------------------------- #


def refresca(entrada: Dict[str, Any], hoy: str) -> str:
    """Resuelve una entrada contra su autoridad. Devuelve el veredicto."""
    citado = entrada.get("title") or ""
    autores = entrada.get("authors") or []

    if entrada.get("isbn13"):
        ficha, motivo = resuelve_isbn(entrada["isbn13"])
        if ficha is None:
            entrada["status"] = "pendiente"
            entrada["note"] = f"Open Library no resuelve el ISBN {entrada['isbn13']} ({motivo})"
            return "pendiente"
        semejanza = parecido(citado, ficha["title"])
        entrada["accessed"] = hoy
        if semejanza >= UMBRAL_TITULO:
            entrada["status"] = "verificada"
            entrada["note"] = f"ISBN resuelto en Open Library como «{ficha['title']}»"
            return "verificada"
        entrada["status"] = "pendiente"
        entrada["note"] = (
            f"el ISBN {entrada['isbn13']} resuelve a «{ficha['title']}», "
            f"que no coincide con la cita «{citado}»: revisar el enlace de la clase"
        )
        return "discrepancia"

    if entrada.get("doi"):
        ficha, motivo = resuelve_doi(entrada["doi"])
        if ficha is None:
            entrada["status"] = "pendiente"
            entrada["note"] = f"el DOI no resuelve ({motivo})"
            return "pendiente"
        entrada["accessed"] = hoy
        entrada["authority"] = f"{ficha['agency']} (agencia de registro del DOI)"
        semejanza = parecido(citado, ficha["title"])
        autor_ok = coincide_autor(autores, ficha.get("authors") or [])
        if semejanza >= UMBRAL_TITULO and autor_ok:
            entrada["status"] = "verificada"
            entrada["note"] = f"DOI resuelto en {ficha['agency']} como «{ficha['title']}»"
            return "verificada"
        entrada["status"] = "pendiente"
        entrada["note"] = (
            f"el DOI resuelve a «{ficha['title']}», que no coincide con la cita "
            f"«{citado}»: revisar el enlace de la clase"
        )
        return "discrepancia"

    # Sin identificador: si la cita tiene pinta de libro, se intenta su ISBN.
    if entrada.get("type") == "reference" and citado and autores:
        isbn, motivo = busca_isbn(citado, autores, entrada.get("published"))
        if isbn:
            entrada["type"] = "book"
            entrada["isbn13"] = isbn
            entrada["locator"] = sources.canonical_locator(entrada)
            entrada["authority"] = "International ISBN Agency (comprobado vía Open Library)"
            entrada["accessed"] = hoy
            entrada["status"] = "verificada"
            entrada["note"] = motivo
            return "verificada"
        pendiente_por = motivo
    else:
        pendiente_por = None

    estado = toca(entrada["locator"])
    entrada["accessed"] = hoy
    if estado == "200":
        if entrada["locator"].startswith("http://"):
            entrada["status"] = "pendiente"
            entrada["note"] = "la fuente primaria responde pero no sirve https"
            return "pendiente"
        entrada["status"] = "verificada"
        nota = "URL de la fuente primaria comprobada con GET"
        if pendiente_por:
            nota += f"; sin ISBN adoptado: {pendiente_por}"
        entrada["note"] = nota
        return "verificada"

    entrada["status"] = "pendiente"
    razon = f"la URL respondió {estado}"
    if pendiente_por:
        razon += f"; {pendiente_por}"
    if entrada["locator"].startswith("http://"):
        razon += "; además no sirve https"
    entrada["note"] = razon
    return "pendiente"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=sources.ESTADOS, help="resuelve solo las entradas en ese estado")
    parser.add_argument("--limit", type=int, default=0, help="corta tras N entradas (pruebas)")
    parser.add_argument("--offset", type=int, default=0,
                        help="empieza en la entrada N: retoma una pasada interrumpida")
    parser.add_argument("--ids", default="",
                        help="lista de identificadores separados por coma: reintenta solo esos")
    parser.add_argument("--dry-run", action="store_true", help="no escribe el registro")
    args = parser.parse_args()

    registro = sources.load_registry()
    entradas = registro.get("entries", [])
    if args.only:
        objetivo = [e for e in entradas if e.get("status") == args.only]
    else:
        objetivo = list(entradas)
    if args.ids:
        pedidos = {i.strip() for i in args.ids.split(",") if i.strip()}
        objetivo = [e for e in objetivo if e["id"] in pedidos]
        desconocidos = pedidos - {e["id"] for e in objetivo}
        if desconocidos:
            print(f"  ! identificadores que no están en el registro: {sorted(desconocidos)}")
    if args.offset:
        objetivo = objetivo[args.offset :]
    if args.limit:
        objetivo = objetivo[: args.limit]

    hoy = date.today().isoformat()
    print(f"Resolviendo {len(objetivo)} de {len(entradas)} entradas contra sus autoridades…")
    conteo = {"verificada": 0, "pendiente": 0, "discrepancia": 0}
    problemas: List[Tuple[str, str]] = []
    for numero, entrada in enumerate(objetivo, start=1):
        veredicto = refresca(entrada, hoy)
        conteo[veredicto] = conteo.get(veredicto, 0) + 1
        if veredicto != "verificada":
            problemas.append((entrada["id"], entrada.get("note", "")))
        marca = {"verificada": "✔", "pendiente": "·", "discrepancia": "!"}[veredicto]
        print(f"  {marca} [{numero:3d}/{len(objetivo)}] {entrada['id']}", flush=True)
        # Guardado incremental: una pasada en red es larga y se puede interrumpir.
        # Lo ya resuelto no se pierde, y `--only pendiente` retoma donde quedó.
        if not args.dry_run and numero % GUARDA_CADA == 0:
            sources.dump_registry(registro)
        time.sleep(PAUSA)

    registro["verified_on"] = hoy
    if not args.dry_run:
        sources.dump_registry(registro)

    print(
        f"\n{conteo['verificada']} verificadas · {conteo['pendiente']} pendientes · "
        f"{conteo['discrepancia']} discrepancias"
    )
    if problemas:
        print("\nLo que no quedó verificado (se marca, no se borra):\n")
        for identificador, nota in problemas:
            print(f"  · {identificador}: {nota}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
