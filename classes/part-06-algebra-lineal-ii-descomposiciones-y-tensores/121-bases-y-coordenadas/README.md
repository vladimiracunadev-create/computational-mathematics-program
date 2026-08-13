# 121 — Bases y coordenadas

**Parte:** 06 — Álgebra lineal II: descomposiciones y tensores
**Nivel:** intermedio-avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part06` · demostración `bases_coordinates`

## 🎯 Propósito

Cambio de base, autovalores, diagonalización, LU, QR, mínimos cuadrados, SVD, pseudoinversa, PCA y álgebra tensorial.

Esta clase concreta ese objetivo sobre **Bases y coordenadas**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Bases y coordenadas** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `bases_coordinates` del motor de la parte.
4. Interpretar las 7 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: aplicar pca sin centrar (ni escalar) los datos.

## 🧠 Idea rectora de la parte 06

> Diagonalizar es elegir la base donde la transformación solo escala.

## 🧩 Qué calcula el laboratorio

`bases_coordinates` — Las coordenadas dependen de la base elegida.

Salidas que devuelve:

- `vector_en_base_canonica`
- `base_alternativa`
- `coordenadas_en_la_nueva_base`
- `reconstruccion`
- `el_vector_no_cambia`
- `lo_que_cambia`
- `base_es_independiente`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-06-algebra-lineal-ii-descomposiciones-y-tensores/121-bases-y-coordenadas/lab.py
```

o desde la CLI del programa:

```bash
compmath run 121
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
