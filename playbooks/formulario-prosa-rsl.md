# Prosa de celdas — formulario UTP (prepare biblio + apply ítems)

Cadena acotada para **texto que va al Excel** (no sustituye [`prosa-rsl.md`](prosa-rsl.md) del informe completo).

## Cuándo

- **Apply:** cada `value` de ítem RQ (filas 17–33) tras veredicto del orquestador, **antes** de `apply-<id>.json` y `formulario:apply-lote`.
- **Prepare (biblio):** frases cortas en filas 3–13 cuando el dato viene del artículo o de web (1 línea; no párrafo).

## Paso 1 — humanize-academic-writing (obligatorio en apply)

Leer [`.agents/skills/humanize-academic-writing/SKILL.md`](../.agents/skills/humanize-academic-writing/SKILL.md).

Entrada: borrador en **español** del defensor (hecho a partir del MD/PDF indexado, **no** copiar inglés literal).

Objetivo por celda de ítem:

| Parámetro | Guía |
|-----------|------|
| Extensión | **1–3 oraciones**, ~25–70 palabras |
| Contenido | Qué reporta el artículo **respecto al ítem** (texto columna B / `summary` en `items.json`) + enlace breve al **tema RSL** (`informe-polish.md`) |
| Negativas | Nunca «No» o «Sí» solos; explicar (p. ej. «No estratifica por perfil neurodivergente; analiza la muestra como grupo único») |
| Ausencia | Celda **`—`**; traza `decision: absent` |
| Prohibido | Plantillas `Campo: X \| Valor: Y`, listas de keywords en inglés, pegar frases del PDF en EN |

## Paso 2 — Revisión crítico (checklist)

El crítico (`extraccion-formulario`) rechaza si:

- Queda texto mayoritariamente en inglés sin traducir/sintetizar.
- Hay menos de ~20 palabras útiles sin ser telegrafía.
- Persisten pipes `\|` de plantilla de `hint`.
- Falta relación mínima con el ítem o el tema RSL.

## Ejemplos (ítem RQ1-I2 — estratificación)

**Mal:** `No`

**Mal:** `no stratification mention`

**Bien:** «El estudio no desagrega resultados por perfil cognitivo o neurodivergente; reporta efectos agregados sobre la muestra global de participantes con dificultades de aprendizaje, lo que limita comparar perfiles en la síntesis de inclusión cognitiva.»

## Biblio (filas 3–13)

- **Una línea** por celda (país, contexto, volumen, N muestra, editorial).
- Español; dato atribuible al artículo, CSV o fuente web citada en `biblio-traza.jsonl`.
- Sin dato fiable → **`—`**.

## Lint (fase script, opcional)

`formulario:lint-prosa` validará telegrafía y plantillas; ver skill **apply**.
