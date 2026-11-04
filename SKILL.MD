# Formulario UTP — especificación (rsl-resultado-formulario-prepare / -apply)

**Estado corpus (ia-inclusion-cognitiva-software):** CSV **146** · **73 SI** · items PASS · **73/73 PDF** · cribado2 OK.

Invoke:

- `Usa rsl-resultado-formulario-prepare sobre docs/<slug>/`
- `Usa rsl-resultado-formulario-apply sobre docs/<slug>/`

Plantilla: [`global/Formulario de extracción de información.xlsx`](global/Formulario%20de%20extracción%20de%20información.xlsx)

---

## Cadena

| Paso | Skill |
| ---- | ----- |
| Ítems RQ | `rsl-resultado-items` |
| Excel + mapa + biblio | **`rsl-resultado-formulario-prepare`** |
| Celdas ítem + traza | **`rsl-resultado-formulario-apply`** |
| Revisión | `rsl-resultado-formulario-polish` (futuro) |

Playbooks: [`playbooks/formulario-prepare-rsl.md`](playbooks/formulario-prepare-rsl.md) · [`playbooks/formulario-apply-rsl.md`](playbooks/formulario-apply-rsl.md)

---

## Comandos

| Comando | Skill |
| ------- | ----- |
| `formulario:prepare` | prepare |
| `formulario:lint-setup` | prepare |
| `formulario:stamp` | prepare |
| `formulario:status` | ambos (`--progress` en apply) |
| `formulario:apply-lote` | apply |
| `formulario:lint-traza` | apply |

Python: `.venv-formulario/bin/python` (openpyxl) o `python-openpyxl` del sistema.

---

## Excel

- Copia por run; si **N SI > 40**, extender columnas clonando formato de la columna 40 (plantilla global intacta).
- Columna **B**: `summary` de `items.json`; filas ítem 17–20, 23–26, 29–33.
- **Biblio 3–13:** CSV → texto completo (Graphify/MD) → **blanco** (no inferir).

---

## `formulario-map.json`

Estudios (columna, csv_id, corpus_id, DOI, pdf), ítems (sheet, row), **lotes de 10**.

Apply escribe `debate/lote-NN/apply-<corpus_id>.json` → `formulario:apply-lote`.

---

## Traza (`extraccion-traza.jsonl`)

Campos: `article_id`, `item_id`, `sheet`, `cell`, `value`, `decision`, `evidence[]`, `lote`.

Política ítem: vacío = `absent`; valor = `extracted`/`partial`; ver playbook apply.

---

## Precondiciones

- `resultado-items:status` PASS · `cribado2:status` OK · `rsl:pipeline-sync`

---

## QA

- README: comandos `formulario:*`
- `qa-destroy`: skills prepare/apply + `formulario_latest` tras stamp
