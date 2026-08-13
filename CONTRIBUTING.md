# Contribuir

Gracias por el interés. Este repositorio tiene una regla que lo gobierna todo:

> **Las clases son artefactos derivados. No se editan a mano.**

Editar un archivo dentro de `classes/` se pierde en la siguiente regeneración, y CI lo
detecta con `python scripts/generate_classes.py --check`.

## Dónde se cambia cada cosa

| Quieres cambiar… | Edita… |
|---|---|
| el título, orden o metadata de una clase | `curriculum.yaml` |
| qué calcula el laboratorio de una clase | `src/computational_math/engines/partNN.py` |
| la redacción común de los 12 archivos de clase | `scripts/generate_classes.py` |
| el portal web | `scripts/generate_site.py` |
| las reglas de validación | `scripts/validate_repository.py` |

Después de cualquiera de esos cambios:

```bash
python scripts/generate_classes.py
python scripts/generate_site.py
python -m unittest discover -s tests -v
python scripts/validate_repository.py --strict
```

## Reglas del contenido

1. **Ninguna afirmación sin comprobación.** Si una demostración dice que dos cosas
   coinciden, debe devolver la clave booleana que lo comprueba.
2. **Todo lo aleatorio lleva semilla fija** y la declara en su salida.
3. **Biblioteca estándar en los motores.** NumPy, SciPy o PyTorch solo pueden aparecer
   dentro de un `try/except ImportError` que degrade con aviso.
4. **Toda referencia bibliográfica lleva año** y es verificable.
5. **Declara los límites.** Si una demostración solo funciona en un caso pequeño o bajo
   una hipótesis concreta, dilo en su propia salida.
6. **No inventes precisión.** Un resultado numérico sin tolerancia declarada no es un
   resultado.

## Estilo de código

- Python 3.11 o superior, con `from __future__ import annotations`.
- `ruff check .` debe pasar sin avisos.
- Nombres de funciones y claves de salida en español cuando describen matemática en
  español; en inglés cuando son términos técnicos consolidados (`softmax`, `backward`).
- Docstring de una línea en cada demostración: es el texto que aparece en la clase
  generada y en el sitio.

## Pull requests

1. Rama desde `main`.
2. Los cuatro comandos de arriba en verde localmente.
3. Describe **qué afirmación nueva** introduce el cambio y **cómo se verifica**.
4. Un cambio de versión toca a la vez `pyproject.toml`,
   `src/computational_math/__init__.py` y `curriculum.yaml`; CI falla si se desincronizan.

## Lo que no se acepta

- Contenido copiado de libros, cursos o repositorios de terceros.
- Resultados numéricos sin la implementación que los produce.
- Afirmaciones sobre rendimiento o "nivel profesional" sin evidencia en el propio repositorio.
- Dependencias nuevas en el núcleo: si algo no se puede hacer con la biblioteca estándar,
  va en un extra opcional.
