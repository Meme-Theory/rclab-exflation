#!/usr/bin/env python3
"""
EULER-DEFICIT-45: Proof (and Correction) of the GGE Euler Deficit Identity
==========================================================================

S44 W6-5 found numerically that the Euler deficit
    delta = E_GGE - sum_k T_k S_k^{FD}
equals ~6.8% of E_GGE and claimed delta = |E_cond|.

This script proves three things:
  1. The claim is WRONG: delta != |E_cond| (ratio = 0.843, not 1.0).
  2. The deficit arises from using the WRONG entropy formula.
  3. The CORRECT Euler relation is an EXACT TAUTOLOGY.

ANALYTIC PROOF:

The system is a single Cooper pair (N=1) distributed among 8 quasiparticle
modes with probabilities f_k = <n_k> (where sum f_k = 1).

The GGE density matrix is canonical (N=1 sector):
    rho_GGE = sum_k f_k |k><k|

The GGE Lagrange multipliers are:
    beta_k = -ln(f_k),    T_k = -1/ln(f_k)

The CORRECT GGE entropy is the Shannon/mixing entropy:
    S_k^{Shannon} = -f_k ln(f_k) = f_k * beta_k

The INCORRECT (Fermi-Dirac) entropy used in S44 is:
    S_k^{FD} = -f_k ln(f_k) - (1-f_k) ln(1-f_k)

THEOREM (Euler Identity for Canonical N=1 GGE):

    T_k * S_k^{Shannon} = [-1/ln(f_k)] * [-f_k ln(f_k)] = f_k

    Therefore: sum_k T_k * S_k^{Shannon} = sum_k f_k = N_pair = 1  (EXACT)

    And: E_GGE = sum_k f_k * 2*xi_k  (energy definition)

    So the "deficit" with correct entropy is:
        E_GGE - N_pair = sum_k f_k * (2*xi_k - 1)   [in M_KK units]

    This is just the pair-number subtraction, not a thermodynamic identity.

THE S44 DEFICIT:

Using the wrong (FD) entropy:
    T_k * S_k^{FD} = f_k + (1-f_k)*ln(1-f_k)/ln(f_k)

    deficit^{FD} = E_GGE - sum_k T_k * S_k^{FD}
                 = E_GGE - 1 - sum_k (1-f_k)*ln(1-f_k)/ln(f_k)
                 = 0.11538 M_KK

    This is NOT |E_cond| = 0.13685 M_KK. The ratio is 0.843.

PHYSICAL INTERPRETATION:

The Euler relation E = TS (with PV=0, mu*N=0) holds exactly for a
single-temperature system. For a GGE with multiple temperatures, the
generalized Euler relation sum_k T_k S_k = N_pair is NOT an energy
identity -- it is a normalization identity.

The S44 "deficit" has no physical content. It is the difference between
E_GGE (an energy) and a sum of non-energy-dimensional quantities (the
binary entropy terms contribute vacuum-mode entropy that does not
exist in the canonical N=1 Hilbert space).

In the language of Volovik (Paper 15, Chapter 29): the cosmological
constant problem arises from computing vacuum energy in an effective
theory. Here the FD entropy is the effective-theory entropy (grand
canonical, including vacuum fluctuations). The correct entropy is the
microscopic entropy (canonical, counting only physical states). Using
the wrong ensemble produces a spurious deficit -- the analog of the
CC problem at the level of thermodynamic identities.

Gate: EULER-DEFICIT-45 = INFO
    Verdict: The identity delta = |E_cond| is DISPROVED (ratio 0.843).
    The "deficit" is an artifact of using Fermi-Dirac (grand canonical)
    entropy in a canonical N=1 system. The correct Euler relation
    sum T_k S_k = N_pair = 1 is an exact tautology.

Author: Volovik Superfluid Universe Theorist, Session 45
Date: 2026-03-15
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ======================================================================
#  Load data
# ======================================================================

gge = np.load(os.path.join(SCRIPT_DIR, 's43_gge_temperatures.npz'),
              allow_pickle=True)
en = np.load(os.path.join(SCRIPT_DIR, 's42_gge_energy.npz'),
             allow_pickle=True)
jac = np.load(os.path.join(SCRIPT_DIR, 's44_multi_t_jacobson.npz'),
              allow_pickle=True)

f_k = gge['nk_exact']          # occupation probabilities (N=1 canonical)
xi_k = gge['E_8']              # quasiparticle energies [M_KK]
labels = gge['branch_labels']
E_cond_MKK = float(en['E_cond_MKK'])
E_GGE_stored = float(gge['E_GGE'])

n_modes = 8

print("=" * 78)
print("EULER-DEFICIT-45: Proof and Correction of the GGE Euler Deficit Identity")
print("=" * 78)

# ======================================================================
#  Step 1: Verify fundamental quantities
# ======================================================================

print("\n--- Step 1: Fundamental quantities ---")

E_GGE = np.sum(f_k * 2.0 * xi_k)
N_pair = np.sum(f_k)

print(f"  f_k = {f_k}")
print(f"  xi_k = {xi_k}")
print(f"  sum f_k = N_pair = {N_pair:.15f}")
print(f"  E_GGE = sum f_k * 2*xi_k = {E_GGE:.15f}")
print(f"  E_GGE stored = {E_GGE_stored:.15f}")
print(f"  |E_cond| = {E_cond_MKK:.15f}")

assert abs(N_pair - 1.0) < 1e-10, f"FATAL: N_pair = {N_pair}, expected 1.0"
assert abs(E_GGE - E_GGE_stored) < 1e-10, f"FATAL: E_GGE mismatch"

# ======================================================================
#  Step 2: GGE temperatures
# ======================================================================

print("\n--- Step 2: GGE temperatures (canonical N=1) ---")

beta_k = -np.log(f_k)
T_k = 1.0 / beta_k

print(f"\n  {'Mode':<8} {'f_k':>12} {'beta_k':>12} {'T_k':>12}")
for i in range(n_modes):
    print(f"  {str(labels[i]):<8} {f_k[i]:12.8f} {beta_k[i]:12.6f} {T_k[i]:12.6f}")

# Verify consistency with stored T_k
T_k_stored = gge['T_k']
max_T_dev = np.max(np.abs(T_k - T_k_stored))
print(f"\n  Max deviation from stored T_k: {max_T_dev:.2e}")
assert max_T_dev < 1e-8, f"FATAL: T_k mismatch"

# ======================================================================
#  Step 3: THEOREM — Correct Euler relation (Shannon entropy)
# ======================================================================

print("\n" + "=" * 78)
print("THEOREM: CORRECT EULER RELATION (SHANNON ENTROPY)")
print("=" * 78)

# Shannon entropy per mode: S_k = -f_k * ln(f_k) = f_k * beta_k
S_k_Shannon = f_k * beta_k   # = -f_k * ln(f_k)

# The Euler product T_k * S_k:
Euler_product = T_k * S_k_Shannon  # = (1/beta_k) * (f_k * beta_k) = f_k

print(f"\n  Per-mode verification: T_k * S_k^Shannon = f_k")
print(f"  {'Mode':<8} {'T_k*S_k':>15} {'f_k':>15} {'|diff|':>15}")
max_Euler_err = 0.0
for i in range(n_modes):
    diff = abs(Euler_product[i] - f_k[i])
    max_Euler_err = max(max_Euler_err, diff)
    print(f"  {str(labels[i]):<8} {Euler_product[i]:15.12f} {f_k[i]:15.12f} {diff:15.2e}")

print(f"\n  Maximum |T_k * S_k - f_k|: {max_Euler_err:.2e}")

# The sum:
Euler_sum_Shannon = np.sum(Euler_product)
print(f"\n  sum_k T_k * S_k^Shannon = {Euler_sum_Shannon:.15f}")
print(f"  N_pair                   = {N_pair:.15f}")
print(f"  |difference|             = {abs(Euler_sum_Shannon - N_pair):.2e}")

EULER_EXACT = abs(Euler_sum_Shannon - N_pair) < 1e-14

print(f"\n  >>> EULER IDENTITY: sum_k T_k * S_k^Shannon = N_pair = 1  [VERIFIED TO {abs(Euler_sum_Shannon - N_pair):.1e}]")
print(f"  >>> This is EXACT (algebraic identity, not numerical accident)")
print(f"  >>> Proof: T_k * S_k = (1/beta_k)(f_k * beta_k) = f_k, Q.E.D.")

# ======================================================================
#  Step 4: DISPROOF — S44 Euler deficit != |E_cond|
# ======================================================================

print("\n" + "=" * 78)
print("DISPROOF: S44 EULER DEFICIT != |E_cond|")
print("=" * 78)

# S44 used Fermi-Dirac (binary) entropy per mode:
S_k_FD = np.zeros(n_modes)
for i in range(n_modes):
    fk = f_k[i]
    if 0 < fk < 1:
        S_k_FD[i] = -fk * np.log(fk) - (1.0 - fk) * np.log(1.0 - fk)

# The Euler sum with wrong entropy:
Euler_sum_FD = np.sum(T_k * S_k_FD)

# Decompose: T_k * S_k^FD = T_k * S_k^Shannon + T_k * [-(1-f_k)ln(1-f_k)]
#            = f_k + (1-f_k)*ln(1-f_k)/ln(f_k)
extra_k = (1.0 - f_k) * np.log(1.0 - f_k) / np.log(f_k)

print(f"\n  Binary entropy decomposition: T_k * S_k^FD = f_k + epsilon_k")
print(f"  where epsilon_k = (1-f_k)*ln(1-f_k)/ln(f_k)")
print(f"\n  {'Mode':<8} {'f_k':>12} {'epsilon_k':>12} {'T_k*S_FD':>12} {'check':>12}")
for i in range(n_modes):
    tk_sk_fd = T_k[i] * S_k_FD[i]
    check = f_k[i] + extra_k[i]
    print(f"  {str(labels[i]):<8} {f_k[i]:12.8f} {extra_k[i]:12.8f} {tk_sk_fd:12.8f} {check:12.8f}")

# Verify decomposition
decomp_err = abs(Euler_sum_FD - (1.0 + np.sum(extra_k)))
print(f"\n  sum T_k * S_k^FD = {Euler_sum_FD:.15f}")
print(f"  1 + sum epsilon_k = {1.0 + np.sum(extra_k):.15f}")
print(f"  |difference|      = {decomp_err:.2e}")

# The deficit:
deficit_FD = E_GGE - Euler_sum_FD
stored_deficit = float(jac['Euler_residual'])

print(f"\n  E_GGE                     = {E_GGE:.10f}")
print(f"  sum T_k * S_k^FD          = {Euler_sum_FD:.10f}")
print(f"  Deficit (E_GGE - sum)      = {deficit_FD:.10f}")
print(f"  Stored Euler_residual (S44) = {-stored_deficit:.10f}")
print(f"  |E_cond|                    = {E_cond_MKK:.10f}")
print()
print(f"  deficit / |E_cond|          = {deficit_FD / E_cond_MKK:.6f}")
print(f"  deficit / E_GGE             = {deficit_FD / E_GGE:.6f} (= 6.83% from S44)")

DEFICIT_EQUALS_ECOND = abs(deficit_FD - E_cond_MKK) / E_cond_MKK < 0.01  # 1% tolerance

print(f"\n  >>> DISPROOF: deficit / |E_cond| = {deficit_FD / E_cond_MKK:.4f}, NOT 1.0")
print(f"  >>> The S44 claim 'Euler deficit = |E_cond|' is WRONG (15.7% error)")
print(f"  >>> The numerical coincidence (6.8% vs 8.1%) was misleading")

# ======================================================================
#  Step 5: Analytic structure of the deficit
# ======================================================================

print("\n" + "=" * 78)
print("ANALYTIC STRUCTURE OF THE FD DEFICIT")
print("=" * 78)

# deficit_FD = E_GGE - 1 - sum_k epsilon_k
# = sum_k f_k * (2*xi_k - 1) - sum_k (1-f_k)*ln(1-f_k)/ln(f_k)
# = sum_k [f_k * (2*xi_k - 1) - (1-f_k)*ln(1-f_k)/ln(f_k)]

print("\n  deficit = sum_k [f_k*(2*xi_k - 1) - (1-f_k)*ln(1-f_k)/ln(f_k)]")
print()
print(f"  {'Mode':<8} {'f*(2xi-1)':>12} {'-(1-f)ln(1-f)/lnf':>20} {'net':>12}")
total_kinetic = 0.0
total_entropy = 0.0
for i in range(n_modes):
    kinetic = f_k[i] * (2 * xi_k[i] - 1)
    entropy = -extra_k[i]  # Note: extra_k is positive, so -extra contributes positively to deficit
    total_kinetic += kinetic
    total_entropy += entropy
    print(f"  {str(labels[i]):<8} {kinetic:12.8f} {-extra_k[i]:20.8f} {kinetic - extra_k[i]:12.8f}")

print(f"\n  sum f*(2xi-1) = {total_kinetic:.10f} (kinematic part)")
print(f"  sum (1-f)ln(1-f)/lnf = {np.sum(extra_k):.10f} (entropy excess)")
print(f"  deficit = kinematic - entropy excess = {total_kinetic - np.sum(extra_k):.10f}")

# ======================================================================
#  Step 6: Physical origin — wrong ensemble (Volovik vacuum energy analog)
# ======================================================================

print("\n" + "=" * 78)
print("PHYSICAL ORIGIN: WRONG ENSEMBLE = WRONG VACUUM ENERGY")
print("=" * 78)

# The FD entropy S_k^FD = -f*ln(f) - (1-f)*ln(1-f) treats each mode
# as a grand canonical Fermi mode (can be occupied or empty independently).
# But in N=1, if mode k is occupied, ALL other modes are empty.
# The (1-f_k)*ln(1-f_k) term counts the entropy of the EMPTY state
# of mode k, which is unphysical in the canonical ensemble:
# - In canonical N=1, if mode k is empty, one of the OTHER modes is occupied.
#   The entropy of that configuration is already counted in THOSE modes' f_j ln f_j.
# - In grand canonical, mode k being empty is an independent event.
#   The (1-f_k) entropy double-counts the vacuum fluctuations.

# This is precisely the vacuum energy problem in condensed matter language:
# - The "correct" (microscopic/canonical) entropy gives Euler = N_pair exactly.
# - The "wrong" (effective/grand canonical) entropy gives a DEFICIT.
# - The deficit is NOT a physical energy; it is a bookkeeping artifact.

S_GGE_Shannon = -np.sum(f_k * np.log(f_k))
S_GGE_FD = np.sum(S_k_FD)
S_max_Shannon = np.log(n_modes)  # ln(8) for 8 modes
S_max_FD = n_modes * np.log(2)   # 8*ln(2) for 8 independent Fermi modes

print(f"\n  Shannon entropy: S_GGE = {S_GGE_Shannon:.6f}, S_max = {S_max_Shannon:.6f}, ratio = {S_GGE_Shannon/S_max_Shannon:.4f}")
print(f"  FD entropy:      S_GGE = {S_GGE_FD:.6f}, S_max = {S_max_FD:.6f}, ratio = {S_GGE_FD/S_max_FD:.4f}")
print(f"\n  FD entropy exceeds Shannon by {S_GGE_FD - S_GGE_Shannon:.6f} nats")
print(f"  This excess = sum (1-f_k)ln(1-f_k) = {np.sum(-(1-f_k)*np.log(1-f_k)):.6f} nats")
print(f"  It counts vacuum fluctuations of modes that CANNOT be independently empty.")

# Connection to Volovik's vacuum energy argument:
print(f"\n  VOLOVIK PARALLEL (Paper 15, Ch. 29):")
print(f"  - In 3He: vacuum energy computed from effective theory includes all modes.")
print(f"    Computed from microscopic theory, the vacuum energy is ZERO (equilibrium).")
print(f"  - Here: FD entropy includes vacuum (empty-mode) contributions per mode.")
print(f"    Canonical entropy includes ONLY occupied-mode contributions.")
print(f"  - The FD deficit is the analog of the CC overestimate from effective field theory.")
print(f"  - The resolution is the same: use the correct (microscopic/canonical) ensemble.")

# ======================================================================
#  Step 7: Cross-check — T_therm * S_GGE = E_GGE
# ======================================================================

print("\n" + "=" * 78)
print("CROSS-CHECK: T_therm * S_GGE = E_GGE (SINGLE-T EULER)")
print("=" * 78)

T_therm = E_GGE / S_GGE_Shannon
T_therm_stored = float(gge['T_therm'])

print(f"\n  T_therm = E_GGE / S_GGE = {T_therm:.10f}")
print(f"  T_therm (stored) = {T_therm_stored:.10f}")
print(f"  T_therm * S_GGE = {T_therm * S_GGE_Shannon:.10f}")
print(f"  E_GGE           = {E_GGE:.10f}")
print(f"  |difference|    = {abs(T_therm * S_GGE_Shannon - E_GGE):.2e}")

SINGLE_T_EULER = abs(T_therm * S_GGE_Shannon - E_GGE) < 1e-12
print(f"\n  Single-temperature Euler: T_therm * S_GGE = E_GGE [VERIFIED TO {abs(T_therm * S_GGE_Shannon - E_GGE):.1e}]")
print(f"  This is TRIVIALLY TRUE by construction (T_therm := E/S)")

# ======================================================================
#  Step 8: What WOULD the correct GGE Euler relation with PV look like?
# ======================================================================

print("\n" + "=" * 78)
print("CORRECT GGE EULER RELATION (GENERALIZED GIBBS-DUHEM)")
print("=" * 78)

# For a GGE with density matrix rho = exp(-sum_k beta_k I_k)/Z:
# The generalized free energy is:
#   Phi = -ln(Z) / beta_ref (some reference beta)
# Or more properly, the GGE thermodynamic potential is:
#   ln Z = S - sum_k beta_k <I_k>
#
# For N=1 canonical: Z = sum_k exp(-beta_k) and f_k = exp(-beta_k)/Z
# beta_k = -ln(f_k) (since Z=1 when sum f_k = 1)
# ln Z = ln(1) = 0
# So: S = sum_k beta_k <I_k> = sum_k (-ln f_k) * f_k = S_Shannon
#
# The generalized Gibbs-Duhem relation:
# d(ln Z) = -sum_k <I_k> d(beta_k) + sum_k (d<I_k>/d_something)
# For constant system: d(ln Z) = 0 => sum_k <I_k> d(beta_k) = 0
# (Constraint: only N-1 of the beta_k are independent due to sum f_k = 1)

# The Euler relation in extensive form:
# For a GGE at scale lambda:
#   E(lambda) = lambda * E, S(lambda) = lambda * S, N_k(lambda) = lambda * N_k
# Euler's theorem: E = sum_k (partial E / partial N_k)_S * N_k + T * S (??)
# But this is for the EXTENSIVITY of E(N_k, S), not for the Euler-from-GGE.

# The correct statement: the generalized Euler relation for a GGE is:
#   sum_k T_k * (partial S / partial <I_k>) * <I_k> = E
# if and only if S is the Legendre transform of the free energy.

# For our system: <I_k> = f_k, S = -sum f_k ln f_k
# partial S / partial f_k = -ln(f_k) - 1 (but with Lagrange constraint sum f_k = 1)
# The constrained derivative: partial S / partial f_k |_{sum f = 1} = -ln(f_k) - 1 + lambda
# where lambda is set by the constraint => lambda = 1 + <ln(f)> = 1 - S/N

# In any case, T_k = 1/beta_k = -1/ln(f_k) is NOT dE/dS_k in the usual sense.
# The Euler relation E = sum T_k S_k holds only when T_k = dE/dS_k.
# For the canonical GGE, dE/df_k = 2*xi_k (mode energy), and
# dS/df_k = -ln(f_k) - 1 + lambda (Shannon entropy derivative).
# So dE/dS_k = 2*xi_k / (-ln(f_k) - 1 + lambda) which is NOT T_k = -1/ln(f_k).

# The correct "thermodynamic temperature" for mode k in the Euler sense:
# T_k^{Euler} = (dE/df_k) / (dS/df_k)_constrained
# This requires specifying which constraint path we use.

# BOTTOM LINE: The multi-temperature Euler relation sum T_k S_k = E
# does NOT hold for the canonical GGE. The identity that DOES hold is:
# sum_k T_k S_k^{Shannon} = N_pair = 1 (tautology)
# sum_k T_therm * S_k^{Shannon} = E_GGE (definition of T_therm)

# The S44 deficit has no thermodynamic content.

print(f"\n  For the canonical N=1 GGE, the multi-temperature Euler relation")
print(f"  sum_k T_k dS_k = dE does NOT hold as an integrated identity.")
print(f"  The beta_k = -ln(f_k) are GGE Lagrange multipliers, NOT")
print(f"  thermodynamic partial derivatives dE/dS_k.")
print(f"")
print(f"  The identities that DO hold exactly:")
print(f"    (a) sum_k T_k * S_k^Shannon = N_pair = 1    [tautology]")
print(f"    (b) T_therm * S_GGE = E_GGE                 [definition of T_therm]")
print(f"    (c) S_GGE = sum_k beta_k * f_k              [= -sum f_k ln f_k]")
print(f"    (d) ln Z = S - sum_k beta_k f_k = 0         [Z = 1 for canonical N=1]")

# ======================================================================
#  Step 9: Is there ANY exact identity involving E_cond?
# ======================================================================

print("\n" + "=" * 78)
print("SEARCH FOR E_COND IDENTITY")
print("=" * 78)

# E_cond = E_gs (the BCS ground state energy, negative)
# E_GGE = sum f_k * 2*xi_k (post-quench energy)
# E_exc = E_GGE - E_gs = E_GGE + |E_cond| (excitation energy)

E_gs = -E_cond_MKK
E_exc = E_GGE - E_gs

print(f"\n  E_GGE    = {E_GGE:.10f} M_KK")
print(f"  E_gs     = {E_gs:.10f} M_KK (BCS ground state)")
print(f"  |E_cond| = {E_cond_MKK:.10f} M_KK")
print(f"  E_exc    = {E_exc:.10f} M_KK (excitation energy above ground state)")

# Check various ratios:
print(f"\n  Ratios involving E_cond:")
print(f"    deficit_FD / |E_cond|    = {deficit_FD / E_cond_MKK:.6f}")
print(f"    deficit_FD / E_exc       = {deficit_FD / E_exc:.6f}")
print(f"    |E_cond| / E_GGE        = {E_cond_MKK / E_GGE:.6f}")
print(f"    deficit_FD / E_GGE       = {deficit_FD / E_GGE:.6f}")
print(f"    E_exc / E_GGE           = {E_exc / E_GGE:.6f}")

# Check if deficit_FD = E_cond * some simple function of f_k:
print(f"\n  deficit_FD = {deficit_FD:.10f}")
print(f"  |E_cond| * S_GGE/S_max = {E_cond_MKK * S_GGE_Shannon / S_max_Shannon:.10f}")
print(f"  |E_cond| * (1 - S_GGE/S_max) = {E_cond_MKK * (1 - S_GGE_Shannon/S_max_Shannon):.10f}")

# Is there a simple relation? Let me compute a few candidates:
candidates = {
    "|E_cond| * f_B2": E_cond_MKK * np.sum(f_k[:4]),
    "E_GGE * S_deficit/S_max": E_GGE * (S_max_Shannon - S_GGE_Shannon) / S_max_Shannon,
    "E_GGE * (1 - N/S_max)": E_GGE * (1 - 1.0/S_max_Shannon),
    "sum f*(2xi-1) - sum eps": deficit_FD,  # tautology check
}

print(f"\n  Candidate identities for deficit = {deficit_FD:.10f}:")
for name, val in candidates.items():
    ratio = deficit_FD / val if val != 0 else float('inf')
    print(f"    {name:<35s} = {val:.10f}  (ratio = {ratio:.6f})")

# No simple identity found. The deficit is a complicated function of {f_k, xi_k}.
print(f"\n  CONCLUSION: No exact identity connects the FD deficit to |E_cond|.")
print(f"  The 6.8% numerical value is an accidental near-coincidence with 8.1%.")

# ======================================================================
#  Step 10: What the superfluid vacuum teaches us
# ======================================================================

print("\n" + "=" * 78)
print("SUPERFLUID VACUUM LESSON")
print("=" * 78)

print("""
  In superfluid 3He (Volovik, Paper 15, Ch. 29), the vacuum energy
  problem has a clean resolution: in EQUILIBRIUM, the vacuum does not
  gravitate. The cosmological constant vanishes not because of fine-tuning
  but because the thermodynamic identity requires it.

  The present computation exhibits the SAME structure at the level of
  the Euler relation:

  1. MICROSCOPIC (canonical N=1):
     The system has exactly 1 Cooper pair in 8 modes.
     The Euler identity sum_k T_k S_k = N_pair = 1 is EXACT.
     No "deficit." No mystery.

  2. EFFECTIVE (grand canonical per mode):
     Each mode is treated as independently occupied/empty.
     The FD entropy double-counts vacuum fluctuations.
     A "deficit" of 6.8% appears.

  3. THE DEFICIT IS NOT PHYSICAL:
     It does not equal E_cond (ratio = 0.843).
     It does not equal any microscopically meaningful quantity.
     It arises from applying the wrong statistical mechanics.

  4. THE LESSON:
     The vacuum energy "problem" (deficit from Euler relation) dissolves
     when you use the correct (microscopic) ensemble. This is not a
     cancellation or fine-tuning -- it is an identity.

     In the superfluid: epsilon + P = 0 in equilibrium => Lambda = 0.
     In the GGE: sum T_k S_k = N_pair in canonical => deficit = 0.

     Same principle, different system.
""")

# ======================================================================
#  Step 11: Gate verdict
# ======================================================================

print("=" * 78)
print("GATE: EULER-DEFICIT-45 = INFO")
print("=" * 78)

verdict = 'INFO'
gate_name = 'EULER-DEFICIT-45'

results = {
    'EULER_IDENTITY_EXACT': EULER_EXACT,
    'DEFICIT_EQUALS_ECOND': DEFICIT_EQUALS_ECOND,
    'deficit_FD': deficit_FD,
    'deficit_over_Econd': deficit_FD / E_cond_MKK,
    'Euler_sum_Shannon': Euler_sum_Shannon,
    'Euler_sum_FD': Euler_sum_FD,
    'S_GGE_Shannon': S_GGE_Shannon,
    'S_GGE_FD': S_GGE_FD,
    'S_max_Shannon': S_max_Shannon,
    'S_max_FD': S_max_FD,
}

print(f"\n  1. sum_k T_k * S_k^Shannon = {Euler_sum_Shannon:.15f} = N_pair = 1  [EXACT]")
print(f"  2. deficit^FD = {deficit_FD:.10f} M_KK")
print(f"  3. |E_cond|   = {E_cond_MKK:.10f} M_KK")
print(f"  4. deficit / |E_cond| = {deficit_FD / E_cond_MKK:.4f} (NOT 1.0, S44 claim DISPROVED)")
print(f"  5. The deficit arises from using FD (grand canonical) entropy in a canonical N=1 system")
print(f"  6. With correct (Shannon) entropy, the Euler relation is an exact tautology")
print(f"  7. The Volovik vacuum energy lesson: wrong ensemble => spurious deficit")

# S44 correction:
print(f"\n  S44 CORRECTIONS:")
print(f"  - 'Euler deficit = |E_cond| = 0.115 M_KK exactly' => WRONG")
print(f"    deficit = 0.1154, |E_cond| = 0.1369, ratio = 0.843")
print(f"  - 'New structural identity linking GGE non-thermality to BCS condensation' => NO")
print(f"    The deficit is an artifact of using FD entropy in canonical N=1 ensemble")
print(f"  - 'sum T_k S_k / E_GGE = 0.932' => CORRECT but misleading")
print(f"    With Shannon entropy: sum T_k S_k = 1.000 (exact)")

# ======================================================================
#  Step 12: Save
# ======================================================================

np.savez(os.path.join(SCRIPT_DIR, 's45_euler_deficit.npz'),
    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([verdict]),

    # Occupation probabilities
    f_k=f_k,
    xi_k=xi_k,
    labels=labels,

    # GGE temperatures
    beta_k=beta_k,
    T_k=T_k,

    # Shannon entropy (correct)
    S_k_Shannon=S_k_Shannon,
    S_GGE_Shannon=S_GGE_Shannon,
    S_max_Shannon=S_max_Shannon,
    Euler_sum_Shannon=Euler_sum_Shannon,

    # FD entropy (incorrect for this system)
    S_k_FD=S_k_FD,
    S_GGE_FD=S_GGE_FD,
    S_max_FD=S_max_FD,
    Euler_sum_FD=Euler_sum_FD,

    # Deficit
    deficit_FD=deficit_FD,
    deficit_over_Econd=deficit_FD / E_cond_MKK,
    extra_k=extra_k,

    # Physical quantities
    E_GGE=E_GGE,
    E_cond=E_cond_MKK,
    N_pair=N_pair,
    T_therm=T_therm,

    # Verdict flags
    EULER_EXACT=EULER_EXACT,
    S44_CLAIM_DISPROVED=not DEFICIT_EQUALS_ECOND,
)

print(f"\nData saved to: {os.path.join(SCRIPT_DIR, 's45_euler_deficit.npz')}")

# ======================================================================
#  Step 13: Plot
# ======================================================================

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, hspace=0.40, wspace=0.35)

# --- Panel (a): Shannon vs FD entropy per mode ---
ax = fig.add_subplot(gs[0, 0])
x = np.arange(n_modes)
w_bar = 0.35
colors = ['#2196F3']*4 + ['#FF9800'] + ['#4CAF50']*3
ax.bar(x - w_bar/2, S_k_Shannon, w_bar, color=colors, alpha=0.9,
       edgecolor='black', lw=0.5, label=r'$S_k^{\rm Shannon}$')
ax.bar(x + w_bar/2, S_k_FD, w_bar, color=colors, alpha=0.4,
       edgecolor='black', lw=0.5, hatch='//', label=r'$S_k^{\rm FD}$')
ax.set_xticks(x)
ax.set_xticklabels([str(l) for l in labels], fontsize=7, rotation=45)
ax.set_ylabel('Entropy [nats]', fontsize=10)
ax.set_title('(a) Shannon vs Fermi-Dirac Entropy', fontsize=11, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (b): T_k * S_k for both entropies ---
ax = fig.add_subplot(gs[0, 1])
TS_Shannon = T_k * S_k_Shannon  # = f_k
TS_FD = T_k * S_k_FD
ax.bar(x - w_bar/2, TS_Shannon, w_bar, color=colors, alpha=0.9,
       edgecolor='black', lw=0.5, label=r'$T_k S_k^{\rm Sh} = f_k$')
ax.bar(x + w_bar/2, TS_FD, w_bar, color=colors, alpha=0.4,
       edgecolor='black', lw=0.5, hatch='//', label=r'$T_k S_k^{\rm FD}$')
# Show the mode energy for comparison
ax.scatter(x, f_k * 2 * xi_k, marker='D', color='red', s=40, zorder=5,
           label=r'$\rho_k = f_k \cdot 2\xi_k$')
ax.set_xticks(x)
ax.set_xticklabels([str(l) for l in labels], fontsize=7, rotation=45)
ax.set_ylabel(r'$T_k S_k$ or $\rho_k$', fontsize=10)
ax.set_title(r'(b) Euler Products $T_k S_k$', fontsize=11, fontweight='bold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (c): The deficit decomposition ---
ax = fig.add_subplot(gs[0, 2])
# Bar chart: E_GGE, sum T_k S_k^Sh, sum T_k S_k^FD, |E_cond|
quantities = [E_GGE, Euler_sum_Shannon, Euler_sum_FD, deficit_FD, E_cond_MKK]
q_labels = [r'$E_{\rm GGE}$', r'$\sum T_k S_k^{\rm Sh}$',
            r'$\sum T_k S_k^{\rm FD}$', r'Deficit$^{\rm FD}$', r'$|E_{\rm cond}|$']
q_colors = ['steelblue', '#2196F3', '#FF9800', '#E53935', '#4CAF50']
bars = ax.bar(np.arange(5), quantities, color=q_colors, alpha=0.8,
              edgecolor='black', lw=0.5)
ax.set_xticks(np.arange(5))
ax.set_xticklabels(q_labels, fontsize=8, rotation=30, ha='right')
ax.set_ylabel(r'Energy [$M_{\rm KK}$]', fontsize=10)
ax.set_title('(c) Deficit Decomposition', fontsize=11, fontweight='bold')
for i, (bar, val) in enumerate(zip(bars, quantities)):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f'{val:.4f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (d): The "vacuum mode" entropy excess ---
ax = fig.add_subplot(gs[1, 0])
vacuum_entropy = -(1.0 - f_k) * np.log(1.0 - f_k)
ax.bar(x, vacuum_entropy, color=colors, alpha=0.7, edgecolor='black', lw=0.5)
ax.set_xticks(x)
ax.set_xticklabels([str(l) for l in labels], fontsize=7, rotation=45)
ax.set_ylabel('Vacuum entropy [nats]', fontsize=10)
ax.set_title(r'(d) Spurious Vacuum Entropy $-(1-f_k)\ln(1-f_k)$', fontsize=11, fontweight='bold')
ax.text(0.02, 0.95, f'Total = {np.sum(vacuum_entropy):.4f} nats\n(FD excess over Shannon)',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(facecolor='lightyellow', alpha=0.8))
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (e): epsilon_k (extra term in T*S^FD) ---
ax = fig.add_subplot(gs[1, 1])
ax.bar(x, extra_k, color=colors, alpha=0.7, edgecolor='black', lw=0.5)
ax.set_xticks(x)
ax.set_xticklabels([str(l) for l in labels], fontsize=7, rotation=45)
ax.set_ylabel(r'$\epsilon_k$', fontsize=10)
ax.set_title(r'(e) Extra Term $\epsilon_k = (1-f_k)\ln(1-f_k)/\ln(f_k)$',
             fontsize=11, fontweight='bold')
ax.text(0.02, 0.95, f'Sum = {np.sum(extra_k):.4f}\n'
        r'$\sum T_k S_k^{\rm FD} = 1 + \sum\epsilon_k$' + f' = {Euler_sum_FD:.4f}',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(facecolor='lightyellow', alpha=0.8))
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (f): The proof — T_k * S_k^Shannon = f_k (scatter) ---
ax = fig.add_subplot(gs[1, 2])
ax.scatter(f_k, TS_Shannon, s=100, c=colors, edgecolors='black', zorder=5)
lims = [0, max(f_k) * 1.15]
ax.plot(lims, lims, 'k--', lw=1, alpha=0.5, label='y = x (exact identity)')
for i in range(n_modes):
    ax.annotate(str(labels[i]), (f_k[i], TS_Shannon[i]),
                textcoords="offset points", xytext=(5, 5), fontsize=7)
ax.set_xlabel(r'$f_k$ (occupation probability)', fontsize=10)
ax.set_ylabel(r'$T_k \cdot S_k^{\rm Shannon}$', fontsize=10)
ax.set_title(r'(f) Proof: $T_k S_k^{\rm Sh} = f_k$ (exact)', fontsize=11, fontweight='bold')
ax.legend(fontsize=9)
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

# --- Panel (g): Deficit vs E_cond comparison ---
ax = fig.add_subplot(gs[2, 0])
x_comp = [0, 1]
ax.bar(x_comp, [deficit_FD, E_cond_MKK],
       color=['#E53935', '#4CAF50'], alpha=0.8, edgecolor='black', lw=1)
ax.set_xticks(x_comp)
ax.set_xticklabels([r'Deficit$^{\rm FD}$', r'$|E_{\rm cond}|$'], fontsize=11)
ax.set_ylabel(r'Energy [$M_{\rm KK}$]', fontsize=10)
ax.set_title('(g) S44 Claim: Deficit = |E_cond|?', fontsize=11, fontweight='bold')
for i, val in enumerate([deficit_FD, E_cond_MKK]):
    ax.text(i, val + 0.003, f'{val:.5f}', ha='center', fontsize=10, fontweight='bold')
ax.text(0.5, 0.85, f'Ratio = {deficit_FD/E_cond_MKK:.3f}\nS44 claim DISPROVED',
        transform=ax.transAxes, fontsize=11, ha='center', fontweight='bold',
        color='red', bbox=dict(facecolor='lightyellow', alpha=0.9))
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (h): Information diagram ---
ax = fig.add_subplot(gs[2, 1])
theta = np.linspace(0, 2*np.pi, 100)
# Shannon entropy circle
r_sh = np.sqrt(S_GGE_Shannon / np.pi)
r_max = np.sqrt(S_max_Shannon / np.pi)
r_fd = np.sqrt(S_GGE_FD / np.pi)
r_fd_max = np.sqrt(S_max_FD / np.pi)

circle_sh = plt.Circle((0, 0), r_sh, color='#2196F3', alpha=0.3, label=f'Shannon S={S_GGE_Shannon:.3f}')
circle_max = plt.Circle((0, 0), r_max, color='#2196F3', alpha=0.1, linestyle='--')
circle_fd = plt.Circle((0, 0), r_fd, color='#FF9800', alpha=0.2, label=f'FD S={S_GGE_FD:.3f}')
ax.add_patch(circle_max)
ax.add_patch(circle_fd)
ax.add_patch(circle_sh)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.legend(fontsize=9, loc='upper right')
ax.set_title('(h) Entropy Comparison', fontsize=11, fontweight='bold')
ax.text(0, 0, f'Shannon\n{S_GGE_Shannon:.3f}', ha='center', fontsize=10, fontweight='bold')
ax.text(0, -r_fd - 0.15, f'FD: {S_GGE_FD:.3f}', ha='center', fontsize=9, color='#FF9800')
ax.text(0, r_max + 0.1, f'S_max={S_max_Shannon:.3f}', ha='center', fontsize=8, color='#2196F3')

# --- Panel (i): Summary text ---
ax = fig.add_subplot(gs[2, 2])
ax.axis('off')
summary = (
    "EULER-DEFICIT-45 SUMMARY\n"
    "========================\n\n"
    f"Correct Euler: sum T_k S_k^Sh = {Euler_sum_Shannon:.12f}\n"
    f"                              = N_pair = 1 (EXACT)\n\n"
    f"S44 deficit:  E_GGE - sum T_k S_k^FD = {deficit_FD:.6f}\n"
    f"|E_cond|:                               {E_cond_MKK:.6f}\n"
    f"Ratio:                                  {deficit_FD/E_cond_MKK:.3f}\n\n"
    "S44 claim 'deficit = |E_cond|' is WRONG.\n"
    "The deficit is an artifact of using\n"
    "Fermi-Dirac entropy in a canonical\n"
    "N=1 system.\n\n"
    "Volovik parallel: wrong ensemble\n"
    "=> spurious vacuum energy."
)
ax.text(0.05, 0.95, summary, transform=ax.transAxes, fontsize=10,
        fontfamily='monospace', va='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

fig.suptitle('EULER-DEFICIT-45: The GGE Euler Deficit is an Ensemble Artifact\n'
             r'$\sum_k T_k S_k^{\rm Shannon} = N_{\rm pair} = 1$ (exact identity)',
             fontsize=13, fontweight='bold', y=0.99)

plt.savefig(os.path.join(SCRIPT_DIR, 's45_euler_deficit.png'), dpi=150, bbox_inches='tight')
print(f"Plot saved to: {os.path.join(SCRIPT_DIR, 's45_euler_deficit.png')}")

print("\nDone.")
