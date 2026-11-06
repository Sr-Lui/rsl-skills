# RQ1-B1 — Ronda 1 — Defensor

Bloque: RQ1-I1, perfiles de discapacidad cognitiva o neurodivergencia declarados. Agregación por frecuencia, síntesis aditiva y presentación en figura. Las cifras salen de `tablas/RQ1-B1.json`, regenerada tras la recodificación, con base n = 49 estudios cualitativos o mixtos.

## Texto propuesto

<!-- inicio -->
### 3.2. Perfiles de discapacidad cognitiva o neurodivergencia abordados (RQ1)

El ítem de perfiles se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos). Todos describen a su población como neurodivergente o con discapacidad cognitiva, y por eso la síntesis se hace sobre los perfiles específicos que declara cada estudio. Como se observa en la Figura {{F1}}, el 67% (n=33) declara el trastorno del espectro autista (TEA). La discapacidad intelectual (DI) y las dificultades de aprendizaje se declaran cada una en el 51% (n=25). Siguen la dislexia, con el 41% (n=20), y el término genérico de discapacidad cognitiva, con el 33% (n=16). El 27% (n=13) menciona el trastorno por déficit de atención con hiperactividad (TDAH) y el 16% (n=8) el síndrome de Down. El 80% (n=39) de los estudios declara dos o más perfiles, de modo que los porcentajes no suman 100%.

**Figura {{F1}}**

*Perfiles de discapacidad cognitiva o neurodivergencia declarados en los estudios*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 73 artículos seleccionados (2021–2027).

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** barras horizontales.
- **Por qué este tipo:** siete categorías nominales de un ítem multivalor, con etiquetas largas; las barras horizontales ordenadas por n comparan las categorías y muestran la concentración en pocos perfiles.
- **Qué muestra:** el porcentaje de los 49 estudios cualitativos o mixtos que declara cada perfil.
- **Datos a dibujar:** TEA, n=33, 67%; DI, n=25, 51%; dificultades de aprendizaje, n=25, 51%; dislexia, n=20, 41%; discapacidad cognitiva (término genérico), n=16, 33%; TDAH, n=13, 27%; síndrome de Down, n=8, 16%.
- **Ejes:** Y, perfil declarado en orden descendente por n (TEA arriba); X, porcentaje de estudios, escala lineal de 0 a 100%.
- **Etiquetas sobre los datos:** `X% (n=Y)` al final de cada barra, p. ej. «67% (n=33)».
- **Leyenda:** sin leyenda (una sola serie).
- **Título interno del gráfico:** ninguno; el título es el de la figura.
- **Nota del gráfico:** «Los porcentajes no suman 100%: un estudio puede declarar más de un perfil (base n = 49 estudios cualitativos o mixtos)».
- **Estilo:** azules sobrios en un solo tono, orden descendente por n (el empate entre DI y dificultades de aprendizaje mantiene el orden de la tabla), 16 × 9 cm.

La distribución es homogénea entre los dos tipos de estudio. El TEA es el perfil más declarado tanto en los 30 estudios cualitativos (n=20) como en los 19 mixtos (n=13), y el síndrome de Down, el menos declarado en ambos grupos (n=5 y n=3). Los perfiles intermedios cambian como mucho un puesto de un grupo a otro. Los 24 estudios cuantitativos no registran este ítem, porque el formulario solo lo recoge en la hoja cualitativa.
<!-- fin -->

## Decisiones

- **Recodificación hecha (`codificacion/RQ1-I1.jsonl`): 49 de 49 filas con `auto: false`.**
  - Se quita «Neurodivergencia» de las 49 filas. Está en el valor bruto de todas, así que no discrimina. Además, todos los MD llevan el encabezado de plantilla «Theme relevance: cognitive accessibility and neurodiversity», de modo que tampoco sirve como evidencia de texto.
  - **R106**, el único que solo declaraba neurodivergencia, no pasa a «Sin perfil específico», como preveía el plan, sino a TEA, DI y discapacidad cognitiva. La razón es que el MD lo desmiente: «personas con discapacidad cognitiva respondieron al cuestionario… mayoría de participantes eran personas con discapacidad intelectual (79%)», y los adaptadores incluyen TEA. La evidencia queda en la fila. Así, «Sin perfil específico» tiene n=0 y no se usa. Me aparto del plan con evidencia y lo dejo a juicio del crítico.
  - **Discapacidad cognitiva añadida en R880, R391, R317 y R587.** Los cuatro usan el término genérico para su población destinataria («individuals with cognitive disabilities», «intellectual and cognitive disabilities»). La extracción no lo había registrado, y aplicar la definición del codebook de forma coherente lo exige. La evidencia está en cada fila.
  - **Cotejo de las 49 filas con los MD.** Busqué cada perfil codificado en el cuerpo del MD, sin las referencias, y todos tienen al menos una mención: no hay perfiles sin apoyo en el texto. También busqué perfiles con 3 o más menciones que no estuvieran codificados. Además de los cinco casos anteriores, salió R147, con «learning disorder», pero ahí define la dislexia y no es otro perfil, así que no lo añado.
- **DI frente a discapacidad cognitiva:** no se fusionan. El valor bruto y el texto los distinguen: 12 estudios llevan solo DI, 3 solo el término genérico y 13 los dos. Las definiciones están en `codebook.md` (`## RQ1-I1`), y RQ2-B2 hereda esta codificación limpia, sin la etiqueta paraguas.
- **Cifras:** todas salen de `tablas/RQ1-B1.json`, con base 49 (`items_meta.RQ1-I1.n_base`). El «80% (n=39)» de dos o más perfiles se obtiene contando, para cada estudio, en cuántas listas `estudios` de esa misma tabla aparece: 39 de 49 están en dos o más, 10 en una sola. La homogeneidad se basa en `por_naturaleza`.
- **Presentación:** una figura de barras horizontales, como se acordó en el plan. No hay tabla, para no repetir los mismos datos. La etiqueta paraguas solo aparece en una frase («Todos describen a su población como neurodivergente…»).
- **Spec:** `graficos/RQ1-B1.spec.json`, con los `n` iguales a la tabla.
