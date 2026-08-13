"""Motor 17 — Frontera matemática para IA e investigación.

Procesos gaussianos, MCMC, inferencia variacional, transporte óptimo,
geometría diferencial e informacional, SDE, Neural ODE, score matching y
teoría estadística del aprendizaje.
"""

from __future__ import annotations

import math
import random

from . import _linalg as la

PART = "17"
TITLE = "Frontera matemática para IA e investigación"

SEED = 20260813
JITTER = 1e-8


def _rbf(a: float, b: float, escala: float = 1.0, amplitud: float = 1.0) -> float:
    return amplitud * math.exp(-((a - b) ** 2) / (2 * escala**2))


def gaussian_processes() -> dict:
    """GP: distribución sobre funciones, con media y varianza posterior."""
    X = [-2.0, -1.0, 0.0, 1.5, 3.0]
    y = [math.sin(x) for x in X]
    ruido = 1e-4

    K = [[_rbf(a, b) + (ruido + JITTER if a == b else 0.0) for b in X] for a in X]
    K_inv = la.inverse(K)
    alpha = la.matvec(K_inv, y)

    def predecir(x_star):
        k = [_rbf(x_star, xi) for xi in X]
        media = la.dot(k, alpha)
        var = _rbf(x_star, x_star) - la.dot(k, la.matvec(K_inv, k))
        return media, max(var, 0.0)

    puntos = [-1.0, 0.5, 2.0, 6.0]
    predicciones = {}
    for p in puntos:
        m, v = predecir(p)
        predicciones[f"x={p}"] = {
            "media": round(m, 6),
            "desviacion": round(math.sqrt(v), 6),
            "valor_real_sin(x)": round(math.sin(p), 6),
        }
    return {
        "observaciones": len(X),
        "kernel": "RBF con escala 1.0",
        "ruido": ruido,
        "predicciones": predicciones,
        "en_un_punto_observado_la_varianza_es_minima": predecir(0.0)[1] < predecir(6.0)[1],
        "lejos_de_los_datos_vuelve_al_prior": round(math.sqrt(predecir(20.0)[1]), 4),
        "coste": "O(n³) por la inversión de la matriz de covarianza",
        "por_que_jitter": "K puede ser numéricamente singular sin él",
        "referencia": "Rasmussen & Williams, 2006",
    }


def advanced_kernels() -> dict:
    """Familias de kernels y la condición de Mercer."""
    a, b = 1.0, 2.5

    def polinomico(x, y, grado=3, c=1.0):
        return (x * y + c) ** grado

    def matern32(x, y, escala=1.0):
        r = abs(x - y) / escala
        return (1 + math.sqrt(3) * r) * math.exp(-math.sqrt(3) * r)

    def periodico(x, y, p=2.0, escala=1.0):
        return math.exp(-2 * math.sin(math.pi * abs(x - y) / p) ** 2 / escala**2)

    puntos = [0.0, 0.5, 1.0, 1.5]
    gram = [[_rbf(x, y) for y in puntos] for x in puntos]
    valores, _ = la.symmetric_eigen(gram)
    return {
        "kernels": {
            "RBF": round(_rbf(a, b), 8),
            "polinomico_grado_3": round(polinomico(a, b), 8),
            "matern_3/2": round(matern32(a, b), 8),
            "periodico": round(periodico(a, b), 8),
        },
        "matriz_de_Gram_RBF": [[round(v, 6) for v in fila] for fila in gram],
        "autovalores_de_Gram": [round(v, 8) for v in valores],
        "es_semidefinida_positiva": all(v >= -1e-8 for v in valores),
        "condicion_de_Mercer": "toda matriz de Gram debe ser semidefinida positiva",
        "suma_de_kernels_es_kernel": True,
        "producto_de_kernels_es_kernel": True,
        "matern_es_menos_suave_que_RBF": "controla la diferenciabilidad de las muestras",
    }


def advanced_mcmc() -> dict:
    """Metropolis-Hastings con diagnóstico de aceptación y autocorrelación."""
    def log_objetivo(x):
        return -0.5 * (x - 2.0) ** 2 / 1.5**2

    resultados = {}
    for paso in (0.2, 2.0, 12.0):
        rng = random.Random(SEED)
        x = 0.0
        cadena, aceptados = [], 0
        for _ in range(8_000):
            propuesta = x + rng.gauss(0, paso)
            if math.log(rng.random() + 1e-300) < log_objetivo(propuesta) - log_objetivo(x):
                x = propuesta
                aceptados += 1
            cadena.append(x)
        quemado = cadena[2_000:]
        media = sum(quemado) / len(quemado)
        var = sum((v - media) ** 2 for v in quemado) / len(quemado)
        lag1 = sum((quemado[i] - media) * (quemado[i + 1] - media)
                   for i in range(len(quemado) - 1)) / (len(quemado) * var)
        resultados[f"paso={paso}"] = {
            "tasa_de_aceptacion": round(aceptados / 8_000, 4),
            "media_estimada": round(media, 4),
            "desviacion_estimada": round(math.sqrt(var), 4),
            "autocorrelacion_lag_1": round(lag1, 4),
            "tamaño_efectivo_aprox": int(len(quemado) * (1 - lag1) / (1 + lag1)),
        }
    return {
        "objetivo": "Normal(2.0, 1.5)",
        "iteraciones": 8_000,
        "burn_in": 2_000,
        "resultados": resultados,
        "aceptacion_optima_1D": "≈ 0.44 para random walk Metropolis",
        "paso_pequeño": "acepta casi todo pero explora muy despacio",
        "paso_grande": "rechaza casi todo y la cadena se queda pegada",
        "diagnosticos_obligatorios": ["traza", "R-hat con varias cadenas", "ESS"],
        "semilla": SEED,
    }


def hamiltonian_monte_carlo() -> dict:
    """HMC: usar el gradiente para proponer estados lejanos con alta aceptación."""
    def log_objetivo(x):
        return -0.5 * (x - 2.0) ** 2 / 1.5**2

    def grad_log(x):
        return -(x - 2.0) / 1.5**2

    rng = random.Random(SEED)
    x = 0.0
    eps, L = 0.35, 12
    cadena, aceptados = [], 0
    for _ in range(3_000):
        p0 = rng.gauss(0, 1)
        q, p = x, p0
        p += 0.5 * eps * grad_log(q)
        for _ in range(L):
            q += eps * p
            p += eps * grad_log(q)
        p -= 0.5 * eps * grad_log(q)
        p = -p
        h0 = -log_objetivo(x) + 0.5 * p0 * p0
        h1 = -log_objetivo(q) + 0.5 * p * p
        if math.log(rng.random() + 1e-300) < h0 - h1:
            x = q
            aceptados += 1
        cadena.append(x)
    quemado = cadena[500:]
    media = sum(quemado) / len(quemado)
    var = sum((v - media) ** 2 for v in quemado) / len(quemado)
    lag1 = sum((quemado[i] - media) * (quemado[i + 1] - media)
               for i in range(len(quemado) - 1)) / (len(quemado) * var)
    return {
        "objetivo": "Normal(2.0, 1.5)",
        "iteraciones": 3_000,
        "step_size_epsilon": eps,
        "pasos_de_leapfrog": L,
        "tasa_de_aceptacion": round(aceptados / 3_000, 4),
        "media_estimada": round(media, 4),
        "desviacion_estimada": round(math.sqrt(var), 4),
        "autocorrelacion_lag_1": round(lag1, 4),
        "tamaño_efectivo_aprox": int(len(quemado) * (1 - lag1) / (1 + lag1)),
        "por_que_leapfrog": "es un integrador simpléctico: conserva el volumen de fase",
        "ventaja_sobre_random_walk": "propuestas lejanas con aceptación alta",
        "coste": "L evaluaciones del gradiente por muestra",
        "NUTS": "elige L automáticamente evitando que la trayectoria se doble",
    }


def advanced_variational_inference() -> dict:
    """Inferencia variacional: optimizar en lugar de muestrear."""
    # Posterior objetivo: Normal(3.0, 0.8). Familia variacional: Normal(m, s).
    mu_real, sigma_real = 3.0, 0.8

    def kl_normales(m, s):
        return math.log(sigma_real / s) + (s**2 + (m - mu_real) ** 2) / (2 * sigma_real**2) - 0.5

    m, log_s = 0.0, 0.0
    lr = 0.1
    historial = []
    for paso in range(1, 401):
        h = 1e-5
        dm = (kl_normales(m + h, math.exp(log_s)) - kl_normales(m - h, math.exp(log_s))) / (2 * h)
        ds = (kl_normales(m, math.exp(log_s + h)) - kl_normales(m, math.exp(log_s - h))) / (2 * h)
        m -= lr * dm
        log_s -= lr * ds
        if paso in (1, 50, 150, 400):
            historial.append({"paso": paso, "m": round(m, 6), "s": round(math.exp(log_s), 6),
                              "KL": round(kl_normales(m, math.exp(log_s)), 8)})
    return {
        "posterior_real": {"mu": mu_real, "sigma": sigma_real},
        "familia_variacional": "Normal(m, s)",
        "historial": historial,
        "solucion": {"m": round(m, 6), "s": round(math.exp(log_s), 6)},
        "KL_final": round(kl_normales(m, math.exp(log_s)), 10),
        "converge_al_posterior": abs(m - mu_real) < 1e-3,
        "VI_es_optimizacion": "MCMC es muestreo; VI es descenso de gradiente",
        "sesgo": "la familia elegida puede no contener el posterior real",
        "mean_field": "suponer independencia entre variables subestima la varianza",
    }


def optimal_transport() -> dict:
    """Transporte óptimo por Sinkhorn: coste de mover una distribución a otra."""
    a = [0.4, 0.3, 0.3]
    b = [0.2, 0.5, 0.3]
    posiciones_a = [0.0, 1.0, 2.0]
    posiciones_b = [0.5, 1.5, 3.0]
    C = [[abs(x - y) for y in posiciones_b] for x in posiciones_a]

    reg = 0.05
    K = [[math.exp(-c / reg) for c in fila] for fila in C]
    u = [1.0] * 3
    v = [1.0] * 3
    for _ in range(500):
        u = [a[i] / max(sum(K[i][j] * v[j] for j in range(3)), 1e-300) for i in range(3)]
        v = [b[j] / max(sum(K[i][j] * u[i] for i in range(3)), 1e-300) for j in range(3)]
    plan = [[u[i] * K[i][j] * v[j] for j in range(3)] for i in range(3)]
    coste = sum(plan[i][j] * C[i][j] for i in range(3) for j in range(3))
    return {
        "distribucion_origen": a,
        "distribucion_destino": b,
        "matriz_de_coste": [[round(c, 4) for c in fila] for fila in C],
        "regularizacion_entropica": reg,
        "plan_de_transporte": [[round(v, 6) for v in fila] for fila in plan],
        "marginales_fila": [round(sum(fila), 6) for fila in plan],
        "marginales_columna": [round(sum(plan[i][j] for i in range(3)), 6) for j in range(3)],
        "coste_de_transporte": round(coste, 6),
        "algoritmo": "Sinkhorn-Knopp (escalado iterativo)",
        "reg_menor": "más cerca del óptimo exacto, pero peor condicionamiento",
        "referencia": "Cuturi, NIPS 2013",
    }


def wasserstein_distance() -> dict:
    """Wasserstein-1 en 1D: comparar distribuciones sin soporte común."""
    def w1(muestras_p, muestras_q):
        p, q = sorted(muestras_p), sorted(muestras_q)
        return sum(abs(a - b) for a, b in zip(p, q)) / len(p)

    rng = random.Random(SEED)
    n = 2_000
    p = [rng.gauss(0, 1) for _ in range(n)]
    q_cercana = [rng.gauss(0.5, 1) for _ in range(n)]
    q_lejana = [rng.gauss(5.0, 1) for _ in range(n)]

    # KL empírica con histogramas: se rompe cuando los soportes son disjuntos.
    def kl_hist(x, y, bins=40, lo=-8.0, hi=12.0):
        ancho = (hi - lo) / bins
        def hist(s):
            h = [0.0] * bins
            for v in s:
                idx = min(bins - 1, max(0, int((v - lo) / ancho)))
                h[idx] += 1
            return [c / len(s) for c in h]
        hp, hq = hist(x), hist(y)
        return sum(a * math.log(a / b) for a, b in zip(hp, hq) if a > 0 and b > 0)

    return {
        "muestras": n,
        "W1(N(0,1), N(0.5,1))": round(w1(p, q_cercana), 6),
        "diferencia_de_medias_teorica": 0.5,
        "W1(N(0,1), N(5,1))": round(w1(p, q_lejana), 6),
        "diferencia_teorica_lejana": 5.0,
        "KL_empirica_cercana": round(kl_hist(p, q_cercana), 6),
        "KL_empirica_lejana_(soportes_casi_disjuntos)": round(kl_hist(p, q_lejana), 6),
        "W1_crece_de_forma_proporcional": True,
        "KL_no_informa_cuando_no_hay_solape": True,
        "por_que_importa_en_GAN": "el gradiente de W1 sigue siendo útil sin solape",
        "formula_1D": "W1 = ∫|F_p(t) - F_q(t)|dt = media de |cuantiles ordenados|",
    }


def manifold_learning() -> dict:
    """Variedad: dimensión intrínseca menor que la del espacio ambiente."""
    n = 120
    datos = []
    for i in range(n):
        t = 3 * math.pi * i / n
        # espiral en 3D: 1 grado de libertad embebido en ℝ³
        datos.append([t * math.cos(t) / 10, t * math.sin(t) / 10, t / 10])

    cov = la.covariance(datos)
    valores, _ = la.symmetric_eigen(cov)
    total = sum(valores)

    # Distancia geodésica aproximada frente a distancia euclídea
    i, j = 0, n - 1
    euclidea = math.dist(datos[i], datos[j])
    geodesica = sum(math.dist(datos[k], datos[k + 1]) for k in range(n - 1))
    return {
        "puntos": n,
        "dimension_ambiente": 3,
        "dimension_intrinseca": 1,
        "autovalores_de_la_covarianza": [round(v, 6) for v in valores],
        "varianza_explicada_%": [round(100 * v / total, 4) for v in valores],
        "PCA_no_detecta_1_dimension": sum(1 for v in valores if v / total > 0.05) > 1,
        "distancia_euclidea_extremos": round(euclidea, 6),
        "distancia_geodesica_extremos": round(geodesica, 6),
        "razon": round(geodesica / euclidea, 4),
        "por_que_falla_PCA": "la variedad es curva y PCA solo encuentra subespacios lineales",
        "alternativas": ["Isomap", "LLE", "t-SNE", "UMAP", "autoencoders"],
    }


def differential_geometry() -> dict:
    """Geometría diferencial: métrica, longitud de curva y curvatura."""
    def curva(t):
        return [math.cos(t), math.sin(t), 0.3 * t]

    def velocidad(t, h=1e-6):
        a, b = curva(t + h), curva(t - h)
        return [(x - y) / (2 * h) for x, y in zip(a, b)]

    def aceleracion(t, h=1e-4):
        a, b, c = curva(t + h), curva(t), curva(t - h)
        return [(x - 2 * y + z) / (h * h) for x, y, z in zip(a, b, c)]

    n = 2_000
    t_max = 2 * math.pi
    longitud = sum(la.norm(velocidad(k * t_max / n)) * t_max / n for k in range(n))
    v = velocidad(1.0)
    a = aceleracion(1.0)
    cross = [v[1] * a[2] - v[2] * a[1], v[2] * a[0] - v[0] * a[2], v[0] * a[1] - v[1] * a[0]]
    curvatura = la.norm(cross) / la.norm(v) ** 3
    return {
        "curva": "hélice (cos t, sin t, 0.3t)",
        "velocidad_en_t=1": [round(x, 6) for x in v],
        "rapidez": round(la.norm(v), 6),
        "rapidez_teorica_√(1+0.09)": round(math.sqrt(1 + 0.09), 6),
        "longitud_de_arco_0_a_2π": round(longitud, 6),
        "longitud_teorica": round(2 * math.pi * math.sqrt(1.09), 6),
        "curvatura": round(curvatura, 6),
        "curvatura_teorica_1/1.09": round(1 / 1.09, 6),
        "metrica_riemanniana": "define longitudes y ángulos en cada punto de la variedad",
        "geodesica": "curva que localmente minimiza la longitud",
    }


def information_geometry() -> dict:
    """Información de Fisher: la métrica natural del espacio de parámetros."""
    # Familia Bernoulli(p): I(p) = 1/(p(1-p))
    def fisher_bernoulli(p):
        return 1.0 / (p * (1 - p))

    # Familia Normal(mu, sigma): I(mu) = 1/sigma²
    def fisher_normal(sigma):
        return 1.0 / sigma**2

    def kl_bernoulli(p, q):
        return p * math.log(p / q) + (1 - p) * math.log((1 - p) / (1 - q))

    eps = 1e-4
    aproximacion = {}
    for p in (0.1, 0.5, 0.9):
        kl = kl_bernoulli(p, p + eps)
        aproximacion[f"p={p}"] = {
            "KL(p ‖ p+ε)": round(kl, 12),
            "½·I(p)·ε²": round(0.5 * fisher_bernoulli(p) * eps**2, 12),
            "razon": round(kl / (0.5 * fisher_bernoulli(p) * eps**2), 6),
        }
    return {
        "informacion_de_Fisher_Bernoulli": {f"p={p}": round(fisher_bernoulli(p), 6)
                                            for p in (0.1, 0.5, 0.9)},
        "la_informacion_es_maxima_en_los_extremos": fisher_bernoulli(0.1) > fisher_bernoulli(0.5),
        "informacion_de_Fisher_Normal": {f"σ={s}": round(fisher_normal(s), 6) for s in (0.5, 1.0, 2.0)},
        "KL_localmente_es_una_metrica": aproximacion,
        "cota_de_Cramer_Rao": "Var(estimador insesgado) ≥ 1/(n·I(θ))",
        "gradiente_natural": "∇̃ = I(θ)⁻¹∇: invariante a la reparametrización",
        "conexion_con_ML": "K-FAC y Adam aproximan información de segundo orden",
    }


def stochastic_differential_equations() -> dict:
    """SDE: proceso de Ornstein-Uhlenbeck simulado con Euler-Maruyama."""
    theta, mu, sigma = 1.5, 2.0, 0.8
    dt = 0.01
    pasos = 3_000
    rng = random.Random(SEED)

    trayectorias = []
    finales = []
    for _ in range(400):
        x = 0.0
        for _ in range(pasos):
            x += theta * (mu - x) * dt + sigma * math.sqrt(dt) * rng.gauss(0, 1)
        finales.append(x)
    media = sum(finales) / len(finales)
    var = sum((v - media) ** 2 for v in finales) / len(finales)

    rng2 = random.Random(SEED + 1)
    x = 0.0
    for k in range(pasos):
        x += theta * (mu - x) * dt + sigma * math.sqrt(dt) * rng2.gauss(0, 1)
        if k in (0, 100, 1_000, 2_999):
            trayectorias.append({"paso": k + 1, "t": round((k + 1) * dt, 3), "x": round(x, 6)})

    return {
        "SDE": "dX = θ(μ - X)dt + σ dW",
        "parametros": {"theta": theta, "mu": mu, "sigma": sigma},
        "integrador": "Euler-Maruyama",
        "dt": dt,
        "trayectoria_de_ejemplo": trayectorias,
        "replicas": 400,
        "media_estacionaria_empirica": round(media, 4),
        "media_estacionaria_teorica": mu,
        "varianza_estacionaria_empirica": round(var, 4),
        "varianza_estacionaria_teorica_σ²/(2θ)": round(sigma**2 / (2 * theta), 4),
        "el_termino_de_ruido_escala_como_√dt": True,
        "conexion_con_difusion": "el proceso directo de un modelo de difusión es una SDE",
        "semilla": SEED,
    }


def neural_odes() -> dict:
    """Neural ODE: capas continuas y el método adjunto."""
    # dz/dt = f(z, θ) con f(z) = -θz  ->  solución z(t) = z0·e^(-θt)
    theta, z0, T = 1.2, 1.0, 1.5

    def exacta(t):
        return z0 * math.exp(-theta * t)

    informe = []
    for n in (5, 20, 80, 320):
        h = T / n
        z = z0
        for _ in range(n):
            z += h * (-theta * z)
        informe.append({"pasos": n, "z(T)": round(z, 8), "error": abs(z - exacta(T))})

    # Método adjunto: da/dt = -a·∂f/∂z, con a(T) = dL/dz(T)
    dLdz_T = 2 * (exacta(T) - 0.2)
    a = dLdz_T
    n = 400
    h = T / n
    grad_theta = 0.0
    z = exacta(T)
    for k in range(n):
        grad_theta += a * (-z) * h          # ∂f/∂θ = -z
        a += h * (a * theta)                # integrar hacia atrás
        z += h * (theta * z)
    # gradiente analítico: dL/dθ = 2(z(T)-0.2)·(-T·z0·e^{-θT})
    analitico = dLdz_T * (-T * z0 * math.exp(-theta * T))
    return {
        "ODE": "dz/dt = -θz",
        "solucion_analitica": "z₀·e^(-θt)",
        "z(T)_exacto": round(exacta(T), 8),
        "convergencia_de_Euler": informe,
        "perdida": "L = (z(T) - 0.2)²",
        "dL/dθ_por_metodo_adjunto": round(grad_theta, 6),
        "dL/dθ_analitico": round(analitico, 6),
        "coinciden_aproximadamente": abs(grad_theta - analitico) / abs(analitico) < 0.05,
        "memoria_del_adjunto": "O(1) en el número de pasos, frente a O(n) del backprop clásico",
        "profundidad": "continua: el solver elige cuántas evaluaciones necesita",
        "referencia": "Chen et al., NeurIPS 2018",
    }


def score_matching() -> dict:
    """Score matching: aprender ∇ log p sin conocer la constante de normalización."""
    mu, sigma = 1.5, 0.7

    def log_p(x):
        return -0.5 * ((x - mu) / sigma) ** 2 - math.log(sigma * math.sqrt(2 * math.pi))

    def score_analitico(x):
        return -(x - mu) / sigma**2

    def score_numerico(x, h=1e-5):
        return (log_p(x + h) - log_p(x - h)) / (2 * h)

    puntos = [0.0, 1.5, 3.0]
    comparacion = {f"x={x}": {"analitico": round(score_analitico(x), 6),
                              "numerico": round(score_numerico(x), 6)} for x in puntos}

    # El score no cambia si multiplicamos p por una constante arbitraria.
    def log_p_sin_normalizar(x):
        return -0.5 * ((x - mu) / sigma) ** 2 + 42.0

    sin_norm = (log_p_sin_normalizar(1.0 + 1e-5) - log_p_sin_normalizar(1.0 - 1e-5)) / 2e-5

    rng = random.Random(SEED)
    langevin = []
    x = 0.0
    eps = 0.01
    for k in range(4_000):
        x += 0.5 * eps * score_analitico(x) + math.sqrt(eps) * rng.gauss(0, 1)
        if k >= 1_000:
            langevin.append(x)
    media_langevin = sum(langevin) / len(langevin)
    return {
        "distribucion": f"Normal({mu}, {sigma})",
        "score": "∇ₓ log p(x)",
        "comparacion": comparacion,
        "score_con_constante_arbitraria": round(sin_norm, 6),
        "es_el_mismo": abs(sin_norm - score_analitico(1.0)) < 1e-4,
        "por_que_importa": "el score no necesita la constante de normalización Z",
        "muestreo_de_Langevin": {
            "media_objetivo": mu,
            "media_obtenida": round(media_langevin, 4),
            "muestras_tras_burn_in": len(langevin),
        },
        "relacion_con_difusion": "un modelo de difusión aprende el score de p(x_t)",
        "denoising_score_matching": "estimar el ruido equivale a estimar el score",
        "referencia": "Hyvärinen, JMLR 2005; Song & Ermon, NeurIPS 2019",
    }


def spectral_graph_theory() -> dict:
    """Clustering espectral: el vector de Fiedler separa el grafo."""
    # Dos comunidades unidas por una sola arista.
    n = 8
    aristas = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (4, 5), (4, 6), (5, 6), (5, 7), (6, 7),
               (3, 4)]
    A = la.zeros(n, n)
    for i, j in aristas:
        A[i][j] = A[j][i] = 1.0
    grados = [sum(fila) for fila in A]
    L = [[(grados[i] if i == j else 0.0) - A[i][j] for j in range(n)] for i in range(n)]
    valores, vectores = la.symmetric_eigen(L)
    orden = sorted(range(n), key=lambda i: valores[i])
    fiedler = [vectores[i][orden[1]] for i in range(n)]
    grupo_a = [i for i in range(n) if fiedler[i] >= 0]
    grupo_b = [i for i in range(n) if fiedler[i] < 0]
    corte = sum(1 for i, j in aristas if (i in grupo_a) != (j in grupo_a))
    return {
        "nodos": n,
        "aristas": len(aristas),
        "autovalores_ordenados": [round(valores[i], 8) for i in orden],
        "conectividad_algebraica": round(valores[orden[1]], 8),
        "grafo_conexo": abs(valores[orden[0]]) < 1e-8 and valores[orden[1]] > 1e-8,
        "vector_de_Fiedler": [round(v, 6) for v in fiedler],
        "particion": {"grupo_A": grupo_a, "grupo_B": grupo_b},
        "aristas_cortadas": corte,
        "corte_minimo_esperado": 1,
        "particion_correcta": corte == 1,
        "cota_de_Cheeger": "λ₂/2 ≤ h(G) ≤ √(2λ₂)",
    }


def causal_inference() -> dict:
    """Confusión, ajuste por backdoor y el sesgo de colisionador."""
    rng = random.Random(SEED)
    n = 6_000
    # Z confunde X e Y:  Z -> X, Z -> Y
    filas = []
    for _ in range(n):
        z = rng.gauss(0, 1)
        x = 0.9 * z + rng.gauss(0, 0.5)
        y = 0.0 * x + 1.2 * z + rng.gauss(0, 0.5)     # efecto causal real de X sobre Y = 0
        filas.append((x, y, z))

    def regresion(cols_x, col_y):
        A = [[1.0] + [f[c] for c in cols_x] for f in filas]
        b = [f[col_y] for f in filas]
        At = la.transpose(A)
        w, _, _ = la.gaussian_elimination(la.matmul(At, A), la.matvec(At, b))
        return w

    ingenua = regresion([0], 1)
    ajustada = regresion([0, 2], 1)

    # Colisionador: C <- X, C <- Y; condicionar en C crea asociación espuria
    colisionador = []
    for _ in range(n):
        x = rng.gauss(0, 1)
        y = rng.gauss(0, 1)
        colisionador.append((x, y, x + y + rng.gauss(0, 0.2)))
    seleccion = [(x, y) for x, y, c in colisionador if c > 1.0]

    def corr(pares):
        n2 = len(pares)
        mx = sum(p[0] for p in pares) / n2
        my = sum(p[1] for p in pares) / n2
        num = sum((p[0] - mx) * (p[1] - my) for p in pares)
        den = math.sqrt(sum((p[0] - mx) ** 2 for p in pares) * sum((p[1] - my) ** 2 for p in pares))
        return num / den

    return {
        "efecto_causal_real_de_X_sobre_Y": 0.0,
        "coeficiente_sin_ajustar": round(ingenua[1], 4),
        "coeficiente_ajustando_por_Z": round(ajustada[1], 4),
        "el_ajuste_recupera_el_efecto": abs(ajustada[1]) < 0.1,
        "criterio_backdoor": "bloquear todos los caminos X ← … → Y",
        "correlacion_X_Y_sin_condicionar_el_colisionador": round(corr([(x, y) for x, y, _ in colisionador]), 4),
        "correlacion_condicionando_el_colisionador": round(corr(seleccion), 4),
        "condicionar_un_colisionador_crea_sesgo": abs(corr(seleccion)) > 0.2,
        "regla": "no todo control mejora la estimación: controlar de más también sesga",
        "referencia": "Pearl, *Causality*, 2ª ed., 2009",
    }


def statistical_learning_theory() -> dict:
    """Riesgo empírico frente a riesgo verdadero y la brecha de generalización."""
    rng = random.Random(SEED)

    def experimento(n, complejidad):
        # Etiquetas aleatorias: no hay señal. Un modelo complejo memoriza.
        X = [[rng.gauss(0, 1) for _ in range(complejidad)] for _ in range(n)]
        y = [1.0 if rng.random() < 0.5 else 0.0 for _ in range(n)]
        Xt = la.transpose(X)
        normal = la.matmul(Xt, X)
        normal = [[normal[i][j] + (0.01 if i == j else 0.0) for j in range(complejidad)]
                  for i in range(complejidad)]
        w, _, _ = la.gaussian_elimination(normal, la.matvec(Xt, y))
        train = sum(1 for xi, yi in zip(X, y) if (la.dot(w, xi) >= 0.5) == (yi == 1.0)) / n
        Xn = [[rng.gauss(0, 1) for _ in range(complejidad)] for _ in range(200)]
        yn = [1.0 if rng.random() < 0.5 else 0.0 for _ in range(200)]
        test = sum(1 for xi, yi in zip(Xn, yn) if (la.dot(w, xi) >= 0.5) == (yi == 1.0)) / 200
        return round(train, 4), round(test, 4)

    resultados = {}
    for n, d in ((30, 25), (30, 5), (300, 25)):
        tr, te = experimento(n, d)
        resultados[f"n={n}, d={d}"] = {"accuracy_train": tr, "accuracy_test": te,
                                       "brecha": round(tr - te, 4)}
    return {
        "señal_real_en_los_datos": "ninguna (etiquetas aleatorias)",
        "accuracy_esperada": 0.5,
        "resultados": resultados,
        "mas_parametros_que_datos_memoriza": resultados["n=30, d=25"]["brecha"] > resultados["n=300, d=25"]["brecha"],
        "descomposicion": "R(h) = R_emp(h) + brecha de generalización",
        "cota_uniforme": "sup_h |R(h) - R_emp(h)| controla el peor caso de la clase",
        "el_riesgo_empirico_solo_no_basta": True,
        "semilla": SEED,
    }


def vc_dimension() -> dict:
    """Dimensión VC: cuántos puntos puede fragmentar una clase de hipótesis."""
    def puede_fragmentar_umbral(k):
        # Clasificadores de umbral en 1D: h(x) = 1 si x > t
        puntos = list(range(k))
        for etiquetas in range(2**k):
            objetivo = [(etiquetas >> i) & 1 for i in range(k)]
            posible = any(
                all((1 if p > t else 0) == e for p, e in zip(puntos, objetivo))
                for t in [-0.5 + i for i in range(k + 1)]
            )
            if not posible:
                return False
        return True

    return {
        "clase_umbral_1D": {
            "fragmenta_1_punto": puede_fragmentar_umbral(1),
            "fragmenta_2_puntos": puede_fragmentar_umbral(2),
            "VC": 1,
        },
        "intervalos_1D": {"VC": 2, "razon": "no puede etiquetar + - + con un único intervalo"},
        "hiperplanos_en_R^d": {"VC": "d + 1"},
        "hiperplanos_en_R^2": 3,
        "por_que_no_4_puntos_en_R2": "XOR en las esquinas de un cuadrado no es separable",
        "clase_infinita_con_VC_finita": "los umbrales son infinitos pero su VC es 1",
        "lema_de_Sauer": "|H restringida a m puntos| ≤ Σ_{i≤VC} C(m,i)",
        "cota_de_generalizacion": "R(h) ≤ R_emp(h) + O(√((VC·log m + log(1/δ))/m))",
        "VC_infinita": "1-NN: memoriza cualquier etiquetado, no hay garantía uniforme",
    }


def pac_learning() -> dict:
    """PAC: cuántas muestras hacen falta para (ε, δ)."""
    def muestras_finitas(tam_clase, eps, delta):
        return math.ceil((math.log(tam_clase) + math.log(1 / delta)) / eps)

    def muestras_vc(vc, eps, delta):
        return math.ceil((vc * math.log(1 / eps) + math.log(1 / delta)) / eps)

    tabla = {}
    for eps in (0.1, 0.05, 0.01):
        tabla[f"ε={eps}"] = {
            "clase_de_1000_hipotesis": muestras_finitas(1_000, eps, 0.05),
            "VC=10": muestras_vc(10, eps, 0.05),
            "VC=100": muestras_vc(100, eps, 0.05),
        }
    return {
        "definicion": "con probabilidad ≥ 1-δ, el error del hipótesis elegido es ≤ ε",
        "delta": 0.05,
        "muestras_necesarias": tabla,
        "el_coste_crece_como_1/ε": True,
        "el_coste_crece_como_log(1/δ)": "aumentar la confianza es barato",
        "dependencia_de_la_complejidad": "lineal en VC",
        "es_una_cota_del_peor_caso": True,
        "limite_practico": "las cotas PAC son muy holgadas para redes profundas",
        "referencia": "Valiant, 1984; Shalev-Shwartz & Ben-David, 2014",
    }


def approximation_theory() -> dict:
    """Teoría de aproximación y leyes de escala: el error como potencia del tamaño."""
    def objetivo(x):
        return math.exp(-x) * math.sin(4 * x)

    # 1) Aproximación polinómica: el error cae rápido con el grado (función suave)
    nodos_ref = [i / 200 for i in range(201)]
    aproximacion = []
    for grado in (1, 3, 5, 9):
        nodos = [i / grado for i in range(grado + 1)]
        valores = [objetivo(x) for x in nodos]

        def interpolar(x, nodos=nodos, valores=valores):
            total = 0.0
            for i, (xi, yi) in enumerate(zip(nodos, valores)):
                base = 1.0
                for j, xj in enumerate(nodos):
                    if i != j:
                        base *= (x - xj) / (xi - xj)
                total += yi * base
            return total

        error = max(abs(interpolar(x) - objetivo(x)) for x in nodos_ref)
        aproximacion.append({"grado": grado, "parametros": grado + 1,
                             "error_maximo": round(error, 10)})

    # 2) Ley de escala empírica: ajustar log(error) ~ a - b·log(parámetros)
    xs = [math.log(p["parametros"]) for p in aproximacion]
    ys = [math.log(p["error_maximo"]) for p in aproximacion]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    pendiente = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)

    # 3) Aproximación por funciones a trozos (ReLU): error O(1/k²) con k trozos
    trozos = []
    for k in (2, 4, 8, 16):
        h = 1.0 / k
        error = max(
            abs(objetivo(x) - (objetivo(math.floor(x / h) * h)
                               + (objetivo(min(math.floor(x / h) * h + h, 1.0))
                                  - objetivo(math.floor(x / h) * h)) * ((x % h) / h)))
            for x in nodos_ref[:-1]
        )
        trozos.append({"trozos": k, "error_maximo": round(error, 10)})

    return {
        "funcion_objetivo": "e^(-x)·sin(4x) en [0,1]",
        "aproximacion_polinomica": aproximacion,
        "exponente_de_escala_empirico": round(pendiente, 4),
        "lectura": "error ≈ C·(parámetros)^(exponente)",
        "aproximacion_lineal_por_trozos": trozos,
        "razon_de_error_al_duplicar_trozos": round(
            trozos[0]["error_maximo"] / trozos[1]["error_maximo"], 4),
        "orden_teorico_por_trozos": "O(h²) para funciones C²",
        "teorema_de_aproximacion_universal": (
            "una red de una capa oculta aproxima cualquier función continua en un compacto, "
            "pero no dice cuántas neuronas hacen falta ni si el entrenamiento las encontrará"
        ),
        "maldicion_de_la_dimension": "el número de parámetros crece como ε^(-d/s)",
        "leyes_de_escala_en_LLM": "pérdida ≈ A·N^(-α) + B·D^(-β) + L∞ (Kaplan 2020; Hoffmann 2022)",
        "lo_que_no_dicen_las_leyes_de_escala": "no garantizan capacidades, solo pérdida agregada",
    }


def capstone_reproduce_paper_idea() -> dict:
    """Capstone: reproducir el núcleo matemático de un resultado publicado.

    Idea reproducida: el estimador de Sinkhorn del transporte óptimo converge
    al plan exacto cuando la regularización entrópica tiende a cero
    (Cuturi, NIPS 2013), y la distancia resultante se comporta como una
    distancia entre distribuciones.
    """
    # Dos distribuciones uniformes de 2 átomos. El coste cuadrático hace que el
    # emparejamiento SÍ importe: con coste |x-y| y estas marginales el problema
    # sería degenerado (todos los planes cuestan lo mismo) y no demostraría nada.
    a = [0.5, 0.5]
    b = [0.5, 0.5]
    pos_a = [0.0, 1.0]
    pos_b = [0.0, 3.0]

    def coste_matriz(xa, xb):
        return [[(x - y) ** 2 for y in xb] for x in xa]

    def optimo_exacto(C):
        """Óptimo exacto por barrido de la única masa libre del problema 2×2."""
        mejor = None
        for k in range(0, 5001):
            t = 0.5 * k / 5000                 # masa que va de a₀ a b₀
            plan = [[t, 0.5 - t], [0.5 - t, t]]
            valor = sum(plan[i][j] * C[i][j] for i in range(2) for j in range(2))
            if mejor is None or valor < mejor[0]:
                mejor = (valor, plan)
        return mejor

    def sinkhorn(C, reg, iteraciones=3_000):
        K = [[math.exp(-c / reg) for c in fila] for fila in C]
        u = [1.0, 1.0]
        v = [1.0, 1.0]
        for _ in range(iteraciones):
            u = [a[i] / max(sum(K[i][j] * v[j] for j in range(2)), 1e-300) for i in range(2)]
            v = [b[j] / max(sum(K[i][j] * u[i] for i in range(2)), 1e-300) for j in range(2)]
        plan = [[u[i] * K[i][j] * v[j] for j in range(2)] for i in range(2)]
        coste = sum(plan[i][j] * C[i][j] for i in range(2) for j in range(2))
        return plan, coste

    C = coste_matriz(pos_a, pos_b)
    exacto, plan_optimo = optimo_exacto(C)
    peor = max(
        sum(plan[i][j] * C[i][j] for i in range(2) for j in range(2))
        for plan in ([[0.5, 0.0], [0.0, 0.5]], [[0.0, 0.5], [0.5, 0.0]])
    )

    # 1) El coste regularizado converge al óptimo exacto cuando ε → 0.
    convergencia = []
    for reg in (4.0, 1.0, 0.3, 0.05):
        plan, coste = sinkhorn(C, reg)
        convergencia.append({
            "regularizacion": reg,
            "coste_regularizado": round(coste, 6),
            "error_vs_optimo": round(coste - exacto, 6),
            "masa_en_el_emparejamiento_optimo": round(plan[0][0] + plan[1][1], 6),
            "entropia_del_plan": round(
                -sum(p * math.log(max(p, 1e-300)) for fila in plan for p in fila), 6),
        })
    errores = [c["error_vs_optimo"] for c in convergencia]

    # 2) La distancia W₂² entre una distribución y su traslación es d².
    traslaciones = {}
    for d in (0.0, 1.0, 2.0, 3.0):
        _, coste = sinkhorn(coste_matriz(pos_a, [x + d for x in pos_a]), 0.02)
        traslaciones[f"d={d}"] = {"obtenido": round(coste, 4), "prediccion_d²": round(d * d, 4)}

    # 3) Simetría: transportar A→B cuesta lo mismo que B→A.
    _, ida = sinkhorn(coste_matriz(pos_a, pos_b), 0.05)
    _, vuelta = sinkhorn(coste_matriz(pos_b, pos_a), 0.05)

    return {
        "resultado_reproducido": (
            "el coste de Sinkhorn converge al transporte óptimo cuando la "
            "regularización entrópica ε tiende a cero"
        ),
        "fuente": "Cuturi, M. *Sinkhorn Distances: Lightspeed Computation of Optimal Transport*. NIPS, 2013",
        "protocolo": {
            "distribuciones": "dos masas uniformes de 2 átomos en ℝ",
            "posiciones_origen": pos_a,
            "posiciones_destino": pos_b,
            "coste": "(x - y)²",
            "iteraciones_de_escalado": 3_000,
            "implementacion": "Python estándar, sin dependencias",
        },
        "matriz_de_coste": C,
        "optimo_exacto_por_barrido": round(exacto, 8),
        "plan_optimo": plan_optimo,
        "peor_plan_extremo": round(peor, 8),
        "el_problema_no_es_degenerado": abs(peor - exacto) > 1e-6,
        "convergencia_al_bajar_epsilon": convergencia,
        "el_error_decrece_monotonamente": all(
            errores[i] > errores[i + 1] for i in range(len(errores) - 1)),
        "el_error_es_siempre_positivo": all(e >= -1e-9 for e in errores),
        "la_entropia_del_plan_baja_con_epsilon": (
            convergencia[-1]["entropia_del_plan"] < convergencia[0]["entropia_del_plan"]),
        "traslaciones": traslaciones,
        "coincide_con_d²": all(
            abs(v["obtenido"] - v["prediccion_d²"]) < 0.05 for v in traslaciones.values()),
        "simetria_ida_A_a_B": round(ida, 6),
        "simetria_vuelta_B_a_A": round(vuelta, 6),
        "diferencia": round(abs(ida - vuelta), 9),
        "tolerancia_declarada": 1e-3,
        "es_simetrica": abs(ida - vuelta) < 1e-3,
        "por_que_no_es_exacta": (
            "el escalado alternado (primero u, luego v) rompe la simetría a un número "
            "finito de iteraciones; la diferencia es residuo de convergencia, no del modelo"
        ),
        "limites_declarados": [
            "2 átomos por distribución: el caso más simple en el que el resultado es visible",
            "la regularización entrópica introduce un sesgo positivo que solo se anula en el límite",
            "no se reproduce el análisis de complejidad ni el comportamiento en alta dimensión",
            "con ε muy pequeño el algoritmo se vuelve numéricamente inestable: aquí se para en 0.02",
        ],
        "que_significa_reproducir": (
            "recuperar la predicción cuantitativa del paper con una implementación "
            "independiente, no repetir su texto"
        ),
    }


DEMOS = {
    "gaussian_processes": gaussian_processes,
    "advanced_kernels": advanced_kernels,
    "advanced_mcmc": advanced_mcmc,
    "hamiltonian_monte_carlo": hamiltonian_monte_carlo,
    "advanced_variational_inference": advanced_variational_inference,
    "optimal_transport": optimal_transport,
    "wasserstein_distance": wasserstein_distance,
    "manifold_learning": manifold_learning,
    "differential_geometry": differential_geometry,
    "information_geometry": information_geometry,
    "stochastic_differential_equations": stochastic_differential_equations,
    "neural_odes": neural_odes,
    "score_matching": score_matching,
    "spectral_graph_theory": spectral_graph_theory,
    "causal_inference": causal_inference,
    "statistical_learning_theory": statistical_learning_theory,
    "vc_dimension": vc_dimension,
    "pac_learning": pac_learning,
    "approximation_theory": approximation_theory,
    "capstone_reproduce_paper_idea": capstone_reproduce_paper_idea,
}

CLASS_DEMOS = {
    "341": "gaussian_processes",
    "342": "advanced_kernels",
    "343": "advanced_mcmc",
    "344": "hamiltonian_monte_carlo",
    "345": "advanced_variational_inference",
    "346": "optimal_transport",
    "347": "wasserstein_distance",
    "348": "manifold_learning",
    "349": "differential_geometry",
    "350": "information_geometry",
    "351": "stochastic_differential_equations",
    "352": "neural_odes",
    "353": "score_matching",
    "354": "spectral_graph_theory",
    "355": "causal_inference",
    "356": "statistical_learning_theory",
    "357": "vc_dimension",
    "358": "pac_learning",
    "359": "approximation_theory",
    "360": "capstone_reproduce_paper_idea",
}
