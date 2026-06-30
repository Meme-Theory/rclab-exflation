#!/usr/bin/env python3
"""
S101 W4-5 S101-M0-BCS-SCREENING — S62 BCS screening applied to M0^{sector}
==========================================================================

Gate: S101-M0-BCS-SCREENING ([SIGN])

Pre-registered threshold (PRIMARY route = m_H-level first-power transfer; the
S100a-measured LINEAR-first-power inheritance law):

  PASS  iff  [delta_BCS^solve exists, unique in [0, 0.5]]
        AND  [|delta_BCS^solve - 0.07| <= 0.03]
        AND  [|r_a^scr| < |r_a^unscr| for BOTH anchors a in {KK, tree}]
        AND  [max_a |r_a^scr| <= 0.020 on the PRIMARY route]

  INFO  iff  direction confirmed (monotone shrink + root exists) BUT either
             0.020 < max_a |r_a^scr| <= 0.035, OR |delta_BCS^solve - 0.07| > 0.03,
             OR the CONVENTION-SENSITIVE flag fires
             (|r_KK^scr,PRIM - r_KK^scr,RG| > 0.010 absolute).

  FAIL  iff  no root in [0, 0.5] (recomputed machinery cannot close m_H —
             machinery-drift alarm vs S62) OR monotonicity fails for either
             anchor (screening moves the M0 residual AWAY from 0) OR
             max_a |r_a^scr| > 0.035.

Classification: PARTICLE.

METHODOLOGY
-----------
THREE-conjunct structure (avoids PASS-by-construction; the genuine contingencies
are conjuncts 1+2, per-anchor monotonicity, and the SECONDARY-route convergence):

  (1) delta_BCS^solve: RE-RUN the S62 2-loop machinery in-process (the
      s62_higgs_bcs_threshold.py lineage: g_3^eff(M_KK) = g_3(M_KK)*(1 - delta);
      lambda_CCM(M_KK) = (4/3)*g_3eff^2*ratio_gilkey; 2-loop SM RG down to M_Z;
      m_H^scr,RG = sqrt(2 lambda_IR)*v_ew) and root-solve
      m_H^scr,RG(delta) = m_H_obs = 125.1 on delta in [0, 0.5]. delta_BCS^solve
      must EXIST and be UNIQUE there.

  (2) delta-consistency: |delta_BCS^solve - 0.07| <= 0.03 — the screening NEEDED
      is the screening the documented BCS enhanced estimate PROVIDES
      (THRESHOLD-62's physical content).

  (3) Screened band, PRIMARY route (m_H-level first-power transfer):
      r_a^scr = (m_H^scr,a - m_H_obs)/m_H_obs with
      m_H^scr,a = m_H^scr,RG(delta_solve)*(m_H_a/m_H_tree). Since
      m_H^scr,RG(delta_solve) = 125.1 BY CONSTRUCTION:
        r_tree^scr = 0 BY CALIBRATION (DISCLOSED, not a finding)
        r_KK^scr   = m_H_KK/m_H_tree - 1 = 131.8/134 - 1 = -11/670 = -1.6418% EXACT
      SECONDARY route (report-only convention-sensitivity diagnostic): apply
      delta_solve at the KK-corrected boundary
      lambda_KK-boundary = (4/3)*g_3eff^2*ratio_gilkey*(131.8/134)^2, run the same
      2-loop RG down, report r_KK^scr,RG and the PRIMARY-vs-SECONDARY deviation;
      flag CONVENTION-SENSITIVE if |r_KK^scr,PRIM - r_KK^scr,RG| > 0.010 absolute.

Substrate framing: PARTICLE. M0^{sector} IS a fiber-excitation mass normalization
anchored through the |s(h)|^2 fiber-embedding amplitude it SHARES with the Higgs
mode; the BCS condensate is the substrate's own pairing structure screening its
own gauge moment (Sigma_anom(q^2=M_KK^2) renormalizes g_3(M_KK), the
fourth-spectral-moment a_4-channel coupling). The arrow flows: BCS pairing (BdG
screening fractions delta_a2/a_2, delta_a4/a_4) -> g_3^eff(M_KK) -> boundary
lambda_CCM -> 2-loop RG -> screened anchor -> first-power M0 residual.

Regulator pin: a_4^{Pauli-Villars} (the BdG anomalous-self-energy / Pauli-Villars
screening fraction delta_a4/a_4 from S61 BdG spectral action; the Gilkey ratio
a_4/a_2 is a_n^{zeta} heat-kernel Seeley-DeWitt). Both carried in the verdict
regulator_pin companion row.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (small 5-coupling 2-loop RG ODE; cpu-cap-OMP8)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
SHARED_DIR_BOOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
sys.path.insert(0, SHARED_DIR_BOOT)
from canonical_constants import (
    PI, M_KK_gravity, M_Z, M_W,
    alpha_em_MZ_inv, sin2_thetaW_MSbar, alpha_s_MZ_obs,
    m_H_obs, m_t_pole, m_b_pole,
    m_H_FW_tree, m_H_FW_KK_threshold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-M0-BCS-SCREENING"                                 # (local)
SCHEME = "KK-threshold-131.8-plus-tree-A10-134"                   # (local)
CONVENTION = "FIRST-POWER-MH-LEVEL-TRANSFER-PRIMARY"              # (local)
L_MAX = "N/A"                                                     # (local)

# Pre-registered thresholds (FROZEN at plan-freeze; do NOT edit after seeing values)
PASS_CEILING = 0.020          # (local) strict PASS on max_a |r_a^scr| (PRIMARY)
INFO_CEILING = 0.035          # (local) INFO ceiling
DELTA_TARGET = 0.07           # (local) documented BCS enhanced estimate
DELTA_WINDOW = 0.03           # (local) delta-consistency half-window about 0.07
CONV_SENS_TOL = 0.010         # (local) PRIMARY-vs-SECONDARY convention-sensitivity tol
SCAN_MIN, SCAN_MAX = 0.0, 0.50  # (local) S62 sensitivity-scan range for delta_BCS
N_SCAN = 101                  # (local) S62 lineage grid
ROOT_TOL_GEV = 1e-6           # (local) bisection tolerance on |m_H^scr - 125.1|
N_PTS_RG = 2000               # (local) S62 N_pts for per-run RG integration

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s101_w4_m0_bcs_screening.npz"
OUT_PNG = SESSION_DIR / "s101_w4_m0_bcs_screening.png"

# Input files consumed (canonical feeds audit_sha256; the S62/S61/S100a npz/py
# feed audit_sha256 too — they are the machinery + inheritance pins)
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-100a" / "s100a_m0_mh_inheritance.npz",
    COMPUTATIONS_DIR / "session-62" / "s62_higgs_bcs_threshold.py",
    COMPUTATIONS_DIR / "session-61" / "s61_higgs_mass.npz",
    COMPUTATIONS_DIR / "session-61" / "s61_bdg_spectral_action.npz",
    COMPUTATIONS_DIR / "session-100a" / "s100a_yukawa_overlap_offdiag.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 5 — S62 2-loop SM RG machinery (re-implemented in-process; NOT cached)
# Reference: Machacek-Vaughn (1984), Ford-Jack-Jones (1992), Buttazzo et al.
# (2013) [1307.3536]. g1 in GUT normalization (g1 = sqrt(5/3)*g'),
# t = ln(mu/M_Z), beta_x = dx/dt. Faithful copy of s62_higgs_bcs_threshold.py.
# ---------------------------------------------------------------------------

def beta_2loop_SM(t, y):
    g1, g2, g3, yt, lam = y  # (local)
    g1sq, g2sq, g3sq, ytsq, lamsq = g1**2, g2**2, g3**2, yt**2, lam**2  # (local)
    b16pi2 = 16.0 * PI**2          # (local)
    b16pi2_sq = b16pi2**2          # (local)

    # gauge 1-loop
    beta_g1_1 = (41.0/10.0) * g1**3 / b16pi2   # (local)
    beta_g2_1 = (-19.0/6.0) * g2**3 / b16pi2   # (local)
    beta_g3_1 = (-7.0) * g3**3 / b16pi2        # (local)
    # gauge 2-loop
    beta_g1_2 = g1**3 / b16pi2_sq * (199.0/50.0*g1sq + 27.0/10.0*g2sq + 44.0/5.0*g3sq - 17.0/10.0*ytsq)  # (local)
    beta_g2_2 = g2**3 / b16pi2_sq * (9.0/10.0*g1sq + 35.0/6.0*g2sq + 12.0*g3sq - 3.0/2.0*ytsq)            # (local)
    beta_g3_2 = g3**3 / b16pi2_sq * (11.0/10.0*g1sq + 9.0/2.0*g2sq - 26.0*g3sq - 2.0*ytsq)                # (local)
    dg1 = beta_g1_1 + beta_g1_2  # (local)
    dg2 = beta_g2_1 + beta_g2_2  # (local)
    dg3 = beta_g3_1 + beta_g3_2  # (local)

    # top Yukawa
    beta_yt_1 = yt / b16pi2 * (9.0/2.0*ytsq - 17.0/20.0*g1sq - 9.0/4.0*g2sq - 8.0*g3sq)  # (local)
    beta_yt_2 = yt / b16pi2_sq * (
        -12.0*ytsq**2
        + ytsq*(393.0/80.0*g1sq + 225.0/16.0*g2sq + 36.0*g3sq)
        + 1187.0/600.0*g1sq**2 - 9.0/20.0*g1sq*g2sq
        + 19.0/15.0*g1sq*g3sq - 23.0/4.0*g2sq**2
        + 9.0*g2sq*g3sq - 108.0*g3sq**2
        + 6.0*lam**2 - 3.0/2.0*lam*ytsq
    )  # (local)
    dyt = beta_yt_1 + beta_yt_2  # (local)

    # Higgs quartic
    beta_lam_1 = (1.0/b16pi2) * (
        24.0*lamsq + 12.0*lam*ytsq - 12.0*ytsq**2
        - 3.0*lam*(3.0/5.0*g1sq + 3.0*g2sq)
        + 3.0/8.0*(3.0/25.0*g1sq**2 + 6.0/5.0*g1sq*g2sq + 3.0*g2sq**2)
    )  # (local)
    beta_lam_2 = (1.0/b16pi2_sq) * (
        -312.0*lam**3
        + lamsq*(-144.0*ytsq)
        + lam*ytsq*(-3.0*ytsq + 80.0*g3sq + 45.0/2.0*g2sq + 85.0/6.0*(3.0/5.0)*g1sq)
        + 60.0*ytsq**3
        - 16.0*ytsq**2*g3sq
        + lam*(108.0/5.0*(3.0/25.0)*g1sq**2 + 36.0*(3.0/5.0*g1sq*g2sq)/5.0 - 73.0/8.0*g2sq**2)
        - 3.0/5.0*g1sq*(-57.0/10.0*g2sq*g1sq + 12.0*ytsq**2)/2.0
        + g2sq*(-289.0/8.0*g2sq**2/4.0)
    )  # (local)
    dlam = beta_lam_1 + beta_lam_2  # (local)
    return [dg1, dg2, dg3, dyt, dlam]


def run_rg_down(g1_UV, g2_UV, g3_UV, yt_UV, lam_UV, t_UV, N_pts=N_PTS_RG):
    y0 = [g1_UV, g2_UV, g3_UV, yt_UV, lam_UV]                        # (local)
    sol = solve_ivp(beta_2loop_SM, [t_UV, 0], y0,
                    t_eval=np.linspace(t_UV, 0, N_pts),
                    method="RK45", rtol=1e-12, atol=1e-14)           # (local)
    return sol.t, sol.y, sol.success


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    res: dict = {}  # (local)

    # ---- S61 inputs (Gilkey ratio + BdG screening fractions) ----
    d_higgs = np.load(COMPUTATIONS_DIR / "session-61" / "s61_higgs_mass.npz", allow_pickle=True)   # (local)
    d_bdg = np.load(COMPUTATIONS_DIR / "session-61" / "s61_bdg_spectral_action.npz", allow_pickle=True)  # (local)
    ratio_gilkey = float(d_higgs["ratio_gilkey"])          # (local) a_4/a_2 = a_n^{zeta} Seeley-DeWitt
    delta_a2_over_a2 = float(d_bdg["ratio_delta_a2"])      # (local) 1.359e-4
    delta_a4_over_a4 = float(d_bdg["ratio_delta_a4"])      # (local) 1.491e-4
    delta_BCS_direct = delta_a4_over_a4 / 2.0              # (local) a_4^{Pauli-Villars} direct-screening reference

    # ---- S100a inheritance npz (exact rationals; the inherited residual band) ----
    d_inh = np.load(COMPUTATIONS_DIR / "session-100a" / "s100a_m0_mh_inheritance.npz", allow_pickle=True)  # (local)
    r_KK_unscr = float(d_inh["r_kk"])                      # (local) 67/1251
    r_tree_unscr = float(d_inh["r_tree"])                 # (local) 89/1251

    # ---- physical constants (PDG 2024); v_ew uses the Fermi-extracted value (S62 convention) ----
    v_ew = 246.22                                          # (local) GeV (Fermi-extracted; S62 lineage)
    m_tau = 1.77686                                        # (local) GeV
    alpha_em_MZ = 1.0 / alpha_em_MZ_inv                    # (local)
    sin2_tW = sin2_thetaW_MSbar                            # (local)
    alpha_s_MZ = alpha_s_MZ_obs                            # (local)

    # ---- SM couplings at M_Z (MSbar); g1 GUT-normalized ----
    g1_MZ = np.sqrt(5.0/3.0) * np.sqrt(4*PI*alpha_em_MZ/(1 - sin2_tW))  # (local)
    g2_MZ = np.sqrt(4*PI*alpha_em_MZ/sin2_tW)                            # (local)
    g3_MZ = np.sqrt(4*PI*alpha_s_MZ)                                     # (local)
    m_t_MSbar = m_t_pole * (1.0 - 4.0*alpha_s_MZ/(3.0*PI))               # (local)
    yt_MZ = np.sqrt(2)*m_t_MSbar/v_ew                                    # (local)
    lambda_MZ_obs = m_H_obs**2 / (2.0*v_ew**2)                           # (local)
    t_MKK = np.log(M_KK_gravity / M_Z)                                   # (local)

    # ---- run UP to M_KK to fix the boundary couplings (S62 step A) ----
    sol_up = solve_ivp(beta_2loop_SM, [0, t_MKK],
                       [g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs],
                       t_eval=np.linspace(0, t_MKK, 5000),
                       method="RK45", rtol=1e-12, atol=1e-14)            # (local)
    g1_MKK = sol_up.y[0, -1]   # (local)
    g2_MKK = sol_up.y[1, -1]   # (local)
    g3_MKK = sol_up.y[2, -1]   # (local) g_3(M_KK) nominal
    yt_MKK = sol_up.y[3, -1]   # (local)

    # ---- m_H from a given delta_BCS via the 2-loop RG-run picture (S62 step B+down) ----
    def m_H_scr_RG(delta, kk_boundary=False):
        """2-loop RG-run Higgs mass under BCS screening delta.
        kk_boundary=False -> PRIMARY-conjunct-1 boundary lambda = (4/3) g3eff^2 ratio_gilkey.
        kk_boundary=True  -> SECONDARY-route boundary lambda *= (m_H_KK/m_H_tree)^2.
        """
        g3_eff = g3_MKK * (1.0 - delta)                                 # (local)
        lam_bc = (4.0/3.0) * g3_eff**2 * ratio_gilkey                   # (local)
        if kk_boundary:
            lam_bc *= (m_H_FW_KK_threshold / m_H_FW_tree)**2            # (local)
        _, y_d, _ = run_rg_down(g1_MKK, g2_MKK, g3_eff, yt_MKK, lam_bc, t_MKK)  # (local)
        lam_IR = y_d[4, -1]                                             # (local)
        return float(np.sqrt(2.0*abs(lam_IR))*v_ew) if lam_IR > 0 else 0.0

    # ---- CONJUNCT 1: scan + root-solve delta_BCS^solve in [0, 0.5] ----
    delta_scan = np.linspace(SCAN_MIN, SCAN_MAX, N_SCAN)               # (local)
    mH_scan = np.array([m_H_scr_RG(db) for db in delta_scan])         # (local)

    # monotonicity of m_H^scr,RG(delta) over the scan (Definition-2 claim, re-verified)
    diffs = np.diff(mH_scan)                                           # (local)
    monotone_decreasing_RG = bool(np.all(diffs < 0))                  # (local)

    # root existence + uniqueness for m_H^scr,RG(delta) = m_H_obs
    f_root = lambda db: m_H_scr_RG(db) - m_H_obs                       # (local)
    sign_changes = np.where(np.diff(np.sign(mH_scan - m_H_obs)))[0]    # (local)
    n_roots = int(len(sign_changes))                                  # (local)
    delta_solve = None                                                # (local)
    root_unique = (n_roots == 1)                                      # (local)
    root_exists = (n_roots >= 1)                                      # (local)
    if root_exists:
        idx = sign_changes[0]                                          # (local)
        lo, hi = delta_scan[idx], delta_scan[idx + 1]                  # (local)
        delta_solve = float(brentq(f_root, lo, hi, xtol=1e-10, rtol=1e-12))  # (local)
        # confirm root tolerance
        mH_at_root = m_H_scr_RG(delta_solve)                          # (local)
        root_resid = abs(mH_at_root - m_H_obs)                        # (local)
    else:
        root_resid = float("nan")                                     # (local)

    # ---- CONJUNCT 2: delta-consistency with the documented 0.07 ----
    if delta_solve is not None:
        delta_consistency_dev = abs(delta_solve - DELTA_TARGET)       # (local)
        delta_consistent = bool(delta_consistency_dev <= DELTA_WINDOW)  # (local)
    else:
        delta_consistency_dev = float("nan")                          # (local)
        delta_consistent = False                                      # (local)

    # ---- CONJUNCT 3 PRIMARY: m_H-level first-power transfer (EXACT rationals) ----
    # m_H^scr,RG(delta_solve) = m_H_obs BY CONSTRUCTION =>
    #   r_tree^scr = 0 EXACT (calibration), r_KK^scr = m_H_KK/m_H_tree - 1 EXACT.
    fr_mH_obs = Fraction(1251, 10)   # 125.1   # (local)
    fr_mH_KK = Fraction(1318, 10)    # 131.8   # (local)
    fr_mH_tree = Fraction(1340, 10)  # 134.0   # (local)
    r_tree_scr_exact = (fr_mH_tree * (fr_mH_obs / fr_mH_tree) - fr_mH_obs) / fr_mH_obs   # (local) == 0
    r_KK_scr_exact = (fr_mH_KK * (fr_mH_obs / fr_mH_tree) - fr_mH_obs) / fr_mH_obs       # (local) == -11/670
    r_tree_scr = float(r_tree_scr_exact)   # (local)
    r_KK_scr = float(r_KK_scr_exact)       # (local)

    # unscreened exact rationals (cross-check vs npz)
    r_KK_unscr_exact = Fraction(67, 1251)    # (local)
    r_tree_unscr_exact = Fraction(89, 1251)  # (local)
    band_unscr_exact = r_tree_unscr_exact - r_KK_unscr_exact  # (local) 22/1251

    # per-anchor monotone shrink (the SIGN-keying contingency)
    shrink_KK = abs(r_KK_scr) < abs(r_KK_unscr)        # (local)
    shrink_tree = abs(r_tree_scr) < abs(r_tree_unscr)  # (local)
    both_shrink = bool(shrink_KK and shrink_tree)      # (local)

    maxabs_unscr = max(abs(r_KK_unscr), abs(r_tree_unscr))  # (local)
    maxabs_scr = max(abs(r_KK_scr), abs(r_tree_scr))        # (local)
    shrink_factor_worst = maxabs_unscr / maxabs_scr if maxabs_scr > 0 else float("inf")  # (local)
    mid_unscr = (r_KK_unscr + r_tree_unscr) / 2.0          # (local)
    mid_scr = (r_KK_scr + r_tree_scr) / 2.0                # (local)
    mid_factor = mid_unscr / abs(mid_scr) if mid_scr != 0 else float("inf")  # (local)
    half_spread_exact = band_unscr_exact / 2              # (local) 11/1251 irreducible remnant

    # ---- CONJUNCT 3 SECONDARY: KK-boundary RG transfer (convention-sensitivity) ----
    # apply delta_solve at the KK-corrected boundary; r_KK^scr,RG = m_H^scr,RG,KK / m_H_obs - 1
    r_KK_scr_RG = float("nan")          # (local)
    mH_scr_RG_KK = float("nan")         # (local)
    conv_sens_dev = float("nan")        # (local)
    convention_sensitive = False        # (local)
    if delta_solve is not None:
        mH_scr_RG_KK = m_H_scr_RG(delta_solve, kk_boundary=True)      # (local)
        r_KK_scr_RG = mH_scr_RG_KK / m_H_obs - 1.0                    # (local)
        conv_sens_dev = abs(r_KK_scr - r_KK_scr_RG)                   # (local)
        convention_sensitive = bool(conv_sens_dev > CONV_SENS_TOL)    # (local)

    # ---- m_H reference points (tree A10 vs 2-loop-noBCS) for context ----
    mH_2loop_noBCS = m_H_scr_RG(0.0)                                  # (local)
    mH_tree_A10 = float(m_H_FW_tree)                                  # (local) = 134.0

    # ===================== assemble result =====================
    res.update(dict(
        ratio_gilkey=ratio_gilkey, delta_a2_over_a2=delta_a2_over_a2,
        delta_a4_over_a4=delta_a4_over_a4, delta_BCS_direct=delta_BCS_direct,
        v_ew=v_ew, t_MKK=t_MKK, g1_MKK=g1_MKK, g2_MKK=g2_MKK, g3_MKK=g3_MKK, yt_MKK=yt_MKK,
        delta_scan=delta_scan, mH_scan=mH_scan,
        monotone_decreasing_RG=monotone_decreasing_RG,
        n_roots=n_roots, root_exists=root_exists, root_unique=root_unique,
        delta_solve=(delta_solve if delta_solve is not None else np.nan),
        root_resid=root_resid,
        delta_consistency_dev=delta_consistency_dev, delta_consistent=delta_consistent,
        r_KK_unscr=r_KK_unscr, r_tree_unscr=r_tree_unscr,
        r_KK_scr=r_KK_scr, r_tree_scr=r_tree_scr,
        r_KK_scr_num=r_KK_scr_exact.numerator, r_KK_scr_den=r_KK_scr_exact.denominator,
        r_KK_unscr_num=67, r_KK_unscr_den=1251, r_tree_unscr_num=89, r_tree_unscr_den=1251,
        band_unscr_num=band_unscr_exact.numerator, band_unscr_den=band_unscr_exact.denominator,
        half_spread_num=half_spread_exact.numerator, half_spread_den=half_spread_exact.denominator,
        shrink_KK=shrink_KK, shrink_tree=shrink_tree, both_shrink=both_shrink,
        maxabs_unscr=maxabs_unscr, maxabs_scr=maxabs_scr,
        shrink_factor_worst=shrink_factor_worst, mid_unscr=mid_unscr, mid_scr=mid_scr,
        mid_factor=mid_factor,
        r_KK_scr_RG=r_KK_scr_RG, mH_scr_RG_KK=mH_scr_RG_KK,
        conv_sens_dev=conv_sens_dev, convention_sensitive=convention_sensitive,
        mH_2loop_noBCS=mH_2loop_noBCS, mH_tree_A10=mH_tree_A10,
        m_H_obs=float(m_H_obs), m_H_FW_KK_threshold=float(m_H_FW_KK_threshold),
        m_H_FW_tree=float(m_H_FW_tree),
    ))
    # the gate's decisive PRIMARY-route value
    res["value"] = maxabs_scr
    return res


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict (composite collapse per gate-verdicts.md schema-v2)
# ---------------------------------------------------------------------------

def evaluate_gate(R: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict)."""
    maxabs_scr = R["maxabs_scr"]  # (local)

    # SIGN: direction predicted = BOTH anchors move DOWN (toward 0); keys on
    # per-anchor monotone shrink AND root-exists (the screening exists at all).
    sign_pass = bool(R["both_shrink"] and R["root_exists"] and R["monotone_decreasing_RG"])  # (local)
    sign_verdict = "PASS" if sign_pass else "FAIL"  # (local)

    # MAGNITUDE: max_a |r_a^scr| vs ceilings.
    if maxabs_scr <= PASS_CEILING:
        magnitude_verdict = "PASS"   # (local)
    elif maxabs_scr <= INFO_CEILING:
        magnitude_verdict = "INFO"   # (local)
    else:
        magnitude_verdict = "FAIL"   # (local)

    # REGIME: the integration regime (2-loop SM RG within validity) + the gate's
    # OWN structural pre-conditions: root unique, delta-consistent, NOT
    # convention-sensitive. A breach of delta-consistency OR convention-sensitivity
    # is a MARGINAL regime per the INFO_meaning (closure works but BCS attribution
    # / transfer convention weakens). Loss of root or non-monotone => BREAKDOWN.
    if not (R["root_exists"] and R["monotone_decreasing_RG"] and R["both_shrink"]):
        regime_verdict = "BREAKDOWN"  # (local)
    elif (not R["root_unique"]) or (not R["delta_consistent"]) or R["convention_sensitive"]:
        regime_verdict = "MARGINAL"   # (local)
    else:
        regime_verdict = "VALID"      # (local)

    # composite collapse (pre-registered rule; gate-verdicts.md)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"            # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"            # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"            # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"           # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"           # (local)
    elif regime_verdict == "MARGINAL":
        composite = "INFO"           # (local)  delta-consistency / convention-sensitivity caveat
    else:
        composite = "PASS"           # (local)
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload emission (race-safe; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          value_string, extra_rows):
    payload: dict = {  # (local)
        "session": 101,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_string,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "extra_rows": list(extra_rows),
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------

def make_plot(R: dict):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    fig.suptitle("S101-M0-BCS-SCREENING: S62 BCS screening transferred to M0^{sector} (band-shrink)",
                 fontsize=12, fontweight="bold")

    # Panel (a): m_H^scr,RG(delta) scan + root + delta=0.07 window
    ax = axes[0]
    ax.plot(R["delta_scan"], R["mH_scan"], "b-", lw=2, label=r"$m_H^{scr,RG}(\delta)$ (2-loop)")
    ax.axhline(R["m_H_obs"], color="red", ls="--", lw=1.5, label=fr"$m_H^{{obs}}={R['m_H_obs']}$")
    if R["root_exists"] and not np.isnan(R["delta_solve"]):
        ax.axvline(R["delta_solve"], color="red", ls=":", lw=1.2,
                   label=fr"$\delta^{{solve}}={R['delta_solve']:.4f}$")
    ax.axvspan(DELTA_TARGET - DELTA_WINDOW, DELTA_TARGET + DELTA_WINDOW,
               color="green", alpha=0.15, label=fr"$\delta$-consistency $0.07\pm0.03$")
    ax.axvline(DELTA_TARGET, color="orange", ls=":", lw=1, label=r"$\delta_{BCS}^{est}=0.07$")
    ax.set_xlabel(r"$\delta_{BCS}$")
    ax.set_ylabel(r"$m_H$ (GeV)")
    ax.set_title("(a) Conjunct-1 root-solve + Conjunct-2 $\\delta$-consistency")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    # Panel (b): band shrink — unscreened vs PRIMARY screened (exact rationals)
    ax = axes[1]
    anchors = ["KK (131.8)", "tree (134.0)"]
    unscr = [R["r_KK_unscr"]*100, R["r_tree_unscr"]*100]   # (local) %
    scr = [R["r_KK_scr"]*100, R["r_tree_scr"]*100]         # (local) %
    x = np.arange(len(anchors))                            # (local)
    w = 0.35                                               # (local)
    ax.bar(x - w/2, unscr, w, color="#e17055", edgecolor="black", label="unscreened (inherited)")
    ax.bar(x + w/2, scr, w, color="#2ecc71", edgecolor="black", label="screened (PRIMARY)")
    ax.axhline(0, color="black", lw=0.8)
    ax.axhspan(-PASS_CEILING*100, PASS_CEILING*100, color="green", alpha=0.08,
               label=fr"PASS $|r|\leq{PASS_CEILING}$")
    for xi, v in zip(x - w/2, unscr):
        ax.text(xi, v + 0.1, f"{v:.3f}", ha="center", va="bottom", fontsize=8)
    for xi, v in zip(x + w/2, scr):
        off = 0.1 if v >= 0 else -0.25
        ax.text(xi, v + off, f"{v:.3f}", ha="center", va="bottom" if v >= 0 else "top", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels(anchors)
    ax.set_ylabel(r"$\delta M_0/M_0$ residual (%)")
    ax.set_title(fr"(b) Band $[+5.356\%,+7.114\%]\to[-1.642\%,0]$; max$|r|$ factor {R['shrink_factor_worst']:.2f}")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy, informational): {closure[:16]}...")
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    R = compute()

    print("=" * 72)
    print("CONJUNCT 1 — delta_BCS^solve root-solve (re-run S62 2-loop machinery)")
    print("=" * 72)
    print(f"  m_H^scr,RG scan range: [{R['mH_scan'].min():.3f}, {R['mH_scan'].max():.3f}] GeV")
    print(f"  m_H(delta=0) [2-loop, no BCS]   = {R['mH_2loop_noBCS']:.4f} GeV")
    print(f"  monotone DECREASING in delta?   = {R['monotone_decreasing_RG']}")
    print(f"  n_roots (m_H^scr,RG = 125.1)    = {R['n_roots']}  exists={R['root_exists']} unique={R['root_unique']}")
    print(f"  delta_BCS^solve                 = {R['delta_solve']:.6f}")
    print(f"  root residual |m_H - 125.1|     = {R['root_resid']:.2e} GeV")

    print("\n" + "=" * 72)
    print("CONJUNCT 2 — delta-consistency with documented 0.07")
    print("=" * 72)
    print(f"  |delta_solve - 0.07|            = {R['delta_consistency_dev']:.6f}  (window +/-{DELTA_WINDOW})")
    print(f"  delta-consistent?               = {R['delta_consistent']}")
    print(f"  delta_BCS direct (BdG a4 PV)    = {R['delta_BCS_direct']:.4e}")

    print("\n" + "=" * 72)
    print("CONJUNCT 3 PRIMARY — m_H-level first-power transfer (EXACT rationals)")
    print("=" * 72)
    print(f"  UNSCREENED: r_KK = 67/1251 = {R['r_KK_unscr']*100:.4f}%, r_tree = 89/1251 = {R['r_tree_unscr']*100:.4f}%")
    print(f"  SCREENED:   r_tree^scr = 0 EXACT (BY CALIBRATION, DISCLOSED)")
    print(f"              r_KK^scr   = {R['r_KK_scr_num']}/{R['r_KK_scr_den']} = {R['r_KK_scr']*100:.4f}% EXACT (= 131.8/134 - 1)")
    print(f"  per-anchor shrink: KK={R['shrink_KK']} tree={R['shrink_tree']} BOTH={R['both_shrink']}")
    print(f"  max|r| unscr = {R['maxabs_unscr']*100:.4f}% -> scr = {R['maxabs_scr']*100:.4f}%  factor {R['shrink_factor_worst']:.3f}")
    print(f"  midpoint     = {R['mid_unscr']*100:.4f}% -> {R['mid_scr']*100:.4f}%  factor {R['mid_factor']:.3f}")
    print(f"  irreducible remnant (half-spread) = {R['half_spread_num']}/{R['half_spread_den']} = {R['maxabs_unscr']*0+ (R['half_spread_num']/R['half_spread_den'])*100:.4f}%")
    print(f"  PASS ceiling {PASS_CEILING}: max|r_scr| at {R['maxabs_scr']/PASS_CEILING*100:.1f}% of ceiling")

    print("\n" + "=" * 72)
    print("CONJUNCT 3 SECONDARY — KK-boundary RG transfer (convention-sensitivity diagnostic)")
    print("=" * 72)
    print(f"  m_H^scr,RG,KK(delta_solve)      = {R['mH_scr_RG_KK']:.4f} GeV")
    print(f"  r_KK^scr,RG (secondary)         = {R['r_KK_scr_RG']*100:.4f}%")
    print(f"  |r_KK^scr,PRIM - r_KK^scr,RG|   = {R['conv_sens_dev']:.6f}  (tol {CONV_SENS_TOL})")
    print(f"  CONVENTION-SENSITIVE flag       = {R['convention_sensitive']}")

    composite, sign_v, mag_v, regime_v = evaluate_gate(R)

    print("\n" + "=" * 72)
    print("GATE VERDICT")
    print("=" * 72)
    print(f"  sign_verdict      = {sign_v}   (both anchors monotone-shrink toward 0; root exists)")
    print(f"  magnitude_verdict = {mag_v}   (max|r_scr| = {R['maxabs_scr']:.6f} vs {PASS_CEILING}/{INFO_CEILING})")
    print(f"  regime_verdict    = {regime_v}")
    print(f"  COMPOSITE         = {composite}")

    # ---- save npz (full float64 round-trip; Class-8.3) ----
    save = {k: v for k, v in R.items() if k != "value"}  # (local)
    save["value_maxabs_r_scr"] = R["value"]
    save["composite_verdict"] = composite
    save["sign_verdict"] = sign_v
    save["magnitude_verdict"] = mag_v
    save["regime_verdict"] = regime_v
    save["PASS_CEILING"] = PASS_CEILING
    save["INFO_CEILING"] = INFO_CEILING
    save["DELTA_TARGET"] = DELTA_TARGET
    save["DELTA_WINDOW"] = DELTA_WINDOW
    save["CONV_SENS_TOL"] = CONV_SENS_TOL
    save["audit_sha256"] = audit_sha
    save["content_sha256"] = content_sha
    np.savez(OUT_NPZ, **save)
    print(f"\n  Data saved: {OUT_NPZ.name}")

    make_plot(R)

    # ---- value string for the verdict line (exact rationals + key contingencies) ----
    conv_flag = "CONVENTION-SENSITIVE" if R["convention_sensitive"] else "conv-stable"  # (local)
    value_string = (
        f"max|r_scr|={R['maxabs_scr']:.4f}(r_KK_scr=-11/670=-0.01642,r_tree_scr=0_BY_CALIBRATION);"
        f"delta_solve={R['delta_solve']:.4f}(|d-0.07|={R['delta_consistency_dev']:.4f},consistent={R['delta_consistent']});"
        f"root:exists={R['root_exists']},unique={R['root_unique']};"
        f"both_shrink={R['both_shrink']}(KK:7.114->1.642%,tree:5.356->0%);"
        f"factor_worst={R['shrink_factor_worst']:.2f};unscr_band=[67/1251,89/1251];"
        f"remnant=11/1251=0.879%;SECONDARY:r_KK_scr_RG={R['r_KK_scr_RG']:.4f},dev={R['conv_sens_dev']:.4f},{conv_flag}"
    )  # (local)
    extra_rows = [
        f"# regulator_pin: a_4^{{Pauli-Villars}} (BdG anomalous-self-energy delta_a4/a_4={R['delta_a4_over_a4']:.4e}); "
        f"a_4/a_2 ratio_gilkey={R['ratio_gilkey']:.6f} is a_n^{{zeta}} Seeley-DeWitt # {GATE_ID} regulator companion",
        f"# calibration_disclosure: r_tree^scr=0 BY CALIBRATION (m_H_obs used once on tree anchor); "
        f"discriminating content = root existence+uniqueness, delta-consistency, KK-anchor screened residual -11/670, "
        f"per-anchor monotonicity, SECONDARY-route convergence # {GATE_ID} disclosure",
    ]  # (local)

    print_verdict_payload(composite, R["value"], audit_sha, content_sha,
                          sign_v, mag_v, regime_v, value_string, extra_rows)

    tag = (f"(value={R['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
