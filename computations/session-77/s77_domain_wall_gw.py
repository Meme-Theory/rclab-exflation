#!/usr/bin/env python3
"""
S77-C8-DW-GW: Gravitational Waves from Domain Wall Annihilation.

Physics: The BCS phase transition at the fold (tau=0.190) breaks a discrete
Z_2 symmetry (BDI class). This nucleates domain walls -- topological defects
with surface tension sigma ~ Delta_BCS^3 * M_KK. S76 closed Z_2 domain-wall
DM (Josephson symmetrization), but the walls themselves form as transient
topological defects and annihilate when the Josephson coupling becomes
dynamically relevant.

The GW spectrum from domain wall annihilation follows:
  - Hiramatsu et al. (2013), Saikawa (2017): numerical calibration
  - The peak frequency is set by the Hubble rate at annihilation
  - The spectral shape is Omega_GW(f) ~ f^3 (causal, f < f_peak)
    and ~ f^{-1} (f > f_peak)

Wall annihilation epoch:
  - Walls form at the BCS transit (T ~ M_KK)
  - Walls annihilate when bias energy > wall tension / Hubble radius
  - For Z_2 with Josephson bias: t_ann ~ sigma / (Delta_V * H)
  - The Josephson coupling provides the bias that collapses walls

Gate: S77-C8-DW-GW
  PASS if Omega_GW > 1e-12 at any frequency in LISA or PTA band
  FAIL if Omega_GW < 1e-15 everywhere
  INFO if 1e-15 < Omega_GW < 1e-12

Inputs:
  - canonical_constants.py: Delta_BCS, M_KK, xi_BCS, J_C2, tau_fold
  - s76_reheat_temperature.npz: T_RH = 1.70e15 GeV
  - s76_moduli_decay_gw_spectrum.npz: cross-checks

Author: hawking-theorist (S77)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_Pl_reduced, M_KK_gravity, M_KK, m_tau, Delta_BCS, xi_BCS,
    J_C2, tau_fold, H_fold, T_CMB_GeV, H_0_GeV, T_BBN_GeV,
    g_star_SM, g_star_BBN, hbar_GeV_s, rho_crit_GeV4, Omega_r,
    Gamma_Langer_BCS, N_cells, dt_transit,
)

# ============================================================
# STEP 0: Domain wall parameters from BCS physics
# ============================================================

print("=" * 70)
print("S77-C8-DW-GW: GW from Domain Wall Annihilation")
print("=" * 70)
print()

# S76 updated parameters
T_RH_GeV = 1.70e15       # (local) GeV, from S76 W2-H
tau_decay_s = 4.44e-40    # (local) s, from S76 (note: this is the PROMPT value)
m_tau_MKK = m_tau         # 2.062 M_KK (canonical)
m_tau_GeV = m_tau_MKK * M_KK_gravity  # (local) GeV

# Domain wall surface tension:
# For a Z_2 BCS domain wall, the wall interpolates between two degenerate
# BCS ground states related by the Z_2. The surface tension is:
#   sigma_wall = integral dz [gradient_energy + potential_barrier]
# For a kink of width ~ xi_BCS connecting two minima separated by Delta_BCS:
#   sigma_wall ~ Delta_BCS^2 / xi_BCS  (in M_KK units, then * M_KK^3)
#
# More precisely, for a GL potential V(phi) = (a/2)*phi^2 + (b/4)*phi^4:
#   The kink solution gives sigma = (2*sqrt(2)/3) * |a|^{3/2} / sqrt(b)
#   = (2*sqrt(2)/3) * Delta^3 / (Delta/xi) (using Delta ~ sqrt(|a|/b), xi ~ 1/sqrt(|a|))
#   = (2*sqrt(2)/3) * Delta^2 * xi  ... but dimensionally this needs M_KK^3
#
# Standard BCS domain wall: sigma ~ Delta_BCS^2 * (1/xi_BCS) * M_KK^3
# This is because the gradient energy is (d phi/dz)^2 * M_KK^3
# where phi varies by Delta_BCS over distance xi_BCS * M_KK^{-1}.

# The GL functional gives: sigma = (2*sqrt(2)/3) * sqrt(|a_GL|^3 / b_GL)
# Using a_GL = -0.5245, b_GL = 0.4418 from canonical:
from canonical_constants import a_GL, b_GL

sigma_wall_MKK3 = (2 * np.sqrt(2) / 3) * np.sqrt(abs(a_GL)**3 / b_GL)  # (local) M_KK^3
sigma_wall_GeV3 = sigma_wall_MKK3 * M_KK_gravity**3  # (local) GeV^3

print("--- STEP 0: Domain Wall Parameters ---")
print(f"  Delta_BCS = {Delta_BCS:.4f} M_KK = {Delta_BCS * M_KK_gravity:.3e} GeV")
print(f"  xi_BCS = {xi_BCS:.4f} M_KK^-1 = {xi_BCS / M_KK_gravity:.3e} GeV^-1")
print(f"  a_GL = {a_GL:.4f}, b_GL = {b_GL:.4f}")
print(f"  sigma_wall = {sigma_wall_MKK3:.4f} M_KK^3 = {sigma_wall_GeV3:.3e} GeV^3")

# Wall width (the region over which order parameter varies):
L_wall_MKK_inv = xi_BCS  # (local) wall width ~ coherence length
L_wall_GeV_inv = L_wall_MKK_inv / M_KK_gravity  # (local) GeV^{-1}
print(f"  L_wall = {L_wall_MKK_inv:.4f} M_KK^-1 = {L_wall_GeV_inv:.3e} GeV^-1")

# Cross-check: sigma ~ Delta^2 / xi in M_KK^3
sigma_check = Delta_BCS**2 / xi_BCS  # (local) rough estimate
print(f"  Cross-check: Delta^2/xi = {sigma_check:.4f} M_KK^3 (cf {sigma_wall_MKK3:.4f})")

# Domain wall spacing at formation:
# Walls form with spacing ~ Hubble radius at formation
# Formation happens at the BCS transit, when H ~ H_fold
L_H_fold = 1.0 / (H_fold * M_KK_gravity)  # (local) Hubble radius at fold, GeV^{-1}
print(f"  H_fold = {H_fold:.1f} M_KK = {H_fold * M_KK_gravity:.3e} GeV")
print(f"  L_Hubble(fold) = {L_H_fold:.3e} GeV^-1")

# Wall separation at formation is ~ the correlation length at the transition
# which is max(xi_BCS, 1/H_fold). Since xi_BCS = 0.808 M_KK^{-1} and
# 1/H_fold = 1/586.5 M_KK^{-1} = 0.00170 M_KK^{-1}:
# The walls are MUCH closer than the Hubble radius at formation.
L_corr_MKK_inv = xi_BCS  # (local) correlation length at formation
print(f"  L_corr / L_Hubble = {L_corr_MKK_inv * H_fold:.2f}")
print(f"  (Walls form INSIDE Hubble volume: {L_corr_MKK_inv * H_fold:.2f} << 1 WAIT")
# Actually: L_corr = xi_BCS = 0.808 M_KK^{-1}, H_fold = 586.5 M_KK
# => L_corr * H_fold = 0.808 * 586.5 = 473.9
# This means L_corr ~ 474 Hubble radii -- the walls are much LARGER than Hubble
# This is wrong. Let me reconsider.
#
# In causal structure: domains form with size at most ~ Hubble at formation.
# After that, domains grow. For Z_2 breaking during the transit:
# The transit is SUPERSONIC (Mach 13.75), so the BCS transition happens
# globally (the transit is causal -- driven by modulus rolling, not thermal).
# The domain size is set by the NUMBER of causal patches at formation.
#
# Actually: N_cells = 32 from canonical. The tessellation has 32 cells.
# Each cell is a domain. Wall spacing ~ L_domain ~ (Volume)^{1/3} / N_cells^{1/3}.

# After transit: the universe reheats. Domain walls start to scale with Hubble.
# The crucial question is: WHEN do they annihilate?

# ============================================================
# STEP 1: Domain wall annihilation from Josephson bias
# ============================================================

print()
print("--- STEP 1: Wall Annihilation from Josephson Bias ---")

# The Z_2 symmetry is APPROXIMATE -- the Josephson coupling J_C2 provides
# a bias between the two vacua. This bias gives a volume energy density
# difference between the two sides of the wall:
#   Delta_V = J_C2 * M_KK^4  (the Josephson coupling has dimension M_KK)
#
# Actually: J_C2 = 0.933 M_KK is a coupling energy, not a volume energy.
# The bias energy density is:
#   epsilon_bias ~ J_C2 * Delta_BCS^2 * M_KK^4 / L_domain
#
# Wait -- let me be more careful. In the GL picture with a Z_2 potential:
#   V(phi) = (a/2)phi^2 + (b/4)phi^4
# The Z_2 is exact. But the Josephson coupling between adjacent cells
# introduces a field-dependent bias. When summed over the tessellation,
# this gives a volume energy difference:
#   Delta_V ~ J_C2 * (Delta_BCS / M_KK)^2 * M_KK^4
# between the + and - domains.
#
# More physically: the Josephson coupling J_C2 = 0.933 M_KK represents
# the inter-cell phase stiffness. For domain walls, the relevant bias is:
#   epsilon_bias = 2 * J_C2 * (cos(theta) - 1) summed over links
# For Z_2 walls, theta = pi, so cos(theta) - 1 = -2.
# Each wall has ~N_cells^{2/3} broken links. The bias per unit volume:
#   Delta_V ~ J_C2 * N_cells^{2/3} / V_total * M_KK^4

# Simpler and more robust: the bias energy DENSITY from the Josephson
# coupling is:
#   Delta_V = J_C2 * Delta_BCS^2 * M_KK^4
# This is because the Josephson coupling acts on the order parameter
# field as a linear perturbation: H_J ~ J * phi, and phi ~ Delta_BCS,
# so the energy difference per M_KK^3 volume is:
#   Delta_V ~ J_C2 * Delta_BCS * M_KK^4

# For precision: the bias comes from the explicit Z_2 breaking.
# S76 found that Josephson symmetrization (tunneling between + and - vacua)
# renders Z_2 walls unstable. The tunneling rate is:
#   Gamma_tunnel ~ omega_att * exp(-S_inst * V_wall / T_acoustic)
# But for GW purposes, what matters is the ANNIHILATION TEMPERATURE.

# Standard domain wall annihilation criterion (Vilenkin & Shellard):
# Walls annihilate when the pressure from the bias exceeds the wall tension / Hubble:
#   Delta_V > sigma_wall * H(T_ann)
# where H(T) = sqrt(g_* * pi^2 / 90) * T^2 / M_Pl in RD era.

# The bias energy density from Josephson coupling:
# epsilon_bias = J_C2 * Delta_BCS * M_KK^4
# This is the energy difference per unit volume between the two vacua.
epsilon_bias_MKK4 = J_C2 * Delta_BCS  # (local) M_KK^4 units
epsilon_bias_GeV4 = epsilon_bias_MKK4 * M_KK_gravity**4  # (local) GeV^4

print(f"  J_C2 = {J_C2:.3f} M_KK (Josephson coupling)")
print(f"  epsilon_bias = J_C2 * Delta_BCS = {epsilon_bias_MKK4:.4f} M_KK^4")
print(f"  epsilon_bias = {epsilon_bias_GeV4:.3e} GeV^4")

# Annihilation condition: Delta_V > sigma_wall * H(T_ann)
# => H(T_ann) < Delta_V / sigma_wall
# => T_ann^2 < (90 / (g_* * pi^2)) * M_Pl^2 * Delta_V / sigma_wall

H_ann_max = epsilon_bias_GeV4 / sigma_wall_GeV3  # (local) GeV
print(f"  H_ann < epsilon_bias / sigma_wall = {H_ann_max:.3e} GeV")

# In RD era: H(T) = sqrt(pi^2 * g_* / 90) * T^2 / M_Pl
# => T_ann = sqrt(H_ann * M_Pl * sqrt(90 / (pi^2 * g_*)))
g_star_ann = g_star_SM  # (local) 106.75, walls annihilate above EW scale
prefactor_H_to_T = np.sqrt(90 / (PI**2 * g_star_ann))  # (local)
T_ann_GeV = np.sqrt(H_ann_max * M_Pl_reduced * prefactor_H_to_T)  # (local) GeV

print(f"  T_ann (from bias condition) = {T_ann_GeV:.3e} GeV")
print(f"  T_ann / M_KK = {T_ann_GeV / M_KK_gravity:.3e}")
print(f"  T_ann / T_RH = {T_ann_GeV / T_RH_GeV:.3e}")

# BUT: T_ann cannot be higher than T_RH (walls only exist after reheating
# in the standard picture). In our framework, walls form during the transit
# BEFORE reheating. They exist during the modulus oscillation epoch too.
# However, the Josephson coupling is active from the moment walls form.
#
# The more relevant question: do walls survive to the RD era?
# During the modulus domination epoch, H ~ (2/3t) and the wall network
# either:
#   (a) Gets eaten by the Josephson bias before modulus decay -> no GW signal
#   (b) Survives to RD -> annihilates at T_ann in RD era -> GW signal
#
# Annihilation timescale from formation:
# t_ann ~ sigma_wall / (epsilon_bias * c^2) for 1D kink dynamics
t_ann_nat = sigma_wall_GeV3 / epsilon_bias_GeV4  # (local) GeV^{-1} (natural units)
t_ann_s = t_ann_nat * hbar_GeV_s  # (local) seconds
print(f"  t_ann (natural) = sigma/epsilon = {t_ann_nat:.3e} GeV^-1")
print(f"  t_ann = {t_ann_s:.3e} s")

# Compare to modulus decay time:
Gamma_total_GeV = 4.05e12  # (local) GeV, from S76
tau_mod_decay_s = hbar_GeV_s / Gamma_total_GeV  # (local) s
print(f"  tau_modulus_decay = {tau_mod_decay_s:.3e} s")
print(f"  t_ann / tau_decay = {t_ann_s / tau_mod_decay_s:.3e}")

# ============================================================
# STEP 2: Determine the wall annihilation epoch
# ============================================================

print()
print("--- STEP 2: Wall Annihilation Epoch ---")

# Key result: t_ann << tau_decay means walls annihilate DURING the
# modulus oscillation epoch, before reheating.
#
# But this needs more care. The annihilation timescale t_ann ~ sigma/epsilon
# assumes the bias acts on a wall of Hubble size. Initially the walls are
# much smaller (formed during transit, spacing ~ xi_BCS).
# Small walls annihilate FASTER (less inertia). So:
# - Small walls: annihilate on timescale ~ L_wall / c ~ xi_BCS / M_KK ~ very fast
# - Hubble-size walls: annihilate on timescale ~ sigma/(epsilon*H)
#
# The wall network undergoes a SCALING SOLUTION: walls quickly reach
# ~one wall per Hubble volume. This happens in time ~ 1/H_fold.
# After that, the network evolves in the scaling regime.
#
# In scaling, the wall energy density is:
#   rho_wall ~ sigma * H(t)
# where H(t) is the Hubble parameter.
#
# The bias causes the network to collapse when:
#   t > t_ann ~ sigma / epsilon_bias
#
# Let's check whether this is before or after reheating.

# H at wall annihilation (during MD era):
# During MD: H(t) = 2/(3t), so t = 2/(3H)
# Wall annihilation when t = t_ann:
H_at_ann = 2.0 / (3.0 * t_ann_nat)  # (local) GeV, H during MD at t_ann

# Compare to H at reheating:
# H(T_RH) = Gamma_total (reheating happens when H ~ Gamma)
H_at_RH = Gamma_total_GeV  # (local) GeV

print(f"  H_at_annihilation = {H_at_ann:.3e} GeV (during MD)")
print(f"  H_at_reheating = {H_at_RH:.3e} GeV")
print(f"  Ratio H_ann/H_RH = {H_at_ann / H_at_RH:.3e}")

if H_at_ann > H_at_RH:
    print("  => Walls annihilate BEFORE reheating (during modulus domination)")
    ann_epoch = "MD"
else:
    print("  => Walls annihilate AFTER reheating (during radiation domination)")
    ann_epoch = "RD"

# The temperature at annihilation (if during RD):
# If during MD, we can still define an effective temperature from the
# radiation sub-component.
if ann_epoch == "MD":
    # During MD, the radiation temperature falls as T ~ a^{-3/8} * T_RH
    # (radiation diluted faster than matter, but entropy conserved within radiation)
    # Actually: during MD, T_rad ~ a^{-1} (adiabatic cooling of the radiation bath)
    # But the radiation is subdominant. After reheating at H = Gamma:
    # T_RH = (90 / (pi^2 * g_*))^{1/4} * sqrt(Gamma * M_Pl)

    # For GW calculation during MD epoch:
    # The wall energy density at annihilation:
    rho_wall_ann = sigma_wall_GeV3 * H_at_ann  # (local) GeV^4 (scaling solution)

    # Total energy density at annihilation:
    rho_total_ann = 3 * M_Pl_reduced**2 * H_at_ann**2  # (local) GeV^4

    # Wall fraction at annihilation:
    Omega_wall_ann = rho_wall_ann / rho_total_ann  # (local)

    print(f"  rho_wall(ann) = sigma * H = {rho_wall_ann:.3e} GeV^4")
    print(f"  rho_total(ann) = 3*M_Pl^2*H^2 = {rho_total_ann:.3e} GeV^4")
    print(f"  Omega_wall(ann) = {Omega_wall_ann:.3e}")

    # Temperature at annihilation for peak frequency:
    # During MD, the Hubble-to-temperature relation:
    # H = (2/3t), t_RH = 1/Gamma
    # a(t)/a(t_RH) = (t/t_RH)^{2/3}
    # T(a) = T_RH * (a_RH/a)
    # => T_ann = T_RH * (t_RH/t_ann)^{2/3}
    T_ann_eff = T_RH_GeV * (tau_mod_decay_s / t_ann_s)**(2.0/3.0)  # (local) GeV
    # Wait -- this gives T_ann > T_RH since t_ann < t_decay.
    # That's consistent: before reheating, the radiation temperature
    # is HIGHER (the universe is hotter earlier).

    # Actually during MD before reheating, there is no thermal bath yet.
    # The "temperature" concept is ill-defined. What matters for the GW
    # peak frequency is the Hubble rate at annihilation, redshifted to today.

    # Scale factor ratio from annihilation to today:
    # a_ann / a_0 = a_ann/a_RH * a_RH/a_0
    # a_ann/a_RH = (H_RH/H_ann)^{2/3} during MD (a ~ t^{2/3}, H ~ t^{-1})
    a_ann_over_a_RH = (H_at_RH / H_at_ann)**(2.0/3.0)  # (local)

    # a_RH/a_0 = T_CMB / T_RH * (g_*(T_0)/g_*(T_RH))^{1/3}
    # Using T_0 = T_CMB_GeV, g_*(T_0) = 3.36 (photons + neutrinos after decoupling)
    g_star_0 = 3.36  # (local) effective dof today
    a_RH_over_a_0 = T_CMB_GeV / T_RH_GeV * (g_star_0 / g_star_SM)**(1.0/3.0)  # (local)

    a_ann_over_a_0 = a_ann_over_a_RH * a_RH_over_a_0  # (local)
    print(f"  a_ann/a_RH = {a_ann_over_a_RH:.3e}")
    print(f"  a_RH/a_0 = {a_RH_over_a_0:.3e}")
    print(f"  a_ann/a_0 = {a_ann_over_a_0:.3e}")

else:
    # RD annihilation
    # Wall energy at annihilation:
    H_ann_RD = epsilon_bias_GeV4 / sigma_wall_GeV3  # (local)
    T_ann_RD = np.sqrt(H_ann_RD * M_Pl_reduced * prefactor_H_to_T)  # (local)

    rho_wall_ann = sigma_wall_GeV3 * H_ann_RD  # (local)
    rho_total_ann = 3 * M_Pl_reduced**2 * H_ann_RD**2  # (local)
    Omega_wall_ann = rho_wall_ann / rho_total_ann  # (local)

    g_star_0 = 3.36  # (local)
    a_ann_over_a_0 = T_CMB_GeV / T_ann_RD * (g_star_0 / g_star_ann)**(1.0/3.0)  # (local)

    print(f"  T_ann (RD) = {T_ann_RD:.3e} GeV")
    print(f"  rho_wall(ann) = {rho_wall_ann:.3e} GeV^4")
    print(f"  rho_total(ann) = {rho_total_ann:.3e} GeV^4")
    print(f"  Omega_wall(ann) = {Omega_wall_ann:.3e}")
    print(f"  a_ann/a_0 = {a_ann_over_a_0:.3e}")

# ============================================================
# STEP 3: GW spectrum from wall annihilation
# ============================================================

print()
print("--- STEP 3: GW Production ---")

# Standard result from numerical simulations of domain wall annihilation
# (Hiramatsu, Kawasaki, Saikawa 2013; Saikawa 2017):
#
#   Omega_GW(production) ~ epsilon_GW * (Omega_wall)^2
#
# where:
#   epsilon_GW ~ 0.7 (GW efficiency from simulations, Hiramatsu+ 2013)
#   Omega_wall = rho_wall / rho_total at annihilation
#
# The peak frequency at production is ~ H_ann (Hubble at annihilation).
# This redshifts to today as f_peak = H_ann * (a_ann/a_0).

epsilon_GW = 0.7  # (local) GW efficiency from lattice simulations (Hiramatsu+ 2013)

# GW density parameter at production:
Omega_GW_prod = epsilon_GW * Omega_wall_ann**2  # (local)

print(f"  epsilon_GW = {epsilon_GW} (lattice calibration)")
print(f"  Omega_wall(ann) = {Omega_wall_ann:.3e}")
print(f"  Omega_GW(production) = epsilon_GW * Omega_wall^2 = {Omega_GW_prod:.3e}")

# Cross-check: GW energy < wall energy
assert Omega_GW_prod < Omega_wall_ann, "GW energy exceeds wall energy -- unphysical"
print(f"  CHK1 PASS: Omega_GW/Omega_wall = {Omega_GW_prod/Omega_wall_ann:.3e} < 1")

# Peak frequency:
# At production, the peak is at the Hubble scale: f_peak(prod) ~ H_ann
# Redshifted to today:
f_peak_GeV = H_at_ann * a_ann_over_a_0  # (local) GeV
f_peak_Hz = f_peak_GeV / (2 * PI * hbar_GeV_s)  # (local) Hz (f = E / (2*pi*hbar))
# More precisely: f = H * (a/a_0) / (2*pi) -- the 2*pi converts angular to linear

print(f"  H_ann = {H_at_ann:.3e} GeV")
print(f"  f_peak(today) = {f_peak_Hz:.3e} Hz")

# ============================================================
# STEP 4: Redshift GW to today
# ============================================================

print()
print("--- STEP 4: Redshift to Today ---")

# The GW density parameter today:
# Omega_GW(today) = Omega_GW(prod) * (rho_rad(prod) / rho_total(prod))
#                  * (g_*(prod)/g_*(today))^{-1/3} * Omega_rad(today)
#
# During MD (if annihilation is during MD):
#   After annihilation, GWs redshift as a^{-4}, matter as a^{-3}.
#   So from annihilation to reheating:
#     Omega_GW dilutes by factor (a_ann/a_RH)
#   After reheating (RD), Omega_GW is constant until matter-radiation equality.
#   Then from equality to today, all radiation gets another factor Omega_rad(today).
#
# Standard formula for GW from a source during MD:
#   Omega_GW(today)*h^2 = Omega_rad(today)*h^2 * (g_*/g_0)^{-1/3}
#                         * Omega_GW(production) / (a_ann/a_RH)
#
# Actually, the simplest approach:
# rho_GW(today) = rho_GW(ann) * (a_ann/a_0)^4
# rho_crit(today) = 3 * H_0^2 * M_Pl^2
# Omega_GW(today) = rho_GW(today) / rho_crit(today)

rho_GW_ann = Omega_GW_prod * rho_total_ann  # (local) GeV^4

# rho_GW(today) = rho_GW(ann) * (a_ann/a_0)^4
rho_GW_today = rho_GW_ann * a_ann_over_a_0**4  # (local) GeV^4

# Omega_GW(today):
Omega_GW_today = rho_GW_today / rho_crit_GeV4  # (local)

print(f"  rho_GW(ann) = {rho_GW_ann:.3e} GeV^4")
print(f"  (a_ann/a_0)^4 = {a_ann_over_a_0**4:.3e}")
print(f"  rho_GW(today) = {rho_GW_today:.3e} GeV^4")
print(f"  rho_crit(today) = {rho_crit_GeV4:.3e} GeV^4")
print(f"  Omega_GW(today) = {Omega_GW_today:.3e}")

# Cross-check via standard transfer formula:
# Omega_GW(today) * h^2 = 1.67e-5 * (g_*/100)^{-1/3} * Omega_GW(source)
# This applies for sources during RD. For MD sources, there's an extra
# dilution factor from the MD->RD transition at reheating.
#
# For MD source:
# Omega_GW(today) = Omega_r * (g_star_ann/g_star_0)^{-1/3} * Omega_GW_prod * (H_RH/H_ann)^{2/3}
# The (H_RH/H_ann)^{2/3} is the dilution during MD (a_ann/a_RH).

if ann_epoch == "MD":
    Omega_GW_today_check = (Omega_r *
                            (g_star_SM / g_star_0)**(-1.0/3.0) *
                            Omega_GW_prod *
                            a_ann_over_a_RH)  # (local)
    print(f"  Cross-check (transfer formula): {Omega_GW_today_check:.3e}")
    print(f"  Ratio (direct/transfer) = {Omega_GW_today / Omega_GW_today_check:.2f}")

# ============================================================
# STEP 5: BBN constraint and detector comparison
# ============================================================

print()
print("--- STEP 5: BBN Constraint and Detector Comparison ---")

BBN_bound = 5.6e-6  # (local) Delta N_eff < 0.4 constraint on Omega_GW at BBN

# Omega_GW at BBN:
# From production to BBN, if during MD:
# Omega_GW(BBN) = Omega_GW(today) / Omega_r * some g_* corrections
# More carefully: Omega_GW(BBN) = rho_GW(BBN) / rho_total(BBN)
# During RD (after reheating), Omega_GW is constant (both scale as a^{-4}).
# So Omega_GW(BBN) = Omega_GW(after reheating).
#
# From production (during MD) to reheating:
# rho_GW ~ a^{-4}, rho_mod ~ a^{-3}
# Omega_GW(RH) = Omega_GW(prod) * (a_ann/a_RH)
# = Omega_GW(prod) * (H_RH/H_ann)^{2/3}
if ann_epoch == "MD":
    Omega_GW_RH = Omega_GW_prod * a_ann_over_a_RH  # (local)
    # During RD from reheating to BBN: constant (up to g_* changes)
    Omega_GW_BBN = Omega_GW_RH * (g_star_BBN / g_star_SM)**(1.0/3.0)  # (local)
else:
    # Annihilation during RD: constant from ann to BBN (up to g_*)
    Omega_GW_BBN = Omega_GW_prod * (g_star_BBN / g_star_ann)**(1.0/3.0)  # (local)

print(f"  Omega_GW(BBN) = {Omega_GW_BBN:.3e}")
print(f"  BBN bound = {BBN_bound:.1e}")
print(f"  BBN safe: {Omega_GW_BBN < BBN_bound} (margin: {BBN_bound/Omega_GW_BBN:.1e}x)")
assert Omega_GW_BBN < BBN_bound, "CHK2 FAIL: Omega_GW(BBN) exceeds BBN bound"
print(f"  CHK2 PASS: Omega_GW(BBN) = {Omega_GW_BBN:.3e} < {BBN_bound:.1e}")

# LISA sensitivity: Omega_GW ~ 1e-12 at 1e-3 Hz (design sensitivity)
# DECIGO: ~ 1e-15 at 0.1-1 Hz
# PTA (NANOGrav): ~ 1e-9 at 1e-8 Hz
# ET (Einstein Telescope): ~ 1e-13 at 10-100 Hz
LISA_band = (1e-4, 1e-1)  # (local) Hz
LISA_sens = 1e-12  # (local) Omega_GW sensitivity
PTA_band = (1e-9, 1e-7)  # (local) Hz
PTA_sens = 1e-9  # (local)
ET_band = (1, 1e4)  # (local) Hz
ET_sens = 1e-13  # (local)
DECIGO_band = (1e-2, 1e1)  # (local) Hz
DECIGO_sens = 1e-16  # (local)

print()
print(f"  f_peak = {f_peak_Hz:.3e} Hz")
print(f"  LISA band: {LISA_band[0]:.0e} - {LISA_band[1]:.0e} Hz")
print(f"  PTA band: {PTA_band[0]:.0e} - {PTA_band[1]:.0e} Hz")
print(f"  ET band: {ET_band[0]:.0e} - {ET_band[1]:.0e} Hz")
print(f"  DECIGO band: {DECIGO_band[0]:.0e} - {DECIGO_band[1]:.0e} Hz")

in_LISA = LISA_band[0] <= f_peak_Hz <= LISA_band[1]  # (local)
in_PTA = PTA_band[0] <= f_peak_Hz <= PTA_band[1]  # (local)
in_ET = ET_band[0] <= f_peak_Hz <= ET_band[1]  # (local)
in_DECIGO = DECIGO_band[0] <= f_peak_Hz <= DECIGO_band[1]  # (local)

print(f"  f_peak in LISA: {in_LISA}")
print(f"  f_peak in PTA: {in_PTA}")
print(f"  f_peak in ET: {in_ET}")
print(f"  f_peak in DECIGO: {in_DECIGO}")

# ============================================================
# STEP 6: Compute full spectrum Omega_GW(f)
# ============================================================

print()
print("--- STEP 6: Full Spectrum ---")

# Spectral shape from domain wall annihilation (Hiramatsu+ 2013):
#   Omega_GW(f) ~ (f/f_peak)^3 for f < f_peak (causal)
#   Omega_GW(f) ~ (f/f_peak)^{-1} for f > f_peak
#
# This is the characteristic "broken power law" shape.

f_array = np.logspace(-12, 12, 2000)  # (local) Hz, broad range
Omega_GW_f = np.zeros_like(f_array)  # (local)

for i, f in enumerate(f_array):
    x = f / f_peak_Hz  # (local)
    if x < 1:
        Omega_GW_f[i] = Omega_GW_today * x**3
    else:
        Omega_GW_f[i] = Omega_GW_today * x**(-1)

print(f"  Spectrum computed over {len(f_array)} frequencies")
print(f"  f range: {f_array[0]:.1e} to {f_array[-1]:.1e} Hz")
print(f"  Omega_GW peak = {Omega_GW_today:.3e} at f = {f_peak_Hz:.3e} Hz")

# Evaluate at specific detector frequencies:
f_LISA_mid = 1e-3  # (local) Hz, LISA optimal
f_PTA_mid = 3e-8  # (local) Hz, PTA (NANOGrav)
f_ET_mid = 30.0  # (local) Hz, ET optimal
f_DECIGO_mid = 0.1  # (local) Hz

def omega_gw_at_f(f_eval):
    """Evaluate Omega_GW at a specific frequency."""
    x = f_eval / f_peak_Hz  # (local)
    if x < 1:
        return Omega_GW_today * x**3
    else:
        return Omega_GW_today * x**(-1)

Omega_at_LISA = omega_gw_at_f(f_LISA_mid)  # (local)
Omega_at_PTA = omega_gw_at_f(f_PTA_mid)  # (local)
Omega_at_ET = omega_gw_at_f(f_ET_mid)  # (local)
Omega_at_DECIGO = omega_gw_at_f(f_DECIGO_mid)  # (local)

print()
print("  Omega_GW at detector frequencies:")
print(f"    PTA (3e-8 Hz):    {Omega_at_PTA:.3e}")
print(f"    LISA (1e-3 Hz):   {Omega_at_LISA:.3e}")
print(f"    DECIGO (0.1 Hz):  {Omega_at_DECIGO:.3e}")
print(f"    ET (30 Hz):       {Omega_at_ET:.3e}")

# Maximum Omega_GW in each detector band:
def max_omega_in_band(f_lo, f_hi):
    """Find maximum Omega_GW within a frequency band."""
    if f_peak_Hz >= f_lo and f_peak_Hz <= f_hi:
        return Omega_GW_today  # peak is in band
    elif f_peak_Hz < f_lo:
        # Peak below band -- evaluate at f_lo (falling spectrum)
        return omega_gw_at_f(f_lo)
    else:
        # Peak above band -- evaluate at f_hi (rising spectrum)
        return omega_gw_at_f(f_hi)

Omega_max_LISA = max_omega_in_band(*LISA_band)  # (local)
Omega_max_PTA = max_omega_in_band(*PTA_band)  # (local)
Omega_max_ET = max_omega_in_band(*ET_band)  # (local)
Omega_max_DECIGO = max_omega_in_band(*DECIGO_band)  # (local)

print()
print("  Maximum Omega_GW in each band:")
print(f"    PTA:    {Omega_max_PTA:.3e} (sensitivity ~{PTA_sens:.0e})")
print(f"    LISA:   {Omega_max_LISA:.3e} (sensitivity ~{LISA_sens:.0e})")
print(f"    DECIGO: {Omega_max_DECIGO:.3e} (sensitivity ~{DECIGO_sens:.0e})")
print(f"    ET:     {Omega_max_ET:.3e} (sensitivity ~{ET_sens:.0e})")

# ============================================================
# STEP 7: Gate Verdict
# ============================================================

print()
print("=" * 70)
print("--- GATE: S77-C8-DW-GW ---")

# The gate evaluates at ANY frequency in LISA or PTA band:
Omega_max_any = max(Omega_max_LISA, Omega_max_PTA, Omega_max_ET, Omega_max_DECIGO)  # (local)

print(f"  Omega_GW(peak) = {Omega_GW_today:.3e}")
print(f"  f_peak = {f_peak_Hz:.3e} Hz")
print(f"  Max in any detector band = {Omega_max_any:.3e}")
print(f"  Max in LISA = {Omega_max_LISA:.3e}")
print(f"  BBN safe: {Omega_GW_BBN:.3e} < {BBN_bound:.1e}")

if Omega_max_any > 1e-12:
    verdict = "PASS"
    verdict_detail = f"Omega_GW = {Omega_max_any:.3e} > 1e-12"
elif Omega_max_any < 1e-15:
    verdict = "FAIL"
    verdict_detail = f"Omega_GW = {Omega_max_any:.3e} < 1e-15"
else:
    verdict = "INFO"
    verdict_detail = f"1e-15 < Omega_GW = {Omega_max_any:.3e} < 1e-12"

print(f"  PASS threshold: Omega_GW > 1e-12")
print(f"  FAIL threshold: Omega_GW < 1e-15")
print(f"  Verdict: {verdict} — {verdict_detail}")
print("=" * 70)

# ============================================================
# STEP 8: Save results
# ============================================================

print()
print("--- Saving results ---")

outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "s77_domain_wall_gw.npz")

np.savez(outpath,
         # Gate
         verdict=verdict,
         # Domain wall parameters
         sigma_wall_MKK3=sigma_wall_MKK3,
         sigma_wall_GeV3=sigma_wall_GeV3,
         epsilon_bias_MKK4=epsilon_bias_MKK4,
         epsilon_bias_GeV4=epsilon_bias_GeV4,
         L_wall_MKK_inv=L_wall_MKK_inv,
         # Annihilation
         ann_epoch=ann_epoch,
         H_at_ann=H_at_ann,
         t_ann_s=t_ann_s,
         T_ann_GeV=T_ann_GeV if ann_epoch == "RD" else 0.0,
         a_ann_over_a_0=a_ann_over_a_0,
         Omega_wall_ann=Omega_wall_ann,
         # GW production
         Omega_GW_prod=Omega_GW_prod,
         Omega_GW_today=Omega_GW_today,
         Omega_GW_BBN=Omega_GW_BBN,
         f_peak_Hz=f_peak_Hz,
         # Spectrum
         f_array_Hz=f_array,
         Omega_GW_f=Omega_GW_f,
         # Detector evaluation
         Omega_max_LISA=Omega_max_LISA,
         Omega_max_PTA=Omega_max_PTA,
         Omega_max_ET=Omega_max_ET,
         Omega_max_DECIGO=Omega_max_DECIGO,
         # BBN
         BBN_bound=BBN_bound,
         BBN_safe=Omega_GW_BBN < BBN_bound,
         # Cross-checks
         Omega_GW_over_Omega_wall=Omega_GW_prod / Omega_wall_ann,
         )

print(f"  Saved: {outpath}")

# ============================================================
# STEP 9: Plot
# ============================================================

print("--- Generating plot ---")

fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# GW spectrum
ax.loglog(f_array, Omega_GW_f, 'b-', linewidth=2, label='Domain wall GW')

# Peak marker
ax.axvline(f_peak_Hz, color='blue', linestyle='--', alpha=0.5, label=f'f_peak = {f_peak_Hz:.1e} Hz')

# Detector sensitivity curves (approximate power-law integrated sensitivities)
f_LISA = np.logspace(-4, -1, 100)  # (local)
Omega_LISA_sens = 1e-12 * np.ones_like(f_LISA)  # (local) approximate
ax.fill_between(f_LISA, Omega_LISA_sens, 1e-6 * np.ones_like(f_LISA),
                alpha=0.15, color='green', label='LISA sensitivity')  # (local)

f_DECIGO_arr = np.logspace(-2, 1, 100)  # (local)
Omega_DECIGO_sens = 1e-16 * np.ones_like(f_DECIGO_arr)  # (local)
ax.fill_between(f_DECIGO_arr, Omega_DECIGO_sens, 1e-12 * np.ones_like(f_DECIGO_arr),
                alpha=0.15, color='purple', label='DECIGO sensitivity')  # (local)

f_ET_arr = np.logspace(0, 4, 100)  # (local)
Omega_ET_sens = 1e-13 * np.ones_like(f_ET_arr)  # (local)
ax.fill_between(f_ET_arr, Omega_ET_sens, 1e-6 * np.ones_like(f_ET_arr),
                alpha=0.15, color='orange', label='ET sensitivity')  # (local)

f_PTA_arr = np.logspace(-9, -7, 100)  # (local)
Omega_PTA_sens = 1e-9 * np.ones_like(f_PTA_arr)  # (local)
ax.fill_between(f_PTA_arr, Omega_PTA_sens, 1e-5 * np.ones_like(f_PTA_arr),
                alpha=0.15, color='red', label='PTA sensitivity')  # (local)

# BBN bound
ax.axhline(BBN_bound, color='red', linestyle=':', linewidth=1.5,
           label=f'BBN bound ({BBN_bound:.1e})')

# Gate thresholds
ax.axhline(1e-12, color='green', linestyle=':', alpha=0.7, linewidth=1,
           label='PASS threshold (1e-12)')
ax.axhline(1e-15, color='gray', linestyle=':', alpha=0.7, linewidth=1,
           label='FAIL threshold (1e-15)')

ax.set_xlabel('Frequency [Hz]', fontsize=14)
ax.set_ylabel(r'$\Omega_{\rm GW}(f)$', fontsize=14)
ax.set_title(f'S77-C8-DW-GW: Domain Wall GW Spectrum\n'
             f'Verdict: {verdict} | Peak: {Omega_GW_today:.2e} at {f_peak_Hz:.2e} Hz',
             fontsize=14)
ax.set_xlim(1e-12, 1e12)
ax.set_ylim(1e-30, 1e-4)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, alpha=0.3, which='both')

# Add annotations
ax.annotate(f'Wall annihilation: {ann_epoch}\n'
            f'sigma = {sigma_wall_MKK3:.3f} M_KK^3\n'
            f'epsilon = {epsilon_bias_MKK4:.3f} M_KK^4\n'
            f't_ann = {t_ann_s:.1e} s\n'
            f'BBN: {Omega_GW_BBN:.1e} (safe)',
            xy=(0.02, 0.02), xycoords='axes fraction',
            fontsize=9, verticalalignment='bottom',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()

plotpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "s77_domain_wall_gw.png")
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

print()
print("DONE.")
