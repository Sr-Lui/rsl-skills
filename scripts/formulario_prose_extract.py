"""Registro agregable + redacción ES breve para celdas de ítem (formulario apply)."""
from __future__ import annotations

import re
from pathlib import Path


def _ev(rel_fn, md: Path, quote: str) -> list[dict]:
    q = " ".join(quote.split())[:160]
    return [{"src": rel_fn(md), "loc": "fulltext", "quote": q}] if q else []


def _absent():
    return "—", "absent", []


def _cell(register: str, note: str | None = None) -> str:
    """Registro literal (para agregación) + oración breve en español."""
    reg = register.strip()
    if not note or not note.strip():
        return reg
    note = note.strip().rstrip(".")
    if reg in ("Sí", "No", "NR") or (len(reg) > 4 and reg in note):
        return f"{reg}. {note}."
    if reg in note:
        return f"{note}."
    return f"{reg}. {note}."


def _wrap(lead: str, register: str) -> str:
    """Intro legible con registro entre paréntesis (mixto / plantillas)."""
    lead = lead.strip().rstrip(".")
    return f"{lead} ({register})."


def _sdlc_phase(text: str, tl: str) -> str | None:
    """Fase principal SDLC donde interviene la IA (ventanas cerca de términos IA)."""
    ai_pat = re.compile(
        r"\b(llm|large language model|gpt|claude|llama|generative ai|"
        r"machine learning|deep learning|\bai\b|artificial intelligence|"
        r"neural network|nlp|prompt engineering|model selection)\b",
        re.I,
    )
    chunks: list[str] = []
    for m in ai_pat.finditer(tl):
        s = max(0, m.start() - 200)
        e = min(len(tl), m.end() + 200)
        chunks.append(tl[s:e])
    blob = " ".join(chunks) if chunks else tl[:120000]
    title_blob = tl[:2500]

    rules: list[tuple[str, str, int]] = [
        ("Pruebas", r"empirical study|experiment|evaluation|assessed|user study|"
         r"participants|metric|readability|usability test|ηp2|cohen|anova|survey", 2),
        ("Desarrollo", r"implement(ed|ation)|develop(ed|ment)|code generat|software build|"
         r"programming|deployment|pipeline", 2),
        ("Diseño", r"prototype|wireframe|ui/ux|interface design|mockup|figma", 2),
        ("Requisitos", r"requirement elicitation|user stor(y|ies)|specification phase|"
         r"requirements engineering", 3),
        ("Personalización en ejecución", r"runtime|personaliz|in situ|live system", 2),
        ("V&V", r"verif(y|ication)|validat(ion|e)", 2),
        ("Auditoría", r"\baudit\b|compliance check", 2),
    ]
    scores: dict[str, int] = {c: 0 for c, _, _ in rules}
    for cat, pat, w in rules:
        scores[cat] += w * len(re.findall(pat, blob, re.I))
        if cat == "Pruebas":
            scores[cat] += w * len(re.findall(pat, title_blob, re.I))
    best = max(scores.values())
    if best == 0:
        if re.search(r"empirical|experiment|evaluation", title_blob, re.I):
            return "Pruebas"
        return None
    top = [c for c, v in scores.items() if v == best]
    if "Pruebas" in top and "Requisitos" in top:
        return "Pruebas"
    return top[0]


def _profiles_tokens(tl: str) -> list[str]:
    out = []
    if re.search(r"autism|autistic|\basd\b", tl):
        out.append("TEA")
    if re.search(r"\badhd\b", tl):
        out.append("TDAH")
    if re.search(r"intellectual disabilit|\bDI\b", tl):
        out.append("DI")
    if re.search(r"dyslexia", tl):
        out.append("dislexia")
    if re.search(r"learning disabilit", tl):
        out.append("dificultades de aprendizaje")
    if re.search(r"cognitive impair", tl):
        out.append("discapacidad cognitiva")
    if re.search(r"neurodiver", tl):
        out.append("neurodivergencia")
    if re.search(r"down syndrome", tl):
        out.append("síndrome de Down")
    return list(dict.fromkeys(out))


def extract_item_prose(
    item_id: str, text: str, tl: str, md: Path, rel_fn
) -> tuple[str, str, list]:
    if item_id == "RQ1-I1":
        tok = _profiles_tokens(tl)
        if not tok:
            return _absent()
        reg = "; ".join(tok)
        return (
            _wrap("La población del estudio declara perfiles", reg),
            "extracted",
            _ev(rel_fn, md, reg),
        )

    if item_id == "RQ1-I2":
        if re.search(r"stratif|subgroup|sub-group|by diagnosis|per profile|split by", tl):
            return (
                _cell(
                    "Sí",
                    "El artículo reporta estratificación o desagregación de resultados por perfil o subgrupo",
                ),
                "extracted",
                _ev(rel_fn, md, "estratificación"),
            )
        if re.search(r"participants|sample|subjects|users", tl):
            return (
                _cell(
                    "No",
                    "No hay desagregación por perfil cognitivo; los resultados corresponden a la muestra global",
                ),
                "extracted",
                _ev(rel_fn, md, "muestra"),
            )
        return _absent()

    if item_id == "RQ1-I3":
        if not re.search(r"participant|user study|users|co-design|involv", tl):
            return _absent()
        pres = "Sí"
        n = "NR"
        m = re.search(r"(\d+)\s+participants|\b[Nn]\s*[=:]\s*(\d+)", text)
        if m:
            n = m.group(1) or m.group(2)
        rol = "evaluación"
        if re.search(r"co-design|participatory|design workshop", tl):
            rol = "ambos"
        elif re.search(r"design", tl) and not re.search(r"evaluat|test|study", tl):
            rol = "diseño"
        reg = f"Presencia: {pres} | N: {n} | Rol: {rol}"
        if rol == "ambos":
            lead = "Participación de personas con la condición en diseño y evaluación"
        elif rol == "diseño":
            lead = "Participación en actividades de diseño"
        else:
            lead = "Participación en evaluación o prueba con usuarios"
        if n != "NR":
            lead += f", con n = {n} participantes reportados"
        dec = "extracted" if n != "NR" else "partial"
        return _wrap(lead, reg), dec, _ev(rel_fn, md, n)

    if item_id == "RQ1-I4":
        pais = "NR"
        for pat, name in (
            (r"\b(Spain|España)\b", "España"),
            (r"\b(United States|USA|U\.S\.)\b", "Estados Unidos"),
            (r"\b(China)\b", "China"),
            (r"\b(India)\b", "India"),
            (r"\b(UK|United Kingdom)\b", "Reino Unido"),
            (r"\b(Canada)\b", "Canadá"),
            (r"\b(Germany)\b", "Alemania"),
        ):
            if re.search(pat, text, re.I):
                pais = name
                break
        enfoque = "NR"
        if re.search(r"strength|asset|difference model|social model", tl):
            enfoque = "diferencia"
        elif re.search(r"deficit|impairment|disabilit", tl):
            enfoque = "déficit"
        perfil = "deducido"
        if re.search(r"diagnosis|medical record|stored profile", tl):
            perfil = "almacenado"
        cons = "NR"
        if re.search(r"IRB|ethics committee|informed consent|consent form", tl):
            cons = "informado reportado"
        if pais == "NR" and enfoque == "NR" and cons == "NR":
            return _absent()
        reg = f"Enfoque: {enfoque} | Perfil: {perfil} | Consentimiento: {cons} | País: {pais}"
        return (
            _wrap("Marco ético, tratamiento del perfil y contexto del estudio", reg),
            "partial" if pais == "NR" or cons == "NR" else "extracted",
            _ev(rel_fn, md, pais),
        )

    if item_id == "RQ2-I1":
        fam = []
        if re.search(r"\bllm\b|large language model|genai|generative ai", tl):
            fam.append("LLM")
        if re.search(r"\bnlp\b|natural language", tl):
            fam.append("NLP")
        if re.search(r"deep learning|neural network", tl):
            fam.append("DL")
        if re.search(r"machine learning|\bml\b", tl):
            fam.append("ML")
        if re.search(r"computer vision|image recognition", tl):
            fam.append("visión")
        mod = re.search(r"(GPT-4[o]?|Claude[-\w]*|Llama[-\.\d\w]*)", text, re.I)
        if not fam and not mod:
            return _absent()
        reg = "; ".join(fam) if fam else "IA"
        if mod:
            reg += f" | Modelo: {mod.group(1)}"
        else:
            reg += " | Modelo: NR"
        return (
            _wrap("Familia de técnica de IA aplicada", reg),
            "extracted",
            _ev(rel_fn, md, reg),
        )

    if item_id == "RQ2-I2":
        roles = []
        if re.search(r"generat(e|ing)|produce|output", tl):
            roles.append("Generador")
        if re.search(r"evaluat(e|ing|or)|assess|metric", tl):
            roles.append("evaluador")
        if re.search(r"quality assurance|assist", tl):
            roles.append("asistente de aseguramiento de la calidad")
        if not roles:
            if re.search(r"\bai\b|artificial intelligence|model", tl):
                return (
                    _cell("otro", "La IA es central en el artefacto, sin rol explícito en el ciclo de vida"),
                    "partial",
                    _ev(rel_fn, md, "AI"),
                )
            return _absent()
        reg = "; ".join(dict.fromkeys(roles))
        return (
            _wrap("Rol de la IA en el estudio", reg),
            "extracted",
            _ev(rel_fn, md, roles[0]),
        )

    if item_id == "RQ2-I3":
        cat = _sdlc_phase(text, tl)
        if not cat:
            return _absent()
        return (
            _cell(
                cat,
                f"Fase principal del ciclo de vida del software en la que interviene la IA",
            ),
            "extracted",
            _ev(rel_fn, md, cat),
        )

    if item_id == "RQ2-I4":
        found = []
        for lab, pat in (
            ("diseño", r"\bdesign\b"),
            ("desarrollo", r"develop|implement"),
            ("pruebas", r"test|evaluat|experiment"),
            ("requisitos", r"requirement"),
        ):
            if re.search(pat, tl):
                found.append(lab)
        if len(found) <= 1:
            return (
                _cell("—", "Solo se identifica una fase del ciclo vinculada a la IA"),
                "extracted",
                _ev(rel_fn, md, "una fase"),
            )
        reg = "; ".join(found[1:] if len(found) > 1 else found)
        return (
            _cell(reg, "Otras fases del ciclo de vida mencionadas además de la principal"),
            "extracted",
            _ev(rel_fn, md, ";".join(found)),
        )

    if item_id == "RQ3-I1":
        m = re.search(
            r"\b(Flesch[-\w]*|accuracy|precision|recall|F1[- ]?score|SUS|reading ease)\b"
            r"[^.\n]{0,50}?(\d+\.?\d*)",
            text,
            re.I,
        )
        if m:
            constructo = m.group(1).strip()
            valor = m.group(2)
            reg = f"Constructo: {constructo} | Valor: {valor}"
            return (
                _wrap(f"Resultado principal reportado ({constructo} = {valor})", reg),
                "extracted",
                _ev(rel_fn, md, m.group(0)[:80]),
            )
        if re.search(r"metric|measure|score|performance|readability", tl):
            reg = "Constructo: métrica reportada | Valor: NR"
            return (
                _cell(reg, "Se mencionan métricas, pero sin valor numérico principal claro en el texto"),
                "partial",
                _ev(rel_fn, md, "métricas"),
            )
        return _absent()

    if item_id == "RQ3-I2":
        inst = []
        if re.search(r"questionnaire|survey", tl):
            inst.append("cuestionario")
        if re.search(r"heuristic", tl):
            inst.append("heurística")
        if re.search(r"user study|think aloud|usability", tl):
            inst.append("estudio con usuarios")
        if re.search(r"Flesch|readability", tl):
            inst.append("legibilidad")
        if not inst:
            return _absent()
        reg = "; ".join(dict.fromkeys(inst))
        return (
            _wrap("Instrumento o protocolo de medición", reg),
            "extracted",
            _ev(rel_fn, md, inst[0]),
        )

    if item_id == "RQ3-I3":
        if re.search(r"\bWCAG\b", tl):
            return (
                _cell("WCAG", "Marco normativo de accesibilidad referenciado en el estudio"),
                "extracted",
                _ev(rel_fn, md, "WCAG"),
            )
        if re.search(r"\bCOGA\b|cognitive accessibility", tl):
            return (
                _cell("COGA", "Alineación con accesibilidad cognitiva"),
                "extracted",
                _ev(rel_fn, md, "COGA"),
            )
        if re.search(r"accessib", tl):
            return (
                _cell(
                    "ninguno",
                    "Trata accesibilidad sin citar WCAG ni COGA de forma explícita",
                ),
                "partial",
                _ev(rel_fn, md, "accessibility"),
            )
        return _absent()

    if item_id == "RQ3-I4":
        cog = bool(re.search(r"cognitive|dyslexia|ADHD|autism|learning disabilit|readability", tl))
        sen = bool(re.search(r"visual|blind|hearing|sensor|motor impairment", tl))
        if cog and sen:
            return (
                _cell("Ambas", "La evaluación aborda dimensiones cognitivas y sensoriales"),
                "extracted",
                _ev(rel_fn, md, "ambas"),
            )
        if cog:
            return (
                _cell("Cognitiva", "Enfoque en accesibilidad cognitiva o legibilidad"),
                "extracted",
                _ev(rel_fn, md, "cognitiva"),
            )
        if sen:
            return (
                _cell("Sensorial", "Predominan aspectos sensoriales de accesibilidad"),
                "extracted",
                _ev(rel_fn, md, "sensorial"),
            )
        return _absent()

    if item_id == "RQ3-I5":
        if re.search(r"automated (test|evaluation)|continuous integration|\bCI\b", tl):
            return (
                _cell(
                    "Integración continua",
                    "Evaluación automatizada o integrada en el pipeline de desarrollo",
                ),
                "extracted",
                _ev(rel_fn, md, "CI"),
            )
        if re.search(r"semi-?automatic|human-in-the-loop", tl):
            return (
                _cell("Semiautomática", "Combina pasos automáticos con revisión humana"),
                "extracted",
                _ev(rel_fn, md, "semi"),
            )
        if re.search(r"user study|participants|usability test", tl):
            return (
                _cell(
                    "Solo validación con usuarios",
                    "La validación depende principalmente de participantes",
                ),
                "extracted",
                _ev(rel_fn, md, "users"),
            )
        return _absent()

    return _absent()
