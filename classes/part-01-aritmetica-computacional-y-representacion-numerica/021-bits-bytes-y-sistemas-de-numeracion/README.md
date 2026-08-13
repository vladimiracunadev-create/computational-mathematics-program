# 021 — Bits, bytes y sistemas de numeración

> [⬅️ 020 Capstone: modelar un problema cotidiano con matemáticas](../../part-00-pensamiento-matematico-desde-cero/020-capstone-modelar-un-problema-cotidiano-con-matematicas/README.md) · [📚 Parte 01](../README.md) · [🏠 Programa](../../../README.md) · [022 Conversión decimal a binario ➡️](../022-conversion-decimal-a-binario/README.md)

**Parte:** 01 — Aritmética computacional y representación numérica · **Nivel:** `basico-computacional` · **Horas estimadas:** 4
**Motor:** `engines.part01` · **Demostración:** `bits_and_bytes` · **Clase 1 de 20** de la parte

---

## 🎯 Propósito

Qué es realmente un número dentro de una máquina: bits, complemento a dos, IEEE 754, error, condicionamiento y estabilidad.

Esta clase concreta ese objetivo sobre **Bits, bytes y sistemas de numeración**: qué es, cómo se
calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica
que el resultado es correcto y no solo plausible.

## ✅ Resultados de aprendizaje

Al terminar podrás:

1. Explicar **Bits, bytes y sistemas de numeración** con lenguaje cotidiano y con notación matemática.
2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.
3. Ejecutar y modificar `lab.py`, que corre la demostración `bits_and_bytes`.
4. Interpretar las 7 salidas del laboratorio y decir qué comprueba cada una.
5. Detectar el error típico de esta parte: comparar floats con `==` en lugar de una tolerancia razonada.

## 🗺️ Ubicación en el programa

```mermaid
flowchart LR
    P["020<br/>Capstone: modelar un<br/>problema cotidiano con<br/>matemáticas"] --> C
    subgraph C["021 · Bits, bytes y sistemas de<br/>numeración"]
        direction TB
        D["Demostración<br/><code>bits_and_bytes</code>"] --> R["Resultados numéricos<br/>valores_por_bit<br/>valores_en_1_byte<br/>valores_en_16_bits<br/>… +4 más"]
        D --> V["Verificaciones<br/>—"]
        D --> O["Contexto y estructura<br/>—"]
    end
    C --> N["022<br/>Conversión decimal a<br/>binario"]
    C -.-> IA["Uso en IA<br/>parte 01"]
```

## 🧠 Idea rectora de la parte 01

> Un float es un racional binario de precisión finita, no un número real.

## 🔬 Qué ejecuta el laboratorio

`bits_and_bytes` — Cuántos valores distintos codifica cada ancho de palabra.

| Grupo | Salidas |
|---|---|
| 🔢 Resultados numéricos (7) | `valores_por_bit`, `valores_en_1_byte`, `valores_en_16_bits`, `valores_en_32_bits`, `valores_en_64_bits`, `bits_para_1000_valores`, `bits_para_1_millon` |
| ✅ Comprobaciones de invariante (0) | — |

Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico
no sería fiable aunque el programa terminase sin error.

```bash
python classes/part-01-aritmetica-computacional-y-representacion-numerica/021-bits-bytes-y-sistemas-de-numeracion/lab.py
compmath run 021
```

> [!TIP]
> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que
> esperabas enseña tanto como uno que te contradice, pero solo si la predicción
> existía antes del resultado.

## ⚠️ Errores frecuentes en esta parte

- Comparar floats con `==` en lugar de una tolerancia razonada.
- Suponer que la suma de floats es asociativa.
- Usar float para dinero en vez de Decimal o enteros de centavos.

## 🤖 Conexión con IA

float32, bfloat16 y la cuantización a int8 son decisiones de representación. Los NaN en un entrenamiento casi siempre nacen aquí, no en la arquitectura.

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
5. ¿Dónde aparece esto en motores numéricos?

Si necesitas releer el código para responderlas, la clase todavía no está superada.

## 📥 Entregable

`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar
código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.

## 🔗 Referencias

- Goldberg, D. *What Every Computer Scientist Should Know About Floating-Point Arithmetic*. ACM Computing Surveys, 1991.
- Higham, N. J. *Accuracy and Stability of Numerical Algorithms*. 2ª ed., SIAM, 2002.
- IEEE 754-2019 Standard for Floating-Point Arithmetic.

## 📂 Material de la clase

[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · [`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · [`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)

---

> [⬅️ 020 Capstone: modelar un problema cotidiano con matemáticas](../../part-00-pensamiento-matematico-desde-cero/020-capstone-modelar-un-problema-cotidiano-con-matematicas/README.md) · [📚 Parte 01](../README.md) · [🏠 Programa](../../../README.md) · [022 Conversión decimal a binario ➡️](../022-conversion-decimal-a-binario/README.md)
