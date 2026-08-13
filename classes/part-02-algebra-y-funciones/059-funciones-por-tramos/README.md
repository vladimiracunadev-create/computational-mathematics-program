# 059 — Funciones por tramos

> [⬅️ 058 Funciones inversas](../058-funciones-inversas/README.md) · [📚 Parte 02](../README.md) · [🏠 Programa](../../../README.md) · [060 Capstone: construir y comparar modelos funcionales ➡️](../060-capstone-construir-y-comparar-modelos-funcionales/README.md)

**Parte:** 02 — Álgebra y funciones · **Nivel:** `basico` · **Horas estimadas:** 4
**Motor:** `engines.part02` · **Demostración:** `piecewise_function` · **Clase 19 de 20** de la parte

---

## 🎯 Propósito

Manipulación simbólica con criterio y la función como objeto central: dominio, imagen, composición, inversa y familias lineal, cuadrática, exponencial y logarítmica.

Esta clase concreta ese objetivo sobre **Funciones por tramos**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Funciones por tramos** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `piecewise_function`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: dividir por una expresión que puede anularse y perder soluciones.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["058<br/>Funciones inversas"] --> C
    subgraph C["059 · Funciones por tramos"]
        direction TB
        D["Demostración<br/><code>piecewise_function</code>"] --> R["Resultados numéricos<br/>f(-3)<br/>f(0)<br/>f(1.999)<br/>… +1 más"]
        D --> V["Verificaciones<br/>continua_en_0<br/>continua_en_2<br/>relu_es_por_tramos"]
        D --> O["Contexto y estructura<br/>definicion"]
    end
    C --> N["060<br/>Capstone: construir y<br/>comparar modelos<br/>funcionales"]
    C -.-> IA["Uso en IA<br/>parte 02"]
```

## 🧠 Idea rectora de la parte 02

> El logaritmo convierte producto en suma: por eso aparece en toda función de pérdida.

## 🔬 Qué ejecuta el laboratorio

`piecewise_function` — Una función por tramos y su continuidad en el punto de corte.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (4) | `f(-3)`, `f(0)`, `f(1.999)`, `f(2)` |
| ✅ Comprobaciones de invariante (3) | `continua_en_0`, `continua_en_2`, `relu_es_por_tramos` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-02-algebra-y-funciones/059-funciones-por-tramos/lab.py
compmath run 059
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

> [⬅️ 058 Funciones inversas](../058-funciones-inversas/README.md) · [📚 Parte 02](../README.md) · [🏠 Programa](../../../README.md) · [060 Capstone: construir y comparar modelos funcionales ➡️](../060-capstone-construir-y-comparar-modelos-funcionales/README.md)
