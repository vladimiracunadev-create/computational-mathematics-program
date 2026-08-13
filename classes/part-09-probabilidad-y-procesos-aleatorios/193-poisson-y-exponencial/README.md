# 193 — Poisson y exponencial

**Parte:** 09 — Probabilidad y procesos aleatorios
**Nivel:** universitario
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part09` · demostración `poisson_exponential`

## 🎯 Propósito

Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.

Esta clase concreta ese objetivo sobre **Poisson y exponencial**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Poisson y exponencial** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `poisson_exponential` del motor de la parte.
4. Interpretar las 8 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: asumir independencia sin justificarla.

## 🧠 Idea rectora de la parte 09

> El TCL explica por qué la normal aparece incluso sin normalidad de origen.

## 🧩 Qué calcula el laboratorio

`poisson_exponential` — Poisson cuenta eventos; la exponencial mide el tiempo entre ellos.

Salidas que devuelve:

- `λ_eventos_por_hora`
- `P(N=0)`
- `P(N=3)`
- `media_poisson`
- `varianza_poisson`
- `media_de_la_espera_1/λ`
- `media_de_espera_simulada`
- `sin_memoria`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-09-probabilidad-y-procesos-aleatorios/193-poisson-y-exponencial/lab.py
```

o desde la CLI del programa:

```bash
compmath run 193
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
