# Teoría — PCA aplicado a ML

## Definición operativa

En esta clase, **PCA aplicado a ML** se trata como un objeto con tres capas
separadas:

| Capa | Qué es | Qué puede fallar |
|---|---|---|
| Modelo matemático | la definición ideal, con su dominio | supuestos no declarados |
| Algoritmo | el procedimiento que la calcula | complejidad y criterio de parada |
| Representación en máquina | los bits que la almacenan | redondeo, desbordamiento, cancelación |

Dos implementaciones del mismo modelo pueden diferir numéricamente sin que
ninguna esté equivocada. Reconocer en qué capa está la diferencia es parte del
contenido de esta clase.

## Ideas centrales de la parte 14

- Cada algoritmo es un objetivo más un método de optimización; nada más.
- Ridge y Lasso resuelven el mismo problema con normas distintas y geometría distinta.
- El kernel trick evita construir el espacio de características explícitamente.
- El error de generalización se descompone en sesgo, varianza y ruido irreducible.
- El leakage produce métricas excelentes y modelos inútiles.

## Propiedades a estudiar

- dominio de validez y qué ocurre en su frontera;
- invariantes que la operación debe conservar;
- unidades o escala de cada cantidad;
- sensibilidad a perturbaciones pequeñas de la entrada;
- coste computacional y cómo crece con el tamaño del problema;
- relación con las clases previas de esta misma parte.

## Herramientas de referencia

Este programa implementa el procedimiento con biblioteca estándar para que
ningún paso quede oculto. En la práctica profesional se usa: math, random, numpy (opcional), scikit-learn (opcional).

Usar la biblioteca no sustituye entender el procedimiento: sirve para poder
**auditar** su salida y reconocer cuándo devuelve un número correcto por la razón
equivocada.

## Verificación

El laboratorio (`pca_ml`) devuelve 9 valores. Varios de ellos
existen únicamente para comprobar una identidad o un invariante: identifícalos y
explica qué se rompería si esa comprobación fallara.

## Aplicación

Scoring crediticio, detección de fraude, segmentación y predicción tabular.
