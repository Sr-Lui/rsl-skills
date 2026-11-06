# RQ3-B4 — Ronda final — Defensor

Propuesta de consenso sobre la objeción de `r2-critico.md`. La acepto: recalculé la integración a partir de los `.jsonl` de la ronda final, ya con las correcciones de RQ3-B1, RQ3-B2 y RQ3-B3. RQ3-I5 no cambia de categoría: `tablas/RQ3-B4.json` se regeneró y da 20, 11, 8 y 4 NR sobre 43.

| # | Objeción R2 | Propuesta de consenso |
|---|---|---|
| 1a | Los 4 mixtos sin evaluación del artefacto contaban como «cubren solo dimensiones cognitivas» | **Aceptada.** Con RQ3-I4 corregido (RQ3-B3), el texto dice «12 de los 15 mixtos que evalúan el artefacto cubren solo dimensiones cognitivas». De los 13 sin marco, 9 evalúan solo dimensiones cognitivas, 2 incluyen también dimensiones sensoriales o motoras y 2 no evalúan el artefacto |
| 1b | Las familias de RQ3-I1 en los mixtos solo con personas heredaban la codificación anterior de R398 y R623 | **Aceptada.** En los 9 mixtos solo con personas la métrica principal es ahora el desempeño de las personas usuarias en 6, la usabilidad y la aceptación en 2 y la experiencia de usuario en 1. En los 43, el desempeño pasa a 13 de 20 |
| 1c | Los instrumentos de los 4 NR dependían de RQ3-B2 | **Aceptada.** Los 4 son NR en RQ3-I2, así que no aportan instrumentos. Los cruces de los 9 mixtos solo con personas (9, 7 y 1) y de los 6 semiautomáticos (6, 4 y 1) no cambian |

## Texto propuesto

<!-- inicio -->
### 3.?. Grado de automatización de la evaluación (RQ3)

El grado de automatización se registró en los 43 estudios con enfoque cuantitativo o mixto (24 cuantitativos y 19 mixtos). El 47% (n=20) evalúa el artefacto solo con personas (usuarios con la condición, cuidadores o expertos), mediante tareas, cuestionarios, entrevistas o valoración experta. El 26% (n=11) sigue una evaluación semiautomática, que combina métricas calculadas por software (rendimiento del modelo, índices de legibilidad, comprobación automática del contraste o puntuaciones de rendimiento web) con la evaluación de personas. El 19% (n=8) evalúa el artefacto solo de forma automática, con métricas calculadas sobre corpus, salidas del modelo o simulaciones y sin participantes. En el 9% (n=4) no hay evaluación del artefacto, porque el estudio recoge necesidades o requisitos antes de construirlo. Ningún estudio reporta una evaluación integrada en el ciclo de construcción del software (integración continua).

La distribución es heterogénea según el tipo de estudio. Los 8 estudios con evaluación solo automática son cuantitativos, y los 4 sin evaluación del artefacto son mixtos. La evaluación solo con personas se reparte entre 11 estudios cuantitativos y 9 mixtos, y la semiautomática entre 5 cuantitativos y 6 mixtos. La diferencia coincide con el diseño de los estudios: las evaluaciones técnicas sobre corpus o simulaciones, sin muestra de participantes, solo aparecen en estudios cuantitativos.

La métrica principal varía con el grado de automatización. El rendimiento del modelo es la métrica principal en 6 de los 8 estudios con evaluación automática y en 8 de los 11 semiautomáticos, y en ninguno de los 20 que evalúan solo con personas. En estos últimos, 13 reportan medidas del desempeño de las personas usuarias. Las dimensiones sensoriales o motoras se evalúan en 4 de los 11 estudios semiautomáticos, 3 de los 8 automáticos y 2 de los 20 que evalúan solo con personas.

**Integración de los resultados cuantitativos y cualitativos de la RQ3.** Los estudios cualitativos (marco normativo e instrumentos) y los cuantitativos (cobertura y automatización) solo coinciden en los 19 estudios mixtos, que registran los cuatro ítems; la métrica principal, registrada en los 73, enlaza ambos grupos.

En la vertiente cuantitativa, 9 de los 19 estudios mixtos evalúan solo con personas, 6 de forma semiautomática y ninguno solo de forma automática; los 4 restantes no evalúan el artefacto. De los 15 mixtos que evalúan el artefacto, 12 cubren solo dimensiones cognitivas y 3 incluyen también dimensiones sensoriales o motoras. En la vertiente cualitativa, 13 de los 19 no se adscriben a ningún marco normativo de accesibilidad y ninguno aplica COGA. De esos 13, 9 evalúan solo dimensiones cognitivas, 2 incluyen también dimensiones sensoriales o motoras y 2 no evalúan el artefacto.

Los instrumentos cualitativos se corresponden con el grado de automatización. Los 9 estudios mixtos que evalúan solo con personas emplean cuestionarios, 7 de ellos también un estudio con usuarios y 1 una inspección heurística. Los 6 semiautomáticos emplean un estudio con usuarios, 4 de ellos también cuestionarios y 1 un índice de legibilidad.

La métrica principal sigue la misma división. En los 9 mixtos que evalúan solo con personas es una medida del desempeño de las personas usuarias en 6, de la usabilidad y la aceptación en 2 y de la experiencia de usuario en 1. En los 6 semiautomáticos es el rendimiento del modelo en 5 y un índice de legibilidad en 1. En cuanto al marco normativo, se adscriben 2 de los 9 mixtos que evalúan solo con personas, 2 de los 6 semiautomáticos y 2 de los 4 sin evaluación del artefacto.
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ3-I5.jsonl`).** No cambia ninguna categoría. Solo se actualiza la `evidencia` de R623 con el pasaje del cuestionario de usabilidad respondido por 110 visitantes, que es la evaluación hecha. Las 43 filas siguen con `auto: false` y `evidencia`.
- **Cifras del bloque:** todas salen de `tablas/RQ3-B4.json`.
  - **RQ3-I5:** 20, 11, 8 y 4 NR sobre 43 (47, 26, 19 y 9%).
  - **Por tipo de estudio (`por_naturaleza`):** 11 y 9 en solo con personas, 5 y 6 en semiautomática, 8 y 0 en automática, y 0 y 4 en NR.
- **Recuentos cruzados de la ronda final.** Calculados intersecando las listas `estudios` de `tablas/RQ3-B1.json` a `RQ3-B4.json`, que se regeneraron desde los `.jsonl` actuales. Los mixtos salen de `matriz.json` (`naturaleza: mixto`, n=19).
  - **Mixtos × RQ3-I5:** 9 solo con personas, 6 semiautomáticos, 0 automáticos y 4 NR.
  - **Mixtos que evalúan el artefacto (15) × RQ3-I4:** 12 cognitiva y 3 ambas.
  - **Mixtos sin marco (13) × RQ3-I4:** 9 cognitiva, 2 ambas y 2 NR.
  - **Mixtos × RQ3-I3:** COGA tiene 0. La adscripción a un marco es de 2 de 9 (solo con personas), 2 de 6 (semiautomáticos) y 2 de 4 (NR).
  - **Mixtos, RQ3-I2 × RQ3-I5:**
    - Solo con personas: cuestionario 9, estudio con usuarios 7 y heurística 1.
    - Semiautomáticos: estudio con usuarios 6, cuestionario 4 e índice de legibilidad 1.
    - NR: 4 NR.
  - **Mixtos, familia de RQ3-I1 × RQ3-I5:**
    - Solo con personas: desempeño 6, usabilidad y aceptación 2 y experiencia de usuario 1.
    - Semiautomáticos: rendimiento del modelo 5 y legibilidad 1.
    - NR: 4 sin métrica principal.
  - **Los 43, RQ3-I1 × RQ3-I5:** el rendimiento del modelo está en 6 de 8, 8 de 11 y 0 de 20. El desempeño está en 13 de 20 solo con personas.
  - **Los 43, RQ3-I4 × RQ3-I5:** ambas o sensorial o motora están en 4 de 11 semiautomáticos, 3 de 8 automáticos y 2 de 20 solo con personas.
- **Sin porcentajes en los cruces**, porque ni 19 ni 15 ni los subtotales son bases de una tabla.
- **Coherencia de la RQ3.** Los cuatro estudios de requisitos (R199, R425, R587 y R626) son NR en RQ3-I1, RQ3-I2, RQ3-I4 y RQ3-I5. En RQ3-I3 conservan su codificación de marco, porque ese ítem registra la adscripción del estudio y no solo de la evaluación.
