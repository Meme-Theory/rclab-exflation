---
name: s101-w3-6-ccs-modelc-ko
description: S101-W3-6 CCS Model-C (G422D) KO-derivation — theory-match (6,+1,+1,-1) but verdict INFO (primaries don't pin KO); the antilinear conjugation-form sign method + reality-axiom-load-bearing diagnostic
metadata:
  type: project
---

# S101-W3-6 — CCS Model-C (G422D) KO-dimension derivation (verdict INFO)

**Gate**: S101-CCS-MODELC-KO-DERIVATION. **Verdict: INFO** (audit_sha256 `bb2fa21a69f4f84938f6aef88c0a7aeb8d616452d046a8b83952617f49cc932d`).

**Fact**: derived triple (ε,ε′,ε″) = (+1,+1,−1) → KO_dim 6, machine-ε on the explicit witness; MATCHES substrate anchor T_S=(6,+1,+1,−1) from `s100b_w2_2_ps_variant_id.npz` on all 4 slots (theory_match=True).

**Why INFO not PASS** (the determinate, reportable finding): the FOUR pinned on-disk CCS/Aydemir transcriptions (Connes/23,24,40; Aydemir Connes/27) are summary-level — they pin the ALGEBRA (ℂ⊕ℍ_L⊕ℍ_R⊕M₄(ℂ)), the FERMION CONTENT ((4,2,1)+(4̄,1,2)), and the DIRAC BLOCK FORM ([[0,H],[H†,0]], Connes/40 L100), but state ZERO KO-fixing ingredients (real structure J, J², order-0 reality axiom, grading antiparticle-sign). Grep-audit returned **0 KO-fixing hits across all 4**. The (+1,+1,−1)/KO-6 triad rests on 3 NCG-canonical inputs supplied from standard theory (SM-inherited J/γ; antiparticle grading = −particle grading; J-real D_F) NOT present in the pinned corpus. Per `feedback_research-corpus`, training-memory ≠ primary source → axis-(iii) indeterminacy is a property of the PRIMARY LITERATURE as transcribed, not just the Aydemir taxonomy.

**Downstream**: W3-7 (S101-PS-RGE-MODELC-SIN2-MZ) dispatches STATUS-QUO (ko_axis=indeterminate-carried). INFO is NOT a determinate FAIL, so W3-7 is NOT re-scoped to axes-(i,ii)-only.

## Reusable methods (verified machine-ε + Sage QQ̄)

1. **Antilinear-J commutation discipline** (the load-bearing step): for antilinear J = S∘K (S = particle↔antiparticle swap, K = c.c.), the relation `J X = s·X J` reduces — strip the common trailing K — to the LINEAR-operator identity `S·conj(X) = s·X·S`. Never a naive complex commutator on a complex operator. Then ε=sign via J²=S·conj(S); ε′ via D; ε″ via γ.

2. **Reality-axiom-load-bearing diagnostic**: ε′ is clean (+1) ONLY when D_F is J-real ⟺ Yukawa block H complex-SYMMETRIC (forced by [D,JaJ⁻¹]=0). A GENERIC non-symmetric H gives `S·conj(D)=±D·S` for NEITHER sign (returns None). That "None" is the witness the reality axiom is doing real work — not an indeterminacy of the physical construction. Use this to distinguish "physical D_F (constrained)" from "arbitrary complex matrix".

3. **γ_F antiparticle-sign**: antiparticle grading = −particle grading (γ=diag(g,−g)) is what yields {J,γ}=0 ⟹ ε″=−1, the KO-dim-6 row. This is the chirality-antimatter nexus.

4. CCS PS construction = relax first-order on the SM triple via quadratic inner fluctuations; H_F, J_F, γ_F UNCHANGED from SM, only the algebra rep + D fluctuated ⟹ inherits KO-dim 6. (Standard CCS-2013/CCM-2007; NOT in the on-disk summary transcriptions.)

5. H_F(Model C): (4,2,1)=8 + (4̄,1,2)=8 = 16 Weyl/sector/gen; ×2 particle+antiparticle = 32/gen; ×3 gen = 96. Matches npz hf_dim_per_gen=32.

**Library gap flagged**: the on-disk Connes/24 (Pati-Salam) + Connes/40 transcriptions are abstract-level summaries lacking the §2 real-structure construction. A future PASS on this gate needs either the full CCS-2013 §2 transcribed on-disk, or a registry theorem "CCS-PS lineage inherits SM (J_F,γ_F)". See [[paper-audit-2026-02-21]] for the transcription-quality pattern.
