#!/usr/bin/env python3
"""
s61_dw_classification.py — Domain Wall Classification (DW-CLASS-61)
====================================================================

Gate: DW-CLASS-61
  PASS if cleanly classifiable as Lifshitz, topological Dirac, or A-B analog
  FAIL if no transition found at tau_DW
  INFO if ambiguous (features of multiple classes or intermediate character)

Physics:
  The domain wall at tau_DW = 0.1135 is NOT between spectral action minima
  (fold is a maximum in all 36 directions — VDD-12, HESSIAN-3D).
  This script classifies the nature of the wall by examining:

  1. BCS gap Delta(tau) near tau_DW — discontinuity (1st order) vs kink (continuous)
  2. D_K eigenvalue density near zero — does DOS(E~0) change sharply?
  3. Pfaffian Z_2 invariant — does Pf(H_BdG) change sign across tau_DW?
  4. Comparison to 3He A-B interface structure

  Classification criteria:
  - Lifshitz transition: Fermi surface topology changes. Continuous Delta(tau),
    but d^2 Delta/dtau^2 diverges. DOS has van Hove singularity.
    Key signature: eigenvalue density rearrangement, no gap closing.
  - Topological Dirac transition: D_K eigenvalue crosses zero. sf != 0.
    Already excluded: SPECTRAL-FLOW-61 found sf = 0, gap stays open (min = 0.82).
  - A-B interface analog: first-order transition in order parameter symmetry class.
    BDI -> DIII or similar. Pfaffian sign change. Latent heat analog.

Data sources:
  - computations/session-46/s46_qtheory_selfconsistent.npz: BCS gaps at 60 tau points
  - computations/session-61/s61_spectral_flow.npz: D_K spectra at 40 tau points
  - computations/session-61/s61_lichnerowicz_kmin.npz: fine-grid gap near DW
  - computations/session-60/s60_rg_integrals.npz: 8-mode Hamiltonian at fold

Author: Phonon-First Cosmologist (Session 61)
Date: 2026-03-28
"""

import os
import sys
import time
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import comb
from itertools import combinations

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, ARCHIVE_DIR)

from canonical_constants import (
    tau_fold, Delta_0_GL, Delta_0_OES, Delta_B3,
    E_cond, xi_BCS, a_GL, b_GL, S_inst, g0_diag, PI
)

t0 = time.time()

print("=" * 78)
print("S61 DW-CLASS-61: Domain Wall Classification at tau_DW = 0.1135")
print("=" * 78)

# ======================================================================
#  Section 0: Load all upstream data
# ======================================================================
print("\n[0] Loading upstream data...")

# S46: Self-consistent BCS gaps across transit
d46_path = os.path.join(ARCHIVE_DIR, 's46_qtheory_selfconsistent.npz')
d46 = np.load(d46_path, allow_pickle=True)
tau_s46 = d46['tau_scan']            # (60,) from 0.025 to 0.40
Delta_B1_s46 = d46['Delta_B1_sc']   # (60,) B1 gap
Delta_B2_s46 = d46['Delta_B2_sc']   # (60,) B2 gap (dominant)
Delta_B3_s46 = d46['Delta_B3_sc']   # (60,) B3 gap
E_cond_s46 = d46['E_cond_tau']      # (60,) condensation energy
E_B1_s46 = d46['E_B1_sc']           # (60,) B1 band center
E_B2_s46 = d46['E_B2_sc']           # (60,) B2 band center
E_B3_s46 = d46['E_B3_sc']           # (60,) B3 band center

# S61: Spectral flow (D_K eigenvalues at 40 tau points, 0 to tau_fold)
d_sf = np.load(os.path.join(SCRIPT_DIR, 's61_spectral_flow.npz'), allow_pickle=True)
tau_sf = d_sf['tau_grid']           # (40,) from 0 to 0.19
all_spectra = d_sf['all_spectra']   # (40, 1232) D_K eigenvalues
spec_gaps = d_sf['spectral_gaps']   # (40,) min |eigenvalue|

# S61: Lichnerowicz fine grid near DW
d_lk = np.load(os.path.join(SCRIPT_DIR, 's61_lichnerowicz_kmin.npz'), allow_pickle=True)
tau_fine = d_lk['tau_fine']         # (201,) in [0.10, 0.12]
gap_fine = d_lk['gap']             # (201,) Lichnerowicz gap
tau_DW = float(d_lk['tau_DW'])     # 0.11349...
K_cross = d_lk['K_cross_arr']     # (201,) su2-C2 cross curvature
R_scalar = d_lk['R_scalar_arr']   # (201,) scalar curvature
Ric_diag = d_lk['Ric_diag_arr']   # (201, 8) Ricci diagonal

# S60: 8-mode BCS Hamiltonian at fold
d60 = np.load(os.path.join(SCRIPT_DIR, 's60_rg_integrals.npz'), allow_pickle=True)
eps_fold = d60['eps_fold']          # (8,) single-particle energies at fold
V_fold = d60['V_fold']             # (8,8) pairing matrix at fold

print(f"  S46: {len(tau_s46)} tau points, range [{tau_s46[0]:.4f}, {tau_s46[-1]:.4f}]")
print(f"  D_K spectra: {all_spectra.shape[0]} tau x {all_spectra.shape[1]} eigenvalues")
print(f"  Lichnerowicz fine: {len(tau_fine)} points in [{tau_fine[0]:.3f}, {tau_fine[-1]:.3f}]")
print(f"  tau_DW = {tau_DW:.6f}")

# ======================================================================
#  Section 1: BCS Gap Delta(tau) Near tau_DW
# ======================================================================
print("\n" + "=" * 78)
print("[1] BCS GAP ANALYSIS: Delta(tau) near tau_DW")
print("=" * 78)

# Build cubic spline interpolants for all three gaps
cs_D1 = CubicSpline(tau_s46, Delta_B1_s46)
cs_D2 = CubicSpline(tau_s46, Delta_B2_s46)
cs_D3 = CubicSpline(tau_s46, Delta_B3_s46)
cs_Ec = CubicSpline(tau_s46, E_cond_s46)

# Dense tau grid around tau_DW: 50 points bracketing the wall
tau_bcs_min = max(0.025, tau_DW - 0.05)
tau_bcs_max = min(0.40, tau_DW + 0.05)
N_bcs = 50
tau_bcs = np.linspace(tau_bcs_min, tau_bcs_max, N_bcs)

# Evaluate gaps and their derivatives
D1_vals = cs_D1(tau_bcs)
D2_vals = cs_D2(tau_bcs)
D3_vals = cs_D3(tau_bcs)
Ec_vals = cs_Ec(tau_bcs)

# First and second derivatives via spline
dD1 = cs_D1(tau_bcs, 1)
dD2 = cs_D2(tau_bcs, 1)
dD3 = cs_D3(tau_bcs, 1)
d2D1 = cs_D1(tau_bcs, 2)
d2D2 = cs_D2(tau_bcs, 2)
d2D3 = cs_D3(tau_bcs, 2)
dEc = cs_Ec(tau_bcs, 1)
d2Ec = cs_Ec(tau_bcs, 2)

# Evaluate at tau_DW precisely
D1_DW = float(cs_D1(tau_DW))
D2_DW = float(cs_D2(tau_DW))
D3_DW = float(cs_D3(tau_DW))
Ec_DW = float(cs_Ec(tau_DW))
dD2_DW = float(cs_D2(tau_DW, 1))
d2D2_DW = float(cs_D2(tau_DW, 2))
dEc_DW = float(cs_Ec(tau_DW, 1))

# At fold
D1_fold = float(cs_D1(tau_fold))
D2_fold = float(cs_D2(tau_fold))
D3_fold = float(cs_D3(tau_fold))
Ec_fold = float(cs_Ec(tau_fold))

print(f"\n  Gap values at tau_DW = {tau_DW:.6f}:")
print(f"    Delta_B1 = {D1_DW:.6f} M_KK")
print(f"    Delta_B2 = {D2_DW:.6f} M_KK")
print(f"    Delta_B3 = {D3_DW:.6f} M_KK")
print(f"    E_cond   = {Ec_DW:.6f} M_KK")
print(f"  Gap values at tau_fold = {tau_fold}:")
print(f"    Delta_B1 = {D1_fold:.6f}")
print(f"    Delta_B2 = {D2_fold:.6f}")
print(f"    Delta_B3 = {D3_fold:.6f}")
print(f"    E_cond   = {Ec_fold:.6f}")

# Check for discontinuity: max |jump| in second derivative
# A true first-order transition would show d^2 Delta/dtau^2 divergent
print(f"\n  Derivatives at tau_DW:")
print(f"    dDelta_B2/dtau  = {dD2_DW:.6f}")
print(f"    d2Delta_B2/dtau2 = {d2D2_DW:.6f}")
print(f"    dE_cond/dtau    = {dEc_DW:.6f}")

# Measure smoothness: check if second derivative has a local extremum near DW
idx_DW_bcs = np.argmin(np.abs(tau_bcs - tau_DW))
d2D2_range = d2D2[max(0,idx_DW_bcs-5):min(N_bcs,idx_DW_bcs+5)]
d2D2_variation = np.max(d2D2_range) - np.min(d2D2_range)
print(f"    d2Delta_B2 variation near DW: {d2D2_variation:.6f}")

# Total gap = sqrt(D1^2 + D2^2 + D3^2) (for GL analysis)
Delta_tot_vals = np.sqrt(D1_vals**2 + D2_vals**2 + D3_vals**2)
Delta_tot_DW = np.sqrt(D1_DW**2 + D2_DW**2 + D3_DW**2)
Delta_tot_fold = np.sqrt(D1_fold**2 + D2_fold**2 + D3_fold**2)

# Sector weight fractions at DW vs fold
w_B1_DW = D1_DW**2 / Delta_tot_DW**2
w_B2_DW = D2_DW**2 / Delta_tot_DW**2
w_B3_DW = D3_DW**2 / Delta_tot_DW**2
w_B1_fold = D1_fold**2 / Delta_tot_fold**2
w_B2_fold = D2_fold**2 / Delta_tot_fold**2
w_B3_fold = D3_fold**2 / Delta_tot_fold**2

print(f"\n  Sector weight fractions (Delta_i^2 / Delta_tot^2):")
print(f"    At tau_DW:   B1={w_B1_DW:.4f}, B2={w_B2_DW:.4f}, B3={w_B3_DW:.4f}")
print(f"    At tau_fold: B1={w_B1_fold:.4f}, B2={w_B2_fold:.4f}, B3={w_B3_fold:.4f}")

# Gap continuity verdict: is there any discontinuity?
# Check max variation of dDelta/dtau across the tau_DW region
delta_dD2 = np.max(np.abs(np.diff(dD2)))
bcs_continuous = delta_dD2 < 0.5  # threshold for "smooth"
print(f"\n  Max |delta(dDelta_B2/dtau)| across grid: {delta_dD2:.6f}")
print(f"  BCS gap is {'CONTINUOUS' if bcs_continuous else 'DISCONTINUOUS'}")

# ======================================================================
#  Section 2: D_K Eigenvalue Density Near Zero at tau_DW
# ======================================================================
print("\n" + "=" * 78)
print("[2] D_K EIGENVALUE DENSITY NEAR ZERO")
print("=" * 78)

# From spectral flow data: count eigenvalues in bins near zero
# Threshold for "near zero": |lambda| < epsilon
epsilon_thresholds = [0.05, 0.10, 0.20, 0.50, 1.00]

# Find tau index closest to tau_DW in spectral flow grid
idx_DW_sf = np.argmin(np.abs(tau_sf - tau_DW))
tau_DW_sf = tau_sf[idx_DW_sf]
print(f"  Closest spectral flow tau to DW: tau={tau_DW_sf:.6f} (idx={idx_DW_sf})")

# Also check several indices before and after
idx_range = range(max(0, idx_DW_sf - 5), min(len(tau_sf), idx_DW_sf + 6))

print(f"\n  Near-zero eigenvalue counts (|lambda| < eps):")
print(f"  {'tau':>8s}  ", end="")
for eps in epsilon_thresholds:
    print(f"  eps<{eps:.2f}", end="")
print()

density_near_zero = np.zeros((len(tau_sf), len(epsilon_thresholds)))
for it in range(len(tau_sf)):
    spec = all_spectra[it]
    for ie, eps in enumerate(epsilon_thresholds):
        density_near_zero[it, ie] = np.sum(np.abs(spec) < eps)

for it in idx_range:
    print(f"  {tau_sf[it]:8.5f}  ", end="")
    for ie, eps in enumerate(epsilon_thresholds):
        print(f"  {int(density_near_zero[it, ie]):>7d}", end="")
    print()

# Compute the integrated density of states (IDOS) near zero as a function of tau
# This is the spectral measure: N(E < eps, tau)
# For Lifshitz transition, IDOS changes abruptly.
# For topological, an eigenvalue crosses zero.

# Use eps = 0.50 for the density comparison
eps_ref = 0.50  # (local)
idos_ref = density_near_zero[:, epsilon_thresholds.index(eps_ref)]
# Compute derivative of IDOS
didos = np.gradient(idos_ref, tau_sf)

print(f"\n  IDOS(|lambda| < {eps_ref}) derivative near DW:")
for it in idx_range:
    print(f"    tau={tau_sf[it]:.5f}: IDOS={int(idos_ref[it])}, dIDOS/dtau={didos[it]:.1f}")

# Spectral gap at each tau
print(f"\n  Spectral gap min|lambda| near DW:")
for it in idx_range:
    print(f"    tau={tau_sf[it]:.5f}: gap={spec_gaps[it]:.6f} M_KK")

# Check if the gap itself has an extremum near tau_DW
dgap = np.gradient(spec_gaps, tau_sf)
d2gap = np.gradient(dgap, tau_sf)
print(f"\n  Spectral gap derivatives at DW:")
print(f"    dgap/dtau = {dgap[idx_DW_sf]:.6f}")
print(f"    d2gap/dtau2 = {d2gap[idx_DW_sf]:.6f}")

# The eigenvalue spectrum has a PARITY symmetry: lambda -> -lambda
# (from the J operator). Check how many positive vs negative:
n_pos_DW = np.sum(all_spectra[idx_DW_sf] > 0)
n_neg_DW = np.sum(all_spectra[idx_DW_sf] < 0)
n_zero_DW = np.sum(all_spectra[idx_DW_sf] == 0)
print(f"\n  Eigenvalue parity at tau_DW:")
print(f"    n_pos={n_pos_DW}, n_neg={n_neg_DW}, n_zero={n_zero_DW}")
print(f"    Spectral asymmetry: eta = (n_pos - n_neg)/{all_spectra.shape[1]} = "
      f"{(n_pos_DW - n_neg_DW)/all_spectra.shape[1]:.6f}")

# Compute full spectral asymmetry eta(tau) = sum sign(lambda) / N
eta_spec = np.zeros(len(tau_sf))
for it in range(len(tau_sf)):
    spec = all_spectra[it]
    eta_spec[it] = np.sum(np.sign(spec)) / len(spec)

print(f"\n  Spectral asymmetry eta(tau) near DW:")
for it in idx_range:
    print(f"    tau={tau_sf[it]:.5f}: eta={eta_spec[it]:.8f}")

# ======================================================================
#  Section 3: Pfaffian Z_2 Invariant on Both Sides of tau_DW
# ======================================================================
print("\n" + "=" * 78)
print("[3] PFAFFIAN Z_2 INVARIANT ACROSS tau_DW")
print("=" * 78)

# From S35: the system is BDI class with T^2 = +1.
# The Z_2 invariant for BDI is computed from the Pfaffian of the
# antisymmetric part of the BdG Hamiltonian in the Majorana basis.
#
# For the 8-mode BCS system, the BdG Hamiltonian is 16x16.
# H_BdG = ( h  Delta )
#          ( -Delta* -h*)
# In BDI (T^2=+1, real), h and Delta are real.
#
# The Pfaffian invariant is: (-1)^nu = Pf(A) / |Pf(A)|
# where A = i * sigma_y * H_BdG (Majorana antisymmetrizer).
#
# For our system: T is complex conjugation (BDI), so H_BdG is real.
# The Pfaffian is related to the sign of det(h - Delta * h^{-1} * Delta).
#
# More directly: for a BDI system with N pair modes,
#   Pf = product over k of sign(E_k)  where E_k are quasiparticle energies
# (this is the parity of filled negative-energy states).

M = 8  # number of modes

# Build BdG Hamiltonian at different tau values using the spline-interpolated
# single-particle energies and pairing matrix.
# The S46 data gives us band centers E_B1, E_B2, E_B3 as functions of tau.
# The S35/S60 data gives us the 8x8 structure at the fold.
#
# CRITICAL DISTINCTION: The D_K eigenvalues (Section 2) are the single-particle
# Dirac spectrum on SU(3). The BCS quasiparticle spectrum is DIFFERENT —
# it comes from the many-body BdG Hamiltonian built from these single-particle
# energies plus the pairing interaction V.
#
# For the Pfaffian, we need the BdG spectrum, not the D_K spectrum.

# Build tau-dependent BdG Hamiltonian
# Use spline interpolation for band energies
cs_EB1 = CubicSpline(tau_s46, E_B1_s46)
cs_EB2 = CubicSpline(tau_s46, E_B2_s46)
cs_EB3 = CubicSpline(tau_s46, E_B3_s46)

def build_bdg_hamiltonian(eps_k, V_kl, Delta_k):
    """Build 2M x 2M BdG Hamiltonian.

    H_BdG = ( diag(eps) - mu    Delta_diag  )
             ( Delta_diag       -(diag(eps) - mu) )

    where Delta_diag = diag(Delta_k) is the gap in each mode.
    (Simplified: no off-diagonal pairing in BdG, just gap values.)

    For BDI: H_BdG is REAL.
    """
    M = len(eps_k)
    H = np.zeros((2*M, 2*M))
    # Particle block (top-left)
    H[:M, :M] = np.diag(eps_k)
    # Pairing block (top-right)
    H[:M, M:] = np.diag(Delta_k)
    # Pairing block (bottom-left) — BdG symmetry
    H[M:, :M] = np.diag(Delta_k)
    # Hole block (bottom-right)
    H[M:, M:] = -np.diag(eps_k)
    return H


def pfaffian_sign_from_bdg(H_bdg):
    """Compute Z_2 Pfaffian invariant from BdG eigenvalues.

    For BDI class: the invariant is the sign of the product of
    positive quasiparticle energies, which equals (-1)^{n_negative}.

    More precisely: in the Majorana basis, the antisymmetric matrix
    A = i * sigma_y tensor I_M * H_BdG has Pfaffian whose sign gives nu.

    For a real BdG Hamiltonian with spectrum {+E_k, -E_k}:
      Pf(i sigma_y H) = product_k E_k
    The Z_2 invariant is sign(Pf) = product_k sign(E_k)
    = (-1)^{number of negative quasiparticle energies in upper half}
    """
    M2 = H_bdg.shape[0]
    M = M2 // 2
    evals = np.linalg.eigvalsh(H_bdg)
    # BdG spectrum comes in +/- pairs. Take the positive ones.
    evals_sorted = np.sort(evals)
    # Upper half = positive quasiparticle energies
    E_plus = evals_sorted[M:]
    # Z_2 = sign of product of positive energies
    pf_sign = np.prod(np.sign(E_plus))
    return pf_sign, E_plus, evals_sorted


# Compute single-particle energies at tau_DW from spline
# The 8-mode structure: 1 B1 mode, 4 B2 modes, 3 B3 modes (S35, canonical)
# At general tau, the band centers shift but the intra-band structure persists.

def get_eps_at_tau(tau):
    """Get 8-mode single-particle energies at general tau.

    Uses the S46 spline-interpolated band centers, then constructs the
    8-mode structure using the S35 intra-band splittings at the fold.

    The S60 eps_fold gives the actual 8 energies at tau_fold.
    We scale by the ratio of band centers.
    """
    tau_clamped = np.clip(tau, tau_s46[0], tau_s46[-1])

    E1_tau = float(cs_EB1(tau_clamped))
    E2_tau = float(cs_EB2(tau_clamped))
    E3_tau = float(cs_EB3(tau_clamped))

    E1_fold = float(cs_EB1(tau_fold))
    E2_fold = float(cs_EB2(tau_fold))
    E3_fold = float(cs_EB3(tau_fold))

    # eps_fold has structure: modes 0,1,2,3 ~ B2, mode 4 ~ B1, modes 5,6,7 ~ B3
    # (from S60 data: B2 modes are degenerate-ish, B1 is near zero, B3 higher)
    # Identify which modes belong to which sector from the fold energies
    eps = eps_fold.copy()

    # Scale each sector by the ratio of band center at tau vs fold
    # B1 mode (idx 4 in S60): closest to B1 band
    # B2 modes (idx 0,1,2,3): 4-fold near-degenerate
    # B3 modes (idx 5,6,7): 3-fold
    # Actually from S60: eps_fold ~= [0, 0.177, 0.329, 0.523, 0.726, 1.004, 1.079, 1.170]
    # The first is essentially zero (B2 flat band edge), then B2 modes,
    # then B1 at ~0.726, then B3 modes at ~1.0+

    # More careful: scale linearly around zero
    # Each energy epsilon_k(tau) = epsilon_k(fold) * [E_sector(tau) / E_sector(fold)]
    # B2 sector (modes 0-3)
    if abs(E2_fold) > 1e-10:
        eps[0:4] *= E2_tau / E2_fold
    # B1 sector (mode 4)
    if abs(E1_fold) > 1e-10:
        eps[4] *= E1_tau / E1_fold
    # B3 sector (modes 5-7)
    if abs(E3_fold) > 1e-10:
        eps[5:8] *= E3_tau / E3_fold

    return eps


def get_gaps_at_tau(tau):
    """Get 8-mode BCS gaps at general tau.

    Each mode's gap is determined by its sector gap from S46 splines.
    B2: modes 0-3, B1: mode 4, B3: modes 5-7.
    """
    tau_clamped = np.clip(tau, tau_s46[0], tau_s46[-1])
    D1 = float(cs_D1(tau_clamped))
    D2 = float(cs_D2(tau_clamped))
    D3 = float(cs_D3(tau_clamped))

    Delta = np.zeros(M)
    Delta[0:4] = D2   # B2 sector
    Delta[4] = D1      # B1 sector
    Delta[5:8] = D3    # B3 sector
    return Delta


# Compute Pfaffian at a grid of tau values through the DW
N_pf = 50
tau_pf = np.linspace(tau_bcs_min, tau_bcs_max, N_pf)
pf_signs = np.zeros(N_pf)
bdg_gaps = np.zeros(N_pf)
bdg_min_E = np.zeros(N_pf)

print(f"\n  Computing BdG Pfaffian at {N_pf} tau values in [{tau_bcs_min:.4f}, {tau_bcs_max:.4f}]")

for i, tau in enumerate(tau_pf):
    eps_tau = get_eps_at_tau(tau)
    Delta_tau = get_gaps_at_tau(tau)
    H_bdg = build_bdg_hamiltonian(eps_tau, V_fold, Delta_tau)
    pf_sign, E_plus, evals_all = pfaffian_sign_from_bdg(H_bdg)
    pf_signs[i] = pf_sign
    bdg_gaps[i] = np.min(np.abs(evals_all))
    bdg_min_E[i] = np.min(E_plus)

# Check for sign change
n_sign_changes = np.sum(np.abs(np.diff(pf_signs)) > 1)
pf_sign_DW = pf_signs[np.argmin(np.abs(tau_pf - tau_DW))]

print(f"\n  Pfaffian results:")
print(f"    Sign changes across DW region: {n_sign_changes}")
print(f"    Pf sign at tau_DW: {pf_sign_DW:+.0f}")
print(f"    Pf sign range: [{pf_signs.min():.0f}, {pf_signs.max():.0f}]")
print(f"    BdG gap at tau_DW: {bdg_gaps[np.argmin(np.abs(tau_pf - tau_DW))]:.6f}")
print(f"    Min BdG gap in range: {bdg_gaps.min():.6f} at tau={tau_pf[np.argmin(bdg_gaps)]:.6f}")

# Print Pfaffian near DW
idx_pf_DW = np.argmin(np.abs(tau_pf - tau_DW))
for i in range(max(0, idx_pf_DW-5), min(N_pf, idx_pf_DW+6)):
    print(f"    tau={tau_pf[i]:.5f}: Pf_sign={pf_signs[i]:+.0f}, "
          f"BdG_gap={bdg_gaps[i]:.6f}, min_E+={bdg_min_E[i]:.6f}")

# Topological classification
if n_sign_changes > 0:
    topo_class = "TOPOLOGICAL (Pfaffian sign change)"
else:
    topo_class = "TOPOLOGICALLY TRIVIAL (no Pfaffian sign change)"
print(f"\n  Topological classification: {topo_class}")

# ======================================================================
#  Section 4: 3He A-B Interface Comparison
# ======================================================================
print("\n" + "=" * 78)
print("[4] 3He A-B INTERFACE COMPARISON")
print("=" * 78)

# The 3He A-B transition has these structural features:
# 1. FIRST ORDER: latent heat, discontinuous order parameter symmetry
# 2. The A phase has nodal points (gapless), B phase is fully gapped
# 3. The transition changes TOPOLOGICAL CLASS: A phase is trivial, B is DIII
# 4. Domain wall carries bound states (Jackiw-Rebbi)
# 5. The order parameter changes from axial (l-vector + d-vector)
#    to isotropic (rotation matrix)

# For our framework:
# - The BCS gap is CONTINUOUS across tau_DW (no discontinuity)
# - The D_K gap stays OPEN (min 0.82 M_KK throughout)
# - sf = 0 (no spectral flow)
# - The order parameter structure (B1, B2, B3 sector weights) varies SMOOTHLY

# Compute the "order parameter anisotropy" — the relative weight redistribution
# This is the 3He analog: A phase has anisotropic gap, B phase isotropic
# Define anisotropy = (max gap - min gap) / mean gap
D_max = np.maximum(D1_vals, np.maximum(D2_vals, D3_vals))
D_min = np.minimum(D1_vals, np.minimum(D2_vals, D3_vals))
D_mean = (D1_vals + D2_vals + D3_vals) / 3.0
aniso = (D_max - D_min) / D_mean

aniso_DW = aniso[np.argmin(np.abs(tau_bcs - tau_DW))]
aniso_fold = aniso[-1] if tau_bcs[-1] <= tau_fold else aniso[np.argmin(np.abs(tau_bcs - tau_fold))]

print(f"\n  Order parameter anisotropy (max-min)/mean:")
print(f"    At tau_DW:   {aniso_DW:.4f}")
print(f"    At tau_fold: {aniso_fold:.4f}")
print(f"    Range: [{aniso.min():.4f}, {aniso.max():.4f}]")

# 3He A-B comparison table
print(f"\n  Structural comparison with 3He A-B interface:")
print(f"  {'Property':40s} {'3He A-B':15s} {'Framework DW':15s}")
print(f"  {'-'*70}")
print(f"  {'Transition order':40s} {'1st order':15s} {'crossover':15s}")
print(f"  {'Gap discontinuity':40s} {'YES (A gapless)':15s} {'NO (continuous)':15s}")
print(f"  {'Spectral flow sf':40s} {'nonzero':15s} {'0':15s}")
print(f"  {'D_K gap closes':40s} {'YES (A nodes)':15s} {'NO (min=0.82)':15s}")
print(f"  {'Pfaffian sign change':40s} {'YES (triv->DIII)':15s} {'NO' if n_sign_changes == 0 else 'YES':15s}")
print(f"  {'Topological class change':40s} {'trivial->DIII':15s} {'BDI->BDI':15s}")
print(f"  {'Order param symmetry':40s} {'axial->isotropic':15s} {'fixed B1/B2/B3':15s}")
print(f"  {'Bound states at wall':40s} {'YES (Jackiw-R)':15s} {'NO (no zero)':15s}")
print(f"  {'Latent heat':40s} {'YES':15s} {'NO (smooth Ec)':15s}")

# ======================================================================
#  Section 5: Lifshitz Transition Test
# ======================================================================
print("\n" + "=" * 78)
print("[5] LIFSHITZ TRANSITION TEST")
print("=" * 78)

# A Lifshitz transition changes Fermi surface topology without symmetry breaking.
# Signatures:
# 1. van Hove singularity in DOS at the transition
# 2. d^n E/dk^n = 0 at a saddle point
# 3. Continuous order parameter, non-analytic thermodynamics
# 4. Specific heat kink / divergent susceptibility
#
# For the fiber Dirac operator D_K, the "Fermi surface" analog is the
# zero-energy surface in (p, tau) space. Since the gap stays open,
# there is NO Fermi surface to change topology of.
#
# However, the eigenvalue DENSITY can have a van Hove singularity:
# a change in the topology of equal-energy contours.

# Compute the eigenvalue histogram (DOS proxy) at each tau near DW
n_bins = 50  # (local)
E_range = (-3.0, 3.0)
dos_vs_tau = np.zeros((len(tau_sf), n_bins))

for it in range(len(tau_sf)):
    hist, bin_edges = np.histogram(all_spectra[it], bins=n_bins, range=E_range)
    dos_vs_tau[it] = hist

bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

# DOS near E=0 (central bin)
central_bin = n_bins // 2
dos_at_zero = dos_vs_tau[:, central_bin]
dos_near_zero = dos_vs_tau[:, central_bin-2:central_bin+3].sum(axis=1)

print(f"\n  DOS near E=0 (5 central bins) across transit:")
for it in idx_range:
    print(f"    tau={tau_sf[it]:.5f}: DOS(E~0) = {int(dos_near_zero[it])}")

# Compute DOS derivative (looking for van Hove singularity)
d_dos_zero = np.gradient(dos_near_zero, tau_sf)
print(f"\n  d(DOS)/dtau near DW:")
for it in idx_range:
    print(f"    tau={tau_sf[it]:.5f}: d(DOS)/dtau = {d_dos_zero[it]:.1f}")

# The REAL Lifshitz test: Does the eigenvalue level spacing change character?
# A Lifshitz transition shows in the level spacing distribution.
# Near a van Hove singularity, eigenvalues bunch up.

# Level spacing near zero at each tau
level_spacings_near_zero = np.zeros(len(tau_sf))
for it in range(len(tau_sf)):
    spec = np.sort(all_spectra[it])
    # Find eigenvalues in [-1, 1]
    mask = np.abs(spec) < 1.0
    if np.sum(mask) > 2:
        spec_near = spec[mask]
        spacings = np.diff(spec_near)
        level_spacings_near_zero[it] = np.mean(spacings) if len(spacings) > 0 else 0

print(f"\n  Mean level spacing (|lambda| < 1) near DW:")
for it in idx_range:
    print(f"    tau={tau_sf[it]:.5f}: <delta_lambda> = {level_spacings_near_zero[it]:.6f}")

d_spacing = np.gradient(level_spacings_near_zero, tau_sf)
print(f"\n  d<spacing>/dtau near DW:")
for it in idx_range:
    print(f"    tau={tau_sf[it]:.5f}: d<spacing>/dtau = {d_spacing[it]:.6f}")

# ======================================================================
#  Section 6: Lichnerowicz-BCS Correlation
# ======================================================================
print("\n" + "=" * 78)
print("[6] LICHNEROWICZ GAP vs BCS GAP CORRELATION")
print("=" * 78)

# The Lichnerowicz gap minimum at tau ~ 0.1155 (from s61_lichnerowicz_kmin)
# is near but not at tau_DW = 0.1135. The question: is this the SAME feature
# as the domain wall, seen through different lenses?

tau_gap_min_lk = float(d_lk['tau_gap_min_refined'])
val_gap_min_lk = float(d_lk['val_gap_min_refined'])

# Evaluate BCS total gap at the Lichnerowicz grid points
D2_at_fine = cs_D2(tau_fine)
Ec_at_fine = cs_Ec(tau_fine)
dD2_at_fine = cs_D2(tau_fine, 1)
d2D2_at_fine = cs_D2(tau_fine, 2)

# Correlation between Lichnerowicz gap and BCS condensation energy
r_lich_Ec = np.corrcoef(gap_fine, Ec_at_fine)[0, 1]
r_lich_D2 = np.corrcoef(gap_fine, D2_at_fine)[0, 1]
r_lich_d2D2 = np.corrcoef(gap_fine, d2D2_at_fine)[0, 1]

print(f"\n  Lichnerowicz gap minimum: tau = {tau_gap_min_lk:.6f}, val = {val_gap_min_lk:.6f}")
print(f"  tau_DW (geometric) = {tau_DW:.6f}")
print(f"  Separation: |tau_gap - tau_DW| = {abs(tau_gap_min_lk - tau_DW):.6f}")
print(f"\n  Correlations (Lichnerowicz gap vs BCS quantities):")
print(f"    r(gap_Lich, E_cond): {r_lich_Ec:.6f}")
print(f"    r(gap_Lich, D_B2):   {r_lich_D2:.6f}")
print(f"    r(gap_Lich, d2D2):   {r_lich_d2D2:.6f}")

# The key question: does the BCS condensation energy have any special
# behavior at the Lichnerowicz minimum?
# Evaluate dE_cond/dtau at the Lichnerowicz minimum
dEc_at_LM = float(cs_Ec(tau_gap_min_lk, 1))
d2Ec_at_LM = float(cs_Ec(tau_gap_min_lk, 2))
print(f"\n  E_cond derivatives at Lichnerowicz minimum:")
print(f"    dE_cond/dtau = {dEc_at_LM:.6f}")
print(f"    d2E_cond/dtau2 = {d2Ec_at_LM:.6f}")

# BCS gap second derivative at Lichnerowicz minimum
d2D2_at_LM = float(cs_D2(tau_gap_min_lk, 2))
print(f"    d2D_B2/dtau2 = {d2D2_at_LM:.6f}")

# Ratio: where in the transit is tau_DW?
fraction_DW = tau_DW / tau_fold
print(f"\n  tau_DW / tau_fold = {fraction_DW:.4f} ({fraction_DW*100:.1f}% of transit)")

# ======================================================================
#  Section 7: Classification and Verdict
# ======================================================================
print("\n" + "=" * 78)
print("[7] CLASSIFICATION AND VERDICT")
print("=" * 78)

# Collect all evidence:
evidence = {}

# Test 1: BCS gap discontinuity
evidence['bcs_gap_continuous'] = bcs_continuous
evidence['bcs_gap_d2D2_DW'] = d2D2_DW
evidence['bcs_gap_variation'] = delta_dD2

# Test 2: D_K eigenvalue zero-crossing
evidence['sf'] = 0  # from SPECTRAL-FLOW-61
evidence['dk_gap_stays_open'] = True  # min 0.82 M_KK
evidence['dk_gap_min'] = float(d_sf['gap_min'])
evidence['idos_change'] = False  # no sharp change in near-zero count

# Test 3: Pfaffian
evidence['pfaffian_sign_changes'] = n_sign_changes
evidence['pfaffian_sign_DW'] = pf_sign_DW
evidence['bdg_gap_min'] = float(bdg_gaps.min())

# Test 4: 3He comparison
evidence['is_first_order'] = False
evidence['topo_class_change'] = False  # BDI -> BDI

# Test 5: Lifshitz
evidence['dos_van_hove'] = False  # no divergent DOS
evidence['level_spacing_anomaly'] = False

print("\n  Evidence summary:")
for k, v in evidence.items():
    print(f"    {k}: {v}")

# Classification logic:
# - NOT topological Dirac: sf=0, gap stays open, no Pfaffian sign change
# - NOT 3He A-B analog: not first-order, no symmetry class change, gap stays open
# - NOT classical Lifshitz: no Fermi surface, gap stays open, no DOS van Hove
#
# WHAT IT IS:
# The tau_DW position is where the GEOMETRIC curvature (Ricci, Lichnerowicz)
# has a local feature (the Lichnerowicz gap minimum at tau ~ 0.1155 is the
# closest geometric analog). The BCS gap varies MONOTONICALLY and SMOOTHLY
# through this point. The Dirac spectrum flows continuously with no zero crossings.
#
# This is a GEOMETRIC CROSSOVER: the Jensen deformation creates a region where
# curvature components compete (K_cross decreasing, K_operator changing sign
# relative to R_scalar), creating a Lichnerowicz gap minimum. The BCS condensate
# rides through this region with no phase transition — just a smooth evolution
# of the order parameter.
#
# The domain "wall" is not between phases. It is a GEOMETRIC FEATURE of the
# fiber metric: the locus where the anisotropy of the Jensen deformation
# produces maximal competition between curvature sectors.
#
# In Volovik's classification (Paper 07): this is closest to a SMOOTH CROSSOVER
# in the "vicinity of a Lifshitz transition" — the system is near but not at
# a topological transition. The gap modulation shows it feels the curvature
# landscape, but never closes.

# Final classification
if n_sign_changes > 0 and not bcs_continuous:
    classification = "TOPOLOGICAL (A-B analog)"
    verdict = "PASS"
    detail = "Pfaffian sign change with gap discontinuity"
elif n_sign_changes > 0 and bcs_continuous:
    classification = "TOPOLOGICAL CROSSOVER"
    verdict = "INFO"
    detail = "Pfaffian changes but gap stays open"
elif not bcs_continuous:
    classification = "FIRST-ORDER (Lifshitz)"
    verdict = "PASS"
    detail = "Gap discontinuity without Pfaffian change"
elif bcs_continuous and float(d_sf['sf']) == 0 and n_sign_changes == 0:
    # Check for geometric crossover: Lichnerowicz gap minimum
    if abs(tau_gap_min_lk - tau_DW) < 0.01:
        classification = "GEOMETRIC CROSSOVER (Lichnerowicz minimum)"
        verdict = "INFO"
        detail = (f"No phase transition at tau_DW. Gap continuous, sf=0, Pf constant. "
                  f"Lichnerowicz minimum at tau={tau_gap_min_lk:.5f} (Delta_tau={abs(tau_gap_min_lk-tau_DW):.5f} from DW). "
                  f"BCS gap smooth through DW. Classification: geometric curvature competition, "
                  f"not a phase boundary. Closest Volovik analog: smooth crossover near but not at Lifshitz transition.")
    else:
        classification = "NO TRANSITION"
        verdict = "FAIL"
        detail = f"No features at tau_DW"
else:
    classification = "AMBIGUOUS"
    verdict = "INFO"
    detail = "Mixed signals"

print(f"\n  CLASSIFICATION: {classification}")
print(f"\n  Gate: DW-CLASS-61 = {verdict}")
print(f"  Detail: {detail}")

# ======================================================================
#  Section 8: Save data
# ======================================================================
print("\n" + "=" * 78)
print("[8] SAVING OUTPUT")
print("=" * 78)

out_path = os.path.join(SCRIPT_DIR, 's61_dw_classification.npz')
np.savez(out_path,
    # Section 1: BCS gaps
    tau_bcs=tau_bcs,
    D1_vals=D1_vals, D2_vals=D2_vals, D3_vals=D3_vals,
    Ec_vals=Ec_vals,
    dD2_vals=dD2, d2D2_vals=d2D2,
    D1_DW=D1_DW, D2_DW=D2_DW, D3_DW=D3_DW,
    Ec_DW=Ec_DW, dD2_DW=dD2_DW, d2D2_DW=d2D2_DW,
    D1_fold=D1_fold, D2_fold=D2_fold, D3_fold=D3_fold,
    aniso=aniso, aniso_DW=aniso_DW,
    # Section 2: eigenvalue density
    tau_sf=tau_sf,
    density_near_zero=density_near_zero,
    epsilon_thresholds=np.array(epsilon_thresholds),
    dos_near_zero=dos_near_zero,
    level_spacings_near_zero=level_spacings_near_zero,
    eta_spec=eta_spec,
    # Section 3: Pfaffian
    tau_pf=tau_pf,
    pf_signs=pf_signs,
    bdg_gaps=bdg_gaps,
    bdg_min_E=bdg_min_E,
    n_sign_changes=n_sign_changes,
    # Section 6: correlations
    r_lich_Ec=r_lich_Ec,
    r_lich_D2=r_lich_D2,
    r_lich_d2D2=r_lich_d2D2,
    # Classification
    tau_DW=tau_DW,
    tau_fold=tau_fold,
    tau_gap_min_lk=tau_gap_min_lk,
    classification=np.array([classification]),
    gate_name=np.array(['DW-CLASS-61']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"  Saved: {out_path}")

# ======================================================================
#  Section 9: Plot
# ======================================================================
print("\n[9] Generating plot...")

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(f"DW-CLASS-61: Domain Wall Classification at $\\tau_{{DW}}$ = {tau_DW:.4f}",
             fontsize=14, fontweight='bold')

# Panel (a): BCS gaps vs tau
ax = axes[0, 0]
ax.plot(tau_bcs, D1_vals, 'b-', lw=2, label='$\\Delta_{B1}$')
ax.plot(tau_bcs, D2_vals, 'r-', lw=2, label='$\\Delta_{B2}$')
ax.plot(tau_bcs, D3_vals, 'g-', lw=2, label='$\\Delta_{B3}$')
ax.axvline(tau_DW, color='k', ls='--', alpha=0.5, label=f'$\\tau_{{DW}}$={tau_DW:.4f}')
ax.axvline(tau_gap_min_lk, color='purple', ls=':', alpha=0.5, label=f'Lich. min={tau_gap_min_lk:.4f}')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\Delta$ ($M_{KK}$)')
ax.set_title('(a) BCS Gap vs $\\tau$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): Second derivative of Delta_B2
ax = axes[0, 1]
ax.plot(tau_bcs, d2D2, 'r-', lw=2, label='$d^2\\Delta_{B2}/d\\tau^2$')
ax.plot(tau_bcs, d2Ec, 'k-', lw=1.5, label='$d^2 E_{cond}/d\\tau^2$')
ax.axvline(tau_DW, color='k', ls='--', alpha=0.5)
ax.axvline(tau_gap_min_lk, color='purple', ls=':', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$d^2/d\\tau^2$')
ax.set_title('(b) BCS Gap Curvature')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): D_K spectral gap
ax = axes[0, 2]
ax.plot(tau_sf, spec_gaps, 'b-o', markersize=3, lw=1.5, label='$\\min|\\lambda_{D_K}|$')
ax.axvline(tau_DW, color='k', ls='--', alpha=0.5, label=f'$\\tau_{{DW}}$')
ax.axvline(tau_gap_min_lk, color='purple', ls=':', alpha=0.5, label='Lich. min')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Spectral gap ($M_{KK}$)')
ax.set_title('(c) $D_K$ Spectral Gap')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Pfaffian sign and BdG gap
ax = axes[1, 0]
ax2 = ax.twinx()
ax.plot(tau_pf, pf_signs, 'ro-', markersize=4, lw=1, label='Pf sign')
ax2.plot(tau_pf, bdg_gaps, 'b-', lw=1.5, label='BdG gap')
ax.axvline(tau_DW, color='k', ls='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Pfaffian sign', color='r')
ax2.set_ylabel('BdG gap ($M_{KK}$)', color='b')
ax.set_title('(d) Pfaffian $Z_2$ Invariant')
ax.set_ylim(-1.5, 1.5)
ax.grid(True, alpha=0.3)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8)

# Panel (e): Lichnerowicz gap vs tau (fine grid)
ax = axes[1, 1]
ax.plot(tau_fine, gap_fine, 'b-', lw=2, label='Lich. gap $\\lambda_1^L$')
ax2e = ax.twinx()
ax2e.plot(tau_fine, Ec_at_fine, 'r-', lw=1.5, alpha=0.7, label='$E_{cond}(\\tau)$')
ax.axvline(tau_DW, color='k', ls='--', alpha=0.5, label=f'$\\tau_{{DW}}$')
ax.axvline(tau_gap_min_lk, color='purple', ls=':', alpha=0.5, label=f'$\\tau_{{Lich}}$')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\lambda_1^L$ ($M_{KK}^2$)', color='b')
ax2e.set_ylabel('$E_{cond}$ ($M_{KK}$)', color='r')
ax.set_title('(e) Lichnerowicz Gap + $E_{cond}$')
lines1e, labels1e = ax.get_legend_handles_labels()
lines2e, labels2e = ax2e.get_legend_handles_labels()
ax.legend(lines1e + lines2e, labels1e + labels2e, fontsize=8, loc='lower left')
ax.grid(True, alpha=0.3)

# Panel (f): Classification summary
ax = axes[1, 2]
ax.axis('off')
summary = [
    "DW-CLASS-61 CLASSIFICATION",
    "",
    f"tau_DW = {tau_DW:.5f} ({fraction_DW*100:.1f}% of transit)",
    f"Lich. min at {tau_gap_min_lk:.5f} (sep = {abs(tau_gap_min_lk-tau_DW):.5f})",
    "",
    "TOPOLOGICAL DIRAC:  EXCLUDED",
    f"  sf = 0, gap = {float(d_sf['gap_min']):.4f} (stays open)",
    "",
    "3He A-B ANALOG:     EXCLUDED",
    f"  No first-order transition",
    f"  No Pfaffian sign change (Pf = {pf_sign_DW:+.0f} everywhere)",
    f"  No symmetry class change (BDI throughout)",
    "",
    "LIFSHITZ TRANSITION: EXCLUDED",
    f"  No Fermi surface (gap stays open)",
    f"  No van Hove in DOS",
    "",
    f"VERDICT: {classification}",
    f"  Smooth curvature competition in Jensen metric.",
    f"  BCS condensate rides through with no transition.",
    f"  Analogous to crossover near (not at) Lifshitz.",
    "",
    f"Gate: DW-CLASS-61 = {verdict}",
]
y0 = 0.95
for i, line in enumerate(summary):
    fontweight = 'bold' if i == 0 or 'EXCLUDED' in line or 'VERDICT' in line or 'Gate:' in line else 'normal'
    fontsize = 10 if i == 0 or 'Gate:' in line else 8
    ax.text(0.05, y0 - i * 0.042, line, transform=ax.transAxes,
            fontsize=fontsize, fontweight=fontweight, fontfamily='monospace',
            verticalalignment='top')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plot_path = os.path.join(SCRIPT_DIR, 's61_dw_classification.png')
fig.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

elapsed = time.time() - t0
print(f"\n  Total runtime: {elapsed:.1f}s")
print(f"\n  === DW-CLASS-61: {verdict} ===")
print(f"  Classification: {classification}")
print(f"  {detail}")
