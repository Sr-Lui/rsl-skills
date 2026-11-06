"""Valida celdas de ítem según response_type y calidad de extraccion-traza.jsonl.

Incluye: duplicados de texto entre ítems distintos (mismo estudio), evidencia mínima
y heurística WARN de plantilla repetida entre estudios.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent

ITEM_IDS = frozenset(
    f"RQ{r}-I{i}" for r in (1, 2, 3) for i in range(1, 6) if not (r == 1 and i > 4) and not (r == 2 and i > 4)
)

# Mismo párrafo en dos ítems distintos del mismo estudio (caracteres tras normalizar espacios).
MIN_DUP_VALUE_LEN = 48
# Cita mínima en evidence[].quote (decision con contenido).
MIN_QUOTE_LEN = 40
# Valor idéntico en muchos estudios → posible copy-paste (WARN, no FAIL).
MIN_TEMPLATE_VALUE_LEN = 80
# Fracción de la muestra SI que debe repetir el mismo texto para disparar WARN plantilla.
TEMPLATE_WARN_FRAC = 0.35
TEMPLATE_WARN_MIN_STUDIES = 5
# Un valor domina demasiadas filas distintas (article_id × item_id) → FAIL (posible plantilla sin leer).
DOMINANCE_FRAC = 0.80
DOMINANCE_MIN_STUDIES = 5
DOMINANCE_MIN_VALUE_LEN = 40
# Lectura máxima del MD para comprobar substring (coste).
MAX_EVIDENCE_FILE_CHARS = 1_500_000

LOC_FORBIDDEN = frozenset({"fulltext", "texto completo", "texto_completo"})
# p.3 | pp. 12–14 | l. 45 | §2.1 | Sección Methods | líneas 10–12
LOC_ANCHOR_RE = re.compile(
    r"^(p\.|pp\.|pg\.|pág\.|líneas?|lineas?|lines?|l\.|§|sec\.|sección|seccion|section|fig\.|tabla)\s*\S.*",
    re.I,
)


def _norm(s: str) -> str:
    return (s or "").strip()


def normalize_whitespace(s: str) -> str:
    """Colapsa espacios para comparar cita con texto fuente."""
    return " ".join(_norm(s).split())


def normalize_value_for_dup(s: str) -> str:
    """Colapsa espacios para comparar duplicados entre ítems."""
    return " ".join(_norm(s).split())


def load_manifest(folder: Path) -> dict[str, Any]:
    man_path = folder / "manifest.json"
    if not man_path.is_file():
        return {}
    try:
        return json.loads(man_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def evidence_loc_whitelist(folder: Path) -> list[str]:
    """Valores de `loc` admitidos además del patrón LOC_ANCHOR_RE (manifest.evidence_loc_whitelist)."""
    w = load_manifest(folder).get("evidence_loc_whitelist")
    if isinstance(w, list):
        return [str(x).strip() for x in w if str(x).strip()]
    return []


def resolve_evidence_src(src: str, repo_root: Path) -> Path | None:
    s = (src or "").strip()
    if not s:
        return None
    p = Path(s)
    if p.is_absolute():
        return p if p.is_file() else None
    cand = (repo_root / s).resolve()
    return cand if cand.is_file() else None


def loc_is_valid(loc: str, whitelist: list[str]) -> bool:
    t = _norm(loc)
    if not t:
        return False
    if t.casefold() in {x.casefold() for x in whitelist}:
        return True
    if t.casefold() in LOC_FORBIDDEN:
        return False
    return bool(LOC_ANCHOR_RE.match(t))


def _quote_in_file(quote: str, file_path: Path) -> bool:
    qn = normalize_whitespace(quote)
    if not qn:
        return False
    try:
        raw = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    if len(raw) > MAX_EVIDENCE_FILE_CHARS:
        raw = raw[:MAX_EVIDENCE_FILE_CHARS]
    fn = normalize_whitespace(raw)
    if qn in fn:
        return True
    return qn.casefold() in fn.casefold()


def lint_item_value(item_id: str, response_type: str, value: str, decision: str) -> list[str]:
    """Returns list of error messages (empty = OK)."""
    val = _norm(value)
    if decision == "absent" or val in ("", "—"):
        return []
    if decision not in ("extracted", "partial", "omitted"):
        return []

    rt = (response_type or "").strip().lower()
    errs: list[str] = []

    if rt == "cuantitativo":
        errs.extend(_lint_cuantitativo(item_id, val))
    elif rt == "mixto":
        errs.extend(_lint_mixto(item_id, val))
    elif rt == "cualitativo":
        errs.extend(_lint_cualitativo(item_id, val))

    return errs


def _lint_cuantitativo(item_id: str, val: str) -> list[str]:
    head = val.split(".", 1)[0].strip()
    if item_id == "RQ1-I2":
        if not re.match(r"^(Sí|No|NR)\b", val, re.I) and not re.search(
            r"\b(Sí|No|NR)\.\s", val
        ):
            return [f"{item_id}: cuantitativo debe incluir Sí, No o NR como registro"]
        return []
    if item_id == "RQ2-I3":
        if not re.search(
            r"(Requisitos|Diseño|Desarrollo|Personalización|Pruebas|V&V|Auditoría|Otro|NR)",
            val,
            re.I,
        ):
            return [f"{item_id}: falta categoría de fase principal (lista items.md)"]
        return []
    if item_id == "RQ2-I4":
        if val.startswith("—") or head == "—":
            return []
        if ";" in val or re.match(r"^[A-Za-zÁ-ú]", head):
            return []
        return [f"{item_id}: otras fases: lista con ; o — al inicio"]
    if item_id == "RQ3-I4":
        if not re.search(r"\b(Cognitiva|Sensorial|Ambas|NR)\b", val, re.I):
            return [f"{item_id}: debe incluir Cognitiva, Sensorial, Ambas o NR"]
        return []
    if item_id == "RQ3-I5":
        if not re.search(
            r"(Integración continua|Semiautomática|Solo validación con usuarios|NR)",
            val,
            re.I,
        ):
            return [
                f"{item_id}: debe incluir Integración continua, Semiautomática, "
                "Solo validación con usuarios o NR"
            ]
        return []
    if re.search(r"\d", val):
        return []
    return [f"{item_id}: cuantitativo sin número ni categoría reconocible"]


def _lint_mixto(item_id: str, val: str) -> list[str]:
    required: dict[str, tuple[str, ...]] = {
        "RQ1-I3": ("Presencia:", "N:", "Rol:"),
        "RQ1-I4": ("Enfoque:", "Perfil:", "Consentimiento:", "País:"),
        "RQ3-I1": ("Constructo:", "Valor:"),
    }
    keys = required.get(item_id)
    if not keys:
        return []
    missing = [k for k in keys if k not in val]
    if missing:
        return [f"{item_id}: plantilla mixta falta {', '.join(missing)}"]
    return []


def _lint_cualitativo(item_id: str, val: str) -> list[str]:
    if item_id in ("RQ1-I1", "RQ2-I1", "RQ2-I2", "RQ3-I3") and len(val) > 120 and ";" not in val:
        return [f"WARN {item_id}: cualitativo nominal/categórico largo sin ; — revisar etiquetas"]
    return []


def _rq3_i1_valor_has_numeric(val: str) -> bool:
    m = re.search(r"Valor:\s*([^\|]+)", val, re.I)
    if not m:
        return False
    part = m.group(1).strip()
    if re.search(r"\bNR\b", part, re.I):
        return False
    return bool(re.search(r"\d", part))


def lint_evidence_row(
    rec: dict[str, Any],
    item_id: str | None,
    *,
    folder: Path,
    repo_root: Path,
) -> list[str]:
    """FAIL: evidencia vacía, quote corto, loc vago, quote no literal en src, quote==value; RQ3-I1 numérico."""
    dec = (rec.get("decision") or "").strip()
    val = _norm(rec.get("value") or "")
    cell = rec.get("cell") or "?"
    loc_whitelist = evidence_loc_whitelist(folder)

    if dec == "absent" or val in ("", "—"):
        return []

    evs = rec.get("evidence") or []
    if not isinstance(evs, list) or not evs:
        return [f"{cell}: evidence[] vacío (se requiere al menos una cita)"]

    val_n = normalize_whitespace(val)
    errs: list[str] = []
    any_numeric_quote = False
    for i, ev in enumerate(evs):
        if not isinstance(ev, dict):
            errs.append(f"{cell}: evidence[{i}] no es objeto JSON")
            continue
        src = (ev.get("src") or "").strip()
        loc = (ev.get("loc") or "").strip()
        quote = (ev.get("quote") or "").strip()
        if not src:
            errs.append(f"{cell}: evidence[{i}] falta src")
            continue
        src_path = resolve_evidence_src(src, repo_root)
        if src_path is None:
            errs.append(f"{cell}: evidence[{i}] src no existe en disco: {src}")
        if not loc:
            errs.append(f"{cell}: evidence[{i}] falta loc")
        elif not loc_is_valid(loc, loc_whitelist):
            errs.append(
                f"{cell}: evidence[{i}] loc no anclado (usa p./l./§/Sección…; "
                f"prohibido «fulltext»; excepciones en manifest.evidence_loc_whitelist): «{loc}»"
            )
        if len(quote) < MIN_QUOTE_LEN:
            errs.append(
                f"{cell}: evidence[{i}] quote demasiado corto ({len(quote)}<{MIN_QUOTE_LEN} caracteres)"
            )
        qn = normalize_whitespace(quote)
        if qn and val_n and qn == val_n:
            errs.append(
                f"{cell}: evidence[{i}] quote no puede ser idéntico al value de la celda "
                "(cita literal distinta del texto sintetizado en Excel)"
            )
        if quote and re.search(r"\d", quote):
            any_numeric_quote = True
        if src_path is not None and len(qn) >= MIN_QUOTE_LEN and not _quote_in_file(quote, src_path):
            errs.append(
                f"{cell}: evidence[{i}] quote no aparece como substring en {src} "
                "(cita literal desde MD)"
            )

    if item_id == "RQ3-I1" and _rq3_i1_valor_has_numeric(val) and evs and not any_numeric_quote:
        errs.append(
            f"{cell}: RQ3-I1 reporta Valor numérico: al menos una evidence.quote debe contener la cifra"
        )

    return errs


def _whitelist_covers_duplicate(
    article_id: str,
    item_ids: frozenset[str],
    whitelist: list[dict[str, Any]],
) -> bool:
    for entry in whitelist:
        if (entry.get("article_id") or "").strip() != article_id:
            continue
        items = entry.get("item_ids") or entry.get("items") or []
        if not isinstance(items, (list, tuple)):
            continue
        s = frozenset(str(x).strip() for x in items if str(x).strip())
        if item_ids <= s or item_ids == s:
            return True
    return False


def lint_duplicate_item_values(
    records: list[dict[str, Any]],
    whitelist: list[dict[str, Any]],
) -> list[str]:
    """
    FAIL si el mismo texto largo (mismo estudio) aparece en dos item_id distintos.
    El mismo item_id en dos hojas (mixto) se deduplica por (article_id, item_id).
    """
    by_study_item: dict[tuple[str, str], dict[str, Any]] = {}
    for rec in records:
        aid = (rec.get("article_id") or "").strip()
        iid = (rec.get("item_id") or "").strip()
        if not aid or not iid:
            continue
        key = (aid, iid)
        dec = (rec.get("decision") or "").strip()
        val = _norm(rec.get("value") or "")
        if dec not in ("extracted", "partial", "omitted") or val in ("", "—"):
            continue
        by_study_item[key] = rec

    by_study_norm: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for (aid, iid), rec in by_study_item.items():
        nv = normalize_value_for_dup(rec.get("value") or "")
        if len(nv) < MIN_DUP_VALUE_LEN:
            continue
        by_study_norm[aid][nv].append(iid)

    errs: list[str] = []
    for aid, norm_map in by_study_norm.items():
        for norm_val, iids in norm_map.items():
            distinct = sorted(frozenset(iids))
            if len(distinct) <= 1:
                continue
            pair_set = frozenset(distinct)
            if _whitelist_covers_duplicate(aid, pair_set, whitelist):
                continue
            preview = (norm_val[:72] + "…") if len(norm_val) > 72 else norm_val
            errs.append(
                f"E10: {aid} mismo texto en ítems distintos {', '.join(distinct)} "
                f"(≥{MIN_DUP_VALUE_LEN} caracteres). … «{preview}». "
                f"Añade duplicate_value_whitelist en manifest.json si es excepción documentada."
            )
    return errs


def lint_template_repeated_across_studies(
    records: list[dict[str, Any]],
    n_si: int,
) -> list[str]:
    """WARN: mismo valor largo en >= fracción de estudios para un mismo item_id."""
    threshold = max(TEMPLATE_WARN_MIN_STUDIES, int(n_si * TEMPLATE_WARN_FRAC))
    by_item_norm: dict[str, Counter[str]] = defaultdict(Counter)
    for rec in records:
        iid = (rec.get("item_id") or "").strip()
        dec = (rec.get("decision") or "").strip()
        val = _norm(rec.get("value") or "")
        aid = (rec.get("article_id") or "").strip()
        if not iid or not aid or dec not in ("extracted", "partial", "omitted"):
            continue
        if val in ("", "—"):
            continue
        nv = normalize_value_for_dup(val)
        if len(nv) < MIN_TEMPLATE_VALUE_LEN:
            continue
        by_item_norm[iid][nv] += 1

    warns: list[str] = []
    for iid, ctr in by_item_norm.items():
        for norm_val, cnt in ctr.items():
            if cnt >= threshold:
                pv = (norm_val[:60] + "…") if len(norm_val) > 60 else norm_val
                warns.append(
                    f"WARN {iid}: mismo texto en {cnt}/{n_si} estudios (≥{MIN_TEMPLATE_VALUE_LEN} "
                    f"car.) — posible plantilla sin leer: «{pv}»"
                )
    return warns


def lint_value_dominance_across_studies(records: list[dict[str, Any]]) -> list[str]:
    """
    FAIL si un único valor normalizado cubre >= DOMINANCE_FRAC de las celdas con contenido
    para un mismo item_id (filas article × item en la traza).
    """
    by_item: dict[str, Counter[str]] = defaultdict(Counter)
    for rec in records:
        iid = (rec.get("item_id") or "").strip()
        dec = (rec.get("decision") or "").strip()
        val = _norm(rec.get("value") or "")
        aid = (rec.get("article_id") or "").strip()
        if not iid or not aid or dec not in ("extracted", "partial", "omitted"):
            continue
        if val in ("", "—"):
            continue
        nv = normalize_value_for_dup(val)
        if len(nv) < DOMINANCE_MIN_VALUE_LEN:
            continue
        by_item[iid][nv] += 1

    errs: list[str] = []
    for iid, ctr in by_item.items():
        total = sum(ctr.values())
        if total < DOMINANCE_MIN_STUDIES:
            continue
        norm_val, cnt = ctr.most_common(1)[0]
        if cnt < total * DOMINANCE_FRAC:
            continue
        preview = (norm_val[:72] + "…") if len(norm_val) > 72 else norm_val
        errs.append(
            f"E13: {iid} un solo valor domina {cnt}/{total} celdas (≥{int(DOMINANCE_FRAC * 100)}%) "
            f"— «{preview}» — revisar MD por estudio o marcar omitted/partial con matiz"
        )
    return errs


def lint_traza_evidence(
    folder: Path,
    *,
    repo_root: Path | None = None,
) -> list[str]:
    """Solo evidencia (src/loc/quote) + RQ3-I1 numérico."""
    rr = repo_root if repo_root is not None else REPO_ROOT
    records, err = load_traza_records(folder / "extraccion-traza.jsonl")
    if err:
        return [err]
    assert records is not None
    errs: list[str] = []
    for rec in records:
        iid = rec.get("item_id")
        if not isinstance(iid, str):
            continue
        errs.extend(lint_evidence_row(rec, iid, folder=folder, repo_root=rr))
    return errs


def load_duplicate_whitelist(folder: Path) -> list[dict[str, Any]]:
    man = load_manifest(folder)
    w = man.get("duplicate_value_whitelist")
    if isinstance(w, list):
        return [x for x in w if isinstance(x, dict)]
    return []


# Ítems principalmente nominales/categóricos: plantilla repetida entre estudios pasa a FAIL con --strict.
STRICT_TEMPLATE_ITEM_IDS = frozenset({"RQ1-I1", "RQ2-I1", "RQ2-I2", "RQ3-I2", "RQ3-I3"})
STRICT_TEMPLATE_FRAC = 0.25


def load_traza_records(traza_path: Path) -> tuple[list[dict[str, Any]] | None, str | None]:
    """Carga extraccion-traza.jsonl. Devuelve (records, error_message)."""
    if not traza_path.is_file():
        return None, "falta extraccion-traza.jsonl"
    records: list[dict[str, Any]] = []
    for line_no, raw in enumerate(traza_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            records.append(json.loads(raw))
        except json.JSONDecodeError as e:
            return None, f"línea {line_no} JSON inválido: {e}"
    return records, None


def lint_extraccion_manifest_complete(folder: Path) -> list[str]:
    """FAIL si extraccion_complete no es true (cierre con formulario:stamp)."""
    man_path = folder / "manifest.json"
    if not man_path.is_file():
        return ["E12: falta manifest.json"]
    try:
        man = json.loads(man_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"E12: manifest.json inválido: {e}"]
    if man.get("extraccion_complete") is not True:
        return [
            "E12: manifest extraccion_complete != true — cierra con "
            "`pnpm -s formulario:stamp docs/<slug> <carpeta>` tras lint-traza y lint-prosa PASS"
        ]
    return []


def lint_traza_structure(lines: list[dict[str, Any]], expected: int) -> tuple[list[str], list[str]]:
    """Estructura de traza (E3, E4, E8, E11). Retorna (errs, warns)."""
    errs: list[str] = []
    warns: list[str] = []
    if len(lines) > expected:
        errs.append(f"E8: traza {len(lines)} líneas > esperado {expected}")
    if len(lines) < expected:
        errs.append(f"E11: extracción incompleta en la traza ({len(lines)}/{expected} líneas)")
    for rec in lines:
        dec = rec.get("decision")
        val = _norm(rec.get("value") or "")
        cell = rec.get("cell") or "?"
        if dec in ("extracted", "partial") and not val:
            errs.append(f"E3: {cell} decision={dec} sin valor")
        if val and dec not in ("extracted", "partial", "omitted", "absent"):
            errs.append(f"E4: {cell} valor sin decision válida")
    return errs, warns


def run_lint_prosa_checks(
    folder: Path,
    item_defs: dict[str, dict[str, Any]],
    *,
    n_si: int,
    strict: bool = False,
    check_evidence: bool = True,
) -> tuple[list[str], list[str]]:
    """
    Prosa de ítem (+ evidencia opcional) + duplicados entre ítems
    + WARN plantilla entre estudios (FAIL parcial con --strict).
    """
    records, err = load_traza_records(folder / "extraccion-traza.jsonl")
    if err:
        return ([err], [])
    assert records is not None
    whitelist = load_duplicate_whitelist(folder)
    errs: list[str] = []
    warns: list[str] = []

    for rec in records:
        iid = rec.get("item_id")
        if not isinstance(iid, str):
            continue
        idef = item_defs.get(iid)
        if not idef:
            continue
        for msg in lint_item_value(
            iid, idef.get("response_type", ""), rec.get("value") or "", rec.get("decision", "")
        ):
            if msg.startswith("WARN"):
                # Heurística de «;» en cualitativos: no bloquea stamp --strict (revisión humana).
                if strict and "cualitativo nominal/categórico largo sin ;" in msg:
                    continue
                warns.append(f"{rec.get('cell')}: {msg}")
            else:
                errs.append(f"E9: {rec.get('cell')} {msg}")
        if check_evidence:
            errs.extend(lint_evidence_row(rec, iid, folder=folder, repo_root=REPO_ROOT))

    errs.extend(lint_duplicate_item_values(records, whitelist))
    errs.extend(lint_value_dominance_across_studies(records))
    tpl_warns = lint_template_repeated_across_studies(records, n_si)
    if strict:
        tpl_re = re.compile(r"^WARN (RQ\d+-I\d+): mismo texto en (\d+)/(\d+) estudios")
        for w in tpl_warns:
            m = tpl_re.match(w)
            if not m:
                warns.append(w)
                continue
            iid, cnt_s, n_s = m.group(1), m.group(2), m.group(3)
            cnt, n_st = int(cnt_s), int(n_s)
            if iid in STRICT_TEMPLATE_ITEM_IDS:
                thr = max(TEMPLATE_WARN_MIN_STUDIES, int(n_st * STRICT_TEMPLATE_FRAC))
            else:
                thr = max(TEMPLATE_WARN_MIN_STUDIES, int(n_st * 0.50))
            if cnt >= thr:
                errs.append(
                    f"E14: {w} — en --strict repeticiones masivas son FAIL; "
                    "revisa MD/cribado2:query o justifica en manifest"
                )
            else:
                warns.append(w)
    else:
        warns.extend(tpl_warns)

    return errs, warns
