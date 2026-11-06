**En desacuerdo** (1 objeción)

# B00-anio — Ronda 1 — Crítico

Verificado: las siete cifras cuadran con `tablas/B00-anio.json` (2/3/4/16/21/26/1; suman 73 y 100%) y con `graficos/B00-anio.spec.json`; apertura con el total, pico y periodo como en el ejemplo 3.1 del playbook; el orden cronológico sigue ese ejemplo, que manda; figura citada antes, título en cursiva, *Nota.* con periodo; Detalle gráfica completa (10 campos) y coherente con la spec; sin citas ni valoraciones. Acepto que no haya tabla adicional.

| # | Fragmento | Problema | Corrección |
|---|---|---|---|
| 1 | «publicados entre 2021 y 2027» + *Nota.* «El año 2027 corresponde a la fecha del volumen de un artículo aceptado en 2026.» | El criterio CI1 del picoc vigente es «Estudios publicados entre 2021 y 2026». Un periodo 2021–2027 en Resultados, sin vínculo con CI1, se lee como un estudio incluido fuera del criterio temporal. El año 2027 viene del export de Web of Science (`resultados-PIO-cribado-2.csv`, año «2027») y el MD confirma «Accepted 3 September 2026». | Mantener el dato sin recodificarlo, pero declarar el origen en la *Nota.* (y en la `nota` de la spec y en «Nota del gráfico»): «El año 2027 es el del volumen asignado por la base de datos a un artículo aceptado en 2026, dentro del criterio temporal 2021–2026». No interpretar más allá. |
