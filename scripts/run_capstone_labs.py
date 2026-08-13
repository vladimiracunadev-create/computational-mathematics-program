"""Ejecuta los 18 laboratorios capstone como procesos independientes.

`compmath run --all` importa los motores dentro del mismo proceso. Este script
comprueba algo distinto: que cada `lab.py` funciona **por sí solo**, tal como lo
ejecutaría un estudiante recién clonado el repositorio.

    python scripts/run_capstone_labs.py
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from computational_math import curriculum  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    # Última clase de cada parte: 020, 040, …, 360.
    capstones = [parte["classes"][-1]["id"] for parte in curriculum.parts()]
    fallos = 0
    inicio = time.perf_counter()

    for class_id in capstones:
        clase = curriculum.find_class(class_id)
        lab = curriculum.class_dir(clase) / "lab.py"
        proceso = subprocess.run(  # noqa: S603 - script del propio repositorio
            [sys.executable, str(lab)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            cwd=ROOT,
        )
        if proceso.returncode == 0:
            print(f"OK     {class_id} {clase['title']}")
        else:
            fallos += 1
            print(f"FALLO  {class_id} {clase['title']} (código {proceso.returncode})")
            print((proceso.stderr or proceso.stdout)[-1500:])

    duracion = time.perf_counter() - inicio
    print(f"\n{len(capstones) - fallos}/{len(capstones)} capstones ejecutados en {duracion:.1f} s")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
