#!/usr/bin/env python3
"""
Session 23a Pre-Check 3b: N=50 V_IR'' Sign Anomaly Investigation

The master synthesis flags an anomaly: V_IR'' > 0 at N=50 when N=10, 20, 100
all show V_IR'' < 0 at tau = 0.30. This script investigates with a finer N grid.

Loads the same data sources as s21c_V_IR.py:
  - s19a_sweep_data.npz: Dirac (fermionic) eigenvalues at 21 tau, with (p,q) labels
  - kk1_bosonic_spectrum.npz: Bosonic eigenvalues at 4 tau values

Computes V_IR(tau) at N = 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
at all 4 available tau values [0.0, 0.15, 0.30, 0.50].

Then computes V_IR'' at tau=0.30 for each N and plots V_IR''(0.30) vs N.

Diagnostic question: Is the sign change at N=50 a smooth crossover or a sharp jump?
"""

import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# 1. LOAD DATA
# ============================================================
dirac = np.load(os.path.join(data_dir, 's19a_sweep_data.npz'), allow_pickle=True)
tau_dirac = dirac['tau_values']

bos = np.load(os.path.join(data_dir, 'kk1_bosonic_spectrum.npz'), allow_pickle=True)
bos_tau_keys = sorted(bos.keys())
bos_tau_vals = np.array([float(k.split('_')[1]) for k in bos_tau_keys])

tau_compute = bos_tau_vals.copy()  # [0.0, 0.15, 0.30, 0.50]
print(f"tau_compute = {tau_compute}")
print(f"tau_dirac = {tau_dirac[:6]}...")

# ============================================================
# 2. HELPER FUNCTIONS (from s21c_V_IR.py)
# ============================================================
def get_fermionic_eigs_at_tau(tau_target, dirac_data, tau_vals, pq_max=2):
    """Extract sorted fermionic eigenvalues with p+q <= pq_max at given tau."""
    idx = np.argmin(np.abs(tau_vals - tau_target))
    if np.abs(tau_vals[idx] - tau_target) < 1e-6:
        eigs = dirac_data[f'eigenvalues_{idx}']
        p_arr = dirac_data[f'sector_p_{idx}']
        q_arr = dirac_data[f'sector_q_{idx}']
        mask = (p_arr + q_arr) <= pq_max
        return np.sort(np.abs(eigs[mask]))
    else:
        if tau_target < tau_vals[idx]:
            i1, i2 = idx - 1, idx
        else:
            i1, i2 = idx, idx + 1
        t1, t2 = tau_vals[i1], tau_vals[i2]
        alpha = (tau_target - t1) / (t2 - t1)
        eigs1 = dirac_data[f'eigenvalues_{i1}']
        p1 = dirac_data[f'sector_p_{i1}']
        q1 = dirac_data[f'sector_q_{i1}']
        mask1 = (p1 + q1) <= pq_max
        eigs2 = dirac_data[f'eigenvalues_{i2}']
        p2 = dirac_data[f'sector_p_{i2}']
        q2 = dirac_data[f'sector_q_{i2}']
        mask2 = (p2 + q2) <= pq_max
        sorted1 = np.sort(np.abs(eigs1[mask1]))
        sorted2 = np.sort(np.abs(eigs2[mask2]))
        return (1 - alpha) * sorted1 + alpha * sorted2

def get_bosonic_eigs_at_tau(tau_target, bos_data, bos_keys, bos_taus):
    """Extract sorted bosonic eigenvalues at given tau."""
    idx = np.argmin(np.abs(bos_taus - tau_target))
    key = bos_keys[idx]
    arr = bos_data[key]
    eigs = arr['eigenvalue']
    sorted_eigs = np.sort(eigs[eigs > 1e-10])
    return sorted_eigs

# ============================================================
# 3. COMPUTE V_IR AT FINE N GRID
# ============================================================
N_values = list(range(10, 101, 10))  # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"\nN values: {N_values}")

# Store results
V_IR_all = np.zeros((len(N_values), len(tau_compute)))
E_bos_all = np.zeros((len(N_values), len(tau_compute)))
E_ferm_all = np.zeros((len(N_values), len(tau_compute)))
FB_all = np.zeros((len(N_values), len(tau_compute)))

for i, N in enumerate(N_values):
    for j, tau in enumerate(tau_compute):
        feigs = get_fermionic_eigs_at_tau(tau, dirac, tau_dirac, pq_max=2)
        beigs = get_bosonic_eigs_at_tau(tau, bos, bos_tau_keys, bos_tau_vals)

        n_ferm = min(N, len(feigs))
        n_bos = min(N, len(beigs))

        E_ferm = 0.5 * np.sum(np.sqrt(feigs[:n_ferm]))
        E_bos = 0.5 * np.sum(np.sqrt(beigs[:n_bos]))

        V_IR_all[i, j] = E_bos - E_ferm
        E_bos_all[i, j] = E_bos
        E_ferm_all[i, j] = E_ferm
        FB_all[i, j] = E_ferm / E_bos if E_bos > 0 else np.nan

print("\nV_IR values:")
print(f"{'N':>5s}  {'tau=0.00':>10s}  {'tau=0.15':>10s}  {'tau=0.30':>10s}  {'tau=0.50':>10s}")
for i, N in enumerate(N_values):
    print(f"{N:5d}  {V_IR_all[i,0]:10.4f}  {V_IR_all[i,1]:10.4f}  {V_IR_all[i,2]:10.4f}  {V_IR_all[i,3]:10.4f}")

# ============================================================
# 4. COMPUTE V_IR'' AT EACH N
# ============================================================
# tau_compute = [0.0, 0.15, 0.30, 0.50] — non-uniform spacing
# For V_IR''(tau=0.30), use 3-point central difference with non-uniform spacing

print("\n" + "="*70)
print("V_IR'' ANALYSIS")
print("="*70)

V_IR_pp = np.zeros((len(N_values), len(tau_compute)))

for i, N in enumerate(N_values):
    V = V_IR_all[i, :]

    # Second derivative at each interior point (non-uniform spacing)
    for j in range(1, len(tau_compute) - 1):
        h1 = tau_compute[j] - tau_compute[j-1]
        h2 = tau_compute[j+1] - tau_compute[j]
        V_IR_pp[i, j] = 2 * (V[j+1]/(h2*(h1+h2)) - V[j]/(h1*h2) + V[j-1]/(h1*(h1+h2)))

    # Boundary points (3-point forward/backward)
    h1, h2 = tau_compute[1]-tau_compute[0], tau_compute[2]-tau_compute[1]
    V_IR_pp[i, 0] = 2*(V[0]/(h1*(h1+h2)) - V[1]/(h1*h2) + V[2]/(h2*(h1+h2)))
    h1, h2 = tau_compute[-2]-tau_compute[-3], tau_compute[-1]-tau_compute[-2]
    V_IR_pp[i, -1] = 2*(V[-3]/(h1*(h1+h2)) - V[-2]/(h1*h2) + V[-1]/(h2*(h1+h2)))

print(f"\n{'N':>5s}  {'V_IR_pp(0.00)':>14s}  {'V_IR_pp(0.15)':>14s}  {'V_IR_pp(0.30)':>14s}  {'V_IR_pp(0.50)':>14s}  {'Sign(0.30)':>10s}")
for i, N in enumerate(N_values):
    sign_str = "NEGATIVE" if V_IR_pp[i, 2] < 0 else "POSITIVE"
    print(f"{N:5d}  {V_IR_pp[i,0]:14.4f}  {V_IR_pp[i,1]:14.4f}  {V_IR_pp[i,2]:14.4f}  {V_IR_pp[i,3]:14.4f}  {sign_str:>10s}")

# ============================================================
# 5. CHARACTERIZE THE SIGN CHANGE
# ============================================================
print("\n" + "="*70)
print("SIGN CHANGE CHARACTERIZATION")
print("="*70)

vpp_030 = V_IR_pp[:, 2]  # V_IR'' at tau=0.30 for each N

# Find sign changes
sign_changes = []
for i in range(len(N_values) - 1):
    if vpp_030[i] * vpp_030[i+1] < 0:
        # Interpolate zero crossing
        N_cross = N_values[i] + (N_values[i+1] - N_values[i]) * (-vpp_030[i]) / (vpp_030[i+1] - vpp_030[i])
        sign_changes.append((N_values[i], N_values[i+1], N_cross))
        print(f"Sign change between N={N_values[i]} and N={N_values[i+1]}: zero crossing at N ~ {N_cross:.1f}")

if len(sign_changes) == 0:
    print("No sign changes detected in V_IR''(0.30) across the N range.")
elif len(sign_changes) == 1:
    N_lo, N_hi, N_cross = sign_changes[0]
    jump_magnitude = abs(vpp_030[N_values.index(N_hi)] - vpp_030[N_values.index(N_lo)])
    avg_deriv = np.mean(np.abs(np.diff(vpp_030)))

    if jump_magnitude > 3 * avg_deriv:
        print(f"\nVERDICT: SHARP JUMP (magnitude {jump_magnitude:.4f} vs avg step {avg_deriv:.4f})")
        print("This suggests a numerical artifact or a discrete mode entering the sum.")
    else:
        print(f"\nVERDICT: SMOOTH CROSSOVER (magnitude {jump_magnitude:.4f} vs avg step {avg_deriv:.4f})")
        print("This identifies a physical scale where UV modes begin dominating.")
else:
    print(f"\n{len(sign_changes)} sign changes detected — non-monotonic behavior in V_IR''(0.30) vs N.")
    print("This suggests oscillatory convergence, typical of competing bosonic/fermionic contributions.")

# ============================================================
# 6. ADDITIONAL DIAGNOSTICS
# ============================================================
print("\n--- Bosonic vs fermionic mode counts ---")
for j, tau in enumerate(tau_compute):
    feigs = get_fermionic_eigs_at_tau(tau, dirac, tau_dirac, pq_max=2)
    beigs = get_bosonic_eigs_at_tau(tau, bos, bos_tau_keys, bos_tau_vals)
    print(f"  tau={tau:.2f}: n_ferm(p+q<=2) = {len(feigs)}, n_bos = {len(beigs)}")

print("\n--- Mode energy at N boundaries ---")
# Show what eigenvalue enters the sum at N=40, 50, 60 for tau=0.30
tau_idx = 2  # tau=0.30
feigs = get_fermionic_eigs_at_tau(0.30, dirac, tau_dirac, pq_max=2)
beigs = get_bosonic_eigs_at_tau(0.30, bos, bos_tau_keys, bos_tau_vals)

for N in [30, 40, 50, 60, 70]:
    n_f = min(N, len(feigs))
    n_b = min(N, len(beigs))
    ferm_edge = feigs[n_f-1] if n_f > 0 else None
    bos_edge = beigs[n_b-1] if n_b > 0 else None
    ferm_next = feigs[n_f] if n_f < len(feigs) else None
    bos_next = beigs[n_b] if n_b < len(beigs) else None
    print(f"  N={N}: ferm_edge={ferm_edge:.6f}, bos_edge={bos_edge:.6f}"
          + (f", ferm_next={ferm_next:.6f}" if ferm_next is not None else "")
          + (f", bos_next={bos_next:.6f}" if bos_next is not None else ""))

# ============================================================
# 7. PLOT
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Session 23a Pre-Check 3b: V_IR'' Sign Anomaly at N=50", fontsize=14, fontweight='bold')

# Panel 1: V_IR''(0.30) vs N
ax = axes[0]
ax.plot(N_values, vpp_030, 'ko-', markersize=8, linewidth=2)
ax.axhline(y=0, color='r', linestyle='--', alpha=0.7, linewidth=1.5)
ax.set_xlabel('N (number of modes)', fontsize=12)
ax.set_ylabel("V_IR''(tau=0.30)", fontsize=12)
ax.set_title("V_IR'' at tau=0.30 vs N")
ax.grid(True, alpha=0.3)

# Mark sign changes
for N_lo, N_hi, N_cross in sign_changes:
    ax.axvline(x=N_cross, color='orange', linestyle=':', alpha=0.7, label=f'Zero at N~{N_cross:.0f}')
ax.legend()

# Panel 2: V_IR(tau) for all N values
ax = axes[1]
for i, N in enumerate(N_values):
    ax.plot(tau_compute, V_IR_all[i, :], 'o-', label=f'N={N}', markersize=5)
ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
ax.axvspan(0.15, 0.35, alpha=0.1, color='green')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('V_IR = E_bos - E_ferm', fontsize=12)
ax.set_title('V_IR(tau) for all N')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 3: F/B ratio at tau=0.30 vs N
ax = axes[2]
fb_030 = FB_all[:, 2]  # tau=0.30
ax.plot(N_values, fb_030, 'bs-', markersize=8, linewidth=2)
ax.axhline(y=0.55, color='r', linestyle='--', alpha=0.7, label='Trap value 0.55')
ax.axhline(y=1.0, color='k', linestyle=':', alpha=0.5, label='F/B = 1')
ax.set_xlabel('N (number of modes)', fontsize=12)
ax.set_ylabel('F/B ratio at tau=0.30', fontsize=12)
ax.set_title('F/B Convergence to Trap')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
out_png = os.path.join(data_dir, 's23a_precheck_3b.png')
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"\nPlot saved to {out_png}")
plt.close()

print("\n=== PRE-CHECK 3b COMPLETE ===")
