# 📖 Glosario — Parte 11: Métodos numéricos y computación científica

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

32 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Bisección** | Partir por la mitad un intervalo con cambio de signo. Lenta pero convergencia garantizada. | [222](222-biseccion/README.md) |
| **Condición de Courant** | Restricción entre paso temporal y espacial. Violarla hace divergir el esquema explícito. | [238](238-introduccion-a-pde-y-discretizacion/README.md) |
| **Convergencia cuadrática** | El número de dígitos correctos se duplica en cada iteración. | [223](223-newton-raphson/README.md) |
| **Cuadratura** | Aproximación de una integral por suma ponderada de valores de la función. | [228](228-cuadratura-numerica/README.md) |
| **Cuadratura gaussiana** | Nodos y pesos elegidos para ser exactos con polinomios de grado 2n−1. | [228](228-cuadratura-numerica/README.md) |
| **Diagonalmente dominante** | Cada elemento diagonal supera en módulo a la suma de su fila. Garantiza convergencia iterativa. | [232](232-jacobi-y-gauss-seidel/README.md) |
| **Diferencia central** | (f(x+h) − f(x−h)) / 2h. Error O(h²) frente al O(h) de la diferencia adelantada. | [227](227-diferenciacion-numerica/README.md) |
| **Diferencias finitas** | Sustituir derivadas por cocientes sobre una malla para discretizar una PDE. | [238](238-introduccion-a-pde-y-discretizacion/README.md) |
| **Ecuaciones normales** | AᵀAx = Aᵀb. Resuelven mínimos cuadrados pero elevan al cuadrado el número de condición. | [234](234-minimos-cuadrados-numericos/README.md) |
| **Error de redondeo** | El que introduce la aritmética finita. Aumenta al reducir h por cancelación. | [221](221-errores-numericos-y-convergencia/README.md) |
| **Error de truncamiento** | El que introduce el método al aproximar. Disminuye al reducir el paso h. | [221](221-errores-numericos-y-convergencia/README.md) |
| **Fenómeno de Runge** | Oscilaciones crecientes al interpolar con grado alto en nodos equiespaciados. | [225](225-interpolacion-de-lagrange/README.md) |
| **Gauss-Seidel** | Como Jacobi pero reutilizando los valores ya actualizados. Suele converger el doble de rápido. | [232](232-jacobi-y-gauss-seidel/README.md) |
| **Interpolación de Lagrange** | Polinomio único de grado n−1 que pasa por n puntos dados. | [225](225-interpolacion-de-lagrange/README.md) |
| **Método de Euler** | Avanzar por la tangente. Orden 1 y una sola evaluación por paso. | [236](236-metodo-de-euler/README.md) |
| **Método de la secante** | Newton con la derivada aproximada por diferencias. Orden 1,618. | [224](224-metodo-de-la-secante/README.md) |
| **Método directo** | Resuelve en un número fijo de operaciones, como LU. Coste O(n³). | [231](231-sistemas-lineales-directos/README.md) |
| **Newton-Raphson** | Iteración x − f(x)/f'(x). Convergencia cuadrática cerca de la raíz. | [223](223-newton-raphson/README.md) |
| **Nodos de Chebyshev** | Nodos concentrados en los extremos que controlan el error de interpolación. | [225](225-interpolacion-de-lagrange/README.md) |
| **Orden de convergencia** | Exponente p tal que el error se comporta como O(hᵖ). Predice la ganancia al refinar. | [221](221-errores-numericos-y-convergencia/README.md) |
| **Paso óptimo** | Valor de h que minimiza el error total. Por debajo, afinar empeora el resultado. | [221](221-errores-numericos-y-convergencia/README.md) |
| **Pivoteo parcial** | Intercambiar filas para usar el pivote de mayor módulo y ganar estabilidad. | [231](231-sistemas-lineales-directos/README.md) |
| **Problema de valor inicial** | EDO más condición inicial. Determina una única trayectoria. | [235](235-ecuaciones-diferenciales-ordinarias/README.md) |
| **Problema rígido** | El que tiene escalas de tiempo muy dispares. Exige métodos implícitos. | [237](237-runge-kutta/README.md) |
| **Región de estabilidad** | Valores del paso para los que el método no amplifica el error. Independiente de la precisión. | [236](236-metodo-de-euler/README.md) |
| **Regla de Simpson** | Aproxima por parábolas. Error O(h⁴) y exacta hasta grado 3. | [230](230-simpson/README.md) |
| **Regla del trapecio** | Aproxima por trapecios. Error O(h²): duplicar n divide el error por 4. | [229](229-regla-del-trapecio/README.md) |
| **Residuo** | ‖Ax − b‖. Mide cuánto incumple la ecuación la solución aproximada. | [233](233-metodos-iterativos-y-tolerancias/README.md) |
| **Runge-Kutta 4** | Cuatro evaluaciones por paso y error O(h⁴). Estándar de facto para EDO no rígidas. | [237](237-runge-kutta/README.md) |
| **Spline** | Interpolación por tramos de grado bajo. Evita las oscilaciones del grado alto. | [226](226-splines/README.md) |
| **Teorema de Bolzano** | Si f es continua y cambia de signo en un intervalo, hay una raíz dentro. | [222](222-biseccion/README.md) |
| **Tolerancia relativa** | Criterio de parada escalado por la magnitud de la solución. Robusto ante cambios de escala. | [233](233-metodos-iterativos-y-tolerancias/README.md) |

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
