# Orquestador — extracción formulario (2026-11-04)

Run automático **md-extract-v1**: lectura de MD del corpus cribado-2, reglas cite-or-blank (sin debate R1–R3 por celda).

- **73** estudios · **8** lotes · **1168** líneas en `extraccion-traza.jsonl` (ítems mixtos en Cuantitativo + Cualitativo)
- Payloads: `debate/lote-NN/apply-<corpus_id>.json`

Revisión humana recomendada en muestra aleatoria antes de síntesis RSL; re-run por lote con debate defensor/critico/orquestador si hay disconformidades.
