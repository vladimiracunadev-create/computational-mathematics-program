# Parte 04 — Matemática discreta para computación

**Nivel:** intermedio
**Clases:** 20
**Horas estimadas:** 80
**Motor ejecutable:** `src/computational_math/engines/part04.py`

Lógica, conjuntos, conteo, inducción, recurrencias, grafos y aritmética modular: la matemática que hace demostrable un programa.

## 🧠 Ideas centrales

- Una demostración por inducción es un bucle `for` con garantía.
- Permutación cuenta orden; combinación cuenta selección.
- Un DAG sin orden topológico contiene un ciclo: es un diagnóstico, no un error.
- La aritmética modular es la base de hashing, criptografía y checksums.
- El principio del palomar demuestra colisiones sin construir un ejemplo.

## 🤖 Por qué importa en IA

Los grafos de cómputo, la búsqueda en árbol y las GNN son estructuras discretas; el conteo sostiene la probabilidad que después usa todo modelo generativo.

## ⚠️ Errores frecuentes

- Contar dos veces al aplicar el principio de inclusión-exclusión.
- Confundir implicación con equivalencia lógica.
- Asumir que un grafo dirigido es acíclico sin verificarlo.

## 🧰 Stack de referencia

`itertools`, `math`, `collections`

Los laboratorios se ejecutan con biblioteca estándar; estas herramientas
aparecen como contraste profesional, no como requisito.

## 📚 Secuencia

1. [081 — Lógica proposicional](081-logica-proposicional/README.md)
2. [082 — Tablas de verdad y equivalencias](082-tablas-de-verdad-y-equivalencias/README.md)
3. [083 — Lógica de predicados y cuantificadores](083-logica-de-predicados-y-cuantificadores/README.md)
4. [084 — Conjuntos y operaciones](084-conjuntos-y-operaciones/README.md)
5. [085 — Relaciones y propiedades](085-relaciones-y-propiedades/README.md)
6. [086 — Funciones discretas](086-funciones-discretas/README.md)
7. [087 — Principios de conteo](087-principios-de-conteo/README.md)
8. [088 — Permutaciones](088-permutaciones/README.md)
9. [089 — Combinaciones](089-combinaciones/README.md)
10. [090 — Principio del palomar](090-principio-del-palomar/README.md)
11. [091 — Inducción matemática](091-induccion-matematica/README.md)
12. [092 — Recurrencias](092-recurrencias/README.md)
13. [093 — Grafos: vértices y aristas](093-grafos-vertices-y-aristas/README.md)
14. [094 — Caminos, ciclos y conectividad](094-caminos-ciclos-y-conectividad/README.md)
15. [095 — Árboles y árboles de expansión](095-arboles-y-arboles-de-expansion/README.md)
16. [096 — DAG y orden topológico](096-dag-y-orden-topologico/README.md)
17. [097 — Álgebra booleana](097-algebra-booleana/README.md)
18. [098 — Aritmética modular](098-aritmetica-modular/README.md)
19. [099 — Números primos y máximo común divisor](099-numeros-primos-y-maximo-comun-divisor/README.md)
20. [100 — Capstone: modelar dependencias con grafos](100-capstone-modelar-dependencias-con-grafos/README.md)

## 🧪 Ejecutar toda la parte

```bash
compmath run --part 04
```

## 📊 Evaluación de la parte

| Componente | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

## 📖 Bibliografía

- Rosen, K. *Discrete Mathematics and Its Applications*. 8ª ed., McGraw-Hill, 2019.
- Graham, R.; Knuth, D.; Patashnik, O. *Concrete Mathematics*. 2ª ed., Addison-Wesley, 1994.
- Cormen, T. et al. *Introduction to Algorithms*. 4ª ed., MIT Press, 2022.
