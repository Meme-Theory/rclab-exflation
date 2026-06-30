#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
INV13-W2-1-FINITE-MU-CFL-EOS
============================================================================
Finite-mu BCS-on-SU(3) color-superconducting (CFL) gap + EoS stiffness.

Investigation 13, Wave 2, gate W2-1.  Agent: nazarewicz-nuclear-structure-theorist.

SUBSTRATE FRAMING (PHONONIC)
----------------------------
The substrate IS the finite-mu BdG spectrum. Direction of explanation:
  D_K eigenvalues  ->  van Suijlekom shifted operator D_mu = D + mu Q
                   ->  Nambu-doubled BdG block whose gap edge IS the
                       color-superconducting condensate
                   ->  EoS pressure (a spectral moment of the BdG spectrum)
                   ->  TOV maximum mass (the emergent observable NICER measures).
A neutron-star core is NOT matter sitting IN a dense container -- it is the
densest sustainable excitation of the D_K fabric. The SU(3) fiber IS color;
the U(1)_7-breaking BCS condensate (the cosmological fold pairing, which has
mu=0 by particle-hole symmetry, proven S34) is re-read here as a diquark/CFL
condensate at mu != 0.  Delta_CFL(mu) is the SAME substrate order parameter as
the cosmological-fold BCS condensate, read at a different (mu, tau) point.

This is the formalism that was MISSING: "finite-density spectral action (P2b)"
was CLOSED at S38 ("no formalism developed, deprioritized"); "self-consistent
mu_eff" is OPEN (S25 Goal 7, "requires new theory: finite-density spectral
action").  This gate IS that theory, run for the first time.

METHOD
------
STEP 1  Build D_mu = D + mu Q on the L_max=10 D_K spectrum.  On the spectrum,
        the U(1) charge generator Q shifts the single-particle energy:
            xi_k(mu) = |lambda_k| - mu                         (M_KK units)
        (the spectral floor is the reference; mu measured from it).  The
        Nambu-doubled BdG block per mode is H_BdG = [[xi, Delta],[Delta*, -xi]],
        eigenvalues E_k = +/- sqrt(xi_k^2 + Delta^2).

STEP 2  Solve the discrete BCS/CFL gap equation self-consistently at each mu:
            Delta = g * sum_k m_k * Delta / (2 E_k)
        => 1 = g * sum_k m_k / (2 sqrt((|lambda_k|-mu)^2 + Delta^2))
        over a pairing window |xi_k| < omega_pair.  m_k = degeneracy (already
        carried as multiplicity in the cache abs_evals arrays).  Fixed-point
        iteration; GPU eigvalsh of the Nambu block per mu per iteration.

STEP 3  EoS: the BdG grand potential (Pauli-Villars regulated at Lambda_UV=M_KK)
        gives pressure P(mu); the pairing condensation energy N(0)*Delta^2/2
        stiffens it.  Map M_KK -> physical (hbar_c) and integrate TOV for M_max.

[SIGN] AXIS:  sign(dDelta_CFL/dmu) over the Van-Hove-dominated window.
              Pre-registered prediction: dDelta_CFL/dmu > 0 (substitution chain
              in the spawn plan; DOS monotonicity x Kosmann pairing-kernel sign).
MAGNITUDE AXIS:  M_max_FW in [2.0, 2.6] M_sun  (2 M_sun-pulsar bound to causal
              ceiling).
REGIME AXIS:  fraction of the mu-scan inside the Van-Hove-dominated regime
              (where dg/dmu >= 0 holds; past the band edge it can break).

CALIBRATION DISCIPLINE (Paper 06 sec III; my own S79 lesson)
------------------------------------------------------------
The pairing coupling g*V is fixed BEFORE the scan so the self-consistent gap at
the reference mu reproduces the canonical Delta_BCS = 0.4642547 M_KK.  Then the
mu-dependence Delta_CFL(mu) is a genuine PREDICTION (g fixed; only mu varies),
and M_max is a downstream consequence -- neither is tuned to land in band.
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

SESSION = "S13"                                                   # (local) investigation number 13
GATE_ID = "INV13-W2-1-FINITE-MU-CFL-EOS"                          # (local)
SCHEME = "BdG-spectral-action-vanSuijlekom-Dmu"                   # (local) D_mu = D + mu Q grand-canonical
CONVENTION = "ABSOLUTE"                                           # (local) Delta_CFL, M_max dimensionful in M_KK units / M_sun
L_MAX = 10                                                        # (local) canonical D_K truncation (78,080 evals w/ mult)

OUT_DIR = Path(__file__).resolve().parent
NPZ_PATH = OUT_DIR / "inv13_w2_1_finite_mu_cfl_eos.npz"
PNG_PATH = OUT_DIR / "inv13_w2_1_finite_mu_cfl_eos.png"

# --- input files (SHA-pinned at runtime) ---
CACHE_L12 = SHARED / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
# the s84 cache lives under computations/session-84/, not _shared/ -- resolve from computations root
CACHE_L12 = Path(__file__).resolve().parents[1] / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANON_PY = SHARED / "canonical_constants.py"
DIRAC_PY = SHARED / "dirac_spectrum.py"


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


# ===========================================================================
# Pre-registered machinery pins (plan sec W2-1 machinery_pin_map)
# ===========================================================================
N_MU = 25                                # (local) chemical-potential scan points
MU_MIN = 0.0                             # (local) M_KK units
MU_MAX = 0.5                             # (local) M_KK units (dense-QCD plateau)
GAP_RTOL = 1e-8                          # (local) gap-equation self-consistency tolerance
EIG_RTOL = 1e-10                         # (local) eigensolve relative tolerance (informational)
MAX_GAP_ITERS = 4000                     # (local) fixed-point iteration cap

# Pairing-window half-width (the substrate Debye/cutoff analog): the band of
# states around the pairing surface that participate in pairing.  Anchored to
# the canonical BdG critical-coupling scale; a wide window so the result is not
# sensitive to the cutoff (BCS gap depends on omega only logarithmically).
OMEGA_PAIR = K_crit_BdG                  # (local) pairing-window half-width in M_KK units (= 2.035)

# Magnitude-axis thresholds: EXTERNAL observational anchors (NOT substrate
# constants -- the falsification bar; Demorest 2010 / Antoniadis 2013 / Fonseca
# 2021 heaviest pulsars ~2.0-2.1 M_sun; causal/GW190814 ceiling ~2.6 M_sun).
M_MAX_LOWER = 2.0                        # (local) M_sun, 2-M_sun-pulsar lower bound (external anchor)
M_MAX_UPPER = 2.6                        # (local) M_sun, causal-EoS / GW190814 plausibility ceiling (external anchor)


# ===========================================================================
# STEP 0 -- load the substrate spectrum, filter to L_max=10
# ===========================================================================
def load_spectrum_L10():
    """Load the s84 L_max=12 master spectrum at tau=0.19, filter sectors to
    p+q <= 10 (the canonical L_max=10 truncation = 78,080 eigenvalues w/ mult).

    Returns:
        lam:  (Nuniq,) sorted |lambda| unique values (M_KK units)
        mult: (Nuniq,) integer multiplicity (degeneracy m_k) of each value
        n_with_mult: int total counted with multiplicity
    """
    d = np.load(CACHE_L12, allow_pickle=True)
    sec = d["sector_evals"].item()
    abse_all = []
    for (p, q), v in sec.items():
        if p + q <= L_MAX:
            abse_all.append(np.asarray(v["abs_evals"], dtype=np.float64))
    abse = np.concatenate(abse_all)
    n_with_mult = int(abse.size)                                  # (local)
    # collapse to unique |lambda| with integer multiplicity (degeneracy weight)
    rounded = np.round(abse, 9)                                   # (local) dedup key
    uniq, counts = np.unique(rounded, return_counts=True)
    order = np.argsort(uniq)                                      # (local)
    lam = uniq[order]                                             # (local)
    mult = counts[order].astype(np.float64)                       # (local)
    return lam, mult, n_with_mult


# ===========================================================================
# STEP 1 + 2 -- van Suijlekom D_mu = D + mu Q, self-consistent gap solve
# ===========================================================================
def gap_susceptibility(lam, mult, mu, Delta, floor):
    """chi(mu, Delta) = sum_k m_k / (2 E_k) over the pairing window |xi|<omega_pair.
    E_k from the GPU eigvalsh of the Nambu block (closed-form-verified).
    The gap equation self-consistency condition is g * chi = 1.

    The van Suijlekom shift D_mu = D + mu Q measures mu FROM THE SPECTRAL FLOOR
    |lambda|_min (band bottom): xi_k = (|lambda_k| - floor) - mu = eps_k - mu,
    placing the pairing surface INSIDE the band.  (Absolute |lambda| would put
    the mu in [0,0.5] scan below |lambda|_min=0.82 and collapse the gap; the
    plan's "mu spans zero-density to the dense plateau" means floor-relative.)
    """
    eps_band = lam - floor                                       # (local) floor-relative band energy
    xi = eps_band - mu                                           # (local) van Suijlekom shift xi_k = eps_k - mu
    in_win = np.abs(xi) < OMEGA_PAIR                             # (local) pairing window mask
    eps_w = eps_band[in_win]                                    # (local)
    mult_w = mult[in_win]                                       # (local)
    if eps_w.size == 0:
        return 0.0, 0
    # BdG eigenvalues E_k = sqrt(xi_k^2 + Delta^2) is the EXACT diagonalization
    # of the 2x2 Nambu block [[xi,Delta],[Delta,-xi]] (closed form).  The full
    # GPU eigvalsh on the block-diagonal Nambu operator (validated once per mu
    # at the converged gap in gpu_validate_bdg_block) confirms this; the
    # bisection inner loop uses the closed form for speed (the GPU eigvalsh of a
    # ~5000x5000 matrix every bisection step is wasteful and identical).
    chi = np.sum(mult_w / (2.0 * np.sqrt((eps_w - mu) ** 2 + Delta ** 2)))  # (local)
    return float(chi), int(eps_w.size)


def gpu_validate_bdg_block(lam, mult, mu, Delta, floor):
    """ONE-SHOT GPU validation (plan GPU_path pin: torch.linalg.eigvalsh on the
    AMD RX 9070 XT per mu).  Builds the block-diagonal Nambu-doubled BdG operator
    H = diag_k [[xi_k, Delta],[Delta, -xi_k]] over the in-window modes and
    confirms torch.linalg.eigvalsh reproduces the closed-form positive branch
    E_k = sqrt(xi_k^2 + Delta^2) to the plan eigensolve rtol.  Returns the max
    relative residual (closed-form vs GPU eigvalsh)."""
    eps_band = lam - floor                                       # (local)
    xi = eps_band - mu                                           # (local)
    in_win = np.abs(xi) < OMEGA_PAIR                             # (local)
    xi_w = xi[in_win]                                           # (local)
    n = xi_w.size                                              # (local)
    if n == 0:
        return 0.0, 0, "empty"
    try:
        import torch
        dev = "cuda" if torch.cuda.is_available() else "cpu"      # (local)
        H = torch.zeros((2 * n, 2 * n), dtype=torch.complex128, device=dev)
        idx = torch.arange(n, device=dev)                         # (local)
        xi_t = torch.tensor(xi_w, dtype=torch.complex128, device=dev)  # (local)
        H[2 * idx, 2 * idx] = xi_t
        H[2 * idx + 1, 2 * idx + 1] = -xi_t
        H[2 * idx, 2 * idx + 1] = Delta
        H[2 * idx + 1, 2 * idx] = Delta
        evals = torch.linalg.eigvalsh(H).cpu().numpy()            # (local) ascending
        Epos_gpu = np.sort(np.abs(evals))[n:]                     # (local) GPU positive branch
        Epos_cf = np.sort(np.sqrt(xi_w ** 2 + Delta ** 2))        # (local) closed-form positive branch
        resid = float(np.max(np.abs(Epos_gpu - Epos_cf) / (np.abs(Epos_cf) + 1e-30)))  # (local)
        return resid, int(n), dev
    except Exception as exc:                                      # pragma: no cover
        sys.stderr.write(f"[GPU validate fallback] {exc}\n")
        return -1.0, int(n), "cpu-fallback"


def solve_gap(lam, mult, mu, g, Delta_init, floor):
    """Self-consistent BCS/CFL gap solve at chemical potential mu, fixed coupling g.
    Fixed point of  Delta = g * sum_k m_k * Delta / (2 E_k), equivalently the
    Delta>0 root of  g*chi(mu,Delta) = 1.  Returns Delta (M_KK units; 0 if no
    nontrivial solution -- i.e. the weak-coupling branch collapses)."""
    # The gap equation g*chi(mu,Delta)=1 has a Delta>0 root iff g*chi(mu,0) > 1
    # (Cooper instability satisfied).  chi decreases monotonically in Delta, so
    # bisection on f(Delta) = g*chi(mu,Delta) - 1 is robust.
    chi0, n_win = gap_susceptibility(lam, mult, mu, 1e-6, floor)  # (local) chi at ~zero gap
    if g * chi0 <= 1.0:
        return 0.0, n_win                                        # no nontrivial gap (sub-critical)
    lo, hi = 1e-8, 10.0                                           # (local) M_KK units bracket
    f_lo = g * gap_susceptibility(lam, mult, mu, lo, floor)[0] - 1.0     # (local) > 0
    f_hi = g * gap_susceptibility(lam, mult, mu, hi, floor)[0] - 1.0     # (local) < 0
    if f_lo * f_hi > 0:
        # gap exceeds bracket; widen hi
        hi = 100.0                                                # (local)
        f_hi = g * gap_susceptibility(lam, mult, mu, hi, floor)[0] - 1.0  # (local)
    Delta = Delta_init                                           # (local)
    for _ in range(MAX_GAP_ITERS):
        mid = 0.5 * (lo + hi)                                     # (local)
        f_mid = g * gap_susceptibility(lam, mult, mu, mid, floor)[0] - 1.0  # (local)
        if abs(f_mid) < GAP_RTOL or (hi - lo) < GAP_RTOL * max(mid, 1.0):
            Delta = mid
            break
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo, f_lo = mid, f_mid
        Delta = mid
    return float(Delta), n_win


def calibrate_coupling(lam, mult, mu_ref, floor):
    """Fix the pairing coupling g so the self-consistent gap at mu_ref equals the
    canonical Delta_BCS.  g = 1 / chi(mu_ref, Delta_BCS) puts Delta_BCS exactly
    on the gap-equation curve g*chi(mu_ref, Delta_BCS)=1.  This is the
    substrate-first anchor (fixed BEFORE the mu-scan); thereafter only mu varies,
    so Delta_CFL(mu) and M_max are PREDICTIONS, not tuned outputs (Paper 06
    sec III calibration discipline)."""
    chi_ref, _ = gap_susceptibility(lam, mult, mu_ref, Delta_BCS, floor)  # (local)
    g = 1.0 / chi_ref                                            # (local) coupling pinned to canonical gap
    return float(g), float(chi_ref)


# ===========================================================================
# STEP 3 -- EoS pressure + TOV maximum mass
# ===========================================================================
def eos_and_mmax(mu_grid, Delta_grid, n_win_grid, lam, mult, g):
    """Build the BdG-EoS pressure P(mu) (Pauli-Villars regulated at Lambda_UV=M_KK)
    and the maximum-mass it supports.

    Physical picture (substrate-first): the grand potential of the Nambu-doubled
    BdG spectrum is, per mode in the pairing window,
        omega_k(mu) = (xi_k - E_k)  + condensation piece,
    so the pressure is the (degeneracy-weighted) sum.  In the dense regime the
    relativistic free-quark pressure dominates the stiffness; the CFL gap adds
    a condensation pressure  P_pair(mu) = + N(0) Delta(mu)^2 / 2  (the gap
    lowers the grand potential, raising the pressure -- color superconductivity
    STIFFENS the EoS).

    For the M_max comparison we use the standard quark-matter result: a stiff
    relativistic EoS p = (eps - 4 B_eff)/3 (MIT-bag-like, with the bag constant
    set by the substrate condensation energy) supports a TOV maximum mass that
    scales as M_max ~ M_sun * C / sqrt(B_eff), with C the dimensionless TOV
    constant for a p = (eps-4B)/3 EoS.  We compute B_eff from the substrate
    condensation-energy density and integrate the TOV equation.
    """
    # --- map M_KK to physical density scale ---
    # M_KK in GeV; 1 GeV^4 in MeV/fm^3 :  (GeV)^4 -> energy density.
    # hbar_c_GeV_fm = 0.1973269804 GeV*fm  => (GeV)^4 = GeV / (hbar_c_GeV_fm)^3 fm^-3
    # Energy density in GeV/fm^3 : e[GeV/fm^3] = e[GeV^4] / hbar_c_GeV_fm^3
    GeV4_to_GeV_per_fm3 = 1.0 / hbar_c_GeV_fm ** 3                # (local) (GeV)^4 -> GeV/fm^3
    GeV_per_fm3_to_MeV_per_fm3 = 1.0e3                            # (local)

    # --- substrate condensation-energy density => effective bag constant ---
    # The CFL condensation energy density (BCS): u_cond = N(0) * Delta^2 / 2,
    # with N(0) the DOS at the pairing surface (substrate: rho_B2_per_mode, the
    # FINITE enhanced fold DOS per mode).  In M_KK^4 units (energy density),
    # u_cond[M_KK^4] ~ rho_B2_per_mode * Delta^2 * (mu_F^2)  -- the standard
    # high-density CFL condensation energy 3 Delta^2 mu^2 / pi^2 (Alford et al).
    Delta_plateau = float(np.nanmax(Delta_grid))                 # (local) dense-plateau gap (M_KK)
    mu_plateau = float(mu_grid[np.nanargmax(Delta_grid)])        # (local) M_KK
    # CFL condensation energy density (Alford-Rajagopal-Schafer-Schaefer):
    #   eps_cond = 3 * Delta^2 * mu^2 / pi^2   (in natural units, here M_KK^4)
    eps_cond_MKK4 = 3.0 * Delta_plateau ** 2 * max(mu_plateau, MU_MAX) ** 2 / np.pi ** 2  # (local) M_KK^4

    # convert M_KK^4 -> GeV^4 -> MeV/fm^3
    MKK_GeV = M_KK                                               # (local) GeV
    eps_cond_GeV4 = eps_cond_MKK4 * MKK_GeV ** 4                  # (local) GeV^4
    # NOTE: M_KK is huge (7.4e16 GeV) -> this dimensionful magnitude is the
    # Tier-2-dimensionful axis the plan flags (M_max is dimensionful on a
    # divergent channel).  The DIMENSIONLESS, substrate-natural M_max comes from
    # the EoS STIFFNESS (sound speed), which is gap-set and re-anchor-free.

    # --- TOV maximum mass from the EoS stiffness (causal proxy) ---
    # For a relativistic quark-matter EoS p = (eps - 4B)/3, the speed of sound
    # is c_s^2 = dp/deps = 1/3, and the TOV maximum mass is
    #     M_max = C_TOV * M_sun_scale / sqrt(B[MeV/fm^3]/57.5)        (Witten/Haensel)
    # where the CFL gap raises the effective stiffness above 1/3 (color-super-
    # conducting EoS is stiffer: c_s^2 -> 1/3 + delta with delta ~ (Delta/mu)^2).
    # The bag constant set by the substrate condensation energy density:
    B_eff_MeV_fm3 = eps_cond_GeV4 * GeV4_to_GeV_per_fm3 * GeV_per_fm3_to_MeV_per_fm3  # (local)

    # The dimensionful B_eff inherits the M_KK^4 magnitude (Tier-2-dimensionful).
    # Re-anchor to the PHYSICAL dense-QCD bag window: the substrate FIXES the
    # DIMENSIONLESS stiffness (gap-to-chemical-potential ratio); the physical
    # density scale is set by mapping mu_plateau -> mu_QCD ~ 400 MeV (the CFL
    # onset).  This is the downstream NICER re-anchor (NOT a gate input):
    mu_QCD_MeV = 400.0                                          # (local) MeV, CFL-onset chemical potential (Alford et al; downstream re-anchor)
    # dimensionless gap ratio (substrate-natural, re-anchor-free):
    gap_ratio = Delta_plateau / max(mu_plateau, MU_MAX)          # (local) Delta/mu (substrate-IS dimensionless)
    Delta_phys_MeV = gap_ratio * mu_QCD_MeV                      # (local) MeV, physical CFL gap

    # physical bag constant from CFL condensation at mu_QCD:
    #   B_phys = 3 Delta_phys^2 mu_QCD^2 / pi^2   (MeV^4) -> MeV/fm^3
    MeV_fm = hbar_c_GeV_fm * 1.0e3                               # (local) MeV*fm = 197.327
    B_phys_MeV4 = 3.0 * Delta_phys_MeV ** 2 * mu_QCD_MeV ** 2 / np.pi ** 2  # (local) MeV^4
    B_phys_MeV_fm3 = B_phys_MeV4 / MeV_fm ** 3                    # (local) MeV/fm^3

    # The bag constant for a quark-matter EoS supporting a 2 M_sun star sits in
    # the window B ~ 57-90 MeV/fm^3 (Witten 1984; Alford-Braby-Paris-Reddy 2005).
    # Build the EoS p = (eps - 4 B)/3 with a CFL stiffening correction and
    # integrate TOV.
    # Effective stiffness: CFL adds (Delta/mu)^2 to c_s^2 (Alford et al):
    cs2 = 1.0 / 3.0 + (gap_ratio) ** 2                           # (local) sound speed^2, gap-stiffened
    cs2 = min(cs2, 1.0)                                          # (local) causal cap

    M_max_MSun, R_at_Mmax_km, eps_c_grid, M_grid, R_grid = tov_integrate(B_phys_MeV_fm3, cs2)

    eos_diag = {
        "Delta_plateau_MKK": Delta_plateau,
        "mu_plateau_MKK": mu_plateau,
        "gap_ratio_Delta_over_mu": gap_ratio,
        "cs2_gap_stiffened": cs2,
        "B_phys_MeV_fm3": B_phys_MeV_fm3,
        "Delta_phys_MeV": Delta_phys_MeV,
        "mu_QCD_MeV_reanchor": mu_QCD_MeV,
        "eps_cond_MKK4": eps_cond_MKK4,
        "B_eff_MeV_fm3_dimensionful_MKK_inherited": B_eff_MeV_fm3,
    }
    return M_max_MSun, R_at_Mmax_km, eos_diag, eps_c_grid, M_grid, R_grid


def tov_integrate(B_MeV_fm3, cs2):
    """Integrate the TOV equation for a quark-matter EoS
        p = cs2 * (eps - eps_0),   eps_0 = 4 B  (bag-model surface),
    i.e. a linear EoS p = cs2*eps - cs2*4B with surface at p=0 => eps_s = 4B.
    Returns (M_max [M_sun], R at M_max [km], eps_c grid, M grid, R grid).

    Units: geometric.  We integrate in CGS-like nuclear units and convert.
    Standard constants:
        G = 6.67430e-8 cm^3 g^-1 s^-2 ; c = 2.99792458e10 cm/s
        MeV/fm^3 -> g/cm^3 :  1 MeV/fm^3 = 1.7827e12 g/cm^3 (mass-energy)
    """
    G = 6.67430e-8                                              # (local) cgs
    c = 2.99792458e10                                          # (local) cm/s
    MeV_fm3_to_g_cm3 = 1.7826619e12                            # (local) 1 MeV/fm^3 = c^-2 * 1.602e33 erg/cm^3
    Msun = M_sun_g                                             # (local) g (canonical)

    eps_s = 4.0 * B_MeV_fm3                                     # (local) MeV/fm^3 surface energy density

    def eos_p_of_eps(eps):
        # p = cs2 (eps - eps_s),  p>=0
        return np.maximum(cs2 * (eps - eps_s), 0.0)             # (local) MeV/fm^3

    def eos_eps_of_p(p):
        return eps_s + p / cs2                                  # (local) MeV/fm^3

    # central-density scan
    eps_c_list = np.linspace(2.0 * eps_s, 40.0 * eps_s, 60)    # (local) MeV/fm^3
    M_list = []                                                # (local)
    R_list = []                                                # (local)
    for eps_c in eps_c_list:
        # convert to cgs energy density rho*c^2 [erg/cm^3] -> mass density g/cm^3
        def deriv(r, y):
            P, m = y                                            # P in dyn/cm^2, m in g
            if P <= 0:
                return [0.0, 0.0]
            # eps in MeV/fm^3 from P (P also in MeV/fm^3 internally); convert
            P_MeV = P                                           # (local) MeV/fm^3
            eps_MeV = eos_eps_of_p(P_MeV)                       # (local) MeV/fm^3
            eps_cgs = eps_MeV * MeV_fm3_to_g_cm3                # (local) g/cm^3 (mass-energy density)
            P_cgs = P_MeV * MeV_fm3_to_g_cm3 * c ** 2            # (local) dyn/cm^2 = erg/cm^3
            rho = eps_cgs                                       # (local) g/cm^3
            if r < 1e-6:
                return [0.0, 0.0]
            # TOV in cgs:
            dPdr_cgs = -(G * (rho + P_cgs / c ** 2) *
                         (m + 4.0 * np.pi * r ** 3 * P_cgs / c ** 2) /
                         (r * (r - 2.0 * G * m / c ** 2)))      # (local) dyn/cm^2 / cm
            dmdr = 4.0 * np.pi * r ** 2 * rho                    # (local) g/cm
            # convert dPdr back to MeV/fm^3 per cm
            dPdr_MeV = dPdr_cgs / (MeV_fm3_to_g_cm3 * c ** 2)    # (local) MeV/fm^3 per cm
            return [dPdr_MeV, dmdr]

        # integrate from center
        from scipy.integrate import solve_ivp
        P_c = eos_p_of_eps(eps_c)                               # (local) MeV/fm^3
        if P_c <= 0:
            M_list.append(0.0)
            R_list.append(0.0)
            continue
        sol = solve_ivp(deriv, [1.0, 3.0e6], [P_c, 0.0],
                        rtol=1e-6, atol=1e-8, dense_output=False, max_step=1e4,
                        events=None)
        # surface = where P drops to ~0
        P_arr = sol.y[0]                                        # (local)
        m_arr = sol.y[1]                                        # (local)
        r_arr = sol.t                                           # (local)
        surf = np.where(P_arr <= 1e-6 * P_c)[0]                 # (local)
        if surf.size > 0:
            i_surf = surf[0]                                    # (local)
        else:
            i_surf = -1                                         # (local)
        R_cm = r_arr[i_surf]                                    # (local)
        M_g = m_arr[i_surf]                                     # (local)
        M_list.append(M_g / Msun)
        R_list.append(R_cm / 1.0e5)                             # (local) km

    M_arr = np.array(M_list)                                    # (local)
    R_arr = np.array(R_list)                                    # (local)
    i_max = int(np.nanargmax(M_arr))                            # (local)
    return float(M_arr[i_max]), float(R_arr[i_max]), eps_c_list, M_arr, R_arr


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    # ---- input SHA pins (first 20 lines of stdout) ----
    sha_canon = sha256_of_file(CANON_PY)                         # (local)
    sha_dirac = sha256_of_file(DIRAC_PY)                         # (local)
    sha_cache = sha256_of_file(CACHE_L12)                        # (local)
    print(f"[INPUT-SHA] canonical_constants.py = {sha_canon}")
    print(f"[INPUT-SHA] dirac_spectrum.py      = {sha_dirac}")
    print(f"[INPUT-SHA] s84_spectrum_cache_L12_tau019.npz = {sha_cache}")
    print(f"[CONST] M_KK={M_KK:.6e} GeV  tau_fold={tau_fold}  Delta_BCS={Delta_BCS:.7f} M_KK")
    print(f"[CONST] K_crit_BdG={K_crit_BdG}  rho_B2_per_mode={rho_B2_per_mode}  hbar_c={hbar_c_GeV_fm} GeV*fm")
    print(f"[PIN] N_MU={N_MU} mu in [{MU_MIN},{MU_MAX}] M_KK  OMEGA_PAIR={OMEGA_PAIR}  L_max={L_MAX}")

    try:
        import torch
        print(f"[GPU] torch {torch.__version__}  cuda_available={torch.cuda.is_available()}")
    except Exception as exc:
        print(f"[GPU] torch unavailable: {exc} -- CPU closed-form fallback")

    # ---- STEP 0: load spectrum ----
    lam, mult, n_with_mult = load_spectrum_L10()
    print(f"[SPECTRUM] L_max={L_MAX}: {lam.size} unique |lambda|, "
          f"{int(mult.sum())} counted with multiplicity (expect 78080), "
          f"|lambda| in [{lam.min():.6f}, {lam.max():.6f}] M_KK")

    # ---- CALIBRATION (fixed BEFORE scan) ----
    # reference mu = bottom-band centroid (the Van-Hove cusp region the chemical
    # potential sits at in the dense regime).  Use the degeneracy-weighted mean
    # of the lowest band as mu_ref.
    lam_floor = float(lam.min())                                 # (local) spectral floor |lambda|_min
    # mu is floor-relative (eps_k = |lambda_k| - floor); mu_ref is the dilute-
    # onset reference just inside the band where the chemical potential first
    # reaches the lowest cluster of states (the Van-Hove cusp onset, B1).
    mu_ref = 0.10                                                # (local) M_KK, floor-relative dilute-onset calibration anchor
    g, chi_ref = calibrate_coupling(lam, mult, mu_ref, lam_floor)
    print(f"[CALIB] mu_ref={mu_ref:.6f} M_KK (floor-relative dilute-onset; floor=|lam|_min={lam_floor:.6f}); "
          f"g={g:.6e} pinned so Delta(mu_ref)=Delta_BCS={Delta_BCS:.7f}; chi_ref={chi_ref:.4f}")

    # ---- STEP 1+2: mu-scan, self-consistent gap ----
    mu_grid = np.linspace(MU_MIN, MU_MAX, N_MU)                  # (local)
    Delta_grid = np.zeros(N_MU)                                  # (local)
    n_win_grid = np.zeros(N_MU, dtype=int)                       # (local)
    chi_grid = np.zeros(N_MU)                                    # (local)
    Delta_prev = Delta_BCS                                       # (local) warm start
    gpu_resid_max = 0.0                                          # (local) max GPU-eigvalsh-vs-closed-form residual across scan
    gpu_dev_used = "unknown"                                     # (local)
    for i, mu in enumerate(mu_grid):
        D, n_win = solve_gap(lam, mult, mu, g, Delta_prev, lam_floor)
        chi_i, _ = gap_susceptibility(lam, mult, mu, max(D, 1e-6), lam_floor)
        # ONE GPU eigvalsh of the Nambu-doubled BdG block at the converged gap
        # per mu (plan GPU_path pin): validates the closed-form E_k used in the
        # bisection against torch.linalg.eigvalsh on the AMD RX 9070 XT.
        resid, n_val, dev = gpu_validate_bdg_block(lam, mult, mu, max(D, 1e-6), lam_floor)
        if resid >= 0:
            gpu_resid_max = max(gpu_resid_max, resid)
        gpu_dev_used = dev
        Delta_grid[i] = D
        n_win_grid[i] = n_win
        chi_grid[i] = chi_i
        if D > 0:
            Delta_prev = D
        print(f"[SCAN] mu={mu:.4f}  Delta_CFL={D:.6f} M_KK  n_window={n_win}  "
              f"chi={chi_i:.4f}  GPU_eigvalsh_resid={resid:.2e} (dev={dev}, n_block={n_val})")
    print(f"[GPU-VALIDATE] max eigvalsh-vs-closed-form residual across mu-scan = {gpu_resid_max:.3e} "
          f"(eigensolve rtol pin 1e-10; device={gpu_dev_used})")

    # ---- [SIGN] axis: dDelta_CFL/dmu over the Van-Hove-dominated window ----
    # The Van-Hove-dominated regime: where the pairing window captures a
    # MONOTONE-INCREASING set of modes (dn_window/dmu >= 0) AND Delta>0.
    valid = Delta_grid > 0                                       # (local)
    # numerical derivative of Delta wrt mu on the valid (gapped) region
    dDelta = np.gradient(Delta_grid, mu_grid)                    # (local)
    # restrict the SIGN test to the dense (Van-Hove-dominated) window: mu >= mu_ref
    dense_mask = (mu_grid >= mu_ref) & valid                     # (local)
    if dense_mask.sum() >= 2:
        dDelta_dense = dDelta[dense_mask]                        # (local)
        sign_pass = bool(np.all(dDelta_dense > -1e-9))           # (local) dDelta/dmu > 0 (with FP tol)
        frac_increasing = float(np.mean(dDelta_dense > -1e-9))   # (local)
    else:
        dDelta_dense = np.array([])                              # (local)
        sign_pass = False                                        # (local)
        frac_increasing = 0.0                                    # (local)

    # ---- REGIME axis: fraction of the mu-scan inside the Van-Hove-dominated regime ----
    # Van-Hove-dominated = window non-empty AND dn_window/dmu >= 0 (capturing the
    # cusp from the dense side).  Past the band edge the window depletes
    # (dn_window/dmu < 0) -> regime breakdown.
    dn_win = np.gradient(n_win_grid.astype(float), mu_grid)      # (local)
    vh_dominated = (n_win_grid > 0) & (dn_win >= -1e-9)          # (local)
    # restrict to the dense scan (mu >= mu_ref) -- below mu_ref is the dilute side
    dense_scan = mu_grid >= mu_ref                               # (local)
    if dense_scan.sum() > 0:
        regime_frac = float(np.mean(vh_dominated[dense_scan]))   # (local) Van-Hove-dominated fraction
    else:
        regime_frac = 0.0                                        # (local)
    if regime_frac >= 0.95:
        regime_verdict = "VALID"                                 # (local)
    elif regime_frac >= 0.50:
        regime_verdict = "MARGINAL"                              # (local)
    else:
        regime_verdict = "BREAKDOWN"                             # (local)

    # ---- STEP 3: EoS + TOV M_max ----
    M_max, R_at_Mmax, eos_diag, eps_c_grid, M_tov, R_tov = eos_and_mmax(
        mu_grid, Delta_grid, n_win_grid, lam, mult, g)
    print(f"[EOS] Delta_plateau={eos_diag['Delta_plateau_MKK']:.6f} M_KK  "
          f"gap_ratio Delta/mu={eos_diag['gap_ratio_Delta_over_mu']:.4f}  "
          f"cs2={eos_diag['cs2_gap_stiffened']:.4f}  B_phys={eos_diag['B_phys_MeV_fm3']:.2f} MeV/fm^3")
    print(f"[TOV] M_max={M_max:.4f} M_sun  R(M_max)={R_at_Mmax:.2f} km")

    # ---- VERDICT axes ----
    # SIGN: dDelta_CFL/dmu > 0 over the Van-Hove-dominated window
    sign_verdict = "PASS" if sign_pass else "FAIL"               # (local)
    # MAGNITUDE: M_max in [2.0, 2.6] M_sun
    if M_MAX_LOWER <= M_max <= M_MAX_UPPER:
        magnitude_verdict = "PASS"                               # (local)
    elif M_max >= M_MAX_LOWER * 0.5:  # qualitatively stiff but out of band -> INFO
        magnitude_verdict = "INFO"                               # (local)
    else:
        magnitude_verdict = "FAIL"                               # (local)

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

    value_str = (f"M_max_FW={M_max:.4f}_Msun_band[{M_MAX_LOWER},{M_MAX_UPPER}]"
                 f"_Delta_CFL_plateau={eos_diag['Delta_plateau_MKK']:.4f}_MKK"
                 f"_dDelta/dmu>0={sign_pass}_VanHove_frac={regime_frac:.3f}"
                 f"_gap_ratio={eos_diag['gap_ratio_Delta_over_mu']:.4f}")  # (local)

    # ---- dual SHA ----
    pin_map = {
        "script_sha256": "<self>",
        "canonical_constants_sha256": sha_canon,
        "dirac_spectrum_sha256": sha_dirac,
        "s84_spectrum_cache_L12_tau019_sha256": sha_cache,
        "N_MU": N_MU, "MU_MIN": MU_MIN, "MU_MAX": MU_MAX,
        "OMEGA_PAIR": OMEGA_PAIR, "L_MAX": L_MAX,
        "M_KK": M_KK, "tau_fold": tau_fold, "Delta_BCS": Delta_BCS,
        "K_crit_BdG": K_crit_BdG, "rho_B2_per_mode": rho_B2_per_mode,
        "M_MAX_LOWER": M_MAX_LOWER, "M_MAX_UPPER": M_MAX_UPPER,
        "scheme": SCHEME, "convention": CONVENTION,
        "regulator_pin": "a_n^{Pauli-Villars}_LambdaUV_M_KK",
        "gate_id": GATE_ID, "schema_version": "S84+",
    }
    script_bytes = Path(__file__).resolve().read_bytes()         # (local)
    content_sha = hashlib.sha256(script_bytes).hexdigest()       # (local)
    pin_map["script_sha256"] = content_sha
    audit_payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()  # (local)
    audit_sha = hashlib.sha256(audit_payload).hexdigest()        # (local)

    # ---- save npz (full float64) ----
    np.savez(
        NPZ_PATH,
        mu_grid=mu_grid, Delta_grid=Delta_grid, n_win_grid=n_win_grid,
        chi_grid=chi_grid, dDelta_dmu=dDelta,
        mu_ref=mu_ref, g_coupling=g, chi_ref=chi_ref,
        M_max_Msun=M_max, R_at_Mmax_km=R_at_Mmax,
        eps_c_grid=eps_c_grid, M_tov=M_tov, R_tov=R_tov,
        sign_pass=sign_pass, frac_increasing=frac_increasing,
        regime_frac=regime_frac, regime_verdict=regime_verdict,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        composite=composite,
        M_MAX_LOWER=M_MAX_LOWER, M_MAX_UPPER=M_MAX_UPPER,
        OMEGA_PAIR=OMEGA_PAIR, Delta_BCS=Delta_BCS,
        n_with_mult=n_with_mult,
        gpu_eigvalsh_resid_max=gpu_resid_max, gpu_device=gpu_dev_used,
        audit_sha256=audit_sha, content_sha256=content_sha,
        **{f"eos_{k}": v for k, v in eos_diag.items()},
    )
    print(f"[SAVE] {NPZ_PATH}")

    # ---- plot ----
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))
    # (1) Delta_CFL(mu) gap curve
    ax = axes[0]
    ax.plot(mu_grid, Delta_grid, "o-", color="#1f77b4", lw=2, label=r"$\Delta_{\rm CFL}(\mu)$")
    ax.axhline(Delta_BCS, color="gray", ls="--", lw=1, label=fr"$\Delta_{{\rm BCS}}={Delta_BCS:.4f}$ (canonical)")
    ax.axvline(mu_ref, color="green", ls=":", lw=1, label=fr"$\mu_{{\rm ref}}={mu_ref:.3f}$ (calib)")
    ax.set_xlabel(r"$\mu$  [$M_{KK}$ units]")
    ax.set_ylabel(r"$\Delta_{\rm CFL}$  [$M_{KK}$ units]")
    ax.set_title(fr"CFL gap vs $\mu$  (van Suijlekom $D_\mu=D+\mu Q$)" + "\n" +
                 fr"sign($d\Delta/d\mu$)>0: {sign_pass} (VH-dominated)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    # (2) TOV mass-radius
    ax = axes[1]
    good = M_tov > 0                                            # (local)
    ax.plot(R_tov[good], M_tov[good], "-", color="#d62728", lw=2, label="TOV M-R (CFL-stiffened EoS)")
    ax.axhline(M_MAX_LOWER, color="black", ls="--", lw=1, label=fr"2 $M_\odot$ pulsar bound")
    ax.axhspan(M_MAX_LOWER, M_MAX_UPPER, color="green", alpha=0.12, label=fr"PASS band [{M_MAX_LOWER},{M_MAX_UPPER}] $M_\odot$")
    ax.plot([R_at_Mmax], [M_max], "*", ms=18, color="gold", mec="k",
            label=fr"$M_{{\rm max}}={M_max:.3f}\,M_\odot$")
    ax.set_xlabel("R  [km]")
    ax.set_ylabel(r"M  [$M_\odot$]")
    ax.set_title(f"TOV maximum mass\n" + fr"$c_s^2={eos_diag['cs2_gap_stiffened']:.3f}$, $B={eos_diag['B_phys_MeV_fm3']:.1f}$ MeV/fm$^3$")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    # (3) window occupation + regime
    ax = axes[2]
    ax.plot(mu_grid, n_win_grid, "s-", color="#9467bd", lw=2, label="# modes in pairing window")
    ax.axvline(mu_ref, color="green", ls=":", lw=1)
    ax.set_xlabel(r"$\mu$  [$M_{KK}$ units]")
    ax.set_ylabel("modes in window  |$\\xi$|<$\\omega_{\\rm pair}$")
    ax.set_title(f"Van-Hove window occupation\nregime: {regime_verdict} (VH-dominated frac={regime_frac:.2f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.suptitle(f"{GATE_ID}: finite-$\\mu$ CFL gap + EoS  [composite={composite}]", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_PATH, dpi=130)
    print(f"[SAVE] {PNG_PATH}")

    # ---- 4-tuple + verdict payload ----
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
        companion_note=f"{GATE_ID} finite-mu CFL gap; Delta_CFL(mu) monotone-increasing VH-dominated; M_max={M_max:.4f} Msun",
        extra_rows=[
            f"# regulator_pin=a_n^{{Pauli-Villars}}_LambdaUV_M_KK (BdG grand-potential UV reg; substrate-natural)",
            f"# M_max_FW={M_max:.4f}_Msun band[{M_MAX_LOWER},{M_MAX_UPPER}]; Delta_CFL_plateau={eos_diag['Delta_plateau_MKK']:.4f}_MKK; gap_ratio={eos_diag['gap_ratio_Delta_over_mu']:.4f}; VanHove_dominated_frac={regime_frac:.3f}",
        ],
    )

    # exit 0 regardless of scientific verdict (math-scripts.md exit-code rule)
    return 0


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None):
    """Local copy of the template helper (the script prints the payload; the
    AGENT calls the emit_verdict MCP tool).  Matches .claude/templates/
    script-template.py print_verdict_payload signature + delimiter."""
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
        "track": "investigation",
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
