# 🎲 Parte 09 — Probabilidad y procesos aleatorios

> [⬅️ Parte 08 — Cálculo multivariable, matricial y autodiferenciación](../part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 10 — Estadística e inferencia ➡️](../part-10-estadistica-e-inferencia/README.md)

**Nivel:** `universitario` · **Clases:** 20 · **Horas estimadas:** 80 · **Motor:** [`part09.py`](../../src/computational_math/engines/part09.py)

---

## 🎯 De qué trata esta parte

Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.

## 🧠 Ideas centrales

- P(A|B) y P(B|A) no son intercambiables: confundirlas es la falacia del fiscal.
- La esperanza es lineal siempre; la varianza solo bajo independencia.
- El TCL explica por qué la normal aparece incluso sin normalidad de origen.
- Monte Carlo convierge como 1/√n: cuadruplicar muestras solo duplica la precisión.
- Una cadena de Markov ergódica olvida su estado inicial.

## 🤖 Por qué importa en IA

> [!IMPORTANT]
> Un modelo de lenguaje es una distribución condicional sobre el siguiente token; la difusión es un proceso estocástico con reverso aprendido.

## ⚠️ Errores frecuentes de esta parte

- Asumir independencia sin justificarla.
- Ignorar la probabilidad base al interpretar un test positivo.
- Reportar resultados Monte Carlo sin semilla ni intervalo.

## 🧭 Secuencia de la parte

```mermaid
flowchart LR
    subgraph B1["Bloque 1"]
        direction TB
        L181["181 · Experimentos, espacio…"]
        L182["182 · Axiomas de probabilidad"]
        L183["183 · Reglas de suma y producto"]
        L184["184 · Probabilidad condicional"]
        L185["185 · Independencia"]
        L181 --> L182
        L182 --> L183
        L183 --> L184
        L184 --> L185
    end
    subgraph B2["Bloque 2"]
        direction TB
        L186["186 · Teorema de Bayes"]
        L187["187 · Variables aleatorias discretas"]
        L188["188 · Variables aleatorias continuas"]
        L189["189 · Esperanza matemática"]
        L190["190 · Varianza y desviación estándar"]
        L186 --> L187
        L187 --> L188
        L188 --> L189
        L189 --> L190
    end
    subgraph B3["Bloque 3"]
        direction TB
        L191["191 · Covarianza y correlación"]
        L192["192 · Bernoulli y binomial"]
        L193["193 · Poisson y exponencial"]
        L194["194 · Distribución normal"]
        L195["195 · Distribuciones conjuntas y…"]
        L191 --> L192
        L192 --> L193
        L193 --> L194
        L194 --> L195
    end
    subgraph B4["Bloque 4"]
        direction TB
        L196["196 · Ley de los grandes números"]
        L197["197 · Teorema central del límite"]
        L198["198 · Métodos Monte Carlo"]
        L199["199 · Cadenas de Markov"]
        L200["200 · Capstone: simulador…"]
        L196 --> L197
        L197 --> L198
        L198 --> L199
        L199 --> L200
    end
    L185 --> L186
    L190 --> L191
    L195 --> L196
```

## 📚 Las clases

| # | Clase | Demostración | Idea central |
|---|---|---|---|
| `181` | [Experimentos, espacio muestral y eventos](181-experimentos-espacio-muestral-y-eventos/README.md) | `sample_space` | Espacio muestral, eventos y su probabilidad en un modelo equiprobable. |
| `182` | [Axiomas de probabilidad](182-axiomas-de-probabilidad/README.md) | `axioms` | Los tres axiomas de Kolmogorov verificados sobre un modelo. |
| `183` | [Reglas de suma y producto](183-reglas-de-suma-y-producto/README.md) | `sum_product_rules` | Regla de la suma con y sin exclusión mutua. |
| `184` | [Probabilidad condicional](184-probabilidad-condicional/README.md) | `conditional` | P(A|B) cambia el espacio muestral, no la realidad. |
| `185` | [Independencia](185-independencia/README.md) | `independence` | Independencia se comprueba, no se supone. |
| `186` | [Teorema de Bayes](186-teorema-de-bayes/README.md) | `bayes` | Test médico: por qué un positivo no significa enfermedad. |
| `187` | [Variables aleatorias discretas](187-variables-aleatorias-discretas/README.md) | `discrete_rv` | Variable aleatoria discreta: pmf, cdf y coherencia. |
| `188` | [Variables aleatorias continuas](188-variables-aleatorias-continuas/README.md) | `continuous_rv` | Variable continua: la densidad no es una probabilidad. |
| `189` | [Esperanza matemática](189-esperanza-matematica/README.md) | `expectation` | Linealidad de la esperanza, incluso sin independencia. |
| `190` | [Varianza y desviación estándar](190-varianza-y-desviacion-estandar/README.md) | `variance` | Varianza, desviación estándar y el estimador insesgado. |
| `191` | [Covarianza y correlación](191-covarianza-y-correlacion/README.md) | `covariance_correlation` | Covarianza depende de la escala; la correlación no. |
| `192` | [Bernoulli y binomial](192-bernoulli-y-binomial/README.md) | `bernoulli_binomial` | De un ensayo a n ensayos: Bernoulli y binomial. |
| `193` | [Poisson y exponencial](193-poisson-y-exponencial/README.md) | `poisson_exponential` | Poisson cuenta eventos; la exponencial mide el tiempo entre ellos. |
| `194` | [Distribución normal](194-distribucion-normal/README.md) | `normal_distribution` | Normal: regla 68-95-99.7 y estandarización. |
| `195` | [Distribuciones conjuntas y marginales](195-distribuciones-conjuntas-y-marginales/README.md) | `joint_marginal` | Distribución conjunta, marginales y condicional. |
| `196` | [Ley de los grandes números](196-ley-de-los-grandes-numeros/README.md) | `law_large_numbers` | La media muestral converge, pero lentamente. |
| `197` | [Teorema central del límite](197-teorema-central-del-limite/README.md) | `central_limit` | El TCL en acción sobre una distribución claramente no normal. |
| `198` | [Métodos Monte Carlo](198-metodos-monte-carlo/README.md) | `monte_carlo` | Estimar π por Monte Carlo con su error e intervalo. |
| `199` | [Cadenas de Markov](199-cadenas-de-markov/README.md) | `markov_chains` | Cadena de Markov: matriz de transición y distribución estacionaria. |
| `200` | [Capstone: simulador probabilístico y bayesiano](200-capstone-simulador-probabilistico-y-bayesiano/README.md) | `capstone_probabilistic_simulator` | Capstone: simulador probabilístico con actualización bayesiana. |

## 🧰 Stack de referencia

`random`, `statistics`, `math`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen
como contraste profesional, no como requisito.

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 09
compmath catalog --part 09
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone ([200](200-capstone-simulador-probabilistico-y-bayesiano/README.md)) | 20 % |

## 📖 Bibliografía

- Ross, S. *A First Course in Probability*. 10ª ed., Pearson, 2018.
- Blitzstein, J.; Hwang, J. *Introduction to Probability*. 2ª ed., CRC, 2019.
- Durrett, R. *Probability: Theory and Examples*. 5ª ed., Cambridge, 2019.

---

> [⬅️ Parte 08 — Cálculo multivariable, matricial y autodiferenciación](../part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 10 — Estadística e inferencia ➡️](../part-10-estadistica-e-inferencia/README.md)
