"""
Session 24a Step 1: V_spec(tau; rho) — Spectral Action Potential
================================================================

V_spec(tau; rho) = -R_K(tau) + rho * [500*R_K(tau)^2 - 32*|Ric(tau)|^2 - 28*K(tau)]

where:
  R_K = scalar curvature
  |Ric|^2 = Ric_{ab} Ric^{ab} (Ricci squared)
  K = Kretschner scalar = R_{abcd} R^{abcd}
  rho = ratio of Seeley-DeWitt coefficients c_4/c_2

Data source: s23c_fiber_integrals.npz (from r20a_riemann_tensor.npz, 147/147 verified)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# =====================================================================
# LOAD DATA
# =====================================================================
base = "C:/sandbox/Ainulindale Exflation/tier0-computation"
d = np.load(f"{base}/s23c_fiber_integrals.npz")

tau = d['tau']           # shape (21,), range [0, 2]
R_K = d['R_scalar']      # scalar curvature
Ric_sq = d['Ric_sq']     # |Ric|^2
K = d['K_kretschner']    # Kretschner scalar

n_tau = len(tau)

# =====================================================================
# VALIDATION
# =====================================================================
print("=" * 60)
print("STEP 1: V_spec(tau; rho)")
print("=" * 60)
print(f"tau range: [{tau[0]:.3f}, {tau[-1]:.3f}], n_tau = {n_tau}")
print(f"R_K(0) = {R_K[0]:.6f} (expected 2.000)")
assert abs(R_K[0] - 2.0) < 1e-10, f"R_K(0) validation FAILED: {R_K[0]}"
print(f"Ric_sq(0) = {Ric_sq[0]:.6f} (expected 0.500)")
print(f"K(0) = {K[0]:.6f} (expected 0.500)")
print("R_K(0) = 2.000: PASS")

# =====================================================================
# COMPUTE V_spec
# =====================================================================
def V_spec(tau_arr, R_arr, Ric_sq_arr, K_arr, rho):
    """Compute V_spec at all tau for a given rho."""
    linear = -R_arr
    quadratic = 500.0 * R_arr**2 - 32.0 * Ric_sq_arr - 28.0 * K_arr
    return linear + rho * quadratic

# Primary rho values
rho_primary = np.array([0.001, 0.01, 0.05, 0.1, 0.5])
# Secondary (finer) rho values
rho_secondary = np.array([0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50])

# Compute V_spec for all rho
print("\n--- Primary rho scan ---")
V_primary = {}
for rho in rho_primary:
    V = V_spec(tau, R_K, Ric_sq, K, rho)
    V_primary[rho] = V
    print(f"  rho={rho:.3f}: V_spec range [{V.min():.4f}, {V.max():.4f}]")

# =====================================================================
# FIND MINIMA via finite differences
# =====================================================================
print("\n--- Minimum search (primary) ---")
results_primary = {}
for rho in rho_primary:
    V = V_primary[rho]
    # Finite difference dV/dtau
    dV = np.gradient(V, tau)
    # Look for sign changes in dV (negative -> positive = minimum)
    min_found = False
    tau_min = None
    V_min = None
    V_dd_min = None
    for i in range(len(dV) - 1):
        if dV[i] < 0 and dV[i+1] > 0:
            # Linear interpolation for zero crossing
            frac = -dV[i] / (dV[i+1] - dV[i])
            tau_cross = tau[i] + frac * (tau[i+1] - tau[i])
            # Interpolate V at the crossing
            V_cross = V[i] + frac * (V[i+1] - V[i])
            # Second derivative at crossing
            d2V = np.gradient(dV, tau)
            V_dd_cross = d2V[i] + frac * (d2V[i+1] - d2V[i])
            tau_min = tau_cross
            V_min = V_cross
            V_dd_min = V_dd_cross
            min_found = True
            break

    if min_found:
        in_window = 0.20 <= tau_min <= 0.40
        print(f"  rho={rho:.3f}: MINIMUM at tau={tau_min:.4f}, V={V_min:.6f}, V''={V_dd_min:.4f}, in_window={in_window}")
    else:
        # Check if monotonically decreasing or increasing
        if V[-1] < V[0]:
            print(f"  rho={rho:.3f}: NO MINIMUM (monotonically decreasing)")
        else:
            print(f"  rho={rho:.3f}: NO MINIMUM (monotonically increasing)")
    results_primary[rho] = {'min_found': min_found, 'tau_min': tau_min, 'V_min': V_min, 'V_dd_min': V_dd_min}

# Secondary scan
print("\n--- Secondary rho scan ---")
V_secondary = {}
results_secondary = {}
for rho in rho_secondary:
    V = V_spec(tau, R_K, Ric_sq, K, rho)
    V_secondary[rho] = V
    dV = np.gradient(V, tau)
    min_found = False
    tau_min = None
    V_min = None
    V_dd_min = None
    for i in range(len(dV) - 1):
        if dV[i] < 0 and dV[i+1] > 0:
            frac = -dV[i] / (dV[i+1] - dV[i])
            tau_cross = tau[i] + frac * (tau[i+1] - tau[i])
            V_cross = V[i] + frac * (V[i+1] - V[i])
            d2V = np.gradient(dV, tau)
            V_dd_cross = d2V[i] + frac * (d2V[i+1] - d2V[i])
            tau_min = tau_cross
            V_min = V_cross
            V_dd_min = V_dd_cross
            min_found = True
            break

    in_window = (0.20 <= tau_min <= 0.40) if min_found and tau_min is not None else False
    if min_found:
        print(f"  rho={rho:.3f}: tau_min={tau_min:.4f}, V_min={V_min:.6f}, V''={V_dd_min:.4f}, in_window={in_window}")
    else:
        print(f"  rho={rho:.3f}: NO MINIMUM")
    results_secondary[rho] = {'min_found': min_found, 'tau_min': tau_min, 'V_min': V_min, 'V_dd_min': V_dd_min}

# =====================================================================
# EUCLIDEAN ACTION (Step 5 data)
# =====================================================================
print("\n--- Euclidean Action at tau = {0.00, 0.10, 1.58} ---")
tau_IE = np.array([0.00, 0.10, 1.58])
# Interpolate V_spec at these tau for each rho
for rho in rho_secondary:
    V_all = V_spec(tau, R_K, Ric_sq, K, rho)
    V_at_IE = np.interp(tau_IE, tau, V_all)
    IE = -V_at_IE  # I_E = -V_spec * Vol(K), Vol(K) = const
    print(f"  rho={rho:.3f}: I_E(0.00)={IE[0]:.6f}, I_E(0.10)={IE[1]:.6f}, I_E(1.58)={IE[2]:.6f}")

# =====================================================================
# SAVE DATA
# =====================================================================
save_dict = {
    'tau': tau,
    'R_K': R_K,
    'Ric_sq': Ric_sq,
    'K_kretschner': K,
    'rho_primary': rho_primary,
    'rho_secondary': rho_secondary,
}

# Save V_spec for each rho
for rho in rho_secondary:
    key = f"V_spec_rho_{rho:.3f}".replace('.', 'p')
    save_dict[key] = V_spec(tau, R_K, Ric_sq, K, rho)

# Save minima results
tau_min_arr = []
V_min_arr = []
Vdd_min_arr = []
min_found_arr = []
for rho in rho_secondary:
    r = results_secondary[rho]
    min_found_arr.append(1 if r['min_found'] else 0)
    tau_min_arr.append(r['tau_min'] if r['tau_min'] is not None else -1.0)
    V_min_arr.append(r['V_min'] if r['V_min'] is not None else 0.0)
    Vdd_min_arr.append(r['V_dd_min'] if r['V_dd_min'] is not None else 0.0)

save_dict['min_found'] = np.array(min_found_arr)
save_dict['tau_min'] = np.array(tau_min_arr)
save_dict['V_min'] = np.array(V_min_arr)
save_dict['V_dd_min'] = np.array(Vdd_min_arr)

# Euclidean action
save_dict['tau_IE'] = tau_IE
for rho in rho_secondary:
    V_all = V_spec(tau, R_K, Ric_sq, K, rho)
    V_at_IE = np.interp(tau_IE, tau, V_all)
    IE = -V_at_IE
    key = f"IE_rho_{rho:.3f}".replace('.', 'p')
    save_dict[key] = IE

np.savez(f"{base}/s24a_vspec.npz", **save_dict)
print(f"\nSaved: {base}/s24a_vspec.npz")

# =====================================================================
# PLOT
# =====================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: V_spec(tau) for 5 primary rho values
ax = axes[0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i, rho in enumerate(rho_primary):
    V = V_primary[rho]
    ax.plot(tau, V, color=colors[i], linewidth=2, label=f'rho={rho}')
    # Mark minimum if found
    r = results_primary[rho]
    if r['min_found']:
        ax.axvline(r['tau_min'], color=colors[i], linestyle='--', alpha=0.5)
        ax.plot(r['tau_min'], r['V_min'], 'o', color=colors[i], markersize=8)

ax.axvspan(0.20, 0.40, alpha=0.15, color='green', label='Physical window')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('V_spec(tau)', fontsize=12)
ax.set_title('V_spec(tau; rho) — Spectral Action Potential', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Right panel: tau_min(rho) for secondary scan
ax2 = axes[1]
rhos_with_min = []
tau_mins = []
for rho in rho_secondary:
    r = results_secondary[rho]
    if r['min_found']:
        rhos_with_min.append(rho)
        tau_mins.append(r['tau_min'])

if rhos_with_min:
    ax2.semilogx(rhos_with_min, tau_mins, 'ko-', linewidth=2, markersize=8)
    ax2.axhspan(0.20, 0.40, alpha=0.15, color='green', label='Physical window')
    ax2.set_xlabel('rho (c_4/c_2)', fontsize=12)
    ax2.set_ylabel('tau_min', fontsize=12)
    ax2.set_title('Minimum location vs rho', fontsize=13)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
else:
    ax2.text(0.5, 0.5, 'No minima found', ha='center', va='center', fontsize=14,
             transform=ax2.transAxes)
    ax2.set_title('Minimum location vs rho', fontsize=13)

plt.tight_layout()
plt.savefig(f"{base}/s24a_vspec.png", dpi=150)
print(f"Saved: {base}/s24a_vspec.png")

print("\n" + "=" * 60)
print("STEP 1 COMPLETE")
print("=" * 60)
