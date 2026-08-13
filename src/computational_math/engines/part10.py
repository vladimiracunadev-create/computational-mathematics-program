"""Motor 10 — Estadística e inferencia.

Estimación, intervalos, pruebas de hipótesis interpretadas correctamente,
verosimilitud, inferencia bayesiana, bootstrap y diseño experimental.
"""

from __future__ import annotations

import math
import random
import statistics

PART = "10"
TITLE = "Estadística e inferencia"

SEED = 20260813
_MUESTRA = [12.1, 11.4, 13.8, 12.9, 11.0, 14.2, 12.5, 13.1, 11.8, 12.7,
            13.4, 12.2, 11.6, 13.9, 12.8, 12.0, 13.2, 11.9, 12.6, 13.0]


def _rng(offset: int = 0) -> random.Random:
    return random.Random(SEED + offset)


def _normal_cdf(z: float) -> float:
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def descriptive_statistics() -> dict:
    """Centro, dispersión y forma: tres preguntas distintas."""
    datos = sorted(_MUESTRA)
    n = len(datos)
    media = statistics.fmean(datos)
    desv = statistics.stdev(datos)
    q1 = statistics.quantiles(datos, n=4)[0]
    q3 = statistics.quantiles(datos, n=4)[2]
    return {
        "n": n,
        "media": round(media, 6),
        "mediana": round(statistics.median(datos), 6),
        "desviacion_estandar": round(desv, 6),
        "rango": round(datos[-1] - datos[0], 6),
        "Q1": round(q1, 6),
        "Q3": round(q3, 6),
        "IQR": round(q3 - q1, 6),
        "coeficiente_de_variacion_%": round(100 * desv / media, 4),
        "asimetria_aprox": round(3 * (media - statistics.median(datos)) / desv, 6),
    }


def population_sample() -> dict:
    """Sesgo de selección: la muestra no representa a la población."""
    rng = _rng(1)
    poblacion = [rng.gauss(50, 10) for _ in range(100_000)]
    aleatoria = rng.sample(poblacion, 500)
    sesgada = [x for x in poblacion if x > 55][:500]
    return {
        "media_poblacional": round(statistics.fmean(poblacion), 4),
        "media_muestra_aleatoria": round(statistics.fmean(aleatoria), 4),
        "error_muestra_aleatoria": round(abs(statistics.fmean(aleatoria) - statistics.fmean(poblacion)), 4),
        "media_muestra_sesgada": round(statistics.fmean(sesgada), 4),
        "error_muestra_sesgada": round(abs(statistics.fmean(sesgada) - statistics.fmean(poblacion)), 4),
        "el_tamaño_no_corrige_el_sesgo": True,
        "leccion": "500 observaciones sesgadas son peores que 50 aleatorias",
    }


def sampling_distributions() -> dict:
    """La distribución de la media muestral y su error estándar."""
    rng = _rng(2)
    sigma = 10.0
    informe = []
    for n in (5, 30, 100):
        medias = [statistics.fmean([rng.gauss(50, sigma) for _ in range(n)]) for _ in range(2_000)]
        informe.append({
            "n": n,
            "media_de_medias": round(statistics.fmean(medias), 4),
            "desviacion_observada": round(statistics.stdev(medias), 4),
            "error_estandar_teorico": round(sigma / math.sqrt(n), 4),
        })
    return {
        "poblacion": "Normal(50, 10)",
        "informe": informe,
        "regla": "SE = σ/√n",
        "cuadruplicar_n_reduce_SE_a_la_mitad": True,
    }


def estimators() -> dict:
    """Sesgo, varianza y consistencia de dos estimadores de la varianza."""
    rng = _rng(3)
    sigma2 = 25.0
    n = 8
    sesgado, insesgado = [], []
    for _ in range(6_000):
        m = [rng.gauss(0, math.sqrt(sigma2)) for _ in range(n)]
        media = statistics.fmean(m)
        sesgado.append(sum((x - media) ** 2 for x in m) / n)
        insesgado.append(sum((x - media) ** 2 for x in m) / (n - 1))
    return {
        "varianza_real": sigma2,
        "tamaño_muestral": n,
        "E[estimador_/n]": round(statistics.fmean(sesgado), 4),
        "sesgo_/n": round(statistics.fmean(sesgado) - sigma2, 4),
        "E[estimador_/(n-1)]": round(statistics.fmean(insesgado), 4),
        "sesgo_/(n-1)": round(statistics.fmean(insesgado) - sigma2, 4),
        "factor_teorico_(n-1)/n": (n - 1) / n,
        "insesgado_no_significa_mejor": "el estimador /n tiene menor MSE en este caso",
    }


def confidence_intervals() -> dict:
    """Un IC 95 % describe el procedimiento, no una probabilidad del parámetro."""
    rng = _rng(4)
    mu, sigma, n = 50.0, 10.0, 30
    cubiertos = 0
    replicas = 3_000
    for _ in range(replicas):
        m = [rng.gauss(mu, sigma) for _ in range(n)]
        media = statistics.fmean(m)
        se = statistics.stdev(m) / math.sqrt(n)
        if media - 1.96 * se <= mu <= media + 1.96 * se:
            cubiertos += 1
    media = statistics.fmean(_MUESTRA)
    se = statistics.stdev(_MUESTRA) / math.sqrt(len(_MUESTRA))
    return {
        "cobertura_simulada_%": round(100 * cubiertos / replicas, 3),
        "cobertura_nominal_%": 95.0,
        "replicas": replicas,
        "muestra_de_ejemplo_media": round(media, 6),
        "IC_95%": (round(media - 1.96 * se, 6), round(media + 1.96 * se, 6)),
        "amplitud": round(2 * 1.96 * se, 6),
        "lectura_correcta": "el 95 % de los intervalos así construidos contienen μ",
        "lectura_incorrecta": "hay 95 % de probabilidad de que μ esté en ESTE intervalo",
    }


def hypothesis_testing() -> dict:
    """Estructura completa de una prueba de hipótesis."""
    mu0 = 12.0
    media = statistics.fmean(_MUESTRA)
    n = len(_MUESTRA)
    se = statistics.stdev(_MUESTRA) / math.sqrt(n)
    z = (media - mu0) / se
    p = 2 * (1 - _normal_cdf(abs(z)))
    return {
        "H0": "μ = 12.0",
        "H1": "μ ≠ 12.0",
        "alfa": 0.05,
        "media_muestral": round(media, 6),
        "error_estandar": round(se, 6),
        "estadistico_z": round(z, 6),
        "p_value": round(p, 6),
        "decision": "rechazar H0" if p < 0.05 else "no rechazar H0",
        "no_rechazar_no_es_aceptar": True,
    }


def p_value() -> dict:
    """Qué mide y qué no mide un p-value."""
    rng = _rng(5)
    # Bajo H0 verdadera, los p-values se distribuyen uniformemente.
    ps = []
    for _ in range(6_000):
        m = [rng.gauss(0, 1) for _ in range(30)]
        z = statistics.fmean(m) / (statistics.stdev(m) / math.sqrt(30))
        ps.append(2 * (1 - _normal_cdf(abs(z))))
    return {
        "definicion": "P(estadístico tan o más extremo | H0 cierta)",
        "no_es": "P(H0 | datos)",
        "bajo_H0_es_uniforme": True,
        "proporcion_p<0.05": round(sum(1 for p in ps if p < 0.05) / len(ps), 5),
        "proporcion_p<0.01": round(sum(1 for p in ps if p < 0.01) / len(ps), 5),
        "media_de_los_p": round(statistics.fmean(ps), 5),
        "riesgo_de_20_pruebas": round(1 - 0.95**20, 5),
        "correccion_de_Bonferroni_alfa": round(0.05 / 20, 6),
    }


def type_errors() -> dict:
    """Errores tipo I y II: el compromiso es inevitable."""
    rng = _rng(6)
    n, alfa = 30, 0.05
    efecto = 0.5
    tipo_i = tipo_ii = 0
    replicas = 3_000
    for _ in range(replicas):
        m0 = [rng.gauss(0, 1) for _ in range(n)]
        z0 = statistics.fmean(m0) / (statistics.stdev(m0) / math.sqrt(n))
        if 2 * (1 - _normal_cdf(abs(z0))) < alfa:
            tipo_i += 1
        m1 = [rng.gauss(efecto, 1) for _ in range(n)]
        z1 = statistics.fmean(m1) / (statistics.stdev(m1) / math.sqrt(n))
        if 2 * (1 - _normal_cdf(abs(z1))) >= alfa:
            tipo_ii += 1
    return {
        "alfa_nominal": alfa,
        "tasa_error_tipo_I_observada": round(tipo_i / replicas, 5),
        "efecto_real": efecto,
        "tasa_error_tipo_II_(beta)": round(tipo_ii / replicas, 5),
        "potencia_1-beta": round(1 - tipo_ii / replicas, 5),
        "bajar_alfa_sube_beta": True,
        "solucion": "aumentar n mejora ambos a la vez",
    }


def statistical_power() -> dict:
    """Potencia en función del tamaño muestral."""
    efecto, alfa = 0.5, 0.05
    z_alfa = 1.96
    informe = []
    for n in (10, 30, 64, 100, 200):
        z = efecto * math.sqrt(n)
        potencia = 1 - _normal_cdf(z_alfa - z) + _normal_cdf(-z_alfa - z)
        informe.append({"n": n, "potencia": round(potencia, 4)})
    n_para_80 = math.ceil(((1.96 + 0.8416) / efecto) ** 2)
    return {
        "tamaño_del_efecto_d": efecto,
        "alfa": alfa,
        "informe": informe,
        "n_para_potencia_80%": n_para_80,
        "regla_practica": "n ≈ 16/d² para 80 % de potencia",
        "estudio_sin_potencia": "un resultado no significativo no dice nada",
    }


def t_test() -> dict:
    """t-test de dos muestras independientes."""
    rng = _rng(7)
    a = [rng.gauss(100, 15) for _ in range(25)]
    b = [rng.gauss(108, 15) for _ in range(25)]
    ma, mb = statistics.fmean(a), statistics.fmean(b)
    va, vb = statistics.variance(a), statistics.variance(b)
    na, nb = len(a), len(b)
    sp = math.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    t = (mb - ma) / (sp * math.sqrt(1 / na + 1 / nb))
    gl = na + nb - 2
    return {
        "grupo_A_media": round(ma, 4),
        "grupo_B_media": round(mb, 4),
        "diferencia": round(mb - ma, 4),
        "desviacion_combinada": round(sp, 4),
        "estadistico_t": round(t, 4),
        "grados_de_libertad": gl,
        "valor_critico_aprox_2.01": 2.01,
        "significativo_al_5%": abs(t) > 2.01,
        "d_de_Cohen": round((mb - ma) / sp, 4),
    }


def chi_square() -> dict:
    """Chi-cuadrado de independencia sobre una tabla de contingencia."""
    tabla = [[30, 20], [15, 35]]
    filas = [sum(f) for f in tabla]
    cols = [sum(c) for c in zip(*tabla)]
    total = sum(filas)
    esperados = [[filas[i] * cols[j] / total for j in range(2)] for i in range(2)]
    chi2 = sum((tabla[i][j] - esperados[i][j]) ** 2 / esperados[i][j] for i in range(2) for j in range(2))
    return {
        "tabla_observada": tabla,
        "totales_fila": filas,
        "totales_columna": cols,
        "tabla_esperada": [[round(v, 4) for v in row] for row in esperados],
        "chi_cuadrado": round(chi2, 6),
        "grados_de_libertad": 1,
        "valor_critico_5%": 3.841,
        "rechaza_independencia": chi2 > 3.841,
        "requisito": "frecuencias esperadas >= 5 en cada celda",
    }


def anova() -> dict:
    """ANOVA de un factor: descomposición de la variabilidad."""
    rng = _rng(8)
    grupos = [[rng.gauss(m, 5) for _ in range(20)] for m in (50, 53, 58)]
    todos = [x for g in grupos for x in g]
    gran_media = statistics.fmean(todos)
    ss_entre = sum(len(g) * (statistics.fmean(g) - gran_media) ** 2 for g in grupos)
    ss_dentro = sum((x - statistics.fmean(g)) ** 2 for g in grupos for x in g)
    gl_entre, gl_dentro = len(grupos) - 1, len(todos) - len(grupos)
    f = (ss_entre / gl_entre) / (ss_dentro / gl_dentro)
    return {
        "grupos": len(grupos),
        "medias": [round(statistics.fmean(g), 4) for g in grupos],
        "gran_media": round(gran_media, 4),
        "SS_entre": round(ss_entre, 4),
        "SS_dentro": round(ss_dentro, 4),
        "SS_total": round(ss_entre + ss_dentro, 4),
        "estadistico_F": round(f, 4),
        "gl": (gl_entre, gl_dentro),
        "valor_critico_aprox_3.16": 3.16,
        "significativo": f > 3.16,
        "eta_cuadrado": round(ss_entre / (ss_entre + ss_dentro), 4),
    }


def correlation_causation() -> dict:
    """Una variable de confusión genera correlación sin causalidad."""
    rng = _rng(9)
    n = 2_000
    temperatura = [rng.gauss(20, 8) for _ in range(n)]
    helados = [3 * t + rng.gauss(0, 10) for t in temperatura]
    ahogamientos = [0.2 * t + rng.gauss(0, 2) for t in temperatura]

    def corr(a, b):
        ma, mb = statistics.fmean(a), statistics.fmean(b)
        num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
        den = math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))
        return num / den

    return {
        "corr(helados, ahogamientos)": round(corr(helados, ahogamientos), 4),
        "corr(temperatura, helados)": round(corr(temperatura, helados), 4),
        "corr(temperatura, ahogamientos)": round(corr(temperatura, ahogamientos), 4),
        "confusor": "temperatura",
        "hay_flecha_causal_helados→ahogamientos": False,
        "como_se_detecta": "controlar el confusor o aleatorizar la asignación",
    }


def linear_regression_stats() -> dict:
    """Regresión lineal con R², error estándar y significancia."""
    xs = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    ys = [2.3, 4.1, 6.2, 7.8, 10.4, 11.9, 14.3, 16.1]
    n = len(xs)
    mx, my = statistics.fmean(xs), statistics.fmean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    pred = [a + b * x for x in xs]
    ss_res = sum((y - p) ** 2 for y, p in zip(ys, pred))
    ss_tot = sum((y - my) ** 2 for y in ys)
    se_b = math.sqrt(ss_res / (n - 2) / sum((x - mx) ** 2 for x in xs))
    return {
        "n": n,
        "intercepto": round(a, 6),
        "pendiente": round(b, 6),
        "R²": round(1 - ss_res / ss_tot, 6),
        "SS_residual": round(ss_res, 6),
        "error_estandar_pendiente": round(se_b, 6),
        "t_de_la_pendiente": round(b / se_b, 4),
        "significativa": abs(b / se_b) > 2.447,
        "residuos": [round(y - p, 4) for y, p in zip(ys, pred)],
    }


def maximum_likelihood() -> dict:
    """MLE para la normal: la media muestral maximiza la verosimilitud."""
    datos = _MUESTRA

    def log_verosimilitud(mu, sigma):
        return sum(-0.5 * math.log(2 * math.pi * sigma**2) - (x - mu) ** 2 / (2 * sigma**2)
                   for x in datos)

    mu_mle = statistics.fmean(datos)
    sigma_mle = math.sqrt(sum((x - mu_mle) ** 2 for x in datos) / len(datos))
    barrido = {round(mu, 2): round(log_verosimilitud(mu, sigma_mle), 4)
               for mu in (mu_mle - 1, mu_mle - 0.5, mu_mle, mu_mle + 0.5, mu_mle + 1)}
    return {
        "n": len(datos),
        "mu_MLE": round(mu_mle, 6),
        "sigma_MLE": round(sigma_mle, 6),
        "log_verosimilitud_maxima": round(log_verosimilitud(mu_mle, sigma_mle), 6),
        "barrido_en_mu": barrido,
        "el_maximo_esta_en_la_media": max(barrido, key=barrido.get) == round(mu_mle, 2),
        "sigma_MLE_es_sesgado": "divide por n, no por n-1",
        "conexion_con_ML": "minimizar cross-entropy = maximizar log-verosimilitud",
    }


def map_estimation() -> dict:
    """MAP: verosimilitud más prior, y su límite con muchos datos."""
    a0, b0 = 8.0, 2.0   # prior Beta fuerte hacia 0.8
    rng = _rng(10)
    p_real = 0.4
    informe = []
    datos = [1 if rng.random() < p_real else 0 for _ in range(500)]
    for n in (5, 20, 100, 500):
        exitos = sum(datos[:n])
        mle = exitos / n
        a, b = a0 + exitos, b0 + (n - exitos)
        mapa = (a - 1) / (a + b - 2)
        informe.append({"n": n, "MLE": round(mle, 6), "MAP": round(mapa, 6),
                        "distancia_al_real": round(abs(mapa - p_real), 6)})
    return {
        "parametro_real": p_real,
        "prior": "Beta(8,2) — sesgado hacia 0.8",
        "informe": informe,
        "MAP_converge_al_MLE": abs(informe[-1]["MAP"] - informe[-1]["MLE"]) < 0.01,
        "el_prior_domina_con_pocos_datos": True,
        "MAP_con_prior_uniforme_es_MLE": True,
    }


def bayesian_inference() -> dict:
    """Actualización bayesiana conjugada Beta-Binomial."""
    rng = _rng(11)
    p_real = 0.62
    datos = [1 if rng.random() < p_real else 0 for _ in range(300)]
    a, b = 1.0, 1.0
    historial = []
    for n in (0, 10, 50, 150, 300):
        exitos = sum(datos[:n])
        an, bn = a + exitos, b + (n - exitos)
        media = an / (an + bn)
        var = an * bn / ((an + bn) ** 2 * (an + bn + 1))
        historial.append({
            "n": n,
            "posterior": f"Beta({an:.0f},{bn:.0f})",
            "media": round(media, 6),
            "sd": round(math.sqrt(var), 6),
        })
    return {
        "parametro_real": p_real,
        "prior": "Beta(1,1) = uniforme",
        "historial": historial,
        "la_incertidumbre_se_reduce": historial[-1]["sd"] < historial[1]["sd"],
        "conjugacion": "prior Beta + verosimilitud Binomial = posterior Beta",
        "credible_vs_confianza": "el intervalo creíble sí es una probabilidad del parámetro",
    }


def bootstrap() -> dict:
    """Bootstrap: estimar la variabilidad sin suponer la distribución."""
    rng = _rng(12)
    datos = _MUESTRA
    n = len(datos)
    medias, medianas = [], []
    for _ in range(10_000):
        remuestra = [datos[rng.randrange(n)] for _ in range(n)]
        medias.append(statistics.fmean(remuestra))
        medianas.append(statistics.median(remuestra))
    medias.sort()
    medianas.sort()
    return {
        "n": n,
        "replicas": len(medias),
        "media_observada": round(statistics.fmean(datos), 6),
        "SE_bootstrap_de_la_media": round(statistics.stdev(medias), 6),
        "SE_teorico": round(statistics.stdev(datos) / math.sqrt(n), 6),
        "IC_95%_percentil_media": (round(medias[250], 6), round(medias[9749], 6)),
        "SE_bootstrap_de_la_mediana": round(statistics.stdev(medianas), 6),
        "ventaja": "funciona para estadísticos sin fórmula cerrada, como la mediana",
    }


def ab_testing() -> dict:
    """A/B test de proporciones con tamaño muestral y significancia."""
    rng = _rng(13)
    p_a, p_b = 0.10, 0.12
    n = 4_000
    a = sum(1 for _ in range(n) if rng.random() < p_a)
    b = sum(1 for _ in range(n) if rng.random() < p_b)
    pa, pb = a / n, b / n
    p_pool = (a + b) / (2 * n)
    se = math.sqrt(p_pool * (1 - p_pool) * (2 / n))
    z = (pb - pa) / se
    p_value = 2 * (1 - _normal_cdf(abs(z)))
    n_requerido = math.ceil(2 * (1.96 + 0.8416) ** 2 * p_a * (1 - p_a) / (p_b - p_a) ** 2)
    return {
        "conversion_A": round(pa, 6),
        "conversion_B": round(pb, 6),
        "lift_relativo_%": round(100 * (pb - pa) / pa, 4),
        "n_por_grupo": n,
        "estadistico_z": round(z, 4),
        "p_value": round(p_value, 6),
        "significativo_al_5%": p_value < 0.05,
        "n_requerido_para_80%_de_potencia": n_requerido,
        "peligro": "detener el test al ver significancia infla el error tipo I",
    }


def capstone_reproducible_study() -> dict:
    """Capstone: estudio completo, reproducible y con límites declarados."""
    rng = _rng(14)
    control = [rng.gauss(72.0, 9.0) for _ in range(60)]
    tratamiento = [rng.gauss(76.5, 9.0) for _ in range(60)]

    mc, mt = statistics.fmean(control), statistics.fmean(tratamiento)
    vc, vt = statistics.variance(control), statistics.variance(tratamiento)
    n = len(control)
    sp = math.sqrt(((n - 1) * vc + (n - 1) * vt) / (2 * n - 2))
    t = (mt - mc) / (sp * math.sqrt(2 / n))
    d = (mt - mc) / sp
    se_dif = sp * math.sqrt(2 / n)

    diffs = []
    for _ in range(5_000):
        rc = [control[rng.randrange(n)] for _ in range(n)]
        rt = [tratamiento[rng.randrange(n)] for _ in range(n)]
        diffs.append(statistics.fmean(rt) - statistics.fmean(rc))
    diffs.sort()

    return {
        "semilla": SEED + 14,
        "diseño": "dos grupos independientes, n=60 cada uno",
        "media_control": round(mc, 4),
        "media_tratamiento": round(mt, 4),
        "diferencia": round(mt - mc, 4),
        "IC_95%_parametrico": (round(mt - mc - 1.98 * se_dif, 4), round(mt - mc + 1.98 * se_dif, 4)),
        "IC_95%_bootstrap": (round(diffs[125], 4), round(diffs[4874], 4)),
        "estadistico_t": round(t, 4),
        "d_de_Cohen": round(d, 4),
        "potencia_aproximada": round(1 - _normal_cdf(1.96 - abs(d) * math.sqrt(n / 2)), 4),
        "significativo": abs(t) > 1.98,
        "limites_declarados": [
            "datos simulados: no hay validez externa",
            "una sola comparación planificada, sin exploración posterior",
            "el efecto observado no implica mecanismo causal fuera de un diseño aleatorizado",
        ],
        "reproducible": True,
    }


DEMOS = {
    "descriptive_statistics": descriptive_statistics,
    "population_sample": population_sample,
    "sampling_distributions": sampling_distributions,
    "estimators": estimators,
    "confidence_intervals": confidence_intervals,
    "hypothesis_testing": hypothesis_testing,
    "p_value": p_value,
    "type_errors": type_errors,
    "statistical_power": statistical_power,
    "t_test": t_test,
    "chi_square": chi_square,
    "anova": anova,
    "correlation_causation": correlation_causation,
    "linear_regression_stats": linear_regression_stats,
    "maximum_likelihood": maximum_likelihood,
    "map_estimation": map_estimation,
    "bayesian_inference": bayesian_inference,
    "bootstrap": bootstrap,
    "ab_testing": ab_testing,
    "capstone_reproducible_study": capstone_reproducible_study,
}

CLASS_DEMOS = {
    "201": "descriptive_statistics",
    "202": "population_sample",
    "203": "sampling_distributions",
    "204": "estimators",
    "205": "confidence_intervals",
    "206": "hypothesis_testing",
    "207": "p_value",
    "208": "type_errors",
    "209": "statistical_power",
    "210": "t_test",
    "211": "chi_square",
    "212": "anova",
    "213": "correlation_causation",
    "214": "linear_regression_stats",
    "215": "maximum_likelihood",
    "216": "map_estimation",
    "217": "bayesian_inference",
    "218": "bootstrap",
    "219": "ab_testing",
    "220": "capstone_reproducible_study",
}
