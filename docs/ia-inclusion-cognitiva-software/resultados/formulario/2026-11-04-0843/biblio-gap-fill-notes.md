# Biblio gap-fill — fila 13 (Tamaño de muestra)

> **Estado (2026-11-04):** aplicado en Excel con `pnpm -s formulario:biblio-enrich docs/ia-inclusion-cognitiva-software --force`. Filas **8–10, 12–13**: **0** celdas `—` (73 estudios). Este archivo queda como **traza del agente** [biblio gap-fill](d16c6e55-84a7-49ab-980f-1e62e6dcff06); la fuente operativa es `biblio-traza.jsonl`.

Formulario: `2026-11-04-0843` · hoja **Cuantitativo** · fila **13**.

Estado inicial (2026-11-04): **45** columnas con `—` en fila 13. Este archivo documenta las **15 primeras** (orden de columna en el Excel), con valores verificados en el corpus cribado-2 (`docs/md/R*.md`) y consultas `pnpm -s cribado2:query` (estas devolvieron sobre todo índice del grafo; los números provienen del texto del PDF indexado).

Formato alineado con celdas ya rellenas en el formulario (p. ej. `n = 15 participantes`, `10 díadas`, `Revisión bibliográfica (sin n empírico)`).

---

## Sugerencias verificadas (corpus_id → fila 13)

| corpus_id | DOI (fila 3) | Sugerencia para fila 13 | Evidencia |
|-----------|--------------|-------------------------|-----------|
| **R106** | 10.14201/scero.32147 | 164 personas con discapacidad cognitiva y 73 expertos en lectura fácil (cuestionarios en línea) | `R106-…md` PDF p.12–13: «164 personas con discapacidad cognitiva respondieron…»; «73 expertos en lectura fácil respondieron…» |
| **R123** | 10.1057/s41599-025-05079-1 | n = 75 participantes (niños de primer grado) | `R123-…md` PDF p.?: «This study recruited a total of 75 first-grade children» |
| **R173** | 10.3390/jcp5030045 | n = 25 padres (cuestionario); encuesta adicional n = 40 (percepción plataforma); n = 3 personal clínico (limitaciones herramientas) | `R173-…md` PDF p.4: «A total of 25 participants completed the questionnaire»; secc. 9 «Survey on End-User Perception»: «40 participants recruited»; p.4: «All three participants highlighted…» (clínicos) |
| **R183** | 10.1371/journal.pone.0342700 | Evaluación técnica sin participantes humanos (consultas estandarizadas sobre proveedores de servicios) | Abstract/métodos: evaluación de sistemas NLP/LLM/RAG con «standardized set of queries»; sin reclutamiento de personas |
| **R193** | 10.1145/3816046.3816307 | n = 1 participante (estudio de caso, análisis conversacional) | `R193-…md`: datos de Lucy, una usuaria en vivienda apoyada; vídeo compartido con consentimiento |
| **R208** | 10.1111/jppi.70061 | n = 5 participantes (adultos con discapacidad intelectual y del desarrollo) | `R208-…md` PDF p.1: «five adults with intellectual and developmental disabilities»; «Of the five participants…» |
| **R239** | 10.1145/3696593.3696625 | n = 14 participantes (estudiantes universitarios con dislexia; 7 fase 1 + 7 fase 2) | `R239-…md`: «A total of 14 native English-speaking undergraduate students with dyslexia were interviewed» |
| **R263** | 10.37933/nipes/7.4.2025.1324 | Sin participantes humanos | `R263-…md`: «No human participants or animals were involved in this study» |
| **R264** | 10.1609/aaai.v39i28.35229 | Propuesta de marco / trabajo futuro (sin evaluación empírica con participantes en este artículo) | `R264-…md`: objetivos y «Future Work: Developing a GenAI Prototype»; evaluación planeada, no reportada aquí |
| **R300** | 10.1177/14604582251345331 | n = 201 cuidadores (estudio principal); n = 12 profesionales de salud (usabilidad exploratoria aparte) | `R300-…md` PDF p.9: «201 completed the study, with 14 excluded»; «12 participants» (psiquiatras/psicólogos) |
| **R327** | 10.2196/85013 | n = 13 (grupo de experiencia vivida); 6 entrevistas think-aloud (3 jóvenes con TDAH + 3 apoyos) — co-producción PPIE | `R327-…md` PDF p.4: «working group of 13 people… 9 young people with ADHD and 4 supporters»; p.~732: «Six think-aloud interviews… 3 young people… and 3 supporters» |
| **R337** | 10.3390/info15120769 | Evaluación heurística de 4 sitios web (expertos/autores; sin usuarios finales con discapacidad cognitiva) | `R337-…md` PDF p.14–16: paso 4 evaluación por evaluador; «Four… websites were selected» |
| **R345** | 10.1016/j.ijhcs.2025.103696 | n = 14 participantes autistas (estudio empírico CARES); preestudio aparte n = 17 entrevistas | `R345-…md` PDF p.10: «recruit 14 participants» (empírico); p.5: «interviewed 17 people» (requisitos) |
| **R356** | 10.1145/3764687.3769943 | n = 12 estudiantes de posgrado (interpretación de intenciones sobre imágenes); datos de imágenes de talleres previos con personas con discapacidad intelectual (n del taller no declarado en este artículo) | `R356-…md` PDF p.4–5: «Twelve postgraduate students…»; p.3: «20 user-selected images» de talleres citados [11] |
| **R360** | 10.1145/3663547.3759705 | n = 7 estudiantes con TDAH (evaluación formativa); pre-diseño n = 5 estudiantes; 5 expertos (E1–E5) | `R360-…md` PDF p.2–3: «five university students (S1-S5)» pre-diseño; «students diagnosed with ADHD (S1–S7) and five experts» evaluación |

---

## Notas de cribado2:query

Consultas ejecutadas (2026-11-04):

```text
pnpm -s cribado2:query docs/ia-inclusion-cognitiva-software "Estudio RXXX: tamaño muestral participantes n="
```

para R106, R123, R173, R183, R193, R208, R239, R263, R264, R300, R327, R337, R345, R356, R360.

El grafo enlazó nodos de metadatos/chunks pero **no extrajo cifras muestrales** en la respuesta por defecto (~2000 tokens); las cifras de la tabla provienen de lectura directa de **Page chunks** en `RSL/picoc/2026-10-03-3-cribado-2-PIO/docs/md/`. Esas pistas se integraron en `scripts/formulario_biblio_enrich.py` (`MANUAL_ROW13` y heurísticas MD) al cerrar el enrich.
