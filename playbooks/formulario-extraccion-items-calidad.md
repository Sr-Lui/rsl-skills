# Calidad de extracción por ítem (formulario apply)

Complementa [`formulario-apply-rsl.md`](formulario-apply-rsl.md) y [`formulario-prosa-rsl.md`](formulario-prosa-rsl.md). Obligatorio en **rsl-resultado-formulario-apply** (no sustituye debate defensor/critico/orquestador).

## Evidencia mínima por artículo

1. MD cribado-2: `RSL/picoc/…-cribado-2-…/docs/md/<corpus_id>-*.md` (Methods, Evaluation, Results).
2. `pnpm -s cribado2:query docs/<slug> "…"` con cita en `evidence[]` (`src`, `loc`, `quote`).

## Ítems de alta prioridad (sesgo conocido en borradores automáticos)

### RQ2-I3 — Fase principal (cuantitativo)

**Lista cerrada:** Requisitos, Diseño, Desarrollo, Personalización en ejecución, Pruebas, V&V, Auditoría, otro, NR.

- Decidir **dónde la IA interviene en el SDLC**, no inferir «Pruebas» solo porque hay *user study*.
- Si la IA se usa en **implementación** y luego se evalúa → **Desarrollo** o **Pruebas** según el **énfasis del paper** (contribución principal).
- Celda: categoría al inicio (`Pruebas. …`) o intro + categoría; debe poder contarse en frecuencia.

### RQ2-I4 — Otras fases (cuantitativo)

- Mismas etiquetas que RQ2-I3, separadas por **`;`**, minúsculas o capitalización items.md.
- **`—`** si solo una fase; no repetir la principal.

### RQ3-I1 — Métrica + valor (mixto)

- Plantilla: `Constructo: … | Valor: número+unidad | NR`.
- Sin número principal claro → `Valor: NR`, `decision: partial`.

### RQ3-I4 — Cobertura (cuantitativo)

- Cognitiva, Sensorial, Ambas, NR — solo si la **evaluación** lo declara; no marcar Ambas por mencionar accesibilidad genérica.

### RQ2-I1 — Técnica IA (cualitativo)

- Familias (`ML; LLM; …`) + `Modelo: nombre | NR`; no inventar nombres.

### RQ1-I1 — Perfiles (cualitativo)

- Multivalor **`;`** (TEA, TDAH, …); evitar solo «neurodivergencia» si el paper lista condiciones.

## Gate piloto (lote 01)

Tras `formulario:aggregate-preview`, si **RQ2-I3** concentra >80 % en una categoría, revisar manualmente antes de lotes 02–08.
