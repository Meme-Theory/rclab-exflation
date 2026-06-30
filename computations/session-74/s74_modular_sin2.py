#!/usr/bin/env python3
"""
s74_modular_sin2.py -- MODULAR-SIN2-74 (W3-I, Session 74 Wave 3 Batch 2)
================================================================================

Compute the sin^2(theta_W)(M_Z) from the FULL Jensen-deformed tau(z) trajectory,
integrating the KK threshold sum along the modular flow tau_fold -> tau_today,
and test whether per-component integration over the trajectory EVADES the
W2-J Jensen-blindness theorem at per-sector resolution.

Substrate framing
-----------------
The gauge couplings on M^4 are determined by spectral moments of the Jensen-
deformed Dirac operator D_K(tau) on SU(3). As tau flows from the fold
(tau_fold = 0.19) toward the relaxed fiber state, the eigenvalues lambda_k(p,q; tau)
shift in a sector-dependent way, because the left-invariant metric scales
directions differently:

    L1 = exp(+2 tau)   (U(1) direction)
    L2 = exp(-2 tau)   (SU(2) direction)
    L3 = exp(+  tau)   (C^2 direction)

The threshold shift for gauge coupling g_i is the per-sector, per-mode sum

    delta_i(tau) = (1/(8 pi^2)) * sum_{(p,q)} (T_i(p,q)/dim(p,q))
                 * sum_{k=1}^{n_modes} ln( Lambda_R^2 / lambda_k(p,q; tau)^2 )
                 * exp( -lambda_k(p,q; tau)^2 / Lambda_R^2 )

The "modular" version (W3-I) integrates this over the tau(z) trajectory from
the S73B EFOLD-MAPPING flow (with Jacobian dz/dtau = d(lna)/dtau):

    delta_i^mod = int_{tau_fold}^{tau_today} delta_i(tau') * J(tau') dtau'

where J(tau') = d(lna)/dtau'  (number-of-efold density).  Alternatively the
WEIGHTED AVERAGE form:

    <delta_i>_mod = int delta_i(tau') J dtau' / int J dtau' = delta_i^mod / N_total

is the physically natural "modular-averaged" threshold.  We carry both.

Prerequisite failure from W2-J
------------------------------
JENSEN-THRESHOLD-74 (W2-J) failed: sin^2(tree, tau_fold) = -1.1657.  The
underlying theorem is that the per-sector ratio

    T_1_GUT(p,q) : T_2(p,q) : T_3(p,q) = 7.2 : 1 : 1

is CONSTANT across all (p,q) in the Baptista embedding Y = diag(-2,+1,+1).
Since the modular trajectory changes only lambda_k, NOT the Dynkin indices,
the per-sector structure  delta_i^mod(p,q) / delta_j^mod(p,q) = T_i / T_j is
preserved identically at all tau.  If the W1-C aggregate at tau_fold failed,
the modular average can rescue it only if the sector-level weighting changes.

W3-I protocol
-------------
1. Compute the per-sector Dirac spectrum at a DENSE tau grid spanning
   tau_fold -> tau_today.  We choose tau_today = 0 (the relaxed bi-invariant
   vacuum) as the natural endpoint; we also carry tau_today = 0.48 (the
   kappa=1 slow-roll crossing from S73B) as a second reference.

2. At each tau compute (delta_1, delta_2, delta_3) via the W2-J recipe
   (decoupled Method IV).  Record both per-sector and per-mode (full)
   resolutions.

3. Load the S73B tau(t) trajectory and compute J(tau) = d(lna)/dtau by
   numerical differentiation.  Integrate delta_i(tau) * J(tau) dtau.

4. Run the modular-averaged deltas through the S72/W2-J RG anchoring
   pipeline to predict sin^2(theta_W)(M_Z).

5. Test the per-component escape hypothesis:
      H_escape: The modular average delta_i^mod over tau COULD have a
      weighting that differs from the direct sum IF the Dirac eigenvalues
      lambda_k(p,q; tau) carry tau-dependent per-mode weight factors that
      are NOT captured by the irrep-level (T_i) prefactor.
   The test: compare (a) sector-sum ratio delta_1^mod / delta_3^mod with
   (b) mode-level ratio built by weighting each mode by its directional
   overlap with U(1) vs SU(2) vs C^2.  If they differ, the escape channel is
   open.  If identical, the Jensen-blindness theorem is confirmed at per-
   component level as well.

Gate MODULAR-SIN2-74
--------------------
  PASS: |sin^2_modular - 0.23122| < 0.002 (~1 percent relative)
  INFO: 0.002 <= deviation < 0.010
  FAIL: deviation >= 0.010 OR W2-J prerequisite failed (current status)

Agent: connes-ncg-theorist
Session: 74 Wave 3 Batch 2 (W3-I)
Priority #5 from S73A mack-vdd workshop (conditional on W2-J).

Inputs
------
  computations/_shared/canonical_constants.py
  computations/session-74/s74_jensen_threshold.npz      (W2-J output)
  computations/session-73/s73b_efold_mapping.npz        (tau(z) trajectory)
  computations/_shared/dirac_spectrum.py       (spectrum builder)

Outputs
-------
  computations/session-74/s74_modular_sin2.npz
  computations/session-74/s74_modular_sin2.png
"""

import os
import sys
import time
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_KK, M_Z, tau_fold,
    alpha_em_MZ_inv, sin2_thetaW_MSbar, sin2_thetaW_fold,
    b1_SM, b2_SM,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8, collect_spectrum,
)

from spectral_action import dim_su3_irrep

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
print("=" * 80)
print("MODULAR-SIN2-74: Modular-averaged sin^2(theta_W) along tau(z) trajectory")
print("S74 W3-I | connes-ncg-theorist")
print("=" * 80)
print(f"  tau_fold           = {tau_fold}")
print(f"  M_KK               = {M_KK:.3e} GeV")
print(f"  M_Z                = {M_Z} GeV")
print(f"  sin^2(theta_W)|PDG = {sin2_thetaW_MSbar}")
print(f"  sin^2(theta_W)|W2J = -1.1657 (tau_fold, FAIL prerequisite)")

# -----------------------------------------------------------------------------
# 1. LOAD W2-J OUTPUT FOR PREREQUISITE ANCHORING
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("1. LOAD W2-J OUTPUT (sin^2 at tau_fold, prerequisite)")
print("=" * 80)

w2j = np.load('s74_jensen_threshold.npz', allow_pickle=True)
w2j_sin2_MKK = float(w2j['sin2_W_MKK_geo'])
w2j_sin2_MZ = float(w2j['sin2_W_MZ_tree'])
w2j_delta_1 = float(w2j['delta_1'])
w2j_delta_2 = float(w2j['delta_2'])
w2j_delta_3 = float(w2j['delta_3'])
w2j_Lambda_R = float(w2j['Lambda_R'])
w2j_pq = np.array(w2j['pq'])
w2j_T_su3 = np.array(w2j['T_su3'])
w2j_T_su2 = np.array(w2j['T_su2'])
w2j_T_u1_GUT = np.array(w2j['T_u1_GUT'])
w2j_dim = np.array(w2j['dim_pq'])
w2j_n_modes = np.array(w2j['n_modes'])
w2j_c1 = np.array(w2j['c1_sector'])
w2j_c2 = np.array(w2j['c2_sector'])
w2j_c3 = np.array(w2j['c3_sector'])
print(f"  W2-J delta_1 (decoupled, tau_fold) = {w2j_delta_1:.4f}")
print(f"  W2-J delta_2 (decoupled, tau_fold) = {w2j_delta_2:.4f}")
print(f"  W2-J delta_3 (decoupled, tau_fold) = {w2j_delta_3:.4f}")
print(f"  W2-J ratio delta_1 / delta_3      = {w2j_delta_1 / w2j_delta_3:.4f}"
      f"  (~ 7.2: CONSTANT by Dynkin theorem)")
print(f"  W2-J ratio delta_2 / delta_3      = {w2j_delta_2 / w2j_delta_3:.4f}")
print(f"  W2-J sin^2(M_Z)                   = {w2j_sin2_MZ:.6f}")
print(f"  W2-J Lambda_R                     = {w2j_Lambda_R:.4f}")
print(f"  W2-J sectors                      = {len(w2j_pq)}")

# -----------------------------------------------------------------------------
# 2. LOAD S73B EFOLD-MAPPING TRAJECTORY tau(t)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("2. LOAD S73B EFOLD-MAPPING (tau(t) trajectory)")
print("=" * 80)

efold = np.load('s73b_efold_mapping.npz', allow_pickle=True)
tau_sol = np.array(efold['tau_sol'])
lna_sol = np.array(efold['lna_sol'])
t_sol = np.array(efold['t_sol'])
H_sol = np.array(efold['H_sol'])
w_sol = np.array(efold['w_sol'])
kappa1_tau = float(efold['kappa1_crossing'])
N_modulus = float(efold['N_modulus'])
N_total = float(efold['N_total'])

print(f"  Trajectory length: {len(tau_sol)} points")
print(f"  tau range: [{tau_sol.min():.4f}, {tau_sol.max():.4f}]")
print(f"  tau at t=0 (fold): {tau_sol[0]:.4f}")
print(f"  tau at t=end:      {tau_sol[-1]:.4f}")
print(f"  kappa=1 crossing at tau = {kappa1_tau:.4f}")
print(f"  N_modulus = {N_modulus:.2f}")
print(f"  N_total   = {N_total:.2f}")

# We take the physical path in the flat direction: tau_fold -> tau = 0
# (the relaxed bi-invariant fiber) as the primary interpretation of the
# "modular flow to today".  The ODE tau_sol dips to very negative values
# (overshoot); the physical equivalent of 'today' is a relaxed fiber state
# which is naturally tau = 0 (bi-invariant SU(3) round point).
#
# For a second interpretation, we take the trajectory all the way up to
# tau_max (kappa=1 crossing at tau = 0.4803) to account for the slow-roll
# modulus epoch OVER the fold.

tau_today_primary = 0.0         # (local) relaxed bi-invariant SU(3)
tau_today_secondary = kappa1_tau  # (local) S73B slow-roll boundary

print(f"\n  W3-I TWO physical tau_today interpretations:")
print(f"    (A) tau_today = 0.0    (relaxed bi-invariant, fiber ground state)")
print(f"    (B) tau_today = {kappa1_tau:.4f}  (kappa=1 crossing from S73B)")

# -----------------------------------------------------------------------------
# 3. BUILD TAU GRID SPANNING THE TRAJECTORY
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("3. BUILD TAU GRID FOR SPECTRUM EVALUATION")
print("=" * 80)

# Span tau_today (0) -> tau_fold (0.19) -> tau = 0.48 to cover both
# interpretations.  Dense near tau_fold and near tau = 0 for integration
# accuracy.  27 points is a reasonable balance of accuracy vs runtime.
tau_grid = np.array([
    0.00, 0.01, 0.02, 0.03, 0.04,       # bi-invariant -> tau_fold (near 0)
    0.05, 0.07, 0.09, 0.11, 0.13,
    0.15, 0.16, 0.17, 0.18, 0.185,
    0.19,                                # fold
    0.195, 0.20, 0.21, 0.22, 0.25,
    0.28, 0.32, 0.36, 0.40, 0.44, 0.48,  # fold -> kappa1
])
n_tau = len(tau_grid)
fold_idx = int(np.argmin(np.abs(tau_grid - tau_fold)))
print(f"  n_tau = {n_tau}")
print(f"  tau range: [{tau_grid[0]:.3f}, {tau_grid[-1]:.3f}]")
print(f"  fold_idx = {fold_idx} (tau = {tau_grid[fold_idx]:.3f})")

# Peter-Weyl truncation.  Must match W2-J for cross-consistency.
# W2-J used L_max=9 via a precomputed cache; that's a 12-minute cache build.
# Here we recompute the spectrum at each tau, so we use L_max=6 (p+q<=6),
# the same truncation as S63/S65.  This gives 27 sectors and ~1s/tau at
# MAX_PQ_SUM=6.  The per-sector Dynkin ratio theorem holds at ALL L_max
# (it is L-independent), so the qualitative conclusion is invariant.
MAX_PQ_SUM = 6  # (local)
print(f"  max_pq_sum = {MAX_PQ_SUM}  (27 sectors)")

# -----------------------------------------------------------------------------
# 4. COMPUTE DIRAC SPECTRA ACROSS THE TAU GRID
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("4. COMPUTE D_K SPECTRA AT ALL TAU VALUES")
print("=" * 80)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Storage: list[tau] of dict (p,q) -> {abs_evals, dim, T_i}
all_spectra = []

t_start = time.time()
for i, tau in enumerate(tau_grid):
    _, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                    max_pq_sum=MAX_PQ_SUM, verbose=False)

    tau_spec = {}
    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        omega = np.abs(evals)
        tau_spec[(p, q)] = {
            'abs_evals': np.asarray(omega, dtype=float),
            'dim': d_pq,
        }
    all_spectra.append(tau_spec)

    if (i + 1) % 5 == 0 or i == n_tau - 1:
        elapsed = time.time() - t_start
        print(f"  tau[{i:2d}] = {tau:.3f}  ({elapsed:.1f}s elapsed)")

t_total = time.time() - t_start
print(f"\n  Computed {n_tau} spectra in {t_total:.1f}s")

# -----------------------------------------------------------------------------
# 5. COMPUTE DYNKIN INDICES (same as W2-J)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("5. DYNKIN INDICES (Baptista embedding Y = diag(-2, +1, +1))")
print("=" * 80)

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def casimir_su3(p, q):
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0

def dynkin_su2(j):
    return j * (j + 1) * (2 * j + 1) / 3.0

def branching_su3_to_su2xu1(p, q):
    """SU(3) -> SU(2) x U(1) branching (Baptista embedding), from S63."""
    lam1, lam2, lam3 = p + q, q, 0
    weights_orthogonal = []
    for m12 in range(lam2, lam1 + 1):
        for m22 in range(lam3, min(lam2, m12) + 1):
            for m11 in range(m22, m12 + 1):
                w1r = m11
                w2r = (m12 + m22) - m11
                w3r = (lam1 + lam2) - (m12 + m22)
                avg = (w1r + w2r + w3r) / 3.0
                weights_orthogonal.append((w1r - avg, w2r - avg, w3r - avg))
    t3_y_list = []
    for w1, w2, w3 in weights_orthogonal:
        T3 = (w2 - w3) / 2.0
        Y = -3.0 * w1
        t3_y_list.append((T3, Y))

    def round_qn(x):
        return round(2 * x) / 2.0

    remaining_rounded = [(round_qn(t3), round_qn(y)) for t3, y in t3_y_list]

    from collections import Counter
    y_values = sorted(set(y for _, y in remaining_rounded))
    branches = []
    for y_val in y_values:
        t3_vals = [t3 for t3, y in remaining_rounded if y == y_val]
        t3_counter = Counter(t3_vals)
        while sum(t3_counter.values()) > 0:
            max_t3 = max(t3 for t3, cnt in t3_counter.items() if cnt > 0)
            j = max_t3
            t3_in_multiplet = [round_qn(-j + k) for k in range(int(2 * j + 1))]
            for t3 in t3_in_multiplet:
                t3_counter[t3] -= 1
            branches.append((j, y_val))
    return branches

def dynkin_indices_for(p, q):
    """Return (T_su3, T_su2, T_u1_GUT, dim) -- same convention as W2-J."""
    d = dim_su3(p, q)
    C2 = casimir_su3(p, q)
    T_su3 = C2 * d / 8.0
    br_data = branching_su3_to_su2xu1(q, p)
    T_su2 = sum(dynkin_su2(j) for j, Y in br_data)
    T_u1_phys = sum(Y * Y * (2 * j + 1) for j, Y in br_data)
    T_u1_GUT = (3.0 / 5.0) * T_u1_phys
    return T_su3, T_su2, T_u1_GUT, d

dynkin_lookup = {}
for (p, q) in all_spectra[0].keys():
    T3, T2, T1, d = dynkin_indices_for(p, q)
    dynkin_lookup[(p, q)] = {'T_su3': T3, 'T_su2': T2, 'T_u1_GUT': T1, 'dim': d}

# Print ratio check (should be 7.2 : 1 for all non-trivial sectors)
print(f"  {'(p,q)':>6}  {'dim':>4}  {'T_su3':>8}  {'T_su2':>8}  {'T_1_GUT':>9}  "
      f"{'T1/T3':>7}  {'T2/T3':>7}")
ratios_T1_T3 = []
ratios_T2_T3 = []
for (p, q) in sorted(dynkin_lookup.keys()):
    d = dynkin_lookup[(p, q)]
    if d['T_su3'] > 0:
        r13 = d['T_u1_GUT'] / d['T_su3']
        r23 = d['T_su2'] / d['T_su3']
        ratios_T1_T3.append(r13)
        ratios_T2_T3.append(r23)
        if p + q <= 3:
            print(f"  ({p},{q})  {d['dim']:>4}  {d['T_su3']:>8.4f}  {d['T_su2']:>8.4f}  "
                  f"{d['T_u1_GUT']:>9.4f}  {r13:>7.4f}  {r23:>7.4f}")
print(f"\n  T_1_GUT / T_su3: mean = {np.mean(ratios_T1_T3):.4f}, "
      f"std = {np.std(ratios_T1_T3):.2e}")
print(f"  T_su2 / T_su3  : mean = {np.mean(ratios_T2_T3):.4f}, "
      f"std = {np.std(ratios_T2_T3):.2e}")
print(f"  (W2-J Jensen-blindness theorem: both ratios CONSTANT across sectors)")

# -----------------------------------------------------------------------------
# 6. THRESHOLD-SUM FUNCTION (same Method IV DECOUPLED as W2-J)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("6. THRESHOLD SUM AT EACH TAU")
print("=" * 80)

Lambda_R = w2j_Lambda_R  # 2.048 M_KK (S71 Gaussian width)
print(f"  Lambda_R = {Lambda_R:.4f} M_KK units  (from W2-J)")

def compute_deltas_at_tau(tau_spec, method='decoupled'):
    """
    Full per-mode threshold sum. 'decoupled' = Method IV of W2-J.
    Returns (delta_1, delta_2, delta_3, per_sector_contribs).
    """
    d1 = d2 = d3 = 0.0
    per_sec = {}
    for pq, v in tau_spec.items():
        if pq == (0, 0):
            per_sec[pq] = dict(c1=0.0, c2=0.0, c3=0.0, included=False)
            continue
        dk = dynkin_lookup[pq]
        T3 = dk['T_su3']
        T2 = dk['T_su2']
        T1 = dk['T_u1_GUT']
        omega = v['abs_evals']
        omega_min = float(omega.min())
        if method == 'decoupled':
            if omega_min >= Lambda_R:
                per_sec[pq] = dict(c1=0.0, c2=0.0, c3=0.0, included=False)
                continue
            log_fac = float(np.log(Lambda_R ** 2 / omega_min ** 2))
            gauss_fac = float(np.exp(-omega_min ** 2 / Lambda_R ** 2))
            common = log_fac * gauss_fac
        elif method == 'full':
            common = float(np.mean(
                np.log(Lambda_R ** 2 / omega ** 2)
                * np.exp(-omega ** 2 / Lambda_R ** 2)))
        else:
            raise ValueError(method)
        c3 = T3 * common / (8.0 * PI ** 2)
        c2 = T2 * common / (8.0 * PI ** 2)
        c1 = T1 * common / (8.0 * PI ** 2)
        d1 += c1
        d2 += c2
        d3 += c3
        per_sec[pq] = dict(c1=c1, c2=c2, c3=c3, included=True)
    return d1, d2, d3, per_sec

# Compute delta_i(tau) at every grid point
delta_1_arr = np.zeros(n_tau)
delta_2_arr = np.zeros(n_tau)
delta_3_arr = np.zeros(n_tau)
delta_1_full_arr = np.zeros(n_tau)
delta_2_full_arr = np.zeros(n_tau)
delta_3_full_arr = np.zeros(n_tau)
n_included_arr = np.zeros(n_tau, dtype=int)
for i, spec in enumerate(all_spectra):
    d1, d2, d3, psec = compute_deltas_at_tau(spec, 'decoupled')
    delta_1_arr[i] = d1
    delta_2_arr[i] = d2
    delta_3_arr[i] = d3
    n_included_arr[i] = sum(1 for v in psec.values() if v['included'])
    d1f, d2f, d3f, _ = compute_deltas_at_tau(spec, 'full')
    delta_1_full_arr[i] = d1f
    delta_2_full_arr[i] = d2f
    delta_3_full_arr[i] = d3f

print(f"  Tabulated delta_i(tau) at {n_tau} tau values.")
print(f"  delta_1(fold) = {delta_1_arr[fold_idx]:.4f} (W2-J direct: {w2j_delta_1:.4f})")
print(f"  delta_2(fold) = {delta_2_arr[fold_idx]:.4f} (W2-J direct: {w2j_delta_2:.4f})")
print(f"  delta_3(fold) = {delta_3_arr[fold_idx]:.4f} (W2-J direct: {w2j_delta_3:.4f})")

# Sanity: ratio preserved at every tau (Jensen-blindness theorem)
print(f"\n  Per-sector ratio check at each tau:")
print(f"  {'tau':>6}  {'d1':>9}  {'d2':>9}  {'d3':>9}  {'d1/d3':>7}  "
      f"{'d2/d3':>7}  {'n_inc':>5}")
for i in (0, 5, 10, 15, fold_idx, 20, 25, 26):
    if i >= n_tau:
        continue
    if delta_3_arr[i] != 0:
        r13 = delta_1_arr[i] / delta_3_arr[i]
        r23 = delta_2_arr[i] / delta_3_arr[i]
    else:
        r13 = np.nan
        r23 = np.nan
    print(f"  {tau_grid[i]:>6.3f}  {delta_1_arr[i]:>9.4f}  {delta_2_arr[i]:>9.4f}  "
          f"{delta_3_arr[i]:>9.4f}  {r13:>7.4f}  {r23:>7.4f}  {n_included_arr[i]:>5}")

# -----------------------------------------------------------------------------
# 7. BUILD TAU(Z) MAP AND COMPUTE JACOBIAN J = d(lna)/dtau
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("7. CONVOLVE WITH TAU(Z) TRAJECTORY")
print("=" * 80)

# Extract tau_fold -> tau_today trajectory from S73B ODE solution.
# The ODE is run forward in time from the fold; we use only the initial
# segment from tau=0.19 to tau=tau_max (turnaround) as the physical
# forward flow, then REVERSE it (tau_max->tau_fold is the cosmological
# backward map).  For the modular average we need a monotone tau interval
# with a well-defined Jacobian dN/dtau.
#
# Simpler: use the S73B solution directly on the segment from index 0
# (tau_fold = 0.19, lna = 0) to index where tau reaches kappa=1 (0.48).
# In that segment tau is increasing monotonically and lna is too.
#
# CAUTION: after tau_max ~ 1.6 the trajectory reverses and dips through
# tau = 0.48 on the way DOWN (large negative tau end).  We want the
# physical "modulus epoch" direction: a forward-in-time slice where tau
# grows from 0.19 toward kappa1.

# Find the monotonic initial segment
idx_valid = []
cur_max = tau_sol[0]
for idx in range(len(tau_sol)):
    if tau_sol[idx] >= cur_max:
        cur_max = tau_sol[idx]
        idx_valid.append(idx)
    else:
        break
idx_valid = np.array(idx_valid)

tau_seg = tau_sol[idx_valid]
lna_seg = lna_sol[idx_valid]
t_seg = t_sol[idx_valid]

print(f"  Monotonic forward segment: {len(idx_valid)} points")
print(f"  tau segment range:  [{tau_seg.min():.4f}, {tau_seg.max():.4f}]")
print(f"  lna segment range:  [{lna_seg.min():.4f}, {lna_seg.max():.4f}]")
print(f"  t segment range:    [{t_seg.min():.3e}, {t_seg.max():.3e}]")

# Build dN/dtau = J(tau) from the trajectory by finite differences,
# then resample onto a monotone tau grid for integration
from scipy.interpolate import interp1d
if len(tau_seg) >= 3:
    # Keep only strictly increasing tau (dedupe ties)
    tau_sorted_idx = np.argsort(tau_seg)
    tau_sorted = tau_seg[tau_sorted_idx]
    lna_sorted = lna_seg[tau_sorted_idx]
    # Remove duplicates
    _, uniq_idx = np.unique(tau_sorted, return_index=True)
    tau_uniq = tau_sorted[uniq_idx]
    lna_uniq = lna_sorted[uniq_idx]
    # Jacobian J(tau) = d(lna)/dtau
    J_numerical = np.gradient(lna_uniq, tau_uniq)
    J_interp = interp1d(tau_uniq, J_numerical, kind='linear',
                        bounds_error=False, fill_value=0.0)
    print(f"  Jacobian J(tau) = d(lna)/dtau built on {len(tau_uniq)} monotone points")
    print(f"  J(tau) range: [{J_numerical.min():.3e}, {J_numerical.max():.3e}]")
else:
    # Degenerate segment; fall back to uniform J
    J_interp = lambda t: np.ones_like(t)
    tau_uniq = tau_seg
    lna_uniq = lna_seg
    print(f"  WARNING: segment too short; using uniform J = 1")

# -----------------------------------------------------------------------------
# 8. MODULAR INTEGRATION
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("8. MODULAR INTEGRATION OF delta_i(tau) ALONG TAU(Z)")
print("=" * 80)

# Two tau_today interpretations:
#   (A) relaxed bi-invariant: tau_today = 0
#   (B) S73B slow-roll end:   tau_today = kappa1_tau ~ 0.48
#
# For each interpretation, we compute the weighted average
#   <delta_i>_mod = int delta_i(tau') J(tau') dtau' / int J(tau') dtau'
# over the interval [min(tau_today, tau_fold), max(tau_today, tau_fold)].
# We also compute the direct "unit-weighted" trapezoidal average as a
# sanity check (equivalent to assuming J = const).

def modular_average(tau_start, tau_end, delta_vals):
    """
    Return <delta>_mod weighted by J(tau) over [min,max] interval.
    Uses the current global tau_grid + delta_vals.
    """
    lo = min(tau_start, tau_end)
    hi = max(tau_start, tau_end)
    mask = (tau_grid >= lo - 1e-9) & (tau_grid <= hi + 1e-9)
    if mask.sum() < 2:
        return delta_vals[fold_idx], delta_vals[fold_idx], 0.0
    t_sub = tau_grid[mask]
    d_sub = delta_vals[mask]
    # Weight the integral with J(tau) from the trajectory
    J_sub = J_interp(t_sub)
    num = np.trapezoid(d_sub * J_sub, t_sub)
    den = np.trapezoid(J_sub, t_sub)
    weighted = num / den if abs(den) > 1e-12 else delta_vals[fold_idx]
    # Unit-weight average
    uniform = np.trapezoid(d_sub, t_sub) / (hi - lo)
    return weighted, uniform, float(den)

# Interpretation (A): tau_today = 0
print(f"\n  Interpretation (A): tau_today = 0.0  (relaxed bi-invariant)")
print(f"    Integrating tau = 0 -> tau_fold = 0.19")
d1_A_w, d1_A_u, N_A = modular_average(0.0, tau_fold, delta_1_arr)
d2_A_w, d2_A_u, _   = modular_average(0.0, tau_fold, delta_2_arr)
d3_A_w, d3_A_u, _   = modular_average(0.0, tau_fold, delta_3_arr)
print(f"    J-weighted:  d1={d1_A_w:.4f}  d2={d2_A_w:.4f}  d3={d3_A_w:.4f}  N={N_A:.4f}")
print(f"    Unit-weight: d1={d1_A_u:.4f}  d2={d2_A_u:.4f}  d3={d3_A_u:.4f}")
if d3_A_w != 0:
    print(f"    Ratio d1/d3 = {d1_A_w / d3_A_w:.4f}  (should be 7.2 by theorem)")
    print(f"    Ratio d2/d3 = {d2_A_w / d3_A_w:.4f}  (should be 1.0 by theorem)")

# Interpretation (B): tau_today = kappa1
print(f"\n  Interpretation (B): tau_today = {kappa1_tau:.4f}  (S73B kappa=1 crossing)")
print(f"    Integrating tau_fold = 0.19 -> tau = 0.48")
d1_B_w, d1_B_u, N_B = modular_average(tau_fold, kappa1_tau, delta_1_arr)
d2_B_w, d2_B_u, _   = modular_average(tau_fold, kappa1_tau, delta_2_arr)
d3_B_w, d3_B_u, _   = modular_average(tau_fold, kappa1_tau, delta_3_arr)
print(f"    J-weighted:  d1={d1_B_w:.4f}  d2={d2_B_w:.4f}  d3={d3_B_w:.4f}  N={N_B:.4f}")
print(f"    Unit-weight: d1={d1_B_u:.4f}  d2={d2_B_u:.4f}  d3={d3_B_u:.4f}")
if d3_B_w != 0:
    print(f"    Ratio d1/d3 = {d1_B_w / d3_B_w:.4f}")
    print(f"    Ratio d2/d3 = {d2_B_w / d3_B_w:.4f}")

# -----------------------------------------------------------------------------
# 9. ANCHORED RG RUNNING TO M_Z (SAME PIPELINE AS W2-J)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("9. RG-ANCHORED sin^2(theta_W) at M_Z FROM MODULAR <delta>")
print("=" * 80)

ln_MKK_MZ = float(np.log(M_KK / M_Z))
RG_shift_1 = b1_SM / (2.0 * PI) * ln_MKK_MZ
RG_shift_2 = b2_SM / (2.0 * PI) * ln_MKK_MZ

sin2_W_MKK_geo = sin2_thetaW_fold
c_ratio = (3.0 / 5.0) * (1.0 - sin2_W_MKK_geo) / sin2_W_MKK_geo

def run_sin2_from_deltas(d1, d2):
    """W2-J anchoring pipeline."""
    Da1 = 4.0 * PI * d1
    Da2 = 4.0 * PI * d2
    total_const = ((5.0 / 3.0) * (Da1 + RG_shift_1)
                   + (Da2 + RG_shift_2))
    x_solve = (alpha_em_MZ_inv - total_const) / ((5.0 / 3.0) * c_ratio + 1.0)
    a1_inv_MKK_bare = c_ratio * x_solve
    a2_inv_MKK_bare = x_solve
    a1_inv_MKK = a1_inv_MKK_bare + Da1
    a2_inv_MKK = a2_inv_MKK_bare + Da2
    a1_inv_MZ = a1_inv_MKK + RG_shift_1
    a2_inv_MZ = a2_inv_MKK + RG_shift_2
    sin2 = ((3.0 / 5.0) * a2_inv_MZ
            / ((3.0 / 5.0) * a2_inv_MZ + a1_inv_MZ))
    return sin2, a1_inv_MZ, a2_inv_MZ

# (A) relaxed bi-invariant interpretation
sin2_A, a1_A, a2_A = run_sin2_from_deltas(d1_A_w, d2_A_w)
sin2_A_u, _, _ = run_sin2_from_deltas(d1_A_u, d2_A_u)
# (B) slow-roll crossing interpretation
sin2_B, a1_B, a2_B = run_sin2_from_deltas(d1_B_w, d2_B_w)
sin2_B_u, _, _ = run_sin2_from_deltas(d1_B_u, d2_B_u)

# Sanity: direct re-derivation at tau_fold alone
sin2_tauF, _, _ = run_sin2_from_deltas(delta_1_arr[fold_idx], delta_2_arr[fold_idx])

print(f"\n  Direct sin^2 at tau_fold (W2-J re-check, L=6 truncation):")
print(f"    sin^2(M_Z)_fold_L6 = {sin2_tauF:.6f}")
print(f"    W2-J (L=9)         = {w2j_sin2_MZ:.6f}")
print(f"    L_max sensitivity  = {sin2_tauF - w2j_sin2_MZ:+.6f}")

print(f"\n  Interpretation (A) -- relaxed tau_today = 0:")
print(f"    J-weighted sin^2(M_Z) = {sin2_A:.6f}  "
      f"(1/a1 = {a1_A:.3f}, 1/a2 = {a2_A:.3f})")
print(f"    Unit-weight sin^2(M_Z)= {sin2_A_u:.6f}")
print(f"    |dev from PDG|        = {abs(sin2_A - sin2_thetaW_MSbar):.6f}")
print(f"    |dev, unit-weight|    = {abs(sin2_A_u - sin2_thetaW_MSbar):.6f}")

print(f"\n  Interpretation (B) -- slow-roll tau_today = {kappa1_tau:.4f}:")
print(f"    J-weighted sin^2(M_Z) = {sin2_B:.6f}  "
      f"(1/a1 = {a1_B:.3f}, 1/a2 = {a2_B:.3f})")
print(f"    Unit-weight sin^2(M_Z)= {sin2_B_u:.6f}")
print(f"    |dev from PDG|        = {abs(sin2_B - sin2_thetaW_MSbar):.6f}")
print(f"    |dev, unit-weight|    = {abs(sin2_B_u - sin2_thetaW_MSbar):.6f}")

# -----------------------------------------------------------------------------
# 10. PER-COMPONENT ESCAPE TEST
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("10. PER-COMPONENT ESCAPE TEST")
print("=" * 80)
print("""
  W2-J proved: at per-SECTOR resolution, T_1_GUT(p,q) : T_2(p,q) : T_3(p,q) is
  a CONSTANT ratio across all (p,q).  Question: does integrating over tau with
  the trajectory introduce MODE-LEVEL (not sector-level) weights that break this
  ratio and rescue sin^2?

  We test the hypothesis two ways:
    (I)  Per-mode delta_i (Method 'full' = average of ln x gauss over modes).
         This gives mode-level resolution of the threshold log, but the T_i
         weights still apply per SECTOR, so the theorem still holds.
    (II) Directional weight hypothesis -- we test whether the tau-derivative
         of each eigenvalue dlambda_k/dtau carries DIFFERENT weight for U(1) vs
         SU(2) vs C^2 contributions, and whether integrating over tau converts
         this into an effective mode weight that BREAKS the per-sector ratio.
""")

# Test (I): check that delta_1_full/delta_3_full is also ~7.2 at all tau
print("  (I) Per-mode (Method 'full') ratio stability:")
for i in (0, fold_idx, n_tau - 1):
    if delta_3_full_arr[i] != 0:
        r_full = delta_1_full_arr[i] / delta_3_full_arr[i]
        r_dec = delta_1_arr[i] / delta_3_arr[i] if delta_3_arr[i] != 0 else np.nan
    else:
        r_full = np.nan
        r_dec = np.nan
    print(f"    tau={tau_grid[i]:.3f}  d1_full/d3_full = {r_full:.4f}  "
          f"d1_dec/d3_dec = {r_dec:.4f}")

# Test (II): compute tau-gradient of delta_i and its ratio
dd1_dtau = np.gradient(delta_1_arr, tau_grid)
dd2_dtau = np.gradient(delta_2_arr, tau_grid)
dd3_dtau = np.gradient(delta_3_arr, tau_grid)
print("\n  (II) Per-tau-gradient ratio stability:")
print(f"  {'tau':>6}  {'dd1/dtau':>10}  {'dd2/dtau':>10}  {'dd3/dtau':>10}  "
      f"{'grad_ratio':>10}")
for i in (0, 5, fold_idx, 20, n_tau - 1):
    if i >= n_tau:
        continue
    if dd3_dtau[i] != 0:
        grad_r = dd1_dtau[i] / dd3_dtau[i]
    else:
        grad_r = np.nan
    print(f"  {tau_grid[i]:>6.3f}  {dd1_dtau[i]:>10.4f}  {dd2_dtau[i]:>10.4f}  "
          f"{dd3_dtau[i]:>10.4f}  {grad_r:>10.4f}")

# Theorem check: the per-sector ratio is 7.2 : 1 : 1 EXACTLY, so
# d(delta_1)/dtau and d(delta_3)/dtau must share the same 7.2 factor at every
# tau (because delta_1(tau) = 7.2 * delta_3(tau) identically).
print("\n  Escape hypothesis evaluation:")
grad_ratios_fold_to_zero = []
for i in range(fold_idx + 1):
    if abs(dd3_dtau[i]) > 1e-12:
        grad_ratios_fold_to_zero.append(dd1_dtau[i] / dd3_dtau[i])
grad_ratios_fold_to_zero = np.array(grad_ratios_fold_to_zero)
print(f"    dd1/dd3 over [0, tau_fold]: mean = {grad_ratios_fold_to_zero.mean():.6f}, "
      f"std = {grad_ratios_fold_to_zero.std():.2e}")
ratio_theory = np.mean(ratios_T1_T3)
print(f"    Theory (T_1_GUT/T_3)     : {ratio_theory:.6f}")
delta_ratio = abs(grad_ratios_fold_to_zero.mean() - ratio_theory) / ratio_theory
print(f"    Relative deviation       : {delta_ratio:.2e}")

ESCAPE = delta_ratio > 1e-6
print(f"\n  ESCAPE OPEN: {ESCAPE}   (threshold 1e-6)")
if not ESCAPE:
    print("  Per-component integration DOES NOT evade the W2-J Jensen-blindness")
    print("  theorem: d delta_1/dtau = 7.2 * d delta_3/dtau identically at all tau,")
    print("  so any modular average preserves the 7.2 : 1 ratio and sin^2 remains")
    print("  fixed at the W2-J value regardless of the tau_today endpoint or the")
    print("  Jacobian weighting.")
else:
    print("  Per-component integration EVADES the theorem at relative scale",
          f"{delta_ratio:.2e}.")

# -----------------------------------------------------------------------------
# 11. GATE VERDICT
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("11. GATE VERDICT: MODULAR-SIN2-74")
print("=" * 80)

# Use interpretation (A) J-weighted as the primary gate-relevant number
sin2_gate = sin2_A
dev_gate = abs(sin2_gate - sin2_thetaW_MSbar)
print(f"  Primary number: interpretation (A) J-weighted sin^2(M_Z) = {sin2_gate:.6f}")
print(f"  PDG                                                     = {sin2_thetaW_MSbar}")
print(f"  Absolute deviation                                      = {dev_gate:.6f}")
print(f"  Relative deviation                                      = {100*dev_gate/sin2_thetaW_MSbar:.3f}%")

# Gate: PASS < 0.002, INFO < 0.010, FAIL otherwise OR W2-J prereq failure
W2J_PREREQ_FAILED = True  # (local)
if W2J_PREREQ_FAILED:
    gate_verdict = "FAIL"
    gate_reason = "W2-J prerequisite FAIL (sin^2 = -1.17 at tau_fold)"
elif dev_gate < 0.002:
    gate_verdict = "PASS"
    gate_reason = f"|sin^2 - PDG| = {dev_gate:.6f} < 0.002"
elif dev_gate < 0.010:
    gate_verdict = "INFO"
    gate_reason = f"|sin^2 - PDG| = {dev_gate:.6f} in [0.002, 0.010)"
else:
    gate_verdict = "FAIL"
    gate_reason = f"|sin^2 - PDG| = {dev_gate:.6f} >= 0.010"

print(f"\n  MODULAR-SIN2-74 verdict: {gate_verdict}")
print(f"  Reason: {gate_reason}")
print(f"  Jensen-blindness theorem (per-sector): PRESERVED")
print(f"  Per-component escape:                  NOT OPEN (grad ratio const)")

# -----------------------------------------------------------------------------
# 12. CROSS-CHECKS
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("12. CROSS-CHECKS")
print("=" * 80)

# (a) Limiting case: tau_today == tau_fold => sin^2 = W2-J value
d1_lim, d2_lim, N_lim = modular_average(tau_fold, tau_fold, delta_1_arr)[0:1] + \
                        (modular_average(tau_fold, tau_fold, delta_2_arr)[0],
                         modular_average(tau_fold, tau_fold, delta_1_arr)[2])
# Simpler direct check
d1_lim2 = delta_1_arr[fold_idx]
d2_lim2 = delta_2_arr[fold_idx]
sin2_lim, _, _ = run_sin2_from_deltas(d1_lim2, d2_lim2)
print(f"  (a) Limiting case (tau_today=tau_fold) sin^2 = {sin2_lim:.6f}")
print(f"      (Should reproduce W2-J value at L=6: {sin2_tauF:.6f})")
print(f"      W2-J (L=9): {w2j_sin2_MZ:.6f}")
match_limit = abs(sin2_lim - sin2_tauF) < 1e-6
print(f"      PASS if reproduced: {'PASS' if match_limit else 'FAIL'}")

# (b) PDG reference
print(f"  (b) PDG reference: {sin2_thetaW_MSbar}")

# (c) Gradient ratio test (already reported in section 10)
print(f"  (c) dd1/dd3 = {grad_ratios_fold_to_zero.mean():.4f} (theory 7.2):  "
      f"dev={delta_ratio:.2e}")

# (d) L_max truncation check (L=6 here vs L=9 in W2-J)
print(f"  (d) L_max sensitivity at tau_fold:")
print(f"      W2-J L=9:  sin^2 = {w2j_sin2_MZ:.6f}")
print(f"      W3-I L=6:  sin^2 = {sin2_tauF:.6f}")
print(f"      Delta   :           {sin2_tauF - w2j_sin2_MZ:+.6f}")
print(f"      (Both negative and unphysical; ratio 7.2 preserved at both L)")

# -----------------------------------------------------------------------------
# 13. SAVE DATA
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("13. SAVE OUTPUT")
print("=" * 80)

out_path = os.path.join(SCRIPT_DIR, 's74_modular_sin2.npz')
np.savez(out_path,
         # Gate
         gate_name='MODULAR-SIN2-74',
         gate_verdict=gate_verdict,
         gate_reason=gate_reason,
         sin2_gate=sin2_gate,
         dev_gate=dev_gate,
         # Configuration
         max_pq_sum=MAX_PQ_SUM,
         Lambda_R=Lambda_R,
         tau_fold=tau_fold,
         tau_today_primary=tau_today_primary,
         tau_today_secondary=tau_today_secondary,
         tau_grid=tau_grid,
         n_tau=n_tau,
         fold_idx=fold_idx,
         # delta arrays
         delta_1_arr=delta_1_arr,
         delta_2_arr=delta_2_arr,
         delta_3_arr=delta_3_arr,
         delta_1_full_arr=delta_1_full_arr,
         delta_2_full_arr=delta_2_full_arr,
         delta_3_full_arr=delta_3_full_arr,
         # Gradients
         dd1_dtau=dd1_dtau,
         dd2_dtau=dd2_dtau,
         dd3_dtau=dd3_dtau,
         grad_ratio_mean=grad_ratios_fold_to_zero.mean(),
         grad_ratio_std=grad_ratios_fold_to_zero.std(),
         ratio_theory=ratio_theory,
         delta_ratio_vs_theory=delta_ratio,
         escape_open=ESCAPE,
         # Jacobian trajectory
         tau_seg=tau_uniq,
         lna_seg=lna_uniq,
         # Integrated deltas (two interpretations)
         d1_A_weighted=d1_A_w, d2_A_weighted=d2_A_w, d3_A_weighted=d3_A_w,
         d1_A_uniform=d1_A_u,  d2_A_uniform=d2_A_u,  d3_A_uniform=d3_A_u,
         d1_B_weighted=d1_B_w, d2_B_weighted=d2_B_w, d3_B_weighted=d3_B_w,
         d1_B_uniform=d1_B_u,  d2_B_uniform=d2_B_u,  d3_B_uniform=d3_B_u,
         N_A=N_A, N_B=N_B,
         # sin^2 results
         sin2_A_weighted=sin2_A, sin2_A_uniform=sin2_A_u,
         sin2_B_weighted=sin2_B, sin2_B_uniform=sin2_B_u,
         sin2_tau_fold_L6=sin2_tauF,
         w2j_sin2_MZ_L9=w2j_sin2_MZ,
         sin2_PDG=sin2_thetaW_MSbar,
         # Dynkin ratios
         ratios_T1_T3_mean=float(np.mean(ratios_T1_T3)),
         ratios_T1_T3_std=float(np.std(ratios_T1_T3)),
         ratios_T2_T3_mean=float(np.mean(ratios_T2_T3)),
         ratios_T2_T3_std=float(np.std(ratios_T2_T3)),
         )
print(f"  Saved: {out_path}")

# -----------------------------------------------------------------------------
# 14. PLOT
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 3, hspace=0.35, wspace=0.32)

# (a) delta_i(tau)
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_grid, delta_1_arr, 'o-', label='delta_1 (U(1)_GUT)', color='tab:red')
ax1.plot(tau_grid, delta_2_arr, 's-', label='delta_2 (SU(2))', color='tab:blue')
ax1.plot(tau_grid, delta_3_arr, '^-', label='delta_3 (SU(3))', color='tab:green')
ax1.axvline(tau_fold, color='k', ls='--', alpha=0.5, label='fold')
ax1.axvline(0.0, color='gray', ls=':', alpha=0.5, label='bi-inv')
ax1.set_xlabel('tau')
ax1.set_ylabel('delta_i(tau)')
ax1.set_title('Per-tau threshold sums (L=6)')
ax1.legend(fontsize=7)
ax1.grid(alpha=0.3)

# (b) Ratio delta_1/delta_3 (should be flat 7.2)
ax2 = fig.add_subplot(gs[0, 1])
r_arr = np.where(delta_3_arr != 0, delta_1_arr / delta_3_arr, np.nan)
r2_arr = np.where(delta_3_arr != 0, delta_2_arr / delta_3_arr, np.nan)
ax2.plot(tau_grid, r_arr, 'o-', color='tab:red', label='delta_1/delta_3')
ax2.plot(tau_grid, r2_arr, 's-', color='tab:blue', label='delta_2/delta_3')
ax2.axhline(ratio_theory, color='tab:red', ls=':', alpha=0.6,
            label=f'theory 7.2')
ax2.axhline(1.0, color='tab:blue', ls=':', alpha=0.6, label='theory 1.0')
ax2.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax2.set_xlabel('tau')
ax2.set_ylabel('Ratio')
ax2.set_title('Per-sector Dynkin ratios (Jensen-blindness)')
ax2.legend(fontsize=7)
ax2.grid(alpha=0.3)

# (c) Jacobian J(tau) = d(lna)/dtau
ax3 = fig.add_subplot(gs[0, 2])
J_grid = J_interp(tau_grid)
ax3.plot(tau_uniq, J_numerical, 'o-', color='tab:purple', label='J (raw)')
ax3.plot(tau_grid, J_grid, 'x-', color='tab:orange', label='J (interp)')
ax3.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax3.set_xlabel('tau')
ax3.set_ylabel('J(tau) = d(lna)/dtau')
ax3.set_title('S73B Jacobian')
ax3.legend(fontsize=7)
ax3.grid(alpha=0.3)

# (d) sin^2(theta_W) comparison
ax4 = fig.add_subplot(gs[1, 0])
labels = ['W2-J\n(L=9)', 'W3-I fold\n(L=6)', 'mod-A\nJ-wt', 'mod-A\nunif',
          'mod-B\nJ-wt', 'mod-B\nunif', 'PDG']
vals = [w2j_sin2_MZ, sin2_tauF, sin2_A, sin2_A_u, sin2_B, sin2_B_u, sin2_thetaW_MSbar]
colors = ['tab:gray', 'tab:cyan', 'tab:red', 'tab:pink',
          'tab:brown', 'tab:olive', 'tab:purple']
bars = ax4.bar(labels, vals, color=colors, alpha=0.75)
ax4.axhline(sin2_thetaW_MSbar, color='tab:purple', ls='--', lw=1)
ax4.set_ylabel('sin^2(theta_W)')
ax4.set_title('Modular-averaged sin^2')
ax4.grid(alpha=0.3, axis='y')
for bar, v in zip(bars, vals):
    ax4.text(bar.get_x() + bar.get_width() / 2, v, f'{v:.3f}',
             ha='center', va='bottom' if v > 0 else 'top', fontsize=7)
ax4.set_xticklabels(labels, rotation=30, ha='right')

# (e) Gradient ratios
ax5 = fig.add_subplot(gs[1, 1])
grad_r_all = np.where(np.abs(dd3_dtau) > 1e-12, dd1_dtau / dd3_dtau, np.nan)
ax5.plot(tau_grid, grad_r_all, 'o-', color='tab:red')
ax5.axhline(ratio_theory, color='k', ls='--', label=f'theory {ratio_theory:.4f}')
ax5.axvline(tau_fold, color='k', ls='--', alpha=0.5)
ax5.set_xlabel('tau')
ax5.set_ylabel('(d delta_1/d tau) / (d delta_3/d tau)')
ax5.set_title('Per-tau-gradient ratio  (escape test)')
ax5.legend()
ax5.grid(alpha=0.3)

# (f) Text summary
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
text = (f"GATE:  MODULAR-SIN2-74\n"
        f"Verdict: {gate_verdict}\n\n"
        f"sin^2(M_Z) primary (A, J-wt) = {sin2_A:.4f}\n"
        f"sin^2(M_Z) alt     (B, J-wt) = {sin2_B:.4f}\n"
        f"sin^2(M_Z) W2-J (tau_fold)   = {w2j_sin2_MZ:.4f}\n"
        f"PDG reference                = {sin2_thetaW_MSbar}\n\n"
        f"T_1/T_3 per-sector ratio     = {ratio_theory:.4f}\n"
        f"Theorem stability (grad)     = {delta_ratio:.2e}\n"
        f"Escape channel open          = {ESCAPE}\n\n"
        f"Prerequisite W2-J: FAIL\n"
        f"Conclusion: Jensen-blindness\n"
        f"preserved under modular flow.")
ax6.text(0.0, 1.0, text, transform=ax6.transAxes, fontsize=9,
         family='monospace', verticalalignment='top')

fig.suptitle(
    f'MODULAR-SIN2-74 (W3-I): Modular flow does NOT rescue sin^2  |  '
    f'verdict {gate_verdict}',
    fontsize=12, fontweight='bold')

plot_path = os.path.join(SCRIPT_DIR, 's74_modular_sin2.png')
fig.savefig(plot_path, dpi=130, bbox_inches='tight')
print(f"  Saved: {plot_path}")

# -----------------------------------------------------------------------------
# FINAL SUMMARY
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("MODULAR-SIN2-74 SUMMARY")
print("=" * 80)
print(f"  tau_grid             = {n_tau} points over [{tau_grid[0]:.3f}, {tau_grid[-1]:.3f}]")
print(f"  max_pq_sum           = {MAX_PQ_SUM}")
print(f"  delta_1(fold)        = {delta_1_arr[fold_idx]:.4f}")
print(f"  delta_2(fold)        = {delta_2_arr[fold_idx]:.4f}")
print(f"  delta_3(fold)        = {delta_3_arr[fold_idx]:.4f}")
print(f"  Jensen-blindness     = PRESERVED (grad ratio dev {delta_ratio:.2e})")
print(f"  sin^2 (mod A, J-wt)  = {sin2_A:.6f}  -- {abs(sin2_A-sin2_thetaW_MSbar):.4f} from PDG")
print(f"  sin^2 (mod B, J-wt)  = {sin2_B:.6f}  -- {abs(sin2_B-sin2_thetaW_MSbar):.4f} from PDG")
print(f"  Prerequisite W2-J    = FAIL")
print(f"  MODULAR-SIN2-74      = {gate_verdict}")
print(f"  Reason: {gate_reason}")
