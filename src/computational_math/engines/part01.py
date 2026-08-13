"""Motor 01 — Aritmética computacional y representación numérica.

Bits, complemento a dos, IEEE 754, error, condicionamiento y estabilidad.
"""

from __future__ import annotations

import math
import struct
import sys
from decimal import Decimal, getcontext
from fractions import Fraction

PART = "01"
TITLE = "Aritmética computacional y representación numérica"


def bits_and_bytes() -> dict:
    """Cuántos valores distintos codifica cada ancho de palabra."""
    return {
        "valores_por_bit": 2,
        "valores_en_1_byte": 2**8,
        "valores_en_16_bits": 2**16,
        "valores_en_32_bits": 2**32,
        "valores_en_64_bits": 2**64,
        "bits_para_1000_valores": math.ceil(math.log2(1000)),
        "bits_para_1_millon": math.ceil(math.log2(1_000_000)),
    }


def decimal_to_binary() -> dict:
    """Divisiones sucesivas frente a la conversión de la biblioteca."""
    n = 156
    restos, q = [], n
    while q > 0:
        restos.append(q % 2)
        q //= 2
    manual = "".join(str(b) for b in reversed(restos))
    return {
        "decimal": n,
        "restos_en_orden_de_calculo": restos,
        "binario_manual": manual,
        "binario_builtin": format(n, "b"),
        "coinciden": manual == format(n, "b"),
        "reconstruido": int(manual, 2),
    }


def bases() -> dict:
    """La misma cantidad en base 2, 8, 10 y 16."""
    n = 3_735_928_559
    return {
        "decimal": n,
        "binario": format(n, "b"),
        "octal": format(n, "o"),
        "hexadecimal": format(n, "x"),
        "digitos_binarios": n.bit_length(),
        "un_hex_equivale_a_bits": 4,
        "un_octal_equivale_a_bits": 3,
    }


def binary_arithmetic() -> dict:
    """Suma y desplazamiento en binario, con acarreo visible."""
    a, b = 0b1011, 0b0110
    return {
        "a": format(a, "04b"),
        "b": format(b, "04b"),
        "a+b": format(a + b, "b"),
        "a&b": format(a & b, "04b"),
        "a|b": format(a | b, "04b"),
        "a^b": format(a ^ b, "04b"),
        "a<<2 (multiplica por 4)": a << 2,
        "a>>1 (divide por 2)": a >> 1,
    }


def twos_complement() -> dict:
    """Representación de negativos en 8 bits."""
    width = 8

    def encode(value: int) -> str:
        return format(value & (2**width - 1), f"0{width}b")

    def decode(bits: str) -> int:
        raw = int(bits, 2)
        return raw - 2**width if raw >= 2 ** (width - 1) else raw

    return {
        "ancho_bits": width,
        "5": encode(5),
        "-5": encode(-5),
        "suma_5_y_-5": encode(5 + (-5)),
        "decodifica_11111011": decode("11111011"),
        "minimo_representable": -(2 ** (width - 1)),
        "maximo_representable": 2 ** (width - 1) - 1,
        "asimetria": "hay un negativo más que positivos",
    }


def overflow_wraparound() -> dict:
    """Wraparound en enteros de ancho fijo simulado sobre Python."""
    width = 8
    modulo = 2**width
    maximo = 2 ** (width - 1) - 1

    def wrap(value: int) -> int:
        value %= modulo
        return value - modulo if value >= modulo // 2 else value

    return {
        "maximo_int8": maximo,
        "maximo+1_con_wraparound": wrap(maximo + 1),
        "maximo+2_con_wraparound": wrap(maximo + 2),
        "python_int_es_ilimitado": maximo + 1,
        "sys_maxsize": sys.maxsize,
        "leccion": "Python no desborda, C/NumPy sí",
    }


def fixed_vs_floating() -> dict:
    """Punto fijo (centavos enteros) frente a punto flotante."""
    precio_float = 0.0
    for _ in range(10):
        precio_float += 0.1
    centavos = sum(10 for _ in range(10))
    return {
        "suma_float_de_0.1_x10": precio_float,
        "es_exactamente_1.0": precio_float == 1.0,
        "error": abs(precio_float - 1.0),
        "suma_en_centavos_enteros": centavos,
        "centavos_a_unidades": centavos / 100,
        "punto_fijo_exacto": centavos == 100,
    }


def ieee754_layout() -> dict:
    """Signo, exponente y mantisa de un float64."""
    value = -6.25
    bits = format(struct.unpack("<Q", struct.pack("<d", value))[0], "064b")
    sign, exponent, mantissa = bits[0], bits[1:12], bits[12:]
    return {
        "valor": value,
        "bits": bits,
        "signo": sign,
        "exponente_bruto": int(exponent, 2),
        "sesgo": 1023,
        "exponente_real": int(exponent, 2) - 1023,
        "mantisa_bits": mantissa,
        "reconstruido": (-1) ** int(sign) * (1 + int(mantissa, 2) / 2**52) * 2 ** (int(exponent, 2) - 1023),
    }


def why_point_one() -> dict:
    """0.1 + 0.2 != 0.3 explicado con la fracción binaria real."""
    return {
        "0.1+0.2": 0.1 + 0.2,
        "0.3": 0.3,
        "iguales": 0.1 + 0.2 == 0.3,
        "diferencia": (0.1 + 0.2) - 0.3,
        "0.1_como_fraccion_exacta": str(Fraction(0.1).limit_denominator(10**20)),
        "0.1_con_50_digitos": f"{Decimal(0.1):.50f}",
        "comparacion_correcta": math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-12),
    }


def absolute_relative_error() -> dict:
    """El error relativo es el que se propaga; el absoluto engaña con la escala."""
    casos = [(1.0, 1.01), (1_000_000.0, 1_000_010.0)]
    salida = {}
    for exacto, aprox in casos:
        salida[f"exacto={exacto}"] = {
            "aproximado": aprox,
            "error_absoluto": abs(aprox - exacto),
            "error_relativo": abs(aprox - exacto) / abs(exacto),
        }
    salida["conclusion"] = "error absoluto mayor no implica peor aproximación"
    return salida


def ulp_epsilon() -> dict:
    """Machine epsilon y la distancia al float siguiente."""
    x = 1.0
    return {
        "sys.float_info.epsilon": sys.float_info.epsilon,
        "2**-52": 2.0**-52,
        "1.0 + eps != 1.0": 1.0 + sys.float_info.epsilon != 1.0,
        "1.0 + eps/2 == 1.0": 1.0 + sys.float_info.epsilon / 2 == 1.0,
        "ulp_en_1.0": math.ulp(x),
        "ulp_en_1e6": math.ulp(1e6),
        "ulp_en_1e-6": math.ulp(1e-6),
        "siguiente_float_tras_1.0": math.nextafter(1.0, math.inf),
    }


def catastrophic_cancellation() -> dict:
    """Dos fórmulas algebraicamente iguales con precisión muy distinta."""
    x = 1e8
    ingenua = math.sqrt(x * x + 1) - x
    estable = 1.0 / (math.sqrt(x * x + 1) + x)
    return {
        "x": x,
        "formula_ingenua_sqrt(x^2+1)-x": ingenua,
        "formula_estable_1/(sqrt(x^2+1)+x)": estable,
        "diferencia": abs(ingenua - estable),
        "error_relativo_de_la_ingenua": abs(ingenua - estable) / estable if estable else float("inf"),
        "causa": "restar dos números casi iguales destruye dígitos significativos",
    }


def float_overflow_underflow() -> dict:
    """Límites del float64 y el paso por subnormales."""
    return {
        "max_float": sys.float_info.max,
        "max*2_da_inf": sys.float_info.max * 2,
        "min_normal": sys.float_info.min,
        "min_subnormal": 5e-324,
        "min_subnormal/2": 5e-324 / 2,
        "underflow_a_cero": 5e-324 / 2 == 0.0,
        "inf-inf_es_nan": math.isnan(float("inf") - float("inf")),
    }


def error_propagation() -> dict:
    """Cómo crece el error al sumar 10^6 veces un valor no representable."""
    n = 1_000_000
    acumulado = 0.0
    for _ in range(n):
        acumulado += 0.1
    exacto = n * Fraction(1, 10)
    return {
        "n_sumas": n,
        "suma_acumulada": acumulado,
        "valor_exacto": float(exacto),
        "error_absoluto": abs(acumulado - float(exacto)),
        "error_relativo": abs(acumulado - float(exacto)) / float(exacto),
        "suma_compensada_fsum": math.fsum([0.1] * 1000) - 100.0,
        "recomendacion": "usar math.fsum o acumuladores compensados",
    }


def conditioning() -> dict:
    """Número de condición de una función: sensibilidad del problema."""

    def cond(f, df, x):
        return abs(x * df(x) / f(x))

    resultados = {}
    for x in (0.5, 0.99, 1.0e-8):
        resultados[f"x={x}"] = {
            "f(x)=1-x": 1 - x,
            "condicion": cond(lambda t: 1 - t, lambda t: -1.0, x),
        }
    resultados["lectura"] = "condición alta = el problema amplifica cualquier error de entrada"
    return resultados


def stability() -> dict:
    """Misma raíz cuadrática por dos algoritmos: uno estable, otro no."""
    a, b, c = 1.0, 1e8, 1.0
    disc = math.sqrt(b * b - 4 * a * c)
    r1_ingenua = (-b + disc) / (2 * a)
    r1_estable = (2 * c) / (-b - disc)
    r2 = (-b - disc) / (2 * a)
    return {
        "coeficientes": (a, b, c),
        "raiz_pequena_ingenua": r1_ingenua,
        "raiz_pequena_estable": r1_estable,
        "raiz_grande": r2,
        "producto_raices_ingenua": r1_ingenua * r2,
        "producto_raices_estable": r1_estable * r2,
        "producto_teorico_c/a": c / a,
    }


def arbitrary_precision() -> dict:
    """Decimal con precisión declarada frente a float."""
    getcontext().prec = 50
    uno_tercio = Decimal(1) / Decimal(3)
    return {
        "precision_configurada": getcontext().prec,
        "1/3_decimal": str(uno_tercio),
        "1/3_float": 1 / 3,
        "suma_0.1x3_decimal": str(Decimal("0.1") * 3),
        "es_exactamente_0.3": Decimal("0.1") * 3 == Decimal("0.3"),
        "coste": "exactitud decimal a cambio de velocidad",
    }


def exact_rationals() -> dict:
    """Fraction mantiene exactitud donde float ya perdió información."""
    suma_exacta = sum((Fraction(1, k) for k in range(1, 11)), Fraction(0))
    suma_float = sum(1 / k for k in range(1, 11))
    return {
        "H_10_exacto": str(suma_exacta),
        "H_10_float": suma_float,
        "H_10_exacto_como_float": float(suma_exacta),
        "error": abs(float(suma_exacta) - suma_float),
        "denominador": suma_exacta.denominator,
        "float_desde_fraction": Fraction(0.1) == Fraction(1, 10),
    }


def reproducibility() -> dict:
    """El orden de la suma cambia el resultado en punto flotante."""
    valores = [1e16, 1.0, -1e16, 1.0]
    izquierda = 0.0
    for v in valores:
        izquierda += v
    derecha = 0.0
    for v in reversed(valores):
        derecha += v
    return {
        "valores": valores,
        "suma_de_izquierda_a_derecha": izquierda,
        "suma_de_derecha_a_izquierda": derecha,
        "coinciden": izquierda == derecha,
        "suma_compensada": math.fsum(valores),
        "suma_es_asociativa_en_R": True,
        "suma_es_asociativa_en_float64": False,
    }


def capstone_precision_auditor() -> dict:
    """Capstone: auditoría de precisión de una expresión numérica."""
    def auditar(nombre, f_ingenua, f_estable, x):
        ing, est = f_ingenua(x), f_estable(x)
        return {
            "expresion": nombre,
            "ingenua": ing,
            "estable": est,
            "digitos_perdidos": (
                0.0 if est == 0 else max(0.0, -math.log10(abs(ing - est) / abs(est) + 1e-300))
            ),
        }

    informe = [
        auditar("exp(x)-1", lambda t: math.exp(t) - 1, math.expm1, 1e-10),
        auditar("log(1+x)", lambda t: math.log(1 + t), math.log1p, 1e-12),
        auditar(
            "sqrt(x^2+1)-x",
            lambda t: math.sqrt(t * t + 1) - t,
            lambda t: 1.0 / (math.sqrt(t * t + 1) + t),
            1e7,
        ),
    ]
    return {
        "informe": informe,
        "expresiones_auditadas": len(informe),
        "regla": "toda diferencia de magnitudes cercanas necesita una forma alternativa",
    }


DEMOS = {
    "bits_and_bytes": bits_and_bytes,
    "decimal_to_binary": decimal_to_binary,
    "bases": bases,
    "binary_arithmetic": binary_arithmetic,
    "twos_complement": twos_complement,
    "overflow_wraparound": overflow_wraparound,
    "fixed_vs_floating": fixed_vs_floating,
    "ieee754_layout": ieee754_layout,
    "why_point_one": why_point_one,
    "absolute_relative_error": absolute_relative_error,
    "ulp_epsilon": ulp_epsilon,
    "catastrophic_cancellation": catastrophic_cancellation,
    "float_overflow_underflow": float_overflow_underflow,
    "error_propagation": error_propagation,
    "conditioning": conditioning,
    "stability": stability,
    "arbitrary_precision": arbitrary_precision,
    "exact_rationals": exact_rationals,
    "reproducibility": reproducibility,
    "capstone_precision_auditor": capstone_precision_auditor,
}

CLASS_DEMOS = {
    "021": "bits_and_bytes",
    "022": "decimal_to_binary",
    "023": "bases",
    "024": "binary_arithmetic",
    "025": "twos_complement",
    "026": "overflow_wraparound",
    "027": "fixed_vs_floating",
    "028": "ieee754_layout",
    "029": "why_point_one",
    "030": "absolute_relative_error",
    "031": "ulp_epsilon",
    "032": "catastrophic_cancellation",
    "033": "float_overflow_underflow",
    "034": "error_propagation",
    "035": "conditioning",
    "036": "stability",
    "037": "arbitrary_precision",
    "038": "exact_rationals",
    "039": "reproducibility",
    "040": "capstone_precision_auditor",
}
