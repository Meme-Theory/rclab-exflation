#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S95 W6-2 — CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT
====================================================

Gate ID    : CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT
Trigger    : [SIGN]   (directional pre-reg => schema-v2 3-tuple companion row REQUIRED)
Class      : PHONONIC (Layer-2 acoustic excitations; BAO sub-feature is an interference
             pattern of post-transit GGE acoustic excitations; scale-and-channel-tagged)
Agent      : mack-cosmic-bridge
Plan       : sessions/session-plan/session-95-plan-w6.md  §W6-2

WHAT THIS GATE DOES
-------------------
Converts the S94 W5-3 / S-1 POSITION-only BAO sensitivity bound into an AMPLITUDE
DETECTION forecast. The S94 S-1 synthesis established the position shift
(Reading-NS, effacement-projected): Delta r/r = s_b * (c_b^(2)/c_Gold)^2.
For B1 that is 0.19 * (0.0798/0.915)^2 = 0.14452% (Sage-exact 0.19*17689/2325625),
OUTSIDE the DESI DR2 ruler (0.24%). The LIVE channel is therefore AMPLITUDE,
principally the S43 first-sound ring (A_FS = c_2^2/c_1^2 = 0.204, r1 = 325.3 Mpc),
which has NO LambdaCDM counterpart.

SUBSTRATE-FIRST (phononic-framing.md):
  D_K spectrum -> Layer-2 BdG branch speeds (c_B1..c_L <= c_Gold) -> substrate
  two-speed split -> effacement projection (c_b^(2)/c_Gold)^2 -> emergent BAO
  amplitude delta_P/P -> detector comparison.
  SCALE-AND-CHANNEL-TAGGED: the substrate-IS observable is the M_KK-internal
  per-branch two-speed split (M_KK units, inside the fiber); the laboratory-IN
  observable is the emergent BAO sub-feature amplitude delta_P/P at the CMB/LSS
  pivot k~0.043 Mpc^-1 and the S43 first-sound ring k1=0.0193 Mpc^-1 (Mpc^-1, in
  the container-observer's P(k)/C_ell). The BRIDGE is the effacement projection +
  the S43 transfer function -- NOT a borrowed LambdaCDM amplitude. The comparison
  against DESI DR2 / Simons / CMB-S4 is valid ONLY at the emergent/pivot scale.

[SIGN] DIRECTIONAL PRE-REGISTRATION (substitution chain, math-scripts.md):
  Claim: "the OBSERVED BAO sub-feature amplitude is the EFFACEMENT PROJECTION of the
          substrate two-speed split; the naive 19% is a container-thinking conflation
          of the M_KK-internal branch speed with the emergent 4D acoustic speed, and
          the transported amplitude is SMALLER than the naive split by (c_b^(2)/c_Gold)^2."
  Step 1: shift_frac (substrate, M_KK-internal)  = 0.19           [npz shift_frac; B1..B3]
  Step 2: b1_delta (substrate split magnitude)   = 0.01516        [npz b1_delta]
  Step 3: transport FORM A_obs,b = shift_b * (c_b^(2)/c_Gold)^2   [effacement projection;
          c_Gold=0.915 envelope; substrate-first, NOT borrowed LambdaCDM]
  Step 4: Substitute (Reading-NS, B1-dominant): (c_B1^(2)/c_Gold)^2 = 17689/2325625
          = 0.0076061 reduces 19% -> 0.14452% (position, Sage-exact 0.19*17689/2325625).
          The AMPLITUDE transport is the ANALOG projection onto delta_P/P, gated
          additionally by the S43 A_FS=0.204 first-sound imprint vs the ~3e-4 effacement
          leakage floor (1 - Gamma_effacement = 1 - 0.9997 = 3e-4).
  Step 5: (c_b^(2)/c_Gold)^2 < 1 since every Layer-2 branch speed v_g <= c_Gold=0.915
          (canonical envelope) ==> A_obs,b < shift_b. DIRECTION: the transported
          amplitude is SMALLER than the naive split (effacement SUPPRESSES). The
          B1-position image 0.14% < DESI DR2 ruler 0.24% confirms the suppression
          direction for position; the amplitude image inherits the same suppression sign.
  Conclusion: A_obs (transported amplitude) < naive split; effacement is a suppression,
          not an amplification. The live channel is the S43 first-sound ring (A_FS=0.204,
          no LambdaCDM counterpart), whose amplitude detectability sets the verdict.

  3-tuple:
    sign_verdict    : PASS iff transported amplitude is BELOW the naive split (predicted:
                      yes, effacement suppresses) AND on the correct side of the floor.
    magnitude_verdict: tracks |A_obs - S_exp| against the comparison anchor (or the
                      floor when paper-search is down).
    regime_verdict  : VALID iff the fetched-forecast domain was available; MARGINAL/
                      BREAKDOWN reserved for the paper-search-down INFO branch (the
                      forecast COMPARISON is unavailable, but the substrate forecast and
                      the suppression-direction structural conclusion are themselves VALID).

CONDITIONAL MCP DISCIPLINE
--------------------------
This gate's forecast comparison needs mcp__paper-search__* for the CMB-S4/SO amplitude
sensitivity (DOWN in S94). The orchestrator RE-CHECKED at dispatch: two arXiv queries
returned empty (service down). Per the PRE-REGISTERED INFO branch (a), the substrate
forecast is computed IN FULL; the bounding-estimate CMB-S4/SO floor (~0.01%) from the
S94 S-1 synthesis is used; the structural conclusion (suppression direction;
S43-ring-is-the-live-channel) is reported robust WITHOUT a fetched value; INFO is a
VERDICT, not a closure.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY import; never hardcode framework constants) ---
SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    Gamma_effacement,   # 0.9997  effacement transmission (S58 Volovik partition)
    c_Gold,             # 0.915   Goldstone sound speed, M_KK units (one true 4D cone)
    c_B1,               # 0.0798  Layer-2 emergent BdG branch speed (gapped B1)
    c_B2,               # 0.002
    c_B3,               # 0.1397  largest gapped branch speed (best-case channel)
    c_L,                # 0.0255  Leggett branch speed
)

# ---------------------------------------------------------------------------
# Identity / machinery pins (PRDR)
# ---------------------------------------------------------------------------
GATE_ID = "CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT"
SCHEME = "effacement-amplitude-projection-(c_b^2/c_Gold)^2"
CONVENTION = "RATIO-substrate-first-transport-NOT-borrowed-LCDM-amplitude"
L_MAX = "N/A"  # Layer-2 emergent BdG branch speeds; no D_K diagonalization (re-uses s94 npz)

HERE = Path(__file__).resolve().parent
S95_DIR = HERE if HERE.name == "session-95" else (HERE.parents[1] / "computations" / "session-95")
S95_DIR.mkdir(parents=True, exist_ok=True)

VERDICT_TXT = S95_DIR / "s95_gate_verdicts.txt"
NPZ_OUT = S95_DIR / "s95_w6_2_bao_amplitude_transport.npz"
PNG_OUT = S95_DIR / "s95_w6_2_bao_amplitude_transport.png"

CANONICAL_PY = SHARED / "canonical_constants.py"
S94_BAO_NPZ = HERE.parents[1] / "computations" / "session-94" / "s94_bao_peak_branch.npz"

# Pinned observational / detector anchors (ALL from fetched local sources, S94 S-1 synthesis)
K_BAO = 0.043            # (local) Mpc^-1  standard BAO scale (W5-3 / S43 0.0427)
K1_RING = 0.0193150486   # (local) Mpc^-1  S43 first-sound ring k1 = 2*pi/r1, r1=325.3 Mpc
R1_RING_MPC = 325.3      # (local) Mpc     S43 first-sound ring comoving scale
A_FS_S43 = 0.204         # (local) S43 KK-CMB-TF-43 A_FS = c_2^2/c_1^2 (knowledge graph eq_9611)
A_FS_PLAN_PIN = 0.2045   # (local) plan-text 4-sig-fig refinement of A_FS

# Forecast / measurement precision anchors (S94 S-1; researchers/Cosmic-Web/19 + Mack tree)
DESI_DR2_RULER = 0.0024     # (local) 0.24% DESI DR2 combined BAO ruler (fetched)
PLANCK_THETA_PREC = 0.00032 / 1.04077  # (local) 0.031% Planck 100*theta_* fractional precision
CMB_S4_FLOOR_EST = 0.0001   # (local) ~0.01% OPTIMISTIC next-gen acoustic-scale FLOOR
                            # (literature GAP per S94 S-1; bounding estimate, NOT a fetched pin)


def banner(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ===========================================================================
# Section 1 — Load S94 W5-3 substrate two-speed split machinery (cache-load only)
# ===========================================================================
banner("[1] LOAD — S94 W5-3 substrate two-speed split (s94_bao_peak_branch.npz)")
s94 = np.load(S94_BAO_NPZ, allow_pickle=True)
branch_names = list(s94["branch_names"])
c1_col = np.asarray(s94["c1"], dtype=float)      # Layer-1 (pre-fold) branch speeds (M_KK units)
c2_col = np.asarray(s94["c2"], dtype=float)      # Layer-2 (post-fold) emergent BdG branch speeds
delta_col = np.asarray(s94["delta"], dtype=float)        # c1 - c2 per branch (M_KK units)
shift_frac_col = np.asarray(s94["shift_frac"], dtype=float)  # fractional split per branch
b1_delta = float(s94["b1_delta"])                # 0.015162 (M_KK-internal B1 split magnitude)
shift_frac = float(shift_frac_col[1])            # 0.19 (B1 fractional split; the substrate split)
gold_delta = float(s94["gold_delta"])            # 0.0 (Goldstone protected, no split)

print(f"    branch_names      = {branch_names}")
print(f"    c2 (Layer-2 emerg)= {c2_col.tolist()}")
print(f"    delta (c1-c2)     = {delta_col.tolist()}")
print(f"    shift_frac        = {shift_frac_col.tolist()}")
print(f"    b1_delta (M_KK)   = {b1_delta:.6f}   shift_frac(B1) = {shift_frac:.6f}")
print(f"    gold_delta        = {gold_delta:.1e}  (Goldstone PROTECTED, no split)")

# cross-check the canonical-constants branch speeds match the npz c2 column (Layer-2)
assert abs(c2_col[1] - c_B1) < 1e-12, f"c_B1 mismatch: npz {c2_col[1]} vs canonical {c_B1}"
assert abs(c2_col[3] - c_B3) < 1e-12, f"c_B3 mismatch: npz {c2_col[3]} vs canonical {c_B3}"
assert abs(c2_col[0] - c_Gold) < 1e-12, f"c_Gold mismatch: npz {c2_col[0]} vs canonical {c_Gold}"
print(f"    [x-check] npz c2 column == canonical (c_Gold,c_B1,c_B3) = "
      f"({c2_col[0]},{c2_col[1]},{c2_col[3]})  OK")

# ===========================================================================
# Section 2 — Effacement-projection transport: per-branch OBSERVED amplitude
# ===========================================================================
banner("[2] TRANSPORT — effacement projection A_eff,b = (c_b^(2)/c_Gold)^2  (per gapped branch)")
# The substrate two-speed split shift_frac=0.19 lives on the M_KK-internal Layer-2 branch
# speed c_b^(2) (sub-luminal). To reach the EMERGENT 4D acoustic channel (Goldstone c_Gold,
# the one true light cone) it projects with the effacement amplitude (c_b^(2)/c_Gold)^2 --
# the SAME (speed-ratio)^2 FORM as the S43 first-sound A_FS = c_2^2/c_1^2 = 0.204.
A_eff = (c2_col / c_Gold) ** 2                    # (local) per-branch effacement projection weight
A_obs_pos = shift_frac_col * A_eff                # (local) transported POSITION shift per branch
# The OBSERVED sub-feature AMPLITUDE delta_P/P is the analog projection: the per-branch
# fractional power modulation = (fractional speed split) * (effacement projection weight).
# delta_P/P_b ~ shift_frac_b * A_eff,b  (the amplitude image of the same suppression).
A_obs_amp = shift_frac_col * A_eff                # (local) transported AMPLITUDE delta_P/P per branch

# Goldstone is protected (shift_frac=0) -> zero amplitude (the protected acoustic carrier).
# The gapped branches (B1..B3, Leggett, Optical) carry the sub-features.
gapped_idx = [i for i, p in enumerate(s94["is_protected"]) if not bool(p)]
print(f"    branch          c2(M_KK)   A_eff=(c2/c_Gold)^2   shift_frac   A_obs(delta_P/P)")
for i, nm in enumerate(branch_names):
    print(f"    {nm:12s}  {c2_col[i]:8.5f}   {A_eff[i]:.6e}        "
          f"{shift_frac_col[i]:.4f}       {A_obs_amp[i]:.6e}")

# Principal channels
A_eff_B1 = float((c_B1 / c_Gold) ** 2)            # (local) 17689/2325625 = 0.0076061
A_eff_B3 = float((c_B3 / c_Gold) ** 2)            # (local) largest gapped (best-case)
A_obs_B1 = float(shift_frac * A_eff_B1)           # (local) B1 transported amplitude (B1-dominant)
A_obs_B3 = float(0.19 * A_eff_B3)                 # (local) B3 best-case transported amplitude
print(f"\n    A_eff,B1 = (c_B1/c_Gold)^2 = {A_eff_B1:.6e}  (Sage-exact 17689/2325625)")
print(f"    A_eff,B3 = (c_B3/c_Gold)^2 = {A_eff_B3:.6e}  (best-case gapped branch)")
print(f"    A_obs,B1 (delta_P/P, B1-dominant) = 0.19 * {A_eff_B1:.6e} = {A_obs_B1:.6e}")
print(f"    A_obs,B3 (delta_P/P, best-case)   = 0.19 * {A_eff_B3:.6e} = {A_obs_B3:.6e}")

# ===========================================================================
# Section 3 — S43 transfer-function level vs effacement floor (which channel imprints?)
# ===========================================================================
banner("[3] S43 TRANSFER FUNCTION — first-sound ring (A_FS) vs effacement leakage floor")
# Effacement LEAKAGE floor: the residual transmission through the impedance mismatch.
# Gamma_effacement = 0.9997 => the effacement LEAKAGE (residual, the part that escapes
# the effacement projection onto pure 4D) = 1 - Gamma = 3e-4. The plan's "~1e-6 effacement
# floor" is the SQUARE (a two-leg leakage), reported as the conservative deep floor.
eff_leak_floor = 1.0 - Gamma_effacement           # (local) 3e-4 single-leg effacement leakage
eff_floor_deep = eff_leak_floor ** 2              # (local) ~9e-8 two-leg deep floor (~1e-6 class)
print(f"    Gamma_effacement                 = {Gamma_effacement}")
print(f"    effacement leakage (1 - Gamma)   = {eff_leak_floor:.3e}  (single-leg)")
print(f"    effacement deep floor (1-Gamma)^2= {eff_floor_deep:.3e}  (two-leg; plan ~1e-6 class)")
print(f"    S43 first-sound ring A_FS        = {A_FS_S43} (knowledge graph eq_9611; "
      f"plan pin {A_FS_PLAN_PIN})")
print(f"    S43 ring scale  r1 = {R1_RING_MPC} Mpc  ->  k1 = 2*pi/r1 = {K1_RING:.7f} Mpc^-1")

# The S43 first-sound ring is a DISTINCT, much larger imprint than the per-branch
# effacement-projected amplitude: A_FS=0.204 is an O(0.2) feature on the matter power
# spectrum at k1, with NO LambdaCDM counterpart. The per-branch sub-feature amplitudes
# A_obs_B1..B3 (~1e-3 -- 4e-3) sit far ABOVE the deep effacement floor (~1e-6) but far
# BELOW the S43 ring (0.204). So the LIVE channel is the S43 ring; the per-branch
# sub-features are a secondary, weaker amplitude modulation.
print(f"\n    A_obs,B1 = {A_obs_B1:.3e} ; A_obs,B3 = {A_obs_B3:.3e}")
print(f"    vs effacement deep floor {eff_floor_deep:.3e}: "
      f"per-branch sub-feature is {'ABOVE' if A_obs_B1 > eff_floor_deep else 'BELOW'} the floor "
      f"(ratio {A_obs_B1/eff_floor_deep:.2e}x)")
print(f"    vs S43 ring A_FS {A_FS_S43}: per-branch sub-feature is "
      f"{'BELOW' if A_obs_B1 < A_FS_S43 else 'ABOVE'} the ring "
      f"(the S43 ring is the LIVE channel, {A_FS_S43/A_obs_B1:.0f}x larger)")

# ===========================================================================
# Section 4 — Build a P(k) sub-feature model on a log-k grid (for the plot + pinned scales)
# ===========================================================================
banner("[4] P(k) SUB-FEATURE MODEL — log-k grid; two pinned scales (k_BAO, k1_ring)")
k_grid = np.logspace(-3, -1, 257)                 # (local) Mpc^-1, [1e-3, 1e-1], >=256 pts
# Gaussian-localized sub-feature bumps:
#  (i) per-branch B1 sub-feature at k_BAO with amplitude A_obs_B1 (effacement-projected);
#  (ii) S43 first-sound ring at k1 with amplitude A_FS (the live, no-LCDM-counterpart feature).
sigma_lnk = 0.08                                  # (local) feature width in ln k
bump_B1 = A_obs_B1 * np.exp(-0.5 * (np.log(k_grid / K_BAO) / sigma_lnk) ** 2)   # (local)
bump_ring = A_FS_S43 * np.exp(-0.5 * (np.log(k_grid / K1_RING) / sigma_lnk) ** 2)  # (local)
delta_P_over_P = bump_B1 + bump_ring              # (local) total fractional modulation model
A_obs_at_kbao = float(delta_P_over_P[np.argmin(np.abs(k_grid - K_BAO))])      # (local)
A_ring_at_k1 = float(delta_P_over_P[np.argmin(np.abs(k_grid - K1_RING))])     # (local)
print(f"    delta_P/P at k_BAO=0.043 Mpc^-1     = {A_obs_at_kbao:.6e}  (per-branch B1 sub-feature)")
print(f"    delta_P/P at k1_ring=0.0193 Mpc^-1  = {A_ring_at_k1:.6e}  (S43 first-sound ring; LIVE)")

# ===========================================================================
# Section 5 — Forecast comparison (CONDITIONAL on paper-search MCP availability)
# ===========================================================================
banner("[5] FORECAST COMPARISON — paper-search MCP availability gate")
# Orchestrator RE-CHECKED mcp__paper-search__* at dispatch (DOWN in S94). Two arXiv
# queries returned empty {"result":[]} (service down). PRE-REGISTERED INFO branch (a).
PAPER_SEARCH_AVAILABLE = False  # (local) re-checked at dispatch: empty results => DOWN
fetched_forecast_value = None   # (local) no fetched S_exp -> INFO branch (a)

# Use the bounding-estimate CMB-S4/SO floor from the S94 S-1 synthesis as S_exp surrogate.
S_exp_used = CMB_S4_FLOOR_EST   # (local) ~0.01% bounding estimate (NOT a fetched pin)
print(f"    PAPER_SEARCH_AVAILABLE = {PAPER_SEARCH_AVAILABLE}  (re-checked at dispatch; 2 empty queries)")
print(f"    => PRE-REGISTERED INFO branch (a): forecast computed in full; S_exp from the")
print(f"       S94 S-1 bounding estimate (CMB-S4/SO floor ~{CMB_S4_FLOOR_EST*100:.2f}%), NOT fetched.")
print(f"\n    Comparison anchors (amplitude / acoustic-scale precision):")
for label, prec in [("Planck theta_* (0.031%)", PLANCK_THETA_PREC),
                    ("DESI DR2 ruler (0.24%)", DESI_DR2_RULER),
                    ("CMB-S4/SO floor (~0.01% est)", CMB_S4_FLOOR_EST)]:
    for chan, amp in [("B1 sub-feature", A_obs_B1), ("S43 ring A_FS", A_FS_S43)]:
        inside = amp >= prec
        print(f"      {chan:16s} A={amp:.3e}  vs {label:30s} {prec:.3e}: "
              f"{'WITHIN (detectable)' if inside else 'BELOW (sub-precision)'}")

# Structural determinations (robust WITHOUT the fetched value):
#  - S43 ring A_FS=0.204 is WAY ABOVE every precision anchor -> if the ring imprints on
#    the matter P(k)/C_ell it is amplitude-DETECTABLE. But its detectability is set by
#    the S43 coupling (fabric internal modes <-> photon-baryon fluid), an UNTESTED
#    prediction, and the comparison against a named experiment's AMPLITUDE sensitivity
#    (not just acoustic-scale ruler) requires the fetched forecast -> carried forward.
#  - Per-branch B1 sub-feature A_obs_B1~1.4e-3 is ABOVE the deep effacement floor but
#    BELOW DESI DR2 (matching the position result) -> a next-gen / sub-precision target.
ring_above_all = A_FS_S43 >= max(DESI_DR2_RULER, PLANCK_THETA_PREC, CMB_S4_FLOOR_EST)
b1_above_floor = A_obs_B1 > eff_floor_deep
b1_below_desi = A_obs_B1 < DESI_DR2_RULER
print(f"\n    [structural] S43 ring above ALL precision anchors : {ring_above_all}")
print(f"    [structural] B1 sub-feature above deep eff floor  : {b1_above_floor}")
print(f"    [structural] B1 sub-feature below DESI DR2 ruler  : {b1_below_desi}")

# ===========================================================================
# Section 6 — [SIGN] 3-tuple + composite verdict (deterministic collapse rule)
# ===========================================================================
banner("[6] VERDICT — [SIGN] 3-tuple + composite collapse (gate-verdicts.md schema-v2)")
# SIGN: predicted A_obs < naive split (effacement SUPPRESSES). Verify the direction.
naive_split = shift_frac                          # (local) 0.19 (the unmatched substrate-scale #)
sign_suppression_ok = (A_obs_B1 < naive_split) and (A_eff_B1 < 1.0)
# Also the position cross-check: B1 image 0.14% < DESI DR2 0.24% (same suppression sign).
pos_below_desi = (shift_frac * A_eff_B1) < DESI_DR2_RULER
sign_v = "PASS" if (sign_suppression_ok and pos_below_desi) else "FAIL"

# MAGNITUDE: |A_obs - S_exp| against the (surrogate) comparison anchor. In the INFO
# branch the magnitude cannot DISCRIMINATE detectability without the fetched amplitude
# sensitivity -> magnitude_verdict = INFO (band between PASS and FAIL; not a clean PASS).
mag_gap_B1 = abs(A_obs_B1 - S_exp_used)           # (local)
mag_v = "INFO"   # forecast comparison anchor is a bounding estimate, not a fetched pin

# REGIME: VALID iff the fetched-forecast domain was available. Paper-search DOWN ->
# the forecast COMPARISON domain is unavailable. Per the auto-shortening discipline the
# fetched-forecast leg is 0% available => the comparison regime is BREAKDOWN, which (by
# the pre-registered collapse rule) forces composite=INFO via the INFO_meaning branch (a).
# NB: the SUBSTRATE forecast and the suppression-direction conclusion are themselves VALID;
# it is specifically the experiment-comparison leg that is unavailable. We tag the regime
# of the experiment-comparison leg = BREAKDOWN (paper-search down) and let the composite
# collapse to the pre-registered INFO branch (a).
regime_v = "BREAKDOWN" if not PAPER_SEARCH_AVAILABLE else "VALID"

# Deterministic composite collapse (gate-verdicts.md; modifications are Class-3 violations).
# Pre-registered INFO branch (a): paper-search DOWN => INFO (a VERDICT, not a FAIL/closure).
if not PAPER_SEARCH_AVAILABLE:
    composite = "INFO"            # PRE-REGISTERED INFO branch (a)
elif regime_v == "BREAKDOWN":
    composite = "FAIL"
elif sign_v == "FAIL":
    composite = "FAIL"
elif mag_v == "FAIL" and regime_v == "VALID":
    composite = "FAIL"
elif mag_v == "FAIL" and regime_v == "MARGINAL":
    composite = "INFO"
elif mag_v == "INFO":
    composite = "INFO"
else:
    composite = "PASS"

print(f"    naive substrate split (unmatched)          = {naive_split:.4f}  (19%)")
print(f"    A_obs,B1 (transported amplitude)           = {A_obs_B1:.6e}")
print(f"    sign_suppression_ok (A_obs < naive split)  = {sign_suppression_ok}")
print(f"    position cross-check (0.14% < DESI 0.24%)  = {pos_below_desi}")
print(f"    => sign_verdict     = {sign_v}")
print(f"    => magnitude_verdict= {mag_v}  (|A_obs,B1 - S_exp_est| = {mag_gap_B1:.3e}; surrogate anchor)")
print(f"    => regime_verdict   = {regime_v}  (paper-search DOWN => forecast-comparison leg unavailable)")
print(f"    => COMPOSITE        = {composite}  (PRE-REGISTERED INFO branch (a))")

# Descriptive value string (names the paper-search-down INFO branch per the plan).
value_str = (
    f"composite={composite};"
    f"A_obs_B1_delta_P_over_P={A_obs_B1:.6e};"
    f"A_obs_B3_best={A_obs_B3:.6e};"
    f"A_eff_B1=(c_B1/c_Gold)^2={A_eff_B1:.6e}_Sage_17689/2325625;"
    f"naive_split=0.19_container_conflation;"
    f"effacement_SUPPRESSES_A_obs_below_naive_split=True;"
    f"S43_first_sound_ring_A_FS={A_FS_S43}_at_k1={K1_RING:.4f}Mpc-1_r1={R1_RING_MPC}Mpc_LIVE_CHANNEL_no_LCDM_counterpart;"
    f"eff_deep_floor={eff_floor_deep:.3e};"
    f"B1_above_floor={b1_above_floor}_below_DESI_DR2_0.24pct={b1_below_desi};"
    f"experiment_sensitivity_unavailable_paper-search-MCP-down_PRE-REG-INFO-branch-a;"
    f"S_exp_surrogate=CMB-S4_SO_floor_~0.01pct_bounding-estimate-NOT-fetched"
)

# ===========================================================================
# Section 7 — Plot
# ===========================================================================
banner("[7] PLOT")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

# Left: P(k) sub-feature model with the two pinned scales
ax1.semilogx(k_grid, delta_P_over_P, "-", color="navy", lw=1.8,
             label=r"$\delta P/P$ model (B1 sub-feature + S43 ring)")
ax1.axvline(K_BAO, color="darkorange", ls="--", lw=1.2,
            label=fr"$k_{{\rm BAO}}={K_BAO}$ Mpc$^{{-1}}$ (B1 sub-feature)")
ax1.axvline(K1_RING, color="crimson", ls=":", lw=1.4,
            label=fr"$k_1={K1_RING:.4f}$ Mpc$^{{-1}}$ (S43 ring, $r_1$={R1_RING_MPC} Mpc)")
ax1.axhline(eff_floor_deep, color="gray", ls="-.", lw=1.0,
            label=fr"deep effacement floor $(1-\Gamma)^2={eff_floor_deep:.1e}$")
ax1.set_xlabel(r"$k$ [Mpc$^{-1}$]")
ax1.set_ylabel(r"$\delta P/P$ (fractional modulation)")
ax1.set_title("BAO sub-feature amplitude (substrate-first, effacement-projected)")
ax1.legend(fontsize=7.5, loc="upper left")
ax1.grid(alpha=0.3)

# Right: per-branch effacement projection (suppression) + comparison anchors
gi = gapped_idx
gnames = [branch_names[i] for i in gi]
gA = [A_obs_amp[i] for i in gi]
xpos = np.arange(len(gi))
ax2.bar(xpos, gA, color="steelblue", alpha=0.8, label=r"$A_{\rm obs}=\delta P/P$ per branch")
ax2.axhline(naive_split, color="black", ls="--", lw=1.3,
            label=fr"naive split $s$={naive_split} (container-conflation, UNMATCHED)")
ax2.axhline(A_FS_S43, color="crimson", ls=":", lw=1.6,
            label=fr"S43 ring $A_{{\rm FS}}$={A_FS_S43} (LIVE channel)")
ax2.axhline(DESI_DR2_RULER, color="darkorange", ls="-.", lw=1.1,
            label=fr"DESI DR2 ruler {DESI_DR2_RULER}")
ax2.axhline(CMB_S4_FLOOR_EST, color="green", ls="-.", lw=1.1,
            label=fr"CMB-S4/SO floor ~{CMB_S4_FLOOR_EST} (est)")
ax2.axhline(eff_floor_deep, color="gray", ls="-.", lw=0.9,
            label=fr"deep eff floor {eff_floor_deep:.1e}")
ax2.set_yscale("log")
ax2.set_xticks(xpos)
ax2.set_xticklabels(gnames, rotation=35, ha="right", fontsize=8)
ax2.set_ylabel(r"amplitude $\delta P/P$ (log)")
ax2.set_title(r"Effacement SUPPRESSES: $A_{\rm obs,b}=s\,(c_b^{(2)}/c_{\rm Gold})^2 < s$")
ax2.legend(fontsize=7, loc="lower left")
ax2.grid(alpha=0.3, which="both")

fig.suptitle(f"{GATE_ID} — two-speed amplitude transport (INFO: paper-search down, "
             f"pre-reg branch a)", fontsize=11)
fig.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig(PNG_OUT, dpi=130)
plt.close(fig)
print(f"    wrote {PNG_OUT}")

# ===========================================================================
# Section 8 — Save data
# ===========================================================================
banner("[8] SAVE NPZ")
np.savez(
    NPZ_OUT,
    gate_id=GATE_ID,
    branch_names=np.array(branch_names, dtype=object),
    c2_col=c2_col, c1_col=c1_col, delta_col=delta_col, shift_frac_col=shift_frac_col,
    A_eff=A_eff, A_obs_amp=A_obs_amp, A_obs_pos=A_obs_pos,
    b1_delta=b1_delta, shift_frac=shift_frac, naive_split=naive_split,
    A_eff_B1=A_eff_B1, A_eff_B3=A_eff_B3, A_obs_B1=A_obs_B1, A_obs_B3=A_obs_B3,
    c_Gold=c_Gold, c_B1=c_B1, c_B3=c_B3, Gamma_effacement=Gamma_effacement,
    eff_leak_floor=eff_leak_floor, eff_floor_deep=eff_floor_deep,
    A_FS_S43=A_FS_S43, A_FS_plan_pin=A_FS_PLAN_PIN,
    k_bao=K_BAO, k1_ring=K1_RING, r1_ring_mpc=R1_RING_MPC,
    k_grid=k_grid, delta_P_over_P=delta_P_over_P,
    A_obs_at_kbao=A_obs_at_kbao, A_ring_at_k1=A_ring_at_k1,
    desi_dr2_ruler=DESI_DR2_RULER, planck_theta_prec=PLANCK_THETA_PREC,
    cmb_s4_floor_est=CMB_S4_FLOOR_EST, S_exp_used=S_exp_used,
    paper_search_available=PAPER_SEARCH_AVAILABLE,
    fetched_forecast_value=(np.nan if fetched_forecast_value is None else fetched_forecast_value),
    ring_above_all=ring_above_all, b1_above_floor=b1_above_floor, b1_below_desi=b1_below_desi,
    sign_v=sign_v, mag_v=mag_v, regime_v=regime_v, composite=composite,
    value_str=value_str,
)
print(f"    wrote {NPZ_OUT}")

# ===========================================================================
# Section 9 — Dual-SHA + schema-v2 3-tuple verdict-line emission
# ===========================================================================
banner("[9] VERDICT-LINE EMISSION (dual-SHA + schema-v2 3-tuple; [SIGN] trigger)")


def build_pinmap():
    """Ordered input-pin map; audit_sha256 := SHA256(script||canonical||s94_npz||pinmap_json)."""
    pins = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "N_eval": "P(k) log-k grid [1e-3,1e-1] 257 pts; pinned k=0.043, k1=0.0193",
        "scan_range": "k in [1e-3,1e-1] Mpc^-1 log-spaced",
        "tolerance": "RATIO; delta_P/P to 3 sig figs (rel_tol>=1e-3)",
        "random_seed": "N/A-deterministic",
        "GPU_path": "numpy (1D transport; cache-load only)",
        "shift_frac": f"{shift_frac:.6f}",
        "b1_delta": f"{b1_delta:.6f}",
        "c_Gold": f"{c_Gold}",
        "c_B1": f"{c_B1}",
        "c_B3": f"{c_B3}",
        "Gamma_effacement": f"{Gamma_effacement}",
        "A_eff_B1": f"{A_eff_B1:.10e}",
        "A_obs_B1": f"{A_obs_B1:.10e}",
        "A_FS_S43": f"{A_FS_S43}",
        "k1_ring": f"{K1_RING:.7f}",
        "paper_search_available": str(PAPER_SEARCH_AVAILABLE),
        "fetched_forecast_value_or_INFO_flag": "INFO-branch-a-paper-search-down",
        "S_exp_used": f"{S_exp_used:.6e}",
        "sign_v": sign_v, "mag_v": mag_v, "regime_v": regime_v, "composite": composite,
    }
    return pins


def compute_dual_sha(script_path, canonical_path, s94_path, pins):
    """audit := SHA256(script_bytes || canonical_bytes || s94_npz_bytes || sorted-pinmap-JSON);
       content := SHA256(script_bytes)."""
    def _rb(p):
        try:
            return p.read_bytes()
        except OSError:
            return b""
    script_bytes = _rb(script_path)          # (local)
    canonical_bytes = _rb(canonical_path)    # (local)
    s94_bytes = _rb(s94_path)                # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h = hashlib.sha256()                     # (local)
    h.update(script_bytes); h.update(canonical_bytes); h.update(s94_bytes); h.update(pinmap_json)
    audit = h.hexdigest()                    # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict, value, audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Append canonical verdict line + dual-SHA companion row + schema-v2 3-tuple row.
    [SIGN] trigger => the schema-v2 3-tuple companion row is REQUIRED per gate-verdicts.md."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )  # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] directional pre-reg: "
        f"effacement SUPPRESSES A_obs below naive 19% split [(c_b^2/c_Gold)^2<1]; "
        f"regime=BREAKDOWN = forecast-comparison leg unavailable (paper-search DOWN) "
        f"=> PRE-REG INFO branch (a))\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tuple_row)


pins = build_pinmap()
audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL_PY, S94_BAO_NPZ, pins)
print(f"    audit_sha256   = {audit_sha}")
print(f"    content_sha256 = {content_sha}")
print(f"    INPUT SHA pins : canonical_constants.py + s94_bao_peak_branch.npz + script + pinmap")

# Emit exactly one canonical line + companion + 3-tuple row.
append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v)
print(f"    appended verdict line to {VERDICT_TXT}")

# Final non-verdict 4-tuple output tag (per gate-verdicts.md step 2)
banner("4-TUPLE OUTPUT TAG")
print(f"(value={composite}/A_obs_B1={A_obs_B1:.3e}, scheme={SCHEME}, "
      f"convention={CONVENTION}, L_max={L_MAX})")
print(f"3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")

sys.exit(0)  # script health: ran successfully and produced a valid verdict (INFO is a result)
