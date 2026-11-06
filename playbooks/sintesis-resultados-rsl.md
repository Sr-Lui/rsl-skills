# Síntesis de resultados por ítem (rsl-resultado-sintesis)

Contrato de la sección **Resultados** de la RSL a partir del formulario de extracción vigente. Lo usan **defensor-rsl** (propone), **critico-rsl** (debate) y **orquestador-sintesis-rsl** (cierra), y lo valida `pnpm -s sintesis:lint`.

**Los ejemplos de la sección «Ejemplos correctos» mandan.** Si una regla y un ejemplo chocan, gana el ejemplo.

## 1. Qué es sintetizar

La síntesis recopila y resume los resultados de los artículos incluidos. La información extraída (población, intervención, contexto, tipo y tamaño de muestra, resultados, conclusiones) se tabula de forma coherente con las preguntas de investigación del marco (PIO, PICO…).

- **Por ítem y resultado, nunca por autor.** Se agrupan artículos, ítems y resultados: «el 65% (n=32) declara TEA». Está **prohibido** el enfoque centrado en el autor, que resume cada artículo por separado:
  - Autor A [concepto X, concepto Y, … concepto Z]
  - Autor B [concepto X, concepto W, … concepto Z]
- **Homogeneidad o heterogeneidad.** Se dice si los resultados son consistentes entre estudios o no, y se tabula para mostrar las causas posibles: tipo de diseño, naturaleza del estudio, tamaño de muestra.
- **Descriptiva + resumen cuantitativo.** La síntesis es narrativa, complementada con tablas, cuadros y frecuencias. **No hay metaanálisis** (fuera del curso).
- **Tipo de síntesis por bloque** (campo `sintesis` de `bloques.json`):
  - **aditiva:** estudios sobre cosas similares; se «traducen» a un lenguaje común (el libro de códigos) y se suman;
  - **refutacional:** estudios que se contradicen; se explican los estudios y la refutación;
  - **argumental:** cada estudio cubre una parte del problema; primero se identifican los temas por estudio y luego se infiere sobre el conjunto.
- **Estudios cuantitativos y cualitativos.** Primero se sintetizan **por separado** y luego se **integran**: se investiga si lo cualitativo ayuda a explicar lo cuantitativo (por qué un modelo o solución funciona o no en circunstancias concretas). Referencia del método: Sutcliffe et al. (2003), con metaanálisis, síntesis temática cualitativa y síntesis cruzada; aquí sin metaanálisis.

## 2. Tono: objetivo

Resultados **solo reporta lo que reporta la literatura**: cifras, categorías y frecuencias. No valora, no recomienda y no interpreta; eso va en Discusión.

| Correcto | Incorrecto |
|---|---|
| «el 68% (n=34) reporta un aumento en los niveles de estrés» | «el teletrabajo es malo» |
| «los sistemas de tutoría inteligente se reportan en el 40% de los estudios» | «esto significa que los profesores prefieren los chatbots» |
| «IoT se reporta en el 80% (n=32)» | «el IoT es lo mejor» |

El lint avisa (WARN) ante términos evaluativos o de recomendación: *notable, preocupante, prometedor, alarmante, excelente, el mejor, es fundamental, es crucial, se recomienda, debería, innovador…*

## 3. Reglas de redacción

- **Sin citas a estudios individuales.** No hay [n], (Autor, año), «Autor et al.» ni identificadores del corpus (R016) en `sintesis-resultados.md`. La traza de qué estudios respaldan cada categoría vive solo en `tablas/<bloque>.json` (campo `estudios`).
- **Apertura con el total:** «Tras la aplicación de los criterios de inclusión y exclusión, se seleccionaron N artículos…», «Del total de N artículos seleccionados…», «De los N artículos que conformaron la muestra final…».
- **Formato de la cifra:** `el X% (n=Y)`, o «Y estudios (X%)». Las categorías van en orden descendente por n. Porcentajes enteros.
- **Verbos neutros de reporte:** reporta, identifica, documenta, menciona, declara, emplea, se identifican, indican.
- **Lista por categoría** cuando hay pocas categorías y cada una tiene un hallazgo que describir: «Categoría: reportada en Y estudios (X%) como…». La menos frecuente puede abrir con «Únicamente Y estudios (X%) indican…».
- **Caracterización:** periodo («publicados entre 2021 y 2026»), pico («Se observa un pico de producción científica en el año 2026»), rango («El tamaño de las muestras osciló entre 1 y 1 536 participantes»).
- **Encabezados numerados** con títulos descriptivos: `### 3.1. Frecuencia de publicaciones por año`, `### 3.2. …`.
- **Los porcentajes no siempre suman 100%:** cuando un estudio puede reportar varias categorías, se aclara en la *Nota.* de la tabla o figura («Un estudio puede reportar más de una categoría»).

### Base de los porcentajes

- Caracterización (3.1): **N = total de estudios incluidos**.
- Ítems: **la base es el número de estudios que tienen ese ítem en el formulario** (`items_meta.<ítem>.n_base` en `matriz.json`). Los ítems cualitativos solo están en la hoja Cualitativo (estudios cualitativos y mixtos) y los cuantitativos solo en la hoja Cuantitativo (estudios cuantitativos y mixtos); los mixtos están en ambas. La base se declara en el texto o en la nota («Del total de 49 estudios con enfoque cualitativo o mixto…»).
- Cruces: la base es el número de estudios con dato en ambos ítems (`cruce.base`).
- Los no reportados (NR) se mencionan aparte cuando aportan («el dato no se reporta en n=7»).

## 4. Tablas

Una tabla organiza el contenido de forma sistemática y resume datos cuantitativos de tamaño pequeño o mediano.

```markdown
**Tabla N**

*Título representativo del contenido*

| Categoría | Hallazgo reportado en la literatura | Frecuencia (n) | Porcentaje |
|---|---|---|---|
| **Grupo A** | Descripción breve | 22 | 73% |
| | Otra descripción | 18 | 60% |

*Nota.* Datos extraídos de los N artículos seleccionados. Un estudio puede reportar más de una categoría.
```

- `**Tabla N**` en su línea, el título en cursiva en la siguiente, y `*Nota.*` al pie. Numeración consecutiva.
- **Cada columna indica su unidad:** `Frecuencia (n)`, `Porcentaje`, `N.º de estudios`.
- **Orientación:** las comparaciones simples entre categorías van en horizontal; las relaciones causa-efecto van en vertical (factor a la izquierda, resultado a la derecha, una fila por factor).
- Se cita en el texto **antes** de aparecer («La Tabla 1 resume…»).

## 5. Figuras (esta skill no dibuja)

Una figura resalta patrones o tendencias, muestra cambios en el tiempo, presenta relaciones entre variables o complementa un concepto complejo. Lleva un título representativo de los datos, va **intercalada** con el texto y se cita antes de aparecer («Como se observa en la Figura 1, …»).

La skill deja el hueco de la figura y, debajo, la subsección **Detalle gráfica**. La siguiente skill dibuja con Python a partir de `graficos/<bloque>.spec.json`:

```markdown
**Figura N**

*Título representativo de los datos*

> Gráfica pendiente — ver «Detalle gráfica».

*Nota.* Elaboración propia a partir de los N artículos seleccionados (AAAA–AAAA).

#### Detalle gráfica (Figura N)

- **Tipo:** barras verticales | barras horizontales | líneas | mapa de calor | barras apiladas | …
- **Por qué este tipo:** motivo según las reglas de figuras.
- **Qué muestra:** una frase.
- **Datos a dibujar:** valores exactos (categoría, n, %), o filas, columnas y matriz si es un cruce.
- **Ejes:** X (variable y orden), Y (unidad: % o N.º de estudios), escala y rango.
- **Etiquetas sobre los datos:** `X% (n=Y)` sobre cada barra o el número de cada celda.
- **Leyenda:** texto y significado de colores o series.
- **Título interno del gráfico:** si difiere del título de la figura.
- **Nota del gráfico:** p. ej. «Los porcentajes no suman 100%: un estudio puede reportar más de una categoría (base n = 49)».
- **Estilo:** paleta (azules sobrios por defecto), orden (descendente por n), tamaño.
```

`graficos/<bloque>.spec.json` (mismos datos; los `n` deben coincidir con `tablas/<bloque>.json`):

```json
{"figura": 1, "bloque": "B00-anio", "titulo": "…", "tipo": "barras verticales", "motivo": "…",
 "muestra": "…", "datos": [{"categoria": "2026", "n": 26, "pct": 36}],
 "ejes": {"x": "Año", "y": "Porcentaje de estudios", "unidad": "%"},
 "etiquetas": "X% (n=Y)", "leyenda": "…", "nota": "…",
 "estilo": {"paleta": "azules sobrios", "orden": "cronológico", "tamano": "16x9 cm"}}
```

Patrones de los ejemplos: barras con `X% (n=Y)` sobre cada barra y eje en %; mapa de calor con el número de estudios en cada celda y barra de color («Número de estudios coincidentes»).

## 6. Estructura de `sintesis-resultados.md`

1. `### 3.1.` y siguientes: **caracterización** de los estudios (bloques B00: año, enfoque metodológico, tipo de documento, distribución geográfica, tamaño de muestra).
2. **Bloques por RQ** (`formato.resultados_por: rq` en `config.yml`). El título de la subsección lleva la RQ, por ejemplo `### 3.4. Perfiles de neurodivergencia abordados (RQ1)`. Cada RQ cierra con la **integración** de lo cuantitativo y lo cualitativo.

## 7. Bloques (`bloques.json`)

Los B00 vienen sembrados por `sintesis:prepare`. Los bloques RQ los propone el defensor (modo `sintesis-bloques`): un ítem solo o varios juntos cuando agruparlos enriquece el análisis frente al objetivo de la RSL (p. ej. perfil × familia de IA). Todo ítem debe quedar en algún bloque.

```json
{"id": "RQ2-B1", "rq": "RQ2", "titulo": "Perfiles neurodivergentes frente a familias de IA",
 "items": ["RQ1-I1", "RQ2-I1"], "campos": {"RQ2-I1": "_registro"},
 "agregacion": "cruce", "sintesis": "argumental", "presentacion": "figura",
 "motivo_presentacion": "Relación entre dos variables nominales"}
```

- `agregacion`: `frecuencia` | `cruce` (2 ítems) | `descriptivo` | `general` (solo B00).
- `presentacion`: `tabla` | `figura` | `lista` | `ambas` | `texto`, con `motivo_presentacion`.
- `campos` (opcional): subcampo de plantilla por ítem (`"Rol"`, `"Presencia"`) o `"_registro"` para usar solo las categorías sin prefijo (p. ej. familias de IA sin «Modelo: …»).

## 8. Codificación

`sintesis:codify-auto` propone categorías a partir del registro agregable de cada celda. Los agentes las revisan y ajustan antes de agregar, con dos archivos:

- **`codebook.md`:** por ítem, la categoría, su definición y sus sinónimos (p. ej. «Trastorno del espectro autista», «autismo» → **TEA**). Es la «traducción» de la síntesis aditiva.
- **`codificacion/<ítem>.jsonl`:** una línea por estudio, con `si_order`, `corpus_id`, `naturaleza`, `valor`, `categorias[]`, `valores{}`, `nr`, `auto` y `revisar`. Al editar a mano, `auto` pasa a `false`.

**Sesgos del registro.** Si una categoría reúne casi todos los estudios (p. ej. «COGA» en 49 de 49 o «Ambas» en 41 de 43), el crítico debe comprobar en el valor bruto que no es un sesgo de extracción. Si lo es, se recodifica desde el valor (no se cambia el Excel) y se anota en el debate.

## 9. Debate por bloque

| Ronda | Quién | Archivo |
|---|---|---|
| R1 | defensor propone (agrupación, codificación, texto, tabla o figura, Detalle gráfica) | `debate/<bloque>/r1-defensor.md` |
| R1 | crítico revisa → **De acuerdo** / **En desacuerdo** + motivos | `debate/<bloque>/r1-critico.md` |
| R2 | defensor corrige o defiende | `debate/<bloque>/r2-defensor.md` |
| R2 | crítico → **De acuerdo** / **En desacuerdo** | `debate/<bloque>/r2-critico.md` |
| R3 | **solo si no hubo acuerdo en R2**: ronda final para buscar consenso | `r3-defensor.md`, `r3-critico.md` |
| Cierre | orquestador-sintesis-rsl | `debate/<bloque>/veredicto.json` |

- **Dos rondas siempre.** No se pasa al bloque siguiente hasta cerrar el actual.
- **Sin acuerdo en R2 → R3 final.** Si en la R3 tampoco hay acuerdo, el orquestador cierra con la decisión mejor sustentada y deja el desacuerdo residual por escrito.

`veredicto.json`:

```json
{"bloque": "RQ2-B1", "rondas": 3, "acuerdo_r2": false, "cierre": "consenso_r3",
 "desacuerdo_residual": "", "resumen": "Consenso en R3: se excluye la categoría genérica «IA» del cruce."}
```

- `cierre`: `acuerdo` (R2) | `consenso_r3` | `orquestador_r3` (este último exige `desacuerdo_residual`).
- **Aviso de tercera ronda:** para cada bloque con R3, la salida dice «Bloque X: requirió una tercera ronda final porque no hubo acuerdo en la segunda; …». Aparece en `sintesis-debate.md` (sección `## Bloques con tercera ronda`, que genera `sintesis:debate-index`), en `manifest.json` (`rondas_3`) y en el mensaje de cierre de `sintesis:stamp`. **Nunca** en la prosa de `sintesis-resultados.md`.

### Lista de revisión del crítico

1. ¿Agrupa por ítem y resultado, sin resumir artículos uno a uno ni citar estudios?
2. ¿Cada «X% (n=Y)» sale de `tablas/<bloque>.json` con la base correcta?
3. ¿Tono objetivo, sin valorar ni interpretar?
4. ¿Categorías bien codificadas (sin duplicados por sinónimo, sin sesgo del registro)?
5. ¿Se sintetiza lo cuantitativo y lo cualitativo por separado y luego se integra?
6. ¿Se señala homogeneidad o heterogeneidad y su posible causa?
7. ¿La elección tabla, figura o lista sigue las reglas? ¿La Detalle gráfica está completa y cuadra con la tabla?
8. ¿Formato de Tabla/Figura (número, título en cursiva, *Nota.*, citada antes, intercalada)?

## 10. Ejemplos correctos (mandan)

> **3.1. Frecuencia de publicaciones por año**
>
> Tras la aplicación de los criterios de inclusión y exclusión, se seleccionaron 45 artículos científicos. La distribución temporal de las publicaciones evidencia que el 15% (n=7) se publicó en 2018, el 20% (n=9) en 2019, el 25% (n=11) en 2020, el 22% (n=10) en 2021 y el 18% (n=8) en 2022. Se observa un pico de producción científica en el año 2020.

> **3.2. Enfoques metodológicos empleados**
>
> Del total de la muestra, el 60% (n=27) de los estudios emplearon un enfoque cuantitativo, utilizando principalmente encuestas a estudiantes. El 30% (n=13) correspondió a enfoques cualitativos, basados en entrevistas semiestructuradas a docentes, y el 10% restante (n=5) utilizó métodos mixtos.

> **3.3. Herramientas de Inteligencia Artificial más reportadas**
>
> Los datos extraídos de los artículos revelan que las herramientas más utilizadas en la educación superior son los Sistemas de Tutoría Inteligente (STI), reportados en el 40% de los estudios. En segundo lugar, se identifican los sistemas de evaluación automatizada en el 35% de los artículos, y en tercer lugar, los asistentes conversacionales (Chatbots) en el 25% de la literatura analizada.

> **3.2. Principales afectaciones reportadas en la salud mental**
>
> La información extraída de los artículos analizados permite agrupar las afectaciones en tres grandes tendencias. Como se observa en la Figura 1, el 68% de los estudios (n=34) reporta un aumento en los niveles de estrés y ansiedad. El 52% (n=26) de la literatura indica la presencia de fatiga digital o «burnout» por la sobreexposición a videollamadas. Finalmente, el 40% (n=20) de los artículos documenta alteraciones en los hábitos de sueño (insomnio).
>
> *(Figura 1 de barras con «68% (n=34)», «52% (n=26)», «40% (n=20)»; nota: «Los porcentajes son no aditivos y no suman 100%, reflejando múltiples afectaciones por estudio»; «Nota. Elaboración propia a partir de los 50 artículos seleccionados (2019-2023).»)*

> **3.1. Distribución geográfica de los estudios**
>
> De los 50 artículos que conformaron la muestra final, el 45% (n=22) se llevó a cabo en Europa, el 30% (n=15) en América del Norte, el 15% (n=8) en Asia y el 10% (n=5) en América Latina.

> **3.1. Descripción general de la muestra**
>
> Se analizaron un total de 35 estudios empíricos. El 70% de estos estudios fueron de naturaleza transversal, mientras que el 30% restante correspondió a estudios longitudinales. El tamaño de las muestras en los artículos analizados osciló entre 150 y 2,500 participantes.

> **3.2. Estrategias de afrontamiento implementadas por las organizaciones**
>
> A partir de la síntesis de la literatura, se identificaron las acciones que las empresas reportaron implementar para mitigar los efectos del teletrabajo en la salud mental:
>
> - Flexibilidad horaria: 28 de los 35 estudios (80%) mencionan la implementación de horarios flexibles y el derecho a la desconexión digital como la principal medida adoptada.
> - Soporte psicológico: 19 estudios (54%) reportan que las organizaciones ofrecieron programas de asistencia al empleado (EAP) o acceso a terapia psicológica en línea.
> - Reestructuración de espacios: 12 investigaciones (34%) documentan la entrega de apoyos económicos para la adecuación de espacios de trabajo en casa (ergonomía).
> - Capacitación en gestión del tiempo: Únicamente 8 estudios (22%) indican que se brindaron talleres para que los empleados gestionaran mejor sus cargas.

> **3.2. Tecnologías implementadas y su reporte en la literatura**
>
> A continuación, se presentan las tecnologías identificadas en los artículos analizados y la frecuencia con la que los autores reportan su uso para la gestión de inventarios.
>
> **Tabla 1**
>
> *Tecnologías de la Industria 4.0 aplicadas a la gestión de inventarios*
>
> | Tecnología | Hallazgo reportado en la literatura | Frecuencia (n) | Porcentaje |
> |---|---|---|---|
> | **IoT (Internet de las Cosas)** | Monitoreo en tiempo real de niveles de stock | 32 | 80% |
> | **Big Data y Analítica** | Predicción de la demanda y optimización de compras | 25 | 62% |
> | **RFID** | Trazabilidad automatizada de productos | 18 | 45% |
> | **Drones** | Conteo cíclico automatizado en almacenes | 8 | 20% |
>
> *Nota.* Datos extraídos de los 40 artículos seleccionados. Un estudio puede reportar el uso de más de una tecnología.

> **3.1. Tipos de vulnerabilidades más frecuentes**
>
> Del total de 42 artículos seleccionados, se extrajeron las vulnerabilidades más comunes reportadas en arquitecturas de microservicios. El 65% de los estudios (n=27) reporta problemas de seguridad en las APIs (Interfaces de Programación de Aplicaciones). El 48% (n=20) identifica fallos en la autenticación y autorización (IAM), y el 35% (n=15) documenta vulnerabilidades relacionadas con la inyección de código.

Por qué cumplen: no dicen «el teletrabajo es malo» ni «el IoT es lo mejor»; solo presentan lo que reporta la literatura, con porcentaje y n, agrupado por categoría y sin nombrar a ningún autor.
