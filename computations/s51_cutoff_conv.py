#!/usr/bin/env python3
"""
S51 CUTOFF-CONV-51: Cutoff function convergence test for chi_SA sector weights

Tests whether the SA correlator sector weights W_{(p,q)} are stable across
4 cutoff functions and across Lambda from 1 to 10 M_KK.

Gate: CUTOFF-CONV-51
  PASS: relative weight variation < 10% across all 4 cutoffs for sectors with > 5% weight
  FAIL: variation > 50% for any major sector
  INFO: 10% < variation < 50%

The SA correlator is:
  chi_SA(K) = sum_{sectors s} W_s / (K^2 + C_2(s))

where the sector weight is:
  W_s = sum_{n in s} dim2_n * |f'(omega_n^2 / Lambda^2)| * (d omega_n / d tau)^2

The key question: do the FRACTIONAL weights W_s / W_total depend on f?
"""
import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import *

# =====================================================================
# LOAD SPECTRUM DATA
# =====================================================================
d = np.load('s44_dos_tau.npz', allow_pickle=True)

omega_15 = d['tau0.15_all_omega']
omega_19 = d['tau0.19_all_omega']
dim2_19 = d['tau0.19_all_dim2']

# Eigenvalue derivative (finite difference, dtau = 0.04)
domega_dtau = (omega_19 - omega_15) / 0.04

N_eig = len(omega_19)
print(f"Spectrum: {N_eig} eigenvalues at tau=0.19 (fold)")
print(f"omega range: [{omega_19.min():.6f}, {omega_19.max():.6f}]")
print(f"|domega/dtau| range: [{np.abs(domega_dtau).min():.6f}, {np.abs(domega_dtau).max():.6f}]")

# =====================================================================
# SECTOR IDENTIFICATION
# =====================================================================
# dim2 values present: 1, 9, 36, 64, 100, 225
# Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3
#
# dim2=1:   (0,0)         -> C_2 = 0.000
# dim2=9:   (1,0)+(0,1)   -> C_2 = 1.333
# dim2=36:  (2,0)+(0,2)   -> C_2 = 3.333
# dim2=64:  (1,1)         -> C_2 = 3.000
# dim2=100: (3,0)+(0,3)   -> C_2 = 6.000
# dim2=225: (2,1)+(1,2) + (4,0)+(0,4) -> C_2 = 5.333 and 9.333 MIXED
#
# NOTE: dim2=225 contains TWO distinct C_2 values that cannot be separated
# from dim2 alone. For the convergence test, we group by dim2 (observable
# from data). The C_2 assignment affects pole positions, not weight stability.

sector_labels = {
    1:   '(0,0)',
    9:   '(1,0)+(0,1)',
    36:  '(2,0)+(0,2)',
    64:  '(1,1)',
    100: '(3,0)+(0,3)',
    225: '(2,1)+(1,2)+(4,0)+(0,4)',
}

sector_C2 = {
    1:   0.000,
    9:   4.0/3,
    36:  10.0/3,
    64:  3.000,
    100: 6.000,
    225: None,  # Mixed — use effective C2 from weighted average
}

unique_dim2 = sorted(np.unique(dim2_19.astype(int)))
print(f"\nSectors present: {unique_dim2}")
for d2 in unique_dim2:
    n = np.sum(dim2_19 == d2)
    print(f"  dim2={d2:4d}: {n:4d} levels, label={sector_labels.get(d2, '?')}")

# =====================================================================
# CUTOFF FUNCTIONS
# =====================================================================
# For the spectral action S = Tr f(D^2/Lambda^2),
# the second variation gives weights involving f'(x) where x = omega^2/Lambda^2.
#
# We compute |f'(x)| for each cutoff. The sign of f' is always negative
# (f is decreasing), so |f'| = -f'.
#
# (a) Gaussian:       f(x) = exp(-x),          |f'(x)| = exp(-x)
# (b) Sharp:          f(x) = theta(1-x),       |f'(x)| = delta(x-1)
#     -> regularized as narrow Gaussian: (1/eps*sqrt(2pi)) exp(-(x-1)^2/(2*eps^2))
# (c) Polynomial:     f(x) = (1-x)^4 theta(1-x), |f'(x)| = 4(1-x)^3 theta(1-x)
# (d) Smooth compact: f(x) = exp(-1/(1-x)) theta(1-x) / f(0)
#     where f(0) = exp(-1), so f(x) = exp(1 - 1/(1-x)) theta(1-x)
#     |f'(x)| = exp(1 - 1/(1-x)) / (1-x)^2 * theta(1-x)

def cutoff_gaussian(x):
    """f(x) = exp(-x). |f'(x)| = exp(-x)."""
    return np.exp(-x)

def cutoff_sharp(x, eps=0.02):
    """f(x) = theta(1-x), regularized. |f'(x)| ~ narrow Gaussian at x=1."""
    return np.exp(-(x - 1.0)**2 / (2 * eps**2)) / (eps * np.sqrt(2 * np.pi))

def cutoff_polynomial(x):
    """f(x) = (1-x)^4 theta(1-x). |f'(x)| = 4(1-x)^3 theta(1-x)."""
    mask = (x < 1.0)
    result = np.zeros_like(x)
    result[mask] = 4.0 * (1.0 - x[mask])**3
    return result

def cutoff_smooth_compact(x):
    """f(x) = exp(1 - 1/(1-x)) theta(1-x). |f'(x)| = f(x)/(1-x)^2."""
    mask = (x < 1.0) & (x >= 0)
    result = np.zeros_like(x)
    one_minus_x = 1.0 - x[mask]
    result[mask] = np.exp(1.0 - 1.0 / one_minus_x) / one_minus_x**2
    return result

cutoff_names = ['Gaussian', 'Sharp', 'Polynomial', 'Smooth compact']
cutoff_funcs = [cutoff_gaussian, cutoff_sharp, cutoff_polynomial, cutoff_smooth_compact]

# =====================================================================
# PART 1: SECTOR WEIGHTS FOR 4 CUTOFFS AT Lambda = 3.0
# =====================================================================
print("\n" + "=" * 70)
print("PART 1: SECTOR WEIGHTS ACROSS 4 CUTOFF FUNCTIONS (Lambda=3.0)")
print("=" * 70)

Lambda_ref = 3.0
x_vals = omega_19**2 / Lambda_ref**2
print(f"\nLambda = {Lambda_ref:.1f} M_KK")
print(f"x = omega^2/Lambda^2 range: [{x_vals.min():.4f}, {x_vals.max():.4f}]")
print(f"Fraction of eigenvalues with x < 1: {np.mean(x_vals < 1):.3f}")

# Storage for sector fractional weights: [cutoff_idx, sector_idx]
all_frac_weights = {}  # cutoff_name -> {dim2: frac_weight}
all_total_weights = {}

for ci, (cname, cfunc) in enumerate(zip(cutoff_names, cutoff_funcs)):
    fp = cfunc(x_vals)  # |f'(x)| at each eigenvalue

    # Weight per eigenvalue: dim2 * |f'(x)| * (domega/dtau)^2
    w = dim2_19 * fp * domega_dtau**2
    w_total = w.sum()

    sector_w = {}
    for d2 in unique_dim2:
        mask = (dim2_19 == d2)
        sector_w[d2] = w[mask].sum()

    # Fractional weights
    frac_w = {d2: sector_w[d2] / w_total if w_total > 0 else 0.0 for d2 in unique_dim2}

    all_frac_weights[cname] = frac_w
    all_total_weights[cname] = w_total

    print(f"\n{cname} cutoff:")
    print(f"  Total weight: {w_total:.4f}")
    for d2 in unique_dim2:
        print(f"    dim2={d2:4d} ({sector_labels.get(d2, '?'):>30s}): "
              f"W={sector_w[d2]:.4f}, frac={frac_w[d2]*100:.2f}%")

# =====================================================================
# PART 2: RELATIVE VARIATION ACROSS CUTOFFS
# =====================================================================
print("\n" + "=" * 70)
print("PART 2: RELATIVE VARIATION OF SECTOR WEIGHTS ACROSS CUTOFFS")
print("=" * 70)

# For each sector, compute: max(frac) - min(frac) / mean(frac)
print(f"\n{'dim2':>6s} {'label':>35s} | ", end='')
for cn in cutoff_names:
    print(f" {cn[:8]:>8s}", end='')
print(f" | {'mean':>6s} {'var%':>6s} {'gate':>6s}")
print("-" * 120)

gate_results = {}
for d2 in unique_dim2:
    fracs = [all_frac_weights[cn][d2] for cn in cutoff_names]
    f_mean = np.mean(fracs)
    f_max = np.max(fracs)
    f_min = np.min(fracs)

    if f_mean > 0:
        rel_var = (f_max - f_min) / f_mean * 100  # percent
    else:
        rel_var = 0.0

    # Gate applies only to sectors with > 5% mean weight
    is_major = (f_mean > 0.05)
    if is_major:
        if rel_var < 10:
            gate_status = "PASS"
        elif rel_var < 50:
            gate_status = "INFO"
        else:
            gate_status = "FAIL"
    else:
        gate_status = "minor"

    gate_results[d2] = {'rel_var': rel_var, 'mean': f_mean, 'gate': gate_status, 'is_major': is_major}

    label = sector_labels.get(d2, '?')
    print(f"{d2:6d} {label:>35s} | ", end='')
    for cn in cutoff_names:
        print(f" {all_frac_weights[cn][d2]*100:8.2f}", end='')
    print(f" | {f_mean*100:6.2f} {rel_var:6.1f} {gate_status:>6s}")

# =====================================================================
# PART 3: chi_SA(K) AND EFFECTIVE ALPHA FOR EACH CUTOFF
# =====================================================================
print("\n" + "=" * 70)
print("PART 3: chi_SA(K) AND EFFECTIVE alpha_eff FOR EACH CUTOFF")
print("=" * 70)

# Since dim2=225 mixes two C_2 values, we need to handle it.
# Option: split dim2=225 into two effective sub-sectors based on eigenvalue ranges.
# At tau=0.19: (2,1)+(1,2) eigenvalues should be lower-lying (C_2=5.33)
# and (4,0)+(0,4) should be higher (C_2=9.33).
# The eigenvalues in a sector scale approximately as sqrt(C_2 + corrections).
# Without exact (p,q) labels per eigenvalue, we cannot split them cleanly.
#
# For the chi_SA computation, we assign an effective C_2 for dim2=225.
# The S50 code (via rep_catalog iteration order) likely assigned C_2=5.333 or 9.333.
# We test BOTH assignments and also the weighted mean.

# For dim2 != 225, assign C_2 directly
C2_assign = {
    1:   0.000,
    9:   4.0/3,
    36:  10.0/3,
    64:  3.000,
    100: 6.000,
}

# For dim2=225, we try splitting: eigenvalues below median -> C2=5.333, above -> C2=9.333
omega_225 = omega_19[dim2_19 == 225]
median_225 = np.median(omega_225)
print(f"\ndim2=225: {len(omega_225)} eigenvalues, median omega = {median_225:.6f}")
print(f"  Range: [{omega_225.min():.6f}, {omega_225.max():.6f}]")

# Use effective C_2 for dim2=225: weight-averaged from constituent reps
# Both (2,1)+(1,2) and (4,0)+(0,4) have dim=15 each.
# Number of levels: 240 eigenvalues for dim2=225. If split evenly: 120 from each pair.
# Assign C_2 = weight-averaged: (5.333*120 + 9.333*120)/240 = 7.333
# But this is a rough approximation. For the convergence test, the exact C_2 assignment
# for dim2=225 does not matter -- we test WEIGHT STABILITY, not pole positions.

# For chi_SA, use the S50 convention (assign all dim2=225 to one effective C_2)
# and also compute with split assignment

K_values = np.logspace(-2, 1, 200)
K_pivot = 2.0
idx_pivot = np.argmin(np.abs(K_values - K_pivot))

print(f"\nK_pivot = {K_pivot}")

for ci, (cname, cfunc) in enumerate(zip(cutoff_names, cutoff_funcs)):
    fp = cfunc(x_vals)
    w = dim2_19 * fp * domega_dtau**2

    # Build chi_SA(K) using dim2 groups
    chi_SA = np.zeros_like(K_values)
    for d2 in unique_dim2:
        mask = (dim2_19 == d2)
        w_sector = w[mask].sum()

        if d2 == 225:
            # Split: half weight at C2=5.333, half at C2=9.333
            # (This is approximate but tests the pole-spread structure)
            C2_low = 16.0 / 3  # (2,1)+(1,2)
            C2_high = 28.0 / 3  # (4,0)+(0,4)
            chi_SA += 0.5 * w_sector / (K_values**2 + C2_low)
            chi_SA += 0.5 * w_sector / (K_values**2 + C2_high)
        elif d2 in C2_assign:
            C2 = C2_assign[d2]
            if C2 == 0:
                C2 = 1e-6  # Regularize singlet
            chi_SA += w_sector / (K_values**2 + C2)

    # Normalize
    chi_SA_norm = chi_SA / chi_SA[0]

    # Effective power law: P(K) ~ K^{-alpha}
    # n_s = 1 + d ln(chi_SA) / d ln(K) at K_pivot
    ln_K = np.log(K_values)
    ln_chi = np.log(np.maximum(chi_SA, 1e-30))
    slope = np.gradient(ln_chi, ln_K)
    n_s_SA = 1 + slope
    alpha_eff = -slope[idx_pivot]
    n_s_at_pivot = n_s_SA[idx_pivot]

    # Running: alpha_s = d(n_s)/d(ln K)
    alpha_s = np.gradient(n_s_SA, ln_K)
    alpha_s_at_pivot = alpha_s[idx_pivot]

    # Identity deviation: alpha_s - (n_s^2 - 1)
    identity_dev = alpha_s_at_pivot - (n_s_at_pivot**2 - 1)

    print(f"\n{cname}:")
    print(f"  chi_SA(K_pivot) / chi_SA(0) = {chi_SA_norm[idx_pivot]:.6f}")
    print(f"  alpha_eff at K_pivot = {alpha_eff:.4f}")
    print(f"  n_s at K_pivot = {n_s_at_pivot:.4f}")
    print(f"  alpha_s at K_pivot = {alpha_s_at_pivot:.6f}")
    print(f"  Identity deviation = {identity_dev:.6f}")

# =====================================================================
# PART 4: LAMBDA SCAN (GAUSSIAN CUTOFF)
# =====================================================================
print("\n" + "=" * 70)
print("PART 4: LAMBDA DEPENDENCE (GAUSSIAN CUTOFF, Lambda = 1 to 10)")
print("=" * 70)

Lambda_scan = np.linspace(1.0, 10.0, 50)
omega_max = omega_19.max()

# Track fractional weights vs Lambda
scan_frac = {d2: np.zeros(len(Lambda_scan)) for d2 in unique_dim2}
scan_alpha = np.zeros(len(Lambda_scan))
scan_identity_dev = np.zeros(len(Lambda_scan))

for li, Lam in enumerate(Lambda_scan):
    x = omega_19**2 / Lam**2
    fp = cutoff_gaussian(x)
    w = dim2_19 * fp * domega_dtau**2
    w_total = w.sum()

    if w_total == 0:
        continue

    for d2 in unique_dim2:
        mask = (dim2_19 == d2)
        scan_frac[d2][li] = w[mask].sum() / w_total

    # chi_SA at this Lambda
    chi_SA = np.zeros_like(K_values)
    for d2 in unique_dim2:
        mask = (dim2_19 == d2)
        w_sector = w[mask].sum()
        if d2 == 225:
            chi_SA += 0.5 * w_sector / (K_values**2 + 16.0/3)
            chi_SA += 0.5 * w_sector / (K_values**2 + 28.0/3)
        elif d2 in C2_assign:
            C2 = C2_assign[d2]
            if C2 == 0:
                C2 = 1e-6
            chi_SA += w_sector / (K_values**2 + C2)

    ln_chi = np.log(np.maximum(chi_SA, 1e-30))
    slope = np.gradient(ln_chi, ln_K)
    n_s_SA = 1 + slope
    alpha_s = np.gradient(n_s_SA, ln_K)

    scan_alpha[li] = -slope[idx_pivot]
    scan_identity_dev[li] = alpha_s[idx_pivot] - (n_s_SA[idx_pivot]**2 - 1)

print(f"\n{'Lambda':>8s} | ", end='')
for d2 in unique_dim2:
    print(f"  d2={d2:<4d}", end='')
print(f" | {'alpha':>7s} {'id_dev':>8s}")
print("-" * 100)

for li in [0, 4, 9, 14, 19, 24, 29, 34, 39, 44, 49]:
    if li < len(Lambda_scan):
        Lam = Lambda_scan[li]
        print(f"{Lam:8.2f} | ", end='')
        for d2 in unique_dim2:
            print(f"  {scan_frac[d2][li]*100:6.2f}", end='')
        print(f" | {scan_alpha[li]:7.4f} {scan_identity_dev[li]:8.5f}")

# Lambda variation for major sectors
print(f"\nLambda variation analysis (Gaussian cutoff):")
print(f"{'dim2':>6s} {'label':>35s} | {'min%':>6s} {'max%':>6s} {'var%':>6s}")
print("-" * 80)
for d2 in unique_dim2:
    fracs = scan_frac[d2]
    f_mean = fracs.mean()
    f_max = fracs.max()
    f_min = fracs.min()
    rel_var = (f_max - f_min) / max(f_mean, 1e-10) * 100
    label = sector_labels.get(d2, '?')
    print(f"{d2:6d} {label:>35s} | {f_min*100:6.2f} {f_max*100:6.2f} {rel_var:6.1f}")

# =====================================================================
# PART 5: CONVERGENCE AT HIGH Lambda (Lambda >> omega_max)
# =====================================================================
print("\n" + "=" * 70)
print("PART 5: HIGH-LAMBDA CONVERGENCE (S45 Taylor exactness regime)")
print("=" * 70)

print(f"\nomega_max = {omega_max:.6f}")
print(f"For Lambda >> omega_max, all x = omega^2/Lambda^2 << 1")
print(f"In this regime, f(x) -> f(0) + f'(0)*x + ... ")
print(f"The leading term of |f'(x)| is |f'(0)| for all smooth f.")
print(f"So all cutoffs should converge to the SAME relative weights.")

# At Lambda = 10 (>> omega_max = 2.06):
Lam_high = 10.0
x_high = omega_19**2 / Lam_high**2
print(f"\nAt Lambda = {Lam_high}: x_max = {x_high.max():.4f}")

# For Gaussian: |f'(x)| = exp(-x) ≈ 1 - x + x^2/2 - ...
# For Polynomial: |f'(x)| = 4(1-x)^3 ≈ 4(1 - 3x + 3x^2 - x^3) for x < 1
# At large Lambda (small x), Gaussian -> 1, Poly -> 4, Smooth compact -> exp(1-1) = 1
# The CONSTANT prefactor cancels in fractional weights.
# The x-dependent correction is O(x) ~ O(omega^2/Lambda^2).

convergence_fracs = {}
for cn, cf in zip(cutoff_names, cutoff_funcs):
    fp = cf(x_high)
    w = dim2_19 * fp * domega_dtau**2
    wt = w.sum()
    fracs = {}
    for d2 in unique_dim2:
        mask = (dim2_19 == d2)
        fracs[d2] = w[mask].sum() / wt if wt > 0 else 0
    convergence_fracs[cn] = fracs

print(f"\nSector fractions at Lambda={Lam_high}:")
print(f"{'dim2':>6s} | ", end='')
for cn in cutoff_names:
    print(f" {cn[:8]:>8s}", end='')
print(f" | {'spread':>7s}")
print("-" * 80)
for d2 in unique_dim2:
    vals = [convergence_fracs[cn][d2] for cn in cutoff_names]
    spread = max(vals) - min(vals)
    print(f"{d2:6d} | ", end='')
    for v in vals:
        print(f" {v*100:8.3f}", end='')
    print(f" | {spread*100:7.4f}")

# =====================================================================
# PART 6: THE DEEP-x REGIME (Lambda ~ omega_max)
# =====================================================================
print("\n" + "=" * 70)
print("PART 6: WORST-CASE DIVERGENCE (Lambda near spectral radius)")
print("=" * 70)

# At Lambda ≈ omega_max, x values range from ~0.16 to ~1.0.
# This is where cutoff functions differ most.
Lam_low = omega_max * 1.05  # Just above spectral radius
x_low = omega_19**2 / Lam_low**2
print(f"\nLambda = {Lam_low:.4f} (1.05 * omega_max)")
print(f"x range: [{x_low.min():.4f}, {x_low.max():.4f}]")

worstcase_fracs = {}
for cn, cf in zip(cutoff_names, cutoff_funcs):
    fp = cf(x_low)
    w = dim2_19 * fp * domega_dtau**2
    wt = w.sum()
    fracs = {}
    for d2 in unique_dim2:
        mask = (dim2_19 == d2)
        fracs[d2] = w[mask].sum() / wt if wt > 0 else 0
    worstcase_fracs[cn] = fracs

print(f"\nSector fractions at Lambda={Lam_low:.3f} (near spectral radius):")
print(f"{'dim2':>6s} | ", end='')
for cn in cutoff_names:
    print(f" {cn[:8]:>8s}", end='')
print(f" | {'spread':>7s} {'rel_var%':>8s}")
print("-" * 90)
for d2 in unique_dim2:
    vals = [worstcase_fracs[cn][d2] for cn in cutoff_names]
    vmean = np.mean(vals)
    spread = max(vals) - min(vals)
    rv = spread / max(vmean, 1e-10) * 100
    print(f"{d2:6d} | ", end='')
    for v in vals:
        print(f" {v*100:8.3f}", end='')
    print(f" | {spread*100:7.4f} {rv:8.1f}")

# =====================================================================
# GATE VERDICT
# =====================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: CUTOFF-CONV-51")
print("=" * 70)

# The gate is evaluated at Lambda = 3.0 (the S50 reference value)
print(f"\nEvaluation at Lambda = {Lambda_ref} M_KK:")
print(f"\n{'dim2':>6s} {'label':>35s} | {'mean%':>7s} {'rel_var%':>8s} | {'verdict':>7s}")
print("-" * 85)

any_fail = False
any_info = False
for d2 in unique_dim2:
    gr = gate_results[d2]
    label = sector_labels.get(d2, '?')
    marker = "*" if gr['is_major'] else " "
    print(f"{d2:6d} {label:>35s} |{marker}{gr['mean']*100:6.2f} {gr['rel_var']:8.1f} | {gr['gate']:>7s}")
    if gr['gate'] == 'FAIL':
        any_fail = True
    if gr['gate'] == 'INFO':
        any_info = True

# Overall verdict
print(f"\nOverall gate:")
if any_fail:
    overall = "FAIL"
    print(f"  CUTOFF-CONV-51: **FAIL** — variation > 50% in at least one major sector")
elif any_info:
    overall = "INFO"
    print(f"  CUTOFF-CONV-51: **INFO** — variation 10-50% in at least one major sector")
else:
    overall = "PASS"
    print(f"  CUTOFF-CONV-51: **PASS** — all major sectors have < 10% variation across cutoffs")

# Physical interpretation
print(f"""
PHYSICAL INTERPRETATION:
  The sector fractional weights depend on how |f'(x)| distributes weight
  across eigenvalue levels. For Lambda >> omega_max, all smooth cutoffs
  converge (|f'(x)| -> |f'(0)| = constant). At Lambda = 3.0, the Gaussian
  cutoff has x_max = {(omega_max/Lambda_ref)**2:.3f}, meaning most eigenvalues
  are in the regime x < 0.5 where cutoff functions still differ.

  The sharp cutoff concentrates ALL weight at x=1 (eigenvalues near Lambda),
  while the Gaussian spreads weight across all eigenvalues. This structural
  difference in the weighting CANNOT be resolved by increasing Lambda alone --
  it reflects the fundamental ambiguity of the NCG spectral action: the
  Lagrangian (from Seeley-DeWitt) is cutoff-universal, but functionals
  involving f' (like chi_SA) are not.
""")

# =====================================================================
# SAVE RESULTS
# =====================================================================
np.savez('s51_cutoff_conv.npz',
    # Spectrum data
    omega_19=omega_19,
    dim2_19=dim2_19,
    domega_dtau=domega_dtau,
    unique_dim2=np.array(unique_dim2),
    # Cutoff comparison at Lambda=3
    cutoff_names=np.array(cutoff_names),
    Lambda_ref=Lambda_ref,
    frac_gaussian=np.array([all_frac_weights['Gaussian'][d2] for d2 in unique_dim2]),
    frac_sharp=np.array([all_frac_weights['Sharp'][d2] for d2 in unique_dim2]),
    frac_polynomial=np.array([all_frac_weights['Polynomial'][d2] for d2 in unique_dim2]),
    frac_smooth=np.array([all_frac_weights['Smooth compact'][d2] for d2 in unique_dim2]),
    # Lambda scan (Gaussian)
    Lambda_scan=Lambda_scan,
    scan_frac_d2_1=scan_frac[1],
    scan_frac_d2_9=scan_frac[9],
    scan_frac_d2_36=scan_frac[36],
    scan_frac_d2_64=scan_frac[64],
    scan_frac_d2_100=scan_frac[100],
    scan_frac_d2_225=scan_frac[225],
    scan_alpha=scan_alpha,
    scan_identity_dev=scan_identity_dev,
    # Gate results
    gate_verdict=overall,
    gate_rel_var=np.array([gate_results[d2]['rel_var'] for d2 in unique_dim2]),
    gate_mean_frac=np.array([gate_results[d2]['mean'] for d2 in unique_dim2]),
)

print(f"\nData saved to s51_cutoff_conv.npz")
print("DONE.")
