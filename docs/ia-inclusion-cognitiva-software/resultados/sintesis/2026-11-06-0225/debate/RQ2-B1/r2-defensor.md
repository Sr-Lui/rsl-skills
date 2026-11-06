# RQ2-B1 — Ronda 2 — Defensor

Acepto las cinco objeciones. Verifiqué R453 y R583 en el MD, recodifiqué `codificacion/RQ2-I1.jsonl` (`auto: false`, evidencia añadida con la marca «(R2)») y volví a correr `sintesis:aggregate` en RQ2-B1, RQ2-B2, RQ2-B3 y RQ2-B4. Las cifras coinciden con las que anticipó el crítico.

| # | Objeción | Acepto / Justifico | Cambio |
|---|---|---|---|
| 1 | R453 es un ensayo conceptual; debe ser NR | **Acepto.** En las l. 150–156, R453 rastrea mecanismos de exclusión y propone métricas y un marco de gobernanza, sin sistema concreto ni procedimiento con IA. Lo distingo de R193, que analiza conversaciones grabadas con un altavoz concreto basado en LLM | R453 → NR. LLM 23 (47%), NLP 16 (33%), NR 8 (16%), «Modelo: no nombrado» 23 (47%), dos o más familias 18 (37%). En `codebook.md`, la regla «objeto de análisis» pasa a «sistema concreto observado» y los ensayos conceptuales quedan fuera |
| 2 | GPT-4 de R583 es antecedente; falta ViLT | **Acepto.** La l. 484 solo dice que los modelos de OpenAI están disponibles como API REST. En las l. 715–720 se lee «We implemented a prototype with two different AI models, ViLT and GIT» | Se retira «Modelo: GPT-4» y se añade «Modelo: ViLT». GPT-4 baja a 3 (6%) y «Otros» pasa a doce modelos. La unión GPT/ChatGPT sigue en 14 |
| 3 | Sobra la variante «solo con resultados» | **Acepto.** El criterio es la aplicación de la técnica, y los prototipos de laboratorio cuentan | Se suprime ese límite. La regla queda en el codebook |
| 4 | NR no equivale a ausencia de IA | **Acepto.** R197 y R600 no especifican la técnica, lo que no es lo mismo que no usar IA | Nueva fórmula en el texto, en la *Nota.* y en el codebook (la misma en RQ2-B3 y RQ2-B4) |
| 5 | Heterogeneidad desfasada | **Acepto** | LLM 57% (17 de 30) frente a 32% (6 de 19); NLP 23% (7 de 30) frente a 47% (9 de 19). Las demás no cambian |

## Texto propuesto

<!-- inicio -->
### 3.?. Familias de técnicas de inteligencia artificial y modelos reportados (RQ2)

La técnica de inteligencia artificial (IA) se registró en los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados (30 cualitativos y 19 mixtos), y se verificó en el texto completo de cada uno qué técnica aplica el estudio en su artefacto o en su procedimiento. La Tabla {{T1}} resume las familias de técnica y los modelos que los estudios nombran. Los modelos de lenguaje grandes (LLM) se reportan en el 47% (n=23) de los estudios y el procesamiento del lenguaje natural o del habla distinto de un LLM, en el 33% (n=16). El aprendizaje automático clásico aparece en el 20% (n=10), el aprendizaje profundo en el 18% (n=9) y la visión por computador o los modelos de imagen en el 16% (n=8). El 16% (n=8) no reporta una técnica de IA aplicada. En unos casos el artefacto no la especifica; en otros, la IA solo aparece en los antecedentes, como trabajo futuro, como percepción de los participantes o como objeto de un análisis conceptual. Además, el 37% (n=18) combina dos o más familias.

El 37% (n=18) nombra al menos un modelo concreto, y el 47% (n=23) aplica una técnica sin nombrar el modelo. Los modelos de la serie GPT de OpenAI son los más nombrados: alguna de sus versiones o ChatGPT aparece en el 29% (n=14). GPT-4o se nombra en el 10% (n=5) y GPT-4 y GPT-3.5 en el 6% (n=3) cada uno. BERT, CLIP, DeepSeek y ChatGPT sin versión indicada se nombran cada uno en el 4% (n=2). Otros doce modelos aparecen en un solo estudio cada uno.

**Tabla {{T1}}**

*Familias de técnicas de inteligencia artificial y modelos nombrados en los estudios*

| Grupo | Categoría | Descripción | Frecuencia (n) | Porcentaje |
|---|---|---|---|---|
| **Familia de técnica** | LLM | Chatbots y generación, reescritura o simplificación de texto con un modelo generativo | 23 | 47% |
| | Procesamiento del lenguaje natural o del habla | Reglas lingüísticas, análisis sintáctico, simplificación léxica y reconocimiento de voz | 16 | 33% |
| | Aprendizaje automático | Clasificadores, agrupamiento, regresión y aprendizaje federado o por refuerzo | 10 | 20% |
| | Aprendizaje profundo | Redes neuronales, *autoencoders*, *transformers* y BERT | 9 | 18% |
| | Visión por computador o modelos de imagen | Reconocimiento facial o de gestos, codificación y generación de imágenes | 8 | 16% |
| **Modelo nombrado** | GPT-4o | Modelo de OpenAI | 5 | 10% |
| | GPT-4 | Modelo de OpenAI | 3 | 6% |
| | GPT-3.5 | Modelo de OpenAI | 3 | 6% |
| | BERT | Codificador de lenguaje | 2 | 4% |
| | CLIP | Codificador de imagen y texto | 2 | 4% |
| | DeepSeek | Modelo de lenguaje | 2 | 4% |
| | ChatGPT (versión no indicada) | Servicio de OpenAI sin versión declarada | 2 | 4% |
| | Otros | Claude, Gemini, LaMDA, Hunyuan, GPT-3, DALL-E, API de imágenes de OpenAI, OTTER, ImageBind, GIT, ViLT y KOSMOS-2 | 1 cada uno | 2% cada uno |

*Nota.* Datos extraídos de los 49 estudios con enfoque cualitativo o mixto de los 73 seleccionados. Un estudio puede reportar más de una familia y más de un modelo, por lo que los porcentajes no suman 100%. El 47% (n=23) aplica una técnica sin nombrar el modelo y el 16% (n=8) no reporta una técnica de IA aplicada (el artefacto no la especifica o la IA solo aparece en los antecedentes, como trabajo futuro, como percepción de los participantes o como objeto de un análisis conceptual); ninguno de los dos grupos figura como fila.

Los resultados son heterogéneos entre los estudios cualitativos y los mixtos. Los LLM se reportan en el 57% (17 de 30) de los cualitativos y en el 32% (6 de 19) de los mixtos. En cambio, el aprendizaje automático aparece en el 7% (2 de 30) de los cualitativos frente al 42% (8 de 19) de los mixtos, el aprendizaje profundo en el 10% (3 de 30) frente al 32% (6 de 19) y el procesamiento del lenguaje natural o del habla en el 23% (7 de 30) frente al 47% (9 de 19). La visión por computador presenta una frecuencia similar en ambos grupos (17% y 16%). Los 24 estudios cuantitativos no registran este ítem, porque el formulario solo lo recoge en la hoja cualitativa.
<!-- fin -->

## Decisiones

- **Recodificación R2** (`codificacion/RQ2-I1.jsonl`): R453 pasa a NR. En R583 se quita GPT-4 y se añade ViLT. Las reglas del codebook (`## RQ2-I1`) se actualizan: NR, objeto de análisis y prototipos.
- **Cifras** (`tablas/RQ2-B1.json`, base 49): LLM 23, NLP 16, ML 10, DL 9, Visión 8 y NR 8; «Modelo: no nombrado» 23.
  - Estudios con al menos un modelo: 49 − 8 − 23 = 18.
  - Unión GPT/ChatGPT: 14 (lista `estudios` de GPT-4o, GPT-4, GPT-3.5, GPT-3 y ChatGPT).
  - Dos o más familias: 18 (12 con dos, 5 con tres y 1 con cuatro).
- **Heterogeneidad:** ML 35 puntos, LLM 25, NLP 24 y DL 22, todas por encima del umbral común de 20; Visión 1.
- **Arrastre.** El cambio en R453 modifica RQ2-B2 (base 40), RQ2-B3 (NR 8) y la integración de RQ2-B4. R453 es cualitativo, así que los 19 mixtos no cambian por él.
