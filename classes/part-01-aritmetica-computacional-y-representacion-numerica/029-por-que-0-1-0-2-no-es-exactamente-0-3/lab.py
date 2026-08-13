"""Laboratorio 029 — Por qué 0.1 + 0.2 no es exactamente 0.3.

Parte 01 · Aritmética computacional y representación numérica
Motor: computational_math.engines.part01 · demostración `why_point_one`

0.1 + 0.2 != 0.3 explicado con la fracción binaria real.

Ciclo de trabajo: predicción → cálculo → verificación → interpretación.
Escribe tu predicción antes de ejecutar; solo entonces el resultado enseña algo.

Ejecutar:
    python lab.py
    compmath run 029
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

DEMO = "why_point_one"


def main() -> dict:
    """Ejecuta la demostración de la clase y muestra sus resultados."""
    resultado = motor.DEMOS[DEMO]()
    print(f"Clase 029 — Por qué 0.1 + 0.2 no es exactamente 0.3")
    print(f"Parte 01 · Aritmética computacional y representación numérica")
    print(f"Demostración: {DEMO} — {motor.DEMOS[DEMO].__doc__.strip().splitlines()[0]}")
    print("-" * 72)
    print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))
    return resultado


if __name__ == "__main__":
    salida = main()
    assert isinstance(salida, dict) and salida, "la demostración debe devolver resultados"
