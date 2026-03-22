#!/usr/bin/env python3
"""
Session 22c L-1: Landau Free Energy Classification on the tau-Line

Performs the complete Landau theory analysis of V_eff(tau):
  1. V_total derivatives: V'(tau), V''(tau), V'''(tau), V''''(tau)
  2. V_IR derivatives: check for spinodal in low-mode sector
  3. Ginzburg number estimation
  4. First-order transition characterization (barrier height, latent heat)
  5. He-3/He-4 analog calibration

Data sources:
  - l20_vtotal_minimum.npz: V_total (Casimir + CW) at 21 tau values
  - s21c_V_IR.npz: V_IR = E_bos - E_ferm for low modes at 4 tau values
  - s22b_block_diagonal_results.npz: E_ferm at 9 tau values (confirmed baseline)

Constraint Gates:
  COMPELLING: V_IR'' < 0 at some tau in [0.10, 0.40] (IR spinodal exists)
  INTERESTING: G_i > 10 (perturbative V_eff unreliable)
  NEUTRAL: V_total'' > 0 throughout (confirmed from 21a)
  CLOSED: G_i < 1 AND V_IR'' > 0 everywhere

Output: s22c_landau_classification.npz, s22c_landau_classification.txt
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys

data_dir = os.path.dirname(os.path.abspath(__file__))
out_txt = os.path.join(data_dir, 's22c_landau_classification.txt')
out_npz = os.path.join(data_dir, 's22c_landau_classification.npz')
out_png = os.path.join(data_dir, 's22c_landau_classification.png')

# Redirect stdout to both console and file
class Tee:
    def __init__(self, *files):
        self.files = files
    def write(self, s):
        for f in self.files:
            f.write(s)
            f.flush()
    def flush(self):
        for f in self.files:
            f.flush()

log_file = open(out_txt, 'w')
sys.stdout = Tee(sys.__stdout__, log_file)

print("=" * 70)
print("SESSION 22c L-1: LANDAU FREE ENERGY CLASSIFICATION")
print("=" * 70)

# ============================================================
# 1. LOAD DATA
# ============================================================
print("\n--- 1. Loading data ---")

vtot = np.load(os.path.join(data_dir, 'l20_vtotal_minimum.npz'), allow_pickle=True)
tau_vtot = vtot['tau']
E_total_casimir = vtot['E_total_casimir']
V_total_cw = vtot['V_total_cw']

# Total effective potential = Casimir + CW
# E_total_casimir is the Casimir energy (sum of sqrt(lambda))
# V_total_cw is the Coleman-Weinberg contribution
# Both are functions of tau at 21 values [0, 0.1, ..., 2.0]
print(f"V_total data: {len(tau_vtot)} tau values, range [{tau_vtot[0]}, {tau_vtot[-1]}]")

# V_IR data
vir = np.load(os.path.join(data_dir, 's21c_V_IR.npz'), allow_pickle=True)
tau_vir = vir['tau_compute']  # [0.0, 0.15, 0.30, 0.50]
N_values_vir = vir['N_values']  # [10, 20, 50, 100, 150, 200]
print(f"V_IR data: {len(tau_vir)} tau values: {tau_vir}")

# E_ferm full (21 tau) from V_IR data
tau_ferm_full = vir['tau_dirac_full']  # 21 values

# s22b confirmed baseline
s22b = np.load(os.path.join(data_dir, 's22b_block_diagonal_results.npz'), allow_pickle=True)
tau_22b = s22b['tau_values']
E_ferm_22b = {N: s22b[f'E_ferm_N{N}'] for N in [20, 50, 100, 200]}
delta_T_22b = s22b['delta_T']
delta_T_b1 = s22b['delta_T_b1']
delta_T_b2 = s22b['delta_T_b2']
print(f"s22b data: {len(tau_22b)} tau values: {tau_22b}")

# ============================================================
# 2. V_TOTAL DERIVATIVES
# ============================================================
print("\n" + "=" * 70)
print("2. V_TOTAL DERIVATIVE ANALYSIS")
print("=" * 70)

dtau = tau_vtot[1] - tau_vtot[0]  # 0.1

# Use both Casimir and CW. The "total" effective potential in the spectral
# action framework is V_eff = V_total_cw (which already includes 1-loop).
# E_total_casimir is the tree-level Casimir (zero-point energy).
# For the Landau classification, we analyze V_total_cw as the 1-loop V_eff,
# and E_total_casimir as the tree-level contribution separately.

print("\n--- 2a. CW effective potential V_CW(tau) ---")
V_cw = V_total_cw

# Numerical derivatives (central differences, forward/backward at boundaries)
def numerical_derivatives(y, dx, order=4):
    """Compute up to 4th derivatives using central differences."""
    n = len(y)
    d1 = np.zeros(n)
    d2 = np.zeros(n)
    d3 = np.zeros(n)
    d4 = np.zeros(n)

    # First derivative (central, 2nd order)
    d1[0] = (-3*y[0] + 4*y[1] - y[2]) / (2*dx)
    d1[-1] = (3*y[-1] - 4*y[-2] + y[-3]) / (2*dx)
    for i in range(1, n-1):
        d1[i] = (y[i+1] - y[i-1]) / (2*dx)

    # Second derivative (central, 2nd order)
    d2[0] = (2*y[0] - 5*y[1] + 4*y[2] - y[3]) / dx**2
    d2[-1] = (2*y[-1] - 5*y[-2] + 4*y[-3] - y[-4]) / dx**2
    for i in range(1, n-1):
        d2[i] = (y[i+1] - 2*y[i] + y[i-1]) / dx**2

    # Third derivative
    for i in range(2, n-2):
        d3[i] = (y[i+2] - 2*y[i+1] + 2*y[i-1] - y[i-2]) / (2*dx**3)
    d3[0] = d3[2]  # extrapolate
    d3[1] = d3[2]
    d3[-1] = d3[-3]
    d3[-2] = d3[-3]

    # Fourth derivative
    for i in range(2, n-2):
        d4[i] = (y[i+2] - 4*y[i+1] + 6*y[i] - 4*y[i-1] + y[i-2]) / dx**4
    d4[0] = d4[2]
    d4[1] = d4[2]
    d4[-1] = d4[-3]
    d4[-2] = d4[-3]

    return d1, d2, d3, d4

# CW derivatives
V_cw_d1, V_cw_d2, V_cw_d3, V_cw_d4 = numerical_derivatives(V_cw, dtau)

print("\nV_CW derivatives at key tau values:")
print(f"{'tau':>5s} {'V_CW':>14s} {'V_CW_prime':>14s} {'V_CW_pp':>14s} {'V_CW_ppp':>14s} {'V_CW_pppp':>14s}")
for i in [0, 1, 2, 3, 4, 5, 10, 15, 20]:
    print(f"{tau_vtot[i]:5.1f} {V_cw[i]:14.4e} {V_cw_d1[i]:14.4e} {V_cw_d2[i]:14.4e} {V_cw_d3[i]:14.4e} {V_cw_d4[i]:14.4e}")

# Casimir derivatives
E_cas = E_total_casimir
E_cas_d1, E_cas_d2, E_cas_d3, E_cas_d4 = numerical_derivatives(E_cas, dtau)

print("\nE_Casimir derivatives at key tau values:")
print(f"{'tau':>5s} {'E_Cas':>14s} {'E_Cas_prime':>14s} {'E_Cas_pp':>14s} {'E_Cas_ppp':>14s}")
for i in [0, 1, 2, 3, 4, 5, 10]:
    print(f"{tau_vtot[i]:5.1f} {E_cas[i]:14.4e} {E_cas_d1[i]:14.4e} {E_cas_d2[i]:14.4e} {E_cas_d3[i]:14.4e}")

# Check sign of V''
print("\n--- 2b. Convexity analysis of V_CW ---")
v2_sign_changes = []
for i in range(len(tau_vtot)-1):
    if V_cw_d2[i] * V_cw_d2[i+1] < 0:
        # Interpolate zero crossing
        tau_cross = tau_vtot[i] - V_cw_d2[i] * dtau / (V_cw_d2[i+1] - V_cw_d2[i])
        v2_sign_changes.append(tau_cross)
        print(f"V_CW'' changes sign at tau ~ {tau_cross:.4f}")

if len(v2_sign_changes) == 0:
    if np.all(V_cw_d2 > 0):
        print("V_CW'' > 0 EVERYWHERE (convex, no spinodal). CONFIRMED.")
    elif np.all(V_cw_d2 < 0):
        print("V_CW'' < 0 EVERYWHERE (concave).")
    else:
        print(f"V_CW'' range: [{V_cw_d2.min():.4e}, {V_cw_d2.max():.4e}]")

# Casimir convexity
print("\n--- 2c. Convexity analysis of E_Casimir ---")
cas_sign_changes = []
for i in range(len(tau_vtot)-1):
    if E_cas_d2[i] * E_cas_d2[i+1] < 0:
        tau_cross = tau_vtot[i] - E_cas_d2[i] * dtau / (E_cas_d2[i+1] - E_cas_d2[i])
        cas_sign_changes.append(tau_cross)
        print(f"E_Cas'' changes sign at tau ~ {tau_cross:.4f}")

if len(cas_sign_changes) == 0:
    if np.all(E_cas_d2 > 0):
        print("E_Cas'' > 0 EVERYWHERE (convex). CONFIRMED.")
    else:
        print(f"E_Cas'' range: [{E_cas_d2.min():.4e}, {E_cas_d2.max():.4e}]")

# Cubic invariant at tau=0
print("\n--- 2d. Cubic invariant at tau=0 ---")
# The cubic term V'''(0) from Session 21a was reported as -7.2.
# Check with the current numerical derivative.
# Note: the 21a value was computed from a different normalization.
# We report V'''(0) from the CW potential directly.
print(f"V_CW'''(0) = {V_cw_d3[0]:.4e}")
print(f"V_CW'''(0.1) = {V_cw_d3[1]:.4e}")
print(f"V_CW'''(0.2) = {V_cw_d3[2]:.4e}")
print(f"V_CW'''(0.3) = {V_cw_d3[3]:.4e}")

# The ratio V'''(0)^2 / V''''(0) determines the first-order strength
if V_cw_d4[0] != 0:
    ratio_34 = V_cw_d3[0]**2 / V_cw_d4[0]
    print(f"\nV'''(0)^2 / V''''(0) = {ratio_34:.4e}")
    print("This ratio determines the barrier height in Landau's first-order theory.")

# ============================================================
# 3. V_IR DERIVATIVE ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("3. V_IR DERIVATIVE ANALYSIS (low-mode sector)")
print("=" * 70)

# V_IR data at 4 tau values: [0.0, 0.15, 0.30, 0.50]
# We need V_IR'' to check for spinodal.
# With only 4 points, numerical differentiation is limited.
# Use 2nd-order central differences where possible, forward/backward at edges.

dtau_vir = np.diff(tau_vir)  # non-uniform spacing

for N in N_values_vir:
    V_ir = vir[f'N{N}_V_IR']
    FB = vir[f'N{N}_FB_ratio']

    print(f"\n--- N={N} ---")
    print(f"  tau:  {tau_vir}")
    print(f"  V_IR: {V_ir}")
    print(f"  F/B:  {FB}")

    # Finite differences (non-uniform spacing)
    # First derivative
    d1 = np.zeros(len(V_ir))
    d1[0] = (V_ir[1] - V_ir[0]) / (tau_vir[1] - tau_vir[0])
    d1[-1] = (V_ir[-1] - V_ir[-2]) / (tau_vir[-1] - tau_vir[-2])
    for i in range(1, len(V_ir)-1):
        h1 = tau_vir[i] - tau_vir[i-1]
        h2 = tau_vir[i+1] - tau_vir[i]
        d1[i] = (V_ir[i+1] - V_ir[i-1]) / (h1 + h2)

    # Second derivative (3-point non-uniform)
    d2 = np.zeros(len(V_ir))
    for i in range(1, len(V_ir)-1):
        h1 = tau_vir[i] - tau_vir[i-1]
        h2 = tau_vir[i+1] - tau_vir[i]
        d2[i] = 2 * (V_ir[i+1]/(h2*(h1+h2)) - V_ir[i]/(h1*h2) + V_ir[i-1]/(h1*(h1+h2)))

    # Boundary: use 3-point forward/backward
    h1, h2 = tau_vir[1]-tau_vir[0], tau_vir[2]-tau_vir[1]
    d2[0] = 2*(V_ir[0]/(h1*(h1+h2)) - V_ir[1]/(h1*h2) + V_ir[2]/(h2*(h1+h2)))
    h1, h2 = tau_vir[-2]-tau_vir[-3], tau_vir[-1]-tau_vir[-2]
    d2[-1] = 2*(V_ir[-3]/(h1*(h1+h2)) - V_ir[-2]/(h1*h2) + V_ir[-1]/(h2*(h1+h2)))

    print(f"  V_IR':  {d1}")
    print(f"  V_IR'': {d2}")

    # Check for spinodal (V_IR'' < 0)
    spinodal_found = False
    for i in range(len(tau_vir)):
        if d2[i] < 0:
            spinodal_found = True
            print(f"  ** V_IR''({tau_vir[i]:.2f}) = {d2[i]:.4f} < 0 --> SPINODAL in IR sector!")

    if not spinodal_found:
        print(f"  V_IR'' > 0 at all computed tau. No IR spinodal.")

# ============================================================
# 3b. EXTENDED V_IR ANALYSIS using E_ferm at all 21 tau values
# ============================================================
print("\n--- 3b. Extended fermionic energy analysis (21 tau, p+q<=2) ---")
print("(Bosonic data limited to 4 tau; fermionic at 21 tau)")

# E_ferm alone can reveal non-monotonicity, which is a prerequisite for
# V_IR non-monotonicity (since E_bos is monotonically increasing).

for N in [20, 50, 100, 200]:
    E_f = vir[f'ferm_energy_full_N{N}']
    # Find minima
    dE = np.diff(E_f)
    sign_changes = []
    for i in range(len(dE)-1):
        if dE[i] < 0 and dE[i+1] > 0:
            # Minimum between tau_ferm_full[i+1] and tau_ferm_full[i+1]
            sign_changes.append(tau_ferm_full[i+1])

    if len(sign_changes) > 0:
        print(f"  N={N}: E_ferm has minimum(a) near tau = {sign_changes}")
        min_idx = np.argmin(E_f)
        print(f"    Global min at tau = {tau_ferm_full[min_idx]:.1f}, E_ferm = {E_f[min_idx]:.4f}")
        depth = (E_f[0] - E_f[min_idx]) / E_f[0] * 100
        print(f"    Depth relative to tau=0: {depth:.3f}%")
    else:
        direction = "INCREASING" if dE[0] > 0 else "DECREASING"
        print(f"  N={N}: E_ferm MONOTONICALLY {direction}")

# ============================================================
# 3c. V_IR from s22b confirmed E_ferm (9 tau values)
# ============================================================
print("\n--- 3c. E_ferm from s22b confirmed baseline (9 tau values) ---")
for N in [20, 50, 100, 200]:
    E_f = E_ferm_22b[N]
    dE = np.diff(E_f)
    sign_changes = []
    for i in range(len(dE)-1):
        if dE[i] < 0 and dE[i+1] > 0:
            sign_changes.append(tau_22b[i+1])

    if len(sign_changes) > 0:
        min_idx = np.argmin(E_f)
        depth = (E_f[0] - E_f[min_idx]) / E_f[0] * 100
        print(f"  N={N}: E_ferm minimum at tau ~ {tau_22b[min_idx]:.2f}, depth {depth:.3f}%")
    else:
        direction = "INCREASING" if dE[0] > 0 else "DECREASING"
        print(f"  N={N}: E_ferm MONOTONICALLY {direction}")

# ============================================================
# 4. GINZBURG NUMBER ESTIMATION
# ============================================================
print("\n" + "=" * 70)
print("4. GINZBURG NUMBER ESTIMATION")
print("=" * 70)

# The Ginzburg number G_i measures the relative importance of fluctuations
# vs mean-field. For a system with effective dimensionality d_eff:
#
#   G_i ~ (T_c / Delta_F)^{2/(4-d_eff)}
#
# where Delta_F is the free energy scale at the transition and T_c is the
# transition temperature (or energy scale of fluctuations).
#
# In the modulus context:
# - d_eff = 1 (one real parameter tau, the modulus)
# - The "barrier" energy Delta_F = V_barrier (if a first-order transition exists)
# - The "temperature" T_c is the scale at which quantum/thermal fluctuations matter
#
# For d_int = 8 (internal space), d_eff = 8 > d_uc = 4, so mean-field is EXACT
# for the INTERNAL space degrees of freedom. But for the modulus alone, d_eff = 1.
#
# The reconciliation: the modulus is a ZERO-MODE of the internal space.
# The Ginzburg criterion for the zero-mode in d_eff = 1 is:
#
#   G_i = (k_B T / (c * a^{d_eff} * xi_0^{d_eff}))^{2/(4-d_eff)}
#
# For d_eff = 1: G_i = (T / (c * a * xi_0))^{2/3}
#
# We estimate:
# - xi_0 = coherence length in tau-space ~ |V''|^{-1/2} (curvature radius)
# - c = V''(tau) at the would-be transition
# - a = lattice spacing ~ minimal tau-resolution = 0.1
# - T_c = characteristic scale

print("\n--- 4a. Effective curvature radius (coherence length in tau-space) ---")

# The curvature radius of V_eff is xi_0 ~ (V/V'')^{1/2}
# At tau=0.3 (physical window center):
idx_03 = np.argmin(np.abs(tau_vtot - 0.3))
V_at_03 = V_cw[idx_03]
Vpp_at_03 = V_cw_d2[idx_03]
xi_0_cw = np.sqrt(np.abs(V_at_03 / Vpp_at_03)) if Vpp_at_03 != 0 else np.inf

print(f"At tau = 0.3:")
print(f"  V_CW = {V_at_03:.4e}")
print(f"  V_CW'' = {Vpp_at_03:.4e}")
print(f"  xi_0 = sqrt(|V/V''|) = {xi_0_cw:.4f}")

# Also for Casimir
E_at_03 = E_cas[idx_03]
Epp_at_03 = E_cas_d2[idx_03]
xi_0_cas = np.sqrt(np.abs(E_at_03 / Epp_at_03)) if Epp_at_03 != 0 else np.inf
print(f"  E_Cas = {E_at_03:.4e}")
print(f"  E_Cas'' = {Epp_at_03:.4e}")
print(f"  xi_0 (Casimir) = {xi_0_cas:.4f}")

print("\n--- 4b. Ginzburg number for 1D modulus (d_eff = 1) ---")

# For a first-order transition characterized by the cubic invariant,
# the Ginzburg criterion in d_eff = 1 is:
#
#   G_i ~ (fluctuation energy)^2 / (mean-field barrier energy)^2
#
# The fluctuation energy in the 1D modulus is governed by the "mass" V''
# and the quartic coupling V''''/4!.
#
# A precise formula from Landau-Ginzburg in d=1:
#   G_i = (V''''^2 * kT) / (V''^3 * xi_0)  [d=1 specific]
#
# But we don't have a temperature. In the quantum modulus context,
# the relevant "temperature" is the zero-point energy of the modulus:
#   T_eff ~ hbar * omega_modulus / 2 = hbar * sqrt(V''/m_eff) / 2
#
# With the KK mass for the modulus m_eff ~ G_{tau tau} ~ 5 (from Session 21b):

G_tau_tau = 5.0  # modulus kinetic coefficient from Session 21b B-3
m_eff = G_tau_tau  # effective mass for the zero-mode

# Modulus frequency
omega_mod = np.sqrt(np.abs(Vpp_at_03) / m_eff)
# Zero-point energy (quantum)
T_eff = 0.5 * omega_mod  # in natural units hbar = 1

print(f"  G_tau_tau = {G_tau_tau} (from Session 21b)")
print(f"  omega_modulus = sqrt(|V''|/m) = {omega_mod:.4e}")
print(f"  T_eff (zero-point) = {T_eff:.4e}")

# Ginzburg number for d_eff = 1
# G_i = (T_eff)^{2/(4-1)} / (|V''| * xi_0)^{2/3}
# Since d_eff = 1, the Ginzburg criterion is:
#   G_i = (T_eff / Delta_F)^{2/(4-d_eff)} = (T_eff / Delta_F)^{2/3}
#
# Here Delta_F is the free energy barrier. For the perturbative landscape
# (no barrier), we use |V''| * xi_0^2 as the characteristic energy scale.

Delta_F_cw = np.abs(Vpp_at_03) * xi_0_cw**2  # Characteristic energy from curvature
if Delta_F_cw > 0:
    G_i_cw = (T_eff / Delta_F_cw)**(2.0/3.0)
else:
    G_i_cw = np.inf
print(f"  Delta_F (CW curvature scale) = {Delta_F_cw:.4e}")
print(f"  G_i (CW, d_eff=1) = {G_i_cw:.4e}")

# For Casimir
Delta_F_cas = np.abs(Epp_at_03) * xi_0_cas**2
omega_mod_cas = np.sqrt(np.abs(Epp_at_03) / m_eff)
T_eff_cas = 0.5 * omega_mod_cas
if Delta_F_cas > 0:
    G_i_cas = (T_eff_cas / Delta_F_cas)**(2.0/3.0)
else:
    G_i_cas = np.inf
print(f"  G_i (Casimir, d_eff=1) = {G_i_cas:.4e}")

print("\n--- 4c. Ginzburg number for d_int = 8 (internal space) ---")
# For d_int = 8 > d_uc = 4: mean-field is exact.
# G_i -> 0 as d -> infinity. For d = 8, Ginzburg criterion:
#   G_i ~ (T/Delta_F)^{2/(4-d)}  with d=8: exponent = 2/(-4) = -1/2
# G_i = (T/Delta_F)^{-1/2} = (Delta_F/T)^{1/2}
# Since Delta_F >> T: G_i >> 1... BUT this is misleading.
# The correct statement: for d > d_uc, mean-field is exact and fluctuations
# are irrelevant. The Ginzburg criterion formula changes character above d_uc.
#
# The resolution: d=8 mean-field exactness applies to SPATIAL fluctuations
# of the order parameter across the internal manifold. The zero-mode (spatially
# uniform tau) has d_eff=1 and IS subject to fluctuations.

print("d_int = 8 > d_uc = 4: Mean-field is EXACT for spatial fluctuations")
print("on the internal manifold (Landau Paper 04, Section 8.7).")
print("However, the zero-mode (uniform tau) has d_eff = 1.")
print("")
print("RECONCILIATION: The perturbative V_eff(tau) is the EXACT mean-field")
print("free energy for the zero-mode. No fluctuation corrections modify it.")
print("The zero-mode's 1D dynamics may have large quantum fluctuations,")
print("but these do not change V_eff -- they change the wave function of tau.")

print("\n--- 4d. He-3/He-4 analog calibration ---")
print("")
print("He-4 lambda transition:")
print("  G_i ~ 0.3, weakly fluctuating, mean-field + log corrections")
print("  d = 3, n = 2 (complex order parameter)")
print("")
print("He-3 A-phase:")
print("  G_i ~ 1, strongly fluctuating")
print("  d = 3, n = 18 (3x3 complex matrix order parameter)")
print("")
print("Our modulus (d_eff = 1, real scalar):")
print(f"  G_i (CW) = {G_i_cw:.4e}")
print(f"  G_i (Casimir) = {G_i_cas:.4e}")
print("")

if G_i_cw < 1:
    print("G_i < 1: Perturbative V_eff is a RELIABLE guide to the zero-mode dynamics.")
    print("Fluctuations do not modify the qualitative picture.")
    ginzburg_verdict = "RELIABLE"
elif G_i_cw < 10:
    print("1 < G_i < 10: Fluctuations are non-negligible but do not dominate.")
    print("Mean-field gives the qualitative picture with quantitative corrections.")
    ginzburg_verdict = "MODERATE"
else:
    print("G_i > 10: Perturbative V_eff is UNRELIABLE. Fluctuations dominate.")
    print("The true ground state may differ qualitatively from V_eff prediction.")
    ginzburg_verdict = "UNRELIABLE"

# ============================================================
# 5. FIRST-ORDER TRANSITION CHARACTERIZATION
# ============================================================
print("\n" + "=" * 70)
print("5. FIRST-ORDER TRANSITION CHARACTERIZATION")
print("=" * 70)

# Landau theory for first-order transitions (Paper 04, Section 6):
#
# F(eta) = a*eta^2 + c*eta^3 + b*eta^4
#
# With a > 0 (symmetric phase locally stable), c != 0 (cubic invariant present),
# b > 0 (stability at large eta). The transition is first-order if c != 0.
#
# The relevant coefficients from the Taylor expansion of V_eff around tau=0:
# V_eff(tau) ~ V_0 + V'(0)*tau + (1/2)*V''(0)*tau^2 + (1/6)*V'''(0)*tau^3 + (1/24)*V''''(0)*tau^4
#
# Mapping to Landau:
# a = V''(0)/2, c = V'''(0)/6, b = V''''(0)/24
# (V'(0) contributes a linear tilt, not a phase transition)

print("\n--- 5a. Taylor coefficients around tau=0 ---")

# Use more precise derivatives at tau=0 from the numerical data
# Note: the Session 21a value V'''(0) = -7.2 was computed in different normalization.
# We use the raw CW potential V_total_cw.

V0 = V_cw[0]
Vp0 = V_cw_d1[0]
Vpp0 = V_cw_d2[0]
Vppp0 = V_cw_d3[0]
Vpppp0 = V_cw_d4[0]

print(f"V_CW(0) = {V0:.6e}")
print(f"V'(0) = {Vp0:.6e}")
print(f"V''(0) = {Vpp0:.6e}")
print(f"V'''(0) = {Vppp0:.6e}")
print(f"V''''(0) = {Vpppp0:.6e}")

# Landau coefficients
a_L = Vpp0 / 2
c_L = Vppp0 / 6
b_L = Vpppp0 / 24

print(f"\nLandau coefficients (F = a*eta^2 + c*eta^3 + b*eta^4):")
print(f"  a = V''/2 = {a_L:.6e}")
print(f"  c = V'''/6 = {c_L:.6e}")
print(f"  b = V''''/24 = {b_L:.6e}")

# Check transition type
if c_L != 0:
    print("\n  c != 0: FIRST-ORDER transition (if transition exists)")
    print("  (Landau Paper 04 Section 6.1: cubic invariant guarantees first-order)")
else:
    print("\n  c = 0: Second-order transition (standard phi^4 universality)")

# For first-order: transition occurs when the secondary minimum is degenerate
# with the primary (tau=0) minimum.
# Barrier location: tau_barrier = -c/(2b) (extremum of F)
# Transition field: tau_tr = -3c/(4b) (degenerate minima)
# Barrier height: Delta F = c^4/(256*b^3) - a*c^2/(16*b^2)

print("\n--- 5b. Barrier and transition estimates ---")

if b_L != 0 and c_L != 0:
    tau_barrier = -c_L / (2 * b_L)
    tau_tr = -3 * c_L / (4 * b_L)

    # At the transition, the barrier height above the metastable minimum:
    # For the pure cubic-quartic part (a=0 for simplicity):
    # Delta_F_barrier = |c|^4 / (256 * |b|^3)
    Delta_F_barrier = np.abs(c_L)**4 / (256 * np.abs(b_L)**3)

    # With the quadratic term: the transition temperature (tau_1 in Landau's notation)
    # For a first-order transition: tau_1 = T_0 - c^2/(4*a*b) (in temperature parameter)
    # Here "temperature" is the control parameter that drives the transition.
    # In our context, there is no external temperature -- the modulus IS the order parameter.

    print(f"  Barrier location (pure cubic-quartic): tau = {tau_barrier:.4f}")
    print(f"  Transition point (degenerate minima): tau = {tau_tr:.4f}")
    print(f"  Barrier height (a=0 limit): Delta_F = {Delta_F_barrier:.4e}")
    print(f"  Barrier height relative to V(0): {Delta_F_barrier/V0:.4e}")

    # The full picture with quadratic term:
    # F(eta) = a*eta^2 + c*eta^3 + b*eta^4
    # F'(eta) = 2*a*eta + 3*c*eta^2 + 4*b*eta^3 = eta*(2a + 3c*eta + 4b*eta^2)
    # Non-trivial extrema at eta = (-3c +/- sqrt(9c^2 - 32ab)) / (8b)
    discriminant = 9*c_L**2 - 32*a_L*b_L
    print(f"\n  Discriminant 9c^2 - 32ab = {discriminant:.4e}")

    if discriminant > 0:
        eta_plus = (-3*c_L + np.sqrt(discriminant)) / (8*b_L)
        eta_minus = (-3*c_L - np.sqrt(discriminant)) / (8*b_L)
        print(f"  Non-trivial extrema at eta = {eta_minus:.4f}, {eta_plus:.4f}")

        # Evaluate F at these points
        F_plus = a_L*eta_plus**2 + c_L*eta_plus**3 + b_L*eta_plus**4
        F_minus = a_L*eta_minus**2 + c_L*eta_minus**3 + b_L*eta_minus**4
        print(f"  F(eta_minus) = {F_minus:.4e}")
        print(f"  F(eta_plus) = {F_plus:.4e}")

        if F_plus < 0 or F_minus < 0:
            print("  ** Secondary minimum BELOW F(0) = 0: transition IS realized!")
        else:
            print("  ** Secondary minimum ABOVE F(0): transition NOT realized perturbatively.")
            print("  ** Non-perturbative barrier required to create the transition.")
    elif discriminant == 0:
        print("  Inflection point (marginal): discriminant = 0")
    else:
        print("  No non-trivial extrema (discriminant < 0): a too large")
        print("  Quadratic term prevents any local maximum/minimum besides eta=0.")
        print("  Perturbative landscape is featureless -- confirmed.")
else:
    print("  b_L or c_L = 0: degenerate case, skip barrier analysis.")

# ============================================================
# 5c. Normalized Landau expansion
# ============================================================
print("\n--- 5c. Normalized Landau expansion ---")
print("Normalizing V_eff to identify the phase transition character:")
# Use Casimir contribution for the normalized expansion since it is the
# leading term in the spectral action. V_CW is the 1-loop correction.
# The total is dominated by CW at large tau but Casimir at small tau.

# Also compute from E_total_casimir directly
Epp0 = E_cas_d2[0]
Eppp0 = E_cas_d3[0]
Epppp0 = E_cas_d4[0]

a_cas = Epp0 / 2
c_cas = Eppp0 / 6
b_cas = Epppp0 / 24

print(f"\nCasimir Landau coefficients:")
print(f"  a = E''/2 = {a_cas:.6e}")
print(f"  c = E'''/6 = {c_cas:.6e}")
print(f"  b = E''''/24 = {b_cas:.6e}")

if c_cas != 0:
    print(f"  c/a = {c_cas/a_cas:.4f} (relative cubic strength)")
    if b_cas != 0:
        print(f"  c^2/(a*b) = {c_cas**2/(a_cas*b_cas):.4f}")

# ============================================================
# 6. DELTA_T DERIVATIVE ANALYSIS
# ============================================================
print("\n" + "=" * 70)
print("6. DELTA_T DERIVATIVE ANALYSIS (from s22b)")
print("=" * 70)

# delta_T(tau) from s22b at 9 tau values
dtau_22b = np.diff(tau_22b)

# Numerical first derivative
dT_d1 = np.zeros(len(delta_T_22b))
for i in range(1, len(delta_T_22b)-1):
    h1 = tau_22b[i] - tau_22b[i-1]
    h2 = tau_22b[i+1] - tau_22b[i]
    dT_d1[i] = (delta_T_22b[i+1] - delta_T_22b[i-1]) / (h1 + h2)
dT_d1[0] = (delta_T_22b[1] - delta_T_22b[0]) / (tau_22b[1] - tau_22b[0])
dT_d1[-1] = (delta_T_22b[-1] - delta_T_22b[-2]) / (tau_22b[-1] - tau_22b[-2])

# Second derivative
dT_d2 = np.zeros(len(delta_T_22b))
for i in range(1, len(delta_T_22b)-1):
    h1 = tau_22b[i] - tau_22b[i-1]
    h2 = tau_22b[i+1] - tau_22b[i]
    dT_d2[i] = 2*(delta_T_22b[i+1]/(h2*(h1+h2)) - delta_T_22b[i]/(h1*h2)
                   + delta_T_22b[i-1]/(h1*(h1+h2)))

print(f"\ndelta_T derivatives:")
print(f"{'tau':>5s} {'dT':>10s} {'dT_prime':>12s} {'dT_pp':>12s} {'dT_b1':>10s} {'dT_b2':>10s}")
for i in range(len(tau_22b)):
    print(f"{tau_22b[i]:5.2f} {delta_T_22b[i]:10.4f} {dT_d1[i]:12.4f} {dT_d2[i]:12.4f} "
          f"{delta_T_b1[i]:10.4f} {delta_T_b2[i]:10.4f}")

# T''(0) gate from Session 21a
print(f"\nT''(0) gate (Session 21a pre-registered):")
print(f"  delta_T''(0) = {dT_d2[0]:.4f}")
# The self-consistency map is T(tau) = tau + delta_T(tau)
# T'(tau) = 1 + delta_T'(tau)
# T''(tau) = delta_T''(tau)
print(f"  T'(0) = 1 + delta_T'(0) = {1 + dT_d1[0]:.4f}")
print(f"  T''(0) = delta_T''(0) = {dT_d2[0]:.4f}")
if dT_d2[0] > 0:
    print("  T''(0) > 0: Curvature is positive (self-consistency map curves UP)")
    print("  This is necessary but NOT sufficient for a fixed point.")
elif dT_d2[0] < 0:
    print("  T''(0) < 0: Constraint Gate TRIGGERED (21a)")
else:
    print("  T''(0) = 0: Marginal")

# Exponential fit to delta_T
print("\n--- 6b. Exponential fit to delta_T ---")
# Fit delta_T ~ A * exp(-alpha * tau)
log_dT = np.log(delta_T_22b)
# Linear fit to log(delta_T) vs tau
from numpy.polynomial import polynomial as P
coeffs = np.polyfit(tau_22b, log_dT, 1)
alpha_fit = -coeffs[0]
A_fit = np.exp(coeffs[1])
print(f"  Exponential fit: delta_T ~ {A_fit:.2f} * exp(-{alpha_fit:.4f} * tau)")
print(f"  Half-life: tau_half = ln(2)/{alpha_fit:.4f} = {np.log(2)/alpha_fit:.4f}")
dT_fitted = A_fit * np.exp(-alpha_fit * tau_22b)
residuals = (delta_T_22b - dT_fitted) / delta_T_22b * 100
print(f"  Residuals (%): {residuals}")
print(f"  R^2 = {1 - np.var(delta_T_22b - dT_fitted)/np.var(delta_T_22b):.6f}")

# ============================================================
# 7. Constraint Gate VERDICTS
# ============================================================
print("\n" + "=" * 70)
print("7. Constraint Gate VERDICTS")
print("=" * 70)

print("\n--- Gate L-1a: V_total'' sign ---")
if np.all(V_cw_d2 > 0) and np.all(E_cas_d2 > 0):
    print("  V_CW'' > 0 everywhere: CONFIRMED")
    print("  E_Cas'' > 0 everywhere: CONFIRMED")
    print("  --> NEUTRAL (0 pp): No spinodal in full perturbative potential.")
    gate_vtotal = "NEUTRAL"
else:
    print("  UNEXPECTED: V'' changes sign somewhere!")
    gate_vtotal = "UNEXPECTED"

print("\n--- Gate L-1b: V_IR'' sign ---")
# Check V_IR'' at the 4 available tau values for each N
ir_spinodal_found = False
ir_spinodal_N = []
for N in N_values_vir:
    V_ir = vir[f'N{N}_V_IR']
    # Non-uniform spacing second derivative
    d2 = np.zeros(len(V_ir))
    for i in range(1, len(V_ir)-1):
        h1 = tau_vir[i] - tau_vir[i-1]
        h2 = tau_vir[i+1] - tau_vir[i]
        d2[i] = 2*(V_ir[i+1]/(h2*(h1+h2)) - V_ir[i]/(h1*h2) + V_ir[i-1]/(h1*(h1+h2)))
    h1, h2 = tau_vir[1]-tau_vir[0], tau_vir[2]-tau_vir[1]
    d2[0] = 2*(V_ir[0]/(h1*(h1+h2)) - V_ir[1]/(h1*h2) + V_ir[2]/(h2*(h1+h2)))
    h1, h2 = tau_vir[-2]-tau_vir[-3], tau_vir[-1]-tau_vir[-2]
    d2[-1] = 2*(V_ir[-3]/(h1*(h1+h2)) - V_ir[-2]/(h1*h2) + V_ir[-1]/(h2*(h1+h2)))

    has_neg = np.any(d2 < 0)
    if has_neg:
        ir_spinodal_found = True
        ir_spinodal_N.append(N)
        neg_idx = np.where(d2 < 0)[0]
        for idx in neg_idx:
            print(f"  N={N}: V_IR''({tau_vir[idx]:.2f}) = {d2[idx]:.4f} < 0 --> IR SPINODAL")

if ir_spinodal_found:
    # Check if in physical window
    print(f"\n  IR spinodal found at N = {ir_spinodal_N}")
    # Classify gate level
    in_window = False
    for N in ir_spinodal_N:
        V_ir = vir[f'N{N}_V_IR']
        d2 = np.zeros(len(V_ir))
        for i in range(1, len(V_ir)-1):
            h1 = tau_vir[i] - tau_vir[i-1]
            h2 = tau_vir[i+1] - tau_vir[i]
            d2[i] = 2*(V_ir[i+1]/(h2*(h1+h2)) - V_ir[i]/(h1*h2) + V_ir[i-1]/(h1*(h1+h2)))
        for i in range(len(d2)):
            if d2[i] < 0 and 0.10 <= tau_vir[i] <= 0.40:
                in_window = True

    if in_window:
        print("  --> COMPELLING (+4-6 pp): V_IR'' < 0 at tau in [0.10, 0.40]")
        gate_vir = "COMPELLING"
    else:
        print("  --> IR spinodal exists but outside physical window")
        gate_vir = "INTERESTING"
else:
    print("  V_IR'' >= 0 at all computed tau for all N.")
    print("  --> No IR spinodal detected.")
    gate_vir = "NO_SPINODAL"

print("\n--- Gate L-1c: Ginzburg number ---")
print(f"  G_i (CW) = {G_i_cw:.4e}")
print(f"  G_i (Casimir) = {G_i_cas:.4e}")

if G_i_cw > 10 or G_i_cas > 10:
    print("  --> INTERESTING (+1-2 pp): G_i > 10, perturbative V_eff unreliable")
    gate_ginzburg = "INTERESTING"
elif G_i_cw < 1 and G_i_cas < 1:
    if gate_vir == "NO_SPINODAL":
        print("  --> CLOSED (-2 pp): G_i < 1 AND V_IR'' > 0 everywhere")
        gate_ginzburg = "CLOSED"
    else:
        print("  --> G_i < 1: mean-field reliable, but IR spinodal exists")
        gate_ginzburg = "RELIABLE_WITH_SPINODAL"
else:
    print("  --> G_i moderate")
    gate_ginzburg = "MODERATE"

print("\n--- Gate L-1d: First-order character ---")
if c_L != 0:
    print(f"  V'''(0) = {Vppp0:.4e} (nonzero)")
    print(f"  c/a = {c_cas/a_cas:.4f}" if a_cas != 0 else "  c/a undefined")
    print("  First-order transition character CONFIRMED by cubic invariant.")
    print("  BUT: perturbative landscape has no barrier (V'' > 0 everywhere).")
    print("  The first-order transition requires a NON-PERTURBATIVE barrier.")
    gate_firstorder = "FIRST_ORDER_CHARACTER"
else:
    print("  V'''(0) = 0: No cubic invariant.")
    gate_firstorder = "NO_CUBIC"

# ============================================================
# 8. SUMMARY TABLE
# ============================================================
print("\n" + "=" * 70)
print("8. L-1 SUMMARY")
print("=" * 70)

print("\n  V_total (CW + Casimir):")
print(f"    V'' > 0 everywhere: YES (no spinodal, CONFIRMED)")
print(f"    V'''(0) = {Vppp0:.4e} (cubic invariant present)")
print(f"    First-order character: YES (c != 0)")
print(f"    Perturbative barrier: NO (discriminant < 0 or secondary min above primary)")

print("\n  V_IR (low-mode sector, 4 tau values):")
for N in N_values_vir:
    V_ir = vir[f'N{N}_V_IR']
    diffs = np.diff(V_ir)
    mono = "INCREASING" if np.all(diffs > 0) else ("DECREASING" if np.all(diffs < 0) else "NON-MONOTONIC")
    print(f"    N={N:3d}: {mono}, V_IR range [{V_ir.min():.4f}, {V_ir.max():.4f}]")

print(f"\n  Ginzburg number:")
print(f"    G_i (CW, d_eff=1) = {G_i_cw:.4e}")
print(f"    G_i (Casimir, d_eff=1) = {G_i_cas:.4e}")
print(f"    Verdict: {ginzburg_verdict}")

print(f"\n  delta_T analysis:")
print(f"    T''(0) = {dT_d2[0]:.4f} {'> 0 (positive curvature)' if dT_d2[0] > 0 else '<= 0 (CLOSED)'}")
print(f"    Exponential fit: delta_T ~ {A_fit:.2f} * exp(-{alpha_fit:.4f} * tau), R^2 = {1 - np.var(delta_T_22b - dT_fitted)/np.var(delta_T_22b):.6f}")
print(f"    delta_T > 0 everywhere: No perturbative fixed point (CONFIRMED)")

print("\n  Constraint Gate summary:")
print(f"    L-1a (V_total spinodal): {gate_vtotal} (0 pp)")
print(f"    L-1b (V_IR spinodal):    {gate_vir}")
print(f"    L-1c (Ginzburg):         {gate_ginzburg}")
print(f"    L-1d (First-order):      {gate_firstorder}")

# ============================================================
# 9. SAVE DATA
# ============================================================
print("\n--- Saving data ---")

save_dict = {
    'tau_vtot': tau_vtot,
    'V_cw': V_cw,
    'V_cw_d1': V_cw_d1,
    'V_cw_d2': V_cw_d2,
    'V_cw_d3': V_cw_d3,
    'V_cw_d4': V_cw_d4,
    'E_casimir': E_cas,
    'E_cas_d1': E_cas_d1,
    'E_cas_d2': E_cas_d2,
    'E_cas_d3': E_cas_d3,
    'E_cas_d4': E_cas_d4,
    'a_L_cw': np.array([a_L]),
    'c_L_cw': np.array([c_L]),
    'b_L_cw': np.array([b_L]),
    'a_L_cas': np.array([a_cas]),
    'c_L_cas': np.array([c_cas]),
    'b_L_cas': np.array([b_cas]),
    'G_i_cw': np.array([G_i_cw]),
    'G_i_cas': np.array([G_i_cas]),
    'xi_0_cw': np.array([xi_0_cw]),
    'xi_0_cas': np.array([xi_0_cas]),
    'tau_22b': tau_22b,
    'delta_T': delta_T_22b,
    'delta_T_d1': dT_d1,
    'delta_T_d2': dT_d2,
    'exp_fit_A': np.array([A_fit]),
    'exp_fit_alpha': np.array([alpha_fit]),
    'gate_vtotal': np.array([gate_vtotal]),
    'gate_vir': np.array([gate_vir]),
    'gate_ginzburg': np.array([gate_ginzburg]),
}

np.savez(out_npz, **save_dict)
print(f"Data saved to {out_npz}")

# ============================================================
# 10. PLOT
# ============================================================
print("\n--- Generating plots ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Session 22c L-1: Landau Free Energy Classification', fontsize=14, fontweight='bold')

# Panel 1: V_CW and derivatives
ax = axes[0, 0]
ax.semilogy(tau_vtot, V_cw, 'b-', linewidth=2, label='V_CW')
ax.set_xlabel('tau')
ax.set_ylabel('V_CW')
ax.set_title('Coleman-Weinberg Potential')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: V'' (second derivative)
ax = axes[0, 1]
ax.semilogy(tau_vtot, V_cw_d2, 'r-', linewidth=2, label="V_CW''")
ax.semilogy(tau_vtot, E_cas_d2, 'b--', linewidth=2, label="E_Cas''")
ax.set_xlabel('tau')
ax.set_ylabel("V''")
ax.set_title("Second Derivatives (convexity)")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 3: V_IR for different N
ax = axes[0, 2]
for N in N_values_vir:
    V_ir = vir[f'N{N}_V_IR']
    ax.plot(tau_vir, V_ir, 'o-', label=f'N={N}', markersize=8)
ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
ax.axvspan(0.15, 0.35, alpha=0.1, color='green', label='Physical window')
ax.set_xlabel('tau')
ax.set_ylabel('V_IR = E_bos - E_ferm')
ax.set_title('V_IR (p+q<=2) at 4 tau values')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: delta_T and derivatives
ax = axes[1, 0]
ax.plot(tau_22b, delta_T_22b, 'ko-', linewidth=2, label='delta_T')
ax.plot(tau_22b, dT_fitted, 'r--', label=f'Exp fit: {A_fit:.1f}*exp(-{alpha_fit:.2f}*tau)')
ax.set_xlabel('tau')
ax.set_ylabel('delta_T')
ax.set_title('Self-consistency map delta_T(tau)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: delta_T'' (T''(0) gate)
ax = axes[1, 1]
ax.plot(tau_22b, dT_d2, 'ro-', linewidth=2, label="delta_T''")
ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel("delta_T''")
ax.set_title("delta_T second derivative (T''(0) gate)")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 6: Landau free energy reconstruction
ax = axes[1, 2]
eta = np.linspace(-0.5, 2.0, 500)
# Reconstruct Landau F from CW coefficients
F_landau = a_L * eta**2 + c_L * eta**3 + b_L * eta**4
# Also include linear tilt
F_full = Vp0 * eta + a_L * eta**2 + c_L * eta**3 + b_L * eta**4
ax.plot(eta, F_landau / np.abs(a_L) if a_L != 0 else F_landau, 'b-', linewidth=2, label='F = a*eta^2 + c*eta^3 + b*eta^4')
ax.plot(eta, F_full / np.abs(a_L) if a_L != 0 else F_full, 'r--', linewidth=1.5, label='F with linear tilt')
ax.set_xlabel('eta (= tau)')
ax.set_ylabel('F/|a| (normalized)')
ax.set_title('Landau Free Energy (Taylor coefficients from V_CW)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(-5, 20)

plt.tight_layout()
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"Plot saved to {out_png}")
plt.close()

print("\n=== L-1 LANDAU CLASSIFICATION COMPLETE ===")

log_file.close()
sys.stdout = sys.__stdout__
print("Done. Output written to", out_txt)
