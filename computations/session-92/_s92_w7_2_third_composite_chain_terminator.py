#!/usr/bin/env python3
"""
S92 §W7-2 — THIRD composite chain-terminator (Option-A Class-6 correction)
===========================================================================

Minimal append helper. Emits ONE new composite canonical line for gate
`S92-W7-CF-W8-CONSOLIDATED-11-VII-AY-W8-7-RE-DISPATCH-POST-CORRIGENDUM`
that re-instates the honest composite=FAIL and TERMINATES the Option-A
supersession chain at FAIL.

Audit-trail defect being corrected (per `gate-verdicts.md §"Option A —
sig_5 remediation pathway under absolute verdict permanence"` — correcting
a Class-6 error is an enumerated valid Option-A corrective reason):

  - Line 221: composite=FAIL audit_sha256=2018915e... supersedes=92a5ed6d... (S91 §W8-7) [HONEST]
  - Line 230: composite=PASS audit_sha256=97f3866a... supersedes=2018915e...      [CLASS-6: mid-run
              threshold-loosening 1e-5 → 2e-5; iterate-until-PASS per
              v3-closure-recovery.md PROHIBITED_ACTIONS Class 6]

  Under the Option-A clause-3 mechanical "latest non-superseded" reading,
  a downstream consumer (/weave --update, _consolidate_t3_intake.py,
  v3-closure-audit) EXCLUDES 2018915e (named in 97f3866a's supersedes) and
  reads 97f3866a (the Class-6 PASS) as canonical. THE FIX: emit a THIRD
  composite line that supersedes 97f3866a and re-instates FAIL, so the
  latest-non-superseded canonical resolves to composite=FAIL.

This helper:
  - DOES NOT touch lines 221 or 230 (absolute verdict permanence; both retained).
  - DOES NOT re-emit the 3 per-axis lines.
  - ONLY appends the one new third composite canonical line + dual-SHA companion
    + schema-v2 3-tuple companion (atomic single open("a") write).

audit_sha256 computed from closure_hash(input_pin_map) per the canonical
dual-SHA discipline; the supersedes target (97f3866a, full 64-char) is IN
the pin map → the new audit_sha256 is provably distinct from both prior
composites (sig_5 uniqueness preserved per v3-closure-recovery.md).
"""

from __future__ import annotations

import sys  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

# Canonical constants import (MANDATORY per computations/_shared/CLAUDE.md S34+).
# This chain-terminator helper re-emits a verdict line; it does not consume a
# framework constant numerically, but the import satisfies the canonical-import
# discipline and pins canonical_constants.py into the audit pin map below.
from canonical_constants import substrate_cocycle_ratio_67_88  # noqa: E402,F401

import hashlib  # noqa: E402
import json  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"

GATE_ID = "S92-W7-CF-W8-CONSOLIDATED-11-VII-AY-W8-7-RE-DISPATCH-POST-CORRIGENDUM"  # (local)
SCHEME = "joint-theorem-promotion-stage-2-3-axis-cross-axis-independent-verify"    # (local)
CONVENTION = (
    "post-corrigendum-substrate-input-orthogonality-K3-MANDATORY-"
    "axis-A-vdd-axis-B-primary-mack-axis-B-cross-pillar-specialist-spectral-geometer"
)                                                                          # (local)
L_MAX = "N/A"                                                              # (local)

# Supersession targets (full 64-char)
CLASS_6_CORRECTIVE_AUDIT_SHA = (
    "97f3866ade348264b0fb6d8e17c2a67b770bd4575a863358aad529e030c12716"
)                                                                          # (local) Class-6 PASS line 230 — THIS is what the new line supersedes
FIRST_HONEST_FAIL_AUDIT_SHA = (
    "2018915e6bff84612e0e57e350ff15d250880d511d9609811beacb32235b18ae"
)                                                                          # (local) first honest FAIL line 221 (transitive ancestor; NOT touched)
S91_W8_7_ORIGIN_AUDIT_SHA = (
    "92a5ed6d62e1ccb56314750a20d4e7a6f36e5d447552c3f003f1b4932c12677c"
)                                                                          # (local) S91 §W8-7 composite FAIL (transitive origin)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                   # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering).

    Per `.claude/templates/script-template.py` closure_hash pattern +
    `v3-closure-recovery.md` sig_5 remediation: audit_sha256 MUST be computed
    from closure_hash(input_pin_map), NEVER hardcoded.
    """
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def main() -> int:
    # Input pin map. The supersedes target (97f3866a) is INCLUDED so the
    # resulting audit_sha256 is provably distinct from both prior composites.
    # File-pin SHAs anchor the audit to the on-disk state at emission time.
    script_path = Path(__file__).resolve()                                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"                  # (local)
    composite_script_path = SESSION_DIR / "s92_w7_2_vii_ay_w8_7_re_dispatch_post_corrigendum.py"  # (local)
    registry_path = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)

    pins = {
        "_gate_id": GATE_ID,
        "_emission": "third-composite-chain-terminator",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_verdict": "FAIL",
        "_supersedes_target_class_6_corrective": CLASS_6_CORRECTIVE_AUDIT_SHA,
        "_transitive_first_honest_fail": FIRST_HONEST_FAIL_AUDIT_SHA,
        "_transitive_s91_w8_7_origin": S91_W8_7_ORIGIN_AUDIT_SHA,
        "computations/session-92/_s92_w7_2_third_composite_chain_terminator.py": sha256_of(script_path),
        "computations/_shared/canonical_constants.py": sha256_of(canonical_path),
        "computations/session-92/s92_w7_2_vii_ay_w8_7_re_dispatch_post_corrigendum.py": sha256_of(composite_script_path),
        "sessions/permanent-results-registry.md": sha256_of(registry_path),
    }                                                                      # (local)

    audit_sha = closure_hash(pins)                                         # (local)
    # content_sha256 = sha256(this helper script bytes) per dual-SHA split.
    content_sha = hashlib.sha256(script_path.read_bytes()).hexdigest()     # (local)

    # Sig_5 distinctness check (defensive)
    assert audit_sha != CLASS_6_CORRECTIVE_AUDIT_SHA, "audit_sha collides with Class-6 corrective"
    assert audit_sha != FIRST_HONEST_FAIL_AUDIT_SHA, "audit_sha collides with first honest FAIL"
    assert audit_sha != S91_W8_7_ORIGIN_AUDIT_SHA, "audit_sha collides with S91 origin"

    value_string = (
        f"composite=FAIL;"
        f"cond1_axis_a_pass=True;"
        f"cond2_axis_b_primary_pass=False;"
        f"cond3_axis_b_cross_pillar_specialist_pass=True;"
        f"cond4_JOINT_clause_pass_and_three_axis=False;"
        f"cond5_substrate_input_orthogonality=True;"
        f"class_6_corrective_disregarded={CLASS_6_CORRECTIVE_AUDIT_SHA};"
        f"reason=mid_run_threshold_loosening_1e-5_to_2e-5_iterate_until_PASS;"
        f"honest_verdict_reinstated=composite_FAIL_per_first_emission_{FIRST_HONEST_FAIL_AUDIT_SHA[:16]};"
        f"axis_b_primary_FAIL_at_canonical_constants_py_276_publication_precision_floor_Class_8_3;"
        f"substrate_IS_hochschild_kunneth_morita_invariance_theorem_INTACT_at_structural_ceiling;"
        f"chain_terminated_at_FAIL=this_line_supersedes_class_6_PASS_97f3866a_latest_non_superseded_resolves_to_FAIL;"
        f"transitive_chain=S91_W8_7_FAIL_92a5ed6d_to_S92_first_FAIL_2018915e_to_S92_class6_PASS_97f3866a_DISREGARDED_to_this_third_FAIL;"
        f"option_a_corrective_reason=correcting_class_6_error_per_gate_verdicts_md_option_a_enumerated_valid_reason"
    )                                                                      # (local)

    canonical = (
        f"{GATE_ID}: FAIL -- value={value_string!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"supersedes={CLASS_6_CORRECTIVE_AUDIT_SHA} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )                                                                      # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} THIRD composite chain-terminator dual-SHA companion row (W9a-99 split); "
        f"supersedes={CLASS_6_CORRECTIVE_AUDIT_SHA} (Class-6 corrective PASS at line 230) per Option A clause 2 (gate-verdicts.md); "
        f"re-instates honest composite=FAIL; terminates Option-A supersession chain at FAIL; "
        f"transitive chain: S91 §W8-7 FAIL ({S91_W8_7_ORIGIN_AUDIT_SHA[:16]}) -> S92 first FAIL ({FIRST_HONEST_FAIL_AUDIT_SHA[:16]}) -> "
        f"S92 Class-6 PASS DISREGARDED ({CLASS_6_CORRECTIVE_AUDIT_SHA[:16]}) -> this third FAIL ({audit_sha[:16]})\n"
    )                                                                      # (local)
    tuple_row = (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {GATE_ID} THIRD composite chain-terminator 3-tuple annotation (S87 schema-v2; [CHAIN] trigger requires 3-tuple); composite=FAIL\n"
    )                                                                      # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(tuple_row)

    print(f"=== {GATE_ID} THIRD composite chain-terminator ===")
    print(f"  verdict: FAIL")
    print(f"  supersedes (Class-6 corrective): {CLASS_6_CORRECTIVE_AUDIT_SHA}")
    print(f"  new audit_sha256:   {audit_sha}")
    print(f"  new content_sha256: {content_sha}")
    print(f"  sig_5 distinctness: PASS (distinct from 2018915e, 97f3866a, 92a5ed6d)")
    print(f"  chain now terminates at FAIL; latest-non-superseded = composite=FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
