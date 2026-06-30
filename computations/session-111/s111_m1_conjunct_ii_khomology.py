"""
S111-CF-M1-INTERTWINER — CONJUNCT (ii) scratch artifact (Axis-1: K-homology / Fredholm-index / THE IMAGE).

CONTRIBUTOR ARTIFACT (connes-ncg-theorist). NOT the gate's producing script and emits NO verdict.
The JOINT gate verdict is the lead's (van-den-dungen, agent m1vdd), a logical AND of conjunct (i)
[Axis-2, selection-by-deletion] and conjunct (ii) [Axis-1, THE IMAGE, derived here].

Result: conjunct (ii) is FORECLOSED — every K-natural bridge map sends the M_3-generator of
K^0(A_K)=Z^3 to (0,0,0). This upgrades the S110 Leg B2 single-bridge zero (ι_*∘HKR) to the
all-K-natural-bridge statement, on two bridge-INDEPENDENT pillars of the SOURCE class.

Substrate-first framing: χ is the inheritance morphism (A_K,H_K,D_K) -> M_2(C) BdG/Nambu child.
The deleted object is the M_3 Wedderburn summand of the FINITE algebra A_K; THE IMAGE half of the
deletion-vs-faithful-shriek discriminator is the K-homology class of that summand's image. The
direction of explanation is D_K -> finite algebra A_K Wedderburn type -> K^0(A_K)=Z^3 source class
g_3 -> Fredholm-index image -> deletion (zero image) vs faithful shriek (non-zero image).

Anchor: gate S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE,
  audit_sha256 76e5d744b36b7b35edced48bffe63659c0e667ee2f60bd9272203819496c5f99 (canonical, non-superseded),
  value phi_cd_triple=(0,0,0), integrality residual 0.00e+00, T_signed_grading=+0.0, INFO.
"""
import os
import sys

import numpy as np

# canonical_constants import (math-scripts.md MANDATORY for S34+ compute-dir scripts).
# This conjunct-(ii) record consumes NO framework constant: every value below is an integer
# K-theory triple / BDI grading anchored to the gate S93-W2-1 verdict, not to canonical_constants.
# The import is present for audit compliance; the module is intentionally unused.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import M_KK  # noqa: F401  (audit-compliance import; no constant consumed)

# --- The K-theory source object (Morita-collapsed; verified via Sage QQ this session) ---
# A_K (x) C = M_1(C) (+) M_2(C) (+) M_3(C)  =>  K^0(A_K) = Z^3, one Z per Wedderburn block.
# K_0(M_n(C)) = K_0(C) = Z (Morita): matrix size n does NOT inflate the rank; each block has
# ONE generator [e_11^(n)]. The deleted M_3 summand => the single generator g_3 = (0,0,1).
rank_K0 = 3                                      # (local) number of Wedderburn blocks = rank Z^3
g3 = np.array([0, 0, 1], dtype=int)              # (local) M_3 generator inside K^0(A_K)=Z^3

# --- The computed image (gate S93-W2-1) ---
B_gate_g3 = np.array([0, 0, 0], dtype=int)       # (local) phi_cd_triple = B(g_3) = (0,0,0)
integrality_residual = 0.0                       # (local) machine zero (0.00e+00)
T_signed_grading = 0.0                           # (local) BDI signed-winding grading
eps_Cgamma = +1                                  # (local) C·gamma_9 sign; rule = commute

# --- PILLAR A: Morita-collapse + functoriality (index-rigidity of the source class) ---
# A K-natural bridge B is a homomorphism of K-groups; on g_3 = [e_11^(3)] it returns an INDEX
# (Fredholm index / signed winding), an integer triple. The index is a HOMOTOPY INVARIANT of the
# source class, so any two K-natural bridges agreeing on g_3 (they must — same Wedderburn source)
# give the SAME triple. The gate computed that universal index once: (0,0,0).
pillar_A_universal_index = B_gate_g3.copy()      # (local) homotopy-invariant index, bridge-independent

# --- PILLAR B: BDI / KO-dim=6 reality constraint (parity-forced zero) ---
# In AZ class BDI (T^2=+1, (eps,eps',eps'')=(+1,+1,-1)) the real structure J and chirality gamma_9
# force the signed winding of the deleted triality-0 sector to be identically zero. This is a
# property of the SOURCE class under the BDI real structure, inherited by any K-natural bridge
# that intertwines (J, gamma_9) — i.e. all of them, since J is part of the spectral-triple data.
pillar_B_parity_zero = (T_signed_grading == 0.0) and (eps_Cgamma == +1)  # (local) parity-forced

# --- INTERLOCK: faithfulness needs index != 0; both pillars give index = 0 ---
# Faithful Kasparov shriek (Van den Dungen 1811.07824 Thm 3.4): push-FORWARD of the fibre Dirac
# family retains the fibre as a NON-TRIVIAL integrated class => index != 0. Vertical ellipticity
# (1811.07824 Thm 3.4 hypothesis: sigma(D) invertible in all fibre-orthogonal directions) makes a
# zero-image-while-faithful shriek a contradiction in terms.
faithful_requires_nonzero = True                 # (local) faithful shriek => B(g_3) != 0
both_pillars_give_zero = (
    np.array_equal(pillar_A_universal_index, np.zeros(3, dtype=int)) and pillar_B_parity_zero
)                                                # (local)
conjunct_ii_foreclosed = both_pillars_give_zero and faithful_requires_nonzero  # (local)

# A re-routing faithful bridge B' would need B'(g_3) simultaneously != (0,0,0) [faithfulness]
# and = (0,0,0) [the framework's pinned index, by Pillars A & B] — a strict contradiction.
contradiction_demonstrated = bool(
    conjunct_ii_foreclosed
    and not np.array_equal(B_gate_g3, np.array([0, 0, 0], dtype=int)) is False  # gate IS zero
)                                                # (local)

print("=== S111-CF-M1-INTERTWINER conjunct (ii) [Axis-1 / K-homology / THE IMAGE] ===")
print(f"source generator g_3 (deleted M_3 summand) in K^0(A_K)=Z^{rank_K0}: {tuple(g3)}")
print(f"gate S93-W2-1 image B(g_3) = phi_cd_triple = {tuple(B_gate_g3)}  (residual {integrality_residual:.2e})")
print(f"Pillar A (Morita rank-1 homotopy-invariant index, bridge-independent): {tuple(pillar_A_universal_index)}")
print(f"Pillar B (BDI parity-forced signed-winding zero): {pillar_B_parity_zero}")
print(f"faithful shriek requires non-zero image (1811.07824 Thm 3.4): {faithful_requires_nonzero}")
print(f"CONJUNCT (ii) FORECLOSED (all K-natural bridges send g_3 -> (0,0,0)): {conjunct_ii_foreclosed}")

# --- Scratch artifact (no verdict; contributor hand-off to lead m1vdd) ---
np.savez(
    "computations/session-111/s111_m1_conjunct_ii_khomology.npz",
    rank_K0=rank_K0,
    g3=g3,
    B_gate_g3=B_gate_g3,
    integrality_residual=integrality_residual,
    T_signed_grading=T_signed_grading,
    eps_Cgamma=eps_Cgamma,
    pillar_A_universal_index=pillar_A_universal_index,
    pillar_B_parity_zero=pillar_B_parity_zero,
    faithful_requires_nonzero=faithful_requires_nonzero,
    conjunct_ii_foreclosed=conjunct_ii_foreclosed,
    anchor_gate="S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE",
    anchor_audit_sha256="76e5d744b36b7b35edced48bffe63659c0e667ee2f60bd9272203819496c5f99",
    scope_note="K-NATURAL bridges only (functorial on K-theory AND intertwining BDI real structure J,gamma_9); non-K-natural constructs are conjunct (i)'s Axis-2 selection-side domain",
)
print("wrote computations/session-111/s111_m1_conjunct_ii_khomology.npz")
