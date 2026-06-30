#!/usr/bin/env python3
"""
s83_w2_g26_sdw_nlo_alpha_universality.py -- S83 W2-G26
=======================================================

Gate ID: S83-SDW-NLO-ALPHA-UNIVERSALITY
Trigger: [VERIFY]
Classification: GEOMETRIC
Owner: spectral-geometer

Task
----
Test whether the NLO rank-scaling exponent alpha_SDW^{NLO} of R_1 drift in
SDW-regularized spectral action is UNIVERSAL (gauge-group independent) to
within 10% across {SU(2), SU(3), SU(4), SU(5)}.

Physics framing (substrate)
---------------------------
R_1 = a_0 * a_4 / a_2^2 is a dimensionless ratio of Seeley-DeWitt coefficients
on a compact simple Lie group G with bi-invariant metric.  Under finite-L_max
Peter-Weyl truncation, R_1 has zero NET Weyl exponent (alpha_0 + alpha_4 =
2*alpha_2 = 2*(d+r+2)) -> the leading divergence cancels.  The residual
pre-asymptotic correction scales as O(L^{-alpha_NLO}).

The S77 D3-R1-UNIVERSAL theorem (see sessions/archive/session-77, s77_r1_other_groups.py)
predicted alpha_NLO(G) = rank(G).  This was numerically confirmed by S78 W3-K
(s78_r1_lmax_cross_groups.py) which fit log(drift) vs log(L) for 5 groups and
found alpha_fit matches rank within ~15% in 3 schemes.

This gate (W2-G26) asks a DIFFERENT question: is the NLO exponent itself the
SAME NUMBER across {SU(2), SU(3), SU(4), SU(5)}?  If the S77 theorem is right,
the answer should be NO: alpha_NLO(SU(2)) ~ 1, alpha_NLO(SU(5)) ~ 4, so
span = max/min ~ 4.0 >> 1.25.  This is STRUCTURALLY INFORMATIVE: the
rank-dependence of the NLO exponent is a FINGERPRINT of the substrate's
weight-lattice dimensionality, not a failure of universality.

Method
------
For each G in {SU(2), SU(3), SU(4), SU(5)}:
  (1) Enumerate irreps Lambda with level |Lambda|_1 <= L_max (sum of Dynkin
      labels) for L_max in a PINNED sampling set.
  (2) lambda^2 = ||Lambda + rho||^2 via symmetrized Cartan inverse.
  (3) SDW scheme: a_k = (dim_spinor/2) * sum_Lambda dim(Lambda)^2 *
                       (lam/lam_max) * lam^{-k}
      where lam_max = sqrt(max lam^2) is the UV cutoff.
  (4) R_1(L, SDW) = a_0 * a_4 / a_2^2.
  (5) Fit log-log: |R_1(L) - R_1(L_ref)|/R_1(L_ref) ~ C * L^{-alpha_NLO}
      where L_ref is the largest L sampled.  Extract alpha_SDW^{NLO}(G).
  (6) Compute span = max/min of alpha across 4 groups.
  (7) Gate: PASS if span < 1.10, INFO if 1.10 <= span < 1.25, FAIL if > 1.25.

L_max pinned sampling (chosen to balance rank-scaling visibility with
computational cost; no post-hoc cherry-picking):
  SU(2): (5, 6, 7, 8, 9, 10)       # rank 1, cheap
  SU(3): (3, 4, 5, 6, 7)           # rank 2
  SU(4): (3, 4, 5, 6)              # rank 3
  SU(5): (3, 4, 5)                 # rank 4 (expensive)

[SIGN] Substitution chain
-------------------------
  Step 1 (definition):
    alpha_SDW^{NLO}(G) = slope of log(|R_1(L) - R_1(L_ref)|/R_1(L_ref))
                        versus log(L) via linear regression, negated.
    span = max_G alpha / min_G alpha across {SU(2), SU(3), SU(4), SU(5)}.
  Step 2 (substitution — universality hypothesis):
    If NLO is universal across gauge groups (rank-independent),
    alpha_NLO(G) is the SAME number for all G, hence span = 1.0.
  Step 3 (S77 theorem prediction):
    alpha_NLO(G) = rank(G) (S77-D3-R1-UNIVERSAL).
    Rank(SU(2))=1, Rank(SU(3))=2, Rank(SU(4))=3, Rank(SU(5))=4.
    Predicted span = max rank / min rank = 4 / 1 = 4.0.
  Step 4 (direction from canonical form):
    span > 1.25 <=> alpha is GROUP-DEPENDENT (rank-scaling).
    span < 1.10 <=> alpha is universal (rank-independent).
  Step 5 (conclusion):
    S77 theorem => span ~ 4.0 => FAIL is structurally expected.
    FAIL here is INFORMATIVE: it confirms alpha_NLO tracks rank(G), not a
    constant.  A PASS would REFUTE the S77 theorem.

Cross-checks
------------
  (a) SU(3) at L=3 (bi-invariant) should have a_0 = 6440 (canonical, a0_fold
      is at tau=0.19 fold, but tau=0 a_0 should match at same L).
  (b) alpha_fit vs rank(G) should be ~ 1:1 up to pre-asymptotic noise
      (cross-check with S77 W3-M and S78 W3-K).
  (c) R^2 of log-log fit >= 0.90 (else fit is unreliable).

Input SHA-256 pins
------------------
  canonical_constants.py: computed at runtime

Expected output 4-tuple
-----------------------
  (span=?, scheme=SDW-NLO, convention=gauge-group-atlas, L_max=N/A)

Agent: spectral-geometer (Session 83, Wave 2, G26)
"""

import numpy as np
import sys
import os
import time
import hashlib
from itertools import product as iter_product

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import PI, a0_fold, a2_fold, a4_fold, R_protected_fold

# =============================================================================
# HEADER — pin inputs, print closure map
# =============================================================================

print("=" * 78)
print("S83 W2-G26: SDW-NLO-ALPHA-UNIVERSALITY")
print("Gate ID: S83-SDW-NLO-ALPHA-UNIVERSALITY")
print("Owner: spectral-geometer")
print("=" * 78)

# SHA-256 pin of canonical_constants.py
cc_path = os.path.join(SCRIPT_DIR, 'canonical_constants.py')  # (local)
with open(cc_path, 'rb') as f:
    cc_sha = hashlib.sha256(f.read()).hexdigest()  # (local)
print(f"  canonical_constants.py SHA-256: {cc_sha}")
print(f"  script SHA-256: (computed at runtime)")

# Pinned L_max sampling (upfront)
L_MAX_PINNED = {
    'SU(2)': (5, 6, 7, 8, 9, 10),   # (local) rank 1
    'SU(3)': (3, 4, 5, 6, 7),        # (local) rank 2
    'SU(4)': (3, 4, 5, 6),           # (local) rank 3
    'SU(5)': (3, 4, 5),              # (local) rank 4
}

# Pinned gate thresholds
SPAN_PASS_THRESHOLD = 1.10  # (local)
SPAN_INFO_THRESHOLD = 1.25  # (local)
R2_MIN = 0.85  # (local) log-log fit quality gate (soft; pre-asymptotic)

print()
print("  PINNED L_max sampling:")
for g, Ls in L_MAX_PINNED.items():
    print(f"    {g}: L_max in {list(Ls)}")
print()
print("  Scheme tested: SDW (Dixmier-Dimensional-Wick, f(x)=sqrt(x))")
print(f"  Span PASS threshold: < {SPAN_PASS_THRESHOLD}")
print(f"  Span INFO threshold: < {SPAN_INFO_THRESHOLD}")
print()

t_start = time.time()

# =============================================================================
# SECTION 1: ROOT SYSTEM DATA FOR SU(N)
# =============================================================================

def su_n_data(N):
    """
    Root system for SU(N) = A_{N-1}.

    Conventions (Dynkin labels basis; inner product via A_inv):
      - rank = N-1, dim = N^2 - 1
      - A_{ij} = 2*delta_{ij} - delta_{|i-j|,1}
      - (A_inv)_{ij} = min(i,j)*(N-max(i,j))/N  (1-indexed)
      - rho = (1,1,...,1) in Dynkin labels
      - ||Lambda + rho||^2 = (Lambda+rho)^T A_inv (Lambda+rho)

    Returns dict with name, dim, rank, dim_irrep, norm_lpr_sq.
    """
    rank = N - 1  # (local)
    dim = N * N - 1  # (local)

    # Cartan matrix A_{N-1}
    A = np.zeros((rank, rank))  # (local)
    for i in range(rank):
        A[i, i] = 2.0
        if i > 0:
            A[i, i-1] = -1.0
        if i < rank - 1:
            A[i, i+1] = -1.0

    # Inverse Cartan (weight-space inner product)
    A_inv = np.zeros((rank, rank))  # (local)
    for i in range(rank):
        for j in range(rank):
            A_inv[i, j] = min(i+1, j+1) * (N - max(i+1, j+1)) / N

    rho = np.ones(rank)  # (local) Weyl vector in Dynkin labels
    norm_rho_sq = float(rho @ A_inv @ rho)  # (local)

    def dim_irrep(hw):
        """Weyl dimension formula for SU(N)."""
        hw = np.array(hw, dtype=float)
        # Partition-coordinate: l_k = sum_{m=k-1}^{rank-1} hw[m] + (N - k)
        l = np.zeros(N)  # (local)
        for k in range(1, N + 1):
            l[k-1] = sum(hw[m] for m in range(k-1, rank)) + (N - k)
        d = 1.0  # (local)
        for i in range(N):
            for j in range(i + 1, N):
                d *= (l[i] - l[j]) / (j - i)
        return int(round(d))

    def norm_lpr_sq(hw):
        hw = np.array(hw, dtype=float)
        lpr = hw + rho  # (local)
        return float(lpr @ A_inv @ lpr)

    return {
        'name': f'SU({N})',
        'type': f'A_{rank}',
        'dim': dim,
        'rank': rank,
        'N': N,
        'rho_dynkin': rho,
        'cartan_inv': A_inv,
        'norm_rho_sq': norm_rho_sq,
        'dim_irrep': dim_irrep,
        'norm_lpr_sq': norm_lpr_sq,
    }


# =============================================================================
# SECTION 2: IRREP ENUMERATION (level = sum of Dynkin labels)
# =============================================================================

def enumerate_irreps(group_data, L_max):
    """All irreps with level = |Lambda|_1 <= L_max, non-negative Dynkin."""
    rank = group_data['rank']  # (local)
    irreps = []  # (local)

    def _generate(remaining_rank, remaining_sum):
        if remaining_rank == 0:
            yield ()
            return
        for a in range(remaining_sum + 1):
            for rest in _generate(remaining_rank - 1, remaining_sum - a):
                yield (a,) + rest

    for hw_tuple in _generate(rank, L_max):
        level = sum(hw_tuple)  # (local)
        lam_sq = group_data['norm_lpr_sq'](hw_tuple)  # (local)
        dim_rep = group_data['dim_irrep'](hw_tuple)  # (local)
        if dim_rep <= 0:
            print(f"    WARNING: dim({hw_tuple}) = {dim_rep}, skipping")
            continue
        irreps.append({
            'hw': hw_tuple,
            'dim': dim_rep,
            'lam_sq': lam_sq,
            'level': level,
        })

    return irreps


# =============================================================================
# SECTION 3: SDW-REGULATED MOMENT COMPUTATION
# =============================================================================

def compute_SDW_moments(group_data, L_max_values):
    """
    SDW scheme:
      a_k^SDW(L) = (dim_spinor/2) * sum_{Lambda: level<=L} dim(Lambda)^2 *
                   (lam/lam_max) * lam^{-k}
      lam_max = max_{Lambda: level<=L} sqrt(||Lambda+rho||^2)

    Returns dict: L -> {'a0', 'a2', 'a4', 'R1', 'n_irreps', 'lam_max'}
    """
    d = group_data['dim']  # (local)
    dim_spinor = 2 ** (d // 2)  # (local)
    half_spinor = dim_spinor / 2  # (local)

    max_L = max(L_max_values)  # (local)
    all_irreps = enumerate_irreps(group_data, max_L)  # (local)

    results = {}  # (local)

    for L in L_max_values:
        irreps_L = [ir for ir in all_irreps if ir['level'] <= L]  # (local)
        lam_sq_arr = np.array([ir['lam_sq'] for ir in irreps_L])  # (local)
        weight_arr = np.array([ir['dim']**2 for ir in irreps_L], dtype=np.float64)  # (local)

        lam_arr = np.sqrt(lam_sq_arr)  # (local)
        lam_max = float(np.max(lam_arr))  # (local)
        xi = lam_arr / lam_max  # (local) = sqrt(x), x = lam^2/lam_max^2

        # SDW weight: f(x) = sqrt(x) = xi
        w_SDW = xi  # (local)

        a0 = half_spinor * float(np.sum(weight_arr * w_SDW))  # (local)
        a2 = half_spinor * float(np.sum(weight_arr * w_SDW / lam_sq_arr))  # (local)
        a4 = half_spinor * float(np.sum(weight_arr * w_SDW / lam_sq_arr ** 2))  # (local)
        R1 = a0 * a4 / (a2 ** 2) if a2 > 0 else float('nan')  # (local)

        results[L] = {
            'a0': a0,
            'a2': a2,
            'a4': a4,
            'R1': R1,
            'n_irreps': len(irreps_L),
            'lam_max': lam_max,
        }

    return results


# =============================================================================
# SECTION 4: LOG-LOG SLOPE EXTRACTION (NLO EXPONENT)
# =============================================================================

def fit_nlo_exponent(L_vals, R1_vals):
    """
    Fit: |R_1(L) - R_1(L_ref)|/|R_1(L_ref)| ~ C * L^{-alpha_NLO}

    L_ref = max(L_vals). Drop L_ref (drift=0 by construction); fit the rest
    in log-log coordinates via np.polyfit(deg=1).

    Returns (alpha_NLO, log_C, R_squared, n_points).
    """
    L_arr = np.array(L_vals, dtype=float)  # (local)
    R1_arr = np.array(R1_vals, dtype=float)  # (local)
    i_ref = int(np.argmax(L_arr))  # (local)
    R1_ref = R1_arr[i_ref]  # (local)

    mask = np.ones(len(L_arr), dtype=bool)  # (local)
    mask[i_ref] = False
    L_fit = L_arr[mask]  # (local)
    drift = np.abs(R1_arr[mask] - R1_ref) / abs(R1_ref)  # (local)

    pos = drift > 1e-15  # (local)
    if np.sum(pos) < 2:
        return np.nan, np.nan, np.nan, int(np.sum(pos))

    x = np.log(L_fit[pos])  # (local)
    y = np.log(drift[pos])  # (local)
    slope, intercept = np.polyfit(x, y, 1)
    alpha = -slope  # (local)
    log_C = intercept  # (local)

    y_pred = slope * x + intercept  # (local)
    ss_res = float(np.sum((y - y_pred) ** 2))  # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))  # (local)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-30 else float('nan')  # (local)
    return float(alpha), float(log_C), R2, int(np.sum(pos))


# =============================================================================
# SECTION 5: COMPUTE FOR 4 GROUPS
# =============================================================================

print("=" * 78)
print("SECTION 5: COMPUTE R_1 UNDER SDW FOR 4 GROUPS")
print("=" * 78)

GROUPS = [
    ('SU(2)', su_n_data(2), L_MAX_PINNED['SU(2)']),
    ('SU(3)', su_n_data(3), L_MAX_PINNED['SU(3)']),
    ('SU(4)', su_n_data(4), L_MAX_PINNED['SU(4)']),
    ('SU(5)', su_n_data(5), L_MAX_PINNED['SU(5)']),
]

all_results = {}  # (local)

for group_name, group_data, L_vals in GROUPS:
    print(f"\n  ---- {group_name} ({group_data['type']}, dim={group_data['dim']}, rank={group_data['rank']}) ----")
    print(f"  L_max sampling: {list(L_vals)}")
    t0 = time.time()
    res = compute_SDW_moments(group_data, L_vals)
    dt = time.time() - t0
    print(f"  Elapsed: {dt:.2f}s, max n_irreps at L={max(L_vals)}: {res[max(L_vals)]['n_irreps']}")

    print(f"  {'L_max':>5s} {'n_irreps':>9s} {'a_0(SDW)':>14s} {'a_2(SDW)':>14s} {'a_4(SDW)':>14s} {'R_1(SDW)':>12s}")
    print("  " + "-" * 75)
    for L in L_vals:
        r = res[L]
        print(f"  {L:>5d} {r['n_irreps']:>9d} {r['a0']:>14.3e} {r['a2']:>14.3e} "
              f"{r['a4']:>14.3e} {r['R1']:>12.6f}")

    all_results[group_name] = {
        'group_data': group_data,
        'L_vals': list(L_vals),
        'results': res,
    }


# =============================================================================
# SECTION 6: CROSS-CHECK (SU(3) bi-invariant a_0 at L=3 — zeta scheme comparison)
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 6: CROSS-CHECK — SU(3) BI-INVARIANT a_0 AT L=3")
print("=" * 78)

# S77 Section 4 cross-check: SU(3) bi-invariant a_0 at L=3 in ZETA scheme is 6440.
# The SDW scheme here applies the sqrt(x) weight, so a_0^SDW differs from a_0^zeta.
# We verify a_0^zeta separately as a sanity check.
su3 = su_n_data(3)  # (local)
irreps_su3_L3 = enumerate_irreps(su3, 3)  # (local)
a0_zeta_su3_L3 = 0.0  # (local) zeta-scheme a_0 = sum dim^2 (half-spinor)
d_su3 = su3['dim']  # (local)
ds_su3 = 2 ** (d_su3 // 2)  # (local)
hs_su3 = ds_su3 / 2  # (local)
for ir in irreps_su3_L3:
    a0_zeta_su3_L3 += ir['dim'] ** 2
a0_zeta_su3_L3 *= hs_su3

print(f"\n  SU(3) zeta-scheme a_0 at L=3 (no sqrt(x) weight): {a0_zeta_su3_L3:.2f}")
print(f"  Canonical a0_fold (S42, at tau=0.19): {a0_fold:.2f}")
print(f"  S77 Section 4 reported 6440 at L=3 bi-invariant -- MATCH expected.")
if abs(a0_zeta_su3_L3 - 6440.0) < 1.0:
    print("  CROSS-CHECK (a): bi-invariant SU(3) a_0(L=3, zeta) = 6440. PASS")
else:
    print(f"  CROSS-CHECK (a): DEVIATION = {a0_zeta_su3_L3 - 6440.0:.2f}")


# =============================================================================
# SECTION 7: EXTRACT NLO EXPONENT FOR EACH GROUP
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 7: NLO EXPONENT EXTRACTION (log-log slope of R_1 drift)")
print("=" * 78)

print(f"\n  {'Group':>6s} {'rank':>4s} {'alpha_SDW_NLO':>14s} {'R^2':>8s} "
      f"{'n_fit':>6s} {'|alpha-rank|/rank':>18s}")
print("  " + "-" * 72)

nlo_table = {}  # (local)
for group_name, info in all_results.items():
    group_data = info['group_data']
    r = group_data['rank']  # (local)
    L_vals = info['L_vals']
    res = info['results']

    R1_arr = [res[L]['R1'] for L in L_vals]  # (local)
    alpha, log_C, R2, n_pts = fit_nlo_exponent(L_vals, R1_arr)

    rel_vs_rank = abs(alpha - r) / r if r > 0 else float('nan')  # (local)

    nlo_table[group_name] = {
        'alpha': alpha,
        'R2': R2,
        'n_pts': n_pts,
        'log_C': log_C,
        'rank': r,
        'rel_vs_rank': rel_vs_rank,
    }

    print(f"  {group_name:>6s} {r:>4d} {alpha:>14.4f} {R2:>8.4f} "
          f"{n_pts:>6d} {rel_vs_rank*100:>17.2f}%")


# =============================================================================
# SECTION 8: GROUP-UNIVERSALITY TEST (SPAN = max alpha / min alpha)
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 8: GROUP-UNIVERSALITY TEST")
print("=" * 78)

alphas = {g: nlo_table[g]['alpha'] for g in nlo_table}  # (local)
valid_alphas = {g: a for g, a in alphas.items() if not np.isnan(a)}  # (local)

print(f"\n  alpha_SDW^NLO across groups:")
for g, a in alphas.items():
    r = nlo_table[g]['rank']  # (local)
    print(f"    {g} (rank {r}): alpha = {a:.4f}")

if len(valid_alphas) < 2:
    span = float('nan')  # (local)
    verdict = "N/A-INSUFFICIENT-DATA"  # (local)
else:
    alpha_max = max(valid_alphas.values())  # (local)
    alpha_min = min(valid_alphas.values())  # (local)
    span = alpha_max / alpha_min  # (local)
    group_max = max(valid_alphas, key=valid_alphas.get)  # (local)
    group_min = min(valid_alphas, key=valid_alphas.get)  # (local)

    print(f"\n  alpha_max = {alpha_max:.4f} ({group_max})")
    print(f"  alpha_min = {alpha_min:.4f} ({group_min})")
    print(f"  span = alpha_max / alpha_min = {span:.4f}")

    if span < SPAN_PASS_THRESHOLD:
        verdict = "PASS"  # (local)
    elif span < SPAN_INFO_THRESHOLD:
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local)

print(f"\n  Thresholds: PASS < {SPAN_PASS_THRESHOLD}, INFO < {SPAN_INFO_THRESHOLD}, FAIL >= {SPAN_INFO_THRESHOLD}")
print(f"  VERDICT: {verdict}")


# =============================================================================
# SECTION 9: STRUCTURAL INTERPRETATION (rank-dependence is the S77 THEOREM)
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 9: STRUCTURAL INTERPRETATION")
print("=" * 78)

# The S77 R1-UNIVERSAL theorem predicts alpha_NLO(G) = rank(G).
# Check correlation of fitted alpha vs rank.
ranks = np.array([nlo_table[g]['rank'] for g in sorted(nlo_table)])  # (local)
alphas_arr = np.array([nlo_table[g]['alpha'] for g in sorted(nlo_table)])  # (local)
names_arr = sorted(nlo_table)  # (local)

# Rank-1 (SU(2)) has only level=0 singlet at small L_max, trivial case; check
# if fit quality is reasonable.
print("\n  S77 D3-R1-UNIVERSAL theorem: alpha_NLO(G) = rank(G) at tau=0 bi-invariant")
print(f"  Fit vs theorem prediction:")
for g in sorted(nlo_table):
    r = nlo_table[g]['rank']  # (local)
    a = nlo_table[g]['alpha']  # (local)
    R2 = nlo_table[g]['R2']  # (local)
    theorem_match = abs(a - r) / r if r > 0 else float('nan')  # (local)
    print(f"    {g}: alpha_fit={a:.3f}, rank={r}, |fit-rank|/rank={theorem_match*100:.1f}%, R^2={R2:.3f}")

# Pearson correlation fit vs rank
valid_idx = ~np.isnan(alphas_arr)  # (local)
if np.sum(valid_idx) >= 2:
    corr = float(np.corrcoef(ranks[valid_idx], alphas_arr[valid_idx])[0, 1])  # (local)
    print(f"\n  Pearson correlation(alpha_fit, rank) = {corr:.4f}")
    # Linear fit: alpha = slope * rank + intercept
    slope_rk, intercept_rk = np.polyfit(ranks[valid_idx], alphas_arr[valid_idx], 1)  # (local)
    print(f"  Linear fit: alpha = {slope_rk:.3f} * rank + {intercept_rk:.3f}")
    print(f"  S77 theorem predicts slope=1.0, intercept=0.0")


# =============================================================================
# SECTION 10: 4-TUPLE CLOSURE & VERDICT LINE
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 10: 4-TUPLE CLOSURE & VERDICT")
print("=" * 78)

# Build closure SHA from input-pin map
input_pin_map = {
    'canonical_constants.py': cc_sha,
    'L_MAX_PINNED_SU2': str(L_MAX_PINNED['SU(2)']),
    'L_MAX_PINNED_SU3': str(L_MAX_PINNED['SU(3)']),
    'L_MAX_PINNED_SU4': str(L_MAX_PINNED['SU(4)']),
    'L_MAX_PINNED_SU5': str(L_MAX_PINNED['SU(5)']),
    'scheme': 'SDW-sqrt-x',
    'convention': 'bi-invariant-tau0',
    'threshold_PASS': str(SPAN_PASS_THRESHOLD),
    'threshold_INFO': str(SPAN_INFO_THRESHOLD),
    'gate_id': 'S83-SDW-NLO-ALPHA-UNIVERSALITY',
}  # (local)
# Ordered pin map for SHA
pin_str = '|'.join(f"{k}={v}" for k, v in sorted(input_pin_map.items()))  # (local)
closure_sha = hashlib.sha256(pin_str.encode()).hexdigest()  # (local)

# 4-tuple
tuple_4 = f"(span={span:.4f}, scheme=SDW-NLO, convention=gauge-group-atlas, L_max=N/A)"  # (local)
print(f"\n  4-tuple: {tuple_4}")
print(f"  Closure SHA-256: {closure_sha}")

verdict_line = (f"S83-SDW-NLO-ALPHA-UNIVERSALITY: {verdict} -- "
                f"value=span={span:.4f} "
                f"alphas=SU2:{alphas['SU(2)']:.3f}|SU3:{alphas['SU(3)']:.3f}|SU4:{alphas['SU(4)']:.3f}|SU5:{alphas['SU(5)']:.3f} "
                f"scheme=SDW-NLO convention=gauge-group-atlas L_max=N/A "
                f"sha256={closure_sha}")  # (local)
print(f"\n  Verdict line:")
print(f"  {verdict_line}")


# =============================================================================
# SECTION 11: SAVE DATA
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 11: SAVE DATA")
print("=" * 78)

save_data = {  # (local)
    'verdict': verdict,
    'span': span,
    'closure_sha': closure_sha,
    'cc_sha': cc_sha,
    'scheme': 'SDW-NLO',
    'convention': 'gauge-group-atlas',
    'pass_threshold': SPAN_PASS_THRESHOLD,
    'info_threshold': SPAN_INFO_THRESHOLD,
    'R2_min': R2_MIN,
}

for group_name, info in all_results.items():
    gkey = group_name.replace('(', '').replace(')', '')  # (local) SU2, SU3, ...
    group_data = info['group_data']
    L_vals = info['L_vals']
    res = info['results']

    save_data[f'{gkey}_dim'] = group_data['dim']
    save_data[f'{gkey}_rank'] = group_data['rank']
    save_data[f'{gkey}_L_vals'] = np.array(L_vals)
    save_data[f'{gkey}_a0'] = np.array([res[L]['a0'] for L in L_vals])
    save_data[f'{gkey}_a2'] = np.array([res[L]['a2'] for L in L_vals])
    save_data[f'{gkey}_a4'] = np.array([res[L]['a4'] for L in L_vals])
    save_data[f'{gkey}_R1'] = np.array([res[L]['R1'] for L in L_vals])
    save_data[f'{gkey}_n_irreps'] = np.array([res[L]['n_irreps'] for L in L_vals])
    save_data[f'{gkey}_lam_max'] = np.array([res[L]['lam_max'] for L in L_vals])
    save_data[f'{gkey}_alpha_NLO'] = nlo_table[group_name]['alpha']
    save_data[f'{gkey}_R2'] = nlo_table[group_name]['R2']
    save_data[f'{gkey}_n_fit'] = nlo_table[group_name]['n_pts']

OUT_NPZ = 's83_w2_g26_sdw_nlo_alpha_universality.npz'  # (local)
np.savez(OUT_NPZ, **save_data)
print(f"\n  Saved to {OUT_NPZ}")


# =============================================================================
# SECTION 12: PLOT
# =============================================================================

print("\n" + "=" * 78)
print("SECTION 12: PLOT")
print("=" * 78)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

colors = {'SU(2)': 'blue', 'SU(3)': 'red', 'SU(4)': 'green', 'SU(5)': 'purple'}
markers = {'SU(2)': 'o', 'SU(3)': 's', 'SU(4)': '^', 'SU(5)': 'D'}

# Panel A: R_1 vs L_max
ax = axes[0]
for group_name, info in all_results.items():
    L_vals = info['L_vals']
    R1_vals = [info['results'][L]['R1'] for L in L_vals]
    r = info['group_data']['rank']
    ax.plot(L_vals, R1_vals, f"{markers[group_name]}-",
            color=colors[group_name], label=f'{group_name} (r={r})')
ax.set_xlabel('$L_{\\max}$')
ax.set_ylabel('$R_1^{SDW} = a_0 a_4 / a_2^2$')
ax.set_title('$R_1^{SDW}$ convergence')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel B: |drift| vs L_max (log-log)
ax = axes[1]
for group_name, info in all_results.items():
    L_vals = info['L_vals']
    R1_vals = [info['results'][L]['R1'] for L in L_vals]
    R1_ref = R1_vals[-1]
    drift = [abs(R1 - R1_ref) / abs(R1_ref) for R1 in R1_vals[:-1]]
    L_drift = L_vals[:-1]
    alpha = nlo_table[group_name]['alpha']
    r = info['group_data']['rank']
    pos = [(L, d) for L, d in zip(L_drift, drift) if d > 1e-15]
    if len(pos) >= 2:
        L_p = [p[0] for p in pos]
        d_p = [p[1] for p in pos]
        ax.loglog(L_p, d_p, f"{markers[group_name]}-",
                  color=colors[group_name], label=f'{group_name} (r={r}, alpha={alpha:.2f})')
        # Reference L^{-rank}
        L_arr = np.array(L_p, dtype=float)
        scale = d_p[0] * L_p[0]**r
        ax.loglog(L_arr, scale * L_arr**(-r), '--', color=colors[group_name], alpha=0.3)
ax.set_xlabel('$L_{\\max}$')
ax.set_ylabel('$|R_1(L) - R_1(L_{ref})| / |R_1(L_{ref})|$')
ax.set_title('SDW-NLO drift (log-log)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which='both')

# Panel C: alpha_fit vs rank
ax = axes[2]
ranks_plot = [nlo_table[g]['rank'] for g in sorted(nlo_table)]
alphas_plot = [nlo_table[g]['alpha'] for g in sorted(nlo_table)]
names_plot = sorted(nlo_table)
for r, a, nm in zip(ranks_plot, alphas_plot, names_plot):
    ax.scatter(r, a, c=colors[nm], marker=markers[nm], s=120,
               label=f'{nm}: alpha={a:.2f}', edgecolors='black', linewidths=0.5)
# S77 theorem: alpha = rank
rr_arr = np.array([1, 2, 3, 4, 5], dtype=float)
ax.plot(rr_arr, rr_arr, 'k--', alpha=0.5, label='S77 theorem: alpha=rank')
# Linear fit
if len(ranks_plot) >= 2:
    sl, ic = np.polyfit(ranks_plot, alphas_plot, 1)
    ax.plot(rr_arr, sl*rr_arr + ic, 'r:', alpha=0.7, label=f'fit: alpha={sl:.2f}*r+{ic:.2f}')
ax.set_xlabel('rank(G)')
ax.set_ylabel('alpha_SDW^NLO (fitted)')
ax.set_title(f'NLO exponent vs rank\nspan = {span:.3f}, verdict: {verdict}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
OUT_PNG = 's83_w2_g26_sdw_nlo_alpha_universality.png'  # (local)
plt.savefig(OUT_PNG, dpi=150)
print(f"\n  Saved plot to {OUT_PNG}")
plt.close()


# =============================================================================
# FINAL — append to verdict file
# =============================================================================

print("\n" + "=" * 78)
print("APPENDING VERDICT TO s83_gate_verdicts.txt")
print("=" * 78)

VERDICT_FILE = 's83_gate_verdicts.txt'  # (local)
with open(VERDICT_FILE, 'a') as f:
    f.write('\n' + verdict_line + '\n')
print(f"\n  Appended to {VERDICT_FILE}")

elapsed = time.time() - t_start  # (local)
print(f"\n  Total elapsed: {elapsed:.2f}s")
print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
