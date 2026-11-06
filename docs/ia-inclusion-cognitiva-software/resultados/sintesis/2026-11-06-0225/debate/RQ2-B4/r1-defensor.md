# RQ2-B4 — Ronda 1 — Defensor

La recodificación de RQ2-I4 hace posible la figura acordada: barras horizontales agrupadas que comparan la fase principal y las otras fases sobre la misma base (n=43). Además de la resta determinista, verifiqué en el MD cada fase restante, porque la plantilla «desarrollo; pruebas; requisitos» se repetía en 28 de 43 filas. También corregí cinco fases principales con errores evidentes. El bloque cierra la RQ2 con la integración cualitativa y cuantitativa en los 19 estudios mixtos.

## Texto propuesto

<!-- inicio -->
### 3.?. Fases del ciclo de vida del software: fase principal y otras fases (RQ2)

La fase del ciclo de vida del software se registró en los 43 estudios con enfoque cuantitativo o mixto de los 73 seleccionados (24 cuantitativos y 19 mixtos), distinguiendo la fase principal en que se sitúa la contribución del estudio y las otras fases que también aborda. Como se observa en la Figura {{F1}}, las pruebas son la fase principal en el 51% (n=22) de los estudios y el desarrollo en el 33% (n=14). Los requisitos y la personalización en ejecución son la fase principal en el 7% (n=3) cada uno, y la verificación y validación en el 2% (n=1).

Como otras fases, el 56% (n=24) aborda también el desarrollo, el 37% (n=16) las pruebas y el 14% (n=6) los requisitos. El 70% (n=30) aborda una fase además de la principal, el 19% (n=8) aborda dos y el 12% (n=5) se limita a una sola fase. Si se suman la fase principal y las otras, las pruebas y el desarrollo aparecen cada uno en el 88% (n=38) de los estudios y los requisitos en el 21% (n=9). La personalización en ejecución y la verificación y validación solo aparecen como fase principal.

Los resultados son homogéneos entre los estudios cuantitativos y los mixtos, con diferencias de hasta 16 puntos porcentuales. Las pruebas son la fase principal en el 54% (13 de 24) de los cuantitativos y en el 47% (9 de 19) de los mixtos, y el desarrollo, en el 33% (8 de 24) y el 32% (6 de 19), respectivamente. Los tres estudios con los requisitos como fase principal son mixtos. Los 30 estudios cualitativos no registran estos ítems, porque el formulario solo los recoge en la hoja cuantitativa.

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
  | Pruebas | n=22, 51% | n=16, 37% |
  | Desarrollo | n=14, 33% | n=24, 56% |
  | Requisitos | n=3, 7% | n=6, 14% |
  | Personalización en ejecución | n=3, 7% | n=0, 0% |
  | Verificación y validación | n=1, 2% | n=0, 0% |

  «Solo una fase» (n=5, 12%) no se dibuja; va en la nota.
- **Ejes:** en el eje Y, la fase, ordenada de mayor a menor por la suma de las dos series (pruebas y desarrollo empatan en 38; las pruebas van arriba por tener más casos como fase principal). En el eje X, el porcentaje de estudios, en escala lineal de 0 a 100%.
- **Etiquetas sobre los datos:** `X% (n=Y)` al final de cada barra, incluidas las de 0% (n=0).
- **Leyenda:** dos series, «Fase principal» (azul oscuro) y «Otras fases» (azul claro).
- **Título interno del gráfico:** ninguno; el título es el de la figura.
- **Nota del gráfico:** «La serie “Otras fases” no suma 100%: un estudio puede abordar más de una fase además de la principal (base n = 43 estudios cuantitativos o mixtos). 5 estudios (12%) abordan solo la fase principal».
- **Estilo:** dos tonos de azul sobrio, barras agrupadas por fase con la principal arriba en cada grupo, 16 × 10 cm.

**Integración de los resultados cualitativos y cuantitativos de la RQ2**

La técnica y el rol de la IA proceden de la hoja de los estudios cualitativos y mixtos, y las fases, de la hoja de los estudios cuantitativos y mixtos. Por eso, ambos tipos de resultados solo pueden relacionarse en los 19 estudios mixtos: los 30 estudios cualitativos no registran la fase y los 24 estudios cuantitativos no registran la técnica ni el rol. En esos 19 estudios, la fase principal es pruebas en 9, desarrollo en 6, requisitos en 3 y personalización en ejecución en 1. De los 9 con las pruebas como fase principal, uno no aplica ninguna técnica de IA; en los otros 8, la IA forma parte del artefacto que se prueba: actúa como intérprete de la entrada o del estado del usuario en 5, como personalizadora en 4 y como generadora en 4, y ninguno la emplea como evaluadora ni como asistente de aseguramiento de la calidad. Los dos estudios mixtos en que la IA evalúa la accesibilidad del contenido tienen el desarrollo como fase principal. Dos de los tres estudios mixtos con los requisitos como fase principal no aplican ninguna técnica de IA. Por familia, el aprendizaje automático (5 de 8) y el aprendizaje profundo (4 de 6) se concentran en estudios cuya fase principal es pruebas, mientras que los LLM se reparten entre desarrollo (3 de 6), pruebas (2 de 6) y personalización en ejecución (1 de 6). Así, en los estudios mixtos, la fase de pruebas, que es la más frecuente en la serie cuantitativa, corresponde a la evaluación de un artefacto cuya IA genera, interpreta o personaliza, y no al uso de la IA para probar el software.
<!-- fin -->

## Decisiones

- **`codificacion/RQ2-I4.jsonl`: 43 de 43 filas con `auto: false` y `evidencia`.** Reglas en `codebook.md` (`## RQ2-I4`).
  - **Resta determinista**, según el plan: a cada estudio se le quita la fase principal de RQ2-I3. Con eso desaparece la repetición de la principal (36 de 41).
  - **Verificación de cada fase restante.** La resta no bastaba: la plantilla «desarrollo; pruebas; requisitos» (28 de 43) seguía dando Requisitos en 30 de 43. Busqué en el cuerpo del MD patrones de requisitos (*requirements elicitation*, *needs assessment*), de desarrollo (*we developed*, *implemented*, *trained*) y de pruebas (*user study*, *usability evaluation*, *pilot study*, *test set*), y leí el contexto de cada coincidencia.
    - Requisitos queda en 6: R040, R106, R208, R345, R587 y R600.
    - Se añadió una fase solo cuando el texto la muestra (Desarrollo en R293 y R296; Requisitos en R106).
    - Pasan a «Solo una fase» 5 estudios: R016 y R440, que evalúan modelos o herramientas sin construir un artefacto; R199 y R425, de requisitos sin desarrollo ni pruebas; y R617, que evalúa textos con lectores.
- **`codificacion/RQ2-I3.jsonl`: 5 filas con `auto: false`** (las otras 38 se mantienen, con `auto: true`).
  - R199, R425 y R626 pasan de Pruebas o Desarrollo a Requisitos. Sus títulos y objetivos son la recogida de requisitos o necesidades: «Gathering Requirements…», «multi-stakeholder needs assessment» y «define which are the requirements».
  - R106 y R630, vacías en el registro, pasan a Desarrollo.
  - Con esto, Requisitos deja de tener 0 en la serie principal y RQ2-I3 ya no tiene NR.
- **Cifras.** Todas salen de `tablas/RQ2-B4.json` (base 43).
  - Fase principal: Pruebas 22, Desarrollo 14, Requisitos 3, Personalización en ejecución 3 y V&V 1. Otras fases: Desarrollo 24, Pruebas 16, Requisitos 6 y «Solo una fase» 5.
  - «Una fase adicional, 30; dos, 8» sale de contar las fases de cada estudio en las listas `estudios`.
  - Las sumas (38, 38 y 9) son uniones sin solapamiento, porque las otras fases ya no incluyen la principal.
  - El reparto por naturaleza sale de `por_naturaleza`.
- **Integración.** Las cifras salen de cruzar las listas `estudios` de `tablas/RQ2-B1.json` (familias y NR), `tablas/RQ2-B3.json` (roles) y `tablas/RQ2-B4.json` (fase principal), restringidas a los 19 estudios mixtos.
  - Los 3 mixtos sin técnica de IA son R199 y R425 (Requisitos) y R600 (Pruebas).
  - Los 2 mixtos evaluadores son R106 y R587 (Desarrollo).
  - Es el par que fijó el plan: RQ2-I1 y RQ2-I2 (cualitativos) frente a RQ2-I3 y RQ2-I4 (cuantitativos). La última frase es la lectura cruzada que pide el playbook (§1: si lo cualitativo ayuda a explicar lo cuantitativo) y se limita a lo que dicen los roles codificados.
- **Heterogeneidad.** Con el umbral común de 20 puntos, ninguna categoría lo supera. La mayor diferencia es Requisitos como fase principal (0% frente a 16%); en las otras fases, Requisitos difiere 13 puntos (8% frente a 21%).
- **Presentación:** figura, como se acordó; la condición del plan (recodificar RQ2-I4) se cumple. Los datos van como tabla de dos series dentro del Detalle gráfica porque son dos series. Spec en `graficos/RQ2-B4.spec.json`.
- **Límites.**
  - El formulario no registró la fase de diseño. Los estudios de codiseño quedan en Requisitos o Desarrollo según su objetivo, y el texto no reporta una fase de diseño.
  - La fase principal se mantuvo como estaba registrada salvo los cinco errores evidentes. Su definición es la fase en que se sitúa la contribución del estudio, no necesariamente aquella en que la IA actúa sobre el software. La integración deja esa diferencia a la vista sin recodificar las 38 filas restantes.
