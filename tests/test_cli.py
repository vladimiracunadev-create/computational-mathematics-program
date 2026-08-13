"""La CLI `compmath`: comandos, códigos de salida y salidas mínimas."""

from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import __version__, cli  # noqa: E402


def ejecutar(argv):
    """Ejecuta la CLI capturando su salida. Devuelve ``(codigo, texto)``."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        codigo = cli.main(argv)
    return codigo, buffer.getvalue()


class TestCLI(unittest.TestCase):
    def test_catalog_lista_las_360_clases(self):
        codigo, salida = ejecutar(["catalog"])
        self.assertEqual(codigo, 0)
        self.assertIn("Total: 360 clases", salida)

    def test_catalog_por_parte(self):
        codigo, salida = ejecutar(["catalog", "--part", "12"])
        self.assertEqual(codigo, 0)
        self.assertIn("Total: 20 clases", salida)
        self.assertIn("Adam", salida)

    def test_catalog_json_es_parseable(self):
        _, salida = ejecutar(["catalog", "--part", "00", "--json"])
        datos = json.loads(salida)
        self.assertEqual(len(datos), 20)
        self.assertEqual(datos[0]["id"], "001")

    def test_catalog_parte_inexistente(self):
        with self.assertRaises(SystemExit):
            ejecutar(["catalog", "--part", "99"])

    def test_show_muestra_la_ficha(self):
        codigo, salida = ejecutar(["show", "250"])
        self.assertEqual(codigo, 0)
        self.assertIn("250 — Adam", salida)
        self.assertIn("part12", salida)

    def test_run_una_clase(self):
        codigo, salida = ejecutar(["run", "001"])
        self.assertEqual(codigo, 0)
        self.assertIn("suma_formula_cerrada", salida)

    def test_run_una_parte_completa(self):
        codigo, salida = ejecutar(["run", "--part", "00", "--quiet"])
        self.assertEqual(codigo, 0)
        self.assertIn("20/20 laboratorios correctos", salida)

    def test_run_sin_argumentos_falla(self):
        with self.assertRaises(SystemExit):
            ejecutar(["run"])

    def test_stats_reporta_los_conteos(self):
        codigo, salida = ejecutar(["stats"])
        self.assertEqual(codigo, 0)
        self.assertIn(__version__, salida)
        self.assertIn("360", salida)
        self.assertIn("1080", salida)

    def test_progress_muestra_las_18_barras(self):
        codigo, salida = ejecutar(["progress"])
        self.assertEqual(codigo, 0)
        self.assertIn("/360 clases", salida)
        self.assertEqual(salida.count("█") + salida.count("·") >= 18 * 20, True)

    def test_version(self):
        with self.assertRaises(SystemExit) as ctx:
            ejecutar(["--version"])
        self.assertEqual(ctx.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
