# B00-muestra — Ronda 3 (final) — Defensor

| # | Objeción R2 | Propuesta de consenso |
|---|---|---|
| 1 | «el 21% (n=15) no incluye participantes humanos» contradice RQ1-B2: seis de esos 15 (si_order 10, 14, 26, 38, 60 y 64) figuran con «Presencia: Sí» en RQ1-I3 | **Acepto.** Verificado en `tablas/RQ1-B2.json`: los seis están en «Presencia: Sí» y en la lista «sin participantes» de `tablas/B00-muestra.json`. Las cifras no cambian (n=15; 21%), pero las cuatro categorías se redactan como lo que son, registros del formulario: «el 21% (n=15) figura en el formulario sin participantes humanos registrados». Las otras categorías siguen la misma lógica («registra el número de participantes», «no registra el tamaño de la muestra»), y el rango y la mediana se refieren a los «51 estudios con número de participantes registrado» |
| 2 | La discrepancia va en la prosa como si fuera un hallazgo, debe ir en una *Nota.* y avisar del choque con la sección de participación (RQ1) | **Acepto.** Se retira la oración del párrafo y se añade la *Nota.* bajo el párrafo, con la redacción del crítico. Se mantiene la presentación en texto, conforme a `bloques.json`: el lint solo exige *Nota.* en las tablas y figuras y no prohíbe una nota bajo un párrafo, así que no hace falta una tabla de cuatro filas que repetiría las cifras del texto |

**Desacuerdo de fondo residual:** ninguno. La corrección de la fila 13 del formulario (los siete registros verificados en el MD en R2) queda escalada al orquestador para una nueva versión del formulario seguida de `sintesis:general`. Si se aplica, el párrafo se rehace con las cifras nuevas y la *Nota.* se retira.

## Texto propuesto

<!-- inicio -->
### 3.5. Tamaño de las muestras

Del total de 73 artículos seleccionados, el 70% (n=51) registra el número de participantes humanos, el 21% (n=15) figura en el formulario sin participantes humanos registrados, el 5% (n=4) no registra el tamaño de la muestra y el 4% (n=3) registra un tamaño de muestra cuya unidad no son participantes humanos o no se especifica. En los 51 estudios con número de participantes registrado, el tamaño de las muestras osciló entre 1 y 1 536 participantes, con una mediana de 14 participantes.

*Nota.* Las categorías proceden del registro de muestra del formulario de extracción. En al menos siete estudios, ese registro no coincide con el tamaño declarado en el texto completo, y seis de los registrados sin participantes humanos figuran con participación de personas con la condición en la sección de participación (RQ1).
<!-- fin -->

## Decisiones

- **Cifras:** sin cambios, de `tablas/B00-muestra.json` (51/15/4/3; 70%/21%/5%/4%; rango 1–1 536; mediana 14; N = 73).
- **Coherencia con RQ1-B2:** la *Nota.* remite a la sección de participación (RQ1), donde las cifras de presencia verificadas (`tablas/RQ1-B2.json`, RQ1-I3) son la referencia para la participación humana. La sección 3.5 no afirma que un estudio carezca de participantes.
- **Presentación:** texto con *Nota.* al pie. No se edita `bloques.json`.
