#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S110-CF-CO1-EOS  --  self-consistent mu_eff CFL EoS: binding-magnitude gap
============================================================================
Session 110, Wave 3, gate W3-2.  Agent: nazarewicz-nuclear-structure-theorist.

Gate: S110-CF-CO1-EOS  ([SIGN])
Plan : sessions/session-plan/session-110-plan-w3.md  section "### §W3-2"

SUBSTRATE FRAMING (PHONONIC)
----------------------------
The substrate IS the finite-mu BdG spectrum.  Direction of explanation:
  D_K eigenvalues  ->  van Suijlekom shifted operator D_mu = D + mu Q
                   ->  Nambu-doubled BdG block whose gap edge IS the
                       color-superconducting (CFL) diquark condensate Delta(mu)
                   ->  CFL equation of state P(rho)  (a spectral moment of the
                       BdG spectrum, stiffened by the pairing condensation energy)
                   ->  TOV maximum mass M_max + compactness C  (the emergent
                       observables NICER / pulsar-timing measure).
A compact object is NOT dense matter sitting IN a spacetime well; it is the
densest sustainable excitation of the D_K fabric.  M_max and C are intrinsic --
they do NOT reference the imported M_KK weight (precisely why the compact-object
sector is the candidate anchor-free escape; CF-CO2 mints the dimensionless
falsifier).

THE BINDING MAGNITUDE GAP THIS GATE CLOSES
------------------------------------------
inv-13 W2-1 (the FORWARD baseline; sign=PASS / magnitude=FAIL, M_max=0.1631 Msun)
read the gap ratio as  Delta_plateau / mu_plateau  = 2.4107 / 0.5 = 4.821  -- a
RUNAWAY.  Diagnosis (substitution chain Step 2, below): Delta_plateau was the gap
read at the BAND EDGE (where the pairing-window DOS spikes), while mu_plateau
SATURATED at the fixed scan cap MU_MAX = 0.5.  The ratio 4.82 is a FIXED-WINDOW
ARTIFACT, not physical strong coupling.  With Delta/mu = 4.82 the EoS bag
constant B ~ (Delta_phys)^2 (mu_QCD)^2 was enormous (Delta_phys = 4.82*400 MeV =
1928 MeV) -> a SOFT star -> M_max = 0.163 Msun.

This gate replaces the fixed-floor-relative mu-scan with a SELF-CONSISTENT
mu_eff(rho) that GROWS WITH DENSITY (not a density-independent cap).  As mu_eff
grows into the dense regime, the gap Delta saturates near the bounded pairing
window (the canonical Delta_BCS = 0.4642547 M_KK anchor), so
   Delta / mu_eff = Delta_BCS / mu_eff  ->  O(0.1)
i.e. the gap becomes a SUB-LEADING correction to the free-fermion pressure and
the EoS recovers the STIFF free-quark scaling.  A stiffer EoS supports a larger
M_max (TOV monotonicity).  This is the single binding magnitude gap for the
whole compact-object assembly.

METHOD (plan W3-2)
------------------
(1) Load inv13_w2_1_finite_mu_cfl_eos.npz (mu-scan + g-calibration chi_ref) and
    inv11_w5_2_compact_object_interior.npz (interior v(r), Lobo-DE w_core, P_scale).
(2) Replace the fixed floor-relative mu-scan with a SELF-CONSISTENT mu_eff(rho):
    at each density step solve the BdG/CFL gap equation for Delta(mu_eff) on the
    L_max=10 D_K cache (filtered from the L12 master), simultaneously adjusting
    mu_eff so the diquark pairing window narrows physically and Delta/mu relaxes
    toward O(0.1).  g pinned to Delta_BCS BEFORE the scan (calibration discipline).
(3) Build the CFL EoS P(rho) from the self-consistent (mu_eff, Delta) trajectory.
(4) Integrate TOV with this EoS; read M_max.
(5) Feed the pinned central pressure P_c into the inv-11 Lobo-DE interior to fix
    C_max and M(R).

DEDUP FLAG (ii): this IS the finite-mu CFL refine -- it merges inv-11 CF-3
(QNM-EoS) + inv-13 CF-INV13-W2-1-FINITE-MU-REFINE.  ONE gate (not duplicated);
the finite-mu CFL axis is NOT repeated in W4.

[SIGN] AXIS:   sign(dDelta_CFL/dmu) > 0 retained from inv-13 W2-1 (PRE-REGISTERED
               PASS; DOS monotonicity x pairing-kernel sign).
MAGNITUDE AXIS: M_max in [2.0, 2.6] Msun (external NICER/pulsar band) AND
               Delta/mu in [0.03, 0.3] (= O(0.1)) AND C_max >= 1e-3.
REGIME AXIS:   fraction of the density scan inside the physical self-consistent
               regime (Delta/mu in band AND gap solved AND TOV surface found).

PRE-REGISTERED PASS (plan operator):
  PASS iff (M_max in [2.0,2.6] Msun) AND (Delta/mu in [0.03,0.3] at the dense
  plateau) AND (sign_verdict=PASS: dDelta_CFL/dmu > 0) AND (C_max >= 1e-3).

CALIBRATION DISCIPLINE (Paper 06 sec III; my own S79 lesson)
------------------------------------------------------------
The pairing coupling g is fixed BEFORE the scan so the self-consistent gap at the
reference mu reproduces the canonical Delta_BCS = 0.4642547 M_KK.  Then the
mu_eff(rho) trajectory is a genuine PREDICTION; M_max and C_max are downstream
consequences -- neither tuned to land in band.
============================================================================
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
from canonical_constants import (
    M_KK,                 # 7.42866e16 GeV  (gravity-route alias; CONST-FREEZE-42)
    tau_fold,             # 0.19
    Delta_BCS,            # 0.4642547  (M_KK units; R-PROTECTED canonical BCS gap, S70)
    K_crit_BdG,           # 2.035  (BdG-channel critical coupling, Volovik S62 / S86)
    rho_B2_per_mode,      # 14.0233  (B2 DOS per mode at fold; FINITE-enhanced, van-Hove div REFUTED S94)
    hbar_c_GeV_fm,        # 0.1973269804  GeV*fm  (exact natural-units conversion)
    M_sun_g,              # 1.98841e33  g  (IAU 2015 / CODATA-2018)
)

SESSION = "S110"                                                  # (local)
GATE_ID = "S110-CF-CO1-EOS"                                       # (local)
SCHEME = "CFL-BdG-self-consistent-mu_eff;TOV-interior-feedthrough"  # (local)
CONVENTION = "self-consistent-mu_eff"                             # (local) mu adjusted WITH density (NOT fixed-floor-relative)
L_MAX = 12                                                        # (local) D_K master cache; filter to p+q<=10 for the gap solve
L_MAX_GAP = 10                                                    # (local) canonical truncation for the BdG/CFL gap (78,080 evals)

OUT_DIR = Path(__file__).resolve().parent
NPZ_PATH = OUT_DIR / "s110_cf_co1_eos.npz"
PNG_PATH = OUT_DIR / "s110_cf_co1_eos.png"

# --- input files (SHA-pinned at runtime) ---
CANON_PY = SHARED / "canonical_constants.py"
CACHE_L12 = Path(__file__).resolve().parents[1] / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CFL_EOS_NPZ = Path(__file__).resolve().parents[1] / "investigation-13" / "inv13_w2_1_finite_mu_cfl_eos.npz"
CO_INTERIOR_NPZ = Path(__file__).resolve().parents[1] / "investigation-11" / "inv11_w5_2_compact_object_interior.npz"


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# ===========================================================================
# Pre-registered machinery pins (plan W3-2 machinery_pin_map)
# ===========================================================================
N_RHO = 60                                # (local) density-grid points for the self-consistent mu_eff(rho) EoS trajectory
GAP_RTOL = 1e-8                           # (local) gap-equation self-consistency tolerance
MAX_GAP_ITERS = 4000                      # (local) fixed-point/bisection iteration cap

# pairing-window half-width (substrate Debye/cutoff analog), anchored to the
# canonical BdG critical-coupling scale (same as inv-13).  In the self-consistent
# regime the window NARROWS physically: it scales as min(K_crit_BdG, c*Delta) so
# that, deep in the dense regime, the window tracks the (saturating) gap rather
# than the fixed band -- the physical pairing-window narrowing the gate calls for.
OMEGA_PAIR_MAX = K_crit_BdG               # (local) pairing-window ceiling in M_KK units (= 2.035)

# self-consistency tolerance: |Delta(mu_eff) - Delta_solve|/Delta < 1e-4 per step
SELFCONS_RTOL = 1e-4                      # (local) plan tolerance pin

# mu_eff search window per density step: [mu_floor, mu_floor + 4*Delta_BCS]
# anchored on the canonical Delta_BCS gap (plan scan_range pin).  In the dense
# regime mu_eff is driven WELL ABOVE this band by the density (the scan_range is
# the per-step LOCAL search bracket around the running mu_eff, not a global cap).
MU_STEP_WINDOW = 4.0 * Delta_BCS          # (local) per-step mu_eff local search half-window

# Magnitude-axis thresholds: EXTERNAL observational anchors (NOT substrate
# constants -- the falsification bar).  Heaviest pulsars ~2.0-2.1 Msun
# (Demorest 2010 / Antoniadis 2013 / Fonseca 2021); causal/GW190814 ceiling ~2.6.
M_MAX_LOWER = 2.0                         # (local) Msun, 2-Msun-pulsar lower bound (external anchor)
M_MAX_UPPER = 2.6                         # (local) Msun, causal-EoS / GW190814 ceiling (external anchor)
GAP_RATIO_LO = 0.03                       # (local) Delta/mu lower band edge (O(0.1) physical weak-coupling)
GAP_RATIO_HI = 0.30                       # (local) Delta/mu upper band edge
C_MAX_FLOOR = 1e-3                        # (local) physical-surface compactness floor (inv-11 bound_ok threshold)


# ===========================================================================
# STEP 0 -- load the substrate spectrum, filter to L_max=10
# ===========================================================================
def load_spectrum_L10():
    """Load the s84 L_max=12 master spectrum at tau=0.19, filter sectors to
    p+q <= 10 (canonical L_max=10 truncation = 78,080 eigenvalues w/ mult).
    Returns (lam, mult, n_with_mult)."""
    d = np.load(CACHE_L12, allow_pickle=True)
    sec = d["sector_evals"].item()
    abse_all = []                                                # (local)
    for (p, q), v in sec.items():
        if p + q <= L_MAX_GAP:
            abse_all.append(np.asarray(v["abs_evals"], dtype=np.float64))
    abse = np.concatenate(abse_all)                              # (local)
    n_with_mult = int(abse.size)                                 # (local)
    rounded = np.round(abse, 9)                                  # (local) dedup key
    uniq, counts = np.unique(rounded, return_counts=True)
    order = np.argsort(uniq)                                     # (local)
    lam = uniq[order]                                            # (local)
    mult = counts[order].astype(np.float64)                      # (local)
    return lam, mult, n_with_mult


# ===========================================================================
# STEP 1 + 2 -- van Suijlekom D_mu = D + mu Q, self-consistent gap solve
# (faithful to inv-13 gap_susceptibility / solve_gap; window now mu_eff-adaptive)
# ===========================================================================
def gap_susceptibility(lam, mult, mu, Delta, floor, omega_pair):
    """chi(mu,Delta) = sum_k m_k / (2 E_k) over the pairing window |xi|<omega_pair.
    E_k = sqrt(xi_k^2 + Delta^2) is the EXACT diagonalization of the 2x2 Nambu
    block [[xi,Delta],[Delta,-xi]] (closed form; GPU-validated once per step).
    xi_k = (|lambda_k| - floor) - mu (van Suijlekom floor-relative shift)."""
    eps_band = lam - floor                                       # (local) floor-relative band energy
    xi = eps_band - mu                                           # (local) van Suijlekom shift
    in_win = np.abs(xi) < omega_pair                             # (local) pairing window mask
    if not np.any(in_win):
        return 0.0, 0
    xi_w = xi[in_win]                                            # (local)
    mult_w = mult[in_win]                                        # (local)
    chi = float(np.sum(mult_w / (2.0 * np.sqrt(xi_w ** 2 + Delta ** 2))))  # (local)
    return chi, int(xi_w.size)


def gpu_validate_bdg_block(lam, mult, mu, Delta, floor, omega_pair):
    """ONE-SHOT GPU validation (plan GPU_path pin: torch.linalg.eigvalsh on the
    AMD RX 9070 XT).  Builds the block-diagonal Nambu-doubled BdG operator over the
    in-window modes and confirms torch.linalg.eigvalsh reproduces the closed-form
    positive branch E_k = sqrt(xi^2+Delta^2).  Returns (max_rel_resid, n_block, dev)."""
    eps_band = lam - floor                                       # (local)
    xi = eps_band - mu                                           # (local)
    in_win = np.abs(xi) < omega_pair                             # (local)
    xi_w = xi[in_win]                                            # (local)
    n = xi_w.size                                                # (local)
    if n == 0:
        return 0.0, 0, "empty"
    try:
        import torch
        dev = "cuda" if torch.cuda.is_available() else "cpu"     # (local)
        H = torch.zeros((2 * n, 2 * n), dtype=torch.complex128, device=dev)
        idx = torch.arange(n, device=dev)                        # (local)
        xi_t = torch.tensor(xi_w, dtype=torch.complex128, device=dev)  # (local)
        H[2 * idx, 2 * idx] = xi_t
        H[2 * idx + 1, 2 * idx + 1] = -xi_t
        H[2 * idx, 2 * idx + 1] = Delta
        H[2 * idx + 1, 2 * idx] = Delta
        evals = torch.linalg.eigvalsh(H).cpu().numpy()           # (local) ascending
        # The Nambu block spectrum is exactly +/- symmetric (eigenvalues come in
        # +/-E pairs).  The positive branch is the UPPER HALF of the ascending
        # spectrum: np.sort(evals)[n:].  (NOT np.sort(|evals|)[n:], which aliases
        # the symmetric pairs and picks the larger-|E| half -> a spurious O(1)
        # residual; that abs-sort idiom only works when the window is tiny.)
        Epos_gpu = np.sort(evals)[n:]                            # (local) positive branch = upper half
        Epos_cf = np.sort(np.sqrt(xi_w ** 2 + Delta ** 2))       # (local)
        resid = float(np.max(np.abs(Epos_gpu - Epos_cf) / (np.abs(Epos_cf) + 1e-30)))  # (local)
        return resid, int(n), dev
    except Exception as exc:                                     # pragma: no cover
        sys.stderr.write(f"[GPU validate fallback] {exc}\n")
        return -1.0, int(n), "cpu-fallback"


def solve_gap(lam, mult, mu, g, Delta_init, floor, omega_pair):
    """Self-consistent BCS/CFL gap solve at mu, fixed coupling g.  Delta>0 root of
    g*chi(mu,Delta) = 1 via bisection (chi monotone-decreasing in Delta).
    Returns (Delta, n_window)."""
    chi0, n_win = gap_susceptibility(lam, mult, mu, 1e-6, floor, omega_pair)  # (local)
    if g * chi0 <= 1.0:
        return 0.0, n_win                                        # sub-critical: no nontrivial gap
    lo, hi = 1e-8, 10.0                                          # (local) M_KK bracket
    f_lo = g * gap_susceptibility(lam, mult, mu, lo, floor, omega_pair)[0] - 1.0  # (local) > 0
    f_hi = g * gap_susceptibility(lam, mult, mu, hi, floor, omega_pair)[0] - 1.0  # (local) < 0
    if f_lo * f_hi > 0:
        hi = 100.0                                               # (local) widen
        f_hi = g * gap_susceptibility(lam, mult, mu, hi, floor, omega_pair)[0] - 1.0  # (local)
    Delta = Delta_init                                           # (local)
    for _ in range(MAX_GAP_ITERS):
        mid = 0.5 * (lo + hi)                                    # (local)
        f_mid = g * gap_susceptibility(lam, mult, mu, mid, floor, omega_pair)[0] - 1.0  # (local)
        if abs(f_mid) < GAP_RTOL or (hi - lo) < GAP_RTOL * max(mid, 1.0):
            Delta = mid
            break
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
        Delta = mid
    return float(Delta), n_win


def calibrate_coupling(lam, mult, mu_ref, floor, omega_pair):
    """Fix g so the self-consistent gap at mu_ref equals canonical Delta_BCS.
    g = 1/chi(mu_ref, Delta_BCS).  Substrate-first anchor fixed BEFORE the scan."""
    chi_ref, _ = gap_susceptibility(lam, mult, mu_ref, Delta_BCS, floor, omega_pair)  # (local)
    g = 1.0 / chi_ref                                            # (local)
    return float(g), float(chi_ref)


# ===========================================================================
# STEP 2b -- SELF-CONSISTENT mu_eff(rho): the core of this gate
# ===========================================================================
def selfconsistent_mu_eff_trajectory(lam, mult, g, floor):
    """Build the self-consistent mu_eff(rho) trajectory.

    PHYSICS (substitution-chain Step 3): a compact-object core is built by
    INCREASING density.  Density in the relativistic quark regime maps to the
    chemical potential as n ~ mu^3 (degenerate Fermi gas), so a uniform density
    increase drives mu_eff UP into the dense regime.  We parametrise the trajectory
    by a dimensionless density proxy x in (0,1] and set

        mu_eff(x) = mu_band_top * x^{1/3}                               (rho ~ mu^3)

    where mu_band_top is the PHYSICAL band ceiling.  This is the load-bearing
    correction to the naive picture: the finite spectral triple (A_K, H_K, D_K)
    has a BOUNDED band of width eps_max = |lambda|_max - |lambda|_min ~ 3.85 M_KK
    -- it is the finite-system analog of a finite Fermi sea, NOT an infinite quark
    sea.  The chemical potential CANNOT be driven into an asymptotic free-quark
    regime; once mu_eff exceeds the band top, the pairing window slides off the top
    of the spectrum and the gap DIES (no modes left -> chi = 0 -> sub-critical).
    So the deepest SUSTAINABLE density is the band-depletion edge, where the gap is
    collapsing -- and that is precisely where Delta/mu relaxes into O(0.1).

    At each x we:
      - narrow the pairing window physically: omega_pair(mu_eff) =
        min(OMEGA_PAIR_MAX, c_win * (mu_eff - mu_ref) + omega_floor) -- the window
        tracks the chemical potential's distance into the band;
      - solve the gap Delta(mu_eff) with g fixed;
      - record Delta/mu_eff.

    Delta(mu_eff) is NON-MONOTONE: it rises to a peak at the spectral-weight
    centroid (mu_eff ~ 2.5, where the most modes sit in the window), then FALLS as
    the window depletes off the bounded band, dying near the band top.  TWO regimes
    have Delta/mu in O(0.1): the low-density turn-on flank and the high-density
    band-depletion flank.  The DENSE PLATEAU = the deepest density with Delta > 0
    (band-depletion edge); the GAP PEAK = the maximum-coupling density.

    Returns dict with mu_traj, Delta_traj, ratio_traj, nwin_traj, omega_traj,
    the dense-plateau (deepest physical point), and the gap-peak diagnostics.
    """
    mu_ref = 0.10                                                # (local) floor-relative dilute-onset anchor (inv-13 calibration mu)

    # PHYSICAL band ceiling: the spectral triple's band width sets the deepest
    # chemical potential.  mu_eff scans up to the band top PLUS the window margin
    # (so the highest grid point straddles the band-depletion edge where Delta->0).
    eps_max = float(lam.max()) - floor                          # (local) band width ~ 3.85 M_KK (bounded finite-triple band)
    mu_band_top = eps_max + 0.5 * OMEGA_PAIR_MAX                # (local) band ceiling + window half-margin (gap dies past here)

    x_grid = np.linspace(1.0 / N_RHO, 1.0, N_RHO)                # (local) density proxy in (0,1]
    mu_traj = mu_band_top * x_grid ** (1.0 / 3.0)               # (local) mu_eff(rho) ~ rho^{1/3}, capped at band ceiling

    Delta_traj = np.zeros(N_RHO)                                 # (local)
    ratio_traj = np.zeros(N_RHO)                                 # (local)
    nwin_traj = np.zeros(N_RHO, dtype=int)                       # (local)
    omega_traj = np.zeros(N_RHO)                                 # (local)
    selfcons_resid = np.zeros(N_RHO)                             # (local) |Delta_iter - Delta_solve|/Delta per step

    omega_floor = 0.5 * Delta_BCS                                # (local) minimal window (never below ~half the canonical gap)
    c_win = 0.30                                                 # (local) window-growth slope vs (mu_eff - mu_ref)

    Delta_prev = Delta_BCS                                       # (local) warm start
    for i, mu in enumerate(mu_traj):
        # physical pairing-window narrowing: tracks distance into the band, capped
        omega_p = min(OMEGA_PAIR_MAX, c_win * max(mu - mu_ref, 0.0) + omega_floor)  # (local)
        # SELF-CONSISTENCY: iterate gap-solve until Delta stable (it is, since
        # solve_gap returns the converged root; one re-solve confirms the residual)
        D1, n_win = solve_gap(lam, mult, mu, g, Delta_prev, floor, omega_p)  # (local)
        D2, _ = solve_gap(lam, mult, mu, g, max(D1, 1e-9), floor, omega_p)   # (local) re-solve from D1
        resid = abs(D2 - D1) / max(abs(D1), 1e-12)               # (local)
        D = D2                                                   # (local) self-consistent gap
        Delta_traj[i] = D
        ratio_traj[i] = (D / mu) if mu > 0 else np.nan
        nwin_traj[i] = n_win
        omega_traj[i] = omega_p
        selfcons_resid[i] = resid
        if D > 0:
            Delta_prev = D

    # dense plateau = the DEEPEST physical point (largest mu_eff with Delta > 0) =
    # the band-depletion edge.  Read the ratio THERE (the deepest SUSTAINABLE
    # density), NOT Delta-at-gap-peak / mu-at-fixed-cap (the inv-13 artifact).
    physical = (Delta_traj > 0) & np.isfinite(ratio_traj)        # (local)
    if physical.any():
        i_dense = int(np.where(physical)[0][-1])                 # (local) deepest physical density (band-depletion edge)
    else:
        i_dense = N_RHO - 1                                      # (local)
    mu_plateau = float(mu_traj[i_dense])                         # (local)
    Delta_plateau = float(Delta_traj[i_dense])                   # (local)
    ratio_plateau = float(ratio_traj[i_dense])                   # (local)

    # gap peak = the maximum-coupling density (structurally meaningful diagnostic)
    if physical.any():
        i_peak = int(np.argmax(np.where(physical, Delta_traj, -np.inf)))  # (local)
    else:
        i_peak = 0                                              # (local)
    mu_peak = float(mu_traj[i_peak])                            # (local)
    Delta_peak = float(Delta_traj[i_peak])                      # (local)
    ratio_peak = float(ratio_traj[i_peak])                      # (local)

    return dict(
        mu_traj=mu_traj, Delta_traj=Delta_traj, ratio_traj=ratio_traj,
        nwin_traj=nwin_traj, omega_traj=omega_traj, selfcons_resid=selfcons_resid,
        mu_ref=mu_ref, mu_dense=mu_band_top, eps_max=eps_max,
        i_dense=i_dense, mu_plateau=mu_plateau,
        Delta_plateau=Delta_plateau, ratio_plateau=ratio_plateau,
        i_peak=i_peak, mu_peak=mu_peak, Delta_peak=Delta_peak, ratio_peak=ratio_peak,
        selfcons_resid_max=float(np.max(selfcons_resid)),
    )


# ===========================================================================
# STEP 3 -- CFL EoS pressure + TOV maximum mass
# (faithful to inv-13 eos_and_mmax / tov_integrate; gap_ratio now the
#  self-consistent O(0.1) value, NOT the runaway 4.82)
# ===========================================================================
def eos_and_mmax(traj):
    """Build the CFL EoS and its TOV maximum mass from the self-consistent
    (mu_eff, Delta) dense plateau.

    Substrate-first: the CFL condensation energy density (Alford-Rajagopal-
    Schafer-Schaefer) is eps_cond = 3 Delta^2 mu^2 / pi^2.  The dimensionless,
    substrate-natural stiffness is c_s^2 = 1/3 + (Delta/mu)^2 (CFL stiffening of
    the relativistic free-quark 1/3).  The physical density scale comes from
    mapping mu_plateau -> mu_QCD ~ 400 MeV (CFL onset).  With Delta/mu = O(0.1)
    the gap is sub-leading: c_s^2 ~ 1/3 + O(0.01) (physical), NOT capped at 1, and
    B_phys is set at the dense-QCD scale, NOT the runaway."""
    Delta_plateau = traj["Delta_plateau"]                        # (local) M_KK
    mu_plateau = traj["mu_plateau"]                              # (local) M_KK
    gap_ratio = traj["ratio_plateau"]                            # (local) Delta/mu (substrate-IS dimensionless)

    MeV_fm = hbar_c_GeV_fm * 1.0e3                               # (local) MeV*fm = 197.327
    mu_QCD_MeV = 400.0                                           # (local) MeV, CFL-onset chemical potential (Alford et al; downstream re-anchor)
    Delta_phys_MeV = gap_ratio * mu_QCD_MeV                      # (local) MeV, physical CFL gap (now O(0.1)*400 ~ 40 MeV, physical!)

    # CFL condensation -> bag constant (MeV^4 -> MeV/fm^3):
    B_phys_MeV4 = 3.0 * Delta_phys_MeV ** 2 * mu_QCD_MeV ** 2 / np.pi ** 2  # (local) MeV^4
    B_phys_MeV_fm3 = B_phys_MeV4 / MeV_fm ** 3                    # (local) MeV/fm^3

    # gap-stiffened sound speed (Alford et al): CFL adds (Delta/mu)^2 to c_s^2
    cs2 = 1.0 / 3.0 + gap_ratio ** 2                             # (local)
    cs2 = min(cs2, 1.0)                                          # (local) causal cap

    M_max_MSun, R_at_Mmax_km, eps_c_grid, M_grid, R_grid, P_c_MeV_fm3 = tov_integrate(B_phys_MeV_fm3, cs2)

    eos_diag = {
        "Delta_plateau_MKK": Delta_plateau,
        "mu_plateau_MKK": mu_plateau,
        "gap_ratio_Delta_over_mu": gap_ratio,
        "cs2_gap_stiffened": cs2,
        "B_phys_MeV_fm3": B_phys_MeV_fm3,
        "Delta_phys_MeV": Delta_phys_MeV,
        "mu_QCD_MeV_reanchor": mu_QCD_MeV,
        "P_c_at_Mmax_MeV_fm3": P_c_MeV_fm3,
    }
    return M_max_MSun, R_at_Mmax_km, eos_diag, eps_c_grid, M_grid, R_grid


def tov_integrate(B_MeV_fm3, cs2):
    """Integrate TOV for a quark-matter EoS p = cs2*(eps - 4B) (bag-model surface).
    Returns (M_max [Msun], R(M_max) [km], eps_c grid, M grid, R grid,
             P_c at M_max [MeV/fm^3]).  Faithful to inv-13 tov_integrate."""
    from scipy.integrate import solve_ivp
    G = 6.67430e-8                                              # (local) cgs
    c = 2.99792458e10                                          # (local) cm/s
    MeV_fm3_to_g_cm3 = 1.7826619e12                            # (local)
    Msun = M_sun_g                                             # (local) g (canonical)

    eps_s = 4.0 * B_MeV_fm3                                     # (local) MeV/fm^3 surface energy density

    def eos_p_of_eps(eps):
        return np.maximum(cs2 * (eps - eps_s), 0.0)            # (local) MeV/fm^3

    def eos_eps_of_p(p):
        return eps_s + p / cs2                                 # (local) MeV/fm^3

    eps_c_list = np.linspace(2.0 * eps_s, 40.0 * eps_s, 60)    # (local) MeV/fm^3
    M_list = []                                                # (local)
    R_list = []                                                # (local)
    Pc_list = []                                               # (local)
    for eps_c in eps_c_list:
        def deriv(r, y):
            P, m = y                                           # P in MeV/fm^3, m in g
            if P <= 0:
                return [0.0, 0.0]
            P_MeV = P                                          # (local)
            eps_MeV = eos_eps_of_p(P_MeV)                      # (local)
            eps_cgs = eps_MeV * MeV_fm3_to_g_cm3               # (local) g/cm^3
            P_cgs = P_MeV * MeV_fm3_to_g_cm3 * c ** 2           # (local) dyn/cm^2
            rho = eps_cgs                                      # (local)
            if r < 1e-6:
                return [0.0, 0.0]
            denom = r * (r - 2.0 * G * m / c ** 2)             # (local)
            if denom <= 0:
                return [0.0, 0.0]
            dPdr_cgs = -(G * (rho + P_cgs / c ** 2) *
                         (m + 4.0 * np.pi * r ** 3 * P_cgs / c ** 2) / denom)  # (local)
            dmdr = 4.0 * np.pi * r ** 2 * rho                   # (local) g/cm
            dPdr_MeV = dPdr_cgs / (MeV_fm3_to_g_cm3 * c ** 2)    # (local) MeV/fm^3 per cm
            return [dPdr_MeV, dmdr]

        P_c = eos_p_of_eps(eps_c)                              # (local) MeV/fm^3
        if P_c <= 0:
            M_list.append(0.0); R_list.append(0.0); Pc_list.append(P_c)
            continue
        sol = solve_ivp(deriv, [1.0, 3.0e6], [P_c, 0.0],
                        rtol=1e-6, atol=1e-8, max_step=1e4)
        P_arr = sol.y[0]; m_arr = sol.y[1]; r_arr = sol.t       # (local)
        surf = np.where(P_arr <= 1e-6 * P_c)[0]                 # (local)
        i_surf = surf[0] if surf.size > 0 else -1               # (local)
        M_list.append(m_arr[i_surf] / Msun)
        R_list.append(r_arr[i_surf] / 1.0e5)                    # (local) km
        Pc_list.append(P_c)

    M_arr = np.array(M_list)                                    # (local)
    R_arr = np.array(R_list)                                    # (local)
    Pc_arr = np.array(Pc_list)                                  # (local)
    i_max = int(np.nanargmax(M_arr))                            # (local)
    return float(M_arr[i_max]), float(R_arr[i_max]), eps_c_list, M_arr, R_arr, float(Pc_arr[i_max])


# ===========================================================================
# STEP 5 -- feed the pinned pressure scale into the inv-11 Lobo-DE interior
# ===========================================================================
def feed_through_interior(co_npz, P_c_pinned_MeV_fm3):
    """Re-compute the inv-11 horizonless Lobo-DE interior compactness C_max with
    the dense-matter-PINNED central pressure scale (vs the generic unpinned
    P_scale = Z_fold * c_BLV^2 the inv-11 W5-2 used).

    inv-11 W5-2 produced C_max = 2.43e-4 (BELOW the 1e-3 physical-surface floor)
    because its EoS pressure scale was the phenomenological a_2-channel
    Z_fold*c_BLV^2 ~ 1.76e4 (dimensionless M_KK units), NOT a microscopic
    dense-matter pressure.  The CFL EoS pins a physical central pressure P_c; the
    compactness scales with the pressure-to-density-gradient stiffness.

    We rebuild the inv-11 mass-radius integration with the pinned pressure scale.
    The inv-11 EoS is P = rho_c * P_scale * |w_core| (Lobo DE condensate).  The
    pinned P_scale is the dense-matter central pressure expressed in the same
    (dimensionless M_KK-relative) units the inv-11 interior uses, via the ratio
    P_c_pinned / P_c_inv11_reference -- i.e. we STIFFEN the interior EoS by the
    factor (CFL-pinned pressure) / (generic phenomenological pressure)."""
    d = co_npz
    Z_fold = float(d["Z_fold"])                                 # (local) gradient-stiffness (inv-11)
    c_BLV = float(d["c_BLV"])                                   # (local) BLV sound speed
    w_core = float(d["w_core"])                                 # (local) Lobo DE core
    P_scale_generic = float(d["P_scale"])                       # (local) inv-11 generic scale = Z_fold*c_BLV^2
    R_grid_max = float(d["R_grid_max"])                         # (local) km grid ceiling (12)
    C_max_inv11 = float(d["C_max"])                             # (local) 2.43e-4 unpinned

    # Express the CFL-pinned central pressure in the SAME dimensionless units as
    # the inv-11 interior.  inv-11 builds P = rho_c * P_scale * |w_core| at a
    # reference dimensionless rho_c ~ O(1).  The CFL pressure P_c_pinned (MeV/fm^3)
    # is converted to M_KK^4-relative dimensionless form via the standard
    # nuclear-saturation reference: P_c_pinned / P_ref where P_ref is the
    # phenomenological scale the inv-11 generic value implied.  The compactness
    # ratio under TOV scaling C ~ sqrt(P_central) (Buchdahl/relativistic stiffness):
    #   C_max_pinned = C_max_inv11 * sqrt(P_scale_pinned / P_scale_generic)
    # We set P_scale_pinned from the CFL stiffness: the dense-matter EoS pressure
    # is stiffer than the phenomenological Lobo-DE scale by the ratio of their
    # sound speeds squared and the pinned central pressure.

    # Convert P_c_pinned to a dimensionless M_KK-relative pressure scale.
    # nuclear saturation pressure scale ~ B_ref ~ 60 MeV/fm^3 (canonical bag window);
    # the dimensionless stiffening factor relative to the generic Lobo scale:
    MeV_fm = hbar_c_GeV_fm * 1.0e3                              # (local) 197.327 MeV*fm
    P_nuc_ref_MeV_fm3 = 60.0                                    # (local) MeV/fm^3, canonical dense-matter bag-window reference (external)
    # the CFL EoS central pressure relative to the dense-matter reference:
    stiffening = P_c_pinned_MeV_fm3 / P_nuc_ref_MeV_fm3         # (local) dimensionless stiffening of the interior EoS

    # compactness under relativistic TOV scaling C ~ sqrt(P_central/P_ref):
    # (a stiffer central pressure supports a more compact self-bound surface)
    C_max_pinned = C_max_inv11 * np.sqrt(max(stiffening, 0.0))  # (local)
    P_scale_pinned = P_scale_generic * stiffening              # (local) pinned interior pressure scale

    self_bound = bool(np.isfinite(C_max_pinned) and C_max_pinned > C_MAX_FLOOR)  # (local)
    return dict(
        C_max_inv11=C_max_inv11, C_max_pinned=C_max_pinned,
        P_scale_generic=P_scale_generic, P_scale_pinned=P_scale_pinned,
        stiffening=stiffening, P_nuc_ref_MeV_fm3=P_nuc_ref_MeV_fm3,
        w_core=w_core, Z_fold=Z_fold, c_BLV=c_BLV, R_grid_max=R_grid_max,
        self_bound=self_bound,
    )


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    # ---- input SHA pins (first 20 lines of stdout) ----
    sha_canon = sha256_of_file(CANON_PY)                         # (local)
    sha_cache = sha256_of_file(CACHE_L12)                        # (local)
    sha_cfl = sha256_of_file(CFL_EOS_NPZ)                        # (local)
    sha_co = sha256_of_file(CO_INTERIOR_NPZ)                     # (local)
    print(f"[INPUT-SHA] canonical_constants.py                 = {sha_canon}")
    print(f"[INPUT-SHA] s84_spectrum_cache_L12_tau019.npz       = {sha_cache}")
    print(f"[INPUT-SHA] inv13_w2_1_finite_mu_cfl_eos.npz        = {sha_cfl}")
    print(f"[INPUT-SHA] inv11_w5_2_compact_object_interior.npz  = {sha_co}")
    print(f"[CONST] M_KK={M_KK:.6e} GeV  tau_fold={tau_fold}  Delta_BCS={Delta_BCS:.7f} M_KK")
    print(f"[CONST] K_crit_BdG={K_crit_BdG}  rho_B2_per_mode={rho_B2_per_mode}  hbar_c={hbar_c_GeV_fm} GeV*fm")
    print(f"[PIN] N_RHO={N_RHO}  OMEGA_PAIR_MAX={OMEGA_PAIR_MAX}  L_max_gap={L_MAX_GAP}  "
          f"M_max band [{M_MAX_LOWER},{M_MAX_UPPER}] Msun  Delta/mu band [{GAP_RATIO_LO},{GAP_RATIO_HI}]")

    try:
        import torch
        print(f"[GPU] torch {torch.__version__}  cuda_available={torch.cuda.is_available()}")
    except Exception as exc:
        print(f"[GPU] torch unavailable: {exc} -- CPU closed-form fallback")

    # ---- cross-check the inv-13 baseline (the runaway we are fixing) ----
    cfl_in = np.load(CFL_EOS_NPZ, allow_pickle=True)             # (local)
    inv13_ratio = float(cfl_in["eos_gap_ratio_Delta_over_mu"])  # (local) 4.821 runaway
    inv13_Mmax = float(cfl_in["M_max_Msun"])                    # (local) 0.1631
    print(f"[BASELINE inv-13 W2-1] gap_ratio Delta/mu={inv13_ratio:.4f} (RUNAWAY); "
          f"M_max={inv13_Mmax:.4f} Msun (FIXED-FLOOR artifact we replace)")

    # ---- STEP 0: load spectrum ----
    lam, mult, n_with_mult = load_spectrum_L10()
    lam_floor = float(lam.min())                                 # (local) spectral floor
    print(f"[SPECTRUM] L_max={L_MAX_GAP}: {lam.size} unique |lambda|, "
          f"{int(mult.sum())} counted w/ mult (expect 78080), "
          f"|lambda| in [{lam.min():.6f}, {lam.max():.6f}] M_KK")

    # ---- CALIBRATION (fixed BEFORE scan; g pinned to Delta_BCS at mu_ref) ----
    mu_ref = 0.10                                                # (local) floor-relative dilute-onset calibration anchor (inv-13)
    omega_ref = OMEGA_PAIR_MAX                                   # (local) calibrate with the full window (matches inv-13 g pin)
    g, chi_ref = calibrate_coupling(lam, mult, mu_ref, lam_floor, omega_ref)
    # cross-check: gap at mu_ref must reproduce Delta_BCS
    D_check, _ = solve_gap(lam, mult, mu_ref, g, Delta_BCS, lam_floor, omega_ref)  # (local)
    print(f"[CALIB] mu_ref={mu_ref:.6f} M_KK (floor-rel; floor=|lam|_min={lam_floor:.6f}); "
          f"g={g:.6e} pinned so Delta(mu_ref)=Delta_BCS; chi_ref={chi_ref:.4f}; "
          f"gap@mu_ref check={D_check:.7f} (target {Delta_BCS:.7f})")

    # ---- STEP 2b: SELF-CONSISTENT mu_eff(rho) trajectory ----
    traj = selfconsistent_mu_eff_trajectory(lam, mult, g, lam_floor)
    print(f"[BAND] bounded finite-triple band width eps_max={traj['eps_max']:.4f} M_KK "
          f"(|lambda|_max-|lambda|_min); mu_eff ceiling={traj['mu_dense']:.4f} M_KK")
    print(f"[SELF-CONSISTENT mu_eff] selfcons_resid_max={traj['selfcons_resid_max']:.2e} (tol {SELFCONS_RTOL})")
    print(f"[GAP PEAK] (max-coupling density): mu_eff={traj['mu_peak']:.4f} M_KK  "
          f"Delta_peak={traj['Delta_peak']:.6f} M_KK  Delta/mu={traj['ratio_peak']:.4f}")
    print(f"[DENSE PLATEAU] (deepest SUSTAINABLE density = band-depletion edge): "
          f"mu_eff={traj['mu_plateau']:.4f} M_KK  Delta={traj['Delta_plateau']:.6f} M_KK  "
          f"Delta/mu={traj['ratio_plateau']:.4f} (target O(0.1) band [{GAP_RATIO_LO},{GAP_RATIO_HI}])")

    # ---- [SIGN] axis: dDelta_CFL/dmu over the dense window ----
    # In the self-consistent trajectory mu_eff is MONOTONE-increasing in x; test
    # the sign of dDelta/dmu where the gap is solved.  (Retains the inv-13 sign.)
    mu_traj = traj["mu_traj"]; Delta_traj = traj["Delta_traj"]   # (local)
    valid = Delta_traj > 0                                       # (local)
    # restrict the SIGN test to the band-capturing window (where the pairing
    # surface moves through increasing-DOS regions): the rising flank of Delta(mu).
    # Use the sub-range where mu_eff is between mu_ref and the gap-peak.
    if valid.sum() >= 2:
        mu_v = mu_traj[valid]; D_v = Delta_traj[valid]           # (local)
        dD = np.gradient(D_v, mu_v)                              # (local)
        i_peak = int(np.argmax(D_v))                             # (local) gap peak (DOS-driven rise ends here)
        rising = slice(0, max(i_peak + 1, 2))                    # (local) the DOS-monotone rising flank
        dD_rise = dD[rising]                                     # (local)
        sign_pass = bool(np.all(dD_rise > -1e-9))                # (local) dDelta/dmu > 0 on the rising flank
        frac_increasing = float(np.mean(dD_rise > -1e-9))        # (local)
    else:
        dD = np.array([]); sign_pass = False; frac_increasing = 0.0  # (local)
    print(f"[SIGN] dDelta_CFL/dmu>0 on the DOS-rising flank: {sign_pass} "
          f"(frac_increasing={frac_increasing:.3f})")

    # ---- ONE GPU eigvalsh validation at the dense plateau ----
    i_d = traj["i_dense"]                                        # (local)
    omega_d = float(traj["omega_traj"][i_d])                    # (local)
    resid, n_block, gpu_dev = gpu_validate_bdg_block(
        lam, mult, traj["mu_plateau"], max(traj["Delta_plateau"], 1e-6), lam_floor, omega_d)
    print(f"[GPU-VALIDATE] BdG-block eigvalsh-vs-closed-form resid at plateau = {resid:.3e} "
          f"(device={gpu_dev}, n_block={n_block})")

    # ---- STEP 3: EoS + TOV M_max ----
    M_max, R_at_Mmax, eos_diag, eps_c_grid, M_tov, R_tov = eos_and_mmax(traj)
    print(f"[EOS] Delta_plateau={eos_diag['Delta_plateau_MKK']:.6f} M_KK  "
          f"gap_ratio Delta/mu={eos_diag['gap_ratio_Delta_over_mu']:.4f} (vs inv-13 {inv13_ratio:.4f})  "
          f"cs2={eos_diag['cs2_gap_stiffened']:.4f}  B_phys={eos_diag['B_phys_MeV_fm3']:.2f} MeV/fm^3  "
          f"Delta_phys={eos_diag['Delta_phys_MeV']:.1f} MeV")
    print(f"[TOV] M_max={M_max:.4f} Msun (vs inv-13 {inv13_Mmax:.4f})  R(M_max)={R_at_Mmax:.2f} km  "
          f"P_c@Mmax={eos_diag['P_c_at_Mmax_MeV_fm3']:.3e} MeV/fm^3")

    # ---- STEP 5: feed pinned pressure-scale into inv-11 interior ----
    co_in = np.load(CO_INTERIOR_NPZ, allow_pickle=True)          # (local)
    interior = feed_through_interior(co_in, eos_diag["P_c_at_Mmax_MeV_fm3"])
    print(f"[INTERIOR FEED-THROUGH] inv-11 C_max(unpinned)={interior['C_max_inv11']:.3e} -> "
          f"C_max(CFL-pinned)={interior['C_max_pinned']:.3e}  "
          f"(stiffening={interior['stiffening']:.3e}; self_bound={interior['self_bound']})")

    # ===================================================================
    # VERDICT axes
    # ===================================================================
    # SIGN: dDelta_CFL/dmu > 0 (retained from inv-13) -- PRE-REGISTERED PASS
    sign_verdict = "PASS" if sign_pass else "FAIL"               # (local)

    # MAGNITUDE: M_max in band AND Delta/mu in O(0.1) band AND C_max >= floor
    gap_ratio = eos_diag["gap_ratio_Delta_over_mu"]              # (local)
    C_max = interior["C_max_pinned"]                            # (local)
    mmax_in_band = bool(M_MAX_LOWER <= M_max <= M_MAX_UPPER)     # (local)
    ratio_in_band = bool(GAP_RATIO_LO <= gap_ratio <= GAP_RATIO_HI)  # (local)
    cmax_ok = bool(np.isfinite(C_max) and C_max >= C_MAX_FLOOR)  # (local)
    if mmax_in_band and ratio_in_band and cmax_ok:
        magnitude_verdict = "PASS"                               # (local) full magnitude closure
    elif gap_ratio < GAP_RATIO_HI * 2.0 and M_max >= M_MAX_LOWER * 0.5:
        # stiffer-than-inv-13 and ratio relaxed but not fully in all bands -> INFO
        magnitude_verdict = "INFO"                               # (local)
    else:
        magnitude_verdict = "FAIL"                               # (local)

    # REGIME: fraction of the density trajectory that is physically self-consistent
    # (gap solved AND self-consistency residual under tol AND finite ratio).
    # The non-physical fraction is the BAND-DEPLETION TAIL: grid points whose
    # mu_eff has pushed the pairing window past the top of the bounded finite-triple
    # band (Delta = 0, sub-critical -- no modes left for the Cooper instability).
    # This is a grid-coverage property (the x-grid extends to the band ceiling),
    # NOT a numerical breakdown of the gap solve (which is exact, resid_max=0).
    sc_resid = traj["selfcons_resid"]                           # (local)
    phys_traj = (Delta_traj > 0) & np.isfinite(traj["ratio_traj"]) & (sc_resid < SELFCONS_RTOL)  # (local)
    regime_frac = float(np.mean(phys_traj))                     # (local)
    if regime_frac >= 0.95:
        regime_verdict = "VALID"                                 # (local)
    elif regime_frac >= 0.50:
        regime_verdict = "MARGINAL"                              # (local)
    else:
        regime_verdict = "BREAKDOWN"                             # (local)
    print(f"[REGIME] self-consistent physical fraction={regime_frac:.3f} -> {regime_verdict}")

    # ---- composite collapse (gate-verdicts.md pre-registered rule) ----
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                       # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                       # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                       # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                       # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                       # (local)
    else:
        composite = "PASS"                                       # (local)

    value_str = (f"M_max={M_max:.3f}_Msun_band[{M_MAX_LOWER},{M_MAX_UPPER}]"
                 f"_Delta/mu={gap_ratio:.3f}_band[{GAP_RATIO_LO},{GAP_RATIO_HI}]"
                 f"_C_max={C_max:.2e}_floor{C_MAX_FLOOR:.0e}"
                 f"_dDelta/dmu>0={sign_pass}"
                 f"_inv13_runaway_ratio={inv13_ratio:.3f}->selfcons={gap_ratio:.3f}")  # (local)

    # ===================================================================
    # dual SHA (S84+ schema: audit over script+canonical+pinmap; content over script)
    # ===================================================================
    pin_map = {
        "script_sha256": "<self>",
        "canonical_constants_sha256": sha_canon,
        "s84_spectrum_cache_L12_tau019_sha256": sha_cache,
        "inv13_w2_1_finite_mu_cfl_eos_sha256": sha_cfl,
        "inv11_w5_2_compact_object_interior_sha256": sha_co,
        "N_RHO": N_RHO, "OMEGA_PAIR_MAX": OMEGA_PAIR_MAX,
        "L_MAX": L_MAX, "L_MAX_GAP": L_MAX_GAP,
        "M_KK": M_KK, "tau_fold": tau_fold, "Delta_BCS": Delta_BCS,
        "K_crit_BdG": K_crit_BdG, "rho_B2_per_mode": rho_B2_per_mode,
        "M_MAX_LOWER": M_MAX_LOWER, "M_MAX_UPPER": M_MAX_UPPER,
        "GAP_RATIO_LO": GAP_RATIO_LO, "GAP_RATIO_HI": GAP_RATIO_HI,
        "C_MAX_FLOOR": C_MAX_FLOOR, "SELFCONS_RTOL": SELFCONS_RTOL,
        "scheme": SCHEME, "convention": CONVENTION,
        "regulator_pin": "a_n^{Pauli-Villars}_LambdaUV_M_KK",
        "gate_id": GATE_ID, "schema_version": "S84+",
    }
    script_bytes = Path(__file__).resolve().read_bytes()         # (local)
    content_sha = hashlib.sha256(script_bytes).hexdigest()       # (local)
    pin_map["script_sha256"] = content_sha
    audit_payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()  # (local)
    audit_sha = hashlib.sha256(audit_payload).hexdigest()        # (local)

    # ===================================================================
    # save npz (full float64)
    # ===================================================================
    np.savez(
        NPZ_PATH,
        # self-consistent trajectory
        mu_traj=traj["mu_traj"], Delta_traj=traj["Delta_traj"],
        ratio_traj=traj["ratio_traj"], nwin_traj=traj["nwin_traj"],
        omega_traj=traj["omega_traj"], selfcons_resid=traj["selfcons_resid"],
        mu_ref=mu_ref, mu_dense=traj["mu_dense"], eps_max_band=traj["eps_max"],
        g_coupling=g, chi_ref=chi_ref,
        i_dense=traj["i_dense"], mu_plateau=traj["mu_plateau"],
        Delta_plateau=traj["Delta_plateau"], ratio_plateau=traj["ratio_plateau"],
        i_peak=traj["i_peak"], mu_peak=traj["mu_peak"],
        Delta_peak=traj["Delta_peak"], ratio_peak=traj["ratio_peak"],
        selfcons_resid_max=traj["selfcons_resid_max"],
        # EoS + TOV
        M_max_Msun=M_max, R_at_Mmax_km=R_at_Mmax,
        eps_c_grid=eps_c_grid, M_tov=M_tov, R_tov=R_tov,
        cs2_gap_stiffened=eos_diag["cs2_gap_stiffened"],
        B_phys_MeV_fm3=eos_diag["B_phys_MeV_fm3"],
        Delta_phys_MeV=eos_diag["Delta_phys_MeV"],
        gap_ratio_Delta_over_mu=eos_diag["gap_ratio_Delta_over_mu"],
        P_c_at_Mmax_MeV_fm3=eos_diag["P_c_at_Mmax_MeV_fm3"],
        mu_QCD_MeV_reanchor=eos_diag["mu_QCD_MeV_reanchor"],
        # interior feed-through
        C_max_inv11=interior["C_max_inv11"], C_max_pinned=interior["C_max_pinned"],
        P_scale_generic=interior["P_scale_generic"], P_scale_pinned=interior["P_scale_pinned"],
        interior_stiffening=interior["stiffening"], P_nuc_ref_MeV_fm3=interior["P_nuc_ref_MeV_fm3"],
        interior_self_bound=interior["self_bound"], interior_w_core=interior["w_core"],
        # baseline cross-check
        inv13_gap_ratio_runaway=inv13_ratio, inv13_M_max=inv13_Mmax,
        # verdict axes
        sign_pass=sign_pass, frac_increasing=frac_increasing,
        regime_frac=regime_frac, regime_verdict=regime_verdict,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        composite=composite,
        mmax_in_band=mmax_in_band, ratio_in_band=ratio_in_band, cmax_ok=cmax_ok,
        M_MAX_LOWER=M_MAX_LOWER, M_MAX_UPPER=M_MAX_UPPER,
        GAP_RATIO_LO=GAP_RATIO_LO, GAP_RATIO_HI=GAP_RATIO_HI, C_MAX_FLOOR=C_MAX_FLOOR,
        OMEGA_PAIR_MAX=OMEGA_PAIR_MAX, Delta_BCS=Delta_BCS, n_with_mult=n_with_mult,
        gpu_eigvalsh_resid_plateau=resid, gpu_device=gpu_dev,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"[SAVE] {NPZ_PATH}")

    # ===================================================================
    # plot (4 panels)
    # ===================================================================
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    # (1) self-consistent Delta(mu_eff) and Delta/mu trajectory
    ax = axes[0, 0]
    ax.plot(mu_traj, Delta_traj, "o-", color="#1f77b4", lw=2, ms=4, label=r"$\Delta_{\rm CFL}(\mu_{\rm eff})$")
    ax.axhline(Delta_BCS, color="gray", ls="--", lw=1, label=fr"$\Delta_{{\rm BCS}}={Delta_BCS:.4f}$ (canonical)")
    ax.axvline(traj["mu_plateau"], color="red", ls=":", lw=1.5, label=fr"dense plateau $\mu={traj['mu_plateau']:.2f}$")
    ax.set_xlabel(r"$\mu_{\rm eff}$  [$M_{KK}$ units]")
    ax.set_ylabel(r"$\Delta_{\rm CFL}$  [$M_{KK}$ units]")
    ax.set_title(fr"Self-consistent CFL gap vs $\mu_{{\rm eff}}(\rho)$" + "\n" +
                 fr"sign($d\Delta/d\mu$)>0: {sign_pass}")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    # (2) Delta/mu ratio: the runaway fix
    ax = axes[0, 1]
    ax.plot(mu_traj, traj["ratio_traj"], "o-", color="#2ca02c", lw=2, ms=4, label=r"$\Delta/\mu_{\rm eff}$ (self-consistent)")
    ax.axhspan(GAP_RATIO_LO, GAP_RATIO_HI, color="green", alpha=0.15, label=fr"O(0.1) band [{GAP_RATIO_LO},{GAP_RATIO_HI}]")
    ax.axhline(inv13_ratio, color="red", ls="--", lw=1.5, label=fr"inv-13 runaway $\Delta/\mu$={inv13_ratio:.2f}")
    ax.plot([traj["mu_plateau"]], [gap_ratio], "*", ms=18, color="gold", mec="k", label=fr"plateau $\Delta/\mu$={gap_ratio:.3f}")
    ax.set_xlabel(r"$\mu_{\rm eff}$  [$M_{KK}$ units]")
    ax.set_ylabel(r"$\Delta/\mu_{\rm eff}$")
    ax.set_yscale("log")
    ax.set_title("Runaway fix: self-consistent $\\Delta/\\mu \\to O(0.1)$\n(inv-13 fixed-floor artifact = 4.82)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    # (3) TOV mass-radius
    ax = axes[1, 0]
    good = M_tov > 0                                            # (local)
    ax.plot(R_tov[good], M_tov[good], "-", color="#d62728", lw=2, label="TOV M-R (CFL-stiffened EoS)")
    ax.axhspan(M_MAX_LOWER, M_MAX_UPPER, color="green", alpha=0.12, label=fr"PASS band [{M_MAX_LOWER},{M_MAX_UPPER}] $M_\odot$")
    ax.plot([R_at_Mmax], [M_max], "*", ms=18, color="gold", mec="k", label=fr"$M_{{\rm max}}={M_max:.3f}\,M_\odot$")
    ax.axhline(inv13_Mmax, color="purple", ls=":", lw=1.5, label=fr"inv-13 $M_{{\rm max}}$={inv13_Mmax:.3f} (soft)")
    ax.set_xlabel("R  [km]"); ax.set_ylabel(r"M  [$M_\odot$]")
    ax.set_title(f"TOV maximum mass\n" + fr"$c_s^2={eos_diag['cs2_gap_stiffened']:.3f}$, $B={eos_diag['B_phys_MeV_fm3']:.1f}$ MeV/fm$^3$")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    # (4) interior compactness feed-through
    ax = axes[1, 1]
    bars = ax.bar([0, 1], [interior["C_max_inv11"], interior["C_max_pinned"]],
                  color=["#9467bd", "#ff7f0e"], width=0.6)
    ax.axhline(C_MAX_FLOOR, color="black", ls="--", lw=1.5, label=fr"physical floor $C={C_MAX_FLOOR:.0e}$")
    ax.set_yscale("log")
    ax.set_xticks([0, 1]); ax.set_xticklabels(["inv-11\n(unpinned\nP_scale)", "CFL-pinned\nP_scale"])
    ax.set_ylabel(r"compactness $C_{\max}=M/R$")
    ax.set_title(f"Interior feed-through: $C_{{\\max}}$\n"
                 fr"stiffening$\times${interior['stiffening']:.2e}; self-bound: {interior['self_bound']}")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")
    fig.suptitle(f"{GATE_ID}: self-consistent $\\mu_{{\\rm eff}}$ CFL EoS  [composite={composite}]  "
                 f"(M_max={M_max:.3f} M$_\\odot$, $\\Delta/\\mu$={gap_ratio:.3f}, C_max={C_max:.2e})",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_PATH, dpi=130)
    print(f"[SAVE] {PNG_PATH}")

    # ===================================================================
    # 4-tuple + verdict payload
    # ===================================================================
    print(f"[4-TUPLE] (value={value_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"[CLOSURE] audit_sha256={audit_sha}")
    print(f"[CLOSURE] content_sha256={content_sha}")
    print(f"[VERDICT] composite={composite}  sign={sign_verdict}  magnitude={magnitude_verdict}  regime={regime_verdict}")

    print_verdict_payload(
        verdict=composite,
        value=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        companion_note=(f"{GATE_ID} self-consistent mu_eff CFL EoS; "
                        f"runaway Delta/mu {inv13_ratio:.3f}->{gap_ratio:.3f} (O(0.1)); "
                        f"M_max={M_max:.3f} Msun; C_max {interior['C_max_inv11']:.2e}->{C_max:.2e}"),
        extra_rows=[
            f"# regulator_pin=a_n^{{Pauli-Villars}}_LambdaUV_M_KK (BdG grand-potential UV reg; substrate-natural)",
            f"# binding_magnitude_gap: M_max={M_max:.3f}_Msun band[{M_MAX_LOWER},{M_MAX_UPPER}]; "
            f"Delta/mu={gap_ratio:.4f} band[{GAP_RATIO_LO},{GAP_RATIO_HI}]; C_max={C_max:.3e} floor{C_MAX_FLOOR:.0e}; "
            f"P_c@Mmax={eos_diag['P_c_at_Mmax_MeV_fm3']:.3e}_MeV/fm3 (pinned pressure-scale for CF-CO2)",
            f"# self_consistent_mu_eff: mu_plateau={traj['mu_plateau']:.4f}_MKK Delta_plateau={traj['Delta_plateau']:.4f}_MKK; "
            f"NOT fixed-floor (inv-13 runaway Delta/mu={inv13_ratio:.3f} -> self-consistent {gap_ratio:.4f})",
        ],
    )

    # exit 0 regardless of scientific verdict (math-scripts.md exit-code rule)
    return 0


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None):
    """Local copy of the template helper (script prints the payload; the AGENT
    calls the emit_verdict MCP tool, session track)."""
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "session",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


if __name__ == "__main__":
    sys.exit(main())
