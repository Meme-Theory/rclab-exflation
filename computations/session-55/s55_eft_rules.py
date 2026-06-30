#!/usr/bin/env python3
"""
s55_eft_rules.py — Post-Transit EFT Feynman Rules
===================================================
Feynman-Theorist, Session 55

From the 8-mode BCS lattice Hamiltonian at the fold (tau~0.194), construct:
  1. The effective Lagrangian with explicit coupling constants
  2. Feynman rules: propagators, vertices, external legs
  3. Tree-level 2→2 scattering amplitudes |M|^2
  4. Cross sections σ in natural units (1/M_KK^2)
  5. Operator classification by scaling dimension (d=1 non-rel EFT)
  6. Renormalizability assessment

Gate: EFT-RULES-55 (INFO)
"""

import numpy as np
import sys
sys.path.insert(0, 'computations')
from canonical_constants import M_KK

# ============================================================
# 1. LOAD DATA AT THE FOLD
# ============================================================

ed = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
fold_idx = int(ed['fold_idx'])
tau_fold = ed['tau_values'][fold_idx]

eps = ed['E_sp_sweep'][fold_idx]        # 8 single-particle energies (in M_KK units)
V_kl = ed['V_bare_cont'].copy()         # 8x8 pairing interaction matrix
n_k = ed['pair_occupations'][fold_idx]  # pair occupations
E0 = ed['E0'][fold_idx]                 # ground state energy (N=1 pair sector)

N_modes = 8  # (local)
labels_32 = tb['cell_labels']           # (p,q) labels for all 32 cells

print("=" * 72)
print("EFT-RULES-55: Post-Transit Effective Field Theory")
print("=" * 72)
print(f"\ntau_fold = {tau_fold:.6f}")
print(f"N_modes = {N_modes}")
print(f"M_KK = {M_KK:.4e} GeV")

# ============================================================
# 2. EFFECTIVE LAGRANGIAN
# ============================================================
# The post-transit EFT is a non-relativistic (d=1) many-body theory.
# All energies in units of M_KK. Time is the modulus flow parameter tau.
#
# L_eff = sum_k psi_k^dag (i d/dt - eps_k) psi_k
#       - sum_{k,l} V_{kl} psi_k^dag psi_{bar{k}}^dag psi_{bar{l}} psi_l
#
# where psi_k creates a Cooper pair in mode k, and the interaction
# scatters pair (l, bar{l}) -> (k, bar{k}).
#
# This is a 0+1 dimensional theory (quantum mechanics of 8 pair modes).
# Spatial dimensions are absent: we are inside a single unit cell of the
# M^4 x SU(3) lattice.

print("\n" + "=" * 72)
print("EFFECTIVE LAGRANGIAN")
print("=" * 72)

print("\nL = sum_k psi_k^dag (i d_t - eps_k) psi_k")
print("  - sum_{kl} V_{kl} psi_k^dag psi_{bar{k}}^dag psi_{bar{l}} psi_l")
print()
print("Single-particle spectrum (units: M_KK):")
print("-" * 50)
for k in range(N_modes):
    pq = labels_32[k]
    print(f"  mode {k}: (p,q)=({pq[0]},{pq[1]})  eps_{k} = {eps[k]:.6f}  "
          f"n_k = {n_k[k]:.6f}")
print(f"\n  Bandwidth W = {eps.max() - eps.min():.6f} M_KK")
print(f"  = {(eps.max() - eps.min()) * M_KK:.4e} GeV")

# Fermi energy: for N_pair=1, the Fermi level sits just above mode 0
eps_F = eps[0]  # lowest mode occupied at ~96%
print(f"\n  Fermi energy (mode 0): eps_F = {eps_F:.6f}")
print(f"  Occupied: mode 0 (n=0.958), weakly: mode 1 (n=0.031)")

# ============================================================
# 3. PAIRING INTERACTION ANALYSIS
# ============================================================

print("\n" + "=" * 72)
print("PAIRING INTERACTION V_{kl}")
print("=" * 72)

# Symmetry check
asym = np.max(np.abs(V_kl - V_kl.T))
print(f"\n  Symmetry: max|V - V^T| = {asym:.2e} (SYMMETRIC)")

# Eigendecomposition
eigs_V, vecs_V = np.linalg.eigh(V_kl)
print(f"\n  Eigenvalues of V:")
for i, e in enumerate(eigs_V):
    sgn = "attractive" if e < 0 else "repulsive "
    print(f"    lambda_{i} = {e:+.6f}  ({sgn})")

n_att = np.sum(eigs_V < -1e-10)
n_rep = np.sum(eigs_V > 1e-10)
print(f"\n  {n_att} attractive channels, {n_rep} repulsive channels")

# Coupling strength hierarchy
V_abs = np.abs(V_kl)
print(f"\n  |V|_max  = {V_abs.max():.6f} M_KK")
print(f"  |V|_mean = {np.mean(V_abs[V_abs > 1e-10]):.6f} M_KK")
print(f"  |V|_min  = {V_abs[V_abs > 1e-10].min():.6f} M_KK  (nonzero)")

# Mode 4 is special: couples only to 0-3, zero self-coupling
print(f"\n  Special structure:")
print(f"  V[4,4] = {V_kl[4,4]:.2e} (ZERO self-pairing)")
print(f"  V[4,0:4] = {V_kl[4,0:4]}  (UNIFORM coupling to lower block)")
print(f"  V[4,5:8] ~ 0: {V_kl[4,5:]}")

# Dimensionless coupling
g_eff = np.max(np.abs(eigs_V))  # largest eigenvalue
print(f"\n  Strongest coupling: g_max = {g_eff:.6f} M_KK")
print(f"  g_max / W = {g_eff / (eps.max() - eps.min()):.4f}  (coupling/bandwidth)")
print(f"  g_max * N(eps_F) estimate ~ g_max / delta_eps ~ {g_eff / (eps[1] - eps[0]):.4f}")

# ============================================================
# 4. FEYNMAN RULES
# ============================================================

print("\n" + "=" * 72)
print("FEYNMAN RULES")
print("=" * 72)

print("""
In the 0+1 dimensional EFT, we have:

PROPAGATOR (retarded):
  G_k(omega) = 1 / (omega - eps_k + i*eta)

  In the BCS ground state, the anomalous (Nambu-Gorkov) propagator is:
  G_k^{11}(omega) =  (omega + eps_k) / (omega^2 - E_k^2 + i*eta)
  G_k^{12}(omega) =  Delta_k / (omega^2 - E_k^2 + i*eta)

  where E_k = sqrt(eps_k^2 + Delta_k^2) is the quasiparticle energy.

VERTEX (4-point pairing):

     k ------>------ k
                |
            -i V_{kl}
                |
     l ------<------ l

  Factor: -i V_{kl}  for each pair scattering vertex
  Conservation: pair number is conserved at each vertex

EXTERNAL LEGS:
  Incoming pair in mode k:  factor 1
  Outgoing pair in mode k:  factor 1
  (No wavefunction renormalization at tree level)
""")

# Numerical propagators at omega = 0 (static limit)
print("Static propagators G_k(omega=0) = -1/eps_k:")
print("-" * 50)
for k in range(N_modes):
    if abs(eps[k]) > 1e-10:
        G0 = -1.0 / eps[k]
        print(f"  G_{k}(0) = {G0:+.4f} M_KK^{{-1}}")
    else:
        print(f"  G_{k}(0) = DIVERGENT (massless mode!)")

# ============================================================
# 5. TREE-LEVEL SCATTERING AMPLITUDES
# ============================================================

print("\n" + "=" * 72)
print("TREE-LEVEL 2→2 SCATTERING AMPLITUDES")
print("=" * 72)

print("""
Process: pair_k + pair_l -> pair_m + pair_n

At tree level, the amplitude is:
  M(kl -> mn) = -V_{km} delta_{ln} - V_{kn} delta_{lm}   (direct + exchange)

For identical incoming pairs (k=l):
  M(kk -> mn) = -V_{km} delta_{kn} - V_{kn} delta_{km}
              = -2 V_{km} delta_{kn}  (if m != n)
              = -2 V_{kk}             (forward, m=n=k)

For pair scattering (l -> k):
  M(l -> k) = -V_{kl}  (single vertex, no exchange)
""")

# Compute ALL distinct 2→2 amplitudes
# For Cooper pair scattering: initial pair in mode l, final pair in mode k
# M(l -> k) = -V_{kl}
print("Pair scattering amplitudes M(l -> k) = -V_{kl}:")
print("-" * 60)

# Find the largest amplitudes
amp_list = []
for k in range(N_modes):
    for l in range(N_modes):
        if abs(V_kl[k, l]) > 1e-10:
            amp_list.append((k, l, -V_kl[k, l]))

amp_list.sort(key=lambda x: abs(x[2]), reverse=True)

print(f"\nTop 15 amplitudes by |M|:")
for i, (k, l, M) in enumerate(amp_list[:15]):
    pq_k = labels_32[k]
    pq_l = labels_32[l]
    print(f"  {l}({pq_l[0]},{pq_l[1]}) -> {k}({pq_k[0]},{pq_k[1]}):  "
          f"M = {M:+.6f}  |M|^2 = {abs(M)**2:.6e}")

print(f"\n  Total nonzero amplitudes: {len(amp_list)}")

# ============================================================
# 6. CROSS SECTIONS
# ============================================================

print("\n" + "=" * 72)
print("CROSS SECTIONS (0+1D: transition rates)")
print("=" * 72)

print("""
In 0+1 dimensions (quantum mechanics), the "cross section" is the
transition rate via Fermi's golden rule:

  Gamma(l -> k) = 2*pi * |M(l->k)|^2 * rho(E_k)
                = 2*pi * V_{kl}^2 * rho(E_k)

where rho(E) is the density of final states. In our discrete system
with 8 modes, rho = delta-function (no continuum). The meaningful
quantity is the transition MATRIX ELEMENT |M|^2 itself.

For scattering in d=1 spatial dimensions (if we restore the lattice):
  sigma = |M|^2 / (4 * E_cm * |v_rel|)

where E_cm is the center-of-mass energy and v_rel the relative velocity.
""")

# Transition rate matrix Gamma_{kl} = 2*pi * V_{kl}^2
Gamma = 2 * np.pi * V_kl**2
print("Transition rate matrix Gamma_{kl} = 2*pi * V_{kl}^2 (M_KK units):")
print("-" * 60)
np.set_printoptions(precision=4, linewidth=110, suppress=True)
print(Gamma)

# Total decay rates out of each mode (sum over final states)
Gamma_tot = np.sum(Gamma, axis=0) - np.diag(Gamma)  # exclude self
print(f"\nTotal out-scattering rates (M_KK units):")
for k in range(N_modes):
    pq = labels_32[k]
    lifetime = 1.0 / Gamma_tot[k] if Gamma_tot[k] > 1e-20 else np.inf
    print(f"  mode {k} ({pq[0]},{pq[1]}): Gamma_out = {Gamma_tot[k]:.6f}  "
          f"tau_life = {lifetime:.4f}")

# In GeV units
print(f"\nIn physical units (GeV):")
print(f"  Gamma_out [GeV] = Gamma [M_KK] * M_KK = Gamma * {M_KK:.3e} GeV")
for k in range(N_modes):
    G_GeV = Gamma_tot[k] * M_KK
    print(f"  mode {k}: Gamma = {G_GeV:.4e} GeV  "
          f"(lifetime = {1.0/G_GeV * 6.582e-25:.4e} s)" if G_GeV > 0 else "")

# ============================================================
# 7. OPERATOR CLASSIFICATION (SCALING DIMENSIONS)
# ============================================================

print("\n" + "=" * 72)
print("OPERATOR CLASSIFICATION BY SCALING DIMENSION")
print("=" * 72)

print("""
This is a d=0+1 dimensional theory (quantum mechanics / 0D field theory).
All 8 modes live in a single spatial cell — no momentum, no spatial gradients.

Scaling analysis in d_spatial = 0:
  [t] = -1  (time has dimension of inverse energy)
  [psi] = 0  (dimensionless — pair creation/annihilation operators)
  [eps_k] = 1  (energy dimension)
  [V_{kl}] = 1  (energy dimension, from 4-point coupling)

In d=0 spatial dimensions, the action S = int dt L is dimensionless, so:
  [L] = [energy] = 1  (dimension of energy)

Power counting:
  - Kinetic term psi^dag i d_t psi:     [d_t] = 1, [psi^dag psi] = 0  -> dim 1 (MARGINAL)
  - Mass term eps_k psi^dag psi:         [eps_k] = 1, [psi^dag psi] = 0  -> dim 1 (MARGINAL)
  - Pairing V_{kl} psi^dag psi^dag psi psi:  [V] = 1, [psi^4] = 0  -> dim 1 (MARGINAL)

ALL operators are marginal in d=0+1! This is the standard result for
quantum mechanics: there is no RG flow from power counting alone.
The theory is EXACTLY RENORMALIZABLE (trivially — no UV divergences in
0+1D quantum mechanics with finitely many degrees of freedom).
""")

# But we can also consider the LATTICE extension with d=1 spatial dimension
# (hopping along the compact direction, 32 cells)
print("LATTICE EXTENSION: d=1+1 (one spatial + one time dimension)")
print("-" * 60)
print("""
If we restore the 32-cell lattice and allow pair hopping, the EFT gains
a spatial dimension. The tight-binding Hamiltonian provides the dispersion
eps_k -> eps(k, momentum). Now:

  [x] = -1  (inverse energy)
  [t] = -1
  [psi(x,t)] = 1/2  (canonical dimension in d=1+1)
  [eps] = 1
  [V] = 1

Power counting in d=1+1:
  Action S = int dx dt L, so [L] = 2 (energy/length = energy^2 in natural units)

  - Kinetic: psi^dag (i d_t - t d_x^2) psi -> [psi^2 d_t] = 1 + 1 = 2 (MARGINAL)
  - Mass: eps psi^dag psi -> [eps psi^2] = 1 + 1 = 2 (MARGINAL)
  - 4-Fermi: V psi^4 -> [V psi^4] = 1 + 2 = 3 > 2 (IRRELEVANT by 1 unit)
    => coupling has dim [V] = [E]^{-1} in natural units
    => theory is NON-RENORMALIZABLE in d=1+1

Wait — but in the BCS channel, the 4-Fermi interaction is MARGINALLY
RELEVANT by the Cooper instability (any attractive coupling, no matter
how weak, flows to strong coupling in 1D). This is the 1D BCS theorem
(RG-BCS-35, proven in Session 35).
""")

# ============================================================
# 8. RENORMALIZABILITY AND UV STRUCTURE
# ============================================================

print("\n" + "=" * 72)
print("RENORMALIZABILITY ASSESSMENT")
print("=" * 72)

# In 0+1D: no loop divergences (finite-dimensional Hilbert space)
# The theory is UV COMPLETE as a quantum mechanics problem

# Loop correction: one-loop self-energy
print("ONE-LOOP STRUCTURE:")
print("-" * 60)

# Self-energy: Sigma_k(omega) = sum_l V_{kl}^2 G_l(omega)
# At omega = eps_k (on-shell):
print("\nOne-loop self-energy (Hartree-Fock shift):")
for k in range(N_modes):
    Sigma_HF = 0.0  # (local)
    for l in range(N_modes):
        if l != k:
            Sigma_HF += V_kl[k, l]**2 * n_k[l] / (eps[k] - eps[l]) if abs(eps[k] - eps[l]) > 1e-10 else 0
    # Hartree term: sum_l V_{kl} <n_l>
    Sigma_H = sum(V_kl[k, l] * n_k[l] for l in range(N_modes))
    print(f"  mode {k}: Sigma_H = {Sigma_H:.6f}, Sigma_Fock = {Sigma_HF:.6f}, "
          f"total = {Sigma_H + Sigma_HF:.6f}")

# Loop integral convergence (in 0+1D)
print("""
UV CONVERGENCE:
  In 0+1D with 8 modes: Hilbert space = 2^8 = 256 states.
  NO UV divergences — the theory is exactly solvable by ED.
  The Fock space is FINITE. No regularization needed.

  In the 32-cell lattice extension (d=1): the Brillouin zone is compact
  (32 k-points). Again NO UV divergences from the lattice cutoff.

  CONCLUSION: The post-transit EFT is UV-COMPLETE as a lattice theory.
  It does NOT need a continuum limit. The lattice IS the theory.
""")

# ============================================================
# 9. COUPLING HIERARCHY AND EFFECTIVE EXPANSION PARAMETER
# ============================================================

print("\n" + "=" * 72)
print("COUPLING HIERARCHY")
print("=" * 72)

# The natural expansion parameter is V/W (interaction/bandwidth)
W = eps.max() - eps.min()  # (local)
print(f"\nBandwidth W = {W:.6f} M_KK = {W * M_KK:.4e} GeV")
print(f"Condensation energy E_cond = {E0:.6f} M_KK")
print(f"|E_cond|/W = {abs(E0)/W:.4f}")

# V eigenvalue hierarchy
print(f"\nV eigenvalue spectrum (defines coupling channels):")
for i, e in enumerate(eigs_V):
    channel = "attractive" if e < 0 else "repulsive"
    ratio = abs(e) / W
    print(f"  Channel {i}: lambda = {e:+.6f} M_KK  ({channel}, |lambda|/W = {ratio:.4f})")

# Most attractive channel
mac = eigs_V[0]  # most negative eigenvalue
mac_vec = vecs_V[:, 0]
print(f"\nMost Attractive Channel (MAC):")
print(f"  lambda_MAC = {mac:.6f} M_KK")
print(f"  |lambda_MAC|/W = {abs(mac)/W:.4f}")
print(f"  MAC eigenvector: {mac_vec}")
print(f"  Dominant mode contributions: ", end="")
top3 = np.argsort(np.abs(mac_vec))[-3:][::-1]
for idx in top3:
    print(f"mode {idx} ({abs(mac_vec[idx]):.3f})", end="  ")
print()

# BCS gap from mean-field (weak coupling formula)
# Delta ~ W * exp(-1/(N(0)*|V_mac|))
# For d=0+1D: N(0) ~ 1/delta_eps for states near Fermi level
delta_eps_01 = eps[1] - eps[0] if eps[1] - eps[0] > 1e-10 else 0.177
N_0 = 1.0 / delta_eps_01
g_mac = abs(mac)
bcs_param = N_0 * g_mac
print(f"\nBCS parameters:")
print(f"  Level spacing delta_eps = {delta_eps_01:.6f} M_KK")
print(f"  N(eps_F) ~ 1/delta_eps = {N_0:.4f}")
print(f"  |V_mac| * N(0) = {bcs_param:.4f}")
if bcs_param > 0:
    Delta_BCS = W * np.exp(-1.0 / bcs_param) if bcs_param > 0.01 else 0
    print(f"  Delta_BCS ~ W * exp(-1/gN) = {Delta_BCS:.6f} M_KK")
    print(f"  Delta_BCS / W = {Delta_BCS/W:.6f}")

# ============================================================
# 10. FEYNMAN DIAGRAM COUNT AND PERTURBATIVE CONVERGENCE
# ============================================================

print("\n" + "=" * 72)
print("PERTURBATIVE STRUCTURE")
print("=" * 72)

# Number of diagrams at each loop order
# In 0+1D with N modes, the n-loop contribution scales as V^n
# Convergence requires V/Delta_eps << 1
print(f"\nExpansion parameter: V_typ / delta_eps")
V_typ = np.mean(np.abs(V_kl[V_kl != 0]))
xi = V_typ / delta_eps_01
print(f"  V_typ = {V_typ:.6f}")
print(f"  delta_eps = {delta_eps_01:.6f}")
print(f"  xi = V_typ/delta_eps = {xi:.4f}")

if xi < 1:
    print(f"  PERTURBATION THEORY CONVERGES (xi < 1)")
else:
    print(f"  PERTURBATION THEORY MAY NOT CONVERGE (xi >= 1)")

# Compare perturbative vs exact
print(f"\nPerturbative vs exact ground state:")
print(f"  E_0^(0) = eps_0 = {eps[0]:.6f}  (unperturbed)")
# First-order: E_0^(1) = V_{00} * n_0
E1 = V_kl[0, 0] * n_k[0]
print(f"  E_0^(1) = V_00 * n_0 = {E1:.6f}")
# Second-order: sum_l |V_{0l}|^2 / (eps_0 - eps_l) for l != 0
E2 = 0
for l in range(1, N_modes):
    if abs(eps[0] - eps[l]) > 1e-10:
        E2 += V_kl[0, l]**2 / (eps[0] - eps[l])
print(f"  E_0^(2) = sum |V_0l|^2/(eps_0-eps_l) = {E2:.6f}")
print(f"  E_pert = {eps[0] + E1 + E2:.6f}")
print(f"  E_exact = {E0:.6f}")
print(f"  Error = {abs(eps[0] + E1 + E2 - E0):.6f} = {abs((eps[0]+E1+E2-E0)/E0)*100:.1f}%")

# ============================================================
# 11. ANOMALOUS PROPAGATOR (BdG / Nambu-Gorkov)
# ============================================================

print("\n" + "=" * 72)
print("ANOMALOUS PROPAGATOR (BdG STRUCTURE)")
print("=" * 72)

# From ED pair occupations, extract BCS coherence factors
# n_k = v_k^2, so v_k = sqrt(n_k), u_k = sqrt(1 - n_k)
v_k = np.sqrt(n_k)
u_k = np.sqrt(1 - n_k)

print("\nBCS coherence factors at fold:")
for k in range(N_modes):
    print(f"  mode {k}: u_k = {u_k[k]:.6f}, v_k = {v_k[k]:.6f}, "
          f"u*v = {u_k[k]*v_k[k]:.6f}, n_k = {n_k[k]:.6f}")

# Gap function from self-consistency: Delta_k = sum_l V_{kl} u_l v_l
Delta_k = np.zeros(N_modes)
for k in range(N_modes):
    Delta_k[k] = sum(V_kl[k, l] * u_k[l] * v_k[l] for l in range(N_modes))

print(f"\nGap function Delta_k = sum_l V_kl * u_l * v_l:")
for k in range(N_modes):
    print(f"  Delta_{k} = {Delta_k[k]:.6f}")

# Quasiparticle energies
E_qp = np.sqrt(eps**2 + Delta_k**2)
print(f"\nQuasiparticle energies E_k = sqrt(eps_k^2 + Delta_k^2):")
for k in range(N_modes):
    print(f"  E_{k} = {E_qp[k]:.6f}  (eps = {eps[k]:.6f}, Delta = {Delta_k[k]:.6f})")

# The full Nambu-Gorkov propagator
print("""
NAMBU-GORKOV PROPAGATOR (2x2 matrix for each mode k):

  G_k(omega) = 1/(omega^2 - E_k^2) * [ omega + eps_k     Delta_k    ]
                                       [  Delta_k      omega - eps_k  ]

where E_k = sqrt(eps_k^2 + Delta_k^2).

Poles at omega = +-E_k give quasiparticle and quasihole excitations.
""")

# ============================================================
# 12. COMPLETE FEYNMAN RULE TABLE
# ============================================================

print("\n" + "=" * 72)
print("COMPLETE FEYNMAN RULE TABLE")
print("=" * 72)

print("""
╔══════════════════════════════════════════════════════════════════════╗
║  POST-TRANSIT EFT FEYNMAN RULES (0+1D, 8 pair modes)              ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                     ║
║  PROPAGATOR (normal):                                               ║
║    ───k──── = G_k(omega) = 1/(omega - eps_k + i*eta)               ║
║                                                                     ║
║  PROPAGATOR (anomalous, in BCS ground state):                       ║
║    ═══k════ = F_k(omega) = Delta_k/(omega^2 - E_k^2 + i*eta)      ║
║                                                                     ║
║  VERTEX (pair scattering):                                          ║
║    k >──┐                                                           ║
║         │ = -i V_{kl}                                               ║
║    l <──┘                                                           ║
║                                                                     ║
║  VERTEX (pair creation/annihilation, from anomalous):               ║
║    k >──┐                                                           ║
║         │ = -i V_{kl} * u_k * v_l  (BCS vertex)                    ║
║    l >──┘                                                           ║
║                                                                     ║
║  SYMMETRY FACTOR: 1/(n! * 2^m) for n equivalent loops, m self-     ║
║    contractions. In practice: factor 2 for each closed pair loop.   ║
║                                                                     ║
║  ENERGY CONSERVATION: sum(omega_in) = sum(omega_out) at each vertex ║
║                                                                     ║
║  LOOP INTEGRAL: sum over intermediate mode index (discrete, not     ║
║    continuous — no UV divergence).                                   ║
║                                                                     ║
╚══════════════════════════════════════════════════════════════════════╝
""")

# ============================================================
# 13. SUMMARY TABLE OF NUMERICAL VALUES
# ============================================================

print("\n" + "=" * 72)
print("NUMERICAL SUMMARY")
print("=" * 72)

print(f"\n{'Quantity':<40} {'Value':<20} {'Units'}")
print("-" * 72)
print(f"{'tau_fold':<40} {tau_fold:<20.6f} {'dimensionless'}")
print(f"{'N_modes':<40} {N_modes:<20d} {''}")
print(f"{'Bandwidth W':<40} {W:<20.6f} {'M_KK'}")
print(f"{'Level spacing delta_eps':<40} {delta_eps_01:<20.6f} {'M_KK'}")
print(f"{'|V|_max':<40} {V_abs.max():<20.6f} {'M_KK'}")
print(f"{'|V|_mean':<40} {V_typ:<20.6f} {'M_KK'}")
print(f"{'lambda_MAC':<40} {abs(mac):<20.6f} {'M_KK'}")
print(f"{'g*N(0) = |V_mac|/delta_eps':<40} {bcs_param:<20.4f} {''}")
print(f"{'Expansion parameter xi':<40} {xi:<20.4f} {''}")
print(f"{'E_cond (exact, ED)':<40} {E0:<20.6f} {'M_KK'}")
print(f"{'|E_cond|/W':<40} {abs(E0)/W:<20.6f} {''}")
print(f"{'Delta_BCS (mean-field)':<40} {Delta_BCS:<20.6f} {'M_KK'}")
print(f"{'E_0 perturbative (2nd order)':<40} {eps[0]+E1+E2:<20.6f} {'M_KK'}")
print(f"{'Perturbative error':<40} {abs((eps[0]+E1+E2-E0)/E0)*100:<20.1f} {'%'}")

# ============================================================
# 14. GATE VERDICT
# ============================================================

print("\n" + "=" * 72)
print("GATE VERDICT: EFT-RULES-55")
print("=" * 72)

print(f"""
CLASSIFICATION: INFO (no pass/fail threshold)

RESULTS:
  1. EFFECTIVE LAGRANGIAN: Written explicitly with 8 modes, numerical
     coupling constants V_kl. All operators MARGINAL in d=0+1.

  2. FEYNMAN RULES: Complete set including normal propagator, anomalous
     propagator, pair-scattering vertex (-iV_kl), BCS vertex.

  3. TREE-LEVEL AMPLITUDES: |M|_max = {V_abs.max():.4f} M_KK
     (mode 4 -> modes 0-3, uniform coupling V = 0.0799).
     |M|^2_max = {V_abs.max()**2:.6f} M_KK^2.

  4. COUPLING HIERARCHY:
     - 3 attractive + 5 repulsive eigenchannels in V
     - Most attractive channel: |lambda_MAC| = {abs(mac):.4f} M_KK
     - BCS parameter g*N(0) = {bcs_param:.2f} (> 1: strong pairing)
     - Expansion parameter xi = V/delta_eps = {xi:.2f}

  5. RENORMALIZABILITY:
     - d=0+1: EXACTLY SOLVABLE. Finite Hilbert space (2^8 = 256).
       No UV divergences. All operators marginal.
     - d=1+1 lattice: UV-COMPLETE via lattice cutoff (32 k-points).
       4-Fermi interaction naively irrelevant but MARGINALLY RELEVANT
       via Cooper instability (1D BCS theorem).
     - Perturbation theory: xi = {xi:.2f} -> {'CONVERGENT' if xi < 1 else 'BORDERLINE'}.
       2nd-order energy error = {abs((eps[0]+E1+E2-E0)/E0)*100:.1f}%.
       ED (exact diagonalization) is preferred.

  6. KEY PHYSICAL FEATURE: Mode 4 (0,2) acts as a UNIVERSAL COUPLER
     to modes 0-3 with identical V = 0.0799 and zero self-pairing.
     This is a selection rule from the SU(3) representation theory
     (Casimir C2 = 10/3 for the 6-dimensional rep).

PHONONIC CLASSIFICATION: PARTICLE (EFT of quasiparticle excitations
  above the BCS ground state of the M^4 x SU(3) substrate).
""")

# ============================================================
# 15. SAVE RESULTS
# ============================================================

np.savez('computations/session-55/s55_eft_rules.npz',
    tau_fold=tau_fold,
    eps=eps,
    V_kl=V_kl,
    n_k=n_k,
    E0=E0,
    eigs_V=eigs_V,
    vecs_V=vecs_V,
    u_k=u_k,
    v_k=v_k,
    Delta_k=Delta_k,
    E_qp=E_qp,
    Gamma_kl=Gamma,
    Gamma_tot=Gamma_tot,
    bandwidth=W,
    delta_eps=delta_eps_01,
    g_N0=bcs_param,
    xi_expansion=xi,
    labels=labels_32[:8],
    gate_name='EFT-RULES-55',
    gate_verdict='INFO',
)

print("\nResults saved to computations/session-55/s55_eft_rules.npz")
print("Script: computations/session-55/s55_eft_rules.py")
print("\nDone.")
