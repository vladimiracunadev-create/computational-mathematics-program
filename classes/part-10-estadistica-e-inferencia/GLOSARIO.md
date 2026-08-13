# 📖 Glosario — Parte 10: Estadística e inferencia

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

36 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Aleatorización** | Asignar el tratamiento al azar para romper la influencia de confusores conocidos y desconocidos. | [213](213-correlacion-frente-a-causalidad/README.md) |
| **ANOVA** | Compara varias medias descomponiendo la variabilidad entre grupos y dentro de ellos. | [212](212-anova/README.md) |
| **Asimetría** | Sesgo de la distribución. Con cola derecha la media supera a la mediana. | [201](201-estadistica-descriptiva/README.md) |
| **Bootstrap** | Remuestrear con reposición los propios datos para estimar la variabilidad de un estadístico. | [218](218-bootstrap-y-remuestreo/README.md) |
| **Chi-cuadrado** | Contraste que compara frecuencias observadas con esperadas en una tabla. | [211](211-chi-cuadrado-y-tablas-de-contingencia/README.md) |
| **Coeficiente de determinación** | R². Proporción de la variabilidad explicada por el modelo. Un R² alto no valida el modelo. | [214](214-regresion-lineal-estadistica/README.md) |
| **Comparaciones múltiples** | Al hacer k contrastes, la probabilidad de algún falso positivo crece; exige corrección. | [212](212-anova/README.md) |
| **Consistencia** | El estimador converge al parámetro cuando n crece. Es una garantía asintótica. | [204](204-estimadores-y-propiedades/README.md) |
| **Distribución muestral** | Distribución de un estadístico al repetir el muestreo. Es el objeto que hace posible inferir. | [203](203-muestreo-y-distribuciones-muestrales/README.md) |
| **Error estándar** | Desviación típica de un estimador. Para la media vale σ/√n. | [203](203-muestreo-y-distribuciones-muestrales/README.md) |
| **Error tipo I** | Rechazar una H0 verdadera. Su tasa es α, elegida de antemano. | [208](208-errores-tipo-i-y-ii/README.md) |
| **Error tipo II** | No rechazar una H0 falsa. Su tasa es β y depende del tamaño del efecto y de n. | [208](208-errores-tipo-i-y-ii/README.md) |
| **Estadístico de contraste** | Número calculado de la muestra cuya distribución bajo H0 se conoce. | [206](206-pruebas-de-hipotesis/README.md) |
| **Estimación MAP** | Máximo de la posterior: verosimilitud por prior. El prior actúa como regularización. | [216](216-estimacion-map/README.md) |
| **Estimador insesgado** | Aquel cuya esperanza coincide con el parámetro. No implica que sea bueno. | [204](204-estimadores-y-propiedades/README.md) |
| **Grados de libertad** | Número de valores libres tras imponer las restricciones del modelo. | [210](210-t-test-y-comparacion-de-medias/README.md) |
| **Hipótesis nula** | Enunciado de ausencia de efecto que se somete a prueba. Nunca se acepta, solo se rechaza o no. | [206](206-pruebas-de-hipotesis/README.md) |
| **Intervalo creíble** | Región que contiene el parámetro con probabilidad dada bajo la posterior. Sí es una probabilidad del parámetro. | [217](217-inferencia-bayesiana/README.md) |
| **Intervalo de confianza** | Procedimiento que, repetido, contiene el parámetro en el 95 % de los casos. No es una probabilidad del parámetro. | [205](205-intervalos-de-confianza/README.md) |
| **Lift** | Mejora relativa de la variante frente al control en un experimento. | [219](219-a-b-testing-y-diseno-experimental/README.md) |
| **Log-verosimilitud** | Logaritmo de la verosimilitud. Convierte productos en sumas y evita el subdesbordamiento. | [215](215-maxima-verosimilitud/README.md) |
| **Media, mediana y moda** | Tres medidas de centro. La mediana resiste valores extremos; la media no. | [201](201-estadistica-descriptiva/README.md) |
| **Máxima verosimilitud** | Elegir el parámetro que hace más probables los datos observados. | [215](215-maxima-verosimilitud/README.md) |
| **p-hacking** | Probar variantes de análisis hasta obtener p < 0,05. Invalida el significado del p-value. | [207](207-p-value-correctamente-interpretado/README.md) |
| **p-value** | P(estadístico tan o más extremo | H0 cierta). Nunca es P(H0 | datos). | [207](207-p-value-correctamente-interpretado/README.md) |
| **Potencia** | 1 − β. Probabilidad de detectar un efecto real. Sin ella, un no significativo no informa. | [209](209-potencia-estadistica/README.md) |
| **Preinscripción del análisis** | Fijar hipótesis, métrica y tamaño muestral antes de recoger datos. Bloquea el p-hacking. | [220](220-capstone-estudio-estadistico-reproducible/README.md) |
| **Prior conjugado** | Prior cuya posterior pertenece a la misma familia. Beta es conjugado de la binomial. | [217](217-inferencia-bayesiana/README.md) |
| **Rango intercuartílico** | Q3 − Q1. Dispersión robusta que ignora el 25 % de cada cola. | [201](201-estadistica-descriptiva/README.md) |
| **Residuo** | Diferencia entre valor observado y predicho. Su patrón revela los fallos del modelo. | [214](214-regresion-lineal-estadistica/README.md) |
| **Sesgo de selección** | La muestra no representa a la población. No se corrige aumentando el tamaño. | [202](202-poblacion-muestra-y-sesgo-de-seleccion/README.md) |
| **Sesgo del superviviente** | Analizar solo los casos que llegaron al final, ignorando los que desaparecieron. | [202](202-poblacion-muestra-y-sesgo-de-seleccion/README.md) |
| **t de Student** | Contraste de medias con varianza desconocida. Sus colas son más pesadas que las de la normal. | [210](210-t-test-y-comparacion-de-medias/README.md) |
| **Tabla de contingencia** | Recuento cruzado de dos variables categóricas. | [211](211-chi-cuadrado-y-tablas-de-contingencia/README.md) |
| **Tamaño del efecto** | Magnitud de la diferencia en unidades de desviación, como la d de Cohen. Independiente de n. | [209](209-potencia-estadistica/README.md) |
| **Variable de confusión** | Causa común de dos variables que genera correlación sin relación causal directa. | [213](213-correlacion-frente-a-causalidad/README.md) |

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
