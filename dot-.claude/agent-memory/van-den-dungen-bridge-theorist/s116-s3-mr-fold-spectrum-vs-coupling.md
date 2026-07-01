---
name: s116-s3-mr-fold-spectrum-vs-coupling
description: S116 S-3 solo — substrate-forced Majorana M_R is the fold-EIGENVALUE-SPECTRUM diag(B1,B2,B3), NOT an A_K-built multiplicity-leg coupling diag(M0,M1,M1); §VII.BL wall scope boundary (eigenvalue-selection vs A_K-built form); closes OQ-4
metadata:
  type: project
---

**S116 S-3 (solo, van-den-dungen) — M_R FORM verdict closes OQ-4 of S116-W2-PMNS-RESCUE.**
Output: `sessions/session-116/session-116-w2-MR-structure-synthesis.md`.

**Verdict**: the substrate-forced Majorana mass is `M_R = diag(B₁,B₂,B₃)` carrying the bowtie `B₁<B₂<B₃` (neutrino's fold-spectrum reading), NOT `diag(M₀,M₁,M₁)` (connes' A_K-built multiplicity-leg-degenerate reading). The §VII.BL homogeneity wall does NOT apply to it.

**Why** (the load-bearing structural argument):
- **§VII.BL wall scope** = forecloses A_K-BUILT forms only (registry route-(b) exhaustion table, lines 21775-21780): (a) inner fluctuation `Σaᵢ[D_K,bᵢ]`, (b) spectrum-only G-invariant **MOMENT** `Σₖmₖg(λₖ)`, (c) twisted-inner `Ω¹_σ`, (d) opposite-action `JAJ⁻¹`. ALL are `⊗1` on the multiplicity leg. An eigenvalue-**SELECTION** (M_R) is NOT in this class. CRITICAL trap: route (b) forecloses a spectrum *moment* (sums the multiplicity leg into a scalar); M_R *resolves* the leg by picking distinct eigenvalues. Moment integrates the leg away; selection reads it out.
- **Two faces of `D_K = ⊕_{(p,q)} D_{(p,q)} ⊗ 1_{m(p,q)}`**: Face-1 (`⊗1` on the leg) IS the wall; Face-2 (`D_{(p,q)}` sector-dependent ⇒ eigenvalues sector-DISTINCT) IS the bowtie. M_R reads Face-2. Same block-diagonal root, opposite faces, opposite objects (built-forms vs eigenvalues) — NO conflict. Kasparov-factorization reading (Paper 01): fiber vertical spectrum is the data the product factors THROUGH; base calculus acts `⊗1` on fiber multiplicity.
- **Generation-lifting complement** `⊕1_V⊗M_m(ℂ)` (registry line 21155) is EMPTY of A_K-built forms (wall) but NOT empty of D_K-SPECTRAL data. M_R (diagonal-on-generations) lives in this complement, populated by the eigenvalue map `(p,q)↦|λ|_(p,q)` (non-constant), a SPECTRAL not A_K-built object.

**Category translation** (the fork is a category confusion, not a contradiction): `M_R^{A_K-coupling}` = standard-NCG free Majorana param on A_F (Connes 2006 §4.1) → §VII.BL forces `diag(M₀,M₁,M₁)` (connes' reading, the un-used object). `M_R^{fiber-spectrum}` = framework's `D_K≡D_F` promotion sources M_R from B-branch fold energies → `diag(B₁,B₂,B₃)` (neutrino's reading, USED). The `D_K≡D_F` commitment (same one making S62 direct-eigenvalue a "rank-1 wall") picks the fiber-spectrum branch.

**Construction (on-disk, settles it)**: `s99_w3_seesaw_summnu.py` METHODOLOGY lines 41-47 ("These Mᵢ ARE D_K eigenvalues … INTERNAL to the spectrum, NOT an external add-on"). `INV11-W2-4-MR-PROVENANCE-AUDIT` lines 25-32: M_R = `E_B3_fold[5:8]*M_KK` = lowest-8 modes of 32-cell tight-binding lattice-ED D_K; exact-membership in L12 cache FAILS (distinct pipeline, NOT a re-read, but IS a D_K eigenvalue). `M_R = [1.0043956635, 1.0785733201, 1.1700026004] M_KK`, three DISTINCT values.

**J-reality** forces M_R real-symmetric (`δ_CP∈{0,π}`), does NOT force degeneracy. connes' `M₁=M₁` collapse needs per-triality-class-constancy of an A_K-COUPLING (J pairs `t=1↔t=2`), absent for a spectrum-sourced M_R. On-disk 2-3 block split: `B₂=1.0786 ≠ B₃=1.1700`, refutes connes' 2-3 degeneracy directly. **STRONGEST form (review-gate hardening, basis-INDEPENDENT)**: M_R eigenvalue multiset {1.0044,1.0786,1.1700} = 3 DISTINCT; connes' diag(M₀,M₁,M₁) has a DOUBLY-DEGENERATE eigenvalue; eigenvalue multiplicity is a UNITARY INVARIANT ⇒ NOT unitarily equivalent in ANY basis ⇒ closes the "your diagonal isn't my triality eigenbasis" rejoinder. (S99 reads M_R straight from E_B3_fold[5:8], no degeneracy-lifting rotation.)

**Load-bearing consequence (sharpens workshop WALLED-AS-UNDER-DETERMINED)**: `√(B₂/B₁)=1.0363` (Sage-exact; matches workshop's 1.036) = bottom-spectrum Casimir near-degeneracy. Via `|λ|_min^(p,q)≈√C₂/r`: implied `C₂_2/C₂_1=(B₂/B₁)²=1.153` (small gap). Resonance `M_D[2,2]/M_D[1,1]≈√(M_R[2]/M_R[1])≈(C₂_2/C₂_1)^{1/4}` needs LARGE Casimir gap; `√(B₂/B₁)=5` needs gap 625. Bottom triple too flat. The flatness is a SUBSTRATE spectral fact, NOT an imposed degeneracy.

**Anchor for CF-S117-SEESAW-RESONANCE-MR-SEARCH** (satisfies CF-W2-2): scan ONLY fiber-spectrum forms (distinct D_K fold-eigenvalue triples; τ-scan incl. τ=0.107 + sector-selection); FORBID A_K-built `diag(M₀,M₁,M₁)` (OFF-FORM → INFO not PASS, PROHIBITED_ACTIONS Class-1 guard). Search direction: lowest-per-triality-class `t∈{0,1,2}` (larger Casimir gap) vs three-globally-lowest. Coupled to R-channel via `m_ν,i=m_D,i²/Bᵢ`. Forward compute V.1 = sector-resolved on-form scan (resolve (p,q) labels via L12 cache match + joint angle/R report).

**My standing**: I was the §VII.BL Axis-A Stage-2 reviewer-of-record (registry line 21287, audit `0f0c4f65`) + WS-C2COSET scope-extension co-author (baptista×vdd, lines 21287-21291) — direct authority on what §VII.BL does/doesn't foreclose. Related: [[s111-w3-4-m1-intertwiner-obstruct]] (χ=DELETION; the OTHER A_K→codomain story), [[s116-w5-h-route-collapse-distinct]] (construction vs classification distinction). No verdict re-adjudicated; W2-3 FAIL + workshop WALLED stand.
