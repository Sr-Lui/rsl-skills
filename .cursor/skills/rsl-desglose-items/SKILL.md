---
name: rsl-desglose-items
description: >-
  Tras cribado 2 aplicado, descompone cada RQ del picoc vigente en 1–5 ítems de
  extracción observables (debate defensor-rsl + critico-rsl, máx. 2 rondas).
  Escribe docs/<slug>/resultados/items/<YYYY-MM-DD-HHMM>/ (items.md, items-debate.md,
  items.json). Cierra con playbooks/prosa-rsl.md (humanize-academic-writing → redaccion-rsl → lint) y extraccion-items:stamp.
  Use when the user says rsl-desglose-items.
---

# rsl-desglose-items

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
      items.json
      manifest.json     ← stamp
```

Invoke: `Usa rsl-desglose-items sobre docs/<slug>/` · add `rewrite` para nueva carpeta timestamp aunque el desglose esté PASS.

## Precondiciones

1. `pnpm -s picoc:latest docs/<slug>` → **OK**
2. Existe `resultados-<MARCO>-cribado-2.csv` en la carpeta del picoc vigente
3. `pnpm -s extraccion-items:prepare docs/<slug>` → JSON con RQs y `dest_folder`

Sin CSV cribado-2 → **ERROR** (rsl-cribado-2-aplicar).

Si `extraccion-items:status` PASS y no hay `rewrite` → informar y parar (no nueva versión).

## Prosa

Cadena obligatoria: [`playbooks/prosa-rsl.md`](../../playbooks/prosa-rsl.md).

1. Tras consenso defensor/critico: aplicar skill **humanize-academic-writing** (`.agents/skills/humanize-academic-writing/SKILL.md`) sobre la prosa de `items.md` (metadatos narrativos, objetivo, etiquetas y notas — no las celdas técnicas de ids).
2. Subagente **`redaccion-rsl`** sobre el mismo archivo.
3. `pnpm -s redaccion:lint docs/<slug>/resultados/items/<carpeta>/items.md` → **0 FAIL**
4. `pnpm -s extraccion-items:lint docs/<slug>` → OK
5. `pnpm -s extraccion-items:stamp docs/<slug> <carpeta>`

## Procedure

1. **Prepare** — `pnpm -s extraccion-items:prepare docs/<slug>`; crear carpeta `resultados/items/<timestamp>/`.
2. **Contexto** — RQs del JSON; grafo del tema (`pnpm graphify:theme:query <slug> "…"`) solo para afinar ítems observables; no PDFs enteros.
3. **Ronda 1 — defensor-rsl** (`modo: extraccion-items`, **propone**): borrador `items.md` + tabla en `items-debate.md` bajo `## Ronda 1 — Defensor` (1–5 ítems por RQ; ids `RQn-Ik`; tipos del playbook).
4. **Ronda 1 — critico-rsl** (`modo: extraccion-items`, **refuta**): solo desacuerdos en `## Ronda 1 — Crítico`; responde una línea (`ronda-1: n desacuerdos`).
5. **Consolidar** — tabla `## Ronda 1 — Decisiones` (aceptar | modificar | eliminar | pendiente).
6. **Ronda 2** (solo si queda **pendiente**): repetir defensor → crítico → `## Ronda 2 — Decisiones`.
7. Si tras ronda 2 queda **pendiente** → cierre **ERROR** (resumen, criterios, preguntas al usuario); **no** stamp.
8. Escribir `items.md` final acordado + `items.json` (esquema del playbook / prepare).
9. **Prosa:** humanize-academic-writing → **redaccion-rsl** → **redaccion:lint** → **extraccion-items:lint** → **stamp** (véase `playbooks/prosa-rsl.md`).

## Plantilla mínima `items.md`

```markdown
# Ítems de extracción

**Tema:** … · **Marco:** PIO · **Picoc:** `picoc/…/picoc.md` · **Incluidos (SI):** n · **Fecha:** …

## Objetivo de extracción

(un párrafo: qué se demostrará con los datos tabulados)

## Campos bibliográficos comunes

(id del corpus, título, autores, año, venue, DOI — no cuentan en el límite 1–5 por RQ)

## RQ1 (P) — …

**Pregunta (literal del picoc):** ¿…?

**Dato a extraer (picoc):** …

### Ítems de extracción

| Id | Ítem (qué registrar) | Tipo de dato | Notas / valores esperados |
|----|----------------------|--------------|---------------------------|
| RQ1-I1 | … | categórico | … |
```

(Repetir `## RQ2` …)

## Cierre

- Fallo (precondición, consenso, lint): `ERROR: <mensaje>. <arreglo>.`
- Éxito: `OK: resultados/items/<carpeta>/ (marco <MARCO>), extraccion-items:status PASS. Próximo paso: skill de formulario Excel (pendiente).`

## Forbidden

- Más de 5 ítems por RQ sin acuerdo explícito del usuario en chat.
- Stamp sin consenso o con lint FAIL.
- Editar `picoc/`, `informe*`, CSV cribado, `config.yml`.
- Inventar RQs que no estén en el picoc vigente.
