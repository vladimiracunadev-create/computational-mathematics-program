"""Motor 15 — Matemática de Deep Learning.

Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso,
inicialización, normalización, convolución, recurrencia y embeddings.
Todo en Python puro: el objetivo es que ningún paso quede oculto.
"""

from __future__ import annotations

import math
import random

from . import _linalg as la
from .part08 import Var

PART = "15"
TITLE = "Matemática de Deep Learning"

SEED = 20260813


def _sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-max(-500.0, min(500.0, z))))


def _softmax(z):
    m = max(z)
    e = [math.exp(v - m) for v in z]
    total = sum(e)
    return [v / total for v in e]


def perceptron() -> dict:
    """Perceptrón: converge si y solo si los datos son linealmente separables."""
    and_datos = [([0.0, 0.0], 0), ([0.0, 1.0], 0), ([1.0, 0.0], 0), ([1.0, 1.0], 1)]
    xor_datos = [([0.0, 0.0], 0), ([0.0, 1.0], 1), ([1.0, 0.0], 1), ([1.0, 1.0], 0)]

    def entrenar(datos, epocas=100):
        w, b = [0.0, 0.0], 0.0
        errores_finales = 0
        for _ in range(epocas):
            errores_finales = 0
            for x, t in datos:
                pred = 1 if la.dot(w, x) + b > 0 else 0
                if pred != t:
                    w = [wk + (t - pred) * xk for wk, xk in zip(w, x)]
                    b += t - pred
                    errores_finales += 1
        return w, b, errores_finales

    w_and, b_and, err_and = entrenar(and_datos)
    _, _, err_xor = entrenar(xor_datos)
    return {
        "AND_pesos": w_and,
        "AND_sesgo": b_and,
        "AND_errores_tras_100_epocas": err_and,
        "AND_es_separable": err_and == 0,
        "XOR_errores_tras_100_epocas": err_xor,
        "XOR_es_separable": err_xor == 0,
        "teorema_de_convergencia": "Rosenblatt, 1958: converge en datos separables",
        "limite_historico": "Minsky & Papert, 1969: un perceptrón no resuelve XOR",
        "solucion": "una capa oculta con no linealidad",
    }


def mlp() -> dict:
    """MLP resolviendo XOR: la capa oculta crea una representación separable."""
    rng = random.Random(SEED)
    datos = [([0.0, 0.0], 0.0), ([0.0, 1.0], 1.0), ([1.0, 0.0], 1.0), ([1.0, 1.0], 0.0)]

    W1 = [[rng.uniform(-1, 1) for _ in range(2)] for _ in range(4)]
    b1 = [0.0] * 4
    W2 = [rng.uniform(-1, 1) for _ in range(4)]
    b2 = 0.0
    lr = 0.5
    historial = []
    for epoca in range(1, 4_001):
        perdida_total = 0.0
        for x, t in datos:
            z1 = [la.dot(W1[j], x) + b1[j] for j in range(4)]
            a1 = [math.tanh(v) for v in z1]
            z2 = la.dot(W2, a1) + b2
            a2 = _sigmoid(z2)
            perdida_total += -(t * math.log(max(a2, 1e-12)) + (1 - t) * math.log(max(1 - a2, 1e-12)))
            dz2 = a2 - t
            dW2 = [dz2 * v for v in a1]
            da1 = [dz2 * W2[j] for j in range(4)]
            dz1 = [da1[j] * (1 - a1[j] ** 2) for j in range(4)]
            for j in range(4):
                for k in range(2):
                    W1[j][k] -= lr * dz1[j] * x[k]
                b1[j] -= lr * dz1[j]
            W2 = [w - lr * g for w, g in zip(W2, dW2)]
            b2 -= lr * dz2
        if epoca in (1, 100, 1_000, 4_000):
            historial.append({"epoca": epoca, "perdida": round(perdida_total / 4, 8)})

    def predecir(x):
        a1 = [math.tanh(la.dot(W1[j], x) + b1[j]) for j in range(4)]
        return _sigmoid(la.dot(W2, a1) + b2)

    return {
        "arquitectura": "2 → 4 (tanh) → 1 (sigmoid)",
        "parametros": 2 * 4 + 4 + 4 + 1,
        "historial": historial,
        "predicciones": {str(x): round(predecir(x), 6) for x, _ in datos},
        "todas_correctas": all((predecir(x) >= 0.5) == (t == 1.0) for x, t in datos),
        "sin_no_linealidad": "el modelo colapsaría a una única transformación lineal",
        "semilla": SEED,
    }


def activations() -> dict:
    """Activaciones y sus derivadas: dónde se saturan."""
    def relu(x):
        return max(0.0, x)

    def leaky(x):
        return x if x > 0 else 0.01 * x

    def gelu(x):
        return 0.5 * x * (1 + math.erf(x / math.sqrt(2)))

    puntos = [-5.0, -1.0, 0.0, 1.0, 5.0]
    h = 1e-6
    salida = {}
    for nombre, f in (("sigmoid", _sigmoid), ("tanh", math.tanh), ("relu", relu),
                      ("leaky_relu", leaky), ("gelu", gelu)):
        salida[nombre] = {
            "valores": {str(x): round(f(x), 6) for x in puntos},
            "derivada_en_-5": round((f(-5 + h) - f(-5 - h)) / (2 * h), 8),
            "derivada_en_0": round((f(0 + h) - f(0 - h)) / (2 * h), 8),
            "derivada_en_5": round((f(5 + h) - f(5 - h)) / (2 * h), 8),
        }
    return {
        **salida,
        "sigmoid_se_satura": abs(salida["sigmoid"]["derivada_en_5"]) < 1e-2,
        "relu_no_se_satura_en_positivos": abs(salida["relu"]["derivada_en_5"] - 1.0) < 1e-4,
        "relu_muere_en_negativos": abs(salida["relu"]["derivada_en_-5"]) < 1e-9,
        "por_que_relu_domina": "derivada 1 en el semieje positivo: el gradiente no se atenúa",
    }


def loss_functions() -> dict:
    """MSE, MAE, Huber y cross-entropy frente a un valor atípico."""
    y = [1.0, 2.0, 3.0, 4.0, 100.0]
    pred = [1.1, 2.1, 2.9, 4.2, 5.0]

    def huber(r, delta=1.0):
        return 0.5 * r * r if abs(r) <= delta else delta * (abs(r) - 0.5 * delta)

    residuos = [p - t for p, t in zip(pred, y)]
    return {
        "objetivos": y,
        "predicciones": pred,
        "MSE": round(sum(r * r for r in residuos) / len(y), 6),
        "MAE": round(sum(abs(r) for r in residuos) / len(y), 6),
        "Huber_delta_1": round(sum(huber(r) for r in residuos) / len(y), 6),
        "MSE_sin_el_atipico": round(sum(r * r for r in residuos[:4]) / 4, 6),
        "el_atipico_domina_el_MSE": True,
        "MAE_es_robusto": True,
        "gradiente_MSE": "2(p - y): proporcional al error",
        "gradiente_MAE": "signo(p - y): constante, no informa magnitud",
        "cuando_usar_cross_entropy": "clasificación, nunca regresión",
    }


def backpropagation() -> dict:
    """Backpropagation paso a paso sobre una red 2-2-1."""
    x = [0.5, -1.2]
    t = 1.0
    W1 = [[0.3, -0.7], [0.9, 0.2]]
    b1 = [0.1, -0.2]
    W2 = [0.6, -0.4]
    b2 = 0.05

    z1 = [la.dot(W1[j], x) + b1[j] for j in range(2)]
    a1 = [math.tanh(v) for v in z1]
    z2 = la.dot(W2, a1) + b2
    a2 = _sigmoid(z2)
    perdida = -(t * math.log(a2) + (1 - t) * math.log(1 - a2))

    dL_da2 = -(t / a2) + (1 - t) / (1 - a2)
    dL_dz2 = a2 - t                       # simplificación sigmoid + BCE
    dL_dW2 = [dL_dz2 * v for v in a1]
    dL_db2 = dL_dz2
    dL_da1 = [dL_dz2 * W2[j] for j in range(2)]
    dL_dz1 = [dL_da1[j] * (1 - a1[j] ** 2) for j in range(2)]
    dL_dW1 = [[dL_dz1[j] * x[k] for k in range(2)] for j in range(2)]

    # Verificación numérica sobre W1[0][0]
    eps = 1e-6
    W1p = [row[:] for row in W1]
    W1p[0][0] += eps
    z1p = [la.dot(W1p[j], x) + b1[j] for j in range(2)]
    a1p = [math.tanh(v) for v in z1p]
    a2p = _sigmoid(la.dot(W2, a1p) + b2)
    perdida_p = -(t * math.log(a2p) + (1 - t) * math.log(1 - a2p))
    numerico = (perdida_p - perdida) / eps

    return {
        "entrada": x,
        "objetivo": t,
        "forward": {"z1": [round(v, 6) for v in z1], "a1": [round(v, 6) for v in a1],
                    "z2": round(z2, 6), "a2": round(a2, 6), "perdida": round(perdida, 6)},
        "dL/da2": round(dL_da2, 6),
        "dL/dz2_simplificado": round(dL_dz2, 6),
        "dL/dW2": [round(v, 6) for v in dL_dW2],
        "dL/db2": round(dL_db2, 6),
        "dL/dz1": [round(v, 6) for v in dL_dz1],
        "dL/dW1": [[round(v, 6) for v in row] for row in dL_dW1],
        "gradiente_numerico_W1[0][0]": round(numerico, 6),
        "gradiente_analitico_W1[0][0]": round(dL_dW1[0][0], 6),
        "coinciden": abs(numerico - dL_dW1[0][0]) < 1e-4,
        "orden": "topológico inverso: de la pérdida hacia las entradas",
    }


def computational_graphs() -> dict:
    """El grafo de cómputo y la acumulación de gradientes en nodos reutilizados."""
    x = Var(2.0)
    y = x * x + x          # x aparece dos veces
    y.backward()

    a = Var(3.0)
    b = Var(4.0)
    c = a * b
    d = c + a
    e = d * c              # c reutilizado
    e.backward()

    return {
        "expresion_1": "y = x² + x en x=2",
        "y": y.value,
        "dy/dx": x.grad,
        "dy/dx_analitico_2x+1": 2 * 2.0 + 1,
        "acumulacion_correcta": abs(x.grad - 5.0) < 1e-12,
        "expresion_2": "e = (ab + a)·(ab) en a=3, b=4",
        "e": e.value,
        "de/da": round(a.grad, 8),
        "de/db": round(b.grad, 8),
        "nodos_con_multiples_consumidores": "sus gradientes se SUMAN, no se sobrescriben",
        "error_clasico": "olvidar zero_grad() entre pasos de entrenamiento",
    }


def weight_initialization() -> dict:
    """Xavier y He: controlar la varianza de las activaciones capa a capa."""
    rng = random.Random(SEED)
    n_in, n_out, capas = 100, 100, 8

    def propagar(escala, activacion):
        x = [rng.gauss(0, 1) for _ in range(n_in)]
        varianzas = []
        for _ in range(capas):
            W = [[rng.gauss(0, escala) for _ in range(len(x))] for _ in range(n_out)]
            z = la.matvec(W, x)
            x = [activacion(v) for v in z]
            m = sum(x) / len(x)
            varianzas.append(round(sum((v - m) ** 2 for v in x) / len(x), 8))
        return varianzas

    return {
        "capas": capas,
        "neuronas_por_capa": n_out,
        "escala_muy_pequeña_0.01_tanh": propagar(0.01, math.tanh)[:: 3],
        "xavier_tanh_(1/√n)": propagar(1 / math.sqrt(n_in), math.tanh)[:: 3],
        "he_relu_(√(2/n))": propagar(math.sqrt(2 / n_in), lambda v: max(0.0, v))[:: 3],
        "escala_muy_grande_1.0_tanh": propagar(1.0, math.tanh)[:: 3],
        "xavier": "Var(W) = 1/n_in para tanh/sigmoid",
        "he": "Var(W) = 2/n_in para ReLU (compensa que anula la mitad)",
        "inicializar_en_cero": "rompe la simetría nunca: todas las neuronas aprenden lo mismo",
        "semilla": SEED,
    }


def normalization() -> dict:
    """Batch norm y layer norm: qué eje se normaliza."""
    lote = [[10.0, 200.0, 3.0], [12.0, 190.0, 5.0], [8.0, 210.0, 1.0], [14.0, 195.0, 7.0]]

    def normalizar(valores):
        m = sum(valores) / len(valores)
        v = sum((x - m) ** 2 for x in valores) / len(valores)
        return [(x - m) / math.sqrt(v + 1e-5) for x in valores]

    batch = la.transpose([normalizar(col) for col in la.transpose(lote)])
    layer = [normalizar(fila) for fila in lote]
    return {
        "lote_original": lote,
        "escalas_por_feature": [round(max(c) - min(c), 2) for c in la.transpose(lote)],
        "batch_norm_(por_columna)": [[round(v, 4) for v in fila] for fila in batch],
        "layer_norm_(por_fila)": [[round(v, 4) for v in fila] for fila in layer],
        "media_por_columna_tras_BN": [round(sum(c) / len(c), 10) for c in la.transpose(batch)],
        "media_por_fila_tras_LN": [round(sum(f) / len(f), 10) for f in layer],
        "batch_norm_depende_del_lote": "hay que guardar estadísticas móviles para inferencia",
        "layer_norm_no_depende_del_lote": True,
        "por_que_los_Transformers_usan_LN": "secuencias de longitud variable y lotes pequeños",
        "gamma_y_beta": "parámetros aprendidos que permiten deshacer la normalización",
    }


def dropout_regularization() -> dict:
    """Dropout: ruido en entrenamiento, escalado coherente en inferencia."""
    rng = random.Random(SEED)
    activaciones = [1.0] * 100
    p = 0.5
    con_dropout = []
    for _ in range(1_000):
        salida = [(a / (1 - p)) if rng.random() > p else 0.0 for a in activaciones]
        con_dropout.append(sum(salida) / len(salida))
    media = sum(con_dropout) / len(con_dropout)
    return {
        "neuronas": len(activaciones),
        "probabilidad_de_apagado": p,
        "media_sin_dropout": 1.0,
        "media_con_inverted_dropout": round(media, 6),
        "la_esperanza_se_conserva": abs(media - 1.0) < 0.02,
        "varianza_introducida": round(sum((v - media) ** 2 for v in con_dropout) / len(con_dropout), 8),
        "en_inferencia": "dropout desactivado, sin reescalado adicional",
        "interpretacion": "entrenar un ensamble exponencial de subredes que comparten pesos",
        "no_combinar_a_ciegas_con_batchnorm": "el ruido descalibra las estadísticas del lote",
    }


def discrete_convolution() -> dict:
    """Convolución 2D con padding y stride: el cálculo de la forma de salida."""
    imagen = [
        [1.0, 2.0, 3.0, 0.0, 1.0],
        [4.0, 5.0, 6.0, 1.0, 0.0],
        [7.0, 8.0, 9.0, 2.0, 1.0],
        [1.0, 0.0, 1.0, 3.0, 2.0],
        [2.0, 1.0, 0.0, 1.0, 4.0],
    ]
    kernel = [[-1.0, 0.0, 1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]]   # Sobel horizontal

    def conv2d(img, k, stride=1):
        n, m, ks = len(img), len(img[0]), len(k)
        salida = []
        for i in range(0, n - ks + 1, stride):
            fila = []
            for j in range(0, m - ks + 1, stride):
                fila.append(sum(img[i + a][j + b] * k[a][b] for a in range(ks) for b in range(ks)))
            salida.append(fila)
        return salida

    s1 = conv2d(imagen, kernel, 1)
    s2 = conv2d(imagen, kernel, 2)
    return {
        "entrada_shape": (5, 5),
        "kernel_shape": (3, 3),
        "kernel": kernel,
        "salida_stride_1": [[round(v, 2) for v in fila] for fila in s1],
        "shape_stride_1": (len(s1), len(s1[0])),
        "shape_stride_2": (len(s2), len(s2[0])),
        "formula": "out = floor((n + 2p - k)/s) + 1",
        "verificacion_stride_1": (5 + 0 - 3) // 1 + 1,
        "parametros_del_kernel": 9,
        "parametros_de_una_densa_equivalente": 25 * 9,
        "compartir_pesos": "misma detección en cualquier posición de la imagen",
    }


def cnn_receptive_fields() -> dict:
    """Campo receptivo: cómo crece al apilar capas."""
    capas = [
        {"tipo": "conv", "k": 3, "s": 1},
        {"tipo": "conv", "k": 3, "s": 1},
        {"tipo": "pool", "k": 2, "s": 2},
        {"tipo": "conv", "k": 3, "s": 1},
        {"tipo": "conv", "k": 3, "s": 1},
    ]
    rf, salto = 1, 1
    traza = []
    for i, capa in enumerate(capas, 1):
        rf = rf + (capa["k"] - 1) * salto
        salto = salto * capa["s"]
        traza.append({"capa": i, "tipo": capa["tipo"], "campo_receptivo": rf, "salto": salto})
    return {
        "arquitectura": [f"{c['tipo']} k={c['k']} s={c['s']}" for c in capas],
        "traza": traza,
        "campo_receptivo_final": rf,
        "formula": "RF_{l} = RF_{l-1} + (k_l - 1)·Π s_i",
        "dos_conv_3x3_equivalen_a_una_5x5": True,
        "parametros_2x(3x3)": 18,
        "parametros_1x(5x5)": 25,
        "ventaja": "menos parámetros y una no linealidad extra",
    }


def pooling() -> dict:
    """Max y average pooling: reducción con y sin pérdida de posición."""
    mapa = [
        [1.0, 3.0, 2.0, 4.0],
        [5.0, 6.0, 1.0, 2.0],
        [7.0, 2.0, 8.0, 3.0],
        [1.0, 4.0, 2.0, 9.0],
    ]

    def pool(m, k, fn):
        return [[fn([m[i + a][j + b] for a in range(k) for b in range(k)])
                 for j in range(0, len(m[0]), k)] for i in range(0, len(m), k)]

    maxp = pool(mapa, 2, max)
    avgp = pool(mapa, 2, lambda v: sum(v) / len(v))
    return {
        "entrada_shape": (4, 4),
        "max_pool_2x2": maxp,
        "avg_pool_2x2": [[round(v, 4) for v in fila] for fila in avgp],
        "salida_shape": (2, 2),
        "reduccion_de_elementos": "16 → 4",
        "parametros_aprendidos": 0,
        "gradiente_del_max_pool": "solo pasa por la posición del máximo",
        "gradiente_del_avg_pool": "se reparte por igual entre las k² entradas",
        "invarianza": "pequeña a la traslación local",
    }


def rnn() -> dict:
    """RNN: el estado oculto acumula historia con pesos compartidos."""
    Wxh, Whh, bh = 0.8, 0.9, 0.05
    secuencia = [1.0, 0.5, -0.3, 0.2, 0.9]
    h = 0.0
    estados = []
    for t, x in enumerate(secuencia, 1):
        h = math.tanh(Wxh * x + Whh * h + bh)
        estados.append({"t": t, "x": x, "h": round(h, 6)})
    return {
        "secuencia": secuencia,
        "parametros": {"Wxh": Wxh, "Whh": Whh, "bh": bh},
        "estados": estados,
        "estado_final": round(h, 6),
        "pesos_compartidos_en_el_tiempo": True,
        "parametros_totales": 3,
        "longitud_de_secuencia": len(secuencia),
        "BPTT": "desenrollar en el tiempo y aplicar la regla de la cadena",
        "no_paralelizable_en_t": "cada paso depende del anterior",
    }


def vanishing_exploding() -> dict:
    """Gradientes que se desvanecen o explotan: un producto de derivadas."""
    def propagar(w, pasos=50):
        gradiente = 1.0
        traza = []
        h = 0.5
        for t in range(1, pasos + 1):
            h = math.tanh(w * h)
            gradiente *= w * (1 - h * h)
            if t in (1, 10, 25, 50):
                traza.append({"paso": t, "gradiente": gradiente})
        return traza

    return {
        "w=0.5_desvanece": propagar(0.5),
        "w=1.0_estable": propagar(1.0),
        "w=1.5_explota": propagar(1.5),
        "causa": "el gradiente en t=0 es el producto de 50 factores",
        "si_cada_factor_<1": "el producto tiende a 0 exponencialmente",
        "si_cada_factor_>1": "el producto diverge",
        "remedios": ["gradient clipping", "LSTM/GRU", "inicialización ortogonal",
                     "conexiones residuales", "normalización"],
        "por_que_las_relu_ayudan": "su derivada es exactamente 1 en el semieje positivo",
    }


def lstm() -> dict:
    """LSTM: la celda mantiene un camino aditivo para el gradiente."""
    def paso(x, h, c, params):
        f = _sigmoid(params["Wf"] * x + params["Uf"] * h + params["bf"])
        i = _sigmoid(params["Wi"] * x + params["Ui"] * h + params["bi"])
        o = _sigmoid(params["Wo"] * x + params["Uo"] * h + params["bo"])
        g = math.tanh(params["Wc"] * x + params["Uc"] * h + params["bc"])
        c = f * c + i * g
        h = o * math.tanh(c)
        return h, c, {"forget": f, "input": i, "output": o, "candidato": g}

    params = {"Wf": 0.5, "Uf": 0.5, "bf": 1.0, "Wi": 0.6, "Ui": 0.4, "bi": 0.0,
              "Wo": 0.7, "Uo": 0.3, "bo": 0.0, "Wc": 0.8, "Uc": 0.2, "bc": 0.0}
    h, c = 0.0, 0.0
    traza = []
    for t, x in enumerate([1.0, 0.0, 0.0, 0.0, 0.5], 1):
        h, c, puertas = paso(x, h, c, params)
        traza.append({"t": t, "x": x, "c": round(c, 6), "h": round(h, 6),
                      "forget": round(puertas["forget"], 4), "input": round(puertas["input"], 4)})
    return {
        "puertas": ["forget", "input", "output"],
        "traza": traza,
        "bf_inicializado_en_1": "sesgo alto en forget: la celda recuerda por defecto",
        "camino_del_gradiente": "c_t = f·c_{t-1} + i·g",
        "si_f≈1_el_gradiente_no_se_atenua": True,
        "parametros_por_celda": 12,
        "referencia": "Hochreiter & Schmidhuber, 1997",
    }


def gru() -> dict:
    """GRU: dos puertas en lugar de tres, menos parámetros."""
    def paso(x, h, p):
        z = _sigmoid(p["Wz"] * x + p["Uz"] * h + p["bz"])
        r = _sigmoid(p["Wr"] * x + p["Ur"] * h + p["br"])
        h_tilde = math.tanh(p["Wh"] * x + p["Uh"] * (r * h) + p["bh"])
        return (1 - z) * h + z * h_tilde, {"update": z, "reset": r}

    p = {"Wz": 0.5, "Uz": 0.4, "bz": 0.0, "Wr": 0.6, "Ur": 0.3, "br": 0.0,
         "Wh": 0.8, "Uh": 0.5, "bh": 0.0}
    h = 0.0
    traza = []
    for t, x in enumerate([1.0, 0.0, 0.0, 0.5], 1):
        h, puertas = paso(x, h, p)
        traza.append({"t": t, "h": round(h, 6), "update": round(puertas["update"], 4),
                      "reset": round(puertas["reset"], 4)})
    return {
        "puertas": ["update", "reset"],
        "traza": traza,
        "parametros_por_celda": 9,
        "parametros_LSTM": 12,
        "ahorro_%": round(100 * (1 - 9 / 12), 2),
        "z=0_conserva_el_estado": True,
        "z=1_lo_reemplaza": True,
        "rendimiento": "comparable a LSTM en la mayoría de tareas, con menos cómputo",
        "referencia": "Cho et al., 2014",
    }


def embeddings() -> dict:
    """Embeddings: geometría del significado y similitud coseno."""
    vocab = {
        "rey":    [0.85, 0.90, 0.10, 0.05],
        "reina":  [0.85, 0.10, 0.10, 0.05],
        "hombre": [0.20, 0.90, 0.15, 0.05],
        "mujer":  [0.20, 0.10, 0.15, 0.05],
        "mesa":   [0.05, 0.50, 0.90, 0.80],
    }

    def coseno(a, b):
        return la.dot(a, b) / (la.norm(a) * la.norm(b))

    analogia = la.add(la.sub(vocab["rey"], vocab["hombre"]), vocab["mujer"])
    ranking = sorted(((round(coseno(analogia, v), 6), k) for k, v in vocab.items()), reverse=True)
    return {
        "dimension": 4,
        "vocabulario": len(vocab),
        "similitudes_con_'rey'": {k: round(coseno(vocab["rey"], v), 6)
                                  for k, v in vocab.items() if k != "rey"},
        "mas_similar_a_rey": max((k for k in vocab if k != "rey"),
                                 key=lambda k: coseno(vocab["rey"], vocab[k])),
        "analogia_rey-hombre+mujer": [round(v, 4) for v in analogia],
        "ranking_de_la_analogia": ranking[:3],
        "one_hot_necesitaria": len(vocab),
        "embedding_denso_usa": 4,
        "por_que_coseno_y_no_distancia": "la magnitud suele codificar frecuencia, no significado",
    }


def deep_optimization() -> dict:
    """Entrenar una red profunda: learning rate, warmup y clipping."""
    rng = random.Random(SEED)

    def entrenar(lr, clip=None, warmup=0):
        w = [rng.gauss(0, 1) for _ in range(5)]
        rng2 = random.Random(SEED + 99)
        objetivo = [1.0, -1.0, 0.5, 0.0, 2.0]
        historial = []
        for paso in range(1, 301):
            lr_t = lr * min(1.0, paso / warmup) if warmup else lr
            g = [2 * (a - b) * (1 + 5 * rng2.random()) for a, b in zip(w, objetivo)]
            if clip:
                norma = la.norm(g)
                if norma > clip:
                    g = la.scale(g, clip / norma)
            w = la.sub(w, la.scale(g, lr_t))
            if paso in (10, 100, 300):
                perdida = sum((a - b) ** 2 for a, b in zip(w, objetivo))
                historial.append({"paso": paso, "perdida": round(perdida, 8) if math.isfinite(perdida) else "inf"})
        return historial

    return {
        "objetivo": "minimizar ‖w - w*‖² con gradientes ruidosos",
        "lr_alto_sin_clipping": entrenar(0.3),
        "lr_alto_con_clipping": entrenar(0.3, clip=1.0),
        "lr_moderado": entrenar(0.05),
        "lr_moderado_con_warmup": entrenar(0.05, warmup=50),
        "gradient_clipping": "acota la norma del gradiente sin cambiar su dirección",
        "warmup": "evita pasos enormes cuando las estadísticas de Adam aún son inestables",
        "scheduler": "cosine o step decay al final del entrenamiento",
        "semilla": SEED,
    }


def autodiff_frameworks() -> dict:
    """Nuestro Var frente a PyTorch/JAX: mismo principio, distinta escala."""
    x = Var(1.5)
    w = Var(0.7)
    b = Var(-0.2)
    z = (w * x + b).tanh()
    loss = (z - 1.0) ** 2
    loss.backward()

    disponible = {}
    for nombre, modulo in (("torch", "torch"), ("jax", "jax"), ("numpy", "numpy")):
        try:  # pragma: no cover - depende del entorno
            __import__(modulo)
            disponible[nombre] = True
        except ImportError:
            disponible[nombre] = False

    return {
        "expresion": "loss = (tanh(wx + b) - 1)²",
        "loss": round(loss.value, 8),
        "dloss/dw": round(w.grad, 8),
        "dloss/db": round(b.grad, 8),
        "dloss/dx": round(x.grad, 8),
        "frameworks_disponibles": disponible,
        "lo_que_añaden_los_frameworks": [
            "operaciones sobre tensores en lugar de escalares",
            "kernels en GPU/TPU",
            "fusión de operaciones y compilación (XLA, TorchInductor)",
            "modo directo y reverso, vmap, jit",
        ],
        "lo_que_no_cambia": "la regla de la cadena en orden topológico inverso",
        "este_motor_no_requiere_torch": True,
    }


def capstone_neural_network() -> dict:
    """Capstone: red neuronal completa desde cero, entrenada y evaluada."""
    rng = random.Random(SEED)

    # Datos: dos espirales entrelazadas (no linealmente separables)
    datos = []
    for clase in (0, 1):
        for i in range(60):
            r = 0.2 + 3.5 * i / 60
            t = clase * math.pi + 3.2 * i / 60 + rng.gauss(0, 0.12)
            datos.append(([r * math.sin(t), r * math.cos(t)], float(clase)))
    rng.shuffle(datos)
    corte = int(len(datos) * 0.75)
    train, test = datos[:corte], datos[corte:]

    H = 16

    def init(n_in, n_out):
        escala = math.sqrt(2.0 / n_in)
        return [[rng.gauss(0, escala) for _ in range(n_in)] for _ in range(n_out)]

    W1, b1 = init(2, H), [0.0] * H
    W2, b2 = init(H, H), [0.0] * H
    W3, b3 = init(H, 1), [0.0]

    lr = 0.08
    historial = []
    for epoca in range(1, 151):
        perdida = 0.0
        for x, t in train:
            z1 = [la.dot(W1[j], x) + b1[j] for j in range(H)]
            a1 = [max(0.0, v) for v in z1]
            z2 = [la.dot(W2[j], a1) + b2[j] for j in range(H)]
            a2 = [max(0.0, v) for v in z2]
            z3 = la.dot(W3[0], a2) + b3[0]
            p = _sigmoid(z3)
            perdida += -(t * math.log(max(p, 1e-12)) + (1 - t) * math.log(max(1 - p, 1e-12)))

            dz3 = p - t
            dW3 = [dz3 * v for v in a2]
            da2 = [dz3 * W3[0][j] for j in range(H)]
            dz2 = [da2[j] * (1.0 if z2[j] > 0 else 0.0) for j in range(H)]
            da1 = [sum(dz2[j] * W2[j][k] for j in range(H)) for k in range(H)]
            dz1 = [da1[k] * (1.0 if z1[k] > 0 else 0.0) for k in range(H)]

            for j in range(H):
                for k in range(H):
                    W2[j][k] -= lr * dz2[j] * a1[k]
                b2[j] -= lr * dz2[j]
                for k in range(2):
                    W1[j][k] -= lr * dz1[j] * x[k]
                b1[j] -= lr * dz1[j]
            W3[0] = [w - lr * g for w, g in zip(W3[0], dW3)]
            b3[0] -= lr * dz3
        if epoca in (1, 25, 75, 150):
            historial.append({"epoca": epoca, "perdida_media": round(perdida / len(train), 6)})

    def predecir(x):
        a1 = [max(0.0, la.dot(W1[j], x) + b1[j]) for j in range(H)]
        a2 = [max(0.0, la.dot(W2[j], a1) + b2[j]) for j in range(H)]
        return _sigmoid(la.dot(W3[0], a2) + b3[0])

    acc_train = sum(1 for x, t in train if (predecir(x) >= 0.5) == (t == 1.0)) / len(train)
    acc_test = sum(1 for x, t in test if (predecir(x) >= 0.5) == (t == 1.0)) / len(test)

    return {
        "problema": "dos espirales entrelazadas (no linealmente separables)",
        "arquitectura": f"2 → {H} (ReLU) → {H} (ReLU) → 1 (sigmoid)",
        "parametros": 2 * H + H + H * H + H + H + 1,
        "inicializacion": "He (√(2/n_in))",
        "optimizador": "SGD por muestra",
        "learning_rate": lr,
        "epocas": 150,
        "historial": historial,
        "accuracy_train": round(acc_train, 4),
        "accuracy_test": round(acc_test, 4),
        "brecha_train_test": round(acc_train - acc_test, 4),
        "linea_base_por_azar": 0.5,
        "dependencias_externas": "ninguna: Python estándar",
        "semilla": SEED,
    }


DEMOS = {
    "perceptron": perceptron,
    "mlp": mlp,
    "activations": activations,
    "loss_functions": loss_functions,
    "backpropagation": backpropagation,
    "computational_graphs": computational_graphs,
    "weight_initialization": weight_initialization,
    "normalization": normalization,
    "dropout_regularization": dropout_regularization,
    "discrete_convolution": discrete_convolution,
    "cnn_receptive_fields": cnn_receptive_fields,
    "pooling": pooling,
    "rnn": rnn,
    "vanishing_exploding": vanishing_exploding,
    "lstm": lstm,
    "gru": gru,
    "embeddings": embeddings,
    "deep_optimization": deep_optimization,
    "autodiff_frameworks": autodiff_frameworks,
    "capstone_neural_network": capstone_neural_network,
}

CLASS_DEMOS = {
    "301": "perceptron",
    "302": "mlp",
    "303": "activations",
    "304": "loss_functions",
    "305": "backpropagation",
    "306": "computational_graphs",
    "307": "weight_initialization",
    "308": "normalization",
    "309": "dropout_regularization",
    "310": "discrete_convolution",
    "311": "cnn_receptive_fields",
    "312": "pooling",
    "313": "rnn",
    "314": "vanishing_exploding",
    "315": "lstm",
    "316": "gru",
    "317": "embeddings",
    "318": "deep_optimization",
    "319": "autodiff_frameworks",
    "320": "capstone_neural_network",
}
