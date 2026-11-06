# RQ1-B2 — Ronda 1 — Defensor

Bloque: RQ1-I2 (estratificación por perfil, base 43) y RQ1-I3 (participación de personas con la condición, base 73). Agregación por frecuencia, síntesis aditiva y presentación en tabla. Las cifras salen de `tablas/RQ1-B2.json`, regenerada tras la recodificación.

## Texto propuesto

<!-- inicio -->
### 3.3. Estratificación por perfil y participación de personas con la condición (RQ1)

Este apartado combina dos ítems con bases distintas: la estratificación de resultados por perfil, registrada en los 43 estudios con enfoque cuantitativo o mixto, y la participación de personas con la condición, registrada en los 73 estudios seleccionados. La Tabla {{T1}} resume ambos.

De los 43 estudios cuantitativos o mixtos, el 81% (n=35) presenta los resultados de la muestra global, sin desagregarlos por perfil. El 16% (n=7) los estratifica por perfil o subgrupo, y un estudio no reporta el dato.

Del total de 73 estudios, el 79% (n=58) incluye a personas con la condición entre sus participantes. El 19% (n=14) no las incluye: evalúa el artefacto con corpus, respuestas generadas, anotadores o expertos, se plantea como ensayo conceptual o deja la prueba con usuarios para un trabajo futuro. En un estudio no se puede confirmar si los participantes tienen la condición. En cuanto al rol, el 47% (n=34) de los 73 estudios registra a estas personas solo en la evaluación del artefacto, el 32% (n=23) en el diseño y en la evaluación, y un estudio (1%) solo en el diseño, mediante un cuestionario de necesidades.

**Tabla {{T1}}**

*Estratificación por perfil y participación de personas con la condición, por enfoque metodológico*

| Ítem | Categoría | Frecuencia (n) | Porcentaje | Cuantitativos (n) | Cualitativos (n) | Mixtos (n) |
|---|---|---|---|---|---|---|
| **Estratificación por perfil** (base n=43) | No: resultados de la muestra global | 35 | 81% | 20 | — | 15 |
| | Sí: resultados desagregados por perfil o subgrupo | 7 | 16% | 4 | — | 3 |
| **Presencia de personas con la condición** (base n=73) | Sí | 58 | 79% | 19 | 22 | 17 |
| | No | 14 | 19% | 5 | 8 | 1 |
| **Rol de las personas con la condición** (base n=73) | Solo evaluación | 34 | 47% | 16 | 10 | 8 |
| | Diseño y evaluación | 23 | 32% | 3 | 12 | 8 |
| | Solo diseño | 1 | 1% | 0 | 0 | 1 |

*Nota.* Datos extraídos de los 73 artículos seleccionados. La estratificación solo se registra en los estudios cuantitativos y mixtos (base n=43); la presencia y el rol, en los 73. El dato de estratificación no se reporta en n=1 y la presencia no se confirma en n=1. El rol solo se registra cuando hay presencia (34 + 23 + 1 = 58). No se agrega el número de personas con la condición por estudio, porque el registro de participantes y el de muestra discrepan en 16 de los 33 estudios con ambos valores; el tamaño de muestra de los estudios se describe en 3.1.

Los resultados son heterogéneos según el enfoque metodológico. En los estudios cuantitativos predomina la participación solo en la evaluación (16 de los 19 con presencia), mientras que en los cualitativos la participación en el diseño y la evaluación (n=12) supera a la que se limita a la evaluación (n=10). Los estudios sin personas con la condición se concentran en los cualitativos (n=8) y los cuantitativos (n=5), frente a un solo estudio mixto.
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ1-I3.jsonl`): 22 filas con `auto: false` y `evidencia`.** Se verificaron en el MD una a una todas las filas que el plan señalaba (15 «sin_participantes», 3 «otro» y 4 «nr» en `matriz.json`).
  - **«Presencia: No» sin Rol (14):** R016 (240 respuestas generadas), R219, R264, R285, R337, R391, R399 (la prueba con usuarios «is planned as future work»), R457 («no human participants were involved»), R643, R1061, R595 (anotadores), R663, R263 (los estudios con usuarios se proponen a futuro) y R453 (ensayo conceptual).
  - **«Presencia: Sí» confirmada en el MD (7):** R193 (análisis conversacional con una mujer con discapacidad de aprendizaje, Evaluación), R208 (cinco adultos con discapacidad intelectual o del desarrollo, Ambos), R327 (expertos por experiencia vivida con TDAH, Ambos), R396 (ocho participantes con dificultades matemáticas autodeclaradas, Evaluación), R626 (más de 1300 personas con certificado de trastorno específico del aprendizaje responden un cuestionario de necesidades; se crea **Rol: Diseño**), R647 (codiseño con un joven adulto con discapacidad intelectual, Ambos) y R504 (diez niños no verbales, Evaluación).
  - **NR (1):** R623. Los 110 que responden el cuestionario son visitantes y la intervención clínica se describe como futura.
- **Me aparto del plan en dos puntos, con evidencia:**
  1. La regla «sin_participantes → Presencia: No» no se aplicó a ciegas, porque es falsa en 6 de 15 estudios. La alerta sobre los estudios con «Revisión bibliográfica (sin n empírico)» en `muestra_raw` (13 de los 15) apunta a un **error de extracción de la muestra, no a estudios secundarios**: ninguno de los que verifiqué es una revisión. Son herramientas, prototipos, marcos o casos, y R208, R327, R396, R626 y R647 tienen participantes, mientras que R193 analiza interacciones reales grabadas en vídeo.
  2. **No se publican el rango ni la mediana de N.** `valores.N` de RQ1-I3 y `muestra.n` discrepan en 16 de los 33 estudios con ambos valores numéricos (p. ej., R145: 15 frente a 1; R425: 202 frente a 1; R705: 105 frente a 2). Además, `sintesis:aggregate` no agrega `valores`, así que esas cifras no estarían en `tablas/RQ1-B2.json`. Publicarlas exigiría verificar N en unos 30 MD, y lo dejo propuesto para la R2 si el crítico lo pide. La *Nota.* declara la limitación y remite a 3.1.
- **RQ1-I2 sin recodificar** (no estaba en el plan). Lo señalo para el crítico: R263 y R457 llevan «Sí» en estratificación pero no tienen participantes con la condición. La desagregación podría ser por perfil simulado o de sistema; no la cambio sin leer el resultado en el MD.
- **Cifras y presentación:** todas salen de `tablas/RQ1-B2.json` (`n`, `pct`, `por_naturaleza`). Va una sola tabla, agrupada por ítem y con la base en cada grupo, más tres columnas por enfoque que muestran la causa de la heterogeneidad. Los NR van en la *Nota.*, no como filas. Los porcentajes del rol se dan sobre 73, que es la base de la tabla, y el texto lo dice expresamente («de los 73 estudios»).
