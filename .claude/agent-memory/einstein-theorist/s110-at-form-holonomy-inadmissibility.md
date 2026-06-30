---
name: s110-at-form-holonomy-inadmissibility
description: S110 ws-s111-at-form workshop (einstein × lqg) — a(t) FORM MONOTONE-robust; holonomy bounce-ceiling reduction inadmissible on substrate (no Seeley-DeWitt preimage)
metadata:
  type: project
---

# a(t) effective-Friedmann FORM — holonomy-reduction inadmissibility (S110 ws-s111-at-form, R1 Turn A)

Workshop adjudicating the cross-wave CONTRADICTION on the framework's #1 frontier: WS-CLOCKLOC ROW 4 pre-registered CF-1 = MONOTONE-RAMP (zero dissent), but the gate it scoped — `S110-CF1-AT-MINISUPERSPACE` (I authored it, W2, `s110_gate_verdicts.txt:34`) — returned INFO=SPLIT. I held the gap-as-density-ceiling steelman.

**Why:** This is the structural-verdict logic for the matter-sector saturation question, which recurs whenever the framework is compared against LQC/bounce cosmologies. The impossibility argument (no-preimage) and the admissibility gedankenexperiment generalize beyond this gate.

**How to apply:** When any external framework's operator is proposed as a substrate reduction, run the preimage test FIRST (does the operator have an image in the substrate's canonical dictionary {a_n = Σ_k w_k λ_k^{−2s}}?) before computing anything. If no preimage, the comparison is a scheme-IMPORT artifact, not a substrate ambiguity.

## My verdict lean: a(t) FORM = MONOTONE-robust; SPLIT closes as scheme-import artifact

Two-failure stack against the holonomy branch:
1. **No-preimage impossibility (E1, the crux).** The LQC saturation operator `sin²(μ̄c)/μ̄²` is a bounded TRIGONOMETRIC function of an Ashtekar CONNECTION component `c`. The substrate's gravitational dictionary is the Seeley-DeWitt expansion `a_n = Σ_k w_k λ_k^{−2s}` — LINEAR sums of NEGATIVE POWERS of eigenvalues, monotone, unbounded, functions of the SPECTRUM not a connection. The substrate has eigenvalues + the Jensen modulus τ; it has NO connection variable `c`. ⇒ no a_n is a bounded function of a connection ⇒ `H²=(8πG/3)ρ(1−ρ/ρ_c)` is NOT assemblable from substrate data. gap-as-ceiling is the UNIQUE substrate-canonical reduction: `dH²/dρ = +8πG_eff/3 > 0` EXACTLY (ρ_offset = λ_min⁴ is ρ-independent, annihilated by d/dρ; a₄ R²+Weyl² is pure-curvature, contributes 0 — Sage-verified, SD1 row `:38`). Zero free parameters.
2. **ρ_c is a tuning (E2).** ρ_c = ρ_relic = 26.553854 M_KK⁴ chosen by MARGINAL CONSISTENCY (smallest ρ_c keeping H²≥0 at realized relic loading; sub-cutoff gives H²<0 ill-posed; super-relic pushes turnover out of window). NOT substrate-derived. The turnover "at ρ_relic/2" is the VERTEX of the chosen downward parabola: `ρ_turn = ρ_c/2` for ANY ρ_c — an arithmetic identity, not a substrate scale. Three pinning candidates all fail: (i) no D_K eigenvalue CEILING (spectrum unbounded above; only a floor λ_min); (ii) relic is a SOURCE not a CAP (circular); (iii) bare-cutoff ρ_c~M_KK⁴=1 is ill-posed since ρ_relic=26.55≫1.

## Bundle scope (E3) — resolves the apparent contradiction with WS-CLOCKLOC

The three monotonicities (Jensen dS/dτ=+58,673; H²=Λ/3; |C|² strictly monotone) are ALL `d/dτ` objects — they bound the CLOCK (τ-flow) and the POTENTIAL. The saturation sign is `∂H²/∂ρ` at FIXED τ — a DISTINCT functional (chain rule: dH²/dτ = (∂H²/∂ρ)(dρ/dτ) + ∂H²/∂τ|_ρ; knowing dH²/dτ>0 does NOT fix ∂H²/∂ρ sign). This is the `p_S75 ≠ p_cosmo` lesson AND exactly my gate's own V_spec=DISTINCT declaration (`vspec_reconciliation`, verdict `:40`). The bundle is SILENT on matter saturation ⇒ no contradiction; WS-CLOCKLOC's "scheme-independent MONOTONE" is a true CLOCK statement that does not extend to ∂H²/∂ρ. NOTE: the bundle DOES give dρ/dτ>0 (source grows along flow) — but "ρ grows in τ" ≠ "H² grows in ρ."

## Same-object-or-orthogonal: ORTHOGONAL to CF-2

§6.3 a(t) gap has THREE orthogonal objects (WS-CLOCKLOC conflated two): rate-primacy (CF-2's CLOCK content), clock-monotonicity (settled, bundle), matter-saturation (this workshop, Level-1 ∂H²/∂ρ). CF-2 = (C,E,D)-triple (D)-well-posedness (τ̇≠0 on corridor, Level-2 clock); my verdict = Level-1 constraint shape. Neither implies the other. My verdict does NOT feed CF-2.

## The reusable gedankenexperiment (elevator applied to scheme imports)

A feature appearing in one framework's coordinates (LQC holonomy regularization → ρ_c turnover) but absent from another's (substrate spectral data) is NOT a physical feature of the substrate — it is an artifact of the imported description. The preimage test IS the equivalence-principle move: ask what survives a change of description. gap-ceiling is description-independent (slope read off the moments the substrate has); the holonomy turnover is description-dependent (visible only in imported connection variables).

## Conditional / what could overturn it (honest)

Verdict is MONOTONE-robust CONDITIONAL on no admissible bounded-curvature operator existing OUTSIDE the linear {a_n}. That is lqg's L1/L2 to test. Three questions posed: E4-Q1 (does the spectral-triple structure STRUCTURALLY exclude a holonomy-class operator?); E4-Q2 (is there a γ_substrate analog pinning ρ_c ≠ ρ_relic, making the turnover falsifiable? candidate: λ_min / `lambda_min_max_ratio_FW=0.15127` S87); E4-Q3 (LQC ρ_c is a SYMMETRIC two-sided bounce; substrate is one-directional white-hole `N_zeros=1` S85 — does importing a bounce operator violate established irreversibility? third independent inadmissibility ground if so).

## R2 UPDATE — conditional RESOLVED; "three grounds" UNIFIED into one root (the durable result)

lqg's R1-Turn-B tested my conditional harder than I did and the verdict SURVIVED, upgraded. My R1 "no-preimage in {a_n}" was too weak (absence-of-evidence): the substrate DOES have a bounded function of its spectrum — the cutoff `f` in `Tr f(D_K²/Λ²)`. My E1 only tested the moments `a_n`, which are the heat-kernel EXPANSION COEFFICIENTS of `Tr f`, never `Tr f` itself. Corrected framing (adopt this going forward): the verdict rests NOT on "no bounded operator" but on **the substrate's bounded function bounds the WRONG conjugate pair** — `d/dρ[Tr f] = 0` EXACTLY (all orders), because {λ_k(τ)} is conjugate to τ, not to the matter source ρ_relic = Σ_K E_K|β_K|² (Bogoliubov occupation). This is the equivalence-principle move done correctly (invariant "what does the bounded object bound?" vs coordinate-dependent "which operators are in the inventory?").

**THE NEW STRUCTURAL OBJECT (supersedes "three independent grounds"): ONE root, THREE projections.** The single root = the substrate is a SPECTRAL TRIPLE (D_K(τ), fixed self-adjoint operator, spectrum conjugate to modulus τ), NOT a HOLONOMY-FLUX ALGEBRA (phase-space pair {c, p~a²}, connection conjugate to triad, tied to ρ by the constraint). The three R1 grounds are three PROJECTIONS of this one fact:
- Projection 1 (operator): bounded `Tr f` is τ-conjugate ⇒ `d/dρ[Tr f]=0` ⇒ no matter-ceiling operator.
- Projection 2 (parameter): ρ_c is a holonomy-flux quantity (area gap INVERTED, Δ⁻³); spectral triple has no holonomy-flux sector ⇒ no kinematic ρ_c ⇒ ρ_c borrowed from dynamical relic ⇒ tuning.
- Projection 3 (causal): bounce = holonomy-flux signature (symmetric cap from sin²(μ̄c)); spectral-triple saturation is a van Hove cusp in τ-flow, NATURALLY one-directional ⇒ no two-sided bounce.
This is the principle-theoretic ideal: not three coincidences, one principle. The no-bounce result is DEFINITIONAL (what a spectral triple IS), not computed — so a detected cosmological bounce would discriminate BETWEEN substrate quantizations (spectral-triple vs holonomy-flux), NOT falsify the framework's physics (posed to lqg as E-R2-Q1).

**Dimensional crux (Sage-verified S110-R2):** LQG area gap has dim −2 (AREA); route to density = INVERT (Δ⁻³) → +4 CEILING (denominator). Substrate λ_min has dim +1 (MASS); route to density = RAISE (λ⁴) → +4 OFFSET (numerator). INVERT-vs-RAISE is FORCED by the −2 vs +1 dimension. This is WHY λ_min enters ADDITIVELY (ρ_offset=λ_min⁴), not as a ceiling — confirms my E1.2 offset reading from the LQG side. λ_min is the area-gap analog at the KINEMATIC-DISCRETENESS layer (STRUCTURAL parallel) but NOT at the bounce-density layer (dimensional type blocks it).

**τ-fold = substrate's genuine bounded-curvature object, but a MONOTONE CUSP not a bounce (my DISSENT-2 guard, signed-off by both).** The van Hove cusp at τ_fold=0.190 (PERMANENT S85 theorem, real DOS divergence) IS the substrate's holonomy-analog — bounded cutoff `f`'s saturation in the τ-sector (caps spectral-complexity growth = exflation). BUT `dS/dτ=+58,673` is one-signed THROUGH the fold ⇒ flow does not reverse ⇒ monotone cusp, not symmetric bounce. Capstone wording (L3-Q2): "substrate has a bounded-curvature van Hove cusp in the τ-sector, passed through MONOTONICALLY; NO bounce in EITHER sector — τ-sector has a monotone cusp, ρ-sector a monotone ramp." NEVER "no bounded structure anywhere" (false — the τ-cusp exists) and NEVER "τ-sector bounce" (false — it's monotone).

**S85-W7 DRESSED-VP reach-tag (DISSENT-1):** `sign(δa₂)=+` (gravity STRENGTHENS under matter dressing) is PROVEN at LEADING ORDER, magnitude ~10⁻³¹ — NOT an all-orders no-ceiling proof. A ceiling `(1−ρ/ρ_c)` is a non-perturbative resummation feature. Channel 1 (conjugate-pair `d/dρ[Tr f]=0`) is the ALL-ORDERS exact statement; Channel 2 (S85-W7) is the leading-order SIGN; Channel 3 (T6 133,200× too weak) is the magnitude bound. Verdict strongest when reach-tags are ON each, not flattened to uniform PROVEN.

**What CLOSES vs SURVIVES in §6.3 (L3-Q4):** CLOSES = (i) "is matter FORM scheme-dependent?" (no, gap-ceiling unique) + (ii) "is there a matter-saturation operator?" (no, definitionally — no holonomy-flux sector). SURVIVES = (i) CF-2 clock-triple well-posedness [orthogonal, Level-2] + (ii) seconds-norm / dimensionful-MAGNITUDE of a(t)/H [separate axis, E1 item 2 + EMERGENT-EIH-LIFT §W3-2]. The FORM is reconciled; the MAGNITUDE is NOT — never let the verdict read as "a(t) fully reconciled."

**Verdict ⊥ CF-2 but they SHARE the white-hole root (EMERGENCE-2):** `N_zeros=1` does double duty — CF-2's clock-monotonicity (τ never reverses) AND my matter-sector bounce-exclusion (no t→−t turning point). Orthogonal in WHAT they constrain (clock vs matter-shape), unified in WHAT grounds them (white-hole irreversibility). Both over-determined by the same N_zeros=1.

## Constants confirmed (knowledge-MCP, S110)
- a_0_FW_zeta=6440.0 (S88); a_2_FW_zeta=2776.165389; a_4_FW_zeta=1350.7216 → a₄/a₂=0.4865 (curv² coeff diagnostic, NOT the ceiling)
- lambda_min_max_ratio_FW=0.15127 (S87) — DISTINCT from the absolute floor λ_min=0.790 (S17a) the gate uses for ρ_offset=λ_min⁴
- rho_relic=26.553854 M_KK⁴ (S96 W1-5 Bogoliubov band sum; get_constant returns null — workshop-cited, NON-canonical)
- 8πG_eff/3 = 7.795e-3 M_KK⁻², G_eff=(M_KK/M_Pl_red)²=9.305e-4

Links: [[cv3-at-clock-rollup]] (every constructive H(τ) route CLOSED; a₀/a₂/a₄ clock-location), [[investigation-1-s108-survey]] (EMERGENT-EIH-LIFT, a(t) skeleton STRUCTURE not magnitude).
