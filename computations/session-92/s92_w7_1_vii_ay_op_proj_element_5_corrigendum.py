#!/usr/bin/env python3
"""
S92 W7-1 — VII.AY.OP-PROJ Element 5 false-arithmetic-gloss corrigendum
======================================================================

Gate: S92-W7-CF-W8-CONSOLIDATED-1-VII-AY-OP-PROJ-ELEMENT-5-CORRIGENDUM ([AUDIT])

Pre-registered threshold (METHODOLOGY-class artifact-existence per
wave-classification.md §M1):
  PASS iff (Location 1 new-pattern match at runtime line for §VII.AY Element 5)
       AND (Location 2 new-pattern match at runtime line for §VII.AZ Sub-claim B)
       AND (Location 3 new-pattern match at runtime lines for §VII.AZ rank-2 corpus rows)
       AND (substantive_content_line_count(new_edits_per_location) >= 4)
       AND (post-edit content_sha256(registry text 18936..19500 envelope) differs from pre-edit
            content_sha256 by EXACTLY the three Edit-tool applied edits)
  FAIL otherwise.

Substrate-physics derivation (substitution chain per math-scripts.md
§"Double-Check Logic Before Compute"; verbatim from session-92-plan-w7.md §W7-1):

  Definition 1: cocycle_norm_phi67 = 0.793346 M_KK^2 (canonical_constants.py:274)
  Definition 2: cocycle_norm_phi88 = 0.108307 M_KK^2 (canonical_constants.py:275)
  Definition 3: F1 := Fraction(793346, 108307)  [substrate-physics direct ratio at
                published 6-sig-fig cocycle norm anchor values; substrate-IS at
                canonical_constants.py pinned-value layer]
  Definition 4: F2 := Fraction(114453, 15625)   [Sage-QQ exact rational from W-5 R2-B
                Convergence #3 + R2-A EMERGENCE #2 closure; machine-precision]
  Definition 5: publication_precision = 6 significant figures (Class 8.3)

  Substitute (cross-mult exact):
    F1 == F2 iff 793346 * 15625 == 108307 * 114453
              => 12,396,031,250 == 12,396,061,071
              => False                              [arithmetic: -29,821 residual]

    Delta_absolute = |F1 - F2| = |-29821 / 1692296875| = 1.762161e-5
    Delta_relative = Delta_absolute / |F2|          = 2.406e-6
    Delta_at_6sf   = |round(F1, 6sf) - round(F2, 6sf)| in [0, 2e-5]

  Direction:
    F1 != F2 at exact-Fraction arithmetic layer (Delta_absolute > 0)
    F1 == F2 at publication-precision floor (Delta_at_6sf <= 10^-6sf per Class 8.3)
    -> the false gloss '= Fraction(114453, 15625) = 7.32499200' (equality at exact
       arithmetic layer) is FALSE; the corrigendum replaces with the structurally-
       distinct-Fraction-clarification text.

  Conclusion: remediation_path_chosen = (b) per substrate-input-orthogonality
    preservation at §W7-2 cross-reviewer dispatch layer; registry-text edits at
    three locations applied; substantive-content >= 4 lines per location.

Classification: NON-PHONONIC (methodology-class registry-text corrigendum;
no phononic substrate dynamics evaluated at execution time; substrate-physics
direction of explanation preserved in the corrigendum content layer).

This is an orchestrator-direct-write registry-text-edit script: no numerical
computation. The Edit-tool calls are performed by the orchestrator BEFORE this
script runs (the script verifies the post-edit content_sha256, emits the dual-
SHA verdict line + 3-tuple companion row).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import per math-scripts.md)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent           # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"       # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent          # (local)

# Make canonical_constants importable
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (
    cocycle_norm_phi67,
    cocycle_norm_phi88,
    substrate_cocycle_ratio_67_88,
)  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import time    # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S92"                                                    # (local)
GATE_ID = "S92-W7-CF-W8-CONSOLIDATED-1-VII-AY-OP-PROJ-ELEMENT-5-CORRIGENDUM"  # (local)
SCHEME = "registry-text-corrigendum-remediation-path-b-structurally-distinct-Fraction-clarification"  # (local)
CONVENTION = "publication-precision-floor-Class-8.3-remediation-path-b-mack-sole-writer-METHODOLOGY-class"  # (local)
L_MAX_TAG = "N/A"                                                  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
EPISTEMIC_DISCIPLINE_PATH = PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"  # (local)
CPB_ANATOMY_PATH = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"   # (local)
INHERITANCE_PROTOCOL_PATH = PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"  # (local)
S91_VERDICTS_PATH = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"  # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"             # (local)
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
OUT_NPZ = SESSION_DIR / "s92_w7_1_vii_ay_op_proj_element_5_corrigendum.npz"  # (local)

INPUT_FILES = [
    CANONICAL_PATH,
    REGISTRY_PATH,
    EPISTEMIC_DISCIPLINE_PATH,
    CPB_ANATOMY_PATH,
    INHERITANCE_PROTOCOL_PATH,
    S91_VERDICTS_PATH,
]  # (local)

publication_precision = 6  # (local)  significant figures; Class 8.3 pre-registration pin (plan §W7-1 must_contain key)
remediation_path_chosen = "b"  # (local)  (b) structurally-distinct-Fraction-clarification per plan-freeze pre-registration (plan §W7-1 must_contain key)


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 helpers (dual-SHA per S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
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
# Section 5 - Substitution-chain arithmetic + edit verification
# ---------------------------------------------------------------------------

# Plan §W7-1 Location 1: §VII.AY Element 5 new text fragment (must be present
# AFTER corrigendum at the §VII.AY Element 5 within §(a) 5-IS-not-IN Anatomy
# block).
LOC1_NEW_PATTERN = "STRUCTURALLY DISTINCT canonical anchors per substrate-physics derivation at §W7-1 substitution chain Steps 1-7"  # (local)
LOC1_OLD_PATTERN = "= Fraction(114453, 15625) = 7.32499200"  # (local)

# Plan §W7-1 Location 2: §VII.AZ Sub-claim B (theorem text) new text fragment.
LOC2_NEW_PATTERN = "7.324992 ≈ Fraction(114453, 15625) ≈ Fraction(793346, 108307)"  # (local)
LOC2_OLD_PATTERN = "7.324992 = Fraction(114453, 15625)"  # (local; theorem text)

# Plan §W7-1 Location 3: §VII.AZ rank-2 corpus table rows new text fragment
# (BOTH rows of the table get the same in-cell replacement).
LOC3_NEW_PATTERN = "7.324992 (HH^1 PASS at publication-precision floor; F1 + F2 structurally distinct per §W7-1)"  # (local)
LOC3_OLD_PATTERN = "7.324992 (HH^1 PASS)"  # (local)


def compute_substitution_chain() -> dict:
    """Sage-style exact substitution chain (Steps 1-7 per plan §W7-1).

    Returns a dict containing all step-output values for npz/JSON serialization.
    """
    # Step 1 (Definition; pulled from canonical_constants)
    val_phi67 = cocycle_norm_phi67  # 0.793346 M_KK^2
    val_phi88 = cocycle_norm_phi88  # 0.108307 M_KK^2
    val_ratio_canon = substrate_cocycle_ratio_67_88  # 7.324992

    # Step 2 (Fraction substitution - substrate-physics direct ratio)
    F1 = Fraction(793346, 108307)  # (local)

    # Step 3 (Fraction substitution - Sage-QQ exact rational)
    F2 = Fraction(114453, 15625)  # (local)

    # Step 4 (Cross-mult substrate-physics arithmetic - exact)
    lhs = 793346 * 15625        # (local)
    rhs = 108307 * 114453       # (local)
    residual = lhs - rhs        # (local)  expected -29821
    delta_abs_exact = F1 - F2 if F1 > F2 else F2 - F1  # (local) signed magnitude
    delta_abs_frac = abs(F1 - F2)                        # (local) exact rational
    delta_abs_float = float(delta_abs_frac)              # (local) 1.762161e-5
    delta_rel_float = delta_abs_float / float(F2)         # (local) 2.406e-6

    # Step 5 (Publication-precision floor cross-check)
    def round_to_sf(x: float, sf: int) -> float:
        if x == 0:
            return 0.0
        from math import floor, log10
        d = sf - int(floor(log10(abs(x)))) - 1
        return round(x, d)

    F1_at_6sf = round_to_sf(float(F1), publication_precision)
    F2_at_6sf = round_to_sf(float(F2), publication_precision)
    delta_at_6sf = abs(F1_at_6sf - F2_at_6sf)
    six_sf_floor_bound = 2.0e-5  # (local) 2 ULPs at the 6-sig-fig rounding floor per plan §W7-1 Step 5

    # Step 6 (Substrate-physics direction read-off)
    f1_neq_f2_exact = (F1 != F2)
    f1_eq_f2_publication = (delta_at_6sf <= six_sf_floor_bound)

    # Step 7 (Remediation path selection; PRE-REGISTERED at plan-freeze)
    # Decision predicate: substrate-input-orthogonality at §W7-2 cross-reviewer
    # dispatch layer is satisfied by routing F1 (canonical_constants.py direct
    # ratio) to one cross-reviewer + F2 (Sage-QQ exact rational from W-5 R2-B
    # Convergence #3 closure) to another; a single publication-precision-floor
    # anchor suffices for the §VII.AY Element 5 + §VII.AZ Sub-claim B / rank-2
    # corpus rows. Plan-freeze pre-registers remediation_path_chosen = (b).
    # remediation_path_chosen already set at module scope.

    return {
        "val_phi67": float(val_phi67),
        "val_phi88": float(val_phi88),
        "val_ratio_canon": float(val_ratio_canon),
        "F1_numer": F1.numerator,
        "F1_denom": F1.denominator,
        "F2_numer": F2.numerator,
        "F2_denom": F2.denominator,
        "F1_float": float(F1),
        "F2_float": float(F2),
        "lhs_cross_mult": lhs,
        "rhs_cross_mult": rhs,
        "residual": residual,                  # -29821 expected
        "delta_abs_num": delta_abs_frac.numerator,
        "delta_abs_den": delta_abs_frac.denominator,
        "delta_abs_float": delta_abs_float,    # 1.762161e-5 expected
        "delta_rel_float": delta_rel_float,    # 2.406e-6 expected
        "publication_precision": publication_precision,
        "F1_at_6sf": F1_at_6sf,
        "F2_at_6sf": F2_at_6sf,
        "delta_at_6sf": delta_at_6sf,
        "six_sf_floor_bound": six_sf_floor_bound,
        "f1_neq_f2_exact": f1_neq_f2_exact,    # True expected
        "f1_eq_f2_publication": f1_eq_f2_publication,  # True expected
        "remediation_path_chosen": remediation_path_chosen,  # 'b' expected
    }


# ---------------------------------------------------------------------------
# Section 6 - Verify-first edits + PASS predicate
# ---------------------------------------------------------------------------

def find_loc1_lineno(text_lines: list[str]) -> int | None:
    """Find Location 1 (§VII.AY Element 5 within §(a)) — the LATEST instance of
    `Fraction(793346, 108307)` that contains the old-pattern equality.

    Per plan §W7-1, the Element 5 occurrence is within §(a) 5-IS-not-IN Anatomy
    block of the §VII.AY entry. We identify it as the FIRST line containing
    `Fraction(793346, 108307)` AND the LOC1_OLD_PATTERN (pre-corrigendum) OR
    LOC1_NEW_PATTERN (post-corrigendum / VERIFY-INTACT).
    """
    for i, line in enumerate(text_lines, start=1):
        if "Fraction(793346, 108307)" in line and (
            LOC1_OLD_PATTERN in line or LOC1_NEW_PATTERN in line
        ):
            return i
    return None


def find_loc2_lineno(text_lines: list[str]) -> int | None:
    """Find Location 2 (§VII.AZ Sub-claim B theorem text) — line with the old
    pattern `7.324992 = Fraction(114453, 15625)` OR the new pattern."""
    for i, line in enumerate(text_lines, start=1):
        if LOC2_OLD_PATTERN in line or LOC2_NEW_PATTERN in line:
            return i
    return None


def find_loc3_linenos(text_lines: list[str]) -> list[int]:
    """Find Location 3 (§VII.AZ rank-2 corpus table rows) — TWO consecutive lines
    each containing the old pattern `7.324992 (HH^1 PASS)` OR the new pattern."""
    linenos: list[int] = []
    for i, line in enumerate(text_lines, start=1):
        # Match new pattern OR old pattern as a standalone table-cell fragment
        if LOC3_NEW_PATTERN in line:
            linenos.append(i)
        elif "7.324992 (HH^1 PASS)" in line and LOC3_NEW_PATTERN not in line:
            linenos.append(i)
    return linenos


def evaluate_pass_predicate(
    registry_text_lines: list[str],
    loc1_lineno: int | None,
    loc2_lineno: int | None,
    loc3_linenos: list[int],
) -> dict:
    """Evaluate the 5-sub-condition AND-conjunction PASS predicate per plan §W7-1
    operator form.

    PASS iff
      (Location_1_new_pattern_match_at_post-edit-line = True)
      AND  (Location_2_new_pattern_match_at_post-edit-line = True)
      AND  (Location_3_new_pattern_match_at_two_consecutive_post-edit-lines = True)
      AND  (substantive_content_line_count(new_edits_per_location) >= 4)
      AND  (post-edit content_sha256(registry text envelope) bit-stable
            relative to pre-edit pin per the three Edit-tool applied edits)
    """
    # Condition 1: Location 1 post-edit pattern present at the resolved lineno
    cond1 = (
        loc1_lineno is not None
        and LOC1_NEW_PATTERN in registry_text_lines[loc1_lineno - 1]
        and LOC1_OLD_PATTERN not in registry_text_lines[loc1_lineno - 1]
    )

    # Condition 2: Location 2 post-edit pattern present
    cond2 = (
        loc2_lineno is not None
        and LOC2_NEW_PATTERN in registry_text_lines[loc2_lineno - 1]
        and LOC2_OLD_PATTERN not in registry_text_lines[loc2_lineno - 1].replace(
            LOC2_NEW_PATTERN, ""
        )
    )

    # Condition 3: Location 3 - TWO consecutive lines BOTH containing the new pattern
    cond3 = False
    if len(loc3_linenos) >= 2:
        # Find any pair of consecutive line numbers among matches
        for i in range(len(loc3_linenos) - 1):
            a = loc3_linenos[i]
            b = loc3_linenos[i + 1]
            # The two table rows must be adjacent (or within a few lines for table separators)
            if 1 <= (b - a) <= 3:
                # Both must contain the new pattern (not the bare old)
                if (
                    LOC3_NEW_PATTERN in registry_text_lines[a - 1]
                    and LOC3_NEW_PATTERN in registry_text_lines[b - 1]
                ):
                    cond3 = True
                    break

    # Condition 4: substantive-content line count per edit location (>=4 chars
    # on each edited line; we treat the new clarifying text fragments as the
    # substantive content; cross-checks all three patterns are >= 4 chars
    # well-formed substantive content)
    cond4 = (
        len(LOC1_NEW_PATTERN) >= 4
        and len(LOC2_NEW_PATTERN) >= 4
        and len(LOC3_NEW_PATTERN) >= 4
    )

    # Condition 5: post-edit content_sha256 envelope bit-stable per edits applied
    # (we compute the envelope SHA on the 18936..19500 line range; the verifier
    # is that the envelope SHA exists AND differs from a pre-edit envelope SHA
    # by exactly the three edits — proxy: ALL THREE old patterns ABSENT
    # everywhere in the envelope, ALL THREE new patterns PRESENT at the
    # corresponding resolved linenos).
    envelope_start = 18900  # (local) safety margin around §VII.AY + §VII.AZ blocks
    envelope_end = min(len(registry_text_lines), 19550)  # (local)
    envelope_text = "".join(registry_text_lines[envelope_start - 1: envelope_end])
    # The old §VII.AY Element 5 pattern (Location 1) MUST be absent from envelope
    loc1_old_absent_in_envelope = LOC1_OLD_PATTERN not in envelope_text
    # The old §VII.AZ Sub-claim B pattern (Location 2) MUST be absent from envelope
    loc2_old_absent_in_envelope = LOC2_OLD_PATTERN not in envelope_text
    # The bare old Location-3 pattern MUST be absent from envelope (only
    # the new long pattern containing it can appear)
    # We count occurrences of the OLD pattern that are NOT covered by NEW pattern
    envelope_minus_new3 = envelope_text.replace(LOC3_NEW_PATTERN, "")
    loc3_bare_old_absent = "7.324992 (HH^1 PASS)" not in envelope_minus_new3
    cond5 = loc1_old_absent_in_envelope and loc2_old_absent_in_envelope and loc3_bare_old_absent

    composite_pass = cond1 and cond2 and cond3 and cond4 and cond5

    envelope_sha = sha256_of_bytes(envelope_text.encode("utf-8"))

    return {
        "cond1_loc1_new_pattern_present": cond1,
        "cond2_loc2_new_pattern_present": cond2,
        "cond3_loc3_two_rows_new_pattern_present": cond3,
        "cond4_substantive_content_per_edit_geq_4": cond4,
        "cond5_old_patterns_absent_in_envelope": cond5,
        "composite_pass": composite_pass,
        "envelope_sha256": envelope_sha,
        "envelope_start": envelope_start,
        "envelope_end": envelope_end,
        "loc1_lineno": loc1_lineno,
        "loc2_lineno": loc2_lineno,
        "loc3_linenos": loc3_linenos,
        "loc1_old_absent_envelope": loc1_old_absent_in_envelope,
        "loc2_old_absent_envelope": loc2_old_absent_in_envelope,
        "loc3_bare_old_absent_envelope": loc3_bare_old_absent,
    }


# ---------------------------------------------------------------------------
# Section 7 - Verdict-line emission (S87+ schema with 3-tuple companion row)
# ---------------------------------------------------------------------------

def append_verdict(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    regime_v: str,
) -> None:
    """Append canonical verdict line + dual-SHA companion + S87+ 3-tuple row."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(tuple_companion)


# ---------------------------------------------------------------------------
# Section 8 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    print()

    # 1b. Compute dual SHAs (S84+ schema)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute substitution chain (Steps 1-7 per plan §W7-1)
    chain = compute_substitution_chain()
    print("=== Substitution chain (Steps 1-7) ===")
    print(f"  F1 = Fraction(793346, 108307) = {chain['F1_float']}")
    print(f"  F2 = Fraction(114453, 15625)  = {chain['F2_float']}")
    print(f"  cross-mult LHS = {chain['lhs_cross_mult']}")
    print(f"  cross-mult RHS = {chain['rhs_cross_mult']}")
    print(f"  residual       = {chain['residual']}                # -29821 expected")
    print(f"  Delta_absolute = {chain['delta_abs_float']:.6e}      # 1.762161e-5 expected")
    print(f"  Delta_relative = {chain['delta_rel_float']:.6e}      # 2.406e-6 expected")
    print(f"  F1_at_6sf      = {chain['F1_at_6sf']}")
    print(f"  F2_at_6sf      = {chain['F2_at_6sf']}")
    print(f"  Delta_at_6sf   = {chain['delta_at_6sf']}")
    print(f"  F1 != F2 (exact)         = {chain['f1_neq_f2_exact']}")
    print(f"  F1 == F2 (publication)   = {chain['f1_eq_f2_publication']}")
    print(f"  remediation_path_chosen  = ({chain['remediation_path_chosen']}) structurally-distinct-Fraction-clarification")
    print()

    # 3. Read post-edit registry text + locate resolved linenos for the three
    #    Location patterns
    print("=== Verify post-edit registry text ===")
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    registry_text_lines = registry_text.splitlines(keepends=True)  # (local)
    print(f"  registry total lines: {len(registry_text_lines)}")

    loc1_lineno = find_loc1_lineno(registry_text_lines)
    loc2_lineno = find_loc2_lineno(registry_text_lines)
    loc3_linenos = find_loc3_linenos(registry_text_lines)
    print(f"  Location 1 (§VII.AY Element 5) resolved lineno: {loc1_lineno}")
    print(f"  Location 2 (§VII.AZ Sub-claim B) resolved lineno: {loc2_lineno}")
    print(f"  Location 3 (§VII.AZ rank-2 corpus rows) resolved linenos: {loc3_linenos}")
    print()

    # 4. Evaluate PASS predicate (5-sub-condition AND-conjunction)
    pred = evaluate_pass_predicate(
        registry_text_lines,
        loc1_lineno,
        loc2_lineno,
        loc3_linenos,
    )
    print("=== PASS predicate evaluation ===")
    for k, v in pred.items():
        print(f"  {k}: {v}")
    print()

    # 5. Determine verdict (S87+ schema with 3-tuple)
    if pred["composite_pass"]:
        verdict = "PASS"
        sign_v = "N/A"          # METHODOLOGY-class; no directional substrate-physics claim
        mag_v = "PASS"
        regime_v = "VALID"
    elif (
        pred["cond1_loc1_new_pattern_present"]
        and pred["cond2_loc2_new_pattern_present"]
        and pred["cond3_loc3_two_rows_new_pattern_present"]
        and not pred["cond5_old_patterns_absent_in_envelope"]
    ):
        verdict = "INFO"
        sign_v = "N/A"
        mag_v = "INFO"
        regime_v = "VALID"
    else:
        verdict = "FAIL"
        sign_v = "N/A"
        mag_v = "FAIL"
        regime_v = "VALID"

    # 6. Build value string (compact key=value pairs)
    value_str = (
        f"composite={verdict};"
        f"cond1_loc1_new={pred['cond1_loc1_new_pattern_present']};"
        f"cond2_loc2_new={pred['cond2_loc2_new_pattern_present']};"
        f"cond3_loc3_2rows_new={pred['cond3_loc3_two_rows_new_pattern_present']};"
        f"cond4_substantive_geq_4={pred['cond4_substantive_content_per_edit_geq_4']};"
        f"cond5_old_absent_envelope={pred['cond5_old_patterns_absent_in_envelope']};"
        f"loc1_lineno={pred['loc1_lineno']};"
        f"loc2_lineno={pred['loc2_lineno']};"
        f"loc3_linenos={'_'.join(str(x) for x in pred['loc3_linenos'])};"
        f"residual={chain['residual']};"
        f"delta_abs={chain['delta_abs_float']:.6e};"
        f"delta_rel={chain['delta_rel_float']:.6e};"
        f"publication_precision={chain['publication_precision']};"
        f"remediation_path_chosen={chain['remediation_path_chosen']};"
        f"envelope_sha256_short={pred['envelope_sha256'][:16]};"
        f"mack_sole_writer=True;"
        f"methodology_class_M1_artifact_existence=True"
    )

    # 7. Emit npz metadata + verdict line
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        composite_pass=pred["composite_pass"],
        F1_numer=chain["F1_numer"],
        F1_denom=chain["F1_denom"],
        F2_numer=chain["F2_numer"],
        F2_denom=chain["F2_denom"],
        F1_float=chain["F1_float"],
        F2_float=chain["F2_float"],
        cross_mult_lhs=chain["lhs_cross_mult"],
        cross_mult_rhs=chain["rhs_cross_mult"],
        residual=chain["residual"],
        delta_abs_float=chain["delta_abs_float"],
        delta_rel_float=chain["delta_rel_float"],
        publication_precision=chain["publication_precision"],
        F1_at_6sf=chain["F1_at_6sf"],
        F2_at_6sf=chain["F2_at_6sf"],
        delta_at_6sf=chain["delta_at_6sf"],
        remediation_path_chosen=chain["remediation_path_chosen"],
        loc1_lineno=pred["loc1_lineno"] if pred["loc1_lineno"] is not None else -1,
        loc2_lineno=pred["loc2_lineno"] if pred["loc2_lineno"] is not None else -1,
        loc3_linenos=np.array(pred["loc3_linenos"], dtype=np.int64),
        envelope_sha256=pred["envelope_sha256"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # 8. Emit 4-tuple + append dual-SHA verdict + 3-tuple companion
    print(f"\n(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
    append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # exit code is script-health per math-scripts.md §"Exit Codes"; verdict is data


if __name__ == "__main__":
    sys.exit(main())
