# Intuición — Entropía cruzada

## La pregunta antes de la fórmula

¿Qué problema resuelve **Entropía cruzada**? Describe, sin símbolos, qué entra,
qué sale y cómo debería cambiar el resultado si una entrada crece, decrece o se
vuelve extrema. Si no puedes decirlo en una frase, todavía no entiendes el objeto:
entiendes su notación.

## Dónde encaja

Esta clase pertenece a **Teoría de la información, señales y series**. Entropía, entropía cruzada, divergencias, información mutua, codificación, muestreo, convolución, Fourier, FFT, filtros y series temporales.

## Analogía y sus límites

Construye una analogía cotidiana y, en la línea siguiente, escribe dónde deja de
funcionar. Una analogía sin límites declarados produce confianza sin comprensión.

## Predicción antes del laboratorio

El laboratorio ejecuta `cross_entropy`: entropía cruzada: el coste de codificar p con un código para q.

Antes de correrlo, predice tres casos:

1. **Normal** — la situación típica.
2. **Límite** — el valor extremo del dominio válido.
3. **Inválido** — una entrada fuera del dominio, y qué debería ocurrir.

Después compara con las salidas reales. Registra las tres predicciones en el
notebook antes de ejecutar nada.

## Señal de que lo entendiste

Puedes explicar por qué el resultado es el que es **sin volver a mirar el código**,
y puedes construir un caso donde tu explicación falle.
