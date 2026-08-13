# Ruta 06 — Investigación en IA

**Para quién:** Lees papers y quieres reproducir su idea matemática, no solo citarlos.

**Objetivo:** Reproducir la predicción cuantitativa de un paper con implementación propia.

| Métrica | Valor |
|---|---:|
| Partes | 6 de 18 |
| Clases | 120 de 360 |
| Horas estimadas | 480 |
| A 10 h/semana | ~48 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 08 | [Cálculo multivariable, matricial y autodiferenciación](../classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md) | 20 | 80 h | universitario-avanzado |
| 10 | [Estadística e inferencia](../classes/part-10-estadistica-e-inferencia/README.md) | 20 | 80 h | universitario-avanzado |
| 12 | [Optimización matemática y computacional](../classes/part-12-optimizacion-matematica-y-computacional/README.md) | 20 | 80 h | avanzado |
| 13 | [Teoría de la información, señales y series](../classes/part-13-teoria-de-la-informacion-senales-y-series/README.md) | 20 | 80 h | avanzado |
| 16 | [Matemática de Transformers, modelos generativos, grafos y RL](../classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/README.md) | 20 | 80 h | experto |
| 17 | [Frontera matemática para IA e investigación](../classes/part-17-frontera-matematica-para-ia-e-investigacion/README.md) | 20 | 80 h | frontera-investigacion |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [179](../classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/179-automatic-differentiation-y-computational-graphs/README.md) | Automatic differentiation y computational graphs | `autodiff` | Autodiferenciación en modo reverso sobre el grafo de cómputo. |
| [217](../classes/part-10-estadistica-e-inferencia/217-inferencia-bayesiana/README.md) | Inferencia bayesiana | `bayesian_inference` | Actualización bayesiana conjugada Beta-Binomial. |
| [332](../classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/332-elbo-y-variational-inference/README.md) | ELBO y variational inference | `elbo` | ELBO: reconstrucción menos KL, y su relación con la log-verosimilitud. |
| [346](../classes/part-17-frontera-matematica-para-ia-e-investigacion/346-optimal-transport/README.md) | Optimal transport | `optimal_transport` | Transporte óptimo por Sinkhorn: coste de mover una distribución a otra. |
| [353](../classes/part-17-frontera-matematica-para-ia-e-investigacion/353-score-matching/README.md) | Score matching | `score_matching` | Score matching: aprender ∇ log p sin conocer la constante de normalización. |
| [360](../classes/part-17-frontera-matematica-para-ia-e-investigacion/360-capstone-final-reproducir-una-idea-matematica-de-un-paper/README.md) | Capstone final: reproducir una idea matemática de un paper | `capstone_reproduce_paper_idea` | Capstone: reproducir el núcleo matemático de un resultado publicado. |

```bash
compmath run 179
compmath run 217
compmath run 332
compmath run 346
compmath run 353
compmath run 360
```

## Partes omitidas

Esta ruta **no** cubre: 00, 01, 02, 03, 04, 05, 06, 07, 09, 11, 14, 15.

Omitir una parte es una decisión, no un descuento: si un ejercicio te bloquea porque
falta un concepto de una parte omitida, vuelve a ella. La tabla de prerrequisitos está
en [docs/LEARNING_PATH.md](../docs/LEARNING_PATH.md).

## Criterio de avance

- [ ] ≥ 80 % de los ejercicios básicos de cada parte;
- [ ] al menos 15 de los 20 laboratorios de cada parte, con predicción escrita previa;
- [ ] el capstone de cada parte entregado;
- [ ] las cinco preguntas de comprobación respondidas sin mirar el código.

```bash
compmath run --part 08 --quiet
compmath run --part 10 --quiet
compmath run --part 12 --quiet
compmath run --part 13 --quiet
compmath run --part 16 --quiet
compmath run --part 17 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
