"""Verifica que el sitio realmente publicado responde y sirve el contenido.

Se ejecuta después del despliegue de GitHub Pages: comprueba el índice, una
página de parte y una página de clase. Reintenta porque la propagación de Pages
no es instantánea.

    python scripts/validate_pages.py --url https://usuario.github.io/repo/ --attempts 12 --delay 10
"""

from __future__ import annotations

import argparse
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RUTAS = [
    ("", ["Computational Mathematics", "window.CATALOG"]),
    ("parts/part-00.html", ["Pensamiento matemático desde cero"]),
    ("parts/part-17.html", ["Frontera matemática"]),
    ("classes/001.html", ["Números naturales y conteo"]),
    ("classes/360.html", ["Capstone"]),
    ("data/catalog.json", ['"id"']),
]


ESQUEMAS_PERMITIDOS = ("http", "https")


def _fetch(url: str, timeout: int = 30) -> str:
    esquema = urllib.parse.urlparse(url).scheme
    if esquema not in ESQUEMAS_PERMITIDOS:
        raise ValueError(f"esquema no permitido: {esquema!r} (solo http y https)")
    peticion = urllib.request.Request(url, headers={"User-Agent": "compmath-pages-validator"})
    # El esquema ya está validado arriba: solo http y https.
    with urllib.request.urlopen(peticion, timeout=timeout) as respuesta:  # nosec B310
        if respuesta.status != 200:
            raise urllib.error.HTTPError(url, respuesta.status, "estado inesperado", respuesta.headers, None)
        return respuesta.read().decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, help="URL base del sitio publicado")
    parser.add_argument("--attempts", type=int, default=10, help="reintentos por ruta")
    parser.add_argument("--delay", type=int, default=10, help="segundos entre reintentos")
    args = parser.parse_args()

    base = args.url if args.url.endswith("/") else args.url + "/"
    print(f"Verificando el sitio publicado en {base}")

    fallos = []
    for ruta, esperados in RUTAS:
        url = base + ruta
        ultimo_error = None
        for intento in range(1, args.attempts + 1):
            try:
                cuerpo = _fetch(url)
            except Exception as exc:  # noqa: BLE001 - se reintenta
                ultimo_error = exc
                if intento < args.attempts:
                    time.sleep(args.delay)
                continue
            faltantes = [t for t in esperados if t not in cuerpo]
            if faltantes:
                ultimo_error = f"contenido esperado ausente: {faltantes}"
                if intento < args.attempts:
                    time.sleep(args.delay)
                    continue
            else:
                print(f"  OK  {url}  ({len(cuerpo):,} bytes)")
                ultimo_error = None
                break
        if ultimo_error:
            fallos.append(f"{url} → {ultimo_error}")

    if fallos:
        print(f"\n{len(fallos)} ruta(s) fallaron:")
        for problema in fallos:
            print(f"  ✗ {problema}")
        return 1

    print(f"\nOK: el sitio publicado responde en las {len(RUTAS)} rutas verificadas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
