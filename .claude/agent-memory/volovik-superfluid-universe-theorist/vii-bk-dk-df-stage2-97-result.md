---
name: vii-bk-dk-df-stage2-97-result
description: S97 W5-1 Stage-2 Axis-B review of §VII.BK D_K≅D_F controlled recovery — substrate-side verification of KK-gap quadrature metric, IR-sector reading, budget legitimacy
metadata:
  type: project
---

S97 W5-1 `S97-DK-DF-STAGE2` — I was the Stage-2 Axis-B (substrate/superfluid) cross-reviewer for the §VII.BK STAGE-1-CANDIDATE controlled-recovery theorem (D_K ≅ D_F at E≪M_KK). Verdict: **Axis-B PASS** on all my single-axis clauses (g,h,m) AND all JOINT clauses (c,d,i,n). PASS-AND eligible pending Axis-A.

**Why:** the registered theorem is honest about being a CONTROLLED recovery, not an isomorphism. The substrate physics holds up under independent recomputation from `s96_consol_dk_df_equiv.npz` (SHA 40bfab58…, verified).

**How to apply:** reusable substrate-side closed forms for any future Stage-2 review of the KK-tower → SM-finite-geometry recovery —

- **KK-gap quadrature metric (clause g)**: the additive |λ| edge-gap `add_gap_minmax = -0.13551411` is NEGATIVE only because the (0,0) band has nonzero spin-connection floor SPREAD (uniq |λ|_(0,0) = {0.81974, 0.84521, 0.97141}); the (0,0) band MAX (0.97141) exceeds the level-1 band MIN (0.83589). The structurally-correct KK separation is in λ² (energy²): `λ² = floor² + k_casimir·C₂` with **k_casimir = 0.34910632 ≈ 1/r²(τ_fold)** (the Jensen-deformed radius rescales the Casimir; NOT k=1 as the registry shorthand `λ²=floor²+C₂` suggests). Quadrature KK-gap = √(⟨λ₁²⟩−⟨λ₀²⟩) = **0.68225735 ∈ [0.5,2]**. C₂(0,0)=0 (pure floor, no orbital) vs C₂(lvl1)=4/3>0 makes the energy-scale ordering unambiguous. The negative additive gap is an EDGE artifact, not an inversion.
- **IR-sector / BdG-ground reading (clause h)**: the (0,0) Peter-Weyl constant-mode block (dim 16 = ℂ¹⁶ = Ψ₊, C₂=0 EXACT) IS the bottom of the KK tower = the BdG/superfluid ground sector; level-1 (C₂=4/3) is the first gapped excited KK band. `L_max_saturated=True` ⇒ the (0,0) block is truncation-invariant ⇒ genuine IR sector. SM finite geometry is DERIVED as the IR limit, not assumed.
- **Budget legitimacy (clause i)**: `kk_suppression_budget = 0.32022702 = (E_low/(E_low+M_KK_eff))² = 1/(1+M/E)²` with E_low=0.88935155, M_KK_eff=0.68225735(=orbital_kk). This is the KK-tower GEOMETRIC-SERIES (resummed-propagator) weight, bounded in [0,1) for ALL E,M>0, NOT the textbook (E/M)²<<1 (which fails here since E/M=1.30>1 at the internal O(1) scale). Binomial partition (M/(E+M))²+2EM/(E+M)²+(E/(E+M))²=1 (Sage-exact). Reduces to genuine (E/M)²→0 at the physical hierarchy E_lab≪M_KK=7.43e16 GeV. The `E/(E+M)` form does NOT pretend E≪M at the internal scale — it is the honest resummed bound.
- **JOINT (c) controlled-not-iso**: literal_exact=False, 4 criteria all True, recovery_residual_literal=0.17053606 ≤ budget 0.32022702. Dimensionally impossible to be an iso (SU(3) 8-dim, F 0-dim; level-1 alone = 96 evals quotiented away vs 16 kept ⇒ LOSSY quotient).
- **JOINT (d) obstructions PERMANENT**: KO_dim_product=4 ≠ KO_dim_fiber=6, KO_dim_SU3_orbital=0 (orbital supplies 0, not 6). N3 order-one fails at norm 4.000 on bare M₄×F. Both are bare-axiom properties FIXED ∀ E (E does not enter KO_dim or the order-one defect); KK quotient does not touch them. Confirmed against canonical anchors PRODUCT-KO-DIM-66 (PASS S66) + N3 (atlas-04 BROKEN+Wedderburn-Frobenius rescue STAGE-3-PERMANENT).
- **JOINT (n) no-over-claim**: affirming UNCONDITIONAL equivalence FAILS. I affirm the CONTROLLED-recovery (obstructions-intact) reading.

**Substrate-input-overlap caveat (load-bearing)**: Axis-A and I read the SAME npz ⇒ Stage-2 PASS-AND establishes structural-OUTPUT-type independence (substrate-BdG/Casimir pipeline vs NCG-axiom pipeline on the same data), NOT structural-INPUT independence. Per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`. Carried explicitly in my review.

See [[project_3heb-inheritance]] (substrate priority / IR-limit direction).
