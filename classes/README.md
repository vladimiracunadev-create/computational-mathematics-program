# Catálogo de clases

**360 clases** en **18 partes** ·
1080 notebooks · 1440 horas estimadas.

Cada clase contiene 12 archivos y ejecuta una demostración
real del motor de su parte. Este índice es un **artefacto generado**: se reconstruye con
`python scripts/generate_classes.py`.

```bash
compmath catalog            # el mismo listado desde la terminal
compmath show <clase>       # ficha de una clase
compmath run <clase>        # ejecutar su laboratorio
```

### Parte 00 — [Pensamiento matemático desde cero](part-00-pensamiento-matematico-desde-cero/README.md)

*Reconstruye la aritmética y el lenguaje matemático básico con el rigor que exige escribir código: cada número tiene dominio, unidad y representación.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [001](part-00-pensamiento-matematico-desde-cero/001-numeros-naturales-y-conteo/README.md) | Números naturales y conteo | `counting` | Conteo, suma de Gauss y verificación cerrada frente a iterativa. |
| [002](part-00-pensamiento-matematico-desde-cero/002-enteros-signo-y-recta-numerica/README.md) | Enteros, signo y recta numérica | `integers_number_line` | Signo, valor absoluto y distancia en la recta numérica. |
| [003](part-00-pensamiento-matematico-desde-cero/003-fracciones-y-numeros-racionales/README.md) | Fracciones y números racionales | `rational_arithmetic` | Un tercio exacto frente a un tercio en punto flotante. |
| [004](part-00-pensamiento-matematico-desde-cero/004-decimales-y-conversiones/README.md) | Decimales y conversiones | `decimal_conversion` | Fracciones con desarrollo decimal finito y periódico. |
| [005](part-00-pensamiento-matematico-desde-cero/005-porcentajes-desde-cero/README.md) | Porcentajes desde cero | `percentage` | Aumento y descuento sucesivos: el orden no cambia, la reversión sí. |
| [006](part-00-pensamiento-matematico-desde-cero/006-razones-tasas-y-proporciones/README.md) | Razones, tasas y proporciones | `ratios` | Razón, tasa y proporción con unidades explícitas. |
| [007](part-00-pensamiento-matematico-desde-cero/007-regla-de-tres-y-escalas/README.md) | Regla de tres y escalas | `rule_of_three` | Proporcionalidad directa e inversa comparadas sobre el mismo dato. |
| [008](part-00-pensamiento-matematico-desde-cero/008-potencias-y-leyes-de-exponentes/README.md) | Potencias y leyes de exponentes | `exponent_laws` | Leyes de exponentes verificadas numéricamente. |
| [009](part-00-pensamiento-matematico-desde-cero/009-raices-y-radicales/README.md) | Raíces y radicales | `radicals` | Raíces como exponentes fraccionarios y su dominio real. |
| [010](part-00-pensamiento-matematico-desde-cero/010-orden-de-operaciones-y-parentesis/README.md) | Orden de operaciones y paréntesis | `operator_precedence` | Precedencia y asociatividad: dos lecturas de la misma cadena. |
| [011](part-00-pensamiento-matematico-desde-cero/011-notacion-cientifica/README.md) | Notación científica | `scientific_notation` | Mantisa, exponente y orden de magnitud. |
| [012](part-00-pensamiento-matematico-desde-cero/012-unidades-y-analisis-dimensional/README.md) | Unidades y análisis dimensional | `dimensional_analysis` | Conversión de unidades como multiplicación por factores unitarios. |
| [013](part-00-pensamiento-matematico-desde-cero/013-aproximacion-redondeo-y-cifras-significativas/README.md) | Aproximación, redondeo y cifras significativas | `rounding` | Redondeo bancario frente a redondeo aritmético. |
| [014](part-00-pensamiento-matematico-desde-cero/014-estimacion-y-calculo-mental/README.md) | Estimación y cálculo mental | `estimation` | Estimación por orden de magnitud contra el cálculo exacto. |
| [015](part-00-pensamiento-matematico-desde-cero/015-variables-como-cantidades-desconocidas/README.md) | Variables como cantidades desconocidas | `variables` | Una incógnita convierte una pregunta en una ecuación resoluble. |
| [016](part-00-pensamiento-matematico-desde-cero/016-expresiones-y-formulas/README.md) | Expresiones y fórmulas | `formula_evaluation` | Una fórmula evaluada con dominio y unidades declaradas. |
| [017](part-00-pensamiento-matematico-desde-cero/017-patrones-secuencias-y-regularidades/README.md) | Patrones, secuencias y regularidades | `sequences` | Detectar la regla de una secuencia y extrapolarla con cuidado. |
| [018](part-00-pensamiento-matematico-desde-cero/018-problemas-verbales-a-lenguaje-matematico/README.md) | Problemas verbales a lenguaje matemático | `word_problem` | Traducir un enunciado a ecuaciones y resolverlo. |
| [019](part-00-pensamiento-matematico-desde-cero/019-comprobacion-y-contraejemplos/README.md) | Comprobación y contraejemplos | `counterexample` | Una conjetura plausible destruida por un único contraejemplo. |
| [020](part-00-pensamiento-matematico-desde-cero/020-capstone-modelar-un-problema-cotidiano-con-matematicas/README.md) | Capstone: modelar un problema cotidiano con matemáticas | `capstone_budget_model` | Capstone: modelar un presupuesto con dinero exacto y proporciones. |
### Parte 01 — [Aritmética computacional y representación numérica](part-01-aritmetica-computacional-y-representacion-numerica/README.md)

*Qué es realmente un número dentro de una máquina: bits, complemento a dos, IEEE 754, error, condicionamiento y estabilidad.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [021](part-01-aritmetica-computacional-y-representacion-numerica/021-bits-bytes-y-sistemas-de-numeracion/README.md) | Bits, bytes y sistemas de numeración | `bits_and_bytes` | Cuántos valores distintos codifica cada ancho de palabra. |
| [022](part-01-aritmetica-computacional-y-representacion-numerica/022-conversion-decimal-a-binario/README.md) | Conversión decimal a binario | `decimal_to_binary` | Divisiones sucesivas frente a la conversión de la biblioteca. |
| [023](part-01-aritmetica-computacional-y-representacion-numerica/023-binario-octal-y-hexadecimal/README.md) | Binario, octal y hexadecimal | `bases` | La misma cantidad en base 2, 8, 10 y 16. |
| [024](part-01-aritmetica-computacional-y-representacion-numerica/024-aritmetica-binaria/README.md) | Aritmética binaria | `binary_arithmetic` | Suma y desplazamiento en binario, con acarreo visible. |
| [025](part-01-aritmetica-computacional-y-representacion-numerica/025-enteros-con-signo-y-complemento-a-dos/README.md) | Enteros con signo y complemento a dos | `twos_complement` | Representación de negativos en 8 bits. |
| [026](part-01-aritmetica-computacional-y-representacion-numerica/026-rango-overflow-y-wraparound/README.md) | Rango, overflow y wraparound | `overflow_wraparound` | Wraparound en enteros de ancho fijo simulado sobre Python. |
| [027](part-01-aritmetica-computacional-y-representacion-numerica/027-punto-fijo-frente-a-punto-flotante/README.md) | Punto fijo frente a punto flotante | `fixed_vs_floating` | Punto fijo (centavos enteros) frente a punto flotante. |
| [028](part-01-aritmetica-computacional-y-representacion-numerica/028-ieee-754-estructura-de-un-float/README.md) | IEEE 754: estructura de un float | `ieee754_layout` | Signo, exponente y mantisa de un float64. |
| [029](part-01-aritmetica-computacional-y-representacion-numerica/029-por-que-0-1-0-2-no-es-exactamente-0-3/README.md) | Por qué 0.1 + 0.2 no es exactamente 0.3 | `why_point_one` | 0.1 + 0.2 != 0.3 explicado con la fracción binaria real. |
| [030](part-01-aritmetica-computacional-y-representacion-numerica/030-error-absoluto-y-error-relativo/README.md) | Error absoluto y error relativo | `absolute_relative_error` | El error relativo es el que se propaga; el absoluto engaña con la escala. |
| [031](part-01-aritmetica-computacional-y-representacion-numerica/031-ulp-y-machine-epsilon/README.md) | ULP y machine epsilon | `ulp_epsilon` | Machine epsilon y la distancia al float siguiente. |
| [032](part-01-aritmetica-computacional-y-representacion-numerica/032-cancelacion-catastrofica/README.md) | Cancelación catastrófica | `catastrophic_cancellation` | Dos fórmulas algebraicamente iguales con precisión muy distinta. |
| [033](part-01-aritmetica-computacional-y-representacion-numerica/033-overflow-y-underflow-flotante/README.md) | Overflow y underflow flotante | `float_overflow_underflow` | Límites del float64 y el paso por subnormales. |
| [034](part-01-aritmetica-computacional-y-representacion-numerica/034-propagacion-de-errores/README.md) | Propagación de errores | `error_propagation` | Cómo crece el error al sumar 10^6 veces un valor no representable. |
| [035](part-01-aritmetica-computacional-y-representacion-numerica/035-condicionamiento-de-problemas/README.md) | Condicionamiento de problemas | `conditioning` | Número de condición de una función: sensibilidad del problema. |
| [036](part-01-aritmetica-computacional-y-representacion-numerica/036-estabilidad-de-algoritmos/README.md) | Estabilidad de algoritmos | `stability` | Misma raíz cuadrática por dos algoritmos: uno estable, otro no. |
| [037](part-01-aritmetica-computacional-y-representacion-numerica/037-precision-arbitraria-y-decimal/README.md) | Precisión arbitraria y Decimal | `arbitrary_precision` | Decimal con precisión declarada frente a float. |
| [038](part-01-aritmetica-computacional-y-representacion-numerica/038-racional-exacto-y-fraction/README.md) | Racional exacto y Fraction | `exact_rationals` | Fraction mantiene exactitud donde float ya perdió información. |
| [039](part-01-aritmetica-computacional-y-representacion-numerica/039-reproducibilidad-numerica-entre-plataformas/README.md) | Reproducibilidad numérica entre plataformas | `reproducibility` | El orden de la suma cambia el resultado en punto flotante. |
| [040](part-01-aritmetica-computacional-y-representacion-numerica/040-capstone-auditor-de-precision-numerica/README.md) | Capstone: auditor de precisión numérica | `capstone_precision_auditor` | Capstone: auditoría de precisión de una expresión numérica. |
### Parte 02 — [Álgebra y funciones](part-02-algebra-y-funciones/README.md)

*Manipulación simbólica con criterio y la función como objeto central: dominio, imagen, composición, inversa y familias lineal, cuadrática, exponencial y logarítmica.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [041](part-02-algebra-y-funciones/041-expresiones-algebraicas-y-terminos/README.md) | Expresiones algebraicas y términos | `algebraic_terms` | Términos semejantes y evaluación de una expresión. |
| [042](part-02-algebra-y-funciones/042-propiedades-distributiva-asociativa-y-conmutativa/README.md) | Propiedades distributiva, asociativa y conmutativa | `algebra_properties` | Conmutativa, asociativa y distributiva: válidas en ℝ, no siempre en float. |
| [043](part-02-algebra-y-funciones/043-ecuaciones-lineales-de-una-variable/README.md) | Ecuaciones lineales de una variable | `linear_equation` | Resolver ax + b = c y verificar el residuo. |
| [044](part-02-algebra-y-funciones/044-desigualdades-lineales/README.md) | Desigualdades lineales | `linear_inequality` | Multiplicar por un negativo invierte el sentido de la desigualdad. |
| [045](part-02-algebra-y-funciones/045-sistemas-de-ecuaciones-2x2/README.md) | Sistemas de ecuaciones 2x2 | `system_2x2` | Sistema 2x2 por determinantes (regla de Cramer) y verificación. |
| [046](part-02-algebra-y-funciones/046-polinomios-y-operaciones/README.md) | Polinomios y operaciones | `polynomial_ops` | Suma, producto y evaluación de polinomios por Horner. |
| [047](part-02-algebra-y-funciones/047-factorizacion-elemental/README.md) | Factorización elemental | `factoring` | Factorizar x² - 3x + 2 y comprobar las raíces. |
| [048](part-02-algebra-y-funciones/048-ecuaciones-cuadraticas/README.md) | Ecuaciones cuadráticas | `quadratic_equation` | Resolver una cuadrática y contrastar con la forma de vértice. |
| [049](part-02-algebra-y-funciones/049-formula-cuadratica-y-discriminante/README.md) | Fórmula cuadrática y discriminante | `discriminant` | El discriminante clasifica las raíces antes de calcularlas. |
| [050](part-02-algebra-y-funciones/050-exponentes-algebraicos/README.md) | Exponentes algebraicos | `algebraic_exponents` | Exponentes negativos, fraccionarios y su dominio. |
| [051](part-02-algebra-y-funciones/051-logaritmos-y-sus-propiedades/README.md) | Logaritmos y sus propiedades | `logarithm_laws` | Las tres leyes del logaritmo verificadas numéricamente. |
| [052](part-02-algebra-y-funciones/052-funciones-dominio-y-rango/README.md) | Funciones: dominio y rango | `domain_range` | El dominio forma parte de la definición de la función. |
| [053](part-02-algebra-y-funciones/053-funciones-lineales-y-pendiente/README.md) | Funciones lineales y pendiente | `linear_function` | Pendiente como razón de cambio constante. |
| [054](part-02-algebra-y-funciones/054-funciones-cuadraticas-y-parabolas/README.md) | Funciones cuadráticas y parábolas | `quadratic_function` | Vértice, eje de simetría y concavidad. |
| [055](part-02-algebra-y-funciones/055-funciones-exponenciales/README.md) | Funciones exponenciales | `exponential_function` | Crecimiento exponencial: razón constante, no diferencia constante. |
| [056](part-02-algebra-y-funciones/056-funciones-logaritmicas/README.md) | Funciones logarítmicas | `logarithmic_function` | El logaritmo como inversa de la exponencial y como escala. |
| [057](part-02-algebra-y-funciones/057-composicion-de-funciones/README.md) | Composición de funciones | `function_composition` | (g∘f) no es (f∘g): la composición no conmuta. |
| [058](part-02-algebra-y-funciones/058-funciones-inversas/README.md) | Funciones inversas | `inverse_function` | Inversa frente a recíproco: dos objetos distintos. |
| [059](part-02-algebra-y-funciones/059-funciones-por-tramos/README.md) | Funciones por tramos | `piecewise_function` | Una función por tramos y su continuidad en el punto de corte. |
| [060](part-02-algebra-y-funciones/060-capstone-construir-y-comparar-modelos-funcionales/README.md) | Capstone: construir y comparar modelos funcionales | `capstone_model_fitting` | Capstone: ¿lineal, cuadrático o exponencial? Decidir con residuos. |
### Parte 03 — [Geometría, trigonometría y geometría analítica](part-03-geometria-trigonometria-y-geometria-analitica/README.md)

*Del espacio a las coordenadas: distancia, ángulo, trigonometría, transformaciones lineales en el plano, coordenadas polares y proyección.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [061](part-03-geometria-trigonometria-y-geometria-analitica/061-puntos-segmentos-y-distancias/README.md) | Puntos, segmentos y distancias | `distances` | Distancia euclídea, Manhattan y Chebyshev sobre los mismos puntos. |
| [062](part-03-geometria-trigonometria-y-geometria-analitica/062-angulos-y-radianes/README.md) | Ángulos y radianes | `angles_radians` | Grados y radianes: por qué el radián es la unidad natural. |
| [063](part-03-geometria-trigonometria-y-geometria-analitica/063-triangulos-y-semejanza/README.md) | Triángulos y semejanza | `similar_triangles` | Semejanza: los ángulos se conservan, las longitudes escalan. |
| [064](part-03-geometria-trigonometria-y-geometria-analitica/064-teorema-de-pitagoras/README.md) | Teorema de Pitágoras | `pythagoras` | Pitágoras, su recíproco y una terna pitagórica generada. |
| [065](part-03-geometria-trigonometria-y-geometria-analitica/065-seno-coseno-y-tangente/README.md) | Seno, coseno y tangente | `trig_ratios` | Seno, coseno y tangente sobre un triángulo rectángulo concreto. |
| [066](part-03-geometria-trigonometria-y-geometria-analitica/066-identidades-trigonometricas-basicas/README.md) | Identidades trigonométricas básicas | `trig_identities` | Identidades fundamentales verificadas en varios ángulos. |
| [067](part-03-geometria-trigonometria-y-geometria-analitica/067-circulo-unitario/README.md) | Círculo unitario | `unit_circle` | El círculo unitario como diccionario de ángulos notables. |
| [068](part-03-geometria-trigonometria-y-geometria-analitica/068-coordenadas-cartesianas/README.md) | Coordenadas cartesianas | `cartesian_coordinates` | Cuadrantes, simetrías y traslación de origen. |
| [069](part-03-geometria-trigonometria-y-geometria-analitica/069-pendiente-y-ecuacion-de-la-recta/README.md) | Pendiente y ecuación de la recta | `line_equation` | Recta en forma pendiente-intercepto y en forma general. |
| [070](part-03-geometria-trigonometria-y-geometria-analitica/070-distancia-punto-recta/README.md) | Distancia punto-recta | `point_line_distance` | Distancia de un punto a una recta y su proyección. |
| [071](part-03-geometria-trigonometria-y-geometria-analitica/071-circunferencias-y-conicas/README.md) | Circunferencias y cónicas | `conics` | Circunferencia, elipse y parábola desde su ecuación. |
| [072](part-03-geometria-trigonometria-y-geometria-analitica/072-vectores-geometricos-2d/README.md) | Vectores geométricos 2D | `vectors_2d` | Vector como dirección y magnitud; ángulo entre vectores. |
| [073](part-03-geometria-trigonometria-y-geometria-analitica/073-transformaciones-traslacion-y-escala/README.md) | Transformaciones: traslación y escala | `translation_scale` | Traslación y escala en coordenadas homogéneas. |
| [074](part-03-geometria-trigonometria-y-geometria-analitica/074-rotaciones-2d/README.md) | Rotaciones 2D | `rotation_2d` | Matriz de rotación: ortogonal y de determinante 1. |
| [075](part-03-geometria-trigonometria-y-geometria-analitica/075-matrices-de-transformacion/README.md) | Matrices de transformación | `transform_matrices` | Composición de rotación, escala y reflexión. |
| [076](part-03-geometria-trigonometria-y-geometria-analitica/076-coordenadas-polares/README.md) | Coordenadas polares | `polar_coordinates` | Conversión cartesiana ↔ polar y su ida y vuelta. |
| [077](part-03-geometria-trigonometria-y-geometria-analitica/077-geometria-3d-y-planos/README.md) | Geometría 3D y planos | `planes_3d` | Plano por su normal, distancia de un punto y producto cruz. |
| [078](part-03-geometria-trigonometria-y-geometria-analitica/078-proyecciones-y-perspectiva/README.md) | Proyecciones y perspectiva | `projection` | Proyección ortogonal de un vector y proyección en perspectiva. |
| [079](part-03-geometria-trigonometria-y-geometria-analitica/079-aplicaciones-en-vision-robotica-y-videojuegos/README.md) | Aplicaciones en visión, robótica y videojuegos | `applications_pipeline` | Pipeline geométrico típico: modelo → mundo → cámara → pantalla. |
| [080](part-03-geometria-trigonometria-y-geometria-analitica/080-capstone-motor-geometrico-2d/README.md) | Capstone: motor geométrico 2D | `capstone_geometry_engine` | Capstone: motor 2D que compone transformaciones sobre un polígono. |
### Parte 04 — [Matemática discreta para computación](part-04-matematica-discreta-para-computacion/README.md)

*Lógica, conjuntos, conteo, inducción, recurrencias, grafos y aritmética modular: la matemática que hace demostrable un programa.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [081](part-04-matematica-discreta-para-computacion/081-logica-proposicional/README.md) | Lógica proposicional | `propositional_logic` | Implicación, contrarrecíproca y recíproca no son lo mismo. |
| [082](part-04-matematica-discreta-para-computacion/082-tablas-de-verdad-y-equivalencias/README.md) | Tablas de verdad y equivalencias | `truth_tables` | Leyes de De Morgan verificadas exhaustivamente. |
| [083](part-04-matematica-discreta-para-computacion/083-logica-de-predicados-y-cuantificadores/README.md) | Lógica de predicados y cuantificadores | `predicate_logic` | Cuantificadores: el orden cambia el significado. |
| [084](part-04-matematica-discreta-para-computacion/084-conjuntos-y-operaciones/README.md) | Conjuntos y operaciones | `sets` | Operaciones de conjuntos e inclusión-exclusión. |
| [085](part-04-matematica-discreta-para-computacion/085-relaciones-y-propiedades/README.md) | Relaciones y propiedades | `relations` | Reflexiva, simétrica y transitiva: la receta de una relación de equivalencia. |
| [086](part-04-matematica-discreta-para-computacion/086-funciones-discretas/README.md) | Funciones discretas | `discrete_functions` | Inyectiva, sobreyectiva y biyectiva sobre conjuntos finitos. |
| [087](part-04-matematica-discreta-para-computacion/087-principios-de-conteo/README.md) | Principios de conteo | `counting_principles` | Regla del producto, de la suma y conteo de contraseñas. |
| [088](part-04-matematica-discreta-para-computacion/088-permutaciones/README.md) | Permutaciones | `permutations_demo` | Permutaciones: el orden importa. |
| [089](part-04-matematica-discreta-para-computacion/089-combinaciones/README.md) | Combinaciones | `combinations_demo` | Combinaciones: el orden no importa. |
| [090](part-04-matematica-discreta-para-computacion/090-principio-del-palomar/README.md) | Principio del palomar | `pigeonhole` | Principio del palomar: colisiones garantizadas sin construirlas. |
| [091](part-04-matematica-discreta-para-computacion/091-induccion-matematica/README.md) | Inducción matemática | `induction` | Inducción: caso base, paso inductivo y verificación empírica. |
| [092](part-04-matematica-discreta-para-computacion/092-recurrencias/README.md) | Recurrencias | `recurrences` | Recurrencia lineal: iterativo, memoizado y forma cerrada. |
| [093](part-04-matematica-discreta-para-computacion/093-grafos-vertices-y-aristas/README.md) | Grafos: vértices y aristas | `graphs` | Grados, aristas y el lema del apretón de manos. |
| [094](part-04-matematica-discreta-para-computacion/094-caminos-ciclos-y-conectividad/README.md) | Caminos, ciclos y conectividad | `paths_connectivity` | Recorrido BFS: alcanzabilidad y distancia en aristas. |
| [095](part-04-matematica-discreta-para-computacion/095-arboles-y-arboles-de-expansion/README.md) | Árboles y árboles de expansión | `trees` | Un árbol con n nodos tiene exactamente n-1 aristas. |
| [096](part-04-matematica-discreta-para-computacion/096-dag-y-orden-topologico/README.md) | DAG y orden topológico | `topological_order` | Orden topológico y detección de ciclos por conteo de Kahn. |
| [097](part-04-matematica-discreta-para-computacion/097-algebra-booleana/README.md) | Álgebra booleana | `boolean_algebra` | Álgebra booleana: simplificación y equivalencia funcional. |
| [098](part-04-matematica-discreta-para-computacion/098-aritmetica-modular/README.md) | Aritmética modular | `modular_arithmetic` | Aritmética modular: exponenciación rápida e inverso modular. |
| [099](part-04-matematica-discreta-para-computacion/099-numeros-primos-y-maximo-comun-divisor/README.md) | Números primos y máximo común divisor | `primes_gcd` | Criba, MCD por Euclides y su relación con el mínimo común múltiplo. |
| [100](part-04-matematica-discreta-para-computacion/100-capstone-modelar-dependencias-con-grafos/README.md) | Capstone: modelar dependencias con grafos | `capstone_dependency_graph` | Capstone: planificar un pipeline con grafos y detectar dependencias rotas. |
### Parte 05 — [Álgebra lineal I: vectores y matrices](part-05-algebra-lineal-i-vectores-y-matrices/README.md)

*Vectores, normas, producto punto, independencia, span, sistemas lineales, eliminación de Gauss, rango, inversa, determinante y proyección ortogonal.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [101](part-05-algebra-lineal-i-vectores-y-matrices/101-escalares-vectores-y-matrices/README.md) | Escalares, vectores y matrices | `scalars_vectors_matrices` | Escalar, vector y matriz como objetos con forma y significado. |
| [102](part-05-algebra-lineal-i-vectores-y-matrices/102-operaciones-con-vectores/README.md) | Operaciones con vectores | `vector_operations` | Suma, resta y combinación lineal con interpretación geométrica. |
| [103](part-05-algebra-lineal-i-vectores-y-matrices/103-producto-punto-y-similitud/README.md) | Producto punto y similitud | `dot_product` | Producto punto: proyección, ángulo y similitud. |
| [104](part-05-algebra-lineal-i-vectores-y-matrices/104-normas-y-distancias/README.md) | Normas y distancias | `norms_distances` | L1, L2 e L∞ sobre el mismo vector. |
| [105](part-05-algebra-lineal-i-vectores-y-matrices/105-vectores-unitarios/README.md) | Vectores unitarios | `unit_vectors` | Normalizar separa dirección de magnitud. |
| [106](part-05-algebra-lineal-i-vectores-y-matrices/106-combinaciones-lineales/README.md) | Combinaciones lineales | `linear_combinations` | Toda combinación lineal de la base canónica reconstruye el vector. |
| [107](part-05-algebra-lineal-i-vectores-y-matrices/107-independencia-y-dependencia-lineal/README.md) | Independencia y dependencia lineal | `linear_independence` | Independencia detectada por el rango, no por inspección. |
| [108](part-05-algebra-lineal-i-vectores-y-matrices/108-span-y-subespacios/README.md) | Span y subespacios | `span_subspaces` | El span de dos vectores en ℝ³ es un plano, no todo el espacio. |
| [109](part-05-algebra-lineal-i-vectores-y-matrices/109-matrices-y-operaciones-basicas/README.md) | Matrices y operaciones básicas | `matrix_basics` | Suma, escala y transpuesta de matrices. |
| [110](part-05-algebra-lineal-i-vectores-y-matrices/110-producto-matriz-vector/README.md) | Producto matriz-vector | `matrix_vector` | Ax como combinación lineal de las columnas de A. |
| [111](part-05-algebra-lineal-i-vectores-y-matrices/111-producto-de-matrices/README.md) | Producto de matrices | `matrix_product` | AB ≠ BA y el coste cúbico del producto. |
| [112](part-05-algebra-lineal-i-vectores-y-matrices/112-transpuesta-y-simetria/README.md) | Transpuesta y simetría | `transpose_symmetry` | Toda matriz cuadrada se descompone en parte simétrica y antisimétrica. |
| [113](part-05-algebra-lineal-i-vectores-y-matrices/113-sistemas-lineales/README.md) | Sistemas lineales | `linear_systems` | Sistema 3x3: solución, residuo y unicidad. |
| [114](part-05-algebra-lineal-i-vectores-y-matrices/114-eliminacion-de-gauss/README.md) | Eliminación de Gauss | `gaussian_elimination_demo` | Eliminación de Gauss con pivoteo parcial, paso a paso. |
| [115](part-05-algebra-lineal-i-vectores-y-matrices/115-forma-escalonada-y-rango/README.md) | Forma escalonada y rango | `echelon_rank` | Rango: la dimensión efectiva de la transformación. |
| [116](part-05-algebra-lineal-i-vectores-y-matrices/116-inversa-de-una-matriz/README.md) | Inversa de una matriz | `matrix_inverse` | La inversa existe, pero rara vez conviene calcularla. |
| [117](part-05-algebra-lineal-i-vectores-y-matrices/117-determinantes/README.md) | Determinantes | `determinants` | El determinante mide el escalado de volumen y detecta singularidad. |
| [118](part-05-algebra-lineal-i-vectores-y-matrices/118-matrices-ortogonales/README.md) | Matrices ortogonales | `orthogonal_matrices` | Matriz ortogonal: QᵀQ = I, preserva normas y ángulos. |
| [119](part-05-algebra-lineal-i-vectores-y-matrices/119-proyecciones-ortogonales/README.md) | Proyecciones ortogonales | `orthogonal_projection` | Proyección sobre un subespacio y descomposición ortogonal. |
| [120](part-05-algebra-lineal-i-vectores-y-matrices/120-capstone-resolver-un-sistema-de-recomendacion-lineal/README.md) | Capstone: resolver un sistema de recomendación lineal | `capstone_linear_recommender` | Capstone: recomendación lineal por similitud coseno entre usuarios. |
### Parte 06 — [Álgebra lineal II: descomposiciones y tensores](part-06-algebra-lineal-ii-descomposiciones-y-tensores/README.md)

*Cambio de base, autovalores, diagonalización, LU, QR, mínimos cuadrados, SVD, pseudoinversa, PCA y álgebra tensorial.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [121](part-06-algebra-lineal-ii-descomposiciones-y-tensores/121-bases-y-coordenadas/README.md) | Bases y coordenadas | `bases_coordinates` | Las coordenadas dependen de la base elegida. |
| [122](part-06-algebra-lineal-ii-descomposiciones-y-tensores/122-cambio-de-base/README.md) | Cambio de base | `change_of_basis` | Matriz de cambio de base y su inversa. |
| [123](part-06-algebra-lineal-ii-descomposiciones-y-tensores/123-transformaciones-lineales/README.md) | Transformaciones lineales | `linear_transformations` | Una transformación lineal preserva sumas y escalados. |
| [124](part-06-algebra-lineal-ii-descomposiciones-y-tensores/124-nucleo-e-imagen/README.md) | Núcleo e imagen | `kernel_image` | Núcleo, imagen y teorema del rango-nulidad. |
| [125](part-06-algebra-lineal-ii-descomposiciones-y-tensores/125-autovalores-y-autovectores/README.md) | Autovalores y autovectores | `eigen` | Autovalores: direcciones que la transformación solo escala. |
| [126](part-06-algebra-lineal-ii-descomposiciones-y-tensores/126-diagonalizacion/README.md) | Diagonalización | `diagonalization` | A = PDP⁻¹: la base donde la transformación solo escala. |
| [127](part-06-algebra-lineal-ii-descomposiciones-y-tensores/127-matrices-positivas-definidas/README.md) | Matrices positivas definidas | `positive_definite` | Definida positiva: todos los autovalores positivos, xᵀAx > 0. |
| [128](part-06-algebra-lineal-ii-descomposiciones-y-tensores/128-formas-cuadraticas/README.md) | Formas cuadráticas | `quadratic_forms` | La forma cuadrática xᵀAx y sus curvas de nivel. |
| [129](part-06-algebra-lineal-ii-descomposiciones-y-tensores/129-descomposicion-lu/README.md) | Descomposición LU | `lu_decomposition` | LU: factorizar una vez, resolver muchos sistemas. |
| [130](part-06-algebra-lineal-ii-descomposiciones-y-tensores/130-descomposicion-qr/README.md) | Descomposición QR | `qr_decomposition` | QR por Gram-Schmidt: base ortonormal del espacio columna. |
| [131](part-06-algebra-lineal-ii-descomposiciones-y-tensores/131-minimos-cuadrados-lineales/README.md) | Mínimos cuadrados lineales | `least_squares` | Mínimos cuadrados por ecuaciones normales. |
| [132](part-06-algebra-lineal-ii-descomposiciones-y-tensores/132-svd-desde-la-intuicion/README.md) | SVD desde la intuición | `svd_intuition` | SVD: rotar, escalar, rotar. Existe siempre. |
| [133](part-06-algebra-lineal-ii-descomposiciones-y-tensores/133-svd-y-compresion/README.md) | SVD y compresión | `svd_compression` | Aproximación de rango 1 y energía retenida. |
| [134](part-06-algebra-lineal-ii-descomposiciones-y-tensores/134-pseudoinversa-de-moore-penrose/README.md) | Pseudoinversa de Moore-Penrose | `pseudoinverse` | Pseudoinversa de Moore-Penrose para sistemas sobredeterminados. |
| [135](part-06-algebra-lineal-ii-descomposiciones-y-tensores/135-pca-desde-algebra-lineal/README.md) | PCA desde álgebra lineal | `pca` | PCA como autodescomposición de la covarianza. |
| [136](part-06-algebra-lineal-ii-descomposiciones-y-tensores/136-producto-de-kronecker/README.md) | Producto de Kronecker | `kronecker` | Producto de Kronecker: estructura en bloques. |
| [137](part-06-algebra-lineal-ii-descomposiciones-y-tensores/137-tensores-indices-shape-y-orden/README.md) | Tensores: índices, shape y orden | `tensors` | Orden, shape y reordenamiento de índices. |
| [138](part-06-algebra-lineal-ii-descomposiciones-y-tensores/138-broadcasting-como-operacion-tensorial/README.md) | Broadcasting como operación tensorial | `broadcasting` | Broadcasting: reglas de compatibilidad de shapes. |
| [139](part-06-algebra-lineal-ii-descomposiciones-y-tensores/139-einstein-summation/README.md) | Einstein summation | `einsum` | Notación de Einstein: índices repetidos se suman. |
| [140](part-06-algebra-lineal-ii-descomposiciones-y-tensores/140-capstone-pca-y-compresion-de-imagenes/README.md) | Capstone: PCA y compresión de imágenes | `capstone_pca_compression` | Capstone: comprimir una matriz con SVD y medir la pérdida. |
### Parte 07 — [Cálculo diferencial e integral](part-07-calculo-diferencial-e-integral/README.md)

*Límite, continuidad, derivada, reglas de derivación, Taylor, optimización de una variable, integral definida y teorema fundamental del cálculo.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [141](part-07-calculo-diferencial-e-integral/141-intuicion-de-limite/README.md) | Intuición de límite | `limit_intuition` | sin(x)/x cuando x→0: indeterminado en el punto, definido en el límite. |
| [142](part-07-calculo-diferencial-e-integral/142-limites-algebraicos/README.md) | Límites algebraicos | `algebraic_limits` | Indeterminación 0/0 resuelta por factorización. |
| [143](part-07-calculo-diferencial-e-integral/143-continuidad/README.md) | Continuidad | `continuity` | Los tres requisitos de continuidad en un punto. |
| [144](part-07-calculo-diferencial-e-integral/144-derivada-como-tasa-de-cambio/README.md) | Derivada como tasa de cambio | `derivative_as_rate` | Derivada como límite del cociente incremental. |
| [145](part-07-calculo-diferencial-e-integral/145-reglas-de-derivacion/README.md) | Reglas de derivación | `derivative_rules` | Reglas de potencia, suma y constante verificadas numéricamente. |
| [146](part-07-calculo-diferencial-e-integral/146-regla-del-producto-y-cociente/README.md) | Regla del producto y cociente | `product_quotient_rule` | Regla del producto y del cociente. |
| [147](part-07-calculo-diferencial-e-integral/147-regla-de-la-cadena/README.md) | Regla de la cadena | `chain_rule` | La regla de la cadena: el mecanismo entero de backpropagation. |
| [148](part-07-calculo-diferencial-e-integral/148-derivadas-de-exponenciales-y-logaritmos/README.md) | Derivadas de exponenciales y logaritmos | `exp_log_derivatives` | e^x es su propia derivada; log tiene derivada 1/x. |
| [149](part-07-calculo-diferencial-e-integral/149-derivadas-trigonometricas/README.md) | Derivadas trigonométricas | `trig_derivatives` | Derivadas trigonométricas y su ciclo de periodo 4. |
| [150](part-07-calculo-diferencial-e-integral/150-derivacion-implicita/README.md) | Derivación implícita | `implicit_differentiation` | Derivación implícita sobre la circunferencia x²+y²=25. |
| [151](part-07-calculo-diferencial-e-integral/151-aproximacion-lineal-y-taylor/README.md) | Aproximación lineal y Taylor | `taylor_approximation` | Taylor de e^x en 0: el error cae con el grado. |
| [152](part-07-calculo-diferencial-e-integral/152-maximos-y-minimos/README.md) | Máximos y mínimos | `extrema` | Máximos y mínimos por derivada y criterio de la segunda derivada. |
| [153](part-07-calculo-diferencial-e-integral/153-integral-como-acumulacion/README.md) | Integral como acumulación | `integral_as_accumulation` | Sumas de Riemann convergiendo a la integral. |
| [154](part-07-calculo-diferencial-e-integral/154-integral-definida/README.md) | Integral definida | `definite_integral` | Propiedades de la integral definida. |
| [155](part-07-calculo-diferencial-e-integral/155-antiderivadas/README.md) | Antiderivadas | `antiderivatives` | La antiderivada no es única: difiere en una constante. |
| [156](part-07-calculo-diferencial-e-integral/156-teorema-fundamental-del-calculo/README.md) | Teorema fundamental del cálculo | `fundamental_theorem` | Teorema fundamental: derivar deshace integrar. |
| [157](part-07-calculo-diferencial-e-integral/157-integracion-por-sustitucion/README.md) | Integración por sustitución | `substitution` | Integración por sustitución: la regla de la cadena al revés. |
| [158](part-07-calculo-diferencial-e-integral/158-integracion-por-partes/README.md) | Integración por partes | `integration_by_parts` | Integración por partes: la regla del producto al revés. |
| [159](part-07-calculo-diferencial-e-integral/159-integracion-numerica-introductoria/README.md) | Integración numérica introductoria | `numerical_integration_intro` | Trapecio frente a Simpson sobre la misma integral. |
| [160](part-07-calculo-diferencial-e-integral/160-capstone-optimizar-y-acumular-una-senal/README.md) | Capstone: optimizar y acumular una señal | `capstone_optimize_and_accumulate` | Capstone: derivar para optimizar e integrar para acumular una señal. |
### Parte 08 — [Cálculo multivariable, matricial y autodiferenciación](part-08-calculo-multivariable-matricial-y-autodiferenciacion/README.md)

*Derivadas parciales, gradiente, Jacobiano, Hessiano, Taylor multivariable, multiplicadores de Lagrange, cálculo matricial y autodiferenciación.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [161](part-08-calculo-multivariable-matricial-y-autodiferenciacion/161-funciones-de-varias-variables/README.md) | Funciones de varias variables | `multivariable_functions` | Una función de dos variables evaluada sobre una malla. |
| [162](part-08-calculo-multivariable-matricial-y-autodiferenciacion/162-superficies-y-curvas-de-nivel/README.md) | Superficies y curvas de nivel | `level_curves` | Curvas de nivel: dónde la función vale lo mismo. |
| [163](part-08-calculo-multivariable-matricial-y-autodiferenciacion/163-derivadas-parciales/README.md) | Derivadas parciales | `partial_derivatives` | Derivadas parciales: mover una variable congelando el resto. |
| [164](part-08-calculo-multivariable-matricial-y-autodiferenciacion/164-gradiente/README.md) | Gradiente | `gradient` | El gradiente apunta al mayor ascenso. |
| [165](part-08-calculo-multivariable-matricial-y-autodiferenciacion/165-derivada-direccional/README.md) | Derivada direccional | `directional_derivative` | Derivada direccional como proyección del gradiente. |
| [166](part-08-calculo-multivariable-matricial-y-autodiferenciacion/166-plano-tangente/README.md) | Plano tangente | `tangent_plane` | Plano tangente: la aproximación lineal en dos variables. |
| [167](part-08-calculo-multivariable-matricial-y-autodiferenciacion/167-regla-de-la-cadena-multivariable/README.md) | Regla de la cadena multivariable | `multivariable_chain_rule` | Regla de la cadena con variables intermedias. |
| [168](part-08-calculo-multivariable-matricial-y-autodiferenciacion/168-jacobiano/README.md) | Jacobiano | `jacobian` | Jacobiano de una función vectorial. |
| [169](part-08-calculo-multivariable-matricial-y-autodiferenciacion/169-hessiano/README.md) | Hessiano | `hessian` | Hessiano: curvatura y clasificación del punto crítico. |
| [170](part-08-calculo-multivariable-matricial-y-autodiferenciacion/170-taylor-multivariable/README.md) | Taylor multivariable | `multivariable_taylor` | Taylor de segundo orden en dos variables. |
| [171](part-08-calculo-multivariable-matricial-y-autodiferenciacion/171-optimizacion-sin-restricciones/README.md) | Optimización sin restricciones | `unconstrained_optimization` | Descenso de gradiente sobre una cuadrática con historial. |
| [172](part-08-calculo-multivariable-matricial-y-autodiferenciacion/172-multiplicadores-de-lagrange/README.md) | Multiplicadores de Lagrange | `lagrange_multipliers` | Maximizar xy sujeto a x+y=10 con multiplicadores de Lagrange. |
| [173](part-08-calculo-multivariable-matricial-y-autodiferenciacion/173-integrales-dobles/README.md) | Integrales dobles | `double_integrals` | Integral doble sobre un rectángulo por suma de Riemann. |
| [174](part-08-calculo-multivariable-matricial-y-autodiferenciacion/174-integrales-triples/README.md) | Integrales triples | `triple_integrals` | Volumen y masa de un cubo con densidad variable. |
| [175](part-08-calculo-multivariable-matricial-y-autodiferenciacion/175-campos-vectoriales/README.md) | Campos vectoriales | `vector_fields` | Campo vectorial, líneas de flujo y campo conservativo. |
| [176](part-08-calculo-multivariable-matricial-y-autodiferenciacion/176-divergencia-y-rotacional/README.md) | Divergencia y rotacional | `divergence_curl` | Divergencia y rotacional calculados numéricamente. |
| [177](part-08-calculo-multivariable-matricial-y-autodiferenciacion/177-calculo-matricial/README.md) | Cálculo matricial | `matrix_calculus` | Identidades básicas de cálculo matricial. |
| [178](part-08-calculo-multivariable-matricial-y-autodiferenciacion/178-derivadas-respecto-de-vectores-y-matrices/README.md) | Derivadas respecto de vectores y matrices | `vector_matrix_derivatives` | Gradiente de una pérdida cuadrática respecto de los pesos. |
| [179](part-08-calculo-multivariable-matricial-y-autodiferenciacion/179-automatic-differentiation-y-computational-graphs/README.md) | Automatic differentiation y computational graphs | `autodiff` | Autodiferenciación en modo reverso sobre el grafo de cómputo. |
| [180](part-08-calculo-multivariable-matricial-y-autodiferenciacion/180-capstone-backpropagation-manual-y-automatica/README.md) | Capstone: backpropagation manual y automática | `capstone_backpropagation` | Capstone: backpropagation manual y automática sobre la misma red. |
### Parte 09 — [Probabilidad y procesos aleatorios](part-09-probabilidad-y-procesos-aleatorios/README.md)

*Axiomas, probabilidad condicional, Bayes, variables aleatorias, esperanza, varianza, distribuciones clave, LGN, TCL, Monte Carlo y cadenas de Markov.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [181](part-09-probabilidad-y-procesos-aleatorios/181-experimentos-espacio-muestral-y-eventos/README.md) | Experimentos, espacio muestral y eventos | `sample_space` | Espacio muestral, eventos y su probabilidad en un modelo equiprobable. |
| [182](part-09-probabilidad-y-procesos-aleatorios/182-axiomas-de-probabilidad/README.md) | Axiomas de probabilidad | `axioms` | Los tres axiomas de Kolmogorov verificados sobre un modelo. |
| [183](part-09-probabilidad-y-procesos-aleatorios/183-reglas-de-suma-y-producto/README.md) | Reglas de suma y producto | `sum_product_rules` | Regla de la suma con y sin exclusión mutua. |
| [184](part-09-probabilidad-y-procesos-aleatorios/184-probabilidad-condicional/README.md) | Probabilidad condicional | `conditional` | P(A|B) cambia el espacio muestral, no la realidad. |
| [185](part-09-probabilidad-y-procesos-aleatorios/185-independencia/README.md) | Independencia | `independence` | Independencia se comprueba, no se supone. |
| [186](part-09-probabilidad-y-procesos-aleatorios/186-teorema-de-bayes/README.md) | Teorema de Bayes | `bayes` | Test médico: por qué un positivo no significa enfermedad. |
| [187](part-09-probabilidad-y-procesos-aleatorios/187-variables-aleatorias-discretas/README.md) | Variables aleatorias discretas | `discrete_rv` | Variable aleatoria discreta: pmf, cdf y coherencia. |
| [188](part-09-probabilidad-y-procesos-aleatorios/188-variables-aleatorias-continuas/README.md) | Variables aleatorias continuas | `continuous_rv` | Variable continua: la densidad no es una probabilidad. |
| [189](part-09-probabilidad-y-procesos-aleatorios/189-esperanza-matematica/README.md) | Esperanza matemática | `expectation` | Linealidad de la esperanza, incluso sin independencia. |
| [190](part-09-probabilidad-y-procesos-aleatorios/190-varianza-y-desviacion-estandar/README.md) | Varianza y desviación estándar | `variance` | Varianza, desviación estándar y el estimador insesgado. |
| [191](part-09-probabilidad-y-procesos-aleatorios/191-covarianza-y-correlacion/README.md) | Covarianza y correlación | `covariance_correlation` | Covarianza depende de la escala; la correlación no. |
| [192](part-09-probabilidad-y-procesos-aleatorios/192-bernoulli-y-binomial/README.md) | Bernoulli y binomial | `bernoulli_binomial` | De un ensayo a n ensayos: Bernoulli y binomial. |
| [193](part-09-probabilidad-y-procesos-aleatorios/193-poisson-y-exponencial/README.md) | Poisson y exponencial | `poisson_exponential` | Poisson cuenta eventos; la exponencial mide el tiempo entre ellos. |
| [194](part-09-probabilidad-y-procesos-aleatorios/194-distribucion-normal/README.md) | Distribución normal | `normal_distribution` | Normal: regla 68-95-99.7 y estandarización. |
| [195](part-09-probabilidad-y-procesos-aleatorios/195-distribuciones-conjuntas-y-marginales/README.md) | Distribuciones conjuntas y marginales | `joint_marginal` | Distribución conjunta, marginales y condicional. |
| [196](part-09-probabilidad-y-procesos-aleatorios/196-ley-de-los-grandes-numeros/README.md) | Ley de los grandes números | `law_large_numbers` | La media muestral converge, pero lentamente. |
| [197](part-09-probabilidad-y-procesos-aleatorios/197-teorema-central-del-limite/README.md) | Teorema central del límite | `central_limit` | El TCL en acción sobre una distribución claramente no normal. |
| [198](part-09-probabilidad-y-procesos-aleatorios/198-metodos-monte-carlo/README.md) | Métodos Monte Carlo | `monte_carlo` | Estimar π por Monte Carlo con su error e intervalo. |
| [199](part-09-probabilidad-y-procesos-aleatorios/199-cadenas-de-markov/README.md) | Cadenas de Markov | `markov_chains` | Cadena de Markov: matriz de transición y distribución estacionaria. |
| [200](part-09-probabilidad-y-procesos-aleatorios/200-capstone-simulador-probabilistico-y-bayesiano/README.md) | Capstone: simulador probabilístico y bayesiano | `capstone_probabilistic_simulator` | Capstone: simulador probabilístico con actualización bayesiana. |
### Parte 10 — [Estadística e inferencia](part-10-estadistica-e-inferencia/README.md)

*Descriptiva, muestreo, estimadores, intervalos de confianza, pruebas de hipótesis, p-value, potencia, verosimilitud, MAP, inferencia bayesiana, bootstrap y A/B testing.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [201](part-10-estadistica-e-inferencia/201-estadistica-descriptiva/README.md) | Estadística descriptiva | `descriptive_statistics` | Centro, dispersión y forma: tres preguntas distintas. |
| [202](part-10-estadistica-e-inferencia/202-poblacion-muestra-y-sesgo-de-seleccion/README.md) | Población, muestra y sesgo de selección | `population_sample` | Sesgo de selección: la muestra no representa a la población. |
| [203](part-10-estadistica-e-inferencia/203-muestreo-y-distribuciones-muestrales/README.md) | Muestreo y distribuciones muestrales | `sampling_distributions` | La distribución de la media muestral y su error estándar. |
| [204](part-10-estadistica-e-inferencia/204-estimadores-y-propiedades/README.md) | Estimadores y propiedades | `estimators` | Sesgo, varianza y consistencia de dos estimadores de la varianza. |
| [205](part-10-estadistica-e-inferencia/205-intervalos-de-confianza/README.md) | Intervalos de confianza | `confidence_intervals` | Un IC 95 % describe el procedimiento, no una probabilidad del parámetro. |
| [206](part-10-estadistica-e-inferencia/206-pruebas-de-hipotesis/README.md) | Pruebas de hipótesis | `hypothesis_testing` | Estructura completa de una prueba de hipótesis. |
| [207](part-10-estadistica-e-inferencia/207-p-value-correctamente-interpretado/README.md) | p-value correctamente interpretado | `p_value` | Qué mide y qué no mide un p-value. |
| [208](part-10-estadistica-e-inferencia/208-errores-tipo-i-y-ii/README.md) | Errores tipo I y II | `type_errors` | Errores tipo I y II: el compromiso es inevitable. |
| [209](part-10-estadistica-e-inferencia/209-potencia-estadistica/README.md) | Potencia estadística | `statistical_power` | Potencia en función del tamaño muestral. |
| [210](part-10-estadistica-e-inferencia/210-t-test-y-comparacion-de-medias/README.md) | t-test y comparación de medias | `t_test` | t-test de dos muestras independientes. |
| [211](part-10-estadistica-e-inferencia/211-chi-cuadrado-y-tablas-de-contingencia/README.md) | Chi-cuadrado y tablas de contingencia | `chi_square` | Chi-cuadrado de independencia sobre una tabla de contingencia. |
| [212](part-10-estadistica-e-inferencia/212-anova/README.md) | ANOVA | `anova` | ANOVA de un factor: descomposición de la variabilidad. |
| [213](part-10-estadistica-e-inferencia/213-correlacion-frente-a-causalidad/README.md) | Correlación frente a causalidad | `correlation_causation` | Una variable de confusión genera correlación sin causalidad. |
| [214](part-10-estadistica-e-inferencia/214-regresion-lineal-estadistica/README.md) | Regresión lineal estadística | `linear_regression_stats` | Regresión lineal con R², error estándar y significancia. |
| [215](part-10-estadistica-e-inferencia/215-maxima-verosimilitud/README.md) | Máxima verosimilitud | `maximum_likelihood` | MLE para la normal: la media muestral maximiza la verosimilitud. |
| [216](part-10-estadistica-e-inferencia/216-estimacion-map/README.md) | Estimación MAP | `map_estimation` | MAP: verosimilitud más prior, y su límite con muchos datos. |
| [217](part-10-estadistica-e-inferencia/217-inferencia-bayesiana/README.md) | Inferencia bayesiana | `bayesian_inference` | Actualización bayesiana conjugada Beta-Binomial. |
| [218](part-10-estadistica-e-inferencia/218-bootstrap-y-remuestreo/README.md) | Bootstrap y remuestreo | `bootstrap` | Bootstrap: estimar la variabilidad sin suponer la distribución. |
| [219](part-10-estadistica-e-inferencia/219-a-b-testing-y-diseno-experimental/README.md) | A/B testing y diseño experimental | `ab_testing` | A/B test de proporciones con tamaño muestral y significancia. |
| [220](part-10-estadistica-e-inferencia/220-capstone-estudio-estadistico-reproducible/README.md) | Capstone: estudio estadístico reproducible | `capstone_reproducible_study` | Capstone: estudio completo, reproducible y con límites declarados. |
### Parte 11 — [Métodos numéricos y computación científica](part-11-metodos-numericos-y-computacion-cientifica/README.md)

*Raíces, interpolación, splines, diferenciación y cuadratura numérica, sistemas lineales iterativos, mínimos cuadrados y ecuaciones diferenciales.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [221](part-11-metodos-numericos-y-computacion-cientifica/221-errores-numericos-y-convergencia/README.md) | Errores numéricos y convergencia | `numerical_errors` | Error de truncamiento frente a error de redondeo. |
| [222](part-11-metodos-numericos-y-computacion-cientifica/222-biseccion/README.md) | Bisección | `bisection` | Bisección: lenta pero garantizada si hay cambio de signo. |
| [223](part-11-metodos-numericos-y-computacion-cientifica/223-newton-raphson/README.md) | Newton-Raphson | `newton_raphson` | Newton: convergencia cuadrática cerca de la raíz. |
| [224](part-11-metodos-numericos-y-computacion-cientifica/224-metodo-de-la-secante/README.md) | Método de la secante | `secant` | Secante: casi tan rápida como Newton sin necesitar la derivada. |
| [225](part-11-metodos-numericos-y-computacion-cientifica/225-interpolacion-de-lagrange/README.md) | Interpolación de Lagrange | `lagrange_interpolation` | Interpolación de Lagrange y el fenómeno de Runge. |
| [226](part-11-metodos-numericos-y-computacion-cientifica/226-splines/README.md) | Splines | `splines` | Spline lineal por tramos frente a un polinomio único. |
| [227](part-11-metodos-numericos-y-computacion-cientifica/227-diferenciacion-numerica/README.md) | Diferenciación numérica | `numerical_differentiation` | Fórmulas de diferencias y su orden de error. |
| [228](part-11-metodos-numericos-y-computacion-cientifica/228-cuadratura-numerica/README.md) | Cuadratura numérica | `quadrature` | Cuadratura gaussiana: máxima exactitud con mínimos nodos. |
| [229](part-11-metodos-numericos-y-computacion-cientifica/229-regla-del-trapecio/README.md) | Regla del trapecio | `trapezoid_rule` | Regla del trapecio y su convergencia O(h²). |
| [230](part-11-metodos-numericos-y-computacion-cientifica/230-simpson/README.md) | Simpson | `simpson_rule` | Simpson y su convergencia O(h⁴). |
| [231](part-11-metodos-numericos-y-computacion-cientifica/231-sistemas-lineales-directos/README.md) | Sistemas lineales directos | `direct_linear_solvers` | Solvers directos: LU y sustitución, con conteo de operaciones. |
| [232](part-11-metodos-numericos-y-computacion-cientifica/232-jacobi-y-gauss-seidel/README.md) | Jacobi y Gauss-Seidel | `jacobi_gauss_seidel` | Métodos iterativos sobre una matriz diagonalmente dominante. |
| [233](part-11-metodos-numericos-y-computacion-cientifica/233-metodos-iterativos-y-tolerancias/README.md) | Métodos iterativos y tolerancias | `iterative_tolerances` | Criterio de parada: absoluto, relativo y residuo. |
| [234](part-11-metodos-numericos-y-computacion-cientifica/234-minimos-cuadrados-numericos/README.md) | Mínimos cuadrados numéricos | `numerical_least_squares` | Mínimos cuadrados: ecuaciones normales frente a QR. |
| [235](part-11-metodos-numericos-y-computacion-cientifica/235-ecuaciones-diferenciales-ordinarias/README.md) | Ecuaciones diferenciales ordinarias | `odes` | EDO con solución analítica para medir el error de cada método. |
| [236](part-11-metodos-numericos-y-computacion-cientifica/236-metodo-de-euler/README.md) | Método de Euler | `euler_method` | Euler explícito: orden 1 y coste mínimo. |
| [237](part-11-metodos-numericos-y-computacion-cientifica/237-runge-kutta/README.md) | Runge-Kutta | `runge_kutta` | RK4: cuatro evaluaciones por paso, error O(h⁴). |
| [238](part-11-metodos-numericos-y-computacion-cientifica/238-introduccion-a-pde-y-discretizacion/README.md) | Introducción a PDE y discretización | `pde_discretization` | Discretización de la ecuación del calor en 1D (esquema explícito). |
| [239](part-11-metodos-numericos-y-computacion-cientifica/239-computacion-cientifica-con-scipy/README.md) | Computación científica con SciPy | `scientific_computing` | Qué aporta SciPy sobre una implementación propia. |
| [240](part-11-metodos-numericos-y-computacion-cientifica/240-capstone-solver-numerico-con-informe-de-error/README.md) | Capstone: solver numérico con informe de error | `capstone_numerical_solver` | Capstone: solver con informe de error y criterio de parada declarado. |
### Parte 12 — [Optimización matemática y computacional](part-12-optimizacion-matematica-y-computacional/README.md)

*Función objetivo, convexidad, descenso de gradiente y su familia completa de optimizadores, métodos de segundo orden, restricciones, KKT y optimización evolutiva.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [241](part-12-optimizacion-matematica-y-computacional/241-problemas-de-optimizacion-y-funcion-objetivo/README.md) | Problemas de optimización y función objetivo | `objective_function` | Anatomía de un problema de optimización. |
| [242](part-12-optimizacion-matematica-y-computacional/242-convexidad/README.md) | Convexidad | `convexity` | Convexidad: la propiedad que convierte un mínimo local en global. |
| [243](part-12-optimizacion-matematica-y-computacional/243-gradiente-y-direcciones-de-descenso/README.md) | Gradiente y direcciones de descenso | `descent_directions` | Cualquier dirección con dᵀ∇f < 0 hace descender la función. |
| [244](part-12-optimizacion-matematica-y-computacional/244-gradient-descent/README.md) | Gradient descent | `gradient_descent` | Descenso de gradiente y el efecto del learning rate. |
| [245](part-12-optimizacion-matematica-y-computacional/245-stochastic-gradient-descent/README.md) | Stochastic gradient descent | `sgd` | SGD: gradiente ruidoso, progreso más barato. |
| [246](part-12-optimizacion-matematica-y-computacional/246-momentum/README.md) | Momentum | `momentum` | Momentum acumula velocidad y amortigua la oscilación. |
| [247](part-12-optimizacion-matematica-y-computacional/247-nesterov-accelerated-gradient/README.md) | Nesterov accelerated gradient | `nesterov` | NAG mira adelante antes de calcular el gradiente. |
| [248](part-12-optimizacion-matematica-y-computacional/248-adagrad/README.md) | AdaGrad | `adagrad` | AdaGrad adapta el paso por coordenada, pero se apaga. |
| [249](part-12-optimizacion-matematica-y-computacional/249-rmsprop/README.md) | RMSProp | `rmsprop` | RMSProp: media móvil del gradiente al cuadrado. |
| [250](part-12-optimizacion-matematica-y-computacional/250-adam/README.md) | Adam | `adam` | Adam: momentum de primer y segundo orden con corrección de sesgo. |
| [251](part-12-optimizacion-matematica-y-computacional/251-adamw/README.md) | AdamW | `adamw` | AdamW desacopla el weight decay del gradiente adaptativo. |
| [252](part-12-optimizacion-matematica-y-computacional/252-metodo-de-newton/README.md) | Método de Newton | `newton_method` | Newton en optimización: usa curvatura, converge en un paso si es cuadrática. |
| [253](part-12-optimizacion-matematica-y-computacional/253-quasi-newton-y-bfgs/README.md) | Quasi-Newton y BFGS | `quasi_newton` | BFGS: aproxima el Hessiano inverso solo con gradientes. |
| [254](part-12-optimizacion-matematica-y-computacional/254-line-search/README.md) | Line search | `line_search` | Búsqueda de línea con la condición de Armijo. |
| [255](part-12-optimizacion-matematica-y-computacional/255-regularizacion-como-optimizacion/README.md) | Regularización como optimización | `regularization_as_optimization` | Regularizar es cambiar el objetivo, no el algoritmo. |
| [256](part-12-optimizacion-matematica-y-computacional/256-restricciones-y-lagrangianos/README.md) | Restricciones y Lagrangianos | `constraints_lagrangian` | Restricción de igualdad resuelta con el Lagrangiano. |
| [257](part-12-optimizacion-matematica-y-computacional/257-condiciones-kkt/README.md) | Condiciones KKT | `kkt_conditions` | KKT: restricciones de desigualdad activas e inactivas. |
| [258](part-12-optimizacion-matematica-y-computacional/258-optimizacion-cuadratica/README.md) | Optimización cuadrática | `quadratic_programming` | Programa cuadrático resuelto por su sistema KKT. |
| [259](part-12-optimizacion-matematica-y-computacional/259-optimizacion-evolutiva/README.md) | Optimización evolutiva | `evolutionary_optimization` | Optimización evolutiva: sin gradiente, sobre una función multimodal. |
| [260](part-12-optimizacion-matematica-y-computacional/260-capstone-banco-de-optimizadores-comparables/README.md) | Capstone: banco de optimizadores comparables | `capstone_optimizer_bench` | Capstone: banco comparable de optimizadores con presupuesto idéntico. |
### Parte 13 — [Teoría de la información, señales y series](part-13-teoria-de-la-informacion-senales-y-series/README.md)

*Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [261](part-13-teoria-de-la-informacion-senales-y-series/261-informacion-y-sorpresa/README.md) | Información y sorpresa | `surprise` | La sorpresa de un evento es -log de su probabilidad. |
| [262](part-13-teoria-de-la-informacion-senales-y-series/262-entropia-de-shannon/README.md) | Entropía de Shannon | `shannon_entropy` | La entropía es la sorpresa esperada y el límite de compresión. |
| [263](part-13-teoria-de-la-informacion-senales-y-series/263-entropia-cruzada/README.md) | Entropía cruzada | `cross_entropy` | Entropía cruzada: el coste de codificar p con un código para q. |
| [264](part-13-teoria-de-la-informacion-senales-y-series/264-divergencia-kl/README.md) | Divergencia KL | `kl_divergence` | KL: no simétrica y no es una distancia. |
| [265](part-13-teoria-de-la-informacion-senales-y-series/265-jensen-shannon-divergence/README.md) | Jensen-Shannon divergence | `js_divergence` | Jensen-Shannon: simétrica y acotada. |
| [266](part-13-teoria-de-la-informacion-senales-y-series/266-informacion-mutua/README.md) | Información mutua | `mutual_information` | Información mutua: cuánto reduce Y la incertidumbre de X. |
| [267](part-13-teoria-de-la-informacion-senales-y-series/267-principio-de-maxima-entropia/README.md) | Principio de máxima entropía | `max_entropy` | Principio de máxima entropía: la distribución menos comprometida. |
| [268](part-13-teoria-de-la-informacion-senales-y-series/268-codificacion-y-compresion/README.md) | Codificación y compresión | `coding_compression` | Código de Huffman frente a codificación de longitud fija. |
| [269](part-13-teoria-de-la-informacion-senales-y-series/269-senales-discretas-y-continuas/README.md) | Señales discretas y continuas | `signals` | Señal continua muestreada: amplitud, frecuencia y fase. |
| [270](part-13-teoria-de-la-informacion-senales-y-series/270-muestreo-y-aliasing/README.md) | Muestreo y aliasing | `sampling_aliasing` | Nyquist: muestrear por debajo del límite crea una señal falsa. |
| [271](part-13-teoria-de-la-informacion-senales-y-series/271-convolucion/README.md) | Convolución | `convolution` | Convolución discreta: el operador de las CNN. |
| [272](part-13-teoria-de-la-informacion-senales-y-series/272-correlacion-de-senales/README.md) | Correlación de señales | `cross_correlation` | Correlación cruzada: convolución sin invertir el kernel. |
| [273](part-13-teoria-de-la-informacion-senales-y-series/273-series-y-transformada-de-fourier/README.md) | Series y transformada de Fourier | `fourier_series` | Descomponer una señal en senos y cosenos. |
| [274](part-13-teoria-de-la-informacion-senales-y-series/274-fft/README.md) | FFT | `fft` | FFT frente a DFT: mismo resultado, coste muy distinto. |
| [275](part-13-teoria-de-la-informacion-senales-y-series/275-filtros-y-respuesta-en-frecuencia/README.md) | Filtros y respuesta en frecuencia | `filters` | Filtro paso-bajo aplicado a una señal con ruido de alta frecuencia. |
| [276](part-13-teoria-de-la-informacion-senales-y-series/276-procesos-estacionarios/README.md) | Procesos estacionarios | `stationarity` | Serie estacionaria frente a serie con tendencia. |
| [277](part-13-teoria-de-la-informacion-senales-y-series/277-autocorrelacion/README.md) | Autocorrelación | `autocorrelation` | Autocorrelación revela la periodicidad oculta. |
| [278](part-13-teoria-de-la-informacion-senales-y-series/278-series-temporales-y-ventanas/README.md) | Series temporales y ventanas | `windowing` | Ventaneo: el precio de analizar un trozo finito de señal. |
| [279](part-13-teoria-de-la-informacion-senales-y-series/279-espectro-y-densidad-espectral/README.md) | Espectro y densidad espectral | `power_spectrum` | Densidad espectral de potencia y reparto de la energía. |
| [280](part-13-teoria-de-la-informacion-senales-y-series/280-capstone-analizar-senal-y-construir-features/README.md) | Capstone: analizar señal y construir features | `capstone_signal_features` | Capstone: de una señal cruda a un vector de características. |
### Parte 14 — [Matemática de Machine Learning](part-14-matematica-de-machine-learning/README.md)

*Derivación matemática de los algoritmos clásicos: regresión, regularización, clasificación, kernels, árboles, ensambles, clustering, EM y compromiso sesgo-varianza.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [281](part-14-matematica-de-machine-learning/281-geometria-del-aprendizaje-supervisado/README.md) | Geometría del aprendizaje supervisado | `supervised_geometry` | Aprendizaje supervisado como búsqueda de una frontera en el espacio. |
| [282](part-14-matematica-de-machine-learning/282-regresion-lineal-desde-minimos-cuadrados/README.md) | Regresión lineal desde mínimos cuadrados | `linear_regression` | Regresión lineal: solución cerrada y descenso de gradiente. |
| [283](part-14-matematica-de-machine-learning/283-ridge-y-regularizacion-l2/README.md) | Ridge y regularización L2 | `ridge` | Ridge: L2 encoge los coeficientes y estabiliza el mal condicionamiento. |
| [284](part-14-matematica-de-machine-learning/284-lasso-y-regularizacion-l1/README.md) | Lasso y regularización L1 | `lasso` | Lasso: L1 produce ceros exactos gracias a su geometría. |
| [285](part-14-matematica-de-machine-learning/285-regresion-logistica-y-sigmoid/README.md) | Regresión logística y sigmoid | `logistic_regression` | Regresión logística derivada desde la log-verosimilitud. |
| [286](part-14-matematica-de-machine-learning/286-cross-entropy-en-clasificacion/README.md) | Cross-entropy en clasificación | `classification_loss` | Cross-entropy penaliza la confianza equivocada de forma no acotada. |
| [287](part-14-matematica-de-machine-learning/287-naive-bayes/README.md) | Naive Bayes | `naive_bayes` | Naive Bayes gaussiano: independencia condicional como supuesto explícito. |
| [288](part-14-matematica-de-machine-learning/288-k-nearest-neighbors-y-metricas/README.md) | k-Nearest Neighbors y métricas | `knn` | k-NN: la métrica y el escalado deciden el resultado. |
| [289](part-14-matematica-de-machine-learning/289-svm-y-margen-maximo/README.md) | SVM y margen máximo | `svm_margin` | SVM: maximizar el margen equivale a minimizar ‖w‖. |
| [290](part-14-matematica-de-machine-learning/290-kernel-trick/README.md) | Kernel trick | `kernel_trick` | El kernel calcula el producto punto sin construir el espacio. |
| [291](part-14-matematica-de-machine-learning/291-arboles-entropia-y-gini/README.md) | Árboles: entropía y Gini | `tree_impurity` | Entropía y Gini: dos medidas de impureza para elegir el corte. |
| [292](part-14-matematica-de-machine-learning/292-random-forest-desde-probabilidad/README.md) | Random Forest desde probabilidad | `random_forest` | Bagging: promediar modelos decorrelacionados reduce la varianza. |
| [293](part-14-matematica-de-machine-learning/293-boosting-y-descenso-funcional/README.md) | Boosting y descenso funcional | `boosting` | Boosting: cada modelo corrige el residuo del anterior (descenso funcional). |
| [294](part-14-matematica-de-machine-learning/294-k-means-como-optimizacion/README.md) | k-means como optimización | `kmeans` | k-means como minimización de la inercia (Lloyd). |
| [295](part-14-matematica-de-machine-learning/295-gaussian-mixture-models/README.md) | Gaussian Mixture Models | `gmm` | Mezcla de gaussianas: asignación blanda en lugar de dura. |
| [296](part-14-matematica-de-machine-learning/296-em-algorithm/README.md) | EM algorithm | `em_algorithm` | EM: E-step y M-step sobre datos con una variable latente. |
| [297](part-14-matematica-de-machine-learning/297-pca-aplicado-a-ml/README.md) | PCA aplicado a ML | `pca_ml` | PCA como preprocesamiento: cuánta varianza se conserva. |
| [298](part-14-matematica-de-machine-learning/298-bias-variance-tradeoff/README.md) | Bias-variance tradeoff | `bias_variance` | Descomposición sesgo-varianza medida por simulación. |
| [299](part-14-matematica-de-machine-learning/299-generalizacion-validacion-y-leakage/README.md) | Generalización, validación y leakage | `generalization` | Validación honesta frente a leakage: la misma métrica, dos verdades. |
| [300](part-14-matematica-de-machine-learning/300-capstone-derivar-y-comparar-6-algoritmos-ml/README.md) | Capstone: derivar y comparar 6 algoritmos ML | `capstone_six_algorithms` | Capstone: seis algoritmos derivados y comparados sobre los mismos datos. |
### Parte 15 — [Matemática de Deep Learning](part-15-matematica-de-deep-learning/README.md)

*Perceptrón, MLP, activaciones, pérdidas, backpropagation paso a paso, grafos de cómputo, inicialización, normalización, convolución, recurrencia y embeddings.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [301](part-15-matematica-de-deep-learning/301-perceptron-y-separabilidad/README.md) | Perceptrón y separabilidad | `perceptron` | Perceptrón: converge si y solo si los datos son linealmente separables. |
| [302](part-15-matematica-de-deep-learning/302-mlp-como-composicion-de-funciones/README.md) | MLP como composición de funciones | `mlp` | MLP resolviendo XOR: la capa oculta crea una representación separable. |
| [303](part-15-matematica-de-deep-learning/303-funciones-de-activacion/README.md) | Funciones de activación | `activations` | Activaciones y sus derivadas: dónde se saturan. |
| [304](part-15-matematica-de-deep-learning/304-funciones-de-perdida/README.md) | Funciones de pérdida | `loss_functions` | MSE, MAE, Huber y cross-entropy frente a un valor atípico. |
| [305](part-15-matematica-de-deep-learning/305-backpropagation-paso-a-paso/README.md) | Backpropagation paso a paso | `backpropagation` | Backpropagation paso a paso sobre una red 2-2-1. |
| [306](part-15-matematica-de-deep-learning/306-computational-graphs/README.md) | Computational graphs | `computational_graphs` | El grafo de cómputo y la acumulación de gradientes en nodos reutilizados. |
| [307](part-15-matematica-de-deep-learning/307-inicializacion-de-pesos/README.md) | Inicialización de pesos | `weight_initialization` | Xavier y He: controlar la varianza de las activaciones capa a capa. |
| [308](part-15-matematica-de-deep-learning/308-batch-normalization-y-layer-normalization/README.md) | Batch normalization y layer normalization | `normalization` | Batch norm y layer norm: qué eje se normaliza. |
| [309](part-15-matematica-de-deep-learning/309-regularizacion-y-dropout/README.md) | Regularización y dropout | `dropout_regularization` | Dropout: ruido en entrenamiento, escalado coherente en inferencia. |
| [310](part-15-matematica-de-deep-learning/310-convolucion-discreta/README.md) | Convolución discreta | `discrete_convolution` | Convolución 2D con padding y stride: el cálculo de la forma de salida. |
| [311](part-15-matematica-de-deep-learning/311-cnn-y-receptive-fields/README.md) | CNN y receptive fields | `cnn_receptive_fields` | Campo receptivo: cómo crece al apilar capas. |
| [312](part-15-matematica-de-deep-learning/312-pooling-y-downsampling/README.md) | Pooling y downsampling | `pooling` | Max y average pooling: reducción con y sin pérdida de posición. |
| [313](part-15-matematica-de-deep-learning/313-rnn-y-recurrencia/README.md) | RNN y recurrencia | `rnn` | RNN: el estado oculto acumula historia con pesos compartidos. |
| [314](part-15-matematica-de-deep-learning/314-vanishing-y-exploding-gradients/README.md) | Vanishing y exploding gradients | `vanishing_exploding` | Gradientes que se desvanecen o explotan: un producto de derivadas. |
| [315](part-15-matematica-de-deep-learning/315-lstm-y-compuertas/README.md) | LSTM y compuertas | `lstm` | LSTM: la celda mantiene un camino aditivo para el gradiente. |
| [316](part-15-matematica-de-deep-learning/316-gru/README.md) | GRU | `gru` | GRU: dos puertas en lugar de tres, menos parámetros. |
| [317](part-15-matematica-de-deep-learning/317-embeddings-como-espacios-vectoriales/README.md) | Embeddings como espacios vectoriales | `embeddings` | Embeddings: geometría del significado y similitud coseno. |
| [318](part-15-matematica-de-deep-learning/318-optimizacion-de-redes-profundas/README.md) | Optimización de redes profundas | `deep_optimization` | Entrenar una red profunda: learning rate, warmup y clipping. |
| [319](part-15-matematica-de-deep-learning/319-autodiff-con-pytorch-jax/README.md) | Autodiff con PyTorch/JAX | `autodiff_frameworks` | Nuestro Var frente a PyTorch/JAX: mismo principio, distinta escala. |
| [320](part-15-matematica-de-deep-learning/320-capstone-red-neuronal-desde-cero-en-python-puro/README.md) | Capstone: red neuronal desde cero en Python puro | `capstone_neural_network` | Capstone: red neuronal completa desde cero, entrenada y evaluada. |
### Parte 16 — [Matemática de Transformers, modelos generativos, grafos y RL](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/README.md)

*Softmax, embeddings, positional encoding, atención escalada, multi-head, Transformer completo, muestreo, VAE, GAN, difusión, GNN y ecuaciones de Bellman.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [321](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/321-softmax-y-distribuciones-categoricas/README.md) | Softmax y distribuciones categóricas | `softmax_distributions` | Softmax: de logits arbitrarios a una distribución categórica. |
| [322](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/322-embeddings-y-similitud-coseno/README.md) | Embeddings y similitud coseno | `cosine_similarity` | Similitud coseno: la métrica estándar entre embeddings. |
| [323](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/323-positional-encoding/README.md) | Positional encoding | `positional_encoding` | Positional encoding sinusoidal: posición sin parámetros aprendidos. |
| [324](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/324-query-key-y-value/README.md) | Query, Key y Value | `query_key_value` | Q, K, V: tres proyecciones distintas del mismo token. |
| [325](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/325-scaled-dot-product-attention/README.md) | Scaled dot-product attention | `scaled_dot_product_attention` | Atención escalada: por qué existe el 1/√d. |
| [326](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/326-self-attention/README.md) | Self-attention | `self_attention` | Self-attention completa sobre una secuencia de 4 tokens. |
| [327](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/327-multi-head-attention/README.md) | Multi-head attention | `multi_head_attention` | Multi-head: varias atenciones en subespacios distintos. |
| [328](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/328-transformer-completo/README.md) | Transformer completo | `transformer_block` | Bloque Transformer: atención, residual, layer norm y feed-forward. |
| [329](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/329-modelado-autoregresivo/README.md) | Modelado autoregresivo | `autoregressive_modeling` | Modelado autoregresivo: la regla de la cadena de la probabilidad. |
| [330](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/330-sampling-temperatura-top-k-y-top-p/README.md) | Sampling, temperatura, top-k y top-p | `sampling_strategies` | Temperatura, top-k y top-p reescriben la distribución antes de muestrear. |
| [331](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/331-variational-autoencoders/README.md) | Variational Autoencoders | `variational_autoencoder` | VAE: reparametrización y el término KL en forma cerrada. |
| [332](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/332-elbo-y-variational-inference/README.md) | ELBO y variational inference | `elbo` | ELBO: reconstrucción menos KL, y su relación con la log-verosimilitud. |
| [333](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/333-gan-y-juegos-minimax/README.md) | GAN y juegos minimax | `gan_minimax` | GAN: el equilibrio del juego minimax y su punto óptimo. |
| [334](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/334-diffusion-models-forward-process/README.md) | Diffusion models: forward process | `diffusion_forward` | Proceso directo de difusión: ruido añadido con horario fijo. |
| [335](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/335-diffusion-models-reverse-process/README.md) | Diffusion models: reverse process | `diffusion_reverse` | Proceso inverso: la red predice el ruido y se reconstruye x₀. |
| [336](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/336-graph-laplacian/README.md) | Graph Laplacian | `graph_laplacian` | Laplaciano del grafo: espectro y componentes conexas. |
| [337](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/337-message-passing-en-gnn/README.md) | Message passing en GNN | `message_passing` | Message passing: cada capa agrega información de un salto más lejos. |
| [338](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/338-bellman-equations/README.md) | Bellman equations | `bellman_equations` | Iteración de valor sobre un MDP pequeño. |
| [339](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/339-policy-gradients/README.md) | Policy gradients | `policy_gradients` | REINFORCE: gradiente de la política sobre un bandido de 3 brazos. |
| [340](part-16-matematica-de-transformers-modelos-generativos-grafos-y-rl/340-capstone-mini-transformer-matematico/README.md) | Capstone: mini-Transformer matemático | `capstone_mini_transformer` | Capstone: mini-Transformer que aprende a copiar el token anterior. |
### Parte 17 — [Frontera matemática para IA e investigación](part-17-frontera-matematica-para-ia-e-investigacion/README.md)

*Procesos gaussianos, MCMC avanzado, inferencia variacional, transporte óptimo, geometría diferencial e informacional, SDE, Neural ODE, score matching y teoría del aprendizaje.*

| # | Clase | Demostración | Qué ejecuta |
|---|---|---|---|
| [341](part-17-frontera-matematica-para-ia-e-investigacion/341-gaussian-processes/README.md) | Gaussian Processes | `gaussian_processes` | GP: distribución sobre funciones, con media y varianza posterior. |
| [342](part-17-frontera-matematica-para-ia-e-investigacion/342-kernel-methods-avanzados/README.md) | Kernel methods avanzados | `advanced_kernels` | Familias de kernels y la condición de Mercer. |
| [343](part-17-frontera-matematica-para-ia-e-investigacion/343-mcmc-avanzado/README.md) | MCMC avanzado | `advanced_mcmc` | Metropolis-Hastings con diagnóstico de aceptación y autocorrelación. |
| [344](part-17-frontera-matematica-para-ia-e-investigacion/344-hamiltonian-monte-carlo/README.md) | Hamiltonian Monte Carlo | `hamiltonian_monte_carlo` | HMC: usar el gradiente para proponer estados lejanos con alta aceptación. |
| [345](part-17-frontera-matematica-para-ia-e-investigacion/345-variational-inference-avanzada/README.md) | Variational inference avanzada | `advanced_variational_inference` | Inferencia variacional: optimizar en lugar de muestrear. |
| [346](part-17-frontera-matematica-para-ia-e-investigacion/346-optimal-transport/README.md) | Optimal transport | `optimal_transport` | Transporte óptimo por Sinkhorn: coste de mover una distribución a otra. |
| [347](part-17-frontera-matematica-para-ia-e-investigacion/347-wasserstein-distance/README.md) | Wasserstein distance | `wasserstein_distance` | Wasserstein-1 en 1D: comparar distribuciones sin soporte común. |
| [348](part-17-frontera-matematica-para-ia-e-investigacion/348-manifold-learning/README.md) | Manifold learning | `manifold_learning` | Variedad: dimensión intrínseca menor que la del espacio ambiente. |
| [349](part-17-frontera-matematica-para-ia-e-investigacion/349-geometria-diferencial-para-ml/README.md) | Geometría diferencial para ML | `differential_geometry` | Geometría diferencial: métrica, longitud de curva y curvatura. |
| [350](part-17-frontera-matematica-para-ia-e-investigacion/350-information-geometry/README.md) | Information geometry | `information_geometry` | Información de Fisher: la métrica natural del espacio de parámetros. |
| [351](part-17-frontera-matematica-para-ia-e-investigacion/351-stochastic-differential-equations/README.md) | Stochastic differential equations | `stochastic_differential_equations` | SDE: proceso de Ornstein-Uhlenbeck simulado con Euler-Maruyama. |
| [352](part-17-frontera-matematica-para-ia-e-investigacion/352-neural-odes/README.md) | Neural ODEs | `neural_odes` | Neural ODE: capas continuas y el método adjunto. |
| [353](part-17-frontera-matematica-para-ia-e-investigacion/353-score-matching/README.md) | Score matching | `score_matching` | Score matching: aprender ∇ log p sin conocer la constante de normalización. |
| [354](part-17-frontera-matematica-para-ia-e-investigacion/354-spectral-graph-theory/README.md) | Spectral graph theory | `spectral_graph_theory` | Clustering espectral: el vector de Fiedler separa el grafo. |
| [355](part-17-frontera-matematica-para-ia-e-investigacion/355-causal-inference/README.md) | Causal inference | `causal_inference` | Confusión, ajuste por backdoor y el sesgo de colisionador. |
| [356](part-17-frontera-matematica-para-ia-e-investigacion/356-statistical-learning-theory/README.md) | Statistical learning theory | `statistical_learning_theory` | Riesgo empírico frente a riesgo verdadero y la brecha de generalización. |
| [357](part-17-frontera-matematica-para-ia-e-investigacion/357-vc-dimension/README.md) | VC dimension | `vc_dimension` | Dimensión VC: cuántos puntos puede fragmentar una clase de hipótesis. |
| [358](part-17-frontera-matematica-para-ia-e-investigacion/358-pac-learning/README.md) | PAC learning | `pac_learning` | PAC: cuántas muestras hacen falta para (ε, δ). |
| [359](part-17-frontera-matematica-para-ia-e-investigacion/359-approximation-theory-y-scaling/README.md) | Approximation theory y scaling | `approximation_theory` | Teoría de aproximación y leyes de escala: el error como potencia del tamaño. |
| [360](part-17-frontera-matematica-para-ia-e-investigacion/360-capstone-final-reproducir-una-idea-matematica-de-un-paper/README.md) | Capstone final: reproducir una idea matemática de un paper | `capstone_reproduce_paper_idea` | Capstone: reproducir el núcleo matemático de un resultado publicado. |
