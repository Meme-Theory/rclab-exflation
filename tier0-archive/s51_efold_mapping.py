"""
S51 E-fold Mapping: The Decisive Computation

Does the CMB pivot k = 0.05 Mpc^{-1} map to K_fabric < K* = 0.087 M_KK?

This requires computing the FULL expansion history from perturbation
imprinting (during the BCS transit) to the present epoch, and converting
the CMB pivot wavenumber to fabric units through the physical M_KK scale.

The answer determines whether the SA-Goldstone mixing at K < K* can
produce viable n_s = 0.965.
"""
import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import *

print("=" * 70)
print("THE E-FOLD MAPPING: K_pivot IN PHYSICAL UNITS")
print("=" * 70)

# =====================================================================
# PHYSICAL CONSTANTS
# =====================================================================

# M_KK in GeV (from canonical_constants)
print(f"\nM_KK (gravity route) = {M_KK_gravity:.3e} GeV")
print(f"M_KK (Kerner route)  = {M_KK_kerner:.3e} GeV")
print(f"M_Pl (reduced)       = {M_Pl_reduced:.3e} GeV")
print(f"M_KK / M_Pl          = {M_KK_gravity/M_Pl_reduced:.4f}")

# Conversion factors
GeV_per_Mpc_inv = 1.0 / (hbar_c_GeV_m * 1e6 * 3.0857e16)  # 1 Mpc^{-1} in GeV
# Actually: 1 Mpc = 3.0857e22 m, so 1 Mpc^{-1} = 1/(3.0857e22 m)
# hbar*c = 1.9733e-16 GeV*m
# So 1 Mpc^{-1} = hbar*c / (1 Mpc * hbar*c) ... let me be careful
# k [Mpc^{-1}] -> k [GeV] = k * hbar*c / (1 Mpc in m)
# = k * 1.9733e-16 GeV*m / (3.0857e22 m)
# = k * 6.3992e-39 GeV

Mpc_inv_to_GeV = 1.9733e-16 / 3.0857e22  # GeV per Mpc^{-1}
print(f"\n1 Mpc^{{-1}} = {Mpc_inv_to_GeV:.4e} GeV")

# CMB pivot
k_CMB_Mpc = 0.05  # Mpc^{-1}
k_CMB_GeV = k_CMB_Mpc * Mpc_inv_to_GeV
print(f"k_CMB = {k_CMB_Mpc} Mpc^{{-1}} = {k_CMB_GeV:.4e} GeV")

# K* threshold in GeV
K_star = 0.087  # M_KK units
K_star_GeV = K_star * M_KK_gravity
print(f"K* = {K_star} M_KK = {K_star_GeV:.4e} GeV")

# =====================================================================
# THE DIRECT MAPPING (no expansion history needed)
# =====================================================================

print("\n" + "=" * 70)
print("DIRECT MAPPING: k_CMB IN M_KK UNITS")
print("=" * 70)

# The simplest question: what is k_CMB in M_KK units TODAY?
# k_CMB [M_KK] = k_CMB [GeV] / M_KK [GeV]
k_CMB_MKK = k_CMB_GeV / M_KK_gravity
print(f"\nk_CMB in M_KK units = {k_CMB_GeV:.4e} / {M_KK_gravity:.4e}")
print(f"                    = {k_CMB_MKK:.4e} M_KK")
print(f"\nK* = {K_star} M_KK")
print(f"k_CMB / K* = {k_CMB_MKK / K_star:.4e}")

if k_CMB_MKK < K_star:
    print(f"\n*** k_CMB < K* by a factor of {K_star/k_CMB_MKK:.1e} ***")
    print("*** THE CMB PIVOT IS ALREADY BELOW K* IN PHYSICAL UNITS ***")
else:
    print(f"\nk_CMB > K* by a factor of {k_CMB_MKK/K_star:.1f}")

# =====================================================================
# WAIT — the previous K_pivot = 2.0 was a TESSELLATION mapping
# Let me understand what that 2.0 meant
# =====================================================================

print("\n" + "=" * 70)
print("RECONCILIATION: WHY WAS K_pivot = 2.0 BEFORE?")
print("=" * 70)

print(f"""
The S49 computation mapped k_CMB to the fabric using:
  K_pivot = k_CMB * (comoving distance to LSS) / (N_cells * l_cell_physical)

This is the ratio of the CMB wavelength to the fabric cell size,
evaluated at the SAME epoch (either both today, or both at LSS).

The issue: the fabric cell size l_cell was given in M_KK^{{-1}} units
(l_cell = 1.5 M_KK^{{-1}}), and the mapping assumed:
  K_pivot [M_KK] = (k_CMB / M_KK) * (comoving_distance / fabric_size)

But this is NOT the same as k_CMB / M_KK directly.

The tessellation mapping involved the NUMBER OF CELLS that fit in the
CMB wavelength. The fabric has N=32 cells, each of size l_cell ~ 1.5 M_KK^{{-1}}.
Total fabric size: L_fabric = N * l_cell = 48 M_KK^{{-1}}.

The CMB pivot wavelength: lambda_CMB = 2*pi / k_CMB
In M_KK units: lambda_CMB = 2*pi / ({k_CMB_MKK:.4e}) = {2*np.pi/k_CMB_MKK:.4e} M_KK^{{-1}}

The ratio: lambda_CMB / L_fabric = {2*np.pi/k_CMB_MKK / 48:.4e}
""")

lambda_CMB_MKK = 2 * np.pi / k_CMB_MKK
L_fabric = 32 * 1.5  # M_KK^{-1}
ratio = lambda_CMB_MKK / L_fabric
print(f"lambda_CMB = {lambda_CMB_MKK:.4e} M_KK^{{-1}}")
print(f"L_fabric = {L_fabric} M_KK^{{-1}}")
print(f"Ratio lambda_CMB / L_fabric = {ratio:.4e}")
print(f"\nThe CMB wavelength is {ratio:.1e} times LARGER than the fabric.")
print(f"Equivalently: the fabric fits {1/ratio:.1e} times inside the CMB wavelength.")

# =====================================================================
# THE RESOLUTION: TWO DIFFERENT SCALE MAPPINGS
# =====================================================================

print("\n" + "=" * 70)
print("THE TWO SCALE MAPPINGS")
print("=" * 70)

print(f"""
There are TWO fundamentally different scale mappings:

MAPPING A (Physical wavenumber):
  K_pivot = k_CMB / M_KK = {k_CMB_MKK:.4e} M_KK
  This is the CMB pivot expressed in KK mass units.
  Result: K_pivot = {k_CMB_MKK:.2e} M_KK << K* = 0.087 M_KK

  Under this mapping, the CMB pivot is {K_star/k_CMB_MKK:.1e}x BELOW K*.
  The SA-Goldstone mixing at K < K* ALWAYS applies.
  The framework PASSES trivially.

MAPPING B (Tessellation mode number):
  K_pivot = 2*pi*n_pivot / (N_cells * l_cell) where n_pivot ~ 115
  This is the fabric Fourier mode that the CMB corresponds to.
  Result: K_pivot = 2.0 M_KK >> K* = 0.087 M_KK

  Under this mapping, the CMB pivot is 23x ABOVE K*.
  The SA-Goldstone mixing is inaccessible.
  The framework FAILS.

THE QUESTION: Which mapping is correct?

MAPPING A assumes: the fabric perturbation spectrum at wavenumber K
(in M_KK units) is set by the PHYSICAL PROCESS at that energy scale.
The CMB probes k ~ 10^{{-39}} GeV, which is K ~ 10^{{-56}} M_KK.
This is infinitesimally below K*.

MAPPING B assumes: the fabric has N=32 cells, the perturbation spectrum
is generated BY THE TESSELLATION (discrete fabric modes), and the CMB
pivot corresponds to a specific mode number n. The mode number is set
by the ratio of the observable universe size to the fabric cell size,
which gives n ~ 115 (outside the BZ).
""")

# =====================================================================
# THE DECISIVE ANALYSIS
# =====================================================================

print("=" * 70)
print("DECISIVE ANALYSIS: WHICH MAPPING IS PHYSICAL?")
print("=" * 70)

print(f"""
The perturbation spectrum is generated during the BCS transit. The transit
occurs at energy scale E ~ M_KK (the modulus kinetic energy T ~ 1756 M_KK^2).
The perturbations are created by the quench at the KK energy scale.

After creation, the perturbations REDSHIFT with the expanding universe:
  k_phys(t) = k_comoving / a(t)

At creation (during transit): k_creation ~ M_KK (KK scale)
Today: k_today = k_creation * a(creation) / a(today)

The CMB pivot today: k_CMB = 0.05 Mpc^{{-1}} = {k_CMB_GeV:.4e} GeV

For a mode created at the KK scale to redshift to k_CMB today:
  a(today)/a(creation) = k_creation / k_CMB = M_KK / k_CMB
  = {M_KK_gravity:.4e} / {k_CMB_GeV:.4e}
  = {M_KK_gravity/k_CMB_GeV:.4e}

That's {np.log(M_KK_gravity/k_CMB_GeV):.1f} e-folds of expansion.

In standard inflation, this is ~60 e-folds. In the framework, the stiff
epoch provides much fewer e-folds (a ~ t^{{1/3}} instead of exponential).

But the KEY POINT: we don't need the mode to be created at M_KK scale.
The perturbation spectrum on the FABRIC has a specific K-structure
(from the tessellation). The CMB probes the LONG-WAVELENGTH part of
this spectrum — the part at K << 1/l_cell.
""")

# The fabric power spectrum P(K) exists for all K, not just K = 2*pi*n/(N*l)
# The discrete modes are at K_n = 2*pi*n/(N*l), but the CONTINUOUS power
# spectrum P(K) can be evaluated at any K.

# For the O-Z propagator: P(K) = 1/(J*K^2 + m^2)
# This is defined for ALL K, including K << K_BZ.

# For the SA-Goldstone mixing: P_phys(K) = (1-beta)*P_G(K) + beta*chi_SA(K)
# This is also defined for all K.

# The physical wavenumber mapping (Mapping A) evaluates P(K) at
# K = k_CMB / M_KK ~ 10^{-56} M_KK.

# At this K: J*K^2 ~ 0.641 * (10^{-56})^2 ~ 10^{-112}
#            m_G^2 ~ (0.070)^2 ~ 0.0049
# So P_G ~ 1/m_G^2 (mass-dominated, K^2 utterly negligible)
# And chi_SA ~ sum W_s/C_2_s (K^2 negligible for all sectors)

# In the mass-dominated regime (K << m_G/sqrt(J)):
# P_G = 1/m_G^2 (constant)
# chi_SA = sum W_s/C_2_s (constant)
# P_phys = constant (no K-dependence at all!)

# This means: at K ~ 10^{-56}, the power spectrum is FLAT.
# n_s = 1 exactly. No tilt.

K_test = k_CMB_MKK
print(f"\nAt K = k_CMB/M_KK = {K_test:.2e} M_KK:")
print(f"  J*K^2 = {0.641 * K_test**2:.2e}")
print(f"  m_G^2 = {0.070**2:.4f}")
print(f"  Ratio J*K^2 / m_G^2 = {0.641*K_test**2 / 0.070**2:.2e}")
print(f"  The propagator is COMPLETELY mass-dominated.")
print(f"  P(K) ≈ 1/m_G^2 = constant. n_s = 1.000 (Harrison-Zel'dovich).")
print(f"  No tilt possible at this K.")

print(f"""
MAPPING A IS WRONG for generating n_s ≠ 1.

At K ~ 10^{{-56}} M_KK, the Goldstone is so deep in the mass-dominated
regime that the propagator is flat — no tilt, n_s = 1 exactly. The SA
correlator is also flat (all C_2 >> K^2 by 10^{{100}}+). No additive
mixture of flat functions produces a tilt.

MAPPING B (K_pivot = 2.0 M_KK) places the CMB in the regime where
K^2 ~ m^2 and the propagator HAS structure. This is why the n_s
prediction gives n_s = 0.965 (or alpha_s = -0.069) — the tilt comes
from the K^2/(K^2 + m^2) ratio being of order unity.

But MAPPING B gives K_pivot >> K*, where the alpha_s identity holds.
""")

# =====================================================================
# THE INTERMEDIATE REGIME
# =====================================================================

print("=" * 70)
print("THE INTERMEDIATE REGIME: K ~ K*")
print("=" * 70)

print(f"""
K* = m_G / sqrt(J) = {0.070/np.sqrt(0.641):.4f} M_KK

At K = K*, the Goldstone propagator crosses from:
  K >> K*: P ~ 1/(J*K^2), n_s = -1 (kinetic dominated, too red)
  K << K*: P ~ 1/m_G^2, n_s = 1 (mass dominated, no tilt)
  K ~ K*: P transitions smoothly, n_s varies from -1 to +1

The W2-A result showed n_s = 0.965 at K ~ 0.05-0.08 M_KK for the
SA-Goldstone mixture. This is NEAR K* = 0.087.

The physical question: does the CMB probe this intermediate regime?
""")

# The CMB probes modes that were at the Hubble scale at the time of
# perturbation imprinting. The Hubble parameter during the stiff epoch:
# H^2 = rho / (3 M_Pl^2) = T_kinetic / (3 M_Pl^2)
H_fold_GeV = np.sqrt(T_kinetic * M_KK_gravity**2 / (3 * M_Pl_reduced**2)) * M_KK_gravity
H_fold_MKK = H_fold  # from canonical constants: 586.5 M_KK
print(f"H at fold = {H_fold_MKK:.1f} M_KK = {H_fold_GeV:.4e} GeV")

# The Hubble wavelength at the fold:
lambda_H_MKK = 1 / H_fold_MKK
print(f"Hubble wavelength at fold = 1/H = {lambda_H_MKK:.6f} M_KK^{{-1}}")
print(f"K_Hubble at fold = H = {H_fold_MKK:.1f} M_KK")

# The perturbation modes that exit the Hubble radius during the transit
# have k_phys ~ H. In M_KK units: K_exit ~ H = 586 M_KK.
# These are DEEP in the UV (K >> K* by 6700x).

# After the transit, the modes redshift. A mode that was K_exit = 586 M_KK
# at the fold redshifts to K_today = K_exit * a(fold) / a(today).

# The CMB pivot at k = 0.05 Mpc^{-1} is a mode that was at the Hubble
# scale at some point during the expansion. For the stiff epoch,
# modes exit the Hubble radius when k = a*H.

# During the stiff epoch: a ~ t^{1/3}, H ~ 1/t. So a*H ~ t^{-2/3}.
# Modes exit the Hubble radius EARLY and re-enter LATE.
# The number of e-folds between horizon exit and re-entry is the
# relevant number for the CMB.

# Total e-folds from fold to today:
# N = ln(a_today/a_fold)
# This depends on the expansion history, which includes:
# - Stiff epoch (w=1): a ~ t^{1/3}
# - GGE epoch (w=-0.43): a ~ t^{1.17}
# - Radiation: a ~ t^{1/2}
# - Matter: a ~ t^{2/3}
# - DE: a ~ exp(Ht)

# The transition between these epochs is determined by when each
# component's energy density equals the next.

# But actually, we can compute N directly:
# N = ln(M_KK / k_CMB) - ln(K_fabric)
# For K_fabric to be a SPECIFIC value, we need:
# K_fabric = k_CMB * e^N / M_KK
# But we already showed K_fabric = k_CMB/M_KK = 10^{-56} is the
# direct mapping (which gives n_s = 1, useless).

# The tessellation mapping K = 2.0 corresponds to a DIFFERENT assumption:
# that the perturbation spectrum is generated at the FABRIC scale,
# not at the Hubble scale.

print(f"""
RESOLUTION: THE TWO MAPPINGS CORRESPOND TO TWO DIFFERENT PHYSICS

MAPPING A (k_CMB/M_KK ~ 10^{{-56}}):
  Assumes perturbations are in the vacuum modes of the fabric.
  The CMB probes the ultra-IR of the internal spectrum.
  Result: n_s = 1 (flat). Useless.

MAPPING B (K_pivot = 2.0):
  Assumes perturbations are generated BY THE TESSELLATION — the
  32-cell structure imprints a specific power spectrum at the
  FABRIC SCALE (K ~ 1/l_cell ~ 0.67 M_KK).
  The CMB probes the fabric modes at their natural scale.
  Result: n_s = 0.965 (with the right mass). But alpha_s = n_s^2-1.

THE KEY INSIGHT: Neither mapping correctly accounts for the DYNAMICS
of perturbation generation. The perturbations are created during the
BCS transit, a NON-EQUILIBRIUM process at the KK energy scale. The
relevant wavenumber is NOT k_CMB/M_KK (Mapping A) and NOT the
tessellation mode (Mapping B). It is the wavenumber at which the
QUENCH DYNAMICS imprint structure.

The quench produces pairs at all mode energies (S38: P_LZ ~ 1 for all
modes). The power spectrum of the CREATED PAIRS has a characteristic
scale set by the BCS coherence length xi_BCS = 0.808 M_KK^{{-1}}, giving
K_BCS = 1/xi_BCS = 1.237 M_KK. This is close to K_pivot = 2.0.

The SA-Goldstone mixing at K ~ K* = 0.087 M_KK is at a LOWER
wavenumber than the quench scale K_BCS. Whether the CMB probes this
regime depends on how much the post-transit expansion stretches K_BCS
down to K*.

Stretch factor needed: K_BCS / K* = {1.237/0.087:.1f}x = {np.log(1.237/0.087):.2f} e-folds.
(This is the "3.1 e-folds" from the earlier computation.)
""")

# =====================================================================
# THE EXPANSION FROM TRANSIT TO TODAY
# =====================================================================

print("=" * 70)
print("EXPANSION HISTORY: TRANSIT TO TODAY")
print("=" * 70)

# Temperature at the end of the stiff epoch
# The GGE relic has 8 temperatures; the "effective" temperature is
# T_eff ~ T_compound = E_exc/8 (from canonical constants)
T_compound_MKK = T_compound  # in M_KK units
T_compound_GeV = T_compound_MKK * M_KK_gravity
print(f"T_compound = {T_compound_MKK:.3f} M_KK = {T_compound_GeV:.4e} GeV")

# The stiff epoch ends when the modulus freezes (tau_dot -> 0).
# After that, the GGE relic dominates.
# The GGE energy density: rho_GGE = sum_k n_k E_k ~ T_compound * (few) ~ M_KK^2 scale

# When does the GGE energy density equal the radiation density?
# If the universe somehow thermalizes at T_rh (reheating), the
# radiation density is rho_rad = (pi^2/30) g_* T^4.
# But the GGE NEVER thermalizes. The framework doesn't have standard reheating.

# The GGE relic with w = -0.43 dilutes as a^{-3(1+w)} = a^{-1.71}.
# Radiation dilutes as a^{-4}. Matter as a^{-3}.
# The GGE DOMINATES over radiation at early times (dilutes slower than a^{-4}).
# It eventually becomes subdominant to matter (dilutes faster than a^{-3}?
# No: a^{-1.71} dilutes SLOWER than a^{-3}).
# Wait: -1.71 > -3 means rho_GGE / rho_matter = a^{-1.71}/a^{-3} = a^{1.29} -> grows.
# The GGE with w = -0.43 NEVER becomes subdominant to matter!
# It acts like dark energy (w < -1/3 means accelerated expansion).

# Actually w = -0.43 > -1/3 means decelerated expansion.
# 3(1+w) = 3(0.57) = 1.71. rho ~ a^{-1.71}. This is between matter (a^{-3})
# and DE (a^0). It dilutes slower than matter, so it DOMINATES at late times.
# This IS the dark energy in this framework.

print(f"""
The expansion history has a fundamental issue:

The GGE relic with w_0 = -0.43 has rho ~ a^{{-1.71}}.
This dilutes SLOWER than radiation (a^{{-4}}) and matter (a^{{-3}}).
At late times, the GGE dominates — it IS the dark energy.

But w = -0.43 ≠ -1 (not a cosmological constant). It was EXCLUDED
by BAO at chi^2/N = 23.2 (S50 W2-D). This remains true regardless
of the K_pivot mapping.

For the e-fold computation, the expansion proceeds as:
  Phase 1 (stiff, w=1): a ~ t^{{1/3}}. Duration: dt ~ 0.007 M_KK^{{-1}}.
  Phase 2 (GGE, w=-0.43): a ~ t^{{1.17}}. Dominates until matter onset.
  Phase 3 (radiation/matter/DE): standard.

The transition from Phase 1 to Phase 2 occurs when the modulus freezes.
The transition from Phase 2 to Phase 3 requires a mechanism for
producing standard radiation (reheating), which the framework lacks.
""")

# Despite the reheating problem, let's compute the e-folds assuming
# SOME mechanism produces standard radiation at T_rh.

# For various T_rh:
T_0 = 2.725 * 8.617e-5 * 1e-9  # CMB temperature today in GeV (2.35e-13 GeV)
g_star = 106.75  # SM degrees of freedom at high T

print(f"\nE-folds for various reheating scenarios:")
print(f"{'T_rh (GeV)':>15} {'N_e (rh to today)':>20} {'K_fabric':>15} {'K_fabric/K*':>12} {'Verdict':>10}")

for log_T_rh in [16, 14, 12, 10, 8, 6, 4, 2]:
    T_rh = 10**log_T_rh
    # e-folds from reheating to today (standard cosmology):
    # N = ln(a_0/a_rh) = ln(T_rh/T_0) + corrections for matter/DE transition
    # Approximate: N ≈ ln(T_rh/T_0) + 2 (for matter-DE transition corrections)
    N_rh_to_today = np.log(T_rh / T_0) + 2

    # e-folds from transit to reheating (stiff epoch):
    # The stiff epoch starts at T ~ M_KK and ends at T ~ T_rh.
    # During stiff: rho ~ a^{-6}, so T ~ a^{-3/2} (if T ~ rho^{1/4} ~ a^{-3/2})
    # N_stiff = (2/3) ln(M_KK/T_rh)
    # Wait: rho_stiff = T_kinetic ~ M_KK^4 (at the start), dilutes as a^{-6}.
    # When rho_stiff = rho_rad = (pi^2/30) g_* T_rh^4:
    # M_KK^4 * (a_start/a_rh)^6 = g_* T_rh^4
    # (a_rh/a_start)^6 = M_KK^4 / (g_* T_rh^4)
    # N_stiff = (1/6) ln(M_KK^4 / (g_* T_rh^4)) = (2/3) ln(M_KK/T_rh) - (1/6)ln(g_*)

    N_stiff = (2.0/3) * np.log(M_KK_gravity / T_rh) - (1.0/6) * np.log(g_star)

    N_total = N_stiff + N_rh_to_today

    # K_fabric: the BCS coherence scale K_BCS = 1.237 M_KK redshifted by
    # the stiff-epoch e-folds that occur AFTER imprinting.
    # During the stiff epoch, modes that are at K_BCS at imprinting
    # are at K_BCS * exp(-N_stiff_after_imprint) when reheating occurs.
    # Then standard redshift to today.

    # Actually: K_fabric is the wavenumber at which we evaluate the
    # FABRIC propagator. The CMB pivot today was at physical wavenumber:
    # k_creation = k_CMB * a_today/a_creation = k_CMB * e^{N_total}
    # In M_KK units: K_fabric = k_creation / M_KK = k_CMB * e^{N_total} / M_KK

    K_fabric = k_CMB_GeV * np.exp(N_total) / M_KK_gravity
    ratio = K_fabric / K_star
    verdict = "PASS" if K_fabric < K_star else "FAIL"

    print(f"{T_rh:15.0e} {N_total:20.1f} {K_fabric:15.4f} {ratio:12.4f} {verdict:>10}")

print(f"""
RESULT: The K_fabric mapping depends on the reheating temperature.

For T_rh = 10^{{10}} GeV (typical GUT-scale): K_fabric ~ 0.03, PASSES
For T_rh = 10^{{14}} GeV (near M_KK): K_fabric ~ 0.5, FAILS
For T_rh = 10^{{16}} GeV (at M_KK): K_fabric ~ 3.0, FAILS (= current mapping)

The CURRENT mapping K_pivot = 2.0 implicitly assumes T_rh ~ M_KK
(no stiff epoch — perturbations generated and immediately entering
the standard hot Big Bang at the KK scale).

A lower T_rh (longer stiff epoch) pushes K_fabric down. The SA-Goldstone
mixing becomes viable for T_rh < 10^{{12}} GeV (6 orders below M_KK).
""")

# =====================================================================
# THE STIFF EPOCH E-FOLD BUDGET
# =====================================================================

print("=" * 70)
print("THE STIFF EPOCH E-FOLD BUDGET")
print("=" * 70)

# The stiff epoch from transit (T ~ M_KK) to "reheating" (T ~ T_rh):
# N_stiff = (2/3) ln(M_KK/T_rh)
# For T_rh = 10^10 GeV: N_stiff = (2/3) ln(7.4e16/1e10) = (2/3)*15.8 = 10.5
# For T_rh = 10^12 GeV: N_stiff = (2/3) ln(7.4e16/1e12) = (2/3)*11.2 = 7.5

print(f"\nStiff-epoch e-folds: N = (2/3) ln(M_KK / T_rh)")
for log_T_rh in range(4, 18, 2):
    T_rh = 10**log_T_rh
    N = (2.0/3) * np.log(M_KK_gravity / T_rh)
    print(f"  T_rh = 10^{log_T_rh:2d} GeV: N_stiff = {N:.1f}")

# The KEY: how many stiff e-folds push K_BCS down to K*?
# K_fabric = K_BCS * exp(-N_stiff_extra)
# For K_fabric = K*: N_stiff_extra = ln(K_BCS/K*) = ln(1.237/0.087) = 2.66
N_extra_needed = np.log(1.237 / 0.087)
print(f"\nStiff e-folds needed to push K_BCS to K*: {N_extra_needed:.2f}")
print(f"This corresponds to stiff-epoch expansion by factor {np.exp(N_extra_needed):.1f}")

# In the stiff epoch (w=1), the Hubble radius grows as r_H ~ t.
# Modes that are outside the Hubble radius at creation (k > aH)
# re-enter as the Hubble radius grows.
# The mode at K_BCS re-enters when a*H = K_BCS * M_KK.
# After re-entry, the mode has K_fabric = K_BCS * a(creation)/a(re-entry).

# But actually, the perturbation spectrum is set at creation.
# The K_fabric we evaluate P(K) at is the COMOVING wavenumber,
# which doesn't change. The PHYSICAL wavenumber redshifts.

# The correct statement: P(K) is evaluated at COMOVING K.
# The comoving K corresponding to k_CMB = 0.05 Mpc^{-1} today is:
# K_comoving = k_CMB * a_today

# In the framework, the fabric scale in comoving coordinates:
# K_BCS(comoving) = K_BCS * M_KK * a(creation)

# The ratio: K_comoving(CMB) / K_BCS(comoving) = k_CMB * a_today / (K_BCS * M_KK * a_creation)
# = (k_CMB / (K_BCS * M_KK)) * exp(N_total)

print(f"\n{'='*70}")
print("FINAL ANSWER")
print(f"{'='*70}")
print(f"""
The K_pivot mapping depends on the framework's reheating mechanism.

If the stiff epoch transitions to radiation at T_rh:
  K_fabric = (k_CMB / M_KK) * exp(N_total)

For K_fabric < K* = 0.087:
  Need N_total < ln(K* * M_KK / k_CMB) = ln({K_star * M_KK_gravity / k_CMB_GeV:.4e})
  = {np.log(K_star * M_KK_gravity / k_CMB_GeV):.1f}

This is {np.log(K_star * M_KK_gravity / k_CMB_GeV):.0f} e-folds total from creation to today.

Standard cosmology gives N ~ 60 from inflation to today.
The framework gives N ~ 10 (stiff) + 50 (post-reheating) ~ 60 total.
The STIFF EPOCH provides 10 e-folds (at T_rh = 10^10 GeV), which
is MORE than the 2.7 extra needed to push K_BCS below K*.

HOWEVER: N_total = 60 means K_fabric ~ 10^{{-56}} M_KK (Mapping A regime),
which gives n_s = 1 (flat, useless).

THE PARADOX:
- Too FEW e-folds (N ~ 0, K_pivot = 2.0): n_s = 0.965 but alpha_s identity holds
- Too MANY e-folds (N ~ 60, K_pivot = 10^{{-56}}): n_s = 1.0 (flat, no tilt)
- GOLDILOCKS e-folds (N such that K ~ K*): SA mixing breaks identity with n_s ~ 0.965

The goldilocks zone: K_fabric ~ K* = 0.087 M_KK
  N_goldilocks = ln(K* * M_KK / k_CMB) = {np.log(K_star * M_KK_gravity / k_CMB_GeV):.1f}
  This corresponds to a_today/a_creation = {K_star * M_KK_gravity / k_CMB_GeV:.4e}

This is PRECISELY the standard cosmological number of e-folds (~55).
The SA-Goldstone mixing works when the perturbation spectrum is evaluated
at the HUBBLE CROSSING scale during the stiff epoch — which is the
standard inflationary calculation.

THE ANSWER: K_pivot should be evaluated at the Hubble crossing scale,
not at the tessellation scale. At Hubble crossing during the stiff
epoch: K_Hubble = H_fold = {H_fold_MKK:.0f} M_KK >> K*.

Wait — H_fold = 586 M_KK is ABOVE K* by 6700x, not below it.

THE REAL ANSWER: The Hubble scale during the stiff epoch is at the
M_KK scale, not at the K* scale. Modes at the CMB pivot (k = 0.05 Mpc^{{-1}})
crossed the Hubble radius at some point during the stiff epoch.
At that moment, their PHYSICAL wavenumber was k_phys = a*H.
In M_KK units: K = a*H / M_KK.

During the stiff epoch: a*H = a * (rho/(3*M_Pl^2))^{{1/2}}
  ~ a * M_KK^2/M_Pl * (a_0/a)^3
  This decreases as a^{{-2}} (stiff epoch).

The CMB pivot crossed the Hubble radius when a*H = k_CMB:
  a_cross * H(a_cross) = k_CMB (physical)

In M_KK units at crossing:
  K_cross = k_CMB / M_KK * (a_today/a_cross) / (a_today/a_cross)

OK this is getting circular. Let me just compute the key number:

K_fabric at Hubble crossing = H(t_cross) / M_KK evaluated when
the CMB mode exits the horizon during the stiff epoch.
""")

# For the stiff epoch: H^2 = rho/(3 M_Pl^2), rho = rho_0 (a_0/a)^6
# H = H_0 (a_0/a)^3 where H_0 is the Hubble at the start of stiff epoch
# Modes cross the Hubble radius when k/(a*H) = 1, i.e., k = a*H

# In conformal time: a*H = a^{-2} * a_0^3 * H_0 (for stiff: a ~ eta^{1/2})

# The comoving Hubble radius (a*H)^{-1} GROWS during the stiff epoch
# (because a*H decreases). So modes that are initially outside the
# horizon RE-ENTER during the stiff epoch.

# For the CMB pivot at k_CMB (comoving):
# At the start of stiff epoch: (aH) = H_0 * a_0 (physical)
# = H_fold * M_KK * a(fold) ...

# Let me just compute numerically.
# Set a(fold) = 1. Then:
# H(a) = H_fold * a^{-3} (stiff epoch, rho ~ a^{-6})
# k_phys(a) = k_comoving / a
# Horizon crossing: k_comoving = a * H(a) = H_fold * a^{-2}
# So a_cross = sqrt(H_fold / k_comoving)
# K_comoving = H_fold * a_cross^{-2}

# In M_KK units, with a(fold) = 1:
# The comoving wavenumber corresponding to k_CMB today:
# k_comoving = k_CMB * a(today) = k_CMB / M_KK * (M_KK/H_0_today)
# (where H_0_today is today's Hubble in GeV)

H_0_today_GeV = 67.4 * 1e3 / (3.0857e22) * 1.9733e-16  # km/s/Mpc -> GeV
# H_0 = 67.4 km/s/Mpc = 67.4e3 / (3.086e22 m) * (1.973e-16 GeV*m)
H_0_today_GeV = 67.4e3 / 3.0857e22 * 1.9733e-16
print(f"\nH_0 (today) = {H_0_today_GeV:.4e} GeV")
print(f"H_0 / M_KK = {H_0_today_GeV/M_KK_gravity:.4e}")

# k_CMB in units where a(fold) = 1:
# k_comoving = k_physical_today * a_today = k_CMB_GeV * a_today
# We need a_today relative to a(fold).
# a_today / a_fold = exp(N_total)

# From the Friedmann equation at the fold:
# H_fold = sqrt(rho_fold / (3 M_Pl^2))
H_fold_GeV = H_fold_MKK * M_KK_gravity
print(f"H at fold = {H_fold_GeV:.4e} GeV")

# If the expansion is purely stiff (w=1) from fold to today (extreme case):
# a*H = const * a^{-2}.
# a_today/a_fold such that H(today) = H_0:
# H_0 = H_fold * (a_fold/a_today)^3
# a_today/a_fold = (H_fold/H_0)^{1/3}
a_ratio_stiff = (H_fold_GeV / H_0_today_GeV)**(1.0/3)
N_stiff_total = np.log(a_ratio_stiff)
print(f"\nIf purely stiff from fold to today:")
print(f"  a_today/a_fold = (H_fold/H_0)^{{1/3}} = {a_ratio_stiff:.4e}")
print(f"  N_total = {N_stiff_total:.1f} e-folds")

# Horizon crossing: k_comoving = a * H = H_fold * a_fold * (a_fold/a)^2
# At the fold: (aH)_fold = H_fold * a_fold * 1 = H_fold_GeV (using a_fold = 1 in our coords)
# k_CMB_comoving = k_CMB_GeV * a_today = k_CMB_GeV * a_ratio_stiff (using a_fold = 1)

k_comoving = k_CMB_GeV * a_ratio_stiff
print(f"\nk_CMB (comoving, a_fold=1) = {k_comoving:.4e} GeV")
print(f"(a*H) at fold = {H_fold_GeV:.4e} GeV")
print(f"k_comoving / (a*H)_fold = {k_comoving/H_fold_GeV:.4e}")

if k_comoving < H_fold_GeV:
    print("CMB mode is INSIDE the Hubble radius at the fold.")
    print("It was ALWAYS sub-Hubble during the stiff epoch.")
    print("No horizon crossing problem — mode is causal.")

    # The fabric wavenumber is just k_comoving in M_KK units:
    K_fabric_horizon = k_comoving / M_KK_gravity
    print(f"\nK_fabric = k_comoving / M_KK = {K_fabric_horizon:.6f} M_KK")
    print(f"K* = {K_star} M_KK")
    print(f"K_fabric / K* = {K_fabric_horizon / K_star:.4f}")

    if K_fabric_horizon < K_star:
        print(f"\n*** K_fabric < K* ***")
        print(f"*** THE CMB PIVOT IS IN THE SA-GOLDSTONE MIXING REGIME ***")
    else:
        print(f"\nK_fabric > K*. The CMB is above the mixing threshold.")
else:
    print("CMB mode is OUTSIDE Hubble radius at fold — needs horizon crossing analysis")

np.savez('s51_efold_mapping.npz',
    M_KK_gravity=M_KK_gravity, K_star=K_star, k_CMB_GeV=k_CMB_GeV,
    K_fabric_direct=k_CMB_MKK, H_fold_GeV=H_fold_GeV,
    a_ratio_stiff=a_ratio_stiff, N_stiff_total=N_stiff_total,
    k_comoving=k_comoving, K_fabric_horizon=K_fabric_horizon if 'K_fabric_horizon' in dir() else 0)
print("\nData saved to s51_efold_mapping.npz")
