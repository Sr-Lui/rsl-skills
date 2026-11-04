# Apply formulario — ítems RQ (rsl-resultado-formulario-apply)

Fuente: [`playbooks/extraccion-items-rsl.md`](extraccion-items-rsl.md) (NR, multivalor `;`, reglas de agregación).

## Política celda ↔ traza

| Situación | Excel | `decision` |
| --------- | ----- | ---------- |
| Tema ítem ausente | Vacío | `absent` |
| Contenido relevante | Valor breve (`hint`) | `extracted` |
| Tangencial | Vacío o valor (debate) | `omitted` / `marginal` |
| Mixto, subcampo ausente | `NR` en subcampo | `partial` |

Prohibido: inventar; inferir solo del resumen.

## Debate (por artículo, dentro del lote)

1. **defensor-rsl** (`extraccion-formulario`) — propuesta + evidencia Graphify
2. **critico-rsl** — conforme / disconforme por ítem
3. **R3** si disconformes
4. **orquestador-extraccion-rsl** — veredicto; incidencias en `extraccion-orquestador.md`

## Persistencia

`debate/lote-NN/apply-<corpus_id>.json` → `pnpm -s formulario:apply-lote docs/<slug> NN`

Traza: `extraccion-traza.jsonl` (append).

## Cierre

`pnpm -s formulario:lint-traza docs/<slug>`
