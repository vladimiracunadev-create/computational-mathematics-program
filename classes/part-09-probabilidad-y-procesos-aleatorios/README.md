# Parte 09 — Probabilidad y procesos aleatorios

**Nivel:** universitario
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part09.py`

Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.

## 🧠 Ideas centrales

- P(A|B) y P(B|A) no son intercambiables: confundirlas es la falacia del fiscal.
- La esperanza es lineal siempre; la varianza solo bajo independencia.
- El TCL explica por qué la normal aparece incluso sin normalidad de origen.
- Monte Carlo convierge como 1/√n: cuadruplicar muestras solo duplica la precisión.
- Una cadena de Markov ergódica olvida su estado inicial.

## 🤖 Por qué importa en IA

Un modelo de lenguaje es una distribución condicional sobre el siguiente token; la difusión es un proceso estocástico con reverso aprendido.

## ⚠️ Errores frecuentes

- Asumir independencia sin justificarla.
- Ignorar la probabilidad base al interpretar un test positivo.
- Reportar resultados Monte Carlo sin semilla ni intervalo.

## 🧰 Stack de referencia

`random`, `statistics`, `math`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [181 — Experimentos, espacio muestral y eventos](181-experimentos-espacio-muestral-y-eventos/README.md)
2. [182 — Axiomas de probabilidad](182-axiomas-de-probabilidad/README.md)
3. [183 — Reglas de suma y producto](183-reglas-de-suma-y-producto/README.md)
4. [184 — Probabilidad condicional](184-probabilidad-condicional/README.md)
5. [185 — Independencia](185-independencia/README.md)
6. [186 — Teorema de Bayes](186-teorema-de-bayes/README.md)
7. [187 — Variables aleatorias discretas](187-variables-aleatorias-discretas/README.md)
8. [188 — Variables aleatorias continuas](188-variables-aleatorias-continuas/README.md)
9. [189 — Esperanza matemática](189-esperanza-matematica/README.md)
10. [190 — Varianza y desviación estándar](190-varianza-y-desviacion-estandar/README.md)
11. [191 — Covarianza y correlación](191-covarianza-y-correlacion/README.md)
12. [192 — Bernoulli y binomial](192-bernoulli-y-binomial/README.md)
13. [193 — Poisson y exponencial](193-poisson-y-exponencial/README.md)
14. [194 — Distribución normal](194-distribucion-normal/README.md)
15. [195 — Distribuciones conjuntas y marginales](195-distribuciones-conjuntas-y-marginales/README.md)
16. [196 — Ley de los grandes números](196-ley-de-los-grandes-numeros/README.md)
17. [197 — Teorema central del límite](197-teorema-central-del-limite/README.md)
18. [198 — Métodos Monte Carlo](198-metodos-monte-carlo/README.md)
19. [199 — Cadenas de Markov](199-cadenas-de-markov/README.md)
20. [200 — Capstone: simulador probabilístico y bayesiano](200-capstone-simulador-probabilistico-y-bayesiano/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 09
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Ross, S. *A First Course in Probability*. 10ª ed., Pearson, 2018.
- Blitzstein, J.; Hwang, J. *Introduction to Probability*. 2ª ed., CRC, 2019.
- Durrett, R. *Probability: Theory and Examples*. 5ª ed., Cambridge, 2019.
