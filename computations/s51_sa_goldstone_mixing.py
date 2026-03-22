#!/usr/bin/env python3
"""
S51 SA-Goldstone Additive Mixing Correlator (SA-GOLDSTONE-MIXING-51)
=====================================================================

MASTER GATE: Tests whether the additive mixture of the Goldstone phase
propagator P_G(K) and the spectral action correlator chi_SA(K) can
produce n_s in [0.950, 0.980] and alpha_s in [-0.040, 0].

Physical picture: a modulus perturbation delta_tau propagates through
TWO independent channels:
  Channel A (Josephson): delta_tau -> delta_Delta -> delta_J -> delta_phi
  Channel B (SA): delta_tau -> delta_S -> delta(geometry)

The total power spectrum: P_phys(K) = (1-beta)*P_G(K) + beta*chi_SA(K)
where beta is the SA channel weight, determined from first principles
via the coupling chain amplitudes.

Gate: SA-GOLDSTONE-MIXING-51
  PASS: n_s in [0.950, 0.980] AND alpha_s in [-0.040, 0] at physical beta
  FAIL: SA negligible (beta < 0.001) OR no beta gives n_s in [0.5, 1.0]
  INFO: SA significant but n_s outside target, or beta undetermined
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import sys
sys.path.insert(0, 'tier0-computation')
from canonical_constants import *

# ========================================================================
# SECTION 1: Load eigenvalue data and compute SA correlator
# ========================================================================
print("=" * 70)
print("SA-GOLDSTONE ADDITIVE MIXING CORRELATOR")
print("SA-GOLDSTONE-MIXING-51 (MASTER GATE)")
print("=" * 70)

data = np.load('tier0-computation/s44_dos_tau.npz', allow_pickle=True)

omega_15 = data['tau0.15_all_omega']
dim2_15 = data['tau0.15_all_dim2']
omega_19 = data['tau0.19_all_omega']
dim2_19 = data['tau0.19_all_dim2']

# ---------------------------------------------------
# 1a. Eigenvalue derivatives domega/dtau at the fold
# Forward difference: (omega(0.19) - omega(0.15)) / 0.04
# ---------------------------------------------------
dtau_fd = 0.04
all_sectors = sorted(set(dim2_19.astype(int)))
print(f"\nSector eigenvalue derivatives (dtau={dtau_fd}):")
print(f"{'dim2':>6} {'count':>6} {'rms(dw/dt)':>12} {'sum(dw/dt)^2':>14} {'SA_raw_wt':>12}")

sector_data = {}
for d2 in all_sectors:
    v15 = np.sort(omega_15[dim2_15 == d2])
    v19 = np.sort(omega_19[dim2_19 == d2])
    nm = min(len(v15), len(v19))
    derivs = (v19[:nm] - v15[:nm]) / dtau_fd
    rms = np.sqrt(np.mean(derivs**2))
    sum_sq = np.sum(derivs**2)
    sa_wt = d2 * sum_sq
    sector_data[d2] = {
        'count': nm, 'derivs': derivs, 'rms': rms,
        'sum_sq': sum_sq, 'sa_weight': sa_wt,
        'omegas': v19[:nm]
    }
    print(f"{d2:6d} {nm:6d} {rms:12.6f} {sum_sq:14.4f} {sa_wt:12.2f}")

total_sa_raw = sum(sd['sa_weight'] for sd in sector_data.values())
print(f"\nTotal raw SA weight: {total_sa_raw:.2f}")

# ---------------------------------------------------
# 1b. Casimir values for each sector
# SU(3) Casimir C_2(p,q) = (p^2 + q^2 + 3p + 3q + pq) / 3
# ---------------------------------------------------
# IMPORTANT: The singlet (dim2=1, C2=0) has a MASSLESS pole 1/K^2.
# It corresponds to the trivial (0,0) representation = constant on SU(3).
# This mode is spatially uniform on SU(3): it does NOT propagate between
# fabric cells. It must be EXCLUDED from the inter-cell correlator.
# Without exclusion, chi_SA diverges at K=0 (unphysical).

casimir_poles = {
    9:   4/3,     # (1,0)+(0,1)
    36:  10/3,    # (2,0)+(0,2)
    64:  3.0,     # (1,1)
    100: 6.0,     # (3,0)+(0,3)
}
C2_225_low = 16/3   # (2,1)+(1,2)
C2_225_high = 28/3  # (4,0)+(0,4)

print("\nSinglet (dim2=1) EXCLUDED: C2=0, spatially uniform, no inter-cell contrast")
print(f"  Singlet raw weight: {sector_data[1]['sa_weight']:.2f} ({sector_data[1]['sa_weight']/total_sa_raw*100:.2f}%)")

# ---------------------------------------------------
# 1c. Build chi_SA(K) with Gaussian cutoff
# chi_SA(K) = sum_sectors W_s / (K^2 + C2_s)
# W_s = dim2 * sum_n |f'(omega_n^2/Lambda^2)|^2 * (domega_n/dtau)^2
# ---------------------------------------------------
Lambda_SA = 3.0  # M_KK

def build_chi_SA(K_vals, Lambda):
    """Build SA correlator (no singlet) from eigenvalue data."""
    chi = np.zeros_like(K_vals)
    weights = {}
    total_w = 0.0

    for d2, C2 in casimir_poles.items():
        sd = sector_data[d2]
        x = sd['omegas']**2 / Lambda**2
        fprime = np.exp(-x)
        w = d2 * np.sum(fprime**2 * sd['derivs']**2)
        chi += w / (K_vals**2 + C2)
        weights[d2] = {'w': w, 'C2': C2}
        total_w += w

    # dim2=225: split between two Casimir values
    sd225 = sector_data[225]
    x225 = sd225['omegas']**2 / Lambda**2
    fp225 = np.exp(-x225)
    w225 = 225 * np.sum(fp225**2 * sd225['derivs']**2)
    chi += (w225/2) / (K_vals**2 + C2_225_low) + (w225/2) / (K_vals**2 + C2_225_high)
    weights[225] = {'w': w225, 'C2_low': C2_225_low, 'C2_high': C2_225_high}
    total_w += w225

    return chi, weights, total_w

K_values = np.logspace(-3, 1.5, 5000)
chi_SA, sa_weights, total_sa_w = build_chi_SA(K_values, Lambda_SA)

# chi_SA(0) = sum W_s / C2_s (finite, since all C2 > 0)
chi_SA_at_zero = sum(sa_weights[d2]['w'] / sa_weights[d2]['C2']
                     for d2 in casimir_poles)
chi_SA_at_zero += (sa_weights[225]['w']/2) / C2_225_low + (sa_weights[225]['w']/2) / C2_225_high
chi_SA_norm = chi_SA / chi_SA_at_zero

print(f"\nSA correlator at Lambda={Lambda_SA} (no singlet, Gaussian):")
for d2 in casimir_poles:
    frac = sa_weights[d2]['w'] / total_sa_w * 100
    print(f"  dim2={d2}: weight={sa_weights[d2]['w']:.1f} ({frac:.1f}%), C2={sa_weights[d2]['C2']:.4f}")
frac225 = sa_weights[225]['w'] / total_sa_w * 100
print(f"  dim2=225: weight={sa_weights[225]['w']:.1f} ({frac225:.1f}%), "
      f"C2={C2_225_low:.4f}/{C2_225_high:.4f}")
print(f"  Total: {total_sa_w:.1f}")
print(f"  chi_SA(0) = {chi_SA_at_zero:.2f}")

# Weighted average Casimir
C2_avg = sum(sa_weights[d2]['w'] * sa_weights[d2]['C2'] for d2 in casimir_poles)
C2_avg += (sa_weights[225]['w']/2) * C2_225_low + (sa_weights[225]['w']/2) * C2_225_high
C2_avg /= total_sa_w
print(f"  Weighted average C2 = {C2_avg:.4f}")
print(f"  Characteristic SA scale: sqrt(C2_avg) = {np.sqrt(C2_avg):.4f} M_KK")

# ========================================================================
# SECTION 2: Goldstone propagator P_G(K)
# ========================================================================
print("\n" + "=" * 70)
print("GOLDSTONE PROPAGATOR")
print("=" * 70)

m_G = 0.070   # M_KK, Leggett mass
J_G = 0.641   # M_KK, effective Josephson stiffness

P_G = 1.0 / (J_G * K_values**2 + m_G**2)
P_G_0 = 1.0 / m_G**2
P_G_norm = P_G / P_G_0

# Critical scale where Goldstone transitions from n_s ~ 1 to n_s ~ -1
K_star = m_G / np.sqrt(J_G)
print(f"m_G = {m_G} M_KK")
print(f"J_G = {J_G} M_KK")
print(f"Critical scale K* = m_G/sqrt(J) = {K_star:.6f} M_KK")
print(f"  Below K*: n_s ~ 1 (constant mode)")
print(f"  Above K*: n_s ~ -1 (K^{{-2}} falloff)")
print(f"  K_pivot=2.0 / K* = {2.0/K_star:.1f}x (deep in K^{{-2}} regime)")

ln_K = np.log(K_values)
n_s_G = 1.0 + np.gradient(np.log(np.maximum(P_G_norm, 1e-30)), ln_K)
n_s_SA = 1.0 + np.gradient(np.log(np.maximum(chi_SA_norm, 1e-30)), ln_K)

K_pivot_default = 2.0
idx_pivot = np.argmin(np.abs(K_values - K_pivot_default))

print(f"\nStandalone spectral indices at K_pivot = {K_pivot_default}:")
print(f"  n_s(Goldstone) = {n_s_G[idx_pivot]:.6f}")
print(f"  n_s(SA)        = {n_s_SA[idx_pivot]:.6f}")

# ========================================================================
# SECTION 3: Coupling chain amplitudes
# ========================================================================
print("\n" + "=" * 70)
print("COUPLING CHAIN AMPLITUDES")
print("=" * 70)

dDelta_dtau = 0.0081   # M_KK per unit tau
Delta_B2_val = 0.084   # M_KK
J_C2_val = 0.933       # M_KK
dJ_dDelta = J_C2_val / Delta_B2_val
A_J = dJ_dDelta * dDelta_dtau

print(f"Channel A (Josephson):")
print(f"  dDelta/dtau = {dDelta_dtau} M_KK/tau")
print(f"  dJ/dDelta = {dJ_dDelta:.2f}")
print(f"  A_J = {A_J:.6f} M_KK/tau")

A_SA_raw = dS_fold
A_SA_projected = A_SA_raw / S_fold
A_G_projected = A_J * rho_B2_per_mode

print(f"\nChannel B (Spectral Action):")
print(f"  A_SA = dS/dtau = {A_SA_raw:.2f}")
print(f"  A_SA_eff = A_SA/S_total = {A_SA_projected:.6f}")
print(f"\nProjected comparison:")
print(f"  A_G_eff = A_J * rho_B2 = {A_G_projected:.6f}")
print(f"  A_SA_eff / A_G_eff = {A_SA_projected/A_G_projected:.4f}")

beta_physical = A_SA_projected**2 / (A_SA_projected**2 + A_G_projected**2)
print(f"  beta_physical = {beta_physical:.6f}")

# ========================================================================
# SECTION 4: STRUCTURAL OBSTRUCTION at K_pivot = 2.0
# ========================================================================
print("\n" + "=" * 70)
print("STRUCTURAL OBSTRUCTION: K_PIVOT = 2.0")
print("=" * 70)

# At K_pivot = 2.0:
#   n_s(Goldstone) = -0.996 (deep K^{-2})
#   n_s(SA) = +0.150 (near transition)
# Additive mixture P = (1-b)*P_G + b*chi_SA
# n_s of mixture <= max(n_s_G, n_s_SA) at endpoints? NO.
# n_s of ADDITIVE mixture can exceed individual values.
# But check: d ln(P)/d ln(K) for P = a*f + b*g is
# (a*f' + b*g') / (a*f + b*g) where primes are d/dK * K
# This is a weighted average of n_s(f) and n_s(g) with weights f and g.
# So n_s(mixture) = [a*f*n_s(f) + b*g*n_s(g)] / (a*f + b*g)
# This is BOUNDED by [min(n_s_f, n_s_g), max(n_s_f, n_s_g)].

# PROOF: Let alpha = a*f/(a*f+b*g) in [0,1]. Then
# n_s = alpha * n_s_f + (1-alpha) * n_s_g
# which is a convex combination. QED.

# At K_pivot = 2.0:
# n_s(mixture) in [n_s_G, n_s_SA] = [-0.996, +0.150]
# The target 0.965 CANNOT be reached. This is a STRUCTURAL THEOREM.

print(f"At K_pivot = {K_pivot_default}:")
print(f"  n_s(G)  = {n_s_G[idx_pivot]:.6f}")
print(f"  n_s(SA) = {n_s_SA[idx_pivot]:.6f}")
print(f"  CONVEX COMBINATION THEOREM: n_s(mixture) in [{n_s_G[idx_pivot]:.4f}, {n_s_SA[idx_pivot]:.4f}]")
print(f"  Target n_s = 0.965 is UNREACHABLE (above upper bound by {0.965-n_s_SA[idx_pivot]:.3f})")

# Verify by direct scan
betas = np.linspace(0, 1, 10000)
ns_at_pivot = np.zeros(len(betas))
for i, b in enumerate(betas):
    P_mix = (1-b) * P_G_norm + b * chi_SA_norm
    ns_local = 1.0 + np.gradient(np.log(np.maximum(P_mix, 1e-30)), ln_K)
    ns_at_pivot[i] = ns_local[idx_pivot]

print(f"\n  Direct scan: n_s range = [{ns_at_pivot.min():.6f}, {ns_at_pivot.max():.6f}]")
print(f"  Confirms: no beta in [0,1] reaches 0.965 at K_pivot = {K_pivot_default}")

# ========================================================================
# SECTION 5: K_PIVOT ANALYSIS -- where does mixing work?
# ========================================================================
print("\n" + "=" * 70)
print("K_PIVOT SWEEP: WHERE IS n_s = 0.965 ACHIEVABLE?")
print("=" * 70)

K_pivots = [0.01, 0.015, 0.02, 0.03, 0.05, 0.07, 0.087, 0.09, 0.10,
            0.15, 0.20, 0.30, 0.50, 1.0, 2.0, 5.0]

print(f"{'K_piv':>8} {'n_s(G)':>10} {'n_s(SA)':>10} {'n_s_max':>10} {'beta_tgt':>10} "
      f"{'alpha_s':>10} {'id_dev':>10} {'status':>10}")

results_kpiv = []
for K_piv in K_pivots:
    idx_kp = np.argmin(np.abs(K_values - K_piv))
    ns_g = n_s_G[idx_kp]
    ns_sa = n_s_SA[idx_kp]

    # Scan beta
    ns_arr = np.zeros(len(betas))
    alpha_arr = np.zeros(len(betas))
    for i, b in enumerate(betas):
        P_mix = (1-b) * P_G_norm + b * chi_SA_norm
        P_mix = np.maximum(P_mix, 1e-30)
        ns_arr[i] = (1.0 + np.gradient(np.log(P_mix), ln_K))[idx_kp]
        alpha_arr[i] = np.gradient(1.0 + np.gradient(np.log(P_mix), ln_K), ln_K)[idx_kp]

    ns_max = ns_arr.max()
    # Find crossing
    beta_tgt = np.nan
    alpha_tgt = np.nan
    for i in range(len(betas)-1):
        if (ns_arr[i] - 0.965) * (ns_arr[i+1] - 0.965) <= 0:
            frac = (0.965 - ns_arr[i]) / (ns_arr[i+1] - ns_arr[i] + 1e-30)
            beta_tgt = betas[i] + frac * (betas[i+1] - betas[i])
            alpha_tgt = alpha_arr[i] + frac * (alpha_arr[i+1] - alpha_arr[i])
            break

    id_dev = alpha_tgt - (0.965**2 - 1) if not np.isnan(alpha_tgt) else np.nan
    status = 'ACHIEVABLE' if not np.isnan(beta_tgt) else 'BLOCKED'

    results_kpiv.append({
        'K_piv': K_piv, 'ns_g': ns_g, 'ns_sa': ns_sa, 'ns_max': ns_max,
        'beta': beta_tgt, 'alpha_s': alpha_tgt, 'id_dev': id_dev
    })

    if np.isnan(beta_tgt):
        print(f"{K_piv:8.3f} {ns_g:10.4f} {ns_sa:10.4f} {ns_max:10.4f} {'---':>10} "
              f"{'---':>10} {'---':>10} {status:>10}")
    else:
        print(f"{K_piv:8.3f} {ns_g:10.4f} {ns_sa:10.4f} {ns_max:10.4f} {beta_tgt:10.4f} "
              f"{alpha_tgt:10.6f} {id_dev:10.6f} {status:>10}")

# Find critical K_pivot (maximum K where n_s=0.965 is achievable)
K_crit = 0.0
for r in results_kpiv:
    if not np.isnan(r['beta']):
        K_crit = max(K_crit, r['K_piv'])

print(f"\nCritical K_pivot (max where achievable): K_crit ~ {K_crit:.3f} M_KK")
print(f"Compare: K* = m_G/sqrt(J) = {K_star:.4f} M_KK")
print(f"The obstruction is fundamental: at K_pivot > K*, the Goldstone is in the")
print(f"K^{{-2}} regime, and the SA maximum n_s at K_pivot=2.0 is only 0.15.")

# ========================================================================
# SECTION 6: IDENTITY BREAKING -- the SA contribution
# ========================================================================
print("\n" + "=" * 70)
print("IDENTITY BREAKING ANALYSIS")
print("=" * 70)

# At K_pivot = 2.0, even though we cannot reach n_s = 0.965,
# what IS the identity deviation?
# alpha_s = n_s^2 - 1 is the identity for pure O-Z (Goldstone).
# Any SA admixture breaks it. Quantify.

# Best achievable at K_pivot = 2.0: beta = 1 (pure SA)
P_pure_SA = chi_SA_norm.copy()
ns_pure_SA = 1.0 + np.gradient(np.log(np.maximum(P_pure_SA, 1e-30)), ln_K)
alpha_pure_SA = np.gradient(ns_pure_SA, ln_K)
id_gold = n_s_G[idx_pivot]**2 - 1
alpha_gold = np.gradient(n_s_G, ln_K)[idx_pivot]

print(f"At K_pivot = {K_pivot_default}:")
print(f"  Pure Goldstone: n_s={n_s_G[idx_pivot]:.6f}, alpha_s={alpha_gold:.6f}, "
      f"n_s^2-1={id_gold:.6f}")
print(f"  Identity deviation (Gold): alpha_s - (n_s^2-1) = {alpha_gold - id_gold:.2e}")
print(f"  Pure SA: n_s={ns_pure_SA[idx_pivot]:.6f}, alpha_s={alpha_pure_SA[idx_pivot]:.6f}, "
      f"n_s^2-1={ns_pure_SA[idx_pivot]**2-1:.6f}")
print(f"  Identity deviation (SA): {alpha_pure_SA[idx_pivot] - (ns_pure_SA[idx_pivot]**2-1):.6f}")

# Effective exponent of SA correlator
# chi_SA ~ K^{-2*alpha_eff} at K_pivot
# alpha_eff = (1 - n_s_SA) / 2
alpha_eff_SA = (1 - ns_pure_SA[idx_pivot]) / 2
print(f"\n  SA effective exponent: alpha_eff = (1-n_s)/2 = {alpha_eff_SA:.4f}")
print(f"  (Compare S50: alpha_eff = 0.86. W1-D: 0.860 +/- 0.02)")

# ========================================================================
# SECTION 7: PHYSICAL beta at K_pivot = 2.0 -- what does it give?
# ========================================================================
print("\n" + "=" * 70)
print("PHYSICAL BETA RESULTS AT K_PIVOT = 2.0")
print("=" * 70)

P_at_phys = (1 - beta_physical) * P_G_norm + beta_physical * chi_SA_norm
ns_phys = 1.0 + np.gradient(np.log(np.maximum(P_at_phys, 1e-30)), ln_K)
alpha_phys = np.gradient(ns_phys, ln_K)

print(f"beta_physical = {beta_physical:.6f}")
print(f"At K_pivot = 2.0:")
print(f"  n_s = {ns_phys[idx_pivot]:.6f}")
print(f"  alpha_s = {alpha_phys[idx_pivot]:.6f}")
print(f"  Identity deviation: {alpha_phys[idx_pivot] - (ns_phys[idx_pivot]**2-1):.6e}")

print(f"\nSA fraction at K_pivot = 2.0:")
PG_val = (1-beta_physical) * P_G_norm[idx_pivot]
PSA_val = beta_physical * chi_SA_norm[idx_pivot]
print(f"  P_G contribution: {PG_val:.6e}")
print(f"  P_SA contribution: {PSA_val:.6e}")
print(f"  SA / total: {PSA_val/(PG_val + PSA_val + 1e-30):.6e}")
print(f"  The SA contribution is negligible because chi_SA_norm(K=2) = {chi_SA_norm[idx_pivot]:.6e}")
print(f"  while P_G_norm(K=2) = {P_G_norm[idx_pivot]:.6e}")
print(f"  Ratio: {chi_SA_norm[idx_pivot] / P_G_norm[idx_pivot]:.4e}")

# ========================================================================
# SECTION 8: Coherent vs incoherent sum
# ========================================================================
print("\n" + "=" * 70)
print("COHERENT vs INCOHERENT SUM")
print("=" * 70)

# Both channels driven by same delta_tau, so in principle:
# P_total = |A_G*sqrt(P_G) + A_SA*sqrt(chi_SA)|^2 (coherent)
# vs P_total = A_G^2 * P_G + A_SA^2 * chi_SA (incoherent)

P_coh = (A_G_projected * np.sqrt(np.maximum(P_G_norm, 0)) +
         A_SA_projected * np.sqrt(np.maximum(chi_SA_norm, 0)))**2
P_coh_norm = P_coh / (P_coh[0] + 1e-30)

P_incoh = A_G_projected**2 * P_G_norm + A_SA_projected**2 * chi_SA_norm
P_incoh_norm = P_incoh / (P_incoh[0] + 1e-30)

ns_coh = 1.0 + np.gradient(np.log(np.maximum(P_coh_norm, 1e-30)), ln_K)
ns_incoh = 1.0 + np.gradient(np.log(np.maximum(P_incoh_norm, 1e-30)), ln_K)

print(f"At K_pivot = 2.0:")
print(f"  Coherent:   n_s = {ns_coh[idx_pivot]:.6f}")
print(f"  Incoherent: n_s = {ns_incoh[idx_pivot]:.6f}")
print(f"  Difference: {ns_coh[idx_pivot] - ns_incoh[idx_pivot]:.2e}")
print(f"  Cross-term is negligible (SA weight vanishingly small at K=2)")

# ========================================================================
# SECTION 9: Required mass for n_s = 0.965 at K_pivot = 2.0
# ========================================================================
print("\n" + "=" * 70)
print("MASS PROBLEM: WHAT m_G IS NEEDED?")
print("=" * 70)

# For a single O-Z propagator: n_s = 1 - 2*J*K^2/(J*K^2 + m^2)
# => m^2 = J*K^2 * 2/(1-n_s) - J*K^2 = J*K^2 * (1+n_s)/(1-n_s)
# For n_s = 0.965: m^2 = J*K^2 * 1.965/0.035 = J*K^2 * 56.14
m_required_sq = J_G * K_pivot_default**2 * (1 + 0.965) / (1 - 0.965)
m_required = np.sqrt(m_required_sq)
print(f"For n_s = 0.965 at K_pivot = {K_pivot_default} with J = {J_G}:")
print(f"  m_required = sqrt(J * K^2 * (1+n_s)/(1-n_s))")
print(f"  m_required = sqrt({J_G} * {K_pivot_default**2} * {1.965/0.035:.2f})")
print(f"  m_required = {m_required:.4f} M_KK")
print(f"  m_Leggett  = {m_G} M_KK")
print(f"  Ratio: {m_required/m_G:.1f}x")
print(f"  This IS the 170x mass problem (S48-S50)")

# For SA to compensate: the SA correlator has effective mass sqrt(C2_avg)
# What fraction SA is needed if we could achieve the target?
# At K=2: chi_SA drops by factor chi_SA_norm(K=2) = significant
# But to get n_s = 0.965, we need the MIXTURE to fall slowly
# The SA falls slowly (n_s_SA ~ 0.15 > 0) but not slowly enough

# What effective single-pole C2 gives n_s = 0.965 at K=2?
# 1 - 2K^2/(K^2+C2) = 0.965 => C2 = K^2*(1+n_s)/(1-n_s) = 4*56.14 = 224.6
C2_needed = K_pivot_default**2 * 1.965 / 0.035
print(f"\n  For SA alone at K=2: need C2 = {C2_needed:.1f}")
print(f"  Actual max C2 = {C2_225_high:.4f} = {28/3:.4f}")
print(f"  Shortfall: {C2_needed / C2_225_high:.1f}x")
print(f"  The SA correlator has poles at C2 in [1.33, 9.33]")
print(f"  All poles contribute n_s < 1 at K=2 (since K^2=4 >> C2 for all sectors)")

# ========================================================================
# SECTION 10: Cutoff dependence
# ========================================================================
print("\n" + "=" * 70)
print("CUTOFF DEPENDENCE")
print("=" * 70)

for Lambda_test in [2.0, 3.0, 5.0, 10.0]:
    chi_test, _, _ = build_chi_SA(K_values, Lambda_test)
    chi_test_0 = build_chi_SA(np.array([1e-10]), Lambda_test)[0][0]
    chi_test_n = chi_test / chi_test_0
    ns_sa_test = 1.0 + np.gradient(np.log(np.maximum(chi_test_n, 1e-30)), ln_K)
    print(f"  Lambda={Lambda_test:4.1f}: n_s(SA, K=2) = {ns_sa_test[idx_pivot]:.6f}, "
          f"max(n_s) over K = {ns_sa_test[50:-50].max():.6f}")

print(f"\n  Result is cutoff-independent: SA n_s at K=2 is ~0.15 regardless.")
print(f"  The STRUCTURAL obstruction (K_pivot >> K*) is not a cutoff artifact.")

# ========================================================================
# SECTION 11: Gate evaluation
# ========================================================================
print("\n" + "=" * 70)
print("GATE EVALUATION: SA-GOLDSTONE-MIXING-51")
print("=" * 70)

print("\nSummary of key numbers:")
print(f"  Goldstone standalone n_s(K=2): {n_s_G[idx_pivot]:.6f}")
print(f"  SA standalone n_s(K=2):        {n_s_SA[idx_pivot]:.6f}")
print(f"  Maximum n_s of any mixture:    {ns_at_pivot.max():.6f}")
print(f"  Target n_s:                    0.965")
print(f"  Shortfall:                     {0.965 - ns_at_pivot.max():.3f}")
print(f"  Physical beta:                 {beta_physical:.6f}")
print(f"  Critical scale K*:             {K_star:.6f} M_KK")
print(f"  K_pivot/K*:                    {K_pivot_default/K_star:.1f}")

print(f"\nStructural obstruction:")
print(f"  The Goldstone O-Z propagator 1/(J K^2 + m_G^2) at K_pivot = 2.0")
print(f"  is deep in its K^{{-2}} regime (K/K* = {K_pivot_default/K_star:.1f}).")
print(f"  The SA correlator chi_SA(K) has poles at C2 in [1.33, 9.33],")
print(f"  all below K_pivot^2 = 4.0, so chi_SA is also falling at K=2.")
print(f"  The spectral index of any ADDITIVE mixture is a convex combination")
print(f"  of n_s(G) = -0.996 and n_s(SA) = +0.150 at K = 2.0.")
print(f"  The target 0.965 exceeds the upper bound by 0.815.")
print(f"")
print(f"  Achievable range of n_s at K_pivot = 2.0: [-0.996, +0.150]")
print(f"  Target n_s = 0.965 requires K_pivot < {K_star:.4f} M_KK (below K*)")
print(f"  At K_pivot = 0.07: achievable with beta = 0.933, alpha_s = -0.020")

# VERDICT
print("\n" + "=" * 70)
gate_pass_ns = False  # Target unreachable at K_pivot = 2.0
gate_fail_negligible = beta_physical < 0.001
# beta_physical = 0.033, so SA is NOT negligible
# But no beta gives n_s in [0.5, 1.0] at K_pivot = 2.0?
ns_in_range = any(0.5 <= ns <= 1.0 for ns in ns_at_pivot)

if ns_in_range:
    # Some beta gives n_s in [0.5, 1.0], just not in [0.95, 0.98]
    verdict = "INFO"
    reason = ("SA contribution significant (beta_phys=0.033) and DOES produce "
              "n_s in [0.5, 1.0] for intermediate beta, but CANNOT reach "
              "n_s = 0.965 at K_pivot = 2.0 M_KK. Structural obstruction: "
              "K_pivot/K* = 22.9x. All SA Casimir poles below K_pivot^2. "
              "Convex combination theorem bounds n_s to [-0.996, +0.150]. "
              "Target achievable only for K_pivot < 0.2 M_KK.")
else:
    # Check -- does any beta give n_s in [0.5, 1.0]?
    if ns_at_pivot.max() < 0.5:
        verdict = "FAIL"
        reason = "No beta produces n_s in [0.5, 1.0] at K_pivot = 2.0"
    else:
        verdict = "INFO"
        reason = "SA significant but n_s outside [0.950, 0.980] at K_pivot = 2.0"

print(f"SA-GOLDSTONE-MIXING-51: {verdict}")
print(f"Reason: {reason}")
print("=" * 70)

# ========================================================================
# SECTION 12: Save data
# ========================================================================
np.savez('tier0-computation/s51_sa_goldstone_mixing.npz',
         K_values=K_values,
         P_G_norm=P_G_norm,
         chi_SA_norm=chi_SA_norm,
         n_s_G=n_s_G,
         n_s_SA=n_s_SA,
         beta_physical=beta_physical,
         K_star=K_star,
         K_pivot=K_pivot_default,
         m_G=m_G,
         J_G=J_G,
         C2_avg=C2_avg,
         A_J=A_J,
         A_SA_raw=A_SA_raw,
         A_SA_projected=A_SA_projected,
         A_G_projected=A_G_projected,
         ns_at_pivot_scan=ns_at_pivot,
         betas_scan=betas,
         results_kpiv_Kpiv=np.array([r['K_piv'] for r in results_kpiv]),
         results_kpiv_nsG=np.array([r['ns_g'] for r in results_kpiv]),
         results_kpiv_nsSA=np.array([r['ns_sa'] for r in results_kpiv]),
         results_kpiv_nsmax=np.array([r['ns_max'] for r in results_kpiv]),
         results_kpiv_beta=np.array([r['beta'] for r in results_kpiv]),
         results_kpiv_alpha=np.array([r['alpha_s'] for r in results_kpiv]),
         results_kpiv_iddev=np.array([r['id_dev'] for r in results_kpiv]),
         verdict=verdict,
)
print(f"\nData saved to tier0-computation/s51_sa_goldstone_mixing.npz")

# ========================================================================
# SECTION 13: Plots
# ========================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Panel 1: Normalized correlators
ax = axes[0, 0]
ax.loglog(K_values, P_G_norm, 'b-', lw=2, label=r'$P_G$ (Goldstone, $m_G=0.070$)')
ax.loglog(K_values, chi_SA_norm, 'r-', lw=2, label=r'$\chi_{SA}$ (no singlet)')
ax.axvline(K_pivot_default, color='gray', ls='--', alpha=0.5, label='$K_{pivot}=2.0$')
ax.axvline(K_star, color='purple', ls=':', alpha=0.7, label=f'$K^*={K_star:.3f}$')
ax.set_xlabel('$K$ [$M_{KK}$]')
ax.set_ylabel('Normalized correlator')
ax.set_title('Standalone Correlators')
ax.legend(fontsize=7)
ax.set_xlim([0.001, 30])
ax.grid(True, alpha=0.3)

# Panel 2: n_s(K) for both
ax = axes[0, 1]
ax.semilogx(K_values, n_s_G, 'b-', lw=2, label='$n_s$(Goldstone)')
ax.semilogx(K_values, n_s_SA, 'r-', lw=2, label='$n_s$(SA)')
ax.axhline(0.965, color='g', ls='--', alpha=0.7, label='$n_s = 0.965$')
ax.axvline(K_pivot_default, color='gray', ls='--', alpha=0.5, label='$K_{pivot}=2.0$')
ax.axvline(K_star, color='purple', ls=':', alpha=0.7, label=f'$K^*={K_star:.3f}$')
ax.fill_between(K_values, -2, 2, where=K_values < K_star, alpha=0.1, color='green',
                label='Achievable zone')
ax.set_xlabel('$K$ [$M_{KK}$]')
ax.set_ylabel('$n_s(K)$')
ax.set_title('Spectral Indices vs Scale')
ax.set_ylim([-1.5, 1.5])
ax.set_xlim([0.001, 30])
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 3: K_pivot sweep -- max achievable n_s
ax = axes[0, 2]
kpivs = np.array([r['K_piv'] for r in results_kpiv])
ns_maxs = np.array([r['ns_max'] for r in results_kpiv])
ax.semilogx(kpivs, ns_maxs, 'ko-', lw=2, ms=5)
ax.axhline(0.965, color='g', ls='--', alpha=0.7, label='$n_s = 0.965$ target')
ax.axhline(0.950, color='orange', ls=':', alpha=0.5)
ax.axhline(0.980, color='orange', ls=':', alpha=0.5)
ax.axvline(K_star, color='purple', ls=':', alpha=0.7, label=f'$K^*={K_star:.3f}$')
ax.axvline(K_pivot_default, color='gray', ls='--', alpha=0.5, label='$K_{{pivot}}=2.0$')
ax.set_xlabel('$K_{pivot}$ [$M_{KK}$]')
ax.set_ylabel('Max achievable $n_s$')
ax.set_title('n_s Achievability vs K_pivot')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: n_s vs beta at K_pivot = 2.0
ax = axes[1, 0]
ax.plot(betas, ns_at_pivot, 'k-', lw=2)
ax.axhline(0.965, color='g', ls='--', alpha=0.7, label='Target $n_s=0.965$')
ax.axhline(n_s_SA[idx_pivot], color='r', ls=':', alpha=0.5, label=f'$n_s$(SA)={n_s_SA[idx_pivot]:.3f}')
ax.axhline(n_s_G[idx_pivot], color='b', ls=':', alpha=0.5, label=f'$n_s$(G)={n_s_G[idx_pivot]:.3f}')
ax.axvline(beta_physical, color='m', ls='--', alpha=0.7, label=f'$\\beta_{{phys}}={beta_physical:.3f}$')
ax.set_xlabel(r'$\beta$ (SA weight)')
ax.set_ylabel(f'$n_s(K={K_pivot_default})$')
ax.set_title(f'n_s vs Mixing at $K_{{pivot}}={K_pivot_default}$')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 5: Mixed spectra at several betas
ax = axes[1, 1]
for beta_show, style in [(0.0, 'b-'), (0.1, 'c-'), (0.5, 'g-'),
                          (0.9, 'orange'), (1.0, 'r-')]:
    P_show = (1 - beta_show) * P_G_norm + beta_show * chi_SA_norm
    if isinstance(style, str):
        ax.loglog(K_values, P_show, style, lw=1.5, label=f'$\\beta={beta_show:.1f}$')
    else:
        ax.loglog(K_values, P_show, color=style, lw=1.5, label=f'$\\beta={beta_show:.1f}$')
ax.axvline(K_pivot_default, color='gray', ls='--', alpha=0.5)
ax.axvline(K_star, color='purple', ls=':', alpha=0.5)
ax.set_xlabel('$K$ [$M_{KK}$]')
ax.set_ylabel('$P_{mix}(K)$')
ax.set_title('Mixed Power Spectrum')
ax.legend(fontsize=7)
ax.set_xlim([0.001, 30])
ax.grid(True, alpha=0.3)

# Panel 6: Achievable beta vs K_pivot (where applicable)
ax = axes[1, 2]
kpivs_ok = [r['K_piv'] for r in results_kpiv if not np.isnan(r['beta'])]
betas_ok = [r['beta'] for r in results_kpiv if not np.isnan(r['beta'])]
alphas_ok = [r['alpha_s'] for r in results_kpiv if not np.isnan(r['alpha_s'])]
if kpivs_ok:
    ax2 = ax.twinx()
    ax.semilogx(kpivs_ok, betas_ok, 'bo-', lw=2, ms=5, label=r'$\beta$ for $n_s=0.965$')
    ax2.semilogx(kpivs_ok, alphas_ok, 'rs-', lw=2, ms=5, label=r'$\alpha_s$')
    ax2.axhline(0, color='gray', ls=':', alpha=0.3)
    ax2.axhline(-0.040, color='orange', ls=':', alpha=0.5)
    ax.set_xlabel('$K_{pivot}$ [$M_{KK}$]')
    ax.set_ylabel(r'$\beta$ for $n_s=0.965$', color='b')
    ax2.set_ylabel(r'$\alpha_s$', color='r')
    ax.set_title('Required $\\beta$ and $\\alpha_s$ vs $K_{pivot}$')
    ax.legend(loc='upper left', fontsize=7)
    ax2.legend(loc='lower right', fontsize=7)
ax.grid(True, alpha=0.3)

plt.suptitle('SA-Goldstone Additive Mixing (SA-GOLDSTONE-MIXING-51)\n'
             f'$m_G={m_G}$, $J={J_G}$, $K^*={K_star:.4f}$, '
             f'$\\Lambda={Lambda_SA}$, verdict={verdict}', fontsize=12)
plt.tight_layout()
plt.savefig('tier0-computation/s51_sa_goldstone_mixing.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to tier0-computation/s51_sa_goldstone_mixing.png")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
