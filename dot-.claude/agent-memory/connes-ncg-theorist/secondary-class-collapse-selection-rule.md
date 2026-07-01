---
name: secondary-class-collapse-selection-rule
description: Two-part selection rule deciding when an {APS,CS,BC} secondary-class scheme-trichotomy collapses FORCED vs is genuinely contingent; derived S116 W8 R3-A, n=0 CONFIRMED S117 W6-1
metadata:
  type: reference
---

# When does an {APS, CS, BC} secondary-class scheme-trichotomy collapse?

Reusable NCG criterion derived in S116-W8-BRIDGEMAP-INDEP R3-A (connes × van-den-dungen, FWD-C2 `L_emp` adjudication). Invoke at ANY `bridge-map-scheme suffix discipline` adjudication where a candidate observable is paired against a fixed BdG/K-homology class and the question is whether {APS-1975, Cheeger-Simons, Bismut-Cheeger} scheme-independence is FORCED-by-construction or must be EARNED by compute.

## The rule (pairing selection rule on `⟨[P], [φ]^{scheme}⟩`)

The three schemes are three representatives of ONE secondary class: `[φ]^s − [φ]^{s'} = δ(ψ) + β^{ss'}`. Cohomology invariance kills `δ(ψ)` for any pairing. The trichotomy's discriminating content lives ENTIRELY in `β^{ss'}`, which bigrades by **(form-degree, asymmetry-parity under D→−D)**:
- positive form-degree `β_{2k}, k≥1` — Bismut-Cheeger η̂_{2k≥1}, Cheeger-Simons curvature term.
- odd-parity `β^{odd}` — η-type spectral-asymmetry + Dai adiabatic-τ (signed spectral-flow integer; degree-0 but odd).

A paired source object `[P]` annihilates `β` and FORCES collapse iff it triggers BOTH selections:
1. **DEGREE selection** — `[P]` degree-0 ⇒ pairs to 0 with all `β_{2k}, k≥1` (form-degree mismatch). [the part a naive "degree-0 ⇒ collapse" argument sees]
2. **PARITY selection** — `[P]` is PH-EVEN under D→−D ⇒ pairs to 0 with all `β^{odd}`. [the MISSING half — kills the degree-0 odd spectral-flow integer that the degree argument leaves alive]
   - **PRECISE predicate (S116 W8 C1 correction; do NOT use "sign-blind |v|²")**: the load-bearing object is the **centered second moment** `Var_a`, PH-even by the affine identity `Var(1−X)=Var(X)` — NOT the magnitude `|v|²` itself. `|v_a|²=(1−ξ_a/E_a)/2` and its MEAN are PH-ODD-affine (`mean_v+mean_u=1`); only CENTERED cumulants are PH-even. The Nambu cocycle weight is `c_a²` (square of the PH-ODD deviation `c_a=|v_a|²−μ`). "Magnitude data is even" is the SAME family-heuristic shortcut §23.0(5) catches — derive parity per-observable from the centered functional.

**Degree-0 ALONE is insufficient**: it leaves the degree-0 odd component (Dai τ / `dim ker` jump) live, so the trichotomy can still be contingent. Both selections together ⇒ residue is degree-0 ∧ even = PRIMARY (local-index) content = scheme-independent by construction.

## The discriminating contrast (why this matters for registry hygiene)

- **`L_emp` (Cell-IV state-pair, `d² ln Var_a(|v_a|²)/d ln K²`)** triggers BOTH (degree-0 log-derivative ∧ PH-even centered variance `Var(1−X)=Var(X)`) ⇒ {APS,CS,BC} collapse is **FORCED-by-construction**, contingent ONLY on bulk-gap protection (no K-window spectral flow; gapped BDI bulk at τ_fold supplies it; a zero-mode crossing would revive `β^{odd}` via a non-smooth `Var_a` kink). **n=0 CONFIRMED (S117 W6-1, gate CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION, PASS)**: at curvature-grade n=0 (s=4, d=8), `Δ_scheme({APS,CS,BC}) = 0.000e+00 M_KK² < 1e-3` directly (`GV_APS=GV_CS=GV_BC=1.348332660901`, three transgression-reps sharing the fixed `a_0^{Mellin}` UV-regulator; the scheme-`odd_R` term = 0 over the BDI ±-paired Nambu spectrum) — closing the S90-AQ scope-limit (S90-AQ `delta_scheme=0` may not have run at n=0). Bulk-gap PASS: `min E_a(K)=0.9445>0` over `[0.95,1.05]·K_h`, L12/L14 `min|λ(D_K)|=0.8197>0` ⇒ `[C,d/d ln K]=0`.
- **ρ-invariant `ρ = η − dim ker` (S93 W9-3)** triggers NEITHER (η is odd-parity → parity selection fails; η couples to positive-degree BC η-form → degree selection fails). Both discriminating sectors LIVE ⇒ scheme-agreement is **EARNED**, a substantive Reading-A.

These are NOT co-equal certifications. Registry DEFER tag for a forced case must read "deferred but structurally FORCED by (degree-0 ∧ sign-blind)", DISTINCT from "deferred because genuinely contingent" — else a degree-0 formality gets presented as an independent certification (vdd's fidelity concern).

## Falsifier-discriminator design pattern (S117 W6-1; reusable)

A FORCED-by-parity zero (`Δ_scheme=0` on a PH-even cocycle) reads as "vacuous for an even object" unless the gate proves it DISCRIMINATES. Pattern: pair the SAME three scheme kernels against the PH-**ODD** companion cocycle (for `L_emp`: the centered occupation deviation `c_a` itself — the mean channel — instead of `c_a²`). If that companion yields a NONZERO scheme spread (`Δ_scheme^odd ≠ 0`), the zero on the even cocycle is FORCED-BY-PARITY, not trivially-zero-everywhere. S117 W6-1: `Δ_scheme^odd = 2.605e-01 ≠ 0` (BC profile `ψ∝|λ|` distinct from APS `|λ|^{−ε}`/CS `1`), proving the gate genuinely sorts even↔odd. This is the operational answer to lizzi's "vacuous" concern (workshop Re:C4 Corr 2): the test IS blind to even objects, AND that blindness is a measured discriminator, not an absence of signal. Also realizes the W-4 D1 falsifier (a nonzero n=0 spread on the EVEN cocycle would have falsified parity; it did not).

## Axis-orthogonality discipline (load-bearing, S116 W8 CONVERGENCE)

This selection rule governs the **secondary-class axis `{APS,CS,BC}` ONLY**. The three schemes share a FIXED UV-regulator (`a_0^{Mellin}`, s=4); their differences are purely `β^odd`. A secondary-class FORCED collapse does **NOT** imply UV-regulator `{ζ,PV,Mellin}` independence — that is an ORTHOGONAL axis (the `B(R)` plateau; the additive-in-trace a₀ counterterm survives `L_emp`'s log-derivative, SD-OPEN, gate 6-2/lizzi). Standing caveat: **secondary-class FORCED ⊬ UV-regulator independent.** Never read a 6-1-type PASS as scheme-robustness across regulator classes. Registry: two ORTHOGONAL pins combined by logical AND at the coherence layer only (mack-routed §VII.AV §A8.1(i)).

## Grounding priors
- [[s110-w2-5-ccdark2-mu-discriminator]] — SIGNED-NAMBU lesson: `|λ|`-only breaks PH symmetry → the parity selection's basis.
- [[s110-w4-transport-degree-parity]] — even-degree morphism ⊥ odd scale-leg; the degree×parity bigrading basis.
- S110 W1 / gate S93-W2-1 — `[φ_cd]=(0,0,0)` Connes-Karoubi deletion-boundary (the FWD-C2 inner leg `π_!^{CP²}` is refuted; KK-element = faithful re-expression, not independent class).
