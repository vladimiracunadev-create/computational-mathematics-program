# Parte 01 — Aritmética computacional y representación numérica

**Nivel:** basico-computacional
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part01.py`

Qué es realmente un número dentro de una máquina: bits, complemento a dos, IEEE 754, error, condicionamiento y estabilidad.

## 🧠 Ideas centrales

- Un float es un racional binario de precisión finita, no un número real.
- El error relativo, no el absoluto, es la magnitud que se propaga.
- Condicionamiento es del problema; estabilidad es del algoritmo.
- La cancelación catastrófica destruye dígitos significativos sin lanzar excepciones.
- Reproducibilidad numérica exige fijar orden de operaciones, no solo semillas.

## 🤖 Por qué importa en IA

float32, bfloat16 y la cuantización a int8 son decisiones de representación. Los NaN en un entrenamiento casi siempre nacen aquí, no en la arquitectura.

## ⚠️ Errores frecuentes

- Comparar floats con `==` en lugar de una tolerancia razonada.
- Suponer que la suma de floats es asociativa.
- Usar float para dinero en vez de Decimal o enteros de centavos.

## 🧰 Stack de referencia

`struct`, `decimal`, `fractions`, `sys.float_info`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [021 — Bits, bytes y sistemas de numeración](021-bits-bytes-y-sistemas-de-numeracion/README.md)
2. [022 — Conversión decimal a binario](022-conversion-decimal-a-binario/README.md)
3. [023 — Binario, octal y hexadecimal](023-binario-octal-y-hexadecimal/README.md)
4. [024 — Aritmética binaria](024-aritmetica-binaria/README.md)
5. [025 — Enteros con signo y complemento a dos](025-enteros-con-signo-y-complemento-a-dos/README.md)
6. [026 — Rango, overflow y wraparound](026-rango-overflow-y-wraparound/README.md)
7. [027 — Punto fijo frente a punto flotante](027-punto-fijo-frente-a-punto-flotante/README.md)
8. [028 — IEEE 754: estructura de un float](028-ieee-754-estructura-de-un-float/README.md)
9. [029 — Por qué 0.1 + 0.2 no es exactamente 0.3](029-por-que-0-1-0-2-no-es-exactamente-0-3/README.md)
10. [030 — Error absoluto y error relativo](030-error-absoluto-y-error-relativo/README.md)
11. [031 — ULP y machine epsilon](031-ulp-y-machine-epsilon/README.md)
12. [032 — Cancelación catastrófica](032-cancelacion-catastrofica/README.md)
13. [033 — Overflow y underflow flotante](033-overflow-y-underflow-flotante/README.md)
14. [034 — Propagación de errores](034-propagacion-de-errores/README.md)
15. [035 — Condicionamiento de problemas](035-condicionamiento-de-problemas/README.md)
16. [036 — Estabilidad de algoritmos](036-estabilidad-de-algoritmos/README.md)
17. [037 — Precisión arbitraria y Decimal](037-precision-arbitraria-y-decimal/README.md)
18. [038 — Racional exacto y Fraction](038-racional-exacto-y-fraction/README.md)
19. [039 — Reproducibilidad numérica entre plataformas](039-reproducibilidad-numerica-entre-plataformas/README.md)
20. [040 — Capstone: auditor de precisión numérica](040-capstone-auditor-de-precision-numerica/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 01
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Goldberg, D. *What Every Computer Scientist Should Know About Floating-Point Arithmetic*. ACM Computing Surveys, 1991.
- Higham, N. J. *Accuracy and Stability of Numerical Algorithms*. 2ª ed., SIAM, 2002.
- IEEE 754-2019 Standard for Floating-Point Arithmetic.
