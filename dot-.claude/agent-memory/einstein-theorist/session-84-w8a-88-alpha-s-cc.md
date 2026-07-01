---
name: S84 W8a-88 alpha_s-CC cross-check
description: INFO-DECOUPLED verdict: Jacobian cross-entry d(Lambda_CC)/d(tau) is analytic zero (S44 permanent), while d(alpha_s)/d(tau) is nonzero. alpha_s and CC-regulator choice live in orthogonal sectors.
type: project
---

# S84-ALPHA-S-CC-CROSS-CHECK (§W8a-88) — INFO-DECOUPLED

**Verdict**: `INFO-DECOUPLED`. R_master = 0.000e+00 (exact analytic zero).
**Audit SHA**: `9686ee0133194441fe465574f4e3bbe7a8b0360bcb83459d233bbf4af4bb3b4d`
**Script**: `computations/s84_w8a_alpha_s_cc_cross_check.py`

## Why: the two structural facts that force INFO-DECOUPLED

1. **S44 permanent**: a_0(τ) = (4π)^(-d/2) · Vol(K) with Vol(K) τ-independent under volume-preserving Jensen deformation. Therefore ∂a_0/∂τ = 0 **exactly** (not "small" — analytic zero).
2. **Framework convention**: regulator f is fixed at pin time (not a function of τ), M_KK is a canonical constant (not a function of τ). Therefore ∂f_0/∂τ = 0 and ∂M_KK⁴/∂τ = 0 by construction.
3. **Product rule** on Λ_CC = a_0 · f_0 · M_KK⁴ gives ∂Λ_CC/∂τ = 0 for **all four regulators** (Gaussian, power_law, exp, smooth_step).

## How to apply: what INFO-DECOUPLED narrows

- α_s prediction is STRUCTURALLY INDEPENDENT of the CC-regulator problem. 34σ CMB-S4 discriminator for α_s is robust against regulator-choice disagreement in the CC sector.
- Measuring α_s provides ZERO constraint on which of {Gaussian, power_law, exp, smooth_step} is preferred. Two observational channels are orthogonal.
- The 110-115 OOM CC-gap is a property of **a_0·M_KK⁴ absolute normalization** ONLY. Resolution must live in a_0 or M_KK⁴, NOT in α_s cross-talk.
- Regulator-choice spread on absolute Λ_CC: a_0·f_0 ∈ {0.0480, 0.0541, 0.0541, 0.0576}·M_KK⁴ (~20% scheme spread); but on ∂Λ_CC/∂τ all four agree at exactly 0.

## Complementary observation: α_s IS τ-sensitive

∂α_s/∂τ ≈ −5.19e−02 via finite-difference on s30b_full_spectrum scenarios (gradient_balance τ=0.18, jensen_ref τ=0.35) — diagnostic only (via lmin-aggregate proxy), but nonzero confirms the Jacobian block-structure:

  J = [[ ∂Λ_CC/∂τ ],   =   [[ 0 ],
       [ ∂α_s/∂τ  ]]       [≠ 0]]

## Plan departure note (for S85 audit log)

Plan W8a-88 §4 cited two input files not on disk:
- `cc_gap_4_regulator_values.npz` — replaced by inline closed-form Mellin moments (exact at machine precision; stronger than cached file).
- `dk_spectrum_lmax10.npz` — fallback to `s30b_full_spectrum.npz` (L_max=10 sector lmin at 3 τ scenarios). Sufficient for finite-difference diagnostic on α_s; the Λ_CC side is analytic-zero regardless of spectrum data.

Both substitutions logged in audit_sha256 payload with `content_source` tags.

## Downstream hooks

- §W8-87b (A_F Birkhoff) can assume α_s is CC-independent
- §W8-90 (variational reformulation) can treat a_0 and a_2 as independent DoF (corroborates S83 L1/L2 layer-ordering)
- Carry-forward to S85: **NONE required**. Result is structural, not a new open item.
