# B00-muestra — Ronda 1 — Defensor

## Texto propuesto

<!-- inicio -->
### 3.5. Tamaño de las muestras

Del total de 73 artículos seleccionados, el 70% (n=51) reporta el número de participantes humanos, el 21% (n=15) no incluye participantes humanos, el 5% (n=4) no reporta el tamaño de la muestra y el 4% (n=3) declara una muestra no humana, compuesta por respuestas generadas, textos o sesiones. En los 51 estudios con participantes humanos, el tamaño de las muestras osciló entre 1 y 1 536 participantes, con una mediana de 14 participantes. De los 15 estudios sin participantes humanos, 13 figuran en el formulario de extracción como revisión bibliográfica sin muestra empírica y 2 como evaluaciones técnicas sobre corpus o herramientas.
<!-- fin -->

## Decisiones

- **Presentación:** texto, como acordó `bloques.json` («Rango y mediana; basta el texto»). Sigue el ejemplo «Descripción general de la muestra» del playbook, que reporta proporciones y rango sin tabla.
- **Base:** N = 73 estudios incluidos para las cuatro categorías (51 + 15 + 4 + 3 = 73; 70% + 21% + 5% + 4% = 100%), en orden descendente por n. El rango y la mediana se calculan sobre los 51 estudios con participantes humanos. Recalculé desde `matriz.json`: mínimo 1, máximo 1536, mediana 14 (la mediana pasa a 13 si se suman las 3 muestras no humanas, que por eso quedan fuera). Cifras de `tablas/B00-muestra.json`.
- **Última oración (dato dudoso declarado sin interpretar):** como el bloque no tiene tabla y por tanto no hay *Nota.*, la declaración va en el texto. Desglose en `muestra_raw`: 13 registros con «Revisión bibliográfica (sin n empírico)» (si_order 10, 14, 15, 20, 21, 26, 27, 38, 40, 45, 60, 64, 73) y 2 evaluaciones técnicas (35: Simple.Text; 63: EASIER sobre corpus). Si el crítico prefiere la caracterización sin esta oración, puede pasar a una *Nota.* si el bloque se reconvierte en tabla.
- **Verificación en el MD (no se cambia el Excel; para el crítico y el orquestador):**
  - R208 (si_order 14): el MD dice «participatory needs assessment and message testing with five adults with intellectual and developmental disabilities». Está registrado como revisión sin n, pero tiene 5 participantes humanos.
  - R396 (si_order 38): «experimental comparison involving eight participants (aged 20–45)». Está registrado como revisión sin n, pero tiene 8 participantes.
  - R647 (si_order 64): el MD describe talleres de codiseño con padres, expertos y diseñadores, sin un n declarado.
  - R263 (si_order 19): está registrado como «n = 000 participantes» y por eso se cuenta en «No reportado», pero el MD declara «No human participants or animals were involved in this study», así que correspondería a «Sin participantes humanos».
  - R595 (si_order 55, «n = 1») y R663 (si_order 65, «n = 10»): el registro no tiene unidad y están clasificados como muestra no humana.
  - Con estos registros, la etiqueta «revisión bibliográfica» parece un rótulo de extracción para «sin n de usuarios», no un diseño secundario (CE). Los B00 no se recodifican: lo dejo declarado para que el orquestador decida si se corrige el formulario en otra versión.
- **Heterogeneidad (propuesta, no incluida en el texto):** el 47% (24 de 51) de las muestras humanas tiene 10 participantes o menos y 6 superan los 100. Ese desglose no está en `tablas/B00-muestra.json`; si el crítico lo pide, habría que agregarlo primero en la tabla para no introducir cifras que no salen de ella.
