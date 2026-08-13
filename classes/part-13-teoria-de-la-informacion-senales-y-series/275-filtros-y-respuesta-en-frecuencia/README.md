# 275 — Filtros y respuesta en frecuencia

**Parte:** 13 — Teoría de la información, señales y series
**Nivel:** avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part13` · demostración `filters`

## 🎯 Propósito

Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

Esta clase concreta ese objetivo sobre **Filtros y respuesta en frecuencia**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Filtros y respuesta en frecuencia** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `filters` del motor de la parte.
4. Interpretar las 8 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: muestrear por debajo de nyquist y culpar al modelo del ruido resultante.

## 🧠 Idea rectora de la parte 13

> Convolución en el tiempo es multiplicación en frecuencia.

## 🧩 Qué calcula el laboratorio

`filters` — Filtro paso-bajo aplicado a una señal con ruido de alta frecuencia.

Salidas que devuelve:

- `muestras`
- `ventana_del_filtro`
- `RMSE_antes_del_filtro`
- `RMSE_despues_del_filtro`
- `mejora_%`
- `tipo`
- `coste`
- `compromiso`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-13-teoria-de-la-informacion-senales-y-series/275-filtros-y-respuesta-en-frecuencia/lab.py
```

o desde la CLI del programa:

```bash
compmath run 275
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
