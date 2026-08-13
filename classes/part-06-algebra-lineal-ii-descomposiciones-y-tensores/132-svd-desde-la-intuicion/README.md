# 132 — SVD desde la intuición

**Parte:** 06 — Álgebra lineal II: descomposiciones y tensores
**Nivel:** intermedio-avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part06` · demostración `svd_intuition`

## 🎯 Propósito

Cambio de base, autovalores, diagonalización, LU, QR, mínimos cuadrados, SVD, pseudoinversa, PCA y álgebra tensorial.

Esta clase concreta ese objetivo sobre **SVD desde la intuición**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **SVD desde la intuición** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `svd_intuition` del motor de la parte.
4. Interpretar las 8 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: confundir el orden de los índices al reordenar un tensor.

## 🧠 Idea rectora de la parte 06

> La SVD existe para toda matriz, incluso no cuadrada y singular.

## 🧩 Qué calcula el laboratorio

`svd_intuition` — SVD: rotar, escalar, rotar. Existe siempre.

Salidas que devuelve:

- `A`
- `valores_singulares`
- `U`
- `V`
- `sigma1_es_la_norma_espectral`
- `numero_de_condicion`
- `rango_numerico`
- `existe_para_toda_matriz`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/132-svd-desde-la-intuicion/lab.py
```

o desde la CLI del programa:

```bash
compmath run 132
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Aplicar PCA sin centrar (ni escalar) los datos.
- Interpretar autovalores complejos como error de cálculo.
- Confundir el orden de los índices al reordenar un tensor.

## 🤖 Conexión con IA

LoRA factoriza matrices de bajo rango, la atención se define con productos tensoriales y la estabilidad del entrenamiento depende del espectro de los pesos.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Golub, G.; Van Loan, C. *Matrix Computations*. 4ª ed., Johns Hopkins, 2013.
- Trefethen, L. N.; Bau, D. *Numerical Linear Algebra*. SIAM, 1997.
- Kolda, T.; Bader, B. *Tensor Decompositions and Applications*. SIAM Review, 2009.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
