"""
N-31Cg: Self-Consistent Cranking Check
Session 31Ca -- Baptista agent

Tests whether any Kapitza minima are self-consistent: does the effective modulus
frequency at the Kapitza-stabilized point equal the assumed drive frequency?

For each Kapitza minimum at reduced omega:
  - Extract d^2V/dtau^2 at the minimum
  - Compute omega_out^2 = (1/m_tau) * d^2V/dtau^2 where m_tau = 5 (Baptista Paper 15 eq 3.79)
  - Check omega_out/omega_input in [0.8, 1.2]

Gate N-31Cg-G: PASS if fixed point at omega^2 in [1, 8].

Input: s31Ba_kapitza_gate.npz
Output: s31Cg_selfconsistent_cranking.{npz,png}
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Load Kapitza data ──
kap = np.load('tier0-computation/s31Ba_kapitza_gate.npz', allow_pickle=True)
tau = kap['tau_fine']  # (201,)
V_jensen = kap['V_jensen']  # (201,)
omega_sq_T3 = float(kap['omega_sq_T3'])  # 8.326
omega_sq_T4 = float(kap['omega_sq_T4'])  # 9.893
A_values = kap['A_values']

print(f"tau range: [{tau[0]:.3f}, {tau[-1]:.3f}], N={len(tau)}")
print(f"omega_sq_T3 = {omega_sq_T3:.4f}")
print(f"omega_sq_T4 = {omega_sq_T4:.4f}")
print(f"A_values: {A_values}")

# Modulus kinetic mass from Baptista Paper 15 eq 3.79: (5/2)*dot{sigma}^2
# => m_tau = 5 (coefficient of (1/2)*m*dot{tau}^2 in the kinetic energy)
m_tau = 5.0

# ── Strategy: Construct V_Kapitza at a range of drive frequencies ──
# The Kapitza effective potential is:
# V_Kap(tau) = V(tau) + A^2 * |V'(tau)|^2 / (4 * omega^2)
# where V'(tau) is the derivative of the static potential.
# The "correction" term is the Kapitza ponderomotive potential.

# Compute V'(tau) and V''(tau) from the Jensen potential
dtau = tau[1] - tau[0]
dV = np.gradient(V_jensen, dtau)
d2V = np.gradient(dV, dtau)

# Sweep over drive frequencies
omega_sq_scan = np.linspace(0.5, 12.0, 47)  # broader range for fixed-point search
A_ref = 0.08  # reference amplitude from K-1

# For each omega_sq, construct V_Kap and find minima
fixed_points = []
omega_out_all = []
omega_in_all = []

print("\n--- Scanning omega^2 for self-consistent cranking ---")
for omega_sq in omega_sq_scan:
    omega = np.sqrt(omega_sq)

    # Kapitza effective potential: V_Kap = V + A^2 |V'|^2 / (4*omega^2)
    V_corr = A_ref**2 * dV**2 / (4.0 * omega_sq)
    V_kap = V_jensen + V_corr

    # Find local minima of V_kap (interior only)
    dV_kap = np.gradient(V_kap, dtau)
    d2V_kap = np.gradient(dV_kap, dtau)

    # Sign changes in dV_kap (negative -> positive = minimum)
    for i in range(1, len(dV_kap) - 1):
        if dV_kap[i-1] < 0 and dV_kap[i+1] > 0:
            # Interior minimum found
            tau_min = tau[i]
            d2V_at_min = d2V_kap[i]

            if d2V_at_min > 0:
                # Self-consistent frequency
                omega_out_sq = d2V_at_min / m_tau
                omega_out = np.sqrt(omega_out_sq)
                ratio = omega_out_sq / omega_sq

                omega_in_all.append(omega_sq)
                omega_out_all.append(omega_out_sq)

                if 0.8 <= np.sqrt(ratio) <= 1.2:
                    fixed_points.append({
                        'omega_in_sq': omega_sq,
                        'omega_out_sq': omega_out_sq,
                        'tau_min': tau_min,
                        'd2V': d2V_at_min,
                        'ratio': ratio,
                        'ratio_sqrt': np.sqrt(ratio),
                    })
                    print(f"  FIXED POINT: omega_in^2={omega_sq:.3f}, omega_out^2={omega_out_sq:.3f}, "
                          f"tau_min={tau_min:.4f}, ratio_sqrt={np.sqrt(ratio):.4f}")

omega_in_all = np.array(omega_in_all)
omega_out_all = np.array(omega_out_all)

# ── Also check the actual V_Kapitza data from s31Ba ──
# The stored V_kap arrays may have different structure
print("\n--- Checking stored Kapitza profiles ---")
for amp_str in ['A0p02', 'A0p05', 'A0p08', 'A0p10', 'A0p12', 'A0p15']:
    for mode in ['T3', 'T4']:
        key = f'V_kap_{mode}_{amp_str}'
        if key in kap:
            V_k = kap[key]
            dV_k = np.gradient(V_k, dtau)
            d2V_k = np.gradient(dV_k, dtau)

            # Find interior minima
            for i in range(5, len(dV_k) - 5):
                if dV_k[i-1] < 0 and dV_k[i+1] > 0 and d2V_k[i] > 0:
                    omega_drive_sq = omega_sq_T3 if mode == 'T3' else omega_sq_T4
                    omega_out_sq = d2V_k[i] / m_tau
                    ratio_sqrt = np.sqrt(omega_out_sq / omega_drive_sq)
                    print(f"  {key}: min at tau={tau[i]:.4f}, d2V={d2V_k[i]:.2f}, "
                          f"omega_out^2={omega_out_sq:.2f}, ratio_sqrt={ratio_sqrt:.4f}")

# ── Also compute d^2V/dtau^2 of V_jensen at the Kapitza "maximum" location ──
# (V_kap_T3_A0p08 has a MAX near tau=0.184, not a min)
print("\n--- Jensen potential curvature analysis ---")
print(f"V_jensen range: [{V_jensen.min():.2f}, {V_jensen.max():.2f}]")
print(f"V_jensen is {'monotonically increasing' if np.all(np.diff(V_jensen) > 0) else 'non-monotonic'}")

# d2V/dtau2 of Jensen at key tau values
for tau_check in [0.15, 0.18, 0.21, 0.25, 0.30]:
    idx = np.argmin(np.abs(tau - tau_check))
    print(f"  tau={tau_check:.2f}: d2V/dtau2 = {d2V[idx]:.2f}, omega_natural^2 = {d2V[idx]/m_tau:.4f}")

# ── Gate classification ──
has_fixed_point_in_range = any(1.0 <= fp['omega_in_sq'] <= 8.0 for fp in fixed_points)

print(f"\n=== GATE N-31Cg-G ===")
print(f"  Fixed points found: {len(fixed_points)}")
for fp in fixed_points:
    print(f"    omega^2={fp['omega_in_sq']:.3f}, tau={fp['tau_min']:.4f}, "
          f"omega_out/omega_in={fp['ratio_sqrt']:.4f}")

if has_fixed_point_in_range:
    verdict = "PASS"
    fp_best = [fp for fp in fixed_points if 1.0 <= fp['omega_in_sq'] <= 8.0][0]
    print(f"  VERDICT: PASS -- Self-consistent fixed point at omega^2={fp_best['omega_in_sq']:.3f}, "
          f"tau={fp_best['tau_min']:.4f}")
elif len(fixed_points) > 0:
    verdict = "MARGINAL"
    print(f"  VERDICT: MARGINAL -- Fixed points exist but outside [1, 8] range")
else:
    verdict = "FAIL"
    if len(omega_out_all) > 0:
        max_ratio = np.max(omega_out_all / omega_in_all)
        print(f"  VERDICT: FAIL -- No self-consistent fixed point. Max omega_out/omega_in = {np.sqrt(max_ratio):.4f}")
    else:
        print(f"  VERDICT: FAIL -- No Kapitza minima found at any tested frequency")

# ── Save ──
save_dict = {
    'tau': tau,
    'V_jensen': V_jensen,
    'dV': dV,
    'd2V': d2V,
    'omega_sq_scan': omega_sq_scan,
    'omega_in_all': omega_in_all,
    'omega_out_all': omega_out_all,
    'A_ref': A_ref,
    'm_tau': m_tau,
    'omega_sq_T3': omega_sq_T3,
    'omega_sq_T4': omega_sq_T4,
    'n_fixed_points': len(fixed_points),
    'verdict': verdict,
}

if fixed_points:
    fp_arr = np.array([(fp['omega_in_sq'], fp['omega_out_sq'], fp['tau_min'],
                        fp['d2V'], fp['ratio'], fp['ratio_sqrt'])
                       for fp in fixed_points])
    save_dict['fixed_points'] = fp_arr

np.savez('tier0-computation/s31Cg_selfconsistent_cranking.npz', **save_dict)
print("\nSaved: tier0-computation/s31Cg_selfconsistent_cranking.npz")

# ── Plot ──
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: omega_out vs omega_in
ax = axes[0, 0]
if len(omega_in_all) > 0:
    ax.scatter(omega_in_all, omega_out_all, c='steelblue', s=20, alpha=0.6, label='Computed')
    # Diagonal line
    diag = np.linspace(0, max(omega_in_all.max(), omega_out_all.max()) * 1.1, 100)
    ax.plot(diag, diag, 'k--', linewidth=1, label='Self-consistent (diagonal)')
    ax.fill_between(diag, 0.64 * diag, 1.44 * diag, alpha=0.1, color='green', label='20% tolerance')
    if fixed_points:
        fp_x = [fp['omega_in_sq'] for fp in fixed_points]
        fp_y = [fp['omega_out_sq'] for fp in fixed_points]
        ax.scatter(fp_x, fp_y, c='red', s=100, marker='*', zorder=5, label='Fixed points')
ax.axvspan(1, 8, alpha=0.05, color='orange', label='Target range [1,8]')
ax.set_xlabel('omega_in^2 (drive frequency squared)')
ax.set_ylabel('omega_out^2 (from d^2V_Kap/dtau^2 / m_tau)')
ax.set_title('N-31Cg: Self-Consistent Cranking')
ax.legend(fontsize=8)

# Panel 2: V_Kapitza profiles at selected frequencies
ax = axes[0, 1]
selected_omega_sq = [1.0, 3.0, 5.0, omega_sq_T3, omega_sq_T4]
colors_v = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
ax.plot(tau, V_jensen, 'k-', linewidth=2, label='V_Jensen (static)')
for j, osq in enumerate(selected_omega_sq):
    V_corr = A_ref**2 * dV**2 / (4.0 * osq)
    V_kap = V_jensen + V_corr
    # Normalize to show shape
    V_rel = V_kap - V_kap.min()
    ax.plot(tau, V_kap, color=colors_v[j], linewidth=1.2,
            label=f'omega^2={osq:.1f}')
ax.set_xlabel('tau')
ax.set_ylabel('V_Kapitza')
ax.set_title(f'V_Kapitza profiles (A={A_ref})')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.5)

# Panel 3: d^2V/dtau^2 of Jensen
ax = axes[1, 0]
ax.plot(tau, d2V, 'b-', linewidth=2)
ax.axhline(0, color='gray', linestyle='--')
ax.axhline(m_tau * omega_sq_T3, color='red', linestyle=':', label=f'm_tau * omega_T3^2 = {m_tau*omega_sq_T3:.1f}')
ax.set_xlabel('tau')
ax.set_ylabel("d^2V/dtau^2")
ax.set_title('Jensen potential curvature')
ax.legend()

# Panel 4: Summary
ax = axes[1, 1]
ax.axis('off')
summary_lines = [
    f"N-31Cg: Self-Consistent Cranking Check",
    f"",
    f"Drive: T3 mode, A = {A_ref}",
    f"Modulus mass: m_tau = {m_tau}",
    f"omega_sq_T3 = {omega_sq_T3:.4f}",
    f"omega_sq_T4 = {omega_sq_T4:.4f}",
    f"",
    f"Fixed points found: {len(fixed_points)}",
]
for fp in fixed_points:
    summary_lines.append(f"  omega^2={fp['omega_in_sq']:.3f}, tau={fp['tau_min']:.4f}, "
                        f"ratio={fp['ratio_sqrt']:.4f}")
summary_lines.extend([
    f"",
    f"GATE N-31Cg-G: {verdict}",
])
ax.text(0.1, 0.95, '\n'.join(summary_lines), transform=ax.transAxes,
        fontsize=10, verticalalignment='top', fontfamily='monospace')

plt.tight_layout()
plt.savefig('tier0-computation/s31Cg_selfconsistent_cranking.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s31Cg_selfconsistent_cranking.png")

print(f"\n=== COMPUTATION COMPLETE ===")
print(f"Gate N-31Cg-G: {verdict}")
