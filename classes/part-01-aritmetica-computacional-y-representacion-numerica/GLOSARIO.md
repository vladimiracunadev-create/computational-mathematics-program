# 📖 Glosario — Parte 01: Aritmética computacional y representación numérica

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md) ·
> [📚 Glosario general](../../docs/GLOSSARY.md)

18 términos definidos con la precisión que exige esta parte. Cada uno enlaza
a la clase donde se estudia y se ejecuta.

| Término | Definición | Clase |
|---|---|---|
| **Base posicional** | Sistema en el que el valor de un dígito depende de su posición. Cambiar de base no cambia la cantidad, solo su escritura. | [023](023-binario-octal-y-hexadecimal/README.md) |
| **Bit** | Unidad mínima de información: dos estados posibles. n bits codifican 2ⁿ valores distintos. | [021](021-bits-bytes-y-sistemas-de-numeracion/README.md) |
| **Cancelación catastrófica** | Pérdida masiva de dígitos significativos al restar dos números casi iguales. No lanza excepción. | [032](032-cancelacion-catastrofica/README.md) |
| **Complemento a dos** | Codificación de enteros con signo en la que el negativo de x es 2ⁿ − x. Permite sumar positivos y negativos con el mismo circuito. | [025](025-enteros-con-signo-y-complemento-a-dos/README.md) |
| **Epsilon de máquina** | Menor ε tal que 1 + ε ≠ 1. En float64 vale 2⁻⁵² ≈ 2.22e−16. | [031](031-ulp-y-machine-epsilon/README.md) |
| **Error absoluto** | Diferencia |aproximado − exacto|. Depende de la escala y no es comparable entre magnitudes distintas. | [030](030-error-absoluto-y-error-relativo/README.md) |
| **Error relativo** | Error absoluto dividido por el valor exacto. Es la magnitud que se propaga y la que define la precisión. | [030](030-error-absoluto-y-error-relativo/README.md) |
| **Estabilidad numérica** | Propiedad de un algoritmo que no amplifica los errores de redondeo más allá de lo que el problema exige. | [036](036-estabilidad-de-algoritmos/README.md) |
| **Exponente sesgado** | Exponente almacenado con un desplazamiento (1023 en float64) para poder representarlo sin signo. | [028](028-ieee-754-estructura-de-un-float/README.md) |
| **Mantisa** | Parte significativa de un número en punto flotante. Determina la precisión relativa, no el rango. | [028](028-ieee-754-estructura-de-un-float/README.md) |
| **Número de condición** | Factor por el que un problema amplifica el error relativo de la entrada. Es propiedad del problema. | [035](035-condicionamiento-de-problemas/README.md) |
| **Overflow** | Resultado que excede el rango representable. En ancho fijo produce wraparound silencioso, no una excepción. | [026](026-rango-overflow-y-wraparound/README.md) |
| **Precisión arbitraria** | Aritmética cuya precisión se declara y no está limitada por el hardware, a cambio de velocidad. | [037](037-precision-arbitraria-y-decimal/README.md) |
| **Punto fijo** | Representación con número fijo de decimales, típicamente enteros de la unidad mínima (centavos). Exacta dentro de su rango. | [027](027-punto-fijo-frente-a-punto-flotante/README.md) |
| **Reproducibilidad numérica** | Propiedad de un cálculo que devuelve bit a bit el mismo resultado. Exige fijar el orden de las operaciones, no solo la semilla. | [039](039-reproducibilidad-numerica-entre-plataformas/README.md) |
| **Subnormal** | Número flotante menor que el mínimo normal, representado con mantisa desnormalizada y precisión reducida. | [033](033-overflow-y-underflow-flotante/README.md) |
| **Suma compensada** | Técnica (Kahan, o math.fsum) que arrastra el error de redondeo para que la suma de muchos términos conserve precisión. | [034](034-propagacion-de-errores/README.md) |
| **ULP** | Unit in the Last Place: distancia entre un float y su vecino. Depende de la magnitud del número. | [031](031-ulp-y-machine-epsilon/README.md) |

## Cómo usar este glosario

No memorices las definiciones: **usa la columna de clase**. Un término se entiende cuando
puedes ejecutar su demostración y explicar qué comprueba, no cuando puedes recitar su
definición.

```bash
compmath show <clase>    # ficha de la clase donde vive el término
compmath run <clase>     # ejecutar su demostración
```

---

> [⬆️ Volver a la parte](README.md) · [🏠 Programa](../../README.md)
