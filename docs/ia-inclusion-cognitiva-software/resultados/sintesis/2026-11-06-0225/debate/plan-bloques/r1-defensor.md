# Plan de bloques — Ronda 1 — Defensor

**Modo:** sintesis-bloques · **Corpus:** 73 estudios (49 en la hoja Cualitativo, 43 en la hoja Cuantitativo y 19 mixtos en ambas) · **Validación:** `sintesis:aggregate all` OK (11 bloques RQ → `tablas/`).

Los cinco B00 (año, enfoque, tipo, país y muestra) se conservan sin cambios: su presentación ya sigue las reglas (la figura para el cambio en el tiempo y la tabla para el país; el resto, con pocas categorías, en texto).

## Bloques RQ propuestos

| Id | Ítems | Agregación | Síntesis | Presentación | Motivo |
|---|---|---|---|---|---|
| RQ1-B1 | RQ1-I1 | frecuencia | aditiva | figura | 8 categorías multivalor; barras horizontales con X% (n=Y) |
| RQ1-B2 | RQ1-I2 + RQ1-I3 | frecuencia | aditiva | tabla | Pocas categorías por subcampo y bases distintas (43 y 73), declaradas por fila |
| RQ1-B3 | RQ1-I4 | frecuencia | aditiva | tabla | Plantilla de 4 subcampos agrupados en una sola tabla |
| RQ2-B1 | RQ2-I1 | frecuencia | aditiva | tabla | Dos grupos (familia y modelo nombrado) de tamaño medio |
| RQ2-B2 | RQ1-I1 × RQ2-I1 (`_registro`) | cruce | argumental | figura | Relación entre dos nominales multivalor (8×6, base n=42); mapa de calor |
| RQ2-B3 | RQ2-I2 | frecuencia | aditiva | lista | Tres roles, cada uno con un hallazgo que describir |
| RQ2-B4 | RQ2-I3 + RQ2-I4 | frecuencia | aditiva | figura | Misma base (n=43) y mismas fases en dos series; barras agrupadas |
| RQ3-B1 | RQ3-I1 (`Constructo`) | frecuencia | aditiva | tabla | Categorías medias con valores numéricos en una columna de hallazgo |
| RQ3-B2 | RQ3-I2 | frecuencia | aditiva | lista | Cuatro instrumentos con descripción de qué miden |
| RQ3-B3 | RQ3-I3 + RQ3-I4 | frecuencia | aditiva | texto | Una o dos categorías por ítem; basta el texto |
| RQ3-B4 | RQ2-I3 × RQ3-I5 | cruce | argumental | tabla | Contingencia pequeña (4×2, base n=34) con la fase como factor a la izquierda |

Los 13 ítems quedan cubiertos: RQ1-I1 y RQ2-I1 aparecen dos veces (frecuencia propia y cruce), y RQ2-I3 aparece en RQ2-B4 y en el cruce RQ3-B4. Los dos cruces tienen exactamente 2 ítems con estudios en común: RQ2-B2 usa 49 estudios de la hoja Cualitativo, de los que quedan 42 tras excluir 7 NR de familia, y RQ3-B4 usa 43 de la hoja Cuantitativo, de los que quedan 34 con dato en ambos.

## Justificación de cada agrupación

- **RQ1-B1 (perfiles).** Responde la primera mitad de la RQ1 («qué perfiles»). Se presenta solo porque su frecuencia es la base de todo lo demás y porque el cruce RQ2-B2 la reutiliza.
- **RQ1-B2 (estratificación + participación).** La RQ1 pregunta literalmente por el «grado de estratificación y participación de usuarios». Juntar ambos ítems en una tabla muestra el contraste entre los estudios que incluyen a personas con la condición y los pocos que desagregan resultados por perfil. Las bases son distintas (43 y 73) y se declaran en la tabla. No se cruzan porque solo comparten 43 estudios y RQ1-I3 no discrimina en presencia.
- **RQ1-B3 (marco ético).** Cubre el enfoque de diferencia o de déficit, el tratamiento del perfil y el consentimiento que exige el protocolo. Se presenta sin `campos` para conservar los cuatro subcampos. El país de RQ1-I4 se refiere al lugar del estudio y no a la afiliación usada en B00-pais; si coincide, se remite a 3.1 y no se repite.
- **RQ2-B1 (familias y modelos).** Da la frecuencia completa de RQ2-I1, con las familias y los modelos nombrados, para responder «qué técnicas».
- **RQ2-B2 (perfil × familia de IA).** Es el cruce que más aporta al objetivo, porque vincula la población (P) con la intervención (I) y muestra qué técnicas se aplican a qué perfil. Usa `_registro` para excluir «Modelo: …». Es argumental porque cada estudio cubre una parte de la matriz.
- **RQ2-B3 (rol de la IA).** Responde «con qué rol». Se presenta solo porque sus tres categorías no discriminan lo bastante para un cruce útil.
- **RQ2-B4 (fase principal + otras fases).** Responde «en qué fase». Ambos ítems tienen la misma base y las mismas categorías, así que la figura agrupada compara en qué fase se concentra la técnica y qué fases se abordan de forma secundaria.
- **RQ3-B1 (métricas).** Usa el subcampo `Constructo`; los valores numéricos (`Valor`) van en la columna de hallazgo y en el texto.
- **RQ3-B2 (instrumentos).** Responde con qué se mide. Con cuatro categorías, la lista por categoría sigue el ejemplo del playbook.
- **RQ3-B3 (marco normativo + cobertura).** Juntos responden la segunda parte de la RQ3: COGA frente a WCAG y el contraste cognitivo frente a sensorial. Las bases (49 y 43) se declaran por separado.
- **RQ3-B4 (fase × automatización).** La RQ3 pide el «grado de automatización». Cruzarlo con la fase principal muestra si la automatización se concentra en pruebas o en desarrollo. En la tabla agregada predomina la validación con usuarios en todas las fases. RQ3-I5 queda cubierto aquí con su frecuencia propia (base 43, con 7 NR).

## Objeciones previsibles del crítico

1. **Sesgos del registro (playbook §8).** «Neurodivergencia» aparece en 49 de 49 estudios (RQ1-I1), «COGA» en 49 de 49 (RQ3-I3), «Ambas» en 41 de 43 (RQ3-I4), «Pruebas» en 43 de 43 (RQ2-I4) y los tres roles de RQ2-I2 en 45 a 49 de 49. Ninguna de estas categorías discrimina. «Neurodivergencia» parece una etiqueta paraguas añadida por la codificación automática; propongo excluirla de RQ1-B1 y de la fila del cruce RQ2-B2 en `codificacion/RQ1-I1.jsonl` (con `auto: false`) en el debate del bloque. En RQ3-I3, el valor bruto («COGA. Alineación con accesibilidad cognitiva.») se repite literal, así que hay que verificarlo frente al MD antes de redactar. Estos sesgos no cambian la agrupación, solo la codificación.
2. **Categorías genéricas.** «Constructo: Métrica reportada» (39 de 73) en RQ3-I1, «IA» (1) y «Modelo: Llamada» (probable Llama) en RQ2-I1 deben recodificarse en el debate de cada bloque.
3. **RQ2-I4 duplica la fase principal**, en contra de la regla del registro. Si se confirma, la figura de RQ2-B4 debe restar la fase principal de cada estudio antes de comparar las series.
4. **¿Por qué no cruzar el perfil con el rol de participación (RQ1-I1 × RQ1-I3)?** Es una alternativa válida, pero el rol de participación tiene dos categorías (Evaluación y Ambos) que cubren 72 de 73 estudios, y el cruce aportaría poco frente a RQ2-B2. Queda abierta si el crítico la considera necesaria.

## Límite honesto de la defensa

Las frecuencias salen de la codificación automática sin revisar. Varios ítems tienen sesgos de extracción que pueden vaciar de contenido RQ3-B3 y RQ2-B3 (ítems casi saturados). La agrupación se sostiene, pero el valor analítico de esos bloques depende de recodificarlos desde el valor bruto en las rondas del bloque.
