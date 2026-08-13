# Parte 02 — Álgebra y funciones

**Nivel:** basico
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part02.py`

Manipulación simbólica con criterio y la función como objeto central: dominio, imagen, composición, inversa y familias lineal, cuadrática, exponencial y logarítmica.

## 🧠 Ideas centrales

- Una ecuación restringe; una función asigna. No son lo mismo.
- El dominio forma parte de la definición: cambiarlo cambia la función.
- El discriminante decide la naturaleza de las raíces antes de calcularlas.
- El logaritmo convierte producto en suma: por eso aparece en toda función de pérdida.
- Componer funciones es la operación que después llamaremos «capa» en una red neuronal.

## 🤖 Por qué importa en IA

Una red neuronal es una composición de funciones parametrizadas. La sigmoide, la softmax y la log-verosimilitud son álgebra de exponenciales y logaritmos.

## ⚠️ Errores frecuentes

- Dividir por una expresión que puede anularse y perder soluciones.
- Aplicar log a valores no positivos sin declarar el dominio.
- Confundir función inversa con recíproco.

## 🧰 Stack de referencia

`math`, `cmath`, `sympy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [041 — Expresiones algebraicas y términos](041-expresiones-algebraicas-y-terminos/README.md)
2. [042 — Propiedades distributiva, asociativa y conmutativa](042-propiedades-distributiva-asociativa-y-conmutativa/README.md)
3. [043 — Ecuaciones lineales de una variable](043-ecuaciones-lineales-de-una-variable/README.md)
4. [044 — Desigualdades lineales](044-desigualdades-lineales/README.md)
5. [045 — Sistemas de ecuaciones 2x2](045-sistemas-de-ecuaciones-2x2/README.md)
6. [046 — Polinomios y operaciones](046-polinomios-y-operaciones/README.md)
7. [047 — Factorización elemental](047-factorizacion-elemental/README.md)
8. [048 — Ecuaciones cuadráticas](048-ecuaciones-cuadraticas/README.md)
9. [049 — Fórmula cuadrática y discriminante](049-formula-cuadratica-y-discriminante/README.md)
10. [050 — Exponentes algebraicos](050-exponentes-algebraicos/README.md)
11. [051 — Logaritmos y sus propiedades](051-logaritmos-y-sus-propiedades/README.md)
12. [052 — Funciones: dominio y rango](052-funciones-dominio-y-rango/README.md)
13. [053 — Funciones lineales y pendiente](053-funciones-lineales-y-pendiente/README.md)
14. [054 — Funciones cuadráticas y parábolas](054-funciones-cuadraticas-y-parabolas/README.md)
15. [055 — Funciones exponenciales](055-funciones-exponenciales/README.md)
16. [056 — Funciones logarítmicas](056-funciones-logaritmicas/README.md)
17. [057 — Composición de funciones](057-composicion-de-funciones/README.md)
18. [058 — Funciones inversas](058-funciones-inversas/README.md)
19. [059 — Funciones por tramos](059-funciones-por-tramos/README.md)
20. [060 — Capstone: construir y comparar modelos funcionales](060-capstone-construir-y-comparar-modelos-funcionales/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 02
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Axler, S. *Precalculus: A Prelude to Calculus*. 3ª ed., Wiley, 2017.
- Gelfand, I. M.; Glagoleva, E.; Shnol, E. *Functions and Graphs*. Dover, 2002.
- Stewart, J. *Precalculus: Mathematics for Calculus*. 7ª ed., Cengage, 2015.
