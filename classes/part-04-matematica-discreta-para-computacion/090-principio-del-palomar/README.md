# 090 — Principio del palomar

> [⬅️ 089 Combinaciones](../089-combinaciones/README.md) · [📚 Parte 04](../README.md) · [🏠 Programa](../../../README.md) · [091 Inducción matemática ➡️](../091-induccion-matematica/README.md)

**Parte:** 04 — Matemática discreta para computación · **Nivel:** `intermedio` · **Horas estimadas:** 4
**Motor:** `engines.part04` · **Demostración:** `pigeonhole` · **Clase 10 de 20** de la parte

---

## 🎯 Propósito

Lógica, conjuntos, conteo, inducción, recurrencias, grafos y aritmética modular: la matemática que hace demostrable un programa.

Esta clase concreta ese objetivo sobre **Principio del palomar**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Principio del palomar** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `pigeonhole`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: contar dos veces al aplicar el principio de inclusión-exclusión.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["089<br/>Combinaciones"] --> C
    subgraph C["090 · Principio del palomar"]
        direction TB
        D["Demostración<br/><code>pigeonhole</code>"] --> R["Resultados numéricos<br/>personas<br/>dias_del_año<br/>minimo_repeticiones<br/>… +2 más"]
        D --> V["Verificaciones<br/>coincidencia_de_cumpleaños_garantizada<br/>colision_garantizada"]
        D --> O["Contexto y estructura<br/>leccion"]
    end
    C --> N["091<br/>Inducción matemática"]
    C -.-> IA["Uso en IA<br/>parte 04"]
```

## 🧠 Idea rectora de la parte 04

> El principio del palomar demuestra colisiones sin construir un ejemplo.

## 🔬 Qué ejecuta el laboratorio

`pigeonhole` — Principio del palomar: colisiones garantizadas sin construirlas.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (5) | `personas`, `dias_del_año`, `minimo_repeticiones`, `espacio_hash`, `entradas` |
| ✅ Comprobaciones de invariante (2) | `coincidencia_de_cumpleaños_garantizada`, `colision_garantizada` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-04-matematica-discreta-para-computacion/090-principio-del-palomar/lab.py
compmath run 090
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

> [⬅️ 089 Combinaciones](../089-combinaciones/README.md) · [📚 Parte 04](../README.md) · [🏠 Programa](../../../README.md) · [091 Inducción matemática ➡️](../091-induccion-matematica/README.md)
