# RQ3-B4 — Ronda 1 — Defensor

Bloque: RQ3-I5, grado de automatización de la evaluación (base n = 43, estudios cuantitativos y mixtos). Agregación por frecuencia, síntesis aditiva y presentación en texto. Es el bloque de cierre de la RQ3, así que también integra lo cualitativo y lo cuantitativo. Las cifras salen de `tablas/RQ3-B4.json`, regenerada tras verificar cada estudio en el MD. La integración usa además las listas `estudios` de `tablas/RQ3-B1.json`, `RQ3-B2.json` y `RQ3-B3.json`.

## Texto propuesto

<!-- inicio -->
### 3.?. Grado de automatización de la evaluación (RQ3)

El grado de automatización se registró en los 43 estudios con enfoque cuantitativo o mixto (24 cuantitativos y 19 mixtos). El 58% (n=25) evalúa el artefacto solo con personas (usuarios con la condición, cuidadores o expertos), mediante tareas, cuestionarios, entrevistas o valoración experta. El 26% (n=11) sigue una evaluación semiautomática, que combina métricas calculadas por software (rendimiento del modelo, índices de legibilidad, comprobación automática del contraste o puntuaciones de rendimiento web) con la evaluación de personas. El 16% (n=7) evalúa el artefacto solo de forma automática, con métricas calculadas sobre corpus, salidas del modelo o perfiles simulados y sin participantes. Ningún estudio reporta una evaluación integrada en el ciclo de construcción del software (integración continua).

La distribución es heterogénea según el tipo de estudio. Los 7 estudios con evaluación solo automática son cuantitativos. La evaluación solo con personas se reparte entre 12 estudios cuantitativos y 13 mixtos, y la semiautomática entre 5 cuantitativos y 6 mixtos. La diferencia coincide con el diseño de los estudios: las evaluaciones técnicas sobre corpus o simulaciones, sin muestra de participantes, solo aparecen en estudios cuantitativos.

**Integración de los resultados cuantitativos y cualitativos de la RQ3.** Los estudios cualitativos (marco normativo e instrumentos) y los cuantitativos (cobertura y automatización) solo coinciden en los 19 estudios mixtos, que registran los cuatro ítems; la métrica principal, registrada en los 73, enlaza ambos grupos. En la vertiente cuantitativa, la evaluación con personas predomina en los mixtos: 13 de los 19 evalúan solo con personas, 6 de forma semiautomática y ninguno solo de forma automática. 16 de los 19 cubren solo dimensiones cognitivas. En la vertiente cualitativa, 13 de los 19 no se adscriben a ningún marco normativo de accesibilidad, ninguno aplica COGA y 11 de esos 13 evalúan solo dimensiones cognitivas. Los instrumentos que identifican los estudios cualitativos y mixtos, sobre todo el estudio con usuarios y el cuestionario, coinciden con el predominio cuantitativo de la validación con personas. La métrica principal muestra la misma división: las métricas de rendimiento del modelo se concentran en la evaluación solo automática (5 de 7) y en la semiautomática (6 de 11), y no aparecen en ninguno de los 25 estudios que evalúan solo con personas. En estos últimos, la métrica principal es la usabilidad, el desempeño de las personas usuarias o la validez del instrumento cuando se especifica, y no se especifica en 17 de ellos.
<!-- fin -->

## Decisiones

- **Recodificación hecha (`codificacion/RQ3-I5.jsonl`): las 43 filas se cotejaron en el MD; 23 llevan `auto: false` y `evidencia`, y en 19 cambia la categoría.**
  - **Los «sin_participantes» del plan.** En la base de 43, `matriz.json` marca como «sin_participantes» a R208, R285, R396, R457, R626 y R643. Cuatro estaban como «Solo validación con usuarios» (el plan hablaba de 5). El MD no confirma el «sin_participantes» en tres de ellos.
    - **R208 → Semiautomática.** Usa Flesch y una «message testing with five adults with IDD».
    - **R396 se queda en «Solo validación».** Hay una «experimental comparison involving eight participants» con NASA-TLX.
    - **R626 se queda en «Solo validación».** Hay una encuesta a visitantes.
    - **R643 → Semiautomática.** Usa el F1 sobre un corpus y «when evaluated by a linguistic expert».
    - R285 y R457 estaban como NR y pasan a «Automática».
  - **Ampliación a las 43 filas.** «Solo validación con usuarios» tenía un valor bruto idéntico en 32 de 43 filas, el mismo sesgo de plantilla que en RQ3-B3. Busqué en cada MD métricas automáticas con valor (*accuracy*, F1, BLEU, SARI, WER, Flesch, Lighthouse, WhoCanUse, simulación, *continuous integration*, *unit test*) y participantes con número, y leí los contextos.
    - **A Semiautomática.** R246, R263, R300, R527, R627 y R831 (venían de «Solo validación»), y R504 (venía de NR).
    - **A Automática.** R040, que venía de «Solo validación»: sus 10 participantes son de un trabajo citado. También R016, R473, R538 y R595, que venían de NR.
    - **A Solo validación.** R106 y R587 venían de «Semiautomática»: lo semiautomático es la herramienta (ATECA, FACILE) y no la evaluación, que se hace por cuestionario. R721 venía de NR y tiene una evaluación cualitativa guiada por un experto.
  - **Categoría añadida: «Automática».** El formulario no la prevé («integración continua, semiautomática, solo validación con usuarios, NR»), pero 7 estudios evalúan solo con métricas o simulación. Codificarlos como NR perdería el dato, y como «Semiautomática» contradiría la definición. La definición está en `codebook.md` (`## RQ3-I5`). Nadie reporta integración continua: no hay ningún término de CI/CD ni de pruebas unitarias en los 43 MD. Por eso la categoría no se tabula y el texto la menciona en una frase.
  - **«Solo validación con usuarios»** incluye la valoración de expertos, como R376 y R721. Lo indica el texto («usuarios con la condición, cuidadores o expertos»).
- **Frase sobre la fase principal: no se incluye.** `tablas/RQ3-B4.json` no cruza RQ3-I5 con la fase principal (RQ2-I3), así que cualquier cifra quedaría fuera de la tabla. El cruce se eliminó en el plan.
- **Integración.** Los recuentos de la integración salen de intersecar las listas `estudios` de las tablas de RQ3-B1 a RQ3-B4 con los 19 mixtos de `matriz.json` (`naturaleza: mixto`), como en RQ1-B1. Los resultados son estos:
  - **Entre los 19 mixtos.** 13 evalúan solo con personas, 6 de forma semiautomática y 0 solo automática. 16 tienen cobertura cognitiva y 3 cubren ambas dimensiones. 13 no tienen marco normativo, y 11 de esos 13 tienen cobertura cognitiva. COGA tiene 0.
  - **Rendimiento del modelo** (exactitud, precisión/exhaustividad/F1 y SARI). Aparece en 5 de las 7 evaluaciones automáticas, en 6 de las 11 semiautomáticas y en 0 de las 25 que evalúan solo con personas.
  - **Constructo NR.** Hay 17 entre las 25 evaluaciones solo con personas.

  Estos recuentos van sin porcentaje, porque 19 no es la base de ninguna tabla y `sintesis:lint` exigiría que el porcentaje cuadrara con una base. Si el orquestador prefiere que la integración tenga su propia tabla, se puede declarar un cruce en una R2.
- **Presentación:** texto, como se acordó (tres categorías con datos y ningún NR tras la verificación).
- **Límite.** La automatización se decidió por términos y contextos, no leyendo cada MD completo. El caso más dudoso es R040: si su evaluación incluyera un estudio propio con usuarios, pasaría de «Automática» a «Semiautomática» (6 y 12).
