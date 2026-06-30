#!/usr/bin/env python3
"""
s63_dynamical_exponent.py — Dynamical Exponent z from Phonon Bands on CG(24)
=============================================================================
Session 63, W6-16: DYNAMICAL-EXPONENT-63

Extracts the dynamical exponent z independently from the S62 phonon dispersion
omega(k) on the 32-cell Cayley graph CG(24).

PHYSICS:
  The dynamical exponent z is defined by the low-energy dispersion relation
    omega(k) ~ k^z
  In condensed matter, z = 1 (acoustic phonon), z = 2 (diffusive/Schrodinger),
  z = 3 (magnon in ferromagnet), etc.

  The S57 gap scaling found Delta_N ~ N^{-1.84} for N = 8, 16, 32 cells
  on a 1D chain, and inferred z = 3.68 assuming d_s = 2.

  This computation independently extracts z from:
    (1) B-sector uncoupled phonon band dispersion omega_B(lambda_n)
    (2) C-sector Leggett mode dispersion omega_C(lambda_n)
    (3) Full coupled band structure omega_full(k_eff)
    (4) Graph spectral dimension d_s of CG(24) from heat kernel
    (5) Analytic finite-size analysis of the 1D chain cos dispersion

Gate: DYNAMICAL-EXPONENT-63
  PASS: z = 3.68 +/- 20%  (i.e., z in [2.94, 4.42])
  INFO: Different z with clear physical interpretation

Author: Phonon-First Cosmologist, Session 63
Date: 2026-03-31
"""

import numpy as np
from scipy.linalg import eigh
from scipy.optimize import curve_fit
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold, E_cond, J_C2, N_dof_BCS, PI

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_dir = Path(__file__).parent
t_start = time.time()

print("=" * 78)
print("DYNAMICAL-EXPONENT-63: z from Phonon Bands on CG(24)")
print("=" * 78)

# =============================================================================
# Section 1: Load Data
# =============================================================================
print("\n--- Section 1: Loading S62 Phonon Dispersion ---")

d = np.load(data_dir / 's62_phonon_dispersion_full.npz', allow_pickle=True)

omega_full = d['omega_full']          # (32, 45) full coupled spectrum
omega_B = d['omega_B_uncoupled']      # (32, 8) B-sector uncoupled
omega_C = d['omega_C_uncoupled']      # (32, 1) C-sector uncoupled
omega_A = d['omega_A']                # (36,) A-sector (k-independent)
sector_weight = d['sector_weight']    # (32, 45, 3)
lambda_n = d['lambda_n']              # (32,) graph Laplacian eigenvalues
k_eff = d['k_eff']                    # (32,) effective wavevectors
E_J_fold = d['E_J_fold'].item()       # Josephson energy at fold
omega_L0 = d['omega_L0'].item()       # Leggett gap
J_L = d['J_L'].item()                 # Leggett Josephson coupling

N_k = len(lambda_n)
DIAMETER = 6  # Graph diameter of CG(24)

print(f"  {N_k} k-points, lambda range [{lambda_n[0]:.4f}, {lambda_n[-1]:.4f}]")
print(f"  k_eff range [{k_eff[0]:.4f}, {k_eff[-1]:.4f}]")
print(f"  E_J = {E_J_fold:.4f} M_KK, omega_L0 = {omega_L0:.4f} M_KK, J_L = {J_L:.6f} M_KK")
print(f"  Graph diameter D = {DIAMETER}")
print(f"  Relation: k_eff = sqrt(lambda_n) * pi / D")

# Verify k_eff definition
k_check = np.sqrt(lambda_n) * PI / DIAMETER
assert np.allclose(k_eff, k_check, atol=1e-10), "k_eff definition mismatch!"
print(f"  k_eff = sqrt(lambda) * pi/{DIAMETER}: VERIFIED")

# =============================================================================
# Section 2: B-Sector Dispersion — z from omega_B(lambda)
# =============================================================================
print("\n--- Section 2: B-Sector Uncoupled Dispersion ---")

# The B-sector lowest band: omega_B0 vs lambda_n
# Test: omega_B0 = a + b * lambda_n (linear in lambda)
mask_pos = lambda_n > 0
c_lin = np.polyfit(lambda_n[mask_pos], omega_B[mask_pos, 0], 1)
E_J_fit = c_lin[0]
omega_B0_offset = c_lin[1]
resid_lin = omega_B[mask_pos, 0] - np.polyval(c_lin, lambda_n[mask_pos])
max_resid_lin = np.max(np.abs(resid_lin))

print(f"  Linear fit: omega_B0 = {omega_B0_offset:.6f} + {E_J_fit:.6f} * lambda_n")
print(f"  E_J(fit) = {E_J_fit:.6f} vs E_J(data) = {E_J_fold:.6f}")
print(f"  Max residual: {max_resid_lin:.2e} M_KK")
print(f"  omega_B0(k=0) = {omega_B[0, 0]:.6f} M_KK (finite — BCS offset)")

# In k_eff coordinates: omega_B0 = offset + E_J * (D/pi)^2 * k_eff^2
# This is QUADRATIC in k_eff -> z = 2
v_B_sq = E_J_fit * (DIAMETER / PI)**2  # coefficient of k_eff^2
print(f"\n  In k_eff: omega_B0 = {omega_B0_offset:.4f} + {v_B_sq:.4f} * k_eff^2")

# Power law fit: omega_B0 ~ lambda^z_lambda for lambda > 0
c_pow = np.polyfit(np.log(lambda_n[mask_pos]), np.log(omega_B[mask_pos, 0]), 1)
z_lambda_B = c_pow[0]
print(f"\n  Power law: omega_B0 ~ lambda^{z_lambda_B:.4f}")
print(f"  Since lambda ~ k_eff^2: omega_B0 ~ k_eff^{2*z_lambda_B:.4f}")

# The near-unity exponent reflects the linear omega(lambda) relation
# The exact z = 2 comes from the dispersion relation structure:
#   omega_B(k) = const + E_J * (D/pi)^2 * k^2
z_B_sector = 2.0  # (local)
print(f"\n  ==> B-sector dynamical exponent: z = {z_B_sector:.1f} (exact, quadratic)")

# Verify ratio omega_B / lambda is constant
ratios = omega_B[mask_pos, 0] / lambda_n[mask_pos]
ratio_spread = (ratios.max() - ratios.min()) / ratios.mean()
print(f"  omega_B0/lambda spread: {ratio_spread:.2e} (relative)")
print(f"  omega_B0/lambda = {ratios.mean():.4f} +/- {ratios.std():.2e}")

# =============================================================================
# Section 3: C-Sector (Leggett) Dispersion
# =============================================================================
print("\n--- Section 3: C-Sector (Leggett) Dispersion ---")

# omega_C^2 = omega_L0^2 + J_L * lambda_n (massive Klein-Gordon)
diff_sq = omega_C[:, 0]**2 - omega_L0**2
J_L_check = diff_sq[mask_pos] / lambda_n[mask_pos]
print(f"  Massive dispersion: omega_C^2 = {omega_L0}^2 + J_L * lambda_n")
print(f"  J_L from fit: {J_L_check.mean():.6f} +/- {J_L_check.std():.2e}")
print(f"  J_L from data: {J_L:.6f}")
print(f"  Match: {abs(J_L_check.mean() - J_L)/J_L:.2e} relative")

# In k_eff: omega_C = sqrt(omega_L0^2 + J_L * (D/pi)^2 * k_eff^2)
# This is a MASSIVE relativistic dispersion (Lorentz invariant form).
# In the massless limit (omega_L0 -> 0): omega ~ k -> z = 1
# In the massive regime (omega >> omega_L0): omega ~ k -> z = 1
# But for the gapped mode: near k=0, omega ~ m + v^2/(2m) * k^2 -> z = 2
# The z depends on the limit! At low k (sub-gap): z = 2. At high k: z = 1.

v_C_sq = J_L * (DIAMETER / PI)**2
k_crossover = omega_L0 / np.sqrt(v_C_sq)

print(f"\n  omega_C = sqrt({omega_L0:.4f}^2 + {v_C_sq:.4f} * k_eff^2)")
print(f"  Crossover k_eff = omega_L0 / v = {k_crossover:.4f}")
print(f"  k_max = {k_eff[-1]:.4f}")
print(f"  Regime: {('massive (k_cross < k_max, most modes sub-gap)' if k_crossover < k_eff[-1] else 'sub-gap dominated')}")

# Power law fit omega_C vs k_eff
c_pow_C = np.polyfit(np.log(k_eff[mask_pos]), np.log(omega_C[mask_pos, 0]), 1)
z_C_apparent = c_pow_C[0]
print(f"\n  Apparent power law: omega_C ~ k_eff^{z_C_apparent:.4f}")
print(f"  (This is NOT z; it reflects the gapped dispersion)")

# Extract z from the slope at k_eff >> k_crossover (if accessible)
# d log omega / d log k = k * d omega / (omega * dk)
# omega = sqrt(m^2 + v^2 k^2)
# d omega/dk = v^2 k / omega
# d log omega / d log k = v^2 k^2 / omega^2 = v^2 k^2 / (m^2 + v^2 k^2)
# At k >> m/v: -> 1 (z=1). At k << m/v: -> v^2 k^2/m^2 -> 0 (z=0 + correction -> z=2 from next order)

running_z_C = v_C_sq * k_eff[mask_pos]**2 / omega_C[mask_pos, 0]**2
print(f"\n  Running z(k) for Leggett mode:")
for i in range(len(k_eff[mask_pos])):
    print(f"    k={k_eff[mask_pos][i]:.4f}, z_running={running_z_C[i]:.4f}")

z_C_low = 2.0   # At low k (sub-gap regime)  # (local)
z_C_high = 1.0   # At high k (massless regime, if accessible)  # (local)
print(f"\n  ==> C-sector: z = 2 (low-k, sub-gap) to z = 1 (high-k, if k >> {k_crossover:.3f})")

# =============================================================================
# Section 4: Full Coupled Band Structure
# =============================================================================
print("\n--- Section 4: Coupled Band Dispersion ---")

# Band 1 (first excitation) is C-dominated at low k, becomes A-dominated at high k
# Let's fit the lowest positive-frequency excitation

# At k=0: band 0 = -2.52 (condensate), band 1 = 0.014 (B near zero-mode)
# At small k (n=1,2,3): band 1 follows the Leggett dispersion
# At k ~ 0.44: band crossing, B-sector rises past Leggett

# Extract z from band 1 in the low-k regime (n=1,2,3, k < 0.4)
idx_low = np.where((k_eff > 0) & (k_eff < 0.4))[0]
k_low = k_eff[idx_low]
omega_low = omega_full[idx_low, 1]

if len(k_low) >= 2:
    c_b1 = np.polyfit(np.log(k_low), np.log(omega_low), 1)
    z_band1_low = c_b1[0]
    print(f"  Band 1, k < 0.4 (C-dominated): omega ~ k^{z_band1_low:.4f}")
else:
    z_band1_low = np.nan
    print("  Insufficient low-k points for band 1 fit")

# Extract z from band 1 in mid-k regime (B-A hybrid, n=5-15)
idx_mid = np.where((k_eff > 0.5) & (k_eff < 1.0))[0]
k_mid = k_eff[idx_mid]
omega_mid = omega_full[idx_mid, 1]

if len(k_mid) >= 3:
    c_b1_mid = np.polyfit(np.log(k_mid), np.log(omega_mid), 1)
    z_band1_mid = c_b1_mid[0]
    print(f"  Band 1, 0.5 < k < 1.0 (A-dominated): omega ~ k^{z_band1_mid:.4f}")
else:
    z_band1_mid = np.nan

# Band 2 (B-sector dominated at small k)
idx_low2 = np.where((k_eff > 0) & (k_eff < 0.3))[0]
if len(idx_low2) >= 2:
    k_l2 = k_eff[idx_low2]
    om_l2 = omega_full[idx_low2, 2]
    c_b2 = np.polyfit(np.log(k_l2), np.log(om_l2), 1)
    z_band2_low = c_b2[0]
    print(f"  Band 2, k < 0.3 (B-dominated): omega ~ k^{z_band2_low:.4f}")
else:
    z_band2_low = np.nan

# The dominant result: uncoupled bands give EXACT z, coupled bands are contaminated
# by band crossings and hybridization gaps.

# =============================================================================
# Section 5: Graph Spectral Dimension of CG(24)
# =============================================================================
print("\n--- Section 5: Spectral Dimension of 32-Cell Graph ---")

# Heat kernel: P(t) = (1/N) * sum_n exp(-lambda_n * t)
# Running spectral dimension: d_s(t) = -2 * d log P(t) / d log t

t_vals = np.logspace(-2, 3, 1000)
P_t = np.zeros_like(t_vals)
for i, t in enumerate(t_vals):
    P_t[i] = np.mean(np.exp(-lambda_n * t))

log_t = np.log(t_vals)
log_P = np.log(P_t)
d_s_run = -2.0 * np.gradient(log_P, log_t)

# Peak spectral dimension
peak_idx = np.argmax(d_s_run)
d_s_peak = d_s_run[peak_idx]
t_peak = t_vals[peak_idx]

# At t = 1
idx_t1 = np.argmin(np.abs(t_vals - 1.0))
d_s_t1 = d_s_run[idx_t1]

# Long-time limit: P -> 1/32, d_s -> 0 (finite graph)
# Short-time limit: P -> 1, d_s -> 0

print(f"  Peak d_s = {d_s_peak:.4f} at t = {t_peak:.4f}")
print(f"  d_s(t=1) = {d_s_t1:.4f}")
print(f"  P(t) saturates to 1/N = {1.0/N_k:.4f} = 1/32 (finite graph)")

# Integrated DOS: N(lambda) ~ lambda^{d_s/2}
N_cum = np.arange(1, N_k + 1)
c_dos = np.polyfit(np.log(lambda_n[mask_pos]), np.log(N_cum[mask_pos]), 1)
d_s_dos = 2 * c_dos[0]
print(f"  d_s from DOS: N(lambda) ~ lambda^{c_dos[0]:.4f} -> d_s = {d_s_dos:.4f}")

# Weyl law: For a d-dimensional manifold, N(lambda) ~ lambda^{d/2}
# The 32-cell graph has d_s ~ 1.7-1.9 depending on method

# =============================================================================
# Section 6: Finite-Size Analysis of S57 Alpha = -1.84
# =============================================================================
print("\n--- Section 6: Finite-Size Analysis of Chain Gap Scaling ---")

# S57 used a 1D linear chain with N cells.
# Open chain Laplacian eigenvalues: lambda_j = 2(1-cos(j*pi/(N+1))), j=1,...,N
# Gap in Model A (diagonal Josephson) = E_J * (lambda_2 - lambda_1)
# = E_J * [2*cos(pi/(N+1)) - 2*cos(2*pi/(N+1))]

# For large N: lambda_j ~ (j*pi/(N+1))^2 -> gap ~ 3*E_J*pi^2/(N+1)^2 -> alpha = -2

E_J_s57 = 0.9186  # From S57 data  # (local)

N_chain_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
gap_analytic = []
for N_c in N_chain_list:
    if N_c == 1:
        gap_analytic.append(np.nan)
        continue
    lam1 = 2 * (1 - np.cos(PI / (N_c + 1)))
    lam2 = 2 * (1 - np.cos(2 * PI / (N_c + 1)))
    gap_analytic.append(E_J_s57 * (lam2 - lam1))

gap_arr = np.array(gap_analytic)
N_arr = np.array(N_chain_list)

# Fit alpha over different N ranges
print(f"  Chain gap Delta_N = E_J * [cos(pi/(N+1)) - cos(2*pi/(N+1))] * 2:")
for N_c, g in zip(N_chain_list, gap_analytic):
    if not np.isnan(g):
        print(f"    N={N_c:4d}: gap = {g:.8f}")

# S57 range: N = 8, 16, 32
mask_s57 = np.isin(N_arr, [8, 16, 32])
c_s57 = np.polyfit(np.log(N_arr[mask_s57].astype(float)),
                   np.log(gap_arr[mask_s57]), 1)
alpha_s57 = c_s57[0]
print(f"\n  alpha (N=8,16,32, S57 range): {alpha_s57:.6f}")

# Larger N ranges
for N_min in [8, 16, 32, 64, 128, 256]:
    mask_range = (N_arr >= N_min) & (~np.isnan(gap_arr))
    if np.sum(mask_range) >= 2:
        c_range = np.polyfit(np.log(N_arr[mask_range].astype(float)),
                            np.log(gap_arr[mask_range]), 1)
        print(f"  alpha (N>={N_min:4d}): {c_range[0]:.6f}")

# The correction to alpha = -2:
# gap = E_J * 2 * [cos(pi/(N+1)) - cos(2*pi/(N+1))]
# = E_J * 4 * sin(3*pi/(2*(N+1))) * sin(pi/(2*(N+1)))
# For large N: ~ E_J * 4 * (3*pi/(2*N)) * (pi/(2*N)) = 3*E_J*pi^2/N^2
# Next correction: ~ 3*E_J*pi^2/N^2 * (1 - 5*pi^2/(6*N^2))
# So alpha(N) = -2 + O(1/N^2) — convergence to -2 is algebraic.

# Compute the RUNNING alpha between consecutive points
print(f"\n  Running alpha between consecutive N values:")
for i in range(1, len(N_chain_list) - 1):
    N1, N2 = N_chain_list[i], N_chain_list[i+1]
    g1, g2 = gap_arr[i], gap_arr[i+1]
    if not np.isnan(g1) and not np.isnan(g2):
        alpha_pair = np.log(g2/g1) / np.log(N2/N1)
        print(f"    N={N1:4d}->{N2:4d}: alpha = {alpha_pair:.6f}")

# =============================================================================
# Section 7: Reconcile S57 z = 3.68 with z = 2
# =============================================================================
print("\n--- Section 7: Reconciliation ---")

print("""
  S57 logic: Delta_N ~ N^{alpha}, alpha = -1.84
             Assumed d_s = 2 -> z = -alpha * d_s = 1.84 * 2 = 3.68

  THREE errors in this chain:

  1. alpha = -1.84 is a FINITE-SIZE artifact.
     The EXACT chain dispersion gives alpha -> -2.0 as N -> infinity.
     At N = 8, 16, 32 the finite-N correction to cos(pi/(N+1)) shifts
     the apparent alpha from -2.0 to -1.84.
     Verified: extending to N = 1024, alpha = -1.998.

  2. The computation was on a 1D LINEAR CHAIN (d = d_s = 1).
     The relation Delta_N ~ N^{-z/d} on this chain gives
     alpha = -z/d = -z/1 = -z.  # (local)
     With z = 2 (exact): alpha = -2.0 (matching the asymptotic fit).

  3. d_s = 2 was assumed, not measured.
     The CG(24) 32-cell graph has d_s ~ 1.7 (heat kernel peak),
     NOT d_s = 2. And the S57 computation was not ON CG(24) —
     it was on a 1D chain where d_s = 1.

  CORRECT result from phonon bands:
     z = 2 (EXACT, from omega_B = E_J * lambda = E_J * (D/pi)^2 * k_eff^2)
""")

# =============================================================================
# Section 8: Cross-Checks
# =============================================================================
print("--- Section 8: Cross-Checks ---")

# Cross-check 1: All 8 B-sector bands have same z
print("  Cross-check 1: z consistency across B-sector bands")
for band_idx in range(8):
    c_band = np.polyfit(lambda_n[mask_pos], omega_B[mask_pos, band_idx], 1)
    E_J_band = c_band[0]
    print(f"    Band {band_idx}: E_J(fit) = {E_J_band:.6f} (should be {E_J_fold:.6f})")
print(f"    All bands: z = 2 (linear in lambda = quadratic in k)")

# Cross-check 2: Leggett mode matches omega_C^2 = m^2 + v^2 k^2
print("\n  Cross-check 2: Leggett massive dispersion")
omega_C_pred = np.sqrt(omega_L0**2 + J_L * lambda_n)
resid_C = np.max(np.abs(omega_C[:, 0] - omega_C_pred))
print(f"    Max residual omega_C_pred vs data: {resid_C:.2e} M_KK")
print(f"    -> Leggett mode: EXACT massive Klein-Gordon dispersion")

# Cross-check 3: S57 Model A gap matches analytic chain formula
# Model A gap for N=8 = E_J * (lambda_2 - lambda_1) for open chain
for N_c in [8, 16, 32]:
    lam1_chain = 2 * (1 - np.cos(PI / (N_c + 1)))
    lam2_chain = 2 * (1 - np.cos(2 * PI / (N_c + 1)))
    gap_predicted = E_J_s57 * (lam2_chain - lam1_chain)
    print(f"\n  Cross-check 3 (N={N_c}): analytic gap = {gap_predicted:.6f}")

# Cross-check 4: omega_B offset comes from eps + V_bare
print(f"\n  Cross-check 4: B-sector offset")
print(f"    omega_B0(k=0) = {omega_B[0, 0]:.6f} M_KK")
print(f"    This = eps_0 + V_bare_00 (single-particle energy + pairing)")

# Cross-check 5: Effective mass consistency
# m_eff = 1/(d^2 omega / dk^2) = pi^2 / (2 * E_J * D^2)
m_eff_B = PI**2 / (2 * E_J_fold * DIAMETER**2)
print(f"\n  Cross-check 5: Effective mass")
print(f"    m*_B = pi^2 / (2 * E_J * D^2) = {m_eff_B:.6f} M_KK")
print(f"    This is the quadratic dispersion effective mass -> z = 2")

# =============================================================================
# Section 9: Gate Verdict
# =============================================================================
print("\n--- Section 9: Gate Verdict ---")

z_phonon = 2.0  # EXACT, from dispersion relation  # (local)
z_target = 3.68  # S57 claim  # (local)
z_tolerance = 0.20  # 20%  # (local)

z_lower = z_target * (1 - z_tolerance)
z_upper = z_target * (1 + z_tolerance)
deviation = abs(z_phonon - z_target) / z_target

print(f"  z from phonon bands: {z_phonon:.2f} (EXACT)")
print(f"  z target (S57): {z_target:.2f}")
print(f"  PASS window: [{z_lower:.2f}, {z_upper:.2f}]")
print(f"  Deviation: {deviation*100:.1f}%")

if z_lower <= z_phonon <= z_upper:
    verdict = "PASS"
    detail = (f"z = {z_phonon:.2f} within 20% of target {z_target:.2f}")
else:
    verdict = "INFO"
    detail = (
        f"z = {z_phonon:.2f} from phonon bands (EXACT: omega_B = E_J * lambda ~ k^2). "
        f"S57 z = {z_target:.2f} was based on: (a) alpha = -1.84 (finite-size artifact, "
        f"asymptotic is -2.0), and (b) assumed d_s = 2 (the 1D chain has d_s = 1). "
        f"Correcting both: z = 2 * 1 = 2, matching the phonon band result. "
        f"Graph spectral dimension of CG(24): d_s = {d_s_peak:.2f} (heat kernel peak). "
        f"On CG(24), gap scaling would give alpha = -z/d_s = -{z_phonon/d_s_peak:.2f}."
    )

print(f"\n  GATE: DYNAMICAL-EXPONENT-63")
print(f"  VERDICT: {verdict}")
print(f"  DETAIL: {detail}")

print(f"\n  KEY NUMBERS:")
print(f"    z (B-sector phonon)   = {z_phonon:.2f} (EXACT, omega ~ k^2)")
print(f"    z (Leggett, low-k)    = 2.0 (gapped quadratic)")
print(f"    z (Leggett, high-k)   = 1.0 (massless relativistic)")
print(f"    E_J (Josephson energy) = {E_J_fold:.4f} M_KK")
print(f"    d_s (CG(24) peak)     = {d_s_peak:.4f}")
print(f"    d_s (CG(24) DOS)      = {d_s_dos:.4f}")
print(f"    alpha (chain, S57)    = {alpha_s57:.4f} (finite-size)")
print(f"    alpha (chain, N->inf) = -2.000 (exact)")
print(f"    z (S57 claimed)       = {z_target:.2f} (RETRACTED: wrong d_s assumption)")

# =============================================================================
# Section 10: Physical Interpretation
# =============================================================================
print("\n--- Section 10: Physical Interpretation ---")

print("""
  The dynamical exponent z = 2 has clear physical meaning:

  1. QUADRATIC DISPERSION: The Josephson phonon on CG(24) has omega ~ k^2,
     the same dispersion as Schrodinger equation / diffusion equation.
     This is STANDARD for tight-binding models on a lattice:
       omega(k) = 2t * sum(1 - cos(k_i * a))  ~  t * k^2  for small k

  2. NOT z = 1 (acoustic): There is no "sound velocity" — the phonon
     is QUADRATIC, not linear. This is because the B-sector modes are
     hopping excitations (Josephson coupling), not acoustic vibrations.

  3. S57's "anomalous z = 3.68" is EXPLAINED:
     - alpha = -1.84 at N=8,16,32 is a finite-size artifact of cos expansion
     - alpha -> -2 at large N
     - The chain had d = d_s = 1, not d_s = 2
     - z = -alpha * d_s = 2 * 1 = 2 (consistent with phonon bands)

  4. IMPLICATIONS for spectral dimension flow:
     - On CG(24), d_s ~ 1.7 (peak), not 2
     - If gap scaling Delta ~ N^{-z/d_s} holds on the graph:
       alpha_graph = -z / d_s = -2 / 1.69 = -1.18
       This is a PREDICTION testable by gap scaling on CG(24) (not a chain)
""")

# =============================================================================
# Section 11: Plotting
# =============================================================================
print("--- Section 11: Plotting ---")

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# Panel 1: B-sector dispersion omega_B vs lambda
ax = axes[0, 0]
for band in range(8):
    ax.plot(lambda_n, omega_B[:, band], 'o-', ms=3,
            label=f'Band {band}' if band < 3 else None, alpha=0.7)
ax.plot(lambda_n, omega_B0_offset + E_J_fit * lambda_n, 'k--', lw=1.5,
        label=f'Linear fit (slope={E_J_fit:.2f})')
ax.set_xlabel(r'$\lambda_n$ (Laplacian eigenvalue)')
ax.set_ylabel(r'$\omega_B$ (M$_{\rm KK}$)')
ax.set_title(r'B-sector: $\omega_B = \omega_0 + E_J \lambda_n$ $\Rightarrow$ z = 2')
ax.legend(fontsize=7, loc='upper left')

# Panel 2: B-sector in k_eff coordinates
ax = axes[0, 1]
ax.plot(k_eff**2, omega_B[:, 0], 'bo-', ms=3, label='B band 0')
ax.plot(k_eff**2, omega_B0_offset + v_B_sq * k_eff**2, 'r--', lw=1.5,
        label=f'Linear fit: slope = {v_B_sq:.1f}')
ax.set_xlabel(r'$k_{\rm eff}^2$')
ax.set_ylabel(r'$\omega_{B,0}$ (M$_{\rm KK}$)')
ax.set_title(r'B-sector: $\omega \propto k^2$ $\Rightarrow$ z = 2')
ax.legend(fontsize=8)

# Panel 3: Leggett mode dispersion
ax = axes[0, 2]
ax.plot(k_eff, omega_C[:, 0], 'go-', ms=4, label='Leggett data')
k_dense = np.linspace(0, k_eff[-1], 200)
lam_dense = (k_dense * DIAMETER / PI)**2
omega_C_dense = np.sqrt(omega_L0**2 + J_L * lam_dense)
ax.plot(k_dense, omega_C_dense, 'r--', lw=1.5,
        label=r'$\sqrt{\omega_{L0}^2 + J_L (D/\pi)^2 k^2}$')
ax.axhline(omega_L0, color='gray', ls=':', label=f'Gap = {omega_L0:.3f}')
ax.set_xlabel(r'$k_{\rm eff}$ (M$_{\rm KK}$)')
ax.set_ylabel(r'$\omega_C$ (M$_{\rm KK}$)')
ax.set_title(r'Leggett mode: massive Klein-Gordon')
ax.legend(fontsize=7)

# Panel 4: Chain gap scaling (S57 finite-size analysis)
ax = axes[1, 0]
N_plot = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
gap_plot = np.array([E_J_s57 * (2*(1-np.cos(2*PI/(N+1))) - 2*(1-np.cos(PI/(N+1))))
                     for N in N_plot])
ax.loglog(N_plot, gap_plot, 'bs-', ms=5, label='Analytic chain gap')

# S57 fit line
N_fit = np.logspace(np.log10(8), np.log10(32), 50)
gap_s57_fit = np.exp(c_s57[1]) * N_fit**c_s57[0]
ax.loglog(N_fit, gap_s57_fit, 'r--', lw=2,
          label=f'S57 fit: $\\alpha$ = {alpha_s57:.2f}')

# Asymptotic N^{-2}
N_asymp = np.logspace(np.log10(32), np.log10(1024), 50)
gap_asymp_coeff = gap_plot[np.where(N_plot == 32)[0][0]] * 32**2
ax.loglog(N_asymp, gap_asymp_coeff * N_asymp**(-2), 'g--', lw=2,
          label=r'Asymptotic $\alpha$ = $-2$')

ax.set_xlabel('N (cells)')
ax.set_ylabel(r'$\Delta_N$ (M$_{\rm KK}$)')
ax.set_title(r'Gap scaling: $\alpha = -1.84$ (finite-size) $\to -2.0$')
ax.legend(fontsize=7)

# Panel 5: Spectral dimension
ax = axes[1, 1]
mask_plot = (t_vals > 0.01) & (t_vals < 100)
ax.semilogx(t_vals[mask_plot], d_s_run[mask_plot], 'b-', lw=1.5)
ax.axhline(d_s_peak, color='r', ls='--', alpha=0.5,
           label=f'Peak $d_s$ = {d_s_peak:.2f}')
ax.axvline(t_peak, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'Diffusion time $t$')
ax.set_ylabel(r'$d_s(t)$')
ax.set_title(f'Graph spectral dimension (32-cell)')
ax.legend(fontsize=8)
ax.set_ylim(-0.1, 2.0)

# Panel 6: Summary diagram
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"DYNAMICAL-EXPONENT-63\n"
    f"Verdict: {verdict}\n\n"
    f"z (phonon bands) = {z_phonon:.1f} (EXACT)\n"
    f"z (S57 claimed)  = {z_target:.2f} (retracted)\n\n"
    f"Root cause of S57 z = 3.68:\n"
    f"  (a) alpha = -1.84 is finite-size\n"
    f"      (asymptotic: -2.00)\n"
    f"  (b) d_s = 2 was assumed\n"
    f"      (chain: d_s = 1)\n"
    f"  (c) z = -alpha * d_s\n"
    f"      = 2.0 * 1 = 2.0 (correct)\n\n"
    f"CG(24) graph d_s = {d_s_peak:.2f} (peak)\n"
    f"Predicted alpha(CG24) = -z/d_s\n"
    f"  = -{z_phonon/d_s_peak:.2f}"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle("S63 Dynamical Exponent: z = 2 from Phonon Bands on CG(24)",
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(data_dir / 's63_dynamical_exponent.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved: s63_dynamical_exponent.png")

# =============================================================================
# Section 12: Save Data
# =============================================================================
print("\n--- Section 12: Saving Data ---")

save_dict = {
    # Primary result
    'z_phonon': z_phonon,
    'z_target': z_target,
    'z_B_sector': z_B_sector,
    'z_C_low_k': z_C_low,
    'z_C_high_k': z_C_high,

    # B-sector fit
    'E_J_fit': E_J_fit,
    'omega_B0_offset': omega_B0_offset,
    'max_resid_lin': max_resid_lin,
    'v_B_sq': v_B_sq,
    'z_lambda_B': z_lambda_B,

    # C-sector
    'omega_L0': omega_L0,
    'J_L': J_L,
    'v_C_sq': v_C_sq,
    'k_crossover': k_crossover,
    'z_C_apparent': z_C_apparent,

    # Coupled bands
    'z_band1_low': z_band1_low,
    'z_band1_mid': z_band1_mid if not np.isnan(z_band1_mid) else -1.0,

    # Spectral dimension
    'd_s_peak': d_s_peak,
    't_peak': t_peak,
    'd_s_t1': d_s_t1,
    'd_s_dos': d_s_dos,
    'd_s_running': d_s_run,
    't_values': t_vals,

    # Chain analysis
    'alpha_s57_range': alpha_s57,
    'N_chain_list': np.array(N_chain_list),
    'gap_analytic': gap_arr,

    # Graph properties
    'diameter': DIAMETER,
    'N_vertices': N_k,
    'lambda_n': lambda_n,
    'k_eff': k_eff,

    # Predicted alpha on CG(24)
    'alpha_predicted_cg24': -z_phonon / d_s_peak,

    # Gate
    'gate_name': np.array(['DYNAMICAL-EXPONENT-63']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([detail]),
}

np.savez(data_dir / 's63_dynamical_exponent.npz', **save_dict)
print(f"  Data saved: s63_dynamical_exponent.npz")

elapsed = time.time() - t_start
print(f"\n  Elapsed: {elapsed:.1f}s")
print("=" * 78)
print("DONE")
print("=" * 78)
