"""
S44 F-FOAM-2: Non-Monotone Cutoff from Foam Decoherence
=========================================================

Tests whether quantum foam decoherence at the Planck scale creates a
non-monotone effective cutoff function f_eff, producing a local minimum
in the spectral action that stabilizes tau at the fold.

Physics:
  S37 monotonicity theorem: spectral action with ANY monotone f gives
  monotone S(tau). PROVED no minimum for monotone f (CUTOFF-SA-37 closure).

  But foam decoherence damps high-lying eigenvalues preferentially:
    S_foam(tau) = sum_k d_k f(lambda_k^2/Lambda^2) exp(-gamma |lambda_k|^alpha)

  For alpha > 2 the effective cutoff f_eff = f * foam_damping might be
  non-monotone, potentially evading the S37 theorem.

  S43 DISSOLUTION-43: epsilon_crossover ~ 0.014. gamma must be < epsilon_crossover
  for the spectral triple to remain emergent.

Data notes:
  S36 spectral action uses f(lambda^2) = |lambda| (= sqrt(lambda^2)), i.e.
  S_{(p,q)}(tau) = sum_k |lambda_k|. S_full = sum_{(p,q)} dim(p,q)^2 S_{(p,q)}.
  Eigenvalues stored at tau = {0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22}.
  We test foam modification with BOTH the S36 cutoff and Gaussian cutoff.

Gate: F-FOAM-2
  PASS: minimum at gamma < 0.014
  FAIL: no minimum in physical range
  INFO: minimum but gamma > 0.014

Author: quantum-foam-theorist (Session 44)
Date: 2026-03-14
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ===========================================================================
# LOAD DATA
# ===========================================================================

base = Path(__file__).parent
s36 = np.load(base / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
s43_gge = np.load(base / 's43_foam_gge.npz', allow_pickle=True)

# Dissolution threshold from S43
epsilon_crossover = 0.014

# SU(3) representation dimension
def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Tau values with stored eigenvalues and their sector structure
tau_with_evals = [0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22]
sector_labels = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]

# Peter-Weyl multiplicity = dim(p,q)^2
mult = {(p,q): dim_su3(p,q)**2 for (p,q) in sector_labels}

# ===========================================================================
# COLLECT EIGENVALUES AT EACH TAU, BY SECTOR
# ===========================================================================

eigenvalues_by_tau_sector = {}
for tau in tau_with_evals:
    for (p, q) in sector_labels:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key in s36:
            eigenvalues_by_tau_sector[(tau, p, q)] = s36[key]

print("=== Eigenvalue data loaded ===")
for tau in tau_with_evals:
    total = sum(len(eigenvalues_by_tau_sector[(tau, p, q)]) for (p,q) in sector_labels)
    print(f"  tau={tau:.3f}: {total} eigenvalues across {len(sector_labels)} sectors")

# ===========================================================================
# VERIFY CONSISTENCY WITH S36 STORED VALUES
# ===========================================================================

print("\n=== Consistency check: S36 base cutoff f(lambda^2) = |lambda| ===")
tau_combined = s36['tau_combined']
S_full_stored = s36['S_full']

for tau in tau_with_evals:
    S_recomp = 0.0
    for (p, q) in sector_labels:
        ev = eigenvalues_by_tau_sector[(tau, p, q)]
        S_sector = np.sum(np.abs(ev))
        S_recomp += mult[(p,q)] * S_sector

    # Find stored value at this tau
    idx = np.argmin(np.abs(tau_combined - tau))
    S_stored = S_full_stored[idx]
    ratio = S_recomp / S_stored
    print(f"  tau={tau:.3f}: S_recomp={S_recomp:.2f}, S_stored={S_stored:.2f}, "
          f"ratio={ratio:.6f}")

# ===========================================================================
# FOAM-MODIFIED SPECTRAL ACTION FUNCTIONS
# ===========================================================================

def S_foam_linear(tau, gamma, alpha):
    """
    Foam-modified spectral action using S36 base cutoff f = |lambda|.

    S_foam = sum_{(p,q)} dim(p,q)^2 * sum_k |lambda_k| * exp(-gamma * |lambda_k|^alpha)
    """
    S = 0.0
    for (p, q) in sector_labels:
        ev = eigenvalues_by_tau_sector[(tau, p, q)]
        lam_abs = np.abs(ev)
        S_sector = np.sum(lam_abs * np.exp(-gamma * lam_abs**alpha))
        S += mult[(p,q)] * S_sector
    return S


def S_foam_gaussian(tau, gamma, alpha, Lambda_sq=1.0):
    """
    Foam-modified spectral action using Gaussian cutoff f = exp(-lambda^2/Lambda^2).

    S_foam = sum_{(p,q)} dim(p,q)^2 * sum_k exp(-lambda_k^2/Lambda^2) * exp(-gamma |lambda_k|^alpha)
    """
    S = 0.0
    for (p, q) in sector_labels:
        ev = eigenvalues_by_tau_sector[(tau, p, q)]
        lam_abs = np.abs(ev)
        log_w = -ev**2 / Lambda_sq - gamma * lam_abs**alpha
        S += mult[(p,q)] * np.sum(np.exp(log_w))
    return S


# ===========================================================================
# ANALYTICAL MONOTONICITY ANALYSIS
# ===========================================================================

print("\n" + "="*70)
print("ANALYTICAL MONOTONICITY ANALYSIS")
print("="*70)

print("""
The S37 monotonicity theorem requires f(x) monotone decreasing in x = lambda^2.

Case 1: S36 base cutoff f(x) = sqrt(x)  [i.e., f(lambda^2) = |lambda|]
  f_eff(x) = sqrt(x) * exp(-gamma * x^{alpha/2})
  df_eff/dx = exp(-gamma*x^{alpha/2}) * [1/(2*sqrt(x)) - gamma*(alpha/2)*x^{alpha/2-1}*sqrt(x)]
            = exp(-gamma*x^{alpha/2}) * [1/(2*sqrt(x)) - gamma*(alpha/2)*x^{(alpha-1)/2}]

  This changes sign at x_* where:
    1/(2*sqrt(x_*)) = gamma*(alpha/2)*x_*^{(alpha-1)/2}
    => x_*^{alpha/2} = 1/(gamma*alpha)
    => x_* = (gamma*alpha)^{-2/alpha}

  For alpha=2: x_* = 1/(2*gamma)      |lambda|_* = 1/sqrt(2*gamma)
  For alpha=3: x_* = (3*gamma)^{-2/3} |lambda|_* = (3*gamma)^{-1/3}
  For alpha=4: x_* = (4*gamma)^{-1/2} |lambda|_* = (4*gamma)^{-1/4}

  f_eff INCREASES for x < x_*, DECREASES for x > x_*.
  This is a GENUINE non-monotone cutoff! The S37 theorem does NOT apply!

Case 2: Gaussian cutoff f(x) = exp(-x)
  f_eff(x) = exp(-x) * exp(-gamma * x^{alpha/2}) = exp(-x - gamma*x^{alpha/2})
  df_eff/dx = f_eff * [-1 - gamma*(alpha/2)*x^{alpha/2-1}]
  For alpha >= 2: coefficient is always < -1 < 0
  => f_eff is ALWAYS monotone decreasing. S37 theorem APPLIES.
  => No minimum possible with Gaussian + foam.

CRITICAL DISTINCTION:
  The S36 spectral action uses f = sqrt(x) = |lambda|, which is INCREASING.
  Multiplying by foam damping creates a peaked function. The S37 theorem
  was stated for monotone DECREASING f. With f = sqrt(x), the product
  f * foam_damping has a maximum at x_*, making it non-monotone.
  This is the ONLY route to a potential minimum in S_foam(tau).
""")

# ===========================================================================
# PARAMETER SCAN: LINEAR CUTOFF (S36 convention)
# ===========================================================================

N_gamma = 300
gamma_values = np.logspace(-6, 0, N_gamma)
alpha_values = [2, 3, 4]

print("=== Computing foam-modified spectral action (linear cutoff) ===")
print(f"  gamma range: [{gamma_values[0]:.2e}, {gamma_values[-1]:.2e}], N={N_gamma}")
print(f"  alpha values: {alpha_values}")
print(f"  tau points: {tau_with_evals}")

# S_foam_array[i_alpha, i_gamma, i_tau]
S_foam_lin = np.zeros((len(alpha_values), N_gamma, len(tau_with_evals)))

for i_alpha, alpha in enumerate(alpha_values):
    for i_gamma, gamma in enumerate(gamma_values):
        for i_tau, tau in enumerate(tau_with_evals):
            S_foam_lin[i_alpha, i_gamma, i_tau] = S_foam_linear(tau, gamma, alpha)

# Also compute Gaussian cutoff for comparison
S_foam_gaus = np.zeros((len(alpha_values), N_gamma, len(tau_with_evals)))
for i_alpha, alpha in enumerate(alpha_values):
    for i_gamma, gamma in enumerate(gamma_values):
        for i_tau, tau in enumerate(tau_with_evals):
            S_foam_gaus[i_alpha, i_gamma, i_tau] = S_foam_gaussian(tau, gamma, alpha)

print("  Done.")

# ===========================================================================
# SEARCH FOR LOCAL MINIMA
# ===========================================================================

print("\n=== Searching for local minima in S_foam(tau) ===")

def search_minima(S_array, label):
    """Search for local minima in S(tau) across (alpha, gamma) parameter space."""
    results = {
        'has_minimum': np.zeros((len(alpha_values), N_gamma), dtype=bool),
        'min_tau_idx': np.full((len(alpha_values), N_gamma), -1, dtype=int),
        'min_tau': np.full((len(alpha_values), N_gamma), np.nan),
        'barrier_left': np.full((len(alpha_values), N_gamma), np.nan),
        'barrier_right': np.full((len(alpha_values), N_gamma), np.nan),
        'relative_depth': np.full((len(alpha_values), N_gamma), np.nan),
    }

    print(f"\n  --- {label} ---")
    for i_alpha, alpha in enumerate(alpha_values):
        n_min = 0
        best_depth = 0
        best_gamma = None
        best_tau = None

        for i_gamma, gamma in enumerate(gamma_values):
            S_tau = S_array[i_alpha, i_gamma, :]

            # Check for local minimum at interior points
            for i_tau in range(1, len(tau_with_evals) - 1):
                if S_tau[i_tau] < S_tau[i_tau - 1] and S_tau[i_tau] < S_tau[i_tau + 1]:
                    results['has_minimum'][i_alpha, i_gamma] = True
                    results['min_tau_idx'][i_alpha, i_gamma] = i_tau
                    results['min_tau'][i_alpha, i_gamma] = tau_with_evals[i_tau]

                    bl = S_tau[i_tau - 1] - S_tau[i_tau]
                    br = S_tau[i_tau + 1] - S_tau[i_tau]
                    results['barrier_left'][i_alpha, i_gamma] = bl
                    results['barrier_right'][i_alpha, i_gamma] = br

                    rd = min(bl, br) / S_tau[i_tau] if S_tau[i_tau] > 0 else 0
                    results['relative_depth'][i_alpha, i_gamma] = rd
                    n_min += 1

                    if rd > best_depth:
                        best_depth = rd
                        best_gamma = gamma
                        best_tau = tau_with_evals[i_tau]
                    break

        print(f"    alpha={alpha}: {n_min}/{N_gamma} parameter points have minima")
        if best_gamma is not None:
            print(f"      Best: tau={best_tau}, gamma={best_gamma:.4e}, "
                  f"rel_depth={best_depth:.4e}, gamma/eps_c={best_gamma/epsilon_crossover:.2f}")

            # Print S profile at best gamma
            i_best = np.argmin(np.abs(gamma_values - best_gamma))
            S_profile = S_array[i_alpha, i_best, :]
            for j, t in enumerate(tau_with_evals):
                marker = " <-- MIN" if t == best_tau else ""
                print(f"        tau={t:.3f}: S={S_profile[j]:.6f}{marker}")
        else:
            print(f"      No minima found in entire gamma range")

    return results

results_lin = search_minima(S_foam_lin, "Linear cutoff f=|lambda|")
results_gaus = search_minima(S_foam_gaus, "Gaussian cutoff f=exp(-lambda^2)")

# ===========================================================================
# FOCUSED ANALYSIS: Where do minima appear relative to epsilon_crossover?
# ===========================================================================

print("\n=== Minimum location vs dissolution threshold ===")

for cutoff_name, res in [("Linear", results_lin), ("Gaussian", results_gaus)]:
    print(f"\n  {cutoff_name} cutoff:")
    for i_alpha, alpha in enumerate(alpha_values):
        mask_min = res['has_minimum'][i_alpha]
        if not np.any(mask_min):
            print(f"    alpha={alpha}: No minima at any gamma")
            continue

        gamma_with_min = gamma_values[mask_min]
        gamma_min_val = gamma_with_min[0]
        gamma_max_val = gamma_with_min[-1]

        n_phys = np.sum(gamma_with_min < epsilon_crossover)
        n_diss = np.sum(gamma_with_min >= epsilon_crossover)

        print(f"    alpha={alpha}: minima at gamma in [{gamma_min_val:.2e}, {gamma_max_val:.2e}]")
        print(f"      Physical (gamma < {epsilon_crossover}): {n_phys}")
        print(f"      Dissolving (gamma >= {epsilon_crossover}): {n_diss}")

        if n_phys > 0:
            # Details of best physical minimum
            phys_mask = mask_min & (gamma_values < epsilon_crossover)
            depths = res['relative_depth'][i_alpha, phys_mask]
            best_idx = np.where(phys_mask)[0][np.argmax(depths)]
            print(f"      Best physical minimum: gamma={gamma_values[best_idx]:.4e}, "
                  f"tau={res['min_tau'][i_alpha, best_idx]:.3f}, "
                  f"rel_depth={res['relative_depth'][i_alpha, best_idx]:.4e}")

# ===========================================================================
# PEAK POSITION ANALYSIS
# ===========================================================================

print("\n=== Peak position of f_eff(|lambda|) for linear cutoff ===")
print("  f_eff(|lambda|) = |lambda| * exp(-gamma * |lambda|^alpha)")
print("  Peak at |lambda|_* = (gamma*alpha)^{-1/alpha}")
print("  Eigenvalue range: |lambda| in [0.82, 2.11]")
print()

for alpha in alpha_values:
    print(f"  alpha={alpha}:")
    for gamma in [1e-4, 1e-3, 0.005, 0.01, 0.014, 0.02, 0.05, 0.1, 0.5, 1.0]:
        lam_peak = (gamma * alpha) ** (-1.0 / alpha)
        in_range = 0.82 <= lam_peak <= 2.11
        eps_ratio = gamma / epsilon_crossover
        print(f"    gamma={gamma:.3e} ({eps_ratio:.2f}x eps_c): "
              f"|lambda|_* = {lam_peak:.3f} {'<-- IN RANGE' if in_range else ''}")

# ===========================================================================
# PHYSICAL INTERPRETATION
# ===========================================================================

print("\n" + "="*70)
print("PHYSICAL INTERPRETATION")
print("="*70)

print("""
For the S36 linear cutoff f(lambda^2) = |lambda|:
  The effective cutoff f_eff(|lambda|) = |lambda| * exp(-gamma * |lambda|^alpha)
  has a peak at |lambda|_* = (gamma*alpha)^{-1/alpha}.

  The Dirac eigenvalues span |lambda| in [0.82, 2.11] for tau in [0.05, 0.22].

  For the peak to fall within the eigenvalue range:
    alpha=2: gamma in [0.12, 0.74]  -- requires gamma >> epsilon_crossover = 0.014
    alpha=3: gamma in [0.027, 0.32] -- requires gamma > epsilon_crossover
    alpha=4: gamma in [0.011, 0.22] -- minimum at gamma ~ 0.011 BARELY in range

  Key question: does the peak at |lambda|_* create a TAU-minimum in S_foam?

  Even with a non-monotone f_eff, a minimum in S_foam(tau) requires the
  SPECTRAL DENSITY to shift through the peak of f_eff in a specific way.
  As tau increases, eigenvalues grow monotonically (Jensen deformation).
  This means eigenvalue density sweeps THROUGH the peak from left to right.

  S_foam(tau) increases when most eigenvalues are to the left of |lambda|_*
  (ascending side of f_eff), and decreases when they pass through and fall
  on the descending side. A minimum would occur when the "center of mass"
  of eigenvalue density crosses |lambda|_*.
""")

# ===========================================================================
# GATE VERDICT
# ===========================================================================

# Check linear cutoff (the physically relevant one matching S36)
any_min_lin = np.any(results_lin['has_minimum'])
any_min_gaus = np.any(results_gaus['has_minimum'])

if any_min_lin:
    phys_min_lin = False
    best_phys_depth = 0
    best_phys_gamma = None
    best_phys_alpha = None
    best_phys_tau = None

    for i_alpha, alpha in enumerate(alpha_values):
        mask = results_lin['has_minimum'][i_alpha] & (gamma_values < epsilon_crossover)
        if np.any(mask):
            phys_min_lin = True
            depths = results_lin['relative_depth'][i_alpha, mask]
            idx = np.where(mask)[0][np.argmax(depths)]
            if results_lin['relative_depth'][i_alpha, idx] > best_phys_depth:
                best_phys_depth = results_lin['relative_depth'][i_alpha, idx]
                best_phys_gamma = gamma_values[idx]
                best_phys_alpha = alpha
                best_phys_tau = results_lin['min_tau'][i_alpha, idx]

    if phys_min_lin:
        verdict = "PASS"
        reason = (f"Minimum found at alpha={best_phys_alpha}, gamma={best_phys_gamma:.4e} "
                  f"(< eps_crossover={epsilon_crossover}), tau={best_phys_tau:.3f}, "
                  f"relative depth={best_phys_depth:.4e}")
    else:
        # Check if any minima exist at all (just above threshold)
        best_depth_any = 0
        best_gamma_any = None
        best_alpha_any = None
        best_tau_any = None
        for i_alpha, alpha in enumerate(alpha_values):
            mask = results_lin['has_minimum'][i_alpha]
            if np.any(mask):
                depths = results_lin['relative_depth'][i_alpha, mask]
                idx = np.where(mask)[0][np.argmax(depths)]
                if results_lin['relative_depth'][i_alpha, idx] > best_depth_any:
                    best_depth_any = results_lin['relative_depth'][i_alpha, idx]
                    best_gamma_any = gamma_values[idx]
                    best_alpha_any = alpha
                    best_tau_any = results_lin['min_tau'][i_alpha, idx]

        verdict = "INFO"
        reason = (f"Minimum found but only at gamma > eps_crossover. "
                  f"Best: alpha={best_alpha_any}, gamma={best_gamma_any:.4e} "
                  f"({best_gamma_any/epsilon_crossover:.1f}x eps_crossover), "
                  f"tau={best_tau_any:.3f}, rel_depth={best_depth_any:.4e}. "
                  f"Spectral triple dissolves before foam is strong enough.")
else:
    verdict = "FAIL"
    reason = ("No minimum found for any (gamma, alpha) with linear cutoff. "
              "Despite f_eff being non-monotone, eigenvalue density evolution "
              "does not produce a turning point in S_foam(tau).")

# Additional context for Gaussian cutoff
if not any_min_gaus:
    reason += (" Gaussian cutoff: STRUCTURAL monotonicity (f_eff always decreasing). "
               "No minimum possible. S37 theorem applies directly.")

print(f"\n{'='*70}")
print(f"GATE VERDICT: F-FOAM-2 = {verdict}")
print(f"{'='*70}")
print(f"Reason: {reason}")

# ===========================================================================
# DETAILED PROFILE AT KEY GAMMA VALUES
# ===========================================================================

print("\n=== Detailed S_foam profiles at key gamma values (linear cutoff) ===")

key_gammas = {
    '1e-4 (well below eps_c)': 1e-4,
    '1e-3': 1e-3,
    '5e-3': 5e-3,
    '0.010 (below eps_c)': 0.010,
    '0.014 (= eps_c)': 0.014,
    '0.020 (above eps_c)': 0.020,
    '0.050': 0.050,
    '0.100': 0.100,
    '0.500': 0.500,
}

for alpha in alpha_values:
    i_alpha = alpha_values.index(alpha)
    print(f"\n  alpha={alpha}:")
    print(f"  {'gamma':>25s}  ", end='')
    for t in tau_with_evals:
        print(f"{'tau='+str(t):>12s}", end='')
    print(f"  {'monotone?':>10s}")

    for label, gamma in key_gammas.items():
        i_gamma = np.argmin(np.abs(gamma_values - gamma))
        S_profile = S_foam_lin[i_alpha, i_gamma, :]
        diffs = np.diff(S_profile)
        mono = "YES" if np.all(diffs > 0) else ("NO" if np.all(diffs < 0) else "MIXED")

        print(f"  {label:>25s}  ", end='')
        for s in S_profile:
            print(f"{s:12.2f}", end='')
        print(f"  {mono:>10s}")

# ===========================================================================
# SAVE DATA
# ===========================================================================

np.savez(base / 's44_foam_cutoff.npz',
    # Parameters
    tau_with_evals=np.array(tau_with_evals),
    gamma_values=gamma_values,
    alpha_values=np.array(alpha_values),
    epsilon_crossover=epsilon_crossover,
    # Spectral action arrays
    S_foam_linear=S_foam_lin,
    S_foam_gaussian=S_foam_gaus,
    # Minimum search: linear cutoff
    has_minimum_lin=results_lin['has_minimum'],
    min_tau_lin=results_lin['min_tau'],
    barrier_left_lin=results_lin['barrier_left'],
    barrier_right_lin=results_lin['barrier_right'],
    relative_depth_lin=results_lin['relative_depth'],
    # Minimum search: Gaussian cutoff
    has_minimum_gaus=results_gaus['has_minimum'],
    # Gate
    gate_name=np.array(['F-FOAM-2']),
    gate_verdict=np.array([verdict]),
    gate_reason=np.array([reason]),
)

print(f"\nData saved to {base / 's44_foam_cutoff.npz'}")

# ===========================================================================
# PLOTTING
# ===========================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle(f'F-FOAM-2: Non-Monotone Cutoff from Foam Decoherence\n'
             f'Gate Verdict: {verdict}', fontsize=14, fontweight='bold')

# --- Panel (a): f_eff(|lambda|) showing non-monotonicity ---
ax = axes[0, 0]
lam = np.linspace(0.01, 4.0, 500)
for alpha in alpha_values:
    for gamma in [0.01, 0.05, 0.2]:
        f_eff = lam * np.exp(-gamma * lam**alpha)
        label = rf'$\alpha={alpha}, \gamma={gamma}$'
        ax.plot(lam, f_eff, label=label)

# Mark eigenvalue range
ax.axvspan(0.82, 2.11, alpha=0.15, color='gray', label='eigenvalue range')
ax.set_xlabel(r'$|\lambda|$', fontsize=12)
ax.set_ylabel(r'$f_{\mathrm{eff}}(|\lambda|) = |\lambda| e^{-\gamma |\lambda|^\alpha}$',
              fontsize=12)
ax.set_title(r'(a) Effective cutoff (linear base)', fontsize=12)
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)

# --- Panel (b): S_foam(tau) for alpha=4 at several gamma values ---
ax = axes[0, 1]
alpha_plot = 4
i_alpha_plot = alpha_values.index(alpha_plot)
gamma_plot = [0, 1e-3, 0.01, 0.014, 0.05, 0.1, 0.5]
colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(gamma_plot)))

for i, gp in enumerate(gamma_plot):
    if gp == 0:
        i_gp = 0
    else:
        i_gp = np.argmin(np.abs(gamma_values - gp))
    S_plot = S_foam_lin[i_alpha_plot, i_gp, :]
    S_norm = S_plot / S_plot[0]
    label = rf'$\gamma={gp:.0e}$' if gp > 0 else r'$\gamma=0$'
    ax.plot(tau_with_evals, S_norm, 'o-', color=colors[i], label=label,
            markersize=4, linewidth=1.5)

ax.axvline(x=0.19, color='red', linestyle='--', alpha=0.5, label=r'fold $\tau=0.19$')
ax.axhline(y=1.0, color='gray', linestyle=':', alpha=0.3)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$S_{\mathrm{foam}}(\tau) / S_{\mathrm{foam}}(0.05)$', fontsize=12)
ax.set_title(rf'(b) Normalized $S_{{\mathrm{{foam}}}}(\tau)$, $\alpha={alpha_plot}$',
             fontsize=12)
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)

# --- Panel (c): Minimum depth vs gamma for each alpha ---
ax = axes[1, 0]
for i_alpha, alpha in enumerate(alpha_values):
    # For each gamma that has a minimum, plot relative depth
    mask = results_lin['has_minimum'][i_alpha]
    if np.any(mask):
        ax.semilogx(gamma_values[mask], results_lin['relative_depth'][i_alpha, mask],
                     'o-', label=rf'$\alpha={alpha}$', markersize=3)

ax.axvline(x=epsilon_crossover, color='red', linestyle='--', linewidth=2,
           label=rf'$\epsilon_{{\mathrm{{crossover}}}}={epsilon_crossover}$')
ax.set_xlabel(r'$\gamma$ (foam strength)', fontsize=12)
ax.set_ylabel('Relative depth of minimum', fontsize=12)
ax.set_title('(c) Minimum depth vs foam strength (linear cutoff)', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

if not np.any(results_lin['has_minimum']):
    ax.text(0.5, 0.5, 'No minima found', transform=ax.transAxes,
            ha='center', va='center', fontsize=16, color='red')

# --- Panel (d): Summary ---
ax = axes[1, 1]
ax.axis('off')

# Build summary based on verdict
if verdict == "FAIL":
    summary_lines = [
        r"$\mathbf{F\text{-}FOAM\text{-}2:\ FAIL}$",
        "",
        r"$\mathbf{Linear\ cutoff}$ $f = |\lambda|$:",
        r"$f_{\mathrm{eff}} = |\lambda| e^{-\gamma|\lambda|^\alpha}$ is non-monotone",
        r"but eigenvalue density sweeps monotonically",
        r"through peak $\Rightarrow$ no minimum in $S_{\mathrm{foam}}(\tau)$.",
        "",
        r"$\mathbf{Gaussian\ cutoff}$ $f = e^{-\lambda^2}$:",
        r"$f_{\mathrm{eff}} = e^{-\lambda^2 - \gamma|\lambda|^\alpha}$",
        r"is monotone decreasing $\Rightarrow$ S37 applies directly.",
        "",
        r"$\mathbf{Structural:}$ Foam decoherence is purely suppressive.",
        r"Cannot create spectral bump to break monotonicity.",
    ]
elif verdict == "INFO":
    summary_lines = [
        r"$\mathbf{F\text{-}FOAM\text{-}2:\ INFO}$",
        "",
        r"Minimum found in $S_{\mathrm{foam}}(\tau)$ with linear cutoff",
        rf"at $\gamma = {best_gamma_any:.3e}$ "
        rf"({best_gamma_any/epsilon_crossover:.1f}$\times$ $\epsilon_{{\mathrm{{crossover}}}}$)",
        "",
        r"Spectral triple dissolves BEFORE foam is strong enough.",
        rf"Required: $\gamma > {epsilon_crossover}$",
        r"Dissolution: $\epsilon_{\mathrm{crossover}} = 0.014$",
        "",
        r"$\mathbf{Gaussian\ cutoff:}$ No minimum at any $\gamma$ (structural).",
    ]
else:  # PASS
    summary_lines = [
        r"$\mathbf{F\text{-}FOAM\text{-}2:\ PASS}$",
        "",
        rf"Minimum at $\alpha={best_phys_alpha}$, "
        rf"$\gamma={best_phys_gamma:.3e}$",
        rf"$\tau = {best_phys_tau:.3f}$, depth = {best_phys_depth:.3e}",
        rf"$\gamma/\epsilon_{{\mathrm{{crossover}}}} = "
        rf"{best_phys_gamma/epsilon_crossover:.2f}$",
    ]

summary_text = "\n".join(summary_lines)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=11, verticalalignment='top', fontfamily='serif',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(base / 's44_foam_cutoff.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to {base / 's44_foam_cutoff.png'}")

print("\n=== COMPUTATION COMPLETE ===")
