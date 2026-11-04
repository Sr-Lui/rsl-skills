#!/usr/bin/env python3
"""Formulario UTP de extracción — skills rsl-resultado-formulario-prepare / -apply.

  formulario.py prepare docs/<slug>
  formulario.py status docs/<slug> [--progress]
  formulario.py lint-setup docs/<slug> [carpeta]
  formulario.py stamp docs/<slug> <YYYY-MM-DD-HHMM>
  formulario.py apply-lote docs/<slug> <NN> [--article corpus_id]
  formulario.py lint-traza docs/<slug> [carpeta]
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
import shutil
import sys
from copy import copy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import picoc_versions as pv  # noqa: E402
from cribado2 import cribado2_dir  # noqa: E402
from rsl_out import Fail, error, ok, run  # noqa: E402

try:
    from openpyxl import load_workbook
    from openpyxl.utils import get_column_letter
except ImportError as e:
    raise SystemExit(
        "ERROR: falta openpyxl. Instala: sudo pacman -S python-openpyxl "
        "o crea .venv-formulario (ver rsl-bootstrap)."
    ) from e

ROOT = Path(__file__).resolve().parent.parent
FORMULARIO_ROOT = "resultados/formulario"
LATEST_FILE = "latest.txt"
TEMPLATE = ROOT / "global/Formulario de extracción de información.xlsx"
FORMULARIO_XLSX = "Formulario.xlsx"
MAP_JSON = "formulario-map.json"
MANIFEST = "manifest.json"
TRAZA_JSONL = "extraccion-traza.jsonl"
COL_OK = "¿Se acepta?"
SHEETS = ("Cuantitativo", "Cualitativo")
FIRST_STUDY_COL = 3
TEMPLATE_STUDY_COUNT = 40
LOTE_SIZE = 10

# fila Excel -> clave CSV (None = dejar vacío en prepare; agente puede completar desde artículo)
BIBLIO_ROWS: dict[int, str | None] = {
    3: "DOI",
    4: "Título",
    5: "Autores",
    6: "Año",
    7: "Revista",
    8: None,
    9: None,
    10: None,
    11: "Tipo de documento",
    12: None,
    13: None,
}

RQ_ITEM_ROWS: dict[str, list[int]] = {
    "RQ1": [17, 18, 19, 20],
    "RQ2": [23, 24, 25, 26],
    "RQ3": [29, 30, 31, 32, 33],
}


def rel(p: Path) -> str:
    p = p.resolve()
    return str(p.relative_to(ROOT) if ROOT in p.parents else p)


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def theme_path(arg: str) -> Path:
    p = Path(arg)
    if not p.is_absolute():
        p = ROOT / p
    if not p.is_dir():
        raise Fail(f"{arg} no es carpeta de tema", "usa docs/<slug>")
    return p


def picoc_context(theme: Path) -> tuple[str, Path]:
    marco, picoc, state = pv.status(theme)
    if state == "FALTA":
        raise Fail("no hay picoc", f"Usa rsl-picoc sobre {rel(theme)}/")
    if state == "DESFASADO":
        raise Fail(f"picoc DESFASADO", f"Usa rsl-picoc sobre {rel(theme)}/")
    assert picoc is not None
    return marco, picoc


def cribado2_csv(picoc: Path) -> Path:
    marco = pv.dir_marco(picoc) or "MARCO"
    path = picoc.parent / f"resultados-{marco}-cribado-2.csv"
    if not path.is_file():
        raise Fail(f"falta {rel(path)}", "Usa rsl-cribado-2-aplicar")
    return path


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def col_ok_key(rows: list[dict[str, str]]) -> str:
    if not rows:
        return COL_OK
    if COL_OK in rows[0]:
        return COL_OK
    for k in rows[0]:
        if "acepta" in k.casefold():
            return k
    return COL_OK


def si_rows(csv_path: Path) -> list[dict[str, str]]:
    rows = read_csv_rows(csv_path)
    key = col_ok_key(rows)
    return [r for r in rows if (r.get(key) or "").strip().upper() == "SI"]


def norm_doi(s: str) -> str:
    s = (s or "").strip().lower()
    for p in ("https://doi.org/", "http://doi.org/"):
        if s.startswith(p):
            s = s[len(p) :]
    return s


def load_documentos(corpus: Path) -> list[dict]:
    path = corpus / "documentos.json"
    if not path.is_file():
        raise Fail(f"falta {rel(path)}", "Usa rsl-cribado-2")
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["registros"]


def match_registro(row: dict[str, str], regs: list[dict]) -> dict | None:
    rid = (row.get("Id") or "").strip()
    doi = norm_doi(row.get("DOI") or "")
    by_id = {r["id"]: r for r in regs if r.get("id")}
    by_doi = {norm_doi(r.get("doi") or ""): r for r in regs if r.get("doi")}
    if rid and rid in by_id:
        return by_id[rid]
    if doi and doi in by_doi:
        return by_doi[doi]
    return None


def items_latest(theme: Path) -> Path:
    latest = theme / "resultados/items/latest.txt"
    if not latest.is_file():
        raise Fail("falta resultados/items/latest.txt", "Usa rsl-resultado-items")
    name = latest.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    folder = theme / "resultados/items" / name
    ij = folder / "items.json"
    if not ij.is_file():
        raise Fail(f"falta {rel(ij)}", "resultado-items:stamp")
    return folder


def formulario_dir(theme: Path) -> Path:
    return theme / FORMULARIO_ROOT


def read_formulario_latest(theme: Path) -> Path | None:
    latest = formulario_dir(theme) / LATEST_FILE
    if not latest.is_file():
        return None
    name = latest.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    folder = formulario_dir(theme) / name
    if (folder / FORMULARIO_XLSX).is_file() and (folder / MAP_JSON).is_file():
        return folder
    return None


def new_timestamp() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d-%H%M")


def copy_cell_style(src, dst) -> None:
    if src.has_style:
        dst.font = copy(src.font)
        dst.border = copy(src.border)
        dst.fill = copy(src.fill)
        dst.number_format = copy(src.number_format)
        dst.protection = copy(src.protection)
        dst.alignment = copy(src.alignment)


def extend_study_columns(ws, n_studies: int) -> None:
    last_tpl_col = FIRST_STUDY_COL + TEMPLATE_STUDY_COUNT - 1
    need_last = FIRST_STUDY_COL + n_studies - 1
    if need_last <= last_tpl_col:
        for i in range(n_studies):
            col = FIRST_STUDY_COL + i
            ws.cell(row=2, column=col, value=float(i + 1))
        return
    for col in range(last_tpl_col + 1, need_last + 1):
        for row in range(1, ws.max_row + 2):
            src = ws.cell(row=row, column=last_tpl_col)
            dst = ws.cell(row=row, column=col)
            copy_cell_style(src, dst)
        ws.cell(row=2, column=col, value=float(col - FIRST_STUDY_COL + 1))
    for i in range(TEMPLATE_STUDY_COUNT):
        col = FIRST_STUDY_COL + i
        ws.cell(row=2, column=col, value=float(i + 1))


def csv_field(row: dict[str, str], key: str) -> str:
    if key in row and (row[key] or "").strip():
        return (row[key] or "").strip()
    for k, v in row.items():
        if k.casefold().startswith(key.casefold()[:5]):
            if (v or "").strip():
                return v.strip()
    return ""


def item_sheets(response_type: str) -> list[str]:
    rt = (response_type or "").strip().lower()
    if rt == "mixto":
        return list(SHEETS)
    if rt == "cuantitativo":
        return ["Cuantitativo"]
    return ["Cualitativo"]


def assign_item_rows(items: list[dict]) -> dict[str, int]:
    """item_id -> excel row."""
    by_rq: dict[str, list[dict]] = {}
    for it in items:
        by_rq.setdefault(it["rq"].upper(), []).append(it)
    out: dict[str, int] = {}
    for rq, rows in RQ_ITEM_ROWS.items():
        pool = by_rq.get(rq, [])
        if len(pool) > len(rows):
            raise Fail(f"demasiados ítems en {rq} ({len(pool)} > {len(rows)})", "revisa items.json")
        for it, row_num in zip(pool, rows):
            out[it["id"]] = row_num
    return out


def build_lotes(studies: list[dict]) -> list[list[dict]]:
    lotes = []
    for i in range(0, len(studies), LOTE_SIZE):
        lotes.append(studies[i : i + LOTE_SIZE])
    return lotes


def cmd_prepare(args: list[str]) -> int:
    if len(args) != 1:
        raise Fail("uso: formulario.py prepare docs/<slug>", None, 2)
    theme = theme_path(args[0])
    marco, picoc = picoc_context(theme)
    csv_path = cribado2_csv(picoc)
    si = si_rows(csv_path)
    n_si = len(si)
    if n_si == 0:
        raise Fail("CSV sin SI", "cribado2:apply")
    items_folder = items_latest(theme)
    items_data = json.loads((items_folder / "items.json").read_text(encoding="utf-8"))
    flat: list[dict] = items_data.get("items") or []
    if not flat:
        raise Fail("items.json sin array items", "rsl-resultado-items")
    item_rows = assign_item_rows(flat)
    corpus = cribado2_dir(theme)
    regs = load_documentos(corpus)

    dest = new_timestamp()
    folder = formulario_dir(theme) / dest
    folder.mkdir(parents=True, exist_ok=True)
    xlsx_path = folder / FORMULARIO_XLSX
    shutil.copy2(TEMPLATE, xlsx_path)

    studies: list[dict] = []
    for idx, row in enumerate(si, start=1):
        reg = match_registro(row, regs)
        corpus_id = reg["id"] if reg else (row.get("Id") or "").strip()
        doi = norm_doi(row.get("DOI") or (reg or {}).get("doi") or "")
        pdf_rel = (reg or {}).get("pdf") or ""
        pdf_path = str(corpus / pdf_rel) if pdf_rel and (corpus / pdf_rel).is_file() else None
        studies.append(
            {
                "study_index": idx,
                "column": get_column_letter(FIRST_STUDY_COL + idx - 1),
                "csv_id": (row.get("Id") or "").strip(),
                "corpus_id": corpus_id,
                "doi": doi,
                "acepta": "SI",
                "extraccion_tier": "full" if pdf_path else "metadata_only",
                "has_pdf": bool(pdf_path),
                "pdf_path": pdf_path,
                "graph_query_id": corpus_id,
                "titulo": csv_field(row, "Título"),
            }
        )

    wb = load_workbook(xlsx_path)
    for sheet_name in SHEETS:
        ws = wb[sheet_name]
        extend_study_columns(ws, n_si)
        for it in flat:
            row_num = item_rows.get(it["id"])
            if row_num and sheet_name in item_sheets(it.get("response_type", "")):
                ws.cell(row=row_num, column=2, value=it.get("summary") or it.get("label") or it["id"])
        for s_idx, study in enumerate(studies):
            col = FIRST_STUDY_COL + s_idx
            row_csv = si[s_idx]
            for excel_row, field in BIBLIO_ROWS.items():
                if field is None:
                    continue
                val = csv_field(row_csv, field)
                if val:
                    ws.cell(row=excel_row, column=col, value=val)
    wb.save(xlsx_path)
    wb.close()

    item_slots = []
    for it in flat:
        row_num = item_rows[it["id"]]
        for sh in item_sheets(it.get("response_type", "")):
            col0 = studies[0]["column"] if studies else "C"
            item_slots.append(
                {
                    "item_id": it["id"],
                    "rq": it["rq"],
                    "picoc_component": it.get("component", ""),
                    "response_type": it.get("response_type", ""),
                    "sheet": sh,
                    "row": row_num,
                }
            )

    lotes_meta = []
    lotes = build_lotes(studies)
    for i, chunk in enumerate(lotes, start=1):
        lotes_meta.append(
            {
                "lote": f"{i:02d}",
                "corpus_ids": [s["corpus_id"] for s in chunk],
                "study_indices": [s["study_index"] for s in chunk],
            }
        )

    map_payload = {
        "version": 1,
        "marco": marco,
        "theme": rel(theme),
        "n_si": n_si,
        "studies": studies,
        "items": item_slots,
        "lotes": lotes_meta,
        "layout": {"biblio_rows": BIBLIO_ROWS, "rq_item_rows": RQ_ITEM_ROWS, "first_study_col": FIRST_STUDY_COL},
    }
    (folder / MAP_JSON).write_text(json.dumps(map_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest = {
        "marco": marco,
        "picoc": rel(picoc),
        "picoc_sha": file_sha(picoc),
        "cribado2_csv": rel(csv_path),
        "cribado2_sha": file_sha(csv_path),
        "items_json": rel(items_folder / "items.json"),
        "items_sha": file_sha(items_folder / "items.json"),
        "n_si": n_si,
        "prepare_stamped": dt.datetime.now().isoformat(timespec="minutes"),
        "folder": dest,
        "extraccion_complete": False,
    }
    (folder / MANIFEST).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return ok(
        f"prepare {rel(folder)} ({n_si} SI, {len(lotes_meta)} lotes)",
        "Usa rsl-resultado-formulario-prepare (biblio CSV→artículo→blanco) y formulario:lint-setup",
    )


def load_map(folder: Path) -> dict:
    path = folder / MAP_JSON
    if not path.is_file():
        raise Fail(f"falta {rel(path)}", "formulario:prepare")
    return json.loads(path.read_text(encoding="utf-8"))


def cmd_lint_setup(args: list[str]) -> int:
    if len(args) not in (1, 2):
        raise Fail("uso: formulario.py lint-setup docs/<slug> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = formulario_dir(theme) / args[1] if len(args) == 2 else read_formulario_latest(theme)
    if folder is None or not folder.is_dir():
        return error("no hay formulario latest", "formulario:prepare")
    mp = load_map(folder)
    n_si = mp["n_si"]
    wb = load_workbook(folder / FORMULARIO_XLSX, read_only=True)
    errs = []
    for sn in SHEETS:
        ws = wb[sn]
        last_col = FIRST_STUDY_COL + n_si - 1
        v = ws.cell(row=2, column=last_col).value
        if v is None or float(v) != float(n_si):
            errs.append(f"E1: {sn} fila 2 col {get_column_letter(last_col)} esperaba {n_si}")
        if ws.cell(row=3, column=FIRST_STUDY_COL).value in (None, ""):
            errs.append(f"W2: {sn} DOI col C vacío (completar biblio)")
    wb.close()
    if len(mp.get("studies") or []) != n_si:
        errs.append("E2: studies en mapa != n_si")
    for e in errs:
        print(e)
    if any(e.startswith("E") for e in errs):
        return error(f"lint-setup {len(errs)} problema(s)", "corrige prepare o Excel")
    return ok(f"lint-setup PASS {rel(folder)}")


def cmd_status(args: list[str]) -> int:
    progress = "--progress" in args
    args = [a for a in args if a != "--progress"]
    if len(args) != 1:
        raise Fail("uso: formulario.py status docs/<slug> [--progress]", None, 2)
    theme = theme_path(args[0])
    folder = read_formulario_latest(theme)
    if folder is None:
        return error("sin formulario", "formulario:prepare")
    manifest_path = folder / MANIFEST
    mp = load_map(folder)
    n_si = mp["n_si"]
    n_items = len({s["item_id"] for s in mp.get("items") or []})
    if progress:
        traza = folder / TRAZA_JSONL
        done = 0
        if traza.is_file():
            done = sum(1 for _ in traza.open(encoding="utf-8") if _.strip())
        total = n_si * n_items
        print(f"progreso ítems: {done}/{total} líneas traza")
    if manifest_path.is_file():
        m = json.loads(manifest_path.read_text(encoding="utf-8"))
        _, picoc = picoc_context(theme)
        csv_path = cribado2_csv(picoc)
        if m.get("cribado2_sha") != file_sha(csv_path):
            return error("DESFASADO (cambió CSV)", "formulario:prepare de nuevo")
    return ok(f"formulario {folder.name} · {n_si} SI")


def cmd_stamp(args: list[str]) -> int:
    if len(args) != 2:
        raise Fail("uso: formulario.py stamp docs/<slug> <carpeta>", None, 2)
    theme = theme_path(args[0])
    folder = formulario_dir(theme) / args[1].strip()
    if not (folder / FORMULARIO_XLSX).is_file():
        raise Fail(f"no existe {rel(folder)}", "formulario:prepare")
    code = cmd_lint_setup([args[0], args[1].strip()])
    if code != 0:
        return error("stamp abortado", "lint-setup")
    formulario_dir(theme).mkdir(parents=True, exist_ok=True)
    (formulario_dir(theme) / LATEST_FILE).write_text(args[1].strip() + "\n", encoding="utf-8")
    try:
        from rsl_pipeline_manifest import sync_pipeline

        sync_pipeline(theme, formulario_latest=rel(folder))
    except ValueError:
        pass
    return ok(f"latest → {FORMULARIO_ROOT}/{args[1].strip()}", "rsl-resultado-formulario-apply lote 01")


def _slot_key(corpus_id: str, item_id: str, sheet: str) -> tuple[str, str, str]:
    return (corpus_id, item_id, sheet)


def cmd_apply_lote(args: list[str]) -> int:
    if len(args) < 2:
        raise Fail("uso: formulario.py apply-lote docs/<slug> <NN> [--article id]", None, 2)
    theme = theme_path(args[0])
    lote_id = args[1].strip().zfill(2)
    article_filter = None
    if "--article" in args:
        i = args.index("--article")
        if i + 1 < len(args):
            article_filter = args[i + 1].strip()
    folder = read_formulario_latest(theme)
    if folder is None:
        return error("sin formulario latest", "formulario:stamp tras prepare")
    mp = load_map(folder)
    lote = next((L for L in mp.get("lotes") or [] if L["lote"] == lote_id), None)
    if lote is None:
        raise Fail(f"lote {lote_id} no está en mapa", "revisa formulario-map.json")
    corpus_ids = lote["corpus_ids"]
    if article_filter:
        corpus_ids = [c for c in corpus_ids if c == article_filter]
        if not corpus_ids:
            raise Fail(f"{article_filter} no está en lote {lote_id}", None)

    wb = load_workbook(folder / FORMULARIO_XLSX)
    traza_path = folder / TRAZA_JSONL
    existing = set()
    if traza_path.is_file():
        for line in traza_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            o = json.loads(line)
            existing.add(_slot_key(o["article_id"], o["item_id"], o["sheet"]))

    studies_by_id = {s["corpus_id"]: s for s in mp["studies"]}
    items_by_id = {}
    for slot in mp.get("items") or []:
        items_by_id.setdefault(slot["item_id"], slot)

    applied = 0
    for cid in corpus_ids:
        payload_path = folder / "debate" / f"lote-{lote_id}" / f"apply-{cid}.json"
        if not payload_path.is_file():
            print(f"WARN falta {rel(payload_path)}")
            continue
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
        study = studies_by_id.get(cid)
        if not study:
            print(f"WARN corpus {cid} no en mapa")
            continue
        col_letter = study["column"]
        col_idx = FIRST_STUDY_COL + study["study_index"] - 1
        for slot in payload.get("slots") or []:
            item_id = slot["item_id"]
            meta = items_by_id.get(item_id)
            if not meta:
                continue
            sh = meta["sheet"]
            row = meta["row"]
            key = _slot_key(cid, item_id, sh)
            if key in existing:
                continue
            ws = wb[sh]
            val = slot.get("value")
            if val is not None and str(val).strip():
                ws.cell(row=row, column=col_idx, value=val)
            cell_ref = f"{col_letter}{row}"
            rec = {
                "article_id": cid,
                "item_id": item_id,
                "rq": meta.get("rq"),
                "picoc_component": meta.get("picoc_component"),
                "sheet": sh,
                "cell": cell_ref,
                "value": val if val is not None else "",
                "decision": slot.get("decision", "absent"),
                "evidence": slot.get("evidence") or [],
                "lote": lote_id,
            }
            with traza_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            existing.add(key)
            applied += 1
    wb.save(folder / FORMULARIO_XLSX)
    wb.close()
    return ok(f"apply-lote {lote_id}: {applied} slot(s)", "lint-traza o siguiente artículo")


def cmd_lint_traza(args: list[str]) -> int:
    if len(args) not in (1, 2):
        raise Fail("uso: formulario.py lint-traza docs/<slug> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = formulario_dir(theme) / args[1] if len(args) == 2 else read_formulario_latest(theme)
    if folder is None:
        return error("sin formulario", "prepare")
    mp = load_map(folder)
    traza_path = folder / TRAZA_JSONL
    if not traza_path.is_file():
        return error("falta extraccion-traza.jsonl", "apply-lote")
    lines = [json.loads(l) for l in traza_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    errs = []
    for rec in lines:
        dec = rec.get("decision")
        val = (rec.get("value") or "").strip()
        if dec in ("extracted", "partial") and not val:
            errs.append(f"E3: {rec.get('cell')} decision={dec} sin valor")
        if val and dec not in ("extracted", "partial", "omitted"):
            if dec != "absent" or val:
                errs.append(f"E4: {rec.get('cell')} valor sin decision válida")
    if errs:
        for e in errs[:20]:
            print(e)
        return error(f"lint-traza {len(errs)} FAIL", "corrige traza o Excel")
    return ok(f"lint-traza PASS ({len(lines)} líneas)")


def dispatch(args: list[str]) -> int:
    if not args:
        print(__doc__)
        return error("falta subcomando", "prepare | status | lint-setup | stamp | apply-lote | lint-traza", code=2)
    cmd, rest = args[0], args[1:]
    handlers = {
        "prepare": cmd_prepare,
        "status": cmd_status,
        "lint-setup": cmd_lint_setup,
        "stamp": cmd_stamp,
        "apply-lote": cmd_apply_lote,
        "lint-traza": cmd_lint_traza,
    }
    fn = handlers.get(cmd)
    if not fn:
        return error(f"subcomando {cmd} desconocido", "prepare | status | lint-setup | stamp | apply-lote | lint-traza", code=2)
    return fn(rest)


def cli(args: list[str]) -> int:
    try:
        return dispatch(args)
    except pv.MarcoError as e:
        raise Fail(str(e), e.fix)


if __name__ == "__main__":
    run(cli)
