#!/usr/bin/env python3
"""
s74_framework_rescale.py -- N17-FRAMEWORK-RESCALE-74
Framework-Level L_max Convergence of sin^2(theta_W), m_H, CC Ratio
====================================================================

Gate: N17-FRAMEWORK-RESCALE-74 (W4-G, EVOI 7.35%, Level 2*)
  PASS  if max drift_{7->9} < 5% across all three observables
  INFO  if max drift_{7->9} in [5%, 15%)
  FAIL  if max drift_{7->9} >= 15%  (framework not converged)

Substrate framing
-----------------
The Peter-Weyl truncation at L_max approximates the full Jensen-SU(3)
spectrum by summing over irreps (p,q) with p+q <= L_max. As L_max grows,
this approximation to the full spectral triple (A, H, D_K) must converge,
because adding the next shell adds finitely many additional eigenmodes
without modifying the lower shells. The framework's predictions inherit
this convergence property directly: a_0, a_2, a_4 are monotone functions
of L_max for the CCM spectral sum convention (S73B), and any downstream
observable built from ratios of a_k and threshold sums must also stabilize.

If the drift between L_max=7 and L_max=9 is large (>5%), the framework
has not yet entered the convergent regime. This is NOT a structural
defect -- it is a direct assessment of whether the current numerical
predictions (e.g., sin^2 = 0.23, m_H = 127 GeV, CC gap = 120 OOM) are
quantitatively reliable as absolute numbers. Ratios within a single L_max
(W2-M R-protected triple) remain stable even if absolute values do not.

Observables (all recomputed at L_max in {5, 7, 9})
---------------------------------------------------

1. sin^2(theta_W) at M_Z with KK threshold correction
   - Tree-level at M_KK: sin^2 = 3 e^{-4*tau} / (3 e^{-4*tau} + 1) = 0.5839
     This is L_max-INDEPENDENT (Baptista eq 5.21, pure geometry of Jensen
     SU(3) in the u(2)+C^2 decomposition).
   - RG running from M_KK to M_Z: 2-loop SM, L_max-INDEPENDENT.
   - KK threshold correction: delta(1/g_3^2)_{PW}(L_max) enters via the
     asymmetric threshold on alpha_1, alpha_2, alpha_3 at M_KK. The
     threshold correction on each coupling carries a L_max-dependent factor
     from the sum delta_i = sum_{(p,q)} T_i(p,q)/(8 pi^2) * log(Lambda^2/omega^2).
     Since T_i depends on i (different Dynkin indices for different groups),
     sin^2(M_Z) picks up mild L_max dependence through delta_1 - delta_2.
   - Here we use a SIMPLIFIED L_max dependence: since the threshold
     correction on *each* coupling scales with the same zeta sum
     S(L_max) = sum d_pq * T(p,q) * log_factor * gauss, and the RATIO
     (3/5) * delta_1 - delta_2 = 0 under the bi-invariant b_i weighting
     (S72 FIRED the asymmetric weighting that sidesteps this degeneracy),
     we recompute sin^2(M_Z) using the 2-loop RG with boundary conditions
     ALPHA_{i,MKK} determined by:
         1/alpha_i(M_KK) = (anchor) - f(L_max) * delta_{i,PW}(L_max)
     where f is the same for i=1,2 (framework has NO geometric asymmetry
     between hypercharge and isospin -- the Baptista 5.21 formula ties them
     to SU(2)_L and U(1)_Y as distinct subgroups of SU(3)).
   - CONCRETE IMPLEMENTATION: tree-level sin^2 at M_KK is L_max-
     INDEPENDENT. The RG running is also L_max-INDEPENDENT. Only
     threshold-subtracted sin^2 sees L_max, and this only through the
     a_4/a_2 ratio (which modifies lambda_h at M_KK, not sin^2 directly).
     Therefore sin^2(M_Z) is L_max-INVARIANT at tree level +/- 1-loop RG.
     To stress-test this, we evaluate sin^2 using the L_max-dependent
     coupling anchor from the same PW threshold sum delta(1/g_3^2)_L.
     If the sin^2 threshold-correction on alpha_2 is equal in magnitude
     but with a distinct sign for alpha_1, then sin^2(M_Z) inherits
     delta_SM / 2 effective.

2. m_H via 2-loop RG and lambda_CCM = (4/3) g_3^2(M_KK) * (a_4/a_2)_{L_max}
   - Ratio (a_4/a_2)_{L_max} is computed from the PW-truncated spectral
     zeta sum at each L_max.
   - RG from M_KK to M_Z with these boundary conditions.
   - m_H = sqrt(2 lambda(M_Z)) * v_ew.

3. CC ratio = rho_Lambda_spectral / rho_Lambda_obs
   - rho_Lambda_spectral = (2/pi^2) * a_0(L_max) * M_KK^4
   - a_0(L_max) is the PW spectral zeta a_0 sum (mode count) at L_max.
   - rho_Lambda_obs = 2.7e-47 GeV^4.

Methodology
-----------
Load D_K eigenvalues from s74_spectrum_cache_L9_tau019.npz (all sectors
p+q<=9 except (4,4), (4,5), (5,4) which hit the irrep-builder recursion
limitation). Missing-sector fractions: L=8 81% coverage, L=9 66% coverage.
These are documented here as partial L_max=9 data; the convergence
assessment is still meaningful because the missing sectors are AT THE BOUNDARY
of the L=8 and L=9 shells, so excluding them gives a LOWER bound on the
true L_max=9 spectral sums. If the reported drift exceeds the PASS
threshold even with incomplete data, the framework is CERTAINLY not
converged.

PW spectral zeta sums (S41/S42 convention, S73B audit-verified):
    a_0(L) = sum_{p+q<=L} dim(p,q) * n_pos(p,q)
    a_2(L) = sum_{p+q<=L} dim(p,q) * 0.5 * sum_j |lambda_j|^{-2}   (all evals, half)
    a_4(L) = sum_{p+q<=L} dim(p,q) * 0.5 * sum_j |lambda_j|^{-4}

Pre-registered drift metric
---------------------------
delta_{L1,L2} = |X(L1) - X(L2)| / max(|X(L1)|, |X(L2)|)

Session: S74 W4-G
Agent: connes-ncg-theorist
"""

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from canonical_constants import (
    PI,
    tau_fold,
    M_KK, M_KK_gravity,
    M_Z, M_W,
    alpha_em_MZ_inv, sin2_thetaW_MSbar,
    alpha_s_MZ_obs,
    m_t_pole, v_ew, m_H_obs,
    a0_fold, a2_fold, a4_fold,
    rho_Lambda_obs,
    Vol_SU3_Haar,
    sin2_thetaW_fold,
    M_Pl_reduced,
)


def log(msg=''):
    print(msg)


log("=" * 80)
log("N17-FRAMEWORK-RESCALE-74: sin^2 / m_H / CC ratio at L_max in {5, 7, 9}")
log("S74 W4-G | connes-ncg-theorist")
log("=" * 80)

# -----------------------------------------------------------------------------
# 1. LOAD D_K SPECTRUM CACHE
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("1. LOAD W1-C SPECTRUM CACHE (s74_spectrum_cache_L9_tau019.npz)")
log("=" * 80)

cache_file = os.path.join(SCRIPT_DIR, "s74_spectrum_cache_L9_tau019.npz")
cache = np.load(cache_file, allow_pickle=True)
sector_evals = cache["sector_evals"].item()

pq_list = sorted(sector_evals.keys(), key=lambda pq: (pq[0] + pq[1], pq[0], pq[1]))
log(f"  n_sectors loaded = {len(pq_list)}")

# Report sector availability by level
missing_sectors = {
    8: [(4, 4)],
    9: [(4, 5), (5, 4)],
}

log(f"\n  Sector availability by level:")
log(f"  {'L':>3} {'avail':>6} {'full':>6} {'frac_sec':>10} {'frac_mode':>12}")


def dim_su3(p, q):
    """SU(3) irrep dim."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def T_su3(p, q):
    """Dynkin index T(R) = dim(R) * C_2(R) / 8."""
    C2 = (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0
    return dim_su3(p, q) * C2 / 8.0


for L in range(10):
    avail = [(p, q) for (p, q) in pq_list if p + q == L]
    full = [(p, L - p) for p in range(L + 1)]
    # Mode count weight = dim^2 * 16 (PW degeneracy squared * D block size)
    full_w = sum(dim_su3(p, q)**2 * 16 for (p, q) in full)
    avail_w = sum(dim_su3(p, q)**2 * 16 for (p, q) in avail)
    frac_mode = avail_w / full_w if full_w > 0 else 1.0
    log(f"  {L:3d} {len(avail):6d} {len(full):6d} "
        f"{len(avail) / len(full):10.4f} {frac_mode:12.6f}")

# -----------------------------------------------------------------------------
# 2. PW SPECTRAL ZETA SUMS AT EACH L_MAX
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("2. PW SPECTRAL ZETA SUMS a_k(L_max) FOR L_max in {5, 7, 9}")
log("=" * 80)

# Convention (S41/S42, S73B SDW-VALIDATION-73B verified):
#   a_0 = sum_{(p,q)} dim(p,q) * n_pos(p,q)
#   a_2 = sum_{(p,q)} dim(p,q) * 0.5 * sum_j |lam_j|^{-2}
#   a_4 = sum_{(p,q)} dim(p,q) * 0.5 * sum_j |lam_j|^{-4}
# where 0.5 converts full spectrum to positive-half spectrum.

EVAL_CUTOFF = 0.01  # (local) same as S41, excludes zero-mode noise

L_MAX_VALUES = [5, 7, 9]  # (local)
zeta_sums = {}

for L_max in L_MAX_VALUES:
    a0 = 0.0  # (local)
    a2 = 0.0  # (local)
    a4 = 0.0  # (local)
    # For threshold correction sum: sum_{(p,q)!=(0,0)} T(p,q) * log(Lambda^2/omega_min^2) * gauss
    S_PW = 0.0  # (local) unregulated, we use gamma_opt cutoff separately
    # Also compute omega_min(p,q) for threshold formula
    omega_min_by_sector = {}
    omega_max_by_sector = {}
    n_pos_by_sector = {}

    for (p, q) in pq_list:
        if p + q > L_max:
            continue
        d_pq = dim_su3(p, q)
        info = sector_evals[(p, q)]
        ev = np.asarray(info["abs_evals"], dtype=np.float64)
        pos = ev[ev > EVAL_CUTOFF]  # (local)
        n_pos_half = len(pos) // 2  # (local) positive-half per S41 convention
        sum_inv2 = 0.5 * np.sum(pos**(-2))  # (local)
        sum_inv4 = 0.5 * np.sum(pos**(-4))  # (local)

        a0 += d_pq * n_pos_half
        a2 += d_pq * sum_inv2
        a4 += d_pq * sum_inv4

        omega_min_by_sector[(p, q)] = np.min(pos) if len(pos) > 0 else np.inf
        omega_max_by_sector[(p, q)] = np.max(pos) if len(pos) > 0 else 0.0
        n_pos_by_sector[(p, q)] = n_pos_half

    zeta_sums[L_max] = {
        'a0': a0,
        'a2': a2,
        'a4': a4,
        'omega_min': omega_min_by_sector,
        'omega_max': omega_max_by_sector,
        'n_pos': n_pos_by_sector,
    }

    log(f"\n  L_max = {L_max}:")
    log(f"    a_0(L_max)       = {a0:.4f}")
    log(f"    a_2(L_max)       = {a2:.6f}")
    log(f"    a_4(L_max)       = {a4:.6f}")
    log(f"    a_0/a_2(L_max)   = {a0/a2:.6f}")
    log(f"    a_2/a_4(L_max)   = {a2/a4:.6f}")
    log(f"    a_4/a_2(L_max)   = {a4/a2:.6f}")

# Cross-check: L_max=3 should give canonical (a0_fold, a2_fold, a4_fold)
log(f"\n  Cross-check vs canonical_constants.py (L_max=3):")
a0_L3, a2_L3, a4_L3 = 0.0, 0.0, 0.0  # (local)
for (p, q) in pq_list:
    if p + q > 3:
        continue
    d_pq = dim_su3(p, q)
    ev = np.asarray(sector_evals[(p, q)]["abs_evals"], dtype=np.float64)
    pos = ev[ev > EVAL_CUTOFF]
    n_pos_half = len(pos) // 2
    a0_L3 += d_pq * n_pos_half
    a2_L3 += d_pq * 0.5 * np.sum(pos**(-2))
    a4_L3 += d_pq * 0.5 * np.sum(pos**(-4))

log(f"    a_0(L=3)    = {a0_L3:.4f} (canonical a0_fold = {a0_fold:.4f}, "
    f"dev = {abs(a0_L3 - a0_fold) / a0_fold:.2e})")
log(f"    a_2(L=3)    = {a2_L3:.6f} (canonical a2_fold = {a2_fold:.6f}, "
    f"dev = {abs(a2_L3 - a2_fold) / a2_fold:.2e})")
log(f"    a_4(L=3)    = {a4_L3:.6f} (canonical a4_fold = {a4_fold:.6f}, "
    f"dev = {abs(a4_L3 - a4_fold) / a4_fold:.2e})")

assert abs(a0_L3 - a0_fold) / a0_fold < 1e-10, \
    f"a_0(L=3) mismatch: {a0_L3} vs {a0_fold}"
assert abs(a2_L3 - a2_fold) / a2_fold < 1e-10, \
    f"a_2(L=3) mismatch: {a2_L3} vs {a2_fold}"
assert abs(a4_L3 - a4_fold) / a4_fold < 1e-10, \
    f"a_4(L=3) mismatch: {a4_L3} vs {a4_fold}"
log(f"    PASS: cache reproduces canonical a_0, a_2, a_4 to machine epsilon.")

# -----------------------------------------------------------------------------
# 3. OBSERVABLE 1: sin^2(theta_W) at M_Z WITH KK THRESHOLD CORRECTION
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("3. OBSERVABLE 1: sin^2(theta_W) WITH THRESHOLD CORRECTION")
log("=" * 80)

# Tree-level boundary condition at M_KK (Baptista Paper 13 eq 5.21)
# This is L_max-INDEPENDENT.
gp2_MKK_tree = 12.0 * np.exp(-2.0 * tau_fold)  # (local) g'^2 at M_KK
g2_MKK_tree = 4.0 * np.exp(2.0 * tau_fold)     # (local) g^2 (SU(2)_L) at M_KK
sin2_MKK_tree = gp2_MKK_tree / (gp2_MKK_tree + g2_MKK_tree)

alpha1_MKK_inv_tree = (3.0 / 5.0) * 4.0 * PI / gp2_MKK_tree  # (local) GUT-normalized
alpha2_MKK_inv_tree = 4.0 * PI / g2_MKK_tree                  # (local)

log(f"\n  Tree-level at M_KK (L_max-independent):")
log(f"    sin^2(theta_W)|_{{M_KK}} = {sin2_MKK_tree:.6f} (canonical fold: {sin2_thetaW_fold:.6f})")
log(f"    1/alpha_1(M_KK) [GUT]  = {alpha1_MKK_inv_tree:.4f}")
log(f"    1/alpha_2(M_KK)        = {alpha2_MKK_inv_tree:.4f}")

# For the L_max-dependent threshold correction, we use the PW threshold
# sum (S70 Formula C). At each L_max we compute delta(1/g_3^2)_{PW}(L_max)
# for the strong coupling, then the asymmetric SM threshold on alpha_1, alpha_2.
#
# Formula C (Gaussian-regulated):
#   delta_i(L_max) = sum_{p+q<=L, (p,q)!=(0,0)} (b^{KK}_i(p,q) / (8 pi^2))
#                    * log(Lambda^2/omega_min^2) * exp(-omega_min^2/Lambda^2)
#
# where b^{KK}_i(p,q) is the gauge-group-dependent Dynkin index.
# For SU(3)_c, b^{KK}_3(p,q) = T_3(p,q) (the Dynkin index in the
# adjoint decomposition).
#
# For U(1)_Y and SU(2)_L, the framework uses the same asymmetric Baptista
# boundary conditions; the threshold sum scales with T(p,q) for the
# GROUP in which the bulk fields transform. For KK modes of the gauge
# bosons, the bulk group is the SU(3) of the internal manifold,
# and each level contributes T_su3(p,q) to the running.
#
# In the absence of group-asymmetric matter content at KK excitations,
# the threshold corrections on 1/alpha_i are identical in their L_max
# dependence, up to an overall coefficient that matches b_i^{KK}.
# Therefore:
#   delta(1/alpha_i)(L_max) = c_i * S_PW(L_max)
# where c_i depends only on the group representation (i=1,2,3).
#
# For this framework-rescale test we focus on the SCHEME-INDEPENDENT
# threshold sum:
#   S_PW(L_max) = sum_{(p,q)!=(0,0), p+q<=L} T(p,q)/(8 pi^2)
#                  * log(Lambda^2/omega_min^2) * exp(-omega_min^2/Lambda^2)
#
# This is the "S_inf" converging quantity that enters delta(1/g_3^2).
# Then sin^2(M_Z) with threshold correction is obtained by running the
# 2-loop SM RGE from M_KK to M_Z starting from anchored alpha_i values.

# Load S71 Lambda (gamma-optimized cutoff)
try:
    s71_data = np.load(os.path.join(SCRIPT_DIR, 's71_spectral_zeta_threshold.npz'),
                        allow_pickle=True)
    Lambda_fixed = float(s71_data['Lambda_fixed'])
    log(f"\n  Lambda_fixed (from S71, gamma-optimized) = {Lambda_fixed:.6f} M_KK")
except Exception:
    Lambda_fixed = 2.048  # (local) S64 default
    log(f"\n  Lambda_fixed (default, S64) = {Lambda_fixed:.6f} M_KK")

# Compute PW threshold sum at each L_max
log(f"\n  PW threshold sum S_PW(L_max) = sum T(p,q)/(8pi^2) * ln(Lambda^2/om^2) * gauss")
log(f"  {'L_max':>6} {'S_PW':>14} {'n_sectors':>10}")

threshold_sums = {}
for L_max in L_MAX_VALUES:
    S_PW = 0.0  # (local)
    n_sec = 0  # (local)
    for (p, q) in pq_list:
        if p + q > L_max:
            continue
        if p == 0 and q == 0:
            continue
        omega = zeta_sums[L_max]['omega_min'][(p, q)]
        if not np.isfinite(omega) or omega <= 0:
            continue
        T_pq = T_su3(p, q)
        log_term = np.log(Lambda_fixed**2 / omega**2)
        gauss_w = np.exp(-omega**2 / Lambda_fixed**2)
        contrib = T_pq / (8 * PI**2) * log_term * gauss_w
        S_PW += contrib
        n_sec += 1
    threshold_sums[L_max] = S_PW
    log(f"  {L_max:6d} {S_PW:14.8f} {n_sec:10d}")

# Cross-check at L_max=7 vs S70/S71 (should give ~3.13 or similar)
log(f"\n  S_PW(L=7) compared to S70/S71 reference:")
try:
    s70_data = np.load(os.path.join(SCRIPT_DIR, 's70_lmax7_pw.npz'), allow_pickle=True)
    S70_gauss = s70_data['S_gauss']  # L=0..7 cumulative
    log(f"    S70 S_gauss(L=7) = {S70_gauss[7]:.8f}")
    log(f"    Ours S_PW(L=7)    = {threshold_sums[7]:.8f}")
    log(f"    Deviation         = {abs(threshold_sums[7] - S70_gauss[7]):.2e}")
except Exception as e:
    log(f"    S70 cross-check not available: {e}")

# SM 2-loop RG equations
def beta_2loop_SM(t, y):
    """2-loop SM betas for (g1, g2, g3, yt, lambda)."""
    g1, g2, g3, yt, lam = y
    g1sq, g2sq, g3sq = g1**2, g2**2, g3**2
    ytsq = yt**2
    b16 = 16.0 * PI**2
    b16sq = b16**2

    dg1 = g1**3 / b16 * (41.0 / 10.0) + g1**3 / b16sq * (
        199.0 / 50.0 * g1sq + 27.0 / 10.0 * g2sq + 44.0 / 5.0 * g3sq
        - 17.0 / 10.0 * ytsq)
    dg2 = g2**3 / b16 * (-19.0 / 6.0) + g2**3 / b16sq * (
        9.0 / 10.0 * g1sq + 35.0 / 6.0 * g2sq + 12.0 * g3sq
        - 3.0 / 2.0 * ytsq)
    dg3 = g3**3 / b16 * (-7.0) + g3**3 / b16sq * (
        11.0 / 10.0 * g1sq + 9.0 / 2.0 * g2sq - 26.0 * g3sq
        - 2.0 * ytsq)

    dyt = yt / b16 * (9.0 / 2.0 * ytsq - 17.0 / 20.0 * g1sq
                      - 9.0 / 4.0 * g2sq - 8.0 * g3sq)

    dlam = (1.0 / b16) * (
        24.0 * lam**2 + 12.0 * lam * ytsq - 12.0 * ytsq**2
        - 3.0 * lam * (3.0 / 5.0 * g1sq + 3.0 * g2sq)
        + 3.0 / 8.0 * (3.0 / 25.0 * g1sq**2 + 6.0 / 5.0 * g1sq * g2sq
                        + 3.0 * g2sq**2))

    return [dg1, dg2, dg3, dyt, dlam]


# Anchor: RG running from M_Z (PDG) UP to M_KK to establish the M_KK-scale
# couplings, then inject the threshold correction and run DOWN. This is
# the convention used in S70/S71.
alpha_em_MZ = 1.0 / alpha_em_MZ_inv
sin2_tW_MZ_PDG = sin2_thetaW_MSbar
g1_MZ = np.sqrt(5.0 / 3.0) * np.sqrt(4 * PI * alpha_em_MZ / (1 - sin2_tW_MZ_PDG))
g2_MZ = np.sqrt(4 * PI * alpha_em_MZ / sin2_tW_MZ_PDG)
g3_MZ = np.sqrt(4 * PI * alpha_s_MZ_obs)
m_t_MSbar = m_t_pole * (1.0 - 4.0 * alpha_s_MZ_obs / (3.0 * PI))
yt_MZ = np.sqrt(2.0) * m_t_MSbar / v_ew
lambda_MZ_obs = m_H_obs**2 / (2.0 * v_ew**2)

t_MKK = np.log(M_KK_gravity / M_Z)  # ~ 34.3

# Run SM up from M_Z to M_KK to anchor the UV couplings
y0_up = [g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs]
sol_up = solve_ivp(
    beta_2loop_SM, [0, t_MKK], y0_up,
    t_eval=np.linspace(0, t_MKK, 2000),
    method='RK45', rtol=1e-12, atol=1e-14
)
g1_MKK_anchor = sol_up.y[0, -1]
g2_MKK_anchor = sol_up.y[1, -1]
g3_MKK_anchor = sol_up.y[2, -1]
yt_MKK_anchor = sol_up.y[3, -1]
lam_MKK_anchor = sol_up.y[4, -1]

log(f"\n  SM couplings at M_KK (2-loop up-run, PDG anchor):")
log(f"    g_1(M_KK) = {g1_MKK_anchor:.6f}, 1/alpha_1 = {4 * PI / g1_MKK_anchor**2:.4f}")
log(f"    g_2(M_KK) = {g2_MKK_anchor:.6f}, 1/alpha_2 = {4 * PI / g2_MKK_anchor**2:.4f}")
log(f"    g_3(M_KK) = {g3_MKK_anchor:.6f}, 1/alpha_3 = {4 * PI / g3_MKK_anchor**2:.4f}")
log(f"    sin^2 at M_KK (PDG-anchored, 2-loop up) = "
    f"{4*PI/g1_MKK_anchor**2 / (4*PI/g1_MKK_anchor**2 + (3./5.)*4*PI/g2_MKK_anchor**2 * (3./5.) + ...):.6f}"
    if False else "")

# Now the L_max-dependent sin^2(theta_W) is computed via the following:
# At each L_max, the threshold sum S_PW(L_max) shifts the effective 1/g_3^2
# (and, in a symmetric framework, also 1/g_1^2 and 1/g_2^2 by proportional
# amounts b_i^{KK}). If we assume equal shifts (which is the tree-level
# expectation for Jensen SU(3) with no matter asymmetry at the KK level),
# sin^2 at M_Z is INVARIANT under S_PW.
#
# To give sin^2 a non-trivial L_max dependence, we use the tree-level
# Baptista boundary condition 5.21 (L_max-independent) combined with an
# EFFECTIVE UV boundary that mixes PDG-anchored + threshold shift.
# The most physical choice is: use the geometric sin^2(M_KK)=0.5839 as
# the tree-level boundary, run down with 2-loop SM, add threshold on
# g_3 only, and see how sin^2(M_Z) moves.
#
# RESULT: tree-level sin^2(M_KK)=0.5839 + pure 2-loop SM run-down (no
# threshold on g_1, g_2) gives sin^2(M_Z) that depends ONLY on the
# starting values (invariant under L_max). Threshold on g_3 alone does
# not affect sin^2 at M_Z.
#
# The TRUE L_max dependence comes from the threshold correction on
# g_1 and g_2 separately, which scales with different Dynkin indices
# for U(1)_Y (b^{KK}_1) and SU(2)_L (b^{KK}_2). In the SIMPLEST
# framework assumption:
#     b^{KK}_i = b^{KK}_SM * (3/5 for i=1, 1 for i=2, 1 for i=3)
# all three shift uniformly and sin^2 is L_max-INVARIANT.
#
# The framework prediction sin^2(M_Z) is therefore INDEPENDENT of L_max
# at leading order in the threshold correction, and only picks up
# L_max dependence at the RATIO level through delta_1/delta_2 asymmetries
# generated by distinct (p,q)-dependent Dynkin indices of the bulk group.
# We compute this explicitly.

log(f"\n  L_max dependence of sin^2 via group-dependent threshold:")
log(f"  {'L_max':>6} {'S_PW':>14} {'1/a_1(MKK)_eff':>16} {'1/a_2(MKK)_eff':>16} "
    f"{'sin^2(MZ)':>12}")

sin2_MZ_by_L = {}
for L_max in L_MAX_VALUES:
    S_PW = threshold_sums[L_max]

    # Asymmetric threshold on alpha_1 and alpha_2 following the standard
    # SM KK threshold formula: delta(1/alpha_i) = b_i^{KK} * S_PW where
    # b_i^{KK} captures the hypercharge / isospin Dynkin indices.
    #
    # Reference: for KK replicas of the SM gauge sector on SU(3),
    # b_i^{KK} / b_i^{SM} ratio follows from Kaluza-Klein counting.
    # For the purpose of the framework rescale test, we use the
    # IDENTICAL shift on all three, which gives sin^2 L_max-invariant.
    #
    # To expose the L_max drift from asymmetric thresholds, we also
    # compute the variant with the Baptista asymmetry (3/5 vs 1 vs 1):
    delta_1 = (3.0 / 5.0) * S_PW  # hypercharge normalized
    delta_2 = 1.0 * S_PW
    delta_3 = 1.0 * S_PW

    alpha1_inv_MKK_eff = 4 * PI / g1_MKK_anchor**2 + delta_1
    alpha2_inv_MKK_eff = 4 * PI / g2_MKK_anchor**2 + delta_2
    alpha3_inv_MKK_eff = 4 * PI / g3_MKK_anchor**2 + delta_3

    g1_MKK_eff = np.sqrt(4 * PI / alpha1_inv_MKK_eff)
    g2_MKK_eff = np.sqrt(4 * PI / alpha2_inv_MKK_eff)
    g3_MKK_eff = np.sqrt(4 * PI / alpha3_inv_MKK_eff)

    # Run DOWN from M_KK to M_Z with threshold-corrected UV values
    y0_down = [g1_MKK_eff, g2_MKK_eff, g3_MKK_eff, yt_MKK_anchor, lam_MKK_anchor]
    sol_down = solve_ivp(
        beta_2loop_SM, [t_MKK, 0], y0_down,
        t_eval=np.linspace(t_MKK, 0, 2000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    g1_MZ_eff = sol_down.y[0, -1]
    g2_MZ_eff = sol_down.y[1, -1]

    # sin^2 from g_1 (GUT-normalized) and g_2
    alpha1_MZ_eff = g1_MZ_eff**2 / (4 * PI)  # (local) GUT-normalized
    alpha2_MZ_eff = g2_MZ_eff**2 / (4 * PI)
    # sin^2 = (3/5)*alpha_1 / ((3/5)*alpha_1 + alpha_2)
    sin2_MZ = (3.0/5.0) * alpha1_MZ_eff / ((3.0/5.0) * alpha1_MZ_eff + alpha2_MZ_eff)
    sin2_MZ_by_L[L_max] = sin2_MZ

    log(f"  {L_max:6d} {S_PW:14.8f} {alpha1_inv_MKK_eff:16.4f} "
        f"{alpha2_inv_MKK_eff:16.4f} {sin2_MZ:12.8f}")

log(f"\n  sin^2(theta_W) at M_Z:")
for L_max in L_MAX_VALUES:
    dev = abs(sin2_MZ_by_L[L_max] - sin2_thetaW_MSbar) / sin2_thetaW_MSbar * 100
    log(f"    L_max={L_max}: sin^2 = {sin2_MZ_by_L[L_max]:.6f} (PDG {sin2_thetaW_MSbar}, dev {dev:+.4f}%)")

# -----------------------------------------------------------------------------
# 4. OBSERVABLE 2: m_H via CCM lambda_h = (4/3) g_3^2 * (a_4/a_2)
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("4. OBSERVABLE 2: m_H via CCM lambda_h(M_KK) = (4/3) g_3^2 * (a_4/a_2)_{L_max}")
log("=" * 80)

log(f"\n  Standard CCM Higgs mass prediction (S70/S71 recipe):")
log(f"    lambda_h(M_KK) = (4/3) * g_3^2(M_KK) * (a_4/a_2)_{{L_max}}")
log(f"    Run 2-loop SM down to M_Z, m_H = sqrt(2*lambda(M_Z)) * v_ew")

mH_by_L = {}
for L_max in L_MAX_VALUES:
    # Apply threshold correction to g_3 at M_KK
    S_PW = threshold_sums[L_max]
    alpha3_inv_MKK_eff = 4 * PI / g3_MKK_anchor**2 + S_PW
    g3_MKK_eff = np.sqrt(4 * PI / alpha3_inv_MKK_eff)

    # PW-truncated a_4/a_2 at this L_max
    ratio_a4_a2_L = zeta_sums[L_max]['a4'] / zeta_sums[L_max]['a2']
    lam_CCM_L = (4.0 / 3.0) * g3_MKK_eff**2 * ratio_a4_a2_L

    # Run SM down with this lambda as the boundary
    y0_down = [g1_MKK_anchor, g2_MKK_anchor, g3_MKK_eff, yt_MKK_anchor, lam_CCM_L]
    sol_down = solve_ivp(
        beta_2loop_SM, [t_MKK, 0], y0_down,
        t_eval=np.linspace(t_MKK, 0, 2000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    lam_MZ = sol_down.y[4, -1]
    mH = np.sqrt(2.0 * lam_MZ) * v_ew if lam_MZ > 0 else 0.0
    mH_by_L[L_max] = mH

    log(f"  L_max={L_max}: (a_4/a_2)={ratio_a4_a2_L:.6f}, g_3_eff={g3_MKK_eff:.4f}, "
        f"lam_CCM={lam_CCM_L:.6f}, m_H={mH:.4f} GeV")

log(f"\n  m_H(L_max):")
for L_max in L_MAX_VALUES:
    dev = (mH_by_L[L_max] - m_H_obs) / m_H_obs * 100
    log(f"    L_max={L_max}: m_H = {mH_by_L[L_max]:.4f} GeV (obs {m_H_obs}, dev {dev:+.4f}%)")

# -----------------------------------------------------------------------------
# 5. OBSERVABLE 3: CC ratio rho_Lambda_spectral / rho_Lambda_obs
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("5. OBSERVABLE 3: CC RATIO (a_0(L_max) * M_KK^4) / rho_Lambda_obs")
log("=" * 80)

# rho_Lambda_spectral = (2/pi^2) * a_0 * M_KK^4 (S42 convention)
# rho_Lambda_obs = 2.7e-47 GeV^4 (Planck 2018 rounding)

log(f"\n  M_KK = {M_KK:.4e} GeV")
log(f"  M_KK_gravity = {M_KK_gravity:.4e} GeV")
log(f"  rho_Lambda_obs = {rho_Lambda_obs:.4e} GeV^4")

# Use M_KK_gravity for consistency with S42 conventions
M_KK_use = M_KK_gravity

CC_ratio_by_L = {}
for L_max in L_MAX_VALUES:
    a0_L = zeta_sums[L_max]['a0']
    rho_Lambda_spectral_L = (2.0 / PI**2) * a0_L * M_KK_use**4  # (local)
    CC_ratio_L = rho_Lambda_spectral_L / rho_Lambda_obs
    CC_ratio_by_L[L_max] = CC_ratio_L

    log(f"  L_max={L_max}: a_0 = {a0_L:.2f}, rho_spectral = {rho_Lambda_spectral_L:.4e} GeV^4, "
        f"CC ratio = {CC_ratio_L:.4e} ({np.log10(CC_ratio_L):.3f} OOM)")

log(f"\n  CC ratio (framework/observed):")
for L_max in L_MAX_VALUES:
    log10_cc = np.log10(CC_ratio_by_L[L_max])
    log(f"    L_max={L_max}: {CC_ratio_by_L[L_max]:.4e} ({log10_cc:.3f} OOM gap)")

# -----------------------------------------------------------------------------
# 6. DRIFT TABLE AND GATE EVALUATION
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("6. DRIFT TABLE AND GATE N17-FRAMEWORK-RESCALE-74")
log("=" * 80)


def compute_drift(x_L1, x_L2):
    """Symmetric relative drift: |x_L1 - x_L2| / max(|x_L1|, |x_L2|)."""
    return abs(x_L1 - x_L2) / max(abs(x_L1), abs(x_L2))


observables = {
    'sin2_MZ':  sin2_MZ_by_L,
    'mH':       mH_by_L,
    'CC_ratio': CC_ratio_by_L,
    'a_0':      {L: zeta_sums[L]['a0'] for L in L_MAX_VALUES},
    'a_2':      {L: zeta_sums[L]['a2'] for L in L_MAX_VALUES},
    'a_4':      {L: zeta_sums[L]['a4'] for L in L_MAX_VALUES},
    'a_4/a_2':  {L: zeta_sums[L]['a4'] / zeta_sums[L]['a2'] for L in L_MAX_VALUES},
    'a_0/a_2':  {L: zeta_sums[L]['a0'] / zeta_sums[L]['a2'] for L in L_MAX_VALUES},
    'S_PW':     threshold_sums,
    'log10(CC)':{L: np.log10(CC_ratio_by_L[L]) for L in L_MAX_VALUES},
}

# Build drift table
log(f"\n  Drift table (delta = |X(L_hi) - X(L_lo)| / max):")
log(f"  {'Observable':<14} {'X(L=5)':>14} {'X(L=7)':>14} {'X(L=9)':>14} "
    f"{'d_{5->7}':>10} {'d_{7->9}':>10}")

drift_table = {}
for name, X_dict in observables.items():
    X5 = X_dict[5]
    X7 = X_dict[7]
    X9 = X_dict[9]
    d_57 = compute_drift(X5, X7)
    d_79 = compute_drift(X7, X9)
    drift_table[name] = {'X5': X5, 'X7': X7, 'X9': X9, 'd_57': d_57, 'd_79': d_79}

    # Format numbers
    fmt_X = lambda x: f"{x:14.6e}" if abs(x) > 1e6 or abs(x) < 1e-3 else f"{x:14.6f}"
    log(f"  {name:<14} {fmt_X(X5)} {fmt_X(X7)} {fmt_X(X9)} "
        f"{d_57*100:9.4f}% {d_79*100:9.4f}%")

# Primary gate: max drift 7->9 across three primary observables
primary_names = ['sin2_MZ', 'mH', 'CC_ratio']
max_drift_79 = max(drift_table[n]['d_79'] for n in primary_names)
which_worst = max(primary_names, key=lambda n: drift_table[n]['d_79'])

log(f"\n  Primary observables drift 7->9:")
for n in primary_names:
    log(f"    {n:<10}: {drift_table[n]['d_79']*100:9.4f}%")

log(f"\n  Max drift 7->9: {max_drift_79*100:.4f}% ({which_worst})")

if max_drift_79 < 0.05:
    gate_verdict = "PASS"
elif max_drift_79 < 0.15:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

log(f"\n  *** GATE N17-FRAMEWORK-RESCALE-74: {gate_verdict} ***")
log(f"      Pre-registered thresholds:")
log(f"        PASS if max drift_{{7->9}} < 5%")
log(f"        INFO if max drift_{{7->9}} in [5%, 15%)")
log(f"        FAIL if max drift_{{7->9}} >= 15%")
log(f"      Computed max drift_{{7->9}} = {max_drift_79*100:.4f}%")
log(f"      Verdict: {gate_verdict}")

# -----------------------------------------------------------------------------
# 7. SAVE DATA
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("7. SAVE DATA")
log("=" * 80)

output_data = {
    'L_max_values': np.array(L_MAX_VALUES),
    # Spectral zeta sums
    'a0_L5': zeta_sums[5]['a0'],
    'a0_L7': zeta_sums[7]['a0'],
    'a0_L9': zeta_sums[9]['a0'],
    'a2_L5': zeta_sums[5]['a2'],
    'a2_L7': zeta_sums[7]['a2'],
    'a2_L9': zeta_sums[9]['a2'],
    'a4_L5': zeta_sums[5]['a4'],
    'a4_L7': zeta_sums[7]['a4'],
    'a4_L9': zeta_sums[9]['a4'],
    # PW threshold sums
    'S_PW_L5': threshold_sums[5],
    'S_PW_L7': threshold_sums[7],
    'S_PW_L9': threshold_sums[9],
    # Observables
    'sin2_MZ_L5': sin2_MZ_by_L[5],
    'sin2_MZ_L7': sin2_MZ_by_L[7],
    'sin2_MZ_L9': sin2_MZ_by_L[9],
    'mH_L5': mH_by_L[5],
    'mH_L7': mH_by_L[7],
    'mH_L9': mH_by_L[9],
    'CC_ratio_L5': CC_ratio_by_L[5],
    'CC_ratio_L7': CC_ratio_by_L[7],
    'CC_ratio_L9': CC_ratio_by_L[9],
    # Drift table
    'drift_sin2_57':   drift_table['sin2_MZ']['d_57'],
    'drift_sin2_79':   drift_table['sin2_MZ']['d_79'],
    'drift_mH_57':     drift_table['mH']['d_57'],
    'drift_mH_79':     drift_table['mH']['d_79'],
    'drift_CC_57':     drift_table['CC_ratio']['d_57'],
    'drift_CC_79':     drift_table['CC_ratio']['d_79'],
    'max_drift_79':    max_drift_79,
    'worst_observable': which_worst,
    'gate_verdict':    gate_verdict,
    # Constants
    'Lambda_fixed':    Lambda_fixed,
    'M_KK_use':        M_KK_use,
    'tau_fold':        tau_fold,
    # Input values
    'sin2_MZ_PDG':     sin2_thetaW_MSbar,
    'mH_obs':          m_H_obs,
    'rho_Lambda_obs':  rho_Lambda_obs,
}

np.savez(
    os.path.join(SCRIPT_DIR, 's74_framework_rescale.npz'),
    **output_data
)
log(f"  Saved: s74_framework_rescale.npz")

# -----------------------------------------------------------------------------
# 8. PLOT
# -----------------------------------------------------------------------------
log("\n" + "=" * 80)
log("8. PLOT")
log("=" * 80)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

L_arr = np.array(L_MAX_VALUES, dtype=float)

# Panel 1: sin^2(theta_W)
ax1 = axes[0, 0]
sin2_vals = [sin2_MZ_by_L[L] for L in L_MAX_VALUES]
ax1.plot(L_arr, sin2_vals, 'bo-', markersize=10, linewidth=2, label='Framework')
ax1.axhline(sin2_thetaW_MSbar, color='r', linestyle='--',
            label=f'PDG: {sin2_thetaW_MSbar}')
ax1.set_xlabel('L_max', fontsize=11)
ax1.set_ylabel('sin^2(theta_W)(M_Z)', fontsize=11)
ax1.set_title('sin^2(theta_W) vs L_max', fontsize=12)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: m_H
ax2 = axes[0, 1]
mH_vals = [mH_by_L[L] for L in L_MAX_VALUES]
ax2.plot(L_arr, mH_vals, 'go-', markersize=10, linewidth=2, label='Framework')
ax2.axhline(m_H_obs, color='r', linestyle='--', label=f'Observed: {m_H_obs} GeV')
ax2.set_xlabel('L_max', fontsize=11)
ax2.set_ylabel('m_H (GeV)', fontsize=11)
ax2.set_title('Higgs mass vs L_max', fontsize=12)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: log10(CC ratio)
ax3 = axes[0, 2]
CC_vals = [np.log10(CC_ratio_by_L[L]) for L in L_MAX_VALUES]
ax3.plot(L_arr, CC_vals, 'mo-', markersize=10, linewidth=2, label='Framework')
ax3.set_xlabel('L_max', fontsize=11)
ax3.set_ylabel('log10(rho_Lambda_spec / rho_Lambda_obs)', fontsize=11)
ax3.set_title('CC gap (OOM) vs L_max', fontsize=12)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# Panel 4: Drift 7->9 bar chart
ax4 = axes[1, 0]
names_plot = ['sin^2', 'm_H', 'CC']
drift_vals_79 = [drift_table['sin2_MZ']['d_79'] * 100,
                 drift_table['mH']['d_79'] * 100,
                 drift_table['CC_ratio']['d_79'] * 100]
drift_vals_57 = [drift_table['sin2_MZ']['d_57'] * 100,
                 drift_table['mH']['d_57'] * 100,
                 drift_table['CC_ratio']['d_57'] * 100]
x_pos = np.arange(len(names_plot))
w_bar = 0.35  # (local)
ax4.bar(x_pos - w_bar/2, drift_vals_57, w_bar, label='5 -> 7', color='tab:orange')
ax4.bar(x_pos + w_bar/2, drift_vals_79, w_bar, label='7 -> 9', color='tab:blue')
ax4.axhline(5, color='g', linestyle='--', alpha=0.6, label='PASS 5%')
ax4.axhline(15, color='r', linestyle='--', alpha=0.6, label='FAIL 15%')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(names_plot)
ax4.set_ylabel('Drift (%)', fontsize=11)
ax4.set_title(f'Convergence drift (verdict: {gate_verdict})', fontsize=12)
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3, axis='y')

# Panel 5: a_0, a_2, a_4 vs L_max
ax5 = axes[1, 1]
a0_vals = [zeta_sums[L]['a0'] for L in L_MAX_VALUES]
a2_vals = [zeta_sums[L]['a2'] for L in L_MAX_VALUES]
a4_vals = [zeta_sums[L]['a4'] for L in L_MAX_VALUES]
ax5.semilogy(L_arr, a0_vals, 'bo-', markersize=8, label='a_0')
ax5.semilogy(L_arr, a2_vals, 'gs-', markersize=8, label='a_2')
ax5.semilogy(L_arr, a4_vals, 'r^-', markersize=8, label='a_4')
ax5.set_xlabel('L_max', fontsize=11)
ax5.set_ylabel('Spectral zeta sum', fontsize=11)
ax5.set_title('a_0, a_2, a_4 vs L_max (log scale)', fontsize=12)
ax5.legend(fontsize=10)
ax5.grid(True, alpha=0.3)

# Panel 6: a_4/a_2 ratio vs L_max (Higgs input)
ax6 = axes[1, 2]
ratio_vals = [zeta_sums[L]['a4'] / zeta_sums[L]['a2'] for L in L_MAX_VALUES]
ax6.plot(L_arr, ratio_vals, 'co-', markersize=10, linewidth=2)
ax6.set_xlabel('L_max', fontsize=11)
ax6.set_ylabel('a_4/a_2 (CCM Higgs quartic input)', fontsize=11)
ax6.set_title('a_4/a_2 ratio vs L_max', fontsize=12)
ax6.grid(True, alpha=0.3)

plt.suptitle(
    f'N17-FRAMEWORK-RESCALE-74: Framework L_max convergence (S74 W4-G) | '
    f'verdict: {gate_verdict}',
    fontsize=14, fontweight='bold'
)
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's74_framework_rescale.png'), dpi=120,
            bbox_inches='tight')
plt.close()
log(f"  Saved: s74_framework_rescale.png")

log("\n" + "=" * 80)
log("N17-FRAMEWORK-RESCALE-74 COMPLETE")
log(f"  Primary observables drift 7->9: "
    f"sin^2={drift_table['sin2_MZ']['d_79']*100:.2f}%, "
    f"m_H={drift_table['mH']['d_79']*100:.2f}%, "
    f"CC={drift_table['CC_ratio']['d_79']*100:.2f}%")
log(f"  GATE VERDICT: {gate_verdict}")
log(f"  Worst drift observable: {which_worst}")
log("=" * 80)
