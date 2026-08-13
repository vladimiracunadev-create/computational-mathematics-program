# 337 — Message passing en GNN

**Parte:** 16 — Matemática de Transformers, modelos generativos, grafos y RL
**Nivel:** experto
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part16` · demostración `message_passing`

## 🎯 Propósito

Softmax, embeddings, positional encoding, atención escalada, multi-head, Transformer completo, muestreo, VAE, GAN, difusión, GNN y ecuaciones de Bellman.

Esta clase concreta ese objetivo sobre **Message passing en GNN**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Message passing en GNN** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `message_passing` del motor de la parte.
4. Interpretar las 10 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: confundir temperatura alta con mayor calidad en lugar de mayor entropía.

## 🧠 Idea rectora de la parte 16

> La escala 1/√d evita que el producto punto sature la softmax en alta dimensión.

## 🧩 Qué calcula el laboratorio

`message_passing` — Message passing: cada capa agrega información de un salto más lejos.

Salidas que devuelve:

- `nodos`
- `features_iniciales`
- `tras_1_capa`
- `tras_2_capas`
- `receptivo_tras_k_capas`
- `normalizacion`
- `el_nodo_4_solo_tiene_1_vecino`
- `permutacion_equivariante`
- `oversmoothing`
- `referencia`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/337-message-passing-en-gnn/lab.py
```

o desde la CLI del programa:

```bash
compmath run 337
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
