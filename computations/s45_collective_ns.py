"""
COLLECTIVE-NS-45: Collective Mode Phonon Pair Creation for n_s
Computes n_s from acoustic-optical phonon pair creation during transit.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ac = np.load('tier0-computation/s45_acoustic_ns.npz', allow_pickle=True)
bcs = np.load('tier0-computation/s38_cc_instanton.npz', allow_pickle=True)

Delta_0 = float(bcs['Delta_0'])
k_vals = ac['k_values']
n_k = len(k_vals)

omega_ac_pre  = ac['omega_acoustic_0.00']
omega_ac_post = ac['omega_acoustic_0.19']
omega_op_pre  = ac['omega_optical_0.00']
omega_op_post = ac['omega_optical_0.19']

print("=" * 70)
print("COLLECTIVE-NS-45: Phonon Pair Creation from Branch Structure")
print("=" * 70)

# Branch gap
gap_pre  = omega_op_pre - omega_ac_pre
gap_post = omega_op_post - omega_ac_post

print("\n--- Branch Gap (optical - acoustic) ---")
print(f"{'k':>8s} {'gap_pre':>10s} {'gap_post':>10s} {'delta':>10s}")
for i in range(n_k):
    print(f"{k_vals[i]:8.4f} {gap_pre[i]:10.6f} {gap_post[i]:10.6f} {gap_post[i]-gap_pre[i]:10.6f}")

# Bogoliubov coefficients
def bogol(w_in, w_out):
    return ((w_in - w_out) / (2 * np.sqrt(w_in * w_out)))**2

beta2_ac = bogol(omega_ac_pre, omega_ac_post)
beta2_op = bogol(omega_op_pre, omega_op_post)

mean_gap = (gap_pre + gap_post) / 2
delta_gap = gap_post - gap_pre
beta2_cross = np.where(mean_gap > 0, (delta_gap / (2 * mean_gap))**2, 0)

print("\n--- Bogoliubov Coefficients ---")
print(f"{'k':>8s} {'|b|2_ac':>12s} {'|b|2_op':>12s} {'|b|2_cross':>12s}")
for i in range(n_k):
    print(f"{k_vals[i]:8.4f} {beta2_ac[i]:12.6e} {beta2_op[i]:12.6e} {beta2_cross[i]:12.6e}")

# Power spectra
P_ac = beta2_ac
P_op = beta2_op
P_cross = beta2_cross
P_total = beta2_ac + beta2_op + beta2_cross

# Extract n_s from each channel
k_fit = k_vals[1:]

def extract_ns(P, label):
    P_fit = P[1:]
    valid = P_fit > 0
    if valid.sum() < 2:
        print(f"  {label}: insufficient points")
        return None
    lnk = np.log(k_fit[valid])
    lnP = np.log(P_fit[valid])
    coeffs = np.polyfit(lnk, lnP, 1)
    ns = coeffs[0] + 1
    pred = np.polyval(coeffs, lnk)
    ss_res = np.sum((lnP - pred)**2)
    ss_tot = np.sum((lnP - np.mean(lnP))**2)
    R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    print(f"  {label}: n_s = {ns:.4f}, R2 = {R2:.4f}")
    return ns, R2

print("\n--- Spectral Tilt ---")
res_ac = extract_ns(P_ac, "Acoustic")
res_op = extract_ns(P_op, "Optical")
res_cross = extract_ns(P_cross, "Cross-branch")
res_total = extract_ns(P_total, "Total")

# Band inversion analysis
print("\n--- Band Inversion at k=0 ---")
print(f"  tau=0.00: ac={omega_ac_pre[0]:.6f}, op={omega_op_pre[0]:.6f}, gap={gap_pre[0]:.6f}")
print(f"  tau=0.19: ac={omega_ac_post[0]:.6f}, op={omega_op_post[0]:.6f}, gap={gap_post[0]:.6f}")

# Adiabaticity
d_omega_ac = (omega_ac_post - omega_ac_pre) / 0.19
omega_mid_ac = (omega_ac_pre + omega_ac_post) / 2
Q_ac = np.abs(d_omega_ac) / omega_mid_ac**2

d_omega_op = (omega_op_post - omega_op_pre) / 0.19
omega_mid_op = (omega_op_pre + omega_op_post) / 2
Q_op = np.abs(d_omega_op) / omega_mid_op**2

print("\n--- Adiabaticity Q ---")
for i in range(n_k):
    print(f"  k={k_vals[i]:.4f}: Q_ac={Q_ac[i]:.4f}, Q_op={Q_op[i]:.4f}")

# GPV collective mode
omega_GPV = 1.430
Delta_pre = 0.826
print(f"\n--- GPV Collective Mode ---")
print(f"  omega_GPV = {omega_GPV:.3f} (S37)")
print(f"  omega_GPV/Delta_0 = {omega_GPV/Delta_0:.3f}")
print(f"  AB standard: sqrt(2/3) = {np.sqrt(2/3):.3f}")
print(f"  Ratio: {omega_GPV/Delta_0/np.sqrt(2/3):.2f}x standard")
print(f"  Post-transit: mode absorbed (condensate destroyed)")

# Gap ratio analysis
ratio_k = np.where(mean_gap > 0, delta_gap / mean_gap, 0)
print(f"\n--- Gap Change Ratio (tilt source) ---")
for i in range(n_k):
    print(f"  k={k_vals[i]:.4f}: delta_gap/mean_gap = {ratio_k[i]:.6f}")

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
if res_ac: print(f"  Acoustic:     n_s = {res_ac[0]:.4f} (R2 = {res_ac[1]:.4f})")
if res_op: print(f"  Optical:      n_s = {res_op[0]:.4f} (R2 = {res_op[1]:.4f})")
if res_cross: print(f"  Cross-branch: n_s = {res_cross[0]:.4f} (R2 = {res_cross[1]:.4f})")
if res_total: print(f"  Total:        n_s = {res_total[0]:.4f} (R2 = {res_total[1]:.4f})")

# Gate
print("\n--- GATE ---")
if res_cross:
    ns_val = res_cross[0]
    if 0.955 <= ns_val <= 0.975:
        verdict = "PASS"
    elif 0.80 <= ns_val <= 1.10:
        verdict = "INFO (extended window)"
    else:
        verdict = "outside extended window"
    print(f"  Cross-branch n_s = {ns_val:.4f}: {verdict}")

# Plot
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle("COLLECTIVE-NS-45: Phonon Pair Creation from Branch Structure", fontsize=14)

ax = axes[0, 0]
ax.plot(k_vals, omega_ac_pre, 'b-o', label='Acoustic (t=0)', ms=4)
ax.plot(k_vals, omega_ac_post, 'b--s', label='Acoustic (t=0.19)', ms=4)
ax.plot(k_vals, omega_op_pre, 'r-o', label='Optical (t=0)', ms=4)
ax.plot(k_vals, omega_op_post, 'r--s', label='Optical (t=0.19)', ms=4)
ax.set_xlabel('k (Casimir)')
ax.set_ylabel('omega (M_KK)')
ax.set_title('Branch Dispersion')
ax.legend(fontsize=7)

ax = axes[0, 1]
ax.plot(k_vals, gap_pre, 'g-o', label='Gap (t=0)', ms=5)
ax.plot(k_vals, gap_post, 'g--s', label='Gap (t=0.19)', ms=5)
ax.set_xlabel('k')
ax.set_ylabel('gap')
ax.set_title('Acoustic-Optical Gap')
ax.legend()

ax = axes[0, 2]
kp = k_vals[1:]
ax.semilogy(kp, beta2_ac[1:], 'b-o', label='acoustic', ms=5)
ax.semilogy(kp, beta2_op[1:], 'r-o', label='optical', ms=5)
v = beta2_cross[1:] > 0
if v.any():
    ax.semilogy(kp[v], beta2_cross[1:][v], 'g-o', label='cross', ms=5)
ax.set_xlabel('k')
ax.set_ylabel('|beta|^2')
ax.set_title('Pair Creation Rate')
ax.legend(fontsize=8)

ax = axes[1, 0]
for P, lab, c in [(P_ac, 'Ac', 'b'), (P_op, 'Op', 'r'), (P_cross, 'Cross', 'g'), (P_total, 'Tot', 'k')]:
    vv = (k_vals > 0) & (P > 0)
    if vv.sum() > 0:
        ax.loglog(k_vals[vv], P[vv], f'{c}-o', label=lab, ms=5)
ax.set_xlabel('k')
ax.set_ylabel('P(k)')
ax.set_title('Power Spectra')
ax.legend(fontsize=8)

ax = axes[1, 1]
if res_cross:
    P_f = P_cross[1:]
    vv = P_f > 0
    if vv.sum() >= 2:
        lnk = np.log(k_fit[vv])
        lnP = np.log(P_f[vv])
        co = np.polyfit(lnk, lnP, 1)
        ax.plot(lnk, lnP, 'go', ms=8, label='Data')
        ax.plot(lnk, np.polyval(co, lnk), 'k--', label=f'n_s-1 = {co[0]:.3f}')
        ax.set_xlabel('ln k')
        ax.set_ylabel('ln P_cross')
        ax.set_title(f'Cross-Branch: n_s = {co[0]+1:.4f}')
        ax.legend()

ax = axes[1, 2]
vg = mean_gap > 0
ax.plot(k_vals[vg], np.abs(ratio_k[vg]), 'mo-', ms=6)
ax.set_xlabel('k')
ax.set_ylabel('|delta_gap / mean_gap|')
ax.set_title('Gap Change Ratio')

plt.tight_layout()
plt.savefig('tier0-computation/s45_collective_ns.png', dpi=150)
print("\nPlot saved.")

# Save
np.savez('tier0-computation/s45_collective_ns.npz',
    k_values=k_vals,
    omega_ac_pre=omega_ac_pre, omega_ac_post=omega_ac_post,
    omega_op_pre=omega_op_pre, omega_op_post=omega_op_post,
    gap_pre=gap_pre, gap_post=gap_post,
    beta2_acoustic=beta2_ac, beta2_optical=beta2_op,
    beta2_cross=beta2_cross, P_total=P_total,
    ns_acoustic=res_ac[0] if res_ac else np.nan,
    ns_optical=res_op[0] if res_op else np.nan,
    ns_cross=res_cross[0] if res_cross else np.nan,
    ns_total=res_total[0] if res_total else np.nan,
    R2_cross=res_cross[1] if res_cross else np.nan,
    Q_ac=Q_ac, Q_op=Q_op, gap_ratio=ratio_k
)
print("Data saved.")
