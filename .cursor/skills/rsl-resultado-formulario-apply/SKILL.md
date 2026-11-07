---
name: rsl-resultado-formulario-apply
description: >-
  Rellena celdas de ítems RQ del formulario UTP por micro-lotes (~5 estudios): debate ligero
  defensor/critico (extraccion-formulario), orquestador solo si hay discrepancia, humanize-academic-writing,
  verify-apply-json, extraccion-traza.jsonl, formulario:apply-lote. Prosa ES, precisa, no plantillas.
  Requiere formulario:stamp. Use rsl-resultado-formulario-apply. No formulario:extract-lote en producción.
---

# rsl-resultado-formulario-apply

Playbooks: [`formulario-apply-rsl.md`](../../playbooks/formulario-apply-rsl.md) · [`formulario-prosa-rsl.md`](../../playbooks/formulario-prosa-rsl.md) · [`formulario-extraccion-items-calidad.md`](../../playbooks/formulario-extraccion-items-calidad.md)

Invoke: `Usa rsl-resultado-formulario-apply sobre docs/<slug>/` · `lote 03`

## Prioridades (efectividad / tokens)

1. **`pnpm -s formulario:verify-apply-json`** sobre los `apply-*.json` del lote **antes** de cada `apply-lote` — evita rehacer lotes por citas (substring, longitud, `loc`).
2. **Lint incremental:** **E11** = traza incompleta mientras falten estudios/ítems (esperable a mitad; `lint-traza` puede seguir en FAIL). **E12** = `manifest.extraccion_complete != true` hasta **`formulario:stamp`**. No confundir “FAIL intermedio” con extracción cerrada; el gate de **rsl-resultado-sintesis** es `extraccion_complete` tras stamp.
3. **Por artículo en paralelo:** una `cribado2:query` acotada con `corpus_id` en la cadena + **solo el fragmento** del MD que indiquen nodos (`src` / página), no el archivo entero.

## Precondiciones

- `resultados/formulario/latest.txt` · `formulario:lint-setup` PASS
- Excel destino: **`docs/<slug>/resultados/formulario/<carpeta>/Formulario.xlsx`** (no `global/`)
- `items.json` + `## Reglas de registro y agregación` · `informe-polish.md`
- `formulario-map.json` con **`placement`** por hoja (`classify-nature` OK)
- Un `apply-<corpus_id>.json` por artículo; **`apply-lote` escribe solo** donde `placement[sheet]` existe.

## Orden de columnas (fila 2)

- **`study_index` en el mapa = `si_order` global** (orden SI del cribado-2, 1…N).
- **Mixto:** mismo número de cabecera en Cuantitativo y Cualitativo (p. ej. estudio 3 → cabecera **3** en ambas hojas).
- **Columna física:** compacta por hoja (`placement.column`); la cabecera fila 2 muestra el **número global**, no 1…k local.
- `formulario:apply-lote` escribe ítems con `column_index` / `placement.column`; al guardar, el script **re-sincroniza fila 2** (`sync_numbered_headers`).

Ejemplo (5 estudios): Cuant. cabeceras 1, 3, 4, 5 · Cual. cabeceras 2, 3, 5.

## Contrato de celda

- **Registro agregable** visible en la celda (literal o entre paréntesis) + **frase breve** en español; humanize pulir la frase, no borrar el dato.
- **Registro vs matiz:** el registro puede repetirse entre estudios si la literatura converge; la **frase de matiz** debe ser **específica del estudio** (detalle factual del MD), no la misma oración genérica en todo el lote. Si no hay matiz fiable, acorta el texto o usa `partial` y apóyate en una cita literal fuerte en `evidence`.
- **Unicidad por ítem:** no pegar el mismo párrafo en **dos `item_id` distintos** del mismo estudio (el mixto duplica el mismo ítem en dos hojas: eso sí es correcto). Si una excepción documentada lo exige, añade una fila en `manifest.json` → `duplicate_value_whitelist`.
- **Evidencia:** cada slot con contenido lleva `evidence[]` con `src` (ruta al MD del cribado-2 bajo el repo), `loc` (ancla reproducible: `p.`, `l.`, `§`, `Sección …`, etc.; **no** `fulltext` salvo `manifest.json` → `evidence_loc_whitelist`) y `quote` (**≥ 40 caracteres**, **substring literal** del fichero `src`, no copia del `value` de la celda); si `RQ3-I1` tiene **Valor** numérico, al menos una `quote` debe **incluir la cifra**.
- **Ausente:** Excel **`—`**, `decision: absent`.
- Validación en cadena: `pnpm -s formulario:verify-apply-json` (evidencia local en JSON) → `pnpm -s formulario:apply-lote` → al cerrar todo: `pnpm -s formulario:lint-traza docs/<slug>` (estructura + evidencia; **E11** posible hasta traza completa) y `pnpm -s formulario:lint-prosa docs/<slug>` (prosa + dominancia + duplicados entre ítems).

## Micro-lote y paralelización

- **Micro-lote recomendado: ~5** `corpus_id` por carpeta `debate/lote-NN` (convención del tema; puede ser 5–10). Motivo: menos contexto por tanda y **paralelizar** un agente/subtarea por artículo dentro del mismo `NN`.
- Tras los ~5 JSON listos: **un** `pnpm -s formulario:apply-lote docs/<slug> NN` (con o sin `--article` para verificación incremental por estudio).

## Orden eficiente por artículo

1. **`pnpm -s cribado2:query docs/<slug> "<pregunta mínima; corpus_id …; ítem si aplica>"`** — Graphify primero; si la salida es ruidosa o truncada, acotar la pregunta o repetir con menos alcance.
2. **MD solo en el tramo** señalado por nodos (`src`, ancla/página); no volcar el `.md` entero salvo necesidad.
3. (Opcional) fragmento de PDF si el MD no alcanza.

## Debate ligero (por artículo)

1. **R1 defensor-rsl** (`extraccion-formulario`) → `debate/lote-NN/r1-defensor-<corpus_id>.md` — **breve:** 1–3 bullets (pregunta Graphify + nodos útiles o «sin hit» + “siguiente: leer MD Lx–Ly” si aplica).
2. **R2 critico-rsl** → `r2-critico-<corpus_id>.md` — **checklist** (sí/no): ¿evidencia cubre el ítem? ¿`quote` ≥40 y literal del `src`? ¿`loc` anclado? ¿coherencia Graphify ↔ fragmento MD?
3. **orquestador-extraccion-rsl** → **solo si** defensor y crítico discrepan en hechos o riesgo de omisión relevante.
4. **humanize-academic-writing** sobre cada `value` final.
5. `resultados/formulario/<carpeta>/debate/lote-NN/apply-<corpus_id>.json` → **`pnpm -s formulario:verify-apply-json docs/<slug> [carpeta] docs/<slug>/resultados/formulario/<carpeta>/debate/lote-NN`** (o rutas concretas a `apply-*.json`) → `pnpm -s formulario:apply-lote docs/<slug> NN [--article id]`

**Verify:** mismo criterio que evidencia en `lint-traza` (longitud, substring en fichero, `loc`, `quote` ≠ `value`). La `[carpeta]` del formulario es opcional si `latest.txt` apunta al Excel vigente.

Tras todos los lotes (traza completa): `pnpm -s formulario:lint-traza docs/<slug>` · `pnpm -s formulario:lint-prosa docs/<slug>`.

**Cierre:** `pnpm -s formulario:stamp docs/<slug> <carpeta>` — exige `lint-setup` PASS y **`lint-traza --strict`** + **`lint-prosa --strict`** (0 WARN) y bloquea `extraccion_complete` si `manifest.nature_needs_review` no está vacío, salvo **`--allow-nature-review`**. Escribe `extraccion_complete: true` y actualiza `resultados/formulario/latest.txt`.

## Forbidden

- **`pnpm -s formulario:draft-lote`** y **`formulario:extract-lote`** en producción (solo qa/dev explícito)
- `apply-lote` sin **R1 + R2** cerrados y sin **`verify-apply-json` OK** para ese lote
- Saltarse el orquestador cuando defensor y crítico **no** discrepaban (debate ligero); invocarlo solo con desacuerdo factual/por omisión
- Celdas ítem en inglés crudo o telegrafía
- Duplicar columna de estudio en hoja sin `placement`; **reclasificar naturaleza** → usuario ejecuta **`formulario:classify-nature --force`** en prepare (no en apply)
- Tocar filas biblio 3–13 en apply
- Editar cabeceras fila 2 a mano en Excel (dejar que classify / biblio / apply las sincronicen)

## Regenerar placement (usuario / prepare)

Si cambia naturaleza o orden SI, en el **tema** (`docs/<slug>/`):

```bash
pnpm -s formulario:classify-nature docs/<slug> <carpeta> --force
pnpm -s formulario:biblio-enrich docs/<slug> <carpeta> --force
```

Luego re-aplicar lotes si el Excel ya tenía ítems.

## Cierre

`OK: extracción apply completa (prosa ES), stamp y extraccion_complete. Próximo: **rsl-resultado-sintesis** (síntesis de resultados por ítem).`
