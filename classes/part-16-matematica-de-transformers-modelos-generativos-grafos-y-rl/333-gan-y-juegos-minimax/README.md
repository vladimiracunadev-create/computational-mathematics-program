# 333 — GAN y juegos minimax

> [⬅️ 332 ELBO y variational inference](../332-elbo-y-variational-inference/README.md) · [📚 Parte 16](../README.md) · [🏠 Programa](../../../README.md) · [334 Diffusion models: forward process ➡️](../334-diffusion-models-forward-process/README.md)

**Parte:** 16 — Matemática de Transformers, modelos generativos, grafos y RL · **Nivel:** `experto` · **Horas estimadas:** 4
**Motor:** `engines.part16` · **Demostración:** `gan_minimax` · **Clase 13 de 20** de la parte

---

## 🎯 Propósito

Softmax, embeddings, positional encoding, atención escalada, multi-head, Transformer completo, muestreo, VAE, GAN, difusión, GNN y ecuaciones de Bellman.

Esta clase concreta ese objetivo sobre **GAN y juegos minimax**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **GAN y juegos minimax** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `gan_minimax`.
4. Interpretar las 9 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: olvidar la máscara causal en el modelado autoregresivo.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["Clase 332 · ELBO y variational…"] --> D
    subgraph CLASE["Clase 333 · GAN y juegos minimax"]
        direction TB
        D["Demostracion gan_minimax"]
        D --> R["Resultados 1: perdida_teorica_en_eq…"]
        D --> V["Comprobaciones 1: en_el_equilibrio_D=0.5"]
        D --> O["Contexto 7: objetivo +6"]
    end
    R --> N["Clase 334 · Diffusion models:…"]
    V -.-> IA["Aplicacion en IA · parte 16"]
```

## 🧠 Idea rectora de la parte 16

> Temperatura, top-k y top-p reescriben la distribución antes de muestrear.

## 🔬 Qué ejecuta el laboratorio

`gan_minimax` — GAN: el equilibrio del juego minimax y su punto óptimo.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (1) | `perdida_teorica_en_equilibrio` |
| ✅ Comprobaciones de invariante (1) | `en_el_equilibrio_D=0.5` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/333-gan-y-juegos-minimax/lab.py
compmath run 333
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Olvidar la máscara causal en el modelado autoregresivo.
- Confundir temperatura alta con mayor calidad en lugar de mayor entropía.
- Normalizar el Laplaciano de un grafo con nodos aislados sin tratar la división por cero.

## 🤖 Conexión con IA

Esta parte es la traducción matemática directa de los papers que definen el estado del arte actual.

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
5. ¿Dónde aparece esto en LLM?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Vaswani, A. et al. *Attention Is All You Need*. NeurIPS, 2017.
- Kingma, D.; Welling, M. *Auto-Encoding Variational Bayes*. ICLR, 2014.
- Ho, J.; Jain, A.; Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS, 2020.
- Sutton, R.; Barto, A. *Reinforcement Learning: An Introduction*. 2ª ed., MIT Press, 2018.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 332 ELBO y variational inference](../332-elbo-y-variational-inference/README.md) · [📚 Parte 16](../README.md) · [🏠 Programa](../../../README.md) · [334 Diffusion models: forward process ➡️](../334-diffusion-models-forward-process/README.md)
