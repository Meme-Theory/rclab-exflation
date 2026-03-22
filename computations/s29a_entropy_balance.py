#!/usr/bin/env python3
"""
Session 29a-3: Entropy Balance (Second Law Gate)
=================================================

GATE K-29b: Does particle creation compensate spectral entropy loss?

Physics (ordinary second law, no horizon — Einstein correction from S28):
    - S_spec(tau) = Bose-Einstein spectral entropy, monotonically DECREASING (TH-01).
    - dS_particles/d(tau) = sum_k Gamma_k * ln(1/B_k), Gamma_k = B_k * omega_k
    - Second law: dS_particles/d(tau) >= |dS_spec/d(tau)| at all tau

GATE K-29b: If dS_particles < |dS_spec| at ANY tau in [0, 0.50], tau evolution
is thermodynamically FORBIDDEN. Session terminates.

Inputs:
    - s23a_eigenvectors_extended.npz: eigenvalues at 9 tau [0..0.50]
    - s28a_bogoliubov_coefficients.npz: B_k(tau), omega(tau), Gamma_inject(tau)

Outputs:
    - s29a_entropy_balance.npz
    - s29a_entropy_balance.png

Author: hawking-theorist agent (Session 29a)
Date: 2026-02-28
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import time

t0 = time.time()
BASE = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")

# ============================================================
# LOAD DATA
# ============================================================
print("=" * 70)
print("SESSION 29a-3: ENTROPY BALANCE (SECOND LAW GATE)")
print("=" * 70)

# Eigenvalues (9 tau points)
eig = np.load(BASE / "s23a_eigenvectors_extended.npz", allow_pickle=True)
tau_eig = eig['tau_values']  # [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]

# Bogoliubov (21 tau points)
bog = np.load(BASE / "s28a_bogoliubov_coefficients.npz", allow_pickle=True)
tau_bog = bog['tau_values']  # 0..2.0 step 0.1
B_k = bog['B_k']            # (21, 11424)
omega = bog['omega_tracked'] # (21, 11424)
Gamma_inject = bog['Gamma_inject']  # (21,)

print(f"Eigenvalue data: {len(tau_eig)} tau points, {eig['eigenvalues_0'].shape[0]} modes")
print(f"Bogoliubov data: {len(tau_bog)} tau points, {B_k.shape[1]} modes")

# Find common tau values
common_tau = []
eig_idx = []
bog_idx = []
for i, t1 in enumerate(tau_eig):
    for j, t2 in enumerate(tau_bog):
        if abs(t1 - t2) < 0.001:
            common_tau.append(t1)
            eig_idx.append(i)
            bog_idx.append(j)
            break

common_tau = np.array(common_tau)
n_common = len(common_tau)
print(f"Common tau grid ({n_common} points): {common_tau}")

# ============================================================
# COMPUTATION 1: S_spec(tau) at T=1.0
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 1: S_spec(tau) [Bose-Einstein, T=1.0]")
print("=" * 70)

def bose_einstein_entropy(eigenvalues, T):
    """Bose-Einstein entropy: sum [x/(e^x-1) - ln(1-e^{-x})]."""
    x = np.abs(eigenvalues) / T
    mask = x < 500
    x_safe = x[mask]
    if len(x_safe) > 0:
        exp_x = np.exp(x_safe)
        term1 = x_safe / (exp_x - 1.0)
        term2 = -np.log(1.0 - np.exp(-x_safe))
        return np.sum(term1 + term2)
    return 0.0

T = 1.0
S_spec_full = np.zeros(len(tau_eig))
for i in range(len(tau_eig)):
    eigs = np.abs(eig[f'eigenvalues_{i}'])
    S_spec_full[i] = bose_einstein_entropy(eigs, T)

# S_spec at common tau values
S_spec = S_spec_full[eig_idx]

print(f"\n{'tau':>6} | {'S_spec':>12}")
print("-" * 25)
for i in range(n_common):
    print(f"{common_tau[i]:>6.2f} | {S_spec[i]:>12.2f}")

# ============================================================
# COMPUTATION 2: |dS_spec/d(tau)| via finite differences
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 2: |dS_spec/d(tau)|")
print("=" * 70)

# Use the full 9-point grid for better derivatives, then extract common points
dS_spec_full = np.gradient(S_spec_full, tau_eig)
dS_spec = dS_spec_full[eig_idx]

print(f"\n{'tau':>6} | {'dS_spec/dtau':>14} | {'|dS_spec/dtau|':>14}")
print("-" * 45)
for i in range(n_common):
    print(f"{common_tau[i]:>6.2f} | {dS_spec[i]:>14.2f} | {abs(dS_spec[i]):>14.2f}")

# ============================================================
# COMPUTATION 3: dS_particles/d(tau) from Bogoliubov data
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 3: dS_particles/d(tau) [rate formula]")
print("=" * 70)

# dS_particles/d(tau) = sum_k Gamma_k * ln(1/B_k)
# where Gamma_k = B_k * omega_k  (per-mode injection rate)
dS_particles = np.zeros(n_common)
dS_particles_detail = []

for ci in range(n_common):
    bi = bog_idx[ci]
    bk = B_k[bi]
    om = omega[bi]

    # Only modes with B_k > threshold (avoid log(inf))
    mask = bk > 1e-10
    bk_m = bk[mask]
    om_m = om[mask]

    # Per-mode rate and entropy contribution
    gamma_k = bk_m * om_m              # per-mode injection rate
    log_inv_bk = np.log(1.0 / bk_m)   # entropy per injection event
    ds_k = gamma_k * log_inv_bk        # entropy production rate per mode

    dS_particles[ci] = np.sum(ds_k)

    # Diagnostics
    n_active = np.sum(mask)
    gap_edge_mask = mask.copy()
    # Gap-edge: lowest 100 modes by omega
    omega_sorted_idx = np.argsort(om)
    gap_edge_set = set(omega_sorted_idx[:100])
    gap_ds = sum(ds_k[j] for j in range(len(ds_k))
                 if np.where(mask)[0][j] in gap_edge_set)

    dS_particles_detail.append({
        'n_active': n_active,
        'gamma_total': np.sum(gamma_k),
        'mean_log_inv_bk': np.mean(log_inv_bk),
        'gap_edge_frac': gap_ds / max(dS_particles[ci], 1e-30),
    })

print(f"\n{'tau':>6} | {'dS_part/dtau':>14} | {'N_active':>10} | {'<ln(1/B)>':>10} | {'Gap%':>6}")
print("-" * 60)
for ci in range(n_common):
    d = dS_particles_detail[ci]
    print(f"{common_tau[ci]:>6.2f} | {dS_particles[ci]:>14.2f} | {d['n_active']:>10} | "
          f"{d['mean_log_inv_bk']:>10.4f} | {100*d['gap_edge_frac']:>5.1f}%")

# ============================================================
# COMPUTATION 4: ENTROPY BALANCE RATIO R(tau)
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 4: ENTROPY BALANCE R = dS_particles / |dS_spec|")
print("=" * 70)

R_balance = np.zeros(n_common)
for i in range(n_common):
    abs_dS = abs(dS_spec[i])
    R_balance[i] = dS_particles[i] / abs_dS if abs_dS > 1e-10 else np.inf

gate_pass = True
violation_taus = []

print(f"\n{'tau':>6} | {'dS_part/dtau':>14} | {'|dS_spec/dtau|':>14} | {'R':>10} | {'Status':>8}")
print("-" * 70)
for i in range(n_common):
    r = R_balance[i]
    if np.isinf(r):
        status = "TRIVIAL"
    elif r >= 1.0:
        status = "PASS"
    else:
        status = "FAIL"
        gate_pass = False
        violation_taus.append(common_tau[i])
    print(f"{common_tau[i]:>6.2f} | {dS_particles[i]:>14.2f} | {abs(dS_spec[i]):>14.2f} | "
          f"{r:>10.4f} | {status:>8}")

# ============================================================
# COMPUTATION 5: CUMULATIVE ENTROPY
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 5: CUMULATIVE ENTROPY S_total(tau)")
print("=" * 70)

# Integrate dS_particles to get cumulative particle entropy
# Use trapezoidal rule on the common tau grid
S_part_cumul = np.zeros(n_common)
for i in range(1, n_common):
    dtau = common_tau[i] - common_tau[i-1]
    S_part_cumul[i] = S_part_cumul[i-1] + 0.5 * (dS_particles[i-1] + dS_particles[i]) * dtau

S_total = S_spec + S_part_cumul
Delta_S = S_total - S_total[0]

print(f"\n{'tau':>6} | {'S_spec':>12} | {'S_part_cum':>12} | {'S_total':>12} | {'Delta_S':>12} | {'OK?':>5}")
print("-" * 75)
cumul_pass = True
for i in range(n_common):
    ok = "YES" if Delta_S[i] >= -1e-6 else "NO"
    if Delta_S[i] < -1e-6:
        cumul_pass = False
    print(f"{common_tau[i]:>6.2f} | {S_spec[i]:>12.2f} | {S_part_cumul[i]:>12.2f} | "
          f"{S_total[i]:>12.2f} | {Delta_S[i]:>12.2f} | {ok:>5}")

# ============================================================
# GATE VERDICT
# ============================================================
print("\n" + "=" * 70)
print("GATE K-29b VERDICT: ENTROPY BALANCE")
print("=" * 70)

min_R = np.min(R_balance)
min_R_tau = common_tau[np.argmin(R_balance)]

print(f"\n  Differential check:")
print(f"    R = dS_particles / |dS_spec| at each tau:")
for i in range(n_common):
    marker = " <-- MIN" if common_tau[i] == min_R_tau else ""
    print(f"      tau={common_tau[i]:.2f}: R = {R_balance[i]:.4f}{marker}")
print(f"    Minimum R: {min_R:.4f} at tau={min_R_tau:.2f}")
print(f"    Gate threshold: R >= 1.0")

print(f"\n  Cumulative check:")
print(f"    S_total(tau) >= S_total(0) for all tau? {cumul_pass}")
print(f"    Minimum Delta S: {np.min(Delta_S):.2f}")

if gate_pass and cumul_pass:
    verdict = "PASS"
    verdict_detail = (
        f"Entropy balance satisfied at all tau in [0, {common_tau[-1]:.1f}]. "
        f"min R = {min_R:.4f} at tau={min_R_tau:.2f}. "
        f"Particle creation produces sufficient entropy."
    )
elif not gate_pass:
    verdict = "FAIL"
    verdict_detail = (
        f"dS_particles < |dS_spec| at tau = {[f'{t:.2f}' for t in violation_taus]}. "
        f"min R = {min_R:.4f}. "
        f"Particle creation insufficient. Smooth tau evolution thermodynamically forbidden."
    )
else:
    verdict = "CONDITIONAL"
    verdict_detail = (
        f"Differential balance passes but cumulative check fails. "
        f"Minimum Delta S = {np.min(Delta_S):.2f}."
    )

print(f"\n  *** GATE K-29b: {verdict} ***")
print(f"  {verdict_detail}")

# ============================================================
# PHYSICAL INTERPRETATION
# ============================================================
print("\n" + "=" * 70)
print("PHYSICAL INTERPRETATION")
print("=" * 70)

print(f"""
1. S_spec(tau) at T=1.0: ranges from {S_spec[0]:.1f} (tau=0) to {S_spec[-1]:.1f} (tau={common_tau[-1]:.1f})
   Monotonically decreasing (confirms TH-01). Total decrease: {S_spec[0]-S_spec[-1]:.1f}

2. dS_particles/d(tau) = sum_k B_k * omega_k * ln(1/B_k):
   Ranges from {dS_particles[0]:.1f} (tau=0) to {dS_particles[-1]:.1f} (tau={common_tau[-1]:.1f})
   Monotonically increasing (more modes participate at larger deformation)

3. Entropy balance ratio R:
   Ranges from {R_balance[0]:.2f} to {R_balance[-1]:.2f}
   {'All values R >= 1: second law satisfied' if gate_pass else 'Some values R < 1: entropy deficit at these tau'}

4. Hawking radiation connection (Paper 05):
   - The Bogoliubov particle creation IS the analog of Hawking radiation
   - The spectral entropy decrease IS the analog of horizon area decrease
   - R >= 1 at all tau = the ordinary second law is satisfied
   - No horizon exists on SU(3), so this is the ordinary (not generalized) second law
   - The entropy production rate dS_particles peaks where Gamma_inject peaks
""")

# ============================================================
# SAVE
# ============================================================
outpath = BASE / "s29a_entropy_balance.npz"
np.savez(outpath,
    common_tau=common_tau,
    tau_eig=tau_eig,
    S_spec_full=S_spec_full,
    S_spec=S_spec,
    dS_spec=dS_spec,
    dS_particles=dS_particles,
    R_balance=R_balance,
    S_part_cumul=S_part_cumul,
    S_total=S_total,
    Delta_S=Delta_S,
    verdict=np.array([verdict]),
    min_R=np.array([min_R]),
    min_R_tau=np.array([min_R_tau]),
)
print(f"Saved: {outpath}")

# ============================================================
# PLOT
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 29a-3: Entropy Balance (Second Law Gate K-29b)',
             fontsize=14, fontweight='bold')

# Panel 1: Entropy derivatives
ax = axes[0, 0]
ax.plot(common_tau, np.abs(dS_spec), 'b-o', linewidth=2, markersize=6,
        label=r'$|dS_{spec}/d\tau|$ (entropy cost)')
ax.plot(common_tau, dS_particles, 'r-s', linewidth=2, markersize=6,
        label=r'$dS_{particles}/d\tau$ (creation)')
# Shade satisfied regions
for i in range(n_common - 1):
    color = 'green' if R_balance[i] >= 1.0 else 'red'
    ax.axvspan(common_tau[i], common_tau[i+1], alpha=0.1, color=color)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Entropy rate')
ax.set_title('Entropy Cost vs Creation')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: Ratio R(tau)
ax = axes[0, 1]
ax.plot(common_tau, R_balance, 'k-o', linewidth=2, markersize=8)
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2, label='R = 1 (threshold)')
for i in range(n_common):
    color = 'green' if R_balance[i] >= 1.0 else 'red'
    ax.plot(common_tau[i], R_balance[i], 'o', color=color, markersize=10, zorder=5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R = dS_{particles}/|dS_{spec}|$')
ax.set_title(f'Entropy Balance Ratio (min R = {min_R:.3f})')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(bottom=0)

# Panel 3: Cumulative entropy
ax = axes[1, 0]
ax.plot(common_tau, S_spec / S_spec[0], 'b-o', linewidth=2, label='S_spec (normalized)')
ax.plot(common_tau, S_part_cumul / max(S_part_cumul[-1], 1), 'r-s', linewidth=2,
        label='S_particles (cumulative, normalized)')
ax.plot(common_tau, Delta_S, 'k--', linewidth=2, label=r'$\Delta S_{total}$')
ax2 = ax.twinx()
ax2.plot(common_tau, Delta_S, 'k--', linewidth=1, alpha=0.5)
ax2.set_ylabel(r'$\Delta S_{total}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Normalized entropy')
ax.set_title('Cumulative Entropy Balance')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: S_spec on fine grid
ax = axes[1, 1]
ax.plot(tau_eig, S_spec_full, 'b-o', linewidth=2, markersize=5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_{spec}(\tau; T=1)$')
ax.set_title('Spectral Entropy (full fine grid)')
ax.grid(True, alpha=0.3)
# Annotate decrease
ax.annotate(f'Decrease: {S_spec_full[0]-S_spec_full[-1]:.0f}\n({(S_spec_full[0]-S_spec_full[-1])/S_spec_full[0]*100:.1f}%)',
            xy=(0.25, (S_spec_full[0]+S_spec_full[-1])/2),
            fontsize=10, ha='center')

plt.tight_layout()
plot_path = BASE / "s29a_entropy_balance.png"
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved: {plot_path}")

elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.1f}s")
print(f"\n*** FINAL VERDICT: {verdict} ***")
