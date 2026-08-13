# Parte 14 — Matemática de Machine Learning

**Nivel:** ml-avanzado
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part14.py`

Derivación matemática de los algoritmos clásicos: regresión, regularización, clasificación, kernels, árboles, ensambles, clustering, EM y compromiso sesgo-varianza.

## 🧠 Ideas centrales

- Cada algoritmo es un objetivo más un método de optimización; nada más.
- Ridge y Lasso resuelven el mismo problema con normas distintas y geometría distinta.
- El kernel trick evita construir el espacio de características explícitamente.
- El error de generalización se descompone en sesgo, varianza y ruido irreducible.
- El leakage produce métricas excelentes y modelos inútiles.

## 🤖 Por qué importa en IA

Estos algoritmos siguen siendo la línea base honesta contra la que se debe comparar cualquier modelo profundo.

## ⚠️ Errores frecuentes

- No estandarizar antes de aplicar regularización o k-NN.
- Elegir hiperparámetros con el conjunto de test.
- Interpretar coeficientes de un modelo con features correlacionadas.

## 🧰 Stack de referencia

`math`, `random`, `numpy (opcional)`, `scikit-learn (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [281 — Geometría del aprendizaje supervisado](281-geometria-del-aprendizaje-supervisado/README.md)
2. [282 — Regresión lineal desde mínimos cuadrados](282-regresion-lineal-desde-minimos-cuadrados/README.md)
3. [283 — Ridge y regularización L2](283-ridge-y-regularizacion-l2/README.md)
4. [284 — Lasso y regularización L1](284-lasso-y-regularizacion-l1/README.md)
5. [285 — Regresión logística y sigmoid](285-regresion-logistica-y-sigmoid/README.md)
6. [286 — Cross-entropy en clasificación](286-cross-entropy-en-clasificacion/README.md)
7. [287 — Naive Bayes](287-naive-bayes/README.md)
8. [288 — k-Nearest Neighbors y métricas](288-k-nearest-neighbors-y-metricas/README.md)
9. [289 — SVM y margen máximo](289-svm-y-margen-maximo/README.md)
10. [290 — Kernel trick](290-kernel-trick/README.md)
11. [291 — Árboles: entropía y Gini](291-arboles-entropia-y-gini/README.md)
12. [292 — Random Forest desde probabilidad](292-random-forest-desde-probabilidad/README.md)
13. [293 — Boosting y descenso funcional](293-boosting-y-descenso-funcional/README.md)
14. [294 — k-means como optimización](294-k-means-como-optimizacion/README.md)
15. [295 — Gaussian Mixture Models](295-gaussian-mixture-models/README.md)
16. [296 — EM algorithm](296-em-algorithm/README.md)
17. [297 — PCA aplicado a ML](297-pca-aplicado-a-ml/README.md)
18. [298 — Bias-variance tradeoff](298-bias-variance-tradeoff/README.md)
19. [299 — Generalización, validación y leakage](299-generalizacion-validacion-y-leakage/README.md)
20. [300 — Capstone: derivar y comparar 6 algoritmos ML](300-capstone-derivar-y-comparar-6-algoritmos-ml/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 14
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Hastie, T.; Tibshirani, R.; Friedman, J. *The Elements of Statistical Learning*. 2ª ed., Springer, 2009.
- Bishop, C. *Pattern Recognition and Machine Learning*. Springer, 2006.
- Murphy, K. *Probabilistic Machine Learning: An Introduction*. MIT Press, 2022.
