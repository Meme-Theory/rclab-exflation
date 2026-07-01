---
name: s117-seesaw-resonance-wall
description: S117 W2-3 FAIL — lepton seesaw single-RH-dominance resonance CANNOT relieve the PMNS angle wall; theta12 is M_R-INVARIANT (rank-2 Y_1=0 decoupling), and the B-branch bowtie is structurally flat
metadata:
  type: project
---

**CF-S117-SEESAW-RESONANCE-MR-SEARCH = FAIL** (clean, not INFO). The seesaw single-RH-dominance resonance (Smirnov/King: mixing enhancement fires when M_D[2,2]/M_D[1,1] ≈ √(M_R[2]/M_R[1])) does NOT rescue the lepton PMNS angle channel that [[s116_lepton_pmns_texture]] walled (mix_grp=0/4) and [[s116_pmns_rescue]] left WALLED-AS-UNDER-DETERMINED. The §VII.CK D4 RESONANT-CONDITIONAL annotation finalizes to WALLED.

**Two independent obstructions, BOTH M_R-INVARIANT** (so no fold-spectrum reshape, ordering, τ, or off-form coupling can move them):

1. **θ₁₂ rank-2-decoupling wall (the deeper one).** ν₁ is Dirac-decoupled (Y₁=0 EXACT ⇒ m₁=0, S100a) ⇒ U_νL[0,:]=[1,0,0] for ALL M_R ⇒ |U_e1|² = |U_eL[0,0]|² = **0.004376** (independent of M_R). NuFIT cos²θ₁₂cos²θ₁₃ = 0.6816 ⇒ **155.8× deficit** ⇒ sin²θ₁₂ ≥ 1−|U_e1|² = **0.99562** > band hi 0.341. The θ₁₂ slot is structurally unreachable ⇒ **mix_grp ≤ 2 for any M_R**. The seesaw resonance only acts in the 2-3 (atmospheric) block; it is geometrically incapable of supplying the solar/reactor angles, which are fixed by U_eL alone. (The wall lives in M_D/U_eL, NOT M_R — that is why it is M_R-invariant and survives off-form.)

2. **Flat B-branch bowtie.** The bottom D_K fold energies cluster at the spectral floor: globally-lowest-3 = [0.81974, 0.83589, 0.87298], lowest-per-triality = [0.81974, 0.83589, 0.83589] (M_KK). On-form max √(B_max/B_min) = **1.0337** across 124 candidates (62 τ ∈ [0.08,0.21] incl. the τ=0.107 B1–B2 crossing × {globally-lowest-3, lowest-per-triality t∈{0,1,2}}), vs the resonance need √ratio ≈ Y₃/Y₂ = **2.488** (C₂ gap ~38). Resonance NEVER fired. To reach √ratio~2.5 needs widely-separated sectors (B₂/B₁~6, C₂ gap~38), NOT the lowest fold energies.

**Off-form guard (CF-W2-2 convention-shopping) confirms clean FAIL, not INFO:** full θ_ν∈[0,π/2] envelope max mix_grp=2/3; A_K-built degenerate diag(M₀,M₁,M₁) [un-used standard-NCG A_F] = 0/3; off-fold forced-reshape = 1/3. Nothing reaches mix_grp≥3.

**Reusable method notes (for future neutrino-sector gates):**
- Reuse the s116 pipeline EXACTLY when varying only M_R: load `U_eL`, `Y_nu_diag`, `w23_nu` from `s116_lepton_pmns_texture.npz`; M_D = `yukawa_block_real(Y_nu_diag,0,0,w23_nu)`; vary M_R only; M_ν = M_D M_R⁻¹ M_Dᵀ → U_νL → U_PMNS = U_eL† U_νL. Bare triple reproduces s116 bit-for-bit (validation anchor).
- The bare B-branch M_R = [1.00440, 1.07857, 1.17000] M_KK resolves to sectors (0,1)/(1,0)/(0,2), C₂=[4/3,4/3,10/3] (matches S60 lepto-cp M₁=1.004396, M₂=1.078573).
- Friedrich-Bär bottom-K saturation: a τ-scan of the LOWEST fold energies is exact at operational max_pq_sum=4 (validated bit-for-bit vs the L12 cache at τ_fold; truncation_consistent=True) — no need for L_max=10/12 diagonalization for bottom-K selections. Disclose op-L vs plan-L in the convention tag.
- R is rescale-invariant; the ε_LX 2-3 texture reshapes M_ν so textured-channel R (113.56) ≠ aligned-basis R (31.58 ≈ R_osc 33.55). mix_grp is the operator; R is the joint companion.

Verdict audit_sha256 `2f5ab6114548918a198e403aff75579990c7f7ec09b81b70b4b2306d17cb6204`. Artifacts: `computations/session-117/s117_seesaw_resonance_mr_search.{py,npz,png}`.
