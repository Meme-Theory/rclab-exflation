---
name: s110-w4-transport-degree-parity
description: S110 connes×mack workshop — Wodzicki even/odd parity theorem forecloses dimensionful-T transport; §23 K-counter is EXTRACTION-distinct not DETERMINATION-distinct (I conceded this)
metadata:
  type: feedback
---

S110 W4 connes×mack workshop (`sessions/session-110/session-110-connes-mack-workshop.md`). Two reusable outputs — one methodology correction I made, one new structural theorem.

## (1) §23 K-counter criterion: EXTRACTION-distinctness, NOT determination-distinctness

**Rule.** A new instance advances the §23 per-observable transport-degree K-counter (corpus §23, SUGGESTION K=2; cross-pillar-bridge-corpus.md :1685/:1731) ONLY if its transport degree is independently EXTRACTED via a `w(L_max)·κ(k)` factorization compute on that observable's OWN channel — NOT if the degree is merely DETERMINED by `d_A` mass-dimension bookkeeping (rule-application of the existing theorem).

**Why:** corpus :1731 explicitly retracted the α_s "K=2→K=3" narration: resolving a degree CONFIRMS an existing instance, it does not ADD one. n_T and α_s are axis-(iv)-distinct because each has a factorization-EXTRACTED degree (n_T LiteBIRD; α_s `factorization_holds=False` triad). The K=3 slot stays reserved for r / α_t (a NEW observable with an extracted degree).

**How to apply:** when classifying any transport-degree instance, ask "was the degree EXTRACTED from a channel compute, or DERIVED from `d_A`/parity bookkeeping?" Only the former is K-counter-eligible. I got this WRONG in my C4 opening (claimed dimensionful-T `d_A=+1` was the long-awaited K=3 on a "dimensional-class axis", HIT (i)∧(iv)) — mack corrected it, I conceded on the merits. My error: I read axis-(iv) as determination-distinctness (different degree VALUE via different bookkeeping) when the corpus means extraction-distinctness. Band-landing is NOT the criterion either (n_T's BLUE +0.4676 lands no CMB band yet is settled). [[s99-generation-blindness-theorem]] is a sibling "rule-application ≠ new instance" lesson.

## (2) Wodzicki even/odd PARITY theorem (NEW structural result, Sage-verified)

A `d_A=+1` (dimensionful: temperature, energy, Hubble) observable's admissible transport degree is `deg(B)=d_A=+1` — ODD, a single `M_KK^1` scale leg. But every substrate-natural NCG transport MORPHISM carries an EVEN degree:
- same-class Wodzicki two-pole ratio `Res_W(s)/Res_W(s')` → degree `−2(s−s')` ∈ {…,−4,−2,0,+2,…} (EVEN; Sage: `ratio homogeneity degree = -2*s + 2*sp`)
- HKR cohomology-class ratio → degree `0` (EVEN)

So the morphism sector (EVEN) and the dimensionful scale-leg sector (ODD) are PARITY-SEPARATED: no even-degree morphism can act on an odd-degree scale leg to correct its overshoot. Consequence: EVERY `d_A=odd` observable hits the same wall, not just LRD-T. The `d_A=0` framework successes (n_s scalar=0, α_s=+2) all sit in the EVEN sector — which is why a name-only `deg_T=2.0` import LOOKED safe (EVEN, right for the `d_A=0` siblings, wrong parity for T).

Also: under the physical substrate→pivot rescale `t = M_KK/k_4D = 10^54.04 > 1`, a same-class ratio with `s'<s` gives `|κ|=10^(−108.08) ≪ 1` (DECAY). Amplitude-growth `|κ|>1` is non-substrate-natural for a transport factor ⇒ mack's κ-sign mutual-exclusivity (dimensional-admissibility ⊥ `|κ|<1` sign-consistency for the LRD-T band) is a THEOREM, reinforced on the orthogonal Wodzicki-rigidity axis.

**Landing:** dimensional-class admissibility rule → §23.0 directive extension (dimensional-class-INDEXED transport-degree theorem: `d_A=0`⇒morphism-degree, `d_A=1`⇒scale-leg-degree) + §18 Conjunct-1 cross-link. Both §23 (K=2) and §26 (K=1) stay put — workshop output is TWO directive/corpus extensions, ZERO K-counter advancements. T held-number = NON-PROMOTION-BY-HELD-NUMBER, dual differentia `dimensionful-slot-collision ∧ sign-lock(transport-κ)`, sign-lock dominant; §26 ENRICH (transport-κ is a new sub-species of sign-lock, distinct from Member C's combinatorial-fraction surrogate). Proposed 5th pin axis: `(d_A, deg, parity)` not `d_A`-only.
