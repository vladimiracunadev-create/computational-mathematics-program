"""Computational Mathematics Program — biblioteca del programa educativo.

Expone el currículo (:mod:`computational_math.curriculum`), los 18 motores
didácticos ejecutables (:mod:`computational_math.engines`) y utilidades
numéricas compartidas (:mod:`computational_math.helpers`).
"""

from __future__ import annotations

__version__ = "0.2.0"

__all__ = ["__version__", "curriculum", "engines", "helpers"]

from . import curriculum, engines, helpers  # noqa: E402,F401
