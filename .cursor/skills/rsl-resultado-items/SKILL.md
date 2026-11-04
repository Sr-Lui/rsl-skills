---
name: rsl-resultado-items
description: >-
  Tras cribado 2 aplicado, descompone cada RQ del picoc vigente en 1–5 ítems de
  extracción observables (debate defensor-rsl + critico-rsl, máx. 2 rondas).
  Escribe docs/<slug>/resultados/items/<YYYY-MM-DD-HHMM>/ (items.md, items-debate.md,
  items.json). Cierra con playbooks/prosa-rsl.md (humanize-academic-writing → redaccion-rsl → lint) y resultado-items:stamp.
  Use when the user says rsl-resultado-items or rsl-desglose-items.
---

# rsl-resultado-items

Protocolo de **ítems de extracción** por RQ (Kitchenham § 6.4; PRISMA 9–10). Reglas: [`playbooks/extraccion-items-rsl.md`](../../playbooks/extraccion-items-rsl.md). No modifica `picoc/`, informe ni CSV de cribado.

```text
docs/<slug>/
  picoc/<fecha>-<MARCO>/picoc.md                    (read)
  picoc/.../resultados-<MARCO>-cribado-2.csv         (read; gate)
  resultados/items/
    latest.txt
    <YYYY-MM-DD-HHMM>/
      items.md          ← salida principal
      items-debate.md
      items.json        ← emit-json en stamp
      manifest.json     ← stamp
```

Invoke: `Usa rsl-resultado-items sobre docs/<slug>/` · add `rewrite` para nueva carpeta timestamp aunque el desglose esté PASS.

## Precondiciones

1. `pnpm -s picoc:latest docs/<slug>` → **OK**
2. Existe `resultados-<MARCO>-cribado-2.csv` en la carpeta del picoc vigente
3. `pnpm -s resultado-items:prepare docs/<slug>` → JSON con RQs y `dest_folder` (+ `items-debate.md` plantilla)

Sin CSV cribado-2 → **ERROR** (rsl-cribado-2-aplicar).

Si `resultado-items:status` PASS y no hay `rewrite` → informar y parar (no nueva versión).

## Prosa

Cadena obligatoria: [`playbooks/prosa-rsl.md`](../../playbooks/prosa-rsl.md).

1. Tras consenso defensor/critico: skill **humanize-academic-writing** sobre la prosa de `items.md`.
2. Subagente **`redaccion-rsl`** sobre el mismo archivo.
3. `pnpm -s redaccion:lint docs/<slug>/resultados/items/<carpeta>/items.md` → **0 FAIL**
4. `pnpm -s resultado-items:lint docs/<slug>` → OK
5. `pnpm -s resultado-items:stamp docs/<slug> <carpeta>` (escribe `manifest.json`, `items.json`, `latest.txt`)

## Procedure

1. **Prepare** — `pnpm -s resultado-items:prepare docs/<slug>`; carpeta `resultados/items/<timestamp>/`.
2. **Contexto** — RQs del JSON; `paper-polish.md` (extracción RQ1 si aplica); grafo del tema (`pnpm graphify:theme:query <slug> "…"`); no PDFs enteros.
3. **Ronda 1 — defensor-rsl** (`modo: extraccion-items`, **propone**): borrador `items.md` + `## Ronda 1 — Defensor` en `items-debate.md`.
4. **Ronda 1 — critico-rsl** (**refuta**): `## Ronda 1 — Crítico`; una línea `ronda-1: n desacuerdos`.
5. **Consolidar** — `## Ronda 1 — Decisiones`.
6. **Ronda 2** solo si queda **pendiente**.
7. Si tras ronda 2 queda **pendiente** → **ERROR**; **no** stamp.
8. **`items.md` final** acordado.
9. **Prosa** → **resultado-items:lint** → **stamp**.

## Cierre

- Fallo: `ERROR: <mensaje>. <arreglo>.`
- Éxito: `OK: resultados/items/<carpeta>/ (marco <MARCO>), resultado-items:status PASS. Próximo paso: skill formulario Excel (pendiente).`

## Forbidden

- Más de 5 ítems por RQ sin acuerdo explícito del usuario.
- Stamp sin consenso o con lint FAIL.
- Editar `picoc/`, `informe*`, CSV cribado, `config.yml`.
- Inventar RQs que no estén en el picoc vigente.
