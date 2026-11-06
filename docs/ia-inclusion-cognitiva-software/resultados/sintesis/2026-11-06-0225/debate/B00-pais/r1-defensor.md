# B00-pais — Ronda 1 — Defensor

## Texto propuesto

<!-- inicio -->
### 3.4. Distribución geográfica de los estudios

De los 73 artículos que conformaron la muestra final, según el país de la afiliación del primer autor, el 45% (n=33) procede de Europa, el 23% (n=17) de Asia, el 18% (n=13) de América del Norte, el 7% (n=5) de Oceanía, el 5% (n=4) de América Latina y el 1% (n=1) de África. Se identifican 26 países; Estados Unidos registra el 18% (n=13), el Reino Unido el 12% (n=9) y Suiza el 8% (n=6). La Tabla {{T1}} detalla los países que integran cada continente.

**Tabla {{T1}}**

*Distribución de los estudios por continente y país de la afiliación del primer autor*

| Continente | Países (n) | Frecuencia (n) | Porcentaje |
|---|---|---|---|
| **Europa** | Reino Unido (9), Suiza (6), España (5), Italia (3), Grecia (2), Finlandia (2), Alemania (1), Países Bajos (1), Polonia (1), Portugal (1), República Checa (1), Rumanía (1) | 33 | 45% |
| **Asia** | China (5), Arabia Saudita (4), India (2), Indonesia (2), Bangladesh (1), Corea del Sur (1), Japón (1), Singapur (1) | 17 | 23% |
| **América del Norte** | Estados Unidos (13) | 13 | 18% |
| **Oceanía** | Australia (5) | 5 | 7% |
| **América Latina** | Perú (2), Argentina (1), Brasil (1) | 4 | 5% |
| **África** | Sudáfrica (1) | 1 | 1% |

*Nota.* Datos extraídos de los 73 artículos seleccionados. Cada estudio se asigna a un único país, el de la afiliación del primer autor; en 8 artículos con afiliaciones en más de un país se registró el primero. Todos los artículos tienen país identificado.
<!-- fin -->

## Decisiones

- **Presentación:** una sola tabla, como acordó `bloques.json` («Comparación simple de categorías de tamaño medio»). Fusiono las dos tablas del borrador (continente y país) en una tabla con orientación horizontal: una fila por continente y sus países con n entre paréntesis. Así se evitan una tabla de 26 filas con 14 países de n=1 y la repetición de Estados Unidos y Australia, que son el único país de su continente.
- **Base:** N = 73 estudios incluidos. Cifras de `tablas/B00-pais.json`: continentes 33 + 17 + 13 + 5 + 4 + 1 = 73 (100%); la suma de los países de cada fila coincide con la frecuencia del continente (Europa 33, Asia 17, América Latina 4). Hay 26 países (12 + 8 + 1 + 1 + 3 + 1). Orden descendente por n; los empates se ordenan alfabéticamente.
- **Verbo:** «procede de» en lugar de «se llevó a cabo en» (el ejemplo del playbook), porque el criterio es la afiliación del primer autor (`criterio` en la tabla), no el lugar del estudio.
- **Datos dudosos:** `no_identificados` está vacío, así que no hay países «No identificado». En `pais_raw` de `matriz.json`, 8 estudios declaran más de un país (si_order 2, 10, 24, 43, 49, 58, 67, 69; p. ej., «Reino Unido; Bélgica»), y se asignó el primero. Otros dos registros traen texto no normalizado, pero de un solo país («Estados Unidos (California)», «University Of Colorado Denver» → Estados Unidos), así que no cuentan como multipaís. Se declara en la *Nota.* sin interpretarlo.
- **Sin interpretación:** no se habla de concentración ni de brecha geográfica (eso va en Discusión).
