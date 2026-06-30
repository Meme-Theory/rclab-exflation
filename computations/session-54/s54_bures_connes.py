#!/usr/bin/env python3
"""
s54_bures_connes.py — BURES-CONNES-54
Information Geometry vs Spectral Geometry on SU(3) moduli space.

Computes:
  1. Bures distance d_B(tau_i, tau_j) = arccos|<gs(tau_i)|gs(tau_j)>|
     from Richardson ED ground states (N_pair=1, 8D pair basis).
  2. Connes moduli distance proxy: |<d_D>(tau_i) - <d_D>(tau_j)|
     from Voronoi-lattice spectral distance (32 cells).
  3. Comparison: d_B vs d_Connes for all (i,j) pairs.
  4. Quantum Fisher information F_Q(tau) vs Connes metric g_C(tau).

Gate: BURES-CONNES-54 (INFO)
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Load data ──────────────────────────────────────────────────────
ROOT = Path(__file__).parent
ed = np.load(ROOT / 's54_ed_sweep.npz', allow_pickle=True)
cl = np.load(ROOT / 's54_connes_latt.npz', allow_pickle=True)

tau_ed = ed['tau_values']       # (50,)
psi_ed = ed['eigenstates']      # (50, 8) — ground state vectors in pair basis
tau_con = cl['tau_values']      # (10,)
mean_d = cl['mean_distance']    # (10,) — <d_D>(tau)

# Map Connes tau to ED indices (exact match verified)
ed_idx = np.array([np.argmin(np.abs(tau_ed - tc)) for tc in tau_con])
assert np.allclose(tau_ed[ed_idx], tau_con, atol=1e-12), "Tau mismatch"

# Extract ground states at Connes tau points
psi_at_con = psi_ed[ed_idx]  # (10, 8)

# ─── 1. Full Bures distance matrix ─────────────────────────────────
N_con = len(tau_con)
overlap_matrix = np.zeros((N_con, N_con))
bures_matrix = np.zeros((N_con, N_con))

for i in range(N_con):
    for j in range(N_con):
        ov = np.abs(np.dot(psi_at_con[i], psi_at_con[j]))
        overlap_matrix[i, j] = ov
        bures_matrix[i, j] = np.arccos(np.clip(ov, -1.0, 1.0))

# ─── 2. Connes moduli distance matrix ──────────────────────────────
# Proxy: |<d_D>(tau_i) - <d_D>(tau_j)|
# This is the 1D metric on moduli space induced by the mean Connes distance
connes_mod_matrix = np.zeros((N_con, N_con))
for i in range(N_con):
    for j in range(N_con):
        connes_mod_matrix[i, j] = np.abs(mean_d[i] - mean_d[j])

# ─── 3. Extract upper-triangle pairs for regression ────────────────
d_B_pairs = []
d_C_pairs = []
pair_labels = []
for i in range(N_con):
    for j in range(i+1, N_con):
        d_B_pairs.append(bures_matrix[i, j])
        d_C_pairs.append(connes_mod_matrix[i, j])
        pair_labels.append((i, j))

d_B = np.array(d_B_pairs)
d_C = np.array(d_C_pairs)
N_pairs = len(d_B)

# ─── 4. Linear fit: d_B = alpha * d_C + beta ───────────────────────
def linear(x, a, b):
    return a * x + b

popt, pcov = curve_fit(linear, d_C, d_B)
alpha, beta = popt
perr = np.sqrt(np.diag(pcov))
alpha_err, beta_err = perr

# R^2
d_B_pred = linear(d_C, alpha, beta)
ss_res = np.sum((d_B - d_B_pred)**2)
ss_tot = np.sum((d_B - d_B.mean())**2)
R2 = 1.0 - ss_res / ss_tot

# Also fit pure proportional: d_B = alpha_0 * d_C (no intercept)
alpha_0 = np.sum(d_B * d_C) / np.sum(d_C**2)
d_B_pred_0 = alpha_0 * d_C
ss_res_0 = np.sum((d_B - d_B_pred_0)**2)
R2_0 = 1.0 - ss_res_0 / ss_tot

# Residuals
resid = d_B - d_B_pred
resid_0 = d_B - d_B_pred_0

print("=" * 70)
print("BURES-CONNES-54: Information Geometry vs Spectral Geometry")
print("=" * 70)
print()
print(f"N_pairs = {N_pairs} (from {N_con} tau points)")
print()
print("--- Linear fit: d_B = alpha * d_C + beta ---")
print(f"  alpha = {alpha:.6f} +/- {alpha_err:.6f}")
print(f"  beta  = {beta:.6f} +/- {beta_err:.6f}")
print(f"  R^2   = {R2:.8f}")
print(f"  max|resid| = {np.max(np.abs(resid)):.6f}")
print(f"  RMS resid   = {np.sqrt(np.mean(resid**2)):.6f}")
print()
print("--- Proportional fit: d_B = alpha_0 * d_C ---")
print(f"  alpha_0 = {alpha_0:.6f}")
print(f"  R^2_0   = {R2_0:.8f}")
print(f"  max|resid| = {np.max(np.abs(resid_0)):.6f}")
print(f"  RMS resid   = {np.sqrt(np.mean(resid_0**2)):.6f}")
print()

# ─── 5. Quantum Fisher information F_Q and Connes metric ───────────
# F_Q from full ED sweep (adjacent overlaps)
dtau = tau_ed[1] - tau_ed[0]
overlaps_adj = np.array([np.abs(np.dot(psi_ed[i], psi_ed[i+1]))
                         for i in range(len(tau_ed)-1)])
# F_Q = 4(1 - |<psi|psi'>|^2) / dtau^2
F_Q_full = 4.0 * (1.0 - overlaps_adj**2) / dtau**2
tau_FQ = 0.5 * (tau_ed[:-1] + tau_ed[1:])  # midpoints

# Bures metric: g_B = F_Q / 4 = (d_B/dtau)^2 for infinitesimal dtau
# Actually d_B = arccos(|<>|), so (d_B/dtau)^2 = (1-|<>|^2)/dtau^2/(1-|<>|^2) ...
# More precisely: for small dtau, d_B ~ sqrt(1-|<>|^2) ~ sqrt(F_Q)*dtau/2
# So g_B = (dd_B/dtau)^2 = F_Q/4
g_B = F_Q_full / 4.0

# Connes metric at the 10 overlap points: g_C = (d<d_D>/dtau)^2
# Use central differences where possible, forward/backward at edges
d_mean_d_dtau = np.gradient(mean_d, tau_con)
g_C = d_mean_d_dtau**2

# F_Q at Connes tau points (interpolate from full sweep)
F_Q_at_con = np.interp(tau_con, tau_FQ, F_Q_full)
g_B_at_con = F_Q_at_con / 4.0

# Metric ratio: g_B / g_C
metric_ratio = g_B_at_con / g_C

print("--- Metric comparison: g_B(tau) vs g_C(tau) ---")
print(f"  {'tau':>8s}  {'F_Q':>10s}  {'g_B':>10s}  {'g_C':>10s}  {'g_B/g_C':>10s}")
for i in range(N_con):
    print(f"  {tau_con[i]:8.4f}  {F_Q_at_con[i]:10.4f}  {g_B_at_con[i]:10.6f}  {g_C[i]:10.4f}  {metric_ratio[i]:10.6f}")

mean_ratio = np.mean(metric_ratio)
std_ratio = np.std(metric_ratio)
cv_ratio = std_ratio / mean_ratio  # coefficient of variation
print()
print(f"  Mean g_B/g_C = {mean_ratio:.6f}")
print(f"  Std  g_B/g_C = {std_ratio:.6f}")
print(f"  CV(g_B/g_C)  = {cv_ratio:.4f} ({cv_ratio*100:.1f}%)")
print()

# ─── 6. Check if ratio is tau-independent (Martinetti-Mercati) ─────
# If g_B = const * g_C, then the two metrics are conformally equivalent
# with constant conformal factor => they define the same geodesics on moduli space

# Test: is d_B/d_C constant for all pairs?
ratio_pairs = d_B / d_C
print("--- Pair-wise ratio d_B/d_C ---")
print(f"  min  = {ratio_pairs.min():.6f}")
print(f"  max  = {ratio_pairs.max():.6f}")
print(f"  mean = {ratio_pairs.mean():.6f}")
print(f"  std  = {ratio_pairs.std():.6f}")
print(f"  CV   = {ratio_pairs.std()/ratio_pairs.mean():.4f} ({ratio_pairs.std()/ratio_pairs.mean()*100:.1f}%)")
print()

# Systematic trend: ratio vs d_C
# If Martinetti-Mercati holds exactly, ratio should be constant
# If there's a nonlinear relationship, ratio will vary

# ─── 7. Nonlinear alternatives ─────────────────────────────────────
# Test power law: d_B = A * d_C^gamma
def power_law(x, A, gamma):
    return A * np.power(x, gamma)

popt_pl, pcov_pl = curve_fit(power_law, d_C, d_B, p0=[alpha_0, 1.0])
A_pl, gamma_pl = popt_pl
d_B_pred_pl = power_law(d_C, A_pl, gamma_pl)
ss_res_pl = np.sum((d_B - d_B_pred_pl)**2)
R2_pl = 1.0 - ss_res_pl / ss_tot

print("--- Power-law fit: d_B = A * d_C^gamma ---")
print(f"  A     = {A_pl:.6f}")
print(f"  gamma = {gamma_pl:.6f}")
print(f"  R^2   = {R2_pl:.8f}")
print()

# ─── 8. Integrated Bures distance along tau path ───────────────────
# d_B^path(tau_i, tau_j) = integral from tau_i to tau_j of sqrt(g_B) dtau
# = integral of sqrt(F_Q)/2 dtau
# Using trapezoidal rule on full 50-point mesh

sqrt_FQ_half = np.sqrt(F_Q_full) / 2.0
# Cumulative integral
bures_cumul = np.zeros(len(tau_ed))
for i in range(1, len(tau_ed)):
    # idx in F_Q array: i-1 corresponds to interval [i-1, i]
    bures_cumul[i] = bures_cumul[i-1] + sqrt_FQ_half[i-1] * dtau

# Extract at Connes tau points
bures_path_at_con = bures_cumul[ed_idx]

# Pairwise geodesic Bures distances
d_B_path = []
for i in range(N_con):
    for j in range(i+1, N_con):
        d_B_path.append(np.abs(bures_path_at_con[j] - bures_path_at_con[i]))
d_B_path = np.array(d_B_path)

# Compare geodesic Bures to chord Bures
chord_vs_path_ratio = d_B / d_B_path
print("--- Geodesic vs chord Bures comparison ---")
print(f"  d_B(chord) / d_B(geodesic):")
print(f"    min  = {chord_vs_path_ratio.min():.6f}")
print(f"    max  = {chord_vs_path_ratio.max():.6f}")
print(f"    mean = {chord_vs_path_ratio.mean():.6f}")
print()

# Now fit geodesic Bures vs Connes
popt_geo, pcov_geo = curve_fit(linear, d_C, d_B_path)
alpha_geo, beta_geo = popt_geo
d_B_path_pred = linear(d_C, alpha_geo, beta_geo)
ss_res_geo = np.sum((d_B_path - d_B_path_pred)**2)
ss_tot_geo = np.sum((d_B_path - d_B_path.mean())**2)
R2_geo = 1.0 - ss_res_geo / ss_tot_geo

# Proportional fit for geodesic
alpha_geo_0 = np.sum(d_B_path * d_C) / np.sum(d_C**2)
d_B_path_pred_0 = alpha_geo_0 * d_C
ss_res_geo_0 = np.sum((d_B_path - d_B_path_pred_0)**2)
R2_geo_0 = 1.0 - ss_res_geo_0 / ss_tot_geo

print("--- Geodesic Bures vs Connes (linear) ---")
print(f"  alpha = {alpha_geo:.6f} +/- {np.sqrt(pcov_geo[0,0]):.6f}")
print(f"  beta  = {beta_geo:.6f} +/- {np.sqrt(pcov_geo[1,1]):.6f}")
print(f"  R^2   = {R2_geo:.8f}")
print()
print("--- Geodesic Bures vs Connes (proportional) ---")
print(f"  alpha_0 = {alpha_geo_0:.6f}")
print(f"  R^2_0   = {R2_geo_0:.8f}")
print()

# ─── 9. Dimensionful comparison ────────────────────────────────────
print("--- Scale analysis ---")
print(f"  Bures distance range: [{d_B.min():.4f}, {d_B.max():.4f}]")
print(f"  Connes distance range: [{d_C.min():.4f}, {d_C.max():.4f}]")
print(f"  Scale ratio alpha: {alpha:.4f} (Bures radians per Connes M_KK^-1)")
print(f"  Bures total (tau=0 to 0.347): {bures_cumul[ed_idx[-1]]:.4f} rad")
print(f"  Connes total: {mean_d[-1] - mean_d[0]:.4f} M_KK^-1")
print(f"  Path ratio: {bures_cumul[ed_idx[-1]] / (mean_d[-1] - mean_d[0]):.6f}")
print()

# ─── 10. Functional relationship test ──────────────────────────────
# Since <d_D>(tau) ~ exp(3.5*tau), test if d_B = f(tau) also exponential
# Bures from tau=0: d_B(0,tau)
d_B_from_0 = bures_matrix[0, :]  # chord distances from tau=0
bures_path_from_0 = bures_path_at_con  # geodesic from tau=0

print("--- d_B(0,tau) and <d_D>(tau) vs tau ---")
print(f"  {'tau':>8s}  {'d_B_chord':>10s}  {'d_B_geod':>10s}  {'<d_D>':>10s}  {'dB_chord/dD':>12s}")
for i in range(N_con):
    if i > 0:
        r = d_B_from_0[i] / (mean_d[i] - mean_d[0]) if mean_d[i] != mean_d[0] else 0
        print(f"  {tau_con[i]:8.4f}  {d_B_from_0[i]:10.6f}  {bures_path_from_0[i]:10.6f}  {mean_d[i]:10.6f}  {r:12.6f}")
    else:
        print(f"  {tau_con[i]:8.4f}  {d_B_from_0[i]:10.6f}  {bures_path_from_0[i]:10.6f}  {mean_d[i]:10.6f}  {'---':>12s}")

print()

# ─── Summary ────────────────────────────────────────────────────────
proportional = R2_0 > 0.99 and ratio_pairs.std()/ratio_pairs.mean() < 0.05
conformal = cv_ratio < 0.10

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"  Chord Bures vs Connes:")
print(f"    Linear:       d_B = {alpha:.4f}*d_C + {beta:.4f},  R^2 = {R2:.6f}")
print(f"    Proportional: d_B = {alpha_0:.4f}*d_C,           R^2 = {R2_0:.6f}")
print(f"    Power-law:    d_B = {A_pl:.4f}*d_C^{gamma_pl:.4f},       R^2 = {R2_pl:.6f}")
print()
print(f"  Geodesic Bures vs Connes:")
print(f"    Linear:       d_B = {alpha_geo:.4f}*d_C + {beta_geo:.4f},  R^2 = {R2_geo:.6f}")
print(f"    Proportional: d_B = {alpha_geo_0:.4f}*d_C,           R^2 = {R2_geo_0:.6f}")
print()
print(f"  Metric comparison:")
print(f"    g_B/g_C: mean={mean_ratio:.6f}, CV={cv_ratio:.4f}")
print(f"    Constant conformal factor: {'YES' if conformal else 'NO'} (CV<10%: {conformal})")
print()
print(f"  Martinetti-Mercati conjecture:")
martinetti = "VERIFIED (approximate)" if (R2 > 0.99 and conformal) else \
             "PARTIAL (high R^2 but variable ratio)" if R2 > 0.99 else \
             "NOT VERIFIED"
print(f"    Status: {martinetti}")
print(f"    The two metrics on 1D moduli space are {'approximately proportional' if R2 > 0.99 else 'not proportional'}.")
if gamma_pl < 0.95 or gamma_pl > 1.05:
    print(f"    Power-law exponent gamma={gamma_pl:.4f} deviates from 1 by {abs(gamma_pl-1)*100:.1f}%.")
print()

# ─── PLOTS ──────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Panel (a): d_B vs d_C scatter + fits
ax = axes[0, 0]
ax.scatter(d_C, d_B, s=12, alpha=0.6, c='steelblue', label='data')
d_C_fit = np.linspace(0, d_C.max()*1.05, 200)
ax.plot(d_C_fit, linear(d_C_fit, alpha, beta), 'r-', lw=1.5,
        label=f'linear: R²={R2:.4f}')
ax.plot(d_C_fit, alpha_0 * d_C_fit, 'g--', lw=1.5,
        label=f'proportional: R²={R2_0:.4f}')
ax.plot(d_C_fit, power_law(d_C_fit, A_pl, gamma_pl), 'k:', lw=1.5,
        label=f'power γ={gamma_pl:.3f}: R²={R2_pl:.4f}')
ax.set_xlabel(r'$\Delta\langle d_D\rangle$ (Connes moduli proxy)', fontsize=12)
ax.set_ylabel(r'$d_{\rm Bures}$ (arccos overlap)', fontsize=12)
ax.set_title('(a) Chord Bures vs Connes Distance', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (b): Metrics g_B and g_C vs tau
ax = axes[0, 1]
ax.plot(tau_FQ, g_B, 'b-', lw=1.2, alpha=0.5, label=r'$g_B = F_Q/4$ (full ED)')
ax.plot(tau_con, g_B_at_con, 'bo', ms=6, label=r'$g_B$ at Connes $\tau$')
# Scale g_C by mean ratio for visual comparison
ax.plot(tau_con, g_C, 'rs', ms=6, label=r'$g_C = (d\langle d_D\rangle/d\tau)^2$')
ax.plot(tau_con, g_C * mean_ratio, 'r--', lw=1.5, alpha=0.7,
        label=rf'$g_C \times {mean_ratio:.4f}$')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel('Metric tensor component', fontsize=12)
ax.set_title('(b) Bures metric vs Connes metric', fontsize=13)
ax.axvline(x=0.194, color='gray', ls=':', alpha=0.5, label='fold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Metric ratio g_B/g_C vs tau
ax = axes[1, 0]
ax.plot(tau_con, metric_ratio, 'ko-', ms=8, lw=2)
ax.axhline(y=mean_ratio, color='r', ls='--', lw=1.5,
           label=rf'mean = {mean_ratio:.4f}')
ax.fill_between(tau_con, mean_ratio - std_ratio, mean_ratio + std_ratio,
                alpha=0.2, color='red')  # (local)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$g_B(\tau) / g_C(\tau)$', fontsize=12)
ax.set_title(f'(c) Metric ratio (CV = {cv_ratio*100:.1f}%)', fontsize=13)
ax.axvline(x=0.194, color='gray', ls=':', alpha=0.5, label='fold')
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel (d): Geodesic Bures vs Connes
ax = axes[1, 1]
ax.scatter(d_C, d_B_path, s=12, alpha=0.6, c='darkorange', label='geodesic Bures')
ax.plot(d_C_fit, linear(d_C_fit, alpha_geo, beta_geo), 'r-', lw=1.5,
        label=f'linear: R²={R2_geo:.4f}')
ax.plot(d_C_fit, alpha_geo_0 * d_C_fit, 'g--', lw=1.5,
        label=f'proportional: R²={R2_geo_0:.4f}')
ax.set_xlabel(r'$\Delta\langle d_D\rangle$ (Connes moduli proxy)', fontsize=12)
ax.set_ylabel(r'$d_{\rm Bures}^{\rm geod}$', fontsize=12)
ax.set_title('(d) Geodesic Bures vs Connes Distance', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.suptitle('BURES-CONNES-54: Information Geometry = Spectral Geometry?',
             fontsize=15, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(ROOT / 's54_bures_connes.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved: {ROOT / 's54_bures_connes.png'}")

# ─── Gate verdict ───────────────────────────────────────────────────
print()
print("=" * 70)
print("GATE: BURES-CONNES-54")
print(f"  Verdict: INFO")
print(f"  alpha = {alpha:.6f} (linear), alpha_0 = {alpha_0:.6f} (proportional)")
print(f"  R^2 = {R2:.6f} (linear), R^2_0 = {R2_0:.6f} (proportional)")
print(f"  gamma_power = {gamma_pl:.6f}")
print(f"  g_B/g_C: mean={mean_ratio:.6f}, CV={cv_ratio:.4f}")
print(f"  Martinetti-Mercati: {martinetti}")
print("=" * 70)
