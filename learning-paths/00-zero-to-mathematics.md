# Ruta 00 — De cero a la matemática

**Para quién:** Nunca te llevaste bien con las matemáticas y quieres empezar de verdad.

**Objetivo:** Terminar sin miedo a una fórmula y con criterio para auditar un número.

| Métrica | Valor |
|---|---:|
| Partes | 5 de 18 |
| Clases | 100 de 360 |
| Horas estimadas | 400 |
| A 10 h/semana | ~40 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 00 | [Pensamiento matemático desde cero](../classes/part-00-pensamiento-matematico-desde-cero/README.md) | 20 | 80 h | cero-absoluto |
| 01 | [Aritmética computacional y representación numérica](../classes/part-01-aritmetica-computacional-y-representacion-numerica/README.md) | 20 | 80 h | basico-computacional |
| 02 | [Álgebra y funciones](../classes/part-02-algebra-y-funciones/README.md) | 20 | 80 h | basico |
| 03 | [Geometría, trigonometría y geometría analítica](../classes/part-03-geometria-trigonometria-y-geometria-analitica/README.md) | 20 | 80 h | basico-intermedio |
| 04 | [Matemática discreta para computación](../classes/part-04-matematica-discreta-para-computacion/README.md) | 20 | 80 h | intermedio |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [001](../classes/part-00-pensamiento-matematico-desde-cero/001-numeros-naturales-y-conteo/README.md) | Números naturales y conteo | `counting` | Conteo, suma de Gauss y verificación cerrada frente a iterativa. |
| [029](../classes/part-01-aritmetica-computacional-y-representacion-numerica/029-por-que-0-1-0-2-no-es-exactamente-0-3/README.md) | Por qué 0.1 + 0.2 no es exactamente 0.3 | `why_point_one` | 0.1 + 0.2 != 0.3 explicado con la fracción binaria real. |
| [043](../classes/part-02-algebra-y-funciones/043-ecuaciones-lineales-de-una-variable/README.md) | Ecuaciones lineales de una variable | `linear_equation` | Resolver ax + b = c y verificar el residuo. |
| [064](../classes/part-03-geometria-trigonometria-y-geometria-analitica/064-teorema-de-pitagoras/README.md) | Teorema de Pitágoras | `pythagoras` | Pitágoras, su recíproco y una terna pitagórica generada. |
| [091](../classes/part-04-matematica-discreta-para-computacion/091-induccion-matematica/README.md) | Inducción matemática | `induction` | Inducción: caso base, paso inductivo y verificación empírica. |

```bash
compmath run 001
compmath run 029
compmath run 043
compmath run 064
compmath run 091
```

## Partes omitidas

Esta ruta **no** cubre: 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17.

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
compmath run --part 01 --quiet
compmath run --part 02 --quiet
compmath run --part 03 --quiet
compmath run --part 04 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
