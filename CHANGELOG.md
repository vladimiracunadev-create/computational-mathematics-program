# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Este proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

## [0.2.0] — 2026-08-13

Reescritura del núcleo del programa: el contenido pasa de plantilla a artefacto
verificable, generado desde una única fuente de verdad y ejecutable de punta a punta.

### Añadido

- `curriculum.yaml` como **fuente de verdad única**: 18 partes con resumen, ideas
  centrales, errores frecuentes, stack, conexión con IA y bibliografía primaria.
- **18 motores didácticos ejecutables** (`src/computational_math/engines/`) escritos en
  Python estándar, con 360 demostraciones deterministas —una por clase—, entre ellas:
  autodiferenciación en modo reverso, MLP entrenado desde cero, mini-Transformer causal,
  banco comparable de optimizadores, SVD, PCA, Sinkhorn y clustering espectral.
- Álgebra lineal en Python puro (`engines/_linalg.py`): Gauss con pivoteo, LU, QR,
  autovalores por Jacobi, SVD, pseudoinversa y covarianza.
- CLI `compmath` con `catalog`, `show`, `run`, `validate`, `progress` y `stats`.
- `scripts/generate_classes.py`: regenera las 360 clases y el catálogo; modo `--check`.
- `scripts/generate_site.py`: portal estático HTML/PWA con buscador, filtros por nivel,
  progreso local, 18 páginas de parte y 360 páginas de clase, sin recursos externos.
- `scripts/validate_site.py` y `scripts/validate_pages.py`.
- Suite de tests `unittest` sobre currículo, motores, estructura, CLI y sitio.
- Workflows `ci.yml` (3 sistemas operativos × 3 versiones de Python), `pages.yml`,
  `security.yml` y `codeql.yml`, con todas las acciones fijadas por SHA.
- Documentación nueva: `INSTALL.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`,
  `docs/STUDENT_GUIDE.md`, `docs/INSTRUCTOR_GUIDE.md`, `docs/METHODOLOGY.md`.

### Cambiado

- Las 360 clases se **regeneran** desde el currículo: su contenido cita la demostración
  concreta que ejecutan, sus salidas reales y la bibliografía de su parte.
- `lab.py` de cada clase ejecuta la demostración de su parte en lugar de un cálculo
  genérico idéntico para todas.
- Los tres notebooks por clase dejan de ser plantillas iguales: ejecutan el motor,
  inspeccionan sus salidas y verifican reproducibilidad.
- `scripts/validate_repository.py` reescrito: valida conteos, contrato de archivos,
  notebooks, mapeo clase→motor, catálogo, versiones y afirmaciones del README.
- `pyproject.toml`: dependencia base reducida a PyYAML; NumPy, SciPy, SymPy, PyTorch y
  JAX pasan a extras opcionales. Añadidos clasificadores, URLs y configuración de ruff.
- README reescrito con estado verificable, mapa Mermaid y límites declarados.

### Eliminado

- `SHA256SUMS.txt` (704 KB de sumas generadas que quedaban obsoletas en cada commit).
- `scripts/catalog.py`, sustituido por `compmath catalog`.
- `mkdocs.yml`: el portal se genera con `scripts/generate_site.py`, sin dependencias.

## [0.1.0] — 2026-08-09

- Versión inicial: 18 partes, 360 clases y rutas de integración.
