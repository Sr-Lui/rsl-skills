# RQ3-B4 — Ronda 2 — Defensor

Respuesta punto por punto a `r1-critico.md`. Acepto las cinco objeciones. Tras recodificar, `tablas/RQ3-B4.json` se regeneró con base n = 43. Ahora las 43 filas de `codificacion/RQ3-I5.jsonl` llevan `auto: false` y `evidencia`.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | R377 es una evaluación por simulación, no una validación con usuarios | **Acepto.** El MD dice «simulation-based evaluations» y «success rate, cumulative rewards, and stability of the policy», y los 24 participantes son de un trabajo citado | R377 → «Automática», con esa evidencia. En RQ3-I1 pasa también a «Otras métricas del modelo» |
| 2 | 20 filas conservaban el valor de plantilla sin `evidencia` | **Acepto** | Las 20 filas llevan ahora `evidencia` y `auto: false`, con los participantes y su n o la métrica. Además de R377 (objeción 1), cambian otras tres filas con el mismo criterio que la objeción 3: R199 (evaluación de necesidades con 62 personas para guiar el desarrollo), R425 (recogida de requisitos con entrevistas) y R626 (cuestionarios de necesidades y preferencias para diseñar OLOS) pasan de «Solo validación» a NR. Las otras 16 se confirman como solo validación con personas, entre ellas R147: el WER mide la lectura de los escolares, no el modelo |
| 3 | R587 recoge requisitos y no evalúa el artefacto | **Acepto** | R587 → NR («la encuesta a 34 expertos recoge requisitos para FACILE; no hay evaluación del artefacto»). Defino NR en el codebook: «el estudio no evalúa el artefacto: recoge necesidades o requisitos antes de construirlo» |
| 4 | Los cruces con la métrica principal dependían del NR sin verificar de RQ3-B1 | **Acepto** | RQ3-B1 se recodificó: las 73 filas llevan `evidencia`. Recalculé los cruces. R504 (BLEU y GLEU) y R831 (exactitud del LLM) ya tienen constructo, y el rendimiento del modelo pasa a 8 de 11 en la evaluación semiautomática y a 6 de 8 en la automática. Se retira «no se especifica en N» |
| 5 | La integración cualitativo↔cuantitativo no daba cifras | **Acepto** | Se añaden los cruces RQ3-I2 × RQ3-I5 en los mixtos, recalculados tras RQ3-B2 #4 y la objeción 3 de este bloque. De los 9 que evalúan solo con personas, 9 usan cuestionario, 7 estudio con usuarios y 1 heurística. De los 6 semiautomáticos, 6 usan estudio con usuarios, 4 cuestionario y 1 índice de legibilidad. Se añaden también los cruces con el marco (RQ3-I3) y con la métrica principal |

## Texto propuesto

<!-- inicio -->
### 3.?. Grado de automatización de la evaluación (RQ3)

El grado de automatización se registró en los 43 estudios con enfoque cuantitativo o mixto (24 cuantitativos y 19 mixtos). El 47% (n=20) evalúa el artefacto solo con personas (usuarios con la condición, cuidadores o expertos), mediante tareas, cuestionarios, entrevistas o valoración experta. El 26% (n=11) sigue una evaluación semiautomática, que combina métricas calculadas por software (rendimiento del modelo, índices de legibilidad, comprobación automática del contraste o puntuaciones de rendimiento web) con la evaluación de personas. El 19% (n=8) evalúa el artefacto solo de forma automática, con métricas calculadas sobre corpus, salidas del modelo o simulaciones y sin participantes. En el 9% (n=4) no hay evaluación del artefacto, porque el estudio recoge necesidades o requisitos antes de construirlo. Ningún estudio reporta una evaluación integrada en el ciclo de construcción del software (integración continua).

La distribución es heterogénea según el tipo de estudio. Los 8 estudios con evaluación solo automática son cuantitativos, y los 4 sin evaluación del artefacto son mixtos. La evaluación solo con personas se reparte entre 11 estudios cuantitativos y 9 mixtos, y la semiautomática entre 5 cuantitativos y 6 mixtos. La diferencia coincide con el diseño de los estudios: las evaluaciones técnicas sobre corpus o simulaciones, sin muestra de participantes, solo aparecen en estudios cuantitativos.

La métrica principal varía con el grado de automatización. El rendimiento del modelo es la métrica principal en 6 de los 8 estudios con evaluación automática y en 8 de los 11 semiautomáticos, y en ninguno de los 20 que evalúan solo con personas. En estos últimos, 12 reportan medidas del desempeño de las personas usuarias. Las dimensiones sensoriales o motoras se evalúan en 4 de los 11 estudios semiautomáticos, 3 de los 8 automáticos y 2 de los 20 que evalúan solo con personas.

**Integración de los resultados cuantitativos y cualitativos de la RQ3.** Los estudios cualitativos (marco normativo e instrumentos) y los cuantitativos (cobertura y automatización) solo coinciden en los 19 estudios mixtos, que registran los cuatro ítems; la métrica principal, registrada en los 73, enlaza ambos grupos.

En la vertiente cuantitativa, 9 de los 19 estudios mixtos evalúan solo con personas, 6 de forma semiautomática y ninguno solo de forma automática; los 4 restantes no evalúan el artefacto. Además, 16 de los 19 cubren solo dimensiones cognitivas. En la vertiente cualitativa, 13 de los 19 no se adscriben a ningún marco normativo de accesibilidad, ninguno aplica COGA y 11 de esos 13 evalúan solo dimensiones cognitivas.

Los instrumentos cualitativos se corresponden con el grado de automatización. Los 9 estudios mixtos que evalúan solo con personas emplean cuestionarios, 7 de ellos también un estudio con usuarios y 1 una inspección heurística. Los 6 semiautomáticos emplean un estudio con usuarios, 4 de ellos también cuestionarios y 1 un índice de legibilidad. La métrica principal sigue la misma división. En los 9 mixtos que evalúan solo con personas es una medida del desempeño de las personas usuarias en 5, de la experiencia de usuario en 3 y de la usabilidad en 1. En los 6 semiautomáticos es el rendimiento del modelo en 5 y un índice de legibilidad en 1. En cuanto al marco normativo, se adscriben 2 de los 9 mixtos que evalúan solo con personas, 2 de los 6 semiautomáticos y 2 de los 4 sin evaluación del artefacto.
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ3-I5.jsonl`): 43 de 43 filas con `auto: false` y `evidencia`.**
  - **Cambios en la R2.** R377 pasa a «Automática». R587, R199, R425 y R626 pasan a NR, porque no evalúan el artefacto; el criterio está en `codebook.md` (`## RQ3-I5`, reescrita). Las otras 16 filas de la objeción 2 se confirman con su evidencia.
  - **Coherencia con RQ3-I1.** Estos cuatro NR también son «Sin métrica principal» en RQ3-I1, y R377 es «Otras métricas del modelo».
- **Cifras del bloque:** todas salen de `tablas/RQ3-B4.json`.
  - **RQ3-I5:** 20, 11, 8 y 4 NR sobre 43, es decir, 47%, 26%, 19% y 9%.
  - **Por tipo de estudio (`por_naturaleza`):** 11 y 9 en solo con personas, 5 y 6 en semiautomática, 8 y 0 en automática, y 0 y 4 en NR.
- **Recuentos cruzados.** Los calculé intersecando las listas `estudios` de `tablas/RQ3-B1.json`, `RQ3-B2.json`, `RQ3-B3.json` y `RQ3-B4.json`, que se regeneraron desde los `.jsonl` de esta ronda. Los mixtos se toman de `matriz.json` (`naturaleza: mixto`, n=19).
  - **Mixtos × RQ3-I5:** 9 solo con personas, 6 semiautomáticos, 0 automáticos y 4 NR.
  - **Mixtos × RQ3-I4:** 16 cognitiva, 3 ambas y 0 sensorial o motora.
  - **Mixtos × RQ3-I3:** 13 sin marco (11 de ellos con cobertura cognitiva) y 6 con adscripción. COGA tiene 0.
  - **Mixtos, RQ3-I2 × RQ3-I5:**
    - Solo con personas (9): cuestionario 9, estudio con usuarios 7 y heurística 1.
    - Semiautomáticos (6): estudio con usuarios 6, cuestionario 4 e índice de legibilidad 1.
    - NR (4): cuestionario 4, estudio con usuarios 3 y heurística 1. No se citan en el texto.
  - **Mixtos, familia de RQ3-I1 × RQ3-I5:**
    - Solo con personas (9): desempeño de las personas usuarias 5, experiencia de usuario 3 y usabilidad y aceptación 1.
    - Semiautomáticos (6): rendimiento del modelo 5 y legibilidad 1.
    - NR (4): los 4 sin métrica principal.
  - **Mixtos, RQ3-I3 × RQ3-I5:** se adscriben a un marco 2 de 9, 2 de 6 y 2 de 4.
  - **Los 43, RQ3-I1 × RQ3-I5:** el rendimiento del modelo está en 6 de 8 automáticos, 8 de 11 semiautomáticos y 0 de 20 solo con personas. El desempeño de las personas usuarias está en 12 de los 20 solo con personas.
  - **Los 43, RQ3-I4 × RQ3-I5:** ambas o sensorial o motora están en 4 de 11 semiautomáticos (4 ambas), 3 de 8 automáticos (3 ambas) y 2 de 20 solo con personas (1 ambas y 1 sensorial o motora).
- **Sin porcentajes en los cruces.** Ni 19 ni los subtotales son bases de una tabla, y `sintesis:lint` exige que cada porcentaje cuadre con una base. Por eso los cruces van como «N de los M».
- **Frase sobre la fase principal:** sigue fuera, porque la tabla no incluye el cruce con RQ2-I3.
