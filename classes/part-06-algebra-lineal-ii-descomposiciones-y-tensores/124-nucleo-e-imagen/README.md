# 124 — Núcleo e imagen

> [⬅️ 123 Transformaciones lineales](../123-transformaciones-lineales/README.md) · [📚 Parte 06](../README.md) · [🏠 Programa](../../../README.md) · [125 Autovalores y autovectores ➡️](../125-autovalores-y-autovectores/README.md)

**Parte:** 06 — Álgebra lineal II: descomposiciones y tensores · **Nivel:** `intermedio-avanzado` · **Horas estimadas:** 4
**Motor:** `engines.part06` · **Demostración:** `kernel_image` · **Clase 4 de 20** de la parte

---

## 🎯 Propósito

Cambio de base, autovalores, diagonalización, LU, QR, mínimos cuadrados, SVD, pseudoinversa, PCA y álgebra tensorial.

Esta clase concreta ese objetivo sobre **Núcleo e imagen**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Núcleo e imagen** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `kernel_image`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: aplicar pca sin centrar (ni escalar) los datos.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["Clase 123 · Transformaciones lineales"] --> D
    subgraph CLASE["Clase 124 · Núcleo e imagen"]
        direction TB
        D["Demostracion kernel_image"]
        D --> R["Resultados 4: columnas +3"]
        D --> V["Comprobaciones 1: teorema_verificado"]
        D --> O["Contexto 3: A +2"]
    end
    R --> N["Clase 125 · Autovalores y autovectores"]
    V -.-> IA["Aplicacion en IA · parte 06"]
```

## 🧠 Idea rectora de la parte 06

> El número de condición es el cociente entre el mayor y el menor valor singular.

## 🔬 Qué ejecuta el laboratorio

`kernel_image` — Núcleo, imagen y teorema del rango-nulidad.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (4) | `columnas`, `rango_(dim_imagen)`, `nulidad_(dim_nucleo)`, `rango+nulidad` |
| ✅ Comprobaciones de invariante (1) | `teorema_verificado` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/124-nucleo-e-imagen/lab.py
compmath run 124
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Aplicar PCA sin centrar (ni escalar) los datos.
- Interpretar autovalores complejos como error de cálculo.
- Confundir el orden de los índices al reordenar un tensor.

## 🤖 Conexión con IA

LoRA factoriza matrices de bajo rango, la atención se define con productos tensoriales y la estabilidad del entrenamiento depende del espectro de los pesos.

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
5. ¿Dónde aparece esto en compresión?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Golub, G.; Van Loan, C. *Matrix Computations*. 4ª ed., Johns Hopkins, 2013.
- Trefethen, L. N.; Bau, D. *Numerical Linear Algebra*. SIAM, 1997.
- Kolda, T.; Bader, B. *Tensor Decompositions and Applications*. SIAM Review, 2009.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 123 Transformaciones lineales](../123-transformaciones-lineales/README.md) · [📚 Parte 06](../README.md) · [🏠 Programa](../../../README.md) · [125 Autovalores y autovectores ➡️](../125-autovalores-y-autovectores/README.md)
