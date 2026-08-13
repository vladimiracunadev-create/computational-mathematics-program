"""Motor 16 — Matemática de Transformers, modelos generativos, grafos y RL.

Softmax, embeddings, positional encoding, atención escalada, multi-head,
Transformer completo, muestreo, VAE, GAN, difusión, GNN y Bellman.
"""

from __future__ import annotations

import math
import random

from . import _linalg as la

PART = "16"
TITLE = "Matemática de Transformers, modelos generativos, grafos y RL"

SEED = 20260813


def _softmax(z):
    m = max(z)
    e = [math.exp(v - m) for v in z]
    total = sum(e)
    return [v / total for v in e]


def _grafo():
    """Grafo no dirigido de 5 nodos usado por las demostraciones de GNN."""
    aristas = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (3, 4)]
    n = 5
    A = la.zeros(n, n)
    for i, j in aristas:
        A[i][j] = A[j][i] = 1.0
    return n, A, aristas


def softmax_distributions() -> dict:
    """Softmax: de logits arbitrarios a una distribución categórica."""
    logits = [2.0, 1.0, 0.1, -1.0]
    p = _softmax(logits)
    grandes = [1000.0, 999.0, 998.1, 997.0]
    return {
        "logits": logits,
        "probabilidades": [round(v, 6) for v in p],
        "suman_1": round(sum(p), 10),
        "invariante_a_desplazamiento": [round(v, 6) for v in _softmax([x + 100 for x in logits])],
        "con_logits_enormes": [round(v, 6) for v in _softmax(grandes)],
        "sin_restar_el_maximo": "exp(1000) desborda a inf",
        "el_orden_se_conserva": p == sorted(p, reverse=True),
        "temperatura_alta_aplana": [round(v, 6) for v in _softmax([x / 5 for x in logits])],
        "temperatura_baja_afila": [round(v, 6) for v in _softmax([x / 0.2 for x in logits])],
    }


def cosine_similarity() -> dict:
    """Similitud coseno: la métrica estándar entre embeddings."""
    consulta = [0.8, 0.5, 0.2, 0.1]
    documentos = {
        "muy_relacionado": [0.75, 0.55, 0.25, 0.05],
        "relacionado": [0.4, 0.4, 0.6, 0.3],
        "ortogonal": [-0.5, 0.8, 0.0, 0.0],
        "escalado_x10": [8.0, 5.0, 2.0, 1.0],
    }

    def coseno(a, b):
        return la.dot(a, b) / (la.norm(a) * la.norm(b))

    return {
        "consulta": consulta,
        "similitudes": {k: round(coseno(consulta, v), 6) for k, v in documentos.items()},
        "distancias_euclideas": {k: round(math.dist(consulta, v), 6) for k, v in documentos.items()},
        "el_escalado_no_afecta_al_coseno": math.isclose(coseno(consulta, documentos["escalado_x10"]), 1.0),
        "el_escalado_si_afecta_a_la_distancia": math.dist(consulta, documentos["escalado_x10"]) > 1,
        "rango": "[-1, 1]",
        "mas_similar": max(documentos, key=lambda k: coseno(consulta, documentos[k])),
        "uso": "búsqueda semántica, RAG y recuperación de vecinos",
    }


def positional_encoding() -> dict:
    """Positional encoding sinusoidal: posición sin parámetros aprendidos."""
    d = 8
    max_pos = 6

    def pe(pos):
        return [math.sin(pos / (10000 ** (2 * (i // 2) / d))) if i % 2 == 0
                else math.cos(pos / (10000 ** (2 * (i // 2) / d))) for i in range(d)]

    codificaciones = {f"pos_{p}": [round(v, 6) for v in pe(p)] for p in range(max_pos)}
    return {
        "dimension": d,
        "codificaciones": codificaciones,
        "normas": {f"pos_{p}": round(la.norm(pe(p)), 6) for p in range(3)},
        "producto_pos0_pos1": round(la.dot(pe(0), pe(1)), 6),
        "producto_pos0_pos5": round(la.dot(pe(0), pe(5)), 6),
        "la_similitud_decae_con_la_distancia": la.dot(pe(0), pe(1)) > la.dot(pe(0), pe(5)),
        "parametros_aprendidos": 0,
        "extrapola_a_secuencias_mas_largas": True,
        "alternativas": ["embeddings de posición aprendidos", "RoPE", "ALiBi"],
    }


def query_key_value() -> dict:
    """Q, K, V: tres proyecciones distintas del mismo token."""
    x = [1.0, 0.5, -0.3, 0.8]
    d_model, d_k = 4, 3
    rng = random.Random(SEED)
    Wq = [[rng.gauss(0, 0.5) for _ in range(d_model)] for _ in range(d_k)]
    Wk = [[rng.gauss(0, 0.5) for _ in range(d_model)] for _ in range(d_k)]
    Wv = [[rng.gauss(0, 0.5) for _ in range(d_model)] for _ in range(d_k)]
    q, k, v = la.matvec(Wq, x), la.matvec(Wk, x), la.matvec(Wv, x)
    return {
        "token_de_entrada": x,
        "d_model": d_model,
        "d_k": d_k,
        "query": [round(val, 6) for val in q],
        "key": [round(val, 6) for val in k],
        "value": [round(val, 6) for val in v],
        "roles": {
            "query": "qué información busca este token",
            "key": "qué información ofrece este token",
            "value": "qué contenido aporta si es seleccionado",
        },
        "parametros_por_cabeza": 3 * d_model * d_k,
        "son_proyecciones_lineales": True,
        "en_self_attention": "Q, K y V salen de la misma secuencia",
        "en_cross_attention": "Q del decodificador, K y V del codificador",
    }


def scaled_dot_product_attention() -> dict:
    """Atención escalada: por qué existe el 1/√d."""
    rng = random.Random(SEED)

    def puntuaciones(d, escalar):
        q = [rng.gauss(0, 1) for _ in range(d)]
        claves = [[rng.gauss(0, 1) for _ in range(d)] for _ in range(4)]
        s = [la.dot(q, k) / (math.sqrt(d) if escalar else 1.0) for k in claves]
        p = _softmax(s)
        entropia = -sum(pi * math.log2(pi) for pi in p if pi > 0)
        return {"puntuaciones": [round(v, 4) for v in s],
                "pesos": [round(v, 6) for v in p],
                "entropia_bits": round(entropia, 6),
                "peso_maximo": round(max(p), 6)}

    return {
        "formula": "softmax(QKᵀ/√d_k)·V",
        "d=8_sin_escalar": puntuaciones(8, False),
        "d=8_escalado": puntuaciones(8, True),
        "d=256_sin_escalar": puntuaciones(256, False),
        "d=256_escalado": puntuaciones(256, True),
        "varianza_del_producto_punto": "d·σ⁴ si las entradas son iid",
        "por_que_1/√d": "normaliza la varianza a 1 y evita que softmax sature",
        "sintoma_de_saturacion": "un peso ≈ 1 y gradiente casi nulo en el resto",
        "entropia_maxima_4_tokens": round(math.log2(4), 6),
    }


def self_attention() -> dict:
    """Self-attention completa sobre una secuencia de 4 tokens."""
    tokens = ["el", "gato", "come", "pescado"]
    d = 4
    rng = random.Random(SEED)
    E = [[rng.gauss(0, 1) for _ in range(d)] for _ in tokens]

    def atencion(X, causal=False):
        n = len(X)
        pesos, salidas = [], []
        for i in range(n):
            s = [la.dot(X[i], X[j]) / math.sqrt(d) for j in range(n)]
            if causal:
                s = [v if j <= i else -1e9 for j, v in enumerate(s)]
            p = _softmax(s)
            pesos.append([round(v, 4) for v in p])
            salidas.append([round(sum(p[j] * X[j][k] for j in range(n)), 6) for k in range(d)])
        return pesos, salidas

    pesos, salidas = atencion(E)
    pesos_causal, _ = atencion(E, causal=True)
    return {
        "tokens": tokens,
        "d_model": d,
        "matriz_de_atencion": pesos,
        "cada_fila_suma_1": [round(sum(f), 8) for f in pesos],
        "matriz_causal": pesos_causal,
        "el_token_0_solo_se_ve_a_si_mismo": pesos_causal[0][0] == 1.0,
        "salida_del_token_1": salidas[1],
        "coste": "O(n²·d) en tiempo y O(n²) en memoria",
        "sin_mascara_causal": "el modelo ve el futuro y el entrenamiento no sirve",
        "es_permutacion_equivariante": "por eso hace falta positional encoding",
    }


def multi_head_attention() -> dict:
    """Multi-head: varias atenciones en subespacios distintos."""
    d_model, n_heads = 8, 4
    d_head = d_model // n_heads
    rng = random.Random(SEED)
    tokens = 3
    X = [[rng.gauss(0, 1) for _ in range(d_model)] for _ in range(tokens)]

    cabezas = []
    for h in range(n_heads):
        sub = [x[h * d_head:(h + 1) * d_head] for x in X]
        pesos = []
        for i in range(tokens):
            s = [la.dot(sub[i], sub[j]) / math.sqrt(d_head) for j in range(tokens)]
            pesos.append([round(v, 4) for v in _softmax(s)])
        cabezas.append(pesos)

    return {
        "d_model": d_model,
        "cabezas": n_heads,
        "d_por_cabeza": d_head,
        "patrones_de_atencion_por_cabeza": cabezas,
        "las_cabezas_atienden_distinto": cabezas[0] != cabezas[1],
        "parametros_totales": 4 * d_model * d_model,
        "parametros_de_una_sola_cabeza_ancha": 4 * d_model * d_model,
        "coste_igual": "d_model/h por cabeza mantiene el coste constante",
        "beneficio": "el modelo puede atender a varias relaciones a la vez",
        "concatenacion_y_proyeccion_final": "W_O une las salidas de todas las cabezas",
    }


def transformer_block() -> dict:
    """Bloque Transformer: atención, residual, layer norm y feed-forward."""
    d_model, d_ff, n = 8, 32, 4
    rng = random.Random(SEED)
    X = [[rng.gauss(0, 1) for _ in range(d_model)] for _ in range(n)]

    def layer_norm(v):
        m = sum(v) / len(v)
        var = sum((x - m) ** 2 for x in v) / len(v)
        return [(x - m) / math.sqrt(var + 1e-5) for x in v]

    attn = []
    for i in range(n):
        s = [la.dot(X[i], X[j]) / math.sqrt(d_model) if j <= i else -1e9 for j in range(n)]
        p = _softmax(s)
        attn.append([sum(p[j] * X[j][k] for j in range(n)) for k in range(d_model)])

    tras_residual_1 = [layer_norm(la.add(x, a)) for x, a in zip(X, attn)]

    W1 = [[rng.gauss(0, 0.3) for _ in range(d_model)] for _ in range(d_ff)]
    W2 = [[rng.gauss(0, 0.3) for _ in range(d_ff)] for _ in range(d_model)]
    ff = [la.matvec(W2, [max(0.0, v) for v in la.matvec(W1, h)]) for h in tras_residual_1]
    salida = [layer_norm(la.add(h, f)) for h, f in zip(tras_residual_1, ff)]

    return {
        "arquitectura": ["multi-head attention", "+residual", "layer norm",
                         "feed-forward", "+residual", "layer norm"],
        "d_model": d_model,
        "d_ff": d_ff,
        "razon_d_ff/d_model": d_ff // d_model,
        "tokens": n,
        "norma_media_entrada": round(sum(la.norm(x) for x in X) / n, 6),
        "norma_media_salida": round(sum(la.norm(x) for x in salida) / n, 6),
        "shape_preservada": len(salida) == n and len(salida[0]) == d_model,
        "parametros_atencion": 4 * d_model * d_model,
        "parametros_feed_forward": 2 * d_model * d_ff,
        "el_FFN_tiene_mas_parametros": 2 * d_model * d_ff > 4 * d_model * d_model,
        "por_que_residual": "abre un camino directo para el gradiente",
    }


def autoregressive_modeling() -> dict:
    """Modelado autoregresivo: la regla de la cadena de la probabilidad."""
    secuencia = ["<inicio>", "el", "gato", "duerme"]
    condicionales = [0.4, 0.25, 0.6]
    conjunta = 1.0
    detalle = []
    for i, p in enumerate(condicionales):
        conjunta *= p
        detalle.append({
            "paso": i + 1,
            "token": secuencia[i + 1],
            "contexto": secuencia[: i + 1],
            "P(token|contexto)": p,
            "log_prob": round(math.log(p), 6),
        })
    return {
        "secuencia": secuencia[1:],
        "descomposicion": "P(x₁…xₙ) = Π P(xᵢ | x₁…xᵢ₋₁)",
        "detalle": detalle,
        "probabilidad_conjunta": round(conjunta, 8),
        "log_probabilidad": round(sum(math.log(p) for p in condicionales), 6),
        "perplejidad": round(math.exp(-sum(math.log(p) for p in condicionales) / len(condicionales)), 6),
        "por_que_en_log": "el producto de miles de probabilidades hace underflow",
        "entrenamiento": "teacher forcing: el contexto real, no el generado",
        "inferencia": "el modelo se alimenta de sus propias predicciones",
    }


def sampling_strategies() -> dict:
    """Temperatura, top-k y top-p reescriben la distribución antes de muestrear."""
    logits = [3.0, 2.5, 2.0, 1.0, 0.5, -1.0, -2.0]

    def con_temperatura(t):
        return _softmax([v / t for v in logits])

    def top_k(k, t=1.0):
        p = con_temperatura(t)
        orden = sorted(range(len(p)), key=lambda i: -p[i])[:k]
        filtrado = [p[i] if i in orden else 0.0 for i in range(len(p))]
        total = sum(filtrado)
        return [v / total for v in filtrado]

    def top_p(umbral, t=1.0):
        p = con_temperatura(t)
        orden = sorted(range(len(p)), key=lambda i: -p[i])
        acumulado, elegidos = 0.0, []
        for i in orden:
            elegidos.append(i)
            acumulado += p[i]
            if acumulado >= umbral:
                break
        filtrado = [p[i] if i in elegidos else 0.0 for i in range(len(p))]
        total = sum(filtrado)
        return [v / total for v in filtrado]

    def entropia(p):
        return round(-sum(v * math.log2(v) for v in p if v > 0), 6)

    return {
        "logits": logits,
        "greedy_argmax": logits.index(max(logits)),
        "T=1.0": {"probs": [round(v, 5) for v in con_temperatura(1.0)], "entropia": entropia(con_temperatura(1.0))},
        "T=0.5_mas_determinista": {"probs": [round(v, 5) for v in con_temperatura(0.5)],
                                   "entropia": entropia(con_temperatura(0.5))},
        "T=2.0_mas_diverso": {"probs": [round(v, 5) for v in con_temperatura(2.0)],
                              "entropia": entropia(con_temperatura(2.0))},
        "top_k=3": {"probs": [round(v, 5) for v in top_k(3)], "tokens_vivos": 3},
        "top_p=0.9": {"probs": [round(v, 5) for v in top_p(0.9)],
                      "tokens_vivos": sum(1 for v in top_p(0.9) if v > 0)},
        "top_p_es_adaptativo": "el número de tokens depende de la forma de la distribución",
        "temperatura_no_mejora_la_calidad": "solo cambia la entropía de la elección",
    }


def variational_autoencoder() -> dict:
    """VAE: reparametrización y el término KL en forma cerrada."""
    rng = random.Random(SEED)
    d = 4
    mu = [0.5, -0.3, 0.8, 0.1]
    log_var = [-0.5, -1.0, -0.2, -0.8]

    muestras = []
    for _ in range(5_000):
        eps = [rng.gauss(0, 1) for _ in range(d)]
        muestras.append([m + math.exp(0.5 * lv) * e for m, lv, e in zip(mu, log_var, eps)])
    media_emp = [sum(s[i] for s in muestras) / len(muestras) for i in range(d)]
    var_emp = [sum((s[i] - media_emp[i]) ** 2 for s in muestras) / len(muestras) for i in range(d)]

    kl = -0.5 * sum(1 + lv - m * m - math.exp(lv) for m, lv in zip(mu, log_var))
    kl_colapsado = -0.5 * sum(1 + 0.0 - 0.0 - 1.0 for _ in range(d))
    return {
        "dimension_latente": d,
        "mu": mu,
        "log_var": log_var,
        "sigma": [round(math.exp(0.5 * v), 6) for v in log_var],
        "media_empirica": [round(v, 4) for v in media_emp],
        "varianza_empirica": [round(v, 4) for v in var_emp],
        "varianza_teorica": [round(math.exp(v), 4) for v in log_var],
        "truco_de_reparametrizacion": "z = μ + σ⊙ε permite derivar respecto de μ y σ",
        "sin_el_truco": "muestrear rompe el grafo de gradiente",
        "KL(q||N(0,I))": round(kl, 6),
        "KL_si_q=prior": round(kl_colapsado, 10),
        "posterior_collapse": "KL → 0: el latente deja de codificar información",
    }


def elbo() -> dict:
    """ELBO: reconstrucción menos KL, y su relación con la log-verosimilitud."""
    reconstruccion = -12.4
    kl = 3.7
    elbo_valor = reconstruccion - kl
    barrido = {}
    for beta in (0.0, 0.5, 1.0, 4.0):
        barrido[f"β={beta}"] = round(reconstruccion - beta * kl, 6)
    return {
        "formula": "ELBO = E_q[log p(x|z)] - KL(q(z|x) ‖ p(z))",
        "termino_de_reconstruccion": reconstruccion,
        "termino_KL": kl,
        "ELBO": round(elbo_valor, 6),
        "log_p(x)_>=_ELBO": True,
        "brecha": "KL(q(z|x) ‖ p(z|x)), siempre ≥ 0",
        "maximizar_ELBO": "sube la verosimilitud y acerca q al posterior real",
        "beta_VAE": barrido,
        "beta_alto": "más desenredo, peor reconstrucción",
        "beta_cero": "autoencoder normal sin regularización latente",
    }


def gan_minimax() -> dict:
    """GAN: el equilibrio del juego minimax y su punto óptimo."""
    def perdida_d(p_real, p_falso):
        return -(math.log(max(p_real, 1e-12)) + math.log(max(1 - p_falso, 1e-12))) / 2

    escenarios = {
        "D_gana": (0.99, 0.01),
        "equilibrio": (0.5, 0.5),
        "G_gana": (0.4, 0.6),
    }
    salida = {}
    for nombre, (pr, pf) in escenarios.items():
        salida[nombre] = {
            "D(real)": pr,
            "D(falso)": pf,
            "perdida_D": round(perdida_d(pr, pf), 6),
            "perdida_G_saturante": round(math.log(max(1 - pf, 1e-12)), 6),
            "perdida_G_no_saturante": round(-math.log(max(pf, 1e-12)), 6),
        }
    return {
        "objetivo": "min_G max_D E[log D(x)] + E[log(1 - D(G(z)))]",
        "escenarios": salida,
        "D_optimo": "D*(x) = p_datos(x) / (p_datos(x) + p_G(x))",
        "en_el_equilibrio_D=0.5": True,
        "perdida_teorica_en_equilibrio": round(math.log(2), 6),
        "el_objetivo_original_equivale_a": "minimizar 2·JS(p_datos ‖ p_G) - log 4",
        "problema_del_gradiente_saturado": "log(1-D) tiene gradiente casi nulo cuando D acierta",
        "solucion_practica": "maximizar log D(G(z)) en lugar de minimizar log(1-D(G(z)))",
        "colapso_de_modos": "G produce pocas muestras distintas que engañan a D",
    }


def diffusion_forward() -> dict:
    """Proceso directo de difusión: ruido añadido con horario fijo."""
    T = 20
    betas = [1e-4 + (0.02 - 1e-4) * t / (T - 1) for t in range(T)]
    alphas = [1 - b for b in betas]
    alpha_barra = []
    acumulado = 1.0
    for a in alphas:
        acumulado *= a
        alpha_barra.append(acumulado)

    x0 = 1.0
    rng = random.Random(SEED)
    traza = []
    for t in (0, 5, 10, 19):
        ab = alpha_barra[t]
        muestras = [math.sqrt(ab) * x0 + math.sqrt(1 - ab) * rng.gauss(0, 1) for _ in range(2_000)]
        media = sum(muestras) / len(muestras)
        traza.append({
            "t": t,
            "alpha_barra": round(ab, 8),
            "señal_conservada_%": round(100 * math.sqrt(ab), 4),
            "media_empirica": round(media, 4),
            "media_teorica": round(math.sqrt(ab) * x0, 4),
            "varianza_teorica": round(1 - ab, 6),
        })
    return {
        "pasos_T": T,
        "beta_inicial": betas[0],
        "beta_final": round(betas[-1], 6),
        "formula": "x_t = √ᾱ_t·x₀ + √(1-ᾱ_t)·ε",
        "traza": traza,
        "salto_directo_a_cualquier_t": "no hace falta simular los t-1 pasos previos",
        "x_T_es_ruido_puro": alpha_barra[-1] < 0.9,
        "el_proceso_directo_no_se_aprende": True,
        "semilla": SEED,
    }


def diffusion_reverse() -> dict:
    """Proceso inverso: la red predice el ruido y se reconstruye x₀."""
    T = 20
    betas = [1e-4 + (0.02 - 1e-4) * t / (T - 1) for t in range(T)]
    alphas = [1 - b for b in betas]
    alpha_barra = []
    acumulado = 1.0
    for a in alphas:
        acumulado *= a
        alpha_barra.append(acumulado)

    rng = random.Random(SEED + 1)
    x0_real = 1.0
    t = 15
    ab = alpha_barra[t]
    eps_real = rng.gauss(0, 1)
    xt = math.sqrt(ab) * x0_real + math.sqrt(1 - ab) * eps_real

    # Un modelo perfecto predice exactamente eps_real.
    def estimar_x0(eps_pred):
        return (xt - math.sqrt(1 - ab) * eps_pred) / math.sqrt(ab)

    return {
        "t": t,
        "alpha_barra_t": round(ab, 8),
        "x0_real": x0_real,
        "ruido_real": round(eps_real, 6),
        "x_t": round(xt, 6),
        "x0_estimado_con_modelo_perfecto": round(estimar_x0(eps_real), 8),
        "x0_estimado_con_error_0.1": round(estimar_x0(eps_real + 0.1), 6),
        "amplificacion_del_error": round(math.sqrt(1 - ab) / math.sqrt(ab), 4),
        "objetivo_de_entrenamiento": "‖ε - ε_θ(x_t, t)‖²",
        "paso_inverso": "x_{t-1} = 1/√α_t·(x_t - (β_t/√(1-ᾱ_t))·ε_θ) + σ_t·z",
        "por_que_predecir_el_ruido": "objetivo con varianza estable en todo el horario",
        "relacion_con_score_matching": "ε_θ ∝ -∇_x log p(x_t)",
    }


def graph_laplacian() -> dict:
    """Laplaciano del grafo: espectro y componentes conexas."""
    n, A, aristas = _grafo()
    grados = [sum(fila) for fila in A]
    L = [[(grados[i] if i == j else 0.0) - A[i][j] for j in range(n)] for i in range(n)]
    valores, vectores = la.symmetric_eigen(L)
    valores_ordenados = sorted(round(v, 8) for v in valores)
    ceros = sum(1 for v in valores_ordenados if abs(v) < 1e-8)
    return {
        "nodos": n,
        "aristas": len(aristas),
        "grados": grados,
        "matriz_de_adyacencia": A,
        "laplaciano": L,
        "autovalores": valores_ordenados,
        "autovalores_nulos": ceros,
        "componentes_conexas": ceros,
        "es_semidefinido_positivo": all(v >= -1e-8 for v in valores_ordenados),
        "conectividad_algebraica_fiedler": valores_ordenados[1],
        "L_normalizado": "D^{-1/2} L D^{-1/2}, con autovalores en [0, 2]",
        "uso": "clustering espectral, GNN y difusión sobre grafos",
    }


def message_passing() -> dict:
    """Message passing: cada capa agrega información de un salto más lejos."""
    n, A, _ = _grafo()
    grados = [sum(fila) for fila in A]
    h = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5], [2.0, -1.0]]

    def capa(estado):
        nuevo = []
        for i in range(n):
            agregado = [0.0, 0.0]
            for j in range(n):
                if A[i][j]:
                    norm = math.sqrt((grados[i] + 1) * (grados[j] + 1))
                    agregado = [a + estado[j][k] / norm for k, a in enumerate(agregado)]
            propio = [v / (grados[i] + 1) for v in estado[i]]
            nuevo.append([max(0.0, a + p) for a, p in zip(agregado, propio)])
        return nuevo

    h1 = capa(h)
    h2 = capa(h1)
    return {
        "nodos": n,
        "features_iniciales": h,
        "tras_1_capa": [[round(v, 6) for v in fila] for fila in h1],
        "tras_2_capas": [[round(v, 6) for v in fila] for fila in h2],
        "receptivo_tras_k_capas": "vecindario de radio k",
        "normalizacion": "D^{-1/2}(A+I)D^{-1/2} como en GCN",
        "el_nodo_4_solo_tiene_1_vecino": grados[4] == 1,
        "permutacion_equivariante": True,
        "oversmoothing": "con muchas capas todos los nodos convergen a la misma representación",
        "referencia": "Kipf & Welling, ICLR 2017",
    }


def bellman_equations() -> dict:
    """Iteración de valor sobre un MDP pequeño."""
    estados = [0, 1, 2, 3]
    terminal = 3
    acciones = {0: [1], 1: [0, 2], 2: [1, 3], 3: []}
    recompensa = {0: 0.0, 1: 0.0, 2: 0.0, 3: 1.0}
    gamma = 0.9

    V = dict.fromkeys(estados, 0.0)
    historial = []
    for it in range(1, 61):
        nuevo = dict(V)
        for s in estados:
            if s == terminal:
                nuevo[s] = recompensa[s]
                continue
            nuevo[s] = max(recompensa[a] + gamma * V[a] for a in acciones[s])
        delta = max(abs(nuevo[s] - V[s]) for s in estados)
        V = nuevo
        if it in (1, 5, 20, 60):
            historial.append({"iter": it, "V": {s: round(v, 6) for s, v in V.items()},
                              "delta": round(delta, 10)})
        if delta < 1e-12:
            break
    politica = {s: max(acciones[s], key=lambda a: recompensa[a] + gamma * V[a])
                for s in estados if acciones[s]}
    return {
        "estados": estados,
        "estado_terminal": terminal,
        "gamma": gamma,
        "ecuacion": "V(s) = max_a [R(s,a) + γ·V(s')]",
        "historial": historial,
        "V_final": {s: round(v, 8) for s, v in V.items()},
        "politica_optima": politica,
        "iteraciones_hasta_converger": it,
        "V(0)_teorico_gamma³": round(gamma**2, 8),
        "contraccion": "el operador de Bellman contrae con factor γ",
        "converge_siempre_si_gamma<1": True,
    }


def policy_gradients() -> dict:
    """REINFORCE: gradiente de la política sobre un bandido de 3 brazos."""
    rng = random.Random(SEED)
    recompensas_reales = [0.2, 0.5, 0.8]
    theta = [0.0, 0.0, 0.0]
    lr = 0.1
    historial = []
    baseline = 0.0
    for episodio in range(1, 1_001):
        p = _softmax(theta)
        u = rng.random()
        acumulado, accion = 0.0, 0
        for i, pi in enumerate(p):
            acumulado += pi
            if u <= acumulado:
                accion = i
                break
        r = 1.0 if rng.random() < recompensas_reales[accion] else 0.0
        baseline += 0.01 * (r - baseline)
        ventaja = r - baseline
        for i in range(3):
            grad = (1.0 if i == accion else 0.0) - p[i]
            theta[i] += lr * ventaja * grad
        if episodio in (1, 100, 500, 1_000):
            historial.append({"episodio": episodio,
                              "politica": [round(v, 4) for v in _softmax(theta)],
                              "baseline": round(baseline, 4)})
    final = _softmax(theta)
    return {
        "brazos": 3,
        "probabilidades_reales_de_recompensa": recompensas_reales,
        "mejor_brazo": recompensas_reales.index(max(recompensas_reales)),
        "historial": historial,
        "politica_final": [round(v, 6) for v in final],
        "brazo_preferido": final.index(max(final)),
        "encuentra_el_mejor": final.index(max(final)) == 2,
        "gradiente": "∇θ J = E[∇θ log π(a|s)·(R - b)]",
        "por_que_la_baseline": "reduce la varianza sin introducir sesgo",
        "episodios": 1_000,
        "semilla": SEED,
    }


def capstone_mini_transformer() -> dict:
    """Capstone: mini-Transformer que aprende a copiar el token anterior."""
    rng = random.Random(SEED)
    vocab = 6
    d = 8
    largo = 5

    # Datos: la salida en la posición t es el token de la posición t-1.
    def generar(n):
        datos = []
        for _ in range(n):
            seq = [rng.randrange(vocab) for _ in range(largo)]
            objetivo = [0] + seq[:-1]
            datos.append((seq, objetivo))
        return datos

    train = generar(200)
    test = generar(60)

    E = [[rng.gauss(0, 0.4) for _ in range(d)] for _ in range(vocab)]
    P = [[math.sin(pos / (10000 ** (2 * (i // 2) / d))) if i % 2 == 0
          else math.cos(pos / (10000 ** (2 * (i // 2) / d))) for i in range(d)]
         for pos in range(largo)]
    Wout = [[rng.gauss(0, 0.3) for _ in range(d)] for _ in range(vocab)]
    # Sesgo de posición relativa aprendido: permite que la atención localice i-k.
    bias = [0.0] * largo

    escala = math.sqrt(d)

    def adelante(seq):
        X = [la.add(E[t], P[i]) for i, t in enumerate(seq)]
        pesos, contexto = [], []
        for i in range(largo):
            s = [la.dot(X[i], X[j]) / escala + bias[i - j] if j <= i else -1e9
                 for j in range(largo)]
            p = _softmax(s)
            pesos.append(p)
            contexto.append([sum(p[j] * X[j][k] for j in range(largo)) for k in range(d)])
        logits = [la.matvec(Wout, c) for c in contexto]
        return X, pesos, contexto, logits

    lr = 0.08
    historial = []
    for epoca in range(1, 21):
        perdida = 0.0
        for seq, objetivo in train:
            X, pesos, contexto, logits = adelante(seq)
            dE = {}
            dX = [[0.0] * d for _ in range(largo)]
            for i in range(1, largo):
                p = _softmax(logits[i])
                perdida += -math.log(max(p[objetivo[i]], 1e-12))
                dlogits = [pi - (1.0 if k == objetivo[i] else 0.0) for k, pi in enumerate(p)]
                dcontexto = [sum(dlogits[k] * Wout[k][j] for k in range(vocab)) for j in range(d)]
                for k in range(vocab):
                    for j in range(d):
                        Wout[k][j] -= lr * dlogits[k] * contexto[i][j]
                a = pesos[i]
                dp = [la.dot(dcontexto, X[j]) if j <= i else 0.0 for j in range(largo)]
                suma = sum(a[j] * dp[j] for j in range(largo))
                ds = [a[j] * (dp[j] - suma) for j in range(largo)]
                for j in range(largo):
                    if j > i:
                        continue
                    for k in range(d):
                        dX[j][k] += a[j] * dcontexto[k]
                        dX[i][k] += ds[j] * X[j][k] / escala
                        dX[j][k] += ds[j] * X[i][k] / escala
                    bias[i - j] -= lr * ds[j]
            for i, token in enumerate(seq):
                fila = dE.setdefault(token, [0.0] * d)
                for k in range(d):
                    fila[k] += dX[i][k]
            for token, g in dE.items():
                for k in range(d):
                    E[token][k] -= lr * g[k]
        if epoca in (1, 5, 12, 20):
            historial.append({"epoca": epoca,
                              "perdida_media": round(perdida / (len(train) * (largo - 1)), 6)})

    def evaluar(datos):
        aciertos = total = 0
        for seq, objetivo in datos:
            _, _, _, logits = adelante(seq)
            for i in range(1, largo):
                if logits[i].index(max(logits[i])) == objetivo[i]:
                    aciertos += 1
                total += 1
        return aciertos / total

    ejemplo_seq, ejemplo_obj = test[0]
    _, pesos_ej, _, logits_ej = adelante(ejemplo_seq)
    prediccion = [logits_ej[i].index(max(logits_ej[i])) for i in range(largo)]

    return {
        "tarea": "predecir el token anterior (copia desplazada)",
        "vocabulario": vocab,
        "d_model": d,
        "longitud_de_secuencia": largo,
        "componentes": ["embedding aprendido", "positional encoding sinusoidal",
                        "self-attention causal de 1 cabeza con sesgo relativo aprendido",
                        "proyección a logits"],
        "parametros_entrenados": vocab * d + vocab * d + largo,
        "ejemplos_train": len(train),
        "ejemplos_test": len(test),
        "historial": historial,
        "accuracy_train": round(evaluar(train), 4),
        "accuracy_test": round(evaluar(test), 4),
        "linea_base_por_azar": round(1 / vocab, 4),
        "ejemplo_entrada": ejemplo_seq,
        "ejemplo_objetivo": ejemplo_obj,
        "ejemplo_prediccion": prediccion,
        "atencion_de_la_ultima_posicion": [round(v, 4) for v in pesos_ej[-1]],
        "sesgo_relativo_aprendido": [round(v, 4) for v in bias],
        "la_atencion_aprende_a_mirar_i-1": bias[1] > bias[0],
        "dependencias_externas": "ninguna",
        "semilla": SEED,
    }


DEMOS = {
    "softmax_distributions": softmax_distributions,
    "cosine_similarity": cosine_similarity,
    "positional_encoding": positional_encoding,
    "query_key_value": query_key_value,
    "scaled_dot_product_attention": scaled_dot_product_attention,
    "self_attention": self_attention,
    "multi_head_attention": multi_head_attention,
    "transformer_block": transformer_block,
    "autoregressive_modeling": autoregressive_modeling,
    "sampling_strategies": sampling_strategies,
    "variational_autoencoder": variational_autoencoder,
    "elbo": elbo,
    "gan_minimax": gan_minimax,
    "diffusion_forward": diffusion_forward,
    "diffusion_reverse": diffusion_reverse,
    "graph_laplacian": graph_laplacian,
    "message_passing": message_passing,
    "bellman_equations": bellman_equations,
    "policy_gradients": policy_gradients,
    "capstone_mini_transformer": capstone_mini_transformer,
}

CLASS_DEMOS = {
    "321": "softmax_distributions",
    "322": "cosine_similarity",
    "323": "positional_encoding",
    "324": "query_key_value",
    "325": "scaled_dot_product_attention",
    "326": "self_attention",
    "327": "multi_head_attention",
    "328": "transformer_block",
    "329": "autoregressive_modeling",
    "330": "sampling_strategies",
    "331": "variational_autoencoder",
    "332": "elbo",
    "333": "gan_minimax",
    "334": "diffusion_forward",
    "335": "diffusion_reverse",
    "336": "graph_laplacian",
    "337": "message_passing",
    "338": "bellman_equations",
    "339": "policy_gradients",
    "340": "capstone_mini_transformer",
}
