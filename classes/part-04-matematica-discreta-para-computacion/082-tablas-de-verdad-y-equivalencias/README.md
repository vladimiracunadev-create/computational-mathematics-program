# 082 — Tablas de verdad y equivalencias

> [⬅️ 081 Lógica proposicional](../081-logica-proposicional/README.md) · [📚 Parte 04](../README.md) · [🏠 Programa](../../../README.md) · [083 Lógica de predicados y cuantificadores ➡️](../083-logica-de-predicados-y-cuantificadores/README.md)

**Parte:** 04 — Matemática discreta para computación · **Nivel:** `intermedio` · **Horas estimadas:** 4
**Motor:** `engines.part04` · **Demostración:** `truth_tables` · **Clase 2 de 20** de la parte

---

## 🎯 Propósito

Lógica, conjuntos, conteo, inducción, recurrencias, grafos y aritmética modular: la matemática que hace demostrable un programa.

Esta clase concreta ese objetivo sobre **Tablas de verdad y equivalencias**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Tablas de verdad y equivalencias** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `truth_tables`.
4. Interpretar las 6 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: confundir implicación con equivalencia lógica.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["081<br/>Lógica proposicional"] --> C
    subgraph C["082 · Tablas de verdad y<br/>equivalencias"]
        direction TB
        D["Demostración<br/><code>truth_tables</code>"] --> R["Resultados numéricos<br/>casos_evaluados"]
        D --> V["Verificaciones<br/>¬(p∧q) ≡ ¬p∨¬q<br/>¬(p∨q) ≡ ¬p∧¬q<br/>tautologia_p∨¬p<br/>… +1 más"]
        D --> O["Contexto y estructura<br/>xor"]
    end
    C --> N["083<br/>Lógica de predicados y<br/>cuantificadores"]
    C -.-> IA["Uso en IA<br/>parte 04"]
```

## 🧠 Idea rectora de la parte 04

> Permutación cuenta orden; combinación cuenta selección.

## 🔬 Qué ejecuta el laboratorio

`truth_tables` — Leyes de De Morgan verificadas exhaustivamente.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (1) | `casos_evaluados` |
| ✅ Comprobaciones de invariante (4) | `¬(p∧q) ≡ ¬p∨¬q`, `¬(p∨q) ≡ ¬p∧¬q`, `tautologia_p∨¬p`, `contradiccion_p∧¬p` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-04-matematica-discreta-para-computacion/082-tablas-de-verdad-y-equivalencias/lab.py
compmath run 082
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Contar dos veces al aplicar el principio de inclusión-exclusión.
- Confundir implicación con equivalencia lógica.
- Asumir que un grafo dirigido es acíclico sin verificarlo.

## 🤖 Conexión con IA

Los grafos de cómputo, la búsqueda en árbol y las GNN son estructuras discretas; el conteo sostiene la probabilidad que después usa todo modelo generativo.

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
5. ¿Dónde aparece esto en algoritmos?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Rosen, K. *Discrete Mathematics and Its Applications*. 8ª ed., McGraw-Hill, 2019.
- Graham, R.; Knuth, D.; Patashnik, O. *Concrete Mathematics*. 2ª ed., Addison-Wesley, 1994.
- Cormen, T. et al. *Introduction to Algorithms*. 4ª ed., MIT Press, 2022.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 081 Lógica proposicional](../081-logica-proposicional/README.md) · [📚 Parte 04](../README.md) · [🏠 Programa](../../../README.md) · [083 Lógica de predicados y cuantificadores ➡️](../083-logica-de-predicados-y-cuantificadores/README.md)
