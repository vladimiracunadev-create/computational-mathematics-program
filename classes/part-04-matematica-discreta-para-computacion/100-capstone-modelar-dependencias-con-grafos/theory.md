# Teoría — Capstone: modelar dependencias con grafos

## Definición operativa

En esta clase, **Capstone: modelar dependencias con grafos** se trata como un objeto con tres capas
separadas:

| Capa | Qué es | Qué puede fallar |
|---|---|---|
| Modelo matemático | la definición ideal, con su dominio | supuestos no declarados |
| Algoritmo | el procedimiento que la calcula | complejidad y criterio de parada |
| Representación en máquina | los bits que la almacenan | redondeo, desbordamiento, cancelación |

Dos implementaciones del mismo modelo pueden diferir numéricamente sin que
ninguna esté equivocada. Reconocer en qué capa está la diferencia es parte del
contenido de esta clase.

## Ideas centrales de la parte 04

- Una demostración por inducción es un bucle `for` con garantía.
- Permutación cuenta orden; combinación cuenta selección.
- Un DAG sin orden topológico contiene un ciclo: es un diagnóstico, no un error.
- La aritmética modular es la base de hashing, criptografía y checksums.
- El principio del palomar demuestra colisiones sin construir un ejemplo.

## Propiedades a estudiar

- dominio de validez y qué ocurre en su frontera;
- invariantes que la operación debe conservar;
- unidades o escala de cada cantidad;
- sensibilidad a perturbaciones pequeñas de la entrada;
- coste computacional y cómo crece con el tamaño del problema;
- relación con las clases previas de esta misma parte.

## Herramientas de referencia

Este programa implementa el procedimiento con biblioteca estándar para que
ningún paso quede oculto. En la práctica profesional se usa: itertools, math, collections.

Usar la biblioteca no sustituye entender el procedimiento: sirve para poder
**auditar** su salida y reconocer cuándo devuelve un número correcto por la razón
equivocada.

## Verificación

El laboratorio (`capstone_dependency_graph`) devuelve 6 valores. Varios de ellos
existen únicamente para comprobar una identidad o un invariante: identifícalos y
explica qué se rompería si esa comprobación fallara.

## Aplicación

Algoritmos, bases de datos, criptografía, compiladores y planificación de dependencias.
