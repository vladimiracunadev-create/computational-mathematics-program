# 📖 Glosario — Parte 02: Álgebra y funciones

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

20 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Composición** | (g∘f)(x) = g(f(x)). No es conmutativa. Es la estructura de una red neuronal. | [057](057-composicion-de-funciones/README.md) |
| **Desigualdad** | Relación de orden entre expresiones. Multiplicar por un negativo invierte su sentido. | [044](044-desigualdades-lineales/README.md) |
| **Discriminante** | b² − 4ac. Su signo determina la naturaleza de las raíces antes de calcularlas. | [049](049-formula-cuadratica-y-discriminante/README.md) |
| **Dominio** | Conjunto de entradas válidas de una función. Forma parte de su definición, no es un detalle. | [052](052-funciones-dominio-y-rango/README.md) |
| **Ecuación equivalente** | Ecuación con el mismo conjunto solución. Se obtiene aplicando operaciones reversibles a ambos lados. | [043](043-ecuaciones-lineales-de-una-variable/README.md) |
| **Escala logarítmica** | Eje donde distancias iguales representan factores iguales. Convierte exponenciales en rectas. | [056](056-funciones-logaritmicas/README.md) |
| **Factorización** | Escritura de un polinomio como producto. Sus raíces se leen directamente de los factores. | [047](047-factorizacion-elemental/README.md) |
| **Función inversa** | Función que deshace a otra. Existe solo si la original es inyectiva. Distinta del recíproco 1/f. | [058](058-funciones-inversas/README.md) |
| **Función por tramos** | Función definida por reglas distintas en subconjuntos del dominio. ReLU es el caso más usado en IA. | [059](059-funciones-por-tramos/README.md) |
| **Grado de un polinomio** | Mayor exponente con coeficiente no nulo. El grado del producto es la suma de los grados. | [046](046-polinomios-y-operaciones/README.md) |
| **Imagen (rango)** | Conjunto de valores que la función realmente alcanza. | [052](052-funciones-dominio-y-rango/README.md) |
| **Logaritmo** | Exponente al que hay que elevar la base para obtener el argumento. Convierte productos en sumas. | [051](051-logaritmos-y-sus-propiedades/README.md) |
| **Pendiente** | Razón de cambio constante de una función lineal: cuánto cambia y por cada unidad de x. | [053](053-funciones-lineales-y-pendiente/README.md) |
| **Propiedad distributiva** | a(b+c) = ab + ac. Es la propiedad que conecta suma y producto y la que justifica la regla de los signos. | [042](042-propiedades-distributiva-asociativa-y-conmutativa/README.md) |
| **Regla de Horner** | Esquema de evaluación de polinomios que usa n multiplicaciones en lugar de n(n+1)/2. | [046](046-polinomios-y-operaciones/README.md) |
| **Sistema compatible determinado** | Sistema con solución única. En 2×2 equivale a determinante no nulo. | [045](045-sistemas-de-ecuaciones-2x2/README.md) |
| **Suma de residuos al cuadrado (SSE)** | Σ(observado − predicho)². Criterio para comparar modelos ajustados a los mismos datos. | [060](060-capstone-construir-y-comparar-modelos-funcionales/README.md) |
| **Tiempo de duplicación** | Tiempo que tarda una cantidad con crecimiento exponencial en duplicarse: ln 2 / ln(base). | [055](055-funciones-exponenciales/README.md) |
| **Término semejante** | Términos con la misma parte literal y los mismos exponentes. Solo ellos pueden sumarse entre sí. | [041](041-expresiones-algebraicas-y-terminos/README.md) |
| **Vértice** | Punto extremo de una parábola, situado en x = −b/2a. Es el punto medio de las raíces. | [054](054-funciones-cuadraticas-y-parabolas/README.md) |

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
