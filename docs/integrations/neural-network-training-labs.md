# neural-network-training-labs

Laboratorios prácticos de entrenamiento de redes.

> Este documento define un **puente conceptual**. No duplica ni resume el contenido de
> [`neural-network-training-labs`](https://github.com/vladimiracunadev-create/neural-network-training-labs): lo referencia como
> superficie de aplicación de la matemática que este programa enseña.

## Prerrequisitos matemáticos

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 05 | [Álgebra lineal I: vectores y matrices](../../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 07 | [Cálculo diferencial e integral](../../classes/part-07-calculo-diferencial-e-integral/README.md) | 20 | 80 h | universitario |
| 08 | [Cálculo multivariable, matricial y autodiferenciación](../../classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md) | 20 | 80 h | universitario-avanzado |
| 12 | [Optimización matemática y computacional](../../classes/part-12-optimizacion-matematica-y-computacional/README.md) | 20 | 80 h | avanzado |
| 13 | [Teoría de la información, señales y series](../../classes/part-13-teoria-de-la-informacion-senales-y-series/README.md) | 20 | 80 h | avanzado |
| 15 | [Matemática de Deep Learning](../../classes/part-15-matematica-de-deep-learning/README.md) | 20 | 80 h | deep-learning |

Total: 120 clases.

## Puntos de conexión concretos

| Concepto que usa `neural-network-training-labs` | Clase | Demostración |
|---|---|---|
| Regla de la cadena | [147](../../classes/part-07-calculo-diferencial-e-integral/147-regla-de-la-cadena/README.md) | `chain_rule` |
| Autodiferenciación | [179](../../classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/179-automatic-differentiation-y-computational-graphs/README.md) | `autodiff` |
| Adam y AdamW | [250](../../classes/part-12-optimizacion-matematica-y-computacional/250-adam/README.md) | `adam` |
| Cross-entropy | [263](../../classes/part-13-teoria-de-la-informacion-senales-y-series/263-entropia-cruzada/README.md) | `cross_entropy` |
| Convolución | [310](../../classes/part-15-matematica-de-deep-learning/310-convolucion-discreta/README.md) | `discrete_convolution` |

```bash
compmath show 147
compmath show 179
compmath show 250
compmath show 263
compmath show 310
```

## Cómo usar el puente

1. Identifica el concepto aplicado que no entiendes en `neural-network-training-labs`.
2. Localízalo en la tabla de arriba y abre su clase aquí.
3. Ejecuta su laboratorio **después de escribir tu predicción**.
4. Vuelve al repositorio especializado y repite la aplicación entendiendo la fórmula.

## Qué no hace este puente

- No sustituye el contenido de `neural-network-training-labs`.
- No garantiza que las partes listadas sean suficientes: son el mínimo, no el techo.
- No cubre las herramientas, frameworks ni prácticas de ingeniería de ese repositorio.
