# 📡 Parte 13 — Teoría de la información, señales y series

> [⬅️ Parte 12 — Optimización matemática y computacional](../part-12-optimizacion-matematica-y-computacional/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 14 — Matemática de Machine Learning ➡️](../part-14-matematica-de-machine-learning/README.md)

**Nivel:** `avanzado` · **Clases:** 20 · **Horas estimadas:** 80 · **Motor:** [`part13.py`](../../src/computational_math/engines/part13.py)

---

## 🎯 De qué trata esta parte

Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

## 🧠 Ideas centrales

- La entropía es el límite inferior de compresión sin pérdida.
- Minimizar cross-entropy equivale a maximizar verosimilitud.
- KL no es simétrica ni es una distancia; JS sí es simétrica.
- Nyquist fija la frecuencia mínima de muestreo; por debajo hay aliasing irreversible.
- Convolución en el tiempo es multiplicación en frecuencia.

## 🤖 Por qué importa en IA

> [!IMPORTANT]
> La función de pérdida de casi todo clasificador es entropía cruzada; el VAE optimiza un ELBO con un término KL; las CNN son convoluciones aprendidas.

## ⚠️ Errores frecuentes de esta parte

- Calcular log(0) sin epsilon de estabilidad.
- Comparar entropías calculadas en bases logarítmicas distintas.
- Muestrear por debajo de Nyquist y culpar al modelo del ruido resultante.

## 🧭 Secuencia de la parte

```mermaid
flowchart LR
    subgraph B1["Bloque 1"]
        direction TB
        L261["261<br/>Información y sorpresa"]
        L262["262<br/>Entropía de Shannon"]
        L263["263<br/>Entropía cruzada"]
        L264["264<br/>Divergencia KL"]
        L265["265<br/>Jensen-Shannon<br/>divergence"]
        L261 --> L262
        L262 --> L263
        L263 --> L264
        L264 --> L265
    end
    subgraph B2["Bloque 2"]
        direction TB
        L266["266<br/>Información mutua"]
        L267["267<br/>Principio de máxima<br/>entropía"]
        L268["268<br/>Codificación y<br/>compresión"]
        L269["269<br/>Señales discretas y<br/>continuas"]
        L270["270<br/>Muestreo y aliasing"]
        L266 --> L267
        L267 --> L268
        L268 --> L269
        L269 --> L270
    end
    subgraph B3["Bloque 3"]
        direction TB
        L271["271<br/>Convolución"]
        L272["272<br/>Correlación de señales"]
        L273["273<br/>Series y transformada de<br/>Fourier"]
        L274["274<br/>FFT"]
        L275["275<br/>Filtros y respuesta en<br/>frecuencia"]
        L271 --> L272
        L272 --> L273
        L273 --> L274
        L274 --> L275
    end
    subgraph B4["Bloque 4"]
        direction TB
        L276["276<br/>Procesos estacionarios"]
        L277["277<br/>Autocorrelación"]
        L278["278<br/>Series temporales y<br/>ventanas"]
        L279["279<br/>Espectro y densidad<br/>espectral"]
        L280["280<br/>Capstone: analizar señal<br/>y construir features"]
        L276 --> L277
        L277 --> L278
        L278 --> L279
        L279 --> L280
    end
    L265 --> L266
    L270 --> L271
    L275 --> L276
```

## 📚 Las clases

| # | Clase | Demostración | Idea central |
|---|---|---|---|
| `261` | [Información y sorpresa](261-informacion-y-sorpresa/README.md) | `surprise` | La sorpresa de un evento es -log de su probabilidad. |
| `262` | [Entropía de Shannon](262-entropia-de-shannon/README.md) | `shannon_entropy` | La entropía es la sorpresa esperada y el límite de compresión. |
| `263` | [Entropía cruzada](263-entropia-cruzada/README.md) | `cross_entropy` | Entropía cruzada: el coste de codificar p con un código para q. |
| `264` | [Divergencia KL](264-divergencia-kl/README.md) | `kl_divergence` | KL: no simétrica y no es una distancia. |
| `265` | [Jensen-Shannon divergence](265-jensen-shannon-divergence/README.md) | `js_divergence` | Jensen-Shannon: simétrica y acotada. |
| `266` | [Información mutua](266-informacion-mutua/README.md) | `mutual_information` | Información mutua: cuánto reduce Y la incertidumbre de X. |
| `267` | [Principio de máxima entropía](267-principio-de-maxima-entropia/README.md) | `max_entropy` | Principio de máxima entropía: la distribución menos comprometida. |
| `268` | [Codificación y compresión](268-codificacion-y-compresion/README.md) | `coding_compression` | Código de Huffman frente a codificación de longitud fija. |
| `269` | [Señales discretas y continuas](269-senales-discretas-y-continuas/README.md) | `signals` | Señal continua muestreada: amplitud, frecuencia y fase. |
| `270` | [Muestreo y aliasing](270-muestreo-y-aliasing/README.md) | `sampling_aliasing` | Nyquist: muestrear por debajo del límite crea una señal falsa. |
| `271` | [Convolución](271-convolucion/README.md) | `convolution` | Convolución discreta: el operador de las CNN. |
| `272` | [Correlación de señales](272-correlacion-de-senales/README.md) | `cross_correlation` | Correlación cruzada: convolución sin invertir el kernel. |
| `273` | [Series y transformada de Fourier](273-series-y-transformada-de-fourier/README.md) | `fourier_series` | Descomponer una señal en senos y cosenos. |
| `274` | [FFT](274-fft/README.md) | `fft` | FFT frente a DFT: mismo resultado, coste muy distinto. |
| `275` | [Filtros y respuesta en frecuencia](275-filtros-y-respuesta-en-frecuencia/README.md) | `filters` | Filtro paso-bajo aplicado a una señal con ruido de alta frecuencia. |
| `276` | [Procesos estacionarios](276-procesos-estacionarios/README.md) | `stationarity` | Serie estacionaria frente a serie con tendencia. |
| `277` | [Autocorrelación](277-autocorrelacion/README.md) | `autocorrelation` | Autocorrelación revela la periodicidad oculta. |
| `278` | [Series temporales y ventanas](278-series-temporales-y-ventanas/README.md) | `windowing` | Ventaneo: el precio de analizar un trozo finito de señal. |
| `279` | [Espectro y densidad espectral](279-espectro-y-densidad-espectral/README.md) | `power_spectrum` | Densidad espectral de potencia y reparto de la energía. |
| `280` | [Capstone: analizar señal y construir features](280-capstone-analizar-senal-y-construir-features/README.md) | `capstone_signal_features` | Capstone: de una señal cruda a un vector de características. |

## 🧰 Stack de referencia

`math`, `cmath`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen
como contraste profesional, no como requisito.

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 13
compmath catalog --part 13
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone ([280](280-capstone-analizar-senal-y-construir-features/README.md)) | 20 % |

## 📖 Bibliografía

- Cover, T.; Thomas, J. *Elements of Information Theory*. 2ª ed., Wiley, 2006.
- MacKay, D. *Information Theory, Inference, and Learning Algorithms*. Cambridge, 2003.
- Oppenheim, A.; Schafer, R. *Discrete-Time Signal Processing*. 3ª ed., Pearson, 2009.

---

> [⬅️ Parte 12 — Optimización matemática y computacional](../part-12-optimizacion-matematica-y-computacional/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 14 — Matemática de Machine Learning ➡️](../part-14-matematica-de-machine-learning/README.md)
