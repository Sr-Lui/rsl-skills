# RSL skills — instrucciones para Claude Code

Las skills (`.claude/skills/`) y agentes (`.claude/agents/`) son enlaces a `.cursor/` y `.agents/`; edita siempre el original y ejecuta `pnpm claude:sync` si añades una. `pnpm claude:check` valida enlaces y rutas.

@.cursor/rules/graphify.mdc

## Lectura mínima de MD (ahorro de tokens)

- No leas un MD de `docs/md/` entero (~30k tokens). Usa `pnpm -s cribado2:outline` y `pnpm -s cribado2:query ... --article <corpus_id>`, y lee solo el tramo con `Read offset/limit`.
- Rutas a playbooks y scripts: siempre desde la raíz del repo (`playbooks/...`).
