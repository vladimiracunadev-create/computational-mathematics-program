"""Contrato de archivos por clase, notebooks y coherencia de la documentación."""

from __future__ import annotations

import ast
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import curriculum  # noqa: E402

CLASES = list(curriculum.classes())
NOTEBOOKS = ("notebook.ipynb", "notebook_student.ipynb", "notebook_solution.ipynb")


class TestEstructura(unittest.TestCase):
    def test_hay_18_directorios_de_parte(self):
        directorios = sorted(p.name for p in (ROOT / "classes").glob("part-*") if p.is_dir())
        self.assertEqual(len(directorios), 18)

    def test_contrato_de_12_archivos_por_clase(self):
        self.assertEqual(len(curriculum.CLASS_FILES), 12)
        for clase in CLASES:
            directorio = curriculum.class_dir(clase)
            with self.subTest(clase=clase["id"]):
                self.assertTrue(directorio.is_dir(), directorio)
                for archivo in curriculum.CLASS_FILES:
                    ruta = directorio / archivo
                    self.assertTrue(ruta.exists(), f"falta {ruta}")
                    self.assertGreater(ruta.stat().st_size, 0, f"vacío {ruta}")

    def test_cada_parte_tiene_readme(self):
        for parte in curriculum.parts():
            readme = ROOT / "classes" / f"part-{parte['id']}-{parte['slug']}" / "README.md"
            with self.subTest(parte=parte["id"]):
                self.assertTrue(readme.exists())

    def test_readme_de_clase_menciona_su_titulo_y_su_demo(self):
        for clase in CLASES:
            readme = (curriculum.class_dir(clase) / "README.md").read_text(encoding="utf-8")
            with self.subTest(clase=clase["id"]):
                self.assertIn(clase["title"], readme)
                self.assertIn(f"compmath run {clase['id']}", readme)

    def test_no_quedan_directorios_de_clase_huerfanos(self):
        declarados = {curriculum.class_dir(c).resolve() for c in CLASES}
        for parte_dir in (ROOT / "classes").glob("part-*"):
            for hijo in parte_dir.iterdir():
                if hijo.is_dir():
                    with self.subTest(directorio=hijo.name):
                        self.assertIn(hijo.resolve(), declarados)


class TestNotebooks(unittest.TestCase):
    def test_hay_1080_notebooks(self):
        total = sum(1 for c in CLASES for n in NOTEBOOKS
                    if (curriculum.class_dir(c) / n).exists())
        self.assertEqual(total, 1080)

    def test_notebooks_son_nbformat_4_validos(self):
        for clase in CLASES:
            for nombre in NOTEBOOKS:
                ruta = curriculum.class_dir(clase) / nombre
                with self.subTest(clase=clase["id"], notebook=nombre):
                    documento = json.loads(ruta.read_text(encoding="utf-8"))
                    self.assertEqual(documento["nbformat"], 4)
                    self.assertTrue(documento["cells"])
                    for celda in documento["cells"]:
                        self.assertIn(celda["cell_type"], {"markdown", "code"})
                        self.assertIn("source", celda)

    def test_notebook_estudiante_tiene_tareas_pendientes(self):
        for clase in CLASES:
            ruta = curriculum.class_dir(clase) / "notebook_student.ipynb"
            with self.subTest(clase=clase["id"]):
                self.assertIn("TODO", ruta.read_text(encoding="utf-8"))

    def test_notebook_solucion_no_tiene_tareas_pendientes(self):
        for clase in CLASES:
            ruta = curriculum.class_dir(clase) / "notebook_solution.ipynb"
            with self.subTest(clase=clase["id"]):
                self.assertNotIn("TODO", ruta.read_text(encoding="utf-8"))


class TestLaboratorios(unittest.TestCase):
    def test_todos_los_labs_compilan(self):
        for clase in CLASES:
            ruta = curriculum.class_dir(clase) / "lab.py"
            with self.subTest(clase=clase["id"]):
                ast.parse(ruta.read_text(encoding="utf-8"), filename=str(ruta))

    def test_cada_lab_apunta_al_motor_de_su_parte(self):
        for clase in CLASES:
            texto = (curriculum.class_dir(clase) / "lab.py").read_text(encoding="utf-8")
            with self.subTest(clase=clase["id"]):
                self.assertIn(f"engines import {clase['engine']}", texto)

    def test_lesson_yaml_declara_los_12_artefactos(self):
        for clase in CLASES:
            texto = (curriculum.class_dir(clase) / "lesson.yaml").read_text(encoding="utf-8")
            with self.subTest(clase=clase["id"]):
                for archivo in curriculum.CLASS_FILES:
                    self.assertIn(archivo, texto)


class TestDocumentacion(unittest.TestCase):
    def test_readme_declara_los_conteos_reales(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        totales = curriculum.totals()
        self.assertRegex(readme, rf"\b{totales['clases_reales']}\s+clases")
        self.assertRegex(readme, rf"\b{totales['partes_reales']}\s+partes")
        self.assertTrue(str(totales["notebooks"]) in readme,
                        f"README.md no menciona los {totales['notebooks']} notebooks")

    def test_readme_muestra_una_insignia_por_workflow(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for workflow in (ROOT / ".github" / "workflows").glob("*.yml"):
            with self.subTest(workflow=workflow.name):
                self.assertTrue(f"workflows/{workflow.name}/badge.svg" in readme,
                                f"falta la insignia de {workflow.name} en README.md")

    def test_version_coherente_en_las_tres_fuentes(self):
        init = (ROOT / "src" / "computational_math" / "__init__.py").read_text(encoding="utf-8")
        pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        version_init = re.search(r'__version__\s*=\s*"([^"]+)"', init).group(1)
        version_toml = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, re.MULTILINE).group(1)
        version_yaml = curriculum.load()["program"]["version"]
        self.assertEqual({version_init, version_toml, version_yaml}, {version_init})

    def test_changelog_menciona_la_version_actual(self):
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn(curriculum.load()["program"]["version"], changelog)

    def test_documentos_obligatorios_presentes(self):
        for nombre in ("README.md", "LICENSE", "CHANGELOG.md", "CONTRIBUTING.md",
                       "SECURITY.md", "CODE_OF_CONDUCT.md", "SUPPORT.md", "ROADMAP.md",
                       "INSTALL.md", "curriculum.yaml", "pyproject.toml"):
            with self.subTest(archivo=nombre):
                self.assertTrue((ROOT / nombre).exists(), nombre)

    def test_docs_referenciados_en_el_readme_existen(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for destino in re.findall(r"\]\((docs/[^)#]+)\)", readme):
            with self.subTest(destino=destino):
                self.assertTrue((ROOT / destino).exists(), destino)

    def test_no_hay_enlaces_internos_rotos_en_markdown(self):
        raices = [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md")),
                  *sorted((ROOT / "learning-paths").glob("*.md"))]
        rotos = []
        for archivo in raices:
            for destino in re.findall(r"\]\(([^)\s]+)\)", archivo.read_text(encoding="utf-8")):
                if destino.startswith(("http", "#", "mailto:")):
                    continue
                destino = destino.split("#")[0]
                if destino and not (archivo.parent / destino).resolve().exists():
                    rotos.append(f"{archivo.relative_to(ROOT).as_posix()} → {destino}")
        self.assertEqual(rotos, [], f"enlaces rotos: {rotos[:5]}")

    def test_hay_una_ruta_por_perfil_para_cada_archivo(self):
        rutas = sorted((ROOT / "learning-paths").glob("*.md"))
        self.assertGreaterEqual(len(rutas), 12)
        for ruta in rutas:
            texto = ruta.read_text(encoding="utf-8")
            with self.subTest(ruta=ruta.name):
                self.assertIn("## Clases-hito", texto)
                self.assertIn("compmath run", texto)
                self.assertIn("Límite honesto", texto)

    def test_las_integraciones_declaran_prerrequisitos(self):
        integraciones = sorted((ROOT / "docs" / "integrations").glob("*.md"))
        self.assertGreaterEqual(len(integraciones), 9)   # 8 repos + índice
        for archivo in integraciones:
            if archivo.name == "README.md":
                continue
            texto = archivo.read_text(encoding="utf-8")
            with self.subTest(integracion=archivo.name):
                self.assertIn("Prerrequisitos matemáticos", texto)
                self.assertIn("No duplica", texto)


if __name__ == "__main__":
    unittest.main()
