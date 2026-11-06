# RQ3-B1 — Ronda final — Defensor

Propuesta de consenso sobre las dos objeciones de `r2-critico.md`. Acepto las dos: las verifiqué en el MD y las apliqué. `tablas/RQ3-B1.json` se regeneró con base n = 73.

| # | Objeción R2 | Propuesta de consenso |
|---|---|---|
| 1 | R398 y R623 no son «Satisfacción» | **Aceptada y verificada.** R398 pasa a «Eficacia de la intervención»: el MD compara la mejora en la prueba NAEP con la enseñanza tradicional (20,5% frente a 8,2%, l. 169), con el mismo criterio que R147, R293 y R440. R623 pasa a «Cuestionario de usabilidad *ad hoc*», en la familia «Usabilidad y aceptación»: lo respondieron 110 visitantes con puntuaciones de 0 a 10 por sección (l. 378–390), y la experimentación clínica «currently just started». Queda así: eficacia 5, desempeño de las personas usuarias 14, usabilidad y aceptación 9, satisfacción 1 y experiencia de usuario 2 (1 mixto y 1 cualitativo). La frase «sobre todo en estudios mixtos (3 de 4)» se retira |
| 2 | Los 21 cualitativos sin métrica no presentan todos temas de entrevistas | **Aceptada** con el desglose del crítico, que coincide con la `evidencia` de los `.jsonl`: 13 con temas de entrevistas, talleres o análisis de la interacción, 7 propuestas, ensayos o prototipos sin evaluación formal, y 1 disponible solo como resumen |

## Texto propuesto

<!-- inicio -->
### 3.?. Métricas y constructos de evaluación reportados (RQ3)

El ítem de métrica principal se registró en los 73 estudios seleccionados (24 cuantitativos, 30 cualitativos y 19 mixtos). El 63% (n=46) reporta una métrica principal de evaluación, y en el 37% (n=27) el texto completo no reporta ninguna. La Tabla {{T1}} agrupa los constructos de la métrica principal en seis familias.

Las métricas de rendimiento del modelo de IA reúnen 18 de los 46 estudios con métrica principal. La exactitud (*accuracy*) se reporta en el 11% (n=8), la precisión, la exhaustividad o el F1 en el 7% (n=5), otras métricas calculadas sobre las salidas del modelo en el 4% (n=3) y la calidad del texto generado (SARI, BLEU o GLEU) en el 3% (n=2). Las medidas del desempeño de las personas usuarias reúnen 14 estudios. La eficacia de la intervención se reporta en el 7% (n=5), la comprensión del contenido en el 5% (n=4), el desempeño en la tarea en el 4% (n=3) y el desempeño lector en el 3% (n=2). La usabilidad y la aceptación reúnen 9 estudios: la System Usability Scale (SUS) se emplea en el 5% (n=4), la inspección heurística de usabilidad y accesibilidad en el 4% (n=3), y el modelo de aceptación tecnológica (TAM) y un cuestionario de usabilidad *ad hoc* en el 1% (n=1) cada uno. La experiencia de usuario reúne 2 estudios: la satisfacción y el User Experience Questionnaire (UEQ) se reportan cada uno en el 1% (n=1). Los índices de legibilidad se reportan en el 3% (n=2) y la validez y fiabilidad de un instrumento en el 1% (n=1).

**Tabla {{T1}}**

*Constructos de la métrica principal de evaluación reportados en los estudios*

| Familia | Constructo de la métrica principal | Frecuencia (n) | Porcentaje |
|---|---|---|---|
| **Rendimiento del modelo** | Exactitud (*accuracy*) | 8 | 11% |
| | Precisión, exhaustividad o F1 | 5 | 7% |
| | Otras métricas del modelo (cobertura, tasa de éxito en simulación, especificidad del vocabulario) | 3 | 4% |
| | Calidad del texto generado (SARI, BLEU, GLEU) | 2 | 3% |
| **Desempeño de las personas usuarias** | Eficacia de la intervención | 5 | 7% |
| | Comprensión del contenido | 4 | 5% |
| | Desempeño en la tarea | 3 | 4% |
| | Desempeño lector | 2 | 3% |
| **Usabilidad y aceptación** | System Usability Scale (SUS) | 4 | 5% |
| | Inspección heurística de usabilidad y accesibilidad | 3 | 4% |
| | Modelo de aceptación tecnológica (TAM) | 1 | 1% |
| | Cuestionario de usabilidad *ad hoc* | 1 | 1% |
| **Experiencia de usuario** | Satisfacción | 1 | 1% |
| | User Experience Questionnaire (UEQ) | 1 | 1% |
| **Legibilidad** | Índice de legibilidad (Flesch Reading Ease) | 2 | 3% |
| **Validez del instrumento** | Validez y fiabilidad del instrumento | 1 | 1% |
| **Sin métrica principal** | — | 27 | 37% |

*Nota.* Datos extraídos de los 73 artículos seleccionados (base n=73). Se registra un constructo por estudio, de modo que las filas suman 73. La fila «Sin métrica principal» reúne cuatro tipos de estudio: cualitativos sin una medida cuantificada, de necesidades o requisitos que no evalúan el artefacto, propuestas o ensayos sin evaluación, y un artículo cuyo texto completo no estaba disponible más allá del resumen. No se tabulan los valores numéricos porque varios valores del registro no coinciden con el texto completo y no se verificaron todos.

La distribución es heterogénea según el tipo de estudio. Reportan una métrica principal 22 de los 24 estudios cuantitativos, 15 de los 19 mixtos y 9 de los 30 cualitativos. Los 21 estudios cualitativos restantes no reportan una métrica principal cuantificada: 13 presentan sus resultados como temas de entrevistas, talleres o análisis de la interacción, 7 son propuestas, ensayos o prototipos sin evaluación formal y 1 solo está disponible como resumen. El rendimiento del modelo se reporta en 9 estudios cuantitativos, 5 mixtos y 4 cualitativos. El desempeño de las personas usuarias se reporta en 8 cuantitativos y 6 mixtos, y en ningún cualitativo. La usabilidad y la aceptación se reparten entre 4 cualitativos, 3 cuantitativos y 2 mixtos, y la inspección heurística solo aparece en cualitativos (3 de 3).
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ3-I1.jsonl`):** se cambiaron R398 y R623 (`auto: false` y `evidencia` con los pasajes del MD). Las 73 filas siguen con `evidencia`. En `codebook.md` (`## RQ3-I1`) se añade «Cuestionario de usabilidad *ad hoc*» y se precisan las definiciones de satisfacción (cuando es la medida principal) y de eficacia (incluye la comparación con la enseñanza tradicional).
- **Cifras:** todas salen de `tablas/RQ3-B1.json`. Las familias, sumas de filas de un ítem univalor, son 18, 14, 9, 2, 2 y 1, que con 27 dan 73. Por tipo de estudio (`por_naturaleza`): el rendimiento del modelo es 9, 5 y 4; el desempeño de las personas usuarias 8, 6 y 0; y la usabilidad y la aceptación 3, 4 y 2. El desglose 13, 7 y 1 de los cualitativos sin métrica sale de la `evidencia` de las 21 filas.
- **Orden:** las familias van en orden descendente por n. Experiencia de usuario y legibilidad empatan a 2 y conservan el orden de la R2.
- **«El 63% (n=46)»** sigue siendo el complemento de la fila NR (aviso W del lint, ya aceptado en la R2).
- **Efecto en RQ3-B4:** en los 9 mixtos que evalúan solo con personas, el desempeño pasa a 6, la usabilidad a 2 y la experiencia de usuario a 1, como anticipaba el crítico.
