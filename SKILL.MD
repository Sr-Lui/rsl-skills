# Formulario UTP — prepare + apply

**Invoke:** `rsl-resultado-formulario-prepare` · `rsl-resultado-formulario-apply`

Plantilla: [`global/Formulario de extracción de información.xlsx`](global/Formulario%20de%20extracción%20de%20información.xlsx)

## Cadena

`rsl-resultado-items` → **prepare** (biblio + mapa) → **apply** (ítems RQ + traza) → **`rsl-resultado-sintesis`** (Resultados por ítem; [`playbooks/sintesis-resultados-rsl.md`](playbooks/sintesis-resultados-rsl.md)) → gráficas en Python (futuro)

## Contrato de celda (apply)

| | |
|--|--|
| Idioma | **Español** |
| Forma | 1–3 oraciones; ítem (col. B) + tema RSL |
| Ausente | **`—`** |
| Prohibido | EN crudo, **solo** `Sí`/`No` sin registro ni nota, prosa cuantitativa sin categoría/número, **`formulario:extract-lote`** en producción |

Apply (flujo por artículo, R2 automatizado): [`playbooks/formulario-apply-rsl.md`](playbooks/formulario-apply-rsl.md) · pendientes: `pnpm -s formulario:pending docs/<slug>`

Prosa: [`playbooks/formulario-prosa-rsl.md`](playbooks/formulario-prosa-rsl.md) + **humanize-academic-writing**

## Biblio (prepare filas 3–13)

`prepare` → **`formulario:classify-nature`** (columnas por hoja; CSV 3–7, 11) → **`formulario:biblio-enrich`** (8–10, 12–13 solo en `placement`) → WebSearch huecos → **`—`** · trazas **`nature-traza.jsonl`** + **`biblio-traza.jsonl`**

Campos enrich: **editorial**, **país**, **contexto**, **volumen**, **tamaño muestra**.

## Comandos

| Comando | Skill |
|---------|--------|
| `formulario:prepare` · **`classify-nature`** · **`biblio-enrich`** · `lint-setup` · `stamp` | prepare |
| `formulario:apply-lote` · `lint-traza` · **`lint-prosa`** · **`aggregate-preview`** | apply |
| `formulario:extract-lote` | **No producción** (qa/dev) |
| `sintesis:prepare` · `general` · `codify-auto` · `aggregate` · `borrador` · `debate-index` · `lint` · `stamp` | rsl-resultado-sintesis |

Python: `.venv-formulario` (`openpyxl`, `pyyaml`).

## Playbooks

[`formulario-prepare-rsl.md`](playbooks/formulario-prepare-rsl.md) · [`formulario-apply-rsl.md`](playbooks/formulario-apply-rsl.md)
