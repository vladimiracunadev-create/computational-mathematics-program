"""El portal estático: se genera, es autocontenido y no tiene enlaces rotos."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT / "src"))

from computational_math import curriculum  # noqa: E402


def _generar_si_falta() -> None:
    if not (SITE / "index.html").exists():
        subprocess.run([sys.executable, str(ROOT / "scripts" / "generate_site.py")],
                       check=True, cwd=ROOT)


class TestSitio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _generar_si_falta()

    def test_archivos_obligatorios(self):
        for relativo in ("index.html", "404.html", "robots.txt", "sitemap.xml",
                         "manifest.webmanifest", "service-worker.js", ".nojekyll",
                         "assets/style.css", "assets/app.js", "data/catalog.json"):
            with self.subTest(archivo=relativo):
                self.assertTrue((SITE / relativo).exists(), relativo)

    def test_una_pagina_por_parte(self):
        for parte in curriculum.parts():
            with self.subTest(parte=parte["id"]):
                self.assertTrue((SITE / "parts" / f"part-{parte['id']}.html").exists())

    def test_una_pagina_por_clase(self):
        paginas = list((SITE / "classes").glob("*.html"))
        self.assertEqual(len(paginas), 360)

    def test_el_catalogo_del_sitio_coincide_con_el_curriculo(self):
        datos = json.loads((SITE / "data" / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(len(datos), 360)
        self.assertEqual([d["id"] for d in datos], [c["id"] for c in curriculum.classes()])

    def test_el_indice_declara_los_conteos_reales(self):
        index = (SITE / "index.html").read_text(encoding="utf-8")
        totales = curriculum.totals()
        self.assertIn(str(totales["clases_reales"]), index)
        self.assertIn(str(totales["notebooks"]), index)
        self.assertIn("window.CATALOG", index)

    def _paginas(self):
        """Páginas del portal, excluyendo el manual descargable."""
        return [p for p in SITE.rglob("*.html") if "downloads" not in p.parts]

    def test_no_hay_recursos_de_hosts_externos(self):
        """Ningún `src` ni `<link>` apunta fuera: el portal se renderiza sin red.

        Los `href` de `<a>` sí pueden salir: son las fuentes citadas por las
        clases, y un enlace no se descarga al abrir la página.
        """
        permitidos = ("github.com", "github.io", "www.sitemaps.org", "www.w3.org")
        recurso = re.compile(r'src="(https?://[^"]+)"|<link\b[^>]*href="(https?://[^"]+)"')
        for pagina in self._paginas():
            texto = pagina.read_text(encoding="utf-8")
            for src, link_href in recurso.findall(texto):
                url = src or link_href
                with self.subTest(pagina=pagina.name, url=url):
                    self.assertTrue(any(h in url for h in permitidos), url)

    def test_no_hay_enlaces_internos_rotos(self):
        rotos = []
        for pagina in self._paginas():
            for destino in re.findall(r'(?:href|src)="([^"#]+)"', pagina.read_text(encoding="utf-8")):
                if destino.startswith(("http", "data:", "mailto:", "//", "/")):
                    continue
                if not (pagina.parent / destino).resolve().exists():
                    rotos.append(f"{pagina.name} → {destino}")
        self.assertEqual(rotos, [], f"enlaces rotos: {rotos[:5]}")

    def test_toda_pagina_declara_charset_y_viewport(self):
        for pagina in self._paginas():
            texto = pagina.read_text(encoding="utf-8")
            with self.subTest(pagina=pagina.name):
                self.assertIn('<meta charset="utf-8">', texto)
                self.assertIn("viewport", texto)
                self.assertIn('lang="es"', texto)

    def test_sitemap_cubre_todas_las_paginas(self):
        sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8")
        self.assertEqual(sitemap.count("<loc>"), 1 + 18 + 360)


class TestSitioReflejaElContenido(unittest.TestCase):
    """El portal publica la capa pedagógica, no solo `curriculum.yaml`.

    Sin estas pruebas el sitio puede quedarse atrás sin que nada avise: se
    genera igual de bien con el contenido y sin él.
    """

    @classmethod
    def setUpClass(cls):
        _generar_si_falta()

    def test_cada_parte_publica_panorama_recorrido_y_glosario(self):
        for parte in curriculum.parts():
            texto = (SITE / "parts" / f"part-{parte['id']}.html").read_text(encoding="utf-8")
            with self.subTest(parte=parte["id"]):
                self.assertIn("Panorama de la parte", texto)
                self.assertIn("Recorrido de la parte", texto)
                self.assertIn("Glosario de la parte", texto)

    def test_cada_clase_publica_desarrollo_ejemplo_y_fuentes(self):
        for clase in curriculum.classes():
            texto = (SITE / "classes" / f"{clase['id']}.html").read_text(encoding="utf-8")
            with self.subTest(clase=clase["id"]):
                self.assertIn("<h2>Desarrollo</h2>", texto)
                self.assertIn("<h2>Ejemplo trabajado</h2>", texto)
                self.assertIn("<h2>Errores comunes</h2>", texto)
                self.assertIn("<h2>Bibliografía de la clase</h2>", texto)

    def test_el_glosario_del_sitio_enlaza_a_clases_que_existen(self):
        enlace = re.compile(r'<a href="\.\./classes/(\d{3})\.html">\1</a>')
        ids = {c["id"] for c in curriculum.classes()}
        total = 0
        for parte in curriculum.parts():
            texto = (SITE / "parts" / f"part-{parte['id']}.html").read_text(encoding="utf-8")
            for cid in enlace.findall(texto):
                total += 1
                self.assertIn(cid, ids)
        self.assertGreaterEqual(total, 400, "faltan términos de glosario en el sitio")

    def test_el_contenido_no_deja_marcado_markdown_sin_convertir(self):
        for clase in list(curriculum.classes())[::17]:
            texto = (SITE / "classes" / f"{clase['id']}.html").read_text(encoding="utf-8")
            cuerpo = re.sub(r"<pre>.*?</pre>", "", texto, flags=re.DOTALL)
            with self.subTest(clase=clase["id"]):
                self.assertNotIn("**", cuerpo)
                self.assertNotIn("](http", cuerpo)


if __name__ == "__main__":
    unittest.main()
