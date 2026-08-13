# 📖 Glosario — Parte 15: Matemática de Deep Learning

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

36 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Acumulación de gradientes** | Un nodo usado en varios sitios suma las contribuciones de todos sus consumos. | [306](306-computational-graphs/README.md) |
| **Autodiferenciación en modo reverso** | Una pasada hacia adelante y una hacia atrás dan todos los gradientes de una salida escalar. | [319](319-autodiff-con-pytorch-jax/README.md) |
| **Backpropagation** | Regla de la cadena aplicada en orden topológico inverso sobre el grafo de cómputo. | [305](305-backpropagation-paso-a-paso/README.md) |
| **Batch normalization** | Normaliza cada característica sobre el lote. Depende del tamaño del lote. | [308](308-batch-normalization-y-layer-normalization/README.md) |
| **Campo receptivo** | Región de la entrada que influye en una activación concreta. Crece al apilar capas. | [311](311-cnn-y-receptive-fields/README.md) |
| **Capa oculta** | Capa intermedia que construye una representación donde el problema sí es separable. | [302](302-mlp-como-composicion-de-funciones/README.md) |
| **Compartición de parámetros** | El mismo núcleo se aplica en todas las posiciones. Reduce parámetros e impone invariancia. | [311](311-cnn-y-receptive-fields/README.md) |
| **Dropout** | Apagar neuronas al azar durante el entrenamiento para evitar coadaptación. | [309](309-regularizacion-y-dropout/README.md) |
| **Embedding** | Representación densa aprendida donde la proximidad geométrica refleja similitud. | [317](317-embeddings-como-espacios-vectoriales/README.md) |
| **Estado de celda** | Memoria de largo plazo de la LSTM, actualizada de forma aditiva. | [315](315-lstm-y-compuertas/README.md) |
| **Estado oculto** | Vector que resume la historia procesada hasta el instante actual. | [313](313-rnn-y-recurrencia/README.md) |
| **Función de activación** | No linealidad aplicada tras la transformación lineal. Sin ella la profundidad no aporta nada. | [303](303-funciones-de-activacion/README.md) |
| **Gradient clipping** | Acotar la norma del gradiente conservando su dirección. Evita la explosión. | [314](314-vanishing-y-exploding-gradients/README.md) |
| **Gradiente que se desvanece** | Producto de muchas derivadas menores que 1: el gradiente tiende a cero exponencialmente. | [314](314-vanishing-y-exploding-gradients/README.md) |
| **Grafo de cómputo** | Representación de la expresión como nodos de operaciones y aristas de dependencia. | [306](306-computational-graphs/README.md) |
| **GRU** | Celda recurrente con puertas de actualización y reinicio. Un 25 % menos de parámetros que LSTM. | [316](316-gru/README.md) |
| **Inicialización de He** | Escala √(2/n). Compensa que ReLU anula la mitad de las activaciones. | [307](307-inicializacion-de-pesos/README.md) |
| **Inicialización de Xavier** | Escala 1/√n. Mantiene la varianza estable con activaciones simétricas como tanh. | [307](307-inicializacion-de-pesos/README.md) |
| **Inverted dropout** | Escalar durante el entrenamiento para que la inferencia no requiera ajuste. | [309](309-regularizacion-y-dropout/README.md) |
| **Layer normalization** | Normaliza cada muestra sobre sus características. Independiente del lote. | [308](308-batch-normalization-y-layer-normalization/README.md) |
| **LSTM** | Celda con puertas de olvido, entrada y salida, y un camino aditivo para el gradiente. | [315](315-lstm-y-compuertas/README.md) |
| **Padding** | Relleno del borde que permite conservar el tamaño espacial tras convolucionar. | [310](310-convolucion-discreta/README.md) |
| **Paso hacia adelante** | Cálculo de las salidas capa a capa, guardando los valores intermedios. | [305](305-backpropagation-paso-a-paso/README.md) |
| **Perceptrón** | Neurona lineal con umbral. Converge si y solo si los datos son linealmente separables. | [301](301-perceptron-y-separabilidad/README.md) |
| **Perceptrón multicapa** | Composición de capas lineales con no linealidad entre ellas. | [302](302-mlp-como-composicion-de-funciones/README.md) |
| **Pooling** | Reducción espacial por máximo o media. Sin parámetros aprendidos. | [312](312-pooling-y-downsampling/README.md) |
| **Pérdida de Huber** | Cuadrática cerca de cero y lineal lejos. Robusta ante valores atípicos. | [304](304-funciones-de-perdida/README.md) |
| **Red recurrente** | Procesa secuencias manteniendo un estado oculto y compartiendo pesos en el tiempo. | [313](313-rnn-y-recurrencia/README.md) |
| **ReLU** | max(0, x). Derivada 1 en positivo: no satura por la derecha y es barata. | [303](303-funciones-de-activacion/README.md) |
| **Ruptura de simetría** | Inicializar con valores distintos para que las neuronas de una capa no aprendan lo mismo. | [307](307-inicializacion-de-pesos/README.md) |
| **Saturación** | Zona donde la derivada de la activación es casi nula y el gradiente deja de fluir. | [303](303-funciones-de-activacion/README.md) |
| **Separabilidad lineal** | Existencia de un hiperplano que separa las clases sin error. XOR no la cumple. | [301](301-perceptron-y-separabilidad/README.md) |
| **Similitud coseno** | Coseno del ángulo entre dos vectores. Ignora la magnitud y mide solo la dirección. | [317](317-embeddings-como-espacios-vectoriales/README.md) |
| **Stride** | Salto del núcleo al desplazarse. Reduce el tamaño de salida. | [310](310-convolucion-discreta/README.md) |
| **Teorema de aproximación universal** | Una capa oculta suficientemente ancha aproxima cualquier función continua. No dice cómo entrenarla. | [302](302-mlp-como-composicion-de-funciones/README.md) |
| **Warmup** | Subir el learning rate gradualmente al inicio para no divergir con estadísticas inmaduras. | [318](318-optimizacion-de-redes-profundas/README.md) |

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
