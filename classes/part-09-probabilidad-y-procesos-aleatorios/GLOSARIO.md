# 📖 Glosario — Parte 09: Probabilidad y procesos aleatorios

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

35 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Axiomas de Kolmogorov** | P(A) ≥ 0, P(Ω) = 1 y aditividad para eventos disjuntos. Toda la teoría se deduce de estos tres. | [182](182-axiomas-de-probabilidad/README.md) |
| **Cadena de Markov** | Proceso donde el siguiente estado depende solo del actual, no de la historia previa. | [199](199-cadenas-de-markov/README.md) |
| **Conjugación** | Prior y posterior de la misma familia. Beta es conjugada de la binomial y la actualización es sumar. | [200](200-capstone-simulador-probabilistico-y-bayesiano/README.md) |
| **Corrección de Bessel** | Dividir entre n−1 en vez de n para que la varianza muestral sea un estimador insesgado. | [190](190-varianza-y-desviacion-estandar/README.md) |
| **Correlación de Pearson** | Covarianza normalizada por las desviaciones. Vive en [−1, 1] y solo detecta relación lineal. | [191](191-covarianza-y-correlacion/README.md) |
| **Covarianza** | E[(X−μₓ)(Y−μᵧ)]. Mide variación conjunta; su valor depende de las unidades. | [191](191-covarianza-y-correlacion/README.md) |
| **Distribución binomial** | Número de éxitos en n ensayos independientes. Media np, varianza np(1−p). | [192](192-bernoulli-y-binomial/README.md) |
| **Distribución conjunta** | Probabilidad de pares de valores. De ella se obtienen marginales sumando y condicionales dividiendo. | [195](195-distribuciones-conjuntas-y-marginales/README.md) |
| **Distribución de Poisson** | Cuenta eventos raros en un intervalo. Su media y su varianza valen ambas λ. | [193](193-poisson-y-exponencial/README.md) |
| **Distribución estacionaria** | Vector π que cumple πP = π. Una cadena ergódica converge a él desde cualquier inicio. | [199](199-cadenas-de-markov/README.md) |
| **Distribución marginal** | Distribución de una variable obtenida sumando la conjunta sobre la otra. | [195](195-distribuciones-conjuntas-y-marginales/README.md) |
| **Distribución normal** | Campana simétrica definida por μ y σ. Regla 68-95-99,7 dentro de una, dos y tres desviaciones. | [194](194-distribucion-normal/README.md) |
| **Ensayo de Bernoulli** | Experimento con dos resultados y probabilidad p de éxito. Ladrillo de la binomial. | [192](192-bernoulli-y-binomial/README.md) |
| **Error estándar** | σ/√n. Desviación estándar de la media muestral; cae como la raíz del tamaño. | [197](197-teorema-central-del-limite/README.md) |
| **Espacio muestral** | Conjunto Ω de todos los resultados posibles de un experimento. Se escribe antes que cualquier cálculo. | [181](181-experimentos-espacio-muestral-y-eventos/README.md) |
| **Esperanza** | E[X] = Σ x·P(X=x). Media ponderada por probabilidad; es lineal incluso sin independencia. | [189](189-esperanza-matematica/README.md) |
| **Evento** | Subconjunto del espacio muestral. Ocurre si el resultado observado pertenece a él. | [181](181-experimentos-espacio-muestral-y-eventos/README.md) |
| **Experimento aleatorio** | Procedimiento cuyo resultado no se puede predecir individualmente, pero sí describir en conjunto. | [181](181-experimentos-espacio-muestral-y-eventos/README.md) |
| **Falacia del jugador** | Creer que los resultados pasados compensan a los futuros. La moneda no tiene memoria. | [196](196-ley-de-los-grandes-numeros/README.md) |
| **Falta de memoria** | Propiedad de la exponencial y la geométrica: P(X > s+t | X > s) = P(X > t). | [193](193-poisson-y-exponencial/README.md) |
| **Función de densidad** | pdf. Su integral sobre un intervalo da la probabilidad. Puede superar 1 sin contradicción. | [188](188-variables-aleatorias-continuas/README.md) |
| **Función de distribución** | cdf. F(x) = P(X ≤ x). Es no decreciente y va de 0 a 1. | [188](188-variables-aleatorias-continuas/README.md) |
| **Función de masa** | pmf. Asigna a cada valor discreto su probabilidad; todas suman 1. | [187](187-variables-aleatorias-discretas/README.md) |
| **Inclusión-exclusión** | P(A∪B) = P(A) + P(B) − P(A∩B). El término restado corrige el solapamiento contado dos veces. | [183](183-reglas-de-suma-y-producto/README.md) |
| **Independencia** | A y B son independientes si P(A∩B) = P(A)·P(B). Se comprueba, no se supone. | [185](185-independencia/README.md) |
| **Ley de los grandes números** | La media muestral converge a la esperanza cuando n crece. No dice nada de una muestra concreta. | [196](196-ley-de-los-grandes-numeros/README.md) |
| **Monte Carlo** | Estimar cantidades por muestreo aleatorio. Su error cae como 1/√n en cualquier dimensión. | [198](198-metodos-monte-carlo/README.md) |
| **Prior y posterior** | Creencia antes y después de ver datos. Bayes es la regla que lleva de una a otra. | [200](200-capstone-simulador-probabilistico-y-bayesiano/README.md) |
| **Probabilidad base** | Prevalencia del evento antes de ver evidencia. Ignorarla es la falacia de la tasa base. | [186](186-teorema-de-bayes/README.md) |
| **Probabilidad condicional** | P(A|B) = P(A∩B)/P(B). Es la probabilidad de A dentro del espacio reducido a B. | [184](184-probabilidad-condicional/README.md) |
| **Puntuación z** | z = (x − μ)/σ. Expresa un valor en desviaciones estándar y permite comparar escalas distintas. | [194](194-distribucion-normal/README.md) |
| **Teorema central del límite** | La media de n variables iid tiende a una normal de media μ y desviación σ/√n. | [197](197-teorema-central-del-limite/README.md) |
| **Teorema de Bayes** | P(H|E) = P(E|H)·P(H)/P(E). Invierte el condicionamiento y actualiza una creencia con evidencia. | [186](186-teorema-de-bayes/README.md) |
| **Variable aleatoria** | Función que asigna un número a cada resultado del espacio muestral. Ni es variable ni es aleatoria. | [187](187-variables-aleatorias-discretas/README.md) |
| **Varianza** | Var(X) = E[(X−μ)²] = E[X²] − E[X]². Mide dispersión en unidades al cuadrado. | [190](190-varianza-y-desviacion-estandar/README.md) |

## Cómo usar este glosario

No memorices las definiciones: **usa la columna de clase**. Un término se entiende cuando
puedes ejecutar su demostración y explicar qué comprueba, no cuando puedes recitar su
definición.

```bash
compmath show <clase>    # ficha de la clase donde vive el término
compmath run <clase>     # ejecutar su demostración
```

---

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md)
