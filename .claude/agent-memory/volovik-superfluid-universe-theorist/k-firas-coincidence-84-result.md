---
name: K-FIRAS Coincidence W5-65
description: S84 W5-65 INFO. K_FIRAS(L=5)=3.6808e5 vs S_IC^cap=3.5563e5 → 3.50% residual; L-invariant under primary Interp A; grows to 39.5% under diagnostic Interp B. NOT a structural identity.
type: project
---

# S84 W5-65 GATE-K-FIRAS-COINCIDENCE

**Verdict: INFO** — numerical coincidence (2 sig figs), not structural identity.

## Key numbers

- K_FIRAS(L=5) = K_base · μ_FIRAS / μ(K_base, L=5) = 2.035 · 9e-5 / 4.9759e-10 = **3.6808×10⁵**
- S_IC^cap (canonical) = 1 + 2 · S_fold / (8 · Δ_B3) = 1 + 2·250360.68/(8·0.176) = **3.5563×10⁵**
- residual(L=5) = |K_FIRAS − S_IC^cap| / S_IC^cap = **3.50%**
- ratio(L=5) = K_FIRAS / S_IC^cap = **1.0350**

## L-scan result (primary Interp A)

μ(K=2.035, L) and S_IC^cap(L) are both L-invariant by construction (plan directive: UV-extrapolated envelope + canonical-constant pins). Drift(5→9) = 0.00% exactly. Residual stays at 3.50% across L ∈ {5, 7, 9}.

## Diagnostic Interp B

Under Zubarev-energy-weighted mode-sum ansatz (μ ∝ S_Zubarev_E(L)), residual grows 3.50% → 34.58% → 39.52% at L=5/7/9. S_Zubarev_E sums: 6564.6 / 10385.1 / 11233.4 (monotone-convergent under Gaussian regulator).

## Structural consequence

FIRAS-IC-IDENTITY theorem candidate CLOSED. K_FIRAS and S_IC^cap are derivatively uncoupled — they share only the K-scale normalization. Plan synthesis rule §7.6 ("if W5-65 PASS → new permanent theorem for §VII") does NOT trigger.

The 3.5% agreement is a numerical coincidence reflecting both quantities riding the same GGE-relic K-scale; neither interpretation of L-dependence produces the monotone-shrinking residual that a truncation signature would require.

## Cross-checks (all PASS)

- CC1 K_FIRAS(L=5) vs plan 3.678e5: rel err 2.2e-4
- CC2 S_IC^cap vs plan 3.556e5: rel err 7.58e-5
- CC4 L=5 S_zeta vs S83 W3-G51 ref 159936: exact
- CC7 Interp B residual grows with L: confirms NOT truncation artifact

## Artifacts

- Script: `computations/s84_w5_k_firas_coincidence.py`
- Data: `computations/s84_w5_65_data.npz`
- Plot: `computations/s84_w5_65_plot.png`
- Closure SHA-256: `dd9d4cca6c30752b62475c5f0663098676627400447fca1d5d97aa4d92a668ad`

## Connection to Volovik program

Inheritance from 3He-B: even in parent BDI class, independent constraints from gap saturation and thermal-phonon window can agree numerically to few-percent without collapsing into a single algebraic identity. The FIRAS-IC agreement here is structurally similar — shared normalization through the GGE-relic K-scale, not common algebraic root.
