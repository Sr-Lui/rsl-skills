# Plan de bloques — Ronda 2 — Defensor

**Alcance.** Este debate decide qué bloques hay y cómo se presentan. La recodificación concreta (con `auto: false` en `codificacion/*.jsonl`) se hace en el debate de cada bloque. Cada bloque con sesgo del registro lleva en `bloques.json` un campo `plan_recodificacion` que dice qué se recodifica y cómo: de forma determinista desde `matriz.json`, verificando contra el MD del estudio (`RSL/picoc/2026-10-03-3-cribado-2-PIO/docs/md/<Id>-*.md`) o, si no es verificable, declarando la limitación en la *Nota.* sin reportar porcentajes saturados como hallazgo.

**Validación:** `sintesis:aggregate all` OK, con 11 bloques RQ. Las tablas actuales siguen siendo las de la codificación automática y se regeneran tras la recodificación de cada bloque.

## Respuesta punto por punto

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | «Neurodivergencia» (49/49) está en el valor bruto, no la añade la codificación; DI frente a discapacidad cognitiva | **Acepto.** Mi afirmación de R1 era incorrecta: la etiqueta está en el valor bruto | RQ1-B1 · `plan_recodificacion`: se quita la etiqueta paraguas, que se menciona en una frase; el estudio que solo la declara pasa a «Sin perfil específico» (n=1); DI y discapacidad cognitiva se definen en el codebook y se fusionan si el valor no las distingue. La figura se mantiene |
| 2 | «Presencia: Sí» 72/73 contradice B00-muestra; N no se agrega | **Acepto.** `matriz.json` lo confirma: 15 «sin_participantes», 3 «otro» (p. ej. «240 respuestas generadas») y 4 «nr» | RQ1-B2 · recodificación determinista desde `muestra.tipo` y `muestra_raw`; los «nr» se verifican en el MD; Rol solo con presencia real; rango y mediana de N de personas con la condición, separados de B00-muestra |
| 3 | País de RQ1-I4 discrepa de B00-pais en 53/73 | **Acepto.** No se publican dos distribuciones geográficas | RQ1-B3 · País sale de la tabla, que queda con enfoque, perfil y consentimiento; la *Nota.* remite a 3.1, salvo que el MD confirme el país del estudio frente al de la afiliación |
| 4 | «Modelo: NR» como fila; «IA» genérica; «Llamada» | **Acepto** | RQ2-B1 · «Modelo: NR» pasa a la *Nota.*; la tabla separa los grupos Familia y Modelo; «Llamada» se recodifica como Llama y la familia «IA» se asigna a una familia concreta o a NR, ambas tras verificar en el MD |
| 5 | La fila Neurodivergencia reproduce el marginal; la columna IA tiene n=1; motivo incoherente (8×6 frente a 8×5); se repiten los marginales | **Acepto** | RQ2-B2 · matriz de 7×5 (sin la fila paraguas ni la columna IA, herencia de las objeciones 1 y 4); motivo unificado; la prosa cita solo la matriz y remite a RQ1-B1 y RQ2-B1 para los marginales; la base se recalcula |
| 6 | RQ2-I2: 44/49 valores son la plantilla copiada; la lista no tiene qué describir | **Acepto** | RQ2-B3 · de `lista` a `texto`; verificación del rol por estudio en el MD y en el grafo cribado-2 (qué genera, qué evalúa, si asiste al aseguramiento de la calidad); si no se verifica, la limitación va en la *Nota.* sin porcentajes saturados |
| 7 | RQ2-I4 repite la fase principal en 36/41; no hay «—» | **Acepto.** Es la sospecha que dejé abierta en R1 | RQ2-B4 · recodificación determinista que resta la fase de RQ2-I3 y añade «Solo una fase»; la figura usa la unión de fases (Requisitos con 0 en la serie principal); sin recodificación no hay figura y el bloque pasa a tabla con la limitación |
| 8 | «Métrica reportada» 39/73 no es un constructo; los valores de accuracy no son proporciones; legibilidad frente a Flesch | **Acepto** | RQ3-B1 · «Métrica reportada» pasa a constructo no especificado en la *Nota.* (base de constructos n=34); sin columna de valor numérico salvo verificación en el MD; Flesch y Flesch-Kincaid pasan a «Legibilidad (índice)», con un codebook común con RQ3-I2 |
| 9 | La lista de RQ3-B2 no tiene hallazgo por categoría; «Legibilidad» no es un instrumento | **Acepto** | RQ3-B2 · de `lista` a `texto` con X% (n=Y); «Legibilidad» se renombra «Índice de legibilidad», con el codebook común con RQ3-B1; vuelve a lista solo si las notas del MD dicen qué mide cada instrumento |
| 10 | RQ3-I3 tiene un único valor bruto (COGA 49/49) y RQ3-I4 repite «Ambas» 41/43 | **Acepto, con evidencia adicional.** Un sondeo de los 73 MD halla «COGA» en 4 y «WCAG» en los 73, así que el registro queda refutado y la verificación es factible | RQ3-B3 · verificación por estudio (WCAG, COGA, W3C, «cognitive accessibility», «Making Content Usable»), que distingue la adscripción al marco de la mera mención en antecedentes o referencias; RQ3-I4 se revisa con la misma lectura; sin verificación no se reporta el 100% ni el 95%. Presentación en texto |
| 11 | El cruce fase × automatización no discrimina (31/34) y tiene sesgo en la columna dominante | **Acepto** | Se elimina el cruce. El nuevo RQ3-B4 es la frecuencia de RQ3-I5 en texto, con los 5 estudios «sin_participantes» recodificados desde `matriz.json` y el MD; la frase sobre la fase solo se incluye si la tabla recodificada muestra diferencias. RQ2-I3 sigue cubierto en RQ2-B4 |
| 12 | No se declara dónde se integran lo cualitativo y lo cuantitativo | **Acepto** | Campo `integracion` en el bloque de cierre de cada RQ: en RQ1-B3, RQ1-I1 con RQ1-I2; en RQ2-B4, RQ2-I1 y RQ2-I2 con RQ2-I3 y RQ2-I4; en RQ3-B4, RQ3-I2 y RQ3-I3 con RQ3-I4 y RQ3-I5 (RQ3-I1, mixto, hace de puente). Las tres integraciones usan los 19 estudios mixtos comunes |

**Aceptadas: 12 de 12.** No justifico en contra ninguna: las doce se comprobaron en `codificacion/*.jsonl` y `matriz.json`, y la 10 también con el sondeo de los MD.

## Alerta fuera del alcance de este debate

`muestra_raw` dice «Revisión bibliográfica (sin n empírico)» en 12 de los 73 estudios incluidos. Si son revisiones, chocan con el criterio de exclusión de estudios secundarios del picoc; si no, es un error de extracción de la muestra. El orquestador debe decidir si se revisa antes de redactar B00-muestra y RQ1-B2. Este plan no lo resuelve.

## Tabla final de bloques

| Id | Ítems | Agregación | Síntesis | Presentación | Motivo | Recodificación previa |
|---|---|---|---|---|---|---|
| RQ1-B1 | RQ1-I1 | frecuencia | aditiva | figura | 7 perfiles específicos multivalor; barras horizontales | Quitar la etiqueta paraguas; «Sin perfil específico»; DI frente a discapacidad cognitiva |
| RQ1-B2 | RQ1-I2 + RQ1-I3 | frecuencia | aditiva | tabla | Subcampos con bases distintas (43 y 73); rango y mediana de N | Presencia y Rol desde `muestra`; los «nr» se verifican en el MD |
| RQ1-B3 | RQ1-I4 | frecuencia | aditiva | tabla | Enfoque, perfil y consentimiento; País se remite a 3.1 | Quitar «País: …» salvo verificación · **cierre RQ1:** integra I1 con I2 |
| RQ2-B1 | RQ2-I1 | frecuencia | aditiva | tabla | Grupos Familia y Modelo; «Modelo: NR» en la *Nota.* | «Llamada» pasa a Llama; «IA» a una familia concreta o a NR |
| RQ2-B2 | RQ1-I1 × RQ2-I1 (`_registro`) | cruce | argumental | figura | Matriz de 7×5; mapa de calor; marginales remitidos | Hereda RQ1-B1 y RQ2-B1; la base se recalcula |
| RQ2-B3 | RQ2-I2 | frecuencia | aditiva | texto | Tres roles; limitación en la *Nota.* si no se verifica | Verificación del rol en el MD y el grafo |
| RQ2-B4 | RQ2-I3 + RQ2-I4 | frecuencia | aditiva | figura | Dos series sobre la unión de fases; barras agrupadas | Restar la fase principal; «Solo una fase» · **cierre RQ2:** integra I1 e I2 con I3 e I4 |
| RQ3-B1 | RQ3-I1 (`Constructo`) | frecuencia | aditiva | tabla | Base de 34 constructos especificados; sin columna de valor | «Métrica reportada» pasa a NR; Flesch a legibilidad (índice) |
| RQ3-B2 | RQ3-I2 | frecuencia | aditiva | texto | Cuatro categorías sin hallazgo descriptivo | «Índice de legibilidad», con codebook común |
| RQ3-B3 | RQ3-I3 + RQ3-I4 | frecuencia | aditiva | texto | Sin porcentajes saturados si no se verifica | Verificación en el MD (COGA en 4 de 73, WCAG en 73 de 73) |
| RQ3-B4 | RQ3-I5 | frecuencia | aditiva | texto | Dos o tres categorías con 7 NR | 5 «sin_participantes» pasan a NR o semiautomática · **cierre RQ3:** integra I2 e I3 con I4 e I5 |

Los 13 ítems quedan cubiertos. Queda un único cruce (RQ2-B2) y RQ2-I3 se cubre en RQ2-B4.

## Límite honesto de la defensa

Cuatro bloques (RQ2-B3, RQ3-B3, la parte de País de RQ1-B3 y la columna de valor de RQ3-B1) dependen de una verificación contra el MD que todavía no está hecha. El sondeo de términos solo prueba que el registro de RQ3-I3 es falso, no cuál es la cifra correcta. Si esa verificación no se completa, esos bloques solo informarán la limitación del registro.
