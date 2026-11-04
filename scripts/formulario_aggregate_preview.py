"""Tablas de frecuencia desde extraccion-traza.jsonl (validación pre-síntesis)."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

PHASE_CATS = (
    "Requisitos",
    "Diseño",
    "Desarrollo",
    "Personalización en ejecución",
    "Pruebas",
    "V&V",
    "Auditoría",
    "Otro",
    "NR",
)


def parse_rq1_i2(val: str) -> str | None:
    if re.match(r"^Sí\b", val, re.I):
        return "Sí"
    if re.match(r"^No\b", val, re.I):
        return "No"
    if re.match(r"^NR\b", val, re.I):
        return "NR"
    return None


def parse_rq2_i3(val: str) -> str | None:
    for c in PHASE_CATS:
        if val.startswith(c + ".") or val.startswith(c + " "):
            return c
        if re.match(rf"^{re.escape(c)}\.", val, re.I):
            return c
    for c in PHASE_CATS:
        if re.search(rf"\b{re.escape(c)}\b", val, re.I):
            return c
    return val.split(".", 1)[0].strip()[:40] if val else None


def parse_rq3_i4(val: str) -> str | None:
    head = val.split(".", 1)[0]
    for k in ("Ambas", "Cognitiva", "Sensorial", "NR"):
        if k.lower() in head.lower():
            return k
    return None


def parse_rq3_i5(val: str) -> str | None:
    for k in (
        "Integración continua",
        "Semiautomática",
        "Solo validación con usuarios",
        "NR",
    ):
        if k in val:
            return k
    return None


PARSERS: dict[str, callable] = {
    "RQ1-I2": parse_rq1_i2,
    "RQ2-I3": parse_rq2_i3,
    "RQ3-I4": parse_rq3_i4,
    "RQ3-I5": parse_rq3_i5,
}


def build_preview(traza_path: Path, n_studies: int) -> str:
    lines = []
    by_item: dict[str, list[str]] = {}
    for raw in traza_path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        rec = json.loads(raw)
        if rec.get("decision") == "absent" or (rec.get("value") or "").strip() in ("", "—"):
            continue
        by_item.setdefault(rec["item_id"], []).append(rec["value"])

    lines.append("# Aggregate preview (extraccion-traza)\n")
    lines.append(f"Estudios SI en mapa: **{n_studies}**. Líneas traza analizadas por ítem.\n")

    for item_id, parser in PARSERS.items():
        vals = by_item.get(item_id, [])
        if not vals:
            lines.append(f"## {item_id}\n\n(sin datos en traza)\n")
            continue
        c = Counter()
        for v in vals:
            key = parser(v)
            c[key or "?"] += 1
        lines.append(f"## {item_id} (n={len(vals)})\n")
        lines.append("| Categoría | n | % |")
        lines.append("|-----------|---:|---:|")
        for cat, n in c.most_common():
            pct = 100.0 * n / len(vals)
            lines.append(f"| {cat} | {n} | {pct:.1f} |")
        lines.append("")
        if item_id == "RQ2-I3" and vals:
            top = c.most_common(1)[0]
            if top[1] / len(vals) > 0.8:
                lines.append(
                    f"> **WARN:** {top[0]} concentra {100*top[1]/len(vals):.0f} % — revisar calidad de extracción.\n"
                )

    dec = Counter()
    total = 0
    for raw in traza_path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        rec = json.loads(raw)
        dec[rec.get("decision", "?")] += 1
        total += 1
    lines.append("## Decisiones (todas las líneas traza)\n")
    lines.append(f"Total líneas: {total}\n")
    for k, n in dec.most_common():
        lines.append(f"- {k}: {n}")
    lines.append("")
    return "\n".join(lines)
