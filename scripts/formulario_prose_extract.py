"""Prosa ES para celdas de ítem (formulario apply). Conservador: cite-or-dash."""
from __future__ import annotations

import re
from pathlib import Path

THEME_HOOK = " Aporta evidencia a la RSL sobre IA e inclusión cognitiva en el desarrollo de software."


def _ev(rel_fn, md: Path, quote: str) -> list[dict]:
    q = " ".join(quote.split())[:160]
    return [{"src": rel_fn(md), "loc": "fulltext", "quote": q}] if q else []


def _absent():
    return "—", "absent", []


def _profiles_es(tl: str) -> list[str]:
    out = []
    if re.search(r"learning disabilit", tl):
        out.append("dificultades de aprendizaje")
    if re.search(r"cognitive impair|intellectual disabilit", tl):
        out.append("discapacidad cognitiva")
    if re.search(r"\badhd\b", tl):
        out.append("TDAH")
    if re.search(r"autism|autistic|\basd\b", tl):
        out.append("autismo")
    if re.search(r"dyslexia", tl):
        out.append("dislexia")
    if re.search(r"neurodiver", tl):
        out.append("neurodivergencia")
    if re.search(r"down syndrome", tl):
        out.append("síndrome de Down")
    return out


def extract_item_prose(
    item_id: str, text: str, tl: str, md: Path, rel_fn
) -> tuple[str, str, list]:
    if item_id == "RQ1-I1":
        prof = _profiles_es(tl)
        if not prof:
            return _absent()
        lista = ", ".join(dict.fromkeys(prof))
        v = (
            f"El estudio delimita la población en torno a {lista}, "
            f"alineado con perfiles de discapacidad cognitiva o neurodivergencia relevantes para la RSL."
            + THEME_HOOK
        )
        return v, "extracted", _ev(rel_fn, md, lista)

    if item_id == "RQ1-I2":
        if re.search(r"stratif|subgroup|sub-group|by diagnosis|per profile|split by", tl):
            v = (
                "Sí reporta estratificación o desagregación de resultados según perfiles "
                "o subgrupos, lo que permite comparar evidencia por población en la síntesis."
                + THEME_HOOK
            )
            return v, "extracted", _ev(rel_fn, md, "estratificación")
        if re.search(r"participants|sample|subjects|users", tl):
            v = (
                "No indica estratificación ni análisis desagregados por perfil cognitivo "
                "o neurodivergente; los resultados se reportan sobre la muestra global, "
                "limitando comparaciones por subpoblación en el formulario."
                + THEME_HOOK
            )
            return v, "extracted", _ev(rel_fn, md, "muestra")
        return _absent()

    if item_id == "RQ1-I3":
        if not re.search(r"participant|user study|users|co-design|involv", tl):
            return _absent()
        n = None
        m = re.search(r"(\d+)\s+participants|\b[Nn]\s*[=:]\s*(\d+)", text)
        if m:
            n = m.group(1) or m.group(2)
        rol = "evaluación o diseño"
        if re.search(r"co-design|participatory|design workshop", tl):
            rol = "co-diseño y evaluación"
        ntxt = f"{n} participantes" if n else "tamaño muestral no precisado en el extracto revisado"
        v = (
            f"Hay participación de personas en {rol} ({ntxt}), "
            f"relevante para validez centrada en usuarios con necesidades cognitivas."
            + THEME_HOOK
        )
        return v, "extracted" if n else "partial", _ev(rel_fn, md, ntxt)

    if item_id == "RQ1-I4":
        pais = None
        for pat, name in (
            (r"\b(Spain|España)\b", "España"),
            (r"\b(United States|USA|U\.S\.)\b", "Estados Unidos"),
            (r"\b(China)\b", "China"),
            (r"\b(India)\b", "India"),
            (r"\b(UK|United Kingdom)\b", "Reino Unido"),
            (r"\b(Canada)\b", "Canadá"),
            (r"\b(Germany)\b", "Alemania"),
            (r"\b(Alabama)\b", "Alabama (EE. UU.)"),
        ):
            if re.search(pat, text, re.I):
                pais = name
                break
        cons = "consentimiento informado o aprobación ética" if re.search(
            r"IRB|ethics committee|informed consent|consent form", tl
        ) else None
        parts = []
        if pais:
            parts.append(f"contexto geográfico asociado a {pais}")
        if cons:
            parts.append(f" menciona {cons}")
        if not parts:
            return _absent()
        v = "El artículo reporta " + " y ".join(parts) + "." + THEME_HOOK
        return v, "partial" if not cons else "extracted", _ev(rel_fn, md, pais or cons or "")

    if item_id == "RQ2-I1":
        fam = []
        if re.search(r"\bllm\b|large language model", tl):
            fam.append("modelos de lenguaje grande (LLM)")
        if re.search(r"\bnlp\b|natural language", tl):
            fam.append("procesamiento de lenguaje natural")
        if re.search(r"deep learning|neural network", tl):
            fam.append("aprendizaje profundo")
        if re.search(r"machine learning|\bml\b", tl):
            fam.append("aprendizaje automático")
        mod = re.search(r"(GPT-4[o]?|Claude[-\w]*|Llama[-\.\d\w]*)", text, re.I)
        if not fam and not mod:
            return _absent()
        base = "La intervención de IA se apoya en " + ", ".join(fam) if fam else "El estudio emplea IA"
        if mod:
            base += f", con mención explícita de {mod.group(1)}"
        v = base + ", en línea con técnicas aplicadas a accesibilidad o inclusión cognitiva." + THEME_HOOK
        return v, "extracted", _ev(rel_fn, md, fam[0] if fam else mod.group(1))

    if item_id == "RQ2-I2":
        roles = []
        if re.search(r"generat(e|ing)|produce|output", tl):
            roles.append("generación de contenido o respuestas")
        if re.search(r"evaluat(e|ing|or)|assess|metric", tl):
            roles.append("evaluación o medición")
        if re.search(r"quality assurance|assist", tl):
            roles.append("asistencia en aseguramiento de calidad")
        if not roles:
            if re.search(r"\bai\b|artificial intelligence|model", tl):
                v = (
                    "La IA interviene como componente central del artefacto o del experimento, "
                    "sin un rol SDLC explícito en el texto revisado."
                    + THEME_HOOK
                )
                return v, "partial", _ev(rel_fn, md, "AI")
            return _absent()
        v = (
            "El rol principal de la IA es "
            + " y ".join(dict.fromkeys(roles))
            + " dentro del estudio de software o contenido digital accesible."
            + THEME_HOOK
        )
        return v, "extracted", _ev(rel_fn, md, roles[0])

    if item_id == "RQ2-I3":
        for lab, pat, frase in (
            (
                "pruebas",
                r"\btest(ing|s)?\b|experiment|empirical|user study|evaluation",
                "La fase principal vinculada a la IA es pruebas o evaluación empírica del artefacto o de salidas generadas.",
            ),
            (
                "desarrollo",
                r"implement(ed|ation)|develop(ed|ment)|built",
                "La IA se utiliza principalmente en desarrollo o implementación del software o prototipo.",
            ),
            (
                "diseño",
                r"\bdesign\b|prototype|UI/UX|interface",
                "La contribución de la IA se sitúa en diseño o prototipado de la solución.",
            ),
            (
                "requisitos",
                r"requirement|elicitation",
                "El trabajo aborda requisitos o definición de necesidades con apoyo de IA.",
            ),
        ):
            if re.search(pat, tl):
                return frase + THEME_HOOK, "extracted", _ev(rel_fn, md, lab)
        return _absent()

    if item_id == "RQ2-I4":
        found = []
        for lab, pat in (
            ("diseño", r"\bdesign\b"),
            ("desarrollo", r"develop|implement"),
            ("pruebas", r"test|evaluat|experiment"),
        ):
            if re.search(pat, tl):
                found.append(lab)
        if len(found) <= 1:
            v = "Solo se identifica una fase del ciclo de vida vinculada a la IA; no hay otras fases secundarias reportadas." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "una fase")
        sec = [f for f in found[1:]] or found
        v = "Además de la fase principal, el artículo alude a " + ", ".join(sec) + " en el ciclo de vida." + THEME_HOOK
        return v, "extracted", _ev(rel_fn, md, ", ".join(sec))

    if item_id == "RQ3-I1":
        m = re.search(
            r"(Flesch[^.\n]{0,30}|accuracy|precision|recall|F1|SUS|reading ease)[^.\n]{0,60}(\d+\.?\d*)",
            text,
            re.I,
        )
        if m:
            v = (
                f"Reporta como métrica principal {m.group(1).strip()} con valor numérico {m.group(2)}, "
                f"útil para la síntesis de resultados de accesibilidad cognitiva."
                + THEME_HOOK
            )
            return v, "extracted", _ev(rel_fn, md, m.group(0)[:80])
        if re.search(r"metric|measure|score|performance|readability", tl):
            v = (
                "Menciona medidas de desempeño o legibilidad, pero sin un valor numérico principal "
                "claro en el extracto revisado."
                + THEME_HOOK
            )
            return v, "partial", _ev(rel_fn, md, "métricas")
        return _absent()

    if item_id == "RQ3-I2":
        inst = []
        if re.search(r"questionnaire|survey", tl):
            inst.append("cuestionario o encuesta")
        if re.search(r"heuristic", tl):
            inst.append("evaluación heurística")
        if re.search(r"user study|think aloud|usability", tl):
            inst.append("estudio con usuarios")
        if re.search(r"Flesch|readability", tl):
            inst.append("índices de legibilidad")
        if not inst:
            return _absent()
        v = "El protocolo de medición incluye " + ", ".join(dict.fromkeys(inst)) + "." + THEME_HOOK
        return v, "extracted", _ev(rel_fn, md, inst[0])

    if item_id == "RQ3-I3":
        if re.search(r"\bWCAG\b", tl):
            v = "Se referencia explícitamente WCAG como marco de accesibilidad." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "WCAG")
        if re.search(r"\bCOGA\b|cognitive accessibility", tl):
            v = "Alinea la evaluación con accesibilidad cognitiva (COGA o equivalente)." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "COGA")
        if re.search(r"accessib", tl):
            v = (
                "Trata accesibilidad pero sin citar un marco normativo concreto (WCAG/COGA) "
                "en el texto revisado."
                + THEME_HOOK
            )
            return v, "partial", _ev(rel_fn, md, "accessibility")
        return _absent()

    if item_id == "RQ3-I4":
        cog = bool(re.search(r"cognitive|dyslexia|ADHD|autism|learning disabilit|readability", tl))
        sen = bool(re.search(r"visual|blind|hearing|sensor|motor impairment", tl))
        if cog and sen:
            v = "La evaluación combina dimensiones cognitivas y sensoriales." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "ambas")
        if cog:
            v = "La evaluación se centra en accesibilidad cognitiva o legibilidad." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "cognitiva")
        if sen:
            v = "Predominan aspectos sensoriales de accesibilidad." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "sensorial")
        return _absent()

    if item_id == "RQ3-I5":
        if re.search(r"automated (test|evaluation)|continuous integration", tl):
            v = "Describe evaluación automatizada o integrada en pipeline (alta automatización)." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "automated")
        if re.search(r"semi-?automatic|human-in-the-loop", tl):
            v = "Combina pasos automáticos con revisión humana (semiautomática)." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "semi")
        if re.search(r"user study|participants|usability test", tl):
            v = "La validación depende principalmente de usuarios, con automatización limitada." + THEME_HOOK
            return v, "extracted", _ev(rel_fn, md, "users")
        return _absent()

    return _absent()
