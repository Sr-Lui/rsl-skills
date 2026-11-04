# Formulario UTP — prepare + apply

**Invoke:** `rsl-resultado-formulario-prepare` · `rsl-resultado-formulario-apply`

Plantilla: [`global/Formulario de extracción de información.xlsx`](global/Formulario%20de%20extracción%20de%20información.xlsx)

## Cadena

`rsl-resultado-items` → **prepare** (biblio + mapa) → **apply** (ítems RQ + traza) → polish (futuro)

## Contrato de celda (apply)

| | |
|--|--|
| Idioma | **Español** |
| Forma | 1–3 oraciones; ítem (col. B) + tema RSL |
| Ausente | **`—`** |
| Prohibido | EN crudo, `Sí`/`No` solos, plantillas `\|`, **`formulario:extract-lote`** en producción |

Prosa: [`playbooks/formulario-prosa-rsl.md`](playbooks/formulario-prosa-rsl.md) + **humanize-academic-writing**

## Biblio (prepare filas 3–13)

CSV → artículo → **WebSearch** (final) → **`—`** · traza `biblio-traza.jsonl`

Campos prioritarios: **país**, **contexto**, **volumen**, **tamaño muestra**, editorial.

## Comandos

| Comando | Skill |
|---------|--------|
| `formulario:prepare` · `lint-setup` · `stamp` | prepare |
| `formulario:apply-lote` · `lint-traza` · `lint-prosa` (futuro) | apply |
| `formulario:extract-lote` | **No producción** (qa/dev) |

Python: `.venv-formulario` (`openpyxl`, `pyyaml`).

## Playbooks

[`formulario-prepare-rsl.md`](playbooks/formulario-prepare-rsl.md) · [`formulario-apply-rsl.md`](playbooks/formulario-apply-rsl.md)
