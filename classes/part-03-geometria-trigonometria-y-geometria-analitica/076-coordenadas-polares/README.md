# 076 — Coordenadas polares

**Parte:** 03 — Geometría, trigonometría y geometría analítica
**Nivel:** basico-intermedio
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part03` · demostración `polar_coordinates`

## 🎯 Propósito

Del espacio a las coordenadas: distancia, ángulo, trigonometría, transformaciones lineales en el plano, coordenadas polares y proyección.

Esta clase concreta ese objetivo sobre **Coordenadas polares**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Coordenadas polares** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `polar_coordinates` del motor de la parte.
4. Interpretar las 7 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: mezclar grados y radianes en la misma expresión.

## 🧠 Idea rectora de la parte 03

> El radián no es una unidad decorativa: es la que hace que d(sin x)/dx = cos x.

## 🧩 Qué calcula el laboratorio

`polar_coordinates` — Conversión cartesiana ↔ polar y su ida y vuelta.

Salidas que devuelve:

- `cartesianas`
- `r`
- `theta_rad`
- `theta_grados`
- `vuelta_a_cartesianas`
- `roundtrip_ok`
- `atan2_maneja_cuadrantes`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-03-geometria-trigonometria-y-geometria-analitica/076-coordenadas-polares/lab.py
```

o desde la CLI del programa:

```bash
compmath run 076
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
