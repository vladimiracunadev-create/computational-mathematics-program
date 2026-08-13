# Parte 11 — Métodos numéricos y computación científica

**Nivel:** cientifico
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part11.py`

Raíces, interpolación, splines, diferenciación y cuadratura numérica, sistemas lineales iterativos, mínimos cuadrados y ecuaciones diferenciales.

## 🧠 Ideas centrales

- Todo método iterativo necesita criterio de parada y tolerancia declarada.
- Newton converge cuadráticamente, pero solo cerca de la raíz.
- Interpolar de grado alto oscila (fenómeno de Runge): por eso existen los splines.
- El orden de un método de integración predice cómo cae el error con el paso.
- Un solver sin estimación de error es un generador de números plausibles.

## 🤖 Por qué importa en IA

Los Neural ODE, los samplers de difusión y los optimizadores de segundo orden son métodos numéricos con parámetros aprendidos.

## ⚠️ Errores frecuentes

- Usar tolerancia absoluta cuando la escala del problema es grande.
- Iterar sin límite máximo y colgar el proceso.
- Aplicar Runge-Kutta con paso fijo a un sistema rígido.

## 🧰 Stack de referencia

`math`, `numpy (opcional)`, `scipy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [221 — Errores numéricos y convergencia](221-errores-numericos-y-convergencia/README.md)
2. [222 — Bisección](222-biseccion/README.md)
3. [223 — Newton-Raphson](223-newton-raphson/README.md)
4. [224 — Método de la secante](224-metodo-de-la-secante/README.md)
5. [225 — Interpolación de Lagrange](225-interpolacion-de-lagrange/README.md)
6. [226 — Splines](226-splines/README.md)
7. [227 — Diferenciación numérica](227-diferenciacion-numerica/README.md)
8. [228 — Cuadratura numérica](228-cuadratura-numerica/README.md)
9. [229 — Regla del trapecio](229-regla-del-trapecio/README.md)
10. [230 — Simpson](230-simpson/README.md)
11. [231 — Sistemas lineales directos](231-sistemas-lineales-directos/README.md)
12. [232 — Jacobi y Gauss-Seidel](232-jacobi-y-gauss-seidel/README.md)
13. [233 — Métodos iterativos y tolerancias](233-metodos-iterativos-y-tolerancias/README.md)
14. [234 — Mínimos cuadrados numéricos](234-minimos-cuadrados-numericos/README.md)
15. [235 — Ecuaciones diferenciales ordinarias](235-ecuaciones-diferenciales-ordinarias/README.md)
16. [236 — Método de Euler](236-metodo-de-euler/README.md)
17. [237 — Runge-Kutta](237-runge-kutta/README.md)
18. [238 — Introducción a PDE y discretización](238-introduccion-a-pde-y-discretizacion/README.md)
19. [239 — Computación científica con SciPy](239-computacion-cientifica-con-scipy/README.md)
20. [240 — Capstone: solver numérico con informe de error](240-capstone-solver-numerico-con-informe-de-error/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 11
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Burden, R.; Faires, J. *Numerical Analysis*. 10ª ed., Cengage, 2015.
- Press, W. et al. *Numerical Recipes*. 3ª ed., Cambridge, 2007.
- Heath, M. *Scientific Computing: An Introductory Survey*. 2ª ed., SIAM, 2018.
