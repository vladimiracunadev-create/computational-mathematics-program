# Ruta 01 — Ingeniería de software

**Para quién:** Programas a diario y quieres dejar de tratar los números como cajas negras.

**Objetivo:** Entender precisión, complejidad, grafos y sistemas lineales en tu propio código.

| Métrica | Valor |
|---|---:|
| Partes | 5 de 18 |
| Clases | 100 de 360 |
| Horas estimadas | 400 |
| A 10 h/semana | ~40 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 01 | [Aritmética computacional y representación numérica](../classes/part-01-aritmetica-computacional-y-representacion-numerica/README.md) | 20 | 80 h | basico-computacional |
| 02 | [Álgebra y funciones](../classes/part-02-algebra-y-funciones/README.md) | 20 | 80 h | basico |
| 04 | [Matemática discreta para computación](../classes/part-04-matematica-discreta-para-computacion/README.md) | 20 | 80 h | intermedio |
| 05 | [Álgebra lineal I: vectores y matrices](../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 11 | [Métodos numéricos y computación científica](../classes/part-11-metodos-numericos-y-computacion-cientifica/README.md) | 20 | 80 h | cientifico |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [029](../classes/part-01-aritmetica-computacional-y-representacion-numerica/029-por-que-0-1-0-2-no-es-exactamente-0-3/README.md) | Por qué 0.1 + 0.2 no es exactamente 0.3 | `why_point_one` | 0.1 + 0.2 != 0.3 explicado con la fracción binaria real. |
| [032](../classes/part-01-aritmetica-computacional-y-representacion-numerica/032-cancelacion-catastrofica/README.md) | Cancelación catastrófica | `catastrophic_cancellation` | Dos fórmulas algebraicamente iguales con precisión muy distinta. |
| [096](../classes/part-04-matematica-discreta-para-computacion/096-dag-y-orden-topologico/README.md) | DAG y orden topológico | `topological_order` | Orden topológico y detección de ciclos por conteo de Kahn. |
| [114](../classes/part-05-algebra-lineal-i-vectores-y-matrices/114-eliminacion-de-gauss/README.md) | Eliminación de Gauss | `gaussian_elimination_demo` | Eliminación de Gauss con pivoteo parcial, paso a paso. |
| [223](../classes/part-11-metodos-numericos-y-computacion-cientifica/223-newton-raphson/README.md) | Newton-Raphson | `newton_raphson` | Newton: convergencia cuadrática cerca de la raíz. |

```bash
compmath run 029
compmath run 032
compmath run 096
compmath run 114
compmath run 223
```

## Partes omitidas

Esta ruta **no** cubre: 00, 03, 06, 07, 08, 09, 10, 12, 13, 14, 15, 16, 17.

Omitir una parte es una decisión, no un descuento: si un ejercicio te bloquea porque
falta un concepto de una parte omitida, vuelve a ella. La tabla de prerrequisitos está
en [docs/LEARNING_PATH.md](../docs/LEARNING_PATH.md).

## Criterio de avance

- [ ] ≥ 80 % de los ejercicios básicos de cada parte;
- [ ] al menos 15 de los 20 laboratorios de cada parte, con predicción escrita previa;
- [ ] el capstone de cada parte entregado;
- [ ] las cinco preguntas de comprobación respondidas sin mirar el código.

```bash
compmath run --part 01 --quiet
compmath run --part 02 --quiet
compmath run --part 04 --quiet
compmath run --part 05 --quiet
compmath run --part 11 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
