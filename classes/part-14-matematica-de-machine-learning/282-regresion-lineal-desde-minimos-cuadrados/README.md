# 282 — Regresión lineal desde mínimos cuadrados

**Parte:** 14 — Matemática de Machine Learning
**Nivel:** ml-avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part14` · demostración `linear_regression`

## 🎯 Propósito

Derivación matemática de los algoritmos clásicos: regresión, regularización, clasificación, kernels, árboles, ensambles, clustering, EM y compromiso sesgo-varianza.

Esta clase concreta ese objetivo sobre **Regresión lineal desde mínimos cuadrados**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Regresión lineal desde mínimos cuadrados** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `linear_regression` del motor de la parte.
4. Interpretar las 9 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: elegir hiperparámetros con el conjunto de test.

## 🧠 Idea rectora de la parte 14

> Ridge y Lasso resuelven el mismo problema con normas distintas y geometría distinta.

## 🧩 Qué calcula el laboratorio

`linear_regression` — Regresión lineal: solución cerrada y descenso de gradiente.

Salidas que devuelve:

- `observaciones`
- `features`
- `parametros_reales`
- `solucion_cerrada`
- `descenso_de_gradiente`
- `MSE_cerrada`
- `MSE_gradiente`
- `coinciden`
- `cuando_usar_gradiente`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-14-matematica-de-machine-learning/282-regresion-lineal-desde-minimos-cuadrados/lab.py
```

o desde la CLI del programa:

```bash
compmath run 282
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- No estandarizar antes de aplicar regularización o k-NN.
- Elegir hiperparámetros con el conjunto de test.
- Interpretar coeficientes de un modelo con features correlacionadas.

## 🤖 Conexión con IA

Estos algoritmos siguen siendo la línea base honesta contra la que se debe comparar cualquier modelo profundo.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Hastie, T.; Tibshirani, R.; Friedman, J. *The Elements of Statistical Learning*. 2ª ed., Springer, 2009.
- Bishop, C. *Pattern Recognition and Machine Learning*. Springer, 2006.
- Murphy, K. *Probabilistic Machine Learning: An Introduction*. MIT Press, 2022.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
