# 📖 Glosario — Parte 04: Matemática discreta para computación

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

21 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Aritmética modular** | Aritmética de los restos respecto a un módulo. Base de hashing, criptografía y checksums. | [098](098-aritmetica-modular/README.md) |
| **BFS** | Recorrido en anchura. Encuentra el camino con menos aristas en un grafo no ponderado. Coste O(V+E). | [094](094-caminos-ciclos-y-conectividad/README.md) |
| **Combinación** | Selección sin orden. C(n,k) = n!/(k!(n−k)!). Simétrica: C(n,k) = C(n,n−k). | [089](089-combinaciones/README.md) |
| **Contrarrecíproca** | ¬q → ¬p. Lógicamente equivalente a p → q, y a menudo más fácil de demostrar. | [081](081-logica-proposicional/README.md) |
| **Criba de Eratóstenes** | Algoritmo que encuentra todos los primos hasta n tachando múltiplos. Coste O(n log log n). | [099](099-numeros-primos-y-maximo-comun-divisor/README.md) |
| **Cuantificador universal** | ∀x P(x): P se cumple para todo elemento del universo. Su negación es ∃x ¬P(x). | [083](083-logica-de-predicados-y-cuantificadores/README.md) |
| **DAG** | Grafo dirigido acíclico. Admite orden topológico; su ausencia delata un ciclo. | [096](096-dag-y-orden-topologico/README.md) |
| **Función inyectiva** | Entradas distintas dan salidas distintas. Condición necesaria para que exista inversa. | [086](086-funciones-discretas/README.md) |
| **Grado de un vértice** | Número de aristas incidentes. La suma de los grados es el doble del número de aristas. | [093](093-grafos-vertices-y-aristas/README.md) |
| **Implicación** | p → q, falsa solo cuando p es verdadera y q falsa. Equivale a su contrarrecíproca, no a su recíproca. | [081](081-logica-proposicional/README.md) |
| **Inclusión-exclusión** | |A∪B| = |A| + |B| − |A∩B|. Corrige el doble conteo de la intersección. | [084](084-conjuntos-y-operaciones/README.md) |
| **Inducción matemática** | Método de demostración con caso base y paso inductivo. Cubre infinitos casos con dos argumentos. | [091](091-induccion-matematica/README.md) |
| **Leyes de De Morgan** | ¬(p∧q) ≡ ¬p∨¬q y ¬(p∨q) ≡ ¬p∧¬q. Rigen la negación de condiciones compuestas. | [082](082-tablas-de-verdad-y-equivalencias/README.md) |
| **Orden topológico** | Ordenación de los vértices de un DAG tal que toda arista va de un vértice anterior a uno posterior. | [096](096-dag-y-orden-topologico/README.md) |
| **Permutación** | Selección ordenada. P(n,k) = n!/(n−k)! | [088](088-permutaciones/README.md) |
| **Principio del palomar** | Si n objetos se reparten en m cajas con n > m, alguna caja tiene al menos dos. Demuestra colisiones sin construirlas. | [090](090-principio-del-palomar/README.md) |
| **Recurrencia** | Definición de un término en función de los anteriores. Su coste depende de si se memoiza. | [092](092-recurrencias/README.md) |
| **Regla del producto** | Si una decisión tiene m opciones y otra n, hay m·n combinaciones. | [087](087-principios-de-conteo/README.md) |
| **Relación de equivalencia** | Relación reflexiva, simétrica y transitiva. Particiona el conjunto en clases disjuntas. | [085](085-relaciones-y-propiedades/README.md) |
| **Tautología** | Fórmula verdadera bajo toda asignación de valores de verdad. | [082](082-tablas-de-verdad-y-equivalencias/README.md) |
| **Árbol** | Grafo conexo sin ciclos. Con n vértices tiene exactamente n−1 aristas. | [095](095-arboles-y-arboles-de-expansion/README.md) |

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
