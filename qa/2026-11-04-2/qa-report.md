# Reporte qa:destroy — 2026-11-04-2

Casos: 90 · fallidos: 4 · grupos: destruir, marco, orden, positivo, skills

## Fallos

| Caso | Grupo | Qué se probó | Comando | Esperado | Obtenido | Problema | Sospechoso |
|---|---|---|---|---|---|---|---|
| S03 | skills | agentes *-rsl y skills rsl-* citados existen; nombre del frontmatter = carpeta | `(verificación)` | OK | .cursor/skills/rsl-resultado-formulario-apply/SKILL.md: la skill rsl-resultado-formulario-polish no existe en .cursor/skills/ | .cursor/skills/rsl-resultado-formulario-apply/SKILL.md: la skill rsl-resultado-formulario-polish no existe en .cursor/skills/ | .cursor/skills · .cursor/agents · README |
| S03 | skills | agentes *-rsl y skills rsl-* citados existen; nombre del frontmatter = carpeta | `(verificación)` | OK | .cursor/skills/rsl-resultado-formulario-prepare/SKILL.md: la skill rsl-resultado-formulario no existe en .cursor/skills/ | .cursor/skills/rsl-resultado-formulario-prepare/SKILL.md: la skill rsl-resultado-formulario no existe en .cursor/skills/ | .cursor/skills · .cursor/agents · README |
| S03 | skills | agentes *-rsl y skills rsl-* citados existen; nombre del frontmatter = carpeta | `(verificación)` | OK | .cursor/skills/rsl-resultado-items/SKILL.md: la skill rsl-desglose-items no existe en .cursor/skills/ | .cursor/skills/rsl-resultado-items/SKILL.md: la skill rsl-desglose-items no existe en .cursor/skills/ | .cursor/skills · .cursor/agents · README |
| S03 | skills | agentes *-rsl y skills rsl-* citados existen; nombre del frontmatter = carpeta | `(verificación)` | OK | .cursor/skills/rsl-resultado-items/SKILL.md: la skill rsl-resultado-formulario no existe en .cursor/skills/ | .cursor/skills/rsl-resultado-items/SKILL.md: la skill rsl-resultado-formulario no existe en .cursor/skills/ | .cursor/skills · .cursor/agents · README |
| S04 | skills | cada skill rsl-* tiene la sección Cierre con el contrato OK/ERROR | `(verificación)` | OK | .cursor/skills/rsl-picoc/SKILL.md: falta '## Cierre' | .cursor/skills/rsl-picoc/SKILL.md: falta '## Cierre' | .cursor/skills · .cursor/agents · README |
| S04 | skills | cada skill rsl-* tiene la sección Cierre con el contrato OK/ERROR | `(verificación)` | OK | .cursor/skills/rsl-resultado-formulario-apply/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills/rsl-resultado-formulario-apply/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills · .cursor/agents · README |
| S04 | skills | cada skill rsl-* tiene la sección Cierre con el contrato OK/ERROR | `(verificación)` | OK | .cursor/skills/rsl-resultado-formulario-prepare/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills/rsl-resultado-formulario-prepare/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills · .cursor/agents · README |
| S04 | skills | cada skill rsl-* tiene la sección Cierre con el contrato OK/ERROR | `(verificación)` | OK | .cursor/skills/rsl-resultado-items/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills/rsl-resultado-items/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills · .cursor/agents · README |
| S04 | skills | cada skill rsl-* tiene la sección Cierre con el contrato OK/ERROR | `(verificación)` | OK | .cursor/skills/rsl-turnitin-arreglar/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills/rsl-turnitin-arreglar/SKILL.md: el Cierre no define `OK: … Próximo paso: …` y `ERROR: …` | .cursor/skills · .cursor/agents · README |
| S05 | skills | sin restos de reglas viejas (PICO \| PICOC \| PICOCT, picoc-polish, mínimos en agentes) | `(verificación)` | OK | .cursor/agents/turnitin-rsl.md: mínimo obligatorio de hallazgos | .cursor/agents/turnitin-rsl.md: mínimo obligatorio de hallazgos | .cursor/skills · .cursor/agents · README |
| S09 | skills | rsl-resultado-items exige debate (2 rondas), redaccion-rsl, lint y ERROR sin consenso | `(verificación)` | OK | rsl-resultado-items/SKILL.md no contiene «pendiente» | rsl-resultado-items/SKILL.md no contiene «pendiente» | .cursor/skills · .cursor/agents · README |

## Ataques propuestos

_(los agrega rsl-qa-destroy tras la corrida; rsl-qa-fix los convierte en casos)_
