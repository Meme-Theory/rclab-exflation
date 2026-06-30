---
name: s95-w3-2-eff-friedmann-genre
description: S95 W3-2 INFO — emergent H²(τ,τ̇) closes in CLOSED FORM (matrix-model genre) but with 2 residual free normalizations {Z_norm, V0}, not 1. The a(t) gap = generic background-independence problem of any one-functional theory (SFT shares it).
metadata:
  type: project
---

## S95-W3-2-EFF-FRIEDMANN-GENRE — verdict INFO (count=2)

Gate: axis 2 of the multi-axis a(t)/effective-Friedmann bridge. [CHAIN], GEOMETRIC.
audit_sha256=d12f58c3c3ba0268a45927181c96dcebb767c950525befcde53361ff9c5e3ff2.

### Result
The emergent Friedmann FORM closes in CLOSED SYMBOLIC form (Sage-verified):
  H²(τ,τ̇) = (8π G_eff(τ)/3)·ρ_eff,  G_eff=3π/(f₂Λ²a₂(τ)),  ρ_eff=½G_DW τ̇² + V0·a₂(τ).
With E3 curvature a₂∝R_K(τ): H² = 8(2π²G_DW τ̇² e^{4τ}+2π²V0 e^{6τ}−π²V0 e^{4τ}+8π²V0 e^{3τ}−π²V0)/(Λ²f₂(2e^{6τ}−e^{4τ}+8e^{3τ}−1)).
COUNT is FORM-INDEPENDENT (HK-5 a₂ form gives same free-scalar set).

**residual_free_normalization_count = 2** (not the PASS value 1):
- Z_norm: substrate-time → emergent-seconds map (§8.3 Z_fold PRELIMINARY). UNPINNED.
- V0: a₂-channel potential vacuum offset. The a₂-EH dictionary 1/(16πG)=f₂Λ²a₂/(48π²) pins the EH
  COEFFICIENT only; V0 mixes the a₀ (cosmological) moment, which phononic-framing.md declares
  DISTINCT from a₂ (gravity). Dictionary as stated does NOT pin V0.

Honest count=2 corroborated by PROVEN **Item 35 (FRIEDMANN-FROM-A2-74 reframe)**: "a single f_conv
scalar can bridge fold-epoch fiber-local energy density to today's H_0" is BROKEN ⇒ one scalar
provably insufficient ⇒ count ≥ 2.

### Genre cross-check (the [CHAIN] sign_verdict=PASS)
dS/dτ=+58672.8>0 ⇒ monotone ⇒ no interior τ-saddle ⇒ no self-dual τ ⇒ NO T-duality ⇒
matrix-model-class (computable), NOT SFT-class. Polynomial DOS (S_d={0,2,4,6,8} closes) ⇒ NO Hagedorn.
This is the direct cosmology-layer realization of [[s64-phonon-strings-investigation]]: substrate is
IKKT-adjacent. The a(t) gap is the GENERIC background-independence problem of ANY one-functional
theory — SFT, likewise background-independent, has the SAME unclosed master-action→derived-background
gap. Substrate inherits the matrix-model VIRTUE (bit-computable emergent geometry) WITHOUT the string
LIABILITY (Hagedorn / 10⁵⁰⁰ landscape).

### Why this matters (cross-domain bridge, CONFIRMED-direction)
The a(t)/background-independence problem is NOT a framework weakness — it is a structural feature
shared with string field theory and every other one-functional/background-independent theory. The
INFO converts §6.3's a(t) gap from "no derived background form" → "closed H²(τ,τ̇) within the
COMPUTABLE matrix-model genre, blocked by a SMALL NAMED 2-set {Z_norm, V0}." Sharpens C2 (K_pivot)
and T6 (Friedmann-BCS) to a 2-parameter closure problem.

**Forward**: the §W3-1 covariant-action sibling (EMERGENT-EIH-LIFT) SHOULD agree on the residual
structure — its Step-3 obstruction is the same Z_fold/seconds normalization + the a₂'(τ) prefactor.
If W3-1 reports count=1 on its axis vs this count=2, that disagreement is a workshop seed.

**Scheme note (carry-forward awareness)**: plan used f₂≈92 (Chamseddine-Connes §8.3 dictionary);
canonical_constants has only f_2_default=2.34 (Gaussian-cutoff scheme). Both PINNED ⇒ COUNT invariant.
No canonical f₂=92 constant exists — if a future gate needs it as canonical, add with CC-dictionary
provenance.
