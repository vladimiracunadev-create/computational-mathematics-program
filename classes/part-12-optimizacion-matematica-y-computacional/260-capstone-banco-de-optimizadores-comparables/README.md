# 260 — Capstone: banco de optimizadores comparables

**Parte:** 12 — Optimización matemática y computacional
**Nivel:** avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part12` · demostración `capstone_optimizer_bench`

## 🎯 Propósito

Función objetivo, convexidad, descenso de gradiente y su familia completa de optimizadores, métodos de segundo orden, restricciones, KKT y optimización evolutiva.

Esta clase concreta ese objetivo sobre **Capstone: banco de optimizadores comparables**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Capstone: banco de optimizadores comparables** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `capstone_optimizer_bench` del motor de la parte.
4. Interpretar las 9 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: aplicar weight decay dentro del gradiente en adam (y no como adamw).

## 🧠 Idea rectora de la parte 12

> KKT generaliza Lagrange a restricciones de desigualdad.

## 🧩 Qué calcula el laboratorio

`capstone_optimizer_bench` — Capstone: banco comparable de optimizadores con presupuesto idéntico.

Salidas que devuelve:

- `protocolo`
- `banco`
- `mejor_en_cuadratica`
- `mejor_en_rosenbrock`
- `divergieron_en_rosenbrock`
- `el_mismo_lr_no_sirve_para_ambos_problemas`
- `ningun_optimizador_gana_siempre`
- `leccion`
- `condicion_de_comparabilidad`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-12-optimizacion-matematica-y-computacional/260-capstone-banco-de-optimizadores-comparables/lab.py
```

o desde la CLI del programa:

```bash
compmath run 260
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
