"""Capa de contenido pedagógico: ``content/part-NN.yaml``.

Separa **qué** enseña el programa (``curriculum.yaml``), **qué calcula**
(``engines/``) y **cómo se explica** (este módulo). Cada archivo de contenido
aporta, para una parte:

- ``resumen_extendido``: la explicación larga de la parte;
- ``mapa``: diagrama Mermaid del mapa conceptual;
- ``glosario``: términos con su definición y la clase donde se estudian;
- ``clases``: por cada clase, concepto, fórmulas, desarrollo, ejemplo trabajado,
  errores conceptuales, aplicación y referencias con enlace.

El contenido es **opcional por clase**: si una clase todavía no tiene registro,
el generador usa el material base. Así el repositorio nunca queda a medias.
"""

from __future__ import annotations

import functools
from pathlib import Path
from typing import Any, Dict, List

import yaml

from .curriculum import ROOT

__all__ = [
    "CONTENT_DIR",
    "load_part",
    "part_content",
    "class_content",
    "glossary",
    "coverage",
    "CAMPOS_CLASE",
]

CONTENT_DIR = ROOT / "content"

CAMPOS_CLASE = (
    "concepto",      # definición de una línea
    "formulas",      # lista de fórmulas en texto plano
    "desarrollo",    # explicación larga (varios párrafos)
    "ejemplo",       # ejemplo numérico trabajado paso a paso
    "errores",       # errores conceptuales frecuentes (lista)
    "aplicacion",    # dónde se usa de verdad
    "referencias",   # lista de enlaces markdown
)


@functools.lru_cache(maxsize=32)
def load_part(part_id: str) -> Dict[str, Any]:
    """Carga el contenido de una parte. Devuelve ``{}`` si aún no existe."""
    ruta = CONTENT_DIR / f"part-{int(part_id):02d}.yaml"
    if not ruta.exists():
        return {}
    with ruta.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def part_content(part_id: str) -> Dict[str, Any]:
    """Contenido de la parte sin la sección de clases."""
    datos = dict(load_part(part_id))
    datos.pop("clases", None)
    return datos


def class_content(class_id: str) -> Dict[str, Any]:
    """Registro de contenido de una clase. Devuelve ``{}`` si no está redactado."""
    class_id = f"{int(class_id):03d}"
    part_id = f"{(int(class_id) - 1) // 20:02d}"
    return (load_part(part_id).get("clases") or {}).get(class_id, {}) or {}


def glossary(part_id: str) -> List[Dict[str, str]]:
    """Términos del glosario de una parte."""
    return load_part(part_id).get("glosario") or []


def coverage() -> Dict[str, Any]:
    """Cuánto contenido pedagógico está redactado, sin exagerarlo."""
    from .curriculum import classes, parts

    con_parte = sum(1 for p in parts() if load_part(p["id"]).get("resumen_extendido"))
    con_mapa = sum(1 for p in parts() if load_part(p["id"]).get("mapa"))
    con_glosario = sum(1 for p in parts() if load_part(p["id"]).get("glosario"))
    terminos = sum(len(glossary(p["id"])) for p in parts())

    completas = 0
    total = 0
    for clase in classes():
        total += 1
        registro = class_content(clase["id"])
        if all(registro.get(campo) for campo in CAMPOS_CLASE):
            completas += 1

    return {
        "partes_con_resumen": con_parte,
        "partes_con_mapa": con_mapa,
        "partes_con_glosario": con_glosario,
        "terminos_de_glosario": terminos,
        "clases_con_contenido_completo": completas,
        "clases_totales": total,
        "cobertura_%": round(100 * completas / total, 1) if total else 0.0,
    }


def ruta_de_parte(part_id: str) -> Path:
    """Ruta del archivo de contenido de una parte."""
    return CONTENT_DIR / f"part-{int(part_id):02d}.yaml"
