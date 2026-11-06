#!/usr/bin/env python3
"""Síntesis de resultados por ítem — skill rsl-resultado-sintesis.

  resultado-sintesis.py prepare docs/<slug>
  resultado-sintesis.py general docs/<slug> [carpeta]
  resultado-sintesis.py codify-auto docs/<slug> <ITEM|all> [carpeta] [--force]
  resultado-sintesis.py aggregate docs/<slug> <BLOQUE|all> [carpeta]
  resultado-sintesis.py borrador docs/<slug> <BLOQUE> [carpeta]
  resultado-sintesis.py debate-index docs/<slug> [carpeta]
  resultado-sintesis.py status docs/<slug> [carpeta]
  resultado-sintesis.py lint docs/<slug> [carpeta]
  resultado-sintesis.py stamp docs/<slug> <carpeta>

Lee el formulario vigente (resultados/formulario/latest.txt) y los ítems vigentes
(resultados/items/latest.txt). No edita el Excel ni items.json. No dibuja gráficas.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rsl_out import Fail, error, ok, run  # noqa: E402

try:
    from openpyxl import load_workbook
except ImportError as e:
    raise SystemExit("ERROR: falta openpyxl. Usa .venv-formulario (ver rsl-bootstrap).") from e

from formulario_placement import (  # noqa: E402
    SHEETS,
    column_index,
    ensure_placement,
    expected_traza_slots,
    placement_cell,
)

from formulario_lint_prosa import (  # noqa: E402
    lint_extraccion_manifest_complete,
    lint_traza_evidence,
    lint_traza_structure,
    load_traza_records,
    run_lint_prosa_checks,
)

FORMULARIO_BLOQUEANTE = "formulario-bloqueante.md"

ROOT = Path(__file__).resolve().parent.parent
FORMULARIO_ROOT = "resultados/formulario"
ITEMS_ROOT = "resultados/items"
SINTESIS_ROOT = "resultados/sintesis"
LATEST = "latest.txt"
FORMULARIO_XLSX = "Formulario.xlsx"
MAP_JSON = "formulario-map.json"
TRAZA_JSONL = "extraccion-traza.jsonl"
MATRIZ = "matriz.json"
BLOQUES = "bloques.json"
MANIFEST = "manifest.json"
OUT_MD = "sintesis-resultados.md"
DEBATE_MD = "sintesis-debate.md"
PLAN_BLOQUES = "plan-bloques"
FIRST_STUDY_COL = 3

BIBLIO_ROWS = {
    3: "doi",
    4: "titulo",
    5: "autores",
    6: "anio",
    7: "revista",
    8: "editorial",
    9: "pais",
    10: "contexto",
    11: "tipo_documento",
    12: "volumen",
    13: "muestra",
}

NR_TOKENS = {"", "—", "-", "nr", "n/r", "no reportado", "no reporta", "none"}

CONTINENTE = {
    # América del Norte
    "Estados Unidos": "América del Norte", "Canadá": "América del Norte", "México": "América del Norte",
    # América Latina
    "Perú": "América Latina", "Argentina": "América Latina", "Brasil": "América Latina", "Chile": "América Latina",
    "Colombia": "América Latina", "Ecuador": "América Latina", "Uruguay": "América Latina",
    "Venezuela": "América Latina", "Bolivia": "América Latina", "Paraguay": "América Latina",
    "Costa Rica": "América Latina", "Cuba": "América Latina", "Guatemala": "América Latina",
    "Panamá": "América Latina", "República Dominicana": "América Latina",
    # Europa
    "Reino Unido": "Europa", "España": "Europa", "Suiza": "Europa", "Italia": "Europa", "Finlandia": "Europa",
    "Grecia": "Europa", "Bélgica": "Europa", "República Checa": "Europa", "Polonia": "Europa",
    "Alemania": "Europa", "Rumanía": "Europa", "Países Bajos": "Europa", "Portugal": "Europa",
    "Francia": "Europa", "Irlanda": "Europa", "Suecia": "Europa", "Noruega": "Europa", "Dinamarca": "Europa",
    "Austria": "Europa", "Hungría": "Europa", "Eslovenia": "Europa", "Croacia": "Europa", "Serbia": "Europa",
    "Estonia": "Europa", "Letonia": "Europa", "Lituania": "Europa", "Islandia": "Europa", "Luxemburgo": "Europa",
    "Chipre": "Europa", "Malta": "Europa", "Eslovaquia": "Europa", "Bulgaria": "Europa", "Ucrania": "Europa",
    # Asia
    "China": "Asia", "Arabia Saudita": "Asia", "Indonesia": "Asia", "India": "Asia", "Bangladesh": "Asia",
    "Singapur": "Asia", "Corea del Sur": "Asia", "Japón": "Asia", "Emiratos Árabes Unidos": "Asia",
    "Israel": "Asia", "Turquía": "Asia", "Pakistán": "Asia", "Malasia": "Asia", "Irán": "Asia", "Catar": "Asia",
    "Jordania": "Asia", "Taiwán": "Asia", "Hong Kong": "Asia", "Vietnam": "Asia", "Tailandia": "Asia",
    "Filipinas": "Asia", "Omán": "Asia", "Kuwait": "Asia", "Líbano": "Asia", "Irak": "Asia", "Nepal": "Asia",
    "Sri Lanka": "Asia",
    # África
    "Sudáfrica": "África", "Egipto": "África", "Nigeria": "África", "Kenia": "África", "Marruecos": "África",
    "Túnez": "África", "Ghana": "África", "Etiopía": "África", "Argelia": "África",
    # Oceanía
    "Australia": "Oceanía", "Nueva Zelanda": "Oceanía",
}

PAIS_ALIAS = {
    "uae": "Emiratos Árabes Unidos", "united arab emirates": "Emiratos Árabes Unidos", "eau": "Emiratos Árabes Unidos",
    "usa": "Estados Unidos", "united states": "Estados Unidos", "ee. uu.": "Estados Unidos", "eeuu": "Estados Unidos",
    "uk": "Reino Unido", "united kingdom": "Reino Unido", "england": "Reino Unido", "inglaterra": "Reino Unido",
    "south korea": "Corea del Sur", "korea": "Corea del Sur", "qatar": "Catar", "netherlands": "Países Bajos",
    "holanda": "Países Bajos", "spain": "España", "germany": "Alemania", "italy": "Italia", "switzerland": "Suiza",
    "japan": "Japón", "brazil": "Brasil", "peru": "Perú", "mexico": "México", "canada": "Canadá",
    "saudi arabia": "Arabia Saudita", "south africa": "Sudáfrica", "romania": "Rumanía", "czech republic": "República Checa",
}

# Pistas de institución → país (afiliaciones que el enrich dejó sin país).
PAIS_PISTAS = {
    "colorado": "Estados Unidos", "california": "Estados Unidos", "harvard": "Estados Unidos",
    "stanford": "Estados Unidos", "mit ": "Estados Unidos", "oxford": "Reino Unido", "cambridge": "Reino Unido",
    "hansung": "Corea del Sur",
}

PARTICIPANTES_RE = re.compile(
    r"participantes?|personas?|usuari[oa]s?|estudiantes?|niñ[oa]s?|adult[oa]s?|jóvenes|docentes?|"
    r"profesores?|cuidadores?|familias?|pacientes?|expert[oa]s?|trabajador[ea]s?|alumn[oa]s?",
    re.I,
)

# Tono: términos evaluativos o de recomendación (WARN en lint).
TONO_EVALUATIVO = [
    "notable", "notablemente", "preocupante", "prometedor", "prometedora", "alarmante", "excelente",
    "sobresaliente", "impresionante", "lamentablemente", "afortunadamente", "desafortunadamente",
    "claramente superior", "el mejor", "la mejor", "los mejores", "las mejores", "es fundamental",
    "es crucial", "es imprescindible", "se recomienda", "se debería", "deberían", "debería", "es necesario que",
    "revolucionari", "innovador", "innovadora", "significativamente mejor", "evidencia sólida",
]

DETALLE_CAMPOS = [
    "Tipo", "Por qué este tipo", "Qué muestra", "Datos a dibujar", "Ejes",
    "Etiquetas sobre los datos", "Leyenda", "Nota del gráfico", "Estilo",
]
SPEC_KEYS = ["figura", "bloque", "titulo", "tipo", "motivo", "muestra", "datos", "ejes", "etiquetas", "leyenda", "nota", "estilo"]

PRESENTACIONES = {"tabla", "figura", "lista", "ambas", "texto"}
AGREGACIONES = {"frecuencia", "cruce", "descriptivo", "general"}
SINTESIS_TIPOS = {"aditiva", "refutacional", "argumental"}


# ───────────────────────── utilidades ─────────────────────────


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


def read_latest(root: Path) -> Path | None:
    latest = root / LATEST
    if not latest.is_file():
        return None
    name = latest.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    folder = root / name
    return folder if folder.is_dir() else None


def formulario_folder(theme: Path) -> Path:
    folder = read_latest(theme / FORMULARIO_ROOT)
    if folder is None or not (folder / FORMULARIO_XLSX).is_file() or not (folder / MAP_JSON).is_file():
        raise Fail("no hay formulario vigente (resultados/formulario/latest.txt)", "rsl-resultado-formulario-prepare + apply")
    return folder


def items_folder(theme: Path) -> Path:
    folder = read_latest(theme / ITEMS_ROOT)
    if folder is None or not (folder / "items.json").is_file():
        raise Fail("no hay ítems vigentes (resultados/items/latest.txt)", "rsl-resultado-items")
    return folder


def sintesis_root(theme: Path) -> Path:
    return theme / SINTESIS_ROOT


def resolve_folder(theme: Path, rest: list[str], *, allow_latest: bool = True) -> Path:
    extra = [a for a in rest if not a.startswith("--")]
    root = sintesis_root(theme)
    if extra:
        folder = root / extra[0].strip()
        if not (folder / MATRIZ).is_file():
            raise Fail(f"{rel(folder)} no es carpeta de síntesis", "sintesis:prepare")
        return folder
    if allow_latest:
        folder = read_latest(root)
        if folder is not None and (folder / MATRIZ).is_file():
            return folder
    if root.is_dir():
        cands = sorted(
            (p for p in root.iterdir() if p.is_dir() and re.match(r"^\d{4}-\d{2}-\d{2}-\d{4}$", p.name)),
            key=lambda p: p.name,
            reverse=True,
        )
        for c in cands:
            if (c / MATRIZ).is_file():
                return c
    raise Fail("no hay carpeta de síntesis", "pnpm -s sintesis:prepare docs/<slug>")


def load_json(path: Path) -> dict:
    if not path.is_file():
        raise Fail(f"falta {rel(path)}", None)
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def pct(n: int, base: int) -> int:
    return int(round(100 * n / base)) if base else 0


def is_nr(value) -> bool:
    if value is None:
        return True
    s = str(value).strip().strip(".").strip().casefold()
    return s in NR_TOKENS


def _campos(g: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for part in g.split("|"):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            out["_registro"] = (out.get("_registro", "") + "; " + part).strip("; ")
            continue
        k, v = part.split(":", 1)
        k, v = k.strip(), v.strip().rstrip(".").strip()
        if k:
            out[k] = v
    return out


def parse_plantilla(value: str) -> dict[str, str]:
    """Campos `Clave: valor | Clave: valor` (último paréntesis con «:») o primera frase con «|» y «:».

    Un tramo sin «:» dentro del grupo (p. ej. `LLM; ML | Modelo: NR`) va a la clave `_registro`.
    """
    if not value:
        return {}
    groups = re.findall(r"\(([^()]*:[^()]*)\)", value)
    for g in reversed(groups):
        out = _campos(g)
        if any(k != "_registro" for k in out):
            return out
    primera = registro_inicial(value)
    if "|" in primera and ":" in primera:
        out = _campos(primera)
        if any(k != "_registro" for k in out):
            return out
    return {}


def registro_inicial(value: str) -> str:
    """Primer tramo antes del primer punto (registro agregable de la celda)."""
    s = str(value or "").strip()
    m = re.match(r"^(.+?)(?:\.\s|\.$|$)", s)
    return (m.group(1) if m else s).strip()


def registro_categorias(value: str) -> str:
    """Registro a partir de la primera frase; si esta lleva una lista entre paréntesis, usa la lista."""
    primera = registro_inicial(value)
    grupos = [g for g in re.findall(r"\(([^()]*)\)", primera) if ":" not in g and "=" not in g]
    return grupos[-1] if grupos else primera


def norm_pais(raw: str) -> tuple[str, str]:
    """→ (país normalizado, continente). País de la primera afiliación reconocible."""
    if is_nr(raw):
        return "No reportado", "No reportado"
    for token in str(raw).split(";"):
        t = re.sub(r"\(.*?\)", "", token).strip().strip(".")
        if not t:
            continue
        key = t.casefold()
        cand = PAIS_ALIAS.get(key, t)
        if cand in CONTINENTE:
            return cand, CONTINENTE[cand]
        for pista, pais in PAIS_PISTAS.items():
            if pista in key:
                return pais, CONTINENTE[pais]
    return "No identificado", "No identificado"


def parse_muestra(raw: str) -> dict:
    s = str(raw or "").strip()
    if is_nr(s):
        return {"tipo": "nr", "n": None}
    if re.search(r"sin\s+(n|participantes)|revisión bibliográfica|sin participantes humanos|corpus", s, re.I):
        return {"tipo": "sin_participantes", "n": None}
    m = re.search(r"n\s*=\s*(\d[\d.,]*)", s, re.I)
    nums: list[int] = []
    if m:
        nums = [int(re.sub(r"[.,]", "", m.group(1)))]
    else:
        nums = [int(re.sub(r"[.,]", "", x)) for x in re.findall(r"(\d[\d.,]*)\s+(?=\w)", s)]
    nums = [x for x in nums if x > 0]
    if not nums:
        return {"tipo": "nr", "n": None}
    n = sum(nums) if not m else nums[0]
    tipo = "participantes" if PARTICIPANTES_RE.search(s) else "otro"
    return {"tipo": tipo, "n": n}


def item_short(item_id: str) -> str:
    return item_id.replace("/", "-")


def write_formulario_bloqueante(
    theme: Path,
    form: Path,
    *,
    gate_errs: list[str],
    gate_warns: list[str],
) -> None:
    """Escribe reporte reproducible cuando sintesis:prepare no puede continuar."""
    slug = rel(theme)
    folder_name = form.name
    lines: list[str] = [
        "# Formulario bloqueante — no continuar síntesis",
        "",
        f"**Tema:** `{slug}`",
        f"**Carpeta:** `resultados/formulario/{folder_name}/`",
        "",
        "## Por qué",
        "",
        "El formulario no supera el gate automático (`formulario:lint-traza`, `formulario:lint-prosa`, "
        "`manifest.extraccion_complete`). La síntesis no debe recodificar celdas ni corregir extracción aquí; "
        "corregir con **rsl-resultado-formulario-apply** y cerrar con `formulario:stamp`.",
        "",
        "## Errores (FAIL)",
        "",
    ]
    for i, e in enumerate(gate_errs, start=1):
        lines.append(f"{i}. {e}")
    if not gate_errs:
        lines.append("(ninguno — error inesperado)")
    lines += ["", "## Avisos (WARN)", ""]
    for w in gate_warns[:40]:
        lines.append(f"- {w}")
    if not gate_warns:
        lines.append("(ninguno)")
    lines += [
        "",
        "## Comandos",
        "",
        "```bash",
        f"pnpm -s formulario:lint-traza {slug} {folder_name}",
        f"pnpm -s formulario:lint-prosa {slug} {folder_name}",
        "```",
        "",
        "Tras corregir todos los FAIL: `pnpm -s formulario:stamp docs/<slug> <carpeta>` "
        "(marca `extraccion_complete` y actualiza `latest.txt`).",
        "",
        "## Prompt para rsl-resultado-formulario-apply",
        "",
        "```text",
        f"Usa rsl-resultado-formulario-apply sobre {slug}. ",
        "Corrige la extracción en los lotes afectados: evidencia con quote≥40 y loc concretos; ",
        "un valor no puede copiarse en dos item_id distintos del mismo estudio (salvo excepción en ",
        "manifest duplicate_value_whitelist). Vuelve a aplicar apply-lote, luego ",
        f"pnpm -s formulario:lint-traza {slug} {folder_name} y ",
        f"pnpm -s formulario:lint-prosa {slug} {folder_name}; cierra con ",
        f"pnpm -s formulario:stamp {slug} {folder_name}.",
        "```",
        "",
    ]
    (form / FORMULARIO_BLOQUEANTE).write_text("\n".join(lines) + "\n", encoding="utf-8")


def _gate_formulario_para_sintesis(theme: Path, form: Path, mp: dict, item_defs: dict) -> None:
    """Levanta Fail y escribe formulario-bloqueante.md si el formulario no califica."""
    gate_errs: list[str] = []
    gate_warns: list[str] = []

    gate_errs.extend(lint_extraccion_manifest_complete(form))

    traza_path = form / TRAZA_JSONL
    records, parse_err = load_traza_records(traza_path)
    if parse_err:
        gate_errs.append(parse_err)
    expected = expected_traza_slots(mp)
    if records is not None:
        tr_errs, _ = lint_traza_structure(records, expected)
        gate_errs.extend(tr_errs)
        gate_errs.extend(lint_traza_evidence(form, repo_root=ROOT))

    n_si = int(mp.get("n_si") or 0)
    prose_errs, prose_warns = run_lint_prosa_checks(
        form, item_defs, n_si=n_si, strict=True, check_evidence=False
    )
    gate_errs.extend(prose_errs)
    gate_warns.extend(prose_warns)

    if gate_errs:
        write_formulario_bloqueante(theme, form, gate_errs=gate_errs, gate_warns=gate_warns)
        preview = gate_errs[0][:200]
        raise Fail(
            f"formulario no válido para síntesis ({len(gate_errs)} FAIL). Primer error: {preview}",
            f"lee {rel(form / FORMULARIO_BLOQUEANTE)} y ejecuta rsl-resultado-formulario-apply",
        )


# ───────────────────────── prepare ─────────────────────────


def cmd_prepare(args: list[str]) -> int:
    if len(args) != 1:
        raise Fail("uso: resultado-sintesis.py prepare docs/<slug>", None, 2)
    theme = theme_path(args[0])
    form = formulario_folder(theme)
    itf = items_folder(theme)
    mp = json.loads((form / MAP_JSON).read_text(encoding="utf-8"))
    for s in mp.get("studies") or []:
        ensure_placement(s)
    items_data = json.loads((itf / "items.json").read_text(encoding="utf-8"))
    item_defs = {it["id"]: it for it in items_data.get("items") or []}
    _gate_formulario_para_sintesis(theme, form, mp, item_defs)
    bloq = form / FORMULARIO_BLOQUEANTE
    if bloq.is_file():
        bloq.unlink()

    wb = load_workbook(form / FORMULARIO_XLSX, read_only=True, data_only=True)
    slots_by_item: dict[str, list[dict]] = {}
    for slot in mp.get("items") or []:
        slots_by_item.setdefault(slot["item_id"], []).append(slot)

    estudios = []
    conflictos = []
    for st in sorted(mp.get("studies") or [], key=lambda x: int(x.get("si_order") or 0)):
        sheets = [sh for sh in SHEETS if placement_cell(st, sh)]
        if not sheets:
            continue
        sh0 = sheets[0]
        col0 = column_index(st, sh0, FIRST_STUDY_COL)
        ws0 = wb[sh0]
        biblio = {}
        for row, key in BIBLIO_ROWS.items():
            v = ws0.cell(row=row, column=col0).value
            biblio[key] = "" if v is None else str(v).strip()
        try:
            anio = int(str(biblio.get("anio") or "").strip()[:4])
        except ValueError:
            anio = None
        pais, continente = norm_pais(biblio.get("pais", ""))
        muestra = parse_muestra(biblio.get("muestra", ""))
        items_vals: dict[str, dict] = {}
        for item_id, slots in slots_by_item.items():
            vals = []
            for slot in slots:
                sh = slot["sheet"]
                if sh not in sheets:
                    continue
                col = column_index(st, sh, FIRST_STUDY_COL)
                v = wb[sh].cell(row=slot["row"], column=col).value
                vals.append((sh, "" if v is None else str(v).strip()))
            if not vals:
                continue
            sh_used, value = vals[0]
            if len(vals) > 1 and vals[0][1] != vals[1][1]:
                conflictos.append(
                    {"si_order": st["si_order"], "corpus_id": st["corpus_id"], "item_id": item_id,
                     "valores": {s: v for s, v in vals}}
                )
            items_vals[item_id] = {
                "valor": value,
                "hoja": sh_used,
                "nr": is_nr(value),
                "plantilla": parse_plantilla(value),
                "registro": registro_inicial(value) if not is_nr(value) else "",
            }
        estudios.append(
            {
                "si_order": int(st["si_order"]),
                "corpus_id": st["corpus_id"],
                "naturaleza": st.get("study_nature"),
                "hojas": sheets,
                "anio": anio,
                "pais": pais,
                "continente": continente,
                "pais_raw": biblio.get("pais", ""),
                "tipo_documento": biblio.get("tipo_documento", ""),
                "muestra": muestra,
                "muestra_raw": biblio.get("muestra", ""),
                "biblio": biblio,
                "items": items_vals,
            }
        )
    wb.close()

    items_meta = {}
    for item_id, d in item_defs.items():
        con_celda = [e for e in estudios if item_id in e["items"]]
        items_meta[item_id] = {
            "rq": d.get("rq"),
            "component": d.get("component"),
            "label": d.get("label"),
            "summary": d.get("summary"),
            "response_type": d.get("response_type"),
            "encoding": d.get("encoding"),
            "hojas": sorted({s["sheet"] for s in slots_by_item.get(item_id, [])}),
            "n_base": len(con_celda),
            "n_nr": sum(1 for e in con_celda if e["items"][item_id]["nr"]),
        }

    dest = dt.datetime.now().strftime("%Y-%m-%d-%H%M")
    folder = sintesis_root(theme) / dest
    for sub in ("debate", "tablas", "graficos", "codificacion"):
        (folder / sub).mkdir(parents=True, exist_ok=True)
    matriz = {
        "version": 1,
        "theme": rel(theme),
        "formulario": rel(form),
        "items": rel(itf / "items.json"),
        "N_total": len(estudios),
        "items_meta": items_meta,
        "conflictos_mixto": conflictos,
        "estudios": estudios,
    }
    write_json(folder / MATRIZ, matriz)
    bloques = {
        "version": 1,
        "nota": "Bloques B00 fijos (caracterización). Los bloques RQ los propone defensor-rsl (modo sintesis-bloques).",
        "bloques": [
            {"id": "B00-anio", "seccion": "3.1", "titulo": "Frecuencia de publicaciones por año",
             "items": [], "agregacion": "general", "sintesis": "aditiva", "presentacion": "figura",
             "motivo_presentacion": "Cambio en el tiempo"},
            {"id": "B00-enfoque", "seccion": "3.1", "titulo": "Enfoques metodológicos empleados",
             "items": [], "agregacion": "general", "sintesis": "aditiva", "presentacion": "texto",
             "motivo_presentacion": "Tres categorías; basta el texto"},
            {"id": "B00-tipo", "seccion": "3.1", "titulo": "Tipo de documento",
             "items": [], "agregacion": "general", "sintesis": "aditiva", "presentacion": "texto",
             "motivo_presentacion": "Dos categorías; basta el texto"},
            {"id": "B00-pais", "seccion": "3.1", "titulo": "Distribución geográfica de los estudios",
             "items": [], "agregacion": "general", "sintesis": "aditiva", "presentacion": "tabla",
             "motivo_presentacion": "Comparación simple de categorías de tamaño medio"},
            {"id": "B00-muestra", "seccion": "3.1", "titulo": "Tamaño de las muestras",
             "items": [], "agregacion": "general", "sintesis": "aditiva", "presentacion": "texto",
             "motivo_presentacion": "Rango y mediana; basta el texto"},
        ],
    }
    write_json(folder / BLOQUES, bloques)
    write_json(
        folder / MANIFEST,
        {
            "theme": rel(theme),
            "formulario": rel(form),
            "formulario_sha": file_sha(form / FORMULARIO_XLSX),
            "items": rel(itf / "items.json"),
            "items_sha": file_sha(itf / "items.json"),
            "N_total": len(estudios),
            "prepared": dt.datetime.now().isoformat(timespec="minutes"),
            "stamped": None,
            "rondas_3": [],
        },
    )
    msg = f"prepare {rel(folder)} ({len(estudios)} estudios, {len(items_meta)} ítems)"
    if conflictos:
        print(f"WARN {len(conflictos)} celda(s) de estudios mixtos difieren entre hojas (ver matriz.conflictos_mixto)")
    for iid, m in items_meta.items():
        print(f"  {iid}: base {m['n_base']} estudios (hojas: {', '.join(m['hojas'])}), NR {m['n_nr']}")
    return ok(msg, "pnpm -s sintesis:general docs/<slug>")


# ───────────────────────── general (3.1) ─────────────────────────


def _tabla_md(titulo: str, filas: list[tuple[str, int, int]], col: str, nota: str) -> str:
    out = [f"*{titulo}*", "", f"| {col} | Frecuencia (n) | Porcentaje |", "|---|---|---|"]
    for cat, n, p in filas:
        out.append(f"| {cat} | {n} | {p}% |")
    out += ["", f"*Nota.* {nota}", ""]
    return "\n".join(out)


def _cats(counter: Counter, estudios_por: dict, base: int, orden=None) -> list[dict]:
    keys = orden if orden is not None else [k for k, _ in counter.most_common()]
    return [
        {"categoria": k, "n": counter[k], "pct": pct(counter[k], base), "estudios": sorted(estudios_por.get(k, []))}
        for k in keys
        if counter[k]
    ]


def cmd_general(args: list[str]) -> int:
    if len(args) < 1:
        raise Fail("uso: resultado-sintesis.py general docs/<slug> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = resolve_folder(theme, args[1:])
    mx = load_json(folder / MATRIZ)
    est = mx["estudios"]
    N = len(est)
    tablas = folder / "tablas"
    anios_validos = [e["anio"] for e in est if e["anio"]]
    periodo = f"{min(anios_validos)}–{max(anios_validos)}" if anios_validos else "s. f."

    def por(key_fn):
        c, ids = Counter(), {}
        for e in est:
            k = key_fn(e)
            c[k] += 1
            ids.setdefault(k, []).append(e["si_order"])
        return c, ids

    # Año
    c, ids = por(lambda e: str(e["anio"]) if e["anio"] else "No reportado")
    orden = sorted([k for k in c if k != "No reportado"]) + (["No reportado"] if "No reportado" in c else [])
    cats = _cats(c, ids, N, orden)
    nat = {}
    for e in est:
        k = str(e["anio"]) if e["anio"] else "No reportado"
        nat.setdefault(k, Counter())[e["naturaleza"] or "NR"] += 1
    for cat in cats:
        cat["por_naturaleza"] = dict(nat.get(cat["categoria"], {}))
    pico = max(cats, key=lambda x: x["n"]) if cats else None
    data = {"bloque": "B00-anio", "tipo": "general", "base": {"N": N, "descripcion": "estudios incluidos"},
            "periodo": periodo, "pico": pico and {"anio": pico["categoria"], "n": pico["n"], "pct": pico["pct"]},
            "categorias": cats}
    write_json(tablas / "B00-anio.json", data)
    (tablas / "B00-anio.md").write_text(
        _tabla_md("Distribución de los estudios por año de publicación",
                  [(x["categoria"], x["n"], x["pct"]) for x in cats], "Año",
                  f"Datos extraídos de los {N} artículos seleccionados ({periodo})."),
        encoding="utf-8")

    # Enfoque
    etiqueta = {"cuantitativo": "Cuantitativo", "cualitativo": "Cualitativo", "mixto": "Mixto"}
    c, ids = por(lambda e: etiqueta.get(e["naturaleza"] or "", "No clasificado"))
    cats = _cats(c, ids, N)
    write_json(tablas / "B00-enfoque.json",
               {"bloque": "B00-enfoque", "tipo": "general", "base": {"N": N, "descripcion": "estudios incluidos"},
                "categorias": cats})
    (tablas / "B00-enfoque.md").write_text(
        _tabla_md("Enfoque metodológico de los estudios", [(x["categoria"], x["n"], x["pct"]) for x in cats],
                  "Enfoque", f"Datos extraídos de los {N} artículos seleccionados."), encoding="utf-8")

    # Tipo de documento
    alias_tipo = {"article": "Artículo de revista", "conference paper": "Artículo de congreso",
                  "review": "Revisión", "book chapter": "Capítulo de libro"}
    c, ids = por(lambda e: alias_tipo.get((e["tipo_documento"] or "").strip().casefold(),
                                          e["tipo_documento"] or "No reportado"))
    cats = _cats(c, ids, N)
    write_json(tablas / "B00-tipo.json",
               {"bloque": "B00-tipo", "tipo": "general", "base": {"N": N, "descripcion": "estudios incluidos"},
                "categorias": cats})
    (tablas / "B00-tipo.md").write_text(
        _tabla_md("Tipo de documento", [(x["categoria"], x["n"], x["pct"]) for x in cats], "Tipo",
                  f"Datos extraídos de los {N} artículos seleccionados."), encoding="utf-8")

    # País y continente
    cc, cids = por(lambda e: e["continente"])
    cp, pids = por(lambda e: e["pais"])
    cats_c = _cats(cc, cids, N)
    cats_p = _cats(cp, pids, N)
    no_ident = [e["si_order"] for e in est if e["pais"] == "No identificado"]
    write_json(tablas / "B00-pais.json",
               {"bloque": "B00-pais", "tipo": "general", "base": {"N": N, "descripcion": "estudios incluidos"},
                "criterio": "país de la primera afiliación reconocible (fila 9 del formulario)",
                "categorias": cats_c, "paises": cats_p, "no_identificados": no_ident})
    md = _tabla_md("Distribución de los estudios por continente",
                   [(x["categoria"], x["n"], x["pct"]) for x in cats_c], "Continente",
                   f"Datos extraídos de los {N} artículos seleccionados; país de la afiliación del primer autor.")
    md += "\n" + _tabla_md("Distribución de los estudios por país",
                           [(x["categoria"], x["n"], x["pct"]) for x in cats_p], "País",
                           f"Datos extraídos de los {N} artículos seleccionados.")
    (tablas / "B00-pais.md").write_text(md, encoding="utf-8")

    # Muestra
    part = [e for e in est if e["muestra"]["tipo"] == "participantes" and e["muestra"]["n"]]
    otros = [e for e in est if e["muestra"]["tipo"] == "otro"]
    sin_p = [e for e in est if e["muestra"]["tipo"] == "sin_participantes"]
    nr = [e for e in est if e["muestra"]["tipo"] == "nr"]
    ns = sorted(e["muestra"]["n"] for e in part)
    cats = [
        {"categoria": "Con participantes humanos (n reportado)", "n": len(part), "pct": pct(len(part), N),
         "estudios": [e["si_order"] for e in part]},
        {"categoria": "Muestra no humana (respuestas, textos, sesiones)", "n": len(otros), "pct": pct(len(otros), N),
         "estudios": [e["si_order"] for e in otros]},
        {"categoria": "Sin participantes humanos", "n": len(sin_p), "pct": pct(len(sin_p), N),
         "estudios": [e["si_order"] for e in sin_p]},
        {"categoria": "No reportado", "n": len(nr), "pct": pct(len(nr), N), "estudios": [e["si_order"] for e in nr]},
    ]
    cats = [x for x in cats if x["n"]]
    rango = {"min": ns[0], "max": ns[-1], "mediana": statistics.median(ns)} if ns else None
    write_json(tablas / "B00-muestra.json",
               {"bloque": "B00-muestra", "tipo": "general", "base": {"N": N, "descripcion": "estudios incluidos"},
                "rango_participantes": rango, "categorias": cats})
    md = _tabla_md("Tamaño de las muestras", [(x["categoria"], x["n"], x["pct"]) for x in cats], "Tipo de muestra",
                   f"Datos extraídos de los {N} artículos seleccionados.")
    if rango:
        md += f"\nRango de participantes: {rango['min']}–{rango['max']} (mediana {rango['mediana']}).\n"
    (tablas / "B00-muestra.md").write_text(md, encoding="utf-8")

    if no_ident:
        print(f"WARN {len(no_ident)} estudio(s) con país no identificado (si_order {no_ident}); revisa fila 9 del formulario")
    return ok(f"general: tablas B00 (año, enfoque, tipo, país, muestra) sobre N = {N}",
              "defensor-rsl modo sintesis-bloques → bloques.json; luego sintesis:codify-auto")


# ───────────────────────── codificación ─────────────────────────


def _auto_categorias(item: dict) -> tuple[list[str], dict, bool]:
    """→ (categorías, valores numéricos, revisar)."""
    pl = item.get("plantilla") or {}
    valores: dict = {}
    if pl:
        cats = []
        for k, v in pl.items():
            if k == "_registro":
                for part in v.split(";"):
                    part = part.strip().strip(".")
                    if part and not is_nr(part):
                        cats.append(part[:1].upper() + part[1:])
                continue
            if k.casefold() in {"n", "valor"}:
                valores[k] = "NR" if is_nr(v) else v
                continue
            if is_nr(v):
                cats.append(f"{k}: NR")
                continue
            for part in v.split(";"):
                part = part.strip()
                if part:
                    cats.append(f"{k}: {part[:1].upper() + part[1:]}")
        return cats, valores, False
    reg = registro_categorias(item.get("valor") or "")
    parts = [p.strip().strip(".").strip() for p in reg.split(";")]
    cats = [p[:1].upper() + p[1:] for p in parts if p and not is_nr(p)]
    revisar = not cats or any(len(c) > 50 for c in cats)
    return cats, valores, revisar


def cmd_codify_auto(args: list[str]) -> int:
    if len(args) < 2:
        raise Fail("uso: resultado-sintesis.py codify-auto docs/<slug> <ITEM|all> [carpeta] [--force]", None, 2)
    theme = theme_path(args[0])
    target = args[1].strip()
    force = "--force" in args
    folder = resolve_folder(theme, args[2:])
    mx = load_json(folder / MATRIZ)
    ids = list(mx["items_meta"]) if target.lower() == "all" else [target]
    written, revisar_total = 0, 0
    for item_id in ids:
        if item_id not in mx["items_meta"]:
            raise Fail(f"ítem {item_id} no existe en items.json", None)
        out = folder / "codificacion" / f"{item_short(item_id)}.jsonl"
        if out.is_file() and not force:
            print(f"  {item_id}: ya codificado (usa --force para regenerar)")
            continue
        lines = []
        for e in mx["estudios"]:
            it = e["items"].get(item_id)
            if it is None:
                continue
            if it["nr"]:
                cats, valores, revisar = [], {}, False
            else:
                cats, valores, revisar = _auto_categorias(it)
            revisar_total += int(revisar)
            lines.append(
                json.dumps(
                    {"si_order": e["si_order"], "corpus_id": e["corpus_id"], "naturaleza": e["naturaleza"],
                     "valor": it["valor"], "categorias": cats, "valores": valores, "nr": it["nr"],
                     "auto": True, "revisar": revisar},
                    ensure_ascii=False,
                )
            )
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        written += 1
    return ok(
        f"codify-auto: {written} ítem(s) codificados automáticamente; {revisar_total} fila(s) marcadas «revisar»",
        "defensor-rsl y critico-rsl revisan codebook.md y codificacion/*.jsonl; luego sintesis:aggregate",
    )


def load_codificacion(folder: Path, item_id: str) -> list[dict]:
    path = folder / "codificacion" / f"{item_short(item_id)}.jsonl"
    if not path.is_file():
        raise Fail(f"falta {rel(path)}", f"pnpm -s sintesis:codify-auto docs/<slug> {item_id} y revisión de agentes")
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


# ───────────────────────── agregación ─────────────────────────


def _filtrar_campo(cats: list[str], campo: str | None) -> list[str]:
    """`campo` = subcampo de plantilla (p. ej. «Rol»); «_registro» = solo categorías sin «Clave:»."""
    if not campo:
        return cats
    if campo == "_registro":
        return [c for c in cats if not re.match(r"^[^:]{1,30}:\s", c)]
    pref = f"{campo}:".casefold()
    return [c.split(":", 1)[1].strip() for c in cats if c.casefold().startswith(pref)]


def _freq(rows: list[dict], campo: str | None, excluir: list[str] | None = None) -> dict:
    base = len(rows)
    c, ids, nat = Counter(), {}, {}
    nr_ids = []
    fuera = set(excluir or [])
    for r in rows:
        cats = [] if r.get("nr") else _filtrar_campo(r.get("categorias") or [], campo)
        cats = [x for x in cats if not is_nr(x) and x not in fuera]
        if not cats:
            nr_ids.append(r["si_order"])
            continue
        for cat in dict.fromkeys(cats):
            c[cat] += 1
            ids.setdefault(cat, []).append(r["si_order"])
            nat.setdefault(cat, Counter())[r.get("naturaleza") or "NR"] += 1
    cats_out = [
        {"categoria": k, "n": n, "pct": pct(n, base), "por_naturaleza": dict(nat[k]), "estudios": sorted(ids[k])}
        for k, n in c.most_common()
    ]
    return {"base": base, "categorias": cats_out, "nr": {"n": len(nr_ids), "pct": pct(len(nr_ids), base),
                                                          "estudios": sorted(nr_ids)},
            "multivalor": sum(x["n"] for x in cats_out) > (base - len(nr_ids))}


def _cruce(rows_a: list[dict], rows_b: list[dict], campo_a: str | None, campo_b: str | None,
           excluir_a: list[str] | None = None, excluir_b: list[str] | None = None) -> dict:
    by_a = {r["si_order"]: r for r in rows_a}
    by_b = {r["si_order"]: r for r in rows_b}
    comunes = sorted(set(by_a) & set(by_b))
    filas, cols = Counter(), Counter()
    celdas: dict[tuple[str, str], list[int]] = {}
    con_ambos = 0
    fa, fb = set(excluir_a or []), set(excluir_b or [])
    for si in comunes:
        ca = [x for x in _filtrar_campo(by_a[si].get("categorias") or [], campo_a) if not is_nr(x) and x not in fa]
        cb = [x for x in _filtrar_campo(by_b[si].get("categorias") or [], campo_b) if not is_nr(x) and x not in fb]
        if by_a[si].get("nr") or by_b[si].get("nr") or not ca or not cb:
            continue
        con_ambos += 1
        for x in dict.fromkeys(ca):
            filas[x] += 1
            for y in dict.fromkeys(cb):
                celdas.setdefault((x, y), []).append(si)
        for y in dict.fromkeys(cb):
            cols[y] += 1
    f_orden = [k for k, _ in filas.most_common()]
    c_orden = [k for k, _ in cols.most_common()]
    matriz = [[len(celdas.get((f, c), [])) for c in c_orden] for f in f_orden]
    return {
        "base": con_ambos,
        "base_descripcion": "estudios con dato en ambos ítems",
        "filas": f_orden,
        "columnas": c_orden,
        "matriz": matriz,
        "estudios": {f"{f} × {c}": sorted(v) for (f, c), v in celdas.items()},
    }


def _bloque_tabla_md(bloque: dict, data: dict) -> str:
    out = [f"### {bloque['id']} — {bloque.get('titulo', '')}", ""]
    if data["tipo"] == "cruce":
        cr = data["cruce"]
        out.append(f"*{bloque.get('titulo', 'Cruce')} (N.º de estudios; base n={cr['base']})*")
        out.append("")
        out.append("| Categoría | " + " | ".join(cr["columnas"]) + " |")
        out.append("|---|" + "---|" * len(cr["columnas"]))
        for f, row in zip(cr["filas"], cr["matriz"]):
            out.append(f"| {f} | " + " | ".join(str(x) for x in row) + " |")
        out.append("")
    for it in data["items"]:
        out.append(f"*{it['item_id']} — {it['label']} (base n={it['base']})*")
        out.append("")
        out.append("| Categoría | Frecuencia (n) | Porcentaje | Cuant. | Cual. | Mixto |")
        out.append("|---|---|---|---|---|---|")
        for cat in it["categorias"]:
            pn = cat["por_naturaleza"]
            out.append(
                f"| {cat['categoria']} | {cat['n']} | {cat['pct']}% | {pn.get('cuantitativo', 0)} | "
                f"{pn.get('cualitativo', 0)} | {pn.get('mixto', 0)} |"
            )
        if it["nr"]["n"]:
            out.append(f"| No reportado | {it['nr']['n']} | {it['nr']['pct']}% | | | |")
        out.append("")
        if it["multivalor"]:
            out.append("*Nota.* Un estudio puede reportar más de una categoría; los porcentajes no suman 100%.")
            out.append("")
    return "\n".join(out)


def aggregate_bloque(folder: Path, mx: dict, bloque: dict) -> dict:
    items = bloque.get("items") or []
    campos = bloque.get("campos") or {}
    excluir = bloque.get("excluir") or {}
    if not items:
        raise Fail(f"bloque {bloque['id']} sin ítems", "revisa bloques.json")
    items_out = []
    rows_by_item = {}
    for item_id in items:
        rows = load_codificacion(folder, item_id)
        rows_by_item[item_id] = rows
        fr = _freq(rows, campos.get(item_id), excluir.get(item_id))
        meta = mx["items_meta"].get(item_id, {})
        items_out.append({"item_id": item_id, "label": meta.get("label", ""), "campo": campos.get(item_id),
                          "hojas": meta.get("hojas", []), **fr})
    data = {"bloque": bloque["id"], "tipo": bloque.get("agregacion", "frecuencia"), "items": items_out,
            "base": {"N": items_out[0]["base"], "descripcion": "estudios con el ítem en el formulario"}}
    if bloque.get("agregacion") == "cruce":
        if len(items) < 2:
            raise Fail(f"bloque {bloque['id']}: un cruce necesita 2 ítems", "revisa bloques.json")
        data["cruce"] = _cruce(rows_by_item[items[0]], rows_by_item[items[1]],
                               campos.get(items[0]), campos.get(items[1]),
                               excluir.get(items[0]), excluir.get(items[1]))
        if excluir:
            data["cruce"]["excluidas"] = excluir
    write_json(folder / "tablas" / f"{bloque['id']}.json", data)
    (folder / "tablas" / f"{bloque['id']}.md").write_text(_bloque_tabla_md(bloque, data), encoding="utf-8")
    return data


def validate_bloques(bj: dict, mx: dict) -> list[str]:
    errs = []
    seen = set()
    for b in bj.get("bloques") or []:
        bid = b.get("id")
        if not bid or bid in seen:
            errs.append(f"E: bloque sin id o duplicado ({bid})")
            continue
        seen.add(bid)
        if b.get("agregacion") not in AGREGACIONES:
            errs.append(f"E: {bid} agregacion «{b.get('agregacion')}» no válida ({', '.join(sorted(AGREGACIONES))})")
        if b.get("presentacion") not in PRESENTACIONES:
            errs.append(f"E: {bid} presentacion «{b.get('presentacion')}» no válida")
        if b.get("sintesis") not in SINTESIS_TIPOS:
            errs.append(f"E: {bid} sintesis «{b.get('sintesis')}» no válida (aditiva/refutacional/argumental)")
        if not b.get("motivo_presentacion"):
            errs.append(f"E: {bid} sin motivo_presentacion")
        for it in b.get("items") or []:
            if it not in mx["items_meta"]:
                errs.append(f"E: {bid} ítem {it} no existe en items.json")
        if b.get("agregacion") != "general" and not b.get("items"):
            errs.append(f"E: {bid} sin ítems")
    cubiertos = {it for b in bj.get("bloques") or [] for it in b.get("items") or []}
    for it in mx["items_meta"]:
        if it not in cubiertos:
            errs.append(f"E: ítem {it} no aparece en ningún bloque (todo ítem se sintetiza, solo o agrupado)")
    return errs


def cmd_aggregate(args: list[str]) -> int:
    if len(args) < 2:
        raise Fail("uso: resultado-sintesis.py aggregate docs/<slug> <BLOQUE|all> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = resolve_folder(theme, args[2:])
    mx = load_json(folder / MATRIZ)
    bj = load_json(folder / BLOQUES)
    errs = [e for e in validate_bloques(bj, mx) if e.startswith("E") and "no aparece en ningún bloque" not in e]
    if errs:
        for e in errs:
            print(e)
        return error("bloques.json inválido", "corrige bloques.json (defensor + crítico)")
    target = args[1].strip()
    bloques = [b for b in bj["bloques"] if b.get("agregacion") != "general"]
    if target.lower() != "all":
        bloques = [b for b in bloques if b["id"] == target]
        if not bloques:
            raise Fail(f"bloque {target} no está en bloques.json (o es B00, que calcula sintesis:general)", None)
    for b in bloques:
        data = aggregate_bloque(folder, mx, b)
        resumen = "; ".join(f"{it['item_id']} base {it['base']}, {len(it['categorias'])} cat." for it in data["items"])
        print(f"  {b['id']}: {resumen}")
    return ok(f"aggregate: {len(bloques)} bloque(s) → tablas/", "sintesis:borrador <bloque> y debate R1")


# ───────────────────────── borrador ─────────────────────────


def _spec_borrador(bloque: dict, data: dict, N: int, periodo: str) -> dict:
    if data.get("tipo") == "cruce":
        cr = data["cruce"]
        datos = {"filas": cr["filas"], "columnas": cr["columnas"], "matriz": cr["matriz"]}
        tipo = "mapa de calor"
        ejes = {"x": f"Categorías de {bloque['items'][1]}", "y": f"Categorías de {bloque['items'][0]}",
                "unidad": "N.º de estudios"}
        etiquetas = "Número de estudios en cada celda"
        leyenda = "Barra de color: número de estudios coincidentes"
    elif data.get("tipo") == "general":
        datos = [{"categoria": c["categoria"], "n": c["n"], "pct": c["pct"]} for c in data["categorias"]]
        tipo = "barras verticales"
        ejes = {"x": "Categoría", "y": "Porcentaje de estudios", "unidad": "%"}
        etiquetas = "X% (n=Y) sobre cada barra"
        leyenda = "Sin leyenda (una sola serie)"
    else:
        it = data["items"][0]
        datos = [{"categoria": c["categoria"], "n": c["n"], "pct": c["pct"]} for c in it["categorias"]]
        tipo = "barras horizontales"
        ejes = {"x": "Porcentaje de estudios", "y": "Categoría (orden descendente por n)", "unidad": "%"}
        etiquetas = "X% (n=Y) al final de cada barra"
        leyenda = "Sin leyenda (una sola serie)"
    return {
        "figura": None,
        "bloque": bloque["id"],
        "titulo": bloque.get("titulo", ""),
        "tipo": tipo,
        "motivo": bloque.get("motivo_presentacion", ""),
        "muestra": "",
        "datos": datos,
        "ejes": ejes,
        "etiquetas": etiquetas,
        "leyenda": leyenda,
        "nota": f"Elaboración propia a partir de los {N} artículos seleccionados ({periodo}).",
        "estilo": {"paleta": "azules sobrios", "orden": "descendente por n", "tamano": "16x9 cm"},
    }


def cmd_borrador(args: list[str]) -> int:
    if len(args) < 2:
        raise Fail("uso: resultado-sintesis.py borrador docs/<slug> <BLOQUE> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = resolve_folder(theme, args[2:])
    mx = load_json(folder / MATRIZ)
    bj = load_json(folder / BLOQUES)
    bid = args[1].strip()
    bloque = next((b for b in bj["bloques"] if b["id"] == bid), None)
    if bloque is None:
        raise Fail(f"bloque {bid} no está en bloques.json", None)
    tpath = folder / "tablas" / f"{bid}.json"
    if not tpath.is_file():
        raise Fail(f"falta {rel(tpath)}", "sintesis:general (B00) o sintesis:aggregate <bloque>")
    data = load_json(tpath)
    N = mx["N_total"]
    anios = [e["anio"] for e in mx["estudios"] if e["anio"]]
    periodo = f"{min(anios)}–{max(anios)}" if anios else "s. f."
    deb = folder / "debate" / bid
    deb.mkdir(parents=True, exist_ok=True)
    md_tabla = (folder / "tablas" / f"{bid}.md").read_text(encoding="utf-8")
    lines = [
        f"# Borrador de datos — {bid}: {bloque.get('titulo', '')}",
        "",
        "Material de partida para la ronda 1 (no es prosa final). Las cifras salen de "
        f"`tablas/{bid}.json`; no se cambian en el debate sin volver a agregar.",
        "",
        f"- Sección: {bloque.get('seccion') or bloque.get('rq', '')}",
        f"- Agregación: {bloque.get('agregacion')} · Síntesis: {bloque.get('sintesis')} · "
        f"Presentación: {bloque.get('presentacion')} ({bloque.get('motivo_presentacion', '')})",
        f"- N total de estudios incluidos: {N} · periodo {periodo}",
        "",
        "## Tabla de datos",
        "",
        md_tabla,
    ]
    if bloque.get("presentacion") in {"figura", "ambas"}:
        spec = _spec_borrador(bloque, data, N, periodo)
        write_json(deb / "spec-borrador.json", spec)
        lines += ["", "## Spec de gráfica (borrador)", "", f"Ver `debate/{bid}/spec-borrador.json`."]
    (deb / "borrador.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return ok(f"borrador {rel(deb / 'borrador.md')}", "R1 defensor-rsl (modo sintesis-resultado)")


# ───────────────────────── debate ─────────────────────────


def _veredicto(folder: Path, bid: str) -> tuple[dict | None, list[str]]:
    errs = []
    deb = folder / "debate" / bid
    for f in ("r1-defensor.md", "r1-critico.md", "r2-defensor.md", "r2-critico.md"):
        if not (deb / f).is_file():
            errs.append(f"E: {bid} falta debate/{bid}/{f} (dos rondas obligatorias)")
    vpath = deb / "veredicto.json"
    if not vpath.is_file():
        errs.append(f"E: {bid} falta debate/{bid}/veredicto.json (orquestador-sintesis-rsl)")
        return None, errs
    v = json.loads(vpath.read_text(encoding="utf-8"))
    rondas = v.get("rondas")
    if rondas not in (2, 3):
        errs.append(f"E: {bid} veredicto.rondas debe ser 2 o 3")
    if v.get("acuerdo_r2") is True and rondas != 2:
        errs.append(f"E: {bid} hubo acuerdo en R2 pero rondas = {rondas}")
    if v.get("acuerdo_r2") is False:
        if rondas != 3:
            errs.append(f"E: {bid} sin acuerdo en R2 exige tercera ronda (rondas = 3)")
        for f in ("r3-defensor.md", "r3-critico.md"):
            if not (deb / f).is_file():
                errs.append(f"E: {bid} falta debate/{bid}/{f} (tercera ronda)")
        if v.get("cierre") not in ("consenso_r3", "orquestador_r3"):
            errs.append(f"E: {bid} cierre de R3 debe ser consenso_r3 u orquestador_r3")
        if v.get("cierre") == "orquestador_r3" and not v.get("desacuerdo_residual"):
            errs.append(f"E: {bid} cierre del orquestador sin desacuerdo_residual")
    elif v.get("acuerdo_r2") is not True:
        errs.append(f"E: {bid} veredicto.acuerdo_r2 debe ser true o false")
    if not v.get("resumen"):
        errs.append(f"E: {bid} veredicto sin resumen")
    return v, errs


def frase_r3(bid: str, v: dict) -> str:
    cierre = (
        "cierre por consenso en la tercera ronda"
        if v.get("cierre") == "consenso_r3"
        else f"cierre del orquestador con desacuerdo residual: {v.get('desacuerdo_residual', '')}"
    )
    return (f"Bloque {bid}: requirió una tercera ronda final porque no hubo acuerdo en la segunda; {cierre}.")


def cmd_debate_index(args: list[str]) -> int:
    if len(args) < 1:
        raise Fail("uso: resultado-sintesis.py debate-index docs/<slug> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = resolve_folder(theme, args[1:])
    bj = load_json(folder / BLOQUES)
    r3, secciones, pendientes = [], [], []
    plan = {"id": PLAN_BLOQUES, "titulo": "Plan de bloques (qué ítems van solos o agrupados)"}
    for b in [plan] + bj["bloques"]:
        bid = b["id"]
        v, errs = _veredicto(folder, bid)
        if v is None:
            pendientes.append(bid)
            continue
        if v.get("rondas") == 3:
            r3.append(frase_r3(bid, v))
        rondas = ["r1-defensor", "r1-critico", "r2-defensor", "r2-critico"]
        if v.get("rondas") == 3:
            rondas += ["r3-defensor", "r3-critico"]
        sec = [f"## Bloque {bid} — {b.get('titulo', '')}", ""]
        sec.append(f"- Rondas: {v.get('rondas')} · acuerdo en R2: {'sí' if v.get('acuerdo_r2') else 'no'}"
                   + (f" · cierre: {v.get('cierre')}" if v.get("rondas") == 3 else ""))
        sec.append("- Archivos: " + ", ".join(f"[`{r}`](debate/{bid}/{r}.md)" for r in rondas)
                   + f", [`veredicto.json`](debate/{bid}/veredicto.json)")
        sec.append(f"- Veredicto del orquestador: {v.get('resumen')}")
        if v.get("desacuerdo_residual"):
            sec.append(f"- Desacuerdo residual: {v['desacuerdo_residual']}")
        if errs:
            sec.append("- Incidencias: " + "; ".join(errs))
        secciones.append("\n".join(sec) + "\n")
    out = ["# Debate de la síntesis de resultados", "",
           "Proponente: defensor-rsl · Debate: critico-rsl · Cierre: orquestador-sintesis-rsl. "
           "Dos rondas obligatorias por bloque; tercera ronda final solo si no hubo acuerdo en la segunda.", "",
           "## Bloques con tercera ronda", ""]
    out += [f"- {x}" for x in r3] if r3 else ["Ninguno: todos los bloques cerraron con acuerdo en la segunda ronda."]
    out.append("")
    if pendientes:
        out += ["## Bloques sin veredicto", "", *[f"- {p}" for p in pendientes], ""]
    out += secciones
    (folder / DEBATE_MD).write_text("\n".join(out), encoding="utf-8")
    return ok(f"debate-index → {rel(folder / DEBATE_MD)} ({len(secciones)} cerrados, {len(pendientes)} pendientes, "
              f"{len(r3)} con R3)", "sintesis:lint")


# ───────────────────────── status ─────────────────────────


def cmd_status(args: list[str]) -> int:
    if len(args) < 1:
        raise Fail("uso: resultado-sintesis.py status docs/<slug> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = resolve_folder(theme, args[1:])
    mx = load_json(folder / MATRIZ)
    bj = load_json(folder / BLOQUES)
    print(f"Carpeta: {rel(folder)} · N = {mx['N_total']}")
    for b in bj["bloques"]:
        bid = b["id"]
        t = (folder / "tablas" / f"{bid}.json").is_file()
        v = (folder / "debate" / bid / "veredicto.json").is_file()
        print(f"  {bid:14s} tabla {'sí' if t else 'no'} · veredicto {'sí' if v else 'no'} · {b.get('titulo', '')}")
    cod = sorted(p.stem for p in (folder / "codificacion").glob("*.jsonl"))
    print(f"  codificación: {', '.join(cod) or 'ninguna'}")
    print(f"  {OUT_MD}: {'sí' if (folder / OUT_MD).is_file() else 'no'}")
    return ok("status")


# ───────────────────────── lint ─────────────────────────

CITA_PATTERNS = [
    (re.compile(r"\[\d+(?:[–,-]\s*\d+)*\]"), "cita numérica [n] a un estudio"),
    (re.compile(r"\([A-ZÁÉÍÓÚÑ][\wáéíóúñ'-]+(?:\s+(?:et al\.|y|&)\s*[A-ZÁÉÍÓÚÑ]?[\wáéíóúñ'-]*)?,\s*\d{4}[a-z]?\)"),
     "cita autor-año"),
    (re.compile(r"\bet al\.?"), "«et al.»"),
    (re.compile(r"\bR\d{3,4}\b"), "identificador del corpus (Rnnn)"),
]
AUTOR_PATTERNS = [
    (re.compile(r"\b[Ee]l (?:estudio|trabajo|artículo) de [A-ZÁÉÍÓÚ]"), "párrafo centrado en autor («el estudio de X»)"),
    (re.compile(r"\b[Ss]egún [A-ZÁÉÍÓÚ][a-záéíóú]+\b(?! (?:la|el|los|las)\b)"), "párrafo centrado en autor («según X»)"),
    (re.compile(r"\b[A-ZÁÉÍÓÚ][a-záéíóú]+ \(\d{4}\)"), "autor con año entre paréntesis"),
]
PCT_N_RE = re.compile(r"(\d+(?:[.,]\d+)?)\s*%\s*\(\s*n\s*=\s*(\d+)\s*\)")
N_PCT_RE = re.compile(r"(\d+)\s+(?:de los \d+\s+)?(?:estudios|artículos|investigaciones|trabajos)\s*\(\s*(\d+(?:[.,]\d+)?)\s*%\s*\)")


def _strip_detalles(md: str) -> str:
    """Quita las subsecciones «Detalle gráfica» (material de trabajo) del texto a revisar."""
    return re.sub(r"(?ms)^#{2,5} Detalle gráfica.*?(?=^#{1,5} |\Z)", "", md)


def lint_folder(folder: Path) -> tuple[list[str], list[str]]:
    errs, warns = [], []
    mx = load_json(folder / MATRIZ)
    bj = load_json(folder / BLOQUES)
    for e in validate_bloques(bj, mx):
        (errs if e.startswith("E") else warns).append(e)
    md_path = folder / OUT_MD
    if not md_path.is_file():
        errs.append(f"E: falta {OUT_MD}")
        return errs, warns
    md = md_path.read_text(encoding="utf-8")
    texto = _strip_detalles(md)

    # tablas y bases
    tablas = {}
    for b in bj["bloques"]:
        tp = folder / "tablas" / f"{b['id']}.json"
        if not tp.is_file():
            errs.append(f"E: {b['id']} falta tablas/{b['id']}.json")
            continue
        tablas[b["id"]] = json.loads(tp.read_text(encoding="utf-8"))
    bases = {mx["N_total"]}
    pares_validos: set[tuple[int, int]] = set()
    for t in tablas.values():
        if isinstance(t.get("base"), dict):
            bases.add(int(t["base"]["N"]))
        for it in t.get("items") or []:
            bases.add(int(it["base"]))
            for c in it["categorias"] + [it["nr"]]:
                pares_validos.add((int(c["n"]), int(it["base"])))
        for c in t.get("categorias") or []:
            pares_validos.add((int(c["n"]), int(t["base"]["N"])))
        for c in t.get("paises") or []:
            pares_validos.add((int(c["n"]), int(t["base"]["N"])))
        if t.get("cruce"):
            bases.add(int(t["cruce"]["base"]))

    # cifras % (n=)
    pares = [(float(p.replace(",", ".")), int(n)) for p, n in PCT_N_RE.findall(texto)]
    pares += [(float(p.replace(",", ".")), int(n)) for n, p in N_PCT_RE.findall(texto)]
    if not pares:
        errs.append("E: el texto no reporta ninguna cifra con el formato «X% (n=Y)» o «Y estudios (X%)»")
    for p, n in pares:
        if not any(abs(pct(n, b) - p) <= 1 for b in bases if b):
            errs.append(f"E: «{p:g}% (n={n})» no cuadra con ninguna base de las tablas ({sorted(bases)})")
        elif not any(abs(pct(nn, b) - p) <= 1 and nn == n for nn, b in pares_validos):
            warns.append(f"W: «{p:g}% (n={n})» cuadra con una base pero no con una categoría de las tablas")

    # citas y enfoque centrado en autor
    for rx, nombre in CITA_PATTERNS + AUTOR_PATTERNS:
        for m in rx.finditer(texto):
            line = texto[: m.start()].count("\n") + 1
            errs.append(f"E: línea ~{line}: {nombre} → «{m.group(0)}» (Resultados no cita estudios individuales)")

    # tono
    low = texto.casefold()
    for term in TONO_EVALUATIVO:
        if re.search(rf"\b{re.escape(term)}", low):
            warns.append(f"W: tono no objetivo: «{term}» (Resultados solo reporta lo que dice la literatura)")

    # encabezados numerados
    if not re.search(r"(?m)^#{2,4} 3\.\d+\.", md):
        warns.append("W: no hay encabezados numerados «3.N.» en las subsecciones")

    # tablas y figuras: etiqueta, título, nota, citada antes, consecutivas
    lines = md.splitlines()
    for kind in ("Tabla", "Figura"):
        nums = []
        for i, ln in enumerate(lines):
            m = re.match(rf"^\*\*{kind} (\d+)\*\*\s*$", ln.strip())
            if not m:
                continue
            num = int(m.group(1))
            nums.append(num)
            sig = [x.strip() for x in lines[i + 1 : i + 4] if x.strip()]
            if not sig or not re.match(r"^\*[^*].*\*$", sig[0]):
                errs.append(f"E: {kind} {num} sin título en cursiva en la línea siguiente")
            if "*Nota.*" not in "\n".join(lines[i : i + 40]):
                errs.append(f"E: {kind} {num} sin «*Nota.*» al pie")
            antes = "\n".join(lines[:i])
            if not re.search(rf"\b{kind} {num}\b", _strip_detalles(antes)):
                errs.append(f"E: {kind} {num} no se cita en el texto antes de aparecer")
            if kind == "Tabla":
                tabla_lines = [x for x in lines[i : i + 40] if x.strip().startswith("|")]
                if tabla_lines:
                    head = tabla_lines[0]
                    if not re.search(r"\(n\)|%|Porcentaje|N\.º|Frecuencia", head):
                        errs.append(f"E: Tabla {num}: las columnas no declaran unidad (Frecuencia (n), Porcentaje…)")
                else:
                    errs.append(f"E: Tabla {num} sin tabla markdown")
        if nums and nums != list(range(1, len(nums) + 1)):
            errs.append(f"E: numeración de {kind} no consecutiva: {nums}")
        if kind == "Figura":
            specs = {}
            for sp in (folder / "graficos").glob("*.spec.json"):
                try:
                    s = json.loads(sp.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    errs.append(f"E: {rel(sp)} no es JSON válido")
                    continue
                specs[s.get("figura")] = (sp, s)
            for num in nums:
                m = re.search(rf"(?ms)^#{{2,5}} Detalle gráfica \(Figura {num}\)(.*?)(?=^#{{1,5}} |\Z)", md)
                if not m:
                    errs.append(f"E: Figura {num} sin subsección «#### Detalle gráfica (Figura {num})»")
                else:
                    cuerpo = m.group(1)
                    for campo in DETALLE_CAMPOS:
                        if not re.search(rf"\*\*{re.escape(campo)}[^*]*\*\*", cuerpo):
                            errs.append(f"E: Detalle gráfica (Figura {num}) sin campo «{campo}»")
                if num not in specs:
                    errs.append(f"E: Figura {num} sin graficos/<bloque>.spec.json con \"figura\": {num}")
                    continue
                sp, s = specs[num]
                for k in SPEC_KEYS:
                    if k not in s or s[k] in (None, "", [], {}):
                        errs.append(f"E: {rel(sp)} sin «{k}»")
                t = tablas.get(s.get("bloque"))
                if t and isinstance(s.get("datos"), list):
                    validos = {}
                    for c in t.get("categorias") or []:
                        validos[c["categoria"]] = c["n"]
                    for it in t.get("items") or []:
                        for c in it["categorias"]:
                            validos.setdefault(c["categoria"], c["n"])
                    for d in s["datos"]:
                        cat, n = d.get("categoria"), d.get("n")
                        if cat in validos and validos[cat] != n:
                            errs.append(f"E: {rel(sp)} «{cat}» n={n} ≠ tabla n={validos[cat]}")
                        elif cat not in validos:
                            warns.append(f"W: {rel(sp)} categoría «{cat}» no está en tablas/{s.get('bloque')}.json")

    for b in bj["bloques"]:
        if b.get("titulo") and b["titulo"].casefold() not in md.casefold():
            warns.append(f"W: el título del bloque {b['id']} («{b['titulo']}») no aparece en {OUT_MD}")

    # integración cuantitativo / cualitativo en bloques RQ
    for rq in sorted({b.get("rq") for b in bj["bloques"] if b.get("rq")}):
        m = re.search(rf"(?ms)^#{{2,4}} [^\n]*\b{rq}\b.*?(?=^#{{2}} |\Z)", texto)
        if not m:
            warns.append(f"W: no se encontró sección con «{rq}» en el título")
            continue
        sec = m.group(0).casefold()
        if not ("cualitativ" in sec and "cuantitativ" in sec):
            warns.append(f"W: sección {rq} sin integración explícita de estudios cuantitativos y cualitativos")

    # debate: 2 rondas + R3 registrada (plan de bloques y cada bloque)
    r3 = []
    for bid in [PLAN_BLOQUES] + [b["id"] for b in bj["bloques"]]:
        v, e = _veredicto(folder, bid)
        errs.extend(e)
        if v and v.get("rondas") == 3:
            r3.append(bid)
    dpath = folder / DEBATE_MD
    if not dpath.is_file():
        errs.append(f"E: falta {DEBATE_MD} (pnpm -s sintesis:debate-index)")
    else:
        dtxt = dpath.read_text(encoding="utf-8")
        if "## Bloques con tercera ronda" not in dtxt:
            errs.append(f"E: {DEBATE_MD} sin «## Bloques con tercera ronda»")
        for bid in r3:
            if f"Bloque {bid}:" not in dtxt:
                errs.append(f"E: {bid} tuvo tercera ronda y no figura en «## Bloques con tercera ronda»")
    if re.search(r"tercera ronda|ronda 3|R3\b", texto, re.I):
        errs.append("E: el aviso de tercera ronda no va en la prosa de resultados (solo debate, manifest y cierre)")
    return errs, warns


def cmd_lint(args: list[str]) -> int:
    if len(args) < 1:
        raise Fail("uso: resultado-sintesis.py lint docs/<slug> [carpeta]", None, 2)
    theme = theme_path(args[0])
    folder = resolve_folder(theme, args[1:])
    errs, warns = lint_folder(folder)
    for w in warns:
        print(w.replace("W:", "WARN", 1))
    for e in errs:
        print(e.replace("E:", "FAIL", 1))
    if errs:
        return error(f"sintesis:lint {len(errs)} FAIL, {len(warns)} WARN en {rel(folder)}", "corrige y vuelve a correr")
    return ok(f"sintesis:lint PASS ({len(warns)} WARN) {rel(folder)}", "pnpm -s sintesis:stamp docs/<slug> <carpeta>")


# ───────────────────────── stamp ─────────────────────────


def cmd_stamp(args: list[str]) -> int:
    if len(args) != 2:
        raise Fail("uso: resultado-sintesis.py stamp docs/<slug> <carpeta>", None, 2)
    theme = theme_path(args[0])
    folder = resolve_folder(theme, [args[1]], allow_latest=False)
    errs, _ = lint_folder(folder)
    if errs:
        for e in errs:
            print(e.replace("E:", "FAIL", 1))
        return error("no se sella con lint en FAIL", "pnpm -s sintesis:lint docs/<slug> <carpeta>")
    bj = load_json(folder / BLOQUES)
    r3 = []
    for bid in [PLAN_BLOQUES] + [b["id"] for b in bj["bloques"]]:
        v, _ = _veredicto(folder, bid)
        if v and v.get("rondas") == 3:
            r3.append({"bloque": bid, "cierre": v.get("cierre"), "frase": frase_r3(bid, v)})
    man_path = folder / MANIFEST
    man = load_json(man_path)
    man["stamped"] = dt.datetime.now().isoformat(timespec="minutes")
    man["rondas_3"] = r3
    md = (folder / OUT_MD).read_text(encoding="utf-8")
    man["figuras"] = len(re.findall(r"(?m)^\*\*Figura \d+\*\*", md))
    man["tablas"] = len(re.findall(r"(?m)^\*\*Tabla \d+\*\*", md))
    man["bloques"] = len(bj["bloques"])
    write_json(man_path, man)
    (sintesis_root(theme) / LATEST).write_text(folder.name + "\n", encoding="utf-8")
    print(f"{OUT_MD} ({man['bloques']} bloques, {man['tablas']} tablas, {man['figuras']} figuras con Detalle gráfica).")
    if r3:
        print("Tercera ronda:")
        for x in r3:
            print(f"  - {x['frase']}")
    else:
        print("Tercera ronda: ninguna (todos los bloques cerraron con acuerdo en la segunda ronda).")
    return ok(f"latest → {SINTESIS_ROOT}/{folder.name}", "skill de gráficas (Python) sobre graficos/*.spec.json")


# ───────────────────────── CLI ─────────────────────────


def dispatch(args: list[str]) -> int:
    if not args:
        print(__doc__)
        return error("falta subcomando", "prepare | general | codify-auto | aggregate | borrador | debate-index | lint | stamp", 2)
    handlers = {
        "prepare": cmd_prepare,
        "general": cmd_general,
        "codify-auto": cmd_codify_auto,
        "aggregate": cmd_aggregate,
        "borrador": cmd_borrador,
        "debate-index": cmd_debate_index,
        "status": cmd_status,
        "lint": cmd_lint,
        "stamp": cmd_stamp,
    }
    fn = handlers.get(args[0])
    if not fn:
        return error(f"subcomando {args[0]} desconocido", ", ".join(handlers), 2)
    return fn(args[1:])


if __name__ == "__main__":
    run(dispatch)
