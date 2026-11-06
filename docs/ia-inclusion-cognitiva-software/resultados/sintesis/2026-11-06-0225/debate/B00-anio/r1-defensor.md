# B00-anio — Ronda 1 — Defensor

## Texto propuesto

<!-- inicio -->
### 3.1. Frecuencia de publicaciones por año

Tras la aplicación de los criterios de inclusión y exclusión, se seleccionaron 73 artículos científicos, publicados entre 2021 y 2027. Como se observa en la Figura {{F1}}, el 3% (n=2) se publicó en 2021, el 4% (n=3) en 2022, el 5% (n=4) en 2023, el 22% (n=16) en 2024, el 29% (n=21) en 2025, el 36% (n=26) en 2026 y el 1% (n=1) en 2027. Se observa un pico de producción científica en el año 2026.

**Figura {{F1}}**

*Distribución de los estudios por año de publicación*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 73 artículos seleccionados (2021–2027). El año 2027 corresponde a la fecha del volumen de un artículo aceptado en 2026.

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** barras verticales.
- **Por qué este tipo:** muestra un cambio en el tiempo con una sola serie de siete años discretos; las barras permiten comparar la frecuencia de cada año sin sugerir continuidad entre años con pocos estudios.
- **Qué muestra:** el porcentaje de los 73 estudios incluidos publicado en cada año entre 2021 y 2027.
- **Datos a dibujar:** 2021: n=2 (3%); 2022: n=3 (4%); 2023: n=4 (5%); 2024: n=16 (22%); 2025: n=21 (29%); 2026: n=26 (36%); 2027: n=1 (1%).
- **Ejes:** X = año de publicación, en orden cronológico (2021 a 2027); Y = porcentaje de estudios (%), escala lineal de 0 a 40%, marcas cada 10%.
- **Etiquetas sobre los datos:** `X% (n=Y)` sobre cada barra (p. ej., «36% (n=26)» sobre 2026).
- **Leyenda:** sin leyenda (una sola serie).
- **Título interno del gráfico:** ninguno (se usa el título de la figura).
- **Nota del gráfico:** base N = 73 estudios incluidos; el año 2027 corresponde a la fecha del volumen de un artículo aceptado en 2026.
- **Estilo:** azules sobrios, un solo tono para todas las barras; orden cronológico; 16 × 9 cm.
<!-- fin -->

## Decisiones

- **Presentación:** figura de barras verticales, como acordó `bloques.json` («Cambio en el tiempo»). Sin tabla adicional: siete valores caben en el texto y en la figura, y duplicarlos en tabla no añade información.
- **Orden de las cifras:** cronológico, no descendente por n. El ejemplo de «Frecuencia de publicaciones por año» del playbook (que manda) recorre los años en orden; el pico se declara aparte.
- **Base:** N = 73 estudios incluidos (caracterización). Las cifras salen de `tablas/B00-anio.json`; suman 73 y 100%.
- **Dato dudoso (2027):** un estudio (si_order 71, R831) figura con año 2027. Verificado en el MD: «Int. J. Human–Computer Studies 218 (2027) 103938», «Received 9 December 2025 … Accepted 3 September 2026». El dato del Excel es correcto (año del volumen); no se cambia y se declara en la *Nota.* sin interpretarlo. El periodo se mantiene como 2021–2027.
- **Sin interpretación:** no se afirma crecimiento ni tendencia (eso va en Discusión); solo pico y periodo, como en el ejemplo.
- **Spec:** `graficos/B00-anio.spec.json` con `"figura": "{{F1}}"`, los mismos `n` que la tabla y orden cronológico (el `spec-borrador.json` traía «descendente por n» y eje X «Categoría»; se corrigen).
