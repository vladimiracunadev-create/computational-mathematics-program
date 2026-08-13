# 📖 Glosario — Parte 13: Teoría de la información, señales y series

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

34 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Aliasing** | Frecuencias altas que aparecen como bajas al muestrear demasiado lento. Es irreversible. | [270](270-muestreo-y-aliasing/README.md) |
| **Asimetría de KL** | KL(p‖q) ≠ KL(q‖p). Cada dirección penaliza un tipo distinto de error. | [264](264-divergencia-kl/README.md) |
| **Autocorrelación** | Correlación de la serie consigo misma desplazada. Revela periodicidad oculta. | [277](277-autocorrelacion/README.md) |
| **Bit y nat** | Unidades de información según se use log₂ o logaritmo natural. 1 nat ≈ 1,4427 bits. | [261](261-informacion-y-sorpresa/README.md) |
| **Centroide espectral** | Frecuencia media ponderada por potencia. Descriptor del brillo de una señal. | [280](280-capstone-analizar-senal-y-construir-features/README.md) |
| **Convolución** | Deslizar un núcleo invertido sobre una señal y sumar productos. Base del filtrado y de las CNN. | [271](271-convolucion/README.md) |
| **Correlación cruzada** | Como la convolución pero sin invertir el núcleo. Es lo que implementan las CNN. | [272](272-correlacion-de-senales/README.md) |
| **Código de Huffman** | Código de longitud variable óptimo entre los de prefijo, con símbolos frecuentes más cortos. | [268](268-codificacion-y-compresion/README.md) |
| **Código de prefijo** | Ningún código es prefijo de otro, lo que permite decodificar sin separadores. | [268](268-codificacion-y-compresion/README.md) |
| **Densidad espectral de potencia** | Reparto de la energía de la señal entre sus frecuencias. | [279](279-espectro-y-densidad-espectral/README.md) |
| **Diferenciación** | Restar el valor anterior a cada término. Elimina tendencias polinómicas. | [276](276-procesos-estacionarios/README.md) |
| **Distribución uniforme y entropía** | Entre distribuciones sobre n símbolos, la uniforme es la de máxima entropía: log n. | [262](262-entropia-de-shannon/README.md) |
| **Divergencia de Jensen-Shannon** | Media de las KL a la mezcla. Simétrica, acotada y su raíz es una métrica. | [265](265-jensen-shannon-divergence/README.md) |
| **Divergencia KL** | KL(p‖q) = H(p,q) − H(p). No negativa, cero solo si p = q, y no simétrica. | [264](264-divergencia-kl/README.md) |
| **Entropía cruzada** | H(p,q) = −Σ p·log q. Coste de codificar p con un código óptimo para q. | [263](263-entropia-cruzada/README.md) |
| **Entropía de Shannon** | H(p) = −Σ p·log p. Sorpresa esperada y límite inferior de compresión sin pérdida. | [262](262-entropia-de-shannon/README.md) |
| **Epsilon de estabilidad** | Constante minúscula que evita log(0) al calcular pérdidas logarítmicas. | [263](263-entropia-cruzada/README.md) |
| **Estacionariedad** | Media, varianza y autocovarianza que no cambian con el tiempo. | [276](276-procesos-estacionarios/README.md) |
| **FFT** | Algoritmo que calcula la DFT en O(n log n) en vez de O(n²). | [274](274-fft/README.md) |
| **Filtro paso-bajo** | Atenúa las frecuencias altas y conserva las bajas. Una media móvil es el caso más simple. | [275](275-filtros-y-respuesta-en-frecuencia/README.md) |
| **Frecuencia de muestreo** | Número de muestras por segundo tomadas de una señal continua. | [269](269-senales-discretas-y-continuas/README.md) |
| **Fuga espectral** | Energía que se dispersa a frecuencias vecinas al analizar un trozo finito de señal. | [278](278-series-temporales-y-ventanas/README.md) |
| **Independencia e información** | I(X;Y) = 0 si y solo si X e Y son independientes. Detecta relaciones no lineales. | [266](266-informacion-mutua/README.md) |
| **Información mutua** | I(X;Y) = H(X) − H(X|Y). Reducción de incertidumbre sobre X al conocer Y. | [266](266-informacion-mutua/README.md) |
| **Núcleo o kernel** | Vector o matriz pequeña que define la operación local de una convolución. | [271](271-convolucion/README.md) |
| **Principio de máxima entropía** | Entre las distribuciones compatibles con lo conocido, elegir la de mayor entropía. | [267](267-principio-de-maxima-entropia/README.md) |
| **Respuesta en frecuencia** | Cuánto atenúa o amplifica un filtro cada frecuencia. | [275](275-filtros-y-respuesta-en-frecuencia/README.md) |
| **Retardo o lag** | Desplazamiento temporal aplicado a la serie al calcular la autocorrelación. | [277](277-autocorrelacion/README.md) |
| **Sorpresa** | −log p(x). Información que aporta observar un evento. Cero si era seguro. | [261](261-informacion-y-sorpresa/README.md) |
| **Teorema de convolución** | Convolucionar en el tiempo equivale a multiplicar en frecuencia. | [274](274-fft/README.md) |
| **Teorema de Nyquist** | Hay que muestrear a más del doble de la frecuencia máxima presente en la señal. | [270](270-muestreo-y-aliasing/README.md) |
| **Teorema de Parseval** | La energía en el dominio del tiempo es igual a la energía en el dominio de la frecuencia. | [273](273-series-y-transformada-de-fourier/README.md) |
| **Transformada de Fourier** | Descompone una señal en sus componentes de frecuencia. Cambio de base a senos y cosenos. | [273](273-series-y-transformada-de-fourier/README.md) |
| **Ventaneo** | Multiplicar por una función que decae en los bordes antes de transformar. | [278](278-series-temporales-y-ventanas/README.md) |

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
