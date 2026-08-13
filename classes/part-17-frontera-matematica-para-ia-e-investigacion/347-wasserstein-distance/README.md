# 347 — Wasserstein distance

**Parte:** 17 — Frontera matemática para IA e investigación
**Nivel:** frontera-investigacion
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part17` · demostración `wasserstein_distance`

## 🎯 Propósito

Procesos gaussianos, MCMC avanzado, inferencia variacional, transporte óptimo, geometría diferencial e informacional, SDE, Neural ODE, score matching y teoría del aprendizaje.

Esta clase concreta ese objetivo sobre **Wasserstein distance**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Wasserstein distance** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `wasserstein_distance` del motor de la parte.
4. Interpretar las 11 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: reportar resultados de mcmc sin diagnóstico de convergencia.

## 🧠 Idea rectora de la parte 17

> HMC usa gradientes para proponer estados lejanos con alta aceptación.

## 🧩 Qué calcula el laboratorio

`wasserstein_distance` — Wasserstein-1 en 1D: comparar distribuciones sin soporte común.

Salidas que devuelve:

- `muestras`
- `W1(N(0,1), N(0.5,1))`
- `diferencia_de_medias_teorica`
- `W1(N(0,1), N(5,1))`
- `diferencia_teorica_lejana`
- `KL_empirica_cercana`
- `KL_empirica_lejana_(soportes_casi_disjuntos)`
- `W1_crece_de_forma_proporcional`
- `KL_no_informa_cuando_no_hay_solape`
- `por_que_importa_en_GAN`
- `formula_1D`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-17-frontera-matematica-para-ia-e-investigacion/347-wasserstein-distance/lab.py
```

o desde la CLI del programa:

```bash
compmath run 347
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Reportar resultados de MCMC sin diagnóstico de convergencia.
- Invertir una matriz de covarianza sin jitter numérico.
- Interpretar una cota teórica como predicción del error real.

## 🤖 Conexión con IA

Score matching fundamenta los modelos de difusión; el transporte óptimo aparece en flow matching; la teoría estadística del aprendizaje explica el scaling.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Rasmussen, C.; Williams, C. *Gaussian Processes for Machine Learning*. MIT Press, 2006.
- Neal, R. *MCMC using Hamiltonian dynamics*. Handbook of MCMC, 2011.
- Peyré, G.; Cuturi, M. *Computational Optimal Transport*. 2019.
- Shalev-Shwartz, S.; Ben-David, S. *Understanding Machine Learning*. Cambridge, 2014.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
