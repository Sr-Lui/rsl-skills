# RQ3-B1 — Ronda 1 — Defensor

Bloque: RQ3-I1, subcampo `Constructo` (métrica principal de evaluación). Agregación por frecuencia, síntesis aditiva y presentación en tabla. Las cifras salen de `tablas/RQ3-B1.json`, regenerada tras la recodificación, con base n = 73 (`items_meta.RQ3-I1.n_base`; ítem mixto, presente en las dos hojas).

## Texto propuesto

<!-- inicio -->
### 3.?. Métricas y constructos de evaluación reportados (RQ3)

El ítem de métrica principal se registró en los 73 estudios seleccionados (24 cuantitativos, 30 cualitativos y 19 mixtos). En 27 de ellos el texto completo permite identificar el constructo de la métrica principal; en el 63% (n=46) el constructo no se especifica o no se confirma. La Tabla {{T1}} agrupa los constructos identificados en cinco familias.

Las métricas de rendimiento del modelo de IA reúnen 13 de los 27 estudios con constructo: la exactitud (*accuracy*) se reporta en el 10% (n=7), la precisión, la exhaustividad o el F1 en el 7% (n=5) y la métrica SARI de calidad de simplificación en el 1% (n=1). Las medidas del desempeño de las personas usuarias reúnen 6 estudios: la comprensión lectora, el desempeño en la tarea y la eficacia de la intervención se reportan cada una en el 3% (n=2). La usabilidad reúne 5 estudios: la System Usability Scale (SUS) en el 5% (n=4) y un índice heurístico de usabilidad y accesibilidad en el 1% (n=1). Los índices de legibilidad se reportan en el 3% (n=2) y la validez y fiabilidad de un instrumento en el 1% (n=1). Entre los 27 estudios con constructo identificado, ninguno reporta como métrica principal la carga cognitiva, la experiencia de usuario ni la calidad del software.

**Tabla {{T1}}**

*Constructos de la métrica principal de evaluación reportados en los estudios*

| Familia | Constructo de la métrica principal | Frecuencia (n) | Porcentaje |
|---|---|---|---|
| **Rendimiento del modelo** | Exactitud (*accuracy*) | 7 | 10% |
| | Precisión, exhaustividad o F1 | 5 | 7% |
| | Calidad de simplificación (SARI) | 1 | 1% |
| **Desempeño de las personas usuarias** | Comprensión lectora | 2 | 3% |
| | Desempeño en la tarea | 2 | 3% |
| | Eficacia de la intervención | 2 | 3% |
| **Usabilidad** | System Usability Scale (SUS) | 4 | 5% |
| | Índice heurístico de usabilidad y accesibilidad | 1 | 1% |
| **Legibilidad** | Índice de legibilidad (Flesch Reading Ease) | 2 | 3% |
| **Validez del instrumento** | Validez y fiabilidad del instrumento | 1 | 1% |
| **Constructo no especificado o no confirmado** | — | 46 | 63% |

*Nota.* Datos extraídos de los 73 artículos seleccionados (base n=73). Se registra un constructo por estudio, de modo que las filas suman 73. En 39 estudios el registro indicaba una métrica sin constructo ni valor principal, y en 7 el constructo registrado no se confirmó en el texto completo; ambos casos figuran como constructo no especificado o no confirmado. No se tabulan los valores numéricos porque los del registro no coinciden con el texto completo.

La distribución es heterogénea según el tipo de estudio. Identifican un constructo 18 de los 24 estudios cuantitativos, frente a 5 de los 19 mixtos y 4 de los 30 cualitativos. Las métricas de desempeño de las personas usuarias, la calidad de simplificación y la validez del instrumento solo aparecen en estudios cuantitativos, y las de rendimiento del modelo se concentran en los cuantitativos (8 de 13). La diferencia coincide con el diseño de los estudios: los cualitativos reportan sus resultados como temas de entrevistas, talleres o análisis de registros, sin una métrica principal cuantificada.
<!-- fin -->

## Decisiones

- **Recodificación hecha (`codificacion/RQ3-I1.jsonl`): 73 de 73 filas con `auto: false`.**
  - **«Métrica reportada» → NR (39 filas)**, según el `plan_recodificacion`. El valor bruto de las 39 es idéntico («Se mencionan métricas, pero sin valor numérico principal claro en el texto»), así que no se puede recodificar desde el valor. Se codifica como `Constructo: NR` y el script lo cuenta como no reportado.
  - **Cotejo de las 34 filas con constructo contra el MD** (resumen y cuerpo, sin el bloque de plantilla ni las referencias). Hice este cotejo porque R016 tenía «accuracy = 5» y su resumen dice «readability quantified as Flesch Reading Ease scores». El resultado fue este:
    - **16 se confirman.** R040, R173, R183, R208, R246, R263, R285, R300, R345, R473, R527, R538, R549, R600, R627 y R643.
    - **11 cambian de constructo, con la evidencia en cada fila.** R016 pasa de *accuracy* a índice de legibilidad. R296 y R617 pasan a comprensión lectora (en R296 el 55% de «accuracy» es de un estudio citado). R337 pasa de SUS al índice heurístico U + A (el artículo dice «we could have conducted an SUS survey», es decir, no lo aplicó). R360 pasa de *recall* a SUS (94 y 92,5). R396 y R630 pasan a desempeño en la tarea. R440 y R457 pasan a eficacia de la intervención (R457 es una simulación de 500 perfiles). R595 pasa a SARI, que el artículo declara como «the main metric». R710 pasa a validez y fiabilidad.
    - **7 pasan a NR** porque la palabra registrada tiene otro sentido o solo aparece en los antecedentes. En R197 y R347, *recall* significa «recordar». En R721 la cadena es «precision of 32-bit floating-point». En R187, R393 y R581, *accuracy* aparece en antecedentes, discusión o temas de entrevista. En R376, Flesch-Kincaid solo se usó para adaptar un cuestionario.
  - **Flesch y Flesch-Kincaid → «Índice de legibilidad».** La etiqueta es la misma que en RQ3-I2, para que el libro de códigos sea común (`codebook.md`, `## RQ3-I1` y `## RQ3-I2`). El plan proponía «Legibilidad (índice)», pero uso la etiqueta de RQ3-B2 para que el mismo código no tenga dos nombres. Si el crítico prefiere la del plan, la cambio en las dos.
  - **Valores:** no se agregan ni se publican. En las filas cambiadas, `valores.Valor` lleva el valor verificado marcado «(no se agrega)» solo en R016 y R040. El resto queda como estaba y no lo usa la tabla.
- **Base y cifras.** La base es 73, porque el ítem está en las dos hojas. Los porcentajes de la tabla se calculan sobre 73, no sobre 34 como preveía el plan. Lo hago así porque `sintesis:aggregate` usa la base del ítem y porque, tras el cotejo, la base de constructos ya no sería 34 sino 27. Las sumas por familia (13, 6, 5, 2 y 1) son sumas de filas de un ítem univalor y se dan sin porcentaje. «27 de los 73» se obtiene como 73 − 46 (NR de la tabla). La heterogeneidad sale de `por_naturaleza`, con 18 cuantitativos, 5 mixtos y 4 cualitativos con constructo.
- **«Ninguno reporta carga cognitiva, experiencia de usuario ni calidad del software»** se limita a los 27 estudios con constructo, como dice el texto. R396 aplica NASA-TLX, pero como medida secundaria junto a la exactitud y el tiempo del proceso. No afirmo nada sobre los 46 NR.
- **Presentación:** una tabla, como se acordó. La agrupé por familia para responder a la RQ3, que pregunta por familias de métricas como usabilidad, legibilidad o carga cognitiva. No hay figura.
- **Límite.** Los 46 NR son la mayoría. Si el crítico lo pide en la R2, se pueden recodificar los 39 «Métrica reportada» desde el resumen del MD; el plan no lo preveía y yo no lo hice en esta ronda.
