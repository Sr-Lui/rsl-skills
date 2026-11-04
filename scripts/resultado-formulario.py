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


def md_for_corpus(corpus: Path, corpus_id: str) -> Path | None:
    md_dir = corpus / "docs" / "md"
    hits = list(md_dir.glob(f"{corpus_id}-*.md"))
    return hits[0] if hits else None


def _ev(md: Path, quote: str) -> list[dict]:
    q = " ".join(quote.split())[:160]
    return [{"src": rel(md), "loc": "fulltext", "quote": q}] if q else []


def _absent() -> tuple[str, str, list]:
    return "", "absent", []


def _hit(text: str, pattern: str) -> re.Match | None:
    return re.search(pattern, text, re.I | re.M)


def extract_item(item_id: str, text: str, tl: str, md: Path) -> tuple[str, str, list]:
    """Conservative full-text extraction; empty value + absent if no anchor."""
    if item_id == "RQ1-I1":
        terms = []
        for pat, label in (
            (r"learning disabilities?", "learning disabilities"),
            (r"cognitive impairments?", "cognitive impairment"),
            (r"\bADHD\b", "ADHD"),
            (r"\bautism\b|\bautistic\b|\bASD\b|\bTEA\b", "autism/ASD"),
            (r"dyslexia", "dyslexia"),
            (r"intellectual disabilit", "intellectual disability"),
            (r"neurodiver", "neurodivergence"),
            (r"Down syndrome", "Down syndrome"),
        ):
            if re.search(pat, tl):
                terms.append(label)
        if terms:
            return "; ".join(dict.fromkeys(terms)), "extracted", _ev(md, terms[0])
        return _absent()
    if item_id == "RQ1-I2":
        if re.search(r"stratif|subgroup|sub-group|by diagnosis|per profile", tl):
            return "Sí", "extracted", _ev(md, "stratification/subgroup")
        if re.search(r"participants|sample|subjects", tl):
            return "No", "extracted", _ev(md, "no stratification mention")
        return _absent()
    if item_id == "RQ1-I3":
        pres = "Sí" if re.search(r"user study|participants|involved users|co-design|with users", tl) else "NR"
        n = "NR"
        m = re.search(r"\b[Nn]\s*[=:]\s*(\d+)|(\d+)\s+participants", text)
        if m:
            n = (m.group(1) or m.group(2) or "NR").strip()
        rol = "NR"
        if re.search(r"co-design| participatory|design workshop", tl):
            rol = "diseño"
        elif re.search(r"user (study|evaluation|test)", tl):
            rol = "evaluación"
        if pres == "NR" and n == "NR" and rol == "NR":
            return _absent()
        v = f"Presencia: {pres} | N: {n} | Rol: {rol}"
        return v, "partial" if "NR" in v else "extracted", _ev(md, v[:80])
    if item_id == "RQ1-I4":
        pais = "NR"
        m = re.search(r"\b(United States|USA|U\.S\.|China|Spain|India|UK|Canada|Germany|Alabama)\b", text)
        if m:
            pais = m.group(1)
        enf = "NR"
        if re.search(r"strength-based|neurodiversity", tl):
            enf = "diferencia"
        elif re.search(r"deficit|impairment model", tl):
            enf = "déficit"
        cons = "NR"
        if re.search(r"IRB|ethics committee|informed consent|consent form", tl):
            cons = "informado"
        v = f"Enfoque: {enf} | Perfil: NR | Consentimiento: {cons} | País: {pais}"
        if v.count("NR") >= 3:
            return _absent()
        return v, "partial", _ev(md, pais)
    if item_id == "RQ2-I1":
        fam = []
        mod = "NR"
        if re.search(r"\bLLM\b|large language model|GPT-4|Claude|Llama", tl):
            fam.append("LLM")
        if re.search(r"\bNLP\b|natural language", tl):
            fam.append("NLP")
        if re.search(r"deep learning|neural network", tl):
            fam.append("DL")
        if re.search(r"machine learning|\bML\b", tl):
            fam.append("ML")
        if re.search(r"generative AI|GenAI", tl):
            fam.append("GenAI")
        mm = re.search(r"(GPT-4[o]?|Claude[-\w]*|Llama[-\.\d\w]*)", text)
        if mm:
            mod = mm.group(1)
        if not fam:
            return _absent()
        return f"{'; '.join(fam)}; Modelo: {mod}", "extracted", _ev(md, fam[0])
    if item_id == "RQ2-I2":
        roles = []
        for pat, lab in (
            (r"generat(e|ing|or)|produce output", "Generador"),
            (r"evaluat(e|ing|or)|assess", "Evaluador"),
            (r"quality assurance|QA assistant", "Asistente de aseguramiento de la calidad"),
        ):
            if re.search(pat, tl):
                roles.append(lab)
        if roles:
            return "; ".join(dict.fromkeys(roles)), "extracted", _ev(md, roles[0])
        if re.search(r"\bAI\b|artificial intelligence|model", tl):
            return "otro", "partial", _ev(md, "AI applied")
        return _absent()
    if item_id == "RQ2-I3":
        for lab, pat in (
            ("pruebas", r"\btest(ing|s)?\b|experiment|empirical study|user study"),
            ("desarrollo", r"implement(ed|ation|ing)?|develop(ed|ment)?"),
            ("diseño", r"\bdesign\b|prototype|UI/UX"),
            ("requisitos", r"requirement"),
            ("V&V", r"validation|verification"),
        ):
            if re.search(pat, tl):
                return lab, "extracted", _ev(md, lab)
        return _absent()
    if item_id == "RQ2-I4":
        phases = []
        primary = None
        for lab, pat in (
            ("pruebas", r"\btest(ing|s)?\b|experiment"),
            ("desarrollo", r"implement|develop"),
            ("diseño", r"\bdesign\b"),
        ):
            if re.search(pat, tl):
                phases.append(lab)
        if len(phases) <= 1:
            return "—", "extracted", _ev(md, "single phase")
        return "; ".join(phases[1:]) if len(phases) > 1 else "—", "extracted", _ev(md, ";".join(phases))
    if item_id == "RQ3-I1":
        m = re.search(
            r"(Flesch|accuracy|precision|recall|F1|SUS|completion rate|reading ease)[^\n]{0,40}(\d+\.?\d*)",
            text,
            re.I,
        )
        if m:
            v = f"Constructo: {m.group(1)} | Valor: {m.group(2)}"
            return v, "extracted", _ev(md, m.group(0)[:80])
        if re.search(r"metric|measure|score|performance", tl):
            return "Constructo: NR | Valor: NR", "partial", _ev(md, "metrics mentioned")
        return _absent()
    if item_id == "RQ3-I2":
        inst = []
        for pat, lab in (
            (r"questionnaire|survey", "Cuestionario"),
            (r"heuristic evaluation", "Heurística"),
            (r"user study|think aloud", "Estudio con usuarios"),
            (r"Flesch|readability", "Legibilidad"),
        ):
            if re.search(pat, tl):
                inst.append(lab)
        if inst:
            return "; ".join(dict.fromkeys(inst)), "extracted", _ev(md, inst[0])
        return _absent()
    if item_id == "RQ3-I3":
        if re.search(r"\bWCAG\b", tl):
            return "WCAG", "extracted", _ev(md, "WCAG")
        if re.search(r"\bCOGA\b|cognitive accessibility", tl):
            return "COGA", "extracted", _ev(md, "COGA/cognitive accessibility")
        if re.search(r"accessibility standard|accessibility guideline", tl):
            return "otro", "partial", _ev(md, "accessibility guidelines")
        if re.search(r"accessib", tl):
            return "ninguno", "extracted", _ev(md, "accessibility without named standard")
        return _absent()
    if item_id == "RQ3-I4":
        cog = bool(re.search(r"cognitive|dyslexia|ADHD|autism|learning disabilit|readability", tl))
        sen = bool(re.search(r"visual|blind|hearing|sensor", tl))
        if cog and sen:
            return "ambas", "extracted", _ev(md, "cognitive and sensory")
        if cog:
            return "Cognitiva", "extracted", _ev(md, "cognitive")
        if sen:
            return "sensorial", "extracted", _ev(md, "sensory")
        return _absent()
    if item_id == "RQ3-I5":
        if re.search(r"automated (test|evaluation)|continuous integration|\bCI\b pipeline", tl):
            return "Integración continua", "extracted", _ev(md, "automated")
        if re.search(r"semi-?automatic|human-in-the-loop", tl):
            return "semiautomática", "extracted", _ev(md, "semi-automatic")
        if re.search(r"user study|participants|usability test", tl):
            return "solo validación con usuarios", "extracted", _ev(md, "user validation")
        return _absent()
    return _absent()


def extract_slots_for_study(corpus: Path, corpus_id: str, item_defs: list[dict]) -> list[dict]:
    md = md_for_corpus(corpus, corpus_id)
    if md is None:
        return [{"item_id": it["id"], "value": "", "decision": "absent", "evidence": []} for it in item_defs]
    text = md.read_text(encoding="utf-8", errors="replace")
    tl = text.lower()
    out = []
    for it in item_defs:
        val, dec, ev = extract_item(it["id"], text, tl, md)
        out.append({"item_id": it["id"], "value": val, "decision": dec, "evidence": ev})
    return out


def cmd_extract_lote(args: list[str]) -> int:
    if len(args) < 2:
        raise Fail("uso: formulario.py extract-lote docs/<slug> <NN>|all", None, 2)
    theme = theme_path(args[0])
    folder = read_formulario_latest(theme)
    if folder is None:
        return error("sin formulario latest", "formulario:prepare")
    mp = load_map(folder)
    corpus = cribado2_dir(theme)
    items_folder = items_latest(theme)
    item_defs = json.loads((items_folder / "items.json").read_text(encoding="utf-8"))["items"]
    target = args[1].strip().lower()
    lotes = mp.get("lotes") or []
    if target == "all":
        chosen = lotes
    else:
        lid = target.zfill(2)
        chosen = [L for L in lotes if L["lote"] == lid]
        if not chosen:
            raise Fail(f"lote {lid} no encontrado", None)
    written = 0
    for lot in chosen:
        lid = lot["lote"]
        deb_dir = folder / "debate" / f"lote-{lid}"
        deb_dir.mkdir(parents=True, exist_ok=True)
        for cid in lot["corpus_ids"]:
            slots = extract_slots_for_study(corpus, cid, item_defs)
            payload = {"article_id": cid, "lote": lid, "slots": slots, "source": "md-extract-v1"}
            (deb_dir / f"apply-{cid}.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
            written += 1
    return ok(f"extract-lote: {written} apply-*.json en {len(chosen)} lote(s)", "formulario:apply-lote")


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
    item_metas: dict[str, list[dict]] = {}
    for slot in mp.get("items") or []:
        item_metas.setdefault(slot["item_id"], []).append(slot)

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
            metas = item_metas.get(item_id) or []
            if not metas:
                continue
            val = slot.get("value")
            dec = slot.get("decision", "absent")
            for meta in metas:
                sh = meta["sheet"]
                row = meta["row"]
                key = _slot_key(cid, item_id, sh)
                if key in existing:
                    continue
                ws = wb[sh]
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
                    "decision": dec,
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
        if val and dec not in ("extracted", "partial", "omitted", "absent"):
            errs.append(f"E4: {rec.get('cell')} valor sin decision válida")
    if errs:
        for e in errs[:20]:
            print(e)
        return error(f"lint-traza {len(errs)} FAIL", "corrige traza o Excel")
    return ok(f"lint-traza PASS ({len(lines)} líneas)")


def dispatch(args: list[str]) -> int:
    if not args:
        print(__doc__)
        return error("falta subcomando", "prepare | extract-lote | apply-lote | lint-traza | …", code=2)
    cmd, rest = args[0], args[1:]
    handlers = {
        "prepare": cmd_prepare,
        "status": cmd_status,
        "lint-setup": cmd_lint_setup,
        "stamp": cmd_stamp,
        "extract-lote": cmd_extract_lote,
        "apply-lote": cmd_apply_lote,
        "lint-traza": cmd_lint_traza,
    }
    fn = handlers.get(cmd)
    if not fn:
        return error(f"subcomando {cmd} desconocido", "prepare | extract-lote | apply-lote | lint-traza", code=2)
    return fn(rest)


def cli(args: list[str]) -> int:
    try:
        return dispatch(args)
    except pv.MarcoError as e:
        raise Fail(str(e), e.fix)


if __name__ == "__main__":
    run(cli)
