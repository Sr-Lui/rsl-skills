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
| **cuantitativo** | Valor numérico del artículo **o** categoría/binario pensado para **% de estudios** (frecuencia en síntesis) |
| **cualitativo** | Texto, listas nominales ricas, matices «por qué»; marcos sin conteo principal |
| **mixto** | Plantilla con subcampos categóricos **y** numéricos en la misma celda |

No fuerces un reparto 50/50: el debate documenta por qué predomina un Tipo en una RQ.

No uses nominal, categórico, numérico ni texto en la columna **Tipo**.

## Naturaleza del estudio vs tipo del ítem

| Concepto | Dónde vive | Efecto en Excel |
|----------|------------|-----------------|
| **Tipo del ítem** (`response_type` en `items.json`) | Columna **Tipo** del desglose | **Filas** 17–33 en la hoja Cuantitativo y/o Cualitativo |
| **Naturaleza del estudio** (cuantitativo / cualitativo / mixto) | Solo `formulario-map.json` (`study_nature`, `placement`) — **no** fila en la plantilla | **Columna** del estudio en una o dos hojas (mixto = ambas) |

Un estudio **cuantitativo** puede tener ítems **cualitativos** en filas de la hoja Cuantitativo; no implica columna en la hoja Cualitativo. Clasificación: **`formulario:classify-nature`** (skill prepare).

## Codificación (columna **Codificación** — opcional)

Detalle interno para diseñar la hoja Excel (lint WARN si falta, no FAIL):

- **nominal**, **categórico**, **numérico**, **texto** (y **mixto** solo si la codificación también es híbrida).

Las **Notas** aclaran valores esperados o subcampos.

**Excel de extracción (`rsl-resultado-formulario-apply`):** los `hint` y plantillas de esta tabla sirven para **diseño y síntesis agregada** (`## Reglas de registro`); **no** se copian literales a las celdas del `.xlsx`. Allí va **prosa en español** según [`formulario-prosa-rsl.md`](formulario-prosa-rsl.md).

## Extracción → síntesis (RSL)

Cada ítem debe anticipar **cómo se agregarán los 73 estudios** en Resultados:

| En extracción (Tipo) | En síntesis RSL |
|----------------------|-----------------|
| **cuantitativo** | Frecuencia (% estudios por categoría) **o** estadísticos de valores reportados |
| **cualitativo** + codificación **texto** / nominal rico | **Narrativa** / temas (el «por qué») |
| **mixto** | Subcampos fijos: frecuencia por subcampo + narrativa en notas |

Reglas operativas (van en **`## Reglas de registro y agregación`** de `items.md`):

- **`NR`** = no reportado en el texto completo (no inferir solo del resumen).
- **Multivalor:** separar con **`;`** (perfiles, fases secundarias, roles múltiples).
- **Fases del ciclo de vida (RQ2):** **fase principal** (una categoría) + **otras fases** (lista o `—` si solo una).
- **No** fusionar en un solo ítem dos dimensiones que luego se cruzan en tablas (p. ej. cobertura cognitivo/sensorial **y** grado de automatización → dos ítems).

## Reglas de registro y agregación (obligatorio en `items.md`)

Sección **`## Reglas de registro y agregación`** después de campos bibliográficos: convenciones anteriores + tabla breve «ítem → agregación prevista» (frecuencia / narrativa / valor numérico).

## Ítems (final de `items.md`)

Después de todas las secciones `## RQn`, incluir **`## Ítems`**: vista operativa (la que lee el equipo y **`rsl-resultado-formulario`** vía `items.json`). Por componente: pregunta acortada y lista `- RQn-Ik — <redacción clara>` sin listas de ejemplo ni **Tipo** al final.

```markdown
## Ítems

### P — Población (RQ1)

**Pregunta:** ¿…?

**Ítems:**
- RQ1-I1 — …
```

## Debate (defensor / crítico)

- **Defensor:** conjunto mínimo suficiente; **Tipo** ternario; ítems breves.
- **Crítico:** refuta tipos mal asignados, etiquetas largas en **tabla**, Resumen demasiado corto (W7), ítems que mezclan dos dimensiones agregables, multifase silenciosa o huecos frente al «Dato a extraer»; pide justificación del balance de Tipos en el debate (sin cuota 50/50).
- Cierre del debate: sección **`## Mejoras respecto a <carpeta-anterior>`** si la corrida es `rewrite`.
- **Máximo 2 rondas.** Sin consenso → **ERROR**; no `stamp`.

## Piloto

Kitchenham recomienda pilotar el formulario en una muestra; la ejecución queda fuera de `rsl-resultado-items` (skill Excel futura).
