---
name: rsl-resultado-formulario-prepare
description: >-
  Prepara el Excel UTP de extracción: copia plantilla, extiende columnas por cada SI del CSV,
  formulario-map.json, columna B con summary de ítems, perfil bibliográfico filas 3–13
  (CSV → artículo → blanco). Cierra con formulario:lint-setup y formulario:stamp.
  Use rsl-resultado-formulario-prepare tras rsl-resultado-items.
---

# rsl-resultado-formulario-prepare

Playbook: [`playbooks/formulario-prepare-rsl.md`](../../playbooks/formulario-prepare-rsl.md) · Spec: [`SKILL.MD`](../../../SKILL.MD)

Invoke: `Usa rsl-resultado-formulario-prepare sobre docs/<slug>/`

## Precondiciones

- `pnpm -s resultado-items:status docs/<slug>` → PASS
- `pnpm -s cribado2:status docs/<slug>` → OK
- `.venv-formulario` con openpyxl (`python3 -m venv .venv-formulario && .venv-formulario/bin/pip install openpyxl`) o `python-openpyxl` del sistema

## Procedure

1. `pnpm -s formulario:prepare docs/<slug>`
2. Campos biblio vacíos tras CSV: por columna estudio, `pnpm -s cribado2:query docs/<slug> "…"`; solo escribir si el texto completo lo dice; si no → **blanco**
3. Opcional: `biblio-traza.jsonl` con `source`: csv | article | blank
4. `pnpm -s formulario:lint-setup docs/<slug> <YYYY-MM-DD-HHMM>` (carpeta del prepare)
5. `pnpm -s formulario:status docs/<slug>`
6. `pnpm -s formulario:stamp docs/<slug> <YYYY-MM-DD-HHMM>`

## Cierre

`OK: formulario preparado. Próximo: **rsl-resultado-formulario-apply** (lote 01).`

## Forbidden

- Rellenar filas ítem 17–33 (datos C+) — eso es **apply**
- Inferir biblio del abstract o de otro estudio
- Editar picoc, CSV, items.json, plantilla global
