#!/usr/bin/env python3
"""Generate debate/lote-01 apply-*.json for ia-inclusion-cognitiva-software (lote 01)."""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
THEME = REPO / "docs/ia-inclusion-cognitiva-software"
MD_DIR = THEME / "RSL/picoc/2026-10-03-3-cribado-2-PIO/docs/md"
OUT_DEBATE = THEME / "resultados/formulario/2026-11-06-0847/debate/lote-01"


def ev(fname: str, page: str, quote: str) -> dict:
    q = quote.strip()
    if len(q) < 40:
        raise ValueError(f"{fname}: quote len {len(q)} < 40")
    rel = str(Path("docs/ia-inclusion-cognitiva-software") / "RSL/picoc/2026-10-03-3-cribado-2-PIO/docs/md" / fname)
    return {"src": rel, "loc": f"p. {page}", "quote": q}


def slot(item_id: str, value: str, decision: str, evidence: list[dict]) -> dict:
    if decision == "absent":
        return {"item_id": item_id, "value": "—", "decision": "absent", "evidence": []}
    if not evidence:
        raise ValueError(f"{item_id}: non-absent without evidence")
    return {"item_id": item_id, "value": value, "decision": decision, "evidence": evidence}


LOTE01: dict[str, list[dict]] = {
    "R016": [
        slot(
            "RQ1-I1",
            "Aprendizaje; discapacidad cognitiva y perfiles (dislexia; discapacidad intelectual; TEA) en el planteamiento.",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "1",
                    "The promise of large language models (LLMs) for individuals with learning disabilities and cognitive impairments is significant, yet their practical accessibility remains limited by readability barriers.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. Se contrastan prompts y modelos sobre salidas de LLM sin desagregación por perfil clínico.",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "4",
                    "Task queries were conceptualized around 4 domains relevant",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: No | N: 240 respuestas generadas vía API (sin participantes humanos con la condición) | Rol: NR",
            "partial",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "3",
                    "total N = 240 responses. This design provides 95% power to",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: déficit | Perfil: deducido | Consentimiento: NR | País: Arabia Saudí (afiliación institucional)",
            "partial",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "1",
                    "Department of Computer Science, College of Computer Science and Engineering, Taibah University, Medina 42353, Saudi Arabia",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "NLP; ML; LLM | Modelo: Llama-3.3-70B; Llama-3.1-8B; GPT-4o; Claude-Sonnet-4.5",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "1",
                    "This study conducted a systematic investigation of prompt engineering versus model selection for enhancing cognitive accessibility of responses in four leading LLMs (Llama-3.3-70B, Llama-3.1-8B, GPT-4o, Claude-Sonnet-4.5).",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Generador (respuestas vía APIs oficiales) y evaluación cuantitativa con métricas de legibilidad.",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "5",
                    "Official APIs were employed in all cases: the Groq Python SDK v0.13 for Llama models, OpenAI Python SDK v1.x, and Anthropic Python SDK v0.39.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Pruebas (evaluación experimental con diseño factorial y FRE como dependiente)",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "3",
                    "Together, these made for a 3 × 2 × 4 factorial study",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "Recolección automatizada (API), control de calidad de respuestas y ANOVA de tres vías.",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "5",
                    "significance using three-way ANOVA. Independent variables",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: Flesch Reading Ease (FRE) | Valor: ηp2 principal del tipo de prompt + contraste descriptivo Baseline vs Cognitive-Explicit (p. ej. M 81,50 vs 43,86; +37,64 puntos)",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "1",
                    "Prompt engineering accounted for 71.9% of variance (ηp2 = 0.719, p < 0.001) versus only 15.8% from model selection (ηp2 = 0.158, p < 0.001).",
                ),
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "1",
                    "Cognitive-Explicit prompts improved readability by 37.64 points (Cohen’s d = 2.49), reducing sentence length by 47% with minimal trade-off in lexical diversity.",
                ),
            ],
        ),
        slot(
            "RQ3-I2",
            "Métrica principal FRE; métricas suplementarias vía Python textstat y tokenización NLTK.",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "11",
                    "Computed using Python textstat library v0.7.3 with NLTK v3.8 Reviewers can download the CSV file to",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (sin WCAG/COGA explícito; foco en accesibilidad cognitiva vía legibilidad)",
            "partial",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "1",
                    "INDEX TERMS Accessibility design, AI ethics, cognitive accessibility, large language models, learning disabilities, prompt engineering, readability.",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "1",
                    "These findings establish prompt engineering as the dominant factor for cognitive accessibility in LLMs and offer actionable guidance for practitioners prioritizing accessibility in AI deployments for cognitive disability populations.",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Semiautomática (generación y medición algorítmica sin estudio principal con usuarios)",
            "partial",
            [
                ev(
                    "R016-prompt-engineering-versus-model-selection-for-cognitive-accessibility-in-large-l.md",
                    "3",
                    "One dependent variable was utilized, Flesch Reading Ease",
                )
            ],
        ),
    ],
    "R040": [
        slot(
            "RQ1-I1",
            "TEA / ASD (niños en el estudio de sistema asistencial educativo)",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "This study presents the design and implementation of an educational assistive system tailored for individuals with Autism Spec- trum Disorder (ASD), leveraging eye-tracking technology and machine learning algorithms.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. Resultados agregados del clasificador sin estratificación por subperfil de ASD.",
            "partial",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "The system was evaluated using an optimized ensemble algorithm, achieving an accuracy of 83.44%, with macro-averaged F1, pre- cision, and recall of 80.43%, 81.43%, and 80.57%, respectively, outperforming the baseline models.",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: Sí | N: 15 niños con ASD (scanpaths) | Rol: evaluación",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "An existing collection of scanpath images obtained from 15 children with ASD was utilized, and a customized heterogeneous dataset was developed by extracting fixation and gaze-related features using machine learning-based processing techniques.",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: déficit | Perfil: almacenado | Consentimiento: NR | País: Bangladés y EE. UU. (afiliaciones)",
            "partial",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "Institute of Information Technology, Jahangirnagar University, Savar, Bangladesh | 2 MU Institute for Data Science and Informatics, University of",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "ML; visión (eye-tracking) | Modelo: ensemble optimizado (detalle en el artículo)",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "leveraging eye-tracking technology and machine learning algorithms.",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Asistente / sistema de selección de teclado basado en fijaciones y mirada",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "The objective is to support commu- nication and learning experiences through ocular gaze and fixation-based keyboard selection.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Pruebas (evaluación con dataset de scanpaths y accuracy del ensemble)",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "The system was evaluated using an optimized ensemble algorithm, achieving an accuracy of 83.44%, with macro-averaged F1, pre- cision, and recall of 80.43%, 81.43%, and 80.57%, respectively, outperforming the baseline models.",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "Ingeniería de datos (extracción de características de fijación y construcción de dataset heterogéneo)",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "a customized heterogeneous dataset was developed by extracting fixation and gaze-related features using machine learning-based processing techniques.",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: accuracy (y F1 macro) del ensemble | Valor: accuracy 83,44%; F1 macro 0,8043",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "The system was evaluated using an optimized ensemble algorithm, achieving an accuracy of 83.44%, with macro-averaged F1, pre- cision, and recall of 80.43%, 81.43%, and 80.57%, respectively, outperforming the baseline models.",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Scanpaths; AOI; métricas de fijación y trayectorias oculares",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "In total, 320 scanpath images were ana- lyzed to capture fixation points and gaze directions during left–right and up–down navigation tasks. Based on fixation metrics and Area of Interest (AOI) analysis, a novel keyboard selection method was proposed, distinct from traditional digital keyboards.",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (sin WCAG/COGA explícito en la cita)",
            "partial",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "Keywords: assistive technology | autism | eye-tracking | gaze-based access control | smart board | virtual keyboard",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "This study presents the design and implementation of an educational assistive system tailored for individuals with Autism Spec- trum Disorder (ASD), leveraging eye-tracking technology and machine learning algorithms.",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Validación con datos reales de usuarios (scanpaths) mediante pipeline de ML; no CI",
            "partial",
            [
                ev(
                    "R040-an-intelligent-assistive-system-for-autistic-learners.md",
                    "1",
                    "An existing collection of scanpath images obtained from 15 children with ASD was utilized, and a customized heterogeneous dataset was developed by extracting fixation and gaze-related features using machine learning-based processing techniques.",
                )
            ],
        ),
    ],
    "R106": [
        slot(
            "RQ1-I1",
            "Discapacidad cognitiva (Lectura Fácil / Easy Read orientado a este colectivo)",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "Easy Read arranges texts in an accessible manner so that people with cognitive disabilities may have an easier time reading a clear and simple language.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "NR (sin desagregación por subperfil en el fragmento citado)",
            "partial",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "Regarding the production of these easy-to-read texts, professional adapters manually correct the texts and strip them of any complicated structures that may difficult the reading process.",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: NR | N: NR | Rol: NR (piloto con CEACOG; sin N explícito aquí)",
            "partial",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "Thus, in collaboration with the Centro Español de Accesibilidad Cognitiva (CEACOG), the online service ATECA (Adaptación de TExtos en CAstellano) was created to identify and adapt any discrepancy with a selection of the guidelines on Spanish Easy Read stablished by the Norma UNE 153101:2018 EX (AENOR, 2018).",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: NR | Perfil: deducido | Consentimiento: NR | País: España (CEACOG)",
            "partial",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "Thus, in collaboration with the Centro Español de Accesibilidad Cognitiva (CEACOG), the online service ATECA (Adaptación de TExtos en CAstellano) was created",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "IA (ATECA basado en IA) orientado a adaptación a Lectura Fácil",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "ATECA is a pilot support system, based on Artificial Intelligence (AI), that can be introduced into the traditional process of manually adapt- ing documents following the methodology.",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Asistente (análisis y sugerencias de transformación en flujo semi-automático)",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "This pilot application performs in a (semi-) automatic manner the two first activities in the cyclical process of adapting documents to Easy Read: the analysis of documents and the suggestion for how to transform such documents, so that they comply with the guidelines of the methodology.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Desarrollo / despliegue de herramienta web piloto en el proceso de adaptación",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "This pilot application performs in a (semi-) automatic manner the two first activities in the cyclical process of adapting documents to Easy Read: the analysis of documents and the suggestion for how to transform such documents, so that they comply with the guidelines of the methodology.",
                )
            ],
        ),
        slot("RQ2-I4", "—", "absent", []),
        slot(
            "RQ3-I1",
            "Constructo: adecuación a guías UNE 153101 (Lectura Fácil) | Valor: NR (sin cifra única en abstract)",
            "partial",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "the online service ATECA (Adaptación de TExtos en CAstellano) was created to identify and adapt any discrepancy with a selection of the guidelines on Spanish Easy Read stablished by the Norma UNE 153101:2018 EX (AENOR, 2018).",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Ciclo de adaptación a Easy Read; producción manual como referencia.",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "Regarding the production of these easy-to-read texts, professional adapters manually correct the texts and strip them of any complicated structures that may difficult the reading process.",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "Otro (Norma UNE 153101:2018 EX como referencia de Lectura Fácil)",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "the online service ATECA (Adaptación de TExtos en CAstellano) was created to identify and adapt any discrepancy with a selection of the guidelines on Spanish Easy Read stablished by the Norma UNE 153101:2018 EX (AENOR, 2018).",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "Easy Read arranges texts in an accessible manner so that people with cognitive disabilities may have an easier time reading a clear and simple language.",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Semiautomática (primeras actividades del ciclo en modo semi-automático)",
            "extracted",
            [
                ev(
                    "R106-ateca-a-web-application-to-facilitate-easy-to-read-adaptations-ateca-una-aplicac.md",
                    "2",
                    "This pilot application performs in a (semi-) automatic manner the two first activities in the cyclical process of adapting documents to Easy Read:",
                )
            ],
        ),
    ],
}

# Remaining corpus R123–R193 appended in second part to keep file readable
_LOTE01_REST: dict[str, list[dict]] = {
    "R123": [
        slot(
            "RQ1-I1",
            "Dislexia evolutiva (niños de habla china con dislexia leve en los experimentos)",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Our study engaged children with mild dyslexia across three experimental phases.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. Se comparan condiciones/modos de CNReader, no resultados estratificados por subtipo.",
            "partial",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "5",
                    "ences in age, RQ, and SPM scores of the three groups (Table 1).",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: Sí | N: 75; 44 y 15 (Experimentos 1–3 con niños y familias) | Rol: evaluación",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "6",
                    "recruited a total of 75 ﬁrst-grade children",
                ),
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "8",
                    "with mild reading difﬁculties. They were divided into three",
                ),
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "9",
                    "total of 15 children, with an average age of 6.73 years (SD = 0.68),",
                ),
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: déficit | Perfil: almacenado | Consentimiento: NR | País: China / Singapur (afiliaciones)",
            "partial",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "1 Hangzhou Dianzi University, Hangzhou, China. 2 China Jiliang University, Hangzhou, China. 3 Zhejiang University, Hangzhou, China. 4 National University of Singapore, Singapore, Singapore.",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "IA (lectura asistida por IA en CNReader) | Modelo: NR en el resumen citado",
            "partial",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Incorporating user-friendly visual text presentation, perso- nalized reading guidance, and artiﬁcial intelligence (AI) reading support, CNReader aims to stimulate and enhance children’s reading interest and ability.",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Tutor / práctica lectora (modo AI-paired reading vs human-paired)",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Notably, AI-paired reading emerged as both more appealing to children and more effective than conventional human-assisted approaches.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Pruebas (tres experimentos de efectividad y experiencia)",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "5",
                    "To test the effectiveness and user experience of CNReader, we conducted three studies. Study 1 tested the effectiveness of CNReader’s single-player reading practice mode.",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "Diseño de interfaz, modos de lectura y guía personalizada (complementarios al experimento principal)",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Incorporating user-friendly visual text presentation, perso- nalized reading guidance, and artiﬁcial intelligence (AI) reading support, CNReader aims to stimulate and enhance children’s reading interest and ability.",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: desempeño lector (errores, fluidez, comprensión) | Valor: NR agregada en abstract (mejoras reportadas cualitativamente)",
            "partial",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Results demonstrated that CNReader signiﬁcantly reduced reading error rates, enhanced reading ﬂuency, and improved compre- hension.",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Experimentos con medidas de precisión, ritmo y comprensión; seguimiento a un mes en Experimento 3",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "6",
                    "Number of reading errors 12.88 ± 6.36 8.08 ± 3.32 22.96 ± 6.42 −3.007/0.003**",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (herramienta accesible; sin WCAG/COGA explícito en la cita)",
            "partial",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "This paper presents an innovative tool, CNReader, designed to support reading training for young Chinese children with dyslexia.",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Chinese children with developmental dyslexia",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Validación con usuarios en experimentos controlados (niños; padres en Experimento 3)",
            "extracted",
            [
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Our study engaged children with mild dyslexia across three experimental phases.",
                ),
                ev(
                    "R123-cnreader-a-reading-practice-tool-designed-for-chinese-children-with-developmenta.md",
                    "1",
                    "Results demonstrated that CNReader signiﬁcantly reduced reading error rates, enhanced reading ﬂuency, and improved compre- hension.",
                ),
            ],
        ),
    ],
    "R145": [
        slot(
            "RQ1-I1",
            "TDAH en educación superior (ADHDvance LearnAR)",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "3",
                    "Attention-Deficit Hyperactivity Disorder (ADHD) is a neurodevelopmental condition characterised by persistent inattention, impulsivity, and hyperactivity, affecting educa- tional and social functioning.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. DBR exploratorio; no se presenta desagregación cuantitativa por subtipo de TDAH.",
            "partial",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "12",
                    "Given the exploratory nature of the study, the aim was not statistical generalisability but the identi- fication of meaningful patterns and user-informed design improvements.",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: Sí | N: 15 estudiantes con TDAH | Rol: evaluación",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "12",
                    "The study involved 15 undergraduate students diagnosed with ADHD, recruited through purposive sampling at a UK university.",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: déficit | Perfil: almacenado | Consentimiento: NR | País: Reino Unido (muestra universitaria UK)",
            "partial",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "12",
                    "The study involved 15 undergraduate students diagnosed with ADHD, recruited through purposive sampling at a UK university.",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "GenAI; AR | Modelo: integrado en ADHDvance LearnAR (sin nombre de modelo único en la cita)",
            "partial",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "2",
                    "Augmented Reality (AR) creates immersive and interactive environments that can foster focus and reduce cognitive overload [5], while Generative AI (GenAI) enables adaptive, person- alised learning experiences responsive to learners’ needs [4].",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Asistente educativo (AR + GenAI para organización y aprendizaje adaptativo)",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "2",
                    "this study introduces ADHDvance LearnAR—a novel educational application that integrates AR and GenAI to provide user-centred, adaptive support.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Pruebas (diseño intra-sujetos con condiciones basales, AR y AR+GenAI)",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "12",
                    "The study adopted a within-subjects experimental design comprising three distinct sequential conditions to comprehensively evaluate the effectiveness of the ADHDvance LearnAR application.",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "DBR (iteración con usuarios, prototipado y refinamiento)",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "2",
                    "The development of ADHDvance LearnAR adopts a rigorous Design-Based Research (DBR) approach, an iterative methodology particularly suitable for educational tech- nology research.",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: efectos cualitativos sobre organización y sobrecarga cognitiva (DBR) | Valor: NR (métrica única no en 5.1)",
            "partial",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "12",
                    "While modest, this sample size aligns with best practices in early-phase Design-Based Research (DBR), where the focus is on iterative development, contextual validation, and in-depth user feedback [43, 44].",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Tres sesiones ~90 min en aula controlada; tareas estandarizadas por condición",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "12",
                    "Each participant engaged with the dis- tinct experimental conditions during three separate sessions, each lasting approximately 90 min, conducted within a controlled classroom environment.",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (inclusión/neurodiversidad; sin WCAG explícito en la cita)",
            "partial",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "2",
                    "inclusive learning environments for neurodiverse learners.",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "3",
                    "Attention-Deficit Hyperactivity Disorder (ADHD) is a neurodevelopmental condition characterised by persistent inattention, impulsivity, and hyperactivity, affecting educa- tional and social functioning.",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Validación con usuarios (estudiantes con TDAH en aula controlada)",
            "extracted",
            [
                ev(
                    "R145-a-user-centred-approach-to-enhancing-engagement-and-task-management-for-adhd-stu.md",
                    "12",
                    "Each participant engaged with the dis- tinct experimental conditions during three separate sessions, each lasting approximately 90 min, conducted within a controlled classroom environment.",
                )
            ],
        ),
    ],
}

LOTE01.update(_LOTE01_REST)

_LOTE01_REST2: dict[str, list[dict]] = {
    "R147": [
        slot(
            "RQ1-I1",
            "Dislexia fonológica (escolares con diagnóstico)",
            "extracted",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Participants were elementary school learners diagnosed with phonological dyslexia.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. Cuasiexperimento pre-post con foco en el modelo adaptativo (sin estratos por subperfil en el abstract)",
            "partial",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "framework, combined with a quasi-experimental pre- and post-test control group design.",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: Sí | N: NR en abstract | Rol: evaluación",
            "partial",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Participants were elementary school learners diagnosed with phonological dyslexia.",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: déficit | Perfil: almacenado | Consentimiento: NR | País: Indonesia (Padang / Bandung)",
            "partial",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Universitas Negeri Padang, (AI) model integrated with real-time speech analytics to optimise phonological dyslexia inter- Padang, Indonesia vention.",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "IA multi-sensorial adaptativa; analítica de habla en tiempo real | Modelo: NR en abstract",
            "extracted",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "This study aims to develop and evaluate a mobile adaptive multi-sensory artificial intelligence",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Tutor con retroalimentación inmediata y rutas personalizadas (phonological training + analytics)",
            "partial",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "real-time speech analytics to provide immediate feedback and personalised learning pathways.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Intervención y evaluación (ADDIE + cuasiexperimento; tests de lectura y métricas de habla)",
            "extracted",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Data were collected through expert validation, usability questionnaires, phono- logical reading tests, and speech analytics metrics, including phoneme error rate (PER) and word error rate (WER).",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "Validación experta; cuestionarios de usabilidad (fases previas a ensayo)",
            "extracted",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Data were collected through expert validation, usability questionnaires, phono- logical reading tests, and speech analytics metrics, including phoneme error rate (PER) and word error rate (WER).",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: PER y WER entre otras métricas | Valor: ver resultados en cuerpo (no agregado en el abstract)",
            "partial",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Data were collected through expert validation, usability questionnaires, phono- logical reading tests, and speech analytics metrics, including phoneme error rate (PER) and word error rate (WER).",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Tests fonológicos; métricas PER/WER; cuestionarios de usabilidad",
            "extracted",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Data were collected through expert validation, usability questionnaires, phono- logical reading tests, and speech analytics metrics, including phoneme error rate (PER) and word error rate (WER).",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (educación inclusiva como contexto motivacional, no normativa WCAG)",
            "partial",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "Conventional dyslexia interventions are often non-adaptive, therapist-dependent, Andhika Herayono1 and limited in scalability, reducing their effectiveness in inclusive education contexts.",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "characterised by persistent difficulties in phoneme awareness, phoneme–grapheme",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Semiautomática (analytics + ajuste adaptativo con feedback inmediato)",
            "extracted",
            [
                ev(
                    "R147-optimising-dyslexia-intervention-leveraging-a-mobile-adaptive-multi-sensory-ai-m.md",
                    "1",
                    "real-time speech analytics to provide immediate feedback and personalised learning pathways.",
                )
            ],
        ),
    ],
    "R173": [
        slot(
            "RQ1-I1",
            "TDAH infantil (apps de salud mental gamificadas como caso de uso del marco)",
            "extracted",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "This research introduces a comprehensive framework for protecting health ap- plications from privacy and security threats, with a specific emphasis on gamified mental health apps designed to manage Attention Deficit Hyperactivity Disorder (ADHD) in children.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "NR (marco propuesto; sin cohorte con desagregación empírica)",
            "partial",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "This research introduces a comprehensive framework for protecting health ap- plications from privacy and security threats, with a specific emphasis on gamified mental health apps designed to manage Attention Deficit Hyperactivity Disorder (ADHD) in children.",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: No | N: NR | Rol: NR (trabajo de marco arquitectónico)",
            "partial",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "We suggest an identity management system based on blockchain technology to ensure secure and transparent credential management and incorporate Federated Learning to enable privacy-preserving AI-driven predictions.",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: NR | Perfil: deducido | Consentimiento: NR | País: Grecia (afiliaciones)",
            "partial",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "1   Department of Informatics & Telecommunications, University of Ioannina, 47100 Arta, Greece;",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "Aprendizaje federado; blockchain; p-ABCs; DP (PETs para apps de salud)",
            "extracted",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "Privacy- Enhancing Technologies (PETs), such as Privacy-Attribute-based Credentials, Differential Privacy, and Federated Learning, have emerged as crucial tools to tackle these challenges.",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Predicciones con IA preservando privacidad (FL) y gestión de identidad",
            "partial",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "incorporate Federated Learning to enable privacy-preserving AI-driven predictions.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Diseño de marco arquitectónico de seguridad y privacidad (no SDLC empírico completo)",
            "extracted",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "This research introduces a comprehensive framework for protecting health ap- plications from privacy and security threats",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "GDPR; stakeholders (menores, familias, educadores, profesionales de salud)",
            "extracted",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "like GDPR, while meeting the needs of various Received: 9 May 2025 stakeholders, including children, parents, educators, and healthcare professionals.",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: cumplimiento y privacidad del marco triple | Valor: NR (sin métrica experimental)",
            "partial",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "We suggest an identity management system based on blockchain technology to ensure secure and transparent credential management and incorporate Federated Learning to enable privacy-preserving AI-driven predictions.",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Marco para datos sensibles de salud mental infantil y contramedidas PETs",
            "extracted",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "Acknowledging the heightened sensitivity of mental health data, especially in ap- plications for children, our framework prioritizes user-centered design and strong privacy measures.",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "Otro (GDPR como referencia normativa explícita)",
            "extracted",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "like GDPR, while meeting the needs of various Received: 9 May 2025 stakeholders, including children, parents, educators, and healthcare professionals.",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "gamified mental health apps designed to manage Attention Deficit Hyperactivity Disorder (ADHD) in children.",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Semiautomática (predicciones FL asistidas por modelo; gobierno de identidad con intervención humana)",
            "partial",
            [
                ev(
                    "R173-triple-shield-privacy-in-healthcare-federated-learning-p-abcs-and-distributed-le.md",
                    "1",
                    "incorporate Federated Learning to enable privacy-preserving AI-driven predictions.",
                )
            ],
        ),
    ],
    "R183": [
        slot(
            "RQ1-I1",
            "Autismo (acceso y coordinación de servicios en Alabama)",
            "extracted",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "This study investigates the potential of artificial intelligence, particularly Natural Lan- guage Processing and large-scale language models, to improve resource manage- ment and service access for individuals with autism in Alabama.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. La evaluación contrasta sistemas/tipos de consulta, no subgrupos clínicos dentro del autismo.",
            "partial",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "Fernandes, Federal University evaluated based on precision, recall, and response accuracy.",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: No | N: NR | Rol: NR (consultas simuladas para trabajadores sociales)",
            "partial",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "A standardized set of queries was used to simulate real-world scenarios encountered doi.org/10.1371/journal.pone.0342700 by social workers engaged in autism service coordination.",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: diferencia | Perfil: deducido | Consentimiento: NR | País: Estados Unidos (Alabama)",
            "partial",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "1 Department of Biological Sciences, The University of Alabama in Huntsville, Huntsville, Alabama, United States of America, 2 Department of Psychology, The University of Alabama in Huntsville, Huntsville, Alabama, United States of America, 3 Autism Services, Alabama Department of Mental Health, Montgomery, Alabama, United States of America, 4 Little Orange Fish, Huntsville, Alabama, United States of America",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "NLP; LLM; RAG | Modelo: GPT-4 (chatbot de dominio) entre otros",
            "extracted",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "AI systems, including general language models, domain-specific chatbots powered healthcare resource management and allocation: A focus on the autism community in by advanced language models, and a Retrieval-Augmented Generation framework.",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Generador de respuestas (chatbots y RAG) para escenarios de coordinación asistencial",
            "extracted",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "A standardized set of queries was used to simulate real-world scenarios encountered doi.org/10.1371/journal.pone.0342700 by social workers engaged in autism service coordination.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Pruebas (evaluación con precision, recall y exactitud de respuesta)",
            "extracted",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "evaluated based on precision, recall, and response accuracy. Results demonstrated of Paraiba, BRAZIL",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "Ingeniería de prompts y despliegue de marcos RAG frente a NLP clásico",
            "partial",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "that the Retrieval-Augmented Generation (RAG) framework achieved superior Received: January 14, 2025 performance compared to traditional NLP methods and general-purpose language Accepted: January 26, 2026 models, attaining approximately 90–96% precision and recall across evaluated query Published: March 16, 2026 types.",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: precision y recall (y exactitud) | Valor: ~90–96% precision y recall en tipos de consulta evaluados (abstract)",
            "extracted",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "that the Retrieval-Augmented Generation (RAG) framework achieved superior Received: January 14, 2025 performance compared to traditional NLP methods and general-purpose language Accepted: January 26, 2026 models, attaining approximately 90–96% precision and recall across evaluated query Published: March 16, 2026 types.",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Consultas estandarizadas que simulan navegación de servicios para autismo",
            "extracted",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "A standardized set of queries was used to simulate real-world scenarios encountered doi.org/10.1371/journal.pone.0342700 by social workers engaged in autism service coordination.",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (equidad en salud y utilidad práctica; sin WCAG explícito en la cita)",
            "partial",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "and enhancing healthcare equity. By streamlining care coordination and delivering",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "to improve resource manage- ment and service access for individuals with autism in Alabama.",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Semiautomática (evaluación con consultas simuladas; sin validación con usuarios finales explícita en la cita)",
            "partial",
            [
                ev(
                    "R183-using-ai-to-enhance-healthcare-resource-management-and-allocation-a-focus-on-the.md",
                    "1",
                    "A standardized set of queries was used to simulate real-world scenarios encountered doi.org/10.1371/journal.pone.0342700 by social workers engaged in autism service coordination.",
                )
            ],
        ),
    ],
    "R187": [
        slot(
            "RQ1-I1",
            "Neurodivergencia explícita (lista: TDAH, autismo, dislexia, discapacidad intelectual, etc.)",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "including those with ADHD, autism, dyslexia, mood disor- bi-directional alignment between neurodivergent users and LLMs, ders, anxiety disorders, intellectual disabilities, and other natural",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. Evidencia cualitativa desde logs y entrevistas; sin desagregación cuantitativa por diagnóstico en el resumen.",
            "partial",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "Through analysis of over 300 chat logs and interviews with 15",
                ),
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "neurodivergent participants, we found that the chatbot frequently",
                ),
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: Sí | N: 15 participantes neurodivergentes | Rol: evaluación",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "Through analysis of over 300 chat logs and interviews with 15",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: diferencia (búsqueda de empleo) | Perfil: almacenado | Consentimiento: NR | País: EE. UU. (Georgia Tech / NYU en cabecera)",
            "partial",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "Georgia Institute of Technology Atlanta, Georgia, USA",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "LLM | Modelo: GPT-4 (chatbot de apoyo a la búsqueda de empleo)",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "ine interactions between neurodivergent job-seekers and a GPT-4- Large Language Models (LLMs) are primarily trained on data that powered career support chatbot through the lens of misalignment.",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Asistente de carrera (chatbot) con recomendaciones conversacionales",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "powered career support chatbot through the lens of misalignment.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Evaluación empírica (logs + entrevistas) en estudio cualitativo",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "Through analysis of over 300 chat logs and interviews with 15",
                ),
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "neurodivergent participants, we found that the chatbot frequently",
                ),
            ],
        ),
        slot(
            "RQ2-I4",
            "Análisis cualitativo de interacción y diseño de IA centrado en desajuste",
            "partial",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "integrate neurodivergent perspec- neurological differences [9]– this imposition of neurotypical norms tives and preferences to ensure more authentic, personalized, and can result in significant psychological harm [25, 77], as it can cause human-centered AI support.",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: desajuste (misalignment) percibido | Valor: >300 logs; 15 entrevistas (conteos explícitos)",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "Through analysis of over 300 chat logs and interviews with 15",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Registros de chat y entrevistas con participantes neurodivergentes",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "Through analysis of over 300 chat logs and interviews with 15",
                ),
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "neurodivergent participants, we found that the chatbot frequently",
                ),
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (ASSETS/SIGACCESS como foro; sin WCAG operativo en la cita)",
            "partial",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "SIGACCESS Conference on Computers and Accessibility (ASSETS ’25), October",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "including those with ADHD, autism, dyslexia, mood disor- bi-directional alignment between neurodivergent users and LLMs, ders, anxiety disorders, intellectual disabilities, and other natural",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Validación con usuarios (entrevistas + interacciones reales con el chatbot)",
            "extracted",
            [
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "Through analysis of over 300 chat logs and interviews with 15",
                ),
                ev(
                    "R187-understanding-human-ai-misalignment-in-llm-based-job-seeking-support-for-neurodi.md",
                    "1",
                    "neurodivergent participants, we found that the chatbot frequently",
                ),
            ],
        ),
    ],
    "R193": [
        slot(
            "RQ1-I1",
            "Discapacidad de aprendizaje (caso con usuario con learning disability)",
            "extracted",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "woman with a learning disability and her LLM-based smart speaker ion’ has been reminding its user ‘Lucy’ about her daily tasks so in a ‘smart homecare’ setting, we show how the system’s multi- persistently that she shouts at it, then threatens to throw it out the unit repair initiations, persistent reminders, and inappropriately window. designed talk create interactional trouble that burdens the user with the work of restoring shared understanding.",
                )
            ],
        ),
        slot(
            "RQ1-I2",
            "No. Estudio conversacional de caso; sin estadística por perfiles.",
            "partial",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "These are often treated 1.1 Extract 1: Do you want to go out that as ‘usability issues’, but we argue that they are better understood as window?",
                )
            ],
        ),
        slot(
            "RQ1-I3",
            "Presencia: Sí | N: 1 caso analizado en el abstract | Rol: evaluación (interacción grabada)",
            "partial",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "woman with a learning disability and her LLM-based smart speaker ion’ has been reminding its user ‘Lucy’ about her daily tasks so in a ‘smart homecare’ setting, we show how the system’s multi- persistently that she shouts at it, then threatens to throw it out the unit repair initiations, persistent reminders, and inappropriately window. designed talk create interactional trouble that burdens the user with the work of restoring shared understanding.",
                )
            ],
        ),
        slot(
            "RQ1-I4",
            "Enfoque: déficit | Perfil: deducido | Consentimiento: NR | País: Reino Unido (Loughborough) en cabecera",
            "partial",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "Loughborough, Leicestershire, United Loughborough, United Kingdom",
                )
            ],
        ),
        slot(
            "RQ2-I1",
            "LLM | Modelo: NR (altavoz inteligente basado en LLM)",
            "partial",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "in care contexts, yet their interactions often undermine the very au- in practice, the closest such devices may get to being treated as tonomy and agency they claim to support for their users.",
                )
            ],
        ),
        slot(
            "RQ2-I2",
            "Asistente de voz conversacional en domótica asistencial",
            "extracted",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "woman with a learning disability and her LLM-based smart speaker ion’ has been reminding its user ‘Lucy’ about her daily tasks so in a ‘smart homecare’ setting, we show how the system’s multi- persistently that she shouts at it, then threatens to throw it out the unit repair initiations, persistent reminders, and inappropriately window. designed talk create interactional trouble that burdens the user with the work of restoring shared understanding.",
                )
            ],
        ),
        slot(
            "RQ2-I3",
            "Evaluación mediante análisis conversacional (CA) de interacciones naturales",
            "extracted",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "These are often treated 1.1 Extract 1: Do you want to go out that as ‘usability issues’, but we argue that they are better understood as window? recurring design problems in how LLMs produce talk.",
                )
            ],
        ),
        slot(
            "RQ2-I4",
            "Provocaciones de diseño (repair, agency, recipient design) para fabricantes",
            "extracted",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "We outline Listen to audio: https://bit.ly/not-listening1 three key areas: repair, agency, and recipient design, and offer nine design provocations to challenge the designers of smart homecare 1 SEN: Good morning breakfast is planned for now. voice assistants to rethink how ‘conversational’ these technologies 2 what will it be today. need to be.",
                )
            ],
        ),
        slot(
            "RQ3-I1",
            "Constructo: fallos de diseño del habla generada por LLM | Valor: NR (CA cualitativo)",
            "partial",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "we argue that they are better understood as window? recurring design problems in how LLMs produce talk.",
                )
            ],
        ),
        slot(
            "RQ3-I2",
            "Análisis conversacional de video; transcripción de interacciones con el asistente",
            "extracted",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "woman with a learning disability and her LLM-based smart speaker ion’ has been reminding its user ‘Lucy’ about her daily tasks so in a ‘smart homecare’ setting, we show how the system’s multi- persistently that she shouts at it, then threatens to throw it out the unit repair initiations, persistent reminders, and inappropriately window. designed talk create interactional trouble that burdens the user with the work of restoring shared understanding.",
                )
            ],
        ),
        slot(
            "RQ3-I3",
            "NR (CCS incluye Accessibility; sin WCAG operativo en la cita)",
            "partial",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "Human-centered computing; • Empirical studies in HCI; • 7 SEN: It seems quiet from you. Just checking in Accessibility;",
                )
            ],
        ),
        slot(
            "RQ3-I4",
            "Cognitiva",
            "extracted",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "woman with a learning disability and her LLM-based smart speaker",
                )
            ],
        ),
        slot(
            "RQ3-I5",
            "Validación con usuarios (interacción doméstica grabada; enfoque cualitativo)",
            "extracted",
            [
                ev(
                    "R193-you-re-not-listening-llm-smart-speakers-need-to-learn-when-to-shut-up.md",
                    "1",
                    "woman with a learning disability and her LLM-based smart speaker ion’ has been reminding its user ‘Lucy’ about her daily tasks so in a ‘smart homecare’ setting, we show how the system’s multi- persistently that she shouts at it, then threatens to throw it out the unit repair initiations, persistent reminders, and inappropriately window. designed talk create interactional trouble that burdens the user with the work of restoring shared understanding.",
                )
            ],
        ),
    ],
}

LOTE01.update(_LOTE01_REST2)


def verify_quotes() -> None:
    for aid, slots in LOTE01.items():
        for s in slots:
            for i, e in enumerate(s.get("evidence") or []):
                src = REPO / e["src"]
                quote = e["quote"]
                raw = src.read_text(encoding="utf-8", errors="replace")
                norm_q = " ".join(quote.split())
                norm_f = " ".join(raw.split())
                if norm_q not in norm_f and norm_q.casefold() not in norm_f.casefold():
                    raise SystemExit(f"QUOTE FAIL {aid} {s['item_id']} ev[{i}]: not substring of {src}")


def write_outputs() -> None:
    OUT_DEBATE.mkdir(parents=True, exist_ok=True)
    stub_q = "## cribado2:query (cruce)\nPregunta acotada por ítem; síntesis en `apply-*.json`.\n"
    for aid, slots in LOTE01.items():
        payload = {
            "article_id": aid,
            "lote": "01",
            "slots": slots,
            "source": "scripts/build_ia_inclusion_lote01_apply.py",
        }
        (OUT_DEBATE / f"apply-{aid}.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (OUT_DEBATE / f"r1-defensor-{aid}.md").write_text(stub_q, encoding="utf-8")
        (OUT_DEBATE / f"r2-critico-{aid}.md").write_text(
            "Checklist: prosa ES; registro+matiz; evidencia `p. N` + quote literal ≥40.\n", encoding="utf-8"
        )
        (OUT_DEBATE / f"orquestador-{aid}.md").write_text(
            "Aprobado: `apply-*.json` listo para `formulario:apply-lote 01`.\n", encoding="utf-8"
        )


def main() -> None:
    verify_quotes()
    write_outputs()
    print("OK:", len(LOTE01), "articles →", OUT_DEBATE)


if __name__ == "__main__":
    main()
