"""Clasificación cuantitativo / cualitativo / mixto desde MD + CSV (solo mapa, no Excel)."""
from __future__ import annotations

import json
import re
from pathlib import Path

VALID = frozenset({"cuantitativo", "cualitativo", "mixto"})

QUANT_PATS = (
    r"\bexperiment\b",
    r"factorial design",
    r"randomized",
    r"controlled trial",
    r"\bp\s*[<>=]\s*0\.",
    r"statistical(ly)? significant",
    r"cohen['']s d",
    r"effect size",
    r"ηp2|eta-squared",
    r"\bANOVA\b",
    r"regression model",
    r"accuracy of \d",
    r"\bF1[- ]score",
    r"precision.*recall",
    r"quasi-experimental",
    r"pre-?post test",
    r"A/B test",
)
QUAL_PATS = (
    r"thematic analysis",
    r"grounded theory",
    r"ethnograph",
    r"semi-structured interview",
    r"focus group",
    r"conversation analysis",
    r"qualitative (study|design|analysis|research)",
    r"participatory design",
    r"co-design",
    r"think aloud",
    r"case study approach",
    r"phenomenolog",
    r"narrative analysis",
    r"reflexive thematic",
)
MIXED_PATS = (
    r"mixed-?methods",
    r"mixed methods",
    r"quantitative and qualitative",
    r"qualitative and quantitative",
    r"triangulation",
)


def score_patterns(blob: str, patterns: tuple[str, ...]) -> int:
    n = 0
    for pat in patterns:
        if re.search(pat, blob, re.I):
            n += 1
    return n


def classify_from_text(text: str, resumen: str) -> tuple[str, bool, dict]:
    blob = f"{resumen}\n{text[:80000]}"
    sq = score_patterns(blob, QUANT_PATS)
    sl = score_patterns(blob, QUAL_PATS)
    sm = score_patterns(blob, MIXED_PATS)
    if sm >= 1 or (sq >= 2 and sl >= 2):
        return "mixto", False, {"quant_signals": sq, "qual_signals": sl, "mixed_signals": sm}
    if sq >= 2 and sl <= 1:
        return "cuantitativo", sl == 1, {"quant_signals": sq, "qual_signals": sl}
    if sl >= 2 and sq <= 1:
        return "cualitativo", sq == 1, {"quant_signals": sq, "qual_signals": sl}
    if sq >= 1 and sl == 0:
        return "cuantitativo", True, {"quant_signals": sq, "qual_signals": sl}
    if sl >= 1 and sq == 0:
        return "cualitativo", True, {"quant_signals": sq, "qual_signals": sl}
    if re.search(r"user study|usability (test|evaluation)|survey", blob, re.I) and sq >= 1:
        return "cuantitativo", True, {"reason": "user_study_metrics"}
    if re.search(r"design (study|research)|framework|conceptual", blob, re.I) and sq == 0 and sl == 0:
        return "cualitativo", True, {"reason": "design_qualitative_default"}
    return "mixto", True, {"quant_signals": sq, "qual_signals": sl, "reason": "ambiguous_default_mixto"}


def load_overrides(folder: Path) -> dict[str, str]:
    path = folder / "nature-overrides.json"
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    out = {}
    for k, v in data.items():
        if k.startswith("_"):
            continue
        vv = str(v).strip().lower()
        if vv in VALID:
            out[k.strip()] = vv
    return out
