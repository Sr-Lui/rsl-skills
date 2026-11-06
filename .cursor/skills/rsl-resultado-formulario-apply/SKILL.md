---
name: rsl-resultado-formulario-apply
description: >-
  Rellena celdas de ítems RQ del formulario UTP por lotes de 10: debate defensor/critico
  (modo extraccion-formulario), orquestador, humanize-academic-writing, extraccion-traza.jsonl,
  formulario:apply-lote. Prosa en español, precisa, no plantillas. Requiere formulario:stamp.
  Use rsl-resultado-formulario-apply. No usar formulario:extract-lote en producción.
---

# rsl-resultado-formulario-apply

Playbooks: [`formulario-apply-rsl.md`](../../playbooks/formulario-apply-rsl.md) · [`formulario-prosa-rsl.md`](../../playbooks/formulario-prosa-rsl.md) · [`formulario-extraccion-items-calidad.md`](../../playbooks/formulario-extraccion-items-calidad.md)

Invoke: `Usa rsl-resultado-formulario-apply sobre docs/<slug>/` · `lote 03`

## Precondiciones

- `resultados/formulario/latest.txt` · `formulario:lint-setup` PASS
- Excel destino: **`docs/<slug>/resultados/formulario/<carpeta>/Formulario.xlsx`** (no `global/`)
- `items.json` + `## Reglas de registro y agregación` · `informe-polish.md`
- `formulario-map.json` con **`placement`** por hoja (`classify-nature` OK)
- Un `apply-<corpus_id>.json` por artículo; **`apply-lote` escribe solo** donde `placement[sheet]` existe.

## Orden de columnas (fila 2)

- **`study_index` en el mapa = `si_order` global** (orden SI del cribado-2, 1…N).
- **Mixto:** mismo número de cabecera en Cuantitativo y Cualitativo (p. ej. estudio 3 → cabecera **3** en ambas hojas).
- **Columna física:** compacta por hoja (`placement.column`); la cabecera fila 2 muestra el **número global**, no 1…k local.
- `formulario:apply-lote` escribe ítems con `column_index` / `placement.column`; al guardar, el script **re-sincroniza fila 2** (`sync_numbered_headers`).

Ejemplo (5 estudios): Cuant. cabeceras 1, 3, 4, 5 · Cual. cabeceras 2, 3, 5.

## Contrato de celda

- **Registro agregable** visible en la celda (literal o entre paréntesis) + **frase breve** en español; humanize pulir la frase, no borrar el dato.
- **Unicidad por ítem:** no pegar el mismo párrafo en **dos `item_id` distintos** del mismo estudio (el mixto duplica el mismo ítem en dos hojas: eso sí es correcto). Si una excepción documentada lo exige, añade una fila en `manifest.json` → `duplicate_value_whitelist`.
- **Evidencia:** cada slot con contenido lleva `evidence[]` con `src`, `loc` y `quote` (**≥ 40 caracteres**); si `RQ3-I1` tiene **Valor** numérico, al menos una `quote` debe **incluir la cifra**.
- **Ausente:** Excel **`—`**, `decision: absent`.
- Tras todos los lotes: `formulario:lint-prosa` + `formulario:lint-traza`.

## Procedure por artículo (dentro del lote)

1. `cribado2:query` + MD/PDF indexado.
2. **R1 defensor-rsl** (`extraccion-formulario`) → `debate/lote-NN/r1-defensor-<corpus_id>.md`
3. **R2 critico-rsl** → `r2-critico-<corpus_id>.md` (checklist en formulario-prosa-rsl)
4. **R3** + **orquestador-extraccion-rsl** si aplica
5. Skill **humanize-academic-writing** sobre cada `value` final
6. `debate/lote-NN/apply-<corpus_id>.json` → `pnpm -s formulario:apply-lote docs/<slug> NN [--article id]`

Tras todos los lotes: `formulario:lint-traza` · `formulario:lint-prosa` (cuando exista).

**Cierre:** `pnpm -s formulario:stamp docs/<slug> <carpeta>` — exige `lint-setup`, `lint-traza` y `lint-prosa` PASS y deja `extraccion_complete: true` en `manifest.json` + `resultados/formulario/latest.txt`.

## Forbidden

- **`pnpm -s formulario:draft-lote`** y **`formulario:extract-lote`** en producción (solo qa/dev explícito)
- `apply-lote` sin debate R1+R2+orquestador cerrado
- Celdas ítem en inglés crudo o telegrafía
- Duplicar columna de estudio en hoja sin `placement`; **reclasificar naturaleza** → usuario ejecuta **`formulario:classify-nature --force`** en prepare (no en apply)
- Tocar filas biblio 3–13 en apply
- Editar cabeceras fila 2 a mano en Excel (dejar que classify / biblio / apply las sincronicen)

## Regenerar placement (usuario / prepare)

Si cambia naturaleza o orden SI, en el **tema** (`docs/<slug>/`):

```bash
pnpm -s formulario:classify-nature docs/<slug> <carpeta> --force
pnpm -s formulario:biblio-enrich docs/<slug> <carpeta> --force
```

Luego re-aplicar lotes si el Excel ya tenía ítems.

## Cierre

`OK: extracción apply completa (prosa ES), stamp y extraccion_complete. Próximo: **rsl-resultado-sintesis** (síntesis de resultados por ítem).`
