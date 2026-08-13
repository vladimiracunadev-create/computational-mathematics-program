"""Valida el artefacto de GitHub Pages antes de publicarlo.

Comprueba que el sitio existe, que tiene una página por parte y por clase, que
no quedan enlaces internos rotos y que no se cuela ninguna referencia a un host
externo (el portal debe funcionar sin conexión).

    python scripts/validate_site.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import curriculum  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SITE = ROOT / "site"
OBLIGATORIOS = (
    "index.html", "404.html", "robots.txt", "sitemap.xml",
    "manifest.webmanifest", "service-worker.js", ".nojekyll",
    "assets/style.css", "assets/app.js", "data/catalog.json",
)
HOSTS_PERMITIDOS = ("github.com", "vladimiracunadev-create.github.io", "www.sitemaps.org",
                    "www.w3.org", "http://www.w3.org/2000/svg")
ENLACE = re.compile(r'(?:href|src)="([^"#]+)"')
# Un recurso se carga al renderizar la página y crea una dependencia de terceros:
# cualquier `src`, y el `href` de <link>. Un `href` de <a> es solo navegación y
# no rompe el funcionamiento sin conexión, así que las fuentes citadas sí pueden
# enlazarse a su origen.
RECURSO = re.compile(r'src="(https?://[^"]+)"|<link\b[^>]*href="(https?://[^"]+)"')
ANCLA_EXTERNA = re.compile(r'<a\b[^>]*href="(https?://[^"]+)"')


def main() -> int:
    errores: List[str] = []

    if not SITE.is_dir():
        print("No existe site/. Ejecuta `python scripts/generate_site.py`.")
        return 1

    for relativo in OBLIGATORIOS:
        ruta = SITE / relativo
        if not ruta.exists():
            errores.append(f"falta {relativo}")
        elif relativo != ".nojekyll" and ruta.stat().st_size == 0:
            errores.append(f"archivo vacío: {relativo}")

    partes = curriculum.parts()
    clases = list(curriculum.classes())

    for parte in partes:
        pagina = SITE / "parts" / f"part-{parte['id']}.html"
        if not pagina.exists():
            errores.append(f"falta la página de la parte {parte['id']}")

    for clase in clases:
        pagina = SITE / "classes" / f"{clase['id']}.html"
        if not pagina.exists():
            errores.append(f"falta la página de la clase {clase['id']}")

    catalogo_sitio = json.loads((SITE / "data" / "catalog.json").read_text(encoding="utf-8"))
    if len(catalogo_sitio) != len(clases):
        errores.append(f"data/catalog.json tiene {len(catalogo_sitio)} entradas, esperadas {len(clases)}")

    index = (SITE / "index.html").read_text(encoding="utf-8")
    if "window.CATALOG" not in index:
        errores.append("index.html no embebe el catálogo para el buscador")
    for afirmacion in (str(len(clases)), str(len(partes)), str(len(clases) * 3)):
        if afirmacion not in index:
            errores.append(f"index.html no declara el conteo {afirmacion}")

    rotos = 0
    recursos_externos = set()
    citas_externas = set()
    # El manual de site/downloads es un documento independiente: cita fuentes
    # externas legítimamente y no forma parte de la navegación del portal.
    paginas = [p for p in SITE.rglob("*.html") if "downloads" not in p.parts]
    for pagina in paginas:
        texto = pagina.read_text(encoding="utf-8")
        for destino in ENLACE.findall(texto):
            if destino.startswith(("http://", "https://", "data:", "mailto:", "//")):
                continue
            if destino.startswith("/"):
                # ruta absoluta del sitio publicado (404.html): se resuelve en Pages
                continue
            resuelto = (pagina.parent / destino).resolve()
            if not resuelto.exists():
                rotos += 1
                if rotos <= 10:
                    errores.append(f"enlace roto en {pagina.relative_to(SITE)}: {destino}")
        for src, link_href in RECURSO.findall(texto):
            url = src or link_href
            if url and not any(host in url for host in HOSTS_PERMITIDOS):
                recursos_externos.add(url)
        for url in ANCLA_EXTERNA.findall(texto):
            if not any(host in url for host in HOSTS_PERMITIDOS):
                citas_externas.add(url)

    if recursos_externos:
        errores.append(f"recursos externos no permitidos: {sorted(recursos_externos)[:5]}")

    descargas = SITE / "downloads"
    manual_html = descargas / "computational-mathematics-program-manual.html"
    manual_pdf = descargas / "computational-mathematics-program-manual.pdf"
    if "downloads/computational-mathematics-program-manual" in index:
        if not manual_html.exists():
            errores.append("el índice enlaza el manual HTML pero no está en site/downloads")
        if not manual_pdf.exists():
            print("  · aviso: el PDF del manual no está en site/downloads "
                  "(instala el extra `manual` para generarlo)")

    sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8")
    urls = sitemap.count("<loc>")
    esperadas = 1 + len(partes) + len(clases)
    if urls != esperadas:
        errores.append(f"sitemap.xml tiene {urls} URLs, esperadas {esperadas}")

    if errores:
        print(f"{len(errores)} problema(s) en el artefacto del sitio:\n")
        for problema in errores[:40]:
            print(f"  ✗ {problema}")
        return 1

    archivos = sum(1 for p in SITE.rglob("*") if p.is_file())
    tamano = sum(p.stat().st_size for p in SITE.rglob("*") if p.is_file()) / 1_048_576
    print(
        f"OK: sitio válido — {archivos} archivos ({tamano:.1f} MB), "
        f"{len(partes)} páginas de parte, {len(clases)} páginas de clase, "
        f"{urls} URLs en el sitemap, 0 enlaces internos rotos, 0 recursos externos "
        f"y {len(citas_externas)} fuentes citadas con enlace a su origen."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
