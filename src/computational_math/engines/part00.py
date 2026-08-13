"""Motor 00 — Pensamiento matemático desde cero.

Aritmética exacta frente a aritmética aproximada, proporcionalidad, unidades,
redondeo y comprobación por contraejemplo.
"""

from __future__ import annotations

import math
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal
from fractions import Fraction

PART = "00"
TITLE = "Pensamiento matemático desde cero"


def counting() -> dict:
    """Conteo, suma de Gauss y verificación cerrada frente a iterativa."""
    n = 100
    iterative = sum(range(1, n + 1))
    closed_form = n * (n + 1) // 2
    return {
        "n": n,
        "suma_iterativa": iterative,
        "suma_formula_cerrada": closed_form,
        "coinciden": iterative == closed_form,
        "operaciones_iterativas": n,
        "operaciones_formula": 3,
    }


def integers_number_line() -> dict:
    """Signo, valor absoluto y distancia en la recta numérica."""
    a, b = -7, 4
    return {
        "a": a,
        "b": b,
        "distancia_|a-b|": abs(a - b),
        "distancia_|b-a|": abs(b - a),
        "simetrica": abs(a - b) == abs(b - a),
        "producto_de_signos": (1 if a > 0 else -1) * (1 if b > 0 else -1),
        "opuesto_de_a": -a,
    }


def rational_arithmetic() -> dict:
    """Un tercio exacto frente a un tercio en punto flotante."""
    exact = Fraction(1, 3) + Fraction(1, 6)
    approx = 1 / 3 + 1 / 6
    return {
        "1/3 + 1/6 exacto": str(exact),
        "1/3 + 1/6 float": approx,
        "es_igual_a_1/2_exacto": exact == Fraction(1, 2),
        "es_igual_a_0.5_float": approx == 0.5,
        "error_absoluto": abs(float(exact) - approx),
        "denominador_reducido": exact.denominator,
    }


def decimal_conversion() -> dict:
    """Fracciones con desarrollo decimal finito y periódico."""
    finite = Fraction(3, 8)
    periodic = Fraction(1, 7)
    return {
        "3/8": float(finite),
        "3/8_es_finito": True,
        "1/7_primeros_12_digitos": str(Decimal(1) / Decimal(7))[:14],
        "1/7_periodo": "142857",
        "1/7_reconstruido": str(Fraction(142857, 999999)),
        "coincide_con_1/7": Fraction(142857, 999999) == periodic,
    }


def percentage() -> dict:
    """Aumento y descuento sucesivos: el orden no cambia, la reversión sí."""
    precio = Decimal("1000")
    con_aumento = precio * Decimal("1.20")
    con_descuento = con_aumento * Decimal("0.80")
    return {
        "precio_inicial": float(precio),
        "tras_+20%": float(con_aumento),
        "tras_-20%": float(con_descuento),
        "vuelve_al_inicial": con_descuento == precio,
        "variacion_neta_%": float((con_descuento / precio - 1) * 100),
        "descuento_que_revierte_+20%": round(float((1 - 1 / Decimal("1.20")) * 100), 4),
    }


def ratios() -> dict:
    """Razón, tasa y proporción con unidades explícitas."""
    distancia_km, tiempo_h = 240.0, 3.0
    return {
        "distancia_km": distancia_km,
        "tiempo_h": tiempo_h,
        "razon_km_por_h": distancia_km / tiempo_h,
        "unidad": "km/h",
        "tiempo_para_400km_h": 400.0 / (distancia_km / tiempo_h),
        "razon_es_adimensional": False,
    }


def rule_of_three() -> dict:
    """Proporcionalidad directa e inversa comparadas sobre el mismo dato."""
    a, b, c = 4.0, 10.0, 6.0
    directa = b * c / a
    inversa = a * b / c
    return {
        "si_4_cuesta_10": "¿cuánto cuestan 6?",
        "proporcion_directa": directa,
        "proporcion_inversa": inversa,
        "producto_cruzado_directa": a * directa == b * c,
        "producto_constante_inversa": a * b == c * inversa,
    }


def exponent_laws() -> dict:
    """Leyes de exponentes verificadas numéricamente."""
    a, m, n = 2.0, 5, 3
    return {
        "a^m * a^n": a**m * a**n,
        "a^(m+n)": a ** (m + n),
        "ley_producto_ok": math.isclose(a**m * a**n, a ** (m + n)),
        "(a^m)^n": (a**m) ** n,
        "a^(m*n)": a ** (m * n),
        "ley_potencia_ok": math.isclose((a**m) ** n, a ** (m * n)),
        "a^0": a**0,
        "a^-n": a ** (-n),
    }


def radicals() -> dict:
    """Raíces como exponentes fraccionarios y su dominio real."""
    x = 2.0
    return {
        "sqrt(2)": math.sqrt(x),
        "2**0.5": x**0.5,
        "coinciden": math.isclose(math.sqrt(x), x**0.5),
        "cuadrado_de_la_raiz": math.sqrt(x) ** 2,
        "error_del_roundtrip": abs(math.sqrt(x) ** 2 - x),
        "raiz_cubica_de_-8": -((8.0) ** (1 / 3)),
        "raiz_par_de_negativo_en_R": None,
    }


def operator_precedence() -> dict:
    """Precedencia y asociatividad: dos lecturas de la misma cadena."""
    return {
        "2+3*4": 2 + 3 * 4,
        "(2+3)*4": (2 + 3) * 4,
        "2**3**2 (asocia derecha)": 2**3**2,
        "(2**3)**2": (2**3) ** 2,
        "-3**2": -(3**2),
        "(-3)**2": (-3) ** 2,
    }


def scientific_notation() -> dict:
    """Mantisa, exponente y orden de magnitud."""
    valor = 0.000_000_123_45
    exponente = math.floor(math.log10(abs(valor)))
    mantisa = valor / 10**exponente
    return {
        "valor": valor,
        "mantisa": mantisa,
        "exponente": exponente,
        "notacion": f"{mantisa:.5f}e{exponente}",
        "reconstruido": mantisa * 10**exponente,
        "orden_de_magnitud": exponente,
    }


def dimensional_analysis() -> dict:
    """Conversión de unidades como multiplicación por factores unitarios."""
    velocidad_kmh = 90.0
    velocidad_ms = velocidad_kmh * 1000 / 3600
    return {
        "velocidad_km/h": velocidad_kmh,
        "factor_1": "1000 m / 1 km",
        "factor_2": "1 h / 3600 s",
        "velocidad_m/s": velocidad_ms,
        "vuelta_a_km/h": velocidad_ms * 3600 / 1000,
        "consistente": math.isclose(velocidad_ms * 3.6, velocidad_kmh),
    }


def rounding() -> dict:
    """Redondeo bancario frente a redondeo aritmético."""
    valores = ["0.5", "1.5", "2.5", "3.5"]
    half_even = [float(Decimal(v).quantize(Decimal("1"), rounding=ROUND_HALF_EVEN)) for v in valores]
    half_up = [float(Decimal(v).quantize(Decimal("1"), rounding=ROUND_HALF_UP)) for v in valores]
    return {
        "valores": valores,
        "ROUND_HALF_EVEN": half_even,
        "ROUND_HALF_UP": half_up,
        "python_round": [round(float(v)) for v in valores],
        "sesgo_half_even": sum(half_even) - sum(float(v) for v in valores),
        "sesgo_half_up": sum(half_up) - sum(float(v) for v in valores),
    }


def estimation() -> dict:
    """Estimación por orden de magnitud contra el cálculo exacto."""
    exacto = 4873 * 297
    estimado = 5000 * 300
    return {
        "operacion": "4873 * 297",
        "exacto": exacto,
        "estimado": estimado,
        "error_relativo_%": abs(estimado - exacto) / exacto * 100,
        "mismo_orden_de_magnitud": math.floor(math.log10(exacto)) == math.floor(math.log10(estimado)),
    }


def variables() -> dict:
    """Una incógnita convierte una pregunta en una ecuación resoluble."""
    # 3x + 7 = 25
    a, b, c = 3.0, 7.0, 25.0
    x = (c - b) / a
    return {
        "ecuacion": "3x + 7 = 25",
        "x": x,
        "verificacion": a * x + b,
        "residuo": a * x + b - c,
        "resuelta": math.isclose(a * x + b, c),
    }


def formula_evaluation() -> dict:
    """Una fórmula evaluada con dominio y unidades declaradas."""
    radio_m = 2.5
    area = math.pi * radio_m**2
    perimetro = 2 * math.pi * radio_m
    return {
        "radio_m": radio_m,
        "area_m2": area,
        "perimetro_m": perimetro,
        "dominio_valido": radio_m > 0,
        "razon_area_perimetro": area / perimetro,
        "razon_teorica_r/2": radio_m / 2,
    }


def sequences() -> dict:
    """Detectar la regla de una secuencia y extrapolarla con cuidado."""
    aritmetica = [3, 7, 11, 15, 19]
    geometrica = [2, 6, 18, 54, 162]
    fib = [1, 1]
    while len(fib) < 10:
        fib.append(fib[-1] + fib[-2])
    return {
        "aritmetica": aritmetica,
        "diferencia_comun": aritmetica[1] - aritmetica[0],
        "siguiente_aritmetica": aritmetica[-1] + (aritmetica[1] - aritmetica[0]),
        "geometrica": geometrica,
        "razon_comun": geometrica[1] // geometrica[0],
        "fibonacci_10": fib,
        "razon_fib_final": fib[-1] / fib[-2],
        "razon_aurea": (1 + 5**0.5) / 2,
    }


def word_problem() -> dict:
    """Traducir un enunciado a ecuaciones y resolverlo."""
    # Dos productos: x + y = 30 unidades, 1500x + 2500y = 61000
    total_unidades = 30.0
    total_dinero = 61_000.0
    precio_a, precio_b = 1_500.0, 2_500.0
    y = (total_dinero - precio_a * total_unidades) / (precio_b - precio_a)
    x = total_unidades - y
    return {
        "enunciado": "30 unidades entre dos productos suman 61000",
        "unidades_producto_a": x,
        "unidades_producto_b": y,
        "verificacion_unidades": x + y,
        "verificacion_dinero": precio_a * x + precio_b * y,
        "solucion_valida": x >= 0 and y >= 0,
    }


def counterexample() -> dict:
    """Una conjetura plausible destruida por un único contraejemplo."""
    conjetura = "n^2 + n + 41 es primo para todo n natural"

    def es_primo(m: int) -> bool:
        if m < 2:
            return False
        for d in range(2, int(m**0.5) + 1):
            if m % d == 0:
                return False
        return True

    primeros = [n for n in range(0, 41) if es_primo(n * n + n + 41)]
    contra = next(n for n in range(0, 100) if not es_primo(n * n + n + 41))
    return {
        "conjetura": conjetura,
        "casos_favorables_consecutivos": len(primeros),
        "primer_contraejemplo_n": contra,
        "valor_en_el_contraejemplo": contra * contra + contra + 41,
        "factor": 41,
        "leccion": "40 confirmaciones no demuestran; 1 contraejemplo refuta",
    }


def capstone_budget_model() -> dict:
    """Capstone: modelar un presupuesto con dinero exacto y proporciones."""
    ingreso = Decimal("1250000")
    reparto = {"vivienda": Decimal("0.35"), "alimentacion": Decimal("0.20"),
               "transporte": Decimal("0.10"), "ahorro": Decimal("0.20"),
               "otros": Decimal("0.15")}
    montos = {k: (ingreso * v).quantize(Decimal("1")) for k, v in reparto.items()}
    total = sum(montos.values())
    return {
        "ingreso": float(ingreso),
        "porcentajes_suman_1": sum(reparto.values()) == Decimal("1"),
        "montos": {k: float(v) for k, v in montos.items()},
        "total_asignado": float(total),
        "descuadre_por_redondeo": float(ingreso - total),
        "meses_para_ahorrar_5M": float(Decimal("5000000") / montos["ahorro"]),
    }


DEMOS = {
    "counting": counting,
    "integers_number_line": integers_number_line,
    "rational_arithmetic": rational_arithmetic,
    "decimal_conversion": decimal_conversion,
    "percentage": percentage,
    "ratios": ratios,
    "rule_of_three": rule_of_three,
    "exponent_laws": exponent_laws,
    "radicals": radicals,
    "operator_precedence": operator_precedence,
    "scientific_notation": scientific_notation,
    "dimensional_analysis": dimensional_analysis,
    "rounding": rounding,
    "estimation": estimation,
    "variables": variables,
    "formula_evaluation": formula_evaluation,
    "sequences": sequences,
    "word_problem": word_problem,
    "counterexample": counterexample,
    "capstone_budget_model": capstone_budget_model,
}

CLASS_DEMOS = {
    "001": "counting",
    "002": "integers_number_line",
    "003": "rational_arithmetic",
    "004": "decimal_conversion",
    "005": "percentage",
    "006": "ratios",
    "007": "rule_of_three",
    "008": "exponent_laws",
    "009": "radicals",
    "010": "operator_precedence",
    "011": "scientific_notation",
    "012": "dimensional_analysis",
    "013": "rounding",
    "014": "estimation",
    "015": "variables",
    "016": "formula_evaluation",
    "017": "sequences",
    "018": "word_problem",
    "019": "counterexample",
    "020": "capstone_budget_model",
}
