# Libro de códigos — síntesis de resultados

Una sección por ítem. Cada categoría lleva su definición y los sinónimos que se traducen a ella. Las filas recodificadas a mano llevan `"auto": false` en `codificacion/<ítem>.jsonl` y, cuando se verificaron en el texto completo, `"evidencia"`.

## RQ1-I1

Perfiles de discapacidad cognitiva o neurodivergencia que el estudio declara para su población destinataria o participante. Multivalor. Base: 49 estudios (cualitativos y mixtos). Lo reutiliza el cruce RQ2-B2.

**Regla de asignación.** Un perfil cuenta solo si aparece en el cuerpo del artículo, antes de la lista de referencias, **y** se refiere a la población destinataria del artefacto o a los participantes del estudio (incluidas las comorbilidades que declaran los participantes). No cuenta si solo aparece en las referencias, en trabajos relacionados, en el nombre de otra herramienta, en la definición general de neurodivergencia o de otro perfil (p. ej., «la dislexia es una dificultad específica del aprendizaje»), en la motivación, en las limitaciones o en el trabajo futuro. Cada fila cambiada lleva en `evidencia` la línea del MD de cada categoría que se mantiene y el motivo de cada categoría que se quita.

| Categoría | Definición | Sinónimos y variantes que se traducen a ella |
|---|---|---|
| TEA | El estudio nombra el trastorno del espectro autista como perfil de su población | autismo, autista, *autism*, *autistic*, ASD, *Asperger*, espectro autista |
| DI | El estudio nombra la discapacidad intelectual como diagnóstico de su población | discapacidad intelectual, *intellectual disability*, *intellectual and developmental disabilities* (IDD), *people with ID* |
| Discapacidad cognitiva | El estudio usa el término genérico de discapacidad o deterioro cognitivo para su población, con o sin un diagnóstico concreto al lado | *cognitive disability*, *cognitive impairment*, *people with cognitive disabilities*, discapacidad cognitiva |
| TDAH | El estudio nombra el trastorno por déficit de atención, con o sin hiperactividad | ADHD, *attention deficit hyperactivity disorder*, TDA, déficit de atención |
| Dificultades de aprendizaje | El estudio nombra dificultades o trastornos del aprendizaje de forma genérica o un trastorno específico distinto de la dislexia (discalculia, disgrafía) | *learning disabilities* (LD), *learning difficulties*, *specific learning disorder* (SLD), trastorno específico del aprendizaje, discalculia |
| Dislexia | El estudio nombra la dislexia (de desarrollo o fonológica) | *dyslexia*, *dyslexic*, dislexia del desarrollo |
| Síndrome de Down | El estudio nombra el síndrome de Down | *Down syndrome*, trisomía 21 |
| Sin perfil específico | El estudio solo describe a su población con la etiqueta general de neurodivergencia o discapacidad, sin un perfil concreto | *neurodiverse students*, *students with disabilities* |

**DI frente a discapacidad cognitiva.** No se fusionan: el texto completo las distingue. DI es un diagnóstico; «Discapacidad cognitiva» es el término paraguas que usa el artículo (p. ej., en la lectura fácil, «personas con discapacidad cognitiva»). Un estudio lleva las dos cuando nombra ambas para su población (p. ej., *intellectual and cognitive disabilities*). En la codificación vigente, 10 estudios llevan solo DI, 5 solo «Discapacidad cognitiva» y 8 las dos. «*Learning disability*» en el uso británico se codifica como dificultad de aprendizaje y no como DI, salvo que el artículo nombre también la discapacidad intelectual.

**Subgrupos minoritarios de participantes.** Cuentan, igual que el resto: si el artículo da la composición de la muestra (p. ej., TEA 3% y TDA 2%), se codifican todos los perfiles que nombra. Las comorbilidades citadas en los antecedentes (con referencia) no cuentan; solo cuentan las que declaran los participantes. Una misma frase de antecedentes no puede justificar un perfil y descartar otro: en la R3, R425 pierde el TDAH, R623 pierde la dislexia y el TEA de R705 pasa a apoyarse en el caso que se da a los participantes (l. 623).

**Excluida como categoría.** «Neurodivergencia» figuraba en las 49 filas del valor bruto y como encabezado de plantilla («Theme relevance: cognitive accessibility and neurodiversity») en todos los MD, así que no discrimina entre estudios. Se quita de `categorias`. La prosa la menciona como sesgo del registro y la figura no la dibuja.

**Sin perfil específico (n=1, R527).** Su único perfil codificado (dificultades de aprendizaje) solo aparece en trabajos relacionados y referencias; el cuerpo habla de «neurodiverse students». La figura no lo dibuja y la prosa lo menciona en una frase. **RQ2-B2 debe excluir esta fila de la matriz de perfiles × familias de IA**, que se queda en 7 filas de perfil específico.

## RQ1-I2

Estratificación o desagregación de los resultados por perfil. Univalor. Base: 43 estudios (cuantitativos y mixtos).

| Categoría | Definición | Sinónimos |
|---|---|---|
| Sí | El artículo da resultados separados para grupos definidos por la condición: un perfil frente a otro, o el grupo con la condición frente a un grupo sin ella | desagregación por perfil, por subgrupo de la condición, grupo objetivo frente a grupo control |
| No | Los resultados son de la muestra global. La partición estratificada del conjunto de datos (*stratified split*, *stratified sampling*) o la estratificación por otra variable no cuentan | sin desagregación |
| NR | La celda está vacía («—») | — |

**Verificación.** Los 7 «Sí» del registro se leyeron en el MD; se mantienen 2 y pasan a «No» 5, cuya «estratificación» es la partición del conjunto de datos o falta. También se leyó una muestra de 8 «No» de estudios con participantes de varios perfiles o con un grupo control, y uno pasa a «Sí»: R617, con el grupo con DI frente al grupo control. Además, se buscaron en los 35 «No» expresiones de comparación entre grupos («compared to neurotypical», «control group», «by diagnosis»), y no apareció ningún otro caso. Los demás «No» conservan la codificación automática.

## RQ1-I3

Participación de personas **con discapacidad cognitiva o neurodivergencia** en el estudio. Plantilla `Presencia | N | Rol`. Base: 73 estudios. Las 73 filas están verificadas en el MD y llevan `evidencia`.

| Categoría | Definición |
|---|---|
| Presencia: Sí | Personas con la condición participan en este estudio (prueba, entrevista, cuestionario, codiseño u observación de uso real) |
| Presencia: No | No participan personas con la condición. Puede ser una evaluación técnica (con corpus, conjuntos de datos, simulación o respuestas generadas) o con anotadores, expertos, cuidadores o profesionales; un ensayo conceptual; participantes con una condición no cognitiva (p. ej., motora); datos de un estudio anterior, o una participación planificada a futuro |
| NR | Hay participantes, pero el artículo no declara si tienen la condición |
| Rol: Evaluación | Las personas con la condición prueban, usan o valoran el artefacto ya construido |
| Rol: Diseño | Las personas con la condición solo aportan necesidades o requisitos antes de construir el artefacto |
| Rol: Ambos | Las personas con la condición participan en el diseño (codiseño, requisitos, investigación formativa) y en la evaluación |

**Reglas.** El Rol solo se registra con «Presencia: Sí». Que haya participantes cualesquiera no basta: tienen que ser personas con la condición. El «sin_participantes» de `matriz.json` no es fiable (6 de esos 15 estudios sí tienen participantes con la condición), y tampoco lo es la plantilla del valor bruto, que decía «Presencia: Sí» en 72 de 73 filas. N no se agrega: el N de RQ1-I3 y el de `muestra_raw` discrepan en 16 de los 33 estudios con ambos valores numéricos.

## RQ1-I4

Enfoque sobre la condición, tratamiento del perfil y consentimiento. Plantilla `Enfoque | Perfil | Consentimiento` (el subcampo País se retira). Base: 73 estudios.

| Categoría | Definición |
|---|---|
| Enfoque: Diferencia | El estudio presenta la condición como una diferencia o diversidad que el software debe acomodar |
| Enfoque: Déficit | El estudio presenta la condición como un déficit o limitación que el software compensa o corrige |
| Perfil: Almacenado | El sistema guarda un perfil declarado del usuario (configuración, preferencias, diagnóstico declarado) |
| Perfil: Deducido | El sistema infiere el perfil o las necesidades a partir del comportamiento o de los datos |
| Perfil: NR | El artefacto no gestiona un perfil de usuario o el artículo no lo describe. Incluye la personalización que solo aparece en la motivación, en trabajos relacionados o como trabajo futuro, y la «adaptación» que se refiere al modelo o al texto y no al usuario. Se informa como no reportado en la *Nota.*, no como hallazgo |
| Consentimiento: Informado reportado | El artículo declara el consentimiento informado (o asentimiento) de los participantes con la condición o de sus tutores |
| Consentimiento: NR | Hay participantes con la condición, o no se descarta que los haya (RQ1-I3 «Presencia: Sí» o NR), y el artículo no informa del consentimiento. Se informa como no reportado, no como hallazgo |
| Consentimiento: No aplica | El estudio no tiene participantes con la condición (RQ1-I3 «Presencia: No»). Se deriva de RQ1-I3, aunque el artículo declare el consentimiento de otros participantes (expertos, cuidadores) |

**Verificación del perfil.** Se buscaron en los 73 MD los términos de perfil y personalización (*user profile*, *user model*, *personali[sz]*, *preferences*, *adaptive*, *customi[sz]*, perfil de usuario). Se leyeron los 32 estudios con 8 o menos menciones; 25 pasaron a «Perfil: NR», entre ellos el ensayo conceptual y los estudios basados en corpus. En la R3 se aplicó la misma regla a R263 (personalización solo como trabajo futuro) y a R337 (heurísticas, sin sistema), y quedan 27 «Perfil: NR».

**País retirado.** El subcampo País discrepa de B00-pais en 53 de 73 estudios y suele reflejar la afiliación de los autores. La distribución geográfica que se publica es la de 3.1. La etiqueta del ítem en `matriz.json` («Marco ético y país del estudio») viene del formulario y no se edita en este debate.

## RQ3-I1

Constructo de la métrica principal de evaluación (subcampo `Constructo` de la plantilla `Constructo | Valor`). Univalor. Base: 73 estudios. Lo usa RQ3-B1. Libro de códigos común con RQ3-I2 en la legibilidad.

| Categoría | Familia (Tabla) | Definición | Sinónimos y variantes que se traducen a ella |
|---|---|---|---|
| Exactitud (accuracy) | Rendimiento del modelo | Proporción de aciertos del modelo o sistema de IA sobre un conjunto de datos, órdenes o reglas | *accuracy*, *recognition accuracy*, *OCR accuracy*, tasa de acierto |
| Precisión, exhaustividad o F1 | Rendimiento del modelo | Métricas de clasificación o recuperación del modelo distintas de la exactitud | *precision*, *recall*, *F1-score*, *average precision* (AP) |
| Calidad del texto generado (SARI, BLEU, GLEU) | Rendimiento del modelo | Métrica automática de calidad del texto generado o simplificado frente a referencias | SARI, BLEU, GLEU; antes «Calidad de simplificación (SARI)» |
| Otras métricas del modelo | Rendimiento del modelo | Otra métrica calculada sobre las salidas del modelo | cobertura y diversidad de recomendaciones, tasa de éxito y recompensa en simulación, especificidad del vocabulario generado |
| Comprensión del contenido | Desempeño de las personas usuarias | Respuestas correctas a preguntas o pruebas de comprensión de personas con la condición | *reading comprehension*, *comprehension questions*, test de comprensión; antes «Comprensión lectora» |
| Eficacia de la intervención | Desempeño de las personas usuarias | Cambio en un resultado de la intervención (pretest/postest, comparación con grupo control o enseñanza tradicional, o simulación) | *pre- and post-test*, *grammar performance*, *adherence* |
| Desempeño en la tarea | Desempeño de las personas usuarias | Exactitud, tiempo o compleción de las personas al realizar la tarea con el artefacto | *selection accuracy*, *task completion*, *engagement duration*, *process accuracy* |
| Desempeño lector | Desempeño de las personas usuarias | Velocidad, tiempo o exactitud de lectura de las personas | *reading speed*, *reading time*, *reading accuracy* |
| Usabilidad (SUS) | Usabilidad y aceptación | Puntuación en la System Usability Scale | SUS, *System Usability Scale* |
| Inspección heurística de usabilidad y accesibilidad | Usabilidad y aceptación | Inspección experta con heurísticas o criterios de usabilidad y accesibilidad, o índice que la agrega | *heuristic evaluation*, heurísticas de Nielsen, *U + A-index*; antes «Índice heurístico de usabilidad y accesibilidad» |
| Cuestionario de usabilidad ad hoc | Usabilidad y aceptación | Cuestionario de usabilidad propio del estudio, con puntuaciones por sección | *anonymous usability questionnaire*, escala de 0 a 10 |
| Aceptación tecnológica (TAM) | Usabilidad y aceptación | Utilidad, facilidad de uso o intención de uso percibidas según el Technology Acceptance Model | TAM, *perceived usefulness*, *intention to use* |
| Satisfacción | Experiencia de usuario | Valoración de satisfacción o comodidad en escalas de valoración, cuando es la medida principal | *satisfaction*, *comfort ratings*, escala Likert de satisfacción |
| Experiencia de usuario (UEQ) | Experiencia de usuario | Puntuación en el User Experience Questionnaire | UEQ |
| Índice de legibilidad | Legibilidad | Fórmula de legibilidad calculada sobre el texto que produce o adapta el artefacto | Flesch Reading Ease, Flesch-Kincaid |
| Validez y fiabilidad del instrumento | Validez del instrumento | Validez convergente o fiabilidad de una prueba desarrollada con IA | *convergent validity*, *reliability* |
| NR | — | El texto completo no reporta una métrica principal: estudio cualitativo sin medida cuantificada, estudio de requisitos o necesidades sin evaluación del artefacto, propuesta o ensayo sin evaluación, o MD sin cuerpo de texto (1 caso) | — |

**Verificación (73 de 73 filas con `evidencia`).** Ronda 1: las 34 filas con constructo se cotejaron con el MD (16 se confirman, 11 cambian, 7 pasan a NR). Ronda 2: las 39 filas con el valor de plantilla «Métrica reportada» se recodificaron desde el resumen y el cuerpo del MD (19 con constructo y 20 en NR). Ronda 3: R398 pasa de satisfacción a eficacia de la intervención (mejora NAEP frente a la enseñanza tradicional) y R623 de satisfacción a cuestionario de usabilidad *ad hoc* (110 visitantes). La familia es una agrupación de presentación para la Tabla y no se agrega como categoría. El subcampo `Valor` no se agrega: varios valores del registro no coinciden con el texto completo (p. ej., accuracy = 15 frente a 83,44% en R040) y no se verificaron todos.

## RQ3-I2

Instrumento o protocolo de medición de la evaluación. Multivalor. Base: 49 estudios (cualitativos y mixtos).

| Categoría | Definición | Sinónimos |
|---|---|---|
| Estudio con usuarios | Personas (usuarios con la condición, cuidadores o expertos) usan, prueban o valoran el artefacto ya construido en sesiones, tareas, entrevistas u observación | *user study*, *usability test*, *think-aloud*, entrevistas, talleres de codiseño, grupos focales |
| Cuestionario | Instrumento escrito o en línea con ítems cerrados o abiertos aplicado a personas | *questionnaire*, *survey*, escala Likert, SUS, UEQ, NASA-TLX |
| Heurística | Inspección por expertos con un conjunto de heurísticas o criterios | heurísticas de Nielsen, *heuristic evaluation*, lista de comprobación |
| Índice de legibilidad | Fórmula de legibilidad calculada como medida de la evaluación (código común con RQ3-I1) | Flesch Reading Ease |
| NR | El texto completo no reporta una evaluación del artefacto con instrumento ni con usuarios: propuestas o ensayos sin evaluación, estudios de necesidades o requisitos y talleres de codiseño previos a construir el artefacto (mismo criterio que el NR de RQ3-I5) | — |

**Reglas.** «Legibilidad» del registro se retira de las filas donde la legibilidad es un criterio de diseño, un tema de las entrevistas, una función del artefacto en ejecución o un cálculo ilustrativo en la discusión; solo R208 la conserva como índice. Se retiran categorías sin apoyo en el cuerpo del MD (cuestionario sin «questionnaire», «survey», «Likert» ni escalas; heurística sin «heuristic»). Las 13 filas NR se verificaron en el MD (7 en la R2; R199, R425, R587, R626, R356 y R647 en la R3). Las métricas automáticas del modelo no son instrumentos de este ítem; van en RQ3-I1 y RQ3-I5. Las 19 filas que conservan el valor del registro sin cambios no se cotejaron una por una (`auto: true`).

## RQ3-I3

Marco normativo de accesibilidad al que se adscribe el estudio. Multivalor. Base: 49 estudios (cualitativos y mixtos).

| Categoría | Definición |
|---|---|
| WCAG | El artefacto se diseña, desarrolla o evalúa conforme a las WCAG (2.0, 2.1 o 2.2) |
| COGA | El artefacto se diseña o evalúa conforme a la guía del W3C *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA) |
| Lectura Fácil o lenguaje claro | El artefacto aplica pautas de Lectura Fácil o de lenguaje claro: UNE 153101 EX, Inclusion Europe, Netzwerk Leichte Sprache, *Plain Language*, ISO 24495-1 |
| Otro marco | Otro marco declarado y aplicado: Diseño Universal para el Aprendizaje (DUA), *Minimized Text Complexity* o EN 301 549; el nombre queda en `valores.Otro marco` |
| Sin marco normativo | El estudio no aplica ningún marco normativo de accesibilidad |
| Solo mención: WCAG | WCAG aparece en antecedentes, como crítica o como auditoría futura, sin aplicarse al artefacto |
| Solo mención: COGA | COGA aparece solo en antecedentes |

**Adscripción frente a mención.** Se busca en el cuerpo de cada MD, sin el bloque de plantilla «Relevance hooks» (que repite «WCAG» y «cognitive accessibility» en los 73 MD) ni las referencias: WCAG, COGA, W3C, *Making Content Usable*, *cognitive accessibility*, ISO 9241, EN 301 549, ISO 24495, UNE 153101, *Plain Language*, *Easy-to-Read*, *Leichte Sprache*, Inclusion Europe, UDL y Section 508. Se codifica como adscripción si el texto dice que el artefacto sigue, cumple o se evalúa con el marco; las menciones en antecedentes, las críticas y las auditorías previstas son «Solo mención». La categoría «COGA» del registro (49 de 49, valor bruto único) se descarta. «Diseño universal» genérico y el lenguaje claro como recomendación sin pauta citada no cuentan como marco.

## RQ3-I4

Cobertura de discapacidad de la evaluación. Univalor. Base: 43 estudios (cuantitativos y mixtos).

| Categoría | Definición |
|---|---|
| Cognitiva | La evaluación solo aborda necesidades cognitivas o de neurodivergencia (comprensión, legibilidad, atención, usabilidad para la población cognitiva) |
| Ambas | La evaluación incluye además criterios, participantes o perfiles simulados con discapacidad sensorial o motora: contraste, lector de pantalla, cumplimiento WCAG de percepción, personas sordas o con discapacidad visual |
| Sensorial o motora | La evaluación solo aborda dimensiones sensoriales o motoras, sin ninguna dimensión cognitiva |
| NR | El estudio no evalúa el artefacto (necesidades o requisitos; mismo criterio que el NR de RQ3-I5): R199, R425, R587 y R626 |

**Reglas.** Se codifica la población y los criterios de la **evaluación**, no la motivación del artículo. Las menciones sensoriales en antecedentes no cuentan. La «accesibilidad sensorial» del TEA (regulación de estímulos) es cognitiva. El valor bruto «Ambas» (41 de 43, texto idéntico) se descarta; las 43 filas se verificaron en el MD.

## RQ3-I5

Grado de automatización de la evaluación del artefacto. Univalor. Base: 43 estudios (cuantitativos y mixtos).

| Categoría | Definición |
|---|---|
| Integración continua | La evaluación automática se ejecuta integrada en el ciclo de construcción (CI/CD, pruebas automatizadas recurrentes). Sin casos en el texto completo |
| Semiautomática | Métricas calculadas por software sobre el artefacto o sus salidas (rendimiento del modelo, índice de legibilidad, BLEU, Lighthouse, comprobador de contraste) **y** evaluación con personas (usuarios o expertos) |
| Automática | Solo métricas calculadas por software o simulación, sin personas que usen o juzguen el artefacto. Categoría añadida: el formulario no la preveía |
| Solo validación con usuarios | Solo evaluación con personas (usuarios con la condición, cuidadores o expertos): tareas, cuestionarios, entrevistas, valoración experta. Las medidas del desempeño de las personas registradas por software (p. ej., WER de la lectura del niño) cuentan aquí |
| NR | El estudio no evalúa el artefacto: recoge necesidades o requisitos antes de construirlo |

**Reglas.** Se codifica la automatización de la **evaluación**, no la de la herramienta (ATECA y FACILE son herramientas semiautomáticas). Las 43 filas llevan `auto: false` y `evidencia`. El «sin_participantes» de `matriz.json` no es fiable (R208, R396 tienen participantes). El valor bruto «Solo validación con usuarios» (32 de 43, texto idéntico) se descarta.

## RQ2-I1

Familia de técnica de IA y modelo nombrado. Multivalor. Base: 49 estudios (cualitativos y mixtos). Se codifica la técnica que el estudio aplica en su artefacto, en su procedimiento (p. ej., generar datos de prueba o analizar datos) o que observa en un sistema concreto (p. ej., un altavoz basado en LLM); no cuentan los ensayos conceptuales sin sistema ni procedimiento con IA, ni las menciones en antecedentes, trabajos citados, trabajo futuro ni el uso de IA para corregir la redacción del artículo.

| Categoría | Definición | Sinónimos |
|---|---|---|
| LLM | Modelos de lenguaje grandes o IA generativa de texto: chatbots, generación, reescritura o simplificación con un modelo generativo | *large language model*, GenAI, IA generativa, ChatGPT, GPT, Claude, Gemini, DeepSeek, LaMDA, Hunyuan |
| NLP | Procesamiento del lenguaje natural o del habla que no es un LLM generativo: reglas lingüísticas, etiquetado y análisis sintáctico, simplificación léxica, reconocimiento de voz | spaCy, NLTK, PARZU, ASR, STT, *speech analytics*, IA simbólica sobre texto |
| ML | Aprendizaje automático clásico: clasificadores, agrupamiento, regresión, aprendizaje federado o por refuerzo | *machine learning*, *random forest*, SVM, K-means, HMM |
| DL | Redes neuronales profundas que no son un LLM generativo ni un modelo de imagen | ANN, *autoencoder*, *transformer*, BERT, corrección gramatical neural |
| Visión | Visión por computador y modelos de imagen: reconocimiento facial o de gestos, codificación de imágenes, generación de imágenes | *computer vision*, CLIP, DALL-E, ImageBind, GIT, KOSMOS-2, *text-to-image* |
| Modelo: <nombre> | Modelo concreto que el texto nombra para la técnica aplicada; versión tal como la escribe el artículo | GPT-4o, GPT-4, GPT-3.5, GPT-3, ChatGPT (versión no indicada), BERT, CLIP, DeepSeek (V3 o sin versión), Claude (3.7 Sonnet), Gemini (2.0 Flash), LaMDA, Hunyuan, DALL-E, API de imágenes de OpenAI, OTTER, ImageBind, GIT, ViLT, KOSMOS-2 |
| Modelo: no nombrado | NR del subcampo modelo: el estudio aplica una familia pero no nombra un modelo concreto. Sustituye a «Modelo: NR» del registro; no es una fila de la tabla, va en la *Nota.* | «Modelo: NR» |
| NR | El estudio no reporta una técnica de IA aplicada: el artefacto no la especifica, o la IA solo aparece en antecedentes, como trabajo futuro, como percepción de los participantes o como objeto de un análisis conceptual | — |

**Reglas.** Un LLM no implica por sí solo NLP ni DL: estas familias se codifican cuando el artefacto incluye un componente propio de ese tipo. La IA simbólica que opera sobre texto (sistemas de producción para detectar estructuras lingüísticas) se codifica como NLP. «Modelo: Llamada» del registro procede de «la llamada IA simbólica» (R106: «así llamada»), no de Llama; R106 nombra ChatGPT. La familia genérica «IA» del registro se sustituye por las familias que el texto nombra. Las 49 filas se verificaron en el cuerpo del MD (sin el bloque «Relevance hooks» ni las referencias); entre los cambios, R581 usa LaMDA y no GPT-4, R337 nombra ChatGPT sin versión, R347 no aplica ningún modelo (los nombrados son herramientas de los participantes) y R394, R605 y R705 sí nombran modelo aunque el registro decía NR o estaba vacío. (R2) R453, ensayo conceptual sin sistema ni procedimiento con IA, pasa a NR. En R583 se retira GPT-4 (solo antecedente, l. 484) y se añade ViLT, que el prototipo implementa (l. 715–720); los modelos de prototipos de laboratorio cuentan como aplicados.

## RQ2-I2

Rol de la IA en el software que el estudio desarrolla, evalúa o analiza. Multivalor. Base: 49 estudios (cualitativos y mixtos).

| Categoría | Definición | Ejemplos |
|---|---|---|
| Generador | La IA produce contenido o salidas del artefacto: texto simplificado o reescrito, respuestas conversacionales, imágenes, pictogramas, recomendaciones, cuestionarios o interfaces | chatbot, simplificación, recomendación de imágenes, generación de interfaz |
| Intérprete de la entrada o del estado del usuario | La IA reconoce o clasifica lo que el usuario hace o expresa: voz, gestos, expresiones, señales no verbales o indicadores de su condición | ASR, reconocimiento de gestos, análisis del habla, clasificación de riesgo |
| Personalizador en ejecución | La IA adapta el artefacto o el contenido al perfil o a la conducta del usuario mientras se usa | perfiles de usuario, aprendizaje por refuerzo, adaptación en tiempo real |
| Evaluador del contenido | La IA juzga la legibilidad o la accesibilidad del texto que procesa el artefacto (función del artefacto en ejecución) | detección de incumplimientos de Lectura Fácil, identificación de palabras complejas |
| Asistente de aseguramiento de la calidad | La IA apoya al equipo en la verificación del artefacto: genera datos o casos de prueba, criterios o heurísticas de evaluación, o señala problemas que una persona revisa | frases de prueba generadas con ChatGPT, heurísticas generadas con GenAI, evaluación heurística de la interfaz con LLM revisada por una persona |
| Análisis de datos de la investigación | La IA se usa para analizar los datos del estudio, no dentro del artefacto | PLN sobre publicaciones de una comunidad, análisis sintáctico de un corpus, GPT-4o en el análisis cualitativo |
| NR | El estudio no reporta una técnica de IA aplicada (coincide con NR en RQ2-I1) | — |

**Reglas.** El valor bruto «Generador; evaluador; asistente de aseguramiento de la calidad» (44 de 49, texto idéntico) se descarta. El rol se codificó desde el texto completo, con la misma lectura que RQ2-I1. Las categorías «Intérprete», «Personalizador» y «Análisis de datos» concretan el «otro» que el formulario preveía.

**Niveles (R2).** Generador, Intérprete, Personalizador y Evaluador del contenido son funciones de la IA **como componente del artefacto**; Asistente de aseguramiento de la calidad es el rol de la IA **en el proceso de desarrollo o evaluación** del software; Análisis de datos es un uso en el **procedimiento de la investigación**. Una misma acción se codifica una sola vez: si la IA emite un juicio que una persona revisa para verificar el artefacto, es Asistente de AC y no Evaluador (R495). R453 pasa a NR, como en RQ2-I1.

## RQ2-I3

Fase principal del ciclo de vida del software en que se sitúa la contribución del estudio. Univalor. Base: 43 estudios (cuantitativos y mixtos).

| Categoría | Definición |
|---|---|
| Requisitos | El estudio recoge necesidades o requisitos para un artefacto (evaluación de necesidades, elicitación) |
| Desarrollo | El estudio construye o entrena el artefacto o su modelo |
| Personalización en ejecución | La contribución es la adaptación del artefacto al usuario mientras se usa |
| Pruebas | La contribución es la evaluación del artefacto con usuarios, expertos o métricas |
| V&V | La contribución es la validación formal de un instrumento o sistema (fiabilidad y validez) |

**Reglas (R2: las 43 filas verificadas, `auto: false`).** Se decide por la contribución que declaran el título y el resumen, en este orden: (1) **Requisitos** si recoge requisitos o necesidades sin construir el artefacto; (2) **V&V** si la contribución es la validación de fiabilidad y validez de un instrumento; (3) **Pruebas** si evalúa un artefacto, modelos o textos que el artículo no construye, o si se presenta expresamente como estudio de evaluación (estudio piloto, hallazgos de rondas de prueba) sin presentar la construcción como aporte; (4) **Personalización en ejecución** si el artefacto que presenta se define en el título o el resumen como adaptativo o personalizado al usuario mientras se usa; (5) **Desarrollo** si presenta, propone o desarrolla el artefacto, aunque después lo evalúe. Con esta regla, 21 filas difieren del registro (19 cambian de fase y 2 estaban vacías): R040, R123, R183, R233, R263, R345, R369, R396, R595, R600 y R623 pasan de Pruebas a Desarrollo; R203 pasa de Personalización a Desarrollo (la IA genera materiales); R147, R293 y R398 pasan de Pruebas a Personalización en ejecución; R145 pasa de Desarrollo a Pruebas; R199, R425 y R626 pasan a Requisitos; R106 (vacía) queda en Desarrollo y R630 (vacía) en Personalización en ejecución.

## RQ2-I4

Otras fases que el estudio también aborda, sin repetir la principal. Multivalor. Base: 43 estudios (cuantitativos y mixtos).

| Categoría | Definición |
|---|---|
| Requisitos | El estudio recoge requisitos o necesidades además de su fase principal |
| Desarrollo | El estudio construye o entrena el artefacto además de su fase principal |
| Pruebas | El estudio evalúa el artefacto además de su fase principal |
| Solo una fase | El estudio no aborda ninguna fase además de la principal (el «—» que el formulario preveía) |

**Reglas.** (R2) RQ2-I4 se deriva del conjunto de fases verificadas de cada estudio (requisitos, desarrollo, pruebas) menos su fase principal verificada; cuando la principal cambió en R2, la fase que deja de ser principal pasa a otras fases si el texto la apoya. En R1: a cada estudio se le resta la fase principal de RQ2-I3 (el registro la repetía en 36 de 41). Cada fase restante se comprobó en el cuerpo del MD con patrones de requisitos (*requirements elicitation*, *needs assessment*), de desarrollo (*we developed*, *implemented*, *trained*) y de pruebas (*user study*, *usability evaluation*, *pilot study*, *test set*); se retiró la fase cuando el texto no la apoya o solo aparece en antecedentes, trabajo futuro o referencias, y se añadió cuando el texto la muestra sin que el registro la tuviera (Desarrollo en R293 y R296; Requisitos en R106). «Requisitos», que el registro repetía en 30 de 43, se mantiene en 6. Diseño no se registró en el formulario y no se codifica aparte: los estudios con codiseño quedan en Requisitos o Desarrollo según su objetivo. Si la fase principal es V&V, Pruebas no se suma como otra fase.
