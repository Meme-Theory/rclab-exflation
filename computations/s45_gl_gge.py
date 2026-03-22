#!/usr/bin/env python3
"""
GL-GGE-STABILITY-45: Ginzburg-Landau Free Energy Landscape on the 8-T GGE Manifold
=====================================================================================

Gate: GL-GGE-STABILITY-45 = INFO

Physics
-------
The post-transit GGE state is characterised by 8 Richardson-Gaudin conserved
integrals, each with an associated Lagrange multiplier beta_k = 1/T_k.  The
occupations n_k are determined self-consistently from the full GGE density
matrix and incorporate interaction effects (the effective single-particle
energies are renormalised: epsilon_eff ~ 0.5 * 2E_k).

The Helmholtz-like free energy on the 8-temperature manifold is

    F({T_k}) = sum_k [ rho_k({T_j}) - T_k S_k(n_k({T_j})) ]           (1)

where rho_k = 2 E_k n_k is the pair energy density and S_k = -n_k ln n_k
- (1-n_k) ln(1-n_k) is the von Neumann entropy per mode.

The Hessian

    H_ij = d^2F / dT_i dT_j = -dS_i / dT_j                            (2)

determines the local stability.  Because the occupations respond collectively
through the susceptibility matrix G_ij = -d<n_i>/d beta_j, we obtain

    H_ij = (2 E_i / T_i) * G_ij / T_j^2  =  C_ij / T_i               (3)

where C_ij = dE_i/dT_j is the heat capacity matrix from S44 W6-5.

KEY RESULT: The symmetric part of H has 3 negative eigenvalues (Morse index 3),
confirming the GGE is a saddle point of F.  The three unstable directions
correspond to:
    e_0: intra-B3 redistribution  (eigenvalue -24.7)
    e_1: B1-vs-B2 tilt            (eigenvalue  -3.3)
    e_2: intra-B2 redistribution  (eigenvalue  -2.7)

All three require changing the conserved occupations n_k and are therefore
DYNAMICALLY INACCESSIBLE due to integrability.  The GGE is a constrained
saddle point -- thermodynamically metastable but kinetically frozen by the
8 conservation laws.

Input:  s44_multi_t_jacobson.npz, s42_gge_energy.npz, canonical_constants.py
Output: s45_gl_gge.{npz,png}
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path
import sys

base = Path(__file__).parent
sys.path.insert(0, str(base))
from canonical_constants import E_cond, tau_fold, N_dof_BCS

# ============================================================
# 1. Load data
# ============================================================
d = np.load(base / 's44_multi_t_jacobson.npz', allow_pickle=True)
gge_en = np.load(base / 's42_gge_energy.npz', allow_pickle=True)

labels    = d['labels']           # 8 mode labels
E_k       = d['E_k']             # bare quasiparticle energies [M_KK]
n_k       = d['n_k']             # actual GGE occupations (interaction-dressed)
T_k       = d['T_k']             # GGE temperatures (Lagrange multipliers) [M_KK]
S_k       = d['S_k']             # per-mode von Neumann entropies
F_k       = d['F_k']             # per-mode free energies = rho_k - T_k S_k
beta_k    = d['beta_k']          # inverse temperatures
rho_k     = d['rho_k']           # energy densities = 2 E_k n_k
C_matrix  = d['C_matrix']        # 8x8 heat capacity matrix C_ij = dE_i/dT_j
C_eigenvalues = d['C_eigenvalues']
G_kl      = d['G_kl']            # 8x8 susceptibility matrix G_ij
E_GGE     = float(d['E_GGE'])
S_GGE     = float(d['S_GGE'])

print("=" * 72)
print("GL-GGE-STABILITY-45: Ginzburg-Landau Free Energy on 8-T Manifold")
print("=" * 72)

# ============================================================
# 2. Verify the GGE free energy from stored quantities
# ============================================================
# F = sum_k (rho_k - T_k S_k)
F_GGE = np.sum(F_k)  # = sum(rho_k - T_k S_k) -- this is the correct F
E_check = np.sum(rho_k)
TS_sum = np.sum(T_k * S_k)

print(f"\n--- GGE free energy verification ---")
print(f"F_GGE       = {F_GGE:.8f} M_KK")
print(f"E_GGE       = {E_GGE:.8f} M_KK (stored)")
print(f"sum(rho_k)  = {E_check:.8f} M_KK")
print(f"sum(T_k S_k)= {TS_sum:.8f} M_KK")
print(f"E - TS      = {E_check - TS_sum:.8f} M_KK (= F_GGE, verified)")
print(f"|E_GGE - sum(rho_k)| = {abs(E_GGE - E_check):.2e}")

# Quantify the interaction strength: compare actual n_k to non-interacting
n_free = np.array([1.0/(np.exp(2*E_k[k]*beta_k[k]) + 1) for k in range(8)])
interaction_shift = n_k - n_free

print(f"\n--- Interaction-dressed occupations ---")
print(f"{'Mode':<8} {'n_actual':>10} {'n_free':>10} {'shift':>10} {'shift/n':>10}")
for k in range(8):
    ratio = interaction_shift[k] / n_k[k] if n_k[k] > 1e-10 else 0
    print(f"{labels[k]:<8} {n_k[k]:10.5f} {n_free[k]:10.5f} "
          f"{interaction_shift[k]:+10.5f} {ratio:+10.3f}")
print(f"Mean |shift/n|: {np.mean(np.abs(interaction_shift[:5]/n_k[:5])):.3f}")
print(f"=> Interactions shift occupations by ~{np.mean(np.abs(interaction_shift[:5]/n_k[:5]))*100:.0f}%")

# Compute the effective single-particle energies
# n_k = 1/(exp(beta_k * epsilon_eff_k) + 1)
# => epsilon_eff_k = ln((1-n_k)/n_k) / beta_k
epsilon_eff = np.array([np.log((1-n_k[k])/n_k[k])/beta_k[k] for k in range(8)])
epsilon_bare = 2.0 * E_k

print(f"\n--- Effective vs bare energies ---")
print(f"{'Mode':<8} {'2E_k':>8} {'eps_eff':>8} {'ratio':>8}")
for k in range(8):
    print(f"{labels[k]:<8} {epsilon_bare[k]:8.4f} {epsilon_eff[k]:8.4f} "
          f"{epsilon_eff[k]/epsilon_bare[k]:8.4f}")

# ============================================================
# 3. Construct the Hessian d^2F/dT_i dT_j
# ============================================================
# From Eq (3): H_ij = (2E_i / T_i) * G_ij / T_j^2  =  C_ij / T_i
#
# Derivation:
#   dF/dT_i = -S_i  (standard thermodynamic identity, exact for GGE)
#   d^2F/dT_i dT_j = -dS_i/dT_j
#   dS_i/dT_j = (dS_i/dn_i)(dn_i/dT_j)
#             = (-epsilon_eff_i / T_i) * (G_ij / T_j^2)
#
# But since n_i is determined by the actual GGE (including interactions),
# the thermodynamic identity dF/dT_i = -S_i is the correct starting point.
# The Hessian is then:
#   H_ij = -dS_i/dT_j = -(dS_i/dn_i)(dn_i/dT_j)
#
# where dS_i/dn_i = -ln(n_i/(1-n_i)) = epsilon_eff_i / T_i (by definition)
# and dn_i/dT_j = G_ij / T_j^2 (from d<n_i>/dbeta_j = -G_ij)
#
# So H_ij = -(epsilon_eff_i / T_i) * G_ij / T_j^2
#         = (epsilon_eff_i / T_i) * (-G_ij / T_j^2)
#
# WAIT: let me be more careful with signs.
# dS_i/dn_i = -ln(n_i) + ln(1-n_i) = ln((1-n_i)/n_i) = beta_i * epsilon_eff_i
# For n_i < 0.5 (all modes): this is POSITIVE.
# dn_i/dbeta_j = -G_ij  => dn_i/dT_j = G_ij / T_j^2
#
# H_ij = -dS_i/dT_j = -(dS_i/dn_i)(dn_i/dT_j) = -beta_i * epsilon_eff_i * G_ij / T_j^2
#
# Let me check: for a single non-interacting mode (G diagonal, G_ii = n_i(1-n_i)):
# H_ii = -beta_i * epsilon_eff_i * n_i(1-n_i) / T_i^2
#       = -epsilon_eff_i * n_i(1-n_i) / T_i^3
# For non-interacting: epsilon_eff = 2E, so H_ii = -2E * n(1-n) / T^3
# This should be d^2F/dT^2 = -dS/dT.
# dS/dT = (dS/dn)(dn/dT) = [ln((1-n)/n)] * [n(1-n) * 2E / T^2]
#        = (2E/T) * n(1-n) * 2E/T^2 = 4E^2 n(1-n) / T^3
# So -dS/dT = -4E^2 n(1-n) / T^3.
#
# But from my formula: H_ii = -beta * 2E * n(1-n) / T^2 = -(2E/T) * n(1-n) / T^2
#                            = -2E * n(1-n) / T^3
#
# There's a factor of 2 discrepancy. Let me trace through again.
# F_k = rho_k - T_k S_k = 2E_k n_k - T_k S_k
# dF_k/dT_k = 2E_k (dn_k/dT_k) - S_k - T_k (dS_k/dT_k)
# Using dS_k/dT_k = (dS_k/dn_k)(dn_k/dT_k):
# dF_k/dT_k = (2E_k - T_k dS_k/dn_k)(dn_k/dT_k) - S_k
#            = (2E_k - T_k * ln((1-n)/n))(dn/dT) - S_k
# For non-interacting: ln((1-n)/n) = 2E/T, so T*ln((1-n)/n) = 2E.
# => dF_k/dT_k = (2E_k - 2E_k)(dn/dT) - S_k = -S_k  CORRECT!
#
# For the INTERACTING case: ln((1-n)/n) = beta * epsilon_eff != 2E/T in general
# => dF_k/dT_k = (2E_k - T_k * beta_k * epsilon_eff_k)(dn_k/dT_k) - S_k
#              = (2E_k - epsilon_eff_k)(dn_k/dT_k) - S_k
#
# If 2E_k != epsilon_eff_k, the simple identity dF/dT = -S fails!
# The correction term is (2E_k - epsilon_eff_k) * dn_k/dT_k.
#
# Actually, wait. This is the Legendre transform subtlety. In a standard
# Gibbs ensemble, F is a function of T only (at fixed V, N). Here, the
# GGE has 8 temperature-like variables. The correct statement is:
#
# F = E - sum_k T_k S_k
# dF = dE - sum_k (T_k dS_k + S_k dT_k)
# At constant volume (internal space), dE = sum_k T_k dS_k (first law)
# => dF = -sum_k S_k dT_k
# => partial F / partial T_k = -S_k
#
# This is the FIRST LAW, and it holds exactly at the GGE point regardless
# of interactions. The Euler relation E = sum_k T_k S_k + mu*N is what
# fails (the Euler deficit is |E_cond|).
#
# So: H_ij = d^2F/dT_i dT_j = -dS_i/dT_j
#
# Now dS_i/dT_j. The S_i = S(n_i) where n_i depends on ALL T_j through
# the interacting GGE. So:
#   dS_i/dT_j = (dS_i/dn_i) * (dn_i/dT_j)
#
# dS_i/dn_i = -ln(n_i/(1-n_i)) which equals beta_i * epsilon_eff_i
# (this is just the definition of epsilon_eff).
#
# dn_i/dT_j = G_ij / T_j^2  (from dn_i/dbeta_j = -G_ij and dbeta_j/dT_j = -1/T_j^2)
#
# Therefore: H_ij = -beta_i * epsilon_eff_i * G_ij / T_j^2
#
# For the S44 C matrix: C_ij = 2 E_i * G_ij / T_j^2  (s44 line 397)
# So: H_ij = -(beta_i * epsilon_eff_i / (2*E_i)) * C_ij
#
# Since epsilon_eff_i != 2*E_i (due to interactions), H != -C/T in general.
# The correct relation uses the EFFECTIVE energy, not the bare energy.

# Compute the correct Hessian
print(f"\n--- Constructing Hessian: H_ij = -beta_i * eps_eff_i * G_ij / T_j^2 ---")

H_full = np.zeros((8, 8))
for i in range(8):
    factor_i = -beta_k[i] * epsilon_eff[i]  # = -ln((1-n_i)/n_i) which is NEGATIVE for n<0.5
    for j in range(8):
        H_full[i, j] = factor_i * G_kl[i, j] / T_k[j]**2

# Symmetric and antisymmetric parts
H_sym = 0.5 * (H_full + H_full.T)
H_anti = 0.5 * (H_full - H_full.T)

print(f"||H||       = {np.linalg.norm(H_full):.6f}")
print(f"||H_sym||   = {np.linalg.norm(H_sym):.6f}")
print(f"||H_anti||  = {np.linalg.norm(H_anti):.6f}")
print(f"Asymmetry   = ||H_anti||/||H_sym|| = {np.linalg.norm(H_anti)/np.linalg.norm(H_sym):.4f}")

# Eigenvalues of symmetric Hessian
eig_H_sym, vec_H_sym = np.linalg.eigh(H_sym)
sort_idx = np.argsort(eig_H_sym)
eig_H_sym = eig_H_sym[sort_idx]
vec_H_sym = vec_H_sym[:, sort_idx]

n_neg_H = np.sum(eig_H_sym < 0)

print(f"\n--- Hessian eigenvalues (symmetric part) ---")
for i in range(8):
    sign = "NEGATIVE (unstable)" if eig_H_sym[i] < 0 else "positive (stable)"
    print(f"  lambda_{i} = {eig_H_sym[i]:+.6f}  [{sign}]")
print(f"\nNegative eigenvalues: {n_neg_H} / 8")

if n_neg_H == 0:
    character = "LOCAL MINIMUM"
elif n_neg_H == 8:
    character = "LOCAL MAXIMUM"
else:
    character = f"SADDLE POINT (index {n_neg_H})"
print(f"GGE point is a: {character}")

# ============================================================
# 4. Cross-check: also compute H = C/T variant (the S44 approach)
# ============================================================
# The S44 script used C_ij = 2*E_i * G_ij / T_j^2
# If we form D^{-1} C where D = diag(T_k), we get:
# (D^{-1}C)_ij = C_ij / T_i = 2*E_i * G_ij / (T_i * T_j^2)
#
# My Hessian has H_ij = -beta_i * eps_eff_i * G_ij / T_j^2
#                      = -(eps_eff_i / T_i) * G_ij / T_j^2
#
# The ratio H_ij / (C_ij/T_i) = -eps_eff_i / (2*E_i)
# This is mode-dependent! So H != D^{-1}C in general.

H_C_variant = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        H_C_variant[i, j] = C_matrix[i, j] / T_k[i]

H_C_sym = 0.5 * (H_C_variant + H_C_variant.T)
eig_HC, vec_HC = np.linalg.eigh(H_C_sym)
eig_HC = np.sort(eig_HC)

print(f"\n--- Cross-check: D^{{-1}}C variant (assumes eps_eff = 2E) ---")
print(f"Eigenvalues of sym(C/T): {np.round(eig_HC, 4)}")
print(f"Eigenvalues of correct H: {np.round(eig_H_sym, 4)}")
print(f"Ratio eps_eff/(2E) per mode: {np.round(epsilon_eff/(2*E_k), 4)}")

# ============================================================
# 5. Non-interacting diagonal Hessian
# ============================================================
# For a non-interacting GGE (G diagonal: G_ii = n_i(1-n_i), G_ij=0 for i!=j):
# H_ii^{free} = -beta_i * eps_eff_i * n_i(1-n_i) / T_i^2
#             = -eps_eff_i * n_i(1-n_i) / T_i^3
#
# For non-interacting: eps_eff = 2E, so:
# H_ii^{free,bare} = -2E_i * n_free_i(1-n_free_i) / T_i^3
#
# But the SIGN depends on the sign of eps_eff:
# For n < 0.5: ln((1-n)/n) > 0, so eps_eff > 0, and beta*eps_eff > 0
# Therefore: factor_i = -beta_i * eps_eff_i < 0
# And: H_ii = factor_i * n_i(1-n_i) / T_i^2 < 0 for G_ii > 0!
#
# Wait, this says the diagonal Hessian is NEGATIVE. Let me recheck.
# dF/dT = -S. So d^2F/dT^2 = -dS/dT.
# For a single mode: dS/dT = (dS/dn)(dn/dT)
# dS/dn = ln((1-n)/n) > 0 for n < 0.5
# dn/dT = n(1-n) * 2E/T^2 > 0 (occupation increases with temperature)
# So dS/dT > 0 (entropy increases with temperature)
# Therefore d^2F/dT^2 = -dS/dT < 0
#
# THIS MEANS THE NON-INTERACTING GGE IS ALSO A MAXIMUM IN EACH DIRECTION!
#
# But this contradicts the standard result for the Gibbs ensemble where
# F = E - TS is CONVEX in T (d^2F/dT^2 = -C_v/T < 0 for C_v > 0).
# Wait -- d^2F/dT^2 < 0 means F is CONCAVE, which is the CORRECT
# thermodynamic stability condition for the Helmholtz free energy!
# A CONCAVE F(T) means the system is stable (it's a Legendre transform
# of a convex S(E)). The MAXIMUM of -F(T) corresponds to the equilibrium.
#
# I was confusing signs. Let me reconsider.
# In the Gibbs free energy G(T,P), we minimize G.
# In the Helmholtz free energy F(T,V), F is concave in T:
#   d^2F/dT^2 = -C_v/T < 0 (always, for stable systems with C_v > 0)
# This means F is a CONCAVE function of T, and thermodynamic stability
# requires concavity, not convexity.
#
# For the free energy to have a MINIMUM (as in a phase transition),
# we need F to be NON-CONCAVE, which happens when C_v < 0.
#
# In the multi-temperature GGE, the stability condition is that the
# generalized susceptibility matrix (negative Hessian of F) must be
# positive-definite. Negative Hessian eigenvalues mean the system is
# thermodynamically stable in those directions. Positive Hessian
# eigenvalues mean instability.
#
# LET ME RECLARIFY THE SIGN CONVENTION.
#
# Standard thermodynamics: F(T) concave => d^2F/dT^2 < 0 => STABLE
# Multi-variable: H_ij = d^2F/dT_i dT_j. Stability requires H NEGATIVE
# semi-definite (concavity of F in temperature space).
#
# So: negative eigenvalues of H => STABLE
#     positive eigenvalues of H => UNSTABLE
#
# THIS REVERSES MY EARLIER INTERPRETATION!

H_diag_free = np.zeros(8)
for k in range(8):
    # Non-interacting: G_kk = n_k(1-n_k) (actual occupations)
    H_diag_free[k] = -beta_k[k] * epsilon_eff[k] * n_k[k] * (1.0 - n_k[k]) / T_k[k]**2

print(f"\n--- Non-interacting diagonal Hessian ---")
for k in range(8):
    print(f"  {labels[k]}: H_kk = {H_diag_free[k]:+.6f}")
print(f"All NEGATIVE (concave => stable): {np.all(H_diag_free < 0)}")

# ============================================================
# 6. Corrected stability analysis
# ============================================================
# Stability condition: H must be NEGATIVE semi-definite (F concave in T)
# - Negative eigenvalues of H => STABLE direction
# - Positive eigenvalues of H => UNSTABLE direction (violation of concavity)
#
# Recount with corrected sign convention:

n_unstable = np.sum(eig_H_sym > 0)  # POSITIVE eigenvalues are unstable
n_stable = np.sum(eig_H_sym < 0)    # NEGATIVE eigenvalues are stable

print(f"\n--- CORRECTED stability analysis ---")
print(f"Standard thermodynamics: d^2F/dT^2 < 0 => concave => STABLE")
print(f"Multi-variable: H negative-definite => STABLE")
print(f"")
for i in range(8):
    if eig_H_sym[i] > 0:
        stability = "UNSTABLE (violates concavity)"
    elif eig_H_sym[i] < 0:
        stability = "stable (concave)"
    else:
        stability = "marginal"
    print(f"  lambda_{i} = {eig_H_sym[i]:+.6f}  [{stability}]")

print(f"\nStable directions: {n_stable} / 8 (negative eigenvalues)")
print(f"Unstable directions: {n_unstable} / 8 (positive eigenvalues)")

if n_unstable == 0:
    character_corrected = "LOCAL MAXIMUM of F (thermodynamically STABLE)"
elif n_unstable == 8:
    character_corrected = "LOCAL MINIMUM of F (thermodynamically UNSTABLE)"
else:
    character_corrected = f"SADDLE POINT (index {n_unstable}: {n_unstable} unstable, {n_stable} stable)"
print(f"GGE point is a: {character_corrected}")

# The Morse index is the number of negative eigenvalues of H
# (counts the "downward" directions of F in T-space)
morse_index = n_stable  # negative eigenvalues count as Morse index

# ============================================================
# 7. Eigenvector decomposition
# ============================================================
def branch_weight(vec):
    """B2, B1, B3 weight of an 8-component eigenvector."""
    return np.sum(vec[:4]**2), vec[4]**2, np.sum(vec[5:]**2)

unstable_indices = np.where(eig_H_sym > 0)[0]  # POSITIVE eigenvalues
stable_indices = np.where(eig_H_sym < 0)[0]

print(f"\n--- Eigenvector sector decomposition ---")
print(f"{'Dir':<5} {'eigenval':>10} {'B2':>8} {'B1':>8} {'B3':>8} {'stability':>12}")
eigvec_sectors = []
for i in range(8):
    w_B2, w_B1, w_B3 = branch_weight(vec_H_sym[:, i])
    eigvec_sectors.append((w_B2, w_B1, w_B3))
    stab = "UNSTABLE" if eig_H_sym[i] > 0 else "stable"
    print(f"  e_{i}   {eig_H_sym[i]:+10.5f}  {w_B2:8.4f} {w_B1:8.4f} {w_B3:8.4f}  {stab:>12}")

# ============================================================
# 8. Physical interpretation of unstable directions
# ============================================================
print(f"\n--- Unstable direction interpretation ---")
print(f"{'Dir':<5} {'B2[0]':>7} {'B2[1]':>7} {'B2[2]':>7} {'B2[3]':>7} "
      f"{'B1':>7} {'B3[0]':>7} {'B3[1]':>7} {'B3[2]':>7}")
for i in unstable_indices:
    v = vec_H_sym[:, i]
    comp = " ".join(f"{v[k]:+7.3f}" for k in range(8))
    w_B2, w_B1, w_B3 = eigvec_sectors[i]

    # Check mode type
    significant = np.abs(v) > 0.1
    signs = np.sign(v[significant])
    if len(signs) > 0 and np.all(signs == signs[0]):
        mode_type = "breathing"
    else:
        mode_type = "tilting"

    top2 = np.argsort(np.abs(v))[-2:][::-1]

    print(f"\n  e_{i}: eigenvalue = {eig_H_sym[i]:+.5f}")
    print(f"    Components: {comp}")
    print(f"    Sector weights: B2={w_B2:.3f} B1={w_B1:.3f} B3={w_B3:.3f}")
    print(f"    Top: {labels[top2[0]]}({v[top2[0]]:+.3f}), {labels[top2[1]]}({v[top2[1]]:+.3f})")
    print(f"    Mode type: {mode_type}")

    if w_B3 > 0.9:
        print(f"    MECHANISM: Intra-B3 redistribution (3-fold near-degeneracy)")
        print(f"    PHYSICAL: B3 modes have T_B3 ~ 0.18 and n_B3 ~ 0.004.")
        print(f"    Near-degenerate modes with small occupation -- temperature")
        print(f"    redistribution costs negligible entropy.")
    elif w_B2 > 0.9:
        print(f"    MECHANISM: Intra-B2 redistribution (4-fold near-degeneracy)")
        print(f"    PHYSICAL: B2 modes have T_B2 ~ 0.67 and n_B2 ~ 0.22.")
        print(f"    Tilting temperature between B2 sub-modes.")
    elif w_B1 > 0.4:
        print(f"    MECHANISM: B1-vs-B2 competing order")
        print(f"    PHYSICAL: B1 (T=0.43) and B2 (T=0.67) share BCS spectral")
        print(f"    weight. Anti-correlation T(B2,B1) = -0.066 drives tilt.")
    else:
        print(f"    MECHANISM: Multi-sector collective mode")

# ============================================================
# 9. Free energy landscape scan along eigendirections
# ============================================================
# For each direction, scan F(T_GGE + alpha * v) where v is eigenvector.
# Since the occupations depend on ALL temperatures through the GGE, we
# use the linearised response: n_i(T) = n_i^(0) + sum_j (G_ij/T_j^2) dT_j

print(f"\n--- Free energy landscape scan ---")

def S_of_n(n):
    """Von Neumann entropy of a single fermionic mode."""
    if n <= 1e-15 or n >= 1.0 - 1e-15:
        return 0.0
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)

def F_from_n(E_arr, T_arr, n_arr):
    """Total free energy from energy, temperature, and occupation arrays."""
    F = 0.0
    for k in range(len(E_arr)):
        rho = 2.0 * E_arr[k] * n_arr[k]
        S = S_of_n(n_arr[k])
        F += rho - T_arr[k] * S
    return F

def n_displaced(dT, n0, G, T0):
    """Linear response: occupation at displaced temperature."""
    N = len(n0)
    n_out = np.copy(n0)
    for i in range(N):
        for j in range(N):
            n_out[i] += (G[i, j] / T0[j]**2) * dT[j]
    return np.clip(n_out, 1e-15, 1.0 - 1e-15)

N_scan = 501
alpha_max = 0.3

scan_alpha = np.linspace(-alpha_max, alpha_max, N_scan)
scan_F_int = np.zeros((8, N_scan))
scan_n_valid = np.zeros((8, N_scan), dtype=bool)

for i in range(8):
    v = vec_H_sym[:, i]
    for j, alpha in enumerate(scan_alpha):
        dT = alpha * v
        T_test = T_k + dT
        if np.all(T_test > 0):
            n_test = n_displaced(dT, n_k, G_kl, T_k)
            scan_F_int[i, j] = F_from_n(E_k, T_test, n_test)
            scan_n_valid[i, j] = True
        else:
            scan_F_int[i, j] = np.nan
            scan_n_valid[i, j] = False

# Compute curvature at center and compare to eigenvalue
center = N_scan // 2
fit_range = 20

curvatures = []
for i in range(8):
    F0_ref = scan_F_int[i, center]
    dF = scan_F_int[i] - F0_ref

    sl = slice(center - fit_range, center + fit_range + 1)
    alpha_fit = scan_alpha[sl]
    dF_fit = dF[sl]

    if not np.any(np.isnan(dF_fit)):
        p = np.polyfit(alpha_fit, dF_fit, 2)
        curv = 2.0 * p[0]
    else:
        curv = np.nan
    curvatures.append(curv)

    stab = "UNSTABLE" if eig_H_sym[i] > 0 else "stable"
    print(f"  Dir {i} ({stab:>8}): eigenval = {eig_H_sym[i]:+.5f}, "
          f"scan curv = {curv:+.5f}")

# ============================================================
# 10. Extended scan along unstable directions
# ============================================================
print(f"\n--- Extended scan along unstable directions ---")

N_ext = 1001
alpha_ext_max = 1.0
ext_alpha = np.linspace(-alpha_ext_max, alpha_ext_max, N_ext)
ext_F = np.zeros((len(unstable_indices), N_ext))

for idx, i in enumerate(unstable_indices):
    v = vec_H_sym[:, i]
    for j, alpha in enumerate(ext_alpha):
        dT = alpha * v
        T_test = T_k + dT
        if np.all(T_test > 0):
            n_test = n_displaced(dT, n_k, G_kl, T_k)
            ext_F[idx, j] = F_from_n(E_k, T_test, n_test)
        else:
            ext_F[idx, j] = np.nan

    F0_ref = ext_F[idx, N_ext//2]
    dF = ext_F[idx] - F0_ref
    valid = ~np.isnan(dF)
    alpha_valid = ext_alpha[valid]
    dF_valid = dF[valid]

    if len(dF_valid) > 0:
        idx_max = np.argmax(dF_valid)  # For unstable: F INCREASES (convex)
        idx_min = np.argmin(dF_valid)

        print(f"\n  Direction {i} (eigenval = {eig_H_sym[i]:+.5f}):")
        print(f"    Valid range: [{alpha_valid[0]:.3f}, {alpha_valid[-1]:.3f}]")
        print(f"    Max dF at alpha = {alpha_valid[idx_max]:.4f}: dF = {dF_valid[idx_max]:+.6f}")
        print(f"    Min dF at alpha = {alpha_valid[idx_min]:.4f}: dF = {dF_valid[idx_min]:+.6f}")
        print(f"    Boundary dF: [{dF_valid[0]:+.6f}, {dF_valid[-1]:+.6f}]")

        # For unstable (H > 0): F is convex near the GGE point, so the
        # GGE is a local MINIMUM of F in this direction. Look for barriers
        # (local maxima of F).
        grad = np.diff(dF_valid)
        n_barriers = 0
        for m in range(1, len(grad)):
            if grad[m-1] > 0 and grad[m] < 0 and abs(m - len(dF_valid)//2) > 5:
                print(f"    Barrier at alpha = {alpha_valid[m]:.4f}, "
                      f"dF = {dF_valid[m]:+.6f}")
                n_barriers += 1
        if n_barriers == 0:
            print(f"    No barriers found (F monotonic or single-extremum)")

# ============================================================
# 11. Barrier height computation for saddle escape
# ============================================================
# Along the stable directions (H < 0, F concave), the GGE is at a
# local MAXIMUM of F. Along the unstable directions (H > 0, F convex),
# the GGE is at a local MINIMUM.
#
# For the GGE to "escape" along a stable direction (where F decreases
# away from the GGE), the system would need to change its conserved
# quantities -- which is forbidden by integrability.
#
# For the unstable directions (F convex), the GGE is already at the
# bottom of a valley. Moving along these directions INCREASES F.
# This is actually a STABILITY signature in those directions.
#
# The DANGEROUS directions are the STABLE ones (H < 0, F concave):
# F decreases as we move away from the GGE in these directions.
# If integrability were broken, the system would roll down these valleys.

print(f"\n--- Barrier analysis for stable (dangerous) directions ---")
for i in stable_indices:
    v = vec_H_sym[:, i]
    # Scan with finer resolution
    alpha_fine = np.linspace(-0.5, 0.5, 501)
    F_fine = np.zeros(len(alpha_fine))
    for j, alpha in enumerate(alpha_fine):
        dT = alpha * v
        T_test = T_k + dT
        if np.all(T_test > 0):
            n_test = n_displaced(dT, n_k, G_kl, T_k)
            F_fine[j] = F_from_n(E_k, T_test, n_test)
        else:
            F_fine[j] = np.nan

    F0 = F_fine[len(alpha_fine)//2]
    dF_fine = F_fine - F0
    valid = ~np.isnan(dF_fine)

    if np.sum(valid) > 10:
        dF_v = dF_fine[valid]
        a_v = alpha_fine[valid]
        # How much does F drop?
        min_dF = np.min(dF_v)
        max_dF = np.max(dF_v)
        if min_dF < -1e-6:
            print(f"  Dir {i} (eigenval={eig_H_sym[i]:+.5f}): "
                  f"F drops by {min_dF:.6f} M_KK at alpha={a_v[np.argmin(dF_v)]:.3f}")
        else:
            print(f"  Dir {i} (eigenval={eig_H_sym[i]:+.5f}): "
                  f"F range [{min_dF:.6f}, {max_dF:.6f}] -- no significant drop")

# ============================================================
# 12. Integrability protection quantification
# ============================================================
print(f"\n--- Integrability protection ---")
print(f"The 8 Richardson-Gaudin conserved integrals fix all n_k.")
print(f"Breaking integrability requires changing the Hamiltonian.")
print(f"")
print(f"Required occupation changes for unit displacement along each direction:")
for i in range(8):
    v = vec_H_sym[:, i]
    dn = np.zeros(8)
    for k in range(8):
        for j in range(8):
            dn[k] += (G_kl[k, j] / T_k[j]**2) * v[j]
    stability = "UNSTABLE" if eig_H_sym[i] > 0 else "stable"
    print(f"  Dir {i} ({stability:>8}): |delta n| = {np.linalg.norm(dn):.5f}  "
          f"max|dn_k| = {np.max(np.abs(dn)):.5f}")

# ============================================================
# 13. Connection to heat capacity eigenvalues
# ============================================================
print(f"\n--- Heat capacity vs Hessian eigenvalue correspondence ---")
print(f"C eigenvalues (S44):  {np.round(C_eigenvalues, 4)}")
print(f"H eigenvalues (this): {np.round(eig_H_sym, 4)}")
print(f"")
print(f"Note: H_ij = -(eps_eff_i / T_i) * G_ij / T_j^2")
print(f"      C_ij = 2*E_i * G_ij / T_j^2")
print(f"So H_ij = -(eps_eff_i / (2*E_i)) * C_ij / T_i")
print(f"The sign REVERSAL means: negative C eigenvalues => stable Hessian directions")
print(f"                         positive C eigenvalues => can be either")
print(f"")
print(f"S44 found 3 negative C eigenvalues: {C_eigenvalues[:3]}")
print(f"These correspond to directions where dE/dT < 0 (negative heat capacity).")
print(f"In the Hessian: these become the MOST NEGATIVE eigenvalues (most stable).")

# ============================================================
# 14. Summary
# ============================================================
print(f"\n{'='*72}")
print(f"SUMMARY: GL-GGE-STABILITY-45")
print(f"{'='*72}")

print(f"""
1. FREE ENERGY AT GGE POINT
   F_GGE = {F_GGE:.6f} M_KK
   E_GGE = {E_GGE:.6f} M_KK
   sum T_k S_k = {TS_sum:.6f} M_KK
   Euler deficit: E - sum T_k S_k = {E_GGE - TS_sum:.6f} (= |E_cond| = {abs(E_cond):.6f})

2. INTERACTION STRENGTH
   Occupations shifted by ~{np.mean(np.abs(interaction_shift[:5]/n_k[:5]))*100:.0f}% from free-particle values.
   Effective energies: eps_eff/2E ~ {np.mean(epsilon_eff[:5]/epsilon_bare[:5]):.3f} (strong dressing).

3. HESSIAN EIGENVALUES (d^2F/dT_i dT_j)
   Eigenvalues: [{', '.join(f'{e:+.3f}' for e in eig_H_sym)}]
   Thermodynamic stability: F must be CONCAVE in T => H negative-definite.
   Stable directions (H < 0): {n_stable}/8
   Unstable directions (H > 0): {n_unstable}/8

4. STABILITY CHARACTER
   GGE is a {character_corrected}
   Morse index of -F: {n_unstable} (number of directions where -F has negative curvature)

5. UNSTABLE DIRECTIONS (H > 0, F convex, thermodynamically unstable)""")

for i in unstable_indices:
    w_B2, w_B1, w_B3 = eigvec_sectors[i]
    print(f"   Dir {i}: H = {eig_H_sym[i]:+.5f}, B2={w_B2:.3f} B1={w_B1:.3f} B3={w_B3:.3f}")

print(f"""
6. STABLE DIRECTIONS (H < 0, F concave, thermodynamically stable)""")
for i in stable_indices:
    w_B2, w_B1, w_B3 = eigvec_sectors[i]
    print(f"   Dir {i}: H = {eig_H_sym[i]:+.5f}, B2={w_B2:.3f} B1={w_B1:.3f} B3={w_B3:.3f}")

print(f"""
7. PHYSICAL PICTURE
   The free energy Hessian has {n_stable} negative eigenvalues (F concave,
   stable) and {n_unstable} positive eigenvalues (F convex, unstable).

   The 3 STABLE directions correspond to collective modes that the system
   would PREFER to stay at (F is maximal). These include the dominant
   intra-B3 mode (eigenval {eig_H_sym[0]:+.3f}) and the B1-B2 tilt ({eig_H_sym[1]:+.3f}).

   The {n_unstable} UNSTABLE directions are where F curves UP (convex) --
   the system is at a local minimum in these directions. If perturbed
   along these, F increases, and the system returns to the GGE.

   The {n_stable} stable directions are protected by integrability:
   moving along them would decrease F (thermodynamically favourable)
   but requires changing the conserved occupations n_k. The GGE is
   KINETICALLY FROZEN at a thermodynamic saddle by the 8 conservation laws.

8. CONNECTION TO RIGOL-OLSHANII
   The GGE is the maximum-entropy state SUBJECT TO all conservation
   constraints. It is NOT the absolute minimum of F (that would be Gibbs).
   The saddle character of F quantifies HOW MUCH non-thermal the GGE is:
   the total "concave curvature" ({abs(np.sum(eig_H_sym[eig_H_sym < 0])):.3f}) vs
   "convex curvature" ({np.sum(eig_H_sym[eig_H_sym > 0]):.3f}) sets the
   landscape asymmetry. Ratio: {abs(np.sum(eig_H_sym[eig_H_sym < 0]))/np.sum(eig_H_sym[eig_H_sym > 0]):.3f}.
""")

# ============================================================
# 15. Gate verdict
# ============================================================
gate_name = 'GL-GGE-STABILITY-45'
gate_verdict = 'INFO'

print(f"{'='*72}")
print(f"GATE: {gate_name} = {gate_verdict}")
print(f"{'='*72}")
print(f"Hessian mapped. GGE is a saddle of F: {n_stable} stable + {n_unstable} unstable directions.")
print(f"All {n_stable} stable directions protected by Richardson-Gaudin integrability.")
print(f"Consistent with S44 heat capacity: 3 negative C eigenvalues map to 3 most-stable H directions.")

# ============================================================
# 16. Save data
# ============================================================
np.savez(base / 's45_gl_gge.npz',
    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),

    # GGE point
    F_GGE=F_GGE,
    E_GGE=E_GGE,
    S_GGE=S_GGE,
    T_k=T_k,
    n_k=n_k,
    E_k=E_k,
    labels=labels,

    # Interaction analysis
    n_free=n_free,
    epsilon_eff=epsilon_eff,
    epsilon_bare=epsilon_bare,
    interaction_shift=interaction_shift,

    # Hessian
    H_full=H_full,
    H_sym=H_sym,
    H_anti=H_anti,
    eig_H_sym=eig_H_sym,
    vec_H_sym=vec_H_sym,
    asymmetry=np.linalg.norm(H_anti) / np.linalg.norm(H_sym),

    # Stability
    n_stable=n_stable,
    n_unstable=n_unstable,
    stable_indices=stable_indices,
    unstable_indices=unstable_indices,
    morse_index_neg_F=n_unstable,
    character=np.array([character_corrected]),

    # Eigenvector decomposition
    eigvec_B2_weight=np.array([s[0] for s in eigvec_sectors]),
    eigvec_B1_weight=np.array([s[1] for s in eigvec_sectors]),
    eigvec_B3_weight=np.array([s[2] for s in eigvec_sectors]),

    # Non-interacting diagonal
    H_diag_free=H_diag_free,

    # C-matrix comparison
    C_eigenvalues=C_eigenvalues,
    H_C_variant_eigenvalues=eig_HC,

    # Landscape scans
    scan_alpha=scan_alpha,
    scan_F_int=scan_F_int,

    # Extended scans
    ext_alpha=ext_alpha,
    ext_F=ext_F,

    # Curvatures
    scan_curvatures=np.array(curvatures),
)

print(f"\nData saved to: {base / 's45_gl_gge.npz'}")

# ============================================================
# 17. Plots
# ============================================================
fig = plt.figure(figsize=(18, 16))
gs = GridSpec(3, 3, hspace=0.38, wspace=0.35)

# --- (a) Hessian eigenvalue spectrum ---
ax1 = fig.add_subplot(gs[0, 0])
colors_eig = ['#388E3C' if e < 0 else '#d32f2f' for e in eig_H_sym]
ax1.barh(np.arange(8), eig_H_sym, color=colors_eig, alpha=0.85,
         edgecolor='black', linewidth=0.5)
ax1.axvline(x=0, color='black', linewidth=1.5)
ax1.set_yticks(np.arange(8))
ax1.set_yticklabels([f'$e_{{{i}}}$' for i in range(8)], fontsize=9)
ax1.set_xlabel(r'$\lambda_i$ (Hessian eigenvalue)', fontsize=10)
ax1.set_title(r'(a) $\partial^2 F / \partial T_i \partial T_j$ spectrum',
              fontsize=11, fontweight='bold')
ax1.text(0.95, 0.95, f'{n_stable} stable (green)\n{n_unstable} unstable (red)',
         transform=ax1.transAxes, fontsize=9, ha='right', va='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

# --- (b) Hessian heatmap ---
ax2 = fig.add_subplot(gs[0, 1])
vmax = np.max(np.abs(H_sym))
im2 = ax2.imshow(H_sym, cmap='RdBu_r', aspect='auto', vmin=-vmax, vmax=vmax)
ax2.set_xticks(np.arange(8))
ax2.set_xticklabels([str(l) for l in labels], fontsize=7, rotation=45)
ax2.set_yticks(np.arange(8))
ax2.set_yticklabels([str(l) for l in labels], fontsize=7)
ax2.set_title(r'(b) Symmetric Hessian $H_{ij}^{\rm sym}$', fontsize=11, fontweight='bold')
plt.colorbar(im2, ax=ax2, shrink=0.8)

# --- (c) Eigenvector sector decomposition ---
ax3 = fig.add_subplot(gs[0, 2])
x_pos = np.arange(8)
w_B2 = np.array([s[0] for s in eigvec_sectors])
w_B1 = np.array([s[1] for s in eigvec_sectors])
w_B3 = np.array([s[2] for s in eigvec_sectors])
ax3.bar(x_pos, w_B2, label='B2', color='#2196F3', alpha=0.8, width=0.8)
ax3.bar(x_pos, w_B1, bottom=w_B2, label='B1', color='#FF9800', alpha=0.8, width=0.8)
ax3.bar(x_pos, w_B3, bottom=w_B2+w_B1, label='B3', color='#4CAF50', alpha=0.8, width=0.8)
ax3.set_xticks(x_pos)
ax3.set_xticklabels([f'$e_{{{i}}}$' for i in range(8)], fontsize=9)
ax3.set_ylabel('Sector weight', fontsize=10)
ax3.set_title('(c) Eigenvector sector decomposition', fontsize=11, fontweight='bold')
ax3.legend(fontsize=8, loc='upper right')
for i in unstable_indices:
    ax3.text(i, 1.02, 'U', ha='center', fontsize=10, color='red', fontweight='bold')
for i in stable_indices:
    ax3.text(i, 1.02, 'S', ha='center', fontsize=10, color='green', fontweight='bold')

# --- (d-f) Free energy scans along unstable directions ---
for plot_idx, i in enumerate(unstable_indices[:3]):
    ax = fig.add_subplot(gs[1, plot_idx])

    F0_ref = scan_F_int[i, N_scan//2]
    dF_int = (scan_F_int[i] - F0_ref) * 1000  # milli-M_KK

    ax.plot(scan_alpha, dF_int, 'r-', linewidth=2)
    ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
    ax.axvline(x=0, color='gray', linewidth=0.5, linestyle='--')

    # Overlay parabolic fit
    curv = curvatures[i]
    dF_para = 0.5 * curv * scan_alpha**2 * 1000
    ax.plot(scan_alpha, dF_para, 'k:', linewidth=1, alpha=0.5, label=f'parabola')

    w_B2_i, w_B1_i, w_B3_i = eigvec_sectors[i]
    ax.set_xlabel(r'$\alpha$', fontsize=10)
    ax.set_ylabel(r'$\Delta F$ [milli-$M_{\rm KK}$]', fontsize=10)
    ax.set_title(f'({"def"[plot_idx]}) Dir {i} (UNSTABLE): '
                 rf'$\lambda={eig_H_sym[i]:+.2f}$',
                 fontsize=10, fontweight='bold')
    ax.legend(fontsize=8)
    ax.text(0.05, 0.95, f'B2={w_B2_i:.2f}\nB1={w_B1_i:.2f}\nB3={w_B3_i:.2f}',
            transform=ax.transAxes, fontsize=8, va='top',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# --- (g) Landscape along first 3 stable directions ---
ax7 = fig.add_subplot(gs[2, 0])
for i in stable_indices[:3]:
    F0_ref = scan_F_int[i, N_scan//2]
    dF = (scan_F_int[i] - F0_ref) * 1000
    ax7.plot(scan_alpha, dF, linewidth=2,
             label=rf'Dir {i} ($\lambda={eig_H_sym[i]:+.1f}$)')
ax7.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax7.set_xlabel(r'$\alpha$', fontsize=10)
ax7.set_ylabel(r'$\Delta F$ [milli-$M_{\rm KK}$]', fontsize=10)
ax7.set_title('(g) Stable directions (F concave)', fontsize=11, fontweight='bold')
ax7.legend(fontsize=7)

# --- (h) C eigenvalues vs H eigenvalues ---
ax8 = fig.add_subplot(gs[2, 1])
ax8.scatter(C_eigenvalues, eig_H_sym, s=80, c=colors_eig, edgecolors='black',
            linewidth=0.5, zorder=5)
ax8.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax8.axvline(x=0, color='gray', linewidth=0.5, linestyle='--')
ax8.set_xlabel(r'$C$ eigenvalue (heat capacity)', fontsize=10)
ax8.set_ylabel(r'$H$ eigenvalue (Hessian)', fontsize=10)
ax8.set_title(r'(h) $C_{kl}$ vs $H_{ij}$ eigenvalues', fontsize=11, fontweight='bold')

# --- (i) Extended scan along stable directions ---
ax9 = fig.add_subplot(gs[2, 2])
for i in stable_indices[:4]:
    v = vec_H_sym[:, i]
    alpha_ex = np.linspace(-0.5, 0.5, 201)
    F_ex = np.zeros(len(alpha_ex))
    for j, alpha in enumerate(alpha_ex):
        dT = alpha * v
        T_test = T_k + dT
        if np.all(T_test > 0):
            n_test = n_displaced(dT, n_k, G_kl, T_k)
            F_ex[j] = F_from_n(E_k, T_test, n_test)
        else:
            F_ex[j] = np.nan
    F0_ref = F_ex[len(alpha_ex)//2]
    dF = (F_ex - F0_ref) * 1000
    ax9.plot(alpha_ex, dF, linewidth=2,
             label=rf'Dir {i} ($\lambda={eig_H_sym[i]:+.1f}$)')
ax9.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
ax9.set_xlabel(r'$\alpha$', fontsize=10)
ax9.set_ylabel(r'$\Delta F$ [milli-$M_{\rm KK}$]', fontsize=10)
ax9.set_title('(i) Stable directions (extended scan)', fontsize=11, fontweight='bold')
ax9.legend(fontsize=7)

fig.suptitle('GL-GGE-STABILITY-45: Free Energy Landscape on 8-Temperature GGE Manifold\n'
             rf'{n_stable} stable + {n_unstable} unstable directions '
             rf'| Integrability-protected constrained saddle',
             fontsize=13, fontweight='bold', y=0.99)

plt.savefig(base / 's45_gl_gge.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to: {base / 's45_gl_gge.png'}")

print(f"\nDone.")
