# rsl-resultado-formulario — especificación (pendiente de implementar)

Documento maestro de lo que se creará en el repo. **Estado:** Fase 0–1 hecha (manifest, CSV, ítems); **Fase 2** (`formulario:prepare`) y **skill Cursor** aún no existen.

Invoke previsto: `Usa rsl-resultado-formulario sobre docs/<slug>/`.

---

## Objetivo

Rellenar el Excel UTP [`global/Formulario de extracción de información.xlsx`](global/Formulario%20de%20extracción%20de%20información.xlsx) (hojas **Cuantitativo** / **Cualitativo**) a partir de:

- `items.json` vía `resultados/items/latest.txt` (13 ítems, `summary`, `response_type`, `hint`)
- `resultados-<MARCO>-cribado-2.csv` — universo PRISMA cribado 2 (**146** filas en tema activo; **73** con `¿Se acepta?` = SI, incluye PODRIA/relleno según `cribado2:apply`)
- Graphify cribado-2: `pnpm cribado2:query docs/<slug> "…"`
- Debate **defensor-rsl** / **critico-rsl** (modo `extraccion-formulario`) + **orquestador-extraccion-rsl**

Salida: Excel versionado + **`extraccion-traza.jsonl`** (+ opcional `extraccion-decisiones.json`) + **`extraccion-orquestador.md`** (incidencias por lote).

**Siguiente skill (fuera de alcance aquí):** `rsl-resultado-formulario-polish`.

---

## Secuencia obligatoria

| Orden | Entregable | Estado tema inclusión cognitiva |
|------|------------|----------------------------------|
| A | `rsl_pipeline` en `RSL/index-manifest.json` | Hecho |
| B | CSV ↔ evaluación ↔ `items.md` (`n_incluidos_si` = 40) | Hecho |
| C | `scripts/resultado-formulario.py` + `openpyxl` + `formulario-map.json` | **Pendiente** |
| Gate | `resultado-items:status` PASS · `cribado2:status` OK · `formulario:prepare` OK | Items PASS; prepare NO |
| D | Skill + playbook + llenado por lotes | **Pendiente** |

---

## Archivos a crear

| Artefacto | Ruta |
|-----------|------|
| Skill | `.cursor/skills/rsl-resultado-formulario/SKILL.md` |
| Playbook | `playbooks/extraccion-formulario-rsl.md` |
| Script | `scripts/resultado-formulario.py` |
| Agente (opcional) | `.cursor/agents/orquestador-extraccion-rsl.md` o sección en skill |
| Extensiones agentes | Modo **`extraccion-formulario`** en `defensor-rsl.md` y `critico-rsl.md` |
| Salida por run | `docs/<slug>/resultados/formulario/<timestamp>/Formulario.xlsx`, `formulario-map.json`, `manifest.json`, `debate/lote-NN/`, `extraccion-traza.jsonl` |

---

## Comandos (`package.json`)

| Comando | Función |
|---------|---------|
| `formulario:prepare docs/<slug>` | Copia plantilla, columna B = `summary`, columnas C+ = estudios del CSV, genera `formulario-map.json` |
| `formulario:status docs/<slug>` | Progreso por artículo / lote |
| `formulario:lint docs/<slug>` | Traza 1:1, coherencia `decision` ↔ celda |
| `formulario:stamp docs/<slug> <carpeta>` | `latest.txt`, actualiza `rsl_pipeline.formulario_latest` |

Auxiliares ya existentes: `pnpm rsl:pipeline-sync`, `pnpm cribado2:eval-csv`, `pnpm cribado2:query`.

---

## `formulario-map.json` (diseño)

Por **columna Excel** (estudio):

- `csv_id` — columna `Id` del CSV cribado-2
- `corpus_id` — id en `documentos.json` (mapeo por **DOI**; ids CSV ≠ ids corpus)
- `doi`, `acepta` (SI/NO), `extraccion_tier`: `full` | `metadata_only`
- `has_pdf`, `pdf_path`, `graph_query_id` (= `corpus_id` si indexado)
- `column`, `sheets[]` (Cuantitativo / Cualitativo según ítem + vista del estudio)

Por **ítem** (filas): `item_id`, `sheet`, `row`, `rq`, `picoc_component`, `response_type`.

Lotes de **10** estudios (orden estable en mapa).

---

## Plantilla Excel (sin cambiar diseño)

- Columna **B**: etiquetas; filas ítem = textos `summary` de `items.json`
- **Datos generales** filas ~3–13 desde CSV
- **RQ1** ~17–20 (4 ítems), **RQ2** ~23–26 (4), **RQ3** ~29–33 (5; celda B puede decir RQ3 (C) en PIO → componente O)
- **Mixto** en ítem → fila en **ambas** hojas; estudio mixto → columnas en ambas hojas

---

## Política celda vs traza

| Situación | Excel | `decision` en JSONL |
|-----------|-------|---------------------|
| Tema del ítem ausente en texto completo | **Vacío** | `absent` |
| Contenido relevante (ítem + PICOC + tema RSL) | Valor breve (`hint`) | `extracted` |
| Tangencial, poco útil | Vacío o valor (debate) | `omitted` o `extracted` + `marginal` |
| Plantilla mixta, subcampo ausente | `NR` solo en subcampo | `partial` |

Prohibido: inventar; inferir solo del abstract; celda con texto sin traza `extracted`/`partial`.

Tema RSL: `docs/<slug>/informe-polish.md`.

---

## Debate (por lote de 10)

Dentro del lote, **un artículo a la vez**:

1. **R1 — defensor-rsl:** propone valor + `decision` + evidencia (Graphify/MD).
2. **R2 — critico-rsl:** `conforme` / `disconforme` por ítem.
3. **R3 (solo disconformes):** ajuste; si persiste → **orquestador** cierra con óptimo razonado (`forced_resolution: true`, sin inventar evidencia).
4. **Orquestador:** veredicto final + filas en **`extraccion-orquestador.md`** (solo incidencias).

Excel y traza se escriben **después** del veredicto del orquestador.

Artefactos: `debate/lote-NN/r1-defensor-<id>.md`, `r2-critico-<id>.md`, `r3-*.md`.

---

## Traza (`extraccion-traza.jsonl`)

Una línea JSON por slot ítem×estudio:

`article_id`, `item_id`, `rq`, `picoc_component`, `sheet`, `cell`, `value`, `decision` (`absent`|`extracted`|`partial`|`omitted`), `topic_in_article`, `theme_relevance`, `theme_anchor`, `picoc_question`, `evidence[]`, `debate_rounds`, `orchestrator_verdict`, `rationale`, `forced_resolution`.

Opcional: `extraccion-decisiones.json` agregado al `stamp`.

---

## Precondiciones skill

- `pnpm -s resultado-items:status docs/<slug>` → PASS
- `pnpm -s cribado2:status docs/<slug>` → OK (rebuild si stale: **rsl-cribado-2-memoria**)
- `rsl_pipeline` coherente (`pnpm rsl:pipeline-sync`)
- `formulario:prepare` ejecutado y mapa revisado

---

## Corpus PDF vs CSV (tema activo)

Tras alineación manual (2026-11-04, usuario + integración):

- **73 / 73 SI** del CSV (146 filas) con PDF en corpus cuando `descargado=si` — revalidar cobertura tras apply
- **13 registros** añadidos a `documentos.json` (estudios del CSV que no estaban en retrieval)
- Graphify cribado-2: **`cribado2:status` OK** — ~7119 nodos, integridad OK
- Excepción **R567** (no está en los 40 SI): PDF Unpaywall incorrecto → `descargado=no` hasta JMIR manual
- **R606** (SI R078): PDF corregido desde HAL (`hal-05716911`)

Tras añadir PDFs: `pnpm cribado2:align` (pdf-draft) → `cribado2:prepare` → `cribado2:build` (usar Python de pipx `graphifyy` si hace falta).

### Descarga manual pendiente (usuario)

Coloca el PDF en `…/docs/pdf-draft/` con nombre parecido al título y ejecuta `pnpm cribado2:align docs/ia-inclusion-cognitiva-software`.

| Id CSV | Id corpus | DOI | Motivo automático | Enlace sugerido |
|--------|-----------|-----|-------------------|-----------------|
| R012 | — | 10.1145/3748333 | ACM / paywall | https://dl.acm.org/doi/pdf/10.1145/3748333 |
| R014 | — | 10.1145/3663547.3746355 | ACM / paywall | https://dl.acm.org/doi/pdf/10.1145/3663547.3746355 |
| R021 | — | 10.1080/17483107.2025.2579822 | Taylor & Francis | https://www.tandfonline.com/doi/pdf/10.1080/17483107.2025.2579822 |
| R029 | — | 10.1145/3800424.3800432 | ACM W4A | https://doi.org/10.1145/3800424.3800432 |
| R051 | — | 10.1145/3704637.3734738 | ACM | https://dl.acm.org/doi/pdf/10.1145/3704637.3734738 |
| R057 | — | 10.1145/3706468.3706483 | repositorio / ACM | https://dspace.library.uu.nl/handle/1874/482787 |
| R077 | — | 10.1145/3786304.3787926 | ACM CHIIR | https://doi.org/10.1145/3786304.3787926 |
| R082 | — | 10.1080/10447318.2026.2618562 | repositorio | https://hdl.handle.net/20.500.14352/139380 |
| R083 | — | 10.1145/3764687.3764713 | Bristol Research | https://research-information.bris.ac.uk/en/publications/202e26da-f8e2-4edd-b1e7-5bed24640953 |
| R084 | R482 | 10.1007/978-981-96-2071-5_16 | capítulo Springer | https://hal.science/hal-04860245v1/document |

### Ya en `pdf-draft` (descarga automática OK; falta alinear)

| Archivo |
|---------|
| R018-enhancing-user-experience-in-virtual-reality-for-children-with-autism-a-signific.pdf |
| R026-large-language-models-for-web-accessibility-a-systematic-literature-review.pdf |
| R031-toward-neurodivergent-aware-productivity-a-systems-andai-based-human-in-the-loop.pdf |
| R038-summarylens-a-smartphone-app-for-exploring-interactive-use-of-automated-text-sum.pdf |

---

## QA / README

- Fila en `README.md` con comandos `formulario:*`
- Caso mínimo en `scripts/qa-destroy.py`: `rsl_pipeline.formulario_latest` tras stamp
- Cierre `rsl-resultado-items` → apunta a esta skill tras gate

---

## Referencia

Plan Cursor: `rsl-resultado-formulario` y `readiness_skill_formulario` en `.cursor/plans/`.
