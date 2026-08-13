# 📖 Glosario — Parte 08: Cálculo multivariable, matricial y autodiferenciación

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

19 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Campo conservativo** | Campo que es el gradiente de una función potencial. Su rotacional es nulo. | [175](175-campos-vectoriales/README.md) |
| **Campo vectorial** | Función que asigna un vector a cada punto del espacio. | [175](175-campos-vectoriales/README.md) |
| **Convención de layout** | Acuerdo sobre si el gradiente es fila o columna. Mezclar convenciones produce transposiciones erróneas. | [177](177-calculo-matricial/README.md) |
| **Curva de nivel** | Conjunto de puntos donde la función toma el mismo valor. El gradiente es perpendicular a ella. | [162](162-superficies-y-curvas-de-nivel/README.md) |
| **Derivada direccional** | Tasa de cambio en una dirección unitaria; es la proyección del gradiente sobre ella. | [165](165-derivada-direccional/README.md) |
| **Derivada parcial** | Derivada respecto a una variable manteniendo las demás fijas. Se denota ∂f/∂x. | [163](163-derivadas-parciales/README.md) |
| **Divergencia** | Medida de cuánto un campo actúa como fuente o sumidero en un punto. | [176](176-divergencia-y-rotacional/README.md) |
| **Gradiente** | Vector de derivadas parciales. Apunta en la dirección de mayor crecimiento y su norma mide la pendiente. | [164](164-gradiente/README.md) |
| **Grafo de cómputo** | DAG cuyos nodos son operaciones. La autodiferenciación lo recorre en orden topológico inverso. | [179](179-automatic-differentiation-y-computational-graphs/README.md) |
| **Hessiano** | Matriz de segundas derivadas. Describe la curvatura y clasifica los puntos críticos. | [169](169-hessiano/README.md) |
| **Jacobiano** | Matriz de primeras derivadas de una función vectorial. Su fila i es el gradiente de la componente i. | [168](168-jacobiano/README.md) |
| **Modo reverso** | Estrategia de autodiferenciación que calcula todas las derivadas con un barrido hacia adelante y uno hacia atrás. | [179](179-automatic-differentiation-y-computational-graphs/README.md) |
| **Multiplicador de Lagrange** | Coeficiente λ que mide cuánto mejora el óptimo al relajar la restricción una unidad. | [172](172-multiplicadores-de-lagrange/README.md) |
| **Plano tangente** | Aproximación lineal de una superficie en un punto. Su error crece cuadráticamente con la distancia. | [166](166-plano-tangente/README.md) |
| **Punto de silla** | Punto crítico con Hessiano de autovalores de signos mixtos: mínimo en unas direcciones y máximo en otras. | [169](169-hessiano/README.md) |
| **Rotacional** | Medida de la circulación local de un campo alrededor de un punto. | [176](176-divergencia-y-rotacional/README.md) |
| **Taylor multivariable** | f(x+d) ≈ f(x) + ∇fᵀd + ½dᵀHd. El término de segundo orden usa el Hessiano. | [170](170-taylor-multivariable/README.md) |
| **Teorema de Fubini** | Permite calcular una integral múltiple como integrales iteradas cuando la función es integrable. | [173](173-integrales-dobles/README.md) |
| **VJP** | Producto vector-Jacobiano. Es lo que calcula el modo reverso sin construir el Jacobiano completo. | [168](168-jacobiano/README.md) |

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
