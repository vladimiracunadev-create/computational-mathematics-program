# 📖 Glosario — Parte 06: Álgebra lineal II: descomposiciones y tensores

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

20 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Autovalor** | Factor λ por el que la transformación escala su autovector: Av = λv. | [125](125-autovalores-y-autovectores/README.md) |
| **Base** | Conjunto independiente que genera todo el espacio. Las coordenadas de un vector dependen de la base elegida. | [121](121-bases-y-coordenadas/README.md) |
| **Broadcasting** | Regla que alinea shapes por la derecha y estira las dimensiones de tamaño 1 sin copiar memoria. | [138](138-broadcasting-como-operacion-tensorial/README.md) |
| **Cambio de base** | Transformación A' = P⁻¹AP que expresa la misma aplicación lineal en otra base. | [122](122-cambio-de-base/README.md) |
| **Definida positiva** | Matriz simétrica con todos los autovalores positivos; equivale a xᵀAx > 0 para todo x no nulo. | [127](127-matrices-positivas-definidas/README.md) |
| **Factorización LU** | A = LU con L triangular inferior y U superior. Factoriza una vez, resuelve muchos sistemas. | [129](129-descomposicion-lu/README.md) |
| **Factorización QR** | A = QR con Q ortogonal y R triangular superior. Numéricamente más estable que las ecuaciones normales. | [130](130-descomposicion-qr/README.md) |
| **Forma cuadrática** | q(x) = xᵀAx. Sus curvas de nivel son elipses si A es definida positiva. | [128](128-formas-cuadraticas/README.md) |
| **Matrices semejantes** | A y P⁻¹AP. Representan la misma transformación y comparten traza, determinante y autovalores. | [122](122-cambio-de-base/README.md) |
| **Mínimos cuadrados** | Solución que minimiza ‖Ax − b‖². Es la proyección de b sobre el espacio columna de A. | [131](131-minimos-cuadrados-lineales/README.md) |
| **Notación de Einstein** | Convenio en el que los índices repetidos se suman. Unifica producto, traza, contracción y transposición. | [139](139-einstein-summation/README.md) |
| **Núcleo** | Conjunto de vectores que la transformación manda al cero. Su dimensión es la nulidad. | [124](124-nucleo-e-imagen/README.md) |
| **Orden de un tensor** | Número de índices necesarios para localizar un elemento. Un lote de imágenes es de orden 4. | [137](137-tensores-indices-shape-y-orden/README.md) |
| **PCA** | Proyección sobre los autovectores de la covarianza. Es la SVD de los datos centrados. | [135](135-pca-desde-algebra-lineal/README.md) |
| **Producto de Kronecker** | A⊗B, matriz en bloques cuyo rango es el producto de los rangos. | [136](136-producto-de-kronecker/README.md) |
| **Pseudoinversa** | A⁺, generalización de la inversa a matrices rectangulares o singulares. Da la solución de mínima norma. | [134](134-pseudoinversa-de-moore-penrose/README.md) |
| **SVD** | A = UΣVᵀ. Existe para toda matriz. De ella se leen rango, condición y mejor aproximación de rango bajo. | [132](132-svd-desde-la-intuicion/README.md) |
| **Teorema de Eckart-Young** | La SVD truncada a rango k es la mejor aproximación de rango k en norma de Frobenius y espectral. | [133](133-svd-y-compresion/README.md) |
| **Teorema espectral** | Toda matriz simétrica real es diagonalizable con autovectores ortonormales y autovalores reales. | [126](126-diagonalizacion/README.md) |
| **Valor singular** | Raíz cuadrada de los autovalores de AᵀA. Miden cuánto estira A en cada dirección principal. | [132](132-svd-desde-la-intuicion/README.md) |

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
