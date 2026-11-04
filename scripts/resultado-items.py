#!/usr/bin/env python3
"""Ítems de extracción por RQ (post cribado 2) — skill rsl-resultado-items.

Uso:
  resultado-items.py prepare docs/<slug>
  resultado-items.py lint docs/<slug> [resultados/items/<carpeta>/items.md]
  resultado-items.py status docs/<slug>
  resultado-items.py stamp docs/<slug> <carpeta-timestamp>
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import picoc_versions as pv  # noqa: E402
from rsl_out import Fail, error, ok, run  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ITEMS_ROOT = "resultados/items"
LATEST_FILE = "latest.txt"
ITEMS_MD = "items.md"
MANIFEST = "manifest.json"
ITEMS_JSON = "items.json"
COL_OK = "¿Se acepta?"
MAX_ITEMS = 5
MIN_ITEMS = 1
ITEM_ID_RE = re.compile(r"^RQ(\d+)-I(\d+)$", re.I)
DATA_TYPES = frozenset({"categórico", "nominal", "numérico", "texto", "mixto"})
DEBATE_MD = "items-debate.md"
DEBATE_SKELETON = """# Debate — ítems de extracción

## Ronda 1 — Defensor

(pendiente)

## Ronda 1 — Crítico

(pendiente)

## Ronda 1 — Decisiones

| RQ | Id | Decisión | Notas |
|----|-----|----------|-------|

## Ronda 2 — Defensor

(solo si quedó pendiente)

## Ronda 2 — Crítico

(solo si quedó pendiente)

## Ronda 2 — Decisiones

| RQ | Id | Decisión | Notas |
|----|-----|----------|-------|
"""


def rel(p: Path) -> str:
    p = p.resolve()
    return str(p.relative_to(ROOT) if ROOT in p.parents else p)


def sections(text: str, level: str = "##") -> dict[str, str]:
    parts = re.split(rf"^{level}\s+(.+)$", text, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def find(secs: dict[str, str], prefix: str) -> str | None:
    p = prefix.casefold()
    return next((v for k, v in secs.items() if k.casefold().startswith(p)), None)


def table(body: str) -> list[dict[str, str]]:
    rows = [l.strip() for l in body.splitlines() if l.strip().startswith("|")]
    if len(rows) < 2:
        return []

    def cells(line: str) -> list[str]:
        return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]

    head = cells(rows[0])
    return [dict(zip(head, cells(r))) for r in rows[2:]]


def col(row: dict[str, str], prefix: str) -> str:
    p = prefix.casefold()
    return next((v for k, v in row.items() if k.casefold().startswith(p)), "")


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def theme_path(arg: str) -> Path:
    p = Path(arg)
    if not p.is_absolute():
        p = ROOT / p
    if not p.is_dir():
        raise Fail(f"{arg} no es la carpeta de un tema", "usa docs/<slug>")
    return p


def picoc_context(theme: Path) -> tuple[str, Path, str]:
    marco, picoc, state = pv.status(theme)
    if state == "FALTA":
        raise Fail("no hay picoc", f"Usa rsl-picoc sobre {rel(theme)}/")
    if state == "DESFASADO":
        raise Fail(f"picoc DESFASADO (config pide {marco})", f"Usa rsl-picoc sobre {rel(theme)}/")
    assert picoc is not None
    return marco, picoc, state


def parse_rqs(picoc: Path) -> list[dict[str, str]]:
    text = picoc.read_text(encoding="utf-8")
    secs = sections(text)
    body = find(secs, "Preguntas por componente") or ""
    rows = table(body)
    out = []
    for r in rows:
        rq = col(r, "RQ").strip()
        if not rq:
            continue
        out.append(
            {
                "id": rq,
                "component": col(r, "Comp").strip(),
                "question": col(r, "Pregunta").strip(),
                "dato_extraer": col(r, "Dato a extraer").strip(),
            }
        )
    if not out:
        raise Fail(f"no hay RQ en {rel(picoc)}", "revisa ## Preguntas por componente")
    return out


def cribado2_csv(picoc: Path) -> Path:
    marco = pv.dir_marco(picoc) or "MARCO"
    path = picoc.parent / f"resultados-{marco}-cribado-2.csv"
    if not path.is_file():
        raise Fail(
            f"falta {rel(path)}",
            f"Usa rsl-cribado-2-aplicar sobre {rel(pv.theme_of(picoc))}/",
        )
    return path


def count_si(csv_path: Path) -> int:
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return 0
    key = COL_OK
    if key not in rows[0]:
        for k in rows[0]:
            if "acepta" in k.casefold():
                key = k
                break
    return sum(1 for r in rows if (r.get(key) or "").strip().upper() == "SI")


def items_dir(theme: Path) -> Path:
    return theme / ITEMS_ROOT


def read_latest(theme: Path) -> Path | None:
    latest = items_dir(theme) / LATEST_FILE
    if not latest.is_file():
        return None
    name = latest.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    if not name:
        return None
    folder = items_dir(theme) / name
    return folder if (folder / ITEMS_MD).is_file() else None


def new_timestamp() -> str:
    now = dt.datetime.now()
    return now.strftime("%Y-%m-%d-%H%M")


def parse_items_md(path: Path) -> tuple[list[str], dict[str, list[dict[str, str]]], list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errs: list[str] = []
    warns: list[str] = []
    items_by_rq: dict[str, list[dict[str, str]]] = {}
    rq_ids: list[str] = []

    for m in re.finditer(r"^##\s+(RQ\d+)\b", text, flags=re.M | re.I):
        rq_ids.append(m.group(1).upper())

    for rq in rq_ids:
        block_m = re.search(rf"^##\s+{re.escape(rq)}\b.*?$(.*?)(?=^##\s|\Z)", text, flags=re.M | re.S)
        if not block_m:
            continue
        block = block_m.group(1)
        sub = find(sections(block, "###"), "ítems") or find(sections(block, "###"), "items")
        if sub is None:
            sub = block
        rows = table(sub)
        parsed = []
        for r in rows:
            iid = col(r, "Id").strip().upper()
            if not iid:
                continue
            parsed.append(
                {
                    "id": iid,
                    "label": col(r, "Ítem").strip() or col(r, "Item").strip(),
                    "data_type": col(r, "Tipo").strip().casefold(),
                    "hint": col(r, "Notas").strip(),
                }
            )
        items_by_rq[rq] = parsed

    for rq in rq_ids:
        items = items_by_rq.get(rq, [])
        if len(items) < MIN_ITEMS:
            errs.append(f"E2: {rq} tiene {len(items)} ítem(s); mínimo {MIN_ITEMS}")
        if len(items) > MAX_ITEMS:
            errs.append(f"E3: {rq} tiene {len(items)} ítems; máximo {MAX_ITEMS}")
        seen = set()
        for it in items:
            im = ITEM_ID_RE.match(it["id"])
            if not im or im.group(1) != rq[2:]:
                errs.append(f"E4: id {it['id']} no coincide con {rq}")
            if it["id"] in seen:
                errs.append(f"E4: id duplicado {it['id']}")
            seen.add(it["id"])
            dtok = it["data_type"]
            if dtok and dtok not in DATA_TYPES:
                errs.append(f"E5: {it['id']} tipo «{dtok}» no válido")
            if not it["label"]:
                errs.append(f"E6: {it['id']} sin etiqueta")

    return rq_ids, items_by_rq, errs, warns


def lint_items(theme: Path, items_md: Path) -> tuple[list[str], list[str]]:
    _, picoc, _ = picoc_context(theme)
    expected = [r["id"].upper() for r in parse_rqs(picoc)]
    rq_ids, items_by_rq, errs, warns = parse_items_md(items_md)

    for rq in expected:
        if rq not in rq_ids and rq not in items_by_rq:
            errs.append(f"E2: falta sección ## {rq}")
    for rq in rq_ids:
        if rq not in expected:
            warns.append(f"W2: {rq} no está en el picoc vigente")

    picoc_rows = {r["id"].upper(): r for r in parse_rqs(picoc)}
    for rq, row in picoc_rows.items():
        dato = row["dato_extraer"]
        if not dato or rq not in items_by_rq:
            continue
        parts = [p.strip() for p in re.split(r"\s·\s|\s*\|\s*", dato) if p.strip()]
        labels = " ".join(it["label"].casefold() for it in items_by_rq.get(rq, []))
        for part in parts[:8]:
            tokens = [t for t in re.split(r"\W+", part.casefold()) if len(t) > 4]
            if tokens and not any(t in labels for t in tokens[:3]):
                short = part if len(part) <= 60 else part[:60] + "…"
                warns.append(f"W1: {rq} — fragmento del picoc posiblemente sin ítem: «{short}»")

    json_path = items_md.parent / ITEMS_JSON
    if json_path.is_file():
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errs.append(f"E7: items.json inválido ({e})")
        else:
            for rq in expected:
                block = next((x for x in data.get("rqs", []) if (x.get("id") or "").upper() == rq), None)
                if not block:
                    errs.append(f"E7: items.json sin bloque {rq}")
                elif len(block.get("items") or []) != len(items_by_rq.get(rq, [])):
                    warns.append(f"W3: items.json y items.md difieren en conteo de {rq}")

    return errs, warns


def emit_json(theme: Path, items_md: Path, marco: str, picoc: Path, csv_path: Path) -> dict:
    rq_ids, items_by_rq, _, _ = parse_items_md(items_md)
    picoc_rows = {r["id"].upper(): r for r in parse_rqs(picoc)}
    rqs_out = []
    for rq in sorted(rq_ids, key=lambda x: int(x[2:])):
        block = picoc_rows.get(rq, {})
        items = []
        for it in items_by_rq.get(rq, []):
            items.append(
                {
                    "id": it["id"],
                    "label": it["label"],
                    "data_type": it["data_type"],
                    "hint": it["hint"],
                }
            )
        rqs_out.append(
            {
                "id": rq,
                "component": block.get("component", ""),
                "items": items,
            }
        )
    return {
        "version": 1,
        "marco": marco,
        "theme": rel(theme),
        "picoc": rel(picoc),
        "cribado2_csv": rel(csv_path),
        "common_fields": ["id", "titulo", "autores", "anio", "venue", "doi"],
        "rqs": rqs_out,
    }


def cmd_prepare(args: list[str]) -> int:
    if len(args) != 1:
        raise Fail("uso: resultado-items.py prepare docs/<slug>", None, 2)
    theme = theme_path(args[0])
    marco, picoc, _ = picoc_context(theme)
    csv_path = cribado2_csv(picoc)
    rqs = parse_rqs(picoc)
    n_si = count_si(csv_path)
    dest = new_timestamp()
    payload = {
        "theme": rel(theme),
        "marco": marco,
        "picoc": rel(picoc),
        "cribado2_csv": rel(csv_path),
        "n_incluidos_si": n_si,
        "rqs": rqs,
        "dest_folder": f"{ITEMS_ROOT}/{dest}",
        "timestamp": dest,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    folder = theme / ITEMS_ROOT / dest
    folder.mkdir(parents=True, exist_ok=True)
    debate = folder / DEBATE_MD
    if not debate.is_file():
        debate.write_text(DEBATE_SKELETON, encoding="utf-8")
    return ok(
        f"prepare {rel(theme)} ({len(rqs)} RQ, {n_si} SI en cribado 2)",
        f"escribe {ITEMS_ROOT}/{dest}/{ITEMS_MD} y Usa rsl-resultado-items",
    )


def cmd_status(args: list[str]) -> int:
    if len(args) != 1:
        raise Fail("uso: resultado-items.py status docs/<slug>", None, 2)
    theme = theme_path(args[0])
    marco, picoc, _ = picoc_context(theme)
    csv_path = cribado2_csv(picoc)
    latest = read_latest(theme)
    if latest is None:
        return error("FALTA desglose de ítems", f"Usa rsl-resultado-items sobre {rel(theme)}/")

    manifest = latest / MANIFEST
    if manifest.is_file():
        meta = json.loads(manifest.read_text(encoding="utf-8"))
        if meta.get("picoc_sha") != file_sha(picoc):
            return error("DESFASADO (cambió picoc)", f"Usa rsl-resultado-items sobre {rel(theme)}/ rewrite")
        if meta.get("cribado2_sha") != file_sha(csv_path):
            return error("DESFASADO (cambió CSV cribado 2)", f"Usa rsl-resultado-items sobre {rel(theme)}/ rewrite")

    errs, warns = lint_items(theme, latest / ITEMS_MD)
    for w in warns:
        print(f"WARN {w}")
    if errs:
        return error(f"lint falla ({len(errs)} error(es))", "corrige items.md y resultado-items:lint")
    return ok(f"PASS {rel(latest)} · marco {marco}")


def cmd_lint(args: list[str]) -> int:
    if len(args) not in (1, 2):
        raise Fail("uso: resultado-items.py lint docs/<slug> [items.md]", None, 2)
    theme = theme_path(args[0])
    if len(args) == 2:
        target = Path(args[1])
        if not target.is_absolute():
            target = ROOT / target
    else:
        folder = read_latest(theme)
        if folder is None:
            return error("E1: no hay latest", f"Usa rsl-resultado-items sobre {rel(theme)}/")
        target = folder / ITEMS_MD

    errs, warns = lint_items(theme, target)
    for w in warns:
        print(f"WARN {w}")
    for e in errs:
        print(e)
    if errs:
        return error(f"{len(errs)} FAIL", "corrige items.md")
    return ok(f"lint {rel(target)}")


def cmd_stamp(args: list[str]) -> int:
    if len(args) != 2:
        raise Fail("uso: resultado-items.py stamp docs/<slug> <YYYY-MM-DD-HHMM>", None, 2)
    theme = theme_path(args[0])
    marco, picoc, _ = picoc_context(theme)
    csv_path = cribado2_csv(picoc)
    folder = items_dir(theme) / args[1].strip()
    items_md = folder / ITEMS_MD
    if not items_md.is_file():
        raise Fail(f"no existe {rel(items_md)}", "genera items.md antes del stamp")

    errs, _ = lint_items(theme, items_md)
    if errs:
        for e in errs:
            print(e)
        return error("stamp abortado por lint", "corrige items.md")

    payload = emit_json(theme, items_md, marco, picoc, csv_path)
    (folder / ITEMS_JSON).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    manifest = {
        "marco": marco,
        "picoc": rel(picoc),
        "picoc_sha": file_sha(picoc),
        "cribado2_csv": rel(csv_path),
        "cribado2_sha": file_sha(csv_path),
        "n_incluidos_si": count_si(csv_path),
        "stamped": dt.datetime.now().isoformat(timespec="minutes"),
        "folder": args[1].strip(),
    }
    (folder / MANIFEST).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    items_dir(theme).mkdir(parents=True, exist_ok=True)
    (items_dir(theme) / LATEST_FILE).write_text(args[1].strip() + "\n", encoding="utf-8")
    return ok(f"latest → {ITEMS_ROOT}/{args[1].strip()}")


def dispatch(args: list[str]) -> int:
    if not args:
        print(__doc__)
        return error("falta subcomando", "prepare | lint | status | stamp", code=2)
    cmd, rest = args[0], args[1:]
    if cmd == "prepare":
        return cmd_prepare(rest)
    if cmd == "status":
        return cmd_status(rest)
    if cmd == "lint":
        return cmd_lint(rest)
    if cmd == "stamp":
        return cmd_stamp(rest)
    return error(f"subcomando desconocido {cmd}", "prepare | lint | status | stamp", code=2)


def cli(args: list[str]) -> int:
    try:
        return dispatch(args)
    except pv.MarcoError as e:
        raise Fail(str(e), e.fix)


if __name__ == "__main__":
    run(cli)
