# Registro de fuentes

`bibliography.json` es el aparato que hace **comprobable** lo que las clases citan.

El contenido de las clases ya estaba: cada una cita obras reales, con capítulo cuando
aplica. Lo que faltaba era poder responder a la pregunta *«¿esa obra existe y este enlace
lleva de verdad a ella?»* sin que la respuesta dependa de la buena fe de nadie.

## La política

> Toda afirmación del programa se apoya en una entrada de este registro.
> Ninguna entrada se acepta sin localizador verificable.

Tres consecuencias que se aplican sin excepción:

1. **No se inventa.** Ningún ISBN, DOI, URL ni fecha se escribe «de memoria». Lo que no se
   resuelve contra su autoridad queda `pendiente` con la razón escrita.
2. **No se borra.** Una fuente que deja de resolver se marca; nunca desaparece del registro.
   Una bibliografía que se limpia sola es una bibliografía que miente.
3. **Un hueco declarado es información.** Un hueco rellenado a ojo es una invención con
   formato de bibliografía.

## El esquema

```jsonc
{
  "schema_version": 1,
  "verified_on": "AAAA-MM-DD",     // última resolución en red
  "policy": "…",
  "entries": [
    {
      "id": "apellido-titulo",      // kebab-case estable, único
      "key": "isbn:…|doi:…|url:…",  // clave canónica: agrupa las URL de una misma obra
      "type": "book | paper | standard | reference | dataset",
      "authors": ["Apellido, N."],
      "title": "Título exacto",
      "published": "AAAA",
      "isbn13": "9780000000000",    // solo libros
      "doi": "10.xxxx/…",           // solo artículos
      "url": "https://…",           // el enlace que la clase cita
      "locator": "https://…",       // forma canónica según el tipo
      "authority": "quién responde por la fuente",
      "accessed": "AAAA-MM-DD",
      "used_in": ["classes/part-NN-…/NNN-…"],
      "status": "verificada | pendiente",
      "note": "qué se comprobó, o por qué sigue pendiente"
    }
  ]
}
```

### Forma canónica del `locator`

| Tipo | Localizador | Autoridad |
|---|---|---|
| `book` | `https://openlibrary.org/isbn/{isbn13}` | agencia ISBN, comprobada vía Open Library |
| `paper` | `https://doi.org/{doi}` | Crossref o DataCite |
| `standard`, `reference`, `dataset` | URL de la fuente primaria, con `accessed` | el organismo que la publica |

El verificador exige que `locator` **sea exactamente** esa forma. Un libro sin ISBN-13 con
dígito de control válido no puede ser `book`; un artículo sin DOI no puede ser `paper`.

### Excepción declarada: fuentes sin https

Dos obras se publican en sedes de autor que no sirven https con certificado válido. No se
las expulsa del registro ni se les inventa un espejo: se quedan `pendiente` y su `note` lo
dice. El verificador solo acepta un `locator` `http://` si la entrada está `pendiente` y lo
explica.

## Las dos capas

Separadas a propósito. Si la red entra en el CI, el CI se vuelve inestable y se acaba
ignorando.

| | `scripts/verify_sources.py` | `scripts/refresh_sources.py` |
|---|---|---|
| Red | no | sí |
| Dónde corre | CI, en cada push | a mano o programado |
| ¿Bloquea? | **sí** | no |
| Qué comprueba | esquema, dígito de control del ISBN, forma del localizador, cobertura, bloques repetidos, cifras del README | que el ISBN, el DOI y la URL resuelven de verdad y describen la obra citada |

```bash
python scripts/verify_sources.py          # verifica (lo que corre en CI)
python scripts/verify_sources.py --sync   # recalcula usos y cifras del README
python scripts/refresh_sources.py         # resuelve en red y actualiza estados
```

### La edición importa

Cuando una obra se cita sin ISBN, `refresh-sources` la busca en Open Library, pero **solo
adopta el ISBN de la edición que la clase cita**: título, apellido del primer autor y año
tienen que coincidir los tres. Una edición distinta no es la fuente que la clase usó, y dar
su ISBN por bueno sería mandar al lector a un libro que no dice lo que la clase afirma que
dice. Cuando la edición citada no está, la entrada se queda `pendiente` y `note` enumera
las ediciones que sí existen.

## Cómo leer `status`

- **`verificada`** — el localizador resolvió contra su autoridad **y** el título que devolvió
  coincide con el que cita la clase.
- **`pendiente`** — una de tres: la autoridad no respondió, la sede bloquea peticiones
  automáticas, o el localizador resuelve a una obra **distinta** de la citada. En este último
  caso `note` dice a qué obra resuelve: es un defecto real del enlace de la clase, y queda
  anotado hasta que se corrija con una fuente comprobada.

Una entrada `pendiente` no es una obra dudosa: es una obra cuya trazabilidad todavía no se
pudo cerrar sin inventar nada.
