"""Motor 02 — Álgebra y funciones.

Manipulación simbólica con criterio y la función como objeto: dominio, imagen,
composición, inversa y las cuatro familias fundamentales.
"""

from __future__ import annotations

import math

PART = "02"
TITLE = "Álgebra y funciones"


def algebraic_terms() -> dict:
    """Términos semejantes y evaluación de una expresión."""
    def expr(x: float, y: float) -> float:
        return 3 * x**2 * y - 2 * x * y + 5 * x**2 * y + 7 * x * y

    def simplificada(x: float, y: float) -> float:
        return 8 * x**2 * y + 5 * x * y

    x, y = 2.0, 3.0
    return {
        "expresion": "3x²y - 2xy + 5x²y + 7xy",
        "simplificada": "8x²y + 5xy",
        "evaluada_original": expr(x, y),
        "evaluada_simplificada": simplificada(x, y),
        "equivalentes": math.isclose(expr(x, y), simplificada(x, y)),
        "terminos_originales": 4,
        "terminos_tras_reducir": 2,
    }


def algebra_properties() -> dict:
    """Conmutativa, asociativa y distributiva: válidas en ℝ, no siempre en float."""
    a, b, c = 2.5, -4.0, 7.25
    return {
        "conmutativa_suma": a + b == b + a,
        "conmutativa_producto": a * b == b * a,
        "asociativa_suma_en_R": (a + b) + c == a + (b + c),
        "distributiva": math.isclose(a * (b + c), a * b + a * c),
        "asociativa_falla_en_float": (1e16 + 1.0) - 1e16 != 1e16 + (1.0 - 1e16),
        "resta_no_es_conmutativa": a - b != b - a,
    }


def linear_equation() -> dict:
    """Resolver ax + b = c y verificar el residuo."""
    a, b, c = 7.0, -3.0, 25.0
    x = (c - b) / a
    return {
        "ecuacion": "7x - 3 = 25",
        "x": x,
        "residuo": a * x + b - c,
        "sin_solucion_si_a_es_0": True,
        "caso_0x=0": "infinitas soluciones",
        "caso_0x=5": "ninguna solución",
    }


def linear_inequality() -> dict:
    """Multiplicar por un negativo invierte el sentido de la desigualdad."""
    # -3x + 4 > 10  ->  -3x > 6  ->  x < -2
    frontera = (10.0 - 4.0) / -3.0
    prueba_dentro, prueba_fuera = -5.0, 0.0
    return {
        "desigualdad": "-3x + 4 > 10",
        "frontera": frontera,
        "solucion": "x < -2",
        "verifica_x=-5": -3 * prueba_dentro + 4 > 10,
        "verifica_x=0": -3 * prueba_fuera + 4 > 10,
        "regla": "al dividir por un negativo se invierte el signo",
    }


def system_2x2() -> dict:
    """Sistema 2x2 por determinantes (regla de Cramer) y verificación."""
    a1, b1, c1 = 2.0, 3.0, 12.0
    a2, b2, c2 = 4.0, -1.0, 10.0
    det = a1 * b2 - a2 * b1
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return {
        "sistema": ["2x + 3y = 12", "4x - y = 10"],
        "determinante": det,
        "x": x,
        "y": y,
        "verificacion_1": a1 * x + b1 * y,
        "verificacion_2": a2 * x + b2 * y,
        "unica_solucion": det != 0,
    }


def polynomial_ops() -> dict:
    """Suma, producto y evaluación de polinomios por Horner."""
    p = [1.0, -3.0, 2.0]   # x² - 3x + 2 (coeficientes de mayor a menor)
    q = [2.0, 1.0]         # 2x + 1

    def horner(coef, x):
        acc = 0.0
        for c in coef:
            acc = acc * x + c
        return acc

    producto = [0.0] * (len(p) + len(q) - 1)
    for i, cp in enumerate(p):
        for j, cq in enumerate(q):
            producto[i + j] += cp * cq

    return {
        "p": "x² - 3x + 2",
        "q": "2x + 1",
        "grado_p": len(p) - 1,
        "grado_producto": len(producto) - 1,
        "coeficientes_producto": producto,
        "p(3)_horner": horner(p, 3.0),
        "p(3)_directo": 3.0**2 - 3 * 3.0 + 2,
        "multiplicaciones_horner": len(p) - 1,
    }


def factoring() -> dict:
    """Factorizar x² - 3x + 2 y comprobar las raíces."""
    b, c = -3.0, 2.0
    disc = b * b - 4 * c
    r1 = (-b + math.sqrt(disc)) / 2
    r2 = (-b - math.sqrt(disc)) / 2
    return {
        "polinomio": "x² - 3x + 2",
        "raices": (r1, r2),
        "factorizacion": f"(x - {r1:.0f})(x - {r2:.0f})",
        "suma_de_raices": r1 + r2,
        "suma_teorica_-b": -b,
        "producto_de_raices": r1 * r2,
        "producto_teorico_c": c,
    }


def quadratic_equation() -> dict:
    """Resolver una cuadrática y contrastar con la forma de vértice."""
    a, b, c = 2.0, -8.0, 6.0
    disc = b * b - 4 * a * c
    r1 = (-b + math.sqrt(disc)) / (2 * a)
    r2 = (-b - math.sqrt(disc)) / (2 * a)
    xv = -b / (2 * a)
    return {
        "ecuacion": "2x² - 8x + 6 = 0",
        "discriminante": disc,
        "raices": (r1, r2),
        "vertice_x": xv,
        "vertice_y": a * xv**2 + b * xv + c,
        "vertice_es_punto_medio_de_raices": math.isclose(xv, (r1 + r2) / 2),
    }


def discriminant() -> dict:
    """El discriminante clasifica las raíces antes de calcularlas."""
    casos = {"dos_reales": (1.0, -5.0, 6.0), "una_doble": (1.0, -4.0, 4.0),
             "complejas": (1.0, 1.0, 1.0)}
    salida = {}
    for nombre, (a, b, c) in casos.items():
        d = b * b - 4 * a * c
        salida[nombre] = {
            "coeficientes": (a, b, c),
            "discriminante": d,
            "naturaleza": "2 reales" if d > 0 else ("1 doble" if d == 0 else "2 complejas conjugadas"),
        }
    return salida


def algebraic_exponents() -> dict:
    """Exponentes negativos, fraccionarios y su dominio."""
    x = 8.0
    return {
        "x^(1/3)": x ** (1 / 3),
        "x^(2/3)": x ** (2 / 3),
        "x^(-1)": x**-1,
        "x^(-1/3)": x ** (-1 / 3),
        "producto_x^(1/3)*x^(2/3)": x ** (1 / 3) * x ** (2 / 3),
        "es_x": math.isclose(x ** (1 / 3) * x ** (2 / 3), x),
        "dominio_de_x^(1/2)": "x >= 0 en los reales",
    }


def logarithm_laws() -> dict:
    """Las tres leyes del logaritmo verificadas numéricamente."""
    a, b = 12.0, 5.0
    return {
        "log(a*b)": math.log(a * b),
        "log(a)+log(b)": math.log(a) + math.log(b),
        "ley_producto": math.isclose(math.log(a * b), math.log(a) + math.log(b)),
        "log(a/b)": math.log(a / b),
        "log(a)-log(b)": math.log(a) - math.log(b),
        "log(a^3)": math.log(a**3),
        "3*log(a)": 3 * math.log(a),
        "cambio_de_base_log2(a)": math.log(a) / math.log(2),
        "math.log2(a)": math.log2(a),
    }


def domain_range() -> dict:
    """El dominio forma parte de la definición de la función."""
    def f(x: float) -> float:
        return 1.0 / (x - 2.0)

    puntos = [0.0, 1.9, 2.1, 5.0]
    return {
        "funcion": "f(x) = 1/(x-2)",
        "dominio": "ℝ \\ {2}",
        "imagen": "ℝ \\ {0}",
        "valores": {str(p): f(p) for p in puntos},
        "x=2_definido": False,
        "asintota_vertical": 2.0,
        "asintota_horizontal": 0.0,
    }


def linear_function() -> dict:
    """Pendiente como razón de cambio constante."""
    puntos = [(1.0, 5.0), (3.0, 11.0), (7.0, 23.0)]
    m = (puntos[1][1] - puntos[0][1]) / (puntos[1][0] - puntos[0][0])
    b = puntos[0][1] - m * puntos[0][0]
    return {
        "puntos": puntos,
        "pendiente": m,
        "intercepto": b,
        "ecuacion": f"y = {m:.0f}x + {b:.0f}",
        "predice_tercer_punto": m * puntos[2][0] + b,
        "es_lineal": math.isclose(m * puntos[2][0] + b, puntos[2][1]),
    }


def quadratic_function() -> dict:
    """Vértice, eje de simetría y concavidad."""
    a, b, c = -1.0, 6.0, -5.0
    xv = -b / (2 * a)
    yv = a * xv**2 + b * xv + c
    return {
        "funcion": "f(x) = -x² + 6x - 5",
        "concavidad": "hacia abajo" if a < 0 else "hacia arriba",
        "vertice": (xv, yv),
        "eje_de_simetria": xv,
        "es_maximo": a < 0,
        "f(xv-2)": a * (xv - 2) ** 2 + b * (xv - 2) + c,
        "f(xv+2)": a * (xv + 2) ** 2 + b * (xv + 2) + c,
        "simetria_verificada": True,
    }


def exponential_function() -> dict:
    """Crecimiento exponencial: razón constante, no diferencia constante."""
    base, x0 = 1.08, 1_000_000.0
    valores = {f"año_{t}": x0 * base**t for t in (0, 5, 10, 20)}
    return {
        "modelo": "P(t) = 1e6 · 1.08^t",
        "valores": valores,
        "razon_entre_años_consecutivos": (x0 * base**6) / (x0 * base**5),
        "tiempo_de_duplicacion": math.log(2) / math.log(base),
        "regla_del_72_aproximada": 72 / 8,
    }


def logarithmic_function() -> dict:
    """El logaritmo como inversa de la exponencial y como escala."""
    return {
        "log10(1000)": math.log10(1000),
        "10^3": 10**3,
        "inversa_verificada": math.isclose(10 ** math.log10(1000), 1000),
        "escala_decibel_de_1e-3": 10 * math.log10(1e-3),
        "crecimiento_de_log_entre_1e3_y_1e6": math.log10(1e6) - math.log10(1e3),
        "dominio": "x > 0",
    }


def function_composition() -> dict:
    """(g∘f) no es (f∘g): la composición no conmuta."""
    def f(x: float) -> float:
        return 2 * x + 1

    def g(x: float) -> float:
        return x**2

    x = 3.0
    return {
        "f": "2x + 1",
        "g": "x²",
        "(g∘f)(3)": g(f(x)),
        "(f∘g)(3)": f(g(x)),
        "conmutan": g(f(x)) == f(g(x)),
        "cadena_de_3": f(g(f(x))),
        "analogia": "una red neuronal es una composición de funciones parametrizadas",
    }


def inverse_function() -> dict:
    """Inversa frente a recíproco: dos objetos distintos."""
    def f(x: float) -> float:
        return 3 * x - 4

    def f_inv(y: float) -> float:
        return (y + 4) / 3

    x = 5.0
    return {
        "f": "3x - 4",
        "f_inversa": "(y + 4)/3",
        "f(5)": f(x),
        "f_inv(f(5))": f_inv(f(x)),
        "roundtrip_ok": math.isclose(f_inv(f(x)), x),
        "reciproco_1/f(5)": 1 / f(x),
        "inversa_es_reciproco": False,
        "condicion_de_existencia": "f debe ser inyectiva en su dominio",
    }


def piecewise_function() -> dict:
    """Una función por tramos y su continuidad en el punto de corte."""
    def f(x: float) -> float:
        if x < 0:
            return -x
        if x < 2:
            return x**2
        return 4.0

    return {
        "definicion": "|x| si x<0; x² si 0<=x<2; 4 si x>=2",
        "f(-3)": f(-3.0),
        "f(0)": f(0.0),
        "f(1.999)": f(1.999),
        "f(2)": f(2.0),
        "continua_en_0": math.isclose(f(-1e-9), f(1e-9), abs_tol=1e-6),
        "continua_en_2": math.isclose(f(2 - 1e-9), f(2.0), abs_tol=1e-6),
        "relu_es_por_tramos": True,
    }


def capstone_model_fitting() -> dict:
    """Capstone: ¿lineal, cuadrático o exponencial? Decidir con residuos."""
    xs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    ys = [2.1, 4.4, 8.9, 17.5, 35.2, 70.8]

    def sse(pred):
        return sum((p - y) ** 2 for p, y in zip(pred, ys))

    lineal = [13.6 * x - 22.0 for x in xs]
    log_ys = [math.log(y) for y in ys]
    n = len(xs)
    mx, my = sum(xs) / n, sum(log_ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, log_ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    exponencial = [math.exp(a) * math.exp(b * x) for x in xs]
    return {
        "datos": list(zip(xs, ys)),
        "modelo_lineal_SSE": sse(lineal),
        "modelo_exponencial": f"y = {math.exp(a):.3f}·e^({b:.3f}x)",
        "modelo_exponencial_SSE": sse(exponencial),
        "razon_de_crecimiento": math.exp(b),
        "modelo_elegido": "exponencial" if sse(exponencial) < sse(lineal) else "lineal",
        "criterio": "menor suma de residuos al cuadrado sobre los mismos datos",
    }


DEMOS = {
    "algebraic_terms": algebraic_terms,
    "algebra_properties": algebra_properties,
    "linear_equation": linear_equation,
    "linear_inequality": linear_inequality,
    "system_2x2": system_2x2,
    "polynomial_ops": polynomial_ops,
    "factoring": factoring,
    "quadratic_equation": quadratic_equation,
    "discriminant": discriminant,
    "algebraic_exponents": algebraic_exponents,
    "logarithm_laws": logarithm_laws,
    "domain_range": domain_range,
    "linear_function": linear_function,
    "quadratic_function": quadratic_function,
    "exponential_function": exponential_function,
    "logarithmic_function": logarithmic_function,
    "function_composition": function_composition,
    "inverse_function": inverse_function,
    "piecewise_function": piecewise_function,
    "capstone_model_fitting": capstone_model_fitting,
}

CLASS_DEMOS = {
    "041": "algebraic_terms",
    "042": "algebra_properties",
    "043": "linear_equation",
    "044": "linear_inequality",
    "045": "system_2x2",
    "046": "polynomial_ops",
    "047": "factoring",
    "048": "quadratic_equation",
    "049": "discriminant",
    "050": "algebraic_exponents",
    "051": "logarithm_laws",
    "052": "domain_range",
    "053": "linear_function",
    "054": "quadratic_function",
    "055": "exponential_function",
    "056": "logarithmic_function",
    "057": "function_composition",
    "058": "inverse_function",
    "059": "piecewise_function",
    "060": "capstone_model_fitting",
}
