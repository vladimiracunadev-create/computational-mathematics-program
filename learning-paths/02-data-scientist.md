# Ruta 02 — Ciencia de datos

**Para quién:** Trabajas con datos y quieres dejar de engañarte con tus propias métricas.

**Objetivo:** Distinguir un resultado real de un artefacto del muestreo o del leakage.

| Métrica | Valor |
|---|---:|
| Partes | 6 de 18 |
| Clases | 120 de 360 |
| Horas estimadas | 480 |
| A 10 h/semana | ~48 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 00 | [Pensamiento matemático desde cero](../classes/part-00-pensamiento-matematico-desde-cero/README.md) | 20 | 80 h | cero-absoluto |
| 02 | [Álgebra y funciones](../classes/part-02-algebra-y-funciones/README.md) | 20 | 80 h | basico |
| 05 | [Álgebra lineal I: vectores y matrices](../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 09 | [Probabilidad y procesos aleatorios](../classes/part-09-probabilidad-y-procesos-aleatorios/README.md) | 20 | 80 h | universitario |
| 10 | [Estadística e inferencia](../classes/part-10-estadistica-e-inferencia/README.md) | 20 | 80 h | universitario-avanzado |
| 14 | [Matemática de Machine Learning](../classes/part-14-matematica-de-machine-learning/README.md) | 20 | 80 h | ml-avanzado |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [005](../classes/part-00-pensamiento-matematico-desde-cero/005-porcentajes-desde-cero/README.md) | Porcentajes desde cero | `percentage` | Aumento y descuento sucesivos: el orden no cambia, la reversión sí. |
| [186](../classes/part-09-probabilidad-y-procesos-aleatorios/186-teorema-de-bayes/README.md) | Teorema de Bayes | `bayes` | Test médico: por qué un positivo no significa enfermedad. |
| [205](../classes/part-10-estadistica-e-inferencia/205-intervalos-de-confianza/README.md) | Intervalos de confianza | `confidence_intervals` | Un IC 95 % describe el procedimiento, no una probabilidad del parámetro. |
| [207](../classes/part-10-estadistica-e-inferencia/207-p-value-correctamente-interpretado/README.md) | p-value correctamente interpretado | `p_value` | Qué mide y qué no mide un p-value. |
| [299](../classes/part-14-matematica-de-machine-learning/299-generalizacion-validacion-y-leakage/README.md) | Generalización, validación y leakage | `generalization` | Validación honesta frente a leakage: la misma métrica, dos verdades. |

```bash
compmath run 005
compmath run 186
compmath run 205
compmath run 207
compmath run 299
```

## Partes omitidas

Esta ruta **no** cubre: 01, 03, 04, 06, 07, 08, 11, 12, 13, 15, 16, 17.

Omitir una parte es una decisión, no un descuento: si un ejercicio te bloquea porque
falta un concepto de una parte omitida, vuelve a ella. La tabla de prerrequisitos está
en [docs/LEARNING_PATH.md](../docs/LEARNING_PATH.md).

## Criterio de avance

- [ ] ≥ 80 % de los ejercicios básicos de cada parte;
- [ ] al menos 15 de los 20 laboratorios de cada parte, con predicción escrita previa;
- [ ] el capstone de cada parte entregado;
- [ ] las cinco preguntas de comprobación respondidas sin mirar el código.

```bash
compmath run --part 00 --quiet
compmath run --part 02 --quiet
compmath run --part 05 --quiet
compmath run --part 09 --quiet
compmath run --part 10 --quiet
compmath run --part 14 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
