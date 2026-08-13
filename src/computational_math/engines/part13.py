"""Motor 13 — Teoría de la información, señales y series.

Entropía, divergencias, información mutua, muestreo, convolución, Fourier,
FFT, filtros y análisis de series temporales.
"""

from __future__ import annotations

import cmath
import math
import random

PART = "13"
TITLE = "Teoría de la información, señales y series"

SEED = 20260813
EPS = 1e-12


def _entropia(p, base=2.0):
    return -sum(pi * math.log(pi, base) for pi in p if pi > 0)


def _dft(x):
    n = len(x)
    return [sum(x[k] * cmath.exp(-2j * math.pi * f * k / n) for k in range(n)) for f in range(n)]


def _fft(x):
    n = len(x)
    if n == 1:
        return list(x)
    if n % 2:
        return _dft(x)
    par = _fft(x[0::2])
    impar = _fft(x[1::2])
    salida = [0j] * n
    for k in range(n // 2):
        t = cmath.exp(-2j * math.pi * k / n) * impar[k]
        salida[k] = par[k] + t
        salida[k + n // 2] = par[k] - t
    return salida


def surprise() -> dict:
    """La sorpresa de un evento es -log de su probabilidad."""
    eventos = {"casi_seguro": 0.99, "frecuente": 0.5, "raro": 0.01, "rarisimo": 0.0001}
    return {
        "sorpresa_en_bits": {k: round(-math.log2(v), 6) for k, v in eventos.items()},
        "un_evento_de_p=1_no_sorprende": -math.log2(1.0),
        "aditiva_para_independientes": round(-math.log2(0.5 * 0.5), 6),
        "suma_de_sorpresas": round(-math.log2(0.5) - math.log2(0.5), 6),
        "por_que_logaritmo": "convierte productos de probabilidades en sumas de información",
        "unidad": "bits con log₂, nats con ln",
    }


def shannon_entropy() -> dict:
    """La entropía es la sorpresa esperada y el límite de compresión."""
    distribuciones = {
        "uniforme_4": [0.25] * 4,
        "sesgada": [0.7, 0.2, 0.05, 0.05],
        "determinista": [1.0, 0.0, 0.0, 0.0],
        "moneda_justa": [0.5, 0.5],
    }
    return {
        "entropias_bits": {k: round(_entropia(v), 6) for k, v in distribuciones.items()},
        "maxima_para_4_simbolos": math.log2(4),
        "la_uniforme_maximiza": _entropia(distribuciones["uniforme_4"]) == math.log2(4),
        "la_determinista_es_0": _entropia(distribuciones["determinista"]) == 0.0,
        "entropia_en_nats_uniforme": round(_entropia(distribuciones["uniforme_4"], math.e), 6),
        "interpretacion": "bits medios necesarios por símbolo en el mejor código posible",
    }


def cross_entropy() -> dict:
    """Entropía cruzada: el coste de codificar p con un código para q."""
    p = [1.0, 0.0, 0.0]           # etiqueta real (one-hot)
    modelos = {
        "muy_bueno": [0.90, 0.07, 0.03],
        "mediocre": [0.50, 0.30, 0.20],
        "malo": [0.05, 0.90, 0.05],
    }
    def ce(p, q):
        return -sum(pi * math.log(max(qi, EPS)) for pi, qi in zip(p, q))

    return {
        "etiqueta_real": p,
        "perdidas": {k: round(ce(p, q), 6) for k, q in modelos.items()},
        "prediccion_perfecta": round(ce(p, [1.0, 0.0, 0.0]), 8),
        "H(p)": round(_entropia(p, math.e), 8),
        "CE = H(p) + KL(p||q)": True,
        "por_que_hace_falta_epsilon": "log(0) es -infinito y rompe el entrenamiento",
        "es_la_perdida_de_todo_clasificador": True,
    }


def kl_divergence() -> dict:
    """KL: no simétrica y no es una distancia."""
    p = [0.5, 0.3, 0.2]
    q = [0.3, 0.4, 0.3]

    def kl(a, b):
        return sum(ai * math.log(ai / max(bi, EPS)) for ai, bi in zip(a, b) if ai > 0)

    return {
        "p": p, "q": q,
        "KL(p||q)": round(kl(p, q), 8),
        "KL(q||p)": round(kl(q, p), 8),
        "simetrica": math.isclose(kl(p, q), kl(q, p)),
        "KL(p||p)": kl(p, p),
        "siempre_no_negativa": kl(p, q) >= 0 and kl(q, p) >= 0,
        "no_cumple_desigualdad_triangular": True,
        "KL_infinita_si_q=0_donde_p>0": "por eso los VAE usan priors de soporte completo",
    }


def js_divergence() -> dict:
    """Jensen-Shannon: simétrica y acotada."""
    p = [0.5, 0.3, 0.2]
    q = [0.3, 0.4, 0.3]
    m = [(a + b) / 2 for a, b in zip(p, q)]

    def kl(a, b):
        return sum(ai * math.log2(ai / max(bi, EPS)) for ai, bi in zip(a, b) if ai > 0)

    js = 0.5 * kl(p, m) + 0.5 * kl(q, m)
    disjuntas = 0.5 * kl([1.0, 0.0], [0.5, 0.5]) + 0.5 * kl([0.0, 1.0], [0.5, 0.5])
    return {
        "p": p, "q": q,
        "mezcla_M": [round(v, 6) for v in m],
        "JS(p,q)_bits": round(js, 8),
        "JS(q,p)_bits": round(0.5 * kl(q, m) + 0.5 * kl(p, m), 8),
        "simetrica": True,
        "distribuciones_disjuntas": round(disjuntas, 8),
        "cota_superior_en_bits": 1.0,
        "sqrt(JS)_es_una_metrica": True,
    }


def mutual_information() -> dict:
    """Información mutua: cuánto reduce Y la incertidumbre de X."""
    conjunta = {(0, 0): 0.4, (0, 1): 0.1, (1, 0): 0.1, (1, 1): 0.4}
    px = {x: sum(v for (a, _), v in conjunta.items() if a == x) for x in (0, 1)}
    py = {y: sum(v for (_, b), v in conjunta.items() if b == y) for y in (0, 1)}
    mi = sum(v * math.log2(v / (px[a] * py[b])) for (a, b), v in conjunta.items() if v > 0)
    independiente = {(a, b): px[a] * py[b] for a in (0, 1) for b in (0, 1)}
    mi_indep = sum(v * math.log2(v / (px[a] * py[b])) for (a, b), v in independiente.items() if v > 0)
    return {
        "conjunta_dependiente": {str(k): v for k, v in conjunta.items()},
        "H(X)": round(_entropia(list(px.values())), 6),
        "H(Y)": round(_entropia(list(py.values())), 6),
        "I(X;Y)": round(mi, 6),
        "I_en_el_caso_independiente": round(mi_indep, 10),
        "I=0_sii_independientes": abs(mi_indep) < 1e-12,
        "I(X;Y)=H(X)-H(X|Y)": True,
        "detecta_relaciones_no_lineales": "a diferencia de la correlación de Pearson",
    }


def max_entropy() -> dict:
    """Principio de máxima entropía: la distribución menos comprometida."""
    candidatas = {
        "uniforme": [1 / 6] * 6,
        "sesgada_al_6": [0.1, 0.1, 0.1, 0.1, 0.1, 0.5],
        "casi_determinista": [0.9, 0.02, 0.02, 0.02, 0.02, 0.02],
    }
    medias = {k: sum((i + 1) * p for i, p in enumerate(v)) for k, v in candidatas.items()}
    return {
        "candidatas": {k: round(_entropia(v), 6) for k, v in candidatas.items()},
        "medias": {k: round(v, 4) for k, v in medias.items()},
        "maxima_entropia": max(candidatas, key=lambda k: _entropia(candidatas[k])),
        "entropia_maxima_teorica": round(math.log2(6), 6),
        "sin_restricciones_gana_la_uniforme": True,
        "con_media_y_varianza_fijas": "la normal maximiza la entropía",
        "con_soporte_positivo_y_media_fija": "la exponencial maximiza la entropía",
    }


def coding_compression() -> dict:
    """Código de Huffman frente a codificación de longitud fija."""
    frecuencias = {"a": 0.45, "b": 0.25, "c": 0.15, "d": 0.10, "e": 0.05}
    nodos = [(p, i, s) for i, (s, p) in enumerate(sorted(frecuencias.items()))]
    contador = len(nodos)
    codigos = dict.fromkeys(frecuencias, "")
    arbol = list(nodos)
    while len(arbol) > 1:
        arbol.sort(key=lambda t: (t[0], t[1]))
        p1, _, s1 = arbol.pop(0)
        p2, _, s2 = arbol.pop(0)
        for s in (s1 if isinstance(s1, tuple) else (s1,)):
            codigos[s] = "0" + codigos[s]
        for s in (s2 if isinstance(s2, tuple) else (s2,)):
            codigos[s] = "1" + codigos[s]
        combinado = (s1 if isinstance(s1, tuple) else (s1,)) + (s2 if isinstance(s2, tuple) else (s2,))
        arbol.append((p1 + p2, contador, combinado))
        contador += 1
    longitud_media = sum(frecuencias[s] * len(c) for s, c in codigos.items())
    entropia = _entropia(list(frecuencias.values()))
    return {
        "frecuencias": frecuencias,
        "codigos_huffman": codigos,
        "longitud_media_bits": round(longitud_media, 6),
        "entropia_bits": round(entropia, 6),
        "longitud_fija_necesaria": math.ceil(math.log2(len(frecuencias))),
        "ahorro_vs_longitud_fija_%": round(100 * (1 - longitud_media / 3), 4),
        "cumple_la_cota_de_Shannon": entropia <= longitud_media < entropia + 1,
        "codigo_libre_de_prefijos": all(
            not a.startswith(b) for a in codigos.values() for b in codigos.values() if a != b),
    }


def signals() -> dict:
    """Señal continua muestreada: amplitud, frecuencia y fase."""
    fs, dur, f0 = 100.0, 1.0, 5.0
    n = int(fs * dur)
    señal = [2.0 * math.sin(2 * math.pi * f0 * k / fs + math.pi / 4) for k in range(n)]
    return {
        "frecuencia_de_muestreo_Hz": fs,
        "duracion_s": dur,
        "muestras": n,
        "frecuencia_de_la_señal_Hz": f0,
        "amplitud": 2.0,
        "fase_rad": round(math.pi / 4, 6),
        "primeras_5_muestras": [round(v, 6) for v in señal[:5]],
        "maximo_observado": round(max(señal), 6),
        "energia": round(sum(v * v for v in señal), 6),
        "periodo_en_muestras": fs / f0,
    }


def sampling_aliasing() -> dict:
    """Nyquist: muestrear por debajo del límite crea una señal falsa."""
    fs = 20.0
    resultados = {}
    for f0 in (3.0, 9.0, 11.0, 17.0):
        muestras = [math.sin(2 * math.pi * f0 * k / fs) for k in range(20)]
        alias = abs(((f0 + fs / 2) % fs) - fs / 2)
        resultados[f"f={f0}Hz"] = {
            "cumple_nyquist": f0 < fs / 2,
            "frecuencia_aparente_Hz": round(alias, 4),
            "primeras_3_muestras": [round(v, 6) for v in muestras[:3]],
        }
    return {
        "frecuencia_de_muestreo_Hz": fs,
        "frecuencia_de_nyquist_Hz": fs / 2,
        "casos": resultados,
        "11Hz_se_ve_como_9Hz": math.isclose(resultados["f=11.0Hz"]["frecuencia_aparente_Hz"], 9.0),
        "el_aliasing_es_irreversible": True,
        "solucion": "filtro antialiasing antes del muestreo",
    }


def convolution() -> dict:
    """Convolución discreta: el operador de las CNN."""
    señal = [0.0, 1.0, 2.0, 3.0, 2.0, 1.0, 0.0]
    kernel_suavizado = [1 / 3, 1 / 3, 1 / 3]
    kernel_borde = [-1.0, 0.0, 1.0]

    def conv_valida(x, h):
        return [sum(x[i + j] * h[len(h) - 1 - j] for j in range(len(h)))
                for i in range(len(x) - len(h) + 1)]

    return {
        "señal": señal,
        "kernel_media_movil": [round(v, 4) for v in kernel_suavizado],
        "suavizada": [round(v, 6) for v in conv_valida(señal, kernel_suavizado)],
        "kernel_detector_de_bordes": kernel_borde,
        "bordes": [round(v, 6) for v in conv_valida(señal, kernel_borde)],
        "longitud_valida": len(señal) - len(kernel_suavizado) + 1,
        "longitud_completa": len(señal) + len(kernel_suavizado) - 1,
        "es_conmutativa": True,
        "en_frecuencia_es_multiplicacion": True,
    }


def cross_correlation() -> dict:
    """Correlación cruzada: convolución sin invertir el kernel."""
    patron = [1.0, 2.0, 1.0]
    señal = [0.0, 0.0, 1.0, 2.0, 1.0, 0.0, 0.5, 1.0, 0.5, 0.0]
    corr = [sum(señal[i + j] * patron[j] for j in range(len(patron)))
            for i in range(len(señal) - len(patron) + 1)]
    pico = corr.index(max(corr))
    return {
        "patron_buscado": patron,
        "señal": señal,
        "correlacion": [round(v, 4) for v in corr],
        "posicion_del_pico": pico,
        "valor_del_pico": max(corr),
        "coincidencia_exacta_en": 2,
        "convolucion_invierte_el_kernel": True,
        "las_CNN_hacen_correlacion": "aunque la llamen convolución",
        "uso": "detección de patrones, alineación y sincronización",
    }


def fourier_series() -> dict:
    """Descomponer una señal en senos y cosenos."""
    n = 64
    fs = 64.0
    señal = [3 * math.sin(2 * math.pi * 4 * k / fs) + 1.5 * math.cos(2 * math.pi * 9 * k / fs)
             for k in range(n)]
    espectro = _dft(señal)
    magnitudes = [abs(c) * 2 / n for c in espectro[: n // 2]]
    picos = sorted(range(len(magnitudes)), key=lambda i: -magnitudes[i])[:2]
    return {
        "muestras": n,
        "componentes_reales": {"4 Hz": 3.0, "9 Hz": 1.5},
        "picos_detectados_Hz": sorted(picos),
        "magnitudes_de_los_picos": [round(magnitudes[i], 6) for i in sorted(picos)],
        "energia_en_el_tiempo": round(sum(v * v for v in señal), 6),
        "energia_en_frecuencia": round(sum(abs(c) ** 2 for c in espectro) / n, 6),
        "teorema_de_Parseval": True,
        "cualquier_periodica_es_suma_de_senoidales": True,
    }


def fft() -> dict:
    """FFT frente a DFT: mismo resultado, coste muy distinto."""
    n = 256
    señal = [math.sin(2 * math.pi * 10 * k / n) + 0.5 * math.sin(2 * math.pi * 40 * k / n)
             for k in range(n)]
    rapida = _fft(señal)
    lenta = _dft(señal[:32])
    lenta_rapida = _fft(señal[:32])
    magnitudes = [abs(c) for c in rapida[: n // 2]]
    picos = sorted(range(len(magnitudes)), key=lambda i: -magnitudes[i])[:2]
    return {
        "muestras": n,
        "picos_detectados": sorted(picos),
        "frecuencias_reales": [10, 40],
        "coinciden": sorted(picos) == [10, 40],
        "fft_y_dft_coinciden": all(abs(a - b) < 1e-9 for a, b in zip(lenta, lenta_rapida)),
        "operaciones_DFT": n * n,
        "operaciones_FFT": int(n * math.log2(n)),
        "factor_de_ahorro": round(n * n / (n * math.log2(n)), 2),
        "requisito_del_algoritmo_radix2": "n potencia de 2",
    }


def filters() -> dict:
    """Filtro paso-bajo aplicado a una señal con ruido de alta frecuencia."""
    n = 128
    limpia = [math.sin(2 * math.pi * 3 * k / n) for k in range(n)]
    rng = random.Random(SEED)
    ruidosa = [v + 0.4 * math.sin(2 * math.pi * 45 * k / n) + rng.gauss(0, 0.05)
               for k, v in enumerate(limpia)]
    ventana = 7
    filtrada = []
    for i in range(n):
        lo, hi = max(0, i - ventana // 2), min(n, i + ventana // 2 + 1)
        filtrada.append(sum(ruidosa[lo:hi]) / (hi - lo))

    def error(x):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, limpia)) / n)

    return {
        "muestras": n,
        "ventana_del_filtro": ventana,
        "RMSE_antes_del_filtro": round(error(ruidosa), 6),
        "RMSE_despues_del_filtro": round(error(filtrada), 6),
        "mejora_%": round(100 * (1 - error(filtrada) / error(ruidosa)), 4),
        "tipo": "media móvil = filtro FIR paso-bajo",
        "coste": "atenúa también parte de la señal útil y desplaza la fase",
        "compromiso": "ventana mayor filtra más ruido pero difumina la señal",
    }


def stationarity() -> dict:
    """Serie estacionaria frente a serie con tendencia."""
    rng = random.Random(SEED)
    n = 400
    estacionaria = [rng.gauss(0, 1) for _ in range(n)]
    con_tendencia = [0.02 * k + rng.gauss(0, 1) for k in range(n)]

    def stats(serie):
        mitad = len(serie) // 2
        m1 = sum(serie[:mitad]) / mitad
        m2 = sum(serie[mitad:]) / (len(serie) - mitad)
        v1 = sum((x - m1) ** 2 for x in serie[:mitad]) / mitad
        v2 = sum((x - m2) ** 2 for x in serie[mitad:]) / (len(serie) - mitad)
        return {"media_1a_mitad": round(m1, 4), "media_2a_mitad": round(m2, 4),
                "varianza_1a": round(v1, 4), "varianza_2a": round(v2, 4),
                "media_estable": abs(m1 - m2) < 0.3}

    diferenciada = [con_tendencia[i] - con_tendencia[i - 1] for i in range(1, n)]
    return {
        "serie_estacionaria": stats(estacionaria),
        "serie_con_tendencia": stats(con_tendencia),
        "tras_diferenciar": stats(diferenciada),
        "diferenciar_elimina_la_tendencia_lineal": True,
        "por_que_importa": "casi todo el análisis clásico supone estacionariedad",
    }


def autocorrelation() -> dict:
    """Autocorrelación revela la periodicidad oculta."""
    n = 200
    periodo = 20
    rng = random.Random(SEED)
    serie = [math.sin(2 * math.pi * k / periodo) + rng.gauss(0, 0.2) for k in range(n)]
    media = sum(serie) / n
    denom = sum((x - media) ** 2 for x in serie)
    acf = []
    for lag in range(0, 41):
        num = sum((serie[k] - media) * (serie[k + lag] - media) for k in range(n - lag))
        acf.append(num / denom)
    pico = max(range(5, 41), key=lambda i: acf[i])
    return {
        "muestras": n,
        "periodo_real": periodo,
        "acf_lag_0": round(acf[0], 8),
        "acf_lag_5": round(acf[5], 6),
        "acf_lag_10": round(acf[10], 6),
        "acf_lag_20": round(acf[20], 6),
        "primer_pico_positivo_en_lag": pico,
        "detecta_el_periodo": abs(pico - periodo) <= 1,
        "acf_en_lag_0_siempre_es_1": math.isclose(acf[0], 1.0),
    }


def windowing() -> dict:
    """Ventaneo: el precio de analizar un trozo finito de señal."""
    n = 64
    señal = [math.sin(2 * math.pi * 8.5 * k / n) for k in range(n)]   # frecuencia no entera
    hann = [0.5 * (1 - math.cos(2 * math.pi * k / (n - 1))) for k in range(n)]
    ventaneada = [s * w for s, w in zip(señal, hann)]
    esp_rect = [abs(c) for c in _fft(señal)[: n // 2]]
    esp_hann = [abs(c) for c in _fft(ventaneada)[: n // 2]]

    def fuga(espectro, pico):
        total = sum(espectro)
        cerca = sum(espectro[max(0, pico - 1): pico + 2])
        return round(100 * (1 - cerca / total), 4)

    pico_rect = esp_rect.index(max(esp_rect))
    pico_hann = esp_hann.index(max(esp_hann))
    return {
        "muestras": n,
        "frecuencia_real": 8.5,
        "pico_con_ventana_rectangular": pico_rect,
        "pico_con_ventana_de_Hann": pico_hann,
        "fuga_espectral_rectangular_%": fuga(esp_rect, pico_rect),
        "fuga_espectral_hann_%": fuga(esp_hann, pico_hann),
        "hann_reduce_la_fuga": fuga(esp_hann, pico_hann) < fuga(esp_rect, pico_rect),
        "coste": "el lóbulo principal se ensancha: menos resolución en frecuencia",
    }


def power_spectrum() -> dict:
    """Densidad espectral de potencia y reparto de la energía."""
    n = 128
    señal = [2.0 * math.sin(2 * math.pi * 5 * k / n) + 1.0 * math.sin(2 * math.pi * 20 * k / n)
             for k in range(n)]
    espectro = _fft(señal)
    psd = [abs(c) ** 2 / n for c in espectro[: n // 2]]
    total = sum(psd)
    orden = sorted(range(len(psd)), key=lambda i: -psd[i])[:2]
    return {
        "muestras": n,
        "componentes": {"5 Hz": 2.0, "20 Hz": 1.0},
        "bins_dominantes": sorted(orden),
        "potencia_relativa_5Hz_%": round(100 * psd[5] / total, 4),
        "potencia_relativa_20Hz_%": round(100 * psd[20] / total, 4),
        "razon_de_potencias": round(psd[5] / psd[20], 4),
        "razon_teorica_amplitudes²": (2.0 / 1.0) ** 2,
        "energia_total_tiempo": round(sum(v * v for v in señal), 4),
        "energia_total_frecuencia": round(sum(abs(c) ** 2 for c in espectro) / n, 4),
    }


def capstone_signal_features() -> dict:
    """Capstone: de una señal cruda a un vector de características."""
    rng = random.Random(SEED)
    n = 256
    fs = 256.0
    señal = [1.5 * math.sin(2 * math.pi * 7 * k / fs)
             + 0.6 * math.sin(2 * math.pi * 23 * k / fs)
             + rng.gauss(0, 0.15) for k in range(n)]

    media = sum(señal) / n
    var = sum((x - media) ** 2 for x in señal) / n
    rms = math.sqrt(sum(x * x for x in señal) / n)
    cruces = sum(1 for i in range(1, n) if (señal[i - 1] < 0) != (señal[i] < 0))

    espectro = _fft(señal)
    psd = [abs(c) ** 2 / n for c in espectro[: n // 2]]
    total = sum(psd)
    centroide = sum(i * p for i, p in enumerate(psd)) / total
    prob = [p / total for p in psd]
    entropia_espectral = _entropia(prob)
    dominante = psd.index(max(psd))

    return {
        "muestras": n,
        "frecuencia_de_muestreo_Hz": fs,
        "features_temporales": {
            "media": round(media, 6),
            "varianza": round(var, 6),
            "RMS": round(rms, 6),
            "cruces_por_cero": cruces,
            "rango": round(max(señal) - min(señal), 6),
        },
        "features_espectrales": {
            "frecuencia_dominante_Hz": dominante,
            "centroide_espectral": round(centroide, 6),
            "entropia_espectral_bits": round(entropia_espectral, 6),
            "entropia_maxima_posible": round(math.log2(len(psd)), 6),
            "planitud_relativa": round(entropia_espectral / math.log2(len(psd)), 6),
        },
        "componentes_reales_Hz": [7, 23],
        "dominante_detectada_correctamente": dominante == 7,
        "vector_de_features": 10,
        "uso": "entrada de un clasificador de audio, vibración o biomédica",
    }


DEMOS = {
    "surprise": surprise,
    "shannon_entropy": shannon_entropy,
    "cross_entropy": cross_entropy,
    "kl_divergence": kl_divergence,
    "js_divergence": js_divergence,
    "mutual_information": mutual_information,
    "max_entropy": max_entropy,
    "coding_compression": coding_compression,
    "signals": signals,
    "sampling_aliasing": sampling_aliasing,
    "convolution": convolution,
    "cross_correlation": cross_correlation,
    "fourier_series": fourier_series,
    "fft": fft,
    "filters": filters,
    "stationarity": stationarity,
    "autocorrelation": autocorrelation,
    "windowing": windowing,
    "power_spectrum": power_spectrum,
    "capstone_signal_features": capstone_signal_features,
}

CLASS_DEMOS = {
    "261": "surprise",
    "262": "shannon_entropy",
    "263": "cross_entropy",
    "264": "kl_divergence",
    "265": "js_divergence",
    "266": "mutual_information",
    "267": "max_entropy",
    "268": "coding_compression",
    "269": "signals",
    "270": "sampling_aliasing",
    "271": "convolution",
    "272": "cross_correlation",
    "273": "fourier_series",
    "274": "fft",
    "275": "filters",
    "276": "stationarity",
    "277": "autocorrelation",
    "278": "windowing",
    "279": "power_spectrum",
    "280": "capstone_signal_features",
}
