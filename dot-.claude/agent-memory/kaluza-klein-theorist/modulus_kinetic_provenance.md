---
name: modulus-kinetic-provenance
description: Provenance structure of the 4D modulus kinetic normalization G_DeWitt=5 — which routes DERIVE it vs CONSUME it, and why the number is unambiguous
metadata:
  type: project
---

# Modulus kinetic normalization (G_DeWitt = 5) — provenance map

Q8 (S116-W4) gap is NOT the value but its PROVENANCE: derived vs assumed. Cross-route map (durable):

- **DERIVED (the one true source)**: `[T14] Kinetic Normalization Identity`, gate `KK-REDUCE-4D-63` (W6-25/S63), `s63_kk_reduce_4d.py`, atlas-07 PERMANENT. GCR (Gauss-Codazzi-Ricci) decomposition of the 12D spectral action on M⁴×SU(3) gives **G_tt = (1/4)[3·(−2)² + 4·(+1)² + 1·(+2)²] = (1/4)(20) = 5.0 EXACT, τ-independent**. The three Jensen blocks {su(2), C², u(1)} carry log-derivatives d ln g/dτ = {−2,+1,+2} and real-dim multiplicities {3,4,1} (SU(3)→u(2)+C²).
- **CONSUME (import G_DeWitt, do NOT re-derive)**: S74 path-integral `S[τ]=∫[½G_DeWitt(∂τ)²+V]` (`s74_lefschetz_gaussian.py` IMPORTS G_DeWitt from canonical_constants line 512); S64 `L_eff` anisotropic kinetic; S96-W1 `Z_norm` (= τ̇² coeff in H²(τ,τ̇)). S41 eq(25) only CLAIMS Z(τ) "derivable from 12D Einstein eqs", never executed.

## Two structural keys (the non-obvious part)
1. **w-independence by volume-preservation**: the DeWitt supermetric carries a conformal-weight-w trace term −w·(Σ nᵢ d ln gᵢ/dτ)². Volume-preservation gives Σ nᵢ d ln gᵢ/dτ = −6+4+2 = **0**, so the trace term vanishes and G_tt = 5 is **independent of w** — removing the usual DeWitt conformal-factor ambiguity. The number is FORCED geometry, no fitting freedom. Corroborated by Frobenius Kinetic Identity (W6-10): G_ab = Vol(K)·δ_ab.
2. **a₄ is the genuine open piece**: "exact 5" is only the LEADING (a₂) term. K_total ≈ 7.07 with the a₄ gradient correction (~41% shift), but that is an **OOM estimate only** — the precise `|R_{μaνb}|²` mixed curvature-gradient coefficient was never computed (W6-25 §Open). Any "modulus kinetic normalization is derived" claim is leading-order-scoped until that lands.

**Why:** future modulus-action / slow-roll / m_φ questions will hit "is G_DeWitt=5 assumed?" — the answer is no (GCR-derived, geometric), but the path-integral route has never independently reproduced it, so the S116-W4-MODULUS-PATHINT compute tests that (derive Z from the one-loop fluctuation determinant, NOT by importing G_DeWitt).
**How to apply:** when asked about the modulus kinetic term, lead with the GCR derivation + w-independence; flag a₄ as the open correction; never present S74/S41/S64 as independent derivations — they consume the GCR number. Constants live in canonical_constants.py + T14 (not here). See [[baptista_analysis]] for Jensen eigenvalue conventions.
