# 050 — Exponentes algebraicos

> [⬅️ 049 Fórmula cuadrática y discriminante](../049-formula-cuadratica-y-discriminante/README.md) · [📚 Parte 02](../README.md) · [🏠 Programa](../../../README.md) · [051 Logaritmos y sus propiedades ➡️](../051-logaritmos-y-sus-propiedades/README.md)

**Parte:** 02 — Álgebra y funciones · **Nivel:** `basico` · **Horas estimadas:** 4
**Motor:** `engines.part02` · **Demostración:** `algebraic_exponents` · **Clase 10 de 20** de la parte

---

## 🎯 Propósito

Manipulación simbólica con criterio y la función como objeto central: dominio, imagen, composición, inversa y familias lineal, cuadrática, exponencial y logarítmica.

Esta clase concreta ese objetivo sobre **Exponentes algebraicos**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Exponentes algebraicos** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `algebraic_exponents`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: dividir por una expresión que puede anularse y perder soluciones.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["049<br/>Fórmula cuadrática y<br/>discriminante"] --> C
    subgraph C["050 · Exponentes algebraicos"]
        direction TB
        D["Demostración<br/><code>algebraic_exponents</code>"] --> R["Resultados numéricos<br/>x^(1/3)<br/>x^(2/3)<br/>x^(-1)<br/>… +2 más"]
        D --> V["Verificaciones<br/>es_x"]
        D --> O["Contexto y estructura<br/>dominio_de_x^(1/2)"]
    end
    C --> N["051<br/>Logaritmos y sus<br/>propiedades"]
    C -.-> IA["Uso en IA<br/>parte 02"]
```

## 🧠 Idea rectora de la parte 02

> Componer funciones es la operación que después llamaremos «capa» en una red neuronal.

## 🔬 Qué ejecuta el laboratorio

`algebraic_exponents` — Exponentes negativos, fraccionarios y su dominio.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (5) | `x^(1/3)`, `x^(2/3)`, `x^(-1)`, `x^(-1/3)`, `producto_x^(1/3)*x^(2/3)` |
| ✅ Comprobaciones de invariante (1) | `es_x` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-02-algebra-y-funciones/050-exponentes-algebraicos/lab.py
compmath run 050
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Dividir por una expresión que puede anularse y perder soluciones.
- Aplicar log a valores no positivos sin declarar el dominio.
- Confundir función inversa con recíproco.

## 🤖 Conexión con IA

Una red neuronal es una composición de funciones parametrizadas. La sigmoide, la softmax y la log-verosimilitud son álgebra de exponenciales y logaritmos.

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
5. ¿Dónde aparece esto en modelado de crecimiento?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Axler, S. *Precalculus: A Prelude to Calculus*. 3ª ed., Wiley, 2017.
- Gelfand, I. M.; Glagoleva, E.; Shnol, E. *Functions and Graphs*. Dover, 2002.
- Stewart, J. *Precalculus: Mathematics for Calculus*. 7ª ed., Cengage, 2015.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 049 Fórmula cuadrática y discriminante](../049-formula-cuadratica-y-discriminante/README.md) · [📚 Parte 02](../README.md) · [🏠 Programa](../../../README.md) · [051 Logaritmos y sus propiedades ➡️](../051-logaritmos-y-sus-propiedades/README.md)
