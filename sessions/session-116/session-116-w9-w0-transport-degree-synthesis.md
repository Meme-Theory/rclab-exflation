# Session 116 Synthesis: w0 under the §23 Per-Observable Transport-Degree Theorem — the W9 Anchor-Fidelity Gap is PROXY-ARTIFACT-TYPED (deg=0 T2-VACUOUS favored), NOT a BZ→pivot morphism

**Date**: 2026-06-28
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/session-116/workshops/s116-w9-saturation-adjud.md`
- `sessions/session-116/session-116-w9-workingpaper.md`
- `sessions/session-116/session-116-housekeeping.md` (§A1, §A8, §A9)
- `computations/session-116/s116_gate_verdicts.txt` (S116-W9-GTBUILDER-L15, line 77)
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-observable transport-degree scale-separation"` + corpus §23.0(5)
- `.claude/rules/phononic-framing.md §"Scale-and-channel-tagging for running/tilt observables"`
- knowledge MCP: `w0_FW=-0.918` (S58); `deg_T_BZ_pivot=2.0` (S110-CF-CV6B-DS-M4)

This is the **THIRD reading** of the W9 anchor-fidelity gap (feeding the W-5 workshop, `w0 spectral-derivability`, baptista×volovik). The W9 panel produced two readings — baptista's "separate Level-3 anchor-fidelity surface" and spectral-geometer's "reading-(B) Weyl-forced proxy artifact" — but **never applied §23**, because neither the KK-geometry nor the heat-kernel axis owns the bridge-map transport-degree machinery. That machinery is the cross-pillar-bridge / NCG axis (mine). I supply the §23 classification the workshop lacked.

---

## I. Session Outcome

**w0 is a dimensionless dark-energy EoS (mass dimension `d_A = 0`); by §23.0(5) its BZ→pivot scale leg is the trivial `M_KK^0 = 1`, so its entire transport degree sits in the dimensionless morphism.** On the structurally-favored reading w0's morphism is **T2-VACUOUS scalar, `deg(T_{BZ→pivot}) = 0`** — substrate w0 = pivot w0 = −0.918 — placing w0 in the **n_s class** (single-pole `s=3`, deg=0), NOT the A_s class (deg=+2 square-relation). **The W9 anchor-fidelity gap (w0_cac → −1.340827 vs −0.918, gap 0.422827) is PROXY-ARTIFACT-TYPED, NOT transport-typed**: it is sourced 100.08% by the λ_max-edge denominator of the branch-(iv) Zubarev proxy, and the running spectral edge λ_max is **not an admissible §23 morphism** (the morphism sector is Wodzicki-ratio / HKR fixed-pole even-degree; a running sup-norm has no heat-kernel image, no fixed pole, no continuum limit). The §23 machinery therefore **adjudicates the W9 binary in favor of the proxy-artifact reading** (spectral-geometer reading-(B)) and confirms the workshop's "de-reference the edge" diagnosis from an independent axis. The deg=0 verdict is **PROVISIONAL**: the morphism-extraction compute (CF below, distinct from the already-minted CF-S117-W0-ANCHOR-FIDELITY) is the formal discriminator, with a pre-registered dual outcome — deg=0 confirmation (joins n_s, no K-advance) vs residual deg≠0 (substrate-natural NON-SCALAR, candidate K=3 §23 instance alongside the reserved r/α_t slot).

---

## II. Key Results

### II.1 — w0's §23 dimensional class: d_A=0, scale leg trivial, degree in the morphism

**Result**: `d_A(w0) = 0` ⇒ scale leg `= M_KK^0 = 1`; transport degree carried entirely by the dimensionless morphism. **GEOMETRIC** (a structural property of the spectral-action BZ→pivot bridge map on the D_K spectrum at τ_fold; Level-1 single-τ-slice substrate-IS).

w0 is the dark-energy equation of state — substrate-first, the ratio of the a₀ Seeley-DeWitt zeroth moment (the "vacuum" partition term) to the a₂ Einstein-Hilbert moment, dressed by the impedance-effacement leakage `Γ_eff = 0.99970` (Volovik vacuum partition; `w0_FW = −0.918`, S58 four-fold-lock, `Superseded=False`). As a ratio of spectral moments it is **dimensionless**: `d_A = 0`.

The §23.0(5) dimensional-class indexing factors the composite bridge map by mass dimension:

```
(1)   B  =  ( M_KK^{d_A} scale leg )  ⊙  ( dimensionless morphism )
```

For `d_A = 0` the scale leg is `M_KK^0 = 1` (the 54.04-decade BZ→CMB-pivot unit conversion is absent — it would only enter through a `d_A = 1` `M_KK^1` leg). Hence the **entire** transport degree of w0 lives in the dimensionless morphism, which is EITHER:

- **T2-VACUOUS scalar** (`deg = 0`) ⇒ `w0^substrate = w0^pivot` (coincidence), OR
- **substrate-natural NON-SCALAR** (`deg ≠ 0`) ⇒ `w0^substrate ≠ w0^pivot` (divergence).

This is the same fork §23 applies to every running/tilt observable. The morphism sector is **even-degree** by the parity selection rule: same-class two-pole Wodzicki ratios carry `−2(s − s')`, HKR cohomology-class ratios carry `0`. The only odd-degree carrier is the `M_KK^1` scale leg, which `d_A = 0` excludes. So w0's classification reduces to: **is its dimensionless morphism the identity scalar, or a genuine non-scalar even-degree map?**

### II.2 — The d_A=0 ledger splits: w0 aligns with the n_s (deg=0) class, not the A_s (deg=+2) class

**Result**: w0 joins **n_s** (deg=0, single-pole `s=3`, T2-VACUOUS) in the d_A=0 SCALAR class; it is structurally DISTINCT from **A_s** (deg=+2, NON-SCALAR, square relation `A_s = H̃²`). **GEOMETRIC.**

The critical lesson from this session's other d_A=0 landings: **`d_A = 0` does NOT force `deg = 0`.** The session's own ledger is split:

| Observable | d_A | Pole / structure | deg(T_{BZ→pivot}) | Class | Anchor |
|:--|:--:|:--|:--:|:--|:--|
| **n_s** (tilt) | 0 | single-pole `s=3`, `1−n_s ∝ ε_H` | **0** (T2-VACUOUS scalar) | substrate = pivot | §A8.2; registry §VII.AU.OP-PROJ Element-3 |
| **A_s** (amplitude) | 0 | power relation `A_s = H̃²` | **+2** (NON-SCALAR, CC3) | substrate ≠ pivot | §A1; INV12-W3-5 PASS `cc3=2.000000` |
| **w0** (EoS) | 0 | single-pole `s=3` (a₂^{Mellin}), ratio of moments | **0 (FAVORED)** / TBD | substrate = pivot (favored) | THIS reading |

The discriminator between the two classes is the **dimensionless morphism's structure**, not d_A:

- **n_s** is a single-pole `s=3` tilt — the same observable at substrate and pivot, morphism = identity ⇒ `deg = 0`. (The canonical `deg_T_BZ_pivot = 2.0` on the M4 base does NOT confer +2 on n_s; n_s landed deg=0 precisely because the tilt is single-pole, not a square relation.)
- **A_s** is the SQUARE of the Mukhanov-Sasaki variable, `A_s = H̃²` — a genuine power-2 relation between the substrate H̃ and the pivot amplitude ⇒ `deg = +2`. The +2 is visible in the observable's DEFINITION (the power-spectrum quadraticity = CC3).

**w0's structure matches n_s, not A_s.** Two structural facts:

1. **Single-pole, no square relation.** The branch-(iv) Zubarev route to w0 is pinned at the a₂^{Mellin} pole (`poleconv-A-double, pole_in_s=3, curvature_grade_n=2`; W9 verdict line) — the SAME pole as n_s. w0_FW = −0.918 is a closed-form vacuum-partition value, NOT a power/square of another observable. w0 carries no A_s-type `O = (O')²` signature that would source a `deg = +2` morphism.
2. **The gap is additive, not multiplicative.** `w0_cac → −1.340827 = −0.918 − 0.422827` is an **additive O(0.4) shift** on an O(1) observable. A `deg = +2` morphism is a power/factor relation (A_s: `oom_{A_s} = 2·oom_{H̃}`); w0's gap carries no such power signature. An additive shift is the signature of an additive proxy contamination (the λ_max-edge `−1` limit), not a graded transport.

A single-pole `s = 3 = s'` Wodzicki morphism has degree `−2(3−3) = 0` — the scalar case. So the §23 prior for w0, absent any square-relation, is `deg = 0`, **T2-VACUOUS scalar**, `w0^substrate = w0^pivot = −0.918`.

### II.3 — Gap typing: the λ_max-edge denominator is NOT an admissible §23 morphism ⇒ PROXY-ARTIFACT-TYPED

**Result**: the W9 anchor-fidelity gap is **PROXY-ARTIFACT-TYPED** (the λ_max-truncation-edge denominator), NOT a real BZ→pivot transport morphism. **GEOMETRIC.** This independently confirms the workshop's spectral-geometer reading-(B).

The W9 Structural Verdict establishes the exact decomposition (verified to the digit by both panelists, Sage QQ exact-rational):

```
(2)   ρ_B  =  mean_Z / λ_max  −  1
              └ bottom ┘  └ edge ┘
              FROZEN       Weyl-linear (∂λ_max/∂L = 0.375)
              (FB-saturated, mean_Z ≈ 1.9879)   (no continuum limit)
```

with the entire ρ_B shift carried **100.08%** by the λ_max denominator (mean_Z channel `−0.08%`; W9 R2/R3 channel split, confirmed both sides). Under CAC the substrate-IS asymptote is, with `mean_Z` frozen and `λ_max → ∞`:

```
(3)   ρ_B → −1   ⇒   w0_cac → −1 + offset_B = −1.340827   (gap 0.422827 from w0_FW = −0.918)
```

**Substitution chain — why the gap cannot be a §23 transport morphism** (per `math-scripts.md §"Double-Check Logic"`, the structural claim "the gap source is not an admissible §23 morphism"):

```
Step 1   Gap source (W9):  Δ(w0_cac) is 100.08% the λ_max denominator of (2);
         the FB-saturated numerator mean_Z is frozen (Δ ≈ 2.6·10⁻⁴ over {13,14,15}).
Step 2   §23 admissible morphism sector (§23.0(5) parity rule):
         { Wodzicki same-class two-pole ratio: deg = −2(s − s')  (fixed poles, even) ;
           HKR cohomology-class ratio:          deg = 0          (even) }.
Step 3   Identify λ_max:  λ_max(L) = max{ |λ_k| : p+q ≤ L } is the sup-norm of the
         RETAINED spectrum — the truncation boundary. Properties (spectral-geometer R3,
         independently verified): NO fixed pole; NO heat-kernel / Seeley-DeWitt image
         (a genuine cutoff Λ enters as f_n Λ^{d−n} a_n; a sup-norm does not); NO continuum
         limit (∂λ_max/∂L = 0.375, diverges with the truncation, by Weyl N(λ)~λ^d).
Step 4   Substitute: division by λ_max is NEITHER a fixed-pole Wodzicki ratio NOR an HKR
         cohomology-class ratio ⇒ it is NOT in the admissible morphism sector of Step 2.
Step 5   Therefore the −0.422827 gap is NOT a deg≠0 BZ→pivot morphism; it is the
         L→∞ artifact of a running-edge normalization injected by the S85 W0-7 Zubarev
         DEFINITION (the −1 offset + λ_max division), not substrate transport physics.
Conclusion   The W9 gap is PROXY-ARTIFACT-TYPED, not transport-typed.   ∎
```

The genuine fixed cutoff in branch-(iv) is `Λ_Z = 1` (the Gaussian regulator scale of mean_Z), which IS heat-kernel-representable and at which mean_Z converges to a finite physical value (reading-(A)). λ_max is the running truncation edge (reading-(B)). The §23 machinery makes spectral-geometer's reading-(B) into a **theorem-level statement**: λ_max-division is structurally outside the admissible-morphism class, so the proxy CANNOT asymptote to −0.918 with the λ_max denominator in place — not because of a real substrate≠pivot transport, but because the proxy's denominator is a non-substrate quantity.

`★ Structural point ─────────────────────────────`
The workshop and §23 converge from independent axes. Spectral-geometer used Weyl asymptotics (λ_max has no continuum limit); §23 uses the admissible-morphism sector (Wodzicki/HKR only). Both reach: the gap is the λ_max-edge proxy artifact, not transport. The §23 reading ADDS the discriminating prediction — the clean (de-λ_max'd) w0 should land at deg=0 (T2-VACUOUS, w0=n_s class), which is a computable, falsifiable degree, not just "de-reference the edge."
`─────────────────────────────────────────────────`

### II.4 — Coherence with the §23 ledger; no-demotion is respected

**Result**: the proxy-artifact verdict is COMPLEMENTARY to (not conflicting with) §A8 (n_s deg=0), §A1 (A_s deg=+2), and the SCALE-AND-CHANNEL-TAGGING "neither demoted" principle. **GEOMETRIC.**

The phononic-framing SCALE-AND-CHANNEL-TAGGING rule says the substrate-scale and pivot-scale values are BOTH real substrate-IS observables, "neither demoted," and their coincidence is set per-observable by `deg(T_{BZ→pivot})`. My proxy-artifact verdict does **not** demote a clean substrate value — because **−1.340827 is not a clean fixed-scale substrate value.** It is the L→∞ limit of a proxy whose normalization scale (λ_max) RUNS with the truncation. The no-demotion principle protects observables evaluated at a FIXED substrate scale (M_KK or Λ_Z); a running-edge-normalized quantity is not in that protected class, so recognizing −1.340827 as a proxy artifact violates no principle.

The clean fixed-scale substrate value (which no-demotion DOES protect) is exactly what the morphism-extraction compute returns. The two outcomes are coherently pre-registered:
- **deg=0** (favored): clean substrate w0 = −0.918 = pivot w0; w0 joins n_s; the −1.340827 was a proxy artifact (no real value demoted).
- **deg≠0**: clean substrate w0 ≠ −0.918; BOTH are real (no-demotion engages); the gap is a genuine substrate-natural NON-SCALAR morphism (w0 joins A_s/α_s in the NON-SCALAR class).

This is the structural reason the verdict must be PROVISIONAL: no-demotion is what would FORCE the NON-SCALAR reading IF a residual gap survives the de-λ_max'ing. The morphism-extraction CF is the discriminator that decides which regime holds.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S116-W9-GTBUILDER-L15 (compute) | INFO (sign=PASS, mag=INFO, regime=VALID) | `spread_CAC{13,14,15} = 0.0392902`; w0_cac → −1.340827; gap 0.422827 |
| S116-W9-SATURATION-ADJUD (workshop) | CONVERGED (artifact-existence) | `ρ_B = mean_Z/λ_max − 1`; gap 100.08% λ_max-channel |
| **This reading (§23 classification of w0)** | **deg=0 T2-VACUOUS FAVORED; gap PROXY-ARTIFACT-TYPED (PROVISIONAL)** | `d_A=0`; single-pole `s=3`; λ_max ∉ {Wodzicki, HKR} morphism sector |

Source-doc gate verdicts (the W9 compute INFO and the workshop convergence) are authoritative and not re-adjudicated. My contribution is the §23 transport-degree TYPING of the already-landed gap — a structural classification, not a numerical re-run.

---

## IV. Structural Implications

**1. The W9 binary is resolved by §23.** The workshop posed the gap as a binary — "proxy-normalization artifact vs real-but-separate Level-3 surface" — and routed it to S117 without typing it. §23 types it: **proxy-artifact** (the λ_max-edge is not an admissible transport morphism). The "separate Level-3 surface" framing (baptista's verdict-placement) remains correct at the **verdict-structure** level (anchor-fidelity ≠ L_max-stability, do not fold into the convergence cell); it is fully compatible with the **physical type** being a proxy artifact. The two analyses operate at different layers and agree.

**2. w0 populates the §23 d_A=0 ledger as a third entry — confirming, not advancing.** The §23 per-observable transport-degree theorem (`cross-pillar-bridge-anatomy.md §23`, SUGGESTION K=2) now has three d_A=0 instances classified by the same machinery: n_s (deg=0), A_s (deg=+2), w0 (deg=0 favored). This **confirms the machinery's per-observable discrimination** (d_A=0 does NOT force deg=0; the dimensionless morphism's structure decides). On the favored reading w0 does **NOT advance K=2→K=3**: a deg=0 scalar confirmation is not the "independently-factorization-EXTRACTED new-observable NON-SCALAR degree" the K=3 slot reserves (r / α_t).

**3. Conditional K=3 candidacy is compute-gated.** IF the morphism-extraction CF returns a residual `deg ≠ 0` after de-referencing λ_max, w0 flips to a substrate-natural NON-SCALAR instance and becomes a candidate K=3 §23 advancement alongside the reserved r/α_t slot. This is the ONLY route by which w0 advances the §23 K-counter, and it is gated on the compute returning deg≠0. Pre-registered as a dual-outcome below.

**4. Feeds the W-5 workshop (w0 spectral-derivability).** The W-5 panel (baptista×volovik) adjudicates whether w0 is spectrally DERIVABLE. The §23 typing is a structural input: on the favored reading, w0's substrate value IS −0.918 (single-pole scalar, the Volovik a₀/a₂ partition), and the branch-(iv) spectral route's apparent −1.340827 asymptote is a proxy-definition artifact, NOT evidence that the spectral derivation gives a different number. The W-5 workshop should treat "is the clean (fixed-scale) branch-(iv) w0 deg=0 (recovers −0.918) or deg≠0 (genuine non-scalar)?" as THE discriminator for spectral-derivability — the morphism-extraction CF supplies it.

**5. Constraint-map update.** The DR3 w0_FW = −0.918 falsifier surface is UNTOUCHED: −0.918 is the L_max-independent closed-form prediction (Volovik partition + effacement), and the §23 reading reinforces it as the substrate=pivot value on the favored reading. What is constrained is the **branch-(iv) spectral PROXY's** normalization: the λ_max-edge denominator is structurally disqualified as a transport morphism, so the proxy must be re-referenced to a fixed scale (Λ_Z / M_KK) before its asymptote can be read as a substrate value. This is a proxy-design constraint, not a prediction change.

---

## V. Carry-Forward Computations

> The already-minted **CF-S117-W0-ANCHOR-FIDELITY** (the {running-edge / fixed-edge / no-edge-normalization} design compute) and **CF-S117-BRANCH-IV-L16** are NOT relisted here — they propagate from the W9 WP. The CF below is the **distinct §23-degree-extraction** compute that sits ON TOP of the fixed-scale trajectory CF-S117-W0-ANCHOR-FIDELITY produces.

### V.1. CF-S117-W0-TRANSPORT-DEGREE — extract deg(T_{BZ→pivot}) for the clean (de-λ_max'd) w0 and classify it on the §23 axis

- **What**: On the fixed-scale (Λ_Z / M_KK) w0 representative produced by CF-S117-W0-ANCHOR-FIDELITY, EXTRACT the §23 transport degree `deg(T_{BZ→pivot})`. Apply (i) the Wodzicki same-class two-pole degree computation `deg = −2(s−s')` to confirm the clean w0 is single-pole `s = s' = 3` ⇒ deg=0, and (ii) the secondary-class scheme-spread test `Δ_scheme(B) → machine-zero` across {APS-1975, Cheeger-Simons, Bismut-Cheeger} (the degree-0 homogeneity signature, per the Composite Bridge-Map admissibility test). Output: the classified degree + the substrate-vs-pivot coincidence verdict. **Dual-outcome pre-registration** (`epistemic-discipline.md §"Dual-prior pre-registration as track-discriminator"`): Track-SCALAR prior 0.7 — `|deg| < tol` ⇒ w0 is a deg=0 T2-VACUOUS confirmation, joins n_s, `w0^substrate = w0^pivot = −0.918`, NO §23 K-advance; Track-NONSCALAR prior 0.3 — `|deg| ≥ tol` (and `Δ_scheme` non-vanishing) ⇒ w0 is substrate-natural NON-SCALAR, joins A_s/α_s, BOTH values real (no-demotion engages), candidate K=3 §23 instance alongside reserved r/α_t.
- **Inputs**: the fixed-scale ρ_B(L) trajectory from `CF-S117-W0-ANCHOR-FIDELITY` (DEPENDS ON it); `mean_Z(L)`, `λ_max(L)` trajectories {10..15} (+ L=16 from CF-S117-BRANCH-IV-L16); the n_s deg=0 anchor (registry §VII.AU.OP-PROJ Element-3, §A8.2); canonical `deg_T_BZ_pivot = 2.0` (S110, the NON-SCALAR reference degree); `w0_FW = −0.918`, `Λ_Z = 1`, `offset_Zubarev = −0.340827`, `M_KK`.
- **Gate**: NEW gate `S117-W0-TRANSPORT-DEGREE` — `[VERIFY]` + `[SIGN]` on the extracted degree. PASS-SCALAR iff `|deg| < 0.05` AND `Δ_scheme < 1e-3 M_KK²` (deg=0 T2-VACUOUS confirmed; w0=n_s class); INFO iff `0.05 ≤ |deg| < 2` (intermediate, indeterminate); PASS-NONSCALAR iff `|deg − 2| < 0.1` OR a clean non-zero even degree extracted (substrate-natural NON-SCALAR; candidate K=3). Composite feeds the §23 K-counter (advance ONLY on PASS-NONSCALAR with an independently-extracted degree).
- **Effort**: low-medium (~2-3 hours, 1 agent session — degree extraction + 3-scheme spread on existing trajectories; no new shell build). DEPENDS ON CF-S117-W0-ANCHOR-FIDELITY landing the fixed-scale trajectory first.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | w0 is `d_A = 0` ⇒ scale leg `M_KK^0 = 1`; degree entirely in the dimensionless morphism | GEOMETRIC | DERIVED (§23.0(5)) | w0's class reduces to scalar-vs-non-scalar morphism |
| 2 | w0's morphism is **deg=0 T2-VACUOUS** (single-pole `s=3`, no square relation) — joins n_s class, distinct from A_s deg=+2 | GEOMETRIC | FAVORED / PROVISIONAL | substrate w0 = pivot w0 = −0.918 |
| 3 | W9 anchor-fidelity gap (→ −1.340827, gap 0.422827) is **PROXY-ARTIFACT-TYPED** (λ_max ∉ admissible morphism sector) | GEOMETRIC | DERIVED (substitution chain) | adjudicates W9 binary → spectral-geometer reading-(B); confirmed from the §23 axis |
| 4 | Coherent with §A8 (n_s deg=0), §A1 (A_s deg=+2); no-demotion respected (−1.340827 is not a clean fixed-scale value) | GEOMETRIC | CONSISTENT | w0 is the 3rd d_A=0 §23 entry; complementary, not conflicting |
| 5 | §23 K-counter: w0 deg=0 is a CONFIRMATION, NOT a K=2→K=3 advance; conditional K=3 candidacy if morphism-extraction returns deg≠0 | GEOMETRIC | COMPUTE-GATED | dual-outcome pre-registered in CF-S117-W0-TRANSPORT-DEGREE |
| 6 | Feeds W-5 (w0 spectral-derivability): deg=0 ⇒ clean substrate w0 IS −0.918; the −1.340827 is proxy artifact, not a rival spectral value | GEOMETRIC | INPUT to W-5 | the deg-extraction is THE spectral-derivability discriminator |
