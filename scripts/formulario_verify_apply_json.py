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
    normalize_whitespace,
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


_NUM_RE = re.compile(r"\d+(?:[.,]\d+)?")
WEAK_QUOTE_LEN = 60


def expected_item_ids(folder: Path, article_id: str) -> set[str] | None:
    """Ítems esperados para el estudio según formulario-map.json (placement por hoja)."""
    try:
        m = json.loads((folder / MAP_JSON).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    st = next((x for x in m.get("studies", []) if x.get("corpus_id") == article_id), None)
    if not st:
        return None
    placed = {sh for sh, pl in (st.get("placement") or {}).items() if pl}
    return {it["item_id"] for it in m.get("items", []) if it.get("sheet") in placed}


def review_flags(article_id: str, slots: list[dict], expected: set[str] | None) -> list[str]:
    """Advertencias de calidad (checklist R2 automatizado): slots que merecen crítico."""
    out: list[str] = []
    seen = {(s.get("item_id") or "").strip() for s in slots if isinstance(s, dict)}
    if expected is not None:
        miss = sorted(expected - seen)
        if miss:
            out.append(f"{article_id}: faltan ítems esperados: {', '.join(miss)}")
    by_quote: dict[str, list[str]] = {}
    for slot in slots:
        if not isinstance(slot, dict):
            continue
        item = (slot.get("item_id") or "").strip()
        val = (slot.get("value") or "").strip()
        dec = (slot.get("decision") or "").strip()
        evs = [e for e in (slot.get("evidence") or []) if isinstance(e, dict)]
        if dec == "absent" or val in ("", "—") or not evs:
            continue
        quotes = [normalize_whitespace(e.get("quote") or "") for e in evs]
        if max((len(q) for q in quotes), default=0) < WEAK_QUOTE_LEN:
            out.append(f"{article_id}:{item}: cita débil (<{WEAK_QUOTE_LEN} caracteres)")
        qtext = " ".join(quotes)
        qnums = {n.replace(",", ".") for n in _NUM_RE.findall(qtext)}
        vnums = {n.replace(",", ".") for n in _NUM_RE.findall(val) if len(n.replace(",", "").replace(".", "")) >= 2}
        # RQ1-I3 etc. pueden declarar N inferido; solo avisa, no bloquea
        lost = sorted(n for n in vnums if n not in qnums)
        if lost:
            out.append(f"{article_id}:{item}: cifras del value ausentes en las citas: {', '.join(lost)}")
        for q in quotes:
            if q:
                by_quote.setdefault(q, []).append(item)
    for q, items in by_quote.items():
        uniq = sorted(set(items))
        if len(uniq) >= 3:
            out.append(f"{article_id}: misma cita sostiene {len(uniq)} ítems ({', '.join(uniq)})")
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
    ap.add_argument("--strict", action="store_true", help="las advertencias (REVISAR) también hacen fallar")
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
    all_flags: list[str] = []
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
        all_flags.extend(
            review_flags(article_id or jf.stem, [x for x in slots if isinstance(x, dict)], expected_item_ids(folder, article_id))
        )
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

    if all_flags:
        print("REVISAR (pasar al crítico solo estos slots):", file=sys.stderr)
        for fl in all_flags[:80]:
            print(f"  - {fl}", file=sys.stderr)
    if all_errs:
        for e in all_errs[:80]:
            print(e, file=sys.stderr)
        if len(all_errs) > 80:
            print(f"... y {len(all_errs) - 80} más", file=sys.stderr)
        print(f"FAIL: {len(all_errs)} error(es) en evidence", file=sys.stderr)
        return 1
    print(
        f"OK: {len(files)} apply JSON(s), evidence coherente (≥{MIN_QUOTE_LEN} chars, substring en src)"
        + (f" · {len(all_flags)} a REVISAR" if all_flags else "")
    )
    return 1 if (all_flags and args.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
