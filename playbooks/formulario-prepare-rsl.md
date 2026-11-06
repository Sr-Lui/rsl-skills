# Prepare formulario UTP (rsl-resultado-formulario-prepare)

Prosa biblio breve: [`formulario-prosa-rsl.md`](formulario-prosa-rsl.md) (filas 3–13, **una línea** en español).

Implementación biblio: [`scripts/formulario_biblio_enrich.py`](../scripts/formulario_biblio_enrich.py) (`enrich_study`, `MANUAL_ROW13`).

## Salida

`docs/<slug>/resultados/formulario/<timestamp>/`

- `Formulario.xlsx` — copia en `docs/<slug>/resultados/formulario/<timestamp>/` (plantilla desde `global/`); columnas = estudios por hoja; **fila 2 = orden SI global** (`si_order`)
- `formulario-map.json`, `manifest.json`
- **`biblio-traza.jsonl`** (obligatorio tras enrich)

## Pipeline

```text
prepare → classify-nature → biblio-enrich → [web/agente huecos] → lint-setup → stamp
```

| Paso | Comando | Qué hace |
|------|---------|----------|
| 1 | `formulario:prepare` | Mapa v2, ítems col. B (sin columnas estudio) |
| 2 | `formulario:classify-nature` | Naturaleza, `placement` (`study_index` = `si_order` global), fila 2, CSV 3–7, 11 |
| 3 | `formulario:biblio-enrich` | Filas 8–10, 12–13; Crossref + MD; traza |
| 4 | Agente / WebSearch | Solo celdas vacías o dudas; append traza `web` |
| 5 | `formulario:lint-setup` | Estructura + biblio 8–10, 12–13 |
| 6 | `formulario:stamp` | `latest.txt`, manifest |

## Perfil bibliográfico (filas 3–13)

| Fila | Campo Excel | prepare (CSV) | biblio-enrich |
| ---- | ----------- | ------------- | ------------- |
| 3 | DOI | sí | — |
| 4 | Título | sí | — |
| 5 | Autores | sí | — |
| 6 | Año | sí | — |
| 7 | Revista | sí | — |
| 8 | Editorial | no | Crossref `publisher` → artículo → **`—`** |
| 9 | País de origen | no | Afiliaciones Crossref → país en MD → **`—`** |
| 10 | Contexto de aplicación | no | Heurísticas MD + resumen CSV → **`—`** |
| 11 | Tipo de estudio | sí | — |
| 12 | Volumen | no | Crossref `volume` / acta / MD «VOLUME n» → **`—`** |
| 13 | Tamaño muestra | no | Patrones MD + resumen; `MANUAL_ROW13` → **`—`** |

**Orden de confianza:** metadatos **Crossref (web)** para editorial/volumen/país · **texto completo indexado** para muestra y contexto · **no** abstract del CSV como única fuente.

**Graphify:** `cribado2:query` enlaza nodos del corpus; **no** usar su salida por defecto para cifras muestrales — leer `docs/md/<Id>-*.md` (Page chunks, abstract).

Traza `biblio-traza.jsonl` por celda lógica (fila × estudio):

```json
{"study_id":"R016","row":13,"value":"n = 240 respuestas generadas","source":"article","evidence":{"pattern":"…"},"doi":"…"}
```

`source`: `web` | `article` | `dash` (celda `—`).

## Paso final — web (opcional)

Tras `biblio-enrich`, para celdas aún **`—`** o claramente erróneas:

- **WebSearch** con DOI + título (OpenAlex/Crossref/publisher).
- Una línea verificable en español; URL o referencia en `evidence`.
- Editar Excel + línea en `biblio-traza.jsonl`.

No usar web para ítems RQ (filas 17–33).

## Columna B (ítems)

`summary` de `items.json` en filas 17–20, 23–26, 29–33 (mixto → ambas hojas). **Sin** datos C+ en prepare.

## Comandos

```bash
pnpm -s formulario:prepare docs/<slug>
pnpm -s formulario:biblio-enrich docs/<slug>
pnpm -s formulario:biblio-enrich docs/<slug> --force   # tras cambiar MD o script
pnpm -s formulario:lint-setup docs/<slug> <carpeta>
pnpm -s formulario:stamp docs/<slug> <carpeta>
```

## Forbidden

- Rellenar filas ítem 17–33 en prepare.
- `extract-lote` / `apply-lote` desde prepare.
- Stamp sin biblio 8–10, 12–13 completada (dato o `—`).
