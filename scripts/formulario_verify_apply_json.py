#!/usr/bin/env python3
"""Verifica evidence[] en apply-<corpus_id>.json antes de formulario:apply-lote.

Comprueba lo mismo que lint-traza sobre evidencia: quote ≥40, substring literal en src
(normalize_whitespace + casefold como en formulario_lint_prosa), loc anclado, quote ≠ value.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from formulario_lint_prosa import (  # noqa: E402
    MIN_QUOTE_LEN,
    lint_evidence_row,
)

FORMULARIO_ROOT = Path("resultados/formulario")
LATEST_FILE = "latest.txt"
MAP_JSON = "formulario-map.json"
FORMULARIO_XLSX = "Formulario.xlsx"


def theme_path(arg: str) -> Path:
    p = Path(arg)
    if not p.is_absolute():
        p = ROOT / p
    return p.resolve()


def resolve_formulario_folder(theme: Path, carpeta: str | None) -> Path:
    """Alineado con resolve_formulario_folder en resultado-formulario.py (simplificado)."""
    base = theme / FORMULARIO_ROOT
    if carpeta:
        folder = base / carpeta.strip()
        if folder.is_dir() and (folder / MAP_JSON).is_file():
            return folder
        raise SystemExit(f"carpeta de formulario inválida o sin mapa: {folder}")
    latest = base / LATEST_FILE
    if latest.is_file():
        name = latest.read_text(encoding="utf-8").strip().splitlines()[0].strip()
        folder = base / name
        if (folder / FORMULARIO_XLSX).is_file() and (folder / MAP_JSON).is_file():
            return folder
    if not base.is_dir():
        raise SystemExit(f"no existe {base}")
    candidates = sorted(
        (
            p
            for p in base.iterdir()
            if p.is_dir() and re.match(r"^\d{4}-\d{2}-\d{2}-\d{4}$", p.name)
        ),
        key=lambda p: p.name,
        reverse=True,
    )
    for folder in candidates:
        if (folder / MAP_JSON).is_file():
            return folder
    raise SystemExit("no se pudo resolver carpeta del formulario (latest.txt o fecha)")


def collect_apply_files(paths: list[Path]) -> list[Path]:
    out: list[Path] = []
    for p in paths:
        p = p.resolve()
        if p.is_file():
            if p.suffix.lower() == ".json" and p.name.startswith("apply-"):
                out.append(p)
            else:
                raise SystemExit(f"no es apply-*.json: {p}")
        elif p.is_dir():
            for f in sorted(p.rglob("apply-*.json")):
                if f.is_file():
                    out.append(f)
        else:
            raise SystemExit(f"ruta inexistente: {p}")
    if not out:
        raise SystemExit("no se encontró ningún apply-*.json")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Verifica evidence en apply-*.json (pre apply-lote). "
        "Uso: docs/<slug> [carpeta] path [path ...]"
    )
    ap.add_argument("theme", type=str, help="Ruta al tema, p. ej. docs/mi-tema")
    ap.add_argument(
        "rest",
        nargs="+",
        help="Carpeta YYYY-MM-DD-HHMM (opcional si va primero y existe) y/o rutas apply-*.json o directorios",
    )
    args = ap.parse_args()
    theme = theme_path(args.theme)
    repo_root = ROOT.resolve()

    rest = [str(x) for x in args.rest]
    carpeta: str | None = None
    path_args: list[str] = []
    if rest:
        cand = theme / FORMULARIO_ROOT / rest[0]
        if len(rest) >= 2 and cand.is_dir() and (cand / MAP_JSON).is_file():
            carpeta = rest[0]
            path_args = rest[1:]
        else:
            path_args = rest[:]

    if not path_args:
        raise SystemExit("faltan rutas a apply-*.json o directorios con apply-*.json")

    folder = resolve_formulario_folder(theme, carpeta)
    files = collect_apply_files([Path(p) for p in path_args])

    all_errs: list[str] = []
    for jf in files:
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            all_errs.append(f"{jf}: JSON inválido: {e}")
            continue
        slots = data.get("slots")
        article_id = (data.get("article_id") or "").strip()
        if not isinstance(slots, list):
            all_errs.append(f"{jf}: falta lista slots")
            continue
        for slot in slots:
            if not isinstance(slot, dict):
                all_errs.append(f"{jf}: entrada no objeto en slots")
                continue
            item_id = (slot.get("item_id") or "").strip()
            cell = f"{article_id or '?'}:{item_id}"
            rec = {**slot, "cell": cell}
            for e in lint_evidence_row(
                rec,
                item_id if item_id else None,
                folder=folder,
                repo_root=repo_root,
            ):
                all_errs.append(f"{jf}: {e}")

    if all_errs:
        for e in all_errs[:80]:
            print(e, file=sys.stderr)
        if len(all_errs) > 80:
            print(f"... y {len(all_errs) - 80} más", file=sys.stderr)
        print(f"FAIL: {len(all_errs)} error(es) en evidence", file=sys.stderr)
        return 1
    print(
        f"OK: {len(files)} apply JSON(s), evidence coherente (≥{MIN_QUOTE_LEN} chars, substring en src)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
