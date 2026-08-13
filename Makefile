.PHONY: help install generate manual site validate test lint labs capstones all clean

PYTHON ?= python

help:  ## Muestra esta ayuda
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

install:  ## Instala el paquete en modo editable
	$(PYTHON) -m pip install -e .

generate:  ## Regenera clases, catálogo, rutas e integraciones desde curriculum.yaml
	$(PYTHON) scripts/generate_classes.py

manual:  ## Construye el manual completo en HTML y PDF
	$(PYTHON) scripts/build_manual.py

site: manual  ## Genera y valida el portal estático en site/ (incluye el manual)
	$(PYTHON) scripts/generate_site.py
	$(PYTHON) scripts/validate_site.py

validate:  ## Validación estricta del repositorio (la que corre en CI)
	$(PYTHON) scripts/generate_classes.py --check
	$(PYTHON) scripts/validate_repository.py --strict

test:  ## Ejecuta la suite de tests
	$(PYTHON) -m unittest discover -s tests -v

lint:  ## Comprueba el estilo con ruff
	$(PYTHON) -m ruff check src scripts tests

labs:  ## Ejecuta las 360 demostraciones
	$(PYTHON) -m computational_math run --all --quiet

capstones:  ## Ejecuta los 18 laboratorios capstone como scripts independientes
	$(PYTHON) scripts/run_capstone_labs.py

all: generate manual site validate test lint labs capstones  ## Todo lo que exige CI

clean:  ## Borra artefactos generados y cachés
	rm -rf site .ruff_cache .pytest_cache build dist *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
