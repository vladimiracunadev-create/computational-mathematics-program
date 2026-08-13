"""Motor 06 — Álgebra lineal II: descomposiciones y tensores.

Cambio de base, autovalores, LU, QR, mínimos cuadrados, SVD, pseudoinversa,
PCA y álgebra tensorial.
"""

from __future__ import annotations

import math

from . import _linalg as la

PART = "06"
TITLE = "Álgebra lineal II: descomposiciones y tensores"

_SIM = [[4.0, 1.0], [1.0, 3.0]]
_DATOS = [
    [2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0],
    [2.3, 2.7], [2.0, 1.6], [1.0, 1.1], [1.5, 1.6], [1.1, 0.9],
]


def bases_coordinates() -> dict:
    """Las coordenadas dependen de la base elegida."""
    base = [[1.0, 1.0], [1.0, -1.0]]
    v = [3.0, 1.0]
    b_mat = la.transpose(base)
    coords, _, _ = la.gaussian_elimination(b_mat, v)
    return {
        "vector_en_base_canonica": v,
        "base_alternativa": base,
        "coordenadas_en_la_nueva_base": [round(c, 12) for c in coords],
        "reconstruccion": [round(x, 12) for x in la.matvec(b_mat, coords)],
        "el_vector_no_cambia": True,
        "lo_que_cambia": "su lista de coordenadas",
        "base_es_independiente": la.rank(base) == 2,
    }


def change_of_basis() -> dict:
    """Matriz de cambio de base y su inversa."""
    p = [[1.0, 1.0], [1.0, -1.0]]
    p_inv = la.inverse(p)
    v = [3.0, 1.0]
    return {
        "P": p,
        "P⁻¹": [[round(x, 12) for x in row] for row in p_inv],
        "coordenadas_nuevas_P⁻¹v": [round(x, 12) for x in la.matvec(p_inv, v)],
        "vuelta_a_la_canonica": [round(x, 12) for x in la.matvec(p, la.matvec(p_inv, v))],
        "P·P⁻¹": [[round(x, 12) for x in row] for row in la.matmul(p, p_inv)],
        "similaridad": "A' = P⁻¹AP representa la misma transformación",
    }


def linear_transformations() -> dict:
    """Una transformación lineal preserva sumas y escalados."""
    a = [[2.0, 0.0], [0.0, 3.0]]
    u, v, k = [1.0, 2.0], [3.0, -1.0], 4.0
    return {
        "matriz": a,
        "T(u+v)": la.matvec(a, la.add(u, v)),
        "T(u)+T(v)": la.add(la.matvec(a, u), la.matvec(a, v)),
        "aditiva": la.matvec(a, la.add(u, v)) == la.add(la.matvec(a, u), la.matvec(a, v)),
        "T(ku)": la.matvec(a, la.scale(u, k)),
        "kT(u)": la.scale(la.matvec(a, u), k),
        "homogenea": la.matvec(a, la.scale(u, k)) == la.scale(la.matvec(a, u), k),
        "T(0)=0": la.matvec(a, [0.0, 0.0]) == [0.0, 0.0],
    }


def kernel_image() -> dict:
    """Núcleo, imagen y teorema del rango-nulidad."""
    a = [[1.0, 2.0, 3.0], [2.0, 4.0, 6.0]]
    r = la.rank(a)
    columnas = len(a[0])
    return {
        "A": a,
        "columnas": columnas,
        "rango_(dim_imagen)": r,
        "nulidad_(dim_nucleo)": columnas - r,
        "rango+nulidad": r + (columnas - r),
        "teorema_verificado": r + (columnas - r) == columnas,
        "vector_del_nucleo": [2.0, -1.0, 0.0],
        "A·nucleo": la.matvec(a, [2.0, -1.0, 0.0]),
    }


def eigen() -> dict:
    """Autovalores: direcciones que la transformación solo escala."""
    valores, vectores = la.symmetric_eigen(_SIM)
    v0 = [vectores[i][0] for i in range(len(_SIM))]
    av = la.matvec(_SIM, v0)
    return {
        "A": _SIM,
        "autovalores": [round(v, 8) for v in valores],
        "autovector_dominante": [round(x, 8) for x in v0],
        "A·v": [round(x, 8) for x in av],
        "λ·v": [round(x, 8) for x in la.scale(v0, valores[0])],
        "Av=λv": all(abs(a - b) < 1e-6 for a, b in zip(av, la.scale(v0, valores[0]))),
        "traza_es_suma_de_autovalores": math.isclose(sum(valores), _SIM[0][0] + _SIM[1][1], rel_tol=1e-9),
        "det_es_producto_de_autovalores": math.isclose(valores[0] * valores[1], la.determinant(_SIM), rel_tol=1e-9),
    }


def diagonalization() -> dict:
    """A = PDP⁻¹: la base donde la transformación solo escala."""
    valores, p = la.symmetric_eigen(_SIM)
    d = [[valores[i] if i == j else 0.0 for j in range(2)] for i in range(2)]
    reconstruida = la.matmul(la.matmul(p, d), la.transpose(p))
    return {
        "A": _SIM,
        "D_diagonal": [[round(x, 8) for x in row] for row in d],
        "P_ortogonal": [[round(x, 8) for x in row] for row in p],
        "PDPᵀ": [[round(x, 8) for x in row] for row in reconstruida],
        "reconstruccion_ok": all(abs(reconstruida[i][j] - _SIM[i][j]) < 1e-6
                                 for i in range(2) for j in range(2)),
        "A^10_via_D": [[round(x, 3) for x in row] for row in la.matmul(
            la.matmul(p, [[valores[i] ** 10 if i == j else 0.0 for j in range(2)] for i in range(2)]),
            la.transpose(p))],
        "ventaja": "potencias de matrices se calculan sobre la diagonal",
    }


def positive_definite() -> dict:
    """Definida positiva: todos los autovalores positivos, xᵀAx > 0."""
    pos = _SIM
    indef = [[1.0, 2.0], [2.0, 1.0]]
    val_pos, _ = la.symmetric_eigen(pos)
    val_ind, _ = la.symmetric_eigen(indef)
    x = [1.0, -1.0]
    return {
        "A_definida_positiva": pos,
        "autovalores_A": [round(v, 8) for v in val_pos],
        "todos_positivos": all(v > 0 for v in val_pos),
        "B_indefinida": indef,
        "autovalores_B": [round(v, 8) for v in val_ind],
        "xᵀBx_con_x=(1,-1)": la.dot(x, la.matvec(indef, x)),
        "criterio_de_Sylvester_A": la.determinant([[pos[0][0]]]) > 0 and la.determinant(pos) > 0,
        "uso": "matriz de covarianza y Hessiano de un mínimo",
    }


def quadratic_forms() -> dict:
    """La forma cuadrática xᵀAx y sus curvas de nivel."""
    a = _SIM
    puntos = {"(1,0)": [1.0, 0.0], "(0,1)": [0.0, 1.0], "(1,1)": [1.0, 1.0], "(1,-1)": [1.0, -1.0]}
    valores = {k: la.dot(v, la.matvec(a, v)) for k, v in puntos.items()}
    eig, _ = la.symmetric_eigen(a)
    return {
        "A": a,
        "forma": "q(x) = 4x₁² + 2x₁x₂ + 3x₂²",
        "valores": valores,
        "minimo_en_la_esfera_unitaria": round(min(eig), 8),
        "maximo_en_la_esfera_unitaria": round(max(eig), 8),
        "curvas_de_nivel": "elipses porque A es definida positiva",
        "gradiente_es_2Ax": [2 * v for v in la.matvec(a, [1.0, 1.0])],
    }


def lu_decomposition() -> dict:
    """LU: factorizar una vez, resolver muchos sistemas."""
    a = [[4.0, 3.0], [6.0, 3.0]]
    lower, upper = la.lu(a)
    return {
        "A": a,
        "L": [[round(x, 8) for x in row] for row in lower],
        "U": [[round(x, 8) for x in row] for row in upper],
        "LU": [[round(x, 8) for x in row] for row in la.matmul(lower, upper)],
        "reconstruccion_ok": all(abs(la.matmul(lower, upper)[i][j] - a[i][j]) < 1e-9 for i in range(2) for j in range(2)),
        "det_como_producto_de_U": round(upper[0][0] * upper[1][1], 8),
        "coste_factorizacion": "O(n³/3)",
        "coste_por_sistema_extra": "O(n²)",
    }


def qr_decomposition() -> dict:
    """QR por Gram-Schmidt: base ortonormal del espacio columna."""
    a = [[1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]
    q, r = la.qr(a)
    qtq = la.matmul(la.transpose(q), q)
    return {
        "A": a,
        "Q": [[round(x, 6) for x in row] for row in q],
        "R": [[round(x, 6) for x in row] for row in r],
        "QᵀQ": [[round(x, 10) for x in row] for row in qtq],
        "Q_es_ortonormal": all(abs(qtq[i][j] - (1.0 if i == j else 0.0)) < 1e-9
                               for i in range(len(qtq)) for j in range(len(qtq))),
        "QR": [[round(x, 6) for x in row] for row in la.matmul(q, r)],
        "R_es_triangular_superior": abs(r[1][0]) < 1e-9,
    }


def least_squares() -> dict:
    """Mínimos cuadrados por ecuaciones normales."""
    xs = [0.0, 1.0, 2.0, 3.0, 4.0]
    ys = [1.0, 3.1, 4.9, 7.2, 8.9]
    a = [[1.0, x] for x in xs]
    at = la.transpose(a)
    coef, _, _ = la.gaussian_elimination(la.matmul(at, a), la.matvec(at, ys))
    pred = la.matvec(a, coef)
    residuo = la.sub(ys, pred)
    return {
        "datos": list(zip(xs, ys)),
        "intercepto": round(coef[0], 6),
        "pendiente": round(coef[1], 6),
        "predicciones": [round(p, 4) for p in pred],
        "residuos": [round(r, 4) for r in residuo],
        "SSE": round(la.dot(residuo, residuo), 8),
        "residuo_ortogonal_a_las_columnas": all(abs(la.dot(col, residuo)) < 1e-9 for col in at),
    }


def svd_intuition() -> dict:
    """SVD: rotar, escalar, rotar. Existe siempre."""
    a = [[3.0, 0.0], [4.0, 5.0]]
    u, s, v = la.svd(a)
    return {
        "A": a,
        "valores_singulares": [round(x, 6) for x in s],
        "U": [[round(x, 6) for x in row] for row in u],
        "V": [[round(x, 6) for x in row] for row in v],
        "sigma1_es_la_norma_espectral": round(max(s), 6),
        "numero_de_condicion": round(max(s) / min(s), 6),
        "rango_numerico": sum(1 for x in s if x > 1e-10),
        "existe_para_toda_matriz": True,
    }


def svd_compression() -> dict:
    """Aproximación de rango 1 y energía retenida."""
    a = [[4.0, 0.0], [3.0, -5.0]]
    u, s, v = la.svd(a)
    rank1 = [[u[i][0] * s[0] * v[j][0] for j in range(2)] for i in range(2)]
    energia_total = sum(x * x for x in s)
    return {
        "A": a,
        "valores_singulares": [round(x, 6) for x in s],
        "aproximacion_rango_1": [[round(x, 6) for x in row] for row in rank1],
        "error_de_frobenius": round(math.sqrt(sum((a[i][j] - rank1[i][j]) ** 2
                                                  for i in range(2) for j in range(2))), 6),
        "error_teorico_sigma2": round(min(s), 6),
        "energia_retenida_%": round(100 * s[0] ** 2 / energia_total, 4),
        "teorema": "Eckart-Young: la truncación SVD es la mejor aproximación de rango k",
    }


def pseudoinverse() -> dict:
    """Pseudoinversa de Moore-Penrose para sistemas sobredeterminados."""
    a = [[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]]
    b = [1.0, 2.0, 4.0]
    at = la.transpose(a)
    normal = la.matmul(at, a)
    x, _, _ = la.gaussian_elimination(normal, la.matvec(at, b))
    pinv = la.matmul(la.inverse(normal), at)
    return {
        "A_shape": la.shape(a),
        "sistema_sobredeterminado": len(a) > len(a[0]),
        "A⁺": [[round(v, 6) for v in row] for row in pinv],
        "A⁺b": [round(v, 6) for v in la.matvec(pinv, b)],
        "solucion_por_ecuaciones_normales": [round(v, 6) for v in x],
        "coinciden": all(abs(p - q) < 1e-9 for p, q in zip(la.matvec(pinv, b), x)),
        "A⁺A": [[round(v, 10) for v in row] for row in la.matmul(pinv, a)],
    }


def pca() -> dict:
    """PCA como autodescomposición de la covarianza."""
    cov = la.covariance(_DATOS)
    valores, vectores = la.symmetric_eigen(cov)
    total = sum(valores)
    pc1 = [vectores[i][0] for i in range(2)]
    centrado = la.center(_DATOS)
    proyeccion = [round(la.dot(fila, pc1), 6) for fila in centrado]
    return {
        "observaciones": len(_DATOS),
        "medias": [round(m, 6) for m in la.column_means(_DATOS)],
        "covarianza": [[round(x, 6) for x in row] for row in cov],
        "autovalores": [round(v, 6) for v in valores],
        "varianza_explicada_PC1_%": round(100 * valores[0] / total, 4),
        "PC1": [round(x, 6) for x in pc1],
        "primeras_proyecciones": proyeccion[:5],
        "PCA_es_SVD_de_los_datos_centrados": True,
    }


def kronecker() -> dict:
    """Producto de Kronecker: estructura en bloques."""
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[0.0, 5.0], [6.0, 7.0]]
    filas = len(a) * len(b)
    cols = len(a[0]) * len(b[0])
    k = [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])]
          for j in range(cols)] for i in range(filas)]
    return {
        "A_shape": la.shape(a),
        "B_shape": la.shape(b),
        "A⊗B_shape": (filas, cols),
        "A⊗B": k,
        "rango": la.rank(k),
        "rango_A_por_rango_B": la.rank(a) * la.rank(b),
        "uso": "sistemas separables, convoluciones y grafos producto",
    }


def tensors() -> dict:
    """Orden, shape y reordenamiento de índices."""
    t = [[[i * 4 + j * 2 + k for k in range(2)] for j in range(2)] for i in range(2)]
    plano = [v for cara in t for fila in cara for v in fila]
    return {
        "orden": 3,
        "shape": (2, 2, 2),
        "tensor": t,
        "elementos": len(plano),
        "aplanado_row_major": plano,
        "elemento_[1][0][1]": t[1][0][1],
        "indice_lineal": 1 * 4 + 0 * 2 + 1,
        "un_batch_de_imagenes_es_orden_4": "(N, C, H, W)",
    }


def broadcasting() -> dict:
    """Broadcasting: reglas de compatibilidad de shapes."""
    matriz = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    fila = [10.0, 20.0, 30.0]
    columna = [[100.0], [200.0]]
    suma_fila = [[x + f for x, f in zip(row, fila)] for row in matriz]
    suma_col = [[x + col[0] for x in row] for row, col in zip(matriz, columna)]
    return {
        "matriz_shape": (2, 3),
        "fila_shape": (3,),
        "columna_shape": (2, 1),
        "matriz+fila": suma_fila,
        "matriz+columna": suma_col,
        "regla": "las dimensiones se alinean por la derecha; 1 se estira",
        "shapes_incompatibles": "(2,3) + (2,) falla",
        "no_copia_memoria": True,
    }


def einsum() -> dict:
    """Notación de Einstein: índices repetidos se suman."""
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[5.0, 6.0], [7.0, 8.0]]
    ij_jk = la.matmul(a, b)
    traza = sum(a[i][i] for i in range(2))
    hadamard = [[a[i][j] * b[i][j] for j in range(2)] for i in range(2)]
    return {
        "'ij,jk->ik' (producto)": ij_jk,
        "'ii->' (traza)": traza,
        "'ij,ij->ij' (Hadamard)": hadamard,
        "'ij,ij->' (Frobenius)": sum(a[i][j] * b[i][j] for i in range(2) for j in range(2)),
        "'ij->ji' (transpuesta)": la.transpose(a),
        "ventaja": "una sola notación para producto, traza, contracción y reordenamiento",
    }


def capstone_pca_compression() -> dict:
    """Capstone: comprimir una matriz con SVD y medir la pérdida."""
    imagen = [
        [10.0, 12.0, 14.0, 16.0],
        [20.0, 24.0, 28.0, 32.0],
        [30.0, 36.0, 42.0, 48.0],
        [11.0, 13.0, 15.0, 18.0],
    ]
    u, s, v = la.svd(imagen)
    energia = sum(x * x for x in s)
    informe = []
    for k in (1, 2, 3, 4):
        aprox = [[sum(u[i][r] * s[r] * v[j][r] for r in range(k)) for j in range(4)] for i in range(4)]
        err = math.sqrt(sum((imagen[i][j] - aprox[i][j]) ** 2 for i in range(4) for j in range(4)))
        informe.append({
            "rango_k": k,
            "valores_guardados": k * (4 + 4 + 1),
            "error_frobenius": round(err, 6),
            "energia_retenida_%": round(100 * sum(x * x for x in s[:k]) / energia, 4),
        })
    return {
        "matriz_original_shape": (4, 4),
        "valores_originales": 16,
        "valores_singulares": [round(x, 6) for x in s],
        "informe_por_rango": informe,
        "rango_efectivo": sum(1 for x in s if x > 1e-8),
        "conclusion": "la matriz es casi de rango 1: dos filas son múltiplos de un patrón",
    }


DEMOS = {
    "bases_coordinates": bases_coordinates,
    "change_of_basis": change_of_basis,
    "linear_transformations": linear_transformations,
    "kernel_image": kernel_image,
    "eigen": eigen,
    "diagonalization": diagonalization,
    "positive_definite": positive_definite,
    "quadratic_forms": quadratic_forms,
    "lu_decomposition": lu_decomposition,
    "qr_decomposition": qr_decomposition,
    "least_squares": least_squares,
    "svd_intuition": svd_intuition,
    "svd_compression": svd_compression,
    "pseudoinverse": pseudoinverse,
    "pca": pca,
    "kronecker": kronecker,
    "tensors": tensors,
    "broadcasting": broadcasting,
    "einsum": einsum,
    "capstone_pca_compression": capstone_pca_compression,
}

CLASS_DEMOS = {
    "121": "bases_coordinates",
    "122": "change_of_basis",
    "123": "linear_transformations",
    "124": "kernel_image",
    "125": "eigen",
    "126": "diagonalization",
    "127": "positive_definite",
    "128": "quadratic_forms",
    "129": "lu_decomposition",
    "130": "qr_decomposition",
    "131": "least_squares",
    "132": "svd_intuition",
    "133": "svd_compression",
    "134": "pseudoinverse",
    "135": "pca",
    "136": "kronecker",
    "137": "tensors",
    "138": "broadcasting",
    "139": "einsum",
    "140": "capstone_pca_compression",
}
