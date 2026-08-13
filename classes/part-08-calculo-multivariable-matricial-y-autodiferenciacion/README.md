# 🌐 Parte 08 — Cálculo multivariable, matricial y autodiferenciación

> [⬅️ Parte 07 — Cálculo diferencial e integral](../part-07-calculo-diferencial-e-integral/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 09 — Probabilidad y procesos aleatorios ➡️](../part-09-probabilidad-y-procesos-aleatorios/README.md)

**Nivel:** `universitario-avanzado` · **Clases:** 20 · **Horas estimadas:** 80 · **Motor:** [`part08.py`](../../src/computational_math/engines/part08.py)

---

## 🎯 De qué trata esta parte

Derivadas parciales, gradiente, Jacobiano, Hessiano, Taylor multivariable, multiplicadores de Lagrange, cálculo matricial y autodiferenciación.

Esta es la parte donde el programa deja de hablar de matemática «que se usa en IA» y pasa a
construir el mecanismo exacto que entrena una red neuronal. Al final de las 20 clases habrás
implementado un motor de autodiferenciación en modo reverso de unas cien líneas y habrás
comprobado que sus gradientes coinciden con los que calculaste a mano.

Las clases 161 a 166 extienden la derivada a varias variables. La idea central es que el
**gradiente** es el vector de derivadas parciales y apunta en la dirección de mayor
crecimiento. De ahí sale, sin más argumento, el descenso de gradiente: para minimizar, hay
que moverse en la dirección opuesta. Todo el entrenamiento de un modelo es esa frase repetida
millones de veces.

Las clases 167 a 170 generalizan la maquinaria: regla de la cadena multivariable, Jacobiano,
Hessiano y Taylor. El Jacobiano es la derivada de una función vectorial y es el objeto que
manipulan internamente los frameworks: `backward()` calcula un producto vector-Jacobiano sin
construir nunca el Jacobiano completo, que sería inmanejable. El Hessiano describe la
curvatura y decide si un punto crítico es mínimo, máximo o silla.

Las clases 171 y 172 son optimización: descenso de gradiente sobre una cuadrática y
multiplicadores de Lagrange. Lagrange convierte una restricción en un término del objetivo, y
su multiplicador tiene una interpretación económica precisa —cuánto mejora el óptimo si se
relaja la restricción— que reaparece en KKT (clase 257) y en el precio sombra de la
programación lineal.

Las clases 173 a 176 tratan integrales múltiples y campos vectoriales, y las clases 177 y 178
el cálculo matricial: cómo derivar respecto a vectores y matrices. Ahí aparece la identidad
más usada en machine learning: el gradiente de la pérdida cuadrática `‖Xw − y‖²/n` es
`2Xᵀ(Xw − y)/n`. Esa expresión **es** el gradiente de una capa lineal.

El cierre (179 y 180) implementa la autodiferenciación y la contrasta con backpropagation
manual sobre la misma red. Que ambos den exactamente el mismo número es la demostración de
que autograd no es magia: es la regla de la cadena aplicada en orden topológico inverso
(clase 096).

## 🗺️ Mapa conceptual

```mermaid
flowchart TD
    A["Clases 161-166 · Funciones de varias variables y gradiente"] --> B["Clases 167-170 · Cadena, Jacobiano, Hessiano y Taylor"]
    B --> C["Clases 171-172 · Optimizacion y Lagrange"]
    A --> D["Clases 173-176 · Integrales multiples y campos"]
    B --> E["Clases 177-178 · Calculo matricial"]
    E --> F["Clases 179-180 · Autodiferenciacion y capstone"]
    C --> F
    F ==> G["Parte 15 · Backpropagation en redes profundas"]
    A -.-> H["Descenso de gradiente · Parte 12"]
    B -.-> I["Metodos de segundo orden · Parte 12"]
    E -.-> J["Gradiente de una capa lineal · Parte 14"]
```

## 🧠 Ideas centrales

- El gradiente apunta al mayor ascenso; por eso se desciende en su dirección opuesta.
- El Jacobiano generaliza la derivada a funciones vectoriales.
- El Hessiano describe la curvatura y decide el tipo de punto crítico.
- Modo reverso calcula todas las derivadas en un solo barrido hacia atrás.
- Lagrange convierte una restricción en un término de la función objetivo.

## 🤖 Por qué importa en IA

> [!IMPORTANT]
> Autograd de PyTorch y JAX es exactamente el modo reverso del grafo de cómputo que se construye en esta parte a mano.

## ⚠️ Errores frecuentes de esta parte

- Confundir la convención de layout (numerador vs denominador) en cálculo matricial.
- Suponer que el Hessiano es definido positivo sin comprobarlo.
- Olvidar acumular gradientes cuando un nodo se reutiliza en el grafo.

## 🧭 Secuencia de la parte

```mermaid
flowchart LR
    subgraph B1["Bloque 1"]
        direction TB
        L161["161 · Funciones de varias variables"]
        L162["162 · Superficies y curvas de nivel"]
        L163["163 · Derivadas parciales"]
        L164["164 · Gradiente"]
        L165["165 · Derivada direccional"]
        L161 --> L162
        L162 --> L163
        L163 --> L164
        L164 --> L165
    end
    subgraph B2["Bloque 2"]
        direction TB
        L166["166 · Plano tangente"]
        L167["167 · Regla de la cadena…"]
        L168["168 · Jacobiano"]
        L169["169 · Hessiano"]
        L170["170 · Taylor multivariable"]
        L166 --> L167
        L167 --> L168
        L168 --> L169
        L169 --> L170
    end
    subgraph B3["Bloque 3"]
        direction TB
        L171["171 · Optimización sin restricciones"]
        L172["172 · Multiplicadores de Lagrange"]
        L173["173 · Integrales dobles"]
        L174["174 · Integrales triples"]
        L175["175 · Campos vectoriales"]
        L171 --> L172
        L172 --> L173
        L173 --> L174
        L174 --> L175
    end
    subgraph B4["Bloque 4"]
        direction TB
        L176["176 · Divergencia y rotacional"]
        L177["177 · Cálculo matricial"]
        L178["178 · Derivadas respecto de…"]
        L179["179 · Automatic differentiation y…"]
        L180["180 · Capstone: backpropagation…"]
        L176 --> L177
        L177 --> L178
        L178 --> L179
        L179 --> L180
    end
    L165 --> L166
    L170 --> L171
    L175 --> L176
```

## 📚 Las clases

| # | Clase | Demostración | Idea central |
|---|---|---|---|
| `161` | [Funciones de varias variables](161-funciones-de-varias-variables/README.md) | `multivariable_functions` | Una función de varias variables asigna un número a cada punto de un espacio; su gráfica vive una dimensión más arriba. |
| `162` | [Superficies y curvas de nivel](162-superficies-y-curvas-de-nivel/README.md) | `level_curves` | Las curvas de nivel son los conjuntos donde la función vale lo mismo, y el gradiente es perpendicular a ellas. |
| `163` | [Derivadas parciales](163-derivadas-parciales/README.md) | `partial_derivatives` | Una derivada parcial mide el cambio en una dirección de eje, congelando el resto. |
| `164` | [Gradiente](164-gradiente/README.md) | `gradient` | El gradiente apunta al mayor ascenso; por eso se minimiza moviéndose en dirección contraria. |
| `165` | [Derivada direccional](165-derivada-direccional/README.md) | `directional_derivative` | La derivada direccional es la proyección del gradiente sobre una dirección unitaria. |
| `166` | [Plano tangente](166-plano-tangente/README.md) | `tangent_plane` | El plano tangente es la aproximación lineal en varias variables, y su error crece cuadráticamente. |
| `167` | [Regla de la cadena multivariable](167-regla-de-la-cadena-multivariable/README.md) | `multivariable_chain_rule` | La regla de la cadena multivariable suma las contribuciones de todos los caminos. |
| `168` | [Jacobiano](168-jacobiano/README.md) | `jacobian` | El Jacobiano es la derivada de una función vectorial; el modo reverso calcula vᵀJ sin construirlo. |
| `169` | [Hessiano](169-hessiano/README.md) | `hessian` | El Hessiano describe la curvatura, y el signo de sus autovalores clasifica el punto crítico. |
| `170` | [Taylor multivariable](170-taylor-multivariable/README.md) | `multivariable_taylor` | Taylor de segundo orden usa el Hessiano y reduce el error de cuadrático a cúbico. |
| `171` | [Optimización sin restricciones](171-optimizacion-sin-restricciones/README.md) | `unconstrained_optimization` | El descenso de gradiente converge en una cuadrática si el paso respeta el límite de estabilidad. |
| `172` | [Multiplicadores de Lagrange](172-multiplicadores-de-lagrange/README.md) | `lagrange_multipliers` | Lagrange convierte una restricción en un término del objetivo, y su multiplicador mide el precio de esa restricción. |
| `173` | [Integrales dobles](173-integrales-dobles/README.md) | `double_integrals` | Fubini permite calcular una integral doble como dos integrales simples encadenadas. |
| `174` | [Integrales triples](174-integrales-triples/README.md) | `triple_integrals` | Una integral triple con densidad variable calcula masa; el volumen es el caso de densidad unitaria. |
| `175` | [Campos vectoriales](175-campos-vectoriales/README.md) | `vector_fields` | Un campo conservativo es el gradiente de un potencial; no todos los campos lo son. |
| `176` | [Divergencia y rotacional](176-divergencia-y-rotacional/README.md) | `divergence_curl` | La divergencia mide fuente o sumidero; el rotacional mide circulación local. |
| `177` | [Cálculo matricial](177-calculo-matricial/README.md) | `matrix_calculus` | El cálculo matricial da fórmulas cerradas para gradientes respecto a vectores y matrices. |
| `178` | [Derivadas respecto de vectores y matrices](178-derivadas-respecto-de-vectores-y-matrices/README.md) | `vector_matrix_derivatives` | El gradiente de la pérdida cuadrática es 2Xᵀ(Xw − y)/n: esa expresión es el gradiente de una capa lineal. |
| `179` | [Automatic differentiation y computational graphs](179-automatic-differentiation-y-computational-graphs/README.md) | `autodiff` | La autodiferenciación en modo reverso obtiene todos los gradientes con un barrido hacia adelante y uno hacia atrás. |
| `180` | [Capstone: backpropagation manual y automática](180-capstone-backpropagation-manual-y-automatica/README.md) | `capstone_backpropagation` | Backpropagation manual y autodiferenciación dan exactamente el mismo número: autograd no es magia. |

## 📖 Glosario de la parte (19 términos)

Definiciones precisas en [`GLOSARIO.md`](GLOSARIO.md).

## 🧰 Stack de referencia

`math`, `numpy (opcional)`, `jax/torch (opcional)`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen
como contraste profesional, no como requisito.

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 08
compmath catalog --part 08
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone ([180](180-capstone-backpropagation-manual-y-automatica/README.md)) | 20 % |

## 📖 Bibliografía

- Petersen, K.; Pedersen, M. *The Matrix Cookbook*. 2012.
- Baydin, A. et al. *Automatic Differentiation in Machine Learning: a Survey*. JMLR, 2018.
- Magnus, J.; Neudecker, H. *Matrix Differential Calculus*. 3ª ed., Wiley, 2019.

---

> [⬅️ Parte 07 — Cálculo diferencial e integral](../part-07-calculo-diferencial-e-integral/README.md) · [🏠 Programa](../../README.md) · [📇 Catálogo](../README.md) · [Parte 09 — Probabilidad y procesos aleatorios ➡️](../part-09-probabilidad-y-procesos-aleatorios/README.md)
