# python-data-science-program

Ciencia de datos aplicada con Python.

> Este documento define un **puente conceptual**. No duplica ni resume el contenido de
> [`python-data-science-program`](https://github.com/vladimiracunadev-create/python-data-science-program): lo referencia como
> superficie de aplicación de la matemática que este programa enseña.

## Prerrequisitos matemáticos

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 00 | [Pensamiento matemático desde cero](../../classes/part-00-pensamiento-matematico-desde-cero/README.md) | 20 | 80 h | cero-absoluto |
| 02 | [Álgebra y funciones](../../classes/part-02-algebra-y-funciones/README.md) | 20 | 80 h | basico |
| 05 | [Álgebra lineal I: vectores y matrices](../../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 09 | [Probabilidad y procesos aleatorios](../../classes/part-09-probabilidad-y-procesos-aleatorios/README.md) | 20 | 80 h | universitario |
| 10 | [Estadística e inferencia](../../classes/part-10-estadistica-e-inferencia/README.md) | 20 | 80 h | universitario-avanzado |
| 14 | [Matemática de Machine Learning](../../classes/part-14-matematica-de-machine-learning/README.md) | 20 | 80 h | ml-avanzado |

Total: 120 clases.

## Puntos de conexión concretos

| Concepto que usa `python-data-science-program` | Clase | Demostración |
|---|---|---|
| Estadística descriptiva | [201](../../classes/part-10-estadistica-e-inferencia/201-estadistica-descriptiva/README.md) | `descriptive_statistics` |
| Intervalos de confianza | [205](../../classes/part-10-estadistica-e-inferencia/205-intervalos-de-confianza/README.md) | `confidence_intervals` |
| p-value bien interpretado | [207](../../classes/part-10-estadistica-e-inferencia/207-p-value-correctamente-interpretado/README.md) | `p_value` |
| Regresión lineal | [214](../../classes/part-10-estadistica-e-inferencia/214-regresion-lineal-estadistica/README.md) | `linear_regression_stats` |
| Leakage y validación | [299](../../classes/part-14-matematica-de-machine-learning/299-generalizacion-validacion-y-leakage/README.md) | `generalization` |

```bash
compmath show 201
compmath show 205
compmath show 207
compmath show 214
compmath show 299
```

## Cómo usar el puente

1. Identifica el concepto aplicado que no entiendes en `python-data-science-program`.
2. Localízalo en la tabla de arriba y abre su clase aquí.
3. Ejecuta su laboratorio **después de escribir tu predicción**.
4. Vuelve al repositorio especializado y repite la aplicación entendiendo la fórmula.

## Qué no hace este puente

- No sustituye el contenido de `python-data-science-program`.
- No garantiza que las partes listadas sean suficientes: son el mínimo, no el techo.
- No cubre las herramientas, frameworks ni prácticas de ingeniería de ese repositorio.
