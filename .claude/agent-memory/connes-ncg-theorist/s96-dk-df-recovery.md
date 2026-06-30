---
name: s96-dk-df-equivalence-controlled-recovery
description: S96 W8-4 — the D_K ≅ D_F controlled-low-energy-recovery theorem; structural recovery EXACT, residual is the KK-suppression budget (INFO, not literal-PASS)
metadata:
  type: project
---

# S96-CONSOL-DK-DF-EQUIV — controlled low-energy recovery theorem

**Gate**: S96-CONSOL-DK-DF-EQUIV (W8-4, the deep-research reviewer's HIGHEST-BURDEN math step).
**Verdict**: INFO (controlled recovery with explicit KK-suppression residual budget; NOT literal-exact).
**Why**: discharges the reviewer's "controlled low-energy recovery theorem" ask but honestly carries the bare-axiom N3 obstruction + KO-mismatch intact.

## The structural statement (the precise sense of "≅")
- Framework position is eq (1.7) `M = <φ, D_K φ> = D_F, φ = Σ_i a_i [D_K, b_i]` (connes-master-equation.md §1.1.2): **D_K IS D_F**; the Higgs is an inner fluctuation of D_K, NOT a separate commuting D_F. The product-geometry reflex "[D_K,a_F]=0" is WRONG (recurring project error).
- "≅" is therefore a **controlled LOW-ENERGY RECOVERY** (D_F = E→0 / constant-mode limit of D_K's bottom sector), NOT a full isometric triple isomorphism (dimensionally impossible: SU(3) 8-dim, F 0-dim — quotient-functor pre-registration, ∞-dim↔finite-rank disparity).

## Numerical recovery (from s84_spectrum_cache_L12_tau019.npz, sector_evals dict)
- **(0,0) constant-mode sector**: dim=1 (trivial Peter-Weyl rep), level=0, carries EXACTLY **16 eigenvalues** = C^16 = Ψ_+. Unique |λ|: 0.81974(×2), 0.84521(×8), 0.97141(×6). Casimir C_2(0,0)=0 EXACT (Sage QQ) — pure spin-connection Ω_LC floor, no orbital energy. THIS is the bottom of the tower.
- Recovery components:
  - **(i) A_F=C⊕H⊕M_3(C) Wedderburn**: 3 factors, center dim 3 (N2/N7 STAGE-3-PERMANENT). block dims {C:1, H:1-over-H/4-real, M_3(C):9-over-C}. STRUCTURAL PASS.
  - **(ii) KO-dim=6**: on the C^16 FIBER real structure (G4, (ε,ε',ε'')=(+1,+1,-1)), carried INTO H_K=L²(S)⊗C^16 BY CONSTRUCTION. NOTE: KO-dim(SU(3) orbital)=0, KO-dim(M^4×SU(3))=4 — the =6 is the finite-fiber value, the product mismatch (4 vs 6) is PERMANENT. PASS-by-construction.
  - **(iii) Ψ_+=C^16 SM multiplets** (G5): 6+3+3+2+1+1=16 (Sage-exact); (0,0) sector dim=16 matches → dim residual = 0.0 EXACT. PASS.
  - **(iv) KK-gap/M_KK**: orbital KK scale = sqrt(<λ₁²>−<λ₀²>) = **0.682257** ∈ [0.5,2]. Controlled separation. PASS. (level-1=(0,1)+(1,0), C_2=4/3; the additive min/max gap is NEGATIVE −0.135 because bands overlap — the quadrature/Casimir metric is the structurally-correct one, λ²=floor²+orbital(C_2).)

## The INFO trigger (honest residual)
- recovery_residual < 1e-6 (literal D_F bare-eigenvalue block match) is NOT satisfiable: D_F is the FLUCTUATION pairing M=<φ,D_K φ>, not the bare (0,0) eigenvalues. The honest residual = **KK-suppression budget ≈ 0.320 = O((E/M_KK)²)** = (E_low/(E_low+M_KK_eff))², explicitly non-zero, flagged as the KK-tower suppression scale.
- Maps to INFO_meaning + dual-prior INFO→0.5/0.5: recovery holds with explicit residual budget; theorem ships with KK-correction caveat.
- bare-axiom N3 BROKEN (axiom-5 orientability=4.000 for M_3(C)) carried INTACT; recovery shows SM content recovered at low E GIVEN the Wedderburn-Frobenius rescue, NOT that the bare axiom is repaired.

## Registry consequence
- §VII recovery-theorem slot: STAGE-1-CANDIDATE eligible (joint-theorem-promotion.md); Stage-2 cross-axis verify warranted given the bare-axiom N3 obstruction. NOT auto-STAGE-3 (residual budget + N3 obstruction).
- Artifacts: computations/_shared/s96_consol_dk_df_equiv.py + computations/session-96/s96_consol_dk_df_equiv.{npz,png}.

## S97 W5-1 LANDED — slot is §VII.BK (NOT §VII.BH)
- The controlled-recovery theorem is registered at **`permanent-results-registry.md §VII.BK`** as STAGE-1-CANDIDATE (S97 W5-1 `S97-DK-DF-STAGE2` Component A, 2026-05-30).
- **SLOT REROUTE**: plan pinned §VII.BH, but §VII.BH/BI/BJ were ALL occupied by S96 W7-8/W-3/S-1 landings between plan-freeze and runtime (§VII.BH = van-den-dungen `c_s²=0`; §VII.BI = string-theory area-law; §VII.BJ = superalgebra-obstruction). Rerouted §VII.BH → §VII.BK per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` (all-header-level scan, next-free letter). Benign Class-(c) plan-text-drift.
- Clauses (a)..(n) registered; JOINT clauses for Stage-2 PASS-AND = (c) controlled-not-isomorphism, (d) N3+KO PERMANENT, (i) 0.320=O((E/M_KK)²) budget legit, (n) no-unconditional-equivalence-over-claim. Axis-A NCG = {a,b,e,f,j,k,l}; Axis-B substrate = {g,h,m}.
- Component-A landing closure SHA pin = `52b8f6f5e7842c2fa4788989f9d1e68620e7017fd6e68de1ced39ab5db6a788e`. npz SHA verified `40bfab58…`. plan_block_sha (allowlist) = `78497501…`.
- Composite `S97-DK-DF-STAGE2` verdict line = the Stage-2 PASS-AND outcome (Axis-A connes + Axis-B volovik, PARALLEL, W8-4 transcript WITHHELD) — emitted by Component B AFTER reviewers run; NOT by the landing. PASS-AND both axes ⇒ §VII.BK STAGE-1-CANDIDATE → STAGE-3-PERMANENT. substrate-input-overlap caveat (shared npz → OUTPUT-type independence only).
