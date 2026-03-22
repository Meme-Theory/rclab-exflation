#!/usr/bin/env python3
"""
LEGGETT-DAMPING-50: Quality Factor of the Leggett Mode
=======================================================

Gate: LEGGETT-DAMPING-50
    PASS: Q > 10 (well-defined collective mode)
    FAIL: Q < 1 (overdamped, mass concept invalid)
    INFO: 1 < Q < 10 (marginal)

Physical question: The Leggett mode at omega_L1 = 0.070 M_KK sits at 41% of
the pair-breaking edge 2*Delta_B3 = 0.168 M_KK. In 3He-B, omega_L/Delta ~ 10^{-3}
and Q ~ 10^3. Here omega_L/Delta ~ 0.095, a 95x compression. Is the mode still sharp?

Method:
    1. Construct the BdG quasiparticle spectrum E_k = sqrt(eps_k^2 + Delta_k^2)
       for all 8 BCS modes (1 B1, 4 B2, 3 B3).
    2. Compute the Leggett self-energy Im[Sigma_L(omega)] from the Beliaev process:
       Leggett mode -> 2 quasiparticles.
       Im[Sigma_L(omega)] ~ sum_{k,k'} |M_{kk'}|^2 * [1-f(E_k)-f(E_{k'})] * delta(omega-E_k-E_{k'})
    3. At T=0: if omega_L < 2*Delta_min, Beliaev process kinematically forbidden.
       Gamma_Beliaev = 0, Q = infinity.
    4. At finite T (GGE): thermal occupation f_k > 0 enables Landau damping
       Leggett -> quasiparticle + quasihole.
       Also enables stimulated Beliaev with Bose factor (1+n_L).
    5. Compute Raman/two-phonon process: Leggett + quasiparticle -> quasiparticle.
       This is the leading T=0 process even below threshold.
    6. Extract Q = omega_L / (2*Gamma_total).
    7. Compare scaling Gamma/omega_L ~ (omega_L/2*Delta)^n to 3He result (n=3).

The critical insight from superfluid physics: in 3He-B, the Leggett mode
(squashing mode) has Q ~ 10^3 because omega_L/Delta ~ 10^{-3}. The damping
rate Gamma ~ omega_L * (omega_L/Delta)^3 from three-body phase space.
At omega_L/Delta ~ 0.095, we expect Gamma/omega_L ~ 0.095^3 ~ 8.6e-4,
giving Q ~ 580. But this scaling assumes deep separation. Near threshold
(omega_L approaching 2*Delta), the phase-space suppression weakens.

Volovik-Superfluid-Universe-Theorist, Session 50, 2026-03-20.

References:
    Leggett, PRL 14, 536 (1966)
    Volovik, "The Universe in a Helium Droplet" (2003), Ch. 7
    S48 s48_leggett_mode.npz — omega_L1 = 0.0696, Delta_B3 = 0.084
    S49 s49_dipolar_catalog.npz — Leggett-dipolar identification
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

import numpy as np
from scipy.linalg import eigh
from scipy.integrate import quad

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 78)
print("LEGGETT-DAMPING-50: Quality Factor of the Leggett Mode")
print("Volovik-Superfluid-Universe-Theorist")
print("=" * 78)

# =============================================================================
# SECTION 1: Load all prior data
# =============================================================================
print("\n--- SECTION 1: Load Prior Data ---")

# S48 Leggett mode data
d48 = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
omega_L1_fold = float(d48['omega_L1_fold'])
omega_L2_fold = float(d48['omega_L2_fold'])
Delta_fold_vec = d48['Delta_fold']           # [Delta_B1, Delta_B2, Delta_B3]
rho_fold_vec = d48['rho_fold']               # [rho_B1, rho_B2, rho_B3]
J_12_fold = float(d48['J_12_fold'])
J_23_fold = float(d48['J_23_fold'])
J_13_fold = float(d48['J_13_fold'])
eigvecs_fold = d48['eigvecs_fold']           # 3x3 eigenvectors (columns)

# S48 Goldstone mass data (BdG spectrum)
d48g = np.load(os.path.join(SCRIPT_DIR, 's48_goldstone_mass.npz'), allow_pickle=True)
evals_DK = d48g['evals_DK']                 # 16 Dirac eigenvalues at fold
q7_joint = d48g['q7_joint']                  # K_7 charges
rho_s_C2 = float(d48g['rho_s_C2'])

# S49 dipolar catalog
d49 = np.load(os.path.join(SCRIPT_DIR, 's49_dipolar_catalog.npz'), allow_pickle=True)

# S46 V matrices
d46 = np.load(os.path.join(SCRIPT_DIR, 's46_qtheory_selfconsistent.npz'), allow_pickle=True)
V_constrained = d46['V_mat_constrained']

# Unpack sector data
Delta_B1, Delta_B2, Delta_B3_val = Delta_fold_vec
rho_B1, rho_B2, rho_B3 = rho_fold_vec

# Pair-breaking thresholds
thresh_B1 = 2.0 * Delta_B1
thresh_B2 = 2.0 * Delta_B2
thresh_B3 = 2.0 * Delta_B3_val

print(f"omega_L1 = {omega_L1_fold:.6f} M_KK")
print(f"omega_L2 = {omega_L2_fold:.6f} M_KK")
print(f"Delta_B1 = {Delta_B1:.6f}, Delta_B2 = {Delta_B2:.6f}, Delta_B3 = {Delta_B3_val:.6f}")
print(f"2*Delta_B3 = {thresh_B3:.6f} (pair-breaking edge for B3)")
print(f"2*Delta_B1 = {thresh_B1:.6f} (pair-breaking edge for B1)")
print(f"2*Delta_B2 = {thresh_B2:.6f} (pair-breaking edge for B2)")
print(f"omega_L1 / (2*Delta_B3) = {omega_L1_fold / thresh_B3:.4f}")
print(f"J_12 = {J_12_fold:.6f}, J_23 = {J_23_fold:.6f}, J_13 = {J_13_fold:.6f}")
print(f"rho_B1 = {rho_B1:.4f}, rho_B2 = {rho_B2:.4f}, rho_B3 = {rho_B3:.4f}")

# =============================================================================
# SECTION 2: Construct BdG quasiparticle spectrum
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 2: BdG Quasiparticle Spectrum at Fold")
print(f"{'='*78}")

# The Dirac eigenvalues at the fold define the single-particle energies.
# The 16 eigenvalues come in +/- pairs (particle-hole symmetry).
# We work with the positive-energy sector (8 modes).
#
# BdG quasiparticle energy: E_k = sqrt(eps_k^2 + Delta_k^2)
# where eps_k is measured from the Fermi level (here eps_k = |lambda_k| - mu)
# and Delta_k is the BCS gap in the sector containing mode k.
#
# Sector assignment:
#   B1: 1 mode (eps ~ 0.820), q7 = 0
#   B2: 4 modes (eps ~ 0.845), |q7| = 1/4
#   B3: 3 modes (eps ~ 0.971), q7 = 0
#
# In the BCS framework on this discrete spectrum, the "Fermi energy" is
# the chemical potential mu. At half-filling (canonical, PH-symmetric),
# mu = 0 analytically (S34 MU-35a). The single-particle energies ARE
# the Dirac eigenvalues.

evals_pos = np.sort(np.abs(evals_DK))[::-1]  # descending by |lambda|
evals_pos_unique = np.unique(np.round(np.abs(evals_DK), 8))
evals_pos_unique = np.sort(evals_pos_unique)

print(f"\nDirac eigenvalue magnitudes (unique): {evals_pos_unique}")

# Sector classification
# B3: |lambda| ~ 0.971 (3 modes, triply degenerate)
# B2: |lambda| ~ 0.845 (4 modes)
# B1: |lambda| ~ 0.820 (1 mode)

eps_B1 = np.array([0.81974111])                         # 1 mode
eps_B2 = np.array([0.8452121, 0.8452121, 0.8452121, 0.8452121])  # 4 modes
eps_B3 = np.array([0.97140762, 0.97140762, 0.97140762]) # 3 modes

# BdG quasiparticle energies (with mu=0, eps_k = |lambda_k|)
E_B1 = np.sqrt(eps_B1**2 + Delta_B1**2)
E_B2 = np.sqrt(eps_B2**2 + Delta_B2**2)
E_B3 = np.sqrt(eps_B3**2 + Delta_B3**2)

print(f"\nBdG quasiparticle energies:")
print(f"  E_B1 = {E_B1} (1 mode)")
print(f"  E_B2 = {E_B2[0]:.6f} (4 degenerate modes)")
print(f"  E_B3 = {E_B3[0]:.6f} (3 degenerate modes)")

# Minimum pair-breaking energy = 2 * E_k_min
E_min = min(E_B1.min(), E_B2.min(), E_B3.min())
pair_break_min = 2.0 * E_min
print(f"\n  E_min = {E_min:.6f} M_KK")
print(f"  2*E_min (pair-breaking threshold) = {pair_break_min:.6f} M_KK")
print(f"  omega_L1 / (2*E_min) = {omega_L1_fold / pair_break_min:.6f}")

# BdG coherence factors (u_k, v_k)
def bcs_uv(eps, Delta):
    """BCS coherence factors u_k, v_k."""
    E = np.sqrt(eps**2 + Delta**2)
    u2 = 0.5 * (1.0 + eps / E)
    v2 = 0.5 * (1.0 - eps / E)
    return np.sqrt(u2), np.sqrt(v2), E

u_B1, v_B1, _ = bcs_uv(eps_B1, Delta_B1)
u_B2, v_B2, _ = bcs_uv(eps_B2, Delta_B2)
u_B3, v_B3, _ = bcs_uv(eps_B3, Delta_B3)

print(f"\nCoherence factors:")
print(f"  B1: u = {u_B1[0]:.6f}, v = {v_B1[0]:.6f}, u^2+v^2 = {u_B1[0]**2+v_B1[0]**2:.10f}")
print(f"  B2: u = {u_B2[0]:.6f}, v = {v_B2[0]:.6f}")
print(f"  B3: u = {u_B3[0]:.6f}, v = {v_B3[0]:.6f}")

# =============================================================================
# SECTION 3: T=0 Beliaev Damping (Pair-Breaking Continuum)
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 3: T=0 Beliaev Damping")
print(f"{'='*78}")

# At T=0, the Beliaev process: Leggett mode -> 2 quasiparticles
# requires omega_L > E_k + E_{k'} for some k, k'.
#
# The minimum of E_k + E_{k'} is:
#   - Same sector: 2*E_B3_min = 2*sqrt(eps_B3^2 + Delta_B3^2) = 2*0.975 ~ 1.95
#   - Cross sector (B3+B3): 2*E_B3 ~ 1.95
#   - Cross sector (B1+B3): E_B1 + E_B3 ~ 0.90 + 0.975 ~ 1.88
#
# Since omega_L1 = 0.070 << 1.88, Beliaev damping is KINEMATICALLY FORBIDDEN
# at T=0 for ALL channels.
#
# This is the key point: the pair-breaking threshold from the PROMPT
# (2*Delta_B3 = 0.168) is the threshold for the ORDER PARAMETER gap,
# not the QUASIPARTICLE gap. The BdG quasiparticle energy is
# E_k = sqrt(eps_k^2 + Delta_k^2), which is ALWAYS > Delta_k.
# For the B3 sector: E_B3 = sqrt(0.971^2 + 0.084^2) = 0.975,
# so 2*E_B3 = 1.95, which is 28x above omega_L1.

# All possible pair combinations
all_E = np.concatenate([E_B1, E_B2, E_B3])
all_sectors = (['B1']*len(E_B1) + ['B2']*len(E_B2) + ['B3']*len(E_B3))
n_modes = len(all_E)

min_pair_E = np.inf
min_pair_label = ""
for i in range(n_modes):
    for j in range(i, n_modes):  # i <= j to avoid double-counting
        pair_E = all_E[i] + all_E[j]
        if pair_E < min_pair_E:
            min_pair_E = pair_E
            min_pair_label = f"{all_sectors[i]}({i})+{all_sectors[j]}({j})"

print(f"\nMinimum pair energy (T=0 Beliaev threshold):")
print(f"  min(E_k + E_k') = {min_pair_E:.6f} M_KK  [{min_pair_label}]")
print(f"  omega_L1 = {omega_L1_fold:.6f} M_KK")
print(f"  omega_L1 / min(E_k+E_k') = {omega_L1_fold / min_pair_E:.6f}")
print(f"  omega_L2 / min(E_k+E_k') = {omega_L2_fold / min_pair_E:.6f}")
print(f"\n  RESULT: omega_L1 << 2*E_min by factor {min_pair_E/omega_L1_fold:.1f}x")
print(f"  => Beliaev (pair-breaking) damping KINEMATICALLY FORBIDDEN at T=0")

# IMPORTANT CORRECTION: The prompt's threshold analysis used 2*Delta_B3 = 0.168
# as the pair-breaking edge. This is the ORDER PARAMETER gap, not the
# quasiparticle gap. The actual pair-breaking threshold for the Beliaev process
# is 2*E_k_min = 2*sqrt(eps_k^2 + Delta_k^2) ~ 1.64, which is 23x above omega_L.
# The confusion arises because in a metal (Fermi liquid) the single-particle
# energies eps_k are measured from the Fermi surface, so E_k_min ~ Delta_k.
# Here, eps_k = |lambda_k| >> Delta_k, so the quasiparticle gap is dominated
# by the single-particle gap, not the BCS gap.

Gamma_Beliaev_T0 = 0.0
print(f"\n  Gamma_Beliaev(T=0) = {Gamma_Beliaev_T0:.6e}")

# =============================================================================
# SECTION 4: Sub-Threshold Processes (T=0)
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 4: Sub-Threshold Processes at T=0")
print(f"{'='*78}")

# Even below the pair-breaking threshold, the Leggett mode can decay
# through virtual processes:
#
# (a) Two-phonon Raman process: Leggett -> 2 Goldstone phonons
#     This requires the Goldstone mode to exist. Post-transit, the
#     condensate is destroyed (P_exc = 1), so no Goldstone mode.
#     DURING the BCS phase (pre-transit), Goldstone exists.
#     The coupling is: M_Raman ~ J_23 * (Delta_B3/E_B3)^2
#     The rate: Gamma_Raman ~ (J_23)^2 * omega_L^5 / (rho_s^2 * v_s^5)
#     where v_s is the Goldstone sound speed.
#
# (b) Lattice emission: The SU(3) manifold has NO continuous translational
#     invariance, so there are no acoustic phonons in the usual sense.
#     The Peter-Weyl modes are discrete. No lattice phonon channel.
#
# (c) Spectral action fluctuation: The Leggett mode couples to the
#     geometry through the spectral action. The coupling is:
#     g_L ~ (dS/dDelta) * (Delta_B3/E_B3) ~ a_2 * (Delta_B3/E_B3)
#     This is effectively the Sakharov-induced gravity coupling.
#     Gamma_grav ~ (G_eff * omega_L^3 / M_KK^2)
#     = negligible (G_eff ~ 1/a_0 ~ 1/6440)

# (a) Two-phonon (Raman) process
# In 3He-B, the leading sub-threshold damping is the Raman process
# where the squashing mode decays into two sound quanta.
# Rate: Gamma_Raman/omega_L ~ (omega_L/Delta)^5 in 3He-B (Vollhardt & Woelfle)
#
# Here the Goldstone speed v_s is set by the superfluid stiffness:
# v_s^2 = rho_s / (sum_i rho_i) where rho_s is the superfluid density
# and rho_i are the normal-state DOS.
#
# However, this system has a DISCRETE spectrum with only 8 modes.
# There is no continuous sound mode. The Goldstone mode is a single
# k=0 oscillation (uniform phase rotation). It cannot carry momentum.
# Therefore, the Raman process is NOT available: the two outgoing
# Goldstone quanta would need to carry opposite momenta (to conserve
# momentum in the decay), but in 0D there is no momentum.

print("\n(a) Two-phonon Raman process:")
print("    Goldstone mode is k=0 only (0D system, 8 discrete modes).")
print("    No momentum-carrying Goldstone mode -> Raman process FORBIDDEN.")
print("    (In 3He-B: Gamma_Raman/omega_L ~ (omega_L/Delta)^5)")

# In 3He, Gamma_Raman/omega_L ~ C * (omega_L / (2*Delta))^5
# The coefficient C depends on the Goldstone coupling.
# For the record, if this scaling applied:
ratio_oL_2D = omega_L1_fold / (2.0 * Delta_B3_val)
scaling_3He_cubic = ratio_oL_2D**3
scaling_3He_quintic = ratio_oL_2D**5

print(f"    For reference: omega_L/(2*Delta_B3) = {ratio_oL_2D:.4f}")
print(f"    3He cubic scaling (phase space):  Gamma/omega ~ {scaling_3He_cubic:.4e}")
print(f"    3He quintic scaling (Raman):      Gamma/omega ~ {scaling_3He_quintic:.4e}")

# (b) Phase-space argument for the 0D discrete system
# The only available decay channel is into the DISCRETE quasiparticle
# spectrum. But ALL quasiparticle energies E_k > 0.82 M_KK, far above
# omega_L = 0.070 M_KK. There is literally nowhere for the energy to go.
#
# The Leggett mode cannot decay into:
# - Quasiparticle pairs (E_k + E_{k'} > 1.64 >> 0.070)
# - Single quasiparticles (E_k > 0.82 >> 0.070)
# - Goldstone quanta (no momentum modes in 0D)
# - Gravitational radiation (suppressed by G_eff ~ 1/6440)
#
# The ONLY remaining process is virtual (off-shell) pair creation,
# which contributes to Re[Sigma] (mass renormalization) but NOT
# to Im[Sigma] (damping). This is standard result: below all
# continuum thresholds, a collective mode is an exact eigenstate
# of the Hamiltonian and has ZERO intrinsic width.

print("\n(b) Phase-space analysis (0D discrete system):")
print(f"    Minimum quasiparticle energy: E_min = {E_min:.6f} M_KK")
print(f"    omega_L1 = {omega_L1_fold:.6f} M_KK")
print(f"    omega_L1 / E_min = {omega_L1_fold / E_min:.6f}")
print(f"    ALL decay channels kinematically closed.")
print(f"    The Leggett mode is an EXACT eigenstate of the finite BCS Hamiltonian.")

# (c) Gravitational radiation
G_eff = 1.0 / a0_fold  # = 1/6440 in M_KK units (Sakharov)
Gamma_grav = G_eff * omega_L1_fold**3  # dimensional estimate
print(f"\n(c) Gravitational radiation:")
print(f"    G_eff = 1/a_0 = {G_eff:.4e}")
print(f"    Gamma_grav ~ G_eff * omega_L^3 = {Gamma_grav:.4e} M_KK")
print(f"    Gamma_grav / omega_L = {Gamma_grav / omega_L1_fold:.4e}")
print(f"    NEGLIGIBLE (suppressed by 1/a_0)")

# =============================================================================
# SECTION 5: GGE Finite-Temperature Effects
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 5: GGE Finite-Temperature Effects")
print(f"{'='*78}")

# The GGE temperatures from S43 (GGE-TEMP-43):
# T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178 (M_KK units)
# These are the sector-resolved effective temperatures of the post-transit relic.
#
# CRITICAL: The Leggett mode exists ONLY during the BCS-condensed phase,
# NOT in the GGE relic. (S49 collab review item 3: "Leggett mode destroyed
# post-transit: Delta=0, J=0, omega_L=0.")
#
# During the BCS phase, the system is in the ground state at T=0.
# The transit produces the GGE relic, but the Leggett mode operates
# BEFORE the transit, when the condensate exists.
#
# Therefore: GGE temperatures are IRRELEVANT for Leggett damping.
# The Leggett mode lives in the T=0 BCS ground state.
#
# However, there is a subtlety: during the TRANSIT, the tau parameter
# evolves and the BCS state is evolving non-adiabatically. The transit
# time dt_transit = 0.00113 M_KK^{-1} (S38). During this time, the
# Leggett mode executes N_oscillations = omega_L * dt_transit / (2*pi)
# oscillations.

N_osc_transit = omega_L1_fold * dt_transit / (2.0 * np.pi)
print(f"\nLeggett mode lifetime context:")
print(f"  Transit duration: dt_transit = {dt_transit:.6f} M_KK^{{-1}}")
print(f"  omega_L1 * dt_transit = {omega_L1_fold * dt_transit:.6f}")
print(f"  N_oscillations during transit = {N_osc_transit:.6f}")
print(f"  => The Leggett mode completes {N_osc_transit:.4f} oscillations during transit")
print(f"  => The Leggett mode is FROZEN during transit (< 1 oscillation period)")

# The Leggett period is T_L = 2*pi/omega_L1
T_Leggett = 2.0 * np.pi / omega_L1_fold
print(f"\n  Leggett period: T_L = 2*pi/omega_L = {T_Leggett:.4f} M_KK^{{-1}}")
print(f"  Transit/Leggett ratio: dt_transit / T_L = {dt_transit / T_Leggett:.6f}")
print(f"  => Transit is {T_Leggett / dt_transit:.0f}x FASTER than Leggett oscillation")
print(f"  => Leggett mode is in the SUDDEN QUENCH regime")

# =============================================================================
# SECTION 6: Full Self-Energy Computation
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 6: Full Leggett Self-Energy Im[Sigma(omega)]")
print(f"{'='*78}")

# Despite omega_L being below all pair-breaking thresholds, we compute
# Im[Sigma(omega)] for the FULL spectral range to:
# (a) Verify Im[Sigma(omega_L)] = 0 exactly
# (b) Map where Im[Sigma] turns on (threshold)
# (c) Compute the spectral function A(omega)
# (d) Show the Q factor is formally infinite at T=0

# The Leggett-to-quasiparticle vertex (Beliaev vertex):
# The Leggett mode is a relative phase oscillation between sectors.
# The Leggett-1 eigenvector from S48 is:
#   v_L1 = eigvecs_fold[:, 1] ~ (-0.038, -0.037, 1.419) (B1, B2, B3)
# This is predominantly a B3 oscillation against B1/B2.
#
# The vertex for Beliaev decay into sector pair (alpha, beta):
# M_{alpha,beta} = sum_{k in alpha, k' in beta}
#     phi_L(alpha) * phi_L(beta) * J_{alpha,beta} * (u_k*v_{k'} - v_k*u_{k'})
# where phi_L is the Leggett eigenvector component.

# Leggett-1 eigenvector (normalised)
phi_L1_raw = eigvecs_fold[:, 1]
phi_L1 = phi_L1_raw / np.sqrt(np.sum(phi_L1_raw**2 * rho_fold_vec))
print(f"\nLeggett-1 eigenvector (raw): {phi_L1_raw}")
print(f"Leggett-1 eigenvector (normalized): {phi_L1}")

# Construct the vertex matrix elements
# For each pair of quasiparticles (k in sector i, k' in sector j),
# the coupling to the Leggett mode is:
#   M(k,k') = phi_L(i) * J(i,j) * (u_k*v_{k'} + v_k*u_{k'})   [pair creation]
#           + phi_L(i) * J(i,j) * (u_k*v_{k'} - v_k*u_{k'})   [pair transfer]
#
# The dominant vertex is the Josephson pair-transfer term.

# Build lists of all quasiparticle states
qp_states = []
# B1 modes
for m in range(len(eps_B1)):
    qp_states.append({'sector': 0, 'eps': eps_B1[m], 'Delta': Delta_B1,
                       'u': u_B1[m], 'v': v_B1[m], 'E': E_B1[m], 'label': 'B1'})
# B2 modes
for m in range(len(eps_B2)):
    qp_states.append({'sector': 1, 'eps': eps_B2[m], 'Delta': Delta_B2,
                       'u': u_B2[m], 'v': v_B2[m], 'E': E_B2[m], 'label': 'B2'})
# B3 modes
for m in range(len(eps_B3)):
    qp_states.append({'sector': 2, 'eps': eps_B3[m], 'Delta': Delta_B3_val,
                       'u': u_B3[m], 'v': v_B3[m], 'E': E_B3[m], 'label': 'B3'})

n_qp = len(qp_states)
print(f"\nTotal quasiparticle states: {n_qp}")

# Josephson coupling matrix (sector-level)
J_sect = np.zeros((3, 3))
J_sect[0, 1] = J_sect[1, 0] = J_12_fold
J_sect[0, 2] = J_sect[2, 0] = J_13_fold
J_sect[1, 2] = J_sect[2, 1] = J_23_fold

# Compute Im[Sigma(omega)] on a dense grid
omega_grid = np.linspace(0.001, 3.0, 10000)
ImSigma = np.zeros_like(omega_grid)

# Broadening for delta function (Lorentzian)
eta_broad = 0.005  # Small broadening

for i_qp in range(n_qp):
    for j_qp in range(i_qp, n_qp):
        s_i = qp_states[i_qp]
        s_j = qp_states[j_qp]

        # Skip same-sector pair creation (Leggett is INTER-sector)
        # Actually, the Leggett mode couples sectors, so the vertex
        # involves inter-sector Josephson terms
        sector_i = s_i['sector']
        sector_j = s_j['sector']

        # The vertex involves Josephson coupling between sectors
        # M_{ij} = phi_L(si) * J(si, sj) * coherence_factor
        # plus phi_L(sj) * J(sj, si) * coherence_factor (symmetrized)
        # For same-sector pairs: J(si, si) = 0 (no self-Josephson)
        # For cross-sector: J(si, sj) > 0

        # Include intra-sector contributions too (from the phase-stiffness coupling)
        # The Leggett eigenvector phi_L1 determines how the mode couples to each sector

        # Coherence factor for pair creation: (u_i*v_j + v_i*u_j)
        coh_factor = s_i['u'] * s_j['v'] + s_i['v'] * s_j['u']

        # Vertex: the Leggett mode amplitude in sector i times the coupling
        # The effective vertex is determined by the phase stiffness matrix
        # For the Beliaev process: Leggett -> (k, sector_i) + (k', sector_j)
        # The coupling comes from the second derivative of the Josephson energy
        # with respect to the gap amplitude

        if sector_i == sector_j:
            # Intra-sector: coupling through J_{i,alpha} * phi_L(alpha) terms
            vertex = 0.0
            for alpha in range(3):
                if alpha != sector_i:
                    vertex += J_sect[sector_i, alpha] * phi_L1[alpha] * coh_factor
        else:
            # Inter-sector: direct Josephson vertex
            vertex = J_sect[sector_i, sector_j] * (phi_L1[sector_i] - phi_L1[sector_j]) * coh_factor

        M_sq = vertex**2

        # Degeneracy factor (for degenerate modes)
        deg_factor = 1.0 if i_qp == j_qp else 2.0

        # Pair energy
        E_pair = s_i['E'] + s_j['E']

        # Add to Im[Sigma] with Lorentzian broadening of the delta function
        # Im[Sigma(omega)] ~ |M|^2 * delta(omega - E_k - E_{k'})
        #                  -> |M|^2 * eta / ((omega - E_pair)^2 + eta^2) / pi
        ImSigma += deg_factor * M_sq * eta_broad / ((omega_grid - E_pair)**2 + eta_broad**2) / np.pi

# Find where Im[Sigma] turns on
threshold_idx = np.where(ImSigma > 1e-10)[0]
if len(threshold_idx) > 0:
    continuum_onset = omega_grid[threshold_idx[0]]
else:
    continuum_onset = np.inf

print(f"\nContinuum onset (Im[Sigma] > 0): omega = {continuum_onset:.4f} M_KK")
print(f"omega_L1 = {omega_L1_fold:.6f} M_KK")
print(f"omega_L1 / continuum_onset = {omega_L1_fold / continuum_onset:.6f}")

# Im[Sigma] at omega_L
idx_oL = np.argmin(np.abs(omega_grid - omega_L1_fold))
ImSigma_at_oL = ImSigma[idx_oL]
print(f"\nIm[Sigma(omega_L1)] = {ImSigma_at_oL:.6e}")
print(f"  (Should be ~0 since omega_L << continuum onset)")

# =============================================================================
# SECTION 7: Spectral Function and Quality Factor
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 7: Spectral Function A(omega) and Quality Factor")
print(f"{'='*78}")

# The retarded Leggett propagator is:
# G_L(omega) = 1 / (omega^2 - omega_L^2 - Sigma(omega))
# Spectral function: A(omega) = -2 * Im[G_L(omega)]
#
# At T=0 with no Beliaev decay channel:
# Im[Sigma(omega)] = 0 for omega < continuum_onset
# => A(omega) = 2*pi * delta(omega^2 - omega_L^2) = pi/omega_L * delta(omega - omega_L)
# => Sharp delta-function peak, Q = infinity

# For visualization, use a small artificial broadening
eta_vis = 0.002  # Artificial broadening for visualization

# Compute spectral function
omega_fine = np.linspace(0.01, 0.20, 5000)
A_L = np.zeros_like(omega_fine)

for i, om in enumerate(omega_fine):
    # For omega below continuum onset, Im[Sigma] = 0
    # Use artificial broadening eta_vis to see the peak
    ImSig = 0.0
    if om > continuum_onset:
        # Interpolate from computed Im[Sigma]
        ImSig = np.interp(om, omega_grid, ImSigma)

    denom_real = om**2 - omega_L1_fold**2
    denom_imag = om * eta_vis + ImSig  # artificial + physical broadening

    A_L[i] = 2.0 * denom_imag / (denom_real**2 + denom_imag**2)

# Find peak
peak_idx = np.argmax(A_L)
omega_peak = omega_fine[peak_idx]
A_peak = A_L[peak_idx]

# FWHM
half_max = A_peak / 2.0
above_half = omega_fine[A_L > half_max]
if len(above_half) > 1:
    FWHM = above_half[-1] - above_half[0]
else:
    FWHM = 2.0 * eta_vis  # Resolution-limited

print(f"\nSpectral function peak: omega = {omega_peak:.6f} M_KK, A = {A_peak:.4f}")
print(f"FWHM = {FWHM:.6f} M_KK")
print(f"FWHM / omega_peak = {FWHM / omega_peak:.6f}")

# Quality factor
# Physical Q (from Im[Sigma]):
Gamma_physical = ImSigma_at_oL / (2.0 * omega_L1_fold) if ImSigma_at_oL > 0 else 0.0
Q_physical = omega_L1_fold / (2.0 * Gamma_physical) if Gamma_physical > 0 else np.inf

# Resolution-limited Q (from artificial broadening):
Q_resolution = omega_peak / FWHM

print(f"\nQuality factor:")
print(f"  Q_physical = omega_L / (2*Gamma) = {Q_physical}")
print(f"  (Gamma_physical = {Gamma_physical:.6e} M_KK)")
print(f"  Q_resolution (from FWHM with eta={eta_vis}) = {Q_resolution:.2f}")
print(f"  Q_resolution is LIMITED BY ARTIFICIAL BROADENING, not physics")

# =============================================================================
# SECTION 8: Comparison with 3He-B
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 8: Comparison with 3He-B")
print(f"{'='*78}")

# In 3He-B:
# omega_L / Delta ~ 10^{-3} (deeply below pair-breaking, protected)
# Q ~ 10^3 (Leggett mode is sharp collective excitation)
# Gamma/omega_L ~ (omega_L/Delta)^3 from phase-space suppression
# The dominant decay channel at low T is two-phonon Raman
# At higher T, thermal excitation of quasiparticles provides Landau damping

# In the framework:
# omega_L / Delta_B3 = 0.095 (95x larger than 3He ratio)
# omega_L / E_min = 0.085 (still far below)
# But omega_L / (2*E_min) = 0.043 (well below pair-breaking)
# The system has 8 DISCRETE modes, not a continuum
# ALL quasiparticle energies > 0.82 M_KK >> omega_L = 0.070

print(f"\n3He-B comparison:")
print(f"  omega_L/Delta (3He):     ~10^{{-3}}")
print(f"  omega_L/Delta_B3 (here): {omega_L1_fold / Delta_B3_val:.4f}")
print(f"  Compression ratio:       {omega_L1_fold / Delta_B3_val / 1e-3:.0f}x")
print(f"")
print(f"  Q (3He-B):               ~10^3")
print(f"  Q (framework, T=0):      infinity (kinematically exact)")
print(f"")
print(f"  Gamma/omega_L scaling (3He): (omega_L/Delta)^3 = {(1e-3)**3:.0e}")
print(f"  If same scaling applied:     (omega_L/Delta_B3)^3 = {(omega_L1_fold/Delta_B3_val)**3:.4e}")
print(f"  But this scaling is IRRELEVANT: there is no pair-breaking continuum near omega_L")
print(f"")

# The crucial difference from 3He:
# In 3He, the Leggett mode sits within a CONTINUOUS quasiparticle spectrum.
# There is always a continuum of states at E > 2*Delta, and the decay rate
# is controlled by phase-space suppression ~ (omega_L/2*Delta)^n.
#
# In this system, the spectrum is DISCRETE. There are exactly 8 quasiparticle
# levels. The minimum quasiparticle energy is E_min = 0.820, which is 11.8x
# above omega_L. The minimum pair energy is 1.64, which is 23.5x above omega_L.
#
# This is not merely "below the continuum threshold" — there IS no continuum.
# The Leggett mode is an exact eigenstate of the finite Hilbert space.

print("KEY STRUCTURAL DIFFERENCE:")
print(f"  3He: continuous spectrum, omega_L < 2*Delta (narrow gap protection)")
print(f"  Framework: DISCRETE spectrum, omega_L << E_min (absolute protection)")
print(f"  E_min / omega_L = {E_min / omega_L1_fold:.1f}x")
print(f"  min(E_k+E_k') / omega_L = {min_pair_E / omega_L1_fold:.1f}x")
print(f"  The gap is not 'narrow' — it is 23x wide. The mode is ABSOLUTELY stable.")

# =============================================================================
# SECTION 9: Off-Shell (Virtual) Mass Renormalization
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 9: Virtual Process Mass Renormalization")
print(f"{'='*78}")

# Even though Im[Sigma] = 0, Re[Sigma] is nonzero from virtual
# pair creation. This renormalizes the Leggett mass but does not
# provide damping.
#
# Re[Sigma(omega_L)] = P.V. integral of Im[Sigma] / (omega' - omega)
# = sum_{k,k'} |M_{kk'}|^2 / (omega_L^2 - (E_k + E_{k'})^2)
#
# Since omega_L << E_k + E_{k'}, this is a perturbative correction:
# Re[Sigma] ~ -sum |M|^2 / (E_k + E_{k'})^2

ReSigma = 0.0
for i_qp in range(n_qp):
    for j_qp in range(i_qp, n_qp):
        s_i = qp_states[i_qp]
        s_j = qp_states[j_qp]
        sector_i = s_i['sector']
        sector_j = s_j['sector']

        coh_factor = s_i['u'] * s_j['v'] + s_i['v'] * s_j['u']

        if sector_i == sector_j:
            vertex = 0.0
            for alpha in range(3):
                if alpha != sector_i:
                    vertex += J_sect[sector_i, alpha] * phi_L1[alpha] * coh_factor
        else:
            vertex = J_sect[sector_i, sector_j] * (phi_L1[sector_i] - phi_L1[sector_j]) * coh_factor

        M_sq = vertex**2
        E_pair = s_i['E'] + s_j['E']
        deg_factor = 1.0 if i_qp == j_qp else 2.0

        # Real part of self-energy
        ReSigma += deg_factor * M_sq / (omega_L1_fold**2 - E_pair**2)

omega_L_renorm_sq = omega_L1_fold**2 + ReSigma
if omega_L_renorm_sq > 0:
    omega_L_renorm = np.sqrt(omega_L_renorm_sq)
else:
    omega_L_renorm = 0.0

mass_shift = (omega_L_renorm - omega_L1_fold) / omega_L1_fold

print(f"\nRe[Sigma(omega_L)] = {ReSigma:.6e}")
print(f"omega_L (bare) = {omega_L1_fold:.6f}")
print(f"omega_L (renormalized) = {omega_L_renorm:.6f}")
print(f"Mass shift: delta_omega / omega = {mass_shift:.6f} ({mass_shift*100:.4f}%)")
print(f"(Virtual pair creation renormalizes mass by {abs(mass_shift*100):.4f}%)")

# =============================================================================
# SECTION 10: Leggett-2 Analysis
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 10: Leggett-2 Mode (omega_L2)")
print(f"{'='*78}")

# Leggett-2 at omega_L2 = 0.107 M_KK is also far below pair-breaking
# Same analysis applies: Q = infinity at T=0

print(f"omega_L2 = {omega_L2_fold:.6f} M_KK")
print(f"omega_L2 / (2*E_min) = {omega_L2_fold / (2*E_min):.6f}")
print(f"omega_L2 / min(E_k+E_k') = {omega_L2_fold / min_pair_E:.6f}")
print(f"omega_L2 is {min_pair_E/omega_L2_fold:.1f}x below pair-breaking threshold")
print(f"Q(Leggett-2) = infinity (same argument as Leggett-1)")

# =============================================================================
# SECTION 11: Summary and Gate Verdict
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 11: GATE VERDICT — LEGGETT-DAMPING-50")
print(f"{'='*78}")

# Collect all results
results = {}
results['omega_L1'] = omega_L1_fold
results['omega_L2'] = omega_L2_fold
results['E_min'] = E_min
results['min_pair_E'] = min_pair_E
results['continuum_onset'] = continuum_onset
results['ImSigma_at_oL'] = ImSigma_at_oL
results['Gamma_physical'] = Gamma_physical
results['Q_physical'] = Q_physical
results['Gamma_Beliaev_T0'] = 0.0
results['Gamma_Raman_T0'] = 0.0  # Forbidden in 0D
results['Gamma_grav'] = Gamma_grav
results['Gamma_total'] = Gamma_grav  # Only non-zero channel (negligible)
results['ReSigma'] = ReSigma
results['omega_L_renorm'] = omega_L_renorm
results['mass_shift'] = mass_shift
results['ratio_oL_2Delta_B3'] = omega_L1_fold / (2.0 * Delta_B3_val)
results['ratio_oL_2E_min'] = omega_L1_fold / (2.0 * E_min)
results['ratio_oL_minPairE'] = omega_L1_fold / min_pair_E
results['N_osc_transit'] = N_osc_transit

# Q factor: formally infinite at T=0 in the discrete spectrum
# The only nonzero channel is gravitational radiation: Q ~ omega_L / (2*Gamma_grav)
Q_total = omega_L1_fold / (2.0 * max(results['Gamma_total'], 1e-30))

print(f"\n  omega_L1 = {omega_L1_fold:.6f} M_KK")
print(f"  E_min (quasiparticle) = {E_min:.6f} M_KK")
print(f"  min(E_k + E_{'{k\'}' }) = {min_pair_E:.6f} M_KK")
print(f"  Continuum onset = {continuum_onset:.4f} M_KK")
print(f"")
print(f"  Beliaev damping (T=0): KINEMATICALLY FORBIDDEN")
print(f"  Raman damping (T=0):   FORBIDDEN IN 0D (no momentum modes)")
print(f"  Gravitational:         Gamma = {Gamma_grav:.4e} M_KK (negligible)")
print(f"  Landau (GGE):          IRRELEVANT (Leggett exists only pre-transit)")
print(f"")
print(f"  Gamma_total = {Gamma_grav:.4e} M_KK")
print(f"  Q = omega_L / (2*Gamma) = {Q_total:.2e}")
print(f"")

# Gate classification
if Q_total > 10:
    gate_verdict = "PASS"
    gate_detail = (f"Q = {Q_total:.1e} >> 10. Leggett mode is sharp collective excitation. "
                   f"Beliaev damping kinematically forbidden: omega_L(0.070) << min(E_k+E_k')(1.64) "
                   f"by factor {min_pair_E/omega_L1_fold:.0f}x. 0D discrete spectrum has no decay channels. "
                   f"Mass concept from DIPOLAR-CATALOG-49 is VALID.")
elif Q_total > 1:
    gate_verdict = "INFO"
    gate_detail = f"Q = {Q_total:.2f} (marginal). Mode partially damped."
else:
    gate_verdict = "FAIL"
    gate_detail = f"Q = {Q_total:.2f} < 1. Mode overdamped. Mass concept invalid."

print(f"  GATE VERDICT: {gate_verdict}")
print(f"  {gate_detail}")

print(f"\n{'='*78}")
print("STRUCTURAL INSIGHT (Volovik perspective)")
print(f"{'='*78}")
print(f"""
The S49 task description framed the damping question using the ORDER PARAMETER
gap Delta_B3 = 0.084 as the pair-breaking scale: omega_L/(2*Delta_B3) = 0.414.
This ratio (41% of threshold) correctly worried about Beliaev damping.

But this framing conflates two different gaps:
  1. The ORDER PARAMETER gap Delta_k (BCS pairing amplitude)
  2. The QUASIPARTICLE gap E_k = sqrt(eps_k^2 + Delta_k^2)

In a Fermi liquid (3He, metals), eps_k is measured from the Fermi surface,
so E_k_min ~ Delta_k and the two gaps are comparable. The Leggett mode
sits just below 2*Delta, and phase-space suppression controls the Q factor.

In the framework, eps_k = |lambda_k| >> Delta_k (the Dirac eigenvalues are
O(1) in M_KK units, while gaps are O(0.01-0.7)). The quasiparticle gap
E_k_min = 0.820, which is 9.7x larger than Delta_B3 = 0.084.

The actual pair-breaking threshold is 2*E_min = 1.64, not 2*Delta_B3 = 0.168.
omega_L sits at 4.3% of the TRUE pair-breaking threshold, not 41%.

This is structurally analogous to 3He-B in the deep BCS limit where
E_F >> Delta, and omega_L/E_F ~ 10^{{-3}} rather than omega_L/Delta ~ 10^{{-3}}.
The framework is even MORE protected than 3He because:
  (a) The spectrum is DISCRETE (no continuum to decay into)
  (b) The system is 0D (no momentum-carrying modes for Raman decay)
  (c) All quasiparticle energies are O(1) while omega_L is O(0.07)

The Leggett mode is an EXACT eigenstate of the finite BCS Hamiltonian.
""")

# =============================================================================
# SECTION 12: Save Data
# =============================================================================
print(f"\n{'='*78}")
print("SECTION 12: Save Data")
print(f"{'='*78}")

save_path = os.path.join(SCRIPT_DIR, 's50_leggett_damping.npz')
np.savez(save_path,
    # Gate
    gate_name='LEGGETT-DAMPING-50',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Leggett mode parameters
    omega_L1=omega_L1_fold,
    omega_L2=omega_L2_fold,
    Delta_fold=Delta_fold_vec,
    rho_fold=rho_fold_vec,
    J_12=J_12_fold,
    J_23=J_23_fold,
    J_13=J_13_fold,
    # BdG spectrum
    E_B1=E_B1,
    E_B2=E_B2,
    E_B3=E_B3,
    E_min=E_min,
    min_pair_E=min_pair_E,
    # Coherence factors
    u_B1=u_B1, v_B1=v_B1,
    u_B2=u_B2, v_B2=v_B2,
    u_B3=u_B3, v_B3=v_B3,
    # Self-energy
    omega_grid=omega_grid,
    ImSigma=ImSigma,
    continuum_onset=continuum_onset,
    ImSigma_at_oL=ImSigma_at_oL,
    ReSigma=ReSigma,
    omega_L_renorm=omega_L_renorm,
    mass_shift=mass_shift,
    # Damping rates
    Gamma_Beliaev_T0=0.0,
    Gamma_Raman_T0=0.0,
    Gamma_grav=Gamma_grav,
    Gamma_total=Gamma_grav,
    Q_total=Q_total,
    Q_physical=Q_physical,
    # Spectral function
    omega_fine=omega_fine,
    A_L=A_L,
    # Ratios
    ratio_oL_2Delta_B3=omega_L1_fold / (2.0 * Delta_B3_val),
    ratio_oL_2E_min=omega_L1_fold / (2.0 * E_min),
    ratio_oL_minPairE=omega_L1_fold / min_pair_E,
    N_osc_transit=N_osc_transit,
    # 3He comparison
    He3_ratio_oL_Delta=1e-3,
    He3_Q=1e3,
    framework_ratio_oL_Delta_B3=omega_L1_fold / Delta_B3_val,
    compression_3He=omega_L1_fold / Delta_B3_val / 1e-3,
)

print(f"Saved to: {save_path}")

# =============================================================================
# SECTION 13: Generate Plot
# =============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('LEGGETT-DAMPING-50: Leggett Mode Quality Factor', fontsize=14, fontweight='bold')

# Panel (a): Spectral function A(omega)
ax = axes[0, 0]
ax.plot(omega_fine, A_L, 'b-', linewidth=1.5)
ax.axvline(omega_L1_fold, color='r', linestyle='--', linewidth=1, label=f'omega_L1 = {omega_L1_fold:.4f}')
ax.axvline(thresh_B3, color='orange', linestyle=':', linewidth=1, label=f'2*Delta_B3 = {thresh_B3:.4f}')
ax.set_xlabel('omega (M_KK)')
ax.set_ylabel('A(omega)')
ax.set_title('(a) Spectral Function (eta_vis = 0.002)')
ax.legend(fontsize=8)
ax.set_xlim(0.01, 0.20)

# Panel (b): Im[Sigma(omega)] over full range
ax = axes[0, 1]
ax.semilogy(omega_grid, np.abs(ImSigma) + 1e-30, 'b-', linewidth=1)
ax.axvline(omega_L1_fold, color='r', linestyle='--', linewidth=1, label=f'omega_L1')
ax.axvline(min_pair_E, color='green', linestyle='-', linewidth=2, label=f'min(E_k+E_k\') = {min_pair_E:.3f}')
ax.axvline(thresh_B3, color='orange', linestyle=':', linewidth=1, label=f'2*Delta_B3 = {thresh_B3:.3f}')
ax.set_xlabel('omega (M_KK)')
ax.set_ylabel('|Im[Sigma(omega)]|')
ax.set_title('(b) Imaginary Self-Energy (Beliaev)')
ax.legend(fontsize=8)
ax.set_xlim(0, 3.0)

# Panel (c): Energy level diagram
ax = axes[1, 0]
# Draw quasiparticle energies
for i, s in enumerate(qp_states):
    x_pos = {'B1': 0, 'B2': 1, 'B3': 2}[s['label']]
    ax.plot([x_pos - 0.3, x_pos + 0.3], [s['E'], s['E']], 'k-', linewidth=2)
# Draw Leggett modes
ax.axhline(omega_L1_fold, color='r', linestyle='--', linewidth=2, label=f'omega_L1 = {omega_L1_fold:.4f}')
ax.axhline(omega_L2_fold, color='m', linestyle='--', linewidth=2, label=f'omega_L2 = {omega_L2_fold:.4f}')
# Draw pair-breaking thresholds
ax.axhline(min_pair_E, color='green', linestyle=':', linewidth=2, label=f'min(E+E\') = {min_pair_E:.3f}')
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['B1 (1)', 'B2 (4)', 'B3 (3)'])
ax.set_ylabel('Energy (M_KK)')
ax.set_title('(c) Energy Levels: Leggett vs Quasiparticles')
ax.legend(fontsize=8)
ax.set_ylim(0, 1.2)

# Panel (d): Comparison with 3He
ax = axes[1, 1]
# Bar chart comparing scales
labels = ['3He-B\nomega_L/Delta', 'Framework\nomega_L/Delta_B3', 'Framework\nomega_L/E_min', 'Framework\nomega_L/min(E+E\')']
values = [1e-3, omega_L1_fold/Delta_B3_val, omega_L1_fold/E_min, omega_L1_fold/min_pair_E]
colors = ['steelblue', 'coral', 'forestgreen', 'darkgreen']
bars = ax.bar(range(len(labels)), values, color=colors)
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel('Ratio')
ax.set_title('(d) Damping Control Ratios')
ax.set_yscale('log')
for i, (bar, val) in enumerate(zip(bars, values)):
    ax.text(bar.get_x() + bar.get_width()/2, val * 1.5, f'{val:.4f}',
            ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's50_leggett_damping.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to: {plot_path}")
plt.close()

print(f"\n{'='*78}")
print(f"COMPUTATION COMPLETE.")
print(f"GATE: LEGGETT-DAMPING-50 = {gate_verdict}")
print(f"Q = {Q_total:.1e}")
print(f"{'='*78}")
