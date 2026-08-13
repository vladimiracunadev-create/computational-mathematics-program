# Ejercicios — Rango, overflow y wraparound

## Básico

1. Define **Rango, overflow y wraparound** con tus palabras y da un ejemplo válido y uno inválido.
2. Resuelve un caso a mano con números pequeños y deja escrito cada paso intermedio.
3. Construye un caso límite y **predice la salida antes de ejecutar** el laboratorio.

## Intermedio

4. Ejecuta `lab.py` y explica qué comprueba cada una de sus 6 salidas.
5. Modifica un parámetro de entrada del motor y describe cómo cambia el resultado
   y por qué; contrasta con tu predicción.
6. Reimplementa el cálculo por un camino distinto y mide el error absoluto y el
   relativo entre ambas versiones. Declara la tolerancia que consideras aceptable
   y justifícala.

## Avanzado

7. Conecta esta clase con motores numéricos, finanzas, simulación científica y depuración de resultados irreproducibles mediante un caso concreto y realista.
8. Escribe un test que **falle** ante una implementación ingenua pero pase con la correcta.
9. Cambia una hipótesis del problema (dominio, escala, independencia, precisión) y
   analiza qué conclusión deja de ser válida.
10. Explica el concepto en 200 palabras a alguien que sabe programar pero no
    conoce esta parte, sin perder rigor y sin usar la palabra «simplemente».

## Reto de la parte 01

float32, bfloat16 y la cuantización a int8 son decisiones de representación. Los NaN en un entrenamiento casi siempre nacen aquí, no en la arquitectura.

Escribe qué operación concreta de un modelo de IA dejaría de funcionar si este
concepto estuviera mal implementado, y cómo se manifestaría el fallo.
