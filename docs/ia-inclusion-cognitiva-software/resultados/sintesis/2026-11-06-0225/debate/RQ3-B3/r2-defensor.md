# RQ3-B3 — Ronda 2 — Defensor

Respuesta punto por punto a `r1-critico.md`. Acepto las dos objeciones. RQ3-I3 no cambia. `tablas/RQ3-B3.json` se regeneró tras recodificar una fila de RQ3-I4.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | R630 → «Ambas» con evidencia tomada de la motivación. La evaluación solo es motora, así que «Ningún estudio evalúa solo dimensiones sensoriales» es falso | **Acepto.** El MD lo confirma: «Our participants were two patients… having involuntary head movements caused by Hypertension and Cervical Strain», y solo mide el tiempo y la exactitud de la selección con la mirada | R630 → «Sensorial o motora», con esa evidencia. Renombré la categoría del codebook de «Sensorial» a «Sensorial o motora» y añadí la regla «se codifica la población y los criterios de la evaluación, no la motivación». Queda así: cognitiva 34 (79%), ambas 8 (19%) y sensorial o motora 1 (2%). La frase pasa a «Únicamente 1 estudio (2%) evalúa solo una dimensión motora». Homogeneidad recalculada: cuantitativos 18, 5 y 1; mixtos 16, 3 y 0 |
| 2 | «participantes… con parálisis cerebral» no se sostiene, y R457 no tiene participantes | **Acepto** | Cambia a «o con participantes sordos o con discapacidad visual, o con perfiles simulados de baja visión» |

## Texto propuesto

<!-- inicio -->
### 3.?. Marco normativo de accesibilidad y cobertura cognitiva frente a sensorial (RQ3)

El marco normativo se registró en los 49 estudios con enfoque cualitativo o mixto (30 cualitativos y 19 mixtos). En el texto completo de cada uno se verificó si el estudio aplica el marco al diseño o a la evaluación del artefacto o si solo lo menciona. El 67% (n=33) no se adscribe a ningún marco normativo de accesibilidad. Entre los que sí lo hacen, las Pautas de Accesibilidad para el Contenido Web (WCAG) se aplican en el 16% (n=8), las pautas de Lectura Fácil o de lenguaje claro en el 12% (n=6) y otros marcos (Diseño Universal para el Aprendizaje, pautas de reducción de la complejidad textual y la norma EN 301 549) en el 8% (n=4). Las orientaciones de accesibilidad cognitiva del W3C (COGA) se aplican en el 4% (n=2), en ambos casos junto a las WCAG. Además, el 10% (n=5) menciona las WCAG sin aplicarlas (en los antecedentes, como crítica de su alcance cognitivo o como auditoría prevista) y el 4% (n=2) menciona COGA solo en los antecedentes. Un estudio puede adscribirse a más de un marco, de modo que los porcentajes no suman 100%.

La adscripción es heterogénea según el tipo de estudio. Las WCAG se aplican en 7 estudios cualitativos y 1 mixto, y los dos estudios con COGA son cualitativos; en cambio, otros marcos aparecen en 3 estudios mixtos y 1 cualitativo. La ausencia de marco es la categoría más frecuente en ambos grupos (20 estudios cualitativos y 13 mixtos).

La cobertura de la evaluación se registró en los 43 estudios con enfoque cuantitativo o mixto (24 cuantitativos y 19 mixtos). El 79% (n=34) evalúa solo dimensiones cognitivas, como la comprensión, la legibilidad, la atención o la usabilidad para la población con discapacidad cognitiva o neurodivergencia. El 19% (n=8) incluye además dimensiones sensoriales o motoras. Lo hace con criterios como el contraste de color, la compatibilidad con lectores de pantalla o el cumplimiento de las WCAG, con participantes sordos o con discapacidad visual, o con perfiles simulados de baja visión. Únicamente 1 estudio (2%) evalúa solo una dimensión motora. La distribución es homogénea entre los dos tipos de estudio. La evaluación solo cognitiva predomina en los cuantitativos (18 estudios, frente a 5 con ambas dimensiones y 1 solo motora) y en los mixtos (16 frente a 3).
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ3-I4.jsonl`).** Solo cambia R630, a «Sensorial o motora», con `auto: false` y `evidencia`. Las 43 filas siguen verificadas.
  - **Nueva lectura de las otras 8 «Ambas» con el criterio de la evaluación.** R369 sí tiene participantes sordos. R233 y R246 comprueban contraste, lector de pantalla o WCAG AA. R538 incluye un módulo de lengua de signos. R527 reporta la autenticación de estudiantes con discapacidad visual. R377 y R457 modelan perfiles de deficiencia visual, auditiva o motora en simulación. R263 está dirigido a estudiantes con discapacidad física y visual, con una evaluación de cumplimiento WCAG.
  - **El texto ya no dice «participantes» de forma genérica**, por R377, R457 y R263.
- **RQ3-I3 sin cambios.** El crítico aceptó la verificación, incluidos R605 y R1061.
- **Codebook:** `## RQ3-I4` reescrita, con la categoría «Sensorial o motora» y la regla de evaluación frente a motivación.
- **Cifras:** todas salen de `tablas/RQ3-B3.json`.
  - **RQ3-I4:** 34, 8 y 1 sobre 43, es decir, 79%, 19% y 2%.
  - **Por tipo de estudio (`por_naturaleza`):** 18, 5 y 1 en los cuantitativos; 16 y 3 en los mixtos.
- **Presentación:** texto, sin cambios.
