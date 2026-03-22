#!/usr/bin/env python3
"""
Session 22a QA-1: Acoustic Impedance Z(tau) and Reflection Coefficient R_reflect(tau)

Computes the acoustic impedance of the Dirac spectrum at the phonon gap edge,
and the reflection coefficient at the Berry curvature monopole locations M1 and M2.

Physical picture: The Jensen deformation tau parametrizes an "internal acoustic medium."
The impedance Z(tau) = sqrt(|rho(tau) * kappa(tau)|) measures the spectral resistance
to a rolling modulus. At topological phase boundaries (M1, M2), the gap-edge sector
switches identity, creating an impedance mismatch that partially reflects the modulus.

Definitions:
  rho(tau) = mult_gap(tau) / delta_E(tau)   [DOS at gap edge]
    where delta_E = E_next - E_gap (spacing to next distinct level)
  kappa(tau) = |d(E_gap)/d(tau)|             [gap stiffness]
  Z(tau) = sqrt(|rho * kappa|)               [acoustic impedance]
  R_reflect = ((Z2 - Z1) / (Z2 + Z1))^2     [reflection coefficient]

Data: tier0-computation/s19a_sweep_data.npz (21 tau values, 11424 eigenvalues each)
Output: s22a_impedance.npz, s22a_impedance.png

Author: quantum-acoustics-theorist
Date: 2026-02-20
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 1. LOAD DATA
# ============================================================
data_dir = Path(__file__).parent
data = np.load(data_dir / 's19a_sweep_data.npz', allow_pickle=True)
tau_values = data['tau_values']  # 21 values: 0.0, 0.1, ..., 2.0
n_tau = len(tau_values)

# Extract gap-edge properties at each tau
gap_ev = np.zeros(n_tau)        # gap eigenvalue (smallest)
next_ev = np.zeros(n_tau)       # next distinct eigenvalue
gap_mult = np.zeros(n_tau)      # multiplicity at gap edge
gap_sector_p = np.zeros(n_tau, dtype=int)
gap_sector_q = np.zeros(n_tau, dtype=int)
next_mult = np.zeros(n_tau)     # multiplicity at next level

for i in range(n_tau):
    ev = data[f'eigenvalues_{i}']
    p = data[f'sector_p_{i}']
    q = data[f'sector_q_{i}']
    m = data[f'multiplicities_{i}']

    # Sort unique eigenvalues
    unique_sorted = np.sort(np.unique(np.round(ev, 6)))
    gap_ev[i] = unique_sorted[0]
    next_ev[i] = unique_sorted[1]

    # Gap edge properties
    mask_gap = np.abs(ev - gap_ev[i]) < 1e-4
    gap_mult[i] = m[mask_gap].sum()
    # Dominant sector at gap edge
    sectors = list(zip(p[mask_gap].tolist(), q[mask_gap].tolist()))
    # Use first sector as representative
    gap_sector_p[i] = sectors[0][0]
    gap_sector_q[i] = sectors[0][1]

    mask_next = np.abs(ev - next_ev[i]) < 1e-4
    next_mult[i] = m[mask_next].sum()


# ============================================================
# 2. COMPUTE IMPEDANCE COMPONENTS
# ============================================================

# 2a. DOS at gap edge: rho = mult / delta_E
delta_E = next_ev - gap_ev  # level spacing
rho = gap_mult / delta_E    # DOS proxy [modes/energy]

# 2b. Gap stiffness: kappa = |d(gap)/d(tau)| via central differences
kappa = np.zeros(n_tau)
for i in range(n_tau):
    if i == 0:
        kappa[i] = abs(gap_ev[1] - gap_ev[0]) / (tau_values[1] - tau_values[0])
    elif i == n_tau - 1:
        kappa[i] = abs(gap_ev[-1] - gap_ev[-2]) / (tau_values[-1] - tau_values[-2])
    else:
        kappa[i] = abs(gap_ev[i+1] - gap_ev[i-1]) / (tau_values[i+1] - tau_values[i-1])

# 2c. Acoustic impedance
Z = np.sqrt(np.abs(rho * kappa))

# ============================================================
# 3. REFLECTION COEFFICIENTS
# ============================================================

# Step reflection: R between consecutive tau points
R_step = np.zeros(n_tau - 1)
for i in range(n_tau - 1):
    Z1, Z2 = Z[i], Z[i+1]
    if Z1 + Z2 > 0:
        R_step[i] = ((Z2 - Z1) / (Z2 + Z1))**2
    else:
        R_step[i] = 0.0

# Identify M1 and M2 transitions
# M1: around tau=0.10-0.20 (transition from fundamental to singlet)
# M2: around tau=1.50-1.60 (transition back)

# At M1 (between tau=0.10 and tau=0.20, indices 1->2):
i_M1 = 1  # tau=0.10 -> tau=0.20 transition
Z_M1_outside = Z[i_M1]
Z_M1_inside = Z[i_M1 + 1]
R_M1 = ((Z_M1_inside - Z_M1_outside) / (Z_M1_inside + Z_M1_outside))**2

# At M2 (between tau=1.50 and tau=1.60, indices 15->16):
i_M2 = 15  # tau=1.50 -> tau=1.60 transition
Z_M2_inside = Z[i_M2]
Z_M2_outside = Z[i_M2 + 1]
R_M2 = ((Z_M2_outside - Z_M2_inside) / (Z_M2_outside + Z_M2_inside))**2

# Also compute the effective impedance ratio at each transition
Z_ratio_M1 = max(Z_M1_outside, Z_M1_inside) / min(Z_M1_outside, Z_M1_inside) if min(Z_M1_outside, Z_M1_inside) > 0 else float('inf')
Z_ratio_M2 = max(Z_M2_outside, Z_M2_inside) / min(Z_M2_outside, Z_M2_inside) if min(Z_M2_outside, Z_M2_inside) > 0 else float('inf')

# Compute cavity round-trip loss
# After one M1 reflection and one M2 reflection:
R_cavity = R_M1 * R_M2  # fraction surviving one round trip
if R_cavity > 0:
    # Finesse-like parameter
    finesse = np.pi * np.sqrt(np.sqrt(R_M1 * R_M2)) / (1 - np.sqrt(R_M1 * R_M2))
else:
    finesse = 0.0

# ============================================================
# 4. ALTERNATIVE IMPEDANCE: USING TOTAL GAP-EDGE WEIGHT
# ============================================================
# Alternative definition: Z_alt = sqrt(mult * |E_gap|)
# This treats impedance as sqrt(rho * c_s^2) where c_s ~ E_gap
Z_alt = np.sqrt(gap_mult * gap_ev)

R_step_alt = np.zeros(n_tau - 1)
for i in range(n_tau - 1):
    Z1, Z2 = Z_alt[i], Z_alt[i+1]
    if Z1 + Z2 > 0:
        R_step_alt[i] = ((Z2 - Z1) / (Z2 + Z1))**2

R_M1_alt = ((Z_alt[i_M1+1] - Z_alt[i_M1]) / (Z_alt[i_M1+1] + Z_alt[i_M1]))**2
R_M2_alt = ((Z_alt[i_M2+1] - Z_alt[i_M2]) / (Z_alt[i_M2+1] + Z_alt[i_M2]))**2

# ============================================================
# 5. PRINT RESULTS
# ============================================================

print("=" * 80)
print("SESSION 22a QA-1: ACOUSTIC IMPEDANCE AND REFLECTION COEFFICIENTS")
print("=" * 80)
print()

print("--- Impedance Components at Each tau ---")
print(f"{'tau':>6s} {'gap_ev':>10s} {'next_ev':>10s} {'delta_E':>10s} {'mult':>6s} {'rho':>12s} {'kappa':>10s} {'Z':>10s} {'sector':>10s}")
print("-" * 90)
for i in range(n_tau):
    sec = f"({gap_sector_p[i]},{gap_sector_q[i]})"
    print(f"{tau_values[i]:6.2f} {gap_ev[i]:10.6f} {next_ev[i]:10.6f} {delta_E[i]:10.6f} {gap_mult[i]:6.0f} {rho[i]:12.2f} {kappa[i]:10.6f} {Z[i]:10.4f} {sec:>10s}")

print()
print("--- Step Reflection Coefficients (Primary: rho*kappa definition) ---")
print(f"{'tau_mid':>8s} {'R_step':>10s} {'Z_low':>10s} {'Z_high':>10s}")
print("-" * 45)
for i in range(n_tau - 1):
    tau_mid = (tau_values[i] + tau_values[i+1]) / 2
    print(f"{tau_mid:8.2f} {R_step[i]:10.6f} {Z[i]:10.4f} {Z[i+1]:10.4f}")

print()
print("=" * 80)
print("MONOPOLE REFLECTION ANALYSIS")
print("=" * 80)

print()
print(f"--- M1 (tau ~ 0.10 -> 0.20): Fundamental -> Singlet Transition ---")
print(f"  Z_outside (tau=0.10, fundamental, mult={gap_mult[i_M1]:.0f}): {Z[i_M1]:.6f}")
print(f"  Z_inside  (tau=0.20, singlet,     mult={gap_mult[i_M1+1]:.0f}):  {Z[i_M1+1]:.6f}")
print(f"  Impedance ratio: {Z_ratio_M1:.4f}")
print(f"  R_reflect(M1) = {R_M1:.6f} ({R_M1*100:.4f}%)")
print(f"  R_M1 > 0.10? {'YES' if R_M1 > 0.10 else 'NO'}")
print(f"  R_M1 > 0.30? {'YES' if R_M1 > 0.30 else 'NO'}")

print()
print(f"--- M2 (tau ~ 1.50 -> 1.60): Singlet -> Fundamental Transition ---")
print(f"  Z_inside  (tau=1.50, singlet,     mult={gap_mult[i_M2]:.0f}):  {Z[i_M2]:.6f}")
print(f"  Z_outside (tau=1.60, fundamental, mult={gap_mult[i_M2+1]:.0f}): {Z[i_M2+1]:.6f}")
print(f"  Impedance ratio: {Z_ratio_M2:.4f}")
print(f"  R_reflect(M2) = {R_M2:.6f} ({R_M2*100:.4f}%)")
print(f"  R_M2 > 0.10? {'YES' if R_M2 > 0.10 else 'NO'}")
print(f"  R_M2 > 0.30? {'YES' if R_M2 > 0.30 else 'NO'}")

print()
print("--- Cavity Parameters ---")
print(f"  Round-trip reflection: R_M1 * R_M2 = {R_cavity:.6f}")
print(f"  Cavity finesse: {finesse:.4f}")
print(f"  Cavity width: tau_M2 - tau_M1 = {tau_values[i_M2] - tau_values[i_M1+1]:.2f}")

print()
print("--- Alternative Impedance (Z_alt = sqrt(mult * E_gap)) ---")
print(f"  R_M1_alt = {R_M1_alt:.6f} ({R_M1_alt*100:.4f}%)")
print(f"  R_M2_alt = {R_M2_alt:.6f} ({R_M2_alt*100:.4f}%)")

# ============================================================
# 6. Constraint Gate ASSESSMENT
# ============================================================

print()
print("=" * 80)
print("Constraint Gate ASSESSMENT (QA-1)")
print("=" * 80)
print()

# Primary impedance definition
if R_M1 > 0.30 and R_M2 > 0.30:
    verdict = "DECISIVE: R_reflect > 0.30 at both M1 and M2"
    bf = 15
    pp = "+8-12 pp"
elif R_M1 > 0.10:
    verdict = "COMPELLING: R_reflect > 0.10 at M1"
    bf = 6
    pp = "+4-6 pp"
elif Z_ratio_M1 > 2.0 or Z_ratio_M2 > 2.0:
    verdict = "INTERESTING: Impedance discontinuity confirmed (Z ratio > 2)"
    bf = 3
    pp = "+1-3 pp"
elif R_M1 < 0.01 and R_M2 < 0.01:
    verdict = "CLOSED: Z(tau) smooth, R_reflect < 0.01"
    bf = 0.3
    pp = "-3-5 pp"
else:
    verdict = "INTERMEDIATE: Some impedance structure but below compelling threshold"
    bf = 2
    pp = "+0-2 pp"

print(f"  Primary Z (rho*kappa): {verdict}")
print(f"  Bayes factor: {bf}")
print(f"  Probability shift: {pp}")
print()

# Check alternative definition
if R_M1_alt > 0.30 and R_M2_alt > 0.30:
    verdict_alt = "DECISIVE (alt)"
elif R_M1_alt > 0.10:
    verdict_alt = "COMPELLING (alt)"
elif R_M1_alt < 0.01 and R_M2_alt < 0.01:
    verdict_alt = "CLOSED (alt)"
else:
    verdict_alt = "INTERMEDIATE (alt)"
print(f"  Alternative Z (sqrt(mult*E)): {verdict_alt}")
print(f"  R_M1_alt={R_M1_alt:.6f}, R_M2_alt={R_M2_alt:.6f}")

print()
print("--- Robustness: Cross-check with both definitions ---")
both_compelling = (R_M1 > 0.10 or R_M1_alt > 0.10) and (R_M2 > 0.10 or R_M2_alt > 0.10)
print(f"  At least one definition gives R > 0.10 at BOTH monopoles: {'YES' if both_compelling else 'NO'}")

# ============================================================
# 7. SAVE DATA
# ============================================================

np.savez(data_dir / 's22a_impedance.npz',
         tau_values=tau_values,
         gap_ev=gap_ev,
         next_ev=next_ev,
         delta_E=delta_E,
         gap_mult=gap_mult,
         gap_sector_p=gap_sector_p,
         gap_sector_q=gap_sector_q,
         rho=rho,
         kappa=kappa,
         Z=Z,
         Z_alt=Z_alt,
         R_step=R_step,
         R_step_alt=R_step_alt,
         R_M1=R_M1,
         R_M2=R_M2,
         R_M1_alt=R_M1_alt,
         R_M2_alt=R_M2_alt,
         Z_ratio_M1=Z_ratio_M1,
         Z_ratio_M2=Z_ratio_M2,
         finesse=finesse)

print()
print(f"Data saved to {data_dir / 's22a_impedance.npz'}")

# ============================================================
# 8. PLOT
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 22a QA-1: Acoustic Impedance Z(tau) and Reflection Coefficient', fontsize=14)

# Panel (a): Z(tau) — primary definition
ax = axes[0, 0]
ax.semilogy(tau_values, Z, 'b-o', markersize=4, label=r'$Z = \sqrt{|\rho \cdot \kappa|}$')
ax.semilogy(tau_values, Z_alt, 'r--s', markersize=4, alpha=0.7, label=r'$Z_{alt} = \sqrt{N_{gap} \cdot E_{gap}}$')
ax.axvspan(0.15, 1.55, alpha=0.1, color='green', label='Physical window')
ax.axvline(0.15, color='orange', linestyle=':', alpha=0.7, label='M1')
ax.axvline(1.55, color='purple', linestyle=':', alpha=0.7, label='M2')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$Z(\tau)$')
ax.set_title('(a) Acoustic Impedance')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): Step reflection coefficient
ax = axes[0, 1]
tau_mid = (tau_values[:-1] + tau_values[1:]) / 2
ax.semilogy(tau_mid, R_step, 'b-o', markersize=4, label=r'$R_{step}$ (primary)')
ax.semilogy(tau_mid, R_step_alt, 'r--s', markersize=4, alpha=0.7, label=r'$R_{step}$ (alt)')
ax.axhline(0.10, color='green', linestyle='--', alpha=0.5, label='R=10% threshold')
ax.axhline(0.30, color='red', linestyle='--', alpha=0.5, label='R=30% threshold')
ax.axvline(0.15, color='orange', linestyle=':', alpha=0.7, label='M1')
ax.axvline(1.55, color='purple', linestyle=':', alpha=0.7, label='M2')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R_{reflect}$')
ax.set_title('(b) Step Reflection Coefficient')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Impedance components
ax = axes[1, 0]
ax.semilogy(tau_values, rho, 'b-o', markersize=4, label=r'$\rho$ (DOS at gap)')
ax.semilogy(tau_values, kappa, 'r-s', markersize=4, label=r'$\kappa$ (gap stiffness)')
ax.axvspan(0.15, 1.55, alpha=0.1, color='green')
ax.axvline(0.15, color='orange', linestyle=':', alpha=0.7)
ax.axvline(1.55, color='purple', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Impedance components')
ax.set_title(r'(c) $\rho(\tau)$ and $\kappa(\tau)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Gap multiplicity and level spacing
ax = axes[1, 1]
ax2 = ax.twinx()
ax.plot(tau_values, gap_mult, 'b-o', markersize=4, label='Gap multiplicity')
ax2.semilogy(tau_values, delta_E, 'r-s', markersize=4, label=r'$\Delta E$ (gap spacing)')
ax.axvspan(0.15, 1.55, alpha=0.1, color='green')
ax.axvline(0.15, color='orange', linestyle=':', alpha=0.7)
ax.axvline(1.55, color='purple', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Gap multiplicity', color='b')
ax2.set_ylabel(r'$\Delta E$', color='r')
ax.set_title('(d) Gap Multiplicity and Level Spacing')
# Combine legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(data_dir / 's22a_impedance.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to {data_dir / 's22a_impedance.png'}")
plt.close()

print()
print("Done.")
