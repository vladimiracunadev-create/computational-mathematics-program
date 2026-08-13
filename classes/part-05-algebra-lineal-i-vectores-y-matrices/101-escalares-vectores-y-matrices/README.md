# 101 — Escalares, vectores y matrices

> [⬅️ 100 Capstone: modelar dependencias con grafos](../../part-04-matematica-discreta-para-computacion/100-capstone-modelar-dependencias-con-grafos/README.md) · [📚 Parte 05](../README.md) · [🏠 Programa](../../../README.md) · [102 Operaciones con vectores ➡️](../102-operaciones-con-vectores/README.md)

**Parte:** 05 — Álgebra lineal I: vectores y matrices · **Nivel:** `intermedio` · **Horas estimadas:** 4
**Motor:** `engines.part05` · **Demostración:** `scalars_vectors_matrices` · **Clase 1 de 20** de la parte

---

## 🎯 Propósito

Vectores, normas, producto punto, independencia, span, sistemas lineales, eliminación de Gauss, rango, inversa, determinante y proyección ortogonal.

Esta clase concreta ese objetivo sobre **Escalares, vectores y matrices**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Escalares, vectores y matrices** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `scalars_vectors_matrices`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: invertir una matriz mal condicionada en lugar de factorizar.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["100<br/>Capstone: modelar<br/>dependencias con<br/>grafos"] --> C
    subgraph C["101 · Escalares, vectores y<br/>matrices"]
        direction TB
        D["Demostración<br/><code>scalars_vectors_matrices</code>"] --> R["Resultados numéricos<br/>escalar"]
        D --> V["Verificaciones<br/>un_tensor_de_orden_0_es_un_escalar"]
        D --> O["Contexto y estructura<br/>vector<br/>shape_vector<br/>matriz<br/>… +3 más"]
    end
    C --> N["102<br/>Operaciones con<br/>vectores"]
    C -.-> IA["Uso en IA<br/>parte 05"]
```

## 🧠 Idea rectora de la parte 05

> Una matriz es una función lineal escrita en una base concreta.

## 🔬 Qué ejecuta el laboratorio

`scalars_vectors_matrices` — Escalar, vector y matriz como objetos con forma y significado.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (1) | `escalar` |
| ✅ Comprobaciones de invariante (1) | `un_tensor_de_orden_0_es_un_escalar` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-05-algebra-lineal-i-vectores-y-matrices/101-escalares-vectores-y-matrices/lab.py
compmath run 101
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Invertir una matriz mal condicionada en lugar de factorizar.
- Confundir dimensión del espacio con número de vectores.
- Aplicar producto punto a vectores de escalas incomparables.

## 🤖 Conexión con IA

Cada capa densa es un producto matriz-vector. Los embeddings viven en subespacios y la similitud entre ellos es producto punto normalizado.

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
5. ¿Dónde aparece esto en sistemas de recomendación?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Strang, G. *Introduction to Linear Algebra*. 6ª ed., Wellesley-Cambridge, 2023.
- Axler, S. *Linear Algebra Done Right*. 4ª ed., Springer, 2024.
- Trefethen, L. N.; Bau, D. *Numerical Linear Algebra*. SIAM, 1997.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 100 Capstone: modelar dependencias con grafos](../../part-04-matematica-discreta-para-computacion/100-capstone-modelar-dependencias-con-grafos/README.md) · [📚 Parte 05](../README.md) · [🏠 Programa](../../../README.md) · [102 Operaciones con vectores ➡️](../102-operaciones-con-vectores/README.md)
