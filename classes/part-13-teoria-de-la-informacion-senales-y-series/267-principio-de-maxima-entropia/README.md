# 267 — Principio de máxima entropía

> [⬅️ 266 Información mutua](../266-informacion-mutua/README.md) · [📚 Parte 13](../README.md) · [🏠 Programa](../../../README.md) · [268 Codificación y compresión ➡️](../268-codificacion-y-compresion/README.md)

**Parte:** 13 — Teoría de la información, señales y series · **Nivel:** `avanzado` · **Horas estimadas:** 4
**Motor:** `engines.part13` · **Demostración:** `max_entropy` · **Clase 7 de 20** de la parte

---

## 🎯 Propósito

Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

Esta clase concreta ese objetivo sobre **Principio de máxima entropía**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Principio de máxima entropía** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `max_entropy`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: calcular log(0) sin epsilon de estabilidad.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["266<br/>Información mutua"] --> C
    subgraph C["267 · Principio de máxima<br/>entropía"]
        direction TB
        D["Demostración<br/><code>max_entropy</code>"] --> R["Resultados numéricos<br/>entropia_maxima_teorica"]
        D --> V["Verificaciones<br/>sin_restricciones_gana_la_uniforme"]
        D --> O["Contexto y estructura<br/>candidatas<br/>medias<br/>maxima_entropia<br/>… +2 más"]
    end
    C --> N["268<br/>Codificación y<br/>compresión"]
    C -.-> IA["Uso en IA<br/>parte 13"]
```

## 🧠 Idea rectora de la parte 13

> Minimizar cross-entropy equivale a maximizar verosimilitud.

## 🔬 Qué ejecuta el laboratorio

`max_entropy` — Principio de máxima entropía: la distribución menos comprometida.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (1) | `entropia_maxima_teorica` |
| ✅ Comprobaciones de invariante (1) | `sin_restricciones_gana_la_uniforme` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-13-teoria-de-la-informacion-senales-y-series/267-principio-de-maxima-entropia/lab.py
compmath run 267
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

> [⬅️ 266 Información mutua](../266-informacion-mutua/README.md) · [📚 Parte 13](../README.md) · [🏠 Programa](../../../README.md) · [268 Codificación y compresión ➡️](../268-codificacion-y-compresion/README.md)
