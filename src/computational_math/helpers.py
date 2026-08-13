"""Utilidades numéricas compartidas por laboratorios y notebooks.

Solo biblioteca estándar: cualquier laboratorio del programa se ejecuta sin
instalar dependencias científicas.
"""

from __future__ import annotations

import math
from typing import Callable, Iterable, Sequence

__all__ = [
    "relative_error",
    "absolute_error",
    "finite_difference",
    "second_derivative",
    "sigmoid",
    "softmax",
    "log_sum_exp",
    "trapezoid",
    "simpson",
    "almost_equal",
    "significant_digits",
    "describe",
]


def absolute_error(approx: float, exact: float) -> float:
    """Error absoluto |aprox - exacto|."""
    return abs(approx - exact)


def relative_error(approx: float, exact: float) -> float:
    """Error relativo, protegido frente a un valor exacto nulo."""
    return abs(approx - exact) / max(abs(exact), 1e-15)


def finite_difference(f: Callable[[float], float], x: float, h: float = 1e-6) -> float:
    """Derivada por diferencia central, de orden O(h²)."""
    return (f(x + h) - f(x - h)) / (2 * h)


def second_derivative(f: Callable[[float], float], x: float, h: float = 1e-4) -> float:
    """Segunda derivada por diferencias centradas."""
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)


def sigmoid(x: float) -> float:
    """Sigmoide numéricamente estable."""
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    z = math.exp(x)
    return z / (1.0 + z)


def softmax(values: Sequence[float]) -> list[float]:
    """Softmax estable: resta el máximo antes de exponenciar."""
    if not values:
        return []
    m = max(values)
    exps = [math.exp(v - m) for v in values]
    total = sum(exps)
    return [v / total for v in exps]


def log_sum_exp(values: Sequence[float]) -> float:
    """log(Σ exp(vᵢ)) sin desbordar."""
    if not values:
        return float("-inf")
    m = max(values)
    return m + math.log(sum(math.exp(v - m) for v in values))


def trapezoid(f: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """Regla del trapecio compuesta, error O(h²)."""
    if n <= 0:
        raise ValueError("n debe ser positivo")
    h = (b - a) / n
    return h * (f(a) / 2 + sum(f(a + i * h) for i in range(1, n)) + f(b) / 2)


def simpson(f: Callable[[float], float], a: float, b: float, n: int = 1000) -> float:
    """Regla de Simpson compuesta, error O(h⁴). Requiere n par."""
    if n <= 0 or n % 2:
        raise ValueError("n debe ser par y positivo")
    h = (b - a) / n
    return h / 3 * (
        f(a) + f(b)
        + 4 * sum(f(a + i * h) for i in range(1, n, 2))
        + 2 * sum(f(a + i * h) for i in range(2, n, 2))
    )


def almost_equal(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 1e-12) -> bool:
    """Comparación de flotantes con tolerancia declarada, nunca con ``==``."""
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def significant_digits(approx: float, exact: float) -> float:
    """Dígitos significativos correctos de una aproximación."""
    err = relative_error(approx, exact)
    return float("inf") if err == 0 else max(0.0, -math.log10(err))


def describe(values: Iterable[float]) -> dict:
    """Resumen descriptivo mínimo de una muestra."""
    data = sorted(values)
    n = len(data)
    if n == 0:
        raise ValueError("la muestra está vacía")
    media = sum(data) / n
    var = sum((x - media) ** 2 for x in data) / (n - 1) if n > 1 else 0.0
    mediana = data[n // 2] if n % 2 else (data[n // 2 - 1] + data[n // 2]) / 2
    return {
        "n": n,
        "min": data[0],
        "max": data[-1],
        "media": media,
        "mediana": mediana,
        "varianza": var,
        "desviacion": math.sqrt(var),
    }
