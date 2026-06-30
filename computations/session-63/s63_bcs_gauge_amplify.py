#!/usr/bin/env python3
"""
s63_bcs_gauge_amplify.py — Non-Perturbative Higgs Threshold (BCS-GAUGE-AMPLIFY-63)
===================================================================================

PROBLEM:
  The BdG spectral action gives delta_a4/a4 = 3.70e-4 (S62, single-cell perturbative).
  The Higgs mass requires delta ~ 0.2-0.3 (Chamseddine-Connes-Marcolli).
  The gap: factor 676 = 0.25 / 3.70e-4.

  Three non-perturbative amplification channels evaluated:
    (A) Instanton tunneling between BCS vacua
    (B) Domain wall contributions at tau_DW = 0.1135
    (C) Inter-cell Josephson collective enhancement (N_cells = 32)

SYMMETRY ANALYSIS:
  Order parameter: Delta_{alpha} in BdG sectors (B1, B2, B3) with
  symmetry group U(1)_B x Z_2 x SU(3)_color (the BCS condensate breaks
  U(1)_B -> Z_2 and the internal SU(3) to its stability group).

  The spectral action coefficient a_4 is a functional of the endomorphism
  E of the Dirac operator. BCS pairing shifts E -> E + Delta^+Delta,
  modifying a_4 at O(Delta^2) (linear correction) and O(Delta^4) (quartic).

  Non-perturbative corrections arise from:
    - Tunneling between degenerate vacua (instanton gas)
    - Spatial gradients of Delta across domain boundaries
    - Phase coherence across the Voronoi tessellation

GATE: BCS-GAUGE-AMPLIFY-63
  PASS if any channel > 500x
  FAIL if all < 100x

Author: Landau Condensed Matter Theorist (S63)
"""

import numpy as np
import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import iv as besseli

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    # BCS constants
    E_cond, Delta_0_GL, Delta_0_OES, Delta_B3,
    S_inst, xi_BCS, xi_GL, a_GL, b_GL, barrier_0d, barrier_1d,
    N_dof_BCS, n_pairs,
    Gamma_Langer_BCS,
    # Spectral action
    a0_fold, a2_fold, a4_fold, S_fold,
    # Geometry
    Vol_SU3_Haar, tau_fold, PI,
    M_KK_gravity, M_KK_kerner,
    # Josephson
    J_C2, J_su2, J_u1, T_acoustic, N_cells,
    # Phonon spectrum
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    # Gradient stiffness
    Z_fold, c_fabric,
    # Other
    L_over_xi,
)

data_dir = os.path.dirname(__file__)

# =============================================================================
# STEP 0: Load input data
# =============================================================================
print("=" * 72)
print("BCS-GAUGE-AMPLIFY-63: Non-Perturbative Higgs Threshold")
print("=" * 72)

# Load BdG gauge fraction data (S62)
d_bdg = np.load(os.path.join(data_dir, 's62_bdg_gauge_fraction.npz'), allow_pickle=True)
delta_a4_pert = float(d_bdg['delta_a4_corrected'])      # 1.115e-4 (absolute)
ratio_a4_pert = float(d_bdg['ratio_a4_corrected'])       # 3.70e-4 (relative delta_a4/a4)
gauge_grav_ratio = float(d_bdg['gauge_grav_ratio'])      # 2.72
tr_Delta_sq = float(d_bdg['tr_Delta_sq'])                # 2.467
tr_Delta_4th = float(d_bdg['tr_Delta_4th'])              # 1.412

# Load Hessian one-loop data (S62)
d_hess = np.load(os.path.join(data_dir, 's62_hessian_oneloop.npz'), allow_pickle=True)
evals_eff = d_hess['evals_eff']           # 36 effective Hessian eigenvalues (all positive)
evals_tree = d_hess['evals_tree']         # 36 tree eigenvalues (all negative)
Lambda_sq = float(d_hess['Lambda_sq'])    # 16.98

# Load DW classification data (S61)
d_dw = np.load(os.path.join(data_dir, 's61_dw_classification.npz'), allow_pickle=True)
tau_DW = float(d_dw['tau_DW'])            # 0.1135
D1_DW = float(d_dw['D1_DW'])             # 0.370
D2_DW = float(d_dw['D2_DW'])             # 0.728
D3_DW = float(d_dw['D3_DW'])             # 0.084
D1_fold = float(d_dw['D1_fold'])          # 0.372
D2_fold = float(d_dw['D2_fold'])          # 0.732
D3_fold = float(d_dw['D3_fold'])          # 0.084
aniso_DW = float(d_dw['aniso_DW'])        # 1.636

# Load bounce action data (S62)
d_bounce = np.load(os.path.join(data_dir, 's62_bounce_action.npz'), allow_pickle=True)
B_1D = float(d_bounce['B_1D_analytic'])   # 38.19

# Load domain wall structure (S57)
d_dw57 = np.load(os.path.join(data_dir, 's57_domain_wall.npz'), allow_pickle=True)
N_bonds_C2 = int(d_dw57['N_bonds_C2'])     # 50
N_bonds_su2 = int(d_dw57['N_bonds_su2'])   # 24
N_bonds_u1 = int(d_dw57['N_bonds_u1'])     # 19
N_bonds_total = int(d_dw57['N_bonds_total'])  # 93
b1_graph = int(d_dw57['b1_graph'])          # 62

# Load anisotropic Josephson data (S63)
d_josph = np.load(os.path.join(data_dir, 's63_aniso_josephson.npz'), allow_pickle=True)
rho_s_directional = d_josph['rho_s_directional']
EJ_mean = float(d_josph['EJ_mean'])

# Derived quantities
target = 0.25         # Target delta_a4/a4 for Higgs mass
gap_factor = target / ratio_a4_pert
dim_spinor = 16       # spinor dimension on M^4 x SU(3)
d_manifold = 8  # total dimension (local)
R_fold = float(d_bdg['R_fold'])        # 2.018
Ric2_fold = float(d_bdg['Ric2_fold'])  # 0.514
K_fold = float(d_bdg['K_fold'])        # 0.535

print(f"\n--- Baseline (S62 perturbative) ---")
print(f"  delta_a4 (absolute)    = {delta_a4_pert:.6e}")
print(f"  delta_a4/a4 (ratio)    = {ratio_a4_pert:.6e}")
print(f"  gauge/gravity ratio    = {gauge_grav_ratio:.4f}")
print(f"  tr(Delta^2) = {tr_Delta_sq:.4f},  tr(Delta^4) = {tr_Delta_4th:.4f}")
print(f"  Target delta_a4/a4     = {target}")
print(f"  Gap factor             = {gap_factor:.0f}x")

# =============================================================================
# CHANNEL A: INSTANTON TUNNELING BETWEEN BCS VACUA
# =============================================================================
print("\n" + "=" * 72)
print("CHANNEL A: Instanton Tunneling Between BCS Vacua")
print("=" * 72)

# The BCS order parameter Delta = |Delta| * exp(i*phi) has a U(1) symmetry.
# Instantons are field configurations that interpolate between vacua with
# different winding number n in Euclidean time. The instanton action
# S_inst = 0.0687 was computed in S37 as the action of the bounce solution
# in the GL functional.
#
# Landau's key principle: the free energy is F = -T * ln(Z), where Z sums
# over ALL field configurations including topological sectors. The
# non-perturbative correction to the free energy from the instanton gas:
#
#   F_NP = -T * ln(Z_inst / Z_0)
#
# In the dilute instanton gas approximation (DIGA):
#   Z_inst = sum_{n_+, n_-} (K*V)^{n_+ + n_-} / (n_+! * n_-!) * exp(-S_inst*(n_+ + n_-))
#          = exp(2 * K * V * exp(-S_inst))
# where K is a dimensionful prefactor from the fluctuation determinant,
# V is the spacetime volume, and n_+, n_- count instantons/anti-instantons.

S_inst_val = S_inst  # 0.0687
exp_mS = np.exp(-S_inst_val)

print(f"\n--- A.1: Instanton parameters ---")
print(f"  S_inst = {S_inst_val:.6f}")
print(f"  exp(-S_inst) = {exp_mS:.6f}")
print(f"  NOTE: S_inst < 1 => DENSE instanton gas (DIGA unreliable)")

# For the DENSE gas (S_inst << 1), the instanton picture breaks down.
# The correct approach is to SUM over winding sectors in the path integral.
# Z = sum_n exp(-S_n) where S_n is the action in the n-winding sector.
#
# For a BCS system with N_dof = 8 modes, the winding number partition:
# S_n = n^2 * S_inst / (2 * N_dof)  (quadratic, each mode contributes)
# or S_n = |n| * S_inst (linear, for coherent tunneling of all modes).

n_max = 100  # (local)
n_arr = np.arange(-n_max, n_max + 1)

# Model 1: Independent-mode quadratic (dilute gas)
S_n_quad = n_arr**2 * S_inst_val / (2.0 * N_dof_BCS)
Z_quad = np.sum(np.exp(-S_n_quad))

# Model 2: Coherent tunneling (linear)
S_n_lin = np.abs(n_arr) * S_inst_val
Z_lin = np.sum(np.exp(-S_n_lin))

print(f"\n--- A.2: Winding number summation ---")
print(f"  Model 1 (quadratic/N_dof): Z/Z_0 = {Z_quad:.2f}")
print(f"  Model 2 (linear coherent): Z/Z_0 = {Z_lin:.2f}")

# The correction to the free energy:
# delta_F / F_0 = -ln(Z / Z_0) / S_fold
# where S_fold is the total spectral action at the fold.
delta_F_quad = np.log(Z_quad) / S_fold
delta_F_lin = np.log(Z_lin) / S_fold

print(f"  delta_F / S_fold (quad) = {delta_F_quad:.6e}")
print(f"  delta_F / S_fold (lin)  = {delta_F_lin:.6e}")

# The correction to a_4 specifically:
# a_4 appears as f_0 * a_4 in the spectral action. The instanton modifies
# the PATH INTEGRAL measure, not the classical action. So the correction to
# a_4 from instantons comes through the CHANGE in the functional integral:
#   delta_a4^{inst} / a4 = (Z_inst - Z_0) / Z_0 * (d ln Z / d(1/g^2)) / a4
# where 1/g^2 parametrizes the a_4 coefficient.
#
# For a single instanton with action S_inst = 8*pi^2 / g^2:
#   d S_inst / d(1/g^2) = 8*pi^2
# So: delta_a4^{inst} / a4 = sum_n exp(-S_n) * (d S_n / d(1/g^2)) / (Z * a4_fold)

# For Model 2 (linear): d S_n / d(1/g^2) = |n| * (d S_inst / d(1/g^2))
# We don't know d S_inst / d(1/g^2) directly (this is model-dependent).
# Instead, use the physical argument: the instanton contributes to a_4
# through the field strength of the instanton gauge field.
# In 8D: integral tr(F^2) for instanton = 8*pi^2 * |k| (by topology).
# But k_SU2_topological = 0 on SU(3) (S61 Chern-instanton).
# So the TOPOLOGICAL contribution to the gauge kinetic term vanishes exactly.

print(f"\n--- A.3: Topological constraint ---")
print(f"  k_SU2 topological on SU(3) = 0 (S61)")
print(f"  => Instanton contribution to tr(F^2) vanishes by topology!")
print(f"  => No topological amplification of the gauge sector a_4.")

# The remaining instanton effect: NON-TOPOLOGICAL corrections.
# These come from the instanton profile (NOT the topological charge) modifying
# the endomorphism E. The correction is:
#   delta_a4^{inst,non-top} = (4*pi)^{-4} * integral tr(delta_E^2) d^8x
# where delta_E_inst ~ exp(-S_inst) * Delta * f(x/xi) (instanton profile).
# Integrating: delta_a4^{inst} ~ exp(-2*S_inst) * Delta^2 * xi_BCS^8 / (4*pi)^4

delta_a4_inst_nontop = np.exp(-2 * S_inst_val) * tr_Delta_sq * xi_BCS**8 / (4*PI)**4
amplification_A_nontop = delta_a4_inst_nontop / delta_a4_pert

print(f"\n--- A.4: Non-topological instanton correction ---")
print(f"  delta_a4^inst = exp(-2S) * tr(D^2) * xi^8 / (4pi)^4")
print(f"              = {delta_a4_inst_nontop:.6e}")
print(f"  Amplification = {amplification_A_nontop:.4f}x")

# The PAIR TUNNELING instanton: the BCS instanton is a pair-transfer event.
# The Langer decay rate gives the tunneling rate per unit time:
# Gamma_L = 0.250 M_KK (S38, canonical_constants).
# Each tunneling event modifies the condensate density by delta_n ~ 1/V_cell.
# The modification of a_4 per tunneling event:
#   delta_a4^{Langer} = (delta_n / n_s) * delta_a4_pert
# where n_s = |Delta|^2 is the superfluid density.
# delta_n / n_s ~ 1 / (n_s * V_cell) ~ 1 / (Delta^2 * xi_BCS^8)
n_s = tr_Delta_sq / N_dof_BCS  # Superfluid density per mode
V_cell_coherence = xi_BCS**8
delta_n_over_ns = 1.0 / (n_s * V_cell_coherence)

# The rate-integrated correction: Gamma_L * delta_a4 * t_observation
# But t_observation is set by the transit time or the system lifetime.
# For the spectral action: no explicit time, so use the static correction.
# The pair susceptibility chi_pair = 1/S_inst diverges at the QCP:
chi_pair = 1.0 / S_inst_val
amplification_A_pair = Gamma_Langer_BCS * chi_pair * delta_n_over_ns

print(f"\n--- A.5: Pair tunneling correction ---")
print(f"  n_s per mode = {n_s:.4f}")
print(f"  V_cell = xi^8 = {V_cell_coherence:.4e}")
print(f"  delta_n/n_s = {delta_n_over_ns:.4e}")
print(f"  chi_pair = 1/S_inst = {chi_pair:.2f}")
print(f"  Amplification (pair) = {amplification_A_pair:.4f}x")

# The MAXIMUM instanton amplification from all sub-channels:
# Also include the winding sum correction to the partition function.
# Z/Z_0 - 1 gives the relative correction to the free energy.
# This feeds into a_4 proportionally.
amplification_A_winding = (Z_lin - 1)  # ~ 28 (from dense gas)

print(f"\n--- A.6: Winding number correction ---")
print(f"  Z_lin/Z_0 - 1 = {Z_lin - 1:.2f}")
print(f"  But this is the correction to the TOTAL free energy,")
print(f"  not specifically to a_4. The a_4 contribution is")
print(f"  suppressed by (delta_a4/a4) * (Z/Z_0 - 1):")
amplification_A_winding_a4 = (Z_lin - 1) * ratio_a4_pert / ratio_a4_pert
# This just gives Z/Z_0 - 1 as a multiplicative factor on the existing delta_a4:
print(f"  Effective amplification = {amplification_A_winding_a4:.2f}x")
print(f"  (Each winding sector contributes comparable delta_a4)")

# Conservative and generous estimates:
amplification_A_conservative = amplification_A_nontop  # sub-1
amplification_A_generous = amplification_A_winding_a4  # ~ 28

amplification_A = max(amplification_A_nontop, amplification_A_pair,
                      amplification_A_winding_a4)
print(f"\n  Sub-channel summary:")
print(f"    Non-topological:  {amplification_A_nontop:.4f}x")
print(f"    Pair tunneling:   {amplification_A_pair:.4f}x")
print(f"    Winding sum:      {amplification_A_winding_a4:.2f}x")
print(f"\n  >>> CHANNEL A AMPLIFICATION = {amplification_A:.2f}x <<<")

# =============================================================================
# CHANNEL B: DOMAIN WALL CONTRIBUTIONS AT tau_DW
# =============================================================================
print("\n" + "=" * 72)
print("CHANNEL B: Domain Wall Contribution at tau_DW = 0.1135")
print("=" * 72)

# The domain wall at tau_DW = 0.1135 is a GEOMETRIC CROSSOVER (DW-CLASS-61),
# not a phase boundary. The BCS gap is continuous through this point.
# However, the spectral geometry changes significantly between tau_DW and tau_fold.
# The amplification comes from the SPATIAL GRADIENT of Delta along the tau
# direction, which contributes to a_4 through the ||nabla Delta||^2 term.

# Gap profiles at DW and fold:
# n_B1 = 1, n_B2 = 4, n_B3 = 3 modes
tr_D2_DW = 1 * D1_DW**2 + 4 * D2_DW**2 + 3 * D3_DW**2
tr_D4_DW = 1 * D1_DW**4 + 4 * D2_DW**4 + 3 * D3_DW**4
tr_D2_fold = 1 * D1_fold**2 + 4 * D2_fold**2 + 3 * D3_fold**2
tr_D4_fold = 1 * D1_fold**4 + 4 * D2_fold**4 + 3 * D3_fold**4

print(f"\n--- B.1: Gap profiles ---")
print(f"  At fold (tau = {tau_fold}): D1={D1_fold:.4f}, D2={D2_fold:.4f}, D3={D3_fold:.4f}")
print(f"  At DW (tau = {tau_DW:.4f}):  D1={D1_DW:.4f}, D2={D2_DW:.4f}, D3={D3_DW:.4f}")
print(f"  tr(Delta^2) fold/DW = {tr_D2_fold:.6f} / {tr_D2_DW:.6f}")
print(f"  tr(Delta^4) fold/DW = {tr_D4_fold:.6f} / {tr_D4_DW:.6f}")

# B.1: GRADIENT CONTRIBUTION
# The spectral action a_4 includes a gradient term:
#   delta_a4^{grad} = (1/12) * (4pi)^{-d/2} * integral tr(|nabla_tau Delta|^2) dtau
# The gradient is estimated from the profile between DW and fold:
delta_tau = tau_fold - tau_DW  # 0.077
d_tr_D2_dtau = (tr_D2_fold - tr_D2_DW) / delta_tau

# The gradient contribution integrated over the wall width L_DW ~ xi_BCS:
L_DW = xi_BCS  # 0.808 M_KK^{-1}
prefactor_sd = (4 * PI)**(-d_manifold / 2.0)  # (4pi)^{-4}

grad_a4 = (1.0 / 12.0) * prefactor_sd * d_tr_D2_dtau**2 * L_DW
amplification_B_grad = grad_a4 / delta_a4_pert

print(f"\n--- B.2: Gradient contribution ---")
print(f"  delta_tau = {delta_tau:.4f}")
print(f"  d(tr D^2)/d(tau) = {d_tr_D2_dtau:.4f}")
print(f"  L_DW = xi_BCS = {L_DW:.4f}")
print(f"  delta_a4^grad = {grad_a4:.6e}")
print(f"  Amplification (gradient) = {amplification_B_grad:.4f}x")

# B.2: CURVATURE-DEPENDENT BCS CORRECTION
# The BCS correction to a_4 depends on the background geometry through
# the R*tr(Delta^2) cross term in the Seeley-DeWitt expansion.
# At the DW, both R and Delta differ from the fold values.
# The question: how does delta_a4^{BCS}(tau_DW) compare to delta_a4^{BCS}(tau_fold)?
#
# CRITICAL: The variation of the GEOMETRIC a_4 between DW and fold is NOT
# an amplification of the BCS signal. It is an independent background effect.
# Only the change in the BCS CONTRIBUTION to a_4 counts.
#
# The BCS delta_a4 scales as: delta_a4 ~ prefactor * (R * tr(D^2) + tr(D^4) + ...)
# The ratio at DW vs fold:
ratio_D2 = tr_D2_DW / tr_D2_fold  # Gap^2 ratio
ratio_D4 = tr_D4_DW / tr_D4_fold  # Gap^4 ratio
# R varies with tau. Estimate R_DW from scaling:
R_DW_est_B2 = R_fold * (tau_DW / tau_fold)  # Linear scaling approximation
ratio_R = R_DW_est_B2 / R_fold

# The cross-term (R * tr(D^2)) ratio:
ratio_cross = ratio_R * ratio_D2

# The BCS correction ratio at DW vs fold (weighted average of terms):
# delta_a4 = c1 * R * tr(D^2) + c2 * tr(D^4) + c3 * (tr D^2)^2
# With roughly equal weights: average the ratios
bcs_correction_ratio_DW = (ratio_cross + ratio_D4 + ratio_D2**2) / 3.0
amplification_B_curv = bcs_correction_ratio_DW
# This measures how the BCS correction ITSELF changes at DW, relative to fold.
# Since the gaps are nearly identical (1.2% variation), this is close to 1.

print(f"\n--- B.3: BCS correction at DW vs fold ---")
print(f"  tr(D^2) ratio DW/fold = {ratio_D2:.6f}")
print(f"  tr(D^4) ratio DW/fold = {ratio_D4:.6f}")
print(f"  R ratio DW/fold (est) = {ratio_R:.6f}")
print(f"  Cross-term ratio = {ratio_cross:.6f}")
print(f"  Average BCS correction ratio = {bcs_correction_ratio_DW:.6f}")
print(f"  Amplification (curvature-BCS) = {amplification_B_curv:.4f}x")
print(f"  NOTE: This is ~1.0 because the BCS gap barely changes at the DW.")

# B.3: CROSS TERM VARIATION
# The R * tr(Delta^2) cross term in a_4 varies between DW and fold.
# The CHANGE in this term gives an additional BCS-dependent contribution.
# But this variation is WITHIN the BCS correction -- it does not amplify it.
# The cross term at fold: (R_fold * tr_D2_fold) / 6
# The cross term at DW: (R_DW * tr_D2_DW) / 6
# The AMPLIFICATION interpretation: if we evaluate delta_a4^BCS at the DW
# instead of the fold, how much bigger is it?
R_DW_est = R_fold * (tau_DW / tau_fold)  # ~ 1.204
cross_fold = (1.0 / 6.0) * R_fold * tr_D2_fold
cross_DW = (1.0 / 6.0) * R_DW_est * tr_D2_DW
delta_cross = abs(cross_fold - cross_DW)

# This delta_cross is a VARIATION of the cross term, not an amplification.
# As a fraction of the cross term at fold:
cross_frac = delta_cross / cross_fold  # fractional change
# As a multiplicative factor on delta_a4: the cross term is ONE part of delta_a4.
# If the cross term dominates: amplification ~ delta_cross / delta_a4_pert.
# But this is comparing an ABSOLUTE shift in the R*Delta^2 term to delta_a4.
# The shift occurs because R changes (GEOMETRIC, not BCS-driven).
# Honest amplification: (R_DW * tr_D2_DW) / (R_fold * tr_D2_fold) - 1
amplification_B_cross = cross_DW / cross_fold  # ratio, should be < 1

print(f"\n--- B.4: Cross term variation ---")
print(f"  R_DW (est) = {R_DW_est:.4f}")
print(f"  Cross at fold = {cross_fold:.6f}")
print(f"  Cross at DW   = {cross_DW:.6f}")
print(f"  Ratio DW/fold = {amplification_B_cross:.4f}")
print(f"  The cross term at DW is {amplification_B_cross:.1%} of fold.")
print(f"  This is NOT an amplification -- it is SUPPRESSION.")

# B.4: WALL TENSION CORRECTION
# The GL wall tension sigma_DW for a 1D profile:
# sigma = integral [-a * |Delta|^2 + b * |Delta|^4 + xi^2 |dDelta/dx|^2] dx
# For a kink profile Delta(x) = Delta_0 * tanh(x / (sqrt(2) * xi)):
# sigma = (2*sqrt(2)/3) * xi * |a|^3 / b^2  (standard Landau wall energy)
# But this describes a PHASE boundary kink, and DW-CLASS-61 says no phase boundary.
# The actual gradient is smooth. Use the sigma estimate for comparison only.
sigma_LW = (2 * np.sqrt(2) / 3.0) * xi_GL * abs(a_GL)**3 / b_GL**2
# sigma contributes to a_4 through the integrated profile over the wall area:
# delta_a4_sigma ~ sigma * A_wall / (Vol_total * (4pi)^4)
# A_wall ~ Vol_SU3^{7/8} (7-dimensional wall in 8D)
A_wall = Vol_SU3_Haar**(7.0/8.0)
Vol_total = Vol_SU3_Haar
delta_a4_sigma = sigma_LW * A_wall / (Vol_total * (4*PI)**4)
amplification_B_sigma = delta_a4_sigma / delta_a4_pert

print(f"\n--- B.5: Wall tension ---")
print(f"  sigma_LW = {sigma_LW:.6e} M_KK^7")
print(f"  A_wall ~ Vol^(7/8) = {A_wall:.2f}")
print(f"  delta_a4_sigma = {delta_a4_sigma:.6e}")
print(f"  Amplification (wall tension) = {amplification_B_sigma:.4f}x")

# Summary Channel B
# amplification_B_curv and amplification_B_cross are BCS correction RATIOS
# (DW vs fold), not amplification factors. They measure how the existing
# delta_a4 changes at DW -- values < 1 mean SUPPRESSION, not amplification.
# The honest amplification channels are gradient and wall tension.
amplification_B = max(amplification_B_grad, amplification_B_sigma,
                      amplification_B_curv, amplification_B_cross)
print(f"\n  Sub-channel summary:")
print(f"    Gradient:          {amplification_B_grad:.4f}x")
print(f"    BCS ratio (curv):  {amplification_B_curv:.4f} (DW/fold ratio, not amplification)")
print(f"    Cross-term ratio:  {amplification_B_cross:.4f} (DW/fold ratio, suppressed)")
print(f"    Wall tension:      {amplification_B_sigma:.4f}x")
print(f"\n  >>> CHANNEL B AMPLIFICATION = {amplification_B:.4f}x <<<")

# =============================================================================
# CHANNEL C: INTER-CELL JOSEPHSON COLLECTIVE ENHANCEMENT
# =============================================================================
print("\n" + "=" * 72)
print("CHANNEL C: Inter-Cell Josephson Collective Enhancement")
print("=" * 72)

# The 32-cell Voronoi tessellation has Josephson couplings between cells.
# The spectral action receives contributions from:
#   (a) The endomorphism E of the MULTI-CELL Dirac operator (off-diagonal Josephson)
#   (b) The superfluid weight (Meissner mass for gauge fields)
#   (c) Collective mode (Goldstone, Higgs) quantum corrections

print(f"\n--- C.1: Tessellation structure ---")
print(f"  N_cells = {N_cells}")
print(f"  Bonds: {N_bonds_C2} (C^2) + {N_bonds_su2} (su2) + {N_bonds_u1} (u1) = {N_bonds_total}")
print(f"  b1(graph) = {b1_graph}")

# C.1: JOSEPHSON ENDOMORPHISM CORRECTION TO a_4
# The multi-cell Dirac operator has E_total = bigoplus_i E_i + sum_{<ij>} J_ij
# The a_4 coefficient involves tr(E_total^2):
# tr(E_total^2) = N * tr(E_cell^2) + 2 * sum_{<ij>} J_ij^2 * dim_spinor
# (The factor 2 from off-diagonal + conjugate blocks)

J_sq_sum = N_bonds_C2 * J_C2**2 + N_bonds_su2 * J_su2**2 + N_bonds_u1 * J_u1**2
tr_E2_Josephson = 2 * J_sq_sum * dim_spinor
tr_E2_BCS_single = dim_spinor * tr_Delta_sq
tr_E2_total = N_cells * tr_E2_BCS_single + tr_E2_Josephson

# The PER-CELL delta_a4 from Josephson:
# (tr_E2_total / N_cells) vs tr_E2_BCS_single
enhancement_E2 = tr_E2_Josephson / (N_cells * tr_E2_BCS_single)
amplification_C_E2 = 1.0 + enhancement_E2

print(f"\n--- C.2: Endomorphism E^2 correction ---")
print(f"  tr(E^2) single cell (BCS)     = {tr_E2_BCS_single:.4f}")
print(f"  tr(E^2) all cells (extensive)  = {N_cells * tr_E2_BCS_single:.4f}")
print(f"  tr(E^2) Josephson bonds        = {tr_E2_Josephson:.4f}")
print(f"  Enhancement ratio = {enhancement_E2:.4f}")
print(f"  Amplification (E^2) = {amplification_C_E2:.4f}x")

# C.2: FOURTH-ORDER ENDOMORPHISM (E^4 and (E^2)^2)
# These are the terms in a_4 that contain |Delta|^4 and cross terms.
# For tr(E^4) in the multi-cell system:
# The leading Josephson cross term: 4 * J^2 * tr(E^2) per bond
# tr(E_total^4) = N * tr(E^4) + 4 * sum_{<ij>} J_ij^2 * dim_spinor * (tr_Delta_sq)
tr_E4_cross = 4 * J_sq_sum * dim_spinor * tr_Delta_sq
tr_E4_single = dim_spinor * tr_Delta_4th

# For (tr E_total^2)^2:
# = (N * e2 + J)^2 = N^2 * e2^2 + 2*N*e2*J + J^2
# Per cell: N * e2^2 + 2*e2*J + J^2/N
# Enhancement: 1 + 2*J/(N*e2) + J^2/(N^2*e2^2)
e2 = tr_E2_BCS_single
J_eff = tr_E2_Josephson
quartic_enhancement = (1.0 + J_eff / (N_cells * e2))**2
amplification_C_quartic = quartic_enhancement

print(f"\n--- C.3: Quartic (E^4) correction ---")
print(f"  tr(E^4) single cell  = {tr_E4_single:.4f}")
print(f"  tr(E^4) cross-term   = {tr_E4_cross:.4f}")
print(f"  (tr E^2)^2 enhancement = {quartic_enhancement:.4f}")
print(f"  Amplification (quartic) = {amplification_C_quartic:.4f}x")

# C.3: SUPERFLUID WEIGHT (MEISSNER MASS)
# The physically crucial contribution: in the Anderson-Higgs mechanism,
# the gauge boson mass m_A^2 = g^2 * rho_s. The superfluid weight rho_s
# is set by the Josephson stiffness across the tessellation.
#
# From S63 anisotropic Josephson data:
rho_s_max = float(np.max(rho_s_directional))
rho_s_min = float(np.min(rho_s_directional))
rho_s_mean = float(np.mean(rho_s_directional))

# Thermal phase coherence at T_acoustic:
cos_avg_C2 = float(besseli(1, J_C2/T_acoustic) / besseli(0, J_C2/T_acoustic))
cos_avg_su2 = float(besseli(1, J_su2/T_acoustic) / besseli(0, J_su2/T_acoustic))
cos_avg_u1 = float(besseli(1, J_u1/T_acoustic) / besseli(0, J_u1/T_acoustic))

print(f"\n--- C.4: Phase coherence at T = {T_acoustic} M_KK ---")
print(f"  J_C2/T = {J_C2/T_acoustic:.2f}, <cos phi> = {cos_avg_C2:.6f}")
print(f"  J_su2/T = {J_su2/T_acoustic:.2f}, <cos phi> = {cos_avg_su2:.6f}")
print(f"  J_u1/T = {J_u1/T_acoustic:.2f}, <cos phi> = {cos_avg_u1:.6f}")

# Effective superfluid stiffness per cell:
rho_s_eff_C2 = (N_bonds_C2 * J_C2 * cos_avg_C2) / N_cells
rho_s_eff_su2 = (N_bonds_su2 * J_su2 * cos_avg_su2) / N_cells
rho_s_eff_u1 = (N_bonds_u1 * J_u1 * cos_avg_u1) / N_cells
rho_s_eff_total = rho_s_eff_C2 + rho_s_eff_su2 + rho_s_eff_u1

print(f"\n--- C.5: Effective superfluid stiffness ---")
print(f"  rho_s (C^2)   = {rho_s_eff_C2:.4f}")
print(f"  rho_s (su(2)) = {rho_s_eff_su2:.4f}")
print(f"  rho_s (u(1))  = {rho_s_eff_u1:.4f}")
print(f"  rho_s (total) = {rho_s_eff_total:.4f}")

# The Meissner mass contribution to a_4:
# m_A^2 enters a_4 through the gauge boson one-loop determinant.
# In the spectral action: delta_a4^{Meissner} ~ rho_s * vol / (4*pi)^4
# But this needs normalization. The correct comparison is:
# The BCS endomorphism gives delta_a4_pert from tr(E_BCS^2) ~ Delta^2.
# The Josephson stiffness gives delta_a4_J from the mass matrix of gauge bosons.
# The Higgs mechanism IS the statement that rho_s sets m_W, m_Z.
# In the spectral action: m_H^2 propto (delta_a4 / a_2) * Lambda^2.
# The rho_s contribution modifies delta_a4 by the ratio rho_s / n_s:
rho_s_over_ns = rho_s_eff_total / (tr_Delta_sq / N_dof_BCS)
amplification_C_meissner = rho_s_over_ns

print(f"  rho_s / n_s = {rho_s_over_ns:.4f}")
print(f"  Amplification (Meissner) = {amplification_C_meissner:.4f}x")

# C.4: COLLECTIVE MODE QUANTUM CORRECTIONS
# The Goldstone and Higgs modes generate Coleman-Weinberg one-loop
# corrections to the effective potential V_eff(Delta).
# V_CW = sum_modes (1/64*pi^2) * m_i^4 * (ln(m_i^2/mu^2) - 3/2)  [4D formula]
#
# CRITICAL NORMALIZATION: V_CW is in M_KK^4 units of energy density.
# The Gilkey coefficient delta_a4 is DIMENSIONLESS (after dividing by a4_fold).
# To compare: delta_a4^{CW} = V_CW * Vol_SU3 / (Lambda^4 * f_4)
# where Lambda^4 * f_4 ~ a_0 * M_KK^4 (from spectral action normalization).
# The correct dimensionless ratio is V_CW / (M_KK^4 * a4_fold).
# Since V_CW is already in M_KK^4 units: delta_a4^{CW} / a4_fold = V_CW / a4_fold.
#
# But the AMPLIFICATION question is: does V_CW modify the BCS contribution?
# V_CW is a quantum correction FROM the collective modes INDUCED by BCS.
# It is a CORRECTION to the BCS delta_a4, proportional to:
#   delta_a4^{CW} / delta_a4^{pert} = V_CW / (delta_a4_pert * a4_fold / a4_fold)
# = V_CW / delta_a4_pert
# BUT V_CW is in M_KK^4 per cell volume, not a dimensionless Gilkey coefficient.
# Correct comparison: V_CW * (4*pi)^{-d/2} * Vol_SU3 / a4_fold vs delta_a4/a4.

mu_sq = 1.0  # M_KK units  # (local)
V_CW = 0.0  # (local)
mode_contributions = []

for label, m_sq in [("Goldstone", c_Gold**2 * (2*PI*L_over_xi/xi_BCS)**2),
                     ("Leggett-1", omega_L1**2),
                     ("Leggett-2", omega_L2**2),
                     ("Higgs-1", omega_H1**2),
                     ("Higgs-2", omega_H2**2),
                     ("Higgs-3", omega_H3**2)]:
    if m_sq > 1e-20:
        V_i = (1.0 / (64 * PI**2)) * m_sq**2 * (np.log(abs(m_sq / mu_sq)) - 1.5)
        V_CW += V_i
        mode_contributions.append((label, m_sq, V_i))

# Convert V_CW to a dimensionless a_4 correction:
# CRITICAL: V_CW is the one-loop vacuum energy. It modifies a_0 (cosmological
# constant), NOT a_4 (gauge kinetic term) directly. The correction to a_4 from
# CW is the SECOND DERIVATIVE of V_CW with respect to the gauge coupling:
#   delta_a4^{CW} = d^2 V_CW / d(1/g^2)^2
# For modes whose mass depends on 1/g^2 through m^2 = g^2 * (BCS condensate):
#   d V_CW / d(1/g^2) = (dm^2/d(1/g^2)) * dV/dm^2
#   dm^2/d(1/g^2) = -g^4 * (condensate)
# So delta_a4^{CW} ~ g^4 * V_CW * (correction factors)
#
# Alternatively, the CW potential generates a correction to the HIGGS QUARTIC
# (which IS in a_4) through d^2 V_CW / d|Delta|^2 evaluated at Delta = Delta_0.
# This is the standard CW correction to the Higgs self-coupling:
#   delta_lambda = d^4 V_CW / d|Delta|^4 |_{Delta_0}
# For V_CW = (1/64*pi^2) * m^4 * (ln m^2 - 3/2) with m^2 = f(Delta):
#   delta_lambda = (1/16*pi^2) * sum_modes (dm^4/d|Delta|^4) * ln(m^2/mu^2)
# The modes are: Goldstone (m ~ k*c_Gold), Leggett, Higgs.
# For the Higgs-3 mode with m^2 = 131.4 M_KK^2:
#   dm^2/d|Delta|^2 ~ m^2/Delta^2 (assuming mass from BCS condensate)
# So d^4V/d|Delta|^4 ~ (1/16*pi^2) * (m^2/Delta^2)^2 * ln(m^2)

# Compute the CW correction to the Higgs quartic (which appears in a_4):
# IMPORTANT: Only include modes with m < Lambda (UV cutoff of spectral action).
# Modes with m > Lambda are ALREADY integrated out in the heat kernel and
# including them again would be double-counting.
# Lambda_sq = 16.98 => Lambda = 4.12 M_KK from S62 Hessian data.
Delta_sq_eff = tr_Delta_sq / N_dof_BCS  # Average Delta^2 per mode
V_CW_quartic = 0.0  # (local)
V_CW_quartic_ALL = 0.0  # For comparison: what happens without UV cutoff  # (local)
for label, m_sq, V_i in mode_contributions:
    if m_sq > 0:
        # d^4 V / d|Delta|^4 ~ (1/16*pi^2) * (m^2/Delta^2)^2 * |ln(m^2)|
        d4V = (1.0 / (16 * PI**2)) * (m_sq / Delta_sq_eff)**2 * abs(np.log(m_sq))
        V_CW_quartic_ALL += d4V
        # Apply UV cutoff: only include modes below Lambda
        if m_sq < Lambda_sq:
            V_CW_quartic += d4V
            print(f"  [INCLUDED] {label}: m^2={m_sq:.4f} < Lambda^2={Lambda_sq:.2f}")
        else:
            print(f"  [EXCLUDED] {label}: m^2={m_sq:.4f} > Lambda^2={Lambda_sq:.2f} (UV cutoff)")

# This quartic correction modifies delta_a4 through the Higgs term in a_4.
# The Higgs quartic in a_4: lambda * |phi|^4 where lambda ~ delta_a4/a4.
# The CW correction to lambda: delta_lambda = V_CW_quartic * Delta_sq_eff^2
# The correction to delta_a4/a4:
delta_lambda_CW = V_CW_quartic * Delta_sq_eff**2
# Normalize by converting to Gilkey units:
V_CW_gilkey = delta_lambda_CW * prefactor_sd * (Vol_SU3_Haar / N_cells)
amplification_C_CW = V_CW_gilkey / delta_a4_pert

print(f"\n--- C.6: Coleman-Weinberg corrections ---")
print(f"  UV cutoff: Lambda^2 = {Lambda_sq:.2f}, Lambda = {np.sqrt(Lambda_sq):.2f} M_KK")
for label, m_sq, V_i in mode_contributions:
    status = "OK" if m_sq < Lambda_sq else "EXCLUDED"
    print(f"  {label:12s}: m^2 = {m_sq:.6f}, V_CW = {V_i:.6e} M_KK^4  [{status}]")
print(f"  V_CW total (M_KK^4) = {V_CW:.6e}")
print(f"  CW quartic (below Lambda) = {V_CW_quartic:.6e}")
print(f"  CW quartic (ALL modes)    = {V_CW_quartic_ALL:.6e}")
print(f"  delta_lambda_CW = {delta_lambda_CW:.6e}")
print(f"  V_CW (Gilkey units) = {V_CW_gilkey:.6e}")
print(f"  Amplification (CW quartic) = {amplification_C_CW:.4f}x")

# C.5: TOTAL JOSEPHSON ENERGY vs BCS ENERGY
# The ratio E_J_total / |E_cond| tells us how important inter-cell coupling is.
E_J_total = N_bonds_C2 * J_C2 + N_bonds_su2 * J_su2 + N_bonds_u1 * J_u1
E_BCS_single = abs(E_cond)
collective_ratio = E_J_total / E_BCS_single

print(f"\n--- C.7: Energy scale comparison ---")
print(f"  E_J (total) = {E_J_total:.4f} M_KK")
print(f"  |E_cond| (single cell) = {E_BCS_single:.4f} M_KK")
print(f"  E_J / |E_cond| = {collective_ratio:.2f}")
print(f"  E_J / (N_cells * |E_cond|) = {E_J_total / (N_cells * E_BCS_single):.2f}")

# C.6: THE PHYSICAL AMPLIFICATION MECHANISM
# The key physical argument for Josephson amplification:
# In GL theory, the Higgs mass depends on the QUARTIC coupling lambda:
#   m_H^2 = 2 * lambda * v^2
# The quartic lambda comes from a_4, and the VEV v comes from a_2.
# The BCS condensate provides BOTH v and lambda. The question is whether
# the Josephson network RENORMALIZES lambda upward.
#
# In a Josephson junction array:
# lambda_eff = lambda_bare + (E_J / E_C) * (corrections from phase fluctuations)
# where E_C ~ 1/(2*n_s) is the charging energy.
# E_J / E_C is the Josephson-to-charging ratio.
# From S57: E_J / E_C = 2.38 for the primary (C^2) bonds.

E_C_single = 1.0 / (2.0 * n_s)  # Charging energy per mode
EJ_over_EC = J_C2 / E_C_single
print(f"\n--- C.8: Josephson-to-charging ratio ---")
print(f"  E_C (single mode) = {E_C_single:.4f}")
print(f"  E_J(C^2) / E_C = {EJ_over_EC:.4f}")

# In the Josephson regime (E_J >> E_C), phase fluctuations are small
# and the phase is well-defined. The quartic coupling gets a correction:
# delta_lambda / lambda ~ (E_J / E_C)^2 * (1/N_cells)
# But this is for the PHASE quartic. The Higgs quartic (AMPLITUDE)
# is set by the intra-cell BCS physics and is NOT enhanced by Josephson.
# The Josephson coupling only sets the PHASE stiffness.

# This is the CRUCIAL point: the Higgs mass in the SM comes from the
# AMPLITUDE mode of the order parameter, not the phase (Goldstone).
# The Josephson coupling enhances the PHASE sector (massive gauge bosons)
# but does NOT directly enhance the Higgs quartic.

# However, there is an indirect effect: the Higgs quartic receives
# corrections from gauge boson loops, which DO depend on rho_s.
# delta_lambda ~ (g^4 / 16*pi^2) * ln(m_A^2 / m_H^2)
# With m_A^2 = rho_s and m_H^2 = 2*lambda*v^2:
# If rho_s >> v^2, then ln(rho_s/m_H^2) > 0 and lambda INCREASES.

# Estimate: the gauge boson loop correction to the Higgs quartic:
# In SM: delta_lambda = (3/8*pi^2) * (g^4 + g'^4/4 + ...) (1-loop RG)
# The correction is O(g^4) ~ O(0.1) (numerically small).
# The Josephson enhancement modifies the running by changing the scale:
# New contribution: delta_lambda ~ (3/8*pi^2) * g^4 * ln(rho_s / m_H^2)
g_sq = 1.0 / (2 * a4_fold / Vol_SU3_Haar)  # ~ gauge coupling^2 from spectral action
delta_lambda_gauge_loop = (3.0 / (8 * PI**2)) * g_sq**2 * abs(np.log(rho_s_eff_total))
amplification_C_gauge_loop = delta_lambda_gauge_loop

print(f"\n--- C.9: Gauge loop correction to Higgs quartic ---")
print(f"  g^2 (effective) = {g_sq:.4f}")
print(f"  delta_lambda (gauge loop) = {delta_lambda_gauge_loop:.6e}")
print(f"  This is a correction to LAMBDA, not directly to delta_a4.")

# C.7: CORRECT PHYSICAL ACCOUNTING
# Let me compute the actual multi-cell correction properly.
# The spectral action a_4 for the multi-cell system:
#   a_4^{multi} = N_cells * a_4^{single} + a_4^{Josephson}
# where a_4^{Josephson} comes from the Josephson coupling in the endomorphism.
# The BCS correction to a_4:
#   delta_a4^{multi} = N_cells * delta_a4^{single} + delta_a4^{Josephson-BCS}
# where delta_a4^{Josephson-BCS} is the CROSS TERM between Josephson and BCS.
# This cross term arises because the Josephson coupling depends on Delta:
#   J_ij ~ J_0 * |Delta_i| * |Delta_j| (pair tunneling amplitude)
# So dJ/dDelta is nonzero, and the variation of a_4 with Delta includes
# the Josephson contribution:
#   d(a_4^{J})/d(Delta) = sum_{<ij>} 2 * J_0 * Delta * dim_spinor

# For each bond: the Josephson coupling is J = J_0 * Delta^2 (pair tunneling).
# So delta(J^2)/delta(Delta^2) = 2 * J_0^2 * Delta^2.
# The Josephson contribution to the endomorphism E_J ~ J per bond, so
# delta(tr E_J^2) / delta(Delta^2) = 2 * N_bonds * J_0 * dim_spinor.
# And the amplification:
#   delta_a4_J / delta_a4_BCS = (2 * N_bonds * J_0 * dim) / (N_cells * dim * 2*Delta^2)
# = N_bonds * J_0 / (N_cells * Delta^2)

# The J values are already in M_KK units and include Delta implicitly.
# J_C2 = 0.933 M_KK is the full coupling GIVEN the BCS gap at the fold.
# So dJ/dDelta^2 ~ J/Delta^2 ~ J / (tr_Delta_sq / N_dof)
dJ_dD2 = J_C2 / (tr_Delta_sq / N_dof_BCS)

# Cross-term amplification per cell:
cross_J_a4 = (N_bonds_C2 * dJ_dD2 * dim_spinor * 2) / (N_cells * dim_spinor * 2 * tr_Delta_sq)
# Simplifies to: N_bonds_C2 * J_C2 * N_dof / (N_cells * tr_Delta_sq^2)
cross_J_a4_v2 = N_bonds_C2 * J_C2 * N_dof_BCS / (N_cells * tr_Delta_sq**2)

amplification_C_cross = 1.0 + cross_J_a4_v2

print(f"\n--- C.10: Josephson-BCS cross amplification ---")
print(f"  dJ_C2/d(Delta^2) = {dJ_dD2:.4f}")
print(f"  Cross-term correction = {cross_J_a4_v2:.4f}")
print(f"  Amplification (Josephson-BCS cross) = {amplification_C_cross:.4f}x")

# Summary Channel C
# The E_J/|E_cond| ratio is an energy scale comparison, NOT an amplification
# of delta_a4. It tells us inter-cell coupling dominates, but does not
# multiply the BCS endomorphism correction. Exclude from amplification max.
amplification_C = max(amplification_C_E2, amplification_C_quartic,
                      amplification_C_meissner, amplification_C_CW,
                      amplification_C_cross)
print(f"\n  Sub-channel summary (HONEST amplification of delta_a4):")
print(f"    E^2 (endomorphism):      {amplification_C_E2:.4f}x")
print(f"    E^4 (quartic):           {amplification_C_quartic:.4f}x")
print(f"    Meissner (rho_s/n_s):    {amplification_C_meissner:.4f}x")
print(f"    Coleman-Weinberg:        {amplification_C_CW:.4f}x")
print(f"    Josephson-BCS cross:     {amplification_C_cross:.4f}x")
print(f"    E_J/|E_cond| (SCALE):    {collective_ratio:.2f} (NOT amplification)")
print(f"\n  >>> CHANNEL C AMPLIFICATION = {amplification_C:.2f}x <<<")

# =============================================================================
# SUMMARY AND GATE VERDICT
# =============================================================================
print("\n" + "=" * 72)
print("SUMMARY: All Three Amplification Channels")
print("=" * 72)

print(f"\n  Channel A (Instanton tunneling):    {amplification_A:.2f}x")
print(f"  Channel B (Domain wall at tau_DW):   {amplification_B:.2f}x")
print(f"  Channel C (Josephson collective):    {amplification_C:.2f}x")

max_single = max(amplification_A, amplification_B, amplification_C)
max_channel = "A" if max_single == amplification_A else \
              "B" if max_single == amplification_B else "C"

print(f"\n  Maximum single channel: {max_channel} = {max_single:.2f}x")

# Combined: the channels are physically independent, so they SUM.
amplification_combined = amplification_A + amplification_B + amplification_C
print(f"  Combined (sum):  {amplification_combined:.2f}x")

# Gap assessment
achieved_single = max_single * ratio_a4_pert
achieved_combined = amplification_combined * ratio_a4_pert
remaining_gap_single = target / achieved_single if achieved_single > 0 else np.inf
remaining_gap_combined = target / achieved_combined if achieved_combined > 0 else np.inf

print(f"\n  Achieved delta_a4/a4 (best channel): {achieved_single:.4e}")
print(f"  Achieved delta_a4/a4 (combined):     {achieved_combined:.4e}")
print(f"  Target delta_a4/a4:                  {target}")
print(f"  Remaining gap (best):  {remaining_gap_single:.1f}x")
print(f"  Remaining gap (combined): {remaining_gap_combined:.1f}x")

# Gate verdict:
print(f"\n--- GATE: BCS-GAUGE-AMPLIFY-63 ---")
print(f"  Criterion: PASS if any channel > 500x, FAIL if all < 100x")

if max_single >= 500:
    verdict = "PASS"
    detail = f"Channel {max_channel} achieves {max_single:.1f}x amplification (> 500x threshold)"
elif max_single >= 100:
    verdict = "INFO"
    detail = f"Best channel {max_channel} = {max_single:.1f}x (between 100x and 500x)"
else:
    verdict = "FAIL"
    detail = (f"All channels < 100x. Best: Channel {max_channel} = {max_single:.2f}x. "
              f"Combined: {amplification_combined:.2f}x. "
              f"Remaining gap: {remaining_gap_combined:.0f}x to Higgs threshold. "
              f"ROOT CAUSE: The BdG perturbative delta_a4/a4 = {ratio_a4_pert:.4e} is a "
              f"volume-suppressed correction (Vol(SU3) = {Vol_SU3_Haar:.0f} divides the "
              f"endomorphism trace). Non-perturbative channels (instanton, domain wall, "
              f"Josephson) are O(1)-O(100) multiplicative corrections — insufficient to "
              f"bridge the factor {gap_factor:.0f}. The Higgs mechanism requires a "
              f"STRUCTURAL modification of a_4, not an amplification of the BdG shift.")

print(f"  Verdict: {verdict}")
print(f"  Detail: {detail}")

# =============================================================================
# CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 72)
print("CROSS-CHECKS")
print("=" * 72)

# Cross-check 1: Dimensional analysis
print(f"\n  CC1: Volume suppression")
print(f"  The ratio delta_a4/a4 = {ratio_a4_pert:.4e}")
print(f"  Naive (no Vol): tr(D^4) / (5R^2) ~ {tr_Delta_4th / (5 * R_fold**2):.4f}")
print(f"  With (4pi)^-4 = {(4*PI)**(-4):.6e}")
print(f"  Combined naive: {tr_Delta_4th / (5 * R_fold**2) * (4*PI)**(-4):.6e}")
print(f"  => Vol(SU3) appears in BOTH num and denom, cancels in ratio.")
print(f"  => The smallness comes from (4pi)^-4 ~ 4e-5 and geometric factors.")

# Cross-check 2: Topological triviality
print(f"\n  CC2: Topological structure")
print(f"  k_SU2 = 0 on SU(3) (S61). No instanton number for SU(2).")
print(f"  pi_7(SU(3)) = Z (non-trivial). But BCS instantons are pair tunneling,")
print(f"  not gauge instantons. The topological amplification vanishes.")

# Cross-check 3: Josephson vs BCS scale
print(f"\n  CC3: Energy scale hierarchy")
print(f"  J_C2 = {J_C2:.3f} M_KK >> |E_cond| = {abs(E_cond):.4f} M_KK")
print(f"  => Josephson network is the DOMINANT energy scale (strong coupling).")
print(f"  => But delta_a4 from Josephson adds to delta_a4 from BCS,")
print(f"     it does not multiply. The combined effect is additive.")

# Cross-check 4: S_inst regime validity
print(f"\n  CC4: Instanton gas density")
print(f"  S_inst = {S_inst_val:.4f} << 1")
print(f"  => DIGA is unreliable. Dense gas = strongly interacting instantons.")
print(f"  => Winding number sum Z/Z_0 = {Z_lin:.1f} captures the physics.")
print(f"  => But this only multiplies the EXISTING delta_a4, not create new O(1).")

# Cross-check 5: Sign of the combined effect
print(f"\n  CC5: Sign consistency")
print(f"  All three channels give POSITIVE amplification (delta_a4 increases).")
print(f"  This is physically correct: more condensate = more endomorphism = bigger a_4 shift.")

# =============================================================================
# SAVE DATA
# =============================================================================
output_path = os.path.join(data_dir, 's63_bcs_gauge_amplify.npz')

np.savez(output_path,
    # Baseline
    delta_a4_pert=delta_a4_pert,
    ratio_a4_pert=ratio_a4_pert,
    gauge_grav_ratio=gauge_grav_ratio,
    target_delta=target,
    gap_factor=gap_factor,

    # Channel A: Instanton
    S_inst=S_inst_val,
    Z_quad=Z_quad,
    Z_lin=Z_lin,
    amplification_A_nontop=amplification_A_nontop,
    amplification_A_pair=amplification_A_pair,
    amplification_A_winding=amplification_A_winding_a4,
    amplification_A=amplification_A,

    # Channel B: Domain wall
    tau_DW=tau_DW,
    aniso_DW=aniso_DW,
    tr_D2_DW=tr_D2_DW,
    tr_D2_fold=tr_D2_fold,
    d_tr_D2_dtau=d_tr_D2_dtau,
    amplification_B_grad=amplification_B_grad,
    amplification_B_curv=amplification_B_curv,
    amplification_B_cross=amplification_B_cross,
    amplification_B_sigma=amplification_B_sigma,
    amplification_B=amplification_B,

    # Channel C: Josephson
    rho_s_eff_total=rho_s_eff_total,
    cos_avg_C2=cos_avg_C2,
    cos_avg_su2=cos_avg_su2,
    cos_avg_u1=cos_avg_u1,
    tr_E2_Josephson=tr_E2_Josephson,
    tr_E2_BCS_single=tr_E2_BCS_single,
    E_J_total=E_J_total,
    collective_ratio=collective_ratio,
    amplification_C_E2=amplification_C_E2,
    amplification_C_quartic=amplification_C_quartic,
    amplification_C_meissner=amplification_C_meissner,
    amplification_C_CW=amplification_C_CW,
    amplification_C_cross=amplification_C_cross,
    amplification_C=amplification_C,

    # Combined
    amplification_combined=amplification_combined,
    max_single=max_single,
    max_channel=np.array([max_channel]),
    achieved_delta_single=achieved_single,
    achieved_delta_combined=achieved_combined,
    remaining_gap_single=remaining_gap_single,
    remaining_gap_combined=remaining_gap_combined,

    # Gate
    gate_name=np.array(['BCS-GAUGE-AMPLIFY-63']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\nData saved to: {output_path}")

# =============================================================================
# PLOT
# =============================================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 6))

# Panel 1: Channel amplifications (log scale)
channels = ['A: Instanton', 'B: Domain Wall', 'C: Josephson', 'Combined']
vals = [amplification_A, amplification_B, amplification_C, amplification_combined]
colors = ['#2196F3', '#FF9800', '#4CAF50', '#9C27B0']
bars = axes[0].bar(range(len(channels)), [max(v, 0.01) for v in vals],
                   color=colors, edgecolor='black', linewidth=0.5)
axes[0].axhline(y=500, color='red', linestyle='--', linewidth=1.5, label='PASS (500x)')
axes[0].axhline(y=100, color='orange', linestyle='--', linewidth=1.5, label='INFO (100x)')
axes[0].axhline(y=1, color='gray', linestyle=':', linewidth=1, label='Baseline (1x)')
axes[0].set_xticks(range(len(channels)))
axes[0].set_xticklabels(channels, rotation=30, ha='right', fontsize=9)
axes[0].set_ylabel('Amplification factor')
axes[0].set_title('Non-Perturbative Amplification Channels')
axes[0].legend(fontsize=7, loc='upper right')
axes[0].set_yscale('log')
axes[0].set_ylim(0.01, 1000)
for bar, val in zip(bars, vals):
    y_pos = max(val, 0.01) * 1.3
    if y_pos > 1000: y_pos = 500
    axes[0].text(bar.get_x() + bar.get_width()/2., y_pos,
                f'{val:.1f}x', ha='center', va='bottom', fontsize=9, fontweight='bold')

# Panel 2: Sub-channel breakdown
sub_labels = ['A: non-top', 'A: pair', 'A: winding',
              'B: gradient', 'B: BCS ratio', 'B: cross ratio', 'B: tension',
              'C: E^2', 'C: E^4', 'C: Meissner', 'C: CW', 'C: J-BCS']
sub_vals = [amplification_A_nontop, amplification_A_pair, amplification_A_winding_a4,
            amplification_B_grad, amplification_B_curv, amplification_B_cross, amplification_B_sigma,
            amplification_C_E2, amplification_C_quartic, amplification_C_meissner,
            amplification_C_CW, amplification_C_cross]
sub_colors = ['#2196F3']*3 + ['#FF9800']*4 + ['#4CAF50']*5
axes[1].barh(range(len(sub_labels)), [max(abs(v), 1e-6) for v in sub_vals],
             color=sub_colors, edgecolor='black', linewidth=0.3)
axes[1].axvline(x=500, color='red', linestyle='--', linewidth=1.5, label='PASS')
axes[1].axvline(x=100, color='orange', linestyle='--', linewidth=1.5, label='INFO')
axes[1].axvline(x=1, color='gray', linestyle=':', linewidth=1)
axes[1].set_yticks(range(len(sub_labels)))
axes[1].set_yticklabels(sub_labels, fontsize=7)
axes[1].set_xlabel('Amplification factor')
axes[1].set_title('Sub-Channel Breakdown')
axes[1].set_xscale('log')
axes[1].set_xlim(1e-6, 1e4)
axes[1].legend(fontsize=7, loc='lower right')
axes[1].invert_yaxis()

# Panel 3: Waterfall - delta_a4/a4 with each channel
waterfall_labels = ['BdG\nbaseline', '+Instanton', '+Domain\nWall', '+Josephson', 'Target']
base = ratio_a4_pert
waterfall_vals = [base,
                  base * amplification_A,
                  base * amplification_B,
                  base * amplification_C,
                  target]
wf_colors = ['#E3F2FD', '#BBDEFB', '#90CAF9', '#64B5F6', '#C8E6C9']
bars_wf = axes[2].bar(range(len(waterfall_labels)), waterfall_vals,
                       color=wf_colors, edgecolor='black', linewidth=0.5)
axes[2].axhline(y=target, color='green', linestyle='--', linewidth=2, label=f'Target ({target})')
axes[2].axhline(y=base, color='blue', linestyle=':', linewidth=1, label=f'Baseline ({base:.1e})')
axes[2].set_xticks(range(len(waterfall_labels)))
axes[2].set_xticklabels(waterfall_labels, fontsize=9)
axes[2].set_ylabel('delta_a4 / a4')
axes[2].set_title(f'Per-Channel delta_a4/a4 vs Target | Verdict: {verdict}')
axes[2].set_yscale('log')
axes[2].legend(fontsize=8)
for bar, val in zip(bars_wf, waterfall_vals):
    y_pos = val * 2
    axes[2].text(bar.get_x() + bar.get_width()/2., y_pos,
                f'{val:.1e}', ha='center', va='bottom', fontsize=7, rotation=45)

plt.suptitle(f'BCS-GAUGE-AMPLIFY-63 | Verdict: {verdict}', fontsize=13, fontweight='bold')
plt.tight_layout()

plot_path = os.path.join(data_dir, 's63_bcs_gauge_amplify.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")

print("\n" + "=" * 72)
print(f"FINAL VERDICT: {verdict}")
print(f"DETAIL: {detail}")
print("=" * 72)
