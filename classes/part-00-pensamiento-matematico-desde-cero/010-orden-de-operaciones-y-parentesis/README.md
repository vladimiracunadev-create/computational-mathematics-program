# 010 — Orden de operaciones y paréntesis

**Parte:** 00 — Pensamiento matemático desde cero
**Nivel:** cero-absoluto
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part00` · demostración `operator_precedence`

## 🎯 Propósito

Reconstruye la aritmética y el lenguaje matemático básico con el rigor que exige escribir código: cada número tiene dominio, unidad y representación.

Esta clase concreta ese objetivo sobre **Orden de operaciones y paréntesis**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Orden de operaciones y paréntesis** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `operator_precedence` del motor de la parte.
4. Interpretar las 6 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: sumar porcentajes como si fueran cantidades absolutas.

## 🧠 Idea rectora de la parte 00

> Un contraejemplo derrumba una regla; mil ejemplos favorables no la demuestran.

## 🧩 Qué calcula el laboratorio

`operator_precedence` — Precedencia y asociatividad: dos lecturas de la misma cadena.

Salidas que devuelve:

- `2+3*4`
- `(2+3)*4`
- `2**3**2 (asocia derecha)`
- `(2**3)**2`
- `-3**2`
- `(-3)**2`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-00-pensamiento-matematico-desde-cero/010-orden-de-operaciones-y-parentesis/lab.py
```

o desde la CLI del programa:

```bash
compmath run 010
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Sumar porcentajes como si fueran cantidades absolutas.
- Confundir aumento del 50 % con multiplicar por 50.
- Escribir 1/3 como 0.33 y arrastrar el error a todo el cálculo.

## 🤖 Conexión con IA

Toda métrica de un modelo (accuracy, loss, learning rate) es una razón, un porcentaje o una escala. Interpretarlas mal es el primer error de un practicante de IA.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Lang, S. *Basic Mathematics*. Springer, 1988.
- Gelfand, I. M.; Shen, A. *Algebra*. Birkhäuser, 2002.
- Polya, G. *How to Solve It*. Princeton University Press, 1945.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
