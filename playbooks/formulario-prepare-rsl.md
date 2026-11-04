# Prepare formulario UTP (rsl-resultado-formulario-prepare)

Prosa biblio breve: [`formulario-prosa-rsl.md`](formulario-prosa-rsl.md) (solo filas 3–13, una línea).

## Salida

`docs/<slug>/resultados/formulario/<timestamp>/`

- `Formulario.xlsx` — N columnas = N SI
- `formulario-map.json`, `manifest.json`
- `biblio-traza.jsonl` (recomendado)

## Perfil bibliográfico (filas 3–13)

| Fila | Campo Excel | Origen 1 | Origen 2 | Origen 3 |
| ---- | ----------- | -------- | -------- | -------- |
| 3 | DOI | CSV | — | — |
| 4 | Título | CSV | — | — |
| 5 | Autores | CSV | — | — |
| 6 | Año | CSV | — | — |
| 7 | Revista | CSV | — | — |
| 8 | Editorial | CSV | artículo | web |
| 9 | **País de origen** | CSV | artículo | web |
| 10 | **Contexto de aplicación** | CSV | artículo | web |
| 11 | Tipo de estudio | CSV | — | — |
| 12 | **Volumen** | CSV | artículo | web |
| 13 | **Tamaño de muestra** | CSV | artículo | web |

**Orden por celda:** CSV → texto completo (`cribado2:query`, MD con `loc`) → si vacío, **paso final** (web) → si no hay fuente fiable → **`—`**.

**No inferir** del abstract solo. **No inventar.**

Traza `biblio-traza.jsonl`: `study_id`, `row`, `source`: `csv` | `article` | `web` | `dash`, `evidence`.

## Paso final — web (background)

Tras completar artículo para **todas** las columnas:

- Agente con **WebSearch** (DOI + título) **solo** para celdas aún vacías en filas 8–10, 12–13 (y 8 editorial si aplica).
- Rellenar **una línea** en español con dato verificable; citar URL en traza.
- Si no hay consenso → **`—`**.

No usar web para ítems RQ (filas 17–33).

## Columna B (ítems)

`summary` de `items.json` en filas 17–20, 23–26, 29–33 (mixto → ambas hojas). **Sin** datos C+ en prepare.

## Comandos

```bash
pnpm -s formulario:prepare docs/<slug>
# completar biblio manual/agente + biblio-traza
pnpm -s formulario:lint-setup docs/<slug> <carpeta>
pnpm -s formulario:stamp docs/<slug> <carpeta>
```

## Forbidden

- Rellenar filas ítem 17–33 en prepare.
- `extract-lote` / apply desde prepare.
