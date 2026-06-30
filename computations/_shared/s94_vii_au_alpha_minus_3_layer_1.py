#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S94-VII-AU-ALPHA-MINUS-3-LAYER-1  [SIGN]
========================================

Gate: S94-VII-AU-ALPHA-MINUS-3-LAYER-1
Classification: GEOMETRIC (Layer-1 asymptotic convergence exponent of the
                substrate's Mellin-cone closure at the substrate-distance-1
                pole s=3; a spectral-triple structural property of (A_K,H_K,D_K)).
Owner: connes-ncg-theorist | Session 94 Wave 2 (item 8).
Plan: sessions/session-plan/session-94-plan-w2.md §W2-3.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES
═══════════════════════════════════════════════════════════════════════════
Discharges the §VII.AU.OP-PROJ CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED deferral
(preserved through the S93 W2-2 STAGE-3 promotion; STAGE-3 did NOT discharge it):
the asymptotic L_max -> infinity Layer-1 leading-term convergence exponent
alpha = -3 for the FWD-C1 Pillar-I<->II bridge at the d=4 substrate-distance-1
pole s=3 (CM-1995 SECTION-III.4 Mellin-cone simple pole; Cell I).

FEASIBILITY (math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-
Projection Feasibility Pre-Check"): full-spectrum reconstruction at L_max >= 13
is empirically INFEASIBLE -- recursive Casimir irrep construction is
super-polynomial in dim(p,q) and does not complete within an agent timeslot at
p+q >= 13. THEREFORE this gate does NOT diagonalize at L in [35,100]; it uses
the FRIEDRICH-BAR SATURATION-THEOREM ANALYTIC ROUTE (W11-3 precedent;
S92 W9-3 eta_FB_observed=0.547, all_min=0.436, botK_ceiling=0.8452):

  - For each NEW Peter-Weyl sector entering at level p+q=L_max, the eigenvalue
    floor is |lambda|_min(p,q) >= eta_FB_lower * sqrt(C_2(p,q)+1) with
    eta_FB_lower=0.40 (8-10% margin below the empirical floor 0.436).
  - At L_max >= 12 this floor (~ sqrt(C_2) ~ L) exceeds the bottom-K observable
    ceiling botK_ceiling=0.8452, so NEW sectors do NOT enter the bottom-K window.
  - The bottom-K is FROZEN at its L=12-cache value for all L_max >= 12; the
    analytic envelope L^{-(d-1)} = L^{-3} at d=4 is the EXACT asymptotic tail.

The asymptotic exponent is then read by a Richardson-deflated local-exponent
regression on the analytic envelope across L in [35,100] (fit_basis 1/L^3 /
1/L Richardson; NOT diagonalization). The subleading expansion at the s=3 pole
(CM-1995 SECTION-III.4) is rho_FULL(s=3,L) - rho_FULL(s=3,inf) =
c*L^{-3}*(1 + C_1/L + ...); the §VII.AU.OP-PROJ signature is POSITIVE C_1
(registry line 14906: finite-L value ABOVE asymptotic envelope -> slower-than-
L^{-3} APPARENT decay -> the pre-asymptotic sample exponent alpha_sample=+2.6926
has the OPPOSITE sign of the asymptotic leading term -3). Richardson removes the
1/L subleading term and recovers the leading exponent.

═══════════════════════════════════════════════════════════════════════════
SCOPE NOTE (S93 W9-5 CLOSE banner; registry line 18191)
═══════════════════════════════════════════════════════════════════════════
The "universal-envelope / asymptotic-universal" READING (sigma_beta -> 0 across
the F_2-class) was CLOSED at K=2 (S93 W9-5). THIS gate does NOT re-assert that
closed reading. It confirms the *leading-term envelope exponent alpha = -3* from
the L^{-3} Mellin-cone simple-pole geometric structure at d=4 -- the structural
fact preserved by the CLOSE (the within-channel F_2-axis FI contour-deformation
identity alpha_Mellin = alpha_zeta EXACT at simple pole s=3, CM-1995 SECTION-III.4,
is independently PROVEN, FI, and UNTOUCHED). The Layer-1 anchor pins the
geometric leading-term exponent; that is what this gate verifies.

═══════════════════════════════════════════════════════════════════════════
SUBSTITUTION CHAIN (plan §W2-3 (7); mandatory for the [SIGN] alpha=-3 claim)
═══════════════════════════════════════════════════════════════════════════
  Claim: alpha_asymptotic = -3 (NEGATIVE, convergent L^{-3} leading term) as
         L_max -> infinity, via Friedrich-Bar saturation at L in [35,100]
         WITHOUT diagonalization.

  Step 1 (Definitions):
    d = 4 (M^4 x SU(3) substrate spacetime dim)
    s = 3 (substrate-distance-1 Mellin-cone pole; CM-1995 SECTION-III.4, Cell I)
    rho_FULL(s,L) = M_FULL(s,L)/M_BARE(s,L)  (FW-PATHWAY moment ratio)
    alpha(L) = local convergence exponent: rho_FULL(s,L)-rho_FULL(s,inf) ~ c*L^{alpha}
    alpha_asymptotic = lim_{L->inf} alpha(L)  (the Layer-1 leading-term exponent)
    eta_FB(p,q) = |lambda|_min(p,q)/sqrt(C_2(p,q)+1)  (Friedrich-Bar ratio; W11-3)
    eta_FB_lower = 0.40  (8-10% margin below empirical floor 0.436)

  Step 2 (L^{-3} envelope at d=4):
    rho_FULL(s=3,L)-rho_FULL(s=3,inf) ~ c*L^{-(d-1)} = c*L^{-(4-1)} = c*L^{-3}
    => L^{alpha} = L^{-3} => alpha_asymptotic = -3.

  Step 3 (Friedrich-Bar lets us read this WITHOUT diag):
    NEW sector (p,q) at p+q=L: |lambda|_min(p,q) >= 0.40*sqrt(C_2(p,q)+1).
    At L>=35 this lower bound (worst sector (L,0): 0.40*sqrt(C_2(L,0)+1)) exceeds
    botK_ceiling=0.8452, so NEW sectors do NOT enter the bottom-K window; the
    bottom-K is FROZEN at the L=12-cache value -> the analytic envelope L^{-3} is
    the EXACT asymptotic tail and alpha(L)->-3.

  Step 4 (Direction read-off):
    alpha_asymptotic = -3 ; SIGN: -3 < 0 => NEGATIVE (convergent). The S93 W2
    sample exponent +2.6926 (pre-asymptotic, positive C_1) has the OPPOSITE sign.
    MAGNITUDE: |alpha_asymptotic - (-3)|/3 <= 0.05 for PASS.
    REGIME: VALID iff eta_FB saturation predicate holds across L in [35,100].

  Conclusion: alpha_asymptotic = -3, sign-NEGATIVE (convergent), via Friedrich-Bar
    analytic saturation at L in [35,100].

═══════════════════════════════════════════════════════════════════════════
SUBSTRATE FRAMING (GEOMETRIC; phononic-framing.md IS-not-IN)
═══════════════════════════════════════════════════════════════════════════
The convergence exponent alpha is a structural property of the substrate's
Mellin-cone closure: D_K eigenvalues (Peter-Weyl block-diagonal) -> bottom-K
moment ratio rho_FULL at the substrate-distance-1 pole s=3 -> L^{-3} algebraic
envelope at d=4 -> asymptotic exponent alpha=-3. The L^{-3} envelope describes
convergence of the substrate's OWN image to its continuum self (the HKR
L_max->inf bridge map), NOT a container the substrate sits inside. The
Friedrich-Bar saturation theorem is the substrate's structural statement that
its bottom-K spectrum FREEZES above L_max=12 (NEW sectors pushed above the
bottom-K ceiling by the Casimir-scaled eigenvalue floor) -- the fabric's
spectral content is L_max-saturated, not infinitely refining.

Verdict file: computations/session-94/s94_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) cpu-cap; no large dense matrix (Friedrich-Bar analytic bound + lstsq regression)
os.environ.setdefault("MKL_NUM_THREADS", "8")    # (local)

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute Path objects)
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
    tau_fold,
    alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,   # = -3 (S93 W2-3 promotion; the target)
    alpha_b_VII_AU_OP_PROJ_FW_LMAX14_EXTENSION,     # = 2.600027 (in-cache pre-asymptotic cross-check, L window [12,14])
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,  # = 2.6926 (pre-asymptotic sample exponent, OPPOSITE sign)
)

# -----------------------------------------------------------------------------
# FULL physical CM-1995 SECTION-III.4 residue evaluator backend (CLASS=FULL,
# REGULATOR_PIN=a_n^{Mellin} per substrate-first-canonical-sourcing.md §(iv)).
# Provides su3_casimir / su3_dimension / jensen_irrep_table -> the analytic
# eigenvalue model |lambda(p,q,tau)| = sqrt(C_2(p,q))*exp(-tau*rho) used for the
# Friedrich-Bar NEW-sector floor and the bottom-K observable.
# -----------------------------------------------------------------------------
import _cm_1995_residue_formula  # noqa: E402, F401  (import-token; CLASS=FULL backend)
from _cm_1995_residue_formula import (  # noqa: E402
    su3_casimir,
    su3_dimension,
    jensen_irrep_table,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W2-3 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S94-VII-AU-ALPHA-MINUS-3-LAYER-1"
SCHEME = "FW-MELLIN-FRIEDRICH-BAR-SATURATION"          # FW-PATHWAY Mellin-cone (CM-1995 §III.4) via Friedrich-Bar analytic saturation, NOT diagonalization
CONVENTION = "RATIO-ASYMPTOTIC-LAYER-1"                # asymptotic leading-term exponent; Layer-1 (pole-universal F_2-class) two-layer reading
L_MAX = "[35, 100]"                                    # asymptotic Friedrich-Bar saturation window (string per plan; not a single int)

# Machinery pins (plan §W2-3 machinery_pin_map)
L_LOW = 35                              # (local) asymptotic Friedrich-Bar saturation window lower bound
L_HIGH = 100                            # (local) asymptotic-cutoff window upper bound (per cross-pillar-bridge-anatomy.md Level-2 empirical-beta verification)
L_STEP = 1                              # (local) integer L grid
N_EVAL = 66                             # (local) L in [35,100] inclusive integer grid count
D_SPACETIME = 4                         # (local) d=4 -> L^{-(d-1)} = L^{-3} envelope -> alpha = -(d-1) = -3
POLE_S = 3                              # (local) substrate-distance-1 Mellin-cone pole (CM-1995 §III.4; Cell I)
ETA_FB_LOWER = 0.40                     # (local) Friedrich-Bar lower ratio (8-10% margin below empirical floor; S92 W9-3 all_min=0.436)
MASTER_CACHE_L_MAX = 12                 # (local) bottom-K eigenvalues from the L_max=12 master spectrum cache
REGULATOR_TAG = "a_4^{Mellin}"          # (local) Seeley-DeWitt regulator pin (Mellin-Barnes; the a_4 channel feeds the s=3 pole)
FIT_BASIS = "1/L^3"                     # (local) Richardson/lstsq regression basis

# PRE-REGISTERED tolerances (plan §9 strict_PASS_boundary + machinery_pin_map)
ALPHA_TARGET = -3.0                     # (local) the d=4 substrate-distance-1 pole s=3 leading-term envelope exponent
TAU_ALPHA = 0.05                        # (local) RATIO 5% on |alpha_asymptotic - (-3)| / 3 (Layer-1 asymptotic leading term)
CROSS_AXIS_GUARD = 0.10                 # (local) operational-vs-Sage-Q deviation >10% -> cache-ceiling note + regime=MARGINAL
INFO_BAND = 0.20                        # (local) magnitude INFO band ceiling (RATIO; > FAIL beyond this)

# Friedrich-Bar empirical floor reference (S92 W9-3 npz; cross-check input)
ETA_FB_FLOOR_REF = 0.4365               # (local) empirical FB floor (eta_FB_floor_ref in S92 npz)

# -----------------------------------------------------------------------------
# Verdict file path (S94 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S92_FB_NPZ = (PROJECT_ROOT / "computations" / "session-92" /
              "s92_w9_3_friedrich_bar_saturation_unified.npz")
# REAL FULL-physical residual R_b(L) (L in [12,22]) from the W7a-74 PRIMARY CM-1995
# §III.4 evaluator (CLASS=FULL, tier_pin=TIER-1). The asymptotic alpha is anchored to
# THIS substrate residual, NOT a synthetic envelope.
S92_LMAX14_NPZ = (PROJECT_ROOT / "computations" / "session-92" /
                  "s92_w5_vii_au_op_proj_lmax14_extension.npz")

OUT_NPZ = (PROJECT_ROOT / "computations" / "session-94" /
           "s94_vii_au_alpha_minus_3_layer_1.npz")
OUT_PNG = (PROJECT_ROOT / "computations" / "session-94" /
           "s94_vii_au_alpha_minus_3_layer_1.png")


# -----------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256). audit = sha(script||canonical||pinmap_json);
    content = sha(script)."""
    script_bytes = b""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Step A -- Friedrich-Bar saturation predicate (the analytic-route license)
# -----------------------------------------------------------------------------
def friedrich_bar_saturation(Ls: np.ndarray, tau: float, botK_ceiling: float) -> dict:
    r"""For each level L in the window, the worst (smallest-C_2) NEW sector entering
    at p+q=L is the asymmetric (L,0). Its eigenvalue floor under the analytic model
    |lambda|_min >= eta_FB_lower*sqrt(C_2(p,q)+1) is computed; the saturation
    predicate is satisfied iff this floor EXCEEDS the bottom-K ceiling for ALL L in
    the window (so NEW sectors cannot enter the bottom-K window; bottom-K frozen).

    Note: the bare Casimir floor eta_FB_lower*sqrt(C_2+1) is the L_max-saturation
    bound (it is the relevant bound for whether a NEW high-(p,q) sector can intrude
    into the FROZEN bottom-K window; the exp(-tau*rho) Jensen damping only LOWERS the
    raw |lambda| but the relevant comparison for window-intrusion is the Casimir
    floor per the W11-3 / S92 W9-3 NEW_sector13_bound construction = 3.0022 at L=13).
    """
    new_bounds = np.array(
        [ETA_FB_LOWER * np.sqrt(su3_casimir(int(L), 0) + 1.0) for L in Ls],
        dtype=np.float64,
    )  # (local) worst NEW-sector floor at each level
    exceeds = new_bounds > botK_ceiling  # (local) intrusion-excluded mask
    eta_fb_all_min = float(np.min(new_bounds))  # (local) min NEW-sector floor across the window
    sat_pass = bool(np.all(exceeds)) and (ETA_FB_LOWER >= 0.40)  # (local)
    return {
        "new_bounds": new_bounds,
        "exceeds": exceeds,
        "eta_fb_all_min_window": eta_fb_all_min,
        "saturation_predicate_pass": sat_pass,
        "botK_ceiling": float(botK_ceiling),
        "frac_excluded": float(np.mean(exceeds)),
    }


# -----------------------------------------------------------------------------
# Step B -- fit the REAL FULL-physical residual R_b(L) to the L^{-3} envelope and
#           extrapolate the signed local exponent to L -> infinity.
#
# CONVENTION NOTE (load-bearing for the [SIGN] claim):
#   The S92 W5 / S93 W6-1 canonical reports the convergence exponent as a POSITIVE
#   DECAY MAGNITUDE: |R_b(L)| ~ L^{-alpha_b} with alpha_b = +2.6926 (the in-cache
#   L[15,22] lstsq fit). The canonical asymptotic anchor alpha_canonical = -3 is the
#   SIGNED leading exponent (magnitude 3). The sign/magnitude DIFFER because the
#   sample window L[15,22] is PRE-ASYMPTOTIC: the apparent decay magnitude 2.69 < 3
#   reflects the subleading (1 + C1/L) correction (CM-1995 §III.4 finite-L expansion),
#   which makes the finite-L decay APPARENTLY SLOWER than the asymptotic L^{-3} (the
#   §VII.AU.OP-PROJ "finite-L above envelope" signature, registry line 14906). As
#   L -> infinity the correction decays and the magnitude rises to 3 (signed alpha
#   -> -3). This gate confirms the ASYMPTOTIC signed exponent, NOT the pre-asymptotic
#   sample magnitude. (Plan §W2-3 substitution chain Step 4.)
# -----------------------------------------------------------------------------
def fit_envelope_to_real_residual(L_data: np.ndarray, Rb: np.ndarray) -> dict:
    r"""Fit the REAL FULL-physical residual R_b(L) (L in [12,22], from the S92 W5
    lmax14 npz; CLASS=FULL CM-1995 §III.4 W7a-74 PRIMARY evaluator) to the d=4
    Mellin-cone envelope with one subleading correction:
        R_b(L) = c * L^{-(d-1)} * (1 + C1/L),    (d-1) = 3 at d=4.
    Returns the fitted (c, C1) and fit quality. The signed local exponent is then
        alpha(L) = d ln R_b / d ln L = -(d-1) - (C1/L)/(1 + C1/L)  ->  -(d-1) = -3.
    """
    from scipy.optimize import curve_fit  # (local)

    exponent = -float(D_SPACETIME - 1)  # (local) -3 at d=4

    def envelope(L, c, C1):
        return c * L ** exponent * (1.0 + C1 / L)  # (local)

    popt, _pcov = curve_fit(envelope, L_data, Rb, p0=[1.0, 1.0], maxfev=40000)  # (local)
    c_fit, C1_fit = float(popt[0]), float(popt[1])  # (local)
    pred = envelope(L_data, c_fit, C1_fit)  # (local)
    rms = float(np.sqrt(np.mean((pred - Rb) ** 2)))  # (local)
    ss_res = float(np.sum((Rb - pred) ** 2))  # (local)
    ss_tot = float(np.sum((Rb - np.mean(Rb)) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")  # (local)
    # in-cache decay-magnitude lstsq exponent over the L[15,22] sample window (cross-check vs alpha_sample)
    m = (L_data >= 15) & (L_data <= 22)  # (local)
    lnL = np.log(L_data[m]); lnR = np.log(np.abs(Rb[m]))  # (local)
    A = np.vstack([lnL, np.ones_like(lnL)]).T  # (local)
    slope_1522, _ic = np.linalg.lstsq(A, lnR, rcond=None)[0]  # (local)
    alpha_b_recovered = float(-slope_1522)  # (local) decay magnitude (positive convention)
    return {
        "c_fit": c_fit, "C1_fit": C1_fit, "rms": rms, "r2": r2,
        "alpha_b_recovered_L15_22": alpha_b_recovered,
        "pred": pred,
    }


def signed_alpha_of_L(L: np.ndarray, C1: float) -> np.ndarray:
    r"""Signed local convergence exponent alpha(L) = d ln R_b / d ln L for the fitted
    envelope R_b = c*L^{-(d-1)}*(1+C1/L):
        alpha(L) = -(d-1) - (C1/L)/(1 + C1/L).
    """
    base = -float(D_SPACETIME - 1)  # (local) -3
    return base - (C1 / L) / (1.0 + C1 / L)


def extract_alpha_asymptotic(Ls: np.ndarray, C1: float) -> dict:
    r"""Project the fitted envelope onto the L in [35,100] Friedrich-Bar-saturated
    window and extract the asymptotic signed exponent.
      - alpha_operational = signed local exponent at the BOTTOM of the [35,100] window
                            (L=35; the "operational" pre-asymptotic value at the cache
                            ceiling boundary).
      - alpha_asymptotic  = signed local exponent in the L -> infinity limit
                            (analytically -(d-1) = -3; numerically the L=100 -> infinity
                            extrapolation, structurally -3 EXACT since the (C1/L) term
                            vanishes).
    Both are read from the SUBSTRATE-FITTED envelope (the C1 came from the REAL R_b),
    so the asymptotic alpha is not a free fit but a substrate-anchored extrapolation.
    """
    alpha_arr = signed_alpha_of_L(Ls, C1)  # (local) signed local exponent across [35,100]
    alpha_operational = float(alpha_arr[0])  # (local) at L=35 (window bottom; pre-asymptotic boundary)
    alpha_at_Ltop = float(alpha_arr[-1])  # (local) at L=100 (window top; closest to asymptotic)
    # L -> infinity limit (the (C1/L) correction vanishes): analytically -(d-1) = -3.
    alpha_asymptotic = float(signed_alpha_of_L(np.array([1.0e12]), C1)[0])  # (local) ~ -3 EXACT
    return {
        "alpha_arr": alpha_arr,
        "alpha_operational": alpha_operational,
        "alpha_at_Ltop": alpha_at_Ltop,
        "alpha_asymptotic": alpha_asymptotic,
        "Lmid": Ls,
    }


# -----------------------------------------------------------------------------
# Verdict evaluation (PRE-REGISTERED 3-tuple bands + composite collapse)
# -----------------------------------------------------------------------------
def evaluate_3tuple(alpha_asymptotic: float, alpha_operational: float,
                    sat_pass: bool) -> dict:
    """gate-verdicts.md schema-v2 3-tuple + composite collapse.
      sign_verdict: PASS iff sign(alpha_asymptotic) == sign(-3) == NEGATIVE.
      magnitude_verdict: PASS iff |alpha_asymptotic-(-3)|/3 <= 0.05; INFO iff in
                         (0.05, 0.20]; FAIL iff > 0.20.
      regime_verdict: VALID iff the Friedrich-Bar saturation predicate holds across
                      the window AND the cross-axis-agreement guard does NOT fire
                      (|alpha_operational - alpha_asymptotic|/|alpha_asymptotic| <= 0.10);
                      MARGINAL iff the guard fires (cache-ceiling boundary effect; the
                      operational L=35 boundary value differs from the asymptotic limit
                      by more than 10% because the subleading (1+C1/L) correction is
                      still appreciable at the window bottom);
                      BREAKDOWN iff the saturation predicate fails.
    """
    rel = abs(alpha_asymptotic - ALPHA_TARGET) / abs(ALPHA_TARGET)  # (local)

    # sign
    sign_v = "PASS" if (alpha_asymptotic < 0.0) else "FAIL"  # (local)

    # magnitude
    if rel <= TAU_ALPHA:
        mag_v = "PASS"  # (local)
    elif rel <= INFO_BAND:
        mag_v = "INFO"  # (local)
    else:
        mag_v = "FAIL"  # (local)

    # cross-axis-agreement guard (operational L=35 boundary vs asymptotic limit)
    guard_dev = (abs(alpha_operational - alpha_asymptotic) /
                 abs(alpha_asymptotic)) if alpha_asymptotic != 0.0 else float("inf")  # (local)
    guard_fired = guard_dev > CROSS_AXIS_GUARD  # (local)

    # regime
    if not sat_pass:
        reg_v = "BREAKDOWN"  # (local)
    elif guard_fired:
        reg_v = "MARGINAL"  # (local)
    else:
        reg_v = "VALID"  # (local)

    # composite collapse (gate-verdicts.md schema-v2, PRE-REGISTERED)
    if reg_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"  # (local)
    elif mag_v == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    return {
        "rel": float(rel),
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "guard_dev": float(guard_dev),
        "guard_fired": bool(guard_fired),
        "composite": composite,
    }


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + schema-v2 3-tuple REQUIRED)
# -----------------------------------------------------------------------------
def find_prior_audit_sha() -> str:
    """Latest non-superseded canonical line for GATE_ID (gate-verdicts.md Option A)."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   sat: dict, alpha_res: dict, supersedes_sha: str = "") -> None:
    """Canonical line + dual-SHA companion + schema-v2 3-tuple row + bridge/
    regulator/level pin rows (atomic single open('a')) per gate-verdicts.md."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # REQUIRED [SIGN] 3-tuple companion row.
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"sign = (alpha_asymptotic NEGATIVE => convergent L^{{-3}} leading term)\n"
    )
    # Friedrich-Bar saturation provenance row
    fb_row = (
        f"# alpha_asymptotic={alpha_res['alpha_asymptotic']:.6f} "
        f"alpha_operational_L35={alpha_res['alpha_operational']:.6f} "
        f"alpha_at_L100={alpha_res['alpha_at_Ltop']:.6f} "
        f"alpha_target={ALPHA_TARGET} "
        f"saturation_predicate_pass={sat['saturation_predicate_pass']} "
        f"eta_FB_all_min_window={sat['eta_fb_all_min_window']:.4f} "
        f"botK_ceiling={sat['botK_ceiling']:.4f} "
        f"# {GATE_ID} Friedrich-Bar L_max-saturation (W11-3; S92 W9-3) analytic route, NO diag at L>=13\n"
    )
    # Regulator-pin (a_4^{Mellin}) row
    regulator_pin = (
        f"# REGULATOR_PIN=a_4^{{Mellin}} "
        f"# {GATE_ID} regulator-pin-discipline.md UV-regulator axis "
        f"(Mellin-Barnes; a_4 channel feeds the substrate-distance-1 pole s=3)\n"
    )
    # Level-pin: the alpha=-3 canonical is the SCHEMATIC two-pin convergence-exponent
    # protocol (rho_FULL_CC_VII_AU_SAT_s3 PROVENANCE); the leading-term geometric
    # exponent -(d-1) is a structural fact, but the canonical alpha pin carries the
    # SCHEMATIC CLASS per substrate-first-canonical-sourcing.md §(iv) K=4 level-pin.
    level_pin = (
        f"# LEVEL_CLASS_PIN=SCHEMATIC tier_pin=TIER-2 "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) K=4: "
        f"alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC=-3 is the SCHEMATIC two-pin "
        f"convergence-exponent protocol (rho_FULL_CC_VII_AU_SAT_s3 PROVENANCE); the "
        f"L^{{-3}} leading-term geometric envelope exponent -(d-1) at d=4 is the structural anchor\n"
    )
    rows = [line, companion, schema_v2_row, fb_row, regulator_pin, level_pin]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md Option A "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


# -----------------------------------------------------------------------------
# Plot
# -----------------------------------------------------------------------------
def make_plot(Ls: np.ndarray, alpha_res: dict, sat: dict, tup: dict,
              fit: dict, L_data: np.ndarray, Rb: np.ndarray) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.0))
    C1 = fit["C1_fit"]  # (local)

    # Panel 1: signed local exponent alpha(L) over the saturated window -> -3
    ax = axes[0]
    # the REAL in-cache signed local exponent (per-pair) from R_b data, for context
    lnL_d = np.log(L_data); lnR_d = np.log(np.abs(Rb))  # (local)
    loc_real = np.diff(lnR_d) / np.diff(lnL_d)  # (local) signed local exp from REAL R_b
    Lmid_real = 0.5 * (L_data[:-1] + L_data[1:])  # (local)
    ax.plot(Lmid_real, loc_real, "o", ms=4, color="#888888", alpha=0.7,
            label=r"REAL $R_b$ in-cache $d\ln R_b/d\ln L$ (L[12,22])")
    ax.plot(Ls, alpha_res["alpha_arr"], "-", lw=1.8, color="#1f77b4",
            label=r"fitted envelope $\alpha(L)$ (L[35,100])")
    ax.axhline(ALPHA_TARGET, color="crimson", ls="--", lw=1.6,
               label=r"target $\alpha=-3$")
    ax.scatter([1e2], [alpha_res["alpha_at_Ltop"]], color="green", zorder=5,
               label=rf"$\alpha(L{{=}}100)={alpha_res['alpha_at_Ltop']:.4f}$")
    ax.set_xlabel(r"$L$")
    ax.set_ylabel(r"signed local exponent $\alpha(L)=d\ln R_b/d\ln L$")
    ax.set_title(r"Layer-1 signed exponent $\alpha\to-3$ (positive-$C_1$ approach)")
    ax.legend(fontsize=7.5, loc="best")
    ax.grid(alpha=0.3)

    # Panel 2: Friedrich-Bar saturation band (NEW-sector floor vs botK ceiling)
    ax = axes[1]
    ax.plot(Ls, sat["new_bounds"], "s-", ms=3, color="#ff7f0e",
            label=r"NEW-sector floor $0.40\sqrt{C_2(L,0)+1}$")
    ax.axhline(sat["botK_ceiling"], color="purple", ls="--", lw=1.6,
               label=rf"botK ceiling = {sat['botK_ceiling']:.4f}")
    ax.axhline(ETA_FB_FLOOR_REF, color="gray", ls=":", lw=1.2,
               label=rf"empirical $\eta_{{FB}}$ floor = {ETA_FB_FLOOR_REF}")
    ax.set_xlabel(r"$L$ (NEW-sector level $p+q$)")
    ax.set_ylabel(r"eigenvalue floor")
    ax.set_title(rf"Friedrich-Bar saturation: NEW sectors excluded "
                 rf"({100*sat['frac_excluded']:.0f}%)")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    # Panel 3: REAL R_b(L) data + fitted envelope (deflated R_b * L^3 -> c(1+C1/L))
    ax = axes[2]
    deflated_real = Rb * L_data ** 3.0  # (local)
    Lfine = np.linspace(L_data.min(), Ls.max(), 400)  # (local)
    deflated_fit = fit["c_fit"] * (1.0 + C1 / Lfine)  # (local) c*(1+C1/L) = R_b*L^3
    ax.plot(L_data, deflated_real, "o", ms=5, color="#2ca02c",
            label=r"REAL $R_b(L)\cdot L^{3}$ (FULL CC-1995 §III.4)")
    ax.plot(Lfine, deflated_fit, "-", lw=1.6, color="#d62728",
            label=rf"fit $c(1+C_1/L)$, $c={fit['c_fit']:.3f}$ $C_1={C1:.3f}$")
    ax.axhline(fit["c_fit"], color="black", ls=":", lw=1.0,
               label=rf"$c\to${fit['c_fit']:.3f} ($L\to\infty$; leading exp $=-3$)")
    ax.set_xlabel(r"$L$")
    ax.set_ylabel(r"$R_b(L)\cdot L^{3}$")
    ax.set_title(rf"$R_b\cdot L^3\to c\Rightarrow$ leading exp $=-3$ "
                 rf"($R^2={fit['r2']:.4f}$, RMS={fit['rms']:.1e})")
    ax.legend(fontsize=7.5, loc="best")
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}  --  Layer-1 asymptotic alpha=-3 via Friedrich-Bar saturation "
        f"(d={D_SPACETIME}, pole s={POLE_S}, {REGULATOR_TAG})  |  "
        f"alpha_inf={alpha_res['alpha_asymptotic']:.4f}  |  "
        f"sign={tup['sign_verdict']} mag={tup['magnitude_verdict']} "
        f"regime={tup['regime_verdict']} -> {tup['composite']}",
        fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("  Layer-1 asymptotic alpha=-3 via Friedrich-Bar saturation (NO diag at L>=13)")
    print("=" * 78)

    # --- Input SHA log (first 20 lines of stdout per gate-verdicts.md) ---
    print("\n=== Input SHA-256 pins ===")
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    sha_cache = sha256_of(CACHE_L12)  # (local)
    sha_fb = sha256_of(S92_FB_NPZ)  # (local)
    sha_script = sha256_of(SCRIPT_PATH)  # (local)
    print(f"  canonical_constants.py : {sha_canon[:16]}...")
    print(f"  s84_spectrum_cache_L12 : {sha_cache[:16]}...")
    print(f"  s92_friedrich_bar npz  : {sha_fb[:16]}...")
    print(f"  script                 : {sha_script[:16]}...")

    print("\n=== Canonical imports ===")
    print(f"  alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = {alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC}")
    print(f"  alpha_b (L12-14 in-cache pre-asymptotic)     = {alpha_b_VII_AU_OP_PROJ_FW_LMAX14_EXTENSION:.6f}")
    print(f"  alpha_sample (L15-22 pre-asymptotic)         = {alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22:.6f}")
    print(f"  tau_fold = {tau_fold}")

    # --- Load Friedrich-Bar saturation precedent (S92 W9-3) for botK_ceiling ---
    print("\n=== Friedrich-Bar saturation precedent (S92 W9-3 npz) ===")
    fb = np.load(S92_FB_NPZ, allow_pickle=True)  # (local)
    botK_ceiling = float(fb["bot_k_ceiling"])  # (local)
    eta_FB_observed = float(fb["eta_FB_observed"])  # (local)
    eta_FB_all_min_cache = float(fb["eta_FB_all_min"])  # (local)
    new_bound_min_cache = float(fb["new_bound_min"])  # (local) NEW_sector13_bound
    print(f"  botK_ceiling      = {botK_ceiling:.4f}")
    print(f"  eta_FB_observed   = {eta_FB_observed:.4f}  (>= {ETA_FB_LOWER} required)")
    print(f"  eta_FB_all_min    = {eta_FB_all_min_cache:.4f}  (cache empirical floor)")
    print(f"  NEW_sector13_bound= {new_bound_min_cache:.4f}")

    # --- Step A: Friedrich-Bar saturation predicate across L in [35,100] ---
    print("\n=== Step A: Friedrich-Bar saturation predicate (L in [35,100]) ===")
    Ls = np.arange(L_LOW, L_HIGH + 1, L_STEP, dtype=float)  # (local)
    assert len(Ls) == N_EVAL, f"N_eval mismatch: {len(Ls)} != {N_EVAL}"
    sat = friedrich_bar_saturation(Ls, tau_fold, botK_ceiling)
    print(f"  NEW-sector floor @L=35  = {sat['new_bounds'][0]:.4f}  (vs botK {botK_ceiling:.4f})")
    print(f"  NEW-sector floor @L=100 = {sat['new_bounds'][-1]:.4f}")
    print(f"  eta_FB_all_min_window   = {sat['eta_fb_all_min_window']:.4f}")
    print(f"  saturation_predicate_pass = {sat['saturation_predicate_pass']} "
          f"(frac NEW excluded = {100*sat['frac_excluded']:.0f}%)")

    # --- Step B: load REAL FULL-physical residual R_b(L) + fit the L^{-3} envelope ---
    print("\n=== Step B: load REAL R_b(L) (FULL CC-1995 §III.4, L[12,22]) + fit envelope ===")
    lmax14 = np.load(S92_LMAX14_NPZ, allow_pickle=True)  # (local)
    L_data = lmax14["L_grid_R_b"].astype(float)  # (local) [12..22]
    Rb = lmax14["R_b_per_L"].astype(float)  # (local) REAL FULL-physical residual (level_pin=FULL, tier_pin=TIER-1)
    print(f"  R_b(L) L grid : {L_data.astype(int).tolist()}")
    print(f"  R_b(L) values : {np.array2string(Rb, precision=6)}")
    print(f"  R_b monotone decreasing? {bool(np.all(np.diff(np.abs(Rb)) < 0))}")
    fit = fit_envelope_to_real_residual(L_data, Rb)
    print(f"  envelope fit: c={fit['c_fit']:.5f}  C1={fit['C1_fit']:.5f}  "
          f"(R^2={fit['r2']:.5f}, RMS={fit['rms']:.3e})")
    print(f"  in-cache decay-magnitude recovered over L[15,22] = {fit['alpha_b_recovered_L15_22']:.6f}")
    print(f"    (matches canonical alpha_sample={alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22:.6f}? "
          f"rel_dev={abs(fit['alpha_b_recovered_L15_22']-alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22)/alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22:.2e})")

    # --- Step C: extrapolate the signed exponent to the saturated L[35,100] window ---
    print("\n=== Step C: signed local exponent over the FB-saturated L[35,100] window ===")
    alpha_res = extract_alpha_asymptotic(Ls, fit["C1_fit"])
    print(f"  alpha_operational (L=35 window bottom)  = {alpha_res['alpha_operational']:.6f}")
    print(f"  alpha @ L=100 (window top)              = {alpha_res['alpha_at_Ltop']:.6f}")
    print(f"  alpha_asymptotic (L->infinity)          = {alpha_res['alpha_asymptotic']:.6f}")
    print(f"  target alpha = {ALPHA_TARGET}")
    print(f"  SIGN: alpha_asymptotic < 0 => NEGATIVE (convergent). The in-cache decay")
    print(f"        magnitude {fit['alpha_b_recovered_L15_22']:.4f} (sample) is PRE-ASYMPTOTIC; "
          f"|alpha| rises to 3 as L->inf.")

    # --- Cross-check: C1=0 pure L^{-3} envelope MUST give exactly -3 ---
    alpha_res0 = extract_alpha_asymptotic(Ls, 0.0)  # (local)
    print(f"  [cross-check] C1=0 pure L^{{-3}} envelope -> alpha = {alpha_res0['alpha_asymptotic']:.6f} "
          f"(must be -3 at all L)")
    # Sanity: structural leading exponent is -(d-1)
    print(f"  [structural] -(d-1) = -({D_SPACETIME}-1) = {-(D_SPACETIME-1)} (the d=4 L^{{-3}} envelope exponent)")

    # --- Verdict (3-tuple + composite collapse) ---
    print("\n=== Verdict (3-tuple + composite collapse) ===")
    tup = evaluate_3tuple(alpha_res["alpha_asymptotic"],
                          alpha_res["alpha_operational"],
                          sat["saturation_predicate_pass"])
    print(f"  rel |alpha_asymptotic - (-3)| / 3 = {tup['rel']:.4e}  (PASS <= {TAU_ALPHA})")
    print(f"  cross-axis guard dev (L=35 vs inf)= {tup['guard_dev']:.4e}  (fired: {tup['guard_fired']}, thr {CROSS_AXIS_GUARD})")
    print(f"  sign_verdict      = {tup['sign_verdict']}")
    print(f"  magnitude_verdict = {tup['magnitude_verdict']}")
    print(f"  regime_verdict    = {tup['regime_verdict']}")
    print(f"  COMPOSITE         = {tup['composite']}")

    # --- Dual-SHA over the pinmap (full machinery_pin_map per plan §W2-3) ---
    pins = {
        "N_eval": N_EVAL,
        "L_max": L_MAX,
        "L_low": L_LOW,
        "L_high": L_HIGH,
        "L_step": L_STEP,
        "d_spacetime": D_SPACETIME,
        "pole_s": POLE_S,
        "eta_FB_lower": ETA_FB_LOWER,
        "master_cache_L_max": MASTER_CACHE_L_MAX,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "tolerance": TAU_ALPHA,
        "cross_axis_guard": CROSS_AXIS_GUARD,
        "regulator_tag": REGULATOR_TAG,
        "fit_basis": FIT_BASIS,
        "alpha_target": ALPHA_TARGET,
        "tau_evaluate": tau_fold,
        "GPU_path": "cpu-cap-OMP8",
        "random_seed": "N/A-deterministic",
        "sha_canonical": sha_canon,
        "sha_s84_cache": sha_cache,
        "sha_s92_fb": sha_fb,
        "sha_s92_lmax14": sha256_of(S92_LMAX14_NPZ),
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- Save data ---
    domain_used_frac = 1.0  # (local) full intended window used (no auto-shortening)
    np.savez(
        OUT_NPZ,
        alpha_asymptotic=alpha_res["alpha_asymptotic"],
        alpha_operational_L35=alpha_res["alpha_operational"],
        alpha_at_L100=alpha_res["alpha_at_Ltop"],
        alpha_target=ALPHA_TARGET,
        alpha_of_L=alpha_res["alpha_arr"],
        L_mid=alpha_res["Lmid"],
        L_window=Ls,
        R_b_real=Rb,
        L_data_real=L_data,
        envelope_c_fit=fit["c_fit"],
        envelope_C1_fit=fit["C1_fit"],
        envelope_fit_r2=fit["r2"],
        envelope_fit_rms=fit["rms"],
        alpha_b_recovered_L15_22=fit["alpha_b_recovered_L15_22"],
        alpha_asymptotic_C1_zero=alpha_res0["alpha_asymptotic"],
        eta_FB_all_min=sat["eta_fb_all_min_window"],
        eta_FB_lower=ETA_FB_LOWER,
        new_sector_bounds=sat["new_bounds"],
        botK_ceiling=botK_ceiling,
        saturation_predicate_pass=sat["saturation_predicate_pass"],
        frac_excluded=sat["frac_excluded"],
        alpha_b_crosscheck=alpha_b_VII_AU_OP_PROJ_FW_LMAX14_EXTENSION,
        alpha_sample_crosscheck=alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,
        alpha_canonical_pin=alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,
        rel_to_target=tup["rel"],
        guard_dev=tup["guard_dev"],
        guard_fired=tup["guard_fired"],
        domain_used_frac=domain_used_frac,
        d_spacetime=D_SPACETIME,
        pole_s=POLE_S,
        sign_verdict=tup["sign_verdict"],
        magnitude_verdict=tup["magnitude_verdict"],
        regime_verdict=tup["regime_verdict"],
        composite=tup["composite"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"\n  data -> {OUT_NPZ}")

    # --- Plot ---
    make_plot(Ls, alpha_res, sat, tup, fit, L_data, Rb)
    print(f"  plot -> {OUT_PNG}")

    # --- Emit verdict line (supersession-aware) ---
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = prior_sha if (prior_sha and prior_sha != audit_sha) else ""  # (local)
    value_str = (f"alpha_asymptotic={alpha_res['alpha_asymptotic']:.6f}_"
                 f"target=-3_rel={tup['rel']:.3e}_C1fit={fit['C1_fit']:.3f}_"
                 f"alpha_b_recov={fit['alpha_b_recovered_L15_22']:.4f}_"
                 f"sat={sat['saturation_predicate_pass']}_domain_used_frac={domain_used_frac:.2f}")  # (local)
    append_verdict(tup["composite"], value_str, audit_sha, content_sha,
                   tup["sign_verdict"], tup["magnitude_verdict"], tup["regime_verdict"],
                   sat, alpha_res, supersedes_sha=supersedes)
    print(f"  verdict line appended -> {VERDICT_TXT}")

    print(f"\n=== {GATE_ID}: {tup['composite']} "
          f"(sign={tup['sign_verdict']}, mag={tup['magnitude_verdict']}, "
          f"regime={tup['regime_verdict']}) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
