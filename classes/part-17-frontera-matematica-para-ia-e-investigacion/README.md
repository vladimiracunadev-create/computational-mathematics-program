# Parte 17 — Frontera matemática para IA e investigación

**Nivel:** frontera-investigacion
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part17.py`

Procesos gaussianos, MCMC avanzado, inferencia variacional, transporte óptimo, geometría diferencial e informacional, SDE, Neural ODE, score matching y teoría del aprendizaje.

## 🧠 Ideas centrales

- Un proceso gaussiano define una distribución sobre funciones, no sobre parámetros.
- HMC usa gradientes para proponer estados lejanos con alta aceptación.
- La distancia de Wasserstein compara distribuciones sin exigir soporte común.
- La geometría de la información dota al espacio de parámetros de una métrica natural.
- Las cotas PAC acotan el error esperado, no garantizan el error observado.

## 🤖 Por qué importa en IA

Score matching fundamenta los modelos de difusión; el transporte óptimo aparece en flow matching; la teoría estadística del aprendizaje explica el scaling.

## ⚠️ Errores frecuentes

- Reportar resultados de MCMC sin diagnóstico de convergencia.
- Invertir una matriz de covarianza sin jitter numérico.
- Interpretar una cota teórica como predicción del error real.

## 🧰 Stack de referencia

`math`, `random`, `numpy (opcional)`, `pymc/jax (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [341 — Gaussian Processes](341-gaussian-processes/README.md)
2. [342 — Kernel methods avanzados](342-kernel-methods-avanzados/README.md)
3. [343 — MCMC avanzado](343-mcmc-avanzado/README.md)
4. [344 — Hamiltonian Monte Carlo](344-hamiltonian-monte-carlo/README.md)
5. [345 — Variational inference avanzada](345-variational-inference-avanzada/README.md)
6. [346 — Optimal transport](346-optimal-transport/README.md)
7. [347 — Wasserstein distance](347-wasserstein-distance/README.md)
8. [348 — Manifold learning](348-manifold-learning/README.md)
9. [349 — Geometría diferencial para ML](349-geometria-diferencial-para-ml/README.md)
10. [350 — Information geometry](350-information-geometry/README.md)
11. [351 — Stochastic differential equations](351-stochastic-differential-equations/README.md)
12. [352 — Neural ODEs](352-neural-odes/README.md)
13. [353 — Score matching](353-score-matching/README.md)
14. [354 — Spectral graph theory](354-spectral-graph-theory/README.md)
15. [355 — Causal inference](355-causal-inference/README.md)
16. [356 — Statistical learning theory](356-statistical-learning-theory/README.md)
17. [357 — VC dimension](357-vc-dimension/README.md)
18. [358 — PAC learning](358-pac-learning/README.md)
19. [359 — Approximation theory y scaling](359-approximation-theory-y-scaling/README.md)
20. [360 — Capstone final: reproducir una idea matemática de un paper](360-capstone-final-reproducir-una-idea-matematica-de-un-paper/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 17
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Rasmussen, C.; Williams, C. *Gaussian Processes for Machine Learning*. MIT Press, 2006.
- Neal, R. *MCMC using Hamiltonian dynamics*. Handbook of MCMC, 2011.
- Peyré, G.; Cuturi, M. *Computational Optimal Transport*. 2019.
- Shalev-Shwartz, S.; Ben-David, S. *Understanding Machine Learning*. Cambridge, 2014.
