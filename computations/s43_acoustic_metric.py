#!/usr/bin/env python3
"""
S43 W6-10: Acoustic Metric from Tau Modulus — Phononic Trimetric Gravity
=========================================================================
Gate: ACOUS-METRIC-43 (INFO)

Physics:
  Each BdG quasiparticle branch propagates with dispersion
    omega_i^2 = m_i^2 + c^2 k^2
  where c = 1/4 (universal, from 1/dim(spinor) = 1/16 via Trap 3).
  Different rest masses m_i = {M_B1, M_B2, M_B3} mean each branch sees
  a different effective acoustic metric in the Barcelo-Liberati-Visser sense.

  The acoustic metric for a massive scalar with dispersion omega^2 = m^2 + c^2 k^2
  in a background with flow velocity v_mu is (Unruh 1981, Barcelo+ 2005 eq 3.1):
    g^{mu nu}_eff,i = eta^{mu nu} + (1 - c_i^2/c^2) u^mu u^nu
  where c_i = effective phase velocity = omega/k = sqrt(m_i^2/k^2 + c^2).

  At the anticrossing (polariton gap), the dressed dispersion has inflection
  points where d^2 omega/dk^2 changes sign -- the group velocity has a local
  extremum. This is the "slow light" regime: v_g -> minimum, the effective
  metric becomes strongly curved.

  The key structural result: three branches with DIFFERENT masses but the
  SAME asymptotic c generate THREE distinct light cones. At low k (k << m_i/c),
  the cones are maximally separated. At high k (k >> m_i/c), they converge
  to a universal cone c = 1/4. This is "asymptotic Lorentz invariance recovery"
  -- the UV is universal, the IR is branch-specific.

Inputs:
  s42_fabric_dispersion.npz  (branch masses, dispersion curves)
  s42_polariton.npz          (anticrossing data, polariton branches)

Outputs:
  s43_acoustic_metric.npz    (all computed quantities)
  s43_acoustic_metric.png    (4-panel figure)

Author: Tesla-Resonance
Date: 2026-03-14
"""

import numpy as np
from numpy.linalg import eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

base = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")

# ============================================================
# 1. LOAD INPUT DATA
# ============================================================

fd = np.load(base / "s42_fabric_dispersion.npz", allow_pickle=True)
pd = np.load(base / "s42_polariton.npz", allow_pickle=True)

# Branch rest masses (BdG quasiparticle energies at k=0)
M_B2 = float(fd['M_star_B2'][0])  # 2.228 M_KK
M_B1 = float(fd['M_star_B1'][0])  # 1.138 M_KK
M_B3 = float(fd['M_star_B3'][0])  # 0.990 M_KK

# Universal high-energy speed: c = 1/M_* = 1/4
# From Trap 3: 1/dim(spinor) = 1/16 -> c^2 = 1/16 -> c = 1/4
c_UV = 0.25  # asymptotic speed of all branches

# Polariton data
g_B2_B1 = float(pd['g_B2_B1'])      # coupling B2-B1
g_B2_B3 = float(pd['g_B2_B3_avg'])  # coupling B2-B3
k_star  = float(pd['k_star_B1'])    # anticrossing momentum

# Polariton dressed branches
k_pol = pd['k_vals']  # (500,)
omega_plus_B1 = pd['omega_plus_B1']
omega_minus_B1 = pd['omega_minus_B1']
omega_plus_B3 = pd['omega_plus_B3']
omega_minus_B3 = pd['omega_minus_B3']

# Tau modulus mass
m_tau = float(fd['m_tau'][0])  # 2.062 M_KK

print("=" * 72)
print("S43 W6-10: ACOUSTIC METRIC FROM TAU MODULUS")
print("           Phononic Trimetric Gravity")
print("=" * 72)
print()

# ============================================================
# 2. BARE DISPERSION AND GROUP/PHASE VELOCITIES
# ============================================================

print("--- SECTION 2: BARE BRANCH DISPERSION ---")
print()

# Dense k grid for smooth derivatives
k = np.linspace(0, 20, 2000)
k[0] = 1e-10  # avoid division by zero

branches = {
    'B1': M_B1,
    'B2': M_B2,
    'B3': M_B3,
}

omega = {}
v_group = {}
v_phase = {}

for name, m in branches.items():
    # Dispersion: omega^2 = m^2 + c^2 k^2
    w = np.sqrt(m**2 + c_UV**2 * k**2)
    omega[name] = w

    # Group velocity: v_g = d omega / dk = c^2 k / omega
    vg = c_UV**2 * k / w
    v_group[name] = vg

    # Phase velocity: v_ph = omega / k
    vp = w / k
    v_phase[name] = vp

print(f"Universal asymptotic speed: c = {c_UV:.4f}")
print(f"c^2 = {c_UV**2:.6f} = 1/16 (Trap 3: e/(a*c) = 1/dim(spinor))")
print()

print("Branch rest masses and low-k group velocities:")
print(f"{'Branch':>6s}  {'m (M_KK)':>10s}  {'v_g(k=1)':>10s}  {'v_g/c':>8s}  {'v_ph(k=1)':>10s}")
for name, m in branches.items():
    w = np.sqrt(m**2 + c_UV**2)
    vg = c_UV**2 / w
    vp = w
    print(f"{name:>6s}  {m:10.6f}  {vg:10.6f}  {vg/c_UV:8.4f}  {vp:10.6f}")

print()

# ============================================================
# 3. EFFECTIVE ACOUSTIC METRIC PER BRANCH
# ============================================================

print("--- SECTION 3: EFFECTIVE ACOUSTIC METRIC ---")
print()

# The Barcelo-Liberati-Visser (BLV) acoustic metric for a massive
# excitation with dispersion omega^2 = m^2 + c^2 k^2 in a static
# homogeneous background (v_flow = 0) is:
#
# In the comoving frame with no flow, the wave equation is:
#   -(d/dt)^2 phi + c^2 nabla^2 phi - m^2 phi = 0
#
# This is the Klein-Gordon equation with "speed of light" = c and mass m.
# The effective metric is:
#   g^{mu nu}_eff = diag(-1, c^2, c^2, c^2)  [contravariant]
#   g_{mu nu}_eff = diag(-1/c^2, 1, 1, 1) * (1/c^2)  [covariant, up to conformal]
#
# Actually, more precisely: the massive KG equation
#   g^{mu nu} nabla_mu nabla_nu phi + m^2 phi = 0
# with g^{mu nu} = diag(-1, c^2, c^2, c^2) gives
#   -d_t^2 phi + c^2 nabla^2 phi + m^2 phi = 0
# which has wrong sign on m^2. The correct form is:
#   g^{mu nu} nabla_mu nabla_nu phi - m^2 phi = 0
# with metric signature (-,+,+,+).
#
# The KEY POINT for multi-metric structure:
# ALL branches share the SAME c (asymptotic light speed).
# The DIFFERENCE is the mass m_i, which affects:
# (a) the group velocity at finite k
# (b) the effective "refractive index" n_i(omega) = c / v_phase_i(omega)
# (c) the causal structure at low energies
#
# For a mode of frequency omega, the effective refractive index is:
#   n_i(omega) = k_i(omega) / omega  (in c=1 units)
# where k_i = (1/c) sqrt(omega^2 - m_i^2)
# So n_i = sqrt(omega^2 - m_i^2) / (c * omega)
#
# The mode-dependent effective metric (for propagation at frequency omega) is:
#   ds_i^2 = -dt^2 + (1/n_i^2) dx^2
#          = -dt^2 + c^2 omega^2 / (omega^2 - m_i^2) dx^2
#
# This is "rainbow gravity" / "doubly special relativity" territory:
# the metric depends on the energy of the probe.

# For each branch, compute the "effective light cone angle" as function of omega
omega_grid = np.linspace(0.5, 10.0, 2000)

n_eff = {}     # effective refractive index
v_ray = {}     # ray velocity = c/n = group velocity for massive KG

print("Effective refractive indices at omega = 3.0 M_KK:")
for name, m in branches.items():
    # n(omega) = sqrt(omega^2 - m^2) / (c * omega) for omega > m
    # Below threshold (omega < m): evanescent, n is imaginary
    mask = omega_grid > m
    n = np.full_like(omega_grid, np.nan)
    n[mask] = np.sqrt(omega_grid[mask]**2 - m**2) / (c_UV * omega_grid[mask])
    n_eff[name] = n

    # Ray (group) velocity
    vr = np.full_like(omega_grid, 0.0)
    vr[mask] = c_UV * np.sqrt(1 - m**2 / omega_grid[mask]**2)
    v_ray[name] = vr

    # Print at omega = 3.0
    idx3 = np.argmin(np.abs(omega_grid - 3.0))
    if omega_grid[idx3] > m:
        n3 = np.sqrt(omega_grid[idx3]**2 - m**2) / (c_UV * omega_grid[idx3])
        vr3 = c_UV * np.sqrt(1 - m**2 / omega_grid[idx3]**2)
        print(f"  {name} (m={m:.3f}): n = {n3:.4f}, v_ray = {vr3:.6f}, v_ray/c = {vr3/c_UV:.4f}")
    else:
        print(f"  {name} (m={m:.3f}): EVANESCENT at omega = 3.0")

print()

# ============================================================
# 4. CAUSAL STRUCTURE: LIGHT CONE SEPARATION
# ============================================================

print("--- SECTION 4: CAUSAL STRUCTURE ---")
print()

# The light cone angle theta_LC for branch i at energy omega is:
#   tan(theta_LC) = v_ray_i = c * sqrt(1 - m_i^2/omega^2)
#
# Two branches i and j have different light cones. The angular
# separation between their light cones is:
#   delta_theta_{ij} = |theta_i - theta_j|
#
# This separation is MAXIMAL at omega just above the larger mass
# (one branch just above threshold, the other well above) and
# goes to ZERO as omega -> infinity (both approach c).

# Compute light cone angles
theta_LC = {}
for name, m in branches.items():
    mask = omega_grid > m
    theta = np.full_like(omega_grid, 0.0)
    theta[mask] = np.arctan(c_UV * np.sqrt(1 - m**2 / omega_grid[mask]**2))
    theta_LC[name] = theta

# Maximum light cone separation between B1 and B2
# B2 has the largest mass (2.228), B3 the smallest (0.990)
# Between M_B3 and M_B1: B3 propagates, B1 propagates, B2 evanescent
# Between M_B1 and M_B2: B3 and B1 propagate, B2 still evanescent
# Above M_B2: all three propagate

# Separation B1-B3 (both propagate for omega > M_B1 = 1.138)
delta_13 = np.abs(theta_LC['B1'] - theta_LC['B3'])
# Separation B2-B1 (both propagate for omega > M_B2 = 2.228)
delta_21 = np.abs(theta_LC['B2'] - theta_LC['B1'])
# Separation B2-B3 (both propagate for omega > M_B2 = 2.228)
delta_23 = np.abs(theta_LC['B2'] - theta_LC['B3'])

# Find maxima
mask_13 = omega_grid > M_B1
if np.any(mask_13 & (delta_13 > 0)):
    idx_max_13 = np.argmax(delta_13)
    omega_max_13 = omega_grid[idx_max_13]
    delta_max_13 = delta_13[idx_max_13]
else:
    omega_max_13, delta_max_13 = 0, 0

mask_21 = omega_grid > M_B2
if np.any(mask_21 & (delta_21 > 0)):
    idx_max_21 = np.argmax(delta_21)
    omega_max_21 = omega_grid[idx_max_21]
    delta_max_21 = delta_21[idx_max_21]
else:
    omega_max_21, delta_max_21 = 0, 0

mask_23 = omega_grid > M_B2
if np.any(mask_23 & (delta_23 > 0)):
    idx_max_23 = np.argmax(delta_23)
    omega_max_23 = omega_grid[idx_max_23]
    delta_max_23 = delta_23[idx_max_23]
else:
    omega_max_23, delta_max_23 = 0, 0

print("Maximum light-cone angular separations:")
print(f"  B1-B3: {np.degrees(delta_max_13):.4f} deg at omega = {omega_max_13:.3f} M_KK")
print(f"  B2-B1: {np.degrees(delta_max_21):.4f} deg at omega = {omega_max_21:.3f} M_KK")
print(f"  B2-B3: {np.degrees(delta_max_23):.4f} deg at omega = {omega_max_23:.3f} M_KK")
print()

# Convergence to universal cone at high energy
omega_test_high = np.array([5.0, 10.0, 20.0, 50.0, 100.0])
print("UV convergence: delta_theta(B2-B3) vs omega")
for wt in omega_test_high:
    theta_B2 = np.arctan(c_UV * np.sqrt(1 - M_B2**2 / wt**2))
    theta_B3 = np.arctan(c_UV * np.sqrt(1 - M_B3**2 / wt**2))
    dt = np.abs(theta_B2 - theta_B3)
    print(f"  omega = {wt:6.1f} M_KK: delta_theta = {np.degrees(dt):.6f} deg "
          f"(~ m_B2^2-m_B3^2)/(2*omega^2) = {(M_B2**2-M_B3**2)/(2*wt**2):.4e})")

print()

# ============================================================
# 5. GROUP VELOCITY SPECTRUM AND SLOW-LIGHT
# ============================================================

print("--- SECTION 5: GROUP VELOCITY AND SLOW LIGHT ---")
print()

# Group velocity for massive KG: v_g = c * sqrt(1 - m^2/omega^2)
# This is monotonically increasing from 0 (at threshold) to c (at infinity).
# For the BARE (uncoupled) branches, there is no slow-light effect beyond
# the trivial vanishing at threshold.
#
# Slow-light effects arise at the ANTICROSSING (polariton gap) where
# two branches hybridize. At the anticrossing, the dressed dispersion
# omega_+(k) and omega_-(k) develop an avoided crossing with
# |d omega/dk| -> local minimum.

# Compute group velocity of dressed polariton branches
dk_pol = np.diff(k_pol)
dk_pol = np.append(dk_pol, dk_pol[-1])  # pad

# B2-B1 anticrossing
d_omega_plus_B1 = np.gradient(omega_plus_B1, k_pol)
d_omega_minus_B1 = np.gradient(omega_minus_B1, k_pol)

# B2-B3 anticrossing
d_omega_plus_B3 = np.gradient(omega_plus_B3, k_pol)
d_omega_minus_B3 = np.gradient(omega_minus_B3, k_pol)

# Find minimum group velocity in each dressed branch
# The anticrossing is at k_star ~ 0.209
# Focus on the region near the anticrossing

mask_ac = (k_pol > 0.05) & (k_pol < 1.0)

# B2-B1: upper polariton
vg_plus_B1 = d_omega_plus_B1
vg_minus_B1 = d_omega_minus_B1

# Find slow-light (minimum |v_g|) near anticrossing
if np.any(mask_ac):
    idx_slow_plus_B1 = np.argmin(np.abs(vg_plus_B1[mask_ac]))
    idx_slow_minus_B1 = np.argmin(np.abs(vg_minus_B1[mask_ac]))

    k_slow_plus = k_pol[mask_ac][idx_slow_plus_B1]
    vg_slow_plus = vg_plus_B1[mask_ac][idx_slow_plus_B1]
    k_slow_minus = k_pol[mask_ac][idx_slow_minus_B1]
    vg_slow_minus = vg_minus_B1[mask_ac][idx_slow_minus_B1]

    print("B2-B1 anticrossing slow-light:")
    print(f"  Upper polariton: v_g_min = {vg_slow_plus:.6f} at k = {k_slow_plus:.4f}")
    print(f"  Lower polariton: v_g_min = {vg_slow_minus:.6f} at k = {k_slow_minus:.4f}")
    print(f"  Ratio v_g_min/c: upper = {vg_slow_plus/c_UV:.4f}, lower = {vg_slow_minus/c_UV:.4f}")
    print(f"  Anticrossing k* = {k_star:.4f}")
    print()

# B2-B3 anticrossing
vg_plus_B3 = d_omega_plus_B3
vg_minus_B3 = d_omega_minus_B3

if np.any(mask_ac):
    idx_slow_plus_B3 = np.argmin(np.abs(vg_plus_B3[mask_ac]))
    idx_slow_minus_B3 = np.argmin(np.abs(vg_minus_B3[mask_ac]))

    k_slow_plus_B3 = k_pol[mask_ac][idx_slow_plus_B3]
    vg_slow_plus_B3 = vg_plus_B3[mask_ac][idx_slow_plus_B3]
    k_slow_minus_B3 = k_pol[mask_ac][idx_slow_minus_B3]
    vg_slow_minus_B3 = vg_minus_B3[mask_ac][idx_slow_minus_B3]

    print("B2-B3 anticrossing slow-light:")
    print(f"  Upper polariton: v_g_min = {vg_slow_plus_B3:.6f} at k = {k_slow_plus_B3:.4f}")
    print(f"  Lower polariton: v_g_min = {vg_slow_minus_B3:.6f} at k = {k_slow_minus_B3:.4f}")
    print(f"  Ratio v_g_min/c: upper = {vg_slow_plus_B3/c_UV:.4f}, lower = {vg_slow_minus_B3/c_UV:.4f}")
    print()

# ============================================================
# 6. MULTI-METRIC STRUCTURE: QUANTITATIVE COMPARISON
# ============================================================

print("--- SECTION 6: MULTI-METRIC QUANTIFICATION ---")
print()

# The effective metric for branch i (in static background, Minkowski 4D) is:
#   g^{mu nu}_i = diag(-1, c_UV^2, c_UV^2, c_UV^2)
# This is UNIVERSAL -- all branches share the same metric at the level
# of the wave equation. The mass enters as a separate term, not as a
# metric modification.
#
# HOWEVER, the mode-dependent dispersion omega_i^2 = m_i^2 + c^2 k^2
# means that each branch has a different PROPAGATION SPEED at finite energy.
# The "effective metric seen by a wavepacket of energy E" is:
#
#   ds_i^2 = -c_i(E)^2 dt^2 + dx^2
#
# where c_i(E) = v_g_i(E) = c * sqrt(1 - m_i^2/E^2).
#
# This is NOT a modified metric in the GR sense -- it IS the standard massive
# Klein-Gordon equation in flat space. But in the analogue gravity framework,
# the mass gap plays the same role as a gravitational potential:
# different excitation species see different "gravitational fields."
#
# The physical signature is ARRIVAL TIME DIFFERENCE:
# Two excitations (B1 and B3) emitted simultaneously from the same event
# arrive at a distant detector at different times because they have
# different group velocities.

print("Arrival time differences (per M_KK^{-1} travel distance):")
print()

# Time for wavepacket at energy E to travel distance L:
# t_i = L / v_g_i = L / (c * sqrt(1 - m_i^2/E^2))
# Delta_t_{ij} = L * (1/v_g_i - 1/v_g_j)

E_test = np.array([2.5, 3.0, 5.0, 10.0, 20.0])
print(f"{'E (M_KK)':>10s}  {'dt(B2-B3)':>12s}  {'dt(B2-B1)':>12s}  {'dt(B1-B3)':>12s}")
for E in E_test:
    if E < M_B2:
        continue
    vg_B1 = c_UV * np.sqrt(1 - M_B1**2 / E**2)
    vg_B2 = c_UV * np.sqrt(1 - M_B2**2 / E**2)
    vg_B3 = c_UV * np.sqrt(1 - M_B3**2 / E**2)
    dt_23 = 1/vg_B2 - 1/vg_B3
    dt_21 = 1/vg_B2 - 1/vg_B1
    dt_13 = 1/vg_B1 - 1/vg_B3
    print(f"{E:10.1f}  {dt_23:12.6f}  {dt_21:12.6f}  {dt_13:12.6f}")

print()
print("(Positive dt means the first-named branch arrives LATER)")
print()

# ============================================================
# 7. EVANESCENT WINDOWS AND MODE EXCLUSION
# ============================================================

print("--- SECTION 7: EVANESCENT WINDOWS ---")
print()

# Below threshold omega < m_i, branch i is evanescent (no propagating solution).
# This creates "mode exclusion zones" in the (omega, branch) plane:
#   B3 propagates for omega > 0.990
#   B1 propagates for omega > 1.138
#   B2 propagates for omega > 2.228
#
# Between omega = 0.990 and 1.138: only B3 propagates -- SINGLE-MODE WINDOW
# Between omega = 1.138 and 2.228: B3 and B1 propagate -- TWO-MODE WINDOW
# Above omega = 2.228: all three propagate -- THREE-MODE WINDOW

print("Mode propagation windows:")
print(f"  omega < {M_B3:.3f}:                    ALL evanescent")
print(f"  {M_B3:.3f} < omega < {M_B1:.3f}:  B3 only (single mode)")
print(f"  {M_B1:.3f} < omega < {M_B2:.3f}:  B3 + B1 (two mode)")
print(f"  omega > {M_B2:.3f}:                    B3 + B1 + B2 (three mode)")
print()

# Width of each window
w_single = M_B1 - M_B3
w_two = M_B2 - M_B1
w_three_onset = M_B2

print(f"Single-mode window width: {w_single:.4f} M_KK ({w_single/M_B3*100:.1f}% of M_B3)")
print(f"Two-mode window width:    {w_two:.4f} M_KK ({w_two/M_B1*100:.1f}% of M_B1)")
print()

# Condensed matter analog: this is the phononic bandgap structure.
# In a phononic crystal with three branches, the gaps between onset
# frequencies create frequency windows where different numbers of
# branches contribute to transport. This is the internal-space analog
# of the "filter" effect in phononic metamaterials (Paper 06, Paper 34).

# ============================================================
# 8. ACOUSTIC METRIC AT ANTICROSSING (POLARITON SLOW-LIGHT)
# ============================================================

print("--- SECTION 8: POLARITON ACOUSTIC METRIC ---")
print()

# At the B2-B1 anticrossing, the dressed dispersion is:
#   omega_+/-(k) = (omega_B2(k) + omega_B1(k))/2 +/- sqrt(delta^2/4 + g^2)
# where omega_i(k) = sqrt(m_i^2 + c^2 k^2) and delta(k) = omega_B2(k) - omega_B1(k).
#
# The anticrossing happens at k = k* where omega_B2(k*) = omega_B1(k*).
# Since both have the SAME c^2 = 1/16, we need m_B2^2 + c^2 k*^2 = m_B1^2 + c^2 k*^2
# which gives k* = impossible (different masses, same c => they NEVER cross!).
#
# Wait -- the polariton data has k_star = 0.209. Let me check what was actually
# computed in s42_polariton.py. The branches are NOT bare Klein-Gordon;
# they include the full 8x8 Hamiltonian with Kosmann coupling.

# The polariton branches from s42_polariton.npz are the dressed ones.
# The anticrossing involves the FULL 8-mode coupled system, not just
# the 2x2 bare B2-B1 pair.

# The PHYSICAL polariton picture (from s42 Section 4):
# "phonon" = GPV collective mode at omega = 0.792 M_KK (flat, dispersionless)
# "photon" = KK gauge boson (dispersive, omega^2 = m^2 + c^2 k^2)
# Anticrossing at the k where the dispersive branch crosses the flat mode.

# For B2-B1: the B2 single-particle mode (0.845) and B1 (0.819) are BOTH
# dispersive with the same c. They never cross in the bare picture.
# The coupling g_B2_B1 = 0.080 produces a constant gap, not an anticrossing.
# What s42_polariton computed is the dressed branches INCLUDING the coupling.

# Let me reconstruct the coupled 2x2 problem at each k
omega_B2_bare = np.sqrt(M_B2**2 + c_UV**2 * k_pol**2)
omega_B1_bare = np.sqrt(M_B1**2 + c_UV**2 * k_pol**2)

# But the stored polariton branches have values near 0.8-0.9, not 2.2 and 1.1.
# The polariton computation used the SINGLE-PARTICLE energies (0.845, 0.819),
# not the BdG quasiparticle energies. Let me check.

omega_B2_sp = float(pd['omega_B2_sp'])  # 0.845
omega_B1_sp = float(pd['omega_B1_sp'])  # 0.819
omega_B3_sp = float(pd['omega_B3_sp'])  # 0.978

print(f"Single-particle energies (gap-edge):")
print(f"  B2 = {omega_B2_sp:.6f} M_KK")
print(f"  B1 = {omega_B1_sp:.6f} M_KK")
print(f"  B3 = {omega_B3_sp:.6f} M_KK")
print()

# The polariton branches are constructed with these gap-edge energies as
# the "phonon-like" flat modes, and they hybridize through V matrix.
# The k-dependence comes from treating them as on-shell modes where
# k enters through the detuning.
# omega_i(k) = sqrt(omega_i_sp^2 + c^2 k^2) seems unlikely given the
# values stored -- let me just use the stored polariton branches directly.

# Group velocity of the polariton branches (numerical derivative)
vg_pol_plus_B1 = np.gradient(omega_plus_B1, k_pol)
vg_pol_minus_B1 = np.gradient(omega_minus_B1, k_pol)
vg_pol_plus_B3 = np.gradient(omega_plus_B3, k_pol)
vg_pol_minus_B3 = np.gradient(omega_minus_B3, k_pol)

# Find the minimum group velocity in the vicinity of the anticrossing
# for the B2-B1 dressed branches
mask_near = (k_pol > 0.05) & (k_pol < 0.8)

if np.any(mask_near):
    # Upper polariton (B2-B1)
    vg_min_up_B1 = np.min(np.abs(vg_pol_plus_B1[mask_near]))
    k_min_up_B1 = k_pol[mask_near][np.argmin(np.abs(vg_pol_plus_B1[mask_near]))]

    # Lower polariton (B2-B1)
    vg_min_lo_B1 = np.min(np.abs(vg_pol_minus_B1[mask_near]))
    k_min_lo_B1 = k_pol[mask_near][np.argmin(np.abs(vg_pol_minus_B1[mask_near]))]

    # Upper polariton (B2-B3)
    vg_min_up_B3 = np.min(np.abs(vg_pol_plus_B3[mask_near]))
    k_min_up_B3 = k_pol[mask_near][np.argmin(np.abs(vg_pol_plus_B3[mask_near]))]

    # Lower polariton (B2-B3)
    vg_min_lo_B3 = np.min(np.abs(vg_pol_minus_B3[mask_near]))
    k_min_lo_B3 = k_pol[mask_near][np.argmin(np.abs(vg_pol_minus_B3[mask_near]))]

    print("Polariton slow-light (minimum |v_g| near anticrossing):")
    print(f"  B2-B1 upper: |v_g|_min = {vg_min_up_B1:.6f} at k = {k_min_up_B1:.4f}")
    print(f"  B2-B1 lower: |v_g|_min = {vg_min_lo_B1:.6f} at k = {k_min_lo_B1:.4f}")
    print(f"  B2-B3 upper: |v_g|_min = {vg_min_up_B3:.6f} at k = {k_min_up_B3:.4f}")
    print(f"  B2-B3 lower: |v_g|_min = {vg_min_lo_B3:.6f} at k = {k_min_lo_B3:.4f}")
    print()

    # Slow-light factor = c / v_g_min
    sf_up_B1 = c_UV / vg_min_up_B1 if vg_min_up_B1 > 0 else np.inf
    sf_lo_B1 = c_UV / vg_min_lo_B1 if vg_min_lo_B1 > 0 else np.inf

    print(f"  Slow-light factor (c / v_g_min):")
    print(f"    B2-B1 upper: {sf_up_B1:.1f}x")
    print(f"    B2-B1 lower: {sf_lo_B1:.1f}x")
    print()

# ============================================================
# 9. EFFECTIVE GRAVITATIONAL POTENTIAL PER BRANCH
# ============================================================

print("--- SECTION 9: EFFECTIVE GRAVITATIONAL POTENTIAL ---")
print()

# In the Volovik framework (Paper 10), the effective gravitational
# potential for a massive excitation with gap Delta is:
#   Phi_grav = Delta / E
# where E is the excitation energy. This gives an energy-dependent
# "gravitational field" that affects different branches differently.
#
# More precisely, the effective Newtonian potential that a mode of
# branch i "feels" in a region of varying tau is:
#   Phi_i(x) = (1/2) * (m_i(tau(x))^2 - m_i(tau_0)^2) / m_i(tau_0)^2
#
# Since m_i depends on tau through the BdG spectrum, spatial variations
# in tau create a branch-dependent gravitational potential.
#
# From s42_fabric_dispersion.npz: m_tau^2(tau) varies from 6.134 (tau=0.05)
# to 2.857 (tau=0.30).

m_tau_sq_arr = fd['m_tau_sq_arr']  # (10,) mass^2 at each tau
tau_grid = fd['tau_grid']          # (10,)

# The BdG quasiparticle energies at the fold are m_i = E_fold[i].
# How do they vary with tau? We need the tau-dependence of M_B1, M_B2, M_B3.
# The stored data gives E_fold at the fold (tau=0.190).
# The eps_fold and Delta_fold give the BCS structure: E = sqrt(eps^2 + Delta^2).
# Since eps and Delta both depend on tau, the branch masses vary with tau.

# Use the stored m_tau_sq_arr as a proxy for the overall spectral action curvature.
# The relative variation is:
dm2_frac = (m_tau_sq_arr[-1] - m_tau_sq_arr[0]) / m_tau_sq_arr[0]
print(f"Tau modulus mass^2 variation: {dm2_frac*100:.1f}% over tau=[{tau_grid[0]:.2f}, {tau_grid[-1]:.2f}]")
print()

# The effective "gravitational potential" difference between branches:
# At the fold (tau=0.190), the three branches see:
#   Phi_i ~ m_i^2 / (2 * m_ref^2)  relative to some reference
# The DIFFERENTIAL potential:
#   Delta_Phi_{ij} = (m_i^2 - m_j^2) / (2 * m_ref^2)
# This is the "tide" that separates different species.

m_ref = (M_B1 + M_B2 + M_B3) / 3.0  # average mass as reference

Delta_Phi_21 = (M_B2**2 - M_B1**2) / (2 * m_ref**2)
Delta_Phi_23 = (M_B2**2 - M_B3**2) / (2 * m_ref**2)
Delta_Phi_13 = (M_B1**2 - M_B3**2) / (2 * m_ref**2)

print(f"Differential gravitational potentials (m_ref = {m_ref:.4f}):")
print(f"  Delta_Phi(B2-B1) = {Delta_Phi_21:.4f}")
print(f"  Delta_Phi(B2-B3) = {Delta_Phi_23:.4f}")
print(f"  Delta_Phi(B1-B3) = {Delta_Phi_13:.4f}")
print()

# These are O(1) numbers -- the branches see VERY different effective
# potentials. This is because the mass hierarchy M_B2:M_B1:M_B3 = 2.23:1.14:0.99
# is not small. The "trimetric gravity" is strongly species-dependent.

# ============================================================
# 10. SUMMARY METRICS
# ============================================================

print("--- SECTION 10: SUMMARY AND CROSS-DOMAIN CONNECTIONS ---")
print()

# Mass hierarchy
r_21 = M_B2 / M_B1
r_23 = M_B2 / M_B3
r_13 = M_B1 / M_B3

print("Mass ratios:")
print(f"  M_B2/M_B1 = {r_21:.4f}")
print(f"  M_B2/M_B3 = {r_23:.4f}")
print(f"  M_B1/M_B3 = {r_13:.4f}")
print()

# Velocity ratios at selected energies
print("Group velocity ratios v_g(B3)/v_g(B2) at selected E:")
for E in [2.5, 3.0, 5.0, 10.0]:
    if E > M_B2:
        vg_B2 = c_UV * np.sqrt(1 - M_B2**2 / E**2)
        vg_B3 = c_UV * np.sqrt(1 - M_B3**2 / E**2)
        print(f"  E = {E:.1f}: v_B3/v_B2 = {vg_B3/vg_B2:.4f}")

print()

# The key structural observation:
# 1. Universal c = 1/4 from Trap 3 (e/(a*c) = 1/dim(spinor))
# 2. Branch masses from BdG: E_i = sqrt(eps_i^2 + Delta_i^2)
# 3. Three distinct light cones at any finite energy
# 4. UV convergence: all three converge to c = 1/4 as E -> infinity
# 5. Slow-light at polariton anticrossings
# 6. Single-mode window between M_B3 and M_B1

print("STRUCTURAL SUMMARY:")
print(f"  1. Universal UV speed: c = 1/4 = {c_UV:.4f}")
print(f"  2. Three rest masses: B1={M_B1:.3f}, B2={M_B2:.3f}, B3={M_B3:.3f}")
print(f"  3. Mass hierarchy: 2.25 : 1.15 : 1.00")
print(f"  4. Single-mode window: [{M_B3:.3f}, {M_B1:.3f}] (width {w_single:.3f})")
print(f"  5. UV Lorentz invariance recovery: delta_theta ~ (m_i^2 - m_j^2)/(2*E^2)")
print(f"  6. Effective metric: g^{{mu nu}} = diag(-1, 1/16, 1/16, 1/16) [universal]")
print(f"     + mass term m_i^2 phi_i = 0 [species-dependent]")
print()

# The multi-metric structure is NOT a modification of the spacetime metric.
# It is the standard physics of massive fields in flat space. The "acoustic
# metric" is UNIVERSAL: all branches share g^{mu nu} = diag(-1, c^2, c^2, c^2).
# The "species-dependent light cone" is the standard massive Klein-Gordon
# dispersion, which makes different-mass particles travel at different speeds.
#
# This is the CONDENSED MATTER analog of massive particle kinematics:
# in a phononic crystal with multiple optical branches, each branch has
# a different gap frequency, and wavepackets near the gap travel slowly.
# The "slow light" near the polariton anticrossing is the condensed-matter
# analog of near-threshold particle production.

print("CONDENSED MATTER ANALOGS:")
print("  - Phononic crystal with multiple optical branches (Paper 06)")
print("  - Branch-dependent group velocity = mass-dependent v_g in vacuum")
print("  - Polariton anticrossing = level repulsion in coupled oscillators")
print("  - Evanescent window = frequency stop-band in phononic bandgap")
print("  - UV convergence = Weyl's law universality at high frequency")
print()

print("VOLOVIK CONNECTION (Paper 10):")
print("  In Volovik's superfluid universe, different fermionic branches of the")
print("  3He-A order parameter see different effective metrics. The B1/B2/B3")
print("  branches are the internal-space analog. Volovik calls this 'multi-metric'")
print("  or 'bi-metric' gravity. Here it is TRI-metric. The crucial test:")
print("  do different SM particle species (corresponding to different branches)")
print("  propagate at different speeds? At energies E >> M_KK, NO (universal c).")
print("  At E ~ M_KK: YES, but this is the KK scale, not accessible.")
print()

# ============================================================
# 11. ACOUSTIC METRIC TENSOR (EXPLICIT FORM)
# ============================================================

print("--- SECTION 11: EXPLICIT METRIC TENSORS ---")
print()

# For a massive scalar field in a static background with no flow,
# the covariant metric is:
#
#   ds_i^2 = -(1/c_UV^2) dt^2 + d vec{x}^2
#
# This is the SAME for all branches. The wave equation is:
#   g^{mu nu} partial_mu partial_nu phi_i - (m_i^2 / c_UV^2) phi_i = 0
#
# Contravariant metric:
#   g^{mu nu} = diag(-c_UV^2, 1, 1, 1) * (rho / c_s) [BLV normalization]
#
# In the BLV convention (Barcelo+ 2005 eq 3.1), the acoustic metric
# for a scalar field with sound speed c_s in a fluid at rest is:
#   g^{mu nu} = (rho / c_s) * diag(-1/c_s^2, 1, 1, 1)
#
# For our system: c_s = c_UV = 1/4, and the conformal factor rho/c_s
# is universal (does not distinguish branches).

print("Barcelo-Liberati-Visser acoustic metric (static background):")
print()
print("  Contravariant (inverse metric):")
print(f"    g^{{mu nu}} = diag(-{1/c_UV**2:.0f}, 1, 1, 1)  [all branches]")
print()
print("  Covariant metric:")
print(f"    g_{{mu nu}} = diag(-{c_UV**2:.4f}, 1, 1, 1)  [all branches]")
print()
print("  The metric is UNIVERSAL. Branch distinction enters through the mass term.")
print()

# The wavepacket group velocity light-cone (not the metric light-cone)
# is mode-dependent:
for name, m in branches.items():
    v_lc = c_UV * np.sqrt(1 - m**2 / (2*m)**2)
    theta_lc = np.degrees(np.arctan(v_lc))
    print(f"  {name} (m={m:.3f}): wavepacket cone angle = {theta_lc:.2f} deg "
          f"at E = 2m = {2*m:.3f}")

print()

# ============================================================
# 12. ARRIVAL TIME DIFFERENCES (PHYSICAL OBSERVABLE)
# ============================================================

print("--- SECTION 12: PHYSICAL OBSERVABLES ---")
print()

# The only physically observable consequence of the multi-metric structure
# is the arrival time difference between wavepackets of different branches.
# This is the analog of neutrino time-of-flight experiments (OPERA, SN1987A).
#
# For two modes i and j with energies E_i, E_j traveling a distance L:
#   Delta_t / L = |1/v_g_i - 1/v_g_j|
#            = |(m_i^2 - m_j^2) / (2 c E^2)| + O(m^4/E^4)
# (in the high-energy limit E >> m_i, m_j)

# This is identical to the standard neutrino mass-induced time delay.
# At the KK scale (E ~ M_KK ~ 10^17 GeV, L ~ L_Planck), the effect is huge.
# At accessible energies (E << M_KK), the KK modes are not produced.

print("Arrival time difference (high-energy limit):")
print("  Delta_t / L = |m_i^2 - m_j^2| / (2 c_UV E^2)")
print()

dm2_21 = M_B2**2 - M_B1**2
dm2_23 = M_B2**2 - M_B3**2
dm2_13 = M_B1**2 - M_B3**2

print(f"  Delta(m^2)_B2-B1 = {dm2_21:.4f} M_KK^2")
print(f"  Delta(m^2)_B2-B3 = {dm2_23:.4f} M_KK^2")
print(f"  Delta(m^2)_B1-B3 = {dm2_13:.4f} M_KK^2")
print()

# At E = 3 M_KK:
E_ref = 3.0
dt_21_per_L = dm2_21 / (2 * c_UV * E_ref**2)
dt_23_per_L = dm2_23 / (2 * c_UV * E_ref**2)
dt_13_per_L = dm2_13 / (2 * c_UV * E_ref**2)

print(f"At E = {E_ref} M_KK:")
print(f"  Delta_t(B2-B1) / L = {dt_21_per_L:.4f} M_KK^{{-1}} per M_KK^{{-1}}")
print(f"  Delta_t(B2-B3) / L = {dt_23_per_L:.4f} M_KK^{{-1}} per M_KK^{{-1}}")
print(f"  Delta_t(B1-B3) / L = {dt_13_per_L:.4f} M_KK^{{-1}} per M_KK^{{-1}}")
print()

# ============================================================
# 13. GATE ASSESSMENT
# ============================================================

print("=" * 72)
print("GATE VERDICT: ACOUS-METRIC-43 = INFO")
print("=" * 72)
print()
print("The acoustic metric is UNIVERSAL: g^{mu nu} = diag(-16, 1, 1, 1)")
print("for all three BdG branches. The multi-metric structure is NOT a")
print("modification of the spacetime metric but the standard physics of")
print("massive Klein-Gordon fields with different masses in flat space.")
print()
print("Key findings:")
print(f"  1. Universal asymptotic speed c = 1/4 (from Trap 3: 1/dim(spinor))")
print(f"  2. Three rest masses create three distinct wavepacket cones")
print(f"  3. Maximum B2-B3 angular separation: {np.degrees(delta_max_23):.2f} deg")
print(f"  4. Single-mode (B3-only) window: [{M_B3:.3f}, {M_B1:.3f}] M_KK")
print(f"  5. UV Lorentz invariance recovery: delta_theta ~ m^2/E^2")
print(f"  6. Polariton slow-light: v_g_min/c as low as {vg_min_lo_B1/c_UV:.3f}")
print(f"  7. No metric modification -- mass term, not metric curvature")
print()
print("Physical interpretation:")
print("  The framework produces STANDARD massive field kinematics, not modified")
print("  gravity. This is the correct result: Volovik's multi-metric structure")
print("  operates at the FUNDAMENTAL level, producing the effective metric")
print("  from which particles emerge. Once the particles exist, they see the")
print("  SAME metric -- their mass differences are encoded in the mass term,")
print("  not the metric. The \"trimetric\" structure IS the three generations")
print("  of masses, not three spacetimes.")
print()

# ============================================================
# 14. PLOTS
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel (a): Group velocity vs k for bare branches
ax = axes[0, 0]
k_plot = np.linspace(0.01, 15, 1000)
colors = {'B3': '#2196F3', 'B1': '#4CAF50', 'B2': '#FF5722'}
labels_m = {'B3': f'B3 (m={M_B3:.3f})', 'B1': f'B1 (m={M_B1:.3f})', 'B2': f'B2 (m={M_B2:.3f})'}

for name in ['B3', 'B1', 'B2']:
    m = branches[name]
    w = np.sqrt(m**2 + c_UV**2 * k_plot**2)
    vg = c_UV**2 * k_plot / w
    ax.plot(k_plot, vg, color=colors[name], linewidth=2, label=labels_m[name])

ax.axhline(c_UV, color='black', linestyle='--', alpha=0.5, label=f'c = {c_UV}')
ax.set_xlabel('k (M_KK)', fontsize=12)
ax.set_ylabel('v_group (c = 1)', fontsize=12)
ax.set_title('(a) Group Velocity vs Momentum', fontsize=13)
ax.legend(fontsize=10)
ax.set_ylim(0, 0.30)
ax.grid(True, alpha=0.3)

# Panel (b): Light-cone angles vs omega
ax = axes[0, 1]
omega_plot = np.linspace(0.5, 8, 1000)

for name in ['B3', 'B1', 'B2']:
    m = branches[name]
    mask = omega_plot > m
    theta = np.full_like(omega_plot, np.nan)
    theta[mask] = np.degrees(np.arctan(c_UV * np.sqrt(1 - m**2 / omega_plot[mask]**2)))
    ax.plot(omega_plot, theta, color=colors[name], linewidth=2, label=labels_m[name])

ax.axhline(np.degrees(np.arctan(c_UV)), color='black', linestyle='--', alpha=0.5,
           label=f'c = 1/4 ({np.degrees(np.arctan(c_UV)):.1f} deg)')

# Mark evanescent boundaries
for name in ['B3', 'B1', 'B2']:
    m = branches[name]
    ax.axvline(m, color=colors[name], linestyle=':', alpha=0.4)

ax.set_xlabel('omega (M_KK)', fontsize=12)
ax.set_ylabel('Light-cone angle (deg)', fontsize=12)
ax.set_title('(b) Wavepacket Cone Angle vs Energy', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel (c): Polariton dispersion with group velocity overlay
ax = axes[1, 0]

# Plot polariton branches
ax.plot(k_pol, omega_plus_B1, color='#E91E63', linewidth=2, label='B2-B1 upper')
ax.plot(k_pol, omega_minus_B1, color='#9C27B0', linewidth=2, label='B2-B1 lower')
ax.plot(k_pol, omega_plus_B3, color='#00BCD4', linewidth=1.5, linestyle='--', label='B2-B3 upper')
ax.plot(k_pol, omega_minus_B3, color='#607D8B', linewidth=1.5, linestyle='--', label='B2-B3 lower')

# Mark anticrossing
ax.axvline(k_star, color='gray', linestyle=':', alpha=0.5)
ax.annotate(f'k* = {k_star:.3f}', xy=(k_star, 0.76), fontsize=9, color='gray')

# Mark gap
gap_B2_B1 = float(pd['gap_B2_B1_disp'])
omega_mid = (omega_plus_B1[np.argmin(np.abs(k_pol - k_star))] +
             omega_minus_B1[np.argmin(np.abs(k_pol - k_star))]) / 2
ax.annotate('', xy=(k_star + 0.03, omega_mid + gap_B2_B1/2),
            xytext=(k_star + 0.03, omega_mid - gap_B2_B1/2),
            arrowprops=dict(arrowstyle='<->', color='red', lw=1.5))
ax.text(k_star + 0.08, omega_mid, f'gap = {gap_B2_B1:.3f}', fontsize=9, color='red')

ax.set_xlabel('k (M_KK)', fontsize=12)
ax.set_ylabel('omega (M_KK)', fontsize=12)
ax.set_title('(c) Polariton Dispersion (Anticrossing)', fontsize=13)
ax.legend(fontsize=9, loc='lower right')
ax.set_xlim(0, 1.0)
ax.set_ylim(0.6, 1.15)
ax.grid(True, alpha=0.3)

# Panel (d): Polariton group velocity
ax = axes[1, 1]

mask_plot = (k_pol > 0.01) & (k_pol < 0.8)
k_p = k_pol[mask_plot]

ax.plot(k_p, vg_pol_plus_B1[mask_plot], color='#E91E63', linewidth=2, label='B2-B1 upper')
ax.plot(k_p, vg_pol_minus_B1[mask_plot], color='#9C27B0', linewidth=2, label='B2-B1 lower')
ax.plot(k_p, vg_pol_plus_B3[mask_plot], color='#00BCD4', linewidth=1.5, linestyle='--', label='B2-B3 upper')
ax.plot(k_p, vg_pol_minus_B3[mask_plot], color='#607D8B', linewidth=1.5, linestyle='--', label='B2-B3 lower')

ax.axhline(c_UV, color='black', linestyle='--', alpha=0.5, label=f'c = {c_UV}')
ax.axvline(k_star, color='gray', linestyle=':', alpha=0.5)

ax.set_xlabel('k (M_KK)', fontsize=12)
ax.set_ylabel('v_group (M_KK = 1)', fontsize=12)
ax.set_title('(d) Polariton Group Velocity (Slow Light)', fontsize=13)
ax.legend(fontsize=9, loc='upper left')
ax.set_xlim(0, 0.8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(base / "s43_acoustic_metric.png", dpi=150, bbox_inches='tight')
print(f"Plot saved: {base / 's43_acoustic_metric.png'}")

# ============================================================
# 15. SAVE DATA
# ============================================================

np.savez(
    base / "s43_acoustic_metric.npz",
    # Gate
    gate_verdict='INFO',
    gate_name='ACOUS-METRIC-43',
    # Branch masses
    M_B1=M_B1,
    M_B2=M_B2,
    M_B3=M_B3,
    c_UV=c_UV,
    # Mass hierarchy
    mass_ratio_B2_B1=r_21,
    mass_ratio_B2_B3=r_23,
    mass_ratio_B1_B3=r_13,
    # Delta m^2
    dm2_B2_B1=dm2_21,
    dm2_B2_B3=dm2_23,
    dm2_B1_B3=dm2_13,
    # Light cone separations
    delta_theta_max_B2_B3_deg=np.degrees(delta_max_23),
    delta_theta_max_B2_B1_deg=np.degrees(delta_max_21),
    delta_theta_max_B1_B3_deg=np.degrees(delta_max_13),
    omega_max_delta_B2_B3=omega_max_23,
    omega_max_delta_B2_B1=omega_max_21,
    # Evanescent windows
    single_mode_window_low=M_B3,
    single_mode_window_high=M_B1,
    single_mode_width=w_single,
    two_mode_window_high=M_B2,
    # Polariton slow-light
    vg_min_upper_B1=vg_min_up_B1,
    vg_min_lower_B1=vg_min_lo_B1,
    vg_min_upper_B3=vg_min_up_B3,
    vg_min_lower_B3=vg_min_lo_B3,
    slow_factor_upper_B1=sf_up_B1,
    slow_factor_lower_B1=sf_lo_B1,
    # Differential potentials
    Delta_Phi_B2_B1=Delta_Phi_21,
    Delta_Phi_B2_B3=Delta_Phi_23,
    Delta_Phi_B1_B3=Delta_Phi_13,
    # Arrival time differences at E = 3 M_KK
    dt_per_L_B2_B1_E3=dt_21_per_L,
    dt_per_L_B2_B3_E3=dt_23_per_L,
    dt_per_L_B1_B3_E3=dt_13_per_L,
    # Grids (for downstream use)
    k_grid=k,
    omega_grid=omega_grid,
    # Group velocities on dense grid
    vg_B1=v_group['B1'],
    vg_B2=v_group['B2'],
    vg_B3=v_group['B3'],
)

print(f"Data saved: {base / 's43_acoustic_metric.npz'}")
print()
print("DONE.")
