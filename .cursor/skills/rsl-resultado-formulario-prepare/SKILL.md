---
name: rsl-resultado-formulario-prepare
description: >-
  Prepara Excel UTP: mapa v2 (placement por naturaleza), columna B ítems;
  classify-nature (columnas por hoja); biblio 3–13; lint y stamp.
  Paso web opcional para huecos. Cierra con lint-setup y stamp. Tras rsl-resultado-items.
---

# rsl-resultado-formulario-prepare

Playbooks: [`formulario-prepare-rsl.md`](../../playbooks/formulario-prepare-rsl.md) · [`formulario-prosa-rsl.md`](../../playbooks/formulario-prosa-rsl.md) (biblio: 1 línea ES)

Tras classify, revisar opcionalmente `manifest.nature_needs_review` y `nature-overrides.json` antes de biblio-enrich.

Invoke: `Usa rsl-resultado-formulario-prepare sobre docs/<slug>/`

## Precondiciones

- `resultado-items:status` PASS · `cribado2:status` OK (PDF + `docs/md/` indexados)
- `.venv-formulario` (`openpyxl`, `pyyaml`)

## Procedure (orden fijo)

1. **`pnpm -s formulario:prepare docs/<slug>`**  
   Carpeta timestamp, `formulario-map.json` **v2** (73 estudios, `placement` vacío), columna B ítems. **Sin** columnas de estudio aún.

2. **`pnpm -s formulario:classify-nature docs/<slug> <carpeta>`**  
   Heurística MD + CSV → `study_nature` (solo mapa/traza, **no** fila Excel).  
   Layout: columnas **solo** en hoja(s) UTP correctas; biblio CSV filas **3–7, 11** ahí.  
   Opcional: `nature-overrides.json` por `corpus_id`. Traza: `nature-traza.jsonl`.

3. **`pnpm -s formulario:biblio-enrich docs/<slug> <carpeta>`**  
   Rellena **Editorial (8), País (9), Contexto (10), Volumen (12), Tamaño muestra (13)** **solo** en hojas con `placement`:
   - **Web:** Crossref por DOI (`publisher`, `volume`, afiliaciones → país).
   - **Artículo:** MD en `RSL/picoc/…-cribado-2-…/docs/md/` (muestra, contexto, volumen en cabecera IEEE, etc.).
   - **`—`** solo si no hay fuente fiable (no inventar).
   - Escribe **`biblio-traza.jsonl`** (`source`: `web` | `article` | `dash`; `evidence`).
   - Casos verificados a mano: ampliar `MANUAL_ROW13` en `scripts/formulario_biblio_enrich.py` si hace falta.
   - Re-ejecutar con **`--force`** tras cambiar heurísticas o MD.

4. **Huecos (opcional)** — solo celdas aún vacías o `—`:
   - Leer MD / `graphify query` **no sustituye** cifras (devuelve índice del grafo); usar **lectura de chunks** en MD o **WebSearch** (DOI + título).
   - Ajustar Excel + append en `biblio-traza.jsonl` (`source`: `web`).
   - Documentar lote grande en `biblio-gap-fill-notes.md` (referencia; no sustituye traza).

5. **`pnpm -s formulario:lint-setup docs/<slug> <carpeta>`**  
   PASS: `nature_classified`, conteos fila 2 **por hoja**, biblio 8–10/12–13 en placement.

6. **`pnpm -s formulario:stamp docs/<slug> <carpeta>`**  
   Actualiza `latest.txt` · `manifest.json` (`biblio_enriched`, etc.).

## Contrato biblio (filas 8–10, 12–13)

| Fila | Campo | Formato |
|------|--------|---------|
| 8 | Editorial | Nombre editorial (IEEE, Elsevier, ACM…) |
| 9 | País de origen | País ES (afiliación 1.º autor o texto) |
| 10 | Contexto de aplicación | 1 frase ES (sanitario, educativo, co-diseño, experimento…) |
| 12 | Volumen | Número, acta de congreso abreviada, o «Online first…» |
| 13 | Tamaño muestra | `n = … participantes`, respuestas, «Sin participantes humanos…», etc. |

**No** inferir solo del abstract del CSV. **No** párrafos largos.

## Forbidden

- Rellenar filas ítem **17–33** (skill **apply**).
- **`formulario:extract-lote`** · apply-lote en prepare.
- Stamp sin **classify-nature** + **biblio-enrich**.

## Comandos

```bash
pnpm -s formulario:prepare docs/<slug>
pnpm -s formulario:classify-nature docs/<slug> <carpeta>   # [--force]
pnpm -s formulario:biblio-enrich docs/<slug> <carpeta>    # [--force]
pnpm -s formulario:lint-setup docs/<slug> <carpeta>
pnpm -s formulario:stamp docs/<slug> <carpeta>
```

`formulario:biblio-graphify` — solo respaldo experimental (Graphify no extrae bien *n*); preferir MD + enrich.

## Cierre

`OK: formulario preparado (biblio 3–13). Próximo: **rsl-resultado-formulario-apply** lote 01.`
