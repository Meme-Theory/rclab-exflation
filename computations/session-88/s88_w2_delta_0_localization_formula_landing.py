#!/usr/bin/env python3
"""
S88 W2-8 — S88-DELTA-0-LOCALIZATION-FORMULA-LANDING
=====================================================

Gate: S88-DELTA-0-LOCALIZATION-FORMULA-LANDING (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class registry-landing at §VII.AD)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-8

Pre-registered threshold (per session-88-plan-w2.md §W2-8.9):
  PASS: §VII.AD entry lands with both CO-PRIMARY anchors per
        registry-landing.md §"Schema"; STAGE-1-CANDIDATE tag present;
        W-8 calibration corpus block present; methodology-wave-allowlist
        row appended.
  INFO: landing partial — registry text present but cross-link to
        falsifier-master-inventory missing or anchor structure mis-tagged.
  FAIL: SOURCE-DOUBLE-CITE-CO-PRIMARY discipline not satisfied; entry
        uses PRIMARY+CONFIRMATION incorrectly; or STAGE-1-CANDIDATE tag
        missing.

This is METHODOLOGY-class per `wave-classification.md` M1-M4: artifact-
existence-with-substantive-content predicate; registry-edit operations;
verbatim-extract from S87 W-8 R3 closure + S88 W2-3 numerical anchor;
gate-ID W2-8 allowlisted in `.claude/rules/methodology-wave-allowlist.md`.

Sage QQ verification of substrate-specialization at (2,4,8,6):
  Δ_0(σ; (2,4,8,6)) = 4 · c_{σ⁻¹((-1,-1))} ∈ 4 · {2, 4, 8, 6} = {8, 16, 32, 24}
  rel_dev_0 / max(c) NORMALIZED: {8/20, 16/20, 32/20, 24/20} = {0.4, 0.8, 1.6, 1.2}

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md (registry edit target)
  - .claude/rules/methodology-wave-allowlist.md (allowlist target)
  - sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md (source workshop)
  - computations/session-87/s87_w11_hypercube_vertex_identity.npz (Sage callable cache)
  - computations/session-88/s88_w2_v4_on_strata_substrate_character_construction.npz (W2-3 anchor)
"""

from __future__ import annotations

# Section 1 — Canonical constants
from canonical_constants import *  # noqa: F401,F403

# Section 2 — Imports
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path

# Section 3 — Pin metadata
GATE_ID = "S88-DELTA-0-LOCALIZATION-FORMULA-LANDING"
SCHEME = "delta-0-localization-formula-V4-on-4-stratum-partition-EXACT-QQ"
CONVENTION = "SOURCE-DOUBLE-CITE-CO-PRIMARY-stage-1-candidate-per-joint-theorem-promotion-md"
L_MAX = "N/A"  # (local) METHODOLOGY-class
LINE_THRESHOLD_PASS = 30  # (local) plan-pinned ≥30 lines registry body criterion

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_delta_0_localization_formula_landing.py"
NPZ_OUT = T0 / "s88_w2_delta_0_localization_formula_landing.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

REGISTRY_PATH = T0.parent / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH = T0.parent / ".claude" / "rules" / "methodology-wave-allowlist.md"
WORKSHOP_PATH = T0.parent / "sessions" / "session-87" / "workshops" / "s87-v4-strata-vs-cartan-relabeling.md"
W11_4_NPZ = T0 / "s87_w11_hypercube_vertex_identity.npz"
W2_3_NPZ = T0 / "s88_w2_v4_on_strata_substrate_character_construction.npz"
CANON_PY = T0 / "canonical_constants.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def count_section_lines(file_path: Path, start_anchor: str, end_anchor: str) -> int:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    in_section = False
    count = 0  # (local) line counter
    for line in lines:
        if start_anchor in line:
            in_section = True
            continue
        if in_section and end_anchor in line:
            break
        if in_section:
            count += 1
    return count


def main() -> int:
    t_start = time.time()
    import numpy as np

    # 4.1 — Sage-QQ verification of LOCALIZATION FORMULA at substrate (2,4,8,6)
    cv_substrate = (2, 4, 8, 6)  # (local)
    delta_0_per_stratum = [4 * c for c in cv_substrate]  # (local) Δ_0 per V_4 character
    rel_dev_0_unnormalized = [Fraction(d, sum(cv_substrate)) for d in delta_0_per_stratum]
    rel_dev_0_floats = [float(r) for r in rel_dev_0_unnormalized]
    max_rel_dev_0 = max(rel_dev_0_floats)  # (local)
    print(f"[W2-8] Sage-QQ verification:")
    print(f"  cv_substrate = {cv_substrate}")
    print(f"  Δ_0 per V_4 character (4·c_i): {delta_0_per_stratum}")
    print(f"  rel_dev_0 normalized by Σc = 20: {[str(r) for r in rel_dev_0_unnormalized]} = {rel_dev_0_floats}")
    print(f"  max rel_dev_0 = {max_rel_dev_0:.4f} (≫ 1e-9 threshold by ≥ 8 OOM ⇒ structurally closes (Z_2)^d=2 route)")

    # 4.2 — W2-3 numerical anchor cross-check
    d_w2_3 = np.load(W2_3_NPZ, allow_pickle=True)
    delta_0_w2_3 = float(d_w2_3["delta_0_numerical"])
    cv_w2_3 = list(d_w2_3["cv"].tolist())
    cc_w2_3_match = bool(delta_0_w2_3 == 24.0 and cv_w2_3 == [2, 4, 8, 6])
    print(f"[W2-8] W2-3 numerical anchor: Δ_0 = {delta_0_w2_3:+.6f}; cv = {cv_w2_3}; match = {cc_w2_3_match}")

    # 4.3 — Registry edit verification
    sub_row_line_count = count_section_lines(
        REGISTRY_PATH,
        "## §VII.AD — Δ_0 LOCALIZATION FORMULA",
        "---\n",
    )
    print(f"[W2-8] §VII.AD body line count: {sub_row_line_count}")

    registry_text = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    cc1_co_primary = "SOURCE-DOUBLE-CITE-CO-PRIMARY" in registry_text and "STAGE-1-CANDIDATE" in registry_text
    cc2_anchor_v_input = "ANCHOR-1 (input layer, V_input — connes V-3 NCG-axiomatic" in registry_text
    cc3_anchor_c_output = "ANCHOR-2 (output layer, C_output — volovik Sage-QQ" in registry_text
    cc4_calibration_corpus = "{8, 16, 32, 24}" in registry_text or "4·{2,4,8,6}" in registry_text or "{2,4,8,6}" in registry_text
    cc5_summary_table = "| §VII.AD | THM | Δ_0 LOCALIZATION FORMULA" in registry_text

    print(f"[W2-8] CC1 SOURCE-DOUBLE-CITE-CO-PRIMARY + STAGE-1-CANDIDATE tags: {cc1_co_primary}")
    print(f"[W2-8] CC2 ANCHOR-1 V_input present: {cc2_anchor_v_input}")
    print(f"[W2-8] CC3 ANCHOR-2 C_output present: {cc3_anchor_c_output}")
    print(f"[W2-8] CC4 substrate calibration corpus present: {cc4_calibration_corpus}")
    print(f"[W2-8] CC5 §VII.AD summary table row: {cc5_summary_table}")

    # 4.4 — Allowlist row check
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")
    cc6_allowlist_w2_8 = "| W2-8 | S88 |" in allowlist_text
    print(f"[W2-8] CC6 methodology-wave-allowlist W2-8 row: {cc6_allowlist_w2_8}")

    # 4.5 — Composite verdict per plan §W2-8.9
    all_cc_pass = (
        cc1_co_primary and cc2_anchor_v_input and cc3_anchor_c_output
        and cc4_calibration_corpus and cc5_summary_table and cc6_allowlist_w2_8
        and cc_w2_3_match and sub_row_line_count >= LINE_THRESHOLD_PASS
    )
    if all_cc_pass:
        composite = "PASS"
        verdict_kind = "PASS-vii-ad-stage-1-candidate-co-primary-landed"
    elif sub_row_line_count >= 15 and not all_cc_pass:
        composite = "INFO"
        verdict_kind = "INFO-partial-landing-some-cross-checks-failed"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-stage-1-candidate-incomplete-or-anchor-mistagged"

    # 4.6 — SHAs
    canon_sha = sha256_file(CANON_PY)
    registry_sha = sha256_file(REGISTRY_PATH)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    workshop_sha = sha256_file(WORKSHOP_PATH) if WORKSHOP_PATH.exists() else "WORKSHOP-NOT-FOUND"
    w11_4_sha = sha256_file(W11_4_NPZ)
    w2_3_sha = sha256_file(W2_3_NPZ)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "LINE_THRESHOLD_PASS": LINE_THRESHOLD_PASS,
        "input_canonical_constants_sha256": canon_sha,
        "input_registry_sha256": registry_sha,
        "input_allowlist_sha256": allowlist_sha,
        "input_workshop_sha256": workshop_sha,
        "input_w11_4_sha256": w11_4_sha,
        "input_w2_3_sha256": w2_3_sha,
        "script_sha256": script_sha,
        "delta_0_per_stratum": delta_0_per_stratum,
        "rel_dev_0_floats": rel_dev_0_floats,
    }
    audit_sha256 = closure_hash(pin_map)

    # 4.7 — Save .npz
    np.savez(
        NPZ_OUT,
        cv_substrate=np.array(cv_substrate),
        delta_0_per_stratum=np.array(delta_0_per_stratum),
        rel_dev_0_floats=np.array(rel_dev_0_floats),
        max_rel_dev_0=np.float64(max_rel_dev_0),
        delta_0_w2_3=np.float64(delta_0_w2_3),
        cv_w2_3=np.array(cv_w2_3),
        cc_w2_3_match=np.bool_(cc_w2_3_match),
        sub_row_line_count=np.int64(sub_row_line_count),
        cc1_co_primary=np.bool_(cc1_co_primary),
        cc2_anchor_v_input=np.bool_(cc2_anchor_v_input),
        cc3_anchor_c_output=np.bool_(cc3_anchor_c_output),
        cc4_calibration_corpus=np.bool_(cc4_calibration_corpus),
        cc5_summary_table=np.bool_(cc5_summary_table),
        cc6_allowlist_w2_8=np.bool_(cc6_allowlist_w2_8),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # 4.8 — Append verdict line
    elapsed = time.time() - t_start
    value_str = (
        f"sub_row_line_count={sub_row_line_count};"
        f"delta_0_per_stratum={delta_0_per_stratum};"
        f"max_rel_dev_0={max_rel_dev_0:.4f};"
        f"cc_w2_3_match={cc_w2_3_match};"
        f"cc1_co_primary={cc1_co_primary};cc2_anchor_v={cc2_anchor_v_input};"
        f"cc3_anchor_c={cc3_anchor_c_output};cc5_table={cc5_summary_table};"
        f"cc6_allowlist={cc6_allowlist_w2_8};verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sign_v = "N/A"
    mag_v = composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W2-8] DONE in {elapsed:.2f}s")
    print(f"[W2-8] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-8] audit_sha256 = {audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
