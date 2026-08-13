# 061 — Puntos, segmentos y distancias

> [⬅️ 060 Capstone: construir y comparar modelos funcionales](../../part-02-algebra-y-funciones/060-capstone-construir-y-comparar-modelos-funcionales/README.md) · [📚 Parte 03](../README.md) · [🏠 Programa](../../../README.md) · [062 Ángulos y radianes ➡️](../062-angulos-y-radianes/README.md)

**Parte:** 03 — Geometría, trigonometría y geometría analítica · **Nivel:** `basico-intermedio` · **Horas estimadas:** 4
**Motor:** `engines.part03` · **Demostración:** `distances` · **Clase 1 de 20** de la parte

---

## 🎯 Propósito

Del espacio a las coordenadas: distancia, ángulo, trigonometría, transformaciones lineales en el plano, coordenadas polares y proyección.

Esta clase concreta ese objetivo sobre **Puntos, segmentos y distancias**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Puntos, segmentos y distancias** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `distances`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: mezclar grados y radianes en la misma expresión.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["060<br/>Capstone: construir y<br/>comparar modelos<br/>funcionales"] --> C
    subgraph C["061 · Puntos, segmentos y<br/>distancias"]
        direction TB
        D["Demostración<br/><code>distances</code>"] --> R["Resultados numéricos<br/>euclidea_L2<br/>manhattan_L1<br/>chebyshev_Linf"]
        D --> V["Verificaciones<br/>orden_L1>=L2>=Linf"]
        D --> O["Contexto y estructura<br/>p<br/>q<br/>punto_medio"]
    end
    C --> N["062<br/>Ángulos y radianes"]
    C -.-> IA["Uso en IA<br/>parte 03"]
```

## 🧠 Idea rectora de la parte 03

> El radián no es una unidad decorativa: es la que hace que d(sin x)/dx = cos x.

## 🔬 Qué ejecuta el laboratorio

`distances` — Distancia euclídea, Manhattan y Chebyshev sobre los mismos puntos.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (3) | `euclidea_L2`, `manhattan_L1`, `chebyshev_Linf` |
| ✅ Comprobaciones de invariante (1) | `orden_L1>=L2>=Linf` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-03-geometria-trigonometria-y-geometria-analitica/061-puntos-segmentos-y-distancias/lab.py
compmath run 061
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

> [⬅️ 060 Capstone: construir y comparar modelos funcionales](../../part-02-algebra-y-funciones/060-capstone-construir-y-comparar-modelos-funcionales/README.md) · [📚 Parte 03](../README.md) · [🏠 Programa](../../../README.md) · [062 Ángulos y radianes ➡️](../062-angulos-y-radianes/README.md)
