#!/usr/bin/env python3
"""
S83 Sagan audit: explicit Zubarev dressing of F_Josephson
==========================================================

Addresses Mack Q1-Q2 of the s83-w_0-regulator-adjudication workshop:
- Is rho_J R-independent (theorem) or R-dependent (by assumption)?
- What does F_Josephson become under explicit Zubarev f_R(lam) = exp(-lam^2/M_KK^2)?

The S57/S58/W3-G51 pipeline computes F_Josephson from s56_leggett_fabric:
  F_anom(tau) = Sum_k [Delta / (2 * E_qp_k^2)]
with E_qp_k = sqrt(xi_k^2 + Delta^2), xi_k = eigs_k - mu, and eigs_k the 32
tight-binding Hamiltonian eigenvalues at tau_fold. The sum uses UNIFORM mode
weight (zeta scheme, f_R=1). The "topological CPT protection" claim in S58 is
NOT a theorem derived from this formula -- it is a verbal assertion inherited
from the Volovik equilibrium-theorem argument for 3He-B ground-state
non-gravitation.

This script:
 1. Reproduces F_Josephson = -336.641 M_KK under zeta scheme (validates pipeline).
 2. Computes F_Josephson under Zubarev f_R(lam_k) = exp(-lam_k^2/M_KK^2) applied
    to the TB eigenvalue spectrum (the correct location for a spectral regulator).
 3. Compares xi_J = F_J_Zub/F_J_zeta against xi_E_GGE = 0.019646 from W3-G51.
 4. Computes w_0 under the "full Zubarev" scheme (both layers dressed) for
    adjudication of resolution (i)/(ii)/(iii).

PRE-REGISTRATION: not a gate; this is an audit computation for the S83 workshop.
Output: s83_sagan_rho_j_audit.npz (saved for reference).
"""
import sys
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from canonical_constants import Delta_BCS, M_KK, T_acoustic, N_cells, tau_fold

# ============================================================================
# Load inputs
# ============================================================================
d54 = np.load(SCRIPT_DIR / 's54_tb_hamiltonian.npz', allow_pickle=True)
d56 = np.load(SCRIPT_DIR / 's56_leggett_fabric.npz', allow_pickle=True)

taus = d54['tau_values']
fold_idx = int(np.argmin(np.abs(taus - tau_fold)))
tau_fold_val = float(taus[fold_idx])
print(f"tau_fold used: {tau_fold_val:.6f} (index {fold_idx})")

# Single-particle TB eigenvalues at fold (32-dim spectrum, M_KK units)
eigs = d54['eigenvalues'][fold_idx].copy()
print(f"TB eigenvalue range: [{eigs.min():.4f}, {eigs.max():.4f}] M_KK")

# Bond counts
adj_C2  = d54['adj_C2']
adj_su2 = d54['adj_su2']
adj_u1  = d54['adj_u1']
n_bonds_C2  = int(adj_C2.sum() // 2)
n_bonds_su2 = int(adj_su2.sum() // 2)
n_bonds_u1  = int(adj_u1.sum() // 2)
print(f"n_bonds: C2={n_bonds_C2}, su2={n_bonds_su2}, u1={n_bonds_u1}")

J_C2  = float(d54['J_C2_tau'][fold_idx])
J_su2 = float(d54['J_su2_tau'][fold_idx])
J_u1  = float(d54['J_u1_tau'][fold_idx])
print(f"J(fold): C2={J_C2:.6f}, su2={J_su2:.6f}, u1={J_u1:.6f}")

Delta = Delta_BCS
print(f"Delta (BCS gap): {Delta:.6f} M_KK")

# Fermi energy and Bogoliubov qp energies
mu   = 0.5 * (eigs[15] + eigs[16])          # (local)
xi_k = eigs - mu                            # (local)
E_qp = np.sqrt(xi_k**2 + Delta**2)          # (local)
print(f"mu (Fermi energy): {mu:.6f} M_KK")
print(f"xi_k range: [{xi_k.min():.4f}, {xi_k.max():.4f}]")
print(f"E_qp_k range: [{E_qp.min():.4f}, {E_qp.max():.4f}]")

# ============================================================================
# Step A: zeta-scheme F_anom (reproduces S56/S57 baseline)
# ============================================================================
integrand = Delta / (2.0 * E_qp**2)         # (local) BCS coherence kernel per mode
F_anom_zeta = float(np.sum(integrand))      # (local)
print(f"\n[ZETA] F_anom_zeta = {F_anom_zeta:.6f}")

E_J_C2_zeta  = J_C2**2  * F_anom_zeta       # (local)
E_J_su2_zeta = J_su2**2 * F_anom_zeta       # (local)
E_J_u1_zeta  = J_u1**2  * F_anom_zeta       # (local)

E_c = float(d56['E_c'][fold_idx])           # (local) charging energy at fold
T_GH = T_acoustic                           # GGE acoustic temperature

def cos_phi_quantum(E_J_val, E_c_val):
    return 1.0 - 1.0 / (2.0 * np.sqrt(E_J_val / E_c_val))

def cos_phi_thermal(E_J_val, T):
    if T <= 0 or E_J_val <= 0:
        return 0.0
    return -T / (2.0 * E_J_val)

m_C2_zeta  = cos_phi_quantum(E_J_C2_zeta,  E_c) + cos_phi_thermal(E_J_C2_zeta,  T_GH)                # (local)
m_su2_zeta = max(cos_phi_quantum(E_J_su2_zeta, E_c) + cos_phi_thermal(E_J_su2_zeta, T_GH), 0.0)      # (local)
m_u1_zeta  = max(cos_phi_quantum(E_J_u1_zeta,  E_c) + cos_phi_thermal(E_J_u1_zeta,  T_GH), 0.0)      # (local)

F_J_zeta = -(n_bonds_C2 * E_J_C2_zeta * m_C2_zeta
             + n_bonds_su2 * E_J_su2_zeta * m_su2_zeta
             + n_bonds_u1 * E_J_u1_zeta  * m_u1_zeta)                                                 # (local)
print(f"[ZETA] F_Josephson = {F_J_zeta:.4f} M_KK  (S58 canonical = -336.641)")
print(f"       Delta vs canonical: {abs(F_J_zeta - (-336.641)):.4f} M_KK")

# ============================================================================
# Step B: Zubarev-dressed F_anom
# ============================================================================
# The canonical W1-G1 mollifier: f_R(lam) = exp(-lam^2 / M_KK^2)
# Applied to the TB eigenvalue spectrum (the natural spectral parameter of the
# substrate D_K in the BCS tight-binding sector).
#
# The S58 F_anom sum is a discrete spectral sum over these eigenvalues.
# The regulated version:
#   F_anom_Zub = Sum_k [Delta / (2 * E_qp_k^2)] * exp(-eigs_k^2 / M_KK^2)
#
# Note: M_KK is 1.0 in M_KK units. TB eigenvalues are reported in M_KK units.
M_KK_scale = 1.0  # (local) TB spectrum already in M_KK units
f_R_Zub = np.exp(-(eigs / M_KK_scale)**2)                                                             # (local)

F_anom_Zub = float(np.sum(integrand * f_R_Zub))                                                       # (local)
xi_F_anom  = F_anom_Zub / F_anom_zeta                                                                 # (local)
print(f"\n[ZUBAREV] F_anom_Zub = {F_anom_Zub:.6f}")
print(f"[ZUBAREV] xi_F_anom  = F_anom_Zub/F_anom_zeta = {xi_F_anom:.6f}")

# Dressed bond energies
E_J_C2_Zub  = J_C2**2  * F_anom_Zub                                                                   # (local)
E_J_su2_Zub = J_su2**2 * F_anom_Zub                                                                   # (local)
E_J_u1_Zub  = J_u1**2  * F_anom_Zub                                                                   # (local)

m_C2_Zub  = cos_phi_quantum(E_J_C2_Zub,  E_c) + cos_phi_thermal(E_J_C2_Zub,  T_GH) if E_J_C2_Zub > 0 else 0.0  # (local)
m_su2_Zub = max(cos_phi_quantum(E_J_su2_Zub, E_c) + cos_phi_thermal(E_J_su2_Zub, T_GH), 0.0) if E_J_su2_Zub > 0 else 0.0  # (local)
m_u1_Zub  = max(cos_phi_quantum(E_J_u1_Zub,  E_c) + cos_phi_thermal(E_J_u1_Zub,  T_GH), 0.0) if E_J_u1_Zub > 0 else 0.0  # (local)

F_J_Zub = -(n_bonds_C2 * E_J_C2_Zub * m_C2_Zub
            + n_bonds_su2 * E_J_su2_Zub * m_su2_Zub
            + n_bonds_u1 * E_J_u1_Zub  * m_u1_Zub)                                                    # (local)
print(f"[ZUBAREV] F_Josephson = {F_J_Zub:.4f} M_KK")

xi_J = F_J_Zub / F_J_zeta                                                                             # (local)
print(f"xi_J = F_J_Zub/F_J_zeta = {xi_J:.6f}")

# ============================================================================
# Step C: Compare with W3-G51 GGE suppression
# ============================================================================
xi_E_GGE = 0.019646  # (local) from W3-G51 (energy-weighted Zubarev/zeta on L_max=5 Dirac spectrum)
print(f"\nxi_E_GGE (W3-G51, GGE E-weighted ratio): {xi_E_GGE:.6f}")
print(f"xi_J / xi_E_GGE = {xi_J / xi_E_GGE:.6f}")
print(f"  (1.0 = exact covariance, 0.0 would mean F_J is unsuppressed)")

# ============================================================================
# Step D: Recompute w_0 under three regulator schemes
# ============================================================================
rho_GGE_zeta = 1.709                              # (local) from S57 cc_sign
P_GGE_zeta   = -0.688                             # (local) from S57 cc_sign
rho_GGE_Zub  = rho_GGE_zeta * xi_E_GGE            # (local) W3-G51 dressed GGE
P_GGE_Zub    = P_GGE_zeta * xi_E_GGE              # (local) w_GGE ratio preserved

rho_J_cell_zeta = abs(F_J_zeta) / N_cells         # (local)
rho_J_cell_Zub  = abs(F_J_Zub)  / N_cells         # (local)

def w0_of(rho_J, rho_GGE, P_GGE):
    rho_vac = rho_J + rho_GGE
    P_vac   = -rho_J + P_GGE
    return P_vac / rho_vac

w_0_zeta_both    = w0_of(rho_J_cell_zeta, rho_GGE_zeta, P_GGE_zeta)                                   # (local)
w_0_Zub_GGE_only = w0_of(rho_J_cell_zeta, rho_GGE_Zub,  P_GGE_Zub)                                    # (local)
w_0_Zub_both     = w0_of(rho_J_cell_Zub,  rho_GGE_Zub,  P_GGE_Zub)                                    # (local)

print(f"\n========== w_0 UNDER THREE REGULATOR SCHEMES ==========")
print(f"Scheme (i)   zeta J + zeta GGE  [S58 canonical]     w_0 = {w_0_zeta_both:.6f}")
print(f"Scheme (ii)  zeta J + Zub GGE   [W3-G51 literal]    w_0 = {w_0_Zub_GGE_only:.6f}")
print(f"Scheme (iii) Zub  J + Zub GGE   [Sagan audit]       w_0 = {w_0_Zub_both:.6f}")
print(f"")
print(f"Target from framework canonical: w_0 = -0.918")
print(f"  |w_0_zeta_both     - (-0.918)| = {abs(w_0_zeta_both     - (-0.918)):.6f}")
print(f"  |w_0_Zub_GGE_only  - (-0.918)| = {abs(w_0_Zub_GGE_only  - (-0.918)):.6f}")
print(f"  |w_0_Zub_both      - (-0.918)| = {abs(w_0_Zub_both      - (-0.918)):.6f}")

# Hypothetical: EXACT covariance (xi_J = xi_E_GGE) -> identity preservation
print(f"\nAnalytic check: if xi_J == xi_E_GGE exactly, w_0 is identity-preserved.")
print(f"  P_Zub/rho_Zub = (xi_J*P_J_0 + xi_E*P_GGE_0) / (xi_J*rho_J_0 + xi_E*rho_GGE_0)")
print(f"  If xi_J == xi_E: factor cancels, w_0 = w_0_zeta = {w_0_zeta_both:.6f}")
print(f"  Our xi_J = {xi_J:.6f}, xi_E = {xi_E_GGE:.6f}, ratio = {xi_J/xi_E_GGE:.4f}")
print(f"  Covariance error: |1 - xi_J/xi_E| = {abs(1.0 - xi_J/xi_E_GGE):.4f}")

# ============================================================================
# Step E: Mode-by-mode diagnostic
# ============================================================================
print(f"\n========== MODE-BY-MODE DIAGNOSTIC (at fold, eigs sorted) ==========")
print(f"  {'k':>2} {'eigs':>8} {'xi':>8} {'E_qp':>8} {'integrand':>10} {'f_R_Zub':>12} {'weighted':>12}")
for k in range(32):
    w = integrand[k] * f_R_Zub[k]
    print(f"  {k:2d} {eigs[k]:+8.4f} {xi_k[k]:+8.4f} {E_qp[k]:8.4f} {integrand[k]:10.4f} {f_R_Zub[k]:12.4e} {w:12.4e}")

# ============================================================================
# Save output
# ============================================================================
out_npz = SCRIPT_DIR / 's83_sagan_rho_j_audit.npz'
np.savez(out_npz,
    eigs=eigs, xi_k=xi_k, E_qp=E_qp, integrand=integrand, f_R_Zub=f_R_Zub,
    Delta=Delta, mu=mu,
    F_anom_zeta=F_anom_zeta, F_anom_Zub=F_anom_Zub, xi_F_anom=xi_F_anom,
    F_J_zeta=F_J_zeta, F_J_Zub=F_J_Zub, xi_J=xi_J, xi_E_GGE=xi_E_GGE,
    rho_J_cell_zeta=rho_J_cell_zeta, rho_J_cell_Zub=rho_J_cell_Zub,
    rho_GGE_zeta=rho_GGE_zeta, rho_GGE_Zub=rho_GGE_Zub,
    P_GGE_zeta=P_GGE_zeta, P_GGE_Zub=P_GGE_Zub,
    w_0_zeta_both=w_0_zeta_both, w_0_Zub_GGE_only=w_0_Zub_GGE_only, w_0_Zub_both=w_0_Zub_both,
)
print(f"\nSaved: {out_npz}")

print(f"\n===================== FINAL SAGAN VERDICT =====================")
print(f"F_J_zeta = {F_J_zeta:+.3f}    [reproduces S58 canonical -336.641]")
print(f"F_J_Zub  = {F_J_Zub:+.3f}")
print(f"xi_J     = {xi_J:.6f}")
print(f"xi_E_GGE = {xi_E_GGE:.6f}")
print(f"|1 - xi_J/xi_E_GGE| = {abs(1.0 - xi_J/xi_E_GGE):.4f}  (covariance error)")
print(f"w_0 under Zub+Zub = {w_0_Zub_both:.6f}")
print(f"  distance from -0.918: {abs(w_0_Zub_both - (-0.918)):.6f}")
print(f"  distance from -0.998 (W3-G51): {abs(w_0_Zub_both - (-0.998)):.6f}")
