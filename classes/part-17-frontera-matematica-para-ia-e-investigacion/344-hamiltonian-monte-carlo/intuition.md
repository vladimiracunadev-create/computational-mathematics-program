# Intuición — Hamiltonian Monte Carlo

## La pregunta antes de la fórmula

¿Qué problema resuelve **Hamiltonian Monte Carlo**? Describe, sin símbolos, qué entra,
qué sale y cómo debería cambiar el resultado si una entrada crece, decrece o se
vuelve extrema. Si no puedes decirlo en una frase, todavía no entiendes el objeto:
entiendes su notación.

## Dónde encaja

Esta clase pertenece a **Frontera matemática para IA e investigación**. Procesos gaussianos, MCMC avanzado, inferencia variacional, transporte óptimo, geometría diferencial e informacional, SDE, Neural ODE, score matching y teoría del aprendizaje.

## Analogía y sus límites

Construye una analogía cotidiana y, en la línea siguiente, escribe dónde deja de
funcionar. Una analogía sin límites declarados produce confianza sin comprensión.

## Predicción antes del laboratorio

El laboratorio ejecuta `hamiltonian_monte_carlo`: hmc: usar el gradiente para proponer estados lejanos con alta aceptación.

Antes de correrlo, predice tres casos:

1. **Normal** — la situación típica.
2. **Límite** — el valor extremo del dominio válido.
3. **Inválido** — una entrada fuera del dominio, y qué debería ocurrir.

Después compara con las salidas reales. Registra las tres predicciones en el
notebook antes de ejecutar nada.

## Señal de que lo entendiste

Puedes explicar por qué el resultado es el que es **sin volver a mirar el código**,
y puedes construir un caso donde tu explicación falle.
