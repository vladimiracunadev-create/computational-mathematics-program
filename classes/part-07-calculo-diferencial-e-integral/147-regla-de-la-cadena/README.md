# 147 — Regla de la cadena

**Parte:** 07 — Cálculo diferencial e integral
**Nivel:** universitario
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part07` · demostración `chain_rule`

## 🎯 Propósito

Límite, continuidad, derivada, reglas de derivación, Taylor, optimización de una variable, integral definida y teorema fundamental del cálculo.

Esta clase concreta ese objetivo sobre **Regla de la cadena**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Regla de la cadena** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `chain_rule` del motor de la parte.
4. Interpretar las 9 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: usar diferencias finitas con h demasiado pequeño y amplificar el error de redondeo.

## 🧠 Idea rectora de la parte 07

> La regla de la cadena es el mecanismo entero de backpropagation.

## 🧩 Qué calcula el laboratorio

`chain_rule` — La regla de la cadena: el mecanismo entero de backpropagation.

Salidas que devuelve:

- `composicion`
- `x`
- `df/du_en_g(x)`
- `dg/dx`
- `producto_de_la_cadena`
- `derivada_numerica`
- `coinciden`
- `cadena_de_3_niveles`
- `en_deep_learning`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-07-calculo-diferencial-e-integral/147-regla-de-la-cadena/lab.py
```

o desde la CLI del programa:

```bash
compmath run 147
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Usar diferencias finitas con h demasiado pequeño y amplificar el error de redondeo.
- Derivar en un punto donde la función no es continua.
- Confundir punto crítico con extremo global.

## 🤖 Conexión con IA

Sin regla de la cadena no hay entrenamiento por gradiente; sin Taylor no hay métodos de segundo orden ni análisis de convergencia.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Spivak, M. *Calculus*. 4ª ed., Publish or Perish, 2008.
- Apostol, T. *Calculus, Vol. 1*. 2ª ed., Wiley, 1967.
- Strang, G. *Calculus*. 3ª ed., Wellesley-Cambridge, 2017.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
