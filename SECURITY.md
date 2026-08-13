# Política de seguridad

## Alcance

Este es un repositorio educativo sin servicios en línea, sin base de datos y sin
credenciales. La superficie de riesgo es la habitual de un paquete Python y de un
sitio estático:

- dependencias del entorno de desarrollo;
- workflows de GitHub Actions;
- código de ejemplo que un tercero podría ejecutar.

## Versiones soportadas

| Versión | Soporte |
|---|---|
| 0.2.x | ✅ |
| 0.1.x | ❌ |

## Reportar una vulnerabilidad

Usa **GitHub Security Advisories** (pestaña *Security* → *Report a vulnerability*) para
un reporte privado. Si no es posible, abre un issue **sin detalles explotables** y pide
un canal privado.

Compromiso de respuesta: acuse de recibo en 7 días naturales, evaluación en 30.

## Garantías del propio repositorio

- **Ningún laboratorio descarga ni ejecuta código remoto.** Todo dato es sintético y
  se genera localmente con semilla fija.
- **Sin secretos.** Los workflows no requieren ningún secreto más allá del `GITHUB_TOKEN`
  automático, y con permisos de solo lectura salvo el despliegue de Pages.
- **Acciones fijadas por SHA**, nunca por etiqueta móvil.
- **El sitio publicado no carga recursos externos**: sin CDN, sin fuentes remotas, sin
  analítica. Un test lo verifica en cada push.
- **Análisis continuo**: `pip-audit` (dependencias), `bandit` (SAST), `zizmor`
  (workflows) y CodeQL, en cada push y semanalmente.

## Nota sobre `random` en los laboratorios

Las demostraciones usan `random` para generar datos didácticos con semilla fija. Ese uso
**no es criptográfico** y está declarado explícitamente en cada salida. Nunca uses el
generador de este programa para claves, tokens o nonces: para eso está `secrets`.

## Fuera de alcance

- Vulnerabilidades en dependencias opcionales que el programa no instala por defecto
  (`scientific`, `ai`, `research`).
- Resultados numéricos incorrectos por mal uso: son errores de contenido, no de
  seguridad; repórtalos como issue normal.
