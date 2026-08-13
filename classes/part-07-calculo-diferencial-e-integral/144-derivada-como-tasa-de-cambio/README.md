# 144 — Derivada como tasa de cambio

> [⬅️ 143 Continuidad](../143-continuidad/README.md) · [📚 Parte 07](../README.md) · [🏠 Programa](../../../README.md) · [145 Reglas de derivación ➡️](../145-reglas-de-derivacion/README.md)

**Parte:** 07 — Cálculo diferencial e integral · **Nivel:** `universitario` · **Horas estimadas:** 4
**Motor:** `engines.part07` · **Demostración:** `derivative_as_rate` · **Clase 4 de 20** de la parte

---

## 🎯 Propósito

Límite, continuidad, derivada, reglas de derivación, Taylor, optimización de una variable, integral definida y teorema fundamental del cálculo.

Esta clase concreta ese objetivo sobre **Derivada como tasa de cambio**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Derivada como tasa de cambio** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `derivative_as_rate`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: usar diferencias finitas con h demasiado pequeño y amplificar el error de redondeo.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["Clase 143 · Continuidad"] --> D
    subgraph CLASE["Clase 144 · Derivada como tasa de cambio"]
        direction TB
        D["Demostracion derivative_as_rate"]
        D --> R["Resultados 4: punto +3"]
        D --> V["Comprobaciones 1: la_central_es_de_orde…"]
        D --> O["Contexto 2: funcion +1"]
    end
    R --> N["Clase 145 · Reglas de derivación"]
    V -.-> IA["Aplicacion en IA · parte 07"]
```

## 🧠 Idea rectora de la parte 07

> Integrar es acumular; derivar e integrar son operaciones inversas.

## 🔬 Qué ejecuta el laboratorio

`derivative_as_rate` — Derivada como límite del cociente incremental.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (4) | `punto`, `derivada_exacta_2x`, `diferencia_central`, `error_central` |
| ✅ Comprobaciones de invariante (1) | `la_central_es_de_orden_h²` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-07-calculo-diferencial-e-integral/144-derivada-como-tasa-de-cambio/lab.py
compmath run 144
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Usar diferencias finitas con h demasiado pequeño y amplificar el error de redondeo.
- Derivar en un punto donde la función no es continua.
- Confundir punto crítico con extremo global.

## 🤖 Conexión con IA

Sin regla de la cadena no hay entrenamiento por gradiente; sin Taylor no hay métodos de segundo orden ni análisis de convergencia.

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
5. ¿Dónde aparece esto en física?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Spivak, M. *Calculus*. 4ª ed., Publish or Perish, 2008.
- Apostol, T. *Calculus, Vol. 1*. 2ª ed., Wiley, 1967.
- Strang, G. *Calculus*. 3ª ed., Wellesley-Cambridge, 2017.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 143 Continuidad](../143-continuidad/README.md) · [📚 Parte 07](../README.md) · [🏠 Programa](../../../README.md) · [145 Reglas de derivación ➡️](../145-reglas-de-derivacion/README.md)
