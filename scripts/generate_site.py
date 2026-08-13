"""Genera el portal estático de GitHub Pages en ``site/``.

Todo el sitio es HTML, CSS y JavaScript sin dependencias externas ni CDN: se
puede abrir con doble clic desde el disco y funciona sin conexión gracias al
service worker.

    python scripts/generate_site.py
"""

from __future__ import annotations

import html
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import __version__, curriculum, engines  # noqa: E402

SITE = ROOT / "site"
REPO = "vladimiracunadev-create/computational-mathematics-program"
BASE_GITHUB = f"https://github.com/{REPO}/blob/main"
PAGES_URL = "https://vladimiracunadev-create.github.io/computational-mathematics-program/"

NIVEL_COLOR = {
    "cero-absoluto": "#4ade80",
    "basico-computacional": "#38bdf8",
    "basico": "#38bdf8",
    "basico-intermedio": "#22d3ee",
    "intermedio": "#a78bfa",
    "intermedio-avanzado": "#c084fc",
    "universitario": "#f472b6",
    "universitario-avanzado": "#fb7185",
    "cientifico": "#fbbf24",
    "avanzado": "#fb923c",
    "ml-avanzado": "#f97316",
    "deep-learning": "#ef4444",
    "experto": "#e11d48",
    "frontera-investigacion": "#7c5cff",
}

CSS = """
:root {
  --bg: #0b0d13;
  --bg-soft: #12151f;
  --card: #161a26;
  --border: #262c3d;
  --text: #e6e9f0;
  --muted: #9aa3b8;
  --accent: #7c5cff;
  --accent-2: #2e8b57;
  --radius: 14px;
  --mono: ui-monospace, "SF Mono", "Cascadia Code", Consolas, monospace;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #f7f8fb; --bg-soft: #eef1f7; --card: #ffffff; --border: #dfe3ed;
    --text: #12151f; --muted: #5b6478;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.65 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.wrap { max-width: 1080px; margin: 0 auto; padding: 0 20px; }
header.top {
  position: sticky; top: 0; z-index: 20; backdrop-filter: blur(12px);
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  border-bottom: 1px solid var(--border);
}
header.top .wrap { display: flex; align-items: center; gap: 18px; height: 60px; }
header.top .brand { font-weight: 700; letter-spacing: -0.02em; white-space: nowrap; }
header.top nav { display: flex; gap: 16px; margin-left: auto; flex-wrap: wrap; }
header.top nav a { color: var(--muted); font-size: 14px; }
header.top nav a:hover { color: var(--text); }
.hero { padding: 56px 0 32px; border-bottom: 1px solid var(--border); }
.hero h1 { font-size: clamp(28px, 5vw, 46px); line-height: 1.15; margin: 0 0 12px; letter-spacing: -0.03em; }
.hero p.lead { color: var(--muted); font-size: 18px; max-width: 68ch; margin: 0 0 24px; }
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 12px; margin: 28px 0; }
.stat { background: var(--card); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px; }
.stat b { display: block; font-size: 26px; letter-spacing: -0.02em; }
.stat span { color: var(--muted); font-size: 13px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 16px; }
.card {
  background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
  padding: 18px; display: block; color: inherit; transition: border-color .15s, transform .15s;
}
.card:hover { border-color: var(--accent); text-decoration: none; transform: translateY(-2px); }
.card h3 { margin: 6px 0 8px; font-size: 17px; letter-spacing: -0.01em; }
.card p { margin: 0; color: var(--muted); font-size: 14px; }
.tag {
  display: inline-block; font-size: 11px; font-family: var(--mono);
  padding: 2px 8px; border-radius: 99px; border: 1px solid currentColor; opacity: .9;
}
.pill { font-family: var(--mono); font-size: 12px; color: var(--muted); }
section { padding: 40px 0; }
section > h2 { font-size: 22px; margin: 0 0 6px; letter-spacing: -0.02em; }
section > p.sub { color: var(--muted); margin: 0 0 22px; }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th, td { text-align: left; padding: 9px 10px; border-bottom: 1px solid var(--border); }
th { color: var(--muted); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: .04em; }
.table-wrap { overflow-x: auto; border: 1px solid var(--border); border-radius: var(--radius); }
code { font-family: var(--mono); font-size: .9em; background: var(--bg-soft); padding: 2px 6px; border-radius: 6px; }
pre { background: var(--bg-soft); border: 1px solid var(--border); border-radius: var(--radius);
      padding: 14px 16px; overflow-x: auto; }
pre code { background: none; padding: 0; }
ul.clean { list-style: none; padding: 0; margin: 0; }
ul.clean li { padding: 8px 0; border-bottom: 1px solid var(--border); }
ul.clean li:last-child { border-bottom: 0; }
.search {
  width: 100%; padding: 13px 16px; border-radius: var(--radius);
  border: 1px solid var(--border); background: var(--card); color: var(--text); font-size: 15px;
}
.search:focus { outline: 2px solid var(--accent); outline-offset: 1px; }
.filters { display: flex; gap: 8px; flex-wrap: wrap; margin: 14px 0 20px; }
.filters button {
  background: var(--card); border: 1px solid var(--border); color: var(--muted);
  padding: 6px 12px; border-radius: 99px; cursor: pointer; font-size: 13px; font-family: inherit;
}
.filters button[aria-pressed="true"] { border-color: var(--accent); color: var(--text); }
.results { display: grid; gap: 8px; }
.result {
  display: flex; gap: 12px; align-items: baseline; padding: 10px 14px;
  border: 1px solid var(--border); border-radius: 10px; background: var(--card); color: inherit;
}
.result:hover { border-color: var(--accent); text-decoration: none; }
.result .id { font-family: var(--mono); color: var(--muted); font-size: 13px; }
.result .t { flex: 1; }
.empty { color: var(--muted); padding: 24px; text-align: center; }
.crumb { color: var(--muted); font-size: 14px; margin: 24px 0 4px; }
h1.page { font-size: clamp(24px, 4vw, 34px); margin: 4px 0 10px; letter-spacing: -0.03em; }
.meta { display: flex; gap: 14px; flex-wrap: wrap; color: var(--muted); font-size: 13px; margin-bottom: 22px; }
.callout {
  border-left: 3px solid var(--accent); background: var(--bg-soft);
  padding: 14px 18px; border-radius: 0 var(--radius) var(--radius) 0; margin: 18px 0;
}
.callout.warn { border-left-color: #fb923c; }
.callout.ok { border-left-color: var(--accent-2); }
.progress-bar { height: 6px; background: var(--bg-soft); border-radius: 99px; overflow: hidden; margin-top: 8px; }
.progress-bar i { display: block; height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent-2)); }
.nav-classes { display: flex; justify-content: space-between; gap: 12px; margin: 32px 0; flex-wrap: wrap; }
footer { border-top: 1px solid var(--border); padding: 32px 0; color: var(--muted); font-size: 13px; }
footer .wrap { display: flex; gap: 16px; flex-wrap: wrap; justify-content: space-between; }
.btn {
  display: inline-block; padding: 10px 18px; border-radius: 10px;
  background: var(--accent); color: #fff; font-weight: 600; font-size: 14px;
}
.btn:hover { text-decoration: none; opacity: .92; }
.btn.ghost { background: transparent; border: 1px solid var(--border); color: var(--text); }
.done-toggle {
  background: var(--card); border: 1px solid var(--border); color: var(--muted);
  padding: 8px 14px; border-radius: 10px; cursor: pointer; font: inherit; font-size: 14px;
}
.done-toggle[aria-pressed="true"] { border-color: var(--accent-2); color: var(--accent-2); }
"""

APP_JS = """
(function () {
  'use strict';
  var KEY = 'compmath-progress-v1';

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; }
  }
  function save(state) {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* modo privado */ }
  }

  window.compmathProgress = { load: load, save: save };

  // ---- Buscador del índice -------------------------------------------------
  var input = document.getElementById('q');
  var results = document.getElementById('results');
  if (input && results && window.CATALOG) {
    var activeLevel = null;
    function render() {
      var q = input.value.trim().toLowerCase();
      var items = window.CATALOG.filter(function (c) {
        var okLevel = !activeLevel || c.level === activeLevel;
        if (!okLevel) return false;
        if (!q) return true;
        return (c.id + ' ' + c.title + ' ' + c.part_title + ' ' + c.demo).toLowerCase().indexOf(q) !== -1;
      });
      if (!items.length) {
        results.innerHTML = '<p class="empty">Sin resultados para esa búsqueda.</p>';
        return;
      }
      results.innerHTML = items.slice(0, 80).map(function (c) {
        return '<a class="result" href="classes/' + c.id + '.html">' +
          '<span class="id">' + c.id + '</span>' +
          '<span class="t">' + c.title + '</span>' +
          '<span class="pill">parte ' + c.part + '</span></a>';
      }).join('') + (items.length > 80
        ? '<p class="empty">' + (items.length - 80) + ' resultados más. Afina la búsqueda.</p>' : '');
    }
    input.addEventListener('input', render);
    Array.prototype.forEach.call(document.querySelectorAll('.filters button'), function (b) {
      b.addEventListener('click', function () {
        var lvl = b.getAttribute('data-level');
        activeLevel = (activeLevel === lvl) ? null : lvl;
        Array.prototype.forEach.call(document.querySelectorAll('.filters button'), function (o) {
          o.setAttribute('aria-pressed', String(o.getAttribute('data-level') === activeLevel));
        });
        render();
      });
    });
    render();
  }

  // ---- Progreso global en el índice ---------------------------------------
  var bar = document.getElementById('progress-fill');
  var label = document.getElementById('progress-label');
  if (bar && label) {
    var state = load();
    var done = Object.keys(state).length;
    var total = (window.CATALOG || []).length || 360;
    bar.style.width = (100 * done / total).toFixed(1) + '%';
    label.textContent = done + ' de ' + total + ' clases marcadas como completadas (solo en este navegador)';
  }

  // ---- Marcar clase como completada ---------------------------------------
  var toggle = document.getElementById('done');
  if (toggle) {
    var id = toggle.getAttribute('data-class');
    var st = load();
    function paint() {
      var on = !!st[id];
      toggle.setAttribute('aria-pressed', String(on));
      toggle.textContent = on ? '✓ Clase completada' : 'Marcar como completada';
    }
    toggle.addEventListener('click', function () {
      if (st[id]) { delete st[id]; } else { st[id] = new Date().toISOString().slice(0, 10); }
      save(st); paint();
    });
    paint();
  }

  // ---- Service worker ------------------------------------------------------
  if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
    window.addEventListener('load', function () {
      navigator.serviceWorker.register('service-worker.js').catch(function () { /* opcional */ });
    });
  }
})();
"""

SERVICE_WORKER = """
var CACHE = 'compmath-v%(version)s';
var CORE = ['./', './index.html', './assets/style.css', './assets/app.js', './data/catalog.json'];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(CORE); }).then(function () {
    return self.skipWaiting();
  }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; })
      .map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then(function (hit) {
      return hit || fetch(e.request).then(function (res) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put(e.request, copy); });
        return res;
      }).catch(function () { return caches.match('./index.html'); });
    })
  );
});
"""


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _layout(titulo: str, contenido: str, prefijo: str = "", descripcion: str = "",
            extra_head: str = "", extra_body: str = "") -> str:
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(descripcion)}">
<meta name="color-scheme" content="dark light">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(descripcion)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{prefijo}assets/style.css">
<link rel="manifest" href="{prefijo}manifest.webmanifest">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧮</text></svg>">
{extra_head}
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="{prefijo}index.html">🧮 Computational Mathematics</a>
    <nav>
      <a href="{prefijo}index.html#partes">Partes</a>
      <a href="{prefijo}index.html#buscar">Buscar</a>
      <a href="{prefijo}index.html#descargas">Manual</a>
      <a href="{prefijo}index.html#rutas">Rutas</a>
      <a href="https://github.com/{REPO}">GitHub</a>
    </nav>
  </div>
</header>
{contenido}
<footer>
  <div class="wrap">
    <span>Computational Mathematics Program v{__version__} · MIT · generado desde <code>curriculum.yaml</code></span>
    <span><a href="https://github.com/{REPO}">Código fuente</a> · <a href="{prefijo}index.html">Inicio</a></span>
  </div>
</footer>
{extra_body}
<script src="{prefijo}assets/app.js"></script>
</body>
</html>
"""


def _nivel_tag(nivel: str) -> str:
    color = NIVEL_COLOR.get(nivel, "#9aa3b8")
    return f'<span class="tag" style="color:{color}">{esc(nivel)}</span>'


def _index(partes: List[Dict[str, Any]], catalogo: List[Dict[str, Any]]) -> str:
    totales = curriculum.totals()
    niveles = []
    vistos = set()
    for p in partes:
        if p["level"] not in vistos:
            vistos.add(p["level"])
            niveles.append(p["level"])

    tarjetas = "\n".join(
        f"""      <a class="card" href="parts/part-{esc(p['id'])}.html">
        {_nivel_tag(p['level'])}
        <h3>{esc(p['id'])} — {esc(p['title'])}</h3>
        <p>{esc(p['summary'])}</p>
        <p class="pill" style="margin-top:10px">{len(p['classes'])} clases · motor <code>{esc(p['engine'])}</code></p>
      </a>"""
        for p in partes
    )

    filtros = "\n".join(
        f'      <button data-level="{esc(n)}" aria-pressed="false">{esc(n)}</button>'
        for n in niveles
    )

    rutas = ROOT / "learning-paths"
    items_ruta = "\n".join(
        f'      <li><a href="https://github.com/{REPO}/blob/main/learning-paths/{esc(f.name)}">'
        f'{esc(f.stem.split("-", 1)[1].replace("-", " ").capitalize())}</a></li>'
        for f in sorted(rutas.glob("*.md"))
    ) if rutas.is_dir() else ""

    contenido = f"""
<div class="hero">
  <div class="wrap">
    <h1>Matemática computacional, de cero absoluto<br>a la matemática que sostiene la IA</h1>
    <p class="lead">{totales['partes_reales']} partes · {totales['clases_reales']} clases ·
    {totales['notebooks']} notebooks · {len(engines.ENGINE_MODULES)} motores ejecutables.
    Cada clase incluye un laboratorio que corre sin instalar dependencias científicas.</p>
    <p>
      <a class="btn" href="#buscar">Buscar una clase</a>
      <a class="btn ghost" href="parts/part-00.html">Empezar por la parte 00</a>
      <a class="btn ghost" href="#descargas">Manual completo (PDF)</a>
      <a class="btn ghost" href="https://github.com/{REPO}">Ver el repositorio</a>
    </p>
    <div class="stats">
      <div class="stat"><b>{totales['partes_reales']}</b><span>partes</span></div>
      <div class="stat"><b>{totales['clases_reales']}</b><span>clases</span></div>
      <div class="stat"><b>{totales['notebooks']}</b><span>notebooks</span></div>
      <div class="stat"><b>{len(engines.ENGINE_MODULES)}</b><span>motores ejecutables</span></div>
      <div class="stat"><b>{totales['horas']}</b><span>horas estimadas</span></div>
    </div>
    <div class="progress-bar"><i id="progress-fill" style="width:0%"></i></div>
    <p class="pill" id="progress-label" style="margin-top:8px">Progreso local</p>
  </div>
</div>

<section id="buscar">
  <div class="wrap">
    <h2>Buscar</h2>
    <p class="sub">Por número, título, parte o nombre de la demostración ejecutable.</p>
    <input class="search" id="q" type="search" placeholder="atención, SVD, Bayes, 250, backpropagation…"
           autocomplete="off" aria-label="Buscar una clase">
    <div class="filters">
{filtros}
    </div>
    <div class="results" id="results"></div>
  </div>
</section>

<section id="partes">
  <div class="wrap">
    <h2>Las {totales['partes_reales']} partes</h2>
    <p class="sub">De la aritmética exacta a la frontera de investigación. Cada parte tiene su propio motor ejecutable.</p>
    <div class="grid">
{tarjetas}
    </div>
  </div>
</section>

<section id="como">
  <div class="wrap">
    <h2>Cómo funciona</h2>
    <p class="sub">El repositorio es reproducible de punta a punta.</p>
    <pre><code>git clone https://github.com/{REPO}.git
cd computational-mathematics-program
python -m venv .venv &amp;&amp; . .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -e .

compmath stats              # conteos del programa
compmath catalog --part 12  # las 20 clases de optimización
compmath run 250            # ejecuta el laboratorio de Adam
compmath run --all          # ejecuta los 360 laboratorios
compmath validate --strict  # la misma validación que corre en CI</code></pre>
    <div class="callout ok">
      <strong>Sin dependencias científicas obligatorias.</strong> Los {totales['clases_reales']} laboratorios
      se ejecutan con biblioteca estándar de Python. NumPy, SciPy, SymPy o PyTorch son
      extras opcionales que sirven de contraste, no de requisito.
    </div>
    <div class="callout warn">
      <strong>Límites honestos.</strong> Un repositorio educativo no sustituye una carrera,
      un posgrado ni supervisión académica. Las derivaciones se orientan a comprensión
      computacional; la profundidad formal completa exige textos especializados.
    </div>
  </div>
</section>

<section id="descargas">
  <div class="wrap">
    <h2>Manual completo</h2>
    <p class="sub">Todo el programa en un solo documento: 18 partes, 360 clases, fundamentos,
    ejemplos trabajados y las salidas reales de cada laboratorio.</p>
    <p>
      <a class="btn" href="downloads/computational-mathematics-program-manual.pdf">📄 Descargar PDF</a>
      <a class="btn ghost" href="downloads/computational-mathematics-program-manual.html">🌐 Ver en HTML</a>
    </p>
    <div class="callout">
      El manual se regenera en cada despliegue con
      <code>python scripts/build_manual.py</code>, ejecutando las 360 demostraciones para
      extraer sus salidas reales. Ninguna cifra del documento está escrita a mano.
    </div>
  </div>
</section>

<section id="rutas">
  <div class="wrap">
    <h2>Rutas por perfil</h2>
    <p class="sub">Recorridos sugeridos según a dónde quieras llegar.</p>
    <ul class="clean">
{items_ruta}
    </ul>
  </div>
</section>
"""
    datos = json.dumps(catalogo, ensure_ascii=False, separators=(",", ":"))
    extra = f'<script>window.CATALOG={datos};</script>'
    return _layout(
        "Computational Mathematics Program",
        contenido,
        descripcion=(f"Programa de matemática computacional en español: {totales['partes_reales']} partes, "
                     f"{totales['clases_reales']} clases y {totales['notebooks']} notebooks, "
                     "de la aritmética a la matemática de la IA."),
        extra_body=extra,
    )


def _part_page(parte: Dict[str, Any]) -> str:
    filas = "\n".join(
        f"""        <tr>
          <td><code>{esc(c['id'])}</code></td>
          <td><a href="../classes/{esc(c['id'])}.html">{esc(c['title'])}</a></td>
          <td><code>{esc(engines.demo_for_class(c['id'])[0])}</code></td>
        </tr>"""
        for c in parte["classes"]
    )
    ideas = "\n".join(f"      <li>{esc(i)}</li>" for i in parte["key_ideas"])
    errores = "\n".join(f"      <li>{esc(i)}</li>" for i in parte["pitfalls"])
    refs = "\n".join(f"      <li>{esc(i)}</li>" for i in parte["references"])
    partes = curriculum.parts()
    idx = [p["id"] for p in partes].index(parte["id"])
    anterior = partes[idx - 1] if idx > 0 else None
    siguiente = partes[idx + 1] if idx < len(partes) - 1 else None

    contenido = f"""
<div class="wrap">
  <p class="crumb"><a href="../index.html">Inicio</a> · Parte {esc(parte['id'])}</p>
  <h1 class="page">{esc(parte['title'])}</h1>
  <div class="meta">
    {_nivel_tag(parte['level'])}
    <span>{len(parte['classes'])} clases</span>
    <span>{len(parte['classes']) * 4} horas estimadas</span>
    <span>motor <code>{esc(parte['engine'])}</code></span>
  </div>
  <p>{esc(parte['summary'])}</p>

  <h2>Ideas centrales</h2>
  <ul class="clean">
{ideas}
  </ul>

  <h2>Por qué importa en IA</h2>
  <div class="callout">{esc(parte['ai_link'])}</div>

  <h2>Errores frecuentes</h2>
  <ul class="clean">
{errores}
  </ul>

  <h2>Secuencia de clases</h2>
  <div class="table-wrap">
    <table>
      <thead><tr><th>#</th><th>Clase</th><th>Demostración ejecutable</th></tr></thead>
      <tbody>
{filas}
      </tbody>
    </table>
  </div>

  <h2>Ejecutar la parte completa</h2>
  <pre><code>compmath run --part {esc(parte['id'])}</code></pre>

  <h2>Bibliografía</h2>
  <ul class="clean">
{refs}
  </ul>

  <div class="nav-classes">
    {f'<a class="btn ghost" href="part-{esc(anterior["id"])}.html">← {esc(anterior["title"])}</a>' if anterior else '<span></span>'}
    {f'<a class="btn ghost" href="part-{esc(siguiente["id"])}.html">{esc(siguiente["title"])} →</a>' if siguiente else '<span></span>'}
  </div>
  <p><a href="{BASE_GITHUB}/src/computational_math/engines/{esc(parte['engine'])}.py">Ver el motor en GitHub</a></p>
</div>
"""
    return _layout(f"Parte {parte['id']} — {parte['title']}", contenido, prefijo="../",
                   descripcion=parte["summary"])


def _class_page(clase: Dict[str, Any], parte: Dict[str, Any], indice: List[Dict[str, Any]]) -> str:
    nombre, funcion = engines.demo_for_class(clase["id"])
    resultado = funcion()
    resumen = (funcion.__doc__ or "").strip().splitlines()[0]
    salidas = "\n".join(f"      <li><code>{esc(k)}</code></li>" for k in resultado)
    ruta = curriculum.class_dir(clase).relative_to(ROOT).as_posix()
    idea = parte["key_ideas"][(clase["index_in_part"] - 1) % len(parte["key_ideas"])]
    error = parte["pitfalls"][(clase["index_in_part"] - 1) % len(parte["pitfalls"])]

    posicion = [c["id"] for c in indice].index(clase["id"])
    anterior = indice[posicion - 1] if posicion > 0 else None
    siguiente = indice[posicion + 1] if posicion < len(indice) - 1 else None

    archivos = "\n".join(
        f'      <li><a href="{BASE_GITHUB}/{ruta}/{esc(f)}">{esc(f)}</a></li>'
        for f in curriculum.CLASS_FILES
    )

    muestra = json.dumps(
        {k: resultado[k] for k in list(resultado)[:6]},
        indent=2, ensure_ascii=False, default=str,
    )

    contenido = f"""
<div class="wrap">
  <p class="crumb"><a href="../index.html">Inicio</a> ·
    <a href="../parts/part-{esc(parte['id'])}.html">Parte {esc(parte['id'])} — {esc(parte['title'])}</a></p>
  <h1 class="page">{esc(clase['id'])} — {esc(clase['title'])}</h1>
  <div class="meta">
    {_nivel_tag(parte['level'])}
    <span>clase {clase['index_in_part']} de {len(parte['classes'])}</span>
    <span>4 horas</span>
    <span>demostración <code>{esc(nombre)}</code></span>
  </div>
  <p><button class="done-toggle" id="done" data-class="{esc(clase['id'])}" aria-pressed="false">Marcar como completada</button></p>

  <h2>Qué calcula el laboratorio</h2>
  <p>{esc(resumen)}</p>
  <pre><code>python {esc(ruta)}/lab.py
compmath run {esc(clase['id'])}</code></pre>

  <h2>Salidas del laboratorio ({len(resultado)})</h2>
  <ul class="clean">
{salidas}
  </ul>

  <h2>Muestra de la ejecución real</h2>
  <pre><code>{esc(muestra)}</code></pre>

  <h2>Idea rectora de la parte</h2>
  <div class="callout">{esc(idea)}</div>

  <h2>Error a evitar</h2>
  <div class="callout warn">{esc(error)}</div>

  <h2>Conexión con IA</h2>
  <p>{esc(parte['ai_link'])}</p>

  <h2>Archivos de la clase</h2>
  <ul class="clean">
{archivos}
  </ul>

  <div class="nav-classes">
    {f'<a class="btn ghost" href="{esc(anterior["id"])}.html">← {esc(anterior["id"])} {esc(anterior["title"])}</a>' if anterior else '<span></span>'}
    {f'<a class="btn ghost" href="{esc(siguiente["id"])}.html">{esc(siguiente["id"])} {esc(siguiente["title"])} →</a>' if siguiente else '<span></span>'}
  </div>
</div>
"""
    return _layout(f"{clase['id']} — {clase['title']}", contenido, prefijo="../",
                   descripcion=f"{clase['title']} · {resumen}")


def _404() -> str:
    contenido = """
<div class="wrap">
  <h1 class="page" style="margin-top:60px">404 — esa página no existe</h1>
  <p class="sub">Puede que el enlace esté desactualizado o que la clase se haya renombrado.</p>
  <p><a class="btn" href="/computational-mathematics-program/">Volver al inicio</a></p>
</div>
"""
    return _layout("404 — Computational Mathematics Program", contenido,
                   descripcion="Página no encontrada")


def _copiar_manual() -> list[str]:
    """Copia el manual a site/downloads si ya está construido."""
    origen = ROOT / "manual"
    copiados = []
    for nombre in ("computational-mathematics-program-manual.html",
                   "computational-mathematics-program-manual.pdf"):
        ruta = origen / nombre
        if ruta.exists():
            shutil.copy2(ruta, SITE / "downloads" / nombre)
            copiados.append(nombre)
    if not copiados:
        print("  · manual no encontrado: ejecuta `python scripts/build_manual.py` antes "
              "si quieres publicarlo en el sitio.")
    return copiados


def generar() -> int:
    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "assets").mkdir(parents=True)
    (SITE / "parts").mkdir()
    (SITE / "classes").mkdir()
    (SITE / "data").mkdir()
    (SITE / "downloads").mkdir()

    partes = curriculum.parts()
    indice = list(curriculum.classes())

    catalogo = []
    for clase in indice:
        nombre, _ = engines.demo_for_class(clase["id"])
        catalogo.append({
            "id": clase["id"],
            "title": clase["title"],
            "part": clase["part"],
            "part_title": clase["part_title"],
            "level": clase["level"],
            "demo": nombre,
        })

    (SITE / "assets" / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    (SITE / "assets" / "app.js").write_text(APP_JS.strip() + "\n", encoding="utf-8")
    (SITE / "data" / "catalog.json").write_text(
        json.dumps(catalogo, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    (SITE / "index.html").write_text(_index(partes, catalogo), encoding="utf-8")
    (SITE / "404.html").write_text(_404(), encoding="utf-8")

    for parte in partes:
        (SITE / "parts" / f"part-{parte['id']}.html").write_text(_part_page(parte), encoding="utf-8")

    for clase in indice:
        parte = curriculum.part(clase["part"])
        (SITE / "classes" / f"{clase['id']}.html").write_text(
            _class_page(clase, parte, indice), encoding="utf-8")

    manifest = {
        "name": "Computational Mathematics Program",
        "short_name": "CompMath",
        "start_url": "./index.html",
        "scope": "./",
        "display": "standalone",
        "background_color": "#0b0d13",
        "theme_color": "#7c5cff",
        "description": "Programa de matemática computacional en español, de cero a la matemática de la IA.",
        "lang": "es",
        "icons": [{
            "src": "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%A7%AE%3C/text%3E%3C/svg%3E",
            "sizes": "any",
            "type": "image/svg+xml",
        }],
    }
    (SITE / "manifest.webmanifest").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (SITE / "service-worker.js").write_text(
        (SERVICE_WORKER % {"version": __version__}).strip() + "\n", encoding="utf-8")
    (SITE / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {PAGES_URL}sitemap.xml\n", encoding="utf-8")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")

    urls = [PAGES_URL]
    urls += [f"{PAGES_URL}parts/part-{p['id']}.html" for p in partes]
    urls += [f"{PAGES_URL}classes/{c['id']}.html" for c in indice]
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sitemap += [f"  <url><loc>{u}</loc></url>" for u in urls]
    sitemap.append("</urlset>")
    (SITE / "sitemap.xml").write_text("\n".join(sitemap) + "\n", encoding="utf-8")

    _copiar_manual()

    archivos = sum(1 for _ in SITE.rglob("*") if _.is_file())
    print(f"OK: sitio generado en site/ — {archivos} archivos, "
          f"{len(partes)} páginas de parte, {len(indice)} páginas de clase.")
    return 0


if __name__ == "__main__":
    raise SystemExit(generar())
