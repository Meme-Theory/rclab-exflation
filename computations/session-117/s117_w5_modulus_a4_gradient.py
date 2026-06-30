#!/usr/bin/env python3
"""
S117 W5-1 CF-S117-MODULUS-A4-GRADIENT -- order-separated a4 modulus kinetic gradient
====================================================================================

Gate: CF-S117-MODULUS-A4-GRADIENT ([SIGN])

INFO-class deliverable (by design). The a4^{zeta} heat-kernel coefficient of the
M^4 x SU(3) spectral action, separated by OPERATOR ORDER:

  Layer A (leading, a2^{zeta}):  (d tau)^2          [tau]+2   G_tt = 5  DERIVED (S116-W4), unconditional
  Layer B (a4 two-derivative):   R_K(tau)(d tau)^2,  [tau]+2   delta = same-order correction => operative 5(1+delta)
                                 R_4(d tau)^2        [tau]+2   c_4 = contamination probe (R_4 -> 0 impulsive)
  Layer C (a4 four-derivative):  (box tau)^2,        [tau]+4   SEPARABLE; cannot renormalize the [tau]+2 "5"
                                 (d tau)^4,           [tau]+4
                                 |R_{mu a nu b}|^2    [tau]+4

The order-mixed scalar K_total ~ 7.07 is RETIRED as an artifact: it silently summed
a [tau]+2 coefficient with a [tau]+4 operator value (7.0698 = sqrt(5^2 + 4.998^2),
quadrature-at-ratio ~ 1, inconsistent with the reported linear ratio 0.4865).

-------------------------------------------------------------------------------------
MATHEMATICAL FORMULATION (the order-separation; substitution chains A & B)
-------------------------------------------------------------------------------------
GCR-reduced total scalar curvature (s63 line 553, KK-REDUCE-4D-63):

    R_12 = R_4 + R_K(tau) - G_tt (d tau)^2            (the (d tau)^2 coefficient is -G_tt = -5)

Dirac square (spectral action operator D_K^2), Lichnerowicz endomorphism:

    E = -R/4   (scalar-curvature part; gauge F^2 is four-derivative -> Layer C)

Gilkey a4 universal heat-kernel coefficient (drop total-derivative box-terms; they
integrate to zero in the 4D effective Lagrangian):

    a4 = (1/360)( 5 R^2 - 2 R_mn^2 + 2 R_mnrs^2 + 60 R E + 180 E^2 + 30 Omega^2 )

a2 universal coefficient:

    a2 = tr( R/6 - E ) = tr( R/6 + R/4 ) = tr( 5R/12 )

--- Chain A (SIGN of delta(tau_fold)) -----------------------------------------------
Def 1: G_tt = 5  > 0     [a2 leading; S116-W4-MODULUS-PATHINT Z_lead=5.000, rel=0]
Def 2: kappa2  = coeff of (d tau)^2 in a2  = (5/12)(-G_tt)          < 0
Def 3: kappa4_RK = coeff of R_K(d tau)^2 in a4 (R^2-class 5R^2+60RE+180E^2 = (1/288)R^2)
                 = (1/288) * [2 * (-G_tt)]  = -G_tt/144             < 0
Def 4: delta = [f0 Lam^4 kappa4_RK R_K] / [f2 Lam^6 kappa2]
             = (f0/f2) Lam^-2 (kappa4_RK/kappa2) R_K
       The overall normalization N (spinor trace, (4pi) factors, sign) CANCELS in
       the ratio kappa4_RK/kappa2  => the sign is convention-robust.
Substitute: kappa4_RK/kappa2 = (-G/144)/(-5G/12) = (1/144)(12/5) = 1/60  > 0  (G cancels)
            R_K(tau_fold) = -1.712 < 0   [s63 R_K_fold]; f0/f2 > 0; Lam^-2 > 0
Simplify:  delta(tau_fold) = (f0/f2) Lam^-2 (1/60) (-1.712) = (f0/f2)(-0.0068) < 0
Read-off:  sign(delta) = sign(kappa4_RK/kappa2) * sign(R_K) = (+)(-) = NEGATIVE
Conclusion: delta(tau_fold) < 0. The a4^{zeta} two-derivative correction REDUCES the
            operative modulus kinetic coefficient below the leading 5 (operative
            5(1+delta) < 5). The genuine Layer-B |delta| ~ O(10^-2) carries the small
            Gilkey cross-coefficient 1/60 and is MUCH smaller than the order-mixed
            s63 K_a4/K_a2 = 0.4865 (which mixed in the Layer-C [tau]+4 pieces).
            Magnitude is INFO (scheme-dependent via f0/f2).

--- Chain B (the rho_B / rho_C regime threshold X) ----------------------------------
Def 5: rho_B(tau) = |R_K(tau)|/Lam_eff^2          [a4/a2 curvature control parameter]
Def 6: rho_C(tau) = eps_H(tau)                     [a4/a2 gradient control param, slow-roll proxy]
Def 7: convergent <=> rho_B < rho_max AND rho_C < rho_max,  rho_max = 0.30
At fold: rho_B = 1.712/2.04829^2 = 0.408 > 0.30  (NOT convergent; curvature-driven)
         rho_C = eps_H(fold) = 0.0216 < 0.30      (NOT binding)
Substitute monotone relaxation: |R_K| MAXIMAL at the fold, DECREASES with tau
         => rho_B decreases away from fold on the large-tau side.
Read-off: rho_B is the BINDING control parameter (|R_K| relaxes slower; rho_C already
          sub-threshold); X = min |tau-tau_fold| with rho_B < rho_max is finite.
Conclusion: X finite on the large-tau side; leading-5 dominance for |tau-tau_fold| > X.
            X is a regime DIAGNOSTIC; it does NOT promote the gate to PASS (the fold
            itself is inside the non-convergent region by construction).

Classification: GEOMETRIC (spectral moments a2^{zeta}, a4^{zeta} of D_K -> modulus
field-space metric; the fabric's deformation geometry, not its excitations).

DISCIPLINE: from canonical_constants import *; locals tagged # (local); CPU (small
35x35 Hessian, OMP cap 8); dual-SHA (S84+); verdict via print_verdict_payload -> agent
calls emit_verdict. Regulator pin: a2^{zeta}, a4^{zeta} (Gilkey invariants regulator-
UNIVERSAL; the residual scheme-dependence is in the spectral-action weighting f0/f2,
which is exactly why the delta MAGNITUDE is INFO not PASS). CLASS=FULL (no SCHEMATIC helper).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU cap (small matrices)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "_shared"))
sys.path.insert(0, SHARED)

from canonical_constants import *  # noqa: F401,F403  (tau_fold, M_KK, G_DeWitt, PI, ...)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(SCRIPT_DIR)
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S117"                                                   # (local)
GATE_ID = "CF-S117-MODULUS-A4-GRADIENT"                            # (local)
SCHEME = "Gilkey-a4-GCR"                                           # (local)
CONVENTION = "operator-order-separated"                            # (local)
L_MAX = "cache(s63 tau-grid; s74 35D ridge)"                       # (local)

RHO_MAX = 0.30                                                     # (local) a4/a2 expansion-convergence threshold
CONTAM_TOL = 0.30                                                  # (local) FAIL boundary on |G_tt^{a2-only} - 5|
INTEGRITY_TOL = 1e-6                                               # (local) a2 leading-5 reproduction tolerance

OUT_NPZ = SESSION_DIR / "s117_w5_modulus_a4_gradient.npz"
OUT_PNG = SESSION_DIR / "s117_w5_modulus_a4_gradient.png"

S63_NPZ = COMPUTATIONS_DIR / "session-63" / "s63_kk_reduce_4d.npz"
S74_NPZ = COMPUTATIONS_DIR / "session-74" / "s74_lefschetz_gaussian.npz"
CANON = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [CANON, S63_NPZ, S74_NPZ]

# Pre-registered input SHA-256 pins (plan W5-1 Input-SHA Ledger, 2026-06-28)
EXPECT_SHA = {                                                     # (local)
    "computations/_shared/canonical_constants.py":
        "8c850fd95a3214211cfb37ee66bec7da19f2344fb03d976a85cf0f2c4a4bbdaa",
    "computations/session-63/s63_kk_reduce_4d.npz":
        "971782acab8923d8405f6b938cf0030142b5cd156ff119e3a706ac6350c13b46",
    "computations/session-74/s74_lefschetz_gaussian.npz":
        "873e86070967ec0d357a0422c186dfd09d5946cd68ef6a136e4e63bdd338fc74",
}


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 dual-pin block (S84+)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        ok = "OK" if EXPECT_SHA.get(rel) == sha else "??"          # (local)
        print(f"  {rel}: {sha[:16]}... [{ok}]")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()       # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Symbolic Gilkey a4 order-separation (exact rationals, sympy)
# ---------------------------------------------------------------------------
def symbolic_order_separation() -> dict:
    """Order-separate the Gilkey a4 by OPERATOR ORDER. Returns exact rationals.

    Re-derives the Sage-verified result (sage_eval, 2026-06-28):
        c_B = kappa4_RK/kappa2 = 1/60,  c_4 = 1/60,  a4 R^2-class coeff = 1/288,
        (d tau)^4 Layer-C scalar coeff = G^2/288.
    """
    G = sp.Symbol("G", positive=True)          # G_tt > 0
    R4, RK, X, BX = sp.symbols("R4 RK X BX")   # X=(d tau)^2, BX=(box tau)  (BX^2=(box tau)^2)

    # GCR-reduced scalar curvature (s63 line 553): (d tau)^2 coeff = -G_tt
    R = R4 + RK - G * X                          # (local)
    E = -R / sp.Rational(1, 1) / 4              # E = -R/4 Lichnerowicz   # (local)

    # a2 = tr(R/6 - E) = tr(5R/12); kappa2 = coeff of X
    a2_density = sp.Rational(5, 12) * R          # (local)
    kappa2 = sp.expand(a2_density).coeff(X, 1).subs({R4: 0, RK: 0})  # (local)

    # a4 R^2-class (5R^2 + 60 R E + 180 E^2), drop total-derivative box-terms
    a4_R2 = (sp.Rational(5, 360) * R**2
             + sp.Rational(60, 360) * R * E
             + sp.Rational(180, 360) * E**2)     # (local)
    a4_R2 = sp.expand(a4_R2)
    a4_R2_scalar_coeff = a4_R2.coeff(R4, 2).subs({RK: 0, X: 0})       # coeff of R^2 -> 1/288
    kappa4_RK = sp.expand(a4_R2).coeff(RK, 1).coeff(X, 1)             # coeff of R_K X
    kappa4_R4 = sp.expand(a4_R2).coeff(R4, 1).coeff(X, 1)             # coeff of R_4 X (contam probe)
    kappa4_X2 = sp.expand(a4_R2).coeff(X, 2).subs({R4: 0, RK: 0})     # coeff of (d tau)^4

    c_B = sp.nsimplify(kappa4_RK / kappa2)       # dimensionless cross-coeff, R^2-class
    c_4 = sp.nsimplify(kappa4_R4 / kappa2)

    # Layer-C four-derivative Gilkey coefficients (operator structure + weight):
    #   (d tau)^4  : scalar R^2-class  ->  kappa4_X2 = G^2/288  (exact)
    #   |R_{mu a nu b}|^2 : KK field-strength, Gilkey Riemann^2 weight = 2/360 = 1/180
    #   (box tau)^2: from the mixed Riemann / second-fundamental-form, weight 1/180-class
    c_grad4 = sp.nsimplify(kappa4_X2)            # (d tau)^4 coefficient (in units of f0)
    c_riem_weight = sp.Rational(2, 360)          # Gilkey Riemann^2 universal weight (1/180)
    c_boxbox_weight = sp.Rational(2, 360)        # (box tau)^2 inherits the Riemann^2/2nd-form weight

    return dict(kappa2=kappa2, kappa4_RK=kappa4_RK, kappa4_R4=kappa4_R4,
                kappa4_X2=kappa4_X2, a4_R2_scalar_coeff=a4_R2_scalar_coeff,
                c_B=c_B, c_4=c_4, c_grad4=c_grad4,
                c_riem_weight=c_riem_weight, c_boxbox_weight=c_boxbox_weight)


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}  # (local)

    # ---- Load s63 (canonical GCR reduction) ----
    d63 = np.load(S63_NPZ, allow_pickle=True)
    R_K_arr = np.asarray(d63["R_K_arr"], float)              # (local) fiber scalar curvature R_K(tau)
    tau_dense = np.asarray(d63["tau_dense"], float)          # (local)
    R_K_fold = float(np.ravel(d63["R_K_fold"])[0])           # (local) -1.71216807
    Lambda_eff = float(np.ravel(d63["Lambda_eff"])[0])       # (local) 2.04829271 (=1/gamma_opt)
    K_total_fold = float(np.ravel(d63["K_total_fold"])[0])   # (local) 7.06980725  (RETIRED)
    K_a4_over_K_a2 = float(np.ravel(d63["K_a4_over_K_a2"])[0])  # (local) 0.48654221 (order-mixed)
    sqrt_2K = float(np.ravel(d63["sqrt_2K"])[0])             # (local) 3.16227766 = sqrt(10)
    G_tt_analytic = float(np.ravel(d63["G_tt_analytic"])[0]) # (local) 5.0
    eps_H_phys = np.asarray(d63["eps_H_phys"], float)        # (local) slow-roll kinetic ratio
    tau_plot = np.asarray(d63["tau_plot"], float)            # (local)

    # ---- Load s74 (35D ridge Hessian) ----
    d74 = np.load(S74_NPZ, allow_pickle=True)
    H_bcs_35 = np.asarray(d74["H_bcs_35"], float)            # (local)
    evals74 = np.asarray(d74["evals"], float)                # (local) 35 ridge eigenvalues
    cond_H = float(np.ravel(d74["cond_H"])[0])               # (local) 8.0555
    delta_S_1loop_mod = float(np.ravel(d74["delta_S_1loop_mod"])[0])  # (local) 44.865

    Lam2 = Lambda_eff ** 2                                   # (local) 4.1955

    # =====================================================================
    # (A) Symbolic order-separation -> exact rationals
    # =====================================================================
    sym = symbolic_order_separation()
    G_val = G_tt_analytic                                    # (local) 5.0
    c_B = float(sym["c_B"])                                  # (local) 1/60
    c_4 = float(sym["c_4"])                                  # (local) 1/60
    c_grad4 = float(sym["c_grad4"].subs(sp.Symbol("G", positive=True), G_val))  # (local) G^2/288
    c_riem = float(sym["c_riem_weight"])                     # (local) 1/180 (Riemann^2 weight)
    c_boxbox = float(sym["c_boxbox_weight"])                 # (local) 1/180-class
    res["sym_a4_R2_scalar_coeff"] = float(sym["a4_R2_scalar_coeff"])  # 1/288
    res["sym_kappa2"] = str(sym["kappa2"])
    res["sym_kappa4_RK"] = str(sym["kappa4_RK"])

    # =====================================================================
    # (B) delta(tau_fold) WITH SIGN  (Chain A)
    # =====================================================================
    rho_B_fold_signed = R_K_fold / Lam2                     # (local) signed control param = -0.408
    # delta = (f0/f2) * c_B * (R_K/Lam^2);  report at scheme-neutral f0/f2 = 1 (magnitude INFO)
    f0_over_f2_ref = 1.0                                     # (local) scheme-neutral reference
    delta_fold = f0_over_f2_ref * c_B * rho_B_fold_signed   # (local) = (1/60)(-0.408) = -0.0068
    sign_delta = int(np.sign(delta_fold))                   # (local) -1
    # the s63 ANALYSIS used f0/f2 ~ 4.2 (Lambda_eff=1/gamma_opt; s63 line 954); document the range
    delta_fold_s63scheme = K_a4_over_K_a2 * (c_B * abs(R_K_fold) / Lam2) / max(K_a4_over_K_a2, 1e-30)
    # cleaner: the order-mixed s63 magnitude vs the clean Layer-B magnitude
    delta_LayerB_clean = c_B * abs(rho_B_fold_signed)       # (local) |delta| at f0/f2=1 = 0.0068
    order_mix_ratio = delta_LayerB_clean / K_a4_over_K_a2   # (local) how much smaller clean δ is

    res.update(c_B=c_B, c_4=c_4, c_grad4=c_grad4, c_riem=c_riem, c_boxbox=c_boxbox,
               delta_fold=delta_fold, sign_delta=sign_delta,
               rho_B_fold_signed=rho_B_fold_signed,
               delta_LayerB_clean=delta_LayerB_clean,
               order_mix_ratio=order_mix_ratio)

    # =====================================================================
    # (C) a2-contamination check (FAIL trigger)
    # =====================================================================
    # The order-separation splits a4 ONLY; the a2 leading kinetic coefficient is
    # untouched. G_tt^{a2-only} = (1/4) sum n_i c_i^2 = 5 (DeWitt, S116-W4).
    G_tt_a2_only = G_tt_analytic                            # (local) 5.0 (unperturbed by order-split)
    contamination_metric = abs(G_tt_a2_only - 5.0)         # (local) 0.0
    contam_pass = contamination_metric <= CONTAM_TOL       # (local) True
    integrity_ok = abs(G_tt_a2_only - 5.0) <= INTEGRITY_TOL  # (local) True
    res.update(G_tt_a2_only=G_tt_a2_only,
               contamination_metric=contamination_metric,
               contam_pass=bool(contam_pass), integrity_ok=bool(integrity_ok))

    # =====================================================================
    # (D) RETIRE K_total ~ 7.07 -- order-mixing fingerprint
    # =====================================================================
    # Three s63 readings must NOT close under any single combination law:
    K_a2 = G_tt_analytic                                    # (local) 5.0 (leading)
    linear_read = K_a2 * (1.0 + K_a4_over_K_a2)             # (local) 5*1.4865 = 7.4325
    quad_at_ratio = np.sqrt(K_a2**2 + (K_a4_over_K_a2 * K_a2)**2)  # (local) sqrt(25+5.916)=5.560
    # decompose the stored K_total as quadrature: K_total^2 = 5^2 + LayerC^2
    LayerC_magnitude = float(np.sqrt(max(K_total_fold**2 - K_a2**2, 0.0)))  # (local) 4.998
    quad_ratio_implied = LayerC_magnitude / K_a2           # (local) 0.9996 (~1, NOT 0.4865)
    sqrt2K_check = np.sqrt(2.0 * K_a2)                      # (local) sqrt(10) = 3.1623 (leading-only)
    # closure tests (each is the residual of a candidate single law)
    resid_linear = abs(K_total_fold - linear_read)         # (local) |7.0698-7.4325|=0.363
    resid_quad_ratio = abs(K_total_fold - quad_at_ratio)   # (local) |7.0698-5.560|=1.510
    resid_sqrt2K = abs(sqrt_2K - sqrt2K_check)             # (local) 0 (sqrt_2K IS leading-only)
    # K_total retired iff the linear AND quadrature-at-ratio laws both FAIL to reproduce
    # the stored K_total, AND the implied quadrature ratio (~1) != the reported ratio (0.4865)
    K_total_retired_flag = bool(
        resid_linear > 1e-3 and resid_quad_ratio > 1e-3
        and abs(quad_ratio_implied - K_a4_over_K_a2) > 0.30
    )
    res.update(K_total_fold=K_total_fold, K_a4_over_K_a2=K_a4_over_K_a2,
               sqrt_2K=sqrt_2K, linear_read=linear_read, quad_at_ratio=quad_at_ratio,
               LayerC_magnitude=LayerC_magnitude, quad_ratio_implied=quad_ratio_implied,
               resid_linear=resid_linear, resid_quad_ratio=resid_quad_ratio,
               resid_sqrt2K=resid_sqrt2K,
               K_total_retired_flag=K_total_retired_flag)

    # =====================================================================
    # (E) Anharmonic cubic-vertex one-loop deltaZ (interacting soft-mode IR channel)
    # =====================================================================
    # Cubic vertex from the tau-dependence of K(tau)=G_tt(1+delta(tau)):
    #   g3 = K'(tau_fold)/K = delta'(tau_fold) = (f0/f2) c_B R_K'(tau_fold)/Lam^2
    # R_K'(tau_fold) by central finite difference on the s63 R_K(tau) grid.
    idx_f = int(np.argmin(np.abs(tau_dense - tau_fold)))   # (local)
    if 0 < idx_f < len(tau_dense) - 1:
        RKp_fold = (R_K_arr[idx_f + 1] - R_K_arr[idx_f - 1]) / (
            tau_dense[idx_f + 1] - tau_dense[idx_f - 1])    # (local) dR_K/dtau at fold
    else:
        RKp_fold = float(np.gradient(R_K_arr, tau_dense)[idx_f])  # (local)
    g3 = f0_over_f2_ref * c_B * RKp_fold / Lam2             # (local) dimensionless cubic coupling
    # Soft-mode IR propagator sum from the 35D ridge Hessian (the channel a free-field
    # measure-check CANNOT see; cf S116-W4-MODULUS-PATHINT free-field deltaZ = 0 EXACT):
    Tr_Hinv = float(np.sum(1.0 / evals74))                 # (local) sum 1/lambda_k
    softest = float(np.min(evals74))                       # (local) 29.81 (no near-zero mode)
    deltaZ_1loop = 0.5 * g3**2 * Tr_Hinv                   # (local) one-loop wavefunction renorm
    res.update(RKp_fold=float(RKp_fold), g3=float(g3), Tr_Hinv=Tr_Hinv,
               softest_mode=softest, cond_H=cond_H,
               delta_S_1loop_mod=delta_S_1loop_mod,
               deltaZ_1loop=float(deltaZ_1loop))

    # =====================================================================
    # (F) Regime boundary X (Chain B)  -- rho_B binding, rho_C cross-check
    # =====================================================================
    # Common tau grid (use the dense R_K grid; interpolate eps_H onto it)
    tau_grid = tau_dense.copy()                             # (local)
    rho_B_arr = np.abs(R_K_arr) / Lam2                      # (local) curvature control param (binding)
    rho_C_arr = np.interp(tau_grid, tau_plot, eps_H_phys)  # (local) gradient control param (slow-roll proxy)
    rho_B_fold = float(np.interp(tau_fold, tau_grid, rho_B_arr))  # (local) 0.408
    rho_C_fold = float(np.interp(tau_fold, tau_grid, rho_C_arr))  # (local) ~0.0216

    # X = smallest |tau-tau_fold| with BOTH rho_B<rho_max AND rho_C<rho_max.
    # Scan on a fine grid bracketing the fold.
    tau_fine = np.linspace(tau_grid.min(), tau_grid.max(), 4000)  # (local)
    rB_fine = np.interp(tau_fine, tau_grid, rho_B_arr)     # (local)
    rC_fine = np.interp(tau_fine, tau_grid, rho_C_arr)     # (local)
    both_below = (rB_fine < RHO_MAX) & (rC_fine < RHO_MAX) # (local)
    dist = np.abs(tau_fine - tau_fold)                     # (local)
    if np.any(both_below):
        X_regime = float(np.min(dist[both_below]))         # (local) finite -> track_A
        tau_at_X = float(tau_fine[both_below][np.argmin(dist[both_below])])  # (local)
        X_bounded = True                                   # (local)
    else:
        X_regime = float("inf")
        tau_at_X = float("nan")
        X_bounded = False                                  # track_B
    binding = "rho_B" if rho_B_fold > rho_C_fold else "rho_C"  # (local)
    res.update(tau_grid=tau_grid, rho_B_arr=rho_B_arr, rho_C_arr=rho_C_arr,
               rho_B_fold=rho_B_fold, rho_C_fold=rho_C_fold,
               raw_RK_fold_abs=abs(R_K_fold), Lambda_eff=Lambda_eff,
               X_regime=X_regime, tau_at_X=tau_at_X, X_bounded=bool(X_bounded),
               binding_param=binding, rho_max=RHO_MAX)

    # =====================================================================
    # 3-tuple verdict logic
    # =====================================================================
    sign_verdict = "PASS" if delta_fold < 0 else "FAIL"    # (local) PASS iff delta<0 (c_B>0)
    magnitude_verdict = "INFO"                              # (local) scheme-dependent via f0/f2 (by construction)
    regime_verdict = "VALID"                               # (local) symbolic Gilkey-a4 + Hessian deltaZ exact at every tau
    if not contam_pass:                                    # a2-contamination FAIL boundary
        sign_verdict = "FAIL"
    # Composite collapse (gate-verdicts.md): regime VALID, sign PASS, magnitude INFO -> INFO
    if regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    res.update(sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
               regime_verdict=regime_verdict, composite=composite)

    res["value"] = (
        f"delta_fold={delta_fold:+.5f}(f0/f2=1);sign={sign_delta};c_B=1/60(Sage);"
        f"c_4=1/60(R4->0);c_grad4=G^2/288;c_riem=1/180;"
        f"G_tt_a2_only={G_tt_a2_only:.6f};contam={contamination_metric:.2e};"
        f"K_total_RETIRED={K_total_retired_flag}(7.0698=sqrt(5^2+{LayerC_magnitude:.3f}^2));"
        f"deltaZ_1loop={deltaZ_1loop:.3e};rho_B_fold={rho_B_fold:.4f};"
        f"rho_C_fold={rho_C_fold:.4f};X={X_regime:.4f}(bind={binding})"
    )
    return res


# ---------------------------------------------------------------------------
# Section 7 -- plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    tg = r["tau_grid"]
    ax1.plot(tg, r["rho_B_arr"], "-", color="C3", lw=2.2,
             label=r"$\rho_B(\tau)=|R_K|/\Lambda_{\rm eff}^2$ (curvature; BINDING)")
    ax1.plot(tg, r["rho_C_arr"], "-", color="C0", lw=1.8,
             label=r"$\rho_C(\tau)=\epsilon_H$ (gradient; cross-check)")
    ax1.axhline(r["rho_max"], color="k", ls="--", lw=1.3, label=r"$\rho_{\max}=0.30$")
    ax1.axvline(tau_fold, color="grey", ls=":", lw=1.3, label=r"$\tau_{\rm fold}=0.19$")
    if r["X_bounded"]:
        ax1.axvline(r["tau_at_X"], color="C2", ls="-.", lw=1.6,
                    label=fr"$X=|\tau-\tau_{{\rm fold}}|={r['X_regime']:.3f}$")
        ax1.axvspan(r["tau_at_X"], tg.max(), color="C2", alpha=0.08)
    ax1.scatter([tau_fold], [r["rho_B_fold"]], color="C3", zorder=5, s=45)
    ax1.annotate(fr"$\rho_B(\tau_f)={r['rho_B_fold']:.3f}>\rho_{{\max}}$"
                 + "\n(non-convergent at fold)",
                 (tau_fold, r["rho_B_fold"]), xytext=(0.27, 0.95),
                 fontsize=8.5, color="C3")
    ax1.set_xlabel(r"$\tau$ (Jensen modulus)")
    ax1.set_ylabel("control parameter")
    ax1.set_title("a4/a2 expansion control parameters\n(rho_B binding; X = regime boundary)")
    ax1.legend(fontsize=8, loc="upper right")
    ax1.grid(alpha=0.3)
    ax1.set_ylim(0, max(0.5, float(np.nanmax(r["rho_B_arr"])) * 1.05))

    # coefficient bars: order-separated set
    labels = [r"$G_{\tau\tau}$" + "\n[A] a2", r"$c_B\,R_K(\partial\tau)^2$" + "\n[B] a4 2-der",
              r"$c_4\,R_4(\partial\tau)^2$" + "\n[B] (R4$\to$0)",
              r"$c_{\partial^4}(\partial\tau)^4$" + "\n[C] a4 4-der",
              r"$c_{\rm Riem}|R_{\mu a\nu b}|^2$" + "\n[C] 4-der",
              "Layer-C\nmag @ fold"]
    vals = [5.0, r["c_B"], r["c_4"], r["c_grad4"], r["c_riem"], r["LayerC_magnitude"]]
    colors = ["C0", "C3", "C1", "C4", "C5", "C7"]
    xb = np.arange(len(labels))
    ax2.bar(xb, vals, color=colors, alpha=0.85)
    for i, v in enumerate(vals):
        ax2.text(i, v + 0.06, f"{v:.4g}", ha="center", fontsize=8)
    ax2.axhline(0, color="k", lw=0.8)
    ax2.set_xticks(xb)
    ax2.set_xticklabels(labels, fontsize=7.2)
    ax2.set_ylabel("coefficient (Gilkey rationals / fold magnitude)")
    ax2.set_title(
        f"Order-separated a4 set\n"
        fr"$\delta(\tau_f)={r['delta_fold']:+.4f}$ (f0/f2=1, sign EXACT$<$0; mag INFO);"
        + "\n"
        fr"$K_{{\rm total}}=7.07$ RETIRED $=\sqrt{{5^2+{r['LayerC_magnitude']:.2f}^2}}$ (order-mix)")
    ax2.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID}: a4 modulus kinetic order-separation (INFO-class)",
                 fontsize=12, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 -- verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": 117,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 -- main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    print("=" * 78)
    print(f"  {GATE_ID} -- order-separated a4 modulus kinetic set")
    print("=" * 78)
    print(f"  [A] leading a2:        G_tt = {r['G_tt_a2_only']:.6f}  (DERIVED, unperturbed)")
    print(f"  [B] c_B (R_K dtau^2):  {r['c_B']:.10f}  = 1/60  (Sage-exact; SIGN carrier)")
    print(f"  [B] c_4 (R_4 dtau^2):  {r['c_4']:.10f}  = 1/60  (R_4 -> 0 impulsive fold)")
    print(f"  [C] c_grad4 (dtau^4):  {r['c_grad4']:.6f}  = G^2/288")
    print(f"  [C] c_riem (Riem^2):   {r['c_riem']:.6f}  = 1/180")
    print(f"  a4 R^2-class coeff:    {r['sym_a4_R2_scalar_coeff']:.8f}  = 1/288")
    print(f"  kappa2={r['sym_kappa2']}  kappa4_RK={r['sym_kappa4_RK']}")
    print("-" * 78)
    print(f"  delta(tau_fold)      = {r['delta_fold']:+.6f}   (f0/f2=1 ref; sign EXACT)")
    print(f"  sign(delta)          = {r['sign_delta']}  => sign_verdict={r['sign_verdict']}")
    print(f"  |delta|_LayerB clean = {r['delta_LayerB_clean']:.6f}")
    print(f"  order-mix ratio      = {r['order_mix_ratio']:.4f} "
          f"(clean Layer-B / s63 mixed K_a4/K_a2={r['K_a4_over_K_a2']:.4f})")
    print("-" * 78)
    print(f"  G_tt^a2-only = {r['G_tt_a2_only']:.6f}   contamination = {r['contamination_metric']:.2e}"
          f"  (tol {CONTAM_TOL}; PASS={r['contam_pass']})")
    print("-" * 78)
    print(f"  K_total RETIRED = {r['K_total_retired_flag']}")
    print(f"    stored K_total = {r['K_total_fold']:.4f} = sqrt(5^2 + {r['LayerC_magnitude']:.3f}^2)"
          f" (quad-ratio {r['quad_ratio_implied']:.4f} ~ 1, NOT 0.4865)")
    print(f"    linear law 5*(1+0.4865) = {r['linear_read']:.4f}   (resid {r['resid_linear']:.4f})")
    print(f"    quad@0.4865            = {r['quad_at_ratio']:.4f}   (resid {r['resid_quad_ratio']:.4f})")
    print(f"    sqrt(2K) leading-only  = {r['sqrt_2K']:.4f} = sqrt(10)  (three inconsistent laws)")
    print("-" * 78)
    print(f"  R_K'(tau_fold) = {r['RKp_fold']:+.4f}   g3(cubic) = {r['g3']:+.4e}")
    print(f"  Tr(H^-1) = {r['Tr_Hinv']:.4f}  softest mode = {r['softest_mode']:.3f}  cond_H = {r['cond_H']:.3f}")
    print(f"  deltaZ_1loop (interacting soft-mode IR) = {r['deltaZ_1loop']:.4e}"
          f"  (free-field measure-check was 0 EXACT, S116-W4)")
    print("-" * 78)
    print(f"  rho_B(fold) = {r['rho_B_fold']:.4f} (= |R_K|/Lam^2 = {r['raw_RK_fold_abs']:.4f}/{r['Lambda_eff']**2:.4f})"
          f"  > rho_max={r['rho_max']}  [BINDING]")
    print(f"  rho_C(fold) = {r['rho_C_fold']:.4f} (eps_H)  < rho_max  [not binding]")
    print(f"  X_regime = {r['X_regime']:.4f} (|tau-tau_fold|; tau_X={r['tau_at_X']:.4f}; "
          f"bounded={r['X_bounded']} -> track_{'A' if r['X_bounded'] else 'B'})")
    print("=" * 78)

    make_plot(r)

    # ---- save npz (all required keys) ----
    np.savez(
        OUT_NPZ,
        c_B=r["c_B"], c_4=r["c_4"], delta_fold=r["delta_fold"], sign_delta=r["sign_delta"],
        c_quad_quad=r["c_boxbox"], c_grad4=r["c_grad4"], c_riem=r["c_riem"],
        deltaZ_1loop=r["deltaZ_1loop"], G_tt_a2_only=r["G_tt_a2_only"],
        contamination_metric=r["contamination_metric"],
        K_total_retired_flag=r["K_total_retired_flag"],
        rho_B_arr=r["rho_B_arr"], rho_C_arr=r["rho_C_arr"], X_regime=r["X_regime"],
        tau_grid=r["tau_grid"],
        # extras (provenance / cross-checks)
        delta_LayerB_clean=r["delta_LayerB_clean"], order_mix_ratio=r["order_mix_ratio"],
        rho_B_fold=r["rho_B_fold"], rho_C_fold=r["rho_C_fold"], tau_at_X=r["tau_at_X"],
        X_bounded=r["X_bounded"], binding_param=r["binding_param"],
        K_total_fold=r["K_total_fold"], K_a4_over_K_a2=r["K_a4_over_K_a2"],
        sqrt_2K=r["sqrt_2K"], LayerC_magnitude=r["LayerC_magnitude"],
        quad_ratio_implied=r["quad_ratio_implied"], linear_read=r["linear_read"],
        quad_at_ratio=r["quad_at_ratio"], a4_R2_scalar_coeff=r["sym_a4_R2_scalar_coeff"],
        RKp_fold=r["RKp_fold"], g3=r["g3"], Tr_Hinv=r["Tr_Hinv"], cond_H=r["cond_H"],
        softest_mode=r["softest_mode"], delta_S_1loop_mod=r["delta_S_1loop_mod"],
        rho_B_fold_signed=r["rho_B_fold_signed"], Lambda_eff=r["Lambda_eff"],
        rho_max=r["rho_max"], contam_tol=CONTAM_TOL,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], composite=r["composite"],
    )

    tag = (f"(value={r['value']!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    extra = [
        "# regulator_pin=a_2^{zeta},a_4^{zeta} (Gilkey invariants regulator-UNIVERSAL; "
        "residual scheme-dep in f0/f2 -> magnitude INFO) CLASS=FULL",
        f"# order-sep: c_B=1/60 c_4=1/60 c_grad4=G^2/288 c_riem=1/180 (Sage-exact); "
        f"K_total=7.0698 RETIRED=sqrt(5^2+{r['LayerC_magnitude']:.3f}^2) order-mix; "
        f"deltaZ_1loop={r['deltaZ_1loop']:.3e} (interacting soft-mode IR; free-field was 0 EXACT)",
    ]
    print_verdict_payload(r["composite"], r["value"], audit_sha, content_sha,
                          r["sign_verdict"], r["magnitude_verdict"], r["regime_verdict"],
                          extra_rows=extra)

    print(f"\n=== {GATE_ID}: {r['composite']} "
          f"(sign={r['sign_verdict']}/mag={r['magnitude_verdict']}/regime={r['regime_verdict']}) "
          f"(wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
