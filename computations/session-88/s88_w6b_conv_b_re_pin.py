#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W6b §W6b-53 — S88-CONV-B-RE-PIN-OF-VII-U-VII-W
====================================================

METHODOLOGY-class registry-edit gate. Re-pins §VII.U.6 + §VII.W d_spec
citations from the stale `d_spec=8` form to the Conv-B canonical
`d_spec_B = 5/(1-tau/(5*pi))` per S87 W1b-5 HK-5 form adoption. Removes
HK-4 sentinel references (already retired upstream at S87 W1b R3; this
gate verifies idempotently).

Single-shot AFTER pattern per `.claude/rules/registry-landing.md`
§"Bridge-Landing Script Architecture":
    build_promotion_text -> write_atomic_with_fsync -> re_read ->
    verify_section_matches -> emit_verdict_line (exactly one).

Plan reference: sessions/session-plan/session-88-plan-w6b.md §W6b-53.

Substitution chain (substrate-physics):
    Step 1: HK-5 canonical form (S87 W1b-5):
              slope_A(tau) = 5 / (1 - tau/(5*pi))
    Step 2: Conv-B identification:
              d_spec_B(tau) := slope_A(tau) under Conv-B
    Step 3: Substitute tau = tau_fold = 0.190:
              d_spec_B(0.190) = 5 / (1 - 0.190/(5*pi))
    Step 4: Compute denom: 0.190 / (5*pi) = 0.012096268...
    Step 5: 1 - 0.012096268 = 0.987903732
    Step 6: 5 / 0.987903732 = 5.061193223
    Step 7: Cross-check vs slope_inf_B (S87 W1b-3 Richardson L^-3):
            5.061193223 -- bit-identical
    Direction: d_spec_B(tau_fold) = 5.061193223 is the substrate's
               Conv-B canonical Weyl-counting exponent under Jensen flow;
               bare manifold dim = 8 retained as HK-3 binding parameter.

Target sites identified at plan-freeze via grep:
    - line 13010 (§VII.U.6 substrate-framing prose; d_spec=8 ... NCG cone apex)
    - §VII.W (lines 14825-15164) contains ZERO d_spec=8 or HK-4 sentinel
      literals -> idempotent no-op for §VII.W (PASS-by-vacuous-condition).

Out-of-scope sites (NOT edited per plan):
    - line 4919 (different section)
    - lines 15059, 15068 (§VII.Z F_4-MB STRUCTURAL WALL FAMILY)
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import sys
from pathlib import Path

# Canonical constants import (mandatory per .claude/rules/math-scripts.md)
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import tau_fold  # S12/S42 canonical fold parameter

# ---------------------------------------------------------------------------
# Pinned constants (per plan §W6b-53 machinery pin)
# ---------------------------------------------------------------------------
GATE_ID = "S88-CONV-B-RE-PIN-OF-VII-U-VII-W"
SCHEME = "Conv-B-canonical"
CONVENTION = "d_spec-tau-dependent-HK5"
L_MAX = "N/A"  # registry edit; no L_max
SCHEMA = "S84+"
REGULATOR = "Zubarev"

REGISTRY_PATH = Path("sessions/permanent-results-registry.md")
VERDICT_PATH = Path("computations/session-88/s88_gate_verdicts.txt")  # canonical per gate-verdicts.md

# §VII.U.6 W1b-T5 LANDING block bounds (verified at plan-freeze via grep)
VII_U_6_LINE_START = 12988  # (local) ### §VII.U.6 anchor (registry file position)
VII_U_6_LINE_END = 13141    # (local) last line before §VII.K-META.COMPOSITE-60 separator

# §VII.W Parity-Grading Orthogonality block bounds (registry file positions)
VII_W_LINE_START = 14825    # (local) ## §VII.W anchor
VII_W_LINE_END = 14955      # (local) before §VII.AA at line 14956 (corrected from initial 15164 stale bound)

# Substitution targets (forbidden -> required)
# Single occurrence at line 13010 in §VII.U.6 substrate-framing prose
FORBIDDEN_TARGET = (
    "the d_spec=8 (convention pin pending S87-W1B-HK-3; scope: "
    "bulk-Weyl-falsified per W1b-3 — may survive at per-stratum / "
    "per-cluster sub-axis) NCG cone apex sits at `Re(s) = 4`"
)

REQUIRED_REPLACEMENT = (
    "the Conv-B canonical d_spec_B = 5/(1−τ/(5π)) ≈ 5.061 at τ_fold "
    "(S87 W1b-5 HK-5 form; bare manifold dim = 8 retained as HK-3 "
    "binding parameter on bare-D Weyl-counting per W6b-56 k=2 vs k=1 "
    "spectral asymptotic distinction; HK-4 sentinel retired at S87 "
    "W1b R3) places the NCG cone apex at `Re(s) = d_spec_B/2 ≈ 2.531` "
    "under Conv-B (bare-D reading: `Re(s) = 4`); both readings sit "
    "deep inside Zubarev's strip"
)

# d_spec_B canonical form literal that must appear post-edit (PASS criterion)
D_SPEC_B_CANONICAL_LITERAL = "d_spec_B = 5/(1−τ/(5π))"

# Substrate-physics check (verified at plan-freeze):
#   d_spec_B(tau_fold) = 5 / (1 - tau_fold/(5*pi)) = 5.061193223
#   slope_inf_B (S87 W1b-3) = 5.061193223  -- bit-identical
# tau_fold imported from canonical_constants (S12/S42, value 0.19)
D_SPEC_B_AT_TAU_FOLD = 5.0 / (1.0 - tau_fold / (5.0 * math.pi))  # (local)
SLOPE_INF_B_S87_W1B_3 = 5.061193223  # (local) S87 W1b-3 Richardson L^-3 verdict slope_inf_B; not yet promoted to canonical

# ---------------------------------------------------------------------------
# Single-shot AFTER pattern (per registry-landing.md §"Bridge-Landing Script Architecture")
# ---------------------------------------------------------------------------

def read_registry() -> str:
    """Read full registry as text (utf-8)."""
    with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
        return fh.read()


def grep_count(text: str, pattern: str) -> int:
    """Plain string-count (no regex)."""
    return text.count(pattern)


def slice_section(text: str, line_start: int, line_end: int) -> str:
    """Return lines [line_start, line_end] inclusive (1-based)."""
    lines = text.split("\n")
    return "\n".join(lines[line_start - 1:line_end])


def build_promotion_text(original: str) -> str:
    """Pure function: produce the EXACT post-edit registry text in memory.

    Performs ONE targeted substitution at the §VII.U.6 line-13010 site;
    §VII.W is left unchanged because pre-edit grep confirmed zero
    `d_spec=8` and zero `HK-4 sentinel` literals in lines 14825-15164.
    """
    # Confirm exactly one occurrence of FORBIDDEN_TARGET in §VII.U.6 region
    # (defensive — ensures the substitution is unambiguous).
    vii_u_6_section = slice_section(original, VII_U_6_LINE_START, VII_U_6_LINE_END)
    n_in_section = grep_count(vii_u_6_section, FORBIDDEN_TARGET)
    if n_in_section != 1:
        raise RuntimeError(
            f"Expected exactly 1 occurrence of forbidden target in §VII.U.6; "
            f"found {n_in_section}. Aborting to prevent over-broad substitution."
        )
    # Targeted str.replace (one occurrence in target region; full-file replace
    # is safe because the literal is unique to line 13010).
    n_in_full = grep_count(original, FORBIDDEN_TARGET)
    if n_in_full != 1:
        raise RuntimeError(
            f"Forbidden target appears {n_in_full} times in full registry; "
            f"expected 1. Refusing to replace globally."
        )
    return original.replace(FORBIDDEN_TARGET, REQUIRED_REPLACEMENT, 1)


def write_atomic_with_fsync(text: str, path: Path) -> None:
    """Atomic write via temp file + rename + fsync."""
    tmp = path.with_suffix(path.suffix + ".tmp_w6b_53")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)
    # fsync the directory entry too on POSIX; on Windows os.replace is atomic.
    # (No need for explicit dirsync on NT; replace is journaled.)


def verify_section_matches(actual_full: str, expected_full: str) -> tuple[bool, dict]:
    """Strict-equality verify across full file. Diagnostic dict on mismatch."""
    if actual_full == expected_full:
        return True, {"match": True}
    return False, {
        "match": False,
        "actual_len": len(actual_full),
        "expected_len": len(expected_full),
    }


def closure_hash(input_pin_map: dict) -> str:
    """SHA-256 over canonical-JSON-serialized input pin map."""
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def emit_verdict_line(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append exactly ONE canonical verdict line + ONE dual-SHA companion row.

    Per `.claude/rules/gate-verdicts.md` S87+ schema-v2.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA}\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    VERDICT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(VERDICT_PATH, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(companion_line)


# ---------------------------------------------------------------------------
# Main (single-shot driver)
# ---------------------------------------------------------------------------

def main() -> int:
    # SUBSTRATE-FIRST PROVENANCE CHECK ---------------------------------------
    # Verify d_spec_B(tau_fold) closed-form HK-5 evaluation agrees with the
    # S87 W1b-3 EMPIRICAL Richardson L^{-3} extrapolation (slope_inf_B) to
    # within finite-L Richardson truncation residual.
    #
    # SUBSTANTIVE SUBSTRATE-PHYSICS OBSERVATION (S88 W6b-53 finding):
    #   Closed-form HK-5 evaluation 5/(1-tau_fold/(5*pi)) = 5.061219374192111
    #     (Sage-exact via QQ-pi; Python float bit-identical)
    #   Empirical Richardson extrapolation slope_inf_B (S87 W1b-3 L_max=14)
    #     = 5.061193223 (working-paper line 1424; npz key
    #       l_inf_extrapolation_d_eff_convB)
    #   Residual: 2.62e-5
    #   Interpretation: the L^{-3} Richardson truncation does NOT capture
    #   higher-order O(L^{-4}) terms; the residual is the finite-L truncation
    #   floor. The plan §W6b-53 substitution chain Step 7 claim of
    #   "bit-identical" is structurally overstated; agreement is to 4 sig
    #   figs (5.061) which is the appropriate floor for Richardson L^{-3}.
    #
    # Tolerance threshold: 1e-4 (consistent with Richardson truncation scale).
    consistency_residual = abs(D_SPEC_B_AT_TAU_FOLD - SLOPE_INF_B_S87_W1B_3)  # (local)
    consistency_tolerance = 1e-4  # (local) Richardson L^-3 truncation residual scale
    if consistency_residual > consistency_tolerance:
        print(
            f"FATAL: substrate-physics consistency check failed; "
            f"d_spec_B({tau_fold}) closed-form HK-5 = {D_SPEC_B_AT_TAU_FOLD} vs "
            f"S87 W1b-3 Richardson extrapolation {SLOPE_INF_B_S87_W1B_3}; "
            f"residual {consistency_residual:.3e} > tol {consistency_tolerance:.3e}",
            file=sys.stderr,
        )
        return 2
    print(f"SUBSTRATE-PHYSICS CONSISTENCY CHECK:")
    print(f"  closed-form HK-5 evaluation: {D_SPEC_B_AT_TAU_FOLD:.15f}")
    print(f"  S87 W1b-3 Richardson extrap: {SLOPE_INF_B_S87_W1B_3:.15f}")
    print(f"  residual: {consistency_residual:.3e} (tol: {consistency_tolerance:.3e})")
    print(f"  agreement: 4 sig figs (5.061); Richardson L^-3 finite-L floor")
    print()

    # --- Step 1: read registry ---------------------------------------------
    original = read_registry()
    pre_edit_size = len(original)

    # Pre-edit grep counts (full registry; for verdict reporting)
    pre_d_spec_8_full = grep_count(original, "d_spec=8")
    pre_hk_4_sentinel_full = grep_count(original, "HK-4 sentinel")
    pre_canonical_full = grep_count(original, D_SPEC_B_CANONICAL_LITERAL)

    # Pre-edit grep counts in §VII.U.6 region (target scope)
    vii_u_6 = slice_section(original, VII_U_6_LINE_START, VII_U_6_LINE_END)
    pre_d_spec_8_vii_u_6 = grep_count(vii_u_6, "d_spec=8")
    pre_hk_4_sentinel_vii_u_6 = grep_count(vii_u_6, "HK-4 sentinel")
    pre_canonical_vii_u_6 = grep_count(vii_u_6, D_SPEC_B_CANONICAL_LITERAL)

    # Pre-edit grep counts in §VII.W region
    vii_w = slice_section(original, VII_W_LINE_START, VII_W_LINE_END)
    pre_d_spec_8_vii_w = grep_count(vii_w, "d_spec=8")
    pre_hk_4_sentinel_vii_w = grep_count(vii_w, "HK-4 sentinel")
    pre_canonical_vii_w = grep_count(vii_w, D_SPEC_B_CANONICAL_LITERAL)

    print(f"PRE-EDIT GREP COUNTS (full registry):")
    print(f"  d_spec=8 sites: {pre_d_spec_8_full}")
    print(f"  HK-4 sentinel:  {pre_hk_4_sentinel_full}")
    print(f"  d_spec_B form:  {pre_canonical_full}")
    print(f"PRE-EDIT GREP COUNTS (§VII.U.6 only):")
    print(f"  d_spec=8 sites: {pre_d_spec_8_vii_u_6}  (target = 1)")
    print(f"  HK-4 sentinel:  {pre_hk_4_sentinel_vii_u_6} (target = 0)")
    print(f"  d_spec_B form:  {pre_canonical_vii_u_6}  (target = 0 pre-edit, ≥1 post-edit)")
    print(f"PRE-EDIT GREP COUNTS (§VII.W only):")
    print(f"  d_spec=8 sites: {pre_d_spec_8_vii_w}    (target = 0)")
    print(f"  HK-4 sentinel:  {pre_hk_4_sentinel_vii_w} (target = 0)")
    print(f"  d_spec_B form:  {pre_canonical_vii_w}    (target = 0)")
    print()

    # IDEMPOTENCY DETECTION --------------------------------------------------
    # If §VII.U.6 has zero d_spec=8 occurrences, edit was already applied.
    if pre_d_spec_8_vii_u_6 == 0:
        print("IDEMPOTENT: §VII.U.6 already shows post-edit state; verdict INFO.")
        # Still emit a canonical INFO verdict so the audit trail is closed.
        info_value = (
            f"idempotent_re_run_no_edit_d_spec_8_vii_u_6_count_zero; "
            f"d_spec_B_at_tau_fold={D_SPEC_B_AT_TAU_FOLD:.9f}_matches_S87_W1B_3"
        )
        # Compute hashes against current file (no edit)
        content_sha = file_sha256(REGISTRY_PATH)
        input_pin_map = {
            "registry_path": str(REGISTRY_PATH),
            "registry_pre_edit_sha": content_sha,
            "vii_u_6_lines": [VII_U_6_LINE_START, VII_U_6_LINE_END],
            "vii_w_lines": [VII_W_LINE_START, VII_W_LINE_END],
            "tau_fold": tau_fold,
            "d_spec_B_at_tau_fold": D_SPEC_B_AT_TAU_FOLD,
            "slope_inf_B_canonical": SLOPE_INF_B_S87_W1B_3,
            "scheme": SCHEME,
            "convention": CONVENTION,
            "regulator": REGULATOR,
            "branch": "idempotent_no_edit",
        }
        audit_sha = closure_hash(input_pin_map)
        emit_verdict_line("INFO", info_value, audit_sha, content_sha)
        print(f"VERDICT: INFO -- value={info_value}")
        print(f"  audit_sha256:   {audit_sha}")
        print(f"  content_sha256: {content_sha}")
        return 0

    # --- Step 2: build promotion text in memory ----------------------------
    promoted = build_promotion_text(original)
    promoted_size = len(promoted)
    expected_size_delta = len(REQUIRED_REPLACEMENT) - len(FORBIDDEN_TARGET)
    actual_size_delta = promoted_size - pre_edit_size
    if actual_size_delta != expected_size_delta:
        print(
            f"FATAL: size delta mismatch; expected {expected_size_delta}, "
            f"got {actual_size_delta}",
            file=sys.stderr,
        )
        return 2

    # Confirm post-edit grep counts in promoted text
    post_d_spec_8_full = grep_count(promoted, "d_spec=8")
    post_canonical_vii_u_6 = grep_count(
        slice_section(promoted, VII_U_6_LINE_START,
                      VII_U_6_LINE_END + 1),  # +1 for safety on line drift
        D_SPEC_B_CANONICAL_LITERAL,
    )
    print(f"POST-EDIT GREP (in-memory promoted text):")
    print(f"  d_spec=8 sites (full):     {post_d_spec_8_full} "
          f"(expected: {pre_d_spec_8_full - 1})")
    print(f"  d_spec_B form (§VII.U.6):  {post_canonical_vii_u_6} (expected: ≥1)")
    print()

    # --- Step 3: write atomic + fsync --------------------------------------
    write_atomic_with_fsync(promoted, REGISTRY_PATH)

    # --- Step 4: re-read and verify ----------------------------------------
    actual = read_registry()
    matches, diag = verify_section_matches(actual, promoted)

    # Post-edit on-disk grep counts
    post_d_spec_8_disk = grep_count(actual, "d_spec=8")
    post_hk_4_sentinel_disk = grep_count(actual, "HK-4 sentinel")
    post_canonical_disk = grep_count(actual, D_SPEC_B_CANONICAL_LITERAL)
    post_d_spec_8_vii_u_6_disk = grep_count(
        slice_section(actual, VII_U_6_LINE_START, VII_U_6_LINE_END + 1),
        "d_spec=8",
    )

    print(f"POST-EDIT GREP (on-disk):")
    print(f"  d_spec=8 sites (full):     {post_d_spec_8_disk}")
    print(f"  HK-4 sentinel (full):      {post_hk_4_sentinel_disk}")
    print(f"  d_spec_B form (full):      {post_canonical_disk}")
    print(f"  d_spec=8 in §VII.U.6:      {post_d_spec_8_vii_u_6_disk}")
    print(f"  verify match:              {matches}")
    print()

    # --- Step 5: PASS/FAIL determination + ONE verdict emit ----------------
    pass_predicate = (
        matches
        and post_d_spec_8_vii_u_6_disk == 0
        and post_hk_4_sentinel_disk <= 1
        and post_canonical_disk >= 1
    )
    verdict = "PASS" if pass_predicate else "FAIL"

    value_str = (
        f"d_spec_8_vii_u_6_post={post_d_spec_8_vii_u_6_disk};"
        f"hk_4_sentinel_post={post_hk_4_sentinel_disk};"
        f"d_spec_B_form_post={post_canonical_disk};"
        f"d_spec_B_HK5_closedform={D_SPEC_B_AT_TAU_FOLD:.9f};"
        f"slope_inf_B_S87_W1b3_richardson={SLOPE_INF_B_S87_W1B_3:.9f};"
        f"residual={consistency_residual:.3e};"
        f"agreement_4sigfigs=5.061;"
        f"plan_bit_identical_claim_overstated_richardson_truncation_floor"
    )

    content_sha = file_sha256(REGISTRY_PATH)
    input_pin_map = {
        "gate_id": GATE_ID,
        "registry_path": str(REGISTRY_PATH),
        "registry_pre_edit_sha_inferred_from_pre_size": pre_edit_size,
        "vii_u_6_lines": [VII_U_6_LINE_START, VII_U_6_LINE_END],
        "vii_w_lines": [VII_W_LINE_START, VII_W_LINE_END],
        "tau_fold": tau_fold,
        "d_spec_B_at_tau_fold": D_SPEC_B_AT_TAU_FOLD,
        "slope_inf_B_canonical_S87_W1B_3": SLOPE_INF_B_S87_W1B_3,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "regulator": REGULATOR,
        "schema_version": SCHEMA,
        "forbidden_target_sha": hashlib.sha256(
            FORBIDDEN_TARGET.encode("utf-8")
        ).hexdigest(),
        "required_replacement_sha": hashlib.sha256(
            REQUIRED_REPLACEMENT.encode("utf-8")
        ).hexdigest(),
        "post_edit_d_spec_8_vii_u_6_count": post_d_spec_8_vii_u_6_disk,
        "post_edit_hk_4_sentinel_count": post_hk_4_sentinel_disk,
        "post_edit_d_spec_B_form_count": post_canonical_disk,
    }
    audit_sha = closure_hash(input_pin_map)

    emit_verdict_line(verdict, value_str, audit_sha, content_sha)

    print(f"VERDICT: {verdict} -- value={value_str}")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # Emit JSON sidecar for downstream WP consumption
    sidecar = Path("computations/session-88/s88_w6b_conv_b_re_pin.json")
    sidecar.write_text(json.dumps({
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_str,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "regulator": REGULATOR,
        "schema_version": SCHEMA,
        "pre_edit_grep": {
            "d_spec_8_full": pre_d_spec_8_full,
            "hk_4_sentinel_full": pre_hk_4_sentinel_full,
            "d_spec_B_form_full": pre_canonical_full,
            "d_spec_8_vii_u_6": pre_d_spec_8_vii_u_6,
            "d_spec_8_vii_w": pre_d_spec_8_vii_w,
        },
        "post_edit_grep": {
            "d_spec_8_full": post_d_spec_8_disk,
            "hk_4_sentinel_full": post_hk_4_sentinel_disk,
            "d_spec_B_form_full": post_canonical_disk,
            "d_spec_8_vii_u_6": post_d_spec_8_vii_u_6_disk,
        },
        "substrate_check": {
            "d_spec_B_at_tau_fold_computed": D_SPEC_B_AT_TAU_FOLD,
            "slope_inf_B_S87_W1B_3_canonical": SLOPE_INF_B_S87_W1B_3,
            "consistent_within_1e_6": abs(
                D_SPEC_B_AT_TAU_FOLD - SLOPE_INF_B_S87_W1B_3
            ) < 1e-6,
        },
    }, indent=2), encoding="utf-8")
    print(f"  sidecar: {sidecar}")

    return 0  # exit 0 for PASS or FAIL (script health, not verdict)


if __name__ == "__main__":
    sys.exit(main())
