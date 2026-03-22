#!/usr/bin/env python3
"""
Session 33a Step 4: RGE Gate -- g1/g2 running from M_KK to M_Z.

Run the bare gauge coupling ratio g_1/g_2 = 0.684 from the compactification
scale M_KK ~ 10^16 GeV to M_Z = 91.1876 GeV using SM one-loop (and two-loop)
beta functions.

Mathematical background:
    The structural identity g_1/g_2 = e^{-2*tau} (Session 17a B-1) with
    tau_dump = 0.190 gives g_1/g_2 = e^{-0.380} = 0.6839 at the
    compactification scale M_KK.

    With GUT normalization (g_1 = sqrt(5/3) * g'), the SM one-loop RGE is:
        1/alpha_i(mu) = 1/alpha_i(M_KK) + b_i/(2*pi) * ln(M_KK/mu)
    where alpha_i = g_i^2/(4*pi) and:
        b_1 = 41/10, b_2 = -19/6, b_3 = -7

    PDG measured values at M_Z:
        sin^2(theta_W) = 0.23122 +/- 0.00003
        alpha_em^{-1} = 127.951 +/- 0.009
        alpha_s = 0.1180 +/- 0.0009

    Gate RGE-33a:
        PASS: g_1(M_Z)/g_2(M_Z) within 10% of 0.710
        SOFT PASS: within 5%
        FAIL: > 10% deviation

Author: sim (phonon-exflation-sim)
Date: 2026-03-06
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────
# 1. Constants and parameters
# ─────────────────────────────────────────────────────────────

# Masses
M_Z = 91.1876  # GeV
M_KK = 1e16    # GeV (compactification scale)

# SM one-loop beta function coefficients (GUT normalization for U(1))
b1 = 41.0 / 10.0   # U(1)_Y, GUT normalized
b2 = -19.0 / 6.0   # SU(2)_L
b3 = -7.0           # SU(3)_C

# Two-loop coefficients (SM, GUT normalized)
# b_ij: 2-loop contributions: d(alpha_i^{-1})/d(ln mu) = -b_i/(2pi) - sum_j b_ij*alpha_j/(8pi^2)
b11 = 199.0 / 50.0
b12 = 27.0 / 10.0
b13 = 44.0 / 5.0
b21 = 9.0 / 10.0
b22 = 35.0 / 6.0
b23 = 12.0
b31 = 11.0 / 10.0
b32 = 9.0 / 2.0
b33 = -26.0

# Framework input at M_KK
tau_dump = 0.190
g1_over_g2_KK = np.exp(-2 * tau_dump)  # structural identity B-1
print(f"Framework structural identity: g1/g2 = e^{{-2*tau}} = e^{{-{2*tau_dump:.3f}}} = {g1_over_g2_KK:.6f}")

# PDG measured values at M_Z
sin2_W_pdg = 0.23122
alpha_em_inv_pdg = 127.951
alpha_s_pdg = 0.1180

# Derived PDG quantities
# sin^2(theta_W) = g'^2/(g^2+g'^2) = g_1^2/(g_1^2*(5/3) + g_2^2)...
# With GUT normalization: sin^2(theta_W) = (3/5)*alpha_1 / ((3/5)*alpha_1 + alpha_2)
# At M_Z: sin^2 = alpha' / (alpha' + alpha_2) where alpha' = (3/5)*alpha_1_GUT
# Standard: sin^2 = g'^2/(g^2+g'^2), g' = g_1*sqrt(3/5)
# g_1/g_2 = (g'/sqrt(3/5)) / g_2 = (g'/g_2) * sqrt(5/3)
# tan(theta_W) = g'/g_2 = sin(theta_W)/cos(theta_W)
# sin^2 = 0.23122 => sin = 0.4808, cos = 0.8769, tan = 0.5484
# g'/g_2 = tan(theta_W) = 0.5484 (standard normalization)
# g_1_GUT/g_2 = tan(theta_W) * sqrt(5/3) = 0.5484 * 1.2910 = 0.7080
g1_over_g2_MZ_pdg = np.sqrt(sin2_W_pdg / (1 - sin2_W_pdg)) * np.sqrt(5.0/3.0)
print(f"PDG target: g1/g2(M_Z) = sqrt(sin2/(1-sin2)) * sqrt(5/3) = {g1_over_g2_MZ_pdg:.6f}")

# ─────────────────────────────────────────────────────────────
# 2. One-loop RGE solution
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("ONE-LOOP RGE")
print(f"{'=' * 70}")

# We need alpha_1(M_KK) and alpha_2(M_KK) individually, not just their ratio.
# The ratio g_1/g_2 = 0.684 gives alpha_1/alpha_2 = (g_1/g_2)^2 = 0.468
# But we need an absolute normalization.

# Approach: parameterize by alpha_2(M_KK) = alpha_GUT, then alpha_1 = ratio^2 * alpha_GUT

# One-loop evolution: 1/alpha_i(M_Z) = 1/alpha_i(M_KK) + b_i/(2pi) * ln(M_KK/M_Z)
L = np.log(M_KK / M_Z)
print(f"  ln(M_KK/M_Z) = {L:.4f}")

# From the ratio alone:
# 1/alpha_1(M_Z) = 1/alpha_1(M_KK) + b_1/(2pi) * L
# 1/alpha_2(M_Z) = 1/alpha_2(M_KK) + b_2/(2pi) * L
# alpha_1(M_KK)/alpha_2(M_KK) = r^2 where r = g_1/g_2 = 0.684

# sin^2(theta_W)(M_Z) = (3/5) * alpha_1 / ((3/5)*alpha_1 + alpha_2)
# At M_Z: sin^2 = alpha_1 / (alpha_1 + (5/3)*alpha_2)  [GUT normalized]

# Let's solve for alpha_GUT = alpha_2(M_KK) by requiring alpha_em(M_Z) = 1/127.951
# 1/alpha_em = 1/alpha_1 + 1/alpha_2 in standard convention
# With GUT normalization: 1/alpha_em = (3/5)/alpha_1_GUT + 1/alpha_2
# Actually: alpha_em = alpha' * cos^2(theta_W) = alpha_2 * sin^2(theta_W)
# 1/alpha_em = 1/alpha_2 + (5/3)/alpha_1_GUT

# Scan alpha_GUT to find consistency
alpha_GUT_range = np.linspace(0.01, 0.10, 1000)
r2 = g1_over_g2_KK**2

best_alpha_GUT = None
best_diff = np.inf

for alpha_GUT in alpha_GUT_range:
    alpha_2_KK = alpha_GUT
    alpha_1_KK = r2 * alpha_GUT

    # One-loop running
    alpha_1_inv_MZ = 1.0/alpha_1_KK + b1/(2*np.pi) * L
    alpha_2_inv_MZ = 1.0/alpha_2_KK + b2/(2*np.pi) * L

    alpha_1_MZ = 1.0 / alpha_1_inv_MZ
    alpha_2_MZ = 1.0 / alpha_2_inv_MZ

    # Electromagnetic coupling
    # 1/alpha_em = (5/3)/alpha_1 + 1/alpha_2 (GUT normalized)
    alpha_em_inv = (5.0/3.0) / alpha_1_MZ + 1.0 / alpha_2_MZ

    diff = abs(alpha_em_inv - alpha_em_inv_pdg)
    if diff < best_diff:
        best_diff = diff
        best_alpha_GUT = alpha_GUT

# Use the best fit
alpha_GUT = best_alpha_GUT
alpha_2_KK = alpha_GUT
alpha_1_KK = r2 * alpha_GUT

print(f"\n  Best-fit alpha_GUT = alpha_2(M_KK) = {alpha_GUT:.6f}")
print(f"  alpha_1(M_KK) = r^2 * alpha_GUT = {alpha_1_KK:.6f}")
print(f"  g_2(M_KK) = {np.sqrt(4*np.pi*alpha_2_KK):.6f}")
print(f"  g_1(M_KK) = {np.sqrt(4*np.pi*alpha_1_KK):.6f}")

# Run to M_Z
alpha_1_inv_MZ = 1.0/alpha_1_KK + b1/(2*np.pi) * L
alpha_2_inv_MZ = 1.0/alpha_2_KK + b2/(2*np.pi) * L

alpha_1_MZ = 1.0 / alpha_1_inv_MZ
alpha_2_MZ = 1.0 / alpha_2_inv_MZ
g1_MZ = np.sqrt(4 * np.pi * alpha_1_MZ)
g2_MZ = np.sqrt(4 * np.pi * alpha_2_MZ)
g1_over_g2_MZ = g1_MZ / g2_MZ

sin2_W_MZ = alpha_1_MZ / (alpha_1_MZ + (5.0/3.0)*alpha_2_MZ)
alpha_em_inv_MZ = (5.0/3.0)/alpha_1_MZ + 1.0/alpha_2_MZ

print(f"\n  One-loop results at M_Z:")
print(f"    alpha_1(M_Z) = {alpha_1_MZ:.6f}")
print(f"    alpha_2(M_Z) = {alpha_2_MZ:.6f}")
print(f"    g_1(M_Z) = {g1_MZ:.6f}")
print(f"    g_2(M_Z) = {g2_MZ:.6f}")
print(f"    g_1/g_2(M_Z) = {g1_over_g2_MZ:.6f}")
print(f"    sin^2(theta_W) = {sin2_W_MZ:.6f}")
print(f"    1/alpha_em = {alpha_em_inv_MZ:.3f}")

# ─────────────────────────────────────────────────────────────
# 3. Two-loop corrections (perturbative estimate)
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("TWO-LOOP CORRECTIONS")
print(f"{'=' * 70}")

# Solve 2-loop RGE numerically using scipy.integrate
from scipy.integrate import solve_ivp

def rge_2loop(t, y):
    """Two-loop RGE for alpha_i^{-1}(t) where t = ln(mu/M_Z).

    d(alpha_i^{-1})/dt = -b_i/(2*pi) - sum_j b_ij * alpha_j / (8*pi^2)
    """
    a1_inv, a2_inv, a3_inv = y
    a1, a2, a3 = 1.0/a1_inv, 1.0/a2_inv, 1.0/a3_inv

    da1_inv = -b1/(2*np.pi) - (b11*a1 + b12*a2 + b13*a3)/(8*np.pi**2)
    da2_inv = -b2/(2*np.pi) - (b21*a1 + b22*a2 + b23*a3)/(8*np.pi**2)
    da3_inv = -b3/(2*np.pi) - (b31*a1 + b32*a2 + b33*a3)/(8*np.pi**2)

    return [da1_inv, da2_inv, da3_inv]

# Initial conditions at M_KK
# Also need alpha_3(M_KK) -- use one-loop running backwards from alpha_s(M_Z) = 0.118
alpha_3_inv_KK = 1.0/alpha_s_pdg + b3/(2*np.pi) * L  # running backward
alpha_3_KK = 1.0/alpha_3_inv_KK

print(f"  alpha_3(M_KK) = {alpha_3_KK:.6f} (from alpha_s(M_Z) = {alpha_s_pdg})")

# Run from M_KK down to M_Z
t_KK = np.log(M_KK / M_Z)  # t at M_KK
t_MZ = 0.0                  # t at M_Z

y0 = [1.0/alpha_1_KK, 1.0/alpha_2_KK, 1.0/alpha_3_KK]

sol = solve_ivp(rge_2loop, [t_KK, t_MZ], y0, method='RK45',
                dense_output=True, rtol=1e-10, atol=1e-12)

if sol.success:
    y_MZ = sol.sol(0.0)
    a1_2loop = 1.0 / y_MZ[0]
    a2_2loop = 1.0 / y_MZ[1]
    a3_2loop = 1.0 / y_MZ[2]

    g1_2loop = np.sqrt(4*np.pi*a1_2loop)
    g2_2loop = np.sqrt(4*np.pi*a2_2loop)
    ratio_2loop = g1_2loop / g2_2loop

    sin2_2loop = a1_2loop / (a1_2loop + (5.0/3.0)*a2_2loop)
    aem_inv_2loop = (5.0/3.0)/a1_2loop + 1.0/a2_2loop

    print(f"\n  Two-loop results at M_Z:")
    print(f"    alpha_1(M_Z) = {a1_2loop:.6f}")
    print(f"    alpha_2(M_Z) = {a2_2loop:.6f}")
    print(f"    alpha_3(M_Z) = {a3_2loop:.6f}")
    print(f"    g_1/g_2(M_Z) = {ratio_2loop:.6f}")
    print(f"    sin^2(theta_W) = {sin2_2loop:.6f}")
    print(f"    1/alpha_em = {aem_inv_2loop:.3f}")
    print(f"    alpha_s(M_Z) = {a3_2loop:.6f}")

    # Two-loop shift
    print(f"\n  Two-loop shift:")
    print(f"    delta(g_1/g_2) = {ratio_2loop - g1_over_g2_MZ:.6f}")
    print(f"    delta(sin^2) = {sin2_2loop - sin2_W_MZ:.6f}")
else:
    print("  Two-loop integration failed!")
    ratio_2loop = g1_over_g2_MZ
    sin2_2loop = sin2_W_MZ

# ─────────────────────────────────────────────────────────────
# 4. Gate evaluation
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("GATE EVALUATION: RGE-33a")
print(f"{'=' * 70}")

target = g1_over_g2_MZ_pdg  # 0.7080
g1g2_best = ratio_2loop  # two-loop result
deviation = abs(g1g2_best - target) / target * 100

print(f"\n  Framework prediction: g_1/g_2(M_KK) = {g1_over_g2_KK:.6f}")
print(f"  After SM RGE running (two-loop): g_1/g_2(M_Z) = {g1g2_best:.6f}")
print(f"  PDG target: g_1/g_2(M_Z) = {target:.6f}")
print(f"  Deviation: {deviation:.2f}%")
print(f"  sin^2(theta_W) prediction: {sin2_2loop:.5f}")
print(f"  PDG sin^2(theta_W): {sin2_W_pdg:.5f}")
print(f"  sin^2 deviation: {abs(sin2_2loop - sin2_W_pdg)/sin2_W_pdg*100:.2f}%")

# Gate
if deviation < 5:
    verdict = "SOFT PASS"
elif deviation < 10:
    verdict = "PASS"
else:
    verdict = "FAIL"

print(f"\n  >>> RGE-33a verdict: {verdict} ({deviation:.1f}% deviation) <<<")
print(f"  (SOFT PASS < 5%, PASS < 10%, FAIL > 10%)")

# Check sin^2 in [0.225, 0.240]
sin2_in_range = 0.225 <= sin2_2loop <= 0.240
print(f"\n  sin^2(theta_W) in [0.225, 0.240]: {'YES' if sin2_in_range else 'NO'}")
print(f"  (PDG: 0.23122)")

# ─────────────────────────────────────────────────────────────
# 5. Sensitivity analysis
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("SENSITIVITY TO M_KK")
print(f"{'=' * 70}")

M_KK_range = np.logspace(14, 18, 50)
g1g2_vs_MKK = np.zeros(len(M_KK_range))
sin2_vs_MKK = np.zeros(len(M_KK_range))

for i, M in enumerate(M_KK_range):
    L_i = np.log(M / M_Z)
    a1_inv = 1.0/alpha_1_KK + b1/(2*np.pi) * L_i
    a2_inv = 1.0/alpha_2_KK + b2/(2*np.pi) * L_i
    a1_i = 1.0/a1_inv
    a2_i = 1.0/a2_inv
    g1g2_vs_MKK[i] = np.sqrt(a1_i/a2_i)
    sin2_vs_MKK[i] = a1_i / (a1_i + (5.0/3.0)*a2_i)

# Find M_KK where sin^2 = 0.231
from scipy.interpolate import interp1d
f_sin2 = interp1d(np.log10(M_KK_range), sin2_vs_MKK, kind='cubic')
from scipy.optimize import brentq
try:
    log_M_best = brentq(lambda lm: f_sin2(lm) - sin2_W_pdg, 14, 18)
    M_best = 10**log_M_best
    print(f"  M_KK for exact sin^2(theta_W) = 0.231: {M_best:.2e} GeV")
except:
    print(f"  Could not find M_KK for exact sin^2")

for M in [1e14, 1e15, 1e16, 1e17, 1e18]:
    idx = np.argmin(np.abs(M_KK_range - M))
    print(f"  M_KK = {M:.0e}: sin^2 = {sin2_vs_MKK[idx]:.5f}, "
          f"g_1/g_2 = {g1g2_vs_MKK[idx]:.5f}")

# ─────────────────────────────────────────────────────────────
# 6. Plot
# ─────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Running couplings
ax = axes[0, 0]
mu_range = np.logspace(np.log10(M_Z), np.log10(M_KK), 500)
t_range = np.log(mu_range / M_Z)
# One-loop
for bi, label, color in [(b1, 'alpha_1^{-1}', 'C0'),
                          (b2, 'alpha_2^{-1}', 'C1'),
                          (b3, 'alpha_3^{-1}', 'C2')]:
    if bi == b1:
        a_inv_0 = 1.0/alpha_1_KK
    elif bi == b2:
        a_inv_0 = 1.0/alpha_2_KK
    else:
        a_inv_0 = 1.0/alpha_3_KK
    a_inv = a_inv_0 + bi/(2*np.pi) * (t_KK - t_range)
    ax.plot(np.log10(mu_range), a_inv, '-', color=color, linewidth=2,
            label=f'$\\{label}$')

ax.axvline(x=np.log10(M_Z), color='gray', linestyle='--', alpha=0.5, label='M_Z')
ax.axvline(x=16, color='red', linestyle='--', alpha=0.5, label='M_KK')
ax.set_xlabel('log10(mu/GeV)')
ax.set_ylabel('alpha_i^{-1}')
ax.set_title('One-Loop Running of Gauge Couplings')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: g_1/g_2 ratio vs scale
ax = axes[0, 1]
a1_inv_mu = 1.0/alpha_1_KK + b1/(2*np.pi) * (t_KK - t_range)
a2_inv_mu = 1.0/alpha_2_KK + b2/(2*np.pi) * (t_KK - t_range)
ratio_mu = np.sqrt((1.0/a1_inv_mu) / (1.0/a2_inv_mu))
ax.plot(np.log10(mu_range), ratio_mu, 'b-', linewidth=2)
ax.axhline(y=g1_over_g2_KK, color='red', linestyle=':', alpha=0.7,
           label=f'Framework: {g1_over_g2_KK:.4f}')
ax.axhline(y=g1_over_g2_MZ_pdg, color='green', linestyle=':', alpha=0.7,
           label=f'PDG: {g1_over_g2_MZ_pdg:.4f}')
ax.axvline(x=np.log10(M_Z), color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('log10(mu/GeV)')
ax.set_ylabel('g_1/g_2')
ax.set_title('Gauge Coupling Ratio Running')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: sin^2(theta_W) vs M_KK
ax = axes[1, 0]
ax.plot(np.log10(M_KK_range), sin2_vs_MKK, 'b-', linewidth=2)
ax.axhline(y=sin2_W_pdg, color='green', linestyle=':', linewidth=2,
           label=f'PDG: {sin2_W_pdg:.5f}')
ax.axhspan(0.225, 0.240, alpha=0.15, color='green', label='Target [0.225, 0.240]')
ax.axvline(x=16, color='red', linestyle='--', alpha=0.5, label='M_KK = 10^16')
ax.set_xlabel('log10(M_KK/GeV)')
ax.set_ylabel('sin^2(theta_W) at M_Z')
ax.set_title('Weinberg Angle vs Compactification Scale')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Summary table as text
ax = axes[1, 1]
ax.axis('off')
summary = (
    f"RGE-33a GATE SUMMARY\n"
    f"{'─' * 40}\n"
    f"Input: g_1/g_2(M_KK) = {g1_over_g2_KK:.6f}\n"
    f"  (from e^{{-2*tau}}, tau = {tau_dump})\n"
    f"M_KK = 10^16 GeV\n"
    f"{'─' * 40}\n"
    f"One-loop results at M_Z:\n"
    f"  g_1/g_2 = {g1_over_g2_MZ:.6f}\n"
    f"  sin^2(theta_W) = {sin2_W_MZ:.5f}\n"
    f"Two-loop results at M_Z:\n"
    f"  g_1/g_2 = {ratio_2loop:.6f}\n"
    f"  sin^2(theta_W) = {sin2_2loop:.5f}\n"
    f"{'─' * 40}\n"
    f"PDG target:\n"
    f"  g_1/g_2 = {target:.6f}\n"
    f"  sin^2 = {sin2_W_pdg:.5f}\n"
    f"{'─' * 40}\n"
    f"Deviation: {deviation:.1f}%\n"
    f"sin^2 in [0.225,0.240]: {'YES' if sin2_in_range else 'NO'}\n"
    f"Verdict: {verdict}"
)
ax.text(0.1, 0.95, summary, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('Session 33a: RGE Gate (RGE-33a)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s33a_rge_gate.png', dpi=150, bbox_inches='tight')
print("\nPlot saved: tier0-computation/s33a_rge_gate.png")

# ─────────────────────────────────────────────────────────────
# 7. Save
# ─────────────────────────────────────────────────────────────

np.savez('tier0-computation/s33a_rge_gate.npz',
         g1_over_g2_KK=np.array([g1_over_g2_KK]),
         g1_over_g2_MZ_1loop=np.array([g1_over_g2_MZ]),
         g1_over_g2_MZ_2loop=np.array([ratio_2loop]),
         g1_over_g2_MZ_pdg=np.array([target]),
         sin2_1loop=np.array([sin2_W_MZ]),
         sin2_2loop=np.array([sin2_2loop]),
         sin2_pdg=np.array([sin2_W_pdg]),
         deviation_pct=np.array([deviation]),
         verdict=np.array([verdict]),
         alpha_GUT=np.array([alpha_GUT]),
         M_KK=np.array([M_KK]),
         tau_dump=np.array([tau_dump]),
         M_KK_range=M_KK_range,
         sin2_vs_MKK=sin2_vs_MKK,
         g1g2_vs_MKK=g1g2_vs_MKK,
         )
print("Data saved: tier0-computation/s33a_rge_gate.npz")
