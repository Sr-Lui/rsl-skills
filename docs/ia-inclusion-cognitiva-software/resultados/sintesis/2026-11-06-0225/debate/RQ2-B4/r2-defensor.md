# RQ2-B4 — Ronda 2 — Defensor

Acepto las cuatro objeciones. Para la n.º 1 fijé una regla de decisión en `codebook.md` (`## RQ2-I3`) y la apliqué a las **43** filas de la fase principal: ahora todas tienen `auto: false` y `evidencia` (título, resumen o línea del MD). Respecto del registro difieren 21 filas: 19 cambian de fase y 2 estaban vacías. RQ2-I4 se rederivó del conjunto de fases verificadas de cada estudio, menos su nueva fase principal. Volví a correr `sintesis:aggregate RQ2-B4`. Las cifras cambian mucho: el desarrollo pasa a ser la fase principal más frecuente y las pruebas pasan a ser sobre todo otra fase.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | Fase principal sin verificar; R040, R263, R246 y R203 contradicen el codebook | **Acepto.** Se decide por la contribución que declaran el título y el resumen, en este orden: Requisitos → V&V → Pruebas (artefacto, modelos o textos no construidos en el artículo, o estudio que se presenta como evaluación) → Personalización en ejecución (artefacto presentado como adaptativo o personalizado al usuario) → Desarrollo (presenta o desarrolla el artefacto, aunque después lo evalúe) | R040, R123, R183, R233, R263, R345, R369, R396, R595, R600 y R623: de Pruebas a Desarrollo. R203: de Personalización a Desarrollo. R147, R293 y R398: de Pruebas a Personalización. R630 (vacía): a Personalización. R145: de Desarrollo a Pruebas. R246 sigue en Desarrollo. Nuevas cifras: Desarrollo 24 (56%), Pruebas 9 (21%), Personalización 6 (14%), Requisitos 3 (7%) y V&V 1 (2%). RQ2-I4: Pruebas 29 (67%), Desarrollo 14 (33%), Requisitos 6 (14%) y solo una fase 5 (12%) |
| 2 | Fórmula de NR | **Acepto** | «no reporta(n) una técnica de IA aplicada» |
| 3 | Reparto por familia selectivo | **Acepto** | Se reportan las cinco familias con las nuevas fases de los 19 mixtos |
| 4 | El «Así…» interpreta | **Acepto en parte.** La fórmula propuesta, «en ninguno de los 19 mixtos la IA se emplea para probar el software», es falsa: en un estudio mixto la IA genera las frases de prueba con que se evalúa la herramienta. Cierro con un dato sin «Así» | «El único estudio mixto en que la IA asiste al aseguramiento de la calidad, al generar datos de prueba, tiene el desarrollo como fase principal; en los tres con las pruebas como fase principal, la IA forma parte del artefacto que se prueba» |

## Texto propuesto

<!-- inicio -->
### 3.?. Fases del ciclo de vida del software: fase principal y otras fases (RQ2)

La fase del ciclo de vida del software se registró en los 43 estudios con enfoque cuantitativo o mixto de los 73 seleccionados (24 cuantitativos y 19 mixtos), distinguiendo la fase principal en que se sitúa la contribución del estudio y las otras fases que también aborda. Como se observa en la Figura {{F1}}, el desarrollo es la fase principal en el 56% (n=24) de los estudios, que presentan o desarrollan un artefacto con IA. Las pruebas lo son en el 21% (n=9), que evalúan modelos, herramientas o textos no construidos en el propio estudio o se presentan como estudios de evaluación. La personalización en ejecución es la fase principal en el 14% (n=6), los requisitos en el 7% (n=3) y la verificación y validación en el 2% (n=1).

Como otras fases, el 67% (n=29) aborda también las pruebas, el 33% (n=14) el desarrollo y el 14% (n=6) los requisitos. El 63% (n=27) aborda una fase además de la principal, el 26% (n=11) aborda dos y el 12% (n=5) se limita a una sola fase. Si se suman la fase principal y las otras, el desarrollo y las pruebas aparecen cada uno en el 88% (n=38) de los estudios y los requisitos en el 21% (n=9). La personalización en ejecución y la verificación y validación solo aparecen como fase principal.

Los resultados son homogéneos entre los estudios cuantitativos y los mixtos, con diferencias de hasta 16 puntos porcentuales. El desarrollo es la fase principal en el 58% (14 de 24) de los cuantitativos y en el 53% (10 de 19) de los mixtos, y las pruebas, en el 25% (6 de 24) y el 16% (3 de 19), respectivamente. Los tres estudios con los requisitos como fase principal son mixtos. Los 30 estudios cualitativos no registran estos ítems, porque el formulario solo los recoge en la hoja cuantitativa.

**Figura {{F1}}**

*Fase principal y otras fases del ciclo de vida del software reportadas en los estudios*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 73 artículos seleccionados (2021–2027). Base: 43 estudios cuantitativos o mixtos. Cada estudio tiene una fase principal y puede abordar más de una fase adicional, por lo que la serie de otras fases no suma 100%. El 12% (n=5) no aborda ninguna fase además de la principal.

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** barras horizontales agrupadas.
- **Por qué este tipo:** compara dos series (fase principal y otras fases) sobre las mismas categorías y la misma base (n=43); las barras horizontales admiten etiquetas largas.
- **Qué muestra:** el porcentaje de los 43 estudios cuantitativos o mixtos en que cada fase es la principal y en que aparece como otra fase.
- **Datos a dibujar:** las categorías del eje Y, en este orden, con sus dos series:

  | Fase | Fase principal | Otras fases |
  |---|---|---|
  | Desarrollo | n=24, 56% | n=14, 33% |
  | Pruebas | n=9, 21% | n=29, 67% |
  | Requisitos | n=3, 7% | n=6, 14% |
  | Personalización en ejecución | n=6, 14% | n=0, 0% |
  | Verificación y validación | n=1, 2% | n=0, 0% |

  «Solo una fase» (n=5, 12%) no se dibuja; va en la nota.
- **Ejes:** en el eje Y, la fase, ordenada de mayor a menor por la suma de las dos series. Desarrollo y pruebas empatan en 38; el desarrollo va arriba por tener más casos como fase principal. En el eje X, el porcentaje de estudios, en escala lineal de 0 a 100%.
- **Etiquetas sobre los datos:** `X% (n=Y)` al final de cada barra, incluidas las de 0% (n=0).
- **Leyenda:** dos series, «Fase principal» (azul oscuro) y «Otras fases» (azul claro).
- **Título interno del gráfico:** ninguno; el título es el de la figura.
- **Nota del gráfico:** «La serie “Otras fases” no suma 100%: un estudio puede abordar más de una fase además de la principal (base n = 43 estudios cuantitativos o mixtos). 5 estudios (12%) abordan solo la fase principal».
- **Estilo:** dos tonos de azul sobrio, barras agrupadas por fase con la principal arriba en cada grupo, 16 × 10 cm.

**Integración de los resultados cualitativos y cuantitativos de la RQ2**

La técnica y el rol de la IA proceden de la hoja de los estudios cualitativos y mixtos, y las fases, de la hoja de los estudios cuantitativos y mixtos. Por eso, ambos tipos de resultados solo pueden relacionarse en los 19 estudios mixtos: los 30 estudios cualitativos no registran la fase y los 24 estudios cuantitativos no registran la técnica ni el rol. En esos 19 estudios, la fase principal es desarrollo en 10, y pruebas, personalización en ejecución y requisitos en 3 cada una.

Tres estudios mixtos no reportan una técnica de IA aplicada: dos tienen los requisitos como fase principal y uno el desarrollo. En los 3 con la personalización en ejecución como fase principal, la IA actúa como personalizadora en los 3, como generadora en 2 y como intérprete del usuario en 2. En los 3 con las pruebas como fase principal, la IA forma parte del artefacto que se prueba: es generadora en 2, intérprete en 1 y personalizadora en 1. En los 10 con el desarrollo como fase principal, la IA es generadora en 6, intérprete en 4 y evaluadora del contenido en 2, y en 1 asiste al aseguramiento de la calidad, al generar las frases de prueba con que se evalúa la herramienta. Este es el único estudio mixto en que la IA interviene en el proceso de prueba del software.

Por familia, el desarrollo es la fase principal más frecuente en las cinco: el procesamiento del lenguaje natural o del habla en 6 de 9 (2 en personalización en ejecución y 1 en requisitos), el aprendizaje automático en 5 de 8 (2 en personalización y 1 en pruebas), el aprendizaje profundo en 3 de 6 (2 en personalización y 1 en pruebas), los LLM en 3 de 6 (2 en pruebas y 1 en personalización) y la visión por computador en 3 de 3.
<!-- fin -->

## Decisiones

- **`codificacion/RQ2-I3.jsonl`: 43 de 43 filas con `auto: false` y `evidencia`.** La regla de decisión está en `codebook.md` (`## RQ2-I3`).
  - **Casos límite**, según la regla:
    - R145 queda en Pruebas, porque el resumen se presenta como «pilot study».
    - R296 queda en Pruebas, porque presenta «findings from three rounds of testing».
    - R527 queda en Pruebas, porque el resumen declara como contribución el examen de las experiencias de 62 estudiantes, no el sistema.
    - R831 queda en Pruebas: es el primer estudio empírico de ChatGPT-4o interpretando reglas, un modelo existente.
    - R630 pasa a Personalización, porque el título y la l. 108 presentan un algoritmo «with involuntary head movement adaptation».
  - **Coherencia con RQ2-I2.** De los 4 estudios mixtos con rol de personalizador, 3 tienen ahora la personalización en ejecución como fase principal. El cuarto es R527 (Pruebas, por lo anterior). R203, que no tiene ese rol, deja la personalización.
- **`codificacion/RQ2-I4.jsonl`.** Se rederivó como conjunto de fases verificadas en R1 (requisitos, desarrollo, pruebas) menos la nueva fase principal. Las filas que cambian llevan la evidencia «(R2)», con la línea de pruebas o de desarrollo cuando esa fase pasa a ser «otra». «Solo una fase» sigue en los mismos 5 estudios.
- **Cifras** (`tablas/RQ2-B4.json`, base 43):
  - Fase principal: Desarrollo 24, Pruebas 9, Personalización 6, Requisitos 3 y V&V 1. Otras fases: Pruebas 29, Desarrollo 14, Requisitos 6 y solo una fase 5.
  - Número de fases adicionales: una en 27 estudios y dos en 11.
  - Uniones sin solapamiento: Desarrollo 38, Pruebas 38 y Requisitos 9.
  - Heterogeneidad: la diferencia máxima es Requisitos como fase principal, 0% frente a 16%. Le sigue Requisitos como otra fase, con 13 puntos (8% frente a 21%). Las pruebas como fase principal difieren 9 puntos (25% frente a 16%) y el resto, 8 puntos o menos. Ninguna supera el umbral común de 20 puntos.
- **Integración.** Sale de cruzar las listas `estudios` de `tablas/RQ2-B1.json`, `RQ2-B3.json` y `RQ2-B4.json` en los 19 mixtos.
  - Los mixtos sin técnica de IA son R199 y R425 (Requisitos) y R600 (Desarrollo).
  - Los evaluadores del contenido son R106 y R587 (Desarrollo). El asistente de AC mixto es R106 (Desarrollo).
  - Por objeción del crítico se reportan las cinco familias. La frase final de R1 («Así…») se elimina y el cierre es un dato.
- **Spec** (`graficos/RQ2-B4.spec.json`): actualizada con las nuevas series y el nuevo orden (Desarrollo arriba).
