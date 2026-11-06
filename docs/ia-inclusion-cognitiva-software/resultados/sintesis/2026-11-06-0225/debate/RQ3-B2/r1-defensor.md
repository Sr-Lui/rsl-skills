# RQ3-B2 — Ronda 1 — Defensor

Bloque: RQ3-I2, instrumento o protocolo de medición. Agregación por frecuencia, síntesis aditiva y presentación en texto. Las cifras salen de `tablas/RQ3-B2.json`, regenerada tras la recodificación, con base n = 49 estudios cualitativos o mixtos (`items_meta.RQ3-I2.n_base`).

## Texto propuesto

<!-- inicio -->
### 3.?. Instrumentos y protocolos de medición (RQ3)

El ítem de instrumentos se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos). El estudio con usuarios es el protocolo más reportado: el 69% (n=34) evalúa el artefacto con personas que lo usan, lo prueban o lo valoran en sesiones, tareas, entrevistas, talleres de codiseño u observación. El 55% (n=27) emplea cuestionarios, entre ellos escalas Likert y escalas estandarizadas como la SUS. El 16% (n=8) aplica una inspección heurística por expertos y el 6% (n=3) calcula un índice de legibilidad sobre el texto que produce el artefacto. El 18% (n=9) no reporta una evaluación con instrumento ni con usuarios. Un estudio puede emplear más de un instrumento, de modo que los porcentajes no suman 100%.

Los resultados son heterogéneos según el tipo de estudio. El cuestionario aparece en 16 de los 19 estudios mixtos y en 11 de los 30 cualitativos, mientras que el estudio con usuarios se reporta en 21 estudios cualitativos y 13 mixtos, y la inspección heurística en 6 cualitativos y 2 mixtos. La diferencia en el uso del cuestionario coincide con el diseño de los estudios mixtos, que añaden una medida cuantitativa a la evaluación con usuarios.
<!-- fin -->

## Decisiones

- **Recodificación hecha (`codificacion/RQ3-I2.jsonl`): 23 de 49 filas con `auto: false`.**
  - **«Legibilidad» → «Índice de legibilidad», solo en 3 de 16 filas.** El plan preveía renombrar las 16, pero antes las cotejé con el MD buscando Flesch, Kincaid, *readability formula/score/index* y *reading ease*. En 13 la legibilidad es un criterio de diseño («Colour and readability»), un tema de entrevistas o una crítica, no un índice calculado. En esas 13 se retira la categoría, porque renombrarla a «índice» afirmaría algo que el texto no dice. Se mantiene en R208 (Flesch Reading Ease 88,4), R393 («Using a standard readability formula») y R399 («automatic quality checkpoints that assess readability»). El código es el mismo que en RQ3-I1 (`codebook.md`).
  - **Retirada de categorías sin ningún apoyo en el cuerpo del MD (9 filas, con la evidencia en cada una).**
    - Se quita «Cuestionario» en R187, R327 y R347, que no mencionan *questionnaire*, *survey*, Likert ni ninguna escala. Lo que tienen son entrevistas, talleres y registros de chat.
    - En R356 se cambia «Cuestionario», que no tiene apoyo, por «Estudio con usuarios», porque reporta talleres de codiseño con personas con DI.
    - En R600 se quita «Heurística»: no aparece *heuristic* en el texto, y lo que reporta es SUS y observación.
    - Pasan a NR R391 (solo describe la herramienta), R453 (ensayo conceptual), R583 (prototipo de laboratorio grabado en vídeo) y R880 (propuesta de API sin evaluación propia).
  - **Sin cambios en el resto**, como preveía el plan. Limitación: el valor bruto es una lista de palabras clave y no dice qué mide cada instrumento. Por eso el texto no describe instrumentos uno por uno y la lista no se usa.
- **Cifras:** todas salen de `tablas/RQ3-B2.json`, con base 49. Las cifras por tipo de estudio (16/19, 11/30, 21 y 13, 6 y 2) salen de `por_naturaleza`. Las métricas automáticas de rendimiento del modelo no son instrumentos de este ítem. Están en RQ3-B1 y RQ3-B4, y por eso no se añadió una categoría para ellas.
- **Presentación:** texto con X% (n=Y), como se acordó (cuatro categorías y NR). No hay tabla ni figura.
- **Límite.** El cotejo se hizo por términos, no leyendo cada MD entero. Puede que haya estudios con cuestionario que lo nombren de otra forma (p. ej., «rating form»), así que no añadí categorías nuevas salvo en R356. R264 conserva «Estudio con usuarios», aunque su MD casi no tiene cuerpo de texto (solo el índice), y no se pudo verificar.
