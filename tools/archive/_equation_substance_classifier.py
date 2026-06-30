"""tools/_equation_substance_classifier.py - NOT_MATH classifier for equations.

DESIGN PHILOSOPHY (v4, post-scrap-and-rewrite):
  - Default verdict is MATH. Math is what this repo is full of.
  - Only call NOT_MATH on patterns where we are CONFIDENT Haiku would too.
  - Binary output: MATH | NOT_MATH. No UNCLEAR bucket — for the filter use
    case, UNCLEAR and MATH are equivalent (both stay in the index).

CALIBRATION TARGET:
  - Haiku's VALID rate on equations is 71.2% (356/500). A "always MATH"
    baseline scores 71.2%. v4's NOT_MATH detector must AT MINIMUM match
    Haiku's NOISE catches without introducing new VALID-misclassifications.
  - Aim: ≥85% agreement on the 500 Haiku-audited equations.

PATTERN SET (high-precision NOT_MATH only):
  1. YAML / config pin             scheme=, convention=, etc.
  2. YAML line continuation        ends with `;\` or `\` (not `\\`)
  3. Boolean / None assignment     X = True / False / None
  4. Gate verdict-file line        gate_name=, gate_verdict=, etc.
  5. File path                     `path/to/file.ext`
  6. Python statement              import/def/class/etc.
  7. Python library call           np., torch., json., etc.
  8. Trailing code comment         `... # comment`
  9. Dimensionality declaration    [X] = dimensionless
  10. Verdict-delta annotation     (delta = ±X%) suffix
  11. Verdict-output value=STATUS  value='outcome=PASS;...'
  12. No math symbols at all       pure prose with zero =,+,-,*,/,^,<,>,Greek,LaTeX

Everything else: MATH.
"""
import argparse
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(".")
INDEX = ROOT / "tools" / "knowledge-index.json"
AGG = ROOT / "tools" / "_anchor_validation_results.json"
BATCH = ROOT / "tools" / "anchor_validation_batches"
OUT = ROOT / "tools" / "_equation_substance_verdicts.json"


# ---------------------------------------------------------------------
# Pattern set — 12 high-precision NOT_MATH detectors. First match wins.
# ---------------------------------------------------------------------

# 1. YAML config pin
#    NOTE: L_max removed — it's a physics parameter (eigenvalue truncation),
#    not a config pin. Same for closure-related quantities; only true config
#    keys remain.
RE_YAML_PIN = re.compile(
    r"^\s*(scheme|convention|value|tier_pin|sha256|content_sha\w*|"
    r"audit_sha\w*|schema_version|closure_sha\w*)\s*=",
    re.IGNORECASE,
)

# 2. YAML line continuation (ends with ;\ or \, but not \\ which is LaTeX)
def _is_yaml_continuation(raw):
    s = raw.rstrip()
    if s.endswith(";\\"):
        return True
    if s.endswith("\\") and not s.endswith("\\\\"):
        return True
    return False

# 3. Boolean / None assignment
RE_BOOL_ASSIGN = re.compile(
    r"=\s*(True|False|None|true|false|null|TRUE|FALSE|NULL)\b"
)

# 4. Gate verdict-file line
RE_GATE_VERDICT = re.compile(
    r"^\s*(gate_name|gate_verdict|gate_detail|gate_id)\s*="
)

# 5. File path
RE_FILE_PATH = re.compile(
    r"^\s*[\w\-]+/[\w\-/.]+\.(py|md|json|txt|npz|csv|yaml|yml|sh|png|jpg|pdf|h5)\s*$"
)

# 6. Python statement
#    NOTE: `with\s+\w` removed because it fires on prose like
#    "with envelope α_k = 2k - 1". Python `with` statements always have
#    either `as` or `(` followed by `:` at line end — capture those forms.
RE_PYTHON_STMT = re.compile(
    r"^\s*(import\s|from\s+\w+\s+import|def\s+\w+\s*\(|class\s+\w+\s*[:(]|"
    r"return\s|raise\s|try\s*:|except\s|finally\s*:|elif\s+|else\s*:|"
    r"@[a-z]\w*|assert\s+|pass\s*$|yield\s+|global\s+|nonlocal\s+|"
    r"with\s+[^=]+\bas\s|with\s+[^=]+\(|with\s+[^=]+:\s*$)"
)

# 7. Trailing code comment (# at non-start, with following text)
#    Note: Python calls are NOT in the NOT_MATH set — in this project the
#    computation scripts ARE the math (per extract_entities.py:2682
#    "Python code IS the math — computation scripts are physics computations").
RE_CODE_COMMENT = re.compile(r"\s+#\s+[A-Za-z]")

# 8. Dimensionality declaration — STRICT: keyword must be the WHOLE RHS,
#    not just the start. `[Y_nu] = dimensionless` matches; `A_IKKT = matrix
#    algebra M_∞(C)` does NOT (because RHS continues with math content).
RE_DIM_DECLARE = re.compile(
    r"^\s*\[?\w+\]?\s*=\s*(dimensionless|integer|float|scalar|vector|"
    r"tensor|boolean|bool|operator|module)\s*(?:\([\w\s]*\))?\s*(?:--.*)?\s*$",
    re.IGNORECASE,
)

# 9. Verdict-output value=STATUS embedded
#    Note: "delta" is intentionally NOT in any NOT_MATH pattern — delta (Δ)
#    is a standard mathematical symbol for change/difference.
RE_VALUE_STATUS = re.compile(
    r"value\s*=\s*['\"]?[A-Z][A-Z_-]+(?:[;,]|\s*['\"]?\s*$)",
)

# 12. No math symbols at all (pure prose) — applied last
# Symbols that count as "math": = + - * / ^ < > ≤ ≥ ≠ ≈ ≡ ∂ ∇ ∫ ∑ ∏ Greek/LaTeX/braces
RE_HAS_MATH_SYMBOL = re.compile(
    r"[=+\-*/^<>]"                              # ASCII math ops
    r"|[α-ωΑ-Ω∂∇∫∑∏≤≥≠≈≡∈∉∀∃∞⊗⊕]"             # Unicode math
    r"|\\(frac|sum|int|partial|nabla|sqrt|leq|geq|sim|times|cdot|"
    r"propto|equiv|approx|alpha|beta|gamma|delta|epsilon|theta|"
    r"kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|phi|chi|psi|omega|"
    r"infty|hbar|to|in)\b"                      # LaTeX math commands
    r"|[_^]\{[^}]"                              # subscript/superscript with braces
)


def classify(text):
    """Return ('MATH'|'NOT_MATH', reason). No UNCLEAR — default is MATH."""
    raw = (text or "").strip().strip("`").strip()
    if not raw:
        return ("NOT_MATH", "empty string")

    # === HIGH-PRECISION NOT_MATH PATTERNS ===
    if RE_YAML_PIN.match(raw):
        return ("NOT_MATH", "YAML / config pin")
    if _is_yaml_continuation(raw):
        return ("NOT_MATH", "YAML line continuation (ends with `;\\` or `\\`)")
    if RE_BOOL_ASSIGN.search(raw):
        return ("NOT_MATH", "boolean / None assignment")
    if RE_GATE_VERDICT.match(raw):
        return ("NOT_MATH", "gate verdict-file line")
    if RE_FILE_PATH.match(raw):
        return ("NOT_MATH", "file path")
    if RE_PYTHON_STMT.match(raw):
        return ("NOT_MATH", "Python statement (import/def/class/etc.)")
    # NOTE: trailing code comment (#) rule REMOVED — Python code IS math in
    # this project, and `D_max = abs(np.log10(...))  # vs ledger` should be
    # MATH not NOT_MATH.
    if RE_DIM_DECLARE.match(raw):
        return ("NOT_MATH", "dimensionality declaration ([X] = dimensionless/scalar/etc.)")
    if RE_VALUE_STATUS.search(raw):
        return ("NOT_MATH", "embedded value=STATUS")
    if not RE_HAS_MATH_SYMBOL.search(raw):
        return ("NOT_MATH", "no math symbols (pure prose)")

    # === DEFAULT: MATH ===
    return ("MATH", "has math content (default-accept)")


# ---------------------------------------------------------------------
# Validation / application drivers (unchanged from prior versions)
# ---------------------------------------------------------------------

def load_audited_equations():
    agg = json.loads(AGG.read_text(encoding="utf-8"))
    eq_verdicts = agg.get("equations", {})
    audited = []
    for b in sorted(BATCH.glob("equations_*.json")):
        try:
            payload = json.loads(b.read_text(encoding="utf-8"))
        except Exception:
            continue
        for a in payload.get("anchors", []):
            aid = a.get("anchor_id")
            v = eq_verdicts.get(aid, {}).get("verdict")
            if not v:
                continue
            audited.append({
                "anchor_id": aid,
                "name": a.get("name") or "",
                "raw": a.get("name") or "",
                "audit_verdict": v,
            })
    return audited


def validate_against_audit():
    audited = load_audited_equations()
    print(f"Validating classifier (v4: default-MATH) against {len(audited)} audited equations...")
    print()

    cm = defaultdict(int)
    false_pos = []  # audit NOISE -> clf MATH
    false_neg = []  # audit VALID -> clf NOT_MATH
    for e in audited:
        verdict, reason = classify(e["raw"])
        cm[(e["audit_verdict"], verdict)] += 1
        if e["audit_verdict"] == "NOISE" and verdict == "MATH":
            false_pos.append({"aid": e["anchor_id"], "name": e["name"][:120], "reason": reason})
        elif e["audit_verdict"] == "VALID" and verdict == "NOT_MATH":
            false_neg.append({"aid": e["anchor_id"], "name": e["name"][:120], "reason": reason})

    # Confusion matrix
    audit_verdicts = sorted({v for v, _ in cm.keys()})
    clf_verdicts = sorted({c for _, c in cm.keys()})
    print(f"{'audit \\\\ clf':<14}", end="")
    for c in clf_verdicts:
        print(f"{c:>12}", end="")
    print(f"{'total':>10}")
    for v in audit_verdicts:
        row_total = sum(cm[(v, c)] for c in clf_verdicts)
        print(f"{v:<14}", end="")
        for c in clf_verdicts:
            print(f"{cm[(v, c)]:>12}", end="")
        print(f"{row_total:>10}")

    # Metrics
    agree = cm[("VALID", "MATH")] + cm[("NOISE", "NOT_MATH")]
    total = sum(cm.values())
    print()
    print(f"Agreement (audit-VALID = clf-MATH OR audit-NOISE = clf-NOT_MATH): {agree}/{total} = {agree/total*100:.1f}%")
    print(f"False positives (audit NOISE -> clf MATH):  {len(false_pos)}")
    print(f"False negatives (audit VALID -> clf NOT_MATH): {len(false_neg)}")
    print()

    if false_neg:
        print(f"--- False NEG (audit VALID -> clf NOT_MATH; first 10) ---")
        for it in false_neg[:10]:
            print(f"  [{it['aid']}] {it['name']}")
            print(f"     reason: {it['reason']}")
        print()
    if false_pos:
        print(f"--- False POS (audit NOISE -> clf MATH; first 10) ---")
        for it in false_pos[:10]:
            print(f"  [{it['aid']}] {it['name']}")
        print()


def apply_to_all_equations():
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    eqns = index.get("equations", [])
    print(f"Classifying {len(eqns)} equations...")

    out_per = {}
    tally = Counter()
    tally_reason = Counter()
    for e in eqns:
        eid = e.get("id")
        if not eid:
            continue
        text = e.get("raw") or e.get("name") or ""
        verdict, reason = classify(text)
        out_per[eid] = {"verdict": verdict, "reason": reason}
        tally[verdict] += 1
        tally_reason[f"{verdict}:{reason}"] += 1

    OUT.write_text(json.dumps({
        "per_anchor": out_per,
        "tally": dict(tally),
        "tally_by_reason": dict(tally_reason),
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}")
    print()
    print("Classifier tally on all equations:")
    for v, c in tally.most_common():
        print(f"  {v:<12} {c:>6}  ({c/sum(tally.values())*100:.1f}%)")
    print()
    print("Top NOT_MATH reasons:")
    for reason, c in tally_reason.most_common(20):
        if reason.startswith("NOT_MATH"):
            print(f"  {c:>6}  {reason}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if args.validate:
        validate_against_audit()
    if args.apply:
        apply_to_all_equations()
    if not args.validate and not args.apply:
        ap.print_help()


if __name__ == "__main__":
    main()
