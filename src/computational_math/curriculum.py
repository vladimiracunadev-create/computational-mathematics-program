"""Acceso al currículo declarado en ``curriculum.yaml``.

``curriculum.yaml`` es la única fuente de verdad del programa: de él se derivan
el catálogo, las 360 clases, el sitio y las validaciones.
"""

from __future__ import annotations

import functools
import json
from pathlib import Path
from typing import Any, Dict, Iterator, List

try:  # PyYAML es la dependencia base declarada en pyproject.toml
    import yaml
except ImportError as exc:  # pragma: no cover - entorno sin dependencias
    raise ImportError(
        "Falta PyYAML. Instala el paquete con `pip install -e .` o `pip install PyYAML`."
    ) from exc

__all__ = [
    "ROOT",
    "CURRICULUM_PATH",
    "CATALOG_PATH",
    "load",
    "parts",
    "part",
    "classes",
    "find_class",
    "class_dir",
    "load_catalog",
    "build_catalog",
    "totals",
]

ROOT = Path(__file__).resolve().parents[2]
CURRICULUM_PATH = ROOT / "curriculum.yaml"
CATALOG_PATH = ROOT / "catalog.json"

CLASS_FILES = (
    "README.md",
    "intuition.md",
    "theory.md",
    "derivation.md",
    "exercises.md",
    "assessment.md",
    "where-is-this-used.md",
    "lesson.yaml",
    "lab.py",
    "notebook.ipynb",
    "notebook_student.ipynb",
    "notebook_solution.ipynb",
)


@functools.lru_cache(maxsize=1)
def load() -> Dict[str, Any]:
    """Carga y cachea ``curriculum.yaml``."""
    if not CURRICULUM_PATH.exists():
        raise FileNotFoundError(f"No existe {CURRICULUM_PATH}")
    with CURRICULUM_PATH.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def parts() -> List[Dict[str, Any]]:
    """Las 18 partes del programa, en orden."""
    return load()["parts"]


def part(part_id: str) -> Dict[str, Any]:
    """Devuelve una parte por su identificador (``"00"`` … ``"17"``)."""
    key = f"{int(part_id):02d}"
    for item in parts():
        if item["id"] == key:
            return item
    raise KeyError(f"parte desconocida: {part_id!r}")


def classes() -> Iterator[Dict[str, Any]]:
    """Itera las 360 clases con su parte asociada."""
    for p in parts():
        for index, clase in enumerate(p["classes"], start=1):
            yield {
                **clase,
                "part": p["id"],
                "part_slug": p["slug"],
                "part_title": p["title"],
                "level": p["level"],
                "engine": p["engine"],
                "index_in_part": index,
            }


def find_class(class_id: str) -> Dict[str, Any]:
    """Busca una clase por su identificador de tres dígitos."""
    key = f"{int(class_id):03d}"
    for clase in classes():
        if clase["id"] == key:
            return clase
    raise KeyError(f"clase desconocida: {class_id!r}")


def class_dir(clase: Dict[str, Any]) -> Path:
    """Ruta del directorio de una clase dentro de ``classes/``."""
    return ROOT / "classes" / f"part-{clase['part']}-{clase['part_slug']}" / clase["slug"]


def build_catalog() -> List[Dict[str, Any]]:
    """Construye el catálogo derivado del currículo."""
    entradas = []
    for clase in classes():
        directorio = class_dir(clase)
        entradas.append({
            "id": clase["id"],
            "part": clase["part"],
            "part_title": clase["part_title"],
            "title": clase["title"],
            "level": clase["level"],
            "slug": clase["slug"],
            "path": str(directorio.relative_to(ROOT) / "README.md").replace("\\", "/"),
        })
    return entradas


def load_catalog() -> List[Dict[str, Any]]:
    """Lee ``catalog.json``."""
    with CATALOG_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def totals() -> Dict[str, int]:
    """Conteos declarados y derivados, para validar coherencia."""
    programa = load()["program"]
    lista = list(classes())
    return {
        "partes_declaradas": programa["parts"],
        "partes_reales": len(parts()),
        "clases_declaradas": programa["classes"],
        "clases_reales": len(lista),
        "archivos_por_clase": len(CLASS_FILES),
        "notebooks": len(lista) * 3,
        "horas": len(lista) * programa["hours_per_class"],
    }
