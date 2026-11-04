---
name: rsl-resultado-items
description: >-
  Tras cribado 2 aplicado, descompone cada RQ del picoc vigente en 1–5 ítems breves
  de extracción (debate defensor-rsl + critico-rsl, máx. 2 rondas). Tipo de respuesta:
  cuantitativo, cualitativo o mixto. Escribe docs/<slug>/resultados/items/<YYYY-MM-DD-HHMM>/.
  Cierra con prosa-rsl + resultado-items:stamp. Use rsl-resultado-items or rsl-desglose-items.
---

# rsl-resultado-items

Protocolo de **ítems de extracción** por RQ. Reglas: [`playbooks/extraccion-items-rsl.md`](../../playbooks/extraccion-items-rsl.md).

Invoke: `Usa rsl-resultado-items sobre docs/<slug>/` · `rewrite` → nueva carpeta timestamp.

## Tipo vs codificación

| Columna | Valores | Obligatorio |
|---------|---------|-------------|
| **Tipo** | `cuantitativo` · `cualitativo` · `mixto` | Sí |
| **Codificación** | `nominal` · `categórico` · `numérico` · `texto` (opcional `mixto`) | Recomendado (WARN si falta) |
| **Notas** | Valores esperados, subcampos | No |

**Ítem breve:** una faceta de la pregunta del componente (≈ ≤ 12 palabras en la etiqueta).

## Estructura de `items.md`

1. Metadatos, objetivo, campos bibliográficos comunes.
2. Por cada RQ: pregunta literal, dato a extraer del picoc, tabla de ítems.
3. **`## Resumen del protocolo`** (obligatorio, al final): por componente → **Pregunta** → **Ítems** en lista.

### Tabla por RQ

| Id | Ítem (qué registrar) | Tipo | Codificación | Notas / valores esperados |
|----|----------------------|------|--------------|---------------------------|
| RQ1-I1 | Perfiles declarados | cualitativo | nominal | TEA, TDAH, DI… |

### Resumen (ejemplo)

```markdown
## Resumen del protocolo

### P — Población (RQ1)

**Pregunta:** ¿Qué perfiles…?

**Ítems:**
- RQ1-I1 — Perfiles declarados (cualitativo)
- RQ1-I2 — Estratificación por perfil (cualitativo)
```

(Repetir por RQ2, RQ3…)

## Procedure

1. `pnpm -s resultado-items:prepare docs/<slug>`
2. Contexto: picoc, `paper-polish.md` (RQ1 ética si aplica), grafo del tema.
3. Ronda 1 **defensor-rsl** / **critico-rsl** (`modo: extraccion-items`) → decisiones (máx. 2 rondas).
4. `items.md` con tablas + **Resumen del protocolo**.
5. Prosa: skill **humanize-academic-writing** → **`redaccion-rsl`** → `pnpm -s redaccion:lint` → `resultado-items:lint` → `resultado-items:stamp` ([`prosa-rsl.md`](../../playbooks/prosa-rsl.md)).

## Cierre

- Éxito: `OK: resultados/items/<carpeta>/ (marco <MARCO>), resultado-items:status PASS. Próximo paso: skill formulario Excel (pendiente).`

## Forbidden

- Tipos distintos de cuantitativo/cualitativo/mixto en columna **Tipo**.
- Stamp sin `## Resumen del protocolo` o sin listar todos los ids.
- Más de 5 ítems por RQ sin acuerdo del usuario.
- Editar `picoc/`, informe, CSV, `config.yml`.
