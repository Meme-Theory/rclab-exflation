#!/usr/bin/env python3
"""
GGE-DM-43: GGE Dark Matter Abundance via Q-Theory
===================================================

Computes dark matter abundance Omega_DM from:
  1. GGE quasiparticle relic (59.8 pairs, E_exc = 50.9 M_KK)
  2. Q-field perturbations delta_q (Paper 35: Klinkhamer & Volovik 2016)

Two-source budget:
  - GGE quasiparticles (internal-space excitations, w=0)
  - Q-field perturbations (spatial tau fluctuations, w=0 by Paper 35)

Key context from W1-1 (QFIELD-43 = FAIL):
  - Q-theory self-tuning trivially satisfied at tau=0
  - Residual CC = 4.9e+66 GeV^4 (113 OOM above obs)
  - rho_Lambda is NOT set by q-theory; it is the raw GGE energy
  - omega_q = 30.8 M_KK (fast oscillation)

Paper 35 mechanism: delta_q oscillations behave as pressureless dust
(w=0) when averaged over many periods. DM density:
  rho_DM = (1/2) * <(d_t delta_q)^2 + c_q^2 (nabla delta_q)^2>

Gate GGE-DM-43:
  PASS:         Omega_DM / Omega_Lambda > 0.03
  FAIL:         Omega_DM / Omega_Lambda < 0.001
  INTERMEDIATE: 0.001 to 0.03

References:
  Paper 35: Klinkhamer & Volovik, JETP Lett. 105, 74-77 (2017) [arXiv:1612.02326]
  Paper 05: Volovik, Ann.Phys. 517, 165 (2005) [gr-qc/0405012]
  Paper 15: Klinkhamer & Volovik, PRD 77, 085015 (2008) [0711.3170]
  Paper 16: Klinkhamer & Volovik, PRD 79, 063527 (2009) [0811.4347]
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ===========================================================================
# STEP 1: Load all input data
# ===========================================================================
print("=" * 72)
print("GGE-DM-43: GGE Dark Matter Abundance via Q-Theory")
print("=" * 72)

# W1-1 results
d_qt = np.load('tier0-computation/s43_qtheory_selftune.npz', allow_pickle=True)
S_0 = float(d_qt['S_0'])
S_fold_val = float(d_qt['S_fold'])
Delta_S_fold = float(d_qt['Delta_S_fold'])
chi_q_0 = float(d_qt['chi_q_0'])
omega_q_MKK = float(d_qt['omega_q_MKK'])
rho_GGE_GeV4 = float(d_qt['rho_GGE_GeV4'])
rho_obs_GeV4 = float(d_qt['rho_obs_GeV4'])
tau_cross_est = float(d_qt['tau_cross_est'])
r_suppression = float(d_qt['r_suppression'])

# Gradient stiffness
d_gs = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
Z_fold = float(d_gs['Z_fold'][0])
dS_fold = float(d_gs['dS_fold'][0])
d2S_fold = float(d_gs['d2S_fold'][0])
c_fabric = float(d_gs['c_fabric'][0])

# GGE energy
d_ge = np.load('tier0-computation/s42_gge_energy.npz', allow_pickle=True)
E_exc_MKK = float(d_ge['E_exc_MKK'])
E_cond_MKK = float(d_ge['E_cond_MKK'])
n_pairs = float(d_ge['n_pairs'])
Delta_pair_MKK = float(d_ge['Delta_pair_MKK'])

# DM profile (S42)
d_dm = np.load('tier0-computation/s42_dm_profile.npz', allow_pickle=True)
Omega_discrepancy = float(d_dm['Omega_discrepancy_factor'][0])
E_DM_per_crystal = float(d_dm['E_DM_per_crystal'][0])
M_DM_MKK = float(d_dm['M_DM_MKK'][0])

# Constants
d_cs = np.load('tier0-computation/s42_constants_snapshot.npz', allow_pickle=True)
M_KK_grav = float(d_cs['M_KK_from_GN'])
M_KK_gauge = float(d_cs['M_KK_kerner'])
a0_fold = float(d_cs['a0_fold'])
a2_fold = float(d_cs['a2_fold'])
a4_fold = float(d_cs['a4_fold'])

# Also load the spectral action data for spline
d36 = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)
tau_16 = d36['tau_combined']
S_full_16 = d36['S_full']
cs_S = CubicSpline(tau_16, S_full_16)

# Physical constants
from canonical_constants import M_Pl_unreduced as M_Pl_GeV  # 1.22e19 GeV
from canonical_constants import hbar_eV_s as hbar_eVs  # eV*s
from canonical_constants import H_0_inv_s as H_0_Hz  # s^{-1} (67.4 km/s/Mpc)
c_light = 2.998e10       # cm/s
G_N = 6.674e-8           # cm^3 g^{-1} s^{-2}
rho_crit_GeV4 = 3.0 * (H_0_Hz / hbar_eVs)**2 * M_Pl_GeV**2 / (8 * np.pi)
# More precise: rho_crit = 3 H_0^2 M_Pl^2 / (8 pi) in natural units
# But let's use the standard value
from canonical_constants import rho_crit_GeV4  # GeV^4 (standard value)
Omega_Lambda_obs = 0.685
Omega_DM_obs = 0.265
rho_Lambda_obs = Omega_Lambda_obs * rho_crit_GeV4
rho_DM_obs = Omega_DM_obs * rho_crit_GeV4

# Friedmann prefactor (from W1-1 convention)
prefactor = 1.0 / (2.0 * (4 * np.pi)**2)  # = 1/315.83

# M_KK unit conversions
M_KK_eV = M_KK_grav * 1e9  # GeV -> eV
t_MKK_s = hbar_eVs / M_KK_eV  # seconds per M_KK^{-1}
L_MKK_cm = hbar_eVs * c_light / M_KK_eV  # cm per M_KK^{-1}

print("\n--- Input Data ---")
print(f"S(0)             = {S_0:.2f} M_KK^4")
print(f"Delta_S_fold     = {Delta_S_fold:.2f} M_KK^4")
print(f"chi_q_0          = {chi_q_0:.2f} M_KK^4")
print(f"omega_q          = {omega_q_MKK:.4f} M_KK")
print(f"Z_fold           = {Z_fold:.2f} M_KK^2")
print(f"c_fabric         = {c_fabric:.2f} M_KK^{{-1}}")
print(f"E_exc_MKK        = {E_exc_MKK:.3f} M_KK")
print(f"E_cond_MKK       = {E_cond_MKK:.4f} M_KK")
print(f"n_pairs          = {n_pairs}")
print(f"Delta_pair_MKK   = {Delta_pair_MKK:.4f} M_KK")
print(f"M_KK (gravity)   = {M_KK_grav:.3e} GeV")
print(f"M_KK (gauge)     = {M_KK_gauge:.3e} GeV")
print(f"rho_crit         = {rho_crit_GeV4:.3e} GeV^4")
print(f"rho_Lambda_obs   = {rho_Lambda_obs:.3e} GeV^4")
print(f"rho_DM_obs       = {rho_DM_obs:.3e} GeV^4")
print(f"S42 discrepancy  = {Omega_discrepancy:.0f}x")

# ===========================================================================
# STEP 2: Q-field perturbation spectrum (Paper 35)
# ===========================================================================
print("\n" + "=" * 72)
print("STEP 2: Q-Field Perturbation Spectrum (Paper 35)")
print("=" * 72)

# Paper 35 EOM for delta_q perturbations:
#   ddot(delta_q) + 3H dot(delta_q) - (c_q^2 / a^2) nabla^2(delta_q) + m_q^2 delta_q = 0
#
# Here q = tau (the geometric deformation parameter).
# From W1-1:
#   m_q^2 = d^2 rho_gs / d tau^2 |_{tau=0}
#   In q-theory notation: m_q^2 = chi_q = |S''(0)|
#
# The mass of the q-field perturbation:
m_q_sq_MKK2 = chi_q_0  # M_KK^2 (since S is in M_KK^4, tau dimensionless)
m_q_MKK = np.sqrt(m_q_sq_MKK2)
m_q_GeV = m_q_MKK * M_KK_grav

print(f"\nQ-field mass (from Paper 05 chi_q):")
print(f"  m_q^2 = chi_q = {m_q_sq_MKK2:.2f} M_KK^2")
print(f"  m_q   = {m_q_MKK:.4f} M_KK = {m_q_GeV:.3e} GeV")

# Speed of q-perturbations from gradient stiffness:
# c_q^2 = Z / (m_q^2 * L^2) where L is the characteristic length
# More precisely, from the spectral action:
#   S[tau(x)] = int d^4x [ (1/2) Z (nabla tau)^2 + V(tau) ]
# The EOM for tau perturbations delta_tau = tau - tau_0:
#   ddot(delta_tau) + 3H dot(delta_tau) - c_q^2 nabla^2(delta_tau) + V''(tau_0) delta_tau = 0
# where c_q^2 = 1 (since the spatial gradient term has the same coefficient
# as the time derivative in Lorentz-invariant theory).
#
# BUT: the internal geometry is NOT Lorentz invariant a priori.
# The speed of perturbations in the internal space is set by the
# ratio Z / (kinetic coefficient) from the DeWitt metric on superspace.
#
# From S42 gradient stiffness: Z_fold = 74,731 and c_fabric = 210.
# c_fabric^2 = Z / M_ATDHFB = 74731 / 1.695 = 44,087
# This is the effective c_q^2 in M_KK units.
#
# Actually, c_fabric = sqrt(Z / M) gives the propagation speed of
# tau perturbations in the internal superspace metric.

M_ATDHFB = 1.695  # GCM mass parameter
c_q_sq = Z_fold / M_ATDHFB  # dimensionless (M_KK units)
c_q = np.sqrt(c_q_sq)

print(f"\nQ-field propagation speed:")
print(f"  c_q^2 = Z/M_ATDHFB = {Z_fold:.2f}/{M_ATDHFB:.3f} = {c_q_sq:.2f} M_KK^0")
print(f"  c_q = {c_q:.2f} M_KK^0 (= {c_q:.2f} in M_KK speed units)")
print(f"  c_fabric (stored) = {c_fabric:.2f} (agreement: {abs(c_q - c_fabric)/c_fabric*100:.1f}%)")

# omega_q from Paper 35:
# omega_q = sqrt(m_q^2 + c_q^2 k^2) for mode k
# For k=0 (homogeneous mode): omega_q = m_q
omega_q_check = m_q_MKK
print(f"\nConsistency: omega_q(k=0) = m_q = {omega_q_check:.4f} M_KK")
print(f"  vs W1-1 omega_q = {omega_q_MKK:.4f} (ratio: {omega_q_check/omega_q_MKK:.4f})")
# The prefactor difference is because W1-1 uses omega_q^2 = chi_q * prefactor
# whereas here we use m_q^2 = chi_q directly (no Friedmann prefactor).
# The physical frequency is omega_phys = sqrt(chi_q) since chi_q has units M_KK^4/1^2 = M_KK^4
# But tau is dimensionless, so chi_q = d^2 S/dtau^2 has units M_KK^4.
# The EOM is: M * ddot(tau) + V''(tau_0) delta_tau = 0
# so omega = sqrt(V''/M) = sqrt(d2S/dtau2 / M_ATDHFB)
omega_q_physical = np.sqrt(d2S_fold / M_ATDHFB)  # using fold value (more accurate)
omega_q_phys_0 = np.sqrt(chi_q_0 / M_ATDHFB)  # using ground state

print(f"\nCorrected frequencies (GCM-weighted):")
print(f"  omega_q(tau=0) = sqrt(chi_q/M) = sqrt({chi_q_0:.0f}/{M_ATDHFB}) = {omega_q_phys_0:.2f} M_KK")
print(f"  omega_q(fold)  = sqrt(d2S/M)   = sqrt({d2S_fold:.0f}/{M_ATDHFB}) = {omega_q_physical:.2f} M_KK")

# Use the ground-state omega for q-field mass (self-tuning happens AT ground state)
omega_q = omega_q_phys_0
m_q_eff = omega_q  # effective mass in M_KK
m_q_eff_GeV = m_q_eff * M_KK_grav

print(f"\n  Adopted: omega_q = {omega_q:.4f} M_KK = {omega_q * M_KK_grav:.3e} GeV")

# Physical frequency
omega_q_Hz = omega_q * M_KK_eV / hbar_eVs
print(f"  omega_q = {omega_q_Hz:.3e} Hz")
print(f"  Planck comparison: omega_Pl ~ 1.85e43 Hz")
print(f"  omega_q / omega_Pl ~ {omega_q_Hz / 1.85e43:.3e}")

# ===========================================================================
# STEP 3: Compute rho_DM from q-perturbations (Paper 35 mechanism)
# ===========================================================================
print("\n" + "=" * 72)
print("STEP 3: rho_DM from Q-Perturbations (Paper 35)")
print("=" * 72)

# Paper 35: rho_DM = (1/2) <(d_t delta_q)^2 + c_q^2 (nabla delta_q)^2>
# For oscillating modes delta_q ~ A cos(omega_q t), virial theorem gives:
#   <(d_t delta_q)^2> = (1/2) omega_q^2 A^2
#   <c_q^2 (nabla delta_q)^2> ≈ 0 for k<<omega_q/c_q (homogeneous limit)
# so rho_DM ~ (1/4) omega_q^2 A^2
#
# What sets the amplitude A?
# TWO SOURCES:
#
# Source 1: Kibble-Zurek defect density
#   xi_KZ = 0.152 M_KK^{-1} from S42 W5-5
#   n_defect ~ 1/xi_KZ^3 (defect density)
#   Each defect carries energy ~ omega_q (one quantum)
#   BUT: these are INTERNAL SPACE defects, not 4D spatial defects
#
# Source 2: Quantum fluctuations of q-field
#   <delta_q^2> = 1/(2 omega_q) per mode (vacuum fluctuation)
#   In 4D: <delta_q^2> = integral d^3k/(2pi)^3 * 1/(2 omega_k)
#   With UV cutoff at M_KK: <delta_q^2> ~ M_KK^2 / (4pi^2 omega_q)

# ---- Source A: KZ density approach ----
xi_KZ = 0.152  # M_KK^{-1}
n_KZ = 1.0 / xi_KZ**3  # M_KK^3 (defect density in internal space)
print(f"\n--- Source A: Kibble-Zurek Defect Density ---")
print(f"  xi_KZ = {xi_KZ:.3f} M_KK^{{-1}}")
print(f"  n_KZ = 1/xi_KZ^3 = {n_KZ:.2f} M_KK^3")

# Each KZ defect in internal space carries q-perturbation energy.
# The amplitude of delta_q per defect ~ 1/sqrt(m_q * xi_KZ) (dimensional)
# Actually, the KZ defect density sets the initial condition for
# delta_q perturbations. Each defect region has delta_tau ~ xi_KZ * (d tau/d x)
# where (d tau/d x) is the gradient across the defect.
#
# More physical: the KZ mechanism produces domains of size xi_KZ where
# tau differs from equilibrium by some amount delta_tau_KZ.
# From S42: the transit goes from tau=0 to tau=0.19 and back.
# After transit, the GGE relic means tau has returned to 0 but
# quasiparticles persist. The q-field perturbation is not tau itself
# but the deviation from ground-state energy.
#
# The proper identification: delta_q ~ E_exc / (V * omega_q^2)
# where V is the volume of the internal space.

# Volume of internal space in M_KK units
Vol_SU3 = 1349.74  # from s42_gradient_stiffness (Haar-normalized)
print(f"  Vol(SU(3)) = {Vol_SU3:.2f} M_KK^{{-8}} (8-dimensional)")

# ---- Source B: GGE quasiparticle energy ----
print(f"\n--- Source B: GGE Quasiparticle Energy ---")
print(f"  n_pairs = {n_pairs}")
print(f"  E_exc = {E_exc_MKK:.3f} M_KK (total excitation energy)")
print(f"  Delta_pair = {Delta_pair_MKK:.4f} M_KK (pair energy)")

# The GGE relic consists of 59.8 quasiparticle pairs with total
# energy E_exc = 50.9 M_KK. These are INTERNAL excitations
# (momentum-space, on SU(3)). They carry no spatial momentum --
# they are pressureless (w=0) by construction.
#
# In q-theory language: the GGE IS the delta_q perturbation.
# The q-field has returned to equilibrium (tau=0), but the
# quasiparticle pairs persist because of integrability protection.
# Their energy density is:
#   rho_GGE = E_exc / Vol_SU3 (in internal volume)
# But this must be promoted to 4D by the Friedmann prefactor.

rho_GGE_MKK4 = E_exc_MKK * prefactor
rho_GGE_GeV4_grav = rho_GGE_MKK4 * M_KK_grav**4
print(f"\n  rho_GGE (Friedmann) = {rho_GGE_MKK4:.6f} M_KK^4")
print(f"  rho_GGE (GeV^4, gravity) = {rho_GGE_GeV4_grav:.3e}")

# ---- Source C: q-field oscillation energy (Paper 35) ----
print(f"\n--- Source C: Paper 35 q-Oscillation Energy ---")

# Paper 35 says the q-field oscillates with amplitude set by
# quantum fluctuations at the Planck scale. For the framework:
# <delta_q^2> ~ (M_KK / omega_q)^2 * n_modes
# where n_modes is the number of active modes.
#
# The number of q-field modes is set by the internal space geometry.
# Each Dirac eigenvalue pair contributes one q-mode (BCS channel).
# From S38: 59.8 pairs = 59.8 modes.
# n_modes_q = n_pairs (each pair is an independent fluctuation channel)

n_modes_q = n_pairs
delta_q_sq_per_mode = 1.0 / (2.0 * omega_q)  # M_KK^{-1} (vacuum fluctuation)
delta_q_sq_total = n_modes_q * delta_q_sq_per_mode

print(f"  n_modes = {n_modes_q}")
print(f"  <delta_q^2> per mode = 1/(2*omega_q) = {delta_q_sq_per_mode:.6f} M_KK^{{-1}}")
print(f"  <delta_q^2> total = {delta_q_sq_total:.4f} M_KK^{{-1}}")

# rho_DM from Paper 35:
# rho_DM = (1/2) m_q^2 <delta_q^2> (for oscillating q-field with w=0)
# In Friedmann normalization:
rho_DM_qfield_MKK4 = 0.5 * omega_q**2 * delta_q_sq_total * prefactor
rho_DM_qfield_GeV4 = rho_DM_qfield_MKK4 * M_KK_grav**4

print(f"\n  rho_DM (q-oscillation) = (1/2) omega_q^2 <delta_q^2> * prefactor")
print(f"  = 0.5 * {omega_q**2:.2f} * {delta_q_sq_total:.4f} * {prefactor:.6f}")
print(f"  = {rho_DM_qfield_MKK4:.6e} M_KK^4")
print(f"  = {rho_DM_qfield_GeV4:.3e} GeV^4")

# ===========================================================================
# STEP 4: Omega_DM / Omega_Lambda from q-perturbations
# ===========================================================================
print("\n" + "=" * 72)
print("STEP 4: Omega_DM / Omega_Lambda")
print("=" * 72)

# W1-1 showed: rho_Lambda = rho_GGE (q-theory self-tuning only removes S(0)).
# The gravitating vacuum energy is the GGE excitation energy.
# But W1-1 also showed this is 113 orders above observed.
#
# Two interpretations:
# A) rho_Lambda = rho_GGE_GeV4 = 4.9e+66 (framework value, QFIELD-43 FAIL)
# B) rho_Lambda = rho_obs = 2.8e-47 (observed, framework cannot compute)
#
# For the RATIO Omega_DM/Omega_Lambda, interpretation matters:

print("\n--- Interpretation A: Framework rho_Lambda = rho_GGE ---")
# Both DM and Lambda come from the same GGE energy.
# The DM is the oscillating part, Lambda is the constant part.
# Paper 35 key insight: delta_q oscillations have w=0, while
# constant q has w=-1. The RATIO depends on the partitioning.

# The GGE energy is E_exc = 50.9 M_KK total.
# Of this, how much oscillates (DM) vs sits constant (DE)?
#
# In BCS theory: the quasiparticle energy has two components:
#   E_k = sqrt(epsilon_k^2 + Delta^2)
# where epsilon_k is the kinetic energy and Delta is the gap.
# The gap part is the condensation energy (contributes to Lambda).
# The kinetic part oscillates (contributes to DM).
#
# Post-transit (S38): condensate is destroyed (P_exc = 1.000).
# ALL energy is in quasiparticles. There is no condensate.
# So the split is:
#   DM component: kinetic/oscillation part of E_exc
#   DE component: "vacuum energy" from being in a non-equilibrium state
#
# In the GGE picture: the conserved integrals fix the distribution.
# The GGE density matrix rho_GGE = exp(-sum_i lambda_i I_i) / Z
# where I_i are the Richardson-Gaudin integrals (8 of them, S38).
#
# The "vacuum energy" (w=-1) part is the part that does not dilute.
# The "matter" (w=0) part dilutes as a^{-3}.
#
# For a free field: E_total = sum_k n_k omega_k
# All of this is "matter" (w=0) -- it all dilutes as a^{-3}.
# There is no w=-1 component from free quasiparticles.
#
# The w=-1 component must come from the q-field ZERO MODE.
# In Paper 35: the homogeneous part of q (constant in space)
# contributes to Lambda, while the fluctuations contribute to DM.
#
# In the framework: after transit, tau=0 (ground state).
# The q-field (tau) has returned to its equilibrium value.
# There is NO homogeneous q-perturbation.
# ALL q-perturbation energy is in MODES (quasiparticles).
# Therefore: ALL GGE energy is DM (w=0), not DE (w=-1).

# This means rho_Lambda = 0 from the q-field (equilibrium)
# and rho_DM = rho_GGE = E_exc * prefactor * M_KK^4.
# But then we have NO cosmological constant at all!
# This is the q-theory equilibrium theorem: Lambda=0 exactly.
# The "residual" from W1-1 is NOT Lambda but rho_matter.

# Let's compute the ratio properly:
# If ALL GGE is matter (w=0):
rho_DM_GGE_MKK4 = E_exc_MKK * prefactor
rho_DM_GGE_GeV4 = rho_DM_GGE_MKK4 * M_KK_grav**4

print(f"  If ALL GGE is DM (w=0, no condensate):")
print(f"    rho_DM = E_exc * prefactor * M_KK^4 = {rho_DM_GGE_GeV4:.3e} GeV^4")
print(f"    rho_Lambda = 0 (q-theory equilibrium)")
print(f"    Omega_DM / Omega_Lambda = UNDEFINED (Lambda=0)")
print(f"    This is the q-theory equilibrium theorem.")

# However: Paper 05 says rho_Lambda ~ rho_matter for an imperfect vacuum.
# If rho_Lambda tracks rho_DM: Omega_DM / Omega_Lambda ~ 1.
# This is the coincidence problem solution!

print(f"\n--- Interpretation B: Paper 05 Coincidence Mechanism ---")
print(f"  Paper 05: rho_Lambda ~ rho_matter (at any epoch)")
print(f"  If rho_Lambda = alpha * rho_DM where alpha ~ O(1):")
print(f"    Omega_DM / Omega_Lambda = 1/alpha ~ O(1)")
print(f"    This IS Paper 35's prediction of DM/DE ~ 3.")

# Let's compute what Paper 35's formula gives directly.
# Paper 35: Omega_DM/Omega_Lambda ~ <(d_t delta_q)^2> / Lambda
#
# The key: Lambda in Paper 35 is NOT the framework's GGE energy.
# Paper 35 assumes Lambda is the OBSERVED tiny CC (set by K^3/M_Pl^2).
# The framework has NOT achieved this suppression (QFIELD-43 FAIL).
#
# So we must use the framework's actual numbers and see what happens.

print(f"\n--- Interpretation C: Framework Numbers (Direct Computation) ---")

# The two DM sources are:
# 1. GGE quasiparticles: ALL internal-space excitations
#    These have w=0 because they carry no spatial momentum.
#    rho_DM_1 = E_exc * prefactor * M_KK^4
# 2. Q-field perturbations: spatial fluctuations of tau
#    These also have w=0 when oscillating at omega_q >> H.
#    rho_DM_2 = (1/2) omega_q^2 <delta_tau^2> * prefactor * M_KK^4

rho_DM_source1 = rho_DM_GGE_GeV4  # GGE quasiparticles
rho_DM_source2 = rho_DM_qfield_GeV4  # q-field oscillations

print(f"  Source 1 (GGE quasiparticles): {rho_DM_source1:.3e} GeV^4")
print(f"  Source 2 (q-field oscillations): {rho_DM_source2:.3e} GeV^4")
print(f"  Source 2/Source 1 = {rho_DM_source2/rho_DM_source1:.3e}")
print(f"  Source 2 is {np.log10(rho_DM_source1/rho_DM_source2):.1f} orders SMALLER than Source 1")

rho_DM_total = rho_DM_source1 + rho_DM_source2
print(f"\n  Total rho_DM = {rho_DM_total:.3e} GeV^4")
print(f"  Dominated by Source 1 (GGE quasiparticles)")

# For Omega_DM / Omega_Lambda:
# The problem is what to use for rho_Lambda.
# Three options:
# (i) rho_Lambda = rho_GGE (same as rho_DM) -> ratio = 1 (but then Lambda is not w=-1)
# (ii) rho_Lambda = rho_obs = 2.8e-47 -> ratio = huge (W1-1: 113 orders mismatch)
# (iii) Paper 35: rho_Lambda = tiny residual from self-tuning

print(f"\n  Omega_DM / Omega_Lambda for different Lambda sources:")
print(f"  (i)   Lambda = GGE: ratio = {rho_DM_total / rho_GGE_GeV4:.6f} (essentially 1)")
print(f"        But this conflates DM and DE.")
print(f"  (ii)  Lambda = observed: ratio = {rho_DM_total / rho_Lambda_obs:.3e}")
print(f"        {np.log10(rho_DM_total / rho_Lambda_obs):.0f} orders overshoot.")
print(f"        Observed ratio = {Omega_DM_obs / Omega_Lambda_obs:.3f}")
print(f"  (iii) Paper 35 self-consistent: DM/DE ~ 3 BY CONSTRUCTION")
print(f"        (if the CC suppression mechanism works)")

# ===========================================================================
# STEP 5: Two-Source Budget
# ===========================================================================
print("\n" + "=" * 72)
print("STEP 5: Two-Source Dark Matter Budget")
print("=" * 72)

# Source 1: GGE quasiparticles (internal excitations)
# 59.8 pairs, E_exc = 50.9 M_KK
# These are the BCS quasiparticles that survive post-transit.
# Their effective mass is M_DM ~ 2.1 M_KK (from S42 DM profile).
# Number density: n_GGE = n_pairs * n_crystals (per unit volume)
#   where n_crystals = 1 per coherence volume = 1 / xi_KZ^3

# Energy per quasiparticle pair
E_per_pair = E_exc_MKK / n_pairs
print(f"\n--- Source 1: GGE Quasiparticle Relic ---")
print(f"  n_pairs = {n_pairs}")
print(f"  E_exc = {E_exc_MKK:.3f} M_KK")
print(f"  E per pair = {E_per_pair:.4f} M_KK")
print(f"  M_DM = {M_DM_MKK:.4f} M_KK (effective DM mass, S42)")
print(f"  Delta_pair = {Delta_pair_MKK:.4f} M_KK")

# The mass of one KZ domain = n_pairs * E_per_pair
# Domain size = xi_KZ = 0.152 M_KK^{-1} (in internal space)
# But we need the 4D mass per domain:
M_domain = E_exc_MKK  # total energy per domain
print(f"  M_domain = E_exc = {M_domain:.3f} M_KK = {M_domain * M_KK_grav:.3e} GeV")
print(f"  In solar masses: {M_domain * M_KK_grav * 1e9 * 1.783e-33 / 1.989e33:.3e} M_sun")
# That's a mass ~ 10^{-19} solar masses per KZ domain = primordial microhalo

# Source 2: Q-field (tau) spatial fluctuations
print(f"\n--- Source 2: Q-Field Spatial Perturbations ---")
print(f"  omega_q = {omega_q:.4f} M_KK")
print(f"  <delta_q^2> = {delta_q_sq_total:.6f} M_KK^{{-1}}")
print(f"  rho_DM(q) = {rho_DM_qfield_MKK4:.6e} M_KK^4")
print(f"  rho_DM(q) = {rho_DM_qfield_GeV4:.3e} GeV^4")

# Ratio
r_sources = rho_DM_source2 / rho_DM_source1
print(f"\n--- Budget ---")
print(f"  Source 1 (GGE):        {rho_DM_source1:.3e} GeV^4 ({1/(1+r_sources)*100:.4f}%)")
print(f"  Source 2 (q-field):    {rho_DM_source2:.3e} GeV^4 ({r_sources/(1+r_sources)*100:.4f}%)")
print(f"  Total:                 {rho_DM_total:.3e} GeV^4 (100%)")
print(f"  Source 1 dominates by {np.log10(1/r_sources):.1f} orders")
print(f"  Source 2 is NEGLIGIBLE (quantum fluctuation of tau)")

# ===========================================================================
# STEP 6: Paper 35 Oscillation Amplification Diagnostic
# ===========================================================================
print("\n" + "=" * 72)
print("STEP 6: Paper 35 Oscillation Amplification & Jeans Scale")
print("=" * 72)

# omega_q = effective mass of q-field perturbation
# At what scale do q-perturbations become gravitationally unstable?
# Jeans wavenumber: k_J = sqrt(4 pi G rho_bg) / c_q
# Jeans length: lambda_J = 2 pi / k_J = 2 pi c_q / sqrt(4 pi G rho_bg)

# For the q-field: the Jeans analysis gives the scale below which
# q-oscillations cluster gravitationally.
# In natural units: k_J^2 = omega_q^2 / c_q^2 - (k_compton)^2
# where k_compton = omega_q / c (from the mass)
# Actually, the Jeans instability for a massive scalar field:
# Perturbation stable if k > k_J where k_J^2 = 4 pi G rho_bg a^2 / c_q^2

# The Compton wavelength of the q-field:
lambda_compton = 1.0 / omega_q  # M_KK^{-1}
lambda_compton_cm = lambda_compton * L_MKK_cm
lambda_compton_Mpc = lambda_compton_cm / 3.086e24

print(f"\nCompton wavelength of q-field:")
print(f"  lambda_C = 1/omega_q = {lambda_compton:.6f} M_KK^{{-1}}")
print(f"  lambda_C = {lambda_compton_cm:.3e} cm")
print(f"  lambda_C = {lambda_compton_Mpc:.3e} Mpc")
print(f"  This is ~ {lambda_compton_Mpc/8.8e-14:.0e} x Planck length")

# Free-streaming length: for massive particles with w=0 and v << c
# lambda_fs = v / H_0 where v is the velocity dispersion
# For q-field oscillations: v ~ c_q * (k/omega_q) ~ c_q / omega_q for k~omega_q
# This gives v ~ 1/M_KK in natural units -> essentially zero

v_q = c_q / omega_q  # velocity in units of c (M_KK units cancel)
# Wait: c_q is in M_KK units but has dimension of speed.
# c_q = sqrt(Z/M) has dimensions [M_KK^4 / M_KK^2]^{1/2} = M_KK.
# The velocity v = c_q * (k/omega_q). For k ~ 1/xi_KZ:
k_KZ = 1.0 / xi_KZ  # M_KK
v_streaming = c_q * k_KZ / omega_q  # dimensionless (in units of c)

print(f"\nFree-streaming:")
print(f"  c_q = {c_q:.2f} M_KK (propagation speed)")
print(f"  k_KZ = 1/xi_KZ = {k_KZ:.2f} M_KK")
print(f"  v_fs = c_q * k_KZ / omega_q = {v_streaming:.4f} c")
print(f"  This is a WARM dark matter velocity: v ~ {v_streaming * 3e10:.3e} cm/s")

# Free-streaming length
lambda_fs = v_streaming * c_light / H_0_Hz  # cm
lambda_fs_Mpc = lambda_fs / 3.086e24
print(f"  lambda_fs = v/H_0 = {lambda_fs:.3e} cm = {lambda_fs_Mpc:.3e} Mpc")

# From S42: lambda_fs was computed as 3.1e-48 Mpc (essentially zero)
# That used a different velocity estimate. Our estimate here uses
# c_q ~ 210 and omega_q ~ 400, giving v ~ 210 * 6.6 / 400 ~ 3.5
# This seems unphysically large. Let's re-examine.
#
# Actually, v_streaming should use the PHYSICAL velocity, not the
# internal-space velocity. The q-field perturbations in 4D:
# c_q_4D = c_q * (M_KK / M_Pl) for KK modes
# KK modes propagate at c_4D = v_internal * (L_internal / L_4D)
# Since L_internal ~ M_KK^{-1} << L_4D, the effective 4D propagation
# speed of internal perturbations is SUPPRESSED by M_KK/M_Pl.

c_q_4D = c_q * (M_KK_grav / M_Pl_GeV)  # dimensionless ratio * M_KK
v_fs_4D = c_q_4D * k_KZ / omega_q  # dimensionless
lambda_fs_4D_cm = v_fs_4D * c_light / H_0_Hz
lambda_fs_4D_Mpc = lambda_fs_4D_cm / 3.086e24

print(f"\n  KK suppression: c_q_4D = c_q * M_KK/M_Pl = {c_q_4D:.6f}")
print(f"  v_fs_4D = {v_fs_4D:.3e} c")
print(f"  lambda_fs_4D = {lambda_fs_4D_Mpc:.3e} Mpc")
print(f"  Classification: {'CDM' if lambda_fs_4D_Mpc < 0.1 else 'WDM' if lambda_fs_4D_Mpc < 10 else 'HDM'}")

# The Jeans mass for the q-field:
# M_J ~ (4/3) pi rho_DM * (lambda_J/2)^3
# For CDM (lambda_fs << Mpc), structures form at all scales.

# Paper 35 oscillation amplification:
# omega_q * t_age >> 1 means many oscillations have occurred.
# t_age ~ 1/H_0 ~ 4.6e17 s
t_age_s = 1.0 / H_0_Hz  # ~ 4.6e17 s
omega_q_Hz_eff = omega_q * M_KK_grav * 1e9 / hbar_eVs  # in Hz
N_oscillations = omega_q_Hz_eff * t_age_s / (2 * np.pi)

print(f"\nOscillation count:")
print(f"  omega_q = {omega_q_Hz_eff:.3e} Hz")
print(f"  t_age = {t_age_s:.3e} s")
print(f"  N_osc = omega_q * t_age / (2 pi) = {N_oscillations:.3e}")
print(f"  >> 1: q-field well-averaged. w = 0 is accurate.")

# ===========================================================================
# STEP 7: The Actual DM/DE Ratio (Gate Computation)
# ===========================================================================
print("\n" + "=" * 72)
print("STEP 7: Gate Computation -- Omega_DM / Omega_Lambda")
print("=" * 72)

# The critical question: what is the framework's prediction for
# Omega_DM / Omega_Lambda?
#
# CASE 1: Pure GGE (no CC suppression)
# If ALL GGE energy is DM (w=0), there is no DE (w=-1).
# Omega_DM / Omega_Lambda is undefined or infinite.
# This FAILS cosmologically (no acceleration).
#
# CASE 2: Paper 05 + Paper 35 self-consistent picture
# rho_Lambda ~ rho_matter (coincidence solution)
# Omega_DM / Omega_Lambda ~ O(1)
# Paper 35: DM/DE ~ 3 without fine-tuning
# But this requires the CC suppression to WORK, which QFIELD-43 showed it doesn't.
#
# CASE 3: Framework's actual numbers
# rho_DM = rho_GGE (all quasiparticles)
# rho_Lambda = ??? (framework cannot compute; CC problem unsolved)
#
# The gate asks: Omega_DM / Omega_Lambda > 0.03?
# We must compute this with the framework's own numbers.
#
# The closest the framework can get:
# If q-theory self-tuning partially works (removes S(0) but not GGE),
# then rho_Lambda = rho_GGE = rho_DM (both from same source).
# Omega_DM / Omega_Lambda would be 1.0 by construction.
#
# But this is wrong: the GGE energy is either DM or DE, not both.
# The split depends on whether quasiparticles gravitate as w=0 or w=-1.
#
# S38 established: post-transit, GGE has n_pairs excited quasiparticles
# that NEVER thermalize. Their equation of state:
# - Massive particles with M >> T: w = 0 (dust)
# - They carry internal quantum numbers, not spatial momentum
# - They are pressureless: P = 0 -> w = 0
#
# Therefore: ALL GGE energy is DM, and Lambda = 0 (by q-theory).
# The ratio is infinite (all DM, no DE).
# This fails the cosmological requirement for acceleration.

# The ONLY way to get a finite ratio is if some of the GGE energy
# is "locked" as vacuum energy (w=-1). This requires:
# - A remnant condensate (but S38 says P_exc=1.000: NO condensate)
# - A topological term (but BDI winding=0 post-transit)
# - A boundary/Casimir contribution (Paper 05 source 4)
#
# Let's compute the Casimir contribution (Paper 05):
# For a domain of size xi_KZ, the Casimir energy is:
# E_Cas ~ n_modes * pi / (2 * xi_KZ) per spatial dimension
# This is a w=-1/3 contribution (radiation), not w=-1.

# Actually, the most natural split follows Paper 35 directly.
# Paper 35: rho_total = rho_q0 + rho_delta_q
# where rho_q0 = V(q_0) = the potential at equilibrium (= 0 by q-theory)
# and rho_delta_q = (1/2)<(d_t delta_q)^2 + ...>
# The ENTIRE delta_q energy is DM (w=0).
# Lambda comes from rho_q0 = 0.
#
# Paper 35's "DM/DE ~ 3" was computed assuming a SPECIFIC
# mechanism sets rho_Lambda ~ (K_QCD^3 / M_Pl^2). In the framework,
# this mechanism fails (QFIELD-43). So we cannot use Paper 35's ratio.

# Final numbers:
print(f"\n--- Framework Prediction ---")
print(f"  rho_DM (GGE, all quasiparticles) = {rho_DM_total:.3e} GeV^4")
print(f"  rho_Lambda (q-theory: equilibrium) = 0 (by theorem)")
print(f"  Omega_DM / Omega_Lambda = UNDEFINED (0/0 or inf)")

# But what if we IMPOSE the observed Lambda?
Omega_ratio_imposed = rho_DM_total / rho_Lambda_obs
print(f"\n  If we impose observed rho_Lambda:")
print(f"    Omega_DM/Omega_Lambda = {Omega_ratio_imposed:.3e}")
print(f"    {np.log10(Omega_ratio_imposed):.1f} orders above observed ratio ({Omega_DM_obs/Omega_Lambda_obs:.3f})")

# What if we use the S42 DM energy per crystal?
E_DM_fraction = E_DM_per_crystal / E_exc_MKK
print(f"\n  S42 DM per crystal: {E_DM_per_crystal:.3f} M_KK")
print(f"    Fraction of E_exc: {E_DM_fraction*100:.1f}%")
print(f"    This was the S42 estimate that gave Omega_DM/Omega_b ~ 2e4")

# The key structural result:
# In the framework, DM and Lambda CANNOT be separated at this level.
# The GGE energy is a SINGLE pool of excitation energy.
# Whether it acts as DM (w=0) or DE (w=-1) depends on DYNAMICS
# that the framework cannot yet compute (it requires knowing how
# the GGE couples to 4D gravity, which requires the full KK reduction).
#
# What we CAN compute is the RATIO of DM energy to total GGE energy.
# This is the fraction that acts as w=0:

# If quasiparticles are massive (E > Delta): w=0 (pressureless matter)
# Their kinetic energy is negligible compared to rest mass.
# fraction_DM = 1 - fraction_Lambda
# Since P_exc=1 (no condensate), ALL are quasiparticles: fraction_DM = 1.

# BUT: Paper 05 says the vacuum RESPONDS to the matter.
# If rho_DM >> rho_Lambda, the vacuum adjusts until rho_Lambda ~ rho_DM.
# This gives Omega_DM / Omega_Lambda ~ 1 automatically.
# This IS the Paper 05 coincidence solution.

# Let's compute the Paper 05 response:
# rho_Lambda(response) ~ (rho_DM)^2 / (chi_q * M_KK^4)
# where chi_q = d^2 V/dq^2 = curvature of the vacuum potential
chi_q_MKK4 = chi_q_0  # M_KK^4
rho_DM_MKK4 = rho_DM_GGE_MKK4  # M_KK^4
rho_Lambda_response = rho_DM_MKK4**2 / chi_q_MKK4  # M_KK^4
rho_Lambda_response_GeV4 = rho_Lambda_response * M_KK_grav**4

print(f"\n--- Paper 05 Vacuum Response ---")
print(f"  chi_q = {chi_q_MKK4:.2f} M_KK^4")
print(f"  rho_DM = {rho_DM_MKK4:.6f} M_KK^4")
print(f"  rho_Lambda(response) = rho_DM^2/chi_q = {rho_Lambda_response:.6e} M_KK^4")
print(f"  rho_Lambda(response) = {rho_Lambda_response_GeV4:.3e} GeV^4")

Omega_ratio_response = rho_DM_MKK4 / rho_Lambda_response
print(f"  Omega_DM/Omega_Lambda = rho_DM / rho_Lambda = {Omega_ratio_response:.2e}")
print(f"  This is {Omega_ratio_response:.0f}, much larger than observed 0.39.")
print(f"  chi_q is TOO LARGE: {chi_q_MKK4:.0f} >> rho_DM = {rho_DM_MKK4:.6f}")
print(f"  This means the vacuum is TOO STIFF to respond significantly.")

# The ACTUAL ratio using Paper 35's formula:
# Omega_DM/Omega_Lambda = <kinetic energy of delta_q> / V(q_0)
# Since V(q_0) = 0 (equilibrium), the ratio is undefined.
#
# Paper 35's trick: V(q_0) is NOT exactly zero but ~ K^3/M_Pl^2.
# This sets rho_Lambda and makes the ratio finite.
# In the framework: M_KK replaces K_QCD, so
# rho_Lambda ~ M_KK^6 / M_Pl^2 (Paper 16 formula)
rho_Lambda_KV = M_KK_grav**6 / M_Pl_GeV**2  # GeV^4
Omega_ratio_KV = rho_DM_total / rho_Lambda_KV

print(f"\n--- Paper 16 dimensional estimate for Lambda ---")
print(f"  rho_Lambda = M_KK^6/M_Pl^2 = {rho_Lambda_KV:.3e} GeV^4")
print(f"  Omega_DM/Omega_Lambda = {Omega_ratio_KV:.6f}")

# This is the most self-consistent estimate.
# Paper 35 gives DM/DE ~ 3 when the hierarchy K<<M_Pl is large.
# Here M_KK/M_Pl ~ 0.006 (only 2.2 orders), so the ratio is ~1e-4.

# Let's also try with BCS gap as the scale:
rho_Lambda_BCS = (Delta_pair_MKK * M_KK_grav)**6 / M_Pl_GeV**2
Omega_ratio_BCS = rho_DM_total / rho_Lambda_BCS

print(f"\n  With BCS gap scale: Delta * M_KK = {Delta_pair_MKK * M_KK_grav:.3e} GeV")
print(f"  rho_Lambda = (Delta*M_KK)^6/M_Pl^2 = {rho_Lambda_BCS:.3e} GeV^4")
print(f"  Omega_DM/Omega_Lambda = {Omega_ratio_BCS:.6f}")

# ===========================================================================
# STEP 8: Summary and Gate Verdict
# ===========================================================================
print("\n" + "=" * 72)
print("STEP 8: Summary and Gate Verdict")
print("=" * 72)

# All estimates for Omega_DM/Omega_Lambda:
estimates = {
    'Pure q-theory (Lambda=0)': np.inf,
    'Paper 05 response': float(Omega_ratio_response),
    'Paper 16 dimensional (M_KK)': float(Omega_ratio_KV),
    'Paper 16 dimensional (BCS)': float(Omega_ratio_BCS),
    'Imposed observed Lambda': float(Omega_ratio_imposed),
    'Paper 35 self-consistent': 3.0,  # By construction
}

print(f"\n{'Estimate':<40s} {'Omega_DM/Omega_Lambda':>25s} {'log10':>8s}")
print("-" * 75)
for name, val in estimates.items():
    if np.isinf(val):
        print(f"{name:<40s} {'INFINITY':>25s} {'INF':>8s}")
    else:
        print(f"{name:<40s} {val:>25.6e} {np.log10(val):>8.1f}")
print(f"{'Observed':<40s} {Omega_DM_obs/Omega_Lambda_obs:>25.6f} {np.log10(Omega_DM_obs/Omega_Lambda_obs):>8.3f}")

# Gate verdict
# The physically meaningful estimate is Paper 16 dimensional
# because it uses the framework's own scale hierarchy.
# Omega_DM/Omega_Lambda ~ rho_DM / (M_KK^6/M_Pl^2)

# Final adopted value
Omega_ratio_final = Omega_ratio_KV
print(f"\n--- Adopted Value ---")
print(f"Omega_DM/Omega_Lambda = {Omega_ratio_final:.6e}")

if Omega_ratio_final > 0.03:
    gate_verdict = "PASS"
elif Omega_ratio_final > 0.001:
    gate_verdict = "INTERMEDIATE"
else:
    gate_verdict = "FAIL"

print(f"\n{'='*72}")
print(f"GATE VERDICT: GGE-DM-43 = {gate_verdict}")
print(f"{'='*72}")
print(f"\nPre-registered criteria:")
print(f"  PASS: Omega_DM/Omega_Lambda > 0.03")
print(f"  FAIL: < 0.001")
print(f"  INTERMEDIATE: 0.001 to 0.03")
print(f"\nResult: Omega_DM/Omega_Lambda = {Omega_ratio_final:.6e}")
print(f"  This is {'>' if Omega_ratio_final > 0.001 else '<'} 0.001")
print(f"  This is {'>' if Omega_ratio_final > 0.03 else '<'} 0.03")

print(f"\n--- Physical Interpretation ---")
print(f"1. ALL GGE energy is DM (w=0): quasiparticles are pressureless.")
print(f"   rho_DM = {rho_DM_total:.3e} GeV^4 (59.8 pairs, E=50.9 M_KK).")
print(f"2. Q-field perturbations (Source 2) are negligible:")
print(f"   rho_DM_q = {rho_DM_source2:.3e} GeV^4 ({np.log10(rho_DM_source1/rho_DM_source2):.0f} orders below GGE).")
print(f"3. Lambda = 0 by q-theory equilibrium (Paper 05 theorem).")
print(f"   The observed Lambda remains unexplained by the framework.")
print(f"4. Using Paper 16 dimensional estimate for Lambda:")
print(f"   rho_Lambda ~ M_KK^6/M_Pl^2 = {rho_Lambda_KV:.3e} GeV^4.")
print(f"   Omega_DM/Omega_Lambda = {Omega_ratio_KV:.6e}.")
print(f"   The ratio is {Omega_DM_obs/Omega_Lambda_obs / Omega_ratio_KV:.0e}x below observed.")
print(f"5. The 2000x shortfall from S42 was an underestimate.")
print(f"   With corrected q-theory: {1/Omega_ratio_KV:.0e}x below observed.")
print(f"6. Root cause: M_KK/M_Pl hierarchy is only 2 orders.")
print(f"   Paper 35 needs K << M_Pl (QCD: 17 orders). Framework: 2 orders.")
print(f"7. Paper 05 coincidence mechanism: rho_Lambda ~ rho_DM BY CONSTRUCTION")
print(f"   if the CC suppression mechanism works. But QFIELD-43 = FAIL.")

# ===========================================================================
# PLOTS
# ===========================================================================
print("\n" + "=" * 72)
print("Generating plots...")
print("=" * 72)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'GGE-DM-43: Dark Matter Abundance via Q-Theory\n'
             f'Gate: {gate_verdict} | Omega_DM/Omega_Lambda = {Omega_ratio_final:.2e}',
             fontsize=13, fontweight='bold')

# Panel 1: Two-source budget (bar chart)
ax = axes[0, 0]
labels = ['GGE\nquasiparticles', 'Q-field\noscillations', 'Total DM']
vals = [np.log10(rho_DM_source1), np.log10(rho_DM_source2), np.log10(rho_DM_total)]
colors = ['#1565c0', '#e65100', '#2e7d32']
bars = ax.bar(labels, vals, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
ax.axhline(np.log10(rho_DM_obs), color='red', linestyle='--', linewidth=2, label='Observed $\\rho_{DM}$')
ax.axhline(np.log10(rho_Lambda_obs), color='green', linestyle=':', linewidth=2, label='Observed $\\Lambda$')
for bar, val in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width()/2., val + 1, f'{val:.0f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax.set_ylabel('log$_{10}(\\rho$ / GeV$^4)$')
ax.set_title('Two-Source DM Budget')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# Panel 2: Omega_DM/Omega_Lambda estimates
ax = axes[0, 1]
est_names = ['Paper 05\nresponse', 'Paper 16\n(M_KK)', 'Paper 16\n(BCS)', 'Paper 35\nself-cons.', 'Observed']
est_vals = [np.log10(Omega_ratio_response), np.log10(Omega_ratio_KV),
            np.log10(Omega_ratio_BCS), np.log10(3.0),
            np.log10(Omega_DM_obs/Omega_Lambda_obs)]
est_colors = ['#7b1fa2', '#1565c0', '#e65100', '#2e7d32', '#d32f2f']
bars = ax.bar(est_names, est_vals, color=est_colors, alpha=0.8, edgecolor='black', linewidth=0.5)
ax.axhline(np.log10(0.03), color='green', linestyle='--', alpha=0.7, label='PASS threshold')
ax.axhline(np.log10(0.001), color='orange', linestyle='--', alpha=0.7, label='FAIL threshold')
ax.axhline(np.log10(Omega_DM_obs/Omega_Lambda_obs), color='red', linewidth=2, linestyle='-', alpha=0.7, label='Observed')
for bar, val in zip(bars, est_vals):
    ax.text(bar.get_x() + bar.get_width()/2., val + 0.3, f'{val:.1f}',
            ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.set_ylabel('log$_{10}(\\Omega_{DM}/\\Omega_{\\Lambda})$')
ax.set_title('DM/DE Ratio Estimates')
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3, axis='y')

# Panel 3: M_KK/M_Pl hierarchy and Paper 35 prediction
ax = axes[0, 2]
hierarchy = np.logspace(-20, 0, 500)  # K/M_Pl ratio
# Paper 35: Omega_DM/Omega_Lambda ~ 1 / (K/M_Pl)^4 * (rho_DM / M_Pl^4)
# Actually: rho_Lambda ~ K^3/M_Pl^2, rho_DM ~ K^4 (condensation energy scale)
# So Omega_DM/Omega_Lambda ~ K^4 / (K^3/M_Pl^2) = K * M_Pl^2
# Paper 35: ratio ~ 3 when K ~ K_QCD, which means K/M_Pl ~ 10^{-17}
# and rho_DM/rho_Lambda ~ K * M_Pl^2 / M_Pl^3 = K/M_Pl ~ 10^{-17}
# That gives ratio ~ 10^{-17}, not 3.
#
# Actually Paper 35's formula is more nuanced. Let me use:
# rho_DM ~ omega_q^2 * <delta_q^2> and rho_Lambda ~ K^3/M_Pl^2
# For the scaling: DM/DE ~ (K/M_Pl)^{-2} * something
# Let's just plot the framework's position vs QCD

K_over_MPl_QCD = 0.44**2 / M_Pl_GeV  # ~ 1.6e-20
K_over_MPl_fw = M_KK_grav / M_Pl_GeV   # ~ 6e-3
K_over_MPl_BCS = Delta_pair_MKK * M_KK_grav / M_Pl_GeV

ax.axvline(np.log10(K_over_MPl_QCD), color='blue', linewidth=2, label=f'QCD ($K/M_{{Pl}}$={K_over_MPl_QCD:.1e})')
ax.axvline(np.log10(K_over_MPl_fw), color='red', linewidth=2, label=f'Framework ($M_{{KK}}/M_{{Pl}}$={K_over_MPl_fw:.1e})')
ax.axvline(np.log10(K_over_MPl_BCS), color='orange', linewidth=2, label=f'BCS gap ({K_over_MPl_BCS:.1e})')
ax.axhline(np.log10(3.0), color='green', linestyle='--', alpha=0.5, label='DM/DE ~ 3 (Paper 35)')
ax.axhline(np.log10(Omega_ratio_KV), color='red', linestyle='--', alpha=0.5, label=f'Framework: {Omega_ratio_KV:.1e}')
ax.set_xlabel('log$_{10}(K/M_{Pl})$')
ax.set_ylabel('log$_{10}(\\Omega_{DM}/\\Omega_{\\Lambda})$')
ax.set_title('Scale Hierarchy Dependence')
ax.set_xlim([-22, 0])
ax.legend(fontsize=7, loc='upper left')
ax.grid(True, alpha=0.3)

# Panel 4: Q-field perturbation spectrum
ax = axes[1, 0]
k_modes = np.arange(1, 61)
omega_k = np.sqrt(omega_q**2 + c_q**2 * (k_modes * 2 * np.pi / xi_KZ)**2)
# Not physical (k is not a spatial wavenumber), but shows the internal spectrum
rho_k = 0.5 / omega_k  # vacuum fluctuation per mode
ax.semilogy(k_modes, omega_k, 'b-o', markersize=3, linewidth=1.5, label='$\\omega_k$')
ax.set_xlabel('Mode number $k$')
ax.set_ylabel('$\\omega_k$ [M$_{KK}$]')
ax.set_title('Q-Field Mode Spectrum')
ax2 = ax.twinx()
ax2.semilogy(k_modes, rho_k, 'r--', linewidth=1, alpha=0.7, label='$\\langle\\delta q_k^2\\rangle$')
ax2.set_ylabel('$\\langle\\delta q^2\\rangle_k$ [M$_{KK}^{-1}$]', color='red')
ax.legend(fontsize=8, loc='center left')
ax2.legend(fontsize=8, loc='center right')
ax.grid(True, alpha=0.3)

# Panel 5: Energy budget pie chart
ax = axes[1, 1]
# Split the GGE energy into components
E_kinetic = E_exc_MKK - n_pairs * Delta_pair_MKK  # kinetic part
E_pair = n_pairs * Delta_pair_MKK  # pair energy part
sizes = [max(E_kinetic, 0), E_pair, abs(E_cond_MKK)]
labels_pie = [f'Kinetic\n{max(E_kinetic,0):.1f} M_KK',
              f'Pair energy\n{E_pair:.1f} M_KK',
              f'Condensation\n{abs(E_cond_MKK):.3f} M_KK']
colors_pie = ['#1565c0', '#e65100', '#2e7d32']
if E_kinetic < 0:
    sizes = [E_exc_MKK, abs(E_cond_MKK)]
    labels_pie = [f'GGE excitation\n{E_exc_MKK:.1f} M_KK',
                  f'|E_cond|\n{abs(E_cond_MKK):.3f} M_KK']
    colors_pie = ['#1565c0', '#2e7d32']
wedges, texts, autotexts = ax.pie(sizes, labels=labels_pie, colors=colors_pie,
                                   autopct='%1.1f%%', startangle=90,
                                   textprops={'fontsize': 8})
ax.set_title('GGE Energy Budget')

# Panel 6: Summary text
ax = axes[1, 2]
ax.axis('off')
summary_text = [
    f"GATE VERDICT: {gate_verdict}",
    "=" * 45,
    "",
    "Two-Source DM Budget:",
    f"  GGE qp:    {rho_DM_source1:.1e} GeV^4 (dominant)",
    f"  Q-field:   {rho_DM_source2:.1e} GeV^4 (negligible)",
    f"  Total:     {rho_DM_total:.1e} GeV^4",
    "",
    "Lambda Estimates:",
    f"  Q-theory:  0 (equilibrium theorem)",
    f"  Paper 16:  {rho_Lambda_KV:.1e} GeV^4",
    f"  Observed:  {rho_Lambda_obs:.1e} GeV^4",
    "",
    "Omega_DM/Omega_Lambda:",
    f"  Paper 16:  {Omega_ratio_KV:.2e}",
    f"  Observed:  {Omega_DM_obs/Omega_Lambda_obs:.3f}",
    f"  Shortfall: {(Omega_DM_obs/Omega_Lambda_obs)/Omega_ratio_KV:.0e}x",
    "",
    "Root Cause:",
    f"  M_KK/M_Pl = {M_KK_grav/M_Pl_GeV:.3e} (2 orders)",
    f"  Paper 35 needs K<<M_Pl (QCD: 17 orders)",
    f"  Only 2 orders -> ratio suppressed by 10^4",
    "",
    "Q-field diagnostics:",
    f"  omega_q = {omega_q:.2f} M_KK ({omega_q_Hz_eff:.1e} Hz)",
    f"  N_osc = {N_oscillations:.1e} >> 1 (w=0 valid)",
    f"  lambda_fs = {lambda_fs_4D_Mpc:.1e} Mpc (CDM)",
]
ax.text(0.05, 0.95, '\n'.join(summary_text), transform=ax.transAxes,
        fontsize=8.5, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('tier0-computation/s43_gge_dm_abundance.png', dpi=150, bbox_inches='tight')
print("Plot saved: tier0-computation/s43_gge_dm_abundance.png")

# ===========================================================================
# SAVE DATA
# ===========================================================================
print("\nSaving data...")

save_dict = {
    # Input parameters
    'M_KK_grav': np.array(M_KK_grav),
    'M_KK_gauge': np.array(M_KK_gauge),
    'M_Pl_GeV': np.array(M_Pl_GeV),
    'E_exc_MKK': np.array(E_exc_MKK),
    'E_cond_MKK': np.array(E_cond_MKK),
    'n_pairs': np.array(n_pairs),
    'Delta_pair_MKK': np.array(Delta_pair_MKK),

    # Q-field parameters
    'chi_q_0': np.array(chi_q_0),
    'omega_q': np.array(omega_q),
    'omega_q_Hz': np.array(omega_q_Hz_eff),
    'm_q_GeV': np.array(m_q_eff_GeV),
    'c_q': np.array(c_q),
    'c_q_4D': np.array(c_q_4D),
    'Z_fold': np.array(Z_fold),

    # DM sources
    'rho_DM_GGE_GeV4': np.array(rho_DM_source1),
    'rho_DM_qfield_GeV4': np.array(rho_DM_source2),
    'rho_DM_total_GeV4': np.array(rho_DM_total),
    'rho_DM_GGE_MKK4': np.array(rho_DM_GGE_MKK4),
    'rho_DM_qfield_MKK4': np.array(rho_DM_qfield_MKK4),

    # Lambda estimates
    'rho_Lambda_qtheory': np.array(0.0),  # equilibrium theorem
    'rho_Lambda_KV': np.array(rho_Lambda_KV),
    'rho_Lambda_BCS': np.array(rho_Lambda_BCS),
    'rho_Lambda_response': np.array(rho_Lambda_response_GeV4),
    'rho_Lambda_obs': np.array(rho_Lambda_obs),

    # Omega ratios
    'Omega_ratio_KV': np.array(Omega_ratio_KV),
    'Omega_ratio_BCS': np.array(Omega_ratio_BCS),
    'Omega_ratio_response': np.array(Omega_ratio_response),
    'Omega_ratio_imposed': np.array(Omega_ratio_imposed),
    'Omega_ratio_obs': np.array(Omega_DM_obs / Omega_Lambda_obs),

    # Free-streaming
    'lambda_fs_Mpc': np.array(lambda_fs_4D_Mpc),
    'v_fs_4D': np.array(v_fs_4D),
    'N_oscillations': np.array(N_oscillations),
    'lambda_compton_Mpc': np.array(lambda_compton_Mpc),

    # KZ parameters
    'xi_KZ': np.array(xi_KZ),
    'n_KZ': np.array(n_KZ),
    'M_domain_GeV': np.array(M_domain * M_KK_grav),

    # Gate
    'gate_name': np.array(['GGE-DM-43']),
    'gate_verdict': np.array([gate_verdict]),
    'gate_value': np.array(Omega_ratio_final),
}

np.savez('tier0-computation/s43_gge_dm_abundance.npz', **save_dict)
print("Data saved: tier0-computation/s43_gge_dm_abundance.npz")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE.")
print("=" * 72)
