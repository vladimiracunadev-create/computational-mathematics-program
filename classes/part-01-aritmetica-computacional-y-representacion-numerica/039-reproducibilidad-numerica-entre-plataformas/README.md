# 039 — Reproducibilidad numérica entre plataformas

> [⬅️ 038 Racional exacto y Fraction](../038-racional-exacto-y-fraction/README.md) · [📚 Parte 01](../README.md) · [🏠 Programa](../../../README.md) · [040 Capstone: auditor de precisión numérica ➡️](../040-capstone-auditor-de-precision-numerica/README.md)

**Parte:** 01 — Aritmética computacional y representación numérica · **Nivel:** `basico-computacional` · **Horas estimadas:** 4
**Motor:** `engines.part01` · **Demostración:** `reproducibility` · **Clase 19 de 20** de la parte

---

## 🎯 Propósito

Qué es realmente un número dentro de una máquina: bits, complemento a dos, IEEE 754, error, condicionamiento y estabilidad.

Esta clase concreta ese objetivo sobre **Reproducibilidad numérica entre plataformas**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Reproducibilidad numérica entre plataformas** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `reproducibility`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: comparar floats con `==` en lugar de una tolerancia razonada.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["038<br/>Racional exacto y<br/>Fraction"] --> C
    subgraph C["039 · Reproducibilidad numérica<br/>entre plataformas"]
        direction TB
        D["Demostración<br/><code>reproducibility</code>"] --> R["Resultados numéricos<br/>suma_de_izquierda_a_derecha<br/>suma_de_derecha_a_izquierda<br/>suma_compensada"]
        D --> V["Verificaciones<br/>coinciden<br/>suma_es_asociativa_en_R<br/>suma_es_asociativa_en_float64"]
        D --> O["Contexto y estructura<br/>valores"]
    end
    C --> N["040<br/>Capstone: auditor de<br/>precisión numérica"]
    C -.-> IA["Uso en IA<br/>parte 01"]
```

## 🧠 Idea rectora de la parte 01

> La cancelación catastrófica destruye dígitos significativos sin lanzar excepciones.

## 🔬 Qué ejecuta el laboratorio

`reproducibility` — El orden de la suma cambia el resultado en punto flotante.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (3) | `suma_de_izquierda_a_derecha`, `suma_de_derecha_a_izquierda`, `suma_compensada` |
| ✅ Comprobaciones de invariante (3) | `coinciden`, `suma_es_asociativa_en_R`, `suma_es_asociativa_en_float64` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-01-aritmetica-computacional-y-representacion-numerica/039-reproducibilidad-numerica-entre-plataformas/lab.py
compmath run 039
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

> [⬅️ 038 Racional exacto y Fraction](../038-racional-exacto-y-fraction/README.md) · [📚 Parte 01](../README.md) · [🏠 Programa](../../../README.md) · [040 Capstone: auditor de precisión numérica ➡️](../040-capstone-auditor-de-precision-numerica/README.md)
