# 📖 Glosario — Parte 14: Matemática de Machine Learning

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

38 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Algoritmo de Lloyd** | Alternar asignación de puntos y recálculo de centroides hasta converger. | [294](294-k-means-como-optimizacion/README.md) |
| **Algoritmo EM** | Alternar expectativa de las latentes y maximización de los parámetros. La verosimilitud nunca baja. | [296](296-em-algorithm/README.md) |
| **Aprendiz débil** | Modelo apenas mejor que el azar. Un tocón de decisión es el ejemplo típico. | [293](293-boosting-y-descenso-funcional/README.md) |
| **Aprendizaje supervisado** | Aprender una función de entrada a salida a partir de pares etiquetados. | [281](281-geometria-del-aprendizaje-supervisado/README.md) |
| **Bagging** | Entrenar modelos sobre remuestras bootstrap y promediar. Reduce la varianza. | [292](292-random-forest-desde-probabilidad/README.md) |
| **Boosting** | Añadir modelos secuencialmente, cada uno ajustando el residuo del conjunto anterior. | [293](293-boosting-y-descenso-funcional/README.md) |
| **Calibración** | Grado en que las probabilidades predichas coinciden con las frecuencias observadas. | [286](286-cross-entropy-en-clasificacion/README.md) |
| **Decorrelación** | Hacer que los modelos del ensemble se equivoquen de formas distintas. Es lo que da la ganancia. | [292](292-random-forest-desde-probabilidad/README.md) |
| **Dirección discriminante** | Dirección que mejor separa los centroides de las clases. | [281](281-geometria-del-aprendizaje-supervisado/README.md) |
| **Dispersión** | Solución con muchos coeficientes nulos. Equivale a selección automática de variables. | [284](284-lasso-y-regularizacion-l1/README.md) |
| **Ecuación normal** | w = (XᵀX)⁻¹Xᵀy. Solución cerrada de la regresión lineal. | [282](282-regresion-lineal-desde-minimos-cuadrados/README.md) |
| **Error irreducible** | Ruido de los datos que ningún modelo puede eliminar. | [298](298-bias-variance-tradeoff/README.md) |
| **Frontera de decisión** | Superficie que separa las regiones asignadas a cada clase. | [281](281-geometria-del-aprendizaje-supervisado/README.md) |
| **Función kernel** | K(a,b) que equivale a φ(a)ᵀφ(b) para alguna transformación φ. | [290](290-kernel-trick/README.md) |
| **Función sigmoide** | σ(z) = 1/(1+e⁻ᶻ). Convierte un número real en una probabilidad. | [285](285-regresion-logistica-y-sigmoid/README.md) |
| **Ganancia de información** | Reducción de impureza que produce un corte. Criterio de división del árbol. | [291](291-arboles-entropia-y-gini/README.md) |
| **Impureza** | Medida de mezcla de clases en un nodo. Entropía y Gini son las habituales. | [291](291-arboles-entropia-y-gini/README.md) |
| **Independencia condicional** | P(x₁,x₂|c) = P(x₁|c)·P(x₂|c). Supuesto falso en la práctica y útil igualmente. | [287](287-naive-bayes/README.md) |
| **Inercia** | Suma de distancias al cuadrado de cada punto a su centroide. Objetivo de k-means. | [294](294-k-means-como-optimizacion/README.md) |
| **k-Nearest Neighbors** | Clasificar por mayoría entre los k vecinos más cercanos. Sin entrenamiento. | [288](288-k-nearest-neighbors-y-metricas/README.md) |
| **Kernel trick** | Calcular productos escalares en un espacio expandido sin construirlo explícitamente. | [290](290-kernel-trick/README.md) |
| **Lasso** | Regresión con penalización L1. Produce coeficientes exactamente cero. | [284](284-lasso-y-regularizacion-l1/README.md) |
| **Leakage** | Información del test que se filtra al entrenamiento. Produce métricas excelentes y modelos inútiles. | [299](299-generalizacion-validacion-y-leakage/README.md) |
| **Logit** | Logaritmo de la razón de probabilidades. Es la inversa de la sigmoide. | [285](285-regresion-logistica-y-sigmoid/README.md) |
| **Maldición de la dimensionalidad** | En dimensión alta todas las distancias se parecen y el concepto de vecino pierde sentido. | [288](288-k-nearest-neighbors-y-metricas/README.md) |
| **Margen** | Distancia entre la frontera y los puntos más cercanos. SVM lo maximiza. | [289](289-svm-y-margen-maximo/README.md) |
| **Mezcla de gaussianas** | Modelo generativo con varias componentes normales y asignación blanda. | [295](295-gaussian-mixture-models/README.md) |
| **Mínimos cuadrados ordinarios** | Minimizar la suma de residuos al cuadrado. Tiene solución cerrada. | [282](282-regresion-lineal-desde-minimos-cuadrados/README.md) |
| **Naive Bayes** | Clasificador que supone independencia condicional de las variables dada la clase. | [287](287-naive-bayes/README.md) |
| **Pérdida logarítmica** | Entropía cruzada aplicada a clasificación. Penaliza sin cota la confianza equivocada. | [286](286-cross-entropy-en-clasificacion/README.md) |
| **Responsabilidad** | Probabilidad de que una componente haya generado un punto concreto. | [295](295-gaussian-mixture-models/README.md) |
| **Ridge** | Regresión con penalización L2. Encoge los coeficientes y estabiliza el mal condicionamiento. | [283](283-ridge-y-regularizacion-l2/README.md) |
| **Sesgo del modelo** | Error por suponer una forma demasiado simple. Un modelo rígido tiene sesgo alto. | [298](298-bias-variance-tradeoff/README.md) |
| **Validación cruzada anidada** | Bucle interno para elegir hiperparámetros y externo para estimar el rendimiento. | [299](299-generalizacion-validacion-y-leakage/README.md) |
| **Variable latente** | Variable no observada que explica la estructura de los datos. | [296](296-em-algorithm/README.md) |
| **Varianza del modelo** | Sensibilidad de la predicción a la muestra concreta de entrenamiento. | [298](298-bias-variance-tradeoff/README.md) |
| **Varianza explicada** | Fracción de la varianza total que capturan las componentes retenidas. | [297](297-pca-aplicado-a-ml/README.md) |
| **Vector de soporte** | Punto que toca el margen y determina la frontera. Los demás no influyen. | [289](289-svm-y-margen-maximo/README.md) |

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
