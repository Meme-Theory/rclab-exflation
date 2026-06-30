# Session 114 Slot-2 Closeout Synthesis: τ_fold Canonical-Value Convention + D4 Right-Regular SU(3)_R Admissibility

**Date**: 2026-06-24
**Agent**: phonon-first-cosmologist (cross-domain pattern detector; solo closeout synthesis)
**Source Documents**:
- `sessions/session-114/workshops/w-1-taufold-canonical-value.md` (transit × lizzi, 2 rounds, CONVERGED — output (iii))
- `sessions/session-114/workshops/w-2-d4-rightreg-su3r-admissibility.md` (vdd × baptista, 2 rounds, CONVERGED — output (ii) Reading-B)
- `sessions/session-114/session-114-housekeeping.md` (S114 Q2 ledger; §B CF-S115-VIICK-STAGE2-VERIFY; capstone-hygiene 5-Q gate)

**Both workshops have LANDED.** No HELD-PENDING degradation is needed. This document folds both verdicts, cross-checks where they touch the shared substrate (the Jensen-deformed SU(3) geometry at the fold), verifies every claimed in-session NON-MATH landing on disk, and enumerates the S115 `/rclab-plan` forward queue.

**Latest-synthesis-wins** (`epistemic-discipline.md`): the two workshop verdicts and their output-form selections are AUTHORITATIVE; this synthesis does NOT re-adjudicate them — it folds, cross-checks, verifies-landings, and routes.

---

## I. Session Outcome

**W-1 (τ_fold canonical value) — STRUCTURAL VERDICT: output form (iii), the three-functional NON-FUNGIBILITY convention.** The single canonical `tau_fold` is reframed as ONE of three distinct functionals of the eigenvalue density `ρ(λ;τ)`: `Φ_anchor` (the rational deformation-parameter freeze `tau_fold = 19/100 = 0.190`, CONST-FREEZE-42, the canonical pin's role), `Φ_cross` (the band-edge anticrossing argmin `tau_cross_van_hove = 0.191038`, the LOCATED feature), and `Φ_DOS` (the DOS singularity-strength argmax `0.221`). The canonical pin is NOT re-pinned; `tau_cross_van_hove = 0.191038` lands as a NEW registered observable. Reached from TWO independent routes — transit's cascade asymmetry (a value re-pin shatters the EXACT rational `S_0 = τ_fold/T_acoustic = 95/56`, trips an `assert` in `s101_w3_s0_knob.py`, and stales 119 registry rows) and lizzi's functional non-identity (no single number is simultaneously `argmin Δ_band` AND the exact rational 19/100). Both authors entered with OPPOSITE naive priors (transit→(i) re-pin, lizzi→(ii) 0.190-stands) and converged on (iii) because the analysis forces it.

**W-2 (D4 right-regular SU(3)_R admissibility) — STRUCTURAL VERDICT: output form (ii) Reading-B, with the externality-KIND tag `CLOSED-EXTERNAL-AS-A-COUPLING`.** Coupling Dirac fermions to the right-ROOT SU(3)_R generators `R_{E_α}` (the off-diagonal cross-generation operators a 3×3 mixing texture requires) is NOT an `A_K`-inner-fluctuation: the cross-generation handle carries center character `t(O) = ±1` while every `A_K` one-form carries `t(O) = 0`, so `0 ≠ ±1 (mod 3)` excludes it group-theoretically (EXACT ∀ L_max — W3-1's residual = 1.000000 is the numerical shadow). It is admissible ONLY via the canonical crossed product `A_K ⋊ SU(3)_R` (Kasparov external product), which enlarges the algebra. D4 discharges CLOSED-EXTERNAL-AS-A-COUPLING; the §VII.CK homogeneity-obstruction genus is COMPLETE as a statement about `A_K`-internal couplings; the SU(3)_R *symmetry* is substrate-internal (it is the commutant of `A_K`'s left-action, `‖[L_g,Y_R]‖_F = 7.25e-17`), only its *coupling* is external. The STAGE-1→STAGE-3-UNCONDITIONAL upgrade is a FUTURE Stage-2 gate, NOT a workshop output.

**Combined landscape.** Both Slot-2 workshops converged cleanly on a pre-registered output form and DECIDED a frontier item the S113 EVOI-frontier campaign had left open. Both sharpen the framework's "PERMANENT EXTERNAL-IMPORT SET" thesis on the SAME structural axis — the rank-1 / N₃=0 / commutant wall: W-1 confirms `τ_fold = 19/100` is a rational ANCHOR (an import that does load-bearing exact-rational work, not a derived spectral value), and W-2 confirms the generation-mixing SHAPE is external-by-enlargement (the substrate's own SU(3)_R symmetry cannot be gauged as a coupling internally). Together they tighten the framework by one closed door (D4) and one resolved value-convention (τ_fold), with NO status-cell flips and NO re-pins. The cross-domain bridge: BOTH verdicts hinge on the same Skolem–Noether `⊗ I_leg` leg-membership fact — for W-1 it makes 0.190 a rational anchor (the spectral functional has an empty critical set, so it cannot locate the cusp); for W-2 it makes `R_{E_α}` external (the leg-acting root operator is in the commutant the calculus cannot reach). One structural fact, two frontier resolutions.

---

## II. Key Results

### Result 1 — τ_fold is a three-functional non-fungible convention, not one number (W-1)

**Result**: `tau_fold = 0.190 = 19/100` (`Φ_anchor`, UNCHANGED canonical pin) + `tau_cross_van_hove = 0.191038` (`Φ_cross`, NEW registered observable) + `0.221` (`Φ_DOS`, the DOS-peak, already registered). Classification: GEOMETRIC (the spectral-triple deformation parameter and the band-edge anticrossing of `ρ(λ;τ)` — the fabric itself, not its excitations).

The substrate IS the van-Hove band-edge anticrossing of the D_K eigenvalue spectrum. The from-scratch crossing functional `Φ_cross = argmin_τ |T5_min(τ) − T3_max(τ)|` (T3 = (0,0)-sector MAX |λ|, T5 = (2,0)/(0,2)-sector MIN |λ|) LOCATES that anticrossing at `0.191038`, with NO `0.190` supplied to the finder. The result is regulator-robust by sector-locality (T3/T5 have p+q ≤ 2, so they ARE the bottom band at every L_max ≥ 2 — Friedrich-Bär saturation by sector-locality, no truncation tail to converge): L_max-INVARIANT across {5,8,10,12} to float precision, mesh-robust to Δ=1e-6, reproducing the independently-registered atlas-07 S45 TRUE crossing `0.19104` to 5sf. The Reading-A "0.55% is finder/mesh noise" form is REFUTED.

But `Φ_cross` is NOT the canonical pin's role. The canonical `tau_fold` is consumed as a RATIONAL ANCHOR: `S_0 = τ_fold/T_acoustic = (19/100)/(14/125) = 95/56` EXACT, the structural-selector winner of `S101-W3-S0-KNOB`. The load-bearing-ness of `19/100` lives on the exact-rational-identity axis: `CF(0.191038/0.112) = [1;1,2,2,1,1,18,44]` has a large partial quotient 18 ⇒ NO clean small-denominator convergent, while `19/100 → 95/56` is exact. The S0-KNOB gate's float PASS_BAND (0.01) is structurally BLIND to this distinction (the 0.55% registers at 7e-3, inside the band) — and the EMERGENT methodology datum is that the blindness IS the proof of functional non-identity: a precision-refinement cannot toggle a number-theoretic property on-and-off. The substrate IS the band-edge feature; `Φ_cross` locates it; `Φ_anchor = 19/100` is the rational role; the 0.5464% gap is the characterized round-number-freeze-vs-located-value offset between two real substrate-IS objects at different layers.

### Result 2 — D4 right-regular SU(3)_R coupling is CLOSED-EXTERNAL-AS-A-COUPLING (W-2)

**Result**: D4 → CLOSED-EXTERNAL-AS-A-COUPLING; §VII.CK genus COMPLETE on `A_K`-internal couplings. Classification: PARTICLE/GEOMETRIC (the representation-theoretic content of D_K — center characters, the SU(3)_R commutant, the inner-fluctuation calculus Ω¹_{D_K}(A_K)).

The substrate IS the SU(3) group manifold with its `SU(3)_L × SU(3)_R` bi-invariant isometry. The right-translation SU(3)_R is a genuine substrate symmetry — it is the COMMUTANT of `A_K`'s left-regular action (`[L_g, R_h] = 0` on `L²(SU(3))` IS `R_h ∈ (A_K^{left})'`; certified at `7.25e-17`), and its Peter-Weyl shadow is the multiplicity leg `ℂ^{m(p,q)} = (q,p)` carrying the three generations (`proven_384`). But a base-geometric symmetry is NOT automatically an admissible fermion coupling. Admissibility requires the generator to lie in the inner-fluctuation bimodule `Ω¹_{D_K}(A_K) + J_F Ω¹_{D_K}(A_K) J_F^{-1}`, and the cross-generation root operators `R_{E_α}` provably do not:

```
Center-character selection rule (the t(O)=±1≠0 parity; EXACT ∀ L_max, ∀ τ, ∀ regulator):
  Every A_K one-form a₀[D_K,a₁] has leg-image ∝ I_leg  ⇒  t(O)|_leg = 0  (coset-preserving; D3 Skolem–Noether).
  A cross-generation handle SHIFTS triality cosets  ⇒  t(O)|_leg = ±1  (necessary for 3×3 mixing).
  ⟨t=0 sector | t=±1 sector⟩ = 0  (distinct Z₃ center characters ⇒ orthogonal, ZERO overlap).
  ⇒ P_{Ω¹}(R_{E_α}) = 0  IDENTICALLY  ⇒  residual = ‖R‖/‖R‖ = 1  EXACT.
```

The center character `t = (p−q) mod 3` is conserved under algebra generation (products and commutators of `t=0` operators stay `t=0`), so enlarging the `A_K`-calculus can never manufacture a `t=±1` operator. The commutant argument makes this `A_F`-INDEPENDENT: by bicommutant logic, a non-scalar element of `A_K`'s commutant is exactly the class `A_K`'s own calculus can never reach. So the right-root coupling is admissible ONLY by the canonical crossed product `A_K ⋊ SU(3)_R` — the enlargement Reading-B asserts. The four-door genus `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` exhausts the possibilities for a leg-acting operator (either `t=0` calculus-internal, doors D1–D3, or `t=±1` non-scalar-commutant, door D4-external; no third place), so the genus is COMPLETE — promoted from CATALOGUE to THEOREM.

The externality is DISTINCT from (softer than) the closed M_KK-magnitude obstruction: M_KK holds the entire observable (a dimensionless-ratio-blind magnitude); the crossed product holds only a single overall coupling `g_R`, with the entire mixing texture and CP phase FORCED around it (`|U_ij|² = 1/3` coefficient-INDEPENDENT, `arg(w) = 2π/3`, `J = 1/(6√3) = 0.0962`). The forced texture is the named external corridor's live residue: quark-CKM FALSIFIED (both quark chiralities share the `M₃(ℂ)` leg ⇒ `U_mix → identity`, zero mixing, ≠ hierarchical CKM, ~3124×), lepton-PMNS RESONANT-CONDITIONAL (on the `ℂ⊕ℍ` charged-lepton-vs-neutrino sector-asymmetry, ~2.9× from observed).

### Result 3 (EMERGENT, cross-workshop) — the COMMUTANT-CALCULUS GAP, and its W-1 sibling

**Result**: a unifying structural law (W-2 EMERGENCE, vdd × baptista). Classification: GEOMETRIC (a theorem about which substrate geometric structures are admissible couplings on the spectral triple).

A base-geometric structure on `SU(3) → CP²` (a submersion shriek `π_!`, OR a right-translation isometry / connection `δA_R`) is admissible as a coupling on `(A_K, H_K, D_K, J)` IFF it factors through `Ω¹_{D_K}(A_K)`; the obstruction in BOTH incarnations is that the geometric object lives in a part of `B(H_K)` the calculus structurally excludes — the codomain-deficient part (§VII.CI shriek-vs-deletion) or the commutant part (§VII.CK isometry-vs-coupling). This unifies two previously-separate obstructions under ONE law with a predictive two-clause admissibility test (`t(O)=0` AND `A_K`-generated) for any future "SM-structure-from-SU(3)-geometry-for-free" proposal.

This is the cross-domain pattern my role exists to detect, and W-1 carries a SIBLING of it at the methodology layer: "the consumer gate passes either way, so the frozen value does not matter" is a Class-6-adjacent error whenever the value's load-bearing role is an exact-rational property the gate's float-band cannot resolve. Both are `phononic-framing.md §"Same-functional-different-scale"` instances — W-2 at the substrate layer (one geometric object, two parts of `B(H_K)`), W-1 at the methodology layer (one observable, a coarse gate-band reading and a fine exact-rational reading). The same structural skeleton — a small bounded subspace (the calculus / the float-band) cannot reach a property living outside it (the commutant content / the number-theoretic identity) — appears in both Slot-2 workshops. That is not coincidence; it is the Skolem–Noether `⊗ I_leg` fact read on two axes.

---

## III. Gate Verdicts

| Gate / Workshop | Verdict | Decisive Number / Output Form |
|:----------------|:--------|:------------------------------|
| W-1 τ_fold canonical value (transit × lizzi) | CONVERGED | Output (iii): three-functional non-fungibility; `tau_fold = 0.19` UNCHANGED, `tau_cross_van_hove = 0.191038` NEW; offset 0.5464% |
| W-1 (a) S85 uniqueness — VALUE or EXISTENCE | Converged | ASSERTS 0.190 (imported premise), PROVES only character (existence + non-stationarity + multiplicity); empty critical set `dS/dτ = +58672.80` |
| W-1 (b) τ_cross canonical?; ±0.5% band | Converged | `Φ_cross = 0.191038` real substrate-IS (L_max-invariant {5,8,10,12}); ±0.5% band = S85 drift-literal, no substrate meaning |
| W-1 (c) re-pin cascade scope | Converged | LAYER-1 survives (location-free); LAYER-2 breaks under re-pin (`S_0 = 95/56` shatters, S0-KNOB `assert` crashes, 119 rows stale) — avoided by (iii) |
| W-2 D4 admissibility (vdd × baptista) | CONVERGED | Output (ii) Reading-B; D4 CLOSED-EXTERNAL-AS-A-COUPLING |
| W-2 (a) R_{E_α} valid triple w/o A_K-enlargement | Converged | NO — `t(O)=±1≠0` selection rule; residual = 1.000000 EXACT; crossed product `A_K ⋊ SU(3)_R` required |
| W-2 (b) isometry-as-connection vs category error | Converged | Category error, `A_F`-INDEPENDENT; SU(3)_R is the commutant; `‖[L_g,Y_R]‖_F = 7.25e-17` |
| W-2 (c) §VII.CK scope consequence | Converged | Genus COMPLETE on A_K-internal couplings; upgrade STAGE-1→STAGE-3 is a FUTURE Stage-2 gate (two-clause separation) |

Source verdict lines (W3-1 routed-to inputs): `CF-S114-TAUFOLD-CUSP-CROSSING` INFO HYBRID, audit `7b637db142d9bea7…`; `CF-S114-YUK-RIGHTREG-CONNECTION` INFO (sign=PASS magnitude=INFO regime=VALID), audit `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`; W3-3 §VII.CK landing PASS, audit `51f411950ae58c74c635d40fa9fb711acdc9b0a172a5959da5cecc710738171f`.

---

## IV. Downstream Consumers

### W-1 (τ_fold) downstream consumers — mapped to registry/atlas/capstone/EVOI objects

| Object | Consumes | Effect of (iii) | Status |
|:-------|:---------|:----------------|:-------|
| `canonical_constants.py:289` `tau_fold = 0.19` | the pin value | UNCHANGED (no re-pin) | held |
| `canonical_constants.py:283` `tau_cross_van_hove` | NEW observable | ADDED 0.191038 | LANDED |
| `S101-W3-S0-KNOB` `S_0 = 95/56` | `Φ_anchor = 19/100` exact-rational | UNCHANGED (depends on 19/100 which (iii) does not move) | held |
| `s101_w3_s0_knob.py` `assert ...< 1e-15` | `tau_fold` value | UNCHANGED (no crash — re-pin avoided) | held |
| §VII.M.W10-3 S85 non-stationarity uniqueness theorem (`proven_1424`/`proven_1905`) | ASSERTS 0.190 | re-read ASSERTS-not-DERIVES; PROVEN content (character) survives location-free | LANDED |
| atlas-07 S45 TRUE crossing `0.19104` | the located feature | now CONSISTENT with `Φ_cross` (confirms to 5sf) | unchanged, agrees |
| §VII.CH NOHOLOFLUX (STAGE-3-PERMANENT) anchor block | `tau_fold = 0.190` | location-free Projection-3 survives; zero anchor-staleness under NEW-observable landing | held |
| S₀^geo Connes-route `(1/3)/ℓ_geo`, `ℓ_geo = τ_fold` | `tau_fold` value | band-insensitive (1.7544→1.7449, both in T1.0 band) | held |
| atlas-04 A4 (τ_fold assumption) | the value sub-status | RESOLVED to two-value non-fungible convention; A4 stays region-selected (NO tag flip) | LANDED |
| capstone §6.3 (the a(t)/effective-Friedmann fold-crossing) | the fold location | RESOLVED to two-value convention; substrate-IS arrow unchanged | LANDED |
| **EVOI Tier-2 #4 τ_fold-RELAXATION** | the value-conditional status | NOT YET updated — still reads "PARTIALLY CLOSED ... τ_fold = 0.190 is the last tuned number" | OPEN (plan-time maintenance; see V) |

The W-1 verdict touches the **a(t) / effective-Friedmann gap** ONLY at the fold-crossing-location level (capstone §6.3), and the resolution is ADDITIVE — it sharpens "imported value" to "region van-Hove-selected, value a two-value convention," and does NOT narrate §6.3 as closed. The §6.3 gap's surviving route (rank-1 normalization non-universality / the M_KK import) is UNCHANGED by W-1.

### W-2 (D4) downstream consumers — mapped to registry/atlas/EVOI objects

| Object | Consumes | Effect of (ii) Reading-B | Status |
|:-------|:---------|:-------------------------|:-------|
| §VII.CK SHAPE-Branch Homogeneity Obstruction (STAGE-1-CANDIDATE) | the D4-open scope qualifier | D4 row OPEN → CLOSED-EXTERNAL-AS-A-COUPLING (pending Stage-2 tag-flip); D1–D3 wall UNCHANGED; STAGE-1-CANDIDATE tag UNCHANGED | LANDED (D4-disposition annotation, registry 22430/22439/22458/22460) |
| §VII.BL WS-C2COSET (MAGNITUDE branch, STAGE-3-PERMANENT) | the companion relationship | cross-reference note: both branches' last internal doors now CLOSED by the commutant mechanism; grade UNCHANGED | LANDED (registry 21291) |
| `A_K = ℂ⊕ℍ⊕M₃(ℂ)` / gauge group `U(A_F)` | — | UNCHANGED — NO enlargement adopted; crossed product is the NAMED external corridor, not a framework commitment | held |
| §VII.CI (shriek-vs-deletion) | — | UNIFIED with §VII.CK under the COMMUTANT-CALCULUS GAP (EMERGENCE) | new law (in-workshop EMERGENCE; registry landing of the LAW itself is NOT claimed effected — see V routing) |
| **EVOI frontier (D4 admissibility)** | the dual prior 0.40 internal / 0.60 external | NO sagan-owned frontier row exists yet; W-2 supplies the discriminating-test verdict the row would key on | OPEN (plan-time maintenance; CF-S115-HK-1 in W3 WP; see V) |

The W-2 verdict does NOT touch the §7 falsifier surface / `falsifier-master-inventory.md` (mack's sole-writer domain): D4 is an internal-structure admissibility ruling, not an observational falsifier row. No inventory edit owed (confirmed in the W3 WP process observations + the housekeeping ledger).

---

## V. Cross-Verdict Consistency Check

**The two workshops share the Jensen-deformed SU(3) geometry at the fold, but consume DIFFERENT functionals of it — and they are mutually consistent. There is NO genuine cross-verdict tension. The consistency is STRUCTURAL, not coincidental.**

### Was τ_fold re-pinned? NO.

W-1's verdict is output (iii), which EXPLICITLY does not re-pin: `canonical_constants.py:289` reads `tau_fold = 0.19` (verified on disk, unchanged; the value `0.191038` lands as the SEPARATE observable `tau_cross_van_hove` at line 283). The W-1 "What Holds" section and the W2-working-paper constraint-map both confirm: "`tau_fold = 0.19` canonical pin UNCHANGED (CONST-FREEZE-42; `get_constant("tau_fold") = 0.19`, Superseded=False). No re-pin."

### Does that leave W-2's single-τ-slice D4 analysis unshifted? YES — and it would be unshifted EVEN IF W-1 had re-pinned.

W-2's 4-part discriminator and its D4 ruling ran AT the single-τ slice `τ_fold = 0.190`. Two independent reasons the W-2 verdict is robust to the (counterfactual) τ-value:

1. **τ_fold was not re-pinned**, so the literal slice W-2 ran at (`0.190`) is unchanged — the most direct consistency check.

2. **The D4 admissibility ruling does NOT depend on the precise τ value at all.** The decisive obstruction is the center-character selection rule `t(O) = ±1 ≠ 0`. The center character `t = (p−q) mod 3` is a representation-theoretic invariant of `A_K`'s image — it is EXACT at every L_max, every τ, every regulator (W-2 R2 CONVERGENCE, both agents). The W-2 verdict itself states: "residual=1 is the numerical shadow of the `t(O)=±1≠0` parity ... EXACT, ∀ L_max, ∀ τ, ∀ regulator." A 0.55% shift in the slice location (0.190 → 0.191038) would leave the triality cosets, the Peter-Weyl leg structure, and the commutant relationship `[L_g, R_h] = 0` completely unchanged — these are τ-independent group-theoretic facts. So the D4 ruling is unshifted by ANY value-only change to the fold location.

**Substrate reason (the cross-domain pattern).** Both verdicts hinge on the SAME Skolem–Noether `⊗ I_leg` leg-membership fact, read on two different axes:
- For W-1, `⊗ I_leg` (the spectral functional acts as identity on the multiplicity leg) is WHY the DOS/spectral-action functional has an empty critical set and cannot LOCATE the cusp — so `0.190` is a rational anchor, not a derived location, and the located value `0.191038` is a DIFFERENT functional.
- For W-2, `⊗ I_leg` (every `A_K` one-form is multiplicity-scalar on the leg) is WHY the root operator `R_{E_α}` (which is non-scalar on the leg, `t(O)=±1`) is OUTSIDE the calculus — so the SHAPE coupling is external.

This is one structural fact (the calculus is multiplicity-scalar on the generation leg) generating two frontier resolutions. The W-1 located value `tau_cross_van_hove` is a band-EDGE-gap observable on the `(0,0)/(2,0)/(0,2)` sectors; the W-2 D4 ruling is a center-character statement on the `(1,1)/(1,0)/(0,1)` generation legs. They operate on different sectors of the same spectrum and do not interact. **No tension; no NEW S115 item from the cross-check.**

### The one genuine cross-item the cross-check DOES surface (slot-overlap, NOT physics tension)

Within W-2's OWN downstream routing there is a same-slot relationship the S115 planner must NOT conflate (both touch §VII.CK):

- `CF-S115-VIICK-STAGE2-VERIFY` (housekeeping §B, from W3-3): verifies the **D1–D3 CLOSED class**, RETAINS the D4-open qualifier. Promotes STAGE-1-CANDIDATE → STAGE-3-PERMANENT for the closed class as registered.
- `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (W-2 CF-1, NEW): verifies the **D4 closure**, and on PASS-AND re-scopes §VII.CK to the COMPLETE genus and advances STAGE-1 → STAGE-3-**UNCONDITIONAL**.

These were pre-flagged "NON-colliding" in both the housekeeping ledger and the W-2 verdict, and that is correct — they verify DIFFERENT clauses (closed-class vs the fourth door). But they share the §VII.CK slot and have an **ordering/semantics dependency**: the STAGE2-VERIFY promotes the closed-class-with-D4-OPEN; the D4-DISCHARGE then re-scopes to D4-CLOSED-UNCONDITIONAL. The S115 planner MUST register them as two distinct gates with the explicit relationship (see §VI CF-1 / CF-2). This is a routing/sequencing flag, NOT a physics tension. It does not change either verdict.

---

## VI. Carry-Forward Computations (the S115 `/rclab-plan` forward queue)

**MANDATORY 4-field specs for every MATH carry-forward from both workshops AND the housekeeping ledger §B.** Where two CFs touch the same registry slot, the relationship and ordering dependency are stated explicitly.

### VI.1 — `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (W-2 CF-1; the D4 Stage-2 verify)

- **What**: blind two-agent cross-axis independent-verify (per `joint-theorem-promotion.md §"Stage 2"`) of the D4-external JOINT clause — "the right-regular `R_{E_α}` SHAPE handle is external-as-a-coupling (admissible only via the canonical crossed product `A_K ⋊ SU(3)_R` / Kasparov external product, outside `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` center-character selection rule), discharging D4 CLOSED-EXTERNAL-AS-A-COUPLING and completing the homogeneity-obstruction genus as a statement about `A_K`-internal couplings." On Stage-2 PASS-AND: §VII.CK re-scoped to the COMPLETE genus, tag STAGE-1-CANDIDATE → STAGE-3-PERMANENT-UNCONDITIONAL.
- **Inputs**: the registered §VII.CK entry (D1–D3 closed class + D4 row, `permanent-results-registry.md` 22430/22439/22458/22460) + W3-1 residual = 1.000000 EXACT (audit `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`) + the `t(O)=±1≠0` selection rule (W-2 Re:V1) + the commutant argument (W-2 Re:V2) + `proven_384` (`t=(p−q) mod 3`). Reviewers receive ONLY the registered entry + these inputs — NOT the W-2 transcript.
- **Gate**: `S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` — PASS-AND across BOTH axes (logical AND). Axis-A (NCG/spectral-functional NON-AUTHOR): `lizzi-spectral-functional-theorist` OR `spectral-geometer` (audits the `Ω¹_{D_K}(A_K)`-membership / selection-rule leg). Axis-B (substrate-geometry NON-AUTHOR, §VII.BL-NON-inheriting): `volovik-superfluid-universe-theorist` (audits the isometry-vs-coupling / commutant / crossed-product-image leg). EXCLUDED set: {connes-ncg-theorist, paasch-mass-quantization-analyst (YUKSHAPE Stage-0)} ∪ {van-den-dungen-bridge-theorist, baptista-spacetime-analyst (this workshop)} ∪ {kaluza-klein-theorist (§VII.BL companion reviewer-of-record `CF-S97-VII-BL-STAGE-2-VERIFY` + co-author, downstream-inheritance reach)} ∪ any other §VII.BL/§VII.CK/WS-C2COSET downstream-inheritance successor.
- **Effort**: ~1 wave (2 parallel cross-reviewers + 1 PASS-AND closeout).
- **Depends on / same-slot relationship**: shares the §VII.CK slot with `CF-S115-VIICK-STAGE2-VERIFY` (VI.3) but verifies a DIFFERENT clause (D4 vs D1–D3). Sequencing: STAGE2-VERIFY promotes the closed-class (D4-OPEN retained); D4-DISCHARGE then re-scopes to D4-CLOSED-UNCONDITIONAL. The two MUST be registered as distinct gates; do NOT conflate or merge. Audit-clean per `joint-theorem-promotion.md §"Audit at plan-freeze"` item 6 (the selection-rule/commutant machinery originates in this workshop + `proven_384`, so both reviewers apply machinery they did not author).

### VI.2 — `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` (W-2 CF-2; the lepton-resonance follow-up)

- **What**: construct the `A_K ⋊ SU(3)_R` right-regular circulant on the LEPTON multiplicity sector, impose the `ℂ⊕ℍ` charged-lepton-vs-neutrino sector-asymmetry (right-regular circulant on the neutrino/seesaw structure, coset-diagonal charged-lepton mass basis), compute the physical misalignment `U_mix = U_L^† U_R`, and test the forced tri-maximal `|U_ij|² = 1/3`, `J = 1/(6√3)` against observed PMNS `J ≈ 0.033`, `δ_CP` AFTER the charged-lepton correction. Pre-register: forced-and-surviving ⇒ the lepton residue is a zero-(mixing)-parameter prediction of the named external corridor; forced-and-washed-out ⇒ down-tag the lepton resonance to a symmetric-limit coincidence.
- **Inputs**: B2 Sage-exact forced circulant (`|U_ij|² = 1/3`, `J = 1/(6√3)`, `arg(w) = 2π/3`) + the W-2 sector-misalignment result (two circulants ⇒ `U_mix = identity`; one-circulant-one-coset-diagonal ⇒ tri-maximal, Sage-confirmed) + the `ℂ⊕ℍ` lepton-sector structure of `A_K` + observed PMNS `J`/`δ_CP` (PDG). CONTINGENCY pin: this tests the NAMED external crossed-product corridor, NOT a substrate-internal prediction — the contingency (coupling external-by-enlargement) stands regardless of outcome.
- **Gate**: `S115-LEPTON-PMNS-FORCED-TEXTURE` — `|J_forced − J_PMNS,observed| / J_PMNS,observed` after charged-lepton correction, against a pre-registered band (PASS if the corrected forced texture lands within the PMNS 3σ tri-maximal-deviation window; FAIL/down-tag otherwise). Negative control: the same machinery on `M₃(ℂ)`-shared quark chiralities MUST give `U_mix → identity` ≠ CKM (already established structurally).
- **Effort**: ~1 wave. Routes through `neutrino-detection-specialist` (PMNS owner) and/or `gen-physicist` for the circulant construction.
- **Depends on**: B2 + the W-2 Q3 sector-misalignment Sage result. INDEPENDENT of CF-1 (VI.1): CF-2 tests the corridor's residue; CF-1 closes the genus. CF-1 is NOT a prerequisite of CF-2.

### VI.3 — `CF-S115-VIICK-STAGE2-VERIFY` (housekeeping §B; the D1–D3 closed-class Stage-2 verify)

- **What**: two-agent blind cross-axis independent-verify of the §VII.CK D1–D3 closed-class SHAPE-Branch Homogeneity Obstruction; PASS-AND → promote STAGE-1-CANDIDATE → STAGE-3-PERMANENT (the D4-open scope qualifier RETAINED — the wall is verified as the closed class, not upgraded to unconditional).
- **Inputs**: §VII.CK registry entry (`permanent-results-registry.md`); W3-3 `audit_sha256=51f411950ae58c74c635d40fa9fb711acdc9b0a172a5959da5cecc710738171f`; D1 machine-exact reproduction; anchors `{γ₉,D_K}=0` (S34/S56) + multiplicity-leg generation id (`proven_384`).
- **Gate**: `S115-VIICK-STAGE2-VERIFY` — PASS = both cross-reviewers PASS-AND on D1/D2/D3 (Axis-A NCG/spectral + Axis-B structurally-distinct), BOTH excluding connes + paasch (YUKSHAPE Stage-0 authors) + downstream-inheritance successors per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection"`.
- **Effort**: ~1 wave (2 parallel verify agents).
- **Depends on / same-slot relationship**: shares the §VII.CK slot with `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (VI.1); verifies D1–D3 (NOT D4). This gate is the pre-existing W3-3 procedural promotion (already mirrored to `session-114-w3-workingpaper.md §"Carry-Forward Computations"` line 220 + housekeeping §B). The S115 planner picks it up via the WP CF mirror per its existing contract.

### VI.4 — `CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` (W-1 sole math CF; LOW-priority / CONFIRMATORY)

- **What**: re-run `s101_w3_s0_knob.py` with candidate (iii) routed as `q = 0.191038` (located crossing) instead of `q = Fraction(19,100)`, AND with the `assert abs(float(tau_f) - tau_fold) < 1e-15` guard relaxed to the substituted value, to mechanically confirm (a) the GRADED selector still selects (iii) and (b) `dev[iii] = 0.00682 ≤ PASS_BAND = 0.01` (gate still PASSes on (iii)); then Sage-confirm `CF(0.191038/0.112)` has no clean small-denominator convergent (large partial quotient 18) so the `S_0 = 95/56` exact-identity has NO analog at the located value.
- **Inputs**: `computations/session-101/s101_w3_s0_knob.py`; `s101_envelope_carrier_discriminate.npz` (`legC_output_form=GRADED`, `S0_fit=1.694153`); `canonical_constants.py` (`tau_fold`, `T_acoustic`); Sage `continued_fraction`.
- **Gate**: `S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` — PASS iff (selector selects (iii) under GRADED) AND (`0.00134 ≤ dev[iii]^{frozen}` and `dev[iii]^{cross} ≤ 0.01` both confirmed) AND (`CF(0.191038/0.112)` has a partial quotient ≥ 10 within the first 8 terms, certifying no clean small-denom rational). CONFIRMS the analytic verdict; CANNOT flip it (the exact-rational asymmetry is regulator-free arithmetic).
- **Effort**: Small (one script edit guarded behind a flag + one Sage CF call; ~15 min). LOW-priority / CONFIRMATORY — mechanical due-diligence, not a verdict-determining gate.

### VI.5 — Non-MATH plan-time maintenance items (route to `/rclab-plan` Step 1c-REGISTERS; NOT compute gates)

These are EVOI / register maintenance the S115 planner consumes; each is bookkeeping with no PASS/FAIL verdict line (sagan-owned per `evoi-prioritization.md`). Listed here so the planner does not miss them.

- **M1 — EVOI frontier-row add for D4 admissibility** (`CF-S115-HK-1`, already specced in `session-114-w3-workingpaper.md §"Carry-Forward Computations"` line 233). Add an EVOI `§EVOI` frontier row for "D4 — right-root SU(3)_R fermion-coupling admissibility," dual-prior 0.40 internal / 0.60 external as the P(pass) seed, keyed on the W-2 verdict (now LANDED) as its discriminating test. The W-2 verdict has DECIDED the row's discriminating test (CLOSED-EXTERNAL-AS-A-COUPLING), so the row can be entered as a DECIDED-at-S114 frontier item rather than an open question. Owner: `sagan-empiricist`. Effort: minutes-scale row insert.
- **M2 — EVOI Tier-2 #4 τ_fold-RELAXATION re-stamp.** The row (`evoi-framework.md` line 69) still reads "PARTIALLY CLOSED ... τ_fold = 0.190 is the last tuned number." S114 W-1 RESOLVED the value sub-status to the (iii) two-value non-fungible convention (region van-Hove-selected; value a convention, NOT an open compute). The re-stamp should reflect that the VALUE question is CLOSED-as-a-convention (no re-pin; `tau_cross_van_hove` registered), while the RELAXATION question (deriving WHY the region sits where it does — the dynamical-relaxation-or-empirical route, S95) remains the open Tier-2 leverage. Owner: `sagan-empiricist` at `/rclab-plan` Step 1c-REGISTERS EVOI staleness pass. Effort: minutes-scale.
- **M3 — (informational completeness, optional) exhaustive `Fraction(19,100)` exact-rational-consumer scan.** W-1 traced S0-KNOB + S₀^geo; an exhaustive scan for OTHER exact-rational identities keyed on `19/100` (vs mere numeric-0.190 citations) would complete the `Φ_anchor`-load-bearing ledger. NOT verdict-affecting (it can only ADD LAYER-2-under-re-pin items, all already avoided by (iii)). Low priority; route to `/rclab-plan` only if a slot is free.

---

## VII. In-Session NON-MATH Landings — Verification

Per `agent-standards.md §"Completion Verification"`: each claimed "Effected In-Session" landing was verified by reading/grepping the named target file by CONTENT (not line number — the two workshops landed concurrently, so cited line numbers can drift). All landings confirmed PRESENT on disk.

### W-1 "Effected In-Session" (lizzi, final agent)

| Item | Claim | Verified on disk | Status |
|:-----|:------|:-----------------|:-------|
| 1 | `canonical_constants.py` ADD `tau_cross_van_hove = 0.191038` (do NOT modify `tau_fold`) | `canonical_constants.py:283` assignment (`tau_cross_van_hove = 0.191038 # van-Hove band-edge anticrossing argmin ... NON-FUNGIBLE with tau_fold=19/100 ... verdict audit 7b637db1`) + `:2034` PROVENANCE dict entry (`"session": "S114", "source": "S114-CF-S114-TAUFOLD-CUSP-CROSSING"`) | **LANDED** |
| 1b | `tau_fold = 0.19` UNCHANGED | `canonical_constants.py:289` `tau_fold = 0.19 # S42 constants_snapshot, fold_idx=7` | **LANDED** (verified unchanged) |
| 2a | registry tag correction (BOTH roles) | `permanent-results-registry.md:2620` (`scheme=RATIONAL-ANCHOR-FREEZE (19/100, CONST-FREEZE-42), convention=anchors-derived-ratio-chain-S0-95/56; located-feature tau_cross_van_hove=0.191038 ...`) | **LANDED** |
| 2b | NEW registered observable `§VII-B.TAU-CROSS-VAN-HOVE` | `permanent-results-registry.md:2724` (`### VII-B.TAU-CROSS-VAN-HOVE — τ_fold Three-Functional Non-Fungibility ...`) + body (`tau_cross_van_hove = 0.191038`, three-functional non-fungibility, cross-references) | **LANDED** |
| 2c | S85 patch ASSERTS-not-DERIVES amendment | `s85_w10_tau_fold_REGISTRY_PATCH.md:11` (`ASSERTED-vs-DERIVED qualifier (S114 W-1 ...): The "= 0.190" ... is an IMPORTED PREMISE ... PROVES only the cusp's CHARACTER ... LOCATION is a SEPARATE substrate-IS observable ... Φ_cross = ... tau_cross_van_hove = 0.191038`) | **LANDED** |
| 3a | atlas-04 A4 RESOLVED to (iii) | `atlas-04-assumptions.md` §"In-cell freshness — S114" A4 clause (`RESOLVED the value sub-status to the two-value / three-functional NON-FUNGIBILITY convention ... rational anchor tau_fold = 19/100 (canonical pin UNCHANGED) + located feature tau_cross_van_hove = 0.191038 ... neither replaceable`; A4 stays region-selected, no tag flip) | **LANDED** |
| 3b | capstone §6.3 RESOLVED to (iii) | `phonic-exflation-equation.md:461` §6.3 S114 W2 note (τ_fold clause: `REGION van-Hove-SELECTED, value RESOLVED to a two-value non-fungible convention ... Φ_cross LOCATES it at 0.191038 ... tau_fold = 19/100 = 0.190 is the rational ANCHOR ... canonical tau_fold pin is UNCHANGED`; substrate-IS arrow unchanged) | **LANDED** |
| 3c | three S85-statement sources qualified ASSERTED-not-DERIVED | atlas-07 `:739` (`§VII.M.W10-3 | van-Hove-cusp non-stationarity uniqueness theorem (ASSERTS tau_fold = 0.190 as an imported premise ... PROVES only existence + non-stationary character ... LOCATION-free ...)`) + Phononic-framework-hypothesis `:431` (P-1 prose: `What the theorem PROVES is the cusp's CHARACTER, not its VALUE ... "= 0.190" is an IMPORTED PREMISE`) + `:598` (proven-results bullet: `ASSERTS tau_fold = 0.190 as an imported premise ... PROVES only existence + non-stationary character ...`) | **LANDED** (all three sources) |

### W-2 "Effected In-Session" (baptista, final agent)

| Item | Claim | Verified on disk | Status |
|:-----|:------|:-----------------|:-------|
| §VII.CK D4-disposition annotation (gen-physicist sole-writer, orchestrator-routed) | D4 OPEN → CLOSED-EXTERNAL-AS-A-COUPLING across the scope qualifier, the four-door table D4 row, and the D4-disposition paragraph | `permanent-results-registry.md:22430` (scope qualifier: `D4 ... now DECIDED — CLOSED-EXTERNAL-AS-A-COUPLING (S114 W-2 ...); closed-INTERNAL wall scope qualifier ... UNCHANGED`) + `:22439` (four-door table D4 row: `CLOSED-EXTERNAL-AS-A-COUPLING (S114 W-2; pending Stage-2 tag-flip)`) + `:22458`/`:22460` (D4-disposition annotation paragraph: full content — symmetry-internal commutant `7.25e-17`, coupling-external via `A_K ⋊ SU(3)_R`, `t(O)=±1≠0`, forced Z₃-circulant residue, quark-FALSIFIED / lepton-RESONANT-CONDITIONAL, upgrade owed to `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`) | **LANDED** |
| §VII.BL companion cross-reference note (baptista, co-authored domain) | records §VII.CK D4 now DECIDED by the same commutant mechanism; names the upgrade gate + the COMMUTANT-CALCULUS GAP | `permanent-results-registry.md:21291` (`Companion SHAPE-branch door (§VII.CK D4) now DECIDED — cross-reference note (S114 W-2 ...) ... both branches' last internal doors are CLOSED by the multiplicity-scalar / commutant mechanism ... CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL ... COMMUTANT-CALCULUS GAP`) | **LANDED** |

### Housekeeping §A items (orchestrator/mack/sole-writer; relevant cross-check)

The S114 housekeeping ledger §A records 8 in-session resolutions (capstone §6.3/§8.5 notes, atlas-04 freshness, the §VII.CK STAGE-1-CANDIDATE landing, chi_q_fold promotion, mack inventory rows). The two Slot-2-relevant ones — A4/§6.3 (W-1 τ_fold) and §VII.CK landing (the W3-3 base on which W-2 built) — are verified LANDED above (Items 3a/3b for W-1; the §VII.CK D4-disposition annotation extends the A4-ledger §VII.CK STAGE-1-CANDIDATE landing). No §A miss surfaced.

### Routing GAP found (NOT a landing miss — a mirror gap; route as S115 in-session-fix, NOT a re-derivation)

**The two W-2 workshop MATH carry-forwards and the W-1 confirmatory CF are NOT yet mirrored to any working-paper `## Carry-Forward Computations` block** — they live ONLY in the workshop files:

- `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (W-2 CF-1) and `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` (W-2 CF-2): the W3 WP `## Carry-Forward Computations` (line 218) carries ONLY the pre-existing `CF-S115-VIICK-STAGE2-VERIFY` + `CF-S115-HK-1` (both from W3-1, written before the W-2 workshop ran). The two W-2 workshop CFs are absent from the WP mirror.
- `CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` (W-1 sole math CF): the W2 WP `## Carry-Forward Computations` (line 222) reads "No carry-forwards: all three deciders resolved in-session" — written before the W-1 workshop ran. The W-1 confirmatory CF is absent.

**Why this matters** (`Investigating-Workshops.md` routing contract): `/rclab-plan` consumes WP `## Carry-Forward Computations` blocks (its existing contract reads WPs, not workshop files). A compute CF that lives ONLY in a workshop file is invisible to `/rclab-plan`. The workshop files were finalized AFTER the WP CF sections; the mirror was not back-filled.

**Route (S115 in-session-fix, targeted patch — NOT a re-derivation; the CF specs are already DECIDED in the workshop files):** mirror the three workshop CFs into the appropriate WP `## Carry-Forward Computations` blocks (W-2 CF-1/CF-2 → `session-114-w3-workingpaper.md`; W-1 CF → `session-114-w2-workingpaper.md`), OR have the S115 planner consume them directly from this closeout synthesis §VI (which carries all four 4-field specs verbatim). This synthesis IS now a complete, self-contained S115 forward-queue source for all four math CFs, so the gap is non-fatal — but the WP-mirror back-fill is the clean fix per the documented contract. Flagged for the orchestrator's S114-close / S115-plan-freeze; the fix is a mechanical mirror of already-decided specs, NOT new physics.

> **RESOLVED in-session (S114-close, orchestrator-direct, 2026-06-24):** the WP-mirror back-fill was executed per the no-technical-debt rule. The three workshop CFs are now present in the WP CF blocks `/rclab-plan` consumes — `CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` → `session-114-w2-workingpaper.md §"Carry-Forward Computations"`; `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` + `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` → `session-114-w3-workingpaper.md §"Carry-Forward Computations"` (each with a routing note citing its source workshop file). The mirror gap is CLOSED; no S115 in-session-fix owed. `CF-S115-VIICK-STAGE2-VERIFY` + `CF-S115-HK-1` were already present (W3-1-authored).

---

## VIII. Structural Implications

**The framework tightens on the rank-1 / commutant / N₃=0 axis with NO status-cell flips and NO re-pins.** Both Slot-2 workshops resolved frontier items the S113 EVOI campaign left open, and both land on the SAME structural thesis the S113 campaign headlined — the "PERMANENT EXTERNAL-IMPORT SET" forced by the rank-1 §VII.BS / N₃=0 wall:

- **W-1** confirms `τ_fold = 19/100` is a rational ANCHOR (an import doing exact-rational `S_0 = 95/56` work), not a derived spectral value — consistent with the S113 WS-2 finding "τ_fold-value better-constrained via the van-Hove cusp but value-imported." The (iii) convention makes the import EXPLICIT and NON-FUNGIBLE with the located feature, while leaving the canonical pin and every downstream identity intact. The located feature `tau_cross_van_hove = 0.191038` is now a registered substrate-IS observable that REMOVES a standing internal disagreement with atlas-07 S45 (which it confirms to 5sf).
- **W-2** confirms the generation-mixing SHAPE is external-by-enlargement — the substrate's own SU(3)_R symmetry (real, the commutant) cannot be gauged as a coupling internally, by the `t(O)=±1≠0` selection rule and the commutant theorem. This COMPLETES the §VII.CK homogeneity-obstruction genus on `A_K`-internal couplings (catalogue → theorem) and supplies a precisely-typed soft externality (`CLOSED-EXTERNAL-AS-A-COUPLING`) distinct from the harder M_KK-magnitude obstruction.

**The EMERGENT cross-workshop law (COMMUTANT-CALCULUS GAP) is the durable output.** It unifies §VII.CI (shriek-vs-deletion) and §VII.CK (isometry-vs-coupling) under one law with a predictive two-clause admissibility test, and it tells every future "SM-structure-from-SU(3)-geometry-for-free" proposal exactly where to fail. From the cross-domain perspective, this is the strongest kind of result my role looks for: the same structural skeleton (a bounded subspace cannot reach content living outside it) appears in BOTH Slot-2 workshops — at the substrate layer (W-2: the calculus cannot reach the commutant) and at the methodology layer (W-1: the gate's float-band cannot resolve the exact-rational identity). The unifying root is the Skolem–Noether `⊗ I_leg` leg-membership fact, read on two axes.

**What did NOT change.** No status-cell flips (atlas-04 A4/C2/C10 tags unchanged; §VII.CK STAGE-1-CANDIDATE tag unchanged pending Stage-2). No re-pins (`tau_fold = 0.19` held; `A_K = ℂ⊕ℍ⊕M₃(ℂ)` held; gauge group `U(A_F)` held). No §7 falsifier-surface edits (D4 and τ_fold are internal-structure objects, not observational falsifier rows). The a(t) / effective-Friedmann gap (capstone §6.3) is SHARPENED by W-1 at the fold-location level only — its surviving route (the M_KK import) is unchanged.

---

## IX. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | τ_fold = three-functional non-fungibility convention (Φ_anchor 19/100 + Φ_cross 0.191038 + Φ_DOS 0.221) | GEOMETRIC | CONVERGED — output (iii); no re-pin | The last tuned number is an explicit rational anchor; located feature registered; canonical pin + S_0=95/56 + 119 rows intact |
| 2 | D4 right-regular SU(3)_R coupling CLOSED-EXTERNAL-AS-A-COUPLING | PARTICLE/GEOMETRIC | CONVERGED — output (ii) Reading-B | §VII.CK genus COMPLETE on A_K-internal couplings; SHAPE is external-by-enlargement; upgrade to UNCONDITIONAL is a future Stage-2 gate |
| 3 | COMMUTANT-CALCULUS GAP (unifies §VII.CI + §VII.CK) | GEOMETRIC | EMERGED (in-workshop; LAW-landing not claimed effected) | One law + two-clause admissibility test for any "SM-from-SU(3)-geometry-for-free" proposal; route the LAW registration via S115 |
| 4 | tau_cross_van_hove = 0.191038 registered observable | GEOMETRIC | LANDED (canonical_constants:283 + registry §VII-B.TAU-CROSS-VAN-HOVE) | Removes the standing atlas-07 S45 internal disagreement; non-fungible with the rational anchor |
| 5 | S85 theorem re-read ASSERTS-not-DERIVES | GEOMETRIC | LANDED (3 source docs + patch) | PROVEN content (character) survives location-free; the "=0.190" is an imported premise, not a derived conclusion |
| 6 | Cross-verdict consistency: no re-pin ⇒ W-2 D4 slice unshifted; D4 ruling τ-independent anyway | — | VERIFIED consistent | No physics tension between the two verdicts; the one cross-item is a §VII.CK slot-overlap (sequencing, not physics) |
| 7 | WP-CF mirror gap (3 workshop CFs not in any WP CF block) | — | RESOLVED in-session (S114-close, orchestrator-direct) | The 3 workshop CFs mirrored to the WP CF blocks `/rclab-plan` consumes (W-1 CF → W2 WP; W-2 CF-1/CF-2 → W3 WP); gap CLOSED, no S115 fix owed |

---

## Closing Line

Two Slot-2 workshops, two clean convergences on the same structural axis: τ_fold is a rational ANCHOR (an explicit import, non-fungible with the located band-edge feature it approximates to 0.55%), and the generation-mixing SHAPE is external-AS-A-COUPLING (the substrate's own SU(3)_R symmetry lives in the commutant, which no algebra's calculus reaches non-scalarly). One Skolem–Noether `⊗ I_leg` fact, read on two axes, resolves both frontier items — and the two verdicts are mutually consistent because the D4 ruling is τ-independent and τ_fold was never re-pinned. The S115 forward queue is four MATH CFs (two §VII.CK Stage-2 gates that must not be conflated, the lepton-PMNS texture test, the W-1 confirmatory re-run) plus three plan-time EVOI/mirror maintenance items; every in-session NON-MATH landing is verified on disk, with one mechanical WP-CF mirror gap flagged as an S115 in-session-fix.
