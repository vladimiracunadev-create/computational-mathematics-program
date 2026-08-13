# Ruta 11 — Bioinformática

**Para quién:** Analizas datos biológicos y necesitas estadística e inferencia sólidas.

**Objetivo:** Aplicar grafos, reducción de dimensionalidad e inferencia con controles honestos.

| Métrica | Valor |
|---|---:|
| Partes | 5 de 18 |
| Clases | 100 de 360 |
| Horas estimadas | 400 |
| A 10 h/semana | ~40 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 04 | [Matemática discreta para computación](../classes/part-04-matematica-discreta-para-computacion/README.md) | 20 | 80 h | intermedio |
| 05 | [Álgebra lineal I: vectores y matrices](../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 09 | [Probabilidad y procesos aleatorios](../classes/part-09-probabilidad-y-procesos-aleatorios/README.md) | 20 | 80 h | universitario |
| 10 | [Estadística e inferencia](../classes/part-10-estadistica-e-inferencia/README.md) | 20 | 80 h | universitario-avanzado |
| 14 | [Matemática de Machine Learning](../classes/part-14-matematica-de-machine-learning/README.md) | 20 | 80 h | ml-avanzado |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [093](../classes/part-04-matematica-discreta-para-computacion/093-grafos-vertices-y-aristas/README.md) | Grafos: vértices y aristas | `graphs` | Grados, aristas y el lema del apretón de manos. |
| [135](../classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/135-pca-desde-algebra-lineal/README.md) | PCA desde álgebra lineal | `pca` | PCA como autodescomposición de la covarianza. |
| [186](../classes/part-09-probabilidad-y-procesos-aleatorios/186-teorema-de-bayes/README.md) | Teorema de Bayes | `bayes` | Test médico: por qué un positivo no significa enfermedad. |
| [211](../classes/part-10-estadistica-e-inferencia/211-chi-cuadrado-y-tablas-de-contingencia/README.md) | Chi-cuadrado y tablas de contingencia | `chi_square` | Chi-cuadrado de independencia sobre una tabla de contingencia. |
| [218](../classes/part-10-estadistica-e-inferencia/218-bootstrap-y-remuestreo/README.md) | Bootstrap y remuestreo | `bootstrap` | Bootstrap: estimar la variabilidad sin suponer la distribución. |

```bash
compmath run 093
compmath run 135
compmath run 186
compmath run 211
compmath run 218
```

## Partes omitidas

Esta ruta **no** cubre: 00, 01, 02, 03, 06, 07, 08, 11, 12, 13, 15, 16, 17.

Omitir una parte es una decisión, no un descuento: si un ejercicio te bloquea porque
falta un concepto de una parte omitida, vuelve a ella. La tabla de prerrequisitos está
en [docs/LEARNING_PATH.md](../docs/LEARNING_PATH.md).

## Criterio de avance

- [ ] ≥ 80 % de los ejercicios básicos de cada parte;
- [ ] al menos 15 de los 20 laboratorios de cada parte, con predicción escrita previa;
- [ ] el capstone de cada parte entregado;
- [ ] las cinco preguntas de comprobación respondidas sin mirar el código.

```bash
compmath run --part 04 --quiet
compmath run --part 05 --quiet
compmath run --part 09 --quiet
compmath run --part 10 --quiet
compmath run --part 14 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
