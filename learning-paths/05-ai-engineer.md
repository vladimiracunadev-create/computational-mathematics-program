# Ruta 05 — Ingeniería de IA

**Para quién:** Construyes sistemas con LLM y quieres entender qué ocurre dentro.

**Objetivo:** Explicar atención, embeddings y muestreo sin recurrir a analogías.

| Métrica | Valor |
|---|---:|
| Partes | 5 de 18 |
| Clases | 100 de 360 |
| Horas estimadas | 400 |
| A 10 h/semana | ~40 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 05 | [Álgebra lineal I: vectores y matrices](../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 06 | [Álgebra lineal II: descomposiciones y tensores](../classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/README.md) | 20 | 80 h | intermedio-avanzado |
| 09 | [Probabilidad y procesos aleatorios](../classes/part-09-probabilidad-y-procesos-aleatorios/README.md) | 20 | 80 h | universitario |
| 13 | [Teoría de la información, señales y series](../classes/part-13-teoria-de-la-informacion-senales-y-series/README.md) | 20 | 80 h | avanzado |
| 16 | [Matemática de Transformers, modelos generativos, grafos y RL](../classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/README.md) | 20 | 80 h | experto |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [103](../classes/part-05-algebra-lineal-i-vectores-y-matrices/103-producto-punto-y-similitud/README.md) | Producto punto y similitud | `dot_product` | Producto punto: proyección, ángulo y similitud. |
| [132](../classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/132-svd-desde-la-intuicion/README.md) | SVD desde la intuición | `svd_intuition` | SVD: rotar, escalar, rotar. Existe siempre. |
| [321](../classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/321-softmax-y-distribuciones-categoricas/README.md) | Softmax y distribuciones categóricas | `softmax_distributions` | Softmax: de logits arbitrarios a una distribución categórica. |
| [325](../classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/325-scaled-dot-product-attention/README.md) | Scaled dot-product attention | `scaled_dot_product_attention` | Atención escalada: por qué existe el 1/√d. |
| [330](../classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/330-sampling-temperatura-top-k-y-top-p/README.md) | Sampling, temperatura, top-k y top-p | `sampling_strategies` | Temperatura, top-k y top-p reescriben la distribución antes de muestrear. |

```bash
compmath run 103
compmath run 132
compmath run 321
compmath run 325
compmath run 330
```

## Partes omitidas

Esta ruta **no** cubre: 00, 01, 02, 03, 04, 07, 08, 10, 11, 12, 14, 15, 17.

Omitir una parte es una decisión, no un descuento: si un ejercicio te bloquea porque
falta un concepto de una parte omitida, vuelve a ella. La tabla de prerrequisitos está
en [docs/LEARNING_PATH.md](../docs/LEARNING_PATH.md).

## Criterio de avance

- [ ] ≥ 80 % de los ejercicios básicos de cada parte;
- [ ] al menos 15 de los 20 laboratorios de cada parte, con predicción escrita previa;
- [ ] el capstone de cada parte entregado;
- [ ] las cinco preguntas de comprobación respondidas sin mirar el código.

```bash
compmath run --part 05 --quiet
compmath run --part 06 --quiet
compmath run --part 09 --quiet
compmath run --part 13 --quiet
compmath run --part 16 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
