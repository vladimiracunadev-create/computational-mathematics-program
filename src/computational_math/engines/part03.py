"""Motor 03 — Geometría, trigonometría y geometría analítica.

Del espacio a las coordenadas: distancia, ángulo, transformaciones lineales del
plano, coordenadas polares y proyección.
"""

from __future__ import annotations

import math

from . import _linalg as la

PART = "03"
TITLE = "Geometría, trigonometría y geometría analítica"


def distances() -> dict:
    """Distancia euclídea, Manhattan y Chebyshev sobre los mismos puntos."""
    p, q = (1.0, 2.0), (4.0, 6.0)
    return {
        "p": p,
        "q": q,
        "euclidea_L2": math.dist(p, q),
        "manhattan_L1": sum(abs(a - b) for a, b in zip(p, q)),
        "chebyshev_Linf": max(abs(a - b) for a, b in zip(p, q)),
        "punto_medio": tuple((a + b) / 2 for a, b in zip(p, q)),
        "orden_L1>=L2>=Linf": True,
    }


def angles_radians() -> dict:
    """Grados y radianes: por qué el radián es la unidad natural."""
    grados = 30.0
    rad = math.radians(grados)
    h = 1e-7
    derivada_num = (math.sin(rad + h) - math.sin(rad - h)) / (2 * h)
    return {
        "grados": grados,
        "radianes": rad,
        "pi/6": math.pi / 6,
        "vuelta_completa_rad": 2 * math.pi,
        "d(sin)/dx_en_radianes": derivada_num,
        "cos(x)": math.cos(rad),
        "coinciden": math.isclose(derivada_num, math.cos(rad), rel_tol=1e-6),
    }


def similar_triangles() -> dict:
    """Semejanza: los ángulos se conservan, las longitudes escalan."""
    k = 2.5
    a, b, c = 3.0, 4.0, 5.0
    return {
        "triangulo_original": (a, b, c),
        "factor_de_escala": k,
        "triangulo_semejante": (a * k, b * k, c * k),
        "razon_de_perimetros": k,
        "razon_de_areas": k**2,
        "area_original": a * b / 2,
        "area_escalada": (a * k) * (b * k) / 2,
        "angulos_invariantes": True,
    }


def pythagoras() -> dict:
    """Pitágoras, su recíproco y una terna pitagórica generada."""
    m, n = 3, 2
    a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
    return {
        "catetos": (a, b),
        "hipotenusa": c,
        "a²+b²": a * a + b * b,
        "c²": c * c,
        "es_rectangulo": a * a + b * b == c * c,
        "generador_(m,n)": (m, n),
        "triangulo_5_5_7_es_rectangulo": 5**2 + 5**2 == 7**2,
    }


def trig_ratios() -> dict:
    """Seno, coseno y tangente sobre un triángulo rectángulo concreto."""
    opuesto, adyacente = 3.0, 4.0
    hipotenusa = math.hypot(opuesto, adyacente)
    theta = math.atan2(opuesto, adyacente)
    return {
        "opuesto": opuesto,
        "adyacente": adyacente,
        "hipotenusa": hipotenusa,
        "angulo_rad": theta,
        "angulo_grados": math.degrees(theta),
        "sin": math.sin(theta),
        "cos": math.cos(theta),
        "tan": math.tan(theta),
        "tan_es_sin/cos": math.isclose(math.tan(theta), math.sin(theta) / math.cos(theta)),
    }


def trig_identities() -> dict:
    """Identidades fundamentales verificadas en varios ángulos."""
    resultados = {}
    for grados in (0, 30, 45, 60, 90):
        x = math.radians(grados)
        resultados[f"{grados}°"] = {
            "sin²+cos²": math.sin(x) ** 2 + math.cos(x) ** 2,
            "sin(2x)": math.sin(2 * x),
            "2·sin·cos": 2 * math.sin(x) * math.cos(x),
            "identidad_doble_ok": math.isclose(math.sin(2 * x), 2 * math.sin(x) * math.cos(x), abs_tol=1e-12),
        }
    return resultados


def unit_circle() -> dict:
    """El círculo unitario como diccionario de ángulos notables."""
    tabla = {}
    for grados in (0, 90, 180, 270, 360):
        x = math.radians(grados)
        tabla[f"{grados}°"] = (round(math.cos(x), 12), round(math.sin(x), 12))
    return {
        "coordenadas": tabla,
        "radio": 1.0,
        "periodo_sin": 2 * math.pi,
        "sin_es_impar": math.isclose(math.sin(-1.0), -math.sin(1.0)),
        "cos_es_par": math.isclose(math.cos(-1.0), math.cos(1.0)),
    }


def cartesian_coordinates() -> dict:
    """Cuadrantes, simetrías y traslación de origen."""
    puntos = [(3.0, 2.0), (-3.0, 2.0), (-3.0, -2.0), (3.0, -2.0)]

    def cuadrante(p):
        x, y = p
        return 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 else 4

    return {
        "puntos": puntos,
        "cuadrantes": [cuadrante(p) for p in puntos],
        "simetrico_respecto_a_x": (3.0, -2.0),
        "simetrico_respecto_a_y": (-3.0, 2.0),
        "simetrico_respecto_al_origen": (-3.0, -2.0),
        "trasladado_(+1,-1)": [(x + 1, y - 1) for x, y in puntos],
    }


def line_equation() -> dict:
    """Recta en forma pendiente-intercepto y en forma general."""
    p, q = (1.0, 2.0), (5.0, 10.0)
    m = (q[1] - p[1]) / (q[0] - p[0])
    b = p[1] - m * p[0]
    # forma general Ax + By + C = 0
    A, B, C = m, -1.0, b
    return {
        "puntos": (p, q),
        "pendiente": m,
        "intercepto": b,
        "forma_explicita": f"y = {m:.1f}x + {b:.1f}",
        "forma_general": f"{A:.1f}x + {B:.1f}y + {C:.1f} = 0",
        "verifica_p": A * p[0] + B * p[1] + C,
        "pendiente_perpendicular": -1 / m,
    }


def point_line_distance() -> dict:
    """Distancia de un punto a una recta y su proyección."""
    A, B, C = 3.0, -4.0, 5.0   # 3x - 4y + 5 = 0
    px, py = 2.0, 7.0
    d = abs(A * px + B * py + C) / math.hypot(A, B)
    t = (A * px + B * py + C) / (A * A + B * B)
    proj = (px - A * t, py - B * t)
    return {
        "recta": "3x - 4y + 5 = 0",
        "punto": (px, py),
        "distancia": d,
        "pie_de_perpendicular": proj,
        "distancia_al_pie": math.dist((px, py), proj),
        "el_pie_pertenece_a_la_recta": abs(A * proj[0] + B * proj[1] + C) < 1e-12,
    }


def conics() -> dict:
    """Circunferencia, elipse y parábola desde su ecuación."""
    r = 3.0
    a, b = 5.0, 3.0
    c = math.sqrt(a * a - b * b)
    return {
        "circunferencia": "x² + y² = 9",
        "radio": r,
        "area_circulo": math.pi * r * r,
        "elipse": "x²/25 + y²/9 = 1",
        "semieje_mayor": a,
        "semieje_menor": b,
        "distancia_focal": c,
        "excentricidad": c / a,
        "parabola_y=x²_foco": (0.0, 0.25),
    }


def vectors_2d() -> dict:
    """Vector como dirección y magnitud; ángulo entre vectores."""
    u, v = [3.0, 4.0], [-4.0, 3.0]
    cos_theta = la.dot(u, v) / (la.norm(u) * la.norm(v))
    return {
        "u": u,
        "v": v,
        "|u|": la.norm(u),
        "|v|": la.norm(v),
        "u·v": la.dot(u, v),
        "cos_theta": cos_theta,
        "angulo_grados": math.degrees(math.acos(max(-1.0, min(1.0, cos_theta)))),
        "son_ortogonales": abs(la.dot(u, v)) < 1e-12,
        "u_normalizado": la.normalize(u),
    }


def translation_scale() -> dict:
    """Traslación y escala en coordenadas homogéneas."""
    punto = [2.0, 3.0, 1.0]
    T = [[1.0, 0.0, 5.0], [0.0, 1.0, -2.0], [0.0, 0.0, 1.0]]
    S = [[2.0, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 1.0]]
    return {
        "punto_homogeneo": punto,
        "trasladado": la.matvec(T, punto),
        "escalado": la.matvec(S, punto),
        "escala_luego_traslada": la.matvec(la.matmul(T, S), punto),
        "traslada_luego_escala": la.matvec(la.matmul(S, T), punto),
        "el_orden_importa": la.matvec(la.matmul(T, S), punto) != la.matvec(la.matmul(S, T), punto),
    }


def rotation_2d() -> dict:
    """Matriz de rotación: ortogonal y de determinante 1."""
    theta = math.radians(90)
    R = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    v = [1.0, 0.0]
    return {
        "angulo_grados": 90.0,
        "matriz": [[round(x, 12) for x in row] for row in R],
        "R·(1,0)": [round(x, 12) for x in la.matvec(R, v)],
        "determinante": round(la.determinant(R), 12),
        "RᵀR_es_identidad": [[round(x, 12) for x in row] for row in la.matmul(la.transpose(R), R)],
        "preserva_la_norma": math.isclose(la.norm(la.matvec(R, v)), la.norm(v)),
        "cuatro_rotaciones_vuelven_al_origen": True,
    }


def transform_matrices() -> dict:
    """Composición de rotación, escala y reflexión."""
    theta = math.radians(45)
    R = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    S = [[2.0, 0.0], [0.0, 2.0]]
    F = [[1.0, 0.0], [0.0, -1.0]]
    v = [1.0, 1.0]
    return {
        "rotacion_45": [[round(x, 6) for x in row] for row in R],
        "escala_2x": S,
        "reflexion_en_x": F,
        "RS·v": [round(x, 6) for x in la.matvec(la.matmul(R, S), v)],
        "det_rotacion": round(la.determinant(R), 12),
        "det_escala": la.determinant(S),
        "det_reflexion": la.determinant(F),
        "reflexion_invierte_orientacion": la.determinant(F) < 0,
    }


def polar_coordinates() -> dict:
    """Conversión cartesiana ↔ polar y su ida y vuelta."""
    x, y = -3.0, 4.0
    r = math.hypot(x, y)
    theta = math.atan2(y, x)
    return {
        "cartesianas": (x, y),
        "r": r,
        "theta_rad": theta,
        "theta_grados": math.degrees(theta),
        "vuelta_a_cartesianas": (r * math.cos(theta), r * math.sin(theta)),
        "roundtrip_ok": math.isclose(r * math.cos(theta), x) and math.isclose(r * math.sin(theta), y),
        "atan2_maneja_cuadrantes": True,
    }


def planes_3d() -> dict:
    """Plano por su normal, distancia de un punto y producto cruz."""
    a, b = [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]
    normal = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
    punto = [2.0, 3.0, 5.0]
    d = abs(la.dot(normal, punto)) / la.norm(normal)
    return {
        "vector_a": a,
        "vector_b": b,
        "normal_axb": normal,
        "plano": "z = 0",
        "punto": punto,
        "distancia_al_plano": d,
        "normal_es_ortogonal_a_a": abs(la.dot(normal, a)) < 1e-12,
        "norma_del_producto_cruz_es_el_area": la.norm(normal),
    }


def projection() -> dict:
    """Proyección ortogonal de un vector y proyección en perspectiva."""
    v, u = [4.0, 3.0], [1.0, 0.0]
    coef = la.dot(v, u) / la.dot(u, u)
    proy = la.scale(u, coef)
    residuo = la.sub(v, proy)
    f, z = 2.0, 5.0
    return {
        "v": v,
        "direccion_u": u,
        "proyeccion": proy,
        "residuo": residuo,
        "residuo_ortogonal_a_u": abs(la.dot(residuo, u)) < 1e-12,
        "pitagoras": math.isclose(la.norm(v) ** 2, la.norm(proy) ** 2 + la.norm(residuo) ** 2),
        "perspectiva_x'_con_f=2_z=5": v[0] * f / z,
        "objetos_lejanos_se_encogen": True,
    }


def applications_pipeline() -> dict:
    """Pipeline geométrico típico: modelo → mundo → cámara → pantalla."""
    punto_modelo = [1.0, 1.0, 1.0]
    theta = math.radians(30)
    R = [
        [math.cos(theta), -math.sin(theta), 0.0],
        [math.sin(theta), math.cos(theta), 0.0],
        [0.0, 0.0, 1.0],
    ]
    mundo = la.matvec(R, punto_modelo)
    camara = [mundo[0], mundo[1], mundo[2] + 4.0]
    f = 1.5
    pantalla = (f * camara[0] / camara[2], f * camara[1] / camara[2])
    return {
        "espacio_modelo": punto_modelo,
        "tras_rotacion_30": [round(x, 6) for x in mundo],
        "espacio_camara": [round(x, 6) for x in camara],
        "proyeccion_en_pantalla": tuple(round(x, 6) for x in pantalla),
        "etapas": ["modelo", "mundo", "cámara", "proyección", "pantalla"],
        "usado_en": "videojuegos, robótica, visión artificial y realidad aumentada",
    }


def capstone_geometry_engine() -> dict:
    """Capstone: motor 2D que compone transformaciones sobre un polígono."""
    cuadrado = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]
    theta = math.radians(45)
    R = [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    S = [[2.0, 0.0], [0.0, 2.0]]
    M = la.matmul(R, S)
    transformado = [[round(c, 6) for c in la.matvec(M, p)] for p in cuadrado]

    def area(poligono):
        n = len(poligono)
        return abs(sum(poligono[i][0] * poligono[(i + 1) % n][1]
                       - poligono[(i + 1) % n][0] * poligono[i][1] for i in range(n))) / 2

    return {
        "poligono_original": cuadrado,
        "matriz_compuesta": [[round(x, 6) for x in row] for row in M],
        "poligono_transformado": transformado,
        "area_original": area(cuadrado),
        "area_transformada": round(area(transformado), 6),
        "determinante": round(la.determinant(M), 6),
        "area_escala_como_|det|": math.isclose(area(transformado), area(cuadrado) * abs(la.determinant(M)), rel_tol=1e-9),
    }


DEMOS = {
    "distances": distances,
    "angles_radians": angles_radians,
    "similar_triangles": similar_triangles,
    "pythagoras": pythagoras,
    "trig_ratios": trig_ratios,
    "trig_identities": trig_identities,
    "unit_circle": unit_circle,
    "cartesian_coordinates": cartesian_coordinates,
    "line_equation": line_equation,
    "point_line_distance": point_line_distance,
    "conics": conics,
    "vectors_2d": vectors_2d,
    "translation_scale": translation_scale,
    "rotation_2d": rotation_2d,
    "transform_matrices": transform_matrices,
    "polar_coordinates": polar_coordinates,
    "planes_3d": planes_3d,
    "projection": projection,
    "applications_pipeline": applications_pipeline,
    "capstone_geometry_engine": capstone_geometry_engine,
}

CLASS_DEMOS = {
    "061": "distances",
    "062": "angles_radians",
    "063": "similar_triangles",
    "064": "pythagoras",
    "065": "trig_ratios",
    "066": "trig_identities",
    "067": "unit_circle",
    "068": "cartesian_coordinates",
    "069": "line_equation",
    "070": "point_line_distance",
    "071": "conics",
    "072": "vectors_2d",
    "073": "translation_scale",
    "074": "rotation_2d",
    "075": "transform_matrices",
    "076": "polar_coordinates",
    "077": "planes_3d",
    "078": "projection",
    "079": "applications_pipeline",
    "080": "capstone_geometry_engine",
}
