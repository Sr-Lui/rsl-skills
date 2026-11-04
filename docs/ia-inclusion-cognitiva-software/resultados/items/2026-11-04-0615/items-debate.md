# Debate — ítems de extracción

**Tema:** ia-inclusion-cognitiva-software · **Picoc:** `picoc/2026-10-03-3-PIO/picoc.md` · **Rewrite desde:** `2026-11-04-0613` · **Versión operativa:** `2026-11-04-0615` (re-ejecución `rsl-resultado-items` solicitada; contenido protocolo = 0613).

## Ronda 1 — Defensor

Propuesta: reetiquetar ítems de **frecuencia / % estudios** como **cuantitativo** (I2, RQ2-I3/I4, RQ3-I4/I5); mantener **cualitativo** en perfiles, rol, instrumento y marco; **mixto** en participación, ética y métrica+valor. Resumen del protocolo con etiquetas largas (12–22 palabras).

ronda-1: 3 RQ, 13 ítems · Tipos: 5 cuantitativo, 5 cualitativo, 3 mixto

## Ronda 1 — Crítico

| Punto | Posición | Motivo |
|-------|----------|--------|
| 9× cualitativo en 0606 | aceptar reetiquetado | Confundía frecuencia en síntesis con «solo cualitativo» |
| Resumen corto | aceptar etiquetas largas | Es la vista operativa del equipo |
| Equilibrio 50/50 | rechazar cuota fija | RQ3 con más cuant es coherente con tablas de resultados |

ronda-1: 3 desacuerdos resueltos

## Ronda 1 — Decisiones

Aceptado reetiquetado semántico + Resumen expandido. Sin cambiar ids ni estructura 0606.

## Mejoras respecto a 2026-11-04-0613

Re-ejecución formal del cierre (lint + stamp). Sin cambio de ítems respecto a 0613 (balance Tipo + Resumen largo ya aplicado).

| Tema | 0613 | 0615 |
|------|------|------|
| Ítems / Tipos | 5 cuant · 5 cual · 3 mix | Igual |
| Resumen del protocolo | Etiquetas 12–22 palabras | Igual |
| latest.txt | — | Apunta a 0615 |

## Ronda 2

(no necesaria)

## Alineación corpus (2026-11-04)

| Fuente | Conteo |
|--------|--------|
| `resultados-PIO-cribado-2.csv` (vía `cribado2:apply`) | **146** registros · **73** SI · **73** NO |
| Metadatos ítems | `n_incluidos_si` = **73** (= SI+PODRIA+relleno en CSV, cuota `min_rsl`) |
| Nota | El commit `8d8d31c` redujo el CSV a 52 filas por error; restaurado con apply |
