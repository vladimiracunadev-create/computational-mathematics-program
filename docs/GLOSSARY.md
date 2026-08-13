# Glosario

Vocabulario preciso del programa. Cada entrada indica la clase donde se estudia y, cuando
existe, la confusión que suele acompañarla.

## Representación numérica

**Punto flotante (float64)** — racional binario de precisión finita, no un número real.
Clase 028.

**ULP (*unit in the last place*)** — distancia entre un float y su vecino. Depende de la
magnitud: `ulp(1.0)` y `ulp(1e6)` no son iguales. Clase 031.

**Machine epsilon** — el menor `ε` tal que `1.0 + ε != 1.0`. En float64, `2⁻⁵²`. Clase 031.
*No confundir con* el menor número representable.

**Error absoluto** — `|aproximado − exacto|`. Depende de la escala. Clase 030.

**Error relativo** — `|aproximado − exacto| / |exacto|`. Es el que se propaga. Clase 030.

**Cancelación catastrófica** — pérdida de dígitos significativos al restar dos números
casi iguales. No lanza excepción. Clase 032.

**Condicionamiento** — sensibilidad **del problema** a perturbaciones de la entrada.
Clase 035.

**Estabilidad** — sensibilidad **del algoritmo** a errores de redondeo. Clase 036.
*Un problema mal condicionado no tiene algoritmo estable que lo salve.*

## Álgebra lineal

**Rango** — dimensión efectiva de la salida de una transformación, no el tamaño de la
tabla. Clase 115.

**Span** — conjunto de todas las combinaciones lineales de unos vectores. Clase 108.

**Norma** — medida de magnitud. L1 induce dispersión, L2 penaliza los valores grandes,
L∞ mira solo el máximo. Clase 104.

**Autovalor / autovector** — dirección que la transformación solo escala, y su factor de
escala. Clase 125.

**Matriz definida positiva** — todos sus autovalores son positivos; `xᵀAx > 0` para todo
`x ≠ 0`. Clase 127.

**Número de condición** — cociente entre el mayor y el menor valor singular. Cuantifica
cuánto amplifica el error una matriz. Clase 132.

**SVD** — descomposición `A = UΣVᵀ` que existe para **toda** matriz, incluso rectangular
y singular. Clase 132.

**Pseudoinversa** — generalización de la inversa a matrices no cuadradas o singulares.
Clase 134.

## Cálculo

**Derivada** — mejor aproximación lineal local, no solo una pendiente. Clase 144.

**Regla de la cadena** — mecanismo entero de backpropagation. Clase 147.

**Gradiente** — vector de derivadas parciales; apunta al mayor ascenso. Clase 164.

**Derivada direccional** — proyección del gradiente sobre una dirección unitaria. Clase 165.

**Jacobiano** — matriz de primeras derivadas de una función vectorial. Clase 168.

**Hessiano** — matriz de segundas derivadas; describe la curvatura. Clase 169.

**Autodiferenciación (modo reverso)** — calcula todas las derivadas en un solo barrido
hacia atrás sobre el grafo de cómputo. Clase 179. *No es diferenciación numérica ni
simbólica.*

**Punto crítico** — donde el gradiente se anula. Puede ser mínimo, máximo o silla.
Clase 152.

## Probabilidad y estadística

**Probabilidad condicional** — `P(A|B)`. **Nunca** es intercambiable con `P(B|A)`.
Clase 184.

**Independencia** — `P(A∩B) = P(A)·P(B)`. Se comprueba, no se supone. Clase 185.

**Esperanza** — es lineal siempre, incluso sin independencia. Clase 189.

**Varianza** — solo es aditiva bajo independencia. Clase 190.

**Verosimilitud (*likelihood*)** — compatibilidad de un parámetro con los datos
observados. **No** es la probabilidad del parámetro. Clase 215.

**MLE / MAP** — máxima verosimilitud / máximo a posteriori. MAP con prior uniforme es MLE.
Clases 215, 216.

**p-value** — `P(estadístico tan o más extremo | H₀ cierta)`. **No** es `P(H₀ | datos)`.
Clase 207.

**Intervalo de confianza** — propiedad del **procedimiento**: el 95 % de los intervalos
así construidos contienen el parámetro. No es una probabilidad sobre este intervalo
concreto. Clase 205.

**Potencia estadística** — `1 − β`: probabilidad de detectar un efecto que existe. Sin
ella declarada, un resultado no significativo no dice nada. Clase 209.

**Bootstrap** — estimar la variabilidad remuestreando, sin suponer la distribución
poblacional. Clase 218.

**Leakage** — información del conjunto de evaluación que se filtró al ajuste. Produce
métricas excelentes y modelos inútiles. Clase 299.

## Información y señales

**Entropía** — sorpresa esperada; límite inferior de compresión sin pérdida. Clase 262.

**Entropía cruzada** — coste de codificar `p` usando un código óptimo para `q`.
Minimizarla equivale a maximizar la verosimilitud. Clase 263.

**Divergencia KL** — `H(p,q) − H(p)`. No es simétrica ni cumple la desigualdad triangular:
**no es una distancia**. Clase 264.

**Información mutua** — cuánto reduce una variable la incertidumbre de otra. Detecta
relaciones no lineales que la correlación de Pearson no ve. Clase 266.

**Nyquist** — frecuencia mínima de muestreo. Por debajo, el aliasing es irreversible.
Clase 270.

**Convolución** — en el tiempo equivale a multiplicación en frecuencia. Clase 271.

## Optimización

**Función objetivo** — lo que se minimiza. Regularizar es cambiarla, no cambiar el
algoritmo. Clase 241.

**Convexidad** — todo mínimo local es global. Fuera de ella no hay garantía. Clase 242.

**Learning rate** — el hiperparámetro que más veces explica una divergencia. Estable si
`lr < 2/L`, con `L` el mayor autovalor del Hessiano. Clase 244.

**Momentum** — promedia gradientes. **Adam** además normaliza por su escala. Clases 246, 250.

**AdamW** — desacopla el weight decay del gradiente adaptativo. No es lo mismo que Adam
con L2 en el gradiente. Clase 251.

**KKT** — generaliza los multiplicadores de Lagrange a restricciones de desigualdad.
Clase 257.

## Machine Learning y Deep Learning

**Embedding** — representación vectorial densa aprendida de un objeto discreto. Clase 317.

**Similitud coseno** — producto punto normalizado. Invariante a la escala, a diferencia de
la distancia euclídea. Clase 322.

**Softmax** — convierte logits en una distribución categórica. Hay que restar el máximo
para no desbordar. Clase 321.

**Atención** — promedio ponderado de valores, con pesos dados por la similitud
consulta-clave y normalizados con softmax. Clase 325.

**Escala 1/√d** — normaliza la varianza del producto punto para que softmax no sature en
alta dimensión. Clase 325.

**Máscara causal** — impide que una posición atienda al futuro. Sin ella, el modelado
autoregresivo no aprende nada útil. Clase 326.

**Sesgo-varianza** — descomposición del error esperado en sesgo², varianza y ruido
irreducible. Clase 298.

**Gradiente que se desvanece** — producto de muchas derivadas menores que uno. Clase 314.

**ELBO** — cota inferior de la log-verosimilitud: reconstrucción menos KL. Clase 332.

**Score** — `∇ₓ log p(x)`. No requiere la constante de normalización. Clase 353.

## Frontera

**Proceso gaussiano** — distribución sobre **funciones**, no sobre parámetros. Clase 341.

**HMC** — MCMC que usa gradientes y un integrador simpléctico para proponer estados
lejanos con alta aceptación. Clase 344.

**Distancia de Wasserstein** — compara distribuciones aunque sus soportes sean disjuntos,
donde la KL deja de informar. Clase 347.

**Geometría de la información** — dota al espacio de parámetros de una métrica (Fisher);
fundamenta el gradiente natural. Clase 350.

**Dimensión VC** — número máximo de puntos que una clase de hipótesis puede fragmentar.
Clase 357.

**PAC** — *probably approximately correct*: cota del error con probabilidad `1 − δ`.
Muy holgada para redes profundas. Clase 358.

## Términos del propio repositorio

**Motor** — módulo `engines/partNN.py` con las 20 demostraciones ejecutables de una parte.

**Demostración (*demo*)** — función sin argumentos, determinista, que devuelve un `dict`
con resultados y comprobaciones de invariante.

**Clave de verificación** — entrada del resultado que comprueba una identidad
(`coinciden`, `es_simetrica`, `residuo`) en lugar de reportar un valor.

**Artefacto derivado** — archivo generado desde `curriculum.yaml` y los motores. Las 360
clases, `catalog.json` y `site/` lo son: editarlos a mano no sobrevive.
