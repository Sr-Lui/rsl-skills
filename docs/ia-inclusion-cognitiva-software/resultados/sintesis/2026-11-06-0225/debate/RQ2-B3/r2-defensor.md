# RQ2-B3 — Ronda 2 — Defensor

Acepto las seis objeciones. Verifiqué R495 en el MD: los LLM reciben capturas de pantalla, no código. Recodifiqué `codificacion/RQ2-I2.jsonl` (R453 → NR; R495 → solo Asistente de AC; «Evaluador» → «Evaluador del contenido» en R106, R549 y R587) y volví a correr `sintesis:aggregate RQ2-B3`. El codebook (`## RQ2-I2`) recoge la nueva definición y los tres niveles.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | «Evaluador» mezcla la función del artefacto con la evaluación del software; ningún estudio evalúa código | **Acepto.** Las l. 289–293 de R495 lo dicen expresamente: el código lo recibían los LLM del trabajo citado, y en R495 se les dieron imágenes | Categoría «Evaluador del contenido»: la IA juzga la legibilidad o la accesibilidad del texto que procesa el artefacto. Se retiran «o del código» y «vinculados a la calidad del software». Evidencia de R495 corregida |
| 2 | R495 contado dos veces | **Acepto.** Por la regla de R1, si una persona verifica a partir del juicio de la IA, el rol es asistente; y R495 se presenta como ayuda («help humans to locate new issues», l. 296) | R495 queda solo en Asistente de AC. Evaluador del contenido = 3 (R106, R549, R587), Asistente de AC = 3 (R106, R337, R495); unión 5 e intersección 1 |
| 3 | El encuadre contradice el ítem (proceso frente a producto) | **Acepto.** El título del bloque viene de `bloques.json` y no lo cambio | La apertura separa tres niveles con sus uniones: componente del artefacto (n=37), proceso de desarrollo o evaluación (Asistente de AC, n=3) y procedimiento de investigación (n=3). Después va el detalle. Las uniones se documentan en Decisiones |
| 4 | R453 es conceptual | **Acepto** (cascada de RQ2-B1) | NR. Generador 29 (59%), Intérprete 13 (27%), NR 8 (16%), generador e intérprete 6, dos o más roles 13 (no 14; ver Decisiones), 21 de los 23 con LLM |
| 5 | Fórmula de NR | **Acepto** | «El 16% (n=8) no reporta una técnica de IA aplicada, por lo que no se le asigna un rol» |
| 6 | «Diferencias menores» sin umbral | **Acepto** | Fórmula de RQ1-B1: «homogéneos …, con diferencias de hasta 18 puntos porcentuales» |

## Texto propuesto

<!-- inicio -->
### 3.?. Rol de la inteligencia artificial en el desarrollo y la evaluación del software (RQ2)

El rol de la IA se registró en los 49 estudios con enfoque cualitativo o mixto (30 cualitativos y 19 mixtos) y se codificó a partir del texto completo de cada uno. Los roles se agrupan en tres niveles. En el 76% (n=37), la IA es un componente del artefacto: genera, interpreta, personaliza o evalúa contenido mientras el software se usa. En el 6% (n=3), la IA interviene en el proceso de desarrollo o evaluación del software como asistente de aseguramiento de la calidad. En otro 6% (n=3), se usa en el procedimiento de la investigación para analizar los datos del estudio. El 16% (n=8) no reporta una técnica de IA aplicada, por lo que no se le asigna un rol.

Dentro del artefacto, el 59% (n=29) emplea la IA como generadora de contenido o de salidas: textos simplificados o reescritos, respuestas conversacionales, imágenes, pictogramas, recomendaciones o interfaces. El 27% (n=13) la emplea como intérprete de la entrada o del estado del usuario, es decir, para reconocer su voz, sus gestos, sus expresiones o indicadores de su condición. El 10% (n=5) reporta la IA como personalizadora en ejecución, que adapta el artefacto o el contenido al perfil o a la conducta del usuario mientras lo usa. El 6% (n=3) la emplea como evaluadora del contenido, que juzga la legibilidad o el cumplimiento de pautas de Lectura Fácil del texto que procesa la herramienta.

En el proceso de desarrollo o evaluación, la IA genera datos de prueba o criterios de evaluación, o señala problemas de la interfaz que después revisa una persona. Un estudio emplea la IA a la vez como evaluadora del contenido y como asistente de aseguramiento de la calidad. El 27% (n=13) asigna a la IA dos o más roles, y la combinación más frecuente es la de generador e intérprete (n=6). De los 23 estudios que emplean LLM, 21 los usan como generadores.

Los resultados son heterogéneos en el rol de intérprete, que se reporta en el 17% (5 de 30) de los estudios cualitativos y en el 42% (8 de 19) de los mixtos. Los demás roles son homogéneos entre ambos grupos, con diferencias de hasta 18 puntos porcentuales: el de generador aparece en el 63% (19 de 30) de los cualitativos y en el 53% (10 de 19) de los mixtos, y el de personalizador en el 3% (1 de 30) y el 21% (4 de 19), respectivamente. Los 24 estudios cuantitativos no registran este ítem, porque el formulario solo lo recoge en la hoja cualitativa.
<!-- fin -->

## Decisiones

- **Recodificación R2** (`codificacion/RQ2-I2.jsonl`, `auto: false`, evidencia «(R2)»):
  - R453 pasa a NR.
  - R495 queda solo como Asistente de AC. Evidencia: l. 289–293 («we provided images like human evaluators»), l. 296 y l. 991.
  - R106, R549 y R587 pasan de «Evaluador» a «Evaluador del contenido».
- **Cifras** (`tablas/RQ2-B3.json`, base 49): Generador 29, Intérprete 13, Personalizador 5, Evaluador del contenido 3, Asistente de AC 3, Análisis de datos 3 y NR 8.
- **Uniones**, derivadas de las listas `estudios` de la tabla:
  - Componente del artefacto = Generador ∪ Intérprete ∪ Personalizador ∪ Evaluador del contenido = **37**.
  - Proceso = Asistente de AC = **3**. Investigación = Análisis de datos = **3**.
  - Hay solapamiento: R106 (AC) y R203 (Análisis) también son componente. 37 + 2 + 2 + 8 = 49, porque 2 estudios solo son AC (R337 y R495) y 2 solo son Análisis (R403 y R693).
  - «Evaluador ∩ AC» = 1 (R106).
- **«Dos o más roles» = 13, no 14.** Además de R453, R495 pierde un rol: tenía Evaluador y AC y ahora solo AC. Quedan 11 estudios con dos roles y 2 con tres. Generador e intérprete = 6. «21 de 23» es la intersección de las listas LLM (`tablas/RQ2-B1.json`) y Generador.
- **Heterogeneidad** (umbral común de 20 puntos): Intérprete, 25 puntos. Personalizador 18, Generador 11, Evaluador del contenido 8, y AC y Análisis de datos 2 cada uno.
- **Presentación:** texto en tres párrafos de nivel más uno de heterogeneidad. Sigue sin publicarse la plantilla saturada (100%, 96% y 92%).
