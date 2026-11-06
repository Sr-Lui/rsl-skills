"""Placement por naturaleza del estudio (map v2) — sin campo en Excel."""
from __future__ import annotations

from typing import Callable

try:
    from openpyxl.utils import column_index_from_string, get_column_letter
except ImportError:
    column_index_from_string = None  # type: ignore
    get_column_letter = None  # type: ignore

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
    idx = study.get("study_index") or study.get("si_order")
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
    col = pc.get("column")
    if col and column_index_from_string:
        return column_index_from_string(col)
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


def studies_on_sheet(studies: list[dict], sheet: str) -> list[dict]:
    out: list[dict] = []
    for s in studies:
        nature = (s.get("study_nature") or "").strip().lower()
        if nature not in VALID_NATURE:
            continue
        if sheet not in study_sheets(nature):
            continue
        out.append(s)
    out.sort(key=lambda x: int(x.get("si_order") or 0))
    return out


def assign_placements(studies: list[dict], first_study_col: int = 3) -> None:
    """Cabecera fila 2 = si_order global; columnas físicas compactas por hoja."""
    if get_column_letter is None:
        raise RuntimeError("openpyxl required for assign_placements")
    for study in studies:
        study["placement"] = {"Cuantitativo": None, "Cualitativo": None}
    for sheet in SHEETS:
        on_sheet = studies_on_sheet(studies, sheet)
        for i, study in enumerate(on_sheet, start=1):
            si = int(study["si_order"])
            study["placement"][sheet] = {
                "study_index": si,
                "column": get_column_letter(first_study_col + i - 1),
            }


def extend_physical_columns(
    ws,
    n_studies: int,
    first_study_col: int,
    template_study_count: int,
    copy_cell_style: Callable,
) -> None:
    """Amplía columnas de estudio (estilos); no escribe fila 2."""
    if n_studies <= 0:
        return
    last_tpl_col = first_study_col + template_study_count - 1
    need_last = first_study_col + n_studies - 1
    if need_last <= last_tpl_col:
        return
    for col in range(last_tpl_col + 1, need_last + 1):
        for row in range(1, ws.max_row + 2):
            src = ws.cell(row=row, column=last_tpl_col)
            dst = ws.cell(row=row, column=col)
            copy_cell_style(src, dst)


def sync_numbered_headers(
    wb,
    mp: dict,
    first_study_col: int = 3,
    template_study_count: int = 40,
    copy_cell_style: Callable | None = None,
) -> None:
    """Fila 2: número global si_order por columna compacta en cada hoja."""
    studies = mp.get("studies") or []
    for sheet in SHEETS:
        ws = wb[sheet]
        on_sheet = studies_on_sheet(studies, sheet)
        n = len(on_sheet)
        if copy_cell_style is not None:
            extend_physical_columns(ws, n, first_study_col, template_study_count, copy_cell_style)
        clear_to = first_study_col + max(n, template_study_count) - 1
        for col in range(first_study_col, clear_to + 1):
            ws.cell(row=2, column=col, value=None)
        for i, study in enumerate(on_sheet, start=1):
            col = first_study_col + i - 1
            ws.cell(row=2, column=col, value=float(study["si_order"]))


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


def lint_header_placement(studies: list[dict], sheet: str, first_study_col: int = 3) -> list[str]:
    """Errores E1/E8 para lint-setup."""
    errs: list[str] = []
    if get_column_letter is None:
        return errs
    on_sheet = studies_on_sheet(studies, sheet)
    for i, study in enumerate(on_sheet, start=1):
        pc = placement_cell(study, sheet)
        if not pc:
            errs.append(f"E8: {study.get('corpus_id')} sin placement en {sheet}")
            continue
        si = int(study.get("si_order") or 0)
        if int(pc["study_index"]) != si:
            errs.append(
                f"E8: {study.get('corpus_id')} study_index {pc['study_index']} != si_order {si}"
            )
        expected_col = get_column_letter(first_study_col + i - 1)
        if pc.get("column") != expected_col:
            errs.append(
                f"E8: {study.get('corpus_id')} col {pc.get('column')} esperaba {expected_col} en {sheet}"
            )
    return errs


def _self_test_assign_placements() -> None:
    studies = [
        {"si_order": 1, "corpus_id": "a", "study_nature": "cuantitativo"},
        {"si_order": 2, "corpus_id": "b", "study_nature": "cualitativo"},
        {"si_order": 3, "corpus_id": "c", "study_nature": "mixto"},
        {"si_order": 4, "corpus_id": "d", "study_nature": "cuantitativo"},
        {"si_order": 5, "corpus_id": "e", "study_nature": "mixto"},
    ]
    assign_placements(studies, first_study_col=3)
    assert studies[0]["placement"]["Cuantitativo"]["study_index"] == 1
    assert studies[0]["placement"]["Cuantitativo"]["column"] == "C"
    assert studies[0]["placement"]["Cualitativo"] is None
    assert studies[1]["placement"]["Cualitativo"]["study_index"] == 2
    assert studies[1]["placement"]["Cualitativo"]["column"] == "C"
    assert studies[2]["placement"]["Cuantitativo"]["study_index"] == 3
    assert studies[2]["placement"]["Cualitativo"]["study_index"] == 3
    assert studies[2]["placement"]["Cuantitativo"]["column"] == "D"
    assert studies[2]["placement"]["Cualitativo"]["column"] == "D"
    cuant = studies_on_sheet(studies, "Cuantitativo")
    assert [s["corpus_id"] for s in cuant] == ["a", "c", "d", "e"]
    assert [s["placement"]["Cuantitativo"]["study_index"] for s in cuant] == [1, 3, 4, 5]
    cual = studies_on_sheet(studies, "Cualitativo")
    assert [s["corpus_id"] for s in cual] == ["b", "c", "e"]
    assert [s["placement"]["Cualitativo"]["study_index"] for s in cual] == [2, 3, 5]


if __name__ == "__main__":
    _self_test_assign_placements()
    print("formulario_placement: self-test OK")
