# 310 — Convolución discreta

**Parte:** 15 — Matemática de Deep Learning
**Nivel:** deep-learning
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part15` · demostración `discrete_convolution`

## 🎯 Propósito

Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso, grafos de cómputo, inicialización, normalización, convolución, recurrencia y embeddings.

Esta clase concreta ese objetivo sobre **Convolución discreta**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Convolución discreta** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `discrete_convolution` del motor de la parte.
4. Interpretar las 11 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: inicializar todos los pesos iguales y romper la simetría nunca.

## 🧠 Idea rectora de la parte 15

> El gradiente que se desvanece es un producto de derivadas menores que uno.

## 🧩 Qué calcula el laboratorio

`discrete_convolution` — Convolución 2D con padding y stride: el cálculo de la forma de salida.

Salidas que devuelve:

- `entrada_shape`
- `kernel_shape`
- `kernel`
- `salida_stride_1`
- `shape_stride_1`
- `shape_stride_2`
- `formula`
- `verificacion_stride_1`
- `parametros_del_kernel`
- `parametros_de_una_densa_equivalente`
- `compartir_pesos`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-15-matematica-de-deep-learning/310-convolucion-discreta/lab.py
```

o desde la CLI del programa:

```bash
compmath run 310
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Inicializar todos los pesos iguales y romper la simetría nunca.
- Aplicar softmax sin restar el máximo y provocar overflow.
- Mezclar estadísticas de batch normalization entre entrenamiento e inferencia.

## 🤖 Conexión con IA

Toda arquitectura moderna, incluido el Transformer, se construye sobre estos bloques y sobre este mismo mecanismo de derivación.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Goodfellow, I.; Bengio, Y.; Courville, A. *Deep Learning*. MIT Press, 2016.
- Glorot, X.; Bengio, Y. *Understanding the difficulty of training deep feedforward neural networks*. AISTATS, 2010.
- He, K. et al. *Delving Deep into Rectifiers*. ICCV, 2015.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
