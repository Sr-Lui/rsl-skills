# Ítems de extracción

**Tema:** Inteligencia artificial en el ciclo de vida del software para accesibilidad cognitiva · **Marco:** población, intervención y resultado (PIO) · **Picoc:** versión 2026-10-03-3-PIO · **Incluidos (SI):** 73 · **Fecha:** 2026-11-04

## Objetivo de extracción

De cada estudio incluido, la revisión tabula la evidencia que responde a las tres preguntas de investigación (RQ) del marco PIO. La primera atiende a la población y su participación; la segunda, a la técnica de inteligencia artificial y la fase del ciclo de vida del software en que se aplica. La tercera se ocupa de las métricas, los marcos normativos y el contraste entre accesibilidad cognitiva y sensorial. Con esos datos se sintetiza cada RQ en tablas de frecuencia, cuando basta una categoría por estudio, y en párrafos, cuando el artículo aporta motivos o matices cualitativos. Para la RQ1 se registran además el enfoque sobre la condición, el tratamiento del perfil, el consentimiento o asentimiento informado y el país, conforme al protocolo de la revisión.

## Campos bibliográficos comunes

Junto con los ítems de cada pregunta, cada fila del corpus lleva una sola vez unos campos bibliográficos ajenos al límite de cinco ítems: identificador del corpus, título, autores, año, medio de publicación e identificador de objeto digital.

## Reglas de registro y agregación

Para que las respuestas sean comparables entre estudios, el registro sigue las convenciones de la primera tabla; la segunda indica cómo se agrega cada ítem en Resultados. En todo el formulario, **no reportado (NR)** indica que el dato no aparece en el texto completo.

| Convención | Uso |
|------------|-----|
| **NR** | No reportado en el texto completo (no inferir solo del resumen). |
| **Multivalor** | Separar valores con **`;`** (perfiles, fases secundarias, roles múltiples). |
| **Fases (RQ2)** | **Fase principal:** una categoría. **Otras fases:** lista con `;` o **`—`** si el estudio solo aborda una fase. |
| **Plantillas mixtas** | Usar etiquetas fijas en la celda (p. ej. `Presencia: … \| N: … \| Rol: …`). |

| Ítem | Agregación prevista en Resultados |
|------|-----------------------------------|
| RQ1-I2, RQ2-I3, RQ2-I4, RQ3-I4, RQ3-I5 | **Frecuencia** (% estudios por categoría; Tipo cuantitativo) |
| RQ1-I1, RQ2-I1, RQ2-I2, RQ3-I2, RQ3-I3 | **Frecuencia** y/o **narrativa** según codificación (Tipo cualitativo) |
| RQ1-I3, RQ1-I4 | **Mixto:** subcampos → frecuencia por subcampo; narrativa en notas |
| RQ3-I1 | **Mixto:** constructo (frecuencia) + **Valor** numérico si el paper lo reporta |

## RQ1 (P) — Población

**Pregunta (literal del picoc):** ¿Qué perfiles de discapacidad cognitiva o neurodivergencia (trastorno del espectro autista [TEA], trastorno por déficit de atención e hiperactividad [TDAH], discapacidad intelectual, dificultades de aprendizaje y dislexia) abordan los estudios y con qué grado de estratificación y participación de usuarios?

**Dato a extraer (picoc):** Condición declarada · estratificación (sí o no) · participación de personas con discapacidad

### Ítems de extracción

| Id | Ítem (qué registrar) | Tipo | Codificación | Notas / valores esperados |
|----|----------------------|------|--------------|---------------------------|
| RQ1-I1 | Perfiles declarados en el estudio | cualitativo | nominal | Multivalor con `;` (TEA, TDAH, DI, dislexia…); redacción del artículo |
| RQ1-I2 | Estratificación por perfil | cuantitativo | categórico | Sí / No / NR; cómo se reporta en notas |
| RQ1-I3 | Participación de personas con la condición | mixto | mixto | Plantilla: `Presencia: Sí\|No\|NR \| N: …\|NR \| Rol: diseño\|evaluación\|ambos\|NR` |
| RQ1-I4 | Marco ético y país del estudio | mixto | mixto | Plantilla: `Enfoque: diferencia\|déficit\|NR \| Perfil: deducido\|almacenado\|NR \| Consentimiento: …\|NR \| País: …\|NR` |

## RQ2 (I) — Intervención

**Pregunta (literal del picoc):** ¿Qué técnicas de inteligencia artificial —incluidas la inteligencia artificial generativa (GenAI) y los modelos de lenguaje grandes (LLM)— se han aplicado, con qué rol y en qué fase del ciclo de vida del software?

**Dato a extraer (picoc):** Familia de técnica (aprendizaje automático, aprendizaje profundo, procesamiento de lenguaje natural, LLM o GenAI) · modelo · rol (generador, evaluador o asistente de aseguramiento de la calidad) · fase del ciclo de vida (requisitos, diseño, desarrollo, personalización en tiempo de ejecución, pruebas, verificación y validación o auditoría) · año de publicación

### Ítems de extracción

| Id | Ítem (qué registrar) | Tipo | Codificación | Notas / valores esperados |
|----|----------------------|------|--------------|---------------------------|
| RQ2-I1 | Familia de técnica de IA | cualitativo | nominal | ML, DL, NLP, LLM, GenAI, visión…; `Modelo: nombre \| NR` en notas |
| RQ2-I2 | Rol de la IA en el estudio | cualitativo | categórico | Generador, evaluador, asistente de aseguramiento de la calidad, otro; multivalor con `;` si aplica |
| RQ2-I3 | Fase principal del ciclo de vida | cuantitativo | categórico | Requisitos, diseño, desarrollo, personalización en ejecución, pruebas, V&V, auditoría, otro, NR |
| RQ2-I4 | Otras fases reportadas | cuantitativo | nominal | Lista con `;` o **`—`** si solo una fase; no duplicar la principal |

## RQ3 (O) — Resultados de evaluación

**Pregunta (literal del picoc):** ¿Qué métricas de evaluación y qué marcos normativos reportan los estudios —usabilidad, experiencia de usuario, legibilidad, carga cognitiva, calidad de software y accesibilidad cognitiva, incluidas las orientaciones de accesibilidad cognitiva del World Wide Web Consortium (COGA) frente a las Pautas de Accesibilidad para el Contenido Web (WCAG)— y con qué grado de automatización? ¿En qué medida, además, la evaluación contrasta usuarios con discapacidad cognitiva o neurodivergencia con la accesibilidad sensorial?

**Dato a extraer (picoc):** Métrica · instrumento · marco normativo (WCAG, COGA o ninguno) · cobertura de discapacidad en la evaluación (cognitiva, sensorial o ambas) · grado de automatización (integración continua, semiautomática o solo validación con usuarios)

### Ítems de extracción

| Id | Ítem (qué registrar) | Tipo | Codificación | Notas / valores esperados |
|----|----------------------|------|--------------|---------------------------|
| RQ3-I1 | Métrica principal y valor reportado | mixto | mixto | Plantilla: `Constructo: … \| Valor: número+unidad \| NR` |
| RQ3-I2 | Instrumento o protocolo de medición | cualitativo | texto | Cuestionario, heurística, tarea…; motivos o limitaciones en notas |
| RQ3-I3 | Marco normativo de accesibilidad | cualitativo | categórico | WCAG, COGA, ninguno, otro (especificar), NR |
| RQ3-I4 | Cobertura de la evaluación | cuantitativo | categórico | Cognitiva, sensorial, ambas, NR |
| RQ3-I5 | Grado de automatización | cuantitativo | categórico | Integración continua, semiautomática, solo validación con usuarios, NR |

## Ítems

### P — Población (RQ1)

**Pregunta:** ¿Qué perfiles abordan los estudios y con qué estratificación y participación de usuarios?

**Ítems:**
- RQ1-I1 — Perfiles de discapacidad cognitiva o neurodivergencia que el estudio declara, con la redacción del artículo
- RQ1-I2 — Si el estudio estratifica o desagrega resultados por perfil cognitivo o neurodivergente
- RQ1-I3 — Participación de personas con la condición en diseño o evaluación, y número de participantes si se reporta
- RQ1-I4 — Enfoque sobre la condición, tratamiento del perfil, consentimiento o asentimiento informado y país del estudio

### I — Intervención (RQ2)

**Pregunta:** ¿Qué técnicas de inteligencia artificial, con qué rol y en qué fases del ciclo de vida del software?

**Ítems:**
- RQ2-I1 — Familia de técnica de inteligencia artificial aplicada y modelo concreto si el artículo lo nombra
- RQ2-I2 — Rol de la inteligencia artificial en el proceso de desarrollo o evaluación del software
- RQ2-I3 — Fase principal del ciclo de vida del software en la que interviene la técnica
- RQ2-I4 — Otras fases del ciclo de vida que el estudio también aborda además de la principal

### O — Resultados (RQ3)

**Pregunta:** ¿Qué métricas y marcos normativos reportan, con qué automatización y contraste cognitivo frente a sensorial?

**Ítems:**
- RQ3-I1 — Métrica o constructo principal de evaluación y valor numérico cuando el artículo lo reporta
- RQ3-I2 — Instrumento o protocolo de medición empleado en el estudio
- RQ3-I3 — Marco normativo de accesibilidad al que se adscribe el estudio
- RQ3-I4 — Cobertura de la evaluación respecto a discapacidad cognitiva, sensorial o ambas
- RQ3-I5 — Grado de automatización de la evaluación que reporta el estudio
