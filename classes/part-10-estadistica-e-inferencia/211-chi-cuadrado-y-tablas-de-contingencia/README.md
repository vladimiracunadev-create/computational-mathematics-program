# 211 — Chi-cuadrado y tablas de contingencia

**Parte:** 10 — Estadística e inferencia
**Nivel:** universitario-avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part10` · demostración `chi_square`

## 🎯 Propósito

Descriptiva, muestreo, estimadores, intervalos de confianza, pruebas de hipótesis, p-value, potencia, verosimilitud, MAP, inferencia bayesiana, bootstrap y A/B testing.

Esta clase concreta ese objetivo sobre **Chi-cuadrado y tablas de contingencia**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Chi-cuadrado y tablas de contingencia** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `chi_square` del motor de la parte.
4. Interpretar las 9 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: confundir significancia estadística con relevancia práctica.

## 🧠 Idea rectora de la parte 10

> El p-value es P(datos tan extremos | H0), nunca P(H0 | datos).

## 🧩 Qué calcula el laboratorio

`chi_square` — Chi-cuadrado de independencia sobre una tabla de contingencia.

Salidas que devuelve:

- `tabla_observada`
- `totales_fila`
- `totales_columna`
- `tabla_esperada`
- `chi_cuadrado`
- `grados_de_libertad`
- `valor_critico_5%`
- `rechaza_independencia`
- `requisito`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-10-estadistica-e-inferencia/211-chi-cuadrado-y-tablas-de-contingencia/lab.py
```

o desde la CLI del programa:

```bash
compmath run 211
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- p-hacking por comparaciones múltiples sin corrección.
- Confundir significancia estadística con relevancia práctica.
- Evaluar sobre datos que participaron en la selección del modelo.

## 🤖 Conexión con IA

Evaluar un modelo es inferencia estadística: métricas con intervalo, comparaciones múltiples corregidas y detección de leakage.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Wasserman, L. *All of Statistics*. Springer, 2004.
- Gelman, A. et al. *Bayesian Data Analysis*. 3ª ed., CRC, 2013.
- Efron, B.; Tibshirani, R. *An Introduction to the Bootstrap*. Chapman & Hall, 1993.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
