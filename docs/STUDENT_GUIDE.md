# Guía del estudiante

## Antes de empezar

Este programa asume **cero base matemática** y **algo de Python** (saber ejecutar un
script y leer un `for`). Si no tienes ni eso, empieza por la parte 00 igualmente: los
laboratorios se ejecutan con un solo comando.

```bash
pip install -e .
compmath stats
compmath run 001
```

## Cómo se estudia una clase

El orden importa. Saltarse el paso 2 es el error más común y el más caro.

| # | Paso | Archivo | Tiempo |
|--:|---|---|---|
| 1 | Leer el propósito y los resultados esperados | `README.md` | 10 min |
| 2 | **Escribir tu predicción** de los tres casos | `intuition.md` | 15 min |
| 3 | Estudiar el modelo y sus tres capas | `theory.md` | 30 min |
| 4 | Derivar a mano, paso por paso | `derivation.md` | 40 min |
| 5 | Ejecutar el laboratorio y comparar con tu predicción | `lab.py` | 20 min |
| 6 | Resolver el notebook de estudiante | `notebook_student.ipynb` | 60 min |
| 7 | Contrastar con la solución de referencia | `notebook_solution.ipynb` | 20 min |
| 8 | Hacer los ejercicios y autoevaluarte | `exercises.md`, `assessment.md` | 45 min |

Total: **unas 4 horas por clase**. 360 clases ≈ 1440 horas.

## La regla de la predicción

Antes de ejecutar cualquier laboratorio, escribe:

1. **Caso normal** — qué esperas que salga.
2. **Caso límite** — qué pasa en el borde del dominio.
3. **Caso inválido** — qué debería ocurrir con una entrada fuera de dominio.

Un resultado que confirma tu predicción enseña tanto como uno que la contradice, **pero
solo si la predicción existía antes**. Ejecutar primero y explicar después produce la
sensación de haber entendido sin el hecho de haber entendido.

## Cómo saber que una clase está superada

Responde estas cinco preguntas sin volver a mirar el código:

1. ¿Cuál es la entrada, cuál la salida, y qué unidades tienen?
2. ¿Qué operación domina el comportamiento del resultado?
3. ¿Qué caso extremo revelaría un error conceptual?
4. ¿Cómo verificarías el resultado por un método independiente?
5. ¿Dónde aparece esto en una aplicación real?

Si necesitas releer el código para contestar, la clase **no** está superada.

## Ritmos sugeridos

| Perfil | Dedicación | Duración estimada |
|---|---|---|
| Intensivo (dedicación completa) | 25 h/semana | ~14 meses |
| Sostenido (con trabajo) | 10 h/semana | ~2,8 años |
| Ligero (constante) | 5 h/semana | ~5,5 años |

Es mucho, y es honesto decirlo. Nadie termina 360 clases en un trimestre.

## Si tienes poco tiempo: rutas cortas

No hace falta hacer las 18 partes. Consulta [LEARNING_PATH.md](LEARNING_PATH.md) y las
[rutas por perfil](../learning-paths/). Ejemplos:

| Objetivo | Partes mínimas | Clases |
|---|---|---|
| Entender backpropagation | 05, 07, 08, 15 | 80 |
| Leer papers de Transformers | 05, 06, 08, 09, 13, 16 | 120 |
| Ciencia de datos aplicada | 00, 02, 05, 09, 10, 14 | 120 |
| Métodos numéricos e ingeniería | 01, 05, 07, 11, 12 | 100 |

## Herramientas del programa

```bash
compmath catalog --part 09     # ver una parte completa
compmath show 197              # ficha de una clase concreta
compmath run 197               # ejecutar su laboratorio
compmath run --part 09         # las 20 clases de la parte
compmath progress              # tu avance
compmath progress --done 197   # marcar una clase como completada
```

El progreso se guarda en `.compmath-progress.json`, es local y no se sincroniza. El
portal web tiene su propio marcador, guardado en el navegador.

## Errores de estudio más costosos

1. **Leer sin ejecutar.** El repositorio no es un libro; los laboratorios están para
   contradecirte.
2. **Ejecutar sin predecir.** Ver el resultado primero destruye el valor del ejercicio.
3. **Aceptar un número sin tolerancia.** Todo resultado numérico necesita saber a qué
   distancia está del valor exacto.
4. **Avanzar con un prerrequisito flojo.** La parte 08 se hunde sin la 07; la 16 sin la 05.
5. **Copiar la solución antes de intentarlo.** El notebook de solución existe para
   contrastar, no para partir de él.
6. **Confundir «me suena» con «lo sé».** Las cinco preguntas de arriba discriminan las dos.

## Qué hacer cuando te atascas

1. Reduce el problema al caso más pequeño posible (2×2, n=3, un solo paso).
2. Ejecuta el laboratorio cambiando **una sola** entrada y observa qué se mueve.
3. Lee el motor de la parte: `src/computational_math/engines/partNN.py`.
4. Busca la clase anterior que introdujo el concepto que te falta.
5. Pregunta en Discussions citando el número de clase y qué esperabas frente a qué obtuviste.

## Límites que debes conocer

- Este programa **no acredita nada**. No emite certificados ni convalida estudios.
- Las derivaciones se orientan a comprensión computacional, no a rigor de análisis
  funcional o teoría de la medida.
- Los datos de los laboratorios son sintéticos: demuestran el mecanismo, no describen
  el mundo.
- Los motores son legibles, no rápidos. No los uses en producción.
