# Parte 15 — Matemática de Deep Learning

**Nivel:** deep-learning
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part15.py`

Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso, grafos de cómputo, inicialización, normalización, convolución, recurrencia y embeddings.

## 🧠 Ideas centrales

- Backpropagation es la regla de la cadena aplicada en orden topológico inverso.
- Sin no linealidad, apilar capas sigue siendo una única transformación lineal.
- La inicialización controla la varianza de las activaciones y de los gradientes.
- Normalizar estabiliza la escala interna y permite tasas de aprendizaje mayores.
- El gradiente que se desvanece es un producto de derivadas menores que uno.

## 🤖 Por qué importa en IA

Toda arquitectura moderna, incluido el Transformer, se construye sobre estos bloques y sobre este mismo mecanismo de derivación.

## ⚠️ Errores frecuentes

- Inicializar todos los pesos iguales y romper la simetría nunca.
- Aplicar softmax sin restar el máximo y provocar overflow.
- Mezclar estadísticas de batch normalization entre entrenamiento e inferencia.

## 🧰 Stack de referencia

`math`, `random`, `numpy (opcional)`, `torch/jax (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [301 — Perceptrón y separabilidad](301-perceptron-y-separabilidad/README.md)
2. [302 — MLP como composición de funciones](302-mlp-como-composicion-de-funciones/README.md)
3. [303 — Funciones de activación](303-funciones-de-activacion/README.md)
4. [304 — Funciones de pérdida](304-funciones-de-perdida/README.md)
5. [305 — Backpropagation paso a paso](305-backpropagation-paso-a-paso/README.md)
6. [306 — Computational graphs](306-computational-graphs/README.md)
7. [307 — Inicialización de pesos](307-inicializacion-de-pesos/README.md)
8. [308 — Batch normalization y layer normalization](308-batch-normalization-y-layer-normalization/README.md)
9. [309 — Regularización y dropout](309-regularizacion-y-dropout/README.md)
10. [310 — Convolución discreta](310-convolucion-discreta/README.md)
11. [311 — CNN y receptive fields](311-cnn-y-receptive-fields/README.md)
12. [312 — Pooling y downsampling](312-pooling-y-downsampling/README.md)
13. [313 — RNN y recurrencia](313-rnn-y-recurrencia/README.md)
14. [314 — Vanishing y exploding gradients](314-vanishing-y-exploding-gradients/README.md)
15. [315 — LSTM y compuertas](315-lstm-y-compuertas/README.md)
16. [316 — GRU](316-gru/README.md)
17. [317 — Embeddings como espacios vectoriales](317-embeddings-como-espacios-vectoriales/README.md)
18. [318 — Optimización de redes profundas](318-optimizacion-de-redes-profundas/README.md)
19. [319 — Autodiff con PyTorch/JAX](319-autodiff-con-pytorch-jax/README.md)
20. [320 — Capstone: red neuronal desde cero en Python puro](320-capstone-red-neuronal-desde-cero-en-python-puro/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 15
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Goodfellow, I.; Bengio, Y.; Courville, A. *Deep Learning*. MIT Press, 2016.
- Glorot, X.; Bengio, Y. *Understanding the difficulty of training deep feedforward neural networks*. AISTATS, 2010.
- He, K. et al. *Delving Deep into Rectifiers*. ICCV, 2015.
