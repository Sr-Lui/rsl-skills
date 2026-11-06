# B00-anio — Ronda 2 — Defensor

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | El periodo 2021–2027 sin vínculo con CI1 («publicados entre 2021 y 2026») se lee como un estudio fuera del criterio temporal | Acepto. El dato no se recodifica (año del volumen en la base de datos; MD: «Int. J. Human–Computer Studies 218 (2027)», «Accepted 3 September 2026»), pero la *Nota.* debe vincularlo al criterio | *Nota.* de la figura, «Nota del gráfico» y `nota` de la spec: «El año 2027 es el del volumen asignado por la base de datos a un artículo aceptado en 2026, dentro del criterio temporal 2021–2026». Texto y cifras sin cambios |

## Texto propuesto

<!-- inicio -->
### 3.1. Frecuencia de publicaciones por año

Tras la aplicación de los criterios de inclusión y exclusión, se seleccionaron 73 artículos científicos, publicados entre 2021 y 2027. Como se observa en la Figura {{F1}}, el 3% (n=2) se publicó en 2021, el 4% (n=3) en 2022, el 5% (n=4) en 2023, el 22% (n=16) en 2024, el 29% (n=21) en 2025, el 36% (n=26) en 2026 y el 1% (n=1) en 2027. Se observa un pico de producción científica en el año 2026.

**Figura {{F1}}**

*Distribución de los estudios por año de publicación*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los 73 artículos seleccionados (2021–2027). El año 2027 es el del volumen asignado por la base de datos a un artículo aceptado en 2026, dentro del criterio temporal 2021–2026.

#### Detalle gráfica (Figura {{F1}})

- **Tipo:** barras verticales.
- **Por qué este tipo:** muestra un cambio en el tiempo con una sola serie de siete años discretos; las barras permiten comparar la frecuencia de cada año sin sugerir continuidad entre años con pocos estudios.
- **Qué muestra:** el porcentaje de los 73 estudios incluidos publicado en cada año entre 2021 y 2027.
- **Datos a dibujar:** 2021: n=2 (3%); 2022: n=3 (4%); 2023: n=4 (5%); 2024: n=16 (22%); 2025: n=21 (29%); 2026: n=26 (36%); 2027: n=1 (1%).
- **Ejes:** X = año de publicación, en orden cronológico (2021 a 2027); Y = porcentaje de estudios (%), escala lineal de 0 a 40%, marcas cada 10%.
- **Etiquetas sobre los datos:** `X% (n=Y)` sobre cada barra (p. ej., «36% (n=26)» sobre 2026).
- **Leyenda:** sin leyenda (una sola serie).
- **Título interno del gráfico:** ninguno (se usa el título de la figura).
- **Nota del gráfico:** base N = 73 estudios incluidos. El año 2027 es el del volumen asignado por la base de datos a un artículo aceptado en 2026, dentro del criterio temporal 2021–2026.
- **Estilo:** azules sobrios, un solo tono para todas las barras; orden cronológico; 16 × 9 cm.
<!-- fin -->

## Decisiones

- Cifras sin cambios: salen de `tablas/B00-anio.json` (2/3/4/16/21/26/1; N = 73).
- `graficos/B00-anio.spec.json`: solo cambia `nota`; los datos, `n` y orden se mantienen.
