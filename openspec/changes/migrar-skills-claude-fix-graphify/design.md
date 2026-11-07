# Design

## Context

- 25 skills (`.cursor/skills/`), 9 agentes (`.cursor/agents/`) y 1 regla (`.cursor/rules/graphify.mdc`, `alwaysApply`) solo en formato Cursor. `.claude/skills/` contiene únicamente las 6 `openspec-*` recién generadas.
- 10 SKILL.md enlazan `../../playbooks/...` (apuntan a `.cursor/playbooks`, inexistente). Los agentes usan `../../playbooks/...` desde `.cursor/agents/`, que sí resuelve a la raíz.
- `cribado2:query` envuelve `graphify query ... --graph <graph.json>` sin filtro por artículo: BFS depth 2 mezcla vecinos de otros artículos y trunca a ~2000 tokens. Los nodos son estructura (título, `Concept:`, `Findings index`) con `src` y `loc=Lnn`.
- Cada MD (≈1250 líneas) ya trae `Locator index`, `Findings index` y `<a id=...>` por sección/página, por lo que el outline puede derivarse del propio MD sin depender del grafo.
- El grafo del cribado-2 vigente es `RSL/picoc/2026-10-03-3-cribado-2-PIO/graphify-out/graph.json` (7119 nodos, 136 MD).

## Goals / Non-Goals

**Goals:**
- Una sola fuente de verdad, consumible por Cursor y Claude Code.
- Reducir la lectura por artículo a outline + tramos, y el debate a un camino rápido con escalado.

**Non-Goals:**
- Reconstruir grafos ni regenerar MD.
- Cambiar el contrato de celda, el formato de `apply-*.json` ni la traza.
- Reclasificar naturaleza (`nature_needs_review`); sigue siendo decisión del usuario.
- Reescribir las demás skills `rsl-*` más allá de rutas y exposición en Claude.

## Decisions

1. **Symlinks en vez de copias.** `.claude/skills/<n>` y `.claude/agents/<n>.md` son enlaces simbólicos relativos a `.cursor/`, creados por `scripts/claude-sync.mjs` (`pnpm claude:sync [--check]`). Alternativa: copiar (diverge y exige sincronizar) o mover a `.claude` (rompe Cursor). Los `openspec-*` y cualquier entrada real que no sea enlace se respetan.
2. **Rutas desde la raíz del repo.** Se sustituyen `../../playbooks/x.md` por `playbooks/x.md` en skills y agentes. Funciona igual a través del symlink y no depende de dónde resuelva cada herramienta. `claude:sync --check` valida que las rutas citadas existen.
3. **`CLAUDE.md` importa la regla.** Contiene `@.cursor/rules/graphify.mdc` más una nota breve sobre lectura mínima de MD. Alternativa: duplicar el texto; se descarta por divergencia.
4. **Outline derivado del MD, no del grafo.** `cribado2:outline <slug> <corpus_id>` parsea `<a id>` y encabezados `### [PDF p.N]` del MD y calcula `start-end` por línea; omite los bloques `Concept:` y chunks. Es determinista, barato y no depende del truncado de graphify.
5. **`cribado2:query` con filtro y budget.** Se añade `--article <corpus_id>` (el stem completo entra en la pregunta y se descartan nodos con otro `src`) y `--budget N` pasado a graphify. Si no hay hits tras filtrar, se indica y se sugiere el outline. Alternativa: parsear solo en la skill; se descarta porque es regla de producto, no de prompt.
6. **R2 como verificación + escalado.** `formulario_verify_apply_json.py` añade: cobertura de ítems esperados por hoja, solapamiento léxico mínimo `quote`↔ítem/valor y exigencia de cifra en RQ3-I1. Los slots con advertencia se pasan a un crítico (agente `critico-rsl` o revisión inline) y solo una discrepancia convoca a `orquestador-extraccion-rsl`.
7. **Skill apply más corta.** Se mueve el contrato duplicado al playbook y la skill queda con precondiciones, orden por artículo, comandos y prohibiciones. Se añade modo "reanudar": calcula pendientes desde `extraccion-traza.jsonl`.
8. **Sin subagente por defecto.** El camino normal lo ejecuta el agente principal; los subagentes quedan para paralelizar lotes grandes o para los slots marcados.

## Risks / Trade-offs

- [Symlinks en Windows o en clones sin soporte] → `claude:sync` falla con mensaje claro y ofrece `--copy`.
- [Frontmatter de agentes Cursor incompatible con Claude] → verificar `name`/`description` y que no usen campos desconocidos; `--check` lo valida.
- [Outline falla si el formato del MD cambia] → test con 3 MD reales y fallback documentado a `Read` por rangos de `loc`.
- [Filtrar por artículo oculta contexto cruzado útil] → `--article` es opcional; la consulta sin filtro sigue igual.
- [Menor debate baja la calidad] → el verificador endurecido y el escalado cubren los slots dudosos; se muestrean 2 artículos del lote 02 contra el criterio de calidad del playbook.

## Migration Plan

1. Añadir script de sincronización y `CLAUDE.md`; ejecutar sync y `--check`.
2. Corregir rutas en skills/agentes.
3. Implementar outline, filtro/budget y verificación ampliada con pruebas sobre R016.
4. Reescribir la skill apply y el playbook; probar con un artículo pendiente.
5. Rollback: borrar los enlaces de `.claude/` (no tocan `.cursor/`) y revertir el commit.

## Open Questions

- ¿Se versionan los symlinks en git o se generan con `claude:sync` tras clonar (`bootstrap`)? Puede decidirse al implementar sin cambiar el resto.

## Línea base de tokens (medida antes de implementar)

Artículo R016, cribado-2 PIO:
- MD completo: 115 042 bytes, 1255 líneas (~29k tokens si se lee entero).
- `cribado2:query` (sin filtro): 6606-7289 bytes (~1.7k tokens) por consulta, truncada, con nodos de R029 y R568; sin contenido citable.
- Objetivo: outline <100 líneas y lectura de 2-4 tramos de ~40-80 líneas por ítem.

## Resultado de la prueba extremo a extremo (R197 y R199, lote 02)

- Por artículo: 1 `cribado2:outline` (~1.6-3 KB) + 3-5 lecturas/`grep` de rangos de 5-80 líneas, en vez de leer ~115 KB de MD o repetir `query` de ~7 KB.
- `verify-apply-json` detectó una cita no literal (columnas intercaladas del PDF) antes del apply y marcó 5 slots REVISAR; sin subagentes ni `r1`/`orquestador`. Solo R199 necesitó un `r2-critico` de 3 líneas.
- `apply-lote --article` aplicó 8 + 16 slots; la traza pasó de 104 a 128 líneas y `lint-traza` solo falla por E11 (esperado). `formulario:pending` pasó de 63 a 61 estudios.
- No se pudo medir el consumo de tokens real de la sesión; las cifras son tamaños de salida/lectura.

## Hallazgos posteriores (auditoría con linters)

- `lint-prosa` no se corría por lote: 4 FAIL previos en lote 01 (RQ3-I5 y RQ2-I3 sin categoría literal) y 6 WARN en lote 02 (cualitativos >120 caracteres sin `;`) pasaron desapercibidos. La skill ahora exige `lint-prosa` tras cada apply.
- `apply-lote` ignoraba celdas ya aplicadas, sin forma de corregir. Se añadió `--replace` (reescribe celdas y traza del artículo). Resultado: `lint-prosa` PASS (0 WARN), traza intacta en 160 líneas, `lint-traza` solo E11.
- Graphify: el grafo indexa estructura (títulos, hallazgos con `loc`), no texto citable. El ahorro real viene de `cribado2:outline` + lectura por rangos; `cribado2:query --article` queda como localizador auxiliar y para búsquedas entre artículos.

## Resolución de nature_needs_review (2026-11-07)

- Se confirmó la naturaleza de los 34 estudios con `nature-overrides.json` (decisión explícita por estudio). Se cambiaron a **mixto** R123, R173, R345, R549, R581 y R705 por tener señales cuantitativas y cualitativas altas a la vez (p. ej. R705: 98 marcas cuant. y 28 cual.); el resto conserva la heurística.
- `classify-nature --force` desplazó columnas (Cuantitativo 43→47, Cualitativo 49→51). Procedimiento seguro aplicado: copia de seguridad, reubicar biblio filas 8-13 por `corpus_id`, vaciar filas 17-33, vaciar la traza y reaplicar los 16 estudios ya extraídos.
- Comprobación: `lint-setup` PASS, `lint-prosa` PASS (0 WARN), traza de 200 líneas sin celdas perdidas ni valores cambiados (16 nuevas por R123 y R173 pasar a mixto), celda de Excel = traza en las 200.
- Para el futuro: si una reclasificación desplaza columnas con extracción ya aplicada, usar este procedimiento (la skill de prepare no lo automatiza).
