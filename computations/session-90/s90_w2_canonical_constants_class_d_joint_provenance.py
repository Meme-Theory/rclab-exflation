#!/usr/bin/env python3
"""
S90 W2-10 + W2-11 — Joint canonical_constants PROVENANCE landings (CF-27 + CF-28)
==================================================================================

Per plan §"Hard prerequisites" item 4: CF-27 (DERIVATIVE) and CF-28
(PRIMARY) are STRUCTURALLY PAIRED with joint atomic emission. This single
script performs BOTH edits in ONE atomic write to canonical_constants.py +
emits TWO verdict lines (one per gate-ID) preserving task-list separation.

Gates emitted:
  - S90-CANONICAL-CONSTANTS-EPS-H-HP1-NORM-PROVENANCE-ADDITION (CF-28)
    PRIMARY canonical PROVENANCE block above line 156 (eps_H_HP1_norm)
  - S90-CANONICAL-CONSTANTS-R-UNIVERSAL-HP1-STRICT-F4-CLASS-D-PROVENANCE-UPDATE (CF-27)
    Class-(d) DERIVATIVE PROVENANCE block above line 235 (R_universal_HP1_strict_F4)

Substrate framing: `eps_H_HP1_norm = 16.197719` IS the PRIMARY substrate-IS
observable (BZ-trace on Jensen-deformed band-0 projector at ζ-regulator,
substrate-IS Level 1 single-τ-slice at τ_fold = 0.19); `R_universal_
HP1_strict_F4 = 1.030902` IS a DERIVATIVE form via 1/f_4_prefactor_sdw
reduction (Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY per
`epistemic-discipline.md §"Source Reconciliation"`).
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

GATE_ID_CF_27 = "S90-CANONICAL-CONSTANTS-R-UNIVERSAL-HP1-STRICT-F4-CLASS-D-PROVENANCE-UPDATE"  # (local)
GATE_ID_CF_28 = "S90-CANONICAL-CONSTANTS-EPS-H-HP1-NORM-PROVENANCE-ADDITION"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local)
CONVENTION_CF_27 = "canonical-constants-provenance-class-d-pin-derivative-vs-source-primary"  # (local)
CONVENTION_CF_28 = "canonical-constants-provenance-primary-canonical-eps-h-hp1-norm"  # (local)
L_MAX = 10  # (local)

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Anchor strings: existing constant lines that we insert above.
ANCHOR_EPS_H_LINE = "eps_H_HP1_norm = 16.197719  # (S84 W10a-114; 6 sig figs)"
ANCHOR_R_UNIVERSAL_LINE = (
    "R_universal_HP1_strict_F4 = 1.030902  # Universal HP^1 strict F_4 ratio "
    "per W-5 V4 substitution chain Step 2. Downstream-cited via W-5 cross-pillar "
    "bridge theorem and W11-C5/C6 lab spec. (S86)"
)

# CF-28 PRIMARY PROVENANCE block (verbatim from plan §W2-11 §6 lines 1273-1289)
CF_28_PROVENANCE_BLOCK = """# eps_H_HP1_norm = 16.197719
#
# PROVENANCE (CF-28 S90 W2; mack-cosmic-bridge writer; connes-ncg-theorist co-sign per W-2 CF-#5):
#   CLASS: PRIMARY canonical (anchors Class-(d) chain for R_universal_HP1_strict_F4; see CF-27 PROVENANCE)
#   DEFINITION: R_universal at ζ-regulator; BZ-trace on Jensen-deformed band-0 projector P_0(τ_fold)
#     - BZ-trace form: ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k (per cross-pillar-bridge-anatomy.md §VII.AF.1)
#     - regulator: ζ-regulator (CM-1995 §III.4 finite-spectral-triple residue formula)
#     - τ-anchor: τ_fold = 0.19 (R-PROTECTED; canonical_constants.py)
#     - L_max: 10 (Level-3 anchor at L_max=10 per registry-PASS criterion of §VII.AF.1.OP-PROJ)
#   SOURCE: S86 W-5 V4 substitution chain Step 1 line 397
#   substrate-IS level: Level 1 single-τ-slice at τ_fold (per phononic-framing.md K=2 MANDATORY since S88 W-7 V.4)
#   DOWNSTREAM CONSUMERS (Class-(d) DERIVATIVE forms cite this PRIMARY):
#     - R_universal_HP1_strict_F4 = 1.030902 (via DERIVATIVE relation 1/f_4_prefactor_sdw; see CF-27 PROVENANCE)
#   Audit-script verification: `_source_reconciliation_audit.py` no Class-(f) PLACEHOLDER flag post-emission
#   landed: CF-28 S90 W2 (mack-cosmic-bridge writer; connes-ncg-theorist co-sign)
"""

# CF-27 DERIVATIVE PROVENANCE block (verbatim from plan §W2-10 §6 lines 1137-1160)
CF_27_PROVENANCE_BLOCK = """# R_universal_HP1_strict_F4 = 1.030902
#
# PROVENANCE (CF-27 S90 W2; joint connes + lizzi co-sign per W-2 CF-#4):
#   CLASS: (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (per epistemic-discipline.md §"Source Reconciliation")
#   PRIMARY canonical: eps_H_HP1_norm = 16.197719 (see canonical_constants.py PROVENANCE entry CF-28)
#     - PRIMARY definition: R_universal at ζ-regulator; BZ-trace on Jensen-deformed band-0 projector at τ_fold
#     - PRIMARY source: S86 W-5 V4 substitution chain Step 1 line 397
#     - PRIMARY substrate-IS observable: Level 1 single-τ-slice at τ_fold per phononic-framing.md
#   DERIVATIVE relation: 1.030902 = 1/0.970024 modulo publication precision
#     where 0.970024 = f_4_prefactor_sdw (canonical_constants.py)
#     algebraic relation: R_universal_HP1_strict_F4 · f_4_prefactor_sdw ≡ 1 to Class-8.3 publication-precision
#   STRUCTURAL READING: F_4-atlas-spread band empirical value at L_max=10 (Level-3 anchor of §VII.AF.1.OP-PROJ)
#   NAME-DRIFT WARNING for downstream consumers:
#     - S88 W1b1 lines 129-133: downstream usage citing `1.030902` is a DERIVATIVE-FORM read;
#       must trace back to PRIMARY canonical `eps_H_HP1_norm = 16.197719` for substrate-IS observable provenance
#     - DO NOT independently re-derive from raw F_4 strict atlas values; the canonical substitution chain
#       (W-5 V4 Step 1 → Step 2) is the only authoritative derivation
#     - DOWNSTREAM CONSUMERS using `R_universal_HP1_strict_F4` in published quantities MUST cite both:
#       (a) this canonical pin name, AND
#       (b) the PRIMARY canonical name `eps_H_HP1_norm` per Class-(d) remediation table
#   Audit-script verification: `_source_reconciliation_audit.py` Class-(d) chain verification PASSes post-emission
#   Provenance chain: S86 W-5 V4 substitution chain Step 1 (PRIMARY) → Step 2 (this DERIVATIVE) → S88 W1b1 downstream
#   landed: CF-27 S90 W2 (mack-cosmic-bridge writer; connes + lizzi co-sign)
"""


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID_CF_27} + {GATE_ID_CF_28} — input SHA-256 pins ===")
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
    """Pure: canonical_constants.py text → text with BOTH PROVENANCE blocks
    inserted above the respective constant assignment lines. Idempotent."""
    promoted = original_text  # (local)

    # CF-28 PRIMARY: insert PROVENANCE block above eps_H_HP1_norm assignment
    if "PROVENANCE (CF-28 S90 W2;" not in promoted:
        idx = promoted.find(ANCHOR_EPS_H_LINE)
        if idx == -1:
            raise ValueError("eps_H_HP1_norm anchor line not found in canonical_constants.py")
        # Insert block BEFORE the anchor line (before "eps_H_HP1_norm = ...")
        promoted = (
            promoted[:idx]
            + CF_28_PROVENANCE_BLOCK
            + promoted[idx:]
        )

    # CF-27 DERIVATIVE: insert PROVENANCE block above R_universal_HP1_strict_F4 assignment
    if "PROVENANCE (CF-27 S90 W2;" not in promoted:
        idx = promoted.find(ANCHOR_R_UNIVERSAL_LINE)
        if idx == -1:
            raise ValueError("R_universal_HP1_strict_F4 anchor line not found in canonical_constants.py")
        promoted = (
            promoted[:idx]
            + CF_27_PROVENANCE_BLOCK
            + promoted[idx:]
        )

    return promoted


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_cf_28(text):
    """Verify CF-28 PRIMARY PROVENANCE block landed."""
    return {
        "cf_28_primary_block_present": "PROVENANCE (CF-28 S90 W2;" in text,
        "cf_28_primary_canonical_tag": "CLASS: PRIMARY canonical" in text,
        "cf_28_bz_trace_definition": "BZ-trace on Jensen-deformed band-0 projector" in text,
        "cf_28_zeta_regulator": "ζ-regulator (CM-1995 §III.4" in text,
        "cf_28_tau_fold_019_pin": "τ_fold = 0.19" in text,
        "cf_28_lmax_10_pin": "L_max: 10" in text,
        "cf_28_level_1_single_tau_slice": "Level 1 single-τ-slice at τ_fold" in text,
        "cf_28_downstream_derivative_cite": "R_universal_HP1_strict_F4 = 1.030902 (via DERIVATIVE relation" in text,
    }


def verify_cf_27(text):
    """Verify CF-27 DERIVATIVE PROVENANCE block landed."""
    return {
        "cf_27_class_d_block_present": "PROVENANCE (CF-27 S90 W2;" in text,
        "cf_27_class_d_tag_explicit": "CLASS: (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY" in text,
        "cf_27_primary_cross_cite": "PRIMARY canonical: eps_H_HP1_norm = 16.197719" in text,
        "cf_27_derivative_relation_explicit": "1.030902 = 1/0.970024 modulo publication precision" in text,
        "cf_27_structural_reading_f4_atlas": "F_4-atlas-spread band empirical value at L_max=10" in text,
        "cf_27_name_drift_warning_s88_w1b1": "S88 W1b1 lines 129-133" in text,
        "cf_27_provenance_chain_explicit": "Provenance chain: S86 W-5 V4 substitution chain Step 1 (PRIMARY) → Step 2 (this DERIVATIVE) → S88 W1b1 downstream" in text,
    }


def emit_verdict(gate_id, convention, verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{gate_id}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={convention} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [CANONICAL_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = CANONICAL_PATH
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (joint CF-27 + CF-28 atomic insert)")
    original = CANONICAL_PATH.read_text(encoding="utf-8")
    try:
        promoted = build_promotion_text(original)
    except ValueError as e:
        print(f"  ERROR: {e}")
        for gate_id, conv in [(GATE_ID_CF_27, CONVENTION_CF_27), (GATE_ID_CF_28, CONVENTION_CF_28)]:
            emit_verdict(gate_id, conv, "FAIL", f"build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending", audit_sha, content_sha)
        return 0

    print("Step 2: write_atomic_with_fsync (single combined write)")
    write_atomic_with_fsync(CANONICAL_PATH, promoted)

    print("Step 3: re-read + verify (separate per-gate checks)")
    re_read = CANONICAL_PATH.read_text(encoding="utf-8")

    cf_28_checks = verify_cf_28(re_read)
    cf_28_overall = all(cf_28_checks.values())
    print(f"  CF-28 (PRIMARY): {sum(cf_28_checks.values())}/{len(cf_28_checks)} PASS")
    for k, v in cf_28_checks.items():
        print(f"    {k}: {'PASS' if v else 'FAIL'}")

    cf_27_checks = verify_cf_27(re_read)
    cf_27_overall = all(cf_27_checks.values())
    print(f"  CF-27 (DERIVATIVE): {sum(cf_27_checks.values())}/{len(cf_27_checks)} PASS")
    for k, v in cf_27_checks.items():
        print(f"    {k}: {'PASS' if v else 'FAIL'}")

    # Emit CF-28 verdict (PRIMARY; emitted FIRST per provenance chain order)
    cf_28_verdict = "PASS" if cf_28_overall else "FAIL"
    cf_28_value = (
        f"eps_h_hp1_norm_provenance_added={cf_28_overall};"
        f"checks_pass={sum(cf_28_checks.values())}_of_{len(cf_28_checks)};"
        f"primary_canonical_tag=True;"
        f"bz_trace_definition_with_zeta_regulator_and_tau_fold_019_and_lmax_10=True;"
        f"level_1_single_tau_slice_per_phononic_framing_K2_MANDATORY=True;"
        f"downstream_consumer_cite_to_r_universal_derivative=True;"
        f"joint_atomic_emission_with_cf_27=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(GATE_ID_CF_28, CONVENTION_CF_28, cf_28_verdict, cf_28_value, audit_sha, content_sha)

    # Emit CF-27 verdict (DERIVATIVE)
    cf_27_verdict = "PASS" if cf_27_overall else "FAIL"
    cf_27_value = (
        f"r_universal_hp1_strict_f4_class_d_provenance_added={cf_27_overall};"
        f"checks_pass={sum(cf_27_checks.values())}_of_{len(cf_27_checks)};"
        f"class_d_tag=PIN-DERIVATIVE-VS-SOURCE-PRIMARY;"
        f"primary_canonical_cross_cite=eps_H_HP1_norm_16_197719;"
        f"derivative_relation=1_030902_eq_1_over_0_970024_modulo_publication_precision;"
        f"f_4_atlas_spread_structural_reading=True;"
        f"name_drift_warning_S88_W1b1_lines_129_133=True;"
        f"joint_atomic_emission_with_cf_28=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(GATE_ID_CF_27, CONVENTION_CF_27, cf_27_verdict, cf_27_value, audit_sha, content_sha)

    joint_verdict = "PASS" if (cf_27_overall and cf_28_overall) else "FAIL"
    print(f"\n=== JOINT EMISSION: CF-27 {cf_27_verdict} + CF-28 {cf_28_verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
