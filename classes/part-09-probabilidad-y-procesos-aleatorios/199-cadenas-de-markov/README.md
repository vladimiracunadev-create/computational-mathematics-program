# 199 — Cadenas de Markov

> [⬅️ 198 Métodos Monte Carlo](../198-metodos-monte-carlo/README.md) · [📚 Parte 09](../README.md) · [🏠 Programa](../../../README.md) · [200 Capstone: simulador probabilístico y bayesiano ➡️](../200-capstone-simulador-probabilistico-y-bayesiano/README.md)

**Parte:** 09 — Probabilidad y procesos aleatorios · **Nivel:** `universitario` · **Horas estimadas:** 4
**Motor:** `engines.part09` · **Demostración:** `markov_chains` · **Clase 19 de 20** de la parte

---

## 🎯 Propósito

Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.

Esta clase concreta ese objetivo sobre **Cadenas de Markov**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Cadenas de Markov** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `markov_chains`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: asumir independencia sin justificarla.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["198<br/>Métodos Monte Carlo"] --> C
    subgraph C["199 · Cadenas de Markov"]
        direction TB
        D["Demostración<br/><code>markov_chains</code>"] --> R["Resultados numéricos<br/>—"]
        D --> V["Verificaciones<br/>filas_suman_1<br/>converge<br/>olvida_el_estado_inicial"]
        D --> O["Contexto y estructura<br/>matriz_de_transicion<br/>estado_inicial<br/>trayectoria<br/>… +2 más"]
    end
    C --> N["200<br/>Capstone: simulador<br/>probabilístico y<br/>bayesiano"]
    C -.-> IA["Uso en IA<br/>parte 09"]
```

## 🧠 Idea rectora de la parte 09

> Monte Carlo convierge como 1/√n: cuadruplicar muestras solo duplica la precisión.

## 🔬 Qué ejecuta el laboratorio

`markov_chains` — Cadena de Markov: matriz de transición y distribución estacionaria.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (0) | — |
| ✅ Comprobaciones de invariante (3) | `filas_suman_1`, `converge`, `olvida_el_estado_inicial` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-09-probabilidad-y-procesos-aleatorios/199-cadenas-de-markov/lab.py
compmath run 199
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Asumir independencia sin justificarla.
- Ignorar la probabilidad base al interpretar un test positivo.
- Reportar resultados Monte Carlo sin semilla ni intervalo.

## 🤖 Conexión con IA

Un modelo de lenguaje es una distribución condicional sobre el siguiente token; la difusión es un proceso estocástico con reverso aprendido.

## 📓 Notebooks

| Archivo | Para qué |
|---|---|
| [`notebook.ipynb`](notebook.ipynb) | recorrido guiado con la demostración ejecutada |
| [`notebook_student.ipynb`](notebook_student.ipynb) | versión con `TODO` para resolver |
| [`notebook_solution.ipynb`](notebook_solution.ipynb) | solución de referencia verificada |

## 📝 Evaluación

| Criterio | Peso |
|---|---:|
| Comprensión conceptual | 25 % |
| Resolución manual | 25 % |
| Implementación y verificación | 25 % |
| Interpretación y comunicación | 15 % |
| Conexión con aplicación real | 10 % |

Detalle y criterios de error crítico en [`assessment.md`](assessment.md).

## ❓ Preguntas de comprobación

1. ¿Cuál es la entrada, cuál la salida y qué unidades tienen?
2. ¿Qué operación domina el comportamiento del resultado?
3. ¿Qué caso extremo revelaría un error conceptual?
4. ¿Cómo verificarías el resultado por un método independiente?
5. ¿Dónde aparece esto en riesgo?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Ross, S. *A First Course in Probability*. 10ª ed., Pearson, 2018.
- Blitzstein, J.; Hwang, J. *Introduction to Probability*. 2ª ed., CRC, 2019.
- Durrett, R. *Probability: Theory and Examples*. 5ª ed., Cambridge, 2019.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 198 Métodos Monte Carlo](../198-metodos-monte-carlo/README.md) · [📚 Parte 09](../README.md) · [🏠 Programa](../../../README.md) · [200 Capstone: simulador probabilístico y bayesiano ➡️](../200-capstone-simulador-probabilistico-y-bayesiano/README.md)
