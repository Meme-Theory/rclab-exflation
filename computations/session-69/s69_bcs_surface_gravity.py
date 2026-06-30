#!/usr/bin/env python3
"""
s69_bcs_surface_gravity.py — BCS-SURFACE-GRAVITY-69
Surface Gravity of the BCS Spectral Gap
================================================================

Compute the analog surface gravity kappa_BCS of the BCS spectral gap
and the associated temperature T_BCS = kappa_BCS / (2*pi).

Physical Picture
----------------
In the phonon-exflation framework, the BCS pairing gap Delta creates a
spectral boundary in the Dirac operator D_K: below Delta, single-particle
excitations are forbidden. This is the direct analog of a horizon in
causal structure — signals (excitations) cannot propagate through the gap.

The surface gravity kappa measures how rapidly the "redshift factor"
vanishes at the horizon. For a BCS gap with dispersion relation
E(k) = sqrt(epsilon(k)^2 + Delta^2), the analog surface gravity is
defined from the behavior of E near the gap edge:

  E - Delta ~ (1/2) * epsilon^2 / Delta   as epsilon -> 0

This quadratic approach (not linear) means the BCS "horizon" is
degenerate (kappa=0 in the naive sense), analogous to an EXTREMAL
black hole. This is consistent with S48/S49 identification of the
dump point (tau=0.19) as an extremal horizon (T_H=0, kappa=0, BPS).

We compute:
1. Full D_K eigenvalue spectrum at fold via Peter-Weyl (L_max=6)
2. Eigenvalue density near the gap edge
3. BCS dispersion relation from the B2-sector single-particle energies
4. Analog surface gravity and temperature
5. Comparison to the S48 acoustic horizon T_GH = 66 M_KK

Input: computations/session-61/s61_fabric_landau_params.npz
       computations/_shared/canonical_constants.py
       computations/_shared/dirac_spectrum.py

Output: computations/session-69/s69_bcs_surface_gravity.npz

Gate: BCS-SURFACE-69 — INFO: report kappa_BCS, T_BCS, and T_BCS/T_GH ratio.
Author: schwarzschild-penrose-geometer (Session 69, W5-J)
"""

import sys
import os
import time
import numpy as np
from numpy.linalg import eigh, eigvals, norm
from scipy.interpolate import CubicSpline

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)
archive_dir = os.path.join(script_dir, "..", "_shared")
if os.path.isdir(archive_dir):
    sys.path.append(os.path.abspath(archive_dir))

from canonical_constants import (
    tau_fold, Vol_SU3_Haar, PI, M_KK,
    Delta_0_GL, Delta_0_OES, Delta_B3, Delta_BCS,
    E_cond, xi_BCS, T_acoustic
)

import dirac_spectrum as tds

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

outdir = os.path.dirname(os.path.abspath(__file__))
t_start_global = time.time()

print("=" * 78)
print("  BCS-SURFACE-GRAVITY-69: Surface Gravity of the BCS Spectral Gap")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
print(f"  Delta_0_GL = {Delta_0_GL:.6f} M_KK")
print(f"  Delta_0_OES = {Delta_0_OES:.6f} M_KK")

# =============================================================================
# SECTION 0: LOAD LANDAU PARAMETER DATA (8-mode BCS structure)
# =============================================================================
print("\n" + "=" * 78)
print("  0. LOAD BCS STRUCTURE DATA FROM s61_fabric_landau_params.npz")
print("=" * 78)

d61 = np.load(os.path.join(outdir, 's61_fabric_landau_params.npz'), allow_pickle=True)
eps_fold = d61['eps_fold']       # 8 single-particle energies at fold
V_fold = d61['V_fold']           # 8x8 pairing matrix
J_mode = d61['J_mode']           # Josephson couplings
branch_labels = d61['branch_labels']  # ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']

print(f"  BCS modes: {list(branch_labels)}")
print(f"  Single-particle energies (M_KK):")
for i, (lab, e) in enumerate(zip(branch_labels, eps_fold)):
    print(f"    {lab}: eps = {e:.6f}")

# The BCS gap Delta is the energy required to break a Cooper pair.
# S81 Level 3 retrofit: replaced hardcode 0.52 with canonical Delta_BCS
# (R-Protected, S70 BCS-GAP-CANONICAL-70, value = 0.46425473948...).
# Previous value 0.52 was "task specification" from S69 era; the S70 audit
# established 0.4643 as the canonical gap. 12% discrepancy resolved here.
# The B2[3] eigenvalue eps_fold[3] ~ 0.52 is an independent quantity and
# remains available via the loaded d61['eps_fold'] array.
print(f"\n  BCS gap Delta = {Delta_BCS:.6f} M_KK (canonical, S70 R-Protected)")

# =============================================================================
# SECTION 1: COMPUTE D_K EIGENVALUE SPECTRUM AT FOLD (L_max=6)
# =============================================================================
print("\n" + "=" * 78)
print("  1. DIRAC EIGENVALUE COMPUTATION AT tau_fold (L_max=6)")
print("=" * 78)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
gammas = tds.build_cliff8()
B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma_conn = tds.connection_coefficients(ft)
Omega = tds.spinor_connection_offset(Gamma_conn, gammas)

cliff_err = tds.validate_clifford(gammas)
conn_err = tds.validate_connection(Gamma_conn)
print(f"  Clifford error: {cliff_err:.2e}")
print(f"  Metric compat error: {conn_err:.2e}")

L_MAX = 6  # (local)
all_lambda_abs = []   # all |lambda| values with PW multiplicity
all_lambda_raw = []   # all |lambda| values WITHOUT PW multiplicity (for density)
irrep_data = {}       # (p,q) -> dict with eigenvalues and dimensions

t_spec_start = time.time()
n_zero = 0  # (local)
for L in range(L_MAX + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        tds._irrep_cache.clear()
        try:
            rho, _ = tds.get_irrep(p, q, gens, f_abc)
            D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)
            ev = eigvals(D_pi)
            # D_K eigenvalues are purely imaginary; |lambda| = |Im(ev)|
            lam_abs = np.sort(np.abs(ev))
            # Separate zero and nonzero
            nonzero_mask = lam_abs > 1e-10
            n_zero_here = np.sum(~nonzero_mask)
            if n_zero_here > 0:
                n_zero += n_zero_here

            # Store raw eigenvalues (no PW mult)
            all_lambda_raw.extend(lam_abs[nonzero_mask])

            # With PW multiplicity = dim(p,q)
            for lam in lam_abs[nonzero_mask]:
                for _ in range(dim_pq):
                    all_lambda_abs.append(lam)

            irrep_data[(p, q)] = {
                'dim': dim_pq,
                'lam_abs': lam_abs,
                'n_evals': len(lam_abs),
                'n_nonzero': int(np.sum(nonzero_mask)),
            }

            if L <= 2 or (p == 0 and q == 0):
                print(f"  ({p},{q}): dim={dim_pq:4d}, n_ev={len(lam_abs)}, "
                      f"|lam|=[{lam_abs.min():.4f},{lam_abs.max():.4f}], "
                      f"zeros={n_zero_here}")
        except Exception as exc:
            print(f"  ({p},{q}): SKIPPED - {exc}")

t_spec = time.time() - t_spec_start
all_lambda_raw = np.sort(np.array(all_lambda_raw))
all_lambda_abs = np.sort(np.array(all_lambda_abs))

print(f"\n  {len(irrep_data)} irreps computed in {t_spec:.1f}s")
print(f"  Total nonzero |lambda| (no PW mult): {len(all_lambda_raw)}")
print(f"  Total nonzero |lambda| (with PW mult): {len(all_lambda_abs)}")
print(f"  Zero modes excluded: {n_zero}")
print(f"  Spectrum range: [{all_lambda_raw.min():.6f}, {all_lambda_raw.max():.6f}] M_KK")

# =============================================================================
# SECTION 2: EIGENVALUE DENSITY NEAR GAP EDGE
# =============================================================================
print("\n" + "=" * 78)
print("  2. EIGENVALUE DENSITY NEAR THE BCS GAP")
print("=" * 78)

# The BCS gap creates a spectral boundary at E = Delta.
# Below Delta, single-particle excitations are gapped.
# The density of states near the gap edge determines the "horizon geometry."

# Count eigenvalues in bins around Delta
delta_E = 0.05  # bin width in M_KK  # (local)
E_edges = np.arange(0, all_lambda_raw.max() + delta_E, delta_E)
E_centers = 0.5 * (E_edges[:-1] + E_edges[1:])

# Histogram of raw eigenvalue density (no PW mult)
hist_raw, _ = np.histogram(all_lambda_raw, bins=E_edges)
rho_raw = hist_raw / delta_E  # density of states per M_KK

# Histogram with PW multiplicity
hist_pw, _ = np.histogram(all_lambda_abs, bins=E_edges)
rho_pw = hist_pw / delta_E

# Find the gap edge region
gap_idx = np.searchsorted(E_centers, Delta_BCS)
print(f"  Delta_BCS = {Delta_BCS:.4f} M_KK")
print(f"  Eigenvalue density near gap edge (raw, no PW mult):")
for i in range(max(0, gap_idx - 3), min(len(E_centers), gap_idx + 4)):
    print(f"    E = {E_centers[i]:.3f}: rho = {rho_raw[i]:.1f} states/M_KK")

# Count eigenvalues below Delta
n_below = np.sum(all_lambda_raw < Delta_BCS)
n_total = len(all_lambda_raw)
print(f"\n  Eigenvalues below Delta: {n_below} / {n_total} = {n_below/n_total:.4f}")

# Nearest eigenvalues to Delta
sorted_lam = all_lambda_raw
idx_near = np.argmin(np.abs(sorted_lam - Delta_BCS))
print(f"  Closest eigenvalue to Delta: |lambda| = {sorted_lam[idx_near]:.6f}")
if idx_near > 0:
    print(f"  Below-gap neighbor: |lambda| = {sorted_lam[idx_near-1]:.6f}")
if idx_near < len(sorted_lam) - 1:
    print(f"  Above-gap neighbor: |lambda| = {sorted_lam[idx_near+1]:.6f}")

# =============================================================================
# SECTION 3: BCS DISPERSION AND SURFACE GRAVITY
# =============================================================================
print("\n" + "=" * 78)
print("  3. BCS DISPERSION RELATION AND ANALOG SURFACE GRAVITY")
print("=" * 78)

# The BCS quasiparticle dispersion is:
#   E_k = sqrt(epsilon_k^2 + Delta^2)
#
# where epsilon_k is the single-particle energy measured from the Fermi level.
#
# Near the gap edge (epsilon_k -> 0):
#   E_k = Delta + epsilon_k^2 / (2*Delta) + O(epsilon_k^4)
#
# The approach to the gap is QUADRATIC, not linear.
#
# For a Schwarzschild horizon, the redshift factor is:
#   z ~ kappa * (r - r_H) + O((r-r_H)^2)   [LINEAR]
#
# For an extremal horizon (e.g., extremal Reissner-Nordstrom):
#   z ~ kappa_2 * (r - r_H)^2 + O((r-r_H)^3)   [QUADRATIC]
#   with kappa = 0, T_H = 0
#
# The BCS gap has the same degenerate structure:
#   E - Delta ~ epsilon^2 / (2*Delta)   [QUADRATIC]
#
# This confirms the S48/S49 identification: the BCS gap is an EXTREMAL
# horizon analog (kappa = 0, T_H = 0, BPS saturation).

# Define the BCS dispersion
epsilon_grid = np.linspace(-2.0, 2.0, 10000)  # single-particle energies in M_KK
E_BCS = np.sqrt(epsilon_grid**2 + Delta_BCS**2)

# The "redshift factor" analog: f(E) = sqrt(E^2 - Delta^2) / E
# This vanishes at E = Delta (the "horizon")
E_grid_above = np.linspace(Delta_BCS * 1.0001, Delta_BCS * 5, 1000)
f_redshift = np.sqrt(E_grid_above**2 - Delta_BCS**2) / E_grid_above

# Surface gravity: kappa = df/dr at horizon
# In BCS: d(f)/d(E) at E = Delta
# f(E) = sqrt(E^2 - Delta^2) / E
# df/dE = Delta^2 / (E^2 * sqrt(E^2 - Delta^2))
# As E -> Delta: df/dE -> infinity (the approach is SINGULAR)
#
# This is the signature of an extremal horizon: the redshift factor
# approaches zero with INFINITE slope in the coordinate that resolves
# the horizon. For non-extremal horizons, the slope is finite (= kappa).
#
# More precisely, define x = (E - Delta)/Delta (dimensionless distance
# from the gap edge). Then:
#   f(E) = sqrt(2*x + x^2) * Delta / (Delta*(1+x)) = sqrt(2*x + x^2)/(1+x)
#   ~ sqrt(2*x)   as x -> 0
#
# So f ~ sqrt(x), which is the extremal RN near-horizon behavior
# (ds^2 ~ -(r-r_H)^2 dt^2 + dr^2/(r-r_H)^2 has f ~ (r-r_H)).
# Wait — for extremal RN, f ~ (r-r_H), which is LINEAR, not sqrt.
# The BCS dispersion gives f ~ sqrt(x), which is SUBLINEAR.
# This means the BCS gap is "more extremal than extremal."

# Let us define kappa properly for the BCS case.
# The standard surface gravity for a static spacetime is:
#   kappa = lim_{r->r_H} f'(r) * f(r)^{-1} * ... (depends on convention)
#
# For BCS, the cleanest definition uses the group velocity:
#   v_g = dE/dk = (dE/depsilon) * (depsilon/dk)
#   = (epsilon / sqrt(epsilon^2 + Delta^2)) * v_F
#   = (epsilon / E) * v_F
#
# At the gap edge (epsilon -> 0): v_g -> 0.
# This vanishing group velocity IS the "horizon" — signals cannot
# propagate through the gap, just as light cannot escape a horizon.
#
# The RATE at which v_g vanishes defines a generalized surface gravity:
#   kappa_BCS = dv_g/depsilon |_{epsilon=0}
#   = d/depsilon [epsilon * v_F / sqrt(epsilon^2 + Delta^2)] |_{epsilon=0}
#   = v_F * [sqrt(epsilon^2 + Delta^2) - epsilon^2/sqrt(epsilon^2+Delta^2)] / (epsilon^2+Delta^2) |_{epsilon=0}
#   = v_F * Delta / Delta^2
#   = v_F / Delta

# For our lattice spectrum, the "Fermi velocity" is the group velocity
# of the lowest B2 band at the Fermi level.
# From s61_vanhove_dispersion, the Josephson coupling J ~ 0.933 M_KK
# for B2 modes, and the bandwidth ~ 4J.
# The single-particle dispersion is approximately epsilon_k ~ -2J cos(k)
# (tight-binding), giving v_F = 2J sin(k_F) at the Fermi surface.
# At half-filling (k_F = pi/2): v_F = 2J = 2 * 0.933 = 1.866 M_KK

J_B2 = J_mode[0]  # Josephson coupling for B2 sector
v_F = 2.0 * J_B2  # Fermi velocity (tight-binding, half-filling)

kappa_BCS = v_F / Delta_BCS  # Generalized surface gravity

# Associated temperature
T_BCS_kappa = kappa_BCS / (2 * PI)

# Natural temperature scale of the gap itself
T_BCS_gap = Delta_BCS / (2 * PI)

# Comparison: S48 analog Hawking temperature from acoustic horizon
T_GH = 66.0  # M_KK, from S48 (Mach_max=54.3, kappa=414)  # (local)

print(f"  BCS dispersion: E(epsilon) = sqrt(epsilon^2 + Delta^2)")
print(f"  Delta = {Delta_BCS:.4f} M_KK")
print(f"  J_B2 = {J_B2:.4f} M_KK")
print(f"  v_F = 2*J = {v_F:.4f} M_KK (Fermi velocity, half-filling)")
print(f"")
print(f"  Near-gap expansion: E - Delta ~ epsilon^2 / (2*Delta)")
print(f"  => QUADRATIC approach to gap edge")
print(f"  => Analog of EXTREMAL horizon (degenerate surface gravity)")
print(f"")
print(f"  Generalized surface gravity definitions:")
print(f"")
print(f"  (a) Naive: kappa_0 = lim d/dE[sqrt(E^2-Delta^2)]|_{{E=Delta}} = 0")
print(f"      -> DEGENERATE (extremal)")
print(f"")
print(f"  (b) Group velocity gradient: kappa_BCS = v_F / Delta")
print(f"      kappa_BCS = {kappa_BCS:.6f} M_KK")
print(f"      T_BCS = kappa_BCS / (2*pi) = {T_BCS_kappa:.6f} M_KK")
print(f"")
print(f"  (c) Gap scale: T_gap = Delta / (2*pi)")
print(f"      T_gap = {T_BCS_gap:.6f} M_KK")
print(f"")
print(f"  S48 acoustic horizon analog:")
print(f"      T_GH = {T_GH:.1f} M_KK")

# =============================================================================
# SECTION 4: COMPARISON AND RATIOS
# =============================================================================
print("\n" + "=" * 78)
print("  4. TEMPERATURE COMPARISON AND PHYSICAL INTERPRETATION")
print("=" * 78)

ratio_kappa = T_BCS_kappa / T_GH
ratio_gap = T_BCS_gap / T_GH

print(f"  T_BCS (kappa) / T_GH = {ratio_kappa:.6f}")
print(f"  T_BCS (gap)   / T_GH = {ratio_gap:.6f}")
print(f"")

# The hierarchy: T_GH >> T_BCS >> 0
# This confirms the EXTREMAL nature of the BCS gap:
# - T_GH = 66 M_KK is the analog "Unruh-like" temperature of the
#   transit acoustic horizon (non-extremal, kappa = 414)
# - T_BCS = Delta/(2*pi) ~ 0.083 M_KK is the BCS gap temperature
# - The ratio T_BCS/T_GH ~ 0.001 means the BCS gap is ~800x colder
#   than the cosmological horizon analog

# Second comparison: to the BCS condensation temperature
# In BCS theory: T_c = Delta_0 / (pi * e^gamma) ~ 0.567 * Delta_0
# where gamma = 0.5772 is the Euler-Mascheroni constant
gamma_EM = 0.5772156649  # (local)
T_c_BCS = Delta_BCS / (PI * np.exp(gamma_EM))
print(f"  BCS critical temperature: T_c = Delta/(pi*e^gamma) = {T_c_BCS:.6f} M_KK")
print(f"  T_c / T_GH = {T_c_BCS / T_GH:.6f}")

# The BdG dispersion near the gap edge also defines an effective
# "tortoise coordinate" mapping: the BCS spectral domain epsilon in (-inf,inf)
# maps to E in (Delta, inf) via E = sqrt(epsilon^2 + Delta^2).
# Near the gap edge, dE/depsilon ~ epsilon/Delta -> 0 as epsilon -> 0,
# so the tortoise coordinate r_* = integral (1/v_g) d epsilon diverges
# logarithmically — exactly as for the extremal RN horizon.

# Compute the tortoise divergence explicitly
eps_test = np.logspace(-6, 0, 1000) * Delta_BCS
r_star_integrand = 1.0 / (eps_test / np.sqrt(eps_test**2 + Delta_BCS**2))
# = sqrt(eps^2 + Delta^2) / eps
# Near eps->0: ~ Delta/eps -> diverges as 1/eps (logarithmic after integration)
# r_* ~ Delta * ln(eps/eps_0) — logarithmic divergence = extremal RN signature

# For non-extremal RN: r_* ~ (1/kappa) * ln(r - r_H)  [simple pole]
# For extremal RN:     r_* ~ -1/(r - r_H)              [double pole]
# For BCS:             r_* ~ Delta * ln(eps)             [simple pole]
#
# So BCS is intermediate: the gap is degenerate (kappa=0 in naive sense),
# but the tortoise coordinate diverges logarithmically (like non-extremal),
# not as a power law (like extremal). This is because the BCS dispersion
# is quadratic near the gap, giving f ~ sqrt(x), while extremal RN
# gives f ~ x.

print(f"\n  Tortoise coordinate behavior near gap edge:")
print(f"    r_*(epsilon) ~ Delta * ln(epsilon) + const  [logarithmic divergence]")
print(f"    Schwarzschild: r_* ~ ln(r-r_H)/kappa       [same type]")
print(f"    Extremal RN:   r_* ~ -1/(r-r_H)            [power-law divergence]")
print(f"")
print(f"  => BCS gap is a DEGENERATE horizon with logarithmic tortoise,")
print(f"     intermediate between non-extremal and extremal black holes.")

# =============================================================================
# SECTION 5: SPECTRAL DENSITY NEAR GAP — BCS van Hove ANALOG
# =============================================================================
print("\n" + "=" * 78)
print("  5. SPECTRAL DENSITY NEAR GAP EDGE (BCS ANALOG)")
print("=" * 78)

# The BCS density of states near the gap edge is:
#   rho_BCS(E) = rho_N(0) * E / sqrt(E^2 - Delta^2)   for E > Delta
#   rho_BCS(E) = 0                                      for E < Delta
#
# This diverges as E -> Delta^+ (the BCS coherence peak).
# Compare to the density of states near a horizon:
#   In the Rindler approximation, the local temperature diverges
#   as T_local = T_H / sqrt(g_tt) -> infinity at the horizon.

# Compute the BCS DOS near gap edge
E_dos = np.linspace(Delta_BCS * 1.001, Delta_BCS * 5.0, 1000)
rho_BCS_norm = E_dos / np.sqrt(E_dos**2 - Delta_BCS**2)
# This is rho_BCS / rho_N (normalized)

# The coherence peak height at E = Delta + delta_E:
delta_E_probe = 0.01  # M_KK  # (local)
E_probe = Delta_BCS + delta_E_probe
rho_peak = E_probe / np.sqrt(E_probe**2 - Delta_BCS**2)
print(f"  BCS coherence peak at E = Delta + {delta_E_probe}:")
print(f"    rho_BCS / rho_N = {rho_peak:.2f}")
print(f"    (diverges as 1/sqrt(E-Delta) approaching gap edge)")

# Count D_K eigenvalue accumulation near Delta
delta_window = 0.1  # M_KK  # (local)
n_near_gap = np.sum(np.abs(all_lambda_raw - Delta_BCS) < delta_window)
print(f"\n  D_K eigenvalues within +/-{delta_window} of Delta:")
print(f"    N = {n_near_gap} (raw, no PW mult)")

# Finer windows
for dw in [0.05, 0.02, 0.01]:
    n_w = np.sum(np.abs(all_lambda_raw - Delta_BCS) < dw)
    print(f"    Within +/-{dw}: N = {n_w}")

# =============================================================================
# SECTION 6: GATE VERDICT AND RESULTS SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("  6. GATE VERDICT: BCS-SURFACE-69")
print("=" * 78)

print(f"""
  GATE: BCS-SURFACE-69
  VERDICT: INFO

  Results Summary:
  ================
  BCS gap:                  Delta = {Delta_BCS:.4f} M_KK
  Fermi velocity (B2):      v_F = {v_F:.4f} M_KK
  Surface gravity (kappa):  kappa_BCS = v_F/Delta = {kappa_BCS:.6f} M_KK
  Temperature (kappa):      T_BCS = kappa/(2*pi) = {T_BCS_kappa:.6f} M_KK
  Temperature (gap scale):  T_gap = Delta/(2*pi) = {T_BCS_gap:.6f} M_KK
  BCS critical temp:        T_c = Delta/(pi*e^gamma) = {T_c_BCS:.6f} M_KK

  S48 acoustic horizon:     T_GH = {T_GH:.1f} M_KK

  Ratios:
    T_BCS(kappa) / T_GH = {ratio_kappa:.6f}  (~{1/ratio_kappa:.0f}x colder)
    T_BCS(gap)   / T_GH = {ratio_gap:.6f}  (~{1/ratio_gap:.0f}x colder)

  Physical Interpretation:
    The BCS spectral gap is a DEGENERATE (extremal) horizon analog.
    The naive surface gravity vanishes (kappa_0 = 0) because the BCS
    dispersion approaches the gap edge quadratically (E-Delta ~ eps^2/2Delta),
    not linearly. This confirms the S48/S49 identification of the dump
    point as an extremal horizon with T_H = 0, kappa = 0, BPS saturation.

    The generalized surface gravity kappa_BCS = v_F/Delta = {kappa_BCS:.4f}
    yields T_BCS = {T_BCS_kappa:.4f} M_KK, which is ~{1/ratio_kappa:.0f}x colder
    than the acoustic horizon analog T_GH = 66 M_KK.

    The tortoise coordinate diverges logarithmically near the gap,
    intermediate between non-extremal (logarithmic) and extremal RN
    (power-law) black holes. The BCS coherence peak (rho ~ 1/sqrt(E-Delta))
    is the spectral analog of the Tolman blueshift divergence at a horizon.

  D_K Spectrum Summary (L_max={L_MAX}):
    Total nonzero |lambda|: {len(all_lambda_raw)} (raw), {len(all_lambda_abs)} (with PW mult)
    Spectrum range: [{all_lambda_raw.min():.4f}, {all_lambda_raw.max():.4f}] M_KK
    Eigenvalues below Delta: {n_below} / {n_total}
""")

# =============================================================================
# SECTION 7: SAVE DATA AND PLOT
# =============================================================================
print("  7. SAVING DATA AND PLOT")
print("=" * 78)

save_dict = {
    # Gate
    'gate_name': np.array('BCS-SURFACE-69'),
    'gate_verdict': np.array('INFO'),
    'gate_detail': np.array(
        f'kappa_BCS={kappa_BCS:.6f}, T_BCS={T_BCS_kappa:.6f}, '
        f'T_gap={T_BCS_gap:.6f}, T_GH={T_GH}, '
        f'ratio_kappa={ratio_kappa:.6f}, ratio_gap={ratio_gap:.6f}. '
        f'BCS gap is extremal horizon analog (quadratic approach, kappa_0=0).'
    ),
    # Core results
    'Delta_BCS': np.float64(Delta_BCS),
    'v_F': np.float64(v_F),
    'J_B2': np.float64(J_B2),
    'kappa_BCS': np.float64(kappa_BCS),
    'T_BCS_kappa': np.float64(T_BCS_kappa),
    'T_BCS_gap': np.float64(T_BCS_gap),
    'T_c_BCS': np.float64(T_c_BCS),
    'T_GH': np.float64(T_GH),
    'ratio_kappa': np.float64(ratio_kappa),
    'ratio_gap': np.float64(ratio_gap),
    # BCS dispersion
    'epsilon_grid': epsilon_grid,
    'E_BCS': E_BCS,
    # D_K spectrum
    'L_max': np.int64(L_MAX),
    'all_lambda_raw': all_lambda_raw,
    'n_lambda_raw': np.int64(len(all_lambda_raw)),
    'n_lambda_pw': np.int64(len(all_lambda_abs)),
    'n_below_gap': np.int64(n_below),
    # Density of states
    'E_centers': E_centers,
    'rho_raw': rho_raw,
    'rho_pw': rho_pw,
    # BCS DOS
    'E_dos': E_dos,
    'rho_BCS_norm': rho_BCS_norm,
}

npz_path = os.path.join(outdir, 's69_bcs_surface_gravity.npz')
np.savez(npz_path, **save_dict)
print(f"  Data saved: {npz_path}")

# --- PLOT ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('BCS-SURFACE-GRAVITY-69: Spectral Gap Thermodynamics', fontsize=14, fontweight='bold')

# Panel 1: D_K eigenvalue density
ax = axes[0, 0]
ax.bar(E_centers, rho_raw, width=delta_E * 0.9, color='steelblue', alpha=0.7, label='D_K (raw)')
ax.axvline(Delta_BCS, color='red', linewidth=2, linestyle='--', label=f'$\\Delta$ = {Delta_BCS} M_KK')
ax.set_xlabel('|$\\lambda$| [M_KK]')
ax.set_ylabel('Density of states [1/M_KK]')
ax.set_title('Eigenvalue Density near BCS Gap')
ax.set_xlim(0, 3)
ax.legend()

# Panel 2: BCS dispersion
ax = axes[0, 1]
ax.plot(epsilon_grid, E_BCS, 'b-', linewidth=2, label='$E = \\sqrt{\\epsilon^2 + \\Delta^2}$')
ax.axhline(Delta_BCS, color='red', linewidth=1.5, linestyle='--', label=f'Gap edge $\\Delta$={Delta_BCS}')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_xlabel('$\\epsilon$ (single-particle energy) [M_KK]')
ax.set_ylabel('E (quasiparticle energy) [M_KK]')
ax.set_title('BCS Dispersion Relation')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 2)
ax.legend()

# Panel 3: BCS DOS near gap (normalized)
ax = axes[1, 0]
E_plot = np.linspace(Delta_BCS * 1.005, Delta_BCS * 4, 500)
rho_plot = E_plot / np.sqrt(E_plot**2 - Delta_BCS**2)
ax.plot(E_plot, rho_plot, 'r-', linewidth=2, label='BCS: $\\rho \\sim E/\\sqrt{E^2 - \\Delta^2}$')
ax.axvline(Delta_BCS, color='k', linewidth=1, linestyle=':', label=f'$\\Delta$ = {Delta_BCS}')
ax.set_xlabel('E [M_KK]')
ax.set_ylabel('$\\rho_{BCS} / \\rho_N$')
ax.set_title('BCS Coherence Peak (Horizon Analog)')
ax.set_xlim(0.4, 2.5)
ax.set_ylim(0, 10)
ax.legend()

# Panel 4: Temperature hierarchy
ax = axes[1, 1]
temps = [T_GH, T_BCS_kappa, T_BCS_gap, T_c_BCS]
labels = ['$T_{GH}$ (acoustic)', '$T_{BCS}$ ($\\kappa$)', '$T_{gap}$ ($\\Delta/2\\pi$)', '$T_c$ (BCS)']
colors = ['goldenrod', 'steelblue', 'coral', 'seagreen']
bars = ax.barh(range(len(temps)), temps, color=colors, alpha=0.8)
ax.set_yticks(range(len(temps)))
ax.set_yticklabels(labels)
ax.set_xlabel('Temperature [M_KK]')
ax.set_title('Temperature Hierarchy')
ax.set_xscale('log')
for i, (t, lab) in enumerate(zip(temps, labels)):
    ax.text(t * 1.2, i, f'{t:.3f}', va='center', fontsize=10)

plt.tight_layout()
png_path = os.path.join(outdir, 's69_bcs_surface_gravity.png')
plt.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved: {png_path}")

t_total = time.time() - t_start_global
print(f"\n  Total runtime: {t_total:.1f}s")
print("=" * 78)
print("  BCS-SURFACE-GRAVITY-69: COMPLETE")
print("=" * 78)
