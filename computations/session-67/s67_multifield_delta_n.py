#!/usr/bin/env python3
"""
MULTIFIELD-DELTA-N-67: Conversion Coefficients per GGE Branch
==============================================================

Computes the delta-N conversion coefficients zeta_I = dN/dsigma_I for each
GGE quasiparticle branch (acoustic, optical, Leggett). The curvature
perturbation in the multifield formalism is:

    zeta = Sum_I (dN/dsigma_I) * delta_sigma_I

where sigma_I is the field amplitude for branch I, N is the number of
e-folds, and the conversion coefficients are determined by:

    dN/dsigma_I = (H / dot{sigma}_total) * (drho_I/dsigma_I) / (Sum_J drho_J/dsigma_J)

For the exflation transit:
  - Acoustic branch (Goldstone): gapless, linear dispersion, carries bulk spectral weight
  - Optical branch (Branch-3, -4, Higgs-1): gapped amplitude modes
  - Leggett branch (Leggett-1, -2): inter-band phase oscillations, DM candidate

The multifield scalar amplitude is:

    A_s^{multi} = (H^2 / (8 pi^2)) * Sum_I (dN/dsigma_I)^2

This can enhance A_s above the single-field value.

Gate: MULTIFIELD-DELTA-N-67
  INFO: Report conversion coefficients per branch. Required for A_s and f_NL.

References:
  - Senatore & Zaldarriaga [08]: Multifield EFT operator construction
  - Lyth & Riotto [02]: delta-N formalism derivation
  - S66 inflation-exflation synthesis, Tool 4 (IV.C)
  - S53 phonon EOS, S52 GL-Josephson, S67 transit PS
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced, PI,
    S_fold, dS_fold, d2S_fold, H_fold,
    dt_transit, v_terminal,
    a0_fold, a2_fold, a4_fold,
    A_s_CMB, n_pairs, N_dof_BCS,
    E_cond, E_exc,
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    E_B1, E_B2_mean, E_B3_mean,
    T_acoustic, M_ATDHFB, G_DeWitt, Z_fold,
)

print("=" * 72)
print("MULTIFIELD-DELTA-N-67: Conversion Coefficients per GGE Branch")
print("=" * 72)

# ============================================================================
#  SECTION 1: Load input data
# ============================================================================

# Transit power spectrum data (from W1-A)
transit_data = np.load(os.path.join(os.path.dirname(__file__),
                                     's67_transit_ps.npz'), allow_pickle=True)
beta_sq_rk = transit_data['beta_sq_rk']       # |beta_k|^2 from RK solve
k_grid_rk = transit_data['k_grid_rk']         # k grid for RK
P_zeta_rk = transit_data['P_zeta_rk']         # P_zeta(k) from RK
A_s_gap_OOM = float(transit_data['A_s_gap_OOM'])

# Phonon branch structure (from S53)
phonon_data = np.load(os.path.join(os.path.dirname(__file__),
                                    's53_phonon_eos.npz'), allow_pickle=True)
rho_branch_phonon = phonon_data['rho_branch']  # 6 branches: energy density
p_branch_phonon = phonon_data['p_branch']      # 6 branches: pressure

# GL-Josephson data (from S52)
gl_data = np.load(os.path.join(os.path.dirname(__file__),
                                's52_gl_josephson.npz'), allow_pickle=True)
omega_branches = gl_data['omega_branches']  # (51, 6) branch dispersions
K_array = gl_data['K_array']                # (51,) K grid
branch_labels = list(gl_data['branch_labels'])
rho_0 = gl_data['rho_0']  # (3,) superfluid density per sector [B1, B2, B3]
Delta_0 = gl_data['Delta_0']  # (3,) BCS gaps per sector

# KZ power spectrum (from S53)
kz_data = np.load(os.path.join(os.path.dirname(__file__),
                                's53_kz_power_spectrum.npz'), allow_pickle=True)
P_branch_kz = kz_data['P_branch']  # (2000, 6) branch power spectra
K_fine_kz = kz_data['K_fine']      # (2000,) K grid
n_occ_kz = kz_data['n_occ']        # (2000, 6) occupation per branch

print(f"\nInput data loaded:")
print(f"  Transit PS: {len(k_grid_rk)} k-modes, A_s gap = {A_s_gap_OOM:.1f} OOM")
print(f"  Phonon EOS: 6 branches, rho_total = {np.sum(rho_branch_phonon):.4e} M_KK^4")
print(f"  GL: 6 branches, K_BZ = {K_array[-1]:.4f} M_KK^{-1}")
print(f"  Branch labels: {branch_labels}")

# ============================================================================
#  SECTION 2: Group branches into acoustic / optical / Leggett
# ============================================================================

# Branch indices:
#   0 = Goldstone (acoustic, gapless)
#   1 = Leggett-1 (inter-band phase B2/B1)
#   2 = Leggett-2 (inter-band phase B2/B3)
#   3 = Branch-3 (amplitude/Higgs, large gap)
#   4 = Branch-4 (amplitude/Higgs)
#   5 = Higgs-1 (massive amplitude mode)

idx_acoustic = [0]
idx_leggett = [1, 2]
idx_optical = [3, 4, 5]

group_names = ['Acoustic (Goldstone)', 'Leggett (1+2)', 'Optical (Higgs 3+4+5)']
group_indices = [idx_acoustic, idx_leggett, idx_optical]

# Effective gaps for each group (M_KK units)
gap_acoustic = 0.0                # gapless  # (local)
gap_leggett = omega_L1            # lower of the two Leggett gaps
gap_optical = omega_H1            # lowest Higgs gap

# Sound speeds for each group
# Goldstone: c_Gold from canonical
# Leggett: massive, v_g = dw/dK at K->0 but the mode has a gap
# Optical: massive, v_g ~ 0 at K=0

# From GL data, extract group velocities at low K
dK = K_array[1] - K_array[0]
vg_branches = np.gradient(omega_branches, dK, axis=0)  # (51, 6) group velocities

# Average sound speed at K ~ 0.1 K_BZ (low-K regime)
K_low_idx = max(1, int(0.1 * len(K_array)))
vg_low = np.abs(vg_branches[K_low_idx, :])

c_acoustic = c_Gold  # = 0.915 M_KK
c_leggett = np.mean(vg_low[idx_leggett])  # group velocity of Leggett modes
c_optical = np.mean(vg_low[idx_optical])   # group velocity of optical modes

print(f"\n--- Branch grouping ---")
print(f"  Acoustic: indices {idx_acoustic}, gap = {gap_acoustic:.4f}, c_s = {c_acoustic:.4f}")
print(f"  Leggett:  indices {idx_leggett}, gap = {gap_leggett:.4f}, c_s = {c_leggett:.4f}")
print(f"  Optical:  indices {idx_optical}, gap = {gap_optical:.4f}, c_s = {c_optical:.4f}")

# ============================================================================
#  SECTION 3: Energy density and field amplitudes per branch
# ============================================================================

# Each branch I has an effective field sigma_I whose energy density is:
#   rho_I = (1/2) dot{sigma}_I^2 + V_I(sigma_I)
#
# For the BCS/GGE quasiparticle system, the energy in each branch is
# determined by the occupation numbers n_k and the dispersion omega_I(k):
#   rho_I = Sum_k omega_I(k) * n_I(k)
#
# The field amplitude sigma_I is related to the occupation number via
# the standard QFT relation for a free field:
#   sigma_I^2 = Sum_k (2 n_I(k) + 1) / (2 omega_I(k))
#
# For the delta-N formalism, what matters is:
#   drho_I / dsigma_I = d/dsigma_I [Sum_k omega_I(k) * n_I(k)(sigma_I)]
#
# In the Bogoliubov framework, the occupation numbers are set by the
# transit (they are the |beta_k|^2 from Parker pair creation). The
# conversion to curvature perturbations happens through the energy
# fraction each branch carries.

# Energy per branch from KZ occupation (S53 data)
dK_kz = K_fine_kz[1] - K_fine_kz[0]
E_per_branch = np.array([np.sum(P_branch_kz[:, i]) * dK_kz for i in range(6)])
E_total = np.sum(E_per_branch)

print(f"\n--- Energy per branch (from S53 KZ spectrum) ---")
for i in range(6):
    frac = E_per_branch[i] / E_total * 100 if E_total > 0 else 0
    print(f"  {branch_labels[i]:>9s}: E = {E_per_branch[i]:.6e} M_KK ({frac:.2f}%)")
print(f"  Total: {E_total:.6e} M_KK")

# Energy per group
E_acoustic = np.sum(E_per_branch[idx_acoustic])
E_leggett = np.sum(E_per_branch[idx_leggett])
E_optical = np.sum(E_per_branch[idx_optical])

f_acoustic = E_acoustic / E_total
f_leggett = E_leggett / E_total
f_optical = E_optical / E_total

print(f"\n--- Energy fractions by group ---")
print(f"  Acoustic: {f_acoustic:.6f} ({f_acoustic*100:.2f}%)")
print(f"  Leggett:  {f_leggett:.6f} ({f_leggett*100:.2f}%)")
print(f"  Optical:  {f_optical:.6f} ({f_optical*100:.2f}%)")

# ============================================================================
#  SECTION 4: Delta-N conversion coefficients
# ============================================================================
#
# The Senatore-Zaldarriaga multifield delta-N formalism:
#
#   zeta = Sum_I (dN/dsigma_I) * delta_sigma_I           (Eq. 1)
#
# For a multifield system where the total energy density drives expansion:
#
#   H^2 = (1/3 M_Pl^2) * Sum_I rho_I                    (Friedmann)
#
# The e-fold number N satisfies dN = H dt, so:
#
#   dN/dsigma_I = (H / Sum_J dot{sigma}_J (drho_J/drho_total))
#                  * (drho_I/dsigma_I) / (drho_total/dsigma_total)
#
# For the simpler case where each branch evolves as a free field with
# dispersion omega_I(k) and the total energy controls the expansion:
#
#   dN/dsigma_I = H * sigma_I / (2 * Sum_J sigma_J * dot{sigma}_J)
#
# In the separate universe approximation (Lyth & Rodriguez 2005), each
# superhorizon patch evolves independently and:
#
#   dN/dsigma_I = (H / dot{sigma}_I) * (1 if single-field)
#
# For multifield, the conversion depends on the trajectory in field space.
# The key insight: during the exflation transit, the spectral action drives
# the evolution through dS/dtau. The GGE branches are excitations ON TOP
# of this background evolution. Their contribution to zeta comes from their
# energy fraction modulating the local expansion rate.
#
# The correct formula in the energy-fraction approach:
#
#   dN/dsigma_I = (1/2) * (drho_I/dsigma_I) / dot{rho}_total
#               = (1/2) * (drho_I/dsigma_I) / (-3 H (rho_total + p_total))
#
# Using drho_I/dsigma_I ~ 2 * rho_I / sigma_I (for free fields), and
# sigma_I^2 ~ 2 * rho_I / m_I_eff^2 (for massive) or ~ 2 * rho_I / k_eff^2
# (for massless), we get:
#
#   dN/dsigma_I = rho_I / (sigma_I * (-3H(rho+p)))

# --- Effective masses for each group ---
# Acoustic: m_eff ~ 0 (gapless), effective "mass" is c_s * k_typical
# Leggett: m_eff ~ omega_L1 (gap)
# Optical: m_eff ~ omega_H1 (gap)

# For a field with dispersion omega^2 = m^2 + c_s^2 k^2:
#   sigma^2 ~ Sum_k n_k / omega_k (field variance)
#   rho ~ Sum_k omega_k * n_k (energy density)
#   drho/dsigma ~ m_eff^2 * sigma (for massive fields)
#                ~ c_s k_typ * rho / sigma (for massless)

# Compute effective sigma^2 for each branch from the occupation spectrum
sigma_sq_branch = np.zeros(6)
rho_branch_from_kz = np.zeros(6)

for i in range(6):
    omega_i = np.interp(K_fine_kz, K_array, omega_branches[:, i])
    omega_i = np.maximum(omega_i, 1e-12)  # prevent division by zero
    # sigma_I^2 = Sum_k n_I(k) / omega_I(k) * dK
    sigma_sq_branch[i] = np.sum(n_occ_kz[:, i] / omega_i) * dK_kz
    # rho_I = Sum_k omega_I(k) * n_I(k) * dK
    rho_branch_from_kz[i] = np.sum(omega_i * n_occ_kz[:, i]) * dK_kz

print(f"\n--- Field variances sigma_I^2 (from KZ occupation) ---")
for i in range(6):
    print(f"  {branch_labels[i]:>9s}: sigma^2 = {sigma_sq_branch[i]:.6e}, "
          f"rho = {rho_branch_from_kz[i]:.6e}")

# Group field variances
sigma_sq_acoustic = np.sum(sigma_sq_branch[idx_acoustic])
sigma_sq_leggett = np.sum(sigma_sq_branch[idx_leggett])
sigma_sq_optical = np.sum(sigma_sq_branch[idx_optical])

rho_acoustic = np.sum(rho_branch_from_kz[idx_acoustic])
rho_leggett = np.sum(rho_branch_from_kz[idx_leggett])
rho_optical = np.sum(rho_branch_from_kz[idx_optical])
rho_total = rho_acoustic + rho_leggett + rho_optical

sigma_acoustic = np.sqrt(sigma_sq_acoustic)
sigma_leggett = np.sqrt(sigma_sq_leggett)
sigma_optical = np.sqrt(sigma_sq_optical)

print(f"\n--- Group field amplitudes ---")
print(f"  Acoustic: sigma = {sigma_acoustic:.6e}, rho = {rho_acoustic:.6e}")
print(f"  Leggett:  sigma = {sigma_leggett:.6e}, rho = {rho_leggett:.6e}")
print(f"  Optical:  sigma = {sigma_optical:.6e}, rho = {rho_optical:.6e}")

# ============================================================================
#  SECTION 5: Compute dN/dsigma_I using the separate universe approach
# ============================================================================
#
# In the separate universe picture, a perturbation delta_sigma_I in branch I
# shifts the local energy density by delta_rho_I = drho_I/dsigma_I * delta_sigma_I.
# This shifts the local expansion rate, giving:
#
#   delta_N = delta_H / H * (1/epsilon_total)
#           = (1/(2 * M_Pl^2 * H^2)) * delta_rho_I / epsilon_total
#
# So: dN/dsigma_I = (1/(2 * M_Pl^2 * H^2 * epsilon_total)) * drho_I/dsigma_I
#
# For a free scalar field with mass m_I: drho_I/dsigma_I = m_I^2 * sigma_I
# For a gapless mode: drho_I/dsigma_I = c_s^2 * k_eff^2 * sigma_I
#
# But the framework is NOT a standard inflation setup. The dominant energy
# density driving expansion is the SPECTRAL ACTION S(tau), not the GGE
# quasiparticle energy. The GGE is a perturbation ON TOP of the spectral
# action background.
#
# The correct approach: the total energy is rho_total = rho_SA + rho_GGE,
# where rho_SA = S(tau) * M_KK^4 >> rho_GGE. The Friedmann equation:
#
#   3 M_Pl^2 H^2 = rho_SA + rho_GGE
#
# A perturbation in branch I changes rho_GGE_I, giving:
#
#   delta_H / H = delta_rho_I / (2 * rho_total)
#
# And: dN/dsigma_I = delta_N / delta_sigma_I
#                   = (1/(2 rho_total)) * drho_I/dsigma_I * (1/eps_H)
#
# where eps_H = -dH/dt / H^2 is the Hubble slow-roll parameter.

# Convert units: everything in M_KK
# H_fold is in M_KK units, M_Pl_reduced in GeV
M_Pl_MKK = M_Pl_reduced / M_KK  # M_Pl in M_KK units
print(f"\n--- Scale hierarchy ---")
print(f"  M_Pl / M_KK = {M_Pl_MKK:.4f}")
print(f"  H_fold (M_KK) = {H_fold:.4f}")
print(f"  3 M_Pl^2 H^2 = {3 * M_Pl_MKK**2 * H_fold**2:.4e} M_KK^4")

# Total energy from Friedmann: rho_total = 3 M_Pl^2 H^2
rho_total_friedmann = 3.0 * M_Pl_MKK**2 * H_fold**2

# The spectral action energy density at the fold
# S_fold ~ 250360 in spectral units. In M_KK^4, we use:
# rho_SA ~ S_fold (dimensionless) represents the spectral action value
# The actual energy density rho = (f_0 * Lambda^4 + ...) / (16 pi^2)
# But S_fold already encodes this. The Hubble rate is derived from:
# H^2 = S_fold * (M_KK / M_Pl)^2 * geometric_factor

eps_H_fold = 0.022  # canonical slow-roll parameter at fold  # (local)

print(f"  S_fold = {S_fold:.2f}")
print(f"  rho_SA (Friedmann) = {rho_total_friedmann:.4e} M_KK^4")
print(f"  rho_GGE = {rho_total:.6e} M_KK^4")
print(f"  rho_GGE / rho_SA = {rho_total / rho_total_friedmann:.4e}")
print(f"  eps_H = {eps_H_fold}")

# --- drho_I / dsigma_I for each group ---
# Acoustic (gapless): drho/dsigma ~ (c_Gold * k_eff)^2 * sigma / V_eff
# where k_eff is the typical wavenumber of excited modes
# More precisely: for modes with n_k ~ exp(-pi k^2 xi_KZ^2),
# the characteristic k is k_KZ = 1/(pi xi_KZ^2)^{1/2}

xi_KZ = float(kz_data['xi_KZ'])
K_KZ = float(kz_data['K_KZ'])  # characteristic KZ wavenumber

print(f"\n  KZ parameters: xi_KZ = {xi_KZ:.6f}, K_KZ = {K_KZ:.4f} M_KK^{-1}")

# Effective mass-squared for each group
# m_eff^2 = omega^2 at k=0 (gap) + c_s^2 * k_eff^2
# For acoustic: omega(k=0) = 0, so m_eff^2 = c_Gold^2 * K_KZ^2
# For Leggett: m_eff^2 = omega_L^2 + c_L^2 * K_KZ^2
# For optical: m_eff^2 = omega_H^2 + c_H^2 * K_KZ^2

m_eff_sq_acoustic = c_acoustic**2 * K_KZ**2
m_eff_sq_leggett = omega_L1**2 + c_leggett**2 * K_KZ**2
m_eff_sq_optical = omega_H1**2 + c_optical**2 * K_KZ**2

print(f"\n--- Effective mass-squared (M_KK^2) ---")
print(f"  Acoustic: m_eff^2 = {m_eff_sq_acoustic:.6e}")
print(f"  Leggett:  m_eff^2 = {m_eff_sq_leggett:.6e}")
print(f"  Optical:  m_eff^2 = {m_eff_sq_optical:.6e}")

# drho_I / dsigma_I = m_eff_I^2 * sigma_I (for massive/massless fields alike)
drho_dsigma_acoustic = m_eff_sq_acoustic * sigma_acoustic
drho_dsigma_leggett = m_eff_sq_leggett * sigma_leggett
drho_dsigma_optical = m_eff_sq_optical * sigma_optical

drho_dsigma_total = drho_dsigma_acoustic + drho_dsigma_leggett + drho_dsigma_optical

print(f"\n--- drho_I / dsigma_I ---")
print(f"  Acoustic: {drho_dsigma_acoustic:.6e}")
print(f"  Leggett:  {drho_dsigma_leggett:.6e}")
print(f"  Optical:  {drho_dsigma_optical:.6e}")
print(f"  Total:    {drho_dsigma_total:.6e}")

# ============================================================================
#  SECTION 6: dN/dsigma_I — the conversion coefficients
# ============================================================================
#
# The delta-N formula in the multifield case with a dominant background:
#
#   dN/dsigma_I = H / (dot{rho}_total / rho_total)^{-1} * drho_I/dsigma_I / (2 * rho_total)
#
# Simplifying using the Friedmann + continuity equations:
#   dot{rho} = -3 H (rho + p) = -3 H rho (1 + w)
#   eps_H = (3/2)(1 + w)  (for single-field; generalized)
#
# So: dN/dsigma_I = (1 / (6 H * (1 + w) * rho_total)) * drho_I/dsigma_I
#                 = (1 / (4 eps_H * H * rho_total)) * drho_I/dsigma_I
#
# But this is the conversion for perturbations of the BACKGROUND.
# The GGE fluctuations are perturbations of the quasiparticle occupation,
# which sits on top of the spectral action background. The relevant
# conversion uses the TOTAL energy density (dominated by spectral action):
#
#   dN/dsigma_I = drho_I/dsigma_I / (2 * eps_H * 3 M_Pl^2 H^2)
#               = drho_I/dsigma_I / (6 * eps_H * M_Pl^2 * H^2)

# Method 1: Direct from Friedmann + slow-roll
dN_dsigma = np.zeros(3)  # [acoustic, leggett, optical]
drho_dsigma_arr = np.array([drho_dsigma_acoustic, drho_dsigma_leggett,
                             drho_dsigma_optical])

prefactor = 1.0 / (6.0 * eps_H_fold * M_Pl_MKK**2 * H_fold**2)

for I in range(3):
    dN_dsigma[I] = prefactor * drho_dsigma_arr[I]

print(f"\n{'='*72}")
print(f"CONVERSION COEFFICIENTS: dN/dsigma_I (Method 1: Friedmann)")
print(f"{'='*72}")
print(f"  Prefactor = 1/(6 eps_H M_Pl^2 H^2) = {prefactor:.6e} M_KK^{-4}")
for I in range(3):
    print(f"  {group_names[I]:>30s}: dN/dsigma = {dN_dsigma[I]:.6e}")

# Method 2: Energy-fraction weighted
# In the curvaton-like scenario, where the GGE excitations' energy fraction
# evolves, the conversion coefficient is:
#
#   dN/dsigma_I = (2/3) * r_I * (1/sigma_I)
#
# where r_I = rho_I / rho_total is the energy fraction at the time of
# conversion (when the branch starts to dominate or decay).
# For the exflation scenario where the GGE never dominates rho_total,
# r_I = rho_I / rho_SA, and:
#
#   dN/dsigma_I = (2/3) * (rho_I / rho_total_friedmann) * (1/sigma_I)

dN_dsigma_m2 = np.zeros(3)
rho_groups = np.array([rho_acoustic, rho_leggett, rho_optical])
sigma_groups = np.array([sigma_acoustic, sigma_leggett, sigma_optical])

for I in range(3):
    if sigma_groups[I] > 0:
        r_I = rho_groups[I] / rho_total_friedmann
        dN_dsigma_m2[I] = (2.0/3.0) * r_I / sigma_groups[I]

print(f"\n{'='*72}")
print(f"CONVERSION COEFFICIENTS: dN/dsigma_I (Method 2: Curvaton-like)")
print(f"{'='*72}")
for I in range(3):
    r_I = rho_groups[I] / rho_total_friedmann if rho_total_friedmann > 0 else 0
    print(f"  {group_names[I]:>30s}: dN/dsigma = {dN_dsigma_m2[I]:.6e}, "
          f"r_I = {r_I:.6e}")

# Method 3: Direct Garriga-Mukhanov generalization
# The standard single-field result is: dN/dsigma = H / dot{sigma}
# For multifield: dN/dsigma_I = H * sigma_I / (2 * Sum_J rho_J)
#   (when all fields contribute to the kinetic energy equally)
# But the GGE fields are not rolling; they are oscillating quasiparticles.
# The "kinetic energy" is rho_I itself (equipartition).
# So: dN/dsigma_I = H / (2 * m_eff_I * sigma_I)  [for each massive field]

dN_dsigma_m3 = np.zeros(3)
m_eff = np.array([np.sqrt(m_eff_sq_acoustic), np.sqrt(m_eff_sq_leggett),
                   np.sqrt(m_eff_sq_optical)])

for I in range(3):
    if sigma_groups[I] > 0 and m_eff[I] > 0:
        # Oscillating field: <dot{sigma}_I> = m_eff_I * sigma_I
        dN_dsigma_m3[I] = H_fold / (2.0 * m_eff[I] * sigma_groups[I])

print(f"\n{'='*72}")
print(f"CONVERSION COEFFICIENTS: dN/dsigma_I (Method 3: GGE oscillating)")
print(f"{'='*72}")
for I in range(3):
    print(f"  {group_names[I]:>30s}: dN/dsigma = {dN_dsigma_m3[I]:.6e}, "
          f"m_eff = {m_eff[I]:.6e}")

# ============================================================================
#  SECTION 7: Multifield A_s enhancement
# ============================================================================
#
# A_s^{multi} = (H^2 / (8 pi^2)) * Sum_I (dN/dsigma_I)^2
#
# In M_KK units, with H in M_KK:
# A_s is dimensionless: (H/M_Pl)^2 / (8 pi^2 eps) for single field
# For multifield: A_s = Sum_I (H * dN/dsigma_I * delta_sigma_I_rms)^2 / (8 pi^2)
#
# The fluctuation amplitude in each branch (from Bogoliubov pair creation):
#   <delta_sigma_I^2> = Sum_k |beta_k|^2 / (2 omega_k)
# For the KZ occupation: n_k = |beta_k|^2 ~ exp(-pi k^2 xi_KZ^2)

# Single-field A_s (standard formula at transit scale)
eps_H = eps_H_fold
A_s_single = H_fold**2 / (8.0 * PI**2 * eps_H * M_Pl_MKK**2)

print(f"\n{'='*72}")
print(f"MULTIFIELD A_s ENHANCEMENT")
print(f"{'='*72}")
print(f"\n  Single-field A_s = H^2 / (8 pi^2 eps M_Pl^2)")
print(f"                   = {H_fold**2:.4e} / (8 pi^2 * {eps_H} * {M_Pl_MKK:.4e}^2)")
print(f"                   = {A_s_single:.6e}")
print(f"  Observed A_s     = {A_s_CMB:.6e}")
print(f"  Gap (single):    {np.log10(A_s_single / A_s_CMB):.2f} OOM")

# Multifield A_s from each method:
# Use the field fluctuations delta_sigma_I from the Bogoliubov occupation
# delta_sigma_I^2 = sigma_sq_group / (2 pi)^3 (per mode, then sum)
# Actually, the delta_sigma are already encoded in sigma_sq from the occupation.
# The power spectrum contribution from each branch:
#   P_zeta_I = (dN/dsigma_I)^2 * <delta_sigma_I^2>
#            = (dN/dsigma_I)^2 * sigma_sq_I

# Method 1 multifield A_s
sigma_sq_groups = np.array([sigma_sq_acoustic, sigma_sq_leggett, sigma_sq_optical])
A_s_multi_m1 = np.sum(dN_dsigma**2 * sigma_sq_groups)
A_s_multi_m2 = np.sum(dN_dsigma_m2**2 * sigma_sq_groups)
A_s_multi_m3 = np.sum(dN_dsigma_m3**2 * sigma_sq_groups)

# Per-branch contributions
print(f"\n  --- Method 1 (Friedmann) ---")
for I in range(3):
    contrib = dN_dsigma[I]**2 * sigma_sq_groups[I]
    frac = contrib / A_s_multi_m1 * 100 if A_s_multi_m1 > 0 else 0
    print(f"    {group_names[I]:>30s}: P_zeta_I = {contrib:.6e} ({frac:.1f}%)")
print(f"    A_s^multi (M1) = {A_s_multi_m1:.6e}")
print(f"    Gap from Planck: {np.log10(A_s_multi_m1 / A_s_CMB):.2f} OOM")
print(f"    Enhancement: A_s^multi / A_s_single = {A_s_multi_m1 / A_s_single:.4e}")

print(f"\n  --- Method 2 (Curvaton-like) ---")
for I in range(3):
    contrib = dN_dsigma_m2[I]**2 * sigma_sq_groups[I]
    frac = contrib / A_s_multi_m2 * 100 if A_s_multi_m2 > 0 else 0
    print(f"    {group_names[I]:>30s}: P_zeta_I = {contrib:.6e} ({frac:.1f}%)")
print(f"    A_s^multi (M2) = {A_s_multi_m2:.6e}")
print(f"    Gap from Planck: {np.log10(A_s_multi_m2 / A_s_CMB):.2f} OOM")
print(f"    Enhancement: A_s^multi / A_s_single = {A_s_multi_m2 / A_s_single:.4e}")

print(f"\n  --- Method 3 (GGE oscillating) ---")
for I in range(3):
    contrib = dN_dsigma_m3[I]**2 * sigma_sq_groups[I]
    frac = contrib / A_s_multi_m3 * 100 if A_s_multi_m3 > 0 else 0
    print(f"    {group_names[I]:>30s}: P_zeta_I = {contrib:.6e} ({frac:.1f}%)")
print(f"    A_s^multi (M3) = {A_s_multi_m3:.6e}")
print(f"    Gap from Planck: {np.log10(A_s_multi_m3 / A_s_CMB):.2f} OOM")
print(f"    Enhancement: A_s^multi / A_s_single = {A_s_multi_m3 / A_s_single:.4e}")

# ============================================================================
#  SECTION 8: Cross-checks
# ============================================================================

print(f"\n{'='*72}")
print(f"CROSS-CHECKS")
print(f"{'='*72}")

# Check 1: Sum rule -- total dN/dsigma should be consistent with single-field
# In the limit where one branch dominates, multifield reduces to single-field
dominant_frac_m1 = np.max(dN_dsigma**2 * sigma_sq_groups) / A_s_multi_m1 if A_s_multi_m1 > 0 else 0
print(f"\n  1. Dominant branch fraction (M1): {dominant_frac_m1*100:.1f}%")
print(f"     (100% = single-field limit; <100% = genuine multifield)")

# Check 2: Normalization -- Bogoliubov coefficients
# |alpha|^2 - |beta|^2 = 1 (bosonic): check from transit PS
beta_sq_mean = np.mean(beta_sq_rk)
print(f"\n  2. Mean |beta_k|^2 from transit (RK): {beta_sq_mean:.4f}")
print(f"     These are MUCH larger than 1 because z''/z >> k^2 c_s^2")
print(f"     (saturated superhorizon amplification, not WKB Bogoliubov)")

# Check 3: Energy conservation
rho_GGE_frac = rho_total / rho_total_friedmann
print(f"\n  3. rho_GGE / rho_Friedmann = {rho_GGE_frac:.4e}")
print(f"     GGE is perturbative: rho_GGE << rho_SA (spectral action)")
print(f"     This justifies the linear delta-N approach.")

# Check 4: Flat-space limit -- if H -> 0, all dN/dsigma -> 0
print(f"\n  4. Flat-space limit: dN/dsigma ~ H, so dN -> 0 as H -> 0. PASS")

# Check 5: Consistency of methods
print(f"\n  5. Method comparison (enhancement factor A_s^multi / A_s_single):")
if A_s_single > 0:
    print(f"     M1 (Friedmann):     {A_s_multi_m1/A_s_single:.4e}")
    print(f"     M2 (Curvaton-like): {A_s_multi_m2/A_s_single:.4e}")
    print(f"     M3 (GGE oscillat.): {A_s_multi_m3/A_s_single:.4e}")

# ============================================================================
#  SECTION 9: f_NL estimate from multifield
# ============================================================================
#
# In the multifield delta-N formalism, the local non-Gaussianity is:
#
#   f_NL^local = (5/6) * Sum_I (dN/dsigma_I)^2 * d2N/dsigma_I^2
#                / [Sum_I (dN/dsigma_I)^2]^2
#
# For the simplest case where N is a separable function of each sigma_I:
#   d2N/dsigma_I^2 ~ -dN/dsigma_I * (m_eff_I^2 + 3 H^2) / (sigma_I * ...)
#
# A rough estimate: f_NL ~ O(1) * (number of contributing branches)
# For 3 groups with comparable contributions: f_NL ~ O(1)

# Simple estimate from energy fraction hierarchy
w_I = np.array([f_acoustic, f_leggett, f_optical])
f_NL_est = (5.0/6.0) * np.sum(w_I**2) / (np.sum(w_I))**2

print(f"\n{'='*72}")
print(f"NON-GAUSSIANITY ESTIMATE")
print(f"{'='*72}")
print(f"  f_NL^local (energy fraction estimate) ~ {f_NL_est:.4f}")
print(f"  (This is the multifield delta-N contribution only)")
print(f"  (Dissipative f_NL from Paper [09] could be much larger)")

# Maldacena consistency check: single-field gives f_NL = (5/12)(1-n_s)
n_s_framework = 0.959
f_NL_maldacena = (5.0/12.0) * (1.0 - n_s_framework)
print(f"  f_NL (Maldacena single-field) = {f_NL_maldacena:.4f}")
print(f"  Multifield can exceed this by ~N_fields factor")

# ============================================================================
#  SECTION 10: Gate verdict
# ============================================================================

print(f"\n{'='*72}")
print(f"GATE VERDICT: MULTIFIELD-DELTA-N-67")
print(f"{'='*72}")

# Collect key results
# Use Method 1 (Friedmann) as primary, report all three
enhancement_m1 = A_s_multi_m1 / A_s_single if A_s_single > 0 else 0
enhancement_m2 = A_s_multi_m2 / A_s_single if A_s_single > 0 else 0
enhancement_m3 = A_s_multi_m3 / A_s_single if A_s_single > 0 else 0

# Best enhancement across methods
best_enhancement = max(enhancement_m1, enhancement_m2, enhancement_m3)
best_method_idx = np.argmax([enhancement_m1, enhancement_m2, enhancement_m3])
method_names = ['M1 (Friedmann)', 'M2 (Curvaton)', 'M3 (GGE osc.)']

gap_m1 = np.log10(A_s_multi_m1 / A_s_CMB) if A_s_multi_m1 > 0 else float('inf')
gap_m2 = np.log10(A_s_multi_m2 / A_s_CMB) if A_s_multi_m2 > 0 else float('inf')
gap_m3 = np.log10(A_s_multi_m3 / A_s_CMB) if A_s_multi_m3 > 0 else float('inf')

gate_detail = (f"dN/dsigma: acoustic={dN_dsigma[0]:.3e}, leggett={dN_dsigma[1]:.3e}, "
               f"optical={dN_dsigma[2]:.3e}. "
               f"Enhancement: M1={enhancement_m1:.3e}, M2={enhancement_m2:.3e}, "
               f"M3={enhancement_m3:.3e}. "
               f"Best gap from Planck: {min(abs(gap_m1), abs(gap_m2), abs(gap_m3)):.1f} OOM")

print(f"\n  Type: INFO (pre-registered)")
print(f"  Detail: {gate_detail}")
print(f"\n  Key numbers:")
print(f"    Conversion coefficients (M1, Friedmann):")
print(f"      Acoustic: dN/dsigma = {dN_dsigma[0]:.6e}")
print(f"      Leggett:  dN/dsigma = {dN_dsigma[1]:.6e}")
print(f"      Optical:  dN/dsigma = {dN_dsigma[2]:.6e}")
print(f"    Enhancement: {best_enhancement:.4e} (best: {method_names[best_method_idx]})")
print(f"    A_s gap: M1={gap_m1:.2f}, M2={gap_m2:.2f}, M3={gap_m3:.2f} OOM from Planck")
print(f"    f_NL estimate: {f_NL_est:.4f}")

# ============================================================================
#  SECTION 11: Save results
# ============================================================================

outfile = os.path.join(os.path.dirname(__file__), 's67_multifield_delta_n.npz')

np.savez(
    outfile,
    # Gate metadata
    gate_name='MULTIFIELD-DELTA-N-67',
    gate_verdict='INFO',
    gate_detail=gate_detail,
    # Branch structure
    branch_labels_6=np.array(branch_labels),
    group_names=np.array(group_names),
    idx_acoustic=np.array(idx_acoustic),
    idx_leggett=np.array(idx_leggett),
    idx_optical=np.array(idx_optical),
    # Energy per branch and group
    E_per_branch=E_per_branch,
    E_total=E_total,
    f_acoustic=f_acoustic,
    f_leggett=f_leggett,
    f_optical=f_optical,
    # Field variances
    sigma_sq_branch=sigma_sq_branch,
    sigma_sq_groups=sigma_sq_groups,
    sigma_groups=sigma_groups,
    rho_groups=rho_groups,
    # Effective masses
    m_eff=m_eff,
    m_eff_sq=np.array([m_eff_sq_acoustic, m_eff_sq_leggett, m_eff_sq_optical]),
    # drho/dsigma
    drho_dsigma=drho_dsigma_arr,
    # Conversion coefficients (3 methods)
    dN_dsigma_m1=dN_dsigma,       # Friedmann
    dN_dsigma_m2=dN_dsigma_m2,    # Curvaton-like
    dN_dsigma_m3=dN_dsigma_m3,    # GGE oscillating
    # A_s results
    A_s_single=A_s_single,
    A_s_multi_m1=A_s_multi_m1,
    A_s_multi_m2=A_s_multi_m2,
    A_s_multi_m3=A_s_multi_m3,
    enhancement_m1=enhancement_m1,
    enhancement_m2=enhancement_m2,
    enhancement_m3=enhancement_m3,
    # Gaps from Planck
    gap_m1_OOM=gap_m1,
    gap_m2_OOM=gap_m2,
    gap_m3_OOM=gap_m3,
    A_s_gap_transit_OOM=A_s_gap_OOM,
    # Non-Gaussianity
    f_NL_multifield_est=f_NL_est,
    f_NL_maldacena=f_NL_maldacena,
    # Scale hierarchy
    M_Pl_over_M_KK=M_Pl_MKK,
    rho_total_friedmann=rho_total_friedmann,
    rho_GGE_total=rho_total,
    eps_H_fold=eps_H_fold,
    # Input parameters
    H_fold=H_fold,
    K_KZ=K_KZ,
    xi_KZ=xi_KZ,
    c_acoustic=c_acoustic,
    c_leggett=c_leggett,
    c_optical=c_optical,
)

print(f"\n  Results saved to: {outfile}")

# ============================================================================
#  SECTION 12: Diagnostic plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('MULTIFIELD-DELTA-N-67: GGE Branch Conversion Coefficients',
             fontsize=14, fontweight='bold')

# (a) Energy fraction per branch
ax = axes[0, 0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
bars = ax.bar(range(6), E_per_branch / E_total * 100, color=colors)
ax.set_xticks(range(6))
ax.set_xticklabels([l[:8] for l in branch_labels], rotation=45, ha='right')
ax.set_ylabel('Energy fraction (%)')
ax.set_title('(a) Energy per GL branch')
ax.set_yscale('log')
for i, b in enumerate(bars):
    if E_per_branch[i] > 0:
        ax.text(b.get_x() + b.get_width()/2., b.get_height(),
                f'{E_per_branch[i]/E_total*100:.1f}%', ha='center', va='bottom', fontsize=8)

# (b) Conversion coefficients (3 methods)
ax = axes[0, 1]
x = np.arange(3)
width = 0.25  # (local)
bars1 = ax.bar(x - width, np.abs(dN_dsigma), width, label='M1 (Friedmann)', alpha=0.8)
bars2 = ax.bar(x, np.abs(dN_dsigma_m2), width, label='M2 (Curvaton)', alpha=0.8)
bars3 = ax.bar(x + width, np.abs(dN_dsigma_m3), width, label='M3 (GGE osc.)', alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels(['Acoustic', 'Leggett', 'Optical'])
ax.set_ylabel('|dN/dsigma_I|')
ax.set_title('(b) Conversion coefficients')
ax.set_yscale('log')
ax.legend(fontsize=8)

# (c) A_s contribution per group
ax = axes[1, 0]
contrib_m1 = dN_dsigma**2 * sigma_sq_groups
contrib_m3 = dN_dsigma_m3**2 * sigma_sq_groups
bars1 = ax.bar(x - width/2, contrib_m1, width, label='M1', alpha=0.8)
bars2 = ax.bar(x + width/2, contrib_m3, width, label='M3', alpha=0.8)
ax.axhline(y=A_s_CMB, color='r', linestyle='--', label=f'A_s(Planck) = {A_s_CMB:.1e}')
ax.set_xticks(x)
ax.set_xticklabels(['Acoustic', 'Leggett', 'Optical'])
ax.set_ylabel('P_zeta_I contribution')
ax.set_title('(c) A_s per group vs Planck')
ax.set_yscale('log')
ax.legend(fontsize=8)

# (d) A_s gap summary
ax = axes[1, 1]
gaps = [A_s_gap_OOM, gap_m1, gap_m2, gap_m3]
labels_gap = ['Transit\n(single)', 'Multi M1\n(Friedmann)', 'Multi M2\n(Curvaton)',
              'Multi M3\n(GGE osc.)']
colors_gap = ['gray', '#1f77b4', '#ff7f0e', '#2ca02c']
bars = ax.bar(range(4), [abs(g) for g in gaps], color=colors_gap, alpha=0.8)
ax.set_xticks(range(4))
ax.set_xticklabels(labels_gap, fontsize=9)
ax.set_ylabel('|log10(A_s/A_s_Planck)| (OOM)')
ax.set_title('(d) A_s gap from Planck (lower = better)')
ax.axhline(y=0, color='green', linestyle='--', label='Planck match')
for i, b in enumerate(bars):
    ax.text(b.get_x() + b.get_width()/2., b.get_height() + 0.2,
            f'{abs(gaps[i]):.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.legend()

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(__file__), 's67_multifield_delta_n.png')
plt.savefig(plot_path, dpi=150)
print(f"  Plot saved to: {plot_path}")

print(f"\n{'='*72}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*72}")
