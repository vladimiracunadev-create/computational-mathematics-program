# 128 — Formas cuadráticas

**Parte:** 06 — Álgebra lineal II: descomposiciones y tensores
**Nivel:** intermedio-avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part06` · demostración `quadratic_forms`

## 🎯 Propósito

Cambio de base, autovalores, diagonalización, LU, QR, mínimos cuadrados, SVD, pseudoinversa, PCA y álgebra tensorial.

Esta clase concreta ese objetivo sobre **Formas cuadráticas**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Formas cuadráticas** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `quadratic_forms` del motor de la parte.
4. Interpretar las 7 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: interpretar autovalores complejos como error de cálculo.

## 🧠 Idea rectora de la parte 06

> PCA es la SVD de los datos centrados: no hay magia estadística adicional.

## 🧩 Qué calcula el laboratorio

`quadratic_forms` — La forma cuadrática xᵀAx y sus curvas de nivel.

Salidas que devuelve:

- `A`
- `forma`
- `valores`
- `minimo_en_la_esfera_unitaria`
- `maximo_en_la_esfera_unitaria`
- `curvas_de_nivel`
- `gradiente_es_2Ax`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/128-formas-cuadraticas/lab.py
```

o desde la CLI del programa:

```bash
compmath run 128
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
