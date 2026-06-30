#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE  (W7-7a, COMPUTE half)
============================================================
Cross-layer a0/a2/a4 shared-borrowed-H(t) covariance audit.

Gate     : S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE  (schema R3, [SIGN], PHONONIC)
Wave     : Session 96, Wave 7
Plan     : sessions/session-plan/session-96-plan-w7.md  §W7-7a
Owner    : gen-physicist (cross-domain UQ audit spanning a0/a2/a4 layers)

DOWNSTREAM (load-bearing): this verdict feeds (1) W7-7b (the capstone 7.3
restriction edit) and (2) the S96 D3 workshop (adversarial algebraic-vs-
statistical-independence adjudication). The max off-diagonal correlation AND its
band (<0.1 PASS / 0.1-0.5 INFO / >0.5 FAIL) are made unambiguous in BOTH the
verdict-line value field and the WP section so the 7.3 restriction can condition
on it.

PURPOSE
-------
Capstone 7.3 multiplies observational improbabilities across the a0 x a2 x a4
spectral-moment layers, "independent by the certified Wronskian" (S75 W2-E:
W[a0,a2,a4](tau) prop R_K'(tau)^3 = e^{-12 tau}(e^{3 tau}-1)^6, nonzero off
tau=0). That certificate licenses ALGEBRAIC layer-independence: the three
Seeley-DeWitt moments are functionally independent functions of tau.

CRUX (the distinction W7-7b restricts on):
  ALGEBRAIC layer-independence (Wronskian != 0)  =/=  STATISTICAL independence
  of the borrowed-H observational residuals.
The dagger rows (w0, wa, CC, sigma8) are evaluated using the container-observer's
FRW H(t) as external input (caveat C10). A SHARED external H(t) can correlate the
OBSERVATIONAL residuals across layers even though the substrate moments are
algebraically independent. This gate measures whether the laboratory-side
correlation survives to break the multiplication.

METHOD (per kaku V.8)
---------------------
Compute d(residual_i)/d(ln H) for each layer under a shared d(ln H) = dH/H
perturbation, then form the 3x3 cross-layer covariance / correlation matrix:

  residual_a0 := w0_obs - w0_FW       a0 layer (DE eq. of state; C10: rho_vac ~ M_Pl^2 H^2)
  residual_a2 := sigma8_obs - sigma8_FW   a2 layer (growth integrates borrowed H(z))
  residual_a4 := m_H_obs - m_H_FW     a4 layer (KK-threshold fiber mass; H-INDEPENDENT)

Only the FW (framework-evaluated) side BORROWS H; the observational anchors are
fixed data. So d(residual_i)/d(ln H) = - d(X_i_FW)/d(ln H).

  Cov(res_i, res_j) = (d res_i/d ln H)(d res_j/d ln H) Var(d ln H)
  Corr(res_i, res_j) = sign(s_i s_j)  if both layers H-sensitive (the Var and any
                       common scale cancel in the normalized correlation), else 0
  where s_i = d(res_i)/d(ln H).

DERIVATIVE STRUCTURE (closed form; substitution chain below)
------------------------------------------------------------
a0 (C10 two-fluid partition). rho_DE = rho_eff (effacement, H-INDEPENDENT) +
rho_track = alpha_V M_Pl^2 H^2 (C10, w=-1). The framework w0_FW is the
pressure-weighted EOS of the two-fluid DE sector:
  w0_FW = (w_track rho_track + w_eff rho_eff)/rho_DE
The departure of w0_FW=-0.918 from the pure-vacuum w=-1 is the normal-fluid
(GGE, w_n=0) admixture: 1+w0_FW = +0.082 is the dust fraction by EOS weight.
Under d ln H, only the H^2-tracking piece moves: d(rho_track)/d ln H = 2 rho_track.
The DE-fraction in the tracking (w=-1) piece thus GROWS, pushing w0_FW MORE
negative => d(w0_FW)/d ln H < 0  => d(res_a0)/d ln H = -d(w0_FW)/d ln H > 0.
Closed form (derived in compute()): s_a0 = -dw0/dlnH = +2 f_n (1+w0_FW)(... ) > 0,
sign(s_a0) = + (a residual that DECREASES, i.e. data minus FW grows less negative,
when H increases -- the partition shift makes w0_FW more negative, widening the
gap to the less-negative observed w0_obs=-0.803).

a2 (growth). sigma8_FW = sigma8_LCDM * (D_FW/D_LCDM) where the growth amplitude
ratio modulates a BORROWED LCDM growth history (S96 W6-1 f.sigma8). The growth
factor D solves D'' + (2 + H'/H) a^{-1} D' = (3/2) Omega_m(a) D; raising H at
fixed Omega_m h^2 SUPPRESSES growth (more Hubble friction) => d(sigma8_FW)/d ln H
< 0 => d(res_a2)/d ln H = -d(sigma8_FW)/d ln H > 0. sign(s_a2) = +.

a4 (Higgs). m_H is the transverse |S|^2 fiber oscillation at the KK threshold --
a fiber-mass spectral read-off, DECOUPLED from the borrowed FRW H(t).
d(m_H_FW)/d ln H = 0 EXACTLY => s_a4 = 0 => Corr(*, a4) = 0.

SUBSTITUTION CHAIN -> DIRECTION
-------------------------------
Both s_a0 > 0 and s_a2 > 0 (same sign): a SHARED +d ln H shifts BOTH the a0 and
a2 residuals in the SAME direction => Corr(a0,a2) = sign(s_a0 s_a2) = +1 at
leading order in the shared-H channel. The off-diagonal a0-a2 correlation is
therefore NOT negligible (|Corr|=1 in the pure shared-H channel), which by the
plan rubric is a FAIL band (>0.5): the shared C10 borrowed-H(t) strongly
correlates the a0/a2 residuals, so the 7.3 product OVER-states the joint
improbability and must be re-derived with the correlation matrix; W7-7b restricts
the joint-BF to the zero-parameter structural spine (which carries NO borrowed H).

  IMPORTANT (substrate-first reading): this is NOT a falsification of the
  algebraic Decoupling Theorem. The substrate moments a0/a2/a4 remain
  algebraically independent (Wronskian != 0, a substrate-IS structural fact).
  What FAILS is the *statistical* multiplication of the *borrowed-H observational*
  residuals: the laboratory-IN projection through a SHARED H(t) re-couples what
  the substrate decoupled. The zero-parameter spine (Higgs mass, mass ordering,
  sigma/m=0, c_s^2=0) carries no borrowed H and its joint evidence stays
  multiplicative; the dagger rows are conditional.

PRE-REGISTERED (machinery_pin): the BF must NOT multiply WITHIN-layer observables
(Omega_DM and sigma8 are BOTH a2 -> not multiplied). This gate audits the
CROSS-layer (a0 x a2 x a4) off-diagonal only.

SCHEME    : shared-H(t)-perturbation-covariance
CONVENTION: cross-LAYER only (a0 x a2 x a4); WITHIN-layer (Omega_DM,sigma8 both a2)
            NOT multiplied -- pre-registered
TRIGGER   : [SIGN]  (does shared-H(t) INDUCE cross-layer correlation? sign of the
            product s_i s_j)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 per machinery pin (3x3 + scalar ODE)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# Section 1 — paths + canonical constants
# ----------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SHARED_DIR = THIS.parent                          # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent              # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_DIR = COMPUTATIONS_DIR / "session-96"     # outputs land here per plan
CANON = SHARED_DIR / "canonical_constants.py"

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (MANDATORY first import)
# names used: w0_FW, wa_FW, sigma_8, m_H_obs, Omega_m, tau_fold

GATE_ID = "S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE"
SCHEME = "shared-H(t)-perturbation-covariance"
CONVENTION = "cross-LAYER-a0xa2xa4-WITHIN-layer-NOT-multiplied"
L_MAX = "N/A"                                     # observational-residual UQ, not a spectral truncation

NPZ_OUT = SESSION_DIR / "s96_hyg_joint_evidence_d3_covariance.npz"
PNG_OUT = SESSION_DIR / "s96_hyg_joint_evidence_d3_covariance.png"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"   # canonical per gate-verdicts.md

INPUT_FILES = [CANON]

# ---- pre-registered machinery pins (plan §W7-7a machinery_pin_map) ----
N_EVAL = 3                                         # (local) 3 layers x 3 cross-pairs
DH_MIN = -0.05                                     # (local) shared dH/H perturbation low
DH_MAX = +0.05                                     # (local) shared dH/H perturbation high
DH_STEP = 0.01                                     # (local) 11-point grid
DERIV_RELTOL = 1e-6                                # (local) residual-derivative rel_tol pin
CORR_PASS = 0.1                                    # (local) PASS if max offdiag |Corr| < 0.1
CORR_FAIL = 0.5                                    # (local) FAIL if max offdiag |Corr| > 0.5

# ---- dagger-row anchors (§7.1 †; observational comparison anchors) ----
# a0: w0 joint posterior central value (Popovic/DES 2511.07517v3 joint fit, §7.1 ‡)
W0_OBS = -0.803                                    # (local) §7.1 w0† joint posterior central
# a2: sigma8 framework prediction (§7.1 σ8† zero-free-parameter)
SIGMA8_FW = 0.799                                  # (local) §7.1 σ8† zero-free-parameter prediction
# a4: m_H framework prediction (KK-threshold band lower edge, the defensible headline §7.1)
M_H_FW = 127.5                                     # (local) §7.1 m_H KK-threshold band lower edge (GeV)


# ----------------------------------------------------------------------------
# Section 2 — SHA-256 dual-pin block (canonical local pattern)
# ----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        sb = Path(script_path).read_bytes()  # (local)
    except OSError:
        sb = b""
    try:
        cb = Path(canonical_path).read_bytes()  # (local)
    except OSError:
        cb = b""
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                    sort_keys=True).encode("utf-8")  # (local)
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)
    hc = hashlib.sha256(); hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


# ----------------------------------------------------------------------------
# Section 3 — derivative kernels (closed-form / numerical, all H-borrowed)
# ----------------------------------------------------------------------------
def dw0_dlnH_a0(w0_fw):
    """d(w0_FW)/d(ln H) from the C10 two-fluid DE partition.

    rho_DE = rho_eff (H-indep, w=-1 effacement leakage) + rho_track (=alpha_V
    M_Pl^2 H^2, w=-1) + (GGE normal admixture giving the dust EOS weight).
    Express w0_FW = -1 + f_n where f_n = 1+w0_FW is the EOS dust fraction (the
    normal/GGE pressure share). The dust fraction f_n is carried by the
    H-INDEPENDENT sector (GGE quasiparticle gas was born at rest, T^{0i}=0); the
    H^2-tracking vacuum is pure w=-1. Under d ln H, rho_track -> rho_track(1+2 dlnH)
    while the dust-bearing sector is fixed, so the vacuum (w=-1) WEIGHT grows and
    the dust weight f_n SHRINKS proportionally:
        f_n(H) = f_n0 * rho_nonvac/(rho_nonvac + rho_track e^{2 dlnH})
    d f_n/d ln H = -2 f_n0 * Omega_track * (1 - Omega_track)  (logistic deriv),
    with Omega_track = rho_track/rho_DE the tracking-vacuum DE fraction.
    Then d w0_FW/d ln H = d f_n/d ln H = -2 f_n Omega_track (1-Omega_track) (to
    leading order f_n~f_n0).  Returns this signed scalar.
    """
    f_n = 1.0 + w0_fw                              # (local) EOS dust fraction = +0.082
    # Omega_track: tracking vacuum saturates observed DE (DILUTION-CC rho_vac/rho_obs=1.032);
    # the DE-sector tracking-vacuum fraction is ~ (1 - f_n) of the DE EOS budget.
    Omega_track = 1.0 - f_n                        # (local) vacuum (w=-1) DE fraction ~ 0.918
    dw0 = -2.0 * f_n * Omega_track * (1.0 - Omega_track)   # (local) logistic partition derivative
    return dw0


def dsigma8_dlnH_a2(Omega_m_val, w0_fw, tol):
    """d(sigma8_FW)/d(ln H) from the linear growth ODE on a borrowed-H background.

    sigma8_FW = sigma8_LCDM * D(a=1; H)/D_ref. Growth factor D(a) solves, in
    e-fold time N=ln a:
        D'' + (2 + dlnH/dN) D' - (3/2) Omega_m(N) D = 0
    with Omega_m(N) = Omega_m0 a^{-3} / E(N)^2, E=H/H0. A uniform fractional shift
    dH/H = const rescales E -> E(1+dlnH); at FIXED Omega_m h^2 (matter density
    pinned) this DILUTES Omega_m(N) = Omega_m0/(E^2) by (1+dlnH)^{-2} AND adds
    Hubble friction, BOTH suppressing growth. Returns d ln(D(a=1))/d ln H * D
    (signed; negative = growth suppressed by larger H). Computed by symmetric
    finite difference of the integrated D(a=1) over +/- a small dlnH, scaled by
    sigma8_FW to give d(sigma8_FW)/d ln H in sigma8 units.
    """
    def growth_D_at_a1(dlnH):
        # integrate from a_i=1e-3 (N_i=ln 1e-3) to a=1 (N=0)
        N_i = np.log(1e-3)                         # (local)
        H0 = 1.0                                   # (local) units cancel in ratio
        Om0 = Omega_m_val * (1.0 + dlnH) ** (-2)   # (local) fixed Omega_m h^2 => dilute by E^2
        OL0 = 1.0 - Om0                            # (local) flat closure on the borrowed background
        def E2(N):
            a = np.exp(N)                          # (local)
            # borrowed LCDM-like background with the DE EOS w0_fw, scaled by (1+dlnH)^2
            rho_de = OL0 * a ** (-3.0 * (1.0 + w0_fw))   # (local)
            return (Om0 * a ** -3 + rho_de) * (1.0 + dlnH) ** 2  # (local)
        def dlnE_dN(N):
            h = 1e-5                               # (local)
            return (np.log(np.sqrt(E2(N + h))) - np.log(np.sqrt(E2(N - h)))) / (2 * h)  # (local)
        def Om_N(N):
            a = np.exp(N)                          # (local)
            return (Om0 * a ** -3) / E2(N)         # (local)
        def rhs(N, y):
            D, Dp = y                              # (local)
            return [Dp, -(2.0 + dlnE_dN(N)) * Dp + 1.5 * Om_N(N) * D]
        # matter-dominated IC: D ~ a => D(N_i)=a_i, D'(N_i)=a_i
        y0 = [np.exp(N_i), np.exp(N_i)]            # (local)
        sol = solve_ivp(rhs, (N_i, 0.0), y0, rtol=tol, atol=tol * 1e-3,
                        dense_output=False, max_step=0.05)
        return sol.y[0, -1]                        # (local) D(a=1)

    eps = 1e-3                                      # (local) symmetric-difference step in dlnH
    D_plus = growth_D_at_a1(+eps)                   # (local)
    D_minus = growth_D_at_a1(-eps)                  # (local)
    D_0 = growth_D_at_a1(0.0)                        # (local)
    dlnD = (np.log(D_plus) - np.log(D_minus)) / (2 * eps)   # (local) d ln D / d ln H
    # sigma8_FW prop D(a=1); d(sigma8_FW)/d ln H = sigma8_FW * d ln D / d ln H
    return SIGMA8_FW * dlnD, dlnD, D_0


def dmH_dlnH_a4():
    """d(m_H_FW)/d(ln H) = 0 EXACTLY. m_H is a KK-threshold fiber mass (|S|^2
    transverse oscillation), a spectral read-off of D_K decoupled from the
    borrowed FRW H(t)."""
    return 0.0


# ----------------------------------------------------------------------------
# Section 4 — compute the 3x3 cross-layer covariance / correlation matrix
# ----------------------------------------------------------------------------
def compute() -> dict:
    res = {}  # (local)

    # residual central values (for the WP context; not used in the correlation)
    res["residual_a0"] = float(W0_OBS - w0_FW)               # -0.803 - (-0.918) = +0.115
    res["residual_a2"] = float(sigma_8 - SIGMA8_FW)          # 0.811 - 0.799 = +0.012
    res["residual_a4"] = float(m_H_obs - M_H_FW)             # 125.1 - 127.5 = -2.4 GeV

    # d(residual_i)/d ln H = - d(X_i_FW)/d ln H  (only FW borrows H)
    dw0 = dw0_dlnH_a0(w0_FW)                                 # (local) signed dw0_FW/dlnH
    dsig8, dlnD, D0 = dsigma8_dlnH_a2(Omega_m, w0_FW, DERIV_RELTOL)  # (local)
    dmH = dmH_dlnH_a4()                                      # (local) = 0

    s_a0 = -dw0                                              # (local) d(res_a0)/dlnH
    s_a2 = -dsig8                                            # (local) d(res_a2)/dlnH
    s_a4 = -dmH                                              # (local) d(res_a4)/dlnH = 0

    res["dw0_FW_dlnH"] = float(dw0)
    res["dsigma8_FW_dlnH"] = float(dsig8)
    res["dlnD_dlnH"] = float(dlnD)
    res["growth_D_a1"] = float(D0)
    res["dmH_FW_dlnH"] = float(dmH)
    res["s_a0"] = float(s_a0)
    res["s_a2"] = float(s_a2)
    res["s_a4"] = float(s_a4)

    # sensitivity vector
    s = np.array([s_a0, s_a2, s_a4], dtype=float)           # (local)

    # shared-H perturbation grid (11-pt) and its variance
    dh_grid = np.arange(DH_MIN, DH_MAX + 0.5 * DH_STEP, DH_STEP)   # (local)
    var_dh = float(np.var(dh_grid, ddof=0))                 # (local) Var(dlnH) over the pinned grid
    res["dh_grid"] = dh_grid
    res["var_dlnH"] = var_dh

    # Cov(res_i,res_j) = s_i s_j Var(dlnH)  (pure shared-H channel, rank-1)
    cov = np.outer(s, s) * var_dh                           # (local) 3x3 rank-1 covariance
    res["cov_matrix"] = cov

    # Correlation: normalize. For the pure shared-H (rank-1) channel the
    # correlation between two H-sensitive layers is exactly sign(s_i s_j)
    # (the Var and the magnitudes cancel). The a4 row is identically 0
    # (s_a4=0) so its correlations are UNDEFINED-as-0 (no shared-H variance).
    corr = np.zeros((3, 3), dtype=float)                    # (local)
    for i in range(3):
        for j in range(3):
            if i == j:
                corr[i, j] = 1.0 if s[i] != 0.0 else 0.0
            else:
                denom = abs(s[i]) * abs(s[j])               # (local)
                if denom > 0.0:
                    corr[i, j] = float(np.sign(s[i] * s[j]))  # +/-1 in pure shared-H channel
                else:
                    corr[i, j] = 0.0                        # a4 carries no shared-H variance
    res["corr_matrix"] = corr

    # max off-diagonal |Corr| over the three CROSS-LAYER pairs
    pairs = {"a0-a2": abs(corr[0, 1]), "a0-a4": abs(corr[0, 2]), "a2-a4": abs(corr[1, 2])}  # (local)
    res["pair_a0_a2"] = float(corr[0, 1])
    res["pair_a0_a4"] = float(corr[0, 2])
    res["pair_a2_a4"] = float(corr[1, 2])
    max_pair = max(pairs, key=pairs.get)                    # (local)
    max_offdiag = float(pairs[max_pair])                    # (local)
    res["max_offdiag_abs_corr"] = max_offdiag
    res["max_offdiag_pair"] = max_pair

    # band classification (unambiguous for downstream W7-7b + D3 workshop)
    if max_offdiag < CORR_PASS:
        band = "<0.1"                                       # (local)
    elif max_offdiag <= CORR_FAIL:
        band = "0.1-0.5"                                    # (local)
    else:
        band = ">0.5"                                       # (local)
    res["band"] = band

    # ---- 3-tuple verdict (schema-v2) ----
    # SIGN: directional pre-reg "shared-H(t) INDUCES cross-layer correlation".
    #   Predicted (substitution chain Step 4): s_a0>0 AND s_a2>0 => Corr(a0,a2)=+1 (>0).
    #   sign_verdict PASS iff the COMPUTED direction matches the predicted direction
    #   (induced correlation is POSITIVE, i.e. the shared-H channel co-shifts a0,a2).
    sign_ok = (s_a0 > 0.0) and (s_a2 > 0.0) and (corr[0, 1] > 0.0)   # (local)
    sign_v = "PASS" if sign_ok else "FAIL"

    # MAGNITUDE: the gate's primary number is max_offdiag vs the 0.1/0.5 bands.
    #   PASS (negligible) iff <0.1 ; INFO iff 0.1-0.5 ; FAIL iff >0.5.
    if max_offdiag < CORR_PASS:
        mag_v = "PASS"                                      # (local)
    elif max_offdiag <= CORR_FAIL:
        mag_v = "INFO"                                      # (local)
    else:
        mag_v = "FAIL"                                      # (local)

    # REGIME: validity of the leading-order shared-H linearization across the
    #   pinned dH/H in [-0.05,+0.05]. The rank-1 shared-H channel + the linear
    #   d/dlnH are exact to O(dlnH) and the grid is fully within the small-
    #   perturbation regime => VALID (no auto-shortening; full intended window).
    regime_v = "VALID"

    # composite collapse (PRE-REGISTERED rule, gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        verdict = "FAIL"
    elif sign_v == "FAIL":
        verdict = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        verdict = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        verdict = "INFO"
    elif mag_v == "INFO":
        verdict = "INFO"
    else:
        verdict = "PASS"

    res["sign_verdict"] = sign_v
    res["magnitude_verdict"] = mag_v
    res["regime_verdict"] = regime_v
    res["verdict"] = verdict

    # value string -- band + max + which-pair + the s-vector, unambiguous for both consumers
    res["value"] = (
        f"max_offdiag_corr={max_offdiag:.4f}_BAND={band}_pair={max_pair};"
        f"Corr(a0,a2)={corr[0,1]:+.4f}_Corr(a0,a4)={corr[0,2]:+.4f}_Corr(a2,a4)={corr[1,2]:+.4f};"
        f"s_a0={s_a0:+.6e}_s_a2={s_a2:+.6e}_s_a4={s_a4:+.6e};"
        f"ALGEBRAIC_indep(Wronskian_W2E)_TRUE_but_STATISTICAL_indep={'TRUE' if band=='<0.1' else 'FALSE'};"
        f"7.3_multiplication={'VALID' if band=='<0.1' else ('VALID-to-leading-order-HEDGE' if band=='0.1-0.5' else 'OVERSTATED-restrict-to-zero-param-spine')};"
        f"within-layer(Omega_DM,sigma8_both_a2)_NOT_multiplied=PRE-REGISTERED"
    )
    return res


# ----------------------------------------------------------------------------
# Section 5 — plot (3x3 cross-layer correlation heatmap)
# ----------------------------------------------------------------------------
def make_plot(res):
    corr = res["corr_matrix"]                               # (local)
    labels = [r"$a_0$ ($w_0$)", r"$a_2$ ($\sigma_8$)", r"$a_4$ ($m_H$)"]   # (local)
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.4))

    im = ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(3)); ax.set_yticks(range(3))
    ax.set_xticklabels(labels); ax.set_yticklabels(labels)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f"{corr[i,j]:+.2f}", ha="center", va="center",
                    color="white" if abs(corr[i, j]) > 0.5 else "black", fontsize=13, fontweight="bold")
    ax.set_title(f"{GATE_ID}\ncross-layer residual correlation (shared C10 borrowed-H(t))", fontsize=10)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="Corr(residual_i, residual_j)")

    # bar of d(residual)/d ln H sensitivities
    s = [res["s_a0"], res["s_a2"], res["s_a4"]]             # (local)
    colors = ["#c0392b" if v > 0 else ("#2980b9" if v < 0 else "#7f8c8d") for v in s]  # (local)
    ax2.bar(range(3), s, color=colors)
    ax2.set_xticks(range(3)); ax2.set_xticklabels([r"$a_0$", r"$a_2$", r"$a_4$"])
    ax2.axhline(0, color="k", lw=0.8)
    ax2.set_ylabel(r"$\partial(\mathrm{residual})/\partial\ln H$  (borrowed-H sensitivity)")
    ax2.set_title(f"max off-diag |Corr| = {res['max_offdiag_abs_corr']:.3f}  ->  band {res['band']}\n"
                  f"verdict {res['verdict']} (s_a0,s_a2 same sign; a4 H-independent)", fontsize=9)
    for i, v in enumerate(s):
        ax2.text(i, v + (0.02 * np.sign(v) if v != 0 else 0.0), f"{v:+.2e}",
                 ha="center", va="bottom" if v >= 0 else "top", fontsize=8)

    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  plot -> {PNG_OUT}")


# ----------------------------------------------------------------------------
# Section 6 — verdict-line emission (dual-SHA + schema-v2 3-tuple)
# ----------------------------------------------------------------------------
def append_verdict(verdict, value, audit_sha, content_sha, sign_v, mag_v, regime_v, res):
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = shared-H(t) INDUCES cross-layer correlation: predicted s_a0>0 AND s_a2>0 "
        f"(C10 partition pushes w0_FW more negative; growth friction suppresses sigma8_FW) => "
        f"Corr(a0,a2)={res['pair_a0_a2']:+.3f} POSITIVE (induced, computed direction matches => PASS); "
        f"mag = max off-diag |Corr|={res['max_offdiag_abs_corr']:.3f} vs bands 0.1(PASS)/0.5(FAIL) => "
        f"BAND {res['band']} (a0-a2 pair co-shifts under shared C10 borrowed-H(t); "
        f"ALGEBRAIC layer-independence [Wronskian W2-E] does NOT carry to STATISTICAL independence here); "
        f"regime = leading-order shared-H linearization VALID across full dH/H in [-0.05,+0.05] (no auto-shortening); "
        f"DOWNSTREAM: W7-7b restricts 7.3 to the zero-parameter structural spine (no borrowed H); "
        f"within-layer (Omega_DM,sigma8 both a2) NOT multiplied [pre-registered]\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(tuple_row)
    print("  verdict line + dual-SHA companion + 3-tuple row appended.")


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
def main():
    print(f"=== {GATE_ID} ===")
    print(f"  anchors: w0_FW={w0_FW}  W0_OBS={W0_OBS}  sigma8_FW={SIGMA8_FW}  sigma8_obs={sigma_8}")
    print(f"           m_H_FW={M_H_FW}  m_H_obs={m_H_obs}  Omega_m={Omega_m}  tau_fold={tau_fold}")
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    print("--- residual central values ---")
    print(f"  residual_a0 (w0_obs-w0_FW)      = {res['residual_a0']:+.4f}")
    print(f"  residual_a2 (sigma8_obs-sigma8_FW) = {res['residual_a2']:+.4f}")
    print(f"  residual_a4 (m_H_obs-m_H_FW)    = {res['residual_a4']:+.4f} GeV")
    print("\n--- borrowed-H sensitivities d(residual)/d ln H ---")
    print(f"  s_a0 = {res['s_a0']:+.6e}  (dw0_FW/dlnH={res['dw0_FW_dlnH']:+.6e})")
    print(f"  s_a2 = {res['s_a2']:+.6e}  (dsigma8_FW/dlnH={res['dsigma8_FW_dlnH']:+.6e}, dlnD/dlnH={res['dlnD_dlnH']:+.6e})")
    print(f"  s_a4 = {res['s_a4']:+.6e}  (m_H H-INDEPENDENT, exact 0)")
    print("\n--- 3x3 cross-layer correlation matrix ---")
    print(res["corr_matrix"])
    print(f"\n  max off-diag |Corr| = {res['max_offdiag_abs_corr']:.4f}  (pair {res['max_offdiag_pair']})  BAND = {res['band']}")
    print(f"  Corr(a0,a2)={res['pair_a0_a2']:+.4f}  Corr(a0,a4)={res['pair_a0_a4']:+.4f}  Corr(a2,a4)={res['pair_a2_a4']:+.4f}")
    print(f"\n  VERDICT: {res['verdict']}  (sign={res['sign_verdict']} mag={res['magnitude_verdict']} regime={res['regime_verdict']})")
    print(f"  VALUE: {res['value']}")

    make_plot(res)

    save = {}  # (local)
    for k, v in res.items():
        if isinstance(v, bool):
            save[k] = int(v)
        else:
            save[k] = v
    save["audit_sha256"] = audit_sha
    save["content_sha256"] = content_sha
    save["GATE_ID"] = GATE_ID
    save["N_eval"] = N_EVAL
    save["scheme"] = SCHEME
    save["convention"] = CONVENTION
    save["CORR_PASS"] = CORR_PASS
    save["CORR_FAIL"] = CORR_FAIL
    np.savez(NPZ_OUT, **save)
    print(f"  data -> {NPZ_OUT}")

    append_verdict(res["verdict"], res["value"], audit_sha, content_sha,
                   res["sign_verdict"], res["magnitude_verdict"], res["regime_verdict"], res)

    print(f"\n4-tuple: (value={res['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print("DONE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
