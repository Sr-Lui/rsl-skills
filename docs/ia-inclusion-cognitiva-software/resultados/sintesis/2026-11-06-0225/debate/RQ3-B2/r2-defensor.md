# RQ3-B2 — Ronda 2 — Defensor

Respuesta punto por punto a `r1-critico.md`. Acepto las cinco objeciones. `tablas/RQ3-B2.json` se regeneró con base n = 49.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | R399: los *checkpoints* de legibilidad son una función del artefacto y el estudio con usuarios solo está previsto | **Acepto** | R399 → NR, con la evidencia «A user-in-the-loop study is planned» |
| 2 | R393: la fórmula de legibilidad se aplica una sola vez, en la discusión. El criterio no coincide con el de RQ3-B1 | **Acepto** | Se quita «Índice de legibilidad» de R393 y se conserva «Estudio con usuarios». El índice queda en n=1 (R208) y el texto lo reporta como «Únicamente 1 estudio (2%)» |
| 3 | R208 tiene personas en RQ3-I5 pero no en este ítem | **Acepto** | R208 → `['Estudio con usuarios', 'Índice de legibilidad']` |
| 4 | De los 9 NR, 5 no se verificaron (R106, R403, R627, R647 y R663) | **Acepto** | Los cinco se verificaron en el MD. R106 → `['Cuestionario', 'Estudio con usuarios']`, por el test de comprensión de las adaptaciones aplicado a 164 personas. R627 → `['Estudio con usuarios']`, por la intervención con 1536 participantes. R647 → `['Estudio con usuarios']`, por sus dos talleres de codiseño con la participante y su familia (el mismo criterio que R356). R403 queda en NR (análisis de redes sociales de una comunidad en línea) y R663 también (formalización del modelo DIAUTIS, cuya escala Likert pondera el modelo). Ahora hay 7 NR y todos tienen `evidencia` |
| 5 | Las 11 filas a las que se quitó «Legibilidad» no tienen `evidencia` | **Acepto** | Las 11 filas (R145, R197, R293, R337, R495, R549, R581, R587, R626, R693 y R713) llevan ahora «sin fórmula ni índice de legibilidad en el cuerpo; la legibilidad aparece solo como criterio de diseño, tema de entrevista o en las referencias» |

## Texto propuesto

<!-- inicio -->
### 3.?. Instrumentos y protocolos de medición (RQ3)

El ítem de instrumentos se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos). El estudio con usuarios es el protocolo más reportado: el 76% (n=37) evalúa o diseña el artefacto con personas que lo usan, lo prueban o lo valoran en sesiones, tareas, entrevistas, talleres de codiseño u observación. El 57% (n=28) emplea cuestionarios, entre ellos escalas Likert y escalas estandarizadas como la SUS. El 16% (n=8) aplica una inspección heurística por expertos. Únicamente 1 estudio (2%) calcula un índice de legibilidad sobre el texto que produce el artefacto. El 14% (n=7) no reporta una evaluación con instrumento ni con usuarios. Un estudio puede emplear más de un instrumento, de modo que los porcentajes no suman 100%.

Los resultados son heterogéneos según el tipo de estudio. El cuestionario aparece en 17 de los 19 estudios mixtos y en 11 de los 30 cualitativos. El estudio con usuarios se reporta en 21 estudios cualitativos y 16 mixtos, y la inspección heurística en 6 cualitativos y 2 mixtos. La diferencia en el uso del cuestionario coincide con el diseño de los estudios mixtos, que añaden una medida cuantitativa a la evaluación con usuarios.
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ3-I2.jsonl`).** En la R2 se modificaron 19 filas: las 3 de las objeciones 1 a 3, las 5 NR de la objeción 4 y las 11 de la objeción 5. En total, 28 de 49 filas llevan `auto: false` y `evidencia`.
  - Las 21 filas restantes conservan el valor del registro (`auto: true`). En ellas el cotejo por términos de la R1 encontró apoyo para cada categoría. El codebook lo declara (`## RQ3-I2`, reescrita).
- **Cifras:** todas salen de `tablas/RQ3-B2.json`.
  - **Categorías:** estudio con usuarios 37 (76%), cuestionario 28 (57%), heurística 8 (16%), índice de legibilidad 1 (2%) y NR 7 (14%).
  - **Por tipo de estudio (`por_naturaleza`):** el cuestionario está en 17 mixtos y 11 cualitativos. El estudio con usuarios está en 21 cualitativos y 16 mixtos.
- **Texto:** «evalúa o diseña» recoge que R356 y R647 cuentan como estudio con usuarios por talleres de codiseño, según la definición del codebook. Si el crítico prefiere limitar la categoría a la evaluación, salen esas 2 filas. R356 tiene, además, métricas calculadas en RQ3-I1.
- **Presentación:** texto con X% (n=Y), sin cambios.
