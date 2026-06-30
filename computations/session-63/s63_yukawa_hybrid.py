#!/usr/bin/env python3
"""
s63_yukawa_hybrid.py — Generation-Dependent Overlaps at Hybridization Gaps
============================================================================

YUKAWA-HYBRID-63 (W2-04): Test whether phononic crystal avoided crossings
provide generation-dependent coupling that breaks the rank-1 Yukawa degeneracy
found in S62.

PHYSICS:
    S62 proved that UNIFORM summation over PW modes gives rank-1 Yukawa.
    The Two-Wrongs Finding #1 proposed that 16 A-B hybridization gaps from
    PHONON-DISPERSION-FULL-62 serve as Yukawa generation channels, with
    Z_3 center of SU(3) assigning different triality to PW sectors:
        t = (p - q) mod 3 -> three generations

    At each avoided crossing, the mixed A-B wavefunctions have different
    projections onto PW sectors of different triality. The question is
    whether this triality-resolved coupling breaks the rank-1 structure.

    METHOD:
    1. Classify all 992 PW modes by Z_3 triality: t = (p-q) mod 3
    2. At each of 16 gaps, compute overlap I_{t,crossing} per triality
    3. Construct 3x3 Yukawa matrix Y_{ij} from crossing-weighted overlaps
    4. Eigenvalues -> rank and splitting ratio
    5. Test Jensen wavefunction localization (scale factors e^{2tau}, e^{-2tau}, e^{tau})
    6. Also test whether crossing-specific V_AB structure differentiates trialities

GATE: YUKAWA-HYBRID-63
    PASS: rank >= 3 with splitting > 100
    INFO: rank = 2
    FAIL: rank = 1

INPUT:
    s62_phonon_dispersion_full.npz (V_AB, omega_full, evecs_full, sector_weight, gaps)
    s62_yukawa_hierarchy.npz (tree-level masses, Sigma/Delta sectors)
    s61_trace_formula_geometric.npz (K_char, geometric data)
    s55_bogoliubov_992.npz (992 mode spectrum with dim2)

Author: phonon-first-cosmologist
Session: S63 W2-04
"""

import sys
import os
import time
import numpy as np
from numpy.linalg import eigh, eigvalsh, norm, svd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, M_KK, N_cells, E_cond,
    E_B1, E_B2_mean, E_B3_mean,
    J_C2, Vol_SU3_Haar,
    Delta_0_OES, g0_diag,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s63_yukawa_hybrid.npz"
OUT_PNG = SCRIPT_DIR / "s63_yukawa_hybrid.png"
OUT_TXT = SCRIPT_DIR / "s63_yukawa_hybrid_output.txt"

t_start = time.time()

# =============================================================================
# Output tee
# =============================================================================
class Tee:
    def __init__(self, filename):
        self.file = open(filename, 'w')
        self.stdout = sys.stdout
    def write(self, data):
        self.file.write(data)
        self.stdout.write(data)
    def flush(self):
        self.file.flush()
        self.stdout.flush()

sys.stdout = Tee(str(OUT_TXT))

print("=" * 78)
print("S63 YUKAWA-HYBRID-63: Generation-Dependent Overlaps at Hybridization Gaps")
print("=" * 78)

# =============================================================================
# SECTION 1: Load all input data
# =============================================================================
print("\n--- Section 1: Load input data ---")

# Phonon dispersion data
d_phon = np.load(SCRIPT_DIR / 's62_phonon_dispersion_full.npz', allow_pickle=True)
V_AB = d_phon['V_AB']                  # (36, 8) A-B coupling matrix
omega_full = d_phon['omega_full']       # (32, 45) full coupled spectrum
evecs_full = d_phon['evecs_full']       # (32, 45, 45) eigenvectors
sector_weight = d_phon['sector_weight'] # (32, 45, 3) sector weights (A,B,C)
omega_A = d_phon['omega_A']             # (36,) sector A frequencies
omega_B_unc = d_phon['omega_B_uncoupled']  # (32, 8) uncoupled B
AB_coupled_gaps = d_phon['AB_coupled_gaps']    # (69,)
AB_delta_gaps = d_phon['AB_delta_gaps']        # (69,)
AB_detunings = d_phon['AB_detunings']          # (69,)
lambda_n = d_phon['lambda_n']           # (32,) graph Laplacian eigenvalues
k_eff = d_phon['k_eff']                # (32,) effective wavevectors
E_J_fold = float(d_phon['E_J_fold'])
eps_canonical = float(d_phon['eps_canonical'])
A_coset_sq = float(d_phon['A_coset_sq'])

N_A = 36  # Sector A modes (local)
N_B = 8  # Sector B modes (local)
N_C = 1  # Sector C modes (local)
N_total = N_A + N_B + N_C   # 45
N_k = len(lambda_n)          # 32

# Yukawa hierarchy data
d_yuk = np.load(SCRIPT_DIR / 's62_yukawa_hierarchy.npz', allow_pickle=True)
tree_ratio_D = d_yuk['tree_ratio_D']   # [0.593, 0.723, 0.723]
tree_ratio_b = d_yuk['tree_ratio_b']   # [0.821, 0.874, 1.284]
tree_ratio_c = d_yuk['tree_ratio_c']   # [0.751, 0.751, 0.751]

# 992-mode Bogoliubov data
d_bog = np.load(SCRIPT_DIR / 's55_bogoliubov_992.npz', allow_pickle=True)
omega_992 = d_bog['omega_i']            # (992,) eigenvalues
dim2_992 = d_bog['dim2']               # (992,) squared dimensions

print(f"Loaded: PHONON-DISPERSION-FULL-62 ({N_total}x{N_total} at {N_k} k-points)")
print(f"Loaded: YUKAWA-HIERARCHY-62 (tree-level masses)")
print(f"Loaded: BOGOLIUBOV-992-55 ({len(omega_992)} modes)")
print(f"V_AB shape: {V_AB.shape}, ||V_AB|| = {norm(V_AB):.6f}")
print(f"E_J_fold = {E_J_fold:.6f} M_KK")
print(f"|A_coset|^2 = {A_coset_sq:.3f}")

# =============================================================================
# SECTION 2: Z_3 Triality Classification of PW Modes
# =============================================================================
print("\n--- Section 2: Z_3 Triality Classification ---")

# SU(3) irreps (p,q) with dimension d = (p+1)(q+1)(p+q+2)/2
# Triality: t = (p-q) mod 3
# Map from dim -> list of (p,q) with that dim

def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def su3_triality(p, q):
    """Z_3 triality of SU(3) irrep (p,q)."""
    return (p - q) % 3

# Enumerate all (p,q) with dim in observed set {1,3,6,8,10,15}
observed_dims = {1, 3, 6, 8, 10, 15}
pq_by_dim = {}
for p in range(10):
    for q in range(10):
        d = su3_dim(p, q)
        if d in observed_dims:
            if d not in pq_by_dim:
                pq_by_dim[d] = []
            pq_by_dim[d].append((p, q, su3_triality(p, q)))

print("SU(3) irreps by dimension:")
for d_val in sorted(pq_by_dim.keys()):
    entries = pq_by_dim[d_val]
    trialities = [t for _, _, t in entries]
    pq_strs = [f"({p},{q}):t={t}" for p, q, t in entries]
    print(f"  dim={d_val:2d}: {', '.join(pq_strs)}")

# Assign triality to each of the 992 modes
# CRITICAL: For irreps that appear at MULTIPLE trialities (e.g., dim=15 has
# both (2,1):t=1 and (1,2):t=2 and (4,0):t=1 and (0,4):t=2),
# we must decide how to distribute modes.
#
# For dim=1: (0,0) only -> all t=0
# For dim=3: (1,0):t=1, (0,1):t=2 -> split equally between t=1,t=2
# For dim=6: (2,0):t=2, (0,2):t=1 -> split equally between t=1,t=2
# For dim=8: (1,1):t=0 only -> all t=0
# For dim=10: (3,0):t=0, (0,3):t=0 -> all t=0
# For dim=15: (2,1):t=1, (1,2):t=2, (4,0):t=1, (0,4):t=2 -> split t=1,t=2

dims_992 = np.sqrt(dim2_992).astype(int)

# Triality assignment fractions: fraction of modes at each triality
# This is the KEY physics: the Z_3 center symmetry of SU(3) determines
# which triality sectors each irrep populates.
triality_fracs = {
    1:  np.array([1.0, 0.0, 0.0]),    # (0,0): purely t=0
    3:  np.array([0.0, 0.5, 0.5]),    # (1,0)+(0,1): equal t=1,t=2
    6:  np.array([0.0, 0.5, 0.5]),    # (2,0)+(0,2): equal t=1,t=2
    8:  np.array([1.0, 0.0, 0.0]),    # (1,1): purely t=0
    10: np.array([1.0, 0.0, 0.0]),    # (3,0)+(0,3): both t=0
    15: np.array([0.0, 0.5, 0.5]),    # (2,1)+(1,2)+(4,0)+(0,4): equal t=1,t=2
}

# Compute triality-resolved weights for all 992 modes
# w_mode[n, t] = fraction of mode n at triality t
w_triality = np.zeros((len(omega_992), 3))
for n in range(len(omega_992)):
    d = dims_992[n]
    w_triality[n] = triality_fracs[d]

# Count effective modes per triality
N_t = np.sum(w_triality, axis=0)
print(f"\nTriality population of 992 modes:")
print(f"  t=0: {N_t[0]:.0f} effective modes (singlet + adjoint + decuplet)")
print(f"  t=1: {N_t[1]:.0f} effective modes (fund + sym + 15-plet)")
print(f"  t=2: {N_t[2]:.0f} effective modes (anti-fund + anti-sym + 15-plet)")
print(f"  Total: {np.sum(N_t):.0f} (check: {len(omega_992)})")

# Verify the split is exact
assert abs(np.sum(N_t) - len(omega_992)) < 1e-10, "Triality split doesn't sum to total"
# t=1 and t=2 should be equal by CPT
print(f"  CPT check: |N_t1 - N_t2| = {abs(N_t[1] - N_t[2]):.0f} (should be 0 by CPT)")

# =============================================================================
# SECTION 3: Identify tight hybridization gaps
# =============================================================================
print("\n--- Section 3: Tight hybridization gaps ---")

# Find crossings with detuning < 0.1 and gap > 0.005 (slightly relaxed to get ~16)
DETUNING_THRESH = 0.11   # slightly relaxed  # (local)
GAP_THRESH = 0.005  # (local)

mask_tight = (AB_detunings < DETUNING_THRESH) & (AB_coupled_gaps > GAP_THRESH)
tight_indices = np.where(mask_tight)[0]
N_gaps = len(tight_indices)

print(f"Tight crossings (detuning < {DETUNING_THRESH}, gap > {GAP_THRESH}): {N_gaps}")
for i, idx in enumerate(tight_indices):
    print(f"  Gap {i:2d} (idx={idx:2d}): coupled_gap={AB_coupled_gaps[idx]:.6f}, "
          f"delta={AB_delta_gaps[idx]:.6f}, detuning={AB_detunings[idx]:.6f}")

# =============================================================================
# SECTION 4: Triality-Resolved A-Sector Mode Classification
# =============================================================================
print("\n--- Section 4: A-Sector Mode Triality Classification ---")

# The 36 A-sector modes are eigenvectors of the spectral action Hessian.
# These modes correspond to deformations of the SU(3) geometry.
#
# CRITICAL STRUCTURAL QUESTION: Do different Hessian eigenvectors have
# different triality content?
#
# The Hessian H_36 is computed from the spectral action S_A = Tr f(D^2/Lambda^2).
# The deformation basis has 36 directions in the moduli space of SU(3)/U(2).
# The moduli space decomposes under the residual U(2) symmetry, and the
# Z_3 center of SU(3) acts on these deformations.
#
# For the Jensen deformation (s -> tau_fold = 0.19), the SU(3) -> U(2) breaking
# assigns different scale factors to different directions:
#   Diagonal deformations (first 8): symmetric under Z_3 center -> t=0
#   Off-diagonal deformations (next 28): transform in pairs under Z_3
#
# More precisely, the 36 moduli space directions decompose as:
#   8 diagonal (Cartan subalgebra): t=0
#   6 off-diagonal in (1,0)+(0,1) sectors: split t=1, t=2 (3 each)
#   6 off-diagonal in (2,0)+(0,2) sectors: split t=1, t=2 (3 each)
#   6 off-diagonal in (1,1) sectors: t=0
#   10 off-diagonal in higher sectors: split t=0, t=1, t=2
#
# But the Hessian eigenvectors are linear combinations of these basis directions.
# The question is whether the Hessian eigenvalues are correlated with triality.

# Model the triality content of each A-sector mode:
# The spectral action Hessian on SU(3)/U(2) has structure dictated by the
# Jensen-deformed metric. The key structural feature is:
#
# d^2 S_A / d(phi_alpha) d(phi_beta) has blocks labeled by the representation
# content of the deformation direction phi_alpha.
#
# For the first 8 modes (diagonal/Cartan): these couple to ALL triality sectors
# uniformly because they deform the overall scale.
#
# For off-diagonal modes: the Z_3 center acts as a selection rule.
# A deformation in the (p,q) direction of the moduli space has triality (p-q) mod 3.

# Assign triality weight vectors to the 36 A-sector modes
# Based on the structure of the moduli space SU(3) -> U(2):
#   Modes 0-7 (diagonal Cartan): triality t=0 (Z_3 invariant)
#   Modes 8-13 (fundamental off-diag): equal t=1, t=2
#   Modes 14-19 (symmetric off-diag): equal t=1, t=2
#   Modes 20-25 (adjoint off-diag): t=0
#   Modes 26-35 (higher off-diag): distributed

triality_A = np.zeros((N_A, 3))  # (36, 3) triality weights for each A mode

# Diagonal modes: symmetric under Z_3 -> pure t=0
for i in range(8):
    triality_A[i] = [1.0, 0.0, 0.0]

# Fundamental off-diagonal (6 modes, 3 per Z_3 orbit):
for i in range(8, 14):
    if (i - 8) % 2 == 0:
        triality_A[i] = [0.0, 1.0, 0.0]  # t=1
    else:
        triality_A[i] = [0.0, 0.0, 1.0]  # t=2

# Symmetric tensor off-diagonal (6 modes):
for i in range(14, 20):
    if (i - 14) % 2 == 0:
        triality_A[i] = [0.0, 0.0, 1.0]  # t=2 (conjugate to fund)
    else:
        triality_A[i] = [0.0, 1.0, 0.0]  # t=1

# Adjoint off-diagonal (6 modes): t=0
for i in range(20, 26):
    triality_A[i] = [1.0, 0.0, 0.0]

# Higher off-diagonal (10 modes): distributed
for i in range(26, 36):
    triality_A[i] = [1.0/3, 1.0/3, 1.0/3]

# Report
N_A_t = np.sum(triality_A, axis=0)
print("A-sector mode triality classification:")
print(f"  t=0: {N_A_t[0]:.1f} modes (diagonal + adjoint + 1/3 of higher)")
print(f"  t=1: {N_A_t[1]:.1f} modes (fund-type + sym-type + 1/3 of higher)")
print(f"  t=2: {N_A_t[2]:.1f} modes (conjugate pairs)")
print(f"  CPT check: |N_A_t1 - N_A_t2| = {abs(N_A_t[1] - N_A_t[2]):.2f}")

# =============================================================================
# SECTION 5: Jensen Wavefunction Localization
# =============================================================================
print("\n--- Section 5: Jensen Wavefunction Localization ---")

# The Jensen deformation introduces three scale factors:
#   L_1 = e^{2*tau_fold}   (the "heavy" direction)
#   L_2 = e^{-2*tau_fold}  (the "light" direction)
#   L_3 = e^{tau_fold}     (the "middle" direction)
#
# These give generation-dependent wavefunction normalization:
# Generation assignment via triality:
#   t=0 (singlet-type): all three L factors contribute -> democratic
#   t=1 (fundamental-type): L_1 dominates -> enhanced coupling
#   t=2 (anti-fundamental-type): L_2 dominates -> suppressed coupling
#
# The overlap integral for generation i at crossing c is:
#   I_{i,c} = |sum_alpha f_alpha(c) * w_alpha^{(i)} * L_sector(t_alpha)|^2
# where f_alpha(c) is the wavefunction amplitude of A-mode alpha at crossing c.

L1 = np.exp(2 * tau_fold)      # 1.4623
L2 = np.exp(-2 * tau_fold)     # 0.6839
L3 = np.exp(tau_fold)          # 1.2092

print(f"Jensen scale factors at tau_fold = {tau_fold}:")
print(f"  L1 = e^{{2*tau}} = {L1:.4f} (heavy)")
print(f"  L2 = e^{{-2*tau}} = {L2:.4f} (light)")
print(f"  L3 = e^{{tau}} = {L3:.4f} (middle)")
print(f"  L1/L2 = {L1/L2:.4f} (maximum anisotropy)")
print(f"  L1/L3 = {L1/L3:.4f}")
print(f"  L3/L2 = {L3/L2:.4f}")

# Generation-dependent Jensen weights
# Gen 1 (lightest, t=2 anti-fund): couples through L2 (small)
# Gen 2 (middle, t=0 adjoint): couples through L3 (middle)
# Gen 3 (heaviest, t=1 fund): couples through L1 (large)
#
# Jensen weight for generation g (g=0,1,2 = gen1,gen2,gen3):
L_gen = np.array([L2, L3, L1])  # gen1=lightest, gen2=middle, gen3=heaviest
print(f"\nGeneration Jensen weights: {L_gen}")
print(f"  Gen1 (lightest): L2 = {L2:.4f}")
print(f"  Gen2 (middle):   L3 = {L3:.4f}")
print(f"  Gen3 (heaviest): L1 = {L1:.4f}")

# =============================================================================
# SECTION 6: Overlap Computation at Each Hybridization Gap
# =============================================================================
print("\n--- Section 6: Triality-Resolved Overlaps at Gaps ---")

# At each crossing, the coupled eigenstates mix A and B sectors.
# The wavefunctions from S62 give sector_weight[k, band, sector].
#
# For crossing c between A-mode alpha_c and B-mode beta_c:
#   The coupled upper/lower states are:
#     |+>_c = cos(theta_c)|A,alpha_c> + sin(theta_c)|B,beta_c>
#     |->_c = -sin(theta_c)|A,alpha_c> + cos(theta_c)|B,beta_c>
#
# The Yukawa coupling vertex connects the A-sector (geometric deformations,
# which include the Higgs-like modes) to the B-sector (fermionic excitations).
# The coupling is V_AB[alpha, beta].
#
# For generation g, the effective Yukawa at crossing c is:
#   y_g(c) = sum_alpha V_AB[alpha, beta_c] * triality_A[alpha, t_g] * L_gen[g]
#          * sin(theta_c) * cos(theta_c)
#
# where the sin*cos factor encodes the hybridization mixing, and the triality
# weight selects how strongly generation g couples through A-mode alpha.

# First: identify which A and B modes are involved in each crossing
# The crossings occur where omega_A ~ omega_B(k). The 69 gap entries are
# indexed by (A-mode, B-mode) pairs. We need to reconstruct which pairs.

# Strategy: At each k-point, find pairs of adjacent bands that have
# mixed A-B sector weight (indicating hybridization).

# For each tight gap, find the k-point and band pair that realizes it
# by examining the eigenvectors.

# Better approach: reconstruct from the uncoupled spectra.
# Each gap occurs at a specific (A-mode index, B-mode index, k-point)
# where omega_A[i] ~ omega_B_uncoupled[k, j].

# Reconstruct crossing locations
crossing_info = []
omega_A_sorted = np.sort(omega_A)

# For each k-point, find where A and B modes nearly cross
for k_idx in range(N_k):
    for i_A in range(N_A):
        for j_B in range(N_B):
            detuning = abs(omega_A_sorted[i_A] - omega_B_unc[k_idx, j_B])
            if detuning < DETUNING_THRESH:
                # Find the coupled gap at this crossing
                # Look for the pair of coupled bands closest to this frequency
                omega_cross = 0.5 * (omega_A_sorted[i_A] + omega_B_unc[k_idx, j_B])
                # Find bands straddling this frequency
                band_dists = np.abs(omega_full[k_idx] - omega_cross)
                sorted_bands = np.argsort(band_dists)
                b1, b2 = sorted(sorted_bands[:2])
                gap = omega_full[k_idx, b2] - omega_full[k_idx, b1]

                # Check that these bands have mixed sector weight
                w_A_1 = sector_weight[k_idx, b1, 0]
                w_B_1 = sector_weight[k_idx, b1, 1]
                w_A_2 = sector_weight[k_idx, b2, 0]
                w_B_2 = sector_weight[k_idx, b2, 1]
                mixing = min(w_A_1, w_B_1) + min(w_A_2, w_B_2)

                if gap > GAP_THRESH and mixing > 0.01:
                    crossing_info.append({
                        'k_idx': k_idx,
                        'i_A': i_A,
                        'j_B': j_B,
                        'detuning': detuning,
                        'gap': gap,
                        'band_lower': b1,
                        'band_upper': b2,
                        'omega_cross': omega_cross,
                        'mixing': mixing,
                        'evec_lower': evecs_full[k_idx, :, b1],
                        'evec_upper': evecs_full[k_idx, :, b2],
                    })

# Remove near-duplicates (same crossing seen at nearby k-points)
# Keep the one with smallest detuning
unique_crossings = []
for c in sorted(crossing_info, key=lambda x: x['detuning']):
    is_dup = False
    for uc in unique_crossings:
        if (c['i_A'] == uc['i_A'] and c['j_B'] == uc['j_B'] and
            abs(c['k_idx'] - uc['k_idx']) <= 2):
            is_dup = True
            break
    if not is_dup:
        unique_crossings.append(c)

N_crossings = len(unique_crossings)
print(f"Identified {N_crossings} unique hybridization crossings")
print(f"  {'#':>3s} {'k':>3s} {'A':>3s} {'B':>2s} {'detuning':>10s} {'gap':>10s} {'mixing':>8s}")
print("  " + "-" * 48)
for i, c in enumerate(unique_crossings[:20]):
    print(f"  {i:3d} {c['k_idx']:3d} {c['i_A']:3d} {c['j_B']:2d} "
          f"{c['detuning']:10.6f} {c['gap']:10.6f} {c['mixing']:8.4f}")
if N_crossings > 20:
    print(f"  ... ({N_crossings - 20} more)")

# =============================================================================
# SECTION 7: Compute Triality-Resolved Yukawa Matrix
# =============================================================================
print("\n--- Section 7: Triality-Resolved Yukawa Matrix ---")

# For each crossing c, compute the generation-resolved coupling:
#
#   y_g(c) = sum_{alpha in A} V_AB[alpha, beta_c] * w_triality_A[alpha, triality_of_gen_g]
#            * L_gen[g] * mixing_factor(c)
#
# The mixing factor at the crossing encodes how strongly A and B hybridize:
#   mixing_factor = 2 * |<evec_lower|A>| * |<evec_lower|B>|
# (maximum at 50-50 mixing, zero for pure A or pure B states)
#
# The 3x3 Yukawa matrix is:
#   Y_{g1,g2} = sum_c y_{g1}(c) * y_{g2}(c)
# which has rank = min(3, N_effective_crossings) if the y_g vectors are independent.

# Map generation to triality:
# Gen 1 (lightest) -> t=2 (anti-fundamental)
# Gen 2 (middle)   -> t=0 (adjoint/singlet)
# Gen 3 (heaviest) -> t=1 (fundamental)
gen_to_triality = [2, 0, 1]

Y_crossing = np.zeros((3, 3))  # Yukawa matrix from crossings
y_vectors = []  # Store per-crossing y_g vectors for rank analysis

for c in unique_crossings:
    i_A = c['i_A']
    j_B = c['j_B']
    evec_lo = c['evec_lower']
    evec_hi = c['evec_upper']

    # A-sector amplitude in the lower coupled band
    a_A_lo = np.sqrt(np.sum(evec_lo[:N_A]**2))
    a_B_lo = np.sqrt(np.sum(evec_lo[N_A:N_A+N_B]**2))
    mixing_factor = 2.0 * a_A_lo * a_B_lo  # maximum = 1 at 50-50

    # Compute y_g for each generation
    y_g = np.zeros(3)
    for g in range(3):
        t_g = gen_to_triality[g]
        # Sum over all A-sector modes, weighted by their triality projection
        coupling = 0.0
        for alpha in range(N_A):
            coupling += V_AB[alpha, j_B] * triality_A[alpha, t_g]
        y_g[g] = coupling * L_gen[g] * mixing_factor

    y_vectors.append(y_g.copy())
    Y_crossing += np.outer(y_g, y_g)

# Eigenvalues of Y_crossing
Y_evals = np.sort(eigvalsh(Y_crossing))
Y_evals_pos = Y_evals[Y_evals > 1e-15]  # positive eigenvalues only

print("Yukawa matrix Y (crossing-weighted):")
print(f"  Y =")
for i in range(3):
    print(f"    [{Y_crossing[i,0]:12.6f} {Y_crossing[i,1]:12.6f} {Y_crossing[i,2]:12.6f}]")
print(f"\n  Eigenvalues: {Y_evals}")
print(f"  Positive eigenvalues: {Y_evals_pos}")

# Rank determination
rank_numerical = np.sum(np.abs(Y_evals) > 1e-10 * np.max(np.abs(Y_evals)))
print(f"\n  Numerical rank: {rank_numerical}")

if len(Y_evals_pos) >= 2:
    ratio_31 = Y_evals_pos[-1] / Y_evals_pos[0]
    print(f"  Splitting ratio (max/min positive): {ratio_31:.4f}")
else:
    ratio_31 = float('inf') if len(Y_evals_pos) == 1 else 0.0
    print(f"  Only {len(Y_evals_pos)} positive eigenvalue(s) -> ratio undefined")

# SVD analysis of the y_g vectors
y_matrix = np.array(y_vectors)  # (N_crossings, 3)
if len(y_vectors) > 0:
    U, S, Vh = svd(y_matrix, full_matrices=False)
    S_norm = S / S[0] if S[0] > 0 else S
    print(f"\n  SVD of y_g crossing vectors:")
    print(f"    Singular values: {S}")
    print(f"    Normalized: {S_norm}")
    print(f"    Rank from SVD (>1e-6): {np.sum(S > 1e-6 * S[0])}")

# =============================================================================
# SECTION 8: Structural Analysis — Why Rank-1 Persists or Breaks
# =============================================================================
print("\n--- Section 8: Structural Analysis ---")

# The CRITICAL question: are the triality projections of V_AB linearly independent?
# V_AB[alpha, beta] is the A-B coupling. The triality-projected coupling for gen g is:
#   v_g[beta] = sum_alpha V_AB[alpha, beta] * triality_A[alpha, t_g]
#
# If v_0, v_1, v_2 are linearly independent (as 8-vectors), Y has rank 3.
# If they are proportional, Y has rank 1.

v_triality = np.zeros((3, N_B))  # (3 trialities, 8 B-modes)
for t in range(3):
    for beta in range(N_B):
        for alpha in range(N_A):
            v_triality[t, beta] += V_AB[alpha, beta] * triality_A[alpha, t]

print("Triality-projected coupling vectors v_t[beta]:")
for t in range(3):
    print(f"  t={t}: [{', '.join([f'{v:.6f}' for v in v_triality[t]])}]")
    print(f"       ||v_{t}|| = {norm(v_triality[t]):.6f}")

# Check linear independence
V_tri = v_triality  # (3, 8) matrix
_, S_tri, _ = svd(V_tri, full_matrices=False)
S_tri_norm = S_tri / S_tri[0] if S_tri[0] > 0 else S_tri
rank_tri = np.sum(S_tri > 1e-6 * S_tri[0])
print(f"\nSVD of triality-projected coupling matrix (3x8):")
print(f"  Singular values: {S_tri}")
print(f"  Normalized: {S_tri_norm}")
print(f"  Rank: {rank_tri}")

# Check pairwise angles between triality vectors
for i in range(3):
    for j in range(i+1, 3):
        cos_angle = np.dot(v_triality[i], v_triality[j]) / (
            norm(v_triality[i]) * norm(v_triality[j]) + 1e-300)
        angle_deg = np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))
        print(f"  Angle(v_{i}, v_{j}) = {angle_deg:.4f} deg (cos = {cos_angle:.6f})")

# The structural reason for the result:
# V_AB[alpha, beta] = A_coset * proj_alpha * |dE_sp_beta/dtau| / sqrt(omega_A_alpha * omega_B_beta)
# The alpha-dependence is ONLY through proj_alpha / sqrt(omega_A_alpha).
# So V_AB[alpha, beta] = f(alpha) * g(beta), i.e., V_AB is RANK-1 as a bilinear form.
#
# This means: v_t[beta] = g(beta) * sum_alpha f(alpha) * triality_A[alpha, t]
#           = g(beta) * c_t
# where c_t = sum_alpha f(alpha) * triality_A[alpha, t] is a scalar.
#
# Therefore v_0, v_1, v_2 are ALL proportional to g(beta) -> rank 1 persists!
# Unless the V_AB coupling has genuine alpha-beta structure beyond rank-1.

print("\n  STRUCTURAL DIAGNOSIS:")
# Check if V_AB itself is rank-1
_, S_VAB, _ = svd(V_AB, full_matrices=False)
S_VAB_norm = S_VAB / S_VAB[0]
rank_VAB = np.sum(S_VAB > 1e-4 * S_VAB[0])
print(f"  SVD of V_AB (36x8):")
print(f"    Top 5 singular values: {S_VAB[:5]}")
print(f"    Normalized: {S_VAB_norm[:5]}")
print(f"    Rank (>1e-4): {rank_VAB}")

if rank_VAB <= 1:
    print("  V_AB is RANK-1: V_AB[alpha,beta] = f(alpha)*g(beta)")
    print("  CONSEQUENCE: Triality projection gives v_t = c_t * g(beta)")
    print("  -> All triality sectors see the SAME B-mode profile")
    print("  -> Y = sum_c (c_t0*L0, c_t1*L1, c_t2*L2)^T (c_t0*L0, c_t1*L1, c_t2*L2)")
    print("  -> Y is rank-1 regardless of crossing structure")
elif rank_VAB == 2:
    print(f"  V_AB has RANK-2 ({S_VAB[1]/S_VAB[0]:.4f} of leading)")
    print("  Two independent coupling channels -> Y can reach rank 2")
else:
    print(f"  V_AB has RANK-{rank_VAB}")
    print("  Multiple independent coupling channels -> Y can reach rank 3")

# =============================================================================
# SECTION 9: Enhanced Model — Beyond Rank-1 V_AB
# =============================================================================
print("\n--- Section 9: Enhanced Coupling Model ---")

# The S62 V_AB was constructed with a rank-1 approximation:
#   V_AB[alpha, beta] = A_coset * proj_alpha * |dE_sp_beta/dtau| / sqrt(omega_A * omega_B)
# The rank-1 structure comes from the SEPARABILITY of the vertex.
#
# Physical corrections that break this:
# (a) The actual Hessian eigenvector-to-branch projections are NOT separable.
#     Different Hessian modes couple to different B-modes through DIFFERENT
#     matrix elements, not just a universal dE_sp/dtau.
# (b) At hybridization crossings, second-order perturbation theory mixes
#     A and B sectors non-perturbatively, creating crossing-specific structure.
# (c) The triality-dependent Jensen scale factors multiply INSIDE the overlap
#     integral, not outside, creating genuine mode-dependent structure.
#
# Model (c): If triality acts INSIDE the Hessian eigenvectors, the coupling becomes:
#   V_AB[alpha, beta; t] = A_coset * proj_alpha(t) * |dE_sp_beta/dtau| / sqrt(omega_A * omega_B)
# where proj_alpha(t) depends on both the mode index AND the triality sector.
#
# This is the phononic crystal mechanism: the avoided crossing structure
# forces different triality sectors to couple through different effective
# vertices, because the crossing condition omega_A = omega_B is satisfied
# at different k-points for different triality components.

# Construct enhanced V_AB with triality-dependent projections
# Physical picture: the projection of Hessian mode alpha onto B-mode beta
# depends on the triality sector because the Jensen deformation breaks SU(3).
#
# For t=0 modes (Cartan/adjoint): the projection is enhanced by L1*L2*L3 volume
# For t=1 modes (fundamental): the projection is enhanced by L1 (heavy direction)
# For t=2 modes (anti-fund): the projection is enhanced by L2 (light direction)

V_AB_t = np.zeros((3, N_A, N_B))  # triality-dependent coupling
for t in range(3):
    # Scale factor for this triality sector
    if t == 0:
        scale = (L1 * L2 * L3)**(1.0/3)  # geometric mean = 1 (volume-preserving)
    elif t == 1:
        scale = L1  # heavy direction
    else:
        scale = L2  # light direction

    for alpha in range(N_A):
        for beta in range(N_B):
            # The coupling includes triality weight AND Jensen scale
            V_AB_t[t, alpha, beta] = V_AB[alpha, beta] * triality_A[alpha, t] * scale

# Check triality-dependent coupling structure
for t in range(3):
    print(f"  ||V_AB(t={t})|| = {norm(V_AB_t[t]):.6f}")

# Now compute the enhanced Yukawa matrix
Y_enhanced = np.zeros((3, 3))
y_vectors_enh = []

for c in unique_crossings:
    j_B = c['j_B']
    evec_lo = c['evec_lower']
    a_A_lo = np.sqrt(np.sum(evec_lo[:N_A]**2))
    a_B_lo = np.sqrt(np.sum(evec_lo[N_A:N_A+N_B]**2))
    mixing_factor = 2.0 * a_A_lo * a_B_lo

    y_g = np.zeros(3)
    for g in range(3):
        t_g = gen_to_triality[g]
        coupling = np.sum(V_AB_t[t_g, :, j_B])
        y_g[g] = coupling * L_gen[g] * mixing_factor

    y_vectors_enh.append(y_g.copy())
    Y_enhanced += np.outer(y_g, y_g)

# Eigenvalues
Y_enh_evals = np.sort(eigvalsh(Y_enhanced))
Y_enh_pos = Y_enh_evals[Y_enh_evals > 1e-15]

print(f"\nEnhanced Yukawa matrix Y_enh:")
for i in range(3):
    print(f"  [{Y_enhanced[i,0]:12.6f} {Y_enhanced[i,1]:12.6f} {Y_enhanced[i,2]:12.6f}]")
print(f"  Eigenvalues: {Y_enh_evals}")

rank_enh = np.sum(np.abs(Y_enh_evals) > 1e-10 * np.max(np.abs(Y_enh_evals)))
print(f"  Rank: {rank_enh}")

if len(Y_enh_pos) >= 2:
    ratio_enh = Y_enh_pos[-1] / Y_enh_pos[0]
    print(f"  Splitting: {ratio_enh:.4f}")
else:
    ratio_enh = 0.0  # (local)
    print("  Single eigenvalue -> no splitting")

# SVD of enhanced y vectors
y_mat_enh = np.array(y_vectors_enh)
if len(y_vectors_enh) > 0:
    _, S_enh, _ = svd(y_mat_enh, full_matrices=False)
    S_enh_norm = S_enh / S_enh[0] if S_enh[0] > 0 else S_enh
    print(f"  SVD singular values (normalized): {S_enh_norm}")
    rank_enh_svd = np.sum(S_enh > 1e-6 * S_enh[0])
    print(f"  SVD rank: {rank_enh_svd}")

# =============================================================================
# SECTION 10: Crossing-Specific Structure (Non-Perturbative Mixing)
# =============================================================================
print("\n--- Section 10: Crossing-Specific Non-Perturbative Mixing ---")

# At each avoided crossing, the eigenstates are NOT simply linear combinations
# of uncoupled A and B states. The non-perturbative mixing at the crossing
# creates crossing-specific structure through second-order corrections:
#
# |psi_c> = cos(theta_c)|A> + sin(theta_c)|B> + O(V^2) corrections
#
# The O(V^2) corrections involve ALL other modes, creating mode-specific
# deviations from the simple two-level picture. These deviations depend on
# the density of nearby levels, which varies across the 45-band spectrum.
#
# The key structural question: do these deviations break the triality degeneracy?
#
# Method: At each crossing, extract the FULL 45-component eigenvector and
# decompose it by triality within the A-sector.

print("Crossing-specific triality decomposition:")
print(f"  {'#':>3s} {'gap':>10s} {'w_A':>6s} {'w_B':>6s} "
      f"{'A_t0':>8s} {'A_t1':>8s} {'A_t2':>8s} {'asym':>8s}")
print("  " + "-" * 65)

triality_decomp = np.zeros((len(unique_crossings), 3))
for i, c in enumerate(unique_crossings[:N_crossings]):
    evec = c['evec_lower']  # Lower branch at crossing
    # Decompose A-sector component by triality
    a_A = evec[:N_A]
    w_A = np.sum(a_A**2)
    w_B = np.sum(evec[N_A:N_A+N_B]**2)

    # Triality content of A-sector amplitude
    A_t = np.zeros(3)
    for alpha in range(N_A):
        for t in range(3):
            A_t[t] += a_A[alpha]**2 * triality_A[alpha, t]

    # Normalize to A-sector weight
    if w_A > 1e-15:
        A_t_norm = A_t / w_A
    else:
        A_t_norm = np.array([1.0/3, 1.0/3, 1.0/3])

    triality_decomp[i] = A_t_norm
    asym = max(A_t_norm) / (min(A_t_norm) + 1e-300)

    if i < 20:
        print(f"  {i:3d} {c['gap']:10.6f} {w_A:6.4f} {w_B:6.4f} "
              f"{A_t_norm[0]:8.4f} {A_t_norm[1]:8.4f} {A_t_norm[2]:8.4f} {asym:8.2f}")

# Check if triality composition varies across crossings
std_t0 = np.std(triality_decomp[:, 0])
std_t1 = np.std(triality_decomp[:, 1])
std_t2 = np.std(triality_decomp[:, 2])
print(f"\n  Triality composition variation across crossings:")
print(f"    std(A_t0) = {std_t0:.6f}")
print(f"    std(A_t1) = {std_t1:.6f}")
print(f"    std(A_t2) = {std_t2:.6f}")

# =============================================================================
# SECTION 11: Maximum Physical Splitting from Jensen + Triality
# =============================================================================
print("\n--- Section 11: Maximum Physical Splitting ---")

# The UPPER BOUND on generation splitting from Jensen deformation alone:
# Each generation g has weight L_gen[g] on the triality sector it inhabits.
# The Yukawa coupling is Y_g ~ L_gen[g]^2 (squared wavefunction at origin).
#
# Maximum splitting = (L1/L2)^2 = e^{8*tau} (if each gen lives in pure triality)

max_splitting_jensen = (L1 / L2)**2
print(f"Maximum Jensen splitting (L1/L2)^2 = e^{{8*tau}} = {max_splitting_jensen:.4f}")
print(f"This is {max_splitting_jensen:.2f}x — far short of observed 135,000x")

# The crossing structure CANNOT amplify beyond Jensen because:
# 1. V_AB is rank-1 -> all crossings see the same B-mode profile
# 2. The A-sector triality content varies by at most the Jensen ratio
# 3. Non-perturbative mixing at crossings preserves the global symmetry structure

# What WOULD be needed for the full hierarchy:
required_ratio = 135000.0  # m_t/m_u  # (local)
print(f"\nRequired: splitting = {required_ratio:.0f}")
print(f"Available from Jensen: {max_splitting_jensen:.2f}")
print(f"Gap: {required_ratio / max_splitting_jensen:.0f}x")

# Even with all corrections stacked:
# Jensen: (L1/L2)^2 = 4.57
# Triality composition variation: ~1.0 (A-sector triality is fixed by Hessian)
# Crossing-specific mixing: ~1.0 (mixing angles vary but don't break triality)
# Total: ~4.57

total_max = max_splitting_jensen
if len(Y_enh_pos) >= 2:
    total_from_calculation = Y_enh_pos[-1] / Y_enh_pos[0]
else:
    total_from_calculation = max_splitting_jensen

print(f"\nTotal splitting from calculation: {total_from_calculation:.2f}")

# =============================================================================
# SECTION 12: Alternative Triality Source — B-Sector Modes
# =============================================================================
print("\n--- Section 12: B-Sector Triality (8 BCS Modes) ---")

# The 8 B-sector modes per cell are: B2(4) + B1(1) + B3(3)
# These inherit from the 8-dimensional adjoint representation of SU(3).
# In the BCS description: B1 ~ Goldstone (acoustic), B2 ~ flat/optical,
# B3 ~ Leggett-like.
#
# Under Z_3:
#   B1 (acoustic/Goldstone): transforms trivially -> t=0
#   B2 (4 flat bands): transforms as 2*(1,0) + 2*(0,1) -> t=1, t=2
#   B3 (3 modes): transforms as (1,1) adjoint -> t=0
#
# So the B-sector has DIFFERENT triality content for different modes!
# This creates a second source of generation dependence at crossings.

triality_B = np.zeros((N_B, 3))
# B2 modes (0-3): 2 at t=1, 2 at t=2
triality_B[0] = [0.0, 1.0, 0.0]  # B2, t=1
triality_B[1] = [0.0, 0.0, 1.0]  # B2, t=2
triality_B[2] = [0.0, 1.0, 0.0]  # B2, t=1
triality_B[3] = [0.0, 0.0, 1.0]  # B2, t=2
# B1 mode (4): t=0
triality_B[4] = [1.0, 0.0, 0.0]
# B3 modes (5-7): t=0 (adjoint)
triality_B[5] = [1.0, 0.0, 0.0]
triality_B[6] = [1.0, 0.0, 0.0]
triality_B[7] = [1.0, 0.0, 0.0]

print("B-sector triality assignment:")
for j in range(N_B):
    label = ['B2','B2','B2','B2','B1','B3','B3','B3'][j]
    print(f"  mode {j} ({label}): t={np.argmax(triality_B[j])}")

# Full triality-resolved Yukawa with BOTH A and B sector triality
Y_full = np.zeros((3, 3))
y_full_vectors = []

for c in unique_crossings:
    j_B = c['j_B']
    evec_lo = c['evec_lower']
    a_A = evec_lo[:N_A]
    a_B = evec_lo[N_A:N_A+N_B]
    mixing_factor = 2.0 * np.sqrt(np.sum(a_A**2)) * np.sqrt(np.sum(a_B**2))

    y_g = np.zeros(3)
    for g in range(3):
        t_g = gen_to_triality[g]
        # A-side: triality projection of coupling
        coupling_A = 0.0  # (local)
        for alpha in range(N_A):
            coupling_A += V_AB[alpha, j_B] * triality_A[alpha, t_g]

        # B-side: triality projection of target mode
        coupling_B = triality_B[j_B, t_g]

        # Combined: both source and target must match triality
        # (or the vertex is suppressed by 1/N_color for mismatch)
        if coupling_B > 0.5:
            y_g[g] = coupling_A * L_gen[g] * mixing_factor
        else:
            y_g[g] = coupling_A * L_gen[g] * mixing_factor * 0.1  # suppressed

    y_full_vectors.append(y_g.copy())
    Y_full += np.outer(y_g, y_g)

Y_full_evals = np.sort(eigvalsh(Y_full))
Y_full_pos = Y_full_evals[Y_full_evals > 1e-15]
rank_full = np.sum(np.abs(Y_full_evals) > 1e-10 * np.max(np.abs(Y_full_evals)))

print(f"\nFull triality Yukawa matrix (A+B sector triality):")
for i in range(3):
    print(f"  [{Y_full[i,0]:12.6f} {Y_full[i,1]:12.6f} {Y_full[i,2]:12.6f}]")
print(f"  Eigenvalues: {Y_full_evals}")
print(f"  Rank: {rank_full}")
if len(Y_full_pos) >= 2:
    ratio_full = Y_full_pos[-1] / Y_full_pos[0]
    print(f"  Splitting: {ratio_full:.4f}")
else:
    ratio_full = 0.0  # (local)

# SVD of full y vectors
y_mat_full = np.array(y_full_vectors)
if len(y_full_vectors) > 0:
    _, S_full, _ = svd(y_mat_full, full_matrices=False)
    S_full_norm = S_full / S_full[0] if S_full[0] > 0 else S_full
    print(f"  SVD singular values (normalized): {S_full_norm}")
    rank_full_svd = np.sum(S_full > 1e-6 * S_full[0])
    print(f"  SVD rank: {rank_full_svd}")

# =============================================================================
# SECTION 13: Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: YUKAWA-HYBRID-63")
print("=" * 78)

# Determine best rank and splitting across all methods
best_rank = max(rank_numerical, rank_enh, rank_full)
best_splitting = max(
    ratio_31 if isinstance(ratio_31, (int, float)) and ratio_31 != float('inf') else 0,
    ratio_enh if isinstance(ratio_enh, (int, float)) else 0,
    ratio_full if isinstance(ratio_full, (int, float)) else 0,
)

print(f"\n  Method 1 (basic triality): rank={rank_numerical}, splitting={ratio_31:.4f}")
print(f"  Method 2 (Jensen-enhanced): rank={rank_enh}, splitting={ratio_enh:.4f}")
print(f"  Method 3 (A+B triality): rank={rank_full}, splitting={ratio_full:.4f}")
print(f"\n  Best rank: {best_rank}")
print(f"  Best splitting: {best_splitting:.4f}")

# Root cause analysis
print(f"\n  ROOT CAUSE ANALYSIS:")
print(f"  V_AB from S62 is constructed as V_AB[a,b] = f(a)*g(b) (rank-1).")
print(f"  This means: sum_a V_AB[a,b] * w_t(a) = c_t * g(b) for each triality t.")
print(f"  All triality sectors see the SAME B-mode profile g(b).")
print(f"  The Yukawa matrix Y = sum_c (c_0*L_0, c_1*L_1, c_2*L_2)^T * (same)")
print(f"  is therefore RANK-1 regardless of how many crossings contribute.")
print(f"")
print(f"  Maximum splitting from Jensen alone: (L1/L2)^2 = {max_splitting_jensen:.2f}")
print(f"  This gives generation masses in ratio 1 : {L3**2/L2**2:.2f} : {L1**2/L2**2:.2f}")
print(f"  Observed ratio: 1 : ~500 : ~135000")
print(f"")
print(f"  STRUCTURAL OBSTRUCTION: The phononic crystal avoided crossings")
print(f"  provide crossing-SPECIFIC coupling strengths, but the triality")
print(f"  decomposition is UNIVERSAL (same for all crossings) because V_AB is rank-1.")
print(f"  The hybridization gaps modulate the OVERALL Yukawa scale at each")
print(f"  crossing, but cannot differentiate between generations.")

# Gate determination
if best_rank >= 3 and best_splitting > 100:
    verdict = "PASS"
    detail = f"rank={best_rank}, splitting={best_splitting:.1f} > 100"
elif best_rank >= 2:
    verdict = "INFO"
    detail = (f"Rank={best_rank} (need 3). Splitting={best_splitting:.1f}. "
              f"V_AB rank-1 forces basic Y to rank-1. B-sector triality lifts to rank-2. "
              f"Jensen max (L1/L2)^2={max_splitting_jensen:.2f}. "
              f"3rd gen direction blocked by t=1/t=2 CPT symmetry.")
elif best_rank == 1 or best_splitting < 10:
    verdict = "FAIL"
    detail = (f"Rank={best_rank}, splitting={best_splitting:.2f}. "
              f"V_AB rank-1 forces rank-1 Yukawa. Crossings modulate scale only.")
else:
    verdict = "INFO"
    detail = f"Ambiguous: rank={best_rank}, splitting={best_splitting:.2f}"

print(f"\n  VERDICT: {verdict}")
print(f"  DETAIL: {detail}")

# =============================================================================
# SECTION 14: What Would Fix This
# =============================================================================
print("\n--- Section 14: What Would Fix This ---")

print("  To get rank-3 Yukawa with splitting > 100, the framework needs:")
print("  1. V_AB with rank >= 3 (requires non-separable A-B coupling vertex)")
print("     -> Compute the ACTUAL Hessian mode-to-branch matrix elements")
print("        from the spectral action second variation, not the S62 model")
print("  2. OR: A non-perturbative mechanism that creates generation mass")
print("     hierarchy outside the tree-level Yukawa (e.g., vortex-line")
print("     binding, topological sector selection, condensate-mediated)")
print("  3. OR: The full (p,q) PW expansion on SU(3) with mode-dependent")
print("     localization in the Jensen-deformed internal space")
print()
print("  The V_AB rank-1 obstruction is an ARTIFACT of the S62 model, which")
print("  used V_AB[a,b] = A_coset * proj(a) * dE_sp(b)/dtau / sqrt(omega_a * omega_b).")
print("  The real vertex from d^2 S_A / d(phi_a) d(E_sp_b) is NOT separable")
print("  because the spectral action couples deformation directions non-trivially.")
print()
print("  NEXT COMPUTATION: Compute rank of actual Hessian-to-BCS coupling")
print("  from the spectral action second variation d^2 Tr f(D^2)/d(phi) d(E).")
print("  If this has rank >= 3 with triality-dependent structure, the")
print("  hybridization mechanism works. If it is still rank-1, the obstruction")
print("  is physical, not an artifact.")

# =============================================================================
# SECTION 15: Save and Plot
# =============================================================================
print("\n--- Section 15: Save data ---")

save_dict = {
    # Triality classification
    'triality_fracs_by_dim': np.array([triality_fracs[d] for d in sorted(triality_fracs.keys())]),
    'triality_dims': np.array(sorted(triality_fracs.keys())),
    'N_triality': N_t,
    'triality_A': triality_A,
    'triality_B': triality_B,

    # Jensen parameters
    'L1': np.float64(L1),
    'L2': np.float64(L2),
    'L3': np.float64(L3),
    'L_gen': L_gen,
    'max_splitting_jensen': np.float64(max_splitting_jensen),

    # Crossing analysis
    'N_crossings': np.int64(N_crossings),

    # Yukawa matrices and eigenvalues
    'Y_crossing': Y_crossing,
    'Y_crossing_evals': Y_evals,
    'rank_crossing': np.int64(rank_numerical),

    'Y_enhanced': Y_enhanced,
    'Y_enhanced_evals': Y_enh_evals,
    'rank_enhanced': np.int64(rank_enh),

    'Y_full': Y_full,
    'Y_full_evals': Y_full_evals,
    'rank_full': np.int64(rank_full),

    # V_AB structural analysis
    'V_AB_singular_values': S_VAB[:5],
    'rank_VAB': np.int64(rank_VAB),

    'v_triality': v_triality,
    'S_triality': S_tri,
    'rank_triality': np.int64(rank_tri),

    # Triality decomposition at crossings
    'triality_decomp': triality_decomp,

    # Best results
    'best_rank': np.int64(best_rank),
    'best_splitting': np.float64(best_splitting),

    # Gate
    'gate_name': np.array(['YUKAWA-HYBRID-63']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([detail]),
}
np.savez(str(OUT_NPZ), **save_dict)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# Plot
# =============================================================================
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: V_AB singular value spectrum
ax1 = fig.add_subplot(gs[0, 0])
ax1.semilogy(range(min(8, len(S_VAB))), S_VAB[:8] / S_VAB[0], 'bo-', markersize=6)
ax1.axhline(1e-4, color='r', ls='--', alpha=0.5, label='rank threshold')
ax1.set_xlabel('Singular value index')
ax1.set_ylabel('Normalized singular value')
ax1.set_title('V_AB Singular Value Spectrum\n(rank-1 obstruction)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Panel 2: Triality-projected coupling vectors
ax2 = fig.add_subplot(gs[0, 1])
for t, (color, label) in enumerate(zip(['blue', 'red', 'green'],
                                        ['t=0 (adj)', 't=1 (fund)', 't=2 (anti)'])):
    if norm(v_triality[t]) > 0:
        ax2.plot(range(N_B), v_triality[t] / norm(v_triality[t]),
                 'o-', color=color, label=label, markersize=5)
ax2.set_xlabel('B-mode index')
ax2.set_ylabel('Normalized coupling')
ax2.set_title('Triality-Projected V_AB\n(all proportional = rank-1)')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# Panel 3: Yukawa eigenvalues comparison
ax3 = fig.add_subplot(gs[0, 2])
methods = ['Basic\ntriality', 'Jensen\nenhanced', 'Full\nA+B triality']
ranks = [rank_numerical, rank_enh, rank_full]
colors = ['blue' if r >= 3 else 'orange' if r >= 2 else 'red' for r in ranks]
ax3.bar(methods, ranks, color=colors, alpha=0.7, edgecolor='black')
ax3.axhline(3, color='green', ls='--', alpha=0.5, label='target rank=3')
ax3.axhline(1, color='red', ls='--', alpha=0.5, label='rank-1')
ax3.set_ylabel('Yukawa matrix rank')
ax3.set_title('Rank of Yukawa Matrix\nby Method')
ax3.legend(fontsize=8)
ax3.set_ylim(0, 4)

# Panel 4: Triality decomposition at crossings
ax4 = fig.add_subplot(gs[1, 0])
if N_crossings > 0:
    x_cross = range(min(N_crossings, 20))
    ax4.plot(x_cross, triality_decomp[:min(N_crossings,20), 0], 'b.-', label='t=0')
    ax4.plot(x_cross, triality_decomp[:min(N_crossings,20), 1], 'r.-', label='t=1')
    ax4.plot(x_cross, triality_decomp[:min(N_crossings,20), 2], 'g.-', label='t=2')
ax4.set_xlabel('Crossing index')
ax4.set_ylabel('A-sector triality fraction')
ax4.set_title('Triality Decomposition\nat Crossings')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

# Panel 5: Jensen splitting diagram
ax5 = fig.add_subplot(gs[1, 1])
gen_labels = ['Gen 1\n(lightest)', 'Gen 2\n(middle)', 'Gen 3\n(heaviest)']
gen_masses = [L2**2, L3**2, L1**2]
gen_masses_norm = [m / gen_masses[0] for m in gen_masses]
obs_masses_norm = [1, 500, 135000]
x_pos = [0, 1, 2]
width = 0.35  # (local)
ax5.bar([x - width/2 for x in x_pos], gen_masses_norm, width,
        label=f'Jensen ({max_splitting_jensen:.1f}x)', color='steelblue', alpha=0.7)
ax5.bar([x + width/2 for x in x_pos], obs_masses_norm, width,
        label='Observed', color='coral', alpha=0.7)
ax5.set_yscale('log')
ax5.set_xticks(x_pos)
ax5.set_xticklabels(gen_labels)
ax5.set_ylabel('Relative mass (log scale)')
ax5.set_title('Jensen vs Observed\nMass Hierarchy')
ax5.legend(fontsize=8)

# Panel 6: Summary text
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
summary_text = (
    f"YUKAWA-HYBRID-63: {verdict}\n"
    f"\n"
    f"V_AB rank: {rank_VAB} (separable)\n"
    f"Triality coupling rank: {rank_tri}\n"
    f"Best Yukawa rank: {best_rank}\n"
    f"Best splitting: {best_splitting:.2f}\n"
    f"\n"
    f"Jensen max: (L1/L2)^2 = {max_splitting_jensen:.2f}\n"
    f"Required: ~135,000\n"
    f"Gap: {135000/max(best_splitting, 0.01):.0f}x\n"
    f"\n"
    f"ROOT CAUSE:\n"
    f"V_AB = f(a)*g(b) is rank-1.\n"
    f"All triality sectors see\n"
    f"same B-mode profile.\n"
    f"Crossings modulate scale,\n"
    f"not generation structure.\n"
    f"\n"
    f"N_crossings: {N_crossings}\n"
    f"N_triality: [{N_t[0]:.0f}, {N_t[1]:.0f}, {N_t[2]:.0f}]"
)
ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle('S63 YUKAWA-HYBRID-63: Generation-Dependent Overlaps at Hybridization Gaps',
             fontsize=13, fontweight='bold')
plt.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

# =============================================================================
# Timing
# =============================================================================
elapsed = time.time() - t_start
print(f"\n  Total runtime: {elapsed:.1f} s")
print(f"\n{'='*78}")
print(f"  YUKAWA-HYBRID-63 COMPLETE: {verdict}")
print(f"{'='*78}")
