# Roadmap

Este documento describe qué está hecho y qué no. Nada aparece como «listo» si no se
puede verificar con un comando del propio repositorio.

## ✅ v0.1 — contenido base (2026-08-09)

- 18 partes y 360 clases declaradas.
- Contrato de 12 archivos por clase.
- Rutas por perfil e integración con el ecosistema.

## ✅ v0.2 — programa ejecutable y verificable (2026-08-13, actual)

| Objetivo | Verificación |
|---|---|
| Fuente de verdad única | `curriculum.yaml` → `scripts/generate_classes.py --check` |
| 18 motores didácticos ejecutables | `compmath run --all` |
| Una demostración real por clase | `compmath show <clase>` |
| CLI del programa | `compmath --help` |
| Portal HTML estático y offline | `python scripts/generate_site.py && python scripts/validate_site.py` |
| Suite de tests | `python -m unittest discover -s tests -v` |
| CI multiplataforma | 3 sistemas operativos × 3 versiones de Python |
| Seguridad continua | `pip-audit`, `bandit`, `zizmor`, CodeQL |

## 🔜 v0.3 — profundidad matemática

- [ ] Derivaciones formales escritas por clase (hoy la derivación es un método guiado,
      no una demostración cerrada). Es la brecha más honesta que tiene el programa.
- [ ] Ejercicios con solución verificable automáticamente, no solo enunciados.
- [ ] Visualizaciones SVG generadas por los propios motores (sin matplotlib) e
      incrustadas en las páginas de clase.
- [ ] Diagnóstico inicial que recomiende por qué parte empezar.
- [ ] Traza de prerrequisitos clase a clase, no solo parte a parte.

## 🔭 v0.4 — producto educativo

- [ ] Exportación a PDF por parte y manual completo, generados desde `curriculum.yaml`.
- [ ] Modo instructor: generación de exámenes con semilla por estudiante.
- [ ] Notebooks ejecutados en CI para garantizar que no se rompen.
- [ ] Track opcional con NumPy/SciPy paralelo al de biblioteca estándar.

## 🎯 v1.0 — programa completo

- [ ] Rúbricas aplicadas y capstones con criterios de corrección automática.
- [ ] Cobertura de tests medida y publicada.
- [ ] Revisión externa del contenido matemático por al menos una persona con formación
      formal en el área. **Hasta que eso ocurra, el programa no se declarará 1.0.**

## Fuera de alcance (decisiones tomadas, no pendientes)

- **No** se implementarán motores optimizados con BLAS: el objetivo es legibilidad.
- **No** habrá dependencia obligatoria de NumPy ni de ningún framework de deep learning.
- **No** se añadirán servicios en línea, cuentas ni telemetría.
- **No** se emitirán certificados: este repositorio no acredita nada.
