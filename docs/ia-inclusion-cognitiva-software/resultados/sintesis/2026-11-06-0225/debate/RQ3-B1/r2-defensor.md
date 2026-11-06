# RQ3-B1 — Ronda 2 — Defensor

Respuesta punto por punto a `r1-critico.md`. Acepto las seis objeciones. Tras la recodificación, `tablas/RQ3-B1.json` se regeneró con `sintesis:aggregate` y la base sigue siendo n = 73. Ahora las 73 filas de `codificacion/RQ3-I1.jsonl` llevan `evidencia`.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | Las 39 filas «Métrica reportada» son un sesgo del registro y no se verificaron | **Acepto, y amplío a las 39.** El crítico pedía como mínimo las 18 cuantitativas o mixtas. Recodifiqué las 39 desde el resumen y el cuerpo del MD, con `evidencia` en cada fila | Las 39 se reparten así: 19 con constructo y 20 en NR. **Las 18 de la lista del crítico:** R106 y R369 a comprensión del contenido; R123 y R239 a desempeño lector; R145 a desempeño en la tarea; R147 y R293 a eficacia de la intervención; R203, R398 y R623 a satisfacción; R233 a aceptación tecnológica (TAM); R377 a otras métricas del modelo; R504 a calidad del texto generado (BLEU y GLEU); R831 a exactitud; R199, R425, R587 y R626 a NR, porque son estudios de necesidades o requisitos y no evalúan el artefacto. **El resto de las 39:** R219 y R495 a inspección heurística; R356 y R705 a otras métricas del modelo; R693 a UEQ; 16 cualitativos a NR. Familias nuevas: «Experiencia de usuario» (satisfacción y UEQ) y «Usabilidad y aceptación» (SUS, inspección heurística y TAM). Renombro «Comprensión lectora» a «Comprensión del contenido» (incluye subtítulos), «SARI» a «Calidad del texto generado (SARI, BLEU, GLEU)» y el índice U + A a «Inspección heurística de usabilidad y accesibilidad» |
| 2 | El NR mezcla 7 verificados con 39 sin verificar y atribuye a los estudios un hueco de la extracción | **Acepto** | Ya no quedan filas sin verificar. Hay 27 NR verificados, y el texto dice «en el 37% (n=27) el texto completo no reporta una métrica principal». La *Nota.* desglosa los motivos |
| 3 | La frase de ausencias (carga cognitiva, experiencia de usuario, calidad del software) interpreta | **Acepto** | La frase se retira. Además, la experiencia de usuario ya aparece en 4 estudios (satisfacción y UEQ) |
| 4 | Generaliza a los 30 cualitativos y descansa en NR sin verificar | **Acepto** | Recalculado con `por_naturaleza`: reportan una métrica principal 22 de 24 cuantitativos, 15 de 19 mixtos y 9 de 30 cualitativos. La frase pasa a «21 de los 30 estudios cualitativos no reportan una métrica principal cuantificada» |
| 5 | La cifra principal va sin el formato X% (n=Y) | **Acepto** | «el 63% (n=46)» con constructo y «el 37% (n=27)» sin métrica principal |
| 6 | La *Nota.* generaliza la falta de coincidencia de los valores | **Acepto** | Cambia a «varios valores numéricos del registro no coinciden con el texto completo y no se verificaron todos» |

## Texto propuesto

<!-- inicio -->
### 3.?. Métricas y constructos de evaluación reportados (RQ3)

El ítem de métrica principal se registró en los 73 estudios seleccionados (24 cuantitativos, 30 cualitativos y 19 mixtos). El 63% (n=46) reporta una métrica principal de evaluación, y en el 37% (n=27) el texto completo no reporta ninguna. La Tabla {{T1}} agrupa los constructos de la métrica principal en seis familias.

Las métricas de rendimiento del modelo de IA reúnen 18 de los 46 estudios con métrica principal. La exactitud (*accuracy*) se reporta en el 11% (n=8), la precisión, la exhaustividad o el F1 en el 7% (n=5), otras métricas calculadas sobre las salidas del modelo en el 4% (n=3) y la calidad del texto generado (SARI, BLEU o GLEU) en el 3% (n=2). Las medidas del desempeño de las personas usuarias reúnen 13 estudios: la comprensión del contenido y la eficacia de la intervención se reportan cada una en el 5% (n=4), el desempeño en la tarea en el 4% (n=3) y el desempeño lector en el 3% (n=2). La usabilidad y la aceptación reúnen 8 estudios: la System Usability Scale (SUS) en el 5% (n=4), la inspección heurística de usabilidad y accesibilidad en el 4% (n=3) y el modelo de aceptación tecnológica (TAM) en el 1% (n=1). La experiencia de usuario reúne 4 estudios: la satisfacción en el 4% (n=3) y el User Experience Questionnaire (UEQ) en el 1% (n=1). Los índices de legibilidad se reportan en el 3% (n=2) y la validez y fiabilidad de un instrumento en el 1% (n=1).

**Tabla {{T1}}**

*Constructos de la métrica principal de evaluación reportados en los estudios*

| Familia | Constructo de la métrica principal | Frecuencia (n) | Porcentaje |
|---|---|---|---|
| **Rendimiento del modelo** | Exactitud (*accuracy*) | 8 | 11% |
| | Precisión, exhaustividad o F1 | 5 | 7% |
| | Otras métricas del modelo (cobertura, tasa de éxito en simulación, especificidad del vocabulario) | 3 | 4% |
| | Calidad del texto generado (SARI, BLEU, GLEU) | 2 | 3% |
| **Desempeño de las personas usuarias** | Comprensión del contenido | 4 | 5% |
| | Eficacia de la intervención | 4 | 5% |
| | Desempeño en la tarea | 3 | 4% |
| | Desempeño lector | 2 | 3% |
| **Usabilidad y aceptación** | System Usability Scale (SUS) | 4 | 5% |
| | Inspección heurística de usabilidad y accesibilidad | 3 | 4% |
| | Modelo de aceptación tecnológica (TAM) | 1 | 1% |
| **Experiencia de usuario** | Satisfacción | 3 | 4% |
| | User Experience Questionnaire (UEQ) | 1 | 1% |
| **Legibilidad** | Índice de legibilidad (Flesch Reading Ease) | 2 | 3% |
| **Validez del instrumento** | Validez y fiabilidad del instrumento | 1 | 1% |
| **Sin métrica principal** | — | 27 | 37% |

*Nota.* Datos extraídos de los 73 artículos seleccionados (base n=73). Se registra un constructo por estudio, de modo que las filas suman 73. La fila «Sin métrica principal» reúne estudios cualitativos sin una medida cuantificada, estudios de necesidades o requisitos que no evalúan el artefacto, propuestas o ensayos sin evaluación y un artículo cuyo texto completo no estaba disponible más allá del resumen. No se tabulan los valores numéricos porque varios valores del registro no coinciden con el texto completo y no se verificaron todos.

La distribución es heterogénea según el tipo de estudio. Reportan una métrica principal 22 de los 24 estudios cuantitativos, 15 de los 19 mixtos y 9 de los 30 cualitativos; los 21 estudios cualitativos restantes no reportan una métrica principal cuantificada y presentan sus resultados como temas de entrevistas, talleres o análisis de la interacción. El rendimiento del modelo se reporta en 9 estudios cuantitativos, 5 mixtos y 4 cualitativos, y el desempeño de las personas usuarias en 8 cuantitativos y 5 mixtos, sin ningún cualitativo. La experiencia de usuario aparece sobre todo en estudios mixtos (3 de 4), y la inspección heurística solo en cualitativos (3 de 3).
<!-- fin -->

## Decisiones

- **Recodificación hecha (`codificacion/RQ3-I1.jsonl`): 73 de 73 filas con `auto: false` y `evidencia`.** En esta ronda se recodificaron las 39 filas «Métrica reportada» (19 con constructo y 20 en NR). Las evidencias y los criterios están en cada fila y en `codebook.md` (`## RQ3-I1`, reescrita).
  - **NR por diseño.** R199, R425, R587 y R626 se marcan como estudios de necesidades o requisitos sin evaluación del artefacto, con el mismo criterio que la objeción 3 de RQ3-B4 aplica a R587. R399 tiene el estudio con usuarios «planned», y R1061 se evaluó «informally» y deja el estudio pendiente. R264 es el único NR por disponibilidad: su MD solo contiene el resumen extendido de 2 páginas.
  - **Casos límite que dejo a juicio del crítico.**
    - R145 va a desempeño en la tarea («engagement duration, interaction frequency, and task completion»), y no a experiencia de usuario.
    - R398 va a satisfacción (comodidad 4,6/5, satisfacción 4,3/5), aunque también reporta un 20,5% de mejora en la prueba NAEP.
    - R369 va a comprensión del contenido (de 54% a casi 100% de respuestas correctas). NASA-TLX queda como medida secundaria.
- **Cifras:** todas salen de `tablas/RQ3-B1.json`. Las sumas por familia son sumas de filas de un ítem univalor, sin porcentaje:
  - **Por familia:** 18, 13, 8, 4, 2 y 1, que con 27 dan 73.
  - **Por tipo de estudio (`por_naturaleza`):** 22, 15 y 9 con métrica principal. El rendimiento del modelo es 9, 5 y 4, y el desempeño de las personas usuarias 8, 5 y 0.
- **«El 63% (n=46)»** es el complemento de la fila NR (73 − 27) y no una categoría de la tabla, así que `sintesis:lint` dará un aviso W (no un error), porque cuadra con la base 73. Lo mantengo por la objeción 5. Si el orquestador prefiere evitar el aviso, se puede escribir «46 de los 73».
- **Presentación:** se mantiene la tabla agrupada por familia. La fila de NR pasa a llamarse «Sin métrica principal», porque ahora es un dato verificado de la literatura y ya no un hueco del registro.
