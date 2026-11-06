# RQ3-B2 — Ronda final — Defensor

Propuesta de consenso sobre la objeción de `r2-critico.md`. La acepto: es la misma regla de evaluación del artefacto que ya se aplica en RQ3-I1 y RQ3-I5. `tablas/RQ3-B2.json` se regeneró con base n = 49.

| # | Objeción R2 | Propuesta de consenso |
|---|---|---|
| 1 | «evalúa o diseña» amplía el ítem más allá de la evaluación. Los 4 estudios de requisitos y los 2 de codiseño cuentan como instrumentos de evaluación | **Aceptada y verificada.** El texto vuelve a decir «evalúa». Pasan a NR R199, R425, R587 y R626, con la misma evidencia de requisitos que en RQ3-I1 y RQ3-I5, y también R356 y R647. En R356, el MD dice que la evaluación son métricas calculadas «prior to broader user studies», y los talleres son previos. R647 recoge fases de codiseño y una discusión conceptual, sin evaluar el artefacto. Queda así: estudio con usuarios 32 (65%), cuestionario 24 (49%), heurística 7 (14%), índice de legibilidad 1 (2%) y NR 13 (27%), que coincide con la estimación del crítico. Por tipo de estudio: estudio con usuarios en 19 cualitativos y 13 mixtos, cuestionario en 11 y 13, y heurística en 6 y 1 |

## Texto propuesto

<!-- inicio -->
### 3.?. Instrumentos y protocolos de medición (RQ3)

El ítem de instrumentos se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos). El estudio con usuarios es el protocolo más reportado: el 65% (n=32) evalúa el artefacto con personas que lo usan, lo prueban o lo valoran en sesiones, tareas, entrevistas u observación. El 49% (n=24) emplea cuestionarios, entre ellos escalas Likert y escalas estandarizadas como la SUS. El 14% (n=7) aplica una inspección heurística por expertos. Únicamente 1 estudio (2%) calcula un índice de legibilidad sobre el texto que produce el artefacto. El 27% (n=13) no reporta una evaluación del artefacto con instrumento ni con usuarios. En este grupo están las propuestas o los ensayos sin evaluación, los estudios de necesidades o requisitos y los talleres de codiseño previos a la construcción del artefacto. Un estudio puede emplear más de un instrumento, de modo que los porcentajes no suman 100%.

Los resultados son heterogéneos según el tipo de estudio. El cuestionario aparece en 13 de los 19 estudios mixtos y en 11 de los 30 cualitativos. El estudio con usuarios se reporta en 19 estudios cualitativos y 13 mixtos, y la inspección heurística en 6 cualitativos y 1 mixto. La diferencia en el uso del cuestionario coincide con el diseño de los estudios mixtos, que añaden una medida cuantitativa a la evaluación con usuarios.
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ3-I2.jsonl`).** Pasan a NR 6 filas con `auto: false` y `evidencia`: R199, R425, R587, R626, R356 y R647. Ya son 30 de 49 las filas con `evidencia`. Las 19 restantes conservan el valor del registro (`auto: true`), lo que se declara en `codebook.md` (`## RQ3-I2`).
- **Codebook (`## RQ3-I2`).** «Estudio con usuarios» se limita al artefacto ya construido y quita los talleres de codiseño de la lista de sinónimos. El NR se define con el mismo criterio que en RQ3-I5.
- **Cifras:** todas salen de `tablas/RQ3-B2.json`. Las categorías son 32, 24, 7, 1 y 13 NR sobre 49 (65, 49, 14, 2 y 27%). Los recuentos por tipo de estudio salen de `por_naturaleza`.
- **Coherencia entre ítems.** Los cuatro estudios de requisitos son ahora NR en RQ3-I1, RQ3-I2, RQ3-I4 y RQ3-I5.
- **Presentación:** texto, sin cambios.
