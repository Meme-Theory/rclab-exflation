#!/usr/bin/env python3
"""
VORTEX-NUCLEATION-53: KZ Vortex Density and Topological Baryogenesis
=====================================================================

Context:
  ETA-B-52 proved phi_CP = 0 identically (3 proofs: BDI, J-symmetry, spectral pairing).
  No baryogenesis from bulk CP violation. The ONLY surviving route is TOPOLOGICAL:
  the ABJ anomaly in vortex cores (Volovik mechanism, Paper 09).

  During the KZ transit, the BCS condensate breaks U(1)_7 -> phase winding produces
  vortex-antivortex pairs. CP violation arises from the TOPOLOGY of the vortex
  configuration, not from the bulk spectrum.

Physics (from Volovik Paper 09, 14, 27):
  - In 3He-A, quantized vortices carry a topological gauge field that induces the
    ABJ anomaly: d_mu j^mu_B = (1/32pi^2) F_munu F~^munu
  - Vortex zero modes carry fractional baryon charge (bulk-defect index theorem)
  - KZ defect density: n_v ~ 1/xi_KZ^2 (codimension-2 vortices from pi_1(U(1))=Z)
  - CP violation from vortex-antivortex IMBALANCE, not bulk spectrum

Critical obstruction (N3-BDG-44):
  - This system is 3He-B class (fully gapped, BDI), NOT 3He-A (Fermi points, N_3=2)
  - N_3 = 0 -> no Fermi points -> no chiral anomaly in the 3He-A sense
  - BUT: U(1)_7 IS broken (S35), so vortex-type defects DO form via KZ
  - The question is: what CP violation mechanism operates in the 3He-B class?

Session: S53
Gate: VORTEX-NUCLEATION-53 (INFO)
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    xi_BCS, dt_transit, omega_att, Vol_SU3_Haar,
    eta_BBN_obs, N_cells, tau_fold, E_cond, Delta_0_GL,
    M_KK, M_KK_gravity, M_Pl_unreduced, PI,
    n_pairs, S_inst, N_dof_BCS, P_exc_kz,
    omega_PV, E_exc, v_terminal,
    rho_Lambda_obs, T_CMB_GeV, H_0_GeV,
    Delta_B3, xi_GL, barrier_0d,
    phi_CP
)

output_lines = []
def log(msg):
    print(msg)
    output_lines.append(msg)

log("=" * 80)
log("VORTEX-NUCLEATION-53: KZ Vortex Density and Topological Baryogenesis")
log("=" * 80)
log("")

# =============================================================================
# STEP 1: KZ correlation length xi_KZ
# =============================================================================
log("=" * 80)
log("STEP 1: KIBBLE-ZUREK CORRELATION LENGTH")
log("=" * 80)
log("")

# KZ scaling: xi_KZ = xi_0 * (tau_quench / tau_0)^{nu/(1+nu*z)}
# Mean-field BCS, model A dynamics: nu = 1/2, z = 2
# xi_0 = xi_BCS (coherence length)
# tau_quench = dt_transit (transit duration)
# tau_0 = 1/omega_att (microscopic relaxation time)

nu = 0.5            # mean-field BCS
z_dyn = 2           # model A (dissipative)
xi_0 = xi_BCS       # coherence length (M_KK^{-1})
tau_quench = dt_transit  # transit duration (M_KK^{-1})
tau_0 = 1.0 / omega_att  # microscopic time (M_KK^{-1})

kz_exponent = nu / (1.0 + nu * z_dyn)  # = 0.5 / (1+1) = 0.25
quench_ratio = tau_quench / tau_0

xi_KZ = xi_0 * quench_ratio**kz_exponent

log(f"Input parameters:")
log(f"  xi_0 = xi_BCS = {xi_0:.6f} M_KK^{{-1}}")
log(f"  tau_quench = dt_transit = {tau_quench:.10f} M_KK^{{-1}}")
log(f"  tau_0 = 1/omega_att = {tau_0:.6f} M_KK^{{-1}}")
log(f"  nu = {nu} (mean-field BCS)")
log(f"  z = {z_dyn} (model A, dissipative)")
log(f"")
log(f"KZ exponent: nu/(1+nu*z) = {kz_exponent:.4f}")
log(f"Quench ratio: tau_quench/tau_0 = {quench_ratio:.6f}")
log(f"  (quench_ratio < 1: SUDDEN QUENCH regime)")
log(f"")
log(f"xi_KZ = xi_0 * (tau_q/tau_0)^{kz_exponent:.2f}")
log(f"      = {xi_0:.6f} * {quench_ratio:.6f}^{kz_exponent:.2f}")
log(f"      = {xi_KZ:.6f} M_KK^{{-1}}")
log(f"")
log(f"xi_KZ / xi_BCS = {xi_KZ / xi_BCS:.6f}")
log(f"  (KZ length SHORTER than coherence length: confirms sudden quench)")
log("")

# Cross-check: in sudden quench regime (tau_q << tau_0), xi_KZ < xi_0
# This is the correct KZ behavior for fast quenches
if quench_ratio < 1.0:
    log(f"CONFIRMATION: tau_quench/tau_0 = {quench_ratio:.4f} < 1")
    log(f"  This is the SUDDEN QUENCH regime.")
    log(f"  S38 found P_exc = {P_exc_kz} (complete excitation).")
    log(f"  KZ formalism applies in its extreme limit: every mode excited.")
    log("")

# =============================================================================
# STEP 2: VORTEX DENSITY
# =============================================================================
log("=" * 80)
log("STEP 2: VORTEX DENSITY AND DEFECT DIMENSIONALITY")
log("=" * 80)
log("")

# Symmetry breaking: U(1)_7 broken by BCS condensate
# pi_1(U(1)) = Z -> codimension-2 vortices (winding number defects)
# In d dimensions: codim-2 defects are (d-2)-dimensional objects
# Density: n_v = 1/xi_KZ^2 (defects per transverse area)

# The internal space is SU(3) (8-dimensional manifold)
# U(1)_7 is a 1-dimensional subgroup -> orbit space S^1
# Vortices: codimension 2 in directions TRANSVERSE to the U(1)_7 orbit
# In 8D: codim-2 defects are 6D objects
# Vortex density per transverse area: n_v = 1/xi_KZ^2

# But the PHYSICAL vortex density is per unit volume of the full internal space
# Vortices are 6D sheets threading the 8D internal space
# Their length density (per transverse 2D area) is 1/xi_KZ^2

n_v_2D = 1.0 / xi_KZ**2  # per transverse area (M_KK^2)

log(f"Symmetry breaking: U(1)_7 (broken by BCS, S35)")
log(f"  pi_1(U(1)) = Z -> vortex-type defects (codimension 2)")
log(f"")
log(f"Internal manifold: SU(3) (dim = 8)")
log(f"  U(1)_7 orbit: dim = 1")
log(f"  Vortex core: codim = 2 -> dim(vortex) = 8 - 2 = 6")
log(f"  Vortices are 6-dimensional sheets in 8D SU(3)")
log(f"")
log(f"Transverse vortex density:")
log(f"  n_v(2D) = 1/xi_KZ^2 = {n_v_2D:.4f} M_KK^2")
log(f"")

# Total number of vortices in internal space
# Need the 2D transverse area through which vortices thread
# The relevant cross-section is the area in the 2 directions transverse to
# the U(1)_7 orbit and transverse to the vortex sheet

# For an 8D manifold with volume V_8 and vortex sheets of dimension 6:
# N_vortex ~ V_8 / (xi_KZ^2 * V_6_per_vortex)
# But V_6 per vortex ~ V_8 / L_transverse^2

# Better approach: the number of independent vortex nucleation events
# in the internal space is the volume in units of (xi_KZ)^8

# Actually, the KZ mechanism gives ONE defect per correlation volume:
# N_defect ~ V_total / xi_KZ^d for point defects in d dimensions
# For codimension-2 defects (line density in 2D): n ~ 1/xi_KZ^2 per transverse area

# The transverse area available is the 2D cross-section of SU(3)
# This is bounded by the SU(3) volume and the vortex sheet volume:
# V_perp_2D ~ Vol(SU(3)) / Vol(S^1 * codim-2 sheet)

# A cleaner approach: the number of vortex-antivortex pairs is
# N_v ~ (L_eff / xi_KZ)^2 where L_eff is the effective system size
# in the 2 transverse directions.

# For SU(3) with volume V_8 = Vol_SU3_Haar M_KK^{-8},
# the effective length scale in each direction is
# L_eff ~ V_8^{1/8} M_KK^{-1}

L_eff = Vol_SU3_Haar**(1.0/8.0)  # effective length in each direction (M_KK^{-1})
L_eff_2 = Vol_SU3_Haar**(1.0/4.0)  # effective 2D extent sqrt(A_perp)

log(f"Effective scales of SU(3):")
log(f"  Vol(SU(3)) = {Vol_SU3_Haar:.2f} (M_KK^{{-8}})")
log(f"  L_eff = V^{{1/8}} = {L_eff:.4f} M_KK^{{-1}}")
log(f"  L_eff_2 = V^{{1/4}} = {L_eff_2:.4f} M_KK^{{-1}} (2D extent)")
log(f"")

# Number of vortex-antivortex pairs in the transverse 2D cross section
N_vortex_pairs = (L_eff_2 / xi_KZ)**2
N_vortex_total = (L_eff / xi_KZ)**2  # using 1D effective size

log(f"Vortex count estimates:")
log(f"  Method 1 (V^{{1/4}}/xi_KZ)^2: N_v = {N_vortex_pairs:.2f}")
log(f"  Method 2 (V^{{1/8}}/xi_KZ)^2: N_v = {N_vortex_total:.2f}")
log(f"")

# BUT: critical constraint from 0D limit (S37)
# L/xi_BCS = 0.031 -> system is in the ZERO-DIMENSIONAL limit
# The system is smaller than one coherence length
# This means: at most O(1) vortex can fit

L_over_xi = 0.031  # from S37, confirmed S42

log(f"CRITICAL: 0D constraint")
log(f"  L/xi_BCS = {L_over_xi} (S37)")
log(f"  System is 0.031 coherence lengths across")
log(f"  L/xi_KZ = L/xi_BCS * (xi_BCS/xi_KZ) = {L_over_xi * (xi_BCS / xi_KZ):.4f}")
log(f"")
log(f"  A vortex core has size ~ xi_KZ. The entire system has size ~ 0.031 * xi_BCS.")
log(f"  L_system = 0.031 * {xi_BCS:.4f} = {0.031 * xi_BCS:.6f} M_KK^{{-1}}")
log(f"  xi_KZ = {xi_KZ:.6f} M_KK^{{-1}}")
log(f"  L_system / xi_KZ = {0.031 * xi_BCS / xi_KZ:.4f}")
log(f"")

L_system = L_over_xi * xi_BCS
ratio_L_xiKZ = L_system / xi_KZ

if ratio_L_xiKZ < 1.0:
    log(f"  L_system < xi_KZ: system is SMALLER than one KZ correlation volume")
    log(f"  MAXIMUM possible vortex count: N_v = 0 or 1 (quantum)")
    log(f"  Classical KZ vortex nucleation is IMPOSSIBLE in 0D")
    N_vortex_0D = 0
    log(f"")
    log(f"  N_v(0D) = 0 (no room for a vortex)")
else:
    N_vortex_0D = int(ratio_L_xiKZ**2)
    log(f"  N_v(0D) ~ (L/xi_KZ)^2 = {N_vortex_0D}")

log("")

# However: the 32-cell fabric has N_cells = 32 domains
# Each cell undergoes the transition independently
# Vortices form at BOUNDARIES between cells
# Number of vortex-like boundary defects:

# On a 32-cell Voronoi tessellation on S^3 (3D boundary of SU(3)):
# Number of cell-cell boundaries ~ (d+1)/2 * N_cells for a d-dimensional tessellation
# In 3D: ~ 2 * N_cells = 64 boundaries
# In 8D: each cell has many more neighbors

# For a random Voronoi tessellation in d dimensions:
# average number of faces per cell ~ 2d + 2 (for large d)
# Number of boundaries = N_cells * n_faces / 2

d_internal = 8
n_faces_per_cell = 2 * d_internal + 2  # ~ 18 for d=8
N_boundaries = int(N_cells * n_faces_per_cell / 2)

log(f"32-cell fabric (S42):")
log(f"  Each cell is a KZ domain that transitions independently")
log(f"  Phase mismatch at boundaries -> vortex-like defects")
log(f"  Faces per cell (d={d_internal}): ~ {n_faces_per_cell}")
log(f"  Total boundaries: N_cells * n_faces / 2 = {N_boundaries}")
log(f"")
log(f"  Each boundary has probability ~ 1/3 of hosting a vortex")
log(f"  (KZ: random phase => winding probability ~ 1/pi ~ 1/3)")
log(f"")

p_vortex_at_boundary = 1.0 / np.pi  # Kibble-Zurek probability
N_vortex_fabric = N_boundaries * p_vortex_at_boundary

log(f"  p(vortex at boundary) = 1/pi = {p_vortex_at_boundary:.4f}")
log(f"  N_vortex(fabric) = N_boundaries * p = {N_vortex_fabric:.1f}")
log(f"")

# =============================================================================
# STEP 3: TOPOLOGICAL BARYOGENESIS ASSESSMENT
# =============================================================================
log("=" * 80)
log("STEP 3: ABJ ANOMALY AND CP VIOLATION IN VORTEX CORES")
log("=" * 80)
log("")

# The ABJ anomaly formula (Paper 09):
# d_mu j^mu_B = (1/32pi^2) F_munu F~^munu
# In 3He-A: the "gauge field" is the phase gradient of the order parameter
# F_munu = d_mu A_nu - d_nu A_mu where A = grad(theta)

# CRITICAL OBSTRUCTION: N3-BDG-44 established N_3 = 0
# System is 3He-B class (fully gapped), NOT 3He-A (Fermi points)
# The chiral anomaly requires Fermi points (Weyl nodes) to produce spectral flow

log(f"Obstruction analysis:")
log(f"")
log(f"1. N_3 invariant (S44 N3-BDG-44):")
log(f"   N_3 = 0 (system is 3He-B, not 3He-A)")
log(f"   The ABJ anomaly in Volovik's sense requires N_3 != 0")
log(f"   Spectral flow through zero energy: NOT AVAILABLE in gapped spectrum")
log(f"   min|E_BdG| at fold = 0.830 M_KK (finite gap)")
log(f"")
log(f"2. phi_CP structural zero (S52 ETA-B-52):")
log(f"   phi_CP = {phi_CP} (3 independent proofs)")
log(f"   BDI symmetry class: T^2 = +1 forces all matrix elements real")
log(f"   No CP violation in BULK spectrum")
log(f"")
log(f"3. Vortex core CP violation (the Volovik mechanism):")
log(f"   In 3He-A: vortex core has BOUND STATES at zero energy")
log(f"   These create local chirality imbalance: N_L - N_R != 0")
log(f"   CP violation from TOPOLOGY of vortex configuration")
log(f"")

# For a single vortex in 3He-A (Paper 09):
# Each vortex of winding w carries |w| zero-energy bound states
# The zero mode carries charge Q_zero = q_0 / integer

# In the BCS on SU(3) (3He-B class):
# Pfaffian Z_2 = -1 (nontrivial, S35)
# This protects gap TOPOLOGY but not vacuum energy
# Vortex core bound states exist (Caroli-de Gennes type)
# BUT: they are at FINITE energy (minigap ~ Delta^2/E_F),
# not at zero energy (because system is fully gapped)

# The Caroli-de Gennes bound state energy in a vortex core:
# E_n = (n + 1/2) * Delta^2 / E_F for a BCS vortex
# In our system: E_F ~ 1 M_KK, Delta ~ Delta_0_GL = 0.770

E_F_eff = 1.0  # M_KK (Fermi energy scale)  # (local)
E_CdG_0 = 0.5 * Delta_0_GL**2 / E_F_eff  # lowest CdG bound state

log(f"Caroli-de Gennes bound states in vortex core:")
log(f"  E_n = (n+1/2) * Delta^2 / E_F")
log(f"  Delta = {Delta_0_GL:.4f} M_KK")
log(f"  E_F ~ {E_F_eff:.1f} M_KK")
log(f"  E_0 = {E_CdG_0:.4f} M_KK (lowest bound state)")
log(f"  E_0 / Delta = {E_CdG_0 / Delta_0_GL:.4f}")
log(f"")
log(f"  These are FINITE energy states, not zero modes.")
log(f"  No spectral flow -> no ABJ anomaly in the standard sense.")
log("")

# =============================================================================
# STEP 4: ETA_B ESTIMATE
# =============================================================================
log("=" * 80)
log("STEP 4: BARYON ASYMMETRY ESTIMATE")
log("=" * 80)
log("")

# Even without the ABJ anomaly, estimate the maximum possible eta_B
# from the topological mechanism:
#
# eta_B ~ (n_vortex / s) * (CP per vortex) * (B per event)
#
# where s is the entropy density

# Method A: If ABJ mechanism worked (3He-A class — COUNTERFACTUAL)
# eta_B ~ (1/s) * integral of (1/32pi^2) F F~ over vortex volume
# For a single vortex with winding w=1:
# integral F F~ = 2*pi * (topological charge) = 2*pi * 1
# So: eta_B_per_vortex = 1/(16*pi) per vortex

eta_B_per_vortex_ABJ = 1.0 / (16 * np.pi)

log(f"Method A: ABJ anomaly (COUNTERFACTUAL — requires N_3 != 0)")
log(f"  eta_B per vortex = 1/(16*pi) = {eta_B_per_vortex_ABJ:.6f}")
log(f"  This is the maximum CP violation per vortex IF the ABJ anomaly operated.")
log(f"")

# The entropy density at reheating:
# s ~ g_* * T_RH^3 / (2*pi^2/45)
# But in this framework, the "entropy" is the GGE entropy
# S_GGE = sum_k [-n_k ln(n_k) - (1-n_k)ln(1-n_k)] over N_dof modes

# From S38: n_Bog = 0.9986 per mode -> S per mode ~ -0.999*ln(0.999) - 0.001*ln(0.001) ~ 0.01
# Total S_GGE ~ N_dof * 0.01 ~ 0.08
# But the "photon entropy" after reheating is much larger

# Physical approach: eta_B = n_B / n_gamma
# n_B ~ N_vortex * (B per vortex) / V_total
# n_gamma ~ T_RH^3 / pi^2 (in natural units)

# N_vortex from fabric: ~91 boundary vortices (step 2)
# V_total = N_cells * Vol(SU(3)) = 32 * 1349.74 M_KK^{-8}

V_total = N_cells * Vol_SU3_Haar
N_v_total = N_vortex_fabric  # ~91

log(f"Method B: Fabric vortex density approach")
log(f"  N_vortex(fabric) = {N_v_total:.1f}")
log(f"  V_total = N_cells * Vol(SU(3)) = {V_total:.1f} M_KK^{{-8}}")
log(f"")

# For the CP violation per vortex in 3He-B class:
# There is NO spectral flow (N_3 = 0), so the CP violation must come from
# a different mechanism. The only candidate is:
#
# CP violation from vortex-antivortex ASYMMETRY in the random KZ nucleation
# The KZ mechanism produces equal numbers of vortices and antivortices ON AVERAGE
# but with statistical fluctuations delta_N ~ sqrt(N_v)

delta_N_v = np.sqrt(N_v_total)

log(f"Vortex-antivortex imbalance:")
log(f"  <N_v> = <N_anti-v> = N_total/2 = {N_v_total/2:.1f}")
log(f"  delta(N_v - N_anti-v) ~ sqrt(N_total) = {delta_N_v:.2f}")
log(f"  Fractional imbalance: delta/N = 1/sqrt(N) = {1.0/np.sqrt(N_v_total):.4f}")
log(f"")

# The baryon number per vortex in the Volovik mechanism:
# For a vortex with winding w=1 and Fermi point charge N_3:
# Delta B = N_3 * w (from index theorem)
# For N_3 = 0 (our case): Delta B = 0 per vortex

Delta_B_per_vortex = 0  # N_3 = 0 -> no baryon number per vortex

log(f"Baryon number per vortex:")
log(f"  Delta_B = N_3 * w = 0 * 1 = {Delta_B_per_vortex}")
log(f"  N_3 = 0 (3He-B class, S44)")
log(f"  The index theorem gives ZERO baryon creation per vortex.")
log(f"")

# Even if we use the statistical imbalance AND assign maximal B per vortex:
eta_B_maximal = delta_N_v / V_total  # vortex density from imbalance
# This is in M_KK^8 units; need to convert to dimensionless ratio

# The relevant ratio is n_B / n_gamma
# n_B ~ delta_N_v * (1 baryon per vortex) / V_4D
# But we need to relate internal space volume to 4D volume at reheating

# In the framework, the internal space volume sets the compactification scale:
# V_6 ~ 1/M_KK^6 (6D Calabi-Yau volume)
# n_B(4D) = n_B(10D) / V_6

# Better: the baryon number is an EXTENSIVE quantity in 4D
# Each Hubble volume contains N_vortex vortices at the transition
# Entropy per Hubble volume: S ~ (T_RH / H)^3 * (2*pi^2/45) * g_*

# For the framework: T_RH ~ E_exc / N_dof (S38 estimate)
T_RH_est = E_exc / N_dof_BCS  # M_KK units = 7.58 M_KK (huge)

# In physical units:
T_RH_GeV = T_RH_est * M_KK  # GeV

log(f"Reheating temperature estimate:")
log(f"  T_RH ~ E_exc / N_dof = {T_RH_est:.3f} M_KK = {T_RH_GeV:.2e} GeV")
log(f"")

# Entropy density at T_RH:
g_star = 106.75  # SM degrees of freedom (local)
s_RH = (2 * np.pi**2 / 45) * g_star * T_RH_GeV**3  # GeV^3

# Baryon density: even with maximal assignment (1 baryon per vortex)
# n_B ~ delta_N_v / V_Hubble where V_Hubble ~ H^{-3}

# But the REAL obstruction is that Delta_B = 0 per vortex (N_3 = 0)
# So eta_B = 0 from the Volovik mechanism in 3He-B class

eta_B_Volovik = 0.0  # (local)

log(f"RESULT:")
log(f"  eta_B(Volovik mechanism) = {eta_B_Volovik}")
log(f"  Reason: N_3 = 0 -> Delta_B per vortex = 0 -> no baryogenesis")
log(f"  eta_B(observed) = {eta_BBN_obs:.2e}")
log(f"")

# =============================================================================
# STEP 5: ALTERNATIVE TOPOLOGICAL ROUTES
# =============================================================================
log("=" * 80)
log("STEP 5: ALTERNATIVE TOPOLOGICAL BARYOGENESIS ROUTES")
log("=" * 80)
log("")

# Even though the ABJ anomaly is structurally absent (N_3=0),
# there are other topological mechanisms to consider:

log(f"Route 1: Spectral flow through minigap (3He-B class)")
log(f"  In 3He-B, the minigap E_CdG provides a barrier to spectral flow.")
log(f"  At finite temperature T > E_CdG, thermal activation can produce")
log(f"  baryon number violation at rate ~ exp(-E_CdG/T).")
log(f"  E_CdG = {E_CdG_0:.4f} M_KK")
log(f"  T_GGE(B2) = 0.668 M_KK (S43 GGE-TEMP-43)")
T_GGE_B2 = 0.668  # NOTE: B2 sector GGE temperature (S43 GGE-TEMP-43), not in canonical_constants — candidate for promotion
rate_thermal = np.exp(-E_CdG_0 / T_GGE_B2)
log(f"  exp(-E_CdG/T_B2) = {rate_thermal:.4f}")
log(f"  Rate is O(1): thermal activation UNSUPPRESSED at GGE temperature.")
log(f"  BUT: phi_CP = 0 -> even with spectral flow, CP violation = 0.")
log(f"  CLOSED: CP is the bottleneck, not B violation.")
log(f"")

log(f"Route 2: Gravitational baryogenesis (Davoudiasl-Hambye-Riotto)")
log(f"  Uses coupling (1/M_*^2) * (d_mu R) * j^mu_B")
log(f"  During the transit, R(tau) is changing -> d_t R != 0")
log(f"  This is EXTERNAL to the BCS system (requires GR)")
log(f"  Not computable within the 0D BCS framework alone.")
log(f"  STATUS: OPEN (requires Friedmann coupling)")
log(f"")

log(f"Route 3: Spontaneous baryogenesis from U(1)_7 condensate")
log(f"  The BCS condensate carries K_7 charge +-1/2 (S35)")
log(f"  N_pair = 1 (S53)")
log(f"  If K_7 charge = baryon number (or lepton number):")
log(f"  Delta B = K_7 charge * N_pair = 1/2 * 1 = 1/2")
log(f"  eta_B ~ Delta B / s ~ (1/2) / (g_* T^3)")
log(f"")
log(f"  BUT: K_7 charge is NOT baryon number.")
log(f"  K_7 is generator of U(1) subset SU(3), acting on INTERNAL space.")
log(f"  Baryon number is a 4D quantum number.")
log(f"  Identifying K_7 = B requires a mapping not established.")
log(f"  STATUS: OPEN (requires K_7 -> B identification)")
log(f"")

log(f"Route 4: KZ domain wall network")
log(f"  32-cell fabric has ~{N_boundaries} boundaries with phase mismatch")
log(f"  Each boundary is a domain wall in the internal space")
log(f"  Domain walls in 4D can trap fermion zero modes")
log(f"  But: this is a DIFFERENT topology from vortices")
log(f"  Codimension-1 defects from discrete symmetry breaking")
log(f"  STATUS: REQUIRES separate computation (domain wall spectrum)")
log(f"")

# =============================================================================
# STEP 6: QUANTITATIVE SUMMARY
# =============================================================================
log("=" * 80)
log("STEP 6: QUANTITATIVE SUMMARY")
log("=" * 80)
log("")

log(f"KEY NUMBERS:")
log(f"  xi_KZ = {xi_KZ:.6f} M_KK^{{-1}} (KZ correlation length)")
log(f"  xi_KZ / xi_BCS = {xi_KZ / xi_BCS:.6f} (shorter: sudden quench)")
log(f"  n_v(2D) = 1/xi_KZ^2 = {n_v_2D:.4f} M_KK^2 (transverse vortex density)")
log(f"  N_vortex(fabric) = {N_vortex_fabric:.1f} (from 32-cell boundaries)")
log(f"  L_system/xi_KZ = {ratio_L_xiKZ:.4f} (< 1: no room for classical vortex)")
log(f"  N_3 = 0 (3He-B class, no Fermi points)")
log(f"  Delta_B per vortex = 0 (index theorem)")
log(f"  phi_CP = 0 (3 proofs, S52)")
log(f"  eta_B(topological) = 0 (structural)")
log(f"  eta_B(observed) = {eta_BBN_obs:.2e}")
log(f"")

log(f"OBSTRUCTIONS (4 independent):")
log(f"  1. N_3 = 0: No Fermi points -> no ABJ anomaly -> no B violation per vortex")
log(f"  2. phi_CP = 0: No bulk CP violation (BDI T^2=+1)")
log(f"  3. 0D limit: L/xi_KZ = {ratio_L_xiKZ:.4f} < 1, no room for classical vortex")
log(f"  4. N_pair = 1: Only 1 Cooper pair, no macroscopic condensate for phase winding")
log(f"")

log(f"VOLOVIK MECHANISM STATUS:")
log(f"  The ABJ anomaly in vortex cores (Paper 09) is the canonical mechanism for")
log(f"  topological baryogenesis in superfluid systems. It requires:")
log(f"    (a) Fermi points (N_3 != 0) for spectral flow")
log(f"    (b) CP-violating vortex textures for matter-antimatter asymmetry")
log(f"    (c) Sufficient system size for vortex nucleation")
log(f"    (d) Macroscopic condensate for coherent phase winding")
log(f"")
log(f"  This framework fails ALL FOUR requirements:")
log(f"    (a) N_3 = 0 (3He-B class)")
log(f"    (b) phi_CP = 0 (BDI structural zero)")
log(f"    (c) L/xi_KZ < 1 (0D limit)")
log(f"    (d) N_pair = 1 (no macroscopic condensate)")
log(f"")
log(f"  This is a STRUCTURAL closure of topological baryogenesis in the")
log(f"  internal space. External mechanisms (gravitational baryogenesis,")
log(f"  K_7 -> B mapping) remain open but require physics beyond the")
log(f"  BCS condensate on SU(3).")
log(f"")

# =============================================================================
# GATE VERDICT
# =============================================================================
log("=" * 80)
log("GATE VERDICT: VORTEX-NUCLEATION-53")
log("=" * 80)
log("")
log(f"INFO (as pre-registered).")
log(f"")
log(f"n_v(2D) = {n_v_2D:.4f} M_KK^2 (transverse KZ vortex density)")
log(f"N_vortex(fabric) = {N_vortex_fabric:.1f} (32-cell boundary defects)")
log(f"")
log(f"Baryogenesis viability: STRUCTURALLY EXCLUDED (4 obstructions)")
log(f"  The Volovik ABJ vortex mechanism (Paper 09) is inapplicable to 3He-B class.")
log(f"  The 0D limit prevents classical vortex nucleation.")
log(f"  phi_CP = 0 prevents CP violation even if vortices existed.")
log(f"  N_pair = 1 prevents macroscopic phase winding.")
log(f"")
log(f"Surviving routes: gravitational baryogenesis (external), K_7->B (unestablished).")
log(f"")
log(f"Classification: PARTICLE (baryogenesis mechanism). Phononic content: NONE.")
log(f"  The ABJ anomaly is a single-particle spectral flow effect, not a collective")
log(f"  phononic phenomenon. The vortex nucleation is a topological defect in the")
log(f"  order parameter, which is the condensate (phononic), but the B violation")
log(f"  mechanism operates on individual quasiparticle zero modes (particle).")

# =============================================================================
# PLOT
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("VORTEX-NUCLEATION-53: KZ Defects and Baryogenesis", fontsize=14, fontweight='bold')

# Panel 1: xi_KZ vs tau_quench/tau_0
ax1 = axes[0, 0]
ratios = np.logspace(-3, 1, 200)
xi_KZ_sweep = xi_0 * ratios**kz_exponent
ax1.loglog(ratios, xi_KZ_sweep, 'b-', linewidth=2, label=r'$\xi_{KZ} = \xi_0 \cdot (t_q/t_0)^{1/4}$')
ax1.axvline(quench_ratio, color='r', linestyle='--', linewidth=1.5, label=f'Framework: $t_q/t_0$ = {quench_ratio:.4f}')
ax1.axhline(xi_BCS, color='gray', linestyle=':', label=f'$\\xi_{{BCS}}$ = {xi_BCS:.3f}')
ax1.axhline(xi_KZ, color='r', linestyle=':', alpha=0.5)
ax1.set_xlabel(r'$\tau_{quench} / \tau_0$', fontsize=12)
ax1.set_ylabel(r'$\xi_{KZ}$ ($M_{KK}^{-1}$)', fontsize=12)
ax1.set_title('KZ Correlation Length', fontsize=12)
ax1.legend(fontsize=9)
ax1.set_ylim(0.01, 10)
ax1.grid(True, alpha=0.3)

# Panel 2: Vortex density
ax2 = axes[0, 1]
categories = ['n_v(2D)\n(M_KK^2)', 'N_v(fabric)\n(32-cell)', 'N_v(0D)\n(per cell)', r'$\delta N_{v-\bar{v}}$'+'\n(fluct.)']
values = [n_v_2D, N_vortex_fabric, N_vortex_0D, delta_N_v]
colors = ['steelblue', 'coral', 'gray', 'gold']
bars = ax2.bar(categories, values, color=colors, edgecolor='black', linewidth=0.5)
for bar, val in zip(bars, values):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             f'{val:.1f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
ax2.set_ylabel('Count / Density', fontsize=12)
ax2.set_title('Vortex Counts by Method', fontsize=12)
ax2.grid(True, alpha=0.3, axis='y')

# Panel 3: Obstruction diagram
ax3 = axes[1, 0]
obstructions = ['N_3 = 0\n(no ABJ)', r'$\phi_{CP}$ = 0'+'\n(BDI)', 'L < xi_KZ\n(0D limit)', 'N_pair = 1\n(no macro)']
severity = [1, 1, 1, 1]  # all structural (max severity)
barcolors = ['#d32f2f', '#d32f2f', '#d32f2f', '#d32f2f']
bars3 = ax3.barh(obstructions, severity, color=barcolors, edgecolor='black', linewidth=0.5, height=0.5)
ax3.set_xlim(0, 1.5)
ax3.set_xlabel('Structural (1 = impossible)', fontsize=12)
ax3.set_title('4 Independent Obstructions', fontsize=12)
for i, bar in enumerate(bars3):
    ax3.text(1.05, bar.get_y() + bar.get_height()/2., 'CLOSED',
             ha='left', va='center', fontsize=10, fontweight='bold', color='#d32f2f')
ax3.axvline(1.0, color='black', linestyle='-', linewidth=0.5)

# Panel 4: eta_B comparison
ax4 = axes[1, 1]
log_eta_obs = np.log10(eta_BBN_obs)  # ~ -9.21
# Even the most generous estimate gives eta_B = 0
# Show comparison of different estimates

labels = ['Observed\neta_B', 'ABJ\n(counterfactual)', 'Fabric\n(stat. fluct.)', 'Actual\n(N_3=0)']
# counterfactual: if ABJ worked with max vortices
eta_counterfactual = N_vortex_fabric * eta_B_per_vortex_ABJ / (g_star * (T_RH_est * M_KK)**3 / (2 * np.pi**2 / 45))
eta_fabric_fluct = delta_N_v / (g_star * (T_RH_est * M_KK)**3 / (2 * np.pi**2 / 45))

log_vals = [log_eta_obs,
            np.log10(max(eta_counterfactual, 1e-300)),
            np.log10(max(eta_fabric_fluct, 1e-300)),
            -300]  # literally zero

# Replace -inf or very negative with a floor for plotting
plot_vals = [log_eta_obs,
             np.log10(max(eta_counterfactual, 1e-200)),
             np.log10(max(eta_fabric_fluct, 1e-200)),
             -20]  # represent "zero" as very small

barcolors4 = ['green', 'orange', 'orange', 'red']
bars4 = ax4.bar(labels, plot_vals, color=barcolors4, edgecolor='black', linewidth=0.5)
ax4.set_ylabel(r'$\log_{10}(\eta_B)$', fontsize=12)
ax4.set_title(r'Baryon Asymmetry: $\eta_B = n_B/n_\gamma$', fontsize=12)
ax4.axhline(log_eta_obs, color='green', linestyle='--', alpha=0.5, label=f'Observed: {eta_BBN_obs:.2e}')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), 's53_vortex_nucleation.png'), dpi=150)
plt.close()
log("")
log("Plot saved: s53_vortex_nucleation.png")

# Save output
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 's53_vortex_nucleation_output.txt')
with open(output_path, 'w') as f:
    f.write('\n'.join(output_lines))
print(f"\nOutput saved: {output_path}")
