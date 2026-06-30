#!/usr/bin/env python3
"""
s63_berry_ktheory.py — Berry Phase at 16 Hybridization Crossings
================================================================

BERRY-KTHEORY-63 (W5-02): Compute the Berry phase gamma_n around each of the
16 tight A-B avoided crossings from S62 phonon dispersion data. If any
|gamma| > 0.1*pi, it carries topological charge. Also compute total Chern
number from the full band structure.

PHYSICS:
    At an avoided crossing between bands n and n+1, the eigenstates rotate
    in Hilbert space as the parameter k sweeps through the crossing region.
    The Berry phase measures this rotation:

        gamma_n = -Im sum_{k} log <psi_n(k)|psi_n(k+dk)>       (1)

    This is the discretized Berry connection along the 1D k-path. For a
    two-level system (Landau-Zener), the Berry phase through an avoided
    crossing is controlled by the ratio gap/bandwidth:
        - Adiabatic limit (slow passage): gamma -> 0 (state follows)
        - Diabatic limit (fast passage): gamma -> pi (state jumps)
        - Intermediate: gamma encodes the geometric mixing angle

    For a closed 1D loop, the total Berry phase is quantized in units of pi
    (Z_2 topological invariant). On the CG(24) graph, the k-path is periodic
    (Brillouin zone of the Cayley graph), so we can compute:
        - Berry phase through each crossing region (local, may be non-quantized)
        - Total Berry phase across the full BZ (must be multiple of pi for
          real Hamiltonian with time-reversal symmetry)

    The Chern number is defined for 2D parameter spaces; on our 1D graph,
    the Z_2 invariant (Zak phase mod pi) is the appropriate topological
    index.

    Cross-domain connection: This is the acoustic analog of the Zak phase
    in phononic crystals (cf. Xiao, Zhang, Chan 2014). The hybridization
    gaps are the phononic bandgaps. The Berry phase determines whether
    topological edge states appear at domain walls in the SU(3) fiber.

Gate: BERRY-KTHEORY-63
    PASS: any |gamma| > 0.1*pi at a crossing
    INFO: all |gamma| < 0.1*pi

Author: tesla-resonance
Session: S63 W5-02
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s63_berry_ktheory.npz"
OUT_PNG = SCRIPT_DIR / "s63_berry_ktheory.png"
OUT_TXT = SCRIPT_DIR / "s63_berry_ktheory_output.txt"

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
print("S63 BERRY-KTHEORY-63: Berry Phase at 16 Hybridization Crossings")
print("=" * 78)

# =============================================================================
# SECTION 1: Load S62 phonon dispersion data
# =============================================================================
print("\n--- Section 1: Load input data ---")

d = np.load(SCRIPT_DIR / "s62_phonon_dispersion_full.npz", allow_pickle=True)
omega_full = d['omega_full']       # (32, 45) eigenvalues
evecs_full = d['evecs_full']       # (32, 45, 45) eigenvectors
sector_weight = d['sector_weight'] # (32, 45, 3)
omega_A = d['omega_A']             # (36,) uncoupled A frequencies
omega_B = d['omega_B_uncoupled']   # (32, 8) uncoupled B
k_eff = d['k_eff']                 # (32,)
lambda_n = d['lambda_n']           # (32,)
V_AB = d['V_AB']                   # (36, 8)
V_BC = d['V_BC']                   # (8,)
V_AC = d['V_AC']                   # (36,)
E_J = float(d['E_J_fold'])
eps_can = float(d['eps_canonical'])
omega_L0 = float(d['omega_L0'])
J_L = float(d['J_L'])
A_coset_sq = float(d['A_coset_sq'])

N_k = omega_full.shape[0]  # 32
N_total = omega_full.shape[1]  # 45
N_A = 36  # (local)
N_B = 8  # (local)
N_C = 1  # (local)

print(f"Loaded S62 data: {N_k} k-points, {N_total} bands")
print(f"k range: [{k_eff[0]:.4f}, {k_eff[-1]:.4f}]")
print(f"omega range: [{omega_full.min():.4f}, {omega_full.max():.4f}] M_KK")

# =============================================================================
# SECTION 2: Identify the 16 tight A-B avoided crossings
# =============================================================================
print("\n--- Section 2: Identify 16 tight A-B avoided crossings ---")

# Find all (A-mode, B-mode, k-index) triples with |detuning| < 0.1
crossings_raw = []
for i_a in range(N_A):
    for i_b in range(N_B):
        for k_idx in range(N_k):
            det = abs(omega_A[i_a] - omega_B[k_idx, i_b])
            if det < 0.1:
                crossings_raw.append({
                    'i_a': i_a, 'i_b': i_b, 'k_idx': k_idx,
                    'detuning': det,
                    'omega_A': omega_A[i_a],
                    'omega_B': omega_B[k_idx, i_b],
                })

# Group by (B-mode, k-index) to identify distinct crossing events
from collections import defaultdict
groups = defaultdict(list)
for c in crossings_raw:
    groups[(c['i_b'], c['k_idx'])].append(c)

# Sort groups by minimum detuning
group_list = []
for key, members in groups.items():
    min_det = min(m['detuning'] for m in members)
    a_modes = sorted(set(m['i_a'] for m in members))
    omega_cross = np.mean([m['omega_A'] for m in members])
    group_list.append({
        'b_mode': key[0], 'k_idx': key[1],
        'a_modes': a_modes, 'n_a': len(a_modes),
        'min_detuning': min_det, 'omega_cross': omega_cross,
    })

group_list.sort(key=lambda x: x['min_detuning'])

print(f"Found {len(group_list)} distinct crossing groups:")
for i, g in enumerate(group_list):
    a_str = f"A-{g['a_modes'][0]}" if g['n_a'] == 1 else f"A-{g['a_modes'][0]}..{g['a_modes'][-1]}"
    print(f"  [{i:2d}] B-{g['b_mode']}, k_idx={g['k_idx']:2d}, {a_str} ({g['n_a']} modes), "
          f"det={g['min_detuning']:.4f}, omega~{g['omega_cross']:.2f} M_KK")

# Take first 16 (tightest detuning) -- this matches S62 definition
N_cross = min(16, len(group_list))
tight_crossings = group_list[:N_cross]
print(f"\nUsing {N_cross} tightest crossings for Berry phase computation")

# =============================================================================
# SECTION 3: Berry phase computation — discrete Berry connection
# =============================================================================
print("\n--- Section 3: Berry phase computation ---")

# Method: For each crossing, identify the two bands that participate in the
# avoided crossing. Then compute the Berry phase along the full k-path for
# each of these bands, and also a local Berry phase through the crossing
# region (k-window centered on the crossing k-point).
#
# The discrete Berry phase for band n along path k_0, k_1, ..., k_{M-1} is:
#
#   gamma_n = -Im sum_{j=0}^{M-1} log <psi_n(k_j) | psi_n(k_{j+1 mod M})>  (2)
#
# For a non-periodic path (open BZ), the total phase is path-dependent.
# For a periodic path (closed BZ), it is the Zak phase = 0 or pi (mod 2pi)
# for time-reversal invariant systems.
#
# LOCAL Berry phase through a crossing: we use a k-window of +-3 points
# around the crossing k-index and compute the accumulated phase.

def berry_phase_segment(evecs_band, periodic=False):
    """
    Compute discrete Berry phase for a sequence of eigenstates.

    Parameters:
        evecs_band: array of shape (N_k, N_dim) — eigenvector at each k-point
        periodic: if True, close the loop (k_last -> k_0)

    Returns:
        gamma: Berry phase (real number)
        overlaps: array of |<psi(k)|psi(k+1)>| for diagnostics
    """
    M = evecs_band.shape[0]
    phase = 0.0
    overlaps = np.zeros(M - 1 + (1 if periodic else 0))

    for j in range(M - 1):
        overlap = np.dot(evecs_band[j].conj(), evecs_band[j + 1])
        overlaps[j] = abs(overlap)
        if abs(overlap) < 1e-15:
            # Degenerate or discontinuous — flag
            phase += 0.0
        else:
            phase += -np.imag(np.log(overlap / abs(overlap)))

    if periodic:
        overlap = np.dot(evecs_band[-1].conj(), evecs_band[0])
        overlaps[-1] = abs(overlap)
        if abs(overlap) > 1e-15:
            phase += -np.imag(np.log(overlap / abs(overlap)))

    return phase, overlaps


def fix_gauge(evecs_band):
    """
    Apply parallel transport gauge: at each k-step, multiply by phase
    so that <psi(k)|psi(k+dk)> is real and positive. This removes the
    arbitrary gauge freedom and isolates the geometric phase.

    Returns gauge-fixed eigenvectors.
    """
    M, N = evecs_band.shape
    fixed = np.copy(evecs_band)
    for j in range(1, M):
        overlap = np.dot(fixed[j - 1].conj(), fixed[j])
        if abs(overlap) > 1e-15:
            phase_factor = overlap / abs(overlap)
            fixed[j] = fixed[j] / phase_factor
    return fixed


def find_crossing_bands(omega_full, k_idx, omega_cross):
    """
    At k-point k_idx, find the two bands whose eigenvalues bracket omega_cross.
    Returns (band_lower, band_upper).
    """
    evals = omega_full[k_idx]
    # Find the band just below and just above omega_cross
    below = np.where(evals <= omega_cross)[0]
    above = np.where(evals > omega_cross)[0]
    if len(below) == 0 or len(above) == 0:
        # Edge case: all bands above or below
        idx_closest = np.argmin(np.abs(evals - omega_cross))
        return max(0, idx_closest - 1), min(N_total - 1, idx_closest + 1)
    return below[-1], above[0]


# =============================================================================
# SECTION 3a: Full-BZ Zak phases for all 45 bands
# =============================================================================
print("\n--- Section 3a: Full-BZ Zak phases (all 45 bands) ---")

# The Zak phase is the Berry phase across the entire Brillouin zone.
# For a 1D system with inversion symmetry, it is quantized to 0 or pi.
# Our CG(24) has the full Weyl group symmetry, so we expect quantization.
#
# IMPORTANT: The CG(24) BZ is NOT periodic in the conventional sense —
# the 32 k-points are the eigenvalues of the graph Laplacian, which form
# a discrete set, not a continuous loop. So the "Zak phase" here is the
# Berry phase along the ordered sequence of k-points (open path).
# The physical quantity is the ACCUMULATED geometric phase.

zak_phases = np.zeros(N_total)
zak_overlaps_min = np.zeros(N_total)

for n in range(N_total):
    # Extract eigenvector for band n at each k-point
    # evecs_full[k, :, n] is the n-th eigenvector at k-point k
    band_evecs = evecs_full[:, :, n]  # (32, 45)

    # Compute Berry phase along full k-path (open)
    gamma, overlaps = berry_phase_segment(band_evecs, periodic=False)
    zak_phases[n] = gamma
    zak_overlaps_min[n] = overlaps.min() if len(overlaps) > 0 else 1.0

print(f"Zak phases (full BZ, open path):")
print(f"  Range: [{zak_phases.min():.6f}, {zak_phases.max():.6f}]")
print(f"  |gamma| > 0.1*pi: {np.sum(np.abs(zak_phases) > 0.1 * PI)} bands")
print(f"  |gamma| > 0.5*pi: {np.sum(np.abs(zak_phases) > 0.5 * PI)} bands")
print(f"  |gamma| > 0.9*pi: {np.sum(np.abs(zak_phases) > 0.9 * PI)} bands")
print(f"  Min overlap (gauge quality): {zak_overlaps_min.min():.6f}")

# Print Zak phases for all bands
for n in range(N_total):
    flag = " ***" if abs(zak_phases[n]) > 0.1 * PI else ""
    print(f"  Band {n:2d}: gamma = {zak_phases[n]:+.6f} ({zak_phases[n]/PI:+.4f}*pi), "
          f"min_overlap = {zak_overlaps_min[n]:.6f}{flag}")

# =============================================================================
# SECTION 3b: Local Berry phase at each crossing
# =============================================================================
print("\n--- Section 3b: Local Berry phase at 16 crossings ---")

# For each crossing, we:
# 1. Identify the two bands that participate
# 2. Compute Berry phase in a k-window around the crossing
# 3. Measure the sector-weight swap (how much A-character swaps to B)

crossing_results = []

for ic, cross in enumerate(tight_crossings):
    k_c = cross['k_idx']
    omega_c = cross['omega_cross']
    b_mode = cross['b_mode']
    a_modes = cross['a_modes']

    # Find the two coupled bands at the crossing
    band_lo, band_hi = find_crossing_bands(omega_full, k_c, omega_c)

    # Local gap at crossing
    gap_at_cross = omega_full[k_c, band_hi] - omega_full[k_c, band_lo]

    # k-window: +-W points centered on k_c
    W = 3  # (local)
    k_lo = max(0, k_c - W)
    k_hi = min(N_k - 1, k_c + W)
    k_window = list(range(k_lo, k_hi + 1))
    n_pts = len(k_window)

    # Extract eigenvectors for both bands in the window
    evecs_lo = evecs_full[k_window, :, band_lo]  # (n_pts, 45)
    evecs_hi = evecs_full[k_window, :, band_hi]  # (n_pts, 45)

    # Berry phase for each band through the crossing window
    gamma_lo, overlaps_lo = berry_phase_segment(evecs_lo, periodic=False)
    gamma_hi, overlaps_hi = berry_phase_segment(evecs_hi, periodic=False)

    # Sector weight swap: measure A-weight change across window
    sw_lo_A_start = sector_weight[k_window[0], band_lo, 0]
    sw_lo_A_end = sector_weight[k_window[-1], band_lo, 0]
    sw_hi_A_start = sector_weight[k_window[0], band_hi, 0]
    sw_hi_A_end = sector_weight[k_window[-1], band_hi, 0]

    sw_lo_B_start = sector_weight[k_window[0], band_lo, 1]
    sw_lo_B_end = sector_weight[k_window[-1], band_lo, 1]

    # Mixing angle from sector weights
    # At the crossing, the eigenstates are maximally mixed
    # The mixing angle theta is defined by:
    #   |psi_lo> = cos(theta)|A> + sin(theta)|B>
    #   |psi_hi> = -sin(theta)|A> + cos(theta)|B>
    # At the crossing point:
    sw_A_at_cross = sector_weight[k_c, band_lo, 0]
    sw_B_at_cross = sector_weight[k_c, band_lo, 1]
    theta_mix = np.arctan2(np.sqrt(sw_B_at_cross), np.sqrt(sw_A_at_cross))

    # The Berry phase through an avoided crossing in the adiabatic picture is
    # related to the mixing angle: for a linear crossing with Landau-Zener
    # parameter delta = V^2/(v * hbar), the geometric phase is:
    #   gamma = pi/2 - arctan(delta) for the adiabatic state
    # In our discrete case, the accumulated phase measures the same thing.

    result = {
        'crossing_idx': ic,
        'b_mode': b_mode,
        'k_idx': k_c,
        'a_modes': a_modes,
        'band_lo': band_lo,
        'band_hi': band_hi,
        'gap': gap_at_cross,
        'omega_cross': omega_c,
        'gamma_lo': gamma_lo,
        'gamma_hi': gamma_hi,
        'theta_mix': theta_mix,
        'min_overlap_lo': overlaps_lo.min() if len(overlaps_lo) > 0 else 1.0,
        'min_overlap_hi': overlaps_hi.min() if len(overlaps_hi) > 0 else 1.0,
        'sw_swap_A': abs(sw_lo_A_end - sw_lo_A_start),
        'sw_swap_B': abs(sw_lo_B_end - sw_lo_B_start),
        'sw_A_at_cross': sw_A_at_cross,
        'sw_B_at_cross': sw_B_at_cross,
        'k_window': k_window,
        'n_pts': n_pts,
    }
    crossing_results.append(result)

    flag = " *** TOPOLOGICAL" if abs(gamma_lo) > 0.1 * PI or abs(gamma_hi) > 0.1 * PI else ""
    print(f"\nCrossing [{ic:2d}]: B-{b_mode}, k_idx={k_c}, bands ({band_lo},{band_hi}), "
          f"gap={gap_at_cross:.4f} M_KK")
    print(f"  gamma_lo = {gamma_lo:+.6f} ({gamma_lo/PI:+.4f}*pi)")
    print(f"  gamma_hi = {gamma_hi:+.6f} ({gamma_hi/PI:+.4f}*pi)")
    print(f"  theta_mix = {theta_mix:.4f} ({theta_mix/PI:.4f}*pi)")
    print(f"  min_overlap: lo={result['min_overlap_lo']:.6f}, hi={result['min_overlap_hi']:.6f}")
    print(f"  sector weight at crossing: A={sw_A_at_cross:.4f}, B={sw_B_at_cross:.4f}")
    print(f"  sw_swap (A across window): {result['sw_swap_A']:.4f}")
    print(f"  A-modes involved: {a_modes}{flag}")

# =============================================================================
# SECTION 4: Enhanced resolution — reconstruct Hamiltonian at interpolated k
# =============================================================================
print("\n--- Section 4: High-resolution Berry phase (interpolated k) ---")

# The 32 CG(24) k-points may be too coarse to resolve Berry phases at tight
# crossings. We reconstruct the Hamiltonian at interpolated k-values.
#
# H(k) = H_AA(block) + H_BB(k) + H_CC(k) + couplings
# where H_BB(k) = diag(E_sp) + V_bare + E_J * lambda(k) * I_8
# and lambda(k) is linearly interpolated between graph eigenvalues.

# Load additional data needed for Hamiltonian reconstruction
d_hess = np.load(SCRIPT_DIR / 's61_moduli_hessian.npz', allow_pickle=True)
evals_A_raw = d_hess['evals_36']
omega_A_sorted = np.sort(np.sqrt(np.abs(evals_A_raw)))

d_ed = np.load(SCRIPT_DIR / 's54_ed_sweep.npz', allow_pickle=True)
E_sp_sweep = d_ed['E_sp_sweep']
V_bare = d_ed['V_bare_cont']
fold_idx = int(d_ed['fold_idx'])
E_sp = E_sp_sweep[fold_idx]


def build_hamiltonian(lam_k):
    """Build the 45x45 Hamiltonian at graph Laplacian eigenvalue lam_k."""
    H = np.zeros((N_total, N_total))

    # Sector A: k-independent diagonal
    H[:N_A, :N_A] = np.diag(omega_A_sorted)

    # Sector B: 8x8 dispersive
    H_BB = np.diag(E_sp) + V_bare + E_J * lam_k * np.eye(N_B)
    H[N_A:N_A+N_B, N_A:N_A+N_B] = H_BB

    # Sector C: 1x1 dispersive
    omega_Lk = np.sqrt(omega_L0**2 + J_L * lam_k)
    H[N_A+N_B:, N_A+N_B:] = omega_Lk

    # A-B coupling
    H[:N_A, N_A:N_A+N_B] = V_AB
    H[N_A:N_A+N_B, :N_A] = V_AB.T

    # B-C coupling
    H[N_A:N_A+N_B, N_A+N_B:] = V_BC.reshape(-1, 1)
    H[N_A+N_B:, N_A:N_A+N_B] = V_BC.reshape(1, -1)

    # A-C coupling
    H[:N_A, N_A+N_B:] = V_AC.reshape(-1, 1)
    H[N_A+N_B:, :N_A] = V_AC.reshape(1, -1)

    return H


def berry_phase_highres(lam_values, band_idx):
    """
    Compute Berry phase for band `band_idx` along a sequence of lambda values
    by building and diagonalizing the Hamiltonian at each point.

    Returns: gamma, omega_path, evecs_path, overlaps
    """
    M = len(lam_values)
    evecs_path = np.zeros((M, N_total))
    omega_path = np.zeros(M)

    for j, lam in enumerate(lam_values):
        H = build_hamiltonian(lam)
        evals, evecs = eigh(H)
        evecs_path[j] = evecs[:, band_idx]
        omega_path[j] = evals[band_idx]

        # Fix sign ambiguity: ensure continuous gauge
        if j > 0:
            overlap = np.dot(evecs_path[j-1], evecs_path[j])
            if overlap < 0:
                evecs_path[j] *= -1

    gamma, overlaps = berry_phase_segment(evecs_path, periodic=False)
    return gamma, omega_path, evecs_path, overlaps


# High-resolution sweep for each of the 16 crossings
N_interp = 200  # points per crossing window

crossing_highres = []

for ic, cross in enumerate(tight_crossings):
    k_c = cross['k_idx']

    # Lambda window: interpolate lambda_n around the crossing
    W = 3  # (local)
    k_lo = max(0, k_c - W)
    k_hi = min(N_k - 1, k_c + W)

    lam_lo = lambda_n[k_lo]
    lam_hi = lambda_n[k_hi]

    # Dense lambda grid
    lam_dense = np.linspace(lam_lo, lam_hi, N_interp)

    # Find which band indices to track
    band_lo = crossing_results[ic]['band_lo']
    band_hi = crossing_results[ic]['band_hi']

    # Compute Berry phase at high resolution for both bands
    gamma_lo_hr, omega_lo_hr, evecs_lo_hr, overlaps_lo_hr = \
        berry_phase_highres(lam_dense, band_lo)
    gamma_hi_hr, omega_hi_hr, evecs_hi_hr, overlaps_hi_hr = \
        berry_phase_highres(lam_dense, band_hi)

    # Compute sector weights along the path
    sw_A_lo = np.array([np.sum(v[:N_A]**2) for v in evecs_lo_hr])
    sw_B_lo = np.array([np.sum(v[N_A:N_A+N_B]**2) for v in evecs_lo_hr])
    sw_A_hi = np.array([np.sum(v[:N_A]**2) for v in evecs_hi_hr])
    sw_B_hi = np.array([np.sum(v[N_A:N_A+N_B]**2) for v in evecs_hi_hr])

    # Berry curvature (discrete derivative of phase)
    # d(gamma)/d(lambda) at each point
    phases_lo = np.zeros(N_interp - 1)
    for j in range(N_interp - 1):
        overlap = np.dot(evecs_lo_hr[j], evecs_lo_hr[j+1])
        if abs(overlap) > 1e-15:
            phases_lo[j] = -np.imag(np.log(overlap / abs(overlap)))

    # Minimum gap along the dense path
    gap_dense = omega_hi_hr - omega_lo_hr
    min_gap_hr = gap_dense.min()
    min_gap_idx = np.argmin(gap_dense)

    # Total sector weight swap
    sw_swap_A = abs(sw_A_lo[-1] - sw_A_lo[0])
    sw_swap_B = abs(sw_B_lo[-1] - sw_B_lo[0])

    # Store
    hr_result = {
        'crossing_idx': ic,
        'gamma_lo': gamma_lo_hr,
        'gamma_hi': gamma_hi_hr,
        'min_gap': min_gap_hr,
        'min_overlap_lo': overlaps_lo_hr.min(),
        'min_overlap_hi': overlaps_hi_hr.min(),
        'sw_swap_A': sw_swap_A,
        'sw_swap_B': sw_swap_B,
        'max_A_weight_lo': sw_A_lo.max(),
        'max_B_weight_lo': sw_B_lo.max(),
        'omega_lo': omega_lo_hr,
        'omega_hi': omega_hi_hr,
        'gap_dense': gap_dense,
        'lam_dense': lam_dense,
        'phases_lo': phases_lo,
    }
    crossing_highres.append(hr_result)

    flag = ""
    if abs(gamma_lo_hr) > 0.1 * PI or abs(gamma_hi_hr) > 0.1 * PI:
        flag = " *** TOPOLOGICAL"
    print(f"\nCrossing [{ic:2d}] HIGH-RES ({N_interp} pts):")
    print(f"  gamma_lo = {gamma_lo_hr:+.6f} ({gamma_lo_hr/PI:+.4f}*pi)")
    print(f"  gamma_hi = {gamma_hi_hr:+.6f} ({gamma_hi_hr/PI:+.4f}*pi)")
    print(f"  min_gap = {min_gap_hr:.6f} M_KK")
    print(f"  min_overlap: lo={hr_result['min_overlap_lo']:.6f}, "
          f"hi={hr_result['min_overlap_hi']:.6f}")
    print(f"  sw_swap: A={sw_swap_A:.4f}, B={sw_swap_B:.4f}")
    print(f"  max(sw_A_lo)={sw_A_lo.max():.4f}, max(sw_B_lo)={sw_B_lo.max():.4f}{flag}")

# =============================================================================
# SECTION 5: Total Zak phase (high-resolution full BZ sweep)
# =============================================================================
print("\n--- Section 5: Full-BZ high-resolution Zak phases ---")

# Sweep lambda from 0 to lambda_max with dense grid
N_BZ = 500
lam_BZ = np.linspace(lambda_n[0], lambda_n[-1], N_BZ)

# Build and diagonalize at all points
evals_BZ = np.zeros((N_BZ, N_total))
evecs_BZ = np.zeros((N_BZ, N_total, N_total))

for j, lam in enumerate(lam_BZ):
    H = build_hamiltonian(lam)
    ev, ec = eigh(H)
    evals_BZ[j] = ev
    evecs_BZ[j] = ec.T  # Now evecs_BZ[j, n, :] = n-th eigenvector at j-th lambda

# Fix gauge for each band
for n in range(N_total):
    for j in range(1, N_BZ):
        overlap = np.dot(evecs_BZ[j-1, n, :], evecs_BZ[j, n, :])
        if overlap < 0:
            evecs_BZ[j, n, :] *= -1

# Compute Zak phase for each band
zak_highres = np.zeros(N_total)
zak_min_overlap_hr = np.zeros(N_total)

for n in range(N_total):
    band_evecs = evecs_BZ[:, n, :]  # (N_BZ, 45)
    gamma, overlaps = berry_phase_segment(band_evecs, periodic=False)
    zak_highres[n] = gamma
    zak_min_overlap_hr[n] = overlaps.min()

print(f"High-res Zak phases ({N_BZ} points, full BZ):")
n_topo = 0
for n in range(N_total):
    flag = " ***" if abs(zak_highres[n]) > 0.1 * PI else ""
    if flag:
        n_topo += 1
    print(f"  Band {n:2d}: gamma = {zak_highres[n]:+.6f} ({zak_highres[n]/PI:+.4f}*pi), "
          f"min_overlap = {zak_min_overlap_hr[n]:.6f}{flag}")

print(f"\nBands with |Zak phase| > 0.1*pi: {n_topo}/{N_total}")
print(f"Bands with |Zak phase| > 0.5*pi: {np.sum(np.abs(zak_highres) > 0.5 * PI)}/{N_total}")

# =============================================================================
# SECTION 6: Wilson loop / Z_2 invariant
# =============================================================================
print("\n--- Section 6: Wilson loop and Z_2 analysis ---")

# For a real symmetric Hamiltonian (time-reversal invariant, T^2 = +1),
# the Berry phase is constrained:
#   - Each band: Zak phase is 0 or pi (mod 2*pi) for a periodic path
#   - For an open path: no strict quantization, but near-quantized values
#     indicate proximity to a topological transition
#
# Wilson loop: W = prod_{k} <psi_n(k)|psi_n(k+dk)>
# The phase of W is the Zak phase.

# Compute Wilson loop for each band
wilson_phases = np.zeros(N_total)
for n in range(N_total):
    band_evecs = evecs_BZ[:, n, :]
    W = 1.0 + 0.0j  # (local)
    for j in range(N_BZ - 1):
        overlap = np.dot(band_evecs[j], band_evecs[j+1])
        W *= (overlap + 0.0j)
    wilson_phases[n] = np.angle(W)

print("Wilson loop phases:")
for n in range(N_total):
    flag = " ***" if abs(wilson_phases[n]) > 0.1 * PI else ""
    print(f"  Band {n:2d}: phi_W = {wilson_phases[n]:+.6f} ({wilson_phases[n]/PI:+.4f}*pi){flag}")

# Z_2 invariant: product of signs of Wilson loop at TRIM points
# For 1D, the Z_2 = (-1)^{n_occupied below gap} for occupied bands below
# each gap. This gives the parity of the Zak phase sum.
print(f"\nCumulative Zak phase (sum over bands 0..n):")
cum_zak = np.cumsum(zak_highres)
for n in range(N_total):
    z2 = int(round(cum_zak[n] / PI)) % 2
    print(f"  Sum(0..{n:2d}) = {cum_zak[n]:+.6f} ({cum_zak[n]/PI:+.4f}*pi), Z_2 parity = {z2}")

# =============================================================================
# SECTION 7: Non-Abelian Berry phase (2x2 subspace at crossings)
# =============================================================================
print("\n--- Section 7: Non-Abelian Berry phase at crossings ---")

# At each avoided crossing, the two participating bands form a 2D subspace.
# The non-Abelian Berry phase is a 2x2 unitary matrix:
#   W_mn = prod_k <psi_m(k)|psi_n(k+dk)>  for m,n in {lo, hi}
#
# Its eigenvalues are e^{i*theta_1} and e^{i*theta_2}.
# The non-Abelian Berry phase theta_1 - theta_2 measures the relative
# rotation of the two bands through the crossing.

na_berry_results = []

for ic, cross in enumerate(tight_crossings):
    hr = crossing_highres[ic]
    band_lo = crossing_results[ic]['band_lo']
    band_hi = crossing_results[ic]['band_hi']

    # Use the dense lambda grid from the high-res computation
    lam_dense = hr['lam_dense']
    N_pts = len(lam_dense)

    # Build eigenvectors along the path for the 2-band subspace
    evecs_2band = np.zeros((N_pts, 2, N_total))  # [k, band_in_subspace, component]

    for j, lam in enumerate(lam_dense):
        H = build_hamiltonian(lam)
        ev, ec = eigh(H)
        evecs_2band[j, 0, :] = ec[:, band_lo]
        evecs_2band[j, 1, :] = ec[:, band_hi]

    # Fix gauge for both bands
    for b in range(2):
        for j in range(1, N_pts):
            overlap = np.dot(evecs_2band[j-1, b, :], evecs_2band[j, b, :])
            if overlap < 0:
                evecs_2band[j, b, :] *= -1

    # Non-Abelian Wilson loop: 2x2 matrix product
    W_na = np.eye(2)
    for j in range(N_pts - 1):
        # Overlap matrix: F_mn = <psi_m(k)|psi_n(k+dk)>
        F = np.zeros((2, 2))
        for m in range(2):
            for n in range(2):
                F[m, n] = np.dot(evecs_2band[j, m, :], evecs_2band[j+1, n, :])
        # Regularize: SVD to get closest unitary
        U_svd, _, Vh_svd = np.linalg.svd(F)
        F_unitary = U_svd @ Vh_svd
        W_na = W_na @ F_unitary

    # Eigenvalues of Wilson loop matrix
    w_eigs = np.linalg.eigvals(W_na)
    w_phases = np.sort(np.angle(w_eigs))
    na_phase_diff = abs(w_phases[1] - w_phases[0])

    # Determinant phase (total U(1) phase)
    det_phase = np.angle(np.linalg.det(W_na))

    na_result = {
        'crossing_idx': ic,
        'wilson_eigs': w_eigs,
        'wilson_phases': w_phases,
        'na_phase_diff': na_phase_diff,
        'det_phase': det_phase,
        'det_W': np.linalg.det(W_na),
    }
    na_berry_results.append(na_result)

    flag = ""
    if na_phase_diff > 0.1 * PI:
        flag = " *** NON-ABELIAN TOPOLOGICAL"
    print(f"\nCrossing [{ic:2d}] Non-Abelian Wilson loop:")
    print(f"  W eigenvalues: {w_eigs}")
    print(f"  W phases: {w_phases[0]/PI:+.4f}*pi, {w_phases[1]/PI:+.4f}*pi")
    print(f"  Phase difference: {na_phase_diff:.6f} ({na_phase_diff/PI:.4f}*pi)")
    print(f"  det(W) = {np.linalg.det(W_na):.6f} (should be ~1)")
    print(f"  det phase = {det_phase:.6f} ({det_phase/PI:.4f}*pi){flag}")

# =============================================================================
# SECTION 8: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Gate Verdict")
print("=" * 78)

# Collect all Berry phases
gamma_local_lo = np.array([r['gamma_lo'] for r in crossing_highres])
gamma_local_hi = np.array([r['gamma_hi'] for r in crossing_highres])
na_phase_diffs = np.array([r['na_phase_diff'] for r in na_berry_results])

# Gate threshold: |gamma| > 0.1 * pi
threshold = 0.1 * PI  # (local)

# Check Abelian Berry phases at crossings (high-res)
n_topo_lo = np.sum(np.abs(gamma_local_lo) > threshold)
n_topo_hi = np.sum(np.abs(gamma_local_hi) > threshold)
max_gamma_lo = np.max(np.abs(gamma_local_lo))
max_gamma_hi = np.max(np.abs(gamma_local_hi))
max_gamma_crossing = max(max_gamma_lo, max_gamma_hi)
which_max_lo = np.argmax(np.abs(gamma_local_lo))
which_max_hi = np.argmax(np.abs(gamma_local_hi))

# Check non-Abelian phase differences
n_na_topo = np.sum(na_phase_diffs > threshold)
max_na = np.max(na_phase_diffs)
which_na_max = np.argmax(na_phase_diffs)

# Check full-BZ Zak phases
n_zak_topo = np.sum(np.abs(zak_highres) > threshold)
max_zak = np.max(np.abs(zak_highres))
which_zak_max = np.argmax(np.abs(zak_highres))

print(f"\n--- Abelian Berry phase (local, high-res) ---")
print(f"  Lower band: {n_topo_lo}/{N_cross} crossings with |gamma| > 0.1*pi")
print(f"  Upper band: {n_topo_hi}/{N_cross} crossings with |gamma| > 0.1*pi")
print(f"  Max |gamma_lo| = {max_gamma_lo:.6f} ({max_gamma_lo/PI:.4f}*pi) at crossing [{which_max_lo}]")
print(f"  Max |gamma_hi| = {max_gamma_hi:.6f} ({max_gamma_hi/PI:.4f}*pi) at crossing [{which_max_hi}]")

print(f"\n--- Non-Abelian Berry phase ---")
print(f"  {n_na_topo}/{N_cross} crossings with phase difference > 0.1*pi")
print(f"  Max phase diff = {max_na:.6f} ({max_na/PI:.4f}*pi) at crossing [{which_na_max}]")

print(f"\n--- Full-BZ Zak phase ---")
print(f"  {n_zak_topo}/{N_total} bands with |Zak phase| > 0.1*pi")
print(f"  Max |Zak| = {max_zak:.6f} ({max_zak/PI:.4f}*pi) at band {which_zak_max}")

# Determine gate verdict
any_topological = (n_topo_lo > 0 or n_topo_hi > 0 or n_na_topo > 0 or n_zak_topo > 0)

if any_topological:
    verdict = "PASS"
    detail = (f"PASS: Topological charge detected. "
              f"Abelian: {n_topo_lo + n_topo_hi} crossings with |gamma| > 0.1*pi "
              f"(max {max_gamma_crossing/PI:.4f}*pi). "
              f"Non-Abelian: {n_na_topo} crossings with phase diff > 0.1*pi "
              f"(max {max_na/PI:.4f}*pi). "
              f"Zak: {n_zak_topo} bands with |gamma| > 0.1*pi "
              f"(max {max_zak/PI:.4f}*pi).")
else:
    verdict = "INFO"
    detail = (f"INFO: No topological charge. "
              f"Max Abelian |gamma| = {max_gamma_crossing/PI:.4f}*pi < 0.1*pi. "
              f"Max non-Abelian diff = {max_na/PI:.4f}*pi < 0.1*pi. "
              f"Max Zak = {max_zak/PI:.4f}*pi < 0.1*pi. "
              f"All crossings adiabatic — hybridization gaps too large for topological charge.")

print(f"\n{'='*78}")
print(f"GATE: BERRY-KTHEORY-63 | W5-02 | {verdict}")
print(f"  {detail}")
print(f"{'='*78}")

# =============================================================================
# SECTION 9: Save results
# =============================================================================
print("\n--- Section 9: Save results ---")

# Pack crossing results into arrays
gamma_lo_arr = np.array([r['gamma_lo'] for r in crossing_results])
gamma_hi_arr = np.array([r['gamma_hi'] for r in crossing_results])
theta_mix_arr = np.array([r['theta_mix'] for r in crossing_results])
gap_arr = np.array([r['gap'] for r in crossing_results])
band_lo_arr = np.array([r['band_lo'] for r in crossing_results])
band_hi_arr = np.array([r['band_hi'] for r in crossing_results])
b_mode_arr = np.array([r['b_mode'] for r in crossing_results])
k_idx_arr = np.array([r['k_idx'] for r in crossing_results])

# High-res results
gamma_lo_hr_arr = np.array([r['gamma_lo'] for r in crossing_highres])
gamma_hi_hr_arr = np.array([r['gamma_hi'] for r in crossing_highres])
min_gap_hr_arr = np.array([r['min_gap'] for r in crossing_highres])
sw_swap_A_arr = np.array([r['sw_swap_A'] for r in crossing_highres])

# Non-Abelian results
na_phase_diff_arr = np.array([r['na_phase_diff'] for r in na_berry_results])
na_det_phase_arr = np.array([r['det_phase'] for r in na_berry_results])

np.savez(OUT_NPZ,
    # Coarse (32-pt) Berry phases
    zak_phases=zak_phases,
    zak_overlaps_min=zak_overlaps_min,
    # High-res (500-pt) Zak phases
    zak_highres=zak_highres,
    zak_min_overlap_hr=zak_min_overlap_hr,
    # Wilson loop phases
    wilson_phases=wilson_phases,
    # Crossing results (coarse)
    gamma_lo_coarse=gamma_lo_arr,
    gamma_hi_coarse=gamma_hi_arr,
    theta_mix=theta_mix_arr,
    crossing_gap=gap_arr,
    crossing_band_lo=band_lo_arr,
    crossing_band_hi=band_hi_arr,
    crossing_b_mode=b_mode_arr,
    crossing_k_idx=k_idx_arr,
    # Crossing results (high-res)
    gamma_lo_highres=gamma_lo_hr_arr,
    gamma_hi_highres=gamma_hi_hr_arr,
    min_gap_highres=min_gap_hr_arr,
    sw_swap_A=sw_swap_A_arr,
    # Non-Abelian results
    na_phase_diff=na_phase_diff_arr,
    na_det_phase=na_det_phase_arr,
    # Gate
    gate_name=np.array(['BERRY-KTHEORY-63']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 10: Plots
# =============================================================================
print("\n--- Section 10: Plots ---")

fig = plt.figure(figsize=(20, 16))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.30)

# --- Panel (0,0): Full-BZ Zak phases ---
ax1 = fig.add_subplot(gs[0, 0])
colors = ['red' if abs(z) > threshold else 'steelblue' for z in zak_highres]
ax1.bar(range(N_total), zak_highres / PI, color=colors, width=0.8, alpha=0.7)
ax1.axhline(y=0.1, color='gray', linestyle='--', alpha=0.5, label=r'$\pm 0.1\pi$')
ax1.axhline(y=-0.1, color='gray', linestyle='--', alpha=0.5)
ax1.set_xlabel('Band index')
ax1.set_ylabel(r'Zak phase / $\pi$')
ax1.set_title(f'Full-BZ Zak Phases (500 pts)\n{n_zak_topo} bands > 0.1*pi')
ax1.legend(fontsize=8)

# --- Panel (0,1): Local Berry phase at crossings ---
ax2 = fig.add_subplot(gs[0, 1])
x_cross = np.arange(N_cross)
ax2.bar(x_cross - 0.2, gamma_lo_hr_arr / PI, width=0.35, color='steelblue',
        label='Lower band', alpha=0.7)
ax2.bar(x_cross + 0.2, gamma_hi_hr_arr / PI, width=0.35, color='coral',
        label='Upper band', alpha=0.7)
ax2.axhline(y=0.1, color='gray', linestyle='--', alpha=0.5)
ax2.axhline(y=-0.1, color='gray', linestyle='--', alpha=0.5)
ax2.set_xlabel('Crossing index')
ax2.set_ylabel(r'Berry phase / $\pi$')
ax2.set_title(f'Local Berry Phase at 16 Crossings\n(high-res, {N_interp} pts)')
ax2.legend(fontsize=8)
ax2.set_xticks(x_cross)

# --- Panel (0,2): Non-Abelian phase difference ---
ax3 = fig.add_subplot(gs[0, 2])
colors_na = ['red' if p > threshold else 'steelblue' for p in na_phase_diff_arr]
ax3.bar(x_cross, na_phase_diff_arr / PI, color=colors_na, width=0.6, alpha=0.7)
ax3.axhline(y=0.1, color='gray', linestyle='--', alpha=0.5, label=r'$0.1\pi$ threshold')
ax3.set_xlabel('Crossing index')
ax3.set_ylabel(r'Non-Abelian phase diff / $\pi$')
ax3.set_title(f'Non-Abelian Berry Phase\n{n_na_topo} crossings > 0.1*pi')
ax3.set_xticks(x_cross)
ax3.legend(fontsize=8)

# --- Panel (1,0): Band structure near strongest crossing ---
# Pick the crossing with largest Berry phase
if len(crossing_highres) > 0:
    best_idx = np.argmax(np.abs(gamma_lo_hr_arr) + np.abs(gamma_hi_hr_arr))
    hr = crossing_highres[best_idx]

    ax4 = fig.add_subplot(gs[1, 0])
    ax4.plot(hr['lam_dense'], hr['omega_lo'], 'b-', linewidth=1.5, label='Lower band')
    ax4.plot(hr['lam_dense'], hr['omega_hi'], 'r-', linewidth=1.5, label='Upper band')
    ax4.fill_between(hr['lam_dense'], hr['omega_lo'], hr['omega_hi'],
                     alpha=0.1, color='purple')  # (local)
    ax4.set_xlabel(r'$\lambda$ (graph Laplacian eigenvalue)')
    ax4.set_ylabel(r'$\omega$ (M_KK)')
    ax4.set_title(f'Avoided Crossing [{best_idx}]\nmin gap = {hr["min_gap"]:.4f} M_KK')
    ax4.legend(fontsize=8)

# --- Panel (1,1): Gap vs lambda for strongest crossing ---
if len(crossing_highres) > 0:
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.plot(hr['lam_dense'], hr['gap_dense'], 'k-', linewidth=1.5)
    ax5.axhline(y=hr['min_gap'], color='red', linestyle='--', alpha=0.5,
                label=f'min = {hr["min_gap"]:.4f}')
    ax5.set_xlabel(r'$\lambda$ (graph Laplacian eigenvalue)')
    ax5.set_ylabel('Gap (M_KK)')
    ax5.set_title(f'Gap Through Crossing [{best_idx}]')
    ax5.legend(fontsize=8)

# --- Panel (1,2): Berry curvature (phase density) for strongest crossing ---
if len(crossing_highres) > 0:
    ax6 = fig.add_subplot(gs[1, 2])
    lam_mid = 0.5 * (hr['lam_dense'][:-1] + hr['lam_dense'][1:])
    ax6.plot(lam_mid, hr['phases_lo'] / PI, 'b-', linewidth=1, alpha=0.7)
    ax6.set_xlabel(r'$\lambda$ (graph Laplacian eigenvalue)')
    ax6.set_ylabel(r'$d\gamma / d\lambda$ ($\pi$ units)')
    ax6.set_title(f'Berry Curvature Density\nCrossing [{best_idx}]')
    ax6.axhline(y=0, color='gray', linestyle='-', alpha=0.3)

# --- Panel (2,0): Mixing angle at crossings ---
ax7 = fig.add_subplot(gs[2, 0])
ax7.bar(x_cross, theta_mix_arr / PI, color='teal', width=0.6, alpha=0.7)
ax7.axhline(y=0.25, color='red', linestyle='--', alpha=0.5, label=r'$\pi/4$ (max mixing)')
ax7.set_xlabel('Crossing index')
ax7.set_ylabel(r'Mixing angle / $\pi$')
ax7.set_title('Sector Mixing Angle at Crossings')
ax7.set_xticks(x_cross)
ax7.legend(fontsize=8)

# --- Panel (2,1): Gap vs detuning correlation ---
ax8 = fig.add_subplot(gs[2, 1])
dets = np.array([tc['min_detuning'] for tc in tight_crossings])
gaps = gap_arr
ax8.scatter(dets, gaps, c=np.abs(gamma_lo_hr_arr) / PI, cmap='hot',
            s=60, edgecolors='k', linewidths=0.5)
cb = plt.colorbar(ax8.collections[0], ax=ax8)
cb.set_label(r'$|\gamma_{lo}|/\pi$')
ax8.set_xlabel('Detuning (M_KK)')
ax8.set_ylabel('Gap (M_KK)')
ax8.set_title('Gap vs Detuning\n(color = Berry phase)')

# --- Panel (2,2): Cumulative Zak phase ---
ax9 = fig.add_subplot(gs[2, 2])
ax9.plot(range(N_total), cum_zak / PI, 'k-', linewidth=1.5)
ax9.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
for n in range(N_total):
    if abs(zak_highres[n]) > threshold:
        ax9.axvline(x=n, color='red', linestyle='--', alpha=0.3)
ax9.set_xlabel('Band index')
ax9.set_ylabel(r'Cumulative Zak phase / $\pi$')
ax9.set_title('Cumulative Zak Phase\n(red = topological bands)')

fig.suptitle('BERRY-KTHEORY-63: Berry Phase at 16 Hybridization Crossings\n'
             f'Gate: {verdict}', fontsize=14, fontweight='bold', y=0.98)

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_PNG}")

# =============================================================================
# SECTION 11: Summary table
# =============================================================================
print("\n" + "=" * 78)
print("SUMMARY TABLE")
print("=" * 78)

print(f"\n{'Idx':>3} {'B':>2} {'k':>3} {'Gap':>8} {'Det':>8} "
      f"{'gamma_lo':>10} {'gamma_hi':>10} {'NA_diff':>10} {'theta_mix':>10} {'Topo':>5}")
print("-" * 78)
for ic in range(N_cross):
    tc = tight_crossings[ic]
    cr = crossing_results[ic]
    hr = crossing_highres[ic]
    na = na_berry_results[ic]
    topo = "YES" if (abs(hr['gamma_lo']) > threshold or
                     abs(hr['gamma_hi']) > threshold or
                     na['na_phase_diff'] > threshold) else "no"
    print(f"{ic:3d} {tc['b_mode']:2d} {tc['k_idx']:3d} {cr['gap']:8.4f} {tc['min_detuning']:8.4f} "
          f"{hr['gamma_lo']/PI:+10.4f}pi {hr['gamma_hi']/PI:+10.4f}pi "
          f"{na['na_phase_diff']/PI:10.4f}pi {cr['theta_mix']/PI:10.4f}pi "
          f"{topo:>5}")

elapsed = time.time() - t_start
print(f"\nTotal time: {elapsed:.1f}s")
print(f"\nDone.")
