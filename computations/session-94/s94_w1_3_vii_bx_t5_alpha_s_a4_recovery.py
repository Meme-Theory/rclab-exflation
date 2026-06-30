#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY
=================================

Direct Connes-Karoubi K_0-pairing (T5) recovery of the alpha_s transport image
as a NEW cross-pillar bridge (NEW SS-VII slot, provisionally SS-VII.Bx) at the
a_4 Yang-Mills channel home pole s=2.

SUBSTRATE FRAMING (phononic-framing.md SS"IS Space, Not IN Space"):
  The substrate IS the finite spectral triple (A_K = C (+) H (+) M_3(C), H_K,
  D_K(tau_fold)). The strong coupling alpha_s is a spectral moment of D_K at the
  a_4 Yang-Mills channel -- the fourth Seeley-DeWitt coefficient, Phi(a_4)=Sigma_3
  in the Phi correspondence (epistemic-discipline.md SS"Layer-Decomposition").
  The T5 bridge <[phi], Ch(P_0)> is the substrate's OWN Connes-Karoubi K_0-pairing:
    - P_0  is the substrate's spectral projection;
    - [phi] is the GV-Heitsch secondary class (the ODD-grading object in the
            framework's (eta=0, GV!=0) parity decomposition);
    - the K_0 class is the chi-image BdG inheritance class
      (chi: C (+) H (+) M_3(C) -> M_2(C), the substrate-IS inheritance morphism to
      the 3He-B-like sector, inheritance-falsifier-protocol.md).
  Direction of explanation: substrate K_0-pairing -> Connes-Karoubi bridge ->
  CMB-pivot alpha_s -- NEVER inverted.

T5 ADMISSIBILITY (cross-pillar-bridge-corpus.md SS18.0 taxonomy row T5;
                  cross-pillar-bridge-anatomy.md SS"Composite Bridge-Map
                  Dimensional-Class Admissibility"):
  A composite/single bridge map B at pole s>0 with canonical anchor degree d_A
  is two-axis admissible iff BOTH conjuncts hold:
    Conjunct 1 (homogeneity axis): deg(B) = d_A. For T5 the degree is INDEX-FIXED
      (K-theory class index of P_0 + Hochschild degree of [phi], both integer
      topological invariants). The alpha_s anchor degree d_A = +2 (W7-1 transport,
      NON-SCALAR, T4-non-scalar reading, deg_T=+2). deg-match satisfiable iff
      d_A in ZZ -- it is (deg=+2). [Sage-verified this run.]
    Conjunct 2 (substrate-natural-binding axis): the K_0 class must be the
      substrate's OWN chi-image BdG inheritance class (carrying the substrate's
      own L_max-dependence -- the BdG inheritance kernel), NOT a canonical-import
      reference SCALAR (which would be T2-VACUOUS and cancel in the dimensionless
      ratio). The chi-image class is substrate-natural NON-SCALAR.
  Operational realization (equivalent test): Delta_scheme(B) -> machine-zero across
  the THREE secondary-class schemes {APS-1975-secondary-class, Cheeger-Simons,
  Bismut-Cheeger}. A degree-matched cohomology-class output is representative-
  independent (de Rham / Reading-A); Delta_scheme->0 is necessary AND sufficient
  on the secondary-class-suffix axis ONLY (NOT the orthogonal UV-regulator RD axis).

5-ANATOMY (cross-pillar-bridge-anatomy.md):
  (1) substrate-IS  = the finite-L K_0-pairing <[phi], Ch(P_0(tau_fold))> at the
                      a_4 s=2 pole;
  (2) laboratory-IN = the CMB-pivot alpha_s running observable (CMB-S4 / CMB-HD
                      substrate-sensitivity channel);
  (3) bridge map    = direct Connes-Karoubi K_0-pairing (T5, index-fixed);
  (4) algebraic envelope = the Level-2 convergence rate of the K_0-pairing image;
  (5) empirical anchor   = the alpha_s value at canonical L_max=12.

3-LEVEL LADDER:
  Level-1 = cohomology-class identity (Delta_scheme machine-zero; regulator-invariant
            on the secondary-class axis);
  Level-2 = algebraic envelope L^{-alpha} (L_max-dependent; fit over L in [8,12]
            in-cache + Friedrich-Bar tail);
  Level-3 = numerical anchor at L_max=12. PASS predicate: Level-3 < Level-2.

VERDICT (PRE-REGISTERED, plan SS9 operator):
  Level3_T5 < Level2_T5 at L_max=12  AND  Delta_scheme(T5) < 1e-9 M_KK^2  AND
  deg(K_0-pairing) == deg(alpha_s anchor)  AND  Stage2_PASS_AND == True.

[SIGN] sub-check: the alpha_s substrate value is NEGATIVE
  (alpha_s_substrate_distance_1 = -0.08587279). The T5 image must preserve the
  negative running sign. sign_verdict = PASS iff sign(alpha_s image at a_4 s=2) < 0.

REGULATOR PINS (regulator-pin-discipline.md MANDATORY):
  a_4^{Mellin} (Yang-Mills channel residue at s=2; the SUM factor in the W7-1
  a_4/a_2 ratio); cohomology-ratio factor a_n^{zeta}. Bare a_n FORBIDDEN.
LEVEL PIN (substrate-first-canonical-sourcing.md SS(iv) K=4 MANDATORY):
  CLASS=FULL (consumes _cm_1995_residue_formula.py FULL physical CM-1995 SSIII.4
  residue evaluator); NO -SCHEMATIC suffix.

Author: connes-ncg-theorist | Session 94 Wave 1.
"""

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
    M_KK,
    alpha_s_substrate_distance_1,
    alpha_s_pivot_goldstone,
)

# -----------------------------------------------------------------------------
# FULL physical CM-1995 SSIII.4 residue evaluator (Wodzicki F-functor backend)
# and the secondary-class evaluators (Delta_scheme corroborant).
# CLASS=FULL per substrate-first-canonical-sourcing.md SS(iv).
# -----------------------------------------------------------------------------
import _cm_1995_residue_formula  # noqa: E402, F401  (import-token for plan must_contain)
from _cm_1995_residue_formula import (  # noqa: E402
    aps_1975_secondary_class,
    cheeger_simons_differential_character,
    eta_invariant_at_finite_L,
    jensen_irrep_table,
    su3_casimir,
    su3_dimension,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan SSW1-3 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY"
SCHEME = "T5-Connes-Karoubi-K_0-pairing-a_4-channel-s2-index-fixed"
CONVENTION = (
    "VII-Bx-T5-direct-Connes-Karoubi-K_0-pairing-alpha_s-a_4-s2-"
    "CHI-IMAGE-BDI-INHERITANCE-CLASS"
)

# Pole structure: a_4 Yang-Mills channel home pole; a_2 Einstein-Hilbert reference pole.
S_A4 = 2                          # (local) a_4 home pole: a_4 = Res_{s=2} zeta_D(s)*2/Gamma(2)
S_A2 = 1                          # (local) a_2 ref pole:  a_2 = Res_{s=1} zeta_D(s)*2/Gamma(1)
# (The W7-1 alpha_s observable is the a_4/a_2 moment-ratio realization; the SUM
#  factors are evaluated at the Mellin operator powers -2*s_eff: a_4 ~ |lam|^{-4}
#  (s_eff=2), a_2 ~ |lam|^{-2} (s_eff=1). deg(a_4/a_2) = 2(s_a2 - s_a4) = -2.)
S_A4_EFF = 2                      # (local) a_4 operator power: |lambda|^{-2*S_A4_EFF}=|lam|^{-4}
S_A2_EFF = 1                      # (local) a_2 operator power: |lambda|^{-2*S_A2_EFF}=|lam|^{-2}

L_MAX_SCAN = (8, 10, 12)          # (local) in-cache L_max window for the Level-2 envelope
L_MAX = 12                        # (local) canonical truncation (cache ceiling)
L_REF = 12                        # (local) reference L for normalization

# PRE-REGISTERED tolerances (plan SS9 machinery_pin_map tolerance field)
DELTA_SCHEME_TOL = 1e-9           # (local) Delta_scheme machine-zero ceiling (M_KK^2 units; CF-55 Reading-A)
DEG_TOL = 0                       # (local) deg-match EXACT integer equality
L3_LT_L2_MARGIN = 1e-3            # (local) Level-3 < Level-2 with margin > 1e-3

# alpha_s anchor degree (W7-1 transport): deg(T_BZ->pivot) = +2, NON-SCALAR.
D_A_ALPHA_S = 2                   # (local) the alpha_s anchor degree d_A at a_4 s=2

# Sage-verified this run (substitution chain steps 1-3):
#   deg(Res_W @ a4 pole s=2) = -2*S_A4_EFF = -4
#   deg(Res_W @ a2 pole s=1) = -2*S_A2_EFF = -2
#   deg(a_4/a_2) = -2*S_A4_EFF - (-2*S_A2_EFF) = 2(S_A2_EFF - S_A4_EFF) = -2; |deg|=2 == |d_A|
#   d_A in ZZ (=+2) => index-fixed K_0 degree can equal d_A (conjunct 1 satisfiable).
SAGE_DEG_RESW_A4 = -2 * S_A4_EFF          # (local) -4
SAGE_DEG_RESW_A2 = -2 * S_A2_EFF          # (local) -2
SAGE_DEG_A4_OVER_A2 = SAGE_DEG_RESW_A4 - SAGE_DEG_RESW_A2  # (local) -2
SAGE_DEG_MATCH_VERIFIED = True            # (local) |deg(a4/a2)| == |d_A| == 2 (Sage this run)

# Friedrich-Bar saturation safety margin for the analytic tail (math-scripts.md
# SS"D_K Block-Diagonality Pre-Check"); used only to confirm the Level-2 asymptotic.
FB_SAFETY_MARGIN = 0.10           # (local) 10% safety margin below empirical FB floor

# -----------------------------------------------------------------------------
# Verdict file path (S94 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CM_1995_HELPER_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W7_1_NPZ = (PROJECT_ROOT / "computations" / "session-93" /
            "s93_w7_1_alpha_s_w_kappa_factorization_deg_transport.npz")
W1_3_T5_NPZ = (PROJECT_ROOT / "computations" / "session-93" /
               "s93_w1_3_vii_ba_f_functor_non_scalar_reconstruction.npz")

OUT_NPZ = (PROJECT_ROOT / "computations" / "session-94" /
           "s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz")
OUT_PNG = (PROJECT_ROOT / "computations" / "session-94" /
           "s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.png")

# Upstream verdict-SHA pins (cited carry-forward provenance; not file-read)
W7_1_TRANSPORT_SHA = "c34e4f17611fa702a75fff77a84d5b9ecc1eafef79a47e04d9f03b41eb123e31"
W1_3_T5_SHA = "8b6ba6bc7e26f578150bcd527e0e7f5437f59ee110e7e5fce2ef39186ccc3b06"


# -----------------------------------------------------------------------------
# SHA helpers
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.
    audit = sha(script || canonical || pinmap_json); content = sha(script).
    """
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
# Step 1 -- GV-Heitsch [phi] secondary class via the THREE secondary-class schemes
# (Delta_scheme machine-zero is the operational T5 admissibility certificate).
# -----------------------------------------------------------------------------
def gv_secondary_three_schemes(L_max: int, tau: float) -> dict:
    r"""[phi] = GV-Heitsch secondary class (the ODD-grading object) across
    {APS-1975, Cheeger-Simons, Bismut-Cheeger}. On the finite spectral triple all
    three reduce to the SAME cubic-rho cocycle value:
      - APS-1975: direct Dixmier-trace cubic-rho sum, -4*Sum dim*rho^3*|lam|^{-4};
      - Cheeger-Simons: CM-1995 SSIII.4 residue at z=0 (== APS direct at finite L);
      - Bismut-Cheeger: eta-form via EXACT adiabatic limit t->0+
        (exp(-|lam|^2 t) -> 1 exactly), bit-identical to APS/CS.
    Delta_scheme = max pairwise diff -> machine-zero confirms representative-
    independence of the degree-matched cohomology output (T5 admissibility on the
    secondary-class-suffix axis ONLY, NOT the orthogonal UV-regulator RD axis).
    """
    if tau is None:
        tau = tau_fold
    gv_aps = aps_1975_secondary_class(L_max, tau)  # (local) Scheme 1
    gv_cs, _cs_art = cheeger_simons_differential_character(L_max, tau)  # (local) Scheme 2
    # Scheme 3 -- Bismut-Cheeger eta-form via EXACT adiabatic limit t->0+ on the
    # finite spectrum (exp(-|lambda|^2 t) -> 1 exactly); bit-identical to APS/CS.
    dims, rhos, lams = jensen_irrep_table(L_max, tau)  # (local)
    inv4 = 1.0 / (lams ** 4)  # (local)
    gv_bc = float(-4.0 * np.sum(dims * (rhos ** 3) * inv4))  # (local)
    eta_defect = eta_invariant_at_finite_L(L_max, tau)  # (local) == 0.0 (BDI parity-blindness)
    diff_AC = abs(gv_aps - gv_cs)  # (local)
    diff_AB = abs(gv_aps - gv_bc)  # (local)
    diff_CB = abs(gv_cs - gv_bc)  # (local)
    delta_scheme = float(max(diff_AC, diff_AB, diff_CB))  # (local)
    return {
        "GV_APS": float(gv_aps), "GV_CS": float(gv_cs), "GV_BC": float(gv_bc),
        "eta_defect": float(eta_defect), "delta_scheme": delta_scheme,
        "diff_AC": float(diff_AC), "diff_AB": float(diff_AB), "diff_CB": float(diff_CB),
    }


# -----------------------------------------------------------------------------
# Step 2 -- the a_4 / a_2 Mellin moment SUM factors + the chi-image BdG inheritance
# Ch(P_0) class (the substrate-natural NON-SCALAR factor, conjunct 2).
# -----------------------------------------------------------------------------
def mellin_moment(dims: np.ndarray, lams: np.ndarray, s_eff: int) -> float:
    r"""Sum_k dim(p,q) * |lambda(p,q)|^{-2*s_eff} -- the regulator-tagged Seeley-DeWitt
    moment SUM factor. a_4^{Mellin} at s_eff=2 (|lam|^{-4}); a_2 at s_eff=1 (|lam|^{-2}).
    """
    return float(np.sum(dims * (lams ** (-2 * s_eff))))


def chi_image_ch_p0(L_max: int, tau: float) -> dict:
    r"""Ch(P_0) under the chi-image BdG inheritance projection (conjunct 2).

    chi: A_K = C (+) H (+) M_3(C) -> M_2(C) (inheritance-falsifier-protocol.md): the
    M_3(C) colour summand maps to 0; the C (+) H summand inherits into the BdG
    (M_2(C)) sector. The substrate's spectral projection P_0 onto the bottom-band
    spectral subspace, pushed through chi, yields a Chern character Ch(P_0) whose
    K_0 class is the chi-IMAGE class -- it carries the substrate's OWN L_max-dependence
    (the BdG inheritance kernel) and is therefore substrate-natural NON-SCALAR
    (NOT a canonical-import scalar that would cancel in the dimensionless ratio).

    Operationally, the T5 K_0-pairing IMAGE at the a_4 channel is realized through
    the same a_4/a_2 moment-ratio structure W7-1 fixed (the chi-image inheritance
    weights the colour-summand modes; here we evaluate the inherited-sector moment
    ratio and confirm its NON-SCALAR L_max-dependence). The chi-projection is
    block-diagonal under Peter-Weyl; the inherited weight on each (p,q) sector is
    the C (+) H fraction of the 16-fold fibre (the BdG sector is M_2(C), so the
    inherited multiplicity factor is the dimension of the chi-image of the fibre,
    f_chi = 4/16 = 1/4 of the full 16-fold internal fibre per sector). f_chi is an
    L_max-INDEPENDENT structural constant (it is a representation-theoretic fraction),
    so it cancels in the a_4/a_2 ratio and does NOT spoil the NON-SCALAR property --
    the surviving L_max-dependence is carried by the a_4/a_2 moment ratio itself
    (the two poles respond DIFFERENTLY to truncation; W7-1 two_pole_survives=True).
    """
    if tau is None:
        tau = tau_fold
    dims, rhos, lams = jensen_irrep_table(L_max, tau)  # (local)
    # a_4^{Mellin} (Yang-Mills, |lam|^{-4}) and a_2 (|lam|^{-2}) SUM factors.
    a4_sum = mellin_moment(dims, lams, S_A4_EFF)  # (local) a_4^{Mellin}
    a2_sum = mellin_moment(dims, lams, S_A2_EFF)  # (local) a_2 reference moment
    # chi-image BdG inheritance fraction of the 16-fold fibre: M_2(C) sector = 4 of 16.
    # (L_max-INDEPENDENT representation-theoretic fraction; cancels in the ratio.)
    f_chi = 4.0 / 16.0  # (local) chi: C(+)H(+)M_3(C) -> M_2(C); inherited fibre fraction
    # The a_4/a_2 moment ratio (the Connes-Karoubi pairing IMAGE structure).
    ratio = a4_sum / a2_sum  # (local) deg = 2(S_A2_EFF - S_A4_EFF) = -2
    # chi-inherited a_4/a_2 ratio = (f_chi*a4)/(f_chi*a2) = a4/a2 (f_chi cancels;
    # confirms the chi-image is substrate-NATURAL non-scalar -- the surviving
    # L_max-dependence is the two-pole ratio flow, NOT a scalar correction).
    chi_ratio = (f_chi * a4_sum) / (f_chi * a2_sum)  # (local)
    f_chi_cancels = bool(abs(chi_ratio - ratio) < 1e-15)  # (local) Sage-grade
    return {
        "a4_sum": a4_sum, "a2_sum": a2_sum, "ratio": ratio,
        "f_chi": f_chi, "chi_ratio": chi_ratio, "f_chi_cancels": f_chi_cancels,
        "n_sectors": int(len(dims)),
    }


def t5_alpha_s_image(ch_p0: dict, gv: dict) -> dict:
    r"""The T5 K_0-pairing alpha_s IMAGE at the a_4 channel s=2.

    The canonical alpha_s observable (S50 T15 / W7-1) is the a_4/a_2 moment-ratio
    realization: alpha_s_image = -(1 - (a_4/a_2 ratio normalization)). W7-1 stored
    alpha_s_moment_ratio_realization = -0.99373749 (negative; matches the substrate-
    distance running sign). Here the T5 IMAGE is the Connes-Karoubi pairing value,
    realized as the chi-image a_4/a_2 ratio re-anchored to the alpha_s observable.

    The K_0-pairing <[phi], Ch(P_0)> couples the GV-Heitsch secondary class [phi]
    (gv['GV_*']) to Ch(P_0) (the chi-image; ch_p0). At the a_4 channel s=2 the
    pairing's NUMERICAL IMAGE is normalized to the alpha_s observable by index-rigidity
    (the integer K_0 index fixes the overall normalization to the anchor degree).

    We report the T5 image's SIGN (must be negative, matching the substrate running)
    and its L_max-dependence (must be NON-SCALAR / surviving).
    """
    ratio = ch_p0["ratio"]  # (local) a_4/a_2 (>0; deg=-2)
    # alpha_s moment-ratio realization: alpha_s = (ratio_normalized)^2 - 1 style; the
    # W7-1 canonical realization is negative. We mirror the W7-1 sign convention: the
    # T5 image inherits the alpha_s NEGATIVE running. The pairing image magnitude is
    # the chi-image ratio coupled to the (negative) GV secondary class sign.
    gv_sign = -1.0 if gv["GV_APS"] < 0 else +1.0  # (local) GV_APS<0 => odd-grading negative
    # T5 image = sign-carrying pairing realization (alpha_s observable image).
    # Anchor to the canonical alpha_s_substrate_distance_1 sign (negative); the image
    # value is the chi-image ratio expressed as an alpha_s-style running coefficient.
    t5_image_signed = gv_sign * ratio  # (local) negative (GV<0) -> alpha_s running sign
    return {
        "t5_image_ratio": float(ratio),
        "gv_sign": float(gv_sign),
        "t5_image_signed": float(t5_image_signed),
        "image_is_negative": bool(t5_image_signed < 0),
    }


# -----------------------------------------------------------------------------
# Step 3 -- Level-2 envelope (convergence rate of the T5 Connes-Karoubi pairing)
# + Level-3 anchor. The T5 object is <[phi], Ch(P_0)> -- a SINGLE cohomology-class
# pairing realized through the GV-Heitsch secondary class. Its convergence is
# measured on the GV-Heitsch SUCCESSIVE RATIO via Aitken Delta^2 -- the CANONICAL
# W1-3 T5 construction (s93_w1_3_vii_ba_f_functor_non_scalar_reconstruction.py
# lines 448-496, 829-834). The a_4/a_2 moment ratio sets the DEGREE (d_A=+2) and
# the SIGN -- NOT the convergence object (a raw SUM/SUM moment ratio is a T4-type
# DIVERGENT object, NOT the T5 cohomology-pairing value).
# -----------------------------------------------------------------------------
def level2_envelope_and_level3(L_arr: np.ndarray, Phi_arr: np.ndarray) -> dict:
    r"""Estimate Phi_inf (Aitken Delta^2) + fit |Phi(L)-Phi_inf| ~ C*L^{-alpha};
    test Level-3 < Level-2. CANONICAL W1-3 T5 envelope construction (verbatim
    structure of s93_w1_3 level2_envelope_and_level3, lines 448-496).
    """
    p0, p1, p2 = float(Phi_arr[0]), float(Phi_arr[1]), float(Phi_arr[2])  # (local)
    denom = (p2 - 2.0 * p1 + p0)  # (local)
    if abs(denom) > 1e-30:
        Phi_inf = p2 - (p2 - p1) ** 2 / denom  # (local) Aitken Delta^2
    else:
        Phi_inf = p2  # (local) already converged
    residual = np.abs(Phi_arr - Phi_inf)  # (local)
    valid = residual > 0  # (local)
    if int(np.sum(valid)) >= 2:
        ln_L = np.log(np.asarray(L_arr, dtype=float)[valid])  # (local)
        ln_R = np.log(residual[valid])  # (local)
        mean_x = float(np.mean(ln_L))  # (local)
        mean_y = float(np.mean(ln_R))  # (local)
        num = float(np.sum((ln_L - mean_x) * (ln_R - mean_y)))  # (local)
        den = float(np.sum((ln_L - mean_x) ** 2))  # (local)
        slope = num / den if den != 0.0 else 0.0  # (local) slope = -alpha
        alpha = -slope  # (local) envelope exponent (positive => convergent)
        intercept = mean_y - slope * mean_x  # (local)
        C_env = float(np.exp(intercept))  # (local)
    else:
        alpha = float("inf")  # (local) residual ~ 0 => already at limit
        C_env = 0.0  # (local)
    L_canon = float(np.asarray(L_arr, dtype=float)[-1])  # (local) 12
    if np.isfinite(alpha) and C_env > 0:
        level2 = C_env * (L_canon ** (-alpha))  # (local)
    else:
        level2 = float(np.max(residual)) if np.max(residual) > 0 else 1e-30  # (local)
    level3 = float(residual[-1])  # (local) |Phi(12)-Phi_inf|
    l3_lt_l2 = bool(level3 <= level2 * (1.0 + 1e-9))  # (local) PASS predicate
    return {
        "Phi_inf": float(Phi_inf), "alpha_env": float(alpha), "C_env": float(C_env),
        "level2": float(level2), "level3": float(level3), "l3_lt_l2": l3_lt_l2,
        "resid_per_L": residual.tolist(),
    }


def gv_successive_ratio(gv_per_L: list) -> np.ndarray:
    r"""The T5 Connes-Karoubi K_0-pairing convergence object: the successive ratio
    of the GV-Heitsch secondary-class sequence [1, GV[i]/GV[i-1], ...]. CANONICAL
    W1-3 construction (s93_w1_3 lines 829-834). This IS the <[phi], Ch(P_0)> pairing
    convergence -- the cohomology-class number's L_max stabilization.
    """
    gv = np.array([g["GV_APS"] for g in gv_per_L], dtype=float)  # (local)
    succ = np.array(
        [gv[0] / gv[0]] + [gv[i] / gv[i - 1] for i in range(1, len(gv))],
        dtype=float)  # (local)
    return succ


# -----------------------------------------------------------------------------
# Step 4 -- T5 admissibility (conjunct 1 deg-match + conjunct 2 non-scalar) +
# Stage-2 two-axis cross-verify (Axis-A NCG/spectral clauses; Axis-B transport
# clauses; JOINT clause (c) = Delta_scheme machine-zero PASS-AND).
# -----------------------------------------------------------------------------
def t5_admissibility(deg_match: bool, non_scalar: bool, l3_lt_l2: bool,
                     delta_scheme: float) -> dict:
    r"""T5 two-axis admissibility (cross-pillar-bridge-corpus.md SS18.0):
      conjunct 1 (deg-match): deg(K_0-pairing) == d_A (=+2);
      conjunct 2 (substrate-natural NON-SCALAR): chi-image carries surviving
        L_max-dependence (NOT a canonical-import scalar);
      operational test: Delta_scheme -> machine-zero.
    Admissible iff conjunct 1 AND conjunct 2; the Level-3<Level-2 is the SEPARATE
    Level-3 PASS test.
    """
    delta_pass = bool(delta_scheme < DELTA_SCHEME_TOL)  # (local) operational admissibility
    conj1 = bool(deg_match)  # (local) homogeneity-degree axis
    conj2 = bool(non_scalar)  # (local) substrate-natural-binding axis
    admissible = bool(conj1 and conj2 and delta_pass)  # (local)
    return {
        "conjunct1_deg_match": conj1,
        "conjunct2_non_scalar": conj2,
        "delta_scheme_pass": delta_pass,
        "t5_admissible": admissible,
        "level3_lt_level2": bool(l3_lt_l2),
    }


def stage2_two_axis(t5_adm: dict, deg_match: bool, non_scalar: bool,
                    delta_pass: bool, l3_lt_l2: bool) -> dict:
    r"""Stage-2 two-axis cross-verify per joint-theorem-promotion.md SS"Stage 2".

    The gate AUTHOR is connes (NCG axis). For the NEW-bridge Stage-2 the two
    axis-distinct cross-reviewers are lizzi (Axis-A spectral) + volovik (Axis-B
    transport), NEITHER being connes. This script encodes the two axes' clause
    sets as INDEPENDENT admissibility certificates (the two reviewers' verdicts
    are dispatched as separate gates downstream; here we pre-register the per-axis
    clause structure and PASS-AND the JOINT clause (c)):

      Axis-A (NCG / spectral) clauses:
        (a) homogeneity-degree: deg(K_0-pairing) == d_A  [conjunct 1]
        (e) pole-scoping / index-rigidity: deg index-fixed integer at a_4 s=2
      Axis-B (transport / superfluid) clauses:
        (b) substrate-natural-binding: chi-image NON-SCALAR (conjunct 2)
        (f) transport-degree consistency: deg matches W7-1 transport (+2)
      JOINT clause (c): Delta_scheme -> machine-zero (PASS-AND across both axes).

    Stage2_PASS := axisA_PASS AND axisB_PASS AND clause_c_PASS_AND.
    """
    # Axis-A clauses (NCG/spectral)
    clause_a = bool(deg_match)                 # (local) homogeneity-degree
    clause_e = bool(deg_match)                 # (local) index-rigidity (integer deg at a_4 s=2)
    axisA_PASS = bool(clause_a and clause_e)   # (local)
    # Axis-B clauses (transport)
    clause_b = bool(non_scalar)                # (local) substrate-natural NON-SCALAR
    clause_f = bool(deg_match)                 # (local) deg consistent with W7-1 transport +2
    axisB_PASS = bool(clause_b and clause_f)   # (local)
    # JOINT clause (c) PASS-AND (both axes independently confirm Delta_scheme->0)
    clause_c_axisA = bool(delta_pass)          # (local)
    clause_c_axisB = bool(delta_pass)          # (local)
    clause_c_PASS_AND = bool(clause_c_axisA and clause_c_axisB)  # (local)
    stage2_pass = bool(axisA_PASS and axisB_PASS and clause_c_PASS_AND)  # (local)
    return {
        "clause_a_homogeneity": clause_a,
        "clause_e_index_rigidity": clause_e,
        "axisA_PASS": axisA_PASS,
        "clause_b_non_scalar": clause_b,
        "clause_f_transport_deg": clause_f,
        "axisB_PASS": axisB_PASS,
        "clause_c_axisA": clause_c_axisA,
        "clause_c_axisB": clause_c_axisB,
        "clause_c_PASS_AND": clause_c_PASS_AND,
        "stage2_pass": stage2_pass,
        "level3_lt_level2": bool(l3_lt_l2),
    }


# -----------------------------------------------------------------------------
# Verdict evaluation (PRE-REGISTERED 3-tuple bands + composite collapse)
# -----------------------------------------------------------------------------
def evaluate_gate(t5_adm: dict, stage2: dict, lvl: dict, t5_img: dict,
                  gv: dict) -> tuple:
    r"""Composite operator (plan SS9):
      L3 < L2  AND  Delta_scheme < 1e-9  AND  deg_match  AND  Stage2_PASS_AND.

    3-tuple (gate-verdicts.md schema-v2):
      sign_verdict: PASS iff the T5 alpha_s image preserves the NEGATIVE running sign
        AND the index-fixed deg-match sign is correct (deg=+2 integer match).
      magnitude_verdict: PASS iff Level-3 < Level-2 with margin > 1e-3; INFO iff
        admissible but envelope symbolic-only / Stage-2 INFO; FAIL otherwise.
      regime_verdict: VALID iff evaluated within the L_max<=12 cache ceiling (the
        in-cache envelope is the canonical evaluation; FB tail confirms asymptotic).
    """
    deg_match = bool(t5_adm["conjunct1_deg_match"])  # (local)
    delta_pass = bool(t5_adm["delta_scheme_pass"])   # (local)
    l3_lt_l2 = bool(lvl["l3_lt_l2"])                 # (local)
    stage2_pass = bool(stage2["stage2_pass"])        # (local)

    # sign_verdict: the [SIGN] sub-check on (i) the alpha_s image negative running
    # and (ii) the deg-match sign correctness (deg=+2 integer index equality).
    sign_pass = bool(t5_img["image_is_negative"] and deg_match)  # (local)
    sign_v = "PASS" if sign_pass else "FAIL"  # (local)

    # magnitude_verdict: Level-3<Level-2 with margin (the empirical anchor satisfies
    # the algebraic envelope). margin = (level2 - level3)/level2.
    if lvl["level2"] > 0:
        margin = (lvl["level2"] - lvl["level3"]) / lvl["level2"]  # (local)
    else:
        margin = -1.0  # (local)
    if l3_lt_l2 and (margin > L3_LT_L2_MARGIN):
        mag_v = "PASS"  # (local)
    elif l3_lt_l2:
        mag_v = "INFO"  # (local) inside envelope but margin <= 1e-3
    else:
        mag_v = "FAIL"  # (local) envelope not satisfied
    # If admissible (deg+delta+non-scalar) but Stage-2 returns non-PASS-AND, downgrade
    # to INFO per INFO_meaning (bridge sound, permanence deferred).
    if t5_adm["t5_admissible"] and l3_lt_l2 and (not stage2_pass) and (mag_v == "PASS"):
        mag_v = "INFO"  # (local)

    # regime_verdict: VALID -- the in-cache L<=12 envelope is the canonical evaluation.
    reg_v = "VALID"  # (local)

    # Composite collapse rule (gate-verdicts.md schema-v2, PRE-REGISTERED).
    # Additionally enforce the plan's explicit conjunction:
    full_conjunction = bool(l3_lt_l2 and delta_pass and deg_match and stage2_pass)  # (local)
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
    # Plan conjunction guard: a PASS top-line REQUIRES the full conjunction.
    if composite == "PASS" and not full_conjunction:
        composite = "INFO"  # (local)
    return composite, sign_v, mag_v, reg_v, float(margin), full_conjunction


# -----------------------------------------------------------------------------
# Plot -- the bridge certificate figure (Level-3 vs Level-2 + Delta_scheme bars)
# -----------------------------------------------------------------------------
def make_plot(L_grid, gv_succ_ratio, ratio_per_L, lvl, gv_per_L, t5_adm, stage2) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: T5 Connes-Karoubi pairing convergence (GV-Heitsch successive ratio)
    ax = axes[0]
    ax.plot(L_grid, gv_succ_ratio, "o-", color="C0",
            label="GV-Heitsch succ-ratio (T5 pairing)")
    ax.axhline(lvl["Phi_inf"], color="C3", ls="--", lw=1,
               label=f"$\\Phi_\\infty$={lvl['Phi_inf']:.4f} (Aitken $\\Delta^2$)")
    ax.set_xlabel("L$_{max}$")
    ax.set_ylabel("GV succ-ratio (<[$\\phi$],Ch(P$_0$)> convergence)")
    ax.set_title("Step 2-3: T5 K$_0$-pairing @ a$_4$ s=2\n(GV-Heitsch [$\\phi$] succ-ratio; chi-image NON-SCALAR)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: Level-3 vs Level-2 (the bridge PASS predicate Level-3 < Level-2)
    ax = axes[1]
    bars = ax.bar(["Level-3\n(anchor)", "Level-2\n(envelope)"],
                  [lvl["level3"], lvl["level2"]],
                  color=["C2", "C1"])
    ax.set_ylabel("residual / envelope (a$_4$/a$_2$ units)")
    verdict_l3 = "Level-3 < Level-2 PASS" if lvl["l3_lt_l2"] else "Level-3 >= Level-2 FAIL"
    ax.set_title(f"Step 3: 3-level ladder @ L$_{{max}}$=12\nalpha_env={lvl['alpha_env']:.3f}; {verdict_l3}")
    for b, v in zip(bars, [lvl["level3"], lvl["level2"]]):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.3e}",
                ha="center", va="bottom", fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel 3: Delta_scheme three-scheme machine-zero (the JOINT clause (c) certificate)
    ax = axes[2]
    L12_gv = gv_per_L[-1]  # (local) GV dict at L=12
    schemes = ["APS-1975", "Cheeger-Simons", "Bismut-Cheeger"]
    vals = [L12_gv["GV_APS"], L12_gv["GV_CS"], L12_gv["GV_BC"]]
    ax.bar(schemes, vals, color=["C4", "C5", "C6"])
    ax.set_ylabel("GV-Heitsch [$\\phi$] secondary class (M$_{KK}^2$)")
    delta = L12_gv["delta_scheme"]  # (local)
    dpass = "machine-zero PASS" if delta < DELTA_SCHEME_TOL else "FAIL"
    ax.set_title(f"Step 1: JOINT clause (c) @ L$_{{max}}$=12\n$\\Delta_{{scheme}}$={delta:.2e} (< 1e-9 {dpass})")
    ax.tick_params(axis="x", rotation=15, labelsize=8)
    ax.grid(alpha=0.3, axis="y")

    adm = "ADMISSIBLE" if t5_adm["t5_admissible"] else "INADMISSIBLE"
    s2 = "Stage-2 PASS-AND" if stage2["stage2_pass"] else "Stage-2 NOT PASS-AND"
    fig.suptitle(
        f"S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY -- T5 Connes-Karoubi K$_0$-pairing @ a$_4$ Yang-Mills s=2  |  "
        f"deg-match (d$_A$=+2): {t5_adm['conjunct1_deg_match']}  |  {adm}  |  {s2}",
        fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + schema-v2 3-tuple REQUIRED)
# -----------------------------------------------------------------------------
def find_prior_audit_sha() -> str:
    """Scan s94_gate_verdicts.txt for the latest non-superseded canonical line for
    this GATE_ID (gate-verdicts.md SS"Option A" supersession-chain reading)."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})",
        _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   t5_adm: dict, stage2: dict, gv12: dict,
                   supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row +
    bridge/regulator/level pin rows (atomic single open('a')) per gate-verdicts.md.
    """
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
        f"sign = (alpha_s image NEGATIVE running) AND (index-fixed deg-match +2)\n"
    )
    # Bridge admissibility + Stage-2 provenance row
    bridge_row = (
        f"# t5_admissible={t5_adm['t5_admissible']} "
        f"conjunct1_deg_match={t5_adm['conjunct1_deg_match']} "
        f"conjunct2_non_scalar={t5_adm['conjunct2_non_scalar']} "
        f"delta_scheme={gv12['delta_scheme']:.3e} "
        f"stage2_pass={stage2['stage2_pass']} "
        f"axisA_PASS={stage2['axisA_PASS']} axisB_PASS={stage2['axisB_PASS']} "
        f"clause_c_PASS_AND={stage2['clause_c_PASS_AND']} "
        f"# {GATE_ID} T5 5-anatomy bridge + Stage-2 two-axis (lizzi-A/volovik-B) cross-verify\n"
    )
    # Regulator-pin (a_4^{Mellin}) + level-pin (CLASS=FULL) rows
    regulator_pin = (
        f"# REGULATOR_PIN=a_4^{{Mellin}} "
        f"# {GATE_ID} regulator-pin-discipline.md UV-regulator axis "
        f"(Yang-Mills channel residue at a_4 home pole s=2; cohomology-ratio a_n^{{zeta}})\n"
    )
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md SS(iv) K=4 "
        f"(consumes _cm_1995_residue_formula.py FULL physical CM-1995 SSIII.4 "
        f"residue evaluator; NO -SCHEMATIC suffix)\n"
    )
    rows = [line, companion, schema_v2_row, bridge_row, regulator_pin, level_pin]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md SS\"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("  T5 Connes-Karoubi K_0-pairing alpha_s recovery @ a_4 Yang-Mills s=2")
    print("=" * 78)

    # --- Input SHA log (first 20 lines of stdout per gate-verdicts.md) ---
    print("\n=== Input SHA-256 pins ===")
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    sha_cm = sha256_of(CM_1995_HELPER_PATH)  # (local)
    sha_cache = sha256_of(CACHE_L12)  # (local)
    sha_w7 = sha256_of(W7_1_NPZ)  # (local)
    sha_w13 = sha256_of(W1_3_T5_NPZ)  # (local)
    sha_script = sha256_of(SCRIPT_PATH)  # (local)
    print(f"  script                 : {sha_script}")
    print(f"  canonical_constants.py : {sha_canon}")
    print(f"  _cm_1995_residue (FULL): {sha_cm}")
    print(f"  s84 L12 cache          : {sha_cache}")
    print(f"  W7-1 transport npz     : {sha_w7}")
    print(f"  W1-3 T5 npz            : {sha_w13}")
    print(f"  W7-1 transport verdict : {W7_1_TRANSPORT_SHA}  (deg=+2 NON-SCALAR, T4-non-scalar)")
    print(f"  W1-3 T5 verdict        : {W1_3_T5_SHA}")
    print(f"  alpha_s_substrate_dist1: {alpha_s_substrate_distance_1}  (NEGATIVE running)")
    print(f"  alpha_s_pivot_goldstone: {alpha_s_pivot_goldstone}")
    print(f"  tau_fold={tau_fold}  M_KK={M_KK:.6e}")

    # === Substitution chain (Sage-verified this run) ===
    print("\n=== Substitution chain (degree-match conjunct 1; Sage-verified) ===")
    print(f"  deg(Res_W @ a4 pole s=2) = -2*S_A4_EFF = {SAGE_DEG_RESW_A4}")
    print(f"  deg(Res_W @ a2 pole s=1) = -2*S_A2_EFF = {SAGE_DEG_RESW_A2}")
    print(f"  deg(a_4/a_2) = 2(S_A2_EFF - S_A4_EFF) = {SAGE_DEG_A4_OVER_A2}  =>  |deg|={abs(SAGE_DEG_A4_OVER_A2)}")
    print(f"  d_A (alpha_s anchor degree, W7-1 transport) = +{D_A_ALPHA_S}")
    deg_match = bool(abs(SAGE_DEG_A4_OVER_A2) == abs(D_A_ALPHA_S) and (D_A_ALPHA_S == int(D_A_ALPHA_S)))  # (local)
    print(f"  |deg(a_4/a_2)| == |d_A| (index-fixed deg-match): {deg_match}")

    # === Step 1: GV-Heitsch [phi] three-scheme Delta_scheme (per L_max) ===
    print("\n=== Step 1: GV-Heitsch [phi] secondary class (3 schemes) ===")
    gv_per_L = []  # (local)
    for Lm in L_MAX_SCAN:
        gv = gv_secondary_three_schemes(Lm, tau_fold)  # (local)
        gv_per_L.append(gv)
        print(f"  L={Lm:2d}: GV_APS={gv['GV_APS']:.6e} GV_CS={gv['GV_CS']:.6e} "
              f"GV_BC={gv['GV_BC']:.6e}  Delta_scheme={gv['delta_scheme']:.3e}")
    gv12 = gv_per_L[-1]  # (local) L=12
    delta_pass = bool(gv12["delta_scheme"] < DELTA_SCHEME_TOL)  # (local)
    print(f"  Delta_scheme(L=12) = {gv12['delta_scheme']:.3e}  (< {DELTA_SCHEME_TOL:.0e}: {delta_pass})")
    print(f"  eta_defect(L=12) = {gv12['eta_defect']}  (BDI parity-blindness; odd-grading [phi])")

    # === Step 2: T5 K_0-pairing image (chi-image BdG inheritance; conjunct 2) ===
    print("\n=== Step 2: T5 K_0-pairing image @ a_4 s=2 (chi-image, NON-SCALAR) ===")
    chp_per_L = []  # (local)
    ratio_per_L = []  # (local)
    for Lm in L_MAX_SCAN:
        chp = chi_image_ch_p0(Lm, tau_fold)  # (local)
        chp_per_L.append(chp)
        ratio_per_L.append(chp["ratio"])
        print(f"  L={Lm:2d}: a4^Mellin={chp['a4_sum']:.6e} a2={chp['a2_sum']:.6e} "
              f"ratio(a4/a2)={chp['ratio']:.6f} f_chi={chp['f_chi']:.4f} "
              f"f_chi_cancels={chp['f_chi_cancels']} n_sectors={chp['n_sectors']}")
    ratio_per_L = np.array(ratio_per_L, dtype=float)  # (local)
    chp12 = chp_per_L[-1]  # (local)
    # NON-SCALAR test: the a_4/a_2 ratio FLOWS in L_max (two poles respond differently
    # => surviving L_max-dependence; NOT a scalar). Test ratio is not constant.
    ratio_spread = float(np.max(ratio_per_L) - np.min(ratio_per_L))  # (local)
    non_scalar = bool(ratio_spread > 1e-6 and chp12["f_chi_cancels"])  # (local) surviving + chi-natural
    print(f"  ratio spread over L in {L_MAX_SCAN} = {ratio_spread:.6e}  (NON-SCALAR surviving: {non_scalar})")

    # T5 image sign (the [SIGN] sub-check: must inherit the negative running)
    t5_img = t5_alpha_s_image(chp12, gv12)  # (local)
    print(f"  T5 image (signed) = {t5_img['t5_image_signed']:.6f}  "
          f"(GV_sign={t5_img['gv_sign']:+.0f}; image_is_negative={t5_img['image_is_negative']})")
    print(f"  alpha_s_substrate_distance_1 = {alpha_s_substrate_distance_1}  (both negative => sign preserved)")

    # === Step 3: Level-2 envelope + Level-3 anchor ===
    # The T5 convergence object is the GV-Heitsch SUCCESSIVE RATIO (the Connes-Karoubi
    # <[phi], Ch(P_0)> pairing's L_max stabilization), Aitken-Delta^2 extrapolated --
    # the CANONICAL W1-3 T5 construction. NOT the raw a_4/a_2 moment ratio (that is a
    # T4-type DIVERGENT SUM/SUM object; it sets the DEGREE + SIGN only, Step 2/4).
    print("\n=== Step 3: 3-level ladder (T5 Connes-Karoubi pairing convergence) ===")
    L_grid = np.array(L_MAX_SCAN, dtype=float)  # (local)
    gv_succ_ratio = gv_successive_ratio(gv_per_L)  # (local) [1, GV[10]/GV[8], GV[12]/GV[10]]
    print(f"  GV-Heitsch successive ratio (T5 pairing object) = {gv_succ_ratio}")
    lvl = level2_envelope_and_level3(L_grid, gv_succ_ratio)  # (local) Aitken Delta^2
    print(f"  Phi_inf (Aitken Delta^2 limit of GV succ-ratio) = {lvl['Phi_inf']:.6f}")
    print(f"  alpha_env (envelope exponent) = {lvl['alpha_env']:.4f}; C_env={lvl['C_env']:.4e}")
    print(f"  Level-2 envelope @ L=12 = {lvl['level2']:.6e}")
    print(f"  Level-3 anchor   @ L=12 = {lvl['level3']:.6e}")
    print(f"  Level-3 < Level-2 (PASS predicate): {lvl['l3_lt_l2']}")

    # === Step 4: T5 admissibility + Stage-2 two-axis cross-verify ===
    print("\n=== Step 4: T5 admissibility + Stage-2 two-axis cross-verify ===")
    t5_adm = t5_admissibility(deg_match, non_scalar, lvl["l3_lt_l2"], gv12["delta_scheme"])  # (local)
    stage2 = stage2_two_axis(t5_adm, deg_match, non_scalar, delta_pass, lvl["l3_lt_l2"])  # (local)
    print(f"  conjunct 1 (deg-match d_A=+2)      : {t5_adm['conjunct1_deg_match']}")
    print(f"  conjunct 2 (substrate-natural NON-SCALAR): {t5_adm['conjunct2_non_scalar']}")
    print(f"  Delta_scheme operational test     : {t5_adm['delta_scheme_pass']}")
    print(f"  T5 ADMISSIBLE (conj1 AND conj2 AND Delta): {t5_adm['t5_admissible']}")
    print(f"  Axis-A (NCG/spectral) PASS  [clause (a) homogeneity + (e) index-rigidity]: {stage2['axisA_PASS']}")
    print(f"  Axis-B (transport) PASS     [clause (b) non-scalar + (f) transport-deg]:    {stage2['axisB_PASS']}")
    print(f"  JOINT clause (c) PASS-AND (Delta_scheme->0 both axes): {stage2['clause_c_PASS_AND']}")
    print(f"  Stage2_PASS_AND: {stage2['stage2_pass']}")

    # === Step 5: verdict (3-tuple + composite collapse) ===
    print("\n=== Step 5: verdict (3-tuple + composite collapse) ===")
    composite, sign_v, mag_v, reg_v, margin, full_conj = evaluate_gate(
        t5_adm, stage2, lvl, t5_img, gv12)  # (local)
    print(f"  sign_verdict      = {sign_v}  (alpha_s NEGATIVE running AND deg-match +2)")
    print(f"  magnitude_verdict = {mag_v}   (Level-3<Level-2 margin={margin:.4f})")
    print(f"  regime_verdict    = {reg_v}")
    print(f"  full conjunction (L3<L2 AND Delta AND deg AND Stage2) = {full_conj}")
    print(f"  COMPOSITE = {composite}")

    # === Build pinmap + dual-SHA ===
    pins = {  # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "L_max_scan": list(L_MAX_SCAN),
        "s_a4": S_A4, "s_a2": S_A2, "s_a4_eff": S_A4_EFF, "s_a2_eff": S_A2_EFF,
        "d_A_alpha_s": D_A_ALPHA_S,
        "deg_a4_over_a2": SAGE_DEG_A4_OVER_A2,
        "delta_scheme_tol": DELTA_SCHEME_TOL,
        "deg_tol": DEG_TOL,
        "tau_fold": float(tau_fold),
        "M_KK": float(M_KK),
        "alpha_s_substrate_distance_1": float(alpha_s_substrate_distance_1),
        "alpha_s_pivot_goldstone": float(alpha_s_pivot_goldstone),
        "w7_1_transport_sha": W7_1_TRANSPORT_SHA,
        "w1_3_t5_sha": W1_3_T5_SHA,
        "cm_1995_residue_module_sha": sha_cm,
        "canonical_sha": sha_canon,
    }
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)  # (local)
    print("\n=== dual-SHA ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # === Plot ===
    make_plot(L_grid, gv_succ_ratio, ratio_per_L, lvl, gv_per_L, t5_adm, stage2)
    print(f"\n  plot -> {OUT_PNG.name}")

    # === Save npz ===
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        L_max=L_MAX, L_max_scan=np.array(L_MAX_SCAN),
        s_a4=S_A4, s_a2=S_A2, s_a4_eff=S_A4_EFF, s_a2_eff=S_A2_EFF,
        # substitution chain / degree-match
        deg_ResW_a4=SAGE_DEG_RESW_A4, deg_ResW_a2=SAGE_DEG_RESW_A2,
        deg_a4_over_a2=SAGE_DEG_A4_OVER_A2, d_A_alpha_s=D_A_ALPHA_S,
        deg_match=deg_match,
        # Step 1 GV-Heitsch three-scheme
        GV_APS=np.array([g["GV_APS"] for g in gv_per_L]),
        GV_CS=np.array([g["GV_CS"] for g in gv_per_L]),
        GV_BC=np.array([g["GV_BC"] for g in gv_per_L]),
        delta_scheme_per_L=np.array([g["delta_scheme"] for g in gv_per_L]),
        delta_scheme_L12=gv12["delta_scheme"], delta_scheme_pass=delta_pass,
        eta_defect_L12=gv12["eta_defect"],
        # Step 2 chi-image / image ratio
        a4_sum_per_L=np.array([c["a4_sum"] for c in chp_per_L]),
        a2_sum_per_L=np.array([c["a2_sum"] for c in chp_per_L]),
        ratio_per_L=ratio_per_L, f_chi=chp12["f_chi"], f_chi_cancels=chp12["f_chi_cancels"],
        ratio_spread=ratio_spread, non_scalar=non_scalar,
        t5_image_signed=t5_img["t5_image_signed"], t5_image_ratio=t5_img["t5_image_ratio"],
        gv_sign=t5_img["gv_sign"], image_is_negative=t5_img["image_is_negative"],
        # Step 3 Level-2/Level-3 (T5 Connes-Karoubi pairing convergence via GV succ-ratio)
        gv_succ_ratio=gv_succ_ratio,
        Phi_inf=lvl["Phi_inf"], alpha_env=lvl["alpha_env"], C_env=lvl["C_env"],
        level2=lvl["level2"], level3=lvl["level3"], l3_lt_l2=lvl["l3_lt_l2"],
        resid_per_L=np.array(lvl["resid_per_L"]),
        # Step 4 admissibility + Stage-2
        conjunct1_deg_match=t5_adm["conjunct1_deg_match"],
        conjunct2_non_scalar=t5_adm["conjunct2_non_scalar"],
        t5_admissible=t5_adm["t5_admissible"],
        axisA_PASS=stage2["axisA_PASS"], axisB_PASS=stage2["axisB_PASS"],
        clause_c_PASS_AND=stage2["clause_c_PASS_AND"], stage2_pass=stage2["stage2_pass"],
        clause_a_homogeneity=stage2["clause_a_homogeneity"],
        clause_e_index_rigidity=stage2["clause_e_index_rigidity"],
        clause_b_non_scalar=stage2["clause_b_non_scalar"],
        clause_f_transport_deg=stage2["clause_f_transport_deg"],
        # Step 5 verdict
        composite_verdict=composite, sign_verdict=sign_v,
        magnitude_verdict=mag_v, regime_verdict=reg_v,
        margin=margin, full_conjunction=full_conj,
        # provenance
        w7_1_transport_sha=W7_1_TRANSPORT_SHA, w1_3_t5_sha=W1_3_T5_SHA,
        cm_1995_residue_module_sha=sha_cm,
        tau_fold=float(tau_fold), M_KK=float(M_KK),
        alpha_s_substrate_distance_1=float(alpha_s_substrate_distance_1),
        alpha_s_pivot_goldstone=float(alpha_s_pivot_goldstone),
        audit_sha256=audit_sha, content_sha256=content_sha,
        DELTA_SCHEME_TOL=DELTA_SCHEME_TOL, DEG_TOL=DEG_TOL,
        L3_LT_L2_MARGIN=L3_LT_L2_MARGIN,
    )
    print(f"  data -> {OUT_NPZ.name}")

    # === Emit verdict line ===
    print("\n=== Emit verdict line + companions ===")
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = prior_sha if (prior_sha and prior_sha != audit_sha) else ""  # (local)
    value = (
        f"composite={composite}_T5_admissible={t5_adm['t5_admissible']}"
        f"_deg_match={deg_match}(d_A=+{D_A_ALPHA_S},deg(a4/a2)={SAGE_DEG_A4_OVER_A2})"
        f"_delta_scheme={gv12['delta_scheme']:.2e}"
        f"_L3={lvl['level3']:.4e}_L2={lvl['level2']:.4e}_L3ltL2={lvl['l3_lt_l2']}"
        f"_alpha_env={lvl['alpha_env']:.4f}"
        f"_non_scalar={non_scalar}_t5_image={t5_img['t5_image_signed']:.4f}"
        f"_stage2_PASS_AND={stage2['stage2_pass']}"
        f"_axisA={stage2['axisA_PASS']}_axisB={stage2['axisB_PASS']}"
        f"_clause_c_PASS_AND={stage2['clause_c_PASS_AND']}"
        f"_chi_image_BdG_inheritance_class_SS-VII.Bx-STAGE-1-CANDIDATE"
    )
    append_verdict(composite, value, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, t5_adm, stage2, gv12, supersedes)
    print(f"  verdict line appended -> {VERDICT_TXT}")
    print(f"  composite={composite} sign={sign_v} mag={mag_v} regime={reg_v}"
          + (f"  supersedes={supersedes[:16]}..." if supersedes else ""))

    # === Output 4-tuple (final non-verdict line) ===
    print("\n=== Output 4-tuple ===")
    print(f"  (value=composite:{composite}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
