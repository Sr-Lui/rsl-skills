# Informe: deficiencias del flujo de extracción al formulario (skill **rsl-resultado-formulario-apply**)

**Tema auditado:** `docs/ia-inclusion-cognitiva-software`  
**Carpeta de formulario:** `resultados/formulario/2026-11-06-0358` (estado analizado antes de endurecer el tooling; ver §10)  
**Objetivo del documento:** motivar mejoras en la skill y en los linters; las reglas nuevas viven en [`scripts/formulario_lint_prosa.py`](scripts/formulario_lint_prosa.py), [`scripts/resultado-formulario.py`](scripts/resultado-formulario.py) y los playbooks enlazados desde la skill.

---

## 1. Resumen ejecutivo (histórico)

- Antes del endurecimiento, **`formulario:lint-traza`** solo validaba **conteo y decisión**; **`lint_evidence_row`** vivía dentro de `lint-prosa`, de modo que **no** se bloqueaba `loc: "fulltext"` ni `quote` copia del `value`.
- **`lint-prosa`** emitía **WARN** por repetición masiva del mismo texto entre estudios (plantilla); **no** eran FAIL → el **stamp** podía cerrar `extraccion_complete` con contenido frágil.
- Un análisis sobre `extraccion-traza.jsonl` mostró **`loc: "fulltext"`** en casi todos los slots y **`quote` ≈ `value`** tras parches manuales para pasar la longitud mínima.
- **`manifest.nature_needs_review`** (p. ej. 34 estudios en ese tema) **no** bloqueaba el stamp de extracción.

*(Los números de líneas y porcentajes de la carpeta 2026-11-06-0358 son diagnóstico histórico; una carpeta nueva debe volver a pasar los gates actuales.)*

---

## 2. Lección: registro vs matiz y «baja diversidad»

- **Pocos valores únicos** en un ítem **categórico** (pocas categorías posibles) **no** implican que los artículos sean homogéneos: es normal que muchos estudios compartan la misma etiqueta.
- Lo problemático es cuando **toda la celda** (registro + matiz) es **idéntica** entre estudios o cuando **un valor domina** casi todas las filas sin lectura del MD: eso suele ser **plantilla de redacción** o **evidencia sintética**, no convergencia empírica.
- La skill y [`formulario-prosa-rsl.md`](playbooks/formulario-prosa-rsl.md) ahora exigen separar **registro** (puede repetirse) de **matiz** (específico del estudio cuando hay `extracted`/`partial`).

---

## 3. WARN históricos de plantilla entre estudios

En el run antiguo, `lint_template_repeated_across_studies` alertaba (umbral ≈ 35% de N) para varios `item_id` (RQ1-I2, RQ1-I3, RQ2-I2, RQ2-I4, RQ3-I1, RQ3-I5, …). Con **`stamp`** en modo estricto, esos WARN pasan a **FAIL** por encima de umbrales (`--strict` en `lint-prosa` / `lint-traza`).

---

## 4. Dominancia de un solo valor (red flag)

Un mismo texto normalizado en **≥80%** de las celdas con contenido de un `item_id` (mínimo 5 filas) indica **un solo resultado pegado a todos los estudios** salvo excepción real. El linter ahora emite **E13** (`lint_value_dominance_across_studies`).

---

## 5. Calidad de `evidence[]` (endurecida)

Reglas actuales (salvo `decision: absent` o celda `—`):

| Regla | Comportamiento |
|--------|------------------|
| `loc` | No vacío; no `fulltext`; debe coincidir con ancla (`p.` / `l.` / `§` / `Sección`…) o estar en `manifest.evidence_loc_whitelist` |
| `src` | Archivo existente bajo el repo (ruta relativa resuelta desde la raíz del workspace) |
| `quote` | ≥40 caracteres; **no** idéntico al `value`; debe aparecer como **substring** (normalizado) del fichero `src` |
| RQ3-I1 | Si **Valor** numérico, alguna `quote` contiene el dígito |

---

## 6. Procedimiento y lectura por estudio

La skill documenta el orden: **MD del cribado-2** → **`pnpm -s cribado2:query docs/<slug> "…"`** (Graphify sobre el grafo del cribado-2) → PDF si hace falta. Eso cubre la hipótesis de que la homogeneización venía de **no cruzar** texto indexado con preguntas acotadas.

---

## 7. `nature_needs_review` y stamp

Si `manifest.nature_needs_review` **no está vacío**, **`formulario:stamp`** **falla** hasta resolver naturaleza (`nature-overrides` + `classify-nature --force`) o usar explícitamente **`pnpm -s formulario:stamp docs/<slug> <carpeta> --allow-nature-review`** (asumiendo el riesgo para la síntesis).

---

## 8. Comandos (cierre)

```bash
pnpm -s formulario:lint-traza docs/<slug> [carpeta]   # estructura + evidencia
pnpm -s formulario:lint-traza docs/<slug> [carpeta] --strict   # + plantilla estricta

pnpm -s formulario:lint-prosa docs/<slug> [carpeta]  # prosa, dominancia, duplicados entre ítems
pnpm -s formulario:lint-prosa docs/<slug> [carpeta] --strict   # convierte WARN restantes en FAIL

pnpm -s formulario:stamp docs/<slug> <carpeta>   # lint-traza --strict + lint-prosa --strict; gate naturaleza
pnpm -s formulario:stamp docs/<slug> <carpeta> --allow-nature-review
```

**`sintesis:prepare`** usa el mismo criterio estricto en el gate de formulario (estructura + evidencia + `lint-prosa` strict).

---

## 9. Conclusión

El caso `2026-11-06-0358` sirvió para ver **huecos del linter** y de la skill. El tooling actual **cierra** esos huecos: evidencia literal, `loc` anclado, dominancia y plantilla estricta en stamp, y bloqueo opcional de naturaleza en revisión.

---

## 10. Estado al 2026-11-06 (implementación)

- Código: [`scripts/formulario_lint_prosa.py`](scripts/formulario_lint_prosa.py), [`scripts/resultado-formulario.py`](scripts/resultado-formulario.py), gate alineado en [`scripts/resultado-sintesis.py`](scripts/resultado-sintesis.py).
- Documentación: [`.cursor/skills/rsl-resultado-formulario-apply/SKILL.md`](.cursor/skills/rsl-resultado-formulario-apply/SKILL.md), [`playbooks/formulario-apply-rsl.md`](playbooks/formulario-apply-rsl.md), [`playbooks/formulario-prosa-rsl.md`](playbooks/formulario-prosa-rsl.md).

Las carpetas de formulario existentes con traza antigua **dejarán de pasar** `stamp` hasta actualizar `apply-*.json` / `extraccion-traza.jsonl` según el nuevo contrato.
