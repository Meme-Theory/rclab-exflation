#!/usr/bin/env python3
"""
s59_pw_cc_extension.py — PW-CC-59
===================================

Does the CC near-cancellation R_cancel = [0.002, 0.007] at max_pq_sum=0 (8 modes
from the trivial irrep) decrease when we include higher Peter-Weyl sectors?

Physics:
  By the block-diagonal theorem (Session 22b), D_K is block-diagonal in the
  Peter-Weyl basis. Each SU(3) irrep (p,q) contributes an independent block
  to the Dirac operator. The spectral action decomposes:

    S[D_K] = sum_{(p,q)} dim(p,q)^2 * S[D_{(p,q)}]

  where dim(p,q)^2 is the Peter-Weyl multiplicity (left x right regular rep).

  The Volovik CC formula likewise decomposes:

    Lambda_eff = sum_{(p,q)} dim(p,q)^2 * Lambda_eff^{(p,q)}

  where Lambda_eff^{(p,q)} is the non-equilibrium vacuum energy from the
  BCS ground state in sector (p,q) alone.

  At max_pq_sum=0, only the (0,0) sector contributes (dim=1, so weight=1).
  The S58 result: Lambda_eff^{(0,0)} = +0.0014, R_cancel = 0.004.

  With higher sectors, the total Lambda_eff gets PW-weighted contributions from
  each sector. The cancellation ratio R_cancel for the full sum tests whether
  these weighted contributions cancel against each other.

Strategy:
  1. At the fold (tau=0.19), compute Dirac spectrum sector by sector up to max_pq_sum=5
  2. For each sector (p,q): extract the 8 positive eigenvalues (Clifford structure
     ensures 16 eigenvalues per block, 8 positive), assign B1/B2/B3 branches,
     run ED in the 256-state Fock space with V_8x8, compute Volovik Lambda
  3. Weight each sector by dim(p,q)^2, sum, compute R_cancel of the total

Key insight (Landau reasoning): The Dirac operator on each irrep has the SAME
Clifford structure (8 generators acting on a 16-dim spinor space). The ONLY
difference between sectors is the representation matrices rho_a(p,q) that enter
the covariant derivative. So each sector produces 8 positive modes with the same
branch structure (B1, B2x4, B3x3), just at different energies. The BCS Hamiltonian
H = sum_k 2*xi_k*n_k - sum_{kk'} V_{kk'} P+_k P_{k'} has the SAME V_8x8
(which is a property of the Clifford algebra, not the irrep), just different
single-particle energies xi_k.

Gate: PW-CC-59
  PASS: R_cancel ~ (level)^{-alpha}, alpha > 2
  FAIL: R_cancel saturates or grows
  INFO: insufficient levels to determine scaling

Author: Landau-Condensed-Matter-Theorist
Session: 59, Task PW-CC-59
"""

import sys
import os
import time
import numpy as np
from scipy.optimize import minimize_scalar

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, ARCHIVE_DIR)

from canonical_constants import (
    E_cond, M_KK, M_KK_gravity, rho_Lambda_obs,
    tau_fold, rho_B2_per_mode, N_dof_BCS,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t_start = time.time()

OUTPUT_TXT = os.path.join(SCRIPT_DIR, 's59_pw_cc_extension_v2_output.txt')
log_lines = []

def log(msg):
    print(msg)
    log_lines.append(msg)

def flush_log():
    with open(OUTPUT_TXT, 'w') as f:
        f.write('\n'.join(log_lines))

log("=" * 78)
log("PW-CC-59: Peter-Weyl CC Extension — Sector-by-Sector Decomposition")
log("=" * 78)

# ============================================================================
# Section 1: Infrastructure
# ============================================================================

log("\n--- Section 1: Loading Infrastructure ---")

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    collect_spectrum, build_cliff8
)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# ============================================================================
# Section 2: Load S58 Reference
# ============================================================================

log("\n--- Section 2: S58 Reference ---")

d58 = np.load(os.path.join(SCRIPT_DIR, 's58_cc_cancellation_sweep.npz'), allow_pickle=True)
R_cancel_fold_s58 = float(d58['R_cancel_fold'])
V_8x8 = d58['V_8x8']
Lambda_eff_fold_s58 = d58['Lambda_eff_sweep'][int(d58['fold_idx'])]

d36 = np.load(os.path.join(ARCHIVE_DIR, 's36_multisector_ed.npz'), allow_pickle=True)
V_8x8_s36 = d36['V_8x8_full']

d35 = np.load(os.path.join(ARCHIVE_DIR, 's35a_vh_impedance_arbiter.npz'), allow_pickle=True)
rho_smooth = float(d35['rho_at_physical'])

log(f"S58 R_cancel at fold: {R_cancel_fold_s58:.6f}")
log(f"S58 Lambda_eff at fold: {Lambda_eff_fold_s58:.8f}")
log(f"V_8x8 norm: {np.linalg.norm(V_8x8_s36):.6f}")
log(f"rho_smooth (B2 DOS): {rho_smooth:.6f}")

# ============================================================================
# Section 3: BCS Infrastructure (S58 Method)
# ============================================================================

N_MODES = 8  # (local)
N_FOCK = 2**N_MODES  # 256


def build_full_fock_H(xi, V, rho_dos, n_modes=8):
    """Build BCS pair Hamiltonian in full 2^N Fock space."""
    dim = 2**n_modes
    H = np.zeros((dim, dim))
    for s in range(dim):
        for k in range(n_modes):
            if s & (1 << k):
                H[s, s] += 2.0 * xi[k]
        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                v_eff = V[k, kp] * np.sqrt(rho_dos[k] * rho_dos[kp])
                if abs(v_eff) < 1e-30:
                    continue
                if (s & (1 << kp)) and not (s & (1 << k)):
                    sp = (s ^ (1 << kp)) | (1 << k)
                    H[sp, s] -= v_eff
    return H


def extract_occupations(psi_gs, n_modes=8):
    """Extract <n_k> from full Fock space ground state."""
    dim = 2**n_modes
    nk = np.zeros(n_modes)
    for k in range(n_modes):
        for s in range(dim):
            if (s >> k) & 1:
                nk[k] += abs(psi_gs[s])**2
    return nk


def volovik_cc_sector(xi_8, V_8x8_mat, rho_8):
    """Compute Volovik CC for a single 8-mode sector using ED.

    This is the S58 method applied to one Peter-Weyl sector.

    Args:
        xi_8: 8 single-particle energies in S36 convention [B2x4, B1, B3x3]
        V_8x8_mat: 8x8 pairing matrix
        rho_8: 8-element DOS array

    Returns:
        Lambda_eff: total CC for this sector
        R_cancel: cancellation ratio
        Lambda_B2, Lambda_B1, Lambda_B3: branch contributions
        E_BCS: BCS ground state energy
        fk_gge: GGE occupations
        metadata dict
    """
    mu = 0.0  # (local)
    E_pair = 2.0 * xi_8

    # Build and diagonalize
    H = build_full_fock_H(xi_8 - mu, V_8x8_mat, rho_8, 8)
    H = 0.5 * (H + H.T)
    evals, evecs = np.linalg.eigh(H)

    E_BCS = evals[0]
    psi_gs = evecs[:, 0]
    fk_gge = extract_occupations(psi_gs, 8)

    # Equilibrium fit
    def L2_canonical(T):
        if T <= 1e-15:
            f_eq = np.zeros(8)
            f_eq[np.argmin(E_pair)] = 1.0
        else:
            boltz = np.exp(-E_pair / T)
            f_eq = boltz / np.sum(boltz)
        return np.sum((fk_gge - f_eq)**2)

    res = minimize_scalar(L2_canonical, bounds=(0.001, 100.0), method='bounded',
                          options={'xatol': 1e-15})
    T_eq = res.x

    if T_eq <= 1e-15:
        fk_eq = np.zeros(8)
        fk_eq[np.argmin(E_pair)] = 1.0
    else:
        boltz = np.exp(-E_pair / T_eq)
        fk_eq = boltz / np.sum(boltz)

    # Volovik formula
    delta_fk = fk_gge - fk_eq
    eps_s = 1e-15
    fk_eq_safe = np.clip(fk_eq, eps_s, 1.0 - eps_s)
    mu_eff = T_eq * np.log((1.0 - fk_eq_safe) / fk_eq_safe)
    Lambda_pm = delta_fk * (E_pair - mu_eff)
    Lambda_eff = np.sum(Lambda_pm)

    # Branch decomposition
    Lambda_B2 = np.sum(Lambda_pm[0:4])
    Lambda_B1 = Lambda_pm[4]
    Lambda_B3 = np.sum(Lambda_pm[5:8])

    denom = max(abs(Lambda_B2), abs(Lambda_B1 + Lambda_B3))
    R_cancel = abs(Lambda_eff) / denom if denom > 1e-20 else 1.0

    return Lambda_eff, R_cancel, Lambda_B2, Lambda_B1, Lambda_B3, E_BCS, fk_gge, {
        'T_eq': T_eq, 'fk_gge': fk_gge, 'fk_eq': fk_eq, 'Lambda_pm': Lambda_pm,
    }


# ============================================================================
# Section 4: Compute Sector-by-Sector CC at Each Level
# ============================================================================

log("\n--- Section 4: Sector-by-Sector CC ---")

tau = tau_fold
MAX_PQ_LEVELS = [0, 1, 2, 3, 4, 5]

# First, compute full spectrum at highest level to get all eigenvalues
log(f"\nComputing full spectrum up to max_pq_sum=5 at tau={tau}...")
t0 = time.time()

# We collect sector-by-sector: for each (p,q), get the 16 eigenvalues from D_{(p,q)}
# The Dirac operator in sector (p,q) is: D_{(p,q)} = i * (Omega + sum_a rho_a E^a_mu partial_mu)
# This is a 16*dim(p,q) x 16*dim(p,q) matrix. Its eigenvalues come in 8 positive/8 negative
# pairs (Dirac structure), with possible degeneracy splits from the irrep structure.

# But within each sector, the D_pi matrix has dim(p,q)*16 eigenvalues, NOT just 16.
# The 8-mode BCS structure is for the (0,0) sector ONLY (dim=1, so D has 16 eigenvalues).
# For (1,0) with dim=3, D is 48x48 with 24 positive eigenvalues.

# This means the "8 modes = B1+B2x4+B3x3" structure is SPECIFIC to the (0,0) sector.
# Higher sectors have MORE modes (not 8, but 8*dim(p,q)) and different branch structures.

# Correct approach: for each sector, we have 8*dim(p,q) positive eigenvalues.
# However, the BCS Fock space at N modes requires 2^N states -- infeasible for N>~20.

# THE RIGHT QUESTION: Does the (0,0) sector dominate, or do higher sectors contribute
# significantly to the weighted sum Lambda_eff = sum dim(p,q)^2 * Lambda_{(p,q)}?

# For BCS pairing, the interaction scale V ~ 0.04 (from S36) while the energy scale
# at higher sectors grows as sqrt(C2). The ratio V/E determines the strength of
# pairing -- it weakens at higher sectors (BCS gap exponentially suppressed at weak coupling).

# Strategy: Compute Lambda_eff for (0,0) exactly (ED, 8 modes, matching S58).
# For higher sectors, use BCS mean-field on the full mode set but with SECTOR-SPECIFIC
# eigenvalues. Use the Landau argument: pairing is relevant only near the Fermi surface
# where delta_n is largest. At higher sectors, the energies are larger, pairing is weaker,
# and the GGE-equilibrium mismatch is smaller.

# Let me compute ALL sector eigenvalues first.

all_sector_results = {}  # (p,q) -> dict with eigenvalues, multiplicity, etc.

for max_pq in range(6):
    log(f"\n  === Computing sectors at max_pq_sum = {max_pq} ===")

    # Get fresh spectrum at this level
    all_evals, eval_data = collect_spectrum(
        tau, gens, f_abc, gammas, max_pq_sum=max_pq, verbose=False
    )

    for (p, q, evals_sector) in eval_data:
        key = (p, q)
        if key in all_sector_results:
            continue  # already computed

        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
        pw_weight = dim_pq**2

        # Extract positive eigenvalues
        evals_imag = evals_sector.imag
        pos_evals = np.sort(evals_imag[evals_imag > 1e-10])
        n_pos = len(pos_evals)

        all_sector_results[key] = {
            'p': p, 'q': q, 'dim': dim_pq, 'C2': C2,
            'pw_weight': pw_weight,
            'pos_evals': pos_evals,
            'n_pos': n_pos,
            'all_evals': evals_sector,
        }

        log(f"    ({p},{q}): dim={dim_pq}, C2={C2:.3f}, PW_weight={pw_weight}, "
            f"n_pos={n_pos}, E_range=[{pos_evals[0]:.4f}, {pos_evals[-1]:.4f}]")

dt = time.time() - t0
log(f"\n  All sectors computed in {dt:.1f}s")
log(f"  Total sectors: {len(all_sector_results)}")

flush_log()

# ============================================================================
# Section 5: ED for (0,0) — S58 Cross-Check
# ============================================================================

log("\n--- Section 5: (0,0) Sector — ED Cross-Check ---")

sec00 = all_sector_results[(0,0)]
pos_evals_00 = sec00['pos_evals']  # 8 positive eigenvalues, sorted ascending

# Map to S36 convention: sorted = [B1, B2x4, B3x3]
# S36 convention: [B2[0..3], B1, B3[0..2]]
xi_00 = np.array([
    pos_evals_00[1], pos_evals_00[2], pos_evals_00[3], pos_evals_00[4],  # B2
    pos_evals_00[0],                                                       # B1
    pos_evals_00[5], pos_evals_00[6], pos_evals_00[7],                    # B3
])
rho_00 = np.array([rho_smooth]*4 + [1.0, 1.0, 1.0, 1.0])

Lambda_00, R_00, LB2_00, LB1_00, LB3_00, E_BCS_00, fk_00, meta_00 = \
    volovik_cc_sector(xi_00, V_8x8_s36, rho_00)

log(f"  (0,0) ED result:")
log(f"    Lambda_eff = {Lambda_00:+.8f}")
log(f"    R_cancel = {R_00:.8f}")
log(f"    B2 = {LB2_00:+.6f}, B1 = {LB1_00:+.6f}, B3 = {LB3_00:+.6f}")
log(f"    E_BCS = {E_BCS_00:.6f}")
log(f"    S58 cross-check: Lambda_eff = {Lambda_eff_fold_s58:.8f}, R_cancel = {R_cancel_fold_s58:.8f}")

flush_log()

# ============================================================================
# Section 6: Higher Sectors — BCS Mean-Field on 8 Effective Modes
# ============================================================================

log("\n--- Section 6: Higher Sectors — 8 Effective Modes ---")

# KEY PHYSICAL ARGUMENT (Landau quasiparticle construction):
#
# For sector (p,q) with dim_pq > 1, the Dirac operator D_{(p,q)} is a
# dim_pq*16 x dim_pq*16 matrix. It has 8*dim_pq positive eigenvalues.
#
# However, the BCS Hamiltonian couples PAIRS of modes. The Cooper pair
# operator P^+_k creates a pair (k, bar{k}) where bar{k} is the
# time-reversed partner. In the (0,0) sector, this gives exactly 8 modes.
#
# In higher sectors, the D eigenvalues have internal multiplicity from the
# irrep decomposition. The DISTINCT eigenvalues (ignoring irrep multiplicity)
# still correspond to the Clifford algebra eigenvalue structure: 8 positive
# values, each with multiplicity dim_pq from the Peter-Weyl decomposition.
#
# For BCS, the Cooper pair involves two modes from the SAME representation
# (pair has total representation weight 0). By Schur's lemma, the pair
# operator within a dim_pq-dimensional irrep creates dim_pq copies of the
# same Cooper pair. The BCS Hamiltonian for each (p,q) sector is therefore
# structurally identical to the (0,0) case: 8 effective pair modes, each
# with DOS enhanced by dim_pq (from the internal multiplicity).
#
# This is the correct Peter-Weyl extension: the BCS Hamiltonian in sector
# (p,q) has the SAME V_8x8 pairing matrix (determined by the Clifford algebra),
# but with:
#   - Different single-particle energies xi_k (from the sector eigenvalues)
#   - Enhanced DOS: rho_k -> rho_k * dim_pq (from internal multiplicity)
#
# The total Lambda_eff = sum_{(p,q)} dim(p,q)^2 * Lambda_eff^{(p,q)}
# where the dim^2 comes from the Peter-Weyl theorem (each distinct eigenvalue
# in sector (p,q) appears dim(p,q) times in L^2(SU(3))).

# For each sector, extract the 8 DISTINCT positive Dirac eigenvalues.
# These are the 8 values from the Clifford algebra structure.

sector_cc_results = {}

for key in sorted(all_sector_results.keys()):
    sec = all_sector_results[key]
    p, q = sec['p'], sec['q']
    dim_pq = sec['dim']
    pw_weight = sec['pw_weight']
    pos_evals = sec['pos_evals']
    n_pos = sec['n_pos']

    # Extract 8 REPRESENTATIVE eigenvalues from the full set.
    # The Clifford algebra guarantees 16 eigenvalues per "unit cell" of the irrep.
    # For (p,q) with dim=d, we have 8*d positive eigenvalues.
    # Group them into 8 clusters of d eigenvalues each.

    if n_pos < 8:
        log(f"  ({p},{q}): SKIP — only {n_pos} positive eigenvalues (need 8)")
        continue

    if n_pos == 8:
        # (0,0) sector — already computed
        representative_evals = pos_evals
        effective_rho = rho_00
    else:
        # Higher sector: 8*dim_pq eigenvalues. Group into 8 clusters.
        # The eigenvalues come in dim_pq copies of each Clifford eigenvalue,
        # possibly split by the representation (breaking the degeneracy).

        # Approach: cluster the n_pos eigenvalues into 8 groups of ~n_pos/8,
        # and take the mean of each cluster.
        n_per_cluster = n_pos // 8
        representative_evals = np.zeros(8)
        for i in range(8):
            start = i * n_per_cluster
            end = start + n_per_cluster if i < 7 else n_pos
            representative_evals[i] = np.mean(pos_evals[start:end])

        # Enhanced DOS: each cluster has dim_pq modes contributing
        # B2 modes (lowest 4 clusters after B1): use rho_smooth * dim_pq
        # B1 mode (lowest cluster): 1.0 * dim_pq
        # B3 modes (top 3 clusters): 1.0 * dim_pq
        effective_rho = np.array(
            [rho_smooth * dim_pq]*4 + [1.0 * dim_pq]*4
        )

    # Sort and assign to S36 branch convention
    # Sorted ascending: [B1, B2x4, B3x3]
    sort_idx = np.argsort(representative_evals)
    sorted_evals = representative_evals[sort_idx]

    # Remap to [B2x4, B1, B3x3]
    xi_sector = np.array([
        sorted_evals[1], sorted_evals[2], sorted_evals[3], sorted_evals[4],  # B2
        sorted_evals[0],                                                       # B1
        sorted_evals[5], sorted_evals[6], sorted_evals[7],                    # B3
    ])

    if key == (0, 0):
        # Use exact result already computed
        xi_sector = xi_00
        effective_rho = rho_00

    # Run ED for this sector
    try:
        Lambda_sec, R_sec, LB2_sec, LB1_sec, LB3_sec, E_BCS_sec, fk_sec, meta_sec = \
            volovik_cc_sector(xi_sector, V_8x8_s36, effective_rho)

        sector_cc_results[key] = {
            'Lambda_eff': Lambda_sec,
            'R_cancel': R_sec,
            'Lambda_B2': LB2_sec,
            'Lambda_B1': LB1_sec,
            'Lambda_B3': LB3_sec,
            'E_BCS': E_BCS_sec,
            'pw_weight': pw_weight,
            'dim': dim_pq,
            'C2': sec['C2'],
            'xi': xi_sector.copy(),
            'rho_eff': effective_rho.copy(),
            'fk_gge': fk_sec.copy(),
        }

        log(f"  ({p},{q}): dim={dim_pq}, PW={pw_weight}, Lambda={Lambda_sec:+.8f}, "
            f"R={R_sec:.6f}, B2={LB2_sec:+.4f}, B1+B3={LB1_sec+LB3_sec:+.4f}")

    except Exception as e:
        log(f"  ({p},{q}): ERROR — {e}")

flush_log()

# ============================================================================
# Section 7: Cumulative CC at Each Level
# ============================================================================

log("\n--- Section 7: Cumulative CC at Each Peter-Weyl Level ---")

cumulative_results = {}

for max_pq in MAX_PQ_LEVELS:
    # Sum over all sectors with p+q <= max_pq
    Lambda_total = 0.0  # (local)
    Lambda_pos_total = 0.0  # (local)
    Lambda_neg_total = 0.0  # (local)
    n_sectors = 0  # (local)

    sector_contributions = {}

    for (p, q), res in sector_cc_results.items():
        if p + q > max_pq:
            continue

        pw_w = res['pw_weight']
        Lambda_weighted = pw_w * res['Lambda_eff']
        Lambda_total += Lambda_weighted

        if Lambda_weighted > 0:
            Lambda_pos_total += Lambda_weighted
        else:
            Lambda_neg_total += Lambda_weighted

        sector_contributions[(p,q)] = Lambda_weighted
        n_sectors += 1

    # R_cancel for the cumulative sum
    denom = max(abs(Lambda_pos_total), abs(Lambda_neg_total))
    R_cancel_cum = abs(Lambda_total) / denom if denom > 1e-20 else 1.0

    # Total PW multiplicity (total number of modes counting multiplicity)
    total_mult = sum(
        all_sector_results[(p,q)]['pw_weight']
        for (p,q) in sector_cc_results
        if p + q <= max_pq
    )

    cumulative_results[max_pq] = {
        'Lambda_total': Lambda_total,
        'R_cancel': R_cancel_cum,
        'Lambda_pos': Lambda_pos_total,
        'Lambda_neg': Lambda_neg_total,
        'n_sectors': n_sectors,
        'total_mult': total_mult,
        'sector_contributions': sector_contributions,
    }

    log(f"\n  max_pq_sum = {max_pq}: {n_sectors} sectors, total_mult = {total_mult}")
    log(f"    Lambda_total = {Lambda_total:+.8f}")
    log(f"    Lambda_pos = {Lambda_pos_total:+.8f}")
    log(f"    Lambda_neg = {Lambda_neg_total:+.8f}")
    log(f"    R_cancel = {R_cancel_cum:.8f}")

    # Show top 5 contributing sectors
    sorted_contribs = sorted(sector_contributions.items(), key=lambda x: abs(x[1]), reverse=True)
    for (p,q), val in sorted_contribs[:5]:
        log(f"      ({p},{q}): dim^2={all_sector_results[(p,q)]['pw_weight']}, "
            f"Lambda_weighted = {val:+.8f}")

flush_log()

# ============================================================================
# Section 8: Alternative — Raw Sector Sum (without PW weight)
# ============================================================================

log("\n--- Section 8: Alternative — Unweighted Sector Sum ---")

# Also report the unweighted sum to disentangle the role of PW multiplicity
for max_pq in MAX_PQ_LEVELS:
    Lambda_unw = 0.0  # (local)
    Lambda_unw_pos = 0.0  # (local)
    Lambda_unw_neg = 0.0  # (local)
    n_sec = 0  # (local)

    for (p, q), res in sector_cc_results.items():
        if p + q > max_pq:
            continue
        Lambda_unw += res['Lambda_eff']
        if res['Lambda_eff'] > 0:
            Lambda_unw_pos += res['Lambda_eff']
        else:
            Lambda_unw_neg += res['Lambda_eff']
        n_sec += 1

    denom = max(abs(Lambda_unw_pos), abs(Lambda_unw_neg))
    R_unw = abs(Lambda_unw) / denom if denom > 1e-20 else 1.0

    log(f"  max_pq={max_pq}: Lambda_unw = {Lambda_unw:+.8f}, R_unw = {R_unw:.8f} ({n_sec} sectors)")

flush_log()

# ============================================================================
# Section 9: Scaling Analysis
# ============================================================================

log("\n--- Section 9: Scaling Analysis ---")

levels = sorted(cumulative_results.keys())
levels_arr = np.array(levels)
R_cancel_arr = np.array([cumulative_results[l]['R_cancel'] for l in levels])
Lambda_arr = np.array([cumulative_results[l]['Lambda_total'] for l in levels])
n_mult_arr = np.array([cumulative_results[l]['total_mult'] for l in levels])
n_sect_arr = np.array([cumulative_results[l]['n_sectors'] for l in levels])

log(f"\n{'Level':>6} {'N_sect':>7} {'PW_mult':>10} {'Lambda_total':>16} {'R_cancel':>12}")
log("-" * 65)
for l in levels:
    cr = cumulative_results[l]
    log(f"{l:>6d} {cr['n_sectors']:>7d} {cr['total_mult']:>10d} "
        f"{cr['Lambda_total']:>+16.8f} {cr['R_cancel']:>12.8f}")

# Fit scaling if enough points
alpha_power = None
A_power = None
beta_exp = None
B_exp = None

if len(levels) >= 3:
    mask = (R_cancel_arr > 1e-15) & (R_cancel_arr < 1.0 - 1e-10)
    if np.sum(mask) >= 2:
        x_log = np.log(levels_arr[mask] + 1.0)
        y_log = np.log(R_cancel_arr[mask])
        coeffs = np.polyfit(x_log, y_log, 1)
        alpha_power = -coeffs[0]
        A_power = np.exp(coeffs[1])
        log(f"\nPower law fit: R_cancel = {A_power:.6f} * (level+1)^(-{alpha_power:.4f})")

        x_lin = levels_arr[mask].astype(float)
        coeffs_exp = np.polyfit(x_lin, y_log, 1)
        beta_exp = -coeffs_exp[0]
        B_exp = np.exp(coeffs_exp[1])
        log(f"Exponential fit: R_cancel = {B_exp:.6f} * exp(-{beta_exp:.4f} * level)")
    else:
        log(f"\nInsufficient non-trivial R_cancel values for fit (mask sum = {np.sum(mask)})")
else:
    log(f"\nInsufficient levels for fit ({len(levels)})")

# Also fit vs PW multiplicity
mask_mult = (R_cancel_arr > 1e-15) & (R_cancel_arr < 1.0 - 1e-10)
if np.sum(mask_mult) >= 2:
    x_mult = np.log(n_mult_arr[mask_mult].astype(float))
    y_mult = np.log(R_cancel_arr[mask_mult])
    coeffs_mult = np.polyfit(x_mult, y_mult, 1)
    alpha_mult = -coeffs_mult[0]
    A_mult = np.exp(coeffs_mult[1])
    log(f"\nMultiplicity scaling: R_cancel = {A_mult:.6f} * N_mult^(-{alpha_mult:.4f})")
else:
    alpha_mult = None

# Projection
log(f"\nProjection:")
log(f"  M_KK = {M_KK:.4e} GeV")
log(f"  rho_Lambda_obs = {rho_Lambda_obs:.4e} GeV^4")
R_target = rho_Lambda_obs / M_KK**4
log(f"  R_target = rho_obs / M_KK^4 = {R_target:.4e}")

if alpha_power is not None and alpha_power > 0 and A_power > 0:
    ratio = R_target / A_power
    if ratio > 0:
        level_needed = np.exp(np.log(ratio) / (-alpha_power)) - 1
        log(f"  Power law -> level_needed = {level_needed:.1f}")

if beta_exp is not None and beta_exp > 0 and B_exp > 0:
    ratio_exp = R_target / B_exp
    if ratio_exp > 0:
        level_needed_exp = -np.log(ratio_exp) / beta_exp
        log(f"  Exponential -> level_needed = {level_needed_exp:.1f}")

if alpha_mult is not None and alpha_mult > 0:
    ratio_m = R_target / A_mult
    if ratio_m > 0:
        N_needed = np.exp(np.log(ratio_m) / (-alpha_mult))
        log(f"  PW multiplicity -> N_mult_needed = {N_needed:.1e}")

flush_log()

# ============================================================================
# Section 10: Gate Verdict
# ============================================================================

log("\n--- Section 10: Gate Verdict ---")

# Check monotonicity
if len(levels) >= 2:
    monotone = all(
        R_cancel_arr[i+1] <= R_cancel_arr[i]
        for i in range(len(R_cancel_arr)-1)
    )
else:
    monotone = False

# Check if R_cancel shows meaningful variation
R_range = np.max(R_cancel_arr) / (np.min(R_cancel_arr[R_cancel_arr > 1e-15]) + 1e-30)

if alpha_power is not None and alpha_power > 2.0 and monotone:
    verdict = 'PASS'
    reason = f'R_cancel ~ level^(-{alpha_power:.2f}), alpha={alpha_power:.2f} > 2, monotone'
elif alpha_power is not None and alpha_power > 0 and monotone:
    verdict = 'INFO'
    reason = f'Decreasing but alpha={alpha_power:.2f} < 2. Need more levels or higher alpha'
elif not monotone and len(levels) >= 3:
    # Check if non-monotone but generally decreasing
    if R_cancel_arr[-1] < R_cancel_arr[0]:
        verdict = 'INFO'
        reason = f'Generally decreasing (end < start) but not monotone'
    else:
        verdict = 'FAIL'
        reason = f'R_cancel saturates or grows: {R_cancel_arr[0]:.6f} -> {R_cancel_arr[-1]:.6f}'
else:
    verdict = 'INFO'
    reason = f'{len(levels)} levels computed. R range: [{np.min(R_cancel_arr):.6f}, {np.max(R_cancel_arr):.6f}]'

log(f"\nGate: PW-CC-59")
log(f"  Verdict: {verdict}")
log(f"  Reason: {reason}")
log(f"  Criterion: PASS if R_cancel ~ level^(-alpha), alpha > 2")
log(f"  R_cancel values: {R_cancel_arr}")

flush_log()

# ============================================================================
# Section 11: Save
# ============================================================================

log("\n--- Section 11: Save ---")

save_dict = {
    'tau': tau,
    'levels': levels_arr,
    'R_cancel': R_cancel_arr,
    'Lambda_total': Lambda_arr,
    'n_sectors': n_sect_arr,
    'n_pw_mult': n_mult_arr,
    'R_cancel_s58_fold': R_cancel_fold_s58,
    'Lambda_s58_fold': Lambda_eff_fold_s58,
    'M_KK': M_KK,
    'rho_Lambda_obs': rho_Lambda_obs,
    'R_target': R_target,
    'gate_name': np.array(['PW-CC-59']),
    'gate_verdict': np.array([verdict]),
    'gate_reason': np.array([reason]),
}

if alpha_power is not None:
    save_dict['alpha_power'] = alpha_power
    save_dict['A_power'] = A_power
if beta_exp is not None:
    save_dict['beta_exp'] = beta_exp
    save_dict['B_exp'] = B_exp
if alpha_mult is not None:
    save_dict['alpha_mult'] = alpha_mult

# Per-sector data
for (p,q), res in sector_cc_results.items():
    prefix = f'sector_{p}_{q}_'
    save_dict[prefix + 'Lambda_eff'] = res['Lambda_eff']
    save_dict[prefix + 'R_cancel'] = res['R_cancel']
    save_dict[prefix + 'Lambda_B2'] = res['Lambda_B2']
    save_dict[prefix + 'Lambda_B1'] = res['Lambda_B1']
    save_dict[prefix + 'Lambda_B3'] = res['Lambda_B3']
    save_dict[prefix + 'E_BCS'] = res['E_BCS']
    save_dict[prefix + 'pw_weight'] = res['pw_weight']
    save_dict[prefix + 'dim'] = res['dim']
    save_dict[prefix + 'C2'] = res['C2']

npz_path = os.path.join(SCRIPT_DIR, 's59_pw_cc_extension_v2.npz')
np.savez(npz_path, **save_dict)
log(f"Saved: {npz_path}")

flush_log()

# ============================================================================
# Section 12: Plot
# ============================================================================

log("\n--- Section 12: Plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: R_cancel vs level (PW-weighted)
ax = axes[0, 0]
valid = R_cancel_arr > 1e-15
ax.semilogy(levels_arr[valid], R_cancel_arr[valid], 'ko-', markersize=8, linewidth=2,
            label='R_cancel (PW-weighted)')
if alpha_power is not None:
    x_fit = np.linspace(0, max(levels_arr) + 1, 100)
    y_fit = A_power * (x_fit + 1)**(-alpha_power)
    ax.semilogy(x_fit[1:], y_fit[1:], 'r--', linewidth=1,
                label=f'Power: $\\alpha$={alpha_power:.2f}')
if beta_exp is not None:
    y_fit_exp = B_exp * np.exp(-beta_exp * x_fit)
    ax.semilogy(x_fit, y_fit_exp, 'b:', linewidth=1,
                label=f'Exp: $\\beta$={beta_exp:.2f}')
ax.axhline(R_target, color='green', linestyle='-.', alpha=0.7, label=f'$R_{{target}}$')
ax.set_xlabel('max_pq_sum (Peter-Weyl level)')
ax.set_ylabel('$R_{cancel}$')
ax.set_title('CC Cancellation vs PW Truncation')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Lambda_total vs level
ax = axes[0, 1]
ax.plot(levels_arr, Lambda_arr, 'ko-', markersize=8, linewidth=2)
ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('max_pq_sum')
ax.set_ylabel('$\\Lambda_{eff}$ (cumulative, $M_{KK}$ units)')
ax.set_title('Cumulative CC vs PW Level')
ax.grid(True, alpha=0.3)

# Panel 3: Sector-by-sector Lambda (PW-weighted)
ax = axes[1, 0]
sectors_sorted = sorted(sector_cc_results.keys())
C2_vals = [all_sector_results[k]['C2'] for k in sectors_sorted]
Lambda_weighted = [sector_cc_results[k]['pw_weight'] * sector_cc_results[k]['Lambda_eff']
                   for k in sectors_sorted]
colors = ['red' if l > 0 else 'blue' for l in Lambda_weighted]
labels = [f'({p},{q})' for (p,q) in sectors_sorted]
ax.bar(range(len(sectors_sorted)), Lambda_weighted, color=colors, alpha=0.7)
ax.set_xticks(range(len(sectors_sorted)))
ax.set_xticklabels(labels, rotation=45, fontsize=7)
ax.axhline(0, color='gray', linestyle='--')
ax.set_ylabel('$dim^2 \\cdot \\Lambda_{eff}^{(p,q)}$')
ax.set_title('PW-Weighted Sector Contributions')
ax.grid(True, alpha=0.3)

# Panel 4: PW multiplicity growth and R_cancel
ax = axes[1, 1]
ax2 = ax.twinx()
ax.semilogy(levels_arr, n_mult_arr, 'bs-', markersize=6, label='PW multiplicity')
ax2.semilogy(levels_arr[valid], R_cancel_arr[valid], 'ro-', markersize=6, label='$R_{cancel}$')
ax.set_xlabel('max_pq_sum')
ax.set_ylabel('Total PW multiplicity', color='blue')
ax2.set_ylabel('$R_{cancel}$', color='red')
ax.set_title('Mode Growth vs Cancellation')
ax.legend(loc='upper left', fontsize=8)
ax2.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle('PW-CC-59: Peter-Weyl CC Extension', fontsize=14, fontweight='bold')
plt.tight_layout()

png_path = os.path.join(SCRIPT_DIR, 's59_pw_cc_extension_v2.png')
plt.savefig(png_path, dpi=150)
plt.close()
log(f"Saved: {png_path}")

elapsed = time.time() - t_start
log(f"\nTotal time: {elapsed:.1f}s")
log("\n" + "=" * 78)
log("PW-CC-59 COMPLETE")
log("=" * 78)

flush_log()
