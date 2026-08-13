# 238 — Introducción a PDE y discretización

> [⬅️ 237 Runge-Kutta](../237-runge-kutta/README.md) · [📚 Parte 11](../README.md) · [🏠 Programa](../../../README.md) · [239 Computación científica con SciPy ➡️](../239-computacion-cientifica-con-scipy/README.md)

**Parte:** 11 — Métodos numéricos y computación científica · **Nivel:** `cientifico` · **Horas estimadas:** 4
**Motor:** `engines.part11` · **Demostración:** `pde_discretization` · **Clase 18 de 20** de la parte

---

## 🎯 Propósito

Raíces, interpolación, splines, diferenciación y cuadratura numérica, sistemas lineales iterativos, mínimos cuadrados y ecuaciones diferenciales.

Esta clase concreta ese objetivo sobre **Introducción a PDE y discretización**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Introducción a PDE y discretización** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `pde_discretization`.
4. Interpretar las 10 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: aplicar runge-kutta con paso fijo a un sistema rígido.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["237<br/>Runge-Kutta"] --> C
    subgraph C["238 · Introducción a PDE y<br/>discretización"]
        direction TB
        D["Demostración<br/><code>pde_discretization</code>"] --> R["Resultados numéricos<br/>nodos<br/>dx<br/>dt<br/>… +5 más"]
        D --> V["Verificaciones<br/>estable_si_alpha<=0.5"]
        D --> O["Contexto y estructura<br/>ecuacion"]
    end
    C --> N["239<br/>Computación científica<br/>con SciPy"]
    C -.-> IA["Uso en IA<br/>parte 11"]
```

## 🧠 Idea rectora de la parte 11

> Interpolar de grado alto oscila (fenómeno de Runge): por eso existen los splines.

## 🔬 Qué ejecuta el laboratorio

`pde_discretization` — Discretización de la ecuación del calor en 1D (esquema explícito).

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (8) | `nodos`, `dx`, `dt`, `numero_de_courant_alpha`, `pico_inicial`, `pico_final_numerico`, `pico_final_analitico`, `error_maximo` |
| ✅ Comprobaciones de invariante (1) | `estable_si_alpha<=0.5` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-11-metodos-numericos-y-computacion-cientifica/238-introduccion-a-pde-y-discretizacion/lab.py
compmath run 238
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Usar tolerancia absoluta cuando la escala del problema es grande.
- Iterar sin límite máximo y colgar el proceso.
- Aplicar Runge-Kutta con paso fijo a un sistema rígido.

## 🤖 Conexión con IA

Los Neural ODE, los samplers de difusión y los optimizadores de segundo orden son métodos numéricos con parámetros aprendidos.

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
5. ¿Dónde aparece esto en simulación física?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Burden, R.; Faires, J. *Numerical Analysis*. 10ª ed., Cengage, 2015.
- Press, W. et al. *Numerical Recipes*. 3ª ed., Cambridge, 2007.
- Heath, M. *Scientific Computing: An Introductory Survey*. 2ª ed., SIAM, 2018.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 237 Runge-Kutta](../237-runge-kutta/README.md) · [📚 Parte 11](../README.md) · [🏠 Programa](../../../README.md) · [239 Computación científica con SciPy ➡️](../239-computacion-cientifica-con-scipy/README.md)
