# Parte 08 — Cálculo multivariable, matricial y autodiferenciación

**Nivel:** universitario-avanzado
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part08.py`

Derivadas parciales, gradiente, Jacobiano, Hessiano, Taylor multivariable, multiplicadores de Lagrange, cálculo matricial y autodiferenciación.

## 🧠 Ideas centrales

- El gradiente apunta al mayor ascenso; por eso se desciende en su dirección opuesta.
- El Jacobiano generaliza la derivada a funciones vectoriales.
- El Hessiano describe la curvatura y decide el tipo de punto crítico.
- Modo reverso calcula todas las derivadas en un solo barrido hacia atrás.
- Lagrange convierte una restricción en un término de la función objetivo.

## 🤖 Por qué importa en IA

Autograd de PyTorch y JAX es exactamente el modo reverso del grafo de cómputo que se construye en esta parte a mano.

## ⚠️ Errores frecuentes

- Confundir la convención de layout (numerador vs denominador) en cálculo matricial.
- Suponer que el Hessiano es definido positivo sin comprobarlo.
- Olvidar acumular gradientes cuando un nodo se reutiliza en el grafo.

## 🧰 Stack de referencia

`math`, `numpy (opcional)`, `jax/torch (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [161 — Funciones de varias variables](161-funciones-de-varias-variables/README.md)
2. [162 — Superficies y curvas de nivel](162-superficies-y-curvas-de-nivel/README.md)
3. [163 — Derivadas parciales](163-derivadas-parciales/README.md)
4. [164 — Gradiente](164-gradiente/README.md)
5. [165 — Derivada direccional](165-derivada-direccional/README.md)
6. [166 — Plano tangente](166-plano-tangente/README.md)
7. [167 — Regla de la cadena multivariable](167-regla-de-la-cadena-multivariable/README.md)
8. [168 — Jacobiano](168-jacobiano/README.md)
9. [169 — Hessiano](169-hessiano/README.md)
10. [170 — Taylor multivariable](170-taylor-multivariable/README.md)
11. [171 — Optimización sin restricciones](171-optimizacion-sin-restricciones/README.md)
12. [172 — Multiplicadores de Lagrange](172-multiplicadores-de-lagrange/README.md)
13. [173 — Integrales dobles](173-integrales-dobles/README.md)
14. [174 — Integrales triples](174-integrales-triples/README.md)
15. [175 — Campos vectoriales](175-campos-vectoriales/README.md)
16. [176 — Divergencia y rotacional](176-divergencia-y-rotacional/README.md)
17. [177 — Cálculo matricial](177-calculo-matricial/README.md)
18. [178 — Derivadas respecto de vectores y matrices](178-derivadas-respecto-de-vectores-y-matrices/README.md)
19. [179 — Automatic differentiation y computational graphs](179-automatic-differentiation-y-computational-graphs/README.md)
20. [180 — Capstone: backpropagation manual y automática](180-capstone-backpropagation-manual-y-automatica/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 08
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Petersen, K.; Pedersen, M. *The Matrix Cookbook*. 2012.
- Baydin, A. et al. *Automatic Differentiation in Machine Learning: a Survey*. JMLR, 2018.
- Magnus, J.; Neudecker, H. *Matrix Differential Calculus*. 3ª ed., Wiley, 2019.
