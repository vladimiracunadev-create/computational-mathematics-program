# 344 — Hamiltonian Monte Carlo

> [⬅️ 343 MCMC avanzado](../343-mcmc-avanzado/README.md) · [📚 Parte 17](../README.md) · [🏠 Programa](../../../README.md) · [345 Variational inference avanzada ➡️](../345-variational-inference-avanzada/README.md)

**Parte:** 17 — Frontera matemática para IA e investigación · **Nivel:** `frontera-investigacion` · **Horas estimadas:** 4
**Motor:** `engines.part17` · **Demostración:** `hamiltonian_monte_carlo` · **Clase 4 de 20** de la parte

---

## 🎯 Propósito

Procesos gaussianos, MCMC avanzado, inferencia variacional, transporte óptimo, geometría diferencial e informacional, SDE, Neural ODE, score matching y teoría del aprendizaje.

Esta clase concreta ese objetivo sobre **Hamiltonian Monte Carlo**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Hamiltonian Monte Carlo** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `hamiltonian_monte_carlo`.
4. Interpretar las 13 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: reportar resultados de mcmc sin diagnóstico de convergencia.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["343<br/>MCMC avanzado"] --> C
    subgraph C["344 · Hamiltonian Monte Carlo"]
        direction TB
        D["Demostración<br/><code>hamiltonian_monte_carlo</code>"] --> R["Resultados numéricos<br/>iteraciones<br/>step_size_epsilon<br/>pasos_de_leapfrog<br/>… +5 más"]
        D --> V["Verificaciones<br/>—"]
        D --> O["Contexto y estructura<br/>objetivo<br/>por_que_leapfrog<br/>ventaja_sobre_random_walk<br/>… +2 más"]
    end
    C --> N["345<br/>Variational inference<br/>avanzada"]
    C -.-> IA["Uso en IA<br/>parte 17"]
```

## 🧠 Idea rectora de la parte 17

> La geometría de la información dota al espacio de parámetros de una métrica natural.

## 🔬 Qué ejecuta el laboratorio

`hamiltonian_monte_carlo` — HMC: usar el gradiente para proponer estados lejanos con alta aceptación.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (8) | `iteraciones`, `step_size_epsilon`, `pasos_de_leapfrog`, `tasa_de_aceptacion`, `media_estimada`, `desviacion_estimada`, `autocorrelacion_lag_1`, `tamaño_efectivo_aprox` |
| ✅ Comprobaciones de invariante (0) | — |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-17-frontera-matematica-para-ia-e-investigacion/344-hamiltonian-monte-carlo/lab.py
compmath run 344
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Reportar resultados de MCMC sin diagnóstico de convergencia.
- Invertir una matriz de covarianza sin jitter numérico.
- Interpretar una cota teórica como predicción del error real.

## 🤖 Conexión con IA

Score matching fundamenta los modelos de difusión; el transporte óptimo aparece en flow matching; la teoría estadística del aprendizaje explica el scaling.

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
5. ¿Dónde aparece esto en investigación aplicada?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Rasmussen, C.; Williams, C. *Gaussian Processes for Machine Learning*. MIT Press, 2006.
- Neal, R. *MCMC using Hamiltonian dynamics*. Handbook of MCMC, 2011.
- Peyré, G.; Cuturi, M. *Computational Optimal Transport*. 2019.
- Shalev-Shwartz, S.; Ben-David, S. *Understanding Machine Learning*. Cambridge, 2014.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 343 MCMC avanzado](../343-mcmc-avanzado/README.md) · [📚 Parte 17](../README.md) · [🏠 Programa](../../../README.md) · [345 Variational inference avanzada ➡️](../345-variational-inference-avanzada/README.md)
