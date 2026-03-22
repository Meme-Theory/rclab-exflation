"""
s36_species_scale.py — Species Scale Computation for W6 Resolution
=====================================================================

Computes Lambda_species(tau) from the KK spectrum of D_K on Jensen-deformed SU(3).

The species scale (Swampland Distance Conjecture, van de Heisteeg et al. 2022):
    Lambda_species = M_P / N_species^{1/(d-2)}

where N_species counts the number of KK modes below the cutoff.

For d=4 (4D EFT):   Lambda_species = M_P / N_species^{1/2}
For d=8 (synthesis): Lambda_species = M_P / N_species^{1/6}

The W6 wall is the ratio Lambda_SA / M_KK ~ 10^6 at tau ~ 0.2.
The gate asks whether Lambda_species / M_KK classifies this as THIN, THICK, or HARMLESS.

Data source: s23a_eigenvectors_extended.npz (Dirac eigenvalues at p+q <= 6)
Extended with analytic Peter-Weyl sector structure to p+q <= L_max.

Key spectral fact: In sector (p,q), the Dirac operator on SU(3) with bi-invariant
metric has Casimir eigenvalues. For the Jensen-deformed metric, each sector (p,q)
produces 16*dim(p,q) eigenvalues in the reduced block, where
    dim(p,q) = (p+1)(q+1)(p+q+2)/2
Each eigenvalue has physical multiplicity dim(p,q) from the Peter-Weyl right-regular
representation.

Author: Spectral-Geometer
Gate: W6-SPECIES-36
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ===========================================================================
# Physical scales (GeV)
# ===========================================================================
from canonical_constants import M_Pl_reduced as M_P  # 2.435e18 GeV
M_KK = 1.0e16        # KK scale (GeV), from framework calibration
Lambda_SA = 1.02e22  # Spectral action cutoff (GeV), from Session 31

# ===========================================================================
# Load eigenvalue data
# ===========================================================================
data_path = 'tier0-computation/s23a_eigenvectors_extended.npz'
d = np.load(data_path, allow_pickle=True)
tau_values = d['tau_values']
n_tau = len(tau_values)
print(f"Tau values: {tau_values}")
print(f"Number of tau points: {n_tau}")

# ===========================================================================
# Extract distinct eigenvalues and their multiplicities per sector
# ===========================================================================
def get_spectrum_with_multiplicities(d, tau_idx):
    """
    Return arrays of (|eigenvalue|, physical_multiplicity) for a given tau.

    The stored eigenvalues are in the reduced Peter-Weyl block.
    Each eigenvalue in sector (p,q) has physical multiplicity = dim(p,q).
    The 'multiplicities' array already stores dim(p,q) for each eigenvalue.
    """
    evals = d[f'eigenvalues_{tau_idx}']
    mults = d[f'multiplicities_{tau_idx}']
    return np.abs(evals), mults

def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p+1) * (q+1) * (p+q+2) // 2

# ===========================================================================
# Species counting function
# ===========================================================================
def count_species(abs_evals, mults, lambda_cut):
    """
    Count N_species = sum of multiplicities for modes with |lambda| < lambda_cut.

    Here lambda_cut is in dimensionless units (eigenvalue units).
    Physical mass: m_n = |lambda_n| * M_KK.
    So lambda_cut = Lambda / M_KK in dimensionless units.
    """
    mask = abs_evals < lambda_cut
    return int(np.sum(mults[mask]))

# ===========================================================================
# Extend spectrum beyond L_max=6 using Weyl law extrapolation
# ===========================================================================
def weyl_extrapolation_count(lambda_cut, d_manifold=8, spinor_rank=16):
    """
    Weyl's law for the Dirac operator on an 8-dimensional compact manifold:
        N(Lambda) ~ (spinor_rank * Vol(M) / (4*pi)^{d/2} * Gamma(d/2+1)) * Lambda^d

    For SU(3) with bi-invariant metric, Vol(SU(3)) = sqrt(3)*pi^4/4 (in unit Killing normalization).
    But we calibrate this from the actual computed spectrum at L_max=6.

    Returns the Weyl-extrapolated count.
    """
    # This is used only as a cross-check. The main computation uses the actual spectrum.
    pass

# ===========================================================================
# Main computation
# ===========================================================================
print("\n" + "="*80)
print("SPECIES SCALE COMPUTATION — W6 RESOLUTION")
print("="*80)

# Physical cutoff ratios to scan
Lambda_ratios = [1.0, 10.0, 100.0, 1000.0]  # Lambda / M_KK

# Storage
results = {}

for tau_idx in range(n_tau):
    tau = tau_values[tau_idx]
    abs_evals, mults = get_spectrum_with_multiplicities(d, tau_idx)

    lambda_max = np.max(abs_evals)
    lambda_min = np.min(abs_evals)
    N_total = int(np.sum(mults))

    print(f"\n--- tau = {tau:.2f} ---")
    print(f"  Eigenvalue range: [{lambda_min:.6f}, {lambda_max:.6f}]")
    print(f"  Total modes (with multiplicity, L_max=6): {N_total}")

    species_counts = {}
    for ratio in Lambda_ratios:
        N_sp = count_species(abs_evals, mults, ratio)
        species_counts[ratio] = N_sp
        print(f"  N_species(Lambda={ratio:.0f}*M_KK) = {N_sp}")

    results[tau] = {
        'lambda_min': lambda_min,
        'lambda_max': lambda_max,
        'N_total': N_total,
        'species_counts': species_counts,
        'abs_evals': abs_evals,
        'mults': mults
    }

# ===========================================================================
# Weyl law calibration and extrapolation to higher L_max
# ===========================================================================
print("\n" + "="*80)
print("WEYL LAW CALIBRATION")
print("="*80)

# At tau=0 (bi-invariant), we know the exact eigenvalue structure.
# Weyl's law: N(Lambda) ~ C * Lambda^d for d=8.
# Calibrate C from the L_max=6 data.

tau_idx_0 = 0  # tau = 0
abs_evals_0, mults_0 = get_spectrum_with_multiplicities(d, tau_idx_0)
lambda_max_0 = np.max(abs_evals_0)

# Count N at several thresholds to check Weyl scaling
thresholds = np.array([0.9, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0])
thresholds = thresholds[thresholds <= lambda_max_0 + 0.01]

print(f"\nWeyl law check at tau=0 (lambda_max={lambda_max_0:.4f}):")
print(f"  If N ~ C*Lambda^d, then log(N)/log(Lambda) should approach d=8")
for th in thresholds:
    N = count_species(abs_evals_0, mults_0, th)
    if N > 0 and th > 1.0:
        effective_d = np.log(N) / np.log(th)
        print(f"  Lambda={th:.2f}: N={N:8d}, effective_dim = log(N)/log(Lambda) = {effective_d:.2f}")
    else:
        print(f"  Lambda={th:.2f}: N={N:8d}")

# Fit Weyl coefficient from the highest available data point
N_at_max = count_species(abs_evals_0, mults_0, lambda_max_0)
C_weyl = N_at_max / lambda_max_0**8
print(f"\nWeyl coefficient C = N_max / lambda_max^8 = {N_at_max} / {lambda_max_0:.4f}^8 = {C_weyl:.2f}")

# Extrapolate to higher Lambda (beyond L_max=6)
print("\nWeyl-extrapolated N_species (beyond L_max=6 data):")
for Lambda_over_MKK in [1, 10, 100, 1000, 1e4, 1e5, 1e6]:
    N_weyl = C_weyl * Lambda_over_MKK**8
    Lambda_sp_d4 = M_P / np.sqrt(N_weyl)
    Lambda_sp_d8 = M_P / N_weyl**(1/6)
    print(f"  Lambda/M_KK = {Lambda_over_MKK:.0e}: N_weyl = {N_weyl:.3e}, "
          f"Lambda_sp(d=4)/M_KK = {Lambda_sp_d4/M_KK:.3e}, "
          f"Lambda_sp(d=8)/M_KK = {Lambda_sp_d8/M_KK:.3e}")

# ===========================================================================
# Self-consistent species scale
# ===========================================================================
print("\n" + "="*80)
print("SELF-CONSISTENT SPECIES SCALE")
print("="*80)

def self_consistent_species_scale(C_weyl, d_eff, M_P, M_KK):
    """
    Solve Lambda_species = M_P / N(Lambda_species)^{1/(d_eff-2)} self-consistently.

    N(Lambda) = C_weyl * (Lambda/M_KK)^8  (Weyl law for 8D internal manifold)

    Lambda_sp = M_P / (C_weyl * (Lambda_sp/M_KK)^8)^{1/(d_eff-2)}

    Let x = Lambda_sp / M_KK. Then:
        x * M_KK = M_P / (C_weyl * x^8)^{1/(d_eff-2)}
        x * M_KK = M_P * C_weyl^{-1/(d_eff-2)} * x^{-8/(d_eff-2)}
        x^{1 + 8/(d_eff-2)} = M_P / (M_KK * C_weyl^{1/(d_eff-2)})
        x = (M_P / (M_KK * C_weyl^{1/(d_eff-2)}))^{(d_eff-2)/(d_eff-2+8)}

    For d_eff=4: exponent = 2/(2+8) = 1/5
    For d_eff=8: exponent = 6/(6+8) = 3/7
    """
    alpha = 1.0 / (d_eff - 2)  # power in species formula
    exponent = (d_eff - 2) / (d_eff - 2 + 8)

    base = M_P / (M_KK * C_weyl**alpha)
    x = base**exponent

    Lambda_sp = x * M_KK
    N_sp = C_weyl * x**8

    # Verify self-consistency
    Lambda_sp_check = M_P / N_sp**alpha

    return Lambda_sp, N_sp, x

# Compute self-consistent species scale at each tau
print("\nSelf-consistent species scale (Weyl extrapolation):")
print(f"{'tau':>6s} {'C_weyl':>12s} {'Lambda_sp(d=4)/M_KK':>22s} {'Lambda_sp(d=8)/M_KK':>22s} {'N_sp(d=4)':>14s} {'N_sp(d=8)':>14s}")

sc_results_d4 = []
sc_results_d8 = []
C_weyl_arr = []

for tau_idx in range(n_tau):
    tau = tau_values[tau_idx]
    abs_evals, mults = get_spectrum_with_multiplicities(d, tau_idx)
    lambda_max = np.max(abs_evals)
    N_at_max = int(np.sum(mults))

    # Weyl coefficient at this tau
    C_w = N_at_max / lambda_max**8
    C_weyl_arr.append(C_w)

    Lambda_sp_4, N_sp_4, x_4 = self_consistent_species_scale(C_w, 4, M_P, M_KK)
    Lambda_sp_8, N_sp_8, x_8 = self_consistent_species_scale(C_w, 8, M_P, M_KK)

    sc_results_d4.append((tau, Lambda_sp_4, N_sp_4, x_4))
    sc_results_d8.append((tau, Lambda_sp_8, N_sp_8, x_8))

    print(f"{tau:6.3f} {C_w:12.2f} {x_4:22.6e} {x_8:22.6e} {N_sp_4:14.3e} {N_sp_8:14.3e}")

# ===========================================================================
# Convergence check: L_max dependence
# ===========================================================================
print("\n" + "="*80)
print("CONVERGENCE CHECK: L_max DEPENDENCE")
print("="*80)

# For the actual data at L_max=6, compute the Weyl coefficient using
# different L_max cutoffs (using only sectors with p+q <= L)
for tau_idx in [0, 2, 3]:  # tau = 0, 0.15, 0.2
    tau = tau_values[tau_idx]
    print(f"\ntau = {tau:.2f}:")

    abs_evals, mults = get_spectrum_with_multiplicities(d, tau_idx)
    sector_p = d[f'sector_p_{tau_idx}']
    sector_q = d[f'sector_q_{tau_idx}']

    for L_cut in [2, 3, 4, 5, 6]:
        mask_L = (sector_p + sector_q) <= L_cut
        evals_cut = abs_evals[mask_L]
        mults_cut = mults[mask_L]

        if len(evals_cut) == 0:
            continue

        lmax_cut = np.max(evals_cut)
        N_cut = int(np.sum(mults_cut))
        C_cut = N_cut / lmax_cut**8 if lmax_cut > 0 else 0

        # Self-consistent at d=4
        if C_cut > 0:
            _, _, x_4 = self_consistent_species_scale(C_cut, 4, M_P, M_KK)
            _, _, x_8 = self_consistent_species_scale(C_cut, 8, M_P, M_KK)
            print(f"  L_max={L_cut}: N_total={N_cut:8d}, lambda_max={lmax_cut:.4f}, "
                  f"C_weyl={C_cut:.2f}, x(d=4)={x_4:.4e}, x(d=8)={x_8:.4e}")

# ===========================================================================
# Direct species count (not using Weyl extrapolation)
# ===========================================================================
print("\n" + "="*80)
print("DIRECT SPECIES COUNT (within computed spectrum, L_max=6)")
print("="*80)

# The W6 ratio is Lambda_SA / M_KK = 1.02e6
# So Lambda_SA corresponds to lambda_cut = 1.02e6 in dimensionless units.
# But our spectrum only goes up to lambda ~ 4.1.
# ALL 439,488 modes are below Lambda_SA.
#
# The question is: how many modes exist at ALL levels (not just L_max=6)?
# For SU(3) with Dirac operator:
# - Each sector (p,q) has Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3
# - The Dirac eigenvalues scale as ~sqrt(C_2) for large (p,q)
# - The largest eigenvalue in sector (p,q) scales as ~sqrt(C_2(p,q))
# - The number of sectors with sqrt(C_2) < Lambda goes as Lambda^8 (Weyl)
#
# For the self-consistent computation:
# The W6 scale ratio Lambda_SA/M_KK = 10^6 means we need N_species at lambda_cut = 10^6
# That is far beyond L_max=6 (where lambda_max ~ 4).

print("\nW6 context:")
print(f"  Lambda_SA / M_KK = {Lambda_SA/M_KK:.3e}")
print(f"  Max computed eigenvalue (L_max=6, tau=0.5): {np.max(np.abs(d['eigenvalues_8'])):.4f}")
print(f"  All computed modes are at lambda << Lambda_SA/M_KK")
print(f"  Weyl extrapolation required for N_species at Lambda_SA")
print()

# Compute N_species at Lambda_SA/M_KK using Weyl law
for tau_idx in range(n_tau):
    tau = tau_values[tau_idx]
    C_w = C_weyl_arr[tau_idx]
    lambda_cut = Lambda_SA / M_KK  # = 1.02e6
    N_at_SA = C_w * lambda_cut**8

    # Species scale at this N_species
    Lambda_sp_d4 = M_P / np.sqrt(N_at_SA)
    Lambda_sp_d8 = M_P / N_at_SA**(1/6)

    print(f"tau={tau:.2f}: N_species(Lambda_SA) = {N_at_SA:.3e}, "
          f"Lambda_sp(d=4) = {Lambda_sp_d4:.3e} GeV = {Lambda_sp_d4/M_KK:.3e} M_KK, "
          f"Lambda_sp(d=8) = {Lambda_sp_d8:.3e} GeV = {Lambda_sp_d8/M_KK:.3e} M_KK")

# ===========================================================================
# THE KEY RESULT: Self-consistent species scale at the fold tau=0.190
# ===========================================================================
print("\n" + "="*80)
print("KEY RESULT: SPECIES SCALE AT THE FOLD (tau ~ 0.190)")
print("="*80)

# Interpolate to tau = 0.190 using tau=0.15 and tau=0.20 data
tau_fold = 0.190
tau_idx_lo, tau_idx_hi = 2, 3  # tau=0.15, tau=0.20
w = (tau_fold - tau_values[tau_idx_lo]) / (tau_values[tau_idx_hi] - tau_values[tau_idx_lo])

C_w_fold = C_weyl_arr[tau_idx_lo] * (1-w) + C_weyl_arr[tau_idx_hi] * w

# Self-consistent species scale
Lambda_sp_4_fold, N_sp_4_fold, x_4_fold = self_consistent_species_scale(C_w_fold, 4, M_P, M_KK)
Lambda_sp_8_fold, N_sp_8_fold, x_8_fold = self_consistent_species_scale(C_w_fold, 8, M_P, M_KK)

print(f"tau_fold = {tau_fold}")
print(f"C_weyl (interpolated) = {C_w_fold:.2f}")
print()
print(f"d=4 effective theory:")
print(f"  Lambda_species / M_KK = {x_4_fold:.6e}")
print(f"  Lambda_species = {Lambda_sp_4_fold:.4e} GeV")
print(f"  N_species = {N_sp_4_fold:.4e}")
print(f"  log10(Lambda_species / M_KK) = {np.log10(x_4_fold):.4f}")
print()
print(f"d=8 (synthesis convention):")
print(f"  Lambda_species / M_KK = {x_8_fold:.6e}")
print(f"  Lambda_species = {Lambda_sp_8_fold:.4e} GeV")
print(f"  N_species = {N_sp_8_fold:.4e}")
print(f"  log10(Lambda_species / M_KK) = {np.log10(x_8_fold):.4f}")

# ===========================================================================
# Gate classification
# ===========================================================================
print("\n" + "="*80)
print("GATE CLASSIFICATION: W6-SPECIES-36")
print("="*80)

for d_eff, x_fold, label in [(4, x_4_fold, "d=4"), (8, x_8_fold, "d=8")]:
    log_ratio = np.log10(x_fold)
    if 0.1 <= x_fold <= 10:
        verdict = "THIN (PASS)"
    elif x_fold < 0.1:
        verdict = "THICK (FAIL)"
    else:
        verdict = "HARMLESS (PASS)"

    print(f"\n{label}: Lambda_species / M_KK = {x_fold:.4e} (log10 = {log_ratio:.2f})")
    print(f"  Gate verdict: {verdict}")

# ===========================================================================
# Cross-checks
# ===========================================================================
print("\n" + "="*80)
print("CROSS-CHECKS")
print("="*80)

# Cross-check 1: Weyl law consistency
print("\n1. Weyl law power-law check:")
for tau_idx in [0, 3]:
    tau = tau_values[tau_idx]
    abs_evals, mults = get_spectrum_with_multiplicities(d, tau_idx)
    sector_p = d[f'sector_p_{tau_idx}']
    sector_q = d[f'sector_q_{tau_idx}']

    # Compute N(lambda) at several thresholds
    thresholds_ck = np.array([1.0, 1.5, 2.0, 2.5])
    Ns = []
    for th in thresholds_ck:
        Ns.append(count_species(abs_evals, mults, th))

    # Check log(N)/log(lambda) approaches 8
    for i in range(1, len(thresholds_ck)):
        if Ns[i] > 0 and Ns[i-1] > 0 and Ns[i] != Ns[i-1]:
            eff_d = (np.log(Ns[i]) - np.log(Ns[i-1])) / (np.log(thresholds_ck[i]) - np.log(thresholds_ck[i-1]))
            print(f"  tau={tau:.2f}: between lambda={thresholds_ck[i-1]:.1f} and {thresholds_ck[i]:.1f}: "
                  f"N changes {Ns[i-1]} -> {Ns[i]}, effective dim = {eff_d:.1f}")

# Cross-check 2: Compare with analytic SU(3) results at tau=0
print("\n2. SU(3) bi-invariant (tau=0) analytic check:")
print("   At tau=0, the Dirac eigenvalues are determined by the Casimir.")
print(f"   Computed C_weyl(tau=0) = {C_weyl_arr[0]:.2f}")
print(f"   Total modes at L_max=6: {results[0.0]['N_total']}")

# Analytic: sum_{p+q <= L} dim(p,q)^2 * 16
N_analytic = 0
for p in range(7):
    for q in range(7-p):
        d_pq = dim_su3(p, q)
        N_analytic += d_pq**2 * 16
# Wait: that's the total number of matrix elements, not the correct count.
# The correct count is: sum over sectors of (n_evals_in_sector * dim(p,q))
# where n_evals_in_sector = 16 * dim(p,q) (from the data structure)
# But each eigenvalue has multiplicity dim(p,q).
# So total = sum of 16 * dim(p,q) * dim(p,q) = 16 * sum dim(p,q)^2
N_analytic_check = 16 * sum(dim_su3(p,q)**2 for p in range(7) for q in range(7-p))
print(f"   Analytic check: 16 * sum(dim^2) = {N_analytic_check}")
print(f"   From data: {results[0.0]['N_total']}")
# These should be different because the stored multiplicity is dim(p,q), not dim(p,q)^2

# Recount: total from data = sum(mults) = sum over all eigenvalues of their stored multiplicity
# The stored multiplicity = dim(p,q) for each eigenvalue.
# There are 16*dim(p,q) eigenvalues in each sector.
# So sum(mults) = sum over sectors of 16*dim(p,q)*dim(p,q) = 16*sum(dim^2) if mult=dim.
# Let me verify this.
abs_e0, m0 = get_spectrum_with_multiplicities(d, 0)
print(f"   sum(mults) from data = {int(np.sum(m0))}")
N_check = 0
labels_0 = d['sector_labels_0']
for i, (p,q) in enumerate(labels_0):
    dim_pq = dim_su3(p, q)
    size_i = d['sector_sizes_0'][i]
    # Each eigenvalue in this sector has mult = dim_pq
    N_check += size_i * dim_pq  # size_i eigenvalues, each with mult dim_pq
print(f"   sum(sector_size * dim) = {N_check}")
print(f"   16 * sum(dim^2) = {16 * sum(dim_su3(p,q)**2 for p in range(7) for q in range(7-p))}")

# Cross-check 3: Lambda_species must be > M_KK for EFT validity
print("\n3. EFT validity check:")
print(f"   For d=4: Lambda_species = {Lambda_sp_4_fold:.3e} GeV")
print(f"   For d=8: Lambda_species = {Lambda_sp_8_fold:.3e} GeV")
print(f"   M_KK = {M_KK:.3e} GeV")
print(f"   M_P = {M_P:.3e} GeV")
print(f"   Lambda_SA = {Lambda_SA:.3e} GeV")

# Cross-check 4: Does the hierarchy make sense?
print("\n4. Scale hierarchy:")
print(f"   M_KK < Lambda_species(d=4) < M_P? ", end="")
print(f"{'YES' if M_KK < Lambda_sp_4_fold < M_P else 'NO'}")
print(f"   M_KK < Lambda_species(d=8) < M_P? ", end="")
print(f"{'YES' if M_KK < Lambda_sp_8_fold < M_P else 'NO'}")

# ===========================================================================
# Detailed tau dependence at the fold
# ===========================================================================
print("\n" + "="*80)
print("TAU DEPENDENCE OF SPECIES SCALE")
print("="*80)

tau_arr = np.array(tau_values)
x4_arr = np.array([sc_results_d4[i][3] for i in range(n_tau)])
x8_arr = np.array([sc_results_d8[i][3] for i in range(n_tau)])
Nsp4_arr = np.array([sc_results_d4[i][2] for i in range(n_tau)])
Nsp8_arr = np.array([sc_results_d8[i][2] for i in range(n_tau)])

print(f"\n{'tau':>6s} {'log10(Lambda_sp/M_KK) [d=4]':>28s} {'log10(Lambda_sp/M_KK) [d=8]':>28s} {'C_weyl':>10s}")
for i in range(n_tau):
    print(f"{tau_arr[i]:6.3f} {np.log10(x4_arr[i]):28.4f} {np.log10(x8_arr[i]):28.4f} {C_weyl_arr[i]:10.2f}")

# ===========================================================================
# Save results
# ===========================================================================
np.savez('tier0-computation/s36_species_scale.npz',
    tau_values=tau_arr,
    C_weyl=np.array(C_weyl_arr),
    Lambda_sp_over_MKK_d4=x4_arr,
    Lambda_sp_over_MKK_d8=x8_arr,
    N_species_d4=Nsp4_arr,
    N_species_d8=Nsp8_arr,
    Lambda_sp_d4=np.array([sc_results_d4[i][1] for i in range(n_tau)]),
    Lambda_sp_d8=np.array([sc_results_d8[i][1] for i in range(n_tau)]),
    tau_fold=tau_fold,
    x4_fold=x_4_fold,
    x8_fold=x_8_fold,
    N_sp_4_fold=N_sp_4_fold,
    N_sp_8_fold=N_sp_8_fold,
    M_P=M_P, M_KK=M_KK, Lambda_SA=Lambda_SA
)
print("\nSaved: tier0-computation/s36_species_scale.npz")

# ===========================================================================
# Plot
# ===========================================================================
fig = plt.figure(figsize=(14, 10))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

# Panel 1: Lambda_species / M_KK vs tau
ax1 = fig.add_subplot(gs[0, 0])
ax1.semilogy(tau_arr, x4_arr, 'bo-', linewidth=2, markersize=6, label=r'$d_{\rm eff}=4$')
ax1.semilogy(tau_arr, x8_arr, 'rs-', linewidth=2, markersize=6, label=r'$d_{\rm eff}=8$')
ax1.axhline(y=10, color='green', linestyle='--', alpha=0.5, label='THIN upper')
ax1.axhline(y=0.1, color='green', linestyle='--', alpha=0.5, label='THIN lower')
ax1.axvline(x=0.190, color='gray', linestyle=':', alpha=0.7, label=r'$\tau_{\rm fold}$')
ax1.set_xlabel(r'$\tau$', fontsize=12)
ax1.set_ylabel(r'$\Lambda_{\rm species} / M_{\rm KK}$', fontsize=12)
ax1.set_title(r'Species Scale vs Jensen Parameter', fontsize=13)
ax1.legend(fontsize=9, loc='best')
ax1.grid(True, alpha=0.3)

# Panel 2: N_species vs tau
ax2 = fig.add_subplot(gs[0, 1])
ax2.semilogy(tau_arr, Nsp4_arr, 'bo-', linewidth=2, markersize=6, label=r'$N_{\rm species}$ ($d=4$)')
ax2.semilogy(tau_arr, Nsp8_arr, 'rs-', linewidth=2, markersize=6, label=r'$N_{\rm species}$ ($d=8$)')
ax2.axvline(x=0.190, color='gray', linestyle=':', alpha=0.7, label=r'$\tau_{\rm fold}$')
ax2.set_xlabel(r'$\tau$', fontsize=12)
ax2.set_ylabel(r'$N_{\rm species}$', fontsize=12)
ax2.set_title(r'Self-Consistent Species Count', fontsize=13)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Scale hierarchy diagram
ax3 = fig.add_subplot(gs[1, 0])
scales = {
    r'$M_{\rm KK}$': M_KK,
    r'$\Lambda_{\rm sp}(d\!=\!4)$': Lambda_sp_4_fold,
    r'$\Lambda_{\rm sp}(d\!=\!8)$': Lambda_sp_8_fold,
    r'$\Lambda_{\rm SA}$': Lambda_SA,
    r'$M_{\rm P}$': M_P,
}
labels_sorted = sorted(scales.keys(), key=lambda k: scales[k])
values_sorted = [np.log10(scales[k]) for k in labels_sorted]

colors_bar = ['#2196F3', '#FF9800', '#FF5722', '#4CAF50', '#9C27B0']
ax3.barh(range(len(labels_sorted)), values_sorted, color=colors_bar[:len(labels_sorted)],
         height=0.6, alpha=0.8)
ax3.set_yticks(range(len(labels_sorted)))
ax3.set_yticklabels(labels_sorted, fontsize=11)
ax3.set_xlabel(r'$\log_{10}(\Lambda / {\rm GeV})$', fontsize=12)
ax3.set_title(r'Scale Hierarchy at $\tau_{\rm fold}=0.190$', fontsize=13)
ax3.grid(True, alpha=0.3, axis='x')

# Panel 4: C_weyl vs tau (Weyl coefficient stability)
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(tau_arr, C_weyl_arr, 'ko-', linewidth=2, markersize=6)
ax4.axvline(x=0.190, color='gray', linestyle=':', alpha=0.7, label=r'$\tau_{\rm fold}$')
ax4.set_xlabel(r'$\tau$', fontsize=12)
ax4.set_ylabel(r'$C_{\rm Weyl} = N_{\rm total} / \lambda_{\rm max}^8$', fontsize=12)
ax4.set_title(r'Weyl Coefficient vs $\tau$', fontsize=13)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

fig.suptitle('W6-SPECIES-36: Species Scale Computation for W6 Wall Resolution',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig('tier0-computation/s36_species_scale.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s36_species_scale.png")
plt.close()

# ===========================================================================
# FINAL SUMMARY
# ===========================================================================
print("\n" + "="*80)
print("FINAL SUMMARY")
print("="*80)
print(f"""
Species Scale at tau_fold = {tau_fold}:

  d=4 convention (4D EFT, standard Swampland):
    Lambda_species / M_KK = {x_4_fold:.4e}
    Lambda_species = {Lambda_sp_4_fold:.4e} GeV
    N_species = {N_sp_4_fold:.4e}
    log10(Lambda_species / M_KK) = {np.log10(x_4_fold):.2f}

  d=8 convention (synthesis, 8D internal):
    Lambda_species / M_KK = {x_8_fold:.4e}
    Lambda_species = {Lambda_sp_8_fold:.4e} GeV
    N_species = {N_sp_8_fold:.4e}
    log10(Lambda_species / M_KK) = {np.log10(x_8_fold):.2f}

Gate W6-SPECIES-36:
  Criterion: THIN if Lambda_species/M_KK in [0.1, 10]
             THICK if Lambda_species/M_KK < 0.1
             HARMLESS if Lambda_species/M_KK > 10

  d=4: Lambda_species/M_KK = {x_4_fold:.4e} => {"HARMLESS (PASS)" if x_4_fold > 10 else ("THIN (PASS)" if x_4_fold >= 0.1 else "THICK (FAIL)")}
  d=8: Lambda_species/M_KK = {x_8_fold:.4e} => {"HARMLESS (PASS)" if x_8_fold > 10 else ("THIN (PASS)" if x_8_fold >= 0.1 else "THICK (FAIL)")}

  The W6 wall is {"resolved — the species scale exceeds M_KK" if min(x_4_fold, x_8_fold) > 0.1 else "NOT resolved"}.
""")
