# 📖 Glosario — Parte 17: Frontera matemática para IA e investigación

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

38 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Algoritmo de Sinkhorn** | Resuelve el transporte con regularización entrópica mediante escalados alternos. | [346](346-optimal-transport/README.md) |
| **Aprendizaje PAC** | Probablemente aproximadamente correcto: error ≤ ε con probabilidad ≥ 1 − δ. | [358](358-pac-learning/README.md) |
| **Brecha de generalización** | Diferencia entre riesgo verdadero y riesgo empírico. | [356](356-statistical-learning-theory/README.md) |
| **Burn-in** | Iteraciones iniciales descartadas hasta que la cadena alcanza su distribución estacionaria. | [343](343-mcmc-avanzado/README.md) |
| **Colisionador** | Variable causada por dos otras. Condicionar sobre ella crea asociación espuria. | [355](355-causal-inference/README.md) |
| **Complejidad muestral** | Número de ejemplos necesarios para garantizar (ε, δ). Crece como 1/ε y log(1/δ). | [358](358-pac-learning/README.md) |
| **Condición de Mercer** | Una función es kernel válido si su matriz de Gram es siempre semidefinida positiva. | [342](342-kernel-methods-avanzados/README.md) |
| **Conectividad algebraica** | Segundo autovalor del Laplaciano. Mide cuán difícil es partir el grafo. | [354](354-spectral-graph-theory/README.md) |
| **Constante de normalización** | Z que hace que la densidad integre 1. Suele ser intratable y el score la evita. | [353](353-score-matching/README.md) |
| **Cota de Cramér-Rao** | Ningún estimador insesgado tiene varianza menor que la inversa de la información de Fisher. | [350](350-information-geometry/README.md) |
| **Criterio de puerta trasera** | Ajustar por un conjunto que bloquee todos los caminos no causales entre X e Y. | [355](355-causal-inference/README.md) |
| **Dimensión intrínseca** | Número de grados de libertad reales de los datos, independiente del espacio de representación. | [348](348-manifold-learning/README.md) |
| **Dimensión VC** | Tamaño del mayor conjunto que la clase de hipótesis puede etiquetar de todas las formas. | [357](357-vc-dimension/README.md) |
| **Distancia de Wasserstein** | Coste mínimo de transporte. Es una métrica verdadera y funciona sin soporte común. | [347](347-wasserstein-distance/README.md) |
| **Ecuación diferencial estocástica** | Ecuación con un término de deriva y otro de ruido browniano. | [351](351-stochastic-differential-equations/README.md) |
| **Euler-Maruyama** | Integrador de SDE. El ruido escala como √dt, no como dt. | [351](351-stochastic-differential-equations/README.md) |
| **Familia variacional** | Conjunto de distribuciones candidatas entre las que se busca la mejor aproximación. | [345](345-variational-inference-avanzada/README.md) |
| **Fragmentar** | Realizar todas las 2ⁿ etiquetaciones posibles de n puntos. | [357](357-vc-dimension/README.md) |
| **Geodésica** | Curva de longitud mínima entre dos puntos de una variedad. | [349](349-geometria-diferencial-para-ml/README.md) |
| **Gradiente natural** | Gradiente preacondicionado por la inversa de Fisher. Invariante a reparametrizaciones. | [350](350-information-geometry/README.md) |
| **Hamiltonian Monte Carlo** | Usa el gradiente y dinámica hamiltoniana para proponer estados lejanos con alta aceptación. | [344](344-hamiltonian-monte-carlo/README.md) |
| **Hipótesis de la variedad** | Los datos reales viven cerca de una variedad de dimensión mucho menor que la ambiente. | [348](348-manifold-learning/README.md) |
| **Inferencia variacional** | Aproximar una posterior optimizando dentro de una familia en vez de muestrear. | [345](345-variational-inference-avanzada/README.md) |
| **Información de Fisher** | Curvatura local de la KL. Métrica natural del espacio de parámetros. | [350](350-information-geometry/README.md) |
| **Jitter numérico** | Pequeña constante sumada a la diagonal para que la covarianza sea invertible. | [341](341-gaussian-processes/README.md) |
| **Leapfrog** | Integrador simpléctico que conserva el volumen y hace válida la propuesta de HMC. | [344](344-hamiltonian-monte-carlo/README.md) |
| **Ley de escala** | Error que decae como una potencia del número de parámetros o de datos. | [359](359-approximation-theory-y-scaling/README.md) |
| **Matriz de Gram** | Matriz de todos los productos kernel entre pares de puntos. | [342](342-kernel-methods-avanzados/README.md) |
| **Metropolis-Hastings** | Propone un estado y lo acepta con probabilidad dependiente de la razón de densidades. | [343](343-mcmc-avanzado/README.md) |
| **Método adjunto** | Calcula gradientes resolviendo una EDO hacia atrás, con memoria constante. | [352](352-neural-odes/README.md) |
| **Neural ODE** | Red donde la profundidad es continua y la salida es la solución de una EDO aprendida. | [352](352-neural-odes/README.md) |
| **Proceso gaussiano** | Distribución sobre funciones definida por una media y un kernel de covarianza. | [341](341-gaussian-processes/README.md) |
| **Riesgo empírico** | Error medido sobre la muestra de entrenamiento. | [356](356-statistical-learning-theory/README.md) |
| **Score** | ∇ₓ log p(x). No depende de la constante de normalización. | [353](353-score-matching/README.md) |
| **Tasa de aceptación** | Fracción de propuestas aceptadas. El óptimo en una dimensión ronda 0,44. | [343](343-mcmc-avanzado/README.md) |
| **Tensor métrico** | Objeto que define distancias y ángulos localmente en una variedad. | [349](349-geometria-diferencial-para-ml/README.md) |
| **Transporte óptimo** | Plan de mínimo coste para transformar una distribución en otra. | [346](346-optimal-transport/README.md) |
| **Vector de Fiedler** | Autovector del segundo autovalor del Laplaciano. Su signo sugiere el corte del grafo. | [354](354-spectral-graph-theory/README.md) |

## Cómo usar este glosario

No memorices las definiciones: **usa la columna de clase**. Un término se entiende cuando
puedes ejecutar su demostración y explicar qué comprueba, no cuando puedes recitar su
definición.

```bash
compmath show <clase>    # ficha de la clase donde vive el término
compmath run <clase>     # ejecutar su demostración
```

---

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md)
