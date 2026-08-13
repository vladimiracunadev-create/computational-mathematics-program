# Ruta 04 — Deep Learning

**Para quién:** Entrenas redes y quieres entender cada término de la actualización.

**Objetivo:** Implementar backpropagation a mano y comprobar que coincide con autograd.

| Métrica | Valor |
|---|---:|
| Partes | 6 de 18 |
| Clases | 120 de 360 |
| Horas estimadas | 480 |
| A 10 h/semana | ~48 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 05 | [Álgebra lineal I: vectores y matrices](../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 07 | [Cálculo diferencial e integral](../classes/part-07-calculo-diferencial-e-integral/README.md) | 20 | 80 h | universitario |
| 08 | [Cálculo multivariable, matricial y autodiferenciación](../classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md) | 20 | 80 h | universitario-avanzado |
| 12 | [Optimización matemática y computacional](../classes/part-12-optimizacion-matematica-y-computacional/README.md) | 20 | 80 h | avanzado |
| 13 | [Teoría de la información, señales y series](../classes/part-13-teoria-de-la-informacion-senales-y-series/README.md) | 20 | 80 h | avanzado |
| 15 | [Matemática de Deep Learning](../classes/part-15-matematica-de-deep-learning/README.md) | 20 | 80 h | deep-learning |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [147](../classes/part-07-calculo-diferencial-e-integral/147-regla-de-la-cadena/README.md) | Regla de la cadena | `chain_rule` | La regla de la cadena: el mecanismo entero de backpropagation. |
| [179](../classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/179-automatic-differentiation-y-computational-graphs/README.md) | Automatic differentiation y computational graphs | `autodiff` | Autodiferenciación en modo reverso sobre el grafo de cómputo. |
| [250](../classes/part-12-optimizacion-matematica-y-computacional/250-adam/README.md) | Adam | `adam` | Adam: momentum de primer y segundo orden con corrección de sesgo. |
| [263](../classes/part-13-teoria-de-la-informacion-senales-y-series/263-entropia-cruzada/README.md) | Entropía cruzada | `cross_entropy` | Entropía cruzada: el coste de codificar p con un código para q. |
| [305](../classes/part-15-matematica-de-deep-learning/305-backpropagation-paso-a-paso/README.md) | Backpropagation paso a paso | `backpropagation` | Backpropagation paso a paso sobre una red 2-2-1. |
| [320](../classes/part-15-matematica-de-deep-learning/320-capstone-red-neuronal-desde-cero-en-python-puro/README.md) | Capstone: red neuronal desde cero en Python puro | `capstone_neural_network` | Capstone: red neuronal completa desde cero, entrenada y evaluada. |

```bash
compmath run 147
compmath run 179
compmath run 250
compmath run 263
compmath run 305
compmath run 320
```

## Partes omitidas

Esta ruta **no** cubre: 00, 01, 02, 03, 04, 06, 09, 10, 11, 14, 16, 17.

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
compmath run --part 07 --quiet
compmath run --part 08 --quiet
compmath run --part 12 --quiet
compmath run --part 13 --quiet
compmath run --part 15 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
