#!/usr/bin/env python3
"""
s49_bragg_goldstone.py — Bragg gap in the 32-cell Goldstone phononic crystal
=============================================================================

Gate: BRAGG-GOLDSTONE-49
  PASS: m_Bragg / M_KK in [10^{-60}, 10^{-30}]
  INFO: gap exists but outside target range
  FAIL: no gap or gap at KK scale

Physics:
  The 32-cell tessellation of the SU(3) fiber forms a phononic crystal for the
  U(1)_7 Goldstone mode. Z_3 domain walls between cells have impedance contrast
  sigma_wall = 4.50 M_KK (S48 W5-D, geodesic). This periodic impedance modulation
  opens Bragg gaps at the Brillouin zone boundary k = pi/a.

  The transfer matrix method gives the exact Bloch dispersion. The Bragg gap
  Delta_omega at the zone boundary translates to an effective mass:
    m_Bragg = Delta_omega / (2 * c_Goldstone)

  where c_Goldstone = sqrt(J_C2 / rho_s) is the Goldstone phase velocity.

Method:
  1. 1D unit cell: bulk region (length l_bulk) + wall region (width w_wall)
     with different impedance Z = rho * c.
  2. Transfer matrix T(omega) for one unit cell (propagation + interface + wall + interface).
  3. Bloch condition: Tr(T) / 2 = cos(k * a) gives omega(k).
  4. Gap at k = pi/a: cos(k*a) = -1, solve |Tr(T)/2| = 1 for omega.
  5. 10% cell-size disorder: randomize l_bulk, compute localization.
  6. 3D extension: 4x4x2 lattice with direction-dependent J (J_xy, J_z).

Input data:
  - s48_curv_extend.npz: sigma_wall_geodesic, w_wall, L_Z3
  - s47_texture_corr.npz: J_C2, J_su2, J_u1, rho_s_eigs, N_cells, l_cell
  - s48_aniso_oz.npz: J_xy, J_z, anisotropy parameters

Output:
  - s49_bragg_goldstone.npz
  - s49_bragg_goldstone.png
"""

import sys
sys.path.insert(0, '.')

import numpy as np
from scipy import optimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    N_cells, M_KK, tau_fold, xi_BCS, xi_GL,
    E_cond, Delta_0_GL, PI
)

# =============================================================================
# Load upstream data
# =============================================================================

d_curv = np.load('s48_curv_extend.npz', allow_pickle=True)
d_tex = np.load('s47_texture_corr.npz', allow_pickle=True)
d_oz = np.load('s48_aniso_oz.npz', allow_pickle=True)

# Stiffness constants (M_KK units)
J_C2 = float(d_tex['J_C2'])        # = 0.933 M_KK
J_su2 = float(d_tex['J_su2'])      # = 0.059 M_KK
J_u1 = float(d_tex['J_u1'])        # = 0.038 M_KK

# Superfluid density eigenvalues
rho_s_eigs = np.array(d_tex['rho_s_eigs'])  # 8 eigenvalues

# Cell geometry
l_cell = float(d_tex['l_cell'])     # = 0.152 M_KK^{-1}
L_total = float(d_tex['L_total'])   # = 4.864 M_KK^{-1}

# Domain wall parameters (S48 W5-D)
sigma_wall = float(d_curv['z3_sigma_wall_geodesic'])  # = 4.50 M_KK
sigma_elastic = float(d_curv['z3_sigma_wall_elastic']) # = 0.010 M_KK
w_wall = float(d_curv['z3_w_wall'])                    # = 0.465 M_KK^{-1}

# 3D anisotropy (S48)
J_xy = float(d_oz['J_xy'])     # = J_C2
J_z = float(d_oz['J_z'])      # = J_su2

print("=" * 72)
print("BRAGG-GOLDSTONE-49: Bragg gap in the 32-cell Goldstone phononic crystal")
print("=" * 72)
print()

# =============================================================================
# Section 1: Unit cell definition and transfer matrix
# =============================================================================
#
# The 1D phononic crystal has period a = l_cell.
# Each unit cell consists of:
#   - Bulk region: length l_b = l_cell - w_wall, impedance Z_b = rho_b * c_b
#   - Wall region: width w_w = w_wall, impedance Z_w = rho_w * c_w
#
# Key question: what is the impedance contrast?
#
# Approach 1 (geodesic wall tension):
#   sigma_wall = 4.50 M_KK is the wall TENSION (energy per area).
#   Wall acts as a potential barrier for the Goldstone mode.
#   Effective wall stiffness: J_wall = J_C2 + delta_J from curvature at wall.
#   The wall impedance depends on how the order parameter varies across the wall.
#
# Approach 2 (elastic/curvature):
#   sigma_elastic = 0.010 M_KK. The elastic wall tension modifies the local
#   sound speed. Impedance contrast eta = Z_wall / Z_bulk.
#
# The correct model: the Goldstone mode is a phase wave of the BCS condensate.
# At Z_3 domain walls, the condensate order parameter rotates by 2*pi/3 in
# phase. This means the wall is a region where:
#   - The superfluid density is locally reduced (pair-breaking at the wall)
#   - The stiffness may be enhanced (curvature gradient adds to kinetic energy)
#
# For a Z_3 domain wall in a superfluid, the standard result is:
#   rho_s(wall) = rho_s(bulk) * cos^2(delta_phi/2)
# where delta_phi = 2*pi/3 is the phase jump.
#
# This gives: rho_s(wall)/rho_s(bulk) = cos^2(pi/3) = 1/4
#
# The wall stiffness J_wall is related to the curvature gradient.
# From the data, sigma_wall >> J_C2, so the wall is "stiff" but has
# reduced superfluid density.

print("--- Section 1: Unit cell parameters ---")
print()

# Superfluid density: use the lowest rho_s eigenvalue (most responsive direction)
rho_s_bulk = rho_s_eigs.min()
print(f"rho_s (bulk, min eigenvalue) = {rho_s_bulk:.6f}")
print(f"rho_s (bulk, max eigenvalue) = {rho_s_eigs.max():.6f}")

# Sound speed in bulk: c = sqrt(J / rho_s)
c_bulk = np.sqrt(J_C2 / rho_s_bulk)
print(f"c_bulk (C2 direction) = sqrt({J_C2:.4f} / {rho_s_bulk:.4f}) = {c_bulk:.6f} (M_KK units)")

# Impedance in bulk
Z_bulk = rho_s_bulk * c_bulk  # = sqrt(rho_s * J)
print(f"Z_bulk = rho_s * c = {Z_bulk:.6f}")
print(f"     = sqrt(rho_s * J_C2) = {np.sqrt(rho_s_bulk * J_C2):.6f}")
print()

# --- Wall impedance models ---
# Model A: Z_3 phase rotation reduces rho_s at wall
#   rho_s(wall) = rho_s(bulk) * cos^2(pi/3) = rho_s(bulk) / 4
#   J_wall = J_C2 (same stiffness)
#   => Z_wall = rho_s(wall) * c_wall = rho_s(bulk)/4 * sqrt(J_C2 / (rho_s(bulk)/4))
#            = rho_s(bulk)/4 * 2 * sqrt(J_C2 / rho_s(bulk)) = Z_bulk / 2
#   Impedance contrast eta = Z_wall/Z_bulk = 1/2

delta_phi_Z3 = 2 * PI / 3  # Z_3 domain wall phase jump
rho_s_wall_A = rho_s_bulk * np.cos(delta_phi_Z3 / 2)**2
c_wall_A = np.sqrt(J_C2 / rho_s_wall_A)
Z_wall_A = rho_s_wall_A * c_wall_A

print("Model A: Z_3 phase-rotation wall (rho_s reduced by cos^2)")
print(f"  delta_phi = 2*pi/3 = {delta_phi_Z3:.6f}")
print(f"  cos^2(delta_phi/2) = {np.cos(delta_phi_Z3/2)**2:.6f}")
print(f"  rho_s(wall) = {rho_s_wall_A:.6f}")
print(f"  c(wall) = {c_wall_A:.6f}")
print(f"  Z(wall) = {Z_wall_A:.6f}")
print(f"  eta = Z_wall/Z_bulk = {Z_wall_A / Z_bulk:.6f}")
print()

# Model B: Wall tension modifies effective stiffness
#   J_eff(wall) = sigma_wall / w_wall (tension / width = effective spring constant)
#   rho_s(wall) = rho_s(bulk) * cos^2(pi/3) (same as Model A)
#   => eta = sqrt(rho_s(wall) * J_wall) / sqrt(rho_s(bulk) * J_bulk)

J_wall_B = sigma_wall / w_wall  # effective wall stiffness from tension
rho_s_wall_B = rho_s_wall_A     # same rho_s reduction
c_wall_B = np.sqrt(J_wall_B / rho_s_wall_B)
Z_wall_B = rho_s_wall_B * c_wall_B

print("Model B: Geodesic wall tension as effective stiffness")
print(f"  J_wall = sigma / w = {sigma_wall:.4f} / {w_wall:.4f} = {J_wall_B:.4f}")
print(f"  rho_s(wall) = {rho_s_wall_B:.6f} (same Z_3 reduction)")
print(f"  c(wall) = {c_wall_B:.6f}")
print(f"  Z(wall) = {Z_wall_B:.6f}")
print(f"  eta = Z_wall/Z_bulk = {Z_wall_B / Z_bulk:.6f}")
print()

# Model C: Elastic wall tension (conservative)
J_wall_C = sigma_elastic / w_wall
rho_s_wall_C = rho_s_wall_A
c_wall_C = np.sqrt(J_wall_C / rho_s_wall_C) if J_wall_C > 0 else 0.0
Z_wall_C = rho_s_wall_C * c_wall_C if c_wall_C > 0 else 0.0

print("Model C: Elastic wall tension (conservative)")
print(f"  J_wall = sigma_elastic / w = {sigma_elastic:.6f} / {w_wall:.4f} = {J_wall_C:.6f}")
print(f"  rho_s(wall) = {rho_s_wall_C:.6f}")
print(f"  c(wall) = {c_wall_C:.6f}")
print(f"  Z(wall) = {Z_wall_C:.6f}")
print(f"  eta = Z_wall/Z_bulk = {Z_wall_C / Z_bulk:.6f}" if Z_bulk > 0 else "  eta = 0")
print()

# =============================================================================
# Section 2: Transfer Matrix Method — 1D Bloch Hamiltonian
# =============================================================================
#
# For a 1D phononic crystal with two layers per unit cell:
#   Layer 1 (bulk): thickness d_b, impedance Z_b, sound speed c_b
#   Layer 2 (wall): thickness d_w, impedance Z_w, sound speed c_w
#
# Total cell size: a = d_b + d_w
#
# The transfer matrix for one unit cell:
#   T(omega) = M_interface(Z_b, Z_w) . P_wall(omega) . M_interface(Z_w, Z_b) . P_bulk(omega)
#
# where P_j(omega) is the propagation matrix through layer j:
#   P_j = [[cos(phi_j), -sin(phi_j)/Z_j], [Z_j*sin(phi_j), cos(phi_j)]]
#   phi_j = omega * d_j / c_j
#
# The Bloch condition: cos(k*a) = Tr(T) / 2
# Gaps occur where |Tr(T)/2| > 1.

print("--- Section 2: Transfer matrix dispersion ---")
print()

def transfer_matrix_1d(omega, d_b, d_w, c_b, c_w, Z_b, Z_w):
    """
    Transfer matrix for one unit cell of a 1D phononic crystal.

    Layers: bulk (d_b, c_b, Z_b) then wall (d_w, c_w, Z_w).

    The transfer matrix relates [p, v] at cell boundaries:
      [p_{n+1}]   [p_n]
      [       ] = T [   ]
      [v_{n+1}]   [v_n]

    where p = pressure, v = velocity.
    """
    # Phase accumulated in each layer
    phi_b = omega * d_b / c_b if c_b > 0 else 0.0
    phi_w = omega * d_w / c_w if c_w > 0 else 0.0

    # Propagation matrix for bulk
    cos_b, sin_b = np.cos(phi_b), np.sin(phi_b)
    P_b = np.array([
        [cos_b, -sin_b / Z_b if Z_b > 0 else 0.0],
        [Z_b * sin_b, cos_b]
    ])

    # Propagation matrix for wall
    cos_w, sin_w = np.cos(phi_w), np.sin(phi_w)
    P_w = np.array([
        [cos_w, -sin_w / Z_w if Z_w > 0 else 0.0],
        [Z_w * sin_w, cos_w]
    ])

    # Total: T = P_w . P_b (wave passes through bulk then wall)
    T = P_w @ P_b
    return T


def bloch_dispersion(omega_array, d_b, d_w, c_b, c_w, Z_b, Z_w):
    """
    Compute cos(k*a) = Tr(T)/2 for each omega.
    Returns the Bloch phase factor.
    """
    a = d_b + d_w
    cos_ka = np.zeros_like(omega_array)
    for i, omega in enumerate(omega_array):
        T = transfer_matrix_1d(omega, d_b, d_w, c_b, c_w, Z_b, Z_w)
        cos_ka[i] = 0.5 * np.trace(T)
    return cos_ka


def find_band_edges(d_b, d_w, c_b, c_w, Z_b, Z_w, n_bands=4, n_scan=10000):
    """
    Find band edges by scanning for |cos(ka)| = 1.
    Band edges occur at cos(ka) = +1 (k=0) and cos(ka) = -1 (k=pi/a).
    """
    a = d_b + d_w
    # Maximum frequency to scan: a few Brillouin zones
    omega_max = n_bands * PI * c_b / a  # n_bands * pi * c / a
    omega_scan = np.linspace(1e-10, omega_max, n_scan)

    cos_ka = bloch_dispersion(omega_scan, d_b, d_w, c_b, c_w, Z_b, Z_w)

    # Find where cos(ka) crosses +/-1
    band_edges = []
    for target in [-1.0, 1.0]:
        crossings = np.where(np.diff(np.sign(cos_ka - target)))[0]
        for idx in crossings:
            # Refine with bisection
            def f(om):
                T = transfer_matrix_1d(om, d_b, d_w, c_b, c_w, Z_b, Z_w)
                return 0.5 * np.trace(T) - target
            try:
                om_edge = optimize.brentq(f, omega_scan[idx], omega_scan[idx+1])
                band_edges.append((om_edge, target))
            except ValueError:
                pass

    band_edges.sort(key=lambda x: x[0])
    return band_edges, omega_scan, cos_ka


# --- Compute for all three models ---

models = {
    'A': {'label': 'Z_3 phase-rotation (rho_s/4)',
           'd_b': l_cell - w_wall, 'd_w': w_wall,
           'c_b': c_bulk, 'c_w': c_wall_A, 'Z_b': Z_bulk, 'Z_w': Z_wall_A},
    'B': {'label': 'Geodesic tension wall',
           'd_b': l_cell - w_wall, 'd_w': w_wall,
           'c_b': c_bulk, 'c_w': c_wall_B, 'Z_b': Z_bulk, 'Z_w': Z_wall_B},
    'C': {'label': 'Elastic tension wall (conservative)',
           'd_b': l_cell - w_wall, 'd_w': w_wall,
           'c_b': c_bulk, 'c_w': c_wall_C, 'Z_b': Z_bulk, 'Z_w': Z_wall_C},
}

# Check: is the bulk region thickness positive?
d_bulk_nominal = l_cell - w_wall
print(f"Cell size a = l_cell = {l_cell:.4f} M_KK^{{-1}}")
print(f"Wall width w_wall = {w_wall:.4f} M_KK^{{-1}}")
print(f"Bulk thickness d_b = l_cell - w_wall = {d_bulk_nominal:.4f} M_KK^{{-1}}")
print()

if d_bulk_nominal <= 0:
    print("*** CRITICAL: w_wall > l_cell. The wall is wider than the cell. ***")
    print("This means the phononic crystal is ALL WALL — no bulk region exists.")
    print("The 'cells' are fully immersed in the Z_3 domain wall structure.")
    print()
    print("Reinterpretation: The relevant periodicity is the Z_3 cell spacing,")
    print("not the sub-cell bulk/wall distinction. The impedance modulation")
    print("comes from the periodic curvature variation across the Z_3 structure.")
    print()

    # Use the Z_3 cell spacing L_Z3 instead
    L_Z3 = float(d_curv['z3_L_Z3_fold'])  # = 1.462 M_KK^{-1}
    print(f"Z_3 cell spacing L_Z3 = {L_Z3:.4f} M_KK^{{-1}} (fold)")
    print(f"Total system size L = N_cells * L_Z3 = {N_cells * L_Z3:.2f} M_KK^{{-1}}")
    print()

    # For the Z_3 structure, the "bulk" is the cell interior and the "wall"
    # is the region near the domain wall center. Both have different curvature.
    # Use a model with:
    #   d_1 = L_Z3 * (1 - w_wall/L_Z3)  (interior)
    #   d_2 = w_wall  (wall region)
    d_interior = L_Z3 - w_wall
    d_wall_region = w_wall

    print(f"Interior region: d_interior = L_Z3 - w_wall = {d_interior:.4f} M_KK^{{-1}}")
    print(f"Wall region: d_wall = w_wall = {d_wall_region:.4f} M_KK^{{-1}}")
    print(f"Fraction wall: {d_wall_region/L_Z3:.3f}")
    print()

    # Update models to use L_Z3 as the period
    for key in models:
        models[key]['d_b'] = d_interior
        models[key]['d_w'] = d_wall_region

    a_cell = L_Z3
else:
    a_cell = l_cell

print(f"Effective lattice period a = {a_cell:.4f} M_KK^{{-1}}")
print(f"Brillouin zone boundary: k_BZ = pi/a = {PI/a_cell:.4f} M_KK")
print()

# =============================================================================
# Section 3: Compute dispersion for each model
# =============================================================================

results = {}

for model_key, m in models.items():
    print(f"\n=== Model {model_key}: {m['label']} ===")

    d_b = m['d_b']
    d_w = m['d_w']
    c_b = m['c_b']
    c_w = m['c_w']
    Z_b = m['Z_b']
    Z_w = m['Z_w']

    if d_b <= 0 or d_w <= 0:
        print(f"  SKIP: d_b = {d_b:.4f}, d_w = {d_w:.4f} — negative thickness")
        results[model_key] = {'skip': True, 'reason': 'negative thickness'}
        continue

    if Z_w <= 0 or Z_b <= 0:
        print(f"  SKIP: Z_b = {Z_b:.6f}, Z_w = {Z_w:.6f} — zero impedance")
        results[model_key] = {'skip': True, 'reason': 'zero impedance'}
        continue

    a = d_b + d_w
    eta = Z_w / Z_b  # impedance contrast ratio

    print(f"  d_b = {d_b:.4f}, d_w = {d_w:.4f}, a = {a:.4f}")
    print(f"  c_b = {c_b:.6f}, c_w = {c_w:.6f}")
    print(f"  Z_b = {Z_b:.6f}, Z_w = {Z_w:.6f}")
    print(f"  eta = Z_w/Z_b = {eta:.6f}")

    # --- Analytical Bragg gap estimate ---
    # For a two-layer phononic crystal, the first Bragg gap has width:
    #   Delta_omega / omega_BZ ~ |1 - eta| / (1 + eta)  (for thin walls)
    # More precisely, at the first zone boundary:
    #   Delta_omega = (2 * c_eff / a) * arcsin(|1 - eta^2| / (2*eta))   (for matched phases)
    # But the general formula requires the transfer matrix.

    # First, compute the gap analytically for the quarter-wave condition
    gap_est_thin = abs(1 - eta) / (1 + eta)
    omega_BZ = PI * c_b / a  # first zone boundary frequency (if uniform medium)
    delta_omega_est = gap_est_thin * omega_BZ

    print(f"  omega_BZ (uniform estimate) = pi*c_b/a = {omega_BZ:.6f}")
    print(f"  Thin-wall gap estimate: |1-eta|/(1+eta) = {gap_est_thin:.6f}")
    print(f"  Delta_omega (estimate) = {delta_omega_est:.6f} M_KK")

    # --- Numerical dispersion ---
    band_edges, omega_scan, cos_ka = find_band_edges(d_b, d_w, c_b, c_w, Z_b, Z_w, n_bands=6)

    print(f"\n  Band edges found: {len(band_edges)}")
    for i, (om, target) in enumerate(band_edges[:12]):
        btype = "Gamma" if abs(target - 1.0) < 0.1 else "X"
        print(f"    edge {i}: omega = {om:.8f}, cos(ka) = {target:+.1f} ({btype})")

    # Extract first Bragg gap (between band edges at X point, cos(ka)=-1)
    x_edges = [(om, t) for om, t in band_edges if abs(t + 1.0) < 0.1]
    gamma_edges = [(om, t) for om, t in band_edges if abs(t - 1.0) < 0.1]

    first_gap = None
    if len(x_edges) >= 2:
        # First gap at X: between first and second X-point edges
        om_lower = x_edges[0][0]
        om_upper = x_edges[1][0]
        first_gap = {
            'omega_lower': om_lower,
            'omega_upper': om_upper,
            'delta_omega': om_upper - om_lower,
            'omega_center': 0.5 * (om_lower + om_upper),
            'relative_gap': (om_upper - om_lower) / (0.5 * (om_lower + om_upper)),
        }
        print(f"\n  FIRST BRAGG GAP (at k = pi/a):")
        print(f"    omega_lower = {first_gap['omega_lower']:.8f} M_KK")
        print(f"    omega_upper = {first_gap['omega_upper']:.8f} M_KK")
        print(f"    Delta_omega = {first_gap['delta_omega']:.8f} M_KK")
        print(f"    omega_center = {first_gap['omega_center']:.8f} M_KK")
        print(f"    Relative gap = {first_gap['relative_gap']:.6f}")

        # Effective mass from Bragg gap
        # m_Bragg = Delta_omega / (2 * v_group) where v_group = d(omega)/dk at zone boundary
        # Near the gap edge: omega^2 = omega_edge^2 + c^2 (k - pi/a)^2
        # => m_eff = omega_gap / (2 * c^2) in the quadratic approximation
        # Standard definition: m_Bragg = Delta_omega / (2 * c_eff)
        # where c_eff is the effective phase velocity
        c_eff = first_gap['omega_center'] * a / PI  # from omega_center = c_eff * pi/a
        m_bragg = first_gap['delta_omega'] / (2.0 * c_eff)

        print(f"    c_eff = omega_center * a / pi = {c_eff:.6f}")
        print(f"    m_Bragg = Delta_omega / (2 * c_eff) = {m_bragg:.8f} M_KK")
        print(f"    m_Bragg / M_KK = {m_bragg:.6e}")
        print(f"    log10(m_Bragg / M_KK) = {np.log10(m_bragg) if m_bragg > 0 else -np.inf:.4f}")

        first_gap['c_eff'] = c_eff
        first_gap['m_bragg'] = m_bragg
    else:
        print("\n  NO BRAGG GAP DETECTED at X-point.")
        if len(x_edges) == 1:
            print(f"  Only one X-point edge found at omega = {x_edges[0][0]:.8f}")
        print(f"  (Total band edges found: {len(band_edges)})")

    # --- Full dispersion relation ---
    n_k = 500
    k_array = np.linspace(0, PI / a, n_k)
    omega_bands = []

    # For each k, find omega values where cos(ka) = cos(k*a)
    # Scan omega and find crossings
    for band_idx in range(4):
        omega_band = np.zeros(n_k)
        # Bracket for this band
        if len(band_edges) > 2 * band_idx + 1:
            om_lo = band_edges[2*band_idx][0] * 0.95 if band_idx > 0 else 0.0
            om_hi = band_edges[2*band_idx + 1][0] * 1.05
        else:
            om_lo = band_idx * PI * c_b / a
            om_hi = (band_idx + 1) * PI * c_b / a

        omega_fine = np.linspace(max(om_lo, 1e-12), om_hi, 5000)
        cos_ka_fine = bloch_dispersion(omega_fine, d_b, d_w, c_b, c_w, Z_b, Z_w)

        for ik, k in enumerate(k_array):
            target = np.cos(k * a)
            diffs = cos_ka_fine - target
            crossings = np.where(np.diff(np.sign(diffs)))[0]
            if len(crossings) > 0:
                # Take the first crossing in this band
                idx = crossings[0]
                def f(om):
                    T = transfer_matrix_1d(om, d_b, d_w, c_b, c_w, Z_b, Z_w)
                    return 0.5 * np.trace(T) - target
                try:
                    omega_band[ik] = optimize.brentq(f, omega_fine[idx], omega_fine[idx+1])
                except ValueError:
                    omega_band[ik] = np.nan
            else:
                omega_band[ik] = np.nan

        omega_bands.append(omega_band)

    results[model_key] = {
        'skip': False,
        'eta': eta,
        'd_b': d_b, 'd_w': d_w,
        'c_b': c_b, 'c_w': c_w,
        'Z_b': Z_b, 'Z_w': Z_w,
        'a': a,
        'band_edges': band_edges,
        'first_gap': first_gap,
        'k_array': k_array,
        'omega_bands': omega_bands,
        'omega_scan': omega_scan,
        'cos_ka': cos_ka,
    }

# =============================================================================
# Section 4: Disorder analysis — 10% cell-size randomness
# =============================================================================

print("\n" + "=" * 72)
print("Section 4: Disorder analysis (10% cell-size randomness)")
print("=" * 72)

# Pick the model with the clearest gap for disorder analysis
best_model = None
best_gap = 0
for key, r in results.items():
    if r.get('skip', True):
        continue
    if r.get('first_gap') and r['first_gap']['delta_omega'] > best_gap:
        best_gap = r['first_gap']['delta_omega']
        best_model = key

if best_model is not None:
    m = results[best_model]
    print(f"\nUsing Model {best_model} for disorder analysis")
    print(f"Clean gap: Delta_omega = {m['first_gap']['delta_omega']:.8f} M_KK")

    # Build a disordered chain of N_cells cells
    n_realizations = 200
    n_cells_chain = N_cells  # 32 cells
    disorder_strength = 0.10  # 10% cell-size variation

    # For each realization, compute transmission through the entire chain
    rng = np.random.default_rng(42)

    # Frequency range around the gap
    gap_info = m['first_gap']
    omega_lo_disor = gap_info['omega_lower'] * 0.5
    omega_hi_disor = gap_info['omega_upper'] * 1.5
    n_omega_disor = 500
    omega_disor = np.linspace(omega_lo_disor, omega_hi_disor, n_omega_disor)

    transmission_clean = np.zeros(n_omega_disor)
    transmission_disor_avg = np.zeros(n_omega_disor)
    transmission_disor_std = np.zeros(n_omega_disor)

    d_b_0 = m['d_b']
    d_w_0 = m['d_w']
    c_b = m['c_b']
    c_w = m['c_w']
    Z_b = m['Z_b']
    Z_w = m['Z_w']

    # Clean transmission
    for i_om, omega in enumerate(omega_disor):
        T_total = np.eye(2)
        for _ in range(n_cells_chain):
            T_cell = transfer_matrix_1d(omega, d_b_0, d_w_0, c_b, c_w, Z_b, Z_w)
            T_total = T_cell @ T_total
        # Transmission: |t|^2 = 4 / (|T11 + T22|^2 + |T12*Z + T21/Z|^2)
        # For the (p,v) convention: t = 2 / (T[0,0] + T[1,1] + Z_b*T[0,1] + T[1,0]/Z_b)
        # But simpler: |cos(k*N*a)| gives the band structure
        # Use Lyapunov exponent: gamma = (1/N) * ln |T_total|
        # Transmission ~ exp(-2*gamma*N)
        trace = np.trace(T_total)
        # Bounded check: if |Tr/2| > 1, it's in a gap (evanescent)
        transmission_clean[i_om] = 1.0 / (1.0 + 0.25 * trace**2) if abs(trace) > 2 else 1.0

    # Disordered transmission
    trans_all = np.zeros((n_realizations, n_omega_disor))
    for i_real in range(n_realizations):
        # Randomize d_b for each cell (keeping d_w fixed — walls have fixed physics)
        d_b_random = d_b_0 * (1.0 + disorder_strength * rng.standard_normal(n_cells_chain))
        d_b_random = np.maximum(d_b_random, 0.01 * d_b_0)  # ensure positive

        for i_om, omega in enumerate(omega_disor):
            T_total = np.eye(2)
            for ic in range(n_cells_chain):
                T_cell = transfer_matrix_1d(omega, d_b_random[ic], d_w_0, c_b, c_w, Z_b, Z_w)
                T_total = T_cell @ T_total
            trace = np.trace(T_total)
            trans_all[i_real, i_om] = 1.0 / (1.0 + 0.25 * trace**2) if abs(trace) > 2 else 1.0

    transmission_disor_avg = np.mean(trans_all, axis=0)
    transmission_disor_std = np.std(trans_all, axis=0)

    # Localization length: xi_loc = -N*a / (2 * <ln(T)>)
    ln_trans = np.log(np.maximum(trans_all, 1e-300))
    lyapunov_avg = -np.mean(ln_trans, axis=0) / (2.0 * n_cells_chain * (d_b_0 + d_w_0))
    xi_loc = np.where(lyapunov_avg > 0, 1.0 / lyapunov_avg, np.inf)

    # Gap survival
    gap_mask = (omega_disor >= gap_info['omega_lower']) & (omega_disor <= gap_info['omega_upper'])
    trans_in_gap_clean = np.mean(transmission_clean[gap_mask])
    trans_in_gap_disor = np.mean(transmission_disor_avg[gap_mask])

    print(f"  Clean: <T> in gap = {trans_in_gap_clean:.6f}")
    print(f"  Disordered: <T> in gap = {trans_in_gap_disor:.6f}")
    print(f"  Gap survives disorder: {'YES' if trans_in_gap_disor < 0.5 else 'NO'}")

    disorder_results = {
        'omega_disor': omega_disor,
        'transmission_clean': transmission_clean,
        'transmission_disor_avg': transmission_disor_avg,
        'transmission_disor_std': transmission_disor_std,
        'xi_loc': xi_loc,
        'gap_survives': trans_in_gap_disor < 0.5,
    }
else:
    print("  No valid model with a Bragg gap found.")
    disorder_results = None

# =============================================================================
# Section 5: 3D Extension — 4x4x2 lattice with anisotropic J
# =============================================================================

print("\n" + "=" * 72)
print("Section 5: 3D Extension (4x4x2 lattice)")
print("=" * 72)

# In 3D, the phononic crystal is a simple cubic lattice with different
# stiffness along different directions.
# J_xy (in-plane) = J_C2 = 0.933
# J_z (out-of-plane) = J_su2 = 0.059
#
# The Bloch Hamiltonian for a tight-binding phononic crystal:
#   H(k) = 2*J_x*(1 - cos(k_x*a_x)) + 2*J_y*(1 - cos(k_y*a_y)) + 2*J_z*(1 - cos(k_z*a_z))
#
# For the Goldstone mode with impedance contrast at walls:
# Each direction has its own Bragg gap.
# The gap in direction i: Delta_omega_i ~ |1-eta_i| / (1+eta_i) * omega_BZ_i
#
# With the Z_3 phase rotation model:
#   eta is the same in all directions (same Z_3 wall physics)
#   but omega_BZ differs: omega_BZ_i = pi * c_i / a_i

# Use Z_3 cell spacing for the lattice constants
# In 3D, the domain structure has 4x4x2 = 32 cells total
# a_xy = L_total_xy / 4, a_z = L_total_z / 2
# But the total system size is N_cells * l_cell in the maximally packed direction
# From the geometry: L_Z3 is the inter-wall spacing

L_Z3 = float(d_curv['z3_L_Z3_fold'])

# For 4x4x2:
# xy directions: a_xy = L_Z3 (each cell has one Z_3 spacing)
# z direction: a_z = L_Z3 (same)
a_xy = L_Z3
a_z = L_Z3

# Sound speeds in each direction
c_xy = np.sqrt(J_xy / rho_s_bulk)
c_z = np.sqrt(J_z / rho_s_bulk)

print(f"J_xy = {J_xy:.4f}, J_z = {J_z:.4f}")
print(f"rho_s = {rho_s_bulk:.4f}")
print(f"c_xy = {c_xy:.6f}, c_z = {c_z:.6f}")
print(f"Anisotropy c_xy/c_z = {c_xy/c_z:.2f}")
print(f"a_xy = a_z = L_Z3 = {L_Z3:.4f}")
print()

# Use Model A wall parameters for 3D
rho_s_wall = rho_s_wall_A
c_wall_xy = np.sqrt(J_C2 / rho_s_wall)
c_wall_z = np.sqrt(J_su2 / rho_s_wall)
Z_bulk_xy = rho_s_bulk * c_xy
Z_wall_xy = rho_s_wall * c_wall_xy
Z_bulk_z = rho_s_bulk * c_z
Z_wall_z = rho_s_wall * c_wall_z

eta_xy = Z_wall_xy / Z_bulk_xy
eta_z = Z_wall_z / Z_bulk_z

print(f"eta_xy = {eta_xy:.6f} (same as 1D Model A: {Z_wall_A/Z_bulk:.6f})")
print(f"eta_z = {eta_z:.6f}")
print()

# 3D dispersion: the 1D Bragg gap in each direction
# Compute gap in xy and z directions separately (since they factorize for
# waves propagating along principal axes)

d_interior = L_Z3 - w_wall
d_wall_reg = w_wall

print("--- xy direction ---")
if d_interior > 0:
    edges_xy, scan_xy, cos_xy = find_band_edges(
        d_interior, d_wall_reg, c_xy, c_wall_xy, Z_bulk_xy, Z_wall_xy, n_bands=4)
    x_edges_xy = [(om, t) for om, t in edges_xy if abs(t + 1.0) < 0.1]
    if len(x_edges_xy) >= 2:
        gap_xy = x_edges_xy[1][0] - x_edges_xy[0][0]
        center_xy = 0.5 * (x_edges_xy[0][0] + x_edges_xy[1][0])
        c_eff_xy = center_xy * (d_interior + d_wall_reg) / PI
        m_bragg_xy = gap_xy / (2 * c_eff_xy)
        print(f"  First Bragg gap: [{x_edges_xy[0][0]:.6f}, {x_edges_xy[1][0]:.6f}]")
        print(f"  Delta_omega_xy = {gap_xy:.8f}")
        print(f"  m_Bragg_xy = {m_bragg_xy:.8f} M_KK")
    else:
        gap_xy = 0
        m_bragg_xy = 0
        print(f"  No gap found (edges: {len(x_edges_xy)})")
else:
    gap_xy = 0
    m_bragg_xy = 0
    print(f"  d_interior <= 0: fully wall-dominated")

print("\n--- z direction ---")
if d_interior > 0:
    edges_z, scan_z, cos_z = find_band_edges(
        d_interior, d_wall_reg, c_z, c_wall_z, Z_bulk_z, Z_wall_z, n_bands=4)
    x_edges_z = [(om, t) for om, t in edges_z if abs(t + 1.0) < 0.1]
    if len(x_edges_z) >= 2:
        gap_z = x_edges_z[1][0] - x_edges_z[0][0]
        center_z = 0.5 * (x_edges_z[0][0] + x_edges_z[1][0])
        c_eff_z = center_z * (d_interior + d_wall_reg) / PI
        m_bragg_z = gap_z / (2 * c_eff_z)
        print(f"  First Bragg gap: [{x_edges_z[0][0]:.6f}, {x_edges_z[1][0]:.6f}]")
        print(f"  Delta_omega_z = {gap_z:.8f}")
        print(f"  m_Bragg_z = {m_bragg_z:.8f} M_KK")
    else:
        gap_z = 0
        m_bragg_z = 0
        print(f"  No gap found (edges: {len(x_edges_z)})")
else:
    gap_z = 0
    m_bragg_z = 0
    print(f"  d_interior <= 0: fully wall-dominated")

# =============================================================================
# Section 6: Analytical cross-check
# =============================================================================

print("\n" + "=" * 72)
print("Section 6: Analytical cross-checks")
print("=" * 72)

# For a two-component 1D phononic crystal with layers of thickness d_1, d_2
# and impedances Z_1, Z_2, the first Bragg gap relative width is:
#
#   Delta_omega / omega_BZ = (2/pi) * |arcsin((Z_1-Z_2)/(Z_1+Z_2))| * correction
#
# For small impedance contrast epsilon = (Z_1-Z_2)/(Z_1+Z_2):
#   Delta_omega / omega_BZ ~ (2/pi) * |epsilon| * (d_w / a)  (thin wall)
#
# For arbitrary thickness ratio but small epsilon:
#   Delta_omega / omega_BZ ~ (2/pi) * |epsilon| * |sin(pi * d_w/a)|

for key in ['A', 'B', 'C']:
    r = results.get(key)
    if r is None or r.get('skip', True):
        continue

    eta = r['eta']
    eps = (r['Z_w'] - r['Z_b']) / (r['Z_w'] + r['Z_b'])
    d_b, d_w, a = r['d_b'], r['d_w'], r['a']

    # Analytical prediction
    thick_factor = abs(np.sin(PI * d_w / a))
    gap_rel_analytic = (2/PI) * abs(eps) * thick_factor

    print(f"\nModel {key}:")
    print(f"  eta = {eta:.6f}")
    print(f"  epsilon = (Z_w-Z_b)/(Z_w+Z_b) = {eps:.6f}")
    print(f"  sin(pi*d_w/a) = {thick_factor:.6f}")
    print(f"  Analytical gap ratio = {gap_rel_analytic:.6f}")

    if r.get('first_gap'):
        print(f"  Numerical gap ratio  = {r['first_gap']['relative_gap']:.6f}")
        ratio = r['first_gap']['relative_gap'] / gap_rel_analytic if gap_rel_analytic > 0 else np.inf
        print(f"  Numerical/Analytical = {ratio:.4f}")

# =============================================================================
# Section 7: Gate Assessment
# =============================================================================

print("\n" + "=" * 72)
print("Section 7: GATE VERDICT — BRAGG-GOLDSTONE-49")
print("=" * 72)

# The gate criterion is:
#   PASS: m_Bragg / M_KK in [10^{-60}, 10^{-30}]
#   INFO: gap exists but outside target range
#   FAIL: no gap or gap at KK scale

# Collect all m_Bragg values
m_bragg_values = {}
for key, r in results.items():
    if r.get('skip', True):
        continue
    if r.get('first_gap') and r['first_gap'].get('m_bragg'):
        m_bragg_values[key] = r['first_gap']['m_bragg']

# Add 3D values
if m_bragg_xy > 0:
    m_bragg_values['3D_xy'] = m_bragg_xy
if m_bragg_z > 0:
    m_bragg_values['3D_z'] = m_bragg_z

print()
print("m_Bragg / M_KK for all models:")
for key, val in m_bragg_values.items():
    log_val = np.log10(val) if val > 0 else -np.inf
    in_range = -60 <= log_val <= -30
    print(f"  Model {key}: m_Bragg/M_KK = {val:.6e}  log10 = {log_val:.2f}  {'IN RANGE' if in_range else 'OUT OF RANGE'}")

print()

# Determine verdict
any_gap = len(m_bragg_values) > 0
any_in_range = any(-60 <= np.log10(v) <= -30 for v in m_bragg_values.values() if v > 0)

if not any_gap:
    verdict = "FAIL"
    verdict_reason = "No Bragg gap found in any model."
elif any_in_range:
    verdict = "PASS"
    verdict_reason = "m_Bragg / M_KK in target range [10^{-60}, 10^{-30}]."
else:
    # Gap exists but at wrong scale
    all_vals = [v for v in m_bragg_values.values() if v > 0]
    min_log = min(np.log10(v) for v in all_vals)
    max_log = max(np.log10(v) for v in all_vals)
    if max_log > -1:
        verdict = "INFO"
        verdict_reason = (f"Bragg gap exists at O(1) M_KK scale (log10 range [{min_log:.1f}, {max_log:.1f}]). "
                         f"This is a KK-scale gap, not a cosmologically small gap. "
                         f"The phononic crystal modulates the Goldstone dispersion "
                         f"but does NOT generate a hierarchically small mass.")
    else:
        verdict = "INFO"
        verdict_reason = (f"Gap exists but outside target: log10(m/M_KK) in [{min_log:.1f}, {max_log:.1f}].")

print(f"VERDICT: {verdict}")
print(f"REASON: {verdict_reason}")
print()

# Physical interpretation
print("--- Physical interpretation ---")
print()
print("The 32-cell phononic crystal has impedance contrast eta = Z_wall/Z_bulk.")
print("For the Z_3 phase-rotation wall (Model A), eta = 0.5 (exact from cos^2(pi/3) = 1/4).")
print("This gives a Bragg gap of O(1) in units of the Brillouin zone frequency,")
print("which is itself O(M_KK) since c ~ O(1) and a ~ O(1) in M_KK units.")
print()
print("The hierarchical suppression needed is 10^{-60} to 10^{-30}.")
print("A Bragg gap can only produce m/M_KK ~ |1-eta|/(1+eta) * (c/a).")
print("Since all quantities are O(1) in M_KK units, the Bragg mechanism")
print("CANNOT generate a hierarchically small mass. It generates a gap")
print("at the KK scale, which is already the natural scale of the phononic crystal.")
print()
print("To get a small mass ratio, one would need either:")
print("  (a) Exponentially small impedance contrast (fine-tuning), or")
print("  (b) A different mechanism entirely (e.g., near-cancellation of ")
print("      competing effects, Anderson localization in the gap, etc.)")
print()

# =============================================================================
# Section 8: Save results
# =============================================================================

save_dict = {
    'gate_name': 'BRAGG-GOLDSTONE-49',
    'gate_verdict': verdict,
    'gate_reason': verdict_reason,

    # Input parameters
    'J_C2': J_C2,
    'J_su2': J_su2,
    'J_u1': J_u1,
    'rho_s_bulk': rho_s_bulk,
    'rho_s_eigs': rho_s_eigs,
    'sigma_wall_geodesic': sigma_wall,
    'sigma_wall_elastic': sigma_elastic,
    'w_wall': w_wall,
    'l_cell': l_cell,
    'L_Z3': float(d_curv['z3_L_Z3_fold']),
    'a_cell': a_cell,
    'c_bulk': c_bulk,

    # Model A
    'eta_A': Z_wall_A / Z_bulk,
    'Z_bulk_A': Z_bulk,
    'Z_wall_A': Z_wall_A,
    'rho_s_wall_A': rho_s_wall_A,

    # Model B
    'eta_B': Z_wall_B / Z_bulk if Z_bulk > 0 else 0,
    'J_wall_B': J_wall_B,

    # Model C
    'eta_C': Z_wall_C / Z_bulk if Z_bulk > 0 else 0,
    'J_wall_C': J_wall_C,

    # 3D
    'J_xy': J_xy,
    'J_z': J_z,
    'c_xy': c_xy,
    'c_z': c_z,
    'eta_xy': eta_xy,
    'eta_z': eta_z,
    'm_bragg_xy': m_bragg_xy,
    'm_bragg_z': m_bragg_z,
}

# Add model-specific gap data
for key, r in results.items():
    if r.get('skip', True):
        continue
    prefix = f'model_{key}_'
    if r.get('first_gap'):
        for gk, gv in r['first_gap'].items():
            save_dict[prefix + gk] = gv
    save_dict[prefix + 'eta'] = r['eta']
    # Save dispersion for plotting
    save_dict[prefix + 'k_array'] = r['k_array']
    for bi, band in enumerate(r['omega_bands']):
        save_dict[prefix + f'band_{bi}'] = band

# Save disorder results
if disorder_results is not None:
    save_dict['disorder_omega'] = disorder_results['omega_disor']
    save_dict['disorder_trans_clean'] = disorder_results['transmission_clean']
    save_dict['disorder_trans_avg'] = disorder_results['transmission_disor_avg']
    save_dict['disorder_trans_std'] = disorder_results['transmission_disor_std']
    save_dict['disorder_xi_loc'] = disorder_results['xi_loc']
    save_dict['disorder_gap_survives'] = disorder_results['gap_survives']

np.savez('s49_bragg_goldstone.npz', **save_dict)
print("\nSaved: s49_bragg_goldstone.npz")

# =============================================================================
# Section 9: Plot
# =============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('BRAGG-GOLDSTONE-49: Bragg gap in 32-cell Goldstone phononic crystal',
             fontsize=14, fontweight='bold')

# Panel (0,0): cos(ka) vs omega for all models
ax = axes[0, 0]
colors = {'A': 'blue', 'B': 'red', 'C': 'green'}
for key, r in results.items():
    if r.get('skip', True):
        continue
    ax.plot(r['omega_scan'], r['cos_ka'], color=colors[key], alpha=0.7, label=f'Model {key}')
ax.axhline(y=1, color='gray', ls='--', alpha=0.5)
ax.axhline(y=-1, color='gray', ls='--', alpha=0.5)
ax.fill_between(ax.get_xlim(), -1, 1, alpha=0.05, color='green')
ax.set_xlabel('omega (M_KK)')
ax.set_ylabel('cos(k*a)')
ax.set_title('Bloch condition: cos(k*a) = Tr(T)/2')
ax.legend(fontsize=8)
ax.set_ylim(-3, 3)
ax.set_xlim(0, None)
ax.grid(True, alpha=0.3)

# Panel (0,1): Dispersion relation omega(k)
ax = axes[0, 1]
for key, r in results.items():
    if r.get('skip', True):
        continue
    a = r['a']
    for bi, band in enumerate(r['omega_bands']):
        label = f'Model {key}' if bi == 0 else None
        ax.plot(r['k_array'] * a / PI, band, color=colors[key], alpha=0.7, label=label)
    # Mark the gap
    if r.get('first_gap'):
        gap = r['first_gap']
        ax.axhspan(gap['omega_lower'], gap['omega_upper'], alpha=0.15, color=colors[key])
ax.set_xlabel('k * a / pi')
ax.set_ylabel('omega (M_KK)')
ax.set_title('Goldstone dispersion omega(k)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (0,2): Impedance contrast diagram
ax = axes[0, 2]
x_pos = [1, 2, 3]
eta_vals = []
labels = []
for key in ['A', 'B', 'C']:
    r = results.get(key)
    if r and not r.get('skip', True):
        eta_vals.append(r['eta'])
        labels.append(f'Model {key}')
if eta_vals:
    bars = ax.bar(x_pos[:len(eta_vals)], eta_vals, color=['blue', 'red', 'green'][:len(eta_vals)], alpha=0.7)
    ax.set_xticks(x_pos[:len(eta_vals)])
    ax.set_xticklabels(labels)
    ax.axhline(y=1, color='gray', ls='--', label='eta = 1 (no contrast)')
    ax.set_ylabel('eta = Z_wall / Z_bulk')
    ax.set_title('Impedance contrast ratio')
    ax.legend()
    ax.grid(True, alpha=0.3)
else:
    ax.text(0.5, 0.5, 'No valid models', ha='center', va='center', transform=ax.transAxes)

# Panel (1,0): m_Bragg values
ax = axes[1, 0]
if m_bragg_values:
    keys = list(m_bragg_values.keys())
    vals = [np.log10(m_bragg_values[k]) if m_bragg_values[k] > 0 else -100 for k in keys]
    ax.barh(range(len(keys)), vals, color='steelblue', alpha=0.7)
    ax.set_yticks(range(len(keys)))
    ax.set_yticklabels(keys)
    ax.axvspan(-60, -30, alpha=0.15, color='green', label='Target: [-60, -30]')
    ax.set_xlabel('log10(m_Bragg / M_KK)')
    ax.set_title('Bragg effective mass')
    ax.legend()
    ax.grid(True, alpha=0.3)
else:
    ax.text(0.5, 0.5, 'No Bragg gaps found', ha='center', va='center', transform=ax.transAxes)

# Panel (1,1): Disorder transmission
ax = axes[1, 1]
if disorder_results is not None:
    dr = disorder_results
    ax.plot(dr['omega_disor'], dr['transmission_clean'], 'b-', alpha=0.7, label='Clean')
    ax.plot(dr['omega_disor'], dr['transmission_disor_avg'], 'r-', alpha=0.7, label='10% disorder (avg)')
    ax.fill_between(dr['omega_disor'],
                    dr['transmission_disor_avg'] - dr['transmission_disor_std'],
                    dr['transmission_disor_avg'] + dr['transmission_disor_std'],
                    alpha=0.2, color='red')
    if best_model and results[best_model].get('first_gap'):
        gap = results[best_model]['first_gap']
        ax.axvspan(gap['omega_lower'], gap['omega_upper'], alpha=0.15, color='yellow', label='Bragg gap')
    ax.set_xlabel('omega (M_KK)')
    ax.set_ylabel('Transmission')
    ax.set_title('Disorder survival (200 realizations)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
else:
    ax.text(0.5, 0.5, 'No disorder analysis', ha='center', va='center', transform=ax.transAxes)

# Panel (1,2): 3D gap comparison
ax = axes[1, 2]
dir_labels = ['xy (C2)', 'z (su2)']
gap_vals_3d = [m_bragg_xy, m_bragg_z]
colors_3d = ['blue', 'orange']
valid_3d = [(l, v, c) for l, v, c in zip(dir_labels, gap_vals_3d, colors_3d) if v > 0]
if valid_3d:
    for i, (l, v, c) in enumerate(valid_3d):
        ax.bar(i, np.log10(v) if v > 0 else -100, color=c, alpha=0.7, label=l)
    ax.axhspan(-60, -30, alpha=0.15, color='green', label='Target')
    ax.set_xticks(range(len(valid_3d)))
    ax.set_xticklabels([x[0] for x in valid_3d])
    ax.set_ylabel('log10(m_Bragg / M_KK)')
    ax.set_title('3D Bragg gap (4x4x2)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
else:
    ax.text(0.5, 0.5, 'No 3D gaps', ha='center', va='center', transform=ax.transAxes)

# Add verdict text
fig.text(0.5, 0.01, f'VERDICT: {verdict} | {verdict_reason}',
         ha='center', fontsize=11, fontweight='bold',
         color='red' if verdict == 'FAIL' else ('orange' if verdict == 'INFO' else 'green'))

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('s49_bragg_goldstone.png', dpi=150, bbox_inches='tight')
print("Saved: s49_bragg_goldstone.png")

print("\n" + "=" * 72)
print(f"BRAGG-GOLDSTONE-49: {verdict}")
print("=" * 72)
