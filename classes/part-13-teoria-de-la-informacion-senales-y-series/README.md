# Parte 13 — Teoría de la información, señales y series

**Nivel:** avanzado
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part13.py`

Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

## 🧠 Ideas centrales

- La entropía es el límite inferior de compresión sin pérdida.
- Minimizar cross-entropy equivale a maximizar verosimilitud.
- KL no es simétrica ni es una distancia; JS sí es simétrica.
- Nyquist fija la frecuencia mínima de muestreo; por debajo hay aliasing irreversible.
- Convolución en el tiempo es multiplicación en frecuencia.

## 🤖 Por qué importa en IA

La función de pérdida de casi todo clasificador es entropía cruzada; el VAE optimiza un ELBO con un término KL; las CNN son convoluciones aprendidas.

## ⚠️ Errores frecuentes

- Calcular log(0) sin epsilon de estabilidad.
- Comparar entropías calculadas en bases logarítmicas distintas.
- Muestrear por debajo de Nyquist y culpar al modelo del ruido resultante.

## 🧰 Stack de referencia

`math`, `cmath`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [261 — Información y sorpresa](261-informacion-y-sorpresa/README.md)
2. [262 — Entropía de Shannon](262-entropia-de-shannon/README.md)
3. [263 — Entropía cruzada](263-entropia-cruzada/README.md)
4. [264 — Divergencia KL](264-divergencia-kl/README.md)
5. [265 — Jensen-Shannon divergence](265-jensen-shannon-divergence/README.md)
6. [266 — Información mutua](266-informacion-mutua/README.md)
7. [267 — Principio de máxima entropía](267-principio-de-maxima-entropia/README.md)
8. [268 — Codificación y compresión](268-codificacion-y-compresion/README.md)
9. [269 — Señales discretas y continuas](269-senales-discretas-y-continuas/README.md)
10. [270 — Muestreo y aliasing](270-muestreo-y-aliasing/README.md)
11. [271 — Convolución](271-convolucion/README.md)
12. [272 — Correlación de señales](272-correlacion-de-senales/README.md)
13. [273 — Series y transformada de Fourier](273-series-y-transformada-de-fourier/README.md)
14. [274 — FFT](274-fft/README.md)
15. [275 — Filtros y respuesta en frecuencia](275-filtros-y-respuesta-en-frecuencia/README.md)
16. [276 — Procesos estacionarios](276-procesos-estacionarios/README.md)
17. [277 — Autocorrelación](277-autocorrelacion/README.md)
18. [278 — Series temporales y ventanas](278-series-temporales-y-ventanas/README.md)
19. [279 — Espectro y densidad espectral](279-espectro-y-densidad-espectral/README.md)
20. [280 — Capstone: analizar señal y construir features](280-capstone-analizar-senal-y-construir-features/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 13
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Cover, T.; Thomas, J. *Elements of Information Theory*. 2ª ed., Wiley, 2006.
- MacKay, D. *Information Theory, Inference, and Learning Algorithms*. Cambridge, 2003.
- Oppenheim, A.; Schafer, R. *Discrete-Time Signal Processing*. 3ª ed., Pearson, 2009.
