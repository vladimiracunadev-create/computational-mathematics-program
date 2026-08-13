"""Laboratorio 030 — Error absoluto y error relativo.

Parte 01 · Aritmética computacional y representación numérica
Motor: computational_math.engines.part01 · demostración `absolute_relative_error`

El error relativo es el que se propaga; el absoluto engaña con la escala.

Ciclo de trabajo: predicción → cálculo → verificación → interpretación.
Escribe tu predicción antes de ejecutar; solo entonces el resultado enseña algo.

Ejecutar:
    python lab.py
    compmath run 030
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # consolas Windows sin UTF-8
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from computational_math.engines import part01 as motor  # noqa: E402

DEMO = "absolute_relative_error"


def main() -> dict:
    """Ejecuta la demostración de la clase y muestra sus resultados."""
    resultado = motor.DEMOS[DEMO]()
    print(f"Clase 030 — Error absoluto y error relativo")
    print(f"Parte 01 · Aritmética computacional y representación numérica")
    print(f"Demostración: {DEMO} — {motor.DEMOS[DEMO].__doc__.strip().splitlines()[0]}")
    print("-" * 72)
    print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))
    return resultado


if __name__ == "__main__":
    salida = main()
    assert isinstance(salida, dict) and salida, "la demostración debe devolver resultados"
