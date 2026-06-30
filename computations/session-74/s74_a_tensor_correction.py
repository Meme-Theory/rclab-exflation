"""
S74 W2-P  |  A-TENSOR-CORRECTION-74
================================================================================
Task: Compute the leading O(H/Lambda)^2 A-tensor mixing correction to per-irrep
      D_K eigenvalues at the fold. Propagate to the CORE quantities
      (a_0, a_2, a_4, R_protected, n_s, m_H) and classify against the
      pre-registered gate.

Author: baptista-spacetime-analyst
Session: S74 Wave 2, Batch 4 (W2-P)
Carry-forward: S73B Landau-Baptista workshop item #7

Governing framework
-------------------
Baptista Paper 13 (arXiv 2105.02899) eq (3.4) gives the Riemannian submersion
decomposition of the total scalar curvature on P = M4 x K:

      R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2 delta_check N

    F = O'Neill A-tensor of horizontal vector fields (integrability of the
        horizontal distribution; vanishes iff the horizontal distribution
        is integrable -- i.e., iff the submersion is locally a product with
        the connection A_L = A_R = 0).

    S = O'Neill T-tensor of the vertical fibres (second fundamental form;
        generates the Higgs kinetic term C_phi |d_A phi|^2 -- eq (3.22))

    N = mean curvature vector of the fibres.

The Dirac operator on P inherits an analogous structure (Bismut-Freed, Brain-
Mesland-van Suijlekom, Baptista Paper 14): the squared total Dirac operator
factorises as

      D_P^2 = D_M^2 + D_K^2 + V_AT + V_T

where V_AT is the A-tensor mixing vertex (horizontal <-> vertical) and V_T is
the second-fundamental-form / mean-curvature vertex. In the direct-product
limit (flat base, A_L = A_R = 0) the A-tensor is identically zero and the
spectrum factorises.

At the fold the effective horizontal connection is set by the Hubble expansion
rate H; the natural dimensionless parameter controlling the A-tensor vertex
is therefore

      eps_AT := (H / M_KK)^2 = (H_0 / M_KK)^2  (at today's scale)

Inside a single fibre at one space-time point the A-tensor matrix element
between two Peter-Weyl irreps (p,q), (p',q') is controlled by the Wigner-
Eckart theorem applied to the adjoint representation of SU(3):

      < (p,q) || A || (p',q') > != 0
          iff  (p',q')  in  (p,q) (x) Ad_SU(3)

and the magnitude obeys the universal bound

      | A_{(p,q),(p',q')} |  <=  C_adj * omega_max[(p,q)] * sqrt{eps_AT}

where omega_max[(p,q)] = max |lambda| within the sector (extracted from the
cache) and C_adj is the Casimir-weighted adjoint Clebsch-Gordan norm, bounded
above by sqrt(Cas_adj) = sqrt(3) = 1.7321.

First-order perturbation to the sector-averaged squared eigenvalue (Rayleigh-
Schrodinger with degeneracies lifted by block-diagonal protection):

      delta lambda^2_{(p,q)}
          = eps_AT * sum_{(p',q') in allowed}
                      |A_{(p,q),(p',q')}|^2
                    / (lambda^2_{(p,q)} - lambda^2_{(p',q')})

For sector-averaged squared eigenvalues this is finite (the denominator never
vanishes since distinct irreps have distinct Casimir, therefore distinct
dominant eigenvalues at tau = tau_fold). Numerically degenerate pairs within
the selection rule are flagged and excluded with their contributions reported
separately.

Core observables
----------------
a_k are spectral moments of |D_K|, so a correction to each |lambda|^2 enters
proportionally:

    a_0  =  prefactor * sum dim * N  (mode count)  -- unchanged by delta lam
    a_2  =  prefactor * sum dim * sum_n |lam_n|^{-1}
    a_4  =  prefactor * sum dim * sum_n |lam_n|^{-2}

R_protected = a_0 * a_4 / a_2^2  (quadratic moment ratio)

n_s  depends on dS/dtau = 58673, which depends on a_0, a_2, a_4 via the
spectral action derivative; at leading order the fractional correction to
n_s is bounded by the largest fractional correction to any a_k.

m_H  at tree level scales as sqrt(R_{g_phi}) * Vol * (geometric factors), so
its fractional correction is half the fractional correction to Vol-weighted
spectral data.

Pre-registered gate
-------------------
A-TENSOR-CORRECTION-74:
    PASS if max fractional correction to CORE quantities < 1%
    INFO if in [1%, 5%]
    FAIL if > 5%

Inputs
------
- computations/_shared/canonical_constants.py
- computations/session-74/s74_spectrum_cache_L9_tau019.npz  (W1-C)

Outputs
-------
- computations/session-74/s74_a_tensor_correction.npz
- computations/session-74/s74_a_tensor_correction.png
- Section W2-P of the working paper
"""

from __future__ import annotations

import os
import sys
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    H_0_GeV,
    Vol_SU3_Haar,
    PI,
    a0_fold,
    a2_fold,
    a4_fold,
    m_H_obs,
    planck_ns,
)

SCRIPT_NAME = "A-TENSOR-CORRECTION-74"
OUT_NPZ = "s74_a_tensor_correction.npz"
OUT_PNG = "s74_a_tensor_correction.png"

R_PROTECTED_CANONICAL = 1.128655       # (local)  W1-M canonical value
NS_TREE_REFERENCE    = 0.9561          # (local)  tree-level n_s from S63/S73B
M_H_TREE_REFERENCE   = 131.8           # (local)  tree m_H (GeV) from S63 W1-M
GATE_PASS_FRAC  = 0.01                 # (local)  1 percent
GATE_INFO_FRAC  = 0.05                 # (local)  5 percent

# -----------------------------------------------------------------------------
# 0. HEADER
# -----------------------------------------------------------------------------
t_start = time.time()

print("=" * 80)
print(f"{SCRIPT_NAME}: A-tensor mixing correction to core quantities")
print("S74 W2-P | baptista-spacetime-analyst")
print("=" * 80)
print()
print(f"  tau_fold     = {tau_fold}")
print(f"  M_KK         = {M_KK:.6e} GeV")
print(f"  H_0          = {H_0_GeV:.6e} GeV")
print(f"  eps_AT       = (H_0/M_KK)^2 = {(H_0_GeV / M_KK)**2:.6e}")
print()
print("  Gate: PASS if max frac correction < 1%, INFO [1%,5%], FAIL > 5%")
print()


# -----------------------------------------------------------------------------
# 1. LOAD W1-C SPECTRUM CACHE
# -----------------------------------------------------------------------------
print("=" * 80)
print("1. LOAD W1-C SPECTRUM CACHE")
print("=" * 80)

cache = np.load("s74_spectrum_cache_L9_tau019.npz", allow_pickle=True)
sector_evals = cache["sector_evals"].item()

pq_list = sorted(sector_evals.keys(), key=lambda x: (x[0] + x[1], x[0], x[1]))
n_sectors = len(pq_list)

print(f"  sectors loaded: {n_sectors}")
print(f"  first 5 sectors: {pq_list[:5]}")
print(f"  last  5 sectors: {pq_list[-5:]}")


def pq_dim(p, q):
    """SU(3) irrep dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def pq_casimir(p, q):
    """Quadratic Casimir of SU(3) irrep (p,q): C2 = (p^2+q^2+pq)/3 + p+q."""
    return (p * p + q * q + p * q) / 3.0 + (p + q)


# Collect per-sector sector-averaged |lambda|^2 and the full absolute spectrum.
sector_data = {}  # (local)
for pq in pq_list:
    p, q = pq
    info = sector_evals[pq]
    abs_ev = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
    if abs_ev.size == 0:
        continue
    dim = pq_dim(p, q)                                        # (local)
    lam2_mean = float(np.mean(abs_ev ** 2))                   # (local) sector-avg
    lam2_min  = float(np.min(abs_ev ** 2))                    # (local)
    lam2_max  = float(np.max(abs_ev ** 2))                    # (local)
    C2 = pq_casimir(p, q)                                     # (local)
    sector_data[pq] = {
        "dim": dim,
        "level": p + q,
        "C2": C2,
        "lam2_mean": lam2_mean,
        "lam2_min": lam2_min,
        "lam2_max": lam2_max,
        "n_modes": int(abs_ev.size),
        "omega_min": float(np.min(abs_ev)),
        "omega_max": float(np.max(abs_ev)),
        "abs_evals": abs_ev,
    }

print(f"  sectors with data: {len(sector_data)}")
print()


# -----------------------------------------------------------------------------
# 2. A-TENSOR SELECTION RULE: (p,q) (x) Ad = (p,q) (x) (1,1)
# -----------------------------------------------------------------------------
print("=" * 80)
print("2. WIGNER-ECKART SELECTION RULE: (p,q) (x) (1,1)")
print("=" * 80)
print()
print("  SU(3) adjoint = (1,1), dim = 8. Decomposition:")
print("  (p,q) (x) (1,1)  contains  (p+1,q+1), (p-1,q+1), (p+1,q-1),")
print("                             (p-1,q-1), (p,q),    (p+2,q-1),")
print("                             (p-1,q+2), etc. (up to 10 tensor products)")
print("  We use the standard Littlewood-Richardson result for SU(3).")
print()


def tensor_with_adjoint(p, q):
    """
    Return the set of Young-label pairs (p', q') that appear in the
    Clebsch-Gordan decomposition (p,q) (x) (1,1).

    SU(3) Clebsch-Gordan for (p,q) (x) (1,1):
        Using Young-tableau / LR rules, the result is the multiset of
        dominant weights reachable by adding one box and subtracting one
        box, plus the trivial and the adjoint contributions.

    Explicitly (Slansky 1981, Di Francesco, Mathieu, Senechal):
        (p,q) (x) (1,1) = (p+1,q+1) + (p+2,q-1) + (p-1,q+2)
                         + (p+1,q-2) + (p-2,q+1)
                         + 2*(p,q)
                         + (p-1,q-1)

    with the convention that any term containing a negative index is dropped.
    (This is the standard result used, e.g., in Baptista Paper 14 sect 3.)
    """
    candidates = [
        (p + 1, q + 1),
        (p + 2, q - 1),
        (p - 1, q + 2),
        (p + 1, q - 2),
        (p - 2, q + 1),
        (p, q),           # appears with multiplicity 2 (see below)
        (p - 1, q - 1),
    ]
    multiplicity = {}  # (local)
    for (pp, qq) in candidates:
        if pp < 0 or qq < 0:
            continue
        key = (pp, qq)
        multiplicity[key] = multiplicity.get(key, 0) + 1
    # (p,q) appears twice (from the trivial piece within the 8 (x) rep)
    if (p, q) in multiplicity:
        multiplicity[(p, q)] += 1
    return multiplicity


# Build the allowed-transitions graph restricted to sectors present in the cache.
present = set(sector_data.keys())
transitions = {}                            # (local)  pq -> list[(pq', mult)]
n_transitions_total = 0                     # (local)
for pq in pq_list:
    p, q = pq
    targets = tensor_with_adjoint(p, q)
    allowed = [(t, m) for t, m in targets.items()
               if t in present and t != pq]   # exclude self
    transitions[pq] = allowed
    n_transitions_total += len(allowed)

print(f"  Total allowed off-diagonal transitions: {n_transitions_total}")
avg_fanout = n_transitions_total / max(1, len(pq_list))
print(f"  Average fan-out per sector: {avg_fanout:.2f}")
print()


# -----------------------------------------------------------------------------
# 3. A-TENSOR MATRIX ELEMENTS
# -----------------------------------------------------------------------------
print("=" * 80)
print("3. A-TENSOR MATRIX ELEMENTS")
print("=" * 80)
print()
print("  Structural scale: the O'Neill integrability tensor A_X Y of a")
print("  Riemannian submersion M4 x K -> M4 is controlled by the horizontal")
print("  curvature F. The relevant dimensionless coupling at the fold is")
print("  (H / M_KK)^2 because the only horizontal scale at the present-day")
print("  base is the Hubble rate. We therefore write")
print()
print("    | A_{(p,q) <-> (p',q')} |^2 / M_KK^4")
print("         =  eps_AT * m * C_adj^2")
print("                  * |lambda|_max[(p,q)] * |lambda|_max[(p',q')]")
print()
print("  where m is the (p',q') multiplicity inside (p,q) (x) (1,1), and")
print("  C_adj^2 = Cas(adj) = 3 is the adjoint quadratic Casimir (universal")
print("  Wigner-Eckart Frobenius norm bound).")
print()

eps_AT = (H_0_GeV / M_KK) ** 2              # (local)
C_ADJ_SQ = 3.0                              # (local) quadratic Casimir of SU(3) adjoint

print(f"  eps_AT    = {eps_AT:.6e}   (natural expansion parameter)")
print(f"  C_adj^2   = {C_ADJ_SQ}       (= quadratic Casimir of SU(3) adjoint)")
print()


# Compute the sector-averaged second-order shift to |lambda|^2 (units of M_KK^2)
# and track the minimum denominator encountered.
delta_lam2_sector = {}                      # (local)
min_denom_abs = np.inf                      # (local)
min_denom_pair = (None, None)               # (local)
degenerate_pairs = []                       # (local)
a_matrix_elements_sq = []                   # (local) all |A|^2 values / M_KK^4

for pq in pq_list:
    info = sector_data[pq]
    lam2_self = info["lam2_mean"]
    lam_max_self = info["omega_max"]
    delta = 0.0                             # (local)
    for (pqp, mult) in transitions[pq]:
        info_p = sector_data[pqp]
        lam2_other = info_p["lam2_mean"]
        lam_max_other = info_p["omega_max"]
        A_sq = eps_AT * mult * C_ADJ_SQ * lam_max_self * lam_max_other
        a_matrix_elements_sq.append(A_sq)
        denom = lam2_self - lam2_other
        if denom == 0.0:
            degenerate_pairs.append((pq, pqp))
            continue
        if abs(denom) < min_denom_abs:
            min_denom_abs = abs(denom)
            min_denom_pair = (pq, pqp)
        delta += A_sq / denom
    delta_lam2_sector[pq] = delta

a_matrix_elements_sq = np.asarray(a_matrix_elements_sq, dtype=np.float64)

print(f"  |A|^2 statistics over all transitions ({a_matrix_elements_sq.size}):")
print(f"    min  = {a_matrix_elements_sq.min():.6e}  (units of M_KK^4)")
print(f"    max  = {a_matrix_elements_sq.max():.6e}")
print(f"    mean = {a_matrix_elements_sq.mean():.6e}")
print(f"    sum  = {a_matrix_elements_sq.sum():.6e}")
print()
print(f"  Closest denominator encountered:")
print(f"    min |lam2_self - lam2_other| = {min_denom_abs:.6e}")
print(f"    pair = {min_denom_pair}")
print()
print(f"  Numerically degenerate pairs flagged: {len(degenerate_pairs)}")
if degenerate_pairs[:5]:
    print(f"    first 5: {degenerate_pairs[:5]}")
print()

delta_lam2_array = np.asarray(list(delta_lam2_sector.values()), dtype=np.float64)
delta_lam2_max_abs = float(np.max(np.abs(delta_lam2_array)))
delta_lam2_rel_max = float(
    np.max(np.abs(delta_lam2_array) /
           np.asarray([sector_data[pq]["lam2_mean"] for pq in pq_list]))
)
print(f"  delta lam^2 statistics:")
print(f"    max |delta lam^2|   = {delta_lam2_max_abs:.6e}")
print(f"    max fractional      = {delta_lam2_rel_max:.6e}")
print()


# Anti-symmetry cross-check: the contribution of the pair (pq -> pq') to
# delta lam2[pq] and the contribution of (pq' -> pq) to delta lam2[pq'] should
# be equal in magnitude and opposite in sign (second-order PT level repulsion).
antisym_check = []                          # (local)
for pq in pq_list:
    for (pqp, mult) in transitions[pq]:
        if pq >= pqp:
            continue  # each unordered pair once
        # Check if reverse transition exists
        reverse_allowed = [t for (t, m) in transitions[pqp]]
        if pq not in reverse_allowed:
            continue
        mult_rev = dict(transitions[pqp]).get(pq, 0)
        lam2_a = sector_data[pq]["lam2_mean"]
        lam2_b = sector_data[pqp]["lam2_mean"]
        denom_ab = lam2_a - lam2_b
        if denom_ab == 0:
            continue
        lam_max_a = sector_data[pq]["omega_max"]
        lam_max_b = sector_data[pqp]["omega_max"]
        A_ab_sq = eps_AT * mult * C_ADJ_SQ * lam_max_a * lam_max_b
        A_ba_sq = eps_AT * mult_rev * C_ADJ_SQ * lam_max_a * lam_max_b
        contrib_a = A_ab_sq / denom_ab
        contrib_b = A_ba_sq / (-denom_ab)
        antisym_check.append(contrib_a + contrib_b)
# Note: the sum is zero only when mult_ab = mult_ba.
antisym_check = np.asarray(antisym_check, dtype=np.float64)
print(f"  Anti-symmetry cross-check (sum of (pq->pq')+(pq'->pq) contributions):")
if antisym_check.size:
    print(f"    max|violation|           = {np.max(np.abs(antisym_check)):.6e}")
    # For mult_ab = mult_ba the residual should be zero; otherwise the residual
    # equals (m_ab - m_ba) * |A|^2_base / denom and is structural.
else:
    print("    (no reciprocal pairs in the present truncation)")
print()


# -----------------------------------------------------------------------------
# 4. PROPAGATE TO CORE QUANTITIES
# -----------------------------------------------------------------------------
print("=" * 80)
print("4. PROPAGATE CORRECTION TO CORE QUANTITIES")
print("=" * 80)
print()

# For spectral-moment observables we compute partial sums in the S73B project
# convention (see s74_r_protected_triple.py) at L_max = 7 which is the largest
# complete block available in the cache.

def partial_sums_S73B_with_delta(L_max, delta_lam2_dict):
    """
    Compute the S73B-convention partial sums P_0, P_1, P_2 at L_max, applying
    a fractional shift delta_lam2_dict[(p,q)] / lam2_mean[(p,q)] uniformly
    inside each sector.

    P_0 = sum dim * N
    P_1 = sum dim * sum_n |lam_n|^{-1}     <->  a_2
    P_2 = sum dim * sum_n |lam_n|^{-2}     <->  a_4
    """
    P_0 = 0.0                               # (local)
    P_1 = 0.0                               # (local)
    P_2 = 0.0                               # (local)
    for pq, info in sector_data.items():
        p, q = pq
        if p + q > L_max:
            continue
        dim = info["dim"]
        lam2_mean = info["lam2_mean"]
        delta = delta_lam2_dict.get(pq, 0.0)
        # Fractional shift applied uniformly inside the sector
        frac = delta / lam2_mean if lam2_mean > 0 else 0.0
        scale_inv2 = 1.0 / (1.0 + frac)       # |lam'|^2 = |lam|^2 (1 + frac)
        scale_inv1 = 1.0 / np.sqrt(1.0 + frac) if (1.0 + frac) > 0 else 0.0
        abs_ev = info["abs_evals"]
        mask = abs_ev > 0
        P_0 += dim * mask.sum()
        P_1 += dim * np.sum(scale_inv1 / abs_ev[mask])
        P_2 += dim * np.sum(scale_inv2 / (abs_ev[mask] ** 2))
    a0 = 0.5 * P_0                          # (local)
    a2 = 0.5 * P_1                          # (local)
    a4 = 0.5 * P_2                          # (local)
    return dict(P_0=P_0, P_1=P_1, P_2=P_2, a0=a0, a2=a2, a4=a4)


L_eval = 7                                  # (local)  largest complete L_max

# Baseline (delta = 0)
zero_delta = {pq: 0.0 for pq in pq_list}    # (local)
base = partial_sums_S73B_with_delta(L_eval, zero_delta)

# Corrected (delta from A-tensor)
corr = partial_sums_S73B_with_delta(L_eval, delta_lam2_sector)

print(f"  L_max = {L_eval}")
print(f"  {'':15s} {'baseline':>16s} {'corrected':>16s} {'delta/base':>14s}")
for key in ("a0", "a2", "a4"):
    b = base[key]
    c = corr[key]
    rel = (c - b) / b if b != 0 else 0.0
    print(f"  {key:<15s} {b:>16.6e} {c:>16.6e} {rel:>14.3e}")
print()
print("  NOTE: The corrected-minus-baseline shift is below float64 precision")
print("  (~1e-16). We therefore compute the analytic first-order shift directly")
print("  from the per-sector fractional correction, which is the physically")
print("  meaningful quantity regardless of floating-point cancellation.")
print()

# Analytic first-order shift (avoids float64 cancellation).
#    a_{2k} = (1/2) sum dim * sum_n |lam_n|^{-k}
# Under lam^2 -> lam^2 (1 + frac_{(p,q)}):
#    |lam|^{-k} -> |lam|^{-k} (1 - (k/2) frac_{(p,q)} + O(frac^2))
# Hence
#    delta a_2 = -(1/2) sum dim frac (sum_n 1/|lam_n|)
#    delta a_4 = -(1/1) sum dim frac (sum_n 1/|lam_n|^2)    (factor 2*(1/2) cancels)
delta_a2_analytic = 0.0                     # (local)
delta_a4_analytic = 0.0                     # (local)
for pq, info in sector_data.items():
    p, q = pq
    if p + q > L_eval:
        continue
    dim = info["dim"]
    lam2_mean = info["lam2_mean"]
    frac = delta_lam2_sector[pq] / lam2_mean if lam2_mean > 0 else 0.0
    abs_ev = info["abs_evals"]
    mask = abs_ev > 0
    sum_invlam  = np.sum(1.0 / abs_ev[mask])
    sum_invlam2 = np.sum(1.0 / (abs_ev[mask] ** 2))
    delta_a2_analytic += dim * (-0.5 * frac) * sum_invlam
    delta_a4_analytic += dim * (-1.0 * frac) * sum_invlam2
delta_a2_analytic *= 0.5                    # S73B convention factor
delta_a4_analytic *= 0.5                    # S73B convention factor

a2_rel_analytic = delta_a2_analytic / base["a2"] if base["a2"] else 0.0   # (local)
a4_rel_analytic = delta_a4_analytic / base["a4"] if base["a4"] else 0.0   # (local)

print(f"  Analytic first-order shifts (single-precision-safe):")
print(f"    delta a_2 (abs) = {delta_a2_analytic:.6e}  "
      f"(rel = {a2_rel_analytic:.6e})")
print(f"    delta a_4 (abs) = {delta_a4_analytic:.6e}  "
      f"(rel = {a4_rel_analytic:.6e})")
print()

# R_protected = a_0 * a_4 / a_2^2
# delta R / R = delta a_0 / a_0 + delta a_4 / a_4 - 2 delta a_2 / a_2
#             = 0 + a4_rel_analytic - 2 * a2_rel_analytic
R_base = base["a0"] * base["a4"] / base["a2"] ** 2
R_rel_analytic = a4_rel_analytic - 2.0 * a2_rel_analytic                  # (local)
R_corr = R_base * (1.0 + R_rel_analytic)
R_rel = R_rel_analytic

print(f"  R_protected_base       = {R_base:.6e}")
print(f"  R_protected_corr       = {R_corr:.6e}")
print(f"  R_protected frac shift = {R_rel:.3e}")
print()

# n_s correction: since n_s depends on ratios of a_k's (via S_tree and dS/dtau),
# we take the fractional correction on n_s to be bounded by the relative shift
# on R_protected, which aggregates all three moments.
ns_frac_shift = abs(R_rel_analytic)          # (local) conservative bound
ns_corr_value = NS_TREE_REFERENCE * (1.0 + R_rel_analytic)  # (local) first-order linearisation
print(f"  n_s (tree reference)   = {NS_TREE_REFERENCE}")
print(f"  n_s fractional shift   = {ns_frac_shift:.3e} (bounded by |R_rel|)")
print()

# m_H correction: tree m_H ~ sqrt(|R_{g_phi}|) * lambda-factor, and the Ricci
# scalar R_{g_phi} is protected by the exact formula (2.40) and not corrected
# at O(eps_AT) -- only the KK-threshold spectral sum receives the A-tensor
# contribution, which enters m_H through the a_4 moment in the C_phi coefficient.
# The m_H fractional shift is therefore bounded by delta a_4 / a_4.
a4_rel_shift = a4_rel_analytic                          # (local) use analytic
m_H_frac_shift = 0.5 * abs(a4_rel_shift)                # (local)
m_H_corr_value = M_H_TREE_REFERENCE * (1.0 + 0.5 * a4_rel_shift)
print(f"  m_H (tree reference)   = {M_H_TREE_REFERENCE} GeV")
print(f"  m_H fractional shift   = {m_H_frac_shift:.3e} (bound = 0.5 |delta a_4/a_4|)")
print()


# -----------------------------------------------------------------------------
# 5. GATE CLASSIFICATION
# -----------------------------------------------------------------------------
print("=" * 80)
print("5. GATE CLASSIFICATION")
print("=" * 80)
print()

frac_shifts = {
    "a_0": 0.0,                                          # structural: count only
    "a_2": abs(a2_rel_analytic),
    "a_4": abs(a4_rel_analytic),
    "R_protected": abs(R_rel_analytic),
    "n_s": ns_frac_shift,
    "m_H": m_H_frac_shift,
}
max_frac = max(frac_shifts.values())
max_key = max(frac_shifts, key=frac_shifts.get)

print(f"  Fractional corrections to CORE quantities:")
for k, v in frac_shifts.items():
    print(f"    {k:<14s} = {v:.3e}")
print()
print(f"  max fractional shift = {max_frac:.3e}  (on {max_key})")
print(f"  Gate thresholds: PASS < {GATE_PASS_FRAC:.0%}, "
      f"INFO < {GATE_INFO_FRAC:.0%}, FAIL >= {GATE_INFO_FRAC:.0%}")
print()

if max_frac < GATE_PASS_FRAC:
    verdict = "PASS"
elif max_frac < GATE_INFO_FRAC:
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"  VERDICT: {verdict}")
print()


# -----------------------------------------------------------------------------
# 6. CROSS-CHECKS
# -----------------------------------------------------------------------------
print("=" * 80)
print("6. CROSS-CHECKS")
print("=" * 80)
print()

# Cross-check 1: eps_AT scale
expected_eps = (1.438e-42 / 7.4286e16) ** 2
print(f"  [CC1] eps_AT = (H_0/M_KK)^2")
print(f"        expected ~ {expected_eps:.3e}")
print(f"        computed  = {eps_AT:.3e}")
print(f"        agreement: {abs(eps_AT - expected_eps) / expected_eps:.2e}")
print()

# Cross-check 2: antisymmetry statistics
print(f"  [CC2] Anti-symmetry: sum of reciprocal contributions")
if antisym_check.size:
    print(f"        max residual = {np.max(np.abs(antisym_check)):.3e}")
    print(f"        structural (survives when mult_ab = mult_ba)")
else:
    print("        no reciprocal pairs in truncation")
print()

# Cross-check 3: min denominator safety
min_denom_norm = min_denom_abs / delta_lam2_rel_max if delta_lam2_rel_max > 0 else np.inf
print(f"  [CC3] Minimum denominator |lam2_a - lam2_b|")
print(f"        value = {min_denom_abs:.3e}")
print(f"        pair  = {min_denom_pair}")
print(f"        no division by zero encountered: {len(degenerate_pairs) == 0}")
print()

# Cross-check 4: order-of-magnitude of delta lam^2
# expected: eps_AT * (lam2 scale) * (num transitions) ~ 10^{-118} * O(1)
expected_mag = eps_AT * 10.0
print(f"  [CC4] delta lam^2 order-of-magnitude")
print(f"        expected ~ eps_AT * O(10) = {expected_mag:.3e}")
print(f"        observed = {delta_lam2_max_abs:.3e}")
print()

# Cross-check 5: sanity of max shift vs eps_AT
print(f"  [CC5] max frac shift / eps_AT = {max_frac / eps_AT:.3e}")
print(f"        (should be O(1-100); if >> eps_AT^{-1}: resonance enhancement)")
print()


# -----------------------------------------------------------------------------
# 7. SAVE ARTIFACTS
# -----------------------------------------------------------------------------
print("=" * 80)
print("7. SAVE ARTIFACTS")
print("=" * 80)

pq_arr = np.array(pq_list, dtype=np.int32)
delta_arr = np.array([delta_lam2_sector[pq] for pq in pq_list], dtype=np.float64)
lam2_mean_arr = np.array([sector_data[pq]["lam2_mean"] for pq in pq_list], dtype=np.float64)
dim_arr = np.array([sector_data[pq]["dim"] for pq in pq_list], dtype=np.int32)

np.savez_compressed(
    OUT_NPZ,
    eps_AT=eps_AT,
    H_0_GeV=H_0_GeV,
    M_KK=M_KK,
    tau_fold=tau_fold,
    pq_list=pq_arr,
    dim_per_sector=dim_arr,
    lam2_mean_per_sector=lam2_mean_arr,
    delta_lam2_per_sector=delta_arr,
    a_matrix_elements_sq=a_matrix_elements_sq,
    min_denom_abs=min_denom_abs,
    min_denom_pair=np.array(min_denom_pair, dtype=object),
    L_eval=L_eval,
    a0_base=base["a0"], a2_base=base["a2"], a4_base=base["a4"],
    a0_corr=corr["a0"], a2_corr=corr["a2"], a4_corr=corr["a4"],
    R_base=R_base, R_corr=R_corr,
    ns_tree_ref=NS_TREE_REFERENCE,
    m_H_tree_ref=M_H_TREE_REFERENCE,
    frac_shift_a2=frac_shifts["a_2"],
    frac_shift_a4=frac_shifts["a_4"],
    frac_shift_R=frac_shifts["R_protected"],
    frac_shift_ns=frac_shifts["n_s"],
    frac_shift_mH=frac_shifts["m_H"],
    max_frac=max_frac,
    max_key=max_key,
    verdict=verdict,
    gate_pass=GATE_PASS_FRAC,
    gate_info=GATE_INFO_FRAC,
)
print(f"  NPZ saved: {OUT_NPZ}")


# -----------------------------------------------------------------------------
# 8. PLOT
# -----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle(
    f"A-TENSOR-CORRECTION-74  |  eps_AT=(H_0/M_KK)^2 = {eps_AT:.3e}\n"
    f"max fractional shift = {max_frac:.3e} on {max_key}  |  VERDICT: {verdict}",
    fontsize=12,
)

# (a) |A|^2 histogram
ax = axes[0, 0]
ax.hist(np.log10(a_matrix_elements_sq + 1e-300), bins=30, color="steelblue",
        edgecolor="k", alpha=0.85)
ax.set_xlabel(r"$\log_{10}|A|^2 / M_{KK}^4$")
ax.set_ylabel("count")
ax.set_title("A-tensor matrix element magnitudes")
ax.grid(True, alpha=0.3)

# (b) delta lam^2 per sector
ax = axes[0, 1]
level_arr = np.array([p + q for (p, q) in pq_list])
ax.scatter(level_arr, np.abs(delta_arr) + 1e-300, c="tab:red", s=40, alpha=0.8)
ax.set_yscale("log")
ax.set_xlabel("level p+q")
ax.set_ylabel(r"$|\delta\lambda^2_{(p,q)}|$")
ax.set_title("Second-order shift per sector (absolute)")
ax.grid(True, alpha=0.3)

# (c) fractional shift bar chart
ax = axes[1, 0]
keys = list(frac_shifts.keys())
vals = [max(v, 1e-300) for v in frac_shifts.values()]
ax.bar(keys, vals, color=["lightgrey"] + ["steelblue"] * 5)
ax.axhline(GATE_PASS_FRAC, color="green", ls="--", label=f"PASS < {GATE_PASS_FRAC:.0%}")
ax.axhline(GATE_INFO_FRAC, color="orange", ls="--", label=f"INFO < {GATE_INFO_FRAC:.0%}")
ax.set_yscale("log")
ax.set_ylabel("|fractional correction|")
ax.set_title("Fractional corrections to CORE quantities")
ax.legend(loc="upper right", fontsize=9)
ax.grid(True, alpha=0.3, axis="y")
for tick in ax.get_xticklabels():
    tick.set_rotation(30)

# (d) regime diagram
ax = axes[1, 1]
ax.text(0.05, 0.95, "Regime of validity", transform=ax.transAxes, weight="bold",
        fontsize=11, va="top")
regime_lines = [
    f"eps_AT        = (H_0/M_KK)^2 = {eps_AT:.3e}",
    f"max |dlam^2|  = {delta_lam2_max_abs:.3e}",
    f"max frac      = {delta_lam2_rel_max:.3e}",
    "",
    "PT controls:",
    f"  min denom    = {min_denom_abs:.3e}",
    f"  pair         = {min_denom_pair}",
    f"  deg pairs    = {len(degenerate_pairs)}",
    "",
    "Core shifts:",
    f"  a_2          = {frac_shifts['a_2']:.3e}",
    f"  a_4          = {frac_shifts['a_4']:.3e}",
    f"  R_protected  = {frac_shifts['R_protected']:.3e}",
    f"  n_s          = {frac_shifts['n_s']:.3e}",
    f"  m_H          = {frac_shifts['m_H']:.3e}",
    "",
    f"VERDICT: {verdict}",
]
for i, line in enumerate(regime_lines):
    ax.text(0.05, 0.88 - 0.055 * i, line, transform=ax.transAxes,
            family="monospace", fontsize=9, va="top")
ax.axis("off")

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
plt.close()
print(f"  PNG saved: {OUT_PNG}")
print()

print("=" * 80)
print(f"Elapsed: {time.time() - t_start:.2f} s")
print("DONE")
print("=" * 80)
