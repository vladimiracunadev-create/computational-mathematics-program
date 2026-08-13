"""Motor 05 — Álgebra lineal I: vectores y matrices.

Vectores, normas, producto punto, independencia, span, sistemas lineales,
eliminación de Gauss, rango, inversa, determinante y proyección ortogonal.
"""

from __future__ import annotations

import math

from . import _linalg as la

PART = "05"
TITLE = "Álgebra lineal I: vectores y matrices"

_A = [[2.0, 1.0, -1.0], [-3.0, -1.0, 2.0], [-2.0, 1.0, 2.0]]
_B = [8.0, -11.0, -3.0]


def scalars_vectors_matrices() -> dict:
    """Escalar, vector y matriz como objetos con forma y significado."""
    escalar = 3.0
    vector = [1.0, 2.0, 3.0]
    matriz = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
    return {
        "escalar": escalar,
        "vector": vector,
        "shape_vector": (len(vector),),
        "matriz": matriz,
        "shape_matriz": la.shape(matriz),
        "escalar_por_vector": la.scale(vector, escalar),
        "transpuesta_shape": la.shape(la.transpose(matriz)),
        "un_tensor_de_orden_0_es_un_escalar": True,
    }


def vector_operations() -> dict:
    """Suma, resta y combinación lineal con interpretación geométrica."""
    u, v = [1.0, 2.0], [3.0, -1.0]
    return {
        "u": u,
        "v": v,
        "u+v": la.add(u, v),
        "u-v": la.sub(u, v),
        "2u-3v": la.sub(la.scale(u, 2), la.scale(v, 3)),
        "|u+v|": la.norm(la.add(u, v)),
        "|u|+|v|": la.norm(u) + la.norm(v),
        "desigualdad_triangular": la.norm(la.add(u, v)) <= la.norm(u) + la.norm(v),
    }


def dot_product() -> dict:
    """Producto punto: proyección, ángulo y similitud."""
    u, v, w = [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]

    def coseno(a, b):
        return la.dot(a, b) / (la.norm(a) * la.norm(b))

    return {
        "u·v": la.dot(u, v),
        "coseno_u_v": coseno(u, v),
        "angulo_u_v_grados": math.degrees(math.acos(coseno(u, v))),
        "u·w": la.dot(u, w),
        "ortogonales": la.dot(u, w) == 0,
        "u·u_es_|u|²": math.isclose(la.dot(u, u), la.norm(u) ** 2),
        "similitud_coseno_en_embeddings": "misma fórmula, dimensión mayor",
    }


def norms_distances() -> dict:
    """L1, L2 e L∞ sobre el mismo vector."""
    v = [3.0, -4.0, 12.0]
    return {
        "v": v,
        "L1": sum(abs(x) for x in v),
        "L2": la.norm(v),
        "Linf": max(abs(x) for x in v),
        "L2_es_la_hipotenusa": math.isclose(la.norm(v), math.sqrt(sum(x * x for x in v))),
        "orden": "L∞ ≤ L2 ≤ L1",
        "L1_induce_sparsidad": "por eso Lasso usa L1",
    }


def unit_vectors() -> dict:
    """Normalizar separa dirección de magnitud."""
    v = [6.0, 8.0]
    u = la.normalize(v)
    return {
        "v": v,
        "|v|": la.norm(v),
        "v_normalizado": u,
        "|v_normalizado|": la.norm(u),
        "reconstruccion": la.scale(u, la.norm(v)),
        "vector_cero_no_se_normaliza": la.normalize([0.0, 0.0]),
        "uso": "comparar dirección sin que la escala domine",
    }


def linear_combinations() -> dict:
    """Toda combinación lineal de la base canónica reconstruye el vector."""
    e1, e2, e3 = [1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]
    coef = [2.0, -3.0, 5.0]
    combinacion = la.add(la.add(la.scale(e1, coef[0]), la.scale(e2, coef[1])), la.scale(e3, coef[2]))
    return {
        "base_canonica": [e1, e2, e3],
        "coeficientes": coef,
        "combinacion": combinacion,
        "coincide_con_los_coeficientes": combinacion == coef,
        "una_capa_densa_es_una_combinacion_lineal": True,
        "mas_sesgo": "y = Wx + b",
    }


def linear_independence() -> dict:
    """Independencia detectada por el rango, no por inspección."""
    independientes = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    dependientes = [[1.0, 2.0, 3.0], [2.0, 4.0, 6.0], [1.0, 1.0, 1.0]]
    return {
        "conjunto_A": independientes,
        "rango_A": la.rank(independientes),
        "A_independiente": la.rank(independientes) == len(independientes),
        "conjunto_B": dependientes,
        "rango_B": la.rank(dependientes),
        "B_independiente": la.rank(dependientes) == len(dependientes),
        "relacion_en_B": "fila2 = 2·fila1",
        "determinante_B": la.determinant(dependientes),
    }


def span_subspaces() -> dict:
    """El span de dos vectores en ℝ³ es un plano, no todo el espacio."""
    v1, v2 = [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]
    generado = [v1, v2]
    fuera = [0.0, 0.0, 1.0]
    ampliado = generado + [fuera]
    return {
        "generadores": generado,
        "dimension_del_span": la.rank(generado),
        "es_un_plano": la.rank(generado) == 2,
        "vector_fuera_del_span": fuera,
        "rango_al_añadirlo": la.rank(ampliado),
        "ahora_genera_R3": la.rank(ampliado) == 3,
        "subespacio_contiene_al_cero": True,
    }


def matrix_basics() -> dict:
    """Suma, escala y transpuesta de matrices."""
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[0.0, 1.0], [-1.0, 2.0]]
    suma = [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]
    return {
        "A": a,
        "B": b,
        "A+B": suma,
        "3A": [[3 * x for x in row] for row in a],
        "Aᵀ": la.transpose(a),
        "(Aᵀ)ᵀ=A": la.transpose(la.transpose(a)) == a,
        "traza_A": sum(a[i][i] for i in range(len(a))),
    }


def matrix_vector() -> dict:
    """Ax como combinación lineal de las columnas de A."""
    a = [[2.0, 1.0], [0.0, 3.0], [1.0, -1.0]]
    x = [4.0, 5.0]
    columnas = la.transpose(a)
    combinacion = la.add(la.scale(columnas[0], x[0]), la.scale(columnas[1], x[1]))
    return {
        "A_shape": la.shape(a),
        "x": x,
        "Ax": la.matvec(a, x),
        "combinacion_de_columnas": combinacion,
        "coinciden": la.matvec(a, x) == combinacion,
        "lectura": "Ax vive en el espacio columna de A",
        "una_capa_densa": "activaciones = W·entradas + sesgo",
    }


def matrix_product() -> dict:
    """AB ≠ BA y el coste cúbico del producto."""
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[0.0, 1.0], [1.0, 0.0]]
    return {
        "A": a,
        "B": b,
        "AB": la.matmul(a, b),
        "BA": la.matmul(b, a),
        "conmutan": la.matmul(a, b) == la.matmul(b, a),
        "(AB)ᵀ": la.transpose(la.matmul(a, b)),
        "BᵀAᵀ": la.matmul(la.transpose(b), la.transpose(a)),
        "identidad_de_transpuesta": la.transpose(la.matmul(a, b)) == la.matmul(la.transpose(b), la.transpose(a)),
        "coste_naive_nxn": "O(n³)",
    }


def transpose_symmetry() -> dict:
    """Toda matriz cuadrada se descompone en parte simétrica y antisimétrica."""
    a = [[1.0, 2.0], [4.0, 5.0]]
    at = la.transpose(a)
    sim = [[(x + y) / 2 for x, y in zip(ra, rb)] for ra, rb in zip(a, at)]
    anti = [[(x - y) / 2 for x, y in zip(ra, rb)] for ra, rb in zip(a, at)]
    return {
        "A": a,
        "parte_simetrica": sim,
        "parte_antisimetrica": anti,
        "suma_reconstruye_A": [[s + t for s, t in zip(rs, ra)] for rs, ra in zip(sim, anti)] == a,
        "sim_es_simetrica": sim == la.transpose(sim),
        "AᵀA_es_simetrica": la.matmul(at, a) == la.transpose(la.matmul(at, a)),
    }


def linear_systems() -> dict:
    """Sistema 3x3: solución, residuo y unicidad."""
    x, _, _ = la.gaussian_elimination(_A, _B)
    residuo = la.sub(la.matvec(_A, x), _B)
    return {
        "A": _A,
        "b": _B,
        "x": [round(v, 12) for v in x],
        "residuo": [round(v, 12) for v in residuo],
        "norma_del_residuo": la.norm(residuo),
        "determinante": la.determinant(_A),
        "solucion_unica": abs(la.determinant(_A)) > 1e-12,
    }


def gaussian_elimination_demo() -> dict:
    """Eliminación de Gauss con pivoteo parcial, paso a paso."""
    x, u, swaps = la.gaussian_elimination(_A, _B)
    return {
        "matriz_original": _A,
        "triangular_superior": [[round(v, 6) for v in row] for row in u],
        "intercambios_de_fila": swaps,
        "solucion": [round(v, 12) for v in x],
        "pivoteo_evita": "dividir por un pivote casi nulo",
        "coste": "O(n³/3) operaciones",
        "verificacion": [round(v, 12) for v in la.matvec(_A, x)],
    }


def echelon_rank() -> dict:
    """Rango: la dimensión efectiva de la transformación."""
    completa = [[1.0, 2.0], [3.0, 4.0]]
    deficiente = [[1.0, 2.0], [2.0, 4.0]]
    rectangular = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    return {
        "rango_completa": la.rank(completa),
        "rango_deficiente": la.rank(deficiente),
        "rango_rectangular_2x3": la.rank(rectangular),
        "rango_maximo_posible": min(la.shape(rectangular)),
        "deficiente_es_invertible": abs(la.determinant(deficiente)) > 1e-12,
        "nulidad_de_la_deficiente": len(deficiente) - la.rank(deficiente),
        "teorema_rango_nulidad": "rango + nulidad = número de columnas",
    }


def matrix_inverse() -> dict:
    """La inversa existe, pero rara vez conviene calcularla."""
    a = [[4.0, 7.0], [2.0, 6.0]]
    inv = la.inverse(a)
    producto = la.matmul(a, inv)
    return {
        "A": a,
        "A⁻¹": [[round(v, 12) for v in row] for row in inv],
        "A·A⁻¹": [[round(v, 12) for v in row] for row in producto],
        "es_identidad": all(abs(producto[i][j] - (1.0 if i == j else 0.0)) < 1e-12
                            for i in range(2) for j in range(2)),
        "determinante": la.determinant(a),
        "formula_2x2": "1/det · [[d,-b],[-c,a]]",
        "recomendacion": "resolver Ax=b por factorización, no invirtiendo",
    }


def determinants() -> dict:
    """El determinante mide el escalado de volumen y detecta singularidad."""
    a = [[2.0, 0.0], [0.0, 3.0]]
    b = [[1.0, 2.0], [2.0, 4.0]]
    return {
        "A_diagonal": a,
        "det_A": la.determinant(a),
        "escala_areas_por": abs(la.determinant(a)),
        "B_singular": b,
        "det_B": la.determinant(b),
        "B_es_singular": abs(la.determinant(b)) < 1e-12,
        "det(AB)=det(A)det(B)": math.isclose(
            la.determinant(la.matmul(a, [[1.0, 1.0], [0.0, 1.0]])),
            la.determinant(a) * la.determinant([[1.0, 1.0], [0.0, 1.0]]),
        ),
        "det_negativo_invierte_orientacion": la.determinant([[0.0, 1.0], [1.0, 0.0]]) < 0,
    }


def orthogonal_matrices() -> dict:
    """Matriz ortogonal: QᵀQ = I, preserva normas y ángulos."""
    theta = math.radians(37)
    q = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    v = [3.0, 4.0]
    return {
        "Q": [[round(x, 6) for x in row] for row in q],
        "QᵀQ": [[round(x, 12) for x in row] for row in la.matmul(la.transpose(q), q)],
        "det_Q": round(la.determinant(q), 12),
        "|v|": la.norm(v),
        "|Qv|": la.norm(la.matvec(q, v)),
        "preserva_norma": math.isclose(la.norm(la.matvec(q, v)), la.norm(v)),
        "inversa_es_la_transpuesta": True,
        "por_que_importa": "las transformaciones ortogonales no amplifican el error",
    }


def orthogonal_projection() -> dict:
    """Proyección sobre un subespacio y descomposición ortogonal."""
    a = [[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]]
    b = [6.0, 0.0, 0.0]
    at = la.transpose(a)
    normal = la.matmul(at, a)
    rhs = la.matvec(at, b)
    coef, _, _ = la.gaussian_elimination(normal, rhs)
    proy = la.matvec(a, coef)
    residuo = la.sub(b, proy)
    return {
        "columnas_del_subespacio": la.transpose(a),
        "b": b,
        "coeficientes": [round(c, 6) for c in coef],
        "proyeccion": [round(p, 6) for p in proy],
        "residuo": [round(r, 6) for r in residuo],
        "residuo_ortogonal": all(abs(la.dot(col, residuo)) < 1e-9 for col in at),
        "norma_del_residuo": la.norm(residuo),
        "es_la_mejor_aproximacion_en_L2": True,
    }


def capstone_linear_recommender() -> dict:
    """Capstone: recomendación lineal por similitud coseno entre usuarios."""
    usuarios = {
        "ana": [5.0, 3.0, 0.0, 1.0],
        "beto": [4.0, 0.0, 0.0, 1.0],
        "cata": [1.0, 1.0, 0.0, 5.0],
        "dario": [0.0, 0.0, 5.0, 4.0],
    }
    objetivo = "ana"

    def coseno(a, b):
        na, nb = la.norm(a), la.norm(b)
        return 0.0 if na == 0 or nb == 0 else la.dot(a, b) / (na * nb)

    similitudes = {u: round(coseno(usuarios[objetivo], v), 6)
                   for u, v in usuarios.items() if u != objetivo}
    items = len(usuarios[objetivo])
    puntajes = []
    for item in range(items):
        num = sum(similitudes[u] * usuarios[u][item] for u in similitudes)
        den = sum(abs(similitudes[u]) for u in similitudes)
        puntajes.append(round(num / den, 6) if den else 0.0)
    no_vistos = [i for i, v in enumerate(usuarios[objetivo]) if v == 0.0]
    return {
        "usuarios": usuarios,
        "objetivo": objetivo,
        "similitudes": similitudes,
        "vecino_mas_parecido": max(similitudes, key=similitudes.get),
        "puntajes_estimados": puntajes,
        "items_no_vistos": no_vistos,
        "recomendacion": max(no_vistos, key=lambda i: puntajes[i]) if no_vistos else None,
        "todo_es_producto_punto": True,
    }


DEMOS = {
    "scalars_vectors_matrices": scalars_vectors_matrices,
    "vector_operations": vector_operations,
    "dot_product": dot_product,
    "norms_distances": norms_distances,
    "unit_vectors": unit_vectors,
    "linear_combinations": linear_combinations,
    "linear_independence": linear_independence,
    "span_subspaces": span_subspaces,
    "matrix_basics": matrix_basics,
    "matrix_vector": matrix_vector,
    "matrix_product": matrix_product,
    "transpose_symmetry": transpose_symmetry,
    "linear_systems": linear_systems,
    "gaussian_elimination_demo": gaussian_elimination_demo,
    "echelon_rank": echelon_rank,
    "matrix_inverse": matrix_inverse,
    "determinants": determinants,
    "orthogonal_matrices": orthogonal_matrices,
    "orthogonal_projection": orthogonal_projection,
    "capstone_linear_recommender": capstone_linear_recommender,
}

CLASS_DEMOS = {
    "101": "scalars_vectors_matrices",
    "102": "vector_operations",
    "103": "dot_product",
    "104": "norms_distances",
    "105": "unit_vectors",
    "106": "linear_combinations",
    "107": "linear_independence",
    "108": "span_subspaces",
    "109": "matrix_basics",
    "110": "matrix_vector",
    "111": "matrix_product",
    "112": "transpose_symmetry",
    "113": "linear_systems",
    "114": "gaussian_elimination_demo",
    "115": "echelon_rank",
    "116": "matrix_inverse",
    "117": "determinants",
    "118": "orthogonal_matrices",
    "119": "orthogonal_projection",
    "120": "capstone_linear_recommender",
}
