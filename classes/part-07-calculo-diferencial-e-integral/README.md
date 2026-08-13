# 📈 Parte 07 — Cálculo diferencial e integral

> [⬅️ Parte 06 — Álgebra lineal II: descomposiciones y tensores](../part-06-algebra-lineal-ii-descomposiciones-y-tensores/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 08 — Cálculo multivariable, matricial y autodiferenciación ➡️](../part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md)

**Nivel:** `universitario` · **Clases:** 20 · **Horas estimadas:** 80 · **Motor:** [`part07.py`](../../src/computational_math/engines/part07.py)

---

## 🎯 De qué trata esta parte

Límite, continuidad, derivada, reglas de derivación, Taylor, optimización de una variable, integral definida y teorema fundamental del cálculo.

## 🧠 Ideas centrales

- La derivada es la mejor aproximación lineal local, no solo una pendiente.
- La regla de la cadena es el mecanismo entero de backpropagation.
- Taylor cambia una función difícil por un polinomio con error acotado.
- Integrar es acumular; derivar e integrar son operaciones inversas.
- Derivada nula señala punto crítico, no necesariamente mínimo.

## 🤖 Por qué importa en IA

> [!IMPORTANT]
> Sin regla de la cadena no hay entrenamiento por gradiente; sin Taylor no hay métodos de segundo orden ni análisis de convergencia.

## ⚠️ Errores frecuentes de esta parte

- Usar diferencias finitas con h demasiado pequeño y amplificar el error de redondeo.
- Derivar en un punto donde la función no es continua.
- Confundir punto crítico con extremo global.

## 🧭 Secuencia de la parte

```mermaid
flowchart LR
    subgraph B1["Bloque 1"]
        direction TB
        L141["141 · Intuición de límite"]
        L142["142 · Límites algebraicos"]
        L143["143 · Continuidad"]
        L144["144 · Derivada como tasa de cambio"]
        L145["145 · Reglas de derivación"]
        L141 --> L142
        L142 --> L143
        L143 --> L144
        L144 --> L145
    end
    subgraph B2["Bloque 2"]
        direction TB
        L146["146 · Regla del producto y cociente"]
        L147["147 · Regla de la cadena"]
        L148["148 · Derivadas de exponenciales y…"]
        L149["149 · Derivadas trigonométricas"]
        L150["150 · Derivación implícita"]
        L146 --> L147
        L147 --> L148
        L148 --> L149
        L149 --> L150
    end
    subgraph B3["Bloque 3"]
        direction TB
        L151["151 · Aproximación lineal y Taylor"]
        L152["152 · Máximos y mínimos"]
        L153["153 · Integral como acumulación"]
        L154["154 · Integral definida"]
        L155["155 · Antiderivadas"]
        L151 --> L152
        L152 --> L153
        L153 --> L154
        L154 --> L155
    end
    subgraph B4["Bloque 4"]
        direction TB
        L156["156 · Teorema fundamental del…"]
        L157["157 · Integración por sustitución"]
        L158["158 · Integración por partes"]
        L159["159 · Integración numérica…"]
        L160["160 · Capstone: optimizar y…"]
        L156 --> L157
        L157 --> L158
        L158 --> L159
        L159 --> L160
    end
    L145 --> L146
    L150 --> L151
    L155 --> L156
```

## 📚 Las clases

| # | Clase | Demostración | Idea central |
|---|---|---|---|
| `141` | [Intuición de límite](141-intuicion-de-limite/README.md) | `limit_intuition` | sin(x)/x cuando x→0: indeterminado en el punto, definido en el límite. |
| `142` | [Límites algebraicos](142-limites-algebraicos/README.md) | `algebraic_limits` | Indeterminación 0/0 resuelta por factorización. |
| `143` | [Continuidad](143-continuidad/README.md) | `continuity` | Los tres requisitos de continuidad en un punto. |
| `144` | [Derivada como tasa de cambio](144-derivada-como-tasa-de-cambio/README.md) | `derivative_as_rate` | Derivada como límite del cociente incremental. |
| `145` | [Reglas de derivación](145-reglas-de-derivacion/README.md) | `derivative_rules` | Reglas de potencia, suma y constante verificadas numéricamente. |
| `146` | [Regla del producto y cociente](146-regla-del-producto-y-cociente/README.md) | `product_quotient_rule` | Regla del producto y del cociente. |
| `147` | [Regla de la cadena](147-regla-de-la-cadena/README.md) | `chain_rule` | La regla de la cadena: el mecanismo entero de backpropagation. |
| `148` | [Derivadas de exponenciales y logaritmos](148-derivadas-de-exponenciales-y-logaritmos/README.md) | `exp_log_derivatives` | e^x es su propia derivada; log tiene derivada 1/x. |
| `149` | [Derivadas trigonométricas](149-derivadas-trigonometricas/README.md) | `trig_derivatives` | Derivadas trigonométricas y su ciclo de periodo 4. |
| `150` | [Derivación implícita](150-derivacion-implicita/README.md) | `implicit_differentiation` | Derivación implícita sobre la circunferencia x²+y²=25. |
| `151` | [Aproximación lineal y Taylor](151-aproximacion-lineal-y-taylor/README.md) | `taylor_approximation` | Taylor de e^x en 0: el error cae con el grado. |
| `152` | [Máximos y mínimos](152-maximos-y-minimos/README.md) | `extrema` | Máximos y mínimos por derivada y criterio de la segunda derivada. |
| `153` | [Integral como acumulación](153-integral-como-acumulacion/README.md) | `integral_as_accumulation` | Sumas de Riemann convergiendo a la integral. |
| `154` | [Integral definida](154-integral-definida/README.md) | `definite_integral` | Propiedades de la integral definida. |
| `155` | [Antiderivadas](155-antiderivadas/README.md) | `antiderivatives` | La antiderivada no es única: difiere en una constante. |
| `156` | [Teorema fundamental del cálculo](156-teorema-fundamental-del-calculo/README.md) | `fundamental_theorem` | Teorema fundamental: derivar deshace integrar. |
| `157` | [Integración por sustitución](157-integracion-por-sustitucion/README.md) | `substitution` | Integración por sustitución: la regla de la cadena al revés. |
| `158` | [Integración por partes](158-integracion-por-partes/README.md) | `integration_by_parts` | Integración por partes: la regla del producto al revés. |
| `159` | [Integración numérica introductoria](159-integracion-numerica-introductoria/README.md) | `numerical_integration_intro` | Trapecio frente a Simpson sobre la misma integral. |
| `160` | [Capstone: optimizar y acumular una señal](160-capstone-optimizar-y-acumular-una-senal/README.md) | `capstone_optimize_and_accumulate` | Capstone: derivar para optimizar e integrar para acumular una señal. |

## 🧰 Stack de referencia

`math`, `sympy (opcional)`, `scipy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen
como contraste profesional, no como requisito.

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 07
compmath catalog --part 07
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone ([160](160-capstone-optimizar-y-acumular-una-senal/README.md)) | 20 % |

## 📖 Bibliografía

- Spivak, M. *Calculus*. 4ª ed., Publish or Perish, 2008.
- Apostol, T. *Calculus, Vol. 1*. 2ª ed., Wiley, 1967.
- Strang, G. *Calculus*. 3ª ed., Wellesley-Cambridge, 2017.

---

> [⬅️ Parte 06 — Álgebra lineal II: descomposiciones y tensores](../part-06-algebra-lineal-ii-descomposiciones-y-tensores/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 08 — Cálculo multivariable, matricial y autodiferenciación ➡️](../part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md)
