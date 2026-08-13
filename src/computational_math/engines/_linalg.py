"""Álgebra lineal mínima en Python puro, compartida por varios motores.

No pretende competir con NumPy: existe para que cada laboratorio pueda ejecutarse
sin dependencias y para que el procedimiento quede visible línea por línea.
"""

from __future__ import annotations

import math
from typing import List, Sequence, Tuple

Vector = List[float]
Matrix = List[List[float]]


def zeros(rows: int, cols: int) -> Matrix:
    return [[0.0] * cols for _ in range(rows)]


def identity(n: int) -> Matrix:
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def shape(a: Matrix) -> Tuple[int, int]:
    return len(a), len(a[0]) if a else 0


def transpose(a: Matrix) -> Matrix:
    return [list(col) for col in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matvec(a: Matrix, x: Sequence[float]) -> Vector:
    return [sum(v * xi for v, xi in zip(row, x)) for row in a]


def dot(u: Sequence[float], v: Sequence[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def norm(u: Sequence[float]) -> float:
    return math.sqrt(dot(u, u))


def scale(u: Sequence[float], k: float) -> Vector:
    return [k * a for a in u]


def add(u: Sequence[float], v: Sequence[float]) -> Vector:
    return [a + b for a, b in zip(u, v)]


def sub(u: Sequence[float], v: Sequence[float]) -> Vector:
    return [a - b for a, b in zip(u, v)]


def normalize(u: Sequence[float]) -> Vector:
    n = norm(u)
    return list(u) if n == 0 else scale(u, 1.0 / n)


def gaussian_elimination(a: Matrix, b: Sequence[float]) -> Tuple[Vector, Matrix, int]:
    """Resuelve ``Ax = b`` con pivoteo parcial.

    Devuelve ``(solución, matriz triangular superior, número de intercambios)``.
    """
    n = len(a)
    m = [row[:] + [rhs] for row, rhs in zip(a, b)]
    swaps = 0
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-15:
            raise ValueError("matriz singular o mal condicionada")
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            swaps += 1
        for row in range(col + 1, n):
            factor = m[row][col] / m[col][col]
            for k in range(col, n + 1):
                m[row][k] -= factor * m[col][k]
    x = [0.0] * n
    for row in reversed(range(n)):
        acc = m[row][n] - sum(m[row][k] * x[k] for k in range(row + 1, n))
        x[row] = acc / m[row][row]
    return x, [row[:n] for row in m], swaps


def determinant(a: Matrix) -> float:
    n = len(a)
    m = [row[:] for row in a]
    det = 1.0
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) < 1e-15:
            return 0.0
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            det = -det
        det *= m[col][col]
        for row in range(col + 1, n):
            factor = m[row][col] / m[col][col]
            for k in range(col, n):
                m[row][k] -= factor * m[col][k]
    return det


def rank(a: Matrix, tol: float = 1e-10) -> int:
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for col in range(cols):
        pivot = None
        for row in range(r, rows):
            if abs(m[row][col]) > tol:
                pivot = row
                break
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        pv = m[r][col]
        m[r] = [v / pv for v in m[r]]
        for row in range(rows):
            if row != r and abs(m[row][col]) > tol:
                factor = m[row][col]
                m[row] = [v - factor * w for v, w in zip(m[row], m[r])]
        r += 1
        if r == rows:
            break
    return r


def inverse(a: Matrix) -> Matrix:
    n = len(a)
    aug = [row[:] + ident_row for row, ident_row in zip(a, identity(n))]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-15:
            raise ValueError("matriz no invertible")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pv = aug[col][col]
        aug[col] = [v / pv for v in aug[col]]
        for row in range(n):
            if row != col:
                factor = aug[row][col]
                aug[row] = [v - factor * w for v, w in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def gram_schmidt(vectors: Matrix) -> Matrix:
    """Ortonormaliza filas mediante Gram-Schmidt modificado."""
    basis: Matrix = []
    for v in vectors:
        w = list(v)
        for b in basis:
            w = sub(w, scale(b, dot(w, b)))
        n = norm(w)
        if n > 1e-12:
            basis.append(scale(w, 1.0 / n))
    return basis


def qr(a: Matrix) -> Tuple[Matrix, Matrix]:
    """Factorización QR por Gram-Schmidt sobre las columnas de ``a``."""
    cols = transpose(a)
    q_cols = gram_schmidt(cols)
    q = transpose(q_cols)
    r = matmul(transpose(q), a)
    return q, r


def lu(a: Matrix) -> Tuple[Matrix, Matrix]:
    """Factorización LU sin pivoteo (Doolittle)."""
    n = len(a)
    lower, upper = identity(n), zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            upper[i][j] = a[i][j] - sum(lower[i][k] * upper[k][j] for k in range(i))
        for j in range(i + 1, n):
            if abs(upper[i][i]) < 1e-15:
                raise ValueError("se requiere pivoteo")
            lower[j][i] = (a[j][i] - sum(lower[j][k] * upper[k][i] for k in range(i))) / upper[i][i]
    return lower, upper


def power_iteration(a: Matrix, iterations: int = 500) -> Tuple[float, Vector]:
    """Autovalor dominante y su autovector por iteración de potencias."""
    n = len(a)
    v = normalize([1.0 / math.sqrt(n)] * n)
    eigenvalue = 0.0
    for _ in range(iterations):
        w = matvec(a, v)
        nw = norm(w)
        if nw < 1e-15:
            break
        v = scale(w, 1.0 / nw)
        eigenvalue = dot(v, matvec(a, v))
    return eigenvalue, v


def symmetric_eigen(a: Matrix, sweeps: int = 60) -> Tuple[Vector, Matrix]:
    """Autovalores y autovectores de una matriz simétrica (Jacobi cíclico)."""
    n = len(a)
    m = [row[:] for row in a]
    v = identity(n)
    for _ in range(sweeps):
        off = math.sqrt(sum(m[i][j] ** 2 for i in range(n) for j in range(n) if i != j))
        if off < 1e-12:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                if abs(m[p][q]) < 1e-15:
                    continue
                theta = (m[q][q] - m[p][p]) / (2 * m[p][q])
                t = math.copysign(1.0, theta) / (abs(theta) + math.sqrt(theta * theta + 1))
                c = 1 / math.sqrt(t * t + 1)
                s = t * c
                for k in range(n):
                    mkp, mkq = m[k][p], m[k][q]
                    m[k][p], m[k][q] = c * mkp - s * mkq, s * mkp + c * mkq
                for k in range(n):
                    mpk, mqk = m[p][k], m[q][k]
                    m[p][k], m[q][k] = c * mpk - s * mqk, s * mpk + c * mqk
                for k in range(n):
                    vkp, vkq = v[k][p], v[k][q]
                    v[k][p], v[k][q] = c * vkp - s * vkq, s * vkp + c * vkq
    eigenvalues = [m[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda i: -eigenvalues[i])
    return [eigenvalues[i] for i in order], [[v[r][i] for i in order] for r in range(n)]


def svd(a: Matrix) -> Tuple[Matrix, Vector, Matrix]:
    """SVD reducida vía autodescomposición de ``AᵀA`` (matrices pequeñas)."""
    at_a = matmul(transpose(a), a)
    eigenvalues, v = symmetric_eigen(at_a)
    singular = [math.sqrt(max(x, 0.0)) for x in eigenvalues]
    u_cols: Matrix = []
    for j, s in enumerate(singular):
        col = [v[i][j] for i in range(len(v))]
        av = matvec(a, col)
        u_cols.append(scale(av, 1.0 / s) if s > 1e-12 else [0.0] * len(a))
    return transpose(u_cols), singular, v


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values)


def column_means(data: Matrix) -> Vector:
    return [mean(col) for col in transpose(data)]


def center(data: Matrix) -> Matrix:
    mu = column_means(data)
    return [[x - m for x, m in zip(row, mu)] for row in data]


def covariance(data: Matrix) -> Matrix:
    centered = center(data)
    n = len(centered)
    ct = transpose(centered)
    return [[dot(ci, cj) / (n - 1) for cj in ct] for ci in ct]
