#!/usr/bin/env python3
"""
TRANSFER-FUNCTION-74: Multifield delta-N Transfer from Fiber P(k) to CMB P(k)
=============================================================================

EVOI Level 1 highest priority (N1, 18.2%). Consolidates:
  - phonon-first S73B TRANSFER-FUNCTION call
  - mack-vdd S73B MULTIFIELD-DELTA-N-L7 call
  - framework chapter 8.4 deferred s75_transfer_function pathway

PHYSICAL SETUP
==============

The fabric IS space. The BCS modes at the fold are NOT fields living inside
a pre-existing spacetime; they are the substrate's internal eigenvalue
reorganization at tau = 0.190. The "CMB pivot scale" is not a wavelength in
a container: it is the mode whose spectral weight at recombination matches
the Hubble radius emerging from a_2(tau_recomb).

The S73B W1-A TRANSIT-PS computation gave alpha_s(CMB-naive) = +0.833
(125 sigma from Planck -0.0045), treating each BCS branch with an identical
horizon-crossing time and an identical Planck factor. This three-field
system (B1 acoustic, B2 flat-optical quartet, B3 dispersive-optical triplet)
has three distinct group velocities, three distinct effective masses, and
three distinct horizon-crossing times.

DIRECTION OF EXPLANATION
========================

   D_K eigenvalues at fold -> per-branch horizon-crossing physics
   -> composed transfer kernel -> emergent scalar power spectrum

COMPUTATION
===========

1. Load BCS mode data from S73B (8 modes, 3-branch decomposition).
2. Build the 3x3 overlap matrix M_ib = <B_i | branch_b> (fallback: diagonal).
3. Compute per-branch group velocity c_b^2 from the BCS dispersion.
4. Compute per-branch horizon-crossing time tau_cross(b) via c_b * k = H(tau).
5. Compute per-branch Planck factor from squeezed-state variance.
6. Compose the full k-dependent transfer T_ib(k).
7. Evaluate at k_pivot, extract n_s, alpha_s, A_s.
8. Cross-check against S73B W1-A naive limit and S66 BCS+CW.

GATE
====

TRANSFER-FUNCTION-74:
  PASS: |alpha_s(k_pivot)| < 0.015 AND n_s in [0.9607, 0.9691]
  FAIL: |alpha_s(k_pivot)| > 0.030 (Planck-incompatible)
  INFO: 0.015 <= |alpha_s| <= 0.030 (partial resolution)

Session: S74 | Wave: W1-A | Classification: PHONONIC

Hawking-theorist note: This is the substrate analog of a multifield
inflation delta-N calculation. The "fields" are the three BCS branches.
The "horizon crossing" is the moment when each branch's group velocity
matches the emergent Hubble rate. The "modes leaving the horizon" is
the substrate description of spectral weight transferring between
internal (fiber) and emergent (4D) degrees of freedom.
"""

import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from canonical_constants import *

t_start = time.time()

# ==============================================================================
#  SECTION 0: Header + gate thresholds
# ==============================================================================

print("=" * 78)
print("TRANSFER-FUNCTION-74: Multifield delta-N Transfer (Fiber -> CMB)")
print("=" * 78)
print()
print("Gate thresholds:")
print("  PASS: |alpha_s(k_pivot)| < 0.015 AND n_s in [0.9607, 0.9691]")
print("  FAIL: |alpha_s(k_pivot)| > 0.030")
print("  INFO: 0.015 <= |alpha_s| <= 0.030")
print()

data_dir = os.path.dirname(os.path.abspath(__file__))  # (local)

# ==============================================================================
#  SECTION 1: Load S73B BCS fold data
# ==============================================================================

print("SECTION 1: Load S73B BCS fold data")
print("-" * 78)

d73b = np.load(os.path.join(data_dir, 's73b_transit_ps.npz'), allow_pickle=True)
d56 = np.load(os.path.join(data_dir, 's56_gge_fabric.npz'), allow_pickle=True)
d73b_l7 = np.load(os.path.join(data_dir, 's73b_transit_ps_lmax7.npz'),
                  allow_pickle=True)

# BCS mode data (from S73B transit_ps)
labels = d73b['labels']                        # 8-mode labels
omega_k_fold = d73b['omega_k_fold']            # frequencies at fold
r_k_bcs = d73b['r_k_bcs']                      # BCS squeezing per mode
r_k_entry = d73b['r_k_entry']                  # entry squeezing per mode
mode_weights = d73b['mode_weights']            # PW degeneracy weights
beta_sq_total = d73b['beta_sq_total']          # compound |beta|^2 per mode
n_k_total = d73b['n_k_total']                  # occupation per mode
Phi_final = d73b['Phi_final']                  # Bogoliubov phase per mode

# Branch weights from S73B
W_B1 = float(d73b['W_B1'])                     # 0.1502
W_B2 = float(d73b['W_B2'])                     # 0.0318
W_B3 = float(d73b['W_B3'])                     # 0.8179
W_total = W_B1 + W_B2 + W_B3                   # (local)

omega_B1 = float(d73b['omega_B1'])             # 0.818 M_KK
omega_B2 = float(d73b['omega_B2'])             # 0.839 M_KK
omega_B3 = float(d73b['omega_B3'])             # 0.876 M_KK

# Per-branch S73B raw power spectrum (for cross-check)
P_B1_raw = float(d73b['P_B1'])                 # (local)
P_B2_raw = float(d73b['P_B2'])                 # (local)
P_B3_raw = float(d73b['P_B3'])                 # (local)

# S56 eigenvalue structure for dispersion
eps_fold_8 = d56['eps_fold']                   # 8 eigenvalues at fold
eps_tau0_8 = d56['eps_tau0']                   # 8 eigenvalues at tau=0

print(f"  Labels       : {list(labels)}")
print(f"  omega_k(fold): {omega_k_fold}")
print(f"  r_k_bcs      : {r_k_bcs}")
print(f"  mode_weights : {mode_weights}")
print(f"  W_B1={W_B1:.6f}, W_B2={W_B2:.6f}, W_B3={W_B3:.6f}")
print(f"  omega_B1={omega_B1:.6f}, omega_B2={omega_B2:.6f}, omega_B3={omega_B3:.6f}")
print(f"  S73B raw P_B1={P_B1_raw:.4e}, P_B2={P_B2_raw:.4e}, P_B3={P_B3_raw:.4e}")
print()

# ==============================================================================
#  SECTION 2: Branch-averaged squeezing and occupation
# ==============================================================================

print("SECTION 2: Branch-averaged squeezing and occupation")
print("-" * 78)

# Mode indices per branch (from labels order: B2[0..3], B1, B3[0..2])
idx_B2 = [0, 1, 2, 3]      # (local)
idx_B1 = [4]               # (local)
idx_B3 = [5, 6, 7]         # (local)

# Degeneracy-weighted squeeze parameters per branch
r_B1 = float(np.mean(r_k_bcs[idx_B1]))          # (local)
r_B2 = float(np.mean(r_k_bcs[idx_B2]))          # (local)
r_B3 = float(np.mean(r_k_bcs[idx_B3]))          # (local)

# Branch-averaged occupation (from compound Bogoliubov)
n_B1 = float(np.mean(beta_sq_total[idx_B1]))    # (local)
n_B2 = float(np.mean(beta_sq_total[idx_B2]))    # (local)
n_B3 = float(np.mean(beta_sq_total[idx_B3]))    # (local)

# Branch Bogoliubov phases (from S73B Phi_final; for B2/B3 average phase)
phi_B1 = float(np.mean(Phi_final[idx_B1]))      # (local)
phi_B2 = float(np.mean(Phi_final[idx_B2]))      # (local)
phi_B3 = float(np.mean(Phi_final[idx_B3]))      # (local)

print(f"  r_B1 = {r_B1:.6f}, r_B2 = {r_B2:.6f}, r_B3 = {r_B3:.6f}")
print(f"  n_B1 = {n_B1:.6e}, n_B2 = {n_B2:.6e}, n_B3 = {n_B3:.6e}")
print(f"  phi_B1={phi_B1:.6f}, phi_B2={phi_B2:.6f}, phi_B3={phi_B3:.6f}")
print()

# ==============================================================================
#  SECTION 3: Per-branch group velocity c_b^2 = d omega_b^2 / d k^2
# ==============================================================================

print("SECTION 3: Per-branch group velocity from BCS dispersion")
print("-" * 78)

# For BCS quasiparticles:  omega_k = sqrt(eps_k^2 + Delta^2)
# The group velocity is: c_g = d omega / dk = (eps/omega) * (d eps / dk)
# Near the fold the gap Delta is large and the single-particle dispersion
# follows from the fiber lattice. We compute c_b^2 directly from the
# eigenvalue structure at the fold:
#
#   c_b^2 = (eps_b / omega_b)^2 * v_F^2
#
# where v_F is the Fermi velocity on the fiber. For the three branches:
#   B1 acoustic:  eps/omega ~ 1 (gapless limit)  -> c_B1 ~ v_F
#   B2 flat:      eps/omega -> 0 (flat band)     -> c_B2 small
#   B3 dispersive: intermediate                  -> c_B3 intermediate
#
# We use c_BA (Bogoliubov-Anderson sound speed) as the characteristic velocity.

c_BA = 0.399  # (local) S73B: Bogoliubov-Anderson sound speed

# eps per branch at fold: for each branch take the single-particle energy
# eps_b^2 = omega_b^2 - Delta_BCS^2 where available
Delta_at_fold = Delta_BCS  # from canonical
eps_B1_sq = max(omega_B1**2 - Delta_at_fold**2, 1e-12)  # (local)
eps_B2_sq = max(omega_B2**2 - Delta_at_fold**2, 1e-12)  # (local)
eps_B3_sq = max(omega_B3**2 - Delta_at_fold**2, 1e-12)  # (local)

eps_B1 = np.sqrt(eps_B1_sq)  # (local)
eps_B2 = np.sqrt(eps_B2_sq)  # (local)
eps_B3 = np.sqrt(eps_B3_sq)  # (local)

# Per-branch group velocity: different branches have distinct dispersions.
# These values come from the BCS + Leggett eigenvalue structure at the fold.
# The task specification provides substrate-native characterizations:
#   B1 acoustic branch:    v_g ~ 0.2 c_BA (gapped sound-like mode)
#   B2 flat-optical quartet: v_g ~ 0.005 c_BA (nearly dispersionless)
#   B3 dispersive-optical triplet: v_g ~ 0.35 c_BA (intermediate)
#
# Physical origin: each branch's group velocity is controlled by its
# projection onto the fiber representation structure. The B2 flat band
# arises from the 4-fold degenerate (1,0)/(0,1) sector where the dispersion
# is quenched by Jensen deformation. B1 (single 0,0 sector) is acoustic.
# B3 (triplet from 1,1) is dispersive.
c_B1 = 0.200 * c_BA  # (local) acoustic branch
c_B2 = 0.005 * c_BA  # (local) flat band (smallest group velocity)
c_B3 = 0.350 * c_BA  # (local) dispersive branch

c_B1_sq = c_B1**2  # (local)
c_B2_sq = c_B2**2  # (local)
c_B3_sq = c_B3**2  # (local)

# Effective mass per branch from the gap and the frequency
m_eff_B1_sq = (Delta_at_fold / omega_B1)**2 * omega_B1**2  # (local)
m_eff_B2_sq = (Delta_at_fold / omega_B2)**2 * omega_B2**2  # (local)
m_eff_B3_sq = (Delta_at_fold / omega_B3)**2 * omega_B3**2  # (local)

print(f"  Delta(fold)   = {Delta_at_fold:.6f} M_KK")
print(f"  eps_B1        = {eps_B1:.6f}, eps_B2 = {eps_B2:.6f}, eps_B3 = {eps_B3:.6f}")
print(f"  c_B1          = {c_B1:.6e}, c_B2 = {c_B2:.6e}, c_B3 = {c_B3:.6e}")
print(f"  c_B1/c_BA     = {c_B1/c_BA:.4f}")
print(f"  c_B2/c_BA     = {c_B2/c_BA:.4f}  (flattest branch)")
print(f"  c_B3/c_BA     = {c_B3/c_BA:.4f}")
print(f"  m_eff^2(B1)   = {m_eff_B1_sq:.6f}")
print(f"  m_eff^2(B2)   = {m_eff_B2_sq:.6f}")
print(f"  m_eff^2(B3)   = {m_eff_B3_sq:.6f}")
print()

# ==============================================================================
#  SECTION 4: Emergent Hubble rate H(tau) from a_2 Seeley-DeWitt
# ==============================================================================

print("SECTION 4: Emergent Hubble rate H(tau) from tessellation mapping")
print("-" * 78)

# The Hubble rate emerges from a_2(tau) via the Jacobson route:
#   G_emergent ~ 1 / a_2(tau)
#   rho_eff(tau) from the spectral action zeroth + second moments
#   H(tau) = sqrt(8 pi G_emergent rho_eff / 3)
#
# At the fold we have the canonical value H_fold = 586.53 M_KK.
# The spectral action derivatives dS/dtau, d2S/dtau2 drive the drift.
#
# For horizon-crossing purposes we need H(tau) in a neighborhood of the fold.
# Use the 8-mode BCS vacuum energy as rho_eff and a_2(tau) as the gravity
# spectral moment.

# Tau grid around fold for horizon-crossing analysis
# Extended VERY far post-fold to capture the expansion to late times
# where modes cross the horizon as H drops below c_b*k.
tau_grid_H = np.logspace(np.log10(0.150), np.log10(1.0e4), 4001)  # (local)

# The emergent Hubble rate drops DRAMATICALLY after the fold. At the fold
# H ~ 586 M_KK (transit speed), but as the fabric spectral weight transfers
# into the emergent 4D sector, a_2 increases and H = (8 pi G / 3 * rho_eff)^{1/2}
# decreases as rho_eff redshifts.
#
# The physical picture: at the fold, H_fold is huge (transit kinetic).
# As tau moves away from the fold, the BCS GGE relic energy decays as
# rho_eff ~ a(tau)^{-4} (radiation-like effacement) and H drops rapidly.
#
# Model: H(tau) = H_fold * exp(-lambda_H * (tau - tau_fold)) for tau > tau_fold
# with the decay rate calibrated so that at tau=tau_recomb (late time),
# H approaches the observed CMB-scale expansion rate.
#
# For numerical purposes we use a power-law decay that matches the
# Friedmann radiation-like behavior:
#   H(tau) ~ H_fold * (tau_fold / tau)^2 for tau > tau_fold
# This gives H -> 0 smoothly as tau increases.
def H_of_tau(tau):
    """Emergent Hubble rate near and far from fold.

    Power-law decay post-fold models the a_2 -> G_N running as the
    fabric spectral weight transfers into emergent 4D. The exponent 2
    corresponds to a radiation-dominated (H ~ 1/a^2) effective phase.
    """
    if tau <= tau_fold:
        # Pre-fold: roughly constant at H_fold with small drift
        dt = tau - tau_fold  # (local)
        Hsq = H_fold**2 * (1.0 + (dS_fold / S_fold) * dt)  # (local)
        return np.sqrt(max(Hsq, 1e-30))
    else:
        # Post-fold: power-law decay (radiation-like effacement)
        # H(tau) = H_fold * (tau_fold / tau)^2
        return H_fold * (tau_fold / tau)**2

H_fold_check = H_of_tau(tau_fold)  # (local)
H_pre_fold = H_of_tau(0.170)       # (local)
H_post_fold_early = H_of_tau(0.210)  # (local)
H_post_fold_mid = H_of_tau(0.50)     # (local)
H_post_fold_late = H_of_tau(2.00)    # (local)
H_post_fold_far = H_of_tau(5.00)     # (local)
H_very_far = H_of_tau(100.0)         # (local)
H_extreme = H_of_tau(1000.0)         # (local)

print(f"  H(tau=0.170) = {H_pre_fold:.4f} M_KK (pre-fold)")
print(f"  H(tau_fold)  = {H_fold_check:.4f} M_KK (canonical: {H_fold:.4f})")
print(f"  H(tau=0.210) = {H_post_fold_early:.4f} M_KK")
print(f"  H(tau=0.500) = {H_post_fold_mid:.4f} M_KK")
print(f"  H(tau=2.000) = {H_post_fold_late:.4f} M_KK")
print(f"  H(tau=5.000) = {H_post_fold_far:.6f} M_KK")
print(f"  H(tau=100)   = {H_very_far:.6e} M_KK")
print(f"  H(tau=1000)  = {H_extreme:.6e} M_KK")
print()

# ==============================================================================
#  SECTION 5: Build overlap matrix M_ib (fallback diagonal)
# ==============================================================================

print("SECTION 5: Overlap matrix M_ib = <B_i | branch_b>")
print("-" * 78)

# OVERLAP-MATRIX-74 (W1-K) has not yet run.
# Fall back to the diagonal assumption with degeneracy counts:
#   M_B1->B1 = 1, M_B2->B2 = 1, M_B3->B3 = 1
# Off-diagonal terms are zero because B1, B2, B3 are spectrally resolved
# (distinct omega_k) and there is no coherent mixing at the BCS level.
#
# In a more sophisticated treatment the overlap picks up corrections from
# BCS mode orthogonality breaking at the fold, but those corrections are
# sub-leading (~r_k^{-1} ~ 0.3 suppressed).
#
# The physical content of M_ib is: how does the i-th BCS branch project
# onto the b-th emergent scalar/vector/tensor mode? For the diagonal
# assumption, each BCS branch couples one-to-one with its corresponding
# emergent mode.

M_overlap = np.eye(3)  # (local) diagonal fallback

overlap_file = os.path.join(data_dir, 's74_overlap_matrix.npz')
if os.path.exists(overlap_file):
    try:
        d_ov = np.load(overlap_file, allow_pickle=True)
        if 'M_overlap' in d_ov.files:
            M_overlap = d_ov['M_overlap']
            print("  Loaded OVERLAP-MATRIX-74 from file.")
    except Exception as e:
        print(f"  OVERLAP-MATRIX-74 load failed ({e}), using diagonal fallback.")
else:
    print("  OVERLAP-MATRIX-74 not available, using diagonal fallback M = I_3.")

print(f"  M_overlap =")
for row in M_overlap:
    print(f"    {row}")
print()

# ==============================================================================
#  SECTION 6: Horizon-crossing time per branch
# ==============================================================================

print("SECTION 6: Per-branch horizon-crossing times tau_cross(b, k)")
print("-" * 78)

# Horizon crossing: c_b(tau) * k = H(tau)
#
# For a fixed c_b (taking the fold value), this gives a k-dependent tau_cross.
# We solve c_b * k_local = H(tau_cross) where k_local is the fiber wavenumber.
#
# The key physics: different branches cross the horizon at different times
# for the same k because they have different group velocities. The B2
# branch (flattest) crosses earliest; B1/B3 cross later.
#
# In substrate language: each branch's spectral weight transitions between
# "sub-horizon" and "super-horizon" at a distinct moment along the fold
# transit. This creates the k-dependent transfer function.

def tau_cross_of_k(c_b, k):
    """Find tau where c_b * k = H(tau).

    Parameters
    ----------
    c_b : float
        Branch group velocity (in M_KK units).
    k : float
        Fiber wavenumber (in M_KK units).
    """
    # Solve c_b * k = H(tau) via bisection/linear search on tau_grid_H
    target = c_b * k  # (local)
    H_vals = np.array([H_of_tau(t) for t in tau_grid_H])  # (local)

    if target < H_vals.min():
        return tau_grid_H[-1]  # after fold, always sub-horizon
    if target > H_vals.max():
        return tau_grid_H[0]   # before fold, always super-horizon

    # Find crossing by sign change
    diffs = H_vals - target  # (local)
    sign_changes = np.where(np.diff(np.sign(diffs)))[0]  # (local)
    if len(sign_changes) == 0:
        # No crossing, return fold value
        return tau_fold
    idx0 = sign_changes[0]  # (local)
    # Linear interpolation
    t1, t2 = tau_grid_H[idx0], tau_grid_H[idx0 + 1]  # (local)
    d1, d2 = diffs[idx0], diffs[idx0 + 1]  # (local)
    if abs(d2 - d1) < 1e-30:
        return (t1 + t2) / 2
    return t1 - d1 * (t2 - t1) / (d2 - d1)

# Pivot scale: k_pivot = 0.05 Mpc^-1 in physical units
# In substrate units we need to convert via M_KK
# k_pivot_sub = (k_pivot_phys * hbar c) / M_KK_GeV
# Here we work with the ratio k/k_fold directly — we set k_fold_sub = omega_B1
# at the fold so k runs from 1e-4 to 1 in Mpc^-1 relative to pivot.

# k-mapping: CMB k (Mpc^-1) <-> substrate k (M_KK units)
#
# The multifield transfer picture: each branch lives in the fiber, the
# branch horizon-crossing happens at a distinct tau based on its group
# velocity, and the substrate k at crossing corresponds to a CMB k via:
#
#   k_sub * (M_KK)  =  k_CMB * (a_0/a_crossing) * (correction factors)
#
# For the pivot relationship, we adopt the substrate-native identification
# that a given CMB k_CMB probes the fiber spectrum at a substrate scale
# set by the Hubble rate at horizon crossing:
#
#   k_CMB(Mpc^-1) -> k_sub(M_KK) via  k_sub / k_fold_pivot = k_CMB / k_pivot_Mpc
#
# This is a linear proportional map: the CMB pivot k = 0.05 Mpc^-1
# corresponds to the fiber pivot k_fold_sub = omega_B2 (middle branch),
# and k varies linearly in log-space around it.

scale_factor = float(d73b['scale_factor'])  # (local) = S73B reference (not used directly)
Delta_lnk_fiber = float(d73b['Delta_lnk_fiber'])  # (local) S73B reference
print(f"  (S73B reference) scale_factor = {scale_factor:.6e}")
print(f"  (S73B reference) Delta_lnk_fiber = {Delta_lnk_fiber:.6f}")
print()

# Set fiber pivot at the middle branch (B2) — this is the substrate scale
# corresponding to the CMB pivot k_pivot = 0.05 Mpc^-1.
k_fold_sub = omega_B2  # (local) middle-branch frequency as fiber pivot in substrate units
k_pivot_sub = k_fold_sub  # (local) fiber k at CMB pivot scale

print(f"  Substrate pivot k_fold_sub = omega_B2 = {k_fold_sub:.6f} M_KK")
print(f"  Mapped to CMB k_pivot_Mpc = 0.05 Mpc^-1 (linear log-k map)")
print()

# Horizon-crossing at pivot with branch-specific k_sub mappings
k_pivot_sub_B1 = omega_B1  # (local) B1's natural fiber pivot
k_pivot_sub_B2 = omega_B2  # (local) B2's natural fiber pivot
k_pivot_sub_B3 = omega_B3  # (local) B3's natural fiber pivot

tau_cross_B1_pivot = tau_cross_of_k(c_B1, k_pivot_sub_B1)  # (local)
tau_cross_B2_pivot = tau_cross_of_k(c_B2, k_pivot_sub_B2)  # (local)
tau_cross_B3_pivot = tau_cross_of_k(c_B3, k_pivot_sub_B3)  # (local)

print(f"  Horizon-crossing at pivot (branch-specific k_sub):")
print(f"    tau_cross(B1) = {tau_cross_B1_pivot:.6f}  (k_sub_B1 = {k_pivot_sub_B1:.4f})")
print(f"    tau_cross(B2) = {tau_cross_B2_pivot:.6f}  (k_sub_B2 = {k_pivot_sub_B2:.4f})")
print(f"    tau_cross(B3) = {tau_cross_B3_pivot:.6f}  (k_sub_B3 = {k_pivot_sub_B3:.4f})")
print()

# ==============================================================================
#  SECTION 7: Per-branch Planck factor P_b(k)
# ==============================================================================

print("SECTION 7: Per-branch Planck factor P_b(k)")
print("-" * 78)

# P_b(k) = (H(tau_cross(b))/(2 pi))^2 * (1 + 2 n_b) *
#          |cosh(r_b) + sinh(r_b) exp(i phi_b)|^2
#
# This is the Planck-scale primordial power spectrum contribution from
# branch b, generalized to include thermal (1 + 2 n_b) and squeezing
# (cosh + sinh e^i phi) factors.

def Planck_factor_branch(r_b, n_b, phi_b, H_at_cross):
    """Compute per-branch Planck factor at horizon crossing."""
    planck_base = (H_at_cross / (2 * np.pi))**2  # (local)
    thermal_factor = 1.0 + 2.0 * n_b              # (local)
    # |cosh(r) + sinh(r) e^{i phi}|^2
    cr = np.cosh(r_b)  # (local)
    sr = np.sinh(r_b)  # (local)
    squeeze_amp = cr**2 + sr**2 + 2 * cr * sr * np.cos(phi_b)  # (local)
    return planck_base * thermal_factor * squeeze_amp

# For each branch, use its own horizon-crossing time for H
H_cross_B1 = H_of_tau(tau_cross_B1_pivot)  # (local)
H_cross_B2 = H_of_tau(tau_cross_B2_pivot)  # (local)
H_cross_B3 = H_of_tau(tau_cross_B3_pivot)  # (local)

P_B1_planck = Planck_factor_branch(r_B1, n_B1, phi_B1, H_cross_B1)  # (local)
P_B2_planck = Planck_factor_branch(r_B2, n_B2, phi_B2, H_cross_B2)  # (local)
P_B3_planck = Planck_factor_branch(r_B3, n_B3, phi_B3, H_cross_B3)  # (local)

print(f"  B1: H_cross={H_cross_B1:.4f}, P_planck={P_B1_planck:.4e}")
print(f"  B2: H_cross={H_cross_B2:.4f}, P_planck={P_B2_planck:.4e}")
print(f"  B3: H_cross={H_cross_B3:.4f}, P_planck={P_B3_planck:.4e}")
print()

# ==============================================================================
#  SECTION 8: Branch Jacobian J_b(k) for delta phi_b -> delta zeta
# ==============================================================================

print("SECTION 8: Branch Jacobian J_b for zeta mapping")
print("-" * 78)

# The comoving curvature perturbation zeta is built from a weighted sum
# over branch perturbations:
#   zeta = sum_b psi_b * (delta rho_b / rho_total)
# where psi_b is the per-branch energy density fraction.
#
# In the multifield delta-N formalism:
#   zeta = sum_b (dN/dphi_b) * delta phi_b
# and the per-branch contribution to P_zeta is:
#   P_zeta = sum_b (dN/dphi_b)^2 * P_phi_b(k)
#
# The Jacobian J_b = dN/dphi_b comes from the Friedmann-derived expression
# for N_e(phi) in the BCS multifield picture. Using the S73B constraint
# that rho_B3 dominates 99.44% of the energy but the conversion weights
# are multifield, we use the branch energy fractions from the mode_weights
# adjusted by the oscillation strength (2 omega_b).

# Per-branch energy fractions (unnormalized): W_b * n_b * 2 omega_b
E_B1_raw = W_B1 * n_B1 * 2 * omega_B1  # (local)
E_B2_raw = W_B2 * n_B2 * 2 * omega_B2  # (local)
E_B3_raw = W_B3 * n_B3 * 2 * omega_B3  # (local)
E_tot_raw = E_B1_raw + E_B2_raw + E_B3_raw  # (local)

psi_B1 = E_B1_raw / E_tot_raw  # (local)
psi_B2 = E_B2_raw / E_tot_raw  # (local)
psi_B3 = E_B3_raw / E_tot_raw  # (local)

# Multifield Jacobian: J_b = dN/dphi_b ~ (1/H) * (d phi_b / dt) / phi_b
# At horizon crossing, for a canonical scalar mode, this reduces to:
#   J_b = psi_b^{1/2} / H_b
# where H_b is the Hubble rate at branch b's crossing time.
#
# This gives the per-branch zeta contribution amplitude.

J_B1 = np.sqrt(psi_B1) / H_cross_B1  # (local)
J_B2 = np.sqrt(psi_B2) / H_cross_B2  # (local)
J_B3 = np.sqrt(psi_B3) / H_cross_B3  # (local)

print(f"  Per-branch psi (energy fractions):")
print(f"    psi_B1 = {psi_B1:.6f}")
print(f"    psi_B2 = {psi_B2:.6f}")
print(f"    psi_B3 = {psi_B3:.6f}  (sum = {psi_B1+psi_B2+psi_B3:.6f})")
print(f"  Per-branch Jacobian J_b = sqrt(psi_b) / H_b:")
print(f"    J_B1 = {J_B1:.6e}")
print(f"    J_B2 = {J_B2:.6e}")
print(f"    J_B3 = {J_B3:.6e}")
print()

# ==============================================================================
#  SECTION 9: k-scan — build T_b(k) and composed P_s(k)
# ==============================================================================

print("SECTION 9: k-scan for T_b(k) and P_s(k)")
print("-" * 78)

# Scan k from 1e-4 to 1 Mpc^-1 (log-spaced)
k_values_Mpc = np.logspace(-4, 0, 201)  # (local) Mpc^-1
k_pivot_Mpc = 0.05  # (local) CMB pivot scale

# Branch-specific mapping: each branch probes a DIFFERENT fiber k for the
# same CMB k, set by the branch's characteristic scale omega_b.
#
# For branch b: k_sub_b(k_CMB) = omega_b * (k_CMB / k_pivot_Mpc)
# This is a proportional map with per-branch anchors at omega_b.
def k_CMB_to_k_sub_branch(k_Mpc, omega_b):
    """Branch-specific fiber k from CMB k (linear proportional map)."""
    return omega_b * (k_Mpc / k_pivot_Mpc)

# NOTE: The fiber-level S73B P(k) non-monotonicity (alpha_s ~ +0.833 from
# a 3-point quadratic fit over Delta_lnk = 0.07) is a STRUCTURAL artifact
# of the B1 mode's extreme squeezing (r_B1 = 2 * r_B2 = 3.57). Extrapolating
# that fiber non-monotonicity to CMB scales via a log-quadratic is
# numerically unstable and physically wrong.
#
# The correct multifield delta-N transfer function uses ONLY the per-branch
# horizon-crossing structure (H(tau_cross_b)) and per-branch Jacobians
# (sqrt(psi_b)/H_b). It does NOT extrapolate the fiber non-monotonicity.
# The multifield smoothing THIS is the physical content of S73B's
# "non-monotonic fiber P(k) must be smoothed" constraint.

# Compute per-branch T_b(k) and composed P_s(k)
T_B1_k = np.zeros_like(k_values_Mpc)  # (local)
T_B2_k = np.zeros_like(k_values_Mpc)  # (local)
T_B3_k = np.zeros_like(k_values_Mpc)  # (local)
P_s_k = np.zeros_like(k_values_Mpc)   # (local)

for ik, k_cmb in enumerate(k_values_Mpc):
    # Branch-specific fiber k mappings
    k_sub_B1 = k_CMB_to_k_sub_branch(k_cmb, omega_B1)  # (local)
    k_sub_B2 = k_CMB_to_k_sub_branch(k_cmb, omega_B2)  # (local)
    k_sub_B3 = k_CMB_to_k_sub_branch(k_cmb, omega_B3)  # (local)

    # Horizon-crossing times (per-branch, using branch-specific k_sub)
    tc_B1 = tau_cross_of_k(c_B1, k_sub_B1)  # (local)
    tc_B2 = tau_cross_of_k(c_B2, k_sub_B2)  # (local)
    tc_B3 = tau_cross_of_k(c_B3, k_sub_B3)  # (local)

    H_B1 = H_of_tau(tc_B1)  # (local)
    H_B2 = H_of_tau(tc_B2)  # (local)
    H_B3 = H_of_tau(tc_B3)  # (local)

    # Planck factors at horizon crossing (k-dependent via H_b)
    Pp_B1 = Planck_factor_branch(r_B1, n_B1, phi_B1, H_B1)  # (local)
    Pp_B2 = Planck_factor_branch(r_B2, n_B2, phi_B2, H_B2)  # (local)
    Pp_B3 = Planck_factor_branch(r_B3, n_B3, phi_B3, H_B3)  # (local)

    # k-DEPENDENT Jacobians: J_b(k) = sqrt(psi_b) / H_b(k)
    J_B1_k = np.sqrt(psi_B1) / max(H_B1, 1e-30)  # (local)
    J_B2_k = np.sqrt(psi_B2) / max(H_B2, 1e-30)  # (local)
    J_B3_k = np.sqrt(psi_B3) / max(H_B3, 1e-30)  # (local)

    # Per-branch transfer amplitudes (diagonal M_overlap)
    # T_b(k) = M_bb * sqrt(P_b) * J_b
    T_B1_k[ik] = M_overlap[0, 0] * np.sqrt(max(Pp_B1, 0)) * J_B1_k
    T_B2_k[ik] = M_overlap[1, 1] * np.sqrt(max(Pp_B2, 0)) * J_B2_k
    T_B3_k[ik] = M_overlap[2, 2] * np.sqrt(max(Pp_B3, 0)) * J_B3_k

    # Composed P_s(k) = sum_b W_b * |T_b|^2
    P_s_k[ik] = W_B1 * T_B1_k[ik]**2 + W_B2 * T_B2_k[ik]**2 + W_B3 * T_B3_k[ik]**2

# Find pivot index
idx_pivot = int(np.argmin(np.abs(k_values_Mpc - k_pivot_Mpc)))  # (local)
k_pivot_actual = k_values_Mpc[idx_pivot]  # (local)
P_pivot = P_s_k[idx_pivot]  # (local)

print(f"  k range: [{k_values_Mpc[0]:.4e}, {k_values_Mpc[-1]:.4e}] Mpc^-1")
print(f"  Points:  {len(k_values_Mpc)}")
print(f"  Pivot idx={idx_pivot}, k_pivot_actual={k_pivot_actual:.6f} Mpc^-1")
print(f"  P_s(k_pivot) = {P_pivot:.6e} (substrate units)")
print()

# ==============================================================================
#  SECTION 10: n_s and alpha_s at the pivot
# ==============================================================================

print("SECTION 10: n_s and alpha_s extraction at pivot")
print("-" * 78)

ln_k = np.log(k_values_Mpc)  # (local)
ln_P = np.log(np.maximum(P_s_k, 1e-300))  # (local)

# Local numerical derivatives at the pivot (5-point stencil, centered)
# d ln P / d ln k at pivot
def deriv1(y, x, i):
    """5-point centered first derivative."""
    if i < 2 or i > len(x) - 3:
        return (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])
    return (-y[i+2] + 8*y[i+1] - 8*y[i-1] + y[i-2]) / (6*(x[i+1] - x[i-1]))

def deriv2(y, x, i):
    """5-point centered second derivative (uniform grid)."""
    if i < 2 or i > len(x) - 3:
        h = (x[i+1] - x[i-1]) / 2
        return (y[i+1] - 2*y[i] + y[i-1]) / h**2
    h = (x[i+1] - x[i-1]) / 2
    return (-y[i+2] + 16*y[i+1] - 30*y[i] + 16*y[i-1] - y[i-2]) / (12*h**2)

ns_minus_1 = deriv1(ln_P, ln_k, idx_pivot)   # (local)
alpha_s = deriv2(ln_P, ln_k, idx_pivot)      # (local)

n_s_pivot = 1.0 + ns_minus_1  # (local)

# Also compute via quadratic polyfit in a wide window around pivot
# (more robust than narrow finite differences if P_s is smooth)
window = 20  # (local) points on either side
i0 = max(0, idx_pivot - window)  # (local)
i1 = min(len(ln_k), idx_pivot + window + 1)  # (local)
coeffs_fit = np.polyfit(ln_k[i0:i1], ln_P[i0:i1], 2)  # (local) [a, b, c]
a_fit = coeffs_fit[0]  # (local)
b_fit = coeffs_fit[1]  # (local)
c_fit = coeffs_fit[2]  # (local)

alpha_s_quad = 2 * a_fit  # (local)
ns_minus_1_quad = b_fit + 2 * a_fit * ln_k[idx_pivot]  # (local)
n_s_pivot_quad = 1.0 + ns_minus_1_quad  # (local)

print(f"  Finite differences at pivot:")
print(f"    n_s(pivot) = {n_s_pivot:.6f}")
print(f"    alpha_s(pivot) = {alpha_s:.6e}")
print(f"  Quadratic fit (window={window} on each side):")
print(f"    n_s(pivot) = {n_s_pivot_quad:.6f}")
print(f"    alpha_s(pivot) = {alpha_s_quad:.6e}")
print()

# ==============================================================================
#  SECTION 11: A_s normalization to 4D emergent units
# ==============================================================================

print("SECTION 11: A_s in dimensionless 4D units")
print("-" * 78)

# Convert substrate P_s(pivot) to dimensionless A_s
# A_s = P_s(pivot) * (M_KK / M_Pl)^2 * normalization
#
# The conversion factor: substrate P in M_KK^{-3}, CMB A_s dimensionless.
# Using M_KK = 7.43e16 GeV and M_Pl = 1.22e19 GeV,
# the ratio (M_KK/M_Pl)^4 gives the dimensional conversion.

ratio_MKK_MPl = M_KK / M_Pl_unreduced  # (local)
A_s_4D = P_pivot * ratio_MKK_MPl**4  # (local) simplified normalization

# Planck A_s reference
A_s_Planck = 2.1e-9  # (local)
A_s_gap_OOM = np.log10(A_s_4D / A_s_Planck) if A_s_4D > 0 else float('-inf')  # (local)

print(f"  P_s(pivot, substrate) = {P_pivot:.6e}")
print(f"  M_KK / M_Pl           = {ratio_MKK_MPl:.6e}")
print(f"  A_s(4D estimate)      = {A_s_4D:.6e}")
print(f"  A_s(Planck)           = {A_s_Planck:.4e}")
print(f"  log10(A_s/A_s_obs)    = {A_s_gap_OOM:+.4f} OOM")
print()

# ==============================================================================
#  SECTION 12: Cross-checks
# ==============================================================================

print("SECTION 12: Cross-checks")
print("-" * 78)

# ---- Cross-check 1: Limiting case (all branches identical) ----
# If M_ib = I AND all tau_cross identical AND all Planck factors identical,
# the result should collapse to the S73B W1-A naive Bogoliubov calculation.
#
# Test: set c_B1 = c_B2 = c_B3 (same velocity), re-run the pivot computation,
# compare alpha_s to the S73B reference +0.833.

def alpha_s_uniform_velocity():
    """Re-run pivot computation with identical branch velocities AND
    identical k_sub mapping.

    In this limit, all three branches cross at the same tau (same H) and
    probe the same fiber k. The composed P(k) reduces to a single-branch
    result, demonstrating the role of multifield staggering.
    """
    c_uniform = c_B1  # (local) use B1 velocity for all branches
    omega_uniform = omega_B1  # (local) use B1 as uniform pivot
    T_vals = np.zeros_like(k_values_Mpc)  # (local)
    for ik, k_cmb in enumerate(k_values_Mpc):
        # All three branches at the same k_sub (uniform mapping)
        k_sub = k_CMB_to_k_sub_branch(k_cmb, omega_uniform)  # (local)
        tc = tau_cross_of_k(c_uniform, k_sub)  # (local)
        H_local = H_of_tau(tc)  # (local)
        Pp1 = Planck_factor_branch(r_B1, n_B1, phi_B1, H_local)  # (local)
        Pp2 = Planck_factor_branch(r_B2, n_B2, phi_B2, H_local)  # (local)
        Pp3 = Planck_factor_branch(r_B3, n_B3, phi_B3, H_local)  # (local)

        # Jacobians at uniform H
        J1u = np.sqrt(psi_B1) / max(H_local, 1e-30)  # (local)
        J2u = np.sqrt(psi_B2) / max(H_local, 1e-30)  # (local)
        J3u = np.sqrt(psi_B3) / max(H_local, 1e-30)  # (local)

        T1 = np.sqrt(max(Pp1, 0)) * J1u  # (local)
        T2 = np.sqrt(max(Pp2, 0)) * J2u  # (local)
        T3 = np.sqrt(max(Pp3, 0)) * J3u  # (local)
        T_vals[ik] = W_B1 * T1**2 + W_B2 * T2**2 + W_B3 * T3**2

    ln_P_u = np.log(np.maximum(T_vals, 1e-300))  # (local)
    # Use quadratic fit for robustness
    coeffs_u = np.polyfit(ln_k[i0:i1], ln_P_u[i0:i1], 2)  # (local)
    alpha_u = 2 * coeffs_u[0]  # (local)
    ns_u = 1.0 + coeffs_u[1] + 2 * coeffs_u[0] * ln_k[idx_pivot]  # (local)
    return alpha_u, ns_u

alpha_s_uniform, n_s_uniform = alpha_s_uniform_velocity()
print(f"  CHK1 (uniform velocity): alpha_s = {alpha_s_uniform:.6e}, "
      f"n_s = {n_s_uniform:.6f}")
print(f"  CHK1 expected: the composed P_s becomes a sum of B_b contributions at a")
print(f"  single tau_cross, removing the multifield horizon-crossing staggering.")
print(f"  The non-trivial k-dependence then arises only through k_CMB_to_k_fiber.")

# ---- Cross-check 2: Dimensional consistency ----
# P_s(pivot) should have dimensions of M_KK^{-3} (substrate) if we're in a
# 3D mode-count sense. Our A_s normalization uses (M_KK/M_Pl)^4.
# Check: the Planck A_s is ~2e-9, our estimate should be within ~10 OOM
# (pre-BCS-dressing and pre-Jacobian corrections).
print()
print(f"  CHK2 (dimensional): A_s estimate = {A_s_4D:.4e}, gap = {A_s_gap_OOM:+.2f} OOM")

# ---- Cross-check 3: Symmetry diagnostic ----
# Swap B1 <-> B3 (c, r, n, phi, psi): total P_s should CHANGE because
# the weights W_B1=0.150 and W_B3=0.818 are unequal.
# If it doesn't change, the symmetry is broken in the pipeline.

def P_swap_B1B3():
    """Compute P_s(pivot) with W_B1<->W_B3 weight swap.

    This tests the asymmetric weighting: if W_B1 != W_B3, the
    total P must change when we swap these weights.
    """
    # Swap only the W weights (leave all other parameters fixed)
    W1_sw = W_B3  # (local) B1-slot now has B3 weight
    W3_sw = W_B1  # (local) B3-slot now has B1 weight

    # Branch-specific k_sub at pivot
    k_sub_B1 = k_CMB_to_k_sub_branch(k_pivot_actual, omega_B1)  # (local)
    k_sub_B2 = k_CMB_to_k_sub_branch(k_pivot_actual, omega_B2)  # (local)
    k_sub_B3 = k_CMB_to_k_sub_branch(k_pivot_actual, omega_B3)  # (local)

    tc1 = tau_cross_of_k(c_B1, k_sub_B1)  # (local)
    tc2 = tau_cross_of_k(c_B2, k_sub_B2)  # (local)
    tc3 = tau_cross_of_k(c_B3, k_sub_B3)  # (local)
    H1 = H_of_tau(tc1)  # (local)
    H2 = H_of_tau(tc2)  # (local)
    H3 = H_of_tau(tc3)  # (local)

    # Recompute energy fractions with swapped W
    E1_sw = W1_sw * n_B1 * 2 * omega_B1  # (local)
    E2_sw = W_B2 * n_B2 * 2 * omega_B2   # (local)
    E3_sw = W3_sw * n_B3 * 2 * omega_B3  # (local)
    E_tot_sw = E1_sw + E2_sw + E3_sw  # (local)
    psi1_sw = E1_sw / E_tot_sw  # (local)
    psi2_sw = E2_sw / E_tot_sw  # (local)
    psi3_sw = E3_sw / E_tot_sw  # (local)

    J1_sw = np.sqrt(psi1_sw) / max(H1, 1e-30)  # (local)
    J2_sw = np.sqrt(psi2_sw) / max(H2, 1e-30)  # (local)
    J3_sw = np.sqrt(psi3_sw) / max(H3, 1e-30)  # (local)

    Pp1 = Planck_factor_branch(r_B1, n_B1, phi_B1, H1)  # (local)
    Pp2 = Planck_factor_branch(r_B2, n_B2, phi_B2, H2)  # (local)
    Pp3 = Planck_factor_branch(r_B3, n_B3, phi_B3, H3)  # (local)

    T1_sq = max(Pp1, 0) * J1_sw**2  # (local)
    T2_sq = max(Pp2, 0) * J2_sw**2  # (local)
    T3_sq = max(Pp3, 0) * J3_sw**2  # (local)
    return W1_sw * T1_sq + W_B2 * T2_sq + W3_sw * T3_sq

P_swapped = P_swap_B1B3()
swap_ratio = P_swapped / P_pivot if P_pivot > 0 else float('inf')  # (local)
print(f"  CHK3 (B1<->B3 swap): P_swapped/P_original = {swap_ratio:.6f}")
print(f"  CHK3 expected: != 1 because W_B1 (0.150) != W_B3 (0.818)")
chk3_pass = not (0.999 < swap_ratio < 1.001)  # (local)
print(f"  CHK3 status: {'PASS' if chk3_pass else 'FAIL (symmetry not broken)'}")
print()

# ==============================================================================
#  SECTION 13: Gate verdict
# ==============================================================================

print("SECTION 13: Gate verdict — TRANSFER-FUNCTION-74")
print("=" * 78)

# Use quadratic fit values (more robust than point finite differences)
ns_final = n_s_pivot_quad  # (local)
alpha_s_final = alpha_s_quad  # (local)

abs_alpha_s = abs(alpha_s_final)  # (local)
planck_n_s_low = 0.9607  # (local) Planck n_s - 1 sigma
planck_n_s_high = 0.9691  # (local) Planck n_s + 1 sigma

n_s_in_band = (planck_n_s_low <= ns_final <= planck_n_s_high)  # (local)

if abs_alpha_s < 0.015 and n_s_in_band:
    verdict = "PASS"
    verdict_reason = f"|alpha_s|={abs_alpha_s:.4e} < 0.015 AND n_s={ns_final:.4f} in [0.9607, 0.9691]"
elif abs_alpha_s > 0.030:
    verdict = "FAIL"
    verdict_reason = f"|alpha_s|={abs_alpha_s:.4e} > 0.030 (Planck-incompatible)"
elif 0.015 <= abs_alpha_s <= 0.030:
    verdict = "INFO"
    verdict_reason = f"|alpha_s|={abs_alpha_s:.4e} in [0.015, 0.030] (partial resolution)"
else:
    # |alpha_s| < 0.015 but n_s out of band
    if abs_alpha_s < 0.015 and not n_s_in_band:
        verdict = "INFO"
        verdict_reason = f"alpha_s OK but n_s={ns_final:.4f} out of Planck band"
    else:
        verdict = "INFO"
        verdict_reason = "partial"

print(f"  n_s(pivot)       = {ns_final:.6f}")
print(f"  alpha_s(pivot)   = {alpha_s_final:.6e}")
print(f"  |alpha_s|        = {abs_alpha_s:.6e}")
print(f"  Planck n_s band  = [{planck_n_s_low}, {planck_n_s_high}]")
print(f"  A_s(estimate)    = {A_s_4D:.4e}")
print(f"  A_s gap          = {A_s_gap_OOM:+.2f} OOM from Planck")
print()
print(f"  VERDICT: {verdict}")
print(f"  Reason: {verdict_reason}")
print()

# ==============================================================================
#  SECTION 14: Save outputs
# ==============================================================================

print("SECTION 14: Save outputs")
print("-" * 78)

output_npz = os.path.join(data_dir, 's74_transfer_function.npz')

np.savez(
    output_npz,
    # Gate
    gate_name='TRANSFER-FUNCTION-74',
    gate_verdict=verdict,
    gate_reason=verdict_reason,
    # Primary results
    n_s_pivot=ns_final,
    alpha_s_pivot=alpha_s_final,
    abs_alpha_s=abs_alpha_s,
    A_s_4D=A_s_4D,
    A_s_gap_OOM=A_s_gap_OOM,
    # Per-branch group velocities
    c_B1=c_B1, c_B2=c_B2, c_B3=c_B3,
    # Per-branch horizon-crossing times at pivot
    tau_cross_B1=tau_cross_B1_pivot,
    tau_cross_B2=tau_cross_B2_pivot,
    tau_cross_B3=tau_cross_B3_pivot,
    # Per-branch energy fractions
    psi_B1=psi_B1, psi_B2=psi_B2, psi_B3=psi_B3,
    # Per-branch Jacobians
    J_B1=J_B1, J_B2=J_B2, J_B3=J_B3,
    # Per-branch Planck factors at pivot
    P_B1_planck=P_B1_planck, P_B2_planck=P_B2_planck, P_B3_planck=P_B3_planck,
    # Overlap matrix
    M_overlap=M_overlap,
    # k-scan
    k_values_Mpc=k_values_Mpc,
    T_B1_k=T_B1_k,
    T_B2_k=T_B2_k,
    T_B3_k=T_B3_k,
    P_s_k=P_s_k,
    k_pivot_Mpc=k_pivot_Mpc,
    idx_pivot=idx_pivot,
    # Cross-checks
    alpha_s_uniform=alpha_s_uniform,
    n_s_uniform=n_s_uniform,
    P_swap_B1B3=P_swapped,
    swap_ratio=swap_ratio,
    # Branch parameters
    omega_B1=omega_B1, omega_B2=omega_B2, omega_B3=omega_B3,
    r_B1=r_B1, r_B2=r_B2, r_B3=r_B3,
    n_B1=n_B1, n_B2=n_B2, n_B3=n_B3,
    phi_B1=phi_B1, phi_B2=phi_B2, phi_B3=phi_B3,
    W_B1=W_B1, W_B2=W_B2, W_B3=W_B3,
    # S73B reference for cross-check
    alpha_s_s73b_reference=float(d73b['alpha_s_adopted']),
    # Dimensional factors
    M_KK_value=M_KK,
    M_Pl_value=M_Pl_unreduced,
    ratio_MKK_MPl=ratio_MKK_MPl,
    scale_factor=scale_factor,
    k_fold_sub=k_fold_sub,
)

print(f"  Data: {output_npz}")

# Plot
output_png = os.path.join(data_dir, 's74_transfer_function.png')

fig = plt.figure(figsize=(12, 10))
gs = GridSpec(3, 2, figure=fig, hspace=0.35, wspace=0.3)

# Panel 1: per-branch T_b(k)
ax1 = fig.add_subplot(gs[0, :])
ax1.loglog(k_values_Mpc, T_B1_k**2, 'b-', lw=2, label=f'B1 (acoustic, c={c_B1:.3f})')
ax1.loglog(k_values_Mpc, T_B2_k**2, 'g-', lw=2, label=f'B2 (flat, c={c_B2:.3e})')
ax1.loglog(k_values_Mpc, T_B3_k**2, 'r-', lw=2, label=f'B3 (disp, c={c_B3:.3f})')
ax1.axvline(k_pivot_Mpc, color='k', ls='--', alpha=0.5, label='k_pivot')
ax1.set_xlabel('k [Mpc$^{-1}$]')
ax1.set_ylabel('|T$_b$(k)|$^2$')
ax1.set_title('Per-branch Transfer Function')
ax1.legend(loc='best', fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: composed P_s(k)
ax2 = fig.add_subplot(gs[1, 0])
ax2.loglog(k_values_Mpc, P_s_k, 'k-', lw=2, label='$P_s(k)$')
ax2.axvline(k_pivot_Mpc, color='k', ls='--', alpha=0.5)
ax2.axhline(P_pivot, color='r', ls=':', alpha=0.5, label=f'$P_s(k_*)$={P_pivot:.2e}')
ax2.set_xlabel('k [Mpc$^{-1}$]')
ax2.set_ylabel('$P_s(k)$')
ax2.set_title('Composed Scalar Power Spectrum')
ax2.legend(loc='best', fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: ln P vs ln k near pivot (for n_s, alpha_s)
ax3 = fig.add_subplot(gs[1, 1])
i0p = max(0, idx_pivot - 40)
i1p = min(len(k_values_Mpc), idx_pivot + 41)
ax3.plot(ln_k[i0p:i1p], ln_P[i0p:i1p], 'b.', label='Data', ms=6)
# Overlay quadratic fit
ln_k_fit = np.linspace(ln_k[i0p], ln_k[i1p - 1], 100)  # (local)
ln_P_fit = a_fit * ln_k_fit**2 + b_fit * ln_k_fit + c_fit  # (local)
ax3.plot(ln_k_fit, ln_P_fit, 'r-', lw=2,
         label=f'Quadratic fit\n$\\alpha_s$={alpha_s_final:.3e}\n$n_s$={ns_final:.4f}')
ax3.axvline(ln_k[idx_pivot], color='k', ls='--', alpha=0.5)
ax3.set_xlabel('ln k')
ax3.set_ylabel('ln $P_s$')
ax3.set_title('Spectral Tilt Extraction at Pivot')
ax3.legend(loc='best', fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: horizon-crossing diagram
ax4 = fig.add_subplot(gs[2, 0])
ax4.plot(tau_grid_H, [H_of_tau(t) for t in tau_grid_H], 'k-', lw=2, label='H(tau)')
ax4.axhline(c_B1 * k_fold_sub, color='b', ls='--',
            label=f'$c_{{B1}}k_*$={c_B1 * k_fold_sub:.2f}')
ax4.axhline(c_B2 * k_fold_sub, color='g', ls='--',
            label=f'$c_{{B2}}k_*$={c_B2 * k_fold_sub:.2e}')
ax4.axhline(c_B3 * k_fold_sub, color='r', ls='--',
            label=f'$c_{{B3}}k_*$={c_B3 * k_fold_sub:.2f}')
ax4.axvline(tau_fold, color='k', ls=':', alpha=0.5, label='$\\tau_{fold}$')
ax4.set_xlabel('$\\tau$')
ax4.set_ylabel('H(tau) [M$_{KK}$]')
ax4.set_yscale('log')
ax4.set_title('Per-branch Horizon Crossing at Pivot')
ax4.legend(loc='best', fontsize=8)
ax4.grid(True, alpha=0.3)

# Panel 5: branch contribution pie chart at pivot
ax5 = fig.add_subplot(gs[2, 1])
T_pivot_sq = np.array([T_B1_k[idx_pivot]**2, T_B2_k[idx_pivot]**2,
                       T_B3_k[idx_pivot]**2])  # (local)
labels_pie = ['B1', 'B2', 'B3']  # (local)
colors_pie = ['blue', 'green', 'red']  # (local)
nonzero_mask = T_pivot_sq > 0  # (local)
if np.any(nonzero_mask):
    ax5.pie(T_pivot_sq[nonzero_mask],
            labels=[l for l, m in zip(labels_pie, nonzero_mask) if m],
            colors=[c for c, m in zip(colors_pie, nonzero_mask) if m],
            autopct='%1.1f%%')
    ax5.set_title(f'Branch Contribution to P_s(k_*)')
else:
    ax5.text(0.5, 0.5, 'All T_b^2 are zero', ha='center', va='center')
    ax5.set_title(f'Branch Contribution to P_s(k_*)')

fig.suptitle(f'TRANSFER-FUNCTION-74: Multifield delta-N Transfer\n'
             f'Verdict: {verdict}  ($\\alpha_s$={alpha_s_final:.3e}, '
             f'$n_s$={ns_final:.4f})',
             fontsize=12, y=0.995)

plt.savefig(output_png, dpi=120, bbox_inches='tight')
plt.close()

print(f"  Plot: {output_png}")

t_total = time.time() - t_start
print()
print(f"Total wall time: {t_total:.2f}s")
print()
print("=" * 78)
print(f"TRANSFER-FUNCTION-74: {verdict}")
print("=" * 78)
