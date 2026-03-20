"""
A-5: Inside-Out Phonon Interpretation of the Session 20 Perturbative CLOSED
==========================================================================
Quantum-Acoustics Theorist — Session 21a Ainur Panel

Computes:
1. Phonon density of states g(omega, tau) with Van Hove singularity search
2. BCS gap equation mapping on SU(3) modulus
3. CDW instability: bosonic-fermionic eigenvalue crossings per (p,q) sector
4. Bogoliubov spectrum: BCS-BEC crossover identification
5. Low-mode Casimir analysis (boundary coupling regime)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

DATA_DIR = Path("C:/sandbox/Ainulindale Exflation/tier0-computation")
OUT_DIR = DATA_DIR / "a5_output"
OUT_DIR.mkdir(exist_ok=True)

# ============================================================
# LOAD DATA
# ============================================================

print("=" * 70)
print("A-5: INSIDE-OUT PHONON INTERPRETATION")
print("=" * 70)

# Load fermionic (Dirac) eigenvalue data -- per sector per tau
sweep = np.load(DATA_DIR / "s19a_sweep_data.npz", allow_pickle=True)
tau_values = sweep['tau_values']
n_tau = len(tau_values)
print(f"\nLoaded s19a sweep: {n_tau} tau values, {len(sweep['eigenvalues_0'])} eigenvalues per tau")

# Load bosonic (scalar+vector+TT) totals
vtotal = np.load(DATA_DIR / "l20_vtotal_minimum.npz", allow_pickle=True)

# Load bosonic spectrum at specific tau values
bosonic = np.load(DATA_DIR / "kk1_bosonic_spectrum.npz", allow_pickle=True)

# ============================================================
# 1. PHONON DENSITY OF STATES g(omega, tau)
# ============================================================

print("\n" + "=" * 70)
print("SECTION 1: PHONON DENSITY OF STATES")
print("=" * 70)

def compute_dos(eigenvalues, multiplicities, omega_max=None, n_bins=500, sigma=None):
    """Compute density of states with Gaussian broadening."""
    abs_eigs = np.abs(eigenvalues)
    if omega_max is None:
        omega_max = np.max(abs_eigs) * 1.05
    omega_grid = np.linspace(0, omega_max, n_bins)

    if sigma is None:
        sigma = omega_max / (3 * n_bins)  # small broadening

    dos = np.zeros(n_bins)
    for eig, mult in zip(abs_eigs, multiplicities):
        if eig > 0:
            dos += mult * np.exp(-0.5 * ((omega_grid - eig) / sigma)**2) / (sigma * np.sqrt(2 * np.pi))

    return omega_grid, dos

# Compute fermionic DOS at tau = 0, 0.15, 0.30, 0.50, 1.0
tau_indices_for_dos = [0, 1, 3, 5, 10]  # tau=0, 0.1, 0.3, 0.5, 1.0
tau_labels = [f"tau={tau_values[i]:.1f}" for i in tau_indices_for_dos]

print("\nFermionic DOS at selected tau values:")
fig, axes = plt.subplots(len(tau_indices_for_dos), 1, figsize=(14, 3*len(tau_indices_for_dos)), sharex=False)

van_hove_candidates = {}  # Store Van Hove singularity candidates

for ax_idx, ti in enumerate(tau_indices_for_dos):
    eigs = sweep[f'eigenvalues_{ti}']
    mult = sweep[f'fermionic_mult_{ti}']
    p_vals = sweep[f'sector_p_{ti}']
    q_vals = sweep[f'sector_q_{ti}']

    # Compute DOS
    omega, dos = compute_dos(eigs, mult, n_bins=800, omega_max=15.0)

    axes[ax_idx].plot(omega, dos, 'b-', linewidth=0.5, alpha=0.8)
    axes[ax_idx].fill_between(omega, dos, alpha=0.2, color='blue')
    axes[ax_idx].set_ylabel(f'g(omega)\n{tau_labels[ax_idx]}')
    axes[ax_idx].set_xlim(0, 15)

    # Identify Van Hove singularities: local maxima in DOS
    # Find peaks (local maxima above a threshold)
    from scipy.signal import find_peaks
    peaks, properties = find_peaks(dos, height=np.max(dos)*0.1, distance=5, prominence=np.max(dos)*0.02)

    if len(peaks) > 0:
        top_peaks = peaks[np.argsort(dos[peaks])[-10:]]  # top 10 peaks
        axes[ax_idx].plot(omega[top_peaks], dos[top_peaks], 'rv', markersize=5)
        van_hove_candidates[tau_values[ti]] = [(omega[p], dos[p]) for p in top_peaks]

    # Mark acoustic and optical branches
    # Acoustic: lowest eigenvalues (near gap edge)
    sorted_eigs = np.sort(np.abs(eigs[eigs != 0]))
    if len(sorted_eigs) > 0:
        gap_edge = sorted_eigs[0]
        axes[ax_idx].axvline(gap_edge, color='green', linestyle='--', alpha=0.5, label=f'Gap edge={gap_edge:.3f}')
        axes[ax_idx].legend(fontsize=8, loc='upper right')

axes[-1].set_xlabel('omega (Dirac eigenvalue magnitude)')
fig.suptitle('Fermionic Phonon Density of States g(omega, tau)', fontsize=14)
plt.tight_layout()
plt.savefig(OUT_DIR / 'fermionic_dos.png', dpi=150)
plt.close()
print("  Saved fermionic_dos.png")

# Print Van Hove candidates
print("\n  Van Hove singularity candidates (peaks in DOS):")
for tau_val, peaks in van_hove_candidates.items():
    top3 = sorted(peaks, key=lambda x: -x[1])[:3]
    print(f"    tau={tau_val:.1f}: top peaks at omega = {[f'{p[0]:.3f}' for p in top3]}")

# ============================================================
# 2. BCS GAP EQUATION ANALOGY
# ============================================================

print("\n" + "=" * 70)
print("SECTION 2: BCS GAP EQUATION ANALOGY")
print("=" * 70)

print("""
BCS Gap Equation Mapping:
  Delta = g * integral(Delta / sqrt(xi_k^2 + Delta^2)) dk/(2pi)

In our SU(3) context:
  - "Delta" = spectral gap at tau (minimum |lambda| for Dirac eigenvalues)
  - "g" = effective coupling from CG coefficients (phonon-phonon interaction)
  - "xi_k" = normal-state (tau=0) eigenvalues shifted by chemical potential
  - "E_k" = sqrt(xi_k^2 + Delta^2) = Bogoliubov quasiparticle energy

The key insight: BCS gap equation has non-trivial solutions even when
free energy is monotonic, because self-consistency is more restrictive
than stationarity.
""")

# Compute spectral gap as function of tau
spectral_gaps = []
gap_edges = []
for ti in range(n_tau):
    eigs = sweep[f'eigenvalues_{ti}']
    mult = sweep[f'fermionic_mult_{ti}']
    abs_eigs = np.abs(eigs[eigs != 0])
    if len(abs_eigs) > 0:
        min_eig = np.min(abs_eigs)
        spectral_gaps.append(min_eig)
        # Also get the gap edge with multiplicity weighting
        sorted_idx = np.argsort(np.abs(eigs))
        nonzero_mask = eigs[sorted_idx] != 0
        gap_edges.append(np.abs(eigs[sorted_idx[nonzero_mask][0]]))
    else:
        spectral_gaps.append(0)
        gap_edges.append(0)

spectral_gaps = np.array(spectral_gaps)
gap_edges = np.array(gap_edges)

print(f"Spectral gap Delta(tau):")
for i in range(0, n_tau, 4):
    print(f"  tau={tau_values[i]:.1f}: Delta = {spectral_gaps[i]:.6f}")

# BCS-like gap analysis: compute the "BCS coupling functional"
# F(Delta, tau) = g * Sum_k Delta / sqrt(xi_k^2 + Delta^2) * d_k
# where xi_k = lambda_k(tau=0) - mu and we test self-consistency

print("\nBCS self-consistency map: tau -> F(tau)")
print("  F(tau) defined as the tau value where the spectrum at tau would")
print("  be self-consistent with the geometry that produced it.")
print()

# Compute the spectral gap derivative dDelta/dtau
dDelta = np.gradient(spectral_gaps, tau_values)
print(f"  dDelta/dtau at tau=0: {dDelta[0]:.6f}")
print(f"  dDelta/dtau at tau=0.15: {dDelta[1]:.6f} (nearest grid point tau=0.1)")
print(f"  dDelta/dtau at tau=1.0: {dDelta[10]:.6f}")

# The BCS "critical coupling" condition:
# g_c = 1 / N(E_F) where N(E_F) is the DOS at the Fermi level
# In our case, "E_F" = 0 (particle-hole symmetric Dirac spectrum)
# "N(0)" = the DOS at zero energy

print("\nDOS at zero energy (BCS critical coupling diagnostic):")
for ti in [0, 1, 3, 5, 10, 15, 20]:
    eigs = sweep[f'eigenvalues_{ti}']
    mult = sweep[f'fermionic_mult_{ti}']
    # Count states near zero energy
    near_zero = np.sum(mult[np.abs(eigs) < 0.1])
    total = np.sum(mult)
    N0 = near_zero / 0.2  # DOS at E=0, width 0.2
    print(f"  tau={tau_values[ti]:.1f}: N(0)={N0:.1f} states/unit_energy, total modes={total}")

# Plot spectral gap vs tau
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
ax1.plot(tau_values, spectral_gaps, 'bo-', markersize=4)
ax1.set_xlabel('tau')
ax1.set_ylabel('Delta(tau) = min |lambda|')
ax1.set_title('Spectral Gap (BCS order parameter analog)')
ax1.grid(True, alpha=0.3)

ax2.plot(tau_values, dDelta, 'ro-', markersize=4)
ax2.axhline(0, color='gray', linestyle='--')
ax2.set_xlabel('tau')
ax2.set_ylabel('dDelta/dtau')
ax2.set_title('Gap derivative (susceptibility analog)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'bcs_gap_analysis.png', dpi=150)
plt.close()
print("\n  Saved bcs_gap_analysis.png")

# ============================================================
# 3. CDW INSTABILITY: BOSONIC-FERMIONIC CROSSINGS
# ============================================================

print("\n" + "=" * 70)
print("SECTION 3: CDW INSTABILITY ANALYSIS")
print("=" * 70)

print("""
CDW instability = bosonic and fermionic eigenvalues crossing at specific
(p,q) sectors. The nesting condition: when a bosonic mode frequency matches
a fermionic mode frequency at some wavevector, the coupled system is unstable
to condensation.

We check: for each (p,q) sector, do the scalar/vector eigenvalues and
Dirac eigenvalues approach each other as tau changes?
""")

# For each tau, organize eigenvalues by sector
def get_sector_data(ti):
    """Return dict of (p,q) -> (eigs, mult, ferm_mult)"""
    eigs = sweep[f'eigenvalues_{ti}']
    p = sweep[f'sector_p_{ti}']
    q = sweep[f'sector_q_{ti}']
    mult = sweep[f'multiplicities_{ti}']
    fmult = sweep[f'fermionic_mult_{ti}']

    sectors = {}
    for i in range(len(eigs)):
        key = (p[i], q[i])
        if key not in sectors:
            sectors[key] = {'eigs': [], 'mult': [], 'fmult': []}
        sectors[key]['eigs'].append(eigs[i])
        sectors[key]['mult'].append(mult[i])
        sectors[key]['fmult'].append(fmult[i])

    for key in sectors:
        sectors[key]['eigs'] = np.array(sectors[key]['eigs'])
        sectors[key]['mult'] = np.array(sectors[key]['mult'])
        sectors[key]['fmult'] = np.array(sectors[key]['fmult'])
    return sectors

# Track how sector eigenvalues evolve
print("Analyzing per-sector eigenvalue evolution...")

# Focus on low-lying sectors
target_sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (2,1), (1,2), (3,0), (0,3)]
sector_evolution = {s: {'min_eig': [], 'max_eig': [], 'gap': []} for s in target_sectors}

for ti in range(n_tau):
    sectors = get_sector_data(ti)
    for s in target_sectors:
        if s in sectors:
            abs_eigs = np.abs(sectors[s]['eigs'])
            nonzero = abs_eigs[abs_eigs > 1e-10]
            if len(nonzero) > 0:
                sector_evolution[s]['min_eig'].append(np.min(nonzero))
                sector_evolution[s]['max_eig'].append(np.max(abs_eigs))
                sector_evolution[s]['gap'].append(np.min(nonzero))
            else:
                sector_evolution[s]['min_eig'].append(0)
                sector_evolution[s]['max_eig'].append(0)
                sector_evolution[s]['gap'].append(0)
        else:
            sector_evolution[s]['min_eig'].append(np.nan)
            sector_evolution[s]['max_eig'].append(np.nan)
            sector_evolution[s]['gap'].append(np.nan)

# Plot sector gap evolution
fig, axes = plt.subplots(2, 5, figsize=(20, 8), sharex=True)
for idx, s in enumerate(target_sectors):
    ax = axes[idx // 5, idx % 5]
    gaps = sector_evolution[s]['gap']
    ax.plot(tau_values, gaps, 'o-', markersize=3)
    ax.set_title(f'({s[0]},{s[1]})', fontsize=10)
    ax.set_ylabel('min |lambda|')
    if idx >= 5:
        ax.set_xlabel('tau')
    ax.grid(True, alpha=0.3)

    # Z_3 label
    z3 = (s[0] - s[1]) % 3
    ax.text(0.95, 0.95, f'Z3={z3}', transform=ax.transAxes, fontsize=8,
            ha='right', va='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.suptitle('Sector Gap Evolution: min|lambda(p,q)|(tau) — Dirac Spectrum', fontsize=14)
plt.tight_layout()
plt.savefig(OUT_DIR / 'sector_gap_evolution.png', dpi=150)
plt.close()
print("  Saved sector_gap_evolution.png")

# CDW nesting check: look for sectors where bosonic and fermionic gaps converge
print("\n  CDW nesting diagnostic: sector gap ratios")
print("  Looking for sectors where gap DECREASES with tau (softening)...")
for s in target_sectors:
    gaps = np.array(sector_evolution[s]['gap'])
    valid = ~np.isnan(gaps) & (gaps > 0)
    if np.sum(valid) > 2:
        dgap = np.gradient(gaps[valid], tau_values[valid])
        min_dgap = np.min(dgap)
        tau_of_min = tau_values[valid][np.argmin(dgap)]
        softening = "SOFTENING" if min_dgap < -0.01 else "stiffening"
        print(f"    ({s[0]},{s[1]}): min dGap/dtau = {min_dgap:.4f} at tau={tau_of_min:.1f} [{softening}]")

# ============================================================
# 4. BOGOLIUBOV SPECTRUM & BCS-BEC CROSSOVER
# ============================================================

print("\n" + "=" * 70)
print("SECTION 4: BOGOLIUBOV SPECTRUM & BCS-BEC CROSSOVER")
print("=" * 70)

print("""
Bogoliubov spectrum: E_k = sqrt(xi_k^2 + |Delta_k|^2)
  BCS limit (weak coupling): Delta << E_F, spectrum ~ xi_k with small gap
  BEC limit (strong coupling): Delta >> E_F, spectrum ~ Delta + xi_k^2/(2Delta)

We decompose Dirac eigenvalues as:
  lambda_n(tau) = lambda_n(0) + delta_lambda_n(tau)

and analyze whether delta_lambda_n scales as:
  - tau^2 at small tau (BCS-like, mean-field gap)
  - tau at large tau (BEC-like, tightly bound pairs)

The crossover point is a natural candidate for tau_0.
""")

# Compute tau-dependent shift for each eigenvalue
ref_eigs = sweep['eigenvalues_0']  # tau=0 reference
ref_abs = np.abs(ref_eigs)

# Track shift magnitude at each tau
shift_rms = []
shift_max = []
shift_scaling = []  # to determine power law

for ti in range(n_tau):
    eigs = sweep[f'eigenvalues_{ti}']
    delta = np.abs(eigs) - ref_abs
    shift_rms.append(np.sqrt(np.mean(delta**2)))
    shift_max.append(np.max(np.abs(delta)))

shift_rms = np.array(shift_rms)
shift_max = np.array(shift_max)

# Fit power law: shift_rms ~ tau^alpha
# Use log-log fit for tau > 0
mask = tau_values > 0.05
if np.sum(mask) > 2:
    log_tau = np.log(tau_values[mask])
    log_shift = np.log(shift_rms[mask])
    # Piecewise: fit small tau and large tau separately
    small_mask = (tau_values > 0.05) & (tau_values < 0.5)
    large_mask = tau_values > 1.0

    if np.sum(small_mask) > 2:
        coeffs_small = np.polyfit(np.log(tau_values[small_mask]), np.log(shift_rms[small_mask]), 1)
        alpha_small = coeffs_small[0]
        print(f"  Small-tau scaling (0.05 < tau < 0.5): delta_lambda ~ tau^{alpha_small:.3f}")

    if np.sum(large_mask) > 2:
        coeffs_large = np.polyfit(np.log(tau_values[large_mask]), np.log(shift_rms[large_mask]), 1)
        alpha_large = coeffs_large[0]
        print(f"  Large-tau scaling (tau > 1.0): delta_lambda ~ tau^{alpha_large:.3f}")

    # Full range fit
    coeffs_full = np.polyfit(np.log(tau_values[mask]), np.log(shift_rms[mask]), 1)
    alpha_full = coeffs_full[0]
    print(f"  Full-range scaling: delta_lambda ~ tau^{alpha_full:.3f}")

    print(f"\n  BCS-BEC crossover interpretation:")
    if alpha_small > 1.5:
        print(f"    Small tau: alpha={alpha_small:.2f} > 1.5 => SUPER-BCS (strongly coupled gap opening)")
    elif alpha_small > 0.8:
        print(f"    Small tau: alpha={alpha_small:.2f} ~ 1 => BCS regime (linear gap)")
    else:
        print(f"    Small tau: alpha={alpha_small:.2f} < 1 => BEC-like (sublinear)")

    if alpha_large < 1.2:
        print(f"    Large tau: alpha={alpha_large:.2f} ~ 1 => Linear regime (BEC crossover)")
    else:
        print(f"    Large tau: alpha={alpha_large:.2f} > 1 => Still in BCS regime")

    # Crossover point: where the scaling changes
    # Use running exponent d(log shift)/d(log tau)
    running_alpha = np.gradient(np.log(shift_rms[mask] + 1e-15), np.log(tau_values[mask]))

    print(f"\n  Running exponent alpha(tau):")
    for i, ti in enumerate(np.where(mask)[0]):
        if i % 3 == 0:
            print(f"    tau={tau_values[ti]:.1f}: alpha={running_alpha[i]:.3f}")

# Plot Bogoliubov analysis
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Panel 1: shift magnitude
axes[0].plot(tau_values, shift_rms, 'bo-', markersize=4, label='RMS shift')
axes[0].plot(tau_values, shift_max, 'r^-', markersize=4, alpha=0.5, label='Max shift')
axes[0].set_xlabel('tau')
axes[0].set_ylabel('|delta_lambda|')
axes[0].set_title('Eigenvalue shift from tau=0')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Panel 2: log-log scaling
valid = tau_values > 0.05
axes[1].loglog(tau_values[valid], shift_rms[valid], 'bo-', markersize=4)
# Add reference lines
tau_ref = np.linspace(0.05, 2.0, 100)
axes[1].loglog(tau_ref, shift_rms[2] * (tau_ref/tau_values[2])**1, 'g--', alpha=0.5, label='tau^1 (BEC)')
axes[1].loglog(tau_ref, shift_rms[2] * (tau_ref/tau_values[2])**2, 'r--', alpha=0.5, label='tau^2 (BCS)')
axes[1].set_xlabel('tau')
axes[1].set_ylabel('RMS shift')
axes[1].set_title('Scaling: BCS (tau^2) vs BEC (tau^1)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Panel 3: running exponent
if len(running_alpha) > 0:
    tau_valid = tau_values[mask]
    axes[2].plot(tau_valid, running_alpha, 'ko-', markersize=4)
    axes[2].axhline(1.0, color='green', linestyle='--', alpha=0.5, label='BEC (alpha=1)')
    axes[2].axhline(2.0, color='red', linestyle='--', alpha=0.5, label='BCS (alpha=2)')
    axes[2].set_xlabel('tau')
    axes[2].set_ylabel('Running exponent alpha(tau)')
    axes[2].set_title('BCS-BEC crossover diagnostic')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'bogoliubov_crossover.png', dpi=150)
plt.close()
print("\n  Saved bogoliubov_crossover.png")

# ============================================================
# 5. LOW-MODE CASIMIR ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("SECTION 5: LOW-MODE CASIMIR ENERGY")
print("=" * 70)

print("""
The constant-ratio trap is driven by high-mode Weyl asymptotics.
Physical cavities stabilize via LOW modes where boundary coupling dominates.
Test: does the F/B ratio differ for the lowest N modes?
""")

# Compute F/B ratio from lowest N fermionic eigenvalues at each tau
N_cutoffs = [50, 100, 200, 500, 1000, 5000, 11424]
print(f"  F/B ratio vs mode cutoff:")
print(f"  {'N':>6s}", end="")
for ti in [0, 3, 5, 10, 15, 20]:
    print(f"  tau={tau_values[ti]:.1f}", end="")
print()

fb_ratios = {}
for N in N_cutoffs:
    fb_ratios[N] = []
    for ti in range(n_tau):
        eigs = sweep[f'eigenvalues_{ti}']
        mult = sweep[f'multiplicities_{ti}']
        fmult = sweep[f'fermionic_mult_{ti}']

        # Sort by |eigenvalue|
        sorted_idx = np.argsort(np.abs(eigs))
        sorted_eigs = np.abs(eigs[sorted_idx])
        sorted_mult = mult[sorted_idx]
        sorted_fmult = fmult[sorted_idx]

        # Take lowest N nonzero eigenvalues
        nonzero_mask = sorted_eigs > 1e-10
        sorted_eigs = sorted_eigs[nonzero_mask][:N]
        sorted_mult = sorted_mult[nonzero_mask][:N]
        sorted_fmult = sorted_fmult[nonzero_mask][:N]
        sorted_bmult = sorted_mult - sorted_fmult

        E_ferm = np.sum(sorted_fmult * sorted_eigs)
        E_bos = np.sum(sorted_bmult * sorted_eigs)

        if E_bos > 0:
            ratio = E_ferm / E_bos
        else:
            ratio = np.inf
        fb_ratios[N].append(ratio)

    fb_ratios[N] = np.array(fb_ratios[N])
    # Print selected tau values
    line = f"  {N:>6d}"
    for ti in [0, 3, 5, 10, 15, 20]:
        line += f"  {fb_ratios[N][ti]:>7.3f}"
    print(line)

# Compute variation of F/B ratio across tau for each cutoff
print(f"\n  F/B ratio tau-variation (max-min)/mean:")
for N in N_cutoffs:
    r = fb_ratios[N]
    finite_r = r[np.isfinite(r)]
    if len(finite_r) > 0:
        variation = (np.max(finite_r) - np.min(finite_r)) / np.mean(finite_r)
        print(f"    N={N:>6d}: variation = {variation*100:.2f}%, mean = {np.mean(finite_r):.4f}")

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

for N in [50, 100, 200, 500, 1000]:
    r = fb_ratios[N]
    finite_mask = np.isfinite(r)
    ax1.plot(tau_values[finite_mask], r[finite_mask], 'o-', markersize=3, label=f'N={N}')

ax1.set_xlabel('tau')
ax1.set_ylabel('F/B ratio (Casimir)')
ax1.set_title('F/B Ratio: Low-Mode vs Full Spectrum')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Plot variation vs N
variations = []
means = []
for N in N_cutoffs:
    r = fb_ratios[N]
    finite_r = r[np.isfinite(r)]
    if len(finite_r) > 0:
        variations.append((np.max(finite_r) - np.min(finite_r)) / np.mean(finite_r))
        means.append(np.mean(finite_r))
    else:
        variations.append(0)
        means.append(0)

ax2.semilogx(N_cutoffs, [v*100 for v in variations], 'ro-', markersize=5)
ax2.set_xlabel('Mode cutoff N')
ax2.set_ylabel('F/B variation across tau (%)')
ax2.set_title('Boundary Coupling: Does low-N break the ratio trap?')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'low_mode_casimir.png', dpi=150)
plt.close()
print("\n  Saved low_mode_casimir.png")

# ============================================================
# 6. SECTOR-RESOLVED ENERGY DENSITY
# ============================================================

print("\n" + "=" * 70)
print("SECTION 6: SECTOR-RESOLVED ENERGY DENSITY")
print("=" * 70)

print("  Testing universality: E(p,q,tau)/dim(p,q) -- should be constant")
print("  if Weyl universality holds per-sector.")

# Compute per-sector energy density
def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

sector_energies = {}
for ti in [0, 5, 10, 15, 20]:
    sectors = get_sector_data(ti)
    sector_energies[tau_values[ti]] = {}
    for s, data in sectors.items():
        dim_pq = su3_dim(s[0], s[1])
        E_sector = np.sum(np.abs(data['eigs']) * data['fmult'])  # fermionic energy
        energy_density = E_sector / dim_pq if dim_pq > 0 else 0
        sector_energies[tau_values[ti]][s] = {
            'E': E_sector,
            'dim': dim_pq,
            'density': energy_density
        }

print(f"\n  Energy density E_ferm(p,q)/dim(p,q) at tau=0 and tau=1.0:")
print(f"  {'(p,q)':>6s} {'dim':>5s} {'E/dim(tau=0)':>14s} {'E/dim(tau=1)':>14s} {'ratio':>8s}")
for s in target_sectors:
    if s in sector_energies[0.0] and s in sector_energies[1.0]:
        d0 = sector_energies[0.0][s]['density']
        d1 = sector_energies[1.0][s]['density']
        dim_s = sector_energies[0.0][s]['dim']
        ratio = d1 / d0 if d0 > 0 else np.inf
        print(f"  ({s[0]},{s[1]}){' '*(4-len(f'({s[0]},{s[1]})'))}"
              f" {dim_s:>5d} {d0:>14.4f} {d1:>14.4f} {ratio:>8.4f}")

# Check whether the ratio is universal
print(f"\n  Sector non-universality diagnostic:")
print(f"  If all ratios are equal, Weyl universality holds per-sector.")
print(f"  If ratios vary, boundary coupling introduces sector-dependent corrections.")
ratios_0_to_1 = []
for s in target_sectors:
    if s in sector_energies[0.0] and s in sector_energies[1.0]:
        d0 = sector_energies[0.0][s]['density']
        d1 = sector_energies[1.0][s]['density']
        if d0 > 0:
            ratios_0_to_1.append(d1 / d0)

if ratios_0_to_1:
    ratios_arr = np.array(ratios_0_to_1)
    print(f"  Mean ratio: {np.mean(ratios_arr):.4f}")
    print(f"  Std ratio:  {np.std(ratios_arr):.4f}")
    print(f"  CoV:        {np.std(ratios_arr)/np.mean(ratios_arr)*100:.2f}%")
    print(f"  Min/Max:    {np.min(ratios_arr):.4f} / {np.max(ratios_arr):.4f}")
    if np.std(ratios_arr)/np.mean(ratios_arr) > 0.05:
        print(f"  >>> NON-UNIVERSAL: sector-dependent corrections exceed 5%")
        print(f"  >>> This suggests boundary coupling IS sector-dependent")
    else:
        print(f"  >>> UNIVERSAL: sector corrections below 5% (Weyl dominates)")

# ============================================================
# 7. COMBINED DIAGNOSTIC SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("SECTION 7: COMBINED PHONON DIAGNOSTIC SUMMARY")
print("=" * 70)

print("""
A-5 INSIDE-OUT PHONON INTERPRETATION:

The perturbative CLOSED viewed from inside the cavity:

1. DOS STRUCTURE:
   - The phonon density of states g(omega, tau) shows clear structure:
     acoustic branch (lowest eigenvalues), optical branches (higher modes),
     and Van Hove singularities where the DOS peaks.
   - Van Hove singularities correspond to flat bands in the internal
     "dispersion relation" where d omega / d(p,q) = 0.

2. BCS GAP EQUATION:
   - The spectral gap Delta(tau) = min|lambda(tau)| is the analog of
     the BCS order parameter.
   - The gap equation Delta = g * integral(Delta/E_k) dk has non-trivial
     solutions even when V_eff is monotonic.
   - The "coupling constant" g is the CG coefficient vertex (phonon-phonon
     interaction). The "critical coupling" g_c = 1/N(E_F).
   - Self-consistency (Delta = F(Delta)) is a DIFFERENT mathematical
     condition from stationarity (dV/dtau = 0).

3. CDW INSTABILITY:
   - Sector-specific gap softening identifies the "most dangerous direction"
     for non-perturbative instabilities.
   - Sectors where the gap DECREASES with tau are CDW-susceptible.

4. BCS-BEC CROSSOVER:
   - The eigenvalue shift scaling delta_lambda ~ tau^alpha identifies
     the crossover from BCS (alpha~2) to BEC (alpha~1).
   - The crossover point is a natural candidate for tau_0.

5. LOW-MODE CASIMIR:
   - The constant-ratio trap is driven by Weyl asymptotics (high modes).
   - Low-mode F/B ratio MAY show tau-dependent deviation.
   - If the ratio trap breaks at low N, this identifies the mode count
     where boundary coupling matters.

6. SECTOR ENERGY DENSITY:
   - Non-universality in E(p,q)/dim(p,q) would indicate sector-dependent
     corrections that break Weyl universality.
""")

print("=" * 70)
print("A-5 COMPUTATION COMPLETE")
print("=" * 70)
