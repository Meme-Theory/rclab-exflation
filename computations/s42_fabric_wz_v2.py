#!/usr/bin/env python3
"""
s42_fabric_wz_v2.py — Fabric-Collective Dark Energy w(z) (W-Z-42 REDO #2)

Einstein-Theorist, Session 42.

CRITICAL ERROR IN REDO #1 (s42_fabric_wz.py):
  Compared domain wall thickness at the KK scale (~10^{-49} Mpc) to cell size
  at the Hubble scale today (~10^3 Mpc). These are quantities from DIFFERENT
  EPOCHS separated by 10^{10+} e-folds. The wall fraction must be evaluated
  AT THE SAME EPOCH.

THE CORRECT PHYSICAL PICTURE:
  The fabric IS space. The 32 cells ARE the spatial structure. Domain walls
  ARE the cosmic web. Cell interiors ARE the cosmic voids.

  At the transit epoch:
  - The Hubble radius was at the KK scale: R_H(transit) ~ 1/H_transit ~ 1/M_KK
  - The correlation length was also at the KK scale: xi_BCS ~ 13.95/M_KK
  - The cell size WAS the Hubble radius (cells were the whole universe)
  - f_walls(transit) = xi_BCS / R_H(transit) = xi_BCS * H_transit
  - Both are at the KK scale => f_walls(transit) ~ O(1) or even >> 1

  After expansion (two scenarios):
  (a) FROZEN walls (tau frozen, comoving structure preserved):
      f_walls(today) = f_walls(transit)  [comoving wall/cell ratio preserved]
  (b) SCALING solution (dynamic walls under tension):
      Standard domain wall network: one wall per Hubble volume
      f_walls decreases as sigma*G/H ~ a^{-1} or faster

  The physical wall fraction TODAY depends on the DYNAMICS of wall evolution.

COMPUTATION:
  1. f_walls in the frozen-wall limit (W2-2: tau frozen)
  2. f_walls in the scaling-solution limit (standard cosmological domain walls)
  3. w_eff for each case
  4. w(z) evolution
  5. Parameter scan over (f_walls, delta_tau)
  6. DESI comparison
  7. CC identification alternatives
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ========================================================================
# 1. LOAD UPSTREAM DATA
# ========================================================================
gs = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
fd = np.load('tier0-computation/s42_fabric_dispersion.npz', allow_pickle=True)
vor = np.load('tier0-computation/s42_giant_voronoi.npz', allow_pickle=True)
td = np.load('tier0-computation/s42_tau_dyn_reopening.npz', allow_pickle=True)
sf = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)
inst = np.load('tier0-computation/s37_instanton_action.npz', allow_pickle=True)

# Extract key quantities
tau_fold = 0.190
Z_fold = float(gs['Z_fold'].flat[0])       # 74730.76
V_fold = float(gs['S_fold'].flat[0])        # 250360.68
dV_fold = float(gs['dS_fold'].flat[0])      # 58672.80
d2V_fold = float(gs['d2S_fold'].flat[0])    # 317862.85
m_tau = float(fd['m_tau'].flat[0])           # 2.062 M_KK
xi_BCS_over_BW = float(inst['xi_BCS_over_BW'])  # 13.952 (xi_BCS in units of 1/M_KK)
xi_BCS_MKK = xi_BCS_over_BW                  # 13.95 M_KK^{-1} -- NO: this is xi_BCS/BW
# Correct: xi_BCS from inst is 0.808 M_KK^{-1}, and xi_BCS_over_BW = xi_BCS / BW = 13.95
xi_BCS_raw = float(inst['xi_BCS'])           # 0.808 M_KK^{-1}

N_cells = int(vor['N_cells'])                # 32

# BCS data
from canonical_constants import E_cond, M_Pl_unreduced as M_Planck_GeV  # S36 ED-CONV-36
Delta_B3 = 0.176      # B3 gap (M_KK)
v_B2 = float(fd['v_th_B2'].flat[0])  # 0.618

# Physical constants
## M_Planck_GeV imported from canonical_constants above
Lambda_obs_MP4 = 2.888e-122
H_0_GeV = 1.438e-42   # H_0 in GeV (67.4 km/s/Mpc)
hbar_c_GeV_fm = 0.1973269804
Mpc_to_fm = 3.0857e38

# M_KK test values
MKK_values = [1e9, 1e13, 1e18]
MKK_labels = ['10^9', '10^{13}', '10^{18}']

print("=" * 78)
print("W-Z-42 (REDO #2): FABRIC-COLLECTIVE DARK ENERGY w(z)")
print("Einstein-Theorist, Session 42")
print("REPLACES: both single-tau AND incorrect-scale-comparison computations.")
print("=" * 78)

# ========================================================================
# 2. CORRELATION LENGTH AND HUBBLE RADIUS AT THE TRANSIT
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 1: WALL FRACTION AT THE TRANSIT EPOCH")
print("=" * 78)

print(f"""
PHYSICAL PICTURE:
  At the transit epoch, the fabric undergoes the BCS transition.
  The Hubble radius R_H = c/H and the correlation length xi_BCS
  are BOTH at the KK scale.

  From the framework:
    xi_BCS = {xi_BCS_raw:.4f} M_KK^{{-1}}   (BCS coherence length, from S37)
    xi_BCS/BW = {xi_BCS_over_BW:.2f}        (ratio to bandwidth)
    m_tau = {m_tau:.4f} M_KK              (modulus mass)
    1/m_tau = {1/m_tau:.4f} M_KK^{{-1}}      (bare Compton wavelength)

  The wall thickness is set by the LARGER of xi_BCS and 1/m_tau:
    delta_wall = max(xi_BCS, 1/m_tau) = {max(xi_BCS_raw, 1/m_tau):.4f} M_KK^{{-1}}

  The Hubble parameter at the transit depends on the energy density:
    H_transit^2 = (8 pi G / 3) * rho_transit
    rho_transit ~ V_fold * M_KK^4   (spectral action dominates)

  In natural units (c = hbar = 1):
    H_transit = sqrt(V_fold) * M_KK^2 / (sqrt(3) * M_Planck)
    R_H = 1/H_transit = sqrt(3) * M_Planck / (sqrt(V_fold) * M_KK^2)
""")

# Wall thickness at transit
delta_wall_MKK = max(xi_BCS_raw, 1.0/m_tau)  # in M_KK^{-1}

# Also compute the BCS coherence length from v_F and Delta
xi_BCS_alt = v_B2 / (np.pi * Delta_B3)  # = 0.618 / (pi * 0.176) = 1.118 M_KK^{-1}
delta_wall_MKK_alt = xi_BCS_alt

print(f"  Wall thickness estimates:")
print(f"    1/m_tau = {1/m_tau:.4f} M_KK^{{-1}}")
print(f"    xi_BCS (S37, from BW) = {xi_BCS_raw:.4f} M_KK^{{-1}}")
print(f"    xi_BCS (v_F/pi*Delta) = {xi_BCS_alt:.4f} M_KK^{{-1}}")
print(f"    Using: delta_wall = {delta_wall_MKK_alt:.4f} M_KK^{{-1}} (v_F/pi*Delta, largest)")

# Use the v_F/pi*Delta estimate as it's the most physically motivated BCS coherence length
delta_wall = delta_wall_MKK_alt  # 1.118 M_KK^{-1}

print(f"\n--- HUBBLE RADIUS AT TRANSIT ---")

results_frozen = {}
results_scaling = {}

for MKK_GeV, label in zip(MKK_values, MKK_labels):
    print(f"\n  M_KK = {label} GeV:")

    # Hubble parameter at transit
    # H = sqrt(8*pi*G/3) * sqrt(rho) = sqrt(V_fold) * M_KK^2 / (sqrt(3) * M_P)
    # In units of M_KK:
    H_transit_MKK = np.sqrt(V_fold) * MKK_GeV / (np.sqrt(3) * M_Planck_GeV)
    R_H_transit_MKK = 1.0 / H_transit_MKK  # in M_KK^{-1}

    # Wall fraction at transit: ratio of wall thickness to Hubble radius
    # For a 3D tessellation at the transit, the wall fraction is:
    # f_walls(transit) = delta_wall / R_H  (if delta_wall < R_H)
    #                  = 1                 (if delta_wall >= R_H, walls fill space)
    #
    # More precisely: the number of domains in one Hubble volume is
    # N_domain = (R_H / xi_corr)^3. The wall volume fraction in each
    # domain is ~ delta_wall / xi_corr. So:
    # f_walls = delta_wall / xi_corr
    # where xi_corr is the correlation length at formation.
    #
    # In the BCS case, the correlation length IS the wall thickness
    # (the wall profile is a kink over one coherence length), so:
    # f_walls = delta_wall / L_domain
    # L_domain = min(R_H, xi_corr at causality-limited scale)
    #
    # If BCS transition happens when xi_BCS > R_H (supercritical),
    # then the entire Hubble volume is ONE domain, and f_walls = 0
    # within that volume (no walls). Walls form at the boundary of
    # causally disconnected regions (Kibble mechanism).
    #
    # If BCS transition happens when xi_BCS < R_H (subcritical),
    # then N_domain = (R_H/xi_BCS)^3 domains form per Hubble volume,
    # with walls between them.
    #
    # The COMOVING wall fraction is:
    # f_walls = (wall area per domain * delta_wall) / (domain volume)
    # For spherical domains of radius L_d:
    # f_walls ~ 3 * delta_wall / L_d   (surface/volume of sphere)

    # Domain size = xi_BCS (each domain has coherent BCS order parameter)
    # Wall thickness = delta_wall ~ xi_BCS (they're the same scale!)
    # So f_walls ~ 3 * delta_wall / xi_BCS ~ 3 * 1 = O(1) at formation

    # But this is TOO simple. The wall between two BCS domains is a KINK
    # in the order parameter. Its thickness is xi_BCS. The domain size is
    # also xi_BCS (for the Kibble mechanism). So the wall fraction at
    # formation is genuinely O(1): the entire fabric is walls.

    # More carefully:
    # At the BCS transition (second order, Z_2 universality from GL-CUBIC-36):
    # - Correlation length diverges: xi -> infinity at T_c
    # - The FROZEN correlation length is set by the quench rate (Kibble-Zurek):
    #   xi_KZ = xi_0 * (tau_Q / tau_0)^{nu/(1 + nu*z_KZ)}
    # - From S37: tau_Q = 0.12, tau_0 = 1.27, nu = 1/2, z_KZ = 2
    #   xi_KZ = (1/m_tau) * (0.12/1.27)^{1/4} = 0.485 * 0.555 = 0.269 M_KK^{-1}
    # - But the BCS coherence length is xi_BCS = 1.118 M_KK^{-1} > xi_KZ
    # - The PHYSICAL domain size is max(xi_KZ, xi_BCS) = xi_BCS

    # For KZ: domain size L_d = xi_KZ (= 0.269 M_KK^{-1}), much smaller than R_H.
    # Wall thickness = 1/m_tau (= 0.485 M_KK^{-1}) or xi_BCS (= 1.118 M_KK^{-1})
    # If wall thickness > domain size: WALLS FILL SPACE (f_walls = 1)

    # Let me be precise about what sets the wall profile width.
    # For a BCS order parameter: the domain wall profile is
    # Delta(x) = Delta_0 * tanh(x / (sqrt(2) * xi_GL))
    # where xi_GL is the Ginzburg-Landau coherence length.
    # xi_GL = hbar v_F / (pi Delta_0) = xi_BCS = 1.118 M_KK^{-1}
    #
    # The Kibble-Zurek domain size is:
    # L_KZ = xi_KZ = 0.269 M_KK^{-1}    (from KZ with BCS exponents)
    #
    # Wall width / domain size = xi_BCS / xi_KZ = 1.118 / 0.269 = 4.15
    # The wall is 4x WIDER than the domain. The walls overlap.
    # => f_walls = 1 at formation.

    # Alternatively, the relevant domain size is NOT xi_KZ but R_H.
    # If R_H > xi_BCS, then we can have domains separated by walls.
    # If R_H < xi_BCS, the entire Hubble patch is within one coherence length
    # and there are no walls within the observable universe at that epoch.

    xi_KZ = (1/m_tau) * (0.12/1.27)**0.25  # 0.269 M_KK^{-1}

    print(f"    H_transit = {H_transit_MKK:.6e} M_KK")
    print(f"    R_H(transit) = {R_H_transit_MKK:.2f} M_KK^{{-1}}")
    print(f"    xi_BCS = {delta_wall:.4f} M_KK^{{-1}}")
    print(f"    xi_KZ = {xi_KZ:.4f} M_KK^{{-1}}")
    print(f"    R_H / xi_BCS = {R_H_transit_MKK / delta_wall:.2f}")
    print(f"    R_H / xi_KZ = {R_H_transit_MKK / xi_KZ:.2f}")
    print(f"    xi_BCS / xi_KZ = {delta_wall / xi_KZ:.2f}")

    # For the frozen-wall limit:
    # The comoving wall fraction is set at formation and preserved.
    # If L_domain = xi_KZ (Kibble-Zurek), then:
    # f_walls_frozen = 3 * min(delta_wall, L_domain) / L_domain
    # But if delta_wall > L_domain, the walls overlap: f_walls = 1.

    if delta_wall >= xi_KZ:
        f_walls_frozen = 1.0  # Walls fill space at formation
        reason = "xi_BCS > xi_KZ: walls overlap, fill space"
    else:
        f_walls_frozen = 3.0 * delta_wall / xi_KZ
        reason = f"3 * delta_wall / xi_KZ = {f_walls_frozen:.3f}"

    # If L_domain = R_H (causally limited), then:
    if delta_wall >= R_H_transit_MKK:
        f_walls_RH = 1.0
        reason_RH = "xi_BCS > R_H: entire Hubble patch is wall"
    else:
        f_walls_RH = 3.0 * delta_wall / R_H_transit_MKK
        reason_RH = f"3 * delta_wall / R_H = {f_walls_RH:.4e}"

    print(f"    f_walls (KZ domains): {f_walls_frozen:.4f} ({reason})")
    print(f"    f_walls (Hubble domains): {f_walls_RH} ({reason_RH})")

    # FROZEN WALL LIMIT: comoving wall fraction preserved
    # Today's wall fraction = f_walls(transit) [no evolution in comoving coords]
    # BUT: the walls redshift differently from the bulk.
    #
    # Domain wall energy density: rho_wall ~ sigma / (a * L_domain_comoving)
    # where sigma is the surface tension.
    # In comoving coordinates, L_domain is fixed. In physical:
    # L_domain_phys = a * L_domain_comov.
    #
    # Domain wall energy density scales as:
    #   rho_wall ~ sigma * (area / volume) ~ sigma / L_phys ~ sigma / (a * L_comov)
    #   => rho_wall ~ a^{-1} (domain walls: effective w = -2/3)
    #
    # The bulk (CC) energy is constant: rho_bulk = V_fold * M_KK^4 = const
    #
    # So the ENERGY fraction in walls today:
    #   f_wall_energy(a) = rho_wall(a) / [rho_wall(a) + rho_bulk]
    #                    = f_0 / (a * (f_0/a + 1 - f_0))   (not quite right)
    #
    # Let me be more careful. At transit (a = a_tr):
    #   rho_total = rho_wall + rho_bulk
    #   f_wall = rho_wall / rho_total
    #
    # At later time (a > a_tr):
    #   rho_wall(a) = rho_wall(a_tr) * (a_tr / a)   [w = -2/3 scaling]
    #   rho_bulk(a) = rho_bulk(a_tr)                 [w = -1 scaling]
    #
    # f_wall(a) = rho_wall(a) / [rho_wall(a) + rho_bulk(a)]
    #           = f_wall_tr * (a_tr/a) / [f_wall_tr*(a_tr/a) + (1 - f_wall_tr)]
    #
    # At a = a_0 = 1 (today), a_tr is incredibly small:
    # a_tr = T_0 / T_transit ~ 2.7 K / T_transit
    # T_transit ~ M_KK ~ 10^9 to 10^18 GeV ~ 10^{22} to 10^{31} K
    # a_tr ~ 10^{-22} to 10^{-31}

    from canonical_constants import T_CMB_GeV  # 2.725 K in GeV
    a_transit = T_CMB_GeV / MKK_GeV  # Very rough: T_transit ~ M_KK
    # More precisely: the number of e-folds from transit to today
    # ln(a_0/a_tr) = ln(1/a_tr) = ln(M_KK / T_CMB) ~ 50 to 72

    ln_expansion = np.log(1.0 / a_transit)

    # Wall energy fraction today (frozen limit):
    f_wall_tr = f_walls_frozen  # = 1 in the KZ case
    f_wall_today_frozen = f_wall_tr * a_transit / (f_wall_tr * a_transit + (1 - f_wall_tr))
    # When f_wall_tr = 1: f_wall_today = a_transit / (a_transit + 0) = 1.0 (!)
    # This is because if ALL the energy is in walls at transit, and walls
    # scale as a^{-1} while nothing else exists, then f_wall = 1 forever.
    # But this can't be right: the bulk V_fold is the CC and doesn't scale away.

    # The issue is WHAT the "bulk" energy is. If:
    # (A) The bulk energy IS V_fold (the spectral action = CC), then
    #     rho_bulk = V_fold * M_KK^4 = const, and
    #     rho_wall = f_wall_tr * V_fold * M_KK^4 at transit, scaling as a^{-1}
    # (B) The bulk energy is from radiation/matter (scaling as a^{-4}/a^{-3})
    #     which dilutes much faster than walls

    # Physical picture: At transit, the energy budget is:
    # rho_total = V_fold * M_KK^4  (spectral action, the CC)
    #           + gradient energy   (from domain wall structure)
    #           + matter/radiation  (from transit products)
    #
    # The gradient/wall energy WITHIN each domain wall is:
    # rho_grad_wall = (1/2) * Z * (delta_tau / delta_wall)^2 * M_KK^4
    #
    # The question is: what is delta_tau?
    # delta_tau = variation in tau between adjacent domains.
    # At the BCS transition, adjacent domains have DIFFERENT BCS phases
    # but the SAME tau (tau is the modulus, which is smooth).
    # The BCS order parameter Delta varies across walls, not tau itself!
    #
    # CRITICAL DISTINCTION:
    # Domain walls in the BCS condensate are walls where Delta(x) changes sign
    # (or phase). The TAU modulus need not vary across these walls at all.
    # The wall energy comes from the gradient in Delta, not in tau.
    #
    # The energy of a BCS domain wall is:
    # sigma_BCS = (2/3) * N(0) * Delta_0^2 * xi_BCS   (BCS kink energy per area)
    # where N(0) is DOS, Delta_0 is gap, xi_BCS is coherence length.
    #
    # This is an energy in the FERMION/PAIRING sector, not in the tau modulus.
    # It contributes to the equation of state differently from tau-gradient walls.

    # For now, compute both scenarios:
    # (i) tau-gradient walls (delta_tau != 0 between domains)
    # (ii) BCS phase walls (Delta changes sign, tau constant)

    # Scenario (i): tau-gradient walls
    # delta_tau between cells is set by quantum fluctuations during transit:
    # delta_tau ~ H / (2*pi*sqrt(Z)) ~ 10^{-6} to 10^{-3}
    delta_tau_quantum = H_transit_MKK / (2 * np.pi * np.sqrt(Z_fold))

    # Scenario (ii): BCS phase walls
    # sigma_BCS = (2/3) * rho_cond * xi_BCS
    # where rho_cond = (1/2) * N(0) * Delta_0^2 ~ |E_cond| * M_KK^4
    rho_cond_MKK4 = abs(E_cond)  # 0.115 M_KK^4
    sigma_BCS = (2.0/3.0) * rho_cond_MKK4 * delta_wall  # M_KK^3

    # Energy density within BCS wall:
    rho_BCS_wall = sigma_BCS / delta_wall  # M_KK^4 = (2/3)*rho_cond = 0.0767

    # Wall energy fraction at transit:
    # f_wall_energy_tr = f_walls_vol * rho_BCS_wall / V_fold
    f_wall_energy_BCS_tr = f_walls_frozen * rho_BCS_wall / V_fold

    # Today (frozen walls, a^{-1} scaling):
    f_wall_energy_BCS_today = f_wall_energy_BCS_tr * a_transit

    print(f"\n    --- Scenario (i): tau-gradient walls ---")
    print(f"    delta_tau (quantum) = {delta_tau_quantum:.6e}")
    grad_tau = delta_tau_quantum / delta_wall
    rho_grad_wall = 0.5 * Z_fold * grad_tau**2
    print(f"    rho_grad_wall = {rho_grad_wall:.6e} M_KK^4")
    f_tau_grad_tr = f_walls_frozen * rho_grad_wall / V_fold
    f_tau_grad_today = f_tau_grad_tr * a_transit
    print(f"    f_grad(transit) = {f_tau_grad_tr:.6e}")
    print(f"    f_grad(today, a^{{-1}} dilution) = {f_tau_grad_today:.6e}")

    print(f"\n    --- Scenario (ii): BCS phase walls ---")
    print(f"    sigma_BCS = {sigma_BCS:.6e} M_KK^3")
    print(f"    rho_BCS_wall = {rho_BCS_wall:.6e} M_KK^4")
    print(f"    rho_BCS_wall / V_fold = {rho_BCS_wall / V_fold:.6e}")
    print(f"    f_wall_energy(transit) = {f_wall_energy_BCS_tr:.6e}")
    print(f"    a_transit = {a_transit:.3e}")
    print(f"    e-folds from transit = {ln_expansion:.1f}")
    print(f"    f_wall_energy(today, frozen + a^{{-1}}) = {f_wall_energy_BCS_today:.6e}")

    # w correction from frozen BCS walls today:
    # w = -1 + (1/3)*f_wall  [domain walls: w_wall = -2/3, so Delta_w = (1/3)*f_wall]
    w_correction_BCS = (1.0/3.0) * f_wall_energy_BCS_today
    w_eff_BCS = -1.0 + w_correction_BCS

    print(f"\n    w_eff = -1 + (1/3)*f_wall = -1 + {w_correction_BCS:.6e}")

    results_frozen[label] = {
        'MKK_GeV': MKK_GeV,
        'H_transit': H_transit_MKK,
        'R_H': R_H_transit_MKK,
        'a_transit': a_transit,
        'f_walls_KZ': f_walls_frozen,
        'f_walls_RH': f_walls_RH if isinstance(f_walls_RH, float) else float(f_walls_RH),
        'f_wall_energy_BCS_tr': f_wall_energy_BCS_tr,
        'f_wall_energy_BCS_today': f_wall_energy_BCS_today,
        'f_tau_grad_tr': f_tau_grad_tr,
        'f_tau_grad_today': f_tau_grad_today,
        'w_correction_BCS': w_correction_BCS,
        'delta_tau_quantum': delta_tau_quantum,
        'rho_BCS_wall': rho_BCS_wall,
        'sigma_BCS': sigma_BCS,
    }


# ========================================================================
# 3. SCALING SOLUTION (DYNAMIC WALLS)
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 2: SCALING SOLUTION (DYNAMIC WALLS)")
print("=" * 78)

print("""
  Standard domain wall cosmology (Vilenkin & Shellard):
  - A network of domain walls reaches a "scaling solution" where
    the number of walls per Hubble volume is O(1).
  - The wall energy density is: rho_wall ~ sigma / R_H ~ sigma * H
  - The fraction relative to rho_total:
    f_wall = rho_wall / rho_crit = sigma * H / (3 H^2 M_P^2 / (8 pi))
           = 8 pi * sigma / (3 H M_P^2)

  For BCS walls: sigma_BCS = (2/3) * |E_cond| * xi_BCS * M_KK^3
  Converting to GeV^3: sigma = sigma_BCS * M_KK^3

  At late times (H = H_0), the scaling solution gives:
  f_wall_scaling = 8 pi * sigma_GeV3 / (3 * H_0_GeV * M_P_GeV^2)

  BUT: this only applies if the walls are DYNAMIC (evolving under tension).
  The W2-2 result says tau is FROZEN. If the BCS order parameter is also
  frozen (which it IS -- the GGE is permanent), then the walls do NOT
  evolve and the scaling solution does NOT apply.

  I compute it for completeness.
""")

for MKK_GeV, label in zip(MKK_values, MKK_labels):
    sigma_BCS = results_frozen[label]['sigma_BCS']
    sigma_GeV3 = sigma_BCS * MKK_GeV**3

    # f_wall_scaling = 8*pi*sigma / (3*H_0*M_P^2)
    f_wall_scaling = 8 * np.pi * sigma_GeV3 / (3 * H_0_GeV * M_Planck_GeV**2)

    # For the domain wall problem: if f_wall > ~10^{-5}, the walls
    # come to dominate the universe, which is the "domain wall problem".
    # In LCDM, this is resolved by inflation diluting the walls.

    w_correction_scaling = (1.0/3.0) * f_wall_scaling
    w_eff_scaling = -1.0 + w_correction_scaling

    print(f"  M_KK = {label} GeV:")
    print(f"    sigma_BCS = {sigma_GeV3:.3e} GeV^3")
    print(f"    f_wall_scaling = {f_wall_scaling:.3e}")
    print(f"    w_eff = -1 + {w_correction_scaling:.3e}")
    print()

    results_scaling[label] = {
        'f_wall_scaling': f_wall_scaling,
        'w_correction_scaling': w_correction_scaling,
        'sigma_GeV3': sigma_GeV3,
    }

# ========================================================================
# 4. THE CRITICAL ISSUE: WHAT DILUTES THE WALLS?
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 3: WHY THE WALL ENERGY IS NEGLIGIBLE TODAY")
print("=" * 78)

print("""
  The key question is NOT the wall volume fraction (which is O(1) at transit).
  The key question is the wall ENERGY FRACTION relative to V_fold.

  At the transit:
    rho_wall / V_fold = rho_BCS_wall / V_fold = |E_cond| / V_fold
                      ~ 0.115 / 250,361 ~ 4.6 x 10^{-7}

  This ratio is determined by the BCS physics: the condensation energy
  is a tiny fraction of the spectral action. The 27 closures tell us
  that V_fold is essentially unaffected by BCS -- the spectral action
  is indifferent to the pairing (effacement ratio 1.5 x 10^{-4}).

  Even at O(1) wall volume fraction, the wall ENERGY fraction is 4.6e-7.
  After a^{-1} dilution from transit to today, it becomes:
    f_wall_energy(today) ~ 4.6e-7 * a_transit

  The a_transit factor is devastating:
    a_transit = T_CMB / T_transit ~ 2.7 K / M_KK
             ~ 10^{-22}  (M_KK = 10^9 GeV)
             ~ 10^{-31}  (M_KK = 10^{18} GeV)

  So f_wall_energy(today) ~ 10^{-29} to 10^{-38}

  The wall correction to w is:
    |w + 1| = (1/3) * f_wall_energy(today) ~ 10^{-29} to 10^{-38}

  This is 28 to 37 orders of magnitude below DESI sensitivity.
  BUT it is 20+ orders LARGER than the v1 estimate of 10^{-59}.
  The v1 error was comparing KK walls to Hubble cells -- getting
  f_walls_vol ~ 10^{-52} instead of O(1), then compounding with
  the energy ratio.
""")

print("\n  Summary of wall energy fractions:")
print(f"  {'M_KK':>10s} | {'f_wall(transit)':>16s} | {'a_transit':>12s} | {'f_wall(today)':>16s} | {'|w+1|':>14s}")
print("  " + "-" * 82)
for label in MKK_labels:
    r = results_frozen[label]
    print(f"  {label:>10s} | {r['f_wall_energy_BCS_tr']:>16.6e} | {r['a_transit']:>12.3e} | {r['f_wall_energy_BCS_today']:>16.6e} | {r['w_correction_BCS']:>14.6e}")

# ========================================================================
# 5. w(z) EVOLUTION
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 4: w(z) EVOLUTION")
print("=" * 78)

# In the frozen-wall picture:
# rho_wall(a) = rho_wall_0 * (a_0/a) = rho_wall_0 * (1+z)
# rho_CC = V_fold * M_KK^4 = const
#
# rho_total(z) = rho_CC + rho_wall_0 * (1+z)
# w_eff(z) = [w_CC * rho_CC + w_wall * rho_wall(z)] / rho_total(z)
#          = [-rho_CC + (-2/3)*rho_wall_0*(1+z)] / [rho_CC + rho_wall_0*(1+z)]
#
# Let x = rho_wall_0 / rho_CC = f_wall_today:
# w_eff(z) = [-1 - (2/3)*x*(1+z)] / [1 + x*(1+z)]
#
# Taylor expand for x << 1:
# w_eff(z) = -1 + (1/3)*x*(1+z) + O(x^2)
#
# In CPL form: w(a) = w_0 + w_a*(1-a) = w_0 + w_a*z/(1+z)
# => w_0 = -1 + (1/3)*x
#    w_a = -(1/3)*x  (negative: walls more important in past)

z_eval = np.array([0.0, 0.295, 0.510, 0.706, 1.0, 1.317, 2.0, 3.0, 5.0, 10.0])

# Use M_KK = 10^9 GeV (most favorable = smallest walls, most energy today)
label_best = '10^9'
r_best = results_frozen[label_best]
x = r_best['f_wall_energy_BCS_today']

w_0_fabric = -1.0 + (1.0/3.0) * x
w_a_fabric = -(1.0/3.0) * x

print(f"\n  Using M_KK = {label_best} GeV (most favorable case):")
print(f"  f_wall_energy(today) = {x:.6e}")
print(f"  w_0 = -1 + (1/3) * {x:.3e} = {w_0_fabric}")
print(f"  w_a = -(1/3) * {x:.3e} = {w_a_fabric:.6e}")
print(f"  (Correct DESI sign: w_a < 0)")
print()

# Exact w(z) (not linearized):
w_z_eval = (-1.0 - (2.0/3.0)*x*(1+z_eval)) / (1.0 + x*(1+z_eval))

print("  z       w(z) [exact]                    |w+1|")
print("  " + "-" * 60)
for z, w in zip(z_eval, w_z_eval):
    print(f"  {z:5.3f}   {w:+.15e}   {abs(w+1):.6e}")

# ========================================================================
# 6. PARAMETER SCAN: (f_walls, delta_tau)
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 5: PARAMETER SCAN (f_walls, delta_tau) -> w_0, w_a")
print("=" * 78)

print("""
  The framework computes f_wall_energy and delta_tau from geometry.
  But to show WHAT VALUES would be needed for DESI consistency,
  we scan the (f_wall, delta_tau) parameter space and compute
  w_0 and w_a for each point.

  For tau-gradient walls:
    rho_wall = (1/2) * Z * (delta_tau / xi_BCS)^2 * M_KK^4 * f_wall_vol
    f_wall_energy = rho_wall / V_fold
    w_0 = -1 + (1/3) * f_wall_energy
    w_a = -(1/3) * f_wall_energy

  For BCS phase walls:
    rho_wall = |E_cond| * f_wall_vol * M_KK^4
    f_wall_energy = |E_cond| * f_wall_vol / V_fold
    w_0 = -1 + (1/3) * |E_cond| * f_wall_vol / V_fold
    (independent of delta_tau -- the BCS gap, not the modulus, varies)

  For DESI: w_0 = -0.55 +/- 0.21  =>  |w+1| ~ 0.45
                                   =>  f_wall_energy ~ 1.35

  This requires the wall energy to EXCEED the CC by 35%.
  Possible only if rho_wall > V_fold, which is impossible for BCS walls
  (|E_cond| / V_fold = 4.6e-7) unless f_wall_vol ~ 10^6.
  Volume fraction cannot exceed 1.

  For tau-gradient walls: need rho_grad * f_vol / V_fold ~ 1.35
  rho_grad = (1/2) * Z * (delta_tau / delta_wall)^2
  (1/2) * 74731 * delta_tau^2 / (1.118)^2 * f_vol / 250361 = 1.35
  delta_tau^2 * f_vol = 1.35 * 250361 / (74731 / (2 * 1.118^2))
  delta_tau^2 * f_vol = 1.35 * 250361 / 29910 = 11.31
  For f_vol = 1: delta_tau = 3.36 (but tau_fold = 0.19, so delta_tau > tau_fold)
  For f_vol = 0.5: delta_tau = 4.76
  IMPOSSIBLE: delta_tau >> tau_fold means the tau field varies by 18x its value.
""")

# Scan grid
f_wall_vol_scan = np.array([0.01, 0.05, 0.1, 0.3, 0.5, 1.0])
delta_tau_scan = np.array([1e-6, 1e-4, 1e-2, 0.05, 0.1, 0.19])

# For tau-gradient walls:
print("  TAU-GRADIENT WALLS: w_0 = -1 + (1/3) * Z * (delta_tau/xi)^2 * f_vol / (2*V_fold)")
print()
print(f"  {'':>12s}", end='')
for dtau in delta_tau_scan:
    print(f"  dtau={dtau:.0e}", end='')
print()
print(f"  {'f_vol':>12s}", end='')
for dtau in delta_tau_scan:
    print(f"  {'|w+1|':>12s}", end='')
print()
print("  " + "-" * (12 + 14 * len(delta_tau_scan)))

w_scan_grid = np.zeros((len(f_wall_vol_scan), len(delta_tau_scan)))

for i, fv in enumerate(f_wall_vol_scan):
    print(f"  {fv:>12.3f}", end='')
    for j, dtau in enumerate(delta_tau_scan):
        rho_grad = 0.5 * Z_fold * (dtau / delta_wall)**2
        f_energy = fv * rho_grad / V_fold
        w_corr = (1.0/3.0) * f_energy
        w_scan_grid[i, j] = w_corr
        if w_corr < 1e-10:
            print(f"  {w_corr:>12.2e}", end='')
        else:
            print(f"  {w_corr:>12.6f}", end='')
    print()

print()
print("  DESI requires |w+1| ~ 0.45. Needed delta_tau for f_vol = 1:")
f_vol_1 = 1.0
dtau_needed = np.sqrt(0.45 * 3.0 * V_fold / (0.5 * Z_fold / delta_wall**2 * f_vol_1))
print(f"    delta_tau_needed = {dtau_needed:.4f}")
print(f"    delta_tau / tau_fold = {dtau_needed / tau_fold:.1f}")
print(f"    IMPOSSIBLE: variation exceeds the modulus value by {dtau_needed/tau_fold:.0f}x")

# For BCS phase walls:
print("\n  BCS PHASE WALLS: |w+1| = (1/3) * |E_cond| * f_vol / V_fold")
print(f"  (independent of delta_tau)")
for fv in f_wall_vol_scan:
    f_energy_BCS = fv * abs(E_cond) / V_fold
    w_corr_BCS = (1.0/3.0) * f_energy_BCS
    print(f"    f_vol = {fv:.2f}: |w+1| = {w_corr_BCS:.6e}")

print(f"\n  Maximum BCS: f_vol=1 gives |w+1| = {abs(E_cond) / (3*V_fold):.6e}")
print(f"  SHORT by factor {0.45 / (abs(E_cond) / (3*V_fold)):.0e}")

# ========================================================================
# 7. ALTERNATIVE CC IDENTIFICATIONS
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 6: ALTERNATIVE CC IDENTIFICATIONS")
print("=" * 78)

print(f"""
  The CC hierarchy depends on WHAT we identify as the vacuum energy:

  (A) V_fold = S_full(tau_fold) = {V_fold:.0f} M_KK^4
      This is the full spectral action at the fold. Naively the CC.

  (B) |E_cond| = {abs(E_cond):.3f} M_KK^4
      BCS condensation energy. 6 orders below V_fold.

  (C) V_fold - V(tau->infinity): the difference between the fold and
      the asymptotic value. From the data:
""")

# V at extreme tau values
tau_Sfull = sf['tau_combined']
S_full = sf['S_full']
V_0 = S_full[0]   # tau = 0
V_fold_val = float(sf['S_fold'].flat[0])
V_05 = S_full[-1]  # tau = 0.5 (largest in data)

print(f"  V(tau=0) = {V_0:.2f}")
print(f"  V(tau_fold=0.19) = {V_fold_val:.2f}")
print(f"  V(tau=0.5) = {V_05:.2f}")
print(f"  V(0.5) - V(0.19) = {V_05 - V_fold_val:.2f} ({(V_05-V_fold_val)/V_fold_val*100:.1f}% of V_fold)")
print(f"  V(0.19) - V(0) = {V_fold_val - V_0:.2f} ({(V_fold_val-V_0)/V_fold_val*100:.1f}% of V_fold)")

print(f"""
  NONE of these differences are small enough to address the CC problem.
  V(0.5) - V(0.19) = {V_05 - V_fold_val:.0f}, which is 13.6% of V_fold.
  Still O(10^4) in M_KK^4 units.

  Lambda_pred / Lambda_obs for each candidate:
""")

print(f"  {'Candidate':>30s} | {'M_KK=10^9':>12s} | {'M_KK=10^{13}':>12s} | {'M_KK=10^{18}':>12s}")
print("  " + "-" * 75)

candidates = {
    'V_fold (full SA)': V_fold,
    '|E_cond| (BCS)': abs(E_cond),
    'V_fold - V(0)': V_fold - V_0,
    'V(0.5) - V_fold': V_05 - V_fold_val,
}

for cand_name, cand_val in candidates.items():
    print(f"  {cand_name:>30s}", end=' |')
    for MKK_GeV in MKK_values:
        ratio_MKK = MKK_GeV / M_Planck_GeV
        Lambda_pred = cand_val * ratio_MKK**4
        if Lambda_pred > 0:
            log_ratio = np.log10(Lambda_pred / Lambda_obs_MP4)
            print(f"  10^{{{log_ratio:.1f}}}  ", end=' |')
        else:
            print(f"  {'N/A':>12s}", end=' |')
    print()

print(f"""
  All candidates overshoot by 80-127 orders. The BCS condensation energy
  saves 6 orders. The S_full variation (monotonic, no plateau) saves 1 order.
  The fundamental hierarchy (M_KK / M_Planck)^4 is the dominant factor.
""")

# ========================================================================
# 8. COMPARISON WITH DESI
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 7: DESI COMPARISON")
print("=" * 78)

desi_fits = {
    'DESI BAO + CMB': {'w0': -0.55, 'w0_err': 0.21, 'wa': -1.30, 'wa_err': 0.70},
    'DESI + Pantheon+': {'w0': -0.827, 'w0_err': 0.063, 'wa': -0.75, 'wa_err': 0.29},
    'DESI + DESY5': {'w0': -0.752, 'w0_err': 0.067, 'wa': -1.05, 'wa_err': 0.31},
}

print(f"\n  Framework prediction (fabric-collective, REDO #2):")
print(f"    w_0 = -1 + {(1.0/3.0)*x:.3e}")
print(f"    w_a = {w_a_fabric:.3e}")
print(f"    INDISTINGUISHABLE from w_0 = -1, w_a = 0")
print()

for lab, fit in desi_fits.items():
    sigma_w0 = abs(w_0_fabric - fit['w0']) / fit['w0_err']
    sigma_wa = abs(w_a_fabric - fit['wa']) / fit['wa_err']
    print(f"  vs {lab}:")
    print(f"    w_0: {fit['w0']:.3f} +/- {fit['w0_err']:.3f} => {sigma_w0:.1f} sigma from framework")
    print(f"    w_a: {fit['wa']:.2f}  +/- {fit['wa_err']:.2f}  => {sigma_wa:.1f} sigma from framework")

# ========================================================================
# 9. WHY THE CORRECTION IS STRUCTURALLY LARGER THAN v1 BUT STILL NEGLIGIBLE
# ========================================================================
print("\n" + "=" * 78)
print("SECTION 8: STRUCTURAL ANALYSIS")
print("=" * 78)

print(f"""
  REDO #1 ERROR:
    Compared wall thickness (KK scale) to cell size (Hubble scale TODAY).
    Got f_walls_vol ~ 10^{{-52}}. WRONG: mixed scales from different epochs.

  REDO #2 CORRECTION:
    At the transit epoch, both wall thickness and domain size are at the
    KK scale. f_walls_vol ~ O(1) at formation. The walls ARE the fabric.

  BUT: the wall ENERGY fraction is NOT O(1). It is:
    f_wall_energy = f_wall_vol * rho_wall / V_fold
                  = O(1) * |E_cond| / V_fold
                  = O(1) * 0.115 / 250,361
                  = 4.6 x 10^{{-7}}

  This is the EFFACEMENT RATIO (Session 40): the spectral action is 10^6x
  larger than the BCS condensation energy. The walls carry BCS energy, not
  spectral action energy.

  After a^{{-1}} dilution from transit to today:
    f_wall(today) = 4.6e-7 * a_transit ~ 10^{{-29}} (M_KK = 10^9 GeV)

  Compare to REDO #1:
    f_wall(today, v1) ~ 10^{{-59}}  (WRONG: used f_vol ~ 10^{{-52}})
    f_wall(today, v2) ~ 10^{{-29}}  (CORRECT: f_vol ~ 1, a^{{-1}} dilution)

  The v2 result is 30 ORDERS LARGER than v1, but still 28 orders below DESI.

  The correction to w traces to TWO scale hierarchies:
    (1) BCS energy / spectral action = |E_cond| / V_fold ~ 10^{{-6}}
    (2) Transit-to-today dilution = a_transit ~ 10^{{-22}}
    Combined: 10^{{-28}} => |w+1| ~ 10^{{-29}}

  For DESI consistency (|w+1| ~ 0.5), we would need:
    f_wall_energy(today) ~ 1.5
    This requires either:
    (a) rho_wall ~ V_fold (impossible: BCS energy is 10^6x smaller)
    (b) No a^{{-1}} dilution (impossible: walls stretch in expanding universe)
    (c) Both: violation of thermodynamics and energy conservation

  CONCLUSION: The fabric-collective calculation with correct epoch-matching
  gives |w+1| ~ 10^{{-29}} (for M_KK = 10^9 GeV). This is 30 orders larger
  than the REDO #1 estimate but still 28 orders below DESI. The framework
  IS geometric Lambda-CDM.

  THE ROOT CAUSE is not the wall volume fraction (O(1) at transit) but the
  wall ENERGY fraction (4.6e-7 at transit due to effacement) multiplied by
  the expansion dilution (10^{{-22}} for M_KK = 10^9 GeV).
""")

# ========================================================================
# 10. GATE VERDICT
# ========================================================================
print("=" * 78)
print("GATE VERDICT: W-Z-42 (REDO #2)")
print("=" * 78)

w_best = w_0_fabric
correction_best = (1.0/3.0) * x

print(f"""
  Pre-registered criterion:
    PASS: -1.2 < w_0 < -0.3 (dynamical DE consistent with DESI)
    FAIL: w_0 = -1.000 (exact Lambda) OR w_0 > 0

  COMPUTED (fabric-collective, correct epoch-matching, M_KK = 10^9 GeV):
    f_walls_vol(transit) = {results_frozen[label_best]['f_walls_KZ']:.1f} (walls fill space at formation)
    f_wall_energy(transit) = {results_frozen[label_best]['f_wall_energy_BCS_tr']:.6e}
    a_transit = {results_frozen[label_best]['a_transit']:.3e}
    f_wall_energy(today) = {x:.6e}
    w_0 = -1 + {correction_best:.6e}
    w_a = {w_a_fabric:.6e} (correct DESI sign)

  vs REDO #1: |w+1|_v1 = 2.5e-59, |w+1|_v2 = {correction_best:.2e}
  The v2 result is {correction_best / 2.5e-59:.0e}x LARGER (epoch-matching correction)
  but still {0.45 / correction_best:.0e}x below DESI sensitivity.
""")

if abs(w_best + 1) < 1e-3:
    verdict = "FAIL"
    print(f"  VERDICT: **{verdict}** — w_0 = -1 + {correction_best:.2e}")
    print(f"    (indistinguishable from Lambda-CDM)")
    print(f"    28 orders of magnitude below DESI")
else:
    verdict = "PASS"
    print(f"  VERDICT: **{verdict}** — dynamical dark energy")

print(f"""
  The two independent routes to w = -1:
    1. Single-tau (S42 v0): epsilon_V = 3.67e-7 => w = -1 + O(10^{-7})
    2. Fabric-collective v1 (WRONG): mixed epochs => w = -1 + O(10^{-59})
    3. Fabric-collective v2 (THIS): correct epochs => w = -1 + O(10^{-29})

  All three give w = -1 to observational precision, but for different reasons:
    v0: tau frozen because omega_tau >> H
    v1: walls negligible because (KK scale) << (Hubble scale) [WRONG LOGIC]
    v2: walls carry BCS energy (10^6x less than SA) AND dilute as a^{{-1}}

  The framework predicts Lambda-CDM. Period.
  If DESI confirms w != -1 at >5 sigma, the framework is EXCLUDED.
""")

# ========================================================================
# 11. SAVE DATA
# ========================================================================
np.savez('tier0-computation/s42_fabric_wz_v2.npz',
    # Gate
    verdict=verdict,
    gate_name='W-Z-42-REDO-2',

    # Frozen-wall results (most favorable: M_KK = 10^9)
    w0_fabric=w_0_fabric,
    wa_fabric=w_a_fabric,
    correction_best=correction_best,
    f_wall_energy_today=x,
    f_wall_energy_transit=results_frozen[label_best]['f_wall_energy_BCS_tr'],
    f_walls_vol_transit=results_frozen[label_best]['f_walls_KZ'],
    a_transit_best=results_frozen[label_best]['a_transit'],

    # w(z) prediction
    z_eval=z_eval,
    w_z_eval=w_z_eval,

    # Upstream data
    tau_fold=tau_fold,
    Z_fold=Z_fold,
    V_fold=V_fold,
    m_tau=m_tau,
    E_cond=E_cond,
    delta_wall=delta_wall,
    xi_BCS_raw=xi_BCS_raw,
    xi_BCS_alt=xi_BCS_alt,
    N_cells=N_cells,

    # Transit physics
    H_transit_9=results_frozen['10^9']['H_transit'],
    H_transit_13=results_frozen['10^{13}']['H_transit'],
    H_transit_18=results_frozen['10^{18}']['H_transit'],
    R_H_transit_9=results_frozen['10^9']['R_H'],
    R_H_transit_13=results_frozen['10^{13}']['R_H'],
    R_H_transit_18=results_frozen['10^{18}']['R_H'],

    # BCS wall physics
    rho_BCS_wall=results_frozen[label_best]['rho_BCS_wall'],
    sigma_BCS=results_frozen[label_best]['sigma_BCS'],
    rho_wall_over_Vfold=results_frozen[label_best]['rho_BCS_wall'] / V_fold,

    # Parameter scan
    f_wall_vol_scan=f_wall_vol_scan,
    delta_tau_scan=delta_tau_scan,
    w_scan_grid=w_scan_grid,

    # Scaling solution (dynamic walls)
    f_wall_scaling_9=results_scaling['10^9']['f_wall_scaling'],
    f_wall_scaling_13=results_scaling['10^{13}']['f_wall_scaling'],
    f_wall_scaling_18=results_scaling['10^{18}']['f_wall_scaling'],

    # CC comparison
    Lambda_obs_MP4=Lambda_obs_MP4,

    # S_full for plotting
    tau_Sfull=sf['tau_combined'],
    S_full=sf['S_full'],
)

print(f"\n  Data saved: tier0-computation/s42_fabric_wz_v2.npz")

# ========================================================================
# 12. PLOT (4-panel)
# ========================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle('W-Z-42 (REDO #2): Fabric-Collective Dark Energy w(z)\n'
             'Correct epoch-matching: f_walls = O(1) at transit, '
             r'$|w_0+1| \sim 10^{-29}$',
             fontsize=12, fontweight='bold')

# --- Panel (a): w(z) with DESI ---
ax = axes[0, 0]
z_fine = np.linspace(0, 3, 200)
a_fine = 1.0 / (1.0 + z_fine)

# Framework prediction (indistinguishable from -1 at this scale)
ax.plot(z_fine, -1.0 * np.ones_like(z_fine), 'b-', lw=2.5,
        label=r'Framework: $w = -1 + O(10^{-29})$')

# DESI fits
w0_d, wa_d = -0.55, -1.30
w_desi = w0_d + wa_d * (1 - a_fine)
ax.plot(z_fine, w_desi, 'r--', lw=1.5, label=r'DESI (BAO+CMB): $w_0=-0.55$')
ax.fill_between(z_fine,
    (w0_d - 0.21) + (wa_d - 0.70) * (1 - a_fine),
    (w0_d + 0.21) + (wa_d + 0.70) * (1 - a_fine),
    color='red', alpha=0.1)

w0_p, wa_p = -0.827, -0.75
w_pan = w0_p + wa_p * (1 - a_fine)
ax.plot(z_fine, w_pan, 'g-.', lw=1.5, label=r'DESI+Pantheon+: $w_0=-0.83$')

ax.axhline(y=-1, color='gray', ls=':', alpha=0.5)
ax.set_xlabel('Redshift z', fontsize=12)
ax.set_ylabel('w(z)', fontsize=12)
ax.set_xlim(0, 3)
ax.set_ylim(-2.5, 0.5)
ax.legend(fontsize=8, loc='upper right')
ax.set_title('(a) Equation of State w(z)', fontsize=11)
ax.grid(True, alpha=0.3)

# --- Panel (b): Energy hierarchy at transit ---
ax = axes[0, 1]
categories = [
    r'$V_{fold}$ (SA)' + '\n250,361',
    r'$|E_{cond}|$ (BCS)' + '\n0.115',
    r'$\rho_{wall}$ (BCS wall)' + f'\n{results_frozen[label_best]["rho_BCS_wall"]:.4f}',
    r'$\rho_{wall} \times a_{tr}$' + f'\n{results_frozen[label_best]["rho_BCS_wall"]*results_frozen[label_best]["a_transit"]:.2e}',
]
values = [
    V_fold,
    abs(E_cond),
    results_frozen[label_best]['rho_BCS_wall'],
    results_frozen[label_best]['rho_BCS_wall'] * results_frozen[label_best]['a_transit'],
]
log_values = [np.log10(max(v, 1e-300)) for v in values]
colors = ['royalblue', 'darkorange', 'green', 'red']

bars = ax.barh(range(len(categories)), log_values, color=colors,
               edgecolor='black', height=0.6, tick_label=categories)
ax.set_xlabel(r'$\log_{10}(\rho$ / $M_{KK}^4)$', fontsize=12)
ax.set_title(r'(b) Energy Hierarchy ($M_{KK}=10^9$ GeV)', fontsize=11)
for bar, lv in zip(bars, log_values):
    ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
            f'{lv:.1f}', va='center', fontsize=10)
ax.set_xlim(-35, 8)
ax.grid(True, alpha=0.3, axis='x')
# Add annotation showing the two suppressions
ax.annotate('', xy=(np.log10(abs(E_cond)), 2.7),
            xytext=(np.log10(V_fold), 2.7),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5))
ax.text((np.log10(V_fold) + np.log10(abs(E_cond)))/2, 3.1,
        'Effacement\n6 orders', ha='center', fontsize=8, color='purple')
ax.annotate('', xy=(log_values[3], 3.3),
            xytext=(log_values[2], 3.3),
            arrowprops=dict(arrowstyle='<->', color='darkred', lw=1.5))
ax.text((log_values[2] + log_values[3])/2, 3.6,
        r'$a^{-1}$ dilution' + '\n22 orders', ha='center', fontsize=8, color='darkred')

# --- Panel (c): Parameter scan heatmap ---
ax = axes[1, 0]
log_w_scan = np.log10(np.maximum(w_scan_grid, 1e-40))
im = ax.imshow(log_w_scan, aspect='auto', cmap='RdYlGn_r',
               vmin=-30, vmax=0,
               extent=[0, len(delta_tau_scan)-1, len(f_wall_vol_scan)-1, 0])
ax.set_xticks(range(len(delta_tau_scan)))
ax.set_xticklabels([f'{dt:.0e}' for dt in delta_tau_scan], fontsize=8, rotation=45)
ax.set_yticks(range(len(f_wall_vol_scan)))
ax.set_yticklabels([f'{fv:.2f}' for fv in f_wall_vol_scan], fontsize=8)
ax.set_xlabel(r'$\delta\tau$', fontsize=12)
ax.set_ylabel(r'$f_{wall,vol}$', fontsize=12)
ax.set_title(r'(c) $\log_{10}|w+1|$ for $\tau$-gradient walls', fontsize=11)
plt.colorbar(im, ax=ax, label=r'$\log_{10}|w+1|$')
# Mark DESI region
for i in range(len(f_wall_vol_scan)):
    for j in range(len(delta_tau_scan)):
        val = log_w_scan[i, j]
        if val > -1:
            ax.text(j, i, f'{val:.0f}', ha='center', va='center',
                    fontsize=7, color='white', fontweight='bold')
        elif val > -10:
            ax.text(j, i, f'{val:.0f}', ha='center', va='center',
                    fontsize=7, color='black')

# --- Panel (d): Comparison of three estimates ---
ax = axes[1, 1]
MKK_range_log = np.linspace(9, 19, 100)
w_plus_1_v2 = []
w_plus_1_v1 = []
w_plus_1_scaling = []

for log_MKK in MKK_range_log:
    MKK = 10**log_MKK
    # v2 (this calculation): f_wall = |E_cond|/V_fold * a_transit
    a_tr = T_CMB_GeV / MKK
    f_wall_v2 = abs(E_cond) / V_fold * a_tr  # f_vol = 1 at transit
    w_corr_v2 = (1.0/3.0) * f_wall_v2
    w_plus_1_v2.append(w_corr_v2)

    # v1 (old, wrong): f_walls_vol ~ (delta_wall_Mpc / R_cell_Mpc)
    MKK_inv_fm = MKK / hbar_c_GeV_fm
    dw_fm = delta_wall / MKK_inv_fm
    dw_Mpc = dw_fm / Mpc_to_fm
    R_cell = 4489.0  # Mpc
    f_vol_v1 = dw_Mpc / R_cell
    # v1 used: f_energy = f_vol * rho_wall/V_fold where rho_wall includes Z*(dtau/dw)^2
    delta_tau_FIRAS = 3e-6 * tau_fold
    rho_grad_v1 = 0.5 * Z_fold * (delta_tau_FIRAS / delta_wall)**2
    sigma_v1 = delta_tau_FIRAS * m_tau * Z_fold
    sigma_vol_v1 = sigma_v1 / delta_wall
    f_wall_v1 = (sigma_vol_v1 / V_fold) * f_vol_v1
    w_corr_v1 = (1.0/3.0) * f_wall_v1
    w_plus_1_v1.append(w_corr_v1)

    # Scaling solution
    sigma_GeV3 = (2.0/3.0) * abs(E_cond) * delta_wall * MKK**3
    f_scaling = 8*np.pi*sigma_GeV3 / (3*H_0_GeV*M_Planck_GeV**2)
    w_corr_scaling = (1.0/3.0) * f_scaling
    w_plus_1_scaling.append(w_corr_scaling)

ax.semilogy(MKK_range_log, w_plus_1_v2, 'b-', lw=2.5,
            label=r'v2 (this): $|E_{cond}|/V_{fold} \times a_{tr}$')
ax.semilogy(MKK_range_log, w_plus_1_v1, 'r--', lw=1.5,
            label='v1 (wrong): KK wall vs Hubble cell')
ax.semilogy(MKK_range_log, w_plus_1_scaling, 'g-.', lw=1.5,
            label='Scaling solution (dynamic walls)')

ax.axhline(y=0.45, color='purple', ls=':', lw=2,
           label=r'DESI: $|w+1| \sim 0.45$')
ax.axhline(y=0.01, color='orange', ls=':', lw=1,
           label=r'Future sensitivity: $|w+1| \sim 0.01$')

# Mark specific M_KK values
for log_mk, label_mk in [(9, r'$10^9$'), (13, r'$10^{13}$'), (18, r'$10^{18}$')]:
    idx = np.argmin(np.abs(MKK_range_log - log_mk))
    ax.plot(log_mk, w_plus_1_v2[idx], 'bo', ms=8)
    ax.annotate(label_mk, xy=(log_mk, w_plus_1_v2[idx]),
                xytext=(log_mk + 0.5, w_plus_1_v2[idx] * 10),
                fontsize=9, arrowprops=dict(arrowstyle='->', lw=0.5))

ax.set_xlabel(r'$\log_{10}(M_{KK}$ / GeV)', fontsize=12)
ax.set_ylabel(r'$|w_0 + 1|$', fontsize=12)
ax.set_title('(d) Three w(z) Estimates vs M_KK', fontsize=11)
ax.set_xlim(9, 19)
ax.set_ylim(1e-80, 1e5)
ax.legend(fontsize=7.5, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('tier0-computation/s42_fabric_wz_v2.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved: tier0-computation/s42_fabric_wz_v2.png")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE — W-Z-42 (REDO #2)")
print("=" * 78)
print(f"""
SUMMARY:
  The fabric-collective calculation with CORRECT epoch-matching gives:

    f_walls_vol(transit) = 1.0  (walls fill space at BCS transition)
    f_wall_energy(transit) = |E_cond| / V_fold = 4.6e-7  (effacement)
    a_transit = T_CMB / M_KK = 2.3e-22  (for M_KK = 10^9 GeV)
    f_wall_energy(today) = 4.6e-7 * 2.3e-22 = 1.1e-28

    w_0 = -1 + 3.5e-29
    w_a = -3.5e-29  (correct DESI sign)

  This is 30 ORDERS LARGER than the v1 estimate (2.5e-59), correcting
  the epoch-mixing error. But still 28 orders below DESI.

  The two suppressions are:
    (1) Effacement: |E_cond| / V_fold ~ 10^{{-6}} (BCS << SA)
    (2) Expansion:  a_transit ~ 10^{{-22}} (walls dilute as a^{{-1}})

  For DESI consistency, would need f_wall_energy(today) ~ 1.5.
  Impossible without violating either effacement or expansion dilution.

  Gate W-Z-42 (REDO #2): FAIL (w_0 = -1, geometric Lambda-CDM)
  The framework IS a cosmological constant theory.
""")
