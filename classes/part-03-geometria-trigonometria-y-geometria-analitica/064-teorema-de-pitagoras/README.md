# 064 — Teorema de Pitágoras

**Parte:** 03 — Geometría, trigonometría y geometría analítica
**Nivel:** basico-intermedio
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part03` · demostración `pythagoras`

## 🎯 Propósito

Del espacio a las coordenadas: distancia, ángulo, trigonometría, transformaciones lineales en el plano, coordenadas polares y proyección.

Esta clase concreta ese objetivo sobre **Teorema de Pitágoras**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Teorema de Pitágoras** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `pythagoras` del motor de la parte.
4. Interpretar las 7 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: mezclar grados y radianes en la misma expresión.

## 🧠 Idea rectora de la parte 03

> Componer transformaciones es multiplicar matrices, y el orden importa.

## 🧩 Qué calcula el laboratorio

`pythagoras` — Pitágoras, su recíproco y una terna pitagórica generada.

Salidas que devuelve:

- `catetos`
- `hipotenusa`
- `a²+b²`
- `c²`
- `es_rectangulo`
- `generador_(m,n)`
- `triangulo_5_5_7_es_rectangulo`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-03-geometria-trigonometria-y-geometria-analitica/064-teorema-de-pitagoras/lab.py
```

o desde la CLI del programa:

```bash
compmath run 064
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Mezclar grados y radianes en la misma expresión.
- Aplicar rotación y traslación en el orden equivocado.
- Olvidar normalizar antes de comparar direcciones.

## 🤖 Conexión con IA

Las transformaciones geométricas son el caso visual de las transformaciones lineales que una red aplica a sus activaciones; la similitud coseno es trigonometría en alta dimensión.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Hartley, R.; Zisserman, A. *Multiple View Geometry in Computer Vision*. 2ª ed., Cambridge, 2004.
- Coxeter, H. S. M. *Introduction to Geometry*. 2ª ed., Wiley, 1989.
- Lengyel, E. *Mathematics for 3D Game Programming and Computer Graphics*. 3ª ed., 2011.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
