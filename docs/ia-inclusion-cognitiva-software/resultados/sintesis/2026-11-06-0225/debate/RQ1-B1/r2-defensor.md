# RQ1-B1 — Ronda 2 — Defensor

Acepto las seis objeciones. La más importante es la 1: mi cotejo de la R1 cortaba las referencias con una expresión regular que no detectaba los encabezados «References» de los PDF a dos columnas, así que contaba como cuerpo lo que eran referencias. Rehice el cotejo y apliqué además la segunda condición de la regla: que el perfil se refiera a la población destinataria o a los participantes. Cambian casi todas las cifras.

## Respuesta punto por punto

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | 22 asignaciones solo en referencias | **Acepto, y amplío.** Corregí la detección de referencias (encabezado «References» seguido de texto de la otra columna; corte manual en R581 y R605) y confirmé las asignaciones que señala el crítico: su tabla enumera 21 distintas. Después leí en contexto las 56 asignaciones con 5 o menos menciones en el cuerpo. Quito además 33 que están en el cuerpo pero no se refieren a la población: aparecen en trabajos relacionados, en el nombre de otra herramienta, en una definición, en la motivación, en limitaciones o en trabajo futuro, y hay un falso positivo («tea» en R317). En total quito 54 asignaciones en 35 filas | La regla queda escrita en `codebook.md` (`## RQ1-I1`). En las 35 filas cambiadas, `evidencia` da la línea del MD de cada categoría que se mantiene y el motivo de cada una que se quita, con `auto: false`. Se volvió a correr `sintesis:aggregate`. Resultado: TEA 20, DI 18, discapacidad cognitiva 13, TDAH 12, dificultades de aprendizaje 11, dislexia 9 y síndrome de Down 4. Dos o más perfiles: 23 de 49 (47%) |
| 2 | R527 debe ir a «Sin perfil específico» | **Acepto.** El cuerpo solo dice «neurodiverse students» | R527 pasa a «Sin perfil específico» (n=1). El texto lo menciona en una frase y la figura no lo dibuja (`excluidas` en el spec). El codebook avisa de que RQ2-B2 debe excluir esa fila de la matriz |
| 3 | En R106, el TEA cita a los adaptadores; falta TDA | **Acepto.** Uso la regla de los subgrupos de participantes: se codifican todos los que nombra la composición de la muestra | La evidencia de R106 cita ahora la composición de los participantes («TEA (3%) y Trastorno por Déficit de Atención (TDA) (2%)»), no la de los adaptadores, y se añade TDAH, cuya definición en el codebook incluye TDA. R106 queda con TEA, DI, discapacidad cognitiva y TDAH |
| 4 | «Todos describen a su población como neurodivergente» presenta un sesgo como hallazgo | **Acepto** | Uso la frase que propone el crítico: la etiqueta figura en todos los registros y no distingue entre estudios |
| 5 | La *Nota.* de la figura dice 73 y no aclara que los porcentajes no suman 100% | **Acepto** | Nueva *Nota.*: base de 49 de los 73 y aclaración de que un estudio puede declarar más de un perfil |
| 6 | El párrafo de homogeneidad va dentro de la Detalle gráfica y se apoya solo en el puesto de cada perfil | **Acepto** | El párrafo pasa antes de **Figura {{F1}}** y se recalcula con `por_naturaleza`, con la proporción dentro de cada grupo. La mayor diferencia es la de dislexia: 7% (2 de 30) en los cualitativos frente al 37% (7 de 19) en los mixtos. Por eso ahora digo que el resultado es heterogéneo en ese perfil |

## Texto propuesto

<!-- inicio -->
### 3.2. Perfiles de discapacidad cognitiva o neurodivergencia abordados (RQ1)

El ítem de perfiles se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos). La etiqueta general de neurodivergencia figura en todos los registros y no distingue entre estudios; por eso, la síntesis se hace sobre los perfiles específicos que declara cada uno para su población destinataria o para sus participantes. Como se observa en la Figura {{F1}}, el 41% (n=20) declara el trastorno del espectro autista (TEA) y el 37% (n=18), la discapacidad intelectual (DI). El 27% (n=13) usa el término genérico de discapacidad cognitiva, el 24% (n=12) menciona el trastorno por déficit de atención con hiperactividad (TDAH) y el 22% (n=11), dificultades de aprendizaje distintas de la dislexia o sin especificar. La dislexia se declara en el 18% (n=9) y el síndrome de Down en el 8% (n=4). Un estudio (2%) describe a su población solo como neurodivergente, sin un perfil específico. El 47% (n=23) de los estudios declara dos o más perfiles.

Los resultados son homogéneos entre los estudios cualitativos y los mixtos en la mayoría de los perfiles, con diferencias de hasta 13 puntos porcentuales, y heterogéneos en la dislexia. Esta se declara en el 7% (2 de 30) de los estudios cualitativos y en el 37% (7 de 19) de los mixtos. La diferencia coincide con la naturaleza del estudio: la dislexia se aborda sobre todo en estudios que combinan datos cuantitativos y cualitativos. En los cualitativos, la DI es el perfil más declarado (40%, 12 de 30); en los mixtos, el TEA (47%, 9 de 19). Los 24 estudios cuantitativos no registran este ítem, porque el formulario solo lo recoge en la hoja cualitativa.

**Figura {{F1}}**

*Perfiles de discapacidad cognitiva o neurodivergencia declarados en los estudios*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 49 estudios cualitativos o mixtos de los 73 seleccionados (2021–2027). Un estudio puede declarar más de un perfil, por lo que los porcentajes no suman 100%.

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** barras horizontales.
- **Por qué este tipo:** siete categorías nominales de un ítem multivalor con etiquetas largas; las barras horizontales ordenadas por n comparan los perfiles específicos.
- **Qué muestra:** el porcentaje de los 49 estudios cualitativos o mixtos que declara cada perfil específico.
- **Datos a dibujar:** TEA, n=20, 41%; DI, n=18, 37%; discapacidad cognitiva (término genérico), n=13, 27%; TDAH, n=12, 24%; dificultades de aprendizaje, n=11, 22%; dislexia, n=9, 18%; síndrome de Down, n=4, 8%. «Sin perfil específico» (n=1, 2%) no se dibuja.
- **Ejes:** Y, perfil declarado en orden descendente por n (TEA arriba); X, porcentaje de estudios, escala lineal de 0 a 100%.
- **Etiquetas sobre los datos:** `X% (n=Y)` al final de cada barra, p. ej. «41% (n=20)».
- **Leyenda:** sin leyenda (una sola serie).
- **Título interno del gráfico:** ninguno; el título es el de la figura.
- **Nota del gráfico:** «Los porcentajes no suman 100%: un estudio puede declarar más de un perfil (base n = 49 estudios cualitativos o mixtos)».
- **Estilo:** azules sobrios en un solo tono, orden descendente por n, 16 × 9 cm.
<!-- fin -->

## Decisiones

- **Recodificación R2 (`codificacion/RQ1-I1.jsonl`):** 35 filas cambiadas, todas con `auto: false` y `evidencia` por categoría. Se quitan 54 asignaciones y se añade una (TDAH en R106). Las 49 filas siguen con `auto: false` desde la R1, porque en la R1 se quitó la etiqueta «Neurodivergencia».
  - Señaladas por el crítico (21; solo en referencias o, en R193, con otro término): R145 (TEA, dislexia, dificultades de aprendizaje), R147 (TDAH), R193 (DI y discapacidad cognitiva), R197 (TEA, dificultades de aprendizaje), R208 (dificultades de aprendizaje), R317 (síndrome de Down), R356 (TEA, síndrome de Down), R360 (TEA), R398 (dificultades de aprendizaje), R399 (TEA, dificultades de aprendizaje), R527 (dificultades de aprendizaje), R600 (dificultades de aprendizaje), R705 (síndrome de Down), R713 (dificultades de aprendizaje) y R831 (dificultades de aprendizaje).
  - En el cuerpo, pero no referidas a la población (33): trabajos relacionados, otra herramienta, definición, motivación, limitación o trabajo futuro, en R187, R197, R199, R219, R264, R293, R317, R327, R347, R360, R391, R393, R394, R425, R495, R549, R587, R605, R623, R626, R627, R705 y R880. El motivo de cada una está en la `evidencia` de la fila.
- **Cifras:** todas salen de `tablas/RQ1-B1.json` (base 49). El «47% (n=23)» se obtiene contando, para cada estudio, en cuántas listas `estudios` de esa tabla aparece: 23 de 49 en dos o más. Las proporciones por grupo salen de `por_naturaleza`, sobre bases de 30 y 19.
- **Estabilidad para RQ2-B2:** RQ1-I1 queda cerrado con la regla del codebook. RQ2-B2 tiene que volver a correr `sintesis:aggregate` y excluir «Sin perfil específico» de la matriz, que queda en 7 filas de perfil.
- **Límite:** la segunda condición de la regla (que el perfil se refiera a la población) la apliqué leyendo en contexto las asignaciones con 5 o menos menciones en el cuerpo. Las que tienen más menciones las doy por referidas a la población, y en las que revisé al azar (R187, R393, R600, R831 y R880) lo están.
