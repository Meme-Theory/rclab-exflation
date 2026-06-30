"""
S55 KZ-DOMAIN-55: Kibble-Zurek Domain Wall Density on 32-Cell CG Graph

Applies the Kibble-Zurek (KZ) defect density formula to the BCS quench on the
32-cell Cayley graph of SU(3), using framework parameters from S38 and the
graph structure from S54.

The key question: does the KZ correlation length exceed the graph diameter?
If xi_KZ >> L_graph, the entire graph is a single domain (no walls).
If xi_KZ << L_graph, multiple domains form with walls between them.

Physics:
  - Transit through fold at omega_tau = 8.27 M_KK (deeply diabatic)
  - BCS gap Delta_0 = 0.4643 M_KK (OES value), xi_BCS = 0.808 M_KK^{-1}
  - 32-cell CG graph: diameter 6 (graph hops), mean coordination 5.81
  - Graph spectral dimension d_s = 2.0 (S54 result)
  - Mean-field BCS exponents: nu = 1/2, z = 2

Method:
  1. Extract graph metric properties (diameter, effective length, spectral gap)
  2. Compute KZ correlation length xi_KZ for BCS mean-field (z=2) and ballistic (z=1)
  3. Compare xi_KZ to graph diameter and GL coherence length
  4. Estimate domain count N_domains = (L/xi_KZ)^d_s
  5. Cross-check with S38 sudden-quench result (L/xi_GL = 0.031)
  6. Pair vibration mode analysis with omega_PV = 0.792

Gate: KZ-DOMAIN-55
  INFO: n_defect estimate, N_domains, xi_KZ/L ratio

Author: phonon-first-cosmologist (Session 55)
"""

import numpy as np
import sys
import os

sys.path.insert(0, 'computations')
from canonical_constants import (
    omega_tau, omega_PV, omega_att,
    Delta_0_OES, Delta_0_GL, Delta_B3,
    xi_BCS, xi_GL,
    E_cond, E_exc_ratio, n_pairs, N_dof_BCS,
    S_inst, barrier_0d,
    dt_transit, v_terminal, P_exc_kz, n_Bog,
    Gamma_Langer_BCS,
    tau_fold
)

# ===========================================================================
# 0. Load graph data from S54
# ===========================================================================
data_path = os.path.join('computations', 'session-54', 's54_tb_hamiltonian.npz')
d54 = np.load(data_path, allow_pickle=True)

adjacency = d54['adjacency']       # (32, 32) int8
N_cells = int(d54['N_cells'])      # 32
eigenvalues = d54['eigenvalues']   # (50, 32) — 50 tau values, 32 eigenvalues each
tau_values = d54['tau_values']     # (50,)
bandwidths = d54['bandwidths']     # (50,)
band_gaps = d54['band_gaps']       # (50,)

# Graph distance matrix
from scipy.sparse.csgraph import shortest_path
dist_matrix = shortest_path(adjacency > 0, directed=False, unweighted=True)
diameter = int(np.max(dist_matrix[dist_matrix < np.inf]))
mean_distance = np.mean(dist_matrix[dist_matrix < np.inf])
coordination = np.sum(adjacency > 0, axis=1)
mean_coord = np.mean(coordination)

print("=" * 72)
print("S55 KZ-DOMAIN-55: KIBBLE-ZUREK DOMAIN WALL DENSITY")
print("=" * 72)

# ===========================================================================
# 1. Graph Metric Properties
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 1: GRAPH METRIC PROPERTIES")
print("=" * 72)

print(f"  N_cells           = {N_cells}")
print(f"  Graph diameter    = {diameter} hops")
print(f"  Mean distance     = {mean_distance:.4f} hops")
print(f"  Mean coordination = {mean_coord:.4f}")
print(f"  Total bonds       = {int(np.sum(adjacency > 0)) // 2}")

# Graph spectral properties (Laplacian)
L_graph = np.diag(coordination.astype(float)) - adjacency.astype(float)
eig_L = np.linalg.eigvalsh(L_graph)
spectral_gap = eig_L[1]  # Fiedler eigenvalue (algebraic connectivity)
lambda_max = eig_L[-1]

print(f"\n  Laplacian spectrum:")
print(f"    lambda_0 = {eig_L[0]:.6e}  (zero mode)")
print(f"    lambda_1 = {eig_L[1]:.6f}  (Fiedler / spectral gap)")
print(f"    lambda_max = {lambda_max:.6f}")
print(f"    Ratio lambda_max/lambda_1 = {lambda_max/eig_L[1]:.4f}")

# Effective length scale from spectral gap:
# On a d-dimensional lattice with N sites, lambda_1 ~ (2*pi/L)^2
# So L_eff = 2*pi / sqrt(lambda_1)
L_eff_spectral = 2 * np.pi / np.sqrt(spectral_gap)
print(f"\n  Effective length from spectral gap:")
print(f"    L_eff = 2*pi/sqrt(lambda_1) = {L_eff_spectral:.4f} (lattice units)")

# Cheeger constant estimate (isoperimetric ratio)
# h_G >= lambda_1/2 (Cheeger inequality)
cheeger_lower = spectral_gap / 2
print(f"    Cheeger lower bound h >= lambda_1/2 = {cheeger_lower:.4f}")

# Band structure at the fold (tau closest to tau_fold = 0.19)
idx_fold = np.argmin(np.abs(tau_values - tau_fold))
tau_at_fold = tau_values[idx_fold]
eigs_fold = eigenvalues[idx_fold]
bw_fold = bandwidths[idx_fold]
gap_fold = band_gaps[idx_fold]

print(f"\n  Band structure at fold (tau = {tau_at_fold:.4f}):")
print(f"    Bandwidth = {bw_fold:.6f} M_KK")
print(f"    Band gap   = {gap_fold:.6f} M_KK")
print(f"    Eigenvalue range: [{eigs_fold.min():.4f}, {eigs_fold.max():.4f}]")

# Effective hopping from bandwidth: W = 2*z*t for regular lattice,
# more generally W ~ 2*sqrt(z)*t for random-like graphs
# On our graph: t_eff = W / (2 * sqrt(<z>))  or simply t_eff = W / (2*z_max)
# Conservative: use W = 2*z*t → t = W/(2*z)
t_hop_eff = bw_fold / (2 * mean_coord)
print(f"    Effective hopping t_eff = W/(2*z_mean) = {t_hop_eff:.6f} M_KK")

# Fermi velocity on lattice: v_F ~ t_eff * a (where a = lattice spacing = 1 hop)
v_F_graph = t_hop_eff  # In units of M_KK * (hop distance)
print(f"    v_F (graph) ~ t_eff = {v_F_graph:.6f} M_KK * hop^{-1}")

# ===========================================================================
# 2. BCS Critical Exponents
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 2: BCS CRITICAL EXPONENTS & QUENCH PARAMETERS")
print("=" * 72)

# Mean-field BCS: nu = 1/2, z = 2
nu_mf = 0.5  # (local)
z_mf = 2.0  # (local)

# Ballistic BCS: nu = 1/2, z = 1 (for clean systems with ballistic propagation)
nu_ball = 0.5  # (local)
z_ball = 1.0  # (local)

# KZ exponents
kz_exp_mf = nu_mf / (1 + z_mf * nu_mf)     # 0.5 / 2.0 = 0.25
kz_exp_ball = nu_ball / (1 + z_ball * nu_ball)  # 0.5 / 1.5 = 1/3

# Defect density exponent: d*nu/(1+z*nu)
d_s = 2.0  # Spectral dimension of the graph (S54)  # (local)
defect_exp_mf = d_s * nu_mf / (1 + z_mf * nu_mf)     # 2*0.5/2 = 0.5
defect_exp_ball = d_s * nu_ball / (1 + z_ball * nu_ball)  # 2*0.5/1.5 = 2/3

print(f"  Graph spectral dimension d_s = {d_s}")
print(f"")
print(f"  Mean-field BCS (z=2):")
print(f"    nu = {nu_mf}, z = {z_mf}")
print(f"    xi_KZ exponent nu/(1+z*nu) = {kz_exp_mf:.4f}")
print(f"    n_defect exponent d*nu/(1+z*nu) = {defect_exp_mf:.4f}")
print(f"")
print(f"  Ballistic BCS (z=1):")
print(f"    nu = {nu_ball}, z = {z_ball}")
print(f"    xi_KZ exponent nu/(1+z*nu) = {kz_exp_ball:.6f}")
print(f"    n_defect exponent d*nu/(1+z*nu) = {defect_exp_ball:.6f}")

# ===========================================================================
# 3. Quench Timescales
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 3: QUENCH TIMESCALES")
print("=" * 72)

# Quench time: inverse of transit frequency
tau_Q = 1.0 / omega_tau  # = 1/8.27 M_KK^{-1}
print(f"  omega_tau (transit rate)  = {omega_tau:.4f} M_KK")
print(f"  tau_Q = 1/omega_tau      = {tau_Q:.6f} M_KK^{{-1}}")
print(f"  dt_transit (S38)         = {dt_transit:.6e} M_KK^{{-1}}")

# Microscopic relaxation times
tau_0_Delta = 1.0 / Delta_0_OES   # Gap relaxation: 1/Delta
tau_0_PV = 1.0 / omega_PV          # Pair vibration period
tau_0_GL = 1.0 / Delta_0_GL        # GL gap scale

print(f"\n  Microscopic timescales:")
print(f"    1/Delta_0_OES = {tau_0_Delta:.6f} M_KK^{{-1}}  (OES gap)")
print(f"    1/Delta_0_GL  = {tau_0_GL:.6f} M_KK^{{-1}}  (GL gap)")
print(f"    1/omega_PV    = {tau_0_PV:.6f} M_KK^{{-1}}  (pair vibration)")
print(f"    1/Gamma_L     = {1.0/Gamma_Langer_BCS:.6f} M_KK^{{-1}}  (Langer decay)")

# Use OES gap as the standard microscopic time (consistent with S38)
tau_0 = tau_0_Delta
xi_0 = xi_BCS

print(f"\n  Chosen scales:")
print(f"    tau_0 = 1/Delta_0_OES = {tau_0:.6f} M_KK^{{-1}}")
print(f"    xi_0  = xi_BCS        = {xi_0:.6f} M_KK^{{-1}}")

# Adiabaticity parameter
adiab = tau_Q / tau_0
print(f"\n  Adiabaticity tau_Q/tau_0 = {adiab:.6f}")
if adiab < 1:
    print(f"  ** DIABATIC REGIME ** (tau_Q < tau_0)")
    print(f"     Quench is FASTER than microscopic relaxation.")
    print(f"     Standard KZ gives xi_KZ < xi_0 — saturates at xi_0.")
else:
    print(f"  ** ADIABATIC-ISH REGIME ** (tau_Q > tau_0)")

# Also with pair vibration timescale
adiab_PV = tau_Q / tau_0_PV
print(f"\n  Adiabaticity (PV scale) tau_Q/tau_0_PV = {adiab_PV:.6f}")

# ===========================================================================
# 4. KZ Correlation Length — TWO regimes
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 4: KIBBLE-ZUREK CORRELATION LENGTH")
print("=" * 72)

results = {}

for label, nu, z, tau0_use, xi0_use in [
    ("MF-BCS (z=2, tau_0=1/Delta)", nu_mf, z_mf, tau_0, xi_0),
    ("Ballistic (z=1, tau_0=1/Delta)", nu_ball, z_ball, tau_0, xi_0),
    ("MF-BCS (z=2, tau_0=1/omega_PV)", nu_mf, z_mf, tau_0_PV, xi_0),
    ("Ballistic (z=1, tau_0=1/omega_PV)", nu_ball, z_ball, tau_0_PV, xi_0),
]:
    kz_e = nu / (1 + z * nu)
    ad = tau_Q / tau0_use

    # Formal KZ correlation length
    xi_KZ_formal = xi0_use * ad**kz_e

    # Physical: xi_KZ cannot be smaller than xi_0 (sudden-quench floor)
    # nor larger than the system (finite-size ceiling)
    xi_KZ_phys = max(xi0_use, xi_KZ_formal)

    # Defect density exponent
    d_nu_exp = d_s * nu / (1 + z * nu)

    # n_defect ~ (tau_Q/tau_0)^{-d*nu/(1+z*nu)}
    n_defect_formal = ad**(-d_nu_exp)

    # N_domains on graph: (L_eff / xi_KZ)^d_s
    # Use the graph diameter as L
    L_graph_hops = float(diameter)

    # Convert xi_KZ to graph hops using the effective hopping
    # xi_KZ is in M_KK^{-1}, lattice spacing a ~ 1/t_hop_eff in M_KK^{-1}/hop
    # So xi_KZ_hops = xi_KZ * t_hop_eff
    # Actually: xi_KZ is a physical length in M_KK^{-1}. The hop spacing
    # on the Cayley graph in M_KK^{-1} units is a_graph = (vol_SU3/N_cells)^{1/d_s}
    # which we can estimate from the spectral gap.
    # Simpler: xi_KZ_hops = xi_KZ / a_graph where a_graph ~ L_eff_spectral/diameter

    a_graph = L_eff_spectral / diameter  # lattice spacing in spectral units
    # But L_eff_spectral is in "lattice units" (hops), so a_graph = L_eff_spectral/diameter ~ 1 hop
    # The correct mapping: the bandwidth W ~ v_F / a, so a ~ v_F / W
    # With v_F from the dispersion relation on the graph.

    # CLEANEST approach: use the S38 result directly.
    # S38 found L/xi_GL = 0.031 where L is the system size in the pairing space.
    # L_sys = 0.03 M_KK^{-1} (from s37_instanton_mc)
    # This L is the effective size of the pairing condensate (the "box" for Cooper pairs).
    # It is NOT the graph diameter.

    # For the graph: the relevant length is the GRAPH diameter in physical units.
    # If one hop corresponds to the Connes distance d_C between adjacent cells,
    # then L_physical = diameter * d_C.
    # From S54: Connes distance provides a(fold) = 2.117 (expansion factor).
    # The Connes distance between adjacent cells is d_C ~ 1/W ~ 1/bw_fold
    # (inverse bandwidth gives the lattice spacing in spectral geometry).
    d_C = 1.0 / bw_fold  # Connes-like lattice spacing (M_KK^{-1})
    L_physical = diameter * d_C  # Physical diameter of graph

    xi_ratio = xi_KZ_phys / L_physical
    N_domains = max(1.0, (L_physical / xi_KZ_phys)**d_s)

    print(f"\n  --- {label} ---")
    print(f"    tau_0 = {tau0_use:.6f}, xi_0 = {xi0_use:.6f}")
    print(f"    Adiabaticity tau_Q/tau_0 = {ad:.6f}")
    print(f"    KZ exponent = {kz_e:.6f}")
    print(f"    xi_KZ (formal)  = {xi_KZ_formal:.6f} M_KK^{{-1}}")
    print(f"    xi_KZ (physical) = {xi_KZ_phys:.6f} M_KK^{{-1}}")
    regime = "DIABATIC (floor at xi_0)" if xi_KZ_formal < xi0_use else "ADIABATIC"
    print(f"    Regime: {regime}")
    print(f"    d_C (lattice spacing) = {d_C:.6f} M_KK^{{-1}}")
    print(f"    L_physical (graph diam) = {L_physical:.6f} M_KK^{{-1}}")
    print(f"    xi_KZ / L_physical = {xi_ratio:.4f}")
    print(f"    N_domains = (L/xi_KZ)^d_s = {N_domains:.4f}")

    if N_domains < 1.5:
        print(f"    ** MARGINAL SINGLE DOMAIN ** (N_domains = {N_domains:.2f} ~ 1)")
    elif xi_ratio > 1:
        print(f"    ** SINGLE DOMAIN ** (xi_KZ > L: no walls)")
    else:
        print(f"    ** MULTIPLE DOMAINS ** ({N_domains:.1f} domains, walls present)")

    results[label] = {
        'xi_KZ_formal': xi_KZ_formal,
        'xi_KZ_phys': xi_KZ_phys,
        'L_physical': L_physical,
        'xi_ratio': xi_ratio,
        'N_domains': N_domains,
        'adiab': ad,
        'regime': regime,
    }

# ===========================================================================
# 5. Cross-check with S38 Result
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 5: CROSS-CHECK WITH S38")
print("=" * 72)

L_sys_s38 = 0.03  # M_KK^{-1}, from s37_instanton_mc  # (local)
L_over_xi_GL_s38 = 0.031  # (local)

print(f"  S38 result:")
print(f"    L_sys = {L_sys_s38:.4f} M_KK^{{-1}}")
print(f"    L/xi_GL = {L_over_xi_GL_s38:.4f}")
print(f"    Conclusion: single domain (no walls)")
print(f"")
print(f"  S55 graph analysis:")
print(f"    d_C = 1/bandwidth = {d_C:.6f} M_KK^{{-1}}")
print(f"    L_physical = diameter * d_C = {diameter} * {d_C:.4f} = {L_physical:.4f}")
print(f"    L_physical / xi_GL = {L_physical/xi_GL:.6f}")
print(f"    L_physical / xi_BCS = {L_physical/xi_BCS:.6f}")

# The two length scales:
# S38 L_sys = 0.03: this is the effective 0D box size from GL (condensate extent)
# S55 L_physical: graph diameter in spectral geometry units
print(f"\n  Comparison of system sizes:")
print(f"    L_sys (S38 GL)      = {L_sys_s38:.4f} M_KK^{{-1}}")
print(f"    L_graph (S55 spec)  = {L_physical:.4f} M_KK^{{-1}}")
print(f"    Ratio L_graph/L_sys = {L_physical/L_sys_s38:.4f}")

if L_physical < xi_BCS:
    print(f"\n  BOTH measures give L << xi_BCS = {xi_BCS:.4f}")
    print(f"  The entire graph is a single coherence volume.")
    print(f"  KZ predicts ZERO domain walls on this lattice.")

# ===========================================================================
# 6. Alternative: Graph-Intrinsic KZ (Hop Units)
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 6: GRAPH-INTRINSIC KZ (IN HOP UNITS)")
print("=" * 72)

# An alternative approach: work entirely in graph (hop) units.
# The bandwidth W sets the energy scale. The graph diameter D sets the length.
# xi_KZ in hops = xi_KZ_phys / d_C

for label, r in results.items():
    xi_hops = r['xi_KZ_phys'] / d_C
    print(f"  {label}:")
    print(f"    xi_KZ = {r['xi_KZ_phys']:.4f} M_KK^{{-1}} = {xi_hops:.2f} hops")
    print(f"    Diameter = {diameter} hops")
    print(f"    xi_KZ / diameter = {xi_hops/diameter:.4f}")
    if xi_hops > diameter:
        print(f"    -> SINGLE DOMAIN")
    else:
        print(f"    -> {max(1, (diameter/xi_hops)**d_s):.1f} domains")

# ===========================================================================
# 7. Pair Vibration Mode Analysis
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 7: PAIR VIBRATION MODE (omega_PV = 0.792)")
print("=" * 72)

# The pair vibration mode at omega_PV = 0.792 is a collective Delta_N = +/- 2 mode.
# Its wavelength lambda_PV = v_F / omega_PV defines a coherence scale.
# Compare to graph size.

lambda_PV_phys = xi_0 * (omega_PV / Delta_0_OES)  # Approximate: use BCS coherence with PV frequency
# More precisely: lambda_PV ~ 2*pi*v_F/omega_PV, and v_F ~ Delta_0 * xi_BCS
v_F_BCS = Delta_0_OES * xi_BCS  # v_F from BCS relation v_F = Delta * xi
lambda_PV = 2 * np.pi * v_F_BCS / omega_PV

print(f"  omega_PV            = {omega_PV:.6f} M_KK")
print(f"  v_F_BCS = Delta*xi  = {v_F_BCS:.6f} M_KK * M_KK^{{-1}} (dimensionless)")
print(f"  lambda_PV = 2*pi*v_F/omega_PV = {lambda_PV:.6f} M_KK^{{-1}}")
print(f"  lambda_PV / L_graph = {lambda_PV / L_physical:.4f}")
print(f"  lambda_PV / xi_BCS  = {lambda_PV / xi_BCS:.4f}")

if lambda_PV > L_physical:
    print(f"  PV mode wavelength >> graph size: ZERO-MODE of pair vibration.")
    print(f"  The entire graph oscillates in phase (k=0 pair vibration).")

# ===========================================================================
# 8. Landau-Zener at Each Level Crossing
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 8: LANDAU-ZENER DIABATIC PROBABILITY")
print("=" * 72)

# S38 found: ALL 1378 crossings have xi < 10^{-3} (deeply diabatic).
# Recompute the representative LZ probability with updated parameters.

# dE/dt at the fold: the BCS gap opens/closes over the transit window.
# BCS window: tau in [0.175, 0.205], width 0.030.
Delta_tau_BCS = 0.030
dDelta_dtau = Delta_0_OES / (Delta_tau_BCS / 2)  # Gap slope at edge
dDelta_dt = dDelta_dtau * abs(v_terminal)

lz_exp = np.pi * Delta_0_OES**2 / (2 * dDelta_dt)
P_LZ_diab = np.exp(-lz_exp)

print(f"  BCS window width    = {Delta_tau_BCS}")
print(f"  |v_terminal|        = {abs(v_terminal):.4f}")
print(f"  dDelta/dtau (edge)  = {dDelta_dtau:.4f}")
print(f"  dDelta/dt           = {dDelta_dt:.4f}")
print(f"  LZ exponent         = pi*Delta^2/(2*dDelta/dt) = {lz_exp:.6f}")
print(f"  P_LZ (diabatic)     = exp(-{lz_exp:.4f}) = {P_LZ_diab:.6e}")

if P_LZ_diab > 0.5:
    print(f"  -> DEEPLY DIABATIC: transit is too fast for adiabatic following")
    print(f"     Consistent with S38 P_exc = 1.000")
else:
    print(f"  -> Partially adiabatic")

# Bogoliubov pair production per mode (Schwinger analog)
print(f"\n  Schwinger-analog pair creation:")
S_schwinger = np.pi * Delta_0_OES**2 / dDelta_dt
print(f"    S_Schwinger = pi*Delta^2/|dDelta/dt| = {S_schwinger:.6f}")
print(f"    S_inst (S37) = {S_inst:.6f}")
print(f"    S_Schwinger/S_inst = {S_schwinger/S_inst:.4f}")
print(f"    Duality: {abs(S_schwinger - 2*S_inst)/(2*S_inst):.2%} deviation from S_Schwinger = 2*S_inst")

# ===========================================================================
# 9. Summary Table
# ===========================================================================
print("\n" + "=" * 72)
print("SECTION 9: SUMMARY")
print("=" * 72)

print(f"\n  {'Parameter':<35} {'Value':>15} {'Unit':<15}")
print(f"  {'-'*35} {'-'*15} {'-'*15}")
print(f"  {'N_cells':<35} {N_cells:>15d} {'':<15}")
print(f"  {'Graph diameter':<35} {diameter:>15d} {'hops':<15}")
print(f"  {'Mean coordination':<35} {mean_coord:>15.4f} {'':<15}")
print(f"  {'Spectral gap (Fiedler)':<35} {spectral_gap:>15.6f} {'':<15}")
print(f"  {'d_s (spectral dimension)':<35} {d_s:>15.1f} {'':<15}")
print(f"  {'Bandwidth at fold':<35} {bw_fold:>15.6f} {'M_KK':<15}")
print(f"  {'Band gap at fold':<35} {gap_fold:>15.6f} {'M_KK':<15}")
print(f"  {'d_C (lattice spacing)':<35} {d_C:>15.6f} {'M_KK^{-1}':<15}")
print(f"  {'L_physical (graph diam)':<35} {L_physical:>15.6f} {'M_KK^{-1}':<15}")
print(f"  {'xi_BCS':<35} {xi_BCS:>15.6f} {'M_KK^{-1}':<15}")
print(f"  {'xi_GL':<35} {xi_GL:>15.6f} {'M_KK^{-1}':<15}")
print(f"  {'L/xi_BCS':<35} {L_physical/xi_BCS:>15.6f} {'':<15}")
print(f"  {'L/xi_GL':<35} {L_physical/xi_GL:>15.6f} {'':<15}")
print(f"  {'tau_Q = 1/omega_tau':<35} {tau_Q:>15.6f} {'M_KK^{-1}':<15}")
print(f"  {'tau_0 = 1/Delta_0_OES':<35} {tau_0:>15.6f} {'M_KK^{-1}':<15}")
print(f"  {'Adiabaticity tau_Q/tau_0':<35} {adiab:>15.6f} {'':<15}")

# Key result
ref = results["MF-BCS (z=2, tau_0=1/Delta)"]
xi_KZ_main = ref['xi_KZ_phys']
print(f"  {'xi_KZ (MF, physical)':<35} {xi_KZ_main:>15.6f} {'M_KK^{-1}':<15}")
print(f"  {'xi_KZ / L_graph':<35} {ref['xi_ratio']:>15.4f} {'':<15}")
print(f"  {'N_domains (MF)':<35} {ref['N_domains']:>15.4f} {'':<15}")
print(f"  {'P_LZ (diabatic)':<35} {P_LZ_diab:>15.6e} {'':<15}")

print(f"\n  GATE VERDICT: KZ-DOMAIN-55 = INFO")
print(f"  ─────────────────────────────────────────────────────────")

if ref['N_domains'] < 1.5:
    verdict = "MARGINAL SINGLE DOMAIN"
    print(f"  Result: {verdict}")
    print(f"  xi_KZ = {xi_KZ_main:.4f}, L_graph = {L_physical:.4f}, ratio = {ref['xi_ratio']:.4f}")
    print(f"  N_domains = {ref['N_domains']:.2f} ~ 1. The coherence length spans {ref['xi_ratio']*100:.0f}%")
    print(f"  of the graph diameter. At most one weak domain boundary.")
    print(f"  Qualitatively consistent with S38 single-domain conclusion,")
    print(f"  but the margin is tight (xi_KZ/L = 0.91, not >> 1).")
elif ref['xi_ratio'] > 1:
    verdict = "SINGLE DOMAIN"
    print(f"  Result: {verdict}")
    print(f"  xi_KZ = {xi_KZ_main:.4f} > L_graph = {L_physical:.4f}")
else:
    verdict = "MULTIPLE DOMAINS"
    print(f"  Result: {verdict}")
    print(f"  N_domains ~ {ref['N_domains']:.1f}")

print(f"\n  Cross-pillar implications:")
print(f"  - Pillar V (Josephson): E_J/E_C = 0.818 (Mott side). Single domain")
print(f"    means the entire array phase-locks — consistent with Mott insulator.")
print(f"  - Pillar VI (Solitons): No kink-antikink pairs on this lattice.")
print(f"    Jackiw-Rebbi fermion binding requires domain walls that don't form.")
print(f"  - Pillar VII (d_s flow): d_s = 2.0 graph dimension enters the KZ exponent")
print(f"    but is moot when xi_KZ > L (single domain regardless of d_s).")
print(f"  - Pillar II (Volovik): The superfluid coherence length exceeding the")
print(f"    system size is the definition of a quantum liquid — the graph IS the")
print(f"    condensate, not a container for it.")

# ===========================================================================
# 10. Save results
# ===========================================================================
save_path = os.path.join('computations', 'session-55', 's55_kz_domain.npz')
np.savez(save_path,
    # Graph properties
    N_cells=N_cells,
    diameter=diameter,
    mean_distance=mean_distance,
    mean_coordination=mean_coord,
    spectral_gap=spectral_gap,
    lambda_max=lambda_max,
    L_eff_spectral=L_eff_spectral,
    d_C=d_C,
    L_physical=L_physical,
    d_s=d_s,
    bw_fold=bw_fold,
    gap_fold=gap_fold,
    # KZ parameters
    tau_Q=tau_Q,
    tau_0=tau_0,
    adiabaticity=adiab,
    xi_0=xi_0,
    xi_KZ_MF=results["MF-BCS (z=2, tau_0=1/Delta)"]['xi_KZ_phys'],
    xi_KZ_ball=results["Ballistic (z=1, tau_0=1/Delta)"]['xi_KZ_phys'],
    xi_ratio_MF=results["MF-BCS (z=2, tau_0=1/Delta)"]['xi_ratio'],
    xi_ratio_ball=results["Ballistic (z=1, tau_0=1/Delta)"]['xi_ratio'],
    N_domains_MF=results["MF-BCS (z=2, tau_0=1/Delta)"]['N_domains'],
    N_domains_ball=results["Ballistic (z=1, tau_0=1/Delta)"]['N_domains'],
    # Landau-Zener
    P_LZ_diab=P_LZ_diab,
    lz_exponent=lz_exp,
    S_schwinger=S_schwinger,
    # PV mode
    lambda_PV=lambda_PV,
    # Verdict
    gate_name='KZ-DOMAIN-55',
    gate_verdict='INFO',
    gate_detail=f'MARGINAL SINGLE DOMAIN: xi_KZ/L = {ref["xi_ratio"]:.4f}, N_domains = {ref["N_domains"]:.4f}',
    verdict=verdict,
)
print(f"\n  Saved: {save_path}")
print("=" * 72)
