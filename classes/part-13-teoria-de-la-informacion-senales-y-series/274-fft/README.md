# 274 — FFT

> [⬅️ 273 Series y transformada de Fourier](../273-series-y-transformada-de-fourier/README.md) · [📚 Parte 13](../README.md) · [🏠 Programa](../../../README.md) · [275 Filtros y respuesta en frecuencia ➡️](../275-filtros-y-respuesta-en-frecuencia/README.md)

**Parte:** 13 — Teoría de la información, señales y series · **Nivel:** `avanzado` · **Horas estimadas:** 4
**Motor:** `engines.part13` · **Demostración:** `fft` · **Clase 14 de 20** de la parte

---

## 🎯 Propósito

Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

Esta clase concreta ese objetivo sobre **FFT**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **FFT** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `fft`.
4. Interpretar las 9 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: comparar entropías calculadas en bases logarítmicas distintas.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["273<br/>Series y transformada<br/>de Fourier"] --> C
    subgraph C["274 · FFT"]
        direction TB
        D["Demostración<br/><code>fft</code>"] --> R["Resultados numéricos<br/>muestras<br/>operaciones_DFT<br/>operaciones_FFT<br/>… +1 más"]
        D --> V["Verificaciones<br/>coinciden<br/>fft_y_dft_coinciden"]
        D --> O["Contexto y estructura<br/>picos_detectados<br/>frecuencias_reales<br/>requisito_del_algoritmo_radix2"]
    end
    C --> N["275<br/>Filtros y respuesta en<br/>frecuencia"]
    C -.-> IA["Uso en IA<br/>parte 13"]
```

## 🧠 Idea rectora de la parte 13

> Nyquist fija la frecuencia mínima de muestreo; por debajo hay aliasing irreversible.

## 🔬 Qué ejecuta el laboratorio

`fft` — FFT frente a DFT: mismo resultado, coste muy distinto.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (4) | `muestras`, `operaciones_DFT`, `operaciones_FFT`, `factor_de_ahorro` |
| ✅ Comprobaciones de invariante (2) | `coinciden`, `fft_y_dft_coinciden` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-13-teoria-de-la-informacion-senales-y-series/274-fft/lab.py
compmath run 274
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Calcular log(0) sin epsilon de estabilidad.
- Comparar entropías calculadas en bases logarítmicas distintas.
- Muestrear por debajo de Nyquist y culpar al modelo del ruido resultante.

## 🤖 Conexión con IA

La función de pérdida de casi todo clasificador es entropía cruzada; el VAE optimiza un ELBO con un término KL; las CNN son convoluciones aprendidas.

## 📓 Notebooks

| Archivo | Para qué |
|---|---|
| [`notebook.ipynb`](notebook.ipynb) | recorrido guiado con la demostración ejecutada |
| [`notebook_student.ipynb`](notebook_student.ipynb) | versión con `TODO` para resolver |
| [`notebook_solution.ipynb`](notebook_solution.ipynb) | solución de referencia verificada |

## 📝 Evaluación

| Criterio | Peso |
|---|---:|
| Comprensión conceptual | 25 % |
| Resolución manual | 25 % |
| Implementación y verificación | 25 % |
| Interpretación y comunicación | 15 % |
| Conexión con aplicación real | 10 % |

Detalle y criterios de error crítico en [`assessment.md`](assessment.md).

## ❓ Preguntas de comprobación

1. ¿Cuál es la entrada, cuál la salida y qué unidades tienen?
2. ¿Qué operación domina el comportamiento del resultado?
3. ¿Qué caso extremo revelaría un error conceptual?
4. ¿Cómo verificarías el resultado por un método independiente?
5. ¿Dónde aparece esto en compresión?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Cover, T.; Thomas, J. *Elements of Information Theory*. 2ª ed., Wiley, 2006.
- MacKay, D. *Information Theory, Inference, and Learning Algorithms*. Cambridge, 2003.
- Oppenheim, A.; Schafer, R. *Discrete-Time Signal Processing*. 3ª ed., Pearson, 2009.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 273 Series y transformada de Fourier](../273-series-y-transformada-de-fourier/README.md) · [📚 Parte 13](../README.md) · [🏠 Programa](../../../README.md) · [275 Filtros y respuesta en frecuencia ➡️](../275-filtros-y-respuesta-en-frecuencia/README.md)
