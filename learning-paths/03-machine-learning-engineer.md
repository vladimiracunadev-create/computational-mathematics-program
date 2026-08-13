# Ruta 03 — Machine Learning

**Para quién:** Usas scikit-learn y quieres poder derivar lo que llamas.

**Objetivo:** Derivar seis algoritmos clásicos desde su función objetivo y compararlos.

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
| 07 | [Cálculo diferencial e integral](../classes/part-07-calculo-diferencial-e-integral/README.md) | 20 | 80 h | universitario |
| 09 | [Probabilidad y procesos aleatorios](../classes/part-09-probabilidad-y-procesos-aleatorios/README.md) | 20 | 80 h | universitario |
| 12 | [Optimización matemática y computacional](../classes/part-12-optimizacion-matematica-y-computacional/README.md) | 20 | 80 h | avanzado |
| 14 | [Matemática de Machine Learning](../classes/part-14-matematica-de-machine-learning/README.md) | 20 | 80 h | ml-avanzado |

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
| [131](../classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/131-minimos-cuadrados-lineales/README.md) | Mínimos cuadrados lineales | `least_squares` | Mínimos cuadrados por ecuaciones normales. |
| [215](../classes/part-10-estadistica-e-inferencia/215-maxima-verosimilitud/README.md) | Máxima verosimilitud | `maximum_likelihood` | MLE para la normal: la media muestral maximiza la verosimilitud. |
| [244](../classes/part-12-optimizacion-matematica-y-computacional/244-gradient-descent/README.md) | Gradient descent | `gradient_descent` | Descenso de gradiente y el efecto del learning rate. |
| [289](../classes/part-14-matematica-de-machine-learning/289-svm-y-margen-maximo/README.md) | SVM y margen máximo | `svm_margin` | SVM: maximizar el margen equivale a minimizar ‖w‖. |
| [300](../classes/part-14-matematica-de-machine-learning/300-capstone-derivar-y-comparar-6-algoritmos-ml/README.md) | Capstone: derivar y comparar 6 algoritmos ML | `capstone_six_algorithms` | Capstone: seis algoritmos derivados y comparados sobre los mismos datos. |

```bash
compmath run 131
compmath run 215
compmath run 244
compmath run 289
compmath run 300
```

## Partes omitidas

Esta ruta **no** cubre: 00, 01, 02, 03, 04, 06, 08, 10, 11, 13, 15, 16, 17.

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
compmath run --part 09 --quiet
compmath run --part 12 --quiet
compmath run --part 14 --quiet
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
