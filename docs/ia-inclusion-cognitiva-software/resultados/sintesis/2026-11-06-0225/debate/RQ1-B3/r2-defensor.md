# RQ1-B3 — Ronda 2 — Defensor

Acepto las objeciones 1 a 4. Justifico la 5 en parte: la etiqueta sale de `matriz.json`, que este debate no puede editar, aunque el texto y la tabla publicados ya usan el título correcto. Las tablas se regeneraron después de cerrar RQ1-I1, RQ1-I2 y RQ1-I3 en la R2 de RQ1-B1 y RQ1-B2.

## Respuesta punto por punto

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | La dicotomía de Perfil es forzada: 73 de 73 sin NR; R391, R643 y R595 «Deducido»; R453 «Almacenado» | **Acepto** | Se añade «Perfil: NR» al codebook con la definición del crítico, ampliada: incluye la personalización que solo aparece en la motivación, en trabajos relacionados o como trabajo futuro, y la «adaptación» del modelo o del texto. Busqué los términos de perfil y personalización en los 73 MD y leí los 32 con 8 o menos menciones. Pasan a «Perfil: NR» 25, entre ellos los cuatro que cita el crítico y los basados en corpus (R285, R549, R595, R643 y R721). Llevan `auto: false` y `evidencia`. Resultado: Almacenado 26, NR 25 y Deducido 22 |
| 2 | La frase de homogeneidad mezcla aspectos; el perfil no es homogéneo; el déficit va en recuentos brutos | **Acepto** | Una frase por aspecto, con la proporción dentro de cada grupo. Criterio explícito: la diferencia es heterogénea si llega a 20 puntos porcentuales entre enfoques, el mismo que en RQ1-B1 y RQ1-B2. Con el perfil recalculado, la diferencia máxima es de 12 puntos (homogéneo). En el déficit es de 21 puntos y en el consentimiento declarado, de 23 (heterogéneos). El consentimiento se calcula sobre los estudios con participantes con la condición, que son los únicos en los que aplica |
| 3 | «No aplica» copia un RQ1-I3 incompleto (R183, R721) | **Acepto** | «No aplica» se regeneró con el RQ1-I3 de la R2, con sus 73 filas verificadas. Pasan a «No aplica» 17 estudios más: 12 tenían «NR» y 5 tenían «Informado reportado» (R040, R173, R300, R495 y R705). En estos 5, el consentimiento declarado es el de cuidadores, profesionales o de un estudio anterior, no el de personas con la condición, y así lo dice el codebook. Resultado: No aplica 31, Informado reportado 23 y NR 19 |
| 4 | La integración se apoya en codificaciones que no resisten (R263, R398, R145); falta la frase con RQ1-I3 | **Acepto** | Rehecha con RQ1-I1 y RQ1-I2 corregidos: R263 y R473 ya no estratifican, R398 tiene un único perfil y R145 solo TDAH. Se añade la frase con RQ1-I3: de los 3 estudios que estratifican, 2 tienen participantes con la condición, y de los 22 estudios cuantitativos o mixtos con esos participantes, 2 estratifican |
| 5 | La etiqueta de `tablas/RQ1-B3.json` sigue nombrando el País | **Justifico en parte.** El `label` lo copia `sintesis:aggregate` de `items_meta` en `matriz.json`, que viene del formulario, y el encargo de este debate prohíbe editar `matriz.json`, `items.json` y `bloques.json` | El título publicado de la tabla y de la subsección ya es «Enfoque sobre la condición, tratamiento del perfil y consentimiento informado». El codebook (`## RQ1-I4`) deja escrito que la etiqueta de `matriz.json` es heredada. Propongo que el orquestador cambie `items_meta.RQ1-I4.label`, o que el script lo tome de `bloques.json`, al cerrar el bloque |

## Texto propuesto

<!-- inicio -->
### 3.4. Enfoque sobre la condición, tratamiento del perfil y consentimiento informado (RQ1)

En los 73 estudios seleccionados se registró cómo presentan la condición, cómo trata el sistema el perfil del usuario y si informan del consentimiento de las personas con la condición que participan. La Tabla {{T1}} reúne los tres aspectos por enfoque metodológico.

En cuanto al enfoque, el 74% (n=54) presenta la condición como una diferencia que el software debe acomodar y el 26% (n=19) como un déficit que el software compensa. En el tratamiento del perfil, el 36% (n=26) describe sistemas que almacenan un perfil declarado por el usuario y el 30% (n=22) sistemas que deducen el perfil o las necesidades a partir del comportamiento o de los datos. En el 34% (n=25) restante, el artefacto no gestiona un perfil de usuario o el artículo no lo describe. Respecto al consentimiento informado, en el 42% (n=31) no aplica, porque el estudio no tiene participantes con la condición. De los 42 estudios en los que sí aplica, 23 (el 32% de los 73) declaran el consentimiento y 19 (26%) no lo reportan.

**Tabla {{T1}}**

*Enfoque sobre la condición, tratamiento del perfil y consentimiento informado, por enfoque metodológico*

| Aspecto | Categoría | Frecuencia (n) | Porcentaje | Cuantitativos, n (%) | Cualitativos, n (%) | Mixtos, n (%) |
|---|---|---|---|---|---|---|
| **Enfoque sobre la condición** | Diferencia que el software acomoda | 54 | 74% | 15 (63%) | 25 (83%) | 14 (74%) |
| | Déficit que el software compensa | 19 | 26% | 9 (38%) | 5 (17%) | 5 (26%) |
| **Tratamiento del perfil** | Almacenado (declarado por el usuario) | 26 | 36% | 8 (33%) | 10 (33%) | 8 (42%) |
| | Deducido por el sistema | 22 | 30% | 6 (25%) | 11 (37%) | 5 (26%) |
| **Consentimiento informado** | Declarado | 23 | 32% | 7 (29%) | 8 (27%) | 8 (42%) |
| | No aplica (sin participantes con la condición) | 31 | 42% | 14 (58%) | 15 (50%) | 2 (11%) |

*Nota.* Datos extraídos de los 73 artículos seleccionados (base n=73 en cada aspecto). Los porcentajes por enfoque se calculan sobre 24 estudios cuantitativos, 30 cualitativos y 19 mixtos. El tratamiento del perfil no se reporta en n=25 (10 cuantitativos, 9 cualitativos y 6 mixtos). El consentimiento no se reporta en n=19 (3 cuantitativos, 7 cualitativos y 9 mixtos). El país del estudio no se tabula aquí; la distribución geográfica se presenta en 3.1.

Los resultados son heterogéneos en el enfoque sobre la condición: el enfoque de déficit aparece en el 38% (9 de 24) de los estudios cuantitativos, el 26% (5 de 19) de los mixtos y el 17% (5 de 30) de los cualitativos. El tratamiento del perfil es homogéneo, con diferencias entre enfoques de 12 puntos porcentuales como máximo. En el consentimiento, calculado sobre los estudios con participantes con la condición, los resultados son heterogéneos: lo declaran el 70% (7 de 10) de los estudios cuantitativos, el 53% (8 de 15) de los cualitativos y el 47% (8 de 17) de los mixtos.

**Integración de los resultados cuantitativos y cualitativos de la RQ1.** El ítem de perfiles se recoge solo en los estudios cualitativos y mixtos (n=49) y el de estratificación solo en los cuantitativos y mixtos (n=43), de modo que el contraste directo entre ambos se limita a los 19 estudios mixtos. En la síntesis cualitativa, el 47% (n=23) de los 49 estudios declara dos o más perfiles. En la síntesis cuantitativa, el 91% (n=39) de los 43 estudios no desagrega los resultados por perfil. De los 19 estudios mixtos, 10 declaran dos o más perfiles. De esos mixtos, 17 no estratifican, y 9 de ellos declaran dos o más perfiles; el único que estratifica declara un solo perfil y compara a los participantes con la condición con usuarios sin ella, y en el restante falta el dato. El ítem de participación, registrado en los 73 estudios, completa el contraste: de los 3 estudios que estratifican, 2 tienen participantes con la condición, y de los 22 estudios cuantitativos o mixtos con esos participantes, 2 estratifican los resultados. Los 24 estudios cuantitativos no registran el perfil y los 30 cualitativos no registran la estratificación.
<!-- fin -->

## Decisiones

- **Recodificación R2 (`codificacion/RQ1-I4.jsonl`):** 36 filas cambiadas, con `auto: false` y `evidencia`. Son 25 que pasan a «Perfil: NR» y 17 que pasan a «Consentimiento: No aplica»; algunas filas tienen los dos cambios. Las 73 filas ya tenían `auto: false` desde la R1, por la retirada del País.
- **Cifras:** salen de `tablas/RQ1-B3.json` (`n`, `pct` y `por_naturaleza`). Los porcentajes por grupo usan las bases de B00-enfoque (24, 30 y 19). El consentimiento sobre los estudios con participantes usa como base, por grupo, la suma de «Declarado» y «NR» de la propia tabla (10, 15 y 17; 42 en total).
- **Integración** (campo `integracion` de `bloques.json`): las cifras salen de las listas `estudios` de `tablas/RQ1-B1.json` y `tablas/RQ1-B2.json`.
  - Mixtos con dos o más perfiles: 10 de 19.
  - «No» en estratificación entre los mixtos: 17, de los que 9 tienen dos o más perfiles.
  - «Sí» entre los mixtos: 1, con un solo perfil (TEA) y comparación con usuarios convencionales.
  - NR entre los mixtos: 1, con cuatro perfiles.
  - Los 3 «Sí» frente a RQ1-I3: dos con presencia («Sí») y uno sin ella.
  - Cuantitativos o mixtos con presencia: 6 + 16 = 22, de los que 2 estratifican.

  El párrafo nombra de forma expresa los estudios cuantitativos, cualitativos y mixtos.
- **Criterio de homogeneidad:** heterogéneo si la diferencia entre enfoques llega a 20 puntos porcentuales. Es el mismo criterio en los tres bloques de la RQ1.
- **Presentación:** una tabla con tres grupos y columnas «n (%)» por enfoque. Los NR del perfil y del consentimiento van en la *Nota.*, no como filas.
