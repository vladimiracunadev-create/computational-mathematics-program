# 🧠 Parte 15 — Matemática de Deep Learning

> [⬅️ Parte 14 — Matemática de Machine Learning](../part-14-matematica-de-machine-learning/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 16 — Matemática de Transformers, modelos generativos, grafos y RL ➡️](../part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/README.md)

**Nivel:** `deep-learning` · **Clases:** 20 · **Horas estimadas:** 80 · **Motor:** [`part15.py`](../../src/computational_math/engines/part15.py)

---

## 🎯 De qué trata esta parte

Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso, grafos de cómputo, inicialización, normalización, convolución, recurrencia y embeddings.

## 🧠 Ideas centrales

- Backpropagation es la regla de la cadena aplicada en orden topológico inverso.
- Sin no linealidad, apilar capas sigue siendo una única transformación lineal.
- La inicialización controla la varianza de las activaciones y de los gradientes.
- Normalizar estabiliza la escala interna y permite tasas de aprendizaje mayores.
- El gradiente que se desvanece es un producto de derivadas menores que uno.

## 🤖 Por qué importa en IA

> [!IMPORTANT]
> Toda arquitectura moderna, incluido el Transformer, se construye sobre estos bloques y sobre este mismo mecanismo de derivación.

## ⚠️ Errores frecuentes de esta parte

- Inicializar todos los pesos iguales y romper la simetría nunca.
- Aplicar softmax sin restar el máximo y provocar overflow.
- Mezclar estadísticas de batch normalization entre entrenamiento e inferencia.

## 🧭 Secuencia de la parte

```mermaid
flowchart LR
    subgraph B1["Bloque 1"]
        direction TB
        L301["301 · Perceptrón y separabilidad"]
        L302["302 · MLP como composición de…"]
        L303["303 · Funciones de activación"]
        L304["304 · Funciones de pérdida"]
        L305["305 · Backpropagation paso a paso"]
        L301 --> L302
        L302 --> L303
        L303 --> L304
        L304 --> L305
    end
    subgraph B2["Bloque 2"]
        direction TB
        L306["306 · Computational graphs"]
        L307["307 · Inicialización de pesos"]
        L308["308 · Batch normalization y layer…"]
        L309["309 · Regularización y dropout"]
        L310["310 · Convolución discreta"]
        L306 --> L307
        L307 --> L308
        L308 --> L309
        L309 --> L310
    end
    subgraph B3["Bloque 3"]
        direction TB
        L311["311 · CNN y receptive fields"]
        L312["312 · Pooling y downsampling"]
        L313["313 · RNN y recurrencia"]
        L314["314 · Vanishing y exploding…"]
        L315["315 · LSTM y compuertas"]
        L311 --> L312
        L312 --> L313
        L313 --> L314
        L314 --> L315
    end
    subgraph B4["Bloque 4"]
        direction TB
        L316["316 · GRU"]
        L317["317 · Embeddings como espacios…"]
        L318["318 · Optimización de redes…"]
        L319["319 · Autodiff con PyTorch/JAX"]
        L320["320 · Capstone: red neuronal desde…"]
        L316 --> L317
        L317 --> L318
        L318 --> L319
        L319 --> L320
    end
    L305 --> L306
    L310 --> L311
    L315 --> L316
```

## 📚 Las clases

| # | Clase | Demostración | Idea central |
|---|---|---|---|
| `301` | [Perceptrón y separabilidad](301-perceptron-y-separabilidad/README.md) | `perceptron` | Perceptrón: converge si y solo si los datos son linealmente separables. |
| `302` | [MLP como composición de funciones](302-mlp-como-composicion-de-funciones/README.md) | `mlp` | MLP resolviendo XOR: la capa oculta crea una representación separable. |
| `303` | [Funciones de activación](303-funciones-de-activacion/README.md) | `activations` | Activaciones y sus derivadas: dónde se saturan. |
| `304` | [Funciones de pérdida](304-funciones-de-perdida/README.md) | `loss_functions` | MSE, MAE, Huber y cross-entropy frente a un valor atípico. |
| `305` | [Backpropagation paso a paso](305-backpropagation-paso-a-paso/README.md) | `backpropagation` | Backpropagation paso a paso sobre una red 2-2-1. |
| `306` | [Computational graphs](306-computational-graphs/README.md) | `computational_graphs` | El grafo de cómputo y la acumulación de gradientes en nodos reutilizados. |
| `307` | [Inicialización de pesos](307-inicializacion-de-pesos/README.md) | `weight_initialization` | Xavier y He: controlar la varianza de las activaciones capa a capa. |
| `308` | [Batch normalization y layer normalization](308-batch-normalization-y-layer-normalization/README.md) | `normalization` | Batch norm y layer norm: qué eje se normaliza. |
| `309` | [Regularización y dropout](309-regularizacion-y-dropout/README.md) | `dropout_regularization` | Dropout: ruido en entrenamiento, escalado coherente en inferencia. |
| `310` | [Convolución discreta](310-convolucion-discreta/README.md) | `discrete_convolution` | Convolución 2D con padding y stride: el cálculo de la forma de salida. |
| `311` | [CNN y receptive fields](311-cnn-y-receptive-fields/README.md) | `cnn_receptive_fields` | Campo receptivo: cómo crece al apilar capas. |
| `312` | [Pooling y downsampling](312-pooling-y-downsampling/README.md) | `pooling` | Max y average pooling: reducción con y sin pérdida de posición. |
| `313` | [RNN y recurrencia](313-rnn-y-recurrencia/README.md) | `rnn` | RNN: el estado oculto acumula historia con pesos compartidos. |
| `314` | [Vanishing y exploding gradients](314-vanishing-y-exploding-gradients/README.md) | `vanishing_exploding` | Gradientes que se desvanecen o explotan: un producto de derivadas. |
| `315` | [LSTM y compuertas](315-lstm-y-compuertas/README.md) | `lstm` | LSTM: la celda mantiene un camino aditivo para el gradiente. |
| `316` | [GRU](316-gru/README.md) | `gru` | GRU: dos puertas en lugar de tres, menos parámetros. |
| `317` | [Embeddings como espacios vectoriales](317-embeddings-como-espacios-vectoriales/README.md) | `embeddings` | Embeddings: geometría del significado y similitud coseno. |
| `318` | [Optimización de redes profundas](318-optimizacion-de-redes-profundas/README.md) | `deep_optimization` | Entrenar una red profunda: learning rate, warmup y clipping. |
| `319` | [Autodiff con PyTorch/JAX](319-autodiff-con-pytorch-jax/README.md) | `autodiff_frameworks` | Nuestro Var frente a PyTorch/JAX: mismo principio, distinta escala. |
| `320` | [Capstone: red neuronal desde cero en Python puro](320-capstone-red-neuronal-desde-cero-en-python-puro/README.md) | `capstone_neural_network` | Capstone: red neuronal completa desde cero, entrenada y evaluada. |

## 🧰 Stack de referencia

`math`, `random`, `numpy (opcional)`, `torch/jax (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen
como contraste profesional, no como requisito.

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 15
compmath catalog --part 15
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone ([320](320-capstone-red-neuronal-desde-cero-en-python-puro/README.md)) | 20 % |

## 📖 Bibliografía

- Goodfellow, I.; Bengio, Y.; Courville, A. *Deep Learning*. MIT Press, 2016.
- Glorot, X.; Bengio, Y. *Understanding the difficulty of training deep feedforward neural networks*. AISTATS, 2010.
- He, K. et al. *Delving Deep into Rectifiers*. ICCV, 2015.

---

> [⬅️ Parte 14 — Matemática de Machine Learning](../part-14-matematica-de-machine-learning/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 16 — Matemática de Transformers, modelos generativos, grafos y RL ➡️](../part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/README.md)
