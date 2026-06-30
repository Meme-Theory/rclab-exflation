#!/usr/bin/env python3
"""
s66_mott_access.py — MOTT-ACCESS-66: Can Any Spectral Functional Drive E_J/E_C → 1?
======================================================================================

Gate: MOTT-ACCESS-66
  PASS: E_J/E_C < 10 for some physically motivated spectral functional
  FAIL: E_J/E_C > 100 for ALL tested functionals
  INFO: E_J/E_C reduced but still > 10

Physics:
--------
The Mott transition (E_J/E_C → 1) provides ~59 OOM CC suppression (S65 MOTT-CC-65).
The physical system sits at E_J/E_C = 194 in the cutoff action, 571x above the
critical value (QMC: 0.34). The question: does changing the spectral functional
modify E_J/E_C?

E_J and E_C are derived from the spectral action on the 32-cell tessellation:
  E_J = J_C2(tau)^2 * F_anomalous    (Josephson coupling * BCS anomalous density)
  E_C = (1/2) * level_spacing_Fermi   (charging energy from TB eigenvalues)

The tight-binding Hamiltonian H_TB = -J_eff * A_C2 has eigenvalues proportional
to J_eff. Therefore:
  E_J ∝ J_eff^2     (J_C2^2 * F_anom, where F_anom has sub-leading J_eff dependence)
  E_C ∝ J_eff       (level spacing ∝ bandwidth ∝ J_eff)
  => E_J/E_C ∝ J_eff

The J_C2 coupling at the fold is 0.933 M_KK for the CUTOFF action with f(x) = sqrt(x).
For different spectral functionals, J_C2 scales with the phase stiffness of the
corresponding spectral functional. We compute:

  1. Cutoff action: S_cutoff(tau) = sum dim^2 * sum |lambda|      [standard]
  2. Zeta action:   S_zeta(tau) = a_4(tau) = sum dim * sum lam^{-4}  [Lizzi 1412.4669]
  3. Gravity sector: S_grav(tau) = a_2(tau) = sum dim * sum lam^{-2}
  4. Anomaly-derived: S_anom(tau, phi) parameterized by conformal coupling phi
  5. Entropy cutoff:  f_S(x) = x * ln(x) / (x - 1)

For each, we compute J_C2^{func} and therefore E_J^{func}/E_C^{func}.

Key insight from ZETA-SA-66: the zeta action gradient is OPPOSITE in sign and
100x smaller in magnitude than the cutoff gradient. This dramatically changes J_eff.

Author: Lizzi Spectral Functional Theorist
Session: S66
"""

import sys, os
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    J_C2, J_su2, J_u1,
    N_cells, Delta_0_OES,
    M_KK, M_KK_gravity, M_KK_kerner,
    PI, rho_Lambda_obs,
)

# ============================================================================
# STEP 0: LOAD SPECTRAL DATA
# ============================================================================
print("=" * 78)
print("MOTT-ACCESS-66: Can Any Spectral Functional Drive E_J/E_C toward 1?")
print("=" * 78)

# Load zeta SA data from ZETA-SA-66
d_zeta = np.load(os.path.join(SCRIPT_DIR, 's66_zeta_sa.npz'), allow_pickle=True)
tau_all = d_zeta['tau_all']
S_cutoff_arr = d_zeta['S_cutoff']
a0_arr = d_zeta['a0']
a2_arr = d_zeta['a2']
a4_arr = d_zeta['a4']
a6_arr = d_zeta['a6']

# Load S57 phase diagram data
d57 = np.load(os.path.join(SCRIPT_DIR, 's57_phase_diagram.npz'), allow_pickle=True)
tau_s57 = d57['tau']
EJ_s57 = d57['E_J']
Ec_s57 = d57['E_c']
idx_fold_s57 = int(d57['idx_fold'])
z_mean = float(d57['z_mean'])
ratio_crit_QMC = float(d57['EJ_Ec_quantum_critical_QMC'])
ratio_crit_MF = float(d57['EJ_Ec_quantum_critical_MF'])

E_J_fold_cutoff = float(EJ_s57[idx_fold_s57])  # 7.0415 M_KK
E_C_fold_cutoff = float(Ec_s57[idx_fold_s57])  # 0.0363 M_KK
ratio_cutoff = E_J_fold_cutoff / E_C_fold_cutoff

print(f"\nLoaded spectral data: {len(tau_all)} tau values")
print(f"Physical E_J/E_C at fold (cutoff, S57): {ratio_cutoff:.2f}")
print(f"QMC critical ratio: {ratio_crit_QMC}")
print(f"Mean-field critical ratio: {ratio_crit_MF:.4f}")

# ============================================================================
# STEP 1: COMPUTE SPECTRAL FUNCTIONAL GRADIENTS AT FOLD
# ============================================================================
print("\n" + "=" * 78)
print("STEP 1: Spectral Functional Gradients at Fold")
print("=" * 78)

# Find fold index in the 16-point tau grid
idx_fold = np.argmin(np.abs(tau_all - tau_fold))
print(f"\nFold index: {idx_fold}, tau = {tau_all[idx_fold]:.4f}")

# Use cubic splines for more accurate derivatives
cs_cutoff = CubicSpline(tau_all, S_cutoff_arr)
cs_a2 = CubicSpline(tau_all, a2_arr)
cs_a4 = CubicSpline(tau_all, a4_arr)
cs_a6 = CubicSpline(tau_all, a6_arr)

# First and second derivatives at fold
dS_cutoff = float(cs_cutoff(tau_fold, 1))
d2S_cutoff = float(cs_cutoff(tau_fold, 2))

da2_dtau = float(cs_a2(tau_fold, 1))
d2a2_dtau2 = float(cs_a2(tau_fold, 2))

da4_dtau = float(cs_a4(tau_fold, 1))
d2a4_dtau2 = float(cs_a4(tau_fold, 2))

da6_dtau = float(cs_a6(tau_fold, 1))
d2a6_dtau2 = float(cs_a6(tau_fold, 2))

print(f"\nFirst derivatives (dS/dtau) at fold:")
print(f"  Cutoff f(x)=sqrt(x):  dS/dtau = {dS_cutoff:+.2f}")
print(f"  Zeta a_4:              da4/dtau = {da4_dtau:+.2f}")
print(f"  Gravity a_2:           da2/dtau = {da2_dtau:+.2f}")
print(f"  Higher a_6:            da6/dtau = {da6_dtau:+.2f}")

print(f"\nSecond derivatives (d2S/dtau2) at fold:")
print(f"  Cutoff f(x)=sqrt(x):  d2S/dtau2 = {d2S_cutoff:+.2f}")
print(f"  Zeta a_4:              d2a4/dtau2 = {d2a4_dtau2:+.2f}")
print(f"  Gravity a_2:           d2a2/dtau2 = {d2a2_dtau2:+.2f}")
print(f"  Higher a_6:            d2a6/dtau2 = {d2a6_dtau2:+.2f}")

# Cross-check with canonical constants
print(f"\n  Cross-check dS_fold (canonical): {dS_fold:.2f}")
print(f"  Cross-check d2S_fold (canonical): {d2S_fold:.2f}")
print(f"  Spline dS:  {dS_cutoff:.2f}  (ratio: {dS_cutoff/dS_fold:.4f})")
print(f"  Spline d2S: {d2S_cutoff:.2f}  (ratio: {d2S_cutoff/d2S_fold:.4f})")

# ============================================================================
# STEP 2: SPECTRAL FUNCTIONAL PHASE STIFFNESS RATIOS
# ============================================================================
print("\n" + "=" * 78)
print("STEP 2: Phase Stiffness Ratios (J_C2 scaling)")
print("=" * 78)

# J_C2 is the nearest-neighbor spectral action coupling.
# It measures the phase stiffness: how much the spectral action changes
# between adjacent Voronoi cells on the tessellation.
#
# The KEY ASSUMPTION: J_C2^{func} = J_C2^{cutoff} * |grad S_func| / |grad S_cutoff|
#
# This is because J_C2 was derived from the spectral action overlap
# between neighboring cells. The gradient is the spectral action's
# response to the Jensen deformation, which IS the inter-cell coupling.
#
# More precisely, from S47/S54:
#   J_C2(tau) = J_C2(fold) * exp(4 * (tau_fold - tau))
# The exponential scaling comes from the metric factor e^{4*tau} on the C^2 coset.
# The tau-dependence of J_C2 is GEOMETRIC (metric on the coset space), not
# spectral-functional-dependent.
#
# HOWEVER, the magnitude J_C2(fold) = 0.933 M_KK was computed from the
# spectral action gradient dS/dtau, normalized appropriately.
# In a different spectral functional, the gradient changes, so J_C2 changes.
#
# The gradient ratio gives the scaling of the phase stiffness.

# Ratio of functional gradients to cutoff gradient
# Use ABSOLUTE VALUES since J_C2 enters as J_C2^2 in E_J
ratio_a4_cutoff = abs(da4_dtau) / abs(dS_cutoff)
ratio_a2_cutoff = abs(da2_dtau) / abs(dS_cutoff)
ratio_a6_cutoff = abs(da6_dtau) / abs(dS_cutoff)

print(f"\nPhase stiffness ratios |grad S_func| / |grad S_cutoff|:")
print(f"  Cutoff (reference):     1.0000")
print(f"  Zeta a_4:               {ratio_a4_cutoff:.6f}  ({1/ratio_a4_cutoff:.0f}x smaller)")
print(f"  Gravity a_2:            {ratio_a2_cutoff:.6f}  ({1/ratio_a2_cutoff:.0f}x smaller)")
print(f"  Higher a_6:             {ratio_a6_cutoff:.6f}  ({1/ratio_a6_cutoff:.0f}x smaller)")

# CRITICAL: All zeta moments are ~100x smaller in gradient than the cutoff.
# This is because the cutoff action S = sum dim^2 * sum|lam| is UV-dominated
# (sensitive to large eigenvalues), while zeta sums lam^{-2k} are IR-dominated
# (sensitive to small eigenvalues). The UV eigenvalues vary MORE with tau.

# ============================================================================
# STEP 3: COMPUTE E_J AND E_C FOR EACH SPECTRAL FUNCTIONAL
# ============================================================================
print("\n" + "=" * 78)
print("STEP 3: E_J and E_C for Each Spectral Functional")
print("=" * 78)

# The Bose-Hubbard mapping from S54/S56/S57:
#
# Tight-binding Hamiltonian: H_TB = -J_eff * A_C2
# with J_eff proportional to J_C2.
#
# Eigenvalues of H_TB: epsilon_k = -J_eff * lambda_k(A_C2)
# where lambda_k are the adjacency matrix eigenvalues.
#
# E_J and E_C formulas (S56):
#   E_J = J_C2^2 * F_anomalous
#   E_C = (1/2) * level_spacing_at_Fermi_surface
#       = (1/2) * J_eff * (lambda_17 - lambda_16)  [in adjacency eigenvalue space]
#
# Since the TB eigenvalues all scale linearly with J_eff:
#   E_C ∝ J_eff ∝ J_C2
#
# And the BCS anomalous density F_anom depends on the eigenvalues relative to
# the gap Delta. When J_eff changes, xi_k = eig - mu changes, so:
#   E_qp_k = sqrt(xi_k^2 + Delta^2)
#   F_anom = sum Delta / (2 * E_qp_k^2)
#
# If we scale J_eff → alpha * J_eff:
#   xi_k → alpha * xi_k
#   E_qp_k → sqrt(alpha^2 * xi_k^2 + Delta^2)
#   F_anom → sum Delta / (2 * (alpha^2 * xi_k^2 + Delta^2))
#
# In the limit alpha * |xi_k| >> Delta (deep BCS, wide bands):
#   F_anom ~ sum Delta / (2 * alpha^2 * xi_k^2) ~ F_anom_0 / alpha^2
#   => E_J = (alpha * J_C2)^2 * F_anom_0 / alpha^2 = J_C2^2 * F_anom_0
#   => E_J is INDEPENDENT of alpha in the wide-band limit!
#
# In the narrow-band limit alpha * |xi_k| << Delta:
#   F_anom ~ sum Delta / (2 * Delta^2) = N_modes / (2 * Delta)
#   => E_J = alpha^2 * J_C2^2 * N_modes / (2 * Delta) ∝ alpha^2
#   => E_J scales as alpha^2 in the narrow-band limit!
#
# Since E_C always scales as alpha:
#   Wide-band: E_J/E_C ∝ 1/alpha (DECREASES when alpha decreases → HELPS Mott!)
#   Narrow-band: E_J/E_C ∝ alpha (INCREASES when alpha increases → same direction as cutoff)
#
# The physical system is WIDE-BAND at the cutoff level (J_C2 = 0.933, Delta = 0.464),
# so we're in the intermediate regime. Let me compute exactly.

Delta = Delta_0_OES  # 0.4643 M_KK

# Load S56 data to get the TB eigenvalues
d56_ba = np.load(os.path.join(SCRIPT_DIR, 's56_ba_spectrum.npz'), allow_pickle=True)

# Load S54 TB data for the adjacency eigenvalues
d54 = np.load(os.path.join(SCRIPT_DIR, 's54_tb_hamiltonian.npz'), allow_pickle=True)
adj_C2 = d54['adj_C2']  # (32, 32) adjacency for C2 bonds
J_C2_tau_arr = d54['J_C2_tau']
tau_s54 = d54['tau_values']
eigs_s54 = d54['eigenvalues']  # (50, 32) — TB eigenvalues

# Graph Laplacian and adjacency eigenvalues (topology-dependent, tau-independent)
A_C2 = adj_C2.astype(float)
adj_eigs_sorted = np.sort(np.linalg.eigvalsh(A_C2))[::-1]  # Descending
print(f"\nAdjacency eigenvalues (A_C2):")
print(f"  lambda_max = {adj_eigs_sorted[0]:.4f}")
print(f"  lambda_16 = {adj_eigs_sorted[15]:.4f}  (below Fermi)")
print(f"  lambda_17 = {adj_eigs_sorted[16]:.4f}  (above Fermi)")
print(f"  Fermi gap = {adj_eigs_sorted[15] - adj_eigs_sorted[16]:.6f}")
print(f"  lambda_min = {adj_eigs_sorted[-1]:.4f}")

# TB eigenvalues at fold: eps_k = -J_eff * adj_eigs (for simple hopping model)
# From S54 data directly at fold
idx_fold_s54 = np.argmin(np.abs(tau_s54 - tau_fold))
eigs_fold = eigs_s54[idx_fold_s54]  # (32,) eigenvalues
J_C2_fold_s54 = J_C2_tau_arr[idx_fold_s54]

print(f"\nTB eigenvalues at fold (S54):")
print(f"  J_C2(fold) = {J_C2_fold_s54:.4f} M_KK")
print(f"  Bandwidth = {eigs_fold.max() - eigs_fold.min():.4f} M_KK")
print(f"  Fermi level gap = {eigs_fold[16] - eigs_fold[15]:.6f} M_KK")


def compute_EJ_EC_ratio(J_eff, eigs_template, adj_eigs, Delta, z):
    """
    Compute E_J and E_C for a given effective coupling J_eff.

    The TB eigenvalues scale linearly with J_eff relative to the template.
    We use the S54 template eigenvalues, scaled by J_eff/J_eff_template.

    Parameters:
      J_eff: effective Josephson coupling (M_KK)
      eigs_template: TB eigenvalues at fold for reference J_eff
      adj_eigs: adjacency eigenvalues (tau-independent topology)
      Delta: BCS gap (M_KK)
      z: mean coordination number

    Returns: (E_J, E_C, E_J/E_C, F_anom, bandwidth)
    """
    # Scale eigenvalues
    alpha = J_eff / J_C2  # scaling factor relative to canonical J_C2
    eigs_scaled = eigs_template * alpha  # TB eigenvalues at new J_eff

    # Chemical potential at half-filling
    eigs_sorted = np.sort(eigs_scaled)
    mu = 0.5 * (eigs_sorted[15] + eigs_sorted[16])  # (local)

    # BCS quasiparticle energies
    xi_k = eigs_sorted - mu
    E_qp_k = np.sqrt(xi_k**2 + Delta**2)

    # Anomalous density
    F_anom = np.sum(Delta / (2.0 * E_qp_k**2))

    # E_J = J_C2^2 * F_anomalous (in the actual S56 formula)
    # Here J_C2 → J_eff (the spectral-functional-dependent coupling)
    E_J = J_eff**2 * F_anom

    # E_C = half the Fermi level spacing
    E_C = 0.5 * (eigs_sorted[16] - eigs_sorted[15])

    bandwidth = eigs_sorted[-1] - eigs_sorted[0]

    return E_J, E_C, E_J / max(E_C, 1e-30), F_anom, bandwidth


# The key quantity: J_C2 for each spectral functional
# J_C2^{func} / J_C2^{cutoff} = |grad S_func / grad S_cutoff|
# (This assumes the inter-cell coupling scales with the spectral action gradient)

# But wait — there is a subtlety. The J_C2 = 0.933 from S47 was computed
# from the spectral action DIFFERENCE between adjacent cells, which involves:
#   Delta S = S(tau_i) - S(tau_j)
# where tau_i and tau_j are the Jensen parameters at adjacent cells.
# The tau difference between cells comes from the tessellation geometry.
#
# The scaling with spectral functional is then:
#   J_C2^{func} / J_C2^{cutoff} = Delta S_func / Delta S_cutoff
#                                 ≈ |dS_func/dtau| / |dS_cutoff/dtau|
#
# This is the gradient ratio we computed in Step 2.

# Define spectral functionals to test
functionals = {}

# 1. Standard cutoff f(x) = sqrt(x)
functionals['cutoff'] = {
    'dS_dtau': dS_cutoff,
    'd2S_dtau2': d2S_cutoff,
    'S_fold': float(cs_cutoff(tau_fold)),
    'gradient_ratio': 1.0,
    'label': 'Cutoff $f(x) = \\sqrt{x}$',
    'color': 'blue',
}

# 2. Zeta action: S_zeta = a_4
functionals['zeta_a4'] = {
    'dS_dtau': da4_dtau,
    'd2S_dtau2': d2a4_dtau2,
    'S_fold': float(cs_a4(tau_fold)),
    'gradient_ratio': ratio_a4_cutoff,
    'label': 'Zeta $S = a_4$',
    'color': 'red',
}

# 3. Gravity sector: S = a_2
functionals['gravity_a2'] = {
    'dS_dtau': da2_dtau,
    'd2S_dtau2': d2a2_dtau2,
    'S_fold': float(cs_a2(tau_fold)),
    'gradient_ratio': ratio_a2_cutoff,
    'label': 'Gravity $S = a_2$',
    'color': 'green',
}

# 4. Higher zeta: S = a_6
functionals['zeta_a6'] = {
    'dS_dtau': da6_dtau,
    'd2S_dtau2': d2a6_dtau2,
    'S_fold': float(cs_a6(tau_fold)),
    'gradient_ratio': ratio_a6_cutoff,
    'label': 'Higher $S = a_6$',
    'color': 'purple',
}

# 5. Anomaly-derived action: S_anom = c_2(phi) * a_2 + c_4(phi) * a_4
# From ANOMALY-CONSTRAINT-66:
#   c_2(phi) = (1/2)(e^{2phi} - 1)
#   c_4(phi) = phi
# The gradient: dS_anom/dtau = c_2 * da_2/dtau + c_4 * da_4/dtau
phi_values = [-5.0, -1.0, -0.5, 0.5, 1.0, 5.0]  # Skip phi=0 (degenerate: c_2=c_4=0)
for phi in phi_values:
    c_2 = 0.5 * (np.exp(2 * phi) - 1)
    c_4 = phi
    dS_anom = c_2 * da2_dtau + c_4 * da4_dtau
    d2S_anom = c_2 * d2a2_dtau2 + c_4 * d2a4_dtau2
    S_anom_fold = c_2 * float(cs_a2(tau_fold)) + c_4 * float(cs_a4(tau_fold))
    grad_ratio = abs(dS_anom) / abs(dS_cutoff)

    key = f'anomaly_phi{phi:+.1f}'
    # Skip degenerate cases where gradient ~ 0 (no physical action)
    if abs(dS_anom) < 1e-10:
        print(f"  Skipping phi={phi}: degenerate (c_2={c_2:.4f}, c_4={c_4:.4f})")
        continue
    functionals[key] = {
        'dS_dtau': dS_anom,
        'd2S_dtau2': d2S_anom,
        'S_fold': S_anom_fold,
        'gradient_ratio': grad_ratio,
        'label': f'Anomaly $\\phi = {phi:.1f}$',
        'color': 'orange',
        'phi': phi,
        'c_2': c_2,
        'c_4': c_4,
    }

# 6. Entropy cutoff: f_S(x) = x * ln(x) / (x - 1)
# This weights each eigenvalue by its information content.
# The spectral action with this cutoff is:
#   S_entropy = sum dim^2 * sum f_S(|lambda|^2 / Lambda^2) * Lambda^2
# The gradient ratio is harder to compute analytically, but we can estimate:
# f_S(x) grows as x*ln(x) for large x, faster than sqrt(x).
# This means the entropy cutoff gives HIGHER weight to UV modes than sqrt(x).
# So the gradient should be LARGER than the cutoff gradient.
# For a crude estimate, the ratio of gradients is approximately:
#   <|lam|^2 * ln(|lam|^2)> / <|lam|>
# which, for a spectrum spanning [~1, ~30], gives a factor of ~10-30.
# We'll compute this directly from the spectrum below.

# ============================================================================
# STEP 3b: COMPUTE ENTROPY CUTOFF GRADIENT FROM SPECTRUM
# ============================================================================

# Reload spectrum at fold and nearby taus to compute entropy gradient
from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8, collect_spectrum,
)
from spectral_action import dim_su3_irrep

print("\n  Computing entropy cutoff gradients from spectrum...")

gens_su3 = su3_generators()
f_abc = compute_structure_constants(gens_su3)
gammas = build_cliff8()

# We need S_entropy at tau_fold-h, tau_fold, tau_fold+h for numerical differentiation
h = 0.01  # (local)
tau_entropy = [tau_fold - h, tau_fold, tau_fold + h]
S_entropy_vals = []

for tau_val in tau_entropy:
    _, eval_data = collect_spectrum(tau_val, gens_su3, f_abc, gammas,
                                   max_pq_sum=3, verbose=False)
    S_ent = 0.0  # (local)
    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        omega = np.abs(evals)
        # f_S(x) = x * ln(x) / (x - 1) for x = |lam|^2 / Lambda^2
        # With Lambda = 1 (dimensionless):
        x = omega**2  # x = |lam|^2
        # Avoid x = 0 and x = 1
        mask = (x > 1e-10) & (np.abs(x - 1.0) > 1e-10)
        f_S = np.zeros_like(x)
        f_S[mask] = x[mask] * np.log(x[mask]) / (x[mask] - 1.0)
        # At x = 1: f_S = 1 (L'Hopital)
        f_S[np.abs(x - 1.0) <= 1e-10] = 1.0
        S_ent += d_pq**2 * np.sum(f_S)

    S_entropy_vals.append(S_ent)

S_entropy_vals = np.array(S_entropy_vals)
dS_entropy = (S_entropy_vals[2] - S_entropy_vals[0]) / (2 * h)
d2S_entropy = (S_entropy_vals[2] - 2 * S_entropy_vals[1] + S_entropy_vals[0]) / h**2
ratio_entropy_cutoff = abs(dS_entropy) / abs(dS_cutoff)

functionals['entropy'] = {
    'dS_dtau': float(dS_entropy),
    'd2S_dtau2': float(d2S_entropy),
    'S_fold': float(S_entropy_vals[1]),
    'gradient_ratio': float(ratio_entropy_cutoff),
    'label': 'Entropy $f_S(x)$',
    'color': 'cyan',
}

print(f"  S_entropy at fold: {S_entropy_vals[1]:.2f}")
print(f"  dS_entropy/dtau: {dS_entropy:.2f}")
print(f"  Entropy/cutoff gradient ratio: {ratio_entropy_cutoff:.6f}")

# ============================================================================
# STEP 4: COMPUTE E_J/E_C FOR ALL FUNCTIONALS
# ============================================================================
print("\n" + "=" * 78)
print("STEP 4: E_J/E_C for All Spectral Functionals")
print("=" * 78)

# Reference eigenvalues at fold from S54
eigs_ref = eigs_fold  # (32,) TB eigenvalues at fold
eigs_ref_sorted = np.sort(eigs_ref)

# Reference computation (sanity check against S56/S57)
E_J_ref, E_C_ref, ratio_ref, F_anom_ref, bw_ref = compute_EJ_EC_ratio(
    J_C2, eigs_ref_sorted, adj_eigs_sorted, Delta, z_mean)

print(f"\nReference (cutoff, J_C2 = {J_C2:.3f} M_KK):")
print(f"  E_J = {E_J_ref:.4f} M_KK")
print(f"  E_C = {E_C_ref:.6f} M_KK")
print(f"  E_J/E_C = {ratio_ref:.2f}")
print(f"  F_anom = {F_anom_ref:.4f}")
print(f"  Bandwidth = {bw_ref:.4f} M_KK")
print(f"  Compare S57: E_J = {E_J_fold_cutoff:.4f}, E_C = {E_C_fold_cutoff:.6f}, "
      f"E_J/E_C = {ratio_cutoff:.2f}")

# Now compute for each functional
print(f"\n{'Functional':<25s} {'J_C2':>8s} {'E_J':>10s} {'E_C':>10s} "
      f"{'E_J/E_C':>10s} {'F_anom':>8s} {'BW':>8s}")
print("-" * 90)

results = {}
for name, func in functionals.items():
    grad_ratio = func['gradient_ratio']
    J_C2_func = J_C2 * grad_ratio
    E_J_f, E_C_f, ratio_f, F_anom_f, bw_f = compute_EJ_EC_ratio(
        J_C2_func, eigs_ref_sorted, adj_eigs_sorted, Delta, z_mean)

    results[name] = {
        'J_C2': J_C2_func,
        'E_J': E_J_f,
        'E_C': E_C_f,
        'ratio': ratio_f,
        'F_anom': F_anom_f,
        'bandwidth': bw_f,
        'gradient_ratio': grad_ratio,
    }

    print(f"  {func['label']:<23s} {J_C2_func:8.5f} {E_J_f:10.4f} {E_C_f:10.6f} "
          f"{ratio_f:10.2f} {F_anom_f:8.4f} {bw_f:8.4f}")

# ============================================================================
# STEP 5: ANALYTICAL SCALING ANALYSIS
# ============================================================================
print("\n" + "=" * 78)
print("STEP 5: Analytical Scaling of E_J/E_C with Gradient Ratio alpha")
print("=" * 78)

# Sweep alpha from 1e-4 to 100 to map the full dependence
N_alpha = 500  # (local)
log_alpha = np.linspace(-4, 2, N_alpha)
alpha_sweep = 10.0**log_alpha

EJ_sweep = np.zeros(N_alpha)
EC_sweep = np.zeros(N_alpha)
ratio_sweep = np.zeros(N_alpha)
Fanom_sweep = np.zeros(N_alpha)

for i, alpha in enumerate(alpha_sweep):
    J_eff = J_C2 * alpha
    EJ_i, EC_i, r_i, fa_i, _ = compute_EJ_EC_ratio(
        J_eff, eigs_ref_sorted, adj_eigs_sorted, Delta, z_mean)
    EJ_sweep[i] = EJ_i
    EC_sweep[i] = EC_i
    ratio_sweep[i] = r_i
    Fanom_sweep[i] = fa_i

# Find minimum E_J/E_C
idx_min_ratio = np.argmin(ratio_sweep)
alpha_min = alpha_sweep[idx_min_ratio]
ratio_min = ratio_sweep[idx_min_ratio]

print(f"\n  E_J/E_C vs alpha (gradient ratio) sweep:")
print(f"  Minimum E_J/E_C = {ratio_min:.4f} at alpha = {alpha_min:.6f}")
print(f"  E_J/E_C at alpha = 1 (cutoff): {ratio_sweep[np.argmin(np.abs(alpha_sweep - 1.0))]:.2f}")

# Mark where each functional falls
print(f"\n  Functional locations on sweep:")
for name, res in results.items():
    alpha_f = res['gradient_ratio']
    idx_near = np.argmin(np.abs(alpha_sweep - alpha_f))
    print(f"    {name:<25s}: alpha = {alpha_f:.6f}, E_J/E_C = {res['ratio']:.4f}")

# Key question: does E_J/E_C EVER drop below 10?
min_possible_ratio = ratio_min
print(f"\n  MINIMUM ACHIEVABLE E_J/E_C (over all alpha): {min_possible_ratio:.4f}")

if min_possible_ratio < 10:
    print(f"  => E_J/E_C < 10 IS achievable! (at alpha = {alpha_min:.4e})")
elif min_possible_ratio < ratio_crit_QMC:
    print(f"  => E_J/E_C < QMC critical IS achievable! (at alpha = {alpha_min:.4e})")
else:
    print(f"  => E_J/E_C never drops below 10 for any alpha")

# ============================================================================
# STEP 6: WHY E_J/E_C HAS A MINIMUM
# ============================================================================
print("\n" + "=" * 78)
print("STEP 6: Physics of the E_J/E_C Minimum")
print("=" * 78)

# E_J = J_eff^2 * F_anom(J_eff)
# E_C = (1/2) * J_eff * delta_lambda   (delta_lambda = adj gap, topology-dependent)
#
# E_J/E_C = 2 * J_eff * F_anom(J_eff) / delta_lambda
#
# F_anom = sum Delta / (2 * (alpha^2 * xi_k0^2 + Delta^2))
# where xi_k0 are the reference xi values at J_C2 = canonical
#
# d(E_J/E_C)/d(alpha) = 0 at the minimum
# This requires: d(alpha * F_anom(alpha))/d(alpha) = 0
# i.e.: F_anom + alpha * dF_anom/dalpha = 0
#
# F_anom decreases as alpha increases (bandwidth opens, BCS pairs are more delocalized)
# alpha * F_anom has a maximum at some alpha_* where the two effects balance.

# Compute alpha * F_anom
alpha_Fanom = alpha_sweep * Fanom_sweep
idx_max_aF = np.argmax(alpha_Fanom)
alpha_max_aF = alpha_sweep[idx_max_aF]

print(f"\n  alpha * F_anom maximum at alpha = {alpha_max_aF:.6f}")
print(f"  This is where E_J/E_C is maximized (not minimized)")
print(f"  E_J/E_C is minimized at the EDGES (alpha → 0 or alpha → inf)")
print(f"  At alpha → 0: narrow-band limit, E_J/E_C → 0 (Mott accessible!)")
print(f"  At alpha → inf: wide-band limit, E_J/E_C → J_C2_eff / delta_lambda")

# Actually E_J/E_C = 2 * J_eff * F_anom / delta_lambda
# = 2 * alpha * J_C2 * F_anom(alpha) / delta_lambda
# In the narrow-band limit (alpha → 0):
#   F_anom → N_modes / (2*Delta) (constant)
#   E_J/E_C → 2 * alpha * J_C2 * N_modes / (2*Delta) / delta_lambda → 0
# In the wide-band limit (alpha → inf):
#   F_anom → F_anom_ref / alpha^2
#   E_J/E_C → 2 * J_C2 * F_anom_ref / (alpha * delta_lambda) → 0 also!
#
# So E_J/E_C has a MAXIMUM at intermediate alpha, and goes to 0 at both edges!
# The minimum is at alpha → 0 or alpha → inf.

# But the PHYSICAL constraint is: alpha must come from a spectral functional.
# The smallest physical alpha is from the zeta a_4 functional: alpha ~ 0.01.
# Can we get alpha even smaller with higher zeta moments a_6, a_8, ...?

# For a_2k, the gradient ratio scales as:
# |da_{2k}/dtau| / |dS_cutoff/dtau| ∝ <lam^{-2k-1}> / <lam^0>
# As k increases, this ratio DECREASES (higher zeta = more IR sensitivity).
# So the series a_0, a_2, a_4, a_6, ... gives progressively smaller alpha.

# Compute the trend
alpha_a2 = ratio_a2_cutoff
alpha_a4 = ratio_a4_cutoff
alpha_a6 = ratio_a6_cutoff
print(f"\n  Gradient ratio trend (higher zeta moments):")
print(f"    a_2: alpha = {alpha_a2:.6f}")
print(f"    a_4: alpha = {alpha_a4:.6f}")
print(f"    a_6: alpha = {alpha_a6:.6f}")
print(f"    Ratio a_4/a_2 = {alpha_a4/alpha_a2:.4f}")
print(f"    Ratio a_6/a_4 = {alpha_a6/alpha_a4:.4f}")

# Extrapolate: for a_{2k}, alpha ~ (alpha_a4/alpha_a2)^{k-1} * alpha_a2
ratio_decay = alpha_a6 / alpha_a4
print(f"    Geometric ratio: {ratio_decay:.4f}")
for k in [4, 5, 6, 10, 20]:
    alpha_est = alpha_a6 * ratio_decay**(k - 3)
    J_eff_est = J_C2 * alpha_est
    _, _, ratio_est, _, _ = compute_EJ_EC_ratio(
        J_eff_est, eigs_ref_sorted, adj_eigs_sorted, Delta, z_mean)
    print(f"    a_{2*k}: alpha ~ {alpha_est:.2e}, "
          f"J_eff = {J_eff_est:.2e}, E_J/E_C ~ {ratio_est:.4f}")

# ============================================================================
# STEP 7: THE NARROW-BAND MOTT CROSSING
# ============================================================================
print("\n" + "=" * 78)
print("STEP 7: Narrow-Band Regime — Mott Crossing Point")
print("=" * 78)

# Find the alpha at which E_J/E_C = ratio_crit_QMC
from scipy.optimize import brentq

def ratio_minus_target(log_alpha, target):
    alpha = 10.0**log_alpha  # (local)
    J_eff = J_C2 * alpha
    _, _, ratio, _, _ = compute_EJ_EC_ratio(
        J_eff, eigs_ref_sorted, adj_eigs_sorted, Delta, z_mean)
    return ratio - target

# E_J/E_C at reference alpha=1 is ~ 194
# E_J/E_C → 0 as alpha → 0
# Find alpha where E_J/E_C = 1 (Mott boundary)
try:
    log_alpha_mott_1 = brentq(ratio_minus_target, -10, 0, args=(1.0,))
    alpha_mott_1 = 10.0**log_alpha_mott_1
    J_eff_mott_1 = J_C2 * alpha_mott_1
    print(f"\n  E_J/E_C = 1.0 at alpha = {alpha_mott_1:.4e} (J_eff = {J_eff_mott_1:.4e} M_KK)")
except:
    print(f"\n  Could not find E_J/E_C = 1.0 crossing")
    alpha_mott_1 = None

# Find alpha where E_J/E_C = ratio_crit_QMC
try:
    log_alpha_mott_qmc = brentq(ratio_minus_target, -10, 0, args=(ratio_crit_QMC,))
    alpha_mott_qmc = 10.0**log_alpha_mott_qmc
    J_eff_mott_qmc = J_C2 * alpha_mott_qmc
    print(f"  E_J/E_C = {ratio_crit_QMC} (QMC crit) at alpha = {alpha_mott_qmc:.4e} "
          f"(J_eff = {J_eff_mott_qmc:.4e} M_KK)")
except:
    print(f"  Could not find E_J/E_C = QMC critical crossing")
    alpha_mott_qmc = None

# Find alpha where E_J/E_C = 10 (gate threshold)
try:
    log_alpha_10 = brentq(ratio_minus_target, -10, 0, args=(10.0,))
    alpha_10 = 10.0**log_alpha_10
    J_eff_10 = J_C2 * alpha_10
    print(f"  E_J/E_C = 10.0 (gate) at alpha = {alpha_10:.4e} (J_eff = {J_eff_10:.4e} M_KK)")
except:
    print(f"  Could not find E_J/E_C = 10.0 crossing")
    alpha_10 = None

# Compare with actual functional alphas
print(f"\n  Comparison of functional alphas with crossing alphas:")
print(f"    Cutoff:   alpha = 1.0000     E_J/E_C = {results['cutoff']['ratio']:.2f}")
print(f"    Zeta a_4: alpha = {ratio_a4_cutoff:.6f}  E_J/E_C = {results['zeta_a4']['ratio']:.4f}")
print(f"    Zeta a_6: alpha = {ratio_a6_cutoff:.6f}  E_J/E_C = {results['zeta_a6']['ratio']:.4f}")
if alpha_10 is not None:
    print(f"    Gate<10:  alpha = {alpha_10:.6f}  (needed for E_J/E_C < 10)")
if alpha_mott_qmc is not None:
    print(f"    QMC Mott: alpha = {alpha_mott_qmc:.6f}  (needed for Mott transition)")

# Is the zeta a_4 or a_6 alpha BELOW the gate crossing alpha?
if alpha_10 is not None:
    for name in ['zeta_a4', 'gravity_a2', 'zeta_a6']:
        alpha_f = results[name]['gradient_ratio']
        if alpha_f < alpha_10:
            print(f"\n  *** {name}: alpha = {alpha_f:.6f} < {alpha_10:.6f} "
                  f"=> E_J/E_C = {results[name]['ratio']:.4f} < 10 => GATE PASS candidate!")
        else:
            print(f"\n  {name}: alpha = {alpha_f:.6f} > {alpha_10:.6f} "
                  f"=> E_J/E_C = {results[name]['ratio']:.4f} > 10")

# ============================================================================
# STEP 8: STRUCTURAL ANALYSIS — WHAT IS FUNCTIONAL-INDEPENDENT?
# ============================================================================
print("\n" + "=" * 78)
print("STEP 8: Functional-Independence Classification")
print("=" * 78)

# E_J/E_C = 2 * J_eff * F_anom / delta_lambda
# where delta_lambda = adj gap = topology-dependent, FUNCTIONAL-INDEPENDENT
# and J_eff = J_C2 * alpha where alpha is SCHEME-DEPENDENT
# and F_anom depends on the BCS gap Delta and J_eff: SCHEME-DEPENDENT

print(f"""
  FUNCTIONAL-INDEPENDENT quantities:
    - Adjacency spectrum of CG(24): delta_lambda = {adj_eigs_sorted[15] - adj_eigs_sorted[16]:.6f}
    - CG(24) topology: N_cells = {N_cells}, z_mean = {z_mean}
    - Mott transition critical ratio: (E_J/E_C)_c = {ratio_crit_QMC} (QMC)
    - BCS gap Delta = {Delta:.4f} M_KK (from OES, functional-independent at leading order)
    - Existence of the Mott transition (structural: BH model on CG(24))

  SCHEME-DEPENDENT quantities:
    - J_C2 (scales with spectral functional gradient)
    - E_J (scales as J_C2^2 * F_anom)
    - E_C (scales as J_C2 * delta_lambda)
    - E_J/E_C (the Mott control parameter)

  STRUCTURAL RESULT: The Mott ratio E_J/E_C is MAXIMALLY SCHEME-DEPENDENT.
  It ranges from 0 (alpha → 0) to ~{np.max(ratio_sweep):.0f} (peak) as a function
  of the spectral functional gradient ratio alpha.
  The cutoff action gives alpha = 1 → E_J/E_C = {results['cutoff']['ratio']:.0f}.
  The zeta action gives alpha = {ratio_a4_cutoff:.4f} → E_J/E_C = {results['zeta_a4']['ratio']:.1f}.
""")

# ============================================================================
# STEP 9: GATE VERDICT
# ============================================================================
print("=" * 78)
print("STEP 9: Gate Verdict — MOTT-ACCESS-66")
print("=" * 78)

# Check all functionals (exclude degenerate ones with alpha < 1e-8)
min_ratio_name = None
min_ratio_val = np.inf
for name, res in results.items():
    if res['gradient_ratio'] < 1e-8:
        continue  # Skip degenerate functionals
    if res['ratio'] < min_ratio_val:
        min_ratio_val = res['ratio']
        min_ratio_name = name

print(f"\n  Minimum E_J/E_C across non-degenerate functionals: {min_ratio_val:.4f} ({min_ratio_name})")
print(f"  Cutoff E_J/E_C: {results['cutoff']['ratio']:.2f}")
print(f"  QMC critical: {ratio_crit_QMC}")

# Gate assessment — exclude degenerate functionals (alpha < 1e-8)
non_degen = {k: v for k, v in results.items() if v['gradient_ratio'] > 1e-8}
all_above_100 = all(res['ratio'] > 100 for res in non_degen.values())
any_below_10 = any(res['ratio'] < 10 for res in non_degen.values())

if any_below_10:
    gate_verdict = "PASS"
    gate_detail = (
        f"E_J/E_C < 10 for {min_ratio_name} functional "
        f"(E_J/E_C = {min_ratio_val:.4f}). "
        f"The Mott transition becomes ACCESSIBLE when the spectral functional gradient "
        f"is sufficiently IR-weighted. "
        f"Physically motivated functionals (zeta a_4, a_6) achieve this."
    )
elif all_above_100:
    gate_verdict = "FAIL"
    gate_detail = (
        f"E_J/E_C > 100 for ALL tested functionals. "
        f"Minimum: {min_ratio_val:.2f} ({min_ratio_name}). "
        f"The Mott transition remains inaccessible regardless of spectral functional choice."
    )
else:
    gate_verdict = "INFO"
    gate_detail = (
        f"E_J/E_C reduced from {results['cutoff']['ratio']:.0f} (cutoff) to "
        f"{min_ratio_val:.2f} ({min_ratio_name}), but still > 10. "
        f"Direction toward Mott accessibility confirmed but not yet achieved "
        f"with tested physically motivated functionals."
    )

print(f"\nGate MOTT-ACCESS-66: {gate_verdict}")
print(f"  {gate_detail}")

# Additional context
print(f"\n  Summary of E_J/E_C across functionals:")
for name, res in sorted(results.items(), key=lambda x: x[1]['ratio']):
    marker = " ***" if res['ratio'] < 10 else ""
    print(f"    {name:<25s}: E_J/E_C = {res['ratio']:.4f} "
          f"(alpha = {res['gradient_ratio']:.6f}){marker}")

if alpha_10 is not None:
    print(f"\n  To reach E_J/E_C < 10, need alpha < {alpha_10:.6f}")
    print(f"  This requires |dS_func/dtau| / |dS_cutoff/dtau| < {alpha_10:.6f}")
    print(f"  i.e., the spectral functional gradient must be < {alpha_10*abs(dS_cutoff):.2f}")

# ============================================================================
# STEP 10: SAVE RESULTS
# ============================================================================

outpath = os.path.join(SCRIPT_DIR, 's66_mott_access.npz')
np.savez(outpath,
    # Sweep data
    alpha_sweep=alpha_sweep,
    log_alpha_sweep=log_alpha,
    EJ_sweep=EJ_sweep,
    EC_sweep=EC_sweep,
    ratio_sweep=ratio_sweep,
    Fanom_sweep=Fanom_sweep,
    # Functional results
    func_names=list(results.keys()),
    func_alphas=np.array([results[n]['gradient_ratio'] for n in results]),
    func_EJ=np.array([results[n]['E_J'] for n in results]),
    func_EC=np.array([results[n]['E_C'] for n in results]),
    func_ratios=np.array([results[n]['ratio'] for n in results]),
    func_Fanom=np.array([results[n]['F_anom'] for n in results]),
    # Crossing points
    alpha_mott_1=alpha_mott_1 if alpha_mott_1 is not None else np.nan,
    alpha_mott_qmc=alpha_mott_qmc if alpha_mott_qmc is not None else np.nan,
    alpha_gate_10=alpha_10 if alpha_10 is not None else np.nan,
    # Derivatives
    dS_cutoff_dtau=dS_cutoff,
    d2S_cutoff_dtau2=d2S_cutoff,
    da2_dtau=da2_dtau,
    d2a2_dtau2=d2a2_dtau2,
    da4_dtau=da4_dtau,
    d2a4_dtau2=d2a4_dtau2,
    da6_dtau=da6_dtau,
    d2a6_dtau2=d2a6_dtau2,
    # Physical parameters
    E_J_fold_cutoff=E_J_fold_cutoff,
    E_C_fold_cutoff=E_C_fold_cutoff,
    ratio_cutoff=ratio_cutoff,
    ratio_crit_QMC=ratio_crit_QMC,
    ratio_crit_MF=ratio_crit_MF,
    # Minimum
    min_ratio=min_ratio_val,
    min_ratio_name=min_ratio_name,
    # Gate
    gate_name='MOTT-ACCESS-66',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
)
print(f"\nSaved results to {outpath}")

# ============================================================================
# STEP 11: PLOTS
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('MOTT-ACCESS-66: E_J/E_C vs Spectral Functional', fontsize=14, fontweight='bold')

# --- Panel (a): E_J/E_C vs alpha (sweep) ---
ax = axes[0, 0]
ax.loglog(alpha_sweep, ratio_sweep, 'k-', linewidth=2, label='$E_J/E_C(\\alpha)$')
ax.axhline(y=ratio_crit_QMC, color='red', linestyle='--', linewidth=1.5,
           label=f'QMC critical = {ratio_crit_QMC}')
ax.axhline(y=10, color='orange', linestyle=':', linewidth=1.5,
           label='Gate threshold = 10')
ax.axhline(y=1, color='gray', linestyle='-.', linewidth=1,
           label='$E_J = E_C$')

# Mark functionals
func_colors = {
    'cutoff': 'blue', 'zeta_a4': 'red', 'gravity_a2': 'green',
    'zeta_a6': 'purple', 'entropy': 'cyan',
}
for name, res in results.items():
    if name in func_colors:
        ax.plot(res['gradient_ratio'], res['ratio'], 'o', color=func_colors[name],
                markersize=10, zorder=5, label=functionals[name]['label'])
    elif 'anomaly' in name:
        ax.plot(res['gradient_ratio'], res['ratio'], 's', color='orange',
                markersize=6, zorder=4)

ax.set_xlabel('Gradient ratio $\\alpha = |\\nabla S_{func}| / |\\nabla S_{cutoff}|$')
ax.set_ylabel('$E_J / E_C$')
ax.set_title('(a) Mott Ratio vs Spectral Functional Gradient')
ax.legend(fontsize=7, loc='upper left')
ax.set_xlim(1e-4, 100)
ax.set_ylim(0.01, 1000)
ax.grid(True, alpha=0.3)

# --- Panel (b): E_J and E_C separately vs alpha ---
ax = axes[0, 1]
ax.loglog(alpha_sweep, EJ_sweep, 'b-', linewidth=2, label='$E_J$')
ax.loglog(alpha_sweep, EC_sweep, 'r-', linewidth=2, label='$E_C$')

for name, res in results.items():
    if name in func_colors:
        ax.plot(res['gradient_ratio'], res['E_J'], 'o', color=func_colors[name],
                markersize=8, zorder=5)
        ax.plot(res['gradient_ratio'], res['E_C'], 's', color=func_colors[name],
                markersize=8, zorder=5)

ax.set_xlabel('Gradient ratio $\\alpha$')
ax.set_ylabel('Energy (M_KK)')
ax.set_title('(b) $E_J$ and $E_C$ vs Gradient Ratio')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# --- Panel (c): F_anom vs alpha ---
ax = axes[1, 0]
ax.semilogx(alpha_sweep, Fanom_sweep, 'k-', linewidth=2)
# Narrow-band limit
F_narrow = 32 / (2 * Delta)  # N_modes / (2 * Delta)
ax.axhline(y=F_narrow, color='gray', linestyle='--', alpha=0.5,
           label=f'Narrow-band limit = {F_narrow:.1f}')

for name, res in results.items():
    if name in func_colors:
        ax.plot(res['gradient_ratio'], res['F_anom'], 'o', color=func_colors[name],
                markersize=8, zorder=5, label=functionals[name]['label'])

ax.set_xlabel('Gradient ratio $\\alpha$')
ax.set_ylabel('$F_{anom}$ (anomalous density)')
ax.set_title('(c) BCS Anomalous Density vs Gradient Ratio')
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)

# --- Panel (d): Functional gradient comparison ---
ax = axes[1, 1]
func_names_sorted = sorted(results.keys(), key=lambda x: results[x]['ratio'], reverse=True)
y_pos = np.arange(len(func_names_sorted))
ratios_plot = [results[n]['ratio'] for n in func_names_sorted]
colors_plot = ['blue' if results[n]['ratio'] > 10 else
               ('orange' if results[n]['ratio'] > ratio_crit_QMC else 'green')
               for n in func_names_sorted]

ax.barh(y_pos, ratios_plot, color=colors_plot, alpha=0.7)
ax.set_yticks(y_pos)
ax.set_yticklabels([n.replace('_', ' ') for n in func_names_sorted], fontsize=8)
ax.set_xscale('log')
ax.axvline(x=10, color='orange', linestyle=':', linewidth=2, label='Gate < 10')
ax.axvline(x=ratio_crit_QMC, color='red', linestyle='--', linewidth=2,
           label=f'QMC critical = {ratio_crit_QMC}')
ax.axvline(x=1, color='gray', linestyle='-.', linewidth=1)
ax.set_xlabel('$E_J / E_C$')
ax.set_title('(d) E_J/E_C Across Spectral Functionals')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plotpath = os.path.join(SCRIPT_DIR, 's66_mott_access.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plotpath}")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
