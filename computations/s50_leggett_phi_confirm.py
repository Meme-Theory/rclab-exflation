#!/usr/bin/env python3
"""
Session 50: LEGGETT-PHI-CONFIRM-50 — Direct Leggett Ratio at tau ~ 0.21
========================================================================

Confirms or denies the S49 spline prediction that R(tau) = omega_L2/omega_L1
crosses phi_paasch = 1.531580 at tau = 0.2117.

S49 found:
  R(0.19) = 1.5437  (fold, 0.789% above phi_paasch)
  R(0.25) = 1.5107  (2.06% below phi_paasch)
  Spline crossing at tau = 0.2117

This script computes the Leggett eigenvalues DIRECTLY at tau = 0.20, 0.21,
0.2117, and 0.22, using the identical S48 pipeline:
  1. S46 CubicSpline interpolation for Delta_i(tau) and E_i(tau)
  2. S35 V_constrained for the Josephson coupling matrix
  3. S35 rho_i at fold, scaled by 1/E_i(tau) for tau-dependence
  4. Generalized eigenvalue problem: M v = omega^2 * diag(rho) * v
  5. R(tau) = omega_L2(tau) / omega_L1(tau)

Gate: LEGGETT-PHI-CONFIRM-50
  PASS: |R(0.21)/phi_paasch - 1| < 0.1%
  INFO: between 0.1% and 1%
  FAIL: |R(0.21)/phi_paasch - 1| > 1%

Author: Tesla-Resonance (Session 50)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.linalg import eigh
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import tau_fold, PI

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
phi_paasch = 1.531580  # Dirac eigenvalue ratio m_{(3,0)}/m_{(0,0)} from S12


# =============================================================================
#  LOAD S46 + S35 DATA (identical to S48 pipeline)
# =============================================================================

print("=" * 78)
print("SESSION 50: LEGGETT-PHI-CONFIRM-50")
print("Direct Leggett Ratio Computation at tau = 0.20, 0.21, 0.2117, 0.22")
print("=" * 78)

d46 = np.load(os.path.join(SCRIPT_DIR, 's46_qtheory_selfconsistent.npz'),
              allow_pickle=True)
d35 = np.load(os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz'),
              allow_pickle=True)
d48 = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'),
              allow_pickle=True)

# V matrix (constrained, same as S48 primary)
V_constrained = d46['V_mat_constrained']

# S35 DOS at fold
rho_B1_fold = float(d35['rho_B1'])
rho_B2_fold = float(d35['rho_B2'])
rho_B3_fold = float(d35['rho_B3'])

# S46 cubic splines for gaps and energies
tau_s46 = d46['tau_scan']
cs_D1 = CubicSpline(tau_s46, d46['Delta_B1_sc'])
cs_D2 = CubicSpline(tau_s46, d46['Delta_B2_sc'])
cs_D3 = CubicSpline(tau_s46, d46['Delta_B3_sc'])
cs_E1 = CubicSpline(tau_s46, d46['E_B1_sc'])
cs_E2 = CubicSpline(tau_s46, d46['E_B2_sc'])
cs_E3 = CubicSpline(tau_s46, d46['E_B3_sc'])

print(f"\nS46 tau range: [{tau_s46[0]:.3f}, {tau_s46[-1]:.3f}] ({len(tau_s46)} points)")
print(f"S35 rho at fold: B1={rho_B1_fold:.4f}, B2={rho_B2_fold:.4f}, B3={rho_B3_fold:.4f}")
print(f"V_constrained:\n{V_constrained}")
print(f"phi_paasch = {phi_paasch}")


# =============================================================================
#  S48 PIPELINE: Josephson mass matrix + Leggett eigenvalue problem
# =============================================================================

def compute_dos_at_tau(tau):
    """DOS at tau via 1/E scaling from fold values (S48 'spline' method)."""
    rho_fold = np.array([rho_B1_fold, rho_B2_fold, rho_B3_fold])
    E_fold = np.array([
        float(cs_E1(tau_fold)),
        float(cs_E2(tau_fold)),
        float(cs_E3(tau_fold)),
    ])
    E_tau = np.array([
        float(cs_E1(tau)),
        float(cs_E2(tau)),
        float(cs_E3(tau)),
    ])
    return rho_fold * (E_fold / E_tau)


def josephson_mass_matrix(V_mat, Delta_vec):
    """3x3 Josephson phase stiffness matrix (identical to S48)."""
    n = len(Delta_vec)
    J = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                J[i, j] = V_mat[i, j] * np.abs(Delta_vec[i]) * np.abs(Delta_vec[j])
    M = np.zeros((n, n))
    for i in range(n):
        M[i, i] = np.sum(J[i, :])
        for j in range(n):
            if i != j:
                M[i, j] = -J[i, j]
    return M, J


def leggett_at_tau(tau):
    """Compute Leggett frequencies at given tau. Returns dict of all quantities."""
    D1 = float(cs_D1(tau))
    D2 = float(cs_D2(tau))
    D3 = float(cs_D3(tau))
    Delta_vec = np.array([D1, D2, D3])

    rho_vec = compute_dos_at_tau(tau)
    M, J = josephson_mass_matrix(V_constrained, Delta_vec)

    # Generalized eigenvalue: M v = omega^2 * diag(rho) * v
    I_mat = np.diag(rho_vec)
    evals, evecs = eigh(M, I_mat)

    omega = np.zeros_like(evals)
    for i, ev in enumerate(evals):
        if ev > 1e-15:
            omega[i] = np.sqrt(ev)

    return {
        'tau': tau,
        'Delta': Delta_vec,
        'rho': rho_vec,
        'J_12': J[0, 1],
        'J_13': J[0, 2],
        'J_23': J[1, 2],
        'evals': evals,
        'omega_L1': omega[1],
        'omega_L2': omega[2],
        'R': omega[2] / omega[1] if omega[1] > 0 else np.nan,
        'evecs': evecs,
        'goldstone': evals[0],
    }


# =============================================================================
#  VALIDATION: Reproduce S48 data points
# =============================================================================

print("\n" + "-" * 78)
print("VALIDATION: Reproduce S48 coarse data")
print("-" * 78)

tau_s48 = d48['tau_scan']
oL1_s48 = d48['omega_L1_scan']
oL2_s48 = d48['omega_L2_scan']

max_rel_err_L1 = 0.0
max_rel_err_L2 = 0.0
for i, tau in enumerate(tau_s48):
    r = leggett_at_tau(tau)
    rel_L1 = abs(r['omega_L1'] - oL1_s48[i]) / oL1_s48[i]
    rel_L2 = abs(r['omega_L2'] - oL2_s48[i]) / oL2_s48[i]
    max_rel_err_L1 = max(max_rel_err_L1, rel_L1)
    max_rel_err_L2 = max(max_rel_err_L2, rel_L2)
    R_here = r['omega_L2'] / r['omega_L1']
    R_s48 = oL2_s48[i] / oL1_s48[i]
    print(f"  tau={tau:.2f}: L1={r['omega_L1']:.8f} (S48: {oL1_s48[i]:.8f}, err={rel_L1:.2e}), "
          f"L2={r['omega_L2']:.8f} (S48: {oL2_s48[i]:.8f}, err={rel_L2:.2e}), "
          f"R={R_here:.6f} (S48: {R_s48:.6f})")

print(f"\n  Max relative error: L1={max_rel_err_L1:.2e}, L2={max_rel_err_L2:.2e}")
validation_pass = max_rel_err_L1 < 1e-10 and max_rel_err_L2 < 1e-10
print(f"  Validation: {'PASS' if validation_pass else 'FAIL'}")

if not validation_pass:
    print("  WARNING: Cannot reproduce S48 data. Results may be unreliable.")


# =============================================================================
#  NEW COMPUTATION: tau = 0.20, 0.21, 0.2117, 0.22
# =============================================================================

print("\n" + "=" * 78)
print("NEW COMPUTATION: Leggett modes at tau = 0.20, 0.21, 0.2117, 0.22")
print("=" * 78)

tau_new = [0.20, 0.21, 0.2117, 0.22]
results_new = []

for tau in tau_new:
    r = leggett_at_tau(tau)
    results_new.append(r)
    mismatch = abs(r['R'] / phi_paasch - 1.0)
    print(f"\n  tau = {tau:.4f}:")
    print(f"    Delta = [{r['Delta'][0]:.6f}, {r['Delta'][1]:.6f}, {r['Delta'][2]:.6f}]")
    print(f"    rho   = [{r['rho'][0]:.6f}, {r['rho'][1]:.6f}, {r['rho'][2]:.6f}]")
    print(f"    J_12  = {r['J_12']:.8f},  J_23 = {r['J_23']:.8f},  J_12/J_23 = {r['J_12']/r['J_23']:.6f}")
    print(f"    omega_L1 = {r['omega_L1']:.8f}")
    print(f"    omega_L2 = {r['omega_L2']:.8f}")
    print(f"    R = omega_L2/omega_L1 = {r['R']:.10f}")
    print(f"    phi_paasch            = {phi_paasch:.10f}")
    print(f"    |R/phi - 1|           = {mismatch:.10f} ({mismatch*100:.6f}%)")
    print(f"    Goldstone eigenvalue  = {r['goldstone']:.2e}")


# =============================================================================
#  BRACKETING AND REFINED CROSSING
# =============================================================================

print("\n" + "=" * 78)
print("CROSSING ANALYSIS")
print("=" * 78)

# Build a dense direct-computation scan around the crossing region
tau_dense = np.linspace(0.19, 0.25, 61)
R_dense = np.zeros_like(tau_dense)
oL1_dense = np.zeros_like(tau_dense)
oL2_dense = np.zeros_like(tau_dense)

for i, tau in enumerate(tau_dense):
    r = leggett_at_tau(tau)
    R_dense[i] = r['R']
    oL1_dense[i] = r['omega_L1']
    oL2_dense[i] = r['omega_L2']

# Spline on the direct-computation dense scan
cs_R_direct = CubicSpline(tau_dense, R_dense)

# Find crossing with Brent
def R_minus_phi(tau):
    return cs_R_direct(tau) - phi_paasch

# Check for sign change
delta_dense = R_dense - phi_paasch
crossings = []
for i in range(len(delta_dense) - 1):
    if delta_dense[i] * delta_dense[i+1] < 0:
        tau_cross = brentq(R_minus_phi, tau_dense[i], tau_dense[i+1], xtol=1e-14)
        crossings.append(tau_cross)

if crossings:
    tau_cross = crossings[0]
    r_cross = leggett_at_tau(tau_cross)
    mismatch_cross = abs(r_cross['R'] / phi_paasch - 1.0)
    print(f"\n  Crossing found at tau = {tau_cross:.12f}")
    print(f"  R(tau_cross) = {r_cross['R']:.12f}")
    print(f"  phi_paasch   = {phi_paasch:.12f}")
    print(f"  |R/phi - 1|  = {mismatch_cross:.2e}")
    print(f"  S49 spline prediction: tau = 0.211686")
    print(f"  |tau_cross - tau_S49| = {abs(tau_cross - 0.211686):.6f}")
else:
    print("\n  No crossing found in [0.19, 0.25]")
    # Find closest approach
    idx_min = np.argmin(np.abs(delta_dense))
    print(f"  Closest approach: tau={tau_dense[idx_min]:.4f}, R={R_dense[idx_min]:.6f}, "
          f"|R/phi-1|={abs(R_dense[idx_min]/phi_paasch - 1.0)*100:.4f}%")


# =============================================================================
#  EXTENDED SCAN: Full range for plot context
# =============================================================================

tau_full = np.linspace(0.05, 0.35, 301)
R_full = np.zeros_like(tau_full)
for i, tau in enumerate(tau_full):
    r = leggett_at_tau(tau)
    R_full[i] = r['R']


# =============================================================================
#  GATE VERDICT
# =============================================================================

print("\n" + "=" * 78)
print("GATE: LEGGETT-PHI-CONFIRM-50")
print("=" * 78)

# Primary gate: R at tau = 0.21
r_021 = results_new[1]  # tau = 0.21
mismatch_021 = abs(r_021['R'] / phi_paasch - 1.0)

print(f"\n  R(0.21) = {r_021['R']:.10f}")
print(f"  phi_paasch = {phi_paasch:.10f}")
print(f"  |R(0.21)/phi - 1| = {mismatch_021:.10f} ({mismatch_021*100:.6f}%)")

if mismatch_021 < 0.001:
    verdict = "PASS"
    detail = f"|R(0.21)/phi - 1| = {mismatch_021*100:.4f}% < 0.1%"
elif mismatch_021 < 0.01:
    verdict = "INFO"
    detail = f"|R(0.21)/phi - 1| = {mismatch_021*100:.4f}%, between 0.1% and 1%"
else:
    verdict = "FAIL"
    detail = f"|R(0.21)/phi - 1| = {mismatch_021*100:.4f}% > 1%"

print(f"\n  VERDICT: {verdict}")
print(f"  {detail}")

# Additional context
print(f"\n  Bracket:")
r_020 = results_new[0]
r_022 = results_new[3]
r_02117 = results_new[2]
print(f"    R(0.20) = {r_020['R']:.10f}, |R/phi-1| = {abs(r_020['R']/phi_paasch-1)*100:.6f}%")
print(f"    R(0.21) = {r_021['R']:.10f}, |R/phi-1| = {mismatch_021*100:.6f}%")
print(f"    R(0.2117)= {r_02117['R']:.10f}, |R/phi-1| = {abs(r_02117['R']/phi_paasch-1)*100:.6f}%")
print(f"    R(0.22) = {r_022['R']:.10f}, |R/phi-1| = {abs(r_022['R']/phi_paasch-1)*100:.6f}%")
if crossings:
    print(f"    Refined crossing: tau = {tau_cross:.10f}")
    print(f"    S49 prediction:   tau = 0.2116857600")
    print(f"    Agreement:        delta_tau = {abs(tau_cross - 0.211686)*1000:.4f} x 10^-3")


# =============================================================================
#  STRUCTURAL ANALYSIS: What drives R(tau)?
# =============================================================================

print("\n" + "-" * 78)
print("STRUCTURAL ANALYSIS: Decomposition of R variation")
print("-" * 78)

# J_12/J_23 constancy check at new points
for r in results_new:
    ratio = r['J_12'] / r['J_23']
    print(f"  tau={r['tau']:.4f}: J_12/J_23 = {ratio:.8f}")

# DOS ratios
print(f"\n  DOS ratios at new tau values:")
for r in results_new:
    print(f"  tau={r['tau']:.4f}: rho_B1/rho_B2={r['rho'][0]/r['rho'][1]:.6f}, "
          f"rho_B3/rho_B2={r['rho'][2]/r['rho'][1]:.6f}, "
          f"rho_B1/rho_B3={r['rho'][0]/r['rho'][2]:.6f}")


# =============================================================================
#  dR/dtau AT CROSSING: Is the crossing robust?
# =============================================================================

print("\n" + "-" * 78)
print("ROBUSTNESS: dR/dtau at crossing region")
print("-" * 78)

dR_dtau = cs_R_direct(tau_dense, 1)
if crossings:
    slope_at_cross = float(cs_R_direct(tau_cross, 1))
    print(f"  dR/dtau at crossing (tau={tau_cross:.6f}) = {slope_at_cross:.6f}")
    # Sensitivity: what change in tau shifts R by 0.1%?
    delta_tau_01pct = 0.001 * phi_paasch / abs(slope_at_cross)
    print(f"  To shift R by 0.1% of phi: delta_tau = {delta_tau_01pct:.6f}")
    print(f"  The crossing is {'sharp' if abs(slope_at_cross) > 0.1 else 'gradual'} "
          f"(slope magnitude {abs(slope_at_cross):.4f})")


# =============================================================================
#  SAVE DATA
# =============================================================================

save_dict = {
    'gate_name': 'LEGGETT-PHI-CONFIRM-50',
    'gate_verdict': verdict,
    'gate_detail': detail,
    'phi_paasch': phi_paasch,

    # Primary gate result
    'R_021': r_021['R'],
    'mismatch_021': mismatch_021,

    # New tau points
    'tau_new': np.array(tau_new),
    'R_new': np.array([r['R'] for r in results_new]),
    'omega_L1_new': np.array([r['omega_L1'] for r in results_new]),
    'omega_L2_new': np.array([r['omega_L2'] for r in results_new]),
    'rho_B1_new': np.array([r['rho'][0] for r in results_new]),
    'rho_B2_new': np.array([r['rho'][1] for r in results_new]),
    'rho_B3_new': np.array([r['rho'][2] for r in results_new]),
    'J_12_new': np.array([r['J_12'] for r in results_new]),
    'J_23_new': np.array([r['J_23'] for r in results_new]),
    'Delta_B1_new': np.array([r['Delta'][0] for r in results_new]),
    'Delta_B2_new': np.array([r['Delta'][1] for r in results_new]),
    'Delta_B3_new': np.array([r['Delta'][2] for r in results_new]),

    # Dense scan
    'tau_dense': tau_dense,
    'R_dense': R_dense,

    # Full range
    'tau_full': tau_full,
    'R_full': R_full,

    # Crossing
    'has_crossing': bool(crossings),
    'tau_crossing_direct': np.array(crossings) if crossings else np.array([]),
    'tau_crossing_s49_spline': 0.211686,

    # Validation
    'validation_pass': validation_pass,
    'max_rel_err_L1': max_rel_err_L1,
    'max_rel_err_L2': max_rel_err_L2,
}

outpath = os.path.join(SCRIPT_DIR, 's50_leggett_phi_confirm.npz')
np.savez(outpath, **save_dict)
print(f"\nSaved: {outpath}")


# =============================================================================
#  PLOT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel 1: R(tau) full range with phi_paasch and new data
ax = axes[0, 0]
ax.plot(tau_full, R_full, 'b-', linewidth=2, label='$R(\\tau)$ direct computation')
ax.axhline(y=phi_paasch, color='red', linestyle='--', linewidth=2,
           label=f'$\\phi_{{\\mathrm{{Paasch}}}}$ = {phi_paasch:.4f}')
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5,
           label=f'$\\tau_{{\\rm fold}}$ = {tau_fold}')
# S48 coarse data
R_s48 = oL2_s48 / oL1_s48
ax.plot(tau_s48, R_s48, 'ko', markersize=5, label='S48 data', zorder=3)
# New data
tau_new_arr = np.array(tau_new)
R_new_arr = np.array([r['R'] for r in results_new])
ax.plot(tau_new_arr, R_new_arr, 'r^', markersize=8, label='S50 direct', zorder=4)
if crossings:
    ax.plot(tau_cross, phi_paasch, 'r*', markersize=15, zorder=5)
    ax.annotate(f'$\\tau$ = {tau_cross:.4f}', (tau_cross, phi_paasch),
                xytext=(tau_cross+0.02, phi_paasch+0.01), fontsize=10)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$R = \\omega_{L2}/\\omega_{L1}$')
ax.set_title('Leggett frequency ratio: full range')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Zoom near crossing
ax = axes[0, 1]
ax.plot(tau_dense, R_dense, 'b-', linewidth=2, label='Direct computation (61 pts)')
ax.axhline(y=phi_paasch, color='red', linestyle='--', linewidth=2)
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5)
ax.plot(tau_new_arr, R_new_arr, 'r^', markersize=10, zorder=4, label='Target tau')
if crossings:
    ax.plot(tau_cross, phi_paasch, 'r*', markersize=15, zorder=5,
            label=f'Crossing: $\\tau$={tau_cross:.5f}')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$R = \\omega_{L2}/\\omega_{L1}$')
ax.set_title('Zoom: crossing region')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.19, 0.25)

# Panel 3: Mismatch (log scale)
ax = axes[1, 0]
mismatch_full = np.abs(R_full / phi_paasch - 1.0)
ax.semilogy(tau_full, mismatch_full, 'b-', linewidth=2)
mismatch_new = np.abs(R_new_arr / phi_paasch - 1.0)
ax.semilogy(tau_new_arr, mismatch_new, 'r^', markersize=10, zorder=4)
ax.axhline(y=0.001, color='green', linestyle='--', label='PASS (0.1%)')
ax.axhline(y=0.01, color='orange', linestyle='--', label='INFO (1%)')
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$|R/\\phi_{\\mathrm{Paasch}} - 1|$')
ax.set_title(f'Mismatch (VERDICT: {verdict})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(1e-6, 0.2)

# Panel 4: DOS ratios driving R
ax = axes[1, 1]
rho_B1_full = np.array([leggett_at_tau(t)['rho'][0] for t in tau_dense])
rho_B2_full = np.array([leggett_at_tau(t)['rho'][1] for t in tau_dense])
rho_B3_full = np.array([leggett_at_tau(t)['rho'][2] for t in tau_dense])
ax.plot(tau_dense, rho_B1_full / rho_B2_full, 's-', markersize=3, label='$\\rho_{B1}/\\rho_{B2}$')
ax.plot(tau_dense, rho_B3_full / rho_B2_full, 'o-', markersize=3, label='$\\rho_{B3}/\\rho_{B2}$')
ax.plot(tau_dense, rho_B1_full / rho_B3_full, '^-', markersize=3, label='$\\rho_{B1}/\\rho_{B3}$')
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5)
if crossings:
    ax.axvline(x=tau_cross, color='red', linestyle=':', linewidth=1.5, label=f'Crossing $\\tau$={tau_cross:.4f}')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('DOS ratio')
ax.set_title('Sector DOS ratios (driver of R variation)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.19, 0.25)

fig.suptitle(f'LEGGETT-PHI-CONFIRM-50: Direct $R(\\tau) = \\omega_{{L2}}/\\omega_{{L1}}$ vs $\\phi_{{\\mathrm{{Paasch}}}}$\n'
             f'VERDICT: {verdict} | $|R(0.21)/\\phi - 1|$ = {mismatch_021*100:.4f}%',
             fontsize=12, fontweight='bold')
plt.tight_layout()

plotpath = os.path.join(SCRIPT_DIR, 's50_leggett_phi_confirm.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")
plt.close()

print("\n" + "=" * 78)
print(f"FINAL VERDICT: LEGGETT-PHI-CONFIRM-50 = {verdict}")
print(f"  {detail}")
print("=" * 78)
