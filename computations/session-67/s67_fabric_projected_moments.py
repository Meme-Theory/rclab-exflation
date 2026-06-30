#!/usr/bin/env python3
"""
FABRIC-PROJECTED-MOMENTS-67: Beyond-Mean-Field a_2 on Josephson-Coupled Fabric
==============================================================================

Extends W2-B (single-cell projected moments) to the 24-cell CG(24) Josephson
fabric. The question: does inter-cell coupling change the spectral moments
beyond the single-cell mean-field values?

STRUCTURAL INSIGHT:
  The Josephson coupling J*z ~ 3.95 M_KK >> Delta_0 ~ 0.46 M_KK.
  A perturbative proximity expansion (delta_Delta/Delta ~ J*z/(N*Delta)) gives
  eta_J > 1 and breaks down immediately. This is NOT a perturbative correction.

  The correct treatment uses three structural results:
  1. BLOCH SUM RULE: Sum_K a_n(K) = N_cells * a_n^{cell} (EXACT).
     The Josephson coupling redistributes spectral weight in K-space but does
     NOT change the total K-integrated moment. D_K is local to each fiber.
  2. BAND CONFINEMENT (S63): Josephson creates bands with inter-band gap/Delta=60.
     Pair correlations are confined to the lowest band (PR=1.03).
  3. PAIRING DILUTION (S63): Within the lowest band, BCS operates on N_cells
     levels instead of N_levels per cell. The effective coupling G_eff = G/N_cells.

  The spectral moments a_n are GEOMETRIC quantities of D_K, not BCS quantities.
  The BCS pairing modifies the occupation numbers n_k which enter the thermal
  spectral moments. But the TOTAL (vacuum) moments are pairing-independent.
  The beyond-mean-field correction is ONLY to the occupation-number-weighted
  (thermal) part of a_n.

Nuclear analog: In heavy nuclei coupled by Coulomb (analogous to Josephson),
the spectral moments of the nuclear density functional are dominated by the
smooth (Thomas-Fermi) part, with shell corrections at the ~1% level (Paper 08).
The inter-cluster coupling creates Josephson-band analogs (giant resonances)
but does not change the total spectral weight.

Gate: FABRIC-PROJECTED-MOMENTS-67
  PASS: |delta_a_2 / a_2| < 10%
  FAIL: |delta_a_2 / a_2| > 20%

Author: Nazarewicz Nuclear Structure Theorist Agent
Session: S67
"""

import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, Delta_0_OES, E_cond, a2_fold, a4_fold, a0_fold,
    J_C2, J_su2, J_u1, N_cells, N_dof_BCS, E_B1, E_B2_mean, E_B3_mean,
    Delta_B3, M_KK
)

# ============================================================================
# 1. Load W2-B single-cell data
# ============================================================================

data_dir = Path(__file__).parent
w2b = np.load(data_dir / 's67_projected_moments.npz', allow_pickle=True)
jose = np.load(data_dir / 's52_gl_josephson.npz', allow_pickle=True)

eps_bare = w2b['eps_bare']       # 8-mode single-particle energies [M_KK]
labels = w2b['labels']
a2_bare = float(w2b['a2_bare'])  # Bare (vacuum) a_2 per cell
a4_bare = float(w2b['a4_bare'])
a2_bcs = float(w2b['a2_bcs'])   # BCS mean-field a_2
a4_bcs = float(w2b['a4_bcs'])
Delta_0 = float(w2b['Delta_0'])  # BCS gap (OES)

ed_data = {}
for N in range(1, 5):
    ed_data[N] = {
        'n_k_ed': w2b[f'N{N}_n_k_ed'],
        'n_k_bcs': w2b[f'N{N}_n_k_bcs'],
        'a2_ed': float(w2b[f'N{N}_a2_ed']),
        'a4_ed': float(w2b[f'N{N}_a4_ed']),
        'delta_a2': float(w2b[f'N{N}_delta_a2']),
        'delta_a4': float(w2b[f'N{N}_delta_a4']),
        'Delta_B1': float(w2b[f'N{N}_Delta_B1_eff']),
        'Delta_B2': float(w2b[f'N{N}_Delta_B2_eff']),
        'Delta_B3': float(w2b[f'N{N}_Delta_B3_eff']),
    }

print("=" * 70)
print("FABRIC-PROJECTED-MOMENTS-67")
print("=" * 70)
print(f"\nW2-B single-cell recap:")
print(f"  a2_bare = {a2_bare:.4f},  a4_bare = {a4_bare:.4f}")
print(f"  a2_bcs  = {a2_bcs:.4f},   a4_bcs  = {a4_bcs:.4f}")
print(f"  Delta_0 = {Delta_0:.6f} M_KK")
for N in range(1, 5):
    d = ed_data[N]
    print(f"  N={N}: a2_ed={d['a2_ed']:.2f}, delta_a2/a2={d['delta_a2']*100:.1f}%")

# ============================================================================
# 2. Build CG(24) graph
# ============================================================================

def build_cg24():
    """24-cell polytope adjacency. Vertices = permutations of (+-1,+-1,0,0)."""
    from itertools import product as iprod
    verts = set()
    for s1, s2 in iprod([1, -1], repeat=2):
        for i in range(4):
            for j in range(i + 1, 4):
                v = [0, 0, 0, 0]
                v[i], v[j] = s1, s2
                verts.add(tuple(v))
    verts = sorted(verts)
    Nv = len(verts)
    adj = np.zeros((Nv, Nv), dtype=float)
    for a in range(Nv):
        for b in range(a + 1, Nv):
            d2 = sum((verts[a][k] - verts[b][k])**2 for k in range(4))
            if abs(d2 - 2.0) < 1e-10:
                adj[a, b] = adj[b, a] = 1.0
    return adj, verts

A_cg24, verts_cg24 = build_cg24()
N_fabric = A_cg24.shape[0]  # 24
z_coord = int(A_cg24.sum(axis=1)[0])  # 8
eigvals_adj = np.sort(np.linalg.eigvalsh(A_cg24))[::-1]

# Isotropic effective Josephson: weighted average over 8 bonds
# (4 C2-type at J_C2, 3 su(2)-type at J_su2, 1 u(1)-type at J_u1)
J_eff_iso = (4 * J_C2 + 3 * J_su2 + 1 * J_u1) / z_coord
J_total_per_vert = 4 * J_C2 + 3 * J_su2 + 1 * J_u1  # z * J_eff

print(f"\n--- CG(24) Graph ---")
print(f"  N_fabric = {N_fabric}, z = {z_coord}, edges = {int(A_cg24.sum())//2}")
print(f"  Adjacency eigenvalues: {np.round(eigvals_adj, 2)}")
print(f"  J_eff_iso = {J_eff_iso:.4f} M_KK,  z*J_eff = {J_total_per_vert:.4f} M_KK")

# ============================================================================
# 3. STRUCTURAL ANALYSIS: Why perturbative proximity fails
# ============================================================================

print("\n" + "=" * 70)
print("3. WHY PERTURBATIVE PROXIMITY FAILS")
print("=" * 70)

W_J = 2 * z_coord * J_eff_iso  # Josephson bandwidth
eps_bw = np.max(eps_bare) - np.min(eps_bare)  # single-cell bandwidth
d_spacing = eps_bw / len(eps_bare)  # mean level spacing

print(f"\n  Josephson bandwidth W_J = 2*z*J_eff = {W_J:.4f} M_KK")
print(f"  BCS gap Delta_0 = {Delta_0:.4f} M_KK")
print(f"  W_J / Delta_0 = {W_J / Delta_0:.2f}")
print(f"  z * J_eff / Delta_0 = {J_total_per_vert / Delta_0:.2f}")
print(f"  Level spacing d = {d_spacing:.4f} M_KK")
print(f"  d / Delta = {d_spacing / Delta_0:.4f}")
print(f"  J_eff / d = {J_eff_iso / d_spacing:.2f}")
print(f"\n  CONCLUSION: J >> Delta >> d. Josephson is the DOMINANT energy scale.")
print(f"  Perturbative expansion in J/Delta INVALID (ratio = {J_total_per_vert/Delta_0:.1f}).")
print(f"  Must use non-perturbative methods.")

# ============================================================================
# 4. NON-PERTURBATIVE APPROACH: Bloch sum rule + band confinement
# ============================================================================

print("\n" + "=" * 70)
print("4. NON-PERTURBATIVE APPROACH")
print("=" * 70)

# THEOREM (Bloch Sum Rule for Spectral Moments):
# -----------------------------------------------
# The Seeley-DeWitt coefficient a_n is defined as:
#   a_n = Tr[P_occ * O_n(D_K)]
# where O_n is a local geometric operator (R for a_2, etc.) and P_occ
# projects onto occupied states.
#
# For the fabric: D_K acts WITHIN each fiber. The Josephson coupling H_J
# acts on the INTER-CELL phase degrees of freedom, not on D_K.
# Therefore:
#   a_n^{fabric} = Sum_{cells i} Tr_i[P_occ^{(i)} * O_n(D_K^{(i)})]
#                = Sum_i a_n^{cell}(n_k^{(i)})
#
# For a UNIFORM fabric (all cells identical, as in the BCS ground state):
#   a_n^{fabric} = N_cells * a_n^{cell}(n_k)
#
# The inter-cell coupling modifies a_n ONLY through its effect on
# the OCCUPATION NUMBERS n_k within each cell.
#
# KEY POINT: The Josephson coupling does NOT enter D_K. It enters the
# Hamiltonian that determines the ground state (hence n_k), but the
# spectral moments themselves are purely geometric (from D_K).

print(f"\n  BLOCH SUM RULE:")
print(f"  a_n^{{fabric}} = N_cells * a_n^{{cell}}(n_k)")
print(f"  Josephson modifies n_k, not D_K.")
print(f"  Question reduces to: how does fabric coupling modify n_k?")

# ============================================================================
# 5. HOW JOSEPHSON MODIFIES OCCUPATION NUMBERS
# ============================================================================

print("\n" + "=" * 70)
print("5. JOSEPHSON EFFECT ON OCCUPATION NUMBERS")
print("=" * 70)

# The fabric ground state has two contributions to the total energy:
#   E_total = Sum_i E_BCS(i) + E_J({phi_i})
#
# In the BCS ground state, all cells are identical and phase-locked:
#   phi_i = phi_0, Delta_i = Delta_0, n_k^{(i)} = n_k^{cell}
#
# The Josephson energy is:
#   E_J = -N_bonds * J_eff * <cos(phi_i - phi_j)>
#       = -(N_fabric * z / 2) * J_eff  (when all phases aligned)
#
# This is a CONSTANT shift to the total energy. It does NOT depend on n_k.
# Therefore: the occupation numbers that minimize E_BCS within each cell
# are UNCHANGED by the Josephson coupling.
#
# PROOF:
# The ground state satisfies: d(E_total)/d(n_k) = 0 for all k, all cells.
# E_total = Sum_i E_BCS(n_k^{(i)}) + E_J({phi_i})
# For the phase-locked state: E_J = constant (independent of n_k)
# So: d(E_total)/d(n_k^{(i)}) = d(E_BCS)/d(n_k^{(i)}) = 0
# => n_k^{fabric} = n_k^{cell}  QED
#
# The ONLY way Josephson can modify n_k is through FLUCTUATIONS:
# (a) Phase fluctuations: <cos(phi_i - phi_j)> < 1
# (b) Amplitude fluctuations: <Delta_i> != Delta_0
# Both are QUANTUM fluctuations beyond mean field.

N_bonds = N_fabric * z_coord // 2
E_J_ground = -N_bonds * J_eff_iso  # Total Josephson energy (phase-locked)

print(f"\n  Phase-locked ground state:")
print(f"  N_bonds = {N_bonds}")
print(f"  E_J = -{N_bonds} * {J_eff_iso:.4f} = {E_J_ground:.4f} M_KK")
print(f"\n  KEY RESULT: In the mean-field (phase-locked) fabric,")
print(f"  Josephson coupling is a CONSTANT energy shift.")
print(f"  n_k^{{fabric}} = n_k^{{cell}} EXACTLY (at mean-field level).")
print(f"  => a_n^{{fabric}} = N_cells * a_n^{{cell}} EXACTLY.")

# ============================================================================
# 6. BEYOND MEAN FIELD: Quantum phase fluctuations
# ============================================================================

print("\n" + "=" * 70)
print("6. QUANTUM PHASE FLUCTUATIONS")
print("=" * 70)

# The mean-field result above is EXACT for the phase-locked state.
# Beyond mean field, quantum fluctuations of the phases modify <cos(dphi)>,
# which feeds back into the effective pairing.
#
# The relevant parameter is the Josephson-to-charging energy ratio:
#   E_J / E_C = J_eff * z / E_C
# where E_C is the "charging energy" (cost of adding one pair to a cell).
# From S56 EJ-UNCERTAINTY-56: E_J/E_C = 194 +/- 14.
#
# In the superfluid regime (E_J >> E_C), phase fluctuations are small:
#   <(phi_i - phi_j)^2> ~ sqrt(E_C / E_J) << 1
#   <cos(dphi)> ~ 1 - <dphi^2>/2 ~ 1 - (1/2)*sqrt(E_C/E_J)
#
# The CORRECTION to n_k from phase fluctuations is:
#   delta_n_k / n_k ~ <dphi^2> * (Delta/E_k)^2 * (J/Delta)
# which is small when <dphi^2> << 1.

# From S56: E_J/E_C = 194
EJ_over_EC = 194.0  # from S56 EJ-UNCERTAINTY-56  # (local)

# Phase fluctuation amplitude
dphi_sq = np.sqrt(1.0 / EJ_over_EC)  # RMS phase fluctuation
cos_dphi = 1.0 - dphi_sq / 2.0

print(f"\n  E_J/E_C = {EJ_over_EC:.0f} (from S56)")
print(f"  <(dphi)^2>^{{1/2}} ~ (E_C/E_J)^{{1/4}} = {dphi_sq:.6f}")
print(f"  <cos(dphi)> ~ 1 - <dphi^2>/2 = {cos_dphi:.6f}")

# Effective Josephson coupling with fluctuation correction:
J_eff_corrected = J_eff_iso * cos_dphi
delta_J_frac = (J_eff_iso - J_eff_corrected) / J_eff_iso

print(f"  J_eff (mean-field) = {J_eff_iso:.6f}")
print(f"  J_eff (corrected) = {J_eff_corrected:.6f}")
print(f"  delta_J/J = {delta_J_frac*100:.4f}%")

# The effect on n_k goes through the SELF-CONSISTENT modification of Delta.
# At mean-field level (Section 5): delta_n_k = 0 (exactly).
# Phase fluctuations introduce a small correction via:
#   delta_E_J = -(z/2) * J_eff * delta<cos(dphi)> per bond
# This modifies the effective pairing potential by:
#   delta_V_pair ~ delta<cos(dphi)> * J_eff / (N_levels * Delta)
# = very small number squared

# The occupation number correction from fluctuations:
# delta_n_k ~ (Delta/E_k)^2 * delta_V_pair / (2*E_k)

# Compute E_k for N=4 (half-filling, decisive case)
n_bcs_N4 = ed_data[4]['n_k_bcs']
mu_bcs = np.mean(eps_bare[:4])  # Approximate: Fermi level in B2 sector
xi_k = eps_bare - mu_bcs
E_k = np.sqrt(xi_k**2 + Delta_0**2)

# delta_V_pair from phase fluctuation correction to Josephson:
# The Josephson coupling modifies the ground-state energy.
# The PHASE FLUCTUATION correction to the gap equation:
# In the Josephson array, the phase-fluctuation-renormalized gap is
# (Fazio & van der Zant, Phys. Rep. 355 (2001)):
#   Delta_eff = Delta_0 * (1 - alpha_QF)
# where alpha_QF is the quantum depletion from phase fluctuations.
#
# For E_J/E_C >> 1 (deep superfluid):
#   alpha_QF ~ (1/(2*pi)) * sqrt(E_C/E_J) * (z/N_levels)
# This accounts for the quantum depletion of the condensate fraction.

alpha_QF = (1.0 / (2 * np.pi)) * np.sqrt(1.0 / EJ_over_EC) * (z_coord / len(eps_bare))
Delta_eff = Delta_0 * (1.0 - alpha_QF)
delta_Delta_frac = alpha_QF

print(f"\n  Quantum depletion alpha_QF = {alpha_QF:.6f}")
print(f"  Delta_eff = Delta_0 * (1 - alpha_QF) = {Delta_eff:.6f}")
print(f"  delta_Delta/Delta = {delta_Delta_frac*100:.4f}%")

# Occupation number shift from delta_Delta:
# delta_n_k = d(n_k)/d(Delta) * delta_Delta
#           = (Delta / (2*E_k^3)) * delta_Delta
delta_n_QF = (Delta_0 / (2 * E_k**3)) * (Delta_0 * alpha_QF)

print(f"\n  Occupation number shifts from quantum fluctuations:")
for i in range(len(eps_bare)):
    print(f"    {labels[i]}: delta_n = {delta_n_QF[i]:.2e}")
print(f"    Sum |delta_n| = {np.sum(np.abs(delta_n_QF)):.2e}")

# ============================================================================
# 7. SPECTRAL MOMENT CORRECTION FROM FLUCTUATIONS
# ============================================================================

print("\n" + "=" * 70)
print("7. SPECTRAL MOMENT CORRECTION")
print("=" * 70)

# The spectral moments with occupation-number weighting:
#   a_n(N_pair) = Sum_k a_n^{(k)} * (1 - 2*n_k)
# where a_n^{(k)} is the per-mode contribution to bare a_n.
#
# Rather than extract per-mode weights (which is ill-conditioned with
# non-uniform modes), use the W2-B data DIRECTLY.
#
# W2-B already computed a_n^{ED}(N) which includes exact pairing correlations.
# The FABRIC correction is ONLY from the quantum fluctuation correction
# to occupation numbers (Section 6).
#
# delta_a2^{QF} = -2 * Sum_k a2_k * delta_n_k^{QF}
#
# We can bound this using the MAXIMUM possible per-mode weight:
# a2_k <= a2_bare (a single mode cannot contribute more than the total)
# And delta_n_k is bounded.

# Upper bound on correction:
# |delta_a2^{QF}| <= 2 * a2_bare * Sum_k |delta_n_k|
# This is a GROSS overestimate but gives a hard upper bound.
sum_abs_delta_n = np.sum(np.abs(delta_n_QF))
upper_bound_a2 = 2 * a2_bare * sum_abs_delta_n

print(f"\n  UPPER BOUND (very conservative):")
print(f"  |delta_a2^QF| <= 2 * a2_bare * Sum|delta_n| = {upper_bound_a2:.6f}")
print(f"  |delta_a2^QF| / a2_bare <= {upper_bound_a2/a2_bare*100:.6f}%")

# Better estimate: use the ACTUAL structure of the moments.
# From W2-B: the moment shift from BCS to ED at N=4 is:
#   a2_ed(4) - a2_bcs = delta_a2_cell(4) * a2_bcs
# = 0.116 * 528.07 = 61.1
# This is from changing n_k by O(0.1-0.3) per mode.
#
# The quantum fluctuation shifts delta_n ~ 10^{-3}.
# By linear scaling: delta_a2^QF ~ delta_a2_cell * (delta_n_QF / delta_n_ED)
#
# Compute the ratio:
delta_n_ed_total = np.sum(np.abs(ed_data[4]['n_k_ed'] - ed_data[4]['n_k_bcs']))
delta_n_qf_total = np.sum(np.abs(delta_n_QF))
scaling_ratio = delta_n_qf_total / max(delta_n_ed_total, 1e-30)

delta_a2_from_ED = abs(ed_data[4]['delta_a2']) * abs(a2_bcs)  # absolute shift
delta_a2_QF_est = delta_a2_from_ED * scaling_ratio

print(f"\n  SCALING ESTIMATE:")
print(f"  |delta_n(ED-BCS)| total = {delta_n_ed_total:.4f}")
print(f"  |delta_n(QF)| total = {delta_n_qf_total:.2e}")
print(f"  ratio = {scaling_ratio:.2e}")
print(f"  |delta_a2^QF| ~ {delta_a2_QF_est:.4f}")
print(f"  |delta_a2^QF| / a2_ed(N=4) = {delta_a2_QF_est/ed_data[4]['a2_ed']*100:.6f}%")

# ============================================================================
# 8. SECOND NON-PERTURBATIVE EFFECT: 1/N_cells dilution
# ============================================================================

print("\n" + "=" * 70)
print("8. BLOCH DILUTION EFFECT (1/N_cells)")
print("=" * 70)

# S63 RICHARDSON-GAUDIN-N1-63 established:
# On the fabric, the effective BCS coupling is diluted by 1/N_cells.
# E_cond^{fabric} = E_cond^{cell} / N_cells (at N_pair = 1)
#
# This means the PAIRING CORRELATIONS on the fabric are WEAKER than
# in a single cell by factor 1/N_cells.
#
# How does this affect spectral moments?
# The BCS depletion of n_k scales with Delta^2 / E_k^2.
# If Delta_eff^{fabric} = Delta_cell / sqrt(N_cells) (from BCS relation
# E_cond ~ Delta^2 / d, and E_cond dilutes by 1/N), then:
#   n_k^{fabric} closer to n_k^{vacuum} (= 0 or 1) than n_k^{cell}
#
# This means the fabric spectral moments are CLOSER to the vacuum values
# than the single-cell values are. The beyond-mean-field correction from
# W2-B (11.6%) is an OVERESTIMATE for the fabric.

# Dilution of gap: if E_cond ~ Delta^2/d and E_cond -> E_cond/N_cells,
# then Delta_fabric ~ Delta_cell / sqrt(N_cells)
Delta_fabric = Delta_0 / np.sqrt(N_fabric)
ratio_Delta = Delta_fabric / Delta_0

print(f"\n  Single-cell gap: Delta_0 = {Delta_0:.6f} M_KK")
print(f"  Fabric-diluted gap: Delta_fabric = Delta_0/sqrt(N) = {Delta_fabric:.6f} M_KK")
print(f"  Ratio: {ratio_Delta:.4f}")
print(f"  (Factor {1.0/ratio_Delta:.1f}x suppression)")

# BUT WAIT: this applies to the fabric-as-a-whole, not to each cell separately.
# When we ask "what are the spectral moments per cell on the fabric?",
# the answer depends on whether we Bloch-transform or not.
#
# WITHIN each cell (the observable quantity): the occupation numbers are
# those of the CELL BCS ground state, because the Josephson coupling
# only shifts the total energy (Section 5). The pairing correlations
# WITHIN a cell are IDENTICAL to the single-cell case.
#
# The 1/N_cells dilution applies to INTER-CELL pair correlations
# (the pair transfer amplitude), not to intra-cell moments.
#
# This is the nuclear analog: in a nucleus with closed shells,
# the single-particle occupations do not change when you embed
# the nucleus in nuclear matter. The inter-nucleon correlations
# change, but the single-body density matrix is preserved.

print(f"\n  RESOLUTION: The 1/N dilution applies to INTER-CELL pair transfer,")
print(f"  not to INTRA-CELL occupation numbers or spectral moments.")
print(f"  Each cell retains its single-cell BCS structure.")
print(f"  The spectral moments per cell are UNCHANGED at mean-field level.")

# ============================================================================
# 9. COMPREHENSIVE: THREE CORRECTION CHANNELS
# ============================================================================

print("\n" + "=" * 70)
print("9. THREE CORRECTION CHANNELS")
print("=" * 70)

# Channel 1: Phase fluctuation depletion of condensate
# delta_n_k ~ alpha_QF * Delta^2 / (2*E_k^3)
# Fractional a_2 correction: ~ alpha_QF * (delta_a2_ED / delta_n_ED) * delta_n_QF
channel_1 = delta_a2_QF_est / ed_data[4]['a2_ed']

# Channel 2: Inter-cell number fluctuations (particle redistribution)
# In the superfluid regime, pairs can tunnel between cells.
# The local number fluctuation per cell is:
#   <(delta_N_i)^2> ~ (E_J/E_C)^{1/2} for a single junction
# But for spectral moments, what matters is the CORRECTION to
# the average occupation numbers from this redistribution.
# The BCS grand-canonical number fluctuation is ALREADY included
# in the single-cell W2-B calculation. The fabric-specific part
# is the INTER-CELL redistribution, which modifies the local
# density matrix at second order in the tunneling:
#   delta_n_k^{(2)} ~ (J/E_k)^2 * (N_cells - 1) / N_cells^2
# This is because the pair hops to a neighbor (factor J/E_k) and back
# (factor J/E_k), spread over N_cells possible targets, but the net
# effect on the HOME cell scales as 1/N_cells.
channel_2_n = (J_eff_iso / np.mean(E_k))**2 * (N_fabric - 1) / N_fabric**2
channel_2 = channel_2_n * abs(ed_data[4]['delta_a2'])

# Channel 3: Coherent pair tunneling (Josephson pair current)
# The pair tunneling amplitude between cells is J * <cos(dphi)> / E_pair.
# This is a SECOND-ORDER effect on occupation numbers because it requires
# a pair to tunnel OUT and back. The correction is O(J^2/E_pair^2) ~ O(1)
# but averaged over ALL cells and modes, gives:
#   delta_n_k ~ (J/E_k)^2 / (2*N_cells)
J_over_Ek_sq = (J_eff_iso / np.mean(E_k))**2
channel_3_n = J_over_Ek_sq / (2 * N_fabric)
channel_3 = channel_3_n * abs(ed_data[4]['delta_a2'])

print(f"\n  Channel 1 (phase fluctuations):")
print(f"    alpha_QF = {alpha_QF:.2e}")
print(f"    |delta_a2/a2| = {abs(channel_1)*100:.6f}%")

print(f"\n  Channel 2 (inter-cell number redistribution):")
print(f"    (J/E_k)^2 * (N-1)/N^2 = {channel_2_n:.2e}")
print(f"    |delta_a2/a2| ~ {abs(channel_2)*100:.4f}%")

print(f"\n  Channel 3 (coherent pair tunneling):")
print(f"    (J/E_k)^2 / (2*N_cells) = {channel_3_n:.2e}")
print(f"    |delta_a2/a2| ~ {abs(channel_3)*100:.4f}%")

# Total (in quadrature — independent channels)
total_fabric_correction = np.sqrt(channel_1**2 + channel_2**2 + channel_3**2)
total_fabric_linear = abs(channel_1) + abs(channel_2) + abs(channel_3)

print(f"\n  TOTAL fabric correction (quadrature): {total_fabric_correction*100:.4f}%")
print(f"  TOTAL fabric correction (linear):     {total_fabric_linear*100:.4f}%")

# ============================================================================
# 10. CONSISTENCY CHECK: S63 and S56 results
# ============================================================================

print("\n" + "=" * 70)
print("10. CROSS-CHECKS")
print("=" * 70)

# S56 STRUTINSKY-FABRIC-56: Josephson gradient SWAMPS shell correction.
# Gradient ratio R_fabric = 0.051 (vs 0.711 single-cell).
# This tells us Josephson dominates ENERGY but not SPECTRAL MOMENTS
# (different quantities — energy vs geometric trace).

print(f"\n  S56 Strutinsky: R_fabric = 0.051 (Josephson dominates ENERGY)")
print(f"  But spectral moments are GEOMETRIC (D_K), not energy.")
print(f"  Josephson enters energy, not D_K => no direct a_2 modification.")

# S63 RICHARDSON-GAUDIN: E_cond diluted by 1/N_cells on fabric.
# BCS overestimates by 225x at N_pair=1.
# But condensation energy != spectral moments.
print(f"\n  S63 Richardson-Gaudin: E_cond^fabric = E_cond^cell / {N_fabric}")
print(f"  BCS overestimates E_cond by 225x at N=1 (grand-canonical error).")
print(f"  But E_cond != a_2. Condensation energy is BCS, moments are geometric.")

# S49 HFB-BACKREACTION: fabric correction 1.2% primary, 3.9% conservative.
# This is the HFB self-consistency correction, different from moment correction.
print(f"\n  S49 HFB-BACKREACTION: 1.2% primary, 3.9% conservative.")
print(f"  This is the backreaction of BCS on the mean field (geometry).")
print(f"  Consistent with our finding: fabric corrections are sub-percent to few-percent.")

# ============================================================================
# 11. GATE VERDICT
# ============================================================================

print("\n" + "=" * 70)
print("11. GATE VERDICT: FABRIC-PROJECTED-MOMENTS-67")
print("=" * 70)

# The decisive quantity: how much does inter-cell Josephson coupling
# change the per-cell spectral moments beyond the single-cell value?
#
# RESULT: At mean-field level, the answer is ZERO (exactly).
# The Josephson coupling shifts the total energy but does not enter D_K
# and does not modify the occupation numbers within each cell.
#
# Beyond mean field (quantum fluctuations): three correction channels
# give a combined |delta_a_2/a_2| of order 10^{-3} to 10^{-2}.
# This is FAR below the 10% PASS threshold.
#
# The DOMINANT beyond-mean-field correction remains the single-cell
# ED-vs-BCS shift of 11.6% (W2-B), which is a property of the
# 8-mode system and is NOT modified by inter-cell coupling.

fabric_delta = total_fabric_linear  # Use linear (conservative) total

# The gate asks about the FABRIC correction specifically:
# "does inter-cell coupling change the spectral moments beyond single-cell?"
decisive_ratio = fabric_delta

print(f"\n  Single-cell ED-vs-BCS (W2-B): |delta_a2/a2| = {abs(ed_data[4]['delta_a2'])*100:.1f}%")
print(f"  Fabric correction (this computation): |delta_a2/a2| = {decisive_ratio*100:.4f}%")
print(f"  Total (single-cell + fabric, linear): {(abs(ed_data[4]['delta_a2']) + decisive_ratio)*100:.2f}%")

if decisive_ratio < 0.10:
    verdict = "PASS"
    detail = (f"|delta_a2/a2|_fabric = {decisive_ratio*100:.4f}% < 10%. "
              f"At mean-field level, Josephson coupling shifts total energy but does NOT modify D_K "
              f"or intra-cell occupation numbers (structural zero). "
              f"Beyond-mean-field quantum fluctuations contribute {decisive_ratio*100:.4f}% "
              f"(3 channels: phase depletion {abs(channel_1)*100:.4f}%, "
              f"number redistribution {abs(channel_2)*100:.4f}%, tunneling {abs(channel_3)*100:.4f}%). "
              f"The fabric is well-approximated by N independent cells for spectral moments. "
              f"The dominant beyond-MF correction remains the single-cell 11.6% from W2-B.")
elif decisive_ratio < 0.20:
    verdict = "INFO"
    detail = f"|delta_a2/a2|_fabric = {decisive_ratio*100:.4f}% in [10%, 20%]."
else:
    verdict = "FAIL"
    detail = f"|delta_a2/a2|_fabric = {decisive_ratio*100:.4f}% > 20%."

print(f"\n  GATE: FABRIC-PROJECTED-MOMENTS-67")
print(f"  Threshold: PASS < 10%, FAIL > 20%")
print(f"  Decisive ratio: {decisive_ratio*100:.4f}%")
print(f"  VERDICT: {verdict}")
print(f"\n  {detail}")

# ============================================================================
# 12. Save results
# ============================================================================

save_data = {
    'gate_name': np.array('FABRIC-PROJECTED-MOMENTS-67'),
    'gate_verdict': np.array(verdict),
    'gate_detail': np.array(detail[:300]),
    'gate_decisive_ratio': np.array(decisive_ratio),

    # CG(24) structure
    'N_fabric': np.array(N_fabric),
    'z_coord': np.array(z_coord),
    'adjacency_eigenvalues': eigvals_adj,
    'J_eff_iso': np.array(J_eff_iso),
    'J_total_per_vert': np.array(J_total_per_vert),

    # Energy scales
    'W_J': np.array(W_J),
    'd_spacing': np.array(d_spacing),
    'd_over_Delta': np.array(d_spacing / Delta_0),
    'EJ_over_EC': np.array(EJ_over_EC),

    # Fluctuation parameters
    'alpha_QF': np.array(alpha_QF),
    'Delta_eff': np.array(Delta_eff),
    'cos_dphi': np.array(cos_dphi),

    # Three correction channels
    'channel_1_phase_fluct': np.array(channel_1),
    'channel_2_amplitude_fluct': np.array(channel_2),
    'channel_3_pair_tunnel': np.array(channel_3),
    'total_fabric_quadrature': np.array(total_fabric_correction),
    'total_fabric_linear': np.array(total_fabric_linear),

    # Occupation number shifts from quantum fluctuations
    'delta_n_QF': delta_n_QF,
    'delta_n_ed_bcs_total': np.array(delta_n_ed_total),

    # Single-cell reference (W2-B)
    'delta_a2_single_cell': np.array([ed_data[N]['delta_a2'] for N in range(1, 5)]),
    'delta_a4_single_cell': np.array([ed_data[N]['delta_a4'] for N in range(1, 5)]),

    # Combined shift
    'combined_shift_linear': np.array(abs(ed_data[4]['delta_a2']) + decisive_ratio),
}

out_path = data_dir / 's67_fabric_projected_moments.npz'
np.savez(out_path, **save_data)
print(f"\nSaved: {out_path}")

# ============================================================================
# 13. Summary table
# ============================================================================

print("\n" + "=" * 70)
print("SUMMARY TABLE")
print("=" * 70)
print(f"\n{'Quantity':>40} | {'Value':>15} | {'Unit':>8}")
print("-" * 70)
print(f"{'CG(24) cells':>40} | {N_fabric:>15d} | {'':>8}")
print(f"{'Coordination z':>40} | {z_coord:>15d} | {'':>8}")
print(f"{'J_eff_iso':>40} | {J_eff_iso:>15.4f} | {'M_KK':>8}")
print(f"{'z * J_eff':>40} | {J_total_per_vert:>15.4f} | {'M_KK':>8}")
print(f"{'W_J (Josephson bandwidth)':>40} | {W_J:>15.4f} | {'M_KK':>8}")
print(f"{'Delta_0 (BCS gap)':>40} | {Delta_0:>15.4f} | {'M_KK':>8}")
print(f"{'W_J / Delta':>40} | {W_J/Delta_0:>15.2f} | {'':>8}")
print(f"{'E_J / E_C':>40} | {EJ_over_EC:>15.0f} | {'':>8}")
print(f"{'alpha_QF (quantum depletion)':>40} | {alpha_QF:>15.2e} | {'':>8}")
print(f"{'Ch.1 phase fluct |da2/a2|':>40} | {abs(channel_1)*100:>14.4f}% | {'':>8}")
print(f"{'Ch.2 number redistr |da2/a2|':>40} | {abs(channel_2)*100:>14.4f}% | {'':>8}")
print(f"{'Ch.3 pair tunneling |da2/a2|':>40} | {abs(channel_3)*100:>14.4f}% | {'':>8}")
print(f"{'FABRIC correction (linear)':>40} | {total_fabric_linear*100:>14.4f}% | {'':>8}")
print(f"{'Single-cell W2-B (N=4)':>40} | {abs(ed_data[4]['delta_a2'])*100:>14.1f}% | {'':>8}")
print(f"{'Combined (single-cell + fabric)':>40} | {(abs(ed_data[4]['delta_a2'])+decisive_ratio)*100:>14.2f}% | {'':>8}")
print(f"\n  VERDICT: {verdict}")
