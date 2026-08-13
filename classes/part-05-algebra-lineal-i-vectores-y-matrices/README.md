# Parte 05 — Álgebra lineal I: vectores y matrices

**Nivel:** intermedio
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part05.py`

Vectores, normas, producto punto, independencia, span, sistemas lineales, eliminación de Gauss, rango, inversa, determinante y proyección ortogonal.

## 🧠 Ideas centrales

- Una matriz es una función lineal escrita en una base concreta.
- El rango es la dimensión real de la salida, no el tamaño de la tabla.
- Resolver Ax=b casi nunca requiere calcular A⁻¹.
- La proyección ortogonal es la mejor aproximación en norma euclídea.
- El determinante mide cuánto escala el volumen una transformación.

## 🤖 Por qué importa en IA

Cada capa densa es un producto matriz-vector. Los embeddings viven en subespacios y la similitud entre ellos es producto punto normalizado.

## ⚠️ Errores frecuentes

- Invertir una matriz mal condicionada en lugar de factorizar.
- Confundir dimensión del espacio con número de vectores.
- Aplicar producto punto a vectores de escalas incomparables.

## 🧰 Stack de referencia

`math`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [101 — Escalares, vectores y matrices](101-escalares-vectores-y-matrices/README.md)
2. [102 — Operaciones con vectores](102-operaciones-con-vectores/README.md)
3. [103 — Producto punto y similitud](103-producto-punto-y-similitud/README.md)
4. [104 — Normas y distancias](104-normas-y-distancias/README.md)
5. [105 — Vectores unitarios](105-vectores-unitarios/README.md)
6. [106 — Combinaciones lineales](106-combinaciones-lineales/README.md)
7. [107 — Independencia y dependencia lineal](107-independencia-y-dependencia-lineal/README.md)
8. [108 — Span y subespacios](108-span-y-subespacios/README.md)
9. [109 — Matrices y operaciones básicas](109-matrices-y-operaciones-basicas/README.md)
10. [110 — Producto matriz-vector](110-producto-matriz-vector/README.md)
11. [111 — Producto de matrices](111-producto-de-matrices/README.md)
12. [112 — Transpuesta y simetría](112-transpuesta-y-simetria/README.md)
13. [113 — Sistemas lineales](113-sistemas-lineales/README.md)
14. [114 — Eliminación de Gauss](114-eliminacion-de-gauss/README.md)
15. [115 — Forma escalonada y rango](115-forma-escalonada-y-rango/README.md)
16. [116 — Inversa de una matriz](116-inversa-de-una-matriz/README.md)
17. [117 — Determinantes](117-determinantes/README.md)
18. [118 — Matrices ortogonales](118-matrices-ortogonales/README.md)
19. [119 — Proyecciones ortogonales](119-proyecciones-ortogonales/README.md)
20. [120 — Capstone: resolver un sistema de recomendación lineal](120-capstone-resolver-un-sistema-de-recomendacion-lineal/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 05
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Strang, G. *Introduction to Linear Algebra*. 6ª ed., Wellesley-Cambridge, 2023.
- Axler, S. *Linear Algebra Done Right*. 4ª ed., Springer, 2024.
- Trefethen, L. N.; Bau, D. *Numerical Linear Algebra*. SIAM, 1997.
