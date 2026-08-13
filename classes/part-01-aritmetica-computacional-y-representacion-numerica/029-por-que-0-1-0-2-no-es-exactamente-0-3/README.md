# 029 — Por qué 0.1 + 0.2 no es exactamente 0.3

> [⬅️ 028 IEEE 754: estructura de un float](../028-ieee-754-estructura-de-un-float/README.md) · [📚 Parte 01](../README.md) · [🏠 Programa](../../../README.md) · [030 Error absoluto y error relativo ➡️](../030-error-absoluto-y-error-relativo/README.md)

**Parte:** 01 — Aritmética computacional y representación numérica · **Nivel:** `basico-computacional` · **Horas estimadas:** 4
**Motor:** `engines.part01` · **Demostración:** `why_point_one` · **Clase 9 de 20** de la parte

---

## 🎯 Propósito

Qué es realmente un número dentro de una máquina: bits, complemento a dos, IEEE 754, error, condicionamiento y estabilidad.

Esta clase concreta ese objetivo sobre **Por qué 0.1 + 0.2 no es exactamente 0.3**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Por qué 0.1 + 0.2 no es exactamente 0.3** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `why_point_one`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: usar float para dinero en vez de decimal o enteros de centavos.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["028<br/>IEEE 754: estructura<br/>de un float"] --> C
    subgraph C["029 · Por qué 0.1 + 0.2 no es<br/>exactamente 0.3"]
        direction TB
        D["Demostración<br/><code>why_point_one</code>"] --> R["Resultados numéricos<br/>0.1+0.2<br/>0.3<br/>diferencia"]
        D --> V["Verificaciones<br/>iguales<br/>comparacion_correcta"]
        D --> O["Contexto y estructura<br/>0.1_como_fraccion_exacta<br/>0.1_con_50_digitos"]
    end
    C --> N["030<br/>Error absoluto y error<br/>relativo"]
    C -.-> IA["Uso en IA<br/>parte 01"]
```

## 🧠 Idea rectora de la parte 01

> La cancelación catastrófica destruye dígitos significativos sin lanzar excepciones.

## 🔬 Qué ejecuta el laboratorio

`why_point_one` — 0.1 + 0.2 != 0.3 explicado con la fracción binaria real.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (3) | `0.1+0.2`, `0.3`, `diferencia` |
| ✅ Comprobaciones de invariante (2) | `iguales`, `comparacion_correcta` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-01-aritmetica-computacional-y-representacion-numerica/029-por-que-0-1-0-2-no-es-exactamente-0-3/lab.py
compmath run 029
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Comparar floats con `==` en lugar de una tolerancia razonada.
- Suponer que la suma de floats es asociativa.
- Usar float para dinero en vez de Decimal o enteros de centavos.

## 🤖 Conexión con IA

float32, bfloat16 y la cuantización a int8 son decisiones de representación. Los NaN en un entrenamiento casi siempre nacen aquí, no en la arquitectura.

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
5. ¿Dónde aparece esto en motores numéricos?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Goldberg, D. *What Every Computer Scientist Should Know About Floating-Point Arithmetic*. ACM Computing Surveys, 1991.
- Higham, N. J. *Accuracy and Stability of Numerical Algorithms*. 2ª ed., SIAM, 2002.
- IEEE 754-2019 Standard for Floating-Point Arithmetic.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 028 IEEE 754: estructura de un float](../028-ieee-754-estructura-de-un-float/README.md) · [📚 Parte 01](../README.md) · [🏠 Programa](../../../README.md) · [030 Error absoluto y error relativo ➡️](../030-error-absoluto-y-error-relativo/README.md)
