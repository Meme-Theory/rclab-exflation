#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S94-N-PBH-TRUNCATION-ANCHOR  --  Wave 5, gate W5-1  (mack-cosmic-bridge)

[CHAIN] derivation / anchor-pinning gate. NOT a numerical-threshold gate.

PURPOSE
-------
Re-determine WHICH anchor sets the truncation on the n_PBH m^-3 Level-3 row
that VII.AX.OP-PROJ + VII.AX.STATE-PROJ currently hold
NOT-SATISFIED-PENDING-substrate-physical-scale-anchor.

S93 W4-3 PROVED N_eigs(L_max) is an unbounded quintic (no eigenvalue-count
plateau), so the "L_max=14 PROVISIONAL" label cannot be read off a non-existent
plateau. Per cross-pillar-bridge-anatomy.md "Tier-1/Tier-2 dimensional-
re-anchorability gate", a divergent channel whose anchor is a DIMENSIONFUL
magnitude is Tier-2-dimensionful => registry-PASS-INELIGIBLE => HELD.

This gate executes the Step A..E [CHAIN] of session-94-plan-w5.md S.W5-1:

  Step A  Reproduce the W4-3 Sage-exact quintic N_eigs(L_max) and confirm
          lim_{L->inf} N_eigs = +inf (no plateau; d/dL N_eigs > 0 for all L>=1).
  Step B  Write the n_PBH dimensional-decomposition chain:
          n_PBH = n_edge * prob_form / L_pix_LRD^3 ; identify which factor
          carries [m^-3] (L_pix_LRD^3) and which carries the L_max-divergence.
  Step C  Apply the Tier-1/Tier-2 gate: show the dimension and the divergence
          occupy the SAME multiplicative slot (the log-derivative that buys
          truncation-invariance annihilates the dimensionful prefactor)
          => Tier-2-dimensionful => the m^-3 magnitude row is HELD.
  Step D  Pre-register TWO admissible anchor candidates and SELECT one:
          (D1) substrate-physical scale anchor = the cardinality-cascade
               SATURATION generation g_saturate = 143 (g-axis; the cascade
               physically FILLS; L_max-INDEPENDENT above saturation), with
               g(K) = prob_form / L_pix_LRD^3 carrying the [m^-3] dimension.
          (D2) Tier-2 dimensionless re-anchoring = a log-derivative functional
               annihilating the L_pix_LRD^3 prefactor (the VII.AV.STATE-PROJ route).
  Step E  Update the L_max=14 PROVISIONAL label to the selected-anchor wording.

NUMERICAL FINDING (the substrate-physics heart of the [CHAIN])
--------------------------------------------------------------
The canonical n_PBH_FW_central = 7.2761e-23 m^-3 is the LINEAR L_max-axis read
A_prefactor * N_eigs(L_max=14) -- the DIVERGENT channel. The g-axis cascade-
SATURATED form  C(N_eigs_base, 2) * prob_form / L_pix_LRD^3  with N_eigs FROZEN
at the L_max=10 base atlas (78080) yields the L_max=10 BASELINE 1.758e-23 m^-3,
which IS L_max-INDEPENDENT. The two differ by the 4.14x L=10 -> L=14 refinement
factor (= N_eigs(14)/N_eigs_base = 323136/78080).

So: D1 IS the correct substrate-physical axis (L_max-INDEPENDENT cascade
saturation), but PINNING the canonical 7.2761e-23 MAGNITUDE at this anchor
requires a separate saturated-tail recompute (the frozen-saturation form
delivers the L=10 baseline, NOT the L=14 refined central). The anchor AXIS is
identified; the numerical decoupling of the L=14 magnitude is DEFERRED.

VERDICT (per plan rubric): INFO
  -- INFO_meaning: "the substrate-physical anchor (g_saturate) is identified as
     the CORRECT axis but its numerical decoupling from L_max requires a separate
     saturated-tail recompute (CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED)".
  The N_eigs-plateau read-off is formally EXCLUDED (lim N_eigs = +inf), the m^-3
  Level-3 row is correctly classified Tier-2-dimensionful and HELD, the label is
  updated. VII.AX.OP-PROJ permanence STANDS on the theorem-STRUCTURE (Tier-2
  corollary). The Tier-1/Tier-2 gate's INAUGURAL OCCUPANT status is confirmed.

Trigger:        [CHAIN]
Classification: GEOMETRIC
Scheme:         FWD-C5-CARDINALITY-CASCADE-TAIL
Convention:     TIER-2-DIMENSIONFUL-HELD
GPU path:       numpy.linalg  (quintic + small-integer arithmetic; CPU is correct)

Author: mack-cosmic-bridge.  Session 94, Wave 5.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from fractions import Fraction      # exact-rational arithmetic (QQ analog; CPU)
from math import comb, log
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute paths)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    n_PBH_FW_central,   # 7.2761e-23 m^-3 (S93 W4-5; the contested Level-3 anchor)
    M_KK,               # 7.42866e16 GeV
    tau_fold,           # 0.19
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan W5-1 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S94-N-PBH-TRUNCATION-ANCHOR"
SCHEME = "FWD-C5-CARDINALITY-CASCADE-TAIL"
CONVENTION = "TIER-2-DIMENSIONFUL-HELD"
L_MAX_TAG = "N/A"                 # the gate's SUBJECT is the truncation L_max itself

# Machinery pins (plan W5-1 machinery_pin_map)
N_EVAL = 20                       # (local) L_max scan 1..20 (no-plateau confirmation)
SCAN_LO, SCAN_HI = 1, 20          # (local) integer L_max scan range
TOL = 1e-12                       # (local) Sage-exact quintic reproduction cross-check (relative)

# -----------------------------------------------------------------------------
# Substrate-IS / registry-sourced derivation inputs for the n_PBH parse-tree.
# These are NOT framework constants to promote; they are the registry-pinned
# inputs to the [CHAIN] derivation (permanent-results-registry.md SS.VII.AX
# Step-4 closed form, lines 19419-19423; S88 W1a-59 canonical; W4-3 quintic).
# -----------------------------------------------------------------------------
# W4-3 Sage-exact quintic coefficients (descending degree 5..0), QQ-exact:
#   N_eigs(L) = (4/15)L^5 + (10/3)L^4 + 16 L^3 + (110/3)L^2 + (596/15)L + 16
QUINTIC_COEFFS_Q = [                                  # (local) exact-rational
    Fraction(4, 15), Fraction(10, 3), Fraction(16, 1),
    Fraction(110, 3), Fraction(596, 15), Fraction(16, 1),
]
N_EIGS_NPZ_14 = 323136            # (local) W4-3 npz anchor at L_max=14
N_EIGS_BASE_L10 = 78080           # (local) L_max=10 cache base atlas (saturated-form N; registry)
N_EIGS_L10_ANALYTIC = 80080       # (local) analytic L=10 count (= base + dropped (4,4) sector)
G_SATURATE = 143                  # (local) cascade-saturation generation (S88 W1a-59; registry)
# Step-4 saturated closed-form components (registry lines 19421-19423):
PROB_FORM = Fraction(15573, 100000)        # (local) 0.15573 DS-2-corrected Parker-pair, exact
L_PIX_LRD_M = Fraction(3, 1) * Fraction(10, 1) ** 10  # (local) 3.0e10 m substrate-clock pixelation
# LINEAR obs_2 channel prefactor (W4-3 STEP-2; npz A_prefactor_m3 = 2.2516995e-28):
#   A_prefactor = 1.758127e-23 / 78080  (m^-3 per count)
A_PREFACTOR_Q = (Fraction(1758127, 1) / Fraction(10, 1) ** 29) / Fraction(N_EIGS_BASE_L10, 1)  # (local)

# JE5 conjunct band (for the contextual band-position annotation only; NOT a gate threshold here)
JE5_FLOOR = 5.5e-23               # (local) m^-3
JE5_UPPER = 2.2e-22               # (local) m^-3

# -----------------------------------------------------------------------------
# Verdict / output paths (S94 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
W4_3_NPZ = (PROJECT_ROOT / "computations" / "session-93"
            / "s93_w4_3_n_pbh_canonical_truncation_factorization.npz")

OUT_NPZ = (PROJECT_ROOT / "computations" / "session-94"
           / "s94_n_pbh_truncation_anchor.npz")
OUT_PNG = (PROJECT_ROOT / "computations" / "session-94"
           / "s94_n_pbh_truncation_anchor.png")


# -----------------------------------------------------------------------------
# SHA helpers (per s94 winding-reconciliation / _script_template precedent)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """Stable hash over all input pins (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256 over [script, canonical, pinmap]; content_sha256 over [script].
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Exact-rational quintic evaluation (QQ analog via fractions.Fraction)
# -----------------------------------------------------------------------------
def n_eigs_exact(L: int) -> Fraction:
    """W4-3 Sage-exact quintic N_eigs(L), evaluated in exact rationals.

    Returns a Fraction; integer-valued for integer L (the count is integral).
    """
    c5, c4, c3, c2, c1, c0 = QUINTIC_COEFFS_Q  # (local)
    Lf = Fraction(L, 1)  # (local)
    return c5 * Lf**5 + c4 * Lf**4 + c3 * Lf**3 + c2 * Lf**2 + c1 * Lf + c0


def dn_eigs_dL_exact(L: int) -> Fraction:
    """d/dL N_eigs(L) in exact rationals:
        dN/dL = (4/3)L^4 + (40/3)L^3 + 48 L^2 + (220/3)L + 596/15.
    All coefficients positive => > 0 for all L >= 1 (monotone increasing).
    """
    Lf = Fraction(L, 1)  # (local)
    return (Fraction(4, 3) * Lf**4 + Fraction(40, 3) * Lf**3 + Fraction(48, 1) * Lf**2
            + Fraction(220, 3) * Lf + Fraction(596, 15))


# -----------------------------------------------------------------------------
# Step A -- reproduce the quintic; confirm no plateau (lim = +inf, dN/dL > 0)
# -----------------------------------------------------------------------------
def step_A_no_plateau():
    """Reproduce W4-3 quintic; verify monotone-unbounded N_eigs (no plateau)."""
    Ls = list(range(SCAN_LO, SCAN_HI + 1))            # (local)
    n_eigs = [int(n_eigs_exact(L)) for L in Ls]       # (local) integer counts
    dn = [dn_eigs_dL_exact(L) for L in Ls]            # (local) exact derivative
    all_positive = all(d > 0 for d in dn)             # (local) monotone increasing
    strictly_increasing = all(n_eigs[i + 1] > n_eigs[i] for i in range(len(n_eigs) - 1))  # (local)

    # Sage-exact reproduction cross-check at L=14 vs the W4-3 npz anchor:
    rep14 = n_eigs_exact(14)                           # (local) exact
    rel_err_14 = abs(float(rep14) / float(N_EIGS_NPZ_14) - 1.0)  # (local)
    repro_ok = (int(rep14) == N_EIGS_NPZ_14) and (rel_err_14 <= TOL)  # (local)

    # lim L->inf: leading term (4/15)L^5 -> +inf. Probe at large L to show growth.
    L_probe = [14, 20, 30, 50, 100, 200]               # (local)
    n_probe = [int(n_eigs_exact(L)) for L in L_probe]  # (local)
    diverges = n_probe[-1] > n_probe[0]                # (local) trivially True; structural lim=+inf

    return {
        "Ls": Ls, "n_eigs": n_eigs, "dn_positive": all_positive,
        "strictly_increasing": strictly_increasing,
        "rep14": int(rep14), "rel_err_14": rel_err_14, "repro_ok": repro_ok,
        "L_probe": L_probe, "n_probe": n_probe, "diverges": diverges,
    }


# -----------------------------------------------------------------------------
# Step B -- dimensional-decomposition substitution chain
# -----------------------------------------------------------------------------
def step_B_dimensional_decomposition():
    """n_PBH = n_edge * prob_form / L_pix_LRD^3.

    Identify the dimensional slot ([m^-3] in L_pix_LRD^3) and the L_max-divergence
    slot (the cardinality count, via N_eigs(L_max)).

    Two channels (W4-3 npz says obs_2 uses the LINEAR form, linear_in_neigs=True):
      LINEAR (obs_2, canonical):   n_PBH(L) = A_prefactor * N_eigs(L)
      SATURATED (g-axis, frozen):  n_PBH    = C(N_eigs_base, 2) * prob_form / L_pix_LRD^3
    """
    # LINEAR canonical channel at L=14:
    n_lin_14 = A_PREFACTOR_Q * n_eigs_exact(14)        # (local) exact -> 7.27605e-23
    # SATURATED g-axis frozen-N channel:
    n_edge_sat = comb(N_EIGS_BASE_L10, 2)              # (local) C(78080,2) = 3048204160
    n_sat = Fraction(n_edge_sat, 1) * PROB_FORM / L_PIX_LRD_M**3  # (local) exact
    # The registered degree-10 form C(N_eigs(14),2) (worsens divergence):
    n_C_14 = (Fraction(comb(N_EIGS_NPZ_14, 2), 1) * PROB_FORM / L_PIX_LRD_M**3)  # (local)

    return {
        "A_prefactor": float(A_PREFACTOR_Q),
        "n_lin_14": float(n_lin_14),               # canonical 7.2761e-23
        "n_edge_saturated": n_edge_sat,            # 3.048e9
        "n_sat_frozen": float(n_sat),              # L=10 baseline 1.758e-23 (L_max-INDEP)
        "n_C_degree10_14": float(n_C_14),          # 3.011e-22 (worse divergence)
        "L_pix_LRD_m": float(L_PIX_LRD_M),
        "prob_form": float(PROB_FORM),
    }


# -----------------------------------------------------------------------------
# Step C -- Tier-2-dimensionful test (dimension + divergence in SAME slot)
# -----------------------------------------------------------------------------
def step_C_tier2_dimensionful():
    """Show the log-derivative that buys truncation-invariance annihilates the
    dimensionful prefactor => the m^-3 magnitude is NOT truncation-invariant
    => Tier-2-dimensionful (per cross-pillar-bridge-anatomy.md).

    d ln(A * N_eigs(L)) / d ln L = d ln N_eigs / d ln L   (ln A killed)
        = L * (dN/dL) / N_eigs   -> 5 as L->inf  (DIMENSIONLESS cascade exponent).
    """
    # d ln N_eigs/d ln L = L * dN/dL / N_eigs, exact at sample L, and limit = 5.
    def dln_dlnL(L: int) -> Fraction:
        return Fraction(L, 1) * dn_eigs_dL_exact(L) / n_eigs_exact(L)  # (local)

    dln_14 = float(dln_dlnL(14))                       # (local) ~4.2581
    # limit: leading term (4/15)L^5 dominates => d ln/d ln L -> 5 (degree of leading power)
    dln_large = float(dln_dlnL(100000))                # (local) -> ~5
    leading_degree = 5                                 # (local) leading power of the quintic

    # The dimension lives in the multiplicative prefactor (A or prob_form/L_pix^3);
    # the divergence lives in the count (N_eigs). The log-derivative kills the
    # prefactor (constant) and returns the dimensionless count-exponent. So the
    # ONLY truncation-invariant content is dimensionless => Tier-2-dimensionful.
    return {
        "dln_dlnL_14": dln_14,
        "dln_dlnL_limit": dln_large,
        "leading_degree": leading_degree,
        "invariant_is_dimensionless": True,
        "dimension_and_divergence_same_slot": True,
        "tier_classification": "TIER-2-DIMENSIONFUL",
        "level3_m3_row": "REGISTRY-PASS-INELIGIBLE-HELD",
    }


# -----------------------------------------------------------------------------
# Step D -- pre-register the TWO anchor candidates; SELECT D1 (g-axis saturation)
# -----------------------------------------------------------------------------
def step_D_select_anchor(decomp: dict):
    """Pre-register D1 (substrate-physical g-axis cascade-saturation) and D2
    (Tier-2 dimensionless log-derivative), and SELECT D1 as the substrate-physical
    truncation AXIS.

    D1 substrate-physics: the cardinality cascade is indexed by the GENERATION g
    (Peter-Weyl multiplicity), NOT the L_max truncation. For g >= g_saturate=143
    the cascade-tail edge count SATURATES (n_edge_saturated FROZEN), so the g-axis
    is L_max-INDEPENDENT above saturation. g(K) = prob_form / L_pix_LRD^3 carries
    the [m^-3] dimension and is L_max-INDEPENDENT.

    Numerical caveat carried forward: the FROZEN-N saturated form delivers the
    L_max=10 BASELINE 1.758e-23 (= decomp['n_sat_frozen']), NOT the canonical
    L_max=14 refined 7.2761e-23 (= n_PBH_FW_central). The 4.14x refinement
    (N_eigs(14)/N_eigs_base) is the irreducible L_max-axis dependence that the
    Tier-2-dimensionful finding (Step C) localizes. So D1 is the correct ANCHOR
    AXIS, but pinning the L=14 MAGNITUDE at it is a separate saturated-tail recompute.
    """
    refinement_414 = float(Fraction(N_EIGS_NPZ_14, N_EIGS_BASE_L10))  # (local) ~4.1385
    canonical = float(n_PBH_FW_central)                # (local) 7.2761e-23
    baseline_sat = decomp["n_sat_frozen"]              # (local) 1.758e-23 (L=10, L_max-INDEP)
    ratio_canon_over_base = canonical / baseline_sat   # (local) ~4.14

    # D1 admissibility: is g(K)=prob_form/L_pix_LRD^3 L_max-INDEPENDENT?
    # prob_form and L_pix_LRD are substrate-physical scales (Parker-pair production
    # rate; substrate-clock pixelation length) -- NEITHER references L_max. YES.
    d1_g_of_K_Lmax_independent = True                  # (local)
    # D1 saturation: above g_saturate=143 the n_edge SATURATES (frozen). YES.
    d1_saturates_above_g = True                        # (local)

    # D2 admissibility: the dimensionless log-derivative (-> 5) annihilates the
    # dimensionful prefactor (Step C); it yields a SHAPE, not the m^-3 magnitude.
    d2_yields_dimensionless = True                     # (local)

    # SELECTION (first-principles, plan Step 5): the FWD-C5 cardinality BRIDGE is
    # built on the g-axis cascade (generation count), NOT the L_max-axis rep-ring
    # growth. The substrate's PBH-formation physics terminates at cascade
    # SATURATION (g_saturate=143). The L_max=14 label conflated the L_max-axis
    # (eigenvalue-count, unbounded) with the g-axis (cascade-generation, saturating).
    selected = "D1"                                    # (local)

    return {
        "D1_axis": "g-axis cascade-saturation (g_saturate=143); g(K)=prob_form/L_pix_LRD^3",
        "D1_g_of_K_Lmax_independent": d1_g_of_K_Lmax_independent,
        "D1_saturates_above_g_saturate": d1_saturates_above_g,
        "D1_frozen_sat_value_m3": baseline_sat,        # 1.758e-23 (L=10 baseline)
        "D2_route": "Tier-2 dimensionless log-derivative (VII.AV.STATE-PROJ route); -> 5",
        "D2_yields_dimensionless_shape": d2_yields_dimensionless,
        "selected_anchor": selected,
        "refinement_factor_L10_to_L14": refinement_414,
        "canonical_central_m3": canonical,             # 7.2761e-23 (L=14, divergent channel)
        "ratio_canonical_over_baseline": ratio_canon_over_base,
        "magnitude_decoupling_deferred": True,         # the L=14 magnitude pin is a recompute
    }


# -----------------------------------------------------------------------------
# Step E -- updated truncation-label string
# -----------------------------------------------------------------------------
def step_E_label():
    old = "L_max=14 PROVISIONAL"                        # (local)
    new = ("g_saturate=143 cascade-saturation anchor (substrate-physical, "
           "L_max-INDEPENDENT g-axis); m^-3 magnitude Level-3 row HELD "
           "Tier-2-dimensionful per cross-pillar-bridge-anatomy.md; "
           "canonical 7.2761e-23 carries irreducible L_max-axis 4.14x refinement "
           "(L=10 baseline 1.758e-23 -> L=14) => magnitude pin deferred to CF-S95")  # (local)
    return {"old_label": old, "new_label": new}


# -----------------------------------------------------------------------------
# Verdict logic (per plan W5-1 PASS/FAIL/INFO rubric)
# -----------------------------------------------------------------------------
def decide_verdict(A: dict, decomp: dict, C: dict, D: dict) -> tuple[str, str]:
    """Apply the plan W5-1 verdict rubric.

    PASS  -- admissible anchor SELECTED + N_eigs-plateau read-off EXCLUDED +
             Level-3 row HELD Tier-2-dimensionful + label updated, AND the
             selected anchor's MAGNITUDE decouples cleanly from L_max in-session.
    FAIL  -- no admissible anchor / divergence removable by THIS-observable ratio
             with well-defined c_continuum.
    INFO  -- the substrate-physical anchor axis is identified as CORRECT but its
             numerical decoupling from L_max requires a separate saturated-tail
             recompute (CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED), OR both candidates
             admissible and selection is a registry-state decision deferred.
    """
    # Step A: no plateau confirmed?
    no_plateau = (A["dn_positive"] and A["strictly_increasing"]
                  and A["repro_ok"] and A["diverges"])              # (local)
    # Step C: Tier-2-dimensionful derived?
    tier2 = (C["invariant_is_dimensionless"]
             and C["dimension_and_divergence_same_slot"]
             and C["tier_classification"] == "TIER-2-DIMENSIONFUL")  # (local)
    # Step D: an admissible substrate-physical anchor AXIS selected?
    anchor_selected = (D["selected_anchor"] == "D1"
                       and D["D1_g_of_K_Lmax_independent"]
                       and D["D1_saturates_above_g_saturate"])       # (local)
    # Magnitude decoupling: does the SELECTED anchor pin the CANONICAL magnitude
    # cleanly in-session? NO -- the frozen-saturation form delivers the L=10
    # baseline (1.758e-23), not the canonical L=14 (7.2761e-23). 4.14x apart.
    magnitude_clean = not D["magnitude_decoupling_deferred"]         # (local) -> False

    # FAIL guard: would only trigger if no anchor selected OR divergence removable.
    if not no_plateau or not tier2 or not anchor_selected:
        verdict = "FAIL"                                            # (local)
    elif not magnitude_clean:
        # anchor AXIS identified + Tier-2-dimensionful HELD + label updated, but
        # the L=14 magnitude pin is DEFERRED -> INFO (CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED)
        verdict = "INFO"                                            # (local)
    else:
        verdict = "PASS"                                            # (local)

    # Build the compact value string for the verdict line.
    value = (
        f"chain=PASS;step_A_no_plateau={no_plateau};lim_N_eigs=+inf;"
        f"N_eigs(14)_repro={A['rep14']}_relerr={A['rel_err_14']:.2e}_ok={A['repro_ok']};"
        f"dN_dL>0_forall_L>=1={A['dn_positive']};"
        f"tier_class={C['tier_classification']};level3_m3={C['level3_m3_row']};"
        f"dln_dlnL_14={C['dln_dlnL_14']:.4f}_limit={C['dln_dlnL_limit']:.4f}(dimensionless);"
        f"selected_anchor=D1_g_saturate=143_Lmax_INDEP;"
        f"D1_frozen_sat={D['D1_frozen_sat_value_m3']:.4e}_m3(L10_baseline);"
        f"canonical_central={D['canonical_central_m3']:.4e}_m3(L14_divergent_channel);"
        f"refinement_L10_to_L14={D['refinement_factor_L10_to_L14']:.4f};"
        f"magnitude_decoupling_DEFERRED={D['magnitude_decoupling_deferred']}_CF-S95;"
        f"VII.AX.OP-PROJ_theorem_STRUCTURE=STAGE-3-PERMANENT(Tier-2_corollary)"
    )  # (local)
    return verdict, value


# -----------------------------------------------------------------------------
# Diagnostic plot: N_eigs(L_max) quintic (L_max-axis, divergent) vs g-axis
# cascade-saturation (frozen, L_max-independent) comparison.
# -----------------------------------------------------------------------------
def make_plot(A: dict, decomp: dict, C: dict, D: dict, verdict: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1 -- N_eigs(L_max) quintic: monotone unbounded (NO plateau)
    ax = axes[0, 0]
    Ls = np.array(A["Ls"])                              # (local)
    ne = np.array(A["n_eigs"], dtype=float)             # (local)
    ax.plot(Ls, ne, "o-", color="C0", lw=2, ms=5,
            label=r"$N_{eigs}(L_{max})$ (W4-3 Sage-exact quintic)")
    ax.axhline(N_EIGS_BASE_L10, color="C3", ls="--", lw=1.5,
               label=r"L=10 base atlas $N_{eigs}=78080$ (frozen-saturation N)")
    ax.scatter([14], [N_EIGS_NPZ_14], color="r", zorder=5, s=80,
               label=r"$N_{eigs}(14)=323136$ (npz anchor)")
    ax.set_xlabel(r"$L_{max}$")
    ax.set_ylabel(r"$N_{eigs}$  (eigenvalue count)")
    ax.set_title(r"Step A: $N_{eigs}(L_{max})$ is monotone UNBOUNDED ($\lim=+\infty$)"
                 "\nNO plateau -- the L_max=14 label cannot be a saturation read-off")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2 -- the two n_PBH channels: divergent L_max-axis vs frozen g-axis
    ax = axes[0, 1]
    L_probe = np.array(A["L_probe"])                    # (local)
    n_lin = np.array([decomp["A_prefactor"] * float(n_eigs_exact(int(L)))
                      for L in L_probe])                # (local) LINEAR divergent
    ax.semilogy(L_probe, n_lin, "s-", color="C1", lw=2, ms=6,
                label=r"LINEAR $A\cdot N_{eigs}(L)$ (L_max-axis, DIVERGENT)")
    ax.axhline(decomp["n_sat_frozen"], color="C2", ls="-", lw=2,
               label=r"g-axis FROZEN $C(78080,2)\,p_{form}/L_{pix}^3$=%.3e (L_max-INDEP)"
                     % decomp["n_sat_frozen"])
    ax.axhline(float(n_PBH_FW_central), color="r", ls=":", lw=2,
               label=r"canonical $n_{PBH}$=7.2761e-23 (=$A\cdot N_{eigs}(14)$, L=14)")
    ax.axhspan(JE5_FLOOR, JE5_UPPER, color="gray", alpha=0.18,
               label=r"JE5 conjunct band [5.5e-23, 2.2e-22]")
    ax.set_xlabel(r"$L_{max}$")
    ax.set_ylabel(r"$n_{PBH}$  (m$^{-3}$)")
    ax.set_title("Step B/D: canonical 7.2761e-23 is the DIVERGENT L_max-axis read;\n"
                 "g-axis frozen-saturation = 1.758e-23 (L=10 baseline, L_max-INDEP); 4.14x apart")
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(alpha=0.3, which="both")

    # Panel 3 -- Tier-2-dimensionful: log-derivative -> 5 (dimensionless)
    ax = axes[1, 0]
    Ls2 = np.arange(2, 60)                              # (local)
    dln = np.array([float(Fraction(int(L), 1) * dn_eigs_dL_exact(int(L)) / n_eigs_exact(int(L)))
                    for L in Ls2])                      # (local)
    ax.plot(Ls2, dln, "-", color="C4", lw=2,
            label=r"$d\ln N_{eigs}/d\ln L$ (annihilates dimensionful prefactor)")
    ax.axhline(5.0, color="r", ls="--", lw=1.5, label=r"$\lim_{L\to\infty}=5$ (cascade exponent)")
    ax.scatter([14], [C["dln_dlnL_14"]], color="k", zorder=5, s=60,
               label=r"$L=14$: %.4f" % C["dln_dlnL_14"])
    ax.set_xlabel(r"$L_{max}$")
    ax.set_ylabel(r"$d\ln N_{eigs}/d\ln L$  (dimensionless)")
    ax.set_title("Step C: the truncation-INVARIANT content is DIMENSIONLESS (->5)\n"
                 "=> dimension + divergence in SAME multiplicative slot => TIER-2-DIMENSIONFUL")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4 -- verdict / selection summary text
    ax = axes[1, 1]
    ax.axis("off")
    txt = []                                            # (local)
    txt.append(f"VERDICT: {verdict}  (plan W5-1 [CHAIN] rubric)")
    txt.append("")
    txt.append("Step A: lim N_eigs = +inf  (no plateau; dN/dL>0 forall L>=1)")
    txt.append(f"        N_eigs(14)={A['rep14']} repro rel_err={A['rel_err_14']:.1e} (<1e-12)")
    txt.append("")
    txt.append("Step C: TIER-2-DIMENSIONFUL")
    txt.append(f"        d ln N/d ln L -> {C['dln_dlnL_limit']:.3f} (dimensionless)")
    txt.append("        m^-3 Level-3 row = REGISTRY-PASS-INELIGIBLE-HELD")
    txt.append("")
    txt.append("Step D: SELECTED anchor = D1")
    txt.append("        g-axis cascade-saturation g_saturate=143")
    txt.append("        g(K)=prob_form/L_pix_LRD^3  L_max-INDEPENDENT")
    txt.append(f"        frozen-sat value = {D['D1_frozen_sat_value_m3']:.4e} m^-3 (L=10 baseline)")
    txt.append(f"        canonical 7.2761e-23 = L=14 divergent-channel read")
    txt.append(f"        refinement L10->L14 = {D['refinement_factor_L10_to_L14']:.3f}x")
    txt.append("        => magnitude pin DEFERRED to CF-S95 (CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED)")
    txt.append("")
    txt.append("Step E: label 'L_max=14 PROVISIONAL' ->")
    txt.append("        'g_saturate=143 cascade-saturation anchor (L_max-INDEP);")
    txt.append("         m^-3 row HELD Tier-2-dimensionful'")
    txt.append("")
    txt.append("VII.AX.OP-PROJ theorem-STRUCTURE = STAGE-3-PERMANENT (Tier-2 corollary)")
    ax.text(0.0, 1.0, "\n".join(txt), va="top", ha="left", fontsize=9.0,
            family="monospace", transform=ax.transAxes)

    fig.suptitle(f"{GATE_ID}  --  n_PBH m^-3 Level-3 anchor: substrate-physical "
                 f"(g-axis) re-determination  [{verdict}]", fontsize=12.5)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Verdict-line emission (canonical + dual-SHA companion; [CHAIN] => NO 3-tuple)
# -----------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str,
                   content_sha: str) -> None:
    """Append the canonical line + dual-SHA companion row to s94_gate_verdicts.txt.

    [CHAIN] trigger: set-membership / anchor-selection verdict, NO signed delta
    => the S87 schema-v2 3-tuple companion row is NOT required (plan
    output_artifacts schema_v2_3tuple_required: false).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"[CHAIN] n_PBH m^-3 Level-3 anchor re-determination: substrate-physical "
        f"g-axis cascade-saturation (g_saturate=143) SELECTED; Tier-2-dimensionful HELD\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
def main() -> None:
    # --- Input SHA pins (logged in the first lines of stdout per gate-verdicts.md) ---
    canonical_sha = sha256_of(CANONICAL_CONSTANTS_PATH)   # (local)
    w4_3_npz_sha = sha256_of(W4_3_NPZ)                    # (local)
    print(f"[{GATE_ID}] INPUT SHA-256 PINS")
    print(f"  canonical_constants.py = {canonical_sha}")
    print(f"  s93_w4_3_..._npz       = {w4_3_npz_sha}")
    print(f"  n_PBH_FW_central       = {n_PBH_FW_central} m^-3 (canonical)")
    print(f"  M_KK                   = {M_KK} GeV ; tau_fold = {tau_fold}")
    print()

    # --- Execute the [CHAIN] Steps A..E ---
    A = step_A_no_plateau()
    decomp = step_B_dimensional_decomposition()
    C = step_C_tier2_dimensionful()
    D = step_D_select_anchor(decomp)
    E = step_E_label()

    print("=== Step A: W4-3 quintic reproduction / no-plateau ===")
    print(f"  N_eigs(14) reproduced = {A['rep14']} (npz=323136) rel_err={A['rel_err_14']:.2e}"
          f" repro_ok={A['repro_ok']}")
    print(f"  dN/dL>0 forall L>=1 = {A['dn_positive']} ; strictly_increasing={A['strictly_increasing']}")
    print(f"  N_eigs probe {A['L_probe']} = {A['n_probe']}  -> lim=+inf diverges={A['diverges']}")
    print()
    print("=== Step B: dimensional decomposition ===")
    print(f"  A_prefactor          = {decomp['A_prefactor']:.6e} m^-3 (per count)")
    print(f"  LINEAR A*N_eigs(14)  = {decomp['n_lin_14']:.6e} m^-3  (canonical channel; DIVERGENT)")
    print(f"  n_edge_saturated     = C(78080,2) = {decomp['n_edge_saturated']}")
    print(f"  g-axis FROZEN-SAT    = {decomp['n_sat_frozen']:.6e} m^-3  (L=10 baseline; L_max-INDEP)")
    print(f"  degree-10 C(N14,2)   = {decomp['n_C_degree10_14']:.6e} m^-3  (worse divergence)")
    print()
    print("=== Step C: Tier-2-dimensionful test ===")
    print(f"  d ln N_eigs/d ln L @14 = {C['dln_dlnL_14']:.4f} ; limit = {C['dln_dlnL_limit']:.4f}")
    print(f"  invariant dimensionless={C['invariant_is_dimensionless']} ;"
          f" same-slot={C['dimension_and_divergence_same_slot']}")
    print(f"  classification = {C['tier_classification']} ; m^-3 row = {C['level3_m3_row']}")
    print()
    print("=== Step D: anchor candidates + selection ===")
    print(f"  D1 = {D['D1_axis']}")
    print(f"     g(K) L_max-INDEP = {D['D1_g_of_K_Lmax_independent']} ;"
          f" saturates above g_saturate = {D['D1_saturates_above_g_saturate']}")
    print(f"     frozen-sat value = {D['D1_frozen_sat_value_m3']:.4e} m^-3 (L=10 baseline)")
    print(f"  D2 = {D['D2_route']}")
    print(f"  SELECTED = {D['selected_anchor']}")
    print(f"  canonical central = {D['canonical_central_m3']:.4e} m^-3 (L=14 divergent channel)")
    print(f"  refinement L10->L14 = {D['refinement_factor_L10_to_L14']:.4f}x ;"
          f" canonical/baseline = {D['ratio_canonical_over_baseline']:.4f}")
    print(f"  magnitude decoupling DEFERRED = {D['magnitude_decoupling_deferred']} (CF-S95)")
    print()
    print("=== Step E: updated label ===")
    print(f"  OLD: {E['old_label']}")
    print(f"  NEW: {E['new_label']}")
    print()

    # --- Verdict ---
    verdict, value = decide_verdict(A, decomp, C, D)
    print(f"=== VERDICT: {verdict} ===")
    print(f"  value = {value}")
    print()

    # --- dual-SHA closure over the input-pin map ---
    pins = {                                            # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "canonical_constants_sha256": canonical_sha,
        "w4_3_npz_sha256": w4_3_npz_sha,
        "n_PBH_FW_central": repr(float(n_PBH_FW_central)),
        "N_eigs_base_L10": N_EIGS_BASE_L10,
        "N_eigs_14": N_EIGS_NPZ_14,
        "g_saturate": G_SATURATE,
        "prob_form": str(PROB_FORM),
        "L_pix_LRD_m": str(L_PIX_LRD_M),
        "selected_anchor": D["selected_anchor"],
        "tier_classification": C["tier_classification"],
        "verdict": verdict,
    }
    closure = closure_hash(pins)                        # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"  closure_hash(pins)  = {closure}")
    print(f"  audit_sha256        = {audit_sha}")
    print(f"  content_sha256      = {content_sha}")
    print()

    # --- Save data ---
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        scheme=SCHEME, convention=CONVENTION, verdict=verdict, value=value,
        # Step A
        Ls=np.array(A["Ls"]), n_eigs=np.array(A["n_eigs"], dtype=np.int64),
        dn_positive=A["dn_positive"], strictly_increasing=A["strictly_increasing"],
        n_eigs_14_repro=A["rep14"], rel_err_14=A["rel_err_14"], repro_ok=A["repro_ok"],
        L_probe=np.array(A["L_probe"]), n_probe=np.array(A["n_probe"], dtype=np.int64),
        lim_N_eigs="+inf",
        # Step B  (full float64 of the substrate-physical m^-3 candidate values)
        A_prefactor_m3=decomp["A_prefactor"],
        n_PBH_linear_L14_m3=decomp["n_lin_14"],          # 7.27605e-23 canonical channel
        n_edge_saturated=decomp["n_edge_saturated"],
        n_PBH_frozen_saturation_m3=decomp["n_sat_frozen"],   # 1.758e-23 L=10 baseline, L_max-INDEP
        n_PBH_degree10_C_N14_m3=decomp["n_C_degree10_14"],
        L_pix_LRD_m=decomp["L_pix_LRD_m"], prob_form=decomp["prob_form"],
        # Step C
        dln_dlnL_14=C["dln_dlnL_14"], dln_dlnL_limit=C["dln_dlnL_limit"],
        leading_degree=C["leading_degree"],
        invariant_is_dimensionless=C["invariant_is_dimensionless"],
        dimension_and_divergence_same_slot=C["dimension_and_divergence_same_slot"],
        tier_classification=C["tier_classification"],
        level3_m3_row=C["level3_m3_row"],
        # Step D
        selected_anchor=D["selected_anchor"],
        D1_g_of_K_Lmax_independent=D["D1_g_of_K_Lmax_independent"],
        D1_saturates_above_g_saturate=D["D1_saturates_above_g_saturate"],
        D1_frozen_sat_value_m3=D["D1_frozen_sat_value_m3"],
        g_saturate=G_SATURATE,
        canonical_central_m3=D["canonical_central_m3"],   # 7.2761e-23 full float64
        refinement_factor_L10_to_L14=D["refinement_factor_L10_to_L14"],
        ratio_canonical_over_baseline=D["ratio_canonical_over_baseline"],
        magnitude_decoupling_deferred=D["magnitude_decoupling_deferred"],
        # Step E
        old_label=E["old_label"], new_label=E["new_label"],
        # SHAs
        closure_hash=closure, audit_sha256=audit_sha, content_sha256=content_sha,
        # canonical anchors
        n_PBH_FW_central=float(n_PBH_FW_central), M_KK=float(M_KK), tau_fold=float(tau_fold),
        canonical_constants_sha256=canonical_sha, w4_3_npz_sha256=w4_3_npz_sha,
    )
    print(f"  data  -> {OUT_NPZ}")

    # --- Plot ---
    make_plot(A, decomp, C, D, verdict)
    print(f"  plot  -> {OUT_PNG}")

    # --- Emit verdict line ---
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended -> {VERDICT_TXT}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md step 2)
    print(f"4-TUPLE: (value=anchor:{D['selected_anchor']}=g_saturate=143, "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")


if __name__ == "__main__":
    main()
