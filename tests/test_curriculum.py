"""Coherencia del currículo: conteos, identificadores y catálogo derivado."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import curriculum  # noqa: E402


class TestCurriculum(unittest.TestCase):
    def test_declaracion_coincide_con_contenido(self):
        totales = curriculum.totals()
        self.assertEqual(totales["partes_declaradas"], totales["partes_reales"])
        self.assertEqual(totales["clases_declaradas"], totales["clases_reales"])

    def test_hay_18_partes(self):
        self.assertEqual(len(curriculum.parts()), 18)

    def test_hay_360_clases(self):
        self.assertEqual(len(list(curriculum.classes())), 360)

    def test_cada_parte_tiene_20_clases(self):
        for parte in curriculum.parts():
            with self.subTest(parte=parte["id"]):
                self.assertEqual(len(parte["classes"]), 20)

    def test_identificadores_correlativos_y_unicos(self):
        ids = [c["id"] for c in curriculum.classes()]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(ids, [f"{i:03d}" for i in range(1, 361)])

    def test_partes_numeradas_de_00_a_17(self):
        self.assertEqual([p["id"] for p in curriculum.parts()], [f"{i:02d}" for i in range(18)])

    def test_cada_parte_tiene_metadatos_completos(self):
        obligatorios = ("slug", "title", "level", "engine", "summary", "applications",
                        "ai_link", "key_ideas", "pitfalls", "stack", "references")
        for parte in curriculum.parts():
            for campo in obligatorios:
                with self.subTest(parte=parte["id"], campo=campo):
                    self.assertIn(campo, parte)
                    self.assertTrue(parte[campo], f"{campo} vacío en la parte {parte['id']}")

    def test_cada_parte_tiene_referencias_reales(self):
        for parte in curriculum.parts():
            with self.subTest(parte=parte["id"]):
                self.assertGreaterEqual(len(parte["references"]), 3)
                for ref in parte["references"]:
                    self.assertRegex(ref, r"\d{4}", "toda referencia debe llevar año")

    def test_catalogo_guardado_coincide_con_el_derivado(self):
        self.assertEqual(curriculum.load_catalog(), curriculum.build_catalog())

    def test_catalogo_apunta_a_archivos_existentes(self):
        for entrada in curriculum.load_catalog():
            with self.subTest(clase=entrada["id"]):
                self.assertTrue((ROOT / entrada["path"]).exists(), entrada["path"])

    def test_busqueda_por_id(self):
        clase = curriculum.find_class("250")
        self.assertEqual(clase["title"], "Adam")
        self.assertEqual(clase["part"], "12")
        with self.assertRaises(KeyError):
            curriculum.find_class("999")

    def test_json_del_catalogo_es_utf8_valido(self):
        contenido = curriculum.CATALOG_PATH.read_text(encoding="utf-8")
        self.assertEqual(len(json.loads(contenido)), 360)


if __name__ == "__main__":
    unittest.main()
