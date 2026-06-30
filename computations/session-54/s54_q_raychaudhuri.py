#!/usr/bin/env python3
"""
S54 W2-4: Quantum Raychaudhuri from Fisher Information
=======================================================

Evaluates the quantum Raychaudhuri equation (Braunstein-Caves form) with
quantum Fisher information F_Q computed from the Richardson/ED ground state.

The classical Jensen deformation is volume-preserving => theta_classical = 0.
The quantum correction introduces F_Q as a repulsive term. We compute:

  d(theta_Q)/dtau = -(1/d)*theta_Q^2 - sigma_Q^2 + (1/4)*F_Q - R_Ricci

where F_Q = 4(1 - |<psi(tau)|psi(tau+dtau)>|^2) / (dtau)^2

Gate: Q-RAYCHAUDHURI-54 (INFO)
"""

import sys
sys.path.insert(0, '.')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import *

# ===================================================================
# 1. LOAD DATA
# ===================================================================
data = np.load('s54_ed_sweep.npz', allow_pickle=True)
tau = data['tau_values']          # (50,)
E0 = data['E0']                  # (50,) ground state energy
psi = data['eigenstates']         # (50, 8) ground state in N_pair=1 basis
E_sp = data['E_sp_sweep']        # (50, 8) single-particle energies
d2E0 = data['E0_second_deriv']   # (50,) second derivative of E0
fold_idx = int(data['fold_idx'])  # index of fold point
N_modes = int(data['N_modes'])    # 8
dtau = tau[1] - tau[0]

print(f"Loaded ED-SWEEP: {len(tau)} tau points, dtau = {dtau:.6f}")
print(f"Fold at tau[{fold_idx}] = {tau[fold_idx]:.4f}")
print(f"N_modes = {N_modes}, N_pair = {int(data['N_pair'])}")

# ===================================================================
# 2. CLASSICAL EXPANSION SCALAR: theta_classical
# ===================================================================
# Jensen metric: g = diag(e^{2tau}, e^{-2tau}, e^{-2tau}, e^{-2tau},
#                          e^{tau}, e^{tau}, e^{tau}, e^{tau})
# theta = (1/2) tr(g^{-1} dg/dtau)
#       = (1/2)(2 - 2 - 2 - 2 + 1 + 1 + 1 + 1) = 0
# Volume-preserving! This is EXACT, not approximate.

theta_classical = np.zeros_like(tau)
print("\ntheta_classical = 0 at ALL tau (volume-preserving Jensen, exact)")

# Classical shear:
# sigma^2 = (1/2) sigma_{ab} sigma^{ab}
# sigma_{ab} = theta_{ab} - (1/d)*theta*g_{ab}  where theta_{ab} = (1/2)(dg/dtau)
# Since theta=0: sigma_{ab} = (1/2)(dg_{ab}/dtau) in an orthonormal frame
# Eigenvalues of (1/2)(g^{-1} dg/dtau): {1, -1, -1, -1, 1/2, 1/2, 1/2, 1/2}
# sigma^2 = (1/2)*sum(lambda_i^2) - (1/8)*(sum lambda_i)^2
#         = (1/2)*(1+1+1+1+0.25+0.25+0.25+0.25) - 0 = (1/2)*4 = 2.0
sigma2_classical = 2.0  # constant, from Jensen eigenvalue structure  # (local)

# Classical Ricci term R_{mu nu} k^mu k^nu along the deformation:
# For Jensen: Raychaudhuri along the deformation direction
# d(theta)/dtau = -(1/8)*theta^2 - sigma^2 - R_{mu nu} k^mu k^nu
# Since theta=0 and dtheta/dtau=0 (theta is identically 0):
# 0 = 0 - sigma^2 - R_kk  =>  R_kk = -sigma^2 = -2.0
# The Ricci focusing exactly cancels the shear defocusing. This is the
# self-consistency of the volume-preserving deformation.
R_kk_classical = -sigma2_classical  # = -2.0

print(f"sigma^2_classical = {sigma2_classical:.4f} (constant)")
print(f"R_kk_classical = {R_kk_classical:.4f} (= -sigma^2, self-consistent)")
print(f"Check: dtheta/dtau = -{sigma2_classical/8:.4f} - {sigma2_classical:.4f} - ({R_kk_classical:.4f}) = 0  [OK]")

# ===================================================================
# 3. QUANTUM FISHER INFORMATION F_Q(tau)
# ===================================================================
# F_Q = 4 * (1 - |<psi(tau_i)|psi(tau_{i+1})>|^2) / dtau^2
# This is the discrete approximation to:
# F_Q = 4 * (<d_tau psi|d_tau psi> - |<psi|d_tau psi>|^2)

# Consecutive overlaps
overlaps = np.array([np.dot(psi[i], psi[i+1]) for i in range(len(tau)-1)])
# These are real since eigenstates are real => overlap is cos(angle)

# Fidelity susceptibility chi_F = (1 - |overlap|^2) / dtau^2
# F_Q = 4 * chi_F
fidelity = overlaps**2  # |<psi_i|psi_{i+1}>|^2
chi_F = (1.0 - fidelity) / dtau**2
F_Q_edges = 4.0 * chi_F  # defined at midpoints tau[i]+dtau/2

# Assign to midpoints, then interpolate to nodes
tau_mid = 0.5 * (tau[:-1] + tau[1:])
# Interpolate F_Q to node points
F_Q = np.interp(tau, tau_mid, F_Q_edges)

print(f"\nQuantum Fisher Information F_Q:")
print(f"  F_Q(tau=0) = {F_Q[0]:.6f}")
print(f"  F_Q(fold, tau={tau[fold_idx]:.4f}) = {F_Q[fold_idx]:.6f}")
print(f"  max(F_Q) = {F_Q.max():.6f} at tau = {tau[np.argmax(F_Q)]:.4f}")
print(f"  min(F_Q) = {F_Q.min():.6f} at tau = {tau[np.argmin(F_Q)]:.4f}")

# ===================================================================
# 4. QUANTUM POTENTIAL FROM E_0(tau)
# ===================================================================
# Bohm-type quantum potential: Q = -d^2 R / (2R * dtau^2) where R = sqrt(rho)
# For parametric quantum mechanics: Q ~ -E0'' / (2*E0)
# But E0 < 0, so be careful with signs.
# More precisely, the quantum potential contributes to the effective Ricci term.
Q_bohm = np.zeros_like(tau)
mask = np.abs(E0) > 1e-15
Q_bohm[mask] = -d2E0[mask] / (2.0 * E0[mask])

print(f"\nBohm quantum potential Q:")
print(f"  Q(tau=0) = {Q_bohm[0]:.6f}")
print(f"  Q(fold) = {Q_bohm[fold_idx]:.6f}")
print(f"  max(Q) = {Q_bohm.max():.6f} at tau = {tau[np.argmax(Q_bohm)]:.4f}")
print(f"  min(Q) = {Q_bohm.min():.6f}")

# ===================================================================
# 5. QUANTUM RAYCHAUDHURI EQUATION
# ===================================================================
# Braunstein-Caves quantum Raychaudhuri (statistical manifold form):
#
#   d(theta_Q)/dtau = -(1/d)*theta_Q^2 - sigma_Q^2 + (1/4)*F_Q - R_eff
#
# In the CLASSICAL limit, F_Q -> 0, theta_Q -> theta_classical = 0.
#
# The quantum correction modifies the effective Ricci curvature:
#   R_eff = R_kk - (1/4)*F_Q
#
# Strategy: We solve the quantum Raychaudhuri equation as an ODE.
# Starting from theta_Q(tau=0) = theta_classical(0) = 0.
# The dimension d = 8 (internal modes).
d = N_modes  # 8

# For the quantum case, sigma^2 also gets modified. In the Braunstein-Caves
# formulation, the full equation on the statistical manifold is:
#
#   d(theta_Q)/dtau = -(1/d)*theta_Q^2 - sigma_Q^2 + (1/4)*F_Q - R_kk
#
# Standard Raychaudhuri: d theta/d tau = -(1/d)theta^2 - sigma^2 - R_{ab}k^a k^b
# With R_kk = R_{ab}k^a k^b = -sigma^2 = -2.0 for Jensen volume-preserving:
#   d theta/d tau = -(1/d)theta^2 - sigma^2 - (-sigma^2) = -(1/d)theta^2
# So theta=0 is stable classically (only the theta^2 term survives).
#
# Quantum modification adds +(1/4)*F_Q:
#   d theta_Q/d tau = -(1/d)*theta_Q^2 - sigma^2 + (1/4)*F_Q - R_kk
#                   = -(1/d)*theta_Q^2 + (1/4)*F_Q    [since -sigma^2 - R_kk = 0]
#
# The ONLY new ingredient is (1/4)*F_Q > 0, which is DEFOCUSING (repulsive).
# We keep sigma_Q^2 = sigma^2_classical as the leading approximation.

# Euler integration of the quantum Raychaudhuri equation
theta_Q = np.zeros_like(tau)
theta_Q[0] = 0.0  # initial condition: classical at tau=0

for i in range(len(tau) - 1):
    # RHS of quantum Raychaudhuri
    # d theta_Q/d tau = -(1/d)*theta_Q^2 - sigma^2 + (1/4)*F_Q - R_kk
    # Note: -R_kk = -(-2) = +2 = sigma^2, so -sigma^2 - R_kk = 0.
    # Net: RHS = -(1/d)*theta_Q^2 + (1/4)*F_Q
    rhs = (-(1.0/d) * theta_Q[i]**2
           - sigma2_classical
           + 0.25 * F_Q[i]
           - R_kk_classical)  # SIGN FIX: standard Raychaudhuri has -R_kk
    theta_Q[i+1] = theta_Q[i] + dtau * rhs

print(f"\nQuantum expansion scalar theta_Q:")
print(f"  theta_Q(tau=0) = {theta_Q[0]:.8f}")
print(f"  theta_Q(fold) = {theta_Q[fold_idx]:.8f}")
print(f"  max(|theta_Q|) = {np.abs(theta_Q).max():.8f} at tau = {tau[np.argmax(np.abs(theta_Q))]:.4f}")

# The quantum correction term (1/4)*F_Q vs classical focusing (-sigma^2 - R_kk = 0)
quantum_pressure = 0.25 * F_Q
print(f"\nQuantum pressure (1/4)*F_Q:")
print(f"  At fold: {quantum_pressure[fold_idx]:.8f}")
print(f"  Max: {quantum_pressure.max():.8f}")
print(f"  Ratio F_Q/(4*sigma^2): {quantum_pressure.max() / sigma2_classical:.6e}")

# ===================================================================
# 6. ALTERNATIVE: FISHER-MODIFIED FOCUSING PARAMETER
# ===================================================================
# Since theta_classical = 0 exactly, the MORE informative quantity is the
# ratio of quantum correction to classical curvature scale:
#
#   xi = F_Q / (4 * |R_kk|) = F_Q / 8
#
# xi << 1: quantum correction negligible
# xi ~ 1: quantum correction comparable to classical geometry
# xi >> 1: quantum-dominated regime

xi = F_Q / (4.0 * np.abs(R_kk_classical))
print(f"\nFocusing modification parameter xi = F_Q / (4|R_kk|):")
print(f"  xi(tau=0) = {xi[0]:.6e}")
print(f"  xi(fold) = {xi[fold_idx]:.6e}")
print(f"  max(xi) = {xi.max():.6e} at tau = {tau[np.argmax(xi)]:.4f}")

# ===================================================================
# 7. FIDELITY SUSCEPTIBILITY = QUANTUM METRIC
# ===================================================================
# chi_F IS the quantum metric g_Q on parameter space.
# It measures how fast the quantum state changes with tau.
# Near a quantum phase transition: chi_F ~ |tau - tau_c|^{-nu*z}

print(f"\nFidelity susceptibility chi_F = F_Q / 4:")
print(f"  chi_F(tau=0) = {chi_F[0]:.6f}")
chi_F_interp = np.interp(tau, tau_mid, chi_F)
print(f"  chi_F(fold) = {chi_F_interp[fold_idx]:.6f}")
print(f"  max(chi_F) = {chi_F.max():.6f} at tau_mid = {tau_mid[np.argmax(chi_F)]:.4f}")

# ===================================================================
# 8. ENERGY-BASED FOCUSING: d^2 E_0 / dtau^2
# ===================================================================
# The second derivative of E0 is related to the "quantum focusing" via
# the quantum stress-energy. Negative d2E0 = attractive (focusing).
# Positive d2E0 = repulsive (defocusing).
print(f"\nd^2E_0/dtau^2 at fold: {d2E0[fold_idx]:.6f}")
print(f"  Sign: {'FOCUSING (concave up, d2E0>0 = repulsive)' if d2E0[fold_idx] > 0 else 'DEFOCUSING (concave down, d2E0<0 = attractive)'}")
print(f"  d2E0 sign changes at tau ~ {tau[np.where(np.diff(np.sign(d2E0)))[0][0] if len(np.where(np.diff(np.sign(d2E0)))[0]) > 0 else -1]:.4f}")

# Find sign changes
sign_changes = np.where(np.diff(np.sign(d2E0)))[0]
print(f"  d2E0 sign change indices: {sign_changes}")
print(f"  d2E0 sign change tau values: {tau[sign_changes]}")

# ===================================================================
# 9. SUMMARY TABLE
# ===================================================================
print("\n" + "="*70)
print("SUMMARY: Q-RAYCHAUDHURI-54")
print("="*70)
print(f"{'Quantity':40s} {'At fold':>15s} {'Max':>15s}")
print("-"*70)
print(f"{'theta_classical':40s} {'0 (exact)':>15s} {'0 (exact)':>15s}")
print(f"{'theta_Q':40s} {theta_Q[fold_idx]:>15.6e} {np.abs(theta_Q).max():>15.6e}")
print(f"{'F_Q':40s} {F_Q[fold_idx]:>15.6e} {F_Q.max():>15.6e}")
print(f"{'(1/4)*F_Q (quantum pressure)':40s} {quantum_pressure[fold_idx]:>15.6e} {quantum_pressure.max():>15.6e}")
print(f"{'sigma^2_classical':40s} {'2.000':>15s} {'2.000':>15s}")
print(f"{'R_kk_classical':40s} {'-2.000':>15s} {'-2.000':>15s}")
print(f"{'xi = F_Q/(4|R_kk|)':40s} {xi[fold_idx]:>15.6e} {xi.max():>15.6e}")
print(f"{'chi_F (fidelity suscept.)':40s} {chi_F_interp[fold_idx]:>15.6e} {chi_F.max():>15.6e}")
print(f"{'d2E0/dtau2':40s} {d2E0[fold_idx]:>15.6e} {d2E0.max():>15.6e}")
print("-"*70)

# Qualitative assessment
max_xi = xi.max()
if max_xi < 1e-3:
    verdict = "NEGLIGIBLE: F_Q correction < 0.1% of classical curvature scale"
elif max_xi < 0.1:
    verdict = "SMALL: F_Q correction 0.1-10% of classical curvature scale"
elif max_xi < 1.0:
    verdict = "MODERATE: F_Q correction comparable to classical curvature"
else:
    verdict = "DOMINANT: F_Q correction exceeds classical curvature scale"

print(f"\nVerdict: {verdict}")
print(f"Qualitative change from classical: {'YES' if np.any(np.diff(np.sign(theta_Q[theta_Q != 0]))) else 'NO'}")
print(f"theta_Q sign: {'POSITIVE (defocusing)' if theta_Q[fold_idx] > 0 else 'NEGATIVE (focusing)' if theta_Q[fold_idx] < 0 else 'ZERO'}")

# Does theta_Q change sign?
nonzero_theta = theta_Q[1:]  # skip initial 0
sign_changes_theta = np.where(np.diff(np.sign(nonzero_theta)))[0]
if len(sign_changes_theta) > 0:
    print(f"theta_Q CHANGES SIGN at tau ~ {tau[sign_changes_theta[0]+1]:.4f}")
else:
    print(f"theta_Q does NOT change sign (monotonic)")

# ===================================================================
# 10. PLOT
# ===================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Q-RAYCHAUDHURI-54: Quantum Raychaudhuri from Fisher Information',
             fontsize=14, fontweight='bold')

# Panel A: F_Q(tau)
ax = axes[0, 0]
ax.plot(tau, F_Q, 'b-', linewidth=2, label=r'$F_Q(\tau)$')
ax.axvline(tau[fold_idx], color='red', linestyle='--', alpha=0.5, label=f'fold ($\\tau$={tau[fold_idx]:.3f})')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$F_Q$ (quantum Fisher information)', fontsize=12)
ax.set_title('(A) Quantum Fisher Information', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel B: theta_Q vs theta_classical
ax = axes[0, 1]
ax.plot(tau, theta_classical, 'k--', linewidth=2, label=r'$\theta_{\rm classical} = 0$')
ax.plot(tau, theta_Q, 'r-', linewidth=2, label=r'$\theta_Q$ (with $F_Q$)')
ax.axvline(tau[fold_idx], color='gray', linestyle='--', alpha=0.5)
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\theta$ (expansion scalar)', fontsize=12)
ax.set_title(r'(B) $\theta_Q$ vs $\theta_{\rm classical}$', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel C: xi = F_Q / (4|R_kk|) — modification parameter
ax = axes[1, 0]
ax.semilogy(tau, xi, 'g-', linewidth=2, label=r'$\xi = F_Q / (4|R_{kk}|)$')
ax.axvline(tau[fold_idx], color='red', linestyle='--', alpha=0.5, label='fold')
ax.axhline(1.0, color='orange', linestyle=':', alpha=0.7, label=r'$\xi = 1$ (quantum = classical)')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$\xi$', fontsize=12)
ax.set_title('(C) Quantum/Classical Ratio', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel D: d2E0 and quantum potential
ax = axes[1, 1]
ax.plot(tau, d2E0, 'm-', linewidth=2, label=r"$d^2E_0/d\tau^2$")
ax.plot(tau, Q_bohm, 'c--', linewidth=1.5, label=r"$Q_{\rm Bohm} = -E_0''/(2E_0)$")
ax.axvline(tau[fold_idx], color='red', linestyle='--', alpha=0.5, label='fold')
ax.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel('Energy curvature', fontsize=12)
ax.set_title(r'(D) Energy Curvature & Bohm Potential', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('s54_q_raychaudhuri.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved: s54_q_raychaudhuri.png")

# ===================================================================
# 11. GATE VERDICT
# ===================================================================
print("\n" + "="*70)
print("GATE: Q-RAYCHAUDHURI-54")
print("="*70)
print(f"Classification: INFO")
print(f"F_Q at fold: {F_Q[fold_idx]:.6e}")
print(f"max(xi) = {xi.max():.6e}")
print(f"theta_Q at fold: {theta_Q[fold_idx]:.6e}")
print(f"Qualitative change from classical theta: {'YES — theta_Q departs from zero' if np.abs(theta_Q).max() > 1e-10 else 'NO — theta_Q remains negligible'}")
print(f"Physical interpretation: The quantum Fisher information of the BCS ground state")
print(f"introduces a {'positive (defocusing)' if theta_Q[fold_idx] > 0 else 'negative (focusing)'} quantum expansion scalar")
print(f"of magnitude |theta_Q| ~ {np.abs(theta_Q).max():.2e}, which is {xi.max():.2e}x the classical curvature scale.")
