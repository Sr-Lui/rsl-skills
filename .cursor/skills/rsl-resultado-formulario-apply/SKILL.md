---
name: rsl-resultado-formulario-apply
description: >-
  Rellena celdas de ítems RQ del formulario UTP por lotes de 10: debate defensor/critico
  (modo extraccion-formulario), orquestador, humanize-academic-writing, extraccion-traza.jsonl,
  formulario:apply-lote. Prosa en español, precisa, no plantillas. Requiere formulario:stamp.
  Use rsl-resultado-formulario-apply. No usar formulario:extract-lote en producción.
---

# rsl-resultado-formulario-apply

Playbooks: [`formulario-apply-rsl.md`](../../playbooks/formulario-apply-rsl.md) · [`formulario-prosa-rsl.md`](../../playbooks/formulario-prosa-rsl.md)

Invoke: `Usa rsl-resultado-formulario-apply sobre docs/<slug>/` · `lote 03`

## Precondiciones

- `resultados/formulario/latest.txt` · `formulario:lint-setup` PASS
- `items.json` + `## Reglas de registro y agregación` · `informe-polish.md`
- Biblio filas 3–13 completada en **prepare** (no rellenar aquí)

## Contrato de celda

- **Español**, 1–3 oraciones (~25–70 palabras): qué dice el artículo sobre **este ítem** (columna B) + enlace breve al **tema RSL**.
- **No** copiar-pegar inglés del PDF; **no** `hint` literales (`Campo: X | Valor: Y`); **no** `Sí`/`No` solos — **explicar** negativas.
- **Ausente:** Excel **`—`**, `decision: absent`.

## Procedure por artículo (dentro del lote)

1. `cribado2:query` + MD/PDF indexado.
2. **R1 defensor-rsl** (`extraccion-formulario`) → `debate/lote-NN/r1-defensor-<corpus_id>.md`
3. **R2 critico-rsl** → `r2-critico-<corpus_id>.md` (checklist en formulario-prosa-rsl)
4. **R3** + **orquestador-extraccion-rsl** si aplica
5. Skill **humanize-academic-writing** sobre cada `value` final
6. `debate/lote-NN/apply-<corpus_id>.json` → `pnpm -s formulario:apply-lote docs/<slug> NN [--article id]`

Tras todos los lotes: `formulario:lint-traza` · `formulario:lint-prosa` (cuando exista).

## Forbidden

- **`pnpm -s formulario:extract-lote`** (bypass; solo qa/dev con acuerdo explícito)
- `apply-lote` sin debate R1+R2+orquestador cerrado
- Celdas ítem en inglés crudo o telegrafía
- Tocar filas biblio 3–13

## Cierre

`OK: extracción apply completa (prosa ES). Próximo: rsl-resultado-formulario-polish (futuro).`
