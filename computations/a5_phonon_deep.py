"""
A-5 Deep Analysis: Focused follow-up on key findings from initial scan.

1. Van Hove singularity evolution (tracking peak migration)
2. CDW softening: (0,0) and (3,0) sectors show STRONG softening
3. BCS-BEC INVERTED scaling (sub-linear at small tau, super-linear at large tau)
4. BCS gap equation: quantitative self-consistency map
5. Per-sector F/B analysis using BOSONIC data
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from pathlib import Path

DATA_DIR = Path("C:/sandbox/Ainulindale Exflation/tier0-computation")
OUT_DIR = DATA_DIR / "a5_output"
OUT_DIR.mkdir(exist_ok=True)

sweep = np.load(DATA_DIR / "s19a_sweep_data.npz", allow_pickle=True)
tau_values = sweep['tau_values']
n_tau = len(tau_values)

vtotal = np.load(DATA_DIR / "l20_vtotal_minimum.npz", allow_pickle=True)
bosonic = np.load(DATA_DIR / "kk1_bosonic_spectrum.npz", allow_pickle=True)

print("=" * 70)
print("A-5 DEEP ANALYSIS")
print("=" * 70)

# ============================================================
# 1. VAN HOVE SINGULARITY EVOLUTION
# ============================================================

print("\n--- 1. VAN HOVE SINGULARITY TRACKING ---")

# Track the top 3 DOS peaks as function of tau
peak_tracking = {i: {'omega': [], 'height': []} for i in range(5)}

for ti in range(n_tau):
    eigs = sweep[f'eigenvalues_{ti}']
    fmult = sweep[f'fermionic_mult_{ti}']

    # Compute DOS
    abs_eigs = np.abs(eigs)
    omega_max = 15.0
    n_bins = 800
    sigma = omega_max / (3 * n_bins)
    omega_grid = np.linspace(0, omega_max, n_bins)

    dos = np.zeros(n_bins)
    for eig, m in zip(abs_eigs, fmult):
        if eig > 0.01 and m > 0:
            dos += m * np.exp(-0.5 * ((omega_grid - eig) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

    peaks, props = find_peaks(dos, height=np.max(dos) * 0.05, distance=5, prominence=np.max(dos) * 0.01)

    if len(peaks) > 0:
        top_idx = np.argsort(dos[peaks])[-5:]  # top 5
        top_peaks = peaks[top_idx]
        top_peaks_sorted = top_peaks[np.argsort(omega_grid[top_peaks])]  # sort by frequency

        for i in range(min(5, len(top_peaks_sorted))):
            peak_tracking[i]['omega'].append(omega_grid[top_peaks_sorted[i]])
            peak_tracking[i]['height'].append(dos[top_peaks_sorted[i]])
    else:
        for i in range(5):
            peak_tracking[i]['omega'].append(np.nan)
            peak_tracking[i]['height'].append(np.nan)

print("Van Hove peak evolution (5 dominant peaks):")
print(f"  {'tau':>5s}", end="")
for i in range(5):
    print(f"  {'peak'+str(i):>8s}", end="")
print()
for ti in range(0, n_tau, 4):
    print(f"  {tau_values[ti]:5.1f}", end="")
    for i in range(5):
        if ti < len(peak_tracking[i]['omega']):
            print(f"  {peak_tracking[i]['omega'][ti]:8.3f}", end="")
        else:
            print(f"  {'N/A':>8s}", end="")
    print()

# Plot peak migration
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
colors = ['b', 'r', 'g', 'm', 'c']
for i in range(5):
    om = np.array(peak_tracking[i]['omega'])
    valid = ~np.isnan(om)
    if np.sum(valid) > 2:
        ax1.plot(tau_values[valid], om[valid], 'o-', color=colors[i],
                 markersize=3, label=f'Peak {i}')
        ht = np.array(peak_tracking[i]['height'])
        ax2.plot(tau_values[valid], ht[valid], 'o-', color=colors[i],
                 markersize=3, label=f'Peak {i}')

ax1.set_xlabel('tau')
ax1.set_ylabel('omega (peak position)')
ax1.set_title('Van Hove Peak Migration')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.set_xlabel('tau')
ax2.set_ylabel('DOS height at peak')
ax2.set_title('Van Hove Peak Intensity')
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'van_hove_evolution.png', dpi=150)
plt.close()
print("  Saved van_hove_evolution.png")

# ============================================================
# 2. CDW SOFTENING DEEP DIVE
# ============================================================

print("\n--- 2. CDW SOFTENING: SECTORS (0,0) AND (3,0) ---")

def get_sector_eigenvalues(ti, target_p, target_q):
    """Get eigenvalues for a specific (p,q) sector at tau index ti."""
    eigs = sweep[f'eigenvalues_{ti}']
    p = sweep[f'sector_p_{ti}']
    q = sweep[f'sector_q_{ti}']
    fmult = sweep[f'fermionic_mult_{ti}']
    mask = (p == target_p) & (q == target_q)
    return eigs[mask], fmult[mask]

# Track individual eigenvalue levels in (0,0) and (3,0) sectors
print("\n  (0,0) sector: lowest 5 eigenvalue magnitudes vs tau")
for s_p, s_q in [(0, 0), (3, 0), (0, 3), (1, 1), (2, 1)]:
    print(f"\n  Sector ({s_p},{s_q}):")
    print(f"  {'tau':>5s}", end="")
    for i in range(5):
        print(f"  {'lam'+str(i):>8s}", end="")
    print()

    for ti in range(0, n_tau, 2):
        eigs, fmult = get_sector_eigenvalues(ti, s_p, s_q)
        sorted_eigs = np.sort(np.abs(eigs))
        nonzero = sorted_eigs[sorted_eigs > 1e-10]
        print(f"  {tau_values[ti]:5.1f}", end="")
        for i in range(min(5, len(nonzero))):
            print(f"  {nonzero[i]:8.4f}", end="")
        print()

# The golden ratio diagnostic: m(3,0)/m(0,0) vs tau
print("\n  PHI DIAGNOSTIC: m(3,0)/m(0,0) ratio vs tau")
print(f"  {'tau':>5s} {'m(0,0)':>10s} {'m(3,0)':>10s} {'ratio':>10s} {'|ratio-phi|':>12s}")
phi = (1 + np.sqrt(5)) / 2  # 1.6180339887...
phi_paasch = 1.53158  # the Paasch version

phi_ratios = []
for ti in range(n_tau):
    eigs_00, _ = get_sector_eigenvalues(ti, 0, 0)
    eigs_30, _ = get_sector_eigenvalues(ti, 3, 0)

    m00 = np.min(np.abs(eigs_00[np.abs(eigs_00) > 1e-10]))
    m30 = np.min(np.abs(eigs_30[np.abs(eigs_30) > 1e-10]))

    ratio = m30 / m00
    phi_ratios.append(ratio)

    if ti % 3 == 0 or abs(ratio - phi_paasch) < 0.01:
        marker = " <<<" if abs(ratio - phi_paasch) < 0.01 else ""
        print(f"  {tau_values[ti]:5.1f} {m00:10.6f} {m30:10.6f} {ratio:10.6f} {abs(ratio-phi_paasch):12.6f}{marker}")

phi_ratios = np.array(phi_ratios)
closest_idx = np.argmin(np.abs(phi_ratios - phi_paasch))
print(f"\n  Closest to phi_paasch={phi_paasch}: tau={tau_values[closest_idx]:.2f}, "
      f"ratio={phi_ratios[closest_idx]:.6f}, "
      f"deviation={abs(phi_ratios[closest_idx]-phi_paasch)*1e6:.1f} ppm")

# ============================================================
# 3. INVERTED BCS-BEC: DETAILED ANALYSIS
# ============================================================

print("\n--- 3. INVERTED BCS-BEC CROSSOVER ---")

print("""
KEY FINDING: The eigenvalue shift scaling is INVERTED from standard BCS-BEC.
  Small tau: alpha ~ 0.47 (sub-linear, BEC-like)
  Large tau: alpha ~ 2.17 (super-linear, BCS-like)

Physical interpretation:
  - At small tau, the Jensen deformation is a WEAK perturbation of the
    bi-invariant metric. The modes respond sub-linearly because they are
    in the BEC limit: tightly bound to the high-symmetry configuration.
  - At large tau, the deformation is STRONG. Modes respond super-linearly
    because the geometry has crossed into the BCS regime where the gap
    opens quadratically with the order parameter.

The crossover point where alpha(tau) = 1 is the BCS-BEC crossover.
""")

# Compute running exponent more carefully
ref_eigs = np.abs(sweep['eigenvalues_0'])
shifts = []
for ti in range(n_tau):
    eigs = np.abs(sweep[f'eigenvalues_{ti}'])
    delta = eigs - ref_eigs
    shifts.append(np.sqrt(np.mean(delta**2)))
shifts = np.array(shifts)

# Running exponent with proper derivative
valid = tau_values > 0.03
tau_v = tau_values[valid]
shift_v = shifts[valid]

# d(log shift)/d(log tau) using finite differences
log_tau = np.log(tau_v)
log_shift = np.log(shift_v + 1e-30)
alpha_running = np.gradient(log_shift, log_tau)

crossover_idx = np.argmin(np.abs(alpha_running - 1.0))
tau_crossover = tau_v[crossover_idx]
print(f"  BCS-BEC crossover: alpha=1 at tau ~ {tau_crossover:.2f}")
print(f"  Running exponent table:")
for i in range(len(tau_v)):
    marker = " <-- CROSSOVER" if i == crossover_idx else ""
    if i % 2 == 0 or i == crossover_idx:
        print(f"    tau={tau_v[i]:.2f}: alpha={alpha_running[i]:.3f}{marker}")

# Plot detailed crossover
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].plot(tau_v, alpha_running, 'ko-', markersize=4)
axes[0].axhline(1.0, color='green', linestyle='--', alpha=0.7, label='alpha=1 (crossover)')
axes[0].axhline(2.0, color='red', linestyle='--', alpha=0.7, label='alpha=2 (BCS)')
axes[0].axvline(tau_crossover, color='blue', linestyle=':', alpha=0.7, label=f'tau*={tau_crossover:.2f}')
axes[0].set_xlabel('tau')
axes[0].set_ylabel('Running exponent alpha(tau)')
axes[0].set_title('BCS-BEC Crossover: Inverted Scaling')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Per-sector crossover: check if different sectors cross at different tau
print("\n  Per-sector BCS-BEC crossover:")
sector_crossovers = {}
for s_p, s_q in [(0,0), (1,0), (1,1), (2,0), (3,0)]:
    ref_s, _ = get_sector_eigenvalues(0, s_p, s_q)
    ref_s = np.abs(ref_s)
    sector_shifts = []
    for ti in range(n_tau):
        eigs_s, _ = get_sector_eigenvalues(ti, s_p, s_q)
        delta_s = np.abs(eigs_s) - ref_s
        sector_shifts.append(np.sqrt(np.mean(delta_s**2)))
    sector_shifts = np.array(sector_shifts)

    s_valid = tau_values > 0.03
    s_tau = tau_values[s_valid]
    s_shift = sector_shifts[s_valid]

    if np.all(s_shift > 0):
        s_alpha = np.gradient(np.log(s_shift + 1e-30), np.log(s_tau))
        s_cross_idx = np.argmin(np.abs(s_alpha - 1.0))
        s_cross_tau = s_tau[s_cross_idx]
        sector_crossovers[(s_p, s_q)] = s_cross_tau
        print(f"    ({s_p},{s_q}): crossover at tau ~ {s_cross_tau:.2f}")

        axes[1].plot(s_tau, s_alpha, 'o-', markersize=3,
                     label=f'({s_p},{s_q}) tau*={s_cross_tau:.2f}')

axes[1].axhline(1.0, color='green', linestyle='--', alpha=0.7)
axes[1].set_xlabel('tau')
axes[1].set_ylabel('alpha(tau)')
axes[1].set_title('Per-Sector Crossover')
axes[1].legend(fontsize=8)
axes[1].grid(True, alpha=0.3)

# Panel 3: phi ratio evolution
axes[2].plot(tau_values, phi_ratios, 'ko-', markersize=4)
axes[2].axhline(phi_paasch, color='gold', linewidth=2, linestyle='--',
                label=f'phi_paasch={phi_paasch}')
axes[2].axhline(phi, color='red', linewidth=1, linestyle='--',
                label=f'phi={phi:.4f}')
axes[2].set_xlabel('tau')
axes[2].set_ylabel('m(3,0)/m(0,0)')
axes[2].set_title('Phi Ratio: (3,0)/(0,0) Mass Ratio')
axes[2].legend()
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'deep_crossover_analysis.png', dpi=150)
plt.close()
print("\n  Saved deep_crossover_analysis.png")

# ============================================================
# 4. BCS GAP EQUATION: QUANTITATIVE
# ============================================================

print("\n--- 4. BCS GAP EQUATION: QUANTITATIVE MAPPING ---")

print("""
The BCS gap equation on (SU(3), g_Jensen) maps to:

  1/g = Sum_n [ 1 / sqrt(xi_n^2 + Delta^2) ] * (1/N_modes)

where:
  - xi_n = lambda_n(tau) - mu (with mu=0 for particle-hole symmetric spectrum)
  - Delta = spectral gap at tau
  - g = effective coupling constant

The self-consistency condition:
  Delta(tau) is self-consistent IF g(tau) = g_physical where g_physical
  is determined by the CG vertex strengths.

We compute 1/g(tau) from the Dirac spectrum to find where the gap equation
has a non-trivial solution.
""")

# Compute BCS-like 1/g from Dirac spectrum
inv_g_values = []
for ti in range(n_tau):
    eigs = sweep[f'eigenvalues_{ti}']
    fmult = sweep[f'fermionic_mult_{ti}']

    Delta = np.min(np.abs(eigs[np.abs(eigs) > 1e-10]))

    # BCS kernel: Sum 1/sqrt(xi^2 + Delta^2) weighted by multiplicity
    abs_eigs = np.abs(eigs)
    nonzero = abs_eigs > 1e-10
    E_k = np.sqrt(abs_eigs[nonzero]**2 + Delta**2)
    kernel = np.sum(fmult[nonzero] / E_k)
    N_total = np.sum(fmult[nonzero])

    inv_g = kernel / N_total  # normalized coupling
    inv_g_values.append(inv_g)

inv_g_values = np.array(inv_g_values)
g_values = 1.0 / inv_g_values

print(f"  BCS coupling 1/g(tau):")
for ti in range(0, n_tau, 3):
    print(f"    tau={tau_values[ti]:.1f}: 1/g = {inv_g_values[ti]:.6f}, g = {g_values[ti]:.4f}")

# Derivative d(1/g)/dtau -- sign change means critical coupling crossed
d_inv_g = np.gradient(inv_g_values, tau_values)
print(f"\n  d(1/g)/dtau:")
for ti in range(0, n_tau, 3):
    print(f"    tau={tau_values[ti]:.1f}: d(1/g)/dtau = {d_inv_g[ti]:.6f}")

# The gap equation is self-consistent when 1/g(tau) = 1/g_physical
# We don't know g_physical, but we can find where 1/g has an EXTREMUM
# (which would indicate a self-consistency fixed point)
extrema = np.where(np.diff(np.sign(d_inv_g)))[0]
if len(extrema) > 0:
    print(f"\n  1/g extrema (potential self-consistency points):")
    for idx in extrema:
        print(f"    tau ~ {tau_values[idx]:.2f}: 1/g = {inv_g_values[idx]:.6f}")
else:
    print(f"\n  No extrema in 1/g(tau) -- monotonic throughout")
    print(f"  1/g ranges from {inv_g_values[0]:.6f} to {inv_g_values[-1]:.6f}")
    print(f"  This means the effective coupling INCREASES with tau")
    print(f"  (1/g decreases => g increases => stronger coupling)")
    if inv_g_values[-1] < inv_g_values[0]:
        print(f"  IMPORTANT: Coupling STRENGTHENS with tau!")
        print(f"  If g exceeds g_c = 1/N(E_F), the gap equation has")
        print(f"  a non-trivial solution EVEN without V_eff minimum.")

# Plot BCS analysis
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(tau_values, inv_g_values, 'bo-', markersize=4)
ax1.set_xlabel('tau')
ax1.set_ylabel('1/g(tau)')
ax1.set_title('BCS Coupling: 1/g from Dirac Spectrum')
ax1.grid(True, alpha=0.3)

ax2.plot(tau_values, g_values, 'ro-', markersize=4)
ax2.set_xlabel('tau')
ax2.set_ylabel('g(tau)')
ax2.set_title('Effective Coupling Strength')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'bcs_coupling.png', dpi=150)
plt.close()
print("  Saved bcs_coupling.png")

# ============================================================
# 5. BOSONIC SPECTRUM: PER-SECTOR ANALYSIS
# ============================================================

print("\n--- 5. BOSONIC SPECTRUM: SECTOR-RESOLVED ---")

# Load bosonic data at available tau values
bos_taus = {'0.0000': 0.0, '0.1500': 0.15, '0.3000': 0.30, '0.5000': 0.50}

for key, tau_val in bos_taus.items():
    bos_data = bosonic[f's_{key}']
    eigs = bos_data['eigenvalue']
    mults = bos_data['multiplicity']
    types = bos_data['type']  # 0=scalar, 1=vector, 2=TT?

    unique_types = np.unique(types)
    print(f"\n  tau={tau_val}: {len(eigs)} bosonic modes, types={unique_types}")

    for t in unique_types:
        mask = types == t
        type_name = {0: 'scalar', 1: 'vector'}.get(t, f'type_{t}')
        t_eigs = eigs[mask]
        t_mults = mults[mask]
        total_dof = np.sum(t_mults)
        E_proxy = np.sum(np.abs(t_eigs) * t_mults)
        print(f"    {type_name}: {np.sum(mask)} levels, {total_dof} DOF, "
              f"E_proxy={E_proxy:.2f}, min|lambda|={np.min(np.abs(t_eigs[t_eigs!=0])):.4f}")

# ============================================================
# 6. COMBINED BOSONIC-FERMIONIC LOW-MODE ANALYSIS
# ============================================================

print("\n--- 6. LOW-MODE F/B RATIO (CORRECT) ---")

print("Using bosonic data from kk1_bosonic_spectrum and fermionic from s19a")

# At tau=0.0, 0.15, 0.30, 0.50
for key, tau_val in bos_taus.items():
    bos_data = bosonic[f's_{key}']
    bos_eigs = np.abs(bos_data['eigenvalue'])
    bos_mults = bos_data['multiplicity']
    E_bos = np.sum(bos_eigs * bos_mults)

    # Find closest tau in fermionic sweep
    ti = np.argmin(np.abs(tau_values - tau_val))
    ferm_eigs = np.abs(sweep[f'eigenvalues_{ti}'])
    ferm_mults = sweep[f'fermionic_mult_{ti}']
    E_ferm = np.sum(ferm_eigs * ferm_mults)

    ratio = E_ferm / E_bos if E_bos > 0 else np.inf
    bos_dof = np.sum(bos_mults)
    ferm_dof = np.sum(ferm_mults)

    print(f"\n  tau={tau_val:.2f}:")
    print(f"    Bosonic:   E={E_bos:.2f}, DOF={bos_dof}")
    print(f"    Fermionic: E={E_ferm:.2f}, DOF={ferm_dof}")
    print(f"    F/B ratio: {ratio:.4f}")

    # Low-mode analysis
    # Sort both spectra by |eigenvalue| and truncate
    for N_cut in [50, 100, 200, 500]:
        # Bosonic: sort and truncate
        bos_sorted_idx = np.argsort(bos_eigs)
        bos_nonzero = bos_eigs[bos_sorted_idx] > 1e-10
        bos_low_eigs = bos_eigs[bos_sorted_idx[bos_nonzero]][:N_cut]
        bos_low_mults = bos_mults[bos_sorted_idx[bos_nonzero]][:N_cut]
        E_bos_low = np.sum(bos_low_eigs * bos_low_mults)

        # Fermionic: sort and truncate
        ferm_sorted_idx = np.argsort(ferm_eigs)
        ferm_nonzero = ferm_eigs[ferm_sorted_idx] > 1e-10
        ferm_low_eigs = ferm_eigs[ferm_sorted_idx[ferm_nonzero]][:N_cut]
        ferm_low_mults = ferm_mults[ferm_sorted_idx[ferm_nonzero]][:N_cut]
        E_ferm_low = np.sum(ferm_low_eigs * ferm_low_mults)

        ratio_low = E_ferm_low / E_bos_low if E_bos_low > 0 else np.inf
        print(f"    N<={N_cut}: F/B = {ratio_low:.4f} (E_bos={E_bos_low:.2f}, E_ferm={E_ferm_low:.2f})")


# ============================================================
# 7. SECTOR EIGENVALUE CROSSING: BOSONIC VS FERMIONIC
# ============================================================

print("\n--- 7. BOSONIC-FERMIONIC CROSSING DIAGNOSTIC ---")

# At tau=0 and tau=0.15, check if any bosonic eigenvalue matches a fermionic one
for key, tau_val in [('0.0000', 0.0), ('0.1500', 0.15)]:
    bos_data = bosonic[f's_{key}']
    bos_eigs = np.sort(np.abs(bos_data['eigenvalue']))
    bos_eigs = bos_eigs[bos_eigs > 1e-10]

    ti = np.argmin(np.abs(tau_values - tau_val))
    ferm_eigs = np.sort(np.abs(sweep[f'eigenvalues_{ti}']))
    ferm_eigs = ferm_eigs[ferm_eigs > 1e-10]

    # Find closest matches
    print(f"\n  tau={tau_val}: Closest bosonic-fermionic eigenvalue matches:")
    matches = []
    for be in bos_eigs[:50]:  # lowest 50 bosonic
        diff = np.abs(ferm_eigs - be)
        min_diff = np.min(diff)
        closest_fe = ferm_eigs[np.argmin(diff)]
        matches.append((be, closest_fe, min_diff))

    matches.sort(key=lambda x: x[2])
    print(f"  {'Bosonic':>10s} {'Fermionic':>10s} {'|diff|':>10s} {'rel diff':>10s}")
    for be, fe, diff in matches[:10]:
        rdiff = diff / ((be + fe) / 2) * 100
        marker = " *** NEAR-DEGENERATE" if rdiff < 1.0 else ""
        print(f"  {be:10.6f} {fe:10.6f} {diff:10.6f} {rdiff:9.3f}%{marker}")

print("\n" + "=" * 70)
print("A-5 DEEP ANALYSIS COMPLETE")
print("=" * 70)
