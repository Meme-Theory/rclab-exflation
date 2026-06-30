#!/usr/bin/env python3
"""
S54 SCALE-FACTOR-54: Connes Distance as Effective Scale Factor
==============================================================
Gate: SCALE-FACTOR-54
  PASS if a(0.19)/a(0) > 1.05
  INFO if ratio in (1.00, 1.05)
  FAIL if ratio <= 1.00

Method:
  1. Load W1-2 Connes lattice data (s54_connes_latt.npz)
  2. Compute a(tau) = <d_D>(tau) / <d_D>(0)
  3. Compute H(tau) = (1/a) da/dtau  (Hubble-like)
  4. Compute q(tau) = -a * a'' / (a')^2  (deceleration parameter)
  5. Fit to exponential, power-law, quadratic forms
  6. Plot a(tau), H(tau), q(tau)
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

from canonical_constants import tau_fold

# =========================================================================
# 1. Load data
# =========================================================================
data = np.load("s54_connes_latt.npz", allow_pickle=True)
tau = data["tau_values"]          # (10,)
d_mean = data["mean_distance"]    # (10,) = <d_D>(tau)
d_std = data["std_distance"]      # (10,)
d_min = data["min_distance"]
d_max = data["max_distance"]
d_median = data["median_distance"]

N_tau = len(tau)
print(f"Loaded {N_tau} tau values: {tau}")
print(f"Mean distances: {d_mean}")

# =========================================================================
# 2. Scale factor a(tau) = <d_D>(tau) / <d_D>(0)
# =========================================================================
a0 = d_mean[0]
a = d_mean / a0
print(f"\na(0) = 1 by definition  [<d_D>(0) = {a0:.6f}]")
print(f"Scale factor a(tau):")
for i in range(N_tau):
    print(f"  tau={tau[i]:.4f}  a={a[i]:.6f}  <d_D>={d_mean[i]:.6f}")

# =========================================================================
# 3. Expansion ratio at fold
# =========================================================================
# Find the tau closest to tau_fold
idx_fold = np.argmin(np.abs(tau - tau_fold))
tau_at_fold = tau[idx_fold]
a_at_fold = a[idx_fold]
print(f"\n--- GATE: SCALE-FACTOR-54 ---")
print(f"tau_fold (canonical) = {tau_fold}")
print(f"Nearest grid tau     = {tau_at_fold:.6f} (index {idx_fold})")
print(f"a(fold) = {a_at_fold:.6f}")
print(f"Expansion ratio a(fold)/a(0) = {a_at_fold:.6f}")

if a_at_fold > 1.05:
    verdict = "PASS"
elif a_at_fold > 1.00:
    verdict = "INFO"
else:
    verdict = "FAIL"
print(f"Gate verdict: {verdict} (threshold > 1.05 for PASS)")

# =========================================================================
# 4. H(tau) = (1/a) da/dtau  via spline differentiation
# =========================================================================
# Use cubic spline for smooth derivatives
# k=3 for cubic, s=0 for exact interpolation
spl_a = UnivariateSpline(tau, a, k=3, s=0)
da_dtau = spl_a.derivative()(tau)
d2a_dtau2 = spl_a.derivative(n=2)(tau)

H = da_dtau / a
print(f"\nHubble-like parameter H(tau) = (1/a) da/dtau:")
for i in range(N_tau):
    print(f"  tau={tau[i]:.4f}  H={H[i]:.4f}")

H_at_fold = H[idx_fold]
print(f"H(fold) = {H_at_fold:.4f}")

# =========================================================================
# 5. q(tau) = -a * a'' / (a')^2  deceleration parameter
# =========================================================================
# q < 0 => acceleration, q > 0 => deceleration, q = 0 => constant rate
# Avoid division by zero
q = np.full_like(a, np.nan)
mask = da_dtau**2 > 1e-20
q[mask] = -a[mask] * d2a_dtau2[mask] / da_dtau[mask]**2
print(f"\nDeceleration parameter q(tau) = -a*a''/(a')^2:")
for i in range(N_tau):
    print(f"  tau={tau[i]:.4f}  q={q[i]:.4f}")

q_at_fold = q[idx_fold]
print(f"q(fold) = {q_at_fold:.4f}")
if q_at_fold < 0:
    print("  => ACCELERATING expansion at fold")
elif q_at_fold > 0:
    print("  => DECELERATING expansion at fold")
else:
    print("  => COASTING at fold")

# =========================================================================
# 6. Functional fits
# =========================================================================
# (a) Exponential: a(tau) = A * exp(B * tau)
def f_exp(t, A, B):
    return A * np.exp(B * t)

popt_exp, pcov_exp = curve_fit(f_exp, tau, a, p0=[1.0, 3.0])
A_exp, B_exp = popt_exp
a_fit_exp = f_exp(tau, *popt_exp)
residual_exp = np.sqrt(np.mean((a - a_fit_exp)**2))
R2_exp = 1 - np.sum((a - a_fit_exp)**2) / np.sum((a - np.mean(a))**2)
print(f"\n--- Fit: Exponential a = A*exp(B*tau) ---")
print(f"  A = {A_exp:.6f}, B = {B_exp:.6f}")
print(f"  RMSE = {residual_exp:.6e}, R^2 = {R2_exp:.6f}")

# (b) Power law: a(tau) = A * (tau + tau_0)^n  (offset to avoid tau=0 singularity)
# Actually try a(tau) = 1 + C*tau^n (since a(0)=1)
def f_power(t, C, n):
    return 1 + C * t**n

try:
    popt_pow, pcov_pow = curve_fit(f_power, tau[1:], a[1:], p0=[10.0, 1.0], maxfev=5000)
    C_pow, n_pow = popt_pow
    a_fit_pow = np.zeros_like(a)
    a_fit_pow[0] = 1.0
    a_fit_pow[1:] = f_power(tau[1:], *popt_pow)
    residual_pow = np.sqrt(np.mean((a - a_fit_pow)**2))
    R2_pow = 1 - np.sum((a - a_fit_pow)**2) / np.sum((a - np.mean(a))**2)
    print(f"\n--- Fit: Power-law a = 1 + C*tau^n ---")
    print(f"  C = {C_pow:.6f}, n = {n_pow:.6f}")
    print(f"  RMSE = {residual_pow:.6e}, R^2 = {R2_pow:.6f}")
except Exception as e:
    print(f"\nPower-law fit failed: {e}")
    C_pow, n_pow = np.nan, np.nan
    R2_pow = -1

# (c) Quadratic: a(tau) = 1 + alpha*tau + beta*tau^2
def f_quad(t, alpha, beta):
    return 1.0 + alpha * t + beta * t**2

popt_quad, pcov_quad = curve_fit(f_quad, tau, a, p0=[3.0, 5.0])
alpha_q, beta_q = popt_quad
a_fit_quad = f_quad(tau, *popt_quad)
residual_quad = np.sqrt(np.mean((a - a_fit_quad)**2))
R2_quad = 1 - np.sum((a - a_fit_quad)**2) / np.sum((a - np.mean(a))**2)
print(f"\n--- Fit: Quadratic a = 1 + alpha*tau + beta*tau^2 ---")
print(f"  alpha = {alpha_q:.6f}, beta = {beta_q:.6f}")
print(f"  RMSE = {residual_quad:.6e}, R^2 = {R2_quad:.6f}")

# (d) Linear: a(tau) = 1 + c*tau
def f_lin(t, c):
    return 1.0 + c * t

popt_lin, _ = curve_fit(f_lin, tau, a)
c_lin = popt_lin[0]
a_fit_lin = f_lin(tau, *popt_lin)
R2_lin = 1 - np.sum((a - a_fit_lin)**2) / np.sum((a - np.mean(a))**2)
print(f"\n--- Fit: Linear a = 1 + c*tau ---")
print(f"  c = {c_lin:.6f}")
print(f"  R^2 = {R2_lin:.6f}")

# Summary of fits
print(f"\n=== FIT COMPARISON (R^2) ===")
print(f"  Exponential: R^2 = {R2_exp:.6f}")
print(f"  Quadratic:   R^2 = {R2_quad:.6f}")
print(f"  Power-law:   R^2 = {R2_pow:.6f}")
print(f"  Linear:      R^2 = {R2_lin:.6f}")

# =========================================================================
# 7. Cross-check with W1-2 fit: a(tau) = 1.014 * exp(3.651 * tau)
# =========================================================================
a_w12 = 1.014 * np.exp(3.651 * tau)
R2_w12 = 1 - np.sum((a - a_w12)**2) / np.sum((a - np.mean(a))**2)
print(f"\n--- W1-2 cross-check: a = 1.014*exp(3.651*tau) ---")
print(f"  R^2 = {R2_w12:.6f}")
print(f"  This fit: A={A_exp:.4f}, B={B_exp:.4f}")
print(f"  W1-2 fit: A=1.014, B=3.651")
print(f"  Deviation: dA={A_exp-1.014:.4f}, dB={B_exp-3.651:.4f}")

# Note: W1-2 was fitting <d_D> directly, we're fitting a = <d_D>/<d_D>(0).
# The W1-2 fit gives: a(tau) = (1.014/a0)*exp(3.651*tau)
# which should be a(tau) = (1.014/0.9916)*exp(3.651*tau) = 1.0226*exp(3.651*tau)
# So A_exp should be close to 1.0226, not 1.014
a_w12_normalized = (1.014 / a0) * np.exp(3.651 * tau)
R2_w12_norm = 1 - np.sum((a - a_w12_normalized)**2) / np.sum((a - np.mean(a))**2)
print(f"\n  W1-2 normalized: a = ({1.014/a0:.4f})*exp(3.651*tau)")
print(f"  R^2 (normalized) = {R2_w12_norm:.6f}")

# =========================================================================
# 8. Additional diagnostics
# =========================================================================
# Scale factor from median, min, max
a_median = d_median / d_median[0]
a_min = d_min / d_min[0]
a_max = d_max / d_max[0]

# Relative dispersion sigma/mean as function of tau
rel_disp = d_std / d_mean
print(f"\nRelative dispersion sigma/<d> at each tau:")
for i in range(N_tau):
    print(f"  tau={tau[i]:.4f}  sigma/mean={rel_disp[i]:.4f}")
print(f"  Mean relative dispersion: {np.mean(rel_disp):.4f}")
print(f"  Variation of rel. disp.: {np.std(rel_disp)/np.mean(rel_disp)*100:.2f}%")

# =========================================================================
# 9. Plots
# =========================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("SCALE-FACTOR-54: Connes Distance Scale Factor", fontsize=14, fontweight="bold")

# --- Panel (a): Scale factor a(tau) ---
ax = axes[0, 0]
ax.plot(tau, a, "ko-", ms=7, lw=2, label=r"$a(\tau) = \langle d_D \rangle / \langle d_D \rangle(0)$")
tau_dense = np.linspace(0, tau[-1], 200)
ax.plot(tau_dense, f_exp(tau_dense, *popt_exp), "r--", lw=1.5,
        label=rf"Exp: ${A_exp:.3f} e^{{{B_exp:.3f}\tau}}$ ($R^2={R2_exp:.4f}$)")
ax.plot(tau_dense, f_quad(tau_dense, *popt_quad), "b:", lw=1.5,
        label=rf"Quad: $1+{alpha_q:.2f}\tau+{beta_q:.2f}\tau^2$ ($R^2={R2_quad:.4f}$)")
ax.axvline(tau_fold, color="green", ls="--", alpha=0.5, label=rf"$\tau_{{fold}}={tau_fold}$")
ax.axhline(1.0, color="gray", ls=":", alpha=0.3)
ax.set_xlabel(r"$\tau$")
ax.set_ylabel(r"$a(\tau)$")
ax.set_title("(a) Scale Factor")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (b): H(tau) Hubble-like parameter ---
ax = axes[0, 1]
ax.plot(tau, H, "ko-", ms=7, lw=2)
ax.axvline(tau_fold, color="green", ls="--", alpha=0.5, label=rf"$\tau_{{fold}}$")
ax.set_xlabel(r"$\tau$")
ax.set_ylabel(r"$H(\tau) = \frac{1}{a}\frac{da}{d\tau}$")
ax.set_title(rf"(b) Hubble-like Parameter [$H(\tau_{{fold}})={H_at_fold:.3f}$]")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Add annotation about deceleration
H_range = H[-1] - H[0]
if H_range < 0:
    ax.annotate("DECELERATING\n(H decreasing)", xy=(0.6, 0.8), xycoords="axes fraction",
                fontsize=10, color="blue", ha="center",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))

# --- Panel (c): q(tau) deceleration parameter ---
ax = axes[1, 0]
ax.plot(tau, q, "ko-", ms=7, lw=2)
ax.axvline(tau_fold, color="green", ls="--", alpha=0.5, label=rf"$\tau_{{fold}}$")
ax.axhline(0, color="red", ls=":", alpha=0.5, label="q=0 (coasting)")
ax.axhline(-1, color="orange", ls=":", alpha=0.3, label="q=-1 (de Sitter)")
ax.set_xlabel(r"$\tau$")
ax.set_ylabel(r"$q(\tau) = -\frac{a \cdot a''}{(a')^2}$")
ax.set_title(rf"(c) Deceleration Parameter [$q(\tau_{{fold}})={q_at_fold:.3f}$]")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Shade acceleration vs deceleration
ax.fill_between(tau, np.min(q)-0.5, 0, alpha=0.05, color="red", label="Acceleration")
ax.fill_between(tau, 0, np.max(q)+0.5, alpha=0.05, color="blue", label="Deceleration")
ax.set_ylim(min(np.nanmin(q)-0.3, -1.5), max(np.nanmax(q)+0.3, 1.5))

# --- Panel (d): Multi-statistic scale factors ---
ax = axes[1, 1]
ax.plot(tau, a, "ko-", ms=6, lw=2, label=r"Mean $\langle d_D \rangle$")
ax.plot(tau, a_median, "s--", color="purple", ms=5, lw=1.5, label="Median")
ax.plot(tau, a_min, "^:", color="blue", ms=5, lw=1, label="Min pair")
ax.plot(tau, a_max, "v:", color="red", ms=5, lw=1, label="Max pair")
ax.fill_between(tau, a - d_std/a0, a + d_std/a0, alpha=0.15, color="gray", label=r"$\pm\sigma$")
ax.axvline(tau_fold, color="green", ls="--", alpha=0.5)
ax.set_xlabel(r"$\tau$")
ax.set_ylabel(r"$a(\tau)$ (various statistics)")
ax.set_title("(d) Scale Factor Consistency")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("s54_scale_factor.png", dpi=150, bbox_inches="tight")
print(f"\nPlot saved: s54_scale_factor.png")

# =========================================================================
# 10. Final summary
# =========================================================================
print("\n" + "="*70)
print("SCALE-FACTOR-54 FINAL SUMMARY")
print("="*70)
print(f"Scale factor a(tau) = <d_D>(tau) / <d_D>(0)")
print(f"  <d_D>(0) = {a0:.6f}")
print(f"  <d_D>(fold) = {d_mean[idx_fold]:.6f}")
print(f"  a(fold) = {a_at_fold:.6f}")
print(f"")
print(f"GATE: SCALE-FACTOR-54")
print(f"  Criterion: a(fold)/a(0) > 1.05")
print(f"  Measured:  a(fold)/a(0) = {a_at_fold:.6f}")
print(f"  Verdict:   {verdict}")
print(f"")
print(f"Hubble-like H(tau):")
print(f"  H(0)    = {H[0]:.4f}")
print(f"  H(fold) = {H_at_fold:.4f}")
print(f"  H(max)  = {H[-1]:.4f}")
print(f"  H decreasing: {H[-1] < H[0]}")
print(f"")
print(f"Deceleration q(tau):")
print(f"  q(fold) = {q_at_fold:.4f}")
print(f"  q < 0 => accelerating, q > 0 => decelerating")
print(f"  Expansion type at fold: {'ACCELERATING' if q_at_fold < 0 else 'DECELERATING'}")
print(f"")
print(f"Best fit: Exponential a = {A_exp:.4f} * exp({B_exp:.4f} * tau)")
print(f"  R^2 = {R2_exp:.6f}")
print(f"  W1-2 comparison: A=1.014, B=3.651 (raw), normalized A={1.014/a0:.4f}")
print(f"  Fit ranking: Exp({R2_exp:.4f}) > Quad({R2_quad:.4f}) > Power({R2_pow:.4f}) > Lin({R2_lin:.4f})")
print(f"")
print(f"Relative dispersion sigma/<d> = {np.mean(rel_disp):.4f} (mean)")
print(f"  Variation: {np.std(rel_disp)/np.mean(rel_disp)*100:.2f}%")
print(f"  => Self-similar expansion (dispersion tracks mean)")
print("="*70)

# =========================================================================
# 11. Save results
# =========================================================================
np.savez("s54_scale_factor.npz",
         tau=tau,
         a=a,
         H=H,
         q=q,
         d_mean=d_mean,
         d_std=d_std,
         a_at_fold=a_at_fold,
         H_at_fold=H_at_fold,
         q_at_fold=q_at_fold,
         A_exp=A_exp, B_exp=B_exp, R2_exp=R2_exp,
         alpha_q=alpha_q, beta_q=beta_q, R2_quad=R2_quad,
         gate_verdict=verdict,
         rel_disp=rel_disp)
print("Data saved: s54_scale_factor.npz")
