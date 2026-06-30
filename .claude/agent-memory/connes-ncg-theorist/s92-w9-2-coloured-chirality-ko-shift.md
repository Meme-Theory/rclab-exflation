---
name: s92-w9-2-coloured-chirality-ko-shift
description: S92 W9-2 FAIL — CM-2008 §11 SU(3)-coloured chirality KO-dim shift (6→2) does NOT realize at framework's A_K for any of 6 non-trivial colour-sign tuples; ε''=−1 colour-sign-INVARIANT under BDI block-swap J
metadata:
  type: project
---

# S92 W9-2: SU(3)-coloured chirality KO-dim-shift sweep — FAIL (structural)

**Gate** `S92-W9-CF-W7-2-VII-AW-OP-PROJ-COLOUR-SIGNS-SWEEP`. Verdict **FAIL**, `pass_count=0/6`.
LIVE audit_sha256=`11ff4d2f60011eed8e50283c0f8e2eef9d958b78a098fbe8cb8045d20491322d` (supersedes `6dd92524...`, pin-path correction). Script `computations/session-92/s92_w9_2_vii_aw_op_proj_colour_signs_sweep.py`.

**Why:** CM-2008 §11 (Connes-Marcolli 2008 monograph) predicts SU(3)-coloured chirality dressing shifts KO-dim 6→2 mod 8 (neutrino-sector compatible). Tested over the 6 non-trivial `(s_r,s_g,s_b) ∈ {±1}³ \ {(+,+,+),(−,−,−)}` on the framework's concrete `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, dim H_F=12. The (+1,−1,+1) tuple is the S91 W7-2b baseline (reproduced ax5dp=3.274141 exactly → parametrization fidelity confirmed).

**STRUCTURAL THEOREM (machine-exact) — ε'' is colour-sign-INVARIANT:**
The framework's J = KO-dim-6 BDI pure L↔R block-swap. The CM-2008 colour-dressing convention sets γ_R = −γ_L on the M_3 chirality block (base `build_su3_coloured_gamma`). Since colour signs are REAL, `J γ'' J⁻¹ = swap-blocks(γ'') = block-diag(γ_R, γ_L) = −γ''` EXACTLY (diff_minus = 0.00e+00 measured; diff_plus = 2·4√3 ≈ 6.93). So ε'' = −1 for ALL 8 tuples (signs cancel out of the ε'' sign test). ⇒ KO-dim = KO_TABLE[(+1,+1,−1)] = **6 for every colour-signs choice**; KO=2 (CI, ε''=+1) is UNREACHABLE by colour-dressing. The substrate's J fixes ε'' independently of the grading signs.

**Second obstruction:** axiom-5'' `{D_F, γ_9''} ≠ 0` for all 6 (residuals 1.20–4.14, all ≫1e-10). D_F's off-diagonal mass couplings (ℂ↔ℍ, ℍ↔M_3, M_3-internal) mix colour eigenstates of different γ_9'' eigenvalue → grading isn't a chirality for D_F. Min residual 1.20 at (+1,+1,−1). n_axiom_pass = 6/7 (axiom-4 order-one FAILs at 4.0 always; axiom-5'' anticomm FAILs).

**9-sector cardinality** `[8,0,0,0,2,0,0,0,2]` (sum 12), tuple-invariant (colour_map partitions by basis index, not by sign).

**How to apply:** §VII.AW.OP-PROJ STAGE-0-CANDIDATE-WITH-FAIL-DIAGNOSTIC RETAINED; promotion BLOCKED. Tensor-product chirality γ_9 = γ_5 ⊗ γ_F at §VII.AQ.OP-PROJ REMAINS sole valid spectral-triple chirality (consistent w/ permanent KO=6). Algebra-axis orthogonality K-counter (chirality-grading sub-axis) gains NO calibration instance (PASS required). Corollary: ANY alternative chirality grading on the colour summand inherits ε''=−1 under the BDI J — to reach KO=2 you must change J itself (not the grading), which conflicts w/ permanent KO-dim=6 result. Bridge map non-binding Level-2 for all (HKR fails via axiom-4; only K-theory-bdy passes → 1/3).

**Pin-path note:** plan/spawn cited non-existent `researchers/Connes-Chamseddine-Marcolli/`; corpus path is `researchers/Connes/10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md` (paper #10, KO-6 BDI baseline). §11 prediction is from Connes-Marcolli 2008 NCG-physics-motives monograph (NOT in-corpus) — methodological/heritage citation per substrate-first-canonical-sourcing §(i); the sweep IS the substrate-first computation.
