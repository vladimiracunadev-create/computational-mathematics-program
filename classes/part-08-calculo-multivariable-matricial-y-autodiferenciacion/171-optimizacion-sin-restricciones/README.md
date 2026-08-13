# 171 — Optimización sin restricciones

> [⬅️ 170 Taylor multivariable](../170-taylor-multivariable/README.md) · [📚 Parte 08](../README.md) · [🏠 Programa](../../../README.md) · [172 Multiplicadores de Lagrange ➡️](../172-multiplicadores-de-lagrange/README.md)

**Parte:** 08 — Cálculo multivariable, matricial y autodiferenciación · **Nivel:** `universitario-avanzado` · **Horas estimadas:** 4
**Motor:** `engines.part08` · **Demostración:** `unconstrained_optimization` · **Clase 11 de 20** de la parte

---

## 🎯 Propósito

Derivadas parciales, gradiente, Jacobiano, Hessiano, Taylor multivariable, multiplicadores de Lagrange, cálculo matricial y autodiferenciación.

Esta clase concreta ese objetivo sobre **Optimización sin restricciones**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Optimización sin restricciones** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `unconstrained_optimization`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: suponer que el hessiano es definido positivo sin comprobarlo.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["170<br/>Taylor multivariable"] --> C
    subgraph C["171 · Optimización sin<br/>restricciones"]
        direction TB
        D["Demostración<br/><code>unconstrained_optimization</code>"] --> R["Resultados numéricos<br/>learning_rate"]
        D --> V["Verificaciones<br/>convergio"]
        D --> O["Contexto y estructura<br/>funcion<br/>minimo_teorico<br/>historial<br/>… +2 más"]
    end
    C --> N["172<br/>Multiplicadores de<br/>Lagrange"]
    C -.-> IA["Uso en IA<br/>parte 08"]
```

## 🧠 Idea rectora de la parte 08

> El gradiente apunta al mayor ascenso; por eso se desciende en su dirección opuesta.

## 🔬 Qué ejecuta el laboratorio

`unconstrained_optimization` — Descenso de gradiente sobre una cuadrática con historial.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (1) | `learning_rate` |
| ✅ Comprobaciones de invariante (1) | `convergio` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/171-optimizacion-sin-restricciones/lab.py
compmath run 171
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Confundir la convención de layout (numerador vs denominador) en cálculo matricial.
- Suponer que el Hessiano es definido positivo sin comprobarlo.
- Olvidar acumular gradientes cuando un nodo se reutiliza en el grafo.

## 🤖 Conexión con IA

Autograd de PyTorch y JAX es exactamente el modo reverso del grafo de cómputo que se construye en esta parte a mano.

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
5. ¿Dónde aparece esto en optimización multivariable?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Petersen, K.; Pedersen, M. *The Matrix Cookbook*. 2012.
- Baydin, A. et al. *Automatic Differentiation in Machine Learning: a Survey*. JMLR, 2018.
- Magnus, J.; Neudecker, H. *Matrix Differential Calculus*. 3ª ed., Wiley, 2019.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 170 Taylor multivariable](../170-taylor-multivariable/README.md) · [📚 Parte 08](../README.md) · [🏠 Programa](../../../README.md) · [172 Multiplicadores de Lagrange ➡️](../172-multiplicadores-de-lagrange/README.md)
