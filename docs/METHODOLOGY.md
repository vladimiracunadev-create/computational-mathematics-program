# Metodología

Por qué el programa está diseñado así y qué se sacrificó a cambio.

## El problema que intenta resolver

La mayoría del material de «matemática para IA» falla de una de estas dos formas:

1. **Demasiado formal.** Empieza en espacios vectoriales abstractos y pierde a quien
   necesitaba entender por qué `0.1 + 0.2 != 0.3`.
2. **Demasiado superficial.** Enseña a llamar `model.fit()` y llama a eso «entender el
   gradiente».

Este programa apuesta por un tercer camino: **procedimiento visible**. Cada concepto se
implementa a mano, en Python legible, antes de mencionar la biblioteca que lo resuelve.

## Los cinco compromisos

### 1. Nada de placeholders

Toda clase apunta a una demostración real, ejecutable y determinista. `compmath run --all`
ejecuta las 360 y falla si alguna deja de funcionar. Un repositorio educativo que afirma
contenidos que no existen es peor que uno pequeño.

### 2. Cero dependencias para aprender

Los 18 motores usan solo biblioteca estándar. Motivos:

- **Accesibilidad**: funciona en cualquier máquina, incluso sin permisos de instalación.
- **Transparencia**: `numpy.linalg.svd` es una caja negra excelente y un pésimo material
  didáctico. La SVD implementada en 30 líneas legibles enseña qué hace.
- **Robustez de CI**: 3 sistemas operativos × 3 versiones de Python sin conflictos de
  compilación.

El coste es real: los motores son órdenes de magnitud más lentos que NumPy y están
declarados como no aptos para producción.

### 3. Predicción antes que resultado

Cada clase exige escribir tres predicciones antes de ejecutar nada. Es el único
mecanismo barato que distingue comprensión de familiaridad. Sin él, ver el resultado
produce la sensación de haberlo entendido —lo que la literatura llama *ilusión de
fluidez*— sin el hecho.

### 4. Verificación dentro del resultado

Las demostraciones no solo calculan: devuelven claves que **comprueban invariantes**.

```python
{
  "raiz_pequena_ingenua": ...,
  "raiz_pequena_estable": ...,
  "producto_raices_ingenua": ...,
  "producto_teorico_c/a": ...,      # ← el invariante que delata cuál falla
}
```

Esto convierte cada laboratorio en un test y hace que la afirmación de la clase sea
falsable por el propio estudiante.

### 5. Límites declarados

Cada parte, cada clase y el README declaran qué **no** cubren. Un programa educativo que
no dice dónde termina su alcance entrena a confiar de más.

## Las tres capas de todo objeto matemático

El programa insiste en separar, en cada clase:

| Capa | Pregunta | Fallo típico |
|---|---|---|
| **Modelo** | ¿qué dice la matemática ideal? | supuestos no declarados |
| **Algoritmo** | ¿qué procedimiento la calcula? | complejidad y criterio de parada |
| **Representación** | ¿qué bits la almacenan? | redondeo, cancelación, desbordamiento |

Casi todo error práctico en computación científica y en ML es una confusión entre estas
tres capas. La parte 01 existe enteramente para instalar esta distinción antes de que
aparezcan derivadas o matrices.

## Progresión: por qué este orden

```text
00-01  representación numérica   →  sin esto, todo resultado posterior es un número sin auditar
02-03  funciones y geometría     →  el vocabulario mínimo para leer cualquier fórmula
04     discreta                  →  demostración, conteo y grafos: la base de la probabilidad
05-06  álgebra lineal            →  el objeto central de todo modelo moderno
07-08  cálculo y autodiff        →  el mecanismo de entrenamiento, sin magia
09-10  probabilidad y estadística→  cómo se decide si un resultado significa algo
11     métodos numéricos         →  cómo se calcula lo que no tiene forma cerrada
12     optimización              →  cómo aprende un modelo
13     información y señales     →  la función de pérdida y la convolución
14-16  ML, DL y frontera aplicada→  todo lo anterior, aplicado
17     frontera de investigación →  qué se está construyendo ahora
```

La regla de dependencia: **ninguna parte usa un concepto que no haya introducido una
parte anterior**. La única excepción declarada son las bibliotecas científicas, que
aparecen como contraste sin ser prerrequisito.

## Por qué las clases se generan

360 clases escritas a mano divergen: unas quedan con seis secciones y otras con tres,
unas citan bibliografía y otras no, y las afirmaciones sobre conteos envejecen mal.

Generarlas desde `curriculum.yaml` garantiza que las 360 tengan el mismo contrato, que
sus referencias sean las de su parte y que sus salidas documentadas sean **las reales**
—el generador ejecuta cada demostración para leerlas.

El coste, declarado sin adornos: **no hay prosa única por clase**. La singularidad de
cada clase vive en su demostración ejecutable, en sus salidas y en la metadata de su
parte; no en un texto escrito a medida. Cerrar esa brecha es el objetivo de la v0.3.

## Reproducibilidad

- Todo lo aleatorio usa `random.Random(SEED)` con semilla fija y la declara en su salida.
- Ninguna demostración lee del reloj, de la red ni del sistema de archivos.
- Un test comprueba que dos ejecuciones devuelven exactamente el mismo diccionario.

Consecuencia honesta: los resultados «estadísticos» del programa son **ilustrativos de un
mecanismo**, no muestras de un experimento. Cuando importa, la propia demostración lo
dice.

## Evaluación

La rúbrica reparte 25/25/25/15/10 entre concepto, resolución manual, implementación,
comunicación y aplicación. El peso de la comunicación no es decorativo: el entregable de
cada clase exige un párrafo **sin código**. Explicar un resultado sin apoyarse en la
implementación es la prueba más barata de que se entendió el resultado y no el código.

## Qué haría distinto una versión académica formal

Este material se orienta a comprensión computacional. Una versión académica formal
añadiría demostraciones de existencia y unicidad, análisis en espacios de Banach y
Hilbert, teoría de la medida bajo la probabilidad, y convergencia con cotas explícitas.
Nada de eso está aquí, y esa ausencia es una decisión, no un descuido: consulta la
[bibliografía](BIBLIOGRAPHY.md) de cada parte para esa profundidad.
