#!/usr/bin/env python3
"""
Session 32a -- UMKLAPP-1 + AUTO-1: Branch classification, vertex sign, group velocities.

UMKLAPP-1: Compute the B3->B2+B1 anharmonic coupling vertex V_{B3,B2,B1}.
  - Sign determines Turing instability channel (activator-inhibitor structure).
  - V > 0: B3 feeds B2 (Turing open). V < 0: B3 depletes B2 (Turing closed).

AUTO-1: Map group velocities v_group(tau) = dlambda_k/dtau for all 8 singlet modes.
  - Find v=0 crossings (bound states in the continuum).
  - If v=0 in [0.10, 0.31]: autoresonance channel open.

Physics:
  At tau=0, the (0,0) singlet sector of D_K on SU(3) with bi-invariant metric has
  8-fold degeneracy at lambda = sqrt(3)/2. Jensen deformation (tau > 0) lifts this
  into B1(1) + B2(4) + B3(3) under residual U(2) symmetry:
    B3 (adjoint, 3 modes): largest |dlambda/dtau| ~ 0.75
    B2 (fundamental, 4 modes): smallest |dlambda/dtau| ~ -0.02 to +0.08
    B1 (trivial, 1 mode): intermediate |dlambda/dtau| ~ -0.33

Input: tier0-computation/s23a_gap_equation.npz
Output: tier0-computation/s32a_umklapp_vertex.npz, .png
Gates: U-32a (vertex sign), A-32a (v=0 in instanton orbit)

Author: phonon-exflation-sim agent, Session 32a
Date: 2026-03-02
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 0. LOAD DATA
# ============================================================

data_dir = Path(__file__).parent
gap_data = np.load(data_dir / 's23a_gap_equation.npz', allow_pickle=True)
tau_values = gap_data['tau_values']
n_tau = len(tau_values)

print(f"tau_values = {tau_values}")
print(f"n_tau = {n_tau}")

# Extract positive eigenvalues (8 per tau) -- sorted ascending
pos_evals = np.zeros((n_tau, 8))
for i in range(n_tau):
    ev = gap_data[f'eigenvalues_{i}']
    pos = np.sort(ev[ev > 0])
    assert len(pos) == 8, f"Expected 8 positive eigenvalues at tau={tau_values[i]}, got {len(pos)}"
    pos_evals[i] = pos

print("\n=== POSITIVE EIGENVALUES (sorted ascending at each tau) ===")
for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: {np.array2string(pos_evals[i], precision=6, separator=', ')}")

# ============================================================
# 1. BRANCH CLASSIFICATION BY EIGENVALUE TRACKING
# ============================================================
# Strategy: At tau=0, all 8 modes degenerate. At tau=0.1 (first nonzero), the
# splitting is already clean: 3 modes at ~0.916, 4 modes at ~0.850, 1 mode at ~0.833.
# Sort by eigenvalue at each tau and track by continuity.
#
# The sorted-ascending order at tau>0 is: B1(1), B2(4), B3(3).
# This means: index 0 = B1, indices 1-4 = B2, indices 5-7 = B3.

# Verify the degeneracy pattern at tau=0.10
ev_tau01 = pos_evals[1]
print(f"\nDegeneracy check at tau=0.10:")
print(f"  Mode 0 (B1):      {ev_tau01[0]:.6f}")
print(f"  Modes 1-4 (B2):   {ev_tau01[1:5]} -- spread={np.ptp(ev_tau01[1:5]):.2e}")
print(f"  Modes 5-7 (B3):   {ev_tau01[5:8]} -- spread={np.ptp(ev_tau01[5:8]):.2e}")

# Verify consistency across all tau
print("\n=== BRANCH CLASSIFICATION ===")
branch_labels = ['B1'] + ['B2']*4 + ['B3']*3
for i in range(n_tau):
    e = pos_evals[i]
    b1 = e[0]
    b2_mean = np.mean(e[1:5])
    b2_spread = np.ptp(e[1:5])
    b3_mean = np.mean(e[5:8])
    b3_spread = np.ptp(e[5:8])
    print(f"  tau={tau_values[i]:.2f}: B1={b1:.6f}  B2={b2_mean:.6f}(+/-{b2_spread:.2e})  "
          f"B3={b3_mean:.6f}(+/-{b3_spread:.2e})  gap(B2-B1)={b2_mean-b1:.6f}  gap(B3-B2)={b3_mean-b2_mean:.6f}")

# Branch-averaged eigenvalues
B1_evals = pos_evals[:, 0]           # shape (9,)
B2_evals = pos_evals[:, 1:5]         # shape (9, 4)
B3_evals = pos_evals[:, 5:8]         # shape (9, 3)
B2_mean = np.mean(B2_evals, axis=1)  # shape (9,)
B3_mean = np.mean(B3_evals, axis=1)  # shape (9,)

# ============================================================
# 2. GROUP VELOCITIES (AUTO-1)
# ============================================================
# v_group_k(tau) = dlambda_k/dtau computed by finite differences.
# Use centered differences where possible, one-sided at boundaries.

dtau = np.diff(tau_values)  # non-uniform spacing

# Compute derivatives for all 8 modes
v_group = np.zeros((n_tau, 8))
for k in range(8):
    lam = pos_evals[:, k]
    for i in range(n_tau):
        if i == 0:
            # Forward difference (tau=0 -> tau=0.1)
            v_group[i, k] = (lam[1] - lam[0]) / dtau[0]
        elif i == n_tau - 1:
            # Backward difference
            v_group[i, k] = (lam[-1] - lam[-2]) / dtau[-1]
        else:
            # Centered difference (non-uniform spacing)
            h_left = dtau[i-1]
            h_right = dtau[i]
            v_group[i, k] = (lam[i+1] - lam[i-1]) / (h_left + h_right)

print("\n=== GROUP VELOCITIES v_group = dlambda/dtau ===")
print(f"{'tau':>6s}  {'B1':>10s}  {'B2_0':>10s}  {'B2_1':>10s}  {'B2_2':>10s}  {'B2_3':>10s}  "
      f"{'B3_0':>10s}  {'B3_1':>10s}  {'B3_2':>10s}")
for i in range(n_tau):
    vals = '  '.join(f'{v_group[i, k]:10.6f}' for k in range(8))
    print(f"  {tau_values[i]:.2f}  {vals}")

# Branch-averaged group velocities
v_B1 = v_group[:, 0]
v_B2 = np.mean(v_group[:, 1:5], axis=1)
v_B3 = np.mean(v_group[:, 5:8], axis=1)

print("\n=== BRANCH-AVERAGED GROUP VELOCITIES ===")
for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: v_B1={v_B1[i]:.6f}  v_B2={v_B2[i]:.6f}  v_B3={v_B3[i]:.6f}")

# ============================================================
# 3. FIND v=0 CROSSINGS
# ============================================================
# For each mode, find tau values where v_group crosses zero by linear interpolation.
v_zero_points = []

for k in range(8):
    branch = branch_labels[k]
    for i in range(n_tau - 1):
        v_i = v_group[i, k]
        v_next = v_group[i+1, k]
        if v_i * v_next < 0:  # sign change
            # Linear interpolation
            tau_zero = tau_values[i] + (-v_i) * (tau_values[i+1] - tau_values[i]) / (v_next - v_i)
            lam_zero = np.interp(tau_zero, tau_values, pos_evals[:, k])
            v_zero_points.append({
                'mode': k,
                'branch': branch,
                'tau_zero': tau_zero,
                'lambda_zero': lam_zero,
                'v_left': v_i,
                'v_right': v_next
            })

print(f"\n=== v=0 CROSSINGS (sign changes in v_group) ===")
if len(v_zero_points) == 0:
    print("  NONE FOUND -- no mode has v_group = 0 crossing in [0, 0.50]")
else:
    for pt in v_zero_points:
        in_instanton = "YES" if 0.10 <= pt['tau_zero'] <= 0.31 else "NO"
        print(f"  Mode {pt['mode']} ({pt['branch']}): v=0 at tau={pt['tau_zero']:.4f}, "
              f"lambda={pt['lambda_zero']:.6f}, in instanton orbit: {in_instanton}")

# ============================================================
# 4. BANDWIDTHS
# ============================================================
# W_k = max(lambda_k(tau)) - min(lambda_k(tau)) for each mode
bandwidths = np.ptp(pos_evals, axis=0)  # shape (8,)

print(f"\n=== BANDWIDTHS W_k = max - min across tau ===")
for k in range(8):
    print(f"  Mode {k} ({branch_labels[k]}): W = {bandwidths[k]:.6f}")

W_B1 = bandwidths[0]
W_B2 = np.mean(bandwidths[1:5])
W_B3 = np.mean(bandwidths[5:8])
print(f"\n  Branch averages: W_B1={W_B1:.6f}  W_B2={W_B2:.6f}  W_B3={W_B3:.6f}")

# ============================================================
# 5. UMKLAPP VERTEX -- d^3(sum_k lambda_k)/dtau^3
# ============================================================
# Total trace: S(tau) = sum_{k=0}^{7} lambda_k(tau)
S_total = np.sum(pos_evals, axis=1)  # shape (9,)

# Branch sums
S_B1 = B1_evals.copy()                       # 1 mode
S_B2 = np.sum(B2_evals, axis=1)              # 4 modes
S_B3 = np.sum(B3_evals, axis=1)              # 3 modes

print(f"\n=== BRANCH SUMS S_Bi(tau) ===")
for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: S_B1={S_B1[i]:.6f}  S_B2={S_B2[i]:.6f}  S_B3={S_B3[i]:.6f}  "
          f"total={S_total[i]:.6f}")

# Compute derivatives of branch sums by finite difference
def finite_diff_deriv(y, x):
    """Compute dy/dx using centered differences (non-uniform spacing)."""
    n = len(x)
    dydx = np.zeros(n)
    for i in range(n):
        if i == 0:
            dydx[i] = (y[1] - y[0]) / (x[1] - x[0])
        elif i == n - 1:
            dydx[i] = (y[-1] - y[-2]) / (x[-1] - x[-2])
        else:
            h_l = x[i] - x[i-1]
            h_r = x[i+1] - x[i]
            dydx[i] = (y[i+1] - y[i-1]) / (h_l + h_r)
    return dydx

# First derivatives (already computed as group velocities, but for branch sums)
dS_B1 = finite_diff_deriv(S_B1, tau_values)
dS_B2 = finite_diff_deriv(S_B2, tau_values)
dS_B3 = finite_diff_deriv(S_B3, tau_values)
dS_total = finite_diff_deriv(S_total, tau_values)

# Second derivatives
d2S_B1 = finite_diff_deriv(dS_B1, tau_values)
d2S_B2 = finite_diff_deriv(dS_B2, tau_values)
d2S_B3 = finite_diff_deriv(dS_B3, tau_values)
d2S_total = finite_diff_deriv(dS_total, tau_values)

# Third derivatives
d3S_B1 = finite_diff_deriv(d2S_B1, tau_values)
d3S_B2 = finite_diff_deriv(d2S_B2, tau_values)
d3S_B3 = finite_diff_deriv(d2S_B3, tau_values)
d3S_total = finite_diff_deriv(d2S_total, tau_values)

print(f"\n=== THIRD DERIVATIVES d^3 S_Bi / dtau^3 ===")
for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: d3S_B1={d3S_B1[i]:+.6f}  d3S_B2={d3S_B2[i]:+.6f}  "
          f"d3S_B3={d3S_B3[i]:+.6f}  d3S_total={d3S_total[i]:+.6f}")

# ============================================================
# 5b. UMKLAPP VERTEX: Three-branch coupling V_{B3,B2,B1}
# ============================================================
# The cubic anharmonic vertex for the B3->B2+B1 process is the mixed partial
# derivative projected onto the three-branch structure.
#
# Method 1: Direct cubic vertex from spectral action expansion.
#   V_cubic = d^3/dtau^3 (sum_k lambda_k) is the total cubic anharmonicity.
#   The branch-resolved vertex is the cross-term between the three branches.
#
# Method 2: Product decomposition.
#   The spectral action's third derivative decomposes as:
#   d^3(S_total)/dtau^3 = d^3(S_B1+S_B2+S_B3)/dtau^3
#     = d^3 S_B1/dtau^3 + d^3 S_B2/dtau^3 + d^3 S_B3/dtau^3
#   This is the INTRA-branch contribution.
#
#   The INTER-branch (umklapp) vertex requires the mixed-mode coupling.
#   From the Taylor expansion of V_spec around tau_0:
#     V_spec(tau) = V_0 + V_1 * delta_tau + (1/2) V_2 * delta_tau^2 + (1/6) V_3 * delta_tau^3 + ...
#   where V_3 = d^3 V_spec/dtau^3.
#
#   The inter-branch vertex is:
#     V_{B3,B2,B1} = d/dtau [dS_B3/dtau * dS_B2/dtau * dS_B1/dtau] / (dS_B3 * dS_B2 * dS_B1)
#   evaluated at the gradient-balance point.
#
#   More precisely, for the Turing mechanism we need the sign of the cross-coupling:
#   does B3 excitation transfer energy to B2?
#
# Physical definition: The vertex V_{B3,B2,B1} is the coefficient of the
# phi_B3 * phi_B2 * phi_B1 term in the anharmonic Hamiltonian, where phi_Bi
# are the amplitude operators for each branch. In the eigenvalue-sum
# approximation, this is extracted from the mixed third derivative:
#
#   V_{321} = (d/dtau_3)(d/dtau_2)(d/dtau_1) V_spec
#
# Since we have only ONE deformation parameter tau (Jensen), all branches
# are driven by the same tau. The mixed vertex is the correlation of
# branch responses to the same drive:
#
#   V_{321}(tau) ~ dS_B3/dtau * dS_B2/dtau * dS_B1/dtau
#
# This product's sign determines energy flow direction.

# Method: Product of first derivatives (phase correlation)
vertex_product = dS_B3 * dS_B2 * dS_B1

print(f"\n=== UMKLAPP VERTEX: V_product = dS_B3 * dS_B2 * dS_B1 ===")
for i in range(n_tau):
    sign = "+" if vertex_product[i] > 0 else "-" if vertex_product[i] < 0 else "0"
    print(f"  tau={tau_values[i]:.2f}: V_product = {vertex_product[i]:+.6f}  "
          f"[dS_B3={dS_B3[i]:+.6f}, dS_B2={dS_B2[i]:+.6f}, dS_B1={dS_B1[i]:+.6f}]  sign: {sign}")

# Gradient-balance point: tau ~ 0.18. Closest grid point is tau=0.20 (index 3).
# Also evaluate at tau=0.15 (index 2).
idx_15 = 2  # tau=0.15
idx_20 = 3  # tau=0.20

print(f"\n=== VERTEX AT KEY POINTS ===")
for idx, label in [(idx_15, "tau=0.15"), (idx_20, "tau=0.20")]:
    print(f"  {label}: V_product = {vertex_product[idx]:+.8f}")
    print(f"    dS_B3/dtau = {dS_B3[idx]:+.8f} (3 modes, optical)")
    print(f"    dS_B2/dtau = {dS_B2[idx]:+.8f} (4 modes, flat)")
    print(f"    dS_B1/dtau = {dS_B1[idx]:+.8f} (1 mode, acoustic)")

# Also compute the cubic vertex as d^3(S_total)/dtau^3 for comparison
# (this includes all intra- and inter-branch terms)
print(f"\n=== TOTAL CUBIC ANHARMONICITY d^3 S_total / dtau^3 ===")
for idx, label in [(idx_15, "tau=0.15"), (idx_20, "tau=0.20")]:
    print(f"  {label}: d^3S/dtau^3 = {d3S_total[idx]:+.8f}")

# Turing mechanism assessment
# D_B3/D_B2 ~ (v_B3)^2 / (v_B2)^2 at the gradient-balance point
for idx, label in [(idx_15, "tau=0.15"), (idx_20, "tau=0.20")]:
    v3 = np.mean(np.abs(v_group[idx, 5:8]))
    v2 = np.mean(np.abs(v_group[idx, 1:5]))
    D_ratio = (v3 / v2)**2 if v2 > 1e-10 else float('inf')
    print(f"\n  {label}: |v_B3| = {v3:.6f}, |v_B2| = {v2:.6f}, D_B3/D_B2 = {D_ratio:.1f}")

# ============================================================
# 6. GATE CLASSIFICATIONS
# ============================================================

# U-32a: Vertex sign
# Evaluate at gradient-balance region (tau = 0.15 to 0.20)
V_at_balance = vertex_product[idx_15]
if V_at_balance > 0:
    u32a_verdict = "PASS"
    u32a_detail = f"V_product = {V_at_balance:+.6f} > 0. B3 feeds B2 (activator-inhibitor satisfied)."
elif V_at_balance < 0:
    u32a_verdict = "FAIL"
    u32a_detail = f"V_product = {V_at_balance:+.6f} < 0. B3 depletes B2 (wrong sign)."
else:
    u32a_verdict = "STRUCTURAL"
    u32a_detail = f"V_product = 0. Selection rule."

# A-32a: v=0 in instanton orbit [0.10, 0.31]
instanton_v_zeros = [pt for pt in v_zero_points if 0.10 <= pt['tau_zero'] <= 0.31]
if len(instanton_v_zeros) > 0:
    a32a_verdict = "PASS"
    modes_str = ', '.join(f"mode {pt['mode']}({pt['branch']}) at tau={pt['tau_zero']:.3f}"
                          for pt in instanton_v_zeros)
    a32a_detail = f"v=0 at: {modes_str}. Autoresonance channel open."
else:
    a32a_verdict = "OPEN"
    all_v_zeros_str = ', '.join(f"mode {pt['mode']}({pt['branch']}) at tau={pt['tau_zero']:.3f}"
                                for pt in v_zero_points) if v_zero_points else "none"
    a32a_detail = f"No v=0 in instanton orbit [0.10, 0.31]. All v=0 points: {all_v_zeros_str}."

print(f"\n{'='*60}")
print(f"GATE U-32a: {u32a_verdict} -- {u32a_detail}")
print(f"GATE A-32a: {a32a_verdict} -- {a32a_detail}")
print(f"{'='*60}")

# ============================================================
# 7. SAVE RESULTS
# ============================================================

np.savez(data_dir / 's32a_umklapp_vertex.npz',
    # Input
    tau_values=tau_values,
    pos_evals=pos_evals,
    # Branch classification
    branch_labels=np.array(branch_labels),
    B1_evals=B1_evals,
    B2_evals=B2_evals,
    B3_evals=B3_evals,
    B2_mean=B2_mean,
    B3_mean=B3_mean,
    # Group velocities
    v_group=v_group,
    v_B1=v_B1,
    v_B2=v_B2,
    v_B3=v_B3,
    # v=0 crossings
    n_v_zero=len(v_zero_points),
    v_zero_taus=np.array([pt['tau_zero'] for pt in v_zero_points]) if v_zero_points else np.array([]),
    v_zero_modes=np.array([pt['mode'] for pt in v_zero_points]) if v_zero_points else np.array([]),
    v_zero_lambdas=np.array([pt['lambda_zero'] for pt in v_zero_points]) if v_zero_points else np.array([]),
    # Bandwidths
    bandwidths=bandwidths,
    W_B1=W_B1,
    W_B2=W_B2,
    W_B3=W_B3,
    # Derivatives
    dS_B1=dS_B1, dS_B2=dS_B2, dS_B3=dS_B3,
    d2S_B1=d2S_B1, d2S_B2=d2S_B2, d2S_B3=d2S_B3,
    d3S_B1=d3S_B1, d3S_B2=d3S_B2, d3S_B3=d3S_B3,
    d3S_total=d3S_total,
    # Vertex
    vertex_product=vertex_product,
    # Gate verdicts
    u32a_verdict=u32a_verdict,
    a32a_verdict=a32a_verdict,
)

print(f"\nSaved: s32a_umklapp_vertex.npz")

# ============================================================
# 8. PLOTS
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 32a: UMKLAPP-1 + AUTO-1 -- Branch Classification & Vertex', fontsize=14)

# Panel (a): Eigenvalue branches
ax = axes[0, 0]
ax.plot(tau_values, B1_evals, 'ko-', label='B1 (trivial, 1 mode)', markersize=5)
for j in range(4):
    label = 'B2 (fund, 4 modes)' if j == 0 else None
    ax.plot(tau_values, B2_evals[:, j], 'b.-', label=label, alpha=0.7, markersize=4)
for j in range(3):
    label = 'B3 (adj, 3 modes)' if j == 0 else None
    ax.plot(tau_values, B3_evals[:, j], 'r^-', label=label, alpha=0.7, markersize=4)
ax.axhline(y=np.sqrt(3)/2, color='gray', linestyle='--', alpha=0.5, label=r'$\sqrt{3}/2$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\lambda_k$')
ax.set_title('(a) Eigenvalue Branches')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): Group velocities
ax = axes[0, 1]
ax.plot(tau_values, v_group[:, 0], 'ko-', label='B1', markersize=5)
for j in range(1, 5):
    label = 'B2' if j == 1 else None
    ax.plot(tau_values, v_group[:, j], 'b.-', label=label, alpha=0.7, markersize=4)
for j in range(5, 8):
    label = 'B3' if j == 5 else None
    ax.plot(tau_values, v_group[:, j], 'r^-', label=label, alpha=0.7, markersize=4)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
# Mark v=0 crossings
for pt in v_zero_points:
    color = {'B1': 'black', 'B2': 'blue', 'B3': 'red'}[pt['branch']]
    ax.axvline(x=pt['tau_zero'], color=color, linestyle=':', alpha=0.5)
    ax.plot(pt['tau_zero'], 0, 'D', color=color, markersize=8, zorder=5)
# Shade instanton orbit
ax.axvspan(0.10, 0.31, alpha=0.1, color='green', label='Instanton orbit')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$v_{\rm group} = d\lambda_k/d\tau$')
ax.set_title('(b) Group Velocities + v=0 Crossings')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Vertex product (Umklapp sign)
ax = axes[1, 0]
ax.plot(tau_values, vertex_product, 'gs-', label=r'$V_{\rm product} = dS_{B3} \cdot dS_{B2} \cdot dS_{B1}$',
        markersize=6, linewidth=2)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
ax.axvspan(0.10, 0.31, alpha=0.1, color='green', label='Instanton orbit')
ax.fill_between(tau_values, 0, vertex_product, where=(vertex_product > 0),
                alpha=0.2, color='green', label='Turing OPEN (V > 0)')
ax.fill_between(tau_values, 0, vertex_product, where=(vertex_product < 0),
                alpha=0.2, color='red', label='Turing CLOSED (V < 0)')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{\rm product}$')
ax.set_title(f'(c) Umklapp Vertex Sign [U-32a: {u32a_verdict}]')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Branch sums and their derivatives
ax = axes[1, 1]
ax2 = ax.twinx()
ax.plot(tau_values, S_B1, 'k-', label='S_B1', linewidth=2)
ax.plot(tau_values, S_B2, 'b-', label='S_B2', linewidth=2)
ax.plot(tau_values, S_B3, 'r-', label='S_B3', linewidth=2)
ax2.plot(tau_values, d3S_total, 'g--', label='d3S_total/dtau3', linewidth=1.5, alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Branch sums $S_{Bi}$')
ax2.set_ylabel(r'$d^3 S_{\rm total}/d\tau^3$', color='green')
ax.set_title('(d) Branch Sums & Total Cubic')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(data_dir / 's32a_umklapp_vertex.png', dpi=150, bbox_inches='tight')
print(f"Saved: s32a_umklapp_vertex.png")

print("\n=== COMPUTATION COMPLETE ===")
