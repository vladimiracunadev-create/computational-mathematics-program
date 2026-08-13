"""Motor 04 — Matemática discreta para computación.

Lógica, conjuntos, conteo, inducción, recurrencias, grafos y aritmética modular.
"""

from __future__ import annotations

import math
from itertools import combinations, permutations, product

PART = "04"
TITLE = "Matemática discreta para computación"

_GRAFO = {
    "entrada": ["limpieza"],
    "limpieza": ["features", "split"],
    "features": ["entrenamiento"],
    "split": ["entrenamiento"],
    "entrenamiento": ["evaluacion"],
    "evaluacion": [],
}


def propositional_logic() -> dict:
    """Implicación, contrarrecíproca y recíproca no son lo mismo."""
    filas = []
    for p, q in product([True, False], repeat=2):
        filas.append({
            "p": p,
            "q": q,
            "p→q": (not p) or q,
            "q→p (recíproca)": (not q) or p,
            "¬q→¬p (contrarrecíproca)": q or (not p),
        })
    return {
        "tabla": filas,
        "implicacion_equivale_a_contrarreciproca": all(f["p→q"] == f["¬q→¬p (contrarrecíproca)"] for f in filas),
        "implicacion_equivale_a_reciproca": all(f["p→q"] == f["q→p (recíproca)"] for f in filas),
        "vacuamente_verdadera": "p falso hace p→q verdadera",
    }


def truth_tables() -> dict:
    """Leyes de De Morgan verificadas exhaustivamente."""
    casos = list(product([True, False], repeat=2))
    de_morgan_1 = all(not (p and q) == ((not p) or (not q)) for p, q in casos)
    de_morgan_2 = all(not (p or q) == ((not p) and (not q)) for p, q in casos)
    return {
        "casos_evaluados": len(casos),
        "¬(p∧q) ≡ ¬p∨¬q": de_morgan_1,
        "¬(p∨q) ≡ ¬p∧¬q": de_morgan_2,
        "tautologia_p∨¬p": all(p or (not p) for p, _ in casos),
        "contradiccion_p∧¬p": not any(p and (not p) for p, _ in casos),
        "xor": [(p, q, p != q) for p, q in casos],
    }


def predicate_logic() -> dict:
    """Cuantificadores: el orden cambia el significado."""
    universo = [1, 2, 3, 4, 5, 6]
    para_todo_par = all(x % 2 == 0 for x in universo)
    existe_par = any(x % 2 == 0 for x in universo)
    # ∀x ∃y : y > x  frente a  ∃y ∀x : y > x  (en un conjunto finito)
    forall_exists = all(any(y > x for y in universo) for x in universo)
    exists_forall = any(all(y > x for x in universo) for y in universo)
    return {
        "universo": universo,
        "∀x par(x)": para_todo_par,
        "∃x par(x)": existe_par,
        "negacion_de_∀_es_∃¬": not para_todo_par == any(x % 2 != 0 for x in universo),
        "∀x∃y y>x": forall_exists,
        "∃y∀x y>x": exists_forall,
        "el_orden_de_cuantificadores_importa": forall_exists != exists_forall,
    }


def sets() -> dict:
    """Operaciones de conjuntos e inclusión-exclusión."""
    a, b = {1, 2, 3, 4, 5}, {4, 5, 6, 7}
    return {
        "A": sorted(a),
        "B": sorted(b),
        "union": sorted(a | b),
        "interseccion": sorted(a & b),
        "diferencia_A-B": sorted(a - b),
        "diferencia_simetrica": sorted(a ^ b),
        "|A|+|B|-|A∩B|": len(a) + len(b) - len(a & b),
        "|A∪B|": len(a | b),
        "inclusion_exclusion_ok": len(a | b) == len(a) + len(b) - len(a & b),
        "partes_de_A": 2 ** len(a),
    }


def relations() -> dict:
    """Reflexiva, simétrica y transitiva: la receta de una relación de equivalencia."""
    universo = [0, 1, 2, 3, 4, 5]
    congruencia = {(x, y) for x in universo for y in universo if (x - y) % 3 == 0}
    reflexiva = all((x, x) in congruencia for x in universo)
    simetrica = all((y, x) in congruencia for x, y in congruencia)
    transitiva = all((x, z) in congruencia for x, y in congruencia for y2, z in congruencia if y == y2)
    clases = {}
    for x in universo:
        clases.setdefault(x % 3, []).append(x)
    return {
        "relacion": "x ≡ y (mod 3)",
        "reflexiva": reflexiva,
        "simetrica": simetrica,
        "transitiva": transitiva,
        "es_equivalencia": reflexiva and simetrica and transitiva,
        "clases_de_equivalencia": clases,
        "particiona_el_universo": sum(len(v) for v in clases.values()) == len(universo),
    }


def discrete_functions() -> dict:
    """Inyectiva, sobreyectiva y biyectiva sobre conjuntos finitos."""
    dominio = [1, 2, 3]
    f = {1: "a", 2: "b", 3: "c"}
    g = {1: "a", 2: "a", 3: "b"}
    codominio = {"a", "b", "c"}
    return {
        "f": f,
        "f_inyectiva": len(set(f.values())) == len(dominio),
        "f_sobreyectiva": set(f.values()) == codominio,
        "f_biyectiva": len(set(f.values())) == len(dominio) and set(f.values()) == codominio,
        "g": g,
        "g_inyectiva": len(set(g.values())) == len(dominio),
        "funciones_totales_posibles": len(codominio) ** len(dominio),
        "biyecciones_posibles": math.factorial(len(dominio)),
    }


def counting_principles() -> dict:
    """Regla del producto, de la suma y conteo de contraseñas."""
    letras, digitos, longitud = 26, 10, 8
    return {
        "regla_del_producto_3x4": 3 * 4,
        "regla_de_la_suma_3+4": 3 + 4,
        "contraseñas_alfanumericas_8": (letras + digitos) ** longitud,
        "contraseñas_solo_digitos_8": digitos**longitud,
        "factor_de_ventaja": (letras + digitos) ** longitud / digitos**longitud,
        "bits_de_entropia": round(math.log2((letras + digitos) ** longitud), 2),
    }


def permutations_demo() -> dict:
    """Permutaciones: el orden importa."""
    elementos = ["A", "B", "C", "D"]
    total = math.factorial(len(elementos))
    parciales = list(permutations(elementos, 2))
    return {
        "elementos": elementos,
        "permutaciones_totales_4!": total,
        "P(4,2)": len(parciales),
        "formula_n!/(n-k)!": math.factorial(4) // math.factorial(2),
        "primeras_5": parciales[:5],
        "con_repeticion_4^2": 4**2,
    }


def combinations_demo() -> dict:
    """Combinaciones: el orden no importa."""
    elementos = list("ABCDE")
    c = list(combinations(elementos, 3))
    return {
        "elementos": elementos,
        "C(5,3)": len(c),
        "math.comb": math.comb(5, 3),
        "simetria_C(5,3)=C(5,2)": math.comb(5, 3) == math.comb(5, 2),
        "todas": ["".join(x) for x in c],
        "suma_fila_de_pascal": sum(math.comb(5, k) for k in range(6)),
        "2^5": 2**5,
    }


def pigeonhole() -> dict:
    """Principio del palomar: colisiones garantizadas sin construirlas."""
    personas, dias = 400, 365
    hashes, entradas = 2**16, 100_000
    return {
        "personas": personas,
        "dias_del_año": dias,
        "coincidencia_de_cumpleaños_garantizada": personas > dias,
        "minimo_repeticiones": math.ceil(personas / dias),
        "espacio_hash": hashes,
        "entradas": entradas,
        "colision_garantizada": entradas > hashes,
        "leccion": "no hace falta encontrar la colisión para demostrar que existe",
    }


def induction() -> dict:
    """Inducción: caso base, paso inductivo y verificación empírica."""
    n_max = 50
    fallos = [n for n in range(1, n_max + 1) if sum(range(1, n + 1)) != n * (n + 1) // 2]
    return {
        "proposicion": "1+2+…+n = n(n+1)/2",
        "caso_base_n=1": sum(range(1, 2)) == 1 * 2 // 2,
        "paso_inductivo": "S(k)+(k+1) = k(k+1)/2 + (k+1) = (k+1)(k+2)/2",
        "verificado_hasta": n_max,
        "contraejemplos": fallos,
        "la_verificacion_no_es_demostracion": True,
    }


def recurrences() -> dict:
    """Recurrencia lineal: iterativo, memoizado y forma cerrada."""
    def fib_iterativo(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    phi = (1 + math.sqrt(5)) / 2
    n = 30
    cerrado = round((phi**n - (-1 / phi) ** n) / math.sqrt(5))
    return {
        "recurrencia": "F(n) = F(n-1) + F(n-2)",
        "F(30)_iterativo": fib_iterativo(n),
        "F(30)_binet": cerrado,
        "coinciden": fib_iterativo(n) == cerrado,
        "coste_recursivo_ingenuo": "O(φ^n)",
        "coste_iterativo": "O(n)",
        "razon_asintotica": fib_iterativo(n + 1) / fib_iterativo(n),
        "razon_aurea": phi,
    }


def graphs() -> dict:
    """Grados, aristas y el lema del apretón de manos."""
    grados = {nodo: len(vecinos) for nodo, vecinos in _GRAFO.items()}
    aristas = sum(grados.values())
    return {
        "nodos": sorted(_GRAFO),
        "grado_de_salida": grados,
        "aristas_dirigidas": aristas,
        "suma_de_grados": aristas,
        "lema_apreton_de_manos_no_dirigido": "Σ grados = 2|E|",
        "densidad": aristas / (len(_GRAFO) * (len(_GRAFO) - 1)),
    }


def paths_connectivity() -> dict:
    """Recorrido BFS: alcanzabilidad y distancia en aristas."""
    from collections import deque

    origen = "entrada"
    dist = {origen: 0}
    cola = deque([origen])
    orden = []
    while cola:
        nodo = cola.popleft()
        orden.append(nodo)
        for vecino in _GRAFO[nodo]:
            if vecino not in dist:
                dist[vecino] = dist[nodo] + 1
                cola.append(vecino)
    return {
        "origen": origen,
        "orden_de_visita": orden,
        "distancias": dist,
        "todos_alcanzables": len(dist) == len(_GRAFO),
        "excentricidad": max(dist.values()),
        "complejidad_BFS": "O(V + E)",
    }


def trees() -> dict:
    """Un árbol con n nodos tiene exactamente n-1 aristas."""
    arbol = {"raiz": ["a", "b"], "a": ["c", "d"], "b": ["e"], "c": [], "d": [], "e": []}
    nodos = len(arbol)
    aristas = sum(len(v) for v in arbol.values())
    profundidades = {"raiz": 0}
    pila = ["raiz"]
    while pila:
        n = pila.pop()
        for h in arbol[n]:
            profundidades[h] = profundidades[n] + 1
            pila.append(h)
    return {
        "nodos": nodos,
        "aristas": aristas,
        "n-1": nodos - 1,
        "es_arbol": aristas == nodos - 1,
        "hojas": [n for n, h in arbol.items() if not h],
        "altura": max(profundidades.values()),
        "profundidades": profundidades,
    }


def topological_order() -> dict:
    """Orden topológico y detección de ciclos por conteo de Kahn."""
    entrada = dict.fromkeys(_GRAFO, 0)
    for vecinos in _GRAFO.values():
        for v in vecinos:
            entrada[v] += 1
    listos = [n for n, g in entrada.items() if g == 0]
    orden = []
    while listos:
        n = listos.pop(0)
        orden.append(n)
        for v in _GRAFO[n]:
            entrada[v] -= 1
            if entrada[v] == 0:
                listos.append(v)
    return {
        "grafo": _GRAFO,
        "orden_topologico": orden,
        "es_DAG": len(orden) == len(_GRAFO),
        "nodos_ordenados": len(orden),
        "diagnostico_si_falla": "los nodos ausentes forman al menos un ciclo",
        "uso": "planificación de tareas, build systems y grafos de cómputo",
    }


def boolean_algebra() -> dict:
    """Álgebra booleana: simplificación y equivalencia funcional."""
    def original(a, b, c):
        return (a and b) or (a and not b) or (a and c)

    def simplificada(a, b, c):
        return a

    casos = list(product([True, False], repeat=3))
    return {
        "expresion": "(a∧b) ∨ (a∧¬b) ∨ (a∧c)",
        "simplificada": "a",
        "casos": len(casos),
        "equivalentes": all(original(*c) == simplificada(*c) for c in casos),
        "absorcion_a∨(a∧b)": all((a or (a and b)) == a for a, b, _ in casos),
        "puertas_ahorradas": 4,
    }


def modular_arithmetic() -> dict:
    """Aritmética modular: exponenciación rápida e inverso modular."""
    base, exp, mod = 7, 128, 13
    return {
        "7^128 mod 13": pow(base, exp, mod),
        "pequeño_teorema_de_fermat": pow(base, mod - 1, mod),
        "inverso_de_7_mod_13": pow(7, -1, 13),
        "verificacion_inverso": (7 * pow(7, -1, 13)) % 13,
        "suma_modular": (25 + 30) % 13,
        "usos": "hashing, criptografía, checksums y generadores pseudoaleatorios",
    }


def primes_gcd() -> dict:
    """Criba, MCD por Euclides y su relación con el mínimo común múltiplo."""
    limite = 50
    criba = [True] * (limite + 1)
    criba[0] = criba[1] = False
    for i in range(2, int(limite**0.5) + 1):
        if criba[i]:
            for j in range(i * i, limite + 1, i):
                criba[j] = False
    primos = [i for i, es in enumerate(criba) if es]
    a, b = 252, 198
    return {
        "primos_hasta_50": primos,
        "cantidad": len(primos),
        "a": a,
        "b": b,
        "mcd": math.gcd(a, b),
        "mcm": a * b // math.gcd(a, b),
        "mcd*mcm=a*b": math.gcd(a, b) * (a * b // math.gcd(a, b)) == a * b,
        "factorizacion_de_252": {2: 2, 3: 2, 7: 1},
    }


def capstone_dependency_graph() -> dict:
    """Capstone: planificar un pipeline con grafos y detectar dependencias rotas."""
    from collections import deque

    entrada = dict.fromkeys(_GRAFO, 0)
    for vecinos in _GRAFO.values():
        for v in vecinos:
            entrada[v] += 1
    cola = deque(sorted(n for n, g in entrada.items() if g == 0))
    orden, nivel = [], {n: 0 for n in _GRAFO if entrada[n] == 0}
    grados = dict(entrada)
    while cola:
        n = cola.popleft()
        orden.append(n)
        for v in _GRAFO[n]:
            grados[v] -= 1
            nivel[v] = max(nivel.get(v, 0), nivel[n] + 1)
            if grados[v] == 0:
                cola.append(v)

    con_ciclo = dict(_GRAFO)
    con_ciclo = {**con_ciclo, "evaluacion": ["limpieza"]}
    grados2 = dict.fromkeys(con_ciclo, 0)
    for vecinos in con_ciclo.values():
        for v in vecinos:
            grados2[v] += 1
    cola2 = deque(n for n, g in grados2.items() if g == 0)
    visitados = 0
    while cola2:
        n = cola2.popleft()
        visitados += 1
        for v in con_ciclo[n]:
            grados2[v] -= 1
            if grados2[v] == 0:
                cola2.append(v)

    etapas = {}
    for nodo, profundidad in nivel.items():
        etapas.setdefault(profundidad, []).append(nodo)
    return {
        "orden_de_ejecucion": orden,
        "niveles_paralelizables": {k: sorted(v) for k, v in sorted(etapas.items())},
        "pasos_secuenciales_minimos": max(nivel.values()) + 1,
        "tareas": len(_GRAFO),
        "grafo_con_ciclo_detectado": visitados < len(con_ciclo),
        "nodos_bloqueados_por_el_ciclo": len(con_ciclo) - visitados,
    }


DEMOS = {
    "propositional_logic": propositional_logic,
    "truth_tables": truth_tables,
    "predicate_logic": predicate_logic,
    "sets": sets,
    "relations": relations,
    "discrete_functions": discrete_functions,
    "counting_principles": counting_principles,
    "permutations_demo": permutations_demo,
    "combinations_demo": combinations_demo,
    "pigeonhole": pigeonhole,
    "induction": induction,
    "recurrences": recurrences,
    "graphs": graphs,
    "paths_connectivity": paths_connectivity,
    "trees": trees,
    "topological_order": topological_order,
    "boolean_algebra": boolean_algebra,
    "modular_arithmetic": modular_arithmetic,
    "primes_gcd": primes_gcd,
    "capstone_dependency_graph": capstone_dependency_graph,
}

CLASS_DEMOS = {
    "081": "propositional_logic",
    "082": "truth_tables",
    "083": "predicate_logic",
    "084": "sets",
    "085": "relations",
    "086": "discrete_functions",
    "087": "counting_principles",
    "088": "permutations_demo",
    "089": "combinations_demo",
    "090": "pigeonhole",
    "091": "induction",
    "092": "recurrences",
    "093": "graphs",
    "094": "paths_connectivity",
    "095": "trees",
    "096": "topological_order",
    "097": "boolean_algebra",
    "098": "modular_arithmetic",
    "099": "primes_gcd",
    "100": "capstone_dependency_graph",
}
