# Teoría — FFT

## Definición operativa

En esta clase, **FFT** se trata como un objeto con tres capas
separadas:

| Capa | Qué es | Qué puede fallar |
|---|---|---|
| Modelo matemático | la definición ideal, con su dominio | supuestos no declarados |
| Algoritmo | el procedimiento que la calcula | complejidad y criterio de parada |
| Representación en máquina | los bits que la almacenan | redondeo, desbordamiento, cancelación |

Dos implementaciones del mismo modelo pueden diferir numéricamente sin que
ninguna esté equivocada. Reconocer en qué capa está la diferencia es parte del
contenido de esta clase.

## Ideas centrales de la parte 13

- La entropía es el límite inferior de compresión sin pérdida.
- Minimizar cross-entropy equivale a maximizar verosimilitud.
- KL no es simétrica ni es una distancia; JS sí es simétrica.
- Nyquist fija la frecuencia mínima de muestreo; por debajo hay aliasing irreversible.
- Convolución en el tiempo es multiplicación en frecuencia.

## Propiedades a estudiar

- dominio de validez y qué ocurre en su frontera;
- invariantes que la operación debe conservar;
- unidades o escala de cada cantidad;
- sensibilidad a perturbaciones pequeñas de la entrada;
- coste computacional y cómo crece con el tamaño del problema;
- relación con las clases previas de esta misma parte.

## Herramientas de referencia

Este programa implementa el procedimiento con biblioteca estándar para que
ningún paso quede oculto. En la práctica profesional se usa: math, cmath, numpy (opcional).

Usar la biblioteca no sustituye entender el procedimiento: sirve para poder
**auditar** su salida y reconocer cuándo devuelve un número correcto por la razón
equivocada.

## Verificación

El laboratorio (`fft`) devuelve 9 valores. Varios de ellos
existen únicamente para comprobar una identidad o un invariante: identifícalos y
explica qué se rompería si esa comprobación fallara.

## Aplicación

Compresión, audio, comunicaciones, análisis espectral y feature engineering temporal.
