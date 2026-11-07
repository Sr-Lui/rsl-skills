---
name: rsl-resultado-formulario-apply
description: >-
  Rellena los ítems RQ del formulario UTP estudio a estudio (micro-lotes ~5): outline del MD, lectura
  solo de los tramos citados, apply-<id>.json con evidencia literal, verify-apply-json (R2 automatizado),
  crítico solo en slots marcados, humanize-academic-writing, apply-lote y traza. Prosa ES. Requiere
  formulario:stamp de prepare. Use rsl-resultado-formulario-apply o "lote NN".
---

# rsl-resultado-formulario-apply

Contrato de celda, política celda↔traza y payload: `playbooks/formulario-apply-rsl.md` (fuente única; no repetirlo aquí). Prosa: `playbooks/formulario-prosa-rsl.md` + `.agents/skills/humanize-academic-writing/SKILL.md`. Calidad por ítem: `playbooks/formulario-extraccion-items-calidad.md`.

Invoke: `Usa rsl-resultado-formulario-apply sobre docs/<slug>/` · `lote 03`

## Precondiciones

`pnpm -s formulario:lint-setup docs/<slug>` PASS · Excel en `docs/<slug>/resultados/formulario/<carpeta>/` · `placement` por hoja en `formulario-map.json`.
**Qué falta:** `pnpm -s formulario:pending docs/<slug>` (lista estudios e ítems pendientes y el siguiente lote). Nunca reescribas lo ya aplicado.

## Por artículo (una pasada; leer lo mínimo)

1. `pnpm -s cribado2:outline docs/<slug> <corpus_id>` → hallazgos, páginas y encabezados con rangos `Lx-Ly` (el MD entero pesa ~30k tokens; **no lo leas entero**).
2. `Read` con `offset/limit` solo de los tramos que respondan a los ítems (resultados, método, participantes, tablas). Si falta un dato, un `pnpm -s cribado2:query docs/<slug> "<pregunta mínima>" --article <corpus_id>` ayuda a localizar (el grafo indexa estructura, no texto citable). PDF solo si el MD no alcanza.
3. Redacta `debate/lote-NN/apply-<corpus_id>.json`: por ítem, registro agregable + frase ES específica, `decision`, `evidence[]` con `src`, `loc` (`p. N`, anclado) y `quote` literal ≥40 car. (idealmente ≥60) que **contenga la cifra** del value. Aplica humanize a la frase, no al dato. Ausente = `—` + `absent`.
4. No uses la misma cita para tres o más ítems ni pegues el mismo párrafo en dos `item_id`.

Varios artículos del lote pueden ir en paralelo (un subagente por artículo, con esta misma receta) si hay muchos.

## R2 automatizado y escalado

1. `pnpm -s formulario:verify-apply-json docs/<slug> <carpeta> docs/<slug>/resultados/formulario/<carpeta>/debate/lote-NN` — errores ⇒ corregir y repetir (bloquea el apply). Las líneas **REVISAR** (cita débil, cifras ausentes, cita repetida, ítems sin cubrir) listan los únicos slots que pasan al crítico.
2. **Crítico** (`critico-rsl`, modo extraccion-formulario) **solo sobre los slots REVISAR** → `r2-critico-<corpus_id>.md` (una línea por slot). Artículo sin REVISAR ⇒ no hay r2.
3. **Orquestador** (`orquestador-extraccion-rsl`) solo si defensor/autor y crítico discrepan en hechos u omisión. Incidencias → `extraccion-orquestador.md`.
4. `pnpm -s formulario:apply-lote docs/<slug> NN [--article id]` (re-sincroniza la fila 2; escribe solo donde hay `placement`; **ignora celdas ya aplicadas**).
5. **Tras cada apply**: `pnpm -s formulario:lint-prosa docs/<slug>` (salida corta). Corrige en el `apply-<id>.json` y reaplica con `apply-lote docs/<slug> NN --article id --replace` (reescribe celdas y traza de ese artículo). Reglas que suelen fallar: ítems categóricos deben **contener la categoría literal** (RQ3-I5: «Integración continua», «Semiautomática», «Solo validación con usuarios» o «NR»; RQ2-I3: Requisitos, Diseño, Desarrollo, Personalización en ejecución, Pruebas, V&V, Auditoría, Otro, NR); cualitativos RQ1-I1, RQ2-I1, RQ2-I2, RQ3-I3 de **más de 120 caracteres** necesitan etiquetas con `;`, o acórtalos.

## Cierre del run

Con la traza completa: `pnpm -s formulario:lint-traza docs/<slug>` · `pnpm -s formulario:lint-prosa docs/<slug>`. **E11** = traza incompleta (normal a mitad); **E12** = falta `formulario:stamp`.
`pnpm -s formulario:stamp docs/<slug> <carpeta>` exige `lint-setup` PASS y lint-traza/lint-prosa `--strict`. Si `manifest.nature_needs_review` no está vacío, díselo al usuario (reclasifica él con `formulario:classify-nature --force` en prepare); **no** uses `--allow-nature-review` sin su confirmación.

## Forbidden

- `formulario:draft-lote` y `formulario:extract-lote` en producción.
- `apply-lote` con errores de `verify-apply-json`.
- Leer el MD completo por rutina; volcar salidas largas de `cribado2:query`.
- Celdas en inglés crudo, telegrafía o solo `Sí`/`No`; tocar biblio filas 3–13; editar la fila 2 a mano.
- Reclasificar naturaleza desde apply.

## Cierre

`OK: extracción apply completa (prosa ES), stamp y extraccion_complete. Próximo: **rsl-resultado-sintesis**.`
