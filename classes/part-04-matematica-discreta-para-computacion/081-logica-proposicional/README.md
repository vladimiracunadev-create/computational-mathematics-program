# 081 — Lógica proposicional

**Parte:** 04 — Matemática discreta para computación
**Nivel:** intermedio
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part04` · demostración `propositional_logic`

## 🎯 Propósito

Lógica, conjuntos, conteo, inducción, recurrencias, grafos y aritmética modular: la matemática que hace demostrable un programa.

Esta clase concreta ese objetivo sobre **Lógica proposicional**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Lógica proposicional** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `propositional_logic` del motor de la parte.
4. Interpretar las 4 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: contar dos veces al aplicar el principio de inclusión-exclusión.

## 🧠 Idea rectora de la parte 04

> Una demostración por inducción es un bucle `for` con garantía.

## 🧩 Qué calcula el laboratorio

`propositional_logic` — Implicación, contrarrecíproca y recíproca no son lo mismo.

Salidas que devuelve:

- `tabla`
- `implicacion_equivale_a_contrarreciproca`
- `implicacion_equivale_a_reciproca`
- `vacuamente_verdadera`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-04-matematica-discreta-para-computacion/081-logica-proposicional/lab.py
```

o desde la CLI del programa:

```bash
compmath run 081
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Contar dos veces al aplicar el principio de inclusión-exclusión.
- Confundir implicación con equivalencia lógica.
- Asumir que un grafo dirigido es acíclico sin verificarlo.

## 🤖 Conexión con IA

Los grafos de cómputo, la búsqueda en árbol y las GNN son estructuras discretas; el conteo sostiene la probabilidad que después usa todo modelo generativo.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Rosen, K. *Discrete Mathematics and Its Applications*. 8ª ed., McGraw-Hill, 2019.
- Graham, R.; Knuth, D.; Patashnik, O. *Concrete Mathematics*. 2ª ed., Addison-Wesley, 1994.
- Cormen, T. et al. *Introduction to Algorithms*. 4ª ed., MIT Press, 2022.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
