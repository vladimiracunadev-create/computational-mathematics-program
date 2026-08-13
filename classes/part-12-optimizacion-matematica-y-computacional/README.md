# Parte 12 — Optimización matemática y computacional

**Nivel:** avanzado
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part12.py`

Función objetivo, convexidad, descenso de gradiente y su familia completa de optimizadores, métodos de segundo orden, restricciones, KKT y optimización evolutiva.

## 🧠 Ideas centrales

- En un problema convexo todo mínimo local es global; fuera de él no hay garantía.
- El learning rate es el hiperparámetro que más veces explica una divergencia.
- Momentum promedia gradientes; Adam además normaliza por su escala.
- Regularizar es añadir un término al objetivo, no un truco de implementación.
- KKT generaliza Lagrange a restricciones de desigualdad.

## 🤖 Por qué importa en IA

AdamW es el optimizador por defecto del entrenamiento moderno; entender su actualización explica el weight decay, el warmup y el gradient clipping.

## ⚠️ Errores frecuentes

- Comparar optimizadores sin fijar semilla ni presupuesto de iteraciones.
- Aplicar weight decay dentro del gradiente en Adam (y no como AdamW).
- Declarar convergencia por número de épocas y no por criterio numérico.

## 🧰 Stack de referencia

`math`, `numpy (opcional)`, `cvxpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [241 — Problemas de optimización y función objetivo](241-problemas-de-optimizacion-y-funcion-objetivo/README.md)
2. [242 — Convexidad](242-convexidad/README.md)
3. [243 — Gradiente y direcciones de descenso](243-gradiente-y-direcciones-de-descenso/README.md)
4. [244 — Gradient descent](244-gradient-descent/README.md)
5. [245 — Stochastic gradient descent](245-stochastic-gradient-descent/README.md)
6. [246 — Momentum](246-momentum/README.md)
7. [247 — Nesterov accelerated gradient](247-nesterov-accelerated-gradient/README.md)
8. [248 — AdaGrad](248-adagrad/README.md)
9. [249 — RMSProp](249-rmsprop/README.md)
10. [250 — Adam](250-adam/README.md)
11. [251 — AdamW](251-adamw/README.md)
12. [252 — Método de Newton](252-metodo-de-newton/README.md)
13. [253 — Quasi-Newton y BFGS](253-quasi-newton-y-bfgs/README.md)
14. [254 — Line search](254-line-search/README.md)
15. [255 — Regularización como optimización](255-regularizacion-como-optimizacion/README.md)
16. [256 — Restricciones y Lagrangianos](256-restricciones-y-lagrangianos/README.md)
17. [257 — Condiciones KKT](257-condiciones-kkt/README.md)
18. [258 — Optimización cuadrática](258-optimizacion-cuadratica/README.md)
19. [259 — Optimización evolutiva](259-optimizacion-evolutiva/README.md)
20. [260 — Capstone: banco de optimizadores comparables](260-capstone-banco-de-optimizadores-comparables/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 12
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Boyd, S.; Vandenberghe, L. *Convex Optimization*. Cambridge, 2004.
- Nocedal, J.; Wright, S. *Numerical Optimization*. 2ª ed., Springer, 2006.
- Loshchilov, I.; Hutter, F. *Decoupled Weight Decay Regularization*. ICLR, 2019.
