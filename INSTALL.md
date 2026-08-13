# Instalación

## Requisitos

| Requisito | Versión | Obligatorio |
|---|---|---|
| Python | 3.11, 3.12 o 3.13 | ✅ |
| PyYAML | ≥ 6, < 7 | ✅ (se instala automáticamente) |
| Git | cualquiera reciente | recomendado |
| NumPy, SciPy, SymPy, matplotlib, pandas | ver `pyproject.toml` | ⚪ opcional |
| PyTorch, JAX, scikit-learn | ver `pyproject.toml` | ⚪ opcional |

**Ningún laboratorio necesita las dependencias opcionales.** Los 18 motores están
escritos en biblioteca estándar. Las bibliotecas científicas aparecen en los notebooks
como contraste profesional.

## Instalación mínima

```bash
git clone https://github.com/vladimiracunadev-create/computational-mathematics-program.git
cd computational-mathematics-program
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

### Linux y macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Verificación

```bash
compmath stats
compmath run 001
python -m unittest discover -s tests
```

Salida esperada de `compmath stats`:

```text
Computational Mathematics Program v0.2.0
  partes declaradas        18
  partes reales            18
  clases declaradas        360
  clases reales            360
  archivos por clase       12
  notebooks                1080
  horas                    1440
  motores                  18
  demostraciones únicas    360
  clases mapeadas a demo   360
```

## Extras opcionales

```bash
pip install -e ".[scientific]"   # numpy, scipy, sympy, matplotlib, pandas
pip install -e ".[notebooks]"    # jupyterlab
pip install -e ".[ai]"           # scikit-learn, torch
pip install -e ".[research]"     # jax, cvxpy, pymc, networkx
pip install -e ".[dev]"          # ruff
```

Combinables: `pip install -e ".[scientific,notebooks]"`.

## Ejecutar los notebooks

```bash
pip install -e ".[notebooks]"
jupyter lab
```

Abre cualquier `classes/part-NN-*/NNN-*/notebook.ipynb`. Los notebooks localizan la raíz
del repositorio por sí solos, así que funcionan desde cualquier directorio de trabajo.

## Generar el sitio en local

```bash
python scripts/generate_site.py
python scripts/validate_site.py
python -m http.server 8000 --directory site
```

Abre <http://localhost:8000>. El portal también funciona abriendo `site/index.html`
directamente con doble clic (sin servidor y sin conexión).

## Sin instalar el paquete

Si prefieres no instalar nada, todo funciona añadiendo `src/` al path:

```bash
python -c "import sys; sys.path.insert(0,'src'); from computational_math import cli; cli.main(['stats'])"
python scripts/validate_repository.py
```

Los `lab.py` ya lo hacen por su cuenta: `python classes/part-00-*/001-*/lab.py` funciona
en un repositorio recién clonado, con solo PyYAML instalado.

## Desinstalar

```bash
pip uninstall computational-mathematics-program
rm -rf .venv site .compmath-progress.json
```
