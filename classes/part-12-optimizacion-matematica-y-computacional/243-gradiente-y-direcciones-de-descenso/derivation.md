# Derivación y razonamiento — Gradiente y direcciones de descenso

## Método

1. **Declara símbolos y supuestos.** Toda letra necesita significado, unidad y dominio.
2. **Parte de una relación conocida** —definición, identidad previa o algoritmo base.
3. **Transforma un paso por línea.** Ningún paso debe requerir «se ve fácilmente».
4. **Justifica cada transformación** nombrando la propiedad que la autoriza.
5. **Verifica dimensiones, signos y casos límite** antes de aceptar el resultado.
6. **Contrasta con un cálculo numérico pequeño** que puedas comprobar a mano.

## Ejercicio de derivación

Construye una derivación de 5 a 10 pasos relacionada con **Gradiente y direcciones de descenso**.
Si el tema no admite una fórmula cerrada, deriva en su lugar:

- el **algoritmo** (por qué cada paso acerca a la solución), o
- la **regla de decisión** (qué garantiza la elección que hace), o
- la **cota de error** (por qué el resultado está a cierta distancia del valor exacto).

## Contraste con el laboratorio

La demostración `descent_directions` recorre este mismo razonamiento en código.
Después de derivarlo a mano, lee la implementación en
`src/computational_math/engines/part12.py` y responde:

- ¿Qué línea del código corresponde a cada paso de tu derivación?
- ¿Hay algún paso que el código resuelve de forma distinta a la tuya?
- ¿Alguna decisión del código (tolerancia, orden de operaciones, semilla) no
  aparece en la matemática pura? ¿Por qué está ahí?

## Trampa habitual de esta parte

Comparar optimizadores sin fijar semilla ni presupuesto de iteraciones.

Una derivación correcta que ignora esta trampa produce código incorrecto.
