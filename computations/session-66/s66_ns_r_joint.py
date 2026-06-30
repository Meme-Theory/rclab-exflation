#!/usr/bin/env python3
"""
NS-R-JOINT-66 (W3-D) — Joint 2D Posterior for (n_s, r)
=======================================================

The framework predicts (n_s = 0.9590, r = 0.033) as a ZERO-parameter point.
This computation evaluates the 2D tension with the Planck+BK posterior
in the (n_s, r) plane.

A 1D marginal comparison (n_s only: 1.40 sigma) may understate the tension
if n_s and r are correlated in the Planck posterior.

Physics:
--------
The Planck 2018 (TT+TE+EE+lowE+lensing) + BK15 posterior for LCDM+r
is approximately a 2D Gaussian in (n_s, r) with positive correlation
rho ~ +0.3. This correlation arises because increasing r (more tensor
contribution) slightly shifts the preferred n_s upward.

We use two observational datasets:
  1. Planck 2018 + BK15: n_s = 0.9649 +/- 0.0042, r < 0.063 (95% CL)
  2. Planck + BICEP/Keck 2021: r < 0.036 (95% CL), n_s unchanged

For r, we model the posterior as a half-Gaussian (r >= 0) with the
95% upper limit determining sigma_r via the relation:
  r_{95} = sigma_r * Phi^{-1}(0.975) for a half-normal
  => sigma_r = r_{95} / (sqrt(2) * erfinv(0.95))

The Mahalanobis distance gives the number of sigma from the posterior
center. For the 2D case with 2 degrees of freedom, the CDF of chi^2(2)
gives the enclosed probability.

Gate: NS-R-JOINT-66
  PASS: 2D tension < 2 sigma
  FAIL: 2D tension > 3 sigma
  INFO: 2-3 sigma (notable tension, borderline)

NOTE: n_s = 0.9590 is a SCHEME-DEPENDENT prediction (sqrt cutoff).
W2-A showed spread = 0.164 across cutoff choices. This computation
uses the standard value; the scheme dependence is noted, not resolved.

Output:
  - s66_ns_r_joint.npz
  - s66_ns_r_joint.png

Agent: Mack-Cosmic-Bridge (Session 66, Wave 3)
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import A_s_CMB, PROVENANCE, planck_ns

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from scipy import stats, special

# ============================================================================
#  SECTION 1: Observational Parameters
# ============================================================================

# --- Framework predictions (zero free parameters) ---
ns_fw = 0.9590    # S65 BCS+one-loop, sqrt cutoff (scheme-dependent)  # (local)
r_fw  = 0.033     # S64 TENSOR-BURST-64 + TENSOR-SCALAR-64  # (local)

# --- Planck 2018 (TT+TE+EE+lowE+lensing) + BK15 ---
# Planck 2018 Paper VI, Table 5 (base_r model):
# n_s = 0.9649 +/- 0.0042 (68% CL, LCDM+r)
ns_planck = planck_ns  # canonical alias (was: = 0.9649)
ns_planck_sigma = 0.0042

# r < 0.063 (95% CL, Planck+BK15, LCDM+r)
# For a half-normal distribution (r >= 0, peaked at r=0):
# P(r < r_95) = 0.95 in the half-normal => r_95 = sigma * Phi^{-1}(0.975)
# where Phi is the standard normal CDF (since half-normal uses |Z|)
# Actually: for half-normal with scale sigma, CDF(x) = erf(x / (sigma * sqrt(2)))
# So P(r < 0.063) = 0.95 => erf(0.063 / (sigma_r * sqrt(2))) = 0.95
# => 0.063 / (sigma_r * sqrt(2)) = erfinv(0.95) = 1.38590...
# => sigma_r = 0.063 / (sqrt(2) * erfinv(0.95))
r_95_planck_bk15 = 0.063  # (local)
erfinv_095 = special.erfinv(0.95)
sigma_r_planck_bk15 = r_95_planck_bk15 / (np.sqrt(2) * erfinv_095)

# The mode of the posterior is at r = 0 (no detection).
# The mean of a half-normal is sigma * sqrt(2/pi).
# For the Gaussian approximation, we center at r_mode = 0.
r_mode_planck = 0.0  # (local)

# Correlation coefficient rho(n_s, r) from Planck chains
# Positive because more tensors shift preferred n_s up.
# Planck 2018 papers report rho ~ 0.3 for LCDM+r
rho_ns_r = 0.30  # (local)

# --- BICEP/Keck 2021 (BK18) ---
# r < 0.036 (95% CL), combined with Planck
# Same half-normal model
r_95_bk18 = 0.036  # (local)
sigma_r_bk18 = r_95_bk18 / (np.sqrt(2) * erfinv_095)

# Correlation weakens slightly with tighter r constraint; use 0.25
rho_ns_r_bk18 = 0.25  # (local)

print("=" * 70)
print("NS-R-JOINT-66: Joint 2D Posterior for (n_s, r)")
print("=" * 70)
print()

# ============================================================================
#  SECTION 2: Construct 2D Covariance Matrices
# ============================================================================

def build_cov(sigma_ns, sigma_r, rho):
    """Build 2D covariance matrix for (n_s, r)."""
    return np.array([
        [sigma_ns**2,              rho * sigma_ns * sigma_r],
        [rho * sigma_ns * sigma_r, sigma_r**2]
    ])

def mahalanobis_distance(x, mu, cov):
    """Compute Mahalanobis distance d^2 = (x-mu)^T Sigma^{-1} (x-mu)."""
    delta = x - mu
    cov_inv = np.linalg.inv(cov)
    d2 = delta @ cov_inv @ delta
    return d2

def chi2_to_sigma_2d(d2):
    """Convert chi^2 value (2 DOF) to equivalent sigma.

    For a 2D Gaussian, the enclosed probability within the d^2 contour is:
    P = 1 - exp(-d^2/2)  (chi^2 with 2 DOF)

    We convert this to an equivalent sigma for a 1D normal:
    sigma_equiv = Phi^{-1}((1 + P) / 2) where Phi is the standard normal CDF

    Alternatively, the standard approach: sigma = sqrt(d^2) gives the
    "Mahalanobis sigma" which is the radius in sigma-units.
    The probability interpretation requires the chi^2(2) CDF.
    """
    p_enclosed = 1.0 - np.exp(-d2 / 2.0)  # chi^2(2) CDF
    # Convert to equivalent 1D sigma (what fraction of a 1D Gaussian is this?)
    sigma_equiv = stats.norm.ppf((1.0 + p_enclosed) / 2.0)
    return p_enclosed, sigma_equiv

# --- Dataset 1: Planck + BK15 ---
mu_planck = np.array([ns_planck, r_mode_planck])
cov_planck = build_cov(ns_planck_sigma, sigma_r_planck_bk15, rho_ns_r)
x_fw = np.array([ns_fw, r_fw])

d2_planck = mahalanobis_distance(x_fw, mu_planck, cov_planck)
p_planck, sigma_planck = chi2_to_sigma_2d(d2_planck)

print("--- Dataset 1: Planck 2018 + BK15 ---")
print(f"  Posterior center: n_s = {ns_planck}, r = {r_mode_planck}")
print(f"  sigma(n_s) = {ns_planck_sigma}, sigma(r) = {sigma_r_planck_bk15:.5f}")
print(f"  rho(n_s, r) = {rho_ns_r}")
print(f"  Covariance matrix:")
print(f"    [{cov_planck[0,0]:.4e}  {cov_planck[0,1]:.4e}]")
print(f"    [{cov_planck[1,0]:.4e}  {cov_planck[1,1]:.4e}]")
print()
print(f"  Framework point: n_s = {ns_fw}, r = {r_fw}")
print(f"  Mahalanobis d^2 = {d2_planck:.4f}")
print(f"  sqrt(d^2) = {np.sqrt(d2_planck):.4f}")
print(f"  P(enclosed) = {p_planck:.6f}  [chi^2(2) CDF]")
print(f"  Equivalent 1D sigma = {sigma_planck:.3f}")
print()

# --- Dataset 2: Planck + BICEP/Keck 2021 (BK18) ---
cov_bk18 = build_cov(ns_planck_sigma, sigma_r_bk18, rho_ns_r_bk18)

d2_bk18 = mahalanobis_distance(x_fw, mu_planck, cov_bk18)
p_bk18, sigma_bk18 = chi2_to_sigma_2d(d2_bk18)

print("--- Dataset 2: Planck + BICEP/Keck 2021 (BK18) ---")
print(f"  Posterior center: n_s = {ns_planck}, r = {r_mode_planck}")
print(f"  sigma(n_s) = {ns_planck_sigma}, sigma(r) = {sigma_r_bk18:.5f}")
print(f"  rho(n_s, r) = {rho_ns_r_bk18}")
print(f"  Covariance matrix:")
print(f"    [{cov_bk18[0,0]:.4e}  {cov_bk18[0,1]:.4e}]")
print(f"    [{cov_bk18[1,0]:.4e}  {cov_bk18[1,1]:.4e}]")
print()
print(f"  Framework point: n_s = {ns_fw}, r = {r_fw}")
print(f"  Mahalanobis d^2 = {d2_bk18:.4f}")
print(f"  sqrt(d^2) = {np.sqrt(d2_bk18):.4f}")
print(f"  P(enclosed) = {p_bk18:.6f}  [chi^2(2) CDF]")
print(f"  Equivalent 1D sigma = {sigma_bk18:.3f}")
print()

# ============================================================================
#  SECTION 3: Cross-Checks
# ============================================================================

print("=" * 70)
print("CROSS-CHECKS")
print("=" * 70)

# Cross-check 1: 1D marginal n_s tension
delta_ns = (ns_fw - ns_planck) / ns_planck_sigma
print(f"\n1. 1D marginal n_s tension: ({ns_fw} - {ns_planck}) / {ns_planck_sigma} = {delta_ns:.3f} sigma")
print(f"   (Should match S65 value of -1.40 sigma)")

# Cross-check 2: 1D marginal r tension (half-normal)
# r_fw = 0.033 vs half-normal with sigma = sigma_r_planck_bk15
# For the half-normal, the "tension" is just r_fw / sigma_r
r_tension_planck = r_fw / sigma_r_planck_bk15
r_tension_bk18 = r_fw / sigma_r_bk18
print(f"\n2. 1D marginal r tension:")
print(f"   Planck+BK15: r/{sigma_r_planck_bk15:.5f} = {r_tension_planck:.3f} sigma (r < 0.063 at 95%)")
print(f"   Planck+BK18: r/{sigma_r_bk18:.5f} = {r_tension_bk18:.3f} sigma (r < 0.036 at 95%)")

# Cross-check 3: Zero-correlation limit
cov_nocorr = build_cov(ns_planck_sigma, sigma_r_planck_bk15, 0.0)
d2_nocorr = mahalanobis_distance(x_fw, mu_planck, cov_nocorr)
_, sigma_nocorr = chi2_to_sigma_2d(d2_nocorr)
print(f"\n3. Zero-correlation limit (rho=0, Planck+BK15):")
print(f"   d^2 = {d2_nocorr:.4f}, equiv sigma = {sigma_nocorr:.3f}")
print(f"   d^2 = (ns deviation)^2 + (r deviation)^2 = {delta_ns**2:.4f} + {r_tension_planck**2:.4f} = {delta_ns**2 + r_tension_planck**2:.4f}")

# Cross-check 4: Sensitivity to rho
print(f"\n4. Sensitivity to correlation coefficient:")
for rho_test in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
    cov_test = build_cov(ns_planck_sigma, sigma_r_planck_bk15, rho_test)
    d2_test = mahalanobis_distance(x_fw, mu_planck, cov_test)
    _, sig_test = chi2_to_sigma_2d(d2_test)
    print(f"   rho = {rho_test:.1f}: d^2 = {d2_test:.4f}, sigma = {sig_test:.3f}")

# Cross-check 5: What if n_s were at other scheme values?
print(f"\n5. Scheme dependence of n_s (from W2-A cutoff spread):")
# W2-A showed spread = 0.164 across cutoffs. sqrt cutoff gives 0.9590.
# Zeta gives n_s > 1 (blue tilt, excluded). Other cutoffs vary.
for ns_test, label in [(0.9557, "KZ (S62)"), (0.9567, "tree-level"),
                        (0.9590, "sqrt cutoff (canonical)"), (0.9649, "Planck central")]:
    x_test = np.array([ns_test, r_fw])
    d2_t = mahalanobis_distance(x_test, mu_planck, cov_planck)
    _, sig_t = chi2_to_sigma_2d(d2_t)
    print(f"   n_s = {ns_test:.4f} ({label}): 2D sigma = {sig_t:.3f}")

# ============================================================================
#  SECTION 4: Effect of Correlation Direction
# ============================================================================

print(f"\n6. Correlation sign analysis:")
print(f"   The framework prediction deviates BELOW in n_s and ABOVE in r.")
print(f"   Positive rho means the posterior extends toward (higher n_s, higher r).")
print(f"   The framework sits in the OPPOSITE corner: (lower n_s, higher r).")
print(f"   Therefore positive correlation INCREASES the tension relative to rho=0.")
# Verify:
cov_neg = build_cov(ns_planck_sigma, sigma_r_planck_bk15, -0.3)
d2_neg = mahalanobis_distance(x_fw, mu_planck, cov_neg)
_, sig_neg = chi2_to_sigma_2d(d2_neg)
print(f"   rho = -0.3: sigma = {sig_neg:.3f} (would REDUCE tension)")
print(f"   rho = +0.3: sigma = {sigma_planck:.3f} (actual: INCREASES tension)")

# ============================================================================
#  SECTION 5: Gate Verdict
# ============================================================================

print()
print("=" * 70)
print("GATE VERDICT: NS-R-JOINT-66")
print("=" * 70)

# Use the more constraining dataset (Planck+BK18)
decisive_sigma = sigma_bk18
decisive_dataset = "Planck+BK18"

# Also report Planck+BK15
print(f"\n  Planck+BK15:  2D tension = {sigma_planck:.3f} sigma  (d^2 = {d2_planck:.4f})")
print(f"  Planck+BK18:  2D tension = {sigma_bk18:.3f} sigma  (d^2 = {d2_bk18:.4f})")
print()

if decisive_sigma < 2.0:
    verdict = "PASS"
    verdict_msg = f"2D tension = {decisive_sigma:.2f} sigma < 2.0 (consistent with {decisive_dataset})"
elif decisive_sigma > 3.0:
    verdict = "FAIL"
    verdict_msg = f"2D tension = {decisive_sigma:.2f} sigma > 3.0 (serious tension with {decisive_dataset})"
else:
    verdict = "INFO"
    verdict_msg = f"2D tension = {decisive_sigma:.2f} sigma (borderline, 2-3 sigma range)"

print(f"  VERDICT: {verdict}")
print(f"  {verdict_msg}")
print()

# Report whether 2D > 1D
print(f"  1D marginal n_s only: {abs(delta_ns):.2f} sigma")
print(f"  2D joint (Planck+BK15): {sigma_planck:.2f} sigma")
print(f"  2D joint (Planck+BK18): {sigma_bk18:.2f} sigma")
if sigma_bk18 > abs(delta_ns):
    print(f"  => 2D tension ({sigma_bk18:.2f}) EXCEEDS 1D marginal ({abs(delta_ns):.2f}) by {sigma_bk18 - abs(delta_ns):.2f} sigma")
else:
    print(f"  => 2D tension ({sigma_bk18:.2f}) does NOT exceed 1D marginal ({abs(delta_ns):.2f})")

# ============================================================================
#  SECTION 6: Save Data
# ============================================================================

outpath = os.path.join(os.path.dirname(__file__), "s66_ns_r_joint.npz")
np.savez(outpath,
    # Framework
    ns_fw=ns_fw, r_fw=r_fw,
    # Planck+BK15
    ns_planck=ns_planck, ns_planck_sigma=ns_planck_sigma,
    sigma_r_planck_bk15=sigma_r_planck_bk15, r_95_planck_bk15=r_95_planck_bk15,
    rho_ns_r=rho_ns_r,
    d2_planck=d2_planck, sigma_planck=sigma_planck, p_planck=p_planck,
    # Planck+BK18
    sigma_r_bk18=sigma_r_bk18, r_95_bk18=r_95_bk18,
    rho_ns_r_bk18=rho_ns_r_bk18,
    d2_bk18=d2_bk18, sigma_bk18=sigma_bk18, p_bk18=p_bk18,
    # Cross-checks
    delta_ns_1d=delta_ns,
    r_tension_bk15=r_tension_planck, r_tension_bk18=r_tension_bk18,
    # Verdict
    verdict=verdict
)
print(f"\nData saved: {outpath}")

# ============================================================================
#  SECTION 7: Plot — 2D Contour with Framework Point
# ============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

for ax_idx, (ax, cov, sigma_val, r_95, sigma_r, rho_val, label) in enumerate([
    (axes[0], cov_planck, sigma_planck, r_95_planck_bk15, sigma_r_planck_bk15, rho_ns_r, "Planck 2018 + BK15"),
    (axes[1], cov_bk18, sigma_bk18, r_95_bk18, sigma_r_bk18, rho_ns_r_bk18, "Planck + BICEP/Keck 2021")
]):
    # Create grid
    ns_grid = np.linspace(0.94, 0.98, 300)
    r_grid = np.linspace(-0.01, 0.10, 300)
    NS, R = np.meshgrid(ns_grid, r_grid)

    # Compute 2D Gaussian (unnormalized)
    cov_inv = np.linalg.inv(cov)
    pos = np.dstack([NS - ns_planck, R - r_mode_planck])
    d2_grid = np.einsum('...i,ij,...j', pos, cov_inv, pos)

    # Mask r < 0 (half-normal truncation)
    d2_grid[R < 0] = np.inf

    # Plot contours at 1, 2, 3 sigma (chi^2 with 2 DOF: d^2 = 2.30, 6.18, 11.83)
    levels_d2 = [2.30, 6.18, 11.83]
    levels_labels = ['1$\\sigma$', '2$\\sigma$', '3$\\sigma$']
    colors = ['#2166ac', '#4393c3', '#92c5de']

    # Fill contours
    cf = ax.contourf(NS, R, d2_grid, levels=[0] + levels_d2 + [100],
                     colors=['#d1e5f0', '#92c5de', '#4393c3', '#f7f7f7'],
                     alpha=0.6)  # (local)

    # Draw contour lines
    cs = ax.contour(NS, R, d2_grid, levels=levels_d2,
                    colors=['#2166ac', '#2166ac', '#2166ac'],
                    linewidths=[1.5, 1.2, 0.8])
    ax.clabel(cs, fmt={2.30: '1$\\sigma$', 6.18: '2$\\sigma$', 11.83: '3$\\sigma$'},
              fontsize=9)

    # Framework prediction
    ax.plot(ns_fw, r_fw, '*', color='red', markersize=15, markeredgecolor='black',
            markeredgewidth=0.8, zorder=10, label=f'Framework ({sigma_val:.2f}$\\sigma$)')

    # Planck best-fit
    ax.plot(ns_planck, r_mode_planck, 'o', color='navy', markersize=8,
            markeredgecolor='black', markeredgewidth=0.8, zorder=10,
            label='Posterior mode')

    # Reference lines
    ax.axhline(y=r_95, color='gray', ls='--', alpha=0.5,
               label=f'r < {r_95} (95% CL)')

    # Slow-roll expectation band (for context)
    # Typical single-field: r = 16*eps, n_s = 1 - 6*eps + 2*eta
    # Concave potentials: r ~ 8/N * (1 - n_s) roughly
    ns_sr = np.linspace(0.94, 0.98, 100)
    # N=50-60 e-folds, phi^2: r = 8*(1-n_s)
    r_sr_phi2 = 8 * (1 - ns_sr)
    # Starobinsky/R^2: r = 12/N^2 ~ 0.003-0.004, essentially flat
    ax.plot(ns_sr, r_sr_phi2, ':', color='green', alpha=0.4, label='$\\phi^2$ (N=50-60)')
    ax.axhline(y=0.004, color='green', ls=':', alpha=0.3)
    ax.text(0.975, 0.006, 'R$^2$', fontsize=7, color='green', alpha=0.5)

    ax.set_xlabel('$n_s$', fontsize=12)
    ax.set_ylabel('$r$', fontsize=12)
    ax.set_title(f'{label}\n2D tension: {sigma_val:.2f}$\\sigma$', fontsize=11)
    ax.set_xlim(0.945, 0.980)
    ax.set_ylim(-0.005, 0.10)
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, alpha=0.2)

plt.suptitle('NS-R-JOINT-66: Framework (n$_s$, r) = (0.9590, 0.033) vs Planck 2D Posterior',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()

plotpath = os.path.join(os.path.dirname(__file__), "s66_ns_r_joint.png")
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plotpath}")

# ============================================================================
#  SECTION 8: Summary Table
# ============================================================================

print()
print("=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print()
print(f"{'Quantity':<40} {'Value':>12} {'Unit':>8}")
print("-" * 62)
print(f"{'n_s (framework)':<40} {ns_fw:>12.4f} {'':>8}")
print(f"{'n_s (Planck)':<40} {ns_planck:>12.4f} {'':>8}")
print(f"{'sigma(n_s)':<40} {ns_planck_sigma:>12.4f} {'':>8}")
print(f"{'r (framework)':<40} {r_fw:>12.4f} {'':>8}")
print(f"{'sigma(r) Planck+BK15':<40} {sigma_r_planck_bk15:>12.5f} {'':>8}")
print(f"{'sigma(r) Planck+BK18':<40} {sigma_r_bk18:>12.5f} {'':>8}")
print(f"{'rho(n_s, r) Planck+BK15':<40} {rho_ns_r:>12.2f} {'':>8}")
print(f"{'rho(n_s, r) Planck+BK18':<40} {rho_ns_r_bk18:>12.2f} {'':>8}")
print("-" * 62)
print(f"{'d^2 (Planck+BK15)':<40} {d2_planck:>12.4f} {'':>8}")
print(f"{'2D sigma (Planck+BK15)':<40} {sigma_planck:>12.3f} {'sigma':>8}")
print(f"{'d^2 (Planck+BK18)':<40} {d2_bk18:>12.4f} {'':>8}")
print(f"{'2D sigma (Planck+BK18)':<40} {sigma_bk18:>12.3f} {'sigma':>8}")
print("-" * 62)
print(f"{'1D marginal n_s only':<40} {abs(delta_ns):>12.3f} {'sigma':>8}")
print(f"{'GATE VERDICT':<40} {verdict:>12} {'':>8}")
print()
print("DONE.")
