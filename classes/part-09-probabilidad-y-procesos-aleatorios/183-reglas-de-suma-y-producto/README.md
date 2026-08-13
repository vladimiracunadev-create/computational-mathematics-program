# 183 — Reglas de suma y producto

> [⬅️ 182 Axiomas de probabilidad](../182-axiomas-de-probabilidad/README.md) · [📚 Parte 09](../README.md) · [🏠 Programa](../../../README.md) · [184 Probabilidad condicional ➡️](../184-probabilidad-condicional/README.md)

**Parte:** 09 — Probabilidad y procesos aleatorios · **Nivel:** `universitario` · **Horas estimadas:** 4
**Motor:** `engines.part09` · **Demostración:** `sum_product_rules` · **Clase 3 de 20** de la parte

---

## 🎯 Propósito

**La regla de la suma resta la intersección; olvidarla infla la probabilidad.**

Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Reglas de suma y producto** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `sum_product_rules`.
4. Interpretar las 8 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: reportar resultados monte carlo sin semilla ni intervalo.

## 🧩 Fórmulas de la clase

```text
P(A∪B) = P(A) + P(B) − P(A∩B)
si A y B son disjuntos: P(A∪B) = P(A) + P(B)
P(A∩B) = P(A)·P(B|A)   (regla del producto)
```

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["Clase 182 · Axiomas de probabilidad"] --> D
    subgraph CLASE["Clase 183 · Reglas de suma y producto"]
        direction TB
        D["Demostracion sum_product_rules"]
        D --> R["Resultados 6: PA_primer_dado_1 +5"]
        D --> V["Comprobaciones 2: son_mutuamente_excluy… +1"]
        D --> O["Contexto: ninguna"]
    end
    R --> N["Clase 184 · Probabilidad condicional"]
    V -.-> IA["Aplicacion en IA · parte 09"]
```

## 📖 Fundamentos

La **regla de la suma** general es inclusión-exclusión, la misma idea que apareció en
combinatoria en la parte 04: al sumar `P(A)` y `P(B)` se cuentan dos veces los resultados
que están en ambos, y hay que restarlos una vez. El caso simple —sumar sin más— solo vale
cuando los eventos son **mutuamente excluyentes**, es decir, cuando su intersección es
vacía.

La distinción importa porque el error es silencioso. Si dos eventos se solapan poco, la
suma sin corregir da un número plausible pero equivocado, y nada avisa. Solo cuando el
solapamiento es grande la suma supera 1 y el fallo se hace visible. La costumbre correcta
es preguntarse siempre si los eventos pueden ocurrir a la vez.

La **regla del producto** es la definición de probabilidad condicional despejada:
`P(A∩B) = P(A)·P(B|A)`. Se lee como una secuencia: primero ocurre A, y después B dado que
A ocurrió. Encadenada, produce la **regla de la cadena** probabilística
`P(A₁∩…∩Aₙ) = P(A₁)·P(A₂|A₁)·…·P(Aₙ|A₁…Aₙ₋₁)`, que es exactamente cómo un modelo de
lenguaje autorregresivo factoriza la probabilidad de una frase.

Solo cuando hay independencia el producto se simplifica a `P(A)·P(B)`. Ese atajo es tan
cómodo que se aplica por inercia, y la clase 185 insiste en que la independencia es una
propiedad que se verifica, no una comodidad que se asume.

## 🧮 Ejemplo trabajado

Dos dados: A = "el primero es 1", B = "la suma es 7".

```text
P(A) = 6/36  = 0,1667
P(B) = 6/36  = 0,1667

A∩B = {(1,6)}          P(A∩B) = 1/36 = 0,0278

inclusión-exclusión:
  P(A∪B) = 0,1667 + 0,1667 − 0,0278 = 0,3056

conteo directo: |A∪B| = 11 pares    11/36 = 0,3056      ✓

sumar sin restar daría 0,3333: un 9 % de más, sin ningún aviso.
```

## 🔬 Qué ejecuta el laboratorio

`sum_product_rules` — Regla de la suma con y sin exclusión mutua.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (6) | `P(A)_primer_dado_1`, `P(B)_suma_7`, `P(A∩B)`, `P(A∪B)_inclusion_exclusion`, `P(A∪B)_directo`, `P(A)·P(B)` |
| ✅ Comprobaciones de invariante (2) | `son_mutuamente_excluyentes`, `son_independientes` |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-09-probabilidad-y-procesos-aleatorios/183-reglas-de-suma-y-producto/lab.py
compmath run 183
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores conceptuales frecuentes

1. Sumar probabilidades de eventos que se solapan.
2. Llamar «excluyentes» a eventos que solo son poco probables a la vez.
3. Usar P(A)·P(B) sin haber comprobado la independencia.

## 🚀 Dónde se usa de verdad

Cálculo de tasas de fallo en sistemas redundantes, unión de condiciones en filtros de
datos y factorización autorregresiva de secuencias.

## 🤖 Conexión con IA

Un modelo de lenguaje es una distribución condicional sobre el siguiente token; la difusión es un proceso estocástico con reverso aprendido.

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
5. ¿Dónde aparece esto en riesgo?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- [Blitzstein, J.; Hwang, J. *Introduction to Probability*, 2ª ed., CRC, 2019, cap. 2](https://projects.iq.harvard.edu/stat110/home)
- [Ross, S. *A First Course in Probability*, 10ª ed., Pearson, 2018, cap. 3](https://www.pearson.com/)

Bibliografía completa de la parte en [`../../../docs/BIBLIOGRAPHY.md`](../../../docs/BIBLIOGRAPHY.md).

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 182 Axiomas de probabilidad](../182-axiomas-de-probabilidad/README.md) · [📚 Parte 09](../README.md) · [🏠 Programa](../../../README.md) · [184 Probabilidad condicional ➡️](../184-probabilidad-condicional/README.md)
