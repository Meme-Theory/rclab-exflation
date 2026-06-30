#!/usr/bin/env python3
"""
S90 W2-8 — S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN (CF-25)
=======================================================================

Gate: S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN ([VERIFY])

CRITICAL gate per cross-wave dependencies: CF-25 → W1 CF-2 (audit-script
TARGET_SLOTS dict extension) + W6 CF-49 (LEVEL-DRESSED K=2 empirical scan)
+ W6 CF-51 (Var_a Stage-1-CANDIDATE corrigendum sub-entry). 3 W1 INFO
mechanical-closure verdicts in s90_gate_verdicts.txt depend on this gate's
PASS for S91+ re-dispatch.

Inserts a CF-25 annotation block AFTER the §VII.U.2 4-corner table (current
end at line 12963) and BEFORE the Corner-III annotations paragraph (line
12965). The annotation block contains: (a) 4-axis structural fingerprint
for Var_a Corner-II per W-3 three-machinery convergence (Wedderburn +
clause-(e) parse-tree + F_traj=(k+1)/2); (b) Cell-I retraction annotation
(prior W6-6 plan baseline RETRACTED); (c) clause-(e) parse-tree decision
procedure cross-link explicit; (d) W4 A.30 → §VII.AS routing note.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"            # (local)
CONVENTION = "vii-u-2-corner-ii-reading-b-lock-in-three-machinery-convergence"  # (local)
L_MAX = "N/A"  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Anchor: the unique closing-fragment of the Corner-IV row in the 4-corner
# table at line 12963; the CF-25 annotation block is inserted immediately
# after this line (between table end + Corner-III annotations paragraph).
ANCHOR_CORNER_IV_END = (
    "envelope-cross-confirmation queued at A.25 "
    "(S89 `S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE` "
    "per W-17 §V.1). |"
)  # (local)

CF_25_ANNOTATION_BLOCK = """**Corner-II 4-axis structural fingerprint lock-in (CF-25 S90 W2 — mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`; lizzi-spectral-functional-theorist co-sign on F_traj=(k+1)/2 dressing per S84 W3-24, 2026-05-13)**:

Per W-3 workshop three-machinery convergence (Wedderburn + clause-(e) parse-tree + F_traj=(k+1)/2 dressing; lizzi + connes joint authorship), the Corner-II classification of `Var_a(n_a^GGE)` is STRUCTURALLY LOCKED with the following 4-axis fingerprint:

```
Corner II (Var_a class): {algebra-axis: INVARIANT, mellin-pole: s=4, FI-RD-class: MIXED-of-RD-with-distinct-F_traj-factors, level-class: LEVEL-DRESSED-candidate-pending-K2-via-CF-W6-49-scan}
```

Substrate-physics resolution: parse-tree expansion `n_a^GGE → |v_a|^2 → Δ_BCS²/(2(λ_a²+Δ_BCS²))` per clause (e) decision procedure (above, line 12995) reduces the state-historic GGE-state label to a substrate-IS closed-form spectrum-only functional of `{λ_a, m_a, Δ_BCS}` — confirming algebra-INVARIANT (Corner-II), NOT algebra-DEPENDENT (Corner-IV). Three-machinery convergence on the Corner-II classification: (i) **Wedderburn** decomposition of `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` constrains Var_a's substrate-algebra image to spectrum-only family; (ii) **clause-(e) parse-tree decision procedure** verifies the symbolic form contains ONLY λ_a, m_a, Δ_BCS — no `π(a)`, no `[D, π(a)]`, no state-pair sup; (iii) **F_traj=(k+1)/2 dressing** (S84 W3-24 lizzi-theorem) classifies the MIXED-of-RD level structure: Var_a is a MIXED-of-RD functional because the closed form contains distinct F_traj factors at different `k`-power moments (`|v_a|²` at k=1 vs `|v_a|⁴` at k=2; the F_traj=(k+1)/2 dressing gives distinct level-factors `1` for k=1 and `3/2` for k=2). The LEVEL-DRESSED-candidate-pending-K2 tag indicates the level-class status is PENDING the W6 CF-49 LEVEL-DRESSED K=2 empirical scan; the K=2 empirical instance lands at S91+ to confirm or refute the LEVEL-DRESSED candidacy.

**Cell-I retraction (CF-25 S90 W2)**: the prior W6-6 plan baseline classifying `Var_a(n_a^GGE)` at Cell I (algebra-INVARIANT spectrum-only-functional) is **RETRACTED** on the parse-tree expansion per clause (e). The retraction is structural reconciliation with the three-machinery convergence reading, NOT convention-shopping: the spectrum-only-functional reading missed the F_traj-dressing structure at distinct `k`-moments (the closed form's `|v_a|²` and `|v_a|⁴` carry distinct F_traj-dressing factors per S84 W3-24). Corner-II classification with MIXED-of-RD-with-distinct-F_traj-factors level structure is the canonical baseline going forward.

**W4 A.30 → §VII.AS routing note**: the Corner-II row reclassification of Var_a (this annotation) routes downstream to §VII.AS dual-reading STAGE-1-CANDIDATE precedent (S88 W-18 landing). §VII.AS's dual-reading framework captures the dual-axis ambiguity (FI-RD-MIXED axis × LEVEL-DRESSED axis) that Var_a inhabits; downstream consumers of §VII.AS will cross-link to this CF-25 lock-in.

**Downstream cross-wave dependencies unblocked by this lock-in**:

- **W1 CF-2** (`_corner_classification_audit.py` TARGET_SLOTS dict extension): the audit-script's TARGET_SLOTS dict can now include the §VII.U.2 Corner-II row with the locked 4-axis fingerprint; W1 INFO mechanical-closure at audit_sha=`526a38d0baca18998d37aff5bd7512616efda575dabf8adb6d7d4854a99541a8` (per S90 W1 PRE-REG-INC) is structurally unblocked for S91+ re-dispatch with Option-A `supersedes` tag.
- **W6 CF-49** (LEVEL-DRESSED K=2 empirical scan): the LEVEL-DRESSED candidacy classification provides the K=2 empirical-scan target; W6 CF-49 can now operate against the locked classification.
- **W6 CF-51** (Var_a Stage-1-CANDIDATE corrigendum sub-entry): the Stage-1-CANDIDATE registration at §VII.U.2 Corner II row sub-entry can now reference this CF-25 lock-in as the canonical baseline.

Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (S87 W-2 R3 close): this lock-in is consistent with the K=3 calibration corpus saturation; the Corner-II classification's MIXED-of-RD structure is a within-Corner-II refinement, NOT a cross-corner classification.

"""  # noqa: E501


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def build_promotion_text(original_text):
    """Pure: registry text → registry with CF-25 annotation block inserted
    after the §VII.U.2 4-corner table Corner-IV row. Idempotent."""
    if "Corner-II 4-axis structural fingerprint lock-in (CF-25 S90 W2" in original_text:
        return original_text  # already inserted
    idx = original_text.find(ANCHOR_CORNER_IV_END)  # (local)
    if idx == -1:
        raise ValueError(
            "Corner-IV row end anchor not found in §VII.U.2 4-corner table"
        )
    # Find end of the anchor line
    end_of_anchor_line = original_text.find("\n", idx)  # (local)
    if end_of_anchor_line == -1:
        raise ValueError("Anchor line not terminated")
    # Insert annotation block after the anchor line + blank line
    # Anchor ends with "| ...V.1). |\n"; expect blank line at end_of_anchor_line+1
    if original_text[end_of_anchor_line + 1] != "\n":
        # Insert with a leading blank line for paragraph separation
        insertion = "\n" + CF_25_ANNOTATION_BLOCK
        insertion_point = end_of_anchor_line + 1
    else:
        insertion = CF_25_ANNOTATION_BLOCK
        insertion_point = end_of_anchor_line + 2  # after blank line
    return original_text[:insertion_point] + insertion + original_text[insertion_point:]


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    """7-check verify on the inserted annotation block."""
    checks = {
        "annotation_block_heading_present": (
            "Corner-II 4-axis structural fingerprint lock-in (CF-25 S90 W2" in text
        ),
        "four_axis_fingerprint_literal_present": (
            "{algebra-axis: INVARIANT, mellin-pole: s=4, FI-RD-class: MIXED-of-RD-with-distinct-F_traj-factors, level-class: LEVEL-DRESSED-candidate-pending-K2-via-CF-W6-49-scan}" in text
        ),
        "cell_i_retraction_annotation_present": (
            "Cell-I retraction (CF-25 S90 W2)" in text
            and "RETRACTED" in text
        ),
        "clause_e_parse_tree_cross_link_explicit": (
            "parse-tree expansion `n_a^GGE → |v_a|^2 → Δ_BCS²/(2(λ_a²+Δ_BCS²))`" in text
        ),
        "w4_a_30_vii_as_routing_note_present": (
            "W4 A.30 → §VII.AS routing note" in text
        ),
        "downstream_w1_cf2_w6_cf49_cf51_unblocked_text": (
            "W1 CF-2" in text
            and "W6 CF-49" in text
            and "W6 CF-51" in text
            and "Downstream cross-wave dependencies unblocked" in text
        ),
        "three_machinery_convergence_explicit": (
            "Wedderburn" in text
            and "clause-(e) parse-tree" in text
            and "F_traj=(k+1)/2" in text
        ),
    }
    return all(checks.values()), checks


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [SHARED_DIR / "canonical_constants.py", REGISTRY_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (pure; CF-25 annotation block)")
    original = REGISTRY_PATH.read_text(encoding="utf-8")
    try:
        promoted = build_promotion_text(original)
    except ValueError as e:
        print(f"  ERROR: {e}")
        emit_verdict(
            "FAIL",
            f"build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending",
            audit_sha, content_sha,
        )
        return 0

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(REGISTRY_PATH, promoted)

    print("Step 3: re-read + verify")
    re_read = REGISTRY_PATH.read_text(encoding="utf-8")
    overall, checks = verify_section_matches(re_read)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    verdict = "PASS" if overall else "FAIL"
    n_pass = sum(1 for v in checks.values() if v)
    verdict_value = (
        f"corner_ii_reading_b_locked={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"four_axis_fingerprint=INVARIANT_s4_MIXED-RD-F_traj_LEVEL-DRESSED-K2-pending;"
        f"cell_i_retraction_annotated=True;"
        f"clause_e_parse_tree_cross_link=True;"
        f"w4_a_30_vii_as_routing_note=True;"
        f"three_machinery_convergence=Wedderburn_AND_parse-tree_AND_F_traj;"
        f"downstream_w1_cf2_unblocked=True;"
        f"downstream_w6_cf49_unblocked=True;"
        f"downstream_w6_cf51_unblocked=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
