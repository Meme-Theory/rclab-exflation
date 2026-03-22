"""
S44 N3-BDG-44: N_3 Topological Invariant for BdG Spectrum
==========================================================

Computes the N_3 topological invariant (Volovik, Paper 04) for the BdG
Hamiltonian at the fold (tau=0.2) and across the transit.

The N_3 invariant classifies topologically protected point nodes (Fermi points)
in the quasiparticle spectrum. Near a Fermi point with N_3 != 0, vacuum energy
is EXACTLY zero by topological protection.

Gate: N3-BDG-44
  PASS: N_3 != 0 found (topological CC suppression applies)
  FAIL: No point nodes or all N_3 = 0 (no topological protection)
  INFO: Nodes found but N_3 computation ambiguous

Physical setup:
  - BdG Hamiltonian H_BdG = [[h - mu, Delta], [Delta^dag, -(h-mu)^T]]
  - h = D_K eigenvalues (1232 modes, 10 sectors at tau=0.2)
  - mu = 0 (S34: PH symmetry forces mu=0)
  - Delta from BCS gap (S38: Delta_0 = 0.770)
  - BDI symmetry class (T^2=+1, S17c)

Key question: does the BdG spectrum have conical intersections
(Weyl/Dirac points) with nontrivial N_3?
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# STEP 1: Load data
# ============================================================
print("=" * 70)
print("N3-BDG-44: Topological Invariant for BdG Spectrum")
print("=" * 70)

d38 = np.load('tier0-computation/s38_cc_instanton.npz', allow_pickle=True)
d35 = np.load('tier0-computation/s35_ed_corrected_dos.npz', allow_pickle=True)
d22 = np.load('tier0-computation/s22b_eigenvectors.npz', allow_pickle=True)
d42 = np.load('tier0-computation/s42_hauser_feshbach.npz', allow_pickle=True)

# BCS parameters
Delta_0 = float(d38['Delta_0'])  # 0.770
xi_fold = d38['xi_fold']          # [0.819, 0.845, 0.978]
mult_k = d38['mult_k']            # [1, 4, 3]
tau_values = d22['tau_values']     # [0, 0.1, ..., 0.5]

# ED results
V_bare = d35['V_5x5_bare']
E_cond = float(d35['scenario_A_E_cond'])
pair_occ = d35['scenario_A_pair_occ']

print(f"\nBCS gap: Delta_0 = {Delta_0:.6f}")
print(f"Gap-edge levels: xi = {xi_fold}")
print(f"Multiplicities: m = {mult_k}")
print(f"Condensation energy: E_cond = {E_cond:.6f}")
print(f"Pair occupations: {pair_occ}")

# ============================================================
# STEP 2: Construct BdG Hamiltonian
# ============================================================
print("\n" + "=" * 70)
print("STEP 2: BdG Hamiltonian Construction")
print("=" * 70)

# The BCS pairing occurs in the B2=(0,0) sector, which has 16 eigenvalues
# that come in +/- pairs: +/-0.819 (x1), +/-0.845 (x4), +/-0.978 (x3)
# Total: 8 positive + 8 negative = 16

# Standard BdG: for each single-particle state |k> with energy epsilon_k,
# H_BdG = [[epsilon_k, Delta_k], [Delta_k*, -epsilon_k]]  (2x2 per level)
# Quasiparticle energy: E_k = sqrt(epsilon_k^2 + |Delta_k|^2)

# For our BCS on SU(3): the 5 pairing levels have energies E_5
E_5 = d35['E_5']
print(f"5 pairing levels: {E_5}")

# The BdG gap function Delta_k for each level comes from the
# self-consistent BCS solution. From the pair occupations and V matrix:
# Delta_k = sum_l V_{kl} * sqrt(v_l * (1-v_l))
# where v_k = pair occupation probability

# Compute BCS gap for each level
v_k = pair_occ
u_k = 1.0 - v_k  # hole amplitudes (using notation: v_k = |v_k|^2)
# In BCS: <c_{-k} c_k> = sqrt(v_k * u_k) * exp(i*phase)
# Delta_k = -sum_l V_{kl} * sqrt(v_l * u_l)
anomalous = np.sqrt(v_k * u_k)  # |<c_{-k} c_k>|
print(f"\nAnomalous amplitudes: {anomalous}")

Delta_k = -V_bare @ anomalous
print(f"Gap function Delta_k: {Delta_k}")
print(f"|Delta_k|: {np.abs(Delta_k)}")

# BdG quasiparticle energies for the 5 pairing levels (mu=0)
E_BdG = np.sqrt(E_5**2 + Delta_k**2)
print(f"\nBdG quasiparticle energies: {E_BdG}")
print(f"Minimum BdG energy: {np.min(E_BdG):.6f}")
print(f"Maximum BdG energy: {np.max(E_BdG):.6f}")

# ============================================================
# STEP 3: Full B2 sector BdG Hamiltonian (8 levels)
# ============================================================
print("\n" + "=" * 70)
print("STEP 3: Full B2 Sector BdG (8 levels)")
print("=" * 70)

# The 8 positive eigenvalues in B2 at fold:
# Level 1: xi_1 = 0.81914 (mult 1) -- this is the "B1-like" level (Trap 1: V=0)
# Level 2: xi_2 = 0.84527 (mult 4)
# Level 3: xi_3 = 0.97822 (mult 3)

# The 5-level ED used levels: 4 at xi_2 + 1 at xi_1
# Level 3 (xi_3) was excluded because it's higher energy
# But for N_3 analysis, we need ALL levels

# For the full 8-level BdG: H_BdG is 16x16
# [[diag(xi_k), Delta_matrix], [Delta_matrix^dag, -diag(xi_k)]]
# Since mu=0

n_levels = 8  # total pairing levels in B2
xi_all = np.array([0.81914] * 1 + [0.84527] * 4 + [0.97822] * 3)
print(f"All 8 xi levels: {xi_all}")

# Construct the gap matrix
# For the 5 paired levels, Delta comes from V_bare
# For the 3 levels at xi_3=0.978, these are above the pairing window
# Trap 1: V(B1,B1)=0 exactly (level 5 = xi_1=0.819 has V_55 ~ 0)
# V(B2,B3) = small but nonzero

# Extended gap function for all 8 levels:
# Levels 1-5 (the ED levels): Delta from computation above
# Levels 6-8 (xi_3=0.978): these are the B3=(1,1) contribution
#   From Trap 1 analysis and V matrix: V(B2,B3) is the off-diagonal
#   But within B2 only: the 3 modes at xi_3 have NO pairing coupling
#   because they're above the pairing cutoff in the ED

# The CRITICAL observation: in the framework's BCS,
# pairing only occurs between degenerate partners (+xi, -xi)
# The gap function Delta_k is nonzero only for the 5 levels in the ED

Delta_all = np.zeros(8)
Delta_all[0] = Delta_k[4]  # xi_1 level: corresponds to E_5[4] = 0.81914
Delta_all[1:5] = Delta_k[0:4]  # xi_2 levels: correspond to E_5[0:4]
# Delta_all[5:8] = 0  # xi_3 levels: above pairing window

print(f"\nGap function for all 8 levels:")
for i in range(8):
    print(f"  Level {i+1}: xi={xi_all[i]:.5f}, Delta={Delta_all[i]:.6f}")

# Construct full 16x16 BdG Hamiltonian
H_BdG_full = np.zeros((16, 16))
H_BdG_full[:8, :8] = np.diag(xi_all)  # particle block
H_BdG_full[8:, 8:] = -np.diag(xi_all)  # hole block
H_BdG_full[:8, 8:] = np.diag(Delta_all)  # pairing
H_BdG_full[8:, :8] = np.diag(Delta_all)  # pairing (real gap)

E_BdG_full = np.linalg.eigvalsh(H_BdG_full)
print(f"\nFull 16x16 BdG eigenvalues: {np.sort(E_BdG_full)}")
print(f"Min |E_BdG|: {np.min(np.abs(E_BdG_full)):.6f}")

# ============================================================
# STEP 4: Search for Point Nodes
# ============================================================
print("\n" + "=" * 70)
print("STEP 4: Point Node Search")
print("=" * 70)

# In standard condensed matter: N_3 is defined for a Hamiltonian H(k)
# where k is a continuous 3D momentum. Point nodes are where E(k)=0.
#
# In our system: the single-particle spectrum is DISCRETE (Peter-Weyl modes
# on SU(3)). There is NO continuous 3D momentum k. The spectrum labels
# are (p,q) representation indices, which are integers.
#
# However, we can define an EFFECTIVE continuous parameter space
# by promoting tau (Jensen deformation) and the BCS gap Delta to
# continuous variables. This gives us a 2D parameter space (tau, Delta/Delta_0).
# For N_3 we need a 3D parameter space -- we add the chemical potential mu.
#
# The BdG Hamiltonian H_BdG(tau, mu, Delta) is then a function of 3 continuous
# parameters, and we can search for zeros of det(H_BdG) = 0.

# For each level k:
# E_k(tau, mu, Delta) = sqrt((xi_k(tau) - mu)^2 + Delta_k(Delta)^2)
# This is zero iff xi_k(tau) = mu AND Delta_k = 0

# ANALYSIS 1: At fixed Delta = Delta_0, varying tau and mu
# E_k = 0 requires xi_k(tau) = mu AND Delta_k = 0
# Delta_k = 0 only for the 3 unpaired levels (xi_3 = 0.978 at fold)
# So we need xi_3(tau) = mu -- this gives nodes at (tau*, mu* = xi_3(tau*))

print("\n--- Analysis 1: Unpaired levels (Delta_k = 0) ---")
print("Levels 6-8 have Delta_k = 0 (above pairing cutoff).")
print("These are ordinary Fermi-surface states, not Fermi points.")
print("E_k = |xi_k - mu|. Zero when mu = xi_k(tau).")
print("This is a Fermi SURFACE (co-dim 1 in 3D, line in 2D parameter space).")
print("Topological class: Fermi surface, not Fermi point. N_1 invariant, not N_3.")

# ANALYSIS 2: BdG spectrum as function of continuous parameter tau
# For all 8 levels at each tau:
print("\n--- Analysis 2: BdG spectrum vs tau (at mu=0) ---")

n_tau = len(tau_values)
E_BdG_vs_tau = np.zeros((n_tau, 16))

# Track level structure
xi_vs_tau = np.zeros((n_tau, 3))  # 3 distinct eigenvalue magnitudes

for i, tau in enumerate(tau_values):
    evals_i = d22[f'eigenvalues_{i}']
    sp_i = d22[f'sector_p_{i}']
    sq_i = d22[f'sector_q_{i}']
    mask = (sp_i == 0) & (sq_i == 0)
    e_B2 = np.sort(evals_i[mask])

    # Get 3 distinct positive eigenvalues
    pos_evals = np.sort(e_B2[e_B2 > 0])
    unique_pos = np.unique(np.round(pos_evals, 8))
    xi_vs_tau[i, :len(unique_pos)] = unique_pos[:3]

    # Construct BdG at this tau
    xi_tau = np.zeros(8)
    xi_tau[0] = unique_pos[0]  # smallest (B1-like)
    xi_tau[1:5] = unique_pos[1] if len(unique_pos) > 1 else unique_pos[0]
    xi_tau[5:8] = unique_pos[2] if len(unique_pos) > 2 else unique_pos[-1]

    # At tau=0: all degenerate (0.866)
    # At tau>0: splits into 3 levels

    # Use same gap structure (self-consistent would change, but topology
    # is about whether nodes exist, not exact energies)
    Delta_tau = np.zeros(8)
    Delta_tau[0] = Delta_k[4]
    Delta_tau[1:5] = Delta_k[0:4]
    # Delta_tau[5:8] = 0  # unpaired

    H = np.zeros((16, 16))
    H[:8, :8] = np.diag(xi_tau)
    H[8:, 8:] = -np.diag(xi_tau)
    H[:8, 8:] = np.diag(Delta_tau)
    H[8:, :8] = np.diag(Delta_tau)

    E_BdG_vs_tau[i] = np.sort(np.linalg.eigvalsh(H))

# Check for zero crossings
for i, tau in enumerate(tau_values):
    min_abs_E = np.min(np.abs(E_BdG_vs_tau[i]))
    print(f"  tau={tau:.2f}: min|E_BdG| = {min_abs_E:.6f}")

# ============================================================
# STEP 5: N_3 Invariant Computation
# ============================================================
print("\n" + "=" * 70)
print("STEP 5: N_3 Invariant Analysis")
print("=" * 70)

# The N_3 invariant (Paper 04, eq. in Section on Momentum-Space Topology):
# N_3 = (1/24pi^2) * epsilon^{ijk} * integral_S2 tr[G dG^{-1} . G dG^{-1} . G dG^{-1}] dS
#
# where G(omega, k) = [i*omega - H_BdG(k)]^{-1} is the Green's function.
#
# For a 2x2 BdG block (single level):
# H_k = tau_3 * xi_k + tau_1 * Delta_k  (tau_i are Pauli in PH space)
# G^{-1} = i*omega - tau_3 * xi_k - tau_1 * Delta_k
#
# The N_3 invariant for a single Fermi point in 3D:
# N_3 = (1/2) * sign(d_xi/dk) * sign(Delta)  for a linear crossing
#
# CRITICAL DIMENSIONAL ANALYSIS:
# N_3 is defined for systems with 3 continuous momenta (3D systems).
# Our system has DISCRETE modes labeled by (p,q) representations.
# The representation space is 2D (p,q), not 3D.
#
# The N_3 invariant is UNDEFINED for our system because:
# 1. The Brillouin zone is DISCRETE (finite set of Peter-Weyl modes)
# 2. Even if we embed in a continuous space, it's 2D not 3D
# 3. The BCS gap opens at ALL paired levels (Delta_k != 0 for levels 1-5)
# 4. The unpaired levels (6-8) have Fermi SURFACES, not Fermi POINTS

print("\n--- DIMENSIONAL ANALYSIS ---")
print("N_3 requires 3 continuous momentum dimensions.")
print("Framework representation space: (p,q) in Z^2 (discrete, 2D).")
print("Even promoted to continuous: 2D Brillouin zone, not 3D.")
print("N_3 is STRUCTURALLY INAPPLICABLE.")

# But: can we define an EFFECTIVE 3D parameter space?
# (tau, mu, theta) where theta parameterizes U(1)_7 phase of order parameter
#
# H_BdG(tau, mu, theta) = [[diag(xi(tau)) - mu*I, e^{i*theta} * diag(Delta)],
#                           [e^{-i*theta} * diag(Delta), -(diag(xi(tau)) - mu*I)]]
#
# Nodes require: xi_k(tau) = mu AND Delta_k = 0
# For unpaired levels: Delta_k = 0 always, so node when xi_k(tau) = mu
# For paired levels: Delta_k != 0, so NO nodes regardless of mu and tau

print("\n--- EXTENDED PARAMETER SPACE (tau, mu, theta) ---")
print("Promoting to 3D parameter space (tau, mu, theta):")

# Compute the node locus in (tau, mu) space for unpaired levels
print("\nNode loci for UNPAIRED levels (Delta_k = 0):")
print("These exist at mu = xi_k(tau) for levels 6-8 (the xi_3 levels).")
for i, tau in enumerate(tau_values):
    print(f"  tau={tau:.2f}: node at mu = {xi_vs_tau[i, 2]:.6f} (xi_3)")

# For unpaired levels with Delta=0, the 2x2 BdG block is:
# H = [[xi - mu, 0], [0, -(xi - mu)]]
# Eigenvalues: +/-(xi - mu)
# At the node (xi = mu): both eigenvalues = 0
# The dispersion near the node:
#   E = +/- sqrt((d_xi/d_tau * delta_tau)^2 + (delta_mu)^2)
# This is LINEAR (conical) in (delta_tau, delta_mu) -- looks like a Weyl point!
# But the third direction (theta) does NOT enter because Delta=0

print("\n--- TOPOLOGY OF UNPAIRED-LEVEL NODES ---")
print("At node (tau*, mu = xi_3(tau*)), the 2x2 BdG block:")
print("  H = [[ xi-mu, 0 ], [ 0, -(xi-mu) ]]")
print("Near node: E = +/- |xi-mu| -- linear but 1D, not conical.")
print("This is a particle-hole crossing with ZERO off-diagonal coupling.")
print("The crossing is NOT gapped because Delta = 0 (unpaired).")
print("Topological classification: this is a FERMI SURFACE in (tau, mu, theta)")
print("co-dimension 1 (the theta direction is flat), not co-dimension 3 (Fermi point).")

# ============================================================
# STEP 5b: Correct topological invariant for our system
# ============================================================
print("\n" + "=" * 70)
print("STEP 5b: Correct Topological Classification")
print("=" * 70)

# For a DISCRETE spectrum with particle-hole symmetry (BDI class):
# The relevant topological invariant is NOT N_3 (Fermi point in 3D)
# but rather:
#
# 1. The Z-valued invariant for 0D BDI systems (class BDI, d=0):
#    This is the winding number of the BCS gap function.
#    From the periodic table: BDI in d=0 is Z.
#
# 2. The Pfaffian Z_2 invariant (already computed S17c, S35)
#    sgn(Pf) = -1 at all 34 tau values tested
#
# 3. The spectral gap: the BdG spectrum is fully gapped when Delta != 0
#    for ALL levels. Currently 3 unpaired levels BREAK the full gap.

# Compute the BDI invariant (d=0)
print("\n--- BDI Classification (d=0) ---")

# For BDI in d=0, the topological invariant is:
# nu = (1/2)(N_+ - N_-) where N_+/- count positive/negative eigenvalues of H_BdG
# OR equivalently: the number of occupied negative-energy states

# At the fold:
E_sorted = np.sort(E_BdG_full)
n_negative = np.sum(E_sorted < 0)
n_positive = np.sum(E_sorted > 0)
n_zero = np.sum(np.abs(E_sorted) < 1e-10)
print(f"BdG eigenvalues at fold:")
print(f"  N_negative = {n_negative}, N_positive = {n_positive}, N_zero = {n_zero}")
print(f"  nu_BDI = (N+ - N-)/2 = {(n_positive - n_negative)//2}")

# Actually for BDI class, the invariant is the winding number W:
# W = (1/2pi) integral_0^{2pi} d[arg(det(q(k)))] dk
# where q(k) is the off-diagonal block of H in the chiral basis
# But our system is 0D (no k-dependence), so W is just a count

# The PH operator C maps: C H C^{-1} = -H
# For BDI: C = tau_1 * K (complex conjugation)
# The chiral operator: S = T * C where T is time-reversal (T = K for spinless)
# S = tau_1 maps H_BdG -> -H_BdG (chiral symmetry for real H)

# In chiral basis: H = [[0, D], [D^T, 0]] where D is the off-diagonal block
# D = diag(xi_1+Delta_1, xi_2+Delta_2, ...) for the specific form of our H_BdG
# Wait -- need to transform to chiral basis

# For H_BdG = [[h, Delta], [Delta, -h]] with h=diag(xi), Delta=diag(Delta_k):
# Chiral operator S = [[0, I], [I, 0]]
# In eigenbasis of S: rotate by U = (1/sqrt(2)) [[I, I], [I, -I]]
# H_chiral = U^dag H_BdG U = [[0, h+Delta], [h+Delta, 0]]  -- NO, need to check

# Let me just compute the spectrum gap and characterize the node structure
print("\n--- Spectral Gap Analysis ---")
print("The BdG spectrum has two types of states:")
print()

for k in range(8):
    if k == 0:
        label = "B1-like (xi=0.819, Trap 1)"
    elif k < 5:
        label = f"B2-core (xi=0.845, paired)"
    else:
        label = f"B3-like (xi=0.978, unpaired)"

    E_qp = np.sqrt(xi_all[k]**2 + Delta_all[k]**2)
    gap = 2 * min(E_qp, abs(xi_all[k]))
    if abs(Delta_all[k]) < 1e-10:
        node_type = "GAPLESS (Delta=0, Fermi surface)"
    else:
        node_type = f"GAPPED (gap = {2*E_qp:.4f})"

    print(f"  Level {k+1} ({label}): E_qp = {E_qp:.6f}, {node_type}")

# ============================================================
# STEP 5c: N_3 in extended parameter space -- formal computation
# ============================================================
print("\n" + "=" * 70)
print("STEP 5c: N_3 in Extended Parameter Space")
print("=" * 70)

# Even though our system is 0D, we can EMBED it in a 3D parameter space
# and ask: do the BdG Hamiltonian's zeros form isolated points?
# If so, we compute N_3 around each.

# Parameter space: p = (tau, mu, phi) where phi = U(1)_7 phase
# H_BdG(p) = [[diag(xi(tau)) - mu*I, e^{i*phi} Delta], [e^{-i*phi} Delta^*, -diag(xi(tau)) + mu*I]]

# For PAIRED levels (1-5): Delta_k != 0
# det(H_2x2) = -(xi-mu)^2 - |Delta|^2 < 0 always. NO ZEROS.

# For UNPAIRED levels (6-8): Delta_k = 0
# det(H_2x2) = -(xi-mu)^2. Zero when xi(tau) = mu.
# But the 2x2 block is [[xi-mu, 0],[0,-(xi-mu)]].
# The Green's function: G(omega) = [i*omega - H]^{-1}
# G = diag(1/(i*omega - (xi-mu)), 1/(i*omega + (xi-mu)))
# G dG^{-1} requires variation in 3 directions.
# Since Delta=0, the phi direction gives ZERO contribution.
# The integral over S^2 enclosing the node is:
# N_3 = 0 (because one direction is flat -- the manifold is degenerate)

print("For UNPAIRED levels (6-8) at Delta_k = 0:")
print("  Node at (tau*, mu = xi(tau*), any phi).")
print("  The node is a LINE in (tau, mu, phi) space (extended in phi).")
print("  Codimension = 2 (not 3). This is NOT a Fermi point.")
print("  N_3 = 0 by dimensional reduction.")
print()
print("For PAIRED levels (1-5) at Delta_k != 0:")
print("  det(H_2x2) = -(xi-mu)^2 - |Delta|^2 < 0 for all (tau, mu, phi).")
print("  NO nodes exist. N_3 undefined (no Fermi point to enclose).")

# ============================================================
# STEP 5d: Can BCS dynamics CREATE Fermi points?
# ============================================================
print("\n" + "=" * 70)
print("STEP 5d: Dynamical Node Creation During Transit")
print("=" * 70)

# During the transit, the BCS condensate is destroyed (P_exc = 1.000, S38).
# Post-transit: Delta -> 0. ALL levels become unpaired.
# The BdG Hamiltonian becomes: H = [[h, 0], [0, -h]]
# Eigenvalues: +/- xi_k for all k.

# In the GGE relic state: the quasiparticle distribution is non-thermal.
# The relevant spectrum is h = diag(xi_k) with the GGE occupation numbers.
# NO pairing gap. ALL levels are gapless at mu = xi_k.

# But: this is STILL a Fermi surface (1D node in 2D parameter space),
# not a Fermi point (0D node in 3D).

print("During transit: Delta(t) -> 0 (P_exc = 1.000).")
print("Post-transit BdG: H = [[h, 0], [0, -h]], eigenvalues +/- xi_k.")
print("ALL levels become gapless at mu = xi_k.")
print("Node structure: Fermi SURFACE (co-dim 1), not Fermi POINT (co-dim 3).")
print()
print("The fundamental obstruction:")
print("  Fermi points require 3 continuous momentum dimensions.")
print("  Our system has 0 continuous momenta (discrete Peter-Weyl modes).")
print("  Even embedding in (tau, mu, phi): nodes are at most co-dim 2.")
print("  N_3 is STRUCTURALLY ZERO in any embedding.")

# ============================================================
# STEP 5e: Could the FULL 992-mode BdG have inter-sector nodes?
# ============================================================
print("\n" + "=" * 70)
print("STEP 5e: Full 992-mode Inter-sector Analysis")
print("=" * 70)

# The block-diagonal theorem (S22b) guarantees that D_K decomposes into
# independent sectors. BCS pairing is confined to B2=(0,0).
# Inter-sector coupling is ZERO by selection rules.
# Therefore: no inter-sector BdG crossings can create new nodes.

# However: what about WITHIN a single sector with continuous momentum?
# In the physical 4D spacetime: the KK modes ARE the momentum-space structure.
# The SU(3) representation labels (p,q) play the role of discrete lattice momenta.
# For Fermi points, we need the ANALOG of continuous k.

# The closest analog: the eigenvalue spectrum as a function of tau.
# xi_n(tau) are smooth functions. As tau varies, levels can cross.
# The BdG spectrum is:
# E_n(tau, mu) = sqrt((xi_n(tau) - mu)^2 + Delta_n^2)

# For a level crossing: xi_m(tau*) = xi_n(tau*) at some tau*
# Near crossing: the 4x4 BdG block has structure
# H = [[diag(xi_m, xi_n), Delta*I], [Delta*I, -diag(xi_m, xi_n)]]
# eigenvalues: +/- sqrt((xi_m +/- xi_n)^2/4 + Delta^2 + ...)
# This is still gapped by Delta. No nodes.

# Check for level crossings in B2 sector
print("\nB2 eigenvalue crossings vs tau:")
for i in range(n_tau - 1):
    xi_i = xi_vs_tau[i]
    xi_next = xi_vs_tau[i + 1]
    # Check if ordering changes
    if xi_i[0] > xi_i[1] or xi_next[0] > xi_next[1]:
        print(f"  CROSSING between tau={tau_values[i]:.2f} and {tau_values[i+1]:.2f}")
    else:
        gap_12 = abs(xi_i[1] - xi_i[0])
        gap_23 = abs(xi_i[2] - xi_i[1])
        print(f"  tau={tau_values[i]:.2f}: gap_12={gap_12:.4f}, gap_23={gap_23:.4f} -- no crossing")

print(f"  tau={tau_values[-1]:.2f}: final point")

# ============================================================
# STEP 6: Alternative: N_1 Invariant (Fermi Surface)
# ============================================================
print("\n" + "=" * 70)
print("STEP 6: N_1 Fermi Surface Invariant")
print("=" * 70)

# Since our nodes are Fermi surfaces (co-dim 1), the correct invariant is N_1:
# N_1 = (1/2pi*i) oint G dG^{-1} dl
# integrated on a contour encircling the Fermi surface in 1D parameter space.
#
# For a particle-hole crossing at xi = mu with Delta = 0:
# G(omega) = diag(1/(i*omega - xi + mu), 1/(i*omega + xi - mu))
#
# The winding number of each component around omega=0:
# Particle block: N_1 = +1/2 (pole at omega = -i*(xi-mu) -> 0 at node)
# Hole block: N_1 = -1/2 (pole at omega = +i*(xi-mu) -> 0 at node)
# Total: N_1 = 0 (particle-hole cancellation!)

# This is the PH symmetry at work: every Fermi surface node is automatically
# paired with its PH conjugate, giving total N_1 = 0.

# For the PAIRED levels: no nodes exist. N_1 = 0 trivially.

print("N_1 Fermi surface invariant for unpaired levels:")
print("  Each node at xi = mu has N_1 = +1/2 (particle) + (-1/2) (hole) = 0")
print("  PH symmetry enforces EXACT cancellation.")
print("  No topological Fermi surface protection either.")
print()

# ============================================================
# STEP 6b: Pfaffian Z_2 and BDI winding
# ============================================================
print("--- Existing topological invariants ---")
print("BDI class (T^2=+1, C^2=+1, S^2=1):")
print("  d=0: Z invariant (winding number W)")
print("  S35: sgn(Pf) = -1 at all tau (Z_2 nontrivial)")
print("  S38: BDI winding = 0 (post-transit, condensate destroyed)")
print()
print("The BDI Z invariant in d=0 is the number of negative-energy states.")
print(f"  At fold: N_negative = {n_negative} (out of 16)")
print(f"  W = N_negative - N_total/2 = {n_negative - 8}")

# Spectral asymmetry
eta = np.sum(np.sign(E_BdG_full))
print(f"  Spectral asymmetry eta = sum(sign(E_k)) = {eta}")
print(f"  (PH symmetry: eta = 0 is enforced by construction)")

# ============================================================
# STEP 7: Vacuum Energy Analysis
# ============================================================
print("\n" + "=" * 70)
print("STEP 7: Vacuum Energy at Nodes")
print("=" * 70)

# Paper 04 theorem: at a Fermi point with N_3 = +/-1,
# the vacuum energy density rho_Lambda = 0 EXACTLY.
# This is because the spectral asymmetry eta(E_F) = 0 is topologically
# protected at the Fermi point.

# For our system: N_3 = 0 (no Fermi points exist)
# Therefore: the Paper 04 vacuum energy cancellation does NOT apply.

# The vacuum energy for the BdG system is:
# E_vac = (1/2) sum_k E_k(BdG) - (1/2) sum_k |xi_k|
# For paired levels: E_k = sqrt(xi_k^2 + Delta_k^2)
# For unpaired levels: E_k = |xi_k| (unchanged from normal state)

E_vac_BdG = 0.5 * np.sum(np.abs(E_BdG_full))
E_vac_normal = 0.5 * np.sum(np.abs(np.concatenate([xi_all, -xi_all])))  # = sum |xi_k|
E_vac_BdG_minus_normal = E_vac_BdG - E_vac_normal

print(f"BdG vacuum energy: {E_vac_BdG:.6f}")
print(f"Normal-state vacuum energy: {E_vac_normal:.6f}")
print(f"Difference (condensation): {E_vac_BdG_minus_normal:.6f}")
print(f"This is NOT zero (no N_3 protection).")
print()

# For comparison: what WOULD the vacuum energy be if N_3 = 1?
# At a Fermi point: the linear dispersion E ~ v_F |k| gives
# E_vac = integral d^3k E(k) = 0 by the N_3 cancellation
# (positive and negative energy contributions cancel by topology)

# But this requires the continuous-k structure that we lack.

print("Paper 04 vacuum energy cancellation:")
print("  Requires: N_3 != 0 at a Fermi point in 3D momentum space.")
print("  Our system: 0D (discrete modes). N_3 undefined.")
print("  Conclusion: No topological vacuum energy protection.")

# ============================================================
# STEP 8: The Correct Analog
# ============================================================
print("\n" + "=" * 70)
print("STEP 8: The Correct Superfluid Analog")
print("=" * 70)

# In 3He-A: the order parameter has Fermi points with N_3 = +/-2.
# The emergent Weyl fermions near these points give vacuum energy = 0.
# This works because 3He-A has a CONTINUOUS 3D Brillouin zone.
#
# The framework's BCS on SU(3) is CLOSER to:
# - 3He-B (fully gapped, BDI class, topological but no Fermi points)
# - Nuclear BCS (finite number of discrete levels, 0D)
# - Sachdev-Ye-Kitaev model (0D, random couplings)
#
# The flat band (B2, W=0) is analogous to:
# - Flat bands in twisted bilayer graphene (but those are 2D, not 0D)
# - Landau levels (0D in some sense, but with continuous guiding center)
# - Dispersionless bands in pyrochlore/kagome lattices
#
# For vacuum energy in 0D systems:
# The relevant protection is NOT N_3 (wrong dimension)
# but rather the equilibrium theorem (Paper 05):
# In equilibrium, the vacuum energy is the thermodynamic potential Omega,
# which self-tunes to zero by the equation of state.
#
# The GGE relic is NOT in equilibrium, so the equilibrium theorem
# doesn't apply directly. But if the GGE conserved charges include
# a "vacuum charge" q that controls the equation of state,
# then q-theory self-tuning could work per-charge.
# This is the CC-GGE-GIBBS-44 proposal from the CC workshop.

print("3He-A (Fermi point analog): N_3 = +/-2, continuous 3D BZ.")
print("3He-B (full gap analog): BDI class, topological but no N_3.")
print("Framework BCS on SU(3): 0D, BDI class, flat band in B2.")
print()
print("The framework is in the SAME universality class as 3He-B,")
print("NOT 3He-A. The relevant topological invariant is:")
print("  - Pfaffian Z_2 (computed S17c, S35: nontrivial)")
print("  - BDI winding number W (computed S38: W=0 post-transit)")
print("  - NOT N_3 (wrong spatial dimension)")
print()
print("For vacuum energy protection: the correct mechanism is")
print("q-theory (Paper 15-16), not Fermi-point cancellation.")
print("The GGE relic requires generalized Gibbs-Duhem (CC-GGE-GIBBS-44).")

# ============================================================
# STEP 9: Quantitative Summary
# ============================================================
print("\n" + "=" * 70)
print("STEP 9: Gate Verdict")
print("=" * 70)

# Summary of all computed quantities
results = {}

# BdG spectrum
results['E_BdG_fold'] = E_BdG_full
results['E_BdG_vs_tau'] = E_BdG_vs_tau
results['xi_all'] = xi_all
results['Delta_all'] = Delta_all
results['anomalous_amplitudes'] = anomalous

# Node search
results['min_abs_E_BdG_fold'] = np.min(np.abs(E_BdG_full))
results['n_gapless_levels'] = np.sum(np.abs(Delta_all) < 1e-10)
results['n_paired_levels'] = np.sum(np.abs(Delta_all) > 1e-10)

# Topological invariants
results['N_3'] = 0  # No Fermi points: N_3 undefined/zero
results['N_1'] = 0  # PH cancellation
results['eta_spectral'] = eta  # Spectral asymmetry
results['n_negative_BdG'] = n_negative
results['pfaffian_sign'] = -1  # From S17c, S35
results['BDI_winding'] = 0  # From S38 (post-transit)

# Level structure
results['xi_vs_tau'] = xi_vs_tau
results['tau_values'] = tau_values
results['B2_dim'] = 16
results['n_unpaired'] = 3  # The 3 xi_3 modes
results['n_paired'] = 5    # The 5 ED modes

# Why N_3 fails
results['codimension_node'] = 1  # Fermi surface, not Fermi point
results['spatial_dimension'] = 0  # Discrete modes, 0D system
results['N_3_required_dim'] = 3  # N_3 needs 3D continuous BZ
results['correct_class'] = '3He-B (fully gapped BDI)'
results['correct_invariant'] = 'Pfaffian Z_2 or q-theory'

# Vacuum energy
results['E_vac_BdG'] = E_vac_BdG
results['E_vac_normal'] = E_vac_normal
results['E_vac_condensation'] = E_vac_BdG_minus_normal

# Gate verdict
gate_verdict = 'FAIL'
results['gate_verdict'] = gate_verdict

print(f"\nGATE VERDICT: {gate_verdict}")
print()
print("FAIL REASON: No Fermi points exist in the BdG spectrum.")
print("  1. System is 0-dimensional (discrete Peter-Weyl modes on SU(3)).")
print("  2. N_3 requires 3 continuous momentum dimensions -- inapplicable.")
print("  3. 5 paired levels are fully gapped (E_qp > 0.82).")
print("  4. 3 unpaired levels have Fermi surfaces (co-dim 1), not Fermi points (co-dim 3).")
print("  5. PH symmetry gives N_1 = 0 for all Fermi surface nodes.")
print("  6. Spectral asymmetry eta = 0 by PH constraint, not topology.")
print()
print("The framework's BCS on SU(3) is in the universality class of 3He-B")
print("(fully gapped, BDI topological), NOT 3He-A (Fermi point, N_3 = +/-2).")
print()
print("DOWNSTREAM CONSEQUENCES:")
print("  - Paper 04 vacuum energy cancellation does NOT apply.")
print("  - Topological CC protection requires DIFFERENT mechanism.")
print("  - Correct path: q-theory (Paper 15-16) + generalized Gibbs-Duhem.")
print("  - The Pfaffian Z_2 = -1 (from S35) IS nontrivial but does not protect vacuum energy.")
print(f"\nKey numbers:")
print(f"  min|E_BdG| at fold = {results['min_abs_E_BdG_fold']:.6f}")
print(f"  n_paired / n_total = {results['n_paired']}/{results['n_paired'] + results['n_unpaired']}")
print(f"  N_3 = {results['N_3']}")
print(f"  N_1 = {results['N_1']}")
print(f"  eta (spectral asymmetry) = {results['eta_spectral']}")
print(f"  Pfaffian sign = {results['pfaffian_sign']} (from S35, nontrivial)")

# ============================================================
# STEP 10: Save Data
# ============================================================
np.savez('tier0-computation/s44_n3_bdg.npz',
    # Gate
    gate_verdict=np.array([gate_verdict]),

    # BdG spectrum
    E_BdG_fold=E_BdG_full,
    E_BdG_vs_tau=E_BdG_vs_tau,
    xi_all=xi_all,
    Delta_all=Delta_all,
    anomalous_amplitudes=anomalous,

    # Node search
    min_abs_E_BdG_fold=results['min_abs_E_BdG_fold'],
    n_gapless_levels=results['n_gapless_levels'],
    n_paired_levels=results['n_paired_levels'],

    # Topological invariants
    N_3=results['N_3'],
    N_1=results['N_1'],
    eta_spectral=results['eta_spectral'],
    n_negative_BdG=results['n_negative_BdG'],
    pfaffian_sign=results['pfaffian_sign'],
    BDI_winding=results['BDI_winding'],

    # Level structure
    xi_vs_tau=xi_vs_tau,
    tau_values=tau_values,
    B2_dim=results['B2_dim'],
    n_unpaired=results['n_unpaired'],
    n_paired=results['n_paired'],

    # Classification
    codimension_node=results['codimension_node'],
    spatial_dimension=results['spatial_dimension'],
    N_3_required_dim=results['N_3_required_dim'],

    # Vacuum energy
    E_vac_BdG=results['E_vac_BdG'],
    E_vac_normal=results['E_vac_normal'],
    E_vac_condensation=results['E_vac_condensation'],
)
print("\nData saved to tier0-computation/s44_n3_bdg.npz")

# ============================================================
# STEP 11: Plot
# ============================================================
fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: BdG spectrum at fold
ax1 = fig.add_subplot(gs[0, 0])
E_sorted_fold = np.sort(E_BdG_full)
colors = []
for e in E_sorted_fold:
    # Color by paired/unpaired
    # Paired levels: E = sqrt(xi^2 + Delta^2), so E > max(xi)
    # Unpaired: E = +/- xi
    e_abs = abs(e)
    is_unpaired = any(abs(e_abs - xi_all[5:]) < 0.001) or any(abs(e_abs - xi_all[5:]) < 0.001)
    colors.append('red' if is_unpaired else 'blue')

for i, (e, c) in enumerate(zip(E_sorted_fold, colors)):
    ax1.barh(i, e, color=c, alpha=0.7, height=0.8)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_xlabel('E (BdG)', fontsize=11)
ax1.set_ylabel('Level index', fontsize=11)
ax1.set_title('BdG Spectrum at Fold (tau=0.2)', fontsize=12)
# Legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='blue', alpha=0.7, label='Paired (gapped)'),
                   Patch(facecolor='red', alpha=0.7, label='Unpaired (gapless)')]
ax1.legend(handles=legend_elements, loc='lower right', fontsize=9)

# Panel 2: BdG spectrum vs tau
ax2 = fig.add_subplot(gs[0, 1])
for j in range(16):
    # Color by type
    is_paired = j < 10  # First 10 (5 paired levels x 2 PH partners)
    c = 'blue' if is_paired else 'red'
    ax2.plot(tau_values, E_BdG_vs_tau[:, j], color=c, alpha=0.5, linewidth=1)
ax2.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax2.set_xlabel('tau', fontsize=11)
ax2.set_ylabel('E_BdG', fontsize=11)
ax2.set_title('BdG Spectrum vs tau', fontsize=12)
ax2.legend(handles=legend_elements, loc='upper left', fontsize=9)

# Panel 3: Single-particle levels (xi) vs tau
ax3 = fig.add_subplot(gs[0, 2])
labels_xi = ['xi_1 (B1-like)', 'xi_2 (B2-core)', 'xi_3 (unpaired)']
colors_xi = ['green', 'blue', 'red']
for j in range(3):
    valid = xi_vs_tau[:, j] > 0
    ax3.plot(tau_values[valid], xi_vs_tau[valid, j], 'o-', color=colors_xi[j],
             label=labels_xi[j], markersize=4, linewidth=1.5)
ax3.set_xlabel('tau', fontsize=11)
ax3.set_ylabel('|xi_k|', fontsize=11)
ax3.set_title('B2 Eigenvalue Magnitudes vs tau', fontsize=12)
ax3.legend(fontsize=9)
ax3.set_ylim([0.7, 1.3])

# Panel 4: Gap structure
ax4 = fig.add_subplot(gs[1, 0])
level_labels = ['B1\n(xi_1)', 'B2a\n(xi_2)', 'B2b\n(xi_2)', 'B2c\n(xi_2)', 'B2d\n(xi_2)',
                'B3a\n(xi_3)', 'B3b\n(xi_3)', 'B3c\n(xi_3)']
bar_colors = ['green'] + ['blue']*4 + ['red']*3
ax4.bar(range(8), np.abs(Delta_all), color=bar_colors, alpha=0.7)
ax4.set_xticks(range(8))
ax4.set_xticklabels(level_labels, fontsize=8)
ax4.set_ylabel('|Delta_k|', fontsize=11)
ax4.set_title('BCS Gap Function by Level', fontsize=12)
ax4.axhline(0, color='black', linewidth=0.5)

# Panel 5: Quasiparticle spectrum
ax5 = fig.add_subplot(gs[1, 1])
E_qp = np.sqrt(xi_all**2 + Delta_all**2)
ax5.bar(range(8), E_qp, color=bar_colors, alpha=0.7, label='E_qp')
ax5.bar(range(8), xi_all, color=bar_colors, alpha=0.3, label='|xi_k| (normal)')
ax5.set_xticks(range(8))
ax5.set_xticklabels(level_labels, fontsize=8)
ax5.set_ylabel('Energy', fontsize=11)
ax5.set_title('Quasiparticle Energy vs Normal State', fontsize=12)
ax5.legend(fontsize=9)

# Panel 6: Topological classification table
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
table_data = [
    ['Invariant', 'Value', 'Meaning'],
    ['N_3', '0 (N/A)', '0D system, no Fermi points'],
    ['N_1', '0', 'PH cancellation at all nodes'],
    ['eta', '0', 'PH enforced, not topological'],
    ['Pfaffian Z_2', '-1', 'Nontrivial (BDI, from S35)'],
    ['BDI winding W', '0', 'Post-transit (S38)'],
    ['min|E_BdG|', f'{results["min_abs_E_BdG_fold"]:.4f}', 'Gapped (no zero modes)'],
    ['Universality', '3He-B', 'NOT 3He-A (no Fermi points)'],
]
table = ax6.table(cellText=table_data, loc='center', cellLoc='center',
                   colWidths=[0.28, 0.22, 0.5])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.0, 1.5)
# Header styling
for j in range(3):
    table[0, j].set_facecolor('#4472C4')
    table[0, j].set_text_props(color='white', fontweight='bold')
# Highlight N_3 row
table[1, 0].set_facecolor('#FFD7D7')
table[1, 1].set_facecolor('#FFD7D7')
table[1, 2].set_facecolor('#FFD7D7')
ax6.set_title('Topological Classification', fontsize=12, pad=10)

fig.suptitle('N3-BDG-44: N_3 Topological Invariant for BdG Spectrum\n'
             'Gate Verdict: FAIL (no Fermi points in 0D system)',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig('tier0-computation/s44_n3_bdg.png', dpi=150, bbox_inches='tight')
print("Plot saved to tier0-computation/s44_n3_bdg.png")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
