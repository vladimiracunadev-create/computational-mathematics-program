# 📖 Glosario — Parte 16: Matemática de Transformers, modelos generativos, grafos y RL

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

33 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Atención escalada** | softmax(QKᵀ/√d)·V. La escala evita que la softmax se sature en alta dimensión. | [325](325-scaled-dot-product-attention/README.md) |
| **Autoencoder variacional** | Codificador que produce una distribución latente y decodificador que reconstruye. | [331](331-variational-autoencoders/README.md) |
| **Brecha del ELBO** | KL entre la posterior aproximada y la verdadera. Siempre no negativa. | [332](332-elbo-y-variational-inference/README.md) |
| **Conexión residual** | Sumar la entrada a la salida del bloque. Crea un camino directo para el gradiente. | [328](328-transformer-completo/README.md) |
| **Discriminador óptimo** | D*(x) = p_datos/(p_datos + p_G). En el equilibrio vale 0,5 en todas partes. | [333](333-gan-y-juegos-minimax/README.md) |
| **Ecuación de Bellman** | V(s) = max_a [R + γ·V(s')]. Valor como recompensa inmediata más futuro descontado. | [338](338-bellman-equations/README.md) |
| **ELBO** | Cota inferior de la log-verosimilitud: reconstrucción menos KL al prior. | [332](332-elbo-y-variational-inference/README.md) |
| **Estabilidad numérica del softmax** | Restar el máximo antes de exponenciar. La salida no cambia y se evita el desbordamiento. | [321](321-softmax-y-distribuciones-categoricas/README.md) |
| **Factor 1/√d** | Corrige que la varianza del producto escalar crece con la dimensión. | [325](325-scaled-dot-product-attention/README.md) |
| **Factor de descuento** | γ entre 0 y 1. Pondera cuánto valen las recompensas futuras. | [338](338-bellman-equations/README.md) |
| **Feed-forward por posición** | MLP aplicado independientemente a cada token, típicamente con expansión ×4. | [328](328-transformer-completo/README.md) |
| **Horario de ruido** | Secuencia de β que determina cuánto ruido se añade en cada paso. | [334](334-diffusion-models-forward-process/README.md) |
| **Juego minimax** | Dos jugadores con objetivos opuestos. Base del entrenamiento de las GAN. | [333](333-gan-y-juegos-minimax/README.md) |
| **Laplaciano del grafo** | L = D − A. Sus autovalores describen la conectividad de la estructura. | [336](336-graph-laplacian/README.md) |
| **Línea base** | Valor restado a la recompensa para reducir la varianza sin sesgar el gradiente. | [339](339-policy-gradients/README.md) |
| **Modelado autorregresivo** | Factorizar la probabilidad de una secuencia como producto de condicionales. | [329](329-modelado-autoregresivo/README.md) |
| **Multi-head attention** | Varias atenciones en subespacios distintos, concatenadas y proyectadas. | [327](327-multi-head-attention/README.md) |
| **Multiplicidad del autovalor cero** | Número de componentes conexas del grafo. | [336](336-graph-laplacian/README.md) |
| **Máscara causal** | Impide que un token atienda a posiciones futuras. Imprescindible en generación. | [326](326-self-attention/README.md) |
| **Paso de mensajes** | Cada nodo agrega información de sus vecinos. Una capa equivale a un salto. | [337](337-message-passing-en-gnn/README.md) |
| **Perplejidad** | Exponencial de la entropía cruzada. Número efectivo de opciones equiprobables. | [329](329-modelado-autoregresivo/README.md) |
| **Positional encoding** | Información de posición añadida al embedding. La versión sinusoidal no tiene parámetros. | [323](323-positional-encoding/README.md) |
| **Proceso directo de difusión** | Añadir ruido gaussiano según un horario fijo hasta destruir la señal. | [334](334-diffusion-models-forward-process/README.md) |
| **Proceso inverso** | Red que predice el ruido añadido y permite reconstruir el dato original. | [335](335-diffusion-models-reverse-process/README.md) |
| **Query, Key, Value** | Tres proyecciones del mismo token: qué busco, qué ofrezco y qué aporto. | [324](324-query-key-y-value/README.md) |
| **REINFORCE** | Gradiente de política que sube la probabilidad de acciones con recompensa alta. | [339](339-policy-gradients/README.md) |
| **Self-attention** | Atención donde consultas, claves y valores vienen de la misma secuencia. | [326](326-self-attention/README.md) |
| **Similitud coseno** | Producto escalar normalizado. Mide dirección e ignora magnitud. | [322](322-embeddings-y-similitud-coseno/README.md) |
| **Sobresuavizado** | Con muchas capas, todos los nodos convergen a representaciones indistinguibles. | [337](337-message-passing-en-gnn/README.md) |
| **Softmax** | Convierte logits reales en una distribución categórica. Es la de máxima entropía dados los logits. | [321](321-softmax-y-distribuciones-categoricas/README.md) |
| **Temperatura** | Divide los logits antes del softmax. Menor concentra la distribución, mayor la aplana. | [330](330-sampling-temperatura-top-k-y-top-p/README.md) |
| **Top-k y top-p** | Truncar el vocabulario a los k mejores o a la masa acumulada p antes de muestrear. | [330](330-sampling-temperatura-top-k-y-top-p/README.md) |
| **Truco de reparametrización** | z = μ + σ·ε con ε fijo, para que el gradiente atraviese el muestreo. | [331](331-variational-autoencoders/README.md) |

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
