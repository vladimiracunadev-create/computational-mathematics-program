# Parte 03 — Geometría, trigonometría y geometría analítica

**Nivel:** basico-intermedio
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part03.py`

Del espacio a las coordenadas: distancia, ángulo, trigonometría, transformaciones lineales en el plano, coordenadas polares y proyección.

## 🧠 Ideas centrales

- El radián no es una unidad decorativa: es la que hace que d(sin x)/dx = cos x.
- Toda rotación 2D es una matriz ortogonal de determinante 1.
- El producto punto mide alineación; la norma mide magnitud.
- Componer transformaciones es multiplicar matrices, y el orden importa.
- Las coordenadas homogéneas convierten la traslación en multiplicación.

## 🤖 Por qué importa en IA

Las transformaciones geométricas son el caso visual de las transformaciones lineales que una red aplica a sus activaciones; la similitud coseno es trigonometría en alta dimensión.

## ⚠️ Errores frecuentes

- Mezclar grados y radianes en la misma expresión.
- Aplicar rotación y traslación en el orden equivocado.
- Olvidar normalizar antes de comparar direcciones.

## 🧰 Stack de referencia

`math`, `numpy (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [061 — Puntos, segmentos y distancias](061-puntos-segmentos-y-distancias/README.md)
2. [062 — Ángulos y radianes](062-angulos-y-radianes/README.md)
3. [063 — Triángulos y semejanza](063-triangulos-y-semejanza/README.md)
4. [064 — Teorema de Pitágoras](064-teorema-de-pitagoras/README.md)
5. [065 — Seno, coseno y tangente](065-seno-coseno-y-tangente/README.md)
6. [066 — Identidades trigonométricas básicas](066-identidades-trigonometricas-basicas/README.md)
7. [067 — Círculo unitario](067-circulo-unitario/README.md)
8. [068 — Coordenadas cartesianas](068-coordenadas-cartesianas/README.md)
9. [069 — Pendiente y ecuación de la recta](069-pendiente-y-ecuacion-de-la-recta/README.md)
10. [070 — Distancia punto-recta](070-distancia-punto-recta/README.md)
11. [071 — Circunferencias y cónicas](071-circunferencias-y-conicas/README.md)
12. [072 — Vectores geométricos 2D](072-vectores-geometricos-2d/README.md)
13. [073 — Transformaciones: traslación y escala](073-transformaciones-traslacion-y-escala/README.md)
14. [074 — Rotaciones 2D](074-rotaciones-2d/README.md)
15. [075 — Matrices de transformación](075-matrices-de-transformacion/README.md)
16. [076 — Coordenadas polares](076-coordenadas-polares/README.md)
17. [077 — Geometría 3D y planos](077-geometria-3d-y-planos/README.md)
18. [078 — Proyecciones y perspectiva](078-proyecciones-y-perspectiva/README.md)
19. [079 — Aplicaciones en visión, robótica y videojuegos](079-aplicaciones-en-vision-robotica-y-videojuegos/README.md)
20. [080 — Capstone: motor geométrico 2D](080-capstone-motor-geometrico-2d/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 03
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Hartley, R.; Zisserman, A. *Multiple View Geometry in Computer Vision*. 2ª ed., Cambridge, 2004.
- Coxeter, H. S. M. *Introduction to Geometry*. 2ª ed., Wiley, 1989.
- Lengyel, E. *Mathematics for 3D Game Programming and Computer Graphics*. 3ª ed., 2011.
