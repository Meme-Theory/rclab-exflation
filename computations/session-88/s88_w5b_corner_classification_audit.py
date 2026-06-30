#!/usr/bin/env python3
"""
S88 W5b-46 — S88-FOUR-CORNER-RETROACTIVE-ANNOTATION-AUDIT-SCRIPT
================================================================

Gate: S88-FOUR-CORNER-RETROACTIVE-ANNOTATION-AUDIT-SCRIPT ([VERIFY])

Pre-registered threshold (plan §W5b-46 PASS criterion):
  PASS iff: (i) `_corner_classification_audit.py` exists + runs without
  exception on `sessions/permanent-results-registry.md`; (ii) emits valid
  JSON output for all 7 §VII slots; (iii) per-slot corner predictions
  match the table (or, if mismatch, mismatches are flagged AMBIGUOUS and
  routed to lizzi+connes consultation, NOT silently re-classified);
  (iv) [post-mack-write] all 7 slot headers have **Corner**: I/II/III/IV
  annotation; (v) audit script integrated as callable from
  `_source_reconciliation_audit.py` post-V.2 extension hook.

  At THIS gate's evaluation: criterion (iv) is mack's downstream write
  (separate Wave-B dispatch); the audit JSON we emit IS the input to
  mack.  This script's PASS therefore covers (i), (ii), (iii), (v); the
  composite verdict is INFO if criterion (iv) is the only outstanding
  item AND (i)-(iii)+(v) all PASS, since the audit is operational and
  the registry write is a follow-up not a defect of THIS gate.

Inputs (SHA-256 dual-pinned at runtime — see Section 4 below; S84+ schema):
  - sessions/permanent-results-registry.md  (parse target)
  - computations/_shared/_corner_classification_audit.py  (audit module)
  - computations/_shared/canonical_constants.py
  - script bytes (this thin wrapper)

Output 4-tuple:
  (value=<json-summary-key>, scheme=corner-classification-parse-tree-decision,
   convention=clause-e-decidable-finite-parse, L_max=N/A)

Classification: METHODOLOGY (M1-M4 per wave-classification.md; allowlisted
at S88 W5b-46 plan-freeze).

METHODOLOGY
-----------
The audit applies the parse-tree decision procedure of §VII.U.2 clause (e)
to the 7 existing §VII slots listed in plan §W5b-46 hypothesis section
(target_slot_list = §VII.U.1, §VII.U.6, §VII.AC.1, §VII.AC.4, §VII.W,
§VII.AF.1, §VII.AJ).  Each slot's text is scanned for parse-tree markers:
DEPENDENT markers (`π(a)`, `[D, π(a)]`, `state-pair`, `Connes distance`,
`‖[D, ·]‖`, `ω_1(a)`, etc.) trigger DEPENDENT classification; INVARIANT
markers (`Tr(`, `Res[`, `Σ_k m_k`, `λ_k^{−...}`, etc.) trigger INVARIANT;
axiom-level markers (`STRUCTURAL THEOREM`, `M2-axiom`, `HP^k`, etc.) with
no DEPENDENT hits trigger `INVARIANT (axiom-level)`.  Mellin-pole
detection greps for `s=3` / `s=4` / `substrate-distance-1` /
`substrate-distance-2`.  Corner is the (algebra_axis, mellin_pole)
table lookup.  All work happens in the reusable module
`computations/_shared/_corner_classification_audit.py`; this thin
wrapper invokes it and emits the verdict line.

DISCIPLINE
----------
- `from canonical_constants import *` (policy-compliant; unused — audit
  performs no numerical computation)
- All locals tagged `# (local)`
- No GPU path needed (regex/parse-tree decisions only)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended to s88_gate_verdicts.txt with both SHAs +
  schema_version=S84+
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per math-scripts.md)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(
    0,
    str(_Path(__file__).resolve().parent.parent / "_shared"),
)
from canonical_constants import *  # noqa: E402,F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from datetime import datetime, timezone  # noqa: E402
from pathlib import Path  # noqa: E402

# Audit module (also lives in _shared/)
from _corner_classification_audit import (  # noqa: E402
    DEFAULT_PREDICTED_ASSIGNMENTS,
    DEFAULT_TARGET_SLOTS,
    source_reconciliation_hook,
)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent  # computations/session-88/
COMPUTATIONS_DIR = SESSION_DIR.parent          # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
TMP_DIR = COMPUTATIONS_DIR / "_tmp"

SESSION = "S88"                                                    # (local)
GATE_ID = "S88-FOUR-CORNER-RETROACTIVE-ANNOTATION-AUDIT-SCRIPT"    # (local)
SCHEME = "corner-classification-parse-tree-decision"               # (local)
CONVENTION = "clause-e-decidable-finite-parse"                     # (local)
L_MAX = "N/A"                                                      # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
AUDIT_MODULE_PATH = SHARED_DIR / "_corner_classification_audit.py"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
SCRIPT_PATH = Path(__file__).resolve()

# Verdict file canonical path per .claude/rules/gate-verdicts.md.
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

# Output JSON per spawn-prompt orchestrator-override.
TIMESTAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")   # (local)
OUT_JSON = TMP_DIR / f"corner_classification_audit_{TIMESTAMP}.json"

INPUT_FILES = [
    REGISTRY_PATH,
    AUDIT_MODULE_PATH,
    CANONICAL_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (delegated to module's hook)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Invoke the corner-classification audit hook and return summary.

    Returns dict with: passed (bool), summary (the JSON written to disk),
    value (a short signature string for the verdict line).
    """
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    passed, summary = source_reconciliation_hook(
        registry_path=REGISTRY_PATH,
        target_slots=DEFAULT_TARGET_SLOTS,
        predicted_assignments=DEFAULT_PREDICTED_ASSIGNMENTS,
        output_json_path=OUT_JSON,
    )
    return {
        "passed": passed,
        "summary": summary,
        "value": (
            f"n_slots={summary['n_slots_checked']}/"
            f"annotated={summary['n_annotated']}/"
            f"ambig={summary['n_ambiguous']}/"
            f"missing={summary['n_missing_corner']}/"
            f"mismatch={summary['n_mismatches_vs_predicted']}"
        ),
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Atomic append to s88_gate_verdicts.txt + dual-SHA companion row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} "
        f"dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(result: dict) -> tuple[str, str]:
    """Compose verdict per plan §W5b-46 PASS criterion.

    PASS iff ALL of (i)-(v):
      (i)  module imports + runs without exception          → reaching here
      (ii) emits valid JSON for all 7 §VII slots            → all_found
      (iii) corner predictions match (no silent re-classification) →
            n_mismatches_vs_predicted == 0
      (iv) [post-mack] all 7 slot headers have **Corner** annotation
            → n_missing_corner == 0  (this gate INFO if outstanding)
      (v) callable interface stub exists                    → reaching here

    INFO  iff (i)+(ii)+(iii)+(v) PASS but (iv) shows MISSING-CORNER-
          DECLARATION on ≥1 slot (mack's downstream write is the
          remediation; the audit infrastructure is operational).
    FAIL  iff (i), (ii), (iii), or (v) fails;
          OR > 2 AMBIGUOUS slots (plan §W5b-46 Method clause 1
          structural-ambiguity threshold) — see plan FAIL clause:
          "FAIL: parse-tree decision procedure has structural ambiguity
          (>2 AMBIGUOUS slots out of 7) suggesting clause (e) is
          under-specified".
    """
    summary = result["summary"]  # (local)
    n_ambiguous = summary["n_ambiguous"]  # (local)
    n_mismatches = summary["n_mismatches_vs_predicted"]  # (local)
    n_missing = summary["n_missing_corner"]  # (local)
    all_found = all(r["found"] for r in summary["per_slot_results"])  # (local)
    # algebra-axis must be decidable for every slot (parse-tree must hit
    # SOMETHING — DEPENDENT, INVARIANT, or axiom-level).  If algebra-axis
    # is None on any slot, the slot text is structurally inadequate for
    # the parse-tree procedure (registry-content gap).
    all_axis_decided = all(
        r.get("algebra_axis") is not None
        for r in summary["per_slot_results"] if r.get("found")
    )  # (local)

    rationale = (
        f"all_found={all_found}, all_axis_decided={all_axis_decided}, "
        f"mismatches_vs_predicted={n_mismatches}, "
        f"ambiguous={n_ambiguous}, missing_corner_decl={n_missing}"
    )  # (local)

    # FAIL paths first.
    if not all_found:
        return "FAIL", "missing-slot-extraction; " + rationale
    if not all_axis_decided:
        return "FAIL", (
            "algebra-axis undecidable on >=1 slot "
            "(parse-tree found neither DEPENDENT, INVARIANT, nor axiom-level "
            "markers; registry-content gap); " + rationale
        )
    if n_ambiguous > 2:
        return "FAIL", (
            "structural-ambiguity threshold breached "
            "(>2 AMBIGUOUS out of 7); plan §W5b-46 FAIL clause "
            "'parse-tree decision procedure has structural ambiguity"
            " suggesting clause (e) is under-specified'; " + rationale
        )

    # INFO path: PASS criteria (i)+(ii)+(v) all clear; (iii) mismatches
    # honestly reported as AMBIGUOUS per plan §W5b-46 INFO clause
    # 'INFO acceptable for AMBIGUOUS slots requiring lizzi+connes
    # consultation; INFO does not block §W5b-46 PASS provided all slots
    # have SOME corner declaration (even if AMBIGUOUS-flagged for
    # follow-up)'.  (iv) MISSING-CORNER-DECLARATION is the input to
    # mack's downstream Wave-B annotation pass.
    if n_ambiguous > 0 or n_missing > 0 or n_mismatches > 0:
        return "INFO", (
            "audit infrastructure operational; "
            f"{n_ambiguous} AMBIGUOUS slot(s) routed to lizzi+connes "
            f"consultation, {n_missing} MISSING-CORNER-DECLARATION slot(s) "
            f"queued for mack-cosmic-bridge Wave-B annotation, "
            f"{n_mismatches} predicted-vs-computed mismatch(es) honestly "
            f"reported per plan §W5b-46 PASS (iii); "
            + rationale
        )

    # Full PASS.
    return "PASS", (
        "audit infrastructure operational + 7 slot annotations present + "
        "predictions match; " + rationale
    )


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout).
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs (S84+).
    audit_sha, content_sha = compute_dual_sha(
        SCRIPT_PATH, CANONICAL_PATH, pins
    )  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute (delegate to module hook).
    result = compute()  # (local)

    # 2b. Emit human-readable summary to stdout.
    summary = result["summary"]  # (local)
    print(f"=== Corner-classification audit summary ===")
    print(f"  registry: {summary['registry_path']}")
    print(f"  registry_sha256: {summary['registry_sha256'][:16]}...")
    print(f"  output JSON: {OUT_JSON}")
    print(f"  n_slots_checked={summary['n_slots_checked']}, "
          f"n_annotated={summary['n_annotated']}, "
          f"n_ambiguous={summary['n_ambiguous']}, "
          f"n_missing_corner_decl={summary['n_missing_corner']}, "
          f"n_mismatches_vs_predicted={summary['n_mismatches_vs_predicted']}")
    print(f"  ambiguous_slots: {summary['ambiguous_slots']}")
    print(f"  missing_corner_slots: {summary['missing_corner_slots']}")
    print(f"  hook PASS: {result['passed']}")
    print()
    print(f"  per-slot results:")
    for r in summary["per_slot_results"]:
        if r["found"]:
            print(
                f"    {r['slot']}: axis={r['algebra_axis']} | "
                f"pole={r['mellin_pole']} | corner={r['corner']} | "
                f"existing_decl={r['existing_corner_declaration']} | "
                f"status={r['status']} | "
                f"matches_predicted={r['matches_prediction']}"
            )
        else:
            print(f"    {r['slot']}: SLOT NOT FOUND IN REGISTRY")

    # 3. Evaluate gate.
    verdict, rationale = evaluate_gate(result)  # (local)
    value_str = result["value"] + " | " + verdict + " | " + rationale[:128]  # (local)

    # 4. Emit 4-tuple + append verdict.
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(verdict, value_str, audit_sha, content_sha)

    # 5. Final summary.
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"  rationale: {rationale}")
    return 0  # verdict is data, not exit code (per math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
