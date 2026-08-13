"""Genera las 360 clases, el catálogo, las rutas por perfil y las integraciones.

Todo lo que produce este script es artefacto derivado: no se edita a mano. Para
cambiar una clase se cambia el currículo o el motor de su parte y se vuelve a
ejecutar este script.

    python scripts/generate_classes.py            # regenera todo
    python scripts/generate_classes.py --check    # falla si algo está desfasado
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import content, curriculum, engines  # noqa: E402

REPOS_CONECTADOS = [
    ("artificial-intelligence-evolution-program", "evolución completa de la IA"),
    ("python-data-science-program", "ciencia de datos aplicada"),
    ("neural-network-training-labs", "entrenamiento de redes neuronales"),
    ("finance-and-banking-evolution-program", "finanzas cuantitativas"),
    ("blockchain-learning-path", "criptografía y sistemas distribuidos"),
    ("modern-cybersecurity-program", "seguridad ofensiva y defensiva"),
    ("modern-gamedev-program", "gráficos y simulación en videojuegos"),
    ("human-genome-labs", "bioinformática y genómica"),
]

# Rutas por perfil: partes obligatorias y clases-hito que las justifican.
RUTAS = [
    ("00-zero-to-mathematics", "De cero a la matemática",
     "Nunca te llevaste bien con las matemáticas y quieres empezar de verdad.",
     ["00", "01", "02", "03", "04"],
     ["001", "029", "043", "064", "091"],
     "Terminar sin miedo a una fórmula y con criterio para auditar un número."),
    ("01-software-engineer", "Ingeniería de software",
     "Programas a diario y quieres dejar de tratar los números como cajas negras.",
     ["01", "02", "04", "05", "11"],
     ["029", "032", "096", "114", "223"],
     "Entender precisión, complejidad, grafos y sistemas lineales en tu propio código."),
    ("02-data-scientist", "Ciencia de datos",
     "Trabajas con datos y quieres dejar de engañarte con tus propias métricas.",
     ["00", "02", "05", "09", "10", "14"],
     ["005", "186", "205", "207", "299"],
     "Distinguir un resultado real de un artefacto del muestreo o del leakage."),
    ("03-machine-learning-engineer", "Machine Learning",
     "Usas scikit-learn y quieres poder derivar lo que llamas.",
     ["05", "07", "09", "12", "14"],
     ["131", "215", "244", "289", "300"],
     "Derivar seis algoritmos clásicos desde su función objetivo y compararlos."),
    ("04-deep-learning-engineer", "Deep Learning",
     "Entrenas redes y quieres entender cada término de la actualización.",
     ["05", "07", "08", "12", "13", "15"],
     ["147", "179", "250", "263", "305", "320"],
     "Implementar backpropagation a mano y comprobar que coincide con autograd."),
    ("05-ai-engineer", "Ingeniería de IA",
     "Construyes sistemas con LLM y quieres entender qué ocurre dentro.",
     ["05", "06", "09", "13", "16"],
     ["103", "132", "321", "325", "330"],
     "Explicar atención, embeddings y muestreo sin recurrir a analogías."),
    ("06-ai-researcher", "Investigación en IA",
     "Lees papers y quieres reproducir su idea matemática, no solo citarlos.",
     ["08", "10", "12", "13", "16", "17"],
     ["179", "217", "332", "346", "353", "360"],
     "Reproducir la predicción cuantitativa de un paper con implementación propia."),
    ("07-finance", "Finanzas cuantitativas",
     "Modelas riesgo, carteras o precios y necesitas la matemática debajo.",
     ["00", "01", "07", "09", "10", "12"],
     ["005", "037", "194", "198", "218", "258"],
     "Modelar incertidumbre con dinero exacto, simulación y optimización con restricciones."),
    ("08-blockchain-cryptography", "Blockchain y criptografía",
     "Trabajas con criptografía y quieres su base en teoría de números y grafos.",
     ["01", "04", "09", "13"],
     ["025", "090", "098", "099", "262"],
     "Entender aritmética modular, colisiones y entropía como cotas, no como intuiciones."),
    ("09-cybersecurity", "Ciberseguridad",
     "Analizas amenazas y quieres cuantificar en lugar de estimar a ojo.",
     ["01", "04", "09", "10", "13"],
     ["081", "090", "186", "208", "262"],
     "Razonar con lógica, probabilidad base, errores tipo I/II y entropía."),
    ("10-game-development", "Desarrollo de videojuegos",
     "Haces gráficos, física o IA de juego y necesitas la geometría exacta.",
     ["01", "03", "05", "07", "11"],
     ["074", "077", "078", "080", "237"],
     "Construir un pipeline geométrico correcto y un integrador estable."),
    ("11-bioinformatics", "Bioinformática",
     "Analizas datos biológicos y necesitas estadística e inferencia sólidas.",
     ["04", "05", "09", "10", "14"],
     ["093", "135", "186", "211", "218"],
     "Aplicar grafos, reducción de dimensionalidad e inferencia con controles honestos."),
]

# Integraciones: repositorio → partes que le sirven de prerrequisito.
INTEGRACIONES = {
    "artificial-intelligence-evolution-program": (
        "Mapa maestro de la evolución de la IA.",
        ["04", "05", "08", "09", "12", "14", "15", "16"],
        [("Bayes y sistemas probabilísticos", "186"),
         ("Gradiente y entrenamiento", "244"),
         ("Backpropagation", "305"),
         ("Atención y Transformers", "325"),
         ("Modelos generativos", "331")],
    ),
    "python-data-science-program": (
        "Ciencia de datos aplicada con Python.",
        ["00", "02", "05", "09", "10", "14"],
        [("Estadística descriptiva", "201"),
         ("Intervalos de confianza", "205"),
         ("p-value bien interpretado", "207"),
         ("Regresión lineal", "214"),
         ("Leakage y validación", "299")],
    ),
    "neural-network-training-labs": (
        "Laboratorios prácticos de entrenamiento de redes.",
        ["05", "07", "08", "12", "13", "15"],
        [("Regla de la cadena", "147"),
         ("Autodiferenciación", "179"),
         ("Adam y AdamW", "250"),
         ("Cross-entropy", "263"),
         ("Convolución", "310")],
    ),
    "finance-and-banking-evolution-program": (
        "Finanzas, banca y riesgo.",
        ["00", "01", "07", "09", "10", "12"],
        [("Porcentajes y dinero exacto", "005"),
         ("Decimal frente a float", "037"),
         ("Distribución normal", "194"),
         ("Monte Carlo", "198"),
         ("Optimización cuadrática", "258")],
    ),
    "blockchain-learning-path": (
        "Criptografía, consenso y sistemas distribuidos.",
        ["01", "04", "09", "13"],
        [("Complemento a dos", "025"),
         ("Principio del palomar", "090"),
         ("Aritmética modular", "098"),
         ("Primos y MCD", "099"),
         ("Entropía", "262")],
    ),
    "modern-cybersecurity-program": (
        "Seguridad ofensiva y defensiva.",
        ["01", "04", "09", "10", "13"],
        [("Lógica proposicional", "081"),
         ("Colisiones garantizadas", "090"),
         ("Teorema de Bayes", "186"),
         ("Errores tipo I y II", "208"),
         ("Entropía y contraseñas", "262")],
    ),
    "modern-gamedev-program": (
        "Gráficos, física y simulación en videojuegos.",
        ["01", "03", "05", "07", "11"],
        [("Rotaciones 2D", "074"),
         ("Planos y 3D", "077"),
         ("Proyección y perspectiva", "078"),
         ("Motor geométrico", "080"),
         ("Runge-Kutta", "237")],
    ),
    "human-genome-labs": (
        "Bioinformática y genómica.",
        ["04", "05", "09", "10", "14"],
        [("Grafos", "093"),
         ("PCA", "135"),
         ("Bayes", "186"),
         ("Chi-cuadrado", "211"),
         ("Bootstrap", "218")],
    ),
}


def _demo_info(class_id: str) -> Dict[str, Any]:
    """Metadatos de la demostración ejecutable asociada a una clase."""
    nombre, funcion = engines.demo_for_class(class_id)
    doc = (funcion.__doc__ or "").strip().splitlines()
    resumen = doc[0].strip() if doc else ""
    resultado = funcion()
    claves = [k for k in resultado if isinstance(k, str)]
    return {
        "name": nombre,
        "summary": resumen,
        "keys": claves,
        "values": resultado,
        "n_keys": len(resultado),
    }


def _fmt_lista(items, prefijo="- ") -> str:
    return "\n".join(f"{prefijo}{item}" for item in items)


def _vecinos(clase):
    """Clase anterior y siguiente en el orden global del programa."""
    indice = int(clase["id"])
    anterior = curriculum.find_class(f"{indice - 1:03d}") if indice > 1 else None
    siguiente = curriculum.find_class(f"{indice + 1:03d}") if indice < 360 else None
    return anterior, siguiente


def _enlace_clase(clase, desde) -> str:
    """Enlace relativo desde el directorio de ``desde`` al de ``clase``."""
    if clase is None:
        return ""
    destino = curriculum.class_dir(clase)
    origen = curriculum.class_dir(desde)
    return f"{os.path.relpath(destino, origen).replace(os.sep, '/')}/README.md"


def _navegacion(clase, parte) -> str:
    anterior, siguiente = _vecinos(clase)
    piezas = []
    if anterior:
        piezas.append(f"[⬅️ {anterior['id']} {anterior['title']}]({_enlace_clase(anterior, clase)})")
    piezas.append(f"[📚 Parte {parte['id']}](../README.md)")
    piezas.append("[🏠 Programa](../../../README.md)")
    if siguiente:
        piezas.append(f"[{siguiente['id']} {siguiente['title']} ➡️]({_enlace_clase(siguiente, clase)})")
    return " · ".join(piezas)


def _clasifica_salidas(demo):
    """Agrupa las claves de la demostración en parámetros, resultados y verificaciones."""
    verificaciones, numericos, otros = [], [], []
    for clave, valor in demo["values"].items():
        if isinstance(valor, bool):
            verificaciones.append(clave)
        elif isinstance(valor, (int, float)):
            numericos.append(clave)
        else:
            otros.append(clave)
    return verificaciones, numericos, otros


def _diagrama_clase(clase, parte, demo) -> str:
    """Diagrama del flujo del laboratorio, construido con sus salidas reales."""
    verificaciones, numericos, otros = _clasifica_salidas(demo)
    anterior, siguiente = _vecinos(clase)
    prev = f"{anterior['id']}<br/>{_wrap(anterior['title'], 22)}" if anterior else "Diagnóstico<br/>inicial"
    nxt = f"{siguiente['id']}<br/>{_wrap(siguiente['title'], 22)}" if siguiente else "Fin del<br/>programa"

    def muestra(claves, n=3):
        if not claves:
            return "—"
        visibles = [c.replace('"', "'") for c in claves[:n]]
        extra = f"<br/>… +{len(claves) - n} más" if len(claves) > n else ""
        return "<br/>".join(visibles) + extra

    return f"""```mermaid
flowchart LR
    P["{prev}"] --> C
    subgraph C["{clase['id']} · {_wrap(clase['title'], 26)}"]
        direction TB
        D["Demostración<br/><code>{demo['name']}</code>"] --> R["Resultados numéricos<br/>{muestra(numericos)}"]
        D --> V["Verificaciones<br/>{muestra(verificaciones)}"]
        D --> O["Contexto y estructura<br/>{muestra(otros)}"]
    end
    C --> N["{nxt}"]
    C -.-> IA["Uso en IA<br/>parte {parte['id']}"]
```"""


def _wrap(texto, ancho):
    """Parte un texto en líneas para que quepa dentro de un nodo Mermaid."""
    palabras = texto.replace('"', "").replace("(", "").replace(")", "").split()
    lineas, actual = [], ""
    for palabra in palabras:
        if len(actual) + len(palabra) + 1 > ancho and actual:
            lineas.append(actual)
            actual = palabra
        else:
            actual = f"{actual} {palabra}".strip()
    if actual:
        lineas.append(actual)
    return "<br/>".join(lineas)


def _readme(clase, parte, demo) -> str:
    registro = content.class_content(clase["id"])
    idea = parte["key_ideas"][(clase["index_in_part"] - 1) % len(parte["key_ideas"])]
    error_parte = parte["pitfalls"][(clase["index_in_part"] - 1) % len(parte["pitfalls"])]
    verificaciones, numericos, _ = _clasifica_salidas(demo)
    nav = _navegacion(clase, parte)

    bloques = [
        f"# {clase['id']} — {clase['title']}",
        "",
        f"> {nav}",
        "",
        f"**Parte:** {parte['id']} — {parte['title']} · **Nivel:** `{parte['level']}` · "
        f"**Horas estimadas:** 4",
        f"**Motor:** `engines.{parte['engine']}` · **Demostración:** `{demo['name']}` · "
        f"**Clase {clase['index_in_part']} de {len(parte['classes'])}** de la parte",
        "",
        "---",
        "",
        "## 🎯 Propósito",
        "",
    ]

    if registro.get("concepto"):
        bloques += [
            f"**{registro['concepto']}**",
            "",
            f"{parte['summary']}",
            "",
        ]
    else:
        bloques += [
            parte["summary"],
            "",
            f"Esta clase concreta ese objetivo sobre **{clase['title']}**: qué es, cómo se",
            "calcula a mano, cómo se implementa sin ocultar el procedimiento y cómo se verifica",
            "que el resultado es correcto y no solo plausible.",
            "",
        ]

    bloques += [
        "## ✅ Resultados de aprendizaje",
        "",
        "Al terminar podrás:",
        "",
        f"1. Explicar **{clase['title']}** con lenguaje cotidiano y con notación matemática.",
        "2. Resolver un caso pequeño a mano y anticipar el orden de magnitud del resultado.",
        f"3. Ejecutar y modificar `lab.py`, que corre la demostración `{demo['name']}`.",
        f"4. Interpretar las {demo['n_keys']} salidas del laboratorio y decir qué comprueba cada una.",
        f"5. Detectar el error típico de esta parte: {error_parte.lower().rstrip('.')}.",
        "",
    ]

    if registro.get("formulas"):
        bloques += [
            "## 🧩 Fórmulas de la clase",
            "",
            "```text",
            *registro["formulas"],
            "```",
            "",
        ]

    bloques += [
        "## 🗺️ Ubicación en el programa",
        "",
        _diagrama_clase(clase, parte, demo),
        "",
    ]

    if registro.get("desarrollo"):
        bloques += ["## 📖 Fundamentos", "", registro["desarrollo"].rstrip(), ""]
    else:
        bloques += [
            f"## 🧠 Idea rectora de la parte {parte['id']}",
            "",
            f"> {idea}",
            "",
        ]

    if registro.get("ejemplo"):
        bloques += ["## 🧮 Ejemplo trabajado", "", registro["ejemplo"].rstrip(), ""]

    bloques += [
        "## 🔬 Qué ejecuta el laboratorio",
        "",
        f"`{demo['name']}` — {demo['summary']}",
        "",
        "| Grupo | Salidas |",
        "|---|---|",
        f"| 🔢 Resultados numéricos ({len(numericos)}) | "
        + (", ".join(f"`{k}`" for k in numericos) if numericos else "—") + " |",
        f"| ✅ Comprobaciones de invariante ({len(verificaciones)}) | "
        + (", ".join(f"`{k}`" for k in verificaciones) if verificaciones else "—") + " |",
        "",
        "Las claves booleanas no son adorno: si alguna fuera `False`, el resultado numérico",
        "no sería fiable aunque el programa terminase sin error.",
        "",
        "```bash",
        f"python classes/part-{parte['id']}-{parte['slug']}/{clase['slug']}/lab.py",
        f"compmath run {clase['id']}",
        "```",
        "",
        "> [!TIP]",
        "> Antes de ejecutar, **escribe tu predicción**. Un laboratorio que confirma lo que",
        "> esperabas enseña tanto como uno que te contradice, pero solo si la predicción",
        "> existía antes del resultado.",
        "",
    ]

    if registro.get("errores"):
        bloques += ["## ⚠️ Errores conceptuales frecuentes", ""]
        bloques += [f"{i}. {e}" for i, e in enumerate(registro["errores"], start=1)]
        bloques.append("")
    else:
        bloques += ["## ⚠️ Errores frecuentes en esta parte", "", _fmt_lista(parte["pitfalls"]), ""]

    if registro.get("aplicacion"):
        bloques += ["## 🚀 Dónde se usa de verdad", "", registro["aplicacion"].rstrip(), ""]

    bloques += [
        "## 🤖 Conexión con IA",
        "",
        parte["ai_link"],
        "",
        "## 📓 Notebooks",
        "",
        "| Archivo | Para qué |",
        "|---|---|",
        "| [`notebook.ipynb`](notebook.ipynb) | recorrido guiado con la demostración ejecutada |",
        "| [`notebook_student.ipynb`](notebook_student.ipynb) | versión con `TODO` para resolver |",
        "| [`notebook_solution.ipynb`](notebook_solution.ipynb) | solución de referencia verificada |",
        "",
        "## 📝 Evaluación",
        "",
        "| Criterio | Peso |",
        "|---|---:|",
        "| Comprensión conceptual | 25 % |",
        "| Resolución manual | 25 % |",
        "| Implementación y verificación | 25 % |",
        "| Interpretación y comunicación | 15 % |",
        "| Conexión con aplicación real | 10 % |",
        "",
        "Detalle y criterios de error crítico en [`assessment.md`](assessment.md).",
        "",
        "## ❓ Preguntas de comprobación",
        "",
        "1. ¿Cuál es la entrada, cuál la salida y qué unidades tienen?",
        "2. ¿Qué operación domina el comportamiento del resultado?",
        "3. ¿Qué caso extremo revelaría un error conceptual?",
        "4. ¿Cómo verificarías el resultado por un método independiente?",
        f"5. ¿Dónde aparece esto en {parte['applications'].split(',')[0]}?",
        "",
        "Si necesitas releer el código para responderlas, la clase todavía no está superada.",
        "",
        "## 📥 Entregable",
        "",
        "`notebook_student.ipynb` resuelto más un párrafo que explique el resultado **sin citar",
        "código**: qué entra, qué sale, qué invariante se comprueba y qué pasaría en un caso límite.",
        "",
        "## 🔗 Referencias",
        "",
    ]

    if registro.get("referencias"):
        bloques += [_fmt_lista(registro["referencias"]), ""]
        bloques += ["Bibliografía completa de la parte en [`../../../docs/BIBLIOGRAPHY.md`](../../../docs/BIBLIOGRAPHY.md).", ""]
    else:
        bloques += [_fmt_lista(parte["references"]), ""]

    bloques += [
        "## 📂 Material de la clase",
        "",
        "[`intuition.md`](intuition.md) · [`theory.md`](theory.md) · [`derivation.md`](derivation.md) · "
        "[`exercises.md`](exercises.md) · [`assessment.md`](assessment.md) · "
        "[`where-is-this-used.md`](where-is-this-used.md) · [`lesson.yaml`](lesson.yaml)",
        "",
        "---",
        "",
        f"> {nav}",
        "",
    ]
    return "\n".join(bloques)


def _intuition(clase, parte, demo) -> str:
    return f"""# Intuición — {clase['title']}

## La pregunta antes de la fórmula

¿Qué problema resuelve **{clase['title']}**? Describe, sin símbolos, qué entra,
qué sale y cómo debería cambiar el resultado si una entrada crece, decrece o se
vuelve extrema. Si no puedes decirlo en una frase, todavía no entiendes el objeto:
entiendes su notación.

## Dónde encaja

Esta clase pertenece a **{parte['title']}**. {parte['summary']}

## Analogía y sus límites

Construye una analogía cotidiana y, en la línea siguiente, escribe dónde deja de
funcionar. Una analogía sin límites declarados produce confianza sin comprensión.

## Predicción antes del laboratorio

El laboratorio ejecuta `{demo['name']}`: {demo['summary'].lower()}

Antes de correrlo, predice tres casos:

1. **Normal** — la situación típica.
2. **Límite** — el valor extremo del dominio válido.
3. **Inválido** — una entrada fuera del dominio, y qué debería ocurrir.

Después compara con las salidas reales. Registra las tres predicciones en el
notebook antes de ejecutar nada.

## Señal de que lo entendiste

Puedes explicar por qué el resultado es el que es **sin volver a mirar el código**,
y puedes construir un caso donde tu explicación falle.
"""


def _theory(clase, parte, demo) -> str:
    ideas = _fmt_lista(parte["key_ideas"])
    return f"""# Teoría — {clase['title']}

## Definición operativa

En esta clase, **{clase['title']}** se trata como un objeto con tres capas
separadas:

| Capa | Qué es | Qué puede fallar |
|---|---|---|
| Modelo matemático | la definición ideal, con su dominio | supuestos no declarados |
| Algoritmo | el procedimiento que la calcula | complejidad y criterio de parada |
| Representación en máquina | los bits que la almacenan | redondeo, desbordamiento, cancelación |

Dos implementaciones del mismo modelo pueden diferir numéricamente sin que
ninguna esté equivocada. Reconocer en qué capa está la diferencia es parte del
contenido de esta clase.

## Ideas centrales de la parte {parte['id']}

{ideas}

## Propiedades a estudiar

- dominio de validez y qué ocurre en su frontera;
- invariantes que la operación debe conservar;
- unidades o escala de cada cantidad;
- sensibilidad a perturbaciones pequeñas de la entrada;
- coste computacional y cómo crece con el tamaño del problema;
- relación con las clases previas de esta misma parte.

## Herramientas de referencia

Este programa implementa el procedimiento con biblioteca estándar para que
ningún paso quede oculto. En la práctica profesional se usa: {', '.join(parte['stack'])}.

Usar la biblioteca no sustituye entender el procedimiento: sirve para poder
**auditar** su salida y reconocer cuándo devuelve un número correcto por la razón
equivocada.

## Verificación

El laboratorio (`{demo['name']}`) devuelve {demo['n_keys']} valores. Varios de ellos
existen únicamente para comprobar una identidad o un invariante: identifícalos y
explica qué se rompería si esa comprobación fallara.

## Aplicación

{parte['applications'].capitalize()}.
"""


def _derivation(clase, parte, demo) -> str:
    return f"""# Derivación y razonamiento — {clase['title']}

## Método

1. **Declara símbolos y supuestos.** Toda letra necesita significado, unidad y dominio.
2. **Parte de una relación conocida** —definición, identidad previa o algoritmo base.
3. **Transforma un paso por línea.** Ningún paso debe requerir «se ve fácilmente».
4. **Justifica cada transformación** nombrando la propiedad que la autoriza.
5. **Verifica dimensiones, signos y casos límite** antes de aceptar el resultado.
6. **Contrasta con un cálculo numérico pequeño** que puedas comprobar a mano.

## Ejercicio de derivación

Construye una derivación de 5 a 10 pasos relacionada con **{clase['title']}**.
Si el tema no admite una fórmula cerrada, deriva en su lugar:

- el **algoritmo** (por qué cada paso acerca a la solución), o
- la **regla de decisión** (qué garantiza la elección que hace), o
- la **cota de error** (por qué el resultado está a cierta distancia del valor exacto).

## Contraste con el laboratorio

La demostración `{demo['name']}` recorre este mismo razonamiento en código.
Después de derivarlo a mano, lee la implementación en
`src/computational_math/engines/{parte['engine']}.py` y responde:

- ¿Qué línea del código corresponde a cada paso de tu derivación?
- ¿Hay algún paso que el código resuelve de forma distinta a la tuya?
- ¿Alguna decisión del código (tolerancia, orden de operaciones, semilla) no
  aparece en la matemática pura? ¿Por qué está ahí?

## Trampa habitual de esta parte

{parte['pitfalls'][0]}

Una derivación correcta que ignora esta trampa produce código incorrecto.
"""


def _exercises(clase, parte, demo) -> str:
    return f"""# Ejercicios — {clase['title']}

## Básico

1. Define **{clase['title']}** con tus palabras y da un ejemplo válido y uno inválido.
2. Resuelve un caso a mano con números pequeños y deja escrito cada paso intermedio.
3. Construye un caso límite y **predice la salida antes de ejecutar** el laboratorio.

## Intermedio

4. Ejecuta `lab.py` y explica qué comprueba cada una de sus {demo['n_keys']} salidas.
5. Modifica un parámetro de entrada del motor y describe cómo cambia el resultado
   y por qué; contrasta con tu predicción.
6. Reimplementa el cálculo por un camino distinto y mide el error absoluto y el
   relativo entre ambas versiones. Declara la tolerancia que consideras aceptable
   y justifícala.

## Avanzado

7. Conecta esta clase con {parte['applications']} mediante un caso concreto y realista.
8. Escribe un test que **falle** ante una implementación ingenua pero pase con la correcta.
9. Cambia una hipótesis del problema (dominio, escala, independencia, precisión) y
   analiza qué conclusión deja de ser válida.
10. Explica el concepto en 200 palabras a alguien que sabe programar pero no
    conoce esta parte, sin perder rigor y sin usar la palabra «simplemente».

## Reto de la parte {parte['id']}

{parte['ai_link']}

Escribe qué operación concreta de un modelo de IA dejaría de funcionar si este
concepto estuviera mal implementado, y cómo se manifestaría el fallo.
"""


def _assessment(clase, parte, demo) -> str:
    return f"""# Evaluación — {clase['title']}

## Rúbrica

| Criterio | Peso | Evidencia esperada |
|---|---:|---|
| Comprensión conceptual | 25 % | explica el objeto, su dominio y sus límites sin recurrir al código |
| Resolución manual | 25 % | caso pequeño resuelto paso a paso, con supuestos declarados |
| Implementación y verificación | 25 % | ejecuta `{demo['name']}`, interpreta sus salidas y comprueba al menos un invariante |
| Interpretación y comunicación | 15 % | explica el resultado, su error y su tolerancia |
| Conexión con aplicación real | 10 % | vincula la clase con {parte['applications'].split(',')[0]} o con IA |

## Aprobación

**80/100 y ningún error conceptual crítico.**

Se considera error conceptual crítico:

- confundir el modelo matemático con su representación en máquina;
- afirmar exactitud sin declarar tolerancia;
- generalizar a partir de un único caso favorable;
- {parte['pitfalls'][0].lower().rstrip('.')}.

## Preguntas de comprobación

1. ¿Cuál es la entrada, cuál es la salida y qué unidades tienen?
2. ¿Qué operación domina el comportamiento del resultado?
3. ¿Qué caso extremo revelaría un error conceptual?
4. ¿Cómo verificarías el cálculo por un método independiente?
5. ¿Dónde aparece este concepto en {parte['applications'].split(',')[0]}?

## Autoevaluación honesta

Si respondes «sí» a la siguiente pregunta, la clase **no** está superada:
*¿necesito volver a mirar el código para explicar por qué el resultado es ese?*
"""


def _where_used(clase, parte, demo) -> str:
    repos = "\n".join(f"- [`{nombre}`](https://github.com/vladimiracunadev-create/{nombre}) — {desc}"
                      for nombre, desc in REPOS_CONECTADOS)
    return f"""# ¿Dónde se usa {clase['title']}?

## En computación

{parte['summary']}

Concretamente, **{clase['title']}** aparece siempre que un programa necesita
representar, calcular o verificar el objeto que esta clase define. El laboratorio
`{demo['name']}` muestra la versión mínima ejecutable de ese uso.

## En IA y Machine Learning

{parte['ai_link']}

Las partes 14 a 17 del programa consumen directamente este contenido. Si esta
clase es un prerrequisito de una operación concreta de un modelo, escríbelo:
nombrar la dependencia es parte del ejercicio.

## En otros dominios

{parte['applications'].capitalize()}.

## Repositorios conectados

Este programa **no reemplaza** ninguno de los siguientes: los referencia como
superficies de aplicación de la matemática que aquí se enseña.

{repos}

## Advertencia de alcance

Que un concepto aparezca en un dominio no significa que esta clase agote su
tratamiento en él. Cada campo añade convenciones, restricciones y literatura
propia que este programa no sustituye.
"""


def _lesson_yaml(clase, parte, demo) -> str:
    archivos = "\n".join(f"  - {f}" for f in curriculum.CLASS_FILES)
    conceptos = "\n".join(f'  - "{k}"' for k in demo["keys"][:8])
    return f"""id: "{clase['id']}"
title: "{clase['title']}"
part: "{parte['id']}"
part_title: "{parte['title']}"
level: "{parte['level']}"
index_in_part: {clase['index_in_part']}
hours: 4
engine: "{parte['engine']}"
demo: "{demo['name']}"
demo_summary: "{demo['summary'].replace('"', "'")}"
prerequisite: "{'diagnóstico inicial' if clase['id'] == '001' else f'clase {int(clase["id"]) - 1:03d}'}"
outputs:
{conceptos}
artifacts:
{archivos}
"""


def _lab(clase, parte, demo) -> str:
    return f'''"""Laboratorio {clase['id']} — {clase['title']}.

Parte {parte['id']} · {parte['title']}
Motor: computational_math.engines.{parte['engine']} · demostración `{demo['name']}`

{demo['summary']}

Ciclo de trabajo: predicción → cálculo → verificación → interpretación.
Escribe tu predicción antes de ejecutar; solo entonces el resultado enseña algo.

Ejecutar:
    python lab.py
    compmath run {clase['id']}
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):  # consolas Windows sin UTF-8
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from computational_math.engines import {parte['engine']} as motor  # noqa: E402

DEMO = "{demo['name']}"


def main() -> dict:
    """Ejecuta la demostración de la clase y muestra sus resultados."""
    resultado = motor.DEMOS[DEMO]()
    print(f"Clase {clase['id']} — {clase['title']}")
    print(f"Parte {parte['id']} · {parte['title']}")
    print(f"Demostración: {{DEMO}} — {{motor.DEMOS[DEMO].__doc__.strip().splitlines()[0]}}")
    print("-" * 72)
    print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))
    return resultado


if __name__ == "__main__":
    salida = main()
    assert isinstance(salida, dict) and salida, "la demostración debe devolver resultados"
'''


def _cell_md(lineas):
    return {"cell_type": "markdown", "metadata": {}, "source": lineas}


def _cell_code(lineas):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": lineas}


def _nb(cells) -> str:
    documento = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    return json.dumps(documento, indent=1, ensure_ascii=False) + "\n"


_BOOTSTRAP = [
    "import json, sys\n",
    "from pathlib import Path\n",
    "ROOT = Path.cwd()\n",
    "while ROOT != ROOT.parent and not (ROOT / 'curriculum.yaml').exists():\n",
    "    ROOT = ROOT.parent\n",
    "sys.path.insert(0, str(ROOT / 'src'))\n",
]


def _notebook_recorrido(clase, parte, demo) -> str:
    return _nb([
        _cell_md([
            f"# {clase['id']} — {clase['title']}\n",
            "\n",
            f"**Parte {parte['id']} · {parte['title']}** · nivel `{parte['level']}`\n",
            "\n",
            f"Notebook de recorrido. Ejecuta la demostración `{demo['name']}` del motor "
            f"`{parte['engine']}` y comenta cada salida.\n",
        ]),
        _cell_md([
            "## 1. Contexto\n",
            "\n",
            f"{parte['summary']}\n",
            "\n",
            f"> {parte['key_ideas'][(clase['index_in_part'] - 1) % len(parte['key_ideas'])]}\n",
        ]),
        _cell_code(_BOOTSTRAP + [
            f"from computational_math.engines import {parte['engine']} as motor\n",
            f"demo = motor.DEMOS['{demo['name']}']\n",
            "print(demo.__doc__)\n",
        ]),
        _cell_md([
            "## 2. Ejecución\n",
            "\n",
            "Antes de ejecutar la celda siguiente, escribe aquí tu predicción:\n",
            "\n",
            "- Caso normal:\n",
            "- Caso límite:\n",
            "- Caso inválido:\n",
        ]),
        _cell_code([
            "resultado = demo()\n",
            "print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))\n",
        ]),
        _cell_md([
            "## 3. Lectura de las salidas\n",
            "\n",
            f"La demostración devuelve {demo['n_keys']} valores. Identifica cuáles son "
            "**resultados** y cuáles son **comprobaciones de invariante**.\n",
        ]),
        _cell_code([
            "for clave, valor in resultado.items():\n",
            "    tipo = type(valor).__name__\n",
            "    print(f'{clave:45s} {tipo:10s} {str(valor)[:60]}')\n",
        ]),
        _cell_md([
            "## 4. Fuente\n",
            "\n",
            "Lee la implementación y localiza dónde ocurre cada paso del razonamiento.\n",
        ]),
        _cell_code([
            "import inspect\n",
            "print(inspect.getsource(demo))\n",
        ]),
        _cell_md([
            "## 5. Reflexión\n",
            "\n",
            "Responde sin volver a mirar el código:\n",
            "\n",
            "1. ¿Qué supuesto hiciste?\n",
            "2. ¿Cómo verificaste el cálculo por un camino independiente?\n",
            "3. ¿Qué cambiaría en un caso límite?\n",
            f"4. Error a evitar en esta parte: *{parte['pitfalls'][0]}*\n",
        ]),
    ])


def _notebook_student(clase, parte, demo) -> str:
    return _nb([
        _cell_md([
            f"# {clase['id']} — {clase['title']} · versión estudiante\n",
            "\n",
            "Completa las celdas marcadas con `TODO`. No borres las comprobaciones.\n",
            "\n",
            f"**Parte {parte['id']} · {parte['title']}**\n",
        ]),
        _cell_md([
            "## 1. Predicción (obligatoria antes de ejecutar)\n",
            "\n",
            "| Caso | Tu predicción | Resultado real | ¿Acertaste? |\n",
            "|---|---|---|---|\n",
            "| Normal |  |  |  |\n",
            "| Límite |  |  |  |\n",
            "| Inválido |  |  |  |\n",
        ]),
        _cell_code(_BOOTSTRAP + [
            "# TODO: importa el motor de la parte y localiza la demostración de esta clase.\n",
            f"# Pista: from computational_math.engines import {parte['engine']} as motor\n",
            "motor = None\n",
            f"DEMO = '{demo['name']}'\n",
        ]),
        _cell_code([
            "# TODO: ejecuta la demostración y guarda el resultado en `resultado`.\n",
            "resultado = None\n",
            "assert isinstance(resultado, dict) and resultado, 'la demostración debe devolver un dict no vacío'\n",
        ]),
        _cell_md([
            "## 2. Interpretación\n",
            "\n",
            f"Explica al menos **tres** de las {demo['n_keys']} salidas: qué mide cada una y "
            "qué se rompería si su valor fuera distinto.\n",
            "\n",
            "1. \n",
            "2. \n",
            "3. \n",
        ]),
        _cell_code([
            "# TODO: elige una salida numérica y comprueba su valor por un camino independiente.\n",
            "# Declara explícitamente la tolerancia que usas y por qué.\n",
            "import math\n",
            "TOLERANCIA = 1e-9   # TODO: justifica esta elección\n",
        ]),
        _cell_md([
            "## 3. Caso límite\n",
            "\n",
            "Modifica una entrada del motor (copia la función y cámbiala) hasta encontrar un\n",
            "caso donde el resultado deje de ser fiable. Describe qué ocurrió.\n",
        ]),
        _cell_code([
            "# TODO: reproduce aquí el caso límite.\n",
        ]),
        _cell_md([
            "## 4. Entregable\n",
            "\n",
            "Escribe un párrafo que explique el resultado **sin citar código**: qué entra,\n",
            "qué sale, qué invariante se comprueba y qué pasaría en un caso extremo.\n",
            "\n",
            "> _Tu párrafo aquí._\n",
        ]),
    ])


def _notebook_solution(clase, parte, demo) -> str:
    return _nb([
        _cell_md([
            f"# {clase['id']} — {clase['title']} · solución de referencia\n",
            "\n",
            "Solución ejecutable. Compárala con la tuya **después** de intentarlo.\n",
            "\n",
            f"**Parte {parte['id']} · {parte['title']}** · motor `{parte['engine']}`\n",
        ]),
        _cell_code(_BOOTSTRAP + [
            f"from computational_math.engines import {parte['engine']} as motor\n",
            f"DEMO = '{demo['name']}'\n",
            "demo = motor.DEMOS[DEMO]\n",
            "resultado = demo()\n",
            "assert isinstance(resultado, dict) and resultado\n",
            f"assert len(resultado) == {demo['n_keys']}, 'la demostración cambió de forma'\n",
            "print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))\n",
        ]),
        _cell_md([
            "## Interpretación de las salidas\n",
            "\n",
            f"`{demo['name']}` — {demo['summary']}\n",
            "\n",
            "Las claves booleanas son comprobaciones de invariante: si alguna fuera `False`,\n",
            "el resultado numérico no sería fiable aunque el código se ejecutase sin error.\n",
        ]),
        _cell_code([
            "invariantes = {k: v for k, v in resultado.items() if isinstance(v, bool)}\n",
            "numericos = {k: v for k, v in resultado.items() if isinstance(v, (int, float))}\n",
            "print('invariantes comprobados:', len(invariantes))\n",
            "for k, v in invariantes.items():\n",
            "    print(f'  {\"OK \" if v else \"REVISAR\"} {k}')\n",
            "print('valores numéricos:', len(numericos))\n",
        ]),
        _cell_code([
            "# Reproducibilidad: la demostración es determinista.\n",
            "assert demo() == resultado, 'la demostración debe ser reproducible'\n",
            "print('Reproducible: dos ejecuciones devuelven exactamente lo mismo.')\n",
        ]),
        _cell_md([
            "## Idea que hay que llevarse\n",
            "\n",
            f"> {parte['key_ideas'][(clase['index_in_part'] - 1) % len(parte['key_ideas'])]}\n",
            "\n",
            "**Error a evitar:** "
            f"{parte['pitfalls'][(clase['index_in_part'] - 1) % len(parte['pitfalls'])]}\n",
            "\n",
            f"**Conexión con IA:** {parte['ai_link']}\n",
        ]),
    ])


def _emoji_parte(part_id: str) -> str:
    return {
        "00": "🔢", "01": "💾", "02": "📐", "03": "📏", "04": "🧩", "05": "🟪",
        "06": "🔷", "07": "📈", "08": "🌐", "09": "🎲", "10": "📊", "11": "🧮",
        "12": "⚙️", "13": "📡", "14": "🤖", "15": "🧠", "16": "🛰️", "17": "🔭",
    }.get(part_id, "📚")


def _mermaid_secuencia(parte, clases) -> str:
    """Diagrama de la secuencia de las 20 clases de la parte, agrupadas de cinco en cinco."""
    lineas = ["```mermaid", "flowchart LR"]
    grupos = [clases[i:i + 5] for i in range(0, len(clases), 5)]
    for indice, grupo in enumerate(grupos, start=1):
        lineas.append(f'    subgraph B{indice}["Bloque {indice}"]')
        lineas.append("        direction TB")
        for clase in grupo:
            lineas.append(f'        L{clase["id"]}["{clase["id"]}<br/>{_wrap(clase["title"], 24)}"]')
        for a, b in zip(grupo, grupo[1:]):
            lineas.append(f'        L{a["id"]} --> L{b["id"]}')
        lineas.append("    end")
    for a, b in zip(grupos, grupos[1:]):
        lineas.append(f'    L{a[-1]["id"]} --> L{b[0]["id"]}')
    lineas.append("```")
    return "\n".join(lineas)


def _tabla_clases_parte(parte, clases) -> str:
    filas = []
    for clase in clases:
        demo, funcion = engines.demo_for_class(clase["id"])
        resumen = (funcion.__doc__ or "").strip().splitlines()[0]
        registro = content.class_content(clase["id"])
        concepto = registro.get("concepto") or resumen
        filas.append(
            f"| `{clase['id']}` | [{clase['title']}]({clase['slug']}/README.md) "
            f"| `{demo}` | {concepto} |"
        )
    return "\n".join(filas)


def _part_readme(parte, clases) -> str:
    extra = content.part_content(parte["id"])
    partes = curriculum.parts()
    idx = [p["id"] for p in partes].index(parte["id"])
    anterior = partes[idx - 1] if idx > 0 else None
    siguiente = partes[idx + 1] if idx < len(partes) - 1 else None

    nav = []
    if anterior:
        nav.append(f"[⬅️ Parte {anterior['id']} — {anterior['title']}](../part-{anterior['id']}-{anterior['slug']}/README.md)")
    nav.append("[🏠 Programa](../../README.md)")
    nav.append("[📇 Catálogo](../README.md)")
    if siguiente:
        nav.append(f"[Parte {siguiente['id']} — {siguiente['title']} ➡️](../part-{siguiente['id']}-{siguiente['slug']}/README.md)")
    navegacion = " · ".join(nav)

    bloques = [
        f"# {_emoji_parte(parte['id'])} Parte {parte['id']} — {parte['title']}",
        "",
        f"> {navegacion}",
        "",
        f"**Nivel:** `{parte['level']}` · **Clases:** {len(clases)} · "
        f"**Horas estimadas:** {len(clases) * 4} · **Motor:** "
        f"[`{parte['engine']}.py`](../../src/computational_math/engines/{parte['engine']}.py)",
        "",
        "---",
        "",
        "## 🎯 De qué trata esta parte",
        "",
        parte["summary"],
        "",
    ]

    if extra.get("resumen_extendido"):
        bloques += [extra["resumen_extendido"].rstrip(), ""]

    if extra.get("mapa"):
        bloques += [
            "## 🗺️ Mapa conceptual",
            "",
            "```mermaid",
            extra["mapa"].rstrip(),
            "```",
            "",
        ]

    bloques += [
        "## 🧠 Ideas centrales",
        "",
        _fmt_lista(parte["key_ideas"]),
        "",
        "## 🤖 Por qué importa en IA",
        "",
        "> [!IMPORTANT]",
        f"> {parte['ai_link']}",
        "",
        "## ⚠️ Errores frecuentes de esta parte",
        "",
        _fmt_lista(parte["pitfalls"]),
        "",
        "## 🧭 Secuencia de la parte",
        "",
        _mermaid_secuencia(parte, clases),
        "",
        "## 📚 Las clases",
        "",
        "| # | Clase | Demostración | Idea central |",
        "|---|---|---|---|",
        _tabla_clases_parte(parte, clases),
        "",
    ]

    if extra.get("glosario"):
        bloques += [
            f"## 📖 Glosario de la parte ({len(extra['glosario'])} términos)",
            "",
            "Definiciones precisas en [`GLOSARIO.md`](GLOSARIO.md).",
            "",
        ]

    bloques += [
        "## 🧰 Stack de referencia",
        "",
        ", ".join(f"`{s}`" for s in parte["stack"]),
        "",
        "Los laboratorios se ejecutan con biblioteca estándar; estas herramientas aparecen",
        "como contraste profesional, no como requisito.",
        "",
        "## 🧪 Ejecutar toda la parte",
        "",
        "```bash",
        f"compmath run --part {parte['id']}",
        f"compmath catalog --part {parte['id']}",
        "```",
        "",
        "## 📊 Evaluación de la parte",
        "",
        "| Componente | Peso |",
        "|---|---:|",
        "| Clases y ejercicios | 40 % |",
        "| Laboratorios y notebooks | 25 % |",
        "| Explicación oral o escrita | 15 % |",
        f"| Capstone ([{clases[-1]['id']}]({clases[-1]['slug']}/README.md)) | 20 % |",
        "",
        "## 📖 Bibliografía",
        "",
        _fmt_lista(parte["references"]),
        "",
        "---",
        "",
        f"> {navegacion}",
        "",
    ]
    return "\n".join(bloques)


def _glosario_parte(parte, clases) -> str:
    terminos = content.glossary(parte["id"])
    if not terminos:
        return ""
    filas = []
    for item in sorted(terminos, key=lambda t: t["termino"].lower()):
        clase_id = item.get("clase")
        if clase_id:
            clase = curriculum.find_class(clase_id)
            enlace = f"[{clase_id}]({clase['slug']}/README.md)"
        else:
            enlace = "—"
        filas.append(f"| **{item['termino']}** | {item['definicion']} | {enlace} |")
    return f"""# 📖 Glosario — Parte {parte['id']}: {parte['title']}

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

{len(terminos)} términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
{chr(10).join(filas)}

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
"""


def _tabla_de_partes(ids, prefijo="..") -> str:
    filas = []
    for pid in ids:
        parte = curriculum.part(pid)
        filas.append(
            f"| {parte['id']} | [{parte['title']}]({prefijo}/classes/part-{parte['id']}-{parte['slug']}/README.md) "
            f"| {len(parte['classes'])} | {len(parte['classes']) * 4} h | {parte['level']} |"
        )
    return "\n".join(filas)


def _tabla_de_hitos(ids, prefijo="..") -> str:
    filas = []
    for class_id in ids:
        clase = curriculum.find_class(class_id)
        demo, funcion = engines.demo_for_class(class_id)
        resumen = (funcion.__doc__ or "").strip().splitlines()[0]
        ruta = f"{prefijo}/{curriculum.class_dir(clase).relative_to(ROOT).as_posix()}"
        filas.append(f"| [{clase['id']}]({ruta}/README.md) | {clase['title']} | `{demo}` | {resumen} |")
    return "\n".join(filas)


def _ruta_md(slug, titulo, perfil, partes, hitos, objetivo) -> str:
    clases = sum(len(curriculum.part(p)["classes"]) for p in partes)
    horas = clases * 4
    omitidas = [p["id"] for p in curriculum.parts() if p["id"] not in partes]
    return f"""# Ruta {slug.split('-', 1)[0]} — {titulo}

**Para quién:** {perfil}

**Objetivo:** {objetivo}

| Métrica | Valor |
|---|---:|
| Partes | {len(partes)} de 18 |
| Clases | {clases} de 360 |
| Horas estimadas | {horas} |
| A 10 h/semana | ~{horas // 10} semanas |

## Partes de la ruta

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
{_tabla_de_partes(partes)}

## Clases-hito

Si solo pudieras hacer unas pocas clases de esta ruta, serían estas. Cada una ejecuta
una demostración real:

| # | Clase | Demostración | Qué demuestra |
|---|---|---|---|
{_tabla_de_hitos(hitos)}

```bash
{chr(10).join(f'compmath run {h}' for h in hitos)}
```

## Partes omitidas

Esta ruta **no** cubre: {', '.join(omitidas)}.

Omitir una parte es una decisión, no un descuento: si un ejercicio te bloquea porque
falta un concepto de una parte omitida, vuelve a ella. La tabla de prerrequisitos está
en [docs/LEARNING_PATH.md](../docs/LEARNING_PATH.md).

## Criterio de avance

- [ ] ≥ 80 % de los ejercicios básicos de cada parte;
- [ ] al menos 15 de los 20 laboratorios de cada parte, con predicción escrita previa;
- [ ] el capstone de cada parte entregado;
- [ ] las cinco preguntas de comprobación respondidas sin mirar el código.

```bash
{chr(10).join(f'compmath run --part {p} --quiet' for p in partes)}
compmath progress
```

## Límite honesto

Completar esta ruta **no acredita** nada ni sustituye formación reglada. Demuestra que
puedes derivar, implementar y verificar los conceptos que cubre; nada más y nada menos.
"""


def _integracion_md(repo, descripcion, partes, hitos) -> str:
    return f"""# {repo}

{descripcion}

> Este documento define un **puente conceptual**. No duplica ni resume el contenido de
> [`{repo}`](https://github.com/vladimiracunadev-create/{repo}): lo referencia como
> superficie de aplicación de la matemática que este programa enseña.

## Prerrequisitos matemáticos

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
{_tabla_de_partes(partes, prefijo="../..")}

Total: {sum(len(curriculum.part(p)["classes"]) for p in partes)} clases.

## Puntos de conexión concretos

| Concepto que usa `{repo}` | Clase | Demostración |
|---|---|---|
{chr(10).join(f"| {concepto} | [{cid}](../../{curriculum.class_dir(curriculum.find_class(cid)).relative_to(ROOT).as_posix()}/README.md) | `{engines.demo_for_class(cid)[0]}` |" for concepto, cid in hitos)}

```bash
{chr(10).join(f'compmath show {cid}' for _, cid in hitos)}
```

## Cómo usar el puente

1. Identifica el concepto aplicado que no entiendes en `{repo}`.
2. Localízalo en la tabla de arriba y abre su clase aquí.
3. Ejecuta su laboratorio **después de escribir tu predicción**.
4. Vuelve al repositorio especializado y repite la aplicación entendiendo la fórmula.

## Qué no hace este puente

- No sustituye el contenido de `{repo}`.
- No garantiza que las partes listadas sean suficientes: son el mínimo, no el techo.
- No cubre las herramientas, frameworks ni prácticas de ingeniería de ese repositorio.
"""


def _integraciones_index() -> str:
    filas = []
    for repo, (descripcion, partes, _) in INTEGRACIONES.items():
        filas.append(f"| [`{repo}`]({repo}.md) | {descripcion} | {', '.join(partes)} |")
    return f"""# Integraciones con el ecosistema

Este directorio define **puentes conceptuales** entre la matemática de este programa y
los repositorios especializados que la aplican. **No duplica su contenido.**

| Repositorio | Aplica | Partes prerrequisito |
|---|---|---|
{chr(10).join(filas)}

## Principio

Este programa enseña la matemática; los repositorios enlazados enseñan su aplicación.
Cuando un concepto aparece en ambos, la fuente de verdad matemática está aquí y la
fuente de verdad aplicada está allí.

## Ver también

- [Rutas por perfil profesional](../../learning-paths/)
- [Mapa matemático de la IA](../AI_MATHEMATICS_MAP.md)
- [Ruta de aprendizaje](../LEARNING_PATH.md)
"""


def _classes_index() -> str:
    totales = curriculum.totals()
    bloques = []
    for parte in curriculum.parts():
        filas = []
        for clase in parte["classes"]:
            demo, funcion = engines.demo_for_class(clase["id"])
            resumen = (funcion.__doc__ or "").strip().splitlines()[0]
            filas.append(
                f"| [{clase['id']}](part-{parte['id']}-{parte['slug']}/{clase['slug']}/README.md) "
                f"| {clase['title']} | `{demo}` | {resumen} |"
            )
        bloques.append(
            f"### Parte {parte['id']} — [{parte['title']}](part-{parte['id']}-{parte['slug']}/README.md)\n\n"
            f"*{parte['summary']}*\n\n"
            f"| # | Clase | Demostración | Qué ejecuta |\n|---|---|---|---|\n"
            + "\n".join(filas)
        )
    return f"""# Catálogo de clases

**{totales['clases_reales']} clases** en **{totales['partes_reales']} partes** ·
{totales['notebooks']} notebooks · {totales['horas']} horas estimadas.

Cada clase contiene {totales['archivos_por_clase']} archivos y ejecuta una demostración
real del motor de su parte. Este índice es un **artefacto generado**: se reconstruye con
`python scripts/generate_classes.py`.

```bash
compmath catalog            # el mismo listado desde la terminal
compmath show <clase>       # ficha de una clase
compmath run <clase>        # ejecutar su laboratorio
```

{chr(10).join(bloques)}
"""


def generar(check: bool = False) -> int:
    """Genera (o verifica) clases, catálogo, índices, rutas por perfil e integraciones."""
    escritos = 0
    desfasados: list[str] = []

    def escribir(ruta: Path, contenido: str) -> None:
        nonlocal escritos
        actual = ruta.read_text(encoding="utf-8") if ruta.exists() else None
        if actual == contenido:
            return
        if check:
            desfasados.append(str(ruta.relative_to(ROOT)).replace("\\", "/"))
            return
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(contenido, encoding="utf-8")
        escritos += 1

    for parte in curriculum.parts():
        clases_de_parte = []
        for index, clase_yaml in enumerate(parte["classes"], start=1):
            clase = {**clase_yaml, "part": parte["id"], "part_slug": parte["slug"],
                     "part_title": parte["title"], "level": parte["level"],
                     "engine": parte["engine"], "index_in_part": index}
            clases_de_parte.append(clase)
            demo = _demo_info(clase["id"])
            directorio = curriculum.class_dir(clase)

            escribir(directorio / "README.md", _readme(clase, parte, demo))
            escribir(directorio / "intuition.md", _intuition(clase, parte, demo))
            escribir(directorio / "theory.md", _theory(clase, parte, demo))
            escribir(directorio / "derivation.md", _derivation(clase, parte, demo))
            escribir(directorio / "exercises.md", _exercises(clase, parte, demo))
            escribir(directorio / "assessment.md", _assessment(clase, parte, demo))
            escribir(directorio / "where-is-this-used.md", _where_used(clase, parte, demo))
            escribir(directorio / "lesson.yaml", _lesson_yaml(clase, parte, demo))
            escribir(directorio / "lab.py", _lab(clase, parte, demo))
            escribir(directorio / "notebook.ipynb", _notebook_recorrido(clase, parte, demo))
            escribir(directorio / "notebook_student.ipynb", _notebook_student(clase, parte, demo))
            escribir(directorio / "notebook_solution.ipynb", _notebook_solution(clase, parte, demo))

        parte_dir = ROOT / "classes" / f"part-{parte['id']}-{parte['slug']}"
        escribir(parte_dir / "README.md", _part_readme(parte, clases_de_parte))
        glosario = _glosario_parte(parte, clases_de_parte)
        if glosario:
            escribir(parte_dir / "GLOSARIO.md", glosario)

    escribir(ROOT / "classes" / "README.md", _classes_index())

    for slug, titulo, perfil, partes, hitos, objetivo in RUTAS:
        escribir(ROOT / "learning-paths" / f"{slug}.md",
                 _ruta_md(slug, titulo, perfil, partes, hitos, objetivo))

    for repo, (descripcion, partes, hitos) in INTEGRACIONES.items():
        escribir(ROOT / "docs" / "integrations" / f"{repo}.md",
                 _integracion_md(repo, descripcion, partes, hitos))
    escribir(ROOT / "docs" / "integrations" / "README.md", _integraciones_index())

    catalogo = json.dumps(curriculum.build_catalog(), indent=2, ensure_ascii=False) + "\n"
    escribir(curriculum.CATALOG_PATH, catalogo)

    if check:
        if desfasados:
            print(f"{len(desfasados)} archivo(s) desfasados respecto de curriculum.yaml:")
            for ruta in desfasados[:20]:
                print(f"  - {ruta}")
            if len(desfasados) > 20:
                print(f"  … y {len(desfasados) - 20} más")
            print("\nEjecuta `python scripts/generate_classes.py` y vuelve a commitear.")
            return 1
        print("OK: las clases generadas coinciden con curriculum.yaml.")
        return 0

    print(f"OK: {escritos} archivo(s) escritos a partir de curriculum.yaml.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="no escribe; falla si algún archivo está desfasado")
    args = parser.parse_args()
    return generar(check=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
