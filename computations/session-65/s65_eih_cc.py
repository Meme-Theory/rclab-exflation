#!/usr/bin/env python3
"""
S65 EIH-CC-65: EIH Effacement Projection on a_0/a_2
=====================================================

Does the Einstein-Infeld-Hoffmann effacement principle apply differentially
to the CC moment (a_0) versus the gravitational moment (a_2) of the spectral
action?

PRINCIPLE:
  The EIH theorem (1938) states that in GR, the motion of a body follows
  from the field equations alone -- internal structure is effaced. In the
  spectral action framework, the gravitational coupling of a mode in the
  Peter-Weyl sector (p,q) is proportional to the isometry Casimir
  C_2(p,q) = (p^2 + q^2 + p*q + 3*p + 3*q)/3.

  The singlet sector (0,0) has C_2 = 0: these modes are gravitationally
  INVISIBLE -- they contribute to the CC (a_0) but have zero gravitational
  self-energy. All non-singlet sectors have C_2 > 0.

  The spectral action has two channels:
    - a_0 = sum_{(p,q)} PW(p,q)^2 * N_evals(p,q)   [CC / mode counting]
    - a_2 = sum_{(p,q)} PW(p,q)^2 * sum 1/lambda^2  [gravity / curvature]

  If gravity couples only through modes with C_2 > 0, then:
    a_0^{grav} = a_0 - (singlet contribution)
    a_2^{grav} = a_2 - (singlet contribution)

  The key question: is the singlet fraction of a_0 different from the
  singlet fraction of a_2? If so, the effective CC/gravity ratio changes.

  DEEPER: The EIH self-energy scales as alpha_G * C_2(p,q) * eps, so
  higher-Casimir modes couple MORE strongly to gravity. We define a
  C_2-weighted projection:
    a_n^{grav}(C_min) = sum over sectors with C_2 >= C_min
  and scan C_min to see how the ratio a_0^{grav}/a_2^{grav} evolves.

  An even finer projection uses the continuous EIH weight:
    w_grav(p,q) = C_2(p,q) / max(C_2)
    a_n^{EIH} = sum w_grav(p,q) * contribution_n(p,q)

GATE: EIH-CC-65
  PASS: a_0^{grav}/a_2^{grav} < bare ratio by > 1 OOM
  FAIL: a_0^{grav}/a_2^{grav} ~ a_0/a_2 (no differential effacement)
  INFO: Some suppression but < 1 OOM

Session: S65 W6-A
Author: Einstein Theorist
"""

import numpy as np
import time
import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold,
    Delta_0_OES, M_KK, M_KK_gravity, M_Pl_reduced,
    PI, Vol_SU3_Haar, g0_diag,
    rho_Lambda_obs,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8, collect_spectrum,
)
from spectral_action import dim_su3_irrep

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# Section 0: Helper Functions
# =============================================================================

def casimir2(p, q):
    """Quadratic Casimir of SU(3) isometry for irrep (p,q)."""
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0


def peter_weyl_weight(p, q):
    """Peter-Weyl degeneracy = dim(p,q)^2."""
    d = dim_su3_irrep(p, q)
    return d * d


# =============================================================================
# Section 1: Compute Spectrum at Fold
# =============================================================================
print("=" * 78)
print("EIH-CC-65: EIH Effacement Projection on a_0/a_2")
print("=" * 78)

print(f"\n  tau_fold = {tau_fold}")
print(f"  a_0(fold) = {a0_fold} (canonical)")
print(f"  a_2(fold) = {a2_fold:.4f} (canonical)")
print(f"  a_0/a_2 (canonical) = {a0_fold / a2_fold:.6f}")

print("\n--- Computing D_K spectrum at fold ---")
t0 = time.time()
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

_, eval_data = collect_spectrum(tau_fold, gens, f_abc, gammas,
                               max_pq_sum=3, verbose=False)
t_spec = time.time() - t0
print(f"  Spectrum computed in {t_spec:.1f}s")

# =============================================================================
# Section 2: Sector-Resolved Spectral Moments
# =============================================================================
print("\n" + "=" * 78)
print("Section 2: Sector-Resolved Spectral Moments")
print("=" * 78)

# Collect per-sector data
sectors = []
for p, q, evals in eval_data:
    d_pq = dim_su3_irrep(p, q)
    pw2 = d_pq**2
    c2 = casimir2(p, q)
    omega = np.abs(evals)
    n_evals = len(evals)

    # Spectral action (f(x) = |x| convention):
    #   S = sum PW^2 * sum |lambda|
    # Mode-count moment:
    #   a_0_sector = PW^2 * n_evals   (counts modes)
    # Curvature moment (zeta convention):
    #   a_2_sector = sum 1/lambda^2    (unweighted, for diagnostic)
    # Spectral action moment:
    #   SA_sector = PW^2 * sum |lambda|

    a0_sector = pw2 * n_evals
    a2_sector_zeta = np.sum(1.0 / omega**2) if np.all(omega > 0) else 0.0
    sa_sector = pw2 * np.sum(omega)

    # For a_2 in heat kernel convention: PW^2 * sum 1/lambda^2
    a2_sector_hk = pw2 * a2_sector_zeta

    sectors.append({
        'p': p, 'q': q,
        'dim': d_pq, 'pw2': pw2, 'C2': c2,
        'n_evals': n_evals, 'omega': omega,
        'a0': a0_sector,
        'a2_zeta': a2_sector_zeta,
        'a2_hk': a2_sector_hk,
        'sa': sa_sector,
    })

# Total moments
total_a0 = sum(s['a0'] for s in sectors)
total_a2_hk = sum(s['a2_hk'] for s in sectors)
total_sa = sum(s['sa'] for s in sectors)
total_n_evals = sum(s['n_evals'] for s in sectors)
total_n_modes = sum(s['a0'] for s in sectors)  # = sum pw2 * n_evals

print(f"\n  Total eigenvalues (unweighted): {total_n_evals}")
print(f"  Total PW-weighted modes: {total_n_modes}")
print(f"  Total a_0 = {total_a0}")
print(f"  Total a_2 (heat kernel) = {total_a2_hk:.6f}")
print(f"  Total spectral action = {total_sa:.4f}")
print(f"  Bare ratio a_0/a_2 = {total_a0 / total_a2_hk:.6f}")

# Print per-sector table
print(f"\n  {'(p,q)':>6s}  {'dim':>4s}  {'PW^2':>6s}  {'C_2':>8s}  {'n_ev':>5s}  "
      f"{'a_0':>8s}  {'a_2^HK':>12s}  {'SA':>12s}  {'a_0 frac':>10s}  {'a_2 frac':>10s}")
print("  " + "-" * 105)
for s in sorted(sectors, key=lambda x: x['C2']):
    a0_frac = s['a0'] / total_a0
    a2_frac = s['a2_hk'] / total_a2_hk
    print(f"  ({s['p']},{s['q']}) {s['dim']:>4d}  {s['pw2']:>6d}  {s['C2']:>8.3f}  {s['n_evals']:>5d}  "
          f"{s['a0']:>8d}  {s['a2_hk']:>12.4f}  {s['sa']:>12.2f}  {a0_frac:>10.6f}  {a2_frac:>10.6f}")


# =============================================================================
# Section 3: EIH Projection — Singlet vs Non-Singlet
# =============================================================================
print("\n" + "=" * 78)
print("Section 3: EIH Projection — Singlet (C_2=0) vs Non-Singlet (C_2>0)")
print("=" * 78)

singlet_a0 = sum(s['a0'] for s in sectors if s['C2'] == 0)
singlet_a2 = sum(s['a2_hk'] for s in sectors if s['C2'] == 0)
singlet_sa = sum(s['sa'] for s in sectors if s['C2'] == 0)

nonsinglet_a0 = total_a0 - singlet_a0
nonsinglet_a2 = total_a2_hk - singlet_a2
nonsinglet_sa = total_sa - singlet_sa

print(f"\n  Singlet (0,0):   a_0 = {singlet_a0}, a_2 = {singlet_a2:.6f}, SA = {singlet_sa:.4f}")
print(f"  Non-singlet:     a_0 = {nonsinglet_a0}, a_2 = {nonsinglet_a2:.6f}, SA = {nonsinglet_sa:.4f}")
print(f"\n  Singlet fraction of a_0: {singlet_a0/total_a0:.6f}")
print(f"  Singlet fraction of a_2: {singlet_a2/total_a2_hk:.6f}")
print(f"  Singlet fraction of SA:  {singlet_sa/total_sa:.6f}")

ratio_bare = total_a0 / total_a2_hk
ratio_grav = nonsinglet_a0 / nonsinglet_a2 if nonsinglet_a2 > 0 else float('inf')

print(f"\n  Bare ratio:              a_0/a_2 = {ratio_bare:.6f}")
print(f"  EIH-projected ratio:     a_0^grav/a_2^grav = {ratio_grav:.6f}")
print(f"  Ratio of ratios:         {ratio_grav/ratio_bare:.6f}")
print(f"  Suppression factor:      {ratio_bare/ratio_grav:.6f}")
print(f"  log10(suppression):      {np.log10(ratio_bare/ratio_grav):.4f}")


# =============================================================================
# Section 4: C_2-Weighted EIH Projection (Continuous)
# =============================================================================
print("\n" + "=" * 78)
print("Section 4: Continuous C_2-Weighted EIH Projection")
print("=" * 78)

# The EIH self-energy of a mode in sector (p,q) scales as C_2(p,q).
# Define gravitational weight: w(p,q) = C_2(p,q).
# Then:
#   a_0^{EIH} = sum_sectors C_2(p,q) * a_0_sector
#   a_2^{EIH} = sum_sectors C_2(p,q) * a_2_sector
# This gives a C_2-weighted CC/gravity ratio.

max_C2 = max(s['C2'] for s in sectors)
print(f"  Max C_2 = {max_C2:.4f}")

a0_eih = sum(s['C2'] * s['a0'] for s in sectors)
a2_eih = sum(s['C2'] * s['a2_hk'] for s in sectors)
sa_eih = sum(s['C2'] * s['sa'] for s in sectors)

ratio_eih = a0_eih / a2_eih if a2_eih > 0 else float('inf')

print(f"\n  C_2-weighted a_0^EIH = {a0_eih:.4f}")
print(f"  C_2-weighted a_2^EIH = {a2_eih:.6f}")
print(f"  C_2-weighted SA^EIH = {sa_eih:.4f}")
print(f"\n  C_2-weighted ratio:  a_0^EIH/a_2^EIH = {ratio_eih:.6f}")
print(f"  vs bare ratio:       a_0/a_2 = {ratio_bare:.6f}")
print(f"  Ratio of ratios:     {ratio_eih/ratio_bare:.6f}")
print(f"  Suppression factor:  {ratio_bare/ratio_eih:.6f}")
print(f"  log10(suppression):  {np.log10(ratio_bare/ratio_eih) if ratio_eih > 0 and ratio_bare > ratio_eih else 0:.4f}")


# =============================================================================
# Section 5: C_2 Threshold Sweep
# =============================================================================
print("\n" + "=" * 78)
print("Section 5: C_2 Threshold Sweep — a_0^grav/a_2^grav vs C_2^min")
print("=" * 78)

# For each threshold C_min, include only sectors with C_2 >= C_min.
# This shows how the CC/gravity ratio evolves as we restrict to
# more strongly gravitating modes.

C2_values = sorted(set(s['C2'] for s in sectors))
print(f"  Distinct C_2 values: {C2_values}")

thresholds = np.linspace(0, max_C2, 50)
ratios_sweep = np.zeros(len(thresholds))
a0_sweep = np.zeros(len(thresholds))
a2_sweep = np.zeros(len(thresholds))
n_sectors_sweep = np.zeros(len(thresholds), dtype=int)

for i, c_min in enumerate(thresholds):
    included = [s for s in sectors if s['C2'] >= c_min]
    a0_sweep[i] = sum(s['a0'] for s in included)
    a2_sweep[i] = sum(s['a2_hk'] for s in included)
    n_sectors_sweep[i] = len(included)
    ratios_sweep[i] = a0_sweep[i] / a2_sweep[i] if a2_sweep[i] > 0 else 0.0

print(f"\n  {'C_2^min':>8s}  {'N_sectors':>10s}  {'a_0':>12s}  {'a_2':>14s}  {'a_0/a_2':>12s}  {'vs bare':>10s}")
print("  " + "-" * 75)
# Print at each distinct C_2 threshold
for c2_val in C2_values:
    idx = np.argmin(np.abs(thresholds - c2_val))
    included = [s for s in sectors if s['C2'] >= c2_val]
    a0_v = sum(s['a0'] for s in included)
    a2_v = sum(s['a2_hk'] for s in included)
    n_v = len(included)
    r_v = a0_v / a2_v if a2_v > 0 else 0.0
    print(f"  {c2_val:>8.3f}  {n_v:>10d}  {a0_v:>12d}  {a2_v:>14.4f}  {r_v:>12.6f}  {r_v/ratio_bare:>10.6f}")


# =============================================================================
# Section 6: Cross-Reference with 8-Mode BCS Data (S64)
# =============================================================================
print("\n" + "=" * 78)
print("Section 6: Cross-Reference with S64 R-G Charge Data")
print("=" * 78)

rg_data = np.load(os.path.join(SCRIPT_DIR, 's64_rg_charge_decomp.npz'),
                  allow_pickle=True)

labels_8 = rg_data['labels']
C2_8 = rg_data['C2_modes']
eps_8 = rg_data['eps_fold']
omega_8 = rg_data['omega_k']
W_k = rg_data['W_k']
W_k_norm = rg_data['W_k_norm']

print(f"\n  8-mode BCS labels: {list(labels_8)}")
print(f"  C_2 values: {C2_8}")
print(f"  Gravitational coupling W_k (normalized):")
for i in range(len(labels_8)):
    print(f"    {labels_8[i]:>6s}: C_2 = {C2_8[i]:.4f}, W_k/max = {W_k_norm[i]:.6f}")

# In the BCS sector, B1 (singlet) has C_2 = 0, B2 (adjoint) has C_2 = 3,
# B3 (fundamental) has C_2 = 4/3.
# W_k incorporates the combined effect of gravitational coupling and
# vacuum energy projection. But here we want the PURE Casimir weighting.

# BCS-level a_0 analog: just mode count
bcs_a0_all = len(labels_8)
bcs_a0_grav = sum(1 for c in C2_8 if c > 0)
bcs_a0_singlet = sum(1 for c in C2_8 if c == 0)

# BCS-level a_2 analog: 1/omega_k^2 weighted
bcs_a2_all = np.sum(1.0 / omega_8**2)
bcs_a2_grav = np.sum(1.0 / omega_8[C2_8 > 0]**2)
bcs_a2_singlet = np.sum(1.0 / omega_8[C2_8 == 0]**2)

ratio_bcs_bare = bcs_a0_all / bcs_a2_all
ratio_bcs_grav = bcs_a0_grav / bcs_a2_grav if bcs_a2_grav > 0 else float('inf')

print(f"\n  BCS bare ratio: a_0/a_2 = {ratio_bcs_bare:.6f}")
print(f"  BCS EIH-projected: a_0^grav/a_2^grav = {ratio_bcs_grav:.6f}")
print(f"  Ratio of ratios: {ratio_bcs_grav/ratio_bcs_bare:.6f}")

# C_2-weighted BCS projection
bcs_a0_eih = np.sum(C2_8)
bcs_a2_eih = np.sum(C2_8 / omega_8**2)
ratio_bcs_eih = bcs_a0_eih / bcs_a2_eih if bcs_a2_eih > 0 else float('inf')

print(f"\n  BCS C_2-weighted: a_0^EIH/a_2^EIH = {ratio_bcs_eih:.6f}")
print(f"  vs BCS bare: {ratio_bcs_eih/ratio_bcs_bare:.6f}")


# =============================================================================
# Section 7: Structural Analysis — Why EIH Cannot Solve CC
# =============================================================================
print("\n" + "=" * 78)
print("Section 7: Structural Analysis")
print("=" * 78)

# The key structural constraint:
# a_0 = sum PW^2 * N_evals ~ integral over spectrum (mode counting)
# a_2 = sum PW^2 / lambda^2 ~ R * Vol (curvature * volume)
#
# For Weyl's law on an 8D manifold: N(lambda) ~ lambda^8 * Vol
# So dN/dlambda ~ lambda^7, and:
#   a_0 = integral dN = integral lambda^7 dlambda ~ Lambda^8 * Vol
#   a_2 = integral (1/lambda^2) dN = integral lambda^5 dlambda ~ Lambda^6 * Vol * R
#
# The C_2-weighted version:
#   a_0^{EIH} = sum C_2(p,q) * PW^2 * N_evals
#   a_2^{EIH} = sum C_2(p,q) * PW^2 / lambda^2
#
# C_2(p,q) grows as (p+q)^2 for large (p,q).
# PW^2 = dim(p,q)^2 grows as (p+q)^6 for large (p,q).
# N_evals per sector grows with p+q (more eigenvalues for higher irreps).
#
# So C_2 * PW^2 * N_evals ~ (p+q)^{2+6+?} grows even FASTER with (p+q).
# Similarly for C_2 * PW^2 / lambda^2.
#
# The question is: does C_2 weighting change the RATIO?
# If C_2 scales uniformly with (p+q), both moments get the same factor
# and the ratio is unchanged. This is Weyl's law in disguise:
# the UV (large p+q) dominates both moments, and C_2 just enhances
# the UV contribution equally.

# Compute fractional contributions by C_2 quintile
C2_all = [s['C2'] for s in sectors]
C2_sorted = sorted(set(C2_all))

print(f"\n  Number of sectors: {len(sectors)}")
print(f"  C_2 range: [{min(C2_all):.4f}, {max(C2_all):.4f}]")

# For each sector, compute the fraction of a_0 and a_2
a0_per_c2 = {}
a2_per_c2 = {}
for s in sectors:
    c2 = s['C2']
    a0_per_c2[c2] = a0_per_c2.get(c2, 0) + s['a0']
    a2_per_c2[c2] = a2_per_c2.get(c2, 0) + s['a2_hk']

print(f"\n  {'C_2':>8s}  {'a_0 frac':>10s}  {'a_2 frac':>10s}  {'a_0/a_2 local':>14s}  {'ratio/bare':>10s}")
print("  " + "-" * 60)
for c2 in C2_sorted:
    a0_f = a0_per_c2[c2] / total_a0
    a2_f = a2_per_c2[c2] / total_a2_hk
    local_ratio = a0_per_c2[c2] / a2_per_c2[c2] if a2_per_c2[c2] > 0 else 0
    print(f"  {c2:>8.3f}  {a0_f:>10.6f}  {a2_f:>10.6f}  {local_ratio:>14.6f}  {local_ratio/ratio_bare:>10.6f}")

# Asymptotic scaling analysis
# For sectors with same C_2, what is the a_0/a_2 ratio?
# If all sectors have the same ratio, EIH weighting cannot help.
print("\n  Structural conclusion:")
print(f"    The singlet (0,0) fraction of a_0 is {singlet_a0/total_a0:.6f}")
print(f"    The singlet (0,0) fraction of a_2 is {singlet_a2/total_a2_hk:.6f}")
diff = singlet_a0/total_a0 - singlet_a2/total_a2_hk
print(f"    Difference: {diff:.6f}")
if abs(diff) < 0.01:
    print("    -> Singlet contributes SIMILARLY to both moments.")
    print("    -> EIH removal of singlet cannot differentially affect a_0/a_2.")
else:
    direction = "more to a_0" if diff > 0 else "more to a_2"
    print(f"    -> Singlet contributes {direction} (asymmetry {diff:.4f}).")
    if diff > 0:
        print("    -> Removing singlet preferentially reduces a_0 -> ratio decreases.")
    else:
        print("    -> Removing singlet preferentially reduces a_2 -> ratio increases.")


# =============================================================================
# Section 8: Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("Section 8: GATE VERDICT — EIH-CC-65")
print("=" * 78)

# Method 1: Binary singlet removal
suppression_binary = ratio_bare / ratio_grav if ratio_grav > 0 else 0
log_suppression_binary = np.log10(suppression_binary) if suppression_binary > 1 else -np.log10(1/suppression_binary) if suppression_binary > 0 else 0

# Method 2: Continuous C_2 weighting
suppression_eih = ratio_bare / ratio_eih if ratio_eih > 0 else 0
log_suppression_eih = np.log10(suppression_eih) if suppression_eih > 1 else -np.log10(1/suppression_eih) if suppression_eih > 0 else 0

print(f"\n  Method 1 — Binary singlet removal:")
print(f"    Bare a_0/a_2 = {ratio_bare:.6f}")
print(f"    Projected a_0^grav/a_2^grav = {ratio_grav:.6f}")
print(f"    Suppression: {suppression_binary:.6f}x")
print(f"    log10(suppression): {log_suppression_binary:.4f}")

print(f"\n  Method 2 — Continuous C_2 weighting:")
print(f"    Bare a_0/a_2 = {ratio_bare:.6f}")
print(f"    EIH-weighted a_0^EIH/a_2^EIH = {ratio_eih:.6f}")
print(f"    Suppression: {suppression_eih:.6f}x")
print(f"    log10(suppression): {log_suppression_eih:.4f}")

# Determine verdict
max_suppression = max(abs(log_suppression_binary), abs(log_suppression_eih))

if max_suppression > 1.0:
    verdict = "PASS"
    detail = f"EIH projection suppresses a_0/a_2 by {max_suppression:.2f} OOM (> 1 OOM threshold)."
elif max_suppression > 0.1:
    verdict = "INFO"
    detail = f"EIH projection gives {max_suppression:.4f} OOM suppression (< 1 OOM, marginal)."
else:
    # Check if it goes the WRONG way
    if ratio_grav > ratio_bare and ratio_eih > ratio_bare:
        verdict = "FAIL"
        detail = f"EIH projection INCREASES a_0/a_2 (wrong direction). No CC suppression."
    else:
        verdict = "FAIL"
        detail = f"EIH projection gives {max_suppression:.4f} OOM (< 0.1 OOM). No significant differential effacement."

print(f"\n  Gate EIH-CC-65: {verdict}")
print(f"  Threshold: PASS if > 1 OOM suppression, FAIL if < 0.1 OOM")
print(f"  Detail: {detail}")


# =============================================================================
# Section 9: Save Data
# =============================================================================
print("\n" + "=" * 78)
print("Section 9: Saving Results")
print("=" * 78)

outpath = os.path.join(SCRIPT_DIR, 's65_eih_cc.npz')

# Build sector arrays for saving
n_sectors = len(sectors)
pq_labels = np.array([(s['p'], s['q']) for s in sectors])
C2_arr = np.array([s['C2'] for s in sectors])
a0_arr = np.array([s['a0'] for s in sectors])
a2_arr = np.array([s['a2_hk'] for s in sectors])
sa_arr = np.array([s['sa'] for s in sectors])
pw2_arr = np.array([s['pw2'] for s in sectors])
nev_arr = np.array([s['n_evals'] for s in sectors])

np.savez(outpath,
         # Gate info
         gate_name='EIH-CC-65',
         gate_verdict=verdict,
         gate_detail=detail,
         # Bare moments
         total_a0=total_a0,
         total_a2_hk=total_a2_hk,
         total_sa=total_sa,
         ratio_bare=ratio_bare,
         # Singlet removal
         singlet_a0=singlet_a0,
         singlet_a2=singlet_a2,
         nonsinglet_a0=nonsinglet_a0,
         nonsinglet_a2=nonsinglet_a2,
         ratio_grav=ratio_grav,
         suppression_binary=suppression_binary,
         log_suppression_binary=log_suppression_binary,
         # C_2-weighted
         a0_eih=a0_eih,
         a2_eih=a2_eih,
         ratio_eih=ratio_eih,
         suppression_eih=suppression_eih,
         log_suppression_eih=log_suppression_eih,
         # Threshold sweep
         thresholds=thresholds,
         ratios_sweep=ratios_sweep,
         a0_sweep=a0_sweep,
         a2_sweep=a2_sweep,
         n_sectors_sweep=n_sectors_sweep,
         # Per-sector data
         pq_labels=pq_labels,
         C2_sectors=C2_arr,
         a0_sectors=a0_arr,
         a2_sectors=a2_arr,
         sa_sectors=sa_arr,
         pw2_sectors=pw2_arr,
         nev_sectors=nev_arr,
         # BCS cross-reference
         ratio_bcs_bare=ratio_bcs_bare,
         ratio_bcs_grav=ratio_bcs_grav,
         ratio_bcs_eih=ratio_bcs_eih,
         )

print(f"  Saved: {outpath}")


# =============================================================================
# Section 10: Plot
# =============================================================================
print("\n  Generating plot...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: Sector-resolved a_0 and a_2 fractions vs C_2
ax = axes[0, 0]
c2_unique = sorted(set(C2_arr))
a0_frac_by_c2 = []
a2_frac_by_c2 = []
for c2_val in c2_unique:
    mask = C2_arr == c2_val
    a0_frac_by_c2.append(np.sum(a0_arr[mask]) / total_a0)
    a2_frac_by_c2.append(np.sum(a2_arr[mask]) / total_a2_hk)

x = np.arange(len(c2_unique))
width = 0.35  # (local)
ax.bar(x - width/2, a0_frac_by_c2, width, label=r'$a_0$ fraction', color='steelblue', alpha=0.8)
ax.bar(x + width/2, a2_frac_by_c2, width, label=r'$a_2$ fraction', color='firebrick', alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels([f'{c:.1f}' for c in c2_unique], rotation=45, fontsize=8)
ax.set_xlabel(r'$C_2$ (isometry Casimir)')
ax.set_ylabel('Fraction')
ax.set_title(r'$a_0$ vs $a_2$ Fraction by Casimir Group')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel B: C_2 threshold sweep
ax = axes[0, 1]
valid = ratios_sweep > 0
ax.plot(thresholds[valid], ratios_sweep[valid], 'k-', linewidth=2)
ax.axhline(y=ratio_bare, color='gray', linestyle='--', alpha=0.7, label=f'Bare = {ratio_bare:.3f}')
ax.set_xlabel(r'$C_2^{\rm min}$ threshold')
ax.set_ylabel(r'$a_0^{\rm grav} / a_2^{\rm grav}$')
ax.set_title('CC Ratio vs Gravitational Coupling Threshold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel C: Per-sector local a_0/a_2 ratio
ax = axes[1, 0]
local_ratios = []
c2_for_plot = []
for s in sectors:
    if s['a2_hk'] > 0:
        lr = s['a0'] / s['a2_hk']
        local_ratios.append(lr)
        c2_for_plot.append(s['C2'])
ax.scatter(c2_for_plot, local_ratios, s=40, alpha=0.6, c='darkblue')
ax.axhline(y=ratio_bare, color='gray', linestyle='--', alpha=0.7, label=f'Global bare = {ratio_bare:.3f}')
ax.set_xlabel(r'$C_2$ (isometry Casimir)')
ax.set_ylabel(r'Local $a_0/a_2$ per sector')
ax.set_title('Per-Sector CC/Gravity Ratio')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')

# Panel D: BCS 8-mode comparison
ax = axes[1, 1]
bar_labels = ['Bare\n(all)', 'Binary\n(C2>0)', 'C2-wtd\n(EIH)', 'BCS bare', 'BCS\n(C2>0)', 'BCS\nC2-wtd']
bar_values = [ratio_bare, ratio_grav, ratio_eih, ratio_bcs_bare, ratio_bcs_grav, ratio_bcs_eih]
colors = ['steelblue', 'firebrick', 'darkgreen', 'steelblue', 'firebrick', 'darkgreen']
alphas = [0.9, 0.9, 0.9, 0.5, 0.5, 0.5]
bars = ax.bar(range(len(bar_labels)), bar_values, color=colors)
for bar, a in zip(bars, alphas):
    bar.set_alpha(a)
ax.set_xticks(range(len(bar_labels)))
ax.set_xticklabels(bar_labels, fontsize=8)
ax.set_ylabel(r'$a_0/a_2$ ratio')
ax.set_title('EIH Projection: Full Spectrum vs BCS 8-Mode')
ax.grid(True, alpha=0.3, axis='y')
# Annotate values
for bar, val in zip(bars, bar_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01*max(bar_values),
            f'{val:.3f}', ha='center', va='bottom', fontsize=8)

fig.suptitle('EIH-CC-65: EIH Effacement Projection on CC Ratio $a_0/a_2$',
             fontsize=13, fontweight='bold')
plt.tight_layout()

plotpath = os.path.join(SCRIPT_DIR, 's65_eih_cc.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {plotpath}")

print("\n" + "=" * 78)
print("EIH-CC-65 COMPLETE")
print("=" * 78)
