# 289 — SVM y margen máximo

> [⬅️ 288 k-Nearest Neighbors y métricas](../288-k-nearest-neighbors-y-metricas/README.md) · [📚 Parte 14](../README.md) · [🏠 Programa](../../../README.md) · [290 Kernel trick ➡️](../290-kernel-trick/README.md)

**Parte:** 14 — Matemática de Machine Learning · **Nivel:** `ml-avanzado` · **Horas estimadas:** 4
**Motor:** `engines.part14` · **Demostración:** `svm_margin` · **Clase 9 de 20** de la parte

---

## 🎯 Propósito

Derivación matemática de los algoritmos clásicos: regresión, regularización, clasificación, kernels, árboles, ensambles, clustering, EM y compromiso sesgo-varianza.

Esta clase concreta ese objetivo sobre **SVM y margen máximo**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **SVM y margen máximo** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `svm_margin`.
4. Interpretar las 9 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: interpretar coeficientes de un modelo con features correlacionadas.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["288<br/>k-Nearest Neighbors y<br/>métricas"] --> C
    subgraph C["289 · SVM y margen máximo"]
        direction TB
        D["Demostración<br/><code>svm_margin</code>"] --> R["Resultados numéricos<br/>b<br/>norma_de_w<br/>ancho_del_margen_2/|w|<br/>… +3 más"]
        D --> V["Verificaciones<br/>solo_los_vectores_de_soporte_definen_la_frontera"]
        D --> O["Contexto y estructura<br/>w<br/>objetivo"]
    end
    C --> N["290<br/>Kernel trick"]
    C -.-> IA["Uso en IA<br/>parte 14"]
```

## 🧠 Idea rectora de la parte 14

> El error de generalización se descompone en sesgo, varianza y ruido irreducible.

## 🔬 Qué ejecuta el laboratorio

`svm_margin` — SVM: maximizar el margen equivale a minimizar ‖w‖.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (6) | `b`, `norma_de_w`, `ancho_del_margen_2/|w|`, `vectores_de_soporte`, `accuracy`, `hinge_loss` |
| ✅ Comprobaciones de invariante (1) | `solo_los_vectores_de_soporte_definen_la_frontera` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-14-matematica-de-machine-learning/289-svm-y-margen-maximo/lab.py
compmath run 289
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- No estandarizar antes de aplicar regularización o k-NN.
- Elegir hiperparámetros con el conjunto de test.
- Interpretar coeficientes de un modelo con features correlacionadas.

## 🤖 Conexión con IA

Estos algoritmos siguen siendo la línea base honesta contra la que se debe comparar cualquier modelo profundo.

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
5. ¿Dónde aparece esto en scoring crediticio?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Hastie, T.; Tibshirani, R.; Friedman, J. *The Elements of Statistical Learning*. 2ª ed., Springer, 2009.
- Bishop, C. *Pattern Recognition and Machine Learning*. Springer, 2006.
- Murphy, K. *Probabilistic Machine Learning: An Introduction*. MIT Press, 2022.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 288 k-Nearest Neighbors y métricas](../288-k-nearest-neighbors-y-metricas/README.md) · [📚 Parte 14](../README.md) · [🏠 Programa](../../../README.md) · [290 Kernel trick ➡️](../290-kernel-trick/README.md)
