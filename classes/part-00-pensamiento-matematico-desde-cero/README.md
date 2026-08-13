# Parte 00 — Pensamiento matemático desde cero

**Nivel:** cero-absoluto
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part00.py`

Reconstruye la aritmética y el lenguaje matemático básico con el rigor que exige escribir código: cada número tiene dominio, unidad y representación.

## 🧠 Ideas centrales

- Un número sin unidad ni dominio es una cadena de dígitos, no una cantidad.
- Fracción exacta y decimal aproximado no son el mismo objeto computacional.
- Proporcionalidad es la primera función lineal que aprendemos sin llamarla así.
- Redondear es una decisión de modelado, no un accidente de la calculadora.
- Un contraejemplo derrumba una regla; mil ejemplos favorables no la demuestran.

## 🤖 Por qué importa en IA

Toda métrica de un modelo (accuracy, loss, learning rate) es una razón, un porcentaje o una escala. Interpretarlas mal es el primer error de un practicante de IA.

## ⚠️ Errores frecuentes

- Sumar porcentajes como si fueran cantidades absolutas.
- Confundir aumento del 50 % con multiplicar por 50.
- Escribir 1/3 como 0.33 y arrastrar el error a todo el cálculo.

## 🧰 Stack de referencia

`math`, `fractions`, `decimal`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [001 — Números naturales y conteo](001-numeros-naturales-y-conteo/README.md)
2. [002 — Enteros, signo y recta numérica](002-enteros-signo-y-recta-numerica/README.md)
3. [003 — Fracciones y números racionales](003-fracciones-y-numeros-racionales/README.md)
4. [004 — Decimales y conversiones](004-decimales-y-conversiones/README.md)
5. [005 — Porcentajes desde cero](005-porcentajes-desde-cero/README.md)
6. [006 — Razones, tasas y proporciones](006-razones-tasas-y-proporciones/README.md)
7. [007 — Regla de tres y escalas](007-regla-de-tres-y-escalas/README.md)
8. [008 — Potencias y leyes de exponentes](008-potencias-y-leyes-de-exponentes/README.md)
9. [009 — Raíces y radicales](009-raices-y-radicales/README.md)
10. [010 — Orden de operaciones y paréntesis](010-orden-de-operaciones-y-parentesis/README.md)
11. [011 — Notación científica](011-notacion-cientifica/README.md)
12. [012 — Unidades y análisis dimensional](012-unidades-y-analisis-dimensional/README.md)
13. [013 — Aproximación, redondeo y cifras significativas](013-aproximacion-redondeo-y-cifras-significativas/README.md)
14. [014 — Estimación y cálculo mental](014-estimacion-y-calculo-mental/README.md)
15. [015 — Variables como cantidades desconocidas](015-variables-como-cantidades-desconocidas/README.md)
16. [016 — Expresiones y fórmulas](016-expresiones-y-formulas/README.md)
17. [017 — Patrones, secuencias y regularidades](017-patrones-secuencias-y-regularidades/README.md)
18. [018 — Problemas verbales a lenguaje matemático](018-problemas-verbales-a-lenguaje-matematico/README.md)
19. [019 — Comprobación y contraejemplos](019-comprobacion-y-contraejemplos/README.md)
20. [020 — Capstone: modelar un problema cotidiano con matemáticas](020-capstone-modelar-un-problema-cotidiano-con-matematicas/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 00
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Lang, S. *Basic Mathematics*. Springer, 1988.
- Gelfand, I. M.; Shen, A. *Algebra*. Birkhäuser, 2002.
- Polya, G. *How to Solve It*. Princeton University Press, 1945.
