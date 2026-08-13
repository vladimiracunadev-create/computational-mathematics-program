# 309 — Regularización y dropout

> [⬅️ 308 Batch normalization y layer normalization](../308-batch-normalization-y-layer-normalization/README.md) · [📚 Parte 15](../README.md) · [🏠 Programa](../../../README.md) · [310 Convolución discreta ➡️](../310-convolucion-discreta/README.md)

**Parte:** 15 — Matemática de Deep Learning · **Nivel:** `deep-learning` · **Horas estimadas:** 4
**Motor:** `engines.part15` · **Demostración:** `dropout_regularization` · **Clase 9 de 20** de la parte

---

## 🎯 Propósito

Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso, grafos de cómputo, inicialización, normalización, convolución, recurrencia y embeddings.

Esta clase concreta ese objetivo sobre **Regularización y dropout**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Regularización y dropout** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `dropout_regularization`.
4. Interpretar las 9 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: mezclar estadísticas de batch normalization entre entrenamiento e inferencia.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["Clase 308 · Batch normalization y…"] --> D
    subgraph CLASE["Clase 309 · Regularización y dropout"]
        direction TB
        D["Demostracion dropout_regularization"]
        D --> R["Resultados 5: neuronas +4"]
        D --> V["Comprobaciones 1: la_esperanza_se_conse…"]
        D --> O["Contexto 3: en_inferencia +2"]
    end
    R --> N["Clase 310 · Convolución discreta"]
    V -.-> IA["Aplicacion en IA · parte 15"]
```

## 🧠 Idea rectora de la parte 15

> Normalizar estabiliza la escala interna y permite tasas de aprendizaje mayores.

## 🔬 Qué ejecuta el laboratorio

`dropout_regularization` — Dropout: ruido en entrenamiento, escalado coherente en inferencia.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (5) | `neuronas`, `probabilidad_de_apagado`, `media_sin_dropout`, `media_con_inverted_dropout`, `varianza_introducida` |
| ✅ Comprobaciones de invariante (1) | `la_esperanza_se_conserva` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-15-matematica-de-deep-learning/309-regularizacion-y-dropout/lab.py
compmath run 309
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

> [⬅️ 308 Batch normalization y layer normalization](../308-batch-normalization-y-layer-normalization/README.md) · [📚 Parte 15](../README.md) · [🏠 Programa](../../../README.md) · [310 Convolución discreta ➡️](../310-convolucion-discreta/README.md)
