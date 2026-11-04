#!/usr/bin/env python3
"""Punteros del pipeline RSL en docs/<slug>/RSL/index-manifest.json (bloque rsl_pipeline)."""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_NAME = "index-manifest.json"
FORMULARIO_TEMPLATE = "global/Formulario de extracción de información.xlsx"
ITEMS_ROOT = "resultados/items"
LATEST_ITEMS = "latest.txt"


def rel(p: Path) -> str:
    p = p.resolve()
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)


def theme_path(arg: str | Path) -> Path:
    p = Path(arg)
    if not p.is_absolute():
        p = ROOT / p
    if not p.is_dir():
        raise ValueError(f"{arg} no es carpeta de tema")
    return p


def load_manifest(theme: Path) -> dict:
    path = theme / "RSL" / MANIFEST_NAME
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"version": 1, "entries": {}}


def read_items_latest(theme: Path) -> tuple[str | None, Path | None]:
    latest_file = theme / ITEMS_ROOT / LATEST_ITEMS
    if not latest_file.is_file():
        return None, None
    stamp = latest_file.read_text(encoding="utf-8").strip()
    if not stamp:
        return None, None
    folder = theme / ITEMS_ROOT / stamp
    if not folder.is_dir():
        return stamp, None
    return stamp, folder


def sync_pipeline(theme: Path, **overrides: str | None) -> dict:
    import picoc_versions as pv
    from cribado2 import cribado2_dir_name

    theme = theme_path(theme)
    marco, picoc, state = pv.status(theme)
    if state == "FALTA" or picoc is None:
        raise ValueError(f"sin picoc vigente en {rel(theme)}")

    marco_tag = pv.dir_marco(picoc) or marco
    picoc_dir = picoc.parent
    cribado2_csv = picoc_dir / f"resultados-{marco_tag}-cribado-2.csv"
    corpus = theme / "RSL" / "picoc" / cribado2_dir_name(picoc_dir.name)
    _stamp, items_folder = read_items_latest(theme)

    pipe: dict[str, str] = {
        "picoc_dir": rel(picoc_dir),
        "picoc_md": rel(picoc),
        "cribado2_csv": rel(cribado2_csv),
        "cribado2_corpus": rel(corpus),
        "cribado2_graph": rel(corpus / "graphify-out" / "graph.json"),
        "formulario_template": FORMULARIO_TEMPLATE,
    }
    if items_folder:
        pipe["items_latest"] = rel(items_folder)
        ij = items_folder / "items.json"
        im = items_folder / "items.md"
        if ij.is_file():
            pipe["items_json"] = rel(ij)
        if im.is_file():
            pipe["items_md"] = rel(im)

    prev = load_manifest(theme).get("rsl_pipeline") or {}
    if prev.get("formulario_latest"):
        pipe["formulario_latest"] = prev["formulario_latest"]
    if prev.get("extraccion_traza"):
        pipe["extraccion_traza"] = prev["extraccion_traza"]

    for k, v in overrides.items():
        if v is not None:
            pipe[k] = v

    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    pipe["updated_at"] = now

    data = load_manifest(theme)
    data["rsl_pipeline"] = pipe
    data["updated_at"] = now
    out = theme / "RSL" / MANIFEST_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return pipe


def cli(argv: list[str]) -> int:
    if len(argv) != 2 or argv[0] != "sync":
        print("uso: rsl_pipeline_manifest.py sync docs/<slug>")
        return 2
    try:
        pipe = sync_pipeline(argv[1])
    except ValueError as e:
        print(f"ERROR {e}")
        return 1
    print(json.dumps(pipe, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli(sys.argv[1:]))
