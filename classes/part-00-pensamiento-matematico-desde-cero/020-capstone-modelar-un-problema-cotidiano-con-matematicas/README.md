# 020 — Capstone: modelar un problema cotidiano con matemáticas

**Parte:** 00 — Pensamiento matemático desde cero
**Nivel:** cero-absoluto
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part00` · demostración `capstone_budget_model`

## 🎯 Propósito

Reconstruye la aritmética y el lenguaje matemático básico con el rigor que exige escribir código: cada número tiene dominio, unidad y representación.

Esta clase concreta ese objetivo sobre **Capstone: modelar un problema cotidiano con matemáticas**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Capstone: modelar un problema cotidiano con matemáticas** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `capstone_budget_model` del motor de la parte.
4. Interpretar las 6 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: confundir aumento del 50 % con multiplicar por 50.

## 🧠 Idea rectora de la parte 00

> Un contraejemplo derrumba una regla; mil ejemplos favorables no la demuestran.

## 🧩 Qué calcula el laboratorio

`capstone_budget_model` — Capstone: modelar un presupuesto con dinero exacto y proporciones.

Salidas que devuelve:

- `ingreso`
- `porcentajes_suman_1`
- `montos`
- `total_asignado`
- `descuadre_por_redondeo`
- `meses_para_ahorrar_5M`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-00-pensamiento-matematico-desde-cero/020-capstone-modelar-un-problema-cotidiano-con-matematicas/lab.py
```

o desde la CLI del programa:

```bash
compmath run 020
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
