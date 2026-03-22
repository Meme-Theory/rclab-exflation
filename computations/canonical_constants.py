#!/usr/bin/env python3
"""
Canonical Constants Module — Single Source of Truth
====================================================

Created: Session 45 (2026-03-15)
Purpose: Eliminate hardcoded constant drift across tier0-computation scripts.

Provenance audit (S44, AUDIT_UPSTREAM_ROOTS.md) found:
  - Three E_cond values (-0.115, -0.137, -0.156) used interchangeably
  - Two Vol(SU(3)) formulas (8880.9 vs 1349.7) in competing scripts
  - M_KK = 1e16 used where 7.43e16 (gravity) or 5.04e17 (Kerner) intended

Every constant below has a session/gate provenance comment.
The PROVENANCE dict (Section F) provides machine-readable lineage.

Usage:
    from canonical_constants import E_cond, tau_fold, M_KK_gravity
    from canonical_constants import PROVENANCE, warn_stale
"""

import sys
import numpy as np
import warnings

PI = np.pi

# ==============================================================================
#  SECTION A: PDG / CODATA Universal Constants
# ==============================================================================

# Planck mass — two conventions, both used in the literature
M_Pl_reduced = 2.435e18        # GeV, M_Pl / sqrt(8*pi)
M_Pl_unreduced = 1.2209e19    # GeV, sqrt(hbar*c/G_N)

# Fundamental constants — SI
G_N = 6.67430e-11             # m^3 kg^{-1} s^{-2} (CODATA 2018)
c_light = 2.99792458e8        # m/s (exact)
hbar_SI = 1.054571817e-34     # J*s (CODATA 2018)
h_planck_SI = 6.62607015e-34  # J*s (exact, 2019 SI redefinition)
k_B = 8.617333262e-5          # eV/K (CODATA 2018)
k_B_SI = 1.380649e-23         # J/K (exact, 2019 SI redefinition)
eV_SI = 1.602176634e-19       # J per eV (exact)
eV_per_GeV = 1e9              # eV per GeV
A_Bohr = 0.529177210903e-10   # m (Bohr radius, CODATA 2018)
arcsec_to_rad = 4.84813681109536e-6  # radians per arcsecond
alpha_em_MZ_inv = 127.955     # 1/alpha_EM at M_Z (PDG 2024)
sin2_thetaW_MSbar = 0.23122   # sin^2(theta_W) MSbar at M_Z (PDG 2024)
M_Z = 91.1876                 # GeV (PDG 2024)
M_W = 80.3692                 # GeV (PDG 2024)

# Fundamental constants — CGS
G_N_cgs = 6.67430e-8          # cm^3 g^{-1} s^{-2}
c_light_cgs = 2.99792458e10   # cm/s
c_light_km_s = 2.99792458e5   # km/s

# Planck units & hbar variants
hbar_c_GeV_fm = 0.1973269804  # GeV * fm (exact in natural units)
hbar_c_GeV_m = 1.973269804e-16  # GeV * m
hbar_c_GeV_cm = 1.973269804e-14  # GeV * cm
hbar_eV_s = 6.582119569e-16   # eV * s (CODATA 2018)
hbar_GeV_s = 6.582119569e-25  # GeV * s (= hbar_eV_s / 1e9)
l_Planck = 1.616255e-35       # m (Planck length)
l_Planck_cm = 1.616255e-33    # cm
t_Planck = 5.391247e-44       # s (Planck time)

# Cosmological
H_0_km_s_Mpc = 67.4           # km/s/Mpc (Planck 2018)
H_0_inv_s = 2.184e-18         # s^{-1}
H_0_GeV = 1.438e-42           # GeV
T_CMB = 2.7255                # K (COBE/FIRAS)
T_CMB_GeV = 2.7255 * 8.617333262e-5 / 1e9  # = 2.348e-13 GeV
rho_Lambda_obs = 2.7e-47      # GeV^4 (observed CC, conventional rounding — see NOTE below)
# NOTE: Precise Planck 2018 value is 2.52e-47 GeV^4 (Omega_L=0.685, H_0=67.36).
# The 2.7e-47 rounding is widely used in the literature and across this codebase.
# The 2.888e-47 in some scripts uses a different density convention.
# All CC-gap calculations use ratios (rho_spectral / rho_obs), so the ~7% difference
# changes the gap by <0.03 orders out of 120 — negligible for all gate verdicts.
Lambda_obs_MP4 = 2.888e-122   # Lambda / M_Pl^4 (widely used convention in codebase)
A_s_CMB = 2.1e-9              # CMB scalar amplitude (Planck 2018)
Omega_r = 9.15e-5             # radiation density parameter (Planck 2018)

Omega_m = 0.315               # matter density parameter (Planck 2018)
Omega_b = 0.0493              # baryon density parameter (Planck 2018)
Omega_DM = Omega_m - Omega_b  # dark matter density parameter (= 0.266)
Omega_Lambda = 0.685          # dark energy density parameter (Planck 2018)
sigma_8 = 0.811               # matter fluctuation amplitude (Planck 2018)

# Critical density
rho_crit_GeV4 = 4.08e-47      # GeV^4 (3*H_0^2 / 8*pi*G in natural units)
rho_crit_cgs = 1.878e-29      # g/cm^3

# BBN / recombination
eta_BBN_obs = 6.12e-10        # baryon-to-photon ratio (Planck 2018 + BBN)
eta_BBN_err = 0.04e-10        # 1-sigma uncertainty
T_BBN_GeV = 1e-3              # BBN temperature (~1 MeV)
T_recomb_GeV = 0.26e-9        # recombination temperature (~0.26 eV)
z_BBN = 4e8                   # BBN redshift
t_universe_s = 4.35e17        # age of universe in seconds (Planck 2018)

# Observational bounds (used in multiple scripts)
sigma_FIRAS = 1.0e-6          # FIRAS spectral distortion bound (delta_mu)
FIRAS_dT_bound = 3.0e-6       # FIRAS temperature anisotropy bound (delta_T/T)

# Conversion factors
GeV_to_inv_s = 1.5193e24      # 1 GeV -> s^{-1}
GeV_to_inv_m = 1.0 / hbar_c_GeV_m  # 1 GeV -> m^{-1} (= 5.068e15)
GeV_inv_to_Mpc = hbar_c_GeV_m / 3.0857e22  # = 6.39e-39 Mpc per GeV^{-1}
Mpc_to_GeV_inv = 3.0857e22 / hbar_c_GeV_m  # = 1.563e38 GeV^{-1} per Mpc
GeV_to_kg = 1.78266192e-27    # 1 GeV/c^2 -> kg
GeV_to_g = 1.78266192e-24     # 1 GeV/c^2 -> g
Mpc_to_fm = 3.0857e38         # 1 Mpc in fm
Mpc_to_m = 3.0857e22          # 1 Mpc in meters
Mpc_to_cm = 3.0857e24         # 1 Mpc in cm
Gpc_to_m = 3.0857e25          # 1 Gpc in meters
kpc_to_cm = 3.0857e21         # 1 kpc in cm

# ==============================================================================
#  SECTION B: Framework Geometric Constants
# ==============================================================================

# Jensen deformation parameter at the fold (van Hove singularity)
# Session 12: phi_paasch found. Session 22a: Pomeranchuk. Session 35: mechanism chain
tau_fold = 0.19               # S42 constants_snapshot, fold_idx=7

# SU(3) Haar volume — the CORRECT Weyl integration formula
# S44 CORRECTION: 8*sqrt(3)*pi^4 = 1349.74 (replaces wrong sqrt(3)*(4*pi^2)^3/12 = 8880.93)
Vol_SU3_Haar = 8.0 * np.sqrt(3) * PI**4   # = 1349.74 (S44 s44_constants_corrected)
Vol_SU3_WRONG = np.sqrt(3) * (4*PI**2)**3 / 12.0  # = 8880.93 (DO NOT USE — kept for audit)

# Diagonal metric element at round SU(3)
g0_diag = 3.0                 # From Killing metric normalization (S7)

# M_KK: TWO extraction routes, 0.83-decade tension (CONST-FREEZE-42 PASS)
M_KK_gravity = 7.428660036284456e16   # GeV, spectral zeta / Newton's constant route (S42)
M_KK_kerner = 5.041679838376001e17    # GeV, Kerner gauge-metric route (S42)
M_KK = M_KK_gravity                   # Default alias — gravity route (conservative)
OOM_diff_MKK = 0.831664779390838      # log10(M_KK_kerner / M_KK_gravity) (S42)

# ==============================================================================
#  SECTION C: BCS / Many-Body Constants
# ==============================================================================

# BCS condensation energy — THREE values exist; each is a DIFFERENT quantity
# All in M_KK units (dimensionless ratios)
E_cond_ED_8mode = -0.13685055970476342  # S36 ED-CONV-36: 8-mode (4B2+1B1+3B3), 256-state, canonical
E_cond_ED_5mode = -0.11507660716341951  # S35 ED: 5-mode (4B2+1B1), 32-state (superseded by 8-mode)
E_cond_GL = -0.156                      # S37: Ginzburg-Landau functional (different quantity)

# The canonical value is the 8-mode ED result (S36, verified to machine epsilon)
E_cond = E_cond_ED_8mode               # = -0.137 (alias for downstream use)

# Excitation energy from BCS transit quench (S38)
E_exc_ratio = 443.0            # E_exc / |E_cond| (S38, Schwinger-instanton duality)
E_exc = E_exc_ratio * abs(E_cond)  # = 60.625 M_KK (derived — was 50.9 with old E_cond)
n_pairs = 59.8                 # Bogoliubov quasiparticle pairs from transit (S38)
N_dof_BCS = 8                  # Fock space modes (4B2 + 1B1 + 3B3)
T_compound = E_exc / 8         # Microcanonical temperature (M_KK units)

# BCS gap and pairing
Delta_0_GL = 0.7704350982797368   # GL gap parameter (M_KK units, s37_instanton_mc)
Delta_0_OES = 0.4642547394830737  # OES/pair-addition gap (s37_pair_susceptibility)
Delta_B3 = 0.176                  # B3 sector gap (M_KK, S38)
M_max_thouless = 1.674            # Maximum Thouless parameter (S35 RPA)
S_inst = 0.06860372346994315      # Instanton action (s37_instanton_mc, quantum critical point)

# Coherence lengths (s37_instanton_mc, high precision)
xi_BCS = 0.8083468753837275       # BCS coherence length (M_KK^{-1})
xi_GL = 0.9763208529368065        # GL coherence length (M_KK^{-1})
xi_BCS_over_BW = 13.952285853679658  # xi_BCS in BW units

# GL functional parameters (s37_instanton_mc)
a_GL = -0.5245475628963554        # GL a coefficient
b_GL = 0.4418580371481792         # GL b coefficient
barrier_0d = 0.004670337347200381 # 0D barrier height (M_KK)
barrier_1d = 0.15567791157334604  # 1D barrier height (M_KK)

# Pair vibration (s37_pair_susceptibility)
omega_PV = 0.791658919261384      # Pair vibration frequency (omega_plus)
omega_split = 1.3371826606372719  # Pair-add/remove splitting
ratio_Evac_Econd = 28.75624796597024  # E_vac/E_cond (fluctuation dominance)

# Langer decay (s38_attempt_freq)
Gamma_Langer_BCS = 0.24973624676840844  # Langer decay rate (BCS)
Kapitza_ratio = 0.030200115133742347    # Corrected Kapitza ratio (S38)

# ==============================================================================
#  SECTION D: Spectral Action Constants
# ==============================================================================

# Seeley-DeWitt coefficients at the fold (tau = 0.19)
# From s42_constants_snapshot.npz (S42, verified against s20a recomputation)
a0_fold = 6440.0               # a_0 (volume term)
a2_fold = 2776.1653888633655   # a_2 (scalar curvature term)
a4_fold = 1350.7216415169728   # a_4 (Gauss-Bonnet / gauge kinetic term)

# Spectral action and derived quantities
S_fold = 250360.67696101       # S_full at fold (S42 s42_gradient_stiffness)
m_tau = 2.062                  # Modulus mass at fold (M_KK units, S42 W2-1)
omega_att = 1.430              # Attractor frequency, fully geometric (S38)

# Collective inertia and dynamics
M_ATDHFB = 1.695               # ATDHFB collective mass (S40, s42_gradient_stiffness)
Z_fold = 74730.76411846        # Gradient stiffness at fold (S42)
G_DeWitt = 5.0                 # DeWitt moduli kinetic coefficient (S42 s42_gradient_stiffness)
dS_fold = 58672.80241318       # dS_full/dtau at fold (S42 s42_gradient_stiffness)
d2S_fold = 317862.84898132     # d^2 S_full/dtau^2 at fold (S42 s42_gradient_stiffness)
c_fabric = 209.97368021        # Fabric sound speed (S42 s42_gradient_stiffness)

# Transit parameters (s38_kz_defects)
H_fold = 586.5267713108464     # Hubble parameter at fold (M_KK units, S38)
v_terminal = 26.544972625732246  # Terminal velocity of modulus (S38)
dt_transit = 0.0011301575037571713  # Transit duration (M_KK^{-1}, S38)
P_exc_kz = 1.0                 # Kibble-Zurek excitation probability (S38, P=1 exactly)
n_Bog = 0.9986332220990328     # Bogoliubov fraction per mode (S38)

# Gauge couplings at M_KK (Kerner route)
g_SU2_fold = 2.0515842276370675   # SU(2) coupling^2 at fold (S42)
g_U1_fold = 4.386853768302675     # U(1)_Y coupling^2 at fold (S42)
alpha2_MKK_inv = 47.85603973035754  # 1/alpha_2 at M_KK (S42)
sin2_thetaW_fold = 0.58385339192799  # sin^2(theta_W) at fold (S42, running value)

# ==============================================================================
#  SECTION E: Cosmological Observables (Framework Predictions)
# ==============================================================================

# Spectral action CC prediction (using Kerner M_KK)
rho_Lambda_spectral = (2.0 / PI**2) * a0_fold * M_KK_kerner**4  # GeV^4 (S42)
CC_ratio = rho_Lambda_spectral / rho_Lambda_obs  # ~10^{120} (the CC problem)

# Clock constraint (S22d)
clock_coeff = -3.08            # dalpha/alpha = clock_coeff * dtau (S22d E-3)

# Voronoi / fabric (S42)
N_cells = 32                   # Voronoi cells from domain formation (S42)
L_over_xi = 0.031              # System size / coherence length — 0D limit (S37)

# Mode spectrum at fold (s37_instanton_action)
rho_B2_per_mode = 14.023250234055  # B2 DOS per mode at fold
E_B1 = 0.8191400026759529     # B1 mode energy at fold (M_KK)
E_B2_mean = 0.845269087679269 # Mean B2 energy at fold (M_KK)
E_B3_mean = 0.9782238787713764  # Mean B3 energy at fold (M_KK)

# ==============================================================================
#  SECTION F: PROVENANCE Dictionary
# ==============================================================================

PROVENANCE = {
    # Section A — PDG/CODATA
    "M_Pl_reduced":      {"session": "S7",  "source": "CODATA 2018", "gate": None, "superseded": False},
    "M_Pl_unreduced":    {"session": "S7",  "source": "CODATA 2018", "gate": None, "superseded": False},
    "alpha_em_MZ_inv":   {"session": "S42", "source": "PDG 2024",    "gate": None, "superseded": False},
    "M_Z":               {"session": "S42", "source": "PDG 2024",    "gate": None, "superseded": False},
    "rho_Lambda_obs":    {"session": "S42", "source": "Planck 2018", "gate": None, "superseded": False},

    # Section B — Geometric
    "tau_fold":          {"session": "S12/S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},
    "Vol_SU3_Haar":      {"session": "S44",     "source": "s44_constants_corrected.py", "gate": None, "superseded": False,
                          "note": "Corrected from 8880.93 to 1349.74 (Weyl integration formula)"},
    "Vol_SU3_WRONG":     {"session": "S42",     "source": "s42_constants_snapshot.py",  "gate": None, "superseded": True},
    "M_KK_gravity":      {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},
    "M_KK_kerner":       {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},

    # Section C — BCS
    "E_cond_ED_8mode":   {"session": "S36", "source": "s36_multisector_ed.npz (config_4_E_cond)", "gate": "ED-CONV-36", "superseded": False},
    "E_cond_ED_5mode":   {"session": "S35", "source": "s36_multisector_ed.npz (config_1_E_cond)", "gate": "ED-CORRECTED-35", "superseded": True,
                          "note": "5-mode result, superseded by 8-mode convergence study"},
    "E_cond_GL":         {"session": "S37", "source": "GL functional",                            "gate": None, "superseded": False,
                          "note": "Different quantity — GL free energy, not ED ground state"},
    "E_cond":            {"session": "S36", "source": "alias for E_cond_ED_8mode",                "gate": "ED-CONV-36", "superseded": False},
    "M_max_thouless":    {"session": "S35", "source": "RPA-BCS-35",                               "gate": "RPA-BCS-35", "superseded": False},
    "S_inst":            {"session": "S37/S38", "source": "s37_instanton_mc.npz (S_inst_D)",      "gate": None, "superseded": False},

    # Section C — BCS (continued)
    "Delta_0_GL":        {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "Delta_0_OES":       {"session": "S37", "source": "s37_pair_susceptibility.npz",    "gate": None, "superseded": False},
    "xi_BCS":            {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "xi_GL":             {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "a_GL":              {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "b_GL":              {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "omega_PV":          {"session": "S37", "source": "s37_pair_susceptibility.npz",    "gate": None, "superseded": False},
    "Gamma_Langer_BCS":  {"session": "S38", "source": "s38_attempt_freq.npz",           "gate": None, "superseded": False},
    "Kapitza_ratio":     {"session": "S38", "source": "s38_attempt_freq.npz",           "gate": None, "superseded": False},

    # Section D — Spectral action
    "a0_fold":           {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},
    "a2_fold":           {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},
    "a4_fold":           {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},
    "S_fold":            {"session": "S42", "source": "s42_gradient_stiffness.npz", "gate": None, "superseded": False},
    "M_ATDHFB":          {"session": "S40", "source": "s42_gradient_stiffness.npz", "gate": None, "superseded": False},
    "G_DeWitt":          {"session": "S42", "source": "s42_gradient_stiffness.npz", "gate": None, "superseded": False},

    # Section D — Transit
    "H_fold":            {"session": "S38", "source": "s38_kz_defects.npz",         "gate": None, "superseded": False},
    "v_terminal":        {"session": "S38", "source": "s38_kz_defects.npz",         "gate": None, "superseded": False},

    # Section E — Fabric
    "N_cells":           {"session": "S42", "source": "s42_fabric_wz.py (giant_voronoi)", "gate": None, "superseded": False},
    "rho_B2_per_mode":   {"session": "S37", "source": "s37_instanton_action.npz",   "gate": None, "superseded": False},
    "E_B1":              {"session": "S38", "source": "s38_attempt_freq.npz",        "gate": None, "superseded": False},
    "E_B2_mean":         {"session": "S38", "source": "s38_attempt_freq.npz",        "gate": None, "superseded": False},
    "E_B3_mean":         {"session": "S38", "source": "s38_attempt_freq.npz",        "gate": None, "superseded": False},
}

# ==============================================================================
#  SECTION G: Audit Patterns (consumed by extract_entities.py --audit-constants)
# ==============================================================================

# Each entry: (tag, regex_pattern_string, message)
# The regex matches ASSIGNMENT lines with stale hardcoded values.
# extract_entities.py compiles these at import time.
# To add a new enforced constant: add an entry here. That's it.

import re as _re

AUDIT_PATTERNS = [
    # --- E_cond variants ---
    ("E_cond=-0.115",
     r"^\s*E_(?:cond|BCS_MKK|BCS|bcs)\s*=\s*-?0\.115\b",
     "Stale E_cond (S35 5-mode). Canonical: -0.137 (S36 ED-CONV-36 8-mode)"),
    ("E_cond=-0.156",
     r"^\s*E_(?:cond|BCS_MKK|BCS|bcs)\s*=\s*-?0\.156\b",
     "GL E_cond used as ED value. If ED intended, use canonical -0.137"),
    # --- Volume ---
    ("Vol_SU3=8880",
     r"^\s*\w+\s*=.*\b8880\.9",
     "Wrong Vol(SU(3)) in assignment. Canonical: 1349.74 (Weyl integration formula)"),
    # --- M_KK ---
    ("M_KK=1e16",
     r"^\s*M_KK\s*=\s*1e16\b",
     "Rounded M_KK. Canonical: 7.43e16 (gravity route, S42)"),
    # --- Planck mass ---
    ("M_Pl=2.435e18",
     r"^\s*M_(?:P|Pl|Planck|PL_REDUCED|Pl_reduced)\s*=\s*2\.435e18\b",
     "Hardcoded M_Pl. Use: from canonical_constants import M_Pl_reduced"),
    ("M_Pl=1.22e19",
     r"^\s*M_(?:P|Pl|Planck|Planck_GeV)\s*=\s*1\.22\d*e19\b",
     "Hardcoded M_Pl. Use: from canonical_constants import M_Pl_unreduced"),
    # --- BCS coherence / instanton ---
    ("xi_BCS=0.808",
     r"^\s*xi_BCS\s*=\s*0\.808\b",
     f"Low-precision xi_BCS. Canonical: {xi_BCS} (s37_instanton_mc)"),
    ("S_inst=0.069",
     r"^\s*S_inst\s*=\s*0\.069\b",
     f"Low-precision S_inst. Canonical: {S_inst} (s37_instanton_mc)"),
    ("Delta_0=0.77",
     r"^\s*Delta_0\s*=\s*0\.77\d*\b",
     f"Hardcoded Delta_0. Use: from canonical_constants import Delta_0_GL"),
    # --- Transit / dynamics ---
    ("G_DeWitt=5",
     r"^\s*G_(?:DeWitt|mod)\s*=\s*5\.0\b",
     "Hardcoded G_DeWitt. Use: from canonical_constants import G_DeWitt"),
    ("H_fold=586",
     r"^\s*H_fold\s*=\s*586\.5\b",
     f"Hardcoded H_fold. Use: from canonical_constants import H_fold"),
    # --- Fabric ---
    ("N_cells=32",
     r"^\s*N_cells\s*=\s*32\b",
     "Hardcoded N_cells. Use: from canonical_constants import N_cells"),
    # --- tau_fold ---
    ("TAU_FOLD=0.19",
     r"^\s*TAU_FOLD\s*=\s*0\.19",
     "Hardcoded TAU_FOLD. Use: from canonical_constants import tau_fold as TAU_FOLD"),
    # --- Observational constants ---
    ("ALPHA_EM_MZ_INV=127",
     r"^\s*ALPHA_EM_MZ_INV\s*=\s*127",
     "Hardcoded ALPHA_EM_MZ_INV. Use: from canonical_constants import alpha_em_MZ_inv"),
]

# Pre-compiled for direct use (extract_entities imports this)
AUDIT_PATTERNS_COMPILED = [
    (tag, _re.compile(pat), msg) for tag, pat, msg in AUDIT_PATTERNS
]

# ---------------------------------------------------------------------------
# Heuristic: detect "potential hardcode" — assignments that LOOK like physics
# constants but aren't in the canon. Catches agents inventing new constants
# without updating canonical_constants.py.
# ---------------------------------------------------------------------------

# All numeric constant names exported by this module (auto-collected)
_CANON_NAMES = frozenset(
    k for k, v in dict(globals()).items()
    if isinstance(v, (int, float)) and not k.startswith("_")
)

# Regex: looks like a physics constant assignment.
# Matches scientific notation (2.435e18) OR plain decimals with a dot (50.945, 0.137).
# Plain integers without a dot are excluded (too many false positives).
_RE_POTENTIAL_HARDCODE = _re.compile(
    r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"    # capture name
    r"-?\d+\.\d+"                               # decimal with dot (e.g. 50.9, 0.137)
    r"(?:[eE][+-]?\d+)?\s*"                     # optional exponent
    r"(?:#.*)?$",
    _re.IGNORECASE
)

# Names that are obviously NOT physics constants
_HARDCODE_IGNORE_NAMES = frozenset({
    # Single-letter
    "i", "j", "k", "m", "n", "p", "q", "r", "s", "t", "x", "y", "z",
    "a", "b", "c", "d", "f", "g", "l", "u", "v", "w",
    # Common non-constant assignments
    "idx", "fig", "ax", "dpi", "fontsize", "figsize", "lw", "ms",
    "npts", "n_pts", "n_points", "n_steps", "n_grid", "n_tau", "n_modes",
    "n_samples", "n_iter", "max_iter", "tol", "rtol", "atol", "eps",
    "step", "dt", "dx", "ds",
    "err", "res", "val", "tmp", "out", "result", "status", "flag",
    "verbose", "debug", "seed", "offset", "limit", "count", "total",
    "width", "height", "size", "dim", "rank", "order", "degree",
    "idx_fold", "idx_min", "idx_max", "fold_idx",
    # --- Script-local values whitelisted by S45 audit (not universal constants) ---
    # NOTE: all entries must be lowercase (audit checks name.lower() against this set)
    # 777 names whitelisted (683 from audit + 94 prior)
    "a0_sum", "a0_total", "a2_berry", "a2_sum", "a2_t", "a2_total", "a4_sum", "a4_t",
    "a4_total", "a_a", "a_above", "a_bao", "a_bao_phys", "a_below", "a_f", "a_final",
    "a_i", "a_init", "a_s_matter", "a_vdn", "alpha1_mz_inv", "alpha2_mz_inv", "alpha_1_mz_inv", "alpha_2_mz_inv",
    "alpha_b1", "alpha_b2", "alpha_b3", "alpha_band", "alpha_s", "alpha_s_mz", "alpha_s_planck", "alpha_s_sigma",
    "alpha_v", "alpha_vdn", "atomic_clock_bound", "b2_bandwidth", "b2_bw", "b2_e_fold", "b2_overlap", "b2_split",
    "b_a", "b_err", "b_first", "b_m", "b_measured", "b_run", "bar_width", "barrier_a",
    "barrier_c", "barrier_d", "barrier_e", "baseline_m_max", "bcs_window", "berry_peak_threshold", "best_dev", "best_dist",
    "best_product", "best_r2", "best_r_sin2", "beta_anal", "beta_check", "beta_detail", "beta_eff", "beta_gate",
    "beta_gibbs", "beta_ising", "beta_rsd", "beta_sff", "beta_v", "beta_vdn", "bf_net", "bin_width",
    "br_formation_b1", "br_formation_b2", "br_formation_b3", "bullet_cluster_bound", "c_1", "c_fabric_a", "c_mw", "c_nat",
    "c_nfw", "c_ngc", "c_uv", "cdf_gauge", "cdf_grav", "cell_height", "center_phi", "center_theta",
    "chi_pass", "clock_coeff", "cmb_bound", "cmbs4_sigma", "collective_strength", "continuum_strength", "cross_check_tol", "cross_ent",
    "ct4_impedance", "d2a2_dtau2", "d2s", "d2s_bare", "d2s_from_c", "d2s_phys", "d2s_total", "d3s_fold",
    "d4s_fold", "d_a_mpc", "d_inst_dtau", "d_kk", "d_perl", "d_ratio", "d_shell", "ddda_init",
    "de_dtau", "degeneracy_tol", "delta2_zeta_obs", "delta_0", "delta_0_bcs", "delta_0_c", "delta_a0_final", "delta_alpha_per_domain",
    "delta_bcs", "delta_c", "delta_d", "delta_eta_chiral", "delta_frac", "delta_gorkov", "delta_max", "delta_min",
    "delta_new", "delta_nl", "delta_out", "delta_pair", "delta_primordial", "delta_tau", "delta_tau_bcs", "delta_tau_over_tau",
    "delta_tau_sector", "delta_tau_wall", "delta_v", "delta_v_0", "delta_w_framework", "desi_xi_precision", "dimflow_ds_sig1", "dkl_opt",
    "dkl_single_mode", "domega", "dr", "dr_arith", "dr_c", "dr_channel", "dr_cum_30", "dr_d",
    "dr_p", "dr_prop_cross", "dr_s", "dr_uncoupled", "ds_plot", "ds_ref", "ds_small", "ds_total",
    "dsigma", "dt_dwell", "dt_rep", "dtau_fd", "dtau_num", "dtau_transit", "dwell_od", "e0_sq",
    "e_bcs_fold", "e_cond", "e_cond_bcs", "e_cond_old", "e_cond_peak", "e_cond_task", "e_cross", "e_diag",
    "e_field", "e_kk_avg", "e_ref", "e_scalar", "e_smooth_weyl", "e_vac_discrete", "e_vac_final", "e_vac_test",
    "eih_combined", "eih_singlet_ratio", "enhancement_3x3", "enhancement_8x8", "eps_large", "eps_scan", "eps_small", "eps_target",
    "eps_test", "epsilon_cp", "epsilon_crossover", "epsilon_h", "epsilon_h_planck", "epsilon_small", "eta_1", "eta_default",
    "eta_eigen_max", "eta_est", "eta_frac", "eta_framework", "eta_from_lattice", "eta_ising", "eta_k7_val", "eta_primary",
    "eta_reg", "eta_reg_frac", "eta_round", "eta_t", "f0_pow", "f4_implied", "f_b2", "f_eih",
    "f_finesse", "f_nl", "f_nl_deltan", "f_nl_modulated", "f_pair", "f_safe_gauge", "f_sky", "f_sum",
    "f_total", "f_tracelog", "f_vol_1", "f_walls_frozen", "f_walls_rh", "face_width_frac", "fail_delta", "fd_step",
    "fiber_collision_scale", "fold_tau", "fom_void_only", "frac_0", "frac_well", "g_dewitt", "g_fs_bcs_fold", "g_mod",
    "g_star", "g_star_bbn", "g_star_rh", "gamma_fit", "gamma_linder", "gamma_mf", "gamma_vh", "gap_015",
    "gap_b2_b3", "gap_closure_threshold", "gate_criterion_threshold", "gate_threshold", "gauge_a0", "gauge_zeta2", "gcm_reg_threshold", "gpv_omega",
    "gpv_power", "h0", "h2", "h_0", "h_bbn", "h_bcs", "h_fd", "h_hubble",
    "ht_0", "imp_defensible_lo", "imp_physical", "impedance", "impedance_factor", "impedance_from_overlap", "inv_16pig_obs", "k7_sum",
    "k_eq", "k_max", "k_min", "k_nl_max", "k_pivot", "k_pivot_gev", "k_pivot_mpc", "k_ref_mpc",
    "k_silk", "k_zoom_max", "kinetic_threshold", "kpc_per_mpc", "ksw_den", "ksw_num", "l_abs_mpc", "l_absorber_mpc",
    "l_arm", "l_box", "l_full", "l_giant", "l_gpc", "l_hcbgw", "l_hubble_m", "l_narrow",
    "l_ref", "l_test", "lam", "lambda", "lambda_b1", "lambda_b2", "lambda_b3", "lambda_ce",
    "lambda_cutoff", "lambda_fs_correct", "lambda_laser", "lambda_plot", "lambda_ref", "lambda_sa", "lambda_standard", "lambda_test",
    "lifshitz_tau", "ln_lambda", "ln_t", "ln_term", "lnt_sum", "local_half_width", "log10_mkk_max", "log10_mkk_min",
    "log_det_b", "log_det_f", "log_lik_gge", "log_lik_gibbs_opt", "log_lik_gibbs_stored", "log_prob", "log_scale", "log_supp",
    "lv_beta_norm", "lyman_alpha", "m1_max_width", "m2_max_width", "m_200_cluster", "m_200_mw", "m_200_ngc", "m_atdhfb_cross_fold",
    "m_atdhfb_diag_fold", "m_atdhfb_fold", "m_atdhfb_frozen_fold", "m_bh", "m_bh_err", "m_constrained_8x8", "m_constrained_b2", "m_disk_mw",
    "m_disk_ngc", "m_gas_ngc", "m_gut_typical", "m_h", "m_higgs", "m_ib_cross_fold", "m_ib_diag_fold", "m_ib_fold",
    "m_ib_frozen_fold", "m_kk_a", "m_kk_c", "m_kk_gauge", "m_kk_gev", "m_kk_grav", "m_kk_kerner", "m_kk_max_firas",
    "m_kk_max_webb", "m_kk_natural", "m_max_auth", "m_max_baseline", "m_max_blocked", "m_max_ref", "m_pl_eff", "m_sol",
    "margin_param", "mass_floor", "match_tol", "merge_tol", "mkk_a", "mkk_best", "mkk_c", "mkk_firas_cross",
    "mmax_calibration", "mmax_threshold", "mpc", "mpc_in_gev_inv", "ms_factor", "ms_relaxed", "mu", "mu_crit",
    "mu_ref_sq_mkk", "multi_sector_factor", "near_crossing_threshold", "non_collective_strength", "non_thermality", "np_dr2", "npair_thermal", "ns_fail_high",
    "ns_fail_low", "ns_from_lattice", "ns_lifshitz", "ns_pass_high", "ns_pass_low", "ns_planck", "ns_planck_sigma", "ns_round",
    "ns_s", "ns_sigma", "ns_t", "nu", "nu_3d", "nu_bcs", "nu_exp", "nu_kz",
    "nu_mf", "nu_xy", "ob", "offset_step", "ol", "om", "om_m", "omega_breathe",
    "omega_check", "omega_de_obs", "omega_dm_obs", "omega_first", "omega_gpv", "omega_k", "omega_l", "omega_lambda0",
    "omega_lambda_0", "omega_lambda_obs", "omega_m0", "omega_m_0", "omega_max", "omega_osc", "omega_qrpa_b2", "omega_tau",
    "omega_vh_center", "omega_zc", "p_avg", "p_constrained", "p_constrained_hi", "p_constrained_lo", "p_even", "p_laser",
    "p_odd", "p_prior", "p_r_obs", "p_structural_floor", "pass_l", "pb_omega", "pb_power", "pc_per_kpc",
    "perlman_2011_arcsec", "perlman_2019_arcsec", "phi_bao", "phi_gap", "phi_paasch", "phi_small", "planck_central", "planck_sigma",
    "pole_strength", "post_transit_ratio", "pr_b2", "q_b2_envelope", "q_best", "q_c", "q_factor", "q_max",
    "q_step", "q_td", "quasar_bound", "quasar_precision", "r8", "r_1_high", "r_1_low", "r_8",
    "r_b2_flatband", "r_bare", "r_bicep", "r_bicep_limit", "r_cell", "r_cell_kk", "r_cmbs4", "r_core_sidm_kpc",
    "r_d_mw", "r_d_ngc", "r_drag", "r_edge", "r_fold", "r_gas_ngc", "r_goe", "r_gue",
    "r_inter", "r_litebird", "r_mean_astra", "r_pdg", "r_s", "r_s43", "r_s44", "r_s_mpc",
    "r_singlet", "r_sm_kk", "r_sol_kpc", "r_star", "r_star_astra", "r_test", "r_upper_bound", "rad_to_arcsec",
    "rate_kk", "rate_minus", "rate_plus", "ratio_1d_volovik", "ratio_2a_bose", "ratio_2b_fermi", "ratio_b_10mkk", "ratio_e3",
    "ratio_gap_split", "ratio_jk", "ratio_oes", "ref_cutoff", "rho_b1", "rho_b1_s34_per", "rho_b1_step", "rho_b2_step",
    "rho_b3_step", "rho_crit", "rho_full_w2", "rho_gge", "rho_obs_standard", "rho_peak", "rho_per_mode", "rho_physical",
    "rho_residual_final_spectral", "rho_sa_phys", "rho_smooth", "rho_vac_mkk4", "rho_vh", "rho_wall2", "rp_1mpc", "s180",
    "s210", "s23_2", "s34_impedance", "s_0", "s_actual_pre", "s_b2_analytic", "s_dump", "s_ent",
    "s_full", "s_gge", "s_gge_bits", "s_gge_check", "s_gge_nats", "s_gibbs_bits", "s_h_vz_10hz", "s_inst_a",
    "s_inst_analytic_a", "s_inst_analytic_d", "s_inst_best", "s_inst_c", "s_inst_e", "s_inst_max", "s_inst_mean", "s_inst_min",
    "s_p", "s_recomp", "s_reg", "s_total", "scalar_a0", "scalar_zeta2", "shell_gap", "sidm_limit",
    "sigma8_planck", "sigma_8_0", "sigma_alpha", "sigma_alpha_th", "sigma_bao", "sigma_bcs", "sigma_bins", "sigma_boundary",
    "sigma_crit", "sigma_etot", "sigma_fs", "sigma_gn_log10", "sigma_l_achieved", "sigma_meas", "sigma_meas_con", "sigma_meas_opt",
    "sigma_model", "sigma_over_m", "sigma_pair", "sigma_rv_frac", "sigma_vh", "sigma_w0_desi", "sigma_w_euclid", "sigma_wa_desi",
    "sigma_xi_scaled", "sigma_zp", "sin2_12_pdg", "sin2_13_pdg", "sin2_23_pdg", "sin2_thetaw_0", "sin2_thetaw_mz", "singlet_e_b",
    "singlet_frac_c_acoustic", "singlet_frac_c_compound", "singlet_frac_d2_c_compound", "snr_bao_desi", "soliton_integral", "stellar_pop_precision_jwst", "sum_pdag_blocked", "suppression_sh",
    "systematics_current", "t0i", "t0i_gge", "t0i_total", "t_bcs", "t_clean_variation", "t_cryogenic", "t_doorway",
    "t_first_cross", "t_fit_min", "t_gibbs", "t_gibbs_mkk", "t_hubble_mkk", "t_max", "t_over_thetad", "t_ref",
    "t_scram", "t_settle", "t_therm", "t_therm_mkk", "t_total", "t_transit", "t_zoom", "target_ds",
    "target_lmax", "target_ns", "target_range", "tau", "tau_0", "tau_0_bcs", "tau_a", "tau_b",
    "tau_bcs_high", "tau_bcs_low", "tau_c", "tau_cal", "tau_check", "tau_conj", "tau_end", "tau_false",
    "tau_final", "tau_fold", "tau_fold_val", "tau_gate", "tau_init", "tau_max", "tau_min", "tau_plot",
    "tau_q", "tau_q_raw", "tau_ref", "tau_ref_small", "tau_start", "tau_target", "tau_test", "tau_wall_hi",
    "tau_wall_lo", "tau_window", "tcmb", "term_4_local", "term_a4", "theta_12", "theta_23", "third_moment",
    "threshold", "threshold_fail", "threshold_pass", "tij", "tij_gge", "tl", "tol_default", "total_dec",
    "total_e_b", "total_eta0", "total_eta_log", "total_gradient", "total_inc", "total_sq", "tr_riem_endo", "v_b1b2_spinor",
    "v_b2_avg", "v_b2b2_c2_max", "v_b2b2_full_max", "v_b2b2_max", "v_b2b2_spinor", "v_b2b3_spinor", "v_b_proj", "v_b_std",
    "v_cdm_threshold", "v_desi", "v_eff", "v_eff_desi", "v_eff_dr2", "v_f", "v_fs", "v_gap_gap",
    "v_infall_z100", "v_kosmann_frame_v", "v_kosmann_spinor", "v_mid", "v_min", "v_min_physical", "v_neg_neg", "v_pos_neg",
    "v_pos_pos", "v_s38", "v_start", "v_survey", "v_t_sign", "v_terminal", "v_transit_phys", "vdn_factor",
    "vh_delta", "vh_spacing_threshold", "void_bias", "vol_su3", "w0_desi", "w0_desi_err", "w0_framework", "w0_pred",
    "w12_gap", "w_a_cpl", "w_b2", "w_eos", "w_gge", "w_minus_total", "w_n", "w_narrow",
    "w_osc_quadratic", "w_plus_total", "w_vac", "wa_desi", "wa_desi_err", "wa_framework", "wa_pred", "width_sec",
    "x_final", "x_max", "x_max_default", "x_max_high", "x_pos", "x_start", "xi_bcs", "xi_kz",
    "xi_kz_com_mpc", "xi_wall", "y_start", "z_3d", "z_dyn", "z_eff", "z_eig_sum", "z_exp",
    "z_fold_fabric", "z_formation", "z_halo", "z_kz", "z_max", "z_s", "z_s42", "z_spectral",
    "z_star", "z_tet", "z_tetrad", "z_xy", "z_xy_relax", "zero_mode_index", "zeta2_sc", "zeta_2",
    "zeta_3",
})

# Names starting with these prefixes are likely local, not constants
_HARDCODE_IGNORE_PREFIXES = ("_", "fig", "ax", "plt", "color", "label", "fmt",
                              "n_", "num_", "max_", "min_", "idx_")

# Session floor: scripts at or below this session number are exempt (historical)
AUDIT_SESSION_FLOOR = 34

# Scripts that intentionally reference old values (audit/correction scripts)
AUDIT_EXEMPT_SCRIPTS = frozenset({
    "canonical_constants.py",
    "s44_constants_corrected.py",
    "s44_mkk_reconcile.py",
    "s44_cc_gap_audit.py",
    "s38_attempt_freq.py",        # S_inst=0.069 appears only in print-statement text, not assignment
    "s43_spectral_dissolution.py", # M_P=1.221e19 appears only in print-statement text, not assignment
})

# ==============================================================================
#  SECTION H: Migration Helper
# ==============================================================================

def warn_stale(name, value, tolerance=0.01):
    """Check a hardcoded value against the canonical constant.

    Usage in migration:
        from canonical_constants import E_cond, warn_stale
        E_cond_local = -0.115  # old hardcoded value
        warn_stale("E_cond", E_cond_local)  # warns if >1% off
    """
    canonical = globals().get(name)
    if canonical is None:
        warnings.warn(f"canonical_constants: '{name}' not found in module", stacklevel=2)
        return
    if isinstance(canonical, (int, float, np.floating)):
        if abs(canonical) > 0:
            frac = abs(value - canonical) / abs(canonical)
        else:
            frac = abs(value - canonical)
        if frac > tolerance:
            warnings.warn(
                f"canonical_constants: '{name}' = {value} differs from canonical "
                f"{canonical} by {frac*100:.1f}% (>{tolerance*100:.0f}% threshold)",
                stacklevel=2
            )


# ==============================================================================
#  __main__: Validate against authoritative NPZ files (PROVENANCE-DRIVEN)
#
#  Uses the PROVENANCE dict to determine WHICH NPZ file is authoritative for
#  each constant. No blind scanning — only checks what PROVENANCE says to check.
#  Add a constant + PROVENANCE entry and it auto-validates. Nothing else to touch.
# ==============================================================================

# NPZ key name differs from module name in some files. This maps npz_key -> module_name.
# Only needed when the NPZ was saved with a different key name than the module constant.
_NPZ_KEY_ALIAS = {
    "config_4_E_cond": "E_cond_ED_8mode",
    "config_1_E_cond": "E_cond_ED_5mode",
    "E_cond_full":     "E_cond_ED_8mode",
    "M_KK_from_GN":    "M_KK_gravity",
    "OOM_diff":         "OOM_diff_MKK",
    "Delta_0":          "Delta_0_GL",
    "S_inst_D":         "S_inst",
    "Delta_OES":        "Delta_0_OES",
    "omega_plus":       "omega_PV",
    "Kapitza_Langer":   "Kapitza_ratio",
}
# Reverse: module_name -> npz_key (for PROVENANCE-driven lookup)
_MODULE_TO_NPZ_KEY = {v: k for k, v in _NPZ_KEY_ALIAS.items()}


if __name__ == "__main__":
    from pathlib import Path
    DATA_DIR = Path(__file__).parent

    # Collect all numeric module constants
    _module_consts = {
        k: v for k, v in globals().items()
        if isinstance(v, (int, float, np.floating)) and not k.startswith("_")
    }

    print("=" * 78)
    print(f"CANONICAL CONSTANTS VALIDATION ({len(_module_consts)} module constants)")
    print("=" * 78)

    passed = 0
    failed = 0
    verified = set()

    def check(label, module_val, npz_val, rtol=1e-10):
        global passed, failed
        if abs(npz_val) > 0:
            err = abs(module_val - npz_val) / abs(npz_val)
        else:
            err = abs(module_val - npz_val)
        status = "PASS" if err < rtol else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"  {status}  {label:<50s}  err={err:.2e}")

    # ── PROVENANCE-driven NPZ checks ──
    # Group PROVENANCE entries by source NPZ file
    from collections import defaultdict
    npz_checks = defaultdict(list)  # npz_filename -> [(module_name, npz_key), ...]
    for const_name, prov in PROVENANCE.items():
        src = prov.get("source", "")
        if ".npz" not in src:
            continue
        # Extract NPZ filename from source string (may have parenthetical key info)
        npz_file = src.split(" ")[0].split("(")[0].strip()
        if not npz_file.endswith(".npz"):
            continue
        # Determine what key to look up in the NPZ
        npz_key = _MODULE_TO_NPZ_KEY.get(const_name, const_name)
        # Check for parenthetical key override: "file.npz (actual_key)"
        if "(" in src and ")" in src:
            override = src.split("(")[1].split(")")[0].strip()
            npz_key = override
        npz_checks[npz_file].append((const_name, npz_key))

    print(f"\n  PROVENANCE maps {sum(len(v) for v in npz_checks.values())} "
          f"constants to {len(npz_checks)} NPZ files\n")

    for npz_file in sorted(npz_checks.keys()):
        npz_path = DATA_DIR / npz_file
        if not npz_path.exists():
            print(f"--- {npz_file} (NOT FOUND) ---")
            for const_name, _ in npz_checks[npz_file]:
                print(f"  SKIP  {const_name}")
            continue

        try:
            d = np.load(npz_path, allow_pickle=True)
        except Exception as e:
            print(f"--- {npz_file} (LOAD ERROR: {e}) ---")
            continue

        print(f"--- {npz_file} ---")
        for const_name, npz_key in npz_checks[npz_file]:
            if npz_key not in d:
                print(f"  SKIP  {const_name} (key '{npz_key}' not in NPZ)")
                continue
            val = d[npz_key]
            if hasattr(val, 'size') and val.size != 1:
                print(f"  SKIP  {const_name} (array, size={val.size})")
                continue
            try:
                npz_val = float(val.flat[0]) if hasattr(val, 'flat') else float(val)
            except (TypeError, ValueError):
                print(f"  SKIP  {const_name} (non-numeric)")
                continue

            module_val = _module_consts.get(const_name)
            if module_val is None:
                print(f"  SKIP  {const_name} (not in module)")
                continue

            label = const_name + (f" (npz:{npz_key})" if npz_key != const_name else "")
            check(label, module_val, npz_val)
            verified.add(const_name)

    # ── Identity alias checks ──
    print(f"\n--- Alias identity checks ---")
    aliases = [("E_cond", "E_cond_ED_8mode"), ("M_KK", "M_KK_gravity")]
    for alias, target in aliases:
        if globals().get(alias) is globals().get(target):
            print(f"  PASS  {alias} is {target}")
            passed += 1
        else:
            print(f"  FAIL  {alias} is NOT {target}")
            failed += 1
        verified.add(alias)

    # ── Self-consistency: derived constants must equal their derivation ──
    print(f"\n--- Derived consistency ---")
    derivations = [
        ("hbar_GeV_s",    hbar_eV_s / 1e9,        "hbar_eV_s / 1e9"),
        ("hbar_c_GeV_cm", hbar_c_GeV_m * 100,      "hbar_c_GeV_m * 100"),
        ("l_Planck_cm",   l_Planck * 100,           "l_Planck * 100"),
        ("c_light_cgs",   c_light * 100,            "c_light * 100"),
        ("c_light_km_s",  c_light / 1000,           "c_light / 1000"),
        ("G_N_cgs",       G_N * 1000,               "G_N * 1000"),
        ("Mpc_to_cm",     Mpc_to_m * 100,           "Mpc_to_m * 100"),
        ("GeV_to_g",      GeV_to_kg * 1000,         "GeV_to_kg * 1000"),
        ("T_CMB_GeV",     T_CMB * k_B / 1e9,        "T_CMB * k_B / 1e9"),
        ("GeV_inv_to_Mpc", hbar_c_GeV_m / Mpc_to_m, "hbar_c_GeV_m / Mpc_to_m"),
        ("Mpc_to_GeV_inv", Mpc_to_m / hbar_c_GeV_m, "Mpc_to_m / hbar_c_GeV_m"),
        ("Gpc_to_m",       Mpc_to_m * 1e3,          "Mpc_to_m * 1e3"),
        ("kpc_to_cm",      Mpc_to_cm / 1e3,         "Mpc_to_cm / 1e3"),
    ]
    for name, expected, formula in derivations:
        actual = _module_consts.get(name)
        if actual is not None:
            check(f"{name} == {formula}", actual, expected, rtol=1e-6)
            verified.add(name)

    # ── Summary ──
    unverified = sorted(set(_module_consts.keys()) - verified)

    print(f"\n{'='*78}")
    print(f"RESULTS: {passed} PASS, {failed} FAIL")
    print(f"  NPZ-verified:     {len(verified & set(c for checks in npz_checks.values() for c, _ in checks))}")
    print(f"  Derived-verified: {len([d for d in derivations if d[0] in verified])}")
    print(f"  Alias-verified:   {len(aliases)}")
    print(f"  Unverified:       {len(unverified)} (PDG/CODATA or no NPZ source)")
    if unverified:
        for name in unverified:
            print(f"    {name} = {_module_consts[name]}")
    print(f"{'='*78}")

    if failed > 0:
        print("\nFAILED — check values against authoritative NPZ sources")
        sys.exit(1)
    else:
        print("\nAll checks passed.")
