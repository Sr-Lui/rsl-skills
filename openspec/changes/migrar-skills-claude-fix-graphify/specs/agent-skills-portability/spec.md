# Spec Delta

## Purpose

Garantiza que las skills, agentes y reglas del repositorio RSL se descubran y funcionen igual en Cursor y en Claude Code, desde una única fuente de verdad.

## ADDED Requirements

### Requirement: Skills disponibles en Claude Code
El sistema SHALL exponer cada skill de `.cursor/skills/<nombre>/` como `.claude/skills/<nombre>/` sin duplicar su contenido.

#### Scenario: Skill descubierta
- **WHEN** se ejecuta la sincronización y luego se abre Claude Code en el repo
- **THEN** `rsl-resultado-formulario-apply` y las demás skills `rsl-*` y `graphify-*` aparecen como invocables

#### Scenario: Edición única
- **WHEN** se edita `.cursor/skills/<nombre>/SKILL.md`
- **THEN** Claude Code y Cursor leen el mismo texto sin pasos adicionales

### Requirement: Agentes disponibles en Claude Code
El sistema SHALL exponer cada agente de `.cursor/agents/*.md` como agente de Claude Code en `.claude/agents/` con frontmatter válido (`name`, `description`).

#### Scenario: Agente invocable
- **WHEN** una skill pide el agente `critico-rsl`
- **THEN** existe `.claude/agents/critico-rsl.md` con el mismo contenido que el original

### Requirement: Reglas de Graphify en Claude Code
El sistema SHALL proveer un `CLAUDE.md` que incorpore las reglas de `.cursor/rules/graphify.mdc`.

#### Scenario: Reglas cargadas
- **WHEN** Claude Code inicia sesión en el repo
- **THEN** conoce los ámbitos de grafo y los comandos `pnpm graphify:<scope>:query`

### Requirement: Rutas sin enlaces rotos
Las skills y agentes SHALL referenciar playbooks y scripts con rutas desde la raíz del repo, no con rutas relativas al directorio de la skill.

#### Scenario: Comprobación de enlaces
- **WHEN** se ejecuta la comprobación de sincronización
- **THEN** cada ruta a `playbooks/`, `scripts/` o `global/` citada en un SKILL.md o agente existe, y los incumplimientos se listan con archivo y línea

### Requirement: Sincronización idempotente
El comando de sincronización SHALL poder ejecutarse repetidamente sin modificar archivos fuente ni crear duplicados, y SHALL informar de entradas obsoletas.

#### Scenario: Skill nueva
- **WHEN** se añade una skill en `.cursor/skills/` y se ejecuta la sincronización
- **THEN** aparece en `.claude/skills/` y las skills `openspec-*` existentes no se tocan
