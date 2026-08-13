# 192 — Bernoulli y binomial

**Parte:** 09 — Probabilidad y procesos aleatorios
**Nivel:** universitario
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part09` · demostración `bernoulli_binomial`

## 🎯 Propósito

Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.

Esta clase concreta ese objetivo sobre **Bernoulli y binomial**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Bernoulli y binomial** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `bernoulli_binomial` del motor de la parte.
4. Interpretar las 9 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: reportar resultados monte carlo sin semilla ni intervalo.

## 🧠 Idea rectora de la parte 09

> La esperanza es lineal siempre; la varianza solo bajo independencia.

## 🧩 Qué calcula el laboratorio

`bernoulli_binomial` — De un ensayo a n ensayos: Bernoulli y binomial.

Salidas que devuelve:

- `p`
- `n`
- `media_teorica_np`
- `varianza_teorica_np(1-p)`
- `media_simulada`
- `pmf_k=3`
- `frecuencia_simulada_k=3`
- `suma_pmf`
- `P(X<=3)`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-09-probabilidad-y-procesos-aleatorios/192-bernoulli-y-binomial/lab.py
```

o desde la CLI del programa:

```bash
compmath run 192
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Asumir independencia sin justificarla.
- Ignorar la probabilidad base al interpretar un test positivo.
- Reportar resultados Monte Carlo sin semilla ni intervalo.

## 🤖 Conexión con IA

Un modelo de lenguaje es una distribución condicional sobre el siguiente token; la difusión es un proceso estocástico con reverso aprendido.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Ross, S. *A First Course in Probability*. 10ª ed., Pearson, 2018.
- Blitzstein, J.; Hwang, J. *Introduction to Probability*. 2ª ed., CRC, 2019.
- Durrett, R. *Probability: Theory and Examples*. 5ª ed., Cambridge, 2019.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
