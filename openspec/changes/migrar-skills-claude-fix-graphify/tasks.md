# Tasks

Supuesto: los symlinks de `.claude/` se versionan en git; `claude:sync` los regenera si faltan. El commit previo del trabajo sin commitear lo decide el usuario antes de empezar.

## 1. Portabilidad Cursor / Claude

- [x] 1.1 Crear `scripts/claude-sync.mjs` y scripts `claude:sync` / `claude:sync --check` en `package.json`. Verificar: ejecutarlo dos veces seguidas no cambia nada y `--check` sale 0.
- [x] 1.2 Enlazar las 25 skills de `.cursor/skills/` y `humanize-academic-writing` (de `.agents/skills/`) en `.claude/skills/` sin tocar `openspec-*`. Verificar: `humanize-academic-writing` aparece invocable y `ls -l .claude/skills` muestra symlinks relativos y `rsl-resultado-formulario-apply` aparece como skill en Claude Code.
- [x] 1.3 Enlazar los 9 agentes en `.claude/agents/` y validar frontmatter (`name`, `description`). Verificar: `claude:sync --check` sin errores y el agente `critico-rsl` listado.
- [x] 1.4 Crear `CLAUDE.md` con `@.cursor/rules/graphify.mdc` y nota de lectura mínima de MD. Verificar: nueva sesión de Claude Code conoce `pnpm graphify:<scope>:query`.
- [x] 1.5 Reemplazar `../../playbooks/...` por `playbooks/...` en los 10 SKILL.md afectados (y revisar agentes). Verificar: `claude:sync --check` confirma que toda ruta citada a `playbooks/`, `scripts/` y `global/` existe.

- [x] 1.6 Medir la línea base de tokens del flujo actual para un artículo (bytes de la salida de `cribado2:query` y del MD completo de R016) y registrarla en `design.md`. Verificar: cifras anotadas antes de tocar `cribado2.py`.
- [x] 1.7 Añadir permisos en `.claude/settings.json` para `pnpm -s formulario:*`, `pnpm -s cribado2:query`, `pnpm -s cribado2:outline` y `pnpm -s sintesis:*` (skill `fewer-permission-prompts`). Verificar: ejecutar un `cribado2:query` desde Claude Code sin prompt.

## 2. Consulta de grafo y outline

- [x] 2.1 Añadir `--article` y `--budget` a `cribado2:query` en `scripts/cribado2.py`, con filtro por `src` y aviso de truncado. Verificar: consulta de R016 no devuelve nodos R029/R568; artículo inexistente da error con siguiente paso.
- [x] 2.2 Implementar `cribado2:outline <docs/slug> <corpus_id>` (secciones, hallazgos, página, líneas inicio-fin). Verificar: sobre R016 la salida es <100 líneas y cada rango coincide con `<a id>` del MD.
- [x] 2.3 Probar outline y query en 3 MD de formatos distintos (R016, R029, R568) y comprobar que `git status` no cambia. Verificar: salida registrada en este change o en el PR.
- [x] 2.5 Revisar `rsl-resultado-sintesis` por usos de `cribado2:query`. Verificar: `grep` no encuentra ninguna referencia (no requiere cambios).
- [x] 2.4 Actualizar `.cursor/rules/graphify.mdc` y `rsl-cribado-2-memoria` con los nuevos flags. Verificar: ejemplos copiables funcionan.

## 3. Verificación y skill apply

- [x] 3.1 Ampliar `scripts/formulario_verify_apply_json.py`: cobertura de ítems por hoja, solapamiento `quote`↔ítem, cifra en RQ3-I1, salida con severidad. Verificar: sobre `lote-01` pasa sin errores y marca la cita de R016 `RQ1-I2` como advertencia.
- [x] 3.2 Mover el contrato duplicado de la skill a `playbooks/formulario-apply-rsl.md` y reescribir `.cursor/skills/rsl-resultado-formulario-apply/SKILL.md` (pasada por artículo, escalado selectivo, modo reanudar, rutas desde raíz). Verificar: SKILL.md <60 líneas y sin enlaces rotos.
- [x] 3.3 Añadir cálculo de pendientes desde `extraccion-traza.jsonl` (comando o sección de skill). Verificar: con 104/736 líneas lista exactamente los `corpus_id` sin aplicar.
- [x] 3.4 Actualizar `.cursor/agents/defensor-rsl.md`, `critico-rsl.md` y `orquestador-extraccion-rsl.md` al flujo compacto (crítico por slots marcados, orquestador por discrepancia). Verificar: coherentes con la skill.
- [x] 3.5 Prueba extremo a extremo: procesar 2 artículos pendientes con la skill desde Claude Code, `verify-apply-json` y `apply-lote`. Verificar: `lint-traza` solo falla por E11, `Formulario.xlsx` conserva los 10 estudios previos y se registra el consumo de tokens frente al flujo anterior.

## 4. Cierre

- [x] 4.1 Actualizar `README.md` y `SKILL.MD` con la instrucción `pnpm claude:sync` y el flujo nuevo. Verificar: referencias a rutas existentes.
- [x] 4.2 Ejecutar `openspec validate migrar-skills-claude-fix-graphify --strict`. Verificar: sin errores.

## 5. Auditoría posterior

- [x] 5.1 Añadir `--replace` a `formulario:apply-lote` y exigir `lint-prosa` tras cada apply en la skill y el playbook. Verificar: corregir 10 celdas con `--replace` deja `lint-prosa` en PASS (0 WARN) y la traza en 160 líneas.
