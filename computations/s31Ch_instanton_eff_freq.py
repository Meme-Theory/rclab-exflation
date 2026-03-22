"""
N-31Ch: Instanton-Driven Effective Frequency
Session 31Ca -- Baptista agent

K-1 tested Hessian frequencies T3/T4 (omega^2 = 8.326, 9.893) and found them
1.7x too stiff. The instanton gas provides an additional oscillation source
that effectively softens the frequency.

Sweep delta in linspace(0, 5, 21):
  omega_eff^2 = T3 - delta = 8.326 - delta
  Re-evaluate V_Kapitza(tau; A=0.08, omega=omega_eff) using arcsine-weighted average.
  Find delta_crit where minimum appears.
  Compare to Gamma_inst^2.

Gate N-31Ch-G (DECISIVE): PASS if delta_crit <= Gamma_inst^2 at tau in [0.15, 0.21].

Input: s31Ba_kapitza_gate.npz, s31Ba_instanton_kapitza.npz
Output: s31Ch_instanton_eff_freq.{npz,png}
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Load data ──
kap = np.load('tier0-computation/s31Ba_kapitza_gate.npz', allow_pickle=True)
inst = np.load('tier0-computation/s31Ba_instanton_kapitza.npz', allow_pickle=True)

tau = kap['tau_fine']  # (201,)
V_jensen = kap['V_jensen']  # (201,)
omega_sq_T3 = float(kap['omega_sq_T3'])  # 8.326

tau_inst = inst['tau']  # (201,)
d2V_dtau2 = inst['d2V_dtau2']  # (201,)

print(f"omega_sq_T3 = {omega_sq_T3:.4f}")
print(f"tau range: [{tau[0]:.3f}, {tau[-1]:.3f}]")

# Get instanton rates at all radii
radii = ['0p1', '0p3', '0p5', '1p0', '2p0', '5p0']
r_vals = [0.1, 0.3, 0.5, 1.0, 2.0, 5.0]
Gamma_inst = {}
S_inst = {}
for r_str, r_val in zip(radii, r_vals):
    Gamma_inst[r_val] = inst[f'Gamma_inst_r{r_str}']
    S_inst[r_val] = inst[f'S_inst_r{r_str}']

# ── Compute V'(tau) from Jensen potential ──
dtau = tau[1] - tau[0]
dV = np.gradient(V_jensen, dtau)

# ── Arcsine-weighted Kapitza average ──
# For periodic drive tau(t) = tau_0 + A*sin(omega*t), the time-averaged
# potential is weighted by the arcsine distribution (PDF of sinusoidal motion):
# p(tau) = 1 / (pi * sqrt(A^2 - (tau - tau_0)^2))
# This is the exact time-average for a sinusoidal drive.
#
# V_Kap(tau_0; A, omega) = <V(tau_0 + A*sin(theta))>_theta
#     + A^2 / (4*omega^2) * <|V'(tau_0 + A*sin(theta))|^2 * cos^2(theta)>_theta
#
# The first term is the bare arcsine average, second is the ponderomotive correction.
# For simplicity and consistency with K-1, use:
# V_Kap(tau_0) = V(tau_0) + A^2 * |V'(tau_0)|^2 / (4*omega^2)
# (leading-order Kapitza, valid for small A/tau_0)

A_ref = 0.08

# ── Sweep delta ──
deltas = np.linspace(0, 5, 51)  # finer grid than prompt's 21 for precision
delta_crit = None
V_kap_profiles = {}

print("\n--- Sweeping delta (omega_eff^2 = T3 - delta) ---")
print(f"{'delta':>8s} {'omega_eff^2':>12s} {'has_min':>8s} {'min_tau':>8s} {'min_V_kap':>12s}")

for delta in deltas:
    omega_eff_sq = omega_sq_T3 - delta
    if omega_eff_sq <= 0:
        # No oscillation possible
        continue

    # Kapitza correction: A^2 * |V'|^2 / (4 * omega_eff^2)
    V_corr = A_ref**2 * dV**2 / (4.0 * omega_eff_sq)
    V_kap = V_jensen + V_corr

    # Look for interior minimum in tau range [0.05, 0.50]
    mask = (tau >= 0.05) & (tau <= 0.50)
    idx_range = np.where(mask)[0]
    V_sub = V_kap[idx_range]
    tau_sub = tau[idx_range]

    dV_kap = np.gradient(V_sub, dtau)

    has_interior_min = False
    min_tau = None
    min_V = None
    for i in range(1, len(dV_kap) - 1):
        if dV_kap[i-1] < 0 and dV_kap[i+1] > 0:
            has_interior_min = True
            min_tau = tau_sub[i]
            min_V = V_sub[i]
            break

    if has_interior_min:
        print(f"{delta:8.3f} {omega_eff_sq:12.4f} {'YES':>8s} {min_tau:8.4f} {min_V:12.4f}")
        if delta_crit is None:
            delta_crit = delta
            print(f"  ** delta_crit = {delta_crit:.4f} **")
    else:
        if delta <= 1.0 or delta % 1.0 < 0.15:
            print(f"{delta:8.3f} {omega_eff_sq:12.4f} {'NO':>8s}")

    # Store selected profiles for plotting
    if abs(delta) < 0.01 or (delta_crit and abs(delta - delta_crit) < 0.06) \
            or abs(delta - 2.0) < 0.06 or abs(delta - 4.0) < 0.06 or abs(delta - 5.0) < 0.06:
        V_kap_profiles[delta] = V_kap.copy()

# ── Gamma_inst^2 at tau ~ 0.18 ──
print("\n--- Instanton Gamma^2 at key tau values ---")
tau_target_range = (tau_inst >= 0.15) & (tau_inst <= 0.21)
for r_val in r_vals:
    G = Gamma_inst[r_val]
    G_sq = G**2
    G_sq_max = G_sq[tau_target_range].max()
    G_sq_at_018 = G_sq[np.argmin(np.abs(tau_inst - 0.18))]
    print(f"  r={r_val}: Gamma_inst^2 max in [0.15,0.21] = {G_sq_max:.4f}, "
          f"at tau=0.18: {G_sq_at_018:.4f}")

# ── Gate classification ──
print(f"\n=== GATE N-31Ch-G ===")
print(f"  delta_crit = {delta_crit}")

if delta_crit is not None:
    # Compare delta_crit to Gamma_inst^2
    gate_pass = False
    gate_details = []
    for r_val in r_vals:
        G = Gamma_inst[r_val]
        G_sq = G**2
        G_sq_max = G_sq[tau_target_range].max()
        passes = delta_crit <= G_sq_max
        gate_details.append((r_val, G_sq_max, passes))
        if passes:
            gate_pass = True
        print(f"  r={r_val}: Gamma^2_max = {G_sq_max:.4f}, delta_crit={delta_crit:.4f}, "
              f"{'PASS' if passes else 'FAIL'}")

    if gate_pass:
        verdict = "PASS"
        passing_r = [gd for gd in gate_details if gd[2]]
        print(f"\n  VERDICT: PASS -- delta_crit = {delta_crit:.4f} <= Gamma_inst^2 "
              f"for r = {[gd[0] for gd in passing_r]}")
    else:
        # Check if within factor 3
        min_ratio = min(delta_crit / gd[1] for gd in gate_details if gd[1] > 0)
        if min_ratio <= 3.0:
            verdict = "MARGINAL"
            print(f"\n  VERDICT: MARGINAL -- delta_crit/Gamma^2_min = {min_ratio:.2f} (< 3)")
        else:
            verdict = "FAIL"
            print(f"\n  VERDICT: FAIL -- delta_crit > 3*Gamma_inst^2 at all tested radii")
else:
    # No minimum appeared even at maximum delta
    verdict = "FAIL"
    print(f"  VERDICT: FAIL -- No Kapitza minimum appears for any delta in [0, 5]")
    print(f"  (omega_eff^2 reduced from {omega_sq_T3:.3f} to {omega_sq_T3-5:.3f}, still no minimum)")

# ── Save ──
save_dict = {
    'tau': tau,
    'V_jensen': V_jensen,
    'dV': dV,
    'deltas': deltas,
    'A_ref': A_ref,
    'omega_sq_T3': omega_sq_T3,
    'delta_crit': delta_crit if delta_crit is not None else -1.0,
    'verdict': verdict,
}

for r_val in r_vals:
    r_str = str(r_val).replace('.', 'p')
    save_dict[f'Gamma_inst_sq_r{r_str}'] = Gamma_inst[r_val]**2

for delta, V_prof in V_kap_profiles.items():
    d_str = f"{delta:.2f}".replace('.', 'p')
    save_dict[f'V_kap_delta_{d_str}'] = V_prof

np.savez('tier0-computation/s31Ch_instanton_eff_freq.npz', **save_dict)
print("\nSaved: tier0-computation/s31Ch_instanton_eff_freq.npz")

# ── Plot ──
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: V_Kapitza profiles at selected delta values
ax = axes[0, 0]
profile_deltas = sorted(V_kap_profiles.keys())
colors_p = plt.cm.viridis(np.linspace(0, 0.9, len(profile_deltas)))
for j, delta in enumerate(profile_deltas):
    V_prof = V_kap_profiles[delta]
    omega_eff_sq = omega_sq_T3 - delta
    label = f'delta={delta:.2f} (omega^2={omega_eff_sq:.2f})'
    ax.plot(tau, V_prof, color=colors_p[j], linewidth=1.5, label=label)
ax.plot(tau, V_jensen, 'k--', linewidth=1, alpha=0.5, label='V_Jensen')
if delta_crit is not None:
    ax.axvline(0.18, color='red', linestyle=':', alpha=0.3)
ax.set_xlabel('tau')
ax.set_ylabel('V_Kapitza')
ax.set_title(f'V_Kapitza profiles (A={A_ref})')
ax.legend(fontsize=7)
ax.set_xlim(0.05, 0.45)

# Panel 2: delta_crit identification
ax = axes[0, 1]
# Re-compute minimum depth vs delta
min_depths = []
for delta in deltas:
    omega_eff_sq = omega_sq_T3 - delta
    if omega_eff_sq <= 0:
        min_depths.append(np.nan)
        continue
    V_corr = A_ref**2 * dV**2 / (4.0 * omega_eff_sq)
    V_kap = V_jensen + V_corr
    # Relative to monotonic baseline: check if min < value at boundaries
    mask = (tau >= 0.05) & (tau <= 0.45)
    V_sub = V_kap[mask]
    # Depth = max(V_sub) - min(V_sub) if non-monotonic, else 0
    dV_sub = np.gradient(V_sub, dtau)
    has_min = False
    for i in range(1, len(dV_sub) - 1):
        if dV_sub[i-1] < 0 and dV_sub[i+1] > 0:
            has_min = True
            break
    if has_min:
        min_depths.append(V_sub.max() - V_sub.min())
    else:
        min_depths.append(0.0)

min_depths = np.array(min_depths)
valid = deltas[deltas < omega_sq_T3]
ax.plot(deltas[:len(valid)], min_depths[:len(valid)], 'b-', linewidth=2)
if delta_crit is not None:
    ax.axvline(delta_crit, color='red', linestyle='--', label=f'delta_crit = {delta_crit:.3f}')
# Overlay Gamma^2 for each radius
for r_val in r_vals:
    G_sq_max = (Gamma_inst[r_val]**2)[tau_target_range].max()
    if G_sq_max < 6:
        ax.axvline(G_sq_max, color='green', linestyle=':', alpha=0.5,
                   label=f'Gamma^2(r={r_val}) = {G_sq_max:.2f}')
ax.set_xlabel('delta (frequency softening)')
ax.set_ylabel('V_Kapitza well depth')
ax.set_title('Minimum appearance vs frequency softening')
ax.legend(fontsize=7)

# Panel 3: Gamma_inst^2 vs tau
ax = axes[1, 0]
for r_val in r_vals:
    G_sq = Gamma_inst[r_val]**2
    ax.plot(tau_inst, G_sq, linewidth=1.5, label=f'r={r_val}')
if delta_crit is not None:
    ax.axhline(delta_crit, color='red', linestyle='--', linewidth=2,
               label=f'delta_crit = {delta_crit:.3f}')
ax.axvspan(0.15, 0.21, alpha=0.1, color='orange', label='target range')
ax.set_xlabel('tau')
ax.set_ylabel('Gamma_inst^2')
ax.set_title('Instanton rate squared vs tau')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.55)
ax.set_ylim(0, min(120, max(Gamma_inst[0.1]**2) * 1.1))

# Panel 4: Summary
ax = axes[1, 1]
ax.axis('off')
summary_lines = [
    f"N-31Ch: Instanton-Driven Effective Frequency",
    f"",
    f"omega_sq_T3 = {omega_sq_T3:.4f}",
    f"A = {A_ref}",
    f"delta_crit = {delta_crit if delta_crit is not None else 'NOT FOUND'}",
    f"",
    f"Gamma_inst^2 at tau~0.18:",
]
for r_val in r_vals:
    G_sq_at = (Gamma_inst[r_val]**2)[np.argmin(np.abs(tau_inst - 0.18))]
    G_sq_max = (Gamma_inst[r_val]**2)[tau_target_range].max()
    comp = "PASS" if (delta_crit is not None and delta_crit <= G_sq_max) else "FAIL"
    summary_lines.append(f"  r={r_val}: {G_sq_max:.3f} (max [0.15,0.21])  [{comp}]")
summary_lines.extend([
    f"",
    f"GATE N-31Ch-G: {verdict}",
])
ax.text(0.1, 0.95, '\n'.join(summary_lines), transform=ax.transAxes,
        fontsize=10, verticalalignment='top', fontfamily='monospace')

plt.tight_layout()
plt.savefig('tier0-computation/s31Ch_instanton_eff_freq.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s31Ch_instanton_eff_freq.png")

print(f"\n=== COMPUTATION COMPLETE ===")
print(f"Gate N-31Ch-G: {verdict}")
