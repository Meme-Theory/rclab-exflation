"""
N-31Ci: Bayesian Three-Fold Convergence Quantification (CORRECTED)
===================================================================
Three observables converge at tau ~ 0.18:
  1. phi_30 ~ 1.532 (golden ratio phi)
  2. sin^2_tw ~ 0.42 (spectral extraction target)
  3. Gamma_inst/omega_tau ratio peak at tau ~ 0.181

CORRECTION: The "instanton peak at 0.181" refers to the RATIO
Gamma_inst/omega_tau, NOT Gamma_inst alone. Gamma_inst is monotonic.
The ratio peaks because omega_tau (Hessian frequency) has a minimum
at the gradient-balance point.

Gate N-31Ci-G: INFORMATIVE if BF > 10.

Input: s30b_grid_bcs.npz, s30b_sdw_grid.npz, s31Ba_instanton_kapitza.npz
Output: s31Ci_bayesian_convergence.{npz,png}
"""

import numpy as np
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, time

t0 = time.time()

data_dir = os.path.dirname(__file__)

# --- Load data ---
grid_data = np.load(os.path.join(data_dir, 's30b_grid_bcs.npz'), allow_pickle=True)
sdw_data = np.load(os.path.join(data_dir, 's30b_sdw_grid.npz'), allow_pickle=True)
inst_data = np.load(os.path.join(data_dir, 's31Ba_instanton_kapitza.npz'), allow_pickle=True)

# Grid data: Jensen curve (eps=0 slice)
tau_grid = grid_data['tau']  # (21,)
eps_grid = grid_data['eps']  # (21,)
i_eps0 = np.argmin(np.abs(eps_grid))

phi_30_jensen = grid_data['phi_30'][:, i_eps0]
sin2_jensen = grid_data['sin2_tw'][:, i_eps0]

# Instanton data
tau_inst = inst_data['tau']  # (201,)
# Use RATIO (Gamma_inst/omega_tau), not raw Gamma_inst
# ratio_r1p0 is the ratio at coupling r=1.0
ratio_r1p0 = inst_data['ratio_r1p0']
Gamma_r1p0 = inst_data['Gamma_inst_r1p0']

print(f"tau_grid: {tau_grid[0]:.3f} to {tau_grid[-1]:.3f}, {len(tau_grid)} points")
print(f"tau_inst: {tau_inst[0]:.3f} to {tau_inst[-1]:.3f}, {len(tau_inst)} points")

# Verify ratio peak
ratio_peak_idx = np.argmax(ratio_r1p0)
ratio_peak_tau = tau_inst[ratio_peak_idx]
print(f"Ratio peak: tau={ratio_peak_tau:.4f}, ratio={ratio_r1p0[ratio_peak_idx]:.4f}")
print(f"Gamma peak: tau={tau_inst[np.argmax(Gamma_r1p0)]:.4f} (monotonic, NOT the convergence observable)")

# --- Define targets ---
phi_target = 1.532
sin2_target_spectral = 0.42
tau_ratio_target = 0.181  # ratio peak

print(f"\nTargets: phi_30={phi_target}, sin2_tw(spec)={sin2_target_spectral}, ratio_peak={tau_ratio_target}")

# --- Observable values at targets ---
phi_residual = np.abs(phi_30_jensen - phi_target)
best_phi_tau = tau_grid[np.argmin(phi_residual)]
print(f"phi_30: closest to target at tau={best_phi_tau:.3f}, residual={phi_residual.min():.6f}")
print(f"phi_30 range: {phi_30_jensen.min():.4f} to {phi_30_jensen.max():.4f}")

sin2_residual = np.abs(sin2_jensen - sin2_target_spectral)
best_sin2_tau = tau_grid[np.argmin(sin2_residual)]
print(f"sin2_tw: closest to target at tau={best_sin2_tau:.3f}, residual={sin2_residual.min():.6f}")
print(f"sin2_tw range: {sin2_jensen.min():.4f} to {sin2_jensen.max():.4f}")

# --- Interpolate to common fine grid ---
tau_lo = max(tau_grid[0], tau_inst[0])
tau_hi = min(tau_grid[-1], tau_inst[-1])
tau_fine = np.linspace(tau_lo, tau_hi, 500)

phi_interp = interp1d(tau_grid, phi_30_jensen, kind='cubic', fill_value='extrapolate')
sin2_interp = interp1d(tau_grid, sin2_jensen, kind='cubic', fill_value='extrapolate')
ratio_interp = interp1d(tau_inst, ratio_r1p0, kind='cubic', fill_value='extrapolate')

phi_fine = phi_interp(tau_fine)
sin2_fine = sin2_interp(tau_fine)
ratio_fine = ratio_interp(tau_fine)

# --- Proximity functions ---
sigma_phi = np.std(phi_fine) * 0.5
phi_prox = np.exp(-(phi_fine - phi_target)**2 / (2 * sigma_phi**2))

sigma_sin2 = np.std(sin2_fine) * 0.5
sin2_prox = np.exp(-(sin2_fine - sin2_target_spectral)**2 / (2 * sigma_sin2**2))

# Ratio proximity: normalized to peak
ratio_max = np.max(ratio_fine)
ratio_prox = ratio_fine / ratio_max if ratio_max > 0 else np.ones_like(ratio_fine)

# Combined
combined_prox = phi_prox * sin2_prox * ratio_prox

peak_idx = np.argmax(combined_prox)
peak_tau = tau_fine[peak_idx]
peak_value = combined_prox[peak_idx]

print(f"\n=== THREE-FOLD CONVERGENCE (CORRECTED) ===")
print(f"Peak combined proximity at tau = {peak_tau:.4f}")
print(f"  phi_prox = {phi_prox[peak_idx]:.6f}")
print(f"  sin2_prox = {sin2_prox[peak_idx]:.6f}")
print(f"  ratio_prox = {ratio_prox[peak_idx]:.6f}")
print(f"  combined = {peak_value:.6f}")

# --- Bayes factor ---
tau_range = tau_fine[-1] - tau_fine[0]
dtau = tau_fine[1] - tau_fine[0]

eff_width_phi = np.sum(phi_prox) * dtau / tau_range
eff_width_sin2 = np.sum(sin2_prox) * dtau / tau_range
eff_width_ratio = np.sum(ratio_prox) * dtau / tau_range

print(f"\nEffective widths (fraction of tau range):")
print(f"  phi: {eff_width_phi:.4f}")
print(f"  sin2: {eff_width_sin2:.4f}")
print(f"  ratio: {eff_width_ratio:.4f}")

p_null = eff_width_phi * eff_width_sin2 * eff_width_ratio
p_signal = np.sum(combined_prox) * dtau / tau_range

BF_integral = p_signal / p_null if p_null > 0 else np.inf
BF_simple = peak_value / p_null if p_null > 0 else np.inf

half_max = peak_value / 2
above_half = combined_prox > half_max
if np.any(above_half):
    fwhm_idx = np.where(above_half)[0]
    fwhm = (fwhm_idx[-1] - fwhm_idx[0]) * dtau
else:
    fwhm = dtau

print(f"\n=== BAYES FACTOR (CORRECTED) ===")
print(f"BF (simple, peak/product): {BF_simple:.2f}")
print(f"BF (integral): {BF_integral:.2f}")
print(f"FWHM of combined peak: {fwhm:.4f}")
print(f"p_null (product of widths): {p_null:.6e}")
print(f"p_signal (integral of combined): {p_signal:.6e}")

# --- Sensitivity ---
print(f"\n=== SENSITIVITY TO SIGMA CHOICE ===")
BF_sensitivity = {}
for sigma_mult in [0.25, 0.5, 1.0, 2.0]:
    sp = np.std(phi_fine) * sigma_mult
    ss = np.std(sin2_fine) * sigma_mult
    pp = np.exp(-(phi_fine - phi_target)**2 / (2*sp**2))
    ps = np.exp(-(sin2_fine - sin2_target_spectral)**2 / (2*ss**2))
    comb = pp * ps * ratio_prox
    ew_p = np.sum(pp) * dtau / tau_range
    ew_s = np.sum(ps) * dtau / tau_range
    ew_r = eff_width_ratio
    p_n = ew_p * ew_s * ew_r
    p_s = np.sum(comb) * dtau / tau_range
    bf = p_s / p_n if p_n > 0 else np.inf
    BF_sensitivity[sigma_mult] = bf
    print(f"  sigma_mult={sigma_mult}: BF={bf:.2f}")

# --- Compare wrong (Gamma) vs correct (ratio) ---
gamma_interp_fn = interp1d(tau_inst, Gamma_r1p0 / np.max(Gamma_r1p0), kind='cubic', fill_value='extrapolate')
gamma_wrong_fine = np.clip(gamma_interp_fn(tau_fine), 0, 1)
comb_wrong = phi_prox * sin2_prox * gamma_wrong_fine
ew_gw = np.sum(gamma_wrong_fine) * dtau / tau_range
p_null_wrong = eff_width_phi * eff_width_sin2 * ew_gw
p_sig_wrong = np.sum(comb_wrong) * dtau / tau_range
BF_wrong = p_sig_wrong / p_null_wrong if p_null_wrong > 0 else 0
print(f"\n  Using raw Gamma_inst (WRONG): BF = {BF_wrong:.2f}")
print(f"  Using ratio Gamma/omega (CORRECT): BF = {BF_integral:.2f}")

# --- Gate verdict ---
if BF_integral > 100:
    gate_verdict = "DECISIVE (BF > 100)"
elif BF_integral > 10:
    gate_verdict = "INFORMATIVE (BF > 10)"
elif BF_integral > 3:
    gate_verdict = "WEAK SIGNAL (3 < BF < 10)"
else:
    gate_verdict = "NO SIGNAL (BF < 3)"

print(f"\n=== GATE N-31Ci-G ===")
print(f"BF (integral) = {BF_integral:.2f}")
print(f"Gate verdict: N-31Ci-G = {gate_verdict}")

# --- Save ---
save_dict = {
    'tau_fine': tau_fine,
    'tau_grid': tau_grid,
    'phi_30_jensen': phi_30_jensen,
    'sin2_jensen': sin2_jensen,
    'phi_fine': phi_fine,
    'sin2_fine': sin2_fine,
    'ratio_fine': ratio_fine,
    'phi_prox': phi_prox,
    'sin2_prox': sin2_prox,
    'ratio_prox': ratio_prox,
    'combined_prox': combined_prox,
    'peak_tau': np.array(peak_tau),
    'peak_value': np.array(peak_value),
    'BF_simple': np.array(BF_simple),
    'BF_integral': np.array(BF_integral),
    'fwhm': np.array(fwhm),
    'eff_width_phi': np.array(eff_width_phi),
    'eff_width_sin2': np.array(eff_width_sin2),
    'eff_width_ratio': np.array(eff_width_ratio),
    'gate_verdict': np.array(gate_verdict),
    'BF_sensitivity_sigmas': np.array(list(BF_sensitivity.keys())),
    'BF_sensitivity_values': np.array(list(BF_sensitivity.values())),
    'ratio_peak_tau': np.array(ratio_peak_tau),
    'correction_note': np.array('CORRECTED: uses ratio Gamma/omega not raw Gamma'),
}
np.savez(os.path.join(data_dir, 's31Ci_bayesian_convergence.npz'), **save_dict)
print(f"\nSaved s31Ci_bayesian_convergence.npz")

# --- Plot ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Three observables vs tau
ax = axes[0, 0]
ax2 = ax.twinx()
ax.plot(tau_fine, phi_fine, 'b-', label=f'phi_30 (target={phi_target})')
ax.axhline(phi_target, color='b', linestyle=':', alpha=0.3)
ax2.plot(tau_fine, sin2_fine, 'r-', label=f'sin2_tw (target={sin2_target_spectral})')
ax2.axhline(sin2_target_spectral, color='r', linestyle=':', alpha=0.3)
ax.set_xlabel('tau')
ax.set_ylabel('phi_30', color='b')
ax2.set_ylabel('sin2_tw', color='r')
ax.set_title('Observables vs tau')
ax.axvline(peak_tau, color='green', linestyle='--', alpha=0.5, label=f'peak={peak_tau:.3f}')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8)

# Panel 2: Proximity functions (CORRECTED)
ax = axes[0, 1]
ax.plot(tau_fine, phi_prox, 'b-', label='phi proximity')
ax.plot(tau_fine, sin2_prox, 'r-', label='sin2 proximity')
ax.plot(tau_fine, ratio_prox, 'g-', label='ratio Gamma/omega proximity')
ax.plot(tau_fine, combined_prox, 'k-', linewidth=2, label='combined')
ax.axvline(peak_tau, color='k', linestyle='--', alpha=0.5)
ax.axvline(ratio_peak_tau, color='green', linestyle=':', alpha=0.5, label=f'ratio peak={ratio_peak_tau:.3f}')
ax.set_xlabel('tau')
ax.set_ylabel('Proximity (0-1)')
ax.set_title(f'Three-fold convergence (BF={BF_integral:.1f})')
ax.legend(fontsize=7)

# Panel 3: BF sensitivity
ax = axes[1, 0]
sigmas = list(BF_sensitivity.keys())
bfs = list(BF_sensitivity.values())
ax.bar(range(len(sigmas)), bfs, tick_label=[f'{s:.2f}' for s in sigmas], color='steelblue')
ax.axhline(10, color='green', linestyle='--', label='BF=10 threshold')
ax.axhline(3, color='orange', linestyle='--', label='BF=3 weak signal')
ax.set_xlabel('sigma multiplier')
ax.set_ylabel('Bayes Factor')
ax.set_title('BF sensitivity to sigma choice')
ax.legend()
if max(bfs) > 10:
    ax.set_yscale('log')

# Panel 4: Ratio profile showing peak at 0.181
ax = axes[1, 1]
ax.plot(tau_fine, ratio_fine, 'g-', linewidth=2, label='Gamma_inst / omega_tau')
ax.axvline(ratio_peak_tau, color='k', linestyle='--', alpha=0.5, label=f'peak={ratio_peak_tau:.3f}')
gamma_norm = np.clip(gamma_interp_fn(tau_fine), 0, None)
ax.plot(tau_fine, gamma_norm * ratio_max, 'g--', alpha=0.4, label='Gamma_inst (scaled)')
ax.set_xlabel('tau')
ax.set_ylabel('Gamma_inst / omega_tau')
ax.set_title('Instanton ratio (CORRECT observable)')
ax.legend()

fig.suptitle(f'N-31Ci: Bayesian Three-Fold Convergence (CORRECTED) | Gate: {gate_verdict}',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's31Ci_bayesian_convergence.png'), dpi=150, bbox_inches='tight')
print(f"Saved s31Ci_bayesian_convergence.png")

elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.2f}s")
