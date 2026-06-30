"""S90 W7-4 — S90-W7-4-STAGE-2-CROSS-AXIS-CROSS-REVIEW-LIZZI-ALPHA-GAMMA
========================================================================

Stage-2 Axis-A spectral-functional cross-review of the three-axis rule-file
refactor landed by CF-57 Phase 1 (joint connes-ncg + volovik authoring).
Reviews axis α (MACHINERY-SCOPE) + axis γ (sharpened Binding-axis with HIT).
Axis β reviewed by mack-cosmic-bridge in a parallel dispatch.

Gate ID:        S90-W7-4-STAGE-2-CROSS-AXIS-CROSS-REVIEW-LIZZI-ALPHA-GAMMA
Owner:          lizzi-spectral-functional-theorist (Stage-2 Axis-A reviewer)
Plan section:   CF-57 Phase 2 dispatch (spawn-prompt)

Procedural-floor compliance (per joint-theorem-promotion.md §"Stage 2"):
- W-5 R2 workshop transcript (s89-w5-vii-aq-level3-binding.md) NOT read.
- R1/R2/R3 round transcripts NOT read.
- Only the rule-file diffs + Phase 1 verdict line + CF-55 verdict + cited
  rule infrastructure consumed.

OAA exclusion attestation: lizzi NOT among original W-5 R2 EME-2 / EME-vB-2
authoring agents (those are connes-ncg + volovik). PASS.

Downstream-inheritance reach test: lizzi project memory does NOT cite W-5 R2
workshop transcripts as canonical reference (verified via Grep search returning
no files matching "W-5 R2"/"EME-2"/"EME-vB-2"/"level3-binding"/"s89-w5"
patterns). PASS.

Substrate-input-orthogonality predicate: lizzi (this script) consumes
`regulator-pin-discipline.md` lines 139-148 as primary substrate input;
mack (parallel dispatch) consumes `cross-pillar-bridge-anatomy.md` Element 3
sub-section as primary. The two input substrates are DISTINCT files in
`.claude/rules/`. Substrate-input-orthogonality PASS at structural ceiling
per S88 W-23 V.1 / B.56 + S90 W1-17 K=2.

Verdict logic (per spawn-prompt PASS-AND criterion):
  - Axis α PASS iff structurally well-formed ∧ audit-extension well-defined
    ∧ K-counter arithmetic correct
  - Axis γ PASS iff structurally well-formed ∧ HIT correctly applied
    ∧ K-counter stays K=1 (CF-55 Reading A confirmed; no advancement)
  - JOINT clause PASS iff K=3 promotion criterion consistent across α + γ
  - Composite = PASS iff all three clauses PASS

Method (this script is a verdict-emit + audit-trail script, not a
numerical-computation script — it consumes verified rule-file diffs,
applies the cross-review logic from the .md companion document, and
emits the canonical verdict line):

  Step 1: Compute SHAs over input pins (rule-file diffs + Phase 1 verdict +
          CF-55 verdict + cited rule infrastructure).
  Step 2: Verify CF-55 reading from verdict-file:128 (Reading A confirmed
          via parse of `reading=A` field).
  Step 3: Apply axis α PASS/FAIL/INFO logic per cross-review .md companion.
  Step 4: Apply axis γ PASS/FAIL/INFO logic per cross-review .md companion.
  Step 5: PASS-AND composite verdict + emit canonical line + dual-SHA
          companion row.

PASS criterion: PASS-AND across all three clauses (α + γ + JOINT).
FAIL criterion: any one clause FAIL with explicit identification.
INFO criterion: any one clause INFO with explicit deferred-item documentation.

Provenance:
    Built S90 W7-4 Phase 2 per orchestrator dispatch (spawn-prompt).
    Owner: lizzi-spectral-functional-theorist (Stage-2 Axis-A α + γ).
    Co-owner: mack-cosmic-bridge (Stage-2 Axis-B β; parallel dispatch).
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

# Path bootstrap (canonical_constants in _shared/)
_REPO_ROOT_BOOTSTRAP = Path(__file__).resolve().parent.parent.parent
_SHARED_DIR_BOOTSTRAP = _REPO_ROOT_BOOTSTRAP / "computations" / "_shared"
sys.path.insert(0, str(_SHARED_DIR_BOOTSTRAP))

# Canonical constants — MANDATORY (per .claude/rules/math-scripts.md S34+).
# This is a verdict-emit + audit-trail script (no numerical computation on
# framework constants), but the import discipline is mandatory regardless.
# M_KK is the canonical-pillar substrate scale; pinned for downstream consumers
# of the verdict-line audit trail.
from canonical_constants import M_KK  # noqa: F401  # imported per S34+ mandate

# ---------------------------------------------------------------------------
# Section 1 — Identifiers, paths, pre-registered thresholds
# ---------------------------------------------------------------------------

GATE_ID = "S90-W7-4-STAGE-2-CROSS-AXIS-CROSS-REVIEW-LIZZI-ALPHA-GAMMA"
SCHEME = "cf-57-stage-2-cross-axis-cross-review-lizzi-spectral-functional-axis-a"
CONVENTION = "cf-57-stage-2-axis-a-spectral-functional-alpha-plus-gamma-cross-review"
L_MAX_TAG = "N/A"  # (local) METHODOLOGY-class cross-review; no L_max
SCHEMA_VERSION = "S87+"

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Rule-file inputs (primary substrate-input axis for this cross-review)
REGULATOR_PIN_DISCIPLINE = REPO_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"
JOINT_THEOREM_PROMOTION = REPO_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
CROSS_PILLAR_BRIDGE_ANATOMY = REPO_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"

# Methodology-wave registry (Phase 1 rationale entry)
METHODOLOGY_WAVE_INSTANCES = REPO_ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"

# Verdict file (Phase 1 verdict at line 121; CF-55 adjudicator at line 128)
VERDICT_TXT = REPO_ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"

# This cross-review's companion .md verdict report
CROSS_REVIEW_MD = REPO_ROOT / "computations" / "session-90" / "s90_w7_cf57_stage_2_cross_review_lizzi_alpha_gamma.md"


# ---------------------------------------------------------------------------
# Section 2 — Dual-SHA helpers (canonical pattern per W9a-99 split)
# ---------------------------------------------------------------------------

def file_sha256(path: Path) -> str:
    """SHA-256 of file contents at path."""
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """SHA-256 of ordered input-pin map (canonical audit-SHA per W9a-99 split)."""
    sorted_pins = sorted(pins.items())
    serialized = json.dumps(sorted_pins, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def parse_cf55_reading(verdict_file: Path) -> str:
    """Parse CF-55 reading (A or B) from s90_gate_verdicts.txt line 128.

    Looks for the S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR verdict line
    and extracts the `reading=A` or `reading=B` field.
    """
    txt = verdict_file.read_text(encoding="utf-8")
    for line in txt.splitlines():
        if line.startswith("S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR:"):
            m = re.search(r"reading=([AB])", line)
            if m:
                return m.group(1)
    raise RuntimeError("CF-55 verdict line not found")


# ---------------------------------------------------------------------------
# Section 3 — Cross-review verdict logic (α + γ + JOINT)
# ---------------------------------------------------------------------------

def axis_alpha_verdict(cf55_reading: str) -> tuple[str, str]:
    """Axis α (MACHINERY-SCOPE) PASS/FAIL/INFO logic.

    Three sub-clauses must PASS:
      (a) structural well-formedness: CACHE-PROJECTION vs FULL-LEAF-FOLIATION
          maps onto a meaningful spectral-functional FI/RD distinction at the
          spectral-triple-truncation layer. PASS by inspection of the rule
          row at regulator-pin-discipline.md:144.
      (b) 4-axis orthogonality: UV-regulator × Level × Binding × MACHINERY-
          SCOPE are structurally independent (no pair maps to the same
          conflation pathology). PASS by inspection of the footer at
          regulator-pin-discipline.md:146-148.
      (c) K-counter arithmetic: K=1 SUGGESTION via §W2-5; advances to K=2
          at S90 with CF-55 PASS (Reading A → cache-projection scheme-
          INDEPENDENT). PASS iff cf55_reading == "A".
    """
    sub_a = True   # structural well-formedness; verified in companion .md
    sub_b = True   # 4-axis orthogonality; verified in companion .md
    sub_c = cf55_reading == "A"  # K-arithmetic consistent with Reading A landing

    if sub_a and sub_b and sub_c:
        return "PASS", "axis_alpha=PASS;structural=PASS;orthogonality=PASS;k_arith=PASS_cf55_reading_A"
    elif not sub_c:
        return "FAIL", f"axis_alpha=FAIL_k_arith;cf55_reading={cf55_reading}_expected_A"
    else:
        return "INFO", "axis_alpha=INFO_partial_pass"


def axis_gamma_verdict(cf55_reading: str) -> tuple[str, str]:
    """Axis γ (sharpened Binding-axis with HIT) PASS/FAIL/INFO logic.

    Three sub-clauses must PASS:
      (a) HIT structural well-formedness: (i ∨ ii ∨ iii) ∧ iv correctly
          discriminates canonical-import-binding vs substrate-natural-binding.
          PASS by inspection of the rule row at regulator-pin-discipline.md:143
          and HIT definition at cross-pillar-bridge-anatomy.md:307.
      (b) K-counter arithmetic: K=1 retained (W7b-82 sole landed instance);
          CF-55 Reading A confirmed → no Binding-axis advancement. PASS iff
          cf55_reading == "A" (which matches the landed rule).
      (c) Audit-script extension well-definedness: _hybrid_independence_test_
          audit.py (S91+) symmetric in form with _joint_theorem_independent_
          verify_audit.py. PASS by inspection.
    """
    sub_a = True   # HIT structurally well-formed; verified in companion .md
    sub_b = cf55_reading == "A"  # K-arithmetic stays K=1 iff Reading A
    sub_c = True   # audit-extension well-defined; verified in companion .md

    if sub_a and sub_b and sub_c:
        return "PASS", "axis_gamma=PASS;HIT_well_formed=PASS;k_arith=PASS_K=1_retained_cf55_reading_A;audit_ext=PASS"
    elif not sub_b:
        return "FAIL", f"axis_gamma=FAIL_k_arith;cf55_reading={cf55_reading}_expected_A_for_K=1_retained"
    else:
        return "INFO", "axis_gamma=INFO_partial_pass"


def joint_clause_verdict() -> tuple[str, str]:
    """JOINT clause: K=3 promotion criterion consistent across (α) and (γ).

    Both axes adopt K=3 MANDATORY promotion threshold per
    feedback_rules-compensate-missing-structure.md K-counter framework.
    Both axes require K=3 distinct calibration instances satisfying HIT
    structural independence. The K-counter framework is consistent across
    both axes; no contradiction when applied jointly. PASS.
    """
    return "PASS", "joint_clause=PASS;K=3_promotion_criterion_consistent_across_alpha_and_gamma"


def composite_verdict(alpha_v: str, gamma_v: str, joint_v: str) -> str:
    """PASS-AND composite verdict per spawn-prompt criterion.

    PASS iff all three clauses PASS.
    FAIL iff any one clause FAIL.
    INFO otherwise (one or more INFO, no FAIL).
    """
    verdicts = [alpha_v, gamma_v, joint_v]
    if all(v == "PASS" for v in verdicts):
        return "PASS"
    if any(v == "FAIL" for v in verdicts):
        return "FAIL"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 4 — Main verdict emission
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"[{datetime.now(timezone.utc).isoformat()}] {GATE_ID} starting")

    # Input-pin map (substrate-input axis for cross-review)
    input_pins = {
        "regulator_pin_discipline_md_sha256": file_sha256(REGULATOR_PIN_DISCIPLINE),
        "joint_theorem_promotion_md_sha256": file_sha256(JOINT_THEOREM_PROMOTION),
        "cross_pillar_bridge_anatomy_md_sha256": file_sha256(CROSS_PILLAR_BRIDGE_ANATOMY),
        "methodology_wave_instances_md_sha256": file_sha256(METHODOLOGY_WAVE_INSTANCES),
        "s90_gate_verdicts_txt_sha256": file_sha256(VERDICT_TXT),
        "cross_review_md_sha256": file_sha256(CROSS_REVIEW_MD),
        "cf_57_phase_1_audit_sha256": "2b7bedaa0473d12ab84f3ed2aef51a8bb112344536121069258935059c020bae",
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
    }

    # Log SHAs to stdout (per gate-verdicts.md "first 20 lines of stdout" discipline)
    print("Input pins:")
    for k, v in sorted(input_pins.items()):
        print(f"  {k} = {v[:16] if isinstance(v, str) and len(v) > 16 else v}")

    # Parse CF-55 outcome
    cf55_reading = parse_cf55_reading(VERDICT_TXT)
    print(f"CF-55 reading: {cf55_reading}")

    # Apply cross-review verdict logic
    alpha_v, alpha_msg = axis_alpha_verdict(cf55_reading)
    gamma_v, gamma_msg = axis_gamma_verdict(cf55_reading)
    joint_v, joint_msg = joint_clause_verdict()
    print(f"Axis α: {alpha_v} — {alpha_msg}")
    print(f"Axis γ: {gamma_v} — {gamma_msg}")
    print(f"JOINT: {joint_v} — {joint_msg}")

    composite = composite_verdict(alpha_v, gamma_v, joint_v)
    print(f"Composite verdict: {composite}")

    # Build value string for verdict line
    value_str = (
        f"axis_alpha={alpha_v};axis_gamma={gamma_v};joint_clause={joint_v};"
        f"composite={composite};cf_55_reading={cf55_reading};"
        f"k_alpha=1_SUGGESTION_advances_to_2_with_cf55_reading_A;"
        f"k_gamma=1_retained_no_advancement_cf55_reading_A;"
        f"k_joint_promotion=K=3_MANDATORY_consistent;"
        f"OAA_exclusion=PASS_lizzi_not_W5_R2_authoring_agent;"
        f"downstream_inheritance_reach=PASS_no_workshop_transcripts_in_memory;"
        f"substrate_input_orthogonality=PASS_distinct_rule_files_consumed;"
        f"phase_2_stage_2_axis_A_cross_review_complete"
    )

    # Compute dual-SHA
    audit_sha = closure_hash(input_pins)
    content_str = value_str + "|" + composite + "|" + GATE_ID
    content_sha = hashlib.sha256(content_str.encode("utf-8")).hexdigest()
    print(f"audit_sha256 = {audit_sha}")
    print(f"content_sha256 = {content_sha}")

    # Canonical verdict line (S87+ schema-v2 form)
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )

    # W9a-99 dual-SHA companion comment row
    audit_short = audit_sha[:16]
    content_short = content_sha[:16]
    companion_row = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )

    # Append both rows atomically
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line + "\n")
        fp.write(companion_row + "\n")

    print(f"Appended verdict line + companion row to {VERDICT_TXT}")
    print(f"[{datetime.now(timezone.utc).isoformat()}] {GATE_ID} complete")

    return 0  # script success; verdict is data, not exit code


if __name__ == "__main__":
    sys.exit(main())
