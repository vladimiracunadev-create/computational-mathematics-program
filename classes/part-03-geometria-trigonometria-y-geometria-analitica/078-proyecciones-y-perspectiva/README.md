# 078 — Proyecciones y perspectiva

> [⬅️ 077 Geometría 3D y planos](../077-geometria-3d-y-planos/README.md) · [📚 Parte 03](../README.md) · [🏠 Programa](../../../README.md) · [079 Aplicaciones en visión, robótica y videojuegos ➡️](../079-aplicaciones-en-vision-robotica-y-videojuegos/README.md)

**Parte:** 03 — Geometría, trigonometría y geometría analítica · **Nivel:** `basico-intermedio` · **Horas estimadas:** 4
**Motor:** `engines.part03` · **Demostración:** `projection` · **Clase 18 de 20** de la parte

---

## 🎯 Propósito

Del espacio a las coordenadas: distancia, ángulo, trigonometría, transformaciones lineales en el plano, coordenadas polares y proyección.

Esta clase concreta ese objetivo sobre **Proyecciones y perspectiva**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Proyecciones y perspectiva** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `projection`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: olvidar normalizar antes de comparar direcciones.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["077<br/>Geometría 3D y planos"] --> C
    subgraph C["078 · Proyecciones y perspectiva"]
        direction TB
        D["Demostración<br/><code>projection</code>"] --> R["Resultados numéricos<br/>perspectiva_x'_con_f=2_z=5"]
        D --> V["Verificaciones<br/>residuo_ortogonal_a_u<br/>pitagoras<br/>objetos_lejanos_se_encogen"]
        D --> O["Contexto y estructura<br/>v<br/>direccion_u<br/>proyeccion<br/>… +1 más"]
    end
    C --> N["079<br/>Aplicaciones en<br/>visión, robótica y<br/>videojuegos"]
    C -.-> IA["Uso en IA<br/>parte 03"]
```

## 🧠 Idea rectora de la parte 03

> El producto punto mide alineación; la norma mide magnitud.

## 🔬 Qué ejecuta el laboratorio

`projection` — Proyección ortogonal de un vector y proyección en perspectiva.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (1) | `perspectiva_x'_con_f=2_z=5` |
| ✅ Comprobaciones de invariante (3) | `residuo_ortogonal_a_u`, `pitagoras`, `objetos_lejanos_se_encogen` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-03-geometria-trigonometria-y-geometria-analitica/078-proyecciones-y-perspectiva/lab.py
compmath run 078
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Mezclar grados y radianes en la misma expresión.
- Aplicar rotación y traslación en el orden equivocado.
- Olvidar normalizar antes de comparar direcciones.

## 🤖 Conexión con IA

Las transformaciones geométricas son el caso visual de las transformaciones lineales que una red aplica a sus activaciones; la similitud coseno es trigonometría en alta dimensión.

## 📓 Notebooks

| Archivo | Para qué |
|---|---|
| [`notebook.ipynb`](notebook.ipynb) | recorrido guiado con la demostración ejecutada |
| [`notebook_student.ipynb`](notebook_student.ipynb) | versión con `TODO` para resolver |
| [`notebook_solution.ipynb`](notebook_solution.ipynb) | solución de referencia verificada |

## 📝 Evaluación

| Criterio | Peso |
|---|---:|
| Comprensión conceptual | 25 % |
| Resolución manual | 25 % |
| Implementación y verificación | 25 % |
| Interpretación y comunicación | 15 % |
| Conexión con aplicación real | 10 % |

Detalle y criterios de error crítico en [`assessment.md`](assessment.md).

## ❓ Preguntas de comprobación

1. ¿Cuál es la entrada, cuál la salida y qué unidades tienen?
2. ¿Qué operación domina el comportamiento del resultado?
3. ¿Qué caso extremo revelaría un error conceptual?
4. ¿Cómo verificarías el resultado por un método independiente?
5. ¿Dónde aparece esto en gráficos por computador?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Hartley, R.; Zisserman, A. *Multiple View Geometry in Computer Vision*. 2ª ed., Cambridge, 2004.
- Coxeter, H. S. M. *Introduction to Geometry*. 2ª ed., Wiley, 1989.
- Lengyel, E. *Mathematics for 3D Game Programming and Computer Graphics*. 3ª ed., 2011.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 077 Geometría 3D y planos](../077-geometria-3d-y-planos/README.md) · [📚 Parte 03](../README.md) · [🏠 Programa](../../../README.md) · [079 Aplicaciones en visión, robótica y videojuegos ➡️](../079-aplicaciones-en-vision-robotica-y-videojuegos/README.md)
