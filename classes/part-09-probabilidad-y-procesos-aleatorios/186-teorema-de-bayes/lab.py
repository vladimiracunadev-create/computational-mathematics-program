"""Laboratorio 186 — Teorema de Bayes.

Parte 09 · Probabilidad y procesos aleatorios
Motor: computational_math.engines.part09 · demostración `bayes`

Test médico: por qué un positivo no significa enfermedad.

Ciclo de trabajo: predicción → cálculo → verificación → interpretación.
Escribe tu predicción antes de ejecutar; solo entonces el resultado enseña algo.

Ejecutar:
    python lab.py
    compmath run 186
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

from computational_math.engines import part09 as motor  # noqa: E402

DEMO = "bayes"


def main() -> dict:
    """Ejecuta la demostración de la clase y muestra sus resultados."""
    resultado = motor.DEMOS[DEMO]()
    print(f"Clase 186 — Teorema de Bayes")
    print(f"Parte 09 · Probabilidad y procesos aleatorios")
    print(f"Demostración: {DEMO} — {motor.DEMOS[DEMO].__doc__.strip().splitlines()[0]}")
    print("-" * 72)
    print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))
    return resultado


if __name__ == "__main__":
    salida = main()
    assert isinstance(salida, dict) and salida, "la demostración debe devolver resultados"
