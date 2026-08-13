# 355 — Causal inference

> [⬅️ 354 Spectral graph theory](../354-spectral-graph-theory/README.md) · [📚 Parte 17](../README.md) · [🏠 Programa](../../../README.md) · [356 Statistical learning theory ➡️](../356-statistical-learning-theory/README.md)

**Parte:** 17 — Frontera matemática para IA e investigación · **Nivel:** `frontera-investigacion` · **Horas estimadas:** 4
**Motor:** `engines.part17` · **Demostración:** `causal_inference` · **Clase 15 de 20** de la parte

---

## 🎯 Propósito

Procesos gaussianos, MCMC avanzado, inferencia variacional, transporte óptimo, geometría diferencial e informacional, SDE, Neural ODE, score matching y teoría del aprendizaje.

Esta clase concreta ese objetivo sobre **Causal inference**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Causal inference** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `causal_inference`.
4. Interpretar las 10 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: interpretar una cota teórica como predicción del error real.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["354<br/>Spectral graph theory"] --> C
    subgraph C["355 · Causal inference"]
        direction TB
        D["Demostración<br/><code>causal_inference</code>"] --> R["Resultados numéricos<br/>efecto_causal_real_de_X_sobre_Y<br/>coeficiente_sin_ajustar<br/>coeficiente_ajustando_por_Z<br/>… +2 más"]
        D --> V["Verificaciones<br/>el_ajuste_recupera_el_efecto<br/>condicionar_un_colisionador_crea_sesgo"]
        D --> O["Contexto y estructura<br/>criterio_backdoor<br/>regla<br/>referencia"]
    end
    C --> N["356<br/>Statistical learning<br/>theory"]
    C -.-> IA["Uso en IA<br/>parte 17"]
```

## 🧠 Idea rectora de la parte 17

> Las cotas PAC acotan el error esperado, no garantizan el error observado.

## 🔬 Qué ejecuta el laboratorio

`causal_inference` — Confusión, ajuste por backdoor y el sesgo de colisionador.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (5) | `efecto_causal_real_de_X_sobre_Y`, `coeficiente_sin_ajustar`, `coeficiente_ajustando_por_Z`, `correlacion_X_Y_sin_condicionar_el_colisionador`, `correlacion_condicionando_el_colisionador` |
| ✅ Comprobaciones de invariante (2) | `el_ajuste_recupera_el_efecto`, `condicionar_un_colisionador_crea_sesgo` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-17-frontera-matematica-para-ia-e-investigacion/355-causal-inference/lab.py
compmath run 355
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

> [⬅️ 354 Spectral graph theory](../354-spectral-graph-theory/README.md) · [📚 Parte 17](../README.md) · [🏠 Programa](../../../README.md) · [356 Statistical learning theory ➡️](../356-statistical-learning-theory/README.md)
