# 044 — Desigualdades lineales

**Parte:** 02 — Álgebra y funciones
**Nivel:** basico
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part02` · demostración `linear_inequality`

## 🎯 Propósito

Manipulación simbólica con criterio y la función como objeto central: dominio, imagen, composición, inversa y familias lineal, cuadrática, exponencial y logarítmica.

Esta clase concreta ese objetivo sobre **Desigualdades lineales**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Desigualdades lineales** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `linear_inequality` del motor de la parte.
4. Interpretar las 6 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: dividir por una expresión que puede anularse y perder soluciones.

## 🧠 Idea rectora de la parte 02

> El logaritmo convierte producto en suma: por eso aparece en toda función de pérdida.

## 🧩 Qué calcula el laboratorio

`linear_inequality` — Multiplicar por un negativo invierte el sentido de la desigualdad.

Salidas que devuelve:

- `desigualdad`
- `frontera`
- `solucion`
- `verifica_x=-5`
- `verifica_x=0`
- `regla`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-02-algebra-y-funciones/044-desigualdades-lineales/lab.py
```

o desde la CLI del programa:

```bash
compmath run 044
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Dividir por una expresión que puede anularse y perder soluciones.
- Aplicar log a valores no positivos sin declarar el dominio.
- Confundir función inversa con recíproco.

## 🤖 Conexión con IA

Una red neuronal es una composición de funciones parametrizadas. La sigmoide, la softmax y la log-verosimilitud son álgebra de exponenciales y logaritmos.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Axler, S. *Precalculus: A Prelude to Calculus*. 3ª ed., Wiley, 2017.
- Gelfand, I. M.; Glagoleva, E.; Shnol, E. *Functions and Graphs*. Dover, 2002.
- Stewart, J. *Precalculus: Mathematics for Calculus*. 7ª ed., Cengage, 2015.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
