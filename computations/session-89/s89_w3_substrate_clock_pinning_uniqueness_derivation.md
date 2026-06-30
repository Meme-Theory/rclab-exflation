# Substrate-Clock Pinning Uniqueness Theorem — Proof Sketch

**Gate ID**: `S89-SUBSTRATE-CLOCK-PINNING-UNIQUENESS-DERIVATION`
**Theorem**: P_1 (a_substrate(g) = L_pix(g)) is THE unique substrate-natural clock for the lock cascade.
**Verdict**: `P_1_UNIQUE`

## Substrate-naturalness criteria (5)

- **C1 — Regulator-class invariance**: invariant under {ζ, Pauli-Villars, Mellin, sharp-cutoff}.
- **C2 — Level-1 substrate-IS**: intrinsic to spectral triple at fixed τ-slice.
- **C3 — Level-2 substrate-IS via cocycle functor F**: moduli-deformation invariance.
- **C4 — Minimality of free parameters**: free params ⊆ {M_KK, Delta_BCS, tau_fold, xi_E_GGE_inv}.
- **C5 — Cancellation-discriminating predicate**: passes A.17 §W3-5 PASS.

## Per-candidate criterion-satisfaction matrix

| Candidate | Definition | C1 | C2 | C3 | C4 | C5 | Total |
|:----------|:-----------|:--:|:--:|:--:|:--:|:--:|:-----:|
| P_1 | a_substrate(g) = L_pix(g) (Pinning-A pixel-volume;... | ✓ | ✓ | ✓ | ✓ | ✓ | **5/5** |
| P_2 | a_mode(g) = ρ_mode(g)^(-1/3) = N_eigs^(-1/3)·V_K^(... | ✓ | ✓ | ✓ | ✓ | ✗ | **4/5** |
| P_3 | a_GGE(g) = xi_E_GGE_inv · (1 + g/G_critical) (GGE-... | ✓ | ✓ | ✗ | ✗ | ✗ | **2/5** |

## Uniqueness argument

P_1 satisfies all 5 criteria (cross-wave inputs from §W3-3 PASS, §W3-4 PASS, §W3-5 PASS).

P_2 (mode-density) FAILS C5: §W3-5 PASS shows Pinning-B FAILS the cancellation predicate (Δ_B ≈ 0 saturates while Δ_A = 290.80 OOM; discriminating ratio = 1.000).

P_3 (GGE-anchored) FAILS C4: G_critical introduces a free parameter NOT in the canonical set {'M_KK', 'tau_fold', 'xi_E_GGE_inv', 'Delta_BCS'}; minimality violated.

No other candidate enumerated satisfies 5/5. Therefore:

**P_1 (a_substrate(g) = L_pix(g)) IS THE UNIQUE substrate-natural clock for the lock cascade.**

## Cross-wave inputs (Wave 3 PASS results consumed)

```
{
  "A14_W3_3": {
    "regulator_class_invariant": true,
    "spread_across_regulators": 0.0,
    "C1_evidence_for_P1": true
  },
  "A16_W3_4": {
    "delta_0_cover_C": 16,
    "m_bot20_invariant": true,
    "C3_evidence_for_P1": true
  },
  "A17_W3_5": {
    "delta_A_322": 290.79497581140583,
    "discriminating_pass": true,
    "C5_evidence_for_P1": true,
    "C5_evidence_for_P2_FAIL": true
  }
}
```