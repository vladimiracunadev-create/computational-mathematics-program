# Parte 16 — Matemática de Transformers, modelos generativos, grafos y RL

**Nivel:** experto
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part16.py`

Softmax, embeddings, positional encoding, atención escalada, multi-head, Transformer completo, muestreo, VAE, GAN, difusión, GNN y ecuaciones de Bellman.

## 🧠 Ideas centrales

- La atención es un promedio ponderado por similitud, normalizado con softmax.
- La escala 1/√d evita que el producto punto sature la softmax en alta dimensión.
- Temperatura, top-k y top-p reescriben la distribución antes de muestrear.
- El ELBO acota inferiormente la log-verosimilitud con un término de reconstrucción y uno KL.
- Bellman expresa el valor como recompensa inmediata más valor futuro descontado.

## 🤖 Por qué importa en IA

Esta parte es la traducción matemática directa de los papers que definen el estado del arte actual.

## ⚠️ Errores frecuentes

- Olvidar la máscara causal en el modelado autoregresivo.
- Confundir temperatura alta con mayor calidad en lugar de mayor entropía.
- Normalizar el Laplaciano de un grafo con nodos aislados sin tratar la división por cero.

## 🧰 Stack de referencia

`math`, `random`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [321 — Softmax y distribuciones categóricas](321-softmax-y-distribuciones-categoricas/README.md)
2. [322 — Embeddings y similitud coseno](322-embeddings-y-similitud-coseno/README.md)
3. [323 — Positional encoding](323-positional-encoding/README.md)
4. [324 — Query, Key y Value](324-query-key-y-value/README.md)
5. [325 — Scaled dot-product attention](325-scaled-dot-product-attention/README.md)
6. [326 — Self-attention](326-self-attention/README.md)
7. [327 — Multi-head attention](327-multi-head-attention/README.md)
8. [328 — Transformer completo](328-transformer-completo/README.md)
9. [329 — Modelado autoregresivo](329-modelado-autoregresivo/README.md)
10. [330 — Sampling, temperatura, top-k y top-p](330-sampling-temperatura-top-k-y-top-p/README.md)
11. [331 — Variational Autoencoders](331-variational-autoencoders/README.md)
12. [332 — ELBO y variational inference](332-elbo-y-variational-inference/README.md)
13. [333 — GAN y juegos minimax](333-gan-y-juegos-minimax/README.md)
14. [334 — Diffusion models: forward process](334-diffusion-models-forward-process/README.md)
15. [335 — Diffusion models: reverse process](335-diffusion-models-reverse-process/README.md)
16. [336 — Graph Laplacian](336-graph-laplacian/README.md)
17. [337 — Message passing en GNN](337-message-passing-en-gnn/README.md)
18. [338 — Bellman equations](338-bellman-equations/README.md)
19. [339 — Policy gradients](339-policy-gradients/README.md)
20. [340 — Capstone: mini-Transformer matemático](340-capstone-mini-transformer-matematico/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 16
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Vaswani, A. et al. *Attention Is All You Need*. NeurIPS, 2017.
- Kingma, D.; Welling, M. *Auto-Encoding Variational Bayes*. ICLR, 2014.
- Ho, J.; Jain, A.; Abbeel, P. *Denoising Diffusion Probabilistic Models*. NeurIPS, 2020.
- Sutton, R.; Barto, A. *Reinforcement Learning: An Introduction*. 2ª ed., MIT Press, 2018.
