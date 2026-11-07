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
| Forma | **Registro agregable primero** (según `response_type`); luego 0–2 frases de **contexto específicas del estudio** (no la misma frase genérica en todo el lote) |
| Tema RSL | No sustituir el registro con párrafos genéricos de encaje |
| Evidencia | **MD del cribado-2** + opcional `pnpm -s cribado2:query docs/<slug> "…"` (Graphify sobre `cribado2/.../graphify-out/graph.json`); traza `evidence[]` con `loc` anclado (`p.` / `l.` / `§` / `Sección …`), **no** `fulltext` salvo `manifest.json` → `evidence_loc_whitelist` |
| Pre-apply | **`pnpm -s formulario:verify-apply-json docs/<slug> [carpeta] <rutas>`** — rutas desde la raíz del repo, p. ej. `docs/<slug>/resultados/formulario/<carpeta>/debate/lote-NN` (mismos criterios que `lint-traza` sobre `evidence`) |
| Ausente | Excel **`—`**, `decision: absent` |
| Prohibido | `formulario:extract-lote`, inglés crudo, `Sí`/`No` solos, `\|` tipo plantilla |
| Unicidad | No reutilizar el mismo párrafo en **dos `item_id` distintos** del mismo estudio; el estudio **mixto** repite el mismo ítem en dos hojas (correcto). Excepción: `manifest.json` → `duplicate_value_whitelist` |
| Evidencia | Cada slot con contenido: `evidence[]` con `src`, `loc`, `quote` (≥ 40 caracteres; `quote` = **literal** del `src`, no copia del `value`); **RQ3-I1** con valor numérico: alguna `quote` contiene la cifra |

Los `hint` de `items.json` guían **qué buscar**, no el texto final de la celda.

## Política celda ↔ traza

| Situación | Excel | `decision` |
| --------- | ----- | ---------- |
| Tema del ítem no reportado | `—` | `absent` |
| Contenido claro en texto completo | Prosa ES (humanize) | `extracted` |
| Parcial (mixto con huecos) | Prosa con «no reporta…» donde falte subcampo | `partial` |
| Tangencial / poco útil para síntesis | `—` o prosa breve justificada | `omitted` |

## Micro-lote (~5) y paralelización

- **Recomendado ~5** `corpus_id` por `debate/lote-NN` (5–10 según carga). Varias subtareas en paralelo (una por artículo); un solo `apply-lote` al cerrar el micro-lote.

## Eficiencia (prioridades)

1. **Verify antes de apply:** `formulario:verify-apply-json` sobre los `apply-*.json` del lote.
2. **E11 vs E12:** **E11** = traza incompleta mientras falten slots (normal a mitad; `lint-traza` puede FAIL). **E12** / cierre = `extraccion_complete` solo tras **`formulario:stamp`** con traza completa y PASS estrictos.
3. **Lectura mínima:** una `cribado2:query` acotada con `corpus_id` + **solo el fragmento** del MD que citen los nodos.

## Flujo por artículo (compacto)

Orden: **`cribado2:outline`** → **`Read` por rango de línea** del MD (no el archivo entero) → (si hace falta) `cribado2:query ... --article <corpus_id>` para localizar → (último recurso) PDF.

1. Autor (agente principal o **defensor-rsl**, modo `extraccion-formulario`) redacta `apply-<corpus_id>.json`; `r1-defensor-<corpus_id>.md` es opcional y breve.
2. **`pnpm -s formulario:verify-apply-json docs/<slug> [carpeta] docs/<slug>/resultados/formulario/<carpeta>/debate/lote-NN`** actúa como **R2 automatizado**: errores bloquean el apply; las líneas **REVISAR** marcan slots dudosos.
3. **critico-rsl** revisa **solo los slots REVISAR** → `r2-critico-<corpus_id>.md`. Sin REVISAR, no hay r2.
4. **orquestador-extraccion-rsl** solo si hay discrepancia factual o de omisión.
5. **humanize-academic-writing** sobre la frase de cada `value`.
6. **`pnpm -s formulario:apply-lote docs/<slug> NN`** — re-sincroniza **fila 2** al guardar.

Pendientes: `pnpm -s formulario:pending docs/<slug>`. Incidencias no triviales → append `extraccion-orquestador.md`.

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

Tras **todos** los lotes (traza completa): `pnpm -s formulario:lint-traza docs/<slug>` (estructura + evidencia) y `pnpm -s formulario:lint-prosa docs/<slug>` (prosa; admite `--strict` localmente). A mitad de extracción, **E11** por líneas `< esperado` es esperable.

**Carpeta cerrada:** `pnpm -s formulario:stamp docs/<slug> <carpeta>` — ejecuta **`lint-traza --strict`** y **`lint-prosa --strict`** (0 WARN); exige `lint-setup` PASS. Si `manifest.nature_needs_review` no está vacío, el stamp **falla** salvo `pnpm -s formulario:stamp docs/<slug> <carpeta> --allow-nature-review`. Escribe `extraccion_complete: true` y actualiza `resultados/formulario/latest.txt`.

## Forbidden

- **`pnpm -s formulario:extract-lote`** en producción (bypass de debate; solo qa/dev explícito).
- **`pnpm -s formulario:apply-lote`** sin **verify-apply-json** OK en los JSON del lote.
- Escribir Excel ítems sin traza coherente.
- Modificar biblio 3–13 desde apply (usar **prepare**).
