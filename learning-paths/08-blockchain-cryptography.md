# Ruta 08 — Blockchain y criptografía

**Para quién:** Trabajas con criptografía y quieres su base en teoría de números y grafos.

**Objetivo:** Entender aritmética modular, colisiones y entropía como cotas, no como intuiciones.

| Métrica | Valor |
|---|---:|
| Partes | 4 de 18 |
| Clases | 80 de 360 |
| Horas estimadas | 320 |
| A 10 h/semana | ~32 semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 01 | [Aritmética computacional y representación numérica](../classes/part-01-aritmetica-computacional-y-representacion-numerica/README.md) | 20 | 80 h | basico-computacional |
| 04 | [Matemática discreta para computación](../classes/part-04-matematica-discreta-para-computacion/README.md) | 20 | 80 h | intermedio |
| 09 | [Probabilidad y procesos aleatorios](../classes/part-09-probabilidad-y-procesos-aleatorios/README.md) | 20 | 80 h | universitario |
| 13 | [Teoría de la información, señales y series](../classes/part-13-teoria-de-la-informacion-senales-y-series/README.md) | 20 | 80 h | avanzado |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [025](../classes/part-01-aritmetica-computacional-y-representacion-numerica/025-enteros-con-signo-y-complemento-a-dos/README.md) | Enteros con signo y complemento a dos | `twos_complement` | Representación de negativos en 8 bits. |
| [090](../classes/part-04-matematica-discreta-para-computacion/090-principio-del-palomar/README.md) | Principio del palomar | `pigeonhole` | Principio del palomar: colisiones garantizadas sin construirlas. |
| [098](../classes/part-04-matematica-discreta-para-computacion/098-aritmetica-modular/README.md) | Aritmética modular | `modular_arithmetic` | Aritmética modular: exponenciación rápida e inverso modular. |
| [099](../classes/part-04-matematica-discreta-para-computacion/099-numeros-primos-y-maximo-comun-divisor/README.md) | Números primos y máximo común divisor | `primes_gcd` | Criba, MCD por Euclides y su relación con el mínimo común múltiplo. |
| [262](../classes/part-13-teoria-de-la-informacion-senales-y-series/262-entropia-de-shannon/README.md) | Entropía de Shannon | `shannon_entropy` | La entropía es la sorpresa esperada y el límite de compresión. |

```bash
compmath run 025
compmath run 090
compmath run 098
compmath run 099
compmath run 262
```

## Partes omitidas

Esta ruta **no** cubre: 00, 02, 03, 05, 06, 07, 08, 10, 11, 12, 14, 15, 16, 17.

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
compmath run --part 04 --quiet
compmath run --part 09 --quiet
compmath run --part 13 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
