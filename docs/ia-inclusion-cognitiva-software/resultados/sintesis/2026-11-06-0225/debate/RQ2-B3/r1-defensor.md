# RQ2-B3 — Ronda 1 — Defensor

El plan exigía verificar el rol por estudio antes de publicar porcentajes, y la verificación refuta el registro. La plantilla «Generador; evaluador; asistente de aseguramiento de la calidad», copiada en 44 de 49 filas, daba Evaluador 100%, Asistente de AC 96% y Generador 92%. En el texto completo, la IA evalúa en 4 estudios y asiste al aseguramiento de la calidad en 3. Propongo texto con seis categorías y los siete NR aparte.

## Texto propuesto

<!-- inicio -->
### 3.?. Rol de la inteligencia artificial en el desarrollo y la evaluación del software (RQ2)

El rol de la IA se registró en los 49 estudios con enfoque cualitativo o mixto (30 cualitativos y 19 mixtos) y se codificó a partir del texto completo de cada uno, según lo que la IA produce, reconoce, adapta o juzga en el software que el estudio desarrolla, evalúa o analiza. El 61% (n=30) emplea la IA como generadora de contenido o de salidas del artefacto: textos simplificados o reescritos, respuestas conversacionales, imágenes, pictogramas, recomendaciones o interfaces. El 29% (n=14) la emplea como intérprete de la entrada o del estado del usuario, es decir, para reconocer su voz, sus gestos, sus expresiones o indicadores de su condición. El 10% (n=5) reporta la IA como personalizadora en ejecución, que adapta el artefacto o el contenido al perfil o a la conducta del usuario mientras lo usa.

Los roles vinculados a la calidad del software son menos frecuentes. El 8% (n=4) emplea la IA como evaluadora de la accesibilidad, la legibilidad o la calidad del contenido o del código, y el 6% (n=3) como asistente de aseguramiento de la calidad, que genera datos de prueba o criterios de evaluación o propone correcciones que revisa una persona. En conjunto, ambos roles se identifican en el 10% (n=5) de los estudios, y dos de ellos reportan los dos. Otro 6% (n=3) usa la IA para analizar los datos de la propia investigación, no dentro del artefacto. El 14% (n=7) no aplica ninguna técnica de IA y no tiene rol. El 31% (n=15) asigna a la IA dos o más roles; la combinación más frecuente es la de generador e intérprete. De los 24 estudios que emplean LLM, 22 los usan como generadores.

Los resultados son heterogéneos en el rol de intérprete, que se reporta en el 20% (6 de 30) de los estudios cualitativos y en el 42% (8 de 19) de los mixtos. Los demás roles presentan diferencias menores: el de generador aparece en el 67% (20 de 30) de los cualitativos y en el 53% (10 de 19) de los mixtos, y el de personalizador en el 3% (1 de 30) y el 21% (4 de 19), respectivamente. Los 24 estudios cuantitativos no registran este ítem, porque el formulario solo lo recoge en la hoja cualitativa.
<!-- fin -->

## Decisiones

- **Verificación hecha en los 49 MD**, según el `plan_recodificacion`. Para cada estudio leí los contextos de la técnica de IA ya verificada en RQ2-I1 y codifiqué qué produce la IA, qué reconoce, qué adapta y qué juzga.
- **`codificacion/RQ2-I2.jsonl`: 49 de 49 filas con `auto: false` y `evidencia`.** Las categorías y las reglas están en `codebook.md` (`## RQ2-I2`). Las tres nuevas, «Intérprete de la entrada o del estado del usuario», «Personalizador en ejecución» y «Análisis de datos de la investigación», concretan el «otro» que el formulario preveía.
  - **Evaluador (4).** R106 (detecta incumplimientos de las pautas de Lectura Fácil), R495 (LLM que revisan el código de la app en busca de problemas de accesibilidad), R549 (identificación de palabras complejas) y R587 (análisis de pautas de Lectura Fácil).
  - **Asistente de AC (3).** R106 (frases de prueba generadas con ChatGPT, l. 783), R337 (heurísticas generadas con GenAI y validadas por los autores, l. 510 y l. 811) y R495 (una persona revisa la salida de cada LLM, l. 991).
  - **Análisis de datos (3).** R203 (GPT-4o en el análisis de datos), R403 (PLN sobre la comunidad en línea) y R693 (análisis sintáctico de un corpus).
  - **NR (7).** Son los mismos 7 estudios sin técnica de IA de RQ2-I1: R197, R199, R219, R425, R600, R713 y R1061.
- **Cifras** (todas de `tablas/RQ2-B3.json`, base 49): Generador 30, Intérprete 14, Personalizador 5, Evaluador 4, Asistente de AC 3, Análisis de datos 3 y NR 7.
  - Evaluador ∪ AC = 5 y Evaluador ∩ AC = 2 (R106 y R495) salen de las listas `estudios`.
  - «Dos o más roles» (n=15) sale de contar los roles de cada estudio en esas listas: 13 tienen dos y 2 tienen tres. La combinación generador e intérprete es la más frecuente: aparece en 7 estudios (R293, R393, R453, R504, R583, R705 y R831). Le siguen generador y evaluador, y generador y personalizador, con 3 cada una.
  - «22 de los 24 con LLM» es la intersección de la lista LLM de `tablas/RQ2-B1.json` con la lista Generador de esta tabla.
- **Heterogeneidad.** Con el umbral común de 20 puntos, solo el intérprete lo supera (22 puntos: 20% frente a 42%). El personalizador queda en 18 y el generador en 14. Doy las cifras sin atribuirles causa.
- **Presentación:** texto, como se acordó. Son seis categorías con descripción, y cada una cabe en una frase con X% (n=Y). Ya no se publican los porcentajes saturados (100%, 96% y 92%), y la *Nota.* sobre la limitación del registro deja de hacer falta porque el rol sí se verificó. La plantilla descartada se documenta en el codebook, no en la prosa de Resultados.
- **Límite.** Varios estudios combinan roles y la frontera entre «Evaluador» y «Asistente de AC» depende de quién decide. Si la IA emite el juicio, es evaluadora; si apoya a una persona que verifica, es asistente. R495 reúne ambos. Si el crítico prefiere fusionar las dos categorías en «Calidad del software», la cifra combinada (n=5, 10%) ya está en el texto.
