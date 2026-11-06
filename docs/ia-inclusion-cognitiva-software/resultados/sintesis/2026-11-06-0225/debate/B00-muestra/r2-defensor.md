# B00-muestra — Ronda 2 — Defensor

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | Sesgo del registro verificado en el MD; recodificar en `tablas/B00-muestra.json` (con participantes 53, sin participantes 14, NR 3, no humana 3; mediana 12) y verificar los otros 10 rótulos «Revisión bibliográfica» | **Acepto el diagnóstico y justifico no recodificar aquí.** (a) La instrucción del orquestador para esta síntesis es explícita: «Los B00 no se recodifican (salen del Excel)… no lo cambies: decláralo». (b) La §8 del playbook regula la recodificación de ítems vía `codificacion/<ítem>.jsonl`, y B00 no tiene ese archivo. `tablas/B00-muestra.json` lo escribe `sintesis:general` desde `matriz.json` (fila 13 del formulario), así que una edición a mano se perdería al regenerar y rompería la traza Excel → tabla. (c) Hice la verificación pedida (ver abajo): las discrepancias son 7, no 5, y en dos casos el n no se puede fijar desde el MD. Por eso las cifras «corregidas» del crítico (53/14/3/3, mediana 12) tampoco serían las definitivas | El texto mantiene las cifras de la tabla y **declara la discrepancia** de forma neutra: «En al menos siete estudios, el tamaño de muestra registrado en el formulario de extracción no coincide con el declarado en el texto completo…». La lista verificada pasa al orquestador como corrección de la fila 13 del formulario en una nueva versión, seguida de `sintesis:general` |
| 2 | Retirar la oración «13 figuran … como revisión bibliográfica…»: es un rótulo del proceso, choca con el CE de estudios secundarios y es falso en varios casos | Acepto | Se retira la oración. No se caracteriza a los estudios sin participantes con categorías que la tabla no agrega |
| 3 | «muestra no humana, compuesta por respuestas generadas, textos o sesiones»: solo el registro de 240 respuestas generadas respalda esa unidad | Acepto. Verificado en el MD: R595 (55) dice «we asked an in-house human annotator to…», así que n=1 sería una persona anotadora, no una muestra de participantes. En R663 (65), el único recuento del MD es «N = 10+13+14+6+15+15+12 = 85» problemas de aprendizaje, y no confirma la unidad de «n = 10». Ninguno de los dos registros trae unidad. No los paso a «No reportado», porque eso sería recodificar un B00 (ver #1) | La frase deja de atribuir unidades: «el 4% (n=3) registra un tamaño de muestra cuya unidad no son participantes humanos o no se especifica». Ambos registros se suman a la lista de corrección del formulario |

### Verificación en el MD (para el orquestador; no entra en el texto)

| si_order | Id | Registro actual (categoría de la tabla) | Evidencia en el MD | Corrección propuesta al formulario |
|---|---|---|---|---|
| 14 | R208 | Revisión bibliográfica (sin participantes) | «message testing with five adults with intellectual and developmental disabilities» | Participantes, n = 5 |
| 38 | R396 | Revisión bibliográfica (sin participantes) | «experimental comparison involving eight participants (aged 20–45)» | Participantes, n = 8 |
| 26 | R327 | Revisión bibliográfica (sin participantes) | «In total, 9 experts by lived experience and 3 health care professionals…»; «6 experts by lived experience engaged with think-aloud interviews» | Participantes; n a fijar por el extractor (12 o 6, según la fase) |
| 60 | R626 | Revisión bibliográfica (sin participantes) | Encuesta: «the respondents were asked…»; «more than 1300 people interviewed» (sin cifra exacta localizada) | Participantes; n exacto a confirmar en el PDF (si es > 1 536, cambia el máximo del rango) |
| 64 | R647 | Revisión bibliográfica (sin participantes) | Talleres de codiseño «with the parents», «with experts, parents, and designers», sin n | No reportado |
| 19 | R263 | «n = 000 participantes» (no reportado) | «No human participants or animals were involved in this study» | Sin participantes humanos |
| 44 | R453 | Ensayo conceptual (no reportado) | `muestra_raw`: «sin estudio empírico con n» | Sin participantes humanos |
| 55 | R595 | «n = 1» (muestra no humana) | «an in-house human annotator» | Unidad a precisar (anotador, no participante) |
| 65 | R663 | «n = 10» (muestra no humana) | Solo «N = … = 85» problemas de aprendizaje; unidad de n = 10 no localizada | No reportado, salvo que el PDF confirme la unidad |

Los otros 6 rótulos «Revisión bibliográfica» se confirman como **sin participantes humanos**, o sin un n localizable en el MD:
- R219 (15): «conceptual design process without direct participant».
- R285 (21): etiquetas asignadas por anotadores a un corpus de publicaciones; evaluación sobre texto.
- R399 (40): «While a full user evaluation…» (no la realiza).
- R457 (45): «synthetic simulation-based evaluation (500 simulated profiles, no real user evaluation)».
- R193 (10), R264 (20), R337 (27) y R1061 (73): no se localiza ningún recuento de participantes. R193 incluye extractos de interacción y R1061 menciona sesiones de codiseño, sin n. Se mantienen como están, con revisión manual recomendada.

Las 7 discrepancias que el texto declara («al menos siete») son R208, R396, R327, R626, R647, R263 y R453; las 7 cambian de categoría. R595 y R663 no cuentan porque su categoría no está demostrada como errónea, solo su unidad.

## Texto propuesto

<!-- inicio -->
### 3.5. Tamaño de las muestras

Del total de 73 artículos seleccionados, el 70% (n=51) reporta el número de participantes humanos, el 21% (n=15) no incluye participantes humanos, el 5% (n=4) no reporta el tamaño de la muestra y el 4% (n=3) registra un tamaño de muestra cuya unidad no son participantes humanos o no se especifica. En los 51 estudios con participantes humanos, el tamaño de las muestras osciló entre 1 y 1 536 participantes, con una mediana de 14 participantes. En al menos siete estudios, el tamaño de muestra registrado en el formulario de extracción no coincide con el declarado en el texto completo; las cifras se presentan tal como figuran en el formulario.
<!-- fin -->

## Decisiones

- **Cifras:** solo de `tablas/B00-muestra.json` (51/15/4/3; rango 1–1 536; mediana 14; N = 73). No se edita la tabla, el Excel ni `matriz.json`.
- **Declaración de la discrepancia:** el bloque se presenta en texto (`bloques.json`), así que no hay *Nota.* y la declaración va en la última oración. Es un hecho verificable y no una interpretación: no dice en qué dirección cambiarían las cifras.
- **Escalado al orquestador:** si autoriza corregir la fila 13 del formulario con la tabla de verificación y regenerar con `sintesis:general`, el texto se rehace con las cifras nuevas y la última oración se retira. Si no lo autoriza, se mantiene esta versión. En ambos casos, no se publican en Resultados cifras corregidas a mano que no salgan de la tabla.
- **Heterogeneidad del tamaño:** no se añade el desglose por tramos, porque no está en la tabla. Se puede incorporar si se regenera la tabla.
