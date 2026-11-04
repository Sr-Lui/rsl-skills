# Prepare formulario UTP (rsl-resultado-formulario-prepare)

## Salida

`docs/<slug>/resultados/formulario/<timestamp>/`

- `Formulario.xlsx` — copia extendida (N columnas = N SI)
- `formulario-map.json` — estudios, ítems, lotes de 10
- `manifest.json` — hashes y `n_si`

## Perfil bibliográfico (filas 3–13)

| Fila | Campo | Origen |
| ---- | ----- | ------ |
| 3 | DOI | CSV |
| 4 | Título | CSV |
| 5 | Autores | CSV |
| 6 | Año | CSV |
| 7 | Revista | CSV |
| 8–10, 12–13 | Editorial, país, contexto, volumen, muestra | CSV si existe; si no → **artículo**; si no → **blanco** |
| 11 | Tipo de estudio | CSV «Tipo de documento» |

**No inferir.** No usar solo el abstract.

## Columna B (ítems)

Texto `summary` de `items.json` en filas 17–20, 23–26, 29–33 según `response_type` (mixto → ambas hojas).

## Comandos

```bash
pnpm -s formulario:prepare docs/<slug>
pnpm -s formulario:lint-setup docs/<slug>
pnpm -s formulario:stamp docs/<slug> <carpeta>
```
