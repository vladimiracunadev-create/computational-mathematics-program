# Teoría — Bits, bytes y sistemas de numeración

## Definición operativa

En esta clase, **Bits, bytes y sistemas de numeración** se trata como un objeto con tres capas
separadas:

| Capa | Qué es | Qué puede fallar |
|---|---|---|
| Modelo matemático | la definición ideal, con su dominio | supuestos no declarados |
| Algoritmo | el procedimiento que la calcula | complejidad y criterio de parada |
| Representación en máquina | los bits que la almacenan | redondeo, desbordamiento, cancelación |

Dos implementaciones del mismo modelo pueden diferir numéricamente sin que
ninguna esté equivocada. Reconocer en qué capa está la diferencia es parte del
contenido de esta clase.

## Ideas centrales de la parte 01

- Un float es un racional binario de precisión finita, no un número real.
- El error relativo, no el absoluto, es la magnitud que se propaga.
- Condicionamiento es del problema; estabilidad es del algoritmo.
- La cancelación catastrófica destruye dígitos significativos sin lanzar excepciones.
- Reproducibilidad numérica exige fijar orden de operaciones, no solo semillas.

## Propiedades a estudiar

- dominio de validez y qué ocurre en su frontera;
- invariantes que la operación debe conservar;
- unidades o escala de cada cantidad;
- sensibilidad a perturbaciones pequeñas de la entrada;
- coste computacional y cómo crece con el tamaño del problema;
- relación con las clases previas de esta misma parte.

## Herramientas de referencia

Este programa implementa el procedimiento con biblioteca estándar para que
ningún paso quede oculto. En la práctica profesional se usa: struct, decimal, fractions, sys.float_info.

Usar la biblioteca no sustituye entender el procedimiento: sirve para poder
**auditar** su salida y reconocer cuándo devuelve un número correcto por la razón
equivocada.

## Verificación

El laboratorio (`bits_and_bytes`) devuelve 7 valores. Varios de ellos
existen únicamente para comprobar una identidad o un invariante: identifícalos y
explica qué se rompería si esa comprobación fallara.

## Aplicación

Motores numéricos, finanzas, simulación científica y depuración de resultados irreproducibles.
