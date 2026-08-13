# 🔭 Parte 17 — Frontera matemática para IA e investigación

> [⬅️ Parte 16 — Matemática de Transformers, modelos generativos, grafos y RL](../part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md)

**Nivel:** `frontera-investigacion` · **Clases:** 20 · **Horas estimadas:** 80 · **Motor:** [`part17.py`](../../src/computational_math/engines/part17.py)

---

## 🎯 De qué trata esta parte

Procesos gaussianos, MCMC avanzado, inferencia variacional, transporte óptimo, geometría diferencial e informacional, SDE, Neural ODE, score matching y teoría del aprendizaje.

## 🧠 Ideas centrales

- Un proceso gaussiano define una distribución sobre funciones, no sobre parámetros.
- HMC usa gradientes para proponer estados lejanos con alta aceptación.
- La distancia de Wasserstein compara distribuciones sin exigir soporte común.
- La geometría de la información dota al espacio de parámetros de una métrica natural.
- Las cotas PAC acotan el error esperado, no garantizan el error observado.

## 🤖 Por qué importa en IA

> [!IMPORTANT]
> Score matching fundamenta los modelos de difusión; el transporte óptimo aparece en flow matching; la teoría estadística del aprendizaje explica el scaling.

## ⚠️ Errores frecuentes de esta parte

- Reportar resultados de MCMC sin diagnóstico de convergencia.
- Invertir una matriz de covarianza sin jitter numérico.
- Interpretar una cota teórica como predicción del error real.

## 🧭 Secuencia de la parte

```mermaid
flowchart LR
    subgraph B1["Bloque 1"]
        direction TB
        L341["341 · Gaussian Processes"]
        L342["342 · Kernel methods avanzados"]
        L343["343 · MCMC avanzado"]
        L344["344 · Hamiltonian Monte Carlo"]
        L345["345 · Variational inference avanzada"]
        L341 --> L342
        L342 --> L343
        L343 --> L344
        L344 --> L345
    end
    subgraph B2["Bloque 2"]
        direction TB
        L346["346 · Optimal transport"]
        L347["347 · Wasserstein distance"]
        L348["348 · Manifold learning"]
        L349["349 · Geometría diferencial para ML"]
        L350["350 · Information geometry"]
        L346 --> L347
        L347 --> L348
        L348 --> L349
        L349 --> L350
    end
    subgraph B3["Bloque 3"]
        direction TB
        L351["351 · Stochastic differential…"]
        L352["352 · Neural ODEs"]
        L353["353 · Score matching"]
        L354["354 · Spectral graph theory"]
        L355["355 · Causal inference"]
        L351 --> L352
        L352 --> L353
        L353 --> L354
        L354 --> L355
    end
    subgraph B4["Bloque 4"]
        direction TB
        L356["356 · Statistical learning theory"]
        L357["357 · VC dimension"]
        L358["358 · PAC learning"]
        L359["359 · Approximation theory y scaling"]
        L360["360 · Capstone final: reproducir…"]
        L356 --> L357
        L357 --> L358
        L358 --> L359
        L359 --> L360
    end
    L345 --> L346
    L350 --> L351
    L355 --> L356
```

## 📚 Las clases

| # | Clase | Demostración | Idea central |
|---|---|---|---|
| `341` | [Gaussian Processes](341-gaussian-processes/README.md) | `gaussian_processes` | GP: distribución sobre funciones, con media y varianza posterior. |
| `342` | [Kernel methods avanzados](342-kernel-methods-avanzados/README.md) | `advanced_kernels` | Familias de kernels y la condición de Mercer. |
| `343` | [MCMC avanzado](343-mcmc-avanzado/README.md) | `advanced_mcmc` | Metropolis-Hastings con diagnóstico de aceptación y autocorrelación. |
| `344` | [Hamiltonian Monte Carlo](344-hamiltonian-monte-carlo/README.md) | `hamiltonian_monte_carlo` | HMC: usar el gradiente para proponer estados lejanos con alta aceptación. |
| `345` | [Variational inference avanzada](345-variational-inference-avanzada/README.md) | `advanced_variational_inference` | Inferencia variacional: optimizar en lugar de muestrear. |
| `346` | [Optimal transport](346-optimal-transport/README.md) | `optimal_transport` | Transporte óptimo por Sinkhorn: coste de mover una distribución a otra. |
| `347` | [Wasserstein distance](347-wasserstein-distance/README.md) | `wasserstein_distance` | Wasserstein-1 en 1D: comparar distribuciones sin soporte común. |
| `348` | [Manifold learning](348-manifold-learning/README.md) | `manifold_learning` | Variedad: dimensión intrínseca menor que la del espacio ambiente. |
| `349` | [Geometría diferencial para ML](349-geometria-diferencial-para-ml/README.md) | `differential_geometry` | Geometría diferencial: métrica, longitud de curva y curvatura. |
| `350` | [Information geometry](350-information-geometry/README.md) | `information_geometry` | Información de Fisher: la métrica natural del espacio de parámetros. |
| `351` | [Stochastic differential equations](351-stochastic-differential-equations/README.md) | `stochastic_differential_equations` | SDE: proceso de Ornstein-Uhlenbeck simulado con Euler-Maruyama. |
| `352` | [Neural ODEs](352-neural-odes/README.md) | `neural_odes` | Neural ODE: capas continuas y el método adjunto. |
| `353` | [Score matching](353-score-matching/README.md) | `score_matching` | Score matching: aprender ∇ log p sin conocer la constante de normalización. |
| `354` | [Spectral graph theory](354-spectral-graph-theory/README.md) | `spectral_graph_theory` | Clustering espectral: el vector de Fiedler separa el grafo. |
| `355` | [Causal inference](355-causal-inference/README.md) | `causal_inference` | Confusión, ajuste por backdoor y el sesgo de colisionador. |
| `356` | [Statistical learning theory](356-statistical-learning-theory/README.md) | `statistical_learning_theory` | Riesgo empírico frente a riesgo verdadero y la brecha de generalización. |
| `357` | [VC dimension](357-vc-dimension/README.md) | `vc_dimension` | Dimensión VC: cuántos puntos puede fragmentar una clase de hipótesis. |
| `358` | [PAC learning](358-pac-learning/README.md) | `pac_learning` | PAC: cuántas muestras hacen falta para (ε, δ). |
| `359` | [Approximation theory y scaling](359-approximation-theory-y-scaling/README.md) | `approximation_theory` | Teoría de aproximación y leyes de escala: el error como potencia del tamaño. |
| `360` | [Capstone final: reproducir una idea matemática de un paper](360-capstone-final-reproducir-una-idea-matematica-de-un-paper/README.md) | `capstone_reproduce_paper_idea` | Capstone: reproducir el núcleo matemático de un resultado publicado. |

## 🧰 Stack de referencia

`math`, `random`, `numpy (opcional)`, `pymc/jax (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen
como contraste profesional, no como requisito.

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 17
compmath catalog --part 17
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone ([360](360-capstone-final-reproducir-una-idea-matematica-de-un-paper/README.md)) | 20 % |

## 📖 Bibliografía

- Rasmussen, C.; Williams, C. *Gaussian Processes for Machine Learning*. MIT Press, 2006.
- Neal, R. *MCMC using Hamiltonian dynamics*. Handbook of MCMC, 2011.
- Peyré, G.; Cuturi, M. *Computational Optimal Transport*. 2019.
- Shalev-Shwartz, S.; Ben-David, S. *Understanding Machine Learning*. Cambridge, 2014.

---

> [⬅️ Parte 16 — Matemática de Transformers, modelos generativos, grafos y RL](../part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md)
