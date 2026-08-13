# 060 — Capstone: construir y comparar modelos funcionales

**Parte:** 02 — Álgebra y funciones
**Nivel:** basico
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part02` · demostración `capstone_model_fitting`

## 🎯 Propósito

Manipulación simbólica con criterio y la función como objeto central: dominio, imagen, composición, inversa y familias lineal, cuadrática, exponencial y logarítmica.

Esta clase concreta ese objetivo sobre **Capstone: construir y comparar modelos funcionales**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Capstone: construir y comparar modelos funcionales** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `capstone_model_fitting` del motor de la parte.
4. Interpretar las 7 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: aplicar log a valores no positivos sin declarar el dominio.

## 🧠 Idea rectora de la parte 02

> Componer funciones es la operación que después llamaremos «capa» en una red neuronal.

## 🧩 Qué calcula el laboratorio

`capstone_model_fitting` — Capstone: ¿lineal, cuadrático o exponencial? Decidir con residuos.

Salidas que devuelve:

- `datos`
- `modelo_lineal_SSE`
- `modelo_exponencial`
- `modelo_exponencial_SSE`
- `razon_de_crecimiento`
- `modelo_elegido`
- `criterio`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-02-algebra-y-funciones/060-capstone-construir-y-comparar-modelos-funcionales/lab.py
```

o desde la CLI del programa:

```bash
compmath run 060
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
