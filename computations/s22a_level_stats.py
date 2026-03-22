"""
SP-4: LOW-MODE LEVEL STATISTICS (BRODY PARAMETER q)
=====================================================

Session 22a -- Schwarzschild-Penrose-Geometer

Extracts the lowest Dirac eigenvalues ACROSS ALL SECTORS,
unfolds by cumulative spectral density, computes nearest-neighbor
spacing distribution P(s), and fits the Brody distribution.

BRODY DISTRIBUTION:
    P(s) = (q+1) * beta * s^q * exp(-beta * s^(q+1))
    where beta = [Gamma((q+2)/(q+1))]^(q+1)
    (normalized so <s> = 1 after unfolding)

    q = 0: Poisson (uncorrelated levels)
    q = 1: GOE (Wigner-Dyson, level repulsion)
    0 < q < 1: intermediate statistics

DATA SOURCE: tier0-computation/s19a_sweep_data.npz
    11424 eigenvalues per tau, 28 sectors (p,q), 21 tau values.
    Each eigenvalue has sector labels and multiplicities.

PRE-REGISTERED Constraint GateS:
    COMPELLING:  q > 0.5 at tau=0.30   (strong coupling, +5-8 pp)
    INTERESTING: q > 0.3 at tau=0.30   (confirms CP-2, +2-4 pp)
    NEUTRAL:     q < 0.1 at all tau    (pure Poisson, 0 pp)
    CLOSED:        q > 0.3 but DECREASING with tau (wrong trend, -2 pp)

Author: Schwarzschild-Penrose-Geometer (Session 22a)
Date: 2026-02-20
"""

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import gamma as gamma_fn
import os

data_dir = os.path.dirname(os.path.abspath(__file__))

# ===========================================================================
# BRODY DISTRIBUTION FUNCTIONS
# ===========================================================================

def brody_beta(q):
    """Normalization constant for Brody distribution with <s>=1."""
    return (gamma_fn((q + 2.0) / (q + 1.0))) ** (q + 1.0)

def brody_pdf(s, q):
    """Brody distribution P(s; q).
    q=0 -> Poisson: P(s) = exp(-s)
    q=1 -> GOE: P(s) = (pi/2)*s*exp(-pi*s^2/4)
    """
    beta = brody_beta(q)
    return (q + 1.0) * beta * s**q * np.exp(-beta * s**(q + 1.0))

def brody_nll(q, spacings):
    """Negative log-likelihood of Brody distribution for given spacings.
    Minimized to find best-fit q.
    """
    s = spacings
    # Exclude any zero or negative spacings
    s = s[s > 1e-12]
    if len(s) < 5:
        return 1e10
    beta = brody_beta(q)
    # log P(s) = log(q+1) + log(beta) + q*log(s) - beta*s^(q+1)
    log_p = np.log(q + 1.0) + np.log(beta) + q * np.log(s) - beta * s**(q + 1.0)
    return -np.sum(log_p)


# ===========================================================================
# SPECTRAL UNFOLDING
# ===========================================================================

def unfold_eigenvalues(eigs, poly_order=5):
    """Unfold eigenvalues using polynomial fit to the staircase function.

    The staircase N(E) = #{eigenvalues <= E} is fitted with a smooth
    polynomial N_smooth(E). Unfolded levels are xi_i = N_smooth(E_i).
    After unfolding, <s> = 1 for nearest-neighbor spacings.
    """
    n = len(eigs)
    # Staircase: N(E_i) = i+1
    staircase = np.arange(1, n + 1, dtype=float)

    # Fit polynomial to staircase
    coeffs = np.polyfit(eigs, staircase, poly_order)
    N_smooth = np.polyval(coeffs, eigs)

    # Unfolded spacings
    unfolded = N_smooth
    spacings = np.diff(unfolded)

    # Normalize so mean spacing = 1
    mean_s = np.mean(spacings)
    if mean_s > 0:
        spacings = spacings / mean_s

    return spacings, unfolded


# ===========================================================================
# MAIN COMPUTATION
# ===========================================================================

print("=" * 78)
print("  SP-4: LOW-MODE LEVEL STATISTICS (BRODY PARAMETER q)")
print("  Schwarzschild-Penrose-Geometer -- Session 22a")
print("=" * 78)

# Load data
data = np.load(os.path.join(data_dir, 's19a_sweep_data.npz'), allow_pickle=True)
tau_values = data['tau_values']

# Target tau values and N_modes
target_taus = [0.0, 0.10, 0.15, 0.20, 0.30, 0.50, 0.80, 1.00, 1.50, 2.00]
N_modes_list = [50, 100, 200]  # Test sensitivity to number of modes

print("\n  PART 1: EXTRACT DISTINCT EIGENVALUES AND COMPUTE BRODY q")
print()

# Find tau indices
tau_indices = {}
for t in target_taus:
    idx = np.argmin(np.abs(tau_values - t))
    tau_indices[t] = idx

def extract_distinct_eigenvalues(data, tau_idx, tol=1e-8):
    """Extract sorted distinct eigenvalues across all sectors."""
    eigs = data[f'eigenvalues_{tau_idx}']
    sorted_eigs = np.sort(eigs)

    # Tolerance-based deduplication
    distinct = [sorted_eigs[0]]
    for e in sorted_eigs[1:]:
        if e - distinct[-1] > tol:
            distinct.append(e)
    return np.array(distinct)


# ===========================================================================
# PART 1: BRODY q FOR LOWEST N MODES AT MULTIPLE TAU VALUES
# ===========================================================================

results = {}  # (tau, N) -> q_brody

print(f"  {'tau':>5}  {'N':>4}  {'q_Brody':>8}  {'NLL':>10}  {'<s>':>6}  {'var(s)':>8}  {'n_spacings':>10}")
print(f"  {'-----':>5}  {'----':>4}  {'-------':>8}  {'----------':>10}  {'------':>6}  {'--------':>8}  {'----------':>10}")

for t in target_taus:
    idx = tau_indices[t]
    distinct = extract_distinct_eigenvalues(data, idx)

    for N in N_modes_list:
        if N > len(distinct):
            continue

        low_eigs = distinct[:N]
        spacings, unfolded = unfold_eigenvalues(low_eigs)

        # Remove any zero spacings (shouldn't exist after dedup, but safety)
        valid_spacings = spacings[spacings > 1e-12]

        if len(valid_spacings) < 10:
            results[(t, N)] = (np.nan, np.nan)
            continue

        # Fit Brody parameter by MLE
        res = minimize_scalar(brody_nll, bounds=(0.001, 2.0), args=(valid_spacings,),
                             method='bounded')
        q_fit = res.x
        nll = res.fun

        mean_s = np.mean(valid_spacings)
        var_s = np.var(valid_spacings)

        results[(t, N)] = (q_fit, nll)

        print(f"  {t:5.2f}  {N:4d}  {q_fit:8.4f}  {nll:10.2f}  {mean_s:6.3f}  {var_s:8.4f}  {len(valid_spacings):10d}")

# ===========================================================================
# PART 2: BULK COMPARISON (ALL 791 DISTINCT LEVELS)
# ===========================================================================

print("\n  PART 2: BULK BRODY q (ALL DISTINCT LEVELS)")
print()
print(f"  {'tau':>5}  {'N_distinct':>10}  {'q_Brody':>8}  {'<s>':>6}  {'var(s)':>8}")
print(f"  {'-----':>5}  {'----------':>10}  {'-------':>8}  {'------':>6}  {'--------':>8}")

for t in [0.0, 0.30, 0.50, 1.00, 2.00]:
    idx = tau_indices[t]
    distinct = extract_distinct_eigenvalues(data, idx)
    spacings, _ = unfold_eigenvalues(distinct)
    valid = spacings[spacings > 1e-12]

    res = minimize_scalar(brody_nll, bounds=(0.001, 2.0), args=(valid,),
                         method='bounded')
    q_bulk = res.x
    mean_s = np.mean(valid)
    var_s = np.var(valid)

    print(f"  {t:5.2f}  {len(distinct):10d}  {q_bulk:8.4f}  {mean_s:6.3f}  {var_s:8.4f}")

# ===========================================================================
# PART 3: TAU-DEPENDENCE OF q (N=50 AND N=100)
# ===========================================================================

print("\n  PART 3: BRODY q AS FUNCTION OF TAU")
print()

# Compute at all 21 tau values for N=50 and N=100
q_vs_tau_50 = []
q_vs_tau_100 = []

print(f"  {'tau':>5}  {'q(N=50)':>8}  {'q(N=100)':>9}  {'q(N=200)':>9}  {'trend':>10}")
print(f"  {'-----':>5}  {'-------':>8}  {'--------':>9}  {'--------':>9}  {'----------':>10}")

for i, tau_val in enumerate(tau_values):
    distinct = extract_distinct_eigenvalues(data, i)

    q_vals = []
    for N in [50, 100, 200]:
        if N > len(distinct):
            q_vals.append(np.nan)
            continue
        low_eigs = distinct[:N]
        spacings, _ = unfold_eigenvalues(low_eigs)
        valid = spacings[spacings > 1e-12]
        if len(valid) < 10:
            q_vals.append(np.nan)
            continue
        res = minimize_scalar(brody_nll, bounds=(0.001, 2.0), args=(valid,),
                             method='bounded')
        q_vals.append(res.x)

    q_vs_tau_50.append(q_vals[0])
    q_vs_tau_100.append(q_vals[1])

    # Trend: increasing or decreasing with tau?
    if i > 0 and not np.isnan(q_vals[0]) and not np.isnan(q_vs_tau_50[-2]):
        trend = "increasing" if q_vals[0] > q_vs_tau_50[-2] else "decreasing"
    else:
        trend = "--"

    print(f"  {tau_val:5.2f}  {q_vals[0]:8.4f}  {q_vals[1]:9.4f}  {q_vals[2]:9.4f}  {trend:>10}")

q_vs_tau_50 = np.array(q_vs_tau_50)
q_vs_tau_100 = np.array(q_vs_tau_100)

# ===========================================================================
# PART 4: SPACING DISTRIBUTION HISTOGRAM AT KEY TAU VALUES
# ===========================================================================

print("\n  PART 4: SPACING DISTRIBUTION AT KEY TAU VALUES")
print()

# We will print a simple text histogram for tau=0.30 with N=50
for t_target in [0.30]:
    idx = tau_indices[t_target]
    distinct = extract_distinct_eigenvalues(data, idx)
    low_eigs = distinct[:50]
    spacings, _ = unfold_eigenvalues(low_eigs)
    valid = spacings[spacings > 1e-12]

    print(f"  Spacing distribution for tau={t_target:.2f}, N=50:")
    print(f"  Number of valid spacings: {len(valid)}")

    # Histogram bins
    bins = np.linspace(0, 4, 21)
    hist, edges = np.histogram(valid, bins=bins, density=True)

    # Also compute Poisson and GOE for comparison
    s_mid = 0.5 * (edges[:-1] + edges[1:])
    poisson = np.exp(-s_mid)
    goe = (np.pi / 2) * s_mid * np.exp(-np.pi * s_mid**2 / 4)

    q_fit = results[(t_target, 50)][0]
    brody_fit = brody_pdf(s_mid, q_fit)

    print(f"  Best-fit Brody q = {q_fit:.4f}")
    print()
    print(f"  {'s_mid':>6}  {'P(s) data':>10}  {'Poisson':>8}  {'GOE':>8}  {'Brody':>8}")
    print(f"  {'------':>6}  {'----------':>10}  {'--------':>8}  {'--------':>8}  {'--------':>8}")
    for i in range(len(hist)):
        print(f"  {s_mid[i]:6.2f}  {hist[i]:10.4f}  {poisson[i]:8.4f}  {goe[i]:8.4f}  {brody_fit[i]:8.4f}")
    print()

# ===========================================================================
# PART 5: INTRA-SECTOR VS CROSS-SECTOR COMPARISON
# ===========================================================================

print("\n  PART 5: INTRA-SECTOR VS CROSS-SECTOR STATISTICS")
print()

# At tau=0.30, compute Brody q:
# (a) Cross-sector: all sectors merged (what we did above)
# (b) Intra-sector: within each sector separately, then average

for t_target in [0.30, 1.00]:
    idx = tau_indices[t_target]
    eigs_all = data[f'eigenvalues_{idx}']
    p_all = data[f'sector_p_{idx}']
    q_all = data[f'sector_q_{idx}']

    # Cross-sector (already computed)
    distinct_cross = extract_distinct_eigenvalues(data, idx)
    sp_cross, _ = unfold_eigenvalues(distinct_cross[:100])
    valid_cross = sp_cross[sp_cross > 1e-12]
    res_cross = minimize_scalar(brody_nll, bounds=(0.001, 2.0), args=(valid_cross,),
                               method='bounded')

    # Intra-sector: for each (p,q) sector with enough eigenvalues
    sectors = set(zip(p_all.tolist(), q_all.tolist()))
    intra_q_values = []

    for (p_sec, q_sec) in sorted(sectors):
        mask = (p_all == p_sec) & (q_all == q_sec)
        sec_eigs = np.sort(eigs_all[mask])

        # Deduplicate
        distinct_sec = [sec_eigs[0]]
        for e in sec_eigs[1:]:
            if e - distinct_sec[-1] > 1e-8:
                distinct_sec.append(e)
        distinct_sec = np.array(distinct_sec)

        if len(distinct_sec) < 20:
            continue

        sp_sec, _ = unfold_eigenvalues(distinct_sec[:50])
        valid_sec = sp_sec[sp_sec > 1e-12]
        if len(valid_sec) < 10:
            continue

        res_sec = minimize_scalar(brody_nll, bounds=(0.001, 2.0), args=(valid_sec,),
                                 method='bounded')
        intra_q_values.append((p_sec, q_sec, res_sec.x, len(distinct_sec)))

    print(f"  tau = {t_target:.2f}:")
    print(f"    Cross-sector q (N=100): {res_cross.x:.4f}")
    print(f"    Intra-sector q values:")
    for (p_s, q_s, q_val, n_lev) in intra_q_values:
        print(f"      ({p_s},{q_s}): q = {q_val:.4f} ({n_lev} distinct levels)")

    if intra_q_values:
        q_intra_arr = np.array([x[2] for x in intra_q_values])
        print(f"    Intra-sector mean q = {np.mean(q_intra_arr):.4f} +/- {np.std(q_intra_arr):.4f}")
        print(f"    Cross > Intra? {res_cross.x > np.mean(q_intra_arr)}")
    print()

# ===========================================================================
# PART 6: Constraint Gate ASSESSMENT
# ===========================================================================

print("\n  PART 6: Constraint Gate ASSESSMENT")
print()

# Key diagnostic: q at tau=0.30 with N=50
q_030_50 = results.get((0.30, 50), (np.nan, np.nan))[0]
q_030_100 = results.get((0.30, 100), (np.nan, np.nan))[0]

# Is q increasing with tau for low modes?
q_trend = "INCREASING" if q_vs_tau_50[-1] > q_vs_tau_50[0] else "DECREASING"

# Assess
if q_030_50 > 0.5:
    verdict = "COMPELLING"
    detail = f"q(tau=0.30, N=50) = {q_030_50:.4f} > 0.5: strong coupling signature"
    prob_shift = "+5-8 pp"
elif q_030_50 > 0.3:
    verdict = "INTERESTING"
    detail = f"q(tau=0.30, N=50) = {q_030_50:.4f} > 0.3: confirms CP-2 prediction"
    prob_shift = "+2-4 pp"
elif q_030_50 > 0.1:
    if q_trend == "DECREASING":
        verdict = "CLOSED"
        detail = f"q(tau=0.30, N=50) = {q_030_50:.4f} > 0.1 but decreasing with tau"
        prob_shift = "-2 pp"
    else:
        verdict = "INTERESTING"
        detail = f"q(tau=0.30, N=50) = {q_030_50:.4f}: weak coupling, increasing trend"
        prob_shift = "+1-2 pp"
else:
    verdict = "NEUTRAL"
    detail = f"q(tau=0.30, N=50) = {q_030_50:.4f} < 0.1: essentially Poisson"
    prob_shift = "0 pp"

print(f"  q(tau=0.30, N=50)  = {q_030_50:.4f}")
print(f"  q(tau=0.30, N=100) = {q_030_100:.4f}")
print(f"  q trend with tau: {q_trend}")
print()
print(f"  *** VERDICT: {verdict} ***")
print(f"  Detail: {detail}")
print(f"  Probability shift: {prob_shift}")
print()

# ===========================================================================
# PART 7: SAVE DATA
# ===========================================================================

np.savez(os.path.join(data_dir, 's22a_level_stats.npz'),
         tau_target=np.array(target_taus),
         tau_all=tau_values,
         q_vs_tau_N50=q_vs_tau_50,
         q_vs_tau_N100=q_vs_tau_100,
         verdict=np.array([verdict]),
         prob_shift=np.array([prob_shift]),
)

# ===========================================================================
# PART 8: PLOT
# ===========================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Brody q vs tau for different N
ax1 = axes[0, 0]
ax1.plot(tau_values, q_vs_tau_50, 'bo-', label='N=50 lowest', markersize=4)
ax1.plot(tau_values, q_vs_tau_100, 'rs-', label='N=100 lowest', markersize=4)
ax1.axhline(y=0.3, color='green', linestyle='--', alpha=0.7, label='CP-2 threshold (q=0.3)')
ax1.axhline(y=0.0, color='gray', linestyle=':', alpha=0.5, label='Poisson (q=0)')
ax1.axhline(y=1.0, color='orange', linestyle=':', alpha=0.5, label='GOE (q=1)')
ax1.set_xlabel('tau')
ax1.set_ylabel('Brody parameter q')
ax1.set_title('Brody q vs tau (low modes)')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel 2: Spacing distribution at tau=0.30
ax2 = axes[0, 1]
idx_030 = tau_indices[0.30]
distinct_030 = extract_distinct_eigenvalues(data, idx_030)
sp_030, _ = unfold_eigenvalues(distinct_030[:50])
valid_030 = sp_030[sp_030 > 1e-12]
ax2.hist(valid_030, bins=20, density=True, alpha=0.6, color='blue', label='Data (N=50)')
s_plot = np.linspace(0.01, 4, 200)
ax2.plot(s_plot, np.exp(-s_plot), 'k--', label='Poisson (q=0)')
ax2.plot(s_plot, (np.pi/2)*s_plot*np.exp(-np.pi*s_plot**2/4), 'r--', label='GOE (q=1)')
q_best = results[(0.30, 50)][0]
ax2.plot(s_plot, brody_pdf(s_plot, q_best), 'g-', linewidth=2,
         label=f'Brody (q={q_best:.3f})')
ax2.set_xlabel('Normalized spacing s')
ax2.set_ylabel('P(s)')
ax2.set_title(f'Spacing distribution tau=0.30, N=50')
ax2.legend(fontsize=8)
ax2.set_xlim(0, 4)
ax2.grid(True, alpha=0.3)

# Panel 3: Spacing distribution at tau=1.00
ax3 = axes[1, 0]
idx_100 = tau_indices[1.00]
distinct_100 = extract_distinct_eigenvalues(data, idx_100)
sp_100, _ = unfold_eigenvalues(distinct_100[:50])
valid_100 = sp_100[sp_100 > 1e-12]
ax3.hist(valid_100, bins=20, density=True, alpha=0.6, color='blue', label='Data (N=50)')
ax3.plot(s_plot, np.exp(-s_plot), 'k--', label='Poisson (q=0)')
ax3.plot(s_plot, (np.pi/2)*s_plot*np.exp(-np.pi*s_plot**2/4), 'r--', label='GOE (q=1)')
q_best_100 = results.get((1.00, 50), (np.nan,))[0]
if not np.isnan(q_best_100):
    ax3.plot(s_plot, brody_pdf(s_plot, q_best_100), 'g-', linewidth=2,
             label=f'Brody (q={q_best_100:.3f})')
ax3.set_xlabel('Normalized spacing s')
ax3.set_ylabel('P(s)')
ax3.set_title(f'Spacing distribution tau=1.00, N=50')
ax3.legend(fontsize=8)
ax3.set_xlim(0, 4)
ax3.grid(True, alpha=0.3)

# Panel 4: N-dependence of q at tau=0.30
ax4 = axes[1, 1]
N_scan = [20, 30, 40, 50, 75, 100, 150, 200, 300, 400, 500]
q_vs_N = []
for N in N_scan:
    if N > len(distinct_030):
        break
    low = distinct_030[:N]
    sp, _ = unfold_eigenvalues(low)
    v = sp[sp > 1e-12]
    if len(v) < 10:
        q_vs_N.append(np.nan)
        continue
    res = minimize_scalar(brody_nll, bounds=(0.001, 2.0), args=(v,), method='bounded')
    q_vs_N.append(res.x)
ax4.plot(N_scan[:len(q_vs_N)], q_vs_N, 'ko-', markersize=5)
ax4.axhline(y=0.3, color='green', linestyle='--', alpha=0.7, label='CP-2 threshold')
ax4.set_xlabel('Number of low modes N')
ax4.set_ylabel('Brody parameter q')
ax4.set_title('N-dependence of q at tau=0.30')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

plt.suptitle('SP-4: Low-Mode Level Statistics (Brody Parameter)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's22a_level_stats.png'), dpi=150, bbox_inches='tight')
print(f"  Plot saved: tier0-computation/s22a_level_stats.png")

# ===========================================================================
# SUMMARY
# ===========================================================================

print("\n" + "=" * 78)
print("  SP-4 SUMMARY: LOW-MODE LEVEL STATISTICS")
print("=" * 78)
print()
print(f"  q(tau=0.30, N=50)  = {q_030_50:.4f}")
print(f"  q(tau=0.30, N=100) = {q_030_100:.4f}")
print(f"  q(tau=0.00, N=50)  = {q_vs_tau_50[0]:.4f}")
print(f"  q(tau=2.00, N=50)  = {q_vs_tau_50[-1]:.4f}")
print()
print(f"  Low-mode q range: [{np.nanmin(q_vs_tau_50):.4f}, {np.nanmax(q_vs_tau_50):.4f}]")
print(f"  q trend: {q_trend}")
print()
print(f"  *** VERDICT: {verdict} ***")
print(f"  {detail}")
print(f"  Probability shift: {prob_shift}")
print()
print("=" * 78)
