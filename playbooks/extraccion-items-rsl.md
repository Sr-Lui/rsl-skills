# Ítems de extracción RSL (desglose por RQ)

Fuente de verdad para **`rsl-resultado-items`**. Prosa: [`playbooks/prosa-rsl.md`](prosa-rsl.md) (**humanize-academic-writing** obligatorio, luego **`redaccion-rsl`** + `pnpm -s redaccion:lint`; R1–R9 en [`redaccion-academica.md`](redaccion-academica.md)).

Normativa: Kitchenham y Charters (2007), § 6.4, pp. 29–34; PRISMA 2020 ítems 9–10 ([`estandares-rsl.md`](estandares-rsl.md) → `extraccion-datos`).

## Qué es un ítem

Un **ítem** es un campo del formulario de extracción que responde a una parte concreta de una **pregunta de revisión (RQ)** del picoc vigente. Debe ser:

- **Observable** en el texto completo del estudio (título, métodos, resultados o discusión).
- **Codificable** en una celda (texto breve, categoría, número o «no reportado»).
- **Unívoco**: una decisión de registro por ítem; no mezclar dos dimensiones en la misma fila.

La columna «Dato a extraer» del picoc es la semilla; el desglose **no** modifica el picoc.

## Límites

| Regla | Detalle |
|-------|---------|
| Por RQ | **Mínimo 1**, **máximo 5** ítems |
| Por tema | Una RQ del picoc → una sección en `items.md`; ids `RQn-Ik` consecutivos |
| Bibliografía | Campos comunes (id, título, autores, año, venue, DOI) **no** cuentan en el límite de 5 |
| Duplicados | El mismo dato no aparece en dos RQ salvo justificación explícita en `items-debate.md` |

## Tipos de dato (columna del formulario)

Valores permitidos en la tabla:

- **categórico** — clases finitas (p. ej. sí/no, familia de técnica).
- **nominal** — etiquetas sin orden (p. ej. condición declarada).
- **numérico** — conteos, años, puntuaciones.
- **texto** — cita o síntesis breve literal.
- **mixto** — parte cualitativa y parte cuantitativa en el mismo ítem (usar poco).

La skill Excel futura usará el tipo para guiar la respuesta por artículo; aquí solo se **define** el campo.

## Relevancia

Priorizar lo que permite:

1. Responder la RQ en la sección **Resultados** del paper.
2. Agrupar y tabular (Kitchenham § 6.5).
3. Contrastar con revisiones previas en **Discusión**.

Descartar ítems «curiosos» que no enlazan con el objetivo de la RSL (pregunta general § 1.2).

## Debate (defensor / crítico)

- **Defensor:** propone el conjunto mínimo suficiente; defiende ítems que reflejen CI/CE relevantes para la síntesis (p. ej. consentimiento, marco normativo).
- **Crítico:** ataca redundancia, granularidad excesiva, ítems no observables, huecos frente al «Dato a extraer», duplicación entre RQs.
- **Máximo 2 rondas.** Sin consenso → la skill termina en **ERROR**; no se marca `latest.txt`.

## Piloto

Kitchenham recomienda pilotar el formulario en una muestra de estudios incluidos; la ejecución del piloto queda fuera de `rsl-resultado-items` (skill de extracción / Excel).
