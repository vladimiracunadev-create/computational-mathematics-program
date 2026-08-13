# 238 — Introducción a PDE y discretización

**Parte:** 11 — Métodos numéricos y computación científica
**Nivel:** cientifico
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part11` · demostración `pde_discretization`

## 🎯 Propósito

Raíces, interpolación, splines, diferenciación y cuadratura numérica, sistemas lineales iterativos, mínimos cuadrados y ecuaciones diferenciales.

Esta clase concreta ese objetivo sobre **Introducción a PDE y discretización**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Introducción a PDE y discretización** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `pde_discretization` del motor de la parte.
4. Interpretar las 10 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: aplicar runge-kutta con paso fijo a un sistema rígido.

## 🧠 Idea rectora de la parte 11

> Interpolar de grado alto oscila (fenómeno de Runge): por eso existen los splines.

## 🧩 Qué calcula el laboratorio

`pde_discretization` — Discretización de la ecuación del calor en 1D (esquema explícito).

Salidas que devuelve:

- `ecuacion`
- `nodos`
- `dx`
- `dt`
- `numero_de_courant_alpha`
- `estable_si_alpha<=0.5`
- `pico_inicial`
- `pico_final_numerico`
- `pico_final_analitico`
- `error_maximo`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-11-metodos-numericos-y-computacion-cientifica/238-introduccion-a-pde-y-discretizacion/lab.py
```

o desde la CLI del programa:

```bash
compmath run 238
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Usar tolerancia absoluta cuando la escala del problema es grande.
- Iterar sin límite máximo y colgar el proceso.
- Aplicar Runge-Kutta con paso fijo a un sistema rígido.

## 🤖 Conexión con IA

Los Neural ODE, los samplers de difusión y los optimizadores de segundo orden son métodos numéricos con parámetros aprendidos.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Burden, R.; Faires, J. *Numerical Analysis*. 10ª ed., Cengage, 2015.
- Press, W. et al. *Numerical Recipes*. 3ª ed., Cambridge, 2007.
- Heath, M. *Scientific Computing: An Introductory Survey*. 2ª ed., SIAM, 2018.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
