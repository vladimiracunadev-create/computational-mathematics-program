# Ruta 10 — Desarrollo de videojuegos

**Para quién:** Haces gráficos, física o IA de juego y necesitas la geometría exacta.

**Objetivo:** Construir un pipeline geométrico correcto y un integrador estable.

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
| 03 | [Geometría, trigonometría y geometría analítica](../classes/part-03-geometria-trigonometria-y-geometria-analitica/README.md) | 20 | 80 h | basico-intermedio |
| 05 | [Álgebra lineal I: vectores y matrices](../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 07 | [Cálculo diferencial e integral](../classes/part-07-calculo-diferencial-e-integral/README.md) | 20 | 80 h | universitario |
| 11 | [Métodos numéricos y computación científica](../classes/part-11-metodos-numericos-y-computacion-cientifica/README.md) | 20 | 80 h | cientifico |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [074](../classes/part-03-geometria-trigonometria-y-geometria-analitica/074-rotaciones-2d/README.md) | Rotaciones 2D | `rotation_2d` | Matriz de rotación: ortogonal y de determinante 1. |
| [077](../classes/part-03-geometria-trigonometria-y-geometria-analitica/077-geometria-3d-y-planos/README.md) | Geometría 3D y planos | `planes_3d` | Plano por su normal, distancia de un punto y producto cruz. |
| [078](../classes/part-03-geometria-trigonometria-y-geometria-analitica/078-proyecciones-y-perspectiva/README.md) | Proyecciones y perspectiva | `projection` | Proyección ortogonal de un vector y proyección en perspectiva. |
| [080](../classes/part-03-geometria-trigonometria-y-geometria-analitica/080-capstone-motor-geometrico-2d/README.md) | Capstone: motor geométrico 2D | `capstone_geometry_engine` | Capstone: motor 2D que compone transformaciones sobre un polígono. |
| [237](../classes/part-11-metodos-numericos-y-computacion-cientifica/237-runge-kutta/README.md) | Runge-Kutta | `runge_kutta` | RK4: cuatro evaluaciones por paso, error O(h⁴). |

```bash
compmath run 074
compmath run 077
compmath run 078
compmath run 080
compmath run 237
```

## Partes omitidas

Esta ruta **no** cubre: 00, 02, 04, 06, 08, 09, 10, 12, 13, 14, 15, 16, 17.

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
compmath run --part 03 --quiet
compmath run --part 05 --quiet
compmath run --part 07 --quiet
compmath run --part 11 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
