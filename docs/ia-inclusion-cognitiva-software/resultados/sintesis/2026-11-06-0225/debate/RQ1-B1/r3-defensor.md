# RQ1-B1 — Ronda 3 (final) — Defensor

Acepto las cuatro objeciones. Para el n.º 4 hay un matiz que cambia la conclusión, aunque no la corrección: con la tabla regenerada, la dislexia queda en 6 de 19 estudios mixtos, no en 5. Su diferencia es de 25 puntos (7% frente a 32%), que supera el umbral de 20, así que el resultado sigue siendo heterogéneo en ese perfil. Quito, como pide el crítico, la frase que atribuía la diferencia a la naturaleza del estudio.

## Propuesta de consenso

| # | Objeción R2 | Propuesta de consenso |
|---|---|---|
| 1 | R425: el TDAH se apoya en una comorbilidad citada en los antecedentes | **Aceptada.** Se quita el TDAH de R425 y se mantienen el TEA y la dislexia, que figuran en las condiciones de los participantes (l. 584–585). La regla queda en el codebook: las comorbilidades citadas en los antecedentes no cuentan, y una misma frase no puede justificar un perfil y descartar otro |
| 2 | R623: la dislexia es un trabajo relacionado o una definición | **Aceptada.** Se quita la dislexia de R623 y se mantienen DI y DA (l. 374) |
| 3 | R705 (TEA) y R106 (DI) apoyados en líneas incorrectas | **Aceptada.** El TEA de R705 se apoya en la l. 623, el caso que se da a los participantes. La DI de R106 se apoya en la l. 704 («personas con discapacidad intelectual (79%)»). Las categorías no cambian, solo la `evidencia` |
| 4 | Con los cambios 1 y 2, el juicio sobre la dislexia deja de ser cierto; falta reordenar el empate | **Aceptada en la forma.** La tabla regenerada da dislexia n=8: 2 de 30 cualitativos y **6 de 19 mixtos**, porque R425 conserva la dislexia, como pide el propio crítico en el n.º 1. Eso es un 7% frente a un 32%, 25 puntos, por encima del umbral de 20, así que la dislexia sigue siendo el único perfil heterogéneo. Se quita «La diferencia coincide con la naturaleza del estudio…». El TDAH y la DA quedan empatados en n=11 (22%). Tabla, spec y texto actualizados |

## Texto propuesto

<!-- inicio -->
### 3.2. Perfiles de discapacidad cognitiva o neurodivergencia abordados (RQ1)

El ítem de perfiles se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos). La etiqueta general de neurodivergencia figura en todos los registros y no distingue entre estudios. Por eso, la síntesis se hace sobre los perfiles específicos que cada estudio declara para su población destinataria o para sus participantes. Como se observa en la Figura {{F1}}, el 41% (n=20) declara el trastorno del espectro autista (TEA) y el 37% (n=18), la discapacidad intelectual (DI). El 27% (n=13) usa el término genérico de discapacidad cognitiva. El trastorno por déficit de atención con hiperactividad (TDAH) y las dificultades de aprendizaje distintas de la dislexia o sin especificar se declaran cada uno en el 22% (n=11). La dislexia aparece en el 16% (n=8) y el síndrome de Down en el 8% (n=4). Un estudio (2%) describe a su población solo como neurodivergente, sin un perfil específico. El 47% (n=23) de los estudios declara dos o más perfiles.

Los resultados de los estudios cualitativos y mixtos son homogéneos en seis de los siete perfiles, con diferencias de hasta 13 puntos porcentuales. La excepción es la dislexia, en la que son heterogéneos: la declara el 7% (2 de 30) de los estudios cualitativos y el 32% (6 de 19) de los mixtos. La DI es el perfil más declarado en los cualitativos (40%, 12 de 30) y el TEA en los mixtos (47%, 9 de 19). Los 24 estudios cuantitativos no registran este ítem, porque el formulario solo lo recoge en la hoja cualitativa.

**Figura {{F1}}**

*Perfiles de discapacidad cognitiva o neurodivergencia declarados en los estudios*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 49 estudios cualitativos o mixtos de los 73 seleccionados (2021–2027). Un estudio puede declarar más de un perfil, por lo que los porcentajes no suman 100%.

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** barras horizontales.
- **Por qué este tipo:** siete categorías nominales de un ítem multivalor, con etiquetas largas; las barras horizontales ordenadas por n permiten comparar los perfiles específicos.
- **Qué muestra:** el porcentaje de los 49 estudios cualitativos o mixtos que declara cada perfil específico.
- **Datos a dibujar:** TEA, n=20, 41%; DI, n=18, 37%; discapacidad cognitiva (término genérico), n=13, 27%; TDAH, n=11, 22%; dificultades de aprendizaje, n=11, 22%; dislexia, n=8, 16%; síndrome de Down, n=4, 8%. «Sin perfil específico» (n=1, 2%) no se dibuja.
- **Ejes:** en el eje Y, el perfil declarado en orden descendente por n, con el TEA arriba; en el eje X, el porcentaje de estudios, en escala lineal de 0 a 100%.
- **Etiquetas sobre los datos:** `X% (n=Y)` al final de cada barra, p. ej. «41% (n=20)».
- **Leyenda:** sin leyenda (una sola serie).
- **Título interno del gráfico:** ninguno; el título es el de la figura.
- **Nota del gráfico:** «Los porcentajes no suman 100%: un estudio puede declarar más de un perfil (base n = 49 estudios cualitativos o mixtos)».
- **Estilo:** azules sobrios en un solo tono, orden descendente por n (el empate entre TDAH y dificultades de aprendizaje mantiene el orden de la tabla), 16 × 9 cm.
<!-- fin -->

## Decisiones

- **Recodificación R3 (`codificacion/RQ1-I1.jsonl`):** se cambian las categorías de 2 filas (R425 sin TDAH; R623 sin dislexia) y la `evidencia` de otras 2 (R705 y R106). Todas llevan `auto: false`. Se volvió a correr `sintesis:aggregate RQ1-B1`.
- **Cifras finales** (`tablas/RQ1-B1.json`, base 49): TEA 20, DI 18, discapacidad cognitiva 13, TDAH 11, DA 11, dislexia 8, síndrome de Down 4 y sin perfil específico 1. Hay 23 estudios con dos o más perfiles (sin cambios) y 10 mixtos con dos o más perfiles (sin cambios, de modo que la integración de RQ1-B3 se mantiene).
- **Heterogeneidad:** se usa el umbral común de 20 puntos. Diferencias entre cualitativos y mixtos: TEA 10, DI 8, discapacidad cognitiva 9, TDAH 2, DA 2, síndrome de Down 13 y dislexia 25. Solo la dislexia supera el umbral.
- **Estabilidad:** RQ1-I1 queda cerrado. RQ2-B2 debe volver a agregar y excluir «Sin perfil específico» de la matriz (7 filas de perfil).
