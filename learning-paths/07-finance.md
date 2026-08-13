# Ruta 07 — Finanzas cuantitativas

**Para quién:** Modelas riesgo, carteras o precios y necesitas la matemática debajo.

**Objetivo:** Modelar incertidumbre con dinero exacto, simulación y optimización con restricciones.

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
| 01 | [Aritmética computacional y representación numérica](../classes/part-01-aritmetica-computacional-y-representacion-numerica/README.md) | 20 | 80 h | basico-computacional |
| 07 | [Cálculo diferencial e integral](../classes/part-07-calculo-diferencial-e-integral/README.md) | 20 | 80 h | universitario |
| 09 | [Probabilidad y procesos aleatorios](../classes/part-09-probabilidad-y-procesos-aleatorios/README.md) | 20 | 80 h | universitario |
| 10 | [Estadística e inferencia](../classes/part-10-estadistica-e-inferencia/README.md) | 20 | 80 h | universitario-avanzado |
| 12 | [Optimización matemática y computacional](../classes/part-12-optimizacion-matematica-y-computacional/README.md) | 20 | 80 h | avanzado |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [005](../classes/part-00-pensamiento-matematico-desde-cero/005-porcentajes-desde-cero/README.md) | Porcentajes desde cero | `percentage` | Aumento y descuento sucesivos: el orden no cambia, la reversión sí. |
| [037](../classes/part-01-aritmetica-computacional-y-representacion-numerica/037-precision-arbitraria-y-decimal/README.md) | Precisión arbitraria y Decimal | `arbitrary_precision` | Decimal con precisión declarada frente a float. |
| [194](../classes/part-09-probabilidad-y-procesos-aleatorios/194-distribucion-normal/README.md) | Distribución normal | `normal_distribution` | Normal: regla 68-95-99.7 y estandarización. |
| [198](../classes/part-09-probabilidad-y-procesos-aleatorios/198-metodos-monte-carlo/README.md) | Métodos Monte Carlo | `monte_carlo` | Estimar π por Monte Carlo con su error e intervalo. |
| [218](../classes/part-10-estadistica-e-inferencia/218-bootstrap-y-remuestreo/README.md) | Bootstrap y remuestreo | `bootstrap` | Bootstrap: estimar la variabilidad sin suponer la distribución. |
| [258](../classes/part-12-optimizacion-matematica-y-computacional/258-optimizacion-cuadratica/README.md) | Optimización cuadrática | `quadratic_programming` | Programa cuadrático resuelto por su sistema KKT. |

```bash
compmath run 005
compmath run 037
compmath run 194
compmath run 198
compmath run 218
compmath run 258
```

## Partes omitidas

Esta ruta **no** cubre: 02, 03, 04, 05, 06, 08, 11, 13, 14, 15, 16, 17.

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
compmath run --part 07 --quiet
compmath run --part 09 --quiet
compmath run --part 10 --quiet
compmath run --part 12 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
