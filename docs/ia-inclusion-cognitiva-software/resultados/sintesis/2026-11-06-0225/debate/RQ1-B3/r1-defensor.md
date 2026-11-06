# RQ1-B3 — Ronda 1 — Defensor

Bloque: RQ1-I4 (enfoque sobre la condición, tratamiento del perfil y consentimiento informado; base 73). Agregación por frecuencia, síntesis aditiva y presentación en tabla. Es el cierre de la RQ1 e incluye la integración de lo cuantitativo y lo cualitativo. Las cifras salen de `tablas/RQ1-B3.json`, regenerada tras la recodificación; las de la integración, de `tablas/RQ1-B1.json` y `tablas/RQ1-B2.json`.

## Texto propuesto

<!-- inicio -->
### 3.4. Enfoque sobre la condición, tratamiento del perfil y consentimiento informado (RQ1)

En los 73 estudios seleccionados se registró cómo presentan la condición, cómo trata el sistema el perfil del usuario y si informan del consentimiento de los participantes. La Tabla {{T1}} reúne los tres aspectos.

Respecto al enfoque, el 74% (n=54) presenta la condición como una diferencia que el software debe acomodar, y el 26% (n=19) como un déficit que el software compensa. En el tratamiento del perfil, el 52% (n=38) describe sistemas que deducen el perfil o las necesidades del usuario a partir de su comportamiento o de sus datos, y el 48% (n=35) sistemas que almacenan un perfil declarado. En cuanto al consentimiento informado, el 38% (n=28) lo declara y en el 19% (n=14) no aplica, porque el estudio no tiene participantes con la condición. El 42% (n=31) restante no reporta el dato aunque tiene participantes con la condición o no lo descarta.

**Tabla {{T1}}**

*Enfoque sobre la condición, tratamiento del perfil y consentimiento informado, por enfoque metodológico*

| Aspecto | Categoría | Frecuencia (n) | Porcentaje | Cuantitativos (n) | Cualitativos (n) | Mixtos (n) |
|---|---|---|---|---|---|---|
| **Enfoque sobre la condición** | Diferencia que el software acomoda | 54 | 74% | 15 | 25 | 14 |
| | Déficit que el software compensa | 19 | 26% | 9 | 5 | 5 |
| **Tratamiento del perfil** | Deducido por el sistema | 38 | 52% | 14 | 16 | 8 |
| | Almacenado (declarado por el usuario) | 35 | 48% | 10 | 14 | 11 |
| **Consentimiento informado** | Declarado | 28 | 38% | 9 | 11 | 8 |
| | No aplica (sin participantes con la condición) | 14 | 19% | 5 | 8 | 1 |

*Nota.* Datos extraídos de los 73 artículos seleccionados (base n=73 en cada aspecto). El consentimiento no se reporta en n=31 (42%; 10 cuantitativos, 11 cualitativos y 10 mixtos). El país del estudio no se tabula aquí; la distribución geográfica se presenta en 3.1.

Los resultados son homogéneos en el tratamiento del perfil y en el consentimiento declarado, que reportan 9 de los 24 estudios cuantitativos, 11 de los 30 cualitativos y 8 de los 19 mixtos. En el enfoque sobre la condición son heterogéneos: el enfoque de déficit aparece en 9 de los 24 estudios cuantitativos, frente a 5 de los 30 cualitativos y 5 de los 19 mixtos.

**Integración de los resultados cuantitativos y cualitativos de la RQ1.** El ítem de perfiles se recoge solo en los estudios cualitativos y mixtos (n=49), y el de estratificación, solo en los cuantitativos y mixtos (n=43). Por eso el contraste entre ambos se limita a los 19 estudios mixtos. En la síntesis cualitativa, el 80% (n=39) de los 49 estudios declara dos o más perfiles; en la cuantitativa, el 81% (n=35) de los 43 estudios no desagrega los resultados por perfil. En los 19 estudios mixtos, 15 declaran dos o más perfiles y 15 no estratifican, y 13 de estos últimos declaran dos o más perfiles. Solo 3 estudios mixtos estratifican los resultados por perfil, y dos de ellos declaran un único perfil; en el estudio restante falta el dato de estratificación. Los 24 estudios cuantitativos no registran el perfil y los 30 cualitativos no registran la estratificación, de modo que en ellos no se puede hacer este contraste.
<!-- fin -->

## Decisiones

- **Recodificación hecha (`codificacion/RQ1-I4.jsonl`): 73 de 73 filas con `auto: false`.**
  - Se quitaron las categorías «País: …» de las 73 filas, como pedía el plan. No verifiqué el país en el MD: el dato publicado es el de B00-pais (3.1) y la *Nota.* remite a esa sección.
  - **«Consentimiento: No aplica» en 14 filas** (fuera del plan, pero consecuencia directa de RQ1-B2): son los 14 estudios con «Presencia: No» en `RQ1-I3.jsonl`. De ellos, 11 tenían «Consentimiento: NR» y 3 (R219, R453 y R1061) «Informado reportado», que es incoherente porque no tienen participantes con la condición (verificado en el MD; la evidencia está en la fila). Por eso el consentimiento declarado pasa de 31 a 28 y el no reportado, de 42 a 31.
- **«Consentimiento: NR»** se informa como «no reportado» en el texto y en la *Nota.*, no como fila de la tabla. Se mantiene en el jsonl para que las cifras (n=31, 42%) sigan en `tablas/RQ1-B3.json`.
- **Enfoque y Perfil** no se recodifican: suman 73 cada uno, son excluyentes y no estaban en el plan.
- **Integración** (campo `integracion` de `bloques.json`): RQ1-I1 (cualitativo) se cruza con RQ1-I2 (cuantitativo) en los 19 estudios mixtos comunes. Las cifras salen de las listas `estudios` de `tablas/RQ1-B1.json` y `tablas/RQ1-B2.json`:
  - estudios mixtos con dos o más perfiles: 15 de 19;
  - «No» en estratificación entre los mixtos: 15, de los que 13 tienen dos o más perfiles;
  - «Sí» en estratificación entre los mixtos: 3 (uno con dos perfiles, dos con uno solo);
  - NR: 1.

  El texto nombra de forma expresa los estudios cuantitativos, cualitativos y mixtos, e indica por qué el contraste solo es posible en los mixtos.
- **Presentación:** una tabla con tres grupos y columnas por enfoque metodológico. La heterogeneidad del enfoque de déficit se explica por la naturaleza del estudio, con bases de B00-enfoque (24, 30 y 19).
