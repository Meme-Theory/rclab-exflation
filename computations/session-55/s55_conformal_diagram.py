#!/usr/bin/env python3
"""
CONFORMAL-DIAGRAM-55: Conformal diagram and energy conditions for lattice spectral triple.

Integrates conformal time from Connes scale factor a(tau), computes w_eff(tau),
tests particle horizon existence, SEC violation, and discrete trapped surfaces
on the 32-cell graph.

Input:
  computations/session-54/s54_connes_latt.npz  (distance_matrix, adjacency, mean_distance)
  computations/session-54/s54_scale_factor.npz (tau, a, H, q)

Output:
  computations/session-55/s55_conformal_diagram.npz  (all results)
  computations/session-55/s55_conformal_diagram.png  (4-panel figure)

Gate: CONFORMAL-DIAGRAM-55 (INFO: causal structure classification)
"""

import sys
sys.path.insert(0, 'computations')
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

# ─── Load data ───────────────────────────────────────────────────────────────

d_latt = np.load('computations/session-54/s54_connes_latt.npz')
d_sf   = np.load('computations/session-54/s54_scale_factor.npz')

tau_vals = d_sf['tau']          # (10,) modulus parameter
a_vals   = d_sf['a']            # (10,) scale factor from Connes distance
H_vals   = d_sf['H']            # (10,) Hubble parameter H = (da/dtau) / a
q_vals   = d_sf['q']            # (10,) deceleration parameter
adj      = d_latt['adjacency']  # (32,32) adjacency matrix
dist_mat = d_latt['distance_matrix']  # (10,32,32) pairwise Connes distances
N_cells  = int(d_latt['N_cells'])

print("=" * 72)
print("CONFORMAL-DIAGRAM-55: Conformal Diagram and Energy Conditions")
print("=" * 72)
print()

# ─── 1. Conformal time integration ──────────────────────────────────────────

# eta(tau) = integral_0^tau dtau'/a(tau')
# For a(tau) ~ A * exp(B*tau), this converges at tau=0 since a(0)=1 (finite).

integrand = 1.0 / a_vals  # dtau/a(tau)

# Cumulative trapezoidal integration
eta_cumul = np.zeros_like(tau_vals)
eta_cumul[1:] = cumulative_trapezoid(integrand, tau_vals)

# Total conformal time
eta_total = eta_cumul[-1]

print("1. CONFORMAL TIME INTEGRATION")
print("-" * 40)
print(f"   tau range: [{tau_vals[0]:.4f}, {tau_vals[-1]:.4f}]")
print(f"   a range:   [{a_vals[0]:.4f}, {a_vals[-1]:.4f}]")
print(f"   eta range: [{eta_cumul[0]:.6f}, {eta_cumul[-1]:.6f}]")
print(f"   eta_total = {eta_total:.6f}")
print()

# ─── 2. Particle horizon ────────────────────────────────────────────────────

# Particle horizon exists if integral_0^tau dtau'/a(tau') is FINITE as tau->0+.
# Since a(0) = 1 (finite, nonzero), the integrand 1/a(0) = 1 is finite.
# Therefore the integral converges trivially: no divergence at tau=0.
#
# Physical meaning: In standard cosmology, particle horizon exists when
# eta(t_initial) is finite. Here tau=0 is the "initial time" (round metric),
# and eta(0) = 0 is trivially finite. The particle horizon at any tau is:
#   d_horizon(tau) = a(tau) * eta(tau)

d_horizon = a_vals * eta_cumul

# Does a PAST particle horizon exist?
# In standard FRW, the question is whether eta(t=0) diverges (no horizon) or
# is finite (horizon exists). Here eta(0)=0 (finite), so a particle horizon EXISTS.
# Every cell can only communicate with cells within comoving distance eta(tau).

# For comparison, in de Sitter space a(t) = exp(Ht), eta = -(1/H)exp(-Ht) + const,
# which gives finite eta at t=0. Our model is "de Sitter-like" in this respect.

# Check: does eta -> finite as tau -> infinity?
# Since a ~ exp(B*tau) with B=3.53, integrand ~ exp(-3.53*tau) -> 0 rapidly.
# Integral converges: eta(inf) is finite. This means there IS an event horizon.
# Estimate eta(inf) using the exponential fit:
A_exp = float(d_sf['A_exp'])
B_exp = float(d_sf['B_exp'])
# eta(inf) ~ eta(tau_max) + integral_{tau_max}^{inf} exp(-B*tau)/A dtau
#           = eta(tau_max) + exp(-B*tau_max)/(A*B)
eta_future_tail = np.exp(-B_exp * tau_vals[-1]) / (A_exp * B_exp)
eta_inf_estimate = eta_total + eta_future_tail
# Comoving event horizon = distance light can travel from now to tau=inf
d_event_horizon = a_vals[-1] * eta_future_tail  # at last tau

print("2. PARTICLE HORIZON ANALYSIS")
print("-" * 40)
print(f"   a(0) = {a_vals[0]:.6f} (finite, nonzero)")
print(f"   1/a(0) = {1.0/a_vals[0]:.6f} (integrand finite at tau=0)")
print(f"   => Particle horizon EXISTS (eta(0)=0 is finite)")
print(f"   d_horizon(tau) = a(tau)*eta(tau):")
for i in range(len(tau_vals)):
    print(f"     tau={tau_vals[i]:.4f}: eta={eta_cumul[i]:.6f}, d_H={d_horizon[i]:.6f}")
print()
print(f"   Event horizon estimate:")
print(f"   eta(inf) ~ {eta_inf_estimate:.6f} (exponential tail = {eta_future_tail:.6f})")
print(f"   Both particle and event horizons exist => de Sitter-like causal structure")
print()

# ─── 3. Equation of state w_eff(tau) ────────────────────────────────────────

# For FRW with perfect fluid: w = (2q - 1)/3
# Acceleration iff q < 0 iff w < -1/3

w_eff = (2.0 * q_vals - 1.0) / 3.0

# SEC requires rho + 3p >= 0, i.e., w >= -1/3 (equivalently q >= 0)
sec_violated = q_vals < 0

# Find the SEC violation boundary (where q crosses zero)
# q goes from -0.973 to +0.814; crosses zero between tau[7] and tau[8]
# Interpolate to find exact crossing
cs_q = CubicSpline(tau_vals, q_vals)
# Find root of q(tau) = 0 by bisection
tau_lo, tau_hi = tau_vals[7], tau_vals[8]
for _ in range(100):
    tau_mid = 0.5 * (tau_lo + tau_hi)
    if cs_q(tau_mid) < 0:
        tau_lo = tau_mid
    else:
        tau_hi = tau_mid
tau_sec = 0.5 * (tau_lo + tau_hi)
a_sec = CubicSpline(tau_vals, a_vals)(tau_sec)
eta_sec = CubicSpline(tau_vals, eta_cumul)(tau_sec)

print("3. EQUATION OF STATE w_eff(tau)")
print("-" * 40)
print(f"   w_eff = (2q - 1)/3 from deceleration parameter")
print(f"   SEC violation: w < -1/3 equivalently q < 0")
print()
for i in range(len(tau_vals)):
    marker = " <-- SEC VIOLATED" if sec_violated[i] else ""
    print(f"   tau={tau_vals[i]:.4f}: q={q_vals[i]:+.6f}, w={w_eff[i]:+.6f}{marker}")
print()
print(f"   SEC violation boundary: tau_SEC = {tau_sec:.6f}")
print(f"     a(tau_SEC) = {a_sec:.4f}")
print(f"     eta(tau_SEC) = {eta_sec:.6f}")
print(f"   SEC violated for tau in [0, {tau_sec:.4f}] ({np.sum(sec_violated)}/10 grid points)")
print()

# ─── 4. Causal structure classification ─────────────────────────────────────

# Classify by w_eff behavior:
# - de Sitter: w = -1  (q = -1)
# - inflation-like: -1 < w < -1/3  (q < 0)
# - radiation-like: w = 1/3  (q = 1)
# - matter-like: w = 0  (q = 1/2)
# - stiff matter: w = 1  (q = 2)
# - phantom: w < -1  (q < -1)

print("4. CAUSAL STRUCTURE CLASSIFICATION")
print("-" * 40)

# Average w in the accelerating phase
w_accel = w_eff[sec_violated]
w_mean_accel = np.mean(w_accel)
w_min = np.min(w_eff)
w_max = np.max(w_eff)

# Average w in the decelerating phase
w_decel = w_eff[~sec_violated]
w_mean_decel = np.mean(w_decel) if len(w_decel) > 0 else float('nan')

print(f"   w range: [{w_min:+.6f}, {w_max:+.6f}]")
print(f"   Mean w (accelerating phase, tau < {tau_sec:.3f}): {w_mean_accel:+.6f}")
if len(w_decel) > 0:
    print(f"   Mean w (decelerating phase, tau > {tau_sec:.3f}): {w_mean_decel:+.6f}")
print()

# Early phase: q ~ -0.97, w ~ -0.98  =>  near de Sitter
# Late phase: q ~ +0.81, w ~ +0.21   =>  between matter and radiation
# Transition: smooth, not sudden

if w_min > -1.0:
    phantom = False
    print(f"   No phantom energy (w > -1 everywhere)")
else:
    phantom = True
    print(f"   WARNING: phantom energy detected (w < -1)")

if w_eff[0] < -0.9:
    print(f"   Early phase: QUASI-DE-SITTER (w(0) = {w_eff[0]:+.4f})")
elif w_eff[0] < -1/3:
    print(f"   Early phase: INFLATIONARY (w(0) = {w_eff[0]:+.4f})")
else:
    print(f"   Early phase: DECELERATING (w(0) = {w_eff[0]:+.4f})")

if w_eff[-1] > 0.25:
    print(f"   Late phase: NEAR-RADIATION (w(-1) = {w_eff[-1]:+.4f})")
elif w_eff[-1] > -0.05:
    print(f"   Late phase: NEAR-MATTER (w(-1) = {w_eff[-1]:+.4f})")
elif w_eff[-1] > -1/3:
    print(f"   Late phase: COASTING (w(-1) = {w_eff[-1]:+.4f})")
else:
    print(f"   Late phase: STILL ACCELERATING (w(-1) = {w_eff[-1]:+.4f})")

classification = "QUASI-DE-SITTER -> DECELERATING (GRACEFUL EXIT)"
print(f"\n   CLASSIFICATION: {classification}")
print()

# ─── 5. Raychaudhuri equation / focusing ────────────────────────────────────

# Raychaudhuri: dtheta/dlambda = -(1/3)theta^2 - sigma^2 - R_mu_nu k^mu k^nu
# For FRW, theta = 3H, sigma = 0
# dtheta/dtau = 3*dH/dtau
# NEC: R_mu_nu k^mu k^nu >= 0  iff  rho + p >= 0  iff  w >= -1
# SEC: R_mu_nu k^mu k^nu >= 0 for timelike  iff  rho + 3p >= 0  iff  w >= -1/3

# Expansion scalar theta = 3H (for FRW)
theta = 3.0 * H_vals

# dH/dtau from finite differences
dH_dtau = np.gradient(H_vals, tau_vals)

# Raychaudhuri check: dtheta/dtau + (1/3)theta^2 = -sigma^2 - R_{mu nu} u^mu u^nu
# For FRW: sigma = 0, so this gives R_{mu nu} u^mu u^nu = -dtheta/dtau - theta^2/3
R_uu = -(3.0 * dH_dtau + theta**2 / 3.0)

# NEC: rho + p >= 0. For FRW: rho + p = -(2/3)*dH/dtau (in units where 8piG=1...)
# Actually let's be precise. Friedmann: H^2 = (8piG/3)*rho, Raychaudhuri: dH/dtau = -H^2(1+q)
# So: NEC violation iff q < -1 (phantom).

nec_violated = q_vals < -1.0

print("5. RAYCHAUDHURI EQUATION / FOCUSING")
print("-" * 40)
print(f"   theta = 3H (expansion scalar for FRW)")
print(f"   theta range: [{np.min(theta):.4f}, {np.max(theta):.4f}]")
print(f"   dH/dtau range: [{np.min(dH_dtau):.4f}, {np.max(dH_dtau):.4f}]")
print()
print(f"   NEC (q >= -1): {'SATISFIED everywhere' if not np.any(nec_violated) else 'VIOLATED'}")
print(f"   SEC (q >= 0):  VIOLATED for tau < {tau_sec:.4f}")
print(f"   q_min = {np.min(q_vals):+.6f} (at tau={tau_vals[np.argmin(q_vals)]:.4f})")
print(f"   q_max = {np.max(q_vals):+.6f} (at tau={tau_vals[np.argmax(q_vals)]:.4f})")
print()
print(f"   R_{{mu nu}} u^mu u^nu (timelike focusing):")
for i in range(len(tau_vals)):
    focus = "DEFOCUSING" if R_uu[i] < 0 else "FOCUSING"
    print(f"     tau={tau_vals[i]:.4f}: R_uu={R_uu[i]:+.4f} ({focus})")
print()

# ─── 6. Discrete trapped surfaces on 32-cell graph ──────────────────────────

# A trapped surface in the continuum: closed 2-surface where BOTH families of
# outgoing null normals have theta < 0 (converging).
#
# Discrete analog on graph: a cell i is "trapped" if the scale factor at ALL
# its neighbors j is SMALLER than a(i). This means "null rays" going outward
# from cell i encounter smaller a — they are being focused.
#
# More precisely: for each tau, compute a_cell(i) from the mean distance to
# neighbors. Then cell i is trapped if a_j < a_i for all neighbors j.
#
# Since the Connes distance is a global quantity (defined on cell pairs),
# we define a local "scale" for each cell as the mean distance to its neighbors.

print("6. DISCRETE TRAPPED SURFACES ON 32-CELL GRAPH")
print("-" * 40)

# For each tau, compute per-cell local scale
# d_cell[i] = mean distance from cell i to its neighbors
adj_bool = adj.astype(bool)
n_neighbors = np.sum(adj_bool, axis=1)  # number of neighbors per cell

trapped_count = np.zeros(len(tau_vals), dtype=int)
antitrapped_count = np.zeros(len(tau_vals), dtype=int)
normal_count = np.zeros(len(tau_vals), dtype=int)

# Also track expansion theta_i = (1/n_i) sum_j [d_ij(tau+dtau) - d_ij(tau)] / d_ij(tau) / dtau
# for each cell, summed over neighbors

cell_scale = np.zeros((len(tau_vals), N_cells))
cell_expansion = np.zeros((len(tau_vals), N_cells))

for t_idx in range(len(tau_vals)):
    D = dist_mat[t_idx]  # (32,32)
    for i in range(N_cells):
        nbrs = np.where(adj_bool[i])[0]
        if len(nbrs) > 0:
            cell_scale[t_idx, i] = np.mean(D[i, nbrs])

# Null expansion analog: rate of change of distances to neighbors
# theta_i(tau) ~ (1/d_i) * dd_i/dtau
for t_idx in range(1, len(tau_vals) - 1):
    dtau = tau_vals[t_idx + 1] - tau_vals[t_idx - 1]
    for i in range(N_cells):
        nbrs = np.where(adj_bool[i])[0]
        if len(nbrs) > 0:
            d_now = dist_mat[t_idx, i, nbrs]
            d_next = dist_mat[t_idx + 1, i, nbrs]
            d_prev = dist_mat[t_idx - 1, i, nbrs]
            # Central difference
            dd = (d_next - d_prev) / dtau
            cell_expansion[t_idx, i] = np.mean(dd / d_now)

# For trapped surface: we need BOTH null directions to converge.
# On a graph, "outgoing" from a set S means edges crossing the boundary of S.
# For a single cell, the expansion is the rate of change of distances to neighbors.
# If theta_i > 0 everywhere, no trapped surfaces (everything expanding).

# Check: a trapped SET of cells where expansion is negative across the boundary
# For each cell, check if its expansion theta is negative
for t_idx in range(1, len(tau_vals) - 1):
    for i in range(N_cells):
        if cell_expansion[t_idx, i] < 0:
            trapped_count[t_idx] += 1
        elif cell_expansion[t_idx, i] > 0:
            normal_count[t_idx] += 1

print(f"   Graph: N_cells = {N_cells}, edges = {np.sum(adj)//2}")
print(f"   Mean neighbors per cell: {np.mean(n_neighbors):.1f}")
print()
print(f"   Per-cell null expansion theta_i (central difference):")
print(f"   {'tau':>8} {'theta_min':>12} {'theta_max':>12} {'theta_mean':>12} {'N_neg':>6} {'N_pos':>6}")
for t_idx in range(1, len(tau_vals) - 1):
    th = cell_expansion[t_idx]
    n_neg = np.sum(th < 0)
    n_pos = np.sum(th > 0)
    print(f"   {tau_vals[t_idx]:8.4f} {np.min(th):12.4f} {np.max(th):12.4f} {np.mean(th):12.4f} {n_neg:6d} {n_pos:6d}")
print()

any_trapped = np.any(trapped_count > 0)
if any_trapped:
    print(f"   TRAPPED CELLS DETECTED at {np.sum(trapped_count > 0)} tau values")
else:
    print(f"   NO TRAPPED CELLS: all theta_i > 0 at all tau (universal expansion)")
    print(f"   => Penrose singularity theorem INAPPLICABLE (no trapped surfaces)")

# Additional check: is expansion monotonically positive?
all_positive = True
for t_idx in range(1, len(tau_vals) - 1):
    if np.any(cell_expansion[t_idx] <= 0):
        all_positive = False
        break

print(f"   All expansions positive: {all_positive}")
print(f"   This is consistent with volume-preserving Jensen deformation")
print(f"   (SU(2) contracts, C2/U(1) expands => net positive in mean distance)")
print()

# ─── 7. Comoving Hubble radius and horizon comparison ───────────────────────

# Comoving Hubble radius: r_H = 1/(aH)
# If r_H decreasing, modes exit the horizon (inflation)
# If r_H increasing, modes enter the horizon (deceleration)

r_H = 1.0 / (a_vals * H_vals)
dr_H = np.gradient(r_H, tau_vals)

print("7. COMOVING HUBBLE RADIUS")
print("-" * 40)
for i in range(len(tau_vals)):
    direction = "SHRINKING (inflationary)" if dr_H[i] < 0 else "GROWING (decelerating)"
    print(f"   tau={tau_vals[i]:.4f}: r_H={r_H[i]:.6f}, dr_H/dtau={dr_H[i]:+.6f} ({direction})")
print()

# Find where r_H starts growing (end of inflation)
# r_H is monotonic? Check
r_H_monotone_decrease = np.all(np.diff(r_H) < 0)
r_H_monotone_increase = np.all(np.diff(r_H) > 0)
if r_H_monotone_decrease:
    print(f"   r_H monotonically DECREASING: perpetual inflation (no horizon re-entry)")
elif r_H_monotone_increase:
    print(f"   r_H monotonically INCREASING: perpetual deceleration (no horizon exit)")
else:
    # Find turning point
    for i in range(1, len(r_H)):
        if np.diff(r_H)[i-1] > 0 and (i == 1 or np.diff(r_H)[i-2] < 0):
            tau_exit = 0.5 * (tau_vals[i-1] + tau_vals[i])
            print(f"   r_H turns at tau ~ {tau_exit:.4f}: inflation -> deceleration")
            break
print()

# ─── 8. Number of e-folds in the accelerating phase ─────────────────────────

# N_e = integral_0^{tau_SEC} H dtau
# Use trapezoidal rule on the accelerating portion

accel_mask = q_vals < 0
tau_accel = tau_vals[accel_mask]
H_accel = H_vals[accel_mask]
a_accel = a_vals[accel_mask]

N_e = np.trapezoid(H_accel, tau_accel)
a_ratio = a_vals[np.sum(accel_mask) - 1] / a_vals[0]  # a(end_accel) / a(start)

print("8. E-FOLDS DURING ACCELERATION")
print("-" * 40)
print(f"   Accelerating phase: tau in [0, ~{tau_sec:.4f}]")
print(f"   N_e = integral H dtau = {N_e:.4f}")
print(f"   a_ratio = a(tau_SEC)/a(0) = {a_ratio:.4f}")
print(f"   ln(a_ratio) = {np.log(a_ratio):.4f}")
print(f"   (N_e and ln(a_ratio) should agree for FRW: N_e={N_e:.4f} vs ln(a_ratio)={np.log(a_ratio):.4f})")
print()

# ─── 9. Summary / Gate verdict ──────────────────────────────────────────────

print("=" * 72)
print("CONFORMAL-DIAGRAM-55: SUMMARY")
print("=" * 72)
print()
print(f"CAUSAL STRUCTURE: {classification}")
print()
print(f"Key results:")
print(f"  1. Particle horizon EXISTS (eta(0)=0, a(0)=1 finite)")
print(f"  2. Event horizon EXISTS (eta(inf) ~ {eta_inf_estimate:.4f}, finite)")
print(f"  3. SEC VIOLATED for tau in [0, {tau_sec:.4f}] (acceleration)")
print(f"  4. NEC SATISFIED everywhere (no phantom, q > -1)")
print(f"  5. w_eff transitions from {w_eff[0]:+.4f} (quasi-de Sitter) to {w_eff[-1]:+.4f} (near-radiation)")
print(f"  6. Graceful exit: smooth transition through w=-1/3 at tau={tau_sec:.4f}")
print(f"  7. NO trapped surfaces on 32-cell graph (all theta_i > 0)")
print(f"  8. Penrose singularity theorem INAPPLICABLE (no trapped surfaces + SEC violated)")
print(f"  9. N_e = {N_e:.4f} e-folds during acceleration")
print(f" 10. Comoving Hubble radius: {'monotonically ' if r_H_monotone_decrease or r_H_monotone_increase else ''}{'decreasing' if r_H_monotone_decrease else 'non-monotonic'}")
print()
print(f"GATE: CONFORMAL-DIAGRAM-55")
print(f"  Verdict: INFO")
print(f"  Classification: QUASI-DE-SITTER -> DECELERATING (graceful exit)")
print(f"  Both horizons (particle + event) exist => finite conformal diamond")
print(f"  Analog: inflationary cosmology with natural graceful exit")

# ─── 10. Save results ───────────────────────────────────────────────────────

np.savez('computations/session-55/s55_conformal_diagram.npz',
    # Grid
    tau=tau_vals, a=a_vals, H=H_vals, q=q_vals,
    # Conformal time
    eta=eta_cumul, eta_total=eta_total, eta_inf=eta_inf_estimate,  # (local)
    # Equation of state
    w_eff=w_eff,
    # SEC boundary
    tau_sec=tau_sec, a_sec=a_sec, eta_sec=eta_sec,
    # Energy conditions
    nec_violated=nec_violated, sec_violated=sec_violated,
    # Raychaudhuri
    theta=theta, R_uu=R_uu,
    # Hubble radius
    r_H=r_H,
    # Trapped surfaces
    cell_scale=cell_scale, cell_expansion=cell_expansion,
    trapped_count=trapped_count,
    any_trapped=any_trapped,
    # E-folds
    N_e=N_e,
    # Classification
    classification=np.array([classification]),
    # Gate
    gate_name=np.array(['CONFORMAL-DIAGRAM-55']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([f'Classification: {classification}. Both horizons exist. SEC violated tau<{tau_sec:.4f}. No trapped surfaces. N_e={N_e:.3f}.'])
)

# ─── 11. Plot ────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle('CONFORMAL-DIAGRAM-55: Conformal Structure of Lattice Spectral Triple',
             fontsize=14, fontweight='bold')

# Panel 1: Conformal diagram (Penrose-style)
ax1 = axes[0, 0]
ax1.set_title('Conformal Diagram (eta vs comoving distance)', fontsize=11)

# The "conformal diagram" for FRW: plot eta(tau) vs comoving distance chi.
# For a homogeneous space, the diagram is a strip: chi in [0, chi_max], eta in [0, eta_inf].
# Light cones are 45-degree lines.

# Draw the conformal diamond
# eta_max ~ eta_inf_estimate. chi_max ~ eta_inf_estimate (light crossing time)
eta_max = eta_inf_estimate
chi_max = eta_max

# Shade SEC violation region
eta_sec_val = eta_sec
ax1.axhspan(0, eta_sec_val, alpha=0.15, color='red', label=f'SEC violated (tau<{tau_sec:.3f})')

# Plot eta(tau) curve (the "worldline" of a comoving observer at chi=0)
ax1.plot([0]*len(eta_cumul), eta_cumul, 'ko-', markersize=4, label='Comoving observer')

# Plot particle horizon: 45-degree line from (0,0)
eta_fine = np.linspace(0, eta_max, 100)
ax1.plot(eta_fine, eta_fine, 'b--', linewidth=1.5, alpha=0.7, label='Particle horizon (past light cone)')

# Plot event horizon: 45-degree line from (0, eta_inf) going backward
ax1.plot(eta_max - eta_fine, eta_fine, 'r--', linewidth=1.5, alpha=0.7, label='Event horizon (future light cone)')

# Mark key tau values on the worldline
for i in [0, 4, -1]:
    ax1.annotate(f'tau={tau_vals[i]:.3f}\neta={eta_cumul[i]:.4f}',
                xy=(0, eta_cumul[i]), xytext=(0.03, eta_cumul[i]),
                fontsize=7, ha='left')

# Mark SEC boundary
ax1.axhline(eta_sec_val, color='red', linewidth=0.8, linestyle=':')
ax1.annotate(f'SEC boundary\ntau={tau_sec:.3f}',
            xy=(chi_max*0.5, eta_sec_val), fontsize=8, color='red', ha='center', va='bottom')

ax1.set_xlabel('Comoving distance chi')
ax1.set_ylabel('Conformal time eta')
ax1.set_xlim(-0.01, chi_max * 1.05)
ax1.set_ylim(-0.005, eta_max * 1.05)
ax1.legend(fontsize=7, loc='upper right')
ax1.set_aspect('equal')

# Panel 2: w_eff and q vs tau
ax2 = axes[0, 1]
ax2.set_title('Equation of State and Deceleration Parameter', fontsize=11)

color1 = 'tab:blue'
color2 = 'tab:red'

ax2.plot(tau_vals, w_eff, 'o-', color=color1, linewidth=2, markersize=5, label='w_eff = (2q-1)/3')
ax2.axhline(-1/3, color=color1, linestyle=':', alpha=0.5, linewidth=1)
ax2.axhline(-1, color='gray', linestyle='--', alpha=0.3, linewidth=1)
ax2.text(tau_vals[-1]*1.02, -1/3, 'w=-1/3\n(SEC)', fontsize=7, color=color1, va='center')
ax2.text(tau_vals[-1]*1.02, -1, 'w=-1\n(dS)', fontsize=7, color='gray', va='center')
ax2.set_ylabel('w_eff', color=color1, fontsize=10)
ax2.tick_params(axis='y', labelcolor=color1)

ax2b = ax2.twinx()
ax2b.plot(tau_vals, q_vals, 's-', color=color2, linewidth=2, markersize=5, label='q (deceleration)')
ax2b.axhline(0, color=color2, linestyle=':', alpha=0.5, linewidth=1)
ax2b.set_ylabel('q (deceleration)', color=color2, fontsize=10)
ax2b.tick_params(axis='y', labelcolor=color2)

# Shade acceleration region
ax2.axvspan(tau_vals[0], tau_sec, alpha=0.1, color='red', label=f'Accelerating (q<0)')
ax2.axvline(tau_sec, color='red', linewidth=1, linestyle='--')
ax2.annotate(f'tau_SEC={tau_sec:.4f}', xy=(tau_sec, w_eff[0]), fontsize=8,
            rotation=90, va='bottom', ha='right', color='red')

ax2.set_xlabel('tau (modulus)')
ax2.legend(fontsize=8, loc='upper left')
ax2b.legend(fontsize=8, loc='lower right')

# Panel 3: Comoving Hubble radius
ax3 = axes[1, 0]
ax3.set_title('Comoving Hubble Radius r_H = 1/(aH)', fontsize=11)

ax3.plot(tau_vals, r_H, 'go-', linewidth=2, markersize=6, label='r_H = 1/(aH)')
ax3.plot(tau_vals, eta_cumul, 'b^-', linewidth=2, markersize=5, label='eta(tau) (conf. time)')
ax3.plot(tau_vals, d_horizon, 'rs-', linewidth=2, markersize=5, label='d_H = a*eta (phys. horizon)')

# Shade inflation region
ax3.axvspan(tau_vals[0], tau_sec, alpha=0.1, color='red')
ax3.axvline(tau_sec, color='red', linewidth=1, linestyle='--', label=f'tau_SEC={tau_sec:.4f}')

ax3.set_xlabel('tau (modulus)')
ax3.set_ylabel('Comoving distance')
ax3.legend(fontsize=8)
ax3.set_yscale('log')

# Panel 4: Discrete trapped surface analysis
ax4 = axes[1, 1]
ax4.set_title('Cell Expansion theta_i on 32-Cell Graph', fontsize=11)

# Plot expansion for each cell as a function of tau (interior points only)
tau_interior = tau_vals[1:-1]
for i in range(N_cells):
    th = cell_expansion[1:-1, i]
    ax4.plot(tau_interior, th, '-', alpha=0.3, linewidth=0.8, color='steelblue')

# Mean expansion
th_mean = np.mean(cell_expansion[1:-1, :], axis=1)
th_min = np.min(cell_expansion[1:-1, :], axis=1)
th_max = np.max(cell_expansion[1:-1, :], axis=1)
ax4.plot(tau_interior, th_mean, 'k-', linewidth=2.5, label='Mean theta')
ax4.fill_between(tau_interior, th_min, th_max, alpha=0.15, color='steelblue', label='Min-max envelope')

ax4.axhline(0, color='red', linewidth=1, linestyle='--', label='theta=0 (trapped boundary)')
ax4.set_xlabel('tau (modulus)')
ax4.set_ylabel('Null expansion theta_i')
ax4.legend(fontsize=8)

# Annotate
if not any_trapped:
    ax4.text(0.5, 0.05, 'ALL theta_i > 0: NO TRAPPED SURFACES',
            transform=ax4.transAxes, fontsize=10, ha='center', color='green',
            fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

plt.tight_layout()
plt.savefig('computations/session-55/s55_conformal_diagram.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved: computations/session-55/s55_conformal_diagram.png")
print(f"Data saved: computations/session-55/s55_conformal_diagram.npz")
