"""CLI del programa: ``compmath``.

    compmath catalog                 lista las 360 clases
    compmath catalog --part 12       lista una parte
    compmath show 250                ficha de una clase
    compmath run 250                 ejecuta el laboratorio de una clase
    compmath run --part 12           ejecuta las 20 clases de una parte
    compmath run --all               ejecuta las 360 (verificación completa)
    compmath validate                valida la coherencia del repositorio
    compmath progress                estado del avance local
    compmath stats                   conteos del programa
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from typing import Any, Dict, List

from . import __version__, curriculum, engines

PROGRESS_FILE = curriculum.ROOT / ".compmath-progress.json"


def _stdout_utf8() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def _filtrar(part: str | None) -> List[Dict[str, Any]]:
    clases = list(curriculum.classes())
    if part is None:
        return clases
    key = f"{int(part):02d}"
    seleccion = [c for c in clases if c["part"] == key]
    if not seleccion:
        raise SystemExit(f"No existe la parte {part!r}. Usa 00–17.")
    return seleccion


def cmd_catalog(args: argparse.Namespace) -> int:
    clases = _filtrar(args.part)
    if args.json:
        print(json.dumps(clases, indent=2, ensure_ascii=False))
        return 0
    parte_actual = None
    for clase in clases:
        if clase["part"] != parte_actual:
            parte_actual = clase["part"]
            print(f"\n── Parte {parte_actual} — {clase['part_title']} ({clase['level']})")
        print(f"  {clase['id']}  {clase['title']}")
    print(f"\nTotal: {len(clases)} clases")
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    clase = curriculum.find_class(args.class_id)
    parte = curriculum.part(clase["part"])
    demo_name, funcion = engines.demo_for_class(clase["id"])
    directorio = curriculum.class_dir(clase)
    print(f"{clase['id']} — {clase['title']}")
    print(f"Parte {parte['id']} — {parte['title']}  ·  nivel {parte['level']}")
    print(f"Directorio: {directorio.relative_to(curriculum.ROOT)}")
    print(f"Motor: engines.{parte['engine']}  ·  demostración: {demo_name}")
    print(f"Qué hace: {(funcion.__doc__ or '').strip().splitlines()[0]}")
    print("\nIdeas de la parte:")
    for idea in parte["key_ideas"]:
        print(f"  · {idea}")
    print("\nReferencias:")
    for ref in parte["references"]:
        print(f"  · {ref}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    if args.all:
        clases = list(curriculum.classes())
    elif args.part is not None:
        clases = _filtrar(args.part)
    elif args.class_id:
        clases = [curriculum.find_class(args.class_id)]
    else:
        raise SystemExit("Indica una clase, --part NN o --all.")

    fallos = 0
    inicio = time.perf_counter()
    for clase in clases:
        etiqueta = f"{clase['id']} {clase['title']}"
        try:
            resultado = engines.run_class(clase["id"])
        except Exception as exc:  # noqa: BLE001 - se reporta y se continúa
            fallos += 1
            print(f"FALLO  {etiqueta}: {exc}")
            continue
        if len(clases) == 1:
            print(f"{etiqueta}")
            print(json.dumps(resultado, indent=2, ensure_ascii=False, default=str))
        elif not args.quiet:
            print(f"OK     {etiqueta}  ({len(resultado)} salidas)")

    duracion = time.perf_counter() - inicio
    if len(clases) > 1:
        print(f"\n{len(clases) - fallos}/{len(clases)} laboratorios correctos en {duracion:.2f} s")
    return 1 if fallos else 0


def cmd_validate(args: argparse.Namespace) -> int:
    script = curriculum.ROOT / "scripts" / "validate_repository.py"
    if not script.exists():
        raise SystemExit(f"No se encontró {script}")
    orden = [sys.executable, str(script)] + (["--strict"] if args.strict else [])
    # Ejecuta un script del propio repositorio con el intérprete actual: sin entrada externa.
    proceso = subprocess.run(orden, cwd=curriculum.ROOT, check=False)  # nosec B603
    return proceso.returncode


def _cargar_progreso() -> Dict[str, str]:
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {}


def cmd_progress(args: argparse.Namespace) -> int:
    progreso = _cargar_progreso()
    if args.done:
        for class_id in args.done:
            clase = curriculum.find_class(class_id)
            progreso[clase["id"]] = time.strftime("%Y-%m-%d")
        PROGRESS_FILE.write_text(json.dumps(progreso, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Registradas {len(args.done)} clase(s). Total completadas: {len(progreso)}")
        return 0
    if args.reset:
        PROGRESS_FILE.unlink(missing_ok=True)
        print("Progreso reiniciado.")
        return 0

    total = len(list(curriculum.classes()))
    print(f"Progreso: {len(progreso)}/{total} clases ({100 * len(progreso) / total:.1f} %)")
    for parte in curriculum.parts():
        ids = [c["id"] for c in parte["classes"]]
        hechas = sum(1 for i in ids if i in progreso)
        barra = "█" * (hechas * 20 // len(ids)) + "·" * (20 - hechas * 20 // len(ids))
        print(f"  {parte['id']} {barra} {hechas:2d}/{len(ids)}  {parte['title']}")
    print("\nEl progreso es local (.compmath-progress.json) y no se sincroniza.")
    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    totales = curriculum.totals()
    demos = engines.all_class_demos()
    unicas = len(set(demos.values()))
    print(f"Computational Mathematics Program v{__version__}")
    for clave, valor in totales.items():
        print(f"  {clave.replace('_', ' '):24s} {valor}")
    print(f"  {'motores':24s} {len(engines.ENGINE_MODULES)}")
    print(f"  {'demostraciones únicas':24s} {unicas}")
    print(f"  {'clases mapeadas a demo':24s} {len(demos)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="compmath", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--version", action="version", version=f"compmath {__version__}")
    sub = parser.add_subparsers(dest="comando", required=True)

    p = sub.add_parser("catalog", help="lista las clases del programa")
    p.add_argument("--part", help="filtra por parte (00–17)")
    p.add_argument("--json", action="store_true", help="salida en JSON")
    p.set_defaults(func=cmd_catalog)

    p = sub.add_parser("show", help="ficha detallada de una clase")
    p.add_argument("class_id", help="identificador de clase (001–360)")
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("run", help="ejecuta laboratorios")
    p.add_argument("class_id", nargs="?", help="identificador de clase (001–360)")
    p.add_argument("--part", help="ejecuta las 20 clases de una parte")
    p.add_argument("--all", action="store_true", help="ejecuta las 360 clases")
    p.add_argument("--quiet", action="store_true", help="solo muestra el resumen final")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("validate", help="valida la coherencia del repositorio")
    p.add_argument("--strict", action="store_true", help="modo estricto (el que usa CI)")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("progress", help="avance local del estudiante")
    p.add_argument("--done", nargs="+", metavar="CLASE", help="marca clases como completadas")
    p.add_argument("--reset", action="store_true", help="borra el progreso local")
    p.set_defaults(func=cmd_progress)

    p = sub.add_parser("stats", help="conteos del programa")
    p.set_defaults(func=cmd_stats)
    return parser


def main(argv: List[str] | None = None) -> int:
    _stdout_utf8()
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
