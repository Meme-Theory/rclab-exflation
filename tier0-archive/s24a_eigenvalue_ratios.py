"""
Session 24a Step 6: Eigenvalue Ratio Map
==========================================

r_n(tau) = |lambda_{n+1}| / |lambda_n| for n = 1,...,15
Mark phi_paasch = 1.53158 crossings (within 0.1%)

Data source: s23a_kosmann_singlet.npz — 16 eigenvalues in (0,0) singlet at 9 tau
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# =====================================================================
# LOAD DATA
# =====================================================================
base = "C:/sandbox/Ainulindale Exflation/tier0-computation"
d = np.load(f"{base}/s23a_kosmann_singlet.npz")

tau_values = d['tau_values']  # shape (9,)
n_tau = len(tau_values)

print("=" * 60)
print("STEP 6: Eigenvalue Ratio Map")
print("=" * 60)
print(f"tau values: {tau_values}")

phi_paasch = 1.53158
tolerance = 0.001  # 0.1%

# =====================================================================
# COMPUTE RATIOS
# =====================================================================
# ratios[t_idx, n] = |lambda_{n+1}|/|lambda_n| for sorted |eigenvalues|
ratios = np.zeros((n_tau, 15))
abs_evals_all = np.zeros((n_tau, 16))

for t_idx in range(n_tau):
    evals = d[f'eigenvalues_{t_idx}']  # shape (16,)
    # Sort by absolute value
    abs_sorted = np.sort(np.abs(evals))
    abs_evals_all[t_idx] = abs_sorted

    for n in range(15):
        if abs_sorted[n] < 1e-14:
            ratios[t_idx, n] = float('inf')
        else:
            ratios[t_idx, n] = abs_sorted[n+1] / abs_sorted[n]

    print(f"\n  tau={tau_values[t_idx]:.2f}: |eigenvalues| = {abs_sorted}")
    print(f"    ratios = {ratios[t_idx]}")

# =====================================================================
# PHI CROSSINGS
# =====================================================================
print(f"\n--- Phi crossings (phi_paasch = {phi_paasch}, tolerance = {tolerance*100}%) ---")
phi_crossings = []
for t_idx in range(n_tau):
    for n in range(15):
        r = ratios[t_idx, n]
        if abs(r - phi_paasch) / phi_paasch < tolerance:
            phi_crossings.append((tau_values[t_idx], n, r))
            print(f"  CROSSING: tau={tau_values[t_idx]:.2f}, ratio index n={n}, "
                  f"r_{n}={r:.6f}, deviation={abs(r-phi_paasch)/phi_paasch*100:.4f}%")

if not phi_crossings:
    print("  NO phi crossings found within 0.1% tolerance")
    # Try 1% tolerance
    print(f"\n  Relaxing to 1% tolerance:")
    for t_idx in range(n_tau):
        for n in range(15):
            r = ratios[t_idx, n]
            if abs(r - phi_paasch) / phi_paasch < 0.01:
                phi_crossings.append((tau_values[t_idx], n, r))
                print(f"    NEAR: tau={tau_values[t_idx]:.2f}, n={n}, r={r:.6f}, "
                      f"dev={abs(r-phi_paasch)/phi_paasch*100:.3f}%")

    if not phi_crossings:
        print("    NO phi crossings found within 1% tolerance either")
        # Report closest
        print(f"\n  Closest ratios to phi_paasch:")
        all_devs = []
        for t_idx in range(n_tau):
            for n in range(15):
                r = ratios[t_idx, n]
                if np.isfinite(r):
                    dev = abs(r - phi_paasch) / phi_paasch
                    all_devs.append((dev, tau_values[t_idx], n, r))
        all_devs.sort()
        for dev, tau, n, r in all_devs[:5]:
            print(f"    tau={tau:.2f}, n={n}, r={r:.6f}, dev={dev*100:.3f}%")

print(f"\nTotal phi crossings (0.1%): {sum(1 for c in phi_crossings if abs(c[2]-phi_paasch)/phi_paasch < tolerance)}")
print(f"Total phi near-misses (1%): {len(phi_crossings)}")

# =====================================================================
# SAVE
# =====================================================================
np.savez(f"{base}/s24a_eigenvalue_ratios.npz",
         tau=tau_values,
         ratios=ratios,
         abs_eigenvalues=abs_evals_all,
         phi_paasch=phi_paasch)
print(f"\nSaved: {base}/s24a_eigenvalue_ratios.npz")

# =====================================================================
# PLOT: Heatmap
# =====================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: heatmap
ax = axes[0]
# Clip ratios for plotting (exclude inf)
ratios_plot = np.clip(ratios, 0.5, 2.5)
im = ax.imshow(ratios_plot.T, aspect='auto', origin='lower',
               extent=[tau_values[0], tau_values[-1], 0.5, 15.5],
               cmap='RdYlBu_r', vmin=0.8, vmax=2.0)
# Mark phi crossings
for tau_c, n_c, r_c in phi_crossings:
    ax.plot(tau_c, n_c + 0.5, 'k*', markersize=15, markeredgecolor='white')
ax.axhline(y=phi_paasch, color='k', linestyle='--', alpha=0.3)
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('Ratio index n', fontsize=12)
ax.set_title('Eigenvalue Ratios r_n = |lambda_{n+1}|/|lambda_n|', fontsize=13)
plt.colorbar(im, ax=ax, label='Ratio')

# Right: line plot of ratios vs tau for selected n
ax2 = axes[1]
# Pick a few representative ratio indices
for n in [0, 3, 7, 11, 14]:
    ax2.plot(tau_values, ratios[:, n], '-o', linewidth=1.5, markersize=5, label=f'n={n}')
ax2.axhline(y=phi_paasch, color='red', linestyle='--', linewidth=2, label=f'phi={phi_paasch}')
ax2.set_xlabel('tau', fontsize=12)
ax2.set_ylabel('r_n(tau)', fontsize=12)
ax2.set_title('Selected Eigenvalue Ratios vs tau', fontsize=13)
ax2.legend(fontsize=9, ncol=2)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0.8, 2.0)

plt.tight_layout()
plt.savefig(f"{base}/s24a_eigenvalue_ratios.png", dpi=150)
print(f"Saved: {base}/s24a_eigenvalue_ratios.png")

print("\n" + "=" * 60)
print("STEP 6 COMPLETE")
print("=" * 60)
