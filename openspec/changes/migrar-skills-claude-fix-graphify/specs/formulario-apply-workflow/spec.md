# Spec Delta

## Purpose

Define cómo se rellenan los ítems RQ del formulario UTP por artículo con evidencia verificable y coste de tokens acotado, ejecutable tanto en Cursor como en Claude Code.

## ADDED Requirements

### Requirement: Una pasada por artículo
La skill SHALL guiar el relleno de cada artículo con el orden: outline, consulta acotada, lectura de tramos por rango de línea, y escritura de `apply-<corpus_id>.json`, sin leer el MD completo salvo necesidad justificada.

#### Scenario: Lectura por rangos
- **WHEN** se procesa el artículo R016
- **THEN** la evidencia se obtiene de tramos identificados por el outline o por `loc` del grafo

### Requirement: Verificación automatizada previa al apply
`formulario:verify-apply-json` SHALL actuar como checklist R2: citas literales de al menos 40 caracteres, `loc` anclado, `quote` distinto de `value`, y cobertura de cada `item_id` esperado por hoja; SHALL emitir advertencias (REVISAR) por cita débil, cifras del `value` ausentes en las citas o una misma cita que sostiene tres o más ítems.

#### Scenario: Cita débil o sin cifra
- **WHEN** una `quote` es literal pero corta (<60 caracteres) o no contiene una cifra citada en el `value`
- **THEN** la verificación emite una advertencia REVISAR con artículo e ítem

#### Scenario: Apply bloqueado
- **WHEN** el lote tiene errores de verificación
- **THEN** la skill no ejecuta `formulario:apply-lote`

### Requirement: Escalado selectivo
El crítico SHALL intervenir solo en los slots marcados por la verificación o por baja confianza, y el orquestador SHALL intervenir solo ante discrepancia entre defensor y crítico.

#### Scenario: Artículo limpio
- **WHEN** la verificación no marca ningún slot
- **THEN** no se generan `r2-critico` ni `orquestador` para ese artículo

#### Scenario: Slot marcado
- **WHEN** la verificación marca un slot
- **THEN** se registra la revisión del crítico antes del apply

### Requirement: Compatibilidad con trabajo previo
La skill SHALL mantener válidos los `apply-*.json` y la traza existentes (lote 01) y SHALL reanudar desde los estudios pendientes.

#### Scenario: Reanudación
- **WHEN** la traza tiene 104 de 736 líneas
- **THEN** la skill identifica los `corpus_id` pendientes y no reescribe los ya aplicados

### Requirement: Cierre bajo condiciones existentes
El cierre SHALL seguir exigiendo `lint-setup`, `lint-traza --strict` y `lint-prosa --strict` en PASS, y SHALL informar de `nature_needs_review` antes del stamp.

#### Scenario: Naturaleza pendiente
- **WHEN** `manifest.nature_needs_review` no está vacío
- **THEN** la skill lo comunica al usuario y no usa `--allow-nature-review` sin su confirmación
