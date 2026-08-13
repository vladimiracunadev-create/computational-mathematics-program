# 311 — CNN y receptive fields

> [⬅️ 310 Convolución discreta](../310-convolucion-discreta/README.md) · [📚 Parte 15](../README.md) · [🏠 Programa](../../../README.md) · [312 Pooling y downsampling ➡️](../312-pooling-y-downsampling/README.md)

**Parte:** 15 — Matemática de Deep Learning · **Nivel:** `deep-learning` · **Horas estimadas:** 4
**Motor:** `engines.part15` · **Demostración:** `cnn_receptive_fields` · **Clase 11 de 20** de la parte

---

## 🎯 Propósito

Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso, grafos de cómputo, inicialización, normalización, convolución, recurrencia y embeddings.

Esta clase concreta ese objetivo sobre **CNN y receptive fields**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **CNN y receptive fields** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `cnn_receptive_fields`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: aplicar softmax sin restar el máximo y provocar overflow.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["Clase 310 · Convolución discreta"] --> D
    subgraph CLASE["Clase 311 · CNN y receptive fields"]
        direction TB
        D["Demostracion cnn_receptive_fields"]
        D --> R["Resultados 3: campo_receptivo_final +2"]
        D --> V["Comprobaciones 1: dos_conv_3x3_equivale…"]
        D --> O["Contexto 4: arquitectura +3"]
    end
    R --> N["Clase 312 · Pooling y downsampling"]
    V -.-> IA["Aplicacion en IA · parte 15"]
```

## 🧠 Idea rectora de la parte 15

> Backpropagation es la regla de la cadena aplicada en orden topológico inverso.

## 🔬 Qué ejecuta el laboratorio

`cnn_receptive_fields` — Campo receptivo: cómo crece al apilar capas.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (3) | `campo_receptivo_final`, `parametros_2x(3x3)`, `parametros_1x(5x5)` |
| ✅ Comprobaciones de invariante (1) | `dos_conv_3x3_equivalen_a_una_5x5` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-15-matematica-de-deep-learning/311-cnn-y-receptive-fields/lab.py
compmath run 311
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Inicializar todos los pesos iguales y romper la simetría nunca.
- Aplicar softmax sin restar el máximo y provocar overflow.
- Mezclar estadísticas de batch normalization entre entrenamiento e inferencia.

## 🤖 Conexión con IA

Toda arquitectura moderna, incluido el Transformer, se construye sobre estos bloques y sobre este mismo mecanismo de derivación.

## 📓 Notebooks

| Archivo | Para qué |
|---|---|
| [`notebook.ipynb`](notebook.ipynb) | recorrido guiado con la demostración ejecutada |
| [`notebook_student.ipynb`](notebook_student.ipynb) | versión con `TODO` para resolver |
| [`notebook_solution.ipynb`](notebook_solution.ipynb) | solución de referencia verificada |

## 📝 Evaluación

| Criterio | Peso |
|---|---:|
| Comprensión conceptual | 25 % |
| Resolución manual | 25 % |
| Implementación y verificación | 25 % |
| Interpretación y comunicación | 15 % |
| Conexión con aplicación real | 10 % |

Detalle y criterios de error crítico en [`assessment.md`](assessment.md).

## ❓ Preguntas de comprobación

1. ¿Cuál es la entrada, cuál la salida y qué unidades tienen?
2. ¿Qué operación domina el comportamiento del resultado?
3. ¿Qué caso extremo revelaría un error conceptual?
4. ¿Cómo verificarías el resultado por un método independiente?
5. ¿Dónde aparece esto en visión?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Goodfellow, I.; Bengio, Y.; Courville, A. *Deep Learning*. MIT Press, 2016.
- Glorot, X.; Bengio, Y. *Understanding the difficulty of training deep feedforward neural networks*. AISTATS, 2010.
- He, K. et al. *Delving Deep into Rectifiers*. ICCV, 2015.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 310 Convolución discreta](../310-convolucion-discreta/README.md) · [📚 Parte 15](../README.md) · [🏠 Programa](../../../README.md) · [312 Pooling y downsampling ➡️](../312-pooling-y-downsampling/README.md)
