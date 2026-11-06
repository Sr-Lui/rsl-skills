---
name: rsl-resultado-sintesis
description: >-
  Genera la síntesis de resultados por ítem (sección Resultados de la RSL) a partir del formulario
  vigente (resultados/formulario/latest.txt) y los ítems vigentes. Agrupa ítems solos o en bloques,
  codifica categorías, calcula X% (n=Y) y redacta en tono objetivo, sin citar estudios, con tablas y
  figuras en formato Tabla N / Figura N / Nota. No dibuja: deja «Detalle gráfica» y spec JSON para la
  skill de gráficas en Python. Cada bloque pasa por defensor-rsl (propone), critico-rsl (debate) y
  orquestador-sintesis-rsl: dos rondas y una tercera final solo si no hubo acuerdo. Escribe
  docs/<slug>/resultados/sintesis/<fecha>/sintesis-resultados.md. Use rsl-resultado-sintesis,
  generar resultados por ítem o síntesis de resultados.
---

# rsl-resultado-sintesis

Playbook (reglas, formatos y **ejemplos que mandan**): [`playbooks/sintesis-resultados-rsl.md`](../../playbooks/sintesis-resultados-rsl.md) · Prosa: [`playbooks/prosa-rsl.md`](../../playbooks/prosa-rsl.md)

Invoke: `Usa rsl-resultado-sintesis sobre docs/<slug>/`

## Reglas de oro

- **Tono objetivo:** Resultados solo reporta lo que reporta la literatura, con porcentajes y n. No valora, no recomienda, no interpreta; eso va en Discusión.
- **Por ítem y resultado, nunca por autor.** **No se citan estudios individuales** en el texto: ni [n], ni autor y año, ni Rnnn.
- **Formato de los ejemplos:**
  - apertura con el total;
  - `el X% (n=Y)` de mayor a menor;
  - verbos neutros;
  - subtítulos `3.N.`;
  - `**Tabla N**` / `**Figura N**` + título en cursiva + `*Nota.*`.
- **Síntesis:**
  - cuantitativa y cualitativa por separado, después integradas;
  - homogeneidad o heterogeneidad señalada;
  - tipo de síntesis aditiva, refutacional o argumental;
  - sin metaanálisis.
- **Gráficas:** esta skill no las dibuja. Cada figura lleva debajo `#### Detalle gráfica (Figura N)` (tipo y por qué, qué muestra, datos exactos, ejes, etiquetas, leyenda, nota, estilo) y su `graficos/<bloque>.spec.json`.

## Precondiciones

- `resultados/formulario/latest.txt` apunta a una carpeta con **`manifest.json` → `extraccion_complete: true`** (solo lo fija **`pnpm -s formulario:stamp`** tras apply).
- Mismo gate que **`pnpm -s formulario:lint-traza`** y **`pnpm -s formulario:lint-prosa`** (estructura de traza, prosa, evidencia, sin duplicar texto entre ítems distintos por estudio).
- `resultados/items/latest.txt` → `items.json`.

## Procedure

0. **Gate formulario.** Si `sintesis:prepare` falla, el tema tiene `resultados/formulario/<carpeta>/formulario-bloqueante.md` con la lista de FAIL y un prompt para **rsl-resultado-formulario-apply**. **No** continuar síntesis ni recodificar extracción aquí.

1. **`pnpm -s sintesis:prepare docs/<slug>`** crea la carpeta `resultados/sintesis/<fecha>/` con:
   - `matriz.json`: estudio × ítem leído del Excel vía `placement`; un estudio mixto cuenta una vez; base por ítem;
   - `bloques.json` con los B00 de caracterización;
   - `manifest.json`.
2. **`pnpm -s sintesis:general docs/<slug>`** calcula las tablas B00: año, enfoque, tipo de documento, país y continente, y muestra.
3. **`pnpm -s sintesis:codify-auto docs/<slug> all`** propone categorías desde el registro de cada celda.
4. **Plan de bloques** (`debate/plan-bloques/`):
   - **defensor-rsl** en modo `sintesis-bloques` propone los bloques RQ (ítems solos o agrupados, p. ej. perfil × familia de IA);
   - **critico-rsl** en modo `sintesis-bloques` debate;
   - **orquestador-sintesis-rsl** cierra con `veredicto.json`.
5. **Por cada bloque, en orden.** No se pasa al siguiente sin `veredicto.json`:
   1. `pnpm -s sintesis:aggregate docs/<slug> <bloque>`, salvo los B00, que ya calculó `general`.
   2. `pnpm -s sintesis:borrador docs/<slug> <bloque>`: tabla de datos y spec de partida.
   3. **R1:**
      - el defensor (modo `sintesis-resultado`) escribe `r1-defensor.md` con codificación revisada (`codebook.md`), texto, tabla o figura y Detalle gráfica;
      - el crítico (modo `sintesis-resultado`) escribe `r1-critico.md`: «De acuerdo» / «En desacuerdo» + objeciones.
   4. **R2:** `r2-defensor.md` y `r2-critico.md`. **Las dos rondas son obligatorias.**
   5. **Orquestador:**
      - con acuerdo en R2 → `veredicto.json` con `rondas: 2`;
      - sin acuerdo → **R3 final** (`r3-*`), para consensuar. Si aun así no hay acuerdo, cierra el orquestador con el desacuerdo residual por escrito (`rondas: 3`).
   6. Si la codificación cambió, se vuelve a correr `aggregate`. Las cifras salen solo de `tablas/<bloque>.json`.
   7. El texto aprobado pasa por la cadena de prosa: **humanize-academic-writing** → **redaccion-rsl** → `pnpm -s redaccion:lint` (0 FAIL), **sin tocar cifras**. Después se inserta en `sintesis-resultados.md` y, si lleva figura, se guarda `graficos/<bloque>.spec.json` con su número de figura.
6. **`pnpm -s sintesis:debate-index docs/<slug>`** genera `sintesis-debate.md`, con `## Bloques con tercera ronda` al inicio.
7. **`pnpm -s sintesis:lint docs/<slug>`** revisa:
   - cifras contra las tablas;
   - ausencia de citas y de enfoque por autor;
   - formato de tablas y figuras;
   - Detalle gráfica y spec;
   - tono objetivo;
   - dos rondas por bloque y registro de la R3.

   Debe dar **0 FAIL**.
8. **`pnpm -s sintesis:stamp docs/<slug> <carpeta>`** actualiza `latest.txt` y `manifest.json` (`rondas_3`).

`pnpm -s sintesis:status docs/<slug>` muestra el avance por bloque.

## Salida (carpeta `resultados/sintesis/<fecha>/`)

| Archivo | Contenido |
|---|---|
| `sintesis-resultados.md` | Sección Resultados: 3.1 caracterización y bloques por RQ |
| `sintesis-debate.md` | Índice del debate; `## Bloques con tercera ronda` |
| `debate/<bloque>/` | `borrador.md`, `r1-*`, `r2-*`, `r3-*` si hubo, `veredicto.json` |
| `bloques.json`, `codebook.md`, `codificacion/*.jsonl` | Plan de bloques y codificación |
| `tablas/<bloque>.json` y `.md` | Frecuencias, cruces y traza interna de estudios por categoría |
| `graficos/<bloque>.spec.json` | Especificación para la skill de gráficas en Python |
| `matriz.json`, `manifest.json` | Matriz estudio × ítem; fuentes, sha y `rondas_3` |

## Cierre

```text
OK: sintesis-resultados.md (B bloques, T tablas, F figuras con Detalle gráfica).
Tercera ronda: ninguna | Bloque X: requirió una tercera ronda final porque no hubo acuerdo en la segunda; cierre …
Próximo paso: skill de gráficas (Python) sobre graficos/*.spec.json.
```

En el mensaje final al usuario, repite la línea «Tercera ronda» tal como la imprime `sintesis:stamp`.

## Forbidden

- Corregir celdas del Excel, la traza `extraccion-traza.jsonl` o la codificación de ítems cuando el fallo es de **apply**; usar `formulario-bloqueante.md` y volver a **rsl-resultado-formulario-apply** + `formulario:stamp`.
- Citar estudios individuales en `sintesis-resultados.md` ([n], autor y año, Rnnn) o resumir artículo por artículo.
- Valorar, recomendar o interpretar en Resultados.
- Cifras que no salgan de `tablas/<bloque>.json`; cambiar cifras en humanize o redacción.
- Cerrar un bloque con una sola ronda, avanzar sin veredicto o abrir una cuarta ronda.
- Escribir el aviso de tercera ronda en la prosa de resultados.
- Dibujar gráficas o instalar librerías de gráficos en esta skill.
- Editar `Formulario.xlsx`, `items.json`, picoc o `config.yml`.
