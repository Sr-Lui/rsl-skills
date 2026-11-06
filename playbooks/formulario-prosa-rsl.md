# Prosa de celdas — formulario UTP (prepare biblio + apply ítems)

Cadena acotada para **texto que va al Excel** (no sustituye [`prosa-rsl.md`](prosa-rsl.md) del informe completo).

## Cuándo

- **Apply:** cada `value` de ítem RQ (filas 17–33) tras veredicto del orquestador, **antes** de `apply-<id>.json` y `formulario:apply-lote`.
- **Prepare (biblio):** frases cortas en filas 3–13 cuando el dato viene del artículo o de web (1 línea; no párrafo).

## Contrato por `response_type` (items.json)

| Tipo | Registro en la celda | Redacción |
|------|----------------------|-----------|
| **cuantitativo** | Categoría/número **`;`** visible (al inicio tipo `No.` / `Pruebas` o en paréntesis) | 1 frase ES que contextualiza sin ocultar el dato |
| **cualitativo** | Etiquetas **`;`** en el texto o en paréntesis | Matiz breve solo si aporta |
| **mixto** | Plantilla literal `Presencia: … \| N: …` (habitualmente al final entre paréntesis) | Intro en español que explica el hecho |

**Ausencia:** celda **`—`**, traza `decision: absent`.

Humanize pulir la intro; **no** quitar el registro literal (pipes y subcampos).

## Paso 1 — humanize-academic-writing (apply)

Leer [`.agents/skills/humanize-academic-writing/SKILL.md`](../.agents/skills/humanize-academic-writing/SKILL.md).

Humanizar la **nota**, no sustituir el **registro** inicial. No alargar cuantitativos con párrafos genéricos de tema RSL.

## Paso 2 — Revisión crítico (checklist)

El crítico (`extraccion-formulario`) rechaza si:

- Ítem **cuantitativo** sin categoría/número explícito al inicio.
- Ítem **mixto** sin claves de plantilla (`Presencia:`, `Constructo:`, …).
- Queda texto mayoritariamente en inglés sin traducir/sintetizar.
- Persisten pipes `\|` **fuera** de plantillas mixtas definidas en `items.md`.
- **Dos ítems distintos** del mismo estudio comparten el mismo párrafo largo (salvo excepción en `duplicate_value_whitelist`).
- **`evidence[]`** vacío o con `quote` demasiado corto (menos de 40 caracteres) cuando `decision` tiene contenido.

## Ejemplos

**RQ1-I2 (cuantitativo)**

- Mal: «No indica estratificación ni análisis desagregados…» (sin **No** explícito).
- Bien: «**No.** Los resultados se reportan sobre la muestra global, sin desagregación por perfil.»

**RQ1-I1 (cualitativo)**

- Bien: `TEA; dificultades de aprendizaje`

**RQ1-I3 (mixto)**

- Bien: «Participación de personas con la condición en diseño y evaluación (Presencia: Sí | N: NR | Rol: ambos).»

**RQ3-I1 (mixto)**

- Bien: «Resultado principal reportado (precision = 6) (Constructo: precision | Valor: 6).»

## Biblio (filas 3–13)

- **Una línea** por celda (país, contexto, volumen, N muestra, editorial).
- Español; dato atribuible al artículo, CSV o fuente web citada en `biblio-traza.jsonl`.
- Sin dato fiable → **`—`**.

## Lint

`pnpm -s formulario:lint-prosa docs/<slug>` valida registro por tipo, evidencia y duplicados en `extraccion-traza.jsonl`.
