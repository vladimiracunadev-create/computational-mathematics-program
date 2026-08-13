"""Motores didácticos ejecutables, uno por parte del programa.

Cada motor es Python estándar, determinista y sin dependencias externas: las
bibliotecas científicas se usan como *contraste* en los notebooks, nunca como
requisito para ejecutar un laboratorio. Cada clase del programa apunta a una
demostración concreta de su motor mediante :data:`CLASS_DEMOS`.
"""

from __future__ import annotations

import importlib
from typing import Any, Callable, Dict

__all__ = ["ENGINE_MODULES", "load_engine", "demo_for_class", "run_class", "all_class_demos"]

ENGINE_MODULES = tuple(f"part{index:02d}" for index in range(18))

_CACHE: Dict[str, Any] = {}


def load_engine(part_id: str):
    """Devuelve el módulo motor de una parte (``"00"`` … ``"17"``)."""
    name = f"part{int(part_id):02d}"
    if name not in ENGINE_MODULES:
        raise KeyError(f"parte desconocida: {part_id!r}")
    if name not in _CACHE:
        _CACHE[name] = importlib.import_module(f"{__name__}.{name}")
    return _CACHE[name]


def demo_for_class(class_id: str) -> tuple[str, Callable[[], dict]]:
    """Devuelve ``(nombre, función)`` de la demostración asociada a una clase."""
    class_id = f"{int(class_id):03d}"
    part_id = f"{(int(class_id) - 1) // 20:02d}"
    engine = load_engine(part_id)
    try:
        demo_name = engine.CLASS_DEMOS[class_id]
    except KeyError as exc:  # pragma: no cover - defensivo
        raise KeyError(f"la clase {class_id} no tiene demostración registrada") from exc
    return demo_name, engine.DEMOS[demo_name]


def run_class(class_id: str) -> dict:
    """Ejecuta la demostración de una clase y devuelve su resultado."""
    _, func = demo_for_class(class_id)
    return func()


def all_class_demos() -> Dict[str, str]:
    """Mapa completo ``clase -> demostración`` de las 360 clases."""
    mapping: Dict[str, str] = {}
    for name in ENGINE_MODULES:
        engine = load_engine(name[-2:])
        mapping.update(engine.CLASS_DEMOS)
    return mapping
