# 107 — Independencia y dependencia lineal

**Parte:** 05 — Álgebra lineal I: vectores y matrices
**Nivel:** intermedio
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part05` · demostración `linear_independence`

## 🎯 Propósito

Vectores, normas, producto punto, independencia, span, sistemas lineales, eliminación de Gauss, rango, inversa, determinante y proyección ortogonal.

Esta clase concreta ese objetivo sobre **Independencia y dependencia lineal**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Independencia y dependencia lineal** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `linear_independence` del motor de la parte.
4. Interpretar las 8 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: invertir una matriz mal condicionada en lugar de factorizar.

## 🧠 Idea rectora de la parte 05

> El rango es la dimensión real de la salida, no el tamaño de la tabla.

## 🧩 Qué calcula el laboratorio

`linear_independence` — Independencia detectada por el rango, no por inspección.

Salidas que devuelve:

- `conjunto_A`
- `rango_A`
- `A_independiente`
- `conjunto_B`
- `rango_B`
- `B_independiente`
- `relacion_en_B`
- `determinante_B`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-05-algebra-lineal-i-vectores-y-matrices/107-independencia-y-dependencia-lineal/lab.py
```

o desde la CLI del programa:

```bash
compmath run 107
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Invertir una matriz mal condicionada en lugar de factorizar.
- Confundir dimensión del espacio con número de vectores.
- Aplicar producto punto a vectores de escalas incomparables.

## 🤖 Conexión con IA

Cada capa densa es un producto matriz-vector. Los embeddings viven en subespacios y la similitud entre ellos es producto punto normalizado.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Strang, G. *Introduction to Linear Algebra*. 6ª ed., Wellesley-Cambridge, 2023.
- Axler, S. *Linear Algebra Done Right*. 4ª ed., Springer, 2024.
- Trefethen, L. N.; Bau, D. *Numerical Linear Algebra*. SIAM, 1997.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
