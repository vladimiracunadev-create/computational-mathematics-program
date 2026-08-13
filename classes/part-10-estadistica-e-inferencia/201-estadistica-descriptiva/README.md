# 201 — Estadística descriptiva

> [⬅️ 200 Capstone: simulador probabilístico y bayesiano](../../part-09-probabilidad-y-procesos-aleatorios/200-capstone-simulador-probabilistico-y-bayesiano/README.md) · [📚 Parte 10](../README.md) · [🏠 Programa](../../../README.md) · [202 Población, muestra y sesgo de selección ➡️](../202-poblacion-muestra-y-sesgo-de-seleccion/README.md)

**Parte:** 10 — Estadística e inferencia · **Nivel:** `universitario-avanzado` · **Horas estimadas:** 4
**Motor:** `engines.part10` · **Demostración:** `descriptive_statistics` · **Clase 1 de 20** de la parte

---

## 🎯 Propósito

Descriptiva, muestreo, estimadores, intervalos de confianza, pruebas de hipótesis, p-value, potencia, verosimilitud, MAP, inferencia bayesiana, bootstrap y A/B testing.

Esta clase concreta ese objetivo sobre **Estadística descriptiva**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Estadística descriptiva** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `descriptive_statistics`.
4. Interpretar las 10 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: p-hacking por comparaciones múltiples sin corrección.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["200<br/>Capstone: simulador<br/>probabilístico y<br/>bayesiano"] --> C
    subgraph C["201 · Estadística descriptiva"]
        direction TB
        D["Demostración<br/><code>descriptive_statistics</code>"] --> R["Resultados numéricos<br/>n<br/>media<br/>mediana<br/>… +7 más"]
        D --> V["Verificaciones<br/>—"]
        D --> O["Contexto y estructura<br/>—"]
    end
    C --> N["202<br/>Población, muestra y<br/>sesgo de selección"]
    C -.-> IA["Uso en IA<br/>parte 10"]
```

## 🧠 Idea rectora de la parte 10

> El p-value es P(datos tan extremos | H0), nunca P(H0 | datos).

## 🔬 Qué ejecuta el laboratorio

`descriptive_statistics` — Centro, dispersión y forma: tres preguntas distintas.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (10) | `n`, `media`, `mediana`, `desviacion_estandar`, `rango`, `Q1`, `Q3`, `IQR`, `coeficiente_de_variacion_%`, `asimetria_aprox` |
| ✅ Comprobaciones de invariante (0) | — |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-10-estadistica-e-inferencia/201-estadistica-descriptiva/lab.py
compmath run 201
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- p-hacking por comparaciones múltiples sin corrección.
- Confundir significancia estadística con relevancia práctica.
- Evaluar sobre datos que participaron en la selección del modelo.

## 🤖 Conexión con IA

Evaluar un modelo es inferencia estadística: métricas con intervalo, comparaciones múltiples corregidas y detección de leakage.

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
5. ¿Dónde aparece esto en experimentación de producto?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Wasserman, L. *All of Statistics*. Springer, 2004.
- Gelman, A. et al. *Bayesian Data Analysis*. 3ª ed., CRC, 2013.
- Efron, B.; Tibshirani, R. *An Introduction to the Bootstrap*. Chapman & Hall, 1993.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 200 Capstone: simulador probabilístico y bayesiano](../../part-09-probabilidad-y-procesos-aleatorios/200-capstone-simulador-probabilistico-y-bayesiano/README.md) · [📚 Parte 10](../README.md) · [🏠 Programa](../../../README.md) · [202 Población, muestra y sesgo de selección ➡️](../202-poblacion-muestra-y-sesgo-de-seleccion/README.md)
