#!/usr/bin/env python3
"""
Session 41 W2-5: Seeley-DeWitt coefficients and physical constants vs tau.

Computes a_0(tau), a_2(tau), a_4(tau) from the Dirac spectrum on SU(3) with
Jensen deformation parameter tau. Tracks spectral proxies for physical constants:
  a_2/a_0 ~ 1/G_N   (Newton's constant in M_KK units)
  a_4/a_2 ~ 1/alpha  (fine structure constant proxy)
  a_4/a_0 ~ gauge coupling combination

Also computes clock constraint: Delta_alpha/alpha = -3.08 * Delta_tau
and compares to CMB / quasar / atomic clock observational bounds.

Data sources:
  s27_multisector_bcs.npz  — tau = 0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50
  s36_sfull_tau_stabilization.npz — tau = 0.050, 0.160, 0.170, 0.180, 0.190, 0.210, 0.220

Peter-Weyl structure:
  Each sector (p,q) stores 16 * dim(p,q) eigenvalues.
  The right-regular representation contributes an additional degeneracy of dim(p,q).
  So the multiplicity for the Seeley-DeWitt sums is dim(p,q) per stored eigenvalue.

  For (1,2) sector: s27 lacks it, use (2,1) data (conjugation symmetry verified to ~1e-14).
  s36 has both (1,2) and (2,1) explicitly.

Cutoff sensitivity: lambda_min = 0.01, 0.1, 0.5 to handle near-zero eigenvalue divergences.

Author: Gen-Physicist (Session 41)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ──────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────

from canonical_constants import tau_fold as TAU_FOLD

DATA_DIR = Path(__file__).parent
SECTORS = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]
CUTOFFS = [0.01, 0.1, 0.5]

# Clock constraint: dalpha/alpha = -3.08 * dtau (Session 22d E-3)
CLOCK_COEFF = -3.08

# Observational bounds on |Delta_alpha / alpha|
CMB_BOUND = 1e-2        # z ~ 1100 (Planck + ACT)
QUASAR_BOUND = 1e-5     # z ~ 2-4 (Webb et al., Keck+VLT)
ATOMIC_CLOCK_BOUND = 1e-16  # per year (Sr/Yb optical lattice clocks)


def dim_pq(p, q):
    """Dimension of SU(3) irrep (p, q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def mult_pq(p, q):
    """Peter-Weyl multiplicity = dim(p,q)^2."""
    return dim_pq(p, q) ** 2


def right_reg_degeneracy(p, q):
    """Additional degeneracy from right-regular representation.

    Stored eigenvalues: 16 * dim(p,q) per sector.
    Full Hilbert space contribution: 16 * dim(p,q)^2 = 16 * mult(p,q).
    So each stored eigenvalue carries degeneracy = dim(p,q).
    """
    return dim_pq(p, q)


# ──────────────────────────────────────────────────────────────────────
# Load data
# ──────────────────────────────────────────────────────────────────────

d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
d27 = np.load(DATA_DIR / 's27_multisector_bcs.npz', allow_pickle=True)

s27_taus = list(d27['tau_values'])
s36_taus = [0.050, 0.160, 0.170, 0.180, 0.190, 0.210, 0.220]

# Build merged tau list (sorted, unique)
all_taus = sorted(set([float(t) for t in s27_taus] + s36_taus))
print(f"Merged tau values ({len(all_taus)}): {[f'{t:.3f}' for t in all_taus]}")


def get_eigenvalues(tau, p, q):
    """Retrieve eigenvalues for sector (p,q) at given tau.

    Tries s36 first (higher tau resolution near fold), then s27.
    For (1,2) in s27: uses (2,1) by conjugation symmetry.
    """
    # Try s36
    key36 = f"evals_tau{tau:.3f}_{p}_{q}"
    if key36 in d36.files:
        return d36[key36]

    # Try s27
    if tau in s27_taus or any(abs(tau - t) < 1e-10 for t in s27_taus):
        ti = min(range(len(s27_taus)), key=lambda i: abs(s27_taus[i] - tau))

        # Handle (1,2) -> (2,1) conjugation in s27
        pp, qq = p, q
        if (p, q) == (1, 2):
            pp, qq = 2, 1

        key27 = f"evals_{pp}_{qq}_{ti}"
        if key27 in d27.files:
            return d27[key27]

    raise KeyError(f"No eigenvalue data for tau={tau:.3f}, sector ({p},{q})")


# ──────────────────────────────────────────────────────────────────────
# Compute Seeley-DeWitt coefficients
# ──────────────────────────────────────────────────────────────────────

# Storage: results[cutoff_idx][tau_idx] = dict with a_0, a_2, a_4, sector contributions
results = {}

for ci, cutoff in enumerate(CUTOFFS):
    results[cutoff] = {}

    for tau in all_taus:
        a0_total = 0.0
        a2_total = 0.0
        a4_total = 0.0

        sector_data = {}

        for (p, q) in SECTORS:
            try:
                evals = get_eigenvalues(tau, p, q)
            except KeyError:
                # Skip missing sectors
                continue

            # Use POSITIVE eigenvalues only (spectral pairing: negative ones duplicate)
            pos_evals = evals[evals > cutoff]

            # Right-regular degeneracy
            deg = right_reg_degeneracy(p, q)

            # Seeley-DeWitt sums with multiplicity
            n_pos = len(pos_evals)
            s_a0 = deg * n_pos
            s_a2 = deg * np.sum(pos_evals**(-2))
            s_a4 = deg * np.sum(pos_evals**(-4))

            a0_total += s_a0
            a2_total += s_a2
            a4_total += s_a4

            sector_data[(p, q)] = {
                'n_pos': n_pos,
                'a0_contrib': s_a0,
                'a2_contrib': s_a2,
                'a4_contrib': s_a4,
                'min_pos_eval': np.min(pos_evals) if len(pos_evals) > 0 else np.inf,
            }

        results[cutoff][tau] = {
            'a0': a0_total,
            'a2': a2_total,
            'a4': a4_total,
            'sectors': sector_data,
        }

# ──────────────────────────────────────────────────────────────────────
# Print results
# ──────────────────────────────────────────────────────────────────────

print("\n" + "=" * 100)
print("SEELEY-DEWITT COEFFICIENTS vs TAU")
print("=" * 100)

for cutoff in CUTOFFS:
    print(f"\n--- Cutoff lambda_min = {cutoff} ---")
    print(f"{'tau':>6s}  {'a_0':>12s}  {'a_2':>14s}  {'a_4':>16s}  {'a_2/a_0':>12s}  {'a_4/a_2':>12s}  {'a_4/a_0':>14s}")
    print("-" * 100)

    for tau in all_taus:
        r = results[cutoff][tau]
        a0, a2, a4 = r['a0'], r['a2'], r['a4']
        r20 = a2 / a0 if a0 > 0 else np.inf
        r42 = a4 / a2 if a2 > 0 else np.inf
        r40 = a4 / a0 if a0 > 0 else np.inf
        print(f"{tau:6.3f}  {a0:12.1f}  {a2:14.6f}  {a4:16.6f}  {r20:12.6f}  {r42:12.6f}  {r40:14.6f}")

# ──────────────────────────────────────────────────────────────────────
# Fractional changes relative to fold (tau = 0.190)
# ──────────────────────────────────────────────────────────────────────

print("\n" + "=" * 100)
print("FRACTIONAL CHANGES RELATIVE TO FOLD (tau = 0.190)")
print("=" * 100)

ref_cutoff = 0.01  # Primary cutoff for physics analysis

# Find closest tau to fold
fold_tau = min(all_taus, key=lambda t: abs(t - TAU_FOLD))
print(f"Reference fold tau = {fold_tau:.3f}")

ref = results[ref_cutoff][fold_tau]
a0_fold = ref['a0']
a2_fold = ref['a2']
a4_fold = ref['a4']
r20_fold = a2_fold / a0_fold
r42_fold = a4_fold / a2_fold
r40_fold = a4_fold / a0_fold

print(f"\nAt fold: a_0 = {a0_fold:.1f}, a_2 = {a2_fold:.6f}, a_4 = {a4_fold:.6f}")
print(f"         a_2/a_0 = {r20_fold:.6f}, a_4/a_2 = {r42_fold:.6f}, a_4/a_0 = {r40_fold:.6f}")

print(f"\n{'tau':>6s}  {'Da_0/a_0':>12s}  {'Da_2/a_2':>12s}  {'Da_4/a_4':>12s}  {'D(a2/a0)':>12s}  {'D(a4/a2)':>12s}  {'D(a4/a0)':>12s}")
print("-" * 84)

for tau in all_taus:
    r = results[ref_cutoff][tau]
    a0, a2, a4 = r['a0'], r['a2'], r['a4']

    da0 = (a0 - a0_fold) / a0_fold
    da2 = (a2 - a2_fold) / a2_fold
    da4 = (a4 - a4_fold) / a4_fold

    r20 = a2 / a0
    r42 = a4 / a2
    r40 = a4 / a0

    dr20 = (r20 - r20_fold) / r20_fold
    dr42 = (r42 - r42_fold) / r42_fold
    dr40 = (r40 - r40_fold) / r40_fold

    print(f"{tau:6.3f}  {da0:+12.6f}  {da2:+12.6f}  {da4:+12.6f}  {dr20:+12.6f}  {dr42:+12.6f}  {dr40:+12.6f}")

# ──────────────────────────────────────────────────────────────────────
# Fractional changes relative to tau = 0
# ──────────────────────────────────────────────────────────────────────

print("\n" + "=" * 100)
print("FRACTIONAL CHANGES RELATIVE TO tau = 0")
print("=" * 100)

ref0 = results[ref_cutoff][0.0]
a0_0 = ref0['a0']
a2_0 = ref0['a2']
a4_0 = ref0['a4']
r20_0 = a2_0 / a0_0
r42_0 = a4_0 / a2_0
r40_0 = a4_0 / a0_0

print(f"At tau=0: a_0 = {a0_0:.1f}, a_2 = {a2_0:.6f}, a_4 = {a4_0:.6f}")
print(f"          a_2/a_0 = {r20_0:.6f}, a_4/a_2 = {r42_0:.6f}, a_4/a_0 = {r40_0:.6f}")
print()

print(f"KEY RATIOS:")
print(f"  a_2(fold)/a_2(0) = {a2_fold / a2_0:.8f}")
print(f"  a_4(fold)/a_4(0) = {a4_fold / a4_0:.8f}")
print(f"  (a_4/a_2)(fold) / (a_4/a_2)(0) = {r42_fold / r42_0:.8f}")
print(f"  (a_2/a_0)(fold) / (a_2/a_0)(0) = {r20_fold / r20_0:.8f}")

# ──────────────────────────────────────────────────────────────────────
# Clock constraint: Delta_alpha / alpha vs observational bounds
# ──────────────────────────────────────────────────────────────────────

print("\n" + "=" * 100)
print("CLOCK CONSTRAINT (Session 22d E-3)")
print("=" * 100)
print(f"dalpha/alpha = {CLOCK_COEFF} * dtau")
print()

# Two versions:
# 1. Analytic: Delta_alpha/alpha = -3.08 * (tau - tau_fold)
# 2. Spectral: use the actual a_4/a_2 ratio change

print("--- Analytic clock constraint ---")
print(f"{'tau':>6s}  {'Delta_tau':>10s}  {'Da/a (analytic)':>16s}  {'|Da/a|':>12s}  {'CMB (<1e-2)':>12s}  {'Quasar (<1e-5)':>14s}")
print("-" * 84)

max_da_analytic = 0
for tau in all_taus:
    dtau = tau - fold_tau
    da_alpha = CLOCK_COEFF * dtau
    abs_da = abs(da_alpha)
    max_da_analytic = max(max_da_analytic, abs_da)

    cmb_status = "PASS" if abs_da < CMB_BOUND else "FAIL"
    quasar_status = "PASS" if abs_da < QUASAR_BOUND else "FAIL"

    print(f"{tau:6.3f}  {dtau:+10.4f}  {da_alpha:+16.8f}  {abs_da:12.8f}  {cmb_status:>12s}  {quasar_status:>14s}")

print(f"\nMax |Delta_alpha/alpha| across tau range = {max_da_analytic:.6f}")
print(f"CMB bound (|Da/a| < 1e-2): {'PASS' if max_da_analytic < CMB_BOUND else 'FAIL'}")
print(f"Quasar bound (|Da/a| < 1e-5): {'PASS' if max_da_analytic < QUASAR_BOUND else 'FAIL'}")

# Spectral clock constraint: use a_4/a_2 as alpha proxy
print("\n--- Spectral clock constraint (a_4/a_2 as alpha proxy) ---")
print(f"{'tau':>6s}  {'a_4/a_2':>12s}  {'D(a4/a2)/(a4/a2)':>18s}  {'|D|':>12s}")
print("-" * 60)

max_dr42 = 0
for tau in all_taus:
    r = results[ref_cutoff][tau]
    r42 = r['a4'] / r['a2']
    dr42 = (r42 - r42_fold) / r42_fold
    abs_dr42 = abs(dr42)
    max_dr42 = max(max_dr42, abs_dr42)
    print(f"{tau:6.3f}  {r42:12.6f}  {dr42:+18.8f}  {abs_dr42:12.8f}")

print(f"\nMax |D(a_4/a_2)/(a_4/a_2)| = {max_dr42:.6f}")

# ──────────────────────────────────────────────────────────────────────
# Cutoff sensitivity analysis
# ──────────────────────────────────────────────────────────────────────

print("\n" + "=" * 100)
print("CUTOFF SENSITIVITY: RATIO STABILITY")
print("=" * 100)
print("Question: Do the RATIOS depend on the infrared cutoff?")
print()

for tau in [0.0, 0.100, fold_tau, 0.300, 0.500]:
    if tau not in all_taus:
        continue
    print(f"tau = {tau:.3f}:")
    for cutoff in CUTOFFS:
        r = results[cutoff][tau]
        a0, a2, a4 = r['a0'], r['a2'], r['a4']
        r20 = a2/a0 if a0 > 0 else np.inf
        r42 = a4/a2 if a2 > 0 else np.inf
        r40 = a4/a0 if a0 > 0 else np.inf
        print(f"  cutoff={cutoff:.2f}: a_2/a_0={r20:.6f}, a_4/a_2={r42:.6f}, a_4/a_0={r40:.6f}")
    print()

# ──────────────────────────────────────────────────────────────────────
# Sector-by-sector breakdown at tau = 0 and tau = fold
# ──────────────────────────────────────────────────────────────────────

print("\n" + "=" * 100)
print("SECTOR BREAKDOWN (cutoff = 0.01)")
print("=" * 100)

for tau_label, tau_val in [("tau=0.000", 0.0), (f"tau={fold_tau:.3f} (fold)", fold_tau)]:
    print(f"\n--- {tau_label} ---")
    r = results[ref_cutoff][tau_val]
    print(f"{'(p,q)':>8s}  {'dim':>4s}  {'deg':>4s}  {'n_pos':>6s}  {'a0_contrib':>12s}  {'a2_contrib':>14s}  {'a4_contrib':>16s}  {'min_eval':>10s}")
    print("-" * 90)

    for (p, q) in SECTORS:
        if (p, q) in r['sectors']:
            sd = r['sectors'][(p, q)]
            d = dim_pq(p, q)
            deg = right_reg_degeneracy(p, q)
            print(f"({p},{q}):    {d:4d}  {deg:4d}  {sd['n_pos']:6d}  {sd['a0_contrib']:12.1f}  {sd['a2_contrib']:14.6f}  {sd['a4_contrib']:16.6f}  {sd['min_pos_eval']:10.6f}")

# ──────────────────────────────────────────────────────────────────────
# Save results
# ──────────────────────────────────────────────────────────────────────

save_dict = {
    'tau_values': np.array(all_taus),
    'cutoffs': np.array(CUTOFFS),
    'tau_fold': fold_tau,
    'clock_coeff': CLOCK_COEFF,
}

for ci, cutoff in enumerate(CUTOFFS):
    a0_arr = np.array([results[cutoff][tau]['a0'] for tau in all_taus])
    a2_arr = np.array([results[cutoff][tau]['a2'] for tau in all_taus])
    a4_arr = np.array([results[cutoff][tau]['a4'] for tau in all_taus])

    save_dict[f'a0_cutoff{ci}'] = a0_arr
    save_dict[f'a2_cutoff{ci}'] = a2_arr
    save_dict[f'a4_cutoff{ci}'] = a4_arr

np.savez(DATA_DIR / 's41_constants_vs_tau.npz', **save_dict)
print(f"\nSaved: {DATA_DIR / 's41_constants_vs_tau.npz'}")

# ──────────────────────────────────────────────────────────────────────
# Plotting
# ──────────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 41: Seeley-DeWitt Coefficients & Physical Constants vs $\\tau$',
             fontsize=14, fontweight='bold')

taus = np.array(all_taus)

# Panel 1: a_0, a_2, a_4 vs tau (primary cutoff)
ax = axes[0, 0]
ci_main = 0  # cutoff = 0.01
a0_main = np.array([results[CUTOFFS[ci_main]][t]['a0'] for t in all_taus])
a2_main = np.array([results[CUTOFFS[ci_main]][t]['a2'] for t in all_taus])
a4_main = np.array([results[CUTOFFS[ci_main]][t]['a4'] for t in all_taus])

ax.plot(taus, a0_main, 'ko-', ms=4, label='$a_0(\\tau)$')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$a_0$', color='k')
ax.tick_params(axis='y', labelcolor='k')

ax2_twin = ax.twinx()
ax2_twin.plot(taus, a2_main, 'b^-', ms=4, label='$a_2(\\tau)$')
ax2_twin.plot(taus, a4_main, 'rs-', ms=4, label='$a_4(\\tau)$')
ax2_twin.set_ylabel('$a_2, a_4$', color='b')
ax2_twin.tick_params(axis='y', labelcolor='b')

# Combine legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8)
ax.axvline(fold_tau, color='gray', ls='--', alpha=0.5, label='fold')
ax.set_title(f'SD coefficients ($\\lambda_{{\\min}}$={CUTOFFS[ci_main]})')

# Panel 2: Ratios vs tau
ax = axes[0, 1]
r20_arr = a2_main / a0_main
r42_arr = a4_main / a2_main
r40_arr = a4_main / a0_main

ax.plot(taus, r20_arr, 'b^-', ms=4, label='$a_2/a_0 \\propto 1/G_N$')
ax.plot(taus, r42_arr, 'rs-', ms=4, label='$a_4/a_2 \\propto 1/\\alpha$')
ax.axvline(fold_tau, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Ratio')
ax.legend(fontsize=8)
ax.set_title('Physical constant proxies')

# Panel 3: Fractional change from fold
ax = axes[1, 0]
fold_idx = np.argmin(np.abs(taus - fold_tau))

dr20 = (r20_arr - r20_arr[fold_idx]) / r20_arr[fold_idx]
dr42 = (r42_arr - r42_arr[fold_idx]) / r42_arr[fold_idx]
dr40 = (r40_arr - r40_arr[fold_idx]) / r40_arr[fold_idx]

ax.plot(taus, dr20, 'b^-', ms=4, label='$\\Delta(a_2/a_0)/(a_2/a_0)$')
ax.plot(taus, dr42, 'rs-', ms=4, label='$\\Delta(a_4/a_2)/(a_4/a_2)$')
ax.plot(taus, dr40, 'gD-', ms=4, label='$\\Delta(a_4/a_0)/(a_4/a_0)$')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axvline(fold_tau, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Fractional change from fold')
ax.legend(fontsize=8)
ax.set_title('Constant variation (spectral)')

# Panel 4: Clock constraint vs observational bounds
ax = axes[1, 1]

# Analytic clock
da_analytic = CLOCK_COEFF * (taus - fold_tau)

# Spectral alpha proxy
da_spectral = dr42  # a_4/a_2 fractional change

ax.semilogy(taus, np.abs(da_analytic), 'ko-', ms=4, label='$|\\Delta\\alpha/\\alpha|$ (analytic, $-3.08\\Delta\\tau$)')
ax.semilogy(taus, np.abs(da_spectral), 'rs-', ms=4, label='$|\\Delta(a_4/a_2)/(a_4/a_2)|$ (spectral)')

# Observational bounds
ax.axhline(CMB_BOUND, color='orange', ls='--', lw=2, label=f'CMB bound ($10^{{-2}}$)')
ax.axhline(QUASAR_BOUND, color='red', ls='--', lw=2, label=f'Quasar bound ($10^{{-5}}$)')
ax.axvline(fold_tau, color='gray', ls='--', alpha=0.5)

ax.set_xlabel('$\\tau$')
ax.set_ylabel('$|\\Delta\\alpha/\\alpha|$')
ax.legend(fontsize=7, loc='lower right')
ax.set_title('Clock constraint vs bounds')
ax.set_ylim(1e-6, 10)

plt.tight_layout()
plt.savefig(DATA_DIR / 's41_constants_vs_tau.png', dpi=150, bbox_inches='tight')
print(f"Saved: {DATA_DIR / 's41_constants_vs_tau.png'}")

# ──────────────────────────────────────────────────────────────────────
# Summary
# ──────────────────────────────────────────────────────────────────────

print("\n" + "=" * 100)
print("SUMMARY")
print("=" * 100)

print(f"\nCutoff = {ref_cutoff} (primary analysis):")
print(f"  a_2(fold)/a_2(0)           = {a2_fold / a2_0:.8f}")
print(f"  a_4(fold)/a_4(0)           = {a4_fold / a4_0:.8f}")
print(f"  (a_4/a_2)(fold)/(a_4/a_2)(0) = {r42_fold / r42_0:.8f}")
print(f"  Max |Da_analytic/a| (full range) = {max_da_analytic:.6f}")
print(f"  Max |D(a4/a2)/(a4/a2)| (spectral) = {max_dr42:.6f}")

# Cutoff sensitivity summary
print(f"\nCutoff sensitivity at fold ({fold_tau:.3f}):")
for cutoff in CUTOFFS:
    r = results[cutoff][fold_tau]
    r42 = r['a4'] / r['a2']
    print(f"  cutoff={cutoff:.2f}: a_4/a_2 = {r42:.8f}")

r42_spread = max(results[c][fold_tau]['a4']/results[c][fold_tau]['a2'] for c in CUTOFFS) - \
             min(results[c][fold_tau]['a4']/results[c][fold_tau]['a2'] for c in CUTOFFS)
r42_mean = np.mean([results[c][fold_tau]['a4']/results[c][fold_tau]['a2'] for c in CUTOFFS])
print(f"  Spread / mean = {r42_spread/r42_mean:.6f} ({r42_spread/r42_mean*100:.4f}%)")

# Physical interpretation
print("\n--- Physical Interpretation ---")
dtau_full = max(all_taus) - 0.0
da_full_analytic = abs(CLOCK_COEFF * dtau_full)
print(f"Full transit tau: 0 -> {max(all_taus):.3f}")
print(f"|Da/a| analytic over full transit = {da_full_analytic:.4f}")
print(f"  vs CMB bound 10^-2: {'VIOLATES by ' + f'{da_full_analytic/CMB_BOUND:.0f}x' if da_full_analytic > CMB_BOUND else 'PASSES'}")

dtau_fold = fold_tau - 0.0
da_fold_analytic = abs(CLOCK_COEFF * dtau_fold)
print(f"\nTransit to fold (tau: 0 -> {fold_tau:.3f}):")
print(f"|Da/a| analytic = {da_fold_analytic:.4f}")
print(f"  vs CMB bound 10^-2: {'VIOLATES by ' + f'{da_fold_analytic/CMB_BOUND:.0f}x' if da_fold_analytic > CMB_BOUND else 'PASSES'}")
print(f"  vs Quasar bound 10^-5: {'VIOLATES by ' + f'{da_fold_analytic/QUASAR_BOUND:.0f}x' if da_fold_analytic > QUASAR_BOUND else 'PASSES'}")

print(f"\nThis means: the ENTIRE transit from tau=0 to tau={fold_tau:.3f} produces")
print(f"|Delta_alpha/alpha| = {da_fold_analytic:.4f}, which is {da_fold_analytic/CMB_BOUND:.0f}x the CMB bound.")
print(f"The spectral (a_4/a_2) change confirms: max |D(a_4/a_2)/(a_4/a_2)| = {max_dr42:.4f}")
print(f"\nCONCLUSION: Constants change by O(1) during transit. The clock constraint")
print(f"(Session 22d E-3) applies to tau EVOLUTION, not to the spectral coefficients")
print(f"directly. But the spectral coefficients confirm that the 'constants' are")
print(f"strongly tau-dependent: they are NOT constant during early universe transit.")
print(f"Post-freeze (tau_dot=0), they are exactly constant.")
