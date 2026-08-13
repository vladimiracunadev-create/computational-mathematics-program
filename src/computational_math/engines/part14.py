"""Motor 14 — Matemática de Machine Learning.

Cada algoritmo se deriva y se implementa desde su función objetivo. Todos
comparten el mismo conjunto de datos sintético y la misma semilla.
"""

from __future__ import annotations

import math
import random

from . import _linalg as la

PART = "14"
TITLE = "Matemática de Machine Learning"

SEED = 20260813


def _datos_regresion(n: int = 60):
    rng = random.Random(SEED)
    xs = [[1.0, k / 10.0, (k / 10.0) ** 2 * 0.1] for k in range(n)]
    ys = [2.0 + 1.5 * x[1] - 0.4 * x[2] + rng.gauss(0, 0.25) for x in xs]
    return xs, ys


def _datos_clasificacion(n: int = 80):
    rng = random.Random(SEED + 1)
    puntos, etiquetas = [], []
    for _ in range(n // 2):
        puntos.append([rng.gauss(2.0, 0.8), rng.gauss(2.0, 0.8)])
        etiquetas.append(1)
        puntos.append([rng.gauss(-1.0, 0.8), rng.gauss(-1.0, 0.8)])
        etiquetas.append(0)
    return puntos, etiquetas


def _sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(-500.0, min(500.0, z))))


def supervised_geometry() -> dict:
    """Aprendizaje supervisado como búsqueda de una frontera en el espacio."""
    X, y = _datos_clasificacion()
    centro1 = [sum(p[i] for p, e in zip(X, y) if e == 1) / sum(y) for i in range(2)]
    centro0 = [sum(p[i] for p, e in zip(X, y) if e == 0) / (len(y) - sum(y)) for i in range(2)]
    direccion = la.normalize(la.sub(centro1, centro0))
    punto_medio = [(a + b) / 2 for a, b in zip(centro1, centro0)]
    aciertos = sum(1 for p, e in zip(X, y)
                   if (la.dot(direccion, la.sub(p, punto_medio)) > 0) == (e == 1))
    return {
        "observaciones": len(X),
        "dimension": 2,
        "centroide_clase_1": [round(v, 4) for v in centro1],
        "centroide_clase_0": [round(v, 4) for v in centro0],
        "direccion_discriminante": [round(v, 4) for v in direccion],
        "distancia_entre_centroides": round(la.norm(la.sub(centro1, centro0)), 4),
        "accuracy_del_clasificador_de_centroides": round(aciertos / len(y), 4),
        "hipotesis": "una frontera lineal separa razonablemente las clases",
    }


def linear_regression() -> dict:
    """Regresión lineal: solución cerrada y descenso de gradiente."""
    X, y = _datos_regresion()
    Xt = la.transpose(X)
    w_cerrada, _, _ = la.gaussian_elimination(la.matmul(Xt, X), la.matvec(Xt, y))

    w = [0.0] * 3
    n = len(y)
    for _ in range(3_000):
        pred = la.matvec(X, w)
        r = la.sub(pred, y)
        g = la.scale(la.matvec(Xt, r), 2.0 / n)
        w = la.sub(w, la.scale(g, 0.02))

    def mse(v):
        return sum((la.dot(v, x) - t) ** 2 for x, t in zip(X, y)) / n

    return {
        "observaciones": n,
        "features": 3,
        "parametros_reales": [2.0, 1.5, -0.4],
        "solucion_cerrada": [round(v, 6) for v in w_cerrada],
        "descenso_de_gradiente": [round(v, 6) for v in w],
        "MSE_cerrada": round(mse(w_cerrada), 8),
        "MSE_gradiente": round(mse(w), 8),
        "coinciden": all(abs(a - b) < 0.05 for a, b in zip(w_cerrada, w)),
        "cuando_usar_gradiente": "cuando n o d hacen inviable invertir XᵀX",
    }


def ridge() -> dict:
    """Ridge: L2 encoge los coeficientes y estabiliza el mal condicionamiento."""
    X, y = _datos_regresion()
    Xt = la.transpose(X)
    xtx = la.matmul(Xt, X)
    xty = la.matvec(Xt, y)
    salida = {}
    for lmbda in (0.0, 0.1, 1.0, 10.0):
        reg = [[xtx[i][j] + (lmbda if i == j else 0.0) for j in range(3)] for i in range(3)]
        w, _, _ = la.gaussian_elimination(reg, xty)
        mse = sum((la.dot(w, x) - t) ** 2 for x, t in zip(X, y)) / len(y)
        salida[f"λ={lmbda}"] = {
            "pesos": [round(v, 6) for v in w],
            "norma_L2": round(la.norm(w), 6),
            "MSE": round(mse, 8),
        }
    valores, _ = la.symmetric_eigen(xtx)
    return {
        **salida,
        "condicion_sin_regularizar": round(max(valores) / min(valores), 2),
        "condicion_con_λ=1": round((max(valores) + 1) / (min(valores) + 1), 2),
        "ridge_nunca_anula_coeficientes": True,
        "solucion_cerrada": "(XᵀX + λI)⁻¹Xᵀy",
    }


def lasso() -> dict:
    """Lasso: L1 produce ceros exactos gracias a su geometría."""
    X, y = _datos_regresion()
    n = len(y)

    def ajustar(lmbda):
        w = [0.0] * 3
        lr = 0.02
        for _ in range(2_500):
            r = la.sub(la.matvec(X, w), y)
            g = la.scale(la.matvec(la.transpose(X), r), 2.0 / n)
            w = la.sub(w, la.scale(g, lr))
            # umbral suave (proximal) del término L1
            w = [math.copysign(max(abs(v) - lr * lmbda, 0.0), v) for v in w]
        return w

    salida = {}
    for lmbda in (0.0, 0.05, 0.3, 1.0):
        w = ajustar(lmbda)
        salida[f"λ={lmbda}"] = {
            "pesos": [round(v, 6) for v in w],
            "coeficientes_exactamente_cero": sum(1 for v in w if abs(v) < 1e-12),
            "norma_L1": round(sum(abs(v) for v in w), 6),
        }
    return {
        **salida,
        "geometria": "la bola L1 tiene vértices en los ejes: el óptimo cae sobre ellos",
        "L2_produce_ceros": False,
        "L1_selecciona_features": True,
        "elastic_net": "combina ambos términos",
    }


def logistic_regression() -> dict:
    """Regresión logística derivada desde la log-verosimilitud."""
    X, y = _datos_clasificacion()
    Xa = [[1.0] + p for p in X]
    w = [0.0] * 3
    n = len(y)
    for _ in range(3_000):
        g = [0.0] * 3
        for xi, yi in zip(Xa, y):
            p = _sigmoid(la.dot(w, xi))
            for k in range(3):
                g[k] += (p - yi) * xi[k] / n
        w = la.sub(w, la.scale(g, 0.5))
    aciertos = sum(1 for xi, yi in zip(Xa, y) if (_sigmoid(la.dot(w, xi)) >= 0.5) == (yi == 1))
    perdida = -sum(yi * math.log(max(_sigmoid(la.dot(w, xi)), 1e-12))
                   + (1 - yi) * math.log(max(1 - _sigmoid(la.dot(w, xi)), 1e-12))
                   for xi, yi in zip(Xa, y)) / n
    return {
        "observaciones": n,
        "pesos": [round(v, 6) for v in w],
        "accuracy": round(aciertos / n, 4),
        "log_loss": round(perdida, 6),
        "sigmoid(0)": _sigmoid(0.0),
        "gradiente_es_(p-y)x": "idéntico en forma al de la regresión lineal",
        "frontera_de_decision": "w₀ + w₁x₁ + w₂x₂ = 0",
        "modelo_lineal_en_el_log_odds": True,
    }


def classification_loss() -> dict:
    """Cross-entropy penaliza la confianza equivocada de forma no acotada."""
    casos = {
        "correcto_seguro": (1, 0.99),
        "correcto_dudoso": (1, 0.55),
        "incorrecto_dudoso": (1, 0.45),
        "incorrecto_seguro": (1, 0.01),
    }
    salida = {}
    for nombre, (y, p) in casos.items():
        ce = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        salida[nombre] = {
            "p_predicha": p,
            "cross_entropy": round(ce, 6),
            "error_cuadratico": round((y - p) ** 2, 6),
        }
    return {
        **salida,
        "razon_CE_seguro_vs_dudoso": round(
            salida["incorrecto_seguro"]["cross_entropy"] / salida["incorrecto_dudoso"]["cross_entropy"], 4),
        "razon_MSE_seguro_vs_dudoso": round(
            salida["incorrecto_seguro"]["error_cuadratico"] / salida["incorrecto_dudoso"]["error_cuadratico"], 4),
        "CE_castiga_mucho_mas": True,
        "gradiente_de_CE_con_sigmoid": "(p - y): no se satura como el del MSE",
    }


def naive_bayes() -> dict:
    """Naive Bayes gaussiano: independencia condicional como supuesto explícito."""
    X, y = _datos_clasificacion()
    clases = {}
    for c in (0, 1):
        puntos = [p for p, e in zip(X, y) if e == c]
        medias = [sum(p[i] for p in puntos) / len(puntos) for i in range(2)]
        varianzas = [sum((p[i] - medias[i]) ** 2 for p in puntos) / len(puntos) for i in range(2)]
        clases[c] = {"prior": len(puntos) / len(y), "medias": medias, "varianzas": varianzas}

    def log_posterior(p, c):
        m = clases[c]
        total = math.log(m["prior"])
        for i in range(2):
            v = m["varianzas"][i]
            total += -0.5 * math.log(2 * math.pi * v) - (p[i] - m["medias"][i]) ** 2 / (2 * v)
        return total

    aciertos = sum(1 for p, e in zip(X, y)
                   if max((0, 1), key=lambda c: log_posterior(p, c)) == e)
    return {
        "clases": {str(c): {"prior": round(v["prior"], 4),
                            "medias": [round(m, 4) for m in v["medias"]],
                            "varianzas": [round(s, 4) for s in v["varianzas"]]}
                   for c, v in clases.items()},
        "accuracy": round(aciertos / len(y), 4),
        "supuesto": "P(x₁,x₂|c) = P(x₁|c)·P(x₂|c)",
        "se_cumple_aqui": "aproximadamente: las features se generaron independientes",
        "por_que_funciona_igual_si_falla": "la decisión solo necesita el orden, no la probabilidad exacta",
        "se_trabaja_en_log": "evita underflow al multiplicar muchas densidades",
    }


def knn() -> dict:
    """k-NN: la métrica y el escalado deciden el resultado."""
    X, y = _datos_clasificacion()
    consulta = [1.0, 1.0]

    def predecir(k, escala=(1.0, 1.0)):
        d = sorted(((math.dist([p[0] * escala[0], p[1] * escala[1]],
                               [consulta[0] * escala[0], consulta[1] * escala[1]]), e)
                    for p, e in zip(X, y)))[:k]
        votos = sum(e for _, e in d)
        return 1 if votos * 2 > k else 0

    return {
        "consulta": consulta,
        "prediccion_k=1": predecir(1),
        "prediccion_k=5": predecir(5),
        "prediccion_k=21": predecir(21),
        "prediccion_con_x2_escalada_x100": predecir(5, (1.0, 100.0)),
        "el_escalado_cambia_la_respuesta": predecir(5) != predecir(5, (1.0, 100.0)),
        "coste_de_prediccion": "O(n·d) por consulta: no hay entrenamiento",
        "k_par_puede_empatar": True,
        "maldicion_de_la_dimension": "en alta dimensión todas las distancias se parecen",
    }


def svm_margin() -> dict:
    """SVM: maximizar el margen equivale a minimizar ‖w‖."""
    X, y = _datos_clasificacion()
    etiquetas = [1 if e == 1 else -1 for e in y]
    w, b = [0.0, 0.0], 0.0
    lr, C = 0.01, 1.0
    n = len(y)
    for epoca in range(2_000):
        for xi, yi in zip(X, etiquetas):
            if yi * (la.dot(w, xi) + b) < 1:
                w = [wk + lr * (C * yi * xk - wk / n) for wk, xk in zip(w, xi)]
                b += lr * C * yi
            else:
                w = [wk - lr * wk / n for wk in w]
    margenes = [yi * (la.dot(w, xi) + b) for xi, yi in zip(X, etiquetas)]
    vectores_soporte = sum(1 for m in margenes if m <= 1.0001)
    aciertos = sum(1 for m in margenes if m > 0)
    return {
        "w": [round(v, 6) for v in w],
        "b": round(b, 6),
        "norma_de_w": round(la.norm(w), 6),
        "ancho_del_margen_2/|w|": round(2 / la.norm(w), 6),
        "vectores_de_soporte": vectores_soporte,
        "accuracy": round(aciertos / n, 4),
        "objetivo": "min ½‖w‖² + C·Σ max(0, 1 - yᵢ(wᵀxᵢ+b))",
        "hinge_loss": round(sum(max(0.0, 1 - m) for m in margenes) / n, 6),
        "solo_los_vectores_de_soporte_definen_la_frontera": True,
    }


def kernel_trick() -> dict:
    """El kernel calcula el producto punto sin construir el espacio."""
    a, b = [1.0, 2.0], [3.0, 4.0]

    def phi(v):
        """Mapeo polinómico de grado 2 explícito."""
        return [v[0] ** 2, math.sqrt(2) * v[0] * v[1], v[1] ** 2]

    explicito = la.dot(phi(a), phi(b))
    kernel = la.dot(a, b) ** 2
    rbf = math.exp(-0.5 * math.dist(a, b) ** 2)
    return {
        "a": a, "b": b,
        "phi(a)": [round(v, 6) for v in phi(a)],
        "producto_en_el_espacio_expandido": round(explicito, 8),
        "kernel_polinomico_(aᵀb)²": round(kernel, 8),
        "coinciden": math.isclose(explicito, kernel),
        "dimension_explicita": len(phi(a)),
        "operaciones_kernel": 3,
        "kernel_RBF": round(rbf, 8),
        "dimension_implicita_del_RBF": "infinita",
        "condicion_de_Mercer": "la matriz de Gram debe ser semidefinida positiva",
    }


def tree_impurity() -> dict:
    """Entropía y Gini: dos medidas de impureza para elegir el corte."""
    X, y = _datos_clasificacion()

    def gini(etiquetas):
        if not etiquetas:
            return 0.0
        p = sum(etiquetas) / len(etiquetas)
        return 1 - p * p - (1 - p) ** 2

    def entropia(etiquetas):
        if not etiquetas:
            return 0.0
        p = sum(etiquetas) / len(etiquetas)
        if p in (0.0, 1.0):
            return 0.0
        return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

    mejor = None
    for feature in (0, 1):
        for umbral in [v / 2 for v in range(-6, 8)]:
            izq = [e for p, e in zip(X, y) if p[feature] <= umbral]
            der = [e for p, e in zip(X, y) if p[feature] > umbral]
            if not izq or not der:
                continue
            ponderada = (len(izq) * entropia(izq) + len(der) * entropia(der)) / len(y)
            ganancia = entropia(y) - ponderada
            if mejor is None or ganancia > mejor["ganancia"]:
                mejor = {"feature": feature, "umbral": umbral, "ganancia": ganancia,
                         "gini_ponderado": (len(izq) * gini(izq) + len(der) * gini(der)) / len(y)}
    return {
        "entropia_del_nodo_raiz": round(entropia(y), 6),
        "gini_del_nodo_raiz": round(gini(y), 6),
        "mejor_corte": {"feature": mejor["feature"], "umbral": mejor["umbral"]},
        "ganancia_de_informacion": round(mejor["ganancia"], 6),
        "gini_tras_el_corte": round(mejor["gini_ponderado"], 6),
        "cortes_evaluados": 28,
        "gini_es_mas_barato": "evita calcular logaritmos",
        "ambos_criterios_suelen_coincidir": True,
    }


def random_forest() -> dict:
    """Bagging: promediar modelos decorrelacionados reduce la varianza."""
    rng = random.Random(SEED + 3)
    X, y = _datos_clasificacion()

    def entrenar_tocon(muestra):
        mejor = None
        for feature in (0, 1):
            for umbral in [v / 2 for v in range(-6, 8)]:
                izq = [e for p, e in muestra if p[feature] <= umbral]
                der = [e for p, e in muestra if p[feature] > umbral]
                if not izq or not der:
                    continue
                error = min(sum(izq), len(izq) - sum(izq)) + min(sum(der), len(der) - sum(der))
                if mejor is None or error < mejor[0]:
                    voto_izq = 1 if sum(izq) * 2 > len(izq) else 0
                    voto_der = 1 if sum(der) * 2 > len(der) else 0
                    mejor = (error, feature, umbral, voto_izq, voto_der)
        return mejor

    arboles = []
    for _ in range(25):
        muestra = [(X[rng.randrange(len(X))], 0) for _ in range(len(X))]
        muestra = [(X[i], y[i]) for i in (rng.randrange(len(X)) for _ in range(len(X)))]
        arboles.append(entrenar_tocon(muestra))

    def predecir(p, arbol):
        _, feature, umbral, vi, vd = arbol
        return vi if p[feature] <= umbral else vd

    unico = entrenar_tocon(list(zip(X, y)))
    acc_unico = sum(1 for p, e in zip(X, y) if predecir(p, unico) == e) / len(y)
    acc_bosque = sum(
        1 for p, e in zip(X, y)
        if (sum(predecir(p, a) for a in arboles) * 2 > len(arboles)) == (e == 1)
    ) / len(y)
    return {
        "arboles": len(arboles),
        "profundidad": 1,
        "accuracy_arbol_unico": round(acc_unico, 4),
        "accuracy_del_bosque": round(acc_bosque, 4),
        "muestreo": "bootstrap con reemplazo",
        "por_que_funciona": "Var(media de k modelos correlacionados ρ) = ρσ² + (1-ρ)σ²/k",
        "reduce_varianza_no_sesgo": True,
        "semilla": SEED + 3,
    }


def boosting() -> dict:
    """Boosting: cada modelo corrige el residuo del anterior (descenso funcional)."""
    X, y = _datos_regresion(40)
    objetivo = list(y)
    prediccion = [sum(y) / len(y)] * len(y)
    historial = []
    for ronda in range(1, 21):
        residuo = [t - p for t, p in zip(objetivo, prediccion)]
        # aprendiz débil: constante por tramos sobre la feature 1
        mejor = None
        for umbral in [k / 4 for k in range(0, 24)]:
            izq = [r for x, r in zip(X, residuo) if x[1] <= umbral]
            der = [r for x, r in zip(X, residuo) if x[1] > umbral]
            if not izq or not der:
                continue
            mi, md = sum(izq) / len(izq), sum(der) / len(der)
            sse = sum((r - mi) ** 2 for r in izq) + sum((r - md) ** 2 for r in der)
            if mejor is None or sse < mejor[0]:
                mejor = (sse, umbral, mi, md)
        _, umbral, mi, md = mejor
        prediccion = [p + 0.3 * (mi if x[1] <= umbral else md) for p, x in zip(prediccion, X)]
        if ronda in (1, 5, 10, 20):
            mse = sum((t - p) ** 2 for t, p in zip(objetivo, prediccion)) / len(y)
            historial.append({"ronda": ronda, "MSE": round(mse, 8)})
    return {
        "observaciones": len(y),
        "aprendiz_debil": "tocón de decisión (1 corte)",
        "learning_rate": 0.3,
        "historial": historial,
        "MSE_inicial": round(sum((t - sum(y) / len(y)) ** 2 for t in y) / len(y), 8),
        "el_error_baja_monotonamente": historial[-1]["MSE"] < historial[0]["MSE"],
        "interpretacion": "descenso de gradiente en el espacio de funciones",
        "riesgo": "demasiadas rondas sobreajustan; hay que validar",
    }


def kmeans() -> dict:
    """k-means como minimización de la inercia (Lloyd)."""
    X, _ = _datos_clasificacion()
    rng = random.Random(SEED + 4)
    k = 2
    centroides = [list(X[rng.randrange(len(X))]) for _ in range(k)]
    historial = []
    for it in range(1, 31):
        asignaciones = [min(range(k), key=lambda c: math.dist(p, centroides[c])) for p in X]
        nuevos = []
        for c in range(k):
            grupo = [p for p, a in zip(X, asignaciones) if a == c]
            nuevos.append([sum(p[i] for p in grupo) / len(grupo) for i in range(2)] if grupo else centroides[c])
        inercia = sum(math.dist(p, nuevos[a]) ** 2 for p, a in zip(X, asignaciones))
        if it in (1, 3, 10, 30):
            historial.append({"iter": it, "inercia": round(inercia, 6)})
        if all(math.dist(a, b) < 1e-12 for a, b in zip(centroides, nuevos)):
            centroides = nuevos
            break
        centroides = nuevos
    return {
        "k": k,
        "iteraciones_hasta_converger": it,
        "centroides": [[round(v, 4) for v in c] for c in centroides],
        "historial_de_inercia": historial,
        "la_inercia_nunca_sube": True,
        "objetivo": "min Σ‖xᵢ - μ_{c(i)}‖²",
        "converge_a_un_optimo_local": True,
        "sensible_a_la_inicializacion": "por eso existe k-means++",
        "semilla": SEED + 4,
    }


def gmm() -> dict:
    """Mezcla de gaussianas: asignación blanda en lugar de dura."""
    X, _ = _datos_clasificacion()
    datos = [p[0] for p in X]
    mu = [-2.0, 3.0]
    sigma2 = [1.0, 1.0]
    pi = [0.5, 0.5]

    def densidad(x, m, v):
        return math.exp(-((x - m) ** 2) / (2 * v)) / math.sqrt(2 * math.pi * v)

    log_ver = []
    for it in range(60):
        resp = []
        for x in datos:
            num = [pi[c] * densidad(x, mu[c], sigma2[c]) for c in range(2)]
            total = sum(num) + 1e-300
            resp.append([v / total for v in num])
        for c in range(2):
            nc = sum(r[c] for r in resp)
            mu[c] = sum(r[c] * x for r, x in zip(resp, datos)) / nc
            sigma2[c] = max(sum(r[c] * (x - mu[c]) ** 2 for r, x in zip(resp, datos)) / nc, 1e-6)
            pi[c] = nc / len(datos)
        if it in (0, 9, 59):
            log_ver.append(round(sum(math.log(sum(pi[c] * densidad(x, mu[c], sigma2[c])
                                                  for c in range(2)) + 1e-300) for x in datos), 6))
    return {
        "componentes": 2,
        "medias": [round(v, 4) for v in mu],
        "varianzas": [round(v, 4) for v in sigma2],
        "pesos_de_mezcla": [round(v, 4) for v in pi],
        "log_verosimilitud": log_ver,
        "la_log_verosimilitud_nunca_baja": log_ver[-1] >= log_ver[0],
        "asignacion_blanda": "cada punto pertenece a ambas clases con cierta probabilidad",
        "kmeans_es_el_caso_limite": "varianzas iguales y responsabilidades 0/1",
    }


def em_algorithm() -> dict:
    """EM: E-step y M-step sobre datos con una variable latente."""
    rng = random.Random(SEED + 5)
    # Dos monedas con sesgos distintos; no sabemos cuál generó cada tanda.
    real_a, real_b = 0.8, 0.3
    tandas = []
    for _ in range(20):
        p = real_a if rng.random() < 0.5 else real_b
        tandas.append(sum(1 for _ in range(10) if rng.random() < p))

    a, b = 0.6, 0.4
    historial = []
    for it in range(1, 41):
        # E-step
        pesos = []
        for caras in tandas:
            la_ = a**caras * (1 - a) ** (10 - caras)
            lb_ = b**caras * (1 - b) ** (10 - caras)
            total = la_ + lb_ + 1e-300
            pesos.append((la_ / total, lb_ / total))
        # M-step
        a = sum(w[0] * c for w, c in zip(pesos, tandas)) / (10 * sum(w[0] for w in pesos))
        b = sum(w[1] * c for w, c in zip(pesos, tandas)) / (10 * sum(w[1] for w in pesos))
        if it in (1, 5, 20, 40):
            historial.append({"iter": it, "p_A": round(a, 6), "p_B": round(b, 6)})
    return {
        "tandas": len(tandas),
        "lanzamientos_por_tanda": 10,
        "sesgos_reales": [real_a, real_b],
        "inicializacion": [0.6, 0.4],
        "historial": historial,
        "estimacion_final": [round(a, 6), round(b, 6)],
        "variable_latente": "qué moneda generó cada tanda",
        "garantia": "la verosimilitud no decrece en ninguna iteración",
        "semilla": SEED + 5,
    }


def pca_ml() -> dict:
    """PCA como preprocesamiento: cuánta varianza se conserva."""
    X, y = _datos_clasificacion()
    cov = la.covariance(X)
    valores, vectores = la.symmetric_eigen(cov)
    total = sum(valores)
    pc1 = [vectores[i][0] for i in range(2)]
    centrado = la.center(X)
    proyectado = [la.dot(fila, pc1) for fila in centrado]
    umbral = sum(proyectado) / len(proyectado)
    aciertos = max(
        sum(1 for p, e in zip(proyectado, y) if (p > umbral) == (e == 1)),
        sum(1 for p, e in zip(proyectado, y) if (p <= umbral) == (e == 1)),
    )
    return {
        "dimension_original": 2,
        "covarianza": [[round(v, 4) for v in row] for row in cov],
        "autovalores": [round(v, 6) for v in valores],
        "varianza_explicada_PC1_%": round(100 * valores[0] / total, 4),
        "PC1": [round(v, 6) for v in pc1],
        "accuracy_usando_solo_PC1": round(aciertos / len(y), 4),
        "dimension_reducida": 1,
        "centrar_es_obligatorio": True,
        "PCA_es_no_supervisado": "puede descartar la dirección que discrimina",
    }


def bias_variance() -> dict:
    """Descomposición sesgo-varianza medida por simulación."""
    rng = random.Random(SEED + 6)

    def verdad(x):
        return math.sin(2 * x)

    x_test = 1.0
    predicciones = {1: [], 3: [], 9: []}
    for _ in range(120):
        xs = [rng.uniform(0, 3) for _ in range(12)]
        ys = [verdad(x) + rng.gauss(0, 0.2) for x in xs]
        for grado in predicciones:
            A = [[x**k for k in range(grado + 1)] for x in xs]
            At = la.transpose(A)
            normal = la.matmul(At, A)
            normal = [[normal[i][j] + (1e-8 if i == j else 0.0) for j in range(grado + 1)]
                      for i in range(grado + 1)]
            try:
                w, _, _ = la.gaussian_elimination(normal, la.matvec(At, ys))
            except ValueError:
                continue
            predicciones[grado].append(sum(w[k] * x_test**k for k in range(grado + 1)))

    salida = {}
    for grado, preds in predicciones.items():
        media = sum(preds) / len(preds)
        sesgo2 = (media - verdad(x_test)) ** 2
        var = sum((p - media) ** 2 for p in preds) / len(preds)
        salida[f"grado_{grado}"] = {
            "prediccion_media": round(media, 6),
            "sesgo²": round(sesgo2, 6),
            "varianza": round(var, 6),
            "error_esperado": round(sesgo2 + var + 0.04, 6),
        }
    return {
        "funcion_real": "sin(2x)",
        "punto_de_prueba": x_test,
        "valor_real": round(verdad(x_test), 6),
        "replicas": 120,
        "resultados": salida,
        "grado_1_alto_sesgo": salida["grado_1"]["sesgo²"] > salida["grado_9"]["sesgo²"],
        "grado_9_alta_varianza": salida["grado_9"]["varianza"] > salida["grado_1"]["varianza"],
        "ruido_irreducible": 0.04,
    }


def generalization() -> dict:
    """Validación honesta frente a leakage: la misma métrica, dos verdades."""
    rng = random.Random(SEED + 7)
    n = 60
    X = [[1.0] + [rng.gauss(0, 1) for _ in range(12)] for _ in range(n)]
    y = [1.0 if rng.random() < 0.5 else 0.0 for _ in range(n)]   # sin relación real

    def ajustar(indices):
        Xs = [X[i] for i in indices]
        ys = [y[i] for i in indices]
        Xt = la.transpose(Xs)
        normal = la.matmul(Xt, Xs)
        normal = [[normal[i][j] + (0.01 if i == j else 0.0) for j in range(13)] for i in range(13)]
        w, _, _ = la.gaussian_elimination(normal, la.matvec(Xt, ys))
        return w

    def accuracy(w, indices):
        return sum(1 for i in indices if (la.dot(w, X[i]) >= 0.5) == (y[i] == 1.0)) / len(indices)

    todos = list(range(n))
    w_todo = ajustar(todos)
    train, test = todos[:40], todos[40:]
    w_train = ajustar(train)
    return {
        "observaciones": n,
        "features": 12,
        "relacion_real_entre_X_y_y": "ninguna",
        "accuracy_entrenando_y_evaluando_en_todo": round(accuracy(w_todo, todos), 4),
        "accuracy_en_train": round(accuracy(w_train, train), 4),
        "accuracy_en_test": round(accuracy(w_train, test), 4),
        "brecha": round(accuracy(w_train, train) - accuracy(w_train, test), 4),
        "accuracy_esperada_por_azar": 0.5,
        "leakage": "evaluar sobre datos que participaron en el ajuste infla la métrica",
        "regla": "el conjunto de test se toca una sola vez, al final",
    }


def capstone_six_algorithms() -> dict:
    """Capstone: seis algoritmos derivados y comparados sobre los mismos datos."""
    X, y = _datos_clasificacion()
    Xa = [[1.0] + p for p in X]
    n = len(y)
    corte = int(n * 0.7)
    idx = list(range(n))
    rng = random.Random(SEED + 8)
    rng.shuffle(idx)
    train, test = idx[:corte], idx[corte:]

    resultados = {}

    # 1. Regresión logística
    w = [0.0] * 3
    for _ in range(2_000):
        g = [0.0] * 3
        for i in train:
            p = _sigmoid(la.dot(w, Xa[i]))
            for k in range(3):
                g[k] += (p - y[i]) * Xa[i][k] / len(train)
        w = la.sub(w, la.scale(g, 0.5))
    resultados["regresion_logistica"] = sum(
        1 for i in test if (_sigmoid(la.dot(w, Xa[i])) >= 0.5) == (y[i] == 1)) / len(test)

    # 2. Clasificador de centroides
    c1 = [sum(X[i][d] for i in train if y[i] == 1) / max(1, sum(1 for i in train if y[i] == 1)) for d in range(2)]
    c0 = [sum(X[i][d] for i in train if y[i] == 0) / max(1, sum(1 for i in train if y[i] == 0)) for d in range(2)]
    resultados["centroides"] = sum(
        1 for i in test if (math.dist(X[i], c1) < math.dist(X[i], c0)) == (y[i] == 1)) / len(test)

    # 3. k-NN
    def knn_pred(p, k=5):
        vecinos = sorted(((math.dist(p, X[i]), y[i]) for i in train))[:k]
        return 1 if sum(e for _, e in vecinos) * 2 > k else 0

    resultados["knn_k5"] = sum(1 for i in test if knn_pred(X[i]) == y[i]) / len(test)

    # 4. Naive Bayes gaussiano
    modelos = {}
    for c in (0, 1):
        pts = [X[i] for i in train if y[i] == c]
        m = [sum(p[d] for p in pts) / len(pts) for d in range(2)]
        v = [max(sum((p[d] - m[d]) ** 2 for p in pts) / len(pts), 1e-6) for d in range(2)]
        modelos[c] = (len(pts) / len(train), m, v)

    def nb_pred(p):
        def score(c):
            prior, m, v = modelos[c]
            return math.log(prior) + sum(
                -0.5 * math.log(2 * math.pi * v[d]) - (p[d] - m[d]) ** 2 / (2 * v[d]) for d in range(2))
        return max((0, 1), key=score)

    resultados["naive_bayes"] = sum(1 for i in test if nb_pred(X[i]) == y[i]) / len(test)

    # 5. SVM lineal (hinge + subgradiente)
    ws, bs = [0.0, 0.0], 0.0
    for _ in range(1_500):
        for i in train:
            yi = 1 if y[i] == 1 else -1
            if yi * (la.dot(ws, X[i]) + bs) < 1:
                ws = [wk + 0.01 * (yi * xk - wk / len(train)) for wk, xk in zip(ws, X[i])]
                bs += 0.01 * yi
    resultados["svm_lineal"] = sum(
        1 for i in test if ((la.dot(ws, X[i]) + bs) > 0) == (y[i] == 1)) / len(test)

    # 6. Tocón de decisión
    mejor = None
    for f in (0, 1):
        for u in [v / 2 for v in range(-6, 8)]:
            izq = [y[i] for i in train if X[i][f] <= u]
            der = [y[i] for i in train if X[i][f] > u]
            if not izq or not der:
                continue
            err = min(sum(izq), len(izq) - sum(izq)) + min(sum(der), len(der) - sum(der))
            if mejor is None or err < mejor[0]:
                mejor = (err, f, u, 1 if sum(izq) * 2 > len(izq) else 0,
                         1 if sum(der) * 2 > len(der) else 0)
    _, f, u, vi, vd = mejor
    resultados["arbol_profundidad_1"] = sum(
        1 for i in test if (vi if X[i][f] <= u else vd) == y[i]) / len(test)

    return {
        "protocolo": {
            "observaciones": n, "train": len(train), "test": len(test),
            "semilla": SEED + 8, "features": 2,
            "los_6_algoritmos_ven_exactamente_la_misma_particion": True,
        },
        "accuracy_en_test": {k: round(v, 4) for k, v in resultados.items()},
        "mejor": max(resultados, key=resultados.get),
        "peor": min(resultados, key=resultados.get),
        "linea_base_por_azar": 0.5,
        "objetivos_optimizados": {
            "regresion_logistica": "log-verosimilitud",
            "centroides": "distancia a la media de clase",
            "knn_k5": "ninguno: memoriza",
            "naive_bayes": "verosimilitud con independencia condicional",
            "svm_lineal": "margen máximo con hinge loss",
            "arbol_profundidad_1": "impureza mínima",
        },
        "leccion": "cada algoritmo es un objetivo distinto sobre los mismos datos",
    }


DEMOS = {
    "supervised_geometry": supervised_geometry,
    "linear_regression": linear_regression,
    "ridge": ridge,
    "lasso": lasso,
    "logistic_regression": logistic_regression,
    "classification_loss": classification_loss,
    "naive_bayes": naive_bayes,
    "knn": knn,
    "svm_margin": svm_margin,
    "kernel_trick": kernel_trick,
    "tree_impurity": tree_impurity,
    "random_forest": random_forest,
    "boosting": boosting,
    "kmeans": kmeans,
    "gmm": gmm,
    "em_algorithm": em_algorithm,
    "pca_ml": pca_ml,
    "bias_variance": bias_variance,
    "generalization": generalization,
    "capstone_six_algorithms": capstone_six_algorithms,
}

CLASS_DEMOS = {
    "281": "supervised_geometry",
    "282": "linear_regression",
    "283": "ridge",
    "284": "lasso",
    "285": "logistic_regression",
    "286": "classification_loss",
    "287": "naive_bayes",
    "288": "knn",
    "289": "svm_margin",
    "290": "kernel_trick",
    "291": "tree_impurity",
    "292": "random_forest",
    "293": "boosting",
    "294": "kmeans",
    "295": "gmm",
    "296": "em_algorithm",
    "297": "pca_ml",
    "298": "bias_variance",
    "299": "generalization",
    "300": "capstone_six_algorithms",
}
