# 266 — Información mutua

**Parte:** 13 — Teoría de la información, señales y series
**Nivel:** avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part13` · demostración `mutual_information`

## 🎯 Propósito

Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

Esta clase concreta ese objetivo sobre **Información mutua**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Información mutua** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `mutual_information` del motor de la parte.
4. Interpretar las 8 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: muestrear por debajo de nyquist y culpar al modelo del ruido resultante.

## 🧠 Idea rectora de la parte 13

> La entropía es el límite inferior de compresión sin pérdida.

## 🧩 Qué calcula el laboratorio

`mutual_information` — Información mutua: cuánto reduce Y la incertidumbre de X.

Salidas que devuelve:

- `conjunta_dependiente`
- `H(X)`
- `H(Y)`
- `I(X;Y)`
- `I_en_el_caso_independiente`
- `I=0_sii_independientes`
- `I(X;Y)=H(X)-H(X|Y)`
- `detecta_relaciones_no_lineales`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-13-teoria-de-la-informacion-senales-y-series/266-informacion-mutua/lab.py
```

o desde la CLI del programa:

```bash
compmath run 266
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
