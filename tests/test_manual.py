"""El manual completo: se construye, cubre todo el programa y no inventa cifras."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import content, curriculum  # noqa: E402

sys.path.insert(0, str(ROOT / "scripts"))
import build_manual  # noqa: E402


class TestConversorMarkdown(unittest.TestCase):
    def test_parrafo(self):
        self.assertEqual(build_manual.md_a_html("hola mundo"), "<p>hola mundo</p>")

    def test_lista_con_vinetas(self):
        salida = build_manual.md_a_html("- uno\n- dos")
        self.assertEqual(salida, "<ul><li>uno</li><li>dos</li></ul>")

    def test_lista_numerada(self):
        salida = build_manual.md_a_html("1. uno\n2. dos")
        self.assertEqual(salida, "<ol><li>uno</li><li>dos</li></ol>")

    def test_bloque_de_codigo(self):
        salida = build_manual.md_a_html("```text\na = 1\n```")
        self.assertIn("<pre><code>a = 1</code></pre>", salida)

    def test_formato_en_linea(self):
        salida = build_manual.md_a_html("un **fuerte**, un `codigo` y un [enlace](http://x)")
        self.assertIn("<strong>fuerte</strong>", salida)
        self.assertIn("<code>codigo</code>", salida)
        self.assertIn('<a href="http://x">enlace</a>', salida)

    def test_escapa_html_del_contenido(self):
        salida = build_manual.md_a_html("5 < 7 y 8 > 3")
        self.assertNotIn("<7", salida)
        self.assertIn("&lt;", salida)

    def test_tabla(self):
        salida = build_manual.md_a_html("| a | b |\n|---|---|\n| 1 | 2 |")
        self.assertIn("<table>", salida)
        self.assertIn("<th>a</th>", salida)
        self.assertIn("<td>1</td>", salida)

    def test_cita(self):
        self.assertIn("<blockquote>", build_manual.md_a_html("> una cita"))

    def test_texto_vacio(self):
        self.assertEqual(build_manual.md_a_html(""), "")


class TestManual(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = build_manual.construir_html()

    def test_cubre_las_18_partes(self):
        for parte in curriculum.parts():
            with self.subTest(parte=parte["id"]):
                self.assertIn(f'id="p{parte["id"]}"', self.html)

    def test_cubre_las_360_clases(self):
        faltan = [c["id"] for c in curriculum.classes() if f'id="c{c["id"]}"' not in self.html]
        self.assertEqual(faltan, [], f"clases ausentes: {faltan[:5]}")

    def test_declara_los_conteos_reales(self):
        totales = curriculum.totals()
        for cifra in (totales["clases_reales"], totales["partes_reales"], totales["notebooks"]):
            with self.subTest(cifra=cifra):
                self.assertIn(str(cifra), self.html)

    def test_declara_la_cobertura_real_del_contenido(self):
        cobertura = content.coverage()
        self.assertIn(str(cobertura["clases_con_contenido_completo"]), self.html)

    def test_no_contiene_scripts(self):
        self.assertNotIn("<script", self.html.lower())

    def test_es_html_bien_formado_en_lo_esencial(self):
        self.assertTrue(self.html.startswith("<!doctype html>"))
        self.assertIn('<html lang="es">', self.html)
        self.assertIn('<meta charset="utf-8">', self.html)
        self.assertTrue(self.html.rstrip().endswith("</html>"))

    def test_el_indice_enlaza_cada_clase(self):
        for clase in list(curriculum.classes())[:20]:
            with self.subTest(clase=clase["id"]):
                self.assertIn(f'href="#c{clase["id"]}"', self.html)

    def test_incluye_el_contenido_redactado(self):
        # La clase 029 está redactada: su concepto debe aparecer en el manual.
        registro = content.class_content("029")
        self.assertTrue(registro, "la clase 029 debería tener contenido redactado")
        self.assertIn("0.1 no es representable", self.html)

    def test_verificador_acepta_el_manual_generado(self):
        self.assertEqual(build_manual.verificar(self.html), 0)

    def test_el_script_se_ejecuta_de_extremo_a_extremo(self):
        proceso = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "build_manual.py"), "--check"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=ROOT,
        )
        self.assertEqual(proceso.returncode, 0, proceso.stdout + proceso.stderr)


if __name__ == "__main__":
    unittest.main()
