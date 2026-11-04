---
name: rsl-resultado-formulario-apply
description: >-
  Rellena celdas de ítems RQ del formulario UTP por lotes de 10: debate defensor/critico
  (modo extraccion-formulario), orquestador-extraccion-rsl, extraccion-traza.jsonl,
  formulario:apply-lote. Requiere formulario:stamp tras prepare. Use rsl-resultado-formulario-apply.
---

# rsl-resultado-formulario-apply

Playbook: [`playbooks/formulario-apply-rsl.md`](../../playbooks/formulario-apply-rsl.md)

Invoke: `Usa rsl-resultado-formulario-apply sobre docs/<slug>/` · `lote 03`

## Precondiciones

- `resultados/formulario/latest.txt` y `formulario:lint-setup` PASS
- `items.json` + `## Reglas de registro y agregación` en items.md
- `informe-polish.md` como ancla temática

## Payload apply

Por artículo, tras orquestador, escribir `debate/lote-NN/apply-<corpus_id>.json`:

```json
{
  "article_id": "R016",
  "slots": [
    {
      "item_id": "RQ1-I1",
      "value": "TEA; TDAH",
      "decision": "extracted",
      "evidence": [{"src": "docs/md/...", "loc": "p.4"}]
    }
  ]
}
```

Luego: `pnpm -s formulario:apply-lote docs/<slug> NN [--article corpus_id]`

## Procedure por lote

1. Estudios = `formulario-map.json` → `lotes[NN].corpus_ids`
2. Por artículo: Graphify → R1 defensor → R2 crítico → R3 si aplica → orquestador
3. Guardar debate en `debate/lote-NN/` y `apply-<id>.json`
4. `formulario:apply-lote` tras cada artículo o al cerrar lote
5. Al terminar todos los lotes: `pnpm -s formulario:lint-traza docs/<slug>`

## Cierre

`OK: extracción completa. Próximo: rsl-resultado-formulario-polish (futuro).`

## Forbidden

- Modificar filas biblio 3–13 (volver a **prepare**)
- `apply-lote` sin `apply-<id>.json` cerrado por orquestador
- Celda con texto sin `decision` extracted/partial en traza
