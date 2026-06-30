#!/usr/bin/env python3
"""
s67_projected_moments.py -- PROJECTED-MOMENTS-67: Spectral Moments from
Richardson-Gaudin Exact Occupations
=====================================================================

Gate: PROJECTED-MOMENTS-67
  PASS: |delta_a_2 / a_2| < 10% at N_pair = 4
  FAIL: |delta_a_2 / a_2| > 20%
  INFO: intermediate (10-20%)

Physics:
--------
The spectral action on Jensen-deformed SU(3) uses BCS mean-field occupations
v_k^2 = (1/2)(1 - xi_k/E_k) to dress the D_K eigenvalue spectrum. The
spectral moments a_n^{BCS} are sums over all 1232 eigenvalues (at L_max=3)
weighted by the Bogoliubov quasiparticle energies:

    a_0^{BCS} = sum_j dim(p,q)^2 * 1                             (mode count)
    a_2^{BCS} = sum_j dim(p,q)^2 * 1/E_j^2    where E_j = sqrt(omega_j^2 + Delta^2)
    a_4^{BCS} = sum_j dim(p,q)^2 * 1/E_j^4

This replaces omega_j -> E_j = sqrt(omega_j^2 + Delta^2) uniformly, using a
SINGLE gap Delta from the mean-field BCS gap equation.

The Richardson-Gaudin (RG) exact solution, equivalently exact diagonalization
(ED) on the 8-mode reduced BCS Hamiltonian, gives DIFFERENT occupation numbers
n_k^{ED} for each of the 8 modes. These deviate from the BCS v_k^2 values,
especially at small N_pair (ultrasmall grain limit, Paper 17).

The key structural question: does replacing BCS v_k^2 with ED n_k change the
spectral moments significantly?

Method:
-------
The 8 BCS modes (4 B2, 1 B1, 3 B3) are sectors of the D_K spectrum. Each
sector s contains multiple D_K eigenvalues {omega_j^{(s)}}. The BCS dressing
replaces omega_j -> E_j^{(s)} = sqrt(omega_j^2 + Delta_s^2) where Delta_s
depends on the occupation of sector s.

For the mean-field BCS: Delta_s = Delta_0 (uniform gap, all modes).

For the ED exact solution: The occupation numbers n_k^{ED} imply a
mode-dependent effective gap. We reconstruct the effective gap from:
    n_k = v_k^2 = (1/2)(1 - xi_k / E_k)
    => E_k = |xi_k| / (1 - 2*n_k)  if n_k != 0.5
    => Delta_k = sqrt(E_k^2 - xi_k^2)

where xi_k = eps_k - mu_ED (the chemical potential solved self-consistently).

This gives an EFFECTIVE mode-dependent gap Delta_k^{ED} for each of the 8 modes.
The spectral action moments are then recomputed with this mode-dependent gap,
assigning each D_K eigenvalue to its sector and using the sector's effective gap.

The alternative approach: use n_k^{ED} directly in the spectral weight.
For the zeta-function moments:

    a_n^{ED} = sum_sectors_s [ sum_j_in_s dim(p,q)^2 * w_s * |omega_j|^{-n} ]

where w_s encodes the ED occupation effect. The two approaches are compared.

Cross-checks:
  1. N_pair = 1: ED is exact and well-benchmarked
  2. N_pair = 4 (half-filling): this is closest to the thermodynamic BCS limit
  3. Sum rule: sum(n_k^{ED}) = N_pair (exact by construction)
  4. BCS self-consistency: verify that BCS v_k^2 reproduce the canonical a2_fold

Author: Nazarewicz Nuclear-Structure Theorist (S67)
References:
  - Paper 02 (Dobaczewski et al.): HFB continuum
  - Paper 03 (Dobaczewski et al.): Odd-even staggering
  - Paper 15 (Dukelsky et al.): Richardson-Gaudin formalism
  - Paper 17 (von Delft & Ralph): Ultrasmall BCS grains
  - Paper 18 (Potel et al.): Pair transfer reactions

Session: S67 W2-B
"""

import sys
import os
import numpy as np
from itertools import combinations
from math import comb as mcomb
from scipy.linalg import eigh
from scipy.optimize import fsolve, minimize_scalar
import time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# === Path setup ===
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, str(_x2_shared_dir()))
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants (NEVER hardcode) ===
from canonical_constants import (
    tau_fold, Delta_0_OES, Delta_0_GL,
    a0_fold, a2_fold, a4_fold,
    S_fold, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
    E_cond, E_cond_ED_8mode,
    M_KK, M_KK_gravity,
    PI,
)

# === Import Dirac spectrum machinery ===
from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)
from spectral_action import dim_su3_irrep

# =============================================================================
# STEP 0: CONFIGURATION
# =============================================================================
print("=" * 78)
print("PROJECTED-MOMENTS-67: Spectral Moments from RG/ED Exact Occupations")
print("=" * 78)
print()

Delta_0 = Delta_0_OES  # = 0.4643 M_KK (canonical BCS gap)
print(f"  Delta_0 (BCS gap, OES) = {Delta_0:.6f} M_KK")
print(f"  tau_fold               = {tau_fold}")
print(f"  a0_fold (canonical)    = {a0_fold}")
print(f"  a2_fold (canonical)    = {a2_fold:.4f}")
print(f"  a4_fold (canonical)    = {a4_fold:.4f}")
print()

# =============================================================================
# STEP 1: LOAD 8-MODE BCS DATA FROM S52
# =============================================================================
print("=" * 78)
print("STEP 1: Load 8-mode BCS spectrum and ED occupations from S52")
print("=" * 78)

hfb_data = np.load(os.path.join(SCRIPT_DIR, 's52_hfb_full.npz'), allow_pickle=True)
eps_bare = hfb_data['E_sp_bare']       # 8 single-particle energies (M_KK)
V_bare = hfb_data['V_bare']            # 8x8 pairing interaction (M_KK)
labels = list(hfb_data['labels'])      # ['B2[0]','B2[1]','B2[2]','B2[3]','B1','B3[0]','B3[1]','B3[2]']
N_modes = len(eps_bare)

print(f"  N_modes = {N_modes}")
print(f"  eps_bare = {eps_bare}")
print(f"  labels = {labels}")
print()

# Cross-check mode energies against canonical constants
assert abs(eps_bare[4] - E_B1) < 1e-6, f"B1 energy mismatch: {eps_bare[4]} vs {E_B1}"
assert abs(np.mean(eps_bare[:4]) - E_B2_mean) < 1e-4, f"B2 mean mismatch"
assert abs(np.mean(eps_bare[5:]) - E_B3_mean) < 1e-4, f"B3 mean mismatch"
print("  Cross-check: mode energies match canonical constants. PASSED.")
print()

# Sector assignment: which sector does each of the 8 BCS modes belong to?
# B1 ~ (0,0) or dominant sector, B2 ~ (1,0)/(0,1), B3 ~ higher sectors
# In the framework:
#   B2 modes (indices 0-3): eps ~ 0.845, 4-fold degenerate
#   B1 mode  (index 4):     eps ~ 0.819, singlet
#   B3 modes (indices 5-7): eps ~ 0.978, 3-fold degenerate
# These are the LOWEST eigenvalues of D_K in their respective sectors.

# Extract ED occupations for N_pair = 1, 2, 3, 4
ed_data = {}
for N in [1, 2, 3, 4]:
    ed_data[N] = {
        'n_k': hfb_data[f'N{N}_n_k_ed'],
        'E': float(hfb_data[f'N{N}_E_ed']),
        'n_k_hfb': hfb_data[f'N{N}_n_k_hfb'],
    }
    print(f"  N_pair={N}: E_ed={ed_data[N]['E']:.6f}, n_k_ed = {ed_data[N]['n_k']}")
    print(f"             sum(n_k) = {np.sum(ed_data[N]['n_k']):.6f}")

print()

# =============================================================================
# STEP 2: SOLVE BCS GAP EQUATION FOR MEAN-FIELD OCCUPATIONS
# =============================================================================
print("=" * 78)
print("STEP 2: BCS Mean-Field Occupations at Each N_pair")
print("=" * 78)


def bcs_gap_equations(params, eps, Delta, N_target):
    """BCS gap + number equations for uniform coupling g."""
    mu, g = params
    E_k = np.sqrt((eps - mu)**2 + Delta**2)
    v2 = 0.5 * (1.0 - (eps - mu) / E_k)
    number_eq = np.sum(v2) - N_target
    gap_eq = 1.0 / g - 0.5 * np.sum(1.0 / E_k)
    return [number_eq, gap_eq]


bcs_data = {}
for N in [1, 2, 3, 4]:
    mu0 = np.mean(eps_bare)
    g0 = 0.15  # (local)
    sol = fsolve(bcs_gap_equations, [mu0, g0],
                 args=(eps_bare, Delta_0, N), full_output=True)
    mu_sol, g_sol = sol[0]
    info = sol[1]

    E_k_bcs = np.sqrt((eps_bare - mu_sol)**2 + Delta_0**2)
    v2_bcs = 0.5 * (1.0 - (eps_bare - mu_sol) / E_k_bcs)

    bcs_data[N] = {
        'mu': mu_sol,
        'g': g_sol,
        'E_k': E_k_bcs,
        'v2': v2_bcs,
    }
    print(f"  N_pair={N}: mu={mu_sol:.6f}, g={g_sol:.6f}")
    print(f"    v2_BCS = {v2_bcs}")
    print(f"    sum(v2) = {np.sum(v2_bcs):.6f}")

print()

# =============================================================================
# STEP 3: COMPUTE D_K EIGENVALUE SPECTRUM AT THE FOLD
# =============================================================================
print("=" * 78)
print("STEP 3: Compute D_K Eigenvalue Spectrum at tau_fold")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

t_start = time.time()
all_evals, eval_data = collect_spectrum(
    tau_fold, gens, f_abc, gammas, max_pq_sum=3, verbose=True
)
t_spec = time.time() - t_start
print(f"  Spectrum computation time: {t_spec:.1f}s")

# Organize spectrum by sector
# eval_data is list of (p, q, eigenvalues_array)
sector_info = []
total_modes = 0  # (local)
for p, q, evals in eval_data:
    d_pq = dim_su3_irrep(p, q)
    omega = np.abs(evals)
    omega_min = np.min(omega)
    sector_info.append({
        'p': p, 'q': q,
        'dim': d_pq,
        'evals': omega,       # |eigenvalues| (all positive)
        'n_evals': len(evals),
        'omega_min': omega_min,
    })
    total_modes += len(evals)
    # Each eigenvalue has PW multiplicity dim(p,q)
    # Total with multiplicity: sum_sector dim(p,q) * n_evals_per_sector

print(f"\n  Total distinct eigenvalues: {total_modes}")
print(f"  Sectors: {len(sector_info)}")
for si in sector_info:
    print(f"    ({si['p']},{si['q']}): dim={si['dim']}, "
          f"n_evals={si['n_evals']}, omega_min={si['omega_min']:.6f}")

# =============================================================================
# STEP 4: COMPUTE BARE SPECTRAL MOMENTS (NO PAIRING)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Bare Spectral Moments (No Pairing)")
print("=" * 78)

# a_n = sum_{sectors} dim(p,q)^2 * sum_j |omega_j|^{2-n}  [for spectral zeta]
# Actually, the canonical a_n are Seeley-DeWitt coefficients, which for zeta:
# a_0 = sum dim(p,q)^2 * n_j  (mode count with PW weight)
# a_2 = sum dim(p,q)^2 * 1/omega_j^2
# a_4 = sum dim(p,q)^2 * 1/omega_j^4
# Wait -- let me check the S65 convention. S65 uses:
# a2_bare_zeta[i] = sum over all sectors of sum(1/omega^2) WITHOUT PW mult
# But the canonical a2_fold = 2776.17 includes PW multiplicity dim^2.
# Let me verify by computing both ways.

# Method A: With PW multiplicity dim^2 (used in S_full formula)
a0_computed_pw = 0.0  # (local)
a2_computed_pw = 0.0  # (local)
a4_computed_pw = 0.0  # (local)
S_computed_pw = 0.0  # (local)

# Method B: Without PW multiplicity (diagnostic, as in S65 zeta)
a0_computed_nopw = 0.0  # (local)
a2_computed_nopw = 0.0  # (local)
a4_computed_nopw = 0.0  # (local)

for si in sector_info:
    d = si['dim']
    omega = si['evals']

    # With PW mult = dim^2
    a0_computed_pw += d**2 * len(omega)
    a2_computed_pw += d**2 * np.sum(1.0 / omega**2)
    a4_computed_pw += d**2 * np.sum(1.0 / omega**4)
    S_computed_pw += d**2 * np.sum(omega)

    # Without PW mult
    a0_computed_nopw += len(omega)
    a2_computed_nopw += np.sum(1.0 / omega**2)
    a4_computed_nopw += np.sum(1.0 / omega**4)

print(f"  Bare moments WITH PW multiplicity (dim^2):")
print(f"    a0 = {a0_computed_pw:.1f}")
print(f"    a2 = {a2_computed_pw:.4f}")
print(f"    a4 = {a4_computed_pw:.4f}")
print(f"    S_full = {S_computed_pw:.2f}")
print()
print(f"  Bare moments WITHOUT PW multiplicity:")
print(f"    a0 = {a0_computed_nopw:.1f}")
print(f"    a2 = {a2_computed_nopw:.4f}")
print(f"    a4 = {a4_computed_nopw:.4f}")

# Determine which convention matches canonical
dev_pw_a2 = abs(a2_computed_pw - a2_fold) / a2_fold
dev_nopw_a2 = abs(a2_computed_nopw - a2_fold) / a2_fold
print(f"\n  Cross-check against a2_fold = {a2_fold:.4f}:")
print(f"    PW:   |a2_pw - a2_fold| / a2_fold   = {dev_pw_a2:.6e}")
print(f"    NoPW: |a2_nopw - a2_fold| / a2_fold = {dev_nopw_a2:.6e}")

# Check S_full
dev_S = abs(S_computed_pw - S_fold) / S_fold
print(f"  Cross-check against S_fold = {S_fold:.2f}:")
print(f"    |S_pw - S_fold| / S_fold = {dev_S:.6e}")

# The S65 script uses NOPW for the zeta moments but PW for S_full.
# The canonical a2_fold and a4_fold may use a different normalization.
# Let me check.
print()

# From the S65 output: a2_bare_zeta at tau_fold ~ 592
# The canonical a2_fold = 2776.17
# So canonical includes PW multiplicity, but the ratio suggests another factor.
# Let me trace through more carefully.

# Actually, looking at s65_bcs_dressed_sa.py lines 167-171:
# a2b_i += np.sum(1.0 / omega**2)  <-- NO PW mult
# And the S65 data shows a2_bare_zeta[fold] = 592.00
# But canonical a2_fold = 2776.17
# So a2_fold is NOT the same as the zeta function moments computed in S65.
# The canonical a2_fold comes from the heat kernel expansion, not the zeta.

# For THIS computation, what matters is the RELATIVE change:
#   delta_a2 / a2 = (a2^{ED} - a2^{BCS}) / a2^{BCS}
# This ratio is convention-independent (PW mult cancels).

# I will compute both conventions but report the ratio.

# Use the S65-style (no PW) as the base for the BCS reference, since
# it matches what S65 computed.
a2_bare = a2_computed_nopw
a4_bare = a4_computed_nopw

print(f"  Using NO-PW convention for moment ratios (PW cancels in ratios)")
print(f"  a2_bare = {a2_bare:.4f}")
print(f"  a4_bare = {a4_bare:.4f}")

# =============================================================================
# STEP 5: MAP 8-MODE SECTORS TO D_K EIGENVALUE GROUPS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Map 8 BCS Modes to D_K Eigenvalue Sectors")
print("=" * 78)

# The 8 BCS modes are grouped by their single-particle energies:
#   B2: eps ~ 0.845 (4-fold degenerate)
#   B1: eps ~ 0.819 (singlet)
#   B3: eps ~ 0.978 (3-fold degenerate)
#
# These correspond to the LOWEST eigenvalues of D_K in the respective
# Peter-Weyl sectors. The D_K spectrum at L_max=3 has eigenvalues from
# multiple sectors (0,0), (1,0), (0,1), ..., (3,0), etc.
#
# The mapping: the 8-mode reduced BCS Hamiltonian uses the 8 lowest
# distinct eigenvalue groups of D_K. The sectors of D_K that contain
# these eigenvalues are identified by matching omega_min.

# Key insight: In the BCS framework, the pairing gap Delta enters
# the spectral action by replacing omega -> sqrt(omega^2 + Delta^2).
# The BCS mean-field uses a UNIFORM Delta for all modes.
# The exact ED solution has mode-dependent occupation numbers n_k.
#
# For the spectral action modification:
# - BCS: all eigenvalues get the same Delta -> E_j = sqrt(omega_j^2 + Delta^2)
# - ED: each mode k has a different effective gap Delta_k^{eff}
#
# The effective gap is extracted from the ED occupations:
#   n_k = v_k^2 = (1/2)(1 - xi_k / E_k)
#   xi_k = eps_k - mu
#   E_k = sqrt(xi_k^2 + Delta_k^2)
#
# Solving: Delta_k = |xi_k| * sqrt(2*n_k / (1 - 2*n_k)) if n_k < 0.5
#          Delta_k -> infty if n_k = 0.5 (fully paired)
#
# However, this approach has a subtlety: the ED ground state is not
# a BCS product state, so the "effective gap" is an approximation.
# The proper quantity is the pairing tensor kappa_k = <c_{-k} c_k>,
# not directly available from the ED occupation numbers alone.
#
# CORRECT APPROACH: Use the occupation numbers directly in the
# spectral weight, without assuming a BCS product state.
# The BCS-dressed spectral action in S65 uses:
#   E_j = sqrt(omega_j^2 + Delta^2)
# This is equivalent to shifting each eigenvalue by the gap.
# With ED occupations, the proper analog is:
#
# For each mode k (of the 8), define an effective quasiparticle energy:
#   E_k^{eff} = eps_k / (1 - 2*n_k)  if n_k < 0.5
#
# Then the "effective gap" is:
#   Delta_k^{eff} = sqrt((E_k^{eff})^2 - (eps_k - mu)^2)
#
# And the spectral moment from sector k's D_K eigenvalues is:
#   a_n^{(k)} = sum_{j in k} |omega_j|^{-n} -> becomes a_n^{(k,dressed)}
#   where each omega_j in sector k is dressed with Delta_k^{eff}
#
# SIMPLER AND MORE ROBUST APPROACH:
# The spectral action with BCS dressing computes:
#   S^{BCS} = sum_j sqrt(omega_j^2 + Delta^2)
# The correction from exact occupations comes from the fact that the
# true ground state has a DIFFERENT pairing tensor kappa from the
# mean-field BCS. The ratio:
#   r_n(k) = a_n^{ED}(k) / a_n^{BCS}(k)
# for each sector k measures the deviation.
#
# MOST DIRECT APPROACH (used here):
# The spectral moments are weighted sums over eigenvalues.
# The mean-field BCS dresses ALL eigenvalues identically: omega -> sqrt(omega^2 + Delta^2).
# With ED occupations, each of the 8 mode sectors gets a different effective
# dressing factor. The dressing factor for sector k is:
#   f_k^{BCS} = sqrt(omega_k^2 + Delta_0^2) / omega_k  (uniform BCS)
#   f_k^{ED} = effective dressing from ED occupations
#
# To extract f_k^{ED}, use the identity:
# In BCS: v_k^2 = (1/2)(1 - xi_k/E_k) where E_k = sqrt(xi_k^2 + Delta^2)
# In ED: n_k = <n_k>_ED (exact)
# The effective quasiparticle energy:
#   E_k^{ED} = |xi_k| / |1 - 2*n_k|  (from inverting BCS occupation formula)
# And the effective gap:
#   Delta_k^{ED} = sqrt(max(0, (E_k^{ED})^2 - xi_k^2))
#
# Then ALL D_K eigenvalues in sector k are dressed with Delta_k^{ED} instead
# of Delta_0.
#
# This is the projected-moments approach: project the exact many-body
# occupation numbers onto an effective mode-dependent gap.

# First, assign each of the 8 modes to a D_K sector group.
# The 8 modes correspond to the 3 distinct energy levels:
# Level 0 (B1): eps = 0.81914,  degeneracy 1
# Level 1 (B2): eps = 0.84527,  degeneracy 4
# Level 2 (B3): eps = 0.97822,  degeneracy 3

# In the D_K spectrum, these correspond to eigenvalue groups.
# ALL D_K eigenvalues are organized by sector (p,q).
# The sectors with omega_min close to the mode energies are identified.

print("\n  8-mode energy structure:")
print(f"    B1 (1 mode):  eps = {eps_bare[4]:.6f}")
print(f"    B2 (4 modes): eps = {eps_bare[0]:.6f}")
print(f"    B3 (3 modes): eps = {eps_bare[5]:.6f}")

# Match D_K sectors to the 3 energy groups
for si in sector_info:
    # Check if omega_min matches any of the 3 mode energies
    match_B1 = abs(si['omega_min'] - eps_bare[4])
    match_B2 = abs(si['omega_min'] - eps_bare[0])
    match_B3 = abs(si['omega_min'] - eps_bare[5])
    best = min(match_B1, match_B2, match_B3)
    if best == match_B1:
        si['mode_group'] = 'B1'
    elif best == match_B2:
        si['mode_group'] = 'B2'
    else:
        si['mode_group'] = 'B3'
    print(f"    Sector ({si['p']},{si['q']}): omega_min={si['omega_min']:.6f}, "
          f"closest to {si['mode_group']}")

# CRITICAL STRUCTURAL POINT:
# In the D_K spectrum, the vast majority of eigenvalues are in HIGHER sectors
# that are NOT included in the 8-mode BCS Hamiltonian. The BCS pairing acts
# only on the modes near the Fermi surface -- the 8 lowest energy groups.
# The higher eigenvalues (omega >> Delta) are effectively undressed by pairing
# because sqrt(omega^2 + Delta^2) ~ omega for omega >> Delta.
#
# Therefore, the pairing correction to the spectral moments comes ENTIRELY
# from the low-lying modes. The high-energy modes contribute the dominant
# part of a0, a2, a4 but are unaffected by pairing.
#
# The question is: what fraction of a2 comes from modes affected by pairing?

# =============================================================================
# STEP 6: COMPUTE BCS-DRESSED SPECTRAL MOMENTS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: BCS-Dressed vs ED-Dressed Spectral Moments")
print("=" * 78)


def compute_dressed_moments(sector_info, delta_map):
    """
    Compute spectral moments with mode-dependent gap Delta.

    delta_map: dict mapping mode_group ('B1','B2','B3','HIGHER') to Delta value.
    Each D_K eigenvalue omega_j in a sector assigned to mode_group g is dressed:
        E_j = sqrt(omega_j^2 + delta_map[g]^2)

    Returns a0, a2, a4 (without PW mult, for ratio computation).
    """
    a0 = 0.0  # (local)
    a2 = 0.0  # (local)
    a4 = 0.0  # (local)
    S = 0.0  # (local)

    for si in sector_info:
        omega = si['evals']
        group = si.get('mode_group', 'HIGHER')
        delta = delta_map.get(group, 0.0)

        E = np.sqrt(omega**2 + delta**2)

        a0 += len(omega)
        a2 += np.sum(1.0 / E**2)
        a4 += np.sum(1.0 / E**4)
        S += np.sum(E)

    return a0, a2, a4, S


def compute_dressed_moments_pw(sector_info, delta_map):
    """Same as above but with PW multiplicity dim^2."""
    a0 = 0.0  # (local)
    a2 = 0.0  # (local)
    a4 = 0.0  # (local)
    S = 0.0  # (local)

    for si in sector_info:
        d = si['dim']
        omega = si['evals']
        group = si.get('mode_group', 'HIGHER')
        delta = delta_map.get(group, 0.0)

        E = np.sqrt(omega**2 + delta**2)

        a0 += d**2 * len(omega)
        a2 += d**2 * np.sum(1.0 / E**2)
        a4 += d**2 * np.sum(1.0 / E**4)
        S += d**2 * np.sum(E)

    return a0, a2, a4, S


# --- 6a: BCS Mean-Field Moments (uniform Delta_0 on all modes) ---
delta_bcs_uniform = {'B1': Delta_0, 'B2': Delta_0, 'B3': Delta_0}
a0_bcs, a2_bcs, a4_bcs, S_bcs = compute_dressed_moments(sector_info, delta_bcs_uniform)
a0_bcs_pw, a2_bcs_pw, a4_bcs_pw, S_bcs_pw = compute_dressed_moments_pw(
    sector_info, delta_bcs_uniform)

print(f"  BCS Mean-Field (uniform Delta = {Delta_0:.4f}):")
print(f"    a0_BCS = {a0_bcs:.1f}   (PW: {a0_bcs_pw:.1f})")
print(f"    a2_BCS = {a2_bcs:.4f}   (PW: {a2_bcs_pw:.4f})")
print(f"    a4_BCS = {a4_bcs:.4f}   (PW: {a4_bcs_pw:.4f})")
print(f"    S_BCS  = {S_bcs:.2f}    (PW: {S_bcs_pw:.2f})")
print()

# Cross-check: ratio r2 = a2_bcs / a2_bare should match S65 value of ~0.892
r2_check = a2_bcs / a2_bare
print(f"  Cross-check: r_2 = a2_BCS / a2_bare = {r2_check:.6f} (S65: 0.892)")
print()

# --- 6b: ED-Dressed Moments for each N_pair ---
print("  Computing ED-dressed moments for N_pair = 1, 2, 3, 4:")
print()

results = {}

for N in [1, 2, 3, 4]:
    print(f"  --- N_pair = {N} ---")

    n_k_ed = ed_data[N]['n_k']
    n_k_bcs = bcs_data[N]['v2']
    mu_bcs = bcs_data[N]['mu']

    # Compute effective mode-dependent gap from ED occupations
    # For each energy group, average the ED occupations over degenerate modes

    # B2: modes 0-3
    n_B2_ed = np.mean(n_k_ed[:4])
    n_B2_bcs = np.mean(n_k_bcs[:4])
    eps_B2 = np.mean(eps_bare[:4])

    # B1: mode 4
    n_B1_ed = n_k_ed[4]
    n_B1_bcs = n_k_bcs[4]
    eps_B1 = eps_bare[4]

    # B3: modes 5-7
    n_B3_ed = np.mean(n_k_ed[5:])
    n_B3_bcs = np.mean(n_k_bcs[5:])
    eps_B3 = np.mean(eps_bare[5:])

    print(f"    Group occupations (ED vs BCS):")
    print(f"      B1: n_ED={n_B1_ed:.6f}, n_BCS={n_B1_bcs:.6f}, "
          f"delta_n={n_B1_ed - n_B1_bcs:.6f}")
    print(f"      B2: n_ED={n_B2_ed:.6f}, n_BCS={n_B2_bcs:.6f}, "
          f"delta_n={n_B2_ed - n_B2_bcs:.6f}")
    print(f"      B3: n_ED={n_B3_ed:.6f}, n_BCS={n_B3_bcs:.6f}, "
          f"delta_n={n_B3_ed - n_B3_bcs:.6f}")

    # Extract effective gap from ED occupations
    # n = (1/2)(1 - xi/E) => E = |xi| / |1 - 2n|
    # Delta_eff = sqrt(E^2 - xi^2)
    # Note: need mu_ED. For the ED ground state, there is no mu (canonical
    # ensemble). Use the BCS mu as a reference (this is an approximation --
    # we are projecting the exact state onto a BCS-like parametrization).

    def effective_gap(eps, mu, n_k):
        """Extract effective gap from occupation number."""
        xi = eps - mu
        if abs(1.0 - 2.0 * n_k) < 1e-10:
            return np.inf  # half-filled => maximally paired
        E_eff = abs(xi) / abs(1.0 - 2.0 * n_k)
        Delta_sq = E_eff**2 - xi**2
        if Delta_sq < 0:
            # Negative Delta^2 means the occupation is outside BCS regime
            # This happens when n_k > 0.5 with xi > 0 (above Fermi surface)
            # or n_k < 0.5 with xi < 0 (below Fermi surface but underpaired)
            return 0.0
        return np.sqrt(Delta_sq)

    # Compute ED chemical potential: solve number equation with ED occupations
    # Use the mean-field mu as starting point, adjust to match N
    # For the effective gap extraction, the key quantity is xi_k = eps_k - mu
    # We use the BCS mu which already satisfies sum(v2) = N

    mu_ed = mu_bcs  # Use BCS mu (the projection approximation)

    Delta_B1_eff = effective_gap(eps_B1, mu_ed, n_B1_ed)
    Delta_B2_eff = effective_gap(eps_B2, mu_ed, n_B2_ed)
    Delta_B3_eff = effective_gap(eps_B3, mu_ed, n_B3_ed)

    print(f"    Effective gaps (mu={mu_ed:.6f}):")
    print(f"      Delta_B1_eff = {Delta_B1_eff:.6f} M_KK "
          f"(BCS: {Delta_0:.6f}, ratio: {Delta_B1_eff/Delta_0:.4f})")
    print(f"      Delta_B2_eff = {Delta_B2_eff:.6f} M_KK "
          f"(BCS: {Delta_0:.6f}, ratio: {Delta_B2_eff/Delta_0:.4f})")
    print(f"      Delta_B3_eff = {Delta_B3_eff:.6f} M_KK "
          f"(BCS: {Delta_0:.6f}, ratio: {Delta_B3_eff/Delta_0:.4f})")

    # Compute ED-dressed spectral moments
    delta_ed = {'B1': Delta_B1_eff, 'B2': Delta_B2_eff, 'B3': Delta_B3_eff}
    a0_ed, a2_ed, a4_ed, S_ed = compute_dressed_moments(sector_info, delta_ed)

    # Also compute using the individual (non-averaged) ED occupations for
    # each mode, to estimate the error from degeneracy averaging
    Delta_modes_ed = np.zeros(N_modes)
    for k in range(N_modes):
        Delta_modes_ed[k] = effective_gap(eps_bare[k], mu_ed, n_k_ed[k])

    # For the mode-resolved approach, assign each D_K sector a gap from
    # the mode with matching energy. Since B2 modes are 4-fold degenerate
    # in the D_K spectrum, all B2-matched sectors use the same eigenvalue
    # group.
    # The non-averaged gaps:
    Delta_B2_modes = Delta_modes_ed[:4]  # individual B2 mode gaps
    Delta_B1_mode = Delta_modes_ed[4]
    Delta_B3_modes = Delta_modes_ed[5:]

    print(f"    Mode-resolved gaps (non-averaged):")
    print(f"      B2 modes: {Delta_B2_modes}")
    print(f"      B1 mode:  {Delta_B1_mode:.6f}")
    print(f"      B3 modes: {Delta_B3_modes}")

    # For the spectral moments, use the averaged gap per group (the D_K
    # sector assignment is by group, not by individual mode)
    # Deviation from averaging:
    if len(Delta_B2_modes[Delta_B2_modes > 0]) > 0:
        Delta_B2_spread = np.std(Delta_B2_modes) / np.mean(Delta_B2_modes) \
            if np.mean(Delta_B2_modes) > 0 else 0.0
    else:
        Delta_B2_spread = 0.0  # (local)
    if len(Delta_B3_modes[Delta_B3_modes > 0]) > 0:
        Delta_B3_spread = np.std(Delta_B3_modes) / np.mean(Delta_B3_modes) \
            if np.mean(Delta_B3_modes) > 0 else 0.0
    else:
        Delta_B3_spread = 0.0  # (local)

    print(f"    Gap spread within groups (CV):")
    print(f"      B2: {Delta_B2_spread:.4f}")
    print(f"      B3: {Delta_B3_spread:.4f}")

    # Compute ratios
    delta_a0 = (a0_ed - a0_bcs) / a0_bcs
    delta_a2 = (a2_ed - a2_bcs) / a2_bcs
    delta_a4 = (a4_ed - a4_bcs) / a4_bcs
    delta_S = (S_ed - S_bcs) / S_bcs

    print(f"\n    Spectral moment changes (ED vs BCS):")
    print(f"      delta_a0 / a0 = {delta_a0:+.6e}  (should be 0, mode count unchanged)")
    print(f"      delta_a2 / a2 = {delta_a2:+.6e}  ({delta_a2*100:+.4f}%)")
    print(f"      delta_a4 / a4 = {delta_a4:+.6e}  ({delta_a4*100:+.4f}%)")
    print(f"      delta_S  / S  = {delta_S:+.6e}   ({delta_S*100:+.4f}%)")
    print()

    # Store results
    results[N] = {
        'n_k_ed': n_k_ed,
        'n_k_bcs': n_k_bcs,
        'Delta_B1_eff': Delta_B1_eff,
        'Delta_B2_eff': Delta_B2_eff,
        'Delta_B3_eff': Delta_B3_eff,
        'a0_ed': a0_ed,
        'a2_ed': a2_ed,
        'a4_ed': a4_ed,
        'S_ed': S_ed,
        'delta_a0': delta_a0,
        'delta_a2': delta_a2,
        'delta_a4': delta_a4,
        'delta_S': delta_S,
        'Delta_B2_spread': Delta_B2_spread,
        'Delta_B3_spread': Delta_B3_spread,
    }

# =============================================================================
# STEP 7: ALTERNATIVE METHOD -- DIRECT OCCUPATION WEIGHTING
# =============================================================================
print("=" * 78)
print("STEP 7: Alternative Method -- Direct Occupation Weighting")
print("=" * 78)
print()
print("  The effective-gap method in Step 6 projects the exact state onto a")
print("  BCS-like parametrization. An alternative is to directly weight the")
print("  spectral moments by the occupation-dependent factor.")
print()
print("  In BCS mean-field, the spectral action uses:")
print("    S = sum_j sqrt(omega_j^2 + Delta^2)")
print("  This can be rewritten as:")
print("    S = sum_j omega_j * sqrt(1 + Delta^2/omega_j^2)")
print("  The BCS correction factor is r_j = sqrt(1 + Delta^2/omega_j^2).")
print()
print("  The BCS occupation v_k^2 determines this correction through:")
print("    v_k^2 = (1/2)(1 - xi_k/E_k)")
print("  where E_k = omega_k * r_k (approximately, for small mu).")
print()
print("  Direct method: compute the ratio of ED-to-BCS contributions")
print("  mode-by-mode and apply as a multiplicative correction to the")
print("  spectral moments.")
print()

# For each N_pair, compute the occupation-ratio correction
for N in [1, 2, 3, 4]:
    n_k_ed = ed_data[N]['n_k']
    n_k_bcs = bcs_data[N]['v2']

    # Average over degenerate groups
    n_groups_ed = [n_k_ed[4], np.mean(n_k_ed[:4]), np.mean(n_k_ed[5:])]
    n_groups_bcs = [n_k_bcs[4], np.mean(n_k_bcs[:4]), np.mean(n_k_bcs[5:])]
    group_names = ['B1', 'B2', 'B3']

    print(f"  N_pair = {N}:")
    for i, gn in enumerate(group_names):
        ratio = n_groups_ed[i] / n_groups_bcs[i] if n_groups_bcs[i] > 1e-15 else float('inf')
        print(f"    {gn}: n_ED/n_BCS = {ratio:.4f} "
              f"(n_ED={n_groups_ed[i]:.6f}, n_BCS={n_groups_bcs[i]:.6f})")
    print()

# =============================================================================
# STEP 8: RICHARDSON-GAUDIN EXACT SOLUTION
# =============================================================================
print("=" * 78)
print("STEP 8: Richardson-Gaudin Exact Pair Energies")
print("=" * 78)
print()
print("  Solving the RG equations for the exact pair amplitudes E_alpha.")
print("  RG eq: 1/G + Sum_j 1/(2*eps_j - E_alpha) - Sum_{b!=a} 2/(E_b - E_a) = 0")
print("  for N_pair coupled equations for E_1, ..., E_{N_pair}.")
print()


def rg_equations(E_pairs, eps, G, N_modes):
    """
    Richardson-Gaudin equations.
    E_pairs: array of N_pair pair energies
    eps: array of N_modes single-particle energies
    G: pairing strength

    Returns residuals (should all be 0).
    """
    N_pair = len(E_pairs)
    residuals = np.zeros(N_pair)

    for alpha in range(N_pair):
        E_a = E_pairs[alpha]

        # Sum over single-particle levels
        sp_sum = np.sum(1.0 / (2.0 * eps - E_a))

        # Sum over other pair energies
        pair_sum = 0.0  # (local)
        for beta in range(N_pair):
            if beta != alpha:
                pair_sum += 2.0 / (E_pairs[beta] - E_a)

        residuals[alpha] = 1.0 / G + sp_sum - pair_sum

    return residuals


def rg_occupation(E_pairs, eps, G):
    """
    Compute occupation numbers from RG solution.

    For the RG ground state with pair energies {E_alpha}:
    n_j = sum_alpha |psi_j^alpha|^2 where psi_j^alpha is the pair amplitude.

    In the electrostatic analogy (Gaudin), the occupation of level j is:
    n_j = Sum_alpha 1 / (2*eps_j - E_alpha)^2 * (normalization)

    More precisely, the occupation numbers are related to the residues of
    the Richardson ansatz wavefunction. For the ground state:

    n_j = -d/d(eps_j) * sum_alpha ln(2*eps_j - E_alpha) / (d/dG * ...)

    This is complex to implement exactly. Instead, use the simpler formula
    valid for the RG ground state:

    The probability that level j is occupied in the RG ground state is:
    n_j = <GS| n_j |GS> = sum_alpha |c_j^alpha|^2

    For a separable pairing interaction with N_pair pairs, the exact occupation
    can be computed from the Bethe ansatz normalization. For our purposes,
    we use exact diagonalization (which we already have) as the benchmark.
    """
    pass  # We use ED occupations instead (already loaded from S52)


# Solve RG equations for each N_pair
rg_results = {}

for N in [1, 2, 3, 4]:
    print(f"  --- N_pair = {N} ---")

    # Use g from BCS gap equation (uniform coupling)
    g = bcs_data[N]['g']
    mu = bcs_data[N]['mu']
    print(f"    G = {g:.6f} M_KK")

    # Initial guess: pair energies near 2*eps_low - g (bound pair below 2*eps)
    eps_sorted = np.sort(eps_bare)
    E0_guess = []
    for i in range(N):
        # Start below 2*eps of the i-th lowest level
        E0_guess.append(2.0 * eps_sorted[min(i, len(eps_sorted)-1)] - 0.5 * g * (i + 1))
    E0_guess = np.array(E0_guess)

    # Add small random perturbation to break symmetry for degenerate levels
    np.random.seed(42 + N)
    E0_guess += np.random.randn(N) * 0.001

    # Solve
    from scipy.optimize import fsolve as fsolve2
    sol = fsolve2(rg_equations, E0_guess, args=(eps_bare, g, N_modes),
                  full_output=True)
    E_pairs_rg = sol[0]
    info_rg = sol[1]
    converged = sol[2] == 1

    # Check residual
    residual = np.max(np.abs(rg_equations(E_pairs_rg, eps_bare, g, N_modes)))

    print(f"    Converged: {converged}")
    print(f"    Max residual: {residual:.6e}")
    print(f"    Pair energies: {np.sort(E_pairs_rg)}")

    # Total energy from RG
    E_total_rg = np.sum(E_pairs_rg)
    E_total_ed = ed_data[N]['E']
    # Note: RG uses separable V (uniform g), ED uses full V_bare.
    # They will not match exactly due to non-separable component.

    print(f"    E_total_RG = {E_total_rg:.6f} M_KK")
    print(f"    E_total_ED = {E_total_ed:.6f} M_KK (full V)")
    print(f"    Difference: {E_total_rg - E_total_ed:.6f} M_KK "
          f"({(E_total_rg - E_total_ed)/E_total_ed * 100:.4f}%)")
    print()

    # For RG occupations: we need the exact occupation from the RG wavefunction.
    # For the separable pairing Hamiltonian, the occupation is:
    #   n_j = sum_alpha prod_{beta != alpha} (2*eps_j - E_beta) /
    #                  prod_{beta != alpha} (E_alpha - E_beta)
    #          * 1 / prod_{gamma} (2*eps_j - E_gamma)
    #
    # This is actually computed from the norm of the Richardson ansatz.
    # For implementation, we use the formula from Paper 15 (Dukelsky et al.):
    #
    #   n_j = -dE_total/d(eps_j) = -sum_alpha dE_alpha/d(eps_j)
    #
    # From the implicit function theorem on the RG equations:
    # The Jacobian J_{alpha,beta} = d(RG_eq_alpha)/d(E_beta)
    # The forcing: f_{alpha,j} = d(RG_eq_alpha)/d(eps_j)
    # Then: dE_beta/d(eps_j) = -J^{-1}_{beta,alpha} * f_{alpha,j}
    # And: n_j = sum_{beta,alpha} J^{-1}_{beta,alpha} * f_{alpha,j}

    # Compute Jacobian of RG equations w.r.t. E_pairs
    J = np.zeros((N, N))
    for alpha in range(N):
        E_a = E_pairs_rg[alpha]
        # d(RG_alpha)/d(E_alpha)
        J[alpha, alpha] = np.sum(1.0 / (2.0 * eps_bare - E_a)**2)
        for beta in range(N):
            if beta != alpha:
                J[alpha, alpha] -= 2.0 / (E_pairs_rg[beta] - E_a)**2
        # d(RG_alpha)/d(E_beta), beta != alpha
        for beta in range(N):
            if beta != alpha:
                J[alpha, beta] = 2.0 / (E_pairs_rg[beta] - E_a)**2

    # Compute forcing d(RG_alpha)/d(eps_j)
    f_matrix = np.zeros((N, N_modes))
    for alpha in range(N):
        E_a = E_pairs_rg[alpha]
        for j in range(N_modes):
            f_matrix[alpha, j] = -2.0 / (2.0 * eps_bare[j] - E_a)**2

    # Solve J * dE/deps = -f
    try:
        J_inv = np.linalg.inv(J)
        # dE_beta/d(eps_j) = -sum_alpha J^{-1}_{beta,alpha} * f_{alpha,j}
        dE_deps = -J_inv @ f_matrix  # shape (N, N_modes)
        # n_j = -sum_beta dE_beta/d(eps_j) = sum_{beta,alpha} J^{-1} * f
        n_rg = -np.sum(dE_deps, axis=0)  # sum over pair index beta

        print(f"    RG occupations (from implicit diff):")
        print(f"      n_RG = {n_rg}")
        print(f"      sum(n_RG) = {np.sum(n_rg):.6f} (should be {N})")

        # Cross-check against ED (using separable H for RG comparison)
        # Note: ED uses full V, RG uses separable. For fair comparison,
        # build separable Hamiltonian and diagonalize.
        from itertools import combinations as combs
        states = list(combs(range(N_modes), N))

        def build_H_sep(eps, g, states):
            """Build separable pairing Hamiltonian."""
            dim = len(states)
            H = np.zeros((dim, dim))
            for i, si in enumerate(states):
                H[i, i] = 2.0 * sum(eps[k] for k in si)
                H[i, i] -= g * len(si)
                for j_idx in range(i + 1, dim):
                    sj = states[j_idx]
                    si_set = set(si)
                    sj_set = set(sj)
                    diff_i = si_set - sj_set
                    diff_j = sj_set - si_set
                    if len(diff_i) == 1 and len(diff_j) == 1:
                        H[i, j_idx] = -g
                        H[j_idx, i] = -g
            return H

        H_sep = build_H_sep(eps_bare, g, states)
        evals_sep, evecs_sep = eigh(H_sep)

        # Ground state occupations from ED of separable H
        gs_vec = evecs_sep[:, 0]
        n_sep_ed = np.zeros(N_modes)
        for i_state, state in enumerate(states):
            prob = gs_vec[i_state]**2
            for k in state:
                n_sep_ed[k] += prob

        print(f"    Separable-ED occupations:")
        print(f"      n_sep_ED = {n_sep_ed}")
        print(f"      sum(n_sep_ED) = {np.sum(n_sep_ed):.6f}")

        # Compare RG vs separable-ED
        max_dev_rg_ed = np.max(np.abs(n_rg - n_sep_ed))
        print(f"    max|n_RG - n_sep_ED| = {max_dev_rg_ed:.6e}")

        # Store RG results
        rg_results[N] = {
            'E_pairs': np.sort(E_pairs_rg),
            'E_total': E_total_rg,
            'n_rg': n_rg,
            'n_sep_ed': n_sep_ed,
            'converged': converged,
            'residual': residual,
            'rg_vs_ed_maxdev': max_dev_rg_ed,
        }

    except np.linalg.LinAlgError:
        print(f"    WARNING: Jacobian singular, RG occupation extraction failed.")
        rg_results[N] = {
            'E_pairs': np.sort(E_pairs_rg),
            'E_total': E_total_rg,
            'n_rg': None,
            'converged': converged,
            'residual': residual,
        }

    print()

# =============================================================================
# STEP 9: COMPUTE ED-PROJECTED SPECTRAL MOMENTS WITH FULL V OCCUPATIONS
# =============================================================================
print("=" * 78)
print("STEP 9: ED-Projected Spectral Moments (Full V, from S52)")
print("=" * 78)
print()
print("  Using the ED occupations from the FULL pairing Hamiltonian (S52),")
print("  not just the separable component. These are the exact many-body")
print("  occupations for the physical system.")
print()

# The key comparison: the spectral moments computed with ED-exact occupations
# versus BCS mean-field. The decisive ratio is delta_a2 / a2 at N_pair = 4.

print(f"  {'N_pair':>6s}  {'|da2/a2|':>10s}  {'|da4/a4|':>10s}  "
      f"{'|dS/S|':>10s}  {'Verdict':>8s}")
print(f"  {'------':>6s}  {'--------':>10s}  {'--------':>10s}  "
      f"{'------':>10s}  {'-------':>8s}")

for N in [1, 2, 3, 4]:
    r = results[N]
    abs_da2 = abs(r['delta_a2'])
    abs_da4 = abs(r['delta_a4'])
    abs_dS = abs(r['delta_S'])

    if abs_da2 < 0.10:
        verdict = 'PASS'
    elif abs_da2 > 0.20:
        verdict = 'FAIL'
    else:
        verdict = 'INFO'

    print(f"  {N:>6d}  {abs_da2:>10.6f}  {abs_da4:>10.6f}  "
          f"{abs_dS:>10.6f}  {verdict:>8s}")

print()

# =============================================================================
# STEP 10: DIAGNOSTIC -- FRACTION OF a2 FROM PAIRING-AFFECTED MODES
# =============================================================================
print("=" * 78)
print("STEP 10: Fraction of a2 from Pairing-Affected Modes")
print("=" * 78)

# Compute the contribution to a2 from each sector group
a2_by_group = {'B1': 0.0, 'B2': 0.0, 'B3': 0.0}
a2_total = 0.0
for si in sector_info:
    omega = si['evals']
    group = si.get('mode_group', 'HIGHER')
    contrib = np.sum(1.0 / omega**2)
    if group in a2_by_group:
        a2_by_group[group] += contrib
    a2_total += contrib

print(f"\n  Bare a2 contributions by sector group:")
for gn in ['B1', 'B2', 'B3']:
    frac = a2_by_group[gn] / a2_total
    print(f"    {gn}: a2_frac = {frac:.6f} ({frac*100:.2f}%)")
not_bcs = 1.0 - sum(a2_by_group[g] / a2_total for g in ['B1', 'B2', 'B3'])
print(f"    Non-BCS sectors: {not_bcs:.6f} ({not_bcs*100:.2f}%)")
print()
print("  NOTE: The D_K sectors are assigned to B1/B2/B3 by matching their")
print("  minimum eigenvalue to the 8-mode energies. Higher-lying eigenvalues")
print("  within each sector are also affected by pairing, but with")
print("  decreasing sensitivity (Delta^2/omega^2 correction).")

# =============================================================================
# STEP 11: STRUCTURAL ANALYSIS AND GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Gate Verdict -- PROJECTED-MOMENTS-67")
print("=" * 78)

# The decisive number: |delta_a2 / a2| at N_pair = 4 (half-filling)
decisive_ratio = abs(results[4]['delta_a2'])
print(f"\n  Decisive quantity: |delta_a2 / a2| at N_pair = 4")
print(f"  Value: {decisive_ratio:.6f} ({decisive_ratio*100:.4f}%)")
print()

if decisive_ratio < 0.10:
    gate_verdict = "PASS"
    gate_detail = (f"|delta_a2/a2| = {decisive_ratio:.6f} < 0.10 (10%). "
                   f"The mean-field BCS spectral action is reliable within the "
                   f"pre-registered threshold. RG/ED corrections to spectral "
                   f"moments are perturbative.")
elif decisive_ratio > 0.20:
    gate_verdict = "FAIL"
    gate_detail = (f"|delta_a2/a2| = {decisive_ratio:.6f} > 0.20 (20%). "
                   f"The mean-field BCS spectral action requires significant "
                   f"correction from exact many-body occupations.")
else:
    gate_verdict = "INFO"
    gate_detail = (f"|delta_a2/a2| = {decisive_ratio:.6f} in [0.10, 0.20]. "
                   f"Intermediate regime. Mean-field BCS is qualitatively OK "
                   f"but quantitative corrections are non-negligible.")

print(f"  Gate: PROJECTED-MOMENTS-67")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")
print()

# Additional structural analysis
print("  Structural analysis:")
print(f"    1. The BCS mean-field Delta = {Delta_0:.4f} M_KK is uniform across all modes.")
print(f"    2. The ED exact occupations give mode-dependent effective gaps.")
print(f"    3. The spectral moment change comes from the mismatch between")
print(f"       the uniform BCS gap and the mode-resolved ED gaps.")
print()

# Print comprehensive results table
print("  Comprehensive results:")
print(f"  {'N_pair':>6s}  {'Delta_B1_eff':>12s}  {'Delta_B2_eff':>12s}  "
      f"{'Delta_B3_eff':>12s}  {'|da2/a2|':>10s}  {'|da4/a4|':>10s}")
print(f"  {'------':>6s}  {'----------':>12s}  {'----------':>12s}  "
      f"{'----------':>12s}  {'--------':>10s}  {'--------':>10s}")
for N in [1, 2, 3, 4]:
    r = results[N]
    print(f"  {N:>6d}  {r['Delta_B1_eff']:>12.6f}  {r['Delta_B2_eff']:>12.6f}  "
          f"{r['Delta_B3_eff']:>12.6f}  {abs(r['delta_a2']):>10.6f}  "
          f"{abs(r['delta_a4']):>10.6f}")

print()

# Nuclear physics interpretation
print("  Nuclear physics interpretation (Papers 15, 17):")
print(f"    The d/Delta ratio: d = (eps_B3 - eps_B1) / N_modes = "
      f"{(eps_bare[5] - eps_bare[4]) / N_modes:.6f}")
d_over_Delta = (eps_bare[5] - eps_bare[4]) / N_modes / Delta_0
print(f"    d/Delta = {d_over_Delta:.4f}")
if d_over_Delta < 1:
    print(f"    d/Delta < 1: deep BCS regime (Paper 17). Mean-field reliable.")
elif d_over_Delta > 10:
    print(f"    d/Delta > 10: fluctuation-dominated regime. Mean-field breaks down.")
else:
    print(f"    d/Delta ~ O(1): crossover regime. Corrections are moderate.")

# The occupation number deviation
for N in [1, 2, 3, 4]:
    n_ed = ed_data[N]['n_k']
    n_bcs = bcs_data[N]['v2']
    max_dev = np.max(np.abs(n_ed - n_bcs))
    rms_dev = np.sqrt(np.mean((n_ed - n_bcs)**2))
    print(f"    N={N}: max|n_ED - n_BCS| = {max_dev:.4f}, "
          f"rms = {rms_dev:.4f}")

print()

# =============================================================================
# STEP 12: SAVE RESULTS
# =============================================================================
print("=" * 78)
print("STEP 12: Saving Results")
print("=" * 78)

save_dict = {
    'gate_name': 'PROJECTED-MOMENTS-67',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
    'gate_decisive_ratio': decisive_ratio,
    'Delta_0': Delta_0,
    'tau_fold': tau_fold,
    'eps_bare': eps_bare,
    'labels': np.array(labels),
    'a2_bare': a2_bare,
    'a4_bare': a4_bare,
    'a2_bcs': a2_bcs,
    'a4_bcs': a4_bcs,
    'r2_bcs_over_bare': a2_bcs / a2_bare,
}

for N in [1, 2, 3, 4]:
    r = results[N]
    save_dict[f'N{N}_n_k_ed'] = ed_data[N]['n_k']
    save_dict[f'N{N}_n_k_bcs'] = bcs_data[N]['v2']
    save_dict[f'N{N}_Delta_B1_eff'] = r['Delta_B1_eff']
    save_dict[f'N{N}_Delta_B2_eff'] = r['Delta_B2_eff']
    save_dict[f'N{N}_Delta_B3_eff'] = r['Delta_B3_eff']
    save_dict[f'N{N}_a2_ed'] = r['a2_ed']
    save_dict[f'N{N}_a4_ed'] = r['a4_ed']
    save_dict[f'N{N}_delta_a2'] = r['delta_a2']
    save_dict[f'N{N}_delta_a4'] = r['delta_a4']
    save_dict[f'N{N}_delta_S'] = r['delta_S']

    if N in rg_results and rg_results[N].get('n_rg') is not None:
        save_dict[f'N{N}_E_pairs_rg'] = rg_results[N]['E_pairs']
        save_dict[f'N{N}_n_rg'] = rg_results[N]['n_rg']
        save_dict[f'N{N}_rg_residual'] = rg_results[N]['residual']

np.savez(os.path.join(SCRIPT_DIR, 's67_projected_moments.npz'), **save_dict)
print("  Saved to s67_projected_moments.npz")
print()

# =============================================================================
# STEP 13: PLOT
# =============================================================================
print("=" * 78)
print("STEP 13: Generating Plots")
print("=" * 78)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Occupation number comparison (N_pair = 4)
ax1 = axes[0, 0]
x = np.arange(N_modes)
width = 0.35  # (local)
n_ed_4 = ed_data[4]['n_k']
n_bcs_4 = bcs_data[4]['v2']
ax1.bar(x - width/2, n_ed_4, width, label='ED (exact)', color='steelblue', alpha=0.8)
ax1.bar(x + width/2, n_bcs_4, width, label='BCS (mean-field)', color='coral', alpha=0.8)
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right')
ax1.set_ylabel(r'$n_k = \langle \hat{n}_k \rangle$')
ax1.set_title(f'Occupation Numbers at N_pair = 4 (half-filling)')
ax1.legend()

# Plot 2: delta_a2/a2 vs N_pair
ax2 = axes[0, 1]
Ns = [1, 2, 3, 4]
da2_vals = [abs(results[N]['delta_a2']) * 100 for N in Ns]
da4_vals = [abs(results[N]['delta_a4']) * 100 for N in Ns]
ax2.plot(Ns, da2_vals, 'o-', color='steelblue', label=r'$|\delta a_2 / a_2|$', lw=2)
ax2.plot(Ns, da4_vals, 's--', color='coral', label=r'$|\delta a_4 / a_4|$', lw=2)
ax2.axhline(y=10, color='green', ls=':', label='PASS threshold (10%)')
ax2.axhline(y=20, color='red', ls=':', label='FAIL threshold (20%)')
ax2.set_xlabel(r'$N_{\rm pair}$')
ax2.set_ylabel(r'$|\delta a_n / a_n|$ (%)')
ax2.set_title('Spectral Moment Deviation: ED vs BCS')
ax2.legend()
ax2.set_xticks(Ns)

# Plot 3: Effective gaps vs N_pair
ax3 = axes[1, 0]
D_B1 = [results[N]['Delta_B1_eff'] for N in Ns]
D_B2 = [results[N]['Delta_B2_eff'] for N in Ns]
D_B3 = [results[N]['Delta_B3_eff'] for N in Ns]
ax3.plot(Ns, D_B1, 'o-', color='green', label=r'$\Delta_{\rm B1}^{\rm eff}$', lw=2)
ax3.plot(Ns, D_B2, 's-', color='steelblue', label=r'$\Delta_{\rm B2}^{\rm eff}$', lw=2)
ax3.plot(Ns, D_B3, '^-', color='coral', label=r'$\Delta_{\rm B3}^{\rm eff}$', lw=2)
ax3.axhline(y=Delta_0, color='black', ls='--', label=r'$\Delta_0^{\rm BCS}$')
ax3.set_xlabel(r'$N_{\rm pair}$')
ax3.set_ylabel(r'$\Delta_k^{\rm eff}$ ($M_{\rm KK}$)')
ax3.set_title('Effective Mode-Dependent Gaps from ED')
ax3.legend()
ax3.set_xticks(Ns)

# Plot 4: Occupation difference (n_ED - n_BCS) for all N_pair
ax4 = axes[1, 1]
for N in Ns:
    diff = ed_data[N]['n_k'] - bcs_data[N]['v2']
    ax4.plot(x, diff, 'o-', label=f'N={N}', lw=1.5)
ax4.axhline(y=0, color='black', ls='-', lw=0.5)
ax4.set_xticks(x)
ax4.set_xticklabels(labels, rotation=45, ha='right')
ax4.set_ylabel(r'$n_k^{\rm ED} - v_k^{2,\rm BCS}$')
ax4.set_title('Occupation Number Deviation: ED - BCS')
ax4.legend()

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's67_projected_moments.png'), dpi=150)
print("  Saved plot to s67_projected_moments.png")

print("\n" + "=" * 78)
print(f"PROJECTED-MOMENTS-67: COMPLETE")
print(f"  Gate verdict: {gate_verdict}")
print(f"  |delta_a2/a2| at N_pair=4 = {decisive_ratio:.6f} ({decisive_ratio*100:.4f}%)")
print("=" * 78)
