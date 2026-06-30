#!/usr/bin/env python3
"""
S102 W2-5 S102-CAPSTONE-73-BFSPINE-PATCH — capstone §7.3 BF-spine dual-column patch verifier
============================================================================================

Gate: S102-CAPSTONE-73-BFSPINE-PATCH ([AUDIT])

Pre-registered threshold (set-membership; NON-COMPUTE artifact-existence + must_contain gate):
  PASS iff (capstone §7.3 box contains ALL dual-column must_contain markers)
         AND (LINE-SCOPED forbidden-pattern grep finds ZERO unqualified external "DECISIVE"
              — every "DECISIVE" on a line carries a dual-column scope token on the SAME line)
         AND (substrate-IS framing markers present: model-SELECTION = "is the substrate special
              among geometries"; model-COMPARISON = "does it beat ΛCDM+ν"; arrow not inverted).
  FAIL iff any required marker absent OR an unqualified external "DECISIVE" survives the
       LINE-SCOPED grep OR the substrate-IS framing is inverted.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - sessions/framework/phonic-exflation-equation.md  (the patched capstone; verifier reads applied state)
  - sessions/framework/registry/falsifier-master-inventory.md  (register-of-record; S101 dual-column block)
  - computations/_shared/canonical_constants.py  (BF_spine_vs_incumbent_ceiling = 31.62; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

content_sha256 is computed over (script bytes || applied-§7.3-patch bytes) per the plan
audit_discriminators.content_sha256_inputs = ["script", "applied_capstone_diff"] (METHODOLOGY-class prose patch).

Output 4-tuple:
  (value=<marker-presence summary>, scheme=designated-writer reviewed patch,
   convention=content_sha256 over applied diff; prose tier == inventory register tier, L_max=N/A)

Classification: NON-PHONONIC (capstone-hygiene designated-writer prose patch).

METHODOLOGY
-----------
Designated-writer reviewed prose patch to the capstone §7.3 BF_spine scorecard box
(`phonic-exflation-equation.md`), per `capstone-hygiene-gate.md` Q4 curated-doc discipline.
The §7.3 box carried the S97/S98 COMPUTED outcome (BF_spine = 2000 DECISIVE, model-class vs
random-geometry) but NOT the S101 BF-spine-reference-class DUAL-COLUMN. This verifier greps the
APPLIED §7.3 patch box for: (1) the dual-column (DECISIVE = random-geometry-scoped model-SELECTION
2000/200; incumbent model-COMPARISON very-strong CEILING 31.62 NEVER-decisive; anecdotal FLOOR ~2);
(2) the evidence-TYPE anti-commensurability guard; (3) CONVERGENT-DERIVED tags; (4) the inventory
register-of-record citation; (5) substrate-IS framing markers. It then runs the LINE-SCOPED
forbidden-pattern grep: every line mentioning "DECISIVE" (external, capitalised) MUST carry a
dual-column scope token on the SAME line (the patch's own explanatory prose quotes "DECISIVE", so a
whole-body grep would self-trip — hence LINE-SCOPED per the plan forbidden_pattern_scope pin).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU text-grep only (no linear algebra) — OMP cap is irrelevant; no torch needed
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema; content over script || applied-diff)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe; the script PRINTS the
  payload via print_verdict_payload, the dispatching AGENT calls mcp__knowledge__emit_verdict).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # text grep only; cap threads defensively
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys as _sys
SHARED_DIR_BOOTSTRAP = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared"
)
if SHARED_DIR_BOOTSTRAP not in _sys.path:
    _sys.path.insert(0, SHARED_DIR_BOOTSTRAP)

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import BF_spine_vs_incumbent_ceiling  # explicit pin import

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S102"                                                   # (local)
GATE_ID = "S102-CAPSTONE-73-BFSPINE-PATCH"                         # (local)
SCHEME = "designated-writer reviewed patch"                       # (local)
CONVENTION = "content_sha256 over applied diff; prose tier == inventory register tier"  # (local)
L_MAX = "N/A"                                                      # (local)

CAPSTONE = PROJECT_ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"      # (local)
INVENTORY = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"  # (local)

OUT_NPZ = SESSION_DIR / "s102_w2_capstone_73_bfspine_patch_verify.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CAPSTONE,
    INVENTORY,
]

# Canonical published values (cross-checked against canonical_constants + knowledge MCP this session).
BF_CEILING = 31.62          # BF_spine_vs_incumbent_ceiling (S101); very-strong band [10,100)   # (local)
BF_DECISIVE_FLOOR = 100.0   # Jeffreys/Kass-Raftery "decisive" boundary                          # (local)
BF_MODEL_SELECTION = 2000.0 # BF_spine_full = 10^3.30103 (model-SELECTION, S98-W4-4-OQ3-COVARIANCE) # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — §7.3 box extraction + marker verification
# ---------------------------------------------------------------------------
def extract_dual_column_box(capstone_text: str) -> str:
    """Return the new dual-column callout box from §7.3 (the patched prose box).

    The box is the blockquote opening with the reference-class dual-column header and
    closing before the next blockquote ('> **Headline test:'). Bounded by literal anchors.
    """
    start_anchor = "> **The reference-class dual-column"  # (local)
    end_anchor = "> **Headline test: the first-sound BAO ring"  # (local)
    i = capstone_text.find(start_anchor)  # (local)
    if i < 0:
        return ""
    j = capstone_text.find(end_anchor, i)  # (local)
    if j < 0:
        j = len(capstone_text)
    return capstone_text[i:j]


def check_markers(box: str) -> dict[str, bool]:
    """Set-membership of the must_contain dual-column markers in the §7.3 box."""
    checks: dict[str, bool] = {}  # (local)
    # (1) model-SELECTION DECISIVE 2000/200
    checks["model_SELECTION_present"] = "model-SELECTION" in box
    checks["decisive_2000_present"] = ("2000" in box) and ("DECISIVE" in box)
    checks["accommodation_floor_200_present"] = "200" in box
    # (2) incumbent model-COMPARISON very-strong CEILING 31.62 NEVER decisive
    checks["model_COMPARISON_present"] = "model-COMPARISON" in box
    checks["ceiling_3162_present"] = "31.62" in box
    checks["very_strong_present"] = ("very-strong" in box.lower()) or ("very strong" in box.lower())
    checks["never_decisive_present"] = bool(re.search(r"NEVER (the )?decisive", box))
    # (3) anecdotal FLOOR ~2
    checks["anecdotal_floor_present"] = ("anecdotal" in box.lower()) and (
        ("~2" in box) or ("`~2`" in box) or ("FLOOR" in box)
    )
    # (4) evidence-TYPE anti-commensurability guard
    checks["evidence_type_guard_present"] = ("evidence TYPE" in box) or ("Two evidence TYPES" in box)
    checks["anti_commensurability_present"] = (
        "anti-commensurab" in box.lower()
        or "NOT two estimates of one quantity" in box
        or "common Bayes scale" in box
        or "one common Bayes scale" in box
    )
    # (5) CONVERGENT-DERIVED tags
    checks["convergent_derived_present"] = "CONVERGENT-DERIVED" in box
    # (6) inventory register-of-record citation
    checks["inventory_register_citation_present"] = "falsifier-master-inventory.md" in box
    # substrate-IS framing markers (model-SELECTION asks special-among-geometries;
    # model-COMPARISON asks beat-ΛCDM; explanation arrow present, not inverted)
    checks["framing_special_among_geometries"] = (
        "special among" in box.lower()
        or "special among geometries" in box.lower()
        or "among random geometries" in box.lower()
    )
    checks["framing_beat_lcdm"] = ("beat" in box.lower()) and ("ΛCDM" in box)
    checks["framing_arrow_not_inverted"] = (
        "D_K eigenvalues → spectral moments → emergent observables → measurement" in box
    )
    return checks


# ---------------------------------------------------------------------------
# Section 5b — LINE-SCOPED forbidden-pattern grep
# ---------------------------------------------------------------------------
# A "DECISIVE" mention PASSES iff the SAME line carries a dual-column scope token.
SCOPE_TOKENS = [
    "random-geometry",
    "random geometr",       # "random geometries" / "random geometry"
    "model-SELECTION",
    "model-COMPARISON",
    "vs incumbent",
    "very-strong",
    "very strong",
    "ceiling",
    "ACCOMMODATION",
    "Column 1",
    "decisive band",        # the substitution-chain line ("NEVER the decisive band")
    "decisive-floor",
]


def forbidden_pattern_count(box: str) -> tuple[int, list[str]]:
    """Count lines in the §7.3 box that mention external 'DECISIVE' WITHOUT a same-line scope token.

    LINE-SCOPED per plan forbidden_pattern_scope. Returns (count, offending_lines).
    """
    offenders: list[str] = []  # (local)
    for raw in box.splitlines():
        if "DECISIVE" not in raw:
            continue
        # The token must be the capitalised external Jeffreys-tier word; "DECISIVE" already is.
        has_scope = any(tok.lower() in raw.lower() for tok in SCOPE_TOKENS)  # (local)
        if not has_scope:
            offenders.append(raw.strip())
    return len(offenders), offenders


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": 102,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 2. Read the applied capstone state + extract the patched §7.3 dual-column box
    capstone_text = CAPSTONE.read_text(encoding="utf-8")  # (local)
    inventory_text = INVENTORY.read_text(encoding="utf-8")  # (local)
    box = extract_dual_column_box(capstone_text)  # (local)
    box_len = len(box)  # (local)
    print(f"  §7.3 dual-column box extracted: {box_len} chars")
    assert box_len > 800, f"§7.3 dual-column box not found / too short ({box_len} chars)"

    # 2b. Cross-check the canonical pin matches the published value used in the patch.
    assert abs(float(BF_spine_vs_incumbent_ceiling) - BF_CEILING) < 1e-9, (
        f"canonical BF_spine_vs_incumbent_ceiling drift: "
        f"{BF_spine_vs_incumbent_ceiling} != {BF_CEILING}"
    )
    # 2c. The register-of-record dual-column block must exist in the inventory (CITED, not edited).
    inv_block_present = (
        "S101 BF-spine-reference-class" in inventory_text
        and "model-SELECTION" in inventory_text
        and "31.62" in inventory_text
    )  # (local)
    print(f"  inventory register-of-record dual-column block present: {inv_block_present}")
    assert inv_block_present, "inventory S101 dual-column block (register-of-record) not found"

    # 3. Marker checks + LINE-SCOPED forbidden-pattern grep
    marker_checks = check_markers(box)  # (local)
    all_markers = all(marker_checks.values())  # (local)
    forbidden_n, offenders = forbidden_pattern_count(box)  # (local)

    print("\n=== must_contain marker presence ===")
    for k, v in marker_checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print(f"\n=== LINE-SCOPED forbidden-pattern grep (unqualified external DECISIVE) ===")
    print(f"  count = {forbidden_n} (PASS iff 0)")
    for off in offenders:
        print(f"    OFFENDER: {off[:120]}")

    # 3b. Substitution-chain numeric cross-check: 31.62 < 100 < 2000.
    ordering_ok = (BF_CEILING < BF_DECISIVE_FLOOR < BF_MODEL_SELECTION)  # (local)
    print(f"\n=== substitution-chain ordering ===")
    print(f"  {BF_CEILING} < {BF_DECISIVE_FLOOR} < {BF_MODEL_SELECTION}  => {ordering_ok}")
    print(f"  ratio ceiling/decisive-floor = {BF_CEILING / BF_DECISIVE_FLOOR:.4f} (< 1)")
    print(f"  ratio model-SELECTION/ceiling = {BF_MODEL_SELECTION / BF_CEILING:.2f}x")

    # 4. Gate rule (set-membership)
    verdict = "PASS" if (all_markers and forbidden_n == 0 and ordering_ok) else "FAIL"  # (local)
    framing_ok = all(  # (local)
        marker_checks[k] for k in (
            "framing_special_among_geometries",
            "framing_beat_lcdm",
            "framing_arrow_not_inverted",
        )
    )

    # 5. dual-SHA: content over (script || applied §7.3 patch box); audit over (script || canonical || pinmap)
    script_bytes = Path(__file__).resolve().read_bytes()  # (local)
    canonical_bytes = (SHARED_DIR / "canonical_constants.py").read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    h_content.update(box.encode("utf-8"))  # applied_capstone_diff = the patched §7.3 box bytes
    content_sha = h_content.hexdigest()  # (local)

    print(f"\n  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script || applied §7.3 patch box)")

    # 6. Optional npz of the marker-presence booleans (plan: optional=true)
    try:
        import numpy as np  # (local)
        np.savez(
            OUT_NPZ,
            marker_keys=np.array(list(marker_checks.keys())),
            marker_values=np.array([bool(v) for v in marker_checks.values()]),
            forbidden_count=np.array(forbidden_n),
            all_markers=np.array(bool(all_markers)),
            framing_ok=np.array(bool(framing_ok)),
            ordering_ok=np.array(bool(ordering_ok)),
            bf_ceiling=np.array(BF_CEILING),
            bf_decisive_floor=np.array(BF_DECISIVE_FLOOR),
            bf_model_selection=np.array(BF_MODEL_SELECTION),
            box_len=np.array(box_len),
        )
        print(f"  npz written: {OUT_NPZ.name}")
    except Exception as e:  # noqa: BLE001
        print(f"  npz write skipped (optional): {e}")

    # 7. Emit 4-tuple + verdict payload
    value = (
        f"markers={sum(marker_checks.values())}/{len(marker_checks)}_PASS_"
        f"forbidden_DECISIVE={forbidden_n}_"
        f"ordering[31.62<100<2000]={ordering_ok}_"
        f"ceiling=31.62_model_SELECTION=2000_floor~2_"
        f"framing_substrate_IS={framing_ok}_register_tier=inventory"
    )  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# content_sha256 over (script || applied §7.3 dual-column box, {box_len} chars) "
        f"per plan content_sha256_inputs=[script,applied_capstone_diff]",
        f"# BF ordering: ceiling 31.62 (very-strong, NEVER decisive) < decisive-floor 100 "
        f"< model-SELECTION 2000; ratio model-SELECTION/ceiling=63.25x",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # verdict is data; exit 0 on a healthy run regardless of PASS/FAIL


if __name__ == "__main__":
    sys.exit(main())
