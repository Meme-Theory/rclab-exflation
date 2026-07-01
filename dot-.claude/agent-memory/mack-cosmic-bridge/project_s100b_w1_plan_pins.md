---
name: s100b-w1-plan-pins
description: S100b Wave-1 plan-freeze findings (2026-06-06) — R_JE-retirement re-pin, dual-rounding trap, queued mack inventory writes
metadata:
  type: project
---

S100b W1 plan (`sessions/session-plan/session-100b-plan-w1.md`, authored by me 2026-06-06; R3 validator 4/4 PASS) carries four pins that matter at execution and at inventory-landing time.

**Why:** plan-freeze canonical-state queries caught two stale-source traps the litrev carry-forwards transcribed verbatim; and three of my sole-writer inventory actions are queued off this wave's verdicts.

**How to apply:**
1. **W1-4 re-pin (Class-(c))**: the consolidation's "branch-iv R_JE stability by L_max=12" pins the RETIRED R_JE tag — S86-BRANCH-IV-FORMULATION-COMMIT (latest line PASS, audit `acc751101c8ca6ce…`) retired it for R_JK (distance-2) + xi_E_GGE_inv (distance-1). Gate tests the branch-iv w_0 EVALUATION under CAC-branch-iv (anchor L=10, demarcation bit-exact at −0.842454, scheme=zeta SV1-anchored); SV2's L=8 FAIL (value=10.077109) is the legacy-form drift record, input not test. `w0_FW_R842` is NOT in canonical_constants (verified 2026-06-06) — promotion happens only on W1-4 PASS.
2. **Dual-rounding trap**: the ΔN_eff bound factor (7/8)(4/11)^(4/3) appears as 0.227107 (S99 verdict line) AND 0.227113 (canonical_constants provenance comment). Sage-exact ≈ 0.2271074. Both W1-1/W1-2 blocks pin in-script Sage-exact computation; never hardcode either image.
3. **Queued mack writes (sole-writer)**: Row #76 BBN-VOLOVIK-67 constraint-scope annotation (after W1-1); Row #1 footnote sub-row (after W1-4); NEW watchlist sub-row "w_a (Planck-low-ℓ-independent)" (W1-3, my own gate). 0.107 Goldstein-Hill budget registers via W1-1 with EXTERNAL-NON-CANONICAL tag — never as a substrate pin. T_RH still non-canonical (get_constant not-found), verify-at-runtime.
4. **Stale path flag (§A housekeeping)**: `branch-iv-canonical.md` §"Anchor cache" cites `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz`; on-disk canonical is `computations/session-85/…` (SHA `ebdeab300b4306af…`).
5. **S66 normalization-anchor discriminator** (W1-1 pre-registered axis): S66's G_eff table (n_eff=2.3 PASS, n_eff≤2 EXCLUDED) is reproduced by FOLD-anchored α_V transport; S98/S99's lever (n_eff<2 relieves) is z=0-anchored (DILUTION-CC). Opposite anchor ends → opposite n_eff directions. The adjudication is einstein's gate; do not pre-judge in inventory text until its verdict lands.
