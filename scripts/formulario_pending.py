#!/usr/bin/env python3
"""Lista los estudios pendientes de extracción (según extraccion-traza.jsonl y formulario-map.json).

Uso: formulario_pending.py docs/<slug> [carpeta]   (solo lectura)
Salida: por lote, corpus_id con ítems hechos/esperados; al final, siguiente lote sugerido.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from formulario_verify_apply_json import (  # noqa: E402
    expected_item_ids,
    resolve_formulario_folder,
    theme_path,
)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    theme = theme_path(sys.argv[1])
    folder = resolve_formulario_folder(theme, sys.argv[2] if len(sys.argv) > 2 else None)
    m = json.loads((folder / "formulario-map.json").read_text(encoding="utf-8"))
    done: dict[str, set[str]] = {}
    traza = folder / "extraccion-traza.jsonl"
    if traza.is_file():
        for ln in traza.read_text(encoding="utf-8").splitlines():
            if ln.strip():
                r = json.loads(ln)
                done.setdefault(r.get("article_id", ""), set()).add(r.get("item_id", ""))
    total_pend = 0
    next_lote = None
    for lote in m.get("lotes", []):
        pend = []
        for cid in lote["corpus_ids"]:
            exp = expected_item_ids(folder, cid) or set()
            miss = exp - done.get(cid, set())
            if miss:
                pend.append((cid, len(exp) - len(miss), len(exp)))
        total_pend += len(pend)
        status = "OK" if not pend else f"{len(pend)} pendiente(s)"
        print(f"lote-{lote['lote']}: {status}")
        for cid, d, e in pend:
            print(f"  {cid}: {d}/{e} ítems")
        if pend and next_lote is None:
            next_lote = lote["lote"]
    print(f"Pendientes: {total_pend} estudio(s)" + (f" · siguiente: lote-{next_lote}" if next_lote else " · extracción completa"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
