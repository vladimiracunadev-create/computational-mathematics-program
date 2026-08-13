# 258 — Optimización cuadrática

**Parte:** 12 — Optimización matemática y computacional
**Nivel:** avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part12` · demostración `quadratic_programming`

## 🎯 Propósito

Función objetivo, convexidad, descenso de gradiente y su familia completa de optimizadores, métodos de segundo orden, restricciones, KKT y optimización evolutiva.

Esta clase concreta ese objetivo sobre **Optimización cuadrática**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Optimización cuadrática** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `quadratic_programming` del motor de la parte.
4. Interpretar las 11 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: declarar convergencia por número de épocas y no por criterio numérico.

## 🧠 Idea rectora de la parte 12

> Momentum promedia gradientes; Adam además normaliza por su escala.

## 🧩 Qué calcula el laboratorio

`quadratic_programming` — Programa cuadrático resuelto por su sistema KKT.

Salidas que devuelve:

- `Q`
- `c`
- `A`
- `b`
- `Q_definida_positiva`
- `sistema_KKT`
- `solucion_x`
- `multiplicador_lambda`
- `restriccion_satisfecha`
- `valor_objetivo`
- `problema_convexo`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-12-optimizacion-matematica-y-computacional/258-optimizacion-cuadratica/lab.py
```

o desde la CLI del programa:

```bash
compmath run 258
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Comparar optimizadores sin fijar semilla ni presupuesto de iteraciones.
- Aplicar weight decay dentro del gradiente en Adam (y no como AdamW).
- Declarar convergencia por número de épocas y no por criterio numérico.

## 🤖 Conexión con IA

AdamW es el optimizador por defecto del entrenamiento moderno; entender su actualización explica el weight decay, el warmup y el gradient clipping.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Boyd, S.; Vandenberghe, L. *Convex Optimization*. Cambridge, 2004.
- Nocedal, J.; Wright, S. *Numerical Optimization*. 2ª ed., Springer, 2006.
- Loshchilov, I.; Hutter, F. *Decoupled Weight Decay Regularization*. ICLR, 2019.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
