"""Valida celdas de ítem según response_type (registro agregable + nota)."""
from __future__ import annotations

import re

ITEM_IDS = frozenset(
    f"RQ{r}-I{i}" for r in (1, 2, 3) for i in range(1, 6) if not (r == 1 and i > 4) and not (r == 2 and i > 4)
)


def _norm(s: str) -> str:
    return (s or "").strip()


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
