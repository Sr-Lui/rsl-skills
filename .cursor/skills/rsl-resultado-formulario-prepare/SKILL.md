---
name: rsl-resultado-formulario-prepare
description: >-
  Prepara Excel UTP: columnas SI, mapa, columna B ítems, biblio filas 3–13 (CSV → artículo → web → —).
  Cierra con lint-setup y stamp. Use rsl-resultado-formulario-prepare tras rsl-resultado-items.
---

# rsl-resultado-formulario-prepare

Playbooks: [`formulario-prepare-rsl.md`](../../playbooks/formulario-prepare-rsl.md) · [`formulario-prosa-rsl.md`](../../playbooks/formulario-prosa-rsl.md) (biblio 1 línea)

Invoke: `Usa rsl-resultado-formulario-prepare sobre docs/<slug>/`

## Precondiciones

- `resultado-items:status` PASS · `cribado2:status` OK
- `.venv-formulario` (openpyxl + pyyaml) o `python-openpyxl` / PyYAML sistema

## Procedure

1. `pnpm -s formulario:prepare docs/<slug>`
2. Por columna estudio, completar **filas 8–10, 12–13** (y 8 editorial si falta):
   - CSV → `cribado2:query` / MD → celda **una línea** ES
   - Anotar `biblio-traza.jsonl` (`source`: csv | article)
3. **Paso final:** agente **background** + **WebSearch** solo para celdas aún vacías (DOI+título) → traza `web` o **`—`**
4. `pnpm -s formulario:lint-setup docs/<slug> <carpeta>`
5. `pnpm -s formulario:stamp docs/<slug> <carpeta>`

## Forbidden

- Rellenar filas ítem **17–33** (apply)
- Inferir biblio solo del abstract
- Invocar `extract-lote`

## Cierre

`OK: formulario preparado. Próximo: **rsl-resultado-formulario-apply** lote 01.`
