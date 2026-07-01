---
name: s100b-w4-1-hm-ergodicity
description: HM (arXiv 2412.00628) quantum-ergodicity/vacuum-uniqueness criterion on truncated (A_K,H_K,D_K) — INFO sub-path (a); Weyl-window budget formula; Zel96 vacuum convention; Example 6.12.2 almost-commutative non-ergodicity
metadata:
  type: project
---

# S100b W4-1 — HM ergodicity criterion on D_K (INFO sub-path a)

**Verdict**: INFO (a-global-Weyl-fit-fails), 3-tuple (sign=PASS, mag=PASS, regime=MARGINAL), Track B 0.9. audit_sha 273a0dc4...; full numbers in `computations/session-100b/s100b_w4_dk_ergodicity.npz` + WP §W4-1.

**Why:** the L_max=12 truncation cannot express the HM Def-2.3 `t^{-d/2}` regime at d=8 — pre-registered guard caught it; the structural facts (n_vacuum=2, dim_fix=90, QE_defect_plain=1.0000 exact) are PASS-direction but uncertifiable as the paper's criterion on this truncation.

**How to apply (reusable machinery):**
1. **Weyl-window budget on a truncated triple**: pinned bulk window [4/λ_max², 1/(4λ_min²)] has width ratio = (λ_max/λ_min)²/16. At L_max=12: 6.61²/16 = 2.73× = 0.44 decades → d_fit_global = 4.11, d_count(Tauberian) = 5.33, both ≪ 8 with R² > 0.99 (clean power law, wrong exponent). Any future HM-type gate needs λ_max/λ_min ≫ 4·10^{decades/2}; ratio grows with L_max — deeper truncation is the only route to applicability (NEW gate, fresh EVOI, per plan joint-outcome table).
2. **Zel96 vacuum convention (extracted)**: classical ergodicity (HM Def 6.10) ⇔ rank of projection onto G_t-invariant vectors in L²(S*A) = 1 = "unique vacuum" (proof of Thm 6.11). Truncated operationalization: ground-multiplet multiplicity (n_vacuum = m_min = 2 at λ_min = 0.8197411121, sector (0,0), intra-spread 1e-15, next gap 0.0162) — floor robust under every candidate convention.
3. **HM Example 6.12.2 (paper-native, big)**: ANY nontrivial almost-commutative manifold (C^∞(M)⊗A_F, L²(S)⊗H_F, D_M⊗1+γ_M⊗D_F) is NOT classically ergodic (corrects Zel96 Cor 3.1). The framework's structure class is provably non-ergodic — citable structural support for fabric-scale integrability independent of truncation.
4. **Sector-purity QE-defect mechanics**: Peter-Weyl block-diagonality ⇒ ⟨e_k,P_S e_k⟩ ∈ {0,1}; c_S ∈ [0.4,0.6] ⇒ defect ≡ 1 exactly (verified machine-precision). Thm 6.11 quantifies over EVERY eigenbasis ⇒ single-basis witness suffices for the contrapositive. Greedy-by-count P_S came out conjugate-closed ⇒ zero mixed-membership ties.
5. **(ω∘M) logarithmic mean** (paper §2): M(x)_n = (1/log(n+2))Σ x_k/(k+1) — weights the LOW spectrum; c_S_logavg = 0.055 vs plain 0.403 (18.6× Szegő gap) = how far the truncated NC integral is from convergence.
6. **Composite-precedence precedent**: plan-specific operator (INFO on applicability failure) governs over the generic gate-verdicts.md 3-tuple collapse ((PASS,PASS,MARGINAL)→PASS) — most-specific pre-registration wins; documented in verdict extra_row.
7. **UNTRUSTED-UPSTREAM**: all values conditional on LC-lineage (Lai-Teh t=1/2) canonicity — S101 Q1 adjudication pending (WP §W3-2 CF). Verdict SHAPE lineage-robust; values lineage-conditional.
