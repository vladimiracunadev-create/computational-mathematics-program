# Soporte

## Antes de preguntar

Casi todo se responde con estos cuatro comandos:

```bash
compmath stats                # qué contiene realmente el programa
compmath show 250             # qué hace una clase concreta
compmath validate --strict    # si el repositorio es coherente
python -m unittest discover -s tests -v
```

## Dónde preguntar cada cosa

| Situación | Canal |
|---|---|
| Un laboratorio falla o da un resultado imposible | **Issue** con el comando exacto, tu versión de Python y la salida completa |
| Un enlace roto, una errata o una afirmación incorrecta | **Issue** con la ruta del archivo |
| No entiendo una clase | **Discussions → Q&A**, citando el número de clase |
| Quiero proponer una parte o una clase nueva | **Discussions → Ideas** |
| Encontré un problema de seguridad | [SECURITY.md](SECURITY.md), nunca un issue público |

## Problemas frecuentes

**`ModuleNotFoundError: computational_math`**
No instalaste el paquete. Ejecuta `pip install -e .` desde la raíz del repositorio.

**`ImportError: Falta PyYAML`**
Misma causa. PyYAML es la única dependencia obligatoria.

**Los acentos salen mal en la consola de Windows**
Los scripts fuerzan UTF-8 en la salida estándar. Si aun así falla, ejecuta `chcp 65001`
antes de lanzar el comando.

**`compmath` no se encuentra**
El entorno virtual no está activado, o instalaste sin `-e`.

**Un laboratorio tarda unos segundos**
Es esperado en las clases 320, 340 y 360: entrenan modelos reales en Python puro. Las
360 juntas tardan menos de 15 segundos con `compmath run --all`.

## Qué no cubre este soporte

- Resolver los ejercicios por ti.
- Asesoría académica formal o convalidación de estudios.
- Depuración de código propio no relacionado con este repositorio.
