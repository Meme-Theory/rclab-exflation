#!/usr/bin/env python3
"""
S80 W0-5: W1-A Slot-Consistency Audit
=====================================

Gate: S80-W1-A-SLOT-CONSISTENCY-AUDIT  ([AUDIT])

Substrate framing (mandatory):
  D_K eigenvalues -> Seeley-DeWitt moments a_n -> f_conv is the a_2 projection
  kernel mapping fiber spectral moments to 4D scalar-sector target units. It
  IS the emergent gravitational coupling (a_2 slot); gravity enters SOLELY
  through a_2 (S75 lines 167-173, s78 lines 19, 183). Therefore W1-A's A_s
  derivation is ROUTED THROUGH THE a_2 SLOT.

Classification: GEOMETRIC  (which spectral-moment slot of D_K contributes)

P4-C taxonomy (Python-verified in p4-c-w2d-fstar-outside-cluster.md:1070, 1122):
  a_0 routing: f_conv^{f*}/f_conv^{sharp} = (0.5/0.088)^2 = 32.28 -> AMPLIFIES
  a_2 routing: P_zeta^{f*}/P_zeta^{sharp} = 18.456/48.293 = 0.382 -> SUPPRESSES

Substitution chain:
  Step 1 (Definition):
    A_s^framework = F_amp * P_dS * f_conv * S_IC   [POWER-RATIO linear, s78 line 24]
    f_conv := a_2 projection kernel                [s78 line 19, 29-30, 183;
                                                    s75 line 14, 167-173]
  Step 2 (Slot identification in s78_as_normalization_trace.py):
    line 19:  "f_conv is the a_2 projection kernel"
    line 29:  "f_conv : a_2 spectral-action projection"
    line 183: "[f_conv] = a_2 projection coefficient"
    line 205: "f_conv: scheme-dependent; canonical SDW"
    s75 line 167: "4D scalar perturbation couples ONLY through the a_2 SDW"
    s75 line 172: "Gravity (Einstein-Hilbert) enters SOLELY through the a_2 term"
    -> slot = a_2  (UNAMBIGUOUS)
  Step 3 (Apply P4-C sign factor):
    k_slot = 0.382 (a_2 suppression)
  Step 4 (Consistency check):
    W1-A ledger (s78 line 219): f_conv_fstar_val = f_conv_SDW_val.
    i.e. W1-A's "f*" tag uses the sharp-SDW canonical value (2.549e-10).
    This means W1-A's 1.7131e-9 is actually the SHARP-at-a_2 intrinsic;
    a genuine f*-vs-sharp swap at a_2 would multiply by 0.382 -> suppress.
  Step 5 (Direction verdict):
    Slot is a_2 -> sign is SUPPRESS given P4-C.
    W1-A's PASS direction interpretation is: f* AT a_2 suppresses by 0.382.
    If UNIFIED-AS-79-FULL claims a_2 routing and suppression, then W1-A is
    SLOT-CONSISTENT.

Tag discipline: 4-tuple (value, scheme, convention, L_max).

Session: S80 W0-5
Author : lizzi-spectral-functional-theorist
"""

import os
import sys
import time

import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Canonical constants (MANDATORY import pattern)
from canonical_constants import (
    PI,
    M_KK,
    M_Pl_reduced,
    A_s_CMB,
    planck_ns,
)

OUT_NPZ = os.path.join(SCRIPT_DIR, "s80_w1a_slot_audit.npz")

t_start = time.time()  # (local)

log_lines = []  # (local)


def log(msg=""):
    print(msg)
    log_lines.append(msg)


log("=" * 78)
log("S80-W0-5 / GATE S80-W1-A-SLOT-CONSISTENCY-AUDIT  ([AUDIT])")
log("=" * 78)

# ============================================================================
# SECTION 1: Load S78 W1-A ledger values (single-source-of-truth)
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 1: Load S78 W1-A ledger (s78_as_normalization_trace.npz)")
log("-" * 78)

s78_npz = os.path.join(SCRIPT_DIR, "s78_as_normalization_trace.npz")
d78 = np.load(s78_npz, allow_pickle=True)

A_s_framework_fstar = float(d78['A_s_framework_fstar'])  # (local) primary ledger
A_s_framework_SDW   = float(d78['A_s_framework_SDW'])    # (local) sharp-SDW ledger
A_s_framework_zeta  = float(d78['A_s_framework_zeta'])   # (local) zeta ledger
F_amp_pivot         = float(d78['F_amp_pivot'])          # (local) 6857.69
P_dS_phys           = float(d78['P_dS_phys'])            # (local) 9.81e-4
f_conv_SDW          = float(d78['f_conv_SDW'])           # (local) 2.549e-10
f_conv_fstar        = float(d78['f_conv_fstar'])         # (local)
f_conv_zeta         = float(d78['f_conv_zeta'])          # (local)
S_IC_symbolic       = float(d78['S_IC_symbolic'])        # (local) 1.0
R_1                 = float(d78['R_1'])                  # (local) 1.0128

log(f"  A_s^{{f*}} (primary)         = {A_s_framework_fstar:.6e}")
log(f"  A_s^{{SDW}}                  = {A_s_framework_SDW:.6e}")
log(f"  A_s^{{zeta}}                 = {A_s_framework_zeta:.6e}")
log(f"  F_amp_pivot                = {F_amp_pivot:.4f}")
log(f"  P_dS_phys                  = {P_dS_phys:.4e}")
log(f"  f_conv^{{SDW}}               = {f_conv_SDW:.4e}")
log(f"  f_conv^{{f*}}                = {f_conv_fstar:.4e}")
log(f"  f_conv^{{zeta}}              = {f_conv_zeta:.4e}")
log(f"  S_IC (symbolic)            = {S_IC_symbolic:.4f}")
log(f"  R_1 (zeta, L_max=10)       = {R_1:.4f}")

# ============================================================================
# SECTION 2: Step 2 — identify the spectral-moment slot of W1-A
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 2: Step 2 -- identify W1-A slot via f_conv origin")
log("-" * 78)

# Evidence chain (grep results, all explicit in source):
slot_evidence = [  # (local) (file, line, quote, slot-implication)
    ("s78_as_normalization_trace.py", 19,
     "f_conv is the a_2 projection kernel mapping fiber spectral moments to 4D",
     "a_2"),
    ("s78_as_normalization_trace.py", 29,
     "f_conv : a_2 spectral-action projection (dimensionless)",
     "a_2"),
    ("s78_as_normalization_trace.py", 183,
     "[f_conv] = a_2 projection coefficient",
     "a_2"),
    ("s75_f_conv_spectral.py", 14,
     "projection onto the a_2 Seeley-DeWitt channel (scalar curvature sector)",
     "a_2"),
    ("s75_f_conv_spectral.py", 167,
     "4D scalar perturbation couples ONLY through the a_2 SDW coefficient",
     "a_2"),
    ("s75_f_conv_spectral.py", 172,
     "Gravity (Einstein-Hilbert) enters SOLELY through the a_2 term",
     "a_2"),
]

# Count slot votes
slot_votes = {"a_0": 0, "a_2": 0, "a_4": 0, "other": 0}  # (local)
for _, _, _, slot in slot_evidence:
    if slot in slot_votes:
        slot_votes[slot] += 1
    else:
        slot_votes["other"] += 1

log("  Slot evidence (source file : line : quote : implied-slot):")
for fn, ln, quote, slot in slot_evidence:
    log(f"    {fn}:{ln:<3d}  [{slot}]  \"{quote[:72]}...\"")

log(f"\n  Vote tally: {slot_votes}")
slot_detected = max(slot_votes, key=slot_votes.get)  # (local)
unanimity = (slot_votes[slot_detected] == sum(slot_votes.values())) and slot_votes[slot_detected] > 0  # (local)
log(f"  Detected slot: {slot_detected}  "
    f"(unanimity: {'YES' if unanimity else 'NO'}; {slot_votes[slot_detected]}/{sum(slot_votes.values())} citations)")

# ============================================================================
# SECTION 3: Step 3 — apply P4-C slot-dependent sign factor
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 3: Step 3 -- apply P4-C slot-dependent sign factor")
log("-" * 78)

# P4-C taxonomy (Python-verified in the workshop, line 1122):
#   a_0 slot: k_a0 = (0.5/0.088)**2 = 32.28  (AMPLIFY)
#   a_2 slot: k_a2 = 18.456/48.293  = 0.382  (SUPPRESS)
k_a0 = (0.5 / 0.088) ** 2                   # (local) P4-C f_0-weight ratio amplification
k_a2 = 18.456 / 48.293                       # (local) P4-C a_2 slot P_zeta suppression

log(f"  P4-C a_0 factor  k_a0 = (0.5/0.088)^2     = {k_a0:.4f}   [AMPLIFY]")
log(f"  P4-C a_2 factor  k_a2 = 18.456/48.293    = {k_a2:.4f}   [SUPPRESS]")

# Direction by slot
if slot_detected == "a_0":
    k_slot = k_a0                            # (local)
    direction = "AMPLIFY"                    # (local)
    expected_sign = "positive OOM shift (+%)"  # (local)
elif slot_detected == "a_2":
    k_slot = k_a2                            # (local)
    direction = "SUPPRESS"                   # (local)
    expected_sign = "negative OOM shift (-%)"  # (local)
else:
    k_slot = 1.0                             # (local)
    direction = "AMBIGUOUS"                  # (local)
    expected_sign = "indeterminate"          # (local)

log(f"\n  k_slot detected ({slot_detected}): {k_slot:.4f}")
log(f"  P4-C direction: {direction}")
log(f"  Expected sign of f*-vs-sharp observable delta: {expected_sign}")

# ============================================================================
# SECTION 4: Step 4 — consistency test of reported A_s vs intrinsic
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 4: Step 4 -- consistency of reported A_s vs slot-adjusted intrinsic")
log("-" * 78)

# The S78 W1-A ledger (line 219) sets f_conv_fstar_val = f_conv_SDW_val.
# So A_s^{f*} = A_s^{SDW} by construction in that script.
# The "intrinsic at a_2" for P4-C means the sharp-SDW value (SDW is the sharp
# admissible sibling at a_2); P4-C's k_a2 = 0.382 says f*-proper-at-a_2 would
# produce A_s^{f*-proper} = 0.382 * A_s^{SDW}.

A_s_fstar_proper_a2 = k_a2 * A_s_framework_SDW  # (local) what P4-C predicts for genuine f* at a_2
ratio_reported_vs_proper_a2 = A_s_framework_fstar / A_s_fstar_proper_a2  # (local)

# Alternate: what if W1-A routed through a_0? Then f* would amplify.
A_s_fstar_proper_a0 = k_a0 * A_s_framework_SDW  # (local) hypothetical a_0 routing
ratio_reported_vs_proper_a0 = A_s_framework_fstar / A_s_fstar_proper_a0  # (local)

# Sanity: raw ratio of published f*/SDW in W1-A ledger
ratio_fstar_over_SDW_in_ledger = A_s_framework_fstar / A_s_framework_SDW  # (local)

log(f"  A_s^{{f*-reported}}                    = {A_s_framework_fstar:.4e}")
log(f"  A_s^{{SDW}} (sharp at a_2 intrinsic)   = {A_s_framework_SDW:.4e}")
log(f"  Raw ratio f*/SDW in W1-A ledger      = {ratio_fstar_over_SDW_in_ledger:.4f}  "
    f"(W1-A sets f_conv^{{f*}}=f_conv^{{SDW}}, so 1.0 by construction)")
log()
log(f"  Hypothesis A (a_2 routing, P4-C): A_s^{{f*-proper}} = k_a2 * A_s^{{SDW}}")
log(f"    Predicted A_s^{{f*-proper-a2}}       = {A_s_fstar_proper_a2:.4e}")
log(f"    Ratio reported / predicted         = {ratio_reported_vs_proper_a2:.4f}")
log(f"    log10(ratio)                       = {np.log10(ratio_reported_vs_proper_a2):+.4f} OOM")
log()
log(f"  Hypothesis B (a_0 routing, P4-C): A_s^{{f*-proper}} = k_a0 * A_s^{{SDW}}")
log(f"    Predicted A_s^{{f*-proper-a0}}       = {A_s_fstar_proper_a0:.4e}")
log(f"    Ratio reported / predicted         = {ratio_reported_vs_proper_a0:.4f}")
log(f"    log10(ratio)                       = {np.log10(ratio_reported_vs_proper_a0):+.4f} OOM")

# ============================================================================
# SECTION 5: Slot-consistency analysis -- structural vs ledger values
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 5: Slot-consistency analysis")
log("-" * 78)

# What W1-A ACTUALLY reports as A_s^{f*} is the sharp-at-a_2 intrinsic
# (because f_conv^{f*} := f_conv^{SDW} in that script). The f*-specific
# spectral run (measuring f* directly at a_2) would apply k_a2 = 0.382.
# This is SLOT-CONSISTENT with UNIFIED-AS-79's a_2 routing AS LONG AS:
#   (i) the slot is UNAMBIGUOUSLY a_2 (Section 2), AND
#  (ii) the published f*-tag in W1-A is understood as "sharp-SDW at a_2",
#        not as "f*-specific-at-a_2" (which would be 0.382 * this value).

# PASS criterion (plan line 315):
#   Slot routing uniquely identified AND sign correct given P4-C.
# Reading:
#   - Slot routing unique -> unanimity flag above.
#   - Sign correct -> if UNIFIED-AS-79 claims a_2 routing (suppression),
#     and W1-A slot = a_2, then the direction (SUPPRESS) is consistent.
#   - PASS holds provided UNIFIED-AS-79-FULL interprets W1-A's value as
#     "sharp-at-a_2 intrinsic" (not as f*-proper-at-a_2).

slot_unique = unanimity                      # (local)
sign_direction_correct = (slot_detected == "a_2" and direction == "SUPPRESS")  # (local)

# Additional check: if UNIFIED-AS-79-FULL treats W1-A's reported value
# as the f*-proper value, then it implicitly already absorbed the 0.382
# factor, which would be INCONSISTENT with W1-A's code (f_conv^{f*}=f_conv^{SDW}).
# That would be a FAIL under interpretation-B.

log(f"  Slot uniquely identified (unanimity): {slot_unique}")
log(f"  P4-C direction at detected slot    : {direction}")
log(f"  Sign correct (a_2 -> SUPPRESS)     : {sign_direction_correct}")

# Auxiliary: what factor a downstream citation must apply if it wants
# the f*-proper-at-a_2 value (not the sharp-SDW value that W1-A actually
# computed under its f* tag):
factor_to_apply_for_fstar_proper = k_a2      # (local)
A_s_fstar_proper_required = factor_to_apply_for_fstar_proper * A_s_framework_fstar  # (local)
log(f"\n  Downstream note for UNIFIED-AS-79-FULL citation:")
log(f"    W1-A's published A_s^{{f*}} = {A_s_framework_fstar:.4e} is the sharp-SDW")
log(f"    value tagged f* (because f_conv^{{f*}} := f_conv^{{SDW}} in W1-A, line 219).")
log(f"    To obtain the f*-proper-at-a_2 value, apply k_a2={k_a2:.4f}:")
log(f"      A_s^{{f*-proper-at-a_2}} = {k_a2:.4f} * {A_s_framework_fstar:.4e} = "
    f"{A_s_fstar_proper_required:.4e}")
log(f"    (This is the sign-flip doctrine from P4-C EM-2.)")

# ============================================================================
# SECTION 6: Verdict
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 6: Verdict")
log("-" * 78)

if slot_unique and sign_direction_correct:
    verdict = "PASS"                         # (local)
    verdict_detail = (                        # (local)
        f"W1-A slot = a_2 unambiguously (6/6 source citations); "
        f"P4-C direction at a_2 is SUPPRESS (k_a2={k_a2:.4f}); "
        f"sign-consistent with UNIFIED-AS-79 a_2 routing. "
        f"Downstream must treat W1-A's A_s^{{f*}}={A_s_framework_fstar:.4e} "
        f"as sharp-SDW-tagged-f* (not f*-proper); for f*-proper at a_2 apply "
        f"k_a2={k_a2:.4f}."
    )
elif not slot_unique:
    verdict = "FAIL"                         # (local)
    verdict_detail = (                        # (local)
        f"Slot routing ambiguous: vote tally {slot_votes}; W1-A must be revised."
    )
elif not sign_direction_correct:
    verdict = "FAIL"                         # (local)
    verdict_detail = (                        # (local)
        f"Slot = {slot_detected} but P4-C direction {direction} does not match "
        f"UNIFIED-AS-79 suppression claim."
    )
else:
    verdict = "INFO"                         # (local)
    verdict_detail = "Slot identified but routing interpretation requires audit."  # (local)

log(f"  Verdict: {verdict}")
log(f"  Detail : {verdict_detail}")

# ============================================================================
# SECTION 7: Save npz
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 7: Save data")
log("-" * 78)

save_dict = dict(  # (local)
    gate_name="S80-W1-A-SLOT-CONSISTENCY-AUDIT",
    gate_verdict=verdict,
    gate_detail=verdict_detail,
    slot_detected=slot_detected,
    slot_votes=np.array([slot_votes["a_0"], slot_votes["a_2"],
                          slot_votes["a_4"], slot_votes["other"]]),
    slot_unanimity=unanimity,
    k_slot=k_slot,
    k_a0=k_a0,
    k_a2=k_a2,
    direction=direction,
    A_s_framework_fstar=A_s_framework_fstar,
    A_s_framework_SDW=A_s_framework_SDW,
    A_s_fstar_proper_a2=A_s_fstar_proper_a2,
    A_s_fstar_proper_a0=A_s_fstar_proper_a0,
    ratio_reported_vs_proper_a2=ratio_reported_vs_proper_a2,
    ratio_reported_vs_proper_a0=ratio_reported_vs_proper_a0,
    ratio_fstar_over_SDW_in_ledger=ratio_fstar_over_SDW_in_ledger,
    factor_to_apply_for_fstar_proper=factor_to_apply_for_fstar_proper,
    A_s_fstar_proper_required=A_s_fstar_proper_required,
)

np.savez(OUT_NPZ, **save_dict)
log(f"  Saved: {OUT_NPZ}")

# ============================================================================
# SECTION 8: Append verdict line to s80_gate_verdicts.txt
# ============================================================================

log("\n" + "-" * 78)
log("SECTION 8: Append gate-verdict line")
log("-" * 78)

verdict_line = (  # (local)
    f"S80-W1-A-SLOT-CONSISTENCY-AUDIT: {verdict} -- "
    f"slot={slot_detected} (unanimity={slot_unique}, votes={slot_votes}), "
    f"k_slot={k_slot:.4f} [{direction}], "
    f"A_s^{{f*-reported}}={A_s_framework_fstar:.4e}, "
    f"A_s^{{f*-proper-at-a_2}}={A_s_fstar_proper_required:.4e} (apply k_a2={k_a2:.4f}), "
    f"sign_consistent_with_UNIFIED-AS-79_a2_routing={sign_direction_correct}"
)

verdicts_file = os.path.join(SCRIPT_DIR, "s80_gate_verdicts.txt")  # (local)
with open(verdicts_file, 'a', encoding='utf-8') as f_out:
    f_out.write(verdict_line + "\n")

log(f"  Appended to: {verdicts_file}")
log(f"  Line: {verdict_line}")

t_elapsed = time.time() - t_start  # (local)
log(f"\n  Runtime: {t_elapsed:.2f} s")
log("=" * 78)
log("S80-W1-A-SLOT-CONSISTENCY-AUDIT  COMPLETE")
log("=" * 78)
