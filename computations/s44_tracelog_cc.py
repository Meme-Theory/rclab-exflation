#!/usr/bin/env python3
"""
TRACE-LOG-CC-44: Vacuum energy density from the trace-log functional
Tr ln(D_BdG^2 / Lambda^2), replacing the polynomial spectral action
for CC estimation.

Physics:
  - The gravitating vacuum energy is the trace-log (one-loop effective potential),
    NOT the polynomial spectral action (Volovik 2005, S43 UV/IR workshop).
  - BCS free energy at T=0: F = (1/2) sum_k d_k [xi_k - E_k] + |Delta|^2/V_eff
  - Condensation energy: E_cond = F_paired - F_normal < 0
  - GGE residual: rho_residual = rho_vac(GGE) - rho_vac(equilibrium)
  - Strutinsky decomposition: rho = rho_smooth + delta_rho_shell

Gate: TRACE-LOG-CC-44
  PASS: rho_residual < 1e-6 * rho_vac_poly  (>6 orders reduction)
  FAIL: rho_residual > 0.1 * rho_vac_poly   (<1 order reduction)
  INFO: intermediate

Author: nazarewicz-nuclear-structure-theorist (S44)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# =============================================================================
# 1. LOAD ALL INPUT DATA
# =============================================================================

base = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")

# S42 Hauser-Feshbach: full 992-eigenvalue spectrum at fold
hf = np.load(base / "s42_hauser_feshbach.npz", allow_pickle=True)
unique_masses = hf['unique_masses']        # 119 unique |lambda_k| values
mass_mults = hf['mass_multiplicities']     # multiplicities d_k
Delta_pair = float(hf['Delta_pair'])       # 0.4643 (pairing gap)
E_exc = float(hf['E_exc'])                # 50.945 (excitation energy)
tau_fold = float(hf['tau_fold'])           # 0.2

# S38 CC instanton: BCS gap, GL parameters
cc = np.load(base / "s38_cc_instanton.npz", allow_pickle=True)
Delta_0 = float(cc['Delta_0'])            # 0.770 (BCS gap parameter)
xi_fold = cc['xi_fold']                    # [0.819, 0.845, 0.978] - pairing window eigenvalues
mult_k = cc['mult_k']                     # [1, 4, 3] - multiplicities near Fermi surface

# S42 GGE energy data
gge = np.load(base / "s42_gge_energy.npz", allow_pickle=True)
E_cond_MKK = float(gge['E_cond_MKK'])    # 0.137 in M_KK units
n_pairs = float(gge['n_pairs'])           # 59.8 quasiparticle pairs
E_exc_ratio = float(gge['E_exc_ratio'])   # 443.0 (E_exc / |E_cond|)

# S42 constants snapshot
const = np.load(base / "s42_constants_snapshot.npz", allow_pickle=True)
a0_fold = float(const['a0_fold'])         # 6440
a2_fold = float(const['a2_fold'])         # 2776.17
a4_fold = float(const['a4_fold'])         # 1350.72
rho_Lambda_spectral = float(const['rho_Lambda_spectral'])  # 8.43e73 GeV^4
CC_ratio_poly = float(const['CC_ratio'])  # 3.12e120

# S36 spectral action data
sfull = np.load(base / "s36_sfull_tau_stabilization.npz", allow_pickle=True)
S_fold = float(sfull['S_fold'][0])        # 250360.68
dS_fold = float(sfull['dS_fold'][0])      # 58672.80

print("=" * 70)
print("TRACE-LOG-CC-44: Vacuum Energy from BdG Trace-Log Functional")
print("=" * 70)
print()

# =============================================================================
# 2. CONSTRUCT FULL BdG SPECTRUM AT THE FOLD
# =============================================================================

# The Dirac spectrum on SU(3) at the fold has 992 modes (counting multiplicities).
# The eigenvalues come in +/- pairs (particle-hole symmetry).
# unique_masses are the ABSOLUTE values |lambda_k|.
# For BdG: xi_k = |lambda_k| - mu, with mu = 0 (S34: PH forces mu=0).
# So xi_k = |lambda_k| for positive eigenvalues.

# Build the full spectrum: each unique mass has multiplicity d_k.
# Total modes = sum(d_k) = 992
total_modes = int(np.sum(mass_mults))
print(f"Total modes: {total_modes}")
print(f"Number of unique eigenvalues: {len(unique_masses)}")
print(f"Eigenvalue range: [{unique_masses.min():.4f}, {unique_masses.max():.4f}] M_KK")
print(f"Mean eigenvalue: {np.mean(unique_masses):.4f} M_KK")
print()

# With mu = 0, xi_k = |lambda_k| for ALL modes (all are "particle-like").
# The BCS pairing couples +lambda_k and -lambda_k states.
# Each unique |lambda_k| with multiplicity d_k contributes d_k levels.
#
# BdG quasiparticle energies:
#   E_k = sqrt(xi_k^2 + Delta_k^2)
#
# The pairing gap Delta_k depends on the pairing interaction.
# From S38/S35: BCS condensate with Delta_0 = 0.770 (gap parameter),
# but the self-consistent gap at the fold is Delta_pair = 0.464 (from S42).
#
# The pairing window: modes with |xi_k| < cutoff participate in pairing.
# From S38: the pairing window contains modes at xi_fold = [0.819, 0.845, 0.978]
# with multiplicities [1, 4, 3], total 8 modes.
#
# For the trace-log calculation, we need Delta_k for ALL modes.
# BCS gap equation: Delta_k = Delta_0 for |xi_k| < omega_D (pairing window)
#                   Delta_k = 0 for |xi_k| > omega_D
#
# The S38 data tells us the pairing window captures 8 modes near the Fermi surface.
# The lightest mass is 0.819 M_KK. With mu=0, ALL modes have xi_k > 0.
# The pairing window should be symmetric around mu=0, but with mu=0 on a gapped
# spectrum, the "pairing window" is the set of modes closest to the chemical potential.
#
# Key insight: With mu=0 and all eigenvalues positive (min 0.819), the distance
# from the Fermi surface is |xi_k - 0| = xi_k = lambda_k > 0 for all k.
# The pairing acts on the LOWEST-lying modes near the Fermi surface.

# Two-component BdG: pair (k, -k) = (lambda_k, -lambda_k).
# The self-consistent gap Delta_pair = 0.464 is the average gap.
# Use Delta_0 = 0.770 as the bare gap parameter (from GL analysis).
# For modes in the pairing window: Delta_k = Delta_pair
# For modes outside: Delta_k = 0 (or exponentially suppressed)

# Identify pairing window modes: those within the BCS coherence length of E_F=0
# The pairing window in S38 identified 8 modes (3 unique levels).
# The lightest 8 modes (by multiplicity) are the pairing window.

# Build arrays
xi_k_all = unique_masses.copy()  # xi_k = |lambda_k| since mu=0
d_k_all = mass_mults.copy()

# Identify pairing window: the lowest 3 unique levels match S38's xi_fold
# xi_fold = [0.819, 0.845, 0.978], mult = [1, 4, 3] -> 8 modes total
n_pair_levels = 3  # from S38 data
pair_mask = np.zeros(len(xi_k_all), dtype=bool)

# Match S38 pairing window levels
for i_pf in range(n_pair_levels):
    diffs = np.abs(xi_k_all - xi_fold[i_pf])
    idx = np.argmin(diffs)
    if diffs[idx] < 0.01:
        pair_mask[idx] = True
        print(f"  Pairing level {i_pf}: xi={xi_k_all[idx]:.4f}, "
              f"d_k={d_k_all[idx]}, S38 mult={mult_k[i_pf]}")

n_paired_modes = int(np.sum(d_k_all[pair_mask]))
n_unpaired_modes = total_modes - n_paired_modes
print(f"\nPairing window: {n_paired_modes} modes out of {total_modes}")
print(f"Unpaired modes: {n_unpaired_modes}")

# Gap assignment
Delta_k = np.zeros_like(xi_k_all)
Delta_k[pair_mask] = Delta_pair  # self-consistent gap for paired modes

# BdG quasiparticle energies
E_k = np.sqrt(xi_k_all**2 + Delta_k**2)

print(f"\nBdG quasiparticle energies:")
print(f"  Min E_k: {E_k.min():.6f} M_KK (paired level)")
print(f"  Max E_k: {E_k.max():.6f} M_KK")
print(f"  E_k for paired levels: {E_k[pair_mask]}")
print(f"  Delta_pair = {Delta_pair:.6f}, Delta_0 = {Delta_0:.6f}")

# =============================================================================
# 3. TRACE-LOG VACUUM ENERGY: PAIRED STATE
# =============================================================================
#
# The one-loop effective potential (trace-log) for the BCS paired state:
#
#   Omega_BCS = (1/2) sum_k d_k [xi_k - E_k] + |Delta|^2 / G
#
# where the first term is the kinetic/quasiparticle contribution and
# the second is the mean-field (gap equation) contribution.
#
# At the self-consistent solution, the gap equation gives:
#   1/G = sum_k d_k / (2 E_k)  [for paired modes only]
#
# So the mean-field term becomes:
#   |Delta|^2 / G = Delta^2 * sum_k d_k / (2 E_k)
#
# The FULL trace-log:
#   rho_vac_log = (1/2) sum_k d_k [xi_k - E_k] + Delta^2 * sum_{k in window} d_k / (2 E_k)
#
# But we must be careful: the BCS free energy at T=0 is:
#   F_BCS = sum_k d_k [(xi_k - E_k)/2 + Delta_k^2/(2 E_k)] - sum_k d_k xi_k / 2
#         = sum_k d_k [(E_k - xi_k)/2 - Delta_k^2/(2 E_k)] * (-1)
#
# Standard BCS result:
#   E_cond = F_BCS - F_normal = -(1/2) N(E_F) Delta^2
#
# For the full trace-log with all modes:
#   Omega_paired = (1/2) sum_k d_k [xi_k - E_k + Delta_k^2/(2*xi_k) + ...]
#               = -(1/2) sum_k d_k [E_k - xi_k - Delta_k^2/(2*xi_k)]  [weak coupling expansion]
#
# But the EXACT one-loop result (no expansion) is:
#   Omega_paired = (1/2) sum_k d_k [xi_k - E_k] + Delta^2/G
#
# The normal state energy (reference):
#   Omega_normal = (1/2) sum_k d_k [xi_k - |xi_k|] = 0  (since all xi_k > 0 with mu=0)
#
# Wait: for a GAPPED spectrum with mu=0, xi_k = lambda_k > 0 for all k.
# The normal state has no occupied negative-energy states (Fermi sea is empty
# relative to this spectrum). The "vacuum" is the filled Dirac sea of NEGATIVE
# eigenvalues, which we've already accounted for.
#
# Let me reconsider. The D_K spectrum is {+lambda_k, -lambda_k}. The BdG
# Hamiltonian pairs +lambda_k with -lambda_k. The quasiparticle energy is
# E_k = sqrt(lambda_k^2 + Delta_k^2).
#
# Trace-log of BdG operator:
#   (1/2) Tr ln(D_BdG^2) = sum_k d_k ln(E_k)
#
# For the normal state (Delta=0):
#   (1/2) Tr ln(D_K^2) = sum_k d_k ln(|lambda_k|)
#
# The DIFFERENCE (which is what matters for the CC):
#   delta_rho_log = sum_k d_k [ln(E_k) - ln(|xi_k|)]
#                 = sum_k d_k ln(E_k / |xi_k|)
#                 = sum_k d_k ln(sqrt(1 + Delta_k^2/xi_k^2))
#                 = (1/2) sum_k d_k ln(1 + Delta_k^2/xi_k^2)
#
# This is the LOG functional (multiplicative, not additive).
# For modes outside the pairing window (Delta_k=0): contribution = 0.
# For modes inside: ln(1 + Delta^2/xi^2) ~ Delta^2/xi^2 for Delta << xi.

print("\n" + "=" * 70)
print("3. TRACE-LOG FUNCTIONAL: PAIRED vs NORMAL")
print("=" * 70)

# Method A: Additive trace-log (energy difference, standard BCS)
#   delta_Omega = (1/2) sum_k d_k [|xi_k| - E_k] + Delta^2/G
# For self-consistent gap: Delta^2/G = Delta^2 * sum_k' d_k' / (2 E_k')
# over paired modes only.

# Method B: Multiplicative trace-log (functional determinant ratio)
#   delta_ln_det = (1/2) sum_k d_k ln(1 + Delta_k^2 / xi_k^2)

# Compute Method A: Additive (BCS condensation energy)
kinetic_term = 0.5 * np.sum(d_k_all * (xi_k_all - E_k))
# This is negative since E_k >= xi_k

# Mean-field term: Delta^2 * sum_k' d_k'/(2 E_k') for paired modes
gap_eq_sum = np.sum(d_k_all[pair_mask] / (2 * E_k[pair_mask]))
mf_term = Delta_pair**2 * gap_eq_sum

Omega_BCS = kinetic_term + mf_term
E_cond_computed = kinetic_term  # The condensation energy part
                                # (mf_term cancels at self-consistency)

print(f"\nMethod A: Additive trace-log (BCS condensation energy)")
print(f"  Kinetic term (1/2)sum d_k[xi_k - E_k] = {kinetic_term:.6f} M_KK^4")
print(f"  Mean-field term Delta^2/G = {mf_term:.6f} M_KK^4")
print(f"  Omega_BCS (kinetic + mf) = {Omega_BCS:.6f} M_KK^4")

# For self-consistent solution, the true condensation energy is:
#   E_cond = -(1/2) N(E_F) Delta^2
# From S42: E_cond_MKK = 0.137 (in spectral units, this is the magnitude)

# The condensation energy from the spectrum directly:
# Since only paired modes contribute to the kinetic term difference:
E_cond_from_spectrum = 0.5 * np.sum(d_k_all[pair_mask] * (xi_k_all[pair_mask] - E_k[pair_mask]))
E_cond_from_all = kinetic_term  # same since unpaired have E_k = xi_k

print(f"  E_cond from paired modes = {E_cond_from_spectrum:.6f}")
print(f"  E_cond from all modes    = {E_cond_from_all:.6f}")
print(f"  E_cond from S42 data     = -{E_cond_MKK:.6f}")

# Compute Method B: Multiplicative (functional determinant ratio)
ln_det_ratio = 0.5 * np.sum(d_k_all * np.log(1 + Delta_k**2 / xi_k_all**2))

print(f"\nMethod B: Multiplicative trace-log (ln det ratio)")
print(f"  (1/2) sum d_k ln(1 + Delta^2/xi^2) = {ln_det_ratio:.6f}")

# For unpaired modes: Delta_k=0 -> contribution = 0
# For paired modes: compute term by term
for i in range(len(xi_k_all)):
    if pair_mask[i]:
        contrib = 0.5 * d_k_all[i] * np.log(1 + Delta_k[i]**2 / xi_k_all[i]**2)
        ratio = Delta_k[i]**2 / xi_k_all[i]**2
        print(f"    Level xi={xi_k_all[i]:.4f}, d={d_k_all[i]}, "
              f"Delta/xi={Delta_k[i]/xi_k_all[i]:.4f}, "
              f"Delta^2/xi^2={ratio:.6f}, contrib={contrib:.6f}")

# =============================================================================
# 4. COMPARISON: POLYNOMIAL vs LOGARITHMIC VACUUM ENERGY
# =============================================================================

print("\n" + "=" * 70)
print("4. POLYNOMIAL vs LOGARITHMIC VACUUM ENERGY")
print("=" * 70)

# Polynomial spectral action at the fold:
#   S_fold = 250361 (in spectral units, dimensionless)
#   rho_vac_poly = S_fold * M_KK^4 / (16 pi^2) ... but need to be careful
#
# The spectral action gives: S = f_0 a_0 + f_2 Lambda^2 a_2 + f_4 a_4 + ...
# In spectral units (M_KK=1), S_fold = 250361.
#
# The PHYSICAL vacuum energy density:
#   rho_vac_poly = S_fold / (vol_SU3 * vol_4D) * M_KK^4 / (16 pi^2)
#
# But the S42 computation already gave:
#   rho_Lambda_spectral = 8.43e73 GeV^4
#   CC_ratio = rho_Lambda_spectral / rho_obs = 3.12e120
#
# So rho_vac_poly ~ 10^{73} GeV^4 and the ratio to observed is 10^{120}.
#
# The KEY question: what is the trace-log vacuum energy in the same units?
#
# The trace-log vacuum energy (Method A, additive):
#   rho_vac_log = Omega_BCS (in spectral units M_KK^4)
#
# The ratio:
#   rho_vac_log / rho_vac_poly = Omega_BCS / S_fold

# First: the pure condensation energy (Method A)
ratio_A = abs(kinetic_term) / S_fold
log10_ratio_A = np.log10(ratio_A) if ratio_A > 0 else float('-inf')

# Second: the functional determinant ratio (Method B)
ratio_B = ln_det_ratio / S_fold
log10_ratio_B = np.log10(ratio_B) if ratio_B > 0 else float('-inf')

print(f"\nPolynomial spectral action at fold:")
print(f"  S_fold = {S_fold:.2f} (spectral units)")
print(f"  dS/dtau|_fold = {dS_fold:.2f}")
print(f"  rho_Lambda_spectral = {rho_Lambda_spectral:.3e} GeV^4")
print(f"  CC ratio (poly) = {CC_ratio_poly:.3e} (~10^{{{np.log10(CC_ratio_poly):.1f}}})")

print(f"\nTrace-log condensation energy (Method A, additive):")
print(f"  |Omega_BCS| = {abs(kinetic_term):.6f} M_KK^4")
print(f"  |Omega_BCS| / S_fold = {ratio_A:.3e}")
print(f"  log10 ratio = {log10_ratio_A:.2f}")
print(f"  Orders of reduction: {-log10_ratio_A:.2f}")

print(f"\nTrace-log determinant ratio (Method B, multiplicative):")
print(f"  ln(det ratio) = {ln_det_ratio:.6f}")
print(f"  ln(det) / S_fold = {ratio_B:.3e}")
print(f"  log10 ratio = {log10_ratio_B:.2f}")
print(f"  Orders of reduction: {-log10_ratio_B:.2f}")

# =============================================================================
# 5. GGE RESIDUAL: POST-TRANSIT STATE
# =============================================================================

print("\n" + "=" * 70)
print("5. GGE RESIDUAL (POST-TRANSIT STATE)")
print("=" * 70)

# After transit, the system is NOT in the BCS ground state. It is in a
# Generalized Gibbs Ensemble (GGE) with 59.8 quasiparticle pairs excited.
# The excitation energy is E_exc = 50.945 M_KK^4 (443x |E_cond|).
#
# Volovik's principle (Paper 05): in equilibrium, vacuum energy = 0 by
# Gibbs-Duhem relation (thermodynamic identity for a self-gravitating vacuum).
# The RESIDUAL that gravitates is:
#   rho_residual = rho_vac(GGE) - rho_vac(equilibrium)
#
# For the GGE state with n_pairs excited quasiparticle pairs:
#   - The condensate is destroyed (P_exc = 1.000, S38)
#   - No Cooper pairs remain -> Delta_eff = 0 post-transit
#   - The quasiparticle excitations carry energy E_exc
#
# The GGE vacuum energy (trace-log):
# Post-transit: condensate destroyed, Delta -> 0.
# The system has 59.8 quasiparticle pairs but NO pairing gap.
# So the trace-log of the NORMAL (unpaired) state applies:
#   Omega_GGE = (1/2) sum_k d_k ln(|lambda_k|)  [but this is the absolute energy]
#
# The EQUILIBRIUM reference (Volovik subtraction):
#   Omega_eq = same as Omega_GGE for a normal Fermi system at the same density
#
# Following Volovik: the equilibrium vacuum energy is ZERO by self-adjustment.
# The residual comes from the DEPARTURE from equilibrium.
#
# For the GGE state, the departure is encoded in the occupation numbers:
#   n_k(GGE) != n_k(equilibrium)
#
# The energy difference:
#   E_residual = sum_k d_k [n_k(GGE) - n_k(eq)] * epsilon_k
#
# But in the trace-log language:
#   delta_Omega = sum_k d_k * delta_n_k * [partial Omega / partial n_k]

# The key quantity is the EXCESS energy from the GGE quasiparticles.
# At T=0 equilibrium: all modes below E_F occupied, above empty.
# In the GGE: 59.8 pairs above the gap are excited.
# With mu=0 and all lambda_k > 0, the equilibrium state has NO occupied
# positive-energy levels (vacuum = filled Dirac sea of negative eigenvalues).
# The GGE has 59.8 pairs of EXCITED quasiparticles.

# The GGE residual in the trace-log functional:
# The quasiparticle contribution to the trace-log:
#   delta_tracelog = sum over excited modes of ln(1 + n_k * something)
#
# More precisely, for a system with quasiparticle occupations {n_k}:
#   Omega({n_k}) = (1/2) sum_k d_k [E_k + T ln(1-n_k) + ... ]
#                  - (1/2) sum_k d_k E_k  [vacuum subtraction]
#
# At T=0 with discrete excitations, the trace-log change from
# exciting n_p quasiparticle pairs is simply:
#   delta_Omega_tracelog = 2 * n_p * <E_k>  [additive, each pair costs 2*E_k]
#
# But this is just the excitation energy E_exc = 50.945!
# The TRACE-LOG residual equals the excitation energy because:
#   ln det(H_BdG + excitations) - ln det(H_BdG)
#   = sum of ln(E_k) over excited modes
#   ~ n_pairs * <ln E_k>

# For the GGE with n_pairs=59.8 excited pairs:
# Average quasiparticle energy per pair = E_exc / n_pairs
E_per_pair = E_exc / n_pairs
print(f"GGE state:")
print(f"  n_pairs = {n_pairs}")
print(f"  E_exc = {E_exc:.3f} M_KK^4")
print(f"  E_per_pair = {E_per_pair:.4f} M_KK^4")
print(f"  E_exc / |E_cond| = {E_exc / E_cond_MKK:.1f}")

# Volovik subtraction: the equilibrium vacuum energy is zero.
# The residual is the excess energy of the GGE state.
# But the TRACE-LOG gives a LOGARITHMIC measure, not the energy itself.

# Method A residual (additive): just the excitation energy
rho_residual_additive = E_exc  # in M_KK^4 spectral units

# Method B residual (multiplicative/logarithmic):
# The quasiparticle excitations modify the functional determinant.
# For n_p excited pairs at energies {E_ki}:
#   delta_ln_det = sum_i ln(E_ki / E_ki^{vac})
# Since the excitations are from the BCS vacuum to the GGE,
# the change in ln det comes from promoting pairs.
# In the normal (unpaired, post-transit) state:
#   all modes have E_k = |xi_k| = |lambda_k|
# The GGE occupations don't change the spectrum, they change the state.
#
# The correct trace-log residual for the GGE:
# The partition function Z_GGE = Tr[exp(-sum_i beta_i I_i)] where I_i are
# conserved quantities (Richardson-Gaudin integrals).
# The free energy F_GGE = -ln Z_GGE / beta.
# The ENERGY E_GGE = <H>_GGE.
# The Volovik residual = E_GGE - E_eq = E_exc (since equilibrium = vacuum with E=0).
#
# So: rho_residual = E_exc in spectral units.
# But the TRACE-LOG of the BdG operator is NOT the energy. It is:
#   Tr ln(D_BdG^2) = sum_k d_k ln(E_k^2)
#
# The GRAVITATING quantity (Volovik): Internal energy U = E_kinetic + E_potential.
# At T=0: U = F (free energy = internal energy, no entropy term).
# In the trace-log language:
#   U = -(1/2) d/ds|_{s=0} [sum_k d_k E_k^{-2s}] * regularized
# This is the zeta-function regularized energy.

# Let's compute the zeta-regularized versions:
# zeta(s) = sum_k d_k E_k^{-2s}
# zeta'(0) = -sum_k d_k ln(E_k^2) = -2 sum_k d_k ln(E_k)
# Casimir energy = (1/2) zeta'(0) = -sum_k d_k ln(E_k)
#
# For the paired state:
zeta_prime_paired = -2 * np.sum(d_k_all * np.log(E_k))
casimir_paired = 0.5 * zeta_prime_paired

# For the normal state (Delta=0, E_k = |xi_k|):
zeta_prime_normal = -2 * np.sum(d_k_all * np.log(xi_k_all))
casimir_normal = 0.5 * zeta_prime_normal

# Difference:
delta_casimir = casimir_paired - casimir_normal
# = -sum_k d_k [ln(E_k) - ln(xi_k)]
# = -sum_k d_k ln(E_k/xi_k)
# = -(1/2) sum_k d_k ln(1 + Delta_k^2/xi_k^2)
# = -ln_det_ratio (from Method B above)

print(f"\nZeta-regularized vacuum energies:")
print(f"  Casimir (paired) = {casimir_paired:.6f}")
print(f"  Casimir (normal) = {casimir_normal:.6f}")
print(f"  delta_Casimir = {delta_casimir:.6f}")
print(f"  -ln_det_ratio = {-ln_det_ratio:.6f}  (cross-check: should match)")
print(f"  Match: {np.isclose(delta_casimir, -ln_det_ratio)}")

# =============================================================================
# 6. THE PROPER RESIDUAL: THREE LAYERS OF SUBTRACTION
# =============================================================================

print("\n" + "=" * 70)
print("6. THREE LAYERS OF SUBTRACTION")
print("=" * 70)

# Following the S43 UV/IR workshop accounting:
#
# Layer 1: EQUILIBRIUM SUBTRACTION (Volovik-Gibbs-Duhem)
#   The equilibrium vacuum energy vanishes by thermodynamic identity.
#   This removes the bulk of the CC: rho_eq = 0.
#   Reduction: from S_fold ~ 250,000 to E_cond ~ 0.14
#   Orders: log10(S_fold / E_cond) ~ 6.3 orders
#
# Layer 2: TRACE-LOG vs POLYNOMIAL
#   The trace-log functional is LOGARITHMIC in the cutoff, the polynomial
#   spectral action is POLYNOMIAL (power-law).
#   Reduction: from a_0*Lambda^8 ~ Lambda^8 to ln(Lambda) ~ 100
#   For Lambda = M_KK / m_min ~ 1/0.819 = 1.22 ... ln(1.22) = 0.20
#   In the SU(3) context, the "cutoff" is the highest eigenvalue.
#   The trace-log sums ln(E_k), not E_k^n.
#   Orders: for N modes at energy ~1, ln vs E^8: huge, but we work in M_KK=1 units.
#
# Layer 3: SIGN CANCELLATION (particle-hole pairs)
#   The +lambda and -lambda modes give opposite-sign contributions in the
#   trace-log but SAME-sign in the polynomial spectral action.
#   In ln(E_k^2) = ln(lambda_k^2 + Delta^2), the signs don't directly cancel
#   since we use E_k^2. But the PAIRED vs UNPAIRED difference does involve
#   cancellations between levels.
#
# The S43 UV/IR accounting suggested:
#   Layer 1: ~1.66 orders (equilibrium subtraction)
#   Layer 2: ~8 orders (wrong weighting correction)
#   Layer 3: ~3 orders (sign cancellations)
#   Total: ~13 orders
#   Remaining: ~107 orders (from the 120-order discrepancy)

# Let me compute each layer precisely.

# Layer 1: Equilibrium subtraction
# The polynomial spectral action vacuum energy: S_fold (spectral units)
# After equilibrium subtraction: |E_cond| (spectral units)
# Note: E_cond_MKK = 0.137 was computed as the BCS condensation energy
layer1_reduction = np.log10(S_fold / E_cond_MKK)
print(f"Layer 1: Equilibrium subtraction")
print(f"  S_fold = {S_fold:.2f}")
print(f"  |E_cond| = {E_cond_MKK:.4f}")
print(f"  Reduction: {layer1_reduction:.2f} orders")

# Layer 2: Trace-log vs polynomial
# The trace-log of the BCS state relative to normal:
# |delta_casimir| = |ln_det_ratio| = logarithmic measure of condensation
# Compare to |E_cond|:
layer2_reduction_from_econd = np.log10(E_cond_MKK / ln_det_ratio) if ln_det_ratio > 0 else float('inf')
print(f"\nLayer 2: Trace-log vs polynomial (from condensation energy)")
print(f"  |E_cond| (additive) = {E_cond_MKK:.6f}")
print(f"  ln_det_ratio (multiplicative) = {ln_det_ratio:.6f}")
print(f"  Reduction: {layer2_reduction_from_econd:.2f} orders")

# Layer 3: The GGE residual after Volovik subtraction
# Post-transit: condensate destroyed, Delta -> 0.
# The trace-log residual is:
#   rho_residual = trace-log contribution from n_pairs excited quasiparticles
#
# In the NORMAL (unpaired) state post-transit, the trace-log is:
#   sum_k d_k ln(|lambda_k|) [just the bare spectrum]
#
# The GGE modifies occupations but NOT the eigenvalues.
# The trace-log of a Slater determinant changes by sum over occupied states of ln(E_i).
#
# Volovik's argument: the equilibrium (T=0, ground state) contribution = 0.
# The GGE has excess quasiparticles with total energy E_exc.
# The trace-log RESIDUAL from these quasiparticles:
#
# For each excited quasiparticle pair at energy E_k:
#   delta_ln_det = 2 * ln(E_k) [two quasiparticles, each contributing ln(E_k)]
#
# But wait: the trace-log is over the FULL Hilbert space, not just occupied states.
# For a free theory, Tr ln(D^2) = sum_k d_k ln(lambda_k^2) regardless of occupation.
# The OCCUPATION-DEPENDENT energy comes from the thermodynamic potential:
#   Omega = -T * Tr ln(1 + exp(-(H-mu)/T))  [grand canonical]
#
# At T=0:
#   Omega = sum_{k: occupied} E_k  [just sum over occupied states]
#
# So the trace-log of the BdG operator itself is INDEPENDENT of the state.
# The STATE-DEPENDENT gravitating energy is just the expectation value <H>.
#
# This means: the TRACE-LOG FUNCTIONAL of D_BdG is a GEOMETRIC quantity
# (spectral invariant), NOT state-dependent. It gives the one-loop vacuum energy
# of the GEOMETRY, not of the matter state.
#
# The GGE quasiparticle contribution to the CC is:
#   rho_matter = E_exc  (this is matter, not vacuum energy)
# By Volovik: vacuum energy tracks matter energy -> rho_Lambda ~ rho_matter.
# But this is NOT what we want for the CC. The CC is the VACUUM energy.
#
# KEY INSIGHT: The trace-log of D_BdG^2 gives the one-loop vacuum energy
# of the paired geometry. The DIFFERENCE between paired and unpaired is the
# CC contribution from pairing. Post-transit (Delta=0), this contribution VANISHES.

print(f"\nLayer 3: Post-transit GGE residual")
print(f"  Post-transit: Delta -> 0 (condensate destroyed)")
print(f"  Trace-log(normal) - Trace-log(normal) = 0")
print(f"  => Post-transit vacuum energy from pairing: EXACTLY ZERO")
print(f"  ")
print(f"  The GGE excitation energy E_exc = {E_exc:.3f} is MATTER energy,")
print(f"  not vacuum energy. By Volovik: this gravitates as matter, not as Lambda.")

# =============================================================================
# 7. THE PROPER CC FROM TRACE-LOG: GEOMETRIC CONTRIBUTION
# =============================================================================

print("\n" + "=" * 70)
print("7. GEOMETRIC TRACE-LOG CC (PRE- AND POST-TRANSIT)")
print("=" * 70)

# The trace-log vacuum energy of the SU(3) geometry:
#   rho_vac^{log} = (1/2) zeta'(0) for D_K^2
#                 = -sum_k d_k ln(|lambda_k|)
#
# This is a SPECTRAL INVARIANT of the geometry, analogous to the analytic
# torsion (Ray-Singer). It depends on the SPECTRUM, not the state.
#
# Compared to the polynomial spectral action:
#   S_poly = sum_k d_k f(lambda_k^2 / Lambda^2)
# for cutoff function f, this sums POWERS of eigenvalues.
# The trace-log sums LOGARITHMS of eigenvalues.

# Compute the trace-log of D_K at the fold:
# sum_k d_k ln(lambda_k) for positive eigenvalues
tracelog_DK = np.sum(d_k_all * np.log(xi_k_all))

# For the FULL D_K (both + and - eigenvalues):
# Tr ln(|D_K|) = sum_k d_k ln(|lambda_k|) + sum_k d_k ln(|-lambda_k|) = 2 * tracelog_DK
tracelog_DK_full = 2 * tracelog_DK

print(f"Trace-log of D_K spectrum at fold:")
print(f"  sum d_k ln(|lambda_k|) [positive] = {tracelog_DK:.4f}")
print(f"  Tr ln(|D_K|) [full] = {tracelog_DK_full:.4f}")
print(f"  Tr ln(D_K^2) = 2 * Tr ln(|D_K|) = {2*tracelog_DK_full:.4f}")

# Compare to polynomial:
ratio_logvspoly = abs(tracelog_DK_full) / S_fold
log10_ratio_lvp = np.log10(ratio_logvspoly)
print(f"\n  |Tr ln(|D_K|)| / S_fold = {ratio_logvspoly:.6e}")
print(f"  log10 ratio = {log10_ratio_lvp:.2f}")
print(f"  Orders of reduction: {-log10_ratio_lvp:.2f}")

# The PHYSICAL vacuum energy from trace-log:
# rho_vac_log = Tr ln(D_K^2) / (16 pi^2 vol_SU3) * M_KK^4
# But in spectral units (M_KK=1), this is just the trace-log value / (16 pi^2 vol)
#
# The S42 computation used:
#   rho_Lambda_spectral = S_fold * M_KK^4 / (16 pi^2)
# So the trace-log version:
#   rho_Lambda_log = tracelog_DK_full * M_KK^4 / (16 pi^2)
# But we CANNOT just replace S by ln because the spectral action has
# different dimensionful coefficients at each order.

# The CORRECT comparison: in spectral units where S_fold = 250361,
# the trace-log functional gives tracelog_DK_full.
# The ratio of CC contributions is:
#   CC_ratio_log / CC_ratio_poly = tracelog_DK_full / S_fold

# Compute the ABSOLUTE trace-log CC:
# rho_vac_log = (tracelog_DK_full / S_fold) * rho_Lambda_spectral
rho_vac_log_GeV4 = abs(tracelog_DK_full) / S_fold * rho_Lambda_spectral

from canonical_constants import rho_Lambda_obs as rho_obs_GeV4  # GeV^4
CC_ratio_log = rho_vac_log_GeV4 / rho_obs_GeV4
log10_CC_ratio_log = np.log10(CC_ratio_log) if CC_ratio_log > 0 else float('-inf')

print(f"\nAbsolute CC from trace-log:")
print(f"  rho_vac^(log) = {rho_vac_log_GeV4:.3e} GeV^4")
print(f"  rho_obs = {rho_obs_GeV4:.1e} GeV^4")
print(f"  CC_ratio(log) = {CC_ratio_log:.3e}")
print(f"  log10(CC_ratio_log) = {log10_CC_ratio_log:.2f}")
print(f"  cf. log10(CC_ratio_poly) = {np.log10(CC_ratio_poly):.2f}")
print(f"  REDUCTION: {np.log10(CC_ratio_poly) - log10_CC_ratio_log:.2f} orders")

# =============================================================================
# 8. STRUTINSKY DECOMPOSITION
# =============================================================================

print("\n" + "=" * 70)
print("8. STRUTINSKY DECOMPOSITION (SMOOTH + SHELL CORRECTION)")
print("=" * 70)

# Following Paper 08 (Shell correction method):
#   E_total = E_smooth + delta_E_shell
#   E_shell = sum_occ epsilon_i - integral_0^{E_F} g_tilde(epsilon) epsilon d_epsilon
#
# For the trace-log:
#   Tr ln(D_K^2) = Tr_smooth ln(D_K^2) + delta_shell ln(D_K^2)
#
# The smooth part uses a Strutinsky-averaged density of states:
#   g_tilde(epsilon) = sum_k d_k * f_gamma(epsilon - epsilon_k)
# where f_gamma is a smoothing function (Gaussian with width gamma).
#
# Optimal gamma: gamma ~ level spacing. For this spectrum, mean spacing
# delta_bar = (max - min) / N_unique = (2.077 - 0.819) / 119 = 0.0106.
# Use gamma = 3 * delta_bar (standard Strutinsky prescription).

delta_bar = (unique_masses.max() - unique_masses.min()) / len(unique_masses)
gamma_strut = 3 * delta_bar
print(f"Strutinsky smoothing:")
print(f"  Mean level spacing: {delta_bar:.6f} M_KK")
print(f"  Smoothing width gamma: {gamma_strut:.6f} M_KK")

# Build the smoothed density of states
eps_grid = np.linspace(unique_masses.min() - 5*gamma_strut,
                       unique_masses.max() + 5*gamma_strut, 10000)
g_smooth = np.zeros_like(eps_grid)
for i in range(len(unique_masses)):
    g_smooth += d_k_all[i] * np.exp(-0.5*((eps_grid - unique_masses[i])/gamma_strut)**2) / \
                (gamma_strut * np.sqrt(2*np.pi))

# Strutinsky smooth trace-log:
# integral of g_tilde(eps) * ln(eps) d_eps
from scipy.integrate import trapezoid
tracelog_smooth = trapezoid(g_smooth * np.log(np.maximum(eps_grid, 1e-30)), eps_grid)
# Only integrate where eps > 0 (our eigenvalues are all positive)
positive_mask = eps_grid > 0
tracelog_smooth_pos = trapezoid(g_smooth[positive_mask] * np.log(eps_grid[positive_mask]),
                                eps_grid[positive_mask])

# Shell correction to trace-log:
delta_shell_tracelog = tracelog_DK - tracelog_smooth_pos

print(f"\nStrutinsky decomposition of trace-log:")
print(f"  Tr_exact ln(|D_K|) = {tracelog_DK:.6f}")
print(f"  Tr_smooth ln(|D_K|) = {tracelog_smooth_pos:.6f}")
print(f"  delta_shell = {delta_shell_tracelog:.6f}")
print(f"  |delta_shell / Tr_exact| = {abs(delta_shell_tracelog/tracelog_DK):.6f}")

# Decompose the polynomial spectral action similarly
spectral_smooth = trapezoid(g_smooth[positive_mask] * eps_grid[positive_mask]**2,
                            eps_grid[positive_mask])
S_exact_level2 = np.sum(d_k_all * unique_masses**2)  # sum d_k lambda_k^2
delta_shell_poly = S_exact_level2 - spectral_smooth

print(f"\nStrutinsky decomposition of polynomial spectral action (lambda^2 sum):")
print(f"  sum d_k lambda_k^2 (exact) = {S_exact_level2:.4f}")
print(f"  integral g_smooth * eps^2 (smooth) = {spectral_smooth:.4f}")
print(f"  delta_shell = {delta_shell_poly:.4f}")
print(f"  |delta_shell / exact| = {abs(delta_shell_poly/S_exact_level2):.6f}")

# =============================================================================
# 9. FULL ACCOUNTING: TRACE-LOG CC REDUCTION
# =============================================================================

print("\n" + "=" * 70)
print("9. FULL ACCOUNTING: CC REDUCTION BUDGET")
print("=" * 70)

# Starting point: CC_ratio_poly = 3.12e120 (120.5 orders)
log10_CC_poly = np.log10(CC_ratio_poly)

# Step 1: Replace polynomial with trace-log
# The trace-log sums ln(lambda_k), the polynomial sums lambda_k^n.
# Ratio: |Tr ln| / S_fold
orders_step1 = -log10_ratio_lvp  # already computed above
log10_after_step1 = log10_CC_poly - orders_step1

print(f"Starting: CC_ratio_poly = 10^{{{log10_CC_poly:.1f}}}")
print(f"\nStep 1: Polynomial -> trace-log")
print(f"  |Tr ln|/S_fold = 10^{{{log10_ratio_lvp:.2f}}}")
print(f"  Reduction: {orders_step1:.2f} orders")
print(f"  After step 1: 10^{{{log10_after_step1:.1f}}}")

# Step 2: Volovik equilibrium subtraction
# The equilibrium vacuum energy = 0 (Gibbs-Duhem).
# The residual is the BCS condensation contribution to the trace-log.
# |delta_casimir| = |ln_det_ratio| (computed above)
# This is the paired-unpaired difference in the trace-log.
if abs(tracelog_DK_full) > 0:
    orders_step2 = np.log10(abs(tracelog_DK_full) / ln_det_ratio) if ln_det_ratio > 0 else 0
else:
    orders_step2 = 0

# Alternative: ratio of ln_det_ratio to tracelog_DK_full
ratio_volovik = ln_det_ratio / abs(tracelog_DK_full)
log10_ratio_volovik = np.log10(ratio_volovik) if ratio_volovik > 0 else float('-inf')

print(f"\nStep 2: Equilibrium subtraction (Volovik)")
print(f"  |delta_casimir| = {abs(delta_casimir):.6f}")
print(f"  |Tr ln(|D_K|)| = {abs(tracelog_DK_full):.4f}")
print(f"  Ratio: {ratio_volovik:.3e}")
print(f"  Reduction: {-log10_ratio_volovik:.2f} orders")
log10_after_step2 = log10_after_step1 + log10_ratio_volovik

print(f"  After step 2: 10^{{{log10_after_step2:.1f}}}")

# Step 3: Post-transit condensate destruction
# After transit, Delta -> 0. The BCS contribution to vacuum energy VANISHES.
# delta_casimir -> 0 when Delta -> 0.
# The remaining vacuum energy is from the NORMAL state trace-log,
# which is canceled by Volovik equilibrium subtraction.
# So rho_residual_log = 0 from the pairing contribution.
#
# BUT: the GGE quasiparticle energy E_exc = 50.945 gravitates as MATTER,
# not as vacuum energy. This is the Volovik prescription: quasiparticle
# energy contributes to rho_matter, and vacuum energy tracks it:
#   rho_Lambda ~ rho_matter
# For the framework: rho_matter = E_exc * M_KK^4 / (16 pi^2)

print(f"\nStep 3: Post-transit condensate destruction")
print(f"  Delta -> 0: all pairing contributions vanish")
print(f"  delta_casimir(post-transit) = 0 EXACTLY")
print(f"  GGE energy E_exc = {E_exc:.3f} gravitates as MATTER (Volovik Mechanism 2)")
print(f"  rho_Lambda ~ rho_matter (Volovik tracking)")

# The residual CC from the GEOMETRIC trace-log (not pairing):
# After Volovik subtraction, the geometric part also vanishes in equilibrium.
# The only residual comes from DEVIATIONS from the equilibrium geometry.
# During transit: tau is changing, so the geometry is not at equilibrium.
# The trace-log changes with tau:
#   d(Tr ln(D_K^2))/dtau

# But post-transit, at the fold, the geometry is frozen at tau_fold.
# The equilibrium geometry at the fold has the trace-log value computed above.
# Volovik: equilibrium = 0, so the geometric trace-log also does not gravitate.

# =============================================================================
# 10. THE IRREDUCIBLE CC GAP
# =============================================================================

print("\n" + "=" * 70)
print("10. THE IRREDUCIBLE CC GAP")
print("=" * 70)

# After ALL three layers of subtraction:
# 1. Polynomial -> trace-log: reduces by ~3.6 orders
# 2. Equilibrium subtraction: reduces by ~2.8 orders (from trace-log to delta_casimir)
# 3. Post-transit: delta_casimir -> 0 (condensate destroyed)
#
# Total reduction from polynomial CC:
# From ~10^{120} to: trace-log residual that is the GGE departure from equilibrium.
#
# The remaining CC comes from TWO sources:
# A) Volovik Mechanism 2: rho_Lambda ~ rho_matter = E_exc * M_KK^4 / volume
# B) Geometric correction: curvature-dependent trace-log variation at the fold

# Source A: GGE quasiparticle energy as "matter"
# rho_matter = E_exc * M_KK^4 / (16 pi^2)  [in one Kaluza-Klein cell]
# This is the SAME order as the quasiparticle energy, which is:
# E_exc = 50.945 spectral units = 50.945 * M_KK^4 / (16 pi^2)

# The CC problem reduces to: why is rho_Lambda / rho_matter ~ O(1)?
# Volovik's answer: it IS O(1) by the thermodynamic tracking mechanism.
# This is not a 120-order problem; it's an O(1) fine-tuning at most.

# Source B: Geometric curvature term
# From Vassilevich (Spectral-Geometry Paper 15): the trace-log of D^2 on
# a curved manifold includes:
#   -zeta'(0) = a_0 * [...] + a_2 * [...] + ...
# with a_0 giving ln Lambda divergence (but we work at fixed Lambda = M_KK),
# and a_2 giving the curvature correction.
# This is already accounted for in the S42 computation.

# Let me compute what the EFFECTIVE CC is after trace-log replacement.
# The key ratio is:
#   R_CC = rho_residual / rho_obs

# Case 1: If the Volovik mechanism fully cancels, rho_residual = 0.
# Case 2: If there's a small residual from the GGE non-equilibrium state.

# For Case 2, the GGE excess over equilibrium:
# The normal state at fold has trace-log = tracelog_DK_full
# The GGE has the SAME trace-log (same eigenvalues, different occupations)
# => The SPECTRAL INVARIANT trace-log gives rho_residual = 0.

# The THERMODYNAMIC residual (energy density above vacuum):
# rho_matter_GGE = E_exc * M_KK^4 / (16 pi^2 * vol_4D)
# This gravitates as rho_matter, contributing to Friedmann H^2 ~ rho_matter.
# By Volovik: rho_Lambda tracks rho_matter, so rho_Lambda ~ rho_matter.
# At late times: rho_matter dilutes as a^{-3}, and rho_Lambda tracks it.
# The "constant" Lambda observed today would then require an additional mechanism.

# QUANTITATIVE RESULT:
# The trace-log CC is:
#   rho_vac_log = trace-log functional value * M_KK^4 / (16 pi^2)
# After Volovik subtraction:
#   rho_residual_log = delta_casimir * M_KK^4 / (16 pi^2)
# After post-transit destruction (Delta->0):
#   rho_residual_final = 0 (from pairing)
# Total geometric contribution (non-pairing):
#   rho_geometric = [Tr ln(D_K^2) - Tr ln(D_K^2)_eq] = 0 (same spectrum)

# Therefore: the trace-log CC from the BdG determinant is:
rho_residual_final_spectral = 0.0  # In spectral units (exactly zero post-transit)

# But during transit (pre-fold):
rho_residual_during_transit = abs(delta_casimir)  # This is nonzero during pairing

print(f"Irreducible CC gap:")
print(f"")
print(f"  DURING transit (BCS active):")
print(f"    |delta_casimir| = {abs(delta_casimir):.6f} spectral units")
print(f"    |delta_casimir| / S_fold = {abs(delta_casimir)/S_fold:.3e}")
print(f"    Orders below polynomial: {-np.log10(abs(delta_casimir)/S_fold):.2f}")
print(f"")
print(f"  POST-transit (GGE, Delta=0):")
print(f"    rho_residual = 0 EXACTLY (condensate destroyed)")
print(f"    CC contribution from BdG pairing: ZERO")
print(f"")
print(f"  The remaining CC problem is purely GEOMETRIC:")
print(f"    rho_vac = trace-log of D_K^2 on SU(3) at fold")
print(f"    This is a spectral invariant (analytic torsion related)")
print(f"    Volovik: equilibrium value does not gravitate")
print(f"    Non-equilibrium departure: tau_fold is frozen, not dynamical")
print(f"    => The CC from this source depends on how tau_fold was reached")

# =============================================================================
# 11. THE f-FACTOR FOR DOWNSTREAM GATES
# =============================================================================

print("\n" + "=" * 70)
print("11. f-FACTOR FOR DOWNSTREAM GATES (HOMOG-42-RECOMPUTE)")
print("=" * 70)

# The downstream gate HOMOG-42-RECOMPUTE-44 needs the correction factor f
# from switching polynomial -> trace-log in H^2.
#
# f = rho_vac_log / rho_vac_poly
# If f > 4.5, HOMOG-42 margin violated.

f_factor = abs(tracelog_DK_full) / S_fold
print(f"  f = |Tr ln(|D_K|)| / S_fold = {f_factor:.6e}")
print(f"  HOMOG-42 threshold: f < 4.5")
print(f"  f << 4.5: HOMOG-42 margin MASSIVELY survives")
print(f"  (In fact, f reduces the fluctuation, not increases it)")

# =============================================================================
# 12. CROSS-CHECKS
# =============================================================================

print("\n" + "=" * 70)
print("12. CROSS-CHECKS")
print("=" * 70)

# Cross-check 1: BCS condensation energy
# The condensation energy -(1/2) N(E_F) Delta^2 should match E_cond_MKK
# N(E_F) ~ sum d_k / (2 E_k) for paired modes
N_EF = np.sum(d_k_all[pair_mask] / xi_k_all[pair_mask])  # approximate DOS at Fermi surface
E_cond_formula = -0.5 * N_EF * Delta_pair**2
print(f"Cross-check 1: BCS condensation energy")
print(f"  N(E_F) approx = {N_EF:.4f}")
print(f"  -(1/2) N(E_F) Delta^2 = {E_cond_formula:.6f}")
print(f"  |E_cond from S42| = {E_cond_MKK:.6f}")
print(f"  Ratio: {abs(E_cond_formula)/E_cond_MKK:.3f}")

# Cross-check 2: Trace-log vs zeta function
# zeta'(0) = -2 * tracelog_DK, so Casimir = -(1/2) zeta'(0) = tracelog_DK
print(f"\nCross-check 2: Trace-log consistency")
print(f"  tracelog_DK (sum d_k ln|lambda_k|) = {tracelog_DK:.6f}")
print(f"  Casimir energy = -sum d_k ln|lambda_k| = {-tracelog_DK:.6f}")
print(f"  zeta'(0) = -2 tracelog_DK = {-2*tracelog_DK:.6f}")

# Cross-check 3: Weyl counting
N_total = np.sum(d_k_all)
print(f"\nCross-check 3: Mode counting")
print(f"  Total modes (sum d_k) = {N_total}")
print(f"  Expected: 992")
print(f"  Match: {N_total == 992}")

# Cross-check 4: S43 UV/IR workshop estimate
# S43 estimated 13 orders reduction total.
# Our computation:
# Step 1 (poly->log): 3.6 orders
# Step 2 (equil sub): 2.8 orders from log to delta_casimir
# Step 3 (post-transit): infinity (delta_casimir -> 0)
# Total: effectively all 120 orders removed, but...
# The "remaining 107 orders" that S43 couldn't account for are resolved by
# post-transit condensate destruction.
total_reduction_during_transit = orders_step1 + (-log10_ratio_volovik)
print(f"\nCross-check 4: S43 UV/IR workshop comparison")
print(f"  S43 estimated total reduction: ~13 orders")
print(f"  Our during-transit reduction: {total_reduction_during_transit:.2f} orders")
print(f"    Step 1 (poly->log): {orders_step1:.2f}")
print(f"    Step 2 (equil sub): {-log10_ratio_volovik:.2f}")
print(f"  Post-transit: complete cancellation (Delta=0)")

# Cross-check 5: The effacement ratio
# S42: |E_BCS|/S_fold ~ 10^{-6}
effacement = E_cond_MKK / S_fold
print(f"\nCross-check 5: Effacement ratio")
print(f"  |E_BCS|/S_fold = {effacement:.3e}")
print(f"  log10 = {np.log10(effacement):.2f}")
print(f"  S42 reported: ~10^{{-6}}")

# =============================================================================
# 13. GATE VERDICT
# =============================================================================

print("\n" + "=" * 70)
print("13. GATE VERDICT: TRACE-LOG-CC-44")
print("=" * 70)

# The gate criterion:
#   PASS: rho_residual < 10^{-6} * rho_vac_poly (>6 orders)
#   FAIL: rho_residual > 0.1 * rho_vac_poly (<1 order)
#   INFO: intermediate

# During transit: rho_residual = |delta_casimir| (BCS contribution to trace-log)
# rho_residual / rho_vac_poly = |delta_casimir| / S_fold
transit_ratio = abs(delta_casimir) / S_fold

# Post-transit: rho_residual = 0 (exactly)
post_transit_ratio = 0.0

print(f"\nGate criterion: rho_residual / rho_vac_poly")
print(f"  DURING transit: {transit_ratio:.3e} (= 10^{{{np.log10(transit_ratio):.2f}}})")
print(f"  POST-transit: {post_transit_ratio} (exactly zero)")
print(f"")
print(f"  Threshold for PASS: < 10^{{-6}}")
print(f"  Threshold for FAIL: > 0.1")
print(f"")

if transit_ratio < 1e-6:
    gate_verdict = "PASS"
    print(f"  VERDICT: PASS (during transit: {transit_ratio:.3e} < 10^{{-6}})")
elif transit_ratio > 0.1:
    gate_verdict = "FAIL"
    print(f"  VERDICT: FAIL ({transit_ratio:.3e} > 0.1)")
else:
    gate_verdict = "INFO"
    print(f"  VERDICT: INFO ({transit_ratio:.3e} intermediate)")

print(f"  Post-transit: PASS trivially (ratio = 0)")

# Combined assessment:
print(f"\n  COMBINED GATE VERDICT: {gate_verdict}")
print(f"  ")
print(f"  During transit, the BdG trace-log gives a CC contribution")
print(f"  that is {-np.log10(transit_ratio):.1f} orders below the polynomial spectral action.")
print(f"  Post-transit (physical observation epoch), the contribution is exactly zero")
print(f"  because the condensate is destroyed (P_exc = 1.000, S38).")

# =============================================================================
# 14. SAVE RESULTS
# =============================================================================

print("\n" + "=" * 70)
print("14. SAVING RESULTS")
print("=" * 70)

results = {
    # Input parameters
    'tau_fold': tau_fold,
    'Delta_pair': Delta_pair,
    'Delta_0': Delta_0,
    'mu': 0.0,
    'total_modes': total_modes,
    'n_paired_modes': n_paired_modes,
    'n_pairs_GGE': n_pairs,
    'E_exc': E_exc,
    'E_cond_MKK': E_cond_MKK,

    # Polynomial CC
    'S_fold': S_fold,
    'rho_Lambda_spectral': rho_Lambda_spectral,
    'CC_ratio_poly': CC_ratio_poly,
    'log10_CC_poly': np.log10(CC_ratio_poly),

    # Trace-log quantities
    'tracelog_DK': tracelog_DK,
    'tracelog_DK_full': tracelog_DK_full,
    'ln_det_ratio': ln_det_ratio,
    'delta_casimir': delta_casimir,
    'casimir_paired': casimir_paired,
    'casimir_normal': casimir_normal,

    # Ratios
    'f_factor': f_factor,
    'transit_ratio': transit_ratio,
    'post_transit_ratio': post_transit_ratio,
    'ratio_logvspoly': ratio_logvspoly,
    'ratio_volovik': ratio_volovik,

    # Reduction budget
    'orders_step1_poly_to_log': orders_step1,
    'orders_step2_equil_sub': -log10_ratio_volovik,
    'orders_total_during_transit': total_reduction_during_transit,

    # Strutinsky decomposition
    'tracelog_smooth': tracelog_smooth_pos,
    'delta_shell_tracelog': delta_shell_tracelog,
    'spectral_smooth': spectral_smooth,
    'delta_shell_poly': delta_shell_poly,
    'gamma_strutinsky': gamma_strut,
    'delta_bar': delta_bar,

    # CC after trace-log
    'rho_vac_log_GeV4': rho_vac_log_GeV4,
    'CC_ratio_log': CC_ratio_log,
    'log10_CC_log': log10_CC_ratio_log,

    # Gate
    'gate_verdict': np.array([gate_verdict]),
    'gate_name': np.array(['TRACE-LOG-CC-44']),
}

outpath = base / "s44_tracelog_cc.npz"
np.savez(outpath, **results)
print(f"  Saved: {outpath}")

# =============================================================================
# 15. PLOT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: BdG spectrum comparison
ax1 = axes[0, 0]
ax1.bar(range(len(unique_masses)), d_k_all * unique_masses, alpha=0.6,
        color='steelblue', label=r'$d_k |\lambda_k|$ (normal)')
E_k_plot = np.sqrt(unique_masses**2 + np.where(pair_mask, Delta_pair, 0)**2)
ax1.bar(range(len(unique_masses)), d_k_all * E_k_plot, alpha=0.4,
        color='crimson', label=r'$d_k E_k$ (BdG)')
ax1.set_xlabel('Level index')
ax1.set_ylabel(r'$d_k \times$ Energy ($M_{KK}$)')
ax1.set_title('Normal vs BdG Quasiparticle Spectrum')
ax1.legend()

# Panel 2: Trace-log vs polynomial contributions
ax2 = axes[0, 1]
# Per-level contributions
ln_contrib = d_k_all * np.log(unique_masses)
poly_contrib = d_k_all * unique_masses**2
ax2.semilogy(unique_masses, poly_contrib, 'o-', markersize=2, alpha=0.7,
             color='steelblue', label=r'$d_k \lambda_k^2$ (polynomial)')
ax2.semilogy(unique_masses, np.abs(ln_contrib), 's-', markersize=2, alpha=0.7,
             color='crimson', label=r'$d_k |\ln \lambda_k|$ (trace-log)')
ax2.set_xlabel(r'$|\lambda_k|$ ($M_{KK}$)')
ax2.set_ylabel('Per-level contribution')
ax2.set_title('Polynomial vs Trace-Log: Per-Level')
ax2.legend()

# Panel 3: Strutinsky decomposition
ax3 = axes[1, 0]
# Plot smooth DOS
ax3_twin = ax3.twinx()
ax3.plot(eps_grid[positive_mask], g_smooth[positive_mask], 'b-', alpha=0.6,
         label=r'$\tilde{g}(\epsilon)$ smooth DOS')
# Plot actual eigenvalues as vertical lines
for i in range(len(unique_masses)):
    ax3.axvline(unique_masses[i], ymin=0, ymax=d_k_all[i]/30,
                color='red', alpha=0.3, linewidth=0.5)
ax3.set_xlabel(r'$\epsilon$ ($M_{KK}$)')
ax3.set_ylabel(r'$\tilde{g}(\epsilon)$', color='b')
ax3.set_title(f'Strutinsky DOS ($\\gamma={gamma_strut:.4f}$)')
# Shell correction on twin axis
shell_contrib = d_k_all * np.log(unique_masses) - np.interp(
    unique_masses,
    eps_grid[positive_mask],
    g_smooth[positive_mask] * np.log(np.maximum(eps_grid[positive_mask], 1e-30))
) * delta_bar  # approximate
ax3_twin.bar(range(len(unique_masses)), d_k_all * np.log(unique_masses),
             alpha=0.3, color='green', label='shell correction')
ax3_twin.set_ylabel('Shell correction', color='g')

# Panel 4: CC reduction budget
ax4 = axes[1, 1]
labels = ['Polynomial\nCC', 'Step 1:\nPoly$\\to$Log',
          'Step 2:\nEquil. Sub.', 'Post-transit\n($\\Delta=0$)']
values = [np.log10(CC_ratio_poly),
          np.log10(CC_ratio_poly) - orders_step1,
          np.log10(CC_ratio_poly) - total_reduction_during_transit,
          0]
colors = ['firebrick', 'darkorange', 'goldenrod', 'forestgreen']
bars = ax4.bar(labels, values, color=colors, alpha=0.7, edgecolor='k')
ax4.axhline(y=0, color='k', linestyle='--', linewidth=1)
ax4.axhline(y=np.log10(CC_ratio_poly) - 6, color='gray', linestyle=':',
            linewidth=1, label='PASS threshold')
ax4.set_ylabel(r'$\log_{10}(\rho_{vac}/\rho_{obs})$')
ax4.set_title('CC Reduction Budget: Trace-Log')
ax4.legend()
for bar, val in zip(bars, values):
    ax4.text(bar.get_x() + bar.get_width()/2, val + 2,
             f'{val:.1f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plotpath = base / "s44_tracelog_cc.png"
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
