# Guía del instructor

## Qué te da este repositorio

- 360 clases con contrato uniforme de 12 archivos.
- 360 laboratorios ejecutables, deterministas y sin dependencias que instalar.
- Rúbrica ponderada por clase y criterios de error crítico.
- Un portal web estático que puedes servir en la red del aula sin conexión a internet.
- Validación automática: si el material se rompe, CI lo dice.

## Qué NO te da

- Corrección automática de los ejercicios (llega en v0.3).
- Banco de exámenes con variantes por estudiante.
- Acreditación de ningún tipo.
- Contenido en otro idioma que no sea español.

## Preparar el aula

```bash
git clone https://github.com/vladimiracunadev-create/computational-mathematics-program.git
cd computational-mathematics-program
pip install -e .
python scripts/generate_site.py
python -m http.server 8000 --directory site
```

Los estudiantes acceden desde la red local. El portal funciona **sin internet**: no
carga fuentes, CDN ni analítica. El service worker lo deja disponible offline tras la
primera visita.

Si no puedes instalar Python en las máquinas del aula, reparte la carpeta `site/`: se
abre con doble clic en `index.html`.

## Estructura de una sesión de 2 horas

| Tiempo | Actividad | Material |
|---|---|---|
| 0–15 min | Pregunta motivadora y **predicción escrita** de los tres casos | `intuition.md` |
| 15–45 min | Exposición del modelo y sus tres capas | `theory.md` |
| 45–75 min | Derivación en pizarra, paso por paso, con los estudiantes | `derivation.md` |
| 75–100 min | Laboratorio en parejas; contraste con la predicción inicial | `lab.py` |
| 100–120 min | Puesta en común de discrepancias y cierre | `assessment.md` |

La predicción escrita del primer bloque es el instrumento pedagógico central: permite
distinguir «no lo sabía» de «creía saberlo».

## Calendarios sugeridos

### Semestre de 16 semanas (una parte por semana, partes 00–15)

| Semanas | Partes | Foco |
|---|---|---|
| 1–2 | 00, 01 | aritmética, representación numérica y error |
| 3–4 | 02, 03 | álgebra, funciones y geometría analítica |
| 5 | 04 | matemática discreta |
| 6–7 | 05, 06 | álgebra lineal y descomposiciones |
| 8–9 | 07, 08 | cálculo y autodiferenciación |
| 10–11 | 09, 10 | probabilidad e inferencia |
| 12 | 11 | métodos numéricos |
| 13 | 12 | optimización |
| 14 | 13 | información y señales |
| 15–16 | 14, 15 | matemática de ML y Deep Learning |

Las partes 16 y 17 quedan como curso avanzado o seminario de lectura de papers.

### Curso corto de 8 semanas: «Matemática para Deep Learning»

Partes 05, 06, 07, 08, 12, 13, 15 y 16. 160 clases, dos por sesión.

### Taller intensivo de 5 días

Una parte por día: 05, 07, 08, 12, 15. Solo laboratorios y capstones.

## Evaluación

Cada clase trae su rúbrica en `assessment.md`:

| Criterio | Peso |
|---|---:|
| Comprensión conceptual | 25 % |
| Resolución manual | 25 % |
| Implementación y verificación | 25 % |
| Interpretación y comunicación | 15 % |
| Conexión con aplicación real | 10 % |

Aprobación recomendada: **80/100 y ningún error conceptual crítico**.

Cada parte propone además su propio reparto:

| Componente de parte | Peso |
|---|---:|
| Clases y ejercicios | 40 % |
| Laboratorios y notebooks | 25 % |
| Explicación oral o escrita | 15 % |
| Capstone de la parte | 20 % |

### Errores conceptuales críticos

Independientemente de la nota numérica, considera no superada una entrega que:

- confunda el modelo matemático con su representación en máquina;
- afirme exactitud sin declarar tolerancia;
- generalice a partir de un único caso favorable;
- presente un resultado numérico sin verificación independiente.

## Detectar entregas sin comprensión

Las tres señales más fiables:

1. **El notebook está correcto pero la predicción inicial está vacía.** Ejecutó primero.
2. **Explica el código en lugar de explicar el resultado.** Pide el párrafo sin código
   que exige el entregable.
3. **Todas las tolerancias son `1e-9` sin justificación.** El notebook de estudiante pide
   explícitamente justificar esa elección.

Pregunta de control que funciona siempre: *«¿qué entrada haría que este resultado dejara
de ser fiable?»*

## Capstones por parte

Cada parte termina en una clase capstone (`020`, `040`, `060`, …, `360`) con una
demostración de mayor alcance. Sirven bien como entrega evaluable de parte:

| Parte | Capstone | Entregable natural |
|---|---|---|
| 01 | auditor de precisión numérica | informe de dígitos perdidos en tres expresiones |
| 06 | PCA y compresión | tabla de error frente a rango retenido |
| 08 | backpropagation manual y automática | derivación a mano que coincida con el motor |
| 12 | banco de optimizadores | comparación con protocolo declarado |
| 14 | seis algoritmos de ML | misma partición, seis objetivos distintos |
| 15 | red neuronal desde cero | red entrenada y brecha train/test discutida |
| 16 | mini-Transformer | interpretación del sesgo relativo aprendido |
| 17 | reproducir una idea de un paper | predicción teórica frente a resultado obtenido |

## Adaptar el material

Cambia `curriculum.yaml` (títulos, orden, metadata de parte) o el motor de la parte
(qué calcula cada laboratorio) y regenera:

```bash
python scripts/generate_classes.py
python scripts/generate_site.py
python scripts/validate_repository.py --strict
```

No edites archivos dentro de `classes/`: se pierden en la siguiente regeneración.

## Licencia para uso en aula

Código y documentación original bajo MIT: puedes usarlo, adaptarlo y redistribuirlo,
incluso comercialmente, conservando el aviso de licencia. Los libros y papers citados
mantienen la suya.
