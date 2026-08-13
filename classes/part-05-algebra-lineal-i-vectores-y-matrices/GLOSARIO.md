# 📖 Glosario — Parte 05: Álgebra lineal I: vectores y matrices

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

19 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Combinación lineal** | Suma de vectores multiplicados por escalares. Es la operación que define todo el álgebra lineal. | [106](106-combinaciones-lineales/README.md) |
| **Desigualdad triangular** | ‖u+v‖ ≤ ‖u‖ + ‖v‖. Es una de las tres condiciones que definen una norma. | [102](102-operaciones-con-vectores/README.md) |
| **Determinante** | Factor por el que la transformación escala el volumen. Cero significa que aplasta el espacio. | [117](117-determinantes/README.md) |
| **Escalar, vector, matriz, tensor** | Tensores de orden 0, 1, 2 y n. El orden es el número de índices necesarios para localizar un elemento. | [101](101-escalares-vectores-y-matrices/README.md) |
| **Espacio columna** | Span de las columnas de A. Es donde vive Ax; el sistema Ax = b tiene solución si y solo si b está en él. | [110](110-producto-matriz-vector/README.md) |
| **Independencia lineal** | Ningún vector del conjunto es combinación de los demás. Se detecta por el rango, no por inspección. | [107](107-independencia-y-dependencia-lineal/README.md) |
| **Matriz ortogonal** | QᵀQ = I. Preserva normas y ángulos, y su número de condición es 1: no amplifica el error. | [118](118-matrices-ortogonales/README.md) |
| **Matriz singular** | Matriz sin inversa; su determinante es cero y su rango es deficiente. | [116](116-inversa-de-una-matriz/README.md) |
| **Norma** | Medida de magnitud de un vector. L2 es la euclídea; L1 induce dispersión; L∞ mira el máximo. | [104](104-normas-y-distancias/README.md) |
| **Pivoteo parcial** | Intercambio de filas para usar el mayor pivote disponible. Evita dividir por valores casi nulos. | [114](114-eliminacion-de-gauss/README.md) |
| **Producto matricial** | Composición de transformaciones lineales. Asociativo pero no conmutativo. Coste O(n³) ingenuo. | [111](111-producto-de-matrices/README.md) |
| **Producto punto** | Σuᵢvᵢ. Mide alineación; es cero si y solo si los vectores son ortogonales. | [103](103-producto-punto-y-similitud/README.md) |
| **Proyección ortogonal** | Mejor aproximación de un vector dentro de un subespacio, en norma euclídea. Su residuo es ortogonal al subespacio. | [119](119-proyecciones-ortogonales/README.md) |
| **Rango** | Dimensión del espacio columna. Es la dimensión efectiva de la salida de la transformación. | [115](115-forma-escalonada-y-rango/README.md) |
| **Span** | Conjunto de todas las combinaciones lineales de unos vectores. Es siempre un subespacio. | [108](108-span-y-subespacios/README.md) |
| **Subespacio** | Subconjunto cerrado bajo suma y producto por escalar. Contiene siempre al vector cero. | [108](108-span-y-subespacios/README.md) |
| **Teorema del rango-nulidad** | rango + nulidad = número de columnas. Lo que no llega a la imagen se pierde en el núcleo. | [115](115-forma-escalonada-y-rango/README.md) |
| **Transpuesta** | Intercambio de filas y columnas. (AB)ᵀ = BᵀAᵀ, con el orden invertido. | [112](112-transpuesta-y-simetria/README.md) |
| **Vector unitario** | Vector de norma 1. Normalizar separa dirección de magnitud. | [105](105-vectores-unitarios/README.md) |

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
