# Apply formulario — ítems RQ (rsl-resultado-formulario-apply)

Fuente ítems: [`extraccion-items-rsl.md`](extraccion-items-rsl.md) · Calidad por ítem: [`formulario-extraccion-items-calidad.md`](formulario-extraccion-items-calidad.md)

Prosa: [`formulario-prosa-rsl.md`](formulario-prosa-rsl.md) (**humanize-academic-writing** obligatorio).

## Precondiciones mapa

- `formulario-map.json` v2: `placement[sheet].study_index` = **`si_order`** (mixto: mismo número en ambas hojas); escribir celdas con `placement.column`.
- Excel en **`docs/<slug>/resultados/formulario/…`**, no en `global/`.

## Contrato de celda (Excel filas 17–33)

| Regla | Detalle |
|-------|---------|
| Idioma | **Español** (informe RSL) |
| Forma | **Registro agregable primero** (según `response_type`); luego 0–2 frases de contexto |
| Tema RSL | No sustituir el registro con párrafos genéricos de encaje |
| Evidencia | Graphify cribado-2 + MD/PDF con `loc`; traza `evidence[]` |
| Ausente | Excel **`—`**, `decision: absent` |
| Prohibido | `formulario:extract-lote`, inglés crudo, `Sí`/`No` solos, `\|` tipo plantilla |
| Unicidad | No reutilizar el mismo párrafo en **dos `item_id` distintos** del mismo estudio; el estudio **mixto** repite el mismo ítem en dos hojas (correcto). Excepción: `manifest.json` → `duplicate_value_whitelist` |
| Evidencia | Cada slot con contenido: `evidence[]` con `src`, `loc`, `quote` (≥ 40 caracteres); **RQ3-I1** con valor numérico: alguna `quote` contiene la cifra |

Los `hint` de `items.json` guían **qué buscar**, no el texto final de la celda.

## Política celda ↔ traza

| Situación | Excel | `decision` |
| --------- | ----- | ---------- |
| Tema del ítem no reportado | `—` | `absent` |
| Contenido claro en texto completo | Prosa ES (humanize) | `extracted` |
| Parcial (mixto con huecos) | Prosa con «no reporta…» donde falte subcampo | `partial` |
| Tangencial / poco útil para síntesis | `—` o prosa breve justificada | `omitted` |

## Debate (por artículo, lote de 10)

1. **defensor-rsl** (`extraccion-formulario`) — borrador prosa ES + evidencia → `r1-defensor-<corpus_id>.md`
2. **critico-rsl** — checklist prosa (ver formulario-prosa-rsl) → `r2-critico-<corpus_id>.md`
3. **R3** si disconformes
4. **orquestador-extraccion-rsl** — veredicto → **`humanize-academic-writing`** sobre cada `value` → `apply-<corpus_id>.json`
5. **`pnpm -s formulario:apply-lote docs/<slug> NN`** — re-sincroniza **fila 2** al guardar.

Incidencias no triviales → append `extraccion-orquestador.md`.

## Payload `apply-<corpus_id>.json`

```json
{
  "article_id": "R016",
  "slots": [
    {
      "item_id": "RQ1-I2",
      "value": "El estudio no desagrega…",
      "decision": "extracted",
      "evidence": [{"src": "docs/.../md/R016-....md", "loc": "p.4", "quote": "…"}]
    }
  ]
}
```

Opcional en debate: `value_draft` (defensor) vs `value` (final humanizado).

## Cierre del run

Tras todos los lotes: `pnpm -s formulario:lint-traza` y `pnpm -s formulario:lint-prosa` (0 FAIL).

**Carpeta cerrada:** `pnpm -s formulario:stamp docs/<slug> <carpeta>` — solo si `lint-setup`, `lint-traza` y `lint-prosa` PASS; escribe `extraccion_complete: true` y actualiza `resultados/formulario/latest.txt`.

## Forbidden

- **`pnpm -s formulario:extract-lote`** en producción (bypass de debate; solo qa/dev explícito).
- Escribir Excel ítems sin traza coherente.
- Modificar biblio 3–13 desde apply (usar **prepare**).
