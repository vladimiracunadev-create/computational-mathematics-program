# Parte 07 — Cálculo diferencial e integral

**Nivel:** universitario
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part07.py`

Límite, continuidad, derivada, reglas de derivación, Taylor, optimización de una variable, integral definida y teorema fundamental del cálculo.

## 🧠 Ideas centrales

- La derivada es la mejor aproximación lineal local, no solo una pendiente.
- La regla de la cadena es el mecanismo entero de backpropagation.
- Taylor cambia una función difícil por un polinomio con error acotado.
- Integrar es acumular; derivar e integrar son operaciones inversas.
- Derivada nula señala punto crítico, no necesariamente mínimo.

## 🤖 Por qué importa en IA

Sin regla de la cadena no hay entrenamiento por gradiente; sin Taylor no hay métodos de segundo orden ni análisis de convergencia.

## ⚠️ Errores frecuentes

- Usar diferencias finitas con h demasiado pequeño y amplificar el error de redondeo.
- Derivar en un punto donde la función no es continua.
- Confundir punto crítico con extremo global.

## 🧰 Stack de referencia

`math`, `sympy (opcional)`, `scipy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [141 — Intuición de límite](141-intuicion-de-limite/README.md)
2. [142 — Límites algebraicos](142-limites-algebraicos/README.md)
3. [143 — Continuidad](143-continuidad/README.md)
4. [144 — Derivada como tasa de cambio](144-derivada-como-tasa-de-cambio/README.md)
5. [145 — Reglas de derivación](145-reglas-de-derivacion/README.md)
6. [146 — Regla del producto y cociente](146-regla-del-producto-y-cociente/README.md)
7. [147 — Regla de la cadena](147-regla-de-la-cadena/README.md)
8. [148 — Derivadas de exponenciales y logaritmos](148-derivadas-de-exponenciales-y-logaritmos/README.md)
9. [149 — Derivadas trigonométricas](149-derivadas-trigonometricas/README.md)
10. [150 — Derivación implícita](150-derivacion-implicita/README.md)
11. [151 — Aproximación lineal y Taylor](151-aproximacion-lineal-y-taylor/README.md)
12. [152 — Máximos y mínimos](152-maximos-y-minimos/README.md)
13. [153 — Integral como acumulación](153-integral-como-acumulacion/README.md)
14. [154 — Integral definida](154-integral-definida/README.md)
15. [155 — Antiderivadas](155-antiderivadas/README.md)
16. [156 — Teorema fundamental del cálculo](156-teorema-fundamental-del-calculo/README.md)
17. [157 — Integración por sustitución](157-integracion-por-sustitucion/README.md)
18. [158 — Integración por partes](158-integracion-por-partes/README.md)
19. [159 — Integración numérica introductoria](159-integracion-numerica-introductoria/README.md)
20. [160 — Capstone: optimizar y acumular una señal](160-capstone-optimizar-y-acumular-una-senal/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 07
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Spivak, M. *Calculus*. 4ª ed., Publish or Perish, 2008.
- Apostol, T. *Calculus, Vol. 1*. 2ª ed., Wiley, 1967.
- Strang, G. *Calculus*. 3ª ed., Wellesley-Cambridge, 2017.
