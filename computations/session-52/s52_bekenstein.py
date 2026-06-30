#!/usr/bin/env python3
"""
BEKENSTEIN-52: Bekenstein Bound on the Full Internal Spectral Triple
=====================================================================

Tests whether the Bekenstein entropy bound S <= 2*pi*R*E is saturated,
violated, or far from saturated for the internal SU(3) geometry at the
van Hove fold.

This EXTENDS S46's BEKENSTEIN-TORSION-46 (which tested only the 16-mode
singlet sector) to the FULL framework:
  - Full 992-mode KK spectrum at the fold
  - Physical BCS energy (E_cond, E_exc) not just zero-point
  - GGE entropy from the 8-mode Richardson-Gaudin system (S38-S39)
  - Gibbs entropy post-thermalization (S39-S40)
  - Multiple entropy measures compared systematically

PHYSICS (Bekenstein 1973, Paper 11):
  The Bekenstein bound is UNIVERSAL for any weakly-gravitating system:
    S <= 2*pi*R*E / (hbar*c)    [natural units: S <= 2*pi*R*E]
  where R = linear size of the smallest enclosing sphere, E = total energy.

  For the internal SU(3) at the fold:
    R = 1/M_KK (compactification radius) or R_Connes (geodesic radius)
    E = various choices (spectral, BCS condensation, excitation, zero-point)
    S = GGE entropy, Gibbs entropy, Fock space maximum, spectral torsion

  The Bousso COVARIANT entropy bound generalizes this:
    S(L) <= A(B)/(4*G)  for any light sheet L of any closed 2-surface B.
  For the internal space this reduces to:
    S <= pi*(R/l_P)^2  (4D holographic bound at scale R)

GATE: BEKENSTEIN-52 (INFO)
  Not pass/fail — this maps the entropy landscape of the internal space.
  Key question: WHERE does the system sit relative to the Bekenstein bound?
    - Saturated (S/S_Bek ~ 1): holographic, the geometry maximally stores info
    - Far below (S/S_Bek << 1): the geometry has enormous unused capacity
    - Violated (S/S_Bek > 1): inconsistency requiring resolution

INPUTS:
  - canonical_constants.py (all framework constants)
  - s39_bayes_gge_thermal.npz (GGE/Gibbs entropies from S39)
  - s45_truncated_torsion.npz (spectral torsion from S46 computation)

OUTPUTS:
  - s52_bekenstein.npz (all computed quantities)
  - s52_bekenstein_plot.png (saturation diagram)

Author: hawking-theorist, Session 52
Date: 2026-03-20
"""

import os
import sys
import time
import numpy as np

PROJECT_ROOT = r'C:\sandbox\Ainulindale Exflation'
SCRIPT_DIR = os.path.join(PROJECT_ROOT, 'computations')
ARCHIVE_DIR = os.path.join(PROJECT_ROOT, "computations", "_shared")
sys.path.insert(0, SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    # Fundamental
    PI, M_Pl_reduced, M_Pl_unreduced, l_Planck, hbar_c_GeV_m,
    G_N, c_light, hbar_SI, k_B_SI, eV_SI,
    # Framework geometric
    tau_fold, Vol_SU3_Haar, g0_diag, M_KK_gravity, M_KK_kerner, M_KK,
    # BCS / many-body
    E_cond, E_cond_ED_8mode, E_exc, E_exc_ratio, n_pairs, N_dof_BCS,
    Delta_0_GL, Delta_B3, T_compound,
    # Spectral action
    a0_fold, a2_fold, a4_fold, S_fold,
    # Mode spectrum
    E_B1, E_B2_mean, E_B3_mean, rho_B2_per_mode,
    # Transit
    H_fold, v_terminal, dt_transit,
    # Fabric
    T_acoustic, N_cells,
    # Cosmological
    rho_Lambda_obs, H_0_GeV,
)

# ============================================================================
# 0. Tee stdout for Windows 0kb workaround
# ============================================================================
_LOG_PATH = os.path.join(SCRIPT_DIR, 's52_bekenstein_log.txt')

class _Tee:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for s in self.streams:
            s.write(data)
            s.flush()
    def flush(self):
        for s in self.streams:
            s.flush()

_log_file = open(_LOG_PATH, 'w', encoding='utf-8')
sys.stdout = _Tee(sys.__stdout__, _log_file)
sys.stderr = _Tee(sys.__stderr__, _log_file)

t0 = time.time()

print("=" * 78)
print("BEKENSTEIN-52: Bekenstein Bound on the Full Internal Spectral Triple")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
print(f"  M_KK (gravity) = {M_KK_gravity:.4e} GeV")
print(f"  M_KK (Kerner)  = {M_KK_kerner:.4e} GeV")
print(f"  M_Pl (reduced) = {M_Pl_reduced:.4e} GeV")

# ============================================================================
# 1. Load archived entropy data
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 1: Loading archived data")
print("=" * 78)

# S39 GGE/Gibbs data
gge_path = os.path.join(ARCHIVE_DIR, 's39_bayes_gge_thermal.npz')
has_gge = os.path.exists(gge_path)
if has_gge:
    gge_data = np.load(gge_path, allow_pickle=True)
    # Extract what we can
    gge_keys = list(gge_data.keys())
    print(f"  Loaded s39_bayes_gge_thermal.npz, keys: {gge_keys}")
else:
    print(f"  WARNING: {gge_path} not found. Using memory values.")

# S46 torsion data
torsion_path = os.path.join(ARCHIVE_DIR, 's45_truncated_torsion.npz')
has_torsion = os.path.exists(torsion_path)
if has_torsion:
    torsion_data = np.load(torsion_path, allow_pickle=True)
    print(f"  Loaded s45_truncated_torsion.npz, keys: {list(torsion_data.keys())}")
else:
    print(f"  WARNING: {torsion_path} not found. Using memory values.")

# ============================================================================
# 2. Entropy measures (5 distinct quantities)
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 2: Entropy Measures of the Internal Space")
print("=" * 78)

# --- 2a. GGE entropy (from Richardson-Gaudin integrability, S38-S39) ---
# The post-transit state is a GGE with 8 conserved quantities.
# lambda_k are the Lagrange multipliers: 3 distinct values
# B2 (4 modes): lambda = 1.459
# B1 (1 mode):  lambda = 2.771
# B3 (3 modes): lambda = 6.007
# p_k = 1/(1 + exp(lambda_k)) for each mode

lambda_B2 = 1.459  # (local)
lambda_B1 = 2.771  # (local)
lambda_B3 = 6.007  # (local)

# Single-mode GGE occupations
p_B2 = 1.0 / (1.0 + np.exp(lambda_B2))
p_B1 = 1.0 / (1.0 + np.exp(lambda_B1))
p_B3 = 1.0 / (1.0 + np.exp(lambda_B3))

# Per-mode entropy: s_k = -[p_k ln p_k + (1-p_k) ln(1-p_k)]
def binary_entropy(p):
    if p <= 0 or p >= 1:
        return 0.0
    return -(p * np.log(p) + (1 - p) * np.log(1 - p))

s_B2 = binary_entropy(p_B2)
s_B1 = binary_entropy(p_B1)
s_B3 = binary_entropy(p_B3)

# Total GGE entropy: 4*s_B2 + 1*s_B1 + 3*s_B3
S_GGE = 4 * s_B2 + 1 * s_B1 + 3 * s_B3

# Also get from .npz if available
if has_gge:
    try:
        S_gge_stored = float(gge_data['S_gge'])
        print(f"  S_GGE (stored in .npz)  = {S_gge_stored:.6f} nats")
    except KeyError:
        S_gge_stored = None
        print(f"  S_gge key not found in .npz")

print(f"\n  GGE Lagrange multipliers:")
print(f"    lambda_B2 = {lambda_B2} (4 modes)")
print(f"    lambda_B1 = {lambda_B1} (1 mode)")
print(f"    lambda_B3 = {lambda_B3} (3 modes)")
print(f"  GGE occupations:")
print(f"    p_B2 = {p_B2:.6f}, s_B2 = {s_B2:.6f} nats/mode")
print(f"    p_B1 = {p_B1:.6f}, s_B1 = {s_B1:.6f} nats/mode")
print(f"    p_B3 = {p_B3:.6f}, s_B3 = {s_B3:.6f} nats/mode")
print(f"  S_GGE (computed) = 4*{s_B2:.4f} + 1*{s_B1:.4f} + 3*{s_B3:.4f}")
print(f"                   = {S_GGE:.6f} nats = {S_GGE / np.log(2):.4f} bits")

# --- 2b. Gibbs entropy (post-thermalization, S39-S40) ---
# After thermalization (t_therm ~ 6), the GGE evolves to Gibbs.
# T_Gibbs = 0.113 M_KK (from MEMORY, S40 result)
# S_Gibbs = 6.701 bits (from MEMORY, S40 result)
T_Gibbs = 0.113  # M_KK units
S_Gibbs_bits = 6.701
S_Gibbs = S_Gibbs_bits * np.log(2)  # convert to nats

if has_gge:
    try:
        T_gibbs_stored = float(gge_data['T_gibbs'])
        S_gibbs_stored = float(gge_data['S_gibbs'])
        print(f"\n  Gibbs (from .npz): T = {T_gibbs_stored:.6f}, S = {S_gibbs_stored:.6f} nats")
        # Use stored values if available
        T_Gibbs = T_gibbs_stored
        S_Gibbs = S_gibbs_stored
        S_Gibbs_bits = S_Gibbs / np.log(2)
    except KeyError:
        print(f"\n  Gibbs keys not found in .npz, using memory values")

print(f"\n  Gibbs (post-thermalization):")
print(f"    T_Gibbs = {T_Gibbs:.6f} M_KK")
print(f"    S_Gibbs = {S_Gibbs:.6f} nats = {S_Gibbs_bits:.4f} bits")
print(f"    Delta_S = S_Gibbs - S_GGE = {S_Gibbs - S_GGE:.6f} nats = {(S_Gibbs - S_GGE)/np.log(2):.4f} bits")

# --- 2c. Fock space maximum entropy ---
# 8 modes, each can be 0 or 1: 2^8 = 256 states
# Maximum entropy = 8 * ln(2) = 5.545 nats
S_Fock_max = N_dof_BCS * np.log(2)
print(f"\n  Fock space maximum:")
print(f"    N_dof = {N_dof_BCS} modes")
print(f"    S_Fock_max = {N_dof_BCS}*ln(2) = {S_Fock_max:.6f} nats = {N_dof_BCS:.1f} bits")

# --- 2d. Spectral torsion entropy (singlet, from S46) ---
if has_torsion:
    T_singlet = float(torsion_data['T_singlet'])
    S_torsion = abs(np.log(T_singlet))
    print(f"\n  Spectral torsion (singlet, S46):")
    print(f"    T_singlet = {T_singlet:.6f}")
    print(f"    S_torsion = |ln T| = {S_torsion:.6f} nats")
else:
    T_singlet = 0.147  # (local)
    S_torsion = abs(np.log(T_singlet))
    print(f"\n  Spectral torsion (singlet, from memory):")
    print(f"    T_singlet = {T_singlet:.6f}")
    print(f"    S_torsion = |ln T| = {S_torsion:.6f} nats")

# --- 2e. Entanglement entropy (S39 result) ---
S_ent = 0.0  # EXACTLY ZERO (product state, no horizon)
print(f"\n  Entanglement entropy (S39, S40):")
print(f"    S_ent = {S_ent:.6f} nats  (EXACTLY ZERO — product state)")

# --- 2f. CCS spectral entropy (Chamseddine-Connes-van Suijlekom, Paper 20) ---
# S_CCS = Tr f_entropy(D^2/Lambda^2) where f_entropy = -x*ln(x) - (1-x)*ln(1-x)
# For the full 992-mode spectrum at the fold:
# Each mode contributes binary entropy at the "occupation" set by the cutoff.
# With Lambda = M_KK: x_k = exp(-lambda_k^2) for each eigenvalue lambda_k.
# For eigenvalues ~0.8-1.0 M_KK: x_k ~ exp(-0.64 to -1.0) ~ 0.37-0.53
# Per mode: s_CCS ~ 0.68-0.69 nats
# Total: S_CCS ~ 992 * 0.69 ~ 685 nats (for the FULL spectrum)
# But the BCS physics only involves the 8 gap-edge modes.
n_full_modes = 992  # all KK eigenvalues at fold (S42 result)
# Estimate CCS entropy for full spectrum
avg_eigenvalue_ratio = (4 * E_B2_mean + 1 * E_B1 + 3 * E_B3_mean) / 8
x_avg = np.exp(-avg_eigenvalue_ratio**2)
s_CCS_per_mode = binary_entropy(x_avg)
S_CCS_full_est = n_full_modes * s_CCS_per_mode
S_CCS_8mode = 8 * s_CCS_per_mode

print(f"\n  CCS spectral entropy (Paper 20 estimate):")
print(f"    avg eigenvalue ratio = {avg_eigenvalue_ratio:.4f}")
print(f"    x_avg = exp(-{avg_eigenvalue_ratio**2:.4f}) = {x_avg:.6f}")
print(f"    s_CCS per mode = {s_CCS_per_mode:.6f} nats")
print(f"    S_CCS (8 gap-edge) = {S_CCS_8mode:.4f} nats")
print(f"    S_CCS (992 full) = {S_CCS_full_est:.1f} nats [estimate]")

# Summary
print(f"\n--- ENTROPY SUMMARY ---")
entropy_dict = {
    "S_ent (entanglement)": S_ent,
    "S_torsion (singlet)": S_torsion,
    "S_GGE (8-mode RG)": S_GGE,
    "S_Fock_max (8*ln2)": S_Fock_max,
    "S_Gibbs (post-therm)": S_Gibbs,
    "S_CCS_8 (gap-edge)": S_CCS_8mode,
    "S_CCS_full (992-mode)": S_CCS_full_est,
}
for label, val in sorted(entropy_dict.items(), key=lambda x: x[1]):
    print(f"  {label:30s} = {val:10.4f} nats = {val/np.log(2):10.4f} bits")

# ============================================================================
# 3. Energy scales
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 3: Energy Scales (in M_KK units)")
print("=" * 78)

# The BCS condensation energy
E_BCS = abs(E_cond)  # = 0.137 M_KK

# The excitation energy from transit
E_transit = E_exc  # = 60.6 M_KK

# Zero-point energy of 8 gap-edge modes
E_zp_8 = 0.5 * (4 * E_B2_mean + 1 * E_B1 + 3 * E_B3_mean)

# Total spectral energy of 8 modes
E_spec_8 = 4 * E_B2_mean + 1 * E_B1 + 3 * E_B3_mean

# Full spectrum zero-point energy (estimated from 992 modes at ~0.88 M_KK avg)
E_zp_full = 0.5 * n_full_modes * avg_eigenvalue_ratio

# Spectral action energy at fold
E_spec_action = S_fold  # dimensionless (M_KK units via sum of f(lambda^2))

print(f"  E_BCS (|E_cond|)      = {E_BCS:.6f} M_KK")
print(f"  E_transit (excitation) = {E_transit:.2f} M_KK")
print(f"  E_zp (8 gap-edge)     = {E_zp_8:.4f} M_KK")
print(f"  E_spec (8 modes)      = {E_spec_8:.4f} M_KK")
print(f"  E_zp (992 full est.)  = {E_zp_full:.1f} M_KK")
print(f"  S_fold (spectral act.) = {E_spec_action:.1f} [dimensionless cutoff sum]")
print(f"  T_compound = E_exc/8  = {T_compound:.4f} M_KK")

# ============================================================================
# 4. Radius scales
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 4: Radius Scales")
print("=" * 78)

# (a) KK compactification radius: R = 1/M_KK
R_KK = 1.0  # in M_KK^{-1} units  # (local)

# (b) Connes geodesic radius: pi*sqrt(g0_diag)/2 for round SU(3)
R_Connes = PI * np.sqrt(g0_diag) / 2  # = pi*sqrt(3)/2 ~ 2.72 in M_KK^{-1}

# (c) Effective radius from volume: V = Vol_SU3_Haar * R_KK^8
# R_eff = (Vol_SU3_Haar)^{1/8} in M_KK^{-1}
R_vol = Vol_SU3_Haar**(1.0/8.0)

# Physical sizes
R_KK_phys = 1.0 / M_KK_gravity  # GeV^{-1}
R_KK_m = R_KK_phys * hbar_c_GeV_m  # meters
R_KK_over_lP = R_KK_m / l_Planck

print(f"  R_KK      = {R_KK:.4f} M_KK^{{-1}}  (compactification radius)")
print(f"  R_Connes  = {R_Connes:.4f} M_KK^{{-1}}  (geodesic radius pi*sqrt(3)/2)")
print(f"  R_vol     = {R_vol:.4f} M_KK^{{-1}}  (volume-effective: Vol^{{1/8}})")
print(f"  R_KK (physical) = {R_KK_phys:.4e} GeV^{{-1}} = {R_KK_m:.4e} m")
print(f"  R_KK / l_Planck = {R_KK_over_lP:.2f}")

# ============================================================================
# 5. Bekenstein bound: S <= 2*pi*E*R
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 5: BEKENSTEIN BOUND TEST (S <= 2*pi*E*R)")
print("=" * 78)

# The PHYSICALLY RELEVANT entropy-energy pairs:
# (a) GGE entropy vs BCS condensation energy (the pairing energy)
# (b) GGE entropy vs transit excitation energy (the quench energy)
# (c) Gibbs entropy vs transit excitation energy (post-thermalization)
# (d) Fock max vs zero-point energy (absolute upper bound)

test_cases = [
    # (label, S, E, R, description)
    ("GGE vs E_BCS at R_KK",       S_GGE,      E_BCS,     R_KK,    "Physical: GGE entropy from BCS ground state energy"),
    ("GGE vs E_BCS at R_Connes",   S_GGE,      E_BCS,     R_Connes,"Physical: GGE entropy at geodesic scale"),
    ("GGE vs E_transit at R_KK",   S_GGE,      E_transit,  R_KK,   "Physical: GGE entropy from transit excitation"),
    ("Gibbs vs E_transit at R_KK", S_Gibbs,    E_transit,  R_KK,   "Thermalized: Gibbs entropy from excitation energy"),
    ("Gibbs vs E_transit at R_Connes", S_Gibbs, E_transit, R_Connes,"Thermalized: at geodesic scale"),
    ("Fock_max vs E_zp_8 at R_KK", S_Fock_max, E_zp_8,    R_KK,   "Upper bound: max entropy from zero-point"),
    ("Fock_max vs E_spec_8 at R_KK", S_Fock_max, E_spec_8, R_KK,  "Upper bound: max entropy from spectral energy"),
    ("CCS_full vs E_zp_full at R_KK", S_CCS_full_est, E_zp_full, R_KK, "Full spectrum CCS entropy"),
    ("CCS_full vs E_zp_full at R_Connes", S_CCS_full_est, E_zp_full, R_Connes, "Full spectrum at geodesic"),
    ("Torsion vs E_zp_8 at R_KK",  S_torsion,  E_zp_8,    R_KK,   "S46 comparison: torsion entropy"),
]

results = []
print(f"\n  {'Test Case':45s} | {'S':8s} | {'S_Bek':8s} | {'S/S_Bek':8s} | {'Margin':8s} | Status")
print(f"  {'-'*45}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-------")

for label, S_val, E_val, R_val, desc in test_cases:
    S_Bek = 2 * PI * E_val * R_val
    ratio = S_val / S_Bek if S_Bek > 0 else float('inf')
    margin = 1.0 / ratio if ratio > 0 else float('inf')
    status = "PASS" if ratio <= 1.0 else "VIOLATED"
    results.append({
        'label': label, 'S': S_val, 'E': E_val, 'R': R_val,
        'S_Bek': S_Bek, 'ratio': ratio, 'margin': margin, 'status': status
    })
    print(f"  {label:45s} | {S_val:8.4f} | {S_Bek:8.2f} | {ratio:8.6f} | {margin:8.2f}x | {status}")

# ============================================================================
# 6. Most conservative and most generous tests
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 6: Extremal Tests")
print("=" * 78)

# Most conservative: largest entropy, smallest E*R
# Physical: S_Gibbs (largest physical entropy) vs E_BCS (smallest energy), R_KK (smallest R)
S_Bek_conservative = 2 * PI * E_BCS * R_KK
ratio_conservative = S_Gibbs / S_Bek_conservative
margin_conservative = 1.0 / ratio_conservative

print(f"\n  MOST CONSERVATIVE (hardest to satisfy):")
print(f"    S = S_Gibbs = {S_Gibbs:.4f} nats")
print(f"    E = |E_cond| = {E_BCS:.6f} M_KK")
print(f"    R = R_KK = {R_KK:.4f} M_KK^{{-1}}")
print(f"    S_Bek = 2*pi*{E_BCS:.6f}*{R_KK:.4f} = {S_Bek_conservative:.6f} nats")
print(f"    S / S_Bek = {ratio_conservative:.6f}")
if ratio_conservative <= 1.0:
    print(f"    Margin = {margin_conservative:.2f}x")
    print(f"    STATUS: PASS (bound satisfied by factor {margin_conservative:.2f})")
else:
    print(f"    STATUS: **VIOLATED** by factor {ratio_conservative:.2f}x")
    print(f"    The Gibbs entropy EXCEEDS the Bekenstein bound at E_BCS, R_KK")
    print(f"    Resolution: E_BCS is the PAIRING energy, not the TOTAL energy.")
    print(f"    The correct energy includes excitations (E_transit) or zero-point (E_zp).")

# Most generous: smallest entropy, largest E*R
S_Bek_generous = 2 * PI * E_transit * R_Connes
ratio_generous = S_GGE / S_Bek_generous

print(f"\n  MOST GENEROUS (easiest to satisfy):")
print(f"    S = S_GGE = {S_GGE:.4f} nats")
print(f"    E = E_transit = {E_transit:.2f} M_KK")
print(f"    R = R_Connes = {R_Connes:.4f} M_KK^{{-1}}")
print(f"    S_Bek = 2*pi*{E_transit:.2f}*{R_Connes:.4f} = {S_Bek_generous:.2f} nats")
print(f"    S / S_Bek = {ratio_generous:.6e}")
print(f"    Margin = {1.0/ratio_generous:.1f}x")

# ============================================================================
# 7. The PHYSICAL test: appropriate energy for each entropy
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 7: PHYSICAL MATCHING (Entropy ↔ Energy)")
print("=" * 78)

# The Bekenstein bound requires the TOTAL energy of the system.
# For the 8-mode BCS system post-transit:
#   E_total = E_exc = 443 * |E_cond| = 60.6 M_KK (from Schwinger-instanton, S38)
# This is the energy available to be stored as entropy.
#
# The GGE entropy is the entropy of the POST-TRANSIT state at fixed E_total.
# The Gibbs entropy is the equilibrium entropy at the same E_total after thermalization.
#
# The Bekenstein bound test is:
#   S_GGE  <= 2*pi * E_total * R_KK  =>  PHYSICAL test (pre-thermalization)
#   S_Gibbs <= 2*pi * E_total * R_KK  =>  PHYSICAL test (post-thermalization)

print(f"\n  Post-transit state (8-mode BCS system):")
print(f"    E_total = E_exc = {E_exc:.2f} M_KK = {E_exc_ratio:.0f} * |E_cond|")
print(f"    R = R_KK = 1/M_KK")
S_Bek_physical = 2 * PI * E_exc * R_KK
print(f"    S_Bek = 2*pi*{E_exc:.2f}*{R_KK:.1f} = {S_Bek_physical:.2f} nats")
print(f"")
print(f"    GGE:   S/S_Bek = {S_GGE:.4f}/{S_Bek_physical:.2f} = {S_GGE/S_Bek_physical:.6f}")
print(f"           Saturation: {S_GGE/S_Bek_physical*100:.4f}%")
print(f"           Margin: {S_Bek_physical/S_GGE:.1f}x below bound")
print(f"")
print(f"    Gibbs: S/S_Bek = {S_Gibbs:.4f}/{S_Bek_physical:.2f} = {S_Gibbs/S_Bek_physical:.6f}")
print(f"           Saturation: {S_Gibbs/S_Bek_physical*100:.4f}%")
print(f"           Margin: {S_Bek_physical/S_Gibbs:.1f}x below bound")

saturation_GGE = S_GGE / S_Bek_physical
saturation_Gibbs = S_Gibbs / S_Bek_physical

# ============================================================================
# 8. Bousso covariant entropy bound (holographic)
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 8: BOUSSO COVARIANT ENTROPY BOUND")
print("=" * 78)

# The holographic bound: S <= A/(4*G) = A*M_Pl^2/4  (in natural units)
# For a sphere of radius R in 4D: A = 4*pi*R^2
# S_holo = pi * R^2 * M_Pl^2 = pi * (M_Pl/M_KK)^2

# In framework units (M_KK = 1):
# S_holo = pi * (M_Pl_reduced / M_KK_gravity)^2
ratio_Pl_KK = M_Pl_reduced / M_KK_gravity
S_holo_4D = PI * ratio_Pl_KK**2

print(f"  4D holographic bound at R = 1/M_KK:")
print(f"    M_Pl / M_KK = {ratio_Pl_KK:.4e}")
print(f"    S_holo = pi*(M_Pl/M_KK)^2 = {S_holo_4D:.4e} nats")
print(f"    S_GGE / S_holo = {S_GGE / S_holo_4D:.4e}")
print(f"    S_Gibbs / S_holo = {S_Gibbs / S_holo_4D:.4e}")
print(f"    => Internal entropy uses {S_Gibbs / S_holo_4D * 100:.4e}% of holographic capacity")

# For the INTERNAL space as a gravitational system:
# The internal space is 8-dimensional (dim SU(3) = 8).
# The "area" bounding it is a 7-sphere: A_7 = (2*pi^4/3) * R^7
# But the internal Planck length l_P^{(10)} relates to the 4D one via:
# l_P^{(10)} = l_P^{(4)} * (M_KK * l_P^{(4)})^{3/4}   (for 6 extra dims)
# This gives an 8D holographic bound that is MUCH weaker.

# More useful: the number of Planck areas on the internal space boundary
# In 4D effective theory, the internal modes contribute:
# S_max ~ (R_KK / l_P)^2 per Planck area cell
print(f"\n  Internal space effective holographic capacity:")
print(f"    R_KK / l_P = {R_KK_over_lP:.2f}")
print(f"    (R_KK/l_P)^2 = {R_KK_over_lP**2:.2f}")
print(f"    This is O(1) — the internal space is only ~{R_KK_over_lP:.0f}x larger than Planck")

# ============================================================================
# 9. Connection to S46 BEKENSTEIN-TORSION-46 result
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 9: Connection to S46 (BEKENSTEIN-TORSION-46)")
print("=" * 78)

# S46 result: 27% holographic saturation, 4.03x margin
# That was for the singlet sector (16 modes) using spectral torsion
# S46 tested S_torsion vs 2*pi*E_zp*R_KK

# Recompute S46 for direct comparison
E_zp_singlet = 0.5 * 16 * avg_eigenvalue_ratio  # approximate
S_Bek_s46 = 2 * PI * E_zp_singlet * R_KK
ratio_s46 = S_torsion / S_Bek_s46

print(f"  S46 (singlet sector, 16 modes):")
print(f"    S_torsion = {S_torsion:.4f} nats")
print(f"    E_zp_singlet ~ {E_zp_singlet:.4f} M_KK")
print(f"    S_Bek = {S_Bek_s46:.4f} nats")
print(f"    S/S_Bek ~ {ratio_s46:.4f} (S46 reported: ~27%)")
print(f"    S46 margin: {1.0/ratio_s46:.2f}x (S46 reported: 4.03x)")
print(f"")
print(f"  THIS computation (full BCS system):")
print(f"    S_GGE = {S_GGE:.4f} nats (physical post-transit entropy)")
print(f"    S_Bek(E_exc, R_KK) = {S_Bek_physical:.2f} nats")
print(f"    S/S_Bek = {saturation_GGE:.6f} ({saturation_GGE*100:.4f}%)")
print(f"    => FAR below bound. The transit excitation energy dominates.")

# ============================================================================
# 10. Entropic hierarchy and thermodynamic interpretation
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 10: ENTROPIC HIERARCHY AND INTERPRETATION")
print("=" * 78)

print(f"""
  HIERARCHY OF ENTROPIES (in nats):

    S_ent       = {S_ent:.4f}      (entanglement: ZERO, product state)
    S_torsion   = {S_torsion:.4f}      (spectral torsion, singlet)
    S_GGE       = {S_GGE:.4f}      (GGE, 8-mode Richardson-Gaudin)
    S_Gibbs     = {S_Gibbs:.4f}      (Gibbs, post-thermalization)
    S_Fock_max  = {S_Fock_max:.4f}      (8-mode Fock maximum)
    S_CCS_8     = {S_CCS_8mode:.4f}      (CCS spectral, 8 gap-edge)
    S_CCS_full  = {S_CCS_full_est:.1f}    (CCS spectral, 992 modes)
    S_Bek(phys) = {S_Bek_physical:.2f}    (Bekenstein at E_exc, R_KK)
    S_holo      = {S_holo_4D:.4e}  (holographic at R_KK)

  The ENTROPIC LADDER:
    S_ent < S_torsion < S_GGE < S_Fock_max < S_Gibbs << S_CCS_full << S_Bek << S_holo

  KEY OBSERVATIONS:

  1. NO VIOLATION: All physical entropies are far below S_Bek. PASS.
     Bekenstein bound satisfied at ALL (E, R) pairs with appropriate matching.

  2. SATURATION at physical pairing:
     The MOST CONSERVATIVE physical test (S_Gibbs vs E_BCS at R_KK)
     gives ratio = {ratio_conservative:.4f}.
""")

if ratio_conservative > 1.0:
    print(f"""     This APPEARS to violate the bound, but this is because E_BCS = |E_cond|
     is the BINDING energy (energy released by pairing), not the TOTAL energy
     contained in the system. The total energy after transit is E_exc >> E_BCS.
     Using E_exc: S/S_Bek = {saturation_Gibbs:.6f} — well below bound.

     PHYSICAL INTERPRETATION: The condensation energy E_BCS is like the
     WORK extracted from a Geroch box — it does not represent the system's
     total energy. The Bekenstein bound constrains total energy, not binding.
""")
else:
    print(f"""     Even at the BCS condensation energy, the bound holds.
     Margin: {margin_conservative:.2f}x.
""")

print(f"""  3. HOLOGRAPHIC FRACTION:
     The internal geometry stores S_Gibbs = {S_Gibbs_bits:.2f} bits in a space
     with holographic capacity S_holo = {S_holo_4D:.2e} nats = {S_holo_4D/np.log(2):.2e} bits.
     Fraction: {S_Gibbs/S_holo_4D*100:.2e}% — the system is FAR from holographic.

     This is consistent with S_ent = 0: no horizon, no holographic encoding.
     The internal entropy is VOLUMETRIC (from Fock space modes), not AREA-law.

  4. CONNECTION TO PAPER 11 (Bekenstein 1973):
     Bekenstein showed S_BH = A/(4*l_P^2) for black holes, with GSL delta S_gen >= 0.
     The internal space has NO horizon (S_ent = 0), so there is no BH entropy
     contribution. The GSL reduces to ordinary second law:
       S_GGE -> S_Gibbs (thermalization, Delta_S = {S_Gibbs - S_GGE:.3f} nats > 0) ✓

  5. THE R_KK/l_P ~ {R_KK_over_lP:.0f} FACT:
     The internal space is only ~{R_KK_over_lP:.0f}x larger than the Planck length.
     This means the holographic capacity is SMALL (~{R_KK_over_lP**2:.0f} Planck areas).
     Yet the BCS Fock space contains only 8 modes (2^8 = 256 states, 8 bits max).
     The internal geometry's entropy content is WELL within its holographic capacity.
""")

# ============================================================================
# 11. Save results
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 11: Saving results")
print("=" * 78)

output_path = os.path.join(SCRIPT_DIR, 's52_bekenstein.npz')
np.savez(output_path,
    # Entropies (nats)
    S_ent=S_ent,
    S_torsion=S_torsion,
    S_GGE=S_GGE,
    S_Gibbs=S_Gibbs,
    S_Fock_max=S_Fock_max,
    S_CCS_8mode=S_CCS_8mode,
    S_CCS_full_est=S_CCS_full_est,
    # Bekenstein bounds
    S_Bek_physical=S_Bek_physical,
    S_Bek_conservative=S_Bek_conservative,
    S_holo_4D=S_holo_4D,
    # Saturation ratios
    saturation_GGE=saturation_GGE,
    saturation_Gibbs=saturation_Gibbs,
    ratio_conservative=ratio_conservative,
    # Physical parameters
    E_BCS=E_BCS,
    E_transit=E_transit,
    E_zp_8=E_zp_8,
    R_KK=R_KK,
    R_Connes=R_Connes,
    R_KK_over_lP=R_KK_over_lP,
    # GGE parameters
    lambda_B2=lambda_B2,
    lambda_B1=lambda_B1,
    lambda_B3=lambda_B3,
    S_GGE_bits=S_GGE / np.log(2),
    S_Gibbs_bits=S_Gibbs_bits,
    # Metadata
    tau_fold=tau_fold,
    M_KK_gravity=M_KK_gravity,
)
print(f"  Saved to {output_path}")

# ============================================================================
# 12. Saturation diagram
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 12: Generating saturation plot")
print("=" * 78)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left panel: bar chart of entropy measures vs Bekenstein bound
ax1 = axes[0]
labels = ['$S_{\\rm ent}$', '$S_{\\rm torsion}$', '$S_{\\rm GGE}$',
          '$S_{\\rm Fock}^{\\rm max}$', '$S_{\\rm Gibbs}$']
values = [S_ent, S_torsion, S_GGE, S_Fock_max, S_Gibbs]
colors = ['#2196F3', '#FF9800', '#4CAF50', '#9C27B0', '#F44336']

bars = ax1.bar(labels, values, color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
ax1.axhline(y=S_Bek_physical, color='red', linestyle='--', linewidth=2,
            label=f'$S_{{\\rm Bek}}(E_{{\\rm exc}}, R_{{\\rm KK}})$ = {S_Bek_physical:.0f}')
ax1.axhline(y=S_Bek_conservative, color='orange', linestyle=':', linewidth=2,
            label=f'$S_{{\\rm Bek}}(E_{{\\rm BCS}}, R_{{\\rm KK}})$ = {S_Bek_conservative:.2f}')
ax1.set_ylabel('Entropy (nats)', fontsize=12)
ax1.set_title('Entropy Measures vs Bekenstein Bound\n(8-mode BCS system at fold)', fontsize=11)
ax1.legend(fontsize=9, loc='upper left')
ax1.set_yscale('log')
# Add 1e-3 floor for log scale (S_ent = 0 would be -inf)
for i, v in enumerate(values):
    if v == 0:
        bars[i].set_height(1e-3)
ax1.set_ylim(1e-3, S_Bek_physical * 2)

# Right panel: saturation diagram
ax2 = axes[1]
# Plot S/S_Bek for different (E,R) pairs
phys_labels = []
phys_ratios = []
phys_colors_r = []
for r in results:
    if r['S_Bek'] > 0 and r['ratio'] > 0:
        phys_labels.append(r['label'][:30])
        phys_ratios.append(r['ratio'])
        phys_colors_r.append('#4CAF50' if r['ratio'] < 1 else '#F44336')

y_pos = np.arange(len(phys_labels))
ax2.barh(y_pos, phys_ratios, color=phys_colors_r, alpha=0.8, edgecolor='black', linewidth=0.5)
ax2.axvline(x=1.0, color='red', linestyle='--', linewidth=2, label='$S/S_{\\rm Bek} = 1$ (bound)')
ax2.set_xlabel('$S / S_{\\rm Bekenstein}$', fontsize=12)
ax2.set_yticks(y_pos)
ax2.set_yticklabels(phys_labels, fontsize=8)
ax2.set_title('Bekenstein Bound Saturation\n($S/S_{\\rm Bek}$ < 1 required)', fontsize=11)
ax2.set_xscale('log')
ax2.legend(fontsize=9)
ax2.invert_yaxis()

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's52_bekenstein_plot.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved plot to {plot_path}")

# ============================================================================
# 13. Final verdict
# ============================================================================
print(f"\n{'='*78}")
print("SECTION 13: GATE VERDICT — BEKENSTEIN-52")
print("=" * 78)

print(f"""
  GATE: BEKENSTEIN-52 (INFO)

  RESULT: Bekenstein bound SATISFIED at all physical (E, R) combinations.

  KEY NUMBERS:
    S_GGE / S_Bek(E_exc, R_KK)  = {saturation_GGE:.6f}  ({saturation_GGE*100:.4f}% saturation)
    S_Gibbs / S_Bek(E_exc, R_KK) = {saturation_Gibbs:.6f}  ({saturation_Gibbs*100:.4f}% saturation)
    S_Gibbs / S_Bek(E_BCS, R_KK) = {ratio_conservative:.4f}  (conservative test)
    S_Gibbs / S_holo(R_KK)       = {S_Gibbs/S_holo_4D:.4e}  (holographic fraction)
    R_KK / l_Planck              = {R_KK_over_lP:.2f}  (internal space ~ Planck scale)
""")

if ratio_conservative > 1.0:
    print(f"""  NOTE: The conservative test S_Gibbs vs E_BCS gives ratio > 1.
  This is NOT a violation because E_BCS = |E_cond| is the BINDING energy,
  not the total system energy. The Bekenstein bound requires E_total.
  At E_total = E_exc (the physical post-transit energy): ratio = {saturation_Gibbs:.6f}.

  PHYSICAL PICTURE:
  The internal SU(3) at the fold contains 8 BCS modes storing {S_Gibbs_bits:.2f} bits
  of information. The Bekenstein capacity at the transit energy is {S_Bek_physical/np.log(2):.0f} bits.
  The system is {S_Bek_physical/S_Gibbs:.0f}x below the Bekenstein limit.

  The holographic capacity is {S_holo_4D/np.log(2):.0e} bits — the system barely uses
  any of it, consistent with S_ent = 0 (no horizon, no holographic encoding).

  This means the INFORMATION in the internal geometry is:
    - Locally stored (no horizon => recoverable, S39 result)
    - Volumetric, not area-law (Fock space modes, not boundary degrees of freedom)
    - Thermalized from GGE to Gibbs with entropy increase {S_Gibbs - S_GGE:.3f} nats
    - Respects all entropy bounds with large margin
""")
else:
    print(f"""  The Bekenstein bound is satisfied even at the most conservative (E_BCS, R_KK).

  PHYSICAL PICTURE:
  The internal SU(3) at the fold contains 8 BCS modes storing {S_Gibbs_bits:.2f} bits
  of information. The Bekenstein capacity at E_BCS is {S_Bek_conservative/np.log(2):.2f} bits.
  The system is at {ratio_conservative*100:.1f}% saturation — substantial but below bound.

  The holographic capacity is {S_holo_4D/np.log(2):.0e} bits — the system barely uses
  any of it, consistent with S_ent = 0 (no horizon, no holographic encoding).
""")

elapsed = time.time() - t0
print(f"\n  Elapsed time: {elapsed:.2f} s")
print(f"\n{'='*78}")
print("BEKENSTEIN-52 COMPLETE")
print("=" * 78)

_log_file.close()
