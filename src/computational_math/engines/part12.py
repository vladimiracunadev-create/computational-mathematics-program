"""Motor 12 — Optimización matemática y computacional.

Todos los optimizadores comparten la misma función objetivo, el mismo punto
inicial y el mismo presupuesto de iteraciones: por eso son comparables.
"""

from __future__ import annotations

import math
import random

from . import _linalg as la

PART = "12"
TITLE = "Optimización matemática y computacional"

SEED = 20260813
X0 = [-2.0, 3.0]
ITERS = 200


def _rosenbrock(v):
    return (1 - v[0]) ** 2 + 100 * (v[1] - v[0] ** 2) ** 2


def _grad_rosenbrock(v):
    x, y = v
    return [-2 * (1 - x) - 400 * x * (y - x * x), 200 * (y - x * x)]


def _quad(v):
    """Cuadrática mal condicionada: f(x,y) = x² + 20y²."""
    return v[0] ** 2 + 20 * v[1] ** 2


def _grad_quad(v):
    return [2 * v[0], 40 * v[1]]


DIVERGIO = "divergió"


def _finito(valores) -> bool:
    return all(math.isfinite(v) for v in valores)


def _run(update, iters=ITERS, f=_quad, grad=_grad_quad, x0=None):
    """Ejecuta un optimizador y devuelve su traza resumida.

    Si la iteración deja de ser finita, se detiene y lo reporta explícitamente
    en lugar de propagar ``nan``: un ``nan`` silencioso es indistinguible de un
    resultado y además rompe la reproducibilidad de la comparación.
    """
    x = list(x0 if x0 is not None else X0)
    estado: dict = {}
    historial = []
    divergio_en = None
    for t in range(1, iters + 1):
        g = grad(x)
        if not _finito(g):
            divergio_en = t
            break
        x = update(x, g, t, estado)
        if not _finito(x) or abs(f(x)) > 1e100:
            divergio_en = t
            break
        if t in (1, 10, 50, iters):
            historial.append({"iter": t, "f": round(f(x), 10), "|∇f|": round(la.norm(grad(x)), 10)})
    if divergio_en is not None:
        return {"x_final": DIVERGIO, "f_final": DIVERGIO, "grad_norm_final": DIVERGIO,
                "historial": historial, "divergio_en_iteracion": divergio_en}
    return {"x_final": [round(v, 8) for v in x], "f_final": round(f(x), 12),
            "grad_norm_final": round(la.norm(grad(x)), 12), "historial": historial}


def objective_function() -> dict:
    """Anatomía de un problema de optimización."""
    return {
        "variables_de_decision": ["x", "y"],
        "funcion_objetivo": "f(x,y) = x² + 20y²",
        "sentido": "minimizar",
        "restricciones": "ninguna (problema irrestricto)",
        "f(X0)": _quad(X0),
        "gradiente_en_X0": _grad_quad(X0),
        "minimo_global": [0.0, 0.0],
        "valor_minimo": 0.0,
        "condicion_de_primer_orden": "∇f(x*) = 0",
    }


def convexity() -> dict:
    """Convexidad: la propiedad que convierte un mínimo local en global."""
    def convexa(t):
        return t * t

    def no_convexa(t):
        return t**4 - 3 * t**2 + t

    a, b, lam = -1.0, 2.0, 0.35
    punto = lam * a + (1 - lam) * b
    hess_quad = [[2.0, 0.0], [0.0, 40.0]]
    valores, _ = la.symmetric_eigen(hess_quad)
    return {
        "test_de_la_cuerda_convexa": {
            "f(λa+(1-λ)b)": convexa(punto),
            "λf(a)+(1-λ)f(b)": lam * convexa(a) + (1 - lam) * convexa(b),
            "cumple": convexa(punto) <= lam * convexa(a) + (1 - lam) * convexa(b),
        },
        "test_no_convexa": {
            "f(λa+(1-λ)b)": round(no_convexa(punto), 6),
            "λf(a)+(1-λ)f(b)": round(lam * no_convexa(a) + (1 - lam) * no_convexa(b), 6),
            "cumple": no_convexa(punto) <= lam * no_convexa(a) + (1 - lam) * no_convexa(b),
        },
        "hessiano_de_x²+20y²": hess_quad,
        "autovalores": valores,
        "definido_positivo": all(v > 0 for v in valores),
        "consecuencia": "todo mínimo local es global",
    }


def descent_directions() -> dict:
    """Cualquier dirección con dᵀ∇f < 0 hace descender la función."""
    x = list(X0)
    g = _grad_quad(x)
    direcciones = {
        "-gradiente": la.scale(g, -1),
        "coordenada_x": [-1.0, 0.0],
        "aleatoria_valida": [-1.0, -1.0],
        "ascenso": list(g),
    }
    paso = 1e-3
    salida = {}
    for nombre, d in direcciones.items():
        producto = la.dot(d, g)
        salida[nombre] = {
            "dᵀ∇f": round(producto, 6),
            "es_de_descenso": producto < 0,
            "f_tras_el_paso": round(_quad(la.add(x, la.scale(la.normalize(d), paso))), 8),
        }
    salida["f_inicial"] = _quad(x)
    salida["la_mas_empinada"] = "-∇f"
    return salida


def gradient_descent() -> dict:
    """Descenso de gradiente y el efecto del learning rate."""
    resultados = {}
    for lr in (0.001, 0.01, 0.049, 0.06):
        x = list(X0)
        divergio = False
        for _ in range(ITERS):
            x = la.sub(x, la.scale(_grad_quad(x), lr))
            if not all(math.isfinite(v) for v in x) or _quad(x) > 1e12:
                divergio = True
                break
        resultados[f"lr={lr}"] = {
            "f_final": "divergió" if divergio else round(_quad(x), 12),
            "x_final": "divergió" if divergio else [round(v, 8) for v in x],
        }
    return {
        "funcion": "x² + 20y²",
        "punto_inicial": X0,
        "iteraciones": ITERS,
        "resultados": resultados,
        "lr_maximo_estable": round(2 / 40, 6),
        "regla": "lr < 2/L donde L es el mayor autovalor del Hessiano",
    }


def sgd() -> dict:
    """SGD: gradiente ruidoso, progreso más barato."""
    rng = random.Random(SEED)
    datos = [(x / 10, 3.0 * (x / 10) + 2.0 + rng.gauss(0, 0.3)) for x in range(-50, 50)]
    w_batch = [0.0, 0.0]
    lr = 0.05
    for _ in range(200):
        gw = [0.0, 0.0]
        for xi, yi in datos:
            err = w_batch[0] + w_batch[1] * xi - yi
            gw[0] += 2 * err / len(datos)
            gw[1] += 2 * err * xi / len(datos)
        w_batch = la.sub(w_batch, la.scale(gw, lr))

    rng2 = random.Random(SEED)
    w_sgd = [0.0, 0.0]
    for epoca in range(200):
        xi, yi = datos[rng2.randrange(len(datos))]
        err = w_sgd[0] + w_sgd[1] * xi - yi
        w_sgd = la.sub(w_sgd, la.scale([2 * err, 2 * err * xi], lr))

    def mse(w):
        return sum((w[0] + w[1] * x - y) ** 2 for x, y in datos) / len(datos)

    return {
        "datos": len(datos),
        "parametros_reales": [2.0, 3.0],
        "batch_completo": [round(v, 6) for v in w_batch],
        "MSE_batch": round(mse(w_batch), 8),
        "gradientes_evaluados_batch": 200 * len(datos),
        "sgd_1_muestra": [round(v, 6) for v in w_sgd],
        "MSE_sgd": round(mse(w_sgd), 8),
        "gradientes_evaluados_sgd": 200,
        "ahorro_de_computo": len(datos),
        "el_ruido_ayuda": "puede escapar de mínimos locales poco profundos",
    }


def momentum() -> dict:
    """Momentum acumula velocidad y amortigua la oscilación."""
    def sin_momentum(x, g, t, s):
        return la.sub(x, la.scale(g, 0.02))

    def con_momentum(x, g, t, s):
        v = s.get("v", [0.0] * len(x))
        v = la.sub(la.scale(v, 0.9), la.scale(g, 0.02))
        s["v"] = v
        return la.add(x, v)

    base = _run(sin_momentum)
    mom = _run(con_momentum)
    return {
        "learning_rate": 0.02,
        "beta": 0.9,
        "sin_momentum": base,
        "con_momentum": mom,
        "momentum_llega_mas_bajo": mom["f_final"] < base["f_final"],
        "factor_de_mejora": round(base["f_final"] / max(mom["f_final"], 1e-300), 2),
        "intuicion": "una bola pesada atraviesa los valles estrechos sin rebotar",
    }


def nesterov() -> dict:
    """NAG mira adelante antes de calcular el gradiente."""
    def clasico(x, g, t, s):
        v = s.get("v", [0.0] * len(x))
        v = la.sub(la.scale(v, 0.9), la.scale(g, 0.02))
        s["v"] = v
        return la.add(x, v)

    def nag(x, g, t, s):
        v = s.get("v", [0.0] * len(x))
        adelantado = la.add(x, la.scale(v, 0.9))
        g_look = _grad_quad(adelantado)
        v = la.sub(la.scale(v, 0.9), la.scale(g_look, 0.02))
        s["v"] = v
        return la.add(x, v)

    a, b = _run(clasico), _run(nag)
    return {
        "momentum_clasico": a,
        "nesterov": b,
        "diferencia": "NAG evalúa el gradiente en x + βv, no en x",
        "nesterov_mejor": b["f_final"] <= a["f_final"],
        "ventaja_teorica": "O(1/k²) frente a O(1/k) en funciones convexas suaves",
    }


def adagrad() -> dict:
    """AdaGrad adapta el paso por coordenada, pero se apaga."""
    def update(x, g, t, s):
        acc = s.get("acc", [0.0] * len(x))
        acc = [a + gi * gi for a, gi in zip(acc, g)]
        s["acc"] = acc
        return [xi - 0.5 * gi / (math.sqrt(a) + 1e-8) for xi, gi, a in zip(x, g, acc)]

    resultado = _run(update)
    x = list(X0)
    estado: dict = {}
    pasos = []
    for t in range(1, ITERS + 1):
        g = _grad_quad(x)
        anterior = list(x)
        x = update(x, g, t, estado)
        if t in (1, 50, 200):
            pasos.append({"iter": t, "tamaño_de_paso": round(la.norm(la.sub(x, anterior)), 10)})
    return {
        "learning_rate_base": 0.5,
        "resultado": resultado,
        "tamaño_de_paso_por_iteracion": pasos,
        "el_paso_decrece_monotonamente": pasos[-1]["tamaño_de_paso"] < pasos[0]["tamaño_de_paso"],
        "problema": "el acumulador solo crece: el aprendizaje termina deteniéndose",
        "solucion": "RMSProp introduce olvido exponencial",
    }


def rmsprop() -> dict:
    """RMSProp: media móvil del gradiente al cuadrado."""
    def update(x, g, t, s):
        acc = s.get("acc", [0.0] * len(x))
        acc = [0.9 * a + 0.1 * gi * gi for a, gi in zip(acc, g)]
        s["acc"] = acc
        return [xi - 0.05 * gi / (math.sqrt(a) + 1e-8) for xi, gi, a in zip(x, g, acc)]

    def adagrad_update(x, g, t, s):
        acc = s.get("acc", [0.0] * len(x))
        acc = [a + gi * gi for a, gi in zip(acc, g)]
        s["acc"] = acc
        return [xi - 0.05 * gi / (math.sqrt(a) + 1e-8) for xi, gi, a in zip(x, g, acc)]

    r, a = _run(update), _run(adagrad_update)
    return {
        "rho": 0.9,
        "epsilon": 1e-8,
        "rmsprop": r,
        "adagrad_mismo_lr": a,
        "rmsprop_mejor": r["f_final"] < a["f_final"],
        "diferencia": "media móvil frente a suma acumulada",
        "el_paso_no_se_apaga": True,
    }


def adam() -> dict:
    """Adam: momentum de primer y segundo orden con corrección de sesgo."""
    def update(x, g, t, s):
        m = s.get("m", [0.0] * len(x))
        v = s.get("v", [0.0] * len(x))
        b1, b2, lr, eps = 0.9, 0.999, 0.1, 1e-8
        m = [b1 * mi + (1 - b1) * gi for mi, gi in zip(m, g)]
        v = [b2 * vi + (1 - b2) * gi * gi for vi, gi in zip(v, g)]
        s["m"], s["v"] = m, v
        mhat = [mi / (1 - b1**t) for mi in m]
        vhat = [vi / (1 - b2**t) for vi in v]
        return [xi - lr * mh / (math.sqrt(vh) + eps) for xi, mh, vh in zip(x, mhat, vhat)]

    resultado = _run(update)
    sin_correccion_t1 = 0.1 * (0.1 * _grad_quad(X0)[0]) / (math.sqrt(0.001 * _grad_quad(X0)[0] ** 2) + 1e-8)
    return {
        "beta1": 0.9, "beta2": 0.999, "lr": 0.1, "eps": 1e-8,
        "resultado": resultado,
        "por_que_la_correccion_de_sesgo": "m y v empiezan en 0 y subestiman los primeros pasos",
        "paso_1_sin_corregir": round(sin_correccion_t1, 8),
        "factor_de_correccion_en_t=1": round(1 / (1 - 0.9), 4),
        "es_el_optimizador_por_defecto": True,
    }


def adamw() -> dict:
    """AdamW desacopla el weight decay del gradiente adaptativo."""
    def objetivo(v):
        return (v[0] - 3.0) ** 2 + (v[1] - 4.0) ** 2

    def gradiente(v):
        return [2 * (v[0] - 3.0), 2 * (v[1] - 4.0)]

    def correr(desacoplado: bool):
        x = [0.0, 0.0]
        m = v = [0.0, 0.0]
        b1, b2, lr, wd, eps = 0.9, 0.999, 0.1, 0.05, 1e-8
        for t in range(1, 301):
            g = gradiente(x)
            if not desacoplado:      # Adam + L2 dentro del gradiente
                g = [gi + wd * xi for gi, xi in zip(g, x)]
            m = [b1 * mi + (1 - b1) * gi for mi, gi in zip(m, g)]
            v = [b2 * vi + (1 - b2) * gi * gi for vi, gi in zip(v, g)]
            mhat = [mi / (1 - b1**t) for mi in m]
            vhat = [vi / (1 - b2**t) for vi in v]
            x = [xi - lr * mh / (math.sqrt(vh) + eps) for xi, mh, vh in zip(x, mhat, vhat)]
            if desacoplado:          # AdamW: decay aplicado al parámetro
                x = [xi - lr * wd * xi for xi in x]
        return x

    adam_l2 = correr(False)
    adam_w = correr(True)
    return {
        "objetivo": "(x-3)² + (y-4)²",
        "optimo_sin_regularizacion": [3.0, 4.0],
        "weight_decay": 0.05,
        "adam_con_L2_en_el_gradiente": [round(v, 6) for v in adam_l2],
        "adamw_desacoplado": [round(v, 6) for v in adam_w],
        "norma_adam_L2": round(la.norm(adam_l2), 6),
        "norma_adamw": round(la.norm(adam_w), 6),
        "diferencia": "en Adam el decay se divide por √v; en AdamW no",
        "referencia": "Loshchilov & Hutter, ICLR 2019",
    }


def newton_method() -> dict:
    """Newton en optimización: usa curvatura, converge en un paso si es cuadrática."""
    x = list(X0)
    H = [[2.0, 0.0], [0.0, 40.0]]
    H_inv = la.inverse(H)
    historial = []
    for t in range(1, 4):
        g = _grad_quad(x)
        x = la.sub(x, la.matvec(H_inv, g))
        historial.append({"iter": t, "x": [round(v, 12) for v in x], "f": round(_quad(x), 14)})
    return {
        "funcion": "x² + 20y² (cuadrática)",
        "hessiano": H,
        "hessiano_inverso": H_inv,
        "historial": historial,
        "converge_en_1_paso": abs(historial[0]["f"]) < 1e-20,
        "coste": "O(n³) por inversión del Hessiano",
        "riesgo": "si el Hessiano no es definido positivo, el paso puede subir",
    }


def quasi_newton() -> dict:
    """BFGS: aproxima el Hessiano inverso solo con gradientes."""
    x = list(X0)
    n = len(x)
    B = la.identity(n)
    g = _grad_quad(x)
    historial = []
    for t in range(1, 31):
        d = la.scale(la.matvec(B, g), -1)
        alpha = 1.0
        for _ in range(40):        # backtracking
            if _quad(la.add(x, la.scale(d, alpha))) < _quad(x) + 1e-4 * alpha * la.dot(g, d):
                break
            alpha *= 0.5
        x_nuevo = la.add(x, la.scale(d, alpha))
        g_nuevo = _grad_quad(x_nuevo)
        s = la.sub(x_nuevo, x)
        y = la.sub(g_nuevo, g)
        sy = la.dot(s, y)
        if sy > 1e-12:
            rho = 1.0 / sy
            ident = la.identity(n)
            left = [[ident[i][j] - rho * s[i] * y[j] for j in range(n)] for i in range(n)]
            right = [[ident[i][j] - rho * y[i] * s[j] for j in range(n)] for i in range(n)]
            B = la.matmul(la.matmul(left, B), right)
            B = [[B[i][j] + rho * s[i] * s[j] for j in range(n)] for i in range(n)]
        x, g = x_nuevo, g_nuevo
        if t in (1, 5, 10, 30):
            historial.append({"iter": t, "f": round(_quad(x), 14), "|∇f|": round(la.norm(g), 12)})
        if la.norm(g) < 1e-12:
            break
    return {
        "metodo": "BFGS con búsqueda de línea por retroceso",
        "historial": historial,
        "x_final": [round(v, 10) for v in x],
        "B_aproxima_H⁻¹": [[round(v, 6) for v in row] for row in B],
        "H⁻¹_real": [[0.5, 0.0], [0.0, 0.025]],
        "no_calcula_el_hessiano": True,
        "coste": "O(n²) por iteración",
    }


def line_search() -> dict:
    """Búsqueda de línea con la condición de Armijo."""
    x = list(X0)
    g = _grad_quad(x)
    d = la.scale(g, -1)
    c1 = 1e-4
    alpha = 1.0
    intentos = []
    for _ in range(20):
        candidato = la.add(x, la.scale(d, alpha))
        cumple = _quad(candidato) <= _quad(x) + c1 * alpha * la.dot(g, d)
        intentos.append({"alpha": alpha, "f": round(_quad(candidato), 8), "armijo": cumple})
        if cumple:
            break
        alpha *= 0.5
    return {
        "punto": x,
        "f(x)": _quad(x),
        "direccion": [round(v, 4) for v in d],
        "c1": c1,
        "intentos": intentos,
        "alpha_aceptado": alpha,
        "condicion_de_Armijo": "f(x+αd) ≤ f(x) + c₁α∇fᵀd",
        "segunda_condicion_de_Wolfe": "controla que el paso no sea demasiado corto",
    }


def regularization_as_optimization() -> dict:
    """Regularizar es cambiar el objetivo, no el algoritmo."""
    datos_x = [[1.0, 0.0], [1.0, 0.1], [1.0, 0.2], [1.0, 0.3]]
    datos_y = [1.0, 1.9, 3.2, 3.9]

    def ajustar(lmbda):
        w = [0.0, 0.0]
        for _ in range(4_000):
            g = [0.0, 0.0]
            for xi, yi in zip(datos_x, datos_y):
                err = la.dot(w, xi) - yi
                g = [gk + 2 * err * xk / len(datos_y) for gk, xk in zip(g, xi)]
            g = [gk + 2 * lmbda * wk for gk, wk in zip(g, w)]
            w = la.sub(w, la.scale(g, 0.05))
        return w

    salida = {}
    for lmbda in (0.0, 0.01, 0.5):
        w = ajustar(lmbda)
        mse = sum((la.dot(w, xi) - yi) ** 2 for xi, yi in zip(datos_x, datos_y)) / len(datos_y)
        salida[f"λ={lmbda}"] = {
            "pesos": [round(v, 6) for v in w],
            "MSE": round(mse, 8),
            "norma_L2_de_w": round(la.norm(w), 6),
            "objetivo_total": round(mse + lmbda * la.dot(w, w), 8),
        }
    salida["conclusion"] = "λ mayor reduce la norma de w a costa de más error de ajuste"
    return salida


def constraints_lagrangian() -> dict:
    """Restricción de igualdad resuelta con el Lagrangiano."""
    # min x² + y² sujeto a x + y = 4  ->  x = y = 2, λ = -4... revisado: λ = 4
    x = y = 2.0
    lam = 4.0
    alternativas = {f"x={a}": a * a + (4 - a) ** 2 for a in (0.0, 1.0, 2.0, 3.0, 4.0)}
    return {
        "objetivo": "min x² + y²",
        "restriccion": "x + y = 4",
        "lagrangiano": "L = x² + y² - λ(x + y - 4)",
        "condiciones": ["2x = λ", "2y = λ", "x + y = 4"],
        "solucion": (x, y),
        "valor_optimo": x * x + y * y,
        "lambda": lam,
        "verificacion_alternativas": alternativas,
        "es_el_minimo": all(v >= x * x + y * y for v in alternativas.values()),
        "interpretacion_de_lambda": "el óptimo sube λ unidades si la restricción sube 1",
    }


def kkt_conditions() -> dict:
    """KKT: restricciones de desigualdad activas e inactivas."""
    # min (x-3)² sujeto a x <= 1  ->  la restricción está activa: x* = 1
    caso_activo = {"objetivo": "(x-3)²", "restriccion": "x ≤ 1", "x*": 1.0,
                   "gradiente_objetivo": 2 * (1.0 - 3.0), "mu": 4.0, "activa": True}
    # min (x-3)² sujeto a x <= 5  ->  inactiva: x* = 3, mu = 0
    caso_inactivo = {"objetivo": "(x-3)²", "restriccion": "x ≤ 5", "x*": 3.0,
                     "gradiente_objetivo": 0.0, "mu": 0.0, "activa": False}
    return {
        "condiciones_KKT": [
            "estacionariedad: ∇f + Σμᵢ∇gᵢ = 0",
            "factibilidad primal: gᵢ(x) ≤ 0",
            "factibilidad dual: μᵢ ≥ 0",
            "holgura complementaria: μᵢ·gᵢ(x) = 0",
        ],
        "caso_restriccion_activa": caso_activo,
        "caso_restriccion_inactiva": caso_inactivo,
        "holgura_complementaria_activo": caso_activo["mu"] * 0.0,
        "holgura_complementaria_inactivo": caso_inactivo["mu"] * (3.0 - 5.0),
        "generaliza_a_Lagrange": "con solo igualdades, KKT se reduce a Lagrange",
    }


def quadratic_programming() -> dict:
    """Programa cuadrático resuelto por su sistema KKT."""
    # min ½xᵀQx + cᵀx  sujeto a  Ax = b
    Q = [[2.0, 0.0], [0.0, 2.0]]
    c = [-2.0, -5.0]
    A = [[1.0, 1.0]]
    b = [3.0]
    # Sistema KKT: [[Q, Aᵀ], [A, 0]] [x; λ] = [-c; b]
    kkt = [
        [Q[0][0], Q[0][1], A[0][0]],
        [Q[1][0], Q[1][1], A[0][1]],
        [A[0][0], A[0][1], 0.0],
    ]
    rhs = [-c[0], -c[1], b[0]]
    sol, _, _ = la.gaussian_elimination(kkt, rhs)
    x = sol[:2]
    return {
        "Q": Q, "c": c, "A": A, "b": b,
        "Q_definida_positiva": all(v > 0 for v in la.symmetric_eigen(Q)[0]),
        "sistema_KKT": kkt,
        "solucion_x": [round(v, 10) for v in x],
        "multiplicador_lambda": round(sol[2], 10),
        "restriccion_satisfecha": round(sum(x), 10),
        "valor_objetivo": round(0.5 * la.dot(x, la.matvec(Q, x)) + la.dot(c, x), 10),
        "problema_convexo": True,
    }


def evolutionary_optimization() -> dict:
    """Optimización evolutiva: sin gradiente, sobre una función multimodal."""
    rng = random.Random(SEED)

    def f(v):
        # Rastrigin 2D: muchos mínimos locales, mínimo global en (0,0)
        return 20 + sum(xi * xi - 10 * math.cos(2 * math.pi * xi) for xi in v)

    poblacion = [[rng.uniform(-5.12, 5.12) for _ in range(2)] for _ in range(60)]
    historial = []
    for gen in range(1, 121):
        poblacion.sort(key=f)
        elite = poblacion[:12]
        nueva = list(elite)
        while len(nueva) < 60:
            p1, p2 = rng.choice(elite), rng.choice(elite)
            hijo = [(a + b) / 2 + rng.gauss(0, 0.35) for a, b in zip(p1, p2)]
            nueva.append([max(-5.12, min(5.12, v)) for v in hijo])
        poblacion = nueva
        if gen in (1, 20, 60, 120):
            historial.append({"generacion": gen, "mejor_f": round(f(min(poblacion, key=f)), 8)})
    mejor = min(poblacion, key=f)
    return {
        "funcion": "Rastrigin 2D (multimodal)",
        "poblacion": 60,
        "generaciones": 120,
        "elitismo": 12,
        "historial": historial,
        "mejor_solucion": [round(v, 6) for v in mejor],
        "mejor_valor": round(f(mejor), 8),
        "minimo_global": [0.0, 0.0],
        "sin_gradiente": True,
        "coste": "muchas evaluaciones de f; solo vale la pena si el gradiente no existe",
    }


def capstone_optimizer_bench() -> dict:
    """Capstone: banco comparable de optimizadores con presupuesto idéntico."""
    lr = 0.02

    def gd(x, g, t, s):
        return la.sub(x, la.scale(g, lr))

    def mom(x, g, t, s):
        v = s.get("v", [0.0] * len(x))
        v = la.sub(la.scale(v, 0.9), la.scale(g, lr))
        s["v"] = v
        return la.add(x, v)

    def rms(x, g, t, s):
        acc = s.get("acc", [0.0] * len(x))
        acc = [0.9 * a + 0.1 * gi * gi for a, gi in zip(acc, g)]
        s["acc"] = acc
        return [xi - lr * gi / (math.sqrt(a) + 1e-8) for xi, gi, a in zip(x, g, acc)]

    def adam_u(x, g, t, s):
        m = s.get("m", [0.0] * len(x))
        v = s.get("v", [0.0] * len(x))
        m = [0.9 * mi + 0.1 * gi for mi, gi in zip(m, g)]
        v = [0.999 * vi + 0.001 * gi * gi for vi, gi in zip(v, g)]
        s["m"], s["v"] = m, v
        mhat = [mi / (1 - 0.9**t) for mi in m]
        vhat = [vi / (1 - 0.999**t) for vi in v]
        return [xi - lr * mh / (math.sqrt(vh) + 1e-8) for xi, mh, vh in zip(x, mhat, vhat)]

    banco = {}
    for nombre, upd in (("gd", gd), ("momentum", mom), ("rmsprop", rms), ("adam", adam_u)):
        cuad = _run(upd, iters=300)
        rosen = _run(upd, iters=300, f=_rosenbrock, grad=_grad_rosenbrock, x0=[-1.2, 1.0])
        banco[nombre] = {
            "cuadratica_f_final": cuad["f_final"],
            "cuadratica_|∇f|": cuad["grad_norm_final"],
            "rosenbrock_f_final": rosen["f_final"],
            "rosenbrock_x": rosen["x_final"],
        }
    def ranking(clave):
        vivos = {k: v[clave] for k, v in banco.items() if v[clave] != DIVERGIO}
        return min(vivos, key=vivos.get) if vivos else None

    mejor_cuad = ranking("cuadratica_f_final")
    mejor_rosen = ranking("rosenbrock_f_final")
    divergieron = [k for k, v in banco.items() if v["rosenbrock_f_final"] == DIVERGIO]
    return {
        "protocolo": {
            "iteraciones": 300,
            "learning_rate": lr,
            "punto_inicial_cuadratica": X0,
            "punto_inicial_rosenbrock": [-1.2, 1.0],
            "semilla": SEED,
        },
        "banco": banco,
        "mejor_en_cuadratica": mejor_cuad,
        "mejor_en_rosenbrock": mejor_rosen,
        "divergieron_en_rosenbrock": divergieron,
        "el_mismo_lr_no_sirve_para_ambos_problemas": bool(divergieron),
        "ningun_optimizador_gana_siempre": mejor_cuad != mejor_rosen,
        "leccion": (
            "un optimizador que gana en una cuadrática bien condicionada puede "
            "divergir en un valle estrecho con el mismo learning rate"
        ),
        "condicion_de_comparabilidad": "mismo objetivo, mismo inicio, mismo presupuesto",
    }


DEMOS = {
    "objective_function": objective_function,
    "convexity": convexity,
    "descent_directions": descent_directions,
    "gradient_descent": gradient_descent,
    "sgd": sgd,
    "momentum": momentum,
    "nesterov": nesterov,
    "adagrad": adagrad,
    "rmsprop": rmsprop,
    "adam": adam,
    "adamw": adamw,
    "newton_method": newton_method,
    "quasi_newton": quasi_newton,
    "line_search": line_search,
    "regularization_as_optimization": regularization_as_optimization,
    "constraints_lagrangian": constraints_lagrangian,
    "kkt_conditions": kkt_conditions,
    "quadratic_programming": quadratic_programming,
    "evolutionary_optimization": evolutionary_optimization,
    "capstone_optimizer_bench": capstone_optimizer_bench,
}

CLASS_DEMOS = {
    "241": "objective_function",
    "242": "convexity",
    "243": "descent_directions",
    "244": "gradient_descent",
    "245": "sgd",
    "246": "momentum",
    "247": "nesterov",
    "248": "adagrad",
    "249": "rmsprop",
    "250": "adam",
    "251": "adamw",
    "252": "newton_method",
    "253": "quasi_newton",
    "254": "line_search",
    "255": "regularization_as_optimization",
    "256": "constraints_lagrangian",
    "257": "kkt_conditions",
    "258": "quadratic_programming",
    "259": "evolutionary_optimization",
    "260": "capstone_optimizer_bench",
}
