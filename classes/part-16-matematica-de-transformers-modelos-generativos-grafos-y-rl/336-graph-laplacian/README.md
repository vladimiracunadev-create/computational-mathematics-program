# 336 — Graph Laplacian

**Parte:** 16 — Matemática de Transformers, modelos generativos, grafos y RL
**Nivel:** experto
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part16` · demostración `graph_laplacian`

## 🎯 Propósito

Softmax, embeddings, positional encoding, atención escalada, multi-head, Transformer completo, muestreo, VAE, GAN, difusión, GNN y ecuaciones de Bellman.

Esta clase concreta ese objetivo sobre **Graph Laplacian**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Graph Laplacian** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `graph_laplacian` del motor de la parte.
4. Interpretar las 12 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: olvidar la máscara causal en el modelado autoregresivo.

## 🧠 Idea rectora de la parte 16

> La atención es un promedio ponderado por similitud, normalizado con softmax.

## 🧩 Qué calcula el laboratorio

`graph_laplacian` — Laplaciano del grafo: espectro y componentes conexas.

Salidas que devuelve:

- `nodos`
- `aristas`
- `grados`
- `matriz_de_adyacencia`
- `laplaciano`
- `autovalores`
- `autovalores_nulos`
- `componentes_conexas`
- `es_semidefinido_positivo`
- `conectividad_algebraica_fiedler`
- `L_normalizado`
- `uso`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/336-graph-laplacian/lab.py
```

o desde la CLI del programa:

```bash
compmath run 336
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Olvidar la máscara causal en el modelado autoregresivo.
- Confundir temperatura alta con mayor calidad en lugar de mayor entropía.
- Normalizar el Laplaciano de un grafo con nodos aislados sin tratar la división por cero.

## 🤖 Conexión con IA

Esta parte es la traducción matemática directa de los papers que definen el estado del arte actual.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Vaswani, A. et al. *Attention Is All You Need*. NeurIPS, 2017.
- Kingma, D.; Welling, M. *Auto-Encoding Variational Bayes*. ICLR, 2014.
- Ho, J.; Jain, A.; Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS, 2020.
- Sutton, R.; Barto, A. *Reinforcement Learning: An Introduction*. 2ª ed., MIT Press, 2018.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
