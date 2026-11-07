# Spec Delta

## Purpose

Permite localizar evidencia de un artículo del cribado-2 consultando el grafo y leyendo solo los rangos de línea necesarios del MD, para minimizar el consumo de tokens.

## ADDED Requirements

### Requirement: Consulta acotada a un artículo
`cribado2:query` SHALL aceptar un `corpus_id` y devolver únicamente nodos cuyo `src` pertenezca a ese artículo.

#### Scenario: Sin ruido de otros artículos
- **WHEN** se consulta con `corpus_id` R016
- **THEN** ningún nodo devuelto tiene `src` de otro artículo (p. ej. R029 o R568)

#### Scenario: Artículo inexistente
- **WHEN** el `corpus_id` no existe en el grafo
- **THEN** el comando termina con error y mensaje que indica el siguiente paso

### Requirement: Presupuesto y truncado explícitos
`cribado2:query` SHALL permitir fijar el presupuesto de salida y SHALL indicar cuando hubo truncado.

#### Scenario: Salida truncada
- **WHEN** la respuesta supera el presupuesto
- **THEN** la salida indica cuántos nodos se omitieron y cómo acotar o ampliar

### Requirement: Outline por artículo con rangos de línea
El sistema SHALL ofrecer `cribado2:outline` que, dado un `corpus_id`, liste secciones, hallazgos y anclas del MD con su rango de líneas y página PDF.

#### Scenario: Lectura mínima
- **WHEN** se ejecuta el outline de R016
- **THEN** cada entrada incluye título, página, línea inicial y final, de modo que el tramo puede leerse sin cargar el MD completo

#### Scenario: Salida compacta
- **WHEN** se ejecuta el outline de un MD de ~1200 líneas
- **THEN** la salida es órdenes de magnitud menor que el MD y no incluye el texto de los chunks

### Requirement: Consultas de solo lectura
Las consultas y el outline SHALL NOT modificar el grafo, los MD ni el manifiesto.

#### Scenario: Sin efectos
- **WHEN** se ejecutan query y outline
- **THEN** `git status` no muestra cambios nuevos
