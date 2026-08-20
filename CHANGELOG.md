# Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).
Este proyecto sigue [Versionado Semántico](https://semver.org/lang/es/).

## [No publicado]

Bibliografía verificable: las clases ya citaban obras reales, pero nada permitía comprobar
ni que un enlace llevara de verdad a la obra que decía, ni que esa obra tratara de lo que
la clase enseña. Esta entrega añade el aparato que responde a las dos preguntas, y publica
la bibliografía **por parte y por clase** en vez de un tablero de cifras.

### Añadido

- **`sources/areas.yaml`**: vocabulario de 44 áreas —cada una con nombre y definición— y,
  por parte, el área que **enseña** y las áreas con las que **conecta**. Cada obra del
  registro declara en `covers` de qué trata: un hecho sobre la obra, revisable, no una
  deducción de dónde nos convino citarla.
- **Cruce comprobado entre la obra y la clase.** `verify_sources.py` bloquea la CI si una
  clase no cita **ninguna obra del área que enseña** (la documentación de la herramienta no
  sirve de ancla) o si una cita queda **fuera del tema** de su parte y de sus conexiones.
  Hoy: 360 de 360 clases ancladas, 607 citas de tema, 78 de conexión y 40 de herramienta.
- **`docs/BIBLIOGRAPHY.md` generado, por parte y por clase**: qué obra sostiene cada una de
  las 360 clases, **por qué está ahí** (🎯 tema de la clase, 🔗 conexión de la parte,
  🛠️ herramienta del laboratorio) y en qué estado quedó su localizador, más el índice de
  las 333 obras con sus temas y sus citas.
- Campo `areas:` opcional por clase en `content/part-NN.yaml`, para las 30 clases cuyo tema
  no es exactamente el de su parte (los vectores dentro de geometría, el gradiente dentro
  de cálculo).
- **`sources/bibliography.json`**: registro con una entrada por obra citada, cada una con
  localizador resoluble (ISBN-13, DOI o URL de la fuente primaria), autoridad que responde
  por él, fecha de consulta, clases que la usan y estado `verificada` / `pendiente`.
- `src/computational_math/sources.py`: extracción de identificadores que **ya viajan dentro
  de la URL citada** (DOI de Springer y SIAM, ISBN-13 en el sufijo del DOI o en la ficha de
  la editorial, DOI canónico de arXiv), validación del dígito de control del ISBN-13 y
  forma canónica del localizador por tipo.
- `scripts/verify_sources.py`: verificador **offline y determinista**. Corre en CI y
  bloquea. Comprueba esquema, dígito de control, forma del localizador, cobertura completa,
  que ningún DOI escrito en una clase falte del registro, que ningún bloque de fuentes se
  repita entre clases y que las cifras del README coincidan con el recuento.
- `scripts/refresh_sources.py`: resolutor **en red**, manual y sin poder de bloqueo.
  Resuelve ISBN contra Open Library y DOI contra Crossref y DataCite, comprueba las URL y
  reporta lo que dejó de resolver **sin borrarlo**. De un libro sin ISBN solo adopta el de
  **la edición citada** —título, autor y año—, nunca el de otra edición de la misma obra.
- `sources/README.md` con el esquema, la política y cómo leer cada estado.
- `tests/test_sources.py` y el paso «Trazabilidad de fuentes» en el workflow de CI.
- Objetivos `make verify-sources` y `make refresh-sources`.

### Cambiado

- Cada referencia de clase dice ahora **qué área comparte con la clase** y cómo se comprobó
  su localizador, en lugar de la fórmula derivada del dominio de la URL. La sección pasa a
  llamarse «Bibliografía de la clase» en las 360 clases, en el sitio y en el manual, que
  comparten el mismo renderizador.
- **Cinco obras dejaron de apuntar a la portada de su editorial.** Ross, Oppenheim, Burden,
  Casella y Bracewell citaban `pearson.com`, `cengage.com` o `mheducation.com` a secas: el
  registro agrupa por localizador, así que *A First Course in Probability* y
  *Discrete-Time Signal Processing* figuraban como **una misma obra**. Las 27 citas
  afectadas resuelven ahora contra su ISBN-13 en Open Library, ya verificado.
- Tres obras que estaban duplicadas bajo dos localizadores (Rumelhart, Tibshirani,
  Oppenheim) quedan en una sola entrada, con el DOI o el ISBN como localizador canónico.
- La clase 138 («Broadcasting como operación tensorial») se apoyaba **solo** en la
  documentación de NumPy y PyTorch; añade *Array programming with NumPy* (Nature, 2020),
  que es la fuente primaria de esa semántica.
- El README sustituye el tablero de cifras por la **bibliografía**: qué se comprueba y qué
  no, un bloque real de clase generado y la obra rectora de cada una de las 18 partes.
- La comprobación de que ningún bloque de fuentes se repite se retira: forzaba a meter el
  título de la clase en cada línea para diferenciarlas. La sustituye el cruce por áreas,
  que comprueba lo que importaba de verdad.
- El README enlaza el registro y publica sus cifras y la obra rectora de cada etapa; las
  cifras las produce el verificador (`--sync`), ya no se escriben a mano.
- Dos enlaces de clase pasan de `http` a `https` tras comprobar que la sede lo sirve.

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
