"""Motor 09 — Probabilidad y procesos aleatorios.

Todo lo aleatorio usa una semilla fija: los resultados son reproducibles y
comparables entre ejecuciones y plataformas.
"""

from __future__ import annotations

import math
import random
import statistics
from itertools import product

PART = "09"
TITLE = "Probabilidad y procesos aleatorios"

SEED = 20260813


def _rng(offset: int = 0) -> random.Random:
    return random.Random(SEED + offset)


def sample_space() -> dict:
    """Espacio muestral, eventos y su probabilidad en un modelo equiprobable."""
    omega = list(product(range(1, 7), repeat=2))
    suma_7 = [p for p in omega if sum(p) == 7]
    ambos_pares = [p for p in omega if p[0] % 2 == 0 and p[1] % 2 == 0]
    return {
        "experimento": "lanzar dos dados equilibrados",
        "|Ω|": len(omega),
        "evento_suma_7": len(suma_7),
        "P(suma=7)": len(suma_7) / len(omega),
        "evento_ambos_pares": len(ambos_pares),
        "P(ambos_pares)": len(ambos_pares) / len(omega),
        "P(complemento_suma_7)": 1 - len(suma_7) / len(omega),
        "suma_mas_probable": 7,
    }


def axioms() -> dict:
    """Los tres axiomas de Kolmogorov verificados sobre un modelo."""
    p = {"a": 0.5, "b": 0.3, "c": 0.2}
    return {
        "distribucion": p,
        "axioma_1_no_negatividad": all(v >= 0 for v in p.values()),
        "axioma_2_P(Ω)=1": math.isclose(sum(p.values()), 1.0),
        "axioma_3_aditividad": math.isclose(p["a"] + p["b"], 0.8),
        "P(∅)": 0.0,
        "P(Aᶜ)": 1 - p["a"],
        "monotonia": p["a"] >= p["a"] * 0.5,
        "P_nunca_supera_1": all(v <= 1 for v in p.values()),
    }


def sum_product_rules() -> dict:
    """Regla de la suma con y sin exclusión mutua."""
    omega = list(product(range(1, 7), repeat=2))
    a = {p for p in omega if p[0] == 1}
    b = {p for p in omega if sum(p) == 7}
    return {
        "P(A)_primer_dado_1": len(a) / 36,
        "P(B)_suma_7": len(b) / 36,
        "P(A∩B)": len(a & b) / 36,
        "P(A∪B)_inclusion_exclusion": (len(a) + len(b) - len(a & b)) / 36,
        "P(A∪B)_directo": len(a | b) / 36,
        "son_mutuamente_excluyentes": len(a & b) == 0,
        "P(A)·P(B)": (len(a) / 36) * (len(b) / 36),
        "son_independientes": math.isclose(len(a & b) / 36, (len(a) / 36) * (len(b) / 36)),
    }


def conditional() -> dict:
    """P(A|B) cambia el espacio muestral, no la realidad."""
    omega = list(product(range(1, 7), repeat=2))
    b = [p for p in omega if p[0] == 6]
    a_dado_b = [p for p in b if sum(p) > 9]
    a = [p for p in omega if sum(p) > 9]
    return {
        "P(suma>9)": len(a) / 36,
        "P(primer_dado=6)": len(b) / 36,
        "P(suma>9 | primer=6)": len(a_dado_b) / len(b),
        "formula_P(A∩B)/P(B)": (len(a_dado_b) / 36) / (len(b) / 36),
        "la_informacion_cambia_la_probabilidad": len(a_dado_b) / len(b) != len(a) / 36,
        "espacio_reducido": len(b),
    }


def independence() -> dict:
    """Independencia se comprueba, no se supone."""
    omega = list(product(range(1, 7), repeat=2))
    a = {p for p in omega if p[0] % 2 == 0}
    b = {p for p in omega if p[1] % 2 == 0}
    c = {p for p in omega if sum(p) % 2 == 0}
    return {
        "P(A)": len(a) / 36,
        "P(B)": len(b) / 36,
        "P(A∩B)": len(a & b) / 36,
        "A_y_B_independientes": math.isclose(len(a & b) / 36, (len(a) / 36) * (len(b) / 36)),
        "P(C)": len(c) / 36,
        "P(A∩C)": len(a & c) / 36,
        "A_y_C_independientes": math.isclose(len(a & c) / 36, (len(a) / 36) * (len(c) / 36)),
        "P(A∩B∩C)": len(a & b & c) / 36,
        "independencia_por_pares_no_implica_conjunta": True,
    }


def bayes() -> dict:
    """Test médico: por qué un positivo no significa enfermedad."""
    prevalencia = 0.001
    sensibilidad = 0.99
    especificidad = 0.99
    p_pos = sensibilidad * prevalencia + (1 - especificidad) * (1 - prevalencia)
    posterior = sensibilidad * prevalencia / p_pos
    return {
        "prevalencia_previa": prevalencia,
        "sensibilidad_P(+|enfermo)": sensibilidad,
        "especificidad_P(-|sano)": especificidad,
        "P(+)": round(p_pos, 8),
        "P(enfermo|+)": round(posterior, 8),
        "falsos_positivos_por_verdadero": round((1 - posterior) / posterior, 4),
        "error_comun": "confundir P(+|enfermo) con P(enfermo|+)",
        "con_prevalencia_10%": round(sensibilidad * 0.1 / (sensibilidad * 0.1 + 0.01 * 0.9), 6),
    }


def discrete_rv() -> dict:
    """Variable aleatoria discreta: pmf, cdf y coherencia."""
    pmf = {0: 0.1, 1: 0.2, 2: 0.4, 3: 0.2, 4: 0.1}
    cdf, acc = {}, 0.0
    for k in sorted(pmf):
        acc += pmf[k]
        cdf[k] = round(acc, 10)
    esperanza = sum(k * p for k, p in pmf.items())
    return {
        "pmf": pmf,
        "suma_pmf": round(sum(pmf.values()), 10),
        "cdf": cdf,
        "P(X<=2)": cdf[2],
        "P(X>2)": round(1 - cdf[2], 10),
        "esperanza": round(esperanza, 10),
        "moda": max(pmf, key=pmf.get),
        "mediana": min(k for k in cdf if cdf[k] >= 0.5),
    }


def continuous_rv() -> dict:
    """Variable continua: la densidad no es una probabilidad."""
    lam = 2.0

    def pdf(x):
        return lam * math.exp(-lam * x)

    def cdf(x):
        return 1 - math.exp(-lam * x)

    return {
        "distribucion": "Exponencial(λ=2)",
        "pdf(0)": pdf(0.0),
        "pdf_puede_superar_1": pdf(0.0) > 1,
        "P(X=0.5)": 0.0,
        "P(X<=0.5)": round(cdf(0.5), 8),
        "P(0.5<X<=1)": round(cdf(1.0) - cdf(0.5), 8),
        "integral_total": round(cdf(1e6), 10),
        "media_1/λ": 1 / lam,
    }


def expectation() -> dict:
    """Linealidad de la esperanza, incluso sin independencia."""
    rng = _rng(1)
    n = 60_000
    x = [rng.random() for _ in range(n)]
    y = [xi**2 for xi in x]
    return {
        "E[X]_teorica_uniforme": 0.5,
        "E[X]_muestral": round(sum(x) / n, 6),
        "E[X²]_teorica": round(1 / 3, 6),
        "E[X²]_muestral": round(sum(y) / n, 6),
        "E[X]²": round((sum(x) / n) ** 2, 6),
        "E[X²]≠E[X]²": True,
        "E[2X+3Y]": round(sum(2 * a + 3 * b for a, b in zip(x, y)) / n, 6),
        "2E[X]+3E[Y]": round(2 * sum(x) / n + 3 * sum(y) / n, 6),
        "linealidad_sin_independencia": True,
    }


def variance() -> dict:
    """Varianza, desviación estándar y el estimador insesgado."""
    datos = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    n = len(datos)
    media = sum(datos) / n
    poblacional = sum((x - media) ** 2 for x in datos) / n
    muestral = sum((x - media) ** 2 for x in datos) / (n - 1)
    return {
        "datos": datos,
        "media": media,
        "varianza_poblacional_/n": poblacional,
        "varianza_muestral_/(n-1)": round(muestral, 8),
        "desviacion_estandar": round(math.sqrt(poblacional), 8),
        "statistics.pstdev": round(statistics.pstdev(datos), 8),
        "statistics.stdev": round(statistics.stdev(datos), 8),
        "correccion_de_Bessel": "dividir por n-1 corrige el sesgo del estimador",
        "Var(aX)=a²Var(X)": round(sum((2 * x - 2 * media) ** 2 for x in datos) / n, 8),
    }


def covariance_correlation() -> dict:
    """Covarianza depende de la escala; la correlación no."""
    x = [1.0, 2.0, 3.0, 4.0, 5.0]
    y = [2.0, 4.1, 5.9, 8.2, 9.8]
    z = [v * 1000 for v in y]

    def cov(a, b):
        ma, mb = sum(a) / len(a), sum(b) / len(b)
        return sum((p - ma) * (q - mb) for p, q in zip(a, b)) / (len(a) - 1)

    def corr(a, b):
        return cov(a, b) / (statistics.stdev(a) * statistics.stdev(b))

    return {
        "cov(x,y)": round(cov(x, y), 6),
        "cov(x,z)_escala_x1000": round(cov(x, z), 3),
        "corr(x,y)": round(corr(x, y), 8),
        "corr(x,z)": round(corr(x, z), 8),
        "la_correlacion_es_invariante_a_escala": math.isclose(corr(x, y), corr(x, z), rel_tol=1e-9),
        "rango_de_la_correlacion": "[-1, 1]",
        "correlacion_0_no_implica_independencia": "y = x² con x simétrica",
    }


def bernoulli_binomial() -> dict:
    """De un ensayo a n ensayos: Bernoulli y binomial."""
    p, n = 0.3, 10

    def pmf(k):
        return math.comb(n, k) * p**k * (1 - p) ** (n - k)

    rng = _rng(2)
    simulaciones = [sum(1 for _ in range(n) if rng.random() < p) for _ in range(20_000)]
    return {
        "p": p,
        "n": n,
        "media_teorica_np": n * p,
        "varianza_teorica_np(1-p)": n * p * (1 - p),
        "media_simulada": round(sum(simulaciones) / len(simulaciones), 6),
        "pmf_k=3": round(pmf(3), 8),
        "frecuencia_simulada_k=3": round(simulaciones.count(3) / len(simulaciones), 6),
        "suma_pmf": round(sum(pmf(k) for k in range(n + 1)), 10),
        "P(X<=3)": round(sum(pmf(k) for k in range(4)), 8),
    }


def poisson_exponential() -> dict:
    """Poisson cuenta eventos; la exponencial mide el tiempo entre ellos."""
    lam = 3.0

    def poisson_pmf(k):
        return math.exp(-lam) * lam**k / math.factorial(k)

    rng = _rng(3)
    esperas = [rng.expovariate(lam) for _ in range(40_000)]
    return {
        "λ_eventos_por_hora": lam,
        "P(N=0)": round(poisson_pmf(0), 8),
        "P(N=3)": round(poisson_pmf(3), 8),
        "media_poisson": lam,
        "varianza_poisson": lam,
        "media_de_la_espera_1/λ": round(1 / lam, 8),
        "media_de_espera_simulada": round(sum(esperas) / len(esperas), 6),
        "sin_memoria": "P(T>s+t | T>s) = P(T>t)",
    }


def normal_distribution() -> dict:
    """Normal: regla 68-95-99.7 y estandarización."""
    mu, sigma = 100.0, 15.0

    def cdf(x):
        return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

    return {
        "μ": mu,
        "σ": sigma,
        "P(μ-σ < X < μ+σ)": round(cdf(mu + sigma) - cdf(mu - sigma), 6),
        "P(μ-2σ < X < μ+2σ)": round(cdf(mu + 2 * sigma) - cdf(mu - 2 * sigma), 6),
        "P(μ-3σ < X < μ+3σ)": round(cdf(mu + 3 * sigma) - cdf(mu - 3 * sigma), 6),
        "z_de_130": (130 - mu) / sigma,
        "P(X>130)": round(1 - cdf(130), 6),
        "percentil_95_aprox": round(mu + 1.6449 * sigma, 4),
        "simetrica": True,
    }


def joint_marginal() -> dict:
    """Distribución conjunta, marginales y condicional."""
    conjunta = {(0, 0): 0.2, (0, 1): 0.3, (1, 0): 0.1, (1, 1): 0.4}
    marg_x = {x: sum(p for (a, _), p in conjunta.items() if a == x) for x in (0, 1)}
    marg_y = {y: sum(p for (_, b), p in conjunta.items() if b == y) for y in (0, 1)}
    return {
        "conjunta": {str(k): v for k, v in conjunta.items()},
        "suma": round(sum(conjunta.values()), 10),
        "marginal_X": marg_x,
        "marginal_Y": marg_y,
        "P(Y=1|X=1)": round(conjunta[(1, 1)] / marg_x[1], 8),
        "producto_de_marginales_(1,1)": round(marg_x[1] * marg_y[1], 8),
        "independientes": math.isclose(conjunta[(1, 1)], marg_x[1] * marg_y[1]),
    }


def law_large_numbers() -> dict:
    """La media muestral converge, pero lentamente."""
    rng = _rng(4)
    informe = []
    acumulado, contador = 0.0, 0
    for n in (10, 100, 1_000, 10_000, 50_000):
        while contador < n:
            acumulado += rng.random()
            contador += 1
        informe.append({"n": n, "media": round(acumulado / contador, 6),
                        "error": round(abs(acumulado / contador - 0.5), 6)})
    return {
        "distribucion": "Uniforme(0,1), media 0.5",
        "informe": informe,
        "velocidad": "el error cae como 1/√n",
        "cuadruplicar_n_reduce_el_error_a_la_mitad": True,
        "no_garantiza_ninguna_muestra_concreta": True,
    }


def central_limit() -> dict:
    """El TCL en acción sobre una distribución claramente no normal."""
    rng = _rng(5)
    tam = 30
    medias = []
    for _ in range(8_000):
        muestra = [rng.expovariate(1.0) for _ in range(tam)]
        medias.append(sum(muestra) / tam)
    media = sum(medias) / len(medias)
    var = sum((m - media) ** 2 for m in medias) / (len(medias) - 1)
    return {
        "poblacion": "Exponencial(1): asimétrica, media 1, varianza 1",
        "tamaño_de_muestra": tam,
        "replicas": len(medias),
        "media_de_las_medias": round(media, 6),
        "media_teorica": 1.0,
        "varianza_de_las_medias": round(var, 6),
        "varianza_teorica_σ²/n": round(1.0 / tam, 6),
        "error_estandar": round(math.sqrt(var), 6),
        "la_distribucion_de_medias_es_casi_normal": True,
    }


def monte_carlo() -> dict:
    """Estimar π por Monte Carlo con su error e intervalo."""
    rng = _rng(6)
    informe = []
    dentro, total = 0, 0
    for n in (1_000, 10_000, 100_000, 200_000):
        while total < n:
            x, y = rng.random(), rng.random()
            dentro += 1 if x * x + y * y <= 1 else 0
            total += 1
        pi = 4 * dentro / total
        p = dentro / total
        err_std = 4 * math.sqrt(p * (1 - p) / total)
        informe.append({"n": n, "pi_estimado": round(pi, 6),
                        "error": round(abs(pi - math.pi), 6),
                        "error_estandar": round(err_std, 6)})
    return {
        "metodo": "puntos uniformes en el cuadrado unitario",
        "semilla": SEED + 6,
        "informe": informe,
        "pi_real": math.pi,
        "convergencia": "O(1/√n) independientemente de la dimensión",
        "ventaja_en_alta_dimension": True,
    }


def markov_chains() -> dict:
    """Cadena de Markov: matriz de transición y distribución estacionaria."""
    p = [[0.9, 0.1], [0.5, 0.5]]
    dist = [1.0, 0.0]
    trayectoria = []
    for paso in range(60):
        dist = [sum(dist[i] * p[i][j] for i in range(2)) for j in range(2)]
        if paso in (0, 1, 4, 9, 59):
            trayectoria.append({"paso": paso + 1, "distribucion": [round(v, 8) for v in dist]})
    # estacionaria: π = πP con π₀+π₁=1  ->  0.1π₀ = 0.5π₁
    pi = [0.5 / 0.6, 0.1 / 0.6]
    return {
        "matriz_de_transicion": p,
        "filas_suman_1": all(math.isclose(sum(row), 1.0) for row in p),
        "estado_inicial": [1.0, 0.0],
        "trayectoria": trayectoria,
        "distribucion_final": [round(v, 8) for v in dist],
        "estacionaria_teorica": [round(v, 8) for v in pi],
        "converge": all(abs(a - b) < 1e-6 for a, b in zip(dist, pi)),
        "olvida_el_estado_inicial": True,
    }


def capstone_probabilistic_simulator() -> dict:
    """Capstone: simulador probabilístico con actualización bayesiana."""
    rng = _rng(7)
    p_real = 0.35
    observaciones = [1 if rng.random() < p_real else 0 for _ in range(200)]

    # Prior Beta(2,2), posterior Beta(2+éxitos, 2+fallos)
    a0 = b0 = 2.0
    informe = []
    for n in (0, 10, 50, 200):
        exitos = sum(observaciones[:n])
        a, b = a0 + exitos, b0 + (n - exitos)
        media = a / (a + b)
        var = a * b / ((a + b) ** 2 * (a + b + 1))
        informe.append({
            "observaciones": n,
            "exitos": exitos,
            "media_posterior": round(media, 6),
            "desviacion_posterior": round(math.sqrt(var), 6),
            "IC_95%_aprox": (round(media - 1.96 * math.sqrt(var), 6),
                             round(media + 1.96 * math.sqrt(var), 6)),
        })
    frecuentista = sum(observaciones) / len(observaciones)
    return {
        "parametro_real": p_real,
        "prior": "Beta(2,2)",
        "actualizacion": informe,
        "estimacion_frecuentista": round(frecuentista, 6),
        "estimacion_bayesiana_final": informe[-1]["media_posterior"],
        "el_prior_se_diluye_con_datos": True,
        "semilla": SEED + 7,
        "reproducible": True,
    }


DEMOS = {
    "sample_space": sample_space,
    "axioms": axioms,
    "sum_product_rules": sum_product_rules,
    "conditional": conditional,
    "independence": independence,
    "bayes": bayes,
    "discrete_rv": discrete_rv,
    "continuous_rv": continuous_rv,
    "expectation": expectation,
    "variance": variance,
    "covariance_correlation": covariance_correlation,
    "bernoulli_binomial": bernoulli_binomial,
    "poisson_exponential": poisson_exponential,
    "normal_distribution": normal_distribution,
    "joint_marginal": joint_marginal,
    "law_large_numbers": law_large_numbers,
    "central_limit": central_limit,
    "monte_carlo": monte_carlo,
    "markov_chains": markov_chains,
    "capstone_probabilistic_simulator": capstone_probabilistic_simulator,
}

CLASS_DEMOS = {
    "181": "sample_space",
    "182": "axioms",
    "183": "sum_product_rules",
    "184": "conditional",
    "185": "independence",
    "186": "bayes",
    "187": "discrete_rv",
    "188": "continuous_rv",
    "189": "expectation",
    "190": "variance",
    "191": "covariance_correlation",
    "192": "bernoulli_binomial",
    "193": "poisson_exponential",
    "194": "normal_distribution",
    "195": "joint_marginal",
    "196": "law_large_numbers",
    "197": "central_limit",
    "198": "monte_carlo",
    "199": "markov_chains",
    "200": "capstone_probabilistic_simulator",
}
