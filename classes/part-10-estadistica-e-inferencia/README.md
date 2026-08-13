# Parte 10 — Estadística e inferencia

**Nivel:** universitario-avanzado
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part10.py`

Descriptiva, muestreo, estimadores, intervalos de confianza, pruebas de hipótesis, p-value, potencia, verosimilitud, MAP, inferencia bayesiana, bootstrap y A/B testing.

## 🧠 Ideas centrales

- El p-value es P(datos tan extremos | H0), nunca P(H0 | datos).
- Un intervalo de confianza describe el procedimiento, no una probabilidad del parámetro.
- Sin potencia declarada, un resultado no significativo no dice nada.
- Correlación no implica causalidad, pero causalidad sí restringe la correlación.
- El bootstrap estima la variabilidad sin suponer la distribución poblacional.

## 🤖 Por qué importa en IA

Evaluar un modelo es inferencia estadística: métricas con intervalo, comparaciones múltiples corregidas y detección de leakage.

## ⚠️ Errores frecuentes

- p-hacking por comparaciones múltiples sin corrección.
- Confundir significancia estadística con relevancia práctica.
- Evaluar sobre datos que participaron en la selección del modelo.

## 🧰 Stack de referencia

`statistics`, `random`, `math`, `scipy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [201 — Estadística descriptiva](201-estadistica-descriptiva/README.md)
2. [202 — Población, muestra y sesgo de selección](202-poblacion-muestra-y-sesgo-de-seleccion/README.md)
3. [203 — Muestreo y distribuciones muestrales](203-muestreo-y-distribuciones-muestrales/README.md)
4. [204 — Estimadores y propiedades](204-estimadores-y-propiedades/README.md)
5. [205 — Intervalos de confianza](205-intervalos-de-confianza/README.md)
6. [206 — Pruebas de hipótesis](206-pruebas-de-hipotesis/README.md)
7. [207 — p-value correctamente interpretado](207-p-value-correctamente-interpretado/README.md)
8. [208 — Errores tipo I y II](208-errores-tipo-i-y-ii/README.md)
9. [209 — Potencia estadística](209-potencia-estadistica/README.md)
10. [210 — t-test y comparación de medias](210-t-test-y-comparacion-de-medias/README.md)
11. [211 — Chi-cuadrado y tablas de contingencia](211-chi-cuadrado-y-tablas-de-contingencia/README.md)
12. [212 — ANOVA](212-anova/README.md)
13. [213 — Correlación frente a causalidad](213-correlacion-frente-a-causalidad/README.md)
14. [214 — Regresión lineal estadística](214-regresion-lineal-estadistica/README.md)
15. [215 — Máxima verosimilitud](215-maxima-verosimilitud/README.md)
16. [216 — Estimación MAP](216-estimacion-map/README.md)
17. [217 — Inferencia bayesiana](217-inferencia-bayesiana/README.md)
18. [218 — Bootstrap y remuestreo](218-bootstrap-y-remuestreo/README.md)
19. [219 — A/B testing y diseño experimental](219-a-b-testing-y-diseno-experimental/README.md)
20. [220 — Capstone: estudio estadístico reproducible](220-capstone-estudio-estadistico-reproducible/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 10
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Wasserman, L. *All of Statistics*. Springer, 2004.
- Gelman, A. et al. *Bayesian Data Analysis*. 3ª ed., CRC, 2013.
- Efron, B.; Tibshirani, R. *An Introduction to the Bootstrap*. Chapman & Hall, 1993.
