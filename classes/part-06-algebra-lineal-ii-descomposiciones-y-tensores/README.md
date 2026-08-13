# Parte 06 — Álgebra lineal II: descomposiciones y tensores

**Nivel:** intermedio-avanzado
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part06.py`

Cambio de base, autovalores, diagonalización, LU, QR, mínimos cuadrados, SVD, pseudoinversa, PCA y álgebra tensorial.

## 🧠 Ideas centrales

- Diagonalizar es elegir la base donde la transformación solo escala.
- La SVD existe para toda matriz, incluso no cuadrada y singular.
- PCA es la SVD de los datos centrados: no hay magia estadística adicional.
- El número de condición es el cociente entre el mayor y el menor valor singular.
- Broadcasting y einsum son notación, no algoritmos nuevos.

## 🤖 Por qué importa en IA

LoRA factoriza matrices de bajo rango, la atención se define con productos tensoriales y la estabilidad del entrenamiento depende del espectro de los pesos.

## ⚠️ Errores frecuentes

- Aplicar PCA sin centrar (ni escalar) los datos.
- Interpretar autovalores complejos como error de cálculo.
- Confundir el orden de los índices al reordenar un tensor.

## 🧰 Stack de referencia

`math`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [121 — Bases y coordenadas](121-bases-y-coordenadas/README.md)
2. [122 — Cambio de base](122-cambio-de-base/README.md)
3. [123 — Transformaciones lineales](123-transformaciones-lineales/README.md)
4. [124 — Núcleo e imagen](124-nucleo-e-imagen/README.md)
5. [125 — Autovalores y autovectores](125-autovalores-y-autovectores/README.md)
6. [126 — Diagonalización](126-diagonalizacion/README.md)
7. [127 — Matrices positivas definidas](127-matrices-positivas-definidas/README.md)
8. [128 — Formas cuadráticas](128-formas-cuadraticas/README.md)
9. [129 — Descomposición LU](129-descomposicion-lu/README.md)
10. [130 — Descomposición QR](130-descomposicion-qr/README.md)
11. [131 — Mínimos cuadrados lineales](131-minimos-cuadrados-lineales/README.md)
12. [132 — SVD desde la intuición](132-svd-desde-la-intuicion/README.md)
13. [133 — SVD y compresión](133-svd-y-compresion/README.md)
14. [134 — Pseudoinversa de Moore-Penrose](134-pseudoinversa-de-moore-penrose/README.md)
15. [135 — PCA desde álgebra lineal](135-pca-desde-algebra-lineal/README.md)
16. [136 — Producto de Kronecker](136-producto-de-kronecker/README.md)
17. [137 — Tensores: índices, shape y orden](137-tensores-indices-shape-y-orden/README.md)
18. [138 — Broadcasting como operación tensorial](138-broadcasting-como-operacion-tensorial/README.md)
19. [139 — Einstein summation](139-einstein-summation/README.md)
20. [140 — Capstone: PCA y compresión de imágenes](140-capstone-pca-y-compresion-de-imagenes/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 06
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Golub, G.; Van Loan, C. *Matrix Computations*. 4ª ed., Johns Hopkins, 2013.
- Trefethen, L. N.; Bau, D. *Numerical Linear Algebra*. SIAM, 1997.
- Kolda, T.; Bader, B. *Tensor Decompositions and Applications*. SIAM Review, 2009.
