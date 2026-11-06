# RQ3-B3 — Ronda final — Defensor

Propuesta de consenso sobre la objeción de `r2-critico.md`. La acepto: los cuatro estudios ya están verificados como «no evalúan el artefacto» en RQ3-I1 y RQ3-I5. `tablas/RQ3-B3.json` se regeneró; RQ3-I3 no cambia.

| # | Objeción R2 | Propuesta de consenso |
|---|---|---|
| 1 | R199, R425, R587 y R626 no pueden tener cobertura «cognitiva» si no evalúan el artefacto | **Aceptada.** Los cuatro pasan a NR en RQ3-I4, con la evidencia de requisitos o necesidades. Queda así: cognitiva 30 (70%), ambas 8 (19%), sensorial o motora 1 (2%) y NR 4 (9%). Por tipo de estudio, los cuantitativos tienen 18, 5 y 1, y los mixtos 12, 3 y 4 NR. Se añade la frase «En el 9% (n=4) no hay evaluación del artefacto» y se rehace la frase de homogeneidad. En el codebook, `## RQ3-I4` incorpora la categoría NR |

## Texto propuesto

<!-- inicio -->
### 3.?. Marco normativo de accesibilidad y cobertura cognitiva frente a sensorial (RQ3)

El marco normativo se registró en los 49 estudios con enfoque cualitativo o mixto (30 cualitativos y 19 mixtos). En el texto completo de cada uno se verificó si el estudio aplica el marco al diseño o a la evaluación del artefacto o si solo lo menciona. El 67% (n=33) no se adscribe a ningún marco normativo de accesibilidad. Entre los que sí lo hacen, las Pautas de Accesibilidad para el Contenido Web (WCAG) se aplican en el 16% (n=8), las pautas de Lectura Fácil o de lenguaje claro en el 12% (n=6) y otros marcos (Diseño Universal para el Aprendizaje, pautas de reducción de la complejidad textual y la norma EN 301 549) en el 8% (n=4). Las orientaciones de accesibilidad cognitiva del W3C (COGA) se aplican en el 4% (n=2), en ambos casos junto a las WCAG. Además, el 10% (n=5) menciona las WCAG sin aplicarlas (en los antecedentes, como crítica de su alcance cognitivo o como auditoría prevista) y el 4% (n=2) menciona COGA solo en los antecedentes. Un estudio puede adscribirse a más de un marco, de modo que los porcentajes no suman 100%.

La adscripción es heterogénea según el tipo de estudio. Las WCAG se aplican en 7 estudios cualitativos y 1 mixto, y los dos estudios con COGA son cualitativos; en cambio, otros marcos aparecen en 3 estudios mixtos y 1 cualitativo. La ausencia de marco es la categoría más frecuente en ambos grupos (20 estudios cualitativos y 13 mixtos).

La cobertura de la evaluación se registró en los 43 estudios con enfoque cuantitativo o mixto (24 cuantitativos y 19 mixtos). El 70% (n=30) evalúa solo dimensiones cognitivas, como la comprensión, la legibilidad, la atención o la usabilidad para la población con discapacidad cognitiva o neurodivergencia. El 19% (n=8) incluye además dimensiones sensoriales o motoras. Lo hace con criterios como el contraste de color, la compatibilidad con lectores de pantalla o el cumplimiento de las WCAG, con participantes sordos o con discapacidad visual, o con perfiles simulados de baja visión. Únicamente 1 estudio (2%) evalúa solo una dimensión motora. En el 9% (n=4) no hay evaluación del artefacto, porque el estudio recoge necesidades o requisitos antes de construirlo. La evaluación solo cognitiva predomina en los dos tipos de estudio: abarca 18 de los 24 estudios cuantitativos, frente a 5 con ambas dimensiones y 1 solo motora, y 12 de los 15 estudios mixtos que evalúan el artefacto, frente a 3 con ambas dimensiones. Los 4 estudios sin evaluación del artefacto son mixtos.
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ3-I4.jsonl`).** R199, R425, R587 y R626 pasan a NR, con `auto: false` y `evidencia`. Las 43 filas siguen con `evidencia`.
- **Cifras:** todas salen de `tablas/RQ3-B3.json`.
  - **RQ3-I4:** 30, 8, 1 y 4 NR sobre 43 (70, 19, 2 y 9%).
  - **Por tipo de estudio (`por_naturaleza`):** 18, 5 y 1 en los cuantitativos; 12, 3 y 4 NR en los mixtos.
  - **«12 de los 15 mixtos que evalúan el artefacto».** Es 19 − 4 NR, sin porcentaje porque 15 no es la base de la tabla.
- **RQ3-I3 sin cambios.** El crítico aceptó la verificación en la R1 y la R2.
- **Presentación:** texto, sin cambios.
