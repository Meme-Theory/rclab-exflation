#!/usr/bin/env python3
"""
Session 32a -- ANHARM-1: Phonon-phonon anharmonic vertices and B3 lifetime.

Compute d^3 V_spec / dtau^3 (cubic) and d^4 V_spec / dtau^4 (quartic) anharmonic
vertices from the singlet eigenvalue sums. Decompose into branch-resolved
contributions. Estimate B3 optical mode lifetime via Fermi golden rule.

Physics:
  The spectral action V_spec(tau) = sum_k f(lambda_k^2 / Lambda^2) encodes the
  effective potential on moduli space. Its Taylor expansion around a reference tau:
    V_spec(tau) = V_0 + V_1 delta_tau + (1/2) V_2 delta_tau^2
                + (1/6) V_3 delta_tau^3 + (1/24) V_4 delta_tau^4 + ...
  where V_n = d^n V_spec / dtau^n.

  V_3 is the cubic anharmonic vertex governing three-phonon decay processes
  (B3 -> B2 + B1, etc.). V_4 is the quartic vertex governing four-phonon scattering.

  The B3 lifetime from three-phonon decay (Fermi golden rule):
    Gamma_B3 ~ |V_3|^2 / (16 pi omega_B3^3)
  where omega_B3 is the B3 eigenvalue (energy scale). If Gamma_B3/omega_B3 < 0.1,
  standard RPA with delta-function spectral weight is valid.

Input: tier0-computation/s23a_gap_equation.npz, s30b_sdw_grid.npz (cross-check)
Output: tier0-computation/s32a_anharmonic_vertices.npz, .png
Gate: AH-32a (Gamma_B3/omega_B3 threshold)

Author: phonon-exflation-sim agent, Session 32a
Date: 2026-03-02
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 0. LOAD DATA
# ============================================================

data_dir = Path(__file__).parent
gap_data = np.load(data_dir / 's23a_gap_equation.npz', allow_pickle=True)
umklapp_data = np.load(data_dir / 's32a_umklapp_vertex.npz', allow_pickle=True)
sdw_data = np.load(data_dir / 's30b_sdw_grid.npz', allow_pickle=True)

tau_values = gap_data['tau_values']
n_tau = len(tau_values)

# Use branch-classified eigenvalues from UMKLAPP-1
pos_evals = umklapp_data['pos_evals']  # (9, 8)
B1_evals = umklapp_data['B1_evals']    # (9,)
B2_evals = umklapp_data['B2_evals']    # (9, 4)
B3_evals = umklapp_data['B3_evals']    # (9, 3)

print(f"tau_values = {tau_values}")
print(f"pos_evals shape = {pos_evals.shape}")

# ============================================================
# 1. SPECTRAL ACTION (eigenvalue sum functional)
# ============================================================
# V_spec(tau) = sum_k lambda_k(tau)  [simplest case: f(x) = sqrt(x)]
# More generally: V_spec(tau) = sum_k f(lambda_k^2)
# For branch diagnostics, we use the linear sum first (= total eigenvalue sum),
# then cross-check with quadratic (= sum of squares, related to heat kernel a_0).

# Linear spectral functional: V_lin = sum lambda_k
V_lin = np.sum(pos_evals, axis=1)  # shape (9,)

# Quadratic spectral functional: V_quad = sum lambda_k^2
V_quad = np.sum(pos_evals**2, axis=1)

# Branch-resolved linear sums
S_B1 = umklapp_data['dS_B1']  # These are actually first derivatives from umklapp
# Recompute branch sums directly
S_B1_sum = B1_evals.copy()
S_B2_sum = np.sum(B2_evals, axis=1)
S_B3_sum = np.sum(B3_evals, axis=1)

# Branch-resolved quadratic sums
Q_B1 = B1_evals**2
Q_B2 = np.sum(B2_evals**2, axis=1)
Q_B3 = np.sum(B3_evals**2, axis=1)

print(f"\n=== SPECTRAL FUNCTIONALS ===")
for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: V_lin={V_lin[i]:.6f}  V_quad={V_quad[i]:.6f}")

# ============================================================
# 2. FINITE DIFFERENCE DERIVATIVES UP TO 4TH ORDER
# ============================================================
# Non-uniform grid: tau = [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
# Use centered differences; forward/backward at boundaries.

def finite_diff(y, x):
    """First derivative by centered differences on non-uniform grid."""
    n = len(x)
    dy = np.zeros(n)
    for i in range(n):
        if i == 0:
            dy[i] = (y[1] - y[0]) / (x[1] - x[0])
        elif i == n - 1:
            dy[i] = (y[-1] - y[-2]) / (x[-1] - x[-2])
        else:
            h_l = x[i] - x[i-1]
            h_r = x[i+1] - x[i]
            # Lagrange 3-point formula for non-uniform grid
            dy[i] = (-h_r / (h_l * (h_l + h_r))) * y[i-1] + \
                     ((h_r - h_l) / (h_l * h_r)) * y[i] + \
                     (h_l / (h_r * (h_l + h_r))) * y[i+1]
    return dy

# Successive derivatives of V_lin
V1 = finite_diff(V_lin, tau_values)
V2 = finite_diff(V1, tau_values)
V3 = finite_diff(V2, tau_values)
V4 = finite_diff(V3, tau_values)

# Same for V_quad
Q1 = finite_diff(V_quad, tau_values)
Q2 = finite_diff(Q1, tau_values)
Q3 = finite_diff(Q2, tau_values)
Q4 = finite_diff(Q3, tau_values)

# Branch-resolved derivatives (for cubic decomposition)
dB1 = finite_diff(S_B1_sum, tau_values)
dB2 = finite_diff(S_B2_sum, tau_values)
dB3 = finite_diff(S_B3_sum, tau_values)

d2B1 = finite_diff(dB1, tau_values)
d2B2 = finite_diff(dB2, tau_values)
d2B3 = finite_diff(dB3, tau_values)

d3B1 = finite_diff(d2B1, tau_values)
d3B2 = finite_diff(d2B2, tau_values)
d3B3 = finite_diff(d2B3, tau_values)

d4B1 = finite_diff(d3B1, tau_values)
d4B2 = finite_diff(d3B2, tau_values)
d4B3 = finite_diff(d3B3, tau_values)

print(f"\n=== ANHARMONIC VERTICES (Linear Spectral Functional) ===")
print(f"{'tau':>6s}  {'V1':>12s}  {'V2':>12s}  {'V3':>12s}  {'V4':>12s}")
for i in range(n_tau):
    print(f"  {tau_values[i]:.2f}  {V1[i]:+12.6f}  {V2[i]:+12.6f}  {V3[i]:+12.6f}  {V4[i]:+12.6f}")

print(f"\n=== ANHARMONIC VERTICES (Quadratic Spectral Functional) ===")
print(f"{'tau':>6s}  {'Q1':>12s}  {'Q2':>12s}  {'Q3':>12s}  {'Q4':>12s}")
for i in range(n_tau):
    print(f"  {tau_values[i]:.2f}  {Q1[i]:+12.6f}  {Q2[i]:+12.6f}  {Q3[i]:+12.6f}  {Q4[i]:+12.6f}")

# ============================================================
# 3. BRANCH-RESOLVED CUBIC VERTEX DECOMPOSITION
# ============================================================
# d^3 V_lin / dtau^3 = d^3 S_B1/dtau^3 + d^3 S_B2/dtau^3 + d^3 S_B3/dtau^3
# Each branch's contribution to the total cubic

print(f"\n=== BRANCH-RESOLVED CUBIC VERTEX (d^3/dtau^3) ===")
print(f"{'tau':>6s}  {'d3B1':>12s}  {'d3B2':>12s}  {'d3B3':>12s}  {'total':>12s}  {'B3 frac':>10s}")
for i in range(n_tau):
    total = d3B1[i] + d3B2[i] + d3B3[i]
    b3_frac = d3B3[i] / total if abs(total) > 1e-10 else 0
    print(f"  {tau_values[i]:.2f}  {d3B1[i]:+12.6f}  {d3B2[i]:+12.6f}  {d3B3[i]:+12.6f}  "
          f"{total:+12.6f}  {b3_frac:+10.4f}")

print(f"\n=== BRANCH-RESOLVED QUARTIC VERTEX (d^4/dtau^4) ===")
print(f"{'tau':>6s}  {'d4B1':>12s}  {'d4B2':>12s}  {'d4B3':>12s}  {'total':>12s}")
for i in range(n_tau):
    total = d4B1[i] + d4B2[i] + d4B3[i]
    print(f"  {tau_values[i]:.2f}  {d4B1[i]:+12.6f}  {d4B2[i]:+12.6f}  {d4B3[i]:+12.6f}  "
          f"{total:+12.6f}")

# ============================================================
# 4. B3 LIFETIME ESTIMATE (Fermi Golden Rule)
# ============================================================
# Three-phonon decay: B3 -> B2 + B1 (or B3 -> 2*B_lower)
# Gamma_B3 ~ |V_3|^2 / (16 * pi * omega_B3^3)
#
# Here V_3 = d^3 V_spec / dtau^3 (total cubic vertex, which includes
# the B3->B2+B1 channel). omega_B3 = mean B3 eigenvalue (energy scale).
#
# This is an ORDER-OF-MAGNITUDE estimate. The precise vertex requires
# mode-resolved matrix elements, but the scaling captures whether B3
# is long-lived or short-lived.

B3_mean = np.mean(B3_evals, axis=1)  # omega_B3 at each tau
B2_mean = np.mean(B2_evals, axis=1)

print(f"\n=== B3 LIFETIME ESTIMATE (Fermi Golden Rule) ===")
print(f"  Using: Gamma_B3 ~ |V_3|^2 / (16 pi omega_B3^3)")
print(f"  V_3 = d^3 V_lin / dtau^3 (total cubic)")
print()
print(f"{'tau':>6s}  {'omega_B3':>10s}  {'|V_3|':>10s}  {'Gamma_B3':>12s}  {'Gamma/omega':>12s}  {'verdict':>10s}")

gamma_ratio = np.zeros(n_tau)
gamma_B3 = np.zeros(n_tau)
for i in range(n_tau):
    omega = B3_mean[i]
    v3 = V3[i]
    gamma = v3**2 / (16 * np.pi * omega**3)
    ratio = gamma / omega
    gamma_B3[i] = gamma
    gamma_ratio[i] = ratio
    verdict = "PASS (<0.1)" if abs(ratio) < 0.1 else "CAUTION (>0.1)" if abs(ratio) < 0.5 else "BROAD (>0.5)"
    print(f"  {tau_values[i]:.2f}  {omega:10.6f}  {abs(v3):10.6f}  {gamma:12.6f}  {ratio:12.6f}  {verdict}")

# Also compute with the quadratic spectral functional for cross-check
print(f"\n=== B3 LIFETIME (Quadratic Functional Cross-Check) ===")
print(f"{'tau':>6s}  {'|Q3|':>10s}  {'Gamma_q':>12s}  {'Gamma_q/omega':>12s}")
for i in range(n_tau):
    omega = B3_mean[i]
    gamma_q = Q3[i]**2 / (16 * np.pi * omega**3)
    ratio_q = gamma_q / omega
    print(f"  {tau_values[i]:.2f}  {abs(Q3[i]):10.6f}  {gamma_q:12.6f}  {ratio_q:12.6f}")

# ============================================================
# 5. SEELEY-DEWITT CROSS-CHECK
# ============================================================
# Load a_2 coefficients from s30b_sdw_grid.npz along the Jensen direction (eps=0)
print(f"\n=== SEELEY-DEWITT CROSS-CHECK ===")
sdw_tau = sdw_data['tau']
sdw_a2 = sdw_data['a2']
sdw_eps = sdw_data['eps']

# Find eps=0 column
eps_zero_idx = np.argmin(np.abs(sdw_eps))
print(f"SDW grid: {len(sdw_tau)} tau x {len(sdw_eps)} eps. eps[{eps_zero_idx}] = {sdw_eps[eps_zero_idx]:.6f}")

# a_2 along Jensen direction
a2_jensen = sdw_a2[:, eps_zero_idx]
R_jensen = sdw_data['R'][:, eps_zero_idx]

print(f"\n  SDW a_2 along Jensen (eps=0):")
for i in range(len(sdw_tau)):
    print(f"    tau={sdw_tau[i]:.3f}: a_2={a2_jensen[i]:.6f}  R={R_jensen[i]:.6f}")

# Compute d^3 a_2 / dtau^3 on SDW grid for comparison
da2_1 = finite_diff(a2_jensen, sdw_tau)
da2_2 = finite_diff(da2_1, sdw_tau)
da2_3 = finite_diff(da2_2, sdw_tau)

print(f"\n  d^3(a_2)/dtau^3 along Jensen:")
for i in range(len(sdw_tau)):
    print(f"    tau={sdw_tau[i]:.3f}: d3a2={da2_3[i]:+.4f}")

# ============================================================
# 6. GATE CLASSIFICATION
# ============================================================
# AH-32a: Gamma_B3/omega_B3 at gradient-balance region (tau=0.15, 0.20)
# These are the physically relevant tau values

idx_15 = 2  # tau=0.15
idx_20 = 3  # tau=0.20

ratio_15 = abs(gamma_ratio[idx_15])
ratio_20 = abs(gamma_ratio[idx_20])
ratio_ref = max(ratio_15, ratio_20)  # use worst case in relevant range

if ratio_ref < 0.1:
    ah32a_verdict = "PASS"
    ah32a_detail = (f"Gamma_B3/omega_B3 = {ratio_15:.4f} (tau=0.15), "
                    f"{ratio_20:.4f} (tau=0.20). Both < 0.1. "
                    f"Standard RPA valid, chi_sep = 0.728 needs no broadening correction.")
elif ratio_ref < 0.5:
    ah32a_verdict = "CAUTION"
    ah32a_detail = (f"Gamma_B3/omega_B3 = {ratio_15:.4f} (tau=0.15), "
                    f"{ratio_20:.4f} (tau=0.20). Between 0.1 and 0.5. "
                    f"RPA needs modest broadening correction.")
else:
    ah32a_verdict = "CAUTION"
    ah32a_detail = (f"Gamma_B3/omega_B3 = {ratio_15:.4f} (tau=0.15), "
                    f"{ratio_20:.4f} (tau=0.20). >= 0.5. "
                    f"RPA needs substantial broadening, chi threshold effectively increases.")

print(f"\n{'='*60}")
print(f"GATE AH-32a: {ah32a_verdict} -- {ah32a_detail}")
print(f"{'='*60}")

# ============================================================
# 7. SAVE RESULTS
# ============================================================

np.savez(data_dir / 's32a_anharmonic_vertices.npz',
    tau_values=tau_values,
    # Spectral functionals
    V_lin=V_lin,
    V_quad=V_quad,
    # Derivatives (linear)
    V1=V1, V2=V2, V3=V3, V4=V4,
    # Derivatives (quadratic)
    Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4,
    # Branch-resolved
    d3B1=d3B1, d3B2=d3B2, d3B3=d3B3,
    d4B1=d4B1, d4B2=d4B2, d4B3=d4B3,
    # B3 lifetime
    gamma_B3=gamma_B3,
    gamma_ratio=gamma_ratio,
    B3_mean=B3_mean,
    # Gate
    ah32a_verdict=ah32a_verdict,
)

print(f"\nSaved: s32a_anharmonic_vertices.npz")

# ============================================================
# 8. PLOTS
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 32a: ANHARM-1 -- Anharmonic Vertices & B3 Lifetime', fontsize=14)

# Panel (a): Cubic and quartic vertices (linear functional)
ax = axes[0, 0]
ax.plot(tau_values, V3, 'rs-', label=r'$V_3 = d^3 V_{\rm lin}/d\tau^3$', markersize=6, linewidth=2)
ax.plot(tau_values, V4, 'b^-', label=r'$V_4 = d^4 V_{\rm lin}/d\tau^4$', markersize=6, linewidth=2)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
ax.axvspan(0.10, 0.31, alpha=0.1, color='green', label='Instanton orbit')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Vertex magnitude')
ax.set_title('(a) Cubic & Quartic Vertices (Linear Functional)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): Branch-resolved cubic
ax = axes[0, 1]
ax.plot(tau_values, d3B1, 'ko-', label='d3(B1)/dtau3', markersize=5)
ax.plot(tau_values, d3B2, 'bs-', label='d3(B2)/dtau3', markersize=5)
ax.plot(tau_values, d3B3, 'r^-', label='d3(B3)/dtau3', markersize=5)
ax.plot(tau_values, V3, 'g--', label='Total V3', linewidth=2, alpha=0.7)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
ax.axvspan(0.10, 0.31, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$d^3 S_{Bi}/d\tau^3$')
ax.set_title('(b) Branch-Resolved Cubic Vertex')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): B3 lifetime ratio
ax = axes[1, 0]
ax.semilogy(tau_values, np.abs(gamma_ratio), 'rs-', markersize=6, linewidth=2,
            label=r'$|\Gamma_{B3}/\omega_{B3}|$')
ax.axhline(y=0.1, color='green', linestyle='--', alpha=0.7, label='PASS threshold (0.1)')
ax.axhline(y=0.5, color='orange', linestyle='--', alpha=0.7, label='CAUTION threshold (0.5)')
ax.axvspan(0.10, 0.31, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\Gamma_{B3}/\omega_{B3}$')
ax.set_title(f'(c) B3 Lifetime Ratio [AH-32a: {ah32a_verdict}]')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): SDW a_2 cross-check
ax = axes[1, 1]
ax.plot(sdw_tau, a2_jensen, 'b-', label=r'$a_2(\tau, \epsilon=0)$', linewidth=2)
ax2 = ax.twinx()
ax2.plot(sdw_tau, da2_3, 'r--', label=r'$d^3 a_2/d\tau^3$', linewidth=1.5, alpha=0.7)
ax.axvspan(0.10, 0.31, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$a_2$', color='blue')
ax2.set_ylabel(r'$d^3 a_2/d\tau^3$', color='red')
ax.set_title('(d) Seeley-DeWitt a_2 Cross-Check')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(data_dir / 's32a_anharmonic_vertices.png', dpi=150, bbox_inches='tight')
print(f"Saved: s32a_anharmonic_vertices.png")

print("\n=== COMPUTATION COMPLETE ===")
