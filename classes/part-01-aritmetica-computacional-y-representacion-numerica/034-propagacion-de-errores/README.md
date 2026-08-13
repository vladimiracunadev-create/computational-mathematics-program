# 034 — Propagación de errores

**Parte:** 01 — Aritmética computacional y representación numérica
**Nivel:** basico-computacional
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part01` · demostración `error_propagation`

## 🎯 Propósito

Qué es realmente un número dentro de una máquina: bits, complemento a dos, IEEE 754, error, condicionamiento y estabilidad.

Esta clase concreta ese objetivo sobre **Propagación de errores**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Propagación de errores** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `error_propagation` del motor de la parte.
4. Interpretar las 7 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: suponer que la suma de floats es asociativa.

## 🧠 Idea rectora de la parte 01

> La cancelación catastrófica destruye dígitos significativos sin lanzar excepciones.

## 🧩 Qué calcula el laboratorio

`error_propagation` — Cómo crece el error al sumar 10^6 veces un valor no representable.

Salidas que devuelve:

- `n_sumas`
- `suma_acumulada`
- `valor_exacto`
- `error_absoluto`
- `error_relativo`
- `suma_compensada_fsum`
- `recomendacion`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-01-aritmetica-computacional-y-representacion-numerica/034-propagacion-de-errores/lab.py
```

o desde la CLI del programa:

```bash
compmath run 034
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Comparar floats con `==` en lugar de una tolerancia razonada.
- Suponer que la suma de floats es asociativa.
- Usar float para dinero en vez de Decimal o enteros de centavos.

## 🤖 Conexión con IA

float32, bfloat16 y la cuantización a int8 son decisiones de representación. Los NaN en un entrenamiento casi siempre nacen aquí, no en la arquitectura.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Goldberg, D. *What Every Computer Scientist Should Know About Floating-Point Arithmetic*. ACM Computing Surveys, 1991.
- Higham, N. J. *Accuracy and Stability of Numerical Algorithms*. 2ª ed., SIAM, 2002.
- IEEE 754-2019 Standard for Floating-Point Arithmetic.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
