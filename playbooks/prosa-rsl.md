# Prosa RSL — cadena obligatoria (humanizar → redacción)

Toda skill `rsl-*` que **entregue o pule prosa** en markdown (informe, paper, picoc, ítems de extracción, etc.) debe cerrar la forma con esta secuencia, en este orden:

## 1. Humanizar (obligatorio)

Leer y aplicar [`.agents/skills/humanize-academic-writing/SKILL.md`](../.agents/skills/humanize-academic-writing/SKILL.md).

- **Objetivo:** voz académica natural, sin cadencia mecánica ni transiciones tipo plantilla (*Moreover*, *Furthermore*; en español: *Además*, *Asimismo* encadenados).
- **Idioma:** el del tema (`formato.idioma` en `config.yml`, por defecto `es`). Las estrategias del skill (ritmo de oraciones, transiciones, concreción, menos andamiaje abstracto) se aplican **en ese idioma**, aunque el skill esté redactado en inglés.
- **Alcance:** párrafos de prosa del entregable; no tablas de datos ni ecuaciones de búsqueda.
- **Integridad:** solo mejorar redacción de ideas ya decididas (declaración ética del skill); no inventar contenido ni evadir detectores a costa del sentido.

Si el texto ya pasó humanize en la misma corrida sobre los mismos párrafos, no repetir el paso.

## 2. Redacción RSL (obligatorio)

Subagente **`redaccion-rsl`** sobre el mismo archivo, con [`playbooks/redaccion-academica.md`](redaccion-academica.md) (R1–R9, Hilo, Calidad de prosa).

- Humanize **no sustituye** a `redaccion-rsl`: corrige naturalidad; `redaccion-rsl` fija siglas, hilo, densidad, marcas editoriales y estándar UTP/FIS.

## 3. Lint (obligatorio)

`pnpm -s redaccion:lint <archivo.md>` → **0 FAIL**; cada WARN corregido o justificado.

## Precedencia

Si humanize y R1–R9 chocan, **gana redaccion-rsl** (y el lint).

## Skills y agentes

| Quién | Cuándo humanize |
|-------|-----------------|
| Skills `rsl-make-report`, `rsl-polish-report`, `rsl-picoc`, `rsl-make-paper`, `rsl-polish-paper`, `rsl-desglose-items`, `rsl-turnitin-arreglar` | Antes de invocar `redaccion-rsl` en el cierre de forma |
| Agente **`redaccion-rsl`** | Asume que el operador ya humanizó; si recibe borrador crudo, aplica mentalmente las estrategias del skill humanize y luego R1–R9 |
| **`critico-rsl`**, **`citas-rsl`**, **`turnitin-rsl`** | No humanizan; solo mencionan forma si oculta un error de contenido |

Las skills citan este playbook en una línea; no repiten la cadena entera.
