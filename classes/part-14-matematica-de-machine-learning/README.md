# 🤖 Parte 14 — Matemática de Machine Learning

> [⬅️ Parte 13 — Teoría de la información, señales y series](../part-13-teoria-de-la-informacion-senales-y-series/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 15 — Matemática de Deep Learning ➡️](../part-15-matematica-de-deep-learning/README.md)

**Nivel:** `ml-avanzado` · **Clases:** 20 · **Horas estimadas:** 80 · **Motor:** [`part14.py`](../../src/computational_math/engines/part14.py)

---

## 🎯 De qué trata esta parte

Derivación matemática de los algoritmos clásicos: regresión, regularización, clasificación, kernels, árboles, ensambles, clustering, EM y compromiso sesgo-varianza.

## 🧠 Ideas centrales

- Cada algoritmo es un objetivo más un método de optimización; nada más.
- Ridge y Lasso resuelven el mismo problema con normas distintas y geometría distinta.
- El kernel trick evita construir el espacio de características explícitamente.
- El error de generalización se descompone en sesgo, varianza y ruido irreducible.
- El leakage produce métricas excelentes y modelos inútiles.

## 🤖 Por qué importa en IA

> [!IMPORTANT]
> Estos algoritmos siguen siendo la línea base honesta contra la que se debe comparar cualquier modelo profundo.

## ⚠️ Errores frecuentes de esta parte

- No estandarizar antes de aplicar regularización o k-NN.
- Elegir hiperparámetros con el conjunto de test.
- Interpretar coeficientes de un modelo con features correlacionadas.

## 🧭 Secuencia de la parte

```mermaid
flowchart LR
    subgraph B1["Bloque 1"]
        direction TB
        L281["281 · Geometría del aprendizaje…"]
        L282["282 · Regresión lineal desde…"]
        L283["283 · Ridge y regularización L2"]
        L284["284 · Lasso y regularización L1"]
        L285["285 · Regresión logística y sigmoid"]
        L281 --> L282
        L282 --> L283
        L283 --> L284
        L284 --> L285
    end
    subgraph B2["Bloque 2"]
        direction TB
        L286["286 · Cross-entropy en clasificación"]
        L287["287 · Naive Bayes"]
        L288["288 · k-Nearest Neighbors y métricas"]
        L289["289 · SVM y margen máximo"]
        L290["290 · Kernel trick"]
        L286 --> L287
        L287 --> L288
        L288 --> L289
        L289 --> L290
    end
    subgraph B3["Bloque 3"]
        direction TB
        L291["291 · Árboles: entropía y Gini"]
        L292["292 · Random Forest desde…"]
        L293["293 · Boosting y descenso funcional"]
        L294["294 · k-means como optimización"]
        L295["295 · Gaussian Mixture Models"]
        L291 --> L292
        L292 --> L293
        L293 --> L294
        L294 --> L295
    end
    subgraph B4["Bloque 4"]
        direction TB
        L296["296 · EM algorithm"]
        L297["297 · PCA aplicado a ML"]
        L298["298 · Bias-variance tradeoff"]
        L299["299 · Generalización, validación y…"]
        L300["300 · Capstone: derivar y comparar…"]
        L296 --> L297
        L297 --> L298
        L298 --> L299
        L299 --> L300
    end
    L285 --> L286
    L290 --> L291
    L295 --> L296
```

## 📚 Las clases

| # | Clase | Demostración | Idea central |
|---|---|---|---|
| `281` | [Geometría del aprendizaje supervisado](281-geometria-del-aprendizaje-supervisado/README.md) | `supervised_geometry` | Aprendizaje supervisado como búsqueda de una frontera en el espacio. |
| `282` | [Regresión lineal desde mínimos cuadrados](282-regresion-lineal-desde-minimos-cuadrados/README.md) | `linear_regression` | Regresión lineal: solución cerrada y descenso de gradiente. |
| `283` | [Ridge y regularización L2](283-ridge-y-regularizacion-l2/README.md) | `ridge` | Ridge: L2 encoge los coeficientes y estabiliza el mal condicionamiento. |
| `284` | [Lasso y regularización L1](284-lasso-y-regularizacion-l1/README.md) | `lasso` | Lasso: L1 produce ceros exactos gracias a su geometría. |
| `285` | [Regresión logística y sigmoid](285-regresion-logistica-y-sigmoid/README.md) | `logistic_regression` | Regresión logística derivada desde la log-verosimilitud. |
| `286` | [Cross-entropy en clasificación](286-cross-entropy-en-clasificacion/README.md) | `classification_loss` | Cross-entropy penaliza la confianza equivocada de forma no acotada. |
| `287` | [Naive Bayes](287-naive-bayes/README.md) | `naive_bayes` | Naive Bayes gaussiano: independencia condicional como supuesto explícito. |
| `288` | [k-Nearest Neighbors y métricas](288-k-nearest-neighbors-y-metricas/README.md) | `knn` | k-NN: la métrica y el escalado deciden el resultado. |
| `289` | [SVM y margen máximo](289-svm-y-margen-maximo/README.md) | `svm_margin` | SVM: maximizar el margen equivale a minimizar ‖w‖. |
| `290` | [Kernel trick](290-kernel-trick/README.md) | `kernel_trick` | El kernel calcula el producto punto sin construir el espacio. |
| `291` | [Árboles: entropía y Gini](291-arboles-entropia-y-gini/README.md) | `tree_impurity` | Entropía y Gini: dos medidas de impureza para elegir el corte. |
| `292` | [Random Forest desde probabilidad](292-random-forest-desde-probabilidad/README.md) | `random_forest` | Bagging: promediar modelos decorrelacionados reduce la varianza. |
| `293` | [Boosting y descenso funcional](293-boosting-y-descenso-funcional/README.md) | `boosting` | Boosting: cada modelo corrige el residuo del anterior (descenso funcional). |
| `294` | [k-means como optimización](294-k-means-como-optimizacion/README.md) | `kmeans` | k-means como minimización de la inercia (Lloyd). |
| `295` | [Gaussian Mixture Models](295-gaussian-mixture-models/README.md) | `gmm` | Mezcla de gaussianas: asignación blanda en lugar de dura. |
| `296` | [EM algorithm](296-em-algorithm/README.md) | `em_algorithm` | EM: E-step y M-step sobre datos con una variable latente. |
| `297` | [PCA aplicado a ML](297-pca-aplicado-a-ml/README.md) | `pca_ml` | PCA como preprocesamiento: cuánta varianza se conserva. |
| `298` | [Bias-variance tradeoff](298-bias-variance-tradeoff/README.md) | `bias_variance` | Descomposición sesgo-varianza medida por simulación. |
| `299` | [Generalización, validación y leakage](299-generalizacion-validacion-y-leakage/README.md) | `generalization` | Validación honesta frente a leakage: la misma métrica, dos verdades. |
| `300` | [Capstone: derivar y comparar 6 algoritmos ML](300-capstone-derivar-y-comparar-6-algoritmos-ml/README.md) | `capstone_six_algorithms` | Capstone: seis algoritmos derivados y comparados sobre los mismos datos. |

## 🧰 Stack de referencia

`math`, `random`, `numpy (opcional)`, `scikit-learn (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen
como contraste profesional, no como requisito.

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 14
compmath catalog --part 14
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone ([300](300-capstone-derivar-y-comparar-6-algoritmos-ml/README.md)) | 20 % |

## 📖 Bibliografía

- Hastie, T.; Tibshirani, R.; Friedman, J. *The Elements of Statistical Learning*. 2ª ed., Springer, 2009.
- Bishop, C. *Pattern Recognition and Machine Learning*. Springer, 2006.
- Murphy, K. *Probabilistic Machine Learning: An Introduction*. MIT Press, 2022.

---

> [⬅️ Parte 13 — Teoría de la información, señales y series](../part-13-teoria-de-la-informacion-senales-y-series/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 15 — Matemática de Deep Learning ➡️](../part-15-matematica-de-deep-learning/README.md)
