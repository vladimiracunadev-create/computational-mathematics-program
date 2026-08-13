# 190 — Varianza y desviación estándar

> [⬅️ 189 Esperanza matemática](../189-esperanza-matematica/README.md) · [📚 Parte 09](../README.md) · [🏠 Programa](../../../README.md) · [191 Covarianza y correlación ➡️](../191-covarianza-y-correlacion/README.md)

**Parte:** 09 — Probabilidad y procesos aleatorios · **Nivel:** `universitario` · **Horas estimadas:** 4
**Motor:** `engines.part09` · **Demostración:** `variance` · **Clase 10 de 20** de la parte

---

## 🎯 Propósito

Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.

Esta clase concreta ese objetivo sobre **Varianza y desviación estándar**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Varianza y desviación estándar** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `variance`.
4. Interpretar las 9 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: asumir independencia sin justificarla.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["Clase 189 · Esperanza matemática"] --> D
    subgraph CLASE["Clase 190 · Varianza y desviación estándar"]
        direction TB
        D["Demostracion variance"]
        D --> R["Resultados 7: media +6"]
        D --> V["Comprobaciones: ninguna"]
        D --> O["Contexto 2: datos +1"]
    end
    R --> N["Clase 191 · Covarianza y correlación"]
    V -.-> IA["Aplicacion en IA · parte 09"]
```

## 🧠 Idea rectora de la parte 09

> Una cadena de Markov ergódica olvida su estado inicial.

## 🔬 Qué ejecuta el laboratorio

`variance` — Varianza, desviación estándar y el estimador insesgado.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (7) | `media`, `varianza_poblacional_/n`, `varianza_muestral_/(n-1)`, `desviacion_estandar`, `statistics.pstdev`, `statistics.stdev`, `Var(aX)=a²Var(X)` |
| ✅ Comprobaciones de invariante (0) | — |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-09-probabilidad-y-procesos-aleatorios/190-varianza-y-desviacion-estandar/lab.py
compmath run 190
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

> [⬅️ 189 Esperanza matemática](../189-esperanza-matematica/README.md) · [📚 Parte 09](../README.md) · [🏠 Programa](../../../README.md) · [191 Covarianza y correlación ➡️](../191-covarianza-y-correlacion/README.md)
