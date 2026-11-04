# Ítems de extracción

**Tema:** Inteligencia artificial en el ciclo de vida del software para accesibilidad cognitiva · **Marco:** población, intervención y resultado (PIO) · **Picoc:** versión 2026-10-03-3-PIO · **Incluidos (SI):** 73 · **Fecha:** 2026-11-04

## Objetivo de extracción

Esta revisión tabulará, para cada estudio incluido, la evidencia que responde a las tres preguntas del marco PIO. Una pregunta cubre la población y su participación; otra, la técnica de inteligencia artificial y la fase del ciclo de vida del software; la tercera, las métricas y los marcos normativos de evaluación, incluido el contraste entre accesibilidad cognitiva y sensorial. Los datos permitirán sintetizar patrones por pregunta de investigación (RQ) y señalar combinaciones con poca evidencia frente al predominio de la accesibilidad sensorial en la literatura.

## Campos bibliográficos comunes

Estos campos se registran una vez por fila del corpus (no cuentan en el límite de cinco ítems por RQ): identificador del corpus, título, autores, año de publicación, venue y DOI.

## RQ1 (P) — Población

**Pregunta (literal del picoc):** ¿Qué perfiles de discapacidad cognitiva o neurodivergencia (trastorno del espectro autista [TEA], trastorno por déficit de atención e hiperactividad [TDAH], discapacidad intelectual, dificultades de aprendizaje y dislexia) abordan los estudios y con qué grado de estratificación y participación de usuarios?

**Dato a extraer (picoc):** Condición declarada · estratificación (sí o no) · participación de personas con discapacidad

### Ítems de extracción

| Id | Ítem (qué registrar) | Tipo de dato | Notas / valores esperados |
|----|----------------------|--------------|---------------------------|
| RQ1-I1 | Perfiles de discapacidad cognitiva o neurodivergencia declarados en el estudio | nominal | TEA, TDAH, discapacidad intelectual, dislexia, dificultades de aprendizaje, etc., con la redacción del artículo |
| RQ1-I2 | Estratificación o desagregación por perfil en diseño o análisis | categórico | Sí o no; indicar cómo se reporta (subgrupos, tareas separadas, etc.) |
| RQ1-I3 | Participación de personas con la condición en diseño o evaluación | mixto | Presencia (sí o no); número aproximado si se reporta; rol (diseño, evaluación, ambos) |
| RQ1-I4 | Enfoque sobre la condición y contexto ético-geográfico | mixto | Diferencia vs déficit; deducción vs almacenamiento del perfil; consentimiento o asentimiento informado; país del estudio |

## RQ2 (I) — Intervención

**Pregunta (literal del picoc):** ¿Qué técnicas de inteligencia artificial —incluidas la inteligencia artificial generativa (GenAI) y los modelos de lenguaje grandes (LLM)— se han aplicado, con qué rol y en qué fase del ciclo de vida del software?

**Dato a extraer (picoc):** Familia de técnica (aprendizaje automático, aprendizaje profundo, procesamiento de lenguaje natural, LLM o GenAI) · modelo · rol (generador, evaluador o asistente de aseguramiento de la calidad) · fase del ciclo de vida (requisitos, diseño, desarrollo, personalización en tiempo de ejecución, pruebas, verificación y validación o auditoría) · año de publicación

### Ítems de extracción

| Id | Ítem (qué registrar) | Tipo de dato | Notas / valores esperados |
|----|----------------------|--------------|---------------------------|
| RQ2-I1 | Familia de técnica de inteligencia artificial (y modelo si se nombra) | nominal | Aprendizaje automático, aprendizaje profundo, procesamiento de lenguaje natural, LLM, GenAI, visión por computadora, etc.; incluir nombre del modelo en las notas |
| RQ2-I2 | Rol de la inteligencia artificial en el estudio | categórico | Generador, evaluador, asistente de aseguramiento de la calidad u otro (especificar) |
| RQ2-I3 | Fase del ciclo de vida del software en la que interviene la técnica | categórico | Requisitos, diseño, desarrollo, personalización en ejecución, pruebas, verificación y validación, auditoría u otra |

## RQ3 (O) — Resultados de evaluación

**Pregunta (literal del picoc):** ¿Qué métricas de evaluación y qué marcos normativos reportan los estudios —usabilidad, experiencia de usuario, legibilidad, carga cognitiva, calidad de software y accesibilidad cognitiva, incluidas las orientaciones de accesibilidad cognitiva del World Wide Web Consortium (COGA) frente a las Pautas de Accesibilidad para el Contenido Web (WCAG)— y con qué grado de automatización? ¿En qué medida, además, la evaluación contrasta usuarios con discapacidad cognitiva o neurodivergencia con la accesibilidad sensorial?

**Dato a extraer (picoc):** Métrica · instrumento · marco normativo (WCAG, COGA o ninguno) · cobertura de discapacidad en la evaluación (cognitiva, sensorial o ambas) · grado de automatización (integración continua, semiautomática o solo validación con usuarios)

### Ítems de extracción

| Id | Ítem (qué registrar) | Tipo de dato | Notas / valores esperados |
|----|----------------------|--------------|---------------------------|
| RQ3-I1 | Métrica o constructo principal de evaluación reportado | nominal | Usabilidad, experiencia de usuario, legibilidad, carga cognitiva, calidad de software, accesibilidad cognitiva, etc. |
| RQ3-I2 | Instrumento o protocolo de medición empleado | texto | Cuestionario, heurística, lista de comprobación, tarea observada; descripción breve |
| RQ3-I3 | Marco normativo de accesibilidad declarado | categórico | WCAG, COGA, ninguno u otro (especificar) |
| RQ3-I4 | Cobertura de la evaluación y grado de automatización | mixto | Subcampo 1: cognitiva, sensorial o ambas; subcampo 2: integración continua, semiautomática o solo validación con usuarios |
