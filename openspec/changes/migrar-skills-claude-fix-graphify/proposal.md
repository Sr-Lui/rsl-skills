# Proposal

## Why

Las skills y agentes RSL viven solo en `.cursor/`, así que Claude Code no los carga (`.claude/skills` y `.claude/agents` no los incluyen) y los enlaces `../../playbooks/...` de las skills apuntan a `.cursor/playbooks`, que no existe. Además, `rsl-resultado-formulario-apply` es inejecutable de forma económica: `cribado2:query` devuelve nodos de estructura con ruido de otros artículos y truncados a ~2000 tokens, cada MD pesa ~115 KB (~30k tokens), y el flujo exige 3 agentes (defensor, crítico, orquestador) por artículo (73 SI). La extracción va en 10/73 estudios y el lote 01 se desvió de la skill (sin `r2-critico`, orquestador siempre).

## What Changes

- Exponer las 25 skills de `.cursor/skills/` y los 9 agentes de `.cursor/agents/` también en Claude Code mediante `.claude/skills/` y `.claude/agents/` (una sola fuente de verdad, sin duplicar contenido), con un comando de sincronización y comprobación.
- Añadir `CLAUDE.md` que importe las reglas de `.cursor/rules/graphify.mdc` para que el uso de Graphify aplique igual en Claude.
- Sustituir los enlaces relativos rotos en skills/agentes por rutas desde la raíz del repo.
- Nuevo helper `cribado2:outline` por artículo: índice de secciones/hallazgos del MD con rangos de línea, para leer solo el tramo con `Read offset/limit`.
- Endurecer `cribado2:query`: filtro por `corpus_id`/stem, `--budget` configurable, sin nodos de otros artículos y con aviso claro si se trunca.
- Reescribir `rsl-resultado-formulario-apply` para ejecución en Claude: una pasada por artículo (outline → query acotada → lectura por rango → `apply-*.json`), R2 como checklist automatizado (`verify-apply-json` ampliado) y crítico/orquestador solo para casos marcados. Reducir duplicación con `playbooks/formulario-apply-rsl.md`.
- **BREAKING**: el debate por artículo deja de generar siempre `r1-defensor` + `r2-critico` + `orquestador`; los lotes futuros usan el flujo compacto (los artefactos del lote 01 existente siguen siendo válidos).

## Capabilities

### New Capabilities
- `agent-skills-portability`: skills, agentes y reglas del repo disponibles en Cursor y Claude Code desde una única fuente, con sincronización verificable y rutas sin enlaces rotos.
- `cribado2-graph-lookup`: consulta acotada al grafo del cribado-2 y outline por artículo con rangos de línea para lectura mínima del MD.
- `formulario-apply-workflow`: flujo de relleno de ítems RQ por artículo, con verificación automatizada y escalado selectivo a crítico/orquestador.

### Modified Capabilities

(ninguna: `openspec/specs/` aún está vacío)

## Impact

- `.cursor/skills/*/SKILL.md`, `.cursor/agents/*.md` (rutas), nuevos `.claude/skills/*`, `.claude/agents/*`, `CLAUDE.md`.
- `scripts/cribado2.py` (query, outline), `scripts/formulario_verify_apply_json.py`, `package.json` (scripts `cribado2:outline`, `claude:sync`).
- `playbooks/formulario-apply-rsl.md`, `SKILL.MD`/`README.md` (referencias).
- Sin cambios en `Formulario.xlsx`, en la traza existente ni en los grafos ya construidos.
