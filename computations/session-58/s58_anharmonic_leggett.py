#!/usr/bin/env python3
"""
S58 ANHARMONIC-LEGGETT-58: Cubic and Quartic Leggett Mode Coupling
===================================================================

Gate: ANHARMONIC-LEGGETT-58
  PASS: Gamma_scat * dt_transit > 1  (harmonic breaks; modes redistribute)
  FAIL: Gamma_scat * dt_transit < 1  (harmonic safe; independent-mode result exact)

Physics:
  The Leggett modes propagate on the C2 sub-graph (50 bonds) of the 32-cell
  CG tessellation. S56 confirmed: the Leggett dispersion uses:
    omega_L^2 = omega_L0^2 + J_L * lambda_n(C2)
  where lambda_n are eigenvalues of the C2-graph Laplacian and J_L = epsilon*E_J.

  The Josephson potential on C2 bonds:
    H_J = -J_L * sum_{C2 bonds} cos(phi_i - phi_j)

  cos(phi) is EVEN => NO CUBIC. Leading anharmonicity is QUARTIC:
    H_4 = (J_L/24) * sum_{C2 bonds} (phi_ij)^4

  Normal modes of the C2 Laplacian diagonalize H_2.
  phi_ZPF = 1/sqrt(2*omega_L) in unit-mass convention (S56 Lagrangian).

  Key suppression factor: J_L ~ 0.017 M_KK (epsilon ~ 0.0025).

Created: Session 58 (2026-03-23)
Agent: quantum-acoustics-theorist
"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

import numpy as np
from canonical_constants import (
    dt_transit, tau_fold, N_cells, PI
)

print("=" * 70)
print("S58 ANHARMONIC-LEGGETT-58: Cubic & Quartic Leggett Mode Coupling")
print("=" * 70)

# ============================================================================
#  1. LOAD DATA
# ============================================================================

d54 = np.load('s54_tb_hamiltonian.npz', allow_pickle=True)
d56 = np.load('s56_leggett_fabric.npz', allow_pickle=True)
d57 = np.load('s57_leggett_partition.npz', allow_pickle=True)

tau_vals = d54['tau_values']
adj_C2 = d54['adj_C2'].astype(float)  # C2 sub-graph adjacency

epsilon_L = float(d56['epsilon_Leggett'])
E_J_tau = d56['E_J']
lap_eigs_s56 = d56['laplacian_eigs']  # C2 Laplacian eigenvalues
omega_L_S49 = d56['omega_L_S49_1']

fold_idx = int(d57['fold_idx'])
N_modes = int(d57['N_modes'])  # 31
omega_i_S49 = d57['omega_i_S49']
omega_end_S49 = d57['omega_end_S49']
n_exc_end = d57['n_exc_end_S49']
n_exc_fold = d57['n_exc_fold_S49']
dt_transit_val = float(d57['dt_transit'])

try:
    d58 = np.load('s58_epsilon_direct.npz', allow_pickle=True)
    epsilon_direct = float(d58['epsilon_direct'])
    print(f"  S58 epsilon = {epsilon_direct:.6f}")
except Exception:
    epsilon_direct = epsilon_L

# ============================================================================
#  2. C2 GRAPH LAPLACIAN (matching S56)
# ============================================================================

degree_C2 = np.sum(adj_C2, axis=1)
L_C2 = np.diag(degree_C2) - adj_C2

evals_C2, evecs_C2 = np.linalg.eigh(L_C2)
evals_C2[0] = 0.0  # enforce zero mode

# Verify against S56
assert np.allclose(np.sort(evals_C2), np.sort(lap_eigs_s56), atol=1e-10), \
    "C2 Laplacian eigenvalues don't match S56"
print(f"  C2 Laplacian eigenvalue check vs S56: PASSED")

# C2 bonds
bonds_i, bonds_j = np.where(np.triu(adj_C2) > 0)
N_bonds = len(bonds_i)

E_J_fold = E_J_tau[fold_idx]
J_L_fold = epsilon_L * E_J_fold
J_L_end = epsilon_L * E_J_tau[-1]
omega_L0 = 0.070  # S49 dipolar gap, intentionally != omega_L1 (0.138)  # (local)

lambda_n = evals_C2[1:]  # 31 nonzero Laplacian eigenvalues
U_C2 = evecs_C2[:, 1:]   # (32, 31) eigenvectors (skip zero mode)

print(f"\n--- Setup ---")
print(f"  N_bonds (C2) = {N_bonds}")
print(f"  epsilon = {epsilon_L:.6f}")
print(f"  E_J(fold) = {E_J_fold:.4f}, J_L = {J_L_fold:.6f} M_KK")
print(f"  lambda_n range: [{lambda_n.min():.4f}, {lambda_n.max():.4f}]")
print(f"  fold_idx = {fold_idx}, tau_fold = {tau_vals[fold_idx]:.4f}")
print(f"  dt_transit = {dt_transit_val:.6e} M_KK^-1")

# ============================================================================
#  3. NORMAL MODE DIFFERENCE VECTORS & CROSS-CHECK
# ============================================================================

d_nb = np.zeros((N_modes, N_bonds))
for b in range(N_bonds):
    i, j = bonds_i[b], bonds_j[b]
    d_nb[:, b] = U_C2[i, :] - U_C2[j, :]

# Cross-check: sum_b d_nb[n]^2 = lambda_n (Laplacian identity)
quad_check = np.sum(d_nb**2, axis=1)
quad_err = np.max(np.abs(quad_check - lambda_n) / lambda_n)
print(f"\n  Quadratic cross-check: max |sum d^2 - lambda|/lambda = {quad_err:.2e}")
assert quad_err < 1e-10, "FAILED"
print(f"  PASSED")

# Orthogonality: sum_b d_nb[n]*d_nb[m] = lambda_n * delta_{nm}
offdiag_max = 0.0  # (local)
for n in range(min(5, N_modes)):
    for m in range(n+1, min(n+5, N_modes)):
        c = np.sum(d_nb[n] * d_nb[m])
        offdiag_max = max(offdiag_max, abs(c))
print(f"  Off-diagonal max = {offdiag_max:.2e}")

# ============================================================================
#  4. LEGGETT FREQUENCIES
# ============================================================================

omega_fold_modes = omega_L_S49[fold_idx, 1:]  # 31 modes at fold

# Verify S56 formula
omega_formula = np.sqrt(omega_L0**2 + J_L_fold * lambda_n)
err_omega = np.max(np.abs(omega_formula - omega_fold_modes) / omega_fold_modes)
print(f"\n  Frequency formula check: max err = {err_omega:.4e}")
if err_omega > 0.01:
    print(f"  NOTE: S56 frequencies don't exactly match sqrt(wL0^2+JL*lambda)")
    print(f"  Using S56 data values directly (most consistent)")

print(f"  omega_fold: [{omega_fold_modes.min():.4f}, {omega_fold_modes.max():.4f}] M_KK")
print(f"  omega_end: [{omega_end_S49.min():.4f}, {omega_end_S49.max():.4f}] M_KK")

# ============================================================================
#  5. ZERO-POINT FLUCTUATIONS
# ============================================================================

phi_ZPF_fold = 1.0 / np.sqrt(2.0 * omega_fold_modes)
phi_ZPF_end = 1.0 / np.sqrt(2.0 * omega_end_S49)

# Total RMS phase on a C2 bond
phi2_bond_fold = np.array([
    np.sum(d_nb[:, b]**2 * phi_ZPF_fold**2 * (2*n_exc_fold + 1))
    for b in range(N_bonds)
])
phi_RMS_bond_fold = np.sqrt(np.mean(phi2_bond_fold))

phi2_bond_end = np.array([
    np.sum(d_nb[:, b]**2 * phi_ZPF_end**2 * (2*n_exc_end + 1))
    for b in range(N_bonds)
])
phi_RMS_bond_end = np.sqrt(np.mean(phi2_bond_end))

anh_param_fold = phi_RMS_bond_fold**2 / 12.0
anh_param_end = phi_RMS_bond_end**2 / 12.0

print(f"\n--- Phase fluctuations ---")
print(f"  AT FOLD: phi_RMS_bond = {phi_RMS_bond_fold:.4f} rad  "
      f"({phi_RMS_bond_fold/np.pi:.3f} pi)  phi^2/12 = {anh_param_fold:.4e}")
print(f"  AT END:  phi_RMS_bond = {phi_RMS_bond_end:.4f} rad  "
      f"({phi_RMS_bond_end/np.pi:.3f} pi)  phi^2/12 = {anh_param_end:.4e}")

if phi_RMS_bond_end > np.pi:
    print(f"  WARNING: phi_RMS > pi at end — Taylor invalid there")
    print(f"  Using FOLD values for scattering rate (self-consistent)")

# ============================================================================
#  6. STRUCTURAL TENSORS S3, S4
# ============================================================================

print(f"\n--- Structural tensors ---")

# S4[n,m,p,q] = sum_b d[n,b]*d[m,b]*d[p,b]*d[q,b]
S4 = np.einsum('nb,mb,pb,qb->nmpq', d_nb, d_nb, d_nb, d_nb)

# Cross-checks
for n_t in [0, 15, 30]:
    direct = np.sum(d_nb[n_t]**4)
    assert abs(S4[n_t,n_t,n_t,n_t] - direct) < 1e-12 * max(abs(direct), 1e-30)
print(f"  S4 self-check: PASSED")

# S3[n,m,p] = sum_b d[n,b]*d[m,b]*d[p,b]
S3 = np.einsum('nb,mb,pb->nmp', d_nb, d_nb, d_nb)

print(f"  S4 shape: {S4.shape}, max |S4| = {np.max(np.abs(S4)):.4f}")
print(f"  S3 shape: {S3.shape}, max |S3| = {np.max(np.abs(S3)):.4f}")

# ============================================================================
#  7. QUARTIC VERTEX V4 (at fold)
# ============================================================================
# V4[n,m,p,q] = (J_L/384) * S4[n,m,p,q] / sqrt(omega_n*omega_m*omega_p*omega_q)

print(f"\n--- Quartic vertex ---")
print(f"  J_L / 384 = {J_L_fold/384:.6e}")

omega_n4 = omega_fold_modes[:, None, None, None]
omega_m4 = omega_fold_modes[None, :, None, None]
omega_p4 = omega_fold_modes[None, None, :, None]
omega_q4 = omega_fold_modes[None, None, None, :]
omega_prod_fold = np.sqrt(omega_n4 * omega_m4 * omega_p4 * omega_q4)

V4_fold_arr = (J_L_fold / 384.0) * S4 / omega_prod_fold

V4_self_fold = np.array([V4_fold_arr[n,n,n,n] for n in range(N_modes)])

print(f"  V4[0,0,0,0] = {V4_fold_arr[0,0,0,0]:.6e} M_KK")
print(f"  V4[15,15,15,15] = {V4_fold_arr[15,15,15,15]:.6e} M_KK")
print(f"  V4[30,30,30,30] = {V4_fold_arr[30,30,30,30]:.6e} M_KK")
print(f"  max |V4| = {np.max(np.abs(V4_fold_arr)):.6e} M_KK")

# At end of transit
omega_en4 = omega_end_S49[:, None, None, None]
omega_em4 = omega_end_S49[None, :, None, None]
omega_ep4 = omega_end_S49[None, None, :, None]
omega_eq4 = omega_end_S49[None, None, None, :]
omega_prod_end = np.sqrt(omega_en4 * omega_em4 * omega_ep4 * omega_eq4)

V4_end_arr = (J_L_end / 384.0) * S4 / omega_prod_end
V4_self_end = np.array([V4_end_arr[n,n,n,n] for n in range(N_modes)])

print(f"\n  At end: J_L_end = {J_L_end:.6f} M_KK")
print(f"  V4[0,0,0,0] = {V4_end_arr[0,0,0,0]:.6e} M_KK")
print(f"  max |V4| = {np.max(np.abs(V4_end_arr)):.6e} M_KK")

# ============================================================================
#  8. CUBIC VERTEX (identically zero + upper bound)
# ============================================================================

print(f"\n--- Cubic vertex ---")
print(f"  V_3 = 0 identically (cos even, no frustration)")

# Upper bound from fluctuation-induced parity breaking
sin_delta = np.sin(phi_RMS_bond_fold)
omega_prod3 = np.sqrt(8.0 *
    omega_fold_modes[:, None, None] *
    omega_fold_modes[None, :, None] *
    omega_fold_modes[None, None, :])

V3_eff = np.abs(J_L_fold * sin_delta / 6.0) * np.abs(S3) / omega_prod3
V3_max = np.max(V3_eff)
print(f"  J_L*sin(phi_RMS)/6 = {J_L_fold*abs(sin_delta)/6:.6e}")
print(f"  max |V3_eff| = {V3_max:.6e} M_KK")

# ============================================================================
#  9. SCATTERING RATES AT FOLD
# ============================================================================

print(f"\n--- Scattering rates at fold ---")

mode_sp = np.mean(np.diff(omega_fold_modes))
print(f"  Mode spacing = {mode_sp:.4f} M_KK")
print(f"  n_exc_fold range: [{n_exc_fold.min():.4e}, {n_exc_fold.max():.4e}]")

V4_0 = V4_fold_arr[0]  # (31,31,31)

# Bare sum
sum_V4_sq_bare = np.sum(V4_0**2)

# Occupation-weighted
F_occ = np.einsum('m,p,q->mpq', 1+n_exc_fold, 1+n_exc_fold, 1+n_exc_fold)
sum_V4_sq_occ = np.sum(V4_0**2 * F_occ)

# FGR upper bound (no energy conservation)
Gamma_4_ub = 2 * np.pi * sum_V4_sq_occ / mode_sp

# Self-energy estimate
Gamma_4_selfE = np.pi * sum_V4_sq_occ / omega_fold_modes[0]**2

# Resonant channels
n_resonant = 0
sum_V4_res = 0.0  # (local)
for m in range(N_modes):
    for p in range(N_modes):
        for q in range(N_modes):
            dE = abs(omega_fold_modes[0] + omega_fold_modes[m]
                     - omega_fold_modes[p] - omega_fold_modes[q])
            if dE < mode_sp:
                n_resonant += 1
                sum_V4_res += V4_0[m,p,q]**2 * F_occ[m,p,q]

Gamma_4_res = 2 * np.pi * sum_V4_res / mode_sp

print(f"  sum |V4(0,m,p,q)|^2 = {sum_V4_sq_bare:.6e}")
print(f"  sum |V4|^2 * F_occ = {sum_V4_sq_occ:.6e}")
print(f"  Occ enhancement = {sum_V4_sq_occ/(sum_V4_sq_bare+1e-30):.3f}x")
print(f"  Gamma_4 (FGR upper)  = {Gamma_4_ub:.6e} M_KK")
print(f"  Gamma_4 (self-energy) = {Gamma_4_selfE:.6e} M_KK")
print(f"  Resonant channels: {n_resonant}/{N_modes**3}")
print(f"  Gamma_4 (resonant) = {Gamma_4_res:.6e} M_KK")

Gamma_4 = max(Gamma_4_ub, Gamma_4_selfE, Gamma_4_res)
print(f"  Gamma_4 (max) = {Gamma_4:.6e} M_KK")

# 3-phonon
V3_0 = V3_eff[0]
F_occ_2 = np.einsum('m,p->mp', 1+n_exc_fold, 1+n_exc_fold)
sum_V3_sq = np.sum(V3_0**2 * F_occ_2)
Gamma_3 = 2 * np.pi * sum_V3_sq / mode_sp
print(f"  Gamma_3_eff (ub) = {Gamma_3:.6e} M_KK")

Gamma_total = Gamma_4 + Gamma_3

# End-of-transit rates
V4_0_end = V4_end_arr[0]
F_occ_end = np.einsum('m,p,q->mpq', 1+n_exc_end, 1+n_exc_end, 1+n_exc_end)
sum_V4_end = np.sum(V4_0_end**2 * F_occ_end)
mode_sp_end = np.mean(np.diff(omega_end_S49))
Gamma_4_end = max(
    2*np.pi*sum_V4_end/mode_sp_end,
    np.pi*sum_V4_end/omega_end_S49[0]**2
)
print(f"\n  At end: Gamma_4 = {Gamma_4_end:.6e} M_KK (post-scission upper bound)")

# ============================================================================
#  10. GATE EVALUATION
# ============================================================================

print(f"\n{'='*70}")
print(f"GATE: ANHARMONIC-LEGGETT-58")
print(f"{'='*70}")

ratio_4 = Gamma_4 * dt_transit_val
ratio_3 = Gamma_3 * dt_transit_val
ratio_total = Gamma_total * dt_transit_val
ratio_4_end = Gamma_4_end * dt_transit_val

print(f"\n  Gamma_4 * dt = {ratio_4:.6e}")
print(f"  Gamma_3 * dt = {ratio_3:.6e}")
print(f"  Gamma_total * dt = {ratio_total:.6e}")
print(f"  End: Gamma_4 * dt = {ratio_4_end:.6e}")
print(f"  Transit rate = {1/dt_transit_val:.2f} M_KK")

if ratio_total < 1.0:
    gate_verdict = "FAIL"
    safety_factor = 1.0 / max(ratio_total, 1e-30)
    print(f"\n  VERDICT: FAIL — harmonic SAFE by {safety_factor:.1e}x")
else:
    gate_verdict = "PASS"
    safety_factor = ratio_total
    print(f"\n  VERDICT: PASS — modes redistribute")

# ============================================================================
#  11. ANHARMONIC FREQUENCY SHIFTS
# ============================================================================

print(f"\n--- Frequency shifts ---")

delta_omega = np.zeros(N_modes)
for n in range(N_modes):
    shift = 3.0 * V4_fold_arr[n,n,n,n] * (2*n_exc_fold[n] + 1)
    for m in range(N_modes):
        if m != n:
            shift += 2.0 * V4_fold_arr[n,n,m,m] * (2*n_exc_fold[m] + 1)
    delta_omega[n] = shift / omega_fold_modes[n]

frac_shift = delta_omega / omega_fold_modes

print(f"  delta_omega[0] = {delta_omega[0]:.6e}  ({frac_shift[0]*100:.3f}%)")
print(f"  delta_omega[15] = {delta_omega[15]:.6e}  ({frac_shift[15]*100:.3f}%)")
print(f"  delta_omega[30] = {delta_omega[30]:.6e}  ({frac_shift[30]*100:.3f}%)")
print(f"  max |shift/omega| = {np.max(np.abs(frac_shift))*100:.3f}%")
print(f"  mean |shift/omega| = {np.mean(np.abs(frac_shift))*100:.3f}%")

# ============================================================================
#  12. ENERGY CROSS-CHECKS
# ============================================================================

print(f"\n--- Energy cross-checks ---")

E_harm_modes = np.sum(omega_fold_modes * (n_exc_fold + 0.5))
E_harm_bonds = (J_L_fold/2.0) * np.sum(phi2_bond_fold)
E_gap = (omega_L0**2/2.0) * np.sum(phi_ZPF_fold**2 * (2*n_exc_fold+1))
E_harm_total = E_gap + E_harm_bonds
E_quart = (J_L_fold/24.0) * np.sum(3.0 * phi2_bond_fold**2)

print(f"  E_harm (modes) = {E_harm_modes:.4f}")
print(f"  E_harm (bonds) = {E_harm_bonds:.6f}")
print(f"  E_gap = {E_gap:.6f}")
print(f"  E_harm_total = {E_harm_total:.4f}")
print(f"  E_quartic = {E_quart:.6e}")
print(f"  E_quart/E_harm_total = {E_quart/E_harm_total:.4e}")
print(f"  E_quart/E_harm_bonds = {E_quart/E_harm_bonds:.4f}")

# ============================================================================
#  13. TOP SCATTERING CHANNELS
# ============================================================================

print(f"\n--- Top 10 quartic vertices (mode 0) ---")
V4_0_flat = V4_0.ravel()
idx_sorted = np.argsort(np.abs(V4_0_flat))[::-1]
for rank in range(10):
    idx = idx_sorted[rank]
    m = idx // (N_modes * N_modes)
    p = (idx % (N_modes * N_modes)) // N_modes
    q = idx % N_modes
    v = V4_0[m, p, q]
    dE = omega_fold_modes[0]+omega_fold_modes[m]-omega_fold_modes[p]-omega_fold_modes[q]
    print(f"  V4(0,{m:2d},{p:2d},{q:2d}) = {v:+.4e}  dE={dE:+.4f}")

# ============================================================================
#  14. MODE-RESOLVED RATES
# ============================================================================

print(f"\n--- Mode-resolved Gamma_4 ---")
Gamma_4_per_mode = np.zeros(N_modes)
for n in range(N_modes):
    V4_n = V4_fold_arr[n]
    s = np.sum(V4_n**2 * F_occ)
    Gamma_4_per_mode[n] = 2 * np.pi * s / mode_sp

for n_show in [0, 5, 10, 15, 20, 25, 30]:
    r = Gamma_4_per_mode[n_show] * dt_transit_val
    print(f"  mode {n_show:2d}: Gamma={Gamma_4_per_mode[n_show]:.4e}  *dt={r:.4e}")
print(f"  max: mode {np.argmax(Gamma_4_per_mode)}, "
      f"*dt={np.max(Gamma_4_per_mode)*dt_transit_val:.4e}")

# ============================================================================
#  15. SUMMARY
# ============================================================================

print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"")
print(f"  Cubic: ZERO (exact, cos even, no frustration)")
print(f"    Fluctuation bound: Gamma_3*dt = {ratio_3:.2e}")
print(f"")
print(f"  Quartic (J_L = {J_L_fold:.4e} M_KK):")
print(f"    V4[0,0,0,0] = {V4_fold_arr[0,0,0,0]:.4e}")
print(f"    max |V4| = {np.max(np.abs(V4_fold_arr)):.4e}")
print(f"    Gamma_4 = {Gamma_4:.4e}  *dt = {ratio_4:.4e}")
print(f"")
print(f"  Freq shifts: max {np.max(np.abs(frac_shift))*100:.2f}%, "
      f"mean {np.mean(np.abs(frac_shift))*100:.2f}%")
print(f"")
print(f"  Energy: E_quart/E_harm = {E_quart/E_harm_total:.4e}")
print(f"  phi_RMS(fold) = {phi_RMS_bond_fold:.3f} rad, "
      f"phi_RMS(end) = {phi_RMS_bond_end:.3f} rad")
print(f"")
print(f"  GATE: {gate_verdict}")
print(f"  Gamma_total * dt = {ratio_total:.4e}")
if gate_verdict == "FAIL":
    print(f"  Safety: {safety_factor:.1e}x")

# ============================================================================
#  16. SAVE
# ============================================================================

np.savez('s58_anharmonic_leggett.npz',
    gate_name=np.array(['ANHARMONIC-LEGGETT-58']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([
        f"Gamma_total*dt={ratio_total:.2e}. "
        f"V3=0 exact. J_L={J_L_fold:.4e}. "
        f"V4_max={np.max(np.abs(V4_fold_arr)):.2e}. "
        f"Shift max {np.max(np.abs(frac_shift))*100:.1f}%. "
        f"phi_RMS(fold)={phi_RMS_bond_fold:.2f}. "
        f"Safe by {safety_factor:.0e}x."
    ]),

    epsilon=epsilon_L,
    E_J_fold=E_J_fold,
    J_L_fold=J_L_fold,
    J_L_end=J_L_end,
    dt_transit=dt_transit_val,
    N_bonds_C2=N_bonds,
    omega_L0=omega_L0,

    Gamma_4_fold=Gamma_4,
    Gamma_3_ub_fold=Gamma_3,
    Gamma_total_fold=Gamma_total,
    Gamma_4_end=Gamma_4_end,
    ratio_4=ratio_4,
    ratio_3=ratio_3,
    ratio_total=ratio_total,
    ratio_4_end=ratio_4_end,
    safety_factor=safety_factor,

    phi_RMS_bond_fold=phi_RMS_bond_fold,
    phi_RMS_bond_end=phi_RMS_bond_end,
    anh_param_fold=anh_param_fold,
    anh_param_end=anh_param_end,

    E_quartic_fold=E_quart,
    E_harmonic_total_fold=E_harm_total,
    E_quartic_frac=E_quart/E_harm_total,

    omega_fold=omega_fold_modes,
    omega_end=omega_end_S49,
    n_exc_fold=n_exc_fold,
    n_exc_end=n_exc_end,
    V4_self_fold=V4_self_fold,
    V4_self_end=V4_self_end,
    delta_omega=delta_omega,
    frac_shift=frac_shift,
    Gamma_4_per_mode=Gamma_4_per_mode,
    lambda_n=lambda_n,

    V4_0_top100=np.sort(np.abs(V4_0.ravel()))[::-1][:100],
    S4_diagonal=np.array([S4[n,n,n,n] for n in range(N_modes)]),
    S3_diagonal=np.array([S3[n,n,n] for n in range(N_modes)]),
    quad_check_err=quad_err,
    N_resonant_fold=n_resonant,
)

print(f"\n  Saved: s58_anharmonic_leggett.npz")
print(f"\nDone.")
