#!/usr/bin/env python3
"""
Session 48 W5-G: QA/Tachyon/Remaining — 8 Sub-computations (QA-TACHYON-48)

Computes 8 carry-forward items from quantum-acoustics and tachyonic-transit analysis:
  1. BERRY-EDGE-48:       Topological edge states at tessellation boundaries
  2. DISSOLUTION-GOE-48:  SFF ramp onset vs dissolution epsilon
  3. VH-HIGHER-ORDER-48:  B2 van Hove protection at 4-phonon order
  4. B3-REPULSIVE-48:     B3 repulsive channel population inversion in GGE
  5. THREE-PHONON-48:     Resonant 3-phonon friction from omega_B2 ~ 2*omega_B1
  6. TRANSIT-279-48:      279-mode tachyonic transit velocity
  7. EIGENVECTOR-48:      (done separately in s48_eigenvectors.py)
  8. DEFECT-CORR-48:      Topological defect correlations and n_s prediction

Gate: QA-TACHYON-48 = INFO (batch of diverse computations)

Input:  s48_wilson_loop.npz, s35_thouless_multiband.npz, s38_level_spacing.npz,
        s44_dissolution_scaling.npz, s46_fabric_tessellation.npz, s46_pseudo_riemannian.npz
Output: s48_qa_tachyon.{npz,png}

Author: quantum-acoustics-theorist (Session 48 W5-G)
Date: 2026-03-17
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import eigh as scipy_eigh, eigvalsh as scipy_eigvalsh
from scipy.optimize import brentq
from scipy.special import zeta as riemann_zeta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold, E_cond, E_cond_ED_8mode, n_pairs, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean, Delta_0_GL, xi_BCS, xi_GL,
    M_max_thouless, S_inst, omega_PV, Gamma_Langer_BCS,
    N_cells, rho_B2_per_mode, M_KK, M_KK_gravity,
    dt_transit, v_terminal, H_fold, P_exc_kz, n_Bog,
    Delta_B3, E_exc_ratio, PI,
)

print("=" * 72)
print("Session 48 W5-G: QA/Tachyon/Remaining (QA-TACHYON-48)")
print("=" * 72)

# Load all input data
wilson_data = np.load(os.path.join(SCRIPT_DIR, 's48_wilson_loop.npz'), allow_pickle=True)
thouless_data = np.load(os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz'), allow_pickle=True)
level_data = np.load(os.path.join(SCRIPT_DIR, 's38_level_spacing.npz'), allow_pickle=True)
dissolution_data = np.load(os.path.join(SCRIPT_DIR, 's44_dissolution_scaling.npz'), allow_pickle=True)
tess_data = np.load(os.path.join(SCRIPT_DIR, 's46_fabric_tessellation.npz'), allow_pickle=True)
pseudo_data = np.load(os.path.join(SCRIPT_DIR, 's46_pseudo_riemannian.npz'), allow_pickle=True)

results = {}

# ============================================================================
# 1. BERRY-EDGE-48: Topological edge states at tessellation boundaries
# ============================================================================

print(f"\n{'='*72}")
print("1. BERRY-EDGE-48: Topological Edge States at Tessellation Boundaries")
print("=" * 72)

# Physics:
# The S48 Wilson loop found 47 total pi-phases (13 Abelian + 34 non-Abelian).
# The global Z_2 = (-1)^{47} = -1 (nontrivial). By bulk-boundary correspondence
# (Su-Schrieffer-Heeger paradigm for 1D Z_2 systems), each Z_2-nontrivial band
# should host a zero-energy edge state at the boundary between topologically
# distinct domains.
#
# In the 32-cell tessellation, each domain boundary is a wall between two
# KZ-frozen cells with potentially different tau orientations. The edge states
# live at these walls.
#
# Method: Construct a minimal 2-cell SSH-type model where each cell has the
# bulk Dirac spectrum, and the inter-cell coupling is the tessellation overlap.
# Diagonalize and look for in-gap edge states.

total_pi = int(wilson_data['total_pi'])
total_ab_pi = int(wilson_data['total_ab_pi'])
total_wl_pi = int(wilson_data['total_wl_pi'])
global_z2 = '+1' if float(wilson_data['global_det_real']) > 0 else '-1'

print(f"\n  Wilson loop input:")
print(f"    Total pi-phases: {total_pi} (13 Abelian + {total_wl_pi} Wilson)")
print(f"    Global Z_2: {global_z2}")
print(f"    PW-weighted pi: {int(wilson_data['total_pi_pw'])}")

# Construct SSH-like model for edge states.
# Each cell: 8 BCS modes at energies E_8 = {E_B1, 4*E_B2, 3*E_B3}
# The Z_2 phases from Wilson loop determine the sign of inter-cell hopping.
# For a pi-phase mode, the hopping acquires a sign flip across the domain wall.

E_8 = thouless_data['E_8']  # 8 mode energies
V_8x8 = thouless_data['V_sorted_pos']  # 8x8 V matrix (intra-cell)

# Branch classification
branch_labels = ['B1', 'B2', 'B2', 'B2', 'B2', 'B3', 'B3', 'B3']

# The inter-cell coupling at a tessellation boundary
# From S46 tessellation: alpha_tess is the tessellation parameter
# The inter-cell hopping t_ij scales as exp(-d_wall / xi_BCS)
# For 32 cells, the mean inter-cell distance ~ L_cell = (Vol_SU3)^{1/8} / N_cells^{1/8}
# In the 0D limit (L/xi_GL = 0.031), the inter-cell coupling is ~exp(-0.031)

L_over_xi = 0.031  # from S37
t_inter = np.exp(-L_over_xi)  # inter-cell hopping amplitude ~ 0.969

print(f"\n  Inter-cell coupling parameters:")
print(f"    L/xi_GL = {L_over_xi}")
print(f"    t_inter = exp(-L/xi) = {t_inter:.6f}")

# Construct 2-cell Hamiltonian (16 modes total: 8 per cell)
# H = [[H_cell, T], [T^dag, H_cell]]
# where H_cell = diag(E_8) + V_8x8 (intra-cell)
# and T_ij = t_inter * V_ij * sign_factor(pi-phase)

# Determine pi-phase structure per mode.
# From Wilson data: sectors contribute different numbers of pi-phases.
# For the 8-mode BCS space: B1 (1 mode), B2 (4 modes), B3 (3 modes)
# S46 found 13 Abelian pi-phases. Distributed across branches:
# B1: contributed pi-phases from (0,0), (1,0), (0,1) sectors
# B2: from (1,1) sector
# B3: from (2,0), (0,2), (3,0), (0,3), (2,1) sectors

# For the 8-mode BCS model, assign Z_2 = -1 to modes with pi-phase
# The 13 Abelian pi-phases and 34 Wilson pi-phases give 47 total.
# Per-branch from Wilson loop:
# We read directly the per-sector pi counts
pi_per_branch = {'B1': 0, 'B2': 0, 'B3': 0}
sectors_pq = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)]
branch_map = {
    (0,0): 'B1', (1,0): 'B1', (0,1): 'B1',
    (1,1): 'B2',
    (2,0): 'B3', (0,2): 'B3', (3,0): 'B3', (0,3): 'B3', (2,1): 'B3',
}

for pq in sectors_pq:
    p, q = pq
    prefix = f's{p}{q}'
    n_ab = int(wilson_data[f'{prefix}_n_ab_pi'])
    n_wl = int(wilson_data[f'{prefix}_n_wl_pi'])
    pi_per_branch[branch_map[pq]] += n_ab + n_wl

print(f"\n  Pi-phases by branch (from Wilson loop):")
for br in ['B1', 'B2', 'B3']:
    print(f"    {br}: {pi_per_branch[br]}")

# For the 8-mode SSH model: assign Z_2 signs.
# Each mode gets sign = (-1)^(fraction of pi-phases in its branch).
# This is a simplification: in reality, each mode individually either is or isn't pi.
# We model the AVERAGE: if branch has odd total pi-count, it's nontrivial.
z2_signs = []
for lab in branch_labels:
    z2_signs.append(-1 if pi_per_branch[lab] % 2 == 1 else +1)
z2_signs = np.array(z2_signs)

print(f"  Z_2 signs for 8 BCS modes: {z2_signs}")

# Construct Hamiltonians
H_cell = np.diag(E_8) + V_8x8  # 8x8 intra-cell

# Inter-cell hopping: T_ij = t_inter * V_ij * z2_i * z2_j
# The Z_2 sign affects the boundary condition
T_inter = t_inter * V_8x8 * np.outer(z2_signs, z2_signs)

# 2-cell Hamiltonian with open boundary conditions
H_2cell = np.zeros((16, 16))
H_2cell[:8, :8] = H_cell
H_2cell[8:, 8:] = H_cell
H_2cell[:8, 8:] = T_inter
H_2cell[8:, :8] = T_inter.T  # Hermitian

evals_2cell = scipy_eigvalsh(H_2cell)

# Reference: 1-cell bulk spectrum (repeated twice)
evals_1cell = scipy_eigvalsh(H_cell)
evals_bulk_ref = np.sort(np.concatenate([evals_1cell, evals_1cell]))

# Edge modes: eigenvalues that differ significantly from doubled bulk
edge_deviation = np.abs(evals_2cell - evals_bulk_ref)
edge_threshold = 0.01  # 1% of typical energy scale

n_edge_modes = np.sum(edge_deviation > edge_threshold)
max_edge_shift = np.max(edge_deviation)
mean_edge_shift = np.mean(edge_deviation)

print(f"\n  2-cell SSH model results:")
print(f"    Bulk spectrum (1-cell): {evals_1cell}")
print(f"    2-cell spectrum: {evals_2cell}")
print(f"    Edge deviation max: {max_edge_shift:.6f}")
print(f"    Edge deviation mean: {mean_edge_shift:.6f}")
print(f"    Modes with deviation > {edge_threshold}: {n_edge_modes}")

# For a proper edge-state analysis, construct a longer chain (N_cells = 32)
# and look for states localized at boundaries

N_chain = 32
H_chain = np.zeros((8*N_chain, 8*N_chain))
for i in range(N_chain):
    H_chain[8*i:8*(i+1), 8*i:8*(i+1)] = H_cell
    if i < N_chain - 1:
        # Alternate Z_2 sign to create a domain wall at i = N_chain//2
        if i < N_chain // 2:
            T = T_inter
        else:
            T = t_inter * V_8x8  # No Z_2 flip in second half
        H_chain[8*i:8*(i+1), 8*(i+1):8*(i+2)] = T
        H_chain[8*(i+1):8*(i+2), 8*i:8*(i+1)] = T.T

evals_chain, evecs_chain = scipy_eigh(H_chain)

# Find states localized near the domain wall (site = N_chain//2)
wall_site = N_chain // 2
localization = np.zeros(8*N_chain)
for n in range(8*N_chain):
    psi = evecs_chain[:, n]
    # Weight at domain wall sites
    wall_weight = np.sum(np.abs(psi[8*(wall_site-1):8*(wall_site+1)])**2)
    localization[n] = wall_weight

# Also weight at edges (sites 0 and N-1)
edge_weight = np.zeros(8*N_chain)
for n in range(8*N_chain):
    psi = evecs_chain[:, n]
    edge_weight[n] = (np.sum(np.abs(psi[:8])**2) +
                       np.sum(np.abs(psi[-8:])**2))

# Identify edge states: localization > 2x average
avg_loc = 2.0 / N_chain  # expected for uniform state
wall_states_mask = localization > 3 * avg_loc
edge_states_mask = edge_weight > 3 * avg_loc

n_wall_states = np.sum(wall_states_mask)
n_edge_states = np.sum(edge_states_mask)

print(f"\n  32-cell chain results:")
print(f"    Total modes: {8*N_chain}")
print(f"    Wall-localized states (>3x avg): {n_wall_states}")
print(f"    Edge-localized states (>3x avg): {n_edge_states}")
if n_wall_states > 0:
    wall_evals = evals_chain[wall_states_mask]
    print(f"    Wall-state energies: {wall_evals[:10]}")
    print(f"    Max wall localization: {np.max(localization):.4f} (avg={avg_loc:.4f})")
if n_edge_states > 0:
    edge_evals = evals_chain[edge_states_mask]
    print(f"    Edge-state energies: {edge_evals[:10]}")
    print(f"    Max edge weight: {np.max(edge_weight):.4f}")

# Dispersion: in a periodic chain, edge states have flat dispersion
# Check participation ratio: IPR = sum |psi_i|^4 / (sum |psi_i|^2)^2
ipr_all = np.zeros(8*N_chain)
for n in range(8*N_chain):
    psi = evecs_chain[:, n]
    prob = np.abs(psi)**2
    ipr_all[n] = np.sum(prob**2)  # Already normalized

ipr_mean = np.mean(ipr_all)
ipr_localized = ipr_all[wall_states_mask] if n_wall_states > 0 else np.array([])

print(f"\n  Inverse participation ratio:")
print(f"    Mean (all states): {ipr_mean:.6f}")
print(f"    Extended state IPR ~ 1/N: {1.0/(8*N_chain):.6f}")
if len(ipr_localized) > 0:
    print(f"    Wall-localized states: mean IPR = {np.mean(ipr_localized):.6f}")

results['berry_edge'] = {
    'total_pi': total_pi,
    'global_z2': global_z2,
    'pi_per_branch': pi_per_branch,
    'z2_signs': z2_signs,
    't_inter': t_inter,
    'n_wall_states': n_wall_states,
    'n_edge_states': n_edge_states,
    'max_edge_shift': max_edge_shift,
    'ipr_mean': ipr_mean,
    'evals_chain': evals_chain,
    'localization': localization,
    'edge_weight': edge_weight,
}

print(f"\n  BERRY-EDGE-48 VERDICT: INFO")
print(f"    Wall-localized states exist: {'YES' if n_wall_states > 0 else 'NO'}")
print(f"    Edge states exist: {'YES' if n_edge_states > 0 else 'NO'}")
print(f"    t_inter ~ 1 (0D limit): coupling too strong for gap opening")
print(f"    The 0D limit (L/xi=0.031) means inter-cell coupling is nearly maximal.")
print(f"    True edge physics requires L/xi >> 1 (NOT the case here).")


# ============================================================================
# 2. DISSOLUTION-GOE-48: SFF ramp onset vs dissolution epsilon
# ============================================================================

print(f"\n{'='*72}")
print("2. DISSOLUTION-GOE-48: Spectral Form Factor Ramp Onset")
print("=" * 72)

# Physics:
# S38 found the spectrum is Poisson (integrable, <r>=0.321->0.439 corrected in S46).
# Dissolution (spectral triple dissolving at large tau) introduces perturbation eps.
# Question: at what eps does Poisson -> GOE (Wigner-Dyson) transition occur?
# This determines whether the post-transit GGE thermalizes.
#
# S44 found: epsilon_crossover scales as 1/sqrt(N) with N = number of modes.
# We compute the spectral form factor SFF(t) = |Z(t)|^2 / |Z(0)|^2 at
# several epsilon values to find where the linear ramp (GOE signature) appears.

eps_crossover_arr = dissolution_data['epsilon_crossover']
max_pq_sums = dissolution_data['max_pq_sums']
N_values = dissolution_data['N_values']

print(f"\n  S44 dissolution data:")
print(f"    max_pq_sums: {max_pq_sums}")
print(f"    N_values: {N_values}")
print(f"    eps_crossover: {eps_crossover_arr}")

# At p+q <= 3 (our working truncation): N = 1232, eps_c = 0.00798
eps_c = float(eps_crossover_arr[2])  # p+q<=3
N_modes = int(N_values[2])

print(f"\n  Working truncation (p+q<=3):")
print(f"    N = {N_modes}")
print(f"    eps_c = {eps_c:.6f}")

# Spectral form factor for the 8-mode BCS spectrum + random perturbation
# SFF(t) = <|sum_n exp(-i E_n t)|^2> / N^2
# For Poisson: SFF(t) = 1 (no ramp)
# For GOE: SFF(t) ~ t/t_H for t < t_H (Heisenberg time), then SFF = 1

eps_scan = np.array([0, 0.1, 0.3, 0.5, 1.0]) * eps_c
n_realizations = 200
n_t = 500
t_max_sff = 200.0  # In units of mean level spacing
t_sff = np.linspace(0.01, t_max_sff, n_t)

sff_results = {}

for eps in eps_scan:
    sff_avg = np.zeros(n_t)
    for real in range(n_realizations):
        # Perturb the 8-mode spectrum with GOE noise of strength eps
        H_pert = np.diag(E_8) + V_8x8
        if eps > 0:
            noise = np.random.randn(8, 8)
            noise = (noise + noise.T) / 2  # Symmetrize
            noise *= eps / np.sqrt(8)  # Scale by eps/sqrt(N)
            H_pert = H_pert + noise
        evals_pert = scipy_eigvalsh(H_pert)
        # Mean level spacing
        spacings = np.diff(evals_pert)
        mean_spacing = np.mean(spacings) if len(spacings) > 0 else 1.0
        # SFF
        for it, t in enumerate(t_sff):
            Z = np.sum(np.exp(-1j * evals_pert * t / mean_spacing))
            sff_avg[it] += np.abs(Z)**2
    sff_avg /= (n_realizations * 8**2)  # Normalize by N^2
    sff_results[eps] = sff_avg

# Detect ramp onset: SFF grows linearly from ~0 to ~1 between t_Thouless and t_H
# For Poisson, SFF ~ 1 + (N-1)/N = 1 at all t (disconnect = 0)
# For GOE, SFF ~ (2t - t ln(2t+1))/(2*pi*t_H) for t < t_H

# Find where SFF first exceeds 0.1 above the Poisson baseline (disconnect)
ramp_onset_eps = {}
for eps in eps_scan:
    sff = sff_results[eps]
    # The Poisson baseline for 8 modes is ~1/8 + 7/8 * delta(t)
    # At finite t, Poisson SFF oscillates around 1 (connected) + 1/N (disconnected)
    # Ramp signature: monotonically increasing region
    # Check for sustained increase
    window = 20
    ramp_found = False
    for it in range(window, n_t - window):
        # Check if SFF is increasing over window
        slope = np.polyfit(t_sff[it-window:it+window], sff[it-window:it+window], 1)[0]
        if slope > 0.002 and sff[it] > 0.2:  # Positive slope and above noise
            ramp_onset_eps[eps] = t_sff[it]
            ramp_found = True
            break
    if not ramp_found:
        ramp_onset_eps[eps] = -1  # No ramp detected

print(f"\n  Spectral Form Factor analysis (8-mode, {n_realizations} realizations):")
print(f"  {'eps/eps_c':>10s} | {'eps':>10s} | {'ramp_onset':>12s} | {'SFF(t=100)':>10s}")
print(f"  {'-'*50}")
for eps in eps_scan:
    ratio = eps / eps_c if eps_c > 0 else 0
    onset = ramp_onset_eps[eps]
    sff_late = sff_results[eps][-1]
    onset_str = f"{onset:.1f}" if onset > 0 else "NONE"
    print(f"  {ratio:>10.2f} | {eps:>10.6f} | {onset_str:>12s} | {sff_late:>10.4f}")

# r-ratio from the 8-mode perturbed spectrum
r_ratios = {}
for eps in eps_scan:
    r_vals = []
    for real in range(n_realizations):
        H_pert = np.diag(E_8) + V_8x8
        if eps > 0:
            noise = np.random.randn(8, 8)
            noise = (noise + noise.T) / 2
            noise *= eps / np.sqrt(8)
            H_pert = H_pert + noise
        evals_pert = np.sort(scipy_eigvalsh(H_pert))
        spacings = np.diff(evals_pert)
        if len(spacings) >= 2:
            ratios = np.minimum(spacings[:-1], spacings[1:]) / np.maximum(spacings[:-1], spacings[1:])
            r_vals.append(np.mean(ratios))
    r_ratios[eps] = np.mean(r_vals) if r_vals else 0

r_poisson = 2 * np.log(2) - 1  # = 0.3863
r_goe = 0.5307

print(f"\n  Level spacing ratio <r> vs perturbation:")
print(f"  {'eps/eps_c':>10s} | {'<r>':>8s} | {'Poisson':>8s} | {'GOE':>8s} | status")
print(f"  {'-'*55}")
for eps in eps_scan:
    ratio = eps / eps_c if eps_c > 0 else 0
    r = r_ratios[eps]
    if r < (r_poisson + r_goe) / 2:
        status = "Poisson"
    else:
        status = "GOE"
    print(f"  {ratio:>10.2f} | {r:>8.4f} | {r_poisson:>8.4f} | {r_goe:>8.4f} | {status}")

# Find crossover epsilon where <r> = midpoint
r_mid = (r_poisson + r_goe) / 2
eps_ratios = list(eps_scan)
r_values = [r_ratios[e] for e in eps_scan]

# Find where r crosses midpoint
crossover_found = False
eps_sff_crossover = -1
for i in range(len(r_values)-1):
    if r_values[i] < r_mid <= r_values[i+1]:
        # Linear interpolation
        frac = (r_mid - r_values[i]) / (r_values[i+1] - r_values[i])
        eps_sff_crossover = eps_ratios[i] + frac * (eps_ratios[i+1] - eps_ratios[i])
        crossover_found = True
        break

if crossover_found:
    print(f"\n  Poisson->GOE crossover at eps = {eps_sff_crossover:.6f} = {eps_sff_crossover/eps_c:.3f} * eps_c")
else:
    print(f"\n  No Poisson->GOE crossover detected in scan range [0, eps_c].")
    # Check if we're already GOE at eps=0
    if r_values[0] > r_mid:
        print(f"  System is ALREADY near GOE at eps=0 (V_8x8 coupling is non-perturbative).")
        eps_sff_crossover = 0.0

results['dissolution_goe'] = {
    'eps_c': eps_c,
    'N_modes': N_modes,
    'eps_scan': eps_scan,
    'sff_results': {float(k): v for k, v in sff_results.items()},
    'r_ratios': {float(k): v for k, v in r_ratios.items()},
    'ramp_onset': {float(k): v for k, v in ramp_onset_eps.items()},
    'eps_crossover_sff': eps_sff_crossover,
    't_sff': t_sff,
}

print(f"\n  DISSOLUTION-GOE-48 VERDICT: INFO")


# ============================================================================
# 3. VH-HIGHER-ORDER-48: B2 van Hove at 4-phonon scattering
# ============================================================================

print(f"\n{'='*72}")
print("3. VH-HIGHER-ORDER-48: B2 Van Hove Protection at 4-Phonon Order")
print("=" * 72)

# Physics:
# The 2-phonon scattering matrix V(B2,B2) is non-zero (S35).
# Question: does the 4-phonon process V(B2,B2,B2,B2) vanish by selection rules?
# If it does, topological protection extends to next order.
#
# The 4-phonon vertex is the quartic correction to the spectral action:
#   V_4 = d^4 S / d(Delta)^4 evaluated at the B2 sector.
# By the constant-ratio trap (F/B = 0.55), the spectral action trace
# is invariant under U(1)_7 rotations. But the BCS kernel V_ij is NOT
# a trace functional.
#
# Selection rule analysis:
# B2 modes live in (1,1) irrep of SU(3) with C_2 = 4/3.
# The 4-phonon process requires: (1,1) x (1,1) x (1,1) x (1,1) contains trivial.
# Clebsch-Gordan: (1,1) x (1,1) = (0,0) + (1,1) + (2,2) + (2,0) + (0,2) + (3,0) + (0,3)
# So ((1,1) x (1,1)) x ((1,1) x (1,1)) definitely contains (0,0).
# Selection rule does NOT forbid 4-phonon B2 scattering.

V_B2B2 = V_8x8[1:5, 1:5]  # B2 block (modes 1-4 are B2)

print(f"\n  V_B2B2 (2-phonon, from S35):")
print(f"    V_B2B2 =")
for i in range(4):
    print(f"      [{', '.join(f'{V_B2B2[i,j]:+.6f}' for j in range(4))}]")
print(f"    max|V_B2B2| = {np.max(np.abs(V_B2B2)):.6f}")
print(f"    Frobenius norm = {np.linalg.norm(V_B2B2, 'fro'):.6f}")

# Check if V_B2B2 has the Schur (irreducible) structure
# By Schur's lemma on (1,1): if the coupling is SU(3)-invariant,
# V_B2B2 should be proportional to the identity.
V_diag = np.mean(np.diag(V_B2B2))
V_offdiag_rms = np.sqrt(np.mean((V_B2B2 - V_diag * np.eye(4))**2))

print(f"\n  Schur analysis of V_B2B2:")
print(f"    Diagonal mean: {V_diag:.6f}")
print(f"    Off-diagonal RMS deviation from Schur: {V_offdiag_rms:.6f}")
print(f"    Ratio (dev/diag): {V_offdiag_rms/abs(V_diag):.4f}")

# 4-phonon matrix element: V_4 = sum_{k,l} V_{ik} V_{kl} V_{lj}
# This is V_B2B2^3 (third power of the coupling matrix)
V2 = V_B2B2 @ V_B2B2
V3 = V2 @ V_B2B2  # V^3 = effective 4-phonon vertex

print(f"\n  4-phonon effective vertex V^3_B2B2:")
print(f"    max|V^3| = {np.max(np.abs(V3)):.8f}")
print(f"    Frobenius norm(V^3) = {np.linalg.norm(V3, 'fro'):.8f}")

# The ratio V^3/V tells us if higher-order scattering is suppressed
ratio_4to2 = np.linalg.norm(V3, 'fro') / np.linalg.norm(V_B2B2, 'fro')
print(f"    ||V^3||/||V|| = {ratio_4to2:.6f}")

# Eigenvalue analysis of V_B2B2 for scattering channels
evals_VB2 = np.sort(scipy_eigvalsh(V_B2B2))
print(f"\n  V_B2B2 eigenvalues (scattering channels):")
for i, ev in enumerate(evals_VB2):
    print(f"    channel {i}: {ev:+.6f}")

# 4-phonon eigenvalues (cube of 2-phonon eigenvalues)
evals_V3 = evals_VB2**3
print(f"\n  4-phonon eigenvalues (lambda^3):")
for i, ev in enumerate(evals_V3):
    print(f"    channel {i}: {ev:+.8f}")

# Check if any channel vanishes
min_4phonon = np.min(np.abs(evals_V3))
print(f"\n  Minimum |4-phonon eigenvalue|: {min_4phonon:.8f}")
print(f"  Protection by selection rule: {'NO' if min_4phonon > 1e-10 else 'YES (channel vanishes)'}")

# Check full 8x8 4-phonon
V4_full = V_8x8 @ V_8x8 @ V_8x8
V4_B2B2 = V4_full[1:5, 1:5]
print(f"\n  Full 8x8 V^3 restricted to B2:")
print(f"    max|V4_B2B2| = {np.max(np.abs(V4_B2B2)):.8f}")
print(f"    This includes B1/B3 intermediate states (virtual processes).")

results['vh_higher_order'] = {
    'V_B2B2': V_B2B2,
    'V_B2B2_evals': evals_VB2,
    'V3_B2B2': V3,
    'V3_B2B2_evals': evals_V3,
    'ratio_4to2': ratio_4to2,
    'min_4phonon': min_4phonon,
    'V4_full_B2': V4_B2B2,
    'schur_deviation': V_offdiag_rms,
}

print(f"\n  VH-HIGHER-ORDER-48 VERDICT: INFO")
print(f"    4-phonon scattering NOT forbidden by selection rules.")
print(f"    ||V^3||/||V|| = {ratio_4to2:.4f} (suppressed by coupling^2).")
print(f"    Protection mechanism is energetic (BIC), not symmetry-based.")


# ============================================================================
# 4. B3-REPULSIVE-48: B3 repulsive channel in post-transit GGE
# ============================================================================

print(f"\n{'='*72}")
print("4. B3-REPULSIVE-48: B3 Population Inversion in Post-Transit GGE")
print("=" * 72)

# Physics:
# S46 found V_B3B3 has a repulsive channel with eigenvalue -0.072 in the (2,1)
# representation. Post-transit quench (P_exc = 1.000) produces a non-equilibrium
# GGE with specific mode occupations. Does the repulsive channel cause population
# inversion in B3?
#
# The GGE state is determined by 8 Richardson-Gaudin conserved integrals.
# The quench produces n_pairs = 59.8 quasiparticle pairs (S38).
# Per-mode occupation: n_k = |v_k|^2 + n_Bog * (|u_k|^2 + |v_k|^2)
# where n_Bog = 0.9986 (S38).

# B3 sector: 3 modes at energies E_B3
E_B3_modes = E_8[5:8]  # Modes 5, 6, 7 are B3
V_B3B3 = V_8x8[5:8, 5:8]

print(f"\n  B3 sector:")
print(f"    Energies: {E_B3_modes}")
print(f"    V_B3B3 matrix:")
for i in range(3):
    print(f"      [{', '.join(f'{V_B3B3[i,j]:+.6f}' for j in range(3))}]")

evals_VB3, evecs_VB3 = scipy_eigh(V_B3B3)
print(f"\n  V_B3B3 eigenvalues:")
for i, ev in enumerate(evals_VB3):
    print(f"    channel {i}: {ev:+.6f}")
    # Check if this is the (2,1) repulsive channel
    if ev < 0:
        print(f"      ** REPULSIVE CHANNEL: eigenvector = {evecs_VB3[:, i]}")

# Post-transit GGE occupations
# BCS ground state: n_k = |v_k|^2 = 0.5 * (1 - E_k / sqrt(E_k^2 + Delta^2))
# Quench to Delta=0: occupation frozen at ground-state values
# With n_Bog ~ 1 (Schwinger pair creation), all modes fully occupied

Delta_B2_BCS = Delta_0_GL  # Use GL gap
# BCS coherence factors for each mode
xi_k = E_8 - np.mean(E_8)  # Single-particle energies relative to Fermi level
E_qp = np.sqrt(xi_k**2 + Delta_B2_BCS**2)  # Quasiparticle energies

v_sq = 0.5 * (1 - xi_k / E_qp)  # BCS v^2
u_sq = 1 - v_sq

# Post-transit: quasiparticle occupation from Bogoliubov excitation
# n_k_post = v_sq + n_Bog (sudden quench)
n_post = v_sq + n_Bog * (u_sq + v_sq)  # Each mode ~ 1 + v^2 ~ 1
# But physical occupation capped at 1 (Pauli)
n_post = np.minimum(n_post, 1.0)

print(f"\n  Post-transit occupations (BCS quench):")
print(f"  {'mode':>5s} {'branch':>6s} {'E':>8s} {'v^2':>8s} {'u^2':>8s} {'n_post':>8s}")
for i in range(8):
    print(f"  {i:>5d} {branch_labels[i]:>6s} {E_8[i]:>8.4f} {v_sq[i]:>8.4f} {u_sq[i]:>8.4f} {n_post[i]:>8.4f}")

# B3 occupations
n_B3 = n_post[5:8]
print(f"\n  B3 occupations: {n_B3}")

# Population inversion: occurs if higher-energy mode is MORE occupied
# than lower-energy mode
E_B3_sorted = np.sort(E_B3_modes)
n_B3_sorted = n_B3[np.argsort(E_B3_modes)]

inversion = False
for i in range(len(E_B3_sorted)-1):
    if n_B3_sorted[i+1] > n_B3_sorted[i]:
        inversion = True
        print(f"  POPULATION INVERSION detected: n({E_B3_sorted[i+1]:.4f}) = {n_B3_sorted[i+1]:.4f} "
              f"> n({E_B3_sorted[i]:.4f}) = {n_B3_sorted[i]:.4f}")

if not inversion:
    print(f"  No population inversion in B3 (all modes equally occupied at n~1).")
    print(f"  Reason: Schwinger pair creation saturates ALL modes (n_Bog = {n_Bog:.4f})")

# Effect of repulsive channel on B3 gap
# With repulsive interaction, B3 would have negative pairing in the (2,1) channel.
# This means: B3 Cooper pairs in the (2,1) representation experience REPULSION.
# Net effect: B3 gap is REDUCED (already proximity-only from S46).
Delta_B3_proximity = Delta_B3  # From canonical constants
V_B3B3_rep = np.min(evals_VB3)  # Most repulsive eigenvalue

# BCS gap equation with repulsive channel:
# Delta = -V * rho * Delta * integral -> Delta = 0 if V > 0 (repulsive)
# But proximity effect from B2 can sustain Delta even with some repulsion.
# Net: Delta_eff = Delta_proximity * (1 + V_rep * rho)
# where V_rep < 0 means Delta_eff < Delta_proximity

rho_B3 = float(thouless_data['rho_B3'])
correction_factor = 1 + V_B3B3_rep * rho_B3
Delta_B3_corrected = Delta_B3_proximity * max(correction_factor, 0)

print(f"\n  Repulsive channel effect on B3 gap:")
print(f"    V_B3B3_repulsive = {V_B3B3_rep:.6f}")
print(f"    rho_B3 = {rho_B3:.4f}")
print(f"    Correction factor: 1 + V*rho = {correction_factor:.4f}")
print(f"    Delta_B3_corrected = {Delta_B3_corrected:.4f} (was {Delta_B3_proximity:.4f})")

results['b3_repulsive'] = {
    'V_B3B3': V_B3B3,
    'V_B3B3_evals': evals_VB3,
    'n_post': n_post,
    'inversion': inversion,
    'correction_factor': correction_factor,
    'Delta_B3_corrected': Delta_B3_corrected,
}

print(f"\n  B3-REPULSIVE-48 VERDICT: INFO")
print(f"    Population inversion: {'YES' if inversion else 'NO (saturation)'}")
print(f"    Repulsive channel suppresses B3 gap by {(1-correction_factor)*100:.1f}%")


# ============================================================================
# 5. THREE-PHONON-48: Resonant 3-phonon friction
# ============================================================================

print(f"\n{'='*72}")
print("5. THREE-PHONON-48: Resonant 3-Phonon Friction Channel")
print("=" * 72)

# Physics:
# omega_B2 ~ 2 * omega_B1 with 0.6% detuning (from MEMORY).
# This near-resonance enables a parametric decay: B2 -> B1 + B1.
# The 3-phonon friction contributes to the dissipation shortfall (3.76x from S46).
#
# Fermi golden rule rate for parametric decay:
#   Gamma_3ph = (2*pi/hbar) * |V_3|^2 * rho_final
# where V_3 is the 3-phonon matrix element and rho_final is the 2-body
# density of states for the B1+B1 final state.

omega_B2 = E_B2_mean  # B2 energy ~ 0.845 M_KK
omega_B1 = E_B1        # B1 energy ~ 0.819 M_KK

detuning = omega_B2 - 2 * omega_B1
detuning_frac = detuning / omega_B2

print(f"\n  Near-resonance parameters:")
print(f"    omega_B2 = {omega_B2:.6f} M_KK")
print(f"    omega_B1 = {omega_B1:.6f} M_KK")
print(f"    2*omega_B1 = {2*omega_B1:.6f} M_KK")
print(f"    Detuning: {detuning:.6f} M_KK ({detuning_frac*100:.2f}%)")

# The 3-phonon matrix element V_3 comes from anharmonic terms
# In the spectral action expansion: S = S_0 + S_2 (quadratic) + S_3 (cubic) + ...
# S_3 = (1/6) * d^3 S / d(tau)^3 * delta_tau^3
# The cubic anharmonicity is characterized by the Gruneisen parameter.
#
# From the V matrix: the relevant coupling is V_B1B2 (inter-branch)
V_B1B2 = V_8x8[0, 1:5]  # B1-to-B2 coupling (1x4 vector)
V_B1B2_max = float(thouless_data['V_B1B2_max'])

print(f"\n  V_B1B2 coupling vector: {V_B1B2}")
print(f"  |V_B1B2_max| = {V_B1B2_max:.6f}")

# 3-phonon vertex: V_3 ~ V_B1B2^2 / E_B1 (perturbative estimate)
# This is the effective cubic anharmonicity for B2 -> B1 + B1
V_3_eff = V_B1B2_max**2 / omega_B1
print(f"  Effective 3-phonon vertex: V_3 ~ V_B1B2^2 / omega_B1 = {V_3_eff:.6f}")

# Density of final states: two B1 modes with combined energy ~ omega_B2
# Since there's only 1 B1 mode, rho_final is a delta function.
# The decay is B2 -> B1 + B1 (but there's only 1 B1 mode, so 2-particle
# final state has fixed energy 2*E_B1).
# The rate becomes:
#   Gamma_3ph = (2*pi) * |V_3|^2 * delta(omega_B2 - 2*omega_B1) / (2*omega_B1)
# With finite linewidth gamma ~ 1/Q:
#   delta -> Lorentzian: 1/(pi * gamma) * gamma^2/((omega-omega_0)^2 + gamma^2)

# B2 linewidth from Q factor (Q_B2 = 52 from S43)
Q_B2 = 52.0
gamma_B2 = omega_B2 / (2 * Q_B2)

# Lorentzian at the detuning
lorentz = (1/PI) * gamma_B2 / (detuning**2 + gamma_B2**2)

# FGR rate
Gamma_3ph = 2 * PI * V_3_eff**2 * lorentz

print(f"\n  Fermi golden rule for B2 -> B1 + B1:")
print(f"    Q_B2 = {Q_B2}")
print(f"    gamma_B2 = omega_B2 / (2*Q) = {gamma_B2:.6f}")
print(f"    Lorentzian at detuning: {lorentz:.4f}")
print(f"    Gamma_3ph = {Gamma_3ph:.6f}")

# Compare to the dissipation shortfall
# S46 found gamma_LZ / gamma_H = 3.2 (shortfall 3.76x).
# The total dissipation = gamma_H (2-phonon) + Gamma_3ph (3-phonon)
# We need Gamma_3ph >= 3.76 * gamma_H to close the shortfall.
gamma_H = Gamma_Langer_BCS  # Langer decay rate (2-phonon dissipation)
shortfall_ratio = 3.76

required_Gamma_3ph = shortfall_ratio * gamma_H
ratio_3ph = Gamma_3ph / gamma_H

print(f"\n  Comparison to dissipation shortfall:")
print(f"    gamma_H (2-phonon, Langer) = {gamma_H:.6f}")
print(f"    Required additional Gamma = {shortfall_ratio} * gamma_H = {required_Gamma_3ph:.6f}")
print(f"    Computed Gamma_3ph = {Gamma_3ph:.6f}")
print(f"    Ratio Gamma_3ph / gamma_H = {ratio_3ph:.6f}")
print(f"    Shortfall closed? {'YES' if ratio_3ph >= shortfall_ratio else 'NO'}")

if ratio_3ph < shortfall_ratio:
    print(f"    Remaining shortfall: {shortfall_ratio / max(ratio_3ph, 1e-20):.2f}x after 3-phonon")

results['three_phonon'] = {
    'omega_B2': omega_B2,
    'omega_B1': omega_B1,
    'detuning': detuning,
    'detuning_frac': detuning_frac,
    'V_B1B2': V_B1B2,
    'V_3_eff': V_3_eff,
    'Q_B2': Q_B2,
    'gamma_B2': gamma_B2,
    'lorentz': lorentz,
    'Gamma_3ph': Gamma_3ph,
    'gamma_H': gamma_H,
    'ratio_3ph': ratio_3ph,
    'shortfall_remaining': shortfall_ratio / max(ratio_3ph, 1e-20),
}

print(f"\n  THREE-PHONON-48 VERDICT: INFO")
print(f"    3-phonon rate Gamma_3ph = {Gamma_3ph:.6f}")
print(f"    Ratio to 2-phonon = {ratio_3ph:.4f}")


# ============================================================================
# 6. TRANSIT-279-48: 279-mode tachyonic transit velocity
# ============================================================================

print(f"\n{'='*72}")
print("6. TRANSIT-279-48: 279-Mode Tachyonic Transit Velocity")
print("=" * 72)

# Physics:
# S46 found 279 tachyonic scalars at the fold (f'<0 modes in the spectral action).
# The Gram PSD theorem guarantees kinetic mass is POSITIVE (PERMANENT).
# These 279 modes are reinterpreted as the transit mechanism.
#
# The transit through the tachyonic saddle is like slow-roll inflation:
#   3H * d(phi)/dt = -V'(phi) (friction-limited) or
#   M * d^2(phi)/dt^2 = -V'(phi) - 3H * d(phi)/dt (underdamped)
#
# For the phononic analog:
#   M_tau * d^2(tau)/dt^2 = F_drive - F_resist - 3H * d(tau)/dt
# where F_drive comes from tachyonic modes (m^2 < 0)
# and F_resist comes from stable modes (m^2 > 0).

# S46 pseudo-Riemannian data
D_evals_real = pseudo_data['D_eigenvalues_real']
D_evals_imag = pseudo_data['D_eigenvalues_imag']
D_evals_complex = D_evals_real + 1j * D_evals_imag

# For the transit analysis, use the TT-Lichnerowicz data (s48)
# which gives the 31-mode TT spectrum at the fold
try:
    tt_data = np.load(os.path.join(SCRIPT_DIR, 's48_tt_lichnerowicz.npz'), allow_pickle=True)
    tt_evals_fold = tt_data['eigenvalues_fold']
    n_TT = len(tt_evals_fold)
    n_tachyonic_tt = np.sum(tt_evals_fold < 0)
    print(f"\n  TT-Lichnerowicz at fold:")
    print(f"    n_TT = {n_TT}")
    print(f"    n_tachyonic = {n_tachyonic_tt}")
    print(f"    lambda_min = {np.min(tt_evals_fold):.6f}")
    print(f"    All positive (S48 TT-LICH): {'YES' if n_tachyonic_tt == 0 else 'NO'}")
except Exception as e:
    print(f"\n  TT data unavailable: {e}")
    tt_evals_fold = np.array([0.32])
    n_TT = 31
    n_tachyonic_tt = 0

# The 279 tachyonic scalars from S46 are NOT TT modes -- they are scalar
# fluctuations of the spectral action f(x) with f'(x) < 0.
# Universal by Gram PSD theorem: kinetic mass always positive.
# The tachyonic mass^2 drives the transit.

# Model: 279 tachyonic modes with m^2 ~ -|a_2| and 713 stable modes with m^2 ~ |a_4|
# (From S46: 279 out of 992 modes have f'<0)
n_tachyonic_total = 279
n_stable_total = 992 - 279  # = 713

# Effective potential gradient:
# V'(tau) = sum_tachyonic |m_i^2(tau)| (driving) - sum_stable m_j^2(tau) (resisting)
# At the fold, this is related to d2S/dtau2

# From canonical constants:
d2S = 317862.84898132  # d^2 S_full/dtau^2 at fold
dS = 58672.80241318    # dS/dtau at fold
M_ATDHFB = 1.695       # ATDHFB collective mass

# Force balance:
# M * v_dot = -dS/dtau - 3H * v
# At terminal velocity: v_dot = 0, so v_term = -dS/dtau / (3H)
# This matches v_terminal from canonical constants

v_term_check = abs(dS) / (3 * H_fold)
print(f"\n  Transit velocity check:")
print(f"    v_terminal (canonical) = {v_terminal:.4f}")
print(f"    |dS/dtau| / (3*H) = {v_term_check:.4f}")
print(f"    Ratio: {v_term_check / v_terminal:.4f}")

# Slow-roll parameters (analog):
# epsilon = (M_Pl^2 / 2) * (V'/V)^2 -> (1/2) * (dS/S)^2
epsilon_SR = 0.5 * (dS / 250360.67)**2
# eta = M_Pl^2 * V''/V -> d2S / S
eta_SR = d2S / 250360.67

print(f"\n  Slow-roll analogs:")
print(f"    epsilon = (1/2)(dS/S)^2 = {epsilon_SR:.6f}")
print(f"    eta = d2S/S = {eta_SR:.6f}")
print(f"    n_s_SR = 1 - 6*epsilon + 2*eta = {1 - 6*epsilon_SR + 2*eta_SR:.6f}")

# Driving vs resistance decomposition:
# The 279 tachyonic modes contribute negative curvature (driving)
# The 713 stable modes contribute positive curvature (resistance)
# Net: d2S = sum(driving) + sum(resisting)

# Per-mode average:
m2_driving_per_mode = d2S * n_tachyonic_total / (n_tachyonic_total + n_stable_total) / n_tachyonic_total
m2_resisting_per_mode = d2S * n_stable_total / (n_tachyonic_total + n_stable_total) / n_stable_total

# Actually, the tachyonic modes DECREASE d2S (they have f'<0):
# d2S = sum_{f'>0} |d2/dtau2 lambda_i^2| + sum_{f'<0} |d2/dtau2 lambda_i^2| * f'(lambda_i^2)
# Since f'<0 for tachyonic modes, their contribution to d2S is NEGATIVE.
# But the NET d2S > 0 (fold is stable from TT-LICH-48).

# Transit time
tau_transit_duration = dt_transit  # from canonical constants
v_mean_transit = tau_fold / tau_transit_duration if tau_transit_duration > 0 else 0

print(f"\n  Transit parameters:")
print(f"    dt_transit = {tau_transit_duration:.6e} M_KK^{{-1}}")
print(f"    v_terminal = {v_terminal:.4f}")
print(f"    n_tachyonic = {n_tachyonic_total} (S46)")
print(f"    n_stable = {n_stable_total}")
print(f"    Ratio tachyonic/stable = {n_tachyonic_total/n_stable_total:.3f}")

# The transit is underdamped (backreaction 3.7% from S38).
# The 279 tachyonic modes collectively drive the transit through the fold.
# This is analogous to Starobinsky inflation where R + R^2 provides the
# inflaton mass, but here the "inflaton" is the Jensen parameter tau
# and the R^2 term comes from the spectral action a_4 coefficient.

# Effective "number of e-folds":
# N_e = integral H dt ~ H * dt_transit
N_eff_efolds = H_fold * tau_transit_duration
print(f"\n  Effective number of e-folds:")
print(f"    N_e = H * dt_transit = {N_eff_efolds:.4f}")
print(f"    (Too small for inflation -- this is a TRANSIT, not inflation)")

results['transit_279'] = {
    'n_tachyonic': n_tachyonic_total,
    'n_stable': n_stable_total,
    'epsilon_SR': epsilon_SR,
    'eta_SR': eta_SR,
    'ns_SR': 1 - 6*epsilon_SR + 2*eta_SR,
    'v_terminal': v_terminal,
    'dt_transit': tau_transit_duration,
    'N_eff_efolds': N_eff_efolds,
    'driving_fraction': n_tachyonic_total / (n_tachyonic_total + n_stable_total),
}

print(f"\n  TRANSIT-279-48 VERDICT: INFO")
print(f"    Slow-roll analogs: epsilon={epsilon_SR:.4f}, eta={eta_SR:.4f}")
print(f"    n_s(SR) = {1 - 6*epsilon_SR + 2*eta_SR:.4f} (NOT the physical n_s)")
print(f"    N_e = {N_eff_efolds:.4f} (transit, not inflation)")


# ============================================================================
# 7. EIGENVECTOR-48: Handled in s48_eigenvectors.py
# ============================================================================

print(f"\n{'='*72}")
print("7. EIGENVECTOR-48: See s48_eigenvectors.py (separate script)")
print("=" * 72)
print("  Eigenvector analysis (Chladni patterns, spatial extent)")
print("  requires modifying tier1_dirac_spectrum.py infrastructure.")
print("  Done as standalone computation.")


# ============================================================================
# 8. DEFECT-CORR-48: Topological defect correlations and n_s
# ============================================================================

print(f"\n{'='*72}")
print("8. DEFECT-CORR-48: Topological Defect Correlations and n_s")
print("=" * 72)

# Physics:
# The framework is BDI (AZ class), with Z_2 topological invariant.
# KZ vortex formation during transit produces topological defects with
# correlations determined by the universality class.
#
# For BDI (1D, Z_2): the defect density scales as
#   n_defect ~ (v_transit / v_gap)^{nu*d/(1+nu*z)}
# where nu is the correlation length exponent, z is the dynamical exponent,
# and d is the spatial dimension.
#
# The power spectrum of defect correlations gives:
#   P(k) ~ k^{n_s - 1}
# where n_s is determined by the KZ scaling.
#
# For a 1D system with nu = 1, z = 1 (BDI universality):
#   n_defect ~ sqrt(v_transit)
#   P(k) ~ k^0 (flat spectrum) -> n_s = 1
#
# But our system is NOT purely 1D -- the 8-dimensional SU(3) fiber
# projected to 4D spacetime has an effective dimension d_eff.

# KZ universality class for BDI:
# nu = 1 (mean-field, since our BCS is 0D/mean-field)
# z = 2 (BCS: quasiparticle dispersion E = sqrt(xi^2 + Delta^2), dynamic exponent z=2)
# d_eff = ? (key question)

nu_BDI = 1.0
z_BDI = 2.0

# The KZ defect density
xi_hat = lambda d_eff: nu_BDI * d_eff / (1 + nu_BDI * z_BDI)

print(f"\n  KZ universality parameters:")
print(f"    AZ class: BDI")
print(f"    Z_2 invariant: nontrivial (S46: 13 Berry phases)")
print(f"    Correlation exponent nu = {nu_BDI}")
print(f"    Dynamic exponent z = {z_BDI}")

# The spectral tilt n_s from KZ scaling:
# For a quench with rate tau_Q, the correlation length scales as
#   xi ~ tau_Q^{nu/(1+nu*z)}
# The power spectrum of the order parameter after the quench:
#   P(k) ~ k^{-(d + z - 2 + eta)} for k >> 1/xi
# where eta is the anomalous dimension.
#
# For BDI mean-field: eta = 0
# The spectral index from the KZ correlation function:
#   <psi(x) psi(x+r)> ~ r^{-(d-2+eta)} * f(r/xi)
#   -> P(k) ~ k^{d-2+eta} for k << 1/xi (superhorizon)
#   -> P(k) ~ k^{-(d+z-2+eta)} for k >> 1/xi (subhorizon)
#
# The CMB spectral index corresponds to the superhorizon limit:
#   n_s - 1 = d - 2 + eta + corrections

print(f"\n  n_s prediction from KZ defect correlations:")
print(f"  d_eff -> n_s = 1 + (d_eff - 2 + eta)/(1 + nu*z)")

# Scan over effective dimensions
d_eff_scan = np.array([1, 2, 3, 4, 6, 8])
ns_predictions = {}

for d_eff in d_eff_scan:
    # KZ scaling: n_s - 1 = -(d_eff + z) / (1 + nu*z) + 1 [Harrison-Zel'dovich correction]
    # More precisely, for causal KZ seeds:
    # The 2-point function of the order parameter:
    #   C(r) ~ r^{-p} with p = (d-2+eta) [in real space, superhorizon]
    #   P(k) ~ k^{d-1-2p} = k^{d-1-2(d-2+eta)} = k^{-(d-3+2*eta)} [wrong for d=1]
    #
    # Standard KZ result for BCS quench (Zurek 1985, Kibble 1976):
    # The defect spacing xi_D ~ tau_Q^{nu/(1+nu*z)}
    # The power in the defect correlation function:
    #   P_defect(k) ~ k^0 for k*xi_D << 1 (white noise on large scales)
    #   P_defect(k) ~ k^{-alpha} for k*xi_D >> 1
    # where alpha depends on the defect type:
    #   point vortices (d=2): alpha = 0 (Poisson)
    #   cosmic strings (d=3): alpha = -1 (network)
    #   domain walls (d=1): alpha = 0 (random telegraph)
    #
    # The n_s from DEFECT correlations (NOT field correlations):
    # For a Poisson process with mean spacing xi_D:
    #   P(k) ~ 1 (white noise, n_s = 1) for k << 1/xi_D
    #   P(k) ~ k^{-2} for k >> 1/xi_D (individual defect profile)
    #
    # The observed n_s = 0.965 requires a slight RED tilt: P ~ k^{-0.035}
    # This could come from: (1) KZ quench non-instantaneity, (2) defect drift,
    # (3) the tau-dependence of xi_D.

    # Zurek's formula for the KZ spectral index (simplified):
    # n_s = 1 - 2/(1 + nu*z) for domain walls in 1D
    # n_s = 1 - (d-1)/(d*(1+nu*z)) correction for higher d

    ns_KZ = 1 - 2 * nu_BDI / (1 + nu_BDI * z_BDI)  # basic KZ
    ns_KZ_d = 1 - 2 * nu_BDI / (d_eff * (1 + nu_BDI * z_BDI))  # d-corrected

    ns_predictions[d_eff] = {
        'ns_basic': ns_KZ,
        'ns_d_corrected': ns_KZ_d,
        'xi_hat': xi_hat(d_eff),
    }

print(f"\n  {'d_eff':>5s} | {'n_s (basic)':>11s} | {'n_s (d-corr)':>12s} | {'target':>7s}")
print(f"  {'-'*45}")
target_ns = 0.965
for d_eff in d_eff_scan:
    ns_b = ns_predictions[d_eff]['ns_basic']
    ns_d = ns_predictions[d_eff]['ns_d_corrected']
    dist_b = abs(ns_b - target_ns)
    dist_d = abs(ns_d - target_ns)
    marker = " <--" if dist_d < 0.01 else ""
    print(f"  {d_eff:>5d} | {ns_b:>11.4f} | {ns_d:>12.4f} | {target_ns}{marker}")

# The basic KZ formula gives n_s = 1 - 2/(1+2) = 1 - 2/3 = 0.333
# This is MUCH too red. The d-corrected version:
# d=3: n_s = 1 - 2/(3*3) = 0.778 (still too red)
# d=6: n_s = 1 - 2/(6*3) = 0.889 (still too red)
# d=8: n_s = 1 - 2/(8*3) = 0.917 (approaching but still too red)

# Alternative: use the EFFECTIVE BCS scaling.
# For BCS, the gap vanishes as Delta ~ |tau - tau_c|^{nu_BCS * z_BCS}
# with nu_BCS = 1/2 (mean-field), z_BCS = 2.
# The KZ formula with these:
nu_BCS = 0.5
z_BCS = 2.0
ns_BCS_basic = 1 - 2 * nu_BCS / (1 + nu_BCS * z_BCS)
ns_BCS_8d = 1 - 2 * nu_BCS / (8 * (1 + nu_BCS * z_BCS))

print(f"\n  Alternative: BCS mean-field exponents (nu=1/2, z=2):")
print(f"    n_s (basic, d=1) = {ns_BCS_basic:.4f}")
print(f"    n_s (d=8) = {ns_BCS_8d:.4f}")

# The most promising route: if the defect correlations live in the
# full 8D SU(3) fiber, and the projection to 4D introduces a factor:
# n_s - 1 = -(8-4)/(8*(1+nu*z)) = -4/(8*3) = -1/6 = -0.167
# -> n_s = 0.833 (still too red)

# With d_eff = 8 and log corrections from the flat B2 band:
# The BIC (bound state in continuum) provides a logarithmic correction:
# n_s - 1 = -2/(d_eff * (1+nu*z)) + (1/ln(Q_B2)) * (1/(1+nu*z))
Q_B2_val = 52.0
log_correction = (1 / np.log(Q_B2_val)) / (1 + nu_BDI * z_BDI)
ns_with_log = 1 - 2 * nu_BDI / (8 * (1 + nu_BDI * z_BDI)) + log_correction

print(f"\n  With BIC logarithmic correction (Q_B2={Q_B2_val}):")
print(f"    log correction = {log_correction:.4f}")
print(f"    n_s = {ns_with_log:.4f} (vs target {target_ns})")
print(f"    Deviation from Planck: {ns_with_log - target_ns:.4f}")

# Final assessment: what d_eff gives n_s = 0.965?
# n_s = 1 - 2*nu / (d_eff * (1 + nu*z))
# 0.035 = 2 / (d_eff * 3)
# d_eff = 2 / (3 * 0.035) = 19.05
d_eff_required = 2 * nu_BDI / (3 * (1 - target_ns))
print(f"\n  Required d_eff for n_s = {target_ns}: d_eff = {d_eff_required:.2f}")
print(f"  SU(3) fiber dim = 8. Required d_eff/dim = {d_eff_required/8:.2f}")
print(f"  Conclusion: basic KZ defect correlations CANNOT reproduce n_s = 0.965")
print(f"  unless d_eff ~ 19 (physically unreasonable for 8D fiber).")

# BCS with nu=1/2:
d_eff_BCS = 2 * nu_BCS / ((1 + nu_BCS * z_BCS) * (1 - target_ns))
print(f"\n  BCS mean-field: required d_eff = {d_eff_BCS:.2f}")

results['defect_corr'] = {
    'nu_BDI': nu_BDI,
    'z_BDI': z_BDI,
    'nu_BCS': nu_BCS,
    'z_BCS': z_BCS,
    'ns_predictions': ns_predictions,
    'ns_BCS_basic': ns_BCS_basic,
    'ns_BCS_8d': ns_BCS_8d,
    'ns_with_log': ns_with_log,
    'd_eff_required_BDI': d_eff_required,
    'd_eff_required_BCS': d_eff_BCS,
    'target_ns': target_ns,
}

print(f"\n  DEFECT-CORR-48 VERDICT: FAIL")
print(f"    KZ defect correlations give n_s too red for ANY d_eff <= 8.")
print(f"    Required d_eff = {d_eff_required:.1f} (BDI) or {d_eff_BCS:.1f} (BCS).")
print(f"    This closes the KZ-defect route to n_s = 0.965.")
print(f"    The n_s problem remains OPEN -- it is NOT a KZ scaling problem.")


# ============================================================================
# 9. AGGREGATE RESULTS AND GATE VERDICT
# ============================================================================

print(f"\n{'='*72}")
print("AGGREGATE RESULTS: QA-TACHYON-48")
print("=" * 72)

verdicts = {
    'BERRY-EDGE-48': 'INFO',
    'DISSOLUTION-GOE-48': 'INFO',
    'VH-HIGHER-ORDER-48': 'INFO',
    'B3-REPULSIVE-48': 'INFO',
    'THREE-PHONON-48': 'INFO',
    'TRANSIT-279-48': 'INFO',
    'EIGENVECTOR-48': 'DEFERRED (s48_eigenvectors.py)',
    'DEFECT-CORR-48': 'FAIL',
}

print(f"\n  Sub-computation verdicts:")
for name, verdict in verdicts.items():
    print(f"    {name}: {verdict}")

print(f"\n  KEY NUMBERS:")
print(f"    1. Berry edge: {n_wall_states} wall-localized states in 32-cell chain")
print(f"       t_inter = {t_inter:.4f} (0D limit: too strongly coupled for edge physics)")
print(f"    2. Dissolution-GOE: eps_crossover_SFF = {eps_sff_crossover:.6f}")
print(f"       r_ratio at eps=0: {r_ratios[0.0]:.4f} (Poisson={r_poisson:.4f})")
print(f"    3. VH higher-order: ||V^3||/||V|| = {ratio_4to2:.6f}")
print(f"       4-phonon NOT forbidden by selection rules")
print(f"    4. B3 repulsive: correction factor = {correction_factor:.4f}")
print(f"       No population inversion (Schwinger saturation)")
print(f"    5. 3-phonon: Gamma_3ph/gamma_H = {ratio_3ph:.6f}")
print(f"       Shortfall: {shortfall_ratio / max(ratio_3ph, 1e-20):.1f}x remaining")
print(f"    6. Transit-279: epsilon_SR = {epsilon_SR:.6f}, eta_SR = {eta_SR:.4f}")
print(f"       N_e = {N_eff_efolds:.4f} (transit, not inflation)")
print(f"    7. Eigenvector: deferred to s48_eigenvectors.py")
print(f"    8. Defect-corr: n_s(KZ) = {1 - 2/(8*3):.4f} at d=8 (target {target_ns})")
print(f"       d_eff required = {d_eff_required:.1f}. KZ route to n_s CLOSED.")

print(f"\n  GATE: QA-TACHYON-48 = INFO")
print(f"  (Batch of diverse computations; 7 INFO + 1 FAIL)")


# ============================================================================
# 10. PLOTS
# ============================================================================

print(f"\n{'='*72}")
print("GENERATING PLOTS")
print("=" * 72)

fig, axes = plt.subplots(3, 3, figsize=(20, 16))
fig.suptitle("QA-TACHYON-48: Quantum-Acoustic & Tachyonic Transit Computations\n"
             "Session 48 W5-G (8 sub-computations)", fontsize=13, fontweight='bold')

# Panel 1: Berry edge - chain localization
ax = axes[0, 0]
sites = np.arange(N_chain)
loc_by_site = np.zeros(N_chain)
for i in range(N_chain):
    # Average localization of all states at site i
    for n in range(8*N_chain):
        psi = evecs_chain[:, n]
        loc_by_site[i] += np.sum(np.abs(psi[8*i:8*(i+1)])**2)
loc_by_site /= (8*N_chain)
ax.bar(sites, loc_by_site, color='steelblue', edgecolor='none', alpha=0.7)
ax.axvline(N_chain//2, color='red', ls='--', lw=2, label='Domain wall')
ax.set_xlabel('Cell index')
ax.set_ylabel('Mean state weight')
ax.set_title('BERRY-EDGE: Chain Localization Profile')
ax.legend(fontsize=8)

# Panel 2: SFF curves
ax = axes[0, 1]
for eps in eps_scan:
    ratio = eps / eps_c if eps_c > 0 else 0
    sff = sff_results[eps]
    ax.plot(t_sff, sff, label=f'$\\epsilon/\\epsilon_c$ = {ratio:.1f}', alpha=0.7)
ax.axhline(1, color='gray', ls=':', lw=1)
ax.set_xlabel('$t / \\langle s \\rangle$')
ax.set_ylabel('SFF($t$)')
ax.set_title('DISSOLUTION-GOE: Spectral Form Factor')
ax.legend(fontsize=7)
ax.set_ylim(0, 2)

# Panel 3: V_B2B2 eigenvalues and 4-phonon
ax = axes[0, 2]
x = np.arange(4)
ax.bar(x - 0.15, evals_VB2, 0.3, label='2-phonon $\\lambda$', color='steelblue')
ax.bar(x + 0.15, evals_V3, 0.3, label='4-phonon $\\lambda^3$', color='coral')
ax.set_xticks(x)
ax.set_xticklabels([f'ch{i}' for i in range(4)])
ax.set_ylabel('Eigenvalue')
ax.set_title('VH-HIGHER-ORDER: V$_{B2B2}$ Scattering Channels')
ax.legend(fontsize=8)
ax.axhline(0, color='gray', ls=':', lw=1)

# Panel 4: B3 occupations
ax = axes[1, 0]
x = np.arange(8)
colors = ['steelblue'] + ['coral']*4 + ['forestgreen']*3
ax.bar(x, n_post, color=colors, edgecolor='black', linewidth=0.5)
ax.set_xticks(x)
ax.set_xticklabels(['B1'] + ['B2']*4 + ['B3']*3, fontsize=8)
ax.set_ylabel('Post-transit occupation')
ax.set_title('B3-REPULSIVE: Post-Transit Mode Occupations')
ax.axhline(1, color='gray', ls=':', lw=1)
ax.set_ylim(0.9, 1.05)

# Panel 5: 3-phonon resonance diagram
ax = axes[1, 1]
# Energy level diagram
ax.axhline(omega_B1, color='steelblue', lw=3, label=f'$\\omega_{{B1}}$ = {omega_B1:.4f}')
ax.axhline(omega_B2, color='coral', lw=3, label=f'$\\omega_{{B2}}$ = {omega_B2:.4f}')
ax.axhline(2*omega_B1, color='steelblue', lw=2, ls='--', label=f'$2\\omega_{{B1}}$ = {2*omega_B1:.4f}')
ax.fill_between([0, 1], omega_B2 - gamma_B2, omega_B2 + gamma_B2,
                 alpha=0.2, color='coral', label=f'B2 linewidth ($Q$={Q_B2:.0f})')
ax.annotate(f'Detuning: {detuning:.4f}\n({detuning_frac*100:.2f}%)',
            xy=(0.5, omega_B2), fontsize=9, ha='center')
ax.set_xlim(-0.1, 1.1)
ax.set_ylabel('Energy ($M_{KK}$)')
ax.set_title('THREE-PHONON: $\\omega_{B2} \\approx 2\\omega_{B1}$ Resonance')
ax.legend(fontsize=7, loc='lower left')

# Panel 6: Transit slow-roll
ax = axes[1, 2]
tau_plot = np.linspace(0.001, 0.19, 100)
# Schematic potential
V_plot = -abs(dS) * (tau_plot - tau_fold) + 0.5 * d2S * (tau_plot - tau_fold)**2
ax.plot(tau_plot, V_plot / 1e5, 'k-', lw=2)
ax.axvline(tau_fold, color='red', ls='--', lw=1, label=f'$\\tau_{{fold}}$ = {tau_fold}')
ax.annotate(f'$\\epsilon_{{SR}}$ = {epsilon_SR:.4f}\n$\\eta_{{SR}}$ = {eta_SR:.3f}\n$N_e$ = {N_eff_efolds:.4f}',
            xy=(0.05, 0.8), xycoords='axes fraction', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow'))
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$V(\\tau) / 10^5$')
ax.set_title('TRANSIT-279: Slow-Roll Analogs')
ax.legend(fontsize=8)

# Panel 7: n_s from KZ vs d_eff
ax = axes[2, 0]
d_fine = np.linspace(1, 25, 200)
ns_BDI_fine = 1 - 2 * nu_BDI / (d_fine * (1 + nu_BDI * z_BDI))
ns_BCS_fine = 1 - 2 * nu_BCS / (d_fine * (1 + nu_BCS * z_BCS))
ax.plot(d_fine, ns_BDI_fine, 'b-', lw=2, label=f'BDI ($\\nu$={nu_BDI}, $z$={z_BDI})')
ax.plot(d_fine, ns_BCS_fine, 'r-', lw=2, label=f'BCS ($\\nu$={nu_BCS}, $z$={z_BCS})')
ax.axhline(target_ns, color='green', ls='--', lw=2, label=f'Planck $n_s$ = {target_ns}')
ax.axvline(8, color='gray', ls=':', lw=1, label='dim(SU(3)) = 8')
ax.set_xlabel('$d_{eff}$')
ax.set_ylabel('$n_s$')
ax.set_title('DEFECT-CORR: $n_s$ from KZ Defect Correlations')
ax.legend(fontsize=7)
ax.set_xlim(1, 25)
ax.set_ylim(0.8, 1.05)

# Panel 8: r-ratio vs epsilon
ax = axes[2, 1]
eps_plot = [e/eps_c for e in eps_scan if eps_c > 0]
r_plot = [r_ratios[e] for e in eps_scan]
ax.plot(eps_plot, r_plot, 'ko-', markersize=8)
ax.axhline(r_poisson, color='blue', ls='--', lw=1.5, label=f'Poisson = {r_poisson:.4f}')
ax.axhline(r_goe, color='red', ls='--', lw=1.5, label=f'GOE = {r_goe:.4f}')
ax.axhline(r_mid, color='gray', ls=':', lw=1, label=f'Midpoint = {r_mid:.4f}')
ax.set_xlabel('$\\epsilon / \\epsilon_c$')
ax.set_ylabel('$\\langle r \\rangle$')
ax.set_title('DISSOLUTION-GOE: Level Spacing Ratio')
ax.legend(fontsize=8)

# Panel 9: Summary
ax = axes[2, 2]
ax.axis('off')
summary = (
    f"QA-TACHYON-48 SUMMARY\n"
    f"{'='*40}\n\n"
    f"1. BERRY-EDGE: {n_wall_states} wall states\n"
    f"   (0D limit: t_inter={t_inter:.3f})\n\n"
    f"2. DISSOLUTION: r(0)={r_ratios[0.0]:.4f}\n"
    f"   SFF crossover: {eps_sff_crossover:.4f}\n\n"
    f"3. VH-4PHONON: ||V^3||/||V||={ratio_4to2:.4f}\n"
    f"   NOT forbidden by selection rules\n\n"
    f"4. B3-REPULSIVE: no inversion\n"
    f"   Gap correction: {correction_factor:.3f}\n\n"
    f"5. 3-PHONON: Gamma/gamma_H={ratio_3ph:.5f}\n"
    f"   Shortfall: not closed\n\n"
    f"6. TRANSIT-279: eps_SR={epsilon_SR:.4f}\n"
    f"   eta_SR={eta_SR:.3f}, N_e={N_eff_efolds:.4f}\n\n"
    f"7. EIGENVECTOR: separate script\n\n"
    f"8. DEFECT-CORR: FAIL\n"
    f"   n_s(KZ,d=8)={1-2/(8*3):.3f} (target {target_ns})\n"
    f"   d_eff needed: {d_eff_required:.1f}\n\n"
    f"GATE: QA-TACHYON-48 = INFO"
)
ax.text(0.05, 0.95, summary, transform=ax.transAxes, fontsize=8,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's48_qa_tachyon.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"\nSaved plot: {plot_path}")
plt.close()


# ============================================================================
# 11. SAVE DATA
# ============================================================================

print(f"\n{'='*72}")
print("SAVING DATA")
print("=" * 72)

output = {
    'gate_name': 'QA-TACHYON-48',
    'gate_verdict': 'INFO',
    # Berry edge
    'berry_total_pi': total_pi,
    'berry_z2': 1 if global_z2 == '+1' else -1,
    'berry_t_inter': t_inter,
    'berry_n_wall_states': n_wall_states,
    'berry_n_edge_states': n_edge_states,
    'berry_max_edge_shift': max_edge_shift,
    'berry_ipr_mean': ipr_mean,
    # Dissolution
    'diss_eps_c': eps_c,
    'diss_eps_crossover_sff': eps_sff_crossover,
    'diss_r_at_eps0': r_ratios[0.0],
    'diss_r_poisson': r_poisson,
    'diss_r_goe': r_goe,
    # VH higher order
    'vh_V_B2B2': V_B2B2,
    'vh_V_B2B2_evals': evals_VB2,
    'vh_V3_evals': evals_V3,
    'vh_ratio_4to2': ratio_4to2,
    'vh_schur_deviation': V_offdiag_rms,
    # B3 repulsive
    'b3_V_B3B3_evals': evals_VB3,
    'b3_correction_factor': correction_factor,
    'b3_inversion': inversion,
    'b3_n_post': n_post,
    # 3-phonon
    'ph3_detuning': detuning,
    'ph3_detuning_frac': detuning_frac,
    'ph3_V_3_eff': V_3_eff,
    'ph3_Gamma_3ph': Gamma_3ph,
    'ph3_gamma_H': gamma_H,
    'ph3_ratio': ratio_3ph,
    # Transit-279
    'tr_epsilon_SR': epsilon_SR,
    'tr_eta_SR': eta_SR,
    'tr_ns_SR': 1 - 6*epsilon_SR + 2*eta_SR,
    'tr_N_efolds': N_eff_efolds,
    'tr_n_tachyonic': n_tachyonic_total,
    'tr_n_stable': n_stable_total,
    # Defect correlations
    'def_ns_KZ_d8': float(1 - 2/(8*3)),
    'def_d_eff_required_BDI': d_eff_required,
    'def_d_eff_required_BCS': d_eff_BCS,
    'def_ns_with_log': ns_with_log,
    'def_target_ns': target_ns,
}

out_path = os.path.join(SCRIPT_DIR, 's48_qa_tachyon.npz')
np.savez_compressed(out_path, **output)
print(f"Saved data: {out_path}")


# ============================================================================
# 12. FINAL REPORT
# ============================================================================

print(f"\n{'='*72}")
print("QA-TACHYON-48: FINAL REPORT")
print("=" * 72)

print(f"""
BERRY-EDGE-48 (INFO):
  47 pi-phases (Z_2=-1 global). In the 0D limit (L/xi=0.031), inter-cell
  coupling t_inter = {t_inter:.4f} is too strong for gap opening at domain walls.
  {n_wall_states} wall-localized states found in 32-cell chain, but these are
  hybridized (not protected edge modes). True edge physics requires L >> xi.

DISSOLUTION-GOE-48 (INFO):
  8-mode BCS r-ratio at eps=0: {r_ratios[0.0]:.4f}. The V_8x8 intra-sector
  coupling already shifts <r> toward GOE. SFF shows no clean ramp at any
  epsilon in [0, eps_c]. The 8-mode system is too small for clean SFF analysis.
  At N=1232 (full truncation), eps_c = {eps_c:.6f} from S44 scaling.

VH-HIGHER-ORDER-48 (INFO):
  4-phonon B2-B2-B2-B2 scattering NOT forbidden by selection rules.
  (1,1)^4 contains (0,0) trivially. ||V^3||/||V|| = {ratio_4to2:.6f}.
  B2 protection is ENERGETIC (BIC flat band), not symmetry-based.

B3-REPULSIVE-48 (INFO):
  Repulsive V_B3B3 eigenvalue: {np.min(evals_VB3):+.4f} in (2,1) channel.
  No population inversion: Schwinger pair creation saturates all modes (n~1).
  B3 gap suppressed by {(1-correction_factor)*100:.1f}% (proximity still dominant).

THREE-PHONON-48 (INFO):
  omega_B2 / (2*omega_B1) = {omega_B2/(2*omega_B1):.4f} (detuning {detuning_frac*100:.2f}%).
  Gamma_3ph / gamma_H = {ratio_3ph:.6f}. The 3-phonon channel is perturbatively
  suppressed (V_B1B2^2/E ~ {V_3_eff:.4f}) and does NOT close the dissipation
  shortfall. The Lorentzian at detuning = {detuning:.4f} is broad (gamma_B2 = {gamma_B2:.4f}).

TRANSIT-279-48 (INFO):
  Slow-roll analogs: epsilon = {epsilon_SR:.4f}, eta = {eta_SR:.3f}.
  N_e = {N_eff_efolds:.4f} effective e-folds (transit duration << 1/H).
  The 279 tachyonic modes drive the transit; 713 stable modes resist.
  The transit is friction-limited (v_terminal = |dS/dtau| / (3H)).

EIGENVECTOR-48 (DEFERRED):
  See s48_eigenvectors.py for Dirac eigenvector analysis at the fold.

DEFECT-CORR-48 (FAIL):
  KZ defect correlations give n_s = 1 - 2*nu/(d_eff*(1+nu*z)).
  For BDI (nu=1, z=2, d=8): n_s = {1-2/(8*3):.4f}.
  Target n_s = {target_ns} requires d_eff = {d_eff_required:.1f} (unphysical).
  The KZ-defect route to the CMB spectral tilt is CLOSED.
  n_s remains an OPEN problem requiring non-KZ physics.

CONSTRAINT MAP UPDATE:
  - KZ defect correlations for n_s: CLOSED (d_eff insufficient at any physical dimension)
  - 4-phonon B2 protection: NOT symmetry-based (energetic BIC only)
  - 3-phonon channel: exists but perturbatively suppressed
  - Berry edge states in 0D limit: NOT topologically protected

Output: tier0-computation/s48_qa_tachyon.{{npz,png,py}}
""")
