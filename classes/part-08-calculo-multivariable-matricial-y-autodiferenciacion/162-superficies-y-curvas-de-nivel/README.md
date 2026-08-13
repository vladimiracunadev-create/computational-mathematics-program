# 162 — Superficies y curvas de nivel

**Parte:** 08 — Cálculo multivariable, matricial y autodiferenciación
**Nivel:** universitario-avanzado
**Duración estimada:** 4 h
**Motor:** `computational_math.engines.part08` · demostración `level_curves`

## 🎯 Propósito

Derivadas parciales, gradiente, Jacobiano, Hessiano, Taylor multivariable, multiplicadores de Lagrange, cálculo matricial y autodiferenciación.

Esta clase concreta ese objetivo sobre **Superficies y curvas de nivel**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Superficies y curvas de nivel** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `level_curves` del motor de la parte.
4. Interpretar las 7 salidas del laboratorio y decir qué invariante comprueba cada una.
5. Detectar el error típico de esta parte: suponer que el hessiano es definido positivo sin comprobarlo.

## 🧠 Idea rectora de la parte 08

> El Jacobiano generaliza la derivada a funciones vectoriales.

## 🧩 Qué calcula el laboratorio

`level_curves` — Curvas de nivel: dónde la función vale lo mismo.

Salidas que devuelve:

- `funcion`
- `nivel`
- `puntos_del_nivel`
- `forma_geometrica`
- `gradiente_en_(2,0)`
- `gradiente_perpendicular_a_la_curva`
- `curvas_mas_juntas`

## 🧪 Cómo ejecutarlo

```bash
python classes/part-08-calculo-multivariable-matricial-y-autodiferenciacion/162-superficies-y-curvas-de-nivel/lab.py
```

o desde la CLI del programa:

```bash
compmath run 162
```

Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
esperabas enseña tanto como uno que te contradice, pero solo si la predicción
existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Confundir la convención de layout (numerador vs denominador) en cálculo matricial.
- Suponer que el Hessiano es definido positivo sin comprobarlo.
- Olvidar acumular gradientes cuando un nodo se reutiliza en el grafo.

## 🤖 Conexión con IA

Autograd de PyTorch y JAX es exactamente el modo reverso del grafo de cómputo que se construye en esta parte a mano.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado sin
citar código: qué entra, qué sale, qué invariante se comprueba y qué pasaría en
un caso límite.

## 📚 Referencias de la parte

- Petersen, K.; Pedersen, M. *The Matrix Cookbook*. 2012.
- Baydin, A. et al. *Automatic Differentiation in Machine Learning: a Survey*. JMLR, 2018.
- Magnus, J.; Neudecker, H. *Matrix Differential Calculus*. 3ª ed., Wiley, 2019.

## 🔗 Siguiente paso

[`where-is-this-used.md`](where-is-this-used.md) conecta esta clase con las rutas
especializadas del ecosistema.
