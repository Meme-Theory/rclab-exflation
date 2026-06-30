---
name: Modulus Kinetic Normalization — measure-check + a4 order-separation (S116-W4)
description: G_DeWitt=5 leading two-derivative modulus kinetic coeff is DERIVED + path-integral one-loop-measure cross-confirmed at rel=0 (S116-W4-MODULUS-PATHINT PASS, G_DeWitt anchor-only). a4 splits by operator order: Layer A (leading, derived) / Layer B (same-order delta COMPUTED S117 W5-1: c_B=1/60 Sage-exact, delta(fold)<0 sign-PASS, |delta|~O(1e-2) clean — NOT O(1)) / Layer C (four-derivative, separable, retires K_total=7.07 order-mixing artifact). Operator-coefficient vs numerical-dominance vs cross-coefficient distinction (3 axes).
type: project
---

## S116-W4 ZNORM-PROVENANCE Workshop Finding (kk × feynman, fork DERIVED vs FITTED)

**Context**: fork = is `Z = G_DeWitt = 5` first-principles-DERIVED or ASSUMED/FITTED? My (feynman) R1 charge: S74 path-integral IMPORTS the 5 (its mass-Hessian determinant never even imports `G_DeWitt`); "imported + silent + unchecked"; zero independent QUANTUM confirmations.

**My pre-registered discriminator = the one-loop fluctuation MEASURE** (FP det of `δ(det g−1)`; conformal/volume zero-mode Jacobian; fiber zero-modes — the channel where a non-Gaussian O(Λ⁰) shift of the kinetic coefficient could hide). The spawn `S116-W4-MODULUS-PATHINT` ran it and returned **PASS against my own charge**: `Z_lead = 5.000000000000`, `rel = 0.000e+00`, `G_DeWitt` ANCHOR-only (never enters `Z_lead`; audit `1148fd1b…`). Channels closed: conformal/volume mode DeWitt-ORTHOGONAL (`⟨∂_τ h,h⟩=0`); FP det τ-indep (`Tr(h⁻¹∂_τ h)=0`); fiber det well-defined (`|λ|_min>0`). **Gap-1 CLOSED, withdrawn.** Honest-outcome pattern: I named the test, it ran, the output settled it.

**Forced-geometry half (R1 Concession 1, adopted both sides)**: `G_ττ = (1/4)Σ n_i c_i² = (1/4)[3·4+4·1+1·4] = 5` over SU(3)→u(2)⊕C² branching `{3,4,1}` × Jensen `{−2,+1,+2}`. The only continuous DeWitt freedom `w` is killed by volume-preservation `Σ n_i c_i = −6+4+2 = 0` ⇒ `∂G/∂w = 0 ∀w`. No dialed coefficient ⇒ "fitted" structurally false.

## a4 Order-Separation (the emergent structure — the key lesson)

The a₄ sector SPLITS by operator order; do NOT lump it into one number:

| Layer | Operator | Order | Status |
|:------|:---------|:------|:-------|
| A (leading, a₂) | `(∂τ)²` | `[τ]+2` | `G_ττ=5` DERIVED, regulator-INVARIANT, measure-confirmed. Unconditional. |
| B (a₄ two-deriv) | `R_K(τ)(∂τ)²`, `R_4(∂τ)²` | `[τ]+2` | `δ`, SAME order ⇒ operative coeff `5(1+δ)`; OPEN; `O(1)` at fold. Load-bearing. |
| C (a₄ four-deriv) | `\|R_{μaνb}\|²`→`(□τ)²,(∂τ)⁴` | `[τ]+4` | SEPARABLE; cannot renormalize the `[τ]+2` 5. Retires `K_total≈7.07`. |

**`K_total≈7.07` RETIRED as an order-mixing ARTIFACT.** Sage fingerprint: the reported linear ratio 0.4865 and the reported total 7.0698 are inconsistent under EVERY simple combination law — linear `5(1.4865)=7.4325`; quadrature@0.4865 `√(5²+(0.4865·5)²)=5.5603`; reported `7.0698=√(5²+4.998²)` is quadrature@ratio **0.9996 ≈ 5√2**. Three mutually inconsistent readings ⇒ a `[τ]+2` coeff silently summed with a `[τ]+4` operator's value (inflated at fold, `∂τ~M_KK`, Mach 13.75). Not a value to reconcile.

## Operator-Coefficient vs Numerical-Dominance (the re-usable distinction — kk R3, I affirm)

- **Proposition (I)**: the LEADING two-derivative coefficient IS 5. Operator-coefficient statement: regulator-INVARIANT (`f_2Λ⁶` dressing cancels in the dimensionless field-space metric), `w`/τ-independent, measure-confirmed; INDEPENDENT of expansion convergence. DERIVED, unconditional.
- **Proposition (II)**: 5 is the NUMERICALLY-DOMINANT term in `5(1+δ)` at the fold. Regime-of-validity statement, governed by `ρ_B = R_K/Λ_eff² = −1.712 ~ O(1)` (single-scale fabric, NO `Λ≫M_KK` hierarchy). FALSE-to-marginal AT the fold; TRUE only for `|τ−τ_fold| ≳ X`.

Both control params `O(1)` at fold: `ρ_B = R_K/Λ² = −1.712`; `ρ_C = (∂τ)²/Λ² ~ O(1)` (Mach 13.75). `τ_fold` sits at the BOUNDARY of the expansion's radius of convergence — kk conceded, I affirm. `δ` propagates O(1) into friction `15H→15(1+δ)H`, `m_φ²∝1/(1+δ)`, e-folds `N∝(1+δ)`. (NOT `ε_V` — it's `≫1`/dynamically-inert at the impulsive transit; kk's sharpening.)

Registry tag = TWO non-conflicting clauses: **DERIVED** (leading coeff, unconditional) + **leading-order-scoped** (operative `5(1+δ)`, `X`-pinned). Standing scope: DERIVED *given S3* (SA-as-modulus-effective-action, ASSUMED, atlas-04) — separate axis, not a "fitted" charge.

## Gaussian δZ vs interacting δZ (conceded cleanly in R1)

A **Gaussian (free-field) one-loop measure renormalizes the two-derivative coefficient by EXACTLY ZERO** — `δZ` is the `O(p²)` part of the 1PI two-point function and needs internal loops at interaction VERTICES (cubic², or the derivative vertex `G'(τ)τ(∂τ)²`). No vertices ⇒ `δZ ≡ 0`. So `S116-W4-MODULUS-PATHINT` PASS does NOT touch the interacting `δZ`. The genuine Layer-B `δZ` is the soft-mode IR channel on the 35D ridge (near-flat directions, large `cond(H)`) — a light mode running in the loop can escape the naive `Λ⁻²` suppression. OPEN: `CF-S117-MODULUS-A4-GRADIENT`.

## Rule for Future Kinetic-Normalization / "Total Coefficient" Checks

1. **A forced/regulator-invariant LEADING coefficient can be exact while the EXPANSION is marginal at the evaluation point.** Never conflate "the leading coefficient is X" (operator-coefficient, scheme-invariant) with "X is numerically dominant" (regime-of-validity, governed by the control parameter at the actual evaluation point). Single-scale substrate ⇒ control params `~O(1)` at the fold by construction.
2. **Order-mixing fingerprint**: if a reported "total" coefficient does NOT close under any single combination law (linear, quadrature), suspect a silent sum of operators of DIFFERENT mass dimension. RETIRE the number; replace with an operator-order-separated set. Diagnostic: does `K_total = 5√2`? (quadrature-ratio 1) vs reported linear ratio → mismatch = order-mixing.
3. **"Expected a₄-suppressed by power-counting" ≠ "computed and confirmed a₄-suppressed."** Soft/flat modes (large `cond(H)`) are the named channel where naive `Λ⁻²` counting fails via IR enhancement. A free-field measure-check (PASS) does not close the interacting `δZ`.
4. **The discriminator that costs you a charge is the one worth having.** Pre-register the test that could go against your own position; report the verdict it returns.
5. **INFO-class order-separation gate — set `regime_verdict` on METHOD-exactness, not EXPANSION-convergence.** When a gate's deliverable is an order-separated coefficient set whose expansion is *designed* to be marginal at the evaluation point (the finding), the schema-v2 3-tuple composite-collapse (`regime=BREAKDOWN ⇒ composite=FAIL`) will mis-fire if you key `regime_verdict` to "is the a₄/a₂ expansion convergent at the fold." It is NOT (ρ~O(1) at the fold) — but that's the FINDING, not a method breakdown. Key `regime_verdict=VALID` on the symbolic-method exactness (Gilkey-a₄ + cached-Hessian δZ are exact at every τ), and report the convergence boundary `X` (smallest |τ−τ_fold| where ρ_B,ρ_C<ρ_max) as a SEPARATE diagnostic. Document the distinction in the gate block so it doesn't read as dodging a FAIL. (Pinned while authoring `CF-S117-MODULUS-A4-GRADIENT`, S117 W5 plan; `sessions/session-plan/session-117-plan-w5.md`.) Same pattern: `[SIGN]` axis on δ (sign exact = PASS-able) + magnitude=INFO (scheme-dependent via f₀/f₂) ⇒ composite INFO by design.

**Anchor**: `computations/session-116/s116_gate_verdicts.txt:41` (`S116-W4-MODULUS-PATHINT` PASS). Workshop: `sessions/session-116/workshops/s116-w4-znorm-provenance.md`. Upstream: `s63_kk_reduce_4d.py/.npz` (`R_K(τ)`, `S(τ)`, `K_total≈7.07`); `s74_lefschetz_gaussian.py/.npz` (consumer; 35D ridge Hessian). [T14] strengthening → `session-116-housekeeping.md §A4`.

## S117 W5-1 EXECUTION — CF-S117-MODULUS-A4-GRADIENT (INFO, the forward compute landed)

Verdict **INFO** (sign=PASS / magnitude=INFO / regime=VALID); `computations/session-117/s117_w5_modulus_a4_gradient.{py,npz,png}`; verdict `audit_sha256=7fc2ac4d…604e1`. Layer-B `δ` is no longer "OPEN" — it is COMPUTED.

**Sage-exact order-separated set** (a₄ R²-class `5R²+60RE+180E²`, Dirac `E=−R/4`; GCR `R = R₄+R_K−G_ττ(∂τ)²`, s63 line 553): `κ₂=−5G/12`, `κ₄^{RK}=−G/144`, a₄ R²-coeff `=1/288`. **c_B = κ₄^{RK}/κ₂ = 1/60**; c_4 = 1/60 (R₄→0 impulsive ⇒ 0 contribution); c_∂⁴ = G²/288; c_Riem = 1/180.

**δ(τ_fold) < 0 (sign_verdict PASS)**. `δ = (f₀/f₂)·c_B·(R_K/Λ_eff²)`; at f₀/f₂=1: `δ = (1/60)(−1.71217/2.04829²) = −0.00680`. a₂-contamination = 0 EXACT (order-split touches a₄ ONLY; G_ττ=5 untouched). K_total=7.0698 RETIRED confirmed = √(5²+4.998²), three inconsistent laws (linear 7.43, quad@0.4865 5.56, sqrt_2K=√10). δZ_1loop (interacting cubic vertex `g₃=δ'(fold)∝R_K'(fold)=+2.717`, soft-mode `Tr H⁻¹=0.510`) = 2.97e-05 — the interacting channel the free-field measure-check (δZ=0 EXACT) can't see; does NOT blow up (cond_H=8.06, no near-zero mode). Regime: ρ_B=|R_K|/Λ²=0.408 BINDING >0.30; ρ_C=ε_H=0.043 not binding; X=0.137 finite (track_A).

### Two re-usable lessons (sharpen rule #1 + the SIGN method)

1. **SIGN-via-RATIO is convention-robust.** Determine sign(δ) from the RATIO κ₄^{RK}/κ₂ (a₄ cross-coeff over a₂ coeff), NOT from the raw a₄ coefficient. Both carry the SAME `−G_ττ` factor from the GCR-reduced `R ⊃ −G_ττ(∂τ)²`, so the overall normalization N (spinor trace, (4π), sign convention) CANCELS in the ratio → sign(δ)=sign(κ₄/κ₂)·sign(R_K). A naive "compute c_B raw, divide by physical +5" FOOLS you: it mixes the raw-negative a₄ coeff with the physical-positive G_ττ (a hidden sign flip between κ₂<0 and the convention-flipped +5). I caught this mid-derivation — first-principle "don't fool yourself."

2. **THREE distinct magnitudes, do not conflate (sharpens rule #1).** (a) leading coeff `G_ττ=5` (operator-coeff, exact/regulator-invariant); (b) control parameter `ρ_B=R_K/Λ²=0.408` (governs a₄/a₂ EXPANSION convergence; O(1)→marginal at fold→the X-diagnostic); (c) the genuine same-order **δ = c_B·ρ_B carries the small Gilkey cross-coefficient 1/60 ⇒ |δ|~O(1e-2)**, NOT O(1). The S116-W4 "δ is O(1) at fold" mislocated the O(1): it lives in ρ_B and in the order-MIXED K_a4/K_a2=0.4865, NOT in the clean operator-order-separated δ (order_mix_ratio=0.014). Order-separation makes the leading 5 MORE dominant for the genuine [τ]+2 correction than K_total suggested.

3. **Plan-mislabel caught**: plan/S116 wrote "ρ_B=−1.712" — that is the RAW fiber curvature R_K, i.e. ρ_B's NUMERATOR. The dimensionless a₄/a₂ expansion parameter is `R_K/Λ_eff² = −0.408`. Both exceed ρ_max=0.30 ⇒ non-convergent-at-fold either way, but report the dimensionless 0.408 (the actual expansion parameter), not the raw 1.712.

4. **Canonical-drift S(ii.B)**: canonical_constants.py drifted plan-freeze→runtime (concurrent W0 constant-landings). BENIGN here (only canonical dep = tau_fold=0.19 immutable); audit_sha256 over runtime canonical, documented in companion row. Future parallel-session gates: expect canonical drift, check whether YOUR pinned constants moved (mine didn't).
