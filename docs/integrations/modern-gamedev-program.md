# modern-gamedev-program

Gráficos, física y simulación en videojuegos.

> Este documento define un **puente conceptual**. No duplica ni resume el contenido de
> [`modern-gamedev-program`](https://github.com/vladimiracunadev-create/modern-gamedev-program): lo referencia como
> superficie de aplicación de la matemática que este programa enseña.

## Prerrequisitos matemáticos

| # | Parte | Clases | Horas | Nivel |
|---|---|---:|---:|---|
| 01 | [Aritmética computacional y representación numérica](../../classes/part-01-aritmetica-computacional-y-representacion-numerica/README.md) | 20 | 80 h | basico-computacional |
| 03 | [Geometría, trigonometría y geometría analítica](../../classes/part-03-geometria-trigonometria-y-geometria-analitica/README.md) | 20 | 80 h | basico-intermedio |
| 05 | [Álgebra lineal I: vectores y matrices](../../classes/part-05-algebra-lineal-i-vectores-y-matrices/README.md) | 20 | 80 h | intermedio |
| 07 | [Cálculo diferencial e integral](../../classes/part-07-calculo-diferencial-e-integral/README.md) | 20 | 80 h | universitario |
| 11 | [Métodos numéricos y computación científica](../../classes/part-11-metodos-numericos-y-computacion-cientifica/README.md) | 20 | 80 h | cientifico |

Total: 100 clases.

## Puntos de conexión concretos

| Concepto que usa `modern-gamedev-program` | Clase | Demostración |
|---|---|---|
| Rotaciones 2D | [074](../../classes/part-03-geometria-trigonometria-y-geometria-analitica/074-rotaciones-2d/README.md) | `rotation_2d` |
| Planos y 3D | [077](../../classes/part-03-geometria-trigonometria-y-geometria-analitica/077-geometria-3d-y-planos/README.md) | `planes_3d` |
| Proyección y perspectiva | [078](../../classes/part-03-geometria-trigonometria-y-geometria-analitica/078-proyecciones-y-perspectiva/README.md) | `projection` |
| Motor geométrico | [080](../../classes/part-03-geometria-trigonometria-y-geometria-analitica/080-capstone-motor-geometrico-2d/README.md) | `capstone_geometry_engine` |
| Runge-Kutta | [237](../../classes/part-11-metodos-numericos-y-computacion-cientifica/237-runge-kutta/README.md) | `runge_kutta` |

```bash
compmath show 074
compmath show 077
compmath show 078
compmath show 080
compmath show 237
```

## Cómo usar el puente

1. Identifica el concepto aplicado que no entiendes en `modern-gamedev-program`.
2. Localízalo en la tabla de arriba y abre su clase aquí.
3. Ejecuta su laboratorio **después de escribir tu predicción**.
4. Vuelve al repositorio especializado y repite la aplicación entendiendo la fórmula.

## Qué no hace este puente

- No sustituye el contenido de `modern-gamedev-program`.
- No garantiza que las partes listadas sean suficientes: son el mínimo, no el techo.
- No cubre las herramientas, frameworks ni prácticas de ingeniería de ese repositorio.
