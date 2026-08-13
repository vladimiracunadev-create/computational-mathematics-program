"""Valida la coherencia del repositorio contra ``curriculum.yaml``.

Comprueba que lo que el repositorio AFIRMA coincide con lo que CONTIENE:
conteos, contrato de archivos por clase, notebooks válidos, mapeo clase→motor,
catálogo derivado y afirmaciones numéricas del README.

    python scripts/validate_repository.py            # informe
    python scripts/validate_repository.py --strict   # además exige el modo CI
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import curriculum, engines  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NOTEBOOKS = ("notebook.ipynb", "notebook_student.ipynb", "notebook_solution.ipynb")


def _check_curriculum(errores: List[str]) -> None:
    totales = curriculum.totals()
    if totales["partes_declaradas"] != totales["partes_reales"]:
        errores.append(
            f"curriculum.yaml declara {totales['partes_declaradas']} partes "
            f"pero contiene {totales['partes_reales']}"
        )
    if totales["clases_declaradas"] != totales["clases_reales"]:
        errores.append(
            f"curriculum.yaml declara {totales['clases_declaradas']} clases "
            f"pero contiene {totales['clases_reales']}"
        )
    vistos = set()
    for clase in curriculum.classes():
        if clase["id"] in vistos:
            errores.append(f"identificador de clase duplicado: {clase['id']}")
        vistos.add(clase["id"])
    esperado = {f"{i:03d}" for i in range(1, totales["clases_reales"] + 1)}
    faltan = esperado - vistos
    if faltan:
        errores.append(f"identificadores ausentes: {sorted(faltan)[:10]}")


def _check_estructura(errores: List[str]) -> None:
    for clase in curriculum.classes():
        directorio = curriculum.class_dir(clase)
        if not directorio.is_dir():
            errores.append(f"falta el directorio {directorio.relative_to(ROOT)}")
            continue
        for archivo in curriculum.CLASS_FILES:
            ruta = directorio / archivo
            if not ruta.exists():
                errores.append(f"falta {ruta.relative_to(ROOT)}")
            elif ruta.stat().st_size == 0:
                errores.append(f"archivo vacío {ruta.relative_to(ROOT)}")

    for parte in curriculum.parts():
        readme = ROOT / "classes" / f"part-{parte['id']}-{parte['slug']}" / "README.md"
        if not readme.exists():
            errores.append(f"falta {readme.relative_to(ROOT)}")

    directorios = {p.name for p in (ROOT / "classes").glob("part-*") if p.is_dir()}
    declarados = {f"part-{p['id']}-{p['slug']}" for p in curriculum.parts()}
    sobrantes = directorios - declarados
    if sobrantes:
        errores.append(f"directorios de parte no declarados en curriculum.yaml: {sorted(sobrantes)}")


def _check_notebooks(errores: List[str]) -> None:
    for clase in curriculum.classes():
        directorio = curriculum.class_dir(clase)
        for nombre in NOTEBOOKS:
            ruta = directorio / nombre
            if not ruta.exists():
                continue
            try:
                documento = json.loads(ruta.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errores.append(f"notebook inválido {ruta.relative_to(ROOT)}: {exc}")
                continue
            if documento.get("nbformat") != 4:
                errores.append(f"nbformat != 4 en {ruta.relative_to(ROOT)}")
            if not documento.get("cells"):
                errores.append(f"notebook sin celdas {ruta.relative_to(ROOT)}")
            for celda in documento.get("cells", []):
                if celda.get("cell_type") not in {"markdown", "code"}:
                    errores.append(f"tipo de celda inválido en {ruta.relative_to(ROOT)}")


def _check_engines(errores: List[str]) -> None:
    mapa = engines.all_class_demos()
    clases = {c["id"] for c in curriculum.classes()}
    sin_demo = clases - set(mapa)
    if sin_demo:
        errores.append(f"clases sin demostración registrada: {sorted(sin_demo)[:10]}")
    sobrantes = set(mapa) - clases
    if sobrantes:
        errores.append(f"demostraciones que apuntan a clases inexistentes: {sorted(sobrantes)[:10]}")
    for parte in curriculum.parts():
        try:
            motor = engines.load_engine(parte["id"])
        except Exception as exc:  # noqa: BLE001
            errores.append(f"no se pudo cargar el motor de la parte {parte['id']}: {exc}")
            continue
        if motor.__name__.rsplit(".", 1)[-1] != parte["engine"]:
            errores.append(f"la parte {parte['id']} declara el motor {parte['engine']}")
        faltantes = [n for n in motor.CLASS_DEMOS.values() if n not in motor.DEMOS]
        if faltantes:
            errores.append(f"motor {parte['engine']}: demos no definidas {faltantes}")


def _check_catalogo(errores: List[str]) -> None:
    if not curriculum.CATALOG_PATH.exists():
        errores.append("falta catalog.json")
        return
    guardado = curriculum.load_catalog()
    esperado = curriculum.build_catalog()
    if guardado != esperado:
        errores.append(
            "catalog.json está desfasado respecto de curriculum.yaml "
            "(ejecuta `python scripts/generate_classes.py`)"
        )
    for entrada in guardado:
        ruta = ROOT / entrada["path"]
        if not ruta.exists():
            errores.append(f"catalog.json apunta a un archivo inexistente: {entrada['path']}")


def _check_readme(errores: List[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    totales = curriculum.totals()
    afirmaciones = {
        "clases": (str(totales["clases_reales"]), rf"\b{totales['clases_reales']}\s+clases"),
        "partes": (str(totales["partes_reales"]), rf"\b{totales['partes_reales']}\s+partes"),
        "notebooks": (str(totales["notebooks"]), rf"\b{totales['notebooks']:,}".replace(",", r"[.,]?") + r"\s+notebooks"),
    }
    for nombre, (_, patron) in afirmaciones.items():
        if not re.search(patron, readme, flags=re.IGNORECASE):
            errores.append(f"README.md no declara correctamente el número de {nombre}")

    workflows = sorted(p.name for p in (ROOT / ".github" / "workflows").glob("*.yml"))
    for nombre in workflows:
        insignia = f"workflows/{nombre}/badge.svg"
        if insignia not in readme:
            errores.append(f"README.md no muestra la insignia del workflow {nombre}")


def _check_strict(errores: List[str]) -> None:
    """Comprobaciones adicionales que solo tienen sentido en CI."""
    ejecutadas = 0
    for clase in curriculum.classes():
        try:
            resultado = engines.run_class(clase["id"])
        except Exception as exc:  # noqa: BLE001
            errores.append(f"el laboratorio {clase['id']} falló: {exc}")
            continue
        if not isinstance(resultado, dict) or not resultado:
            errores.append(f"el laboratorio {clase['id']} no devolvió resultados")
        ejecutadas += 1
    print(f"  · {ejecutadas} laboratorios ejecutados correctamente")

    version_pkg = (ROOT / "src" / "computational_math" / "__init__.py").read_text(encoding="utf-8")
    version = re.search(r'__version__\s*=\s*"([^"]+)"', version_pkg)
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    version_toml = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, flags=re.MULTILINE)
    version_yaml = curriculum.load()["program"]["version"]
    versiones = {version.group(1) if version else None,
                 version_toml.group(1) if version_toml else None,
                 version_yaml}
    if len(versiones) != 1:
        errores.append(f"versiones incoherentes entre __init__.py, pyproject.toml y curriculum.yaml: {versiones}")
    else:
        print(f"  · versión coherente en todas las fuentes: {version_yaml}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="ejecuta además los 360 laboratorios y valida versiones")
    args = parser.parse_args()

    errores: List[str] = []
    print("Validando el repositorio contra curriculum.yaml…")
    _check_curriculum(errores)
    _check_estructura(errores)
    _check_notebooks(errores)
    _check_engines(errores)
    _check_catalogo(errores)
    _check_readme(errores)
    if args.strict:
        _check_strict(errores)

    if errores:
        print(f"\n{len(errores)} problema(s) encontrados:\n")
        for problema in errores[:60]:
            print(f"  ✗ {problema}")
        if len(errores) > 60:
            print(f"  … y {len(errores) - 60} más")
        return 1

    totales = curriculum.totals()
    print(
        f"\nOK: {totales['partes_reales']} partes, {totales['clases_reales']} clases, "
        f"{totales['notebooks']} notebooks, {len(engines.ENGINE_MODULES)} motores "
        f"y contrato de {totales['archivos_por_clase']} archivos por clase."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
