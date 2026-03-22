#!/usr/bin/env python3
"""
Session 22a QA-3: delta_T Decay Profile Fitting

Characterizes the decay profile of delta_T(tau) and tests whether the
decay rate is algebraically determined by the Dynkin indices.

delta_T decays from 3399 at tau=0 to 3.04 at tau=2.0. This computation:
1. Fits single and double exponentials
2. Tests Tesla's Bragg hypothesis (half-wavelength of e^{-4tau})
3. Tests algebraic determination of the decay rate (gamma vs Dynkin indices)
4. Analyzes the sign structure (singlet contribution)

Data: tier0-computation/s21c_cp1_investigation.npz

Author: quantum-acoustics-theorist
Date: 2026-02-20
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from pathlib import Path

data_dir = Path(__file__).parent

# ============================================================
# 1. LOAD DATA
# ============================================================

data = np.load(data_dir / 's21c_cp1_investigation.npz', allow_pickle=True)
tau = data['tau_values']
dT_total = data['delta_T_total']
dT_b1 = data['delta_T_b1']
dT_b2 = data['delta_T_b2']
dT_z3_0 = data['delta_T_z3_0']
dT_z3_1 = data['delta_T_z3_1']
dT_z3_2 = data['delta_T_z3_2']
S_b1 = data['S_b1']
S_b2 = data['S_b2']
S_signed = data['S_signed']

print("=" * 70)
print("SESSION 22a QA-3: delta_T DECAY PROFILE FITTING")
print("=" * 70)
print()

print("--- Raw Data ---")
print(f"{'tau':>6s} {'dT_total':>12s} {'dT_b1':>12s} {'dT_b2':>12s} {'dT_z3_0':>12s}")
for i in range(len(tau)):
    print(f"{tau[i]:6.2f} {dT_total[i]:12.4f} {dT_b1[i]:12.4f} {dT_b2[i]:12.4f} {dT_z3_0[i]:12.4f}")

# ============================================================
# 2. SINGLE EXPONENTIAL FIT
# ============================================================

print()
print("=" * 70)
print("2. SINGLE EXPONENTIAL FIT: dT = A * exp(-gamma * tau)")
print("=" * 70)

def single_exp(tau, A, gamma):
    return A * np.exp(-gamma * tau)

# Use all 21 points
popt_1, pcov_1 = curve_fit(single_exp, tau, dT_total, p0=[3400, 3.5])
A1, gamma1 = popt_1
perr_1 = np.sqrt(np.diag(pcov_1))
fit_1 = single_exp(tau, *popt_1)
rss_1 = np.sum((dT_total - fit_1)**2)
r2_1 = 1 - rss_1 / np.sum((dT_total - np.mean(dT_total))**2)

print(f"  A     = {A1:.4f} +/- {perr_1[0]:.4f}")
print(f"  gamma = {gamma1:.6f} +/- {perr_1[1]:.6f}")
print(f"  tau*  = 1/gamma = {1/gamma1:.4f}")
print(f"  R^2   = {r2_1:.8f}")
print(f"  RSS   = {rss_1:.4f}")

# ============================================================
# 3. DOUBLE EXPONENTIAL FIT
# ============================================================

print()
print("=" * 70)
print("3. DOUBLE EXPONENTIAL FIT: dT = A1*exp(-g1*tau) + A2*exp(-g2*tau)")
print("=" * 70)

def double_exp(tau, A1, g1, A2, g2):
    return A1 * np.exp(-g1 * tau) + A2 * np.exp(-g2 * tau)

try:
    popt_2, pcov_2 = curve_fit(double_exp, tau, dT_total,
                                p0=[2000, 5.0, 1400, 3.0],
                                bounds=([0, 0.1, 0, 0.1], [5000, 20, 5000, 20]),
                                maxfev=20000)
    A2a, g2a, A2b, g2b = popt_2
    perr_2 = np.sqrt(np.diag(pcov_2))
    fit_2 = double_exp(tau, *popt_2)
    rss_2 = np.sum((dT_total - fit_2)**2)
    r2_2 = 1 - rss_2 / np.sum((dT_total - np.mean(dT_total))**2)

    print(f"  A1    = {A2a:.4f} +/- {perr_2[0]:.4f}")
    print(f"  g1    = {g2a:.6f} +/- {perr_2[1]:.6f}")
    print(f"  A2    = {A2b:.4f} +/- {perr_2[2]:.4f}")
    print(f"  g2    = {g2b:.6f} +/- {perr_2[3]:.6f}")
    print(f"  R^2   = {r2_2:.8f}")
    print(f"  RSS   = {rss_2:.4f}")
    print(f"  RSS improvement over single: {(rss_1 - rss_2)/rss_1 * 100:.2f}%")
    double_fit_ok = True
except Exception as e:
    print(f"  Fit failed: {e}")
    double_fit_ok = False
    rss_2 = rss_1

# ============================================================
# 4. POWER-LAW * EXPONENTIAL FIT
# ============================================================

print()
print("=" * 70)
print("4. POWER-LAW * EXPONENTIAL: dT = A * (tau+eps)^(-alpha) * exp(-gamma*tau)")
print("=" * 70)

def power_exp(tau, A, alpha, gamma, eps):
    return A * (tau + eps)**(-alpha) * np.exp(-gamma * tau)

try:
    popt_pe, pcov_pe = curve_fit(power_exp, tau, dT_total,
                                  p0=[100, 0.5, 3.0, 0.01],
                                  bounds=([0, -2, 0.1, 0.001], [10000, 5, 20, 1]),
                                  maxfev=20000)
    A_pe, alpha_pe, gamma_pe, eps_pe = popt_pe
    perr_pe = np.sqrt(np.diag(pcov_pe))
    fit_pe = power_exp(tau, *popt_pe)
    rss_pe = np.sum((dT_total - fit_pe)**2)
    r2_pe = 1 - rss_pe / np.sum((dT_total - np.mean(dT_total))**2)

    print(f"  A     = {A_pe:.4f} +/- {perr_pe[0]:.4f}")
    print(f"  alpha = {alpha_pe:.6f} +/- {perr_pe[1]:.6f}")
    print(f"  gamma = {gamma_pe:.6f} +/- {perr_pe[2]:.6f}")
    print(f"  eps   = {eps_pe:.6f} +/- {perr_pe[3]:.6f}")
    print(f"  R^2   = {r2_pe:.8f}")
    print(f"  RSS   = {rss_pe:.4f}")
    print(f"  RSS improvement over single exp: {(rss_1 - rss_pe)/rss_1 * 100:.2f}%")
except Exception as e:
    print(f"  Fit failed: {e}")
    rss_pe = rss_1

# ============================================================
# 5. GAUGE-WEIGHTED COMPONENTS
# ============================================================

print()
print("=" * 70)
print("5. GAUGE-WEIGHTED COMPONENT ANALYSIS")
print("=" * 70)

# Fit single exponential to |dT_b1| and |dT_b2|
popt_b1, _ = curve_fit(single_exp, tau, np.abs(dT_b1), p0=[2700, 3.5])
popt_b2, _ = curve_fit(single_exp, tau, np.abs(dT_b2), p0=[6100, 3.5])

print(f"\n  |dT_b1| fit: A={popt_b1[0]:.2f}, gamma={popt_b1[1]:.6f}")
print(f"  |dT_b2| fit: A={popt_b2[0]:.2f}, gamma={popt_b2[1]:.6f}")
print(f"  Amplitude ratio A_b1/A_b2 = {popt_b1[0]/popt_b2[0]:.6f}")
print(f"  Expected from Trap 2: 4/9 = {4/9:.6f}")
print(f"  Match: {abs(popt_b1[0]/popt_b2[0] - 4/9) / (4/9) * 100:.4f}%")
print(f"  Decay rate ratio gamma_b1/gamma_b2 = {popt_b1[1]/popt_b2[1]:.6f}")
print(f"  Are they equal? {abs(popt_b1[1] - popt_b2[1]) / popt_b1[1] * 100:.2f}% difference")

# ============================================================
# 6. SIGN STRUCTURE ANALYSIS
# ============================================================

print()
print("=" * 70)
print("6. SIGN STRUCTURE AND SINGLET CONTRIBUTION")
print("=" * 70)

# delta_T_total = sum over all eigenvalues of (lambda^2 - T(tau))
# delta_T_b1 = sum weighted by b1 charge
# delta_T_b2 = sum weighted by b2 charge
# The singlet (0,0) has b1=0, b2=0, so it contributes to total but NOT to b1 or b2

# dT_total > 0 (all positive, decaying)
# dT_b1 < 0 (all negative, increasing in magnitude)
# dT_b2 < 0 (all negative, increasing in magnitude)

# The relation: dT_total is NOT a linear combination of dT_b1 and dT_b2
# because they use DIFFERENT weightings of the same eigenvalues

# Z3 analysis: total = z3_0 + z3_1 + z3_2
z3_sum = dT_z3_0 + dT_z3_1 + dT_z3_2
print("  Z3 sector analysis:")
print(f"  {'tau':>6s} {'z3_0':>12s} {'z3_1':>12s} {'z3_2':>12s} {'sum':>12s} {'total':>12s} {'diff':>12s}")
for i in range(len(tau)):
    print(f"  {tau[i]:6.2f} {dT_z3_0[i]:12.4f} {dT_z3_1[i]:12.4f} {dT_z3_2[i]:12.4f} "
          f"{z3_sum[i]:12.4f} {dT_total[i]:12.4f} {abs(z3_sum[i]-dT_total[i]):12.6f}")

# Z3 fractions
print()
print("  Z3 fractional contributions:")
print(f"  {'tau':>6s} {'f_0':>10s} {'f_1':>10s} {'f_2':>10s}")
for i in range(len(tau)):
    total = dT_total[i]
    print(f"  {tau[i]:6.2f} {dT_z3_0[i]/total:10.6f} {dT_z3_1[i]/total:10.6f} {dT_z3_2[i]/total:10.6f}")

# ============================================================
# 7. TESLA'S BRAGG HYPOTHESIS
# ============================================================

print()
print("=" * 70)
print("7. TESLA'S BRAGG HYPOTHESIS")
print("=" * 70)
print()

# The e^{-4tau} modulation period creates a bandgap in tau-space.
# Half-wavelength = pi/2 ~ 1.571
# Physical window width = 1.582 - 0.108 = 1.474
# (using exact crossing points from QA-1)

half_wavelength = np.pi / 2
window_width = 1.5816 - 0.1084
agreement = abs(half_wavelength - window_width) / half_wavelength * 100

print(f"  e^{{-4tau}} half-wavelength: pi/2 = {half_wavelength:.4f}")
print(f"  Physical window width: {window_width:.4f}")
print(f"  Agreement: {agreement:.2f}%")
print(f"  Tesla predicted ~11% agreement; actual = {agreement:.2f}%")
print()

# Does the decay rate gamma relate to 4 (from e^{-4tau})?
print(f"  Fitted gamma (single exp): {gamma1:.4f}")
print(f"  Expected from e^{{-4tau}}: 4.0000")
print(f"  Ratio gamma/4: {gamma1/4:.4f}")
print()

# The b1 and b2 decay rates
print(f"  gamma_b1: {popt_b1[1]:.4f}")
print(f"  gamma_b2: {popt_b2[1]:.4f}")
print(f"  gamma_b1/4: {popt_b1[1]/4:.4f}")
print(f"  gamma_b2/4: {popt_b2[1]/4:.4f}")

# ============================================================
# 8. ALGEBRAIC DETERMINATION TEST
# ============================================================

print()
print("=" * 70)
print("8. ALGEBRAIC DETERMINATION OF DECAY RATE")
print("=" * 70)
print()

# Dynkin embedding indices:
# b1 = 4 (from U(1)_Y embedding)
# b2 = 9 (from SU(2)_L embedding)
# The Jensen scaling: e^{2tau} for u(1), e^{-2tau} for su(2), e^{tau} for C^2
# The dominant exponential component is e^{-4tau} (from S_b1 and S_b2)

# Candidate algebraic values for gamma:
candidates = {
    '4 (exact e^{-4tau})': 4.0,
    '2*b1/b2': 2*4/9,
    'b1': 4.0,
    'b2/b1': 9/4,
    'sqrt(b1*b2)': np.sqrt(4*9),
    '(b1+b2)/2': (4+9)/2,
    'b1-b2/4': 4-9/4,
    '4*b1/b2': 4*4/9,
    '8/3 = 2*(b1+b2)/(b1*b2/gcd)': 8/3,
}

print(f"  Fitted gamma = {gamma1:.6f}")
print(f"  {'Candidate':>30s} {'Value':>10s} {'|gamma-val|/val':>15s}")
print("  " + "-" * 60)
for name, val in candidates.items():
    pct = abs(gamma1 - val) / val * 100
    marker = " <-- MATCH" if pct < 5 else ""
    print(f"  {name:>30s} {val:10.4f} {pct:14.2f}%{marker}")

# ============================================================
# 9. Constraint Gate (no explicit gate for QA-3; structural understanding)
# ============================================================

print()
print("=" * 70)
print("9. SUMMARY AND STRUCTURAL ASSESSMENT")
print("=" * 70)
print()

best_fit = "single exponential" if rss_1 <= rss_2 else "double exponential"
print(f"  Best fit: {best_fit}")
print(f"  Decay rate gamma = {gamma1:.4f} (characteristic scale tau* = {1/gamma1:.4f})")
print(f"  Amplitude ratio A_b1/A_b2 = {popt_b1[0]/popt_b2[0]:.6f} (expected 4/9 = 0.444444)")
print(f"  Z3 uniform to {max(abs(dT_z3_0/dT_total - 1/3).max(), abs(dT_z3_1/dT_total - 1/3).max())*100:.2f}%")
print(f"  Bragg half-wavelength vs window: {agreement:.1f}% agreement")
print(f"  gamma vs 4.0: {abs(gamma1-4)/4*100:.1f}% difference")

# ============================================================
# 10. SAVE AND PLOT
# ============================================================

# Plot
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 22a QA-3: delta_T Decay Profile', fontsize=14)

# (a) Log plot of delta_T with fits
ax = axes[0, 0]
ax.semilogy(tau, dT_total, 'ko', markersize=5, label='data')
tau_fine = np.linspace(0, 2, 200)
ax.semilogy(tau_fine, single_exp(tau_fine, *popt_1), 'b-', label=f'exp: gamma={gamma1:.3f}', alpha=0.7)
if double_fit_ok:
    ax.semilogy(tau_fine, double_exp(tau_fine, *popt_2), 'r--',
                label=f'double exp: g1={g2a:.2f}, g2={g2b:.2f}', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\delta_T(\tau)$')
ax.set_title('(a) delta_T Decay (log scale)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (b) Residuals of single exp fit
ax = axes[0, 1]
resid_1 = (dT_total - fit_1) / dT_total * 100
ax.plot(tau, resid_1, 'b-o', markersize=4)
ax.axhline(0, color='k', linestyle='-', alpha=0.3)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Residual (%)')
ax.set_title('(b) Single Exponential Residuals')
ax.grid(True, alpha=0.3)

# (c) Gauge-weighted components
ax = axes[1, 0]
ax.semilogy(tau, dT_total, 'k-o', markersize=4, label=r'$\delta T_{total}$')
ax.semilogy(tau, np.abs(dT_b1), 'b-s', markersize=4, label=r'$|\delta T_{b1}|$')
ax.semilogy(tau, np.abs(dT_b2), 'r-^', markersize=4, label=r'$|\delta T_{b2}|$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('|delta_T|')
ax.set_title('(c) Gauge-Weighted Components')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (d) Z3 fractions
ax = axes[1, 1]
ax.plot(tau, dT_z3_0/dT_total, 'b-o', markersize=4, label='Z3 class 0')
ax.plot(tau, dT_z3_1/dT_total, 'r-s', markersize=4, label='Z3 class 1')
ax.plot(tau, dT_z3_2/dT_total, 'g-^', markersize=4, label='Z3 class 2')
ax.axhline(1/3, color='k', linestyle='--', alpha=0.5, label='1/3')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Z3 fraction')
ax.set_title('(d) Z3 Sector Fractions')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim([0.32, 0.34])

plt.tight_layout()
plt.savefig(data_dir / 's22a_delta_T_profile.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved to {data_dir / 's22a_delta_T_profile.png'}")

# Save text output
with open(data_dir / 's22a_delta_T_profile.txt', 'w') as f:
    f.write("QA-3 RESULTS SUMMARY\n")
    f.write(f"gamma = {gamma1:.6f}, tau* = {1/gamma1:.4f}\n")
    f.write(f"A_b1/A_b2 = {popt_b1[0]/popt_b2[0]:.6f} (4/9 = {4/9:.6f})\n")
    f.write(f"Bragg agreement: {agreement:.1f}%\n")
    if double_fit_ok:
        f.write(f"Double exp: g1={g2a:.4f}, g2={g2b:.4f}\n")
        f.write(f"Double exp RSS improvement: {(rss_1-rss_2)/rss_1*100:.1f}%\n")

print("\nDone.")
