# RQ2-B1 — Ronda 1 — Defensor

Propongo una tabla con dos grupos, familias de técnica y modelos nombrados, sobre la base de 49 estudios cualitativos o mixtos. El plan pedía tres cambios: tratar «Modelo: NR» como NR del subcampo, corregir «Modelo: Llamada» y concretar la familia genérica «IA». Al verificarlos en el texto completo salieron más errores del registro en la familia y en el modelo, así que comprobé las 49 filas en el cuerpo de cada MD (sin el bloque «Relevance hooks» ni las referencias).

## Texto propuesto

<!-- inicio -->
### 3.?. Familias de técnicas de inteligencia artificial y modelos reportados (RQ2)

La técnica de inteligencia artificial (IA) se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos), y se verificó en el texto completo de cada uno qué técnica aplica el estudio en su artefacto o en su procedimiento. La Tabla {{T1}} resume las familias de técnica y los modelos que los estudios nombran. Los modelos de lenguaje grandes (LLM) se reportan en el 49% (n=24) de los estudios y el procesamiento del lenguaje natural o del habla distinto de un LLM, en el 35% (n=17). El aprendizaje automático clásico aparece en el 20% (n=10), el aprendizaje profundo en el 18% (n=9) y la visión por computador o los modelos de imagen en el 16% (n=8). El 14% (n=7) no aplica ninguna técnica de IA; cuando la menciona, lo hace en los antecedentes, como trabajo futuro o como percepción de los participantes. Además, el 39% (n=19) combina dos o más familias.

El 37% (n=18) nombra al menos un modelo concreto, y el 49% (n=24) aplica una técnica sin nombrar el modelo. Los modelos de la serie GPT de OpenAI son los más nombrados: alguna de sus versiones o ChatGPT aparece en el 29% (n=14). GPT-4o se nombra en el 10% (n=5), GPT-4 en el 8% (n=4) y GPT-3.5 en el 6% (n=3). BERT, CLIP, DeepSeek y ChatGPT sin versión indicada se nombran cada uno en el 4% (n=2). Otros once modelos aparecen en un solo estudio cada uno.

**Tabla {{T1}}**

*Familias de técnicas de inteligencia artificial y modelos nombrados en los estudios*

| Grupo | Categoría | Descripción | Frecuencia (n) | Porcentaje |
|---|---|---|---|---|
| **Familia de técnica** | LLM | Chatbots y generación, reescritura o simplificación de texto con un modelo generativo | 24 | 49% |
| | Procesamiento del lenguaje natural o del habla | Reglas lingüísticas, análisis sintáctico, simplificación léxica y reconocimiento de voz | 17 | 35% |
| | Aprendizaje automático | Clasificadores, agrupamiento, regresión y aprendizaje federado o por refuerzo | 10 | 20% |
| | Aprendizaje profundo | Redes neuronales, *autoencoders*, *transformers* y BERT | 9 | 18% |
| | Visión por computador o modelos de imagen | Reconocimiento facial o de gestos, codificación y generación de imágenes | 8 | 16% |
| **Modelo nombrado** | GPT-4o | Modelo de OpenAI | 5 | 10% |
| | GPT-4 | Modelo de OpenAI | 4 | 8% |
| | GPT-3.5 | Modelo de OpenAI | 3 | 6% |
| | BERT | Codificador de lenguaje | 2 | 4% |
| | CLIP | Codificador de imagen y texto | 2 | 4% |
| | DeepSeek | Modelo de lenguaje | 2 | 4% |
| | ChatGPT (versión no indicada) | Servicio de OpenAI sin versión declarada | 2 | 4% |
| | Otros | Claude, Gemini, LaMDA, Hunyuan, GPT-3, DALL-E, API de imágenes de OpenAI, OTTER, ImageBind, GIT y KOSMOS-2 | 1 cada uno | 2% cada uno |

*Nota.* Datos extraídos de los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados. Un estudio puede reportar más de una familia y más de un modelo, por lo que los porcentajes no suman 100%. El 49% (n=24) aplica una técnica sin nombrar el modelo y el 14% (n=7) no aplica ninguna técnica de IA; ambos grupos no figuran como filas.

Los resultados son heterogéneos entre los estudios cualitativos y los mixtos. Los LLM se reportan en el 60% (18 de 30) de los cualitativos y en el 32% (6 de 19) de los mixtos. En cambio, el aprendizaje automático aparece en el 7% (2 de 30) de los cualitativos frente al 42% (8 de 19) de los mixtos, el aprendizaje profundo en el 10% (3 de 30) frente al 32% (6 de 19) y el procesamiento del lenguaje natural o del habla en el 27% (8 de 30) frente al 47% (9 de 19). La visión por computador presenta una frecuencia similar en ambos grupos (17% y 16%). Los 24 estudios cuantitativos no registran este ítem, porque el formulario solo lo recoge en la hoja cualitativa.
<!-- fin -->

## Decisiones

- **Recodificación (`codificacion/RQ2-I1.jsonl`): 49 de 49 filas con `auto: false` y `evidencia`** (archivo MD, línea y cita breve). Las reglas y los sinónimos están en `codebook.md` (`## RQ2-I1`).
  - **«Modelo: Llamada» (R106).** No es Llama. El registro tomó «la llamada IA simbólica» (l. 600, «así llamada»). R106 combina sistemas de producción y PLN con spaCy (l. 617 y l. 845), un modelo *transformer* (l. 845) y frases de prueba «generadas automáticamente … vía ChatGPT» (l. 783). Se codifica como NLP, ML, DL y LLM, y el modelo como «ChatGPT (versión no indicada)».
  - **La familia genérica «IA» (R106)** desaparece al sustituirla por esas familias. La IA simbólica sobre texto se codifica como NLP, así que no se crea una familia nueva y la matriz de RQ2-B2 queda en 5 columnas.
  - **«Modelo: NR» → «Modelo: no nombrado».** Es el NR del subcampo. Lo mantengo como etiqueta en el jsonl para que su cifra (n=24) salga de `tablas/RQ2-B1.json`, pero no aparece como fila: va en la *Nota.*, como acordó el plan.
  - **Otros cambios de modelo verificados.** R581 usa LaMDA y no GPT-4 (l. 299). R337 nombra ChatGPT sin versión y no GPT-4 (l. 807). En R347 los modelos nombrados son herramientas de los participantes (l. 1797) o se usaron para corregir la redacción (l. 1485), así que el modelo queda como no nombrado. R394 (GPT-4, l. 370), R605 (GPT-3 y la API de imágenes de OpenAI, l. 442 y l. 460) y R705 (GPT-3.5, l. 692) nombran modelo, aunque el registro decía NR o estaba vacío. R495 nombra GPT-4o, DeepSeek-V3, Claude 3.7 Sonnet y Gemini 2.0 Flash (l. 909–911), pero el registro solo tenía Claude. R203 usa Hunyuan en el artefacto y GPT-4o en el análisis de datos. R317 y R356 usan CLIP (l. 641 y l. 379).
  - **Familias.** Se retiraron las que el registro tomó de los antecedentes o de las referencias. Por ejemplo, R263 tenía LLM porque un LLM corrigió la gramática del artículo (l. 1077), y R880 tenía visión por computador porque cita Azure como ejemplo de la industria (l. 381). Un LLM no implica NLP ni DL por sí solo.
  - **NR (7):** R197, R199, R219, R425, R600, R713 y R1061. R147, R394 y R605, que el registro dejó vacíos, tienen técnica.
- **Cifras** (todas de `tablas/RQ2-B1.json`, base 49):
  - Familias: LLM 24, NLP 17, ML 10, DL 9 y Visión 8; NR 7.
  - Modelos: «Modelo: no nombrado» 24. Los que nombran al menos un modelo son 49 − 7 − 24 = 18.
  - «Alguna versión de GPT o ChatGPT» (n=14) es la unión de las listas `estudios` de GPT-4o, GPT-4, GPT-3.5, GPT-3 y ChatGPT.
  - «Dos o más familias» (n=19) sale de contar las familias de cada estudio en esas listas: 13 tienen dos, 5 tres y 1 cuatro.
  - El reparto por naturaleza sale de `por_naturaleza`.
- **Heterogeneidad.** Uso el umbral común de 20 puntos de RQ1-B1. LLM: 28 puntos (60% frente a 32%); ML: 35; DL: 22; NLP: 20,7. Superan el umbral. Visión queda en 1 punto. El texto da las cifras sin atribuirles causa.
- **Presentación:** tabla, como se acordó. Las familias van con nombre en español y el acrónimo solo para los LLM. Los once modelos con n=1 van en una fila agrupada para no alargar la tabla; sus nombres quedan visibles.
- **Límite.** La verificación se hizo leyendo los contextos de los términos de IA en el cuerpo del MD, no el texto entero. R583 nombra siete modelos que dice usar en prototipos de laboratorio (l. 627); si el crítico pide contar solo los modelos con resultados reportados, la fila «Otros» pierde OTTER, ImageBind, GIT y KOSMOS-2, y GPT-3.5 baja a n=2.
