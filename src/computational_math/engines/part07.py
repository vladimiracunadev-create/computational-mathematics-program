"""Motor 07 — Cálculo diferencial e integral.

Límite, continuidad, derivada, reglas, Taylor, optimización de una variable,
integral definida y teorema fundamental del cálculo.
"""

from __future__ import annotations

import math

PART = "07"
TITLE = "Cálculo diferencial e integral"


def _central(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def limit_intuition() -> dict:
    """sin(x)/x cuando x→0: indeterminado en el punto, definido en el límite."""
    def f(x):
        return math.sin(x) / x

    tabla = {f"x={h:g}": f(h) for h in (1.0, 0.1, 0.01, 1e-3, 1e-6)}
    return {
        "funcion": "sin(x)/x",
        "definida_en_0": False,
        "tabla_de_aproximacion": tabla,
        "limite": 1.0,
        "error_en_1e-6": abs(f(1e-6) - 1.0),
        "por_la_izquierda": f(-1e-6),
        "limites_laterales_coinciden": math.isclose(f(1e-6), f(-1e-6), rel_tol=1e-9),
    }


def algebraic_limits() -> dict:
    """Indeterminación 0/0 resuelta por factorización."""
    def f(x):
        return (x * x - 4) / (x - 2)

    return {
        "funcion": "(x²-4)/(x-2)",
        "en_x=2": "indeterminado 0/0",
        "simplificada": "x + 2",
        "limite_en_2": 4.0,
        "f(2.0001)": f(2.0001),
        "f(1.9999)": f(1.9999),
        "error": abs(f(2.0001) - 4.0),
        "leccion": "la indeterminación es de la expresión, no del límite",
    }


def continuity() -> dict:
    """Los tres requisitos de continuidad en un punto."""
    def salto(x):
        return 0.0 if x < 1 else 1.0

    def removible(x):
        return (x * x - 1) / (x - 1) if x != 1 else 5.0

    return {
        "funcion_con_salto": {"limite_izq": salto(0.999), "limite_der": salto(1.001),
                              "continua": salto(0.999) == salto(1.001)},
        "discontinuidad_removible": {"limite": 2.0, "valor_asignado": removible(1.0),
                                     "continua": removible(1.0) == 2.0},
        "requisitos": ["f(a) existe", "el límite existe", "coinciden"],
        "continua_no_implica_derivable": "|x| en 0",
        "derivable_implica_continua": True,
    }


def derivative_as_rate() -> dict:
    """Derivada como límite del cociente incremental."""
    def f(x):
        return x**2

    x0 = 3.0
    tabla = {f"h={h:g}": (f(x0 + h) - f(x0)) / h for h in (1.0, 0.1, 0.01, 1e-4)}
    return {
        "funcion": "x²",
        "punto": x0,
        "cocientes_incrementales": tabla,
        "derivada_exacta_2x": 2 * x0,
        "diferencia_central": _central(f, x0),
        "error_central": abs(_central(f, x0) - 2 * x0),
        "la_central_es_de_orden_h²": True,
    }


def derivative_rules() -> dict:
    """Reglas de potencia, suma y constante verificadas numéricamente."""
    casos = {
        "x³ en 2": (lambda x: x**3, lambda x: 3 * x**2, 2.0),
        "5x en 7": (lambda x: 5 * x, lambda x: 5.0, 7.0),
        "x³+5x en 2": (lambda x: x**3 + 5 * x, lambda x: 3 * x**2 + 5, 2.0),
        "constante 4": (lambda x: 4.0, lambda x: 0.0, 1.0),
    }
    salida = {}
    for nombre, (f, df, x) in casos.items():
        salida[nombre] = {
            "numerica": round(_central(f, x), 8),
            "analitica": df(x),
            "coinciden": math.isclose(_central(f, x), df(x), abs_tol=1e-5),
        }
    return salida


def product_quotient_rule() -> dict:
    """Regla del producto y del cociente."""
    f = lambda x: x**2          # noqa: E731
    g = lambda x: math.sin(x)   # noqa: E731
    x = 1.3
    producto_num = _central(lambda t: f(t) * g(t), x)
    producto_reg = 2 * x * math.sin(x) + x**2 * math.cos(x)
    cociente_num = _central(lambda t: f(t) / g(t), x)
    cociente_reg = (2 * x * math.sin(x) - x**2 * math.cos(x)) / math.sin(x) ** 2
    return {
        "f": "x²", "g": "sin(x)", "x": x,
        "(fg)'_numerica": round(producto_num, 8),
        "(fg)'_regla": round(producto_reg, 8),
        "producto_ok": math.isclose(producto_num, producto_reg, rel_tol=1e-5),
        "(f/g)'_numerica": round(cociente_num, 8),
        "(f/g)'_regla": round(cociente_reg, 8),
        "cociente_ok": math.isclose(cociente_num, cociente_reg, rel_tol=1e-5),
    }


def chain_rule() -> dict:
    """La regla de la cadena: el mecanismo entero de backpropagation."""
    f = lambda u: math.sin(u)        # noqa: E731
    g = lambda x: x**2 + 1           # noqa: E731
    x = 1.5
    numerica = _central(lambda t: f(g(t)), x)
    analitica = math.cos(g(x)) * (2 * x)
    return {
        "composicion": "sin(x²+1)",
        "x": x,
        "df/du_en_g(x)": math.cos(g(x)),
        "dg/dx": 2 * x,
        "producto_de_la_cadena": round(analitica, 8),
        "derivada_numerica": round(numerica, 8),
        "coinciden": math.isclose(numerica, analitica, rel_tol=1e-5),
        "cadena_de_3_niveles": round(_central(lambda t: math.exp(math.sin(t**2)), 0.8), 8),
        "en_deep_learning": "cada capa aporta un factor al producto",
    }


def exp_log_derivatives() -> dict:
    """e^x es su propia derivada; log tiene derivada 1/x."""
    x = 2.0
    return {
        "d(e^x)/dx_numerica": round(_central(math.exp, x), 8),
        "e^x": math.exp(x),
        "es_su_propia_derivada": math.isclose(_central(math.exp, x), math.exp(x), rel_tol=1e-6),
        "d(ln x)/dx_numerica": round(_central(math.log, x), 8),
        "1/x": 1 / x,
        "d(a^x)/dx_con_a=3": round(_central(lambda t: 3.0**t, x), 8),
        "a^x·ln(a)": 3.0**x * math.log(3),
    }


def trig_derivatives() -> dict:
    """Derivadas trigonométricas y su ciclo de periodo 4."""
    x = 0.7
    return {
        "d(sin)/dx": round(_central(math.sin, x), 8),
        "cos(x)": math.cos(x),
        "d(cos)/dx": round(_central(math.cos, x), 8),
        "-sin(x)": -math.sin(x),
        "d(tan)/dx": round(_central(math.tan, x), 8),
        "sec²(x)": 1 / math.cos(x) ** 2,
        "ciclo": "sin → cos → -sin → -cos → sin",
        "cuarta_derivada_de_sin_es_sin": True,
    }


def implicit_differentiation() -> dict:
    """Derivación implícita sobre la circunferencia x²+y²=25."""
    x0 = 3.0
    y0 = math.sqrt(25 - x0**2)
    dydx = -x0 / y0

    def y(x):
        return math.sqrt(25 - x * x)

    return {
        "ecuacion": "x² + y² = 25",
        "punto": (x0, y0),
        "dy/dx_implicita": dydx,
        "dy/dx_numerica": round(_central(y, x0), 8),
        "coinciden": math.isclose(_central(y, x0), dydx, rel_tol=1e-5),
        "recta_tangente": f"y - {y0:.1f} = {dydx:.4f}(x - {x0:.1f})",
        "tangente_perpendicular_al_radio": abs(dydx * (y0 / x0) + 1) < 1e-9,
    }


def taylor_approximation() -> dict:
    """Taylor de e^x en 0: el error cae con el grado."""
    x = 0.5
    informe = []
    acumulado = 0.0
    for n in range(6):
        acumulado += x**n / math.factorial(n)
        informe.append({
            "grado": n,
            "aproximacion": round(acumulado, 10),
            "error": round(abs(math.exp(x) - acumulado), 12),
        })
    return {
        "funcion": "e^x en x=0.5",
        "valor_exacto": math.exp(x),
        "informe": informe,
        "aproximacion_lineal": 1 + x,
        "cota_de_error_grado_5": round(math.exp(x) * x**6 / math.factorial(6), 12),
        "uso": "linealizar un modelo, métodos de segundo orden, análisis de convergencia",
    }


def extrema() -> dict:
    """Máximos y mínimos por derivada y criterio de la segunda derivada."""
    def f(x):
        return x**3 - 3 * x

    criticos = [-1.0, 1.0]
    salida = {}
    for c in criticos:
        segunda = (f(c + 1e-4) - 2 * f(c) + f(c - 1e-4)) / 1e-8
        salida[f"x={c}"] = {
            "f(x)": f(c),
            "f'(x)": round(_central(f, c), 6),
            "f''(x)": round(segunda, 4),
            "tipo": "mínimo local" if segunda > 0 else "máximo local",
        }
    salida["extremos_globales_en_R"] = "no existen: f no está acotada"
    return salida


def integral_as_accumulation() -> dict:
    """Sumas de Riemann convergiendo a la integral."""
    def f(x):
        return x**2

    a, b, exacto = 0.0, 1.0, 1 / 3
    informe = []
    for n in (4, 16, 64, 256):
        h = (b - a) / n
        suma = sum(f(a + (i + 0.5) * h) * h for i in range(n))
        informe.append({"n": n, "suma": round(suma, 10), "error": round(abs(suma - exacto), 12)})
    return {
        "integrando": "x²",
        "intervalo": (a, b),
        "valor_exacto_1/3": exacto,
        "sumas_de_riemann": informe,
        "orden_de_convergencia": "el error del punto medio cae como h²",
    }


def definite_integral() -> dict:
    """Propiedades de la integral definida."""
    def f(x):
        return x**2

    def integra(a, b, n=2000):
        h = (b - a) / n
        return sum(f(a + (i + 0.5) * h) * h for i in range(n))

    return {
        "∫₀¹x²": round(integra(0, 1), 8),
        "∫₁²x²": round(integra(1, 2), 8),
        "∫₀²x²": round(integra(0, 2), 8),
        "aditividad": math.isclose(integra(0, 1) + integra(1, 2), integra(0, 2), rel_tol=1e-6),
        "∫₁⁰x² (orientación)": round(-integra(0, 1), 8),
        "∫₀⁰x²": 0.0,
        "valor_medio_en_[0,2]": round(integra(0, 2) / 2, 8),
    }


def antiderivatives() -> dict:
    """La antiderivada no es única: difiere en una constante."""
    def F1(x):
        return x**3 / 3

    def F2(x):
        return x**3 / 3 + 7

    x = 2.0
    return {
        "f": "x²",
        "F1": "x³/3",
        "F2": "x³/3 + 7",
        "F1'(2)": round(_central(F1, x), 8),
        "F2'(2)": round(_central(F2, x), 8),
        "misma_derivada": math.isclose(_central(F1, x), _central(F2, x), rel_tol=1e-8),
        "diferencia_constante": F2(x) - F1(x),
        "la_constante_desaparece_en_la_definida": (F2(3) - F2(1)) - (F1(3) - F1(1)),
    }


def fundamental_theorem() -> dict:
    """Teorema fundamental: derivar deshace integrar."""
    def f(x):
        return math.cos(x)

    def F(x, n=4000):
        h = x / n
        return sum(f((i + 0.5) * h) * h for i in range(n)) if n else 0.0

    x = 1.2
    return {
        "f": "cos(x)",
        "F(x)=∫₀ˣcos": round(F(x), 8),
        "sin(x)": math.sin(x),
        "primera_parte_ok": math.isclose(F(x), math.sin(x), abs_tol=1e-6),
        "dF/dx_numerica": round((F(x + 1e-4) - F(x - 1e-4)) / 2e-4, 6),
        "f(x)": f(x),
        "segunda_parte_ok": math.isclose((F(x + 1e-4) - F(x - 1e-4)) / 2e-4, f(x), abs_tol=1e-4),
    }


def substitution() -> dict:
    """Integración por sustitución: la regla de la cadena al revés."""
    def integra(f, a, b, n=4000):
        h = (b - a) / n
        return sum(f(a + (i + 0.5) * h) * h for i in range(n))

    directo = integra(lambda x: 2 * x * math.cos(x * x), 0.0, 1.0)
    sustituido = integra(math.cos, 0.0, 1.0)   # u = x², du = 2x dx
    return {
        "integral": "∫₀¹ 2x·cos(x²) dx",
        "sustitucion": "u = x², du = 2x dx",
        "integral_transformada": "∫₀¹ cos(u) du",
        "valor_directo": round(directo, 8),
        "valor_sustituido": round(sustituido, 8),
        "valor_analitico_sin(1)": math.sin(1),
        "coinciden": math.isclose(directo, math.sin(1), abs_tol=1e-6),
    }


def integration_by_parts() -> dict:
    """Integración por partes: la regla del producto al revés."""
    def integra(f, a, b, n=6000):
        h = (b - a) / n
        return sum(f(a + (i + 0.5) * h) * h for i in range(n))

    numerica = integra(lambda x: x * math.exp(x), 0.0, 1.0)
    analitica = 1.0   # [x·e^x - e^x]₀¹ = (e - e) - (0 - 1) = 1
    return {
        "integral": "∫₀¹ x·eˣ dx",
        "u": "x", "dv": "eˣ dx",
        "formula": "uv - ∫v du",
        "resultado_analitico": analitica,
        "resultado_numerico": round(numerica, 8),
        "error": round(abs(numerica - analitica), 10),
        "criterio_LIATE": "elegir u en el orden log, inversa, algebraica, trig, exponencial",
    }


def numerical_integration_intro() -> dict:
    """Trapecio frente a Simpson sobre la misma integral."""
    def f(x):
        return math.exp(-x * x)

    a, b, n = 0.0, 1.0, 100
    h = (b - a) / n
    trap = h * (f(a) / 2 + sum(f(a + i * h) for i in range(1, n)) + f(b) / 2)
    simp = h / 3 * (f(a) + f(b)
                    + 4 * sum(f(a + i * h) for i in range(1, n, 2))
                    + 2 * sum(f(a + i * h) for i in range(2, n, 2)))
    referencia = math.sqrt(math.pi) / 2 * math.erf(1.0)
    return {
        "integrando": "e^(-x²)",
        "intervalo": (a, b),
        "subintervalos": n,
        "trapecio": round(trap, 12),
        "simpson": round(simp, 12),
        "referencia_erf": round(referencia, 12),
        "error_trapecio": round(abs(trap - referencia), 14),
        "error_simpson": round(abs(simp - referencia), 14),
        "ordenes": "trapecio O(h²), Simpson O(h⁴)",
    }


def capstone_optimize_and_accumulate() -> dict:
    """Capstone: derivar para optimizar e integrar para acumular una señal."""
    def señal(t):
        return math.exp(-0.5 * t) * math.sin(3 * t)

    # máximo por búsqueda de raíz de la derivada (bisección sobre f')
    lo, hi = 0.1, 1.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if _central(señal, lo) * _central(señal, mid) <= 0:
            hi = mid
        else:
            lo = mid
    t_max = (lo + hi) / 2

    n = 4000
    h = 6.0 / n
    energia = sum(señal((i + 0.5) * h) ** 2 * h for i in range(n))
    area = sum(señal((i + 0.5) * h) * h for i in range(n))
    return {
        "señal": "e^(-0.5t)·sin(3t)",
        "t_del_primer_maximo": round(t_max, 8),
        "valor_maximo": round(señal(t_max), 8),
        "derivada_en_el_maximo": round(_central(señal, t_max), 8),
        "area_acumulada_0_a_6": round(area, 8),
        "energia_∫f²": round(energia, 8),
        "valor_medio": round(area / 6.0, 8),
        "las_dos_operaciones": "derivar localiza; integrar acumula",
    }


DEMOS = {
    "limit_intuition": limit_intuition,
    "algebraic_limits": algebraic_limits,
    "continuity": continuity,
    "derivative_as_rate": derivative_as_rate,
    "derivative_rules": derivative_rules,
    "product_quotient_rule": product_quotient_rule,
    "chain_rule": chain_rule,
    "exp_log_derivatives": exp_log_derivatives,
    "trig_derivatives": trig_derivatives,
    "implicit_differentiation": implicit_differentiation,
    "taylor_approximation": taylor_approximation,
    "extrema": extrema,
    "integral_as_accumulation": integral_as_accumulation,
    "definite_integral": definite_integral,
    "antiderivatives": antiderivatives,
    "fundamental_theorem": fundamental_theorem,
    "substitution": substitution,
    "integration_by_parts": integration_by_parts,
    "numerical_integration_intro": numerical_integration_intro,
    "capstone_optimize_and_accumulate": capstone_optimize_and_accumulate,
}

CLASS_DEMOS = {
    "141": "limit_intuition",
    "142": "algebraic_limits",
    "143": "continuity",
    "144": "derivative_as_rate",
    "145": "derivative_rules",
    "146": "product_quotient_rule",
    "147": "chain_rule",
    "148": "exp_log_derivatives",
    "149": "trig_derivatives",
    "150": "implicit_differentiation",
    "151": "taylor_approximation",
    "152": "extrema",
    "153": "integral_as_accumulation",
    "154": "definite_integral",
    "155": "antiderivatives",
    "156": "fundamental_theorem",
    "157": "substitution",
    "158": "integration_by_parts",
    "159": "numerical_integration_intro",
    "160": "capstone_optimize_and_accumulate",
}
