# 070 — Distancia punto-recta

> [⬅️ 069 Pendiente y ecuación de la recta](../069-pendiente-y-ecuacion-de-la-recta/README.md) · [📚 Parte 03](../README.md) · [🏠 Programa](../../../README.md) · [071 Circunferencias y cónicas ➡️](../071-circunferencias-y-conicas/README.md)

**Parte:** 03 — Geometría, trigonometría y geometría analítica · **Nivel:** `basico-intermedio` · **Horas estimadas:** 4
**Motor:** `engines.part03` · **Demostración:** `point_line_distance` · **Clase 10 de 20** de la parte

---

## 🎯 Propósito

Del espacio a las coordenadas: distancia, ángulo, trigonometría, transformaciones lineales en el plano, coordenadas polares y proyección.

Esta clase concreta ese objetivo sobre **Distancia punto-recta**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Distancia punto-recta** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `point_line_distance`.
4. Interpretar las 6 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: mezclar grados y radianes en la misma expresión.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["069<br/>Pendiente y ecuación<br/>de la recta"] --> C
    subgraph C["070 · Distancia punto-recta"]
        direction TB
        D["Demostración<br/><code>point_line_distance</code>"] --> R["Resultados numéricos<br/>distancia<br/>distancia_al_pie"]
        D --> V["Verificaciones<br/>el_pie_pertenece_a_la_recta"]
        D --> O["Contexto y estructura<br/>recta<br/>punto<br/>pie_de_perpendicular"]
    end
    C --> N["071<br/>Circunferencias y<br/>cónicas"]
    C -.-> IA["Uso en IA<br/>parte 03"]
```

## 🧠 Idea rectora de la parte 03

> Las coordenadas homogéneas convierten la traslación en multiplicación.

## 🔬 Qué ejecuta el laboratorio

`point_line_distance` — Distancia de un punto a una recta y su proyección.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (2) | `distancia`, `distancia_al_pie` |
| ✅ Comprobaciones de invariante (1) | `el_pie_pertenece_a_la_recta` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-03-geometria-trigonometria-y-geometria-analitica/070-distancia-punto-recta/lab.py
compmath run 070
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Mezclar grados y radianes en la misma expresión.
- Aplicar rotación y traslación en el orden equivocado.
- Olvidar normalizar antes de comparar direcciones.

## 🤖 Conexión con IA

Las transformaciones geométricas son el caso visual de las transformaciones lineales que una red aplica a sus activaciones; la similitud coseno es trigonometría en alta dimensión.

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
5. ¿Dónde aparece esto en gráficos por computador?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Hartley, R.; Zisserman, A. *Multiple View Geometry in Computer Vision*. 2ª ed., Cambridge, 2004.
- Coxeter, H. S. M. *Introduction to Geometry*. 2ª ed., Wiley, 1989.
- Lengyel, E. *Mathematics for 3D Game Programming and Computer Graphics*. 3ª ed., 2011.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 069 Pendiente y ecuación de la recta](../069-pendiente-y-ecuacion-de-la-recta/README.md) · [📚 Parte 03](../README.md) · [🏠 Programa](../../../README.md) · [071 Circunferencias y cónicas ➡️](../071-circunferencias-y-conicas/README.md)
