# 273 — Series y transformada de Fourier

**Parte:** 13 — Teoría de la información, señales y series
**Nivel:** avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part13` · demostración `fourier_series`

## 🎯 Propósito

Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

Esta clase concreta ese objetivo sobre **Series y transformada de Fourier**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Series y transformada de Fourier** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `fourier_series` del motor de la parte.
4. Interpretar las 8 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: calcular log(0) sin epsilon de estabilidad.

## 🧠 Idea rectora de la parte 13

> KL no es simétrica ni es una distancia; JS sí es simétrica.

## 🧩 Qué calcula el laboratorio

`fourier_series` — Descomponer una señal en senos y cosenos.

Salidas que devuelve:

- `muestras`
- `componentes_reales`
- `picos_detectados_Hz`
- `magnitudes_de_los_picos`
- `energia_en_el_tiempo`
- `energia_en_frecuencia`
- `teorema_de_Parseval`
- `cualquier_periodica_es_suma_de_senoidales`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-13-teoria-de-la-informacion-senales-y-series/273-series-y-transformada-de-fourier/lab.py
```

o desde la CLI del programa:

```bash
compmath run 273
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Calcular log(0) sin epsilon de estabilidad.
- Comparar entropías calculadas en bases logarítmicas distintas.
- Muestrear por debajo de Nyquist y culpar al modelo del ruido resultante.

## 🤖 Conexión con IA

La función de pérdida de casi todo clasificador es entropía cruzada; el VAE optimiza un ELBO con un término KL; las CNN son convoluciones aprendidas.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Cover, T.; Thomas, J. *Elements of Information Theory*. 2ª ed., Wiley, 2006.
- MacKay, D. *Information Theory, Inference, and Learning Algorithms*. Cambridge, 2003.
- Oppenheim, A.; Schafer, R. *Discrete-Time Signal Processing*. 3ª ed., Pearson, 2009.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
