#!/usr/bin/env python3
"""
s64_transfer_bogoliubov.py — A_s Transfer Function via Bogoliubov Projection
=============================================================================

Gate: TRANSFER-BOGOLIUBOV-64
  PASS: |beta_proj|^2 varies by < factor 2 across cutoff choices (trans-Planckian universality)
  FAIL: > factor 10 variation (cutoff-sensitive)

PHYSICS:
    The scalar amplitude A_s at the CMB scale derives from spectral action
    perturbations in the (0,0) Peter-Weyl sector of D_K on SU(3). These
    singlet modes are the ONLY modes that project to 4D scalar perturbations
    without representation-theoretic suppression (all higher (p,q) modes
    carry SU(3) quantum numbers and decouple from the 4D scalar sector).

    The (0,0) sector contains 16 eigenvalues with multiplicity dim=1.
    Their spectral weight is S_occ_00 = 6.016 (0.032% of S_occ = 18,852).

    To propagate from the KK scale (~10^16 GeV) to the CMB scale (~10^{-4} eV),
    these perturbations must traverse 16 hybridization gaps in the phononic
    crystal structure of the coupled A-B-C spectrum (S62). Each gap acts as
    a tunneling barrier for the spectral action perturbation amplitude.

    The Bogoliubov transformation through gap j with width Delta_j and
    bandwidth W_j gives a transmission coefficient:

        |T_j|^2 = 1 / (1 + (Delta_j / W_j)^2 * pi^2 / 4)    (Landau-Zener form)

    For the spectral action perturbation, the "bandwidth" is the local
    density of states (DOS) weighted by the cutoff function f(x). This
    makes the transmission cutoff-dependent in principle.

    Three cutoff families are tested:
        1. Gaussian: f(x) = exp(-x)
        2. Sharp:    f(x) = Theta(1-x)
        3. Zeta:     f(x) = (1+x)^{-s} with s=4 (Bessel regularization)

    The trans-Planckian universality conjecture (Chamseddine-Connes) states
    that A_s should depend only on the spectral moments a_0, a_2, a_4 and
    NOT on the detailed form of f(x). If |beta_proj|^2 is cutoff-insensitive,
    this confirms universality for the transfer function.

    Architecture:
        1. Load (0,0) sector eigenvalues from D_K spectrum
        2. Load 16 hybridization gaps from S62 phonon dispersion
        3. Compute Bogoliubov coefficients through each gap for each cutoff
        4. Total |beta_proj|^2 = product (sequential tunneling)
        5. Peter-Weyl selection factor: dim(0,0)^2 / sum dim(p,q)^2 = 1/155984
        6. Report total suppression and A_s gap

Session: S64 W3-D
Author: gen-physicist
Depends on: S62 phonon_dispersion_full, S64 occ_spec, S63 epsilon_decompose
"""

import sys
import os
import time
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, M_KK, M_KK_gravity, M_KK_kerner,
    A_s_CMB, PI, Delta_0_OES, E_cond,
    Vol_SU3_Haar, G_DeWitt,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s64_transfer_bogoliubov.npz"
OUT_PNG = SCRIPT_DIR / "s64_transfer_bogoliubov.png"

t_start = time.time()

print("=" * 78)
print("S64 TRANSFER-BOGOLIUBOV-64: A_s Transfer Function via Bogoliubov Projection")
print("=" * 78)

# =============================================================================
# SECTION 1: Load input data
# =============================================================================
print("\n--- Section 1: Load input data ---")

# S62: Hybridization gaps from phononic crystal
d62 = np.load(SCRIPT_DIR / "s62_phonon_dispersion_full.npz", allow_pickle=True)
omega_full = d62['omega_full']          # (32, 45) eigenvalues at each k
evecs_full = d62['evecs_full']          # (32, 45, 45) eigenvectors
sector_weight = d62['sector_weight']    # (32, 45, 3) sector decomposition
omega_A = d62['omega_A']               # (36,) Sector A frequencies
omega_B_unc = d62['omega_B_uncoupled'] # (32, 8) Sector B uncoupled
omega_C_unc = d62['omega_C_uncoupled'] # (32, 1) Sector C uncoupled
lambda_n = d62['lambda_n']             # (32,) graph Laplacian eigenvalues
AB_coupled_gaps = d62['AB_coupled_gaps']  # (69,) all A-B gaps
AB_delta_gaps = d62['AB_delta_gaps']      # (69,) coupling-induced openings
AB_detunings = d62['AB_detunings']        # (69,) detunings
V_AB = d62['V_AB']                     # (36, 8) A-B coupling matrix
E_J_fold = float(d62['E_J_fold'])

# S64: (0,0) sector spectral weight
d64 = np.load(SCRIPT_DIR / "s64_occ_spec.npz", allow_pickle=True)
all_omega = d64['all_omega']      # all eigenvalues
all_v2 = d64['all_v2']            # Bogoliubov v^2 factors
all_mult = d64['all_mult']        # multiplicities
S_occ_total = float(d64['S_occ'])
sectors = d64['sectors']
sector_S_occ = d64['sector_S_occ']
sector_v2_mean = d64['sector_v2_mean']

# S63: Cutoff function moments
d63 = np.load(SCRIPT_DIR / "s63_epsilon_decompose.npz", allow_pickle=True)
f0 = float(d63['f0'])    # zeroth moment
f2 = float(d63['f2'])    # second moment
f4 = float(d63['f4'])    # fourth moment

# (0,0) sector identification
idx_00 = np.where(sectors == '(0,0)')[0][0]
S_occ_00 = sector_S_occ[idx_00]
v2_mean_00 = sector_v2_mean[idx_00]

# (0,0) eigenvalues: these have mult=1
mask_00 = all_mult == 1
omega_00 = all_omega[mask_00]   # 16 eigenvalues
v2_00 = all_v2[mask_00]         # their v^2 factors

print(f"Loaded S62 phonon dispersion: {omega_full.shape[0]} k-points x {omega_full.shape[1]} modes")
print(f"  Hybridization gaps: {len(AB_coupled_gaps)} A-B crossings")
print(f"  V_AB norm: {np.linalg.norm(V_AB):.4f} M_KK")
print(f"Loaded S64 occupation spectrum:")
print(f"  S_occ_total = {S_occ_total:.4f}")
print(f"  S_occ_(0,0) = {S_occ_00:.6f} ({S_occ_00/S_occ_total*100:.4f}%)")
print(f"  (0,0) eigenvalues: {len(omega_00)} modes")
print(f"  omega_(0,0) range: [{omega_00.min():.4f}, {omega_00.max():.4f}] M_KK")
print(f"  v^2_(0,0) range: [{v2_00.min():.6f}, {v2_00.max():.6f}]")
print(f"  <v^2>_(0,0) = {v2_mean_00:.6f}")
print(f"Loaded S63 cutoff moments: f0={f0:.4f}, f2={f2:.4f}, f4={f4:.4f}")

# =============================================================================
# SECTION 2: Identify the 16 relevant hybridization gaps
# =============================================================================
print("\n--- Section 2: Identify hybridization gaps for (0,0) sector ---")

# The (0,0) sector eigenvalues sit in the range [0.82, 0.97] M_KK.
# These are in Sector B (BCS quasiparticle energies).
# The hybridization gaps relevant to propagation from KK to 4D are:
#
# Physical picture: A spectral action perturbation at KK scale in the (0,0)
# sector must propagate through the phononic crystal band structure.
# At each avoided crossing between sectors, part of the amplitude is
# reflected (beta coefficient) and part transmitted (alpha coefficient).
#
# The 16 A-B crossings from S62 (tight, detuning < 0.1) serve as the
# physical tunneling barriers. However, the (0,0) modes at ~0.9 M_KK
# are BELOW the Sector A range (3.88-12.19 M_KK), so they do not
# directly encounter A-B crossings. Instead, the transfer occurs through:
#
# 1. B-sector internal structure: The 8 BCS modes per cell disperse
#    across the 32-cell graph. The (0,0) modes see the FULL B-sector
#    band structure, including all hybridization-induced avoided crossings.
#
# 2. The critical gaps are at the BAND EDGES where van Hove singularities
#    create strong scattering. From S62, these occur at specific k-points.
#
# Strategy: Compute the FULL Bogoliubov transformation for a perturbation
# in the (0,0) sector propagating through the entire coupled spectrum.

# Extract the 16 tight-crossing hybridization gaps (detuning < 0.1)
tight_mask = AB_detunings < 0.1
tight_gaps = AB_coupled_gaps[tight_mask]
tight_deltas = AB_delta_gaps[tight_mask]
tight_detunings = AB_detunings[tight_mask]

# Sort by gap size (descending)
sort_idx = np.argsort(tight_gaps)[::-1]
tight_gaps = tight_gaps[sort_idx]
tight_deltas = tight_deltas[sort_idx]
tight_detunings = tight_detunings[sort_idx]

N_gaps = len(tight_gaps)
print(f"Tight hybridization gaps (detuning < 0.1): {N_gaps}")
for i in range(N_gaps):
    print(f"  Gap {i+1:2d}: Delta = {tight_gaps[i]:.6f} M_KK, "
          f"delta_gap = {tight_deltas[i]:.6f}, detuning = {tight_detunings[i]:.6f}")

# Compute effective bandwidths at each crossing.
# The bandwidth is the local DOS inverse at the crossing energy.
# From S62: Sector B bandwidth = 51.60 M_KK (total per band).
# The local bandwidth at a crossing with Sector A is set by the
# B-sector dispersion rate: W_j = E_J * |d(lambda_n)/dk| at the crossing k.
#
# For the CG(24) graph, lambda_n ranges from 0 to 7.33, with
# N_k = 32 points. The mean spacing is ~0.23.

# Compute bandwidths from B-sector dispersion
# At each crossing, the local bandwidth is the rate at which B modes
# sweep through the crossing energy as k varies.
# W_j ~ E_J * delta(lambda) where delta(lambda) is the local
# graph Laplacian eigenvalue spacing.

lambda_spacing = np.diff(np.sort(lambda_n))
mean_lambda_spacing = np.mean(lambda_spacing)
W_local = E_J_fold * mean_lambda_spacing  # Mean local bandwidth per k-step

print(f"\nLocal bandwidth parameters:")
print(f"  E_J at fold = {E_J_fold:.4f} M_KK")
print(f"  Mean lambda spacing = {mean_lambda_spacing:.4f}")
print(f"  W_local = E_J * <delta_lambda> = {W_local:.4f} M_KK")

# The physical bandwidth for each gap is the SECTOR B band velocity
# times the k-space extent. For tight crossings, the relevant bandwidth
# is the full B-sector dispersion bandwidth / N_k (local momentum resolution):
W_B_total = 51.603  # Total B-sector bandwidth (M_KK)  # (local)
W_B_per_k = W_B_total / 32  # Per k-point bandwidth
print(f"  W_B total = {W_B_total:.3f} M_KK")
print(f"  W_B per k-point = {W_B_per_k:.4f} M_KK")

# =============================================================================
# SECTION 3: Three cutoff function families
# =============================================================================
print("\n--- Section 3: Cutoff function families ---")

# The spectral action S = Tr f(D^2/Lambda^2) depends on the cutoff f.
# The Seeley-DeWitt expansion gives:
#   S ~ f_4 Lambda^8 a_0 + f_2 Lambda^6 a_2 + f_0 Lambda^4 a_4
# where f_k = int_0^inf f(u) u^{k/2-1} du (Mellin moments).
#
# Different f choices give different f_k values but the SAME a_k.
# The question is whether the Bogoliubov coefficients, which depend
# on the detailed propagation through the spectrum, are cutoff-sensitive.
#
# Three families:
# 1. GAUSSIAN: f(x) = exp(-x)
#    f_k = Gamma(k/2) => f_0 = 1, f_2 = 1, f_4 = 1
#    (normalized to match moments)
#
# 2. SHARP: f(x) = Theta(1-x)
#    f_k = 2/k => f_0 = 2, f_2 = 1, f_4 = 1/2
#
# 3. ZETA: f(x) = (1+x)^{-s}, s=4
#    f_k = Gamma(k/2)*Gamma(s-k/2)/Gamma(s)
#    f_0 = Gamma(4)/Gamma(4) * Gamma(4) = 6, f_2 = 1/3 * 6 = 2, f_4 = 1

# Normalize all families so that f_2*a_2 + f_4*a_4 matches a common value.
# The physical content is in the RATIO of contributions.

# Actual moments from S63 data (used as reference):
# f0 = 9.817, f2 = 2.340, f4 = 0.558

# Define three families with standard Mellin moments:
cutoff_families = {
    'Gaussian': {'f0': 1.0, 'f2': 1.0, 'f4': 1.0,
                 'desc': 'f(x) = exp(-x)'},
    'Sharp':    {'f0': 2.0, 'f2': 1.0, 'f4': 0.5,
                 'desc': 'f(x) = Theta(1-x)'},
    'Zeta_s4':  {'f0': 6.0, 'f2': 2.0, 'f4': 1.0,
                 'desc': 'f(x) = (1+x)^{-4}'},
}

# Normalized to match the S63 reference at second order:
# f2_ref * a2 is the gravity sector contribution. We normalize
# each family so that f2 * a2 = f2_ref * a2_ref.
for name, fam in cutoff_families.items():
    scale = f2 / fam['f2']
    fam['f0_scaled'] = fam['f0'] * scale
    fam['f2_scaled'] = fam['f2'] * scale
    fam['f4_scaled'] = fam['f4'] * scale

print("Cutoff families (raw and scaled to match f2*a2):")
for name, fam in cutoff_families.items():
    print(f"  {name:10s}: f0={fam['f0']:.1f}, f2={fam['f2']:.1f}, f4={fam['f4']:.1f} "
          f"-> scaled: f0={fam['f0_scaled']:.4f}, f2={fam['f2_scaled']:.4f}, f4={fam['f4_scaled']:.4f}")

# =============================================================================
# SECTION 4: Bogoliubov transformation through hybridization gaps
# =============================================================================
print("\n--- Section 4: Bogoliubov transformation ---")

# The Bogoliubov transformation for a spectral action perturbation
# propagating through a hybridization gap is derived from the
# analogy with quantum tunneling in a periodic potential.
#
# At each avoided crossing with gap Delta_j and local bandwidth W_j,
# the scattering matrix is:
#
#   S_j = ( alpha_j   beta_j  )
#         ( beta_j*   alpha_j* )
#
# where |alpha_j|^2 - |beta_j|^2 = 1 (Bogoliubov condition).
#
# The Landau-Zener transmission probability through the gap:
#
#   |alpha_j|^2 = exp(-pi * Delta_j^2 / (2 * hbar * v_j))     (LZ)
#
# where v_j = dE/dt is the level velocity at the crossing.
# In the spectral action context, v_j = W_j (bandwidth = level velocity).
#
# The reflection probability:
#   |beta_j|^2 = 1 - |alpha_j|^2
#
# For SEQUENTIAL tunneling through N gaps, the total transmission is:
#   |alpha_total|^2 = product_j |alpha_j|^2
#   |beta_proj|^2 = 1 - |alpha_total|^2
#
# But the physical quantity we want is NOT the total transmission.
# We want the PROJECTED Bogoliubov coefficient: how much of the
# (0,0) sector spectral weight appears in the 4D scalar channel.
#
# The key insight from the workshop (E3, QA-E3): the transfer function
# depends on the TOTAL (0,0) spectral weight, not on individual gap details.
# This is because the spectral action is a TRACE — it sums over all modes.
# The hybridization gaps redistribute spectral weight between sectors
# but preserve the total trace.
#
# Therefore:
#   |beta_proj|^2 = (spectral weight in 4D channel) / (total KK spectral weight)
#                 = S_occ_(0,0) / S_occ_total * (Peter-Weyl factor) * (gap suppression)
#
# The Peter-Weyl factor: (0,0) has dim=1. Total dim^2 = sum_pq dim(p,q)^2.
# From S7-8: the total number of eigenvalues at L_max=10 is 155,984.
# The (0,0) sector contributes 16 eigenvalues.
# Peter-Weyl weight = 16 / 155,984 = 1.026e-4.
#
# But S_occ already includes this weighting (it's computed with mult=dim^2).
# So the suppression is simply S_occ_(0,0) / S_fold.

# Method: Direct computation through the phononic crystal band structure.
# Model the propagation as a 1D scattering problem through N_gaps barriers.
# Each barrier has:
#   - Gap width: Delta_j (from S62 tight crossings)
#   - Barrier thickness: determined by the inverse coupling strength |V_AB|
#   - The tunneling probability depends on the ratio Delta_j / W_eff_j

def compute_bogoliubov_sequential(gaps, bandwidths, cutoff_weights=None):
    """
    Compute total |beta_proj|^2 for sequential tunneling through N gaps.

    The Landau-Zener transmission through each gap j:
        P_trans_j = exp(-pi * Delta_j^2 / (2 * W_j))

    Total transmission = product of individual transmissions.

    The cutoff function enters through the DOS weighting:
        W_eff_j = W_j * (f_n * a_n at energy E_j) / (f_n * a_n reference)

    If cutoff_weights is provided, it modifies the effective bandwidth
    at each gap according to the local spectral action weight.

    Parameters:
        gaps: array of gap widths (M_KK)
        bandwidths: array of local bandwidths (M_KK)
        cutoff_weights: optional array of cutoff-dependent weights

    Returns:
        P_trans_total: total transmission probability
        P_trans_per_gap: individual transmissions
    """
    N = len(gaps)
    if cutoff_weights is None:
        cutoff_weights = np.ones(N)

    P_trans = np.zeros(N)
    for j in range(N):
        W_eff = bandwidths[j] * cutoff_weights[j]
        # Landau-Zener: P = exp(-pi Delta^2 / (2 W))
        exponent = PI * gaps[j]**2 / (2.0 * W_eff)
        P_trans[j] = np.exp(-exponent)

    P_total = np.prod(P_trans)
    return P_total, P_trans


def compute_bogoliubov_parallel(gaps, bandwidths, cutoff_weights=None):
    """
    Compute |beta_proj|^2 for parallel channels through N gaps.

    In the parallel picture, each gap provides an independent channel.
    The total transmission is the SUM of individual transmissions
    (weighted by mode density at each crossing).

    Parameters:
        gaps: array of gap widths (M_KK)
        bandwidths: array of local bandwidths (M_KK)
        cutoff_weights: optional array of cutoff-dependent weights

    Returns:
        P_trans_total: total transmission (sum of channels)
        P_trans_per_gap: individual transmissions
    """
    N = len(gaps)
    if cutoff_weights is None:
        cutoff_weights = np.ones(N)

    P_trans = np.zeros(N)
    for j in range(N):
        W_eff = bandwidths[j] * cutoff_weights[j]
        exponent = PI * gaps[j]**2 / (2.0 * W_eff)
        P_trans[j] = np.exp(-exponent)

    # Parallel: sum with equal weight per channel (normalized)
    P_total = np.mean(P_trans)
    return P_total, P_trans


# Compute bandwidths for each gap.
# The bandwidth at each crossing is determined by the Sector B
# dispersion rate at that k-point. Since we have the full coupled
# spectrum, we compute the local level velocity.

# For each tight crossing, the bandwidth is the energy difference
# between adjacent k-points at the crossing energy:
bandwidths_per_gap = np.zeros(N_gaps)
for j in range(N_gaps):
    # Use the B-sector bandwidth dispersed over all k-points
    # The effective bandwidth at a crossing is:
    # W_j = E_J * delta_lambda * (number of modes at crossing energy)
    #
    # For tight crossings, the detuning is small, meaning the A and B
    # modes are nearly resonant. The bandwidth is dominated by the
    # B-sector dispersion rate.
    bandwidths_per_gap[j] = W_local  # E_J * mean lambda spacing

print(f"Gap parameters (N={N_gaps}):")
print(f"  Gap range: [{tight_gaps.min():.6f}, {tight_gaps.max():.6f}] M_KK")
print(f"  Bandwidth (uniform): {W_local:.4f} M_KK")
print(f"  Gap/bandwidth ratio range: [{(tight_gaps/W_local).min():.4f}, {(tight_gaps/W_local).max():.4f}]")

# =============================================================================
# SECTION 5: Cutoff-dependent weights
# =============================================================================
print("\n--- Section 5: Cutoff-dependent weighting ---")

# The spectral action at energy E has contributions from all three
# Seeley-DeWitt orders. The relative weight depends on the cutoff:
#
#   w(E) = f_4 * Lambda^8 * a0_density(E) + f_2 * Lambda^6 * a2_density(E)
#          + f_0 * Lambda^4 * a4_density(E)
#
# At the hybridization gaps (E ~ 4-12 M_KK), the a_0 contribution
# (cosmological constant) is uniform, while a_2 (gravity) and a_4 (gauge)
# are energy-dependent.
#
# For the cutoff test, we compute the RATIO of spectral weights
# at the gap energies for each cutoff family:
#
#   w_cutoff(E) / w_reference(E) = [f4*a0 + f2*a2(E) + f0*a4(E)] / [f4_ref*a0 + ...]
#
# Since a_0 is constant and a_2, a_4 are monotonic in tau (not in energy),
# the energy dependence enters only through the eigenvalue-resolved
# contributions. For a first computation, use the BULK Seeley-DeWitt
# coefficients (not eigenvalue-resolved).

# At the fold: spectral action contributions from each order
S_a0 = f0 * a0_fold  # = 9.817 * 6440 = 63222
S_a2 = f2 * a2_fold  # = 2.340 * 2776 = 6496
S_a4 = f4 * a4_fold  # = 0.558 * 1351 = 753
S_total_ref = S_a0 + S_a2 + S_a4

print(f"Reference spectral action at fold:")
print(f"  f0*a0 = {S_a0:.2f} ({S_a0/S_total_ref*100:.1f}%)")
print(f"  f2*a2 = {S_a2:.2f} ({S_a2/S_total_ref*100:.1f}%)")
print(f"  f4*a4 = {S_a4:.2f} ({S_a4/S_total_ref*100:.1f}%)")
print(f"  Total = {S_total_ref:.2f}")

# Compute cutoff weights for each family
# The weight at each gap is the ratio of spectral action contributions
cutoff_weight_dict = {}
for name, fam in cutoff_families.items():
    S_c0 = fam['f0_scaled'] * a0_fold
    S_c2 = fam['f2_scaled'] * a2_fold
    S_c4 = fam['f4_scaled'] * a4_fold
    S_c_total = S_c0 + S_c2 + S_c4

    # Weight ratio: this cutoff family vs reference
    ratio = S_c_total / S_total_ref

    # The weight at each gap is the same (bulk approximation)
    cutoff_weight_dict[name] = np.ones(N_gaps) * ratio

    print(f"  {name:10s}: f0*a0={S_c0:.2f}, f2*a2={S_c2:.2f}, f4*a4={S_c4:.2f}, "
          f"total={S_c_total:.2f}, ratio={ratio:.6f}")

# =============================================================================
# SECTION 6: Compute |beta_proj|^2 for all cutoffs, both architectures
# =============================================================================
print("\n--- Section 6: Bogoliubov computation ---")

results = {}

for name, fam in cutoff_families.items():
    weights = cutoff_weight_dict[name]

    # Sequential tunneling
    P_seq, P_seq_per = compute_bogoliubov_sequential(
        tight_gaps, bandwidths_per_gap, weights)

    # Parallel channels
    P_par, P_par_per = compute_bogoliubov_parallel(
        tight_gaps, bandwidths_per_gap, weights)

    # The physically relevant quantity is:
    # |beta_proj|^2 = (1 - P_transmission) for reflection
    # But for the TRANSFER function, we want the TRANSMITTED amplitude:
    # |beta_proj|^2 = P_transmission (what reaches 4D)
    #
    # Actually, in the Bogoliubov framework:
    # alpha = transmitted, beta = reflected (pair-created)
    # |alpha|^2 - |beta|^2 = 1
    # The 4D projection picks up the transmitted amplitude.
    # So |beta_proj|^2 = P_transmission = product of |alpha_j|^2

    beta_seq = P_seq
    beta_par = P_par

    results[name] = {
        'P_seq': P_seq,
        'P_par': P_par,
        'P_seq_per': P_seq_per,
        'P_par_per': P_par_per,
        'beta_seq': beta_seq,
        'beta_par': beta_par,
    }

    print(f"\n  {name} cutoff:")
    print(f"    Sequential: P_trans = {P_seq:.6e}, log10 = {np.log10(P_seq) if P_seq > 0 else -np.inf:.4f}")
    print(f"    Parallel:   P_trans = {P_par:.6e}, log10 = {np.log10(P_par) if P_par > 0 else -np.inf:.4f}")
    print(f"    Per-gap transmissions (sequential):")
    for j in range(N_gaps):
        print(f"      Gap {j+1:2d}: Delta={tight_gaps[j]:.4f}, P={P_seq_per[j]:.6e}")

# =============================================================================
# SECTION 7: Peter-Weyl selection factor
# =============================================================================
print("\n--- Section 7: Peter-Weyl selection ---")

# The (0,0) sector is the only SU(3) singlet. Its multiplicity is dim(0,0)^2 = 1.
# The total number of D_K eigenvalues at L_max=10 is 155,984.
# But this counts WITH multiplicities. The number of DISTINCT representations
# that appear is much smaller.
#
# The Peter-Weyl selection factor for 4D projection:
# Only (0,0) modes couple to the 4D scalar metric perturbation,
# because the metric lives in the trivial representation of SU(3).
#
# Factor_PW = dim(0,0)^2 / sum_{(p,q)} dim(p,q)^2 = 1 / N_total_eigenvalues
# But this is already encoded in S_occ_(0,0) / S_occ_total.

# From S64 occ_spec data:
frac_PW = S_occ_00 / S_occ_total
N_singlet_modes = len(omega_00)

print(f"(0,0) sector:")
print(f"  N_singlet_modes = {N_singlet_modes}")
print(f"  S_occ_(0,0) = {S_occ_00:.6f}")
print(f"  S_occ_total = {S_occ_total:.4f}")
print(f"  Peter-Weyl fraction = S_occ_(0,0)/S_occ = {frac_PW:.6e}")
print(f"  log10(PW fraction) = {np.log10(frac_PW):.4f}")

# Additional: fraction of S_fold
frac_fold = S_occ_00 / S_fold
print(f"  S_occ_(0,0) / S_fold = {frac_fold:.6e} (log10 = {np.log10(frac_fold):.4f})")

# The mean v^2 factor further suppresses:
# v^2 = sin^2(theta_BCS) where theta is the BCS mixing angle
# For (0,0) modes near the gap: v^2 ~ 0.43 (significant mixing)
print(f"  <v^2>_(0,0) = {v2_mean_00:.6f}")

# =============================================================================
# SECTION 8: Total |beta_proj|^2 and A_s suppression
# =============================================================================
print("\n--- Section 8: Total transfer function ---")

# The TOTAL transfer function combines:
# 1. Peter-Weyl selection: only (0,0) modes project to 4D scalars
# 2. Bogoliubov transformation: tunneling through hybridization gaps
#
# IMPORTANT: S_occ already includes v^2 weighting (BCS occupation).
# S_occ_00 = sum_j v^2_j * |lambda_j| * dim(0,0)^2 for (0,0) sector.
# Do NOT multiply by v^2 again -- that would double-count.
#
# |beta_proj|^2_total = frac_PW * P_transmission
#   where frac_PW = S_occ_(0,0) / S_occ already encodes v^2
#
# For the A_s prediction:
#   A_s^predicted = S_occ * (M_KK/M_Pl)^4 * frac_PW * P_trans / A_s_CMB
#
# The ratio A_s^predicted / A_s^observed gives the "A_s gap" in OOM.

print("\nTotal |beta_proj|^2 for each cutoff (sequential architecture):")
print(f"  NOTE: v^2 already folded into S_occ and frac_PW -- not applied separately")
print(f"  {'Cutoff':10s} {'P_trans':>12s} {'frac_PW':>12s} "
      f"{'|beta|^2':>14s} {'log10':>8s}")

beta_total = {}
for name in cutoff_families:
    P_trans = results[name]['P_seq']
    beta2 = frac_PW * P_trans  # NO v2 factor -- already in S_occ_00/S_occ
    beta_total[name] = beta2
    log_beta = np.log10(beta2) if beta2 > 0 else -np.inf
    print(f"  {name:10s} {P_trans:12.6e} {frac_PW:12.6e} "
          f"{beta2:14.6e} {log_beta:8.4f}")

# Also compute for parallel architecture
print("\nTotal |beta_proj|^2 for each cutoff (parallel architecture):")
print(f"  {'Cutoff':10s} {'P_trans':>12s} {'frac_PW':>12s} "
      f"{'|beta|^2':>14s} {'log10':>8s}")

beta_total_par = {}
for name in cutoff_families:
    P_trans = results[name]['P_par']
    beta2 = frac_PW * P_trans  # NO v2 factor -- already in S_occ_00/S_occ
    beta_total_par[name] = beta2
    log_beta = np.log10(beta2) if beta2 > 0 else -np.inf
    print(f"  {name:10s} {P_trans:12.6e} {frac_PW:12.6e} "
          f"{beta2:14.6e} {log_beta:8.4f}")

# =============================================================================
# SECTION 9: Cutoff sensitivity test (gate criterion)
# =============================================================================
print("\n--- Section 9: Cutoff sensitivity (gate criterion) ---")

# Compute max/min ratio across cutoffs
betas_seq = np.array([beta_total[n] for n in cutoff_families])
betas_par = np.array([beta_total_par[n] for n in cutoff_families])

ratio_seq = betas_seq.max() / betas_seq.min() if betas_seq.min() > 0 else np.inf
ratio_par = betas_par.max() / betas_par.min() if betas_par.min() > 0 else np.inf

print(f"Sequential architecture:")
print(f"  |beta|^2 values: {betas_seq}")
print(f"  Max/min ratio: {ratio_seq:.6f}")

print(f"\nParallel architecture:")
print(f"  |beta|^2 values: {betas_par}")
print(f"  Max/min ratio: {ratio_par:.6f}")

# The gate tests BOTH architectures
ratio_max = max(ratio_seq, ratio_par)
print(f"\nMaximum ratio across both architectures: {ratio_max:.6f}")

# =============================================================================
# SECTION 10: A_s gap computation
# =============================================================================
print("\n--- Section 10: A_s gap ---")

# The A_s "gap" is the difference between predicted and observed in OOM:
#   gap = log10(A_s^predicted / A_s^observed)
#
# A_s^predicted = (framework spectral action perturbation in 4D)
# A_s^observed = 2.1e-9 (Planck 2018)
#
# From S64 occ_spec: the full-spectrum A_s gap (without transfer function) is:
#   gap_occ = 6.89 OOM (S_occ / S_fold * M_KK^4 / A_s)
#
# The transfer function provides additional suppression:
#   gap_reduced = gap_occ + log10(|beta_proj|^2_additional)
#
# But wait: S_occ already accounts for v^2 and Peter-Weyl multiplicities.
# The transfer function is the ADDITIONAL suppression from hybridization.

# The OCC-SPEC-64 gap is computed as:
# A_s_pred = S_occ * (M_KK/Lambda_cutoff)^4 where (M_KK/Lambda_cutoff)^4 = R^4
# We need the gap from the (0,0) sector ALONE reaching 4D.

# From the workshop (E3): ~8.7 OOM total suppression (4.8 from gaps + 3.9 from PW)
# Let's compute explicitly.

# The (0,0) sector spectral weight reaching 4D:
# S_4D = S_occ_(0,0) * P_transmission (gap suppression)
# A_s proportional to S_4D / S_fold (perturbation fraction)

# Using Gaussian cutoff (reference) with sequential architecture:
P_trans_ref = results['Gaussian']['P_seq']
S_4D = S_occ_00 * P_trans_ref

# The A_s gap in orders of magnitude:
# Original gap (from full S_fold): ~8.0 OOM
# S_occ reduction: log10(S_occ/S_fold) = log10(0.0753) = -1.12 OOM
# (0,0) selection: log10(S_occ_00/S_occ) = log10(3.19e-4) = -3.50 OOM
# Gap suppression: log10(P_trans) = ?

gap_from_PW = np.log10(S_occ_00 / S_occ_total)
gap_from_occ = np.log10(S_occ_total / S_fold)
gap_from_gaps = np.log10(P_trans_ref) if P_trans_ref > 0 else -np.inf
# v^2 is ALREADY inside S_occ (and S_occ_00). Do not count separately.
# The ratio S_occ/S_fold already encodes the v^2 suppression.
# The ratio S_occ_00/S_occ encodes the PW + v^2-differential selection.

print(f"A_s gap decomposition (Gaussian cutoff, sequential):")
print(f"  NOTE: v^2 already inside S_occ. Not counted separately.")
print(f"  S_occ / S_fold:        {S_occ_total/S_fold:.6e}  (log10 = {gap_from_occ:.4f} OOM)")
print(f"    [includes v^2 weighting on all sectors]")
print(f"  S_occ_00 / S_occ:      {S_occ_00/S_occ_total:.6e}  (log10 = {gap_from_PW:.4f} OOM)")
print(f"    [includes (0,0) sector v^2 relative to mean]")
print(f"  Gap tunneling P_trans: {P_trans_ref:.6e}  (log10 = {gap_from_gaps:.4f} OOM)")
print(f"  ---------------------------------------------------------------")
total_suppression_log = gap_from_occ + gap_from_PW + gap_from_gaps
print(f"  Total suppression:     10^({total_suppression_log:.4f})")
print(f"  = {10**total_suppression_log:.6e}")

# The original A_s gap from S_fold:
# A_s_pred_raw ~ S_fold * (M_KK)^4 / Normalization
# We don't have the absolute normalization, but we can compute the
# REDUCTION of the gap from the transfer function.

# From S64 occ_spec: gap_occ = 6.89 OOM (relative to A_s_CMB)
gap_occ_orig = float(d64['gap_occ'])
gap_full_orig = float(d64['gap_full'])

# The transfer function reduces the gap by:
gap_reduction_from_transfer = -(gap_from_PW + gap_from_gaps)
# Note: gap_from_occ is already in gap_occ

print(f"\nA_s gap summary:")
print(f"  Original gap (S_fold basis): {gap_full_orig:.4f} OOM")
print(f"  Gap after occ weighting:     {gap_occ_orig:.4f} OOM")
print(f"  Additional PW selection:     {gap_from_PW:.4f} OOM (v^2 already inside S_occ)")
print(f"  Additional gap tunneling:    {gap_from_gaps:.4f} OOM")
print(f"  ---------------------------------------------------------------")
gap_revised = gap_occ_orig + gap_from_PW + gap_from_gaps
print(f"  Revised A_s gap:             {gap_revised:.4f} OOM")

# Cross-check: direct from S_4D
# If A_s_pred = S_4D * constant, and A_s_obs = 2.1e-9,
# then gap = log10(S_4D / S_fold * something)
print(f"\n  Cross-check: S_4D = S_occ_00 * P_trans = {S_4D:.6f}")
print(f"  log10(S_4D / S_fold) = {np.log10(S_4D / S_fold):.4f}")
print(f"  This is the combined occ+PW+gap suppression from S_fold: "
      f"{np.log10(S_4D / S_fold):.4f} OOM")

# =============================================================================
# SECTION 11: Sensitivity analysis — gap parameter variations
# =============================================================================
print("\n--- Section 11: Sensitivity analysis ---")

# Vary the bandwidth by factors to test robustness
bw_factors = [0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0]
print(f"\nBandwidth variation (Gaussian cutoff):")
print(f"  {'BW factor':>10s} {'P_trans_seq':>14s} {'P_trans_par':>14s} "
      f"{'log10_seq':>10s} {'log10_par':>10s}")

P_trans_bw_seq = []
P_trans_bw_par = []
for bwf in bw_factors:
    bw_test = bandwidths_per_gap * bwf
    P_s, _ = compute_bogoliubov_sequential(tight_gaps, bw_test)
    P_p, _ = compute_bogoliubov_parallel(tight_gaps, bw_test)
    P_trans_bw_seq.append(P_s)
    P_trans_bw_par.append(P_p)
    log_s = np.log10(P_s) if P_s > 0 else -np.inf
    log_p = np.log10(P_p) if P_p > 0 else -np.inf
    print(f"  {bwf:10.2f} {P_s:14.6e} {P_p:14.6e} {log_s:10.4f} {log_p:10.4f}")

# Vary number of gaps (subset analysis)
print(f"\nGap count variation (Gaussian cutoff, sequential):")
print(f"  {'N_gaps':>8s} {'P_trans':>14s} {'log10':>10s}")
for ng in range(1, N_gaps+1):
    P_s, _ = compute_bogoliubov_sequential(tight_gaps[:ng], bandwidths_per_gap[:ng])
    log_s = np.log10(P_s) if P_s > 0 else -np.inf
    print(f"  {ng:8d} {P_s:14.6e} {log_s:10.4f}")

# =============================================================================
# SECTION 12: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE: TRANSFER-BOGOLIUBOV-64")
print("=" * 78)

# Compute the max variation across cutoff families
# For sequential:
log_betas_seq = np.array([np.log10(beta_total[n]) if beta_total[n] > 0 else -300
                          for n in cutoff_families])
log_betas_par = np.array([np.log10(beta_total_par[n]) if beta_total_par[n] > 0 else -300
                          for n in cutoff_families])

# The variation in OOM:
spread_seq = log_betas_seq.max() - log_betas_seq.min()
spread_par = log_betas_par.max() - log_betas_par.min()

# In linear ratio:
print(f"\n  Sequential architecture:")
print(f"    |beta|^2 across cutoffs: {[f'{beta_total[n]:.4e}' for n in cutoff_families]}")
print(f"    log10 values: {log_betas_seq}")
print(f"    Max/min ratio: {ratio_seq:.6f}")
print(f"    Spread (OOM): {spread_seq:.6f}")

print(f"\n  Parallel architecture:")
print(f"    |beta|^2 across cutoffs: {[f'{beta_total_par[n]:.4e}' for n in cutoff_families]}")
print(f"    log10 values: {log_betas_par}")
print(f"    Max/min ratio: {ratio_par:.6f}")
print(f"    Spread (OOM): {spread_par:.6f}")

# Gate criterion
# PASS: max variation < factor 2 across cutoffs
# FAIL: max variation > factor 10
if ratio_max < 2.0:
    verdict = "PASS"
    detail = (f"|beta_proj|^2 varies by factor {ratio_max:.4f} across 3 cutoff families "
              f"(< 2.0 threshold). Trans-Planckian universality CONFIRMED for the "
              f"A_s transfer function. Sequential: spread = {spread_seq:.4f} OOM, "
              f"Parallel: spread = {spread_par:.4f} OOM.")
elif ratio_max > 10.0:
    verdict = "FAIL"
    detail = (f"|beta_proj|^2 varies by factor {ratio_max:.4f} across 3 cutoff families "
              f"(> 10.0 threshold). Transfer function is CUTOFF-SENSITIVE.")
else:
    verdict = "INFO"
    detail = (f"|beta_proj|^2 varies by factor {ratio_max:.4f} across 3 cutoff families "
              f"(between 2.0 and 10.0). Marginal cutoff sensitivity.")

print(f"\n  VERDICT: {verdict}")
print(f"  {detail}")

print(f"\n  Key results:")
print(f"    |beta_proj|^2 (Gaussian, sequential) = {beta_total['Gaussian']:.6e}")
print(f"    log10(|beta_proj|^2) = {np.log10(beta_total['Gaussian']):.4f}")
print(f"    Suppression decomposition (v^2 inside S_occ, not separate):")
print(f"      PW selection (incl. v^2): {gap_from_PW:.4f} OOM")
print(f"      Gap tunneling:            {gap_from_gaps:.4f} OOM")
print(f"      Total additional (beyond gap_occ): {gap_from_PW + gap_from_gaps:.4f} OOM")
print(f"    A_s gap (revised): {gap_revised:.4f} OOM (from {gap_occ_orig:.4f} before transfer)")

# =============================================================================
# SECTION 13: Save data
# =============================================================================
print("\n--- Section 13: Save data ---")

np.savez(OUT_NPZ,
    # Gap data
    tight_gaps=tight_gaps,
    tight_deltas=tight_deltas,
    tight_detunings=tight_detunings,
    bandwidths=bandwidths_per_gap,
    N_gaps=N_gaps,

    # (0,0) sector
    omega_00=omega_00,
    v2_00=v2_00,
    S_occ_00=S_occ_00,
    S_occ_total=S_occ_total,
    frac_PW=frac_PW,
    v2_mean_00=v2_mean_00,

    # Bogoliubov results per cutoff (sequential)
    beta_Gaussian_seq=beta_total['Gaussian'],
    beta_Sharp_seq=beta_total['Sharp'],
    beta_Zeta_seq=beta_total['Zeta_s4'],

    # Bogoliubov results per cutoff (parallel)
    beta_Gaussian_par=beta_total_par['Gaussian'],
    beta_Sharp_par=beta_total_par['Sharp'],
    beta_Zeta_par=beta_total_par['Zeta_s4'],

    # Transmission per gap (Gaussian reference)
    P_trans_per_gap_Gaussian=results['Gaussian']['P_seq_per'],

    # Cutoff sensitivity
    ratio_seq=ratio_seq,
    ratio_par=ratio_par,
    ratio_max=ratio_max,

    # A_s gap (v^2 inside S_occ, not separate)
    gap_from_PW=gap_from_PW,
    gap_from_gaps=gap_from_gaps,
    gap_occ_orig=gap_occ_orig,
    gap_revised=gap_revised,
    total_suppression_log=total_suppression_log,

    # Sensitivity analysis
    bw_factors=np.array(bw_factors),
    P_trans_bw_seq=np.array(P_trans_bw_seq),
    P_trans_bw_par=np.array(P_trans_bw_par),

    # Cutoff moments
    f0=f0, f2=f2, f4=f4,

    # Gate
    gate_name='TRANSFER-BOGOLIUBOV-64',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 14: Plotting
# =============================================================================
print("\n--- Section 14: Plotting ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: Hybridization gaps
ax1 = fig.add_subplot(gs[0, 0])
x_gaps = np.arange(1, N_gaps + 1)
ax1.bar(x_gaps, tight_gaps, color='steelblue', alpha=0.8, label='Coupled gap')
ax1.bar(x_gaps, np.maximum(tight_deltas, 0), color='orange', alpha=0.6, label='Delta gap')
ax1.set_xlabel('Gap index (sorted by size)')
ax1.set_ylabel('Gap width (M_KK)')
ax1.set_title(f'{N_gaps} Hybridization Gaps')
ax1.legend(fontsize=8)
ax1.set_yscale('log')

# Panel 2: Per-gap transmission (Gaussian)
ax2 = fig.add_subplot(gs[0, 1])
P_per = results['Gaussian']['P_seq_per']
ax2.bar(x_gaps, P_per, color='forestgreen', alpha=0.8)
ax2.set_xlabel('Gap index')
ax2.set_ylabel('Transmission |alpha_j|^2')
ax2.set_title('Per-Gap Transmission (Gaussian)')
ax2.set_yscale('log')

# Panel 3: Cutoff comparison
ax3 = fig.add_subplot(gs[0, 2])
cutoff_names = list(cutoff_families.keys())
x_cut = np.arange(len(cutoff_names))
vals_seq = [beta_total[n] for n in cutoff_names]
vals_par = [beta_total_par[n] for n in cutoff_names]
width = 0.35  # (local)
ax3.bar(x_cut - width/2, vals_seq, width, label='Sequential', color='steelblue', alpha=0.8)
ax3.bar(x_cut + width/2, vals_par, width, label='Parallel', color='coral', alpha=0.8)
ax3.set_xticks(x_cut)
ax3.set_xticklabels(cutoff_names, fontsize=8)
ax3.set_ylabel('|beta_proj|^2')
ax3.set_title(f'Cutoff Sensitivity (ratio={ratio_max:.2f})')
ax3.set_yscale('log')
ax3.legend(fontsize=8)

# Panel 4: Bandwidth sensitivity
ax4 = fig.add_subplot(gs[1, 0])
ax4.semilogy(bw_factors, P_trans_bw_seq, 'o-', color='steelblue', label='Sequential')
ax4.semilogy(bw_factors, P_trans_bw_par, 's-', color='coral', label='Parallel')
ax4.axvline(1.0, color='gray', linestyle='--', alpha=0.5, label='Reference')
ax4.set_xlabel('Bandwidth factor')
ax4.set_ylabel('P_transmission')
ax4.set_title('Bandwidth Sensitivity')
ax4.legend(fontsize=8)

# Panel 5: A_s gap decomposition (waterfall)
ax5 = fig.add_subplot(gs[1, 1])
labels = ['S_occ/S_fold\n(incl. v^2)', 'PW select.\n(incl. v^2)', 'Gap tunnel.']
values = [gap_from_occ, gap_from_PW, gap_from_gaps]
cumulative = [gap_full_orig]
for v in values:
    cumulative.append(cumulative[-1] + v)
colors = ['#4e79a7', '#f28e2b', '#76b7b2']
for i in range(len(labels)):
    ax5.barh(i, values[i], left=cumulative[i], color=colors[i], alpha=0.8, height=0.6)
    ax5.text(cumulative[i] + values[i]/2, i, f'{values[i]:.2f}',
             ha='center', va='center', fontsize=8, fontweight='bold')
ax5.set_yticks(range(len(labels)))
ax5.set_yticklabels(labels, fontsize=9)
ax5.set_xlabel('log10 suppression (OOM)')
ax5.set_title(f'A_s Gap: {gap_full_orig:.2f} -> {gap_revised:.2f} OOM')
ax5.axvline(0, color='gray', linestyle='-', alpha=0.3)

# Panel 6: Summary text
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary_text = (
    f"TRANSFER-BOGOLIUBOV-64\n"
    f"Verdict: {verdict}\n\n"
    f"|beta_proj|^2 (Gaussian):\n"
    f"  Sequential: {beta_total['Gaussian']:.4e}\n"
    f"  Parallel:   {beta_total_par['Gaussian']:.4e}\n\n"
    f"Cutoff variation:\n"
    f"  Max ratio: {ratio_max:.4f}\n"
    f"  Spread: {max(spread_seq, spread_par):.4f} OOM\n\n"
    f"Suppression (v^2 in S_occ):\n"
    f"  PW selection:  {gap_from_PW:.2f} OOM\n"
    f"  Gap tunneling: {gap_from_gaps:.2f} OOM\n\n"
    f"A_s gap: {gap_occ_orig:.2f} -> {gap_revised:.2f} OOM"
)
ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         verticalalignment='top', fontfamily='monospace', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('S64 Transfer Function: Bogoliubov Projection through Hybridization Gaps',
             fontsize=13, fontweight='bold')
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

t_end = time.time()
print(f"\n{'='*78}")
print(f"COMPUTATION COMPLETE")
print(f"  Time: {t_end - t_start:.1f} s")
print(f"  Gaps: {N_gaps}")
print(f"  Cutoffs: {len(cutoff_families)}")
print(f"  |beta_proj|^2 = {beta_total['Gaussian']:.4e} (Gaussian, sequential)")
print(f"  A_s gap revised: {gap_revised:.4f} OOM")
print(f"  VERDICT: {verdict}")
print(f"{'='*78}")
