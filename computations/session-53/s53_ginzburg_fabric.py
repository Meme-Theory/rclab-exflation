#!/usr/bin/env python3
"""
S53 GINZBURG-FABRIC-53: GL Validity Criterion for the Fabric
=============================================================

Gate: GINZBURG-FABRIC-53 (INFO)

Computes:
  1. Cell size a_cell = (Vol_SU3_Haar / N_cells)^{1/8}  [8D cell radius]
  2. Ginzburg ratio Gi = xi_BCS / a_cell
  3. Ginzburg number Gi_fluct = (Delta_0 / E_F)^{2/3}  [d=8 fluctuation criterion]
  4. Josephson array assessment: phase-coherent vs charge-quantized
  5. 0D limit validity assessment for GL-JOSEPHSON-52 dispersion

All constants from canonical_constants.py.
"""

import sys
sys.path.insert(0, r"C:\sandbox\Ainulindale Exflation\computations")

import numpy as np
from canonical_constants import (
    Vol_SU3_Haar, N_cells, xi_BCS, xi_GL, Delta_0_GL, E_B2_mean,
    J_C2, J_su2, J_u1, L_over_xi, a_GL, b_GL, E_cond, barrier_0d,
    rho_B2_per_mode, E_B1, E_B3_mean, T_acoustic, PI,
    omega_PV, N_dof_BCS, E_cond_ED_8mode,
)

# Output file
outpath = r"C:\sandbox\Ainulindale Exflation\computations\s53_ginzburg_fabric_output.txt"
outlines = []

def pr(s=""):
    print(s)
    outlines.append(s)

pr("=" * 70)
pr("S53 GINZBURG-FABRIC-53: GL Validity Criterion for the Fabric")
pr("=" * 70)

# =====================================================================
# Section 1: Cell size in 8D
# =====================================================================
pr("\n--- Section 1: Cell Size ---")

V_cell = Vol_SU3_Haar / N_cells
dim_SU3 = 8  # dim(SU(3)) = 8

# 8D cell radius: volume of 8D ball = pi^4 / 24 * R^8
# But cells are not spherical; the natural length scale is V^{1/d}
a_cell_8D = V_cell ** (1.0 / dim_SU3)

# For comparison: 3D BCC convention used in S52
a_BCC_3D = (2.0 * V_cell) ** (1.0 / 3.0)

# Also compute the 8D "sphere-equivalent radius" for completeness
# V_8 = pi^4 / 24 * R^8  =>  R = (24 * V_cell / pi^4)^{1/8}
R_sphere_8D = (24.0 * V_cell / PI**4) ** (1.0 / dim_SU3)

pr(f"  Vol(SU(3))_Haar = {Vol_SU3_Haar:.2f}")
pr(f"  N_cells         = {N_cells}")
pr(f"  V_cell           = {V_cell:.4f}")
pr(f"  dim(SU(3))       = {dim_SU3}")
pr(f"")
pr(f"  a_cell (8D) = V_cell^{{1/8}} = {a_cell_8D:.6f}  M_KK^{{-1}}")
pr(f"  R_sphere_8D = (24*V/(pi^4))^{{1/8}} = {R_sphere_8D:.6f}  M_KK^{{-1}}")
pr(f"  a_BCC (3D, S52 convention) = {a_BCC_3D:.4f}  M_KK^{{-1}}")
pr(f"")
pr(f"  NOTE: a_cell(8D) is the correct intrinsic cell scale for an 8D manifold.")
pr(f"  The S52 a_BCC used the 3D BCC convention (2*V)^{{1/3}} which is")
pr(f"  an effective 3D projection. The 8D measure is the physically relevant one.")

# =====================================================================
# Section 2: Ginzburg ratio
# =====================================================================
pr("\n--- Section 2: Ginzburg Ratio ---")

Gi = xi_BCS / a_cell_8D
Gi_GL = xi_GL / a_cell_8D

# Also compute with sphere-equivalent
Gi_sphere = xi_BCS / R_sphere_8D

# With the 3D BCC scale (for cross-check with S52)
Gi_3D = xi_BCS / a_BCC_3D

pr(f"  xi_BCS = {xi_BCS:.6f}  M_KK^{{-1}}")
pr(f"  xi_GL  = {xi_GL:.6f}  M_KK^{{-1}}")
pr(f"")
pr(f"  Gi (8D) = xi_BCS / a_cell = {Gi:.4f}")
pr(f"  Gi_GL   = xi_GL  / a_cell = {Gi_GL:.4f}")
pr(f"  Gi (8D sphere) = xi_BCS / R_sphere = {Gi_sphere:.4f}")
pr(f"  Gi (3D BCC)    = xi_BCS / a_BCC    = {Gi_3D:.4f}")
pr(f"")

if Gi > 10:
    regime_str = "Gi >> 1: CONTINUUM GL VALID. Mean-field applies."
elif Gi > 2:
    regime_str = "Gi > 1: GL marginally valid. Lattice corrections of order 1/Gi."
elif Gi > 0.5:
    regime_str = "Gi ~ 1: JOSEPHSON ARRAY REGIME. Lattice effects comparable to continuum."
else:
    regime_str = "Gi << 1: STRONG-COUPLING LATTICE. GL fails."

pr(f"  VERDICT: {regime_str}")

# =====================================================================
# Section 3: Ginzburg number (fluctuation criterion)
# =====================================================================
pr("\n--- Section 3: Ginzburg Number (Fluctuation Criterion) ---")

# Standard Ginzburg criterion for d spatial dimensions:
# Gi_fluct = (T_c / E_F)^{4/(d-2)}
# In BCS, T_c ~ Delta_0 and E_F ~ E_B2_mean (Fermi energy at band center)
# For d=8: exponent = 4/(8-2) = 4/6 = 2/3

d_eff = 8  # (local)
exponent_fluct = 4.0 / (d_eff - 2)

Delta_over_EF = Delta_0_GL / E_B2_mean
Gi_fluct = Delta_over_EF ** exponent_fluct

pr(f"  d_eff = {d_eff} (SU(3) manifold dimension)")
pr(f"  Ginzburg exponent = 4/(d-2) = {exponent_fluct:.4f}")
pr(f"")
pr(f"  Delta_0 = {Delta_0_GL:.6f}  M_KK")
pr(f"  E_F     = E_B2_mean = {E_B2_mean:.6f}  M_KK")
pr(f"  Delta_0 / E_F = {Delta_over_EF:.6f}")
pr(f"")
pr(f"  Gi_fluct = (Delta_0/E_F)^{{2/3}} = {Gi_fluct:.6f}")
pr(f"")

# More refined: use the number-theoretic formula
# Gi_fluct = (1/N_eff) * (T_c/E_F)^{(4-d)/2} for d < 4
# For d > 4: mean-field becomes EXACT in thermodynamic limit
# But we are NOT in thermodynamic limit (N_pair = 1)

pr(f"  CRITICAL OBSERVATION: For d >= 4 (upper critical dimension d_uc = 4 for")
pr(f"  phi^4 theory), mean-field critical exponents are EXACT in the thermodynamic")
pr(f"  limit. At d = 8, we are WELL ABOVE d_uc = 4.")
pr(f"")
pr(f"  HOWEVER, we have N_pair = 1 (S53 W2-6). The thermodynamic limit does not")
pr(f"  apply. Finite-size corrections scale as 1/N, which is O(1) here.")
pr(f"")
pr(f"  The Ginzburg number Gi_fluct = {Gi_fluct:.4f} ~ 1 is FORMALLY large,")
pr(f"  but this is the bulk criterion. The true validity issue is N_pair = 1,")
pr(f"  not the dimensionality.")

# =====================================================================
# Section 4: Josephson array analysis
# =====================================================================
pr("\n--- Section 4: Josephson Array Assessment ---")

# Each cell has N_pair = 1 Cooper pair.
# The Josephson energy is E_J = J * cos(phi_i - phi_j)
# The charging energy is E_C = (2e)^2 / (2C) where C is cell capacitance
#
# In the framework, the "charge" is the Cooper pair number n_i
# and the phase phi_i is the conjugate variable.
# For a single pair per cell: n_i = 0 or 1 (charge quantization matters)
#
# E_J / E_C determines the regime:
#   E_J >> E_C: phase-coherent (Josephson regime, phi well-defined)
#   E_J << E_C: Coulomb blockade (n well-defined, phase fluctuations destroy coherence)

# The charging energy for the BCS system:
# In the nuclear BCS analogy, E_C ~ 1/(2 * N(E_F) * a_cell^d)
# = inverse compressibility per cell
# For our system: N(E_F) per cell = rho_B2_per_mode * V_cell / Vol_SU3_Haar
# But rho_B2_per_mode is the total DOS. Per cell:
rho_per_cell = rho_B2_per_mode / N_cells

# Charging energy: E_C = 1 / (2 * rho_per_cell)
# This is the energy cost to add one particle to a cell
E_C = 1.0 / (2.0 * rho_per_cell)

# Josephson coupling (dominant C^2 direction)
E_J = J_C2

ratio_JC = E_J / E_C

pr(f"  N_pair per cell = 1  (S53 W2-6)")
pr(f"  N_cells = {N_cells}")
pr(f"")
pr(f"  Josephson coupling:")
pr(f"    J_C2  = {J_C2:.4f}  M_KK  (C^2 coset, 4 bonds)")
pr(f"    J_su2 = {J_su2:.4f}  M_KK  (su(2), 3 bonds)")
pr(f"    J_u1  = {J_u1:.4f}  M_KK  (u(1), 1 bond)")
pr(f"")
pr(f"  Charging energy:")
pr(f"    rho_B2 (total) = {rho_B2_per_mode:.4f}")
pr(f"    rho_per_cell   = {rho_per_cell:.6f}")
pr(f"    E_C = 1/(2*rho) = {E_C:.6f}  M_KK")
pr(f"")
pr(f"  E_J / E_C = {ratio_JC:.4f}")

if ratio_JC > 10:
    josephson_regime = "PHASE-COHERENT (E_J >> E_C). Phase is well-defined, number fluctuates."
elif ratio_JC > 1:
    josephson_regime = "INTERMEDIATE (E_J > E_C). Partial phase coherence."
elif ratio_JC > 0.1:
    josephson_regime = "CHARGE-QUANTIZED regime (E_J ~ E_C). Phase fluctuations important."
else:
    josephson_regime = "COULOMB BLOCKADE (E_J << E_C). Number is well-defined, phase fluctuates."

pr(f"")
pr(f"  VERDICT: {josephson_regime}")

# Additional: quantum phase model analysis
# The quantum phase transition occurs at E_J/E_C ~ (z/d_eff) for a d-dim lattice
# z = coordination number. For BCC in 8D this is model-dependent.
# Conservatively use z = 2*d = 16 for hypercubic.

z_hyper = 2 * dim_SU3  # = 16 for 8D hypercubic
critical_ratio = z_hyper  # rough criterion for phase coherence in d>2

pr(f"")
pr(f"  Phase transition criterion (quantum rotor model, d={dim_SU3}):")
pr(f"    Critical E_J/E_C ~ z = {z_hyper} for d-dim lattice")
pr(f"    Actual E_J/E_C = {ratio_JC:.2f}")
if ratio_JC > critical_ratio:
    pr(f"    => Above critical: SUPERFLUID (phase-ordered)")
else:
    pr(f"    => Below critical: MOTT INSULATOR (charge-ordered)")

# =====================================================================
# Section 5: 0D limit and dispersion validity
# =====================================================================
pr("\n--- Section 5: 0D Limit and Dispersion Validity ---")

# TWO notions of "L":
# (A) L_fabric = Vol_SU3^{1/8} = geometric extent of the full SU(3) manifold
# (B) L_pairing = pairing window width in energy/momentum space (S37 convention)
#     The canonical L_over_xi = 0.031 (S37) is this BCS pairing-window quantity.
#     It measures the width of the energy shell where pairing acts, divided by xi.
#
# We compute L_fabric here. The canonical 0.031 is a different (but consistent)
# statement about the pairing physics.

L_fabric = Vol_SU3_Haar ** (1.0 / dim_SU3)
L_over_xi_check = L_fabric / xi_BCS

# The S37 canonical L/xi = 0.031 uses the BCS pairing window as "L"
# L_pairing = 0.031 * xi_BCS
L_pairing = L_over_xi * xi_BCS

pr(f"  Two notions of system size:")
pr(f"    L_fabric  = Vol^{{1/8}}  = {L_fabric:.6f}  M_KK^{{-1}}  (geometric)")
pr(f"    L_pairing = 0.031*xi   = {L_pairing:.6f}  M_KK^{{-1}}  (BCS window, S37)")
pr(f"  xi_BCS    = {xi_BCS:.6f}  M_KK^{{-1}}")
pr(f"")
pr(f"  L_fabric / xi  = {L_over_xi_check:.4f}  (geometric: xi fits ~3x in fabric)")
pr(f"  L_pairing / xi = {L_over_xi}  (canonical: 0D limit of BCS)")
pr(f"")
pr(f"  INTERPRETATION: The geometric fabric is ~3 coherence lengths across (8D),")
pr(f"  but the BCS pairing window is 32x SMALLER than xi. This means the pair")
pr(f"  wavefunction extends over the entire pairing shell — the 0D limit of BCS")
pr(f"  is about energy-space confinement, not real-space confinement.")
pr(f"")

# How many K-modes fit in one cell?
# K_max = pi / a_cell (first Brillouin zone boundary)
K_BZ = PI / a_cell_8D
K_min = 2 * PI / L_fabric  # longest mode that fits in the fabric

# Number of distinct K-modes per dimension
n_K_per_dim = L_fabric / (2 * a_cell_8D)

# Total K-modes (8D): N_K ~ (L/2a)^8 ~ N_cells
N_K_total = n_K_per_dim ** dim_SU3

# Number of K-modes with K < 1/xi (the relevant low-energy modes)
K_xi = 1.0 / xi_BCS
n_K_below_xi = (K_xi / K_min)  # per dimension
N_K_below_xi_total = n_K_below_xi ** dim_SU3

pr(f"  K_BZ = pi/a_cell = {K_BZ:.4f}")
pr(f"  K_min = 2*pi/L   = {K_min:.4f}")
pr(f"  K_xi  = 1/xi_BCS = {1.0/xi_BCS:.4f}")
pr(f"")
pr(f"  N_K per dim   = L/(2a) = {n_K_per_dim:.4f}")
pr(f"  N_K total (8D) ~ N_K^8 = {N_K_total:.2f}  (cf. N_cells = {N_cells})")
pr(f"")
pr(f"  Modes with K < 1/xi:")
pr(f"    per dim: {n_K_below_xi:.4f}")
pr(f"    total (8D): {N_K_below_xi_total:.4f}")

# The critical question: does the Goldstone dispersion omega = c*K
# have any K-modes between K_min and K_BZ?
n_propagating = int(K_BZ / K_min)

pr(f"")
pr(f"  Number of propagating K-modes (K_min to K_BZ): {n_propagating}")
pr(f"  = N_cells^{{1/8}} per dim = {N_cells**(1.0/8):.4f}")

# =====================================================================
# Section 6: Comprehensive validity assessment
# =====================================================================
pr("\n--- Section 6: Comprehensive Validity Assessment ---")

pr(f"")
pr(f"  CRITERION 1: Ginzburg ratio Gi = xi_BCS / a_cell")
pr(f"    Value: {Gi:.4f}")
pr(f"    Interpretation: xi_BCS {'>' if Gi > 1 else '<='} a_cell")
if Gi > 1:
    pr(f"    The coherence length EXCEEDS the cell size by {Gi:.1f}x.")
    pr(f"    A Cooper pair extends over ~Gi^8 = {Gi**8:.1f} cells.")
    pr(f"    Continuum GL is geometrically valid at the cell scale.")
else:
    pr(f"    The coherence length is SMALLER than the cell size.")
    pr(f"    Each Cooper pair is confined to a single cell.")
    pr(f"    Continuum GL is NOT geometrically valid.")

N_cells_per_pair = Gi ** dim_SU3  # number of cells a pair spans

pr(f"")
pr(f"  CRITERION 2: Ginzburg number (fluctuation criterion)")
pr(f"    Gi_fluct = {Gi_fluct:.4f}")
pr(f"    For d=8 > d_uc=4: bulk mean-field is exact (thermodynamic limit).")
pr(f"    But N_pair=1: finite-size fluctuations O(1/N_pair) = O(1).")
pr(f"    GL mean-field theory CANNOT be trusted for 1 Cooper pair.")

pr(f"")
pr(f"  CRITERION 3: Josephson array regime")
pr(f"    E_J/E_C = {ratio_JC:.2f}")
if ratio_JC > 1:
    pr(f"    E_J > E_C: phase is partially well-defined.")
    pr(f"    But with N_pair=1 per cell, the array is in the QUANTUM REGIME")
    pr(f"    where number and phase cannot both be sharp (uncertainty relation).")
else:
    pr(f"    E_J < E_C: Coulomb blockade dominates.")
    pr(f"    Cooper pair number is well-defined (n=0 or 1), phase is undefined.")

pr(f"")
pr(f"  CRITERION 4: 0D limit")
pr(f"    L_fabric/xi = {L_over_xi_check:.4f}  (geometric: fabric ~ 3 xi across)")
pr(f"    L_pairing/xi = {L_over_xi}  (BCS pairing window: 32x smaller than xi)")
pr(f"    The geometric fabric spans ~3 coherence lengths, so the pair could")
pr(f"    in principle exhibit real-space structure. BUT:")
pr(f"    - The BCS pairing window (energy shell) is 32x smaller than xi (0D limit)")
pr(f"    - With Gi = 0.5, a pair barely extends beyond one cell")
pr(f"    - K_min > K_BZ: zero propagating modes in the Brillouin zone")
pr(f"    The GL free energy reduces to a 0D quantum mechanics problem:")
pr(f"      F[Delta] -> F(Delta) (no gradient terms)")
pr(f"    The S52 dispersion exists mathematically but K_min > K_BZ means")
pr(f"    no discrete K-point falls within the zone. The continuum limit is")
pr(f"    an extrapolation beyond the lattice resolution.")

pr(f"")
pr(f"  CRITERION 5: K-mode counting")
pr(f"    Propagating modes: {n_propagating}")
pr(f"    Cells spanned by xi_BCS: Gi^8 = {N_cells_per_pair:.1f}")
if N_cells_per_pair > N_cells:
    pr(f"    xi spans MORE cells ({N_cells_per_pair:.0f}) than exist ({N_cells}).")
    pr(f"    Equivalently, L/xi < 1. The only relevant mode is K=0.")
    pr(f"    All finite-K modes in the S52 dispersion are VIRTUAL (exponentially")
    pr(f"    suppressed by the factor exp(-a_cell/xi) per lattice spacing).")
elif N_cells_per_pair > 1:
    pr(f"    xi spans {N_cells_per_pair:.0f} cells (< N_cells = {N_cells}).")
    pr(f"    Low-K modes propagate; high-K modes are lattice artifacts.")
else:
    pr(f"    xi < a_cell. Each pair is localized to one cell.")

# =====================================================================
# Section 7: What IS the correct description?
# =====================================================================
pr("\n--- Section 7: Correct Physical Description ---")

pr(f"")
pr(f"  Given: N_pair = 1, N_cells = 32, L/xi = {L_over_xi_check:.4f}, Gi = {Gi:.4f}")
pr(f"")
pr(f"  The system is a SINGLE COOPER PAIR delocalized across a 32-site lattice")
pr(f"  with Josephson coupling J_C2 = {J_C2:.3f} M_KK.")
pr(f"")
pr(f"  The correct description is NOT Ginzburg-Landau (continuum, mean-field,")
pr(f"  macroscopic order parameter), but rather:")
pr(f"")
pr(f"  (a) TIGHT-BINDING for the pair center-of-mass motion on the 32-cell lattice.")
pr(f"      Bandwidth ~ 2*z*J = 2*{z_hyper}*{J_C2:.3f} = {2*z_hyper*J_C2:.3f} M_KK")
pr(f"      This pair is NOT condensed — it is a single quantum particle on a lattice.")
pr(f"")
pr(f"  (b) The S52 'Goldstone mode' (c = 0.915) is actually the pair dispersion")
pr(f"      omega(K) = 2*J*(1 - cos(K*a)). For small K this looks like c*K,")
pr(f"      but it is the kinetic energy of ONE pair, not a collective Goldstone boson")
pr(f"      of a macroscopic condensate.")
pr(f"")
pr(f"  (c) True spontaneous U(1)_7 breaking requires the thermodynamic limit N->inf.")
pr(f"      For N_pair=1, the ground state has DEFINITE particle number, not")
pr(f"      definite phase. The phase is COMPLETELY UNCERTAIN: delta_phi = 2*pi.")
pr(f"")
pr(f"  (d) The Leggett modes (inter-sector phase oscillations) require at least")
pr(f"      O(1) pairs PER SECTOR. With 1 pair total in 3 sectors, the pair")
pr(f"      occupies one sector at a time. Leggett modes are NOT SUPPORTED.")

# =====================================================================
# Section 8: Salvageable physics from GL-JOSEPHSON-52
# =====================================================================
pr("\n--- Section 8: What Survives from S52 ---")

pr(f"")
pr(f"  Despite GL being invalid for N_pair=1, the S52 computation is not wasted:")
pr(f"")
pr(f"  1. STIFFNESS MATRIX: The Josephson couplings J_C2, J_su2, J_u1 are")
pr(f"     properties of the GEOMETRY (inter-cell overlap integrals), independent")
pr(f"     of N_pair. They define the lattice Hamiltonian for pair hopping.")
pr(f"")
pr(f"  2. AMPLITUDE MASSES: The V_amp eigenvalues give the pair binding energy")
pr(f"     in each sector. These are single-pair properties, valid at N_pair=1.")
pr(f"")
pr(f"  3. SOUND SPEED: c_Gold = 0.915 reinterpreted as pair group velocity")
pr(f"     v_pair = dE/dK|_K=0 = a_cell * J_C2 / hbar. This is the pair mobility.")
pr(f"")
pr(f"  4. DISPERSION TOPOLOGY: The number of branches (6) is a symmetry property")
pr(f"     (3 sectors x 2 = amplitude + phase per sector). This structure persists")
pr(f"     regardless of pair number.")

# =====================================================================
# Section 9: Summary table
# =====================================================================
pr("\n--- Section 9: Summary Table ---")
pr(f"")
pr(f"  {'Quantity':<30s} {'Value':<15s} {'Unit':<15s}")
pr(f"  {'='*60}")
pr(f"  {'V_cell':<30s} {V_cell:<15.4f} {'M_KK^{-8}':<15s}")
pr(f"  {'a_cell (8D)':<30s} {a_cell_8D:<15.6f} {'M_KK^{-1}':<15s}")
pr(f"  {'a_BCC (3D, S52)':<30s} {a_BCC_3D:<15.4f} {'M_KK^{-1}':<15s}")
pr(f"  {'xi_BCS':<30s} {xi_BCS:<15.6f} {'M_KK^{-1}':<15s}")
pr(f"  {'xi_GL':<30s} {xi_GL:<15.6f} {'M_KK^{-1}':<15s}")
pr(f"  {'Gi = xi_BCS/a_cell':<30s} {Gi:<15.4f} {'':<15s}")
pr(f"  {'Gi_fluct':<30s} {Gi_fluct:<15.6f} {'':<15s}")
pr(f"  {'E_J (J_C2)':<30s} {J_C2:<15.4f} {'M_KK':<15s}")
pr(f"  {'E_C':<30s} {E_C:<15.6f} {'M_KK':<15s}")
pr(f"  {'E_J / E_C':<30s} {ratio_JC:<15.4f} {'':<15s}")
pr(f"  {'L_fabric':<30s} {L_fabric:<15.6f} {'M_KK^{-1}':<15s}")
pr(f"  {'L/xi_BCS':<30s} {L_over_xi_check:<15.4f} {'':<15s}")
pr(f"  {'K_BZ':<30s} {K_BZ:<15.4f} {'M_KK':<15s}")
pr(f"  {'N_cells_per_pair (Gi^8)':<30s} {N_cells_per_pair:<15.1f} {'':<15s}")
pr(f"  {'N_K propagating':<30s} {n_propagating:<15d} {'':<15s}")

pr(f"")
pr("=" * 70)
pr("GATE VERDICT: GINZBURG-FABRIC-53 — INFO")
pr("=" * 70)
pr(f"")
pr(f"  Gi = xi_BCS / a_cell = {Gi:.4f}")
pr(f"")
pr(f"  GL validity: MARGINAL at the geometric level (Gi ~ {Gi:.1f}),")
pr(f"  but INVALID at the particle-number level (N_pair = 1).")
pr(f"")
pr(f"  The system is a single Cooper pair on a 32-site 8D lattice,")
pr(f"  not a macroscopic condensate described by a GL order parameter.")
pr(f"  The S52 dispersion branches are reinterpreted as the energy bands")
pr(f"  of a single pair hopping on the Josephson lattice, not as")
pr(f"  collective modes of a superfluid.")
pr(f"")
pr(f"  Classification: The Josephson array is in the intermediate regime")
pr(f"  (E_J/E_C = {ratio_JC:.2f}), but with N_pair = 1 the relevant")
pr(f"  physics is quantum mechanics of a single pair, not a quantum")
pr(f"  phase model.")
pr("=" * 70)

# Write output
with open(outpath, "w") as f:
    f.write("\n".join(outlines) + "\n")

print(f"\nSaved: {outpath}")
