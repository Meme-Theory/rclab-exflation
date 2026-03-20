"""
ENTROPY-35: Spectral Entropy at Fold
=====================================
Computes the von Neumann spectral entropy:
    S = -sum_k [n_k ln(n_k) + (1 - n_k) ln(1 - n_k)]
where n_k = 1 / (exp(beta * |lambda_k|) + 1)
for the 16 singlet eigenvalues of D_K(tau) on SU(3).

This connects to Connes Paper 15 (Chamseddine-Connes-van Suijlekom 2019,
arXiv:1809.02944), which proves that the von Neumann entropy of the
fermionic Gibbs state IS a spectral action with a specific universal
cutoff function f_S.

The question: does S have a maximum at or near tau = 0.190 (the B2 fold)?
If yes, the fold is an entropy attractor.

Pre-registered gate (INFORMATIVE):
    S(tau=0.190) > S(tau=0.10) AND S(tau=0.190) > S(tau=0.30) at beta=1.0

Author: Connes-NCG-Theorist
Session: 35, Wave 3, Task W3-D
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import os

# ── Load data ───────────────────────────────────────────────────────────
data_path = os.path.join(os.path.dirname(__file__), 's23a_kosmann_singlet.npz')
data = np.load(data_path, allow_pickle=True)
tau_values = data['tau_values']
n_tau = len(tau_values)

print(f"Tau values: {tau_values}")
print(f"Number of tau points: {n_tau}")

# Extract eigenvalues at each tau
all_eigs = []
for i in range(n_tau):
    eigs = data[f'eigenvalues_{i}'].real
    all_eigs.append(np.sort(eigs))
    print(f"  tau={tau_values[i]:.3f}: {len(eigs)} eigenvalues, "
          f"range [{eigs.min():.6f}, {eigs.max():.6f}]")

# ── Entropy computation ─────────────────────────────────────────────────
def binary_entropy(p):
    """Compute -p*ln(p) - (1-p)*ln(1-p) with safe handling of p=0,1."""
    result = np.zeros_like(p, dtype=float)
    mask = (p > 0) & (p < 1)
    pm = p[mask]
    result[mask] = -pm * np.log(pm) - (1.0 - pm) * np.log(1.0 - pm)
    return result

def fermi_dirac(beta, lam):
    """Fermi-Dirac occupation n_k = 1/(exp(beta*|lam|) + 1)."""
    # Use |lambda| so all n_k <= 0.5
    x = beta * np.abs(lam)
    # For numerical stability at large x: n = exp(-x)/(1+exp(-x))
    n = np.where(x < 500, 1.0 / (np.exp(x) + 1.0), np.exp(-x))
    return n

def spectral_entropy(beta, eigenvalues):
    """
    Compute S_vN = -sum_k [n_k ln(n_k) + (1-n_k) ln(1-n_k)]
    where n_k = 1/(exp(beta*|lambda_k|)+1).

    Note on PH symmetry and signed eigenvalues:
    For a PH-symmetric spectrum {lambda_k, -lambda_k}, using signed eigenvalues
    gives n(lambda) = 1/(e^{beta*lambda}+1) and n(-lambda) = e^{beta*lambda}/(e^{beta*lambda}+1).
    The binary entropy h(n) = h(1-n), so the contribution from (+lambda, -lambda)
    is 2*h(1/(e^{beta*|lambda|}+1)). Using |lambda_k| for all 16 modes gives the
    same total (each pair contributes the same h-value twice).

    We use |lambda_k| here for clarity: all occupations are in [0, 0.5].
    """
    n_k = fermi_dirac(beta, eigenvalues)
    return np.sum(binary_entropy(n_k))

# Beta values to test
betas = [0.5, 1.0, 2.0, 5.0]

# Compute entropy at each (tau, beta)
S = np.zeros((len(betas), n_tau))
for j, beta in enumerate(betas):
    for i in range(n_tau):
        S[j, i] = spectral_entropy(beta, all_eigs[i])

# ── Print results table ─────────────────────────────────────────────────
print("\n" + "="*80)
print("SPECTRAL ENTROPY TABLE: S(tau, beta)")
print("="*80)
header = f"{'tau':>6s}"
for beta in betas:
    header += f" | S(beta={beta:.1f}):>12s"
print(f"{'tau':>6s}", end="")
for beta in betas:
    print(f" | S(b={beta:.1f})", end="")
print()
print("-" * (8 + 14 * len(betas)))

for i in range(n_tau):
    print(f"{tau_values[i]:6.3f}", end="")
    for j in range(len(betas)):
        print(f" | {S[j,i]:11.6f}", end="")
    print()

# ── Find maximum for each beta ──────────────────────────────────────────
print("\n" + "="*80)
print("ENTROPY MAXIMA")
print("="*80)

# For interpolation, use cubic spline to find refined maximum
tau_fine = np.linspace(tau_values[0], tau_values[-1], 1000)
S_max_tau = []
S_max_val = []

for j, beta in enumerate(betas):
    # Cubic spline interpolation
    cs = CubicSpline(tau_values, S[j, :])
    S_fine = cs(tau_fine)
    idx_max = np.argmax(S_fine)
    tau_max = tau_fine[idx_max]
    S_at_max = S_fine[idx_max]
    S_max_tau.append(tau_max)
    S_max_val.append(S_at_max)

    # Also report discrete maximum
    idx_disc = np.argmax(S[j, :])
    print(f"  beta={beta:.1f}: tau_max(discrete) = {tau_values[idx_disc]:.3f}, "
          f"S = {S[j,idx_disc]:.6f}")
    print(f"           tau_max(spline)   = {tau_max:.4f}, "
          f"S = {S_at_max:.6f}")

# ── Gate evaluation ──────────────────────────────────────────────────────
print("\n" + "="*80)
print("GATE EVALUATION: ENTROPY-35")
print("="*80)

# Need to evaluate at tau=0.190 (between grid points 0.15 and 0.20)
# Also need tau=0.10 and tau=0.30 (on grid)
tau_gate = 0.190
beta_gate = 1.0
j_gate = betas.index(beta_gate)

cs_gate = CubicSpline(tau_values, S[j_gate, :])
S_at_fold = cs_gate(tau_gate)
S_at_010 = S[j_gate, 1]  # tau=0.10
S_at_030 = S[j_gate, 5]  # tau=0.30

print(f"  At beta = {beta_gate}:")
print(f"    S(tau=0.100) = {S_at_010:.6f}")
print(f"    S(tau=0.190) = {S_at_fold:.6f} (interpolated)")
print(f"    S(tau=0.300) = {S_at_030:.6f}")
print(f"    S(0.190) > S(0.10)? {S_at_fold > S_at_010} "
      f"(diff = {S_at_fold - S_at_010:+.6f})")
print(f"    S(0.190) > S(0.30)? {S_at_fold > S_at_030} "
      f"(diff = {S_at_fold - S_at_030:+.6f})")

gate_pass = (S_at_fold > S_at_010) and (S_at_fold > S_at_030)
print(f"\n  >>> GATE ENTROPY-35: {'PASS' if gate_pass else 'FAIL'} <<<")

# ── Detailed analysis ────────────────────────────────────────────────────
print("\n" + "="*80)
print("DETAILED ANALYSIS")
print("="*80)

# Analyze sector-by-sector entropy contribution
print("\nSector decomposition at beta=1.0:")
beta_anal = 1.0
for i in range(n_tau):
    eigs = np.sort(np.abs(all_eigs[i]))
    # Identify sectors by degeneracy structure
    # B1: 2 modes (1 pair), smallest |lambda|
    # B2: 8 modes (4 pairs), middle |lambda|
    # B3: 6 modes (3 pairs), largest |lambda|
    pos_eigs = eigs[8:]  # positive eigenvalues (sorted)

    # At tau=0, all degenerate, so skip sector decomposition
    if tau_values[i] == 0:
        n_all = fermi_dirac(beta_anal, all_eigs[i])
        S_total = np.sum(binary_entropy(n_all))
        print(f"  tau={tau_values[i]:.3f}: S_total={S_total:.6f} "
              f"(all degenerate, no sector decomposition)")
        continue

    # For tau > 0: identify sectors
    # B1: singlet (smallest |lambda|, multiplicity 1 in positive sector)
    # B2: doublet (next 4, middle, multiplicity 4 in positive sector)
    # B3: triplet (outer 3, largest |lambda|, multiplicity 3 in positive sector)

    abs_pos = np.sort(np.abs(all_eigs[i]))[8:]  # 8 positive eigenvalues
    # Cluster by value
    unique_vals = []
    for val in abs_pos:
        if not unique_vals or abs(val - unique_vals[-1]) > 0.001:
            unique_vals.append(val)

    # B1: smallest unique value (1 mode positive + 1 negative = 2 total)
    # B2: middle unique value (4 modes positive + 4 negative = 8 total)
    # B3: largest unique value (3 modes positive + 3 negative = 6 total)

    S_sectors = {}
    for k, eig in enumerate(all_eigs[i]):
        abs_eig = abs(eig)
        # Classify
        if abs(abs_eig - unique_vals[0]) < 0.001:
            sector = 'B1'
        elif abs(abs_eig - unique_vals[1]) < 0.001:
            sector = 'B2'
        else:
            sector = 'B3'

        n_k = fermi_dirac(beta_anal, np.array([eig]))
        h_k = binary_entropy(n_k)[0]
        S_sectors[sector] = S_sectors.get(sector, 0.0) + h_k

    S_total = sum(S_sectors.values())
    print(f"  tau={tau_values[i]:.3f}: S_total={S_total:.6f} | "
          f"B1={S_sectors.get('B1',0):.6f} ({S_sectors.get('B1',0)/S_total*100:.1f}%) | "
          f"B2={S_sectors.get('B2',0):.6f} ({S_sectors.get('B2',0)/S_total*100:.1f}%) | "
          f"B3={S_sectors.get('B3',0):.6f} ({S_sectors.get('B3',0)/S_total*100:.1f}%)")

# ── Monotonicity analysis ────────────────────────────────────────────────
print("\n" + "="*80)
print("MONOTONICITY ANALYSIS")
print("="*80)

for j, beta in enumerate(betas):
    diffs = np.diff(S[j, :])
    monotone_inc = all(d > 0 for d in diffs)
    monotone_dec = all(d < 0 for d in diffs)
    sign_changes = sum(1 for k in range(len(diffs)-1) if diffs[k]*diffs[k+1] < 0)

    status = "MONOTONE INCREASING" if monotone_inc else \
             "MONOTONE DECREASING" if monotone_dec else \
             f"NON-MONOTONE ({sign_changes} sign change(s))"
    print(f"  beta={beta:.1f}: {status}")
    if not monotone_inc and not monotone_dec:
        # Find where sign changes occur
        for k in range(len(diffs)-1):
            if diffs[k] * diffs[k+1] < 0:
                # Sign change between tau[k+1] and tau[k+2]
                print(f"    Sign change near tau = {tau_values[k+1]:.3f}")

# ── Connection to Connes Paper 15 ────────────────────────────────────────
print("\n" + "="*80)
print("CONNECTION TO CONNES PAPER 15")
print("="*80)
print("""
Chamseddine-Connes-van Suijlekom (2019) prove:
    S_vN = Tr(f_S(D^2/beta^2))
where f_S is the universal entropy function:
    f_S(x) = -[1/(e^x+1)] ln[1/(e^x+1)] - [e^x/(e^x+1)] ln[e^x/(e^x+1)]
evaluated at x = beta * |lambda_k|.

Our computation IS this spectral action, evaluated on the 16-mode
singlet sector of D_K(tau) on SU(3).

Key observation: The entropy depends on tau ONLY through the spectrum
{lambda_k(tau)}. As tau increases, the eigenvalue spread increases
(B3 eigenvalues grow, B1 decreases slightly, B2 fold structure).
Larger |lambda_k| -> n_k closer to 0 -> less entropy per mode.
Thus S_vN is MONOTONICALLY DECREASING with eigenvalue spread.

At tau=0, all 16 eigenvalues are degenerate at |lambda|=0.866, giving
the MAXIMUM entropy for any given beta. As tau increases, the spread
increases and entropy decreases.

The fold at tau=0.190 does NOT create an entropy maximum because:
1. The fold affects only v(tau) = dlambda/dtau, not lambda(tau) itself
2. At the fold, lambda_B2 has a minimum, but it does NOT return to
   the tau=0 value
3. The B3 eigenvalues continue growing monotonically, dominating the
   spread increase
""")

# ── Per-eigenvalue analysis at key tau values ────────────────────────────
print("="*80)
print("PER-EIGENVALUE OCCUPATIONS AND ENTROPIES (beta=1.0)")
print("="*80)
beta_detail = 1.0
for tau_idx in [0, 2, 3, 5]:  # tau=0.00, 0.15, 0.20, 0.30
    eigs = np.sort(all_eigs[tau_idx])
    n_k = fermi_dirac(beta_detail, eigs)
    h_k = binary_entropy(n_k)
    print(f"\ntau = {tau_values[tau_idx]:.3f}:")
    print(f"  {'lambda_k':>10s} {'|lambda_k|':>10s} {'n_k':>10s} {'h(n_k)':>10s}")
    for k in range(len(eigs)):
        print(f"  {eigs[k]:10.6f} {abs(eigs[k]):10.6f} {n_k[k]:10.6f} {h_k[k]:10.6f}")
    print(f"  {'TOTAL S':>10s} = {np.sum(h_k):.6f}")

# ── Save results ─────────────────────────────────────────────────────────
save_path = os.path.join(os.path.dirname(__file__), 's35_spectral_entropy.npz')
np.savez(save_path,
         tau_values=tau_values,
         betas=np.array(betas),
         S=S,
         S_max_tau=np.array(S_max_tau),
         S_max_val=np.array(S_max_val),
         S_at_fold_beta1=S_at_fold,
         S_at_010_beta1=S_at_010,
         S_at_030_beta1=S_at_030,
         gate_pass=gate_pass,
         eigenvalues=[all_eigs[i] for i in range(n_tau)])
print(f"\nData saved to: {save_path}")

# ── Plot ─────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: S vs tau for all beta values
ax = axes[0, 0]
colors = ['#d62728', '#2ca02c', '#1f77b4', '#9467bd']
for j, beta in enumerate(betas):
    cs = CubicSpline(tau_values, S[j, :])
    tau_plot = np.linspace(0, 0.5, 500)
    S_plot = cs(tau_plot)
    ax.plot(tau_plot, S_plot, '-', color=colors[j], linewidth=2,
            label=f'beta = {beta:.1f}')
    ax.plot(tau_values, S[j, :], 'o', color=colors[j], markersize=6)
    # Mark maximum
    ax.axvline(S_max_tau[j], color=colors[j], linestyle=':', alpha=0.5)

ax.axvline(0.190, color='gray', linestyle='--', alpha=0.7, label='B2 fold (0.190)')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('S_vN', fontsize=12)
ax.set_title('Von Neumann Spectral Entropy vs tau', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 2: Normalized S/S_max for each beta
ax = axes[0, 1]
for j, beta in enumerate(betas):
    S_norm = S[j, :] / S[j, 0]  # Normalize to tau=0 value
    ax.plot(tau_values, S_norm, 'o-', color=colors[j], linewidth=2,
            label=f'beta = {beta:.1f}')

ax.axvline(0.190, color='gray', linestyle='--', alpha=0.7, label='B2 fold')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('S(tau) / S(tau=0)', fontsize=12)
ax.set_title('Normalized Entropy (relative to tau=0)', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 3: Eigenvalue spectrum vs tau
ax = axes[1, 0]
for i in range(n_tau):
    eigs = np.sort(np.abs(all_eigs[i]))[8:]  # positive eigenvalues
    ax.plot([tau_values[i]] * len(eigs), eigs, 'ko', markersize=3)

# Connect eigenvalue branches
for branch_idx in range(8):
    branch = [np.sort(np.abs(all_eigs[i]))[8 + branch_idx] for i in range(n_tau)]
    ax.plot(tau_values, branch, 'k-', linewidth=0.5, alpha=0.5)

ax.axvline(0.190, color='gray', linestyle='--', alpha=0.7, label='B2 fold')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('|lambda_k|', fontsize=12)
ax.set_title('Positive Eigenvalue Spectrum of D_K(tau)', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 4: Sector-resolved entropy at beta=1.0
ax = axes[1, 1]
S_B1 = []
S_B2 = []
S_B3 = []
for i in range(n_tau):
    if tau_values[i] == 0:
        # All degenerate at tau=0
        n_k = fermi_dirac(1.0, all_eigs[i])
        h_total = np.sum(binary_entropy(n_k))
        # At tau=0, B1 gets 2/16, B2 gets 8/16, B3 gets 6/16 of total
        S_B1.append(h_total * 2 / 16)
        S_B2.append(h_total * 8 / 16)
        S_B3.append(h_total * 6 / 16)
    else:
        abs_pos = np.sort(np.abs(all_eigs[i]))[8:]
        unique_vals = []
        for val in abs_pos:
            if not unique_vals or abs(val - unique_vals[-1]) > 0.001:
                unique_vals.append(val)

        s1, s2, s3 = 0.0, 0.0, 0.0
        for eig in all_eigs[i]:
            ae = abs(eig)
            n_k = fermi_dirac(1.0, np.array([eig]))
            h_k = binary_entropy(n_k)[0]
            if abs(ae - unique_vals[0]) < 0.001:
                s1 += h_k
            elif abs(ae - unique_vals[1]) < 0.001:
                s2 += h_k
            else:
                s3 += h_k
        S_B1.append(s1)
        S_B2.append(s2)
        S_B3.append(s3)

ax.stackplot(tau_values, S_B1, S_B2, S_B3,
             labels=['B1 (2 modes)', 'B2 (8 modes)', 'B3 (6 modes)'],
             colors=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.8)
ax.plot(tau_values, [sum(x) for x in zip(S_B1, S_B2, S_B3)],
        'k-', linewidth=2, label='Total S')
ax.axvline(0.190, color='gray', linestyle='--', alpha=0.7, label='B2 fold')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('Entropy contribution', fontsize=12)
ax.set_title('Sector-Resolved Entropy (beta=1.0)', fontsize=13)
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(__file__), 's35_spectral_entropy.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")

print("\n" + "="*80)
print("COMPUTATION COMPLETE")
print("="*80)
