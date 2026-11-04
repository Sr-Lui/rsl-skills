"""Placement por naturaleza del estudio (map v2) — sin campo en Excel."""
from __future__ import annotations

SHEETS = ("Cuantitativo", "Cualitativo")
VALID_NATURE = frozenset({"cuantitativo", "cualitativo", "mixto"})


def study_sheets(nature: str) -> list[str]:
    n = (nature or "").strip().lower()
    if n == "mixto":
        return list(SHEETS)
    if n == "cuantitativo":
        return ["Cuantitativo"]
    if n == "cualitativo":
        return ["Cualitativo"]
    return []


def ensure_placement(study: dict) -> dict:
    """Normaliza estudio map v1 → v2-like placement."""
    if study.get("placement") is not None:
        return study
    pl: dict = {"Cuantitativo": None, "Cualitativo": None}
    idx = study.get("study_index")
    col = study.get("column")
    if idx and col:
        for sh in SHEETS:
            pl[sh] = {"study_index": idx, "column": col}
        if not study.get("study_nature"):
            study["study_nature"] = "mixto"
    study["placement"] = pl
    return study


def placement_cell(study: dict, sheet: str) -> dict | None:
    pl = study.get("placement") or {}
    cell = pl.get(sheet)
    return cell if cell else None


def column_index(study: dict, sheet: str, first_study_col: int) -> int | None:
    pc = placement_cell(study, sheet)
    if not pc:
        return None
    return first_study_col + int(pc["study_index"]) - 1


def column_letter(study: dict, sheet: str) -> str | None:
    pc = placement_cell(study, sheet)
    return pc.get("column") if pc else None


def sheets_for_study(study: dict) -> list[str]:
    nature = (study.get("study_nature") or "").strip().lower()
    if nature in VALID_NATURE:
        return study_sheets(nature)
    pl = study.get("placement") or {}
    return [sh for sh in SHEETS if pl.get(sh)]


def expected_traza_slots(mp: dict) -> int:
    item_metas: dict[str, list] = {}
    for slot in mp.get("items") or []:
        item_metas.setdefault(slot["item_id"], []).append(slot)
    total = 0
    for study in mp.get("studies") or []:
        for sh in sheets_for_study(study):
            if not placement_cell(study, sh):
                continue
            for metas in item_metas.values():
                for meta in metas:
                    if meta["sheet"] == sh:
                        total += 1
    return total


def count_by_sheet(mp: dict) -> dict[str, int]:
    out = {sh: 0 for sh in SHEETS}
    for s in mp.get("studies") or []:
        for sh in SHEETS:
            if placement_cell(s, sh):
                out[sh] += 1
    return out
