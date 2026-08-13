# 📖 Glosario — Parte 12: Optimización matemática y computacional

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

33 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **AdaGrad** | Paso adaptativo por coordenada usando la suma acumulada de gradientes al cuadrado. | [248](248-adagrad/README.md) |
| **Adam** | Momentum de primer y segundo orden con corrección de sesgo inicial. | [250](250-adam/README.md) |
| **AdamW** | Adam con weight decay desacoplado, aplicado al peso y no al gradiente. | [251](251-adamw/README.md) |
| **Algoritmo evolutivo** | Búsqueda por población con selección, cruce y mutación. No necesita gradiente. | [259](259-optimizacion-evolutiva/README.md) |
| **BFGS** | Cuasi-Newton que aproxima el Hessiano inverso solo con gradientes sucesivos. | [253](253-quasi-newton-y-bfgs/README.md) |
| **Búsqueda por retroceso** | Probar α, reducirlo a la mitad y repetir hasta cumplir Armijo. | [254](254-line-search/README.md) |
| **Condiciones KKT** | Estacionariedad, factibilidad, no negatividad y holgura complementaria. | [257](257-condiciones-kkt/README.md) |
| **Condición de Armijo** | Exige que el paso reduzca la función al menos una fracción de lo que predice el gradiente. | [254](254-line-search/README.md) |
| **Convexidad y óptimos** | En un problema convexo todo mínimo local es global. Fuera de él no hay garantía. | [242](242-convexidad/README.md) |
| **Corrección de sesgo** | División por 1 − βᵗ que compensa que los acumuladores empiezan en cero. | [250](250-adam/README.md) |
| **Dirección de descenso** | Cualquier d con dᵀ∇f < 0. El gradiente negativo es la más empinada localmente. | [243](243-gradiente-y-direcciones-de-descenso/README.md) |
| **Elitismo** | Conservar los mejores individuos entre generaciones para no perder el óptimo hallado. | [259](259-optimizacion-evolutiva/README.md) |
| **Función convexa** | La que queda por debajo de cualquier cuerda entre dos de sus puntos. | [242](242-convexidad/README.md) |
| **Función objetivo** | Cantidad que se minimiza o maximiza. Define qué significa mejor en el problema. | [241](241-problemas-de-optimizacion-y-funcion-objetivo/README.md) |
| **Hessiano definido positivo** | Criterio de convexidad estricta: todos los autovalores positivos. | [242](242-convexidad/README.md) |
| **Holgura complementaria** | μᵢ·gᵢ(x) = 0. Una restricción inactiva tiene multiplicador cero. | [257](257-condiciones-kkt/README.md) |
| **L-BFGS** | Variante de memoria limitada que guarda solo los últimos pares de vectores. | [253](253-quasi-newton-y-bfgs/README.md) |
| **Lagrangiano** | L = f − Σλᵢgᵢ. Convierte un problema con restricciones de igualdad en uno irrestricto. | [256](256-restricciones-y-lagrangianos/README.md) |
| **Learning rate** | Tamaño del paso. El hiperparámetro que más veces explica una divergencia. | [244](244-gradient-descent/README.md) |
| **Límite de estabilidad** | lr < 2/L con L el mayor autovalor del Hessiano. Por encima, el descenso diverge. | [244](244-gradient-descent/README.md) |
| **Mini-batch** | Lote de muestras para estimar el gradiente. Compromiso entre ruido y coste. | [245](245-stochastic-gradient-descent/README.md) |
| **Momentum** | Media móvil de los gradientes. Acelera en direcciones consistentes y amortigua la oscilación. | [246](246-momentum/README.md) |
| **Multiplicador de Lagrange** | λ. Mide cuánto mejoraría el óptimo al relajar la restricción una unidad. | [256](256-restricciones-y-lagrangianos/README.md) |
| **Método de Newton** | Usa el Hessiano para elegir dirección y paso. Converge en un paso en cuadráticas. | [252](252-metodo-de-newton/README.md) |
| **Nesterov** | Momentum que evalúa el gradiente en el punto adelantado x + βv. | [247](247-nesterov-accelerated-gradient/README.md) |
| **Presupuesto de iteraciones** | Número fijo de pasos concedido a cada método para que la comparación sea justa. | [260](260-capstone-banco-de-optimizadores-comparables/README.md) |
| **Problema irrestricto** | Aquel sin restricciones sobre las variables. El caso de casi todo entrenamiento de redes. | [241](241-problemas-de-optimizacion-y-funcion-objetivo/README.md) |
| **Programa cuadrático** | Objetivo cuadrático con restricciones lineales. Convexo si Q es definida positiva. | [258](258-optimizacion-cuadratica/README.md) |
| **Regularización L1** | Sumar λ‖w‖₁. Produce soluciones dispersas anulando coeficientes. | [255](255-regularizacion-como-optimizacion/README.md) |
| **Regularización L2** | Sumar λ‖w‖² al objetivo. Encoge todos los pesos sin anular ninguno. | [255](255-regularizacion-como-optimizacion/README.md) |
| **RMSProp** | AdaGrad con media móvil exponencial en vez de suma. Evita que el paso se apague. | [249](249-rmsprop/README.md) |
| **SGD** | Gradiente estimado sobre un subconjunto de datos. Más barato y más ruidoso. | [245](245-stochastic-gradient-descent/README.md) |
| **Variables de decisión** | Parámetros libres sobre los que se optimiza. | [241](241-problemas-de-optimizacion-y-funcion-objetivo/README.md) |

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
