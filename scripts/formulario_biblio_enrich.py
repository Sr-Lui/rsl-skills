"""Biblio filas 8–10, 12–13: CSV ya aplicado en prepare; esto completa desde artículo, metadatos web y MD."""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = "rsl-skills-formulario/1.0 (mailto:fer@localhost; biblio-enrich)"

COUNTRY_ES: dict[str, str] = {
    "saudi arabia": "Arabia Saudita",
    "united states": "Estados Unidos",
    "u.s.a.": "Estados Unidos",
    "usa": "Estados Unidos",
    "china": "China",
    "india": "India",
    "united kingdom": "Reino Unido",
    "uk": "Reino Unido",
    "canada": "Canadá",
    "germany": "Alemania",
    "spain": "España",
    "españa": "España",
    "malaysia": "Malasia",
    "australia": "Australia",
    "sweden": "Suecia",
    "norway": "Noruega",
    "finland": "Finlandia",
    "france": "Francia",
    "italy": "Italia",
    "brazil": "Brasil",
    "mexico": "México",
    "colombia": "Colombia",
    "chile": "Chile",
    "argentina": "Argentina",
    "peru": "Perú",
    "perú": "Perú",
    "indonesia": "Indonesia",
    "japan": "Japón",
    "south korea": "Corea del Sur",
    "korea": "Corea del Sur",
    "taiwan": "Taiwán",
    "hong kong": "Hong Kong",
    "singapore": "Singapur",
    "netherlands": "Países Bajos",
    "belgium": "Bélgica",
    "switzerland": "Suiza",
    "austria": "Austria",
    "poland": "Polonia",
    "portugal": "Portugal",
    "ireland": "Irlanda",
    "new zealand": "Nueva Zelanda",
    "south africa": "Sudáfrica",
    "alabama": "Estados Unidos (Alabama)",
    "texas": "Estados Unidos (Texas)",
    "california": "Estados Unidos (California)",
    "bangladesh": "Bangladesh",
    "pakistan": "Pakistán",
    "nigeria": "Nigeria",
    "egypt": "Egipto",
    "turkey": "Turquía",
    "türkiye": "Turquía",
    "iran": "Irán",
    "israel": "Israel",
    "denmark": "Dinamarca",
    "czech republic": "República Checa",
    "czechia": "República Checa",
    "romania": "Rumanía",
    "greece": "Grecia",
    "thailand": "Tailandia",
    "vietnam": "Vietnam",
    "philippines": "Filipinas",
    "russia": "Rusia",
    "ukraine": "Ucrania",
}


def fetch_crossref(doi: str) -> dict | None:
    doi = doi.strip().lower()
    if not doi:
        return None
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=25) as resp:
            data = json.loads(resp.read().decode())
        return data.get("message") or {}
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None


def _country_from_affiliation(aff: str) -> str | None:
    if not aff:
        return None
    tail = aff.split(",")[-1].strip().lower()
    tail = re.sub(r"^\d+\s+", "", tail)
    for key, es in sorted(COUNTRY_ES.items(), key=lambda x: -len(x[0])):
        if key in tail or tail == key:
            return es
    if len(tail) > 2 and tail.isascii() and not tail.startswith("http"):
        return tail.title()
    return None


def editorial_from_crossref(msg: dict, revista: str) -> tuple[str, str, dict]:
    pub = (msg.get("publisher") or "").strip()
    if pub:
        pub = re.sub(r"\s*\([^)]+\)\s*$", "", pub).strip()
        if "Institute of Electrical" in pub or pub.endswith("IEEE"):
            pub = "IEEE"
        elif "John Wiley" in pub or "Wiley" in pub:
            pub = "John Wiley & Sons"
        elif "Springer" in pub:
            pub = "Springer Nature"
        elif "Elsevier" in pub:
            pub = "Elsevier"
        elif "Oxford University Press" in pub:
            pub = "Oxford University Press"
        elif "SAGE" in pub:
            pub = "SAGE Publications"
        elif "ACM" in pub or "Association for Computing" in pub:
            pub = "ACM"
        return pub, "web", {"publisher": msg.get("publisher")}
    r = (revista or "").lower()
    if "ieee access" in r or r.startswith("ieee "):
        return "IEEE", "article", {"revista": revista}
    if "plos one" in r:
        return "Public Library of Science", "web", {}
    return "—", "dash", {}


def pais_from_crossref(msg: dict, text: str) -> tuple[str, str, dict]:
    countries: list[str] = []
    for author in msg.get("author") or []:
        for aff in author.get("affiliation") or []:
            name = aff.get("name") or ""
            c = _country_from_affiliation(name)
            if c and c not in countries:
                countries.append(c)
    if countries:
        return countries[0] if len(countries) == 1 else "; ".join(countries[:3]), "web", {"affiliations": countries}
    tl = text.lower()
    for key, es in sorted(COUNTRY_ES.items(), key=lambda x: -len(x[0])):
        if re.search(rf"\b{re.escape(key)}\b", tl):
            return es, "article", {"match": key}
    return "—", "dash", {}


def volumen_from_crossref(msg: dict, text: str) -> tuple[str, str, dict]:
    vol = msg.get("volume")
    if vol is not None and str(vol).strip():
        issue = msg.get("issue")
        if issue:
            return f"{vol} ({issue})", "web", {"volume": vol, "issue": issue}
        return str(vol).strip(), "web", {"volume": vol}
    if (msg.get("type") or "") in ("proceedings-article", "book-chapter"):
        ct = msg.get("container-title") or msg.get("short-container-title") or []
        if ct:
            label = ct[0] if isinstance(ct, list) else str(ct)
            if len(label) > 100:
                label = label[:97] + "…"
            return label, "web", {"container-title": label}
        return "Acta de congreso (sin volumen)", "web", {"type": msg.get("type")}
    m = re.search(r"VOLUME\s+(\d+)", text, re.I)
    if m:
        return m.group(1), "article", {"loc": "md-header"}
    return "—", "dash", {}


def muestra_from_text(text: str, csv_resumen: str) -> tuple[str, str, dict]:
    blob = f"{csv_resumen}\n{text}"
    patterns = [
        (r"\b[Nn]\s*=\s*(\d+)\s+participants?", "participantes"),
        (r"(\d+)\s+participants?", "participantes"),
        (r"\(\s*[Nn]\s*=\s*(\d+)\s+responses?\)", "respuestas"),
        (r"\b[Nn]\s*=\s*(\d+)\s+responses?", "respuestas"),
        (r"\b[Nn]\s*=\s*(\d+)\s+(?:undergraduate|students?|children|users|adults|learners|parents|clinicians|caregivers|teachers|specialists)", "participantes"),
        (r"with\s+[Nn]\s*=\s*(\d+)", "participantes"),
        (r"(\d+)\s+children with", "participantes"),
        (r"(\d+)\s+children\b", "participantes"),
        (r"(\d+)\s+adults with", "participantes"),
        (r"(\d+)\s+adults\b", "participantes"),
        (r"(\d+)\s+users\b", "participantes"),
        (r"(\d+)\s+learners\b", "participantes"),
        (r"(\d+)\s+students\b", "participantes"),
        (r"(\d+)\s+annotators?", "anotadores"),
        (r"(\d+)\s+dyads?", "díadas"),
        (r"(\d+)\s+educator-student dyads", "díadas"),
        (r"(\d+)\s+test cases?", "casos de prueba"),
        (r"recruited\s+(\d+)", "participantes"),
        (r"sample of\s+(\d+)", "participantes"),
        (r"total of\s+(\d+)\s+participants", "participantes"),
        (r"(\d+)\s+in-depth interviews", "entrevistas"),
        (r"(\d+)\s+interviews", "entrevistas"),
        (r"recruited a total of (\d+)", "participantes"),
        (r"recruited a total of (\d+)\s+\S+\s+children", "participantes"),
        (r"invited (\d+) children", "participantes"),
        (r"total of (\d+)\s+\S+\s+children", "participantes"),
        (r"total of (\d+) children", "participantes"),
        (r"(\d+)\s+chat logs", "registros"),
        (r"over\s+(\d+)\s+chat", "registros"),
        (r"(\d+)\s+PWD", "participantes"),
        (r"Twelve postgraduate students", "participantes_twelve"),
        (r"evaluated with seven university\s+students", "participantes_seven"),
        (r"(\d+) personas con discapacidad cognitiva", "personas_dc"),
        (r"(\d+) expertos en lectura", "expertos"),
        (r"\(\s*[Nn]\s*=\s*(\d+)\s*\)", "participantes"),
        (r"\b[Nn]\s*=\s*(\d+)\b", "unidades"),
    ]
    for pat, kind in patterns:
        m = re.search(pat, blob, re.I)
        if m:
            if kind == "participantes_twelve":
                return "n = 12 estudiantes de posgrado", "article", {"pattern": pat}
            if kind == "participantes_seven":
                return "n = 7 estudiantes universitarios con TDAH", "article", {"pattern": pat}
            if kind == "personas_dc":
                n = m.group(1)
                ex = re.search(r"(\d+) expertos en lectura", blob, re.I)
                if ex:
                    return (
                        f"{n} personas con discapacidad cognitiva y {ex.group(1)} expertos (encuestas en línea)",
                        "article",
                        {},
                    )
                return f"{n} personas con discapacidad cognitiva (encuesta)", "article", {"n": n}
            if kind == "expertos":
                continue
            n = m.group(1)
            if kind == "unidades":
                ni = int(n)
                if ni > 5000 or (ni > 500 and "response" not in pat):
                    continue
            label = {
                "participantes": f"n = {n} participantes",
                "respuestas": f"n = {n} respuestas generadas",
                "unidades": f"n = {n}",
                "díadas": f"{n} díadas",
                "casos de prueba": f"{n} casos de prueba",
                "anotadores": f"{n} anotadores",
                "entrevistas": f"{n} entrevistas",
                "registros": f"{n} registros analizados",
            }.get(kind, n)
            return label, "article", {"pattern": pat, "n": n}
    if re.search(r"systematic review|scoping review|literature review", blob, re.I):
        return "Revisión bibliográfica (sin n empírico)", "article", {}
    if re.search(r"design (?:study|research)|conceptual|framework proposal|pilot platform", blob, re.I):
        if re.search(r"no (?:human )?participants|without user study", blob, re.I):
            return "Sin participantes humanos reportados", "article", {}
    if re.search(r"no human participants|without participants|synthetic dataset only", blob, re.I):
        return "Sin participantes humanos reportados", "article", {}
    return "—", "dash", {}


def contexto_from_text(text: str, csv_resumen: str, pais: str) -> tuple[str, str, dict]:
    blob = f"{csv_resumen}\n{text[:15000]}"
    tl = blob.lower()
    parts = []
    if re.search(r"alabama", tl):
        parts.append("servicios de autismo en Alabama (EE. UU.)")
    if re.search(r"public health|healthcare|hospital|clinical|ehealth|e-health|well-child", tl):
        parts.append("atención sanitaria o e-salud pública")
    if re.search(r"university|school|classroom|education|students?|campus", tl):
        parts.append("contexto educativo universitario o escolar")
    if re.search(r"museum", tl):
        parts.append("museo y accesibilidad cultural")
    if re.search(r"smart home|home automation|domestic", tl):
        parts.append("hogar inteligente")
    if re.search(r"co-design|participatory|workshop", tl):
        parts.append("co-diseño participativo con usuarios")
    if re.search(r"user study|usability test|field study|deployment study", tl):
        parts.append("evaluación con usuarios")
    if re.search(r"online experiment|factorial experiment|laboratory experiment", tl):
        parts.append("experimento controlado (laboratorio o en línea)")
    if re.search(r"open.?source|github|software platform|web platform|mobile app", tl):
        parts.append("desarrollo y evaluación de artefacto software")
    if not parts:
        if pais and pais != "—":
            return f"Estudio reportado en contexto asociado a {pais}.", "partial", {}
        return "—", "dash", {}
    sentence = "Contexto: " + "; ".join(dict.fromkeys(parts)) + "."
    if len(sentence) > 220:
        sentence = sentence[:217] + "…"
    return sentence, "article", {"themes": parts}


MANUAL_ROW13: dict[str, str] = {
    "R106": "164 personas con discapacidad cognitiva y 73 expertos en lectura fácil (encuestas en línea)",
    "R183": "Sin participantes humanos (evaluación con consultas estandarizadas)",
    "R263": "Sin participantes humanos",
    "R264": "Marco conceptual sin evaluación empírica con participantes",
    "R337": "Evaluación heurística de 4 sitios web (sin usuarios finales)",
    "R391": "Herramienta Simple.Text; evaluación técnica sin n de usuarios reportado",
    "R453": "Ensayo conceptual sobre voz e IA (sin estudio empírico con n)",
    "R504": "Desarrollo de PICTalky; estudio empírico con usuarios no reportado",
    "R623": "Interfaz evaluada en sesiones clínicas (n de estudiantes no unificado)",
    "R643": "Sistema EASIER; evaluación con corpus (sin n de participantes humanos)",
}


def enrich_study(
    doi: str,
    revista: str,
    csv_resumen: str,
    md_text: str | None,
    corpus_id: str = "",
) -> dict[int, tuple[str, str, dict]]:
    text = md_text or ""
    msg = fetch_crossref(doi) or {}
    out: dict[int, tuple[str, str, dict]] = {}

    v8, s8, e8 = editorial_from_crossref(msg, revista)
    out[8] = (v8, s8, e8)

    v9, s9, e9 = pais_from_crossref(msg, text)
    out[9] = (v9, s9, e9)

    v12, s12, e12 = volumen_from_crossref(msg, text)
    out[12] = (v12, s12, e12)

    v13, s13, e13 = muestra_from_text(text, csv_resumen)
    if v13 == "—" and corpus_id in MANUAL_ROW13:
        v13, s13, e13 = MANUAL_ROW13[corpus_id], "article", {"manual": True}
    out[13] = (v13, s13, e13)

    v10, s10, e10 = contexto_from_text(text, csv_resumen, v9)
    out[10] = (v10, s10, e10)

    if corpus_id == "R199" and out[12][0] == "—":
        out[12] = ("Online first (sin volumen en Crossref)", "web", {"doi": doi})

    return out
