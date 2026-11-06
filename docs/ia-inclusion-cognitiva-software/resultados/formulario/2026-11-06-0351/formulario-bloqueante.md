# Formulario bloqueante — no continuar síntesis

**Tema:** `docs/ia-inclusion-cognitiva-software`
**Carpeta:** `resultados/formulario/2026-11-06-0351/`

## Por qué

El formulario no supera el gate automático (`formulario:lint-traza`, `formulario:lint-prosa`, `manifest.extraccion_complete`). La síntesis no debe recodificar celdas ni corregir extracción aquí; corregir con **rsl-resultado-formulario-apply** y cerrar con `formulario:stamp`.

## Errores (FAIL)

1. E12: manifest extraccion_complete != true — cierra con `pnpm -s formulario:stamp docs/<slug> <carpeta>` tras lint-traza y lint-prosa PASS
2. falta extraccion-traza.jsonl
3. falta extraccion-traza.jsonl

## Avisos (WARN)

(ninguno)

## Comandos

```bash
pnpm -s formulario:lint-traza docs/ia-inclusion-cognitiva-software 2026-11-06-0351
pnpm -s formulario:lint-prosa docs/ia-inclusion-cognitiva-software 2026-11-06-0351
```

Tras corregir todos los FAIL: `pnpm -s formulario:stamp docs/<slug> <carpeta>` (marca `extraccion_complete` y actualiza `latest.txt`).

## Prompt para rsl-resultado-formulario-apply

```text
Usa rsl-resultado-formulario-apply sobre docs/ia-inclusion-cognitiva-software. 
Corrige la extracción en los lotes afectados: evidencia con quote≥40 y loc concretos; 
un valor no puede copiarse en dos item_id distintos del mismo estudio (salvo excepción en 
manifest duplicate_value_whitelist). Vuelve a aplicar apply-lote, luego 
pnpm -s formulario:lint-traza docs/ia-inclusion-cognitiva-software 2026-11-06-0351 y 
pnpm -s formulario:lint-prosa docs/ia-inclusion-cognitiva-software 2026-11-06-0351; cierra con 
pnpm -s formulario:stamp docs/ia-inclusion-cognitiva-software 2026-11-06-0351.
```

