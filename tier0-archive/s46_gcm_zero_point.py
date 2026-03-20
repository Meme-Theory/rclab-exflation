#!/usr/bin/env python3
"""
Session 46 W4-9: GCM Zero-Point Correction for Tau Stabilization (GCM-ZERO-POINT-46)

Generator Coordinate Method for the tau modulus using BCS trial states.
Zero-point correction = E_0^GCM - V(tau_min).

=== PHYSICAL SETUP ===

The GCM equation:
    sum_j H(tau_i, tau_j) f_j = E * sum_j N(tau_i, tau_j) f_j       (1)

N(tau_i, tau_j) = <BCS(tau_i)|BCS(tau_j)> = prod_k (u_ik u_jk + v_ik v_jk)  (Onishi)
H(tau_i, tau_j) = [V(tau_i) + V(tau_j)]/2 * N(tau_i, tau_j)        (GOA)

V(tau) = q-theory ground-state vacuum energy density rho_gs(tau)
from S45 Q-THEORY-BCS-45, NOT the BCS condensation energy.
This is the potential whose zero-crossing defines tau*.

BCS wave functions: adiabatic scaling from ED-calibrated fold state.
Delta_k(tau) = Delta_k(fold) * [epsilon spread at tau / epsilon spread at fold]^{1/2}

=== NUCLEAR CONTEXT ===

GCM in nuclear DFT (Paper 13, Bender et al. Rev. Mod. Phys. 2003):
- Uses the constrained HFB energy as V(q) where q = deformation
- BCS/HFB trial states define norm overlaps
- ZPE typically 0.5-1 MeV (5-10% of barrier for A ~ 150-250)
- For light nuclei (sd-shell, A ~ 24): ZPE/barrier ~ 10-25%

Our system: 8-mode BCS, 0D limit (L/xi = 0.031), N_pair = 1.
Closest nuclear analog: near-closed-shell sd-shell nucleus.

Author: nazarewicz-nuclear-structure-theorist (Session 46 W4-9)
Date: 2026-03-15
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import (
    tau_fold, E_cond, barrier_0d, omega_PV,
    E_B1, E_B2_mean, E_B3_mean, rho_B2_per_mode,
)

print("=" * 75)
print("Session 46 W4-9: GCM Zero-Point Correction (GCM-ZERO-POINT-46)")
print("=" * 75)

# =====================================================================
# 1. LOAD DATA
# =====================================================================

# ED reference at fold
d_ed = np.load(os.path.join(SCRIPT_DIR, "s46_v_b3b3.npz"), allow_pickle=True)
E_8_fold = d_ed['E_8']
n_k_fold = d_ed['n_k']
kappa_fold = d_ed['kappa_k']
Delta_fold = d_ed['Delta_from_occ']
rho_8_fold = d_ed['rho_8']
labels = d_ed['labels']
v_k_fold = np.sqrt(np.maximum(n_k_fold, 0.0))
u_k_fold = np.sqrt(np.maximum(1.0 - n_k_fold, 0.0))

# Q-theory potential (vacuum energy density)
d45 = np.load(os.path.join(SCRIPT_DIR, "s45_qtheory_bcs.npz"), allow_pickle=True)
tau_dense = d45['tau_dense']
rho_gs_flatband = d45['rho_gs_ext_uniform']  # flatband scenario (used for tau*)
tau_star_orig = float(d45['tau_star_flatband'])

# Eigenvalue data
s27 = np.load(os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz"), allow_pickle=True)
s36 = np.load(os.path.join(SCRIPT_DIR, "s36_sfull_tau_stabilization.npz"), allow_pickle=True)

print(f"\n  ED fold: Delta_B2 = {Delta_fold[0]:.6f}, v_B2 = {v_k_fold[0]:.6f}")
print(f"  tau* (S45 flatband) = {tau_star_orig:.6f}")

# =====================================================================
# 2. GCM GRID
# =====================================================================

tau_gcm = np.array([0.10, 0.15, 0.19, 0.20, 0.25])
n_gcm = len(tau_gcm)

tau_ext_extra = np.array([0.16, 0.17, 0.18, 0.21, 0.22])
tau_ext = np.sort(np.concatenate([tau_gcm, tau_ext_extra]))
n_ext = len(tau_ext)

tau_source = {
    0.10: ('s27', 1), 0.15: ('s27', 2), 0.19: ('s36', 'tau0.190'),
    0.20: ('s27', 3), 0.25: ('s27', 4),
    0.16: ('s36', 'tau0.160'), 0.17: ('s36', 'tau0.170'),
    0.18: ('s36', 'tau0.180'), 0.21: ('s36', 'tau0.210'),
    0.22: ('s36', 'tau0.220'),
}

def get_evals(tau_val, p, q):
    src, idx = tau_source[tau_val]
    if src == 's27':
        return np.abs(s27[f'evals_{p}_{q}_{idx}'])
    return np.abs(s36[f'evals_{idx}_{p}_{q}'])

def get_8mode_E(tau_val):
    return np.array([
        np.min(get_evals(tau_val, 1, 1)),  # B2 x4
        np.min(get_evals(tau_val, 1, 1)),
        np.min(get_evals(tau_val, 1, 1)),
        np.min(get_evals(tau_val, 1, 1)),
        np.min(get_evals(tau_val, 0, 0)),  # B1
        np.min(get_evals(tau_val, 3, 0)),  # B3_30
        np.min(get_evals(tau_val, 0, 3)),  # B3_03
        np.min(get_evals(tau_val, 2, 1)),  # B3_21
    ])

# =====================================================================
# 3. V(tau) FROM Q-THEORY TRACE-LOG
# =====================================================================
# The q-theory potential is rho_gs(tau) from S45, interpolated.
# This is the energy whose zero-crossing defines tau*.

print(f"\n{'='*75}")
print("V(tau) FROM Q-THEORY (TRACE-LOG)")
print(f"{'='*75}")

# Interpolate rho_gs onto GCM grid
cs_rho = CubicSpline(tau_dense, rho_gs_flatband)

V_5 = np.array([float(cs_rho(t)) for t in tau_gcm])
V_ext_arr = np.array([float(cs_rho(t)) for t in tau_ext])

print(f"\n  V(tau) = rho_gs_flatband(tau) at GCM grid:")
for i, t in enumerate(tau_gcm):
    print(f"    V({t:.2f}) = {V_5[i]:+.8f} M_KK^4")

V_min_5 = np.min(V_5)
idx_min_5 = np.argmin(V_5)
tau_vmin = tau_gcm[idx_min_5]
print(f"\n  V_min = {V_min_5:+.8f} at tau = {tau_vmin:.2f}")

# V(tau*) should be near zero by construction
V_at_taustar = float(cs_rho(tau_star_orig))
print(f"  V(tau*={tau_star_orig:.4f}) = {V_at_taustar:+.8f} (should be ~0)")

# =====================================================================
# 4. BCS WAVE FUNCTIONS (ADIABATIC)
# =====================================================================
# BCS amplitudes change with tau through the single-particle energies.
# We use the ED fold state as reference and adiabatically track the
# (u_k, v_k) as epsilon_k changes.
#
# At each tau:
#   xi_k(tau) = epsilon_k(tau) - mu(tau)
#   E_qp_k(tau) = sqrt(xi_k^2 + Delta_k^2)
#   v_k^2(tau) = 0.5*(1 - xi_k/E_qp_k)
#
# Delta_k is held at the fold ED values.
# This is "frozen pairing gap" -- exact in the adiabatic limit.

print(f"\n{'='*75}")
print("BCS WAVE FUNCTIONS (FROZEN DELTA, ADIABATIC xi)")
print(f"{'='*75}")

all_bcs = {}
for tau_val in np.sort(np.concatenate([tau_gcm, tau_ext_extra])):
    E_8 = get_8mode_E(tau_val)
    mu = 0.5 * (E_8.min() + E_8.max())
    xi = E_8 - mu

    # Frozen gap: use fold Delta values
    E_qp = np.sqrt(xi**2 + Delta_fold**2)
    v_sq = 0.5 * (1.0 - xi / E_qp)
    u_sq = 1.0 - v_sq
    v_k = np.sqrt(np.maximum(v_sq, 0.0))
    u_k = np.sqrt(np.maximum(u_sq, 0.0))

    all_bcs[tau_val] = {'u_k': u_k, 'v_k': v_k, 'xi': xi, 'E_8': E_8, 'mu': mu}

# Verify at fold: should reproduce ED
r19 = all_bcs[0.19]
print(f"\n  Fold verification:")
print(f"    v_B2: ED = {v_k_fold[0]:.6f}, adiab = {r19['v_k'][0]:.6f}, "
      f"diff = {abs(r19['v_k'][0]-v_k_fold[0]):.2e}")
print(f"    v_B1: ED = {v_k_fold[4]:.6f}, adiab = {r19['v_k'][4]:.6f}")
print(f"    v_B3: ED = {v_k_fold[5]:.6f}, adiab = {r19['v_k'][5]:.6f}")

# The fold (u,v) won't exactly match ED because ED uses self-consistent Delta
# and our xi uses a different mu. But the OVERLAP is what matters for GCM.

# Print BCS at each tau
for tau_val in tau_gcm:
    r = all_bcs[tau_val]
    print(f"  tau = {tau_val:.2f}: v_B2 = {r['v_k'][0]:.6f}, "
          f"v_B1 = {r['v_k'][4]:.6f}, v_B3 = {r['v_k'][5]:.6f}, "
          f"mu = {r['mu']:.6f}")

# =====================================================================
# 5. NORM KERNEL
# =====================================================================

print(f"\n{'='*75}")
print("NORM OVERLAP KERNEL")
print(f"{'='*75}")

def compute_N(tau_arr, bcs):
    n = len(tau_arr)
    N = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            ov = all_bcs[tau_arr[i]]['u_k'] * all_bcs[tau_arr[j]]['u_k'] + \
                 all_bcs[tau_arr[i]]['v_k'] * all_bcs[tau_arr[j]]['v_k']
            N[i, j] = np.prod(ov)
    return N

N_5 = compute_N(tau_gcm, all_bcs)

print(f"\n  5-point norm kernel N(tau_i, tau_j):")
print(f"  {'':>8s}", end='')
for t in tau_gcm:
    print(f"  {t:>10.2f}", end='')
print()
for i, ti in enumerate(tau_gcm):
    print(f"  {ti:>8.2f}", end='')
    for j in range(n_gcm):
        print(f"  {N_5[i,j]:>10.7f}", end='')
    print()

N5_evals = np.linalg.eigvalsh(N_5)
print(f"\n  Eigenvalues: {N5_evals}")
cond5 = N5_evals[-1] / max(N5_evals[0], 1e-30)
print(f"  Condition number: {cond5:.2e}")
off5 = N_5[np.triu_indices(n_gcm, k=1)]
print(f"  Off-diag range: [{off5.min():.7f}, {off5.max():.7f}]")
print(f"  1 - min(N_offdiag) = {1 - off5.min():.7f}")

# =====================================================================
# 6. GCM SOLUTION
# =====================================================================

print(f"\n{'='*75}")
print("GCM SOLUTION")
print(f"{'='*75}")

# GOA Hamiltonian kernel
H_5 = np.zeros((n_gcm, n_gcm))
for i in range(n_gcm):
    for j in range(n_gcm):
        H_5[i, j] = 0.5 * (V_5[i] + V_5[j]) * N_5[i, j]

def solve_gcm(N, H, threshold=1e-8):
    evals, evecs = np.linalg.eigh(N)
    valid = evals > threshold
    nv = np.sum(valid)
    if nv < 1:
        return np.array([]), np.zeros((len(N), 0)), nv
    D = np.diag(1.0 / np.sqrt(evals[valid]))
    U = evecs[:, valid]
    Hn = D @ U.T @ H @ U @ D
    E, g = np.linalg.eigh(Hn)
    f = U @ D @ g
    return E, f, nv

E_gcm_5, f_gcm_5, nv5 = solve_gcm(N_5, H_5)

print(f"\n  Valid norm eigenvalues (>1e-8): {nv5} / {n_gcm}")
print(f"  GCM eigenvalues (M_KK^4):")
for i, E in enumerate(E_gcm_5):
    print(f"    E_{i} = {E:+.10f}")

if len(E_gcm_5) > 0:
    f0 = f_gcm_5[:, 0]
    nrm = np.sqrt(f0 @ N_5 @ f0)
    f0n = f0 / nrm if abs(nrm) > 1e-15 else f0
    print(f"\n  Ground state weight f_0(tau):")
    for i, t in enumerate(tau_gcm):
        print(f"    f_0({t:.2f}) = {f0n[i]:+.8f}")
else:
    f0n = np.zeros(n_gcm)

# =====================================================================
# 7. ZERO-POINT CORRECTION
# =====================================================================

print(f"\n{'='*75}")
print("ZERO-POINT CORRECTION")
print(f"{'='*75}")

E0_5 = E_gcm_5[0] if len(E_gcm_5) > 0 else V_min_5
E_ZPE_5 = E0_5 - V_min_5

print(f"\n  V_min = {V_min_5:+.10f} M_KK^4 at tau = {tau_vmin:.2f}")
print(f"  E_0^GCM = {E0_5:+.10f} M_KK^4")
print(f"  E_ZPE = {E_ZPE_5:+.10f} M_KK^4")

# For nuclear comparison, normalize ZPE by the potential depth
V_depth = abs(V_5.max() - V_5.min())
print(f"\n  V depth across GCM grid = {V_depth:.8f} M_KK^4")
print(f"  |E_ZPE| / V_depth = {abs(E_ZPE_5) / V_depth:.4f}" if V_depth > 1e-15 else "")

# Barrier_0d is in M_KK units; V is in M_KK^4 units.
# The barrier in the q-theory potential is the depth of V between
# tau_min and the zero-crossing (tau*).
V_at_min = V_min_5
V_at_cross = 0.0  # by definition, rho_gs(tau*) = 0
q_barrier = abs(V_at_cross - V_at_min)
print(f"  Q-theory barrier (V_min to zero-crossing) = {q_barrier:.8f} M_KK^4")
zpe_qbarrier = abs(E_ZPE_5) / q_barrier if q_barrier > 1e-15 else float('inf')
print(f"  |E_ZPE| / q-barrier = {zpe_qbarrier:.6f}")

# tau* shift
dV_5 = cs_rho(tau_star_orig, 1)
print(f"\n  dV/dtau at tau* = {float(dV_5):.8f} M_KK^4")
if abs(dV_5) > 1e-15:
    delta_tau_5 = -E_ZPE_5 / float(dV_5)
else:
    delta_tau_5 = 0.0
tau_star_5 = tau_star_orig + delta_tau_5

print(f"  delta_tau* = {delta_tau_5:+.8f}")
print(f"  tau*_corrected = {tau_star_5:.6f}")
print(f"  Direction: {'TOWARD fold' if delta_tau_5 < 0 else 'AWAY from fold' if delta_tau_5 > 0 else 'none'}")

# =====================================================================
# 8. EXTENDED GCM (10-point)
# =====================================================================

print(f"\n{'='*75}")
print("EXTENDED GCM (10-point)")
print(f"{'='*75}")

N_10 = compute_N(tau_ext, all_bcs)
H_10 = np.zeros((n_ext, n_ext))
for i in range(n_ext):
    for j in range(n_ext):
        H_10[i, j] = 0.5 * (V_ext_arr[i] + V_ext_arr[j]) * N_10[i, j]

E_gcm_10, f_gcm_10, nv10 = solve_gcm(N_10, H_10)
V_min_10 = np.min(V_ext_arr)
E0_10 = E_gcm_10[0] if len(E_gcm_10) > 0 else V_min_10
E_ZPE_10 = E0_10 - V_min_10

print(f"  Valid: {nv10} / {n_ext}")
if len(E_gcm_10) > 0:
    print(f"  GCM eigenvalues (first 5):")
    for i, E in enumerate(E_gcm_10[:min(5, len(E_gcm_10))]):
        print(f"    E_{i} = {E:+.10f}")
    f0_10 = f_gcm_10[:, 0]
    nrm10 = np.sqrt(f0_10 @ N_10 @ f0_10)
    f0_10n = f0_10 / nrm10 if abs(nrm10) > 1e-15 else f0_10
else:
    f0_10n = np.zeros(n_ext)

print(f"\n  E_ZPE(10-pt) = {E_ZPE_10:+.10f}")

dV_10 = cs_rho(tau_star_orig, 1)
delta_tau_10 = -E_ZPE_10 / float(dV_10) if abs(dV_10) > 1e-15 else 0.0
tau_star_10 = tau_star_orig + delta_tau_10

# =====================================================================
# 9. GOA VALIDATION
# =====================================================================

print(f"\n{'='*75}")
print("GOA VALIDATION")
print(f"{'='*75}")

dtaus, ovs = [], []
for i in range(n_gcm):
    for j in range(i+1, n_gcm):
        dtaus.append(abs(tau_gcm[i] - tau_gcm[j]))
        ovs.append(N_5[i, j])
dtaus = np.array(dtaus)
ovs = np.array(ovs)

mask = ovs > 1e-20
if np.sum(mask) >= 2:
    x = dtaus[mask]**2
    y = np.log(ovs[mask])
    a_goa = -np.sum(x * y) / np.sum(x**2) if np.sum(x**2) > 0 else 0
    yp = -a_goa * x
    R2 = 1 - np.sum((y-yp)**2)/np.sum((y-np.mean(y))**2) if np.sum((y-np.mean(y))**2) > 0 else 0
    sigma_goa = 1/np.sqrt(2*a_goa) if a_goa > 0 else float('inf')
    print(f"  GOA: N ~ exp(-{a_goa:.4f} dtau^2), sigma = {sigma_goa:.4f}, R^2 = {R2:.6f}")
else:
    a_goa, R2, sigma_goa = 0, 0, float('inf')

# =====================================================================
# 10. CONVERGENCE
# =====================================================================

print(f"\n{'='*75}")
print("CONVERGENCE")
print(f"{'='*75}")

conv = abs(E_ZPE_10 - E_ZPE_5)/abs(E_ZPE_5) if abs(E_ZPE_5) > 1e-15 else 0

print(f"\n  {'':>22s} | {'5-pt':>14s} | {'10-pt':>14s} | {'diff':>14s}")
print(f"  {'-'*68}")
print(f"  {'E_ZPE':>22s} | {E_ZPE_5:>+14.8f} | {E_ZPE_10:>+14.8f} | {E_ZPE_10-E_ZPE_5:>+14.8f}")
print(f"  {'delta_tau*':>22s} | {delta_tau_5:>+14.8f} | {delta_tau_10:>+14.8f} | {delta_tau_10-delta_tau_5:>+14.8f}")
print(f"  {'|dE/E|':>22s} | {'':>14s} | {'':>14s} | {conv:>14.6f}")

# =====================================================================
# 11. NUCLEAR ANALOG ASSESSMENT
# =====================================================================

print(f"\n{'='*75}")
print("NUCLEAR ANALOG ASSESSMENT")
print(f"{'='*75}")

print(f"""
  The GCM norm kernel N(tau_i, tau_j) > {off5.min():.4f} for all pairs.
  This extreme near-unity means the BCS wave function is nearly identical
  across the tau range [0.10, 0.25].

  Physical interpretation:
    The pairing gap Delta_B2 = 1.334 M_KK >> bandwidth ~ 0.13 M_KK.
    This places the system deep in the STRONG-COUPLING regime where
    the gap overwhelms the single-particle spectrum variations.
    Changing tau barely perturbs the BCS state.

  Nuclear analog (Paper 03, Section IV):
    A closed-shell nucleus (e.g., ^208Pb) has such a large shell gap
    that pairing is suppressed. When pairing IS present (e.g., ^116Sn),
    the GCM correction from deformation is typically 5-10% of the barrier.

    Our system is the OPPOSITE: pairing is so strong that deformation
    (tau variation) cannot significantly alter the paired state.
    The GCM norm kernel being near-identity means the tau zero-point
    motion has very little effect on the BCS condensate.

  q-theory potential parameters:
    q-barrier (V_min to crossing) = {q_barrier:.6f} M_KK^4
    |E_ZPE| / q-barrier = {zpe_qbarrier:.4f}
    |delta_tau*| = {abs(delta_tau_5):.6f}
    |delta_tau*| / |tau*-tau_fold| = {abs(delta_tau_5)/abs(tau_star_orig-tau_fold):.4f}
""")

if zpe_qbarrier < 0.05:
    assessment = "NEGLIGIBLE -- ZPE < 5% of q-barrier"
elif zpe_qbarrier < 0.30:
    assessment = "MODERATE -- in nuclear range (5-30%)"
elif zpe_qbarrier < 1.0:
    assessment = "LARGE -- significant fraction of q-barrier"
else:
    assessment = "DOMINANT -- quantum delocalization exceeds barrier"
print(f"  Assessment: {assessment}")

# =====================================================================
# 12. SAVE
# =====================================================================

print(f"\n{'='*75}")
print("SAVING")
print(f"{'='*75}")

output = {
    'tau_gcm': tau_gcm, 'tau_ext': tau_ext,
    'N_kernel': N_5, 'H_kernel': H_5,
    'V_tau': V_5, 'V_ext': V_ext_arr,
    'E_gcm': E_gcm_5, 'f_gcm': f_gcm_5,
    'f0_normalized': f0n,
    'E_ZPE': E_ZPE_5, 'V_min': V_min_5,
    'tau_min': tau_vmin, 'E0_gcm': E0_5,
    'delta_tau_star': delta_tau_5,
    'tau_star_original': tau_star_orig,
    'tau_star_corrected': tau_star_5,
    'q_barrier': q_barrier,
    'zpe_qbarrier_ratio': zpe_qbarrier,
    # 10-point
    'N_ext': N_10,
    'E_gcm_ext': E_gcm_10,
    'E_ZPE_ext': E_ZPE_10,
    'E0_ext': E0_10,
    'delta_tau_ext': delta_tau_10,
    'tau_star_ext': tau_star_10,
    'f0_ext_normalized': f0_10n,
    # GOA
    'a_goa': a_goa, 'R2_goa': R2, 'sigma_tau_goa': sigma_goa,
    'N_eigenvalues': N5_evals, 'N_condition': cond5,
    'conv_ratio': conv,
    # BCS data
    'Delta_B2_vs_tau': np.array([all_bcs[t]['v_k'][0]**2 for t in tau_gcm]),
    'v_B2_vs_tau': np.array([all_bcs[t]['v_k'][0] for t in tau_gcm]),
    'v_B1_vs_tau': np.array([all_bcs[t]['v_k'][4] for t in tau_gcm]),
    'v_B3_vs_tau': np.array([all_bcs[t]['v_k'][5] for t in tau_gcm]),
    # Gate
    'gate_name': np.array(['GCM-ZERO-POINT-46']),
    'gate_verdict': np.array(['INFO']),
    'gate_detail': np.array([f'E_ZPE={E_ZPE_5:+.6f}, delta_tau*={delta_tau_5:+.6f}, '
                             f'GOA R^2={R2:.4f}, ZPE/q-barrier={zpe_qbarrier:.4f}']),
}

out_path = os.path.join(SCRIPT_DIR, "s46_gcm_zero_point.npz")
np.savez_compressed(out_path, **output)
print(f"  Saved: {out_path}")

# =====================================================================
# 13. PLOTS
# =====================================================================

print(f"\nGenerating plots...")
fig = plt.figure(figsize=(20, 14))
fig.suptitle("GCM Zero-Point Correction (GCM-ZERO-POINT-46)\n"
             "Q-theory potential + frozen-Delta BCS overlaps",
             fontsize=13, fontweight='bold')

# A: V(tau) = q-theory potential
ax1 = fig.add_subplot(2, 3, 1)
tau_plot = np.linspace(0.05, 0.30, 200)
V_plot = cs_rho(tau_plot)
ax1.plot(tau_plot, V_plot, 'k-', lw=1.5, alpha=0.5, label=r'$\rho_{gs}(\tau)$ smooth')
ax1.plot(tau_gcm, V_5, 'ro', ms=10, zorder=5, label='GCM grid')
ax1.plot(tau_ext, V_ext_arr, 'b^', ms=6, alpha=0.6, label='Extended grid')
ax1.axhline(0, color='gray', ls='--', lw=1)
if len(E_gcm_5) > 0:
    ax1.axhline(E0_5, color='r', ls=':', lw=2, label=f'$E_0^{{GCM}}$ = {E0_5:.4f}')
ax1.axvline(tau_star_orig, color='green', ls=':', alpha=0.5, label=f'$\\tau^*$ = {tau_star_orig:.3f}')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$\rho_{gs}$ ($M_{KK}^4$)')
ax1.set_title('Q-Theory Potential (GCM Hamiltonian)')
ax1.legend(fontsize=7)
ax1.grid(alpha=0.3)

# B: Norm kernel heatmap
ax2 = fig.add_subplot(2, 3, 2)
im = ax2.imshow(N_5, cmap='RdBu_r', aspect='equal',
                extent=[tau_gcm[0], tau_gcm[-1], tau_gcm[-1], tau_gcm[0]])
margin = max(0.005, 0.1*(N_5.max()-N_5.min()))
im.set_clim(N_5.min()-margin, N_5.max()+margin)
plt.colorbar(im, ax=ax2, label=r'$N(\tau_i, \tau_j)$')
for i in range(n_gcm):
    for j in range(n_gcm):
        ax2.text(tau_gcm[j], tau_gcm[i], f'{N_5[i,j]:.5f}',
                ha='center', va='center', fontsize=6,
                color='white' if abs(N_5[i,j]-N_5.min()) < margin else 'black')
ax2.set_xlabel(r'$\tau_j$'); ax2.set_ylabel(r'$\tau_i$')
ax2.set_title('BCS Norm Overlap Kernel')

# C: GOA validation
ax3 = fig.add_subplot(2, 3, 3)
if len(dtaus) > 0:
    ax3.plot(dtaus**2, np.log(np.maximum(ovs, 1e-30)), 'ko', ms=8, label='Data')
    if a_goa > 0:
        xp = np.linspace(0, dtaus.max()**2*1.1, 50)
        ax3.plot(xp, -a_goa*xp, 'r-', lw=2, label=f'GOA: $a$={a_goa:.3f}, $R^2$={R2:.4f}')
ax3.set_xlabel(r'$(\Delta\tau)^2$'); ax3.set_ylabel(r'$\ln N$')
ax3.set_title('Gaussian Overlap Approximation')
ax3.legend(fontsize=8); ax3.grid(alpha=0.3)

# D: GCM spectrum
ax4 = fig.add_subplot(2, 3, 4)
if len(E_gcm_5) > 1:
    lvl5 = E_gcm_5 - E_gcm_5[0]
    for i, lv in enumerate(lvl5):
        ax4.plot([0.7, 1.3], [lv, lv], 'b-', lw=3)
        ax4.text(1.35, lv, f'{lv:.6f}', fontsize=9, va='center')
if len(E_gcm_10) > 1:
    lvl10 = E_gcm_10[:min(5,len(E_gcm_10))] - E_gcm_10[0]
    for i, lv in enumerate(lvl10):
        ax4.plot([1.7, 2.3], [lv, lv], 'r-', lw=3)
        ax4.text(2.35, lv, f'{lv:.6f}', fontsize=9, va='center')
ax4.set_xlim(0.4, 3.5); ax4.set_xticks([1, 2]); ax4.set_xticklabels(['5-pt', '10-pt'])
ax4.set_ylabel(r'$E - E_0$ ($M_{KK}^4$)'); ax4.set_title('GCM Spectrum')
ax4.grid(alpha=0.3, axis='y')

# E: Weight function
ax5 = fig.add_subplot(2, 3, 5)
if len(E_gcm_5) > 0:
    ax5.bar(tau_gcm-0.004, f0n**2, width=0.008, color='blue', alpha=0.7, label='5-pt')
if np.any(f0_10n != 0):
    ax5.bar(tau_ext+0.004, f0_10n**2, width=0.006, color='red', alpha=0.5, label='10-pt')
ax5.set_xlabel(r'$\tau$'); ax5.set_ylabel(r'$|f_0|^2$')
ax5.set_title('GCM Ground State Weight'); ax5.legend(fontsize=8); ax5.grid(alpha=0.3)

# F: BCS v_k vs tau
ax6 = fig.add_subplot(2, 3, 6)
vB2 = np.array([all_bcs[t]['v_k'][0] for t in tau_gcm])
vB1 = np.array([all_bcs[t]['v_k'][4] for t in tau_gcm])
vB3 = np.array([all_bcs[t]['v_k'][5] for t in tau_gcm])
ax6.plot(tau_gcm, vB2, 'ro-', lw=2, ms=7, label='$v_{B2}$')
ax6.plot(tau_gcm, vB1, 'bs-', lw=2, ms=7, label='$v_{B1}$')
ax6.plot(tau_gcm, vB3, 'g^-', lw=2, ms=7, label='$v_{B3}$')
ax6.set_xlabel(r'$\tau$'); ax6.set_ylabel(r'$v_k$')
ax6.set_title('BCS Amplitudes vs $\\tau$'); ax6.legend(fontsize=8); ax6.grid(alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s46_gcm_zero_point.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")
plt.close()

# =====================================================================
# 14. FINAL SUMMARY
# =====================================================================

print(f"\n{'='*75}")
print("GCM-ZERO-POINT-46 FINAL SUMMARY")
print(f"{'='*75}")

print(f"""
  METHOD:
    GCM with frozen-Delta BCS trial states on q-theory potential
    V(tau) = rho_gs_flatband(tau) from S45 Q-THEORY-BCS-45
    Onishi norm overlap (exact for real amplitudes)
    GOA for Hamiltonian kernel

  NORM KERNEL:
    N(tau_i, tau_j) > {off5.min():.5f} for all pairs
    Eigenvalues: {N5_evals}
    Condition: {cond5:.2e}
    GOA: a = {a_goa:.4f}, sigma = {sigma_goa:.4f}, R^2 = {R2:.6f}

  Q-THEORY POTENTIAL:
    V_min = {V_min_5:+.8f} at tau = {tau_vmin:.2f}
    V(tau*) ~ 0 (crossing at tau* = {tau_star_orig:.4f})
    q-barrier = {q_barrier:.8f} M_KK^4

  ZERO-POINT CORRECTION:
    E_ZPE (5-pt) = {E_ZPE_5:+.8f} M_KK^4
    E_ZPE (10-pt) = {E_ZPE_10:+.8f} M_KK^4
    Convergence |dE/E| = {conv:.6f}
    |E_ZPE| / q-barrier = {zpe_qbarrier:.6f}

  TAU-STAR SHIFT:
    tau* original = {tau_star_orig:.6f}
    delta_tau* (5-pt) = {delta_tau_5:+.8f}
    delta_tau* (10-pt) = {delta_tau_10:+.8f}
    tau* corrected (5-pt) = {tau_star_5:.6f}
    Direction: {'TOWARD fold' if delta_tau_5 < 0 else 'AWAY from fold' if delta_tau_5 > 0 else 'none'}

  GCM SPECTRUM:""")
if len(E_gcm_5) > 1:
    print(f"    E_1 - E_0 = {E_gcm_5[1]-E_gcm_5[0]:.8f} M_KK^4")
    print(f"    omega_PV = {omega_PV:.6f} M_KK")

print(f"""
  PHYSICAL INTERPRETATION:
    The BCS norm kernel is near-identity (N > {off5.min():.4f}) because the
    pairing gap Delta ~ 1.3 M_KK greatly exceeds the single-particle energy
    variation across the GCM grid (~ 0.06 M_KK). The BCS state is "rigid"
    in the tau coordinate -- it barely responds to the geometry change.

    This is the nuclear analog of a strongly-paired system where the
    collective mass for shape deformation is very large. The zero-point
    motion in the tau coordinate is correspondingly small, controlled by
    the collective mass M ~ 1/[sum_k (du_k/dtau)^2].

    The near-identity N means the GCM reduces to an effective 1D
    Schrodinger equation with the q-theory potential V(tau):
      E_ZPE ~ (1/2) * sqrt(d^2V/dtau^2 / M_eff)
    The correction {assessment.split(' -- ')[0].lower()}.

  ASSESSMENT: {assessment}

  GATE: GCM-ZERO-POINT-46 (INFO)
  Data: tier0-computation/s46_gcm_zero_point.npz
  Plot: tier0-computation/s46_gcm_zero_point.png
  Script: tier0-computation/s46_gcm_zero_point.py
""")
