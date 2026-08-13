# 306 — Computational graphs

**Parte:** 15 — Matemática de Deep Learning
**Nivel:** deep-learning
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part15` · demostración `computational_graphs`

## 🎯 Propósito

Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso, grafos de cómputo, inicialización, normalización, convolución, recurrencia y embeddings.

Esta clase concreta ese objetivo sobre **Computational graphs**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Computational graphs** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `computational_graphs` del motor de la parte.
4. Interpretar las 11 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: mezclar estadísticas de batch normalization entre entrenamiento e inferencia.

## 🧠 Idea rectora de la parte 15

> Backpropagation es la regla de la cadena aplicada en orden topológico inverso.

## 🧩 Qué calcula el laboratorio

`computational_graphs` — El grafo de cómputo y la acumulación de gradientes en nodos reutilizados.

Salidas que devuelve:

- `expresion_1`
- `y`
- `dy/dx`
- `dy/dx_analitico_2x+1`
- `acumulacion_correcta`
- `expresion_2`
- `e`
- `de/da`
- `de/db`
- `nodos_con_multiples_consumidores`
- `error_clasico`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-15-matematica-de-deep-learning/306-computational-graphs/lab.py
```

o desde la CLI del programa:

```bash
compmath run 306
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
