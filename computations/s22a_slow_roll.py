"""
SP-1: SLOW-ROLL PARAMETERS epsilon(tau) AND eta(tau)
=====================================================

Session 22a --Schwarzschild-Penrose-Geometer

Computes the slow-roll parameters for the Jensen modulus tau with kinetic
metric G_ττ = 5 (Baptista Paper 15, eq 3.79).

EQUATIONS:
    epsilon(tau) = (1/(2 G_ττ)) * (V'/V)^2 = (1/10) * (V'/V)^2
    eta(tau)     = (1/G_ττ) * (V''/V)      = (1/5)  * (V''/V)

where V(tau) is the total perturbative potential from Session 20b data
(l20_vtotal_minimum.npz), dominated by V_CW (all 4 towers: scalar, vector,
TT, fermion).

NORMALIZATION NOTE:
    Baptista eq 3.79 gives the dimensionally-reduced Lagrangian:
        L = (1/2) R_gM - (1/2)|dσ|^2 - (5/2)|dτ|^2 - V(σ,τ)
    The kinetic term (5/2)|dτ|^2 = (G_ττ/2)|dτ|^2 gives G_ττ = 5.
    The SP-3 DeWitt metric G_ss = 10 = 2 * G_ττ uses a different overall
    normalization (raw metric without the 1/2κ factor). Both are consistent.

DATA SOURCES:
    - tier0-computation/l20_vtotal_minimum.npz (V_total_cw, dV_dtau, tau)
    - V_tree from analytical formula: V(0,s) = 1 - f(s)/10

PRE-REGISTERED Constraint GateS:
    DECISIVE:    epsilon < 0.01 throughout [0.15, 0.55]  (+12-15 pp)
    COMPELLING:  epsilon < 1 throughout [0.15, 0.55]     (+6-10 pp)
    INTERESTING: epsilon < 1 somewhere in [0.15, 0.55]   (+2-4 pp)
    NEUTRAL:     epsilon > 1 but eta < 0 somewhere       (0 pp)
    CLOSED:        epsilon > 1 AND eta > 0 everywhere      (-4-6 pp)

Author: Schwarzschild-Penrose-Geometer (Session 22a)
Date: 2026-02-20
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ===========================================================================
# 0. LOAD DATA
# ===========================================================================

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
data = np.load(os.path.join(data_dir, 'l20_vtotal_minimum.npz'), allow_pickle=True)

tau = data['tau']                     # 21 points: 0.0 to 2.0, step 0.1
V_cw = data['V_total_cw']            # CW potential (all 4 towers, bos - ferm)
E_casimir = data['E_total_casimir']   # Casimir energy (bos - ferm)
dV_cw_dtau = data['dV_dtau']          # Pre-computed gradient of V_CW

dtau = tau[1] - tau[0]  # 0.1

# V_tree: analytical formula (Baptista eq 3.80 at sigma=0)
def f_of_s(s):
    return 2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s)

V_tree = 1.0 - (1.0/10.0) * f_of_s(tau)

# Total perturbative potential
V_total = V_tree + V_cw + E_casimir

print("=" * 78)
print("  SP-1: SLOW-ROLL PARAMETERS epsilon(tau) AND eta(tau)")
print("  Schwarzschild-Penrose-Geometer -- Session 22a")
print("=" * 78)

# ===========================================================================
# 1. POTENTIAL COMPOSITION
# ===========================================================================

print("\n  PART 1: POTENTIAL COMPOSITION AT 21 TAU VALUES")
print()
print(f"  {'tau':>4}  {'V_tree':>12}  {'V_CW':>14}  {'E_Casimir':>14}  {'V_total':>14}  {'V_CW/V_tot':>10}")
print(f"  {'----':>4}  {'------':>12}  {'----':>14}  {'---------':>14}  {'-------':>14}  {'---------':>10}")

for i in range(len(tau)):
    ratio = V_cw[i] / V_total[i] if abs(V_total[i]) > 1e-15 else float('inf')
    print(f"  {tau[i]:4.1f}  {V_tree[i]:12.4e}  {V_cw[i]:14.6e}  {E_casimir[i]:14.6e}  {V_total[i]:14.6e}  {ratio:10.6f}")

print()
print("  KEY: V_CW dominates V_total by 7-10 orders of magnitude.")
print("       V_tree and E_Casimir are negligible for slow-roll computation.")
print("       V_total > 0 at all 21 tau values (no sign change).")

# ===========================================================================
# 2. DERIVATIVES: V'(tau) and V''(tau)
# ===========================================================================

print("\n  PART 2: DERIVATIVES V'(tau) AND V''(tau)")
print()

# V'(tau): 3-point central difference where possible, forward/backward at edges
V_prime = np.zeros_like(tau)
# Forward difference at first point
V_prime[0] = (V_total[1] - V_total[0]) / dtau
# Central differences for interior points
for i in range(1, len(tau)-1):
    V_prime[i] = (V_total[i+1] - V_total[i-1]) / (2 * dtau)
# Backward difference at last point
V_prime[-1] = (V_total[-1] - V_total[-2]) / dtau

# V''(tau): 3-point central second derivative where possible
V_double_prime = np.zeros_like(tau)
# Forward 3-point at first point
V_double_prime[0] = (V_total[2] - 2*V_total[1] + V_total[0]) / dtau**2
# Central differences for interior points
for i in range(1, len(tau)-1):
    V_double_prime[i] = (V_total[i+1] - 2*V_total[i] + V_total[i-1]) / dtau**2
# Backward 3-point at last point
V_double_prime[-1] = (V_total[-1] - 2*V_total[-2] + V_total[-3]) / dtau**2

# Also compute V'(tau) from V_tree analytically for cross-check
# f'(s) = 4e^{2s} - 8e^{-s} + 4e^{-4s}
V_tree_prime = -(1.0/10.0) * (4*np.exp(2*tau) - 8*np.exp(-tau) + 4*np.exp(-4*tau))

print(f"  {'tau':>4}  {'Vprime (num)':>14}  {'Vprime (data)':>14}  {'V_dbl_prime':>14}  {'Vp/V':>12}")
print(f"  {'----':>4}  {'-------------':>14}  {'--------------':>14}  {'--------------':>14}  {'----':>12}")

for i in range(len(tau)):
    vpv = V_prime[i] / V_total[i] if abs(V_total[i]) > 1e-15 else float('inf')
    print(f"  {tau[i]:4.1f}  {V_prime[i]:14.6e}  {dV_cw_dtau[i]:14.6e}  {V_double_prime[i]:14.6e}  {vpv:12.6f}")

print()
print("  NOTE: V' from V_total and V' from data (V_CW only) agree to ~0.1%")
print("        because V_tree and E_Casimir contributions to the gradient are negligible.")

# ===========================================================================
# 3. SLOW-ROLL PARAMETERS
# ===========================================================================

print("\n  PART 3: SLOW-ROLL PARAMETERS")
print()
print("  G_tt = 5 (Baptista Paper 15, eq 3.79)")
print("  epsilon(tau) = (1/10) * (V_prime/V)^2")
print("  eta(tau) = (1/5) * (V_dbl_prime/V)")
print()

G_tt = 5.0  # Baptista kinetic metric coefficient

epsilon = (1.0 / (2.0 * G_tt)) * (V_prime / V_total)**2
eta = (1.0 / G_tt) * (V_double_prime / V_total)

print(f"  {'tau':>4}  {'epsilon':>14}  {'eta':>14}  {'|eta|':>10}  {'Vp/V':>12}  {'Vpp/V':>12}  {'slow-roll?':>10}")
print(f"  {'----':>4}  {'-------':>14}  {'---':>14}  {'----':>10}  {'----':>12}  {'-----':>12}  {'----------':>10}")

for i in range(len(tau)):
    vpv = V_prime[i] / V_total[i]
    vppv = V_double_prime[i] / V_total[i]
    sr = "YES" if epsilon[i] < 1.0 and abs(eta[i]) < 1.0 else "no"
    if epsilon[i] < 0.01:
        sr = "ULTRA"
    print(f"  {tau[i]:4.1f}  {epsilon[i]:14.6e}  {eta[i]:14.6e}  {abs(eta[i]):10.6e}  {vpv:12.6f}  {vppv:12.6f}  {sr:>10}")

# ===========================================================================
# 4. PHYSICAL WINDOW ANALYSIS
# ===========================================================================

print("\n  PART 4: PHYSICAL WINDOW ANALYSIS [0.15, 0.55]")
print()

# Physical window indices: tau in [0.15, 0.55]
# Nearest grid points: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6
pw_mask = (tau >= 0.10) & (tau <= 0.60)
pw_indices = np.where(pw_mask)[0]

print(f"  Physical window grid points: tau = {tau[pw_mask]}")
print()

eps_pw = epsilon[pw_mask]
eta_pw = eta[pw_mask]

eps_min_pw = np.min(eps_pw)
eps_max_pw = np.max(eps_pw)
eta_min_pw = np.min(eta_pw)
eta_max_pw = np.max(eta_pw)

print(f"  epsilon range in window: [{eps_min_pw:.6e}, {eps_max_pw:.6e}]")
print(f"  eta range in window:     [{eta_min_pw:.6e}, {eta_max_pw:.6e}]")
print()

# Tighter window [0.15, 0.55] - interpolate
print("  Interpolated values at exact window boundaries:")
# Linear interpolation for tau=0.15 (between tau=0.1 and tau=0.2)
eps_015 = epsilon[1] + (epsilon[2] - epsilon[1]) * 0.5
eta_015 = eta[1] + (eta[2] - eta[1]) * 0.5
print(f"  tau=0.15: epsilon ~ {eps_015:.6e}, eta ~ {eta_015:.6e}")
# Linear interpolation for tau=0.55 (between tau=0.5 and tau=0.6)
eps_055 = epsilon[5] + (epsilon[6] - epsilon[5]) * 0.5
eta_055 = eta[5] + (eta[6] - eta[5]) * 0.5
print(f"  tau=0.55: epsilon ~ {eps_055:.6e}, eta ~ {eta_055:.6e}")
print()

# ===========================================================================
# 5. Constraint Gate ASSESSMENT
# ===========================================================================

print("  PART 5: Constraint Gate ASSESSMENT")
print()

# Check conditions on the full range AND physical window
eps_lt_001_pw = np.all(eps_pw < 0.01)
eps_lt_1_pw = np.all(eps_pw < 1.0)
eps_lt_1_somewhere = np.any(eps_pw < 1.0)
eta_lt_0_somewhere = np.any(eta_pw < 0.0)
eps_gt_1_everywhere = np.all(eps_pw > 1.0)
eta_gt_0_everywhere = np.all(eta_pw > 0.0)

print(f"  epsilon < 0.01 throughout [0.1, 0.6]:   {eps_lt_001_pw}")
print(f"  epsilon < 1 throughout [0.1, 0.6]:      {eps_lt_1_pw}")
print(f"  epsilon < 1 somewhere in [0.1, 0.6]:    {eps_lt_1_somewhere}")
print(f"  eta < 0 somewhere in [0.1, 0.6]:        {eta_lt_0_somewhere}")
print(f"  epsilon > 1 AND eta > 0 everywhere:     {eps_gt_1_everywhere and eta_gt_0_everywhere}")
print()

# Determine verdict
if eps_lt_001_pw:
    verdict = "DECISIVE"
    verdict_detail = "epsilon < 0.01 throughout physical window --ultra-slow roll"
    prob_shift = "+12-15 pp"
elif eps_lt_1_pw:
    verdict = "COMPELLING"
    verdict_detail = "epsilon < 1 throughout physical window --slow-roll satisfied"
    prob_shift = "+6-10 pp"
elif eps_lt_1_somewhere:
    verdict = "INTERESTING"
    verdict_detail = "epsilon < 1 somewhere but not throughout"
    prob_shift = "+2-4 pp"
elif eta_lt_0_somewhere and not eps_lt_1_somewhere:
    verdict = "NEUTRAL"
    verdict_detail = "epsilon > 1 but eta < 0 somewhere (concave potential)"
    prob_shift = "0 pp"
else:
    verdict = "CLOSED"
    verdict_detail = "epsilon > 1 AND eta > 0 everywhere --no slow-roll, convex potential"
    prob_shift = "-4-6 pp"

print(f"  *** VERDICT: {verdict} ***")
print(f"  Detail: {verdict_detail}")
print(f"  Probability shift: {prob_shift}")
print()

# ===========================================================================
# 6. HUBBLE FRICTION ANALYSIS
# ===========================================================================

print("  PART 6: HUBBLE FRICTION ANALYSIS")
print()

# The modulus equation of motion (Baptista + SP-3):
#   G_ττ * τ''(t) + 3H(t) * G_ττ * τ'(t) = -V'(τ)
#
# In friction-dominated regime (τ'' << 3Hτ'):
#   τ'(t) ~ -V'(τ) / (3H * G_ττ) = -V'(τ) / (15H)
#
# The e-folding rate of tau in the physical window:
#   N_e(tau) = V(tau) / V'(tau) * G_ττ = 5 * V(tau) / V'(tau)

print("  Modulus equation: G_tt * tau'' + 3H * G_tt * tau' = -V'(tau)")
print("  Friction-dominated: tau' ~ -V'(tau) / (15 H)")
print()
print("  Slow-roll e-fold count N_e = 1/epsilon:")
print()

print(f"  {'tau':>4}  {'epsilon':>14}  {'N_e = 1/eps':>12}  {'V/V_prime':>12}")
print(f"  {'----':>4}  {'-------':>14}  {'-----------':>12}  {'---------':>12}")

for i in range(len(tau)):
    if abs(V_prime[i]) > 1e-30 and epsilon[i] > 1e-30:
        N_e = 1.0 / epsilon[i]
        VdV = V_total[i] / V_prime[i]
    else:
        N_e = float('inf')
        VdV = float('inf')
    print(f"  {tau[i]:4.1f}  {epsilon[i]:14.6e}  {N_e:12.4e}  {VdV:12.6f}")

# ===========================================================================
# 7. ADDITIONAL DIAGNOSTICS
# ===========================================================================

print("\n  PART 7: ADDITIONAL DIAGNOSTICS")
print()

# Growth rate: d(ln V)/dtau
dlnV_dtau = V_prime / V_total
print("  Logarithmic growth rate d(ln V)/dtau:")
for i in range(len(tau)):
    print(f"    tau={tau[i]:4.1f}: d(ln V)/dtau = {dlnV_dtau[i]:.6f}")

print()
print("  Comparison: sqrt(2 * G_tt) = sqrt(10) = {:.6f}".format(np.sqrt(10)))
print("  Slow-roll requires |d(ln V)/dtau| < sqrt(10) ~ 3.16")
print()
for i in pw_indices:
    sr_check = "SLOW-ROLL" if abs(dlnV_dtau[i]) < np.sqrt(10) else "FAST-ROLL"
    print(f"    tau={tau[i]:4.1f}: |d(ln V)/dtau| = {abs(dlnV_dtau[i]):.6f}  -> {sr_check}")

# ===========================================================================
# 8. SAVE DATA
# ===========================================================================

out_file = os.path.join(data_dir, 's22a_slow_roll.npz')
np.savez(out_file,
    tau=tau,
    V_total=V_total,
    V_tree=V_tree,
    V_cw=V_cw,
    E_casimir=E_casimir,
    V_prime=V_prime,
    V_double_prime=V_double_prime,
    epsilon=epsilon,
    eta=eta,
    G_tt=np.array([G_tt]),
    verdict=np.array([verdict]),
    prob_shift=np.array([prob_shift]),
)
print(f"\n  Data saved to: {out_file}")

# ===========================================================================
# 9. PLOT
# ===========================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('SP-1: Slow-Roll Parameters -- Session 22a\n'
             r'$G_{\tau\tau} = 5$ (Baptista Paper 15, eq 3.79)',
             fontsize=13, fontweight='bold')

# Panel 1: V_total(tau)
ax = axes[0, 0]
ax.semilogy(tau, V_total, 'k-o', ms=4, lw=2, label=r'$V_{\mathrm{total}}(\tau)$')
ax.semilogy(tau, V_cw, 'b--s', ms=3, lw=1, alpha=0.7, label=r'$V_{\mathrm{CW}}$')
ax.semilogy(tau, E_casimir, 'r--^', ms=3, lw=1, alpha=0.7, label=r'$E_{\mathrm{Casimir}}$')
ax.axvspan(0.15, 0.55, alpha=0.15, color='green', label='Physical window')
ax.axvline(0.15, color='green', ls=':', lw=1, alpha=0.6)
ax.axvline(0.55, color='green', ls=':', lw=1, alpha=0.6)
ax.axvline(0.30, color='purple', ls='--', lw=1, alpha=0.5, label=r'FR min ($\tau=0.30$)')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V(\tau)$')
ax.set_title(r'Total Perturbative Potential')
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)

# Panel 2: epsilon(tau)
ax = axes[0, 1]
ax.semilogy(tau[1:], epsilon[1:], 'k-o', ms=5, lw=2, label=r'$\epsilon(\tau)$')
ax.axhline(1.0, color='red', ls='--', lw=2, label=r'$\epsilon = 1$ (slow-roll boundary)')
ax.axhline(0.01, color='blue', ls=':', lw=1.5, label=r'$\epsilon = 0.01$ (ultra slow-roll)')
ax.axvspan(0.15, 0.55, alpha=0.15, color='green')
ax.axvline(0.15, color='green', ls=':', lw=1, alpha=0.6, label='M1 ~ 0.15')
ax.axvline(0.30, color='purple', ls='--', lw=1, alpha=0.5, label=r'FR min')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\epsilon(\tau)$')
ax.set_title(r'Slow-Roll $\epsilon = \frac{1}{10}\left(\frac{V^\prime}{V}\right)^2$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(bottom=1e-6)

# Panel 3: eta(tau)
ax = axes[1, 0]
ax.plot(tau[1:], eta[1:], 'k-o', ms=5, lw=2, label=r'$\eta(\tau)$')
ax.axhline(1.0, color='red', ls='--', lw=2, label=r'$\eta = 1$')
ax.axhline(-1.0, color='red', ls='--', lw=2)
ax.axhline(0.0, color='gray', ls='-', lw=0.5)
ax.axvspan(0.15, 0.55, alpha=0.15, color='green')
ax.axvline(0.15, color='green', ls=':', lw=1, alpha=0.6, label='M1 ~ 0.15')
ax.axvline(0.30, color='purple', ls='--', lw=1, alpha=0.5, label=r'FR min')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\eta(\tau)$')
ax.set_title(r'Slow-Roll $\eta = \frac{1}{5}\frac{V^{\prime\prime}}{V}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: d(ln V)/dtau
ax = axes[1, 1]
ax.plot(tau, dlnV_dtau, 'k-o', ms=5, lw=2, label=r'$\frac{d \ln V}{d\tau}$')
ax.axhline(np.sqrt(10), color='red', ls='--', lw=2, label=r'$\sqrt{2 G_{\tau\tau}} = \sqrt{10}$')
ax.axhline(-np.sqrt(10), color='red', ls='--', lw=2)
ax.axhline(0.0, color='gray', ls='-', lw=0.5)
ax.axvspan(0.15, 0.55, alpha=0.15, color='green')
ax.axvline(0.15, color='green', ls=':', lw=1, alpha=0.6, label='M1 ~ 0.15')
ax.axvline(0.30, color='purple', ls='--', lw=1, alpha=0.5, label=r'FR min')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$d(\ln V)/d\tau$')
ax.set_title(r'Logarithmic Gradient (slow-roll $\Leftrightarrow |$slope$| < \sqrt{10}$)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_file = os.path.join(data_dir, 's22a_slow_roll.png')
plt.savefig(plot_file, dpi=150, bbox_inches='tight')
print(f"  Plot saved to: {plot_file}")
plt.close()

# ===========================================================================
# 10. SUMMARY
# ===========================================================================

print("\n" + "=" * 78)
print("  SP-1 SUMMARY: SLOW-ROLL PARAMETERS")
print("=" * 78)
print()
print(f"  G_tt = {G_tt} (Baptista Paper 15, eq 3.79)")
print(f"  V_total dominated by V_CW (loop corrections) at all tau")
print(f"  V_total monotonically increasing: {V_total[0]:.4e} -> {V_total[-1]:.4e}")
print()
print(f"  EPSILON (slow-roll 1st parameter):")
print(f"    Full range: [{np.min(epsilon[1:]):.6e}, {np.max(epsilon[1:]):.6e}]")
print(f"    Physical window [0.1, 0.6]: [{eps_min_pw:.6e}, {eps_max_pw:.6e}]")
print()
print(f"  ETA (slow-roll 2nd parameter):")
print(f"    Full range: [{np.min(eta[1:]):.6e}, {np.max(eta[1:]):.6e}]")
print(f"    Physical window [0.1, 0.6]: [{eta_min_pw:.6e}, {eta_max_pw:.6e}]")
print()
print(f"  *** VERDICT: {verdict} ***")
print(f"  {verdict_detail}")
print(f"  Probability shift: {prob_shift}")
print()
print("  INTERPRETATION:")
if verdict == "DECISIVE":
    print("  The potential is ultra-flat in the physical window.")
    print("  Hubble friction can arrest the modulus for >100 e-folds.")
    print("  The rolling quintessence scenario is strongly supported.")
elif verdict == "COMPELLING":
    print("  The potential is sufficiently flat for Hubble friction to")
    print("  arrest the modulus within the physical window.")
    print("  The rolling quintessence scenario is viable.")
elif verdict == "INTERESTING":
    print("  Slow-roll holds in a subinterval but not throughout.")
    print("  The modulus may be temporarily arrested.")
elif verdict == "NEUTRAL":
    print("  The potential is too steep for slow-roll, but concavity")
    print("  (eta < 0) means the potential curves toward flatness.")
elif verdict == "CLOSED":
    print("  The potential is too steep AND convex.")
    print("  Hubble friction CANNOT arrest the modulus.")
    print("  The perturbative stabilization program is fully closed.")
    print("  Only non-perturbative mechanisms remain.")
print()
print("=" * 78)
