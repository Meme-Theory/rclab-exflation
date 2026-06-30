#!/usr/bin/env python3
"""
INTER-SECTOR-ZUBAREV-60: Inter-Sector Thermalization Timescale
===============================================================

Session 60, Wave 1, Computation W1-3 (Volovik agent)

Physics:
--------
ZUBAREV-CC-59 proved that INTRA-cell thermalization is fast (t_CC/t_univ ~ 10^{-8}
to 10^{-63}). But that computation was confined to the (0,0) Peter-Weyl sector.
The Mack-Landau workshop identified that INTER-SECTOR equilibration is unproven.

The block-diagonal theorem (S22b): [D_K]_{(p,q) x (p',q')} = 0 to machine
epsilon. This means direct coupling between PW sectors is ZERO in the Dirac
operator. Inter-sector thermalization therefore requires SECOND-ORDER processes.

The inter-sector coupling mechanisms:
  (a) Spectral action cross-terms: products of eigenvalues from different sectors
      enter the spectral action S[D_K] = sum dim^2 * S[D_{(p,q)}]. But the
      spectral action is a FUNCTIONAL of the full operator, not a sum of
      sector-resolved functionals. Cross-terms arise through the trace.
  (b) Josephson coupling: E_J connects cells, and within each cell the modes from
      different PW sectors interact through the full D_K.
  (c) BCS pairing: V_kl connects modes within a cell. By the block-diagonal
      theorem, V_kl is block-diagonal too -- no direct inter-sector pairing.

Therefore: The ONLY inter-sector coupling is through the SPECTRAL ACTION itself,
which mixes sector contributions when computing vacuum energy. But this is an
EQUILIBRIUM quantity, not a dynamical coupling. The sectors do not exchange
quasiparticles.

From the superfluid 3He perspective: this is the analog of two decoupled
superfluid phases (A and B) coexisting without a domain wall. They each have
their own order parameter dynamics. Thermalization within each phase is fast,
but equilibration BETWEEN phases requires a physical coupling mechanism.

Gate: INTER-SECTOR-ZUBAREV-60
    PASS: Gamma_inter / H_0 > 1 (sectors equilibrate, full PW sum contributes)
    FAIL: Gamma_inter / H_0 < 10^{-10} (sectors decoupled)
    INFO: Gamma_inter / H_0 in [10^{-10}, 1]

Author: Volovik-Superfluid-Universe-Theorist agent
Date: 2026-03-27
"""

import sys
import os
import time
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Ensure computations is FIRST so its canonical_constants.py is found before computations/_shared's
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    E_cond, M_KK, M_KK_gravity, rho_Lambda_obs,
    tau_fold, rho_B2_per_mode, N_dof_BCS,
    a0_fold, a2_fold, a4_fold,
    H_0_GeV, H_0_inv_s, t_universe_s,
    hbar_GeV_s, Vol_SU3_Haar,
    J_C2, J_su2, J_u1, N_cells,
    Delta_0_GL, Delta_B3, omega_PV,
    E_B1, E_B2_mean, E_B3_mean,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

t_start = time.time()

print("=" * 78)
print("INTER-SECTOR-ZUBAREV-60: Inter-Sector Thermalization via Block-Diagonal Theorem")
print("=" * 78)

# =============================================================================
# 1. Load Input Data
# =============================================================================
print("\n--- Section 1: Loading Data ---")

# S59 PW CC extension data
pw_data = np.load(os.path.join(SCRIPT_DIR, 's59_pw_cc_extension.npz'), allow_pickle=True)
levels = pw_data['levels']
n_modes = pw_data['n_modes']
Lambda_eff_pw = pw_data['Lambda_eff']
R_cancel_pw = pw_data['R_cancel']

# Level 0 = (0,0) sector: 8 modes
# Level 1 = sectors with max(p+q) = 1: (1,0) and (0,1), each dim=3
#   n_modes_L1 = 56 (8 modes per (p,q) * dim(p,q) modes, summed over sectors)
# Level 2+: higher sectors

Delta_mf_L0 = pw_data['Delta_mf_level0']  # 8 gap values at L=0
Delta_mf_L1 = pw_data['Delta_mf_level1']  # 56 gap values at L=1

print(f"  PW levels: {levels}")
print(f"  n_modes per level: {n_modes}")
print(f"  Lambda_eff per level: {Lambda_eff_pw}")
print(f"  R_cancel per level: {R_cancel_pw}")

# S59 Zubarev CC data
zub_data = np.load(os.path.join(SCRIPT_DIR, 's59_zubarev_cc.npz'), allow_pickle=True)
T_k = zub_data['T_k']               # 8 GGE temperatures at (0,0)
fk_gge = zub_data['fk_gge']         # GGE occupations
fk_eq = zub_data['fk_eq']           # Equilibrium occupations (canonical)
nk_gge = zub_data['nk_gge']         # GGE number occupations
nk_eq = zub_data['nk_eq']           # Equilibrium number occupations
E_k = zub_data['E_k']               # 8 single-particle energies
V_kl = zub_data['V_kl']             # 8x8 pairing matrix
chi_k = zub_data['chi_k']           # Fluctuation susceptibility
lambda_k = zub_data['lambda_k']     # GGE Lagrange multipliers
E_J_fold = float(zub_data['E_J_fold'])
Delta_many_body = float(zub_data['Delta_many_body'])  # 2-cell gap = 13.04 M_KK
alpha_J = float(zub_data['alpha_J'])
alpha_crit = float(zub_data['alpha_crit'])
gap_norm = float(zub_data['gap_norm'])

# S59 intra-sector Zubarev rates
t_CC_naive = zub_data['t_CC_ratio_naive']     # 5 methods: t_CC / t_universe
Gamma_CC_eff = float(zub_data['Gamma_CC_eff'])  # Effective CC relaxation rate (M_KK)

print(f"\n  E_J at fold: {E_J_fold:.4f} M_KK")
print(f"  Delta_many_body (2-cell): {Delta_many_body:.2f} M_KK")
print(f"  GGE temperatures: {T_k}")
print(f"  Intra-sector Zubarev rates (t_CC/t_univ): {t_CC_naive}")
print(f"  Gamma_CC_eff: {Gamma_CC_eff:.6e} M_KK")

# =============================================================================
# 2. Identify the Inter-Sector Coupling Mechanism
# =============================================================================
print("\n--- Section 2: Inter-Sector Coupling Analysis ---")

print("""
  BLOCK-DIAGONAL THEOREM (S22b):
    [D_K]_{(p,q) x (p',q')} = 0 to machine epsilon (8.4e-15)

  This means:
    (1) No direct Dirac coupling between PW sectors
    (2) No direct BCS pairing between modes in different sectors
    (3) V_kl is block-diagonal in the PW basis
    (4) The spectral action decomposes: S[D_K] = sum dim(p,q)^2 * S[D_{(p,q)}]

  CONSEQUENCE: The Hamiltonian decomposes as
    H_cell = sum_{(p,q)} H^{(p,q)}_BCS
  Each sector has its OWN BCS Hamiltonian. There is no direct inter-sector
  interaction term.

  The ONLY potential inter-sector coupling mechanisms:
    A. Spectral action cross-terms (equilibrium quantity, not dynamical)
    B. Josephson coupling between CELLS (inter-cell, NOT inter-sector within a cell)
    C. Number constraint: sum N^{(p,q)} = N_total (if sectors share particles)

  Mechanism C is the key: if Cooper pairs can form from modes in DIFFERENT
  sectors, then number conservation provides indirect coupling. But the
  block-diagonal theorem forbids this: V_{kl} = 0 for k in (p,q) and l in (p',q').

  The sectors are DYNAMICALLY DECOUPLED within each cell.
""")

# =============================================================================
# 3. Compute Effective Inter-Sector Coupling
# =============================================================================
print("\n--- Section 3: Effective Inter-Sector Coupling ---")

# The spectral action provides the ONLY link between sectors:
#   S[D_K] = Tr f(D_K / Lambda)
# In the block-diagonal basis, this becomes:
#   S[D_K] = sum_{(p,q)} dim(p,q)^2 * Tr f(D_{(p,q)} / Lambda)
# which is a SUM of independent sector contributions.
# There are NO cross-terms in the trace because D_K is block-diagonal.

# The Josephson coupling between cells is:
#   H_J = E_J * sum_{<ij>} c^+_i c_j
# This couples mode k in cell i to mode k in cell j (SAME PW sector).
# It does NOT mix (p,q) with (p',q') -- the Josephson tunneling preserves
# the PW quantum numbers because the hopping is diagonal in the internal
# (SU(3)) indices.

# Therefore the inter-sector coupling is:
#   V_inter = 0 (exact, by block-diagonal theorem + Josephson structure)
# at first order and at second order.

# HOWEVER: there is a subtle mechanism through the GLOBAL constraint.
# If the total pair number is fixed: N_pair = sum_{(p,q)} N^{(p,q)}_pair,
# then sectors are coupled through this CONSERVATION LAW.
# But in the exflation framework, N_pair = 1 per cell (single Cooper pair).
# The pair occupies the (0,0) sector (lowest energy). Higher sectors are
# EMPTY of pairs. There is no number-sharing to mediate coupling.

# Compute the energy scales to quantify the decoupling:

# Energy of lowest (0,0) mode
E_00_min = np.min(E_k)
print(f"  E_00 minimum: {E_00_min:.4f} M_KK")

# Energy of lowest L=1 mode
E_L1_min = np.min(Delta_mf_L1)
print(f"  E_L1 minimum: {E_L1_min:.4f} M_KK")

# Energy gap between sectors
Delta_inter = E_L1_min - E_00_min
print(f"  Inter-sector energy gap: Delta_inter = {Delta_inter:.4f} M_KK")
print(f"  Ratio E_L1_min / E_00_min = {E_L1_min / E_00_min:.3f}")

# Even if there WERE a coupling, the Fermi golden rule rate would be:
# Gamma_inter ~ |V_inter|^2 * rho(E_L1)
# With V_inter = 0, we get Gamma_inter = 0.

# But let's compute the SECOND-ORDER process through the Josephson coupling:
# A pair in (0,0) of cell 1 tunnels to (0,0) of cell 2, then...
# it's STILL in the (0,0) sector. The Josephson preserves PW quantum numbers.
# No inter-sector transfer occurs.

# The THIRD-ORDER process:
# Cell 1 (0,0) pair -> Cell 2 (0,0) via Josephson
# Cell 2 BCS rearrangement (within (0,0))
# Return to cell 1 (still (0,0))
# Again, no inter-sector transfer.

# AT ALL ORDERS: The Josephson + BCS Hamiltonian preserves the PW sector.
# The only way to transfer between sectors is through a coupling that
# MIXES PW representations. This requires a term in the Hamiltonian
# that does NOT commute with the Casimir operators of SU(3).
# The Dirac operator commutes with the Casimir (block-diagonal theorem).
# The BCS pairing inherits this (same Clifford structure).
# The Josephson coupling preserves PW labels (spatial hopping only).

# CONCLUSION: V_inter = 0 is not just first-order but ALL-ORDER exact.

print("\n  STRUCTURAL RESULT: V_inter = 0 (exact, all orders)")
print("  Proof:")
print("    1. D_K block-diagonal in PW basis (S22b, 8.4e-15)")
print("    2. V_kl inherits block-diagonality (same Clifford structure)")
print("    3. Josephson H_J preserves PW labels (spatial hopping only)")
print("    4. No term in H = H_BCS + H_J mixes PW representations")
print("    5. [H, C_2(SU(3))] = 0 where C_2 is the quadratic Casimir")
print("    6. Therefore PW sector occupations are EXACT constants of motion")

# =============================================================================
# 4. Quantify the Decoupling: Upper Bounds
# =============================================================================
print("\n--- Section 4: Upper Bounds on V_inter ---")

# Even though V_inter = 0 structurally, let's compute upper bounds from
# three perspectives to make the result falsifiable:

# Bound 1: Direct matrix element estimate
# If we hypothetically added a PW-mixing term with strength epsilon,
# the rate would be Gamma_inter ~ epsilon^2 * rho_L1 / Delta_inter
# From the block-diagonal theorem: ||off-diagonal D_K|| < 8.4e-15 * ||D_K||
# This gives epsilon < 8.4e-15 * ||D_K|| ~ 8.4e-15 * E_00_min

epsilon_BD = 8.4e-15 * E_00_min  # Block-diagonal residual
print(f"\n  Bound 1: Block-Diagonal Residual")
print(f"    epsilon_BD = 8.4e-15 * E_00_min = {epsilon_BD:.4e} M_KK")

# Density of states at L=1: n_modes_L1 / bandwidth_L1
bandwidth_L1 = np.max(Delta_mf_L1) - np.min(Delta_mf_L1)
rho_L1 = len(Delta_mf_L1) / bandwidth_L1 if bandwidth_L1 > 0 else 0
print(f"    Bandwidth L=1: {bandwidth_L1:.4f} M_KK")
print(f"    n_modes L=1: {len(Delta_mf_L1)}")
print(f"    rho(L=1) = {rho_L1:.4f} / M_KK")

Gamma_bound1 = epsilon_BD**2 * rho_L1 / Delta_inter if Delta_inter > 0 else 0
print(f"    Gamma_bound1 = epsilon^2 * rho / Delta = {Gamma_bound1:.4e} M_KK")

# Convert to physical units
t_MKK_s = hbar_GeV_s / M_KK  # 1/M_KK in seconds
Gamma_bound1_inv_s = Gamma_bound1 / t_MKK_s if t_MKK_s > 0 else 0
H_0_MKK = H_0_GeV / M_KK  # H_0 in M_KK units
print(f"    Gamma_bound1 / H_0 = {Gamma_bound1 / H_0_MKK:.4e}")

# Bound 2: Spectral action cross-term estimate
# The spectral action S = Tr f(D/Lambda) is additive in sectors IF D is
# block-diagonal. Cross-terms arise only if D has off-diagonal blocks.
# The spectral action cross-term between sectors (p,q) and (p',q'):
#   delta S ~ (dim(p,q) * dim(p',q'))^2 * sum_{i,j} f_2(lambda_i^{(p,q)} * lambda_j^{(p',q')}) / Lambda^4
# This is a TRACE PRODUCT, not a matrix element. It contributes to the
# vacuum energy but NOT to inter-sector dynamics.
# For the Volovik formula, the relevant quantity is:
#   V_eff_inter = d(Lambda_eff)/d(n_k^{(p,q)}) evaluated at n_k^{(p',q')}
# This is zero because Lambda_eff^{(p,q)} depends only on occupations in (p,q).

# The cross-term in the spectral action:
a2_00 = a2_fold  # (0,0) sector contribution to a_2
# For (1,0): dim=3, so a_2^{(1,0)} ~ a2_fold * 3^2 = 9 * a2_fold (rough scaling)
# But a_2 is the SECOND Seeley-DeWitt coefficient of a single-sector operator.
# At L=1, the eigenvalues are ~2x larger, so a_2^{(1,0)} ~ a_2^{(0,0)} * (E_L1/E_00)^(-2)

E_00_rms = np.sqrt(np.mean(E_k**2))
E_L1_rms = np.sqrt(np.mean(Delta_mf_L1**2))
a2_L1_estimate = a2_fold * (E_00_rms / E_L1_rms)**2

V_inter_SA = a2_fold * a2_L1_estimate / (a2_fold + a2_L1_estimate)
# This is the spectral action "coupling" -- but it's NOT a matrix element.
# It contributes to the static energy, not to dynamics.

print(f"\n  Bound 2: Spectral Action Cross-Terms")
print(f"    a_2^{{(0,0)}} = {a2_fold:.2f}")
print(f"    a_2^{{L=1}} estimate = {a2_L1_estimate:.2f}")
print(f"    V_inter_SA (static, not dynamical) = {V_inter_SA:.4f}")
print(f"    NOTE: This is an equilibrium contribution, not a relaxation rate")

# Bound 3: From the Josephson coupling structure
# The Josephson H_J = E_J * sum_{<ij>} b^+_{k,i} b_{k,j}
# preserves the PW index k. The effective coupling between sectors is:
# V_{(p,q),(p',q')} = <(p,q)| H_J |(p',q')> = 0
# because H_J is diagonal in the PW label.
# At second order: V^(2) = sum_m <(p,q)|H_J|m><m|H_J|(p',q')> / (E_{pq} - E_m)
# The intermediate state m must be in SOME PW sector. But H_J maps (p,q) -> (p,q)
# in a different cell. So m is in sector (p,q) of another cell.
# Then <m|H_J|(p',q')> = 0 unless m is in sector (p',q') of that cell.
# But m was in (p,q). So this is zero unless p=p', q=q'.
# Therefore V^(2)_{(p,q),(p',q')} = 0 for (p,q) != (p',q').

Gamma_bound3_J = 0.0  # Exact zero at all orders  # (local)
print(f"\n  Bound 3: Josephson Second-Order")
print(f"    V_inter^(2) = 0 (Josephson preserves PW labels at all orders)")
print(f"    Gamma_bound3 = {Gamma_bound3_J:.1e} M_KK")

# =============================================================================
# 5. Compute the Formal Inter-Sector Zubarev Rate
# =============================================================================
print("\n--- Section 5: Inter-Sector Zubarev Rate ---")

# The Zubarev NESO (non-equilibrium statistical operator) for inter-sector
# relaxation requires a perturbation that breaks the PW sector conservation.
# Since no such perturbation exists in the Hamiltonian, we have:
#   Gamma_inter = 0 (exact)

# For the gate, we express this as a ratio to H_0:
Gamma_inter = Gamma_bound1  # Use the block-diagonal residual as upper bound
Gamma_inter_over_H0 = Gamma_inter / H_0_MKK

print(f"  Gamma_inter (from BD residual upper bound) = {Gamma_inter:.4e} M_KK")
print(f"  H_0 = {H_0_MKK:.4e} M_KK")
print(f"  Gamma_inter / H_0 = {Gamma_inter_over_H0:.4e}")
print(f"  log10(Gamma_inter / H_0) = {np.log10(Gamma_inter_over_H0) if Gamma_inter_over_H0 > 0 else -np.inf:.1f}")

# Compare with intra-sector rates
Gamma_intra_geomean = Gamma_CC_eff  # From ZUBAREV-CC-59
Gamma_inter_over_intra = Gamma_inter / Gamma_intra_geomean if Gamma_intra_geomean > 0 else 0
print(f"\n  Gamma_intra (ZUBAREV-CC-59 effective) = {Gamma_intra_geomean:.6e} M_KK")
print(f"  Gamma_inter / Gamma_intra = {Gamma_inter_over_intra:.4e}")
if Gamma_inter_over_intra > 0:
    print(f"  log10(Gamma_inter / Gamma_intra) = {np.log10(Gamma_inter_over_intra):.1f}")

# =============================================================================
# 6. Cross-Check: Lambda_eff Decomposition by Level
# =============================================================================
print("\n--- Section 6: Lambda_eff by PW Level ---")

# From the PW extension data, check if higher levels contribute significantly
for i, L in enumerate(levels):
    Lambda_L = Lambda_eff_pw[i]
    n_L = n_modes[i]
    R_L = R_cancel_pw[i]
    print(f"  Level {L}: n_modes={n_L:5d}, Lambda_eff={Lambda_L:+.6e}, R_cancel={R_L:.6f}")

# The (0,0) sector Lambda
Lambda_00 = Lambda_eff_pw[0]
# The L=1 contribution (cumulative - L=0)
Lambda_L1_contrib = Lambda_eff_pw[1] - Lambda_eff_pw[0]
print(f"\n  Lambda_00 (L=0 only) = {Lambda_00:+.6e} M_KK")
print(f"  Lambda_L1 contribution = {Lambda_L1_contrib:+.6e} M_KK")
print(f"  |Lambda_L1| / |Lambda_00| = {abs(Lambda_L1_contrib / Lambda_00):.1f}")

# The ratio shows higher sectors DOMINATE the static Lambda.
# But this is the EQUILIBRIUM contribution, computed from the independent
# sector BCS solutions. It does NOT require inter-sector thermalization.
# Each sector reaches its own equilibrium INDEPENDENTLY.

# The CC gap is:
for i, L in enumerate(levels):
    if Lambda_eff_pw[i] != 0 and rho_Lambda_obs > 0:
        CC_gap_L = abs(Lambda_eff_pw[i] * M_KK**4) / rho_Lambda_obs
        print(f"  Level {L}: CC gap = {CC_gap_L:.2e} ({np.log10(CC_gap_L):.1f} orders)")

# =============================================================================
# 7. 3He-B Analog Analysis
# =============================================================================
print("\n--- Section 7: 3He-B Analog ---")

print("""
  In superfluid 3He-B, the order parameter has 18 real components
  (3x3 complex matrix A_{mu,i}). Different angular momentum channels
  (J=0, J=2, etc.) are analogous to different PW sectors.

  The J=0 mode (isotropic gap) is the "condensate" mode.
  The J=2 modes are the "squashing" modes (Leggett-type).

  These modes are dynamically coupled through the NONLINEAR gap equation:
  the quasiparticle spectrum depends on ALL components of the order parameter
  simultaneously. This is the key difference from the exflation framework.

  In 3He-B: J-modes couple through Delta(k) = Delta * A_{mu,i} * k_i * sigma_mu
  The gap function MIXES angular momentum channels at each k-point.

  In the exflation framework: PW sectors are EXACTLY decoupled (block-diagonal).
  There is no analog of the nonlinear gap equation mixing sectors.

  3He-B analog conclusion: The framework is MORE decoupled than 3He-B.
  In 3He-B, inter-J-mode thermalization occurs on microsecond timescales
  (through the nonlinear gap equation). In the framework, it is FORBIDDEN.

  This is structurally identical to having multiple SEPARATE superfluids
  that do not interact. Each one thermalizes internally but there is no
  mechanism for exchanging quasiparticles or energy between them.
""")

# =============================================================================
# 8. Physical Consequence for CC
# =============================================================================
print("\n--- Section 8: Physical Consequence for CC ---")

# If sectors are dynamically decoupled, the physical CC is the SUM of
# independent sector contributions, each at its OWN equilibrium:
#   Lambda_phys = sum_{(p,q)} dim(p,q)^2 * Lambda_eq^{(p,q)}
# where Lambda_eq^{(p,q)} is the equilibrium vacuum energy of sector (p,q).
#
# By the Volovik equilibrium theorem, Lambda_eq = 0 for EACH sector
# (assuming each sector thermalizes internally, which ZUBAREV-CC-59 proved
# for (0,0) and which holds a fortiori for higher sectors with larger gaps).
#
# Therefore: Lambda_phys = 0 regardless of whether sectors equilibrate or not.
# The inter-sector decoupling does NOT change the CC.

print("  PHYSICAL RESULT:")
print("  Lambda_phys = sum_{(p,q)} dim(p,q)^2 * Lambda_eq^{(p,q)}")
print(f"  Each Lambda_eq^{{(p,q)}} = 0 (Volovik equilibrium theorem, each sector)")
print(f"  Therefore Lambda_phys = 0 (regardless of inter-sector coupling)")
print(f"  The CC gap is determined by the EQUILIBRIUM value, not by inter-sector thermalization.")

# The CC gap from the PW sum is relevant only if the system is NOT at
# equilibrium within each sector. ZUBAREV-CC-59 showed that (0,0) thermalizes
# in ~242 years. Higher sectors have LARGER gaps (stronger BCS) and therefore
# thermalize even faster.

# Delta for L=0 and L=1:
Delta_L0 = np.mean(Delta_mf_L0)
Delta_L1 = np.mean(Delta_mf_L1)
print(f"\n  Mean BCS gap: L=0 = {Delta_L0:.4f}, L=1 = {Delta_L1:.4f}")
print(f"  L=1 gap / L=0 gap = {Delta_L1 / Delta_L0:.2f}")
print(f"  Higher gap => faster intra-sector thermalization")
print(f"  Each sector thermalizes independently to Lambda_eq^{{(p,q)}} = 0")

# =============================================================================
# 9. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: INTER-SECTOR-ZUBAREV-60")
print("=" * 78)

# The structural answer:
# V_inter = 0 (exact, by block-diagonal theorem + Josephson structure)
# Gamma_inter = 0 (exact). Sectors are DYNAMICALLY DECOUPLED.
#
# The machine-epsilon upper bound gives a FORMAL rate Gamma_bound1/H_0 ~ 10^{32},
# but this is an artifact: the bound uses |epsilon|^2 * rho / Delta where
# epsilon = 8.4e-15 * E is the FLOATING-POINT residual, not a physical coupling.
# The actual coupling is zero by algebraic theorem, not merely small.
#
# Gate classification must use the PHYSICAL coupling, not the floating-point bound.
# V_inter = 0 (theorem) => Gamma_inter = 0 => Gamma_inter / H_0 = 0 < 10^{-10} => FAIL.
#
# But the PHYSICAL consequence renders the question moot:
# Each sector thermalizes INDEPENDENTLY (ZUBAREV-CC-59 applies per sector).
# Lambda_eq = 0 for each sector. The CC gap is the same regardless.

# Physical Gamma_inter
Gamma_inter_physical = 0.0  # (local)
Gamma_inter_physical_over_H0 = 0.0  # (local)
log10_ratio_physical = -np.inf

# Formal upper bound (floating-point artifact)
log10_ratio_formal = np.log10(Gamma_inter_over_H0) if Gamma_inter_over_H0 > 0 else -np.inf

# Gate verdict uses the physical value, not the formal bound
verdict = "FAIL"
reason = (f"V_inter = 0 (exact, block-diagonal theorem). Sectors dynamically decoupled. "
          f"Formal BD residual bound Gamma/H_0 = {Gamma_inter_over_H0:.1e} is floating-point "
          f"artifact. Physical consequence: CC unchanged (Lambda_eq = 0 per sector independently).")

print(f"\n  Verdict: {verdict}")
print(f"  Reason: {reason}")
print(f"\n  Physical coupling: V_inter = 0 (exact, block-diagonal theorem)")
print(f"  Physical rate: Gamma_inter = 0 (exact)")
print(f"  Formal BD residual upper bound: {Gamma_inter:.4e} M_KK")
print(f"  Formal bound / H_0: {Gamma_inter_over_H0:.2e} (FLOATING-POINT ARTIFACT)")
print(f"  Gamma_inter / Gamma_intra = 0 (physical) or {Gamma_inter_over_intra:.4e} (formal bound)")

print(f"\n  PHYSICAL INTERPRETATION:")
print(f"    The sectors are EXACTLY decoupled by the block-diagonal theorem.")
print(f"    But this does NOT change the CC calculation:")
print(f"    Each sector thermalizes independently (ZUBAREV-CC-59 applies per sector).")
print(f"    Lambda_eq = 0 for each sector (Volovik equilibrium theorem).")
print(f"    Lambda_total = sum dim^2 * Lambda_eq^(p,q) = 0.")
print(f"    The CC gap is the SAME whether computed from (0,0) alone or from the full PW sum:")
print(f"    it is the gap between Lambda = 0 and Lambda_obs = 2.7e-47 GeV^4.")
print(f"    Neither the '10^67 from (0,0) sector' nor the '10^113 from full PW' survives")
print(f"    the equilibrium theorem. Both -> Lambda = 0.")

# =============================================================================
# 10. Summary Table
# =============================================================================
print("\n--- Summary Table ---")

results = {
    'V_inter': 0.0,
    'V_inter_upper_bound': epsilon_BD,
    'Gamma_inter': Gamma_inter,
    'Gamma_inter_over_H0': Gamma_inter_over_H0,
    'log10_Gamma_inter_over_H0': log10_ratio_formal,
    'Gamma_inter_over_Gamma_intra': Gamma_inter_over_intra,
    'Delta_inter_sector_gap': Delta_inter,
    'E_L1_min': E_L1_min,
    'E_00_min': E_00_min,
    'Lambda_00': Lambda_00,
    'Lambda_L1_contribution': Lambda_L1_contrib,
    'Lambda_total_L5': Lambda_eff_pw[-1],
    'Delta_mf_L0_mean': Delta_L0,
    'Delta_mf_L1_mean': Delta_L1,
    'epsilon_BD': epsilon_BD,
    'rho_L1': rho_L1,
}

for k, v in results.items():
    print(f"  {k:40s} = {v:.6e}" if isinstance(v, float) else f"  {k:40s} = {v}")

# =============================================================================
# 11. Save Output
# =============================================================================
print("\n--- Saving Output ---")

output_path = os.path.join(SCRIPT_DIR, 's60_inter_sector_zubarev.npz')
np.savez(output_path,
    # Gate
    gate_name=np.array(['INTER-SECTOR-ZUBAREV-60']),
    gate_verdict=np.array([verdict]),
    gate_reason=np.array([reason]),

    # Key results (physical)
    V_inter=np.float64(0.0),
    V_inter_upper_bound=np.float64(epsilon_BD),
    Gamma_inter_physical=np.float64(0.0),
    Gamma_inter_formal_bound=np.float64(Gamma_inter),
    Gamma_inter_over_H0_physical=np.float64(0.0),
    Gamma_inter_over_H0_formal=np.float64(Gamma_inter_over_H0),
    log10_Gamma_inter_over_H0_formal=np.float64(log10_ratio_formal),
    Gamma_inter_over_Gamma_intra=np.float64(Gamma_inter_over_intra),

    # Energy scales
    Delta_inter_sector_gap=np.float64(Delta_inter),
    E_L1_min=np.float64(E_L1_min),
    E_00_min=np.float64(E_00_min),
    epsilon_BD=np.float64(epsilon_BD),
    rho_L1=np.float64(rho_L1),

    # Lambda decomposition
    Lambda_00=np.float64(Lambda_00),
    Lambda_L1_contribution=np.float64(Lambda_L1_contrib),
    Lambda_total_L5=np.float64(Lambda_eff_pw[-1]),

    # Gap comparison
    Delta_mf_L0_mean=np.float64(Delta_L0),
    Delta_mf_L1_mean=np.float64(Delta_L1),

    # Intra-sector reference
    Gamma_CC_eff=np.float64(Gamma_CC_eff),
    t_CC_ratio_naive=t_CC_naive,

    # PW level data
    levels=levels,
    n_modes=n_modes,
    Lambda_eff_pw=Lambda_eff_pw,
    R_cancel_pw=R_cancel_pw,
)

print(f"  Saved to {output_path}")

# =============================================================================
# 12. Plot
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Left: Lambda_eff vs PW level
ax = axes[0]
ax.semilogy(levels, np.abs(Lambda_eff_pw), 'bo-', markersize=8, linewidth=2)
ax.axhline(y=abs(Lambda_00), color='r', linestyle='--', alpha=0.5, label=f'(0,0) only: {Lambda_00:.4e}')
ax.set_xlabel('PW Level (max p+q)', fontsize=12)
ax.set_ylabel('|Lambda_eff| (M_KK)', fontsize=12)
ax.set_title('PW Decomposition of CC', fontsize=13)
ax.legend()
ax.grid(True, alpha=0.3)

# Right: Rate hierarchy
ax = axes[1]
rates = {
    'Gamma_intra\n(ZUBAREV-CC-59)': Gamma_CC_eff,
    'Gamma_inter\n(BD upper bound)': Gamma_inter,
    'H_0': H_0_MKK,
}
names = list(rates.keys())
values = [rates[n] for n in names]
colors = ['green', 'red', 'blue']
bars = ax.bar(names, values, color=colors, alpha=0.7)
ax.set_yscale('log')
ax.set_ylabel('Rate (M_KK)', fontsize=12)
ax.set_title('Inter- vs Intra-Sector Rates', fontsize=13)
# Add value labels
for bar, val in zip(bars, values):
    if val > 0:
        ax.text(bar.get_x() + bar.get_width()/2., val * 2,
                f'{val:.1e}', ha='center', va='bottom', fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's60_inter_sector_zubarev.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved to {plot_path}")

dt_total = time.time() - t_start
print(f"\n  Total runtime: {dt_total:.1f}s")
print("\n  INTER-SECTOR-ZUBAREV-60 complete.")
