"""Compone el manual completo del programa en HTML autocontenido y en PDF.

El manual reúne portada, índice, las 18 partes con su mapa conceptual y su
glosario, y las 360 clases con sus fundamentos, ejemplo trabajado, salidas del
laboratorio, errores frecuentes y referencias.

    python scripts/build_manual.py              # HTML (y PDF si hay motor)
    python scripts/build_manual.py --no-pdf     # solo HTML
    python scripts/build_manual.py --check      # verifica el HTML generado

El HTML no depende de nada externo: se abre con doble clic y se imprime a PDF
desde el navegador. El PDF automático usa `xhtml2pdf` si está instalado; si no,
el script lo indica y termina con éxito, sin fingir que produjo el archivo.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import __version__, content, curriculum, engines, sources  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SALIDA = ROOT / "manual"
HTML_OUT = SALIDA / "computational-mathematics-program-manual.html"
PDF_OUT = SALIDA / "computational-mathematics-program-manual.pdf"

CSS = """
/* Sin variables CSS ni `var()`: xhtml2pdf no las soporta y el manual debe
   convertirse a PDF sin depender de un navegador. */
@page { size: A4; margin: 20mm 18mm; }
* { box-sizing: border-box; }
body {
  margin: 0 auto; max-width: 190mm; padding: 0 6mm;
  font-family: Georgia, "Times New Roman", serif; font-size: 10.5pt; line-height: 1.55;
  color: #14161d; background: #ffffff;
}
h1, h2, h3, h4 { font-family: "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.25; }
h1 { font-size: 22pt; margin: 0 0 6pt; }
h2 { font-size: 16pt; margin: 22pt 0 8pt; padding-bottom: 4pt;
     border-bottom: 2px solid #5a3fd6; page-break-after: avoid; }
h3 { font-size: 12.5pt; margin: 16pt 0 6pt; color: #5a3fd6; page-break-after: avoid; }
h4 { font-size: 11pt; margin: 12pt 0 4pt; color: #5b6478; page-break-after: avoid; }
p { margin: 0 0 8pt; text-align: justify; }
a { color: #5a3fd6; text-decoration: none; }
code { font-family: Consolas, "Courier New", monospace; font-size: 9pt;
       background: #f4f5f9; padding: 1pt 3pt; }
pre { font-family: Consolas, "Courier New", monospace; font-size: 9pt;
      background: #f4f5f9; border-left: 3px solid #5a3fd6;
      padding: 7pt 9pt; page-break-inside: avoid; }
pre code { background: #f4f5f9; padding: 0; }
table { width: 100%; border-collapse: collapse; margin: 8pt 0; font-size: 9pt;
        page-break-inside: avoid; }
th, td { border: 1px solid #d9dee9; padding: 4pt 6pt; text-align: left; vertical-align: top; }
th { background: #f4f5f9; font-family: "Segoe UI", Helvetica, sans-serif;
     font-size: 8.5pt; color: #5b6478; }
ul, ol { margin: 0 0 8pt; padding-left: 18pt; }
li { margin-bottom: 3pt; }
blockquote { margin: 8pt 0; padding: 6pt 10pt; border-left: 3px solid #1f7a4d;
             background: #f6faf7; }
hr { border-top: 1px solid #d9dee9; margin: 16pt 0; }
.portada { text-align: center; padding: 40mm 0 20mm; page-break-after: always; }
.portada .titulo { font-size: 30pt; font-weight: bold;
                   font-family: "Segoe UI", Helvetica, sans-serif; margin-bottom: 6pt; }
.portada .sub { font-size: 13pt; color: #5b6478; margin-bottom: 22pt; }
.portada .cifras { font-size: 11pt; color: #14161d; }
.portada .pie { margin-top: 26pt; font-size: 9.5pt; color: #5b6478; }
.chip { font-family: "Segoe UI", Helvetica, sans-serif; font-size: 8pt;
        padding: 2pt 7pt; border: 1px solid #5a3fd6; color: #5a3fd6; }
.parte { page-break-before: always; }
.clase { margin-bottom: 14pt; }
.meta { font-family: "Segoe UI", Helvetica, sans-serif; font-size: 8.5pt;
        color: #5b6478; margin: 0 0 8pt; }
.indice ol { list-style-type: none; padding-left: 0; }
.indice ol ol { padding-left: 14pt; font-size: 9.5pt; }
.nota { font-size: 9pt; color: #5b6478; }
"""


# Compilados fuera de las f-strings: una barra invertida dentro de una f-string
# es un error de sintaxis en Python 3.11, y el programa soporta 3.11+.
VINETA = re.compile(r"^\s*[-*]\s+")
NUMERADA = re.compile(r"^\s*\d+[.)]\s+")
SEPARADOR_TABLA = re.compile(r":?-{2,}:?")


def esc(texto: Any) -> str:
    return html.escape(str(texto), quote=False)


def _items(lineas: List[str], patron: "re.Pattern[str]") -> str:
    """Convierte líneas de lista en elementos <li>."""
    return "".join(f"<li>{_inline(patron.sub('', linea))}</li>" for linea in lineas)


def md_a_html(texto: str) -> str:
    """Conversor Markdown mínimo y suficiente para el contenido del programa.

    Cubre lo que el contenido usa realmente: bloques de código, listas, negrita,
    cursiva, código en línea, enlaces y párrafos. No pretende ser general.
    """
    if not texto:
        return ""
    partes: List[str] = []
    bloques = texto.split("```")
    for indice, bloque in enumerate(bloques):
        if indice % 2 == 1:                       # bloque de código
            cuerpo = bloque.split("\n", 1)[1] if "\n" in bloque else bloque
            partes.append(f"<pre><code>{esc(cuerpo.rstrip())}</code></pre>")
            continue
        for parrafo in re.split(r"\n\s*\n", bloque.strip()):
            if not parrafo.strip():
                continue
            lineas = parrafo.strip().split("\n")
            if all(VINETA.match(ln) for ln in lineas):
                items = _items(lineas, VINETA)
                partes.append(f"<ul>{items}</ul>")
            elif all(NUMERADA.match(ln) for ln in lineas):
                items = _items(lineas, NUMERADA)
                partes.append(f"<ol>{items}</ol>")
            elif all(ln.lstrip().startswith("|") for ln in lineas) and len(lineas) >= 2:
                partes.append(_tabla(lineas))
            elif parrafo.lstrip().startswith(">"):
                cuerpo = " ".join(ln.lstrip("> ").strip() for ln in lineas)
                partes.append(f"<blockquote>{_inline(cuerpo)}</blockquote>")
            else:
                partes.append(f"<p>{_inline(' '.join(ln.strip() for ln in lineas))}</p>")
    return "".join(partes)


def _tabla(lineas: List[str]) -> str:
    filas = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lineas]
    filas = [f for f in filas if not all(SEPARADOR_TABLA.fullmatch(c) for c in f)]
    if not filas:
        return ""
    cabecera = "".join(f"<th>{_inline(c)}</th>" for c in filas[0])
    cuerpo = "".join(
        "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in fila) + "</tr>" for fila in filas[1:]
    )
    return f"<table><thead><tr>{cabecera}</tr></thead><tbody>{cuerpo}</tbody></table>"


def _inline(texto: str) -> str:
    texto = esc(texto)
    texto = re.sub(r"`([^`]+)`", r"<code>\1</code>", texto)
    texto = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", texto)
    texto = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", texto)
    texto = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', texto)
    return texto


def _portada(totales: Dict[str, int], cobertura: Dict[str, Any]) -> str:
    return f"""<div class="portada">
  <div class="titulo">Computational Mathematics Program</div>
  <div class="sub">De cero absoluto a la matemática que sostiene la inteligencia artificial</div>
  <div class="cifras">
    <span class="chip">{totales['partes_reales']} partes</span>
    <span class="chip">{totales['clases_reales']} clases</span>
    <span class="chip">{totales['notebooks']} notebooks</span>
    <span class="chip">{len(engines.ENGINE_MODULES)} motores</span>
    <span class="chip">{totales['horas']} horas</span>
  </div>
  <div class="pie">
    Manual completo · versión {__version__}<br>
    Generado desde <code>curriculum.yaml</code>, <code>content/</code> y los motores ejecutables<br>
    <a href="https://github.com/vladimiracunadev-create/computational-mathematics-program">
      github.com/vladimiracunadev-create/computational-mathematics-program</a><br>
    Licencia MIT · contenido pedagógico redactado en {cobertura['clases_con_contenido_completo']}
    de {cobertura['clases_totales']} clases ({cobertura['cobertura_%']} %)
  </div>
</div>"""


def _indice(partes) -> str:
    items = []
    for parte in partes:
        clases = "".join(
            f'<li><a href="#c{c["id"]}">{c["id"]} · {esc(c["title"])}</a></li>'
            for c in parte["classes"]
        )
        items.append(
            f'<li><a href="#p{parte["id"]}">Parte {parte["id"]} — {esc(parte["title"])}</a>'
            f"<ol>{clases}</ol></li>"
        )
    return f"""<div class="indice parte">
  <h2>Índice</h2>
  <ol>{''.join(items)}</ol>
</div>"""


def _seccion_parte(parte) -> str:
    extra = content.part_content(parte["id"])
    bloques = [
        f'<div class="parte" id="p{parte["id"]}">',
        f'<h2>Parte {parte["id"]} — {esc(parte["title"])}</h2>',
        f'<p class="meta">Nivel {esc(parte["level"])} · {len(parte["classes"])} clases · '
        f'{len(parte["classes"]) * 4} horas · motor <code>{esc(parte["engine"])}</code></p>',
        f"<p>{_inline(parte['summary'])}</p>",
    ]
    if extra.get("resumen_extendido"):
        bloques.append(md_a_html(extra["resumen_extendido"]))

    bloques.append("<h3>Ideas centrales</h3>")
    bloques.append("<ul>" + "".join(f"<li>{_inline(i)}</li>" for i in parte["key_ideas"]) + "</ul>")

    bloques.append("<h3>Por qué importa en IA</h3>")
    bloques.append(f"<blockquote>{_inline(parte['ai_link'])}</blockquote>")

    bloques.append("<h3>Errores frecuentes de la parte</h3>")
    bloques.append("<ul>" + "".join(f"<li>{_inline(i)}</li>" for i in parte["pitfalls"]) + "</ul>")

    glosario = content.glossary(parte["id"])
    if glosario:
        filas = "".join(
            f"<tr><td><strong>{esc(t['termino'])}</strong></td><td>{_inline(t['definicion'])}</td>"
            f"<td>{esc(t.get('clase', '—'))}</td></tr>"
            for t in sorted(glosario, key=lambda x: x["termino"].lower())
        )
        bloques.append(f"<h3>Glosario de la parte ({len(glosario)} términos)</h3>")
        bloques.append(
            "<table><thead><tr><th>Término</th><th>Definición</th><th>Clase</th></tr></thead>"
            f"<tbody>{filas}</tbody></table>"
        )

    bloques.append("<h3>Bibliografía de la parte</h3>")
    bloques.append("<ul>" + "".join(f"<li>{_inline(r)}</li>" for r in parte["references"]) + "</ul>")
    bloques.append("</div>")
    return "".join(bloques)


def _seccion_clase(clase, parte) -> str:
    demo, funcion = engines.demo_for_class(clase["id"])
    resultado = funcion()
    resumen = (funcion.__doc__ or "").strip().splitlines()[0]
    registro = content.class_content(clase["id"])

    verificaciones = [k for k, v in resultado.items() if isinstance(v, bool)]
    numericos = [k for k, v in resultado.items() if isinstance(v, (int, float)) and not isinstance(v, bool)]

    bloques = [
        f'<div class="clase" id="c{clase["id"]}">',
        f'<h3>{clase["id"]} · {esc(clase["title"])}</h3>',
        f'<p class="meta">Parte {parte["id"]} · clase {clase["index_in_part"]} de '
        f'{len(parte["classes"])} · demostración <code>{esc(demo)}</code></p>',
    ]

    if registro.get("concepto"):
        bloques.append(f"<p><strong>{_inline(registro['concepto'])}</strong></p>")

    if registro.get("formulas"):
        cuerpo = "\n".join(registro["formulas"])
        bloques.append(f"<pre><code>{esc(cuerpo)}</code></pre>")

    if registro.get("desarrollo"):
        bloques.append("<h4>Fundamentos</h4>")
        bloques.append(md_a_html(registro["desarrollo"]))

    if registro.get("ejemplo"):
        bloques.append("<h4>Ejemplo trabajado</h4>")
        bloques.append(md_a_html(registro["ejemplo"]))

    bloques.append("<h4>Qué ejecuta el laboratorio</h4>")
    bloques.append(f"<p>{_inline(resumen)}</p>")
    bloques.append(
        "<table><thead><tr><th>Grupo</th><th>Salidas</th></tr></thead><tbody>"
        f"<tr><td>Resultados numéricos ({len(numericos)})</td>"
        f"<td>{', '.join(f'<code>{esc(k)}</code>' for k in numericos) or '—'}</td></tr>"
        f"<tr><td>Comprobaciones ({len(verificaciones)})</td>"
        f"<td>{', '.join(f'<code>{esc(k)}</code>' for k in verificaciones) or '—'}</td></tr>"
        "</tbody></table>"
    )
    bloques.append(f"<pre><code>compmath run {clase['id']}</code></pre>")

    if registro.get("errores"):
        bloques.append("<h4>Errores conceptuales frecuentes</h4>")
        bloques.append("<ol>" + "".join(f"<li>{_inline(e)}</li>" for e in registro["errores"]) + "</ol>")

    if registro.get("aplicacion"):
        bloques.append("<h4>Dónde se usa</h4>")
        bloques.append(md_a_html(registro["aplicacion"]))

    if registro.get("referencias"):
        bloques.append("<h4>Bibliografía de la clase</h4>")
        lineas = sources.class_block(clase["id"], clase["title"])
        bloques.append("<ul>" + "".join(f"<li>{_inline(r)}</li>" for r in lineas) + "</ul>")

    bloques.append("</div>")
    return "".join(bloques)


def construir_html() -> str:
    totales = curriculum.totals()
    cobertura = content.coverage()
    partes = curriculum.parts()

    cuerpo = [_portada(totales, cobertura), _indice(partes)]

    cuerpo.append('<div class="parte"><h2>Cómo leer este manual</h2>')
    cuerpo.append(md_a_html(f"""
Este manual es un **artefacto generado**. Se reconstruye con
`python scripts/build_manual.py` a partir de tres fuentes: el currículo
(`curriculum.yaml`), el contenido pedagógico (`content/`) y los 18 motores
ejecutables, cuyas demostraciones se **ejecutan durante la generación** para
extraer sus salidas reales.

Cada clase incluye su concepto, sus fórmulas, sus fundamentos, un ejemplo
numérico trabajado, las salidas que devuelve su laboratorio, los errores
conceptuales frecuentes y sus referencias. Los apartados que no aparecen en una
clase concreta son los que todavía no están redactados: el manual no rellena
huecos con texto genérico.

> Estado del contenido pedagógico: {cobertura['clases_con_contenido_completo']} de
> {cobertura['clases_totales']} clases redactadas ({cobertura['cobertura_%']} %),
> {cobertura['partes_con_resumen']} de 18 partes con resumen extendido y
> {cobertura['terminos_de_glosario']} términos de glosario.

**Límites declarados.** Un manual educativo no sustituye una carrera ni
supervisión académica. Las derivaciones se orientan a comprensión computacional;
la profundidad formal completa exige los textos citados en cada parte. Los
motores son legibles, no rápidos, y no deben usarse en producción.
"""))
    cuerpo.append("</div>")

    for parte in partes:
        cuerpo.append(_seccion_parte(parte))
        for indice, clase_yaml in enumerate(parte["classes"], start=1):
            clase = {**clase_yaml, "part": parte["id"], "index_in_part": indice}
            cuerpo.append(_seccion_clase(clase, parte))

    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Computational Mathematics Program — Manual completo v{__version__}</title>
<meta name="description" content="Manual completo del programa: {totales['partes_reales']} partes,
{totales['clases_reales']} clases y {totales['notebooks']} notebooks.">
<style>{CSS}</style>
</head>
<body>
{''.join(cuerpo)}
<hr>
<p class="nota">Computational Mathematics Program v{__version__} · MIT ·
generado automáticamente · ninguna cifra de este manual se escribió a mano:
todas se derivan del repositorio.</p>
</body>
</html>
"""


def construir_pdf(html_texto: str) -> bool:
    """Convierte el HTML a PDF si hay un motor disponible. No falla si no lo hay."""
    try:  # pragma: no cover - depende del entorno
        from xhtml2pdf import pisa
    except ImportError:
        print("  · xhtml2pdf no está instalado: se omite el PDF.")
        print("    Instálalo con `pip install -e \".[manual]\"` o imprime el HTML desde el navegador.")
        return False
    with PDF_OUT.open("wb") as destino:
        estado = pisa.CreatePDF(html_texto, dest=destino, encoding="utf-8")
    if estado.err:
        print(f"  · el motor de PDF reportó {estado.err} error(es).")
        return False
    print(f"  · PDF: {PDF_OUT.relative_to(ROOT)} ({PDF_OUT.stat().st_size / 1_048_576:.1f} MB)")
    return True


def verificar(html_texto: str) -> int:
    """Comprueba que el manual contiene lo que dice contener."""
    totales = curriculum.totals()
    errores = []
    for parte in curriculum.parts():
        if f'id="p{parte["id"]}"' not in html_texto:
            errores.append(f"falta la sección de la parte {parte['id']}")
    faltantes = [c["id"] for c in curriculum.classes() if f'id="c{c["id"]}"' not in html_texto]
    if faltantes:
        errores.append(f"faltan {len(faltantes)} clases, p. ej. {faltantes[:5]}")
    for cifra in (str(totales["clases_reales"]), str(totales["partes_reales"]), str(totales["notebooks"])):
        if cifra not in html_texto:
            errores.append(f"el manual no declara la cifra {cifra}")
    if "<script" in html_texto.lower():
        errores.append("el manual no debe contener scripts")

    if errores:
        print(f"{len(errores)} problema(s) en el manual:")
        for problema in errores:
            print(f"  ✗ {problema}")
        return 1
    print(
        f"OK: manual válido — {totales['partes_reales']} partes, {totales['clases_reales']} clases, "
        f"{len(html_texto) / 1_048_576:.1f} MB de HTML, sin scripts."
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-pdf", action="store_true", help="genera solo el HTML")
    parser.add_argument("--check", action="store_true", help="verifica el manual y no escribe PDF")
    args = parser.parse_args()

    SALIDA.mkdir(exist_ok=True)
    print("Construyendo el manual (esto ejecuta las 360 demostraciones)…")
    html_texto = construir_html()
    HTML_OUT.write_text(html_texto, encoding="utf-8")
    print(f"  · HTML: {HTML_OUT.relative_to(ROOT)} ({HTML_OUT.stat().st_size / 1_048_576:.1f} MB)")

    codigo = verificar(html_texto)
    if codigo or args.check:
        return codigo

    if not args.no_pdf:
        construir_pdf(html_texto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
