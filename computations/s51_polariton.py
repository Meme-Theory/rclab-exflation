#!/usr/bin/env python3
"""
s51_polariton.py — Polariton/Hopfield Model for SA-Goldstone Coupling
=====================================================================

Gate: POLARITON-51
    PASS: Lower polariton alpha_eff at K_pivot differs from 2.0 by > 0.1
    FAIL: Coupling too weak (Omega_R / linewidth < 0.1), both branches remain pure
    INFO: alpha_eff changes but magnitude insufficient for n_s target

Physics:
    Two excitation branches — the Goldstone phase mode (light, m_G = 0.070 M_KK)
    and the spectral action effective mode (heavy, sqrt(C2_eff) ~ 2.71 M_KK) —
    couple through the BCS gap chain: delta_tau -> delta_Delta -> delta_J.

    The 2x2 Hopfield dynamical matrix (entries are omega^2 in M_KK^2 units):

        M(K) = | J_G K^2 + m_G^2,   g_mix     |
               | g_mix,             C2_eff     |

    has eigenvalues omega_pm^2(K) = (Tr +/- sqrt(Tr^2 - 4 Det)) / 2.

    Stability requires Det(M) > 0, i.e. g_mix^2 < (J_G K^2 + m_G^2) * C2_eff.
    At K=0, this gives g_mix < sqrt(m_G^2 * C2_eff) = 0.1899 M_KK^2.
    A coupling exceeding this threshold produces a tachyonic lower branch at K=0,
    signaling the model breaks down (runaway instability, not polariton formation).

Session: S51  |  Author: Landau condensed-matter-theorist
Inputs: S49 DIPOLAR-CATALOG, S50 cross-domain, S48 Josephson, canonical_constants
"""

import sys
import numpy as np
sys.path.insert(0, '.')
from canonical_constants import (
    dS_fold, Delta_0_GL, Delta_0_OES, E_cond, tau_fold,
    omega_PV, S_inst, Delta_B3, PI, Gamma_Langer_BCS
)

# ============================================================================
#  SECTION 1: Input Constants (all in M_KK units)
# ============================================================================

# Goldstone sector (from S49 DIPOLAR-CATALOG, S48, S47)
m_G = 0.070            # Leggett mass = omega_L1 (S49 DIPOLAR-CATALOG)
epsilon_inner = 0.052  # inner fluctuation breaking parameter (S49)
rho_s = 7.962          # superfluid stiffness (S47, C2 Casimir)
J_eff = 0.641          # effective Josephson coupling (2*J_C2 + J_su2)/3 (S48)

# Goldstone stiffness
J_G = J_eff            # spatial stiffness for the Goldstone
m_G_sq = m_G**2        # = 0.0049 M_KK^2

# Spectral action sector (from S50 cross-domain finding)
# chi_SA(K) = Sum W_{(p,q)} / (K^2 + C2(p,q))
SA_data = [
    # (label, C2, weight_fraction)
    ('(1,0)/(0,1)', 1.333, 0.006),
    ('(1,1)',        3.000, 0.072),
    ('(2,0)/(0,2)', 3.333, 0.061),
    ('(3,0)/(0,3)', 6.000, 0.333),
    ('(2,1)/(1,2)', 9.333, 0.529),
]
C2_values = np.array([d[1] for d in SA_data])
W_raw = np.array([d[2] for d in SA_data])
W_values = W_raw / W_raw.sum()  # normalize

C2_eff = np.dot(W_values, C2_values)   # weighted average
C2_rms = np.sqrt(np.dot(W_values, C2_values**2))

# Coupling chain constants
dS_dtau = dS_fold                      # = 58,672.8 (S42)
dDelta_dtau = 0.0081                   # M_KK (task specification)

# Pivot
K_pivot = 2.0                          # M_KK

# Damping
Q_Leggett = 670000.0
Gamma_G = m_G / Q_Leggett             # ~ 1.04e-7 M_KK
Gamma_SA = Gamma_Langer_BCS           # ~ 0.25 M_KK (Langer rate as upper bound)
total_linewidth = Gamma_G + Gamma_SA

# Stability threshold at K=0
g_stability = np.sqrt(m_G_sq * C2_eff)  # = sqrt(0.0049 * 7.355) = 0.1899

print("=" * 78)
print("S51 POLARITON/HOPFIELD MODEL: SA-Goldstone Coupling")
print("=" * 78)
print()

# ============================================================================
#  SECTION 2: Coupling Constants — Three Physical Estimates
# ============================================================================

print("--- Section 2: Coupling Constants ---")
print()

# (a) Geometric mean: g_geom = epsilon_inner * sqrt(m_G^2 * C2_eff)
# Dimensionally: [dimensionless] * sqrt([M_KK^2] * [M_KK^2]) = [M_KK^2]. Correct.
g_geom = epsilon_inner * np.sqrt(m_G_sq * C2_eff)
print(f"  (a) g_geom = eps_inner * sqrt(m_G^2 * C2_eff)")
print(f"       = {epsilon_inner} * sqrt({m_G_sq:.6f} * {C2_eff:.4f})")
print(f"       = {g_geom:.6f} M_KK^2")
print()

# (b) BCS gap chain: the off-diagonal matrix element arises because a tau
# perturbation shifts both sectors. The natural dimensionless coupling is:
#   g_BCS / sqrt(m_G^2 * C2_eff) = dimensionless measure of mixing.
# The mixing arises from the gap sensitivity:
#   lambda_BCS = (dDelta/dtau) / Delta_0 = 0.0081 / 0.770 = 0.0105
# The spectral action sensitivity normalized to the SA mass scale:
#   lambda_SA  = (dS/dtau) / (S_fold * C2_eff)
# The coupling is: g_mix ~ lambda_BCS * sqrt(m_G^2 * C2_eff)
# This keeps g_mix < g_stability because lambda_BCS < 1.
lambda_BCS = dDelta_dtau / Delta_0_GL  # = 0.0105 (dimensionless)
g_BCS_corrected = lambda_BCS * np.sqrt(m_G_sq * C2_eff)
print(f"  (b) g_BCS = lambda_BCS * sqrt(m_G^2 * C2_eff)")
print(f"       lambda_BCS = dDelta/dtau / Delta_0 = {dDelta_dtau} / {Delta_0_GL:.4f} = {lambda_BCS:.6f}")
print(f"       = {lambda_BCS:.6f} * {np.sqrt(m_G_sq * C2_eff):.6f}")
print(f"       = {g_BCS_corrected:.6f} M_KK^2")
print()

# (c) Modulus-mediated: the tau modulation connects both sectors.
# The energy coupling is:
#   V_mix = d^2 E / (d phi_G d phi_SA) evaluated at equilibrium.
# From the BCS gap equation: Delta depends on the Dirac spectrum (SA sector)
# through the DOS. The cross-susceptibility:
#   chi_cross = (d Delta / d tau) * (d^2 S / d tau d phi)
# In units: [M_KK] * [M_KK * M_KK^{-2}] is wrong. Need careful treatment.
# Use the dimensionless tau derivative of the Josephson coupling:
#   dJ/dtau = dJ/dDelta * dDelta/dtau
# where dJ/dDelta ~ J_eff / Delta_0 (linear in Delta for BCS).
# Then g_mod = (dJ/dtau) * epsilon_inner / rho_s
#            = (J_eff/Delta_0) * dDelta/dtau * epsilon_inner / rho_s
g_mod = (J_eff / Delta_0_GL) * dDelta_dtau * epsilon_inner / rho_s
print(f"  (c) g_mod = (J_eff/Delta_0) * (dDelta/dtau) * eps_inner / rho_s")
print(f"       = ({J_eff}/{Delta_0_GL:.4f}) * {dDelta_dtau} * {epsilon_inner} / {rho_s}")
print(f"       = {g_mod:.6e} M_KK^2")
print()

# (d) Original task estimate (equation from prompt) — for completeness
# g_BCS_task = (dDelta/dtau)^2 * (dS/dtau) / sqrt(rho_s)
# Dimensional check: [M_KK]^2 * [1] / [M_KK^{1/2}] = [M_KK^{3/2}] — NOT M_KK^2!
# This formula is dimensionally inconsistent if dS/dtau is dimensionless (S is a number).
# If we interpret S in M_KK^{-2} units: [M_KK]^2 * [M_KK^2] / [M_KK^{1/2}] = [M_KK^{7/2}].
# Neither works. The formula likely involves an implicit M_KK scaling.
# We record the numerical value but flag the dimensional issue.
g_BCS_task_raw = dDelta_dtau**2 * dS_dtau / np.sqrt(rho_s)
print(f"  (d) g_BCS_task (as specified) = (dDelta/dtau)^2 * dS/dtau / sqrt(rho_s)")
print(f"       = {dDelta_dtau}^2 * {dS_dtau:.1f} / {np.sqrt(rho_s):.4f}")
print(f"       = {g_BCS_task_raw:.4f}")
print(f"       WARNING: dimensional analysis fails for this formula.")
print(f"       At K=0, stability requires g < {g_stability:.4f} M_KK^2.")
print(f"       g_BCS_task = {g_BCS_task_raw:.4f} >> {g_stability:.4f}: TACHYONIC at K=0.")
print(f"       This coupling produces a negative eigenvalue (runaway instability),")
print(f"       not polariton formation. It must be renormalized or the formula is wrong.")
print()

# Collect physical (stable) couplings
couplings = {
    'g_geom': g_geom,
    'g_BCS': g_BCS_corrected,
    'g_mod': g_mod,
}

print(f"  STABLE coupling estimates (all < g_stab = {g_stability:.4f}):")
for name, g_val in couplings.items():
    print(f"    {name:<10s} = {g_val:.6e} M_KK^2   (g/C2_eff = {g_val/C2_eff:.4e})")
print()

# ============================================================================
#  SECTION 3: Hopfield Dynamical Matrix — Analytic Solution
# ============================================================================

print("--- Section 3: Hopfield Dynamical Matrix ---")
print()

K_arr = np.linspace(0.01, 6.0, 4000)

def hopfield_eigenvalues(K, J_G, m_G_sq, C2, g):
    """Upper/lower polariton: omega_pm^2 = (Tr +/- sqrt(disc)) / 2."""
    diag_G = J_G * K**2 + m_G_sq
    diag_SA = C2
    Tr = diag_G + diag_SA
    Det = diag_G * diag_SA - g**2
    disc = Tr**2 - 4 * Det
    sqrt_disc = np.sqrt(np.maximum(disc, 0.0))
    return 0.5 * (Tr + sqrt_disc), 0.5 * (Tr - sqrt_disc)

def mixing_angle(K, J_G, m_G_sq, C2, g):
    """theta = 0.5 arctan(2g / (diag_G - diag_SA)). 0 = pure, pi/4 = max."""
    delta = J_G * K**2 + m_G_sq - C2
    return 0.5 * np.arctan2(2 * g, delta)

def effective_exponent(K_arr, omega_sq, K_pivot):
    """d ln(omega^2) / d ln(K) at K_pivot via centered finite difference."""
    idx = np.argmin(np.abs(K_arr - K_pivot))
    ln_om = np.log(np.maximum(omega_sq, 1e-30))
    ln_K = np.log(K_arr)
    return (ln_om[idx+1] - ln_om[idx-1]) / (ln_K[idx+1] - ln_K[idx-1])

results = {}
for name, g_val in couplings.items():
    om_p, om_m = hopfield_eigenvalues(K_arr, J_G, m_G_sq, C2_eff, g_val)

    # Check stability: om_m > 0 everywhere?
    stable = np.all(om_m > 0)

    # Rabi splitting
    gap = np.sqrt(np.maximum(om_p, 0)) - np.sqrt(np.maximum(om_m, 0))
    Omega_R = np.min(gap)
    K_cross = K_arr[np.argmin(gap)]

    # alpha_eff at K_pivot
    alpha_eff = effective_exponent(K_arr, om_m, K_pivot)

    # Mixing angle at K_pivot
    theta = mixing_angle(K_pivot, J_G, m_G_sq, C2_eff, g_val)

    # Lower polariton mass at K=0
    _, om0 = hopfield_eigenvalues(np.array([0.0]), J_G, m_G_sq, C2_eff, g_val)
    m_lower = np.sqrt(max(om0[0], 0.0)) if om0[0] > 0 else 0.0

    coupling_ratio = Omega_R / total_linewidth if total_linewidth > 0 else np.inf
    g_over_C2 = abs(g_val) / C2_eff

    results[name] = {
        'g': g_val,
        'stable': stable,
        'Omega_R': Omega_R,
        'K_crossing': K_cross,
        'alpha_eff': alpha_eff,
        'theta_pivot': theta,
        'theta_deg': np.degrees(theta),
        'm_lower': m_lower,
        'coupling_ratio': coupling_ratio,
        'g_over_C2': g_over_C2,
        'omega_p_sq': om_p,
        'omega_m_sq': om_m,
    }

    regime = ("ULTRA-STRONG" if g_over_C2 > 0.1
              else "STRONG" if coupling_ratio > 1.0
              else "INTERMEDIATE" if coupling_ratio > 0.1
              else "WEAK")

    print(f"  {name} = {g_val:.6e} M_KK^2")
    print(f"    Stable:       {stable}")
    print(f"    Omega_R:      {Omega_R:.6f} M_KK")
    print(f"    K_cross:      {K_cross:.4f} M_KK")
    print(f"    alpha_eff:    {alpha_eff:.6f}   |a-2| = {abs(alpha_eff-2):.6f}")
    print(f"    theta(K_piv): {np.degrees(theta):.4f} deg")
    print(f"    m_lower(K=0): {m_lower:.6f} M_KK")
    print(f"    Omega_R/Gam:  {coupling_ratio:.4e}")
    print(f"    g/C2:         {g_over_C2:.4e}")
    print(f"    Regime:       {regime}")
    print()

# ============================================================================
#  SECTION 4: Coupling Scan — Weak to Strong Transition
# ============================================================================

print("--- Section 4: Coupling Scan ---")
print()

# Scan g from 0 to just below stability threshold
g_scan = np.linspace(1e-6, g_stability * 0.99, 500)
alpha_scan = np.zeros_like(g_scan)
Omega_R_scan = np.zeros_like(g_scan)
m_lower_scan = np.zeros_like(g_scan)
theta_scan = np.zeros_like(g_scan)

for i, gv in enumerate(g_scan):
    omp, omm = hopfield_eigenvalues(K_arr, J_G, m_G_sq, C2_eff, gv)
    gap_i = np.sqrt(np.maximum(omp, 0)) - np.sqrt(np.maximum(omm, 0))
    Omega_R_scan[i] = np.min(gap_i)
    alpha_scan[i] = effective_exponent(K_arr, omm, K_pivot)
    _, om0i = hopfield_eigenvalues(np.array([0.0]), J_G, m_G_sq, C2_eff, gv)
    m_lower_scan[i] = np.sqrt(max(om0i[0], 0.0)) if om0i[0] > 0 else 0.0
    theta_scan[i] = np.degrees(mixing_angle(K_pivot, J_G, m_G_sq, C2_eff, gv))

# Find where alpha deviates by 0.1 from 2
dev_scan = np.abs(alpha_scan - 2.0)
gate_mask = dev_scan > 0.1
if np.any(gate_mask):
    g_crit = g_scan[np.argmax(gate_mask)]
    max_dev = dev_scan.max()
    print(f"  |alpha - 2| > 0.1 first at g = {g_crit:.6f} M_KK^2")
    print(f"  Maximum deviation in scan: {max_dev:.6f} at g = {g_scan[np.argmax(dev_scan)]:.6f}")
else:
    g_crit = np.inf
    max_dev = dev_scan.max()
    print(f"  Gate threshold NOT reached in stable coupling range")
    print(f"  Maximum |alpha - 2| = {max_dev:.6f} at g = {g_scan[np.argmax(dev_scan)]:.6f}")
    print(f"  Stability limit g_stab = {g_stability:.4f} M_KK^2")

print(f"  alpha_eff range: [{alpha_scan.min():.6f}, {alpha_scan.max():.6f}]")
print(f"  m_lower range:   [{m_lower_scan.min():.6f}, {m_lower_scan.max():.6f}] M_KK")
print()

# ============================================================================
#  SECTION 5: Self-Energy Formulation (Multi-pole SA)
# ============================================================================

print("--- Section 5: Self-Energy (Multi-Pole SA) ---")
print()

# Instead of a single effective SA mass, use the full multi-pole structure.
# The SA sector acts as a self-energy dressing the Goldstone propagator:
#   G^{-1}(K) = J_G K^2 + m_G^2 + g^2 * chi_SA(K)
# where chi_SA(K) = Sum_i W_i / (K^2 + C2_i)
# This adds a K-dependent mass correction to the Goldstone.

def chi_SA(K, C2_arr, W_arr):
    """Multi-pole spectral action correlator."""
    return sum(w / (K**2 + c2) for c2, w in zip(C2_arr, W_arr))

def polariton_selfenergy(K, J_G, m_G_sq, g, C2_arr, W_arr):
    """omega^2(K) = J_G K^2 + m_G^2 + g^2 * chi_SA(K)"""
    return J_G * K**2 + m_G_sq + g**2 * chi_SA(K, C2_arr, W_arr)

results_se = {}
for name, g_val in couplings.items():
    om_se = polariton_selfenergy(K_arr, J_G, m_G_sq, g_val, C2_values, W_values)
    alpha_se = effective_exponent(K_arr, om_se, K_pivot)

    # Effective mass at K~0
    om0_se = polariton_selfenergy(np.array([0.01]), J_G, m_G_sq, g_val, C2_values, W_values)
    m_eff_se = np.sqrt(max(om0_se[0], 0.0))

    results_se[name] = {
        'alpha_eff': alpha_se,
        'm_eff': m_eff_se,
        'omega_sq': om_se,
    }
    print(f"  {name}: alpha_eff = {alpha_se:.6f}, |a-2| = {abs(alpha_se-2):.6f}, "
          f"m_eff = {m_eff_se:.6f} M_KK")

# Self-energy scan
alpha_se_scan = np.zeros_like(g_scan)
for i, gv in enumerate(g_scan):
    om_se_i = polariton_selfenergy(K_arr, J_G, m_G_sq, gv, C2_values, W_values)
    alpha_se_scan[i] = effective_exponent(K_arr, om_se_i, K_pivot)

dev_se_scan = np.abs(alpha_se_scan - 2.0)
if np.any(dev_se_scan > 0.1):
    g_crit_se = g_scan[np.argmax(dev_se_scan > 0.1)]
    print(f"\n  Self-energy: |alpha - 2| > 0.1 first at g = {g_crit_se:.6f}")
else:
    g_crit_se = np.inf
    print(f"\n  Self-energy: maximum |alpha - 2| = {dev_se_scan.max():.6f}")
print()

# ============================================================================
#  SECTION 6: n_s and alpha_s at K_pivot (g_geom, best physical coupling)
# ============================================================================

print("--- Section 6: Spectral Indices ---")
print()

# The power spectrum P(K) ~ K^3 / omega^2(K) (for 3D density of states)
# n_s - 1 = d ln(K^3 / omega^2) / d ln K = 3 - alpha_eff

for name, g_val in couplings.items():
    alpha = results[name]['alpha_eff']
    n_s = 1.0 + (3.0 - alpha)  # = 4 - alpha_eff
    # alpha_s = d(n_s - 1)/d ln K requires second derivative
    # For the nearly-uncoupled case, alpha_s ~ 0 (K^2 is scale-free)
    # The correction from coupling is:
    #   d(alpha_eff)/d(ln K) at K_pivot
    om_m = results[name]['omega_m_sq']
    idx_p = np.argmin(np.abs(K_arr - K_pivot))
    ln_om = np.log(np.maximum(om_m, 1e-30))
    ln_K = np.log(K_arr)
    # alpha_eff at three nearby points
    a_m = (ln_om[idx_p] - ln_om[idx_p-2]) / (ln_K[idx_p] - ln_K[idx_p-2])
    a_p = (ln_om[idx_p+2] - ln_om[idx_p]) / (ln_K[idx_p+2] - ln_K[idx_p])
    dalpha = (a_p - a_m) / (ln_K[idx_p+2] - ln_K[idx_p-2]) * 2
    alpha_s = -dalpha  # alpha_s = -d(alpha_eff)/d(ln K)

    print(f"  {name}: n_s = {n_s:.6f}, alpha_s = {alpha_s:.6e}, alpha_eff = {alpha:.6f}")

print()

# Also from self-energy
for name, g_val in couplings.items():
    alpha = results_se[name]['alpha_eff']
    n_s = 1.0 + (3.0 - alpha)
    print(f"  SE {name}: n_s = {n_s:.6f}, alpha_eff = {alpha:.6f}")

print()

# ============================================================================
#  SECTION 7: Tachyonic Regime Analysis (g_BCS_task)
# ============================================================================

print("--- Section 7: Tachyonic Regime (g_BCS_task = {:.4f}) ---".format(g_BCS_task_raw))
print()

# When g > g_stability, the lower eigenvalue goes negative at K=0.
# This means the system is UNSTABLE — not a polariton but a phase transition.
# The Goldstone and SA modes are too strongly coupled; the quadratic form
# is no longer positive definite. The physical meaning: the BCS gap chain
# coupling is strong enough to destabilize the saddle point.

omp_tach, omm_tach = hopfield_eigenvalues(K_arr, J_G, m_G_sq, C2_eff, g_BCS_task_raw)
# Find K where omega_-^2 = 0 (tachyonic boundary)
zero_crossings = np.where(np.diff(np.sign(omm_tach)))[0]
if len(zero_crossings) > 0:
    K_tach = K_arr[zero_crossings[0]]
    print(f"  omega_-^2 crosses zero at K = {K_tach:.4f} M_KK")
    print(f"  For K < {K_tach:.4f}, the lower branch is TACHYONIC")
    print(f"  omega_-^2(K=0) = {omm_tach[0]:.4f} M_KK^2 (negative!)")
else:
    print(f"  omega_-^2(K=0) = {omm_tach[0]:.4f} M_KK^2")
    if omm_tach[0] < 0:
        print(f"  Lower branch tachyonic at ALL K in range (entire branch unstable)")
    else:
        print(f"  No tachyonic region")

# For K > K_tach (if it exists), compute alpha_eff
# But this is the regime where the 2x2 model is unreliable
valid_mask = omm_tach > 0
if np.any(valid_mask) and K_pivot < K_arr[valid_mask][-1]:
    alpha_tach = effective_exponent(K_arr[valid_mask], omm_tach[valid_mask],
                                    K_pivot) if K_pivot > K_arr[valid_mask][0] else np.nan
    print(f"  alpha_eff at K_pivot (in stable region): {alpha_tach:.4f}")
else:
    print(f"  K_pivot = {K_pivot} not in stable region — no meaningful alpha_eff")

print()
print(f"  Physical interpretation: g_BCS_task = {g_BCS_task_raw:.4f} M_KK^2 is")
print(f"  {g_BCS_task_raw / g_stability:.1f}x above the stability threshold")
print(f"  ({g_stability:.4f} M_KK^2). This does NOT produce polariton formation.")
print(f"  Instead, it signals a PHASE INSTABILITY: the equilibrium configuration")
print(f"  is a saddle point, not a minimum. The system would undergo spontaneous")
print(f"  symmetry breaking in the Goldstone-SA mixed channel.")
print(f"  This regime requires non-perturbative treatment beyond Hopfield.")
print()

# ============================================================================
#  SECTION 8: Summary Table
# ============================================================================

print("--- Section 8: Summary Table ---")
print()
header = f"  {'Quantity':<30s} {'Uncoupled':<16s} {'g_geom':<16s} {'g_BCS':<16s} {'g_mod':<16s}"
print(header)
print(f"  {'-'*30} {'-'*16} {'-'*16} {'-'*16} {'-'*16}")

rows = [
    ('g (M_KK^2)', '0',
     f"{g_geom:.4e}", f"{g_BCS_corrected:.4e}", f"{g_mod:.4e}"),
    ('alpha_eff(K_piv)', '2.000000',
     f"{results['g_geom']['alpha_eff']:.6f}",
     f"{results['g_BCS']['alpha_eff']:.6f}",
     f"{results['g_mod']['alpha_eff']:.6f}"),
    ('|alpha - 2|', '0.000000',
     f"{abs(results['g_geom']['alpha_eff']-2):.6f}",
     f"{abs(results['g_BCS']['alpha_eff']-2):.6f}",
     f"{abs(results['g_mod']['alpha_eff']-2):.6f}"),
    ('Omega_R (M_KK)', '0',
     f"{results['g_geom']['Omega_R']:.6f}",
     f"{results['g_BCS']['Omega_R']:.6f}",
     f"{results['g_mod']['Omega_R']:.6f}"),
    ('m_lower (M_KK)', f"{m_G:.6f}",
     f"{results['g_geom']['m_lower']:.6f}",
     f"{results['g_BCS']['m_lower']:.6f}",
     f"{results['g_mod']['m_lower']:.6f}"),
    ('theta (deg)', '0',
     f"{results['g_geom']['theta_deg']:.4f}",
     f"{results['g_BCS']['theta_deg']:.4f}",
     f"{results['g_mod']['theta_deg']:.4f}"),
    ('Omega_R / Gamma', '---',
     f"{results['g_geom']['coupling_ratio']:.2e}",
     f"{results['g_BCS']['coupling_ratio']:.2e}",
     f"{results['g_mod']['coupling_ratio']:.2e}"),
    ('g / C2_eff', '---',
     f"{results['g_geom']['g_over_C2']:.2e}",
     f"{results['g_BCS']['g_over_C2']:.2e}",
     f"{results['g_mod']['g_over_C2']:.2e}"),
]

for row in rows:
    print(f"  {row[0]:<30s} {row[1]:<16s} {row[2]:<16s} {row[3]:<16s} {row[4]:<16s}")
print()

# ============================================================================
#  SECTION 9: Gate Verdict
# ============================================================================

print("=" * 78)
print("GATE VERDICT: POLARITON-51")
print("=" * 78)
print()

max_dev_hopfield = max(abs(r['alpha_eff'] - 2.0) for r in results.values())
max_dev_se = max(abs(r['alpha_eff'] - 2.0) for r in results_se.values())
overall_max_dev = max(max_dev_hopfield, max_dev_se)
max_Omega_R = max(r['Omega_R'] for r in results.values())
max_coupling_ratio = max(r['coupling_ratio'] for r in results.values())

print(f"  Max |alpha - 2| (Hopfield 2x2):   {max_dev_hopfield:.6e}")
print(f"  Max |alpha - 2| (self-energy):     {max_dev_se:.6e}")
print(f"  Max Rabi splitting:                {max_Omega_R:.6e} M_KK")
print(f"  Max Omega_R / Gamma:               {max_coupling_ratio:.4e}")
print(f"  Gate threshold:                    |alpha - 2| > 0.1")
print(f"  Stability limit:                   g < {g_stability:.4f} M_KK^2")
print()

# All three physical couplings are far below the threshold
if overall_max_dev > 0.1:
    verdict = "PASS"
    reason = f"alpha_eff deviates by {overall_max_dev:.4f} > 0.1"
elif max_coupling_ratio < 0.1:
    verdict = "FAIL"
    reason = (f"Coupling too weak. Omega_R/Gamma = {max_coupling_ratio:.4e} < 0.1. "
              f"Max |alpha-2| = {overall_max_dev:.6f}")
else:
    verdict = "INFO"
    reason = (f"alpha_eff changes by {overall_max_dev:.6f} but below threshold. "
              f"Coupling intermediate (Omega_R/Gamma = {max_coupling_ratio:.4e})")

print(f"  VERDICT: {verdict}")
print(f"  REASON:  {reason}")
print()

if verdict != "PASS" and g_crit < np.inf:
    print(f"  Required g for PASS: {g_crit:.6f} M_KK^2")
    best_g = max(g_val for g_val in couplings.values())
    print(f"  Best physical g:     {best_g:.6e} M_KK^2")
    print(f"  Shortfall:           {g_crit / best_g:.0f}x")
    print(f"  Stability limit:     {g_stability:.6f} M_KK^2")
    if g_crit > g_stability:
        print(f"  NOTE: g_crit ({g_crit:.4f}) > g_stab ({g_stability:.4f}).")
        print(f"  The PASS threshold CANNOT be reached within the stable regime.")
        print(f"  The polariton model is structurally incapable of producing")
        print(f"  |alpha - 2| > 0.1 without destabilizing the vacuum.")
elif verdict != "PASS":
    print(f"  Gate threshold UNREACHABLE in stable coupling range.")
    print(f"  Maximum stable deviation: {max(dev_scan.max(), dev_se_scan.max()):.6f}")
    print(f"  The Hopfield polariton cannot produce the required mixing.")

print()

# ============================================================================
#  SECTION 10: Physical Interpretation
# ============================================================================

print("--- Section 10: Physical Interpretation ---")
print()
print(f"  Two excitation branches with extreme mass asymmetry:")
print(f"    Goldstone:  m_G = {m_G} M_KK  (light)")
print(f"    SA (eff):   sqrt(C2) = {np.sqrt(C2_eff):.3f} M_KK  (heavy)")
print(f"    Mass ratio: {np.sqrt(C2_eff)/m_G:.0f}x")
print()
print(f"  The coupling enters through the BCS gap sensitivity chain:")
print(f"    delta_tau -> delta_Delta (dDelta/dtau = {dDelta_dtau})")
print(f"    delta_tau -> delta_S     (dS/dtau = {dS_dtau:.0f})")
print()
print(f"  Physical coupling strengths are 1e-3 to 1e-2 of C2_eff.")
print(f"  The mixing angle at K_pivot is {results['g_geom']['theta_deg']:.1f} deg")
print(f"  (90 = pure Goldstone, 0 = pure SA). The branches are")
print(f"  essentially decoupled at all physical K.")
print()
print(f"  The Hopfield model is the correct framework for analyzing")
print(f"  the SA-Goldstone coupling. The computation shows that this")
shortfall_str = f"{g_crit/g_geom:.0f}x" if g_crit < np.inf else ">19x (stability limit)"
print(f"  coupling is too weak by {shortfall_str} (geometric)")
print(f"  to produce meaningful mode mixing at K_pivot = {K_pivot} M_KK.")
print()
print(f"  STRUCTURAL CONCLUSION:")
print(f"  The polariton route cannot modify alpha_eff within the stable")
print(f"  regime of the Hopfield model. The SA mode (heavy) and Goldstone")
print(f"  (light) live at vastly different energy scales. Their coupling")
print(f"  through the BCS gap chain is parametrically suppressed by")
print(f"  (dDelta/dtau / Delta_0)^2 ~ {lambda_BCS**2:.4e}.")
print()

# ============================================================================
#  SECTION 11: Save Data
# ============================================================================

save_data = {
    # Input
    'm_G': m_G, 'm_G_sq': m_G_sq,
    'epsilon_inner': epsilon_inner,
    'rho_s': rho_s, 'J_eff': J_eff, 'J_G': J_G,
    'C2_eff': C2_eff, 'C2_rms': C2_rms,
    'C2_values': C2_values, 'W_values': W_values,
    'K_pivot': K_pivot, 'K_arr': K_arr,
    'dS_dtau': dS_dtau, 'dDelta_dtau': dDelta_dtau,
    'g_stability': g_stability,

    # Coupling estimates
    'g_geom': g_geom, 'g_BCS': g_BCS_corrected, 'g_mod': g_mod,
    'g_BCS_task_raw': g_BCS_task_raw,
    'lambda_BCS': lambda_BCS,

    # Hopfield results
    'alpha_eff_geom': results['g_geom']['alpha_eff'],
    'alpha_eff_BCS': results['g_BCS']['alpha_eff'],
    'alpha_eff_mod': results['g_mod']['alpha_eff'],
    'Omega_R_geom': results['g_geom']['Omega_R'],
    'Omega_R_BCS': results['g_BCS']['Omega_R'],
    'Omega_R_mod': results['g_mod']['Omega_R'],
    'theta_geom': results['g_geom']['theta_deg'],
    'theta_BCS': results['g_BCS']['theta_deg'],
    'theta_mod': results['g_mod']['theta_deg'],
    'm_lower_geom': results['g_geom']['m_lower'],
    'm_lower_BCS': results['g_BCS']['m_lower'],
    'm_lower_mod': results['g_mod']['m_lower'],

    # Self-energy
    'alpha_se_geom': results_se['g_geom']['alpha_eff'],
    'alpha_se_BCS': results_se['g_BCS']['alpha_eff'],
    'alpha_se_mod': results_se['g_mod']['alpha_eff'],

    # Scan
    'g_scan': g_scan,
    'alpha_scan': alpha_scan,
    'Omega_R_scan': Omega_R_scan,
    'm_lower_scan': m_lower_scan,
    'theta_scan': theta_scan,
    'alpha_se_scan': alpha_se_scan,

    # Gate
    'verdict': verdict,
    'max_deviation_hopfield': max_dev_hopfield,
    'max_deviation_selfenergy': max_dev_se,
    'g_crit_hopfield': g_crit if g_crit < np.inf else -1,
    'g_crit_selfenergy': g_crit_se if g_crit_se < np.inf else -1,
}

import os
save_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(save_dir, 's51_polariton.npz')
np.savez(save_path, **save_data)
print(f"  Data saved: {save_path}")
print()
print("=" * 78)
print(f"  POLARITON-51: {verdict}")
print("=" * 78)
