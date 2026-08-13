"""Laboratorio 338 — Bellman equations.

Parte 16 · Matemática de Transformers, modelos generativos, grafos y RL
Motor: computational_math.engines.part16 · demostración `bellman_equations`

Iteración de valor sobre un MDP pequeño.

Ciclo de trabajo: predicción → cálculo → verificación → interpretación.
Escribe tu predicción antes de ejecutar; solo entonces el resultado enseña algo.

Ejecutar:
    python lab.py
    compmath run 338
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

from computational_math.engines import part16 as motor  # noqa: E402

DEMO = "bellman_equations"


def main() -> dict:
    """Ejecuta la demostración de la clase y muestra sus resultados."""
    resultado = motor.DEMOS[DEMO]()
    print(f"Clase 338 — Bellman equations")
    print(f"Parte 16 · Matemática de Transformers, modelos generativos, grafos y RL")
    print(f"Demostración: {DEMO} — {motor.DEMOS[DEMO].__doc__.strip().splitlines()[0]}")
    print("-" * 72)
    print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))
    return resultado


if __name__ == "__main__":
    salida = main()
    assert isinstance(salida, dict) and salida, "la demostración debe devolver resultados"
