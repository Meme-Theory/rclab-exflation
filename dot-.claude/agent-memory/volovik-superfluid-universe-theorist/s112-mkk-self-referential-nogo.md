---
name: s112-mkk-self-referential-nogo
description: S112 W1-1 CF-S112-MKK-SUBSTRATE-ANCHOR FAIL — M_KK self-referential-unit-system no-go (lattice-QCD scale-setting analog); the §6.3 magnitude leg is a permanent external-import boundary
metadata:
  type: project
---

S112 W1-1 CF-S112-MKK-SUBSTRATE-ANCHOR closed **FAIL** (composite; 3-tuple sign=PASS / magnitude=FAIL / regime=VALID). This is the **registered no-go** (dual-prior Track-B → 0.95), NOT an agent failure (`math-scripts.md §"All Results Are Good Results"`).

**Claim falsified**: a substrate-natural dimensionful anchor Λ_anchor (no CODATA, no M_Pl routing) can fix M_KK = Λ_anchor·R(τ_fold) τ-RG-invariantly. **Result**: the §6.3 a(t)/effective-Friedmann **MAGNITUDE leg is a permanent external-import boundary** — the self-referential-unit-system no-go.

**Two-fold structural wall** (both pinned candidates, A=GAP-EMERGENT-LENGTH Δ_BCS·M_KK, B=EMERGENT-NEWTON √(a_2^ζ/48π²)·M_KK):
1. **leg1 unreachable by any τ-constant anchor**: `M_KK(τ)/M_KK(τ_fold) = R(τ)/R(τ_fold)` because both candidate anchors are `(τ-INDEPENDENT pure number)·M_KK`. The τ-non-flatness is intrinsic to `R(τ)=exp(−1/(λ_eff·N₀))` (range [3.6e-11, 0.16] over the scan), NOT a property the anchor magnitude can fix. max|R(τ)/R_fold − 1| = 1.0000 ⇒ leg1=False. Same reason the bare M_Pl anchor failed leg1 in S111 (M_Pl also τ-constant). Flattening would need an anchor whose OWN τ-flow cancels the van-Hove exponential — a fold-anchored canonical scalar cannot.
2. **magnitude leg self-referential**: every substrate spectral datum (a_2^ζ=2776.165389, Δ_BCS=0.4642547) is DIMENSIONLESS in M_KK units. So `Λ_anchor = M_KK·(pure number)` ⇒ the closed form maps `M_KK ↦ prefactor·M_KK`, fixed point only at M_KK=0. prefac_B=0.387730 (Δ_rel_B=0.612270), prefac_A=0.074359 (Δ_rel_A=0.925641); neither carries an INDEPENDENT GeV scale.

**Volovik-corpus analog (the structural blueprint)**: this IS the superfluid scale-setting lesson. A superfluid (³He-B substrate) predicts all DIMENSIONLESS ratios (Δ/E_F, ξk_F, c_⊥/v_F) from its gap equation, but the absolute energy scale E_F itself is an EXTERNAL input fixed by the microscopic Hamiltonian's bare parameters (atomic mass, density, scattering length) — you cannot bootstrap E_F from the dimensionless gap equation alone. M_KK = 1/R_K is the framework's E_F: the substrate measures EVERY observable in M_KK units, so the absolute GeV value is the ONE irreducible external anchor. The lattice-QCD analog (predict all ratios, input f_π / m_proton once to set the scale) is the same no-go in a third domain. See [[desitter-temperature-taxonomy]] for the related "which scale is physical" discipline.

**Structural twin in the framework**: the rank-1-Yukawa-wall "irreducibly external, not a refinable approximation" precedent (S100a INV2-W1-1) — see [[d5-seesaw-adjudication-100a]] for the suffix-discipline citation rule on such walls.

**Bit-exact continuity** vs S111/S110 CV2A: R_fold/λ_fold residuals 0.0, N₀ 1.78e-15 (all < 1e-9). R_fold=0.16016847970570353, λ_fold=0.038934760900644856, N₀_fold=14.023250234055.

**Downstream**: W1-2 (CF-S112-H0-BAND-CLOSURE, mack) consumes this FAIL → registered fallback: H0 relief CAPPED at the 6.125% dimensionless channel (band_closed=False), dimensionful remainder pinned to the external M_KK scale. §6.3 capstone routes capstone-hygiene Q1-YES + Q3-YES (magnitude leg irreducibly external). The substrate-natural anchors DO beat the bare baseline on magnitude (0.612/0.926 < S111's 8.193) but not into the 5e-2 PASS or 5e-1 INFO band — removing CODATA M_Pl removes a misnormalized anchor but replaces it with a pure-number multiple of the very scale being solved.

Artifacts: `computations/session-112/s112_mkk_substrate_anchor.py/.npz/.png`; verdict audit_sha256=3fa9be16e90ada96e6d1b0f43748b0ddc48626b1c428c1f01a769ed4561e39af.
