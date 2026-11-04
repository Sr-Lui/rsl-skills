# Ítems de extracción RSL (desglose por RQ)

Fuente de verdad para **`rsl-resultado-items`**. Prosa: [`playbooks/prosa-rsl.md`](prosa-rsl.md) (**humanize-academic-writing** obligatorio, luego **`redaccion-rsl`** + `pnpm -s redaccion:lint`; R1–R9 en [`redaccion-academica.md`](redaccion-academica.md)).

Normativa: Kitchenham y Charters (2007), § 6.4, pp. 29–34; PRISMA 2020 ítems 9–10 ([`estandares-rsl.md`](estandares-rsl.md) → `extraccion-datos`).

## Qué es un ítem

Un **ítem** es un campo del formulario de extracción que responde a **una parte concreta** de la pregunta de revisión (RQ) del componente del marco (P, I, O…). Debe ser:

- **Breve** en la etiqueta (objetivo ≈ 12 palabras): ataca un solo fragmento de la pregunta o del «Dato a extraer» del picoc, no resume toda la RQ.
- **Observable** en el texto completo del estudio.
- **Codificable** en una celda (texto breve, categoría, número o «no reportado»).
- **Unívoco**: una decisión de registro por ítem.

La columna «Dato a extraer» del picoc es la semilla; el desglose **no** modifica el picoc.

Ejemplo de etiqueta demasiado larga (mal): «Perfiles de discapacidad cognitiva o neurodivergencia declarados en el estudio con la redacción del artículo». Mejor (bien): «Perfiles declarados (TEA, TDAH, DI, dislexia…)».

## Límites

| Regla | Detalle |
|-------|---------|
| Por RQ | **Mínimo 1**, **máximo 5** ítems |
| Por tema | Una RQ del picoc → una sección `## RQn` en `items.md`; ids `RQn-Ik` consecutivos |
| Bibliografía | Campos comunes (id, título, autores, año, venue, DOI) **no** cuentan en el límite de 5 |
| Duplicados | El mismo dato no aparece en dos RQ salvo justificación en `items-debate.md` |

## Tipo de respuesta (columna **Tipo** — obligatorio)

Valores **únicos** permitidos en la tabla y en el Excel:

| Tipo | Cuándo usarlo |
|------|----------------|
| **cuantitativo** | Conteos, puntuaciones, porcentajes, escalas numéricas |
| **cualitativo** | Categorías, texto, presencia/ausencia sin métrica numérica principal |
| **mixto** | En la misma celda se registran parte numérica y parte categórica o textual (usar poco) |

No uses nominal, categórico, numérico ni texto en la columna **Tipo**.

## Codificación (columna **Codificación** — opcional)

Detalle interno para diseñar la hoja Excel (lint WARN si falta, no FAIL):

- **nominal**, **categórico**, **numérico**, **texto** (y **mixto** solo si la codificación también es híbrida).

Las **Notas** aclaran valores esperados o subcampos.

## Resumen del protocolo (final de `items.md`)

Después de todas las secciones `## RQn`, incluir **`## Resumen del protocolo`**: por componente, la pregunta y la lista de ítems (id + etiqueta breve + tipo). Es la vista «documento» del protocolo; no sustituye las tablas detalladas.

```markdown
## Resumen del protocolo

### P — Población (RQ1)

**Pregunta:** ¿…?

**Ítems:**
- RQ1-I1 — … (cualitativo)
- RQ1-I2 — … (cuantitativo)
```

## Debate (defensor / crítico)

- **Defensor:** conjunto mínimo suficiente; **Tipo** ternario; ítems breves.
- **Crítico:** refuta tipos no ternarios, etiquetas largas, ítems que mezclan dos dimensiones o ignoran el «Dato a extraer».
- **Máximo 2 rondas.** Sin consenso → **ERROR**; no `stamp`.

## Piloto

Kitchenham recomienda pilotar el formulario en una muestra; la ejecución queda fuera de `rsl-resultado-items` (skill Excel futura).
