# 📖 Glosario — Parte 07: Cálculo diferencial e integral

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

18 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Antiderivada** | Función cuya derivada es la dada. Está determinada salvo una constante aditiva. | [155](155-antiderivadas/README.md) |
| **Continuidad** | f(a) existe, el límite existe y coinciden. Continua no implica derivable. | [143](143-continuidad/README.md) |
| **Criterio de la segunda derivada** | En un punto crítico, f'' > 0 indica mínimo y f'' < 0 máximo. | [152](152-maximos-y-minimos/README.md) |
| **Derivación implícita** | Derivar una relación F(x,y)=0 sin despejar y, tratando y como función de x. | [150](150-derivacion-implicita/README.md) |
| **Derivada** | Límite del cociente incremental. Es la pendiente de la mejor aproximación lineal local. | [144](144-derivada-como-tasa-de-cambio/README.md) |
| **Diferencia central** | (f(x+h) − f(x−h))/2h. Aproxima la derivada con error O(h²), un orden mejor que la diferencia adelantada. | [144](144-derivada-como-tasa-de-cambio/README.md) |
| **Indeterminación** | Forma como 0/0 o ∞/∞ que no determina el límite por sí sola; es de la expresión, no del límite. | [142](142-limites-algebraicos/README.md) |
| **Integración por partes** | ∫u dv = uv − ∫v du. Es la regla del producto leída al revés. | [158](158-integracion-por-partes/README.md) |
| **Integral definida** | Área con signo bajo la curva entre dos límites. Es aditiva y cambia de signo al invertir la orientación. | [154](154-integral-definida/README.md) |
| **Límite** | Valor al que se acerca una función cerca de un punto, exista o no la función en él. | [141](141-intuicion-de-limite/README.md) |
| **Orden de convergencia** | Exponente p tal que el error de un método cae como O(hᵖ). Trapecio es 2, Simpson es 4. | [159](159-integracion-numerica-introductoria/README.md) |
| **Punto crítico** | Punto donde la derivada se anula. Puede ser máximo, mínimo o inflexión. | [152](152-maximos-y-minimos/README.md) |
| **Regla de la cadena** | (f∘g)' = f'(g(x))·g'(x). Es el mecanismo completo de backpropagation. | [147](147-regla-de-la-cadena/README.md) |
| **Regla del producto** | (fg)' = f'g + fg'. No es el producto de las derivadas. | [146](146-regla-del-producto-y-cociente/README.md) |
| **Serie de Taylor** | Aproximación polinómica de una función alrededor de un punto, con error acotado por el término siguiente. | [151](151-aproximacion-lineal-y-taylor/README.md) |
| **Suma de Riemann** | Aproximación de una integral por rectángulos. Converge a la integral al refinar la partición. | [153](153-integral-como-acumulacion/README.md) |
| **Sustitución** | Cambio de variable en una integral. Es la regla de la cadena leída al revés. | [157](157-integracion-por-sustitucion/README.md) |
| **Teorema fundamental del cálculo** | Derivar la integral de una función devuelve la función. Derivación e integración son inversas. | [156](156-teorema-fundamental-del-calculo/README.md) |

## Cómo usar este glosario

No memorices las definiciones: **usa la columna de clase**. Un término se entiende cuando
puedes ejecutar su demostración y explicar qué comprueba, no cuando puedes recitar su
definición.

```bash
compmath show <clase>    # ficha de la clase donde vive el término
compmath run <clase>     # ejecutar su demostración
```

---

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md)
