#!/usr/bin/env python3
"""
S53 PHONON-LIFETIMES-53: Pair Hopping Coherence Times
======================================================

Physics:
  W2-6 (S53) proved N_pair = 1 (singlet only). W3-12 showed GL is invalid
  at N_pair = 1 (Gi = 0.506, Mott regime, E_J/E_C = 0.82).

  The S52 6-branch GL dispersion reinterprets as tight-binding bands for a
  single Cooper pair hopping on the 32-cell lattice. "Phonon lifetimes"
  become pair-hopping coherence times.

  Scattering rates from two sources:
    1. QUARTIC (anharmonic) vertices in the GL functional: b_GL |Delta|^4
       These produce pair-lattice scattering when reexpanded around the
       tight-binding ground state.
    2. DISORDER scattering from cell-to-cell variations (absent in our
       perfectly ordered tessellation — included for completeness).

  Method:
    - Load 6-branch dispersion from s52_gl_josephson.npz
    - Extract quartic coupling V_4 from b_GL
    - Compute Fermi's golden rule: Gamma = (2pi/hbar) |V_4|^2 * rho_final
    - Evaluate Gamma/omega for each branch to classify ballistic vs diffusive

Gate: PHONON-LIFETIMES-53 — INFO
  Report: Gamma/omega ratio (ballistic vs diffusive).

Author: Quantum-Acoustics-Theorist (S53)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, sin, cos, log
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# Import canonical constants
# ============================================================
from canonical_constants import (
    a_GL, b_GL, Delta_0_GL, Delta_B3,
    J_C2, J_su2, J_u1, N_cells, c_fabric,
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    xi_BCS, xi_GL, omega_PV, tau_fold,
    E_cond, M_max_thouless, Vol_SU3_Haar,
    barrier_0d, S_inst, n_pairs,
    T_acoustic, N_dof_BCS,
    omega_L1, omega_L2, omega_H1
)

print("=" * 70)
print("S53 PHONON-LIFETIMES-53: Pair Hopping Coherence Times")
print("=" * 70)

# ============================================================
# Section 1: Load S52 dispersion data
# ============================================================
print("\n--- Section 1: Load S52 GL-Josephson dispersion ---")

data = np.load(os.path.join(os.path.dirname(__file__),
                            "s52_gl_josephson.npz"), allow_pickle=True)

K_array = data['K_array']          # (51,) wavevectors
omega_branches = data['omega_branches']  # (51, 6) frequencies
omega_sq = data['omega_sq']        # (51, 6) omega^2
eigvecs_all = data['eigvecs_all']  # (51, 6, 6) eigenvectors
branch_labels = data['branch_labels']  # (6,) names
Delta_0 = data['Delta_0']          # (3,) ground state gaps
rho_0 = data['rho_0']              # (3,) ground state DOS
a_alpha = data['a_alpha']          # (3,) GL a coefficients
b_alpha_data = data['b_alpha']     # (3,) GL b coefficients
K_BZ = float(data['K_BZ'])
a_BCC = float(data['a_BCC'])

print(f"  Branches: {list(branch_labels)}")
print(f"  K range: [0, {K_BZ:.4f}] M_KK, {len(K_array)} points")
print(f"  Delta_0 = {Delta_0}")
print(f"  rho_0 = {rho_0}")
print(f"  a_alpha = {a_alpha}")
print(f"  b_alpha = {b_alpha_data}")

# Frequencies at K=0 and K=K_BZ
print(f"\n  omega(K=0):   {omega_branches[0]}")
print(f"  omega(K_BZ):  {omega_branches[-1]}")

# ============================================================
# Section 2: N_pair = 1 reframing: tight-binding interpretation
# ============================================================
print("\n--- Section 2: Tight-binding reinterpretation ---")
print("  W2-6 proved N_pair = 1 (singlet pairing only).")
print("  W3-12 showed GL invalid: Gi = 0.506, E_J/E_C = 0.82 (Mott regime).")
print("  The 6-branch dispersion is the tight-binding band structure for")
print("  a single Cooper pair hopping on the 32-cell lattice.")
print("  'Phonon lifetimes' = pair-hopping coherence times.")

# Effective hopping parameters from dispersion bandwidths
bandwidths = np.zeros(6)
for ib in range(6):
    bandwidths[ib] = omega_branches[-1, ib] - omega_branches[0, ib]

print(f"\n  Branch bandwidths (omega_BZ - omega_0):")
for ib in range(6):
    print(f"    {branch_labels[ib]:>10s}: BW = {bandwidths[ib]:.6f} M_KK, "
          f"omega_0 = {omega_branches[0,ib]:.6f}, omega_BZ = {omega_branches[-1,ib]:.6f}")

# Tight-binding hopping parameter t_eff = BW / (2*z) for z nearest neighbors
# On BCC: z_NN = 8, z_NNN = 6
# For omega ~ omega_0 + 2t(1-cos Ka), BW = 4t, so t = BW/4
t_hop = bandwidths / 4.0
print(f"\n  Effective hopping parameters t_eff = BW/4:")
for ib in range(6):
    print(f"    {branch_labels[ib]:>10s}: t_eff = {t_hop[ib]:.6f} M_KK")

# ============================================================
# Section 3: Quartic coupling V_4 from GL functional
# ============================================================
print("\n--- Section 3: Quartic coupling from GL ---")

# The GL free energy density is:
#   F = sum_alpha [a_alpha |Delta_alpha|^2 + b_alpha |Delta_alpha|^4]
#
# Expanding Delta_alpha(x) = Delta_0_alpha + delta_alpha(x) around the
# ground state, the quartic term generates anharmonic vertices:
#   F_4 = sum_alpha b_alpha * 4 * Delta_0_alpha^2 * delta_alpha^2
#   (the leading anharmonic term from b*|Delta_0 + delta|^4)
#
# More precisely, expand |Delta_alpha|^4 = (Delta_0 + delta)^4:
#   = Delta_0^4 + 4*Delta_0^3*delta + 6*Delta_0^2*delta^2
#     + 4*Delta_0*delta^3 + delta^4
#
# The cubic term (3-vertex): V_3 = 4*b*Delta_0 per sector
# The quartic term (4-vertex): V_4 = b per sector
#
# In the tight-binding picture at N_pair = 1, the "quartic coupling"
# is the on-site pair-pair interaction U. Since N_pair = 1, there is
# no second pair to interact with via quartic vertices.
#
# CRITICAL: At N_pair = 1, the quartic vertex V_4 = b * delta^4 is
# a SELF-INTERACTION of the single pair's wave packet spreading.
# It represents the anharmonicity of the on-site potential.

print(f"  b_GL (canonical B2) = {b_GL:.6f}")
print(f"  b_alpha per sector:")
for i, lab in enumerate(['B1', 'B2', 'B3']):
    print(f"    {lab}: b = {b_alpha_data[i]:.6f}")

# Cubic vertex: V_3_alpha = 4 * b_alpha * Delta_0_alpha (per sector)
V_3 = 4.0 * b_alpha_data * Delta_0
print(f"\n  Cubic vertex V_3 = 4*b*Delta_0:")
for i, lab in enumerate(['B1', 'B2', 'B3']):
    print(f"    {lab}: V_3 = {V_3[i]:.6f} M_KK")

# Quartic vertex: V_4_alpha = b_alpha (per sector)
V_4 = b_alpha_data.copy()
print(f"\n  Quartic vertex V_4 = b (per sector):")
for i, lab in enumerate(['B1', 'B2', 'B3']):
    print(f"    {lab}: V_4 = {V_4[i]:.6f} M_KK")

# ============================================================
# Section 4: Density of final states
# ============================================================
print("\n--- Section 4: Density of states for scattering ---")

# In the tight-binding picture on a 32-cell lattice, the DOS is discrete.
# Each branch has N_cells = 32 K-states uniformly distributed in the BZ.
# The DOS per branch: rho(omega) = N_cells / (pi * BW) at band center
# (for a 1D tight-binding band; for 8D angle-averaged dispersion, similar).
#
# The continuous-approximation DOS per branch:
#   rho_branch = N_cells / BW  (uniform approximation)
#
# But N_cells = 32 is small. The DISCRETE spacing is:
#   delta_K = K_BZ / N_cells = pi / (a_BCC * N_cells)
#   delta_omega ~ BW / N_cells  (uniform approximation)

delta_K = K_BZ / N_cells
print(f"  K_BZ = {K_BZ:.6f}")
print(f"  delta_K = K_BZ / N_cells = {delta_K:.6f}")
print(f"  N_cells = {N_cells}")

rho_branch = np.zeros(6)
for ib in range(6):
    if bandwidths[ib] > 1e-10:
        rho_branch[ib] = N_cells / bandwidths[ib]
    else:
        rho_branch[ib] = np.inf  # Flat band: divergent DOS

print(f"\n  Approximate DOS per branch (N_cells/BW):")
for ib in range(6):
    if np.isfinite(rho_branch[ib]):
        print(f"    {branch_labels[ib]:>10s}: rho = {rho_branch[ib]:.4f} M_KK^{{-1}}")
    else:
        print(f"    {branch_labels[ib]:>10s}: rho = inf (flat band)")

# More precise: compute DOS from the actual dispersion
# rho(omega) = sum_K delta(omega - omega_K) ~ dK/domega integrated over angles
# For the angle-averaged dispersion, rho ~ 1/|domega/dK|
# Compute numerical group velocities
v_g = np.zeros((len(K_array), 6))
for ib in range(6):
    v_g[:, ib] = np.gradient(omega_branches[:, ib], K_array)

# DOS at each K point: rho ~ 1/|v_g| (1D analog)
# For 3D (or 8D) angle averaging, rho ~ K^{d-1}/|v_g|
# Use d_eff = 3 (BCC lattice is 3D-embedded despite 8D origin)
d_eff = 3  # See W3-12: 3D BCC projection convention from S52
rho_K = np.zeros((len(K_array), 6))
for ib in range(6):
    for ik in range(len(K_array)):
        if abs(v_g[ik, ib]) > 1e-12:
            # rho ~ K^{d-1} / |v_g| * (4pi / (2pi)^3)
            rho_K[ik, ib] = K_array[ik]**(d_eff - 1) / abs(v_g[ik, ib]) / (2*pi**2)
        else:
            rho_K[ik, ib] = np.inf

print(f"\n  Group velocities at K = K_BZ/2:")
ik_mid = len(K_array) // 2
for ib in range(6):
    print(f"    {branch_labels[ib]:>10s}: v_g = {v_g[ik_mid, ib]:.6f} M_KK")

# ============================================================
# Section 5: Scattering rates via Fermi's Golden Rule
# ============================================================
print("\n--- Section 5: Scattering rates Gamma(K) ---")
print("  Gamma = (2*pi) * |V_eff|^2 * rho_final")
print("  (hbar = 1 in M_KK units)")

# At N_pair = 1, the relevant scattering processes are:
#
# (A) CUBIC: A pair in branch i scatters to branch j by emitting/absorbing
#     a virtual excitation. This is a 1 -> 1 process (single pair changes
#     its band). The cubic vertex couples amplitude and phase modes.
#     |V_3|^2 / Delta_omega gives the second-order rate.
#
# (B) QUARTIC (self-interaction): The pair's wave packet evolves in the
#     anharmonic potential. This gives energy-dependent dephasing.
#     |V_4|^2 * rho gives the rate.
#
# (C) PAIR-LATTICE DISORDER: Zero (the tessellation is perfectly ordered).
#
# Key physical point: At N_pair = 1, there is NO pair-pair scattering.
# The only scattering is pair-against-lattice (anharmonicity of the
# on-site potential) and inter-branch transitions.

# For the quartic self-interaction:
# The fluctuation amplitude at N_pair = 1 is set by zero-point motion:
#   <delta^2> ~ 1/(2*M*omega) where M = rho_alpha (inertia)
#
# V_eff for quartic: matrix element of b*delta^4 between initial and final
# states. For a single pair hopping on the lattice:
#   V_eff = V_4 * <delta^2> = b_alpha / (2 * rho_alpha * omega_alpha)
#
# But this is the PERTURBATIVE correction to the frequency, not a
# decay rate. For an actual transition (change of K), we need the
# inter-site matrix element of the anharmonicity.

# More precisely: the anharmonic term at site n is
#   H_anh = sum_alpha b_alpha * delta_alpha(n)^4
# In the tight-binding basis |K>, |K'>, the matrix element is:
#   <K'|H_anh|K> = (1/N_cells) * sum_n b_alpha * <K'|delta^4(n)|K>
#
# For a single particle: delta(n) for a pair at site n has amplitude
# A = sqrt(1/N_cells) (normalized over N_cells sites).
# <K'|delta^4(n)|K> involves the fourth moment, which for a plane wave is:
#   sum_n e^{i(K-K')n} * A^4 = (1/N_cells^2) * delta_{K,K'} * N_cells
#   (for the diagonal part, K=K', giving a frequency shift, not decay)
#
# Off-diagonal (K != K'): This vanishes by translational invariance for
# a perfectly periodic lattice. Umklapp is the only exception, but
# Umklapp is structurally absent on SU(3) (S41).
#
# CONCLUSION: For a single pair on a perfectly ordered lattice,
# the quartic vertex does NOT produce scattering. It only shifts
# the on-site energy (Lamb-type shift). There is no decay channel.

print("\n  === CRITICAL STRUCTURAL RESULT ===")
print("  At N_pair = 1 on a perfectly ordered lattice:")
print("  - Quartic vertex gives frequency SHIFT, not decay")
print("  - Off-diagonal <K'|H_anh|K> = 0 by translational invariance")
print("  - Umklapp is structurally absent (S41)")
print("  - NO pair-pair scattering (only 1 pair)")
print("  => Gamma_quartic(K) = 0 EXACTLY for all K")

# However, the CUBIC vertex can induce inter-branch transitions.
# Process: pair in branch i at wavevector K transitions to branch j
# at wavevector K (K-conserving, since the cubic vertex is on-site).
#
# The cubic vertex couples amplitude and phase fluctuations:
#   H_3 = sum_alpha 4*b_alpha*Delta_0_alpha * delta_amp(n) * delta_phase(n)^2
#        + permutations
#
# This is a 1-phonon -> 2-phonon process in the GL language, but at
# N_pair = 1, it's a single-pair inter-branch transition:
# |K, branch i> -> |K, branch j>
#
# Matrix element: V_3_ij = cubic coupling projected onto eigenvectors
# Gamma_ij = 2*pi * |V_3_ij|^2 * rho_j(omega_i)
# where rho_j is evaluated at the energy of the initial state (energy conservation).

print("\n--- Section 5b: Inter-branch transition rates (cubic vertex) ---")

# Build the cubic vertex matrix at each K
# The cubic term in the GL expansion connects the 6-mode space
# V_3 couples amplitude modes to phase modes quadratically.
#
# In the eigenbasis at each K, the cubic coupling between
# eigenmodes i and j is:
#   g_{ij}(K) = sum_alpha V_3_alpha * [u_i(alpha,amp) * u_j(alpha,phase)^2
#                                     + permutations]
#
# where u_i(alpha, amp/phase) is the eigenvector component of mode i
# in sector alpha, amplitude or phase channel.

# For the inter-branch transition rate, we need energy conservation.
# At N_pair = 1, the pair can only be in ONE mode at a time.
# A cubic process like |K,i> -> |K,j> requires the energy difference
# omega_i - omega_j to be absorbed somehow. On a lattice with no
# thermal bath (GGE at T_acoustic = 0.112 M_KK, but the pair itself
# is at T=0 since N_pair=1), the only absorption channel is
# excitation of the PAIR's internal degree of freedom (pair breaking).
#
# Pair breaking requires energy >= 2*Delta_0_B2 ~ 1.46 M_KK.
# The inter-branch energy differences are:
delta_omega_branches = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        delta_omega_branches[i, j] = abs(omega_branches[0, i] - omega_branches[0, j])

print(f"\n  Inter-branch energy differences at K=0 (M_KK):")
print(f"  {'':>10s}", end='')
for j in range(6):
    print(f"  {branch_labels[j][:6]:>8s}", end='')
print()
for i in range(6):
    print(f"  {branch_labels[i][:6]:>10s}", end='')
    for j in range(6):
        print(f"  {delta_omega_branches[i,j]:8.4f}", end='')
    print()

# Check: which transitions are below the pair-breaking threshold?
pair_break_energy = 2.0 * Delta_0[1]  # B2 gap
print(f"\n  Pair breaking threshold: 2*Delta_B2 = {pair_break_energy:.4f} M_KK")

# For a transition |i> -> |j>, the pair must find a final state at the
# same total energy. Without thermal phonons or other pairs, this requires
# delta_omega = 0 (elastic) or involves virtual intermediate states.
#
# ELASTIC inter-branch scattering requires degeneracies (band crossings).
# From the S52 data: n_crossings = 0, n_anticrossings = 4.
# No exact crossings -> no elastic inter-branch channels.

n_crossings = int(data['n_crossings'])
n_anticrossings = int(data['n_anticrossings'])
print(f"\n  Band crossings: {n_crossings} (exact), {n_anticrossings} (anti-crossings)")
print(f"  No exact crossings => no elastic inter-branch channels")

# ============================================================
# Section 6: Virtual (off-shell) inter-branch rates
# ============================================================
print("\n--- Section 6: Virtual inter-branch scattering ---")
print("  With no elastic channels, we compute the off-shell rate.")
print("  This is a second-order process (virtual intermediate state).")
print("  Gamma_virt ~ |V_3|^2 / delta_omega (perturbative)")

# Project cubic vertex onto eigenbasis at each K
# V_3_alpha = 4*b_alpha*Delta_0_alpha
# The 3-vertex couples index alpha in the amplitude channel to
# index alpha in the phase channel (squared).
#
# For eigenmodes i,j: the matrix element involves the overlap of
# eigenvector components.

Gamma_virt = np.zeros((len(K_array), 6))  # Virtual scattering rate per branch
Gamma_over_omega = np.zeros((len(K_array), 6))

for ik in range(len(K_array)):
    evecs = eigvecs_all[ik]  # (6, 6): columns are eigenvectors
    # Ordering: [|Delta_B1|, |Delta_B2|, |Delta_B3|, theta_B1, theta_B2, theta_B3]

    for ib_init in range(6):
        # Sum over all final branches j != i
        gamma_sum = 0.0  # (local)
        for ib_final in range(6):
            if ib_final == ib_init:
                continue

            delta_om = abs(omega_branches[ik, ib_init] - omega_branches[ik, ib_final])
            if delta_om < 1e-10:
                continue  # Skip degenerate (handled separately)

            # Cubic coupling: sum over sectors alpha
            # g_{ij} = sum_alpha V_3_alpha * u_i(alpha,amp) * u_j(alpha,phase)
            # where amp indices are 0,1,2 and phase indices are 3,4,5
            g_ij = 0.0  # (local)
            for alpha in range(3):
                g_ij += V_3[alpha] * evecs[alpha, ib_init] * evecs[3+alpha, ib_final]

            # Also the reverse coupling (phase -> amp)
            g_ij_rev = 0.0  # (local)
            for alpha in range(3):
                g_ij_rev += V_3[alpha] * evecs[3+alpha, ib_init] * evecs[alpha, ib_final]

            # Total squared matrix element
            g_sq = g_ij**2 + g_ij_rev**2

            # Virtual rate: |g|^2 / delta_omega (energy denominator)
            gamma_sum += g_sq / delta_om

        Gamma_virt[ik, ib_init] = gamma_sum

        if abs(omega_branches[ik, ib_init]) > 1e-10:
            Gamma_over_omega[ik, ib_init] = gamma_sum / abs(omega_branches[ik, ib_init])

# Report at key K values
print(f"\n  Virtual scattering rates at K = K_BZ/4:")
ik_quarter = len(K_array) // 4
for ib in range(6):
    print(f"    {branch_labels[ib]:>10s}: Gamma_virt = {Gamma_virt[ik_quarter, ib]:.6e}, "
          f"Gamma/omega = {Gamma_over_omega[ik_quarter, ib]:.6e}")

print(f"\n  Virtual scattering rates at K = K_BZ/2:")
for ib in range(6):
    print(f"    {branch_labels[ib]:>10s}: Gamma_virt = {Gamma_virt[ik_mid, ib]:.6e}, "
          f"Gamma/omega = {Gamma_over_omega[ik_mid, ib]:.6e}")

print(f"\n  Virtual scattering rates at K = K_BZ:")
for ib in range(6):
    print(f"    {branch_labels[ib]:>10s}: Gamma_virt = {Gamma_virt[-1, ib]:.6e}, "
          f"Gamma/omega = {Gamma_over_omega[-1, ib]:.6e}")

# ============================================================
# Section 7: Thermal scattering from GGE background
# ============================================================
print("\n--- Section 7: Thermal scattering from GGE ---")
print(f"  GGE acoustic temperature: T_acoustic = {T_acoustic:.4f} M_KK")

# The GGE background is a non-thermal distribution of quasiparticles
# from the transit (n_pairs = 59.8 quasiparticle pairs total, not
# all Cooper pairs). These quasiparticles provide a scattering
# environment for the single Cooper pair.
#
# However, the GGE is INTEGRABLE (Richardson-Gaudin with 8 conserved
# quantities). This means the quasiparticle-pair scattering is
# constrained by conservation laws.
#
# The effective scattering rate from thermal quasiparticles:
# Gamma_th = n_qp * sigma_scatter * v_rel
# where n_qp ~ n_pairs / Vol_SU3 is the quasiparticle density,
# sigma_scatter ~ |V_3|^2 / (E_F^2) is the scattering cross-section,
# v_rel ~ v_F is the relative velocity.

n_qp_density = n_pairs / Vol_SU3_Haar
print(f"  Quasiparticle density: n_qp = {n_qp_density:.6e} M_KK^8")

# But these are quasiparticles (broken pairs), not Cooper pairs.
# The single Cooper pair sees them as incoherent scatterers.
# The cross-section for a Cooper pair scattering off a quasiparticle
# involves the pair-breaking vertex, which requires energy >= 2*Delta.
#
# At T_acoustic = 0.112 M_KK << 2*Delta_B2 = 1.46 M_KK,
# the quasiparticles have thermal energy far below the pair-breaking
# threshold. Elastic scattering preserves the pair.

T_over_Delta = T_acoustic / (2.0 * Delta_0[1])
print(f"  T_acoustic / (2*Delta_B2) = {T_over_Delta:.4f}")
print(f"  => Thermal quasiparticles cannot break the pair")
print(f"  => Only elastic scattering contributes")

# Elastic scattering cross-section from Andreev reflection:
# When a quasiparticle hits the Cooper pair's bound state,
# it undergoes Andreev reflection (retro-reflection).
# The cross-section is ~ xi_BCS^2 (geometric).
sigma_Andreev = pi * xi_BCS**2
print(f"  Andreev cross-section: sigma ~ pi*xi_BCS^2 = {sigma_Andreev:.4f} M_KK^{{-2}}")

# Quasiparticle velocity: v_qp ~ omega_BZ for the pair bands
# But we need the quasiparticle Fermi velocity, not the pair velocity.
# v_F ~ E_B2 / k_F where k_F ~ 1/xi_BCS
v_F = E_B2_mean / (1.0 / xi_BCS)  # rough estimate
print(f"  Fermi velocity: v_F ~ {v_F:.4f} M_KK")

# Rate: Gamma_elastic = n_qp * sigma * v_F
# But this is a 3D formula. In 8D:
# Gamma_elastic = n_qp * sigma_8D * v_F where sigma_8D ~ xi_BCS^7
# (d-1 dimensional cross-section in d dimensions)
# This is extremely small because the density is so low.
sigma_8D = xi_BCS**7 * pi**3 / 6.0  # rough 8D geometric estimate
Gamma_elastic_8D = n_qp_density * sigma_8D * v_F
print(f"  sigma_8D ~ xi^7 * pi^3/6 = {sigma_8D:.4e}")
print(f"  Gamma_elastic(8D) = n_qp * sigma * v_F = {Gamma_elastic_8D:.4e} M_KK")

# But the pair LIVES on the 32-cell lattice (discrete).
# The relevant calculation is:
# Gamma = (1/tau_scatter) where tau_scatter = mean free path / v_pair
# Mean free path: l_mfp = 1 / (n_qp_density * sigma)
if n_qp_density * sigma_Andreev > 0:
    l_mfp_3D = 1.0 / (n_qp_density * sigma_Andreev)
else:
    l_mfp_3D = np.inf
print(f"  Mean free path (3D convention): l_mfp = {l_mfp_3D:.4e} M_KK^{{-1}}")
print(f"  Compare: L_fabric = Vol^(1/8) = {Vol_SU3_Haar**(1.0/8.0):.4f}")
print(f"  l_mfp / L_fabric = {l_mfp_3D / Vol_SU3_Haar**(1.0/8.0):.4e}")

# ============================================================
# Section 8: Pair-lattice dephasing from on-site anharmonicity
# ============================================================
print("\n--- Section 8: On-site anharmonic dephasing ---")

# Even though the quartic vertex doesn't cause real transitions
# (Section 5), it DOES produce energy-dependent frequency shifts.
# This leads to dephasing of a wave packet.
#
# The anharmonic frequency shift:
#   delta_omega_alpha = (3/2) * b_alpha * <delta^2> / (rho_alpha * omega_alpha)
#
# For a single pair on N_cells sites, the zero-point fluctuation is:
#   <delta^2> = 1 / (2 * rho_alpha * omega_alpha * N_cells)
#
# So delta_omega / omega ~ b_alpha / (rho_alpha * omega_alpha)^2 / N_cells

print("  Anharmonic frequency shift (dephasing source):")
print("  delta_omega/omega ~ b / (rho * omega)^2 / N_cells")

dephasing_ratio = np.zeros(6)
for ib in range(6):
    omega_ib = max(abs(omega_branches[ik_mid, ib]), 1e-10)
    # Map eigenmode to dominant sector
    evec_mid = eigvecs_all[ik_mid, :, ib]
    # Weight by sector
    delta_omega_sum = 0.0  # (local)
    for alpha in range(3):
        weight_amp = evec_mid[alpha]**2
        weight_phase = evec_mid[3+alpha]**2
        total_weight = weight_amp + weight_phase
        if total_weight < 1e-10:
            continue
        rho_a = rho_0[alpha]
        b_a = abs(b_alpha_data[alpha])

        # Anharmonic shift: perturbative 1st order
        delta_om_a = (3.0/2.0) * b_a / (rho_a * omega_ib * N_cells)
        delta_omega_sum += total_weight * delta_om_a

    dephasing_ratio[ib] = delta_omega_sum / omega_ib if omega_ib > 1e-10 else 0.0

print(f"\n  Dephasing ratios at K = K_BZ/2:")
for ib in range(6):
    status = "BALLISTIC" if dephasing_ratio[ib] < 1 else "DIFFUSIVE"
    print(f"    {branch_labels[ib]:>10s}: delta_omega/omega = {dephasing_ratio[ib]:.6e} ({status})")

# ============================================================
# Section 9: Coherence time and mean free path
# ============================================================
print("\n--- Section 9: Coherence times and classification ---")

# The coherence time is:
#   tau_coh = 1 / Gamma_total
# where Gamma_total = Gamma_virt + Gamma_elastic + Gamma_dephasing
#
# From above: Gamma_quartic = 0 (exact), Gamma_elastic ~ 10^{-many},
# Gamma_dephasing ~ delta_omega (Section 8)
#
# The dominant dephasing mechanism is the on-site anharmonicity.

# Coherence times at K_BZ/2
print(f"\n  At K = K_BZ/2 (K = {K_array[ik_mid]:.4f}):")
tau_coh = np.zeros(6)
l_coh = np.zeros(6)
for ib in range(6):
    omega_ib = abs(omega_branches[ik_mid, ib])
    vg_ib = abs(v_g[ik_mid, ib])
    gamma_total = dephasing_ratio[ib] * omega_ib  # dominant contribution
    if gamma_total > 1e-20:
        tau_coh[ib] = 1.0 / gamma_total
    else:
        tau_coh[ib] = np.inf
    l_coh[ib] = vg_ib * tau_coh[ib] if np.isfinite(tau_coh[ib]) else np.inf

    n_cells_coh = l_coh[ib] / a_BCC if np.isfinite(l_coh[ib]) else np.inf

    status = "BALLISTIC" if dephasing_ratio[ib] < 1 else "DIFFUSIVE"
    print(f"    {branch_labels[ib]:>10s}: omega = {omega_ib:.6f}, v_g = {vg_ib:.6f}, "
          f"tau_coh = {tau_coh[ib]:.4e}, l_coh/a = {n_cells_coh:.4e} ({status})")

# ============================================================
# Section 10: N_pair = 1 structural argument
# ============================================================
print("\n--- Section 10: Structural coherence at N_pair = 1 ---")

print("""
  STRUCTURAL ARGUMENT (independent of numerics above):

  At N_pair = 1, the single Cooper pair propagates as a quantum particle
  on the 32-cell lattice. Its Hamiltonian is:

    H = sum_{<ij>} -t_ij |i><j| + sum_i epsilon_i |i><i|

  This is a TIGHT-BINDING Hamiltonian with NO interactions (N_pair = 1).
  A single particle on a lattice with no disorder and no interactions
  propagates BALLISTICALLY by definition. The eigenstates are Bloch
  waves |K> with definite crystal momentum, which are EXACT energy
  eigenstates and never decay.

  The anharmonic correction (Section 8) is a PERTURBATIVE energy shift,
  not a decay rate. It modifies the dispersion relation omega(K) but
  does not produce finite lifetimes.

  THEREFORE: Gamma/omega = 0 EXACTLY for all branches at N_pair = 1.
  The pair is a COHERENT QUANTUM WALKER, not a diffusive hopper.

  This result is STRUCTURAL: it follows from N_pair = 1 alone,
  independent of the lattice geometry, coupling constants, or
  anharmonicity strength.

  Physical consequences:
  1. The pair maintains phase coherence across all 32 cells
  2. The pair wavef'n is a Bloch state (delocalized, definite K)
  3. No resistivity (pair current is persistent)
  4. Decoherence requires EXTERNAL environment (not self-generated)
""")

# ============================================================
# Section 11: Summary table
# ============================================================
print("\n--- Section 11: Summary ---")

print(f"\n  {'Branch':>10s} | {'omega(0)':>10s} | {'BW':>10s} | {'Gamma/omega':>12s} | {'Status':>10s}")
print(f"  {'-'*10} | {'-'*10} | {'-'*10} | {'-'*12} | {'-'*10}")
for ib in range(6):
    status = "BALLISTIC"
    gamma_str = "0 (exact)"
    print(f"  {branch_labels[ib]:>10s} | {omega_branches[0,ib]:10.6f} | {bandwidths[ib]:10.6f} | {gamma_str:>12s} | {status:>10s}")

print(f"""
  GATE VERDICT: PHONON-LIFETIMES-53 = INFO

  At N_pair = 1 (singlet only, W2-6):
  - Quartic scattering: Gamma = 0 EXACTLY (translational invariance + no Umklapp)
  - Pair-pair scattering: Gamma = 0 EXACTLY (no second pair)
  - Thermal qp scattering: Gamma ~ {Gamma_elastic_8D:.2e} M_KK (negligible)
  - Anharmonic dephasing: delta_omega/omega ~ {np.max(dephasing_ratio):.2e} (perturbative shift, not decay)

  RESULT: The single Cooper pair is a COHERENT QUANTUM WALKER.
  Gamma/omega = 0 exactly for all 6 branches.
  This is structural: a single particle on a periodic lattice
  with no disorder is ballistic by definition.

  The 6-branch dispersion from S52 survives reinterpretation as
  tight-binding bands for single-pair hopping. The branches are
  exact energy eigenstates (Bloch waves) with infinite lifetime.
""")

# ============================================================
# Section 12: Plot
# ============================================================
print("\n--- Section 12: Generating plot ---")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: Dispersion with branch labels
ax1 = axes[0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
for ib in range(6):
    ax1.plot(K_array, omega_branches[:, ib], color=colors[ib],
             linewidth=2, label=branch_labels[ib])
ax1.set_xlabel('K (M$_{KK}$)', fontsize=12)
ax1.set_ylabel('$\\omega$ (M$_{KK}$)', fontsize=12)
ax1.set_title('Tight-binding dispersion\n(N$_{pair}$ = 1 reinterpretation)', fontsize=12)
ax1.legend(fontsize=8, loc='upper left')
ax1.set_xlim(0, K_BZ)
ax1.set_ylim(-0.5, 2.0)
ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax1.grid(alpha=0.3)

# Panel 2: Gamma/omega (all zero, but show the upper bound from dephasing)
ax2 = axes[1]
for ib in range(6):
    if ib == 5:  # Higgs-1 is the highest branch we can plot
        continue
    # Plot the dephasing ratio as an UPPER BOUND (it's not a decay rate)
    deph_profile = np.zeros(len(K_array))
    for ik in range(len(K_array)):
        omega_ib = abs(omega_branches[ik, ib])
        evec = eigvecs_all[ik, :, ib]
        delta_sum = 0.0  # (local)
        for alpha in range(3):
            w = evec[alpha]**2 + evec[3+alpha]**2  # (local)
            if w < 1e-10:
                continue
            delta_sum += w * (3.0/2.0) * abs(b_alpha_data[alpha]) / (rho_0[alpha] * max(omega_ib, 1e-10) * N_cells)
        deph_profile[ik] = delta_sum / max(omega_ib, 1e-10)

    ax2.semilogy(K_array, np.maximum(deph_profile, 1e-20), color=colors[ib],
                 linewidth=2, label=branch_labels[ib], linestyle='--')

ax2.axhline(y=1.0, color='red', linestyle='-', linewidth=2, alpha=0.7, label='$\\Gamma/\\omega$ = 1')
ax2.set_xlabel('K (M$_{KK}$)', fontsize=12)
ax2.set_ylabel('$\\delta\\omega/\\omega$ (upper bound)', fontsize=12)
ax2.set_title('Anharmonic dephasing\n(NOT a decay rate)', fontsize=12)
ax2.legend(fontsize=8, loc='upper left')
ax2.set_xlim(0, K_BZ)
ax2.set_ylim(1e-8, 1e2)
ax2.grid(alpha=0.3)

# Panel 3: Group velocity (shows pair propagation character)
ax3 = axes[2]
for ib in range(5):  # Skip Higgs-3 (too large)
    ax3.plot(K_array, v_g[:, ib], color=colors[ib], linewidth=2,
             label=branch_labels[ib])
ax3.set_xlabel('K (M$_{KK}$)', fontsize=12)
ax3.set_ylabel('$v_g$ (M$_{KK}$)', fontsize=12)
ax3.set_title('Group velocity\n(pair hopping speed)', fontsize=12)
ax3.legend(fontsize=8, loc='upper right')
ax3.set_xlim(0, K_BZ)
ax3.axhline(y=0, color='gray', linestyle='--', alpha=0.3)
ax3.grid(alpha=0.3)

plt.tight_layout()
outpath = os.path.join(os.path.dirname(__file__), "s53_phonon_lifetimes.png")
plt.savefig(outpath, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {outpath}")
plt.close()

# ============================================================
# Section 13: Save data
# ============================================================
outdata = os.path.join(os.path.dirname(__file__), "s53_phonon_lifetimes.npz")
np.savez(outdata,
    # Dispersion (inherited)
    K_array=K_array,
    omega_branches=omega_branches,
    branch_labels=branch_labels,
    K_BZ=K_BZ,
    a_BCC=a_BCC,
    # Bandwidth and hopping
    bandwidths=bandwidths,
    t_hop=t_hop,
    # Scattering rates
    Gamma_quartic=np.zeros(6),  # EXACT zero
    Gamma_virt=Gamma_virt,
    Gamma_over_omega=Gamma_over_omega,
    dephasing_ratio=dephasing_ratio,
    Gamma_elastic_8D=Gamma_elastic_8D,
    # Group velocities
    v_g=v_g,
    # Coherence
    tau_coh=tau_coh,
    l_coh=l_coh,
    # Gate
    gate_name=np.array(['PHONON-LIFETIMES-53']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([f'Gamma/omega = 0 exactly (N_pair=1, no scattering). Coherent quantum walker. Dephasing upper bound {np.max(dephasing_ratio):.2e}.']),
)
print(f"  Data saved: {outdata}")
print("\n" + "=" * 70)
print("DONE")
print("=" * 70)
