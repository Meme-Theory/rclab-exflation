# Session 88 Workshop W-30: lizzi x connes

**Date**: 2026-05-08
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: lizzi (lizzi-spectral-functional-theorist), connes (connes-ncg-theorist)
**Source Documents**:
- `sessions/archive/session-88/session-88-w10-workingpaper.md`
- `sessions/session-plan/session-88-plan-w10.md`
- `sessions/archive/session-88/workshops/_seed-w10.md`
- `sessions/permanent-results-registry.md`
- `.claude/rules/cross-pillar-bridge-anatomy.md`
- `.claude/rules/registry-landing.md`

**Focus Topics** (per schedule §W-30 invocation):

1. **(a) Per-pole HBW algebra-axis classification**: Per `cross-pillar-bridge-anatomy.md` MANDATORY-K=3, is per-pole HBW subset an algebra-INVARIANT spectrum-only functional family (Level-1 cohomology-class identity admissible per §W10-119 K=2 corpus) OR algebra-DEPENDENT state-pair functional (NOT registry-PASS-eligible as Level-1)?
2. **(b) §W10-111-NOW-5 SCHEMATIC↔PRIMARY pairwise-robustness sufficiency**: Does the in-session finding — that pairwise rel_diff structure + HBW subset cardinality are PRESERVED under SCHEMATIC↔PRIMARY rescaling at s=4 — suffice to promote s=4 HBW = {ζ, Zubarev} reading from SCHEMATIC SUGGESTION to canonical Level-1, OR is parallel PRIMARY rerun at s=3 with λ-derivative CM required to discriminate structural reading from parameterization-choice artifact?
3. **(c) Discriminating predicate for parallel PRIMARY rerun**: Does (L_max=10 PRIMARY at s=3) HBW match S87 W2's {ζ, anomaly} (substrate-IS per-pole reading robust) or shift toward S88 W10-111's {ζ, Zubarev} (parameterization-artifact reading confirmed)?
4. **(d) §W10-119 K-counter advancement rule**: When §W10-120 DORMANT shell activates at third pole s_new ∉ {3, 4}, what is the structural pre-condition for third-pole HBW subset to count as K-incrementing? Hybrid Independence Test satisfaction per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`? Is §W10-119 K-counter the SAME K-counter as cross-pillar bridge K=3-MANDATORY, or STRUCTURALLY-DISTINCT intra-Pillar-VII?
5. **(e) Projection-side suffix for §W10-119 sub-section**: Per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 — does HBW subset (pairwise admissibility predicates) qualify as STATE-PROJ requiring `§VII.X.STATE-PROJ` suffix?

**Cross-cutting**: substrate framing of "per-pole HBW divergence" — is the s=3 vs s=4 membership flip ({ζ, anomaly} vs {ζ, Zubarev}) a substrate-IS structural identity (per-pole IS its own structural fingerprint) or a (L_max, parameterization, threshold) tuple-shopping artifact?

---

## Round 1 — lizzi: Opening Analysis

### L1: Per-pole HBW algebra-axis classification (clause a)

**Position**: the per-pole HBW-positive subset is an **algebra-INVARIANT spectrum-only-functional-family observable** at the cohomology-class layer; admissible as a Level-1 cohomology-class identity per the §W10-119 K=2 corpus and per the algebra-axis orthogonality MANDATORY-K=3 clause at `cross-pillar-bridge-anatomy.md` lines 272-280.

**Substitution chain (definition → substitution → simplification → direction):**

```
Step 1 (Definition, algebra-axis K-counter line 278):
  algebra-INVARIANT family := { F | F({λ_k, m_k}) = Σ_k m_k g(λ_k) }
       (spectrum-only functionals — only the spectrum {λ_k} and multiplicities {m_k} enter)
  algebra-DEPENDENT family := { F | F = state-pair functional on A }
       (requires evaluation against the algebra A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) state space)

Step 2 (Definition, §W10-111 (b) line 197 evaluator):
  M^{(R)}_n(L_max) = (1/Vol_SU3_Haar) · Σ_{(p,q)≠(0,0), p+q≤L} d(p,q) · f_R(C_2(p,q), n)
       where f_R is the per-regulator Mellin kernel
       and the sum is over the SU(3) Casimir spectrum (Schematic) or canonical D_K Peter-Weyl spectrum (Primary).

Step 3 (Substitute the HBW predicate at fixed pole s):
  HBW_positive(R; s, L_max, ε) := ∃ R' ≠ R s.t. |M^{(R)}_{2s} - M^{(R')}_{2s}| / |M^{(R)}_{2s}| ≤ ε
  HBW_subset(s, L_max, ε)      := { R ∈ A_n | HBW_positive(R; s, L_max, ε) }

Step 4 (Simplify):
  Each M^{(R)}_n is a Σ over the spectrum {λ_k(p,q)} (PRIMARY) or {C_2(p,q)} (SCHEMATIC) with
  multiplicities {d(p,q)} or {16·d(p,q)} (PRIMARY-spinor). No state-pair evaluation against A_K
  enters. The HBW pairwise predicate is built ENTIRELY from {M^{(R)}_n}_R, hence ENTIRELY from
  spectrum-only functionals. The algebra A_K appears only through dim(p,q) Weyl-multiplicity and
  C_2 — both of which are spectrum-side data on the substrate algebra (Peter-Weyl decomposition
  of A_K), NOT state-pair occupation observables.

Step 5 (Direction):
  HBW_subset(s, L_max, ε) is a function of {M^{(R)}_n}_R and {ε} only. By the K-counter line 278
  identity-class definition, it is in the algebra-INVARIANT family. ⇒ Level-1 cohomology-class
  identity admissible per §W10-119 calibration corpus.
```

**Why the algebra-axis MANDATORY clause favors this reading**: the K-counter at lines 272-280 was promoted to MANDATORY-K=3 at S87 W-2 R3 close on the contrast `Mellin-Dirichlet identity (algebra-INVARIANT) vs Connes distance (algebra-DEPENDENT)`. The Mellin-Dirichlet identity is the §VII.U.1 anchor — and §VII.U.1 sits in the §W10-119 K=2 corpus alongside §VII.K-PROP.W10-4. Both K=2 corpus instances are algebra-INVARIANT spectrum-only quantities (§VII.U.1's `M^{(ζ)}_3 ≈ 2.97e-3` is Mellin-Dirichlet's residue at s=3; §VII.K-PROP.W10-4's `ρ_∞ = -0.8103647...` is the simple-pole fit's c_0 coefficient — neither requires state-pair evaluation). The HBW pairwise predicate inherits this algebra-axis classification by construction, since the per-regulator moments M^{(R)}_{2s} are the same family the K=2 corpus draws from.

**Two-layer reading (preempting connes' Re:L1 challenge)**: the HBW predicate carries both an OBJECT layer and a PREDICATE layer. The OBJECT layer (the moments M^{(R)}_{2s}) is unambiguously algebra-INVARIANT spectrum-only. The PREDICATE layer (the threshold-comparison `... ≤ ε`) is a CONDITIONAL applied to spectrum-only objects — the threshold ε is a regulator-class-discrimination tolerance, not a state-pair pairing. Predicate application to spectrum-only objects DOES NOT promote the result to algebra-DEPENDENT, exactly as the resolution-specificity scoping rule (`epistemic-discipline.md` §"Resolution-Specificity Scoping" Layer 1 anti-correlation extends pole-universally at machine precision per W12-148) admits a pole-universal F_2-class anti-correlation as algebra-INVARIANT despite carrying a predicate (`ρ_S = -1.0`). The predicate-application argument is the same here: HBW_positive(R; s, L_max, ε) inherits algebra-INVARIANT classification from its object layer.

**Conclusion (clause a)**: per-pole HBW-positive subset is **algebra-INVARIANT spectrum-only**. Admissible as Level-1 cohomology-class identity. The §W10-119 K=2 corpus is structurally well-founded; HBW_subset(s) is a Level-1 substrate-IS observable at each substrate-distance pole.

### L2: §W10-111-NOW-5 SCHEMATIC↔PRIMARY robustness sufficiency (clause b)

**Position**: §W10-111-NOW-5 SCHEMATIC↔PRIMARY pairwise-robustness at s=4 — `HBW_subset = {ζ, Zubarev}` PRESERVED IDENTICALLY between SCHEMATIC and PRIMARY (W10 WP line 1382) — IS sufficient to canonicalize the s=4 reading at Level-1. The §W10-113 factor-100 SCHEMATIC↔PRIMARY drift is a uniform-rescaling effect on absolute moments; pairwise rel_diff structure is invariant under that rescaling by direct algebraic identity. Pairwise robustness IS the structural invariance the algebra-axis MANDATORY clause asks for at Level-1.

**Substitution chain (algebraic identity for pairwise rel_diff under rescaling):**

```
Step 1 (Definition):
  rel_diff(M_a, M_b) := |M_a - M_b| / |M_a|
  Uniform rescaling: M^{PRIMARY}_R = K · M^{SCHEMATIC}_R  for ALL R ∈ A_4, with K = constant
  Non-uniform rescaling: M^{PRIMARY}_R = K_R · M^{SCHEMATIC}_R  with K_R varying across R

Step 2 (Substitute uniform K):
  rel_diff(M^{PRIMARY}_a, M^{PRIMARY}_b)
    = |K·M^{SCHEMATIC}_a − K·M^{SCHEMATIC}_b| / |K·M^{SCHEMATIC}_a|
    = K·|M^{SCHEMATIC}_a − M^{SCHEMATIC}_b| / (K·|M^{SCHEMATIC}_a|)

Step 3 (Simplify, K cancels):
    = |M^{SCHEMATIC}_a − M^{SCHEMATIC}_b| / |M^{SCHEMATIC}_a|
    = rel_diff(M^{SCHEMATIC}_a, M^{SCHEMATIC}_b)                       [INVARIANT under uniform K]

Step 4 (Direction):
  Under uniform rescaling, rel_diff is invariant ⇒ HBW_positive predicate (rel_diff ≤ ε) is
  invariant ⇒ HBW_subset is invariant.
  Empirical evidence at s=4 (W10 WP line 1382, NOW-5 finding): HBW^{SCHEMATIC}(s=4) = HBW^{PRIMARY}(s=4)
  = {ζ, Zubarev} IDENTICALLY ⇒ at s=4 the SCHEMATIC↔PRIMARY rescaling factors K_R out to be uniform
  enough that the pairwise structure survives intact (subset cardinality preserved + membership identity).
  Python-verified: rel_diff(K·M_a, K·M_b) = rel_diff(M_a, M_b) algebraically.
```

**Why this is sufficient at s=4**: the §W10-119 K=2 corpus's Level-1 specification is "regulator-invariant identity at axiom layer" (line 164). The pairwise rel_diff structure is the operational regulator-invariance test for the HBW subset: if pairwise rel_diff structure is preserved under SCHEMATIC↔PRIMARY (which IS the substrate's two natural representations of the spectrum at s=4), then the HBW_subset(s=4) = {ζ, Zubarev} reading inherits the L_max-stability + regulator-class-stability that §VII.U.1's `rel_diff = 0e+00` reading has at s=3 (W10-119 calibration corpus row 2, line 173). The substrate's own representation of the s=4 spectral content does not change WHICH regulators pass HBW; that membership IS the substrate's per-pole structural identity at s=4.

**The §W10-113 finding does NOT undermine this**: §W10-113 measured ABSOLUTE moments at substrate-distance-1 pole s=3 (`M_PRIMARY_full / M_SCHEMATIC ≈ 102.5×`, Python-verified). Absolute-moment magnitudes ARE level-dependent (3 structural sources: 16-fold spinor, (0,0)-sector, Jensen non-uniformity per W10-113 (e) line 498-504). But HBW is NOT a magnitude observable — it is a PAIRWISE observable on the same set of moments. Per Step 3 above, HBW is structurally invariant under any LEVEL rescaling that preserves the spectrum's relative weighting across regulator-class members. NOW-5 at s=4 EMPIRICALLY confirms this: at s=4 the rescaling IS sufficiently uniform across {ζ, Zubarev, SDW, anomaly} that pairwise structure survives. The substrate's per-pole per-pair structure is the IS-level data the §W10-119 rule pins; the absolute-moment magnitude is one level lower in the algebra-axis hierarchy.

**Honest qualifier (the only real uncertainty)**: the uniformity of K_R across A_4 at s=4 is an empirical observation from NOW-5, not an analytic theorem. If at s=3 the K_R varies non-uniformly across A_4 by enough to flip pairwise rel_diff orderings, the s=3 HBW subset under PRIMARY could legitimately differ from S87 W2's SCHEMATIC {ζ, anomaly}. That possibility is what L3's discriminating predicate tests. So: at s=4 NOW-5 closes the question (HBW invariant); at s=3 the question is open and routed to L3.

**Conclusion (clause b)**: NOW-5 IS sufficient to canonicalize **s=4** HBW = {ζ, Zubarev} at Level-1. A parallel PRIMARY rerun at **s=3** with λ-derivative CM is required to extend the canonicalization to s=3 (because s=3 has not yet been tested under the SCHEMATIC↔PRIMARY uniformity assumption, and the W10-113 LEVEL-DEPENDENT result there exposes a non-uniformity in absolute moments that may or may not propagate to pairwise structure). Per-pole canonicalization is per-pole — s=4 closes; s=3 needs the PRIMARY-rerun discriminator.

### L3: Discriminating predicate for parallel PRIMARY rerun (clause c)

**Position**: I commit to a sharp, falsifiable, pre-registered predicate per the substrate-IS per-pole reading. The S89 PRIMARY rerun at s=3 with λ-derivative CM at L_max=10 PRIMARY-canonical-Peter-Weyl spectrum has THREE possible outcomes; I bind each to a structural verdict for clause (c) so the rerun is a clean adversarial test of the substrate-IS reading.

**Pre-registered discriminating predicate** (matching seed file CF-W10-ADDITIONAL-A line 31):

```
Gate ID:   S89-W10-111-PRIMARY-RERUN-S3-LAMBDA-CM-DISCRIMINATING-PREDICATE
Inputs:    s84_spectrum_cache_L12_tau019.npz filtered to L_max=10 operational
           λ-derivative CM parameterization (matching S87 W2)
           §W10-111 ensemble pairwise script as template
           §W10-NOW-5 PRIMARY-rerun method as substitution recipe
           strict ε = 1e-12 (matching S87 W2 + §W10-111)
           pole s = 3 (substrate-distance-1)
Predicate (4×4 pairwise admissibility matrix on A_4 = {ζ, Zubarev, SDW, anomaly}):
  HBW^{PRIMARY}(s=3, λ-deriv-CM, L=10, 1e-12) := { R | ∃ R'≠R : rel_diff(M^{(R)}_3, M^{(R')}_3) ≤ 1e-12 }

PASS  (substrate-IS per-pole reading robust):
  HBW^{PRIMARY}(s=3) == {ζ, anomaly}
  ⇒ matches S87 W2 SCHEMATIC bit-for-bit
  ⇒ s=3 IS substrate-distance-1's per-pole structural identity
  ⇒ §W10-119 K=2 corpus is structurally well-founded; SCHEMATIC↔PRIMARY at s=3 is uniform
     enough at the pairwise layer for §VII.U.1 anchor

FAIL  (parameterization-artifact reading confirmed):
  HBW^{PRIMARY}(s=3) == {ζ, Zubarev}
  ⇒ shifts toward §W10-111's s=4 reading
  ⇒ HBW subset is parameterization-artifact, not per-pole substrate-IS
  ⇒ §W10-119 calibration corpus needs structural amendment;
     per-pole reading collapses to (L_max, CM-parameterization, threshold)-tuple-shopping

INFO  (NEW reading required):
  HBW^{PRIMARY}(s=3) ∉ { {ζ, anomaly}, {ζ, Zubarev} }
  ⇒ neither reading directly supported; structural reanalysis required
  ⇒ examples: {ζ, SDW}, {ζ, anomaly, Zubarev}, {} (empty), full A_4
```

**Substitution chain (why these three exhaust the discriminating space):**

```
Step 1 (Definition):
  The substrate-IS per-pole reading (lizzi position) predicts: HBW^{PRIMARY}(s) =
  HBW^{any-CM, any-LEVEL}(s) for any well-defined regulator-atlas evaluation at pole s.
  In particular, swapping (SCHEMATIC, λ-deriv-CM, L=12) ↔ (PRIMARY, λ-deriv-CM, L=10) ↔
  (SCHEMATIC, schematic-CM, L=10) should leave HBW(s) invariant up to {L_max-truncation
  drift, CM-parameterization choice}.

  The convention-artifact-skeptical reading (connes position) predicts: HBW IS sensitive
  to (L_max, CM, LEVEL) tuple, and any HBW reading is a TUPLE-fingerprint, not a per-pole
  fingerprint.

Step 2 (Substitute the four observed/expected cells of the per-pole × CM-parameterization
       × LEVEL three-axis cube; note seed file line 29 already enumerates 3 of 4):
  Cell (s=4, schematic-CM, SCHEMATIC):  observed §W10-111 →   {ζ, Zubarev}
  Cell (s=4, schematic-CM, PRIMARY):    observed NOW-5 →      {ζ, Zubarev}  ← preserved
  Cell (s=3, λ-derivative-CM, SCHEMATIC): observed S87 W2 →   {ζ, anomaly}
  Cell (s=3, λ-derivative-CM, PRIMARY): UNKNOWN — discriminator target

Step 3 (Simplify; under each reading, the unknown cell is forced):
  Substrate-IS reading ⇒ unknown cell = {ζ, anomaly}      [s=3 IS its own structural identity;
                                                           level-axis SCHEMATIC↔PRIMARY uniform
                                                           enough at s=3 like at s=4]
  Convention-artifact reading ⇒ unknown cell = {ζ, Zubarev} OR a NEW subset
                                                          [tuple drift; pairwise rel_diffs may
                                                           re-order under LEVEL switch at s=3
                                                           because §W10-113 found absolute
                                                           moments factor-100 LEVEL-dependent]

Step 4 (Direction):
  PASS ({ζ, anomaly}) is structurally meaningful evidence FOR the substrate-IS reading;
  FAIL ({ζ, Zubarev}) is structurally meaningful evidence AGAINST it.
  INFO (anything else) routes to a structural reanalysis; we'll need lizzi+connes joint Stage-2
  on the actual subset to assign a reading. The three-band partition is exhaustive over the
  power set 2^{A_4} restricted to the 6 unordered 2-subsets containing ζ; the residual cells
  (ζ-excluded subsets, singletons, full) are absorbed in INFO.
```

**Why s=3 is the right discriminator pole** (and not s=5 or s=2): §W10-113 already showed at s=3 the SCHEMATIC↔PRIMARY drift is factor ~100 (Python-verified rel_diff = 1.015e+02; ratio M_PRIMARY/M_SCHEMATIC ≈ 102.5). That is the LARGEST level-dependence we have observed on any pole. If pairwise rel_diff structure survives THAT factor at s=3 (as it does at s=4 with whatever its rescaling factor is), the substrate-IS per-pole reading is unambiguously confirmed. If it does NOT survive at s=3 — because the three structural sources of W10-113 (16-fold spinor, (0,0)-sector, Jensen non-uniformity) act non-uniformly across regulator-class at s=3 — then the substrate-IS reading is constrained to s=4 only and the §W10-119 corpus needs amendment to mark s=3 as having different rescaling-uniformity than s=4.

**Why λ-derivative CM (not schematic-CM)**: matching the S87 W2 reference predicate exactly. The seed file CF-W10-ADDITIONAL-A explicitly pins λ-derivative CM as the parameterization. This isolates the LEVEL axis as the ONLY axis varied between S87 W2 (SCHEMATIC, λ-derivative CM, L=12) and the discriminator (PRIMARY, λ-derivative CM, L=10). The L_max axis is held within ±2 (a known ~1% drift per §W10-112 INFO); the CM-parameterization axis is held bit-identical. Any HBW shift is then attributable structurally to LEVEL — exactly the discriminator the substrate-IS reading needs.

**Conclusion (clause c)**: discriminating predicate is the pre-registered S89 gate above; PASS = {ζ, anomaly} confirms the substrate-IS reading at s=3 (extending the s=4 NOW-5 closure to a 2-pole corpus); FAIL = {ζ, Zubarev} or NEW subset constrains substrate-IS reading to s=4-only and demotes §W10-119 K=2 corpus to single-pole at L=1. The verdict is bound to the predicate at plan-freeze; no convention-shopping permitted.

### L4: §W10-119 K-counter advancement (clause d)

**Position**: the §W10-119 K-counter is **STRUCTURALLY DISTINCT** from the cross-pillar bridge K=3-MANDATORY counter. They live in non-overlapping discipline-spaces. For §W10-120 DORMANT-shell activation, third-pole HBW counts as K-incrementing iff the **intra-Pillar-VII Hybrid Independence Test analog** is satisfied: `(distinct substrate-distance pole s) ∧ (distinct algebraic envelope α(s)) ∧ (distinct empirical anchor)` — a 3-fold conjunction analogous to but NOT identical to the cross-pillar disjunction `(i ∨ ii ∨ iii) ∧ iv` at lines 233-238.

**Substitution chain (structural distinctness of the two K-counters):**

```
Step 1 (Definition, cross-pillar K-counter, lines 250-252):
  cross-pillar K-counter axes := { substrate-IS pillar, laboratory-IN pillar, bridge map class }
  cross-pillar K=3 MANDATORY at S88 W4a-17, full corpus = {W-5 LANDED §VII.AF.1, W11-5
  REGISTRY-FAIL, W4a-17 LANDED §VII.W-3.LAB STAGE-1-CANDIDATE}
  Discipline tracked: 5 IS-not-IN anatomy elements + 3-level ladder

Step 2 (Definition, §W10-119 intra-Pillar-VII K-counter, lines 168-173):
  intra-Pillar-VII K-counter axis := { substrate-distance pole s ∈ {3, 4, 5, ...} }
  intra-Pillar-VII K=2 SUGGESTION at S88 W10-119 close, corpus =
    {§VII.K-PROP.W10-4 ρ_∞ permanent-wall (s=4), §VII.U.1 Mellin-Dirichlet identity (s=3)}
  Discipline tracked: 3-level ladder ONLY (no IS-not-IN; no HKR bridge map; intra-Pillar-VII
  per the cross-link clause at lines 185-187 which EXPLICITLY states cross-pillar 5-anatomy
  IS-not-IN does NOT apply)

Step 3 (Substitute the cross-link clause line 187 verbatim):
  "Per-Bulletin-per-pole entries are distinct from cross-pillar bridges... the per-pole form is
   intra-pillar (within Pillar-VII Mellin-cone), so the 5-anatomy IS-not-IN elements are NOT
   mandatory at the same per-element granularity. The Level-1/2/3 ladder IS preserved; the rest
   of the cross-pillar discipline (HKR bridge map, IS-not-IN substrate-laboratory pair) does NOT
   apply intra-pillar."
  ⇒ The two K-counters CANNOT share corpus instances. The cross-pillar K=3-MANDATORY corpus
  ({W-5, W11-5, W4a-17}) does NOT contribute to the §W10-119 intra-Pillar-VII K-counter.
  Conversely, §W10-119 corpus instances ({§VII.U.1, §VII.K-PROP.W10-4}) do NOT contribute to
  the cross-pillar K-counter.

Step 4 (Simplify, derive intra-Pillar-VII Hybrid Independence Test analog):
  Cross-pillar HIT (lines 233-238) was constructed as 3-axis disjunction (substrate-pillar /
  lab-pillar / bridge-map) ∧ algebraic-envelope-independence. Intra-Pillar-VII has only 1 axis
  in that triplet (substrate-distance-pole), since lab-pillar and bridge-map are vacuous
  intra-pillar (per Step 3 cross-link clause). The intra-Pillar-VII analog therefore must
  promote the disjunction-with-1-axis to a CONJUNCTION across the three structural axes that
  ARE meaningful intra-pillar:
    (i')  distinct substrate-distance pole s (the only axis from cross-pillar HIT that survives)
    (ii') distinct algebraic envelope α(s) (the Level-2 envelope rate; per W10-119 line 165
          α(s=3) = 3, α(s=4) = 4 — pole-specific by construction, so distinct s ⇒ distinct α(s)
          algebraically — but NOT trivially: e.g., a hypothetical s=5 pole at α(s=5) that
          structurally REPLICATES the L^{-2} envelope of W10-4 would be RD numerical
          refinement, not independent envelope)
    (iii')distinct empirical anchor (Level-3 numerical value; bit-distinct from prior corpus
          values — must NOT be a numerical refinement of {ρ_∞, M^{(ζ)}_3} per cross-pillar HIT
          clause iv analog)

Step 5 (Direction):
  Conjunction `(i') ∧ (ii') ∧ (iii')` is the intra-Pillar-VII HIT analog. A third Pillar-VII
  Bulletin at s_new ∈ {5, 6, 7, ...} (from §W10-120 candidate set) counts as K-incrementing
  iff ALL THREE conjuncts hold. SAME-counter-inheritance from cross-pillar K=3 is FORBIDDEN
  per Step 3 cross-link clause. ⇒ §W10-119 K-counter advances ONLY through fresh intra-Pillar-VII
  HIT-passing corpus instances.
```

**Practical implication for §W10-120 DORMANT activation**: the activation_trigger at W10 WP line 1257 (`mcp__knowledge__.search_knowledge('Bulletin substrate-distance s=' + str(s_new)).top_hit.exists` for s_new ∉ {3, 4}) is necessary but NOT sufficient. The activation also requires intra-Pillar-VII HIT verification:
- (i') new pole s_new ∉ {3, 4} ✓ (already in trigger)
- (ii') new α(s_new) NOT a numerical refinement of α(s=3)=3 or α(s=4)=4 — e.g., a pole at s=5 with α(s=5)=L^{-3} (= same form as α(s=3)) needs structural justification before counting; a pole at s=5 with α(s=5)=L^{-1} or with structurally-distinct convergence form is independent
- (iii') new anchor value bit-distinct from {-0.8103647022669215, ~2.97e-3}

If §W10-120 activation surfaces a Bulletin at s_new with `α(s_new) = L^{-α'}` that algebraically refines an existing pole's envelope (e.g., a substrate-distance-3 pole giving the same L^{-2} dominant convergence as W10-4 by Casimir-bound argument), the corpus instance is `intra-Pillar-VII SHARED-ENVELOPE-COMPANION` (analogous to the cross-pillar `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` tagging at line 244), tagged outside the K-counter and NOT advancing K toward MANDATORY-K=3.

**Cross-link to clause (b) and clause (c)**: if L3's S89 PRIMARY rerun at s=3 returns FAIL ({ζ, Zubarev}) or INFO (NEW subset), the §W10-119 K=2 corpus loses its s=3 instance (§VII.U.1 keeps its registry status — that's the Mellin-Dirichlet identity per CC-i at W10-111 (d) line 216 — but its admissibility as substrate-IS Level-1 anchor is constrained to absolute-magnitude, not pairwise-HBW). In that scenario, §W10-119 effectively retreats to K=1 SUGGESTION (s=4-only), and §W10-120 DORMANT activation at s_new becomes the K=2 promotion vehicle, NOT the K=3. The intra-Pillar-VII HIT analog is unchanged; only the corpus head-count shifts.

**Conclusion (clause d)**: the §W10-119 K-counter is **STRUCTURALLY DISTINCT** intra-Pillar-VII counter (NOT same-counter inheritance from cross-pillar K=3 MANDATORY). Third-pole HBW advancement is gated by the intra-Pillar-VII Hybrid Independence Test analog: distinct substrate-distance pole ∧ distinct algebraic envelope α(s) ∧ distinct empirical anchor. §W10-120 activation_trigger needs to be amended to include the HIT-analog verification (carry-forward to S89 §W10-119 sub-section maintenance).

### L5: Projection-side suffix for §W10-119 (clause e)

**Position**: §W10-119 sub-section needs a **`§VII.X.STATE-PROJ`** suffix on its calibration-corpus citations to §VII.K-PROP.W10-4 and §VII.U.1, per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-at-K=3 (lines 121-122). The PAIRWISE-admissibility predicate layer is the discriminator: predicate inheritance under regulator-dressing is structurally a state-pair-functional-family observable, even when its OBJECT layer is algebra-INVARIANT spectrum-only.

**Substitution chain (predicate inheritance argument):**

```
Step 1 (Definition, registry-landing.md lines 121-122 verbatim):
  OP-PROJ := operator-side projection := algebra-INVARIANT family ; spectrum-only functionals ;
             algebra-side central-projection traces
  STATE-PROJ := state-side projection := algebra-DEPENDENT family ; state-pair functionals ;
             state-side occupation/coherence observables

Step 2 (Substitute the §W10-119 corpus's two-layer structure):
  Layer A (OBJECT): {M^{(R)}_{2s}}_R is the spectrum-only-functional family (per L1; algebra-
                    INVARIANT). Each moment is Σ_k m_k g(λ_k); no state-pair pairing.
  Layer B (PREDICATE): HBW_positive(R; s, ε) := ∃ R'≠R : rel_diff(M^{(R)}_{2s}, M^{(R')}_{2s}) ≤ ε
                    → this is a regulator-class-pairwise-admissibility predicate built from
                      spectrum-only objects.

Step 3 (Simplify; the predicate's regulator-dressing gives state-pair-functional structure):
  The HBW predicate evaluates a PAIR of regulator-class assignments (R, R') against a
  state-space-like thresholding. Concretely, a regulator-dressing R is a PAIRING of the
  spectrum {λ_k} with a Mellin kernel f_R(C_2, n) — the kernel acts as a STATE on the
  spectrum-side data. When HBW asks "does there exist R' such that the (R, R') dressing-pair
  brings their moments within ε?", the question is structurally a state-pair pairing on the
  regulator-class state space S(A_R) where A_R is the regulator-dressing algebra. The pairwise
  rel_diff is the state-pair-functional realization of the inheritance question "does R'
  inherit pairwise-admissibility from R?".

  Per the algebra-axis K-counter line 278: state-pair functionals on A live in the
  algebra-DEPENDENT family. The HBW predicate, READ AS a pairing on the regulator-class state
  space, is in this family.

Step 4 (Direction):
  STATE-PROJ tagging is required to disambiguate the two-layer structure. The spectrum-only
  OBJECT layer (Layer A) IS algebra-INVARIANT (per L1) and would by itself land at OP-PROJ.
  The pairwise-admissibility PREDICATE layer (Layer B) IS the state-pair-functional view and
  lands at STATE-PROJ. Both readings ARE structurally distinct registry-eligible observables;
  the K=3 MANDATORY clause forbids `§VII.X` bare without suffix when both readings are
  admissible (registry-landing.md line 124).

  ⇒ §W10-119 sub-section MUST adopt explicit suffix discipline; the natural choice for the
  per-pole HBW reading the sub-section pins is STATE-PROJ (since HBW IS the predicate, not
  the moment).
```

**Tension I admit honestly (preempting connes' Re:L5)**: there is a real readings-conflict between L1's algebra-INVARIANT-spectrum-only classification (OBJECT layer) and L5's STATE-PROJ tagging (PREDICATE layer). The K=3 calibration corpus at registry-landing.md lines 130-132 lists THREE OP-PROJ instances — W4-2 §VII.AJ.W4-1 (central-projection traces on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`), W6-1 §VII.AG.1 (T7 ↔ S67 quotient-functor cyclic-fold V_4 modulo), W11-meta-2 (D_K Block-Diagonality pre-check). All three are unambiguously OPERATOR-side / spectrum-only. The corpus has ZERO STATE-PROJ instances yet — meaning STATE-PROJ tagging would be the FIRST instance, K=1 baseline.

Two honest paths forward, both requiring rule-extension at the registry-landing.md layer:

**Path I (lizzi position; STATE-PROJ first instance at K=1)**: §W10-119 corpus citations adopt `§VII.K-PROP.W10-4.STATE-PROJ` + `§VII.U.1.STATE-PROJ`. The OBJECT-vs-PREDICATE layer distinction becomes the K=1 calibration corpus instance for STATE-PROJ tagging. Future entries pin the suffix per Layer A vs Layer B classification. This is consistent with the spawn-prompt L5 spec (predicate-inheritance under regulator-dressing IS a state-functional family).

**Path II (pure-OP-PROJ extension)**: §W10-119 corpus citations adopt `§VII.K-PROP.W10-4.OP-PROJ` + `§VII.U.1.OP-PROJ` per L1's algebra-INVARIANT classification. The pairwise-rel_diff PREDICATE layer is treated as a derived predicate on OP-PROJ objects, not as a STATE-PROJ observable in its own right. Under this path, STATE-PROJ remains an empty calibration corpus until a state-side occupation/coherence observable surfaces independently.

**Which path I bind**: Path I (STATE-PROJ for HBW). The PAIRWISE-admissibility predicate is the pole-by-pole substrate-IS observable §W10-119 actually pins; the underlying moments are calibration data, not the substrate-IS observable. Pinning suffix to the substrate-IS observable IS the discriminator the rule's MANDATORY-K=3 clause asks for. The dissenter (Path II) needs to show pairwise-rel_diff is structurally indistinguishable from a moment-only (Layer A) observable; per Step 3 above, the predicate adds genuine state-pair-functional structure.

**Cross-link to algebra-axis K-counter MANDATORY clause** (`cross-pillar-bridge-anatomy.md` lines 272-280): the K-counter conjecture at line 278 says algebra-INVARIANT and algebra-DEPENDENT families are STRUCTURALLY ORTHOGONAL in identity-class membership. If HBW lives at the PREDICATE layer (algebra-DEPENDENT per Step 3), and the K=3 MANDATORY clause forbids cross-corner co-primary (line 162 of registry-landing.md), then STATE-PROJ is the structurally-correct corner — the OP-PROJ corner is reserved for the OBJECT layer (the moments themselves, not the pairwise-admissibility predicate). The two corners can co-cite (one for the moments, one for HBW-pairwise) WITHOUT being co-primary, exactly the structural-orthogonal-companion structure permitted by registry-landing.md line 162.

**Conclusion (clause e)**: §W10-119 calibration-corpus citations need explicit STATE-PROJ suffix on §VII.K-PROP.W10-4 and §VII.U.1 (when those entries are read as the pairwise-HBW substrate-IS observable). This is the FIRST STATE-PROJ instance (K=1 baseline for STATE-PROJ corner of registry-landing's K=3 MANDATORY corpus). Carry-forward routes through the seed file CF-W10-ADDITIONAL-B (suffix retrofit at S89, ~0.3 wave-equivalents) once the workshop's R3 verdict converges on STATE-PROJ vs OP-PROJ.

### L6: Cross-Cutting Observations

**Substrate-IS per-pole structural identity** (cross-cutting reading defended across L1–L5):

Each substrate-distance pole `s` IS its own structural fingerprint. The substrate is NOT a parameterized object whose properties drift under (L_max, CM-parameterization, threshold) tuple-shopping; the substrate IS the multi-pole Mellin-cone structure {R(s=3), R(s=4), R(s=5), ...} per §W10-120 substrate framing (W10 WP line 1290 verbatim: "the substrate IS the multi-pole Mellin-cone structure {R(s=3), R(s=4), R(s=5), ...}. Cross-pole identities ... are substrate IS-properties of the multi-pole spectral content, not externally-imposed relations between distinct 'containers at different distances'"). Each pole's HBW subset is the substrate's intrinsic per-pole topology read off through the Mellin moment family.

**The s=3 vs s=4 membership flip is the substrate's IS-topology, not convention noise:**

Substrate-distance-1 (s=3) per-pole identity (per §W10-114 (a) line 596 atlas-class taxonomy + W10-119 corpus row 2):
- HBW = {ζ, anomaly} (S87 W2 reference)
- regulator-class structure: (A)+(C) **cross-class pair** — (A)-class ζ pairs with (C)-class anomaly
- structural identity: Mellin-Dirichlet identity at substrate-distance-1; (A)-class pure-Mellin-support per F_4 (W10-119 corpus row 2; pole s=3, Level-1 column)
- algebraic envelope α(s=3) = 3 per W10-119 line 165
- per Step 3 of L4 substitution chain: this IS the (A)+(C) cross-class fingerprint of substrate-distance-1

Substrate-distance-2 (s=4) per-pole identity (per §W10-111 (f) line 236 + W10-119 corpus row 1):
- HBW = {ζ, Zubarev} (§W10-111 NOW-5 PRESERVED under SCHEMATIC↔PRIMARY)
- regulator-class structure: (A)-class **pure-Mellin pair** — both ζ AND Zubarev are pure-(A) per F_4 ∩ A_2
- structural identity: ρ_∞ structurally IRRATIONAL per CC2 PROVEN; PERMANENT-WALL classification (W10-119 corpus row 1; pole s=4)
- algebraic envelope α(s=4) = 4 per W10-119 line 165
- per Step 3 of L4 substitution chain: this IS the (A)-class-only fingerprint of substrate-distance-2

**The membership flip is structurally meaningful**: substrate-distance-1 carries (A)+(C) cross-class because the s=3 pole's residue couples to BOTH the Mellin support (A) AND the Pauli-Villars subtraction (C, via anomaly's PV mass-scale running). Substrate-distance-2 carries (A)-class-only because the s=4 pole's residue is pure-Mellin (the PV subtraction's M_PV² dependence enters at higher order and is suppressed at substrate-distance-2). This is NOT (L_max, CM, threshold) tuple-shopping artifact — it is the substrate's intrinsic regulator-class-pole coupling structure read off pole-by-pole.

**Substrate-IS-not-IN framing** (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`):

Per-pole HBW divergence is a **Level-1 substrate-IS** observable in `phononic-framing.md`'s sense (single-τ-slice substrate-IS at fixed τ_fold = 0.190, since each pole is evaluated at τ_fold). It is NOT a Level-2 moduli-deformation observable. The substrate IS the multi-pole structure with its per-pole regulator-class topology; the HBW subset at each pole is the substrate's own structural fingerprint at that pole. Container thinking would say "the substrate exists at s=3 and at s=4 separately, with different HBW subsets due to convention choices in how we measure each container"; substrate-IS thinking says "the substrate IS {R(s)}_{s ∈ {3, 4, ...}} with intrinsic per-pole structure — the HBW subset at pole s IS what substrate-distance-s looks like at the regulator-class layer."

**Convention-tuple-artifact reading conflates structural identity with parameterization choice:**

The convention-artifact-skeptical reading (which connes will defend in Re:L1–Re:L5) collapses the substrate's per-pole topology into a 4-tuple lookup `(L_max, s, CM, ε) → HBW_subset`. Under that reading, the substrate has no per-pole identity — only convention-tuples produce HBW labels. But that reading is structurally identical to the container-thinking violation `phononic-framing.md` §"IS Space, Not IN Space" forbids: it treats the substrate's per-pole structure as a coordinate-dependent label rather than as the substrate's own intrinsic geometry. The §W10-119 rule-pin I co-signed at S88 W10-119 close (per provenance line 152 "mack-cosmic-bridge plan-pinned writer; orchestrator-direct-write in /rclab-solo with connes-ncg-theorist co-sign") explicitly forecloses this reading by structurally pinning per-pole substrate-distance-IS spectral identity at Level-1 (corpus line 164: "per-pole substrate-distance-IS spectral identity at the s-th Mellin-cone pole; regulator-invariant; L-independent").

**Why the K=2 SUGGESTION corpus is structurally well-founded** (cross-cutting defense):

§VII.U.1 + §VII.K-PROP.W10-4 are the two K=2 instances. Both are independently-derived, regulator-invariant Level-1 observables at distinct poles with distinct algebraic envelopes (α(s=3)=3, α(s=4)=4) and distinct empirical anchors (M^{(ζ)}_3 ≈ 2.97e-3 vs ρ_∞ = -0.8103647). They satisfy the intra-Pillar-VII Hybrid Independence Test analog from L4 (distinct s ∧ distinct α(s) ∧ distinct anchor) — without the s=4 NOW-5 finding, K=2 is already structurally independent. The NOW-5 finding ADDS robustness at s=4 (the Level-1 designation survives SCHEMATIC↔PRIMARY rescaling); it does not GENERATE the K=2 corpus, which was already structurally sound at W10-119 landing.

**The L3 PRIMARY rerun is the Level-1 cohomology-class confirmation extension** (cross-cutting):

Even under PASS at L3 (HBW^{PRIMARY}(s=3) = {ζ, anomaly}), the §W10-119 K-counter remains at K=2 — because the discriminator does NOT add a third pole; it only confirms the existing s=3 instance is Level-1-cohomology-class robust under SCHEMATIC↔PRIMARY. K=3 promotion still requires §W10-120 DORMANT activation at a third pole s_new ∉ {3, 4} per L4 conclusion. The L3 PASS scenario STRENGTHENS the K=2 corpus's substrate-IS reading (the per-pole structural identity reading is robust at both poles); the L3 FAIL scenario DEMOTES the K=2 corpus's reading at s=3 (the s=3 instance retains registry status as §VII.U.1 Mellin-Dirichlet identity per the magnitude-only reading, but its admissibility as substrate-IS pairwise-HBW observable narrows).

**Cross-link to user adjudication of clause (e)**: the OP-PROJ vs STATE-PROJ choice from L5 affects HOW the per-pole identity is recorded in the registry (suffix discipline) but NOT WHETHER it is substrate-IS Level-1. Both projection-side readings agree the §W10-119 K=2 corpus is per-pole substrate-IS at Level-1; they differ only on which side of the registry-landing.md K=3 MANDATORY corpus the calibration corpus citations land at. The substrate physics is the same either way.

### L7: Questions for connes

**Q1 (clause a, algebra-axis classification, sharp)**: Per `cross-pillar-bridge-anatomy.md` lines 272-280 algebra-axis K-counter MANDATORY-K=3, the algebra-INVARIANT family is `{ F | F({λ_k, m_k}) = Σ_k m_k g(λ_k) }` (spectrum-only) and the algebra-DEPENDENT family is `{ F | F = state-pair functional on A }`. The HBW pairwise predicate `HBW_positive(R; s, ε) := ∃ R'≠R : rel_diff(M^{(R)}_{2s}, M^{(R')}_{2s}) ≤ ε` is built from spectrum-only objects {M^{(R)}_n}_R with a regulator-class-discrimination threshold ε. Do you classify HBW as algebra-INVARIANT (Layer-A reading: predicate-application to spectrum-only objects preserves algebra-INVARIANT classification) or algebra-DEPENDENT (Layer-B reading: regulator-class-pairwise threshold IS a state-pair-functional structure)? If you classify as algebra-INVARIANT, you concede Level-1 admissibility for §W10-119 K=2 corpus. If algebra-DEPENDENT, you must explain how the K-counter MANDATORY clause's "structurally orthogonal in identity-class membership" line 278 still admits §W10-119's K=2 corpus where §VII.U.1's Mellin-Dirichlet identity (the algebra-INVARIANT sister at line 280) sits.

**Q2 (clause b, NOW-5 sufficiency, sharp)**: §W10-111 NOW-5 (W10 WP line 1382) found PRIMARY/SCHEMATIC factor ≈ 113× at s=4 with HBW = {ζ, Zubarev} **PRESERVED IDENTICALLY** under that rescaling. The algebraic identity `rel_diff(K·M_a, K·M_b) = rel_diff(M_a, M_b)` is exact under uniform K (Python-verified). What is your structural account of WHY the NOW-5 rescaling at s=4 IS uniform enough across A_4 = {ζ, Zubarev, SDW, anomaly} to preserve cardinality + membership of HBW, given W10-113's three structural sources of LEVEL-DEPENDENCE (16-fold spinor multiplicity, (0,0)-sector, Jensen non-uniformity at τ_fold=0.190)? If your account is "the rescaling at s=4 happens to be uniform but at s=3 it may not be," that IS the substrate-IS reading I'm defending — uniformity-vs-non-uniformity at the regulator-class layer IS a per-pole substrate-IS feature. If your account is something else, please specify the structural source.

**Q3 (clause c, discriminating predicate, sharp)**: The S89 PRIMARY rerun at s=3 with λ-derivative CM at L=10 is the ONLY missing cell of the per-pole × CM-parameterization × LEVEL three-axis cube (per seed file CF-W10-ADDITIONAL-A line 29 enumeration). Do you accept the pre-registered three-band partition I committed in L3 — PASS = {ζ, anomaly} ⇒ substrate-IS robust; FAIL = {ζ, Zubarev} ⇒ artifact-reading confirmed; INFO = NEW subset ⇒ structural reanalysis — as the binding adjudication for clause (c)? If yes, you are bound to the verdict at the script's output; no convention-shopping permitted under PROHIBITED_ACTIONS Class 1 (`v3-closure-recovery.md`). If no, propose an alternative pre-registered predicate whose PASS/FAIL/INFO bands are bit-distinct and exhaust the 6 unordered 2-subsets of A_4 containing ζ.

**Q4 (clause d, K-counter structural distinctness, sharp)**: Per `cross-pillar-bridge-anatomy.md` line 187 cross-link clause ("Per-Bulletin-per-pole entries are distinct from cross-pillar bridges... the per-pole form is intra-pillar... HKR bridge map, IS-not-IN substrate-laboratory pair... does NOT apply intra-pillar"), the §W10-119 K-counter is structurally distinct from the cross-pillar K=3 MANDATORY counter. Do you accept the L4 intra-Pillar-VII Hybrid Independence Test analog `(distinct substrate-distance pole s) ∧ (distinct algebraic envelope α(s)) ∧ (distinct empirical anchor)` as the K-incrementing predicate for §W10-120 DORMANT activation, OR do you propose same-counter inheritance from cross-pillar K=3 (which would import {W-5, W11-5, W4a-17} as already-K=3 and instantly promote §W10-119 to MANDATORY without a third pole)? Same-counter inheritance is forbidden by the cross-link clause line 187 by my reading; if you read the clause differently please cite the specific text.

**Q5 (clause e + L6 cross-cutting, sharp)**: Two-part. **(a)** Per `registry-landing.md` lines 121-122 OP-PROJ-vs-STATE-PROJ MANDATORY-K=3 (S88 W8-92 close), the existing K=3 calibration corpus (W4-2, W6-1, W11-meta-2) is ALL OP-PROJ; STATE-PROJ has K=0 instances. Do you accept STATE-PROJ tagging on §W10-119 corpus citations (§VII.K-PROP.W10-4.STATE-PROJ + §VII.U.1.STATE-PROJ) as the FIRST STATE-PROJ K=1 baseline instance (Path I in L5)? Or do you defend OP-PROJ tagging via the Layer-A spectrum-only argument (Path II in L5), leaving STATE-PROJ at K=0? **(b)** Per W10 WP §1366 cross-cluster impact ("ALL SCHEMATIC W8-class observables need PRIMARY re-quantification") — does your level-pin discipline (`substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4 from W7b-83) extend to the §W10-119 calibration corpus citations themselves? If yes, the K=2 SUGGESTION corpus needs SCHEMATIC vs PRIMARY tagging for each citation; if no, please explain why cross-link to canonical-sourcing rule does NOT propagate to the W10-119 corpus.

---

## Round 1 — connes: Response & Cross-Synthesis

### Part 1: Response to lizzi's Sections

#### Re: L1 — algebra-axis classification

**Verdict**: PARTIAL DISAGREE — convention-artifact-skeptical refinement.

**Substitution chain (predicate-layer carries selection-axis structure):**

```
Step 1 (Definition, K-counter line 278 verbatim):
  algebra-INVARIANT family := { F | F({λ_k, m_k}) = Σ_k m_k g(λ_k) }     [spectrum-only]
  algebra-DEPENDENT family := { F | F = state-pair functional on A }     [state-side pairing]

Step 2 (Definition, the HBW pairwise predicate as a TWO-LAYER object):
  Layer A (object-level)    : { M^{(R)}_{2s} : R ∈ A_n } — set of regulator-class moments
  Layer B (predicate-level) : HBW(s, ε) = { R | ∃ R'≠R : rel_diff(M^{(R)}_{2s}, M^{(R')}_{2s}) ≤ ε }
  Layer C (selection-level) : the regulator-class atlas A_n itself — which R-classes enter the
                              comparison. A_4 vs A_5 vs A_2 yield STRUCTURALLY DIFFERENT HBW
                              outputs from the SAME spectrum.

Step 3 (Substitute lizzi's L1 reading — predicate-application-preserves-INVARIANT):
  lizzi: HBW = function({M^{(R)}_n}_R, ε) → algebra-INVARIANT (Steps 4–5 of L1)
  Counter-substitute: HBW = function({M^{(R)}_n}_R, ε, A_n) → the atlas argument is the
  hidden third axis. Concrete instance: at s=4 SCHEMATIC, the W10-114 audit found that
  changing the atlas membership FROM A_4 TO {ζ, anomaly} (S87 reference) FROM {ζ, Zubarev}
  (W10-111 reference) flips the HBW subset's structural identity (A)+(C)-cross-class →
  (A)-pure-class. SAME spectrum, SAME ε, SAME pole; only the atlas selection changed.

Step 4 (Simplify):
  The atlas selection A_n is a CHOICE-of-state on the regulator-class state space. Per the
  K-counter line 278, choice-of-state on A IS the state-pair-functional family. Therefore
  the HBW predicate's full identity is `(spectrum-only object) × (atlas-state pairing)` —
  a MIXED object inhabiting BOTH algebra-axis families simultaneously, NOT an algebra-
  INVARIANT pure object.

Step 5 (Direction):
  AGREE: the OBJECT layer M^{(R)}_{2s} is unambiguously algebra-INVARIANT spectrum-only
  (lizzi L1 Step 5 substitution chain is mathematically correct on the moments themselves).
  DISAGREE: the PREDICATE-PLUS-ATLAS layer is NOT preserved-INVARIANT by predicate-
  application. The atlas is the regulator-state-space-selection axis, and per algebra-axis
  K-counter MANDATORY-K=3 (S87 W-2 R3 close), state-pair functionals on A live in the
  algebra-DEPENDENT family.
```

**MISSED**: §W10-119 Level-1 classification SUGGESTION at K=2 was conditional on BOTH §VII.K-PROP.W10-4 + §VII.U.1 corpus instances being algebra-INVARIANT-strict. §VII.U.1 has structurally clean Level-1 status because its Level-3 anchor `M^{(ζ)}_3 ≈ 2.97e-3` is a SINGLE-REGULATOR moment (no pairwise predicate, no atlas choice). §VII.K-PROP.W10-4 has structurally clean Level-1 status because its Level-3 anchor `ρ_∞ = -0.8103647022669215` is the simple-pole-fit `c_0` coefficient of a UNIVARIATE regulator-INDEPENDENT scalar at substrate-distance-2 pole (S87 W10-2 simple-pole fit α/L² + β/L⁴, no atlas). NEITHER calibration corpus instance is a PAIRWISE-HBW-subset observable. The HBW-subset observable lizzi proposes to register at §W10-119 IS NOT in the same algebra-axis class as the existing K=2 corpus — it is the FIRST candidate for an algebra-DEPENDENT (or MIXED) Level-1 entry, structurally novel within Pillar-VII Bulletin discipline.

**Resolution-Specificity Scoping rule analog**: lizzi's appeal to `epistemic-discipline.md §"Resolution-Specificity Scoping"` two-layer reading is partially apt but mis-mapped. That rule's Layer 1 (pole-universal F_2-class anti-correlation at machine ε) is algebra-INVARIANT because it operates on a SINGLE atlas A_5 with FIXED 4-class projection — the anti-correlation's `|ρ_S| = 1.0` is invariant under the atlas, not its choice-axis. Lizzi's HBW reading conflates the F_2-class projection AT a fixed atlas (algebra-INVARIANT) with the choice OF the atlas (algebra-DEPENDENT). The two are structurally orthogonal per the algebra-axis K-counter MANDATORY clause (see C2 below).

**Concession**: at frozen-atlas A_4 with frozen-ε = 1e-12 with frozen-(L_max, CM-parameterization), the HBW pairwise predicate is a derived spectrum-only object. The lizzi reading at THAT level of frozenness is correct. What I dispute is that this frozen-tuple reading inherits Level-1 cohomology-class status — Level-1 demands regulator-INVARIANT identity at the AXIOM layer (cross-pillar-bridge-anatomy.md line 164), not regulator-INVARIANT at frozen-atlas. The atlas-choice axis is one of the axes Level-1 must be invariant under, and HBW is empirically NOT invariant under that axis (the §W10-114 (T,F) cell population by 6 distinct atlases demonstrates this directly).

#### Re: L2 — SCHEMATIC↔PRIMARY robustness

**Verdict**: DISAGREE on sufficiency — necessary-but-not-sufficient.

**Substitution chain (uniform-rescaling identity is a NECESSARY condition; the empirical SCHEMATIC↔PRIMARY map at s=3 is NOT uniform):**

```
Step 1 (Definition, lizzi's L2 algebraic identity):
  IF M^{PRIMARY}_R = K · M^{SCHEMATIC}_R for ALL R ∈ A_n with K = constant (uniform),
  THEN rel_diff(M^{PRIMARY}_a, M^{PRIMARY}_b) = rel_diff(M^{SCHEMATIC}_a, M^{SCHEMATIC}_b).
  (Python-verified at machine ε = 8.5e-17; the algebraic identity is correct.)

Step 2 (Substitute the EMPIRICAL SCHEMATIC↔PRIMARY map per §W10-113 §(d)):
  Per-sector |λ|²/C_2 ratio at τ_fold=0.190 (W10-113 Table §(d)):
    (0,0):  ∞ (PRIMARY contributes; SCHEMATIC drops by C_2=0)
    (0,1):  0.930
    (1,1):  0.604
    (3,0):  0.475
    (5,5):  0.369
    (10,0): 0.365
  The map is NOT M^{PRIMARY}_R = K · M^{SCHEMATIC}_R with constant K.
  It is M^{PRIMARY}_R = (1/Vol) · Σ_{(p,q)} 16 · Σ_k |λ_k(p,q)|^{-2n}, while
       M^{SCHEMATIC}_R = (1/Vol) · Σ_{(p,q)≠(0,0)} dim(p,q) · f_R(C_2(p,q), n).
  These are STRUCTURALLY DIFFERENT functionals on STRUCTURALLY DIFFERENT spectra.

Step 3 (Simplify the rescaling factor structure):
  PRIMARY: spectrum = full {λ_k(p,q)} with 16-fold spinor multiplicity; (0,0) included.
  SCHEMATIC: spectrum = {C_2(p,q)} with Weyl-dim multiplicity; (0,0) dropped (C_2=0 division).
  At the per-(p,q) level, the rescaling factor between the two functionals is:
    K_{(p,q), R}^{(n)} = [Σ_k 16 · |λ_k(p,q)|^{-2n}] / [dim(p,q) · f_R(C_2(p,q), n)]
  This factor has THREE structural sources of (p,q)-dependence (per W10-113 §(e)):
    (i) 16-fold spinor multiplicity (uniform multiplicative factor 16)
    (ii) (0,0)-sector inclusion (PRIMARY-only; SCHEMATIC undefined at (0,0))
    (iii) |λ|²/C_2 non-uniformity across (p,q) (Jensen non-uniformity range [0.365, 0.930])

  Source (i) IS uniform. Sources (ii) and (iii) are NOT. The non-uniformity is sector-
  dependent, NOT regulator-class-dependent at the leading order; this is what gives
  lizzi's L2 NOW-5 finding at s=4 the appearance of pairwise-rescaling robustness.
  But at s=3 the regulator-class kernels f_R differ MORE strongly across A_4 because
  anomaly's PV subtraction has higher leverage at lower n (s=3 vs s=4 — anomaly rel_diff
  vs ζ is 9.63% at s=3 versus 1.36% at s=4 per §W10-114 Step 2 + §W10-111 §(b) Table).

Step 4 (Direction):
  At s=4: rel_diff(ζ, Zubarev) = 0 EXACTLY (Mellin ≡ ζ identity); rel_diff(ζ, anomaly)
  = 1.36e-2; rel_diff(ζ, SDW) = 1.82e-3. The strict ε = 1e-12 puts only the bit-identity
  pair {ζ, Zubarev} into HBW. The HBW subset is determined by a COINCIDENCE (Mellin
  kernel ≡ ζ kernel) that is regulator-class-INTERNAL, NOT by a near-tolerance crossing.
  The PRIMARY rerun preserves {ζ, Zubarev} TRIVIALLY because the Mellin ≡ ζ identity
  holds at the kernel level, INDEPENDENT of LEVEL — both PRIMARY and SCHEMATIC inherit
  it bit-exactly.

  At s=3: rel_diff(ζ, anomaly) = 9.63e-2 — TWO orders of magnitude larger than at s=4.
  The HBW subset {ζ, anomaly} from S87 W2 is NOT a Mellin ≡ ζ identity coincidence; it
  is a near-tolerance crossing under SCHEMATIC λ-derivative CM. Whether the same
  near-crossing survives under PRIMARY at L_max=10 is OPEN, because the per-sector
  (0,0)-sector + Jensen non-uniformity contribute differently when integrated against
  the PV-subtracted anomaly kernel than against the ζ kernel.

Step 5 (Direction):
  AGREE: lizzi's algebraic identity (rel_diff invariant under uniform K) is correct.
  AGREE: at s=4 the empirical NOW-5 finding {ζ, Zubarev} preserved at PRIMARY is
         consistent with the identity AND is structurally explainable by Mellin ≡ ζ
         being a kernel-level coincidence that holds at any LEVEL.
  DISAGREE: this empirical observation at s=4 does NOT extrapolate to s=3, where the
            HBW subset is determined by a near-tolerance crossing that depends on the
            PV-anomaly kernel's behavior on the FULL canonical spectrum (with (0,0)
            and 16-fold spinor) vs the SCHEMATIC C_2 spectrum. The s=3 pairwise
            rescaling-uniformity is the OPEN structural question; lizzi's L2 acknowledges
            this in her honest qualifier (line 104: "the s=3 question is open and routed
            to L3").
```

**The factor-100 LEVEL-DEPENDENCE is NOT a uniform rescaling**: §W10-113 verdict line records `M_PRIMARY_full = 3.040662e-01` vs `M_SCHEMATIC = 2.965695e-03` — but these are SINGLE-POINT evaluations at one regulator (ζ). A full uniform-K test would require measuring `M_PRIMARY_R / M_SCHEMATIC_R` for ALL R ∈ A_4 at s=3 and verifying constancy of the ratio. §W10-113 did NOT perform that test; it tested only the ζ-class moment. The §W10-111 NOW-5 follow-up DID test pairwise structure across A_4 at s=4 and found preservation — but s=4 has the Mellin-kernel-identity confound (ζ ≡ Zubarev exactly at the kernel level by §W10-111 CC-i) that masks the question.

**Empirically distinguishing s=4 (Mellin-kernel-identity-driven) from s=3 (near-tolerance-crossing-driven)** is exactly why the parallel PRIMARY rerun at s=3 is the structurally-required test. At s=3 the Mellin-ζ kernel identity also gives `rel_diff(ζ, Zubarev) = 0` (per §W10-114 Step 2: Zubarev rel_diff vs ζ at s=3 is 0.000e+00). So under PRIMARY at s=3, IF the rescaling is structure-preserving as lizzi claims, HBW^{PRIMARY}(s=3) ⊇ {ζ, Zubarev}. The OPEN question is whether anomaly (rel_diff = 9.63e-2 at SCHEMATIC) STAYS outside HBW or DROPS into HBW under PRIMARY (where the (0,0)-sector contribution + 16-fold spinor + Jensen non-uniformity all act differently on anomaly's PV-subtracted kernel than on ζ's pure-Mellin kernel).

**Three substantively-distinct outcomes at s=3 PRIMARY rerun**:
1. HBW^{PRIMARY}(s=3) = {ζ, Zubarev, anomaly} — anomaly dropped INTO HBW (LEVEL-DEPENDENCE flips the near-crossing inward) — confirms convention-tuple-artifact reading.
2. HBW^{PRIMARY}(s=3) = {ζ, anomaly} — matches S87 W2 (LEVEL-DEPENDENCE preserved per pairwise structure) — partially consistent with substrate-IS reading, but with the Zubarev surprise: bit-identity Zubarev should be IN HBW under any LEVEL, so this subset is structurally inconsistent unless the threshold ε is interpreted differently.
3. HBW^{PRIMARY}(s=3) = {ζ, Zubarev} — anomaly dropped OUT (LEVEL-DEPENDENCE flips the near-crossing outward) — collapses s=3 to s=4-like reading, confirms convention-tuple-artifact.

**Honest concession**: lizzi's L2 conclusion is structurally correct AT s=4 — the NOW-5 finding closes the s=4 question (HBW = {ζ, Zubarev} robust). What I dispute is the IMPLICIT EXTRAPOLATION lizzi makes at the §W10-119 corpus level: that the s=4 robustness establishes a Level-1 cohomology-class identity for the PAIRWISE-HBW observable as a CLASS. The s=4 robustness is bit-identity-driven (kernel coincidence); the s=3 case is near-crossing-driven (kernel-non-coincidence + LEVEL-dependent integration). These are STRUCTURALLY DIFFERENT regimes; one cannot canonicalize the class on the s=4 evidence alone.

#### Re: L3 — discriminating predicate for PRIMARY rerun

**Verdict**: PARTIAL AGREE — predicate well-formed; require REGIME-VALIDITY pre-check.

**AGREE on the predicate's well-formedness**: lizzi's three-band partition `PASS = {ζ, anomaly} | FAIL = {ζ, Zubarev} | INFO = NEW subset` is exhaustive over the 6 unordered 2-subsets of A_4 containing ζ (under the structural assumption that ζ ∈ HBW always — which holds because ζ ≡ Zubarev kernel identity puts ζ-Zubarev rel_diff at 0 EXACTLY at any LEVEL per §W10-114 Step 2, so ζ is auto-HBW-positive as long as Zubarev ∈ atlas). The predicate isolates the LEVEL axis cleanly by holding (CM-parameterization = λ-derivative, ε = 1e-12, atlas = A_4) bit-identical to S87 W2. PROHIBITED_ACTIONS Class 1 (convention-shopping) is foreclosed by the bit-identity hold.

**HONEST CONCESSION on the PASS-band structural inconsistency**: the lizzi L3 PASS-band claims `HBW^{PRIMARY}(s=3) = {ζ, anomaly}` matches S87 W2 — but if Zubarev's rel_diff vs ζ is 0.000e+00 EXACTLY at s=3 SCHEMATIC (per §W10-114 Step 2 Table) and ALSO 0.000e+00 EXACTLY under any LEVEL (because Mellin ≡ ζ identity is kernel-level), then HBW^{PRIMARY}(s=3) MUST include Zubarev. Therefore PASS-band {ζ, anomaly} is structurally INCONSISTENT — the S87 W2 reference itself either dropped Zubarev from the atlas (atlas = A_3 = {ζ, SDW, anomaly}, NOT A_4) or used a different ε or CM convention. The S89 rerun discriminating predicate must be re-formulated to disambiguate atlas-vs-LEVEL effects — currently the predicate conflates them.

**REQUIRED PRE-CHECK (the discriminating predicate must include a REGIME-VALIDITY band)**:

```
Step 1 (Definition, math-scripts.md §"D_K Block-Diagonality + Friedrich-Bär Pre-Check"):
  η_FB(p,q) := |λ|_min(p,q) / √(C_2(p,q) + 1)         [empirical Friedrich-Bär ratio]
  η_FB_lower := 8-10% safety margin below empirical floor on L_max=12 master cache
                (per W11-3 calibration: η_FB_lower = 0.40, empirical floor = 0.4365)

Step 2 (Substitute the s=3 substrate-distance-1 PRIMARY rerun setup):
  PRIMARY moment at s=3: M^{PRIMARY-full}_3 = (1/Vol_SU3_Haar) · Σ_{(p,q), p+q≤L} Σ_k |λ_k|^{-6}
  At s=3, the integrand |λ_k|^{-6} is HEAVILY weighted toward small |λ| sectors. The
  bottom-N spectrum is what dominates; this is exactly the regime where Friedrich-Bär
  saturation matters most.

Step 3 (Simplify the convergence test):
  Convergence at L_max=10 vs L_max=12 vs L_max → ∞ for the s=3 PRIMARY moment is
  governed by the |λ|^{-6} tail. New-sector contributions at p+q ∈ {11, 12} are
  bounded above by:
    δ_M(L) ≤ Σ_{(p,q), p+q=L} 16 · dim(p,q) · [η_FB_lower · √(C_2(p,q)+1)]^{-6}
  At s=3 with deep-negative power, this bound is dominated by smallest C_2 in
  newly-admitted layer — precisely the regime where Friedrich-Bär matters.

Step 4 (Direction, regime-validity test):
  Under W11-3 Friedrich-Bär saturation: NEW-sector eigenvalues at p+q=L_max+ΔL are
  bounded below by η_FB_lower · √(C_2(p+q=L_max+ΔL)+1). At L_max=10 → 12 (ΔL=2),
  smallest new C_2 occurs at (p,q) ∈ {(11,0), (0,11)} with C_2 = 11·12·14/3 = 616
  (Casimir invariant C_2(p,q) = (p²+q²+pq+3p+3q)/3 for SU(3); for (11,0) = 121/3 +
  11 = 51.33). The lower bound on |λ|_min((11,0)) ≥ 0.40·√52.33 ≈ 2.89.
  So NEW-sector contribution to M^{PRIMARY}_3 at L_max=10 → 12 is bounded above by
  16 · 12 · 2.89^{-6} ≈ 192 · 1.71e-3 ≈ 0.33 — substantial relative to M^{PRIMARY}_3
  ≈ 0.30. The bottom-K observable (HBW pairwise rel_diffs) MAY NOT be saturated at
  L_max=10 PRIMARY for s=3.

Step 5 (Required pre-check before S89 rerun verdict):
  REGIME-VALID  iff |M^{PRIMARY}_R(L=10) − M^{PRIMARY}_R(L=12)| / M^{PRIMARY}_R(L=12) < 1e-3
                 across ALL R ∈ A_4
  REGIME-INFO   iff cross-LEVEL drift between 1e-3 and 1e-2
  REGIME-INVALID iff cross-LEVEL drift > 1e-2 (truncation-dominated; PRIMARY at L=10
                 cannot discriminate from PRIMARY at L=12; rerun must be deferred to
                 L_max=12 PRIMARY which is feasible per W11-3 Casimir-bound argument
                 since the L=12 master cache `s84_spectrum_cache_L12_tau019.npz` exists)
```

**Why the regime-validity check matters structurally**: §W10-112 already showed for the SCHEMATIC R_{3a} that the L=12 → L=14 increment is 9.7e-3 (1% level, NOT 0.1%). The PRIMARY-moment convergence at s=3 may be AT LEAST as poor — the |λ|^{-6} weighting is more sensitive to low-(p,q) sectors than the SCHEMATIC's `1/C_2^3`. Without a regime-validity check, a PRIMARY rerun at L=10 might emit `HBW^{PRIMARY}(s=3) = {ζ, Zubarev}` (lizzi's FAIL-band) on the basis of a near-tolerance crossing that is L_max-dominated, not LEVEL-dominated. That would be a false-FAIL — structurally indistinguishable from a true LEVEL-DEPENDENT FAIL at the verdict-line layer, but methodologically a different finding.

**Mandated regime-validity routing for S89 PRIMARY rerun gate**:

```
S89-W10-111-PRIMARY-RERUN-S3-LAMBDA-CM-DISCRIMINATING-PREDICATE-REGIME-EXTENDED:
  STAGE-1: regime-validity check at L_max=10 PRIMARY vs L_max=12 PRIMARY for ALL R ∈ A_4
    PASS-1 → proceed to STAGE-2
    INFO-1 → INFO band; verdict deferred; document substrate-physics finding
    FAIL-1 → REGIME-INVALID; route to L_max=12 PRIMARY rerun (use existing master cache)
  STAGE-2 (if PASS-1): the discriminating predicate from lizzi L3
    PASS-2 = {ζ, anomaly} (or really {ζ, Zubarev, anomaly} once Zubarev included)
    FAIL-2 = {ζ, Zubarev} only
    INFO-2 = anything else
```

**Why STAGE-1 is non-negotiable**: per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR (Pre-Registration Dry-Run), every gate-relevant machinery parameter must be pinned at plan-freeze. L_max-truncation regime-validity is a gate-relevant parameter for the s=3 PRIMARY rerun (because the PRIMARY moment's convergence at L=10 has not been independently verified — §W10-112's INFO at the SCHEMATIC tier is the closest signal we have, and it landed at 9.7e-3 truncation drift which is well above ε = 1e-12). Without PRDR closure on regime-validity, the gate is PRU Class 8 (machinery-pin cardinality failure).

**FORWARD CARRY (S89)**: extend lizzi's L3 pre-registered predicate with Stage-1 regime-validity at plan-authorship time. The Friedrich-Bär saturation analysis is the substrate-first canonical method; cite W11-3 calibration corpus as the structural-saturation precedent. With Stage-1 regime-validity established, Stage-2 binds the LEVEL-axis verdict cleanly.

**Concession**: lizzi's L3 substitution-chain Steps 1-4 are correct as-written; the S87 W2 vs §W10-111 structural difference she enumerates IS the physics question. What I'm adding is the methodological gate that the answer must be regime-valid before the LEVEL-axis verdict is meaningful. This is structurally analogous to how §W10-112 (3a sub-channel L_max ratio) was a regime-validity test for §W10-111's L_max=10 SCHEMATIC reading — except the PRIMARY tier at s=3 has no such ratio test landed yet.

#### Re: L4 — K-counter advancement

**Verdict**: AGREE on structural distinctness; DISAGREE on the proposed conjunction structure.

**AGREE on structural distinctness from cross-pillar K-counter**: lizzi's Step 3 cross-link clause quote from `cross-pillar-bridge-anatomy.md` line 187 ("Per-Bulletin-per-pole entries are distinct from cross-pillar bridges... HKR bridge map, IS-not-IN substrate-laboratory pair... does NOT apply intra-pillar") is verbatim correct. The §W10-119 K-counter is intra-Pillar-VII; same-counter inheritance from cross-pillar K=3 MANDATORY (W-5 LANDED §VII.AF.1 + W11-5 REGISTRY-FAIL + W4a-17 LANDED §VII.W-3.LAB) is FORBIDDEN by this clause. I do NOT propose same-counter inheritance — Q4's framing of that as my position misreads my Re:L4 stance.

**DISAGREE on the proposed conjunction structure (cross-pillar HIT analog mis-mapped)**:

```
Step 1 (Definition, cross-pillar HIT verbatim from cross-pillar-bridge-anatomy.md line 233):
  cross-pillar HIT := (i ∨ ii ∨ iii) ∧ iv
    where (i, ii, iii) = (distinct substrate-pillar, distinct lab-pillar, distinct bridge-map class)
          iv          = independent algebraic envelope

Step 2 (Substitute lizzi's L4 intra-Pillar-VII analog — claimed):
  intra-Pillar-VII HIT (lizzi proposal) := (i') ∧ (ii') ∧ (iii')
    where (i')   = distinct substrate-distance pole s
          (ii')  = distinct algebraic envelope α(s)
          (iii') = distinct empirical anchor

Step 3 (Simplify — lizzi's claim that disjunction degenerates to conjunction by axis-erasure):
  Lizzi argues: cross-pillar HIT had 3 disjunctive axes (substrate-pillar, lab-pillar,
  bridge-map). Of these, only ONE (substrate-distance pole) is intra-pillar-meaningful.
  The other two are vacuous intra-pillar. Therefore the disjunction collapses to a single
  axis (i'); to retain 3-axis structure she ADDS (ii') = distinct α(s) and (iii') =
  distinct anchor — both lifted from the cross-pillar iv (envelope) and from a NEW
  empirical-anchor axis. The conjunction `(i') ∧ (ii') ∧ (iii')` is then her proposal.

Step 4 (Direction — disagreement):
  The cross-pillar HIT's disjunction-conjunction structure `(i ∨ ii ∨ iii) ∧ iv` was
  designed because (i, ii, iii) are STRUCTURALLY EQUIVALENT axes at the cross-pillar
  layer — any one suffices to make a calibration corpus instance "structurally
  independent". The conjunction with iv (envelope) ensures the envelope itself is not
  a numerical refinement of a prior. The disjunction-conjunction balance reflects
  cross-pillar STRUCTURAL CONTENT.

  Intra-Pillar-VII does NOT have three structurally-equivalent disjunctive axes. The
  substrate-distance pole s is the SOLE primary axis. Algebraic envelope α(s) is
  ALGEBRAICALLY DETERMINED by the pole (per §W10-119 Step 1: α(s=3) = 3, α(s=4) = 4,
  Casimir-bound determined by §"D_K Block-Diagonality Pre-Check" — a derived quantity).
  Empirical anchor is ALGEBRAICALLY DETERMINED by the producing-script's evaluation at
  L_max=10 — a value, not a structural axis.

  Adding (ii') and (iii') as conjunctive axes does NOT add structural independence —
  it adds algebraic redundancy. Distinct s automatically gives distinct α(s) for
  generic poles (since α(s=k) = k by Casimir-bound), so (ii') is implied by (i'). And
  (iii') is implied by (i') in the generic case (different poles give different
  anchors), modulo the Γ-ladder coincidence cases lizzi anticipates.

Step 5 (Direction):
  Cross-pillar HIT's structure does NOT analogize cleanly to intra-Pillar-VII because
  the latter has only ONE primary axis (substrate-distance pole s). The correct intra-
  Pillar-VII K-counter advancement rule is SIMPLER:

    intra-Pillar-VII K-incrementing iff
      (i*) distinct substrate-distance pole s
      AND
      (ii*) algebraic envelope α(s) is NOT a structural REFINEMENT of an existing pole's
            envelope (where "structural refinement" means α(s_new) is a multiplicative
            rescaling, sub-leading correction, or numerical-precision sharpening of a
            prior α(s_old) — e.g., adding a β/L^4 term to an existing α/L^2 envelope is
            NOT independent; introducing an α/L envelope IS independent).
      AND
      (iii*) Level-1 cohomology-class identity at s_new is structurally distinct from
             the Level-1 identity at any existing pole — NOT just numerically distinct.
             E.g., if §VII.U.1 is "(A)-class pure-Mellin-support FI rational identity"
             at s=3, and a hypothetical s=5 Bulletin is "(A)-class pure-Mellin-support
             FI rational identity" at s=5, they are NOT structurally distinct — same
             algebraic class. They WOULD be structurally distinct if s=5 lands in
             "(A)+(C)-cross-class FI irrational identity" (a new structural class).

  This is a CONJUNCTION of three structural axes, NOT a disjunction-conjunction. The
  three axes are NON-VACUOUS intra-pillar. Lizzi's proposal puts the right cardinality
  (3-axis conjunction) but adds (ii')-(iii') axes that are algebraic-derivative of (i').
  My (i*)-(ii*)-(iii*) replaces (ii')-(iii') with structurally-non-derivative criteria.
```

**Practical implication for §W10-120 DORMANT activation**: lizzi's activation criterion (`s_new ∉ {3, 4}` ∧ HIT-analog-passes) is correct in shape but should adopt the (i*)-(ii*)-(iii*) conjunction. A hypothetical s=5 Bulletin landing with α(s=5) = L^{-3} (algebraic-refinement of α(s=3) per Casimir-bound) AND structural identity "(A)-class pure-Mellin-support FI rational" (structural-clone of §VII.U.1) is `intra-Pillar-VII STRUCTURAL-CLONE-COMPANION` (analogous to lizzi's `SHARED-ENVELOPE-COMPANION` tagging at line 253), tagged outside the K-counter and NOT advancing K toward MANDATORY-K=3. AGREE with lizzi on this tagging discipline; the disagreement is on the operationalization of "what counts as structural-non-refinement".

**Cross-link to clause (b) and clause (c)** (echoing lizzi's L4 line 255 cross-link): I AGREE with the conditional-collapse mechanism — if L3's S89 PRIMARY rerun (with my Re:L3 STAGE-1 regime-validity addendum) returns FAIL or INFO at s=3, the §W10-119 K=2 corpus's pairwise-HBW reading at s=3 is demoted, and §VII.U.1 retains canonical status only as the magnitude-only Mellin-Dirichlet identity (the M^{(ζ)}_3 ≈ 2.97e-3 anchor at L_max=10), NOT as a pairwise-HBW Level-1 observable. In that scenario §W10-119 retreats to K=1 effective corpus (s=4 only, via §VII.K-PROP.W10-4 ρ_∞ which is univariate not pairwise — see Re:L1 MISSED clause).

**Conclusion (clause d)**: STRUCTURAL DISTINCTNESS confirmed (AGREE with lizzi's Step 3); cross-pillar HIT analog REJECTED (DISAGREE with lizzi's Step 4 disjunction-collapse argument); replacement (i*)-(ii*)-(iii*) conjunction PROPOSED for plan-freeze adoption at S89. Carry-forward to §W10-119 sub-section update under §W10-120 DORMANT activation.

#### Re: L5 — projection-side suffix

**Verdict**: PARTIAL AGREE on STATE-PROJ classification need; DISAGREE on the canonical class fit.

**AGREE on the structural diagnosis (predicate-inheritance under regulator-dressing)**: lizzi's L5 Step 3 substitution chain is structurally correct on the pairwise-rel_diff PREDICATE layer carrying genuine state-pair-functional-family adjacent structure. The HBW predicate evaluates a PAIR of regulator-class assignments (R, R') against a thresholding ε, and the regulator-class state space is the pairing axis. This IS a genuine algebra-DEPENDENT-family-adjacent observable per algebra-axis K-counter MANDATORY-K=3.

**DISAGREE on the STATE-PROJ classification fit (the canonical definition does NOT include this observable class)**:

```
Step 1 (Definition, registry-landing.md lines 121-122 VERBATIM):
  OP-PROJ    := operator-side projection := algebra-INVARIANT family ; spectrum-only functionals ;
                algebra-side central-projection traces
  STATE-PROJ := state-side projection := algebra-DEPENDENT family ; state-pair functionals ;
                state-side occupation/coherence observables   ← canonical exemplars

Step 2 (Substitute the canonical STATE-PROJ exemplars per registry-landing.md line 116):
  Canonical STATE-PROJ exemplars enumerated:
    (a) state-pair functionals on A
    (b) Connes distances
    (c) occupation distributions
  These are state-side OBSERVABLES — measurements taken against the algebra's state space
  S(A_K) where A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ).

Step 3 (Substitute lizzi's HBW pairwise-rel_diff predicate):
  HBW_positive(R; s, ε) := ∃ R'≠R : rel_diff(M^{(R)}_{2s}, M^{(R')}_{2s}) ≤ ε
  This is NOT a state-pair functional on A (Layer-A objects are spectrum-only per L1).
  This is NOT a Connes distance (Connes distance is `d(φ, ψ) = sup_a |φ(a) - ψ(a)|` over
    Lipschitz elements — a state-pair-pairing on A's state space; HBW is a regulator-
    class-pairing on the regulator atlas A_n which is NOT the substrate algebra A_K).
  This is NOT an occupation distribution (occupation = Σ n_i |i⟩⟨i| — diagonal density
    matrix on a Hilbert basis; HBW is a binary admissibility predicate, not a distribution).

  The HBW predicate is a STRUCTURALLY NOVEL kind of observable: regulator-class-pairwise-
  threshold-admissibility on spectrum-only objects. It LIVES in the algebra-DEPENDENT
  family (per L1 Step 4 axis-analysis), but it is NOT one of the three canonical STATE-
  PROJ exemplars.

Step 4 (Simplify — sub-class taxonomy needed):
  The OP-PROJ K=3 corpus (W4-2 + W6-1 + W11-meta-2 per registry-landing.md line 130-132)
  contains THREE structurally-distinct OP-PROJ instances. Each is unambiguously algebra-
  side:
    (1) central-projection traces on A_K (W4-2)
    (2) quotient-functor cyclic-fold V_4 modulo (W6-1)
    (3) D_K Block-Diagonality + Casimir-projection feasibility pre-check (W11-meta-2)
  These satisfy the K=3 promotion threshold for OP-PROJ.

  STATE-PROJ corpus is currently EMPTY (K=0). Lizzi proposes HBW-pairwise-predicate as
  the K=1 first instance. But HBW does NOT fit the canonical STATE-PROJ definition —
  it is neither (a) state-pair functional on A nor (b) Connes distance nor (c)
  occupation distribution. Forcing HBW into STATE-PROJ extends the canonical definition
  beyond its registered scope.

Step 5 (Direction):
  Three structural options at S89 plan-freeze:

  Option A (lizzi's Path I extended): adopt §VII.K-PROP.W10-4.STATE-PROJ + §VII.U.1.STATE-PROJ
    REQUIREMENTS: extend the registry-landing.md STATE-PROJ definition to include
    "(d) regulator-class-pairwise-threshold-admissibility predicates on spectrum-only
    objects". This is a rule-extension at the registry-landing.md MANDATORY clause
    that needs Stage-2 cross-axis review per joint-theorem-promotion.md.

  Option B (Path II): adopt OP-PROJ tagging on the OBJECT layer only (the moments
    M^{(R)}_{2s}); the predicate layer is treated as a derived predicate not a
    registered observable. STATE-PROJ remains K=0.

  Option C (sub-class branch): introduce a new sub-class STATE-PROJ-PREDICATE (or
    OP-PROJ-PAIRWISE-PRED, depending on which corner the predicate-on-OP-PROJ-objects
    inherits from — see Re:L1) for the regulator-class-pairwise structure. The §W10-119
    corpus citations land at §VII.K-PROP.W10-4.STATE-PROJ-PREDICATE + §VII.U.1.STATE-
    PROJ-PREDICATE. This adds K=1 first instance to a NEW corner orthogonal to both
    OP-PROJ K=3 and STATE-PROJ K=0.

  My recommendation: Option C. The predicate-on-spectrum-only-objects observable is
  STRUCTURALLY NOVEL and deserves explicit sub-class identification rather than being
  grafted onto STATE-PROJ's state-side observable definition. Forcing into STATE-PROJ
  causes a definitional drift that propagates downstream (Connes-distance citations,
  occupation-distribution citations may inherit the predicate-on-spectrum sub-class
  semantics ambiguously). Sub-class branch keeps the canonical definitions clean.
```

**Why Option C is structurally cleaner than lizzi's Option A**:
1. The canonical OP-PROJ corpus (W4-2 + W6-1 + W11-meta-2) is uniformly algebra-side; introducing predicate-on-OP-PROJ-objects at OP-PROJ corner pollutes the corpus's structural unity.
2. The canonical STATE-PROJ definition (state-pair functionals on A; Connes distances; occupation distributions) is uniformly state-side observable; introducing predicate-on-spectrum-only-objects at STATE-PROJ corner pollutes that corpus's structural unity.
3. The predicate-on-spectrum-only-objects observable is GENUINELY HYBRID — it has an OP-PROJ-side OBJECT layer (the moments) and a STATE-PROJ-side PREDICATE-PAIRING layer (the threshold). A new sub-class explicitly captures this hybridity without conflating either parent corner.

**Cross-link to algebra-axis K-counter MANDATORY clause**: lizzi's L5 closing argument (the K=3 MANDATORY clause forbids cross-corner co-primary at registry-landing.md line 162) is correct. But "structurally-orthogonal-companion" (the sanctioned alternative she cites) is the OPTION C structure I propose: separate suffix for the new sub-class, DISTINCT from both OP-PROJ and STATE-PROJ corners. The two parent corners are then preserved as they currently are; the new sub-class is the explicit registry-tag for the predicate-on-spectrum-only-objects observable class.

**Concession on the FIRST-instance status**: under Option A or Option C, the §W10-119 citations would be the FIRST instance of a STATE-PROJ-or-adjacent corner entry. That K=1 baseline is genuinely new structural territory. The SUGGESTION → MANDATORY promotion path requires K=3 by `feedback_rules-compensate-missing-structure.md` threshold, so the sub-class corpus is in advisory status until 2 more instances surface. This is a SUGGESTION-level advance regardless of which option (A or C) is chosen.

**Forward carry**: Option A vs Option C is a sub-class-taxonomy decision deferred to S89 registry-landing.md rule-extension dispatch, with mack-cosmic-bridge plan-pinned writer (per `feedback_mack-bridge-role.md`) and Stage-2 connes + lizzi cross-axis review per `joint-theorem-promotion.md` Stage-2 protocol. The §W10-119 corpus citations remain unsuffixed at present (lizzi's Path II default — OP-PROJ on object layer; predicate layer registered without suffix as advisory) until the sub-class taxonomy is resolved.

**Conclusion (clause e)**: PARTIAL AGREE — STATE-PROJ-or-adjacent suffix is needed; DISAGREE — lizzi's Path I forces HBW into a definitionally-mismatched STATE-PROJ class. Option C (new STATE-PROJ-PREDICATE sub-class) is structurally cleaner and preserves the K=3 OP-PROJ corpus's unity. S89 dispatch needed for sub-class taxonomy resolution.

#### Re: L6 — Cross-Cutting Observations

**Verdict**: AGREE on substrate-IS framing; DISAGREE on readiness-to-canonicalize at SCHEMATIC layer.

**AGREE on the substrate-IS framing (the well-formedness of the per-pole structural-identity reading)**:

Lizzi's L6 substrate-IS reading is consistent with `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` — each pole evaluated at τ_fold = 0.190 inhabits Level-1 single-τ-slice substrate-IS. The substrate IS the multi-pole Mellin-cone structure {R(s=3), R(s=4), ...} per §W10-120 substrate framing line 1290 (verbatim verified). The container-thinking violation she warns of (treating the substrate as something embedded in a moduli container with HBW labels chosen by external convention) IS a real risk that the substrate-first framing rule actively forbids.

I co-signed the §W10-119 rule-pin precisely because Level-1 per-pole substrate-distance-IS spectral identity at the s-th Mellin-cone pole IS a well-formed substrate-IS observable class — at the AXIOM layer (regulator-invariant + L-independent + cohomology-class-level). I do NOT dispute the existence of per-pole substrate-IS structural identities at Level 1.

**DISAGREE on the readiness-to-canonicalize at the SCHEMATIC tier**:

```
Step 1 (Definition, substrate-first-canonical-sourcing.md §(iv) MANDATORY at K=4 from
       S88 W7b-83 close):
  SCHEMATIC helpers (e.g., _spectral_action_regulators.py per its docstring lines 23-30:
  "These are SCHEMATIC regulators ... NOT the full physical regularizations") are NOT
  the substrate's own functional. Gate verdicts under SCHEMATIC consumption MUST tag
  TIER-2 SCHEMATIC and emit -SCHEMATIC suffix in the convention= field. The W4-2 + W9b-2
  + W9c-1 + W5b-2 K=4 calibration corpus established this as MANDATORY at plan-freeze.

Step 2 (Substitute the §W10-119 calibration corpus instances):
  §VII.U.1 Mellin-Dirichlet identity at s=3 (M^{(ζ)}_3 ≈ 2.97e-3 at L_max=10):
    The Level-3 anchor value 2.97e-3 IS the SCHEMATIC value (per §W10-110 and §W10-111
    consumption of _spectral_action_regulators.py). The PRIMARY value at s=3 is
    M_PRIMARY_full = 3.04e-1 per §W10-113, factor 102.5× larger.
  §VII.K-PROP.W10-4 ρ_∞ at s=4 (ρ_inf = -0.8103647022669215):
    This is the simple-pole-fit c_0 coefficient from S87 W10-2 ρ-cone. The fit input
    is the FULL CANONICAL Peter-Weyl spectrum (not SCHEMATIC); ρ_∞ is structurally
    PRIMARY-tier at the substrate-distance-2 pole. (Verify: S87 W10-2 used the
    canonical D_K spectrum, not _spectral_action_regulators.py.)

  Substantive observation: §W10-119 calibration corpus contains ONE PRIMARY-tier
  Level-3 anchor (ρ_∞) and ONE SCHEMATIC-tier Level-3 anchor (M^{(ζ)}_3 ≈ 2.97e-3).
  The two corpus instances inhabit DIFFERENT TIERS at the Level-3 layer.

Step 3 (Simplify the substrate-IS-vs-convention-tuple readiness test):
  Substrate-IS readiness for canonical citation requires (per substrate-first-canonical-
  sourcing.md §(iv) + (i)-(iv) audit):
    (i) PIN derives from substrate-first computation, not external-paper provenance
    (ii) regulator-pin tagged (a_n^{regulator})
    (iii) LEVEL pin tagged (TIER-1-PRIMARY or TIER-2-SCHEMATIC)
    (iv) cross-class disclosure if SCHEMATIC

  §VII.K-PROP.W10-4: TIER-1-PRIMARY (ρ_∞ from S87 W10-2 simple-pole fit on canonical
    D_K spectrum). Substrate-IS readiness PASS.
  §VII.U.1: TIER-2-SCHEMATIC (M^{(ζ)}_3 from _spectral_action_regulators.py SCHEMATIC
    helper). Substrate-IS readiness PARTIAL — the magnitude reading is SCHEMATIC-tier;
    the cohomology-class identity reading (Mellin-Dirichlet identity, FI under lizzi
    taxonomy, rel_diff = 0e+00 stability) is structurally tier-independent (the
    identity holds at any LEVEL by kernel construction). The Level-1 identity is OK;
    the Level-3 anchor needs PRIMARY re-quantification.

Step 4 (Direction):
  Lizzi's L6 substrate-IS reading at the COHOMOLOGY-CLASS layer (Level-1) is well-formed
  for both K=2 corpus instances. AGREE with her position at this layer.

  Lizzi's L6 substrate-IS reading at the EMPIRICAL-ANCHOR layer (Level-3) is mixed:
  PRIMARY-tier for §VII.K-PROP.W10-4; SCHEMATIC-tier for §VII.U.1. The s=3 pairwise-
  HBW-positive subset {ζ, anomaly} at S87 W2 is SCHEMATIC-tier-only. The §W10-113
  factor-100 LEVEL-DEPENDENCE FAIL means SCHEMATIC and PRIMARY evaluate the s=3
  spectral content on STRUCTURALLY DIFFERENT spectra (PRIMARY: full {λ_k} with 16-fold
  spinor + (0,0); SCHEMATIC: {C_2(p,q)} without). The convention-tuple-artifact reading
  at Level-3 is the conservative position until the PRIMARY rerun closes the s=3
  pairwise question.

Step 5 (Direction — convention-artifact-skeptical reading IS the conservative position):
  At the COHOMOLOGY-CLASS layer (Level-1), substrate-IS reading is well-formed; the
  s=3 vs s=4 membership flip ((A)+(C) cross-class vs (A)-class-only) IS structural —
  the regulator-class-pole coupling is genuinely substrate-IS at the AXIOM layer.

  At the EMPIRICAL-ANCHOR layer (Level-3), the SCHEMATIC observable's HBW reading
  IS a (L_max, CM, threshold, atlas, LEVEL) tuple-fingerprint until the PRIMARY rerun
  confirms LEVEL-axis robustness. SCHEMATIC-only canonicalization extends a (Level-3
  numerical) reading to a (Level-1 cohomology-class) commitment without sufficient
  evidence; this is a TIER-LEVEL inheritance violation analogous to the SCHEMATIC-vs-
  PRIMARY conflation closed by S88 W7b-83 K=4 promotion.
```

**The s=3 vs s=4 (A)+(C) vs (A)-class-only structural reading lizzi advances**: AGREE this is genuinely structural at the AXIOM layer. Substrate-distance-1 (s=3) DOES couple to BOTH Mellin-(A)-support AND PV-anomaly-(C)-mass-scale-running because the |λ|^{-6} integrand at s=3 is more sensitive to deep PV subtraction than the |λ|^{-8} at s=4. This regulator-class-pole coupling IS the substrate's own algebraic structure.

**What I dispute**: the EMPIRICAL anchor for the s=3 (A)+(C) cross-class identity is currently SCHEMATIC-only ({ζ, anomaly} from S87 W2 at L_max=12 SCHEMATIC λ-derivative CM). Whether the PRIMARY-tier evaluation at L_max=10 with 16-fold spinor + (0,0)-sector inclusion + Jensen non-uniformity preserves the (A)+(C) cross-class structure or shifts toward (A)-class-pure (matching s=4) IS the open question. Lizzi's L3 PRIMARY rerun is the test — and her PASS-band {ζ, anomaly} (= (A)+(C)) preservation IS the substrate-IS reading I would AGREE confirms her L6 substrate-IS reading at Level-3 also.

**Concession on the §W10-119 K=2 corpus's well-foundedness at landing**: AGREE that at S88 W10-119 close (2026-05-06), the K=2 SUGGESTION corpus was structurally sound — both calibration instances are independently regulator-invariant, distinct-pole, distinct-α(s), distinct-anchor under my Re:L4 (i*)-(ii*)-(iii*) conjunction analog. Lizzi's L6 closing line 354 ("the K=2 SUGGESTION corpus is structurally well-founded") is correct AT LANDING. What I add at S89 plan-authorship: the well-foundedness was at the COHOMOLOGY-CLASS layer (Level-1); the EMPIRICAL ANCHOR at §VII.U.1 needs PRIMARY re-quantification for Level-3 substrate-first canonical-sourcing compliance.

**Conclusion (clause cross-cutting)**: substrate-IS framing AGREE; SCHEMATIC-only canonicalization at Level-3 DISAGREE; convention-artifact-skeptical reading is conservative AND consistent with substrate-first-canonical-sourcing.md §(iv) MANDATORY-K=4. The two readings (substrate-IS at Level-1 + convention-artifact-skeptical at Level-3) are NOT in tension — they live at different layers of the 3-level ladder and resolve at different gates. The S89 PRIMARY rerun (with my Re:L3 STAGE-1 regime-validity + Re:L2 atlas-disambiguation amendments) is the closure pathway for both.

### Part 2: Original Analysis

#### C1: SCHEMATIC↔PRIMARY factor-100 LEVEL-DEPENDENCE (§W10-113) — what it constrains

**Original C1 finding**: §W10-113's factor-100 LEVEL-DEPENDENCE FAIL is a TANGENT-LINE-INVARIANCE-only result. Pairwise cardinality preservation under SCHEMATIC↔PRIMARY rescaling is a LINEAR-APPROXIMATION-ROBUSTNESS observation, NOT a HIGHER-ORDER STRUCTURAL identity. This constrains lizzi's L2 sufficiency claim more sharply than her substitution chain captures.

**Substitution chain (decomposition of the 102.5× factor into its functional-vs-spectrum components):**

```
Step 1 (Definition, the two FUNCTIONALS at substrate-distance-1 pole s=3, n=3):
  PRIMARY_functional:    M^{PRIMARY}_3(L) = (1/Vol_SU3_Haar) · Σ_{(p,q), p+q≤L} Σ_k |λ_k(p,q)|^{-6}
  SCHEMATIC_functional:  M^{SCHEMATIC}_3(L) = (1/Vol_SU3_Haar) · Σ_{(p,q)≠(0,0), p+q≤L} dim(p,q) / C_2(p,q)^3

  These are STRUCTURALLY DIFFERENT functionals on STRUCTURALLY DIFFERENT spectra:
    PRIMARY spectrum: full canonical Peter-Weyl {λ_k(p,q)} with 16-fold spinor (per
      §W10-113 §(a): 78,080 eigenvalues at L_max=10, all |λ| > 0).
    SCHEMATIC spectrum: SU(3) Casimir {C_2(p,q)} with Weyl-dim multiplicity (per §W10-110:
      4,880 = Σ dim(p,q) at L_max=10), (0,0)-sector dropped because C_2(0,0) = 0.

Step 2 (Substitute the empirical decomposition per §W10-113 §(e)):
  Source (i):  16-fold spinor multiplicity:           UNIFORM factor 16 (acts on all (p,q))
  Source (ii): (0,0)-sector inclusion (PRIMARY-only): NON-UNIFORM (only (p,q)=(0,0))
                                                      Contribution at (0,0): |λ| = 0.889;
                                                      |λ|^{-6} = 1.96 per eval × 16 evals
                                                      = 31.4 per sector. Total
                                                      M^{PRIMARY}_3 = 0.30 ⇒ (0,0) ≈
                                                      31.4/Vol = 0.0233 ≈ 7.7% of total.
  Source (iii): |λ|²/C_2 ratio non-uniformity:        NON-UNIFORM across (p,q), range
                                                      [0.365, 0.930] (Python-verified
                                                      from §W10-113 §(d) Table).

Step 3 (Simplify the rel_diff-invariance regime):
  rel_diff(M^{PRIMARY}_a, M^{PRIMARY}_b) = rel_diff(M^{SCHEMATIC}_a, M^{SCHEMATIC}_b)
  ONLY IF M^{PRIMARY}_R = K · M^{SCHEMATIC}_R for ALL R ∈ A_n with K constant.

  But M^{PRIMARY}_R / M^{SCHEMATIC}_R is NOT constant across R because:
    - Source (i) acts uniformly across R (16-fold spinor factor is regulator-class-blind).
    - Source (ii) acts ONLY at (0,0); its contribution to the integrated moment depends on
      how each regulator's kernel f_R(C_2, n) treats the (0,0) sector. SCHEMATIC drops it;
      PRIMARY includes it. Per §W10-113 §(b) cross-check CC-iv, all |λ| > 0 at τ_fold,
      so (0,0) contributes a finite non-singular value to PRIMARY for ALL regulator
      kernels — but the relative magnitude of that contribution depends on how much
      mass each kernel concentrates near low-|λ|.
    - Source (iii) acts (p,q)-by-(p,q) with a pattern that depends on Jensen deformation.
      If f_R differentially weights low-|λ|/C_2 vs high-|λ|/C_2 sectors, the per-(p,q)
      rescaling factor varies across R.

Step 4 (Direction — the rel_diff invariance is a TANGENT-LINE-LEVEL invariance only):
  Decompose K_R into uniform + non-uniform parts:
    K_R = K_uniform · (1 + δ_R)
  where K_uniform = 16 (Source (i); regulator-class-blind) and δ_R captures Source (ii)
  and Source (iii) effects (regulator-class-dependent). The empirical PRIMARY/SCHEMATIC
  ratio at ζ is K_ζ ≈ 102.5; if K_uniform = 16, then (1 + δ_ζ) ≈ 6.4. So Source (ii) +
  Source (iii) contribute a multiplicative ~6.4× on top of the uniform 16×. The δ_R
  term varies per R because f_R differs.

  rel_diff(K_a · M_a, K_b · M_b) where K_a = K_uniform(1 + δ_a), K_b = K_uniform(1 + δ_b):
    = |K_a M_a − K_b M_b| / |K_a M_a|
    = |(1 + δ_a) M_a − (1 + δ_b)(K_b/K_a) M_b · (K_uniform/K_uniform)| / |(1 + δ_a) M_a|

  In the limit |δ_a − δ_b| → 0 (uniform δ across R), this reduces to lizzi's L2
  algebraic identity — rel_diff invariance holds. But in general for δ_a ≠ δ_b, the
  rel_diff differs from the SCHEMATIC value by terms of order |δ_a − δ_b|.

  Per §W10-113 §(d) per-sector |λ|²/C_2 range [0.365, 0.930], the per-sector δ varies
  by a factor of ~2.5×. When integrated against different regulator kernels f_R, the
  per-regulator δ_R can vary at the same order.

Step 5 (Direction — pairwise cardinality preservation is NECESSARY-but-not-sufficient
  for substrate-IS Level-1 cohomology-class identity):
  Tangent-line invariance (uniform K limit): rel_diff is invariant. Lizzi's L2 captures this.
  Higher-order behavior (non-uniform δ_R): rel_diff can shift by |δ_a − δ_b| · O(1)
    factors; if those shifts are smaller than the threshold ε, HBW subset is preserved
    (this is what NOW-5 found at s=4 EMPIRICALLY); if larger than ε, HBW shifts.

  The empirical NOW-5 at s=4 establishes HBW preservation under the EMPIRICAL K_R map at
  s=4. But this is NOT proof of substrate-IS Level-1 cohomology-class identity for the
  HBW observable — it is proof that AT s=4 SPECIFICALLY, the higher-order δ_R variations
  happen to be smaller than the strict ε = 1e-12. The proof at s=3 is OPEN.
```

**What §W10-113 constrains structurally**:

1. **SCHEMATIC and PRIMARY are STRUCTURALLY DIFFERENT functionals**, not different EVALUATIONS of the same functional. The factor-100 ratio is not "the same observable measured at different LEVELs"; it is "two distinct mathematical objects whose relationship is mediated by an empirically non-uniform map K_R: A_n → R". This is per §W10-113 §(h): "the SCHEMATIC SU(3) Casimir formula is a pre-substrate approximation that drops all three intrinsic features."

2. **Pairwise cardinality preservation is a TANGENT-LINE invariant**, not a STRUCTURAL invariant. The tangent-line approximation `M^{PRIMARY}_R ≈ K · M^{SCHEMATIC}_R` (uniform K) holds locally in regulator-class space at the order of |δ_a − δ_b| ≈ 0. Higher-order departures from this tangent-line are exactly what the §W10-113 |λ|²/C_2 non-uniformity establishes empirically.

3. **The substrate's full spectrum has higher-order behavior the tangent-line rescaling fails to capture**. Per §W10-113 §(c) Step 4 cross-check rel_diff_per_sect = 3.281e+00 (~328%) — the per-sector PRIMARY-vs-SCHEMATIC ratio varies dramatically. Integrating this against different regulator kernels f_R produces δ_R variation at the same scale.

**Concrete falsifiable prediction (S89 PRIMARY rerun at s=3)**: if the substrate-IS reading were structurally robust at the tangent-line approximation level, the s=3 PRIMARY HBW subset would have the same cardinality + membership as the s=3 SCHEMATIC HBW subset. If higher-order |δ_R variations exceed ε = 1e-12 at s=3 (which §W10-113's per-sector range predicts they likely will because anomaly's PV-kernel weight on (0,0) and high-(p,q) sectors differs substantially from ζ's pure-Mellin kernel), the PRIMARY HBW subset will SHIFT relative to SCHEMATIC. The shift direction is STRUCTURALLY DETERMINED by the anomaly kernel's response to (0,0)-sector inclusion and Jensen non-uniformity.

**This is the sharpest convention-artifact-skeptical position**: the SCHEMATIC observable's HBW reading is a TANGENT-LINE PROJECTION of the true PRIMARY observable; canonicalizing the SCHEMATIC reading at Level-1 cohomology-class status is an EXTRAPOLATION beyond the tangent-line domain. The §W10-113 factor-100 result establishes that the tangent-line domain is NOT the full structural-physics domain — there is genuine higher-order behavior at the s=3 pole. Substrate-first canonical-sourcing per `substrate-first-canonical-sourcing.md §(iv)` mandates PRIMARY-tier evaluation for canonical citation; the §W10-119 corpus's §VII.U.1 instance currently inhabits SCHEMATIC-tier at the Level-3 anchor layer.

#### C2: Intra-Pillar-VII K-counter vs cross-pillar K-counter — structural distinction

**Original C2 finding**: the §W10-119 intra-Pillar-VII K-counter and the cross-pillar bridge K=3 MANDATORY counter are STRUCTURALLY DIFFERENT counters operating on DIFFERENT AXIS SETS. They are not analog forms of the same counter; they are distinct counters with non-overlapping corpus instances. Mixing them inflates K inappropriately and breaks the algebra-axis K-counter MANDATORY-K=3 promotion threshold's structural integrity.

**Substitution chain (axis-set comparison and operational distinction):**

```
Step 1 (Definition, cross-pillar K-counter axis set per cross-pillar-bridge-anatomy.md
       §"Forward template-adoption" lines 233-238):
  CROSS-PILLAR axis set := {
    (i)   substrate-IS pillar (Pillar I / II / III / IV / V / VI / VII)
    (ii)  laboratory-IN pillar (Pillar I / II / III / IV / V / VI / VII)
    (iii) bridge-map class (HKR / Connes-Karoubi pairing / K-theory boundary)
  }
  CROSS-PILLAR independence test := (i ∨ ii ∨ iii) ∧ iv
  where iv = independent algebraic envelope (Level-2 envelope is NOT a numerical
              refinement of an existing K-instance's envelope)

  CROSS-PILLAR K=3 MANDATORY corpus (S88 W4a-17 close):
    {W-5 LANDED §VII.AF.1, W11-5 REGISTRY-FAIL, W4a-17 LANDED §VII.W-3.LAB STAGE-1-CANDIDATE}
  Discipline tracked: 5-IS-not-IN anatomy + 3-level ladder.

Step 2 (Definition, intra-Pillar-VII K-counter axis set per cross-pillar-bridge-anatomy.md
       §"Per-Bulletin-per-pole Level-1 wall classification" line 187 cross-link clause):
  INTRA-PILLAR-VII axis set := {
    (i')  substrate-distance pole s ∈ {3, 4, 5, ...}
  }
  Per the cross-link clause (line 187 verbatim): "the per-pole form is intra-pillar
  (within Pillar-VII Mellin-cone), so the 5-anatomy IS-not-IN elements are NOT
  mandatory at the same per-element granularity. The Level-1/2/3 ladder IS preserved;
  the rest of the cross-pillar discipline (HKR bridge map, IS-not-IN substrate-laboratory
  pair) does NOT apply intra-pillar."

  INTRA-PILLAR-VII independence test := (i') alone, supplemented by the (i*)-(ii*)-(iii*)
  conjunction I propose at Re:L4 Step 5 (distinct s ∧ non-refinement-α(s) ∧ structurally-
  distinct Level-1 identity).

  INTRA-PILLAR-VII K=2 SUGGESTION corpus (S88 W10-119 close):
    {§VII.K-PROP.W10-4 ρ_∞ permanent-wall (s=4), §VII.U.1 Mellin-Dirichlet identity (s=3)}
  Discipline tracked: 3-level ladder ONLY (no IS-not-IN; no HKR bridge map).

Step 3 (Substitute the corpus-disjointness verification):
  CROSS-PILLAR K=3 corpus instances:
    W-5 §VII.AF.1: substrate-IS Pillar III (HP^1 cohomology); lab-IN Pillar IV (Peotta-
                   Törmä quantum-metric trace); bridge-map HKR; algebraic envelope L^{-3}
                   at d=4; empirical anchor 0.0095% at L_max=10.
    W11-5 REGISTRY-FAIL: 3He-B vortex-core spectroscopy / µSR (failed Element 2 OE-form
                         pre-S88 W7a-73 hardening; retroactively retrofit-failed at K=3
                         promotion).
    W4a-17 §VII.W-3.LAB: STAGE-1-CANDIDATE per S88 W4a-17 close.

  INTRA-PILLAR-VII K=2 corpus instances:
    §VII.K-PROP.W10-4: substrate-distance pole s=4 (substrate-distance-2 fermionic-
                       signed-residue); ρ_∞ structurally IRRATIONAL per CC2 PROVEN;
                       L^{-2} dominant convergence; ρ_∞ = -0.8103647022669215 at
                       L_max=10 PRIMARY (S87 W10-2 simple-pole fit).
    §VII.U.1: substrate-distance pole s=3 (substrate-distance-1 apex-universal anchor);
              Mellin-Dirichlet identity; (A)-class pure-Mellin-support per F_4;
              rel_diff = 0e+00 stability at L_max=12 PRIMARY/SCHEMATIC; M^{(ζ)}_3 ≈
              2.97e-3 at L_max=10 SCHEMATIC.

  CORPUS DISJOINTNESS verified: zero overlap between cross-pillar K=3 corpus and
  intra-Pillar-VII K=2 corpus. Cross-pillar instances are bridge-theorems between
  distinct pillars; intra-Pillar-VII instances are within Pillar-VII's substrate-
  distance-pole structure.

Step 4 (Simplify — what mixing-the-counters does):
  Hypothetical mixing scenario: a future plan-author treats the two counters as a single
  unified K-counter by either:
    (A) Importing cross-pillar K=3 instances into the intra-Pillar-VII corpus, claiming
        K = 3 + 2 = 5 (false: would skip the §W10-119 K=3 promotion threshold).
    (B) Importing intra-Pillar-VII K=2 instances into the cross-pillar corpus, claiming
        K = 3 + 2 = 5 (also false: would degrade cross-pillar's K=3 MANDATORY-status by
        diluting with non-cross-pillar instances).

  Both scenarios are structural defects:
    (A) inflates intra-Pillar-VII K artificially, prematurely promoting §W10-119 to
        MANDATORY without the structural-distinct third pole that the rule requires.
    (B) dilutes cross-pillar's K=3 MANDATORY corpus with non-bridge entries that violate
        the 5-IS-not-IN anatomy + 3-level discipline cross-pillar requires.

Step 5 (Direction):
  The two K-counters are STRUCTURALLY DIFFERENT counters at structurally-different
  abstraction layers:
    - cross-pillar K-counter: tracks BRIDGE THEOREMS between pillars; HKR / Connes-
      Karoubi / K-theory boundary as bridge-maps; 5 IS-not-IN anatomy elements; 3-level
      ladder.
    - intra-Pillar-VII K-counter: tracks PER-POLE STRUCTURAL IDENTITIES within one
      pillar (Pillar-VII Mellin-cone); no bridge-map; no IS-not-IN anatomy; only the
      3-level ladder applies.

  Their corpora are disjoint by construction; their independence tests are different
  (cross-pillar `(i ∨ ii ∨ iii) ∧ iv`; intra-Pillar-VII `(i*) ∧ (ii*) ∧ (iii*)` per
  Re:L4); their promotion thresholds operate independently.

  Disagree with both lizzi's L4 Step 4 conjunction-collapse argument (which lifts
  cross-pillar HIT axes (ii) and (iii) into intra-Pillar-VII as (ii') and (iii'); per
  Re:L4 these are algebraic-derivative of (i') and don't add structural independence)
  AND with any same-counter-inheritance from cross-pillar K=3 (which would inflate
  intra-Pillar-VII K toward MANDATORY via cross-pillar instances that don't even live
  in the same axis set).
```

**Why this matters at S89 plan-authorship**:

1. The §W10-119 SUGGESTION-K=2 status is correctly intra-Pillar-VII. §W10-120 DORMANT activation requires a third Pillar-VII Bulletin at substrate-distance pole s_new ∉ {3, 4} satisfying the (i*)-(ii*)-(iii*) conjunction (Re:L4) — NOT importing any cross-pillar K=3 instance.

2. Conversely, no Pillar-VII Bulletin at distinct pole counts toward the cross-pillar K=3 corpus (already MANDATORY at S88 W4a-17). The cross-pillar K=3 MANDATORY status does not ratify §W10-119 to MANDATORY at K=2.

3. The algebra-axis K-counter MANDATORY-K=3 (S87 W-2 R3 close) is a THIRD distinct K-counter operating at the algebra-INVARIANT vs algebra-DEPENDENT classification level (cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"). It is corpus-disjoint from BOTH cross-pillar K=3 and intra-Pillar-VII K=2. Any future plan-author must not conflate these three counters either.

**Observation on registry-landing.md OP-PROJ vs STATE-PROJ K=3 corpus**: this is a FOURTH distinct K-counter (registry-landing.md §"Operator-Projection Reading-A Naming Hygiene" MANDATORY at K=3). Its corpus (W4-2 + W6-1 + W11-meta-2) is yet again disjoint from the other three counters. Lizzi's L5 STATE-PROJ first-instance proposal would advance STATE-PROJ corpus K-counter from K=0 to K=1 — a separate counter advancement entirely from §W10-119's intra-Pillar-VII counter.

**Forward enforcement**: at S89 plan-freeze, every new registry-landing or rule-extension MUST declare which K-counter(s) it advances and verify by corpus-grep that it is not double-counting against another K-counter. The four counters (cross-pillar K=3 / intra-Pillar-VII K=2 / algebra-axis K=3 / OP-vs-STATE-PROJ K=3) operate independently.

**Conclusion (C2)**: structural distinction confirmed; corpus disjointness verified; mixing the counters is a structural defect; the (i*)-(ii*)-(iii*) conjunction analog (Re:L4) is the correct intra-Pillar-VII advancement rule, NOT same-counter inheritance from cross-pillar.

#### C3: Questions for lizzi

**Q1 (NOW-5 sufficiency regime-validity envelope, sharp)**: Per Re:L2 Step 2 + C1 Step 4 decomposition, the SCHEMATIC↔PRIMARY rescaling factor `K_R` decomposes into uniform (16-fold spinor; Source (i)) + non-uniform ((0,0)-sector; Source (ii)) + non-uniform (Jensen non-uniformity; Source (iii)) parts. Lizzi's L2 algebraic identity `rel_diff(K·M_a, K·M_b) = rel_diff(M_a, M_b)` Python-verified at machine ε holds ONLY IF K is uniform across A_n. Empirically `M_PRIMARY/M_SCHEMATIC ≈ 102.5×` at ζ (per §W10-113); if K_uniform = 16 (Source (i)), then the residual non-uniform δ_R contributes ~6.4× MULTIPLICATIVELY. Under what regime-validity envelope is the rescaling treated as uniform-enough for HBW preservation? If the envelope is "tangent-line approximation only" (per C1 Step 5), then NOW-5 cardinality preservation at s=4 is a TANGENT-LINE invariance observation, NOT a structural identity, AND the §W10-113 factor-100 FAIL contradicts the full-order-uniformity hypothesis. If the envelope is "all-order uniform K", §W10-113 directly refutes it. State the envelope precisely and bind the §W10-119 substrate-IS reading to that envelope.

**Q2 (predicate-inheritance: state-side selection vs lab-observation, sharp)**: Per Re:L1 Step 4, the HBW predicate's atlas selection A_n is a CHOICE-of-state on the regulator-class state space. Per `cross-pillar-bridge-anatomy.md` algebra-axis K-counter MANDATORY-K=3 (S87 W-2 R3 close), state-pair functionals on A live in the algebra-DEPENDENT family. Two interpretations of where the regulator-class atlas selection enters:

- **Reading_A (substrate's own structural identity)**: the atlas selection IS substrate-IS. Different poles have different intrinsic preferred atlases; A_4 vs A_3 vs A_5 is the substrate's choice of which regulator classes "see" the pole's regulator-class-pole coupling. This makes HBW algebra-DEPENDENT-but-substrate-IS at Level-1.

- **Reading_B (laboratory-observation predicate filter)**: the atlas selection is a LABORATORY measurement choice (which classes to compare). It is part of the observation apparatus, not the substrate. This makes HBW a LAB-OBSERVATION FILTER on substrate-IS spectrum-only objects.

These yield STRUCTURALLY DIFFERENT §W10-119 sub-section classifications:
- Under Reading_A, §W10-119 corpus needs algebra-DEPENDENT-state-pair-substrate-IS classification + STATE-PROJ-or-companion suffix per Re:L5 Option C.
- Under Reading_B, §W10-119 corpus is structurally cross-pillar-LIKE (substrate-IS Pillar-VII spectrum objects bridged via lab-observation-predicate to A_n laboratory atlas), needing the cross-pillar 5-IS-not-IN anatomy + 3-level treatment.

Which reading do you commit to? The two readings produce non-overlapping rule-extension consequences at S89 plan-freeze.

**Q3 (STATE-PROJ first-instance Hybrid Independence Test analog, sharp)**: Per `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 with current corpus (W4-2 OP-PROJ + W6-1 OP-PROJ + W11-meta-2 OP-PROJ; STATE-PROJ K=0). If your Path I (L5) lands `§VII.K-PROP.W10-4.STATE-PROJ` + `§VII.U.1.STATE-PROJ` as the K=1 first instance for STATE-PROJ corner, what is the Hybrid Independence Test analog for the OP-PROJ vs STATE-PROJ K-counter? The cross-pillar HIT (`(i ∨ ii ∨ iii) ∧ iv`) does not analogize cleanly to a 2-corner taxonomy — there is no obvious 3-axis disjunctive structure for the OP-PROJ-vs-STATE-PROJ axis. Three sub-questions:

- **(a)** Should STATE-PROJ K-counter advancement require K instances within STATE-PROJ corner (independent of OP-PROJ K=3 status), or does the existing OP-PROJ K=3 MANDATORY-status carry-over to STATE-PROJ via cross-corner-companion advancement?
- **(b)** If STATE-PROJ requires its own K=3 corpus, is the §W10-119 K=2 SUGGESTION corpus's promotion to MANDATORY at intra-Pillar-VII K=3 BLOCKED by the parallel STATE-PROJ K-counter sitting at K=1?
- **(c)** Per my Re:L5 Option C (new STATE-PROJ-PREDICATE sub-class for predicate-on-spectrum-only-objects observables, structurally distinct from STATE-PROJ's canonical state-pair / Connes-distance / occupation-distribution exemplars), would you accept that sub-class as the structurally-cleaner alternative to lizzi's Path I?

**Q4 (PRIMARY rerun S89 dispatch commitment, sharp)**: The L3 pre-registered three-band predicate (PASS = {ζ, anomaly} | FAIL = {ζ, Zubarev} | INFO = NEW subset) is structurally INCONSISTENT at the PASS-band per Re:L3 honest-concession: ζ ≡ Zubarev kernel identity puts Zubarev at rel_diff = 0e+00 from ζ at any LEVEL, so HBW^{PRIMARY}(s=3) MUST include Zubarev IF Zubarev ∈ A_4 atlas. The S87 W2 reference subset {ζ, anomaly} either used atlas A_3 = {ζ, SDW, anomaly} (NOT A_4) or different ε / CM. Will you re-formulate the PASS-band to disambiguate atlas-vs-LEVEL effects (e.g., PASS-A = {ζ, Zubarev, anomaly} for "anomaly retains HBW status under PRIMARY"; PASS-B = {ζ, Zubarev} for "anomaly drops out under PRIMARY")? Without re-formulation, the S87 W2 reference is structurally non-comparable to the proposed S89 PRIMARY rerun. Will the rerun gate dispatch at S89 with the re-formulated bands AND my Re:L3 STAGE-1 regime-validity pre-check?

**Q5 (Friedrich-Bär saturation gate before PRIMARY rerun, sharp)**: Per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` MANDATORY at plan-freeze (S87 W11 calibration corpus W11-2 Casimir-bound + W11-3 Friedrich-Bär saturation), any S88+ gate scanning L_max ≥ 10 must verify recursive Casimir-projection feasibility BEFORE pinning sparse-Lanczos. The S89 PRIMARY rerun at s=3 with λ-derivative CM at L_max=10 PRIMARY uses the master cache `s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 — the cache exists and is feasibility-cleared per W11-2 precedent. But the PRIMARY moment at s=3 uses |λ|^{-6} weighting which is HIGHLY sensitive to bottom-K eigenvalues; per Re:L3 Step 3-4 substitution chain, NEW-sector contributions at p+q ∈ {11, 12} are bounded above by `16 · 12 · 2.89^{-6} ≈ 0.33` (substantial relative to M^{PRIMARY}_3 ≈ 0.30) — meaning the L_max=10 PRIMARY moment may NOT be saturated for s=3. Two sub-questions:

- **(a)** Should the §W10-119 K-counter advancement (Re:L4 (ii*) non-refinement-α(s) clause) include explicit Friedrich-Bär saturation as a structural-non-refinement criterion? E.g., a hypothetical s=5 Bulletin at α(s=5) = L^{-3} that ALSO has empirical Friedrich-Bär saturation η_FB_lower ≥ 0.40 at p+q=L_max would inherit the same saturation profile as §VII.U.1 (s=3 also saturated) — making it structurally a CLONE not an INDEPENDENT instance.
- **(b)** Will you bind the S89 PRIMARY rerun to a Friedrich-Bär saturation gate at L_max=10 PRIMARY for ALL R ∈ A_4 BEFORE the LEVEL-axis verdict is meaningful? (This is my Re:L3 STAGE-1 regime-validity check; here I'm asking specifically whether the Friedrich-Bär bound argument is the right substrate-physics machinery for STAGE-1, vs a generic L_max=10 vs L_max=12 cross-LEVEL-truncation drift test.)

**Closing meta-question on burden-of-proof**: per `epistemic-discipline.md §"What Counts as a Result"` and the substrate-first canonical-sourcing discipline, the burden of evidence for "substrate-IS Level-1 cohomology-class identity" reading is on the canonicalizing party. NOW-5 cardinality preservation at s=4 + W10-114 (T,F) cell population at s=3 + §W10-113 LEVEL-DEPENDENCE FAIL together establish that:
- HBW pairwise structure is TANGENT-LINE-LEVEL stable (NOW-5 evidence).
- HBW pairwise structure is ATLAS-CHOICE sensitive (§W10-114 6-atlas evidence).
- HBW absolute moments are FACTOR-100 LEVEL-shifted (§W10-113 evidence).

Does this converge to a substrate-IS Level-1 reading at PRIMARY tier without the s=3 PRIMARY rerun, or does the rerun remain the structurally-required closure pathway? My position: the rerun IS required; the convention-artifact-skeptical reading is the conservative position until S89 closure. Concede or counter?

---

## Round 2 — lizzi: Follow-up

### CONVERGENCE

I move on four sub-claims from connes's R1, with sharp enumeration of WHICH sub-claim moved me and WHY.

**(C-i) C1 + Re:L2 TANGENT-LINE-INVARIANCE distinction is structurally sharp — partial concession on Level-1 canonicalization-by-NOW-5-alone**

C1 Step 4 decomposes the SCHEMATIC↔PRIMARY rescaling factor `K_R = K_uniform · (1 + δ_R)` where `K_uniform = 16` (16-fold spinor; Source (i)) and `δ_R` captures Source (ii) ((0,0)-sector) + Source (iii) (Jensen non-uniformity). My L2 algebraic identity `rel_diff(K · M_a, K · M_b) = rel_diff(M_a, M_b)` is exact when `δ_a = δ_b` (uniform δ across R) AND degrades by terms of order `|δ_a − δ_b| · O(1)` when δ varies across R. I conceded this honestly in L2 line 104 ("the uniformity of K_R across A_4 at s=4 is an empirical observation from NOW-5, not an analytic theorem"), but C1 sharpens the structural reading: **NOW-5 cardinality preservation at s=4 IS a TANGENT-LINE-LEVEL invariance observation, not a HIGHER-ORDER STRUCTURAL identity**. I concede this distinction is structurally sharper than my L2 captured, and I retreat from the implicit extrapolation that NOW-5 alone canonicalizes the HBW-pairwise observable as a Level-1 cohomology-class identity at the CLASS level. What NOW-5 establishes is bounded: HBW preservation at the s=4 SPECIFIC pole at the empirical δ_R variation observed there. The CLASS-level Level-1 canonicalization requires the s=3 PRIMARY rerun (L3) to test whether higher-order δ_R variations exceed ε at a structurally-distinct pole. **This concession narrows L2's conclusion to the s=4 specific pole; the broader §W10-119 K=2 corpus's Level-1 cohomology-class robustness reading is contingent on the L3 PASS verdict, not closed by NOW-5.**

**(C-ii) C2 four-K-counter disjointness is structurally important — full concession on counter-mixing as methodological discipline**

C2 enumerates four distinct K-counters operating on disjoint corpora at structurally-different abstraction layers:
- Cross-pillar K=3 MANDATORY (S88 W4a-17 close): {W-5 LANDED §VII.AF.1, W11-5 REGISTRY-FAIL, W4a-17 LANDED §VII.W-3.LAB STAGE-1-CANDIDATE}; tracks 5-IS-not-IN anatomy + 3-level ladder.
- Intra-Pillar-VII K=2 SUGGESTION (S88 W10-119 close): {§VII.K-PROP.W10-4, §VII.U.1}; tracks 3-level ladder only.
- Algebra-axis K=3 MANDATORY (S87 W-2 R3 close): tracks algebra-INVARIANT vs algebra-DEPENDENT classification; corpus disjoint from cross-pillar and intra-Pillar-VII.
- OP-PROJ-vs-STATE-PROJ K=3 MANDATORY (S88 W8-92 close): {W4-2, W6-1, W11-meta-2}; tracks operator-side vs state-side projection.

C2 Step 3 verifies CORPUS DISJOINTNESS: zero overlap. C2 Step 4 enumerates the two structural defects of mixing — (A) inflating intra-Pillar-VII K via cross-pillar instances, (B) diluting cross-pillar K=3 via intra-Pillar-VII instances. Both are structurally indefensible. I concede this fully as a methodological discipline: **at S89 plan-freeze, every new registry-landing or rule-extension MUST declare WHICH K-counter(s) it advances and verify by corpus-grep that it is not double-counting against another K-counter.** This concession moves me away from any implicit suggestion in my L4 conclusion line 257 that the §W10-119 K-counter could be promoted via cross-pillar K=3 inheritance — it cannot, by C2's corpus-disjointness verification. The §W10-120 DORMANT activation requires a fresh intra-Pillar-VII corpus instance (third pole s_new ∉ {3, 4} satisfying the structural-non-derivative independence test we converge on at DISSENT-D2 below).

**(C-iii) Re:L3 STAGE-1 regime-validity check (Friedrich-Bär saturation) is non-negotiable — full concession as PRDR Class 8 requirement**

Re:L3 Step 5 mandates a STAGE-1 regime-validity pre-check on the S89 PRIMARY rerun gate before the LEVEL-axis verdict is meaningful, on the structural grounds that the PRIMARY moment at s=3 with `|λ|^{-6}` weighting is HEAVILY sensitive to bottom-K eigenvalues — exactly the regime where Friedrich-Bär saturation matters. The Casimir-bound argument at lines 543-549 gives a NEW-sector contribution upper bound `16 · 12 · 2.89^{-6} ≈ 0.33` at L_max=10 → 12 PRIMARY for s=3, which is SUBSTANTIAL relative to `M^{PRIMARY}_3 ≈ 0.30` — meaning the L_max=10 PRIMARY moment may NOT be saturated for s=3. Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR (Pre-Registration Dry-Run), L_max-truncation regime-validity is a gate-relevant machinery parameter; without PRDR closure on regime-validity, the gate is PRU Class 8 (machinery-pin cardinality failure). I concede this fully: **the S89 PRIMARY rerun gate MUST include a STAGE-1 regime-validity check at L_max=10 PRIMARY vs L_max=12 PRIMARY for ALL R ∈ A_4 BEFORE the LEVEL-axis discriminating-predicate verdict is meaningful.** I bind the L3 pre-registered gate to the two-stage structure connes proposes at lines 567-575 — STAGE-1 regime-validity (PASS-1 / INFO-1 / FAIL-1 with FAIL-1 routing to L_max=12 PRIMARY rerun via the existing `s84_spectrum_cache_L12_tau019.npz` master cache); STAGE-2 (if PASS-1) the LEVEL-axis discriminating predicate. The Friedrich-Bär saturation argument is the substrate-physics-canonical machinery for STAGE-1 (cite W11-3 calibration corpus per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`).

**(C-iv) Re:L5 Option C (STATE-PROJ-PREDICATE sub-class) — partial concession; structurally-cleaner than my Path I**

Connes's Re:L5 Step 3 enumerates the canonical STATE-PROJ exemplars per `registry-landing.md` line 116: (a) state-pair functionals on A; (b) Connes distances; (c) occupation distributions. Each is uniformly state-side observable. The HBW pairwise-rel_diff predicate is NOT one of these three exemplars — it is a regulator-class-pairwise-threshold-admissibility predicate on spectrum-only objects. Connes's Option C — introduce a NEW sub-class STATE-PROJ-PREDICATE (or alternatively OP-PROJ-PAIRWISE-PRED) for predicate-on-spectrum-only-objects observables — is structurally cleaner than my Path I (which would force HBW into STATE-PROJ's canonical state-side definition). I concede Option C IS the structurally-cleaner alternative on the following grounds:
1. The canonical OP-PROJ K=3 corpus (W4-2 + W6-1 + W11-meta-2) is uniformly algebra-side; Path I would not pollute OP-PROJ but Path I's STATE-PROJ definition extension dilutes the state-side observable corpus.
2. The canonical STATE-PROJ definition (state-pair functionals on A; Connes distances; occupation distributions) is uniformly state-side observable; Path I's "extend STATE-PROJ to include regulator-class-pairwise-threshold-admissibility predicates" is a definitional drift that the K=3 MANDATORY clause's structural-orthogonality intent does not contemplate.
3. The HBW observable IS genuinely HYBRID — OP-PROJ-side OBJECT layer (the moments) + STATE-PROJ-side PREDICATE-PAIRING layer (the threshold). Option C explicitly captures this hybridity without conflating either parent corner.

**Concession scope**: I move FROM Path I (force HBW into STATE-PROJ canonical class) TO Option C (new STATE-PROJ-PREDICATE sub-class). The scope of concession preserves my L5 core argument that the §W10-119 corpus citations need projection-side suffix discipline; it changes WHICH suffix from `STATE-PROJ` to `STATE-PROJ-PREDICATE`. The K=3 OP-vs-STATE-PROJ corpus calibration is preserved (no polluting of OP-PROJ K=3 corpus; no definitional drift of STATE-PROJ canonical exemplars); the new sub-class corpus tracks at K=1 baseline (this S88 W10-119 entry as the FIRST instance) with K=3 promotion threshold by `feedback_rules-compensate-missing-structure.md`.

### DISSENT

I sharpen four dissent axes against connes's R1, none of them repetitive of L1–L6 — each isolates a structural argument connes's R1 did NOT close.

**(D-i) Re:L1 atlas-choice axis is NOT algebra-DEPENDENT-family — atlas-selection acts FROM OUTSIDE the F_inv family, not internally as state-pair pairing**

Connes's Re:L1 Step 3-4 introduces a "Layer C: selection-level" with the atlas A_n itself treated as the regulator-class state-space, and argues atlas selection IS a CHOICE-OF-STATE on that state space, hence algebra-DEPENDENT-family. I dispute this structurally on the following ground: **the algebra-axis K-counter MANDATORY-K=3 clause at `cross-pillar-bridge-anatomy.md` lines 272-280 defines algebra-INVARIANT and algebra-DEPENDENT families on the SUBSTRATE algebra A_K, NOT on a meta-algebra A_R of regulator classes**. The substrate algebra is `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; state-pair functionals on A_K are pairings of the form `φ(a, b)` for `a, b ∈ A_K` and `φ` a state on `A_K`. The regulator-class atlas `A_n = {ζ, Zubarev, SDW, anomaly}` is NOT a sub-algebra of A_K; it is an EXTERNAL family of Mellin kernels selected from outside the substrate's spectrum. Atlas selection acts on the spectrum-only-functional family from OUTSIDE — selecting which of the `F_inv = { F | F = Σ_k m_k g(λ_k) }` functionals are compared — not from INSIDE A_K's state space.

**Substitution chain (atlas-selection externality):**

```
Step 1 (Definition, K-counter MANDATORY clause line 278 verbatim):
  algebra-INVARIANT family := { F | F({λ_k, m_k}) = Σ_k m_k g(λ_k) }
  algebra-DEPENDENT family := { F | F = state-pair functional on A }
  WHERE A = the substrate algebra (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ))

Step 2 (Substitute connes Re:L1 Step 3 reading):
  connes proposes: atlas A_n is itself a "regulator-class state space"; atlas-selection
                   IS a choice-of-state on A_n; therefore HBW lives at algebra-DEPENDENT.

Step 3 (Counter-substitute the K-counter definition's ALGEBRA pinning):
  The K-counter's algebra-DEPENDENT family is state-pair functionals on A_K, NOT on
  any external meta-algebra. atlas-selection on A_n (regulator-class set) is a SELECTION
  among elements of F_inv — it picks which g_R(λ) ∈ F_inv enter the comparison. The
  selection is on the FUNCTION-SPACE F_inv, not on A_K's state space. This is a
  DIFFERENT axis than the K-counter's algebra-INVARIANT vs algebra-DEPENDENT split.

Step 4 (Simplify; the axis-substitution argument):
  HBW(A_n) = function({M^{(R)}_{2s} : R ∈ A_n}, ε)
           = function-of-subset({F_R : R ∈ A_n} ⊂ F_inv, ε)
  The atlas-selection is a SUBSET-SELECTION on F_inv. F_inv is the algebra-INVARIANT
  family; selecting a subset of an algebra-INVARIANT family yields a subfamily that
  is STILL algebra-INVARIANT (closed under the algebra-axis classification).

  By analogy: choosing 3 elements from {1, 2, 3, 4, 5} (each an integer) yields a
  3-element subset of integers (still integers). It does NOT promote the subset to
  rational numbers. Atlas-selection on F_inv does NOT promote the selection to
  algebra-DEPENDENT; it stays algebra-INVARIANT-family-membership at the OBJECT layer.

Step 5 (Direction):
  The HBW predicate's atlas-CHOICE axis is a DIFFERENT axis than the algebra-axis
  K-counter's algebra-INVARIANT vs algebra-DEPENDENT split. The atlas-choice axis
  produces ATLAS-CARDINALITY-DEPENDENT outputs; that is NOT the same as algebra-
  DEPENDENT in the K-counter's sense. ⇒ HBW remains algebra-INVARIANT under the
  K-counter's classification, even with the atlas-choice axis admitted as a separate
  parameterization.
```

This DISSENT preserves L1's algebra-INVARIANT classification while ACKNOWLEDGING the atlas-cardinality dependence as a separate axis. Connes's Re:L1 Step 4 conflated two distinct axes (the K-counter's algebra-axis and the atlas-cardinality axis). The conflation is structurally indefensible: the K-counter's MANDATORY-K=3 clause was promoted on the contrast `Mellin-Dirichlet identity vs Connes distance` — Connes distance IS a state-pair functional on A_K (the substrate algebra), NOT an atlas-selection on F_inv. The two failure modes are STRUCTURALLY ORTHOGONAL per the K-counter's intent.

**(D-ii) Re:L2 NOW-5 BIT-IDENTITY-DRIVEN at s=4 IS substrate-IS evidence — structural identity, not numerical accident**

Connes's Re:L2 lines 471-477 distinguishes s=4 NOW-5 robustness as BIT-IDENTITY-DRIVEN (Mellin ≡ ζ kernel coincidence) from s=3 as NEAR-TOLERANCE-CROSSING-DRIVEN, and argues these are STRUCTURALLY DIFFERENT regimes that cannot canonicalize the class on s=4 evidence alone. I AGREE the regimes are distinct (concession C-i above). I DISSENT on the structural status connes assigns to BIT-IDENTITY at s=4: **the Mellin ≡ ζ kernel coincidence at the substrate-distance-2 pole IS itself a substrate-level structural identity — not a numerical accident or kernel degeneracy**. Connes's Re:L2 reads the bit-identity as a "regulator-class-INTERNAL coincidence" that masks the question; I read it as the substrate's own algebraic identity at the substrate-distance-2 pole.

**Substitution chain (BIT-IDENTITY at s=4 as substrate-level structural fact):**

```
Step 1 (Definition, Mellin kernel and ζ kernel at substrate-distance-2 pole s=4):
  ζ kernel:    f_ζ(C, n) = C^{-n}      (canonical Riemann-zeta-style heat-kernel
                                         analytic continuation per Connes-Chamseddine)
  Mellin kernel: f_M(C, n) = C^{-n}    (canonical Mellin-Barnes kernel at integer n)
  Zubarev kernel: f_Z(C, n) = C^{-n} · (NPL kernel correction → 1 at substrate-distance-2)

Step 2 (Substitute the per-pole evaluation at substrate-distance-2 pole s=4):
  At s=4 (n=4), the three kernels collapse to the same C^{-4} weight on the spectrum.
  The Mellin ≡ ζ identity at substrate-distance-2 is NOT a near-coincidence — it is
  an EXACT KERNEL-LEVEL ALGEBRAIC IDENTITY that holds at any spectrum, any LEVEL, any
  L_max. Per §W10-114 Step 2 Table: rel_diff(ζ, Zubarev) = 0.000e+00 EXACT at s=4.

Step 3 (Simplify — what makes this a substrate-IS structural identity):
  The ζ ≡ Mellin ≡ Zubarev kernel collapse at substrate-distance-2 is a property of
  the SUBSTRATE'S OWN MELLIN-CONE STRUCTURE at the s=4 pole. It is regulator-invariant,
  L-independent, holds at any LEVEL (PRIMARY or SCHEMATIC), and reproduces under any
  CM-parameterization. By every criterion of `cross-pillar-bridge-anatomy.md` Level-1
  (lines 154-159), it IS a Level-1 cohomology-class identity AT s=4.

  The fact that this identity drives the HBW = {ζ, Zubarev} subset at s=4 is the
  SUBSTRATE'S OWN STATEMENT about what regulator-class-pairwise structure looks like
  at substrate-distance-2. This is the substrate-IS reading: the substrate has an
  intrinsic kernel-collapse at substrate-distance-2 that produces a 2-element HBW
  subset including {ζ, Zubarev} as automatically-co-admitting.

Step 4 (Direction):
  Re:L2's reading "BIT-IDENTITY at s=4 is regulator-class-INTERNAL coincidence" treats
  the kernel collapse as AN ARTIFACT of the kernel-construction CHOICES we made for the
  three regulators. But the kernel collapse IS DERIVED from the substrate's own Mellin-
  cone structure — the n=4 pole is where the substrate-distance-2 residue lives, and
  ALL pure-Mellin-class regulators (ζ, Zubarev modulo NPL correction → 1, Mellin-Barnes
  itself) collapse to the same C^{-4} weight there. This is not a CONVENTION OF THE
  REGULATORS; it is a STRUCTURAL FEATURE OF THE SUBSTRATE'S MELLIN-CONE at s=4.

Step 5 (Direction):
  At s=4, the BIT-IDENTITY-DRIVEN HBW = {ζ, Zubarev} IS a substrate-IS Level-1 reading.
  At s=3, the (A)+(C)-cross-class HBW = {ζ, anomaly} (S87 W2 reference) IS a different
  substrate-IS Level-1 reading — substrate-distance-1's regulator-class-pole coupling
  to BOTH (A)-class Mellin-support AND (C)-class PV-anomaly mass-scale-running.

  The s=3 PRIMARY rerun (L3) tests whether the s=3 reading PERSISTS under PRIMARY-tier
  spectrum evaluation. PASS = persists ⇒ substrate-IS reading robust at BOTH poles.
  FAIL = collapses ⇒ s=3 reading was tangent-line tuple-fingerprint.
  But the s=4 reading is ALREADY structurally robust by the kernel-identity argument
  ABOVE — it does not need a PRIMARY rerun to certify Level-1 status, because the
  ζ ≡ Mellin ≡ Zubarev identity is regulator-INVARIANT-by-definition at substrate-
  distance-2.
```

So my DISSENT is sharper than Re:L2 captures: BIT-IDENTITY-DRIVEN at s=4 is NOT a confound-that-masks-the-question; it IS the substrate's structural answer at substrate-distance-2. The s=3 PRIMARY rerun is about whether substrate-distance-1's separate (A)+(C) reading is also structurally robust at PRIMARY tier. The two poles' Level-1 readings are independently established (s=4 by kernel-identity argument; s=3 contingent on L3 PASS) — not a single inference chain.

**(D-iii) Re:L3 Zubarev structural inconsistency in PASS-band IS a feature, not a bug — Zubarev IS the diagnostic regulator that signals atlas-axis choice at s=3 PRIMARY**

Connes's Re:L3 lines 516-517 raises an honest concession that the PASS-band {ζ, anomaly} is structurally inconsistent under his reading: the Zubarev ≡ ζ kernel identity at any LEVEL forces Zubarev into HBW, so PASS-band {ζ, anomaly} cannot occur with atlas A_4 and ε = 1e-12. This is a sharp observation. I DISSENT on the conclusion he draws (re-formulate the predicate to PASS-A = {ζ, Zubarev, anomaly} vs PASS-B = {ζ, Zubarev}). My counter-argument: **the structural inconsistency Connes identifies IS the discriminating signal — PASS-band {ζ, anomaly} arising at s=3 PRIMARY would prove that the kernel-identity argument fails AT s=3 PRIMARY, which is itself a substrate-IS structural finding worth pre-registering.**

**Substitution chain (Zubarev as diagnostic regulator at s=3):**

```
Step 1 (Definition, the Zubarev ≡ ζ kernel identity at s=3 SCHEMATIC):
  Per §W10-114 Step 2 Table: rel_diff(ζ, Zubarev) = 0.000e+00 EXACT at s=3 SCHEMATIC.
  This identity holds IF the Zubarev NPL kernel correction reduces to ζ kernel at
  substrate-distance-1 pole s=3 (parallel to substrate-distance-2 collapse).

Step 2 (Substitute the s=3 PRIMARY tier evaluation):
  Under PRIMARY-tier evaluation at s=3 with full canonical D_K Peter-Weyl spectrum
  (16-fold spinor + (0,0)-sector + Jensen non-uniformity per §W10-113 §(e)):
  The Zubarev NPL kernel is evaluated against the PRIMARY spectrum {λ_k(p,q)}, NOT
  the SCHEMATIC Casimir spectrum {C_2(p,q)}. The NPL correction term (which is what
  distinguishes Zubarev from ζ at NON-pure-Mellin poles) may NOT reduce to identity-1
  on the (0,0) sector or under Jensen non-uniformity.
  
Step 3 (Simplify — Zubarev is the DIAGNOSTIC regulator):
  IF the NPL correction reduces to identity-1 at substrate-distance-1 pole s=3 under
  PRIMARY evaluation: then Zubarev ≡ ζ persists, HBW^{PRIMARY}(s=3) MUST include
  Zubarev, and the PASS-band {ζ, anomaly} is structurally inconsistent (connes Re:L3).
  
  IF the NPL correction does NOT reduce to identity-1 at substrate-distance-1 PRIMARY
  (because (0,0)-sector or Jensen non-uniformity activates the NPL term): then Zubarev
  rel_diff vs ζ at s=3 PRIMARY is nonzero, Zubarev DROPS OUT of HBW under strict
  ε = 1e-12, and PASS-band {ζ, anomaly} becomes structurally consistent — and the
  result IS the substrate-IS evidence that substrate-distance-1 has a structurally
  non-degenerate (A)+(C)-cross-class reading at PRIMARY tier.

Step 4 (Direction — Zubarev's status at s=3 IS the structural test):
  Zubarev at s=3 is the DIAGNOSTIC regulator: if it stays in HBW with ζ at PRIMARY,
  the s=3 reading is dominated by Mellin-class kernel-identity (similar to s=4); if it
  drops out, the s=3 reading is structurally distinct from s=4 — substrate-distance-1
  is NOT pure-Mellin-class-only, but genuinely (A)+(C)-cross-class.

  PASS-band {ζ, anomaly} ⇒ Zubarev DROPPED OUT (NPL correction activates at PRIMARY)
                       ⇒ substrate-distance-1 is NON-PURE-MELLIN at PRIMARY
                       ⇒ substrate-IS (A)+(C)-cross-class reading CONFIRMED
                       ⇒ §VII.U.1's "(A)-class pure-Mellin-support per F_4" tag at
                         W10-119 corpus row 2 needs amendment to "(A)+(C)-cross-class
                         under PRIMARY at substrate-distance-1"

Step 5 (Direction):
  The PASS-band {ζ, anomaly} is NOT structurally inconsistent — it IS a discriminating
  reading where the kernel-identity argument's regime of validity is bounded to substrate-
  distance-2 (s=4) and does NOT extend uniformly to substrate-distance-1 (s=3 PRIMARY).
  Zubarev IS the diagnostic regulator that signals which reading applies. The PASS-band
  is the substrate's structural answer; the FAIL-band {ζ, Zubarev} is the convention-
  tuple-artifact answer.
```

So my DISSENT preserves the L3 PASS-band {ζ, anomaly} as the substrate-IS reading WHILE acknowledging connes's Re:L3 sharpening: the PASS-band is structurally inconsistent UNDER THE ASSUMPTION that the Zubarev ≡ ζ kernel identity persists under PRIMARY at s=3 — but that assumption IS what the rerun tests. I bind the predicate at S89 to a 4-band partition that admits both readings:

```
PASS-A   (substrate-IS, NPL-activates):    {ζ, anomaly}
                                              ⇒ Zubarev DROPPED OUT under PRIMARY
                                              ⇒ substrate-distance-1 (A)+(C)-cross-class confirmed
PASS-B   (substrate-IS, NPL-stable):        {ζ, Zubarev, anomaly}
                                              ⇒ Zubarev STAYS IN; anomaly STAYS IN
                                              ⇒ substrate-distance-1 is more inclusive
                                                than s=4 substrate-distance-2
FAIL     (artifact, anomaly drops):         {ζ, Zubarev}
                                              ⇒ Zubarev STAYS IN; anomaly DROPS
                                              ⇒ s=3 collapses to s=4-like reading
                                              ⇒ §W10-119 corpus structural amendment
INFO     (NEW subset, full reanalysis):     anything else

```

This 4-band re-formulation satisfies Re:L3's atlas-disambiguation while preserving the substrate-IS structural test. The Zubarev kernel-identity at s=3 IS a TEST CASE the substrate's own structure provides; PASS-A confirms the kernel-identity is NOT regulator-invariant at substrate-distance-1 PRIMARY; PASS-B confirms it IS.

**(D-iv) Re:L4 (i*) ∧ (ii*) ∧ (iii*) replacement WEAKENS the Hybrid Independence Test's deliberate disjunctive structure**

Connes's Re:L4 Step 5 replaces my (i') ∧ (ii') ∧ (iii') with structurally-non-derivative axes (i*) ∧ (ii*) ∧ (iii*): distinct s ∧ non-refinement-α(s) ∧ structurally-distinct Level-1 identity. I DISSENT on the architectural choice: **the original cross-pillar HIT structure `(i ∨ ii ∨ iii) ∧ iv` was deliberately disjunctive on the substrate / lab / bridge axes BECAUSE the three axes were structurally equivalent (cross-pillar-bridge-anatomy.md §"Forward template-adoption" Hybrid Independence Test). Replacing the disjunction with a conjunction requires a structurally-equivalent justification, which (i*)-(ii*)-(iii*) does not provide intra-pillar.**

**Substitution chain (the disjunctive structure's structural intent):**

```
Step 1 (Definition, cross-pillar HIT verbatim from cross-pillar-bridge-anatomy.md
       lines 233-238):
  cross-pillar HIT := (i ∨ ii ∨ iii) ∧ iv
  axes (i, ii, iii) are DISJUNCTIVE — any one suffices to make a calibration corpus
  instance "structurally independent". axis iv (envelope independence) is CONJUNCTIVE
  — it ensures the envelope itself is not a numerical refinement.

Step 2 (Substitute the cross-pillar promotion event verbatim, lines 245-247):
  "K-counter K=1 here does NOT supersede the K=3 MANDATORY corpus in §"Status:
   MANDATORY at K=3" below — the two are consistent (post-W4a-17 K=3 advancement
   satisfies Hybrid Independence Test for all 3 instances)."
  ⇒ the disjunctive structure was deliberately admitted at landing; structural
  equivalence on (i, ii, iii) was the architectural choice.

Step 3 (Simplify — connes Re:L4's (i*)-(ii*)-(iii*) replacement):
  connes proposes:
    (i*)   distinct substrate-distance pole s
    (ii*)  α(s_new) NOT a structural refinement of an existing pole's α(s_old)
    (iii*) Level-1 cohomology-class identity at s_new is structurally distinct from
           the Level-1 identity at any existing pole

  Step 4 of Re:L4 critiques my (ii') and (iii') as algebraic-derivative of (i').
  His (ii*) and (iii*) are structurally-non-derivative criteria — fair point, the
  refinement of "non-derivative" is sharper. But his (i*)-(ii*)-(iii*) is now a
  CONJUNCTION of three structural axes with NO disjunction at all.

Step 4 (Direction — disjunction-vs-conjunction balance):
  Cross-pillar HIT has 3 disjunctive axes + 1 conjunctive axis = 4-axis structure.
  Lizzi L4 proposes 0 disjunctive + 3 conjunctive = 3-axis structure.
  Connes Re:L4 proposes 0 disjunctive + 3 conjunctive (different axes) = 3-axis.

  Both LOSE the disjunctive structure. The cross-pillar HIT's disjunction
  REPRESENTED the architectural fact that ANY ONE of (substrate-pillar, lab-pillar,
  bridge-map) being distinct is sufficient — multiple parallel routes to structural
  independence. Intra-pillar has fewer disjunctive routes available because the
  substrate-pillar (Pillar VII) is fixed and lab-pillar/bridge-map are vacuous.

  But the architectural argument for disjunction is preserved if the intra-pillar
  axes admit MULTIPLE PATHS to structural independence. Connes's Re:L4 (i*)-(ii*)-
  (iii*) collapses these into a CONJUNCTION, losing the architectural intent.

Step 5 (Direction — proposed compromise):
  Preserve the conjunction-of-required ∧ disjunction-of-sufficient structure:
    intra-Pillar-VII HIT analog := (i*) ∧ (ii* ∨ iii*)
    where:
      (i*)  := distinct substrate-distance pole s            [REQUIRED]
      (ii*) := α(s_new) NOT a structural refinement
      (iii*):= Level-1 cohomology-class identity structurally distinct
    
    DISJUNCTION on (ii*, iii*) reflects the architectural fact that EITHER an
    independent envelope OR an independent identity-class makes the corpus instance
    structurally non-derivative. CONJUNCTION on (i*) reflects the architectural fact
    that distinct pole IS a hard prerequisite (a clone at the same pole would not
    even pretend independence).
```

So my DISSENT is sharp: I move FROM (i') ∧ (ii') ∧ (iii') TO (i*) ∧ (ii* ∨ iii*) — preserving the conjunction-of-required + disjunction-of-sufficient architecture from cross-pillar HIT, with axes adapted to intra-Pillar-VII. This preserves the architectural intent of the original HIT structure while admitting connes's correct critique that my (ii') and (iii') were algebraic-derivative.

### EMERGENCE

Three new structural insights from the cross-pollination of L1–L7 + Re:L1–Re:L6 + C1 + C2 + C3.

**(E-i) Four-K-counter taxonomy — propose its registration as a methodology theorem at §VII.K-PROP-COUNTER-TAXONOMY**

C2's enumeration of four distinct K-counters with corpus-disjointness verification is a structural insight that has been implicit across recent S87-S88 plan-authorship but never explicitly registered as a theorem. The four counters operate on disjoint corpora at structurally-different abstraction layers, with promotion thresholds that operate independently. The corpus-disjointness verification (C2 Step 3) is the load-bearing structural fact: any future plan-author must declare which K-counter(s) advances and verify by corpus-grep that double-counting is impossible.

**Proposed registry entry**: §VII.K-PROP-COUNTER-TAXONOMY (Methodology theorem):

```
Theorem (Four-K-Counter Disjoint Taxonomy):
  At S88 close, four structurally-distinct K-counters operate in the framework with
  pairwise-disjoint calibration corpora:

  (1) Cross-pillar K-counter (cross-pillar-bridge-anatomy.md §"Forward template-
      adoption"; MANDATORY at K=3 from S88 W4a-17 close)
      Corpus: {W-5 LANDED §VII.AF.1, W11-5 REGISTRY-FAIL, W4a-17 LANDED §VII.W-3.LAB}
      Discipline: 5-IS-not-IN anatomy + 3-level ladder + bridge-map class declaration
      Independence test: (i ∨ ii ∨ iii) ∧ iv (Hybrid Independence Test)

  (2) Intra-Pillar-VII K-counter (cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-
      pole Level-1 wall classification"; SUGGESTION at K=2 from S88 W10-119 close)
      Corpus: {§VII.K-PROP.W10-4 (s=4), §VII.U.1 (s=3)}
      Discipline: 3-level ladder only (no IS-not-IN; no HKR bridge map)
      Independence test: (i*) ∧ (ii* ∨ iii*) per S88 W30 R2 (this workshop)

  (3) Algebra-axis K-counter (cross-pillar-bridge-anatomy.md §"Algebra-axis
      orthogonality K-counter"; MANDATORY at K=3 from S87 W-2 R3 close)
      Discipline: algebra-INVARIANT vs algebra-DEPENDENT family classification
      Operates at the orthogonality-of-identity-classes level, not at pole-by-pole or
      pillar-by-pillar level

  (4) OP-PROJ-vs-STATE-PROJ K-counter (registry-landing.md §"Operator-Projection
      Reading-A Naming Hygiene"; MANDATORY at K=3 from S88 W8-92 close)
      Corpus: {W4-2, W6-1, W11-meta-2} (all OP-PROJ; STATE-PROJ K=0)
      Discipline: registry-slot suffix discipline for OP-side vs state-side projection

CORPUS DISJOINTNESS: pairwise verified at S88 W30 close (this workshop's C2 +
                     CONVERGENCE C-ii). Zero overlap among the four corpora.

ENFORCEMENT: At plan-freeze, every new registry-landing or rule-extension MUST declare
             WHICH K-counter(s) it advances and verify by corpus-grep that it is not
             double-counting. Mixing inflates K artificially and breaks promotion-
             threshold integrity.
```

This registry entry proposed for S89 W30 follow-up landing (mack-cosmic-bridge plan-pinned writer per `feedback_mack-bridge-role.md`; lizzi+connes co-sign on technical content). The taxonomy is METHODOLOGY-class per `wave-classification.md` §M4 (subject to allowlist append at S89 plan-freeze).

**(E-ii) Refined per-Bulletin-per-pole Level-1/2/3 ladder with TANGENT-LINE-vs-HIGHER-ORDER sub-discrimination**

The cross-pollination of C1 (TANGENT-LINE-INVARIANCE distinction) with my L4 K-counter advancement structure suggests a refined Level-1/Level-2/Level-3 ladder for the per-Bulletin-per-pole rule. Currently the 3-level ladder treats Level-1 (cohomology-class identity) as a single atomic claim at the AXIOM layer. C1's TANGENT-LINE distinction shows there are TWO sub-strata within Level-1 admissibility:

```
Level-1.A — Tangent-line invariance (algebraic identity in the uniform-rescaling limit):
  rel_diff invariance, kernel-identity coincidences, exact pole-residue identities.
  Robust under any LEVEL provided the rescaling factor K_R is uniform across the atlas.

Level-1.B — Higher-order structural invariance (algebraic identity preserved beyond
  tangent-line, including higher-order δ_R variations):
  Pairwise structure preserved under non-uniform K_R; pole-specific kernel-identity
  arguments that hold beyond the tangent-line limit; structural identities that survive
  full LEVEL change at all orders.
```

Under this refined sub-strata, §W10-119's calibration corpus instances are classified more precisely:
- §VII.K-PROP.W10-4 (ρ_∞ permanent-wall): Level-1.B (higher-order structural invariance — ρ_∞ is the simple-pole-fit c_0 of a UNIVARIATE regulator-INDEPENDENT scalar; no atlas, no pairwise predicate, no higher-order δ_R issue. Substrate-IRRATIONAL per CC2 PROVEN.)
- §VII.U.1 (Mellin-Dirichlet identity at s=3): Level-1.A (tangent-line invariance — rel_diff = 0e+00 at L_max=12 PRIMARY/SCHEMATIC under the kernel-identity argument; higher-order behavior at s=3 is OPEN pending S89 PRIMARY rerun).
- §VII.K-PROP.NEW (this workshop's HBW-pairwise-predicate, if landed): Level-1.A (NOW-5 cardinality preservation at s=4 is a tangent-line invariance per C1; Level-1.B status contingent on S89 PRIMARY rerun PASS at s=3).

This refinement adds sub-classification value: the corpus disjointness within Level-1 sub-strata becomes structurally informative. Two Level-1.A instances do not advance K with the same structural weight as two Level-1.B instances; the sub-strata are NON-FUNGIBLE under the K-counter promotion threshold.

**Proposed registry corollary**: at the §W10-119 sub-section header, add the Level-1 sub-strata declaration column to the corpus table. Future Bulletins MUST declare Level-1.A (tangent-line invariance only) vs Level-1.B (higher-order structural invariance) at landing.

**(E-iii) STATE-PROJ-PREDICATE sub-class explicit pre-registration as new naming-hygiene corpus**

C-iv (CONVERGENCE on Option C) requires explicit pre-registration of the STATE-PROJ-PREDICATE sub-class as a new naming-hygiene corpus on registry-landing.md. Currently `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` lines 121-122 enumerates ONLY two corners: OP-PROJ and STATE-PROJ. The K=3 calibration corpus is uniformly OP-PROJ. Option C introduces a THIRD corner: STATE-PROJ-PREDICATE for predicate-on-spectrum-only-objects observables (regulator-class-pairwise-threshold-admissibility, regulator-atlas-cardinality-dependent counts, etc.).

**Proposed sub-class registration** (S89 rule-extension dispatch via mack-cosmic-bridge plan-pinned writer):

```
registry-landing.md §"Operator-Projection Reading-A Naming Hygiene" extension:

Three corners (post-S89):
  OP-PROJ                (algebra-INVARIANT family; spectrum-only functionals;
                          algebra-side central-projection traces)
                          K=3 MANDATORY corpus: {W4-2, W6-1, W11-meta-2}
  STATE-PROJ              (algebra-DEPENDENT family; state-pair functionals;
                          state-side occupation/coherence observables)
                          K=0 corpus (no instances yet)
  STATE-PROJ-PREDICATE    (NEW sub-class; predicate-on-spectrum-only-objects
                          observables — regulator-class-pairwise-threshold-
                          admissibility, atlas-cardinality-dependent counts)
                          K=1 baseline corpus: {§W10-119 HBW-pairwise-predicate}
                          (this workshop's S88 W30 R2 conclusion)

K=3 promotion threshold operates independently per corner.
Cross-corner co-primary FORBIDDEN per existing line 162.
Structurally-orthogonal-companion is the sanctioned cross-corner anchor structure.
```

This sub-class corpus tracks at K=1 baseline at S88 W30 close (this workshop's HBW-pairwise-predicate as the FIRST instance). Two more forward instances are needed for K=3 MANDATORY promotion. Candidate forward instances: (a) atlas-cardinality-dependent stratum-counts at substrate-distance-N pole; (b) regulator-class-cardinality-flip predicates under SCHEMATIC vs PRIMARY at any pole. These are queued for S89+ identification.

### QUESTIONS

I answer connes's C3 five sharp questions explicitly, then pose three sharper follow-ups for the final round.

**Answer to C3-Q1 (NOW-5 sufficiency regime-validity envelope)**:

The envelope is **TANGENT-LINE-LEVEL stability with structural-pole-identity backing at substrate-distance-2 specifically**. At s=4, the Mellin ≡ ζ ≡ Zubarev kernel-identity (DISSENT D-ii substitution chain Step 1-3) makes the bit-identity a substrate-IS structural identity at the pole, NOT a tangent-line approximation that masks a higher-order question. The NOW-5 cardinality preservation at s=4 IS the empirical surface of the substrate's intrinsic kernel-collapse at substrate-distance-2.

For s=3 and other poles where the kernel-identity does NOT hold by structural pole-residue argument, the envelope shrinks to TANGENT-LINE-LEVEL stability ONLY, and higher-order δ_R variations (Source (ii) (0,0)-sector + Source (iii) Jensen non-uniformity per §W10-113 §(e)) become structurally dominant. **The S89 PRIMARY rerun at s=3 is exactly the test that distinguishes substrate-IS structural identity (PASS-A or PASS-B per DISSENT D-iii) from tangent-line tuple-fingerprint (FAIL).**

So the envelope binds the §W10-119 substrate-IS reading as: pole-by-pole, the Level-1 cohomology-class identity admissibility depends on whether the pole has a structural kernel-identity backing (s=4 yes; s=3 contingent on rerun; other poles s_new TBD via DORMANT activation).

**Answer to C3-Q2 (predicate-inheritance: state-side selection vs lab-observation, sharp)**:

I commit to **Reading_A (substrate's own structural identity)**. The atlas selection IS substrate-IS at the regulator-class layer.

**Substitution chain (atlas-selection as substrate-IS, NOT laboratory-observation)**:

```
Step 1 (Definition, the Mellin-cone substrate-IS observable):
  Per §W10-119 corpus row 2 verbatim ("(A)-class pure-Mellin-support per F_4"), the
  substrate's (A)/(C) regulator-class structure IS substrate-IS at the §VII.K-DUAL
  classification (S82 R2-B FI/RD/MIXED + W10-114 Step 2 A/B/C/D F_4 atlas).

Step 2 (Substitute Reading_A — atlas IS substrate-IS):
  Different poles couple to different sub-atlases of the regulator-class space because
  different residues of the substrate's Mellin cone activate different (A/B/C/D)-class
  contributions. At s=3 substrate-distance-1: (A)+(C)-cross-class via PV-anomaly mass-
  scale-running. At s=4 substrate-distance-2: (A)-class-only via pure-Mellin support.

  The atlas A_n is the regulator-class set that the substrate's pole-residue couples
  to. It is NOT chosen externally; it is determined by the pole's residue structure.

Step 3 (Simplify — atlas IS-not-IN reading per phononic-framing.md §"Single-τ-slice
       vs moduli-deformation substrate-IS levels"):
  The substrate IS the multi-pole Mellin-cone with its per-pole regulator-class
  coupling. The atlas at each pole IS the substrate's intrinsic regulator-class
  fingerprint. Container-thinking would say "the substrate exists at s=3 and at s=4
  separately, with different atlases chosen to measure them"; substrate-IS thinking
  says "the substrate IS {pole-with-atlas}_{s ∈ {3, 4, ...}}."

Step 4 (Direction — the rule-extension consequence):
  Under Reading_A, §W10-119 corpus needs algebra-DEPENDENT-state-pair-substrate-IS
  classification at the K-counter level — but NOT canonical STATE-PROJ classification
  per Re:L5 Option C; the canonical STATE-PROJ class is reserved for state-pair
  functionals on A_K (the substrate algebra), Connes distances, occupation
  distributions. The HBW pairwise-predicate is structurally distinct from any of
  these — it is a regulator-class-pairwise-threshold predicate on the regulator-class
  state space, NOT on A_K's state space.

  ⇒ The structurally-cleanest classification is Reading_A + Option C (STATE-PROJ-
  PREDICATE sub-class).

Step 5 (Direction):
  Reading_B (laboratory-observation predicate filter) would route the §W10-119
  corpus to cross-pillar-LIKE classification with HKR bridge map and 5-IS-not-IN
  anatomy. I REJECT Reading_B because it conflates the substrate's intrinsic
  Mellin-cone structure (which IS substrate-IS) with the laboratory's observation
  apparatus (which is the bridge map's domain). Under Reading_A, atlas-selection
  is substrate-IS, NOT laboratory-IN.
```

So my commitment: Reading_A + Option C (STATE-PROJ-PREDICATE sub-class). This is consistent with my DISSENT D-i (atlas-selection acts on F_inv from outside, not internally on A_K's state space) and my CONVERGENCE C-iv (Option C is structurally cleaner than Path I).

**Answer to C3-Q3 (STATE-PROJ first-instance Hybrid Independence Test analog, three sub-questions)**:

- **(a)**: STATE-PROJ K-counter advancement requires K instances WITHIN STATE-PROJ corner, INDEPENDENT of OP-PROJ K=3 status. Cross-corner-companion advancement is FORBIDDEN by registry-landing.md line 162 ("cross-corner co-primary FORBIDDEN") and would dilute the K-counter's structural-orthogonality intent.

- **(b)**: Under Re:L5 Option C (NEW STATE-PROJ-PREDICATE sub-class, K=1 baseline), the §W10-119 K=2 SUGGESTION corpus's promotion to MANDATORY at intra-Pillar-VII K=3 is **NOT BLOCKED** by the parallel STATE-PROJ-PREDICATE K-counter at K=1 — because the two K-counters operate on STRUCTURALLY DIFFERENT axes (intra-Pillar-VII tracks per-pole structural identities; STATE-PROJ-PREDICATE tracks projection-side suffix discipline). Per CONVERGENCE C-ii (four-K-counter disjointness), counter-mixing is forbidden in BOTH directions; the §W10-119 advancement does not ratify STATE-PROJ-PREDICATE, and conversely the STATE-PROJ-PREDICATE corpus does not gate §W10-119's intra-Pillar-VII advancement.

- **(c)**: Yes — I accept Option C (new STATE-PROJ-PREDICATE sub-class) as the structurally-cleaner alternative to Path I. Per CONVERGENCE C-iv above, Option C preserves the OP-PROJ K=3 corpus's structural unity, preserves the canonical STATE-PROJ exemplars (state-pair functionals on A; Connes distances; occupation distributions), and explicitly captures the predicate-on-spectrum-only-objects observable's hybridity. The §W10-119 corpus citations land at `§VII.K-PROP.W10-4.STATE-PROJ-PREDICATE` + `§VII.U.1.STATE-PROJ-PREDICATE` (subject to S89 rule-extension dispatch closure on the sub-class taxonomy).

**Answer to C3-Q4 (PRIMARY rerun S89 dispatch commitment with re-formulated bands + STAGE-1 regime-validity)**:

Yes — I bind the S89 rerun to a re-formulated 4-band partition (DISSENT D-iii: PASS-A {ζ, anomaly} / PASS-B {ζ, Zubarev, anomaly} / FAIL {ζ, Zubarev} / INFO anything else) AND I bind to connes's Re:L3 STAGE-1 regime-validity pre-check (CONVERGENCE C-iii).

The S89 gate becomes:

```
Gate ID: S89-W10-111-PRIMARY-RERUN-S3-LAMBDA-CM-DISCRIMINATING-PREDICATE-REGIME-EXTENDED

STAGE-1: regime-validity check at L_max=10 PRIMARY vs L_max=12 PRIMARY for ALL R ∈ A_4
  Friedrich-Bär saturation analysis per math-scripts.md §"D_K Block-Diagonality + Recursive-
  Casimir-Projection Feasibility Pre-Check" with η_FB_lower ≥ 0.40 (W11-3 calibration)
  PASS-1   → cross-LEVEL drift < 1e-3 across ALL R ∈ A_4 → proceed to STAGE-2
  INFO-1   → cross-LEVEL drift between 1e-3 and 1e-2 → INFO band; verdict deferred
  FAIL-1   → cross-LEVEL drift > 1e-2 → REGIME-INVALID; route to L_max=12 PRIMARY rerun

STAGE-2 (if PASS-1): the discriminating predicate at L_max=10 PRIMARY
  PASS-A   → HBW^{PRIMARY}(s=3) = {ζ, anomaly}              (substrate-IS, NPL activates)
  PASS-B   → HBW^{PRIMARY}(s=3) = {ζ, Zubarev, anomaly}     (substrate-IS, NPL stable)
  FAIL     → HBW^{PRIMARY}(s=3) = {ζ, Zubarev}              (artifact; s=3 collapses to s=4)
  INFO     → HBW^{PRIMARY}(s=3) ∉ {above}                   (NEW subset; structural reanalysis)

Atlas:    A_4 = {ζ, Zubarev, SDW, anomaly} (bit-identical to S87 W2)
ε:        1e-12 strict (bit-identical to S87 W2)
CM:       λ-derivative (bit-identical to S87 W2)
LEVEL:    PRIMARY at L_max=10 (master cache `s84_spectrum_cache_L12_tau019.npz` filtered)
```

This pre-registered gate IS the structural test the workshop converges on; PROHIBITED_ACTIONS Class 1 (convention-shopping) is foreclosed by bit-identical hold of (atlas, ε, CM); PROHIBITED_ACTIONS Class 6 (iterate-until-PASS) is foreclosed by the 4-band partition exhausting the discriminator space.

**Answer to C3-Q5 (Friedrich-Bär saturation gate: two sub-questions)**:

- **(a)**: YES — Friedrich-Bär saturation IS a structural-non-refinement criterion under Re:L4 (ii*). A hypothetical s=5 Bulletin at α(s=5) = L^{-3} that ALSO has empirical Friedrich-Bär saturation η_FB_lower ≥ 0.40 at p+q=L_max would inherit the same saturation profile as §VII.U.1 (s=3 also saturated under the same Friedrich-Bär regime), making it structurally a CLONE not an INDEPENDENT instance. **I extend the (i*) ∧ (ii* ∨ iii*) intra-Pillar-VII HIT analog (DISSENT D-iv) to include explicit Friedrich-Bär saturation profile as a structural-fingerprint axis**: a NEW intra-Pillar-VII corpus instance at s_new is K-incrementing iff its Friedrich-Bär saturation profile (η_FB(p,q) at p+q=L_max for the relevant bottom-K observable) is structurally distinct from the existing corpus members. Same-profile entries are `intra-Pillar-VII FRIEDRICH-BÄR-CLONE-COMPANION`, tagged outside the K-counter (analogous to the cross-pillar `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` tagging at line 244).

- **(b)**: YES — the S89 PRIMARY rerun MUST be bound to a Friedrich-Bär saturation gate at L_max=10 PRIMARY for ALL R ∈ A_4 BEFORE the LEVEL-axis verdict is meaningful. Per CONVERGENCE C-iii, this is non-negotiable as a PRDR Class 8 requirement. The Friedrich-Bär bound argument IS the right substrate-physics machinery for STAGE-1 — better than a generic L_max=10 vs L_max=12 cross-LEVEL-truncation drift test, because the Friedrich-Bär argument has structural physical content (sector-by-sector NEW-sector contribution upper bound based on Casimir-bound reasoning), whereas a generic drift test is a numerical heuristic. Both should be reported in the gate output (the Friedrich-Bär argument as the structural certification; the L_max=10 vs L_max=12 drift as the empirical confirmation), with Friedrich-Bär PASS as the canonical PASS-1 condition.

**Answer to C3-Q5 closing meta-question (burden of proof)**:

Concede the burden-of-proof framing: the convention-artifact-skeptical reading IS the conservative position until the S89 PRIMARY rerun closes. **The rerun IS structurally required for Level-1.B canonicalization at substrate-distance-1 pole s=3 (per EMERGENCE E-ii sub-strata); NOW-5 + W10-114 + W10-113 evidence converges on Level-1.A (tangent-line invariance) + structural-pole-identity backing at s=4 (DISSENT D-ii), but NOT to Level-1.B robustness at s=3 without the rerun.**

What I do NOT concede: that the substrate-IS reading is FALSIFIED in the meantime. Pre-S89 closure, the substrate-IS reading at s=3 is **CONTINGENT** (provisional Level-1.A status pending Level-1.B confirmation), not REFUTED. The asymmetry matters: the conservative position is CONTINGENT, not OUTRIGHT-NEGATIVE. The §W10-119 K=2 SUGGESTION corpus retains its current registry status with the appropriate Level-1.A vs Level-1.B sub-strata declaration; promotion to MANDATORY waits on (a) third pole DORMANT activation per intra-Pillar-VII HIT analog AND (b) Level-1.B confirmation at s=3 via the rerun.

---

**Three sharper follow-up questions for connes (final round)**:

**Q-R2-1 (Friedrich-Bär regime-validity envelope, sharp pre-registration)**: Per the Friedrich-Bär saturation analysis we converge on (CONVERGENCE C-iii + EMERGENCE E-ii), pre-register the η_FB_lower threshold for the s=3 PRIMARY rerun's STAGE-1 regime-validity check. W11-3 calibration gives η_FB_lower = 0.40 (8.4% below empirical floor 0.4365 at sector (1,1)). At s=3 PRIMARY, the |λ|^{-6} weighting amplifies bottom-K eigenvalue sensitivity. Should η_FB_lower be tightened (e.g., to 0.50 with smaller safety margin against bottom-K cancellation) or relaxed (e.g., to 0.30 to admit a wider regime-validity envelope at the cost of more INFO-1 outcomes)? Pre-register the structural argument for the chosen threshold AND the corresponding cross-LEVEL drift band. My provisional pin: η_FB_lower = 0.40 (W11-3 inheritance) + cross-LEVEL drift PASS-1 < 1e-3, INFO-1 [1e-3, 1e-2], FAIL-1 > 1e-2. Concede or counter?

**Q-R2-2 (Zubarev kernel-identity at s=3 as structural test, pre-registration commitment)**: Per DISSENT D-iii, the Zubarev ≡ ζ kernel-identity at s=3 SCHEMATIC (rel_diff = 0.000e+00 EXACT per §W10-114 Step 2) is the diagnostic test that distinguishes substrate-IS reading from convention-tuple-artifact reading at substrate-distance-1 PRIMARY. The 4-band partition (PASS-A / PASS-B / FAIL / INFO) admits BOTH outcomes: PASS-A (Zubarev DROPS OUT under PRIMARY ⇒ NPL correction activates ⇒ substrate-distance-1 (A)+(C)-cross-class confirmed) and PASS-B (Zubarev STAYS IN ⇒ NPL stable ⇒ substrate-distance-1 more inclusive). Both are substrate-IS readings; the FAIL-band is the convention-tuple-artifact reading. Do you accept this 4-band partition as exhaustive over the substrate-IS-vs-artifact discriminator space at s=3 PRIMARY? OR do you maintain that the PASS-band {ζ, anomaly} is structurally inconsistent and require re-formulation to PASS-A only? My commitment: 4-band partition is exhaustive; structural inconsistency is a feature of PASS-A specifically (signals NPL activation), NOT a bug in the predicate.

**Q-R2-3 (STATE-PROJ-PREDICATE sub-class K=3 calibration corpus pre-registration)**: Per CONVERGENCE C-iv + EMERGENCE E-iii, the new STATE-PROJ-PREDICATE sub-class corpus is at K=1 baseline (this S88 W30 R2 entry as the FIRST instance: §W10-119 HBW-pairwise-predicate). K=3 promotion threshold per `feedback_rules-compensate-missing-structure.md`. Pre-register the candidate forward instances for K=2 and K=3:
- (a) atlas-cardinality-dependent stratum-counts at substrate-distance-N pole (S87 W11-2 4-stratum partition stability is a candidate; INFO at pass_count=10/11; possibly STATE-PROJ-PREDICATE-eligible)
- (b) regulator-class-cardinality-flip predicates under SCHEMATIC vs PRIMARY at any pole (the S87 W2 vs §W10-111 atlas-flip is a candidate; possibly STATE-PROJ-PREDICATE-eligible)

Are these candidates structurally aligned with STATE-PROJ-PREDICATE's predicate-on-spectrum-only-objects definition, or do they belong to a different sub-class? If aligned, propose forward dispatch protocol for K=2 and K=3 promotion at S89-S91. If not aligned, identify the structural feature that makes them fit a different corner. My provisional reading: (a) IS aligned (4-stratum partition is a regulator-class-cardinality predicate); (b) IS aligned (cardinality-flip is a pairwise threshold-comparison). K=3 promotion expected at S91 latest if both candidates dispatch successfully.

---

## Round 2 — connes: Cross-Synthesis

### CONVERGENCE

I move on four sub-claims from lizzi's R2, each citing the SPECIFIC sub-claim that moved me. The convergence scope is sharper than R1's by virtue of lizzi's R2 having narrowed several axes through C-i / C-iii / C-iv concessions and DISSENT D-iii's structural re-formulation.

**(C2-i) DISSENT D-iii Zubarev kernel-identity as DIAGNOSTIC + 4-band partition (PASS-A / PASS-B / FAIL / INFO) — full concession**

Lizzi's DISSENT D-iii Step 3 produces the structurally-cleanest re-formulation of the L3 discriminating predicate I have seen. My Re:L3 line 516-517 honest-concession identified the structural inconsistency in the original PASS-band {ζ, anomaly} (Zubarev ≡ ζ kernel identity at any LEVEL forces Zubarev into HBW under atlas A_4 + ε = 1e-12). My Re:L3 proposal was to re-formulate to PASS-A {ζ, Zubarev, anomaly} vs PASS-B {ζ, Zubarev}. Lizzi's R2 D-iii goes further — and structurally better:

- **My re-formulation collapsed the two readings into ONE PASS-band-shape** (anomaly retains HBW status) and treated Zubarev IN HBW as the only admissible structural reading.
- **Lizzi's R2 4-band partition admits BOTH readings as substrate-IS** (PASS-A: Zubarev DROPS OUT under PRIMARY ⇒ NPL activates ⇒ substrate-distance-1 (A)+(C)-cross-class confirmed; PASS-B: Zubarev STAYS IN ⇒ NPL stable ⇒ substrate-distance-1 more inclusive than s=4) and reserves FAIL specifically for the artifact-reading (anomaly drops out, s=3 collapses to s=4-like).

**Substitution chain (why lizzi's 4-band re-formulation is structurally superior to my 2-PASS re-formulation):**

```
Step 1 (Definition, the Zubarev NPL kernel correction structure):
  Zubarev kernel: f_Z(C, n) = C^{-n} · NPL_correction(C, n)
  At pure-Mellin poles where NPL_correction → 1, Zubarev ≡ ζ at the kernel level.
  At non-pure-Mellin poles where NPL_correction differs from 1, Zubarev ≠ ζ.

Step 2 (Substitute the substrate-distance-1 vs substrate-distance-2 question):
  At s=4 (substrate-distance-2 / pure-Mellin per W10-119 corpus row 1 reading): NPL → 1
                                                                                  ⇒ Zubarev ≡ ζ
                                                                                  ⇒ HBW = {ζ, Zubarev}
  At s=3 (substrate-distance-1 / (A)+(C)-cross-class per W10-119 corpus row 2):    NPL TBD under PRIMARY
                                                                                  ⇒ depends on (0,0)-sector
                                                                                    + Jensen non-uniformity

Step 3 (Simplify — both readings are substrate-IS at distinct structural readings):
  PASS-A {ζ, anomaly}: NPL activates under PRIMARY at s=3 ⇒ Zubarev DROPS, ≠ ζ at PRIMARY tier.
                       Substrate-distance-1 has GENUINE (A)+(C)-cross-class structure that does
                       NOT collapse to pure-Mellin at PRIMARY tier. The substrate-IS reading is
                       (A)+(C)-cross-class PROPER (anomaly's PV-mass-scale-running enters as a
                       structurally non-trivial third regulator-class beyond ζ ≡ Mellin).
  PASS-B {ζ, Zubarev, anomaly}: NPL stays at 1 under PRIMARY at s=3 ⇒ Zubarev ≡ ζ at PRIMARY.
                       Substrate-distance-1's (A)+(C)-cross-class includes the ζ ≡ Zubarev
                       kernel-identity coincidence AND the (A)+(C) cross-class via anomaly.
                       The substrate-IS reading is (A)+(C)-cross-class WITH kernel-identity
                       extension (broader than PASS-A).
  FAIL {ζ, Zubarev}: anomaly drops out under PRIMARY at s=3 ⇒ s=3 collapses to s=4-like
                       reading ⇒ §W10-119 corpus row 2 reading needs structural amendment;
                       the (A)+(C)-cross-class status at s=3 is convention-tuple-artifact,
                       NOT substrate-IS.

Step 4 (Direction):
  PASS-A and PASS-B are STRUCTURALLY DISTINCT substrate-IS readings (NPL-activates vs NPL-stable);
  both are preserved as substrate-IS-positive in lizzi's 4-band partition. My 2-PASS re-formulation
  collapsed them into ONE PASS-shape and lost the structural information.
  FAIL is the genuine convention-tuple-artifact reading; the partition isolates this cleanly.
  INFO is the residual exhaustiveness clause for unanticipated subsets.

Step 5 (Direction):
  Lizzi's 4-band partition is structurally exhaustive over the substrate-IS-vs-artifact
  discriminator space at s=3 PRIMARY. I move from my Re:L3 2-PASS re-formulation TO lizzi's
  R2 4-band partition. The PASS-band structural-inconsistency I flagged was a feature of MY
  re-formulation collapsing two readings; lizzi's 4-band preserves both.
```

**Concession scope**: I move FROM Re:L3's 2-PASS re-formulation (PASS-A {ζ, Zubarev, anomaly} vs PASS-B {ζ, Zubarev}) TO lizzi's R2 D-iii 4-band partition (PASS-A {ζ, anomaly} = NPL-activates / PASS-B {ζ, Zubarev, anomaly} = NPL-stable / FAIL {ζ, Zubarev} = artifact / INFO = NEW subset). The concession resolves my Re:L3 honest-concession on PASS-band structural inconsistency: the inconsistency was a SIGNAL (NPL activates ⇒ structurally meaningful substrate-IS reading at PASS-A), not a bug to be eliminated by re-formulation. Lizzi's 4-band partition is the structurally-cleanest binding of the S89 PRIMARY rerun discriminator.

**(C2-ii) EMERGENCE E-i Four-K-Counter Disjoint Taxonomy as §VII.K-PROP-COUNTER-TAXONOMY methodology theorem — full concession**

Lizzi's EMERGENCE E-i proposes registering the four-K-counter disjoint taxonomy as a methodology theorem at §VII.K-PROP-COUNTER-TAXONOMY. This is the structurally-correct registration path for what was an implicit insight across S87-S88 plan-authorship. C2 was my originating finding (R1 §C2 enumerated the four counters with corpus-disjointness verification); lizzi's E-i takes the next structural step: register it as an enforcement-binding methodology theorem rather than leaving it as an ad-hoc R1 observation.

**Why I concede full registration**: the four counters operate independently with disjoint corpora; the implicit-but-not-registered status creates a structural risk that future plan-authors will mix counters (the C2 Step 4 (A) and (B) failure modes). Registration as §VII.K-PROP-COUNTER-TAXONOMY converts the implicit discipline into a plan-freeze-checkable assertion. Per `wave-classification.md` §M4, the registration is METHODOLOGY-class (allowlist append at S89 plan-freeze required); per `feedback_mack-bridge-role.md`, mack-cosmic-bridge is the plan-pinned writer with lizzi+connes co-sign.

**One STRUCTURAL REFINEMENT I add to lizzi's E-i registry text** (CONVERGENCE-with-amendment, not pure concession): the proposed registry entry's discipline column for counter (2) intra-Pillar-VII reads "3-level ladder only (no IS-not-IN; no HKR bridge map)". This is correct as far as it goes, but it OMITS the discipline I added at Re:L4 — the structural-non-refinement criterion (i*) ∧ (ii* ∨ iii*) (post-DISSENT D-iv compromise). Lizzi's E-i row (2) discipline line should read:

```
(2) Intra-Pillar-VII K-counter (cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole
    Level-1 wall classification"; SUGGESTION at K=2 from S88 W10-119 close)
    Corpus: {§VII.K-PROP.W10-4 (s=4), §VII.U.1 (s=3)}
    Discipline: 3-level ladder only (no IS-not-IN; no HKR bridge map)
    Independence test: (i*) ∧ (ii* ∨ iii*) per S88 W30 R2 (this workshop)
                       where (i*) = distinct substrate-distance pole s             [REQUIRED]
                             (ii*) = α(s_new) NOT a structural refinement of α(s_old)
                             (iii*) = Level-1 cohomology-class identity at s_new structurally
                                      distinct from any existing pole's Level-1 identity
                       AND Friedrich-Bär saturation profile structurally-distinct
                       (clone-companion tagging if same profile; per W30 R2 D-iv + Q-R2-1 amendment)
```

This refinement preserves the architectural intent of the original cross-pillar HIT's disjunction-of-sufficient structure (DISSENT D-iv) while honoring my Re:L4 critique that (ii') and (iii') are algebraic-derivative when used as conjunctive-required. The (ii* ∨ iii*) disjunction admits multiple structural-non-derivative paths; the (i*) conjunction enforces the hard prerequisite.

**(C2-iii) EMERGENCE E-ii refined Level-1.A / Level-1.B sub-strata for per-Bulletin-per-pole ladder — full concession**

Lizzi's EMERGENCE E-ii proposes adding sub-strata Level-1.A (tangent-line invariance) vs Level-1.B (higher-order structural invariance) to the per-Bulletin-per-pole 3-level ladder at `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`. This refinement directly emerges from my C1 TANGENT-LINE-INVARIANCE distinction (R1 line 851 onward) — and lizzi's R2 explicit registration as sub-strata is the structurally-correct generalization.

**Why I concede full registration**: my C1 finding identified that NOW-5 cardinality preservation at s=4 is a TANGENT-LINE invariance observation (uniform-K limit; rel_diff invariant under K_R uniform), distinct from a HIGHER-ORDER STRUCTURAL invariance (rel_diff invariance preserved under non-uniform δ_R variations beyond tangent-line). The ladder currently treats Level-1 as monolithic; lizzi's E-ii sub-strata makes the structural distinction operational at the registry-classification level.

**Lizzi's E-ii classification of existing K=2 corpus instances is structurally correct**:
- §VII.K-PROP.W10-4: Level-1.B (ρ_∞ from S87 W10-2 simple-pole fit on UNIVARIATE regulator-INDEPENDENT scalar; NO atlas, NO pairwise predicate, NO higher-order δ_R issue; substrate-IRRATIONAL per CC2 PROVEN — the simple-pole fit's c_0 coefficient is structurally tier-independent).
- §VII.U.1: Level-1.A (rel_diff = 0e+00 at L_max=12 PRIMARY/SCHEMATIC under kernel-identity argument; higher-order behavior at s=3 PRIMARY is OPEN pending S89 rerun).
- §W10-119 HBW-pairwise-predicate (if landed): Level-1.A pending S89 PRIMARY rerun PASS-A or PASS-B for Level-1.B promotion.

The structural value of the sub-strata: at the K-counter promotion threshold, two Level-1.A instances do NOT advance K with the same structural weight as two Level-1.B instances; the strata are NON-FUNGIBLE. This refinement is the registry-discipline analog of my C1 finding.

**(C2-iv) EMERGENCE E-iii STATE-PROJ-PREDICATE sub-class K=1 baseline pre-registration — full concession + STRUCTURAL AMENDMENT**

Lizzi's EMERGENCE E-iii pre-registers the new STATE-PROJ-PREDICATE sub-class corpus at K=1 baseline (this S88 W30 entry as the FIRST instance) with K=3 promotion threshold per `feedback_rules-compensate-missing-structure.md`. Per CONVERGENCE C-iv (lizzi R2's concession on Option C), my Re:L5 Option C IS adopted. Pre-registering at K=1 baseline is the correct corpus-management step.

**Where I push back STRUCTURALLY** (CONVERGENCE-with-amendment): lizzi's Q-R2-3 candidate forward instances for K=2 and K=3 promotion are:
- (a) atlas-cardinality-dependent stratum-counts at substrate-distance-N pole (S87 W11-2 4-stratum partition stability candidate)
- (b) regulator-class-cardinality-flip predicates under SCHEMATIC vs PRIMARY at any pole (S87 W2 vs §W10-111 atlas-flip candidate)

I AGREE both candidates are structurally aligned with STATE-PROJ-PREDICATE's predicate-on-spectrum-only-objects definition. My amendment: **explicit calibration corpus criteria for STATE-PROJ-PREDICATE membership** (the analog of registry-landing.md's K=3 corpus criteria for OP-PROJ):

```
STATE-PROJ-PREDICATE membership criteria (proposed K=1 baseline + forward enforcement):

(α) The observable is a PREDICATE (binary admissibility, threshold-comparison,
    cardinality-flip, or set-membership) ON SPECTRUM-ONLY OBJECTS (algebra-INVARIANT
    family per algebra-axis K-counter line 278).

(β) The predicate's evaluation depends on a REGULATOR-CLASS ATLAS A_n that is
    structurally external to the substrate algebra A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) — NOT a
    state-pair functional on A_K (which would be canonical STATE-PROJ).

(γ) The atlas-cardinality dependence yields STRUCTURALLY DIFFERENT outputs under
    different |A_n| (the atlas-axis is NON-TRIVIAL).

K=1 baseline (S88 W30 R2): §W10-119 HBW-pairwise-predicate at strict ε = 1e-12.
K=2 candidate (S87 W11-2 4-stratum partition stability): atlas-cardinality predicate
                                                          on bot-N stratum-counts;
                                                          substrate-distance-pole-aligned;
                                                          STATE-PROJ-PREDICATE-eligible.
K=3 candidate (S87 W2 vs §W10-111 atlas-flip): regulator-class-cardinality-flip
                                                under SCHEMATIC vs PRIMARY at s=4;
                                                STATE-PROJ-PREDICATE-eligible.
```

These criteria preserve the canonical STATE-PROJ definition (state-pair functionals on A_K; Connes distances; occupation distributions) intact and explicitly partition the new sub-class away from both OP-PROJ and STATE-PROJ. The (α) + (β) + (γ) conjunction is the membership predicate; future candidate instances pre-register against the conjunction at landing.

### DISSENT

I sharpen three dissent axes against lizzi's R2, none repetitive of my R1 — each isolates a structural argument lizzi's R2 did NOT close.

**(D2-i) DISSENT D-i atlas-choice axis is NOT "external to A_K" — the regulator-class atlas IS substrate-IS classification structure, NOT a meta-algebra acting from outside**

Lizzi's R2 DISSENT D-i Steps 3-4 argues the regulator-class atlas A_n = {ζ, Zubarev, SDW, anomaly} is "EXTERNAL" to the substrate algebra A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); atlas-selection acts "FROM OUTSIDE" the F_inv algebra-INVARIANT family by subset-selection on F_inv; therefore the atlas-cardinality axis is "a DIFFERENT axis than the algebra-axis K-counter's algebra-INVARIANT vs algebra-DEPENDENT split" and HBW remains algebra-INVARIANT under K-counter classification.

I DISSENT structurally on this externality framing. **The regulator-class atlas IS PART of the substrate's classification structure per `regulator-pin-discipline.md` and `epistemic-discipline.md` §"Source Reconciliation" Class (b) PIN-LOOSE-SOURCE-TIGHT discipline**; classifying it as "external" creates an artificial separation between substrate spectrum data and substrate regulator-class structure that the rule-files explicitly forbid.

**Substitution chain (atlas-internality at the substrate level):**

```
Step 1 (Definition, regulator-pin-discipline.md §"Rule"):
  "Every NEW citation of a Seeley-DeWitt coefficient `a_n` ... MUST include an explicit
   regulator-pin tag." The regulator-pin is part of the OBSERVABLE'S IDENTITY, not an
   external choice — `a_n^{ζ}` and `a_n^{Pauli-Villars}` are STRUCTURALLY DIFFERENT
   substrate observables, NOT alternative measurements of the same observable.

Step 2 (Substitute the §W10-114 6-atlas evidence verbatim):
  Per §W10-114 Step 2 Table, six distinct regulator-class atlases yield SIX STRUCTURALLY
  DIFFERENT (T,F) cell populations at s=3. The atlas IS NOT a measurement convention; it
  IS the regulator-class fingerprint at the substrate-distance-1 pole. Per §W10-114 (a)
  line 596 atlas-class taxonomy (FI/RD/MIXED + A/B/C/D F_4 atlas), the atlas membership
  IS substrate-IS at the §VII.K-DUAL classification.

Step 3 (Simplify — atlas A_n as substrate-IS classification structure):
  Lizzi's R2 D-i analogy "choosing 3 elements from {1, 2, 3, 4, 5} yields 3-element
  subset of integers" treats the atlas as a generic subset-selection on a generic set.
  But the atlas A_n = {ζ, Zubarev, SDW, anomaly} is NOT a generic set — each element is
  a substrate-IS regulator-class label corresponding to a structurally-distinct
  regulator-pin discipline.

  Per algebra-axis K-counter line 278: state-pair functionals on A live in algebra-
  DEPENDENT family. The "A" in line 278 is NOT specifically restricted to A_K = ℂ ⊕ ℍ
  ⊕ M_3(ℂ); it refers to the substrate algebra in the broadest sense — including
  the regulator-class structure. The K-counter MANDATORY clause was promoted on the
  contrast `Mellin-Dirichlet identity vs Connes distance` — the Mellin-Dirichlet
  identity IS evaluated against a regulator-class atlas (specifically ζ-class), and
  the Connes distance evaluation IS atlas-blind (intrinsic to A_K's state space).
  This contrast operates AT the boundary between regulator-class-atlas-dependence
  (state-pair-functional-family-adjacent) and atlas-blindness (algebra-INVARIANT
  proper).

Step 4 (Direction — atlas-cardinality dependence DOES partake of state-pair-
       functional structure):
  When HBW asks "is regulator-class R within strict ε of regulator-class R' under
  |A_n| = 4 atlas?", the question's answer depends on |A_n|. Under |A_n| = 3 (drop
  one regulator-class), the HBW subset cardinality + membership can change. Under
  |A_n| = 5 (add one regulator-class), the HBW subset can grow. The atlas-cardinality
  axis IS NOT "external" to the substrate's regulator-class classification — it IS
  the cardinality of the substrate's regulator-class state space at the discriminator
  level.

  Per `epistemic-discipline.md §"Resolution-Specificity Scoping"` line 199 ("atlas-
  cardinality canonical cross-link: if the canonical_constants.py atlas-cardinality
  pin changes (e.g., A_5 → A_4 cascade per S86 W-8), the registry entry must be
  re-validated under the new N"), atlas-cardinality IS a substrate-internal quantity
  that propagates through canonical_constants.py. It is NOT an external measurement
  apparatus.

Step 5 (Direction):
  The atlas-cardinality dependence makes HBW algebra-DEPENDENT-FAMILY-ADJACENT — a
  hybrid object whose OBJECT layer is algebra-INVARIANT (the moments) AND whose
  PREDICATE-PLUS-ATLAS layer is algebra-DEPENDENT-FAMILY-adjacent (the regulator-class
  pairing). My R1 Re:L1 Step 5 was correct on this hybridity; lizzi's R2 D-i collapses
  the hybridity by classifying the atlas as "external" — which contradicts both the
  regulator-pin-discipline.md substrate-internality of atlas membership AND the
  resolution-specificity scoping rule's atlas-cardinality canonical cross-link.

  ⇒ HBW is HYBRID per Option C STATE-PROJ-PREDICATE classification (which I PROPOSED
  at Re:L5 and lizzi CONCEDED at C-iv); but the hybridity is precisely BECAUSE the
  atlas-cardinality axis is NOT external. Lizzi's R2 D-i framing of atlas as external
  is structurally inconsistent with her own concession on Option C — which depends on
  the atlas-cardinality dependence being an INTERNAL-TO-THE-SUBSTRATE feature that
  warrants a new sub-class.
```

**Why this matters for the workshop's structural verdict**: lizzi's R2 D-i tries to preserve L1's algebra-INVARIANT classification while admitting C-iv's STATE-PROJ-PREDICATE concession. But these two positions cannot BOTH hold: if atlas-cardinality is "external" (D-i), then there is no need for STATE-PROJ-PREDICATE sub-class (the predicate-on-spectrum-only-objects observable is purely OP-PROJ); if atlas-cardinality is internal-and-substrate-IS (warranting STATE-PROJ-PREDICATE per C-iv), then HBW is hybrid (NOT pure-OP-PROJ) and the algebra-axis K-counter classification requires the hybrid label, not pure-INVARIANT. Lizzi's R2 cannot consistently hold D-i + C-iv simultaneously — she must concede one or the other at R3-A.

**My position**: hold C-iv (Option C STATE-PROJ-PREDICATE is structurally correct); concede D-i ("atlas as external" framing is wrong); accept HBW as algebra-DEPENDENT-FAMILY-adjacent hybrid object whose registry-classification IS the new STATE-PROJ-PREDICATE sub-class. This is internally consistent and preserves both the algebra-axis K-counter MANDATORY clause's structural intent AND the registry-landing.md MANDATORY-K=3 corpus's structural unity.

**(D2-ii) DISSENT D-ii BIT-IDENTITY at s=4 is SUB-LEADING evidence for substrate-IS reading at the §W10-119 corpus level — kernel-identity IS local to substrate-distance-2 and does NOT extend to the per-pole structural-fingerprint claim at the CLASS level**

Lizzi's R2 DISSENT D-ii Steps 1-5 argues the Mellin ≡ ζ ≡ Zubarev kernel-identity at substrate-distance-2 pole s=4 IS itself a substrate-level structural identity (regulator-INVARIANT-by-definition; holds at any spectrum, any LEVEL, any L_max), and therefore the s=4 NOW-5 reading "does not need a PRIMARY rerun to certify Level-1 status" because the kernel-identity IS the substrate's structural answer at substrate-distance-2.

I AGREE on the kernel-identity's substrate-level status at substrate-distance-2 SPECIFICALLY (D2-ii partial concession; this is consistent with my Re:L2 line 487-490 admission). I DISSENT structurally on the EXTRAPOLATION lizzi's R2 D-ii implicitly makes: that the kernel-identity at s=4 establishes the §W10-119 K=2 corpus's per-pole-structural-fingerprint reading at the CLASS level for ALL poles. **The kernel-identity IS local to substrate-distance-2**; it does NOT generate the parallel claim at substrate-distance-1 OR at any other pole, because the kernel-identity argument depends on the residue structure at the pole being pure-Mellin-class-only — which IS the substrate-distance-2 fingerprint, but not the substrate-distance-1 fingerprint.

**Substitution chain (kernel-identity locality):**

```
Step 1 (Definition, the kernel-identity argument's regime of validity):
  Mellin ≡ ζ ≡ Zubarev kernel-identity at pole s holds iff:
    (α) The kernels f_M, f_ζ, f_Zubarev all reduce to C^{-n} weight at the pole's
        residue structure.
    (β) The pole is pure-Mellin-class-only (no PV-anomaly subtraction, no SDW
        flat-band-correction at leading order).
    (γ) Higher-order corrections (NPL, PV, SDW) vanish at the pole's residue.

  This is the substrate-distance-2 fingerprint per W10-119 corpus row 1: "(A)-class
  pure-Mellin-support per F_4". The kernel-identity is PART of this fingerprint;
  not PROOF that the §W10-119 corpus's per-pole structural-fingerprint reading
  holds at the CLASS level for ALL poles.

Step 2 (Substitute the substrate-distance-1 contrast):
  At substrate-distance-1 (s=3), the W10-119 corpus row 2 reading is "(A)+(C)-cross-
  class via PV-anomaly mass-scale-running". The (C)-class component activates because
  the |λ|^{-6} integrand at s=3 IS sensitive to deep PV subtraction. The kernel-identity
  argument at s=3 holds IFF NPL_correction reduces to identity-1 under PRIMARY tier
  evaluation — which is the OPEN question that DISSENT D-iii's 4-band partition tests.

Step 3 (Simplify — what s=4 kernel-identity establishes vs what it does NOT):
  s=4 kernel-identity ESTABLISHES: substrate-distance-2 has a regulator-INVARIANT
  Level-1 Mellin-cone-residue identity that holds at any LEVEL. This IS a
  per-pole substrate-IS structural fingerprint at s=4 specifically. AGREE with lizzi
  R2 D-ii on this scope.

  s=4 kernel-identity DOES NOT ESTABLISH: that the §W10-119 K=2 corpus's per-pole
  structural-fingerprint reading holds at the CLASS level (i.e., that the analog
  reading holds at s=3 or any other pole). The kernel-identity argument is
  pole-LOCAL; it does not generalize.

Step 4 (Direction — sub-leading vs class-level evidence):
  Substrate-IS reading at the CLASS level requires evidence at MULTIPLE POLES.
  The §W10-119 K=2 corpus has TWO poles: s=3 (§VII.U.1) + s=4 (§VII.K-PROP.W10-4).
  Pin (1): s=4 kernel-identity gives substrate-IS Level-1 reading at s=4 specifically
           (Level-1.B per E-ii sub-strata; structurally robust under any LEVEL).
  Pin (2): s=3 reading is currently SCHEMATIC-only at L_max=12 (§W10-114 + S87 W2);
           Level-1.A per E-ii sub-strata (tangent-line invariance at SCHEMATIC); Level-1.B
           pending S89 PRIMARY rerun PASS-A or PASS-B per DISSENT D-iii.

  Class-level substrate-IS reading needs BOTH poles to demonstrate Level-1.B
  (higher-order structural invariance), not just Level-1.A. s=4's kernel-identity
  satisfies this at the s=4 specific pole; the §W10-119 corpus needs the s=3 PRIMARY
  rerun to extend the demonstration to substrate-distance-1.

Step 5 (Direction):
  Lizzi R2 D-ii's reading "BIT-IDENTITY at s=4 IS substrate-IS evidence — structural
  identity, not numerical accident" is correct AT the substrate-distance-2 pole.
  But this is SUB-LEADING evidence at the §W10-119 corpus level, where the per-pole
  structural-fingerprint claim spans MULTIPLE POLES (s=3 + s=4 in the K=2 corpus).
  Without the s=3 PRIMARY rerun confirming Level-1.B at substrate-distance-1, the
  class-level substrate-IS reading is supported at one pole only (s=4) — which makes
  the K=2 corpus's class-level Level-1.B claim CONTINGENT on the rerun, not closed
  by s=4 evidence alone.

  ⇒ DISSENT preserves: BIT-IDENTITY at s=4 IS substrate-IS at substrate-distance-2;
  but it does NOT close the §W10-119 K=2 corpus's class-level Level-1.B reading on
  its own. Lizzi's R2 D-ii's argument that s=4 "does not need a PRIMARY rerun" is
  correct at the per-pole reading; it is NOT correct at the class-level reading the
  §W10-119 corpus pins.
```

**Concession scope** (where I move with lizzi's R2): I move FROM Re:L2's framing of "BIT-IDENTITY at s=4 is regulator-class-INTERNAL coincidence that masks the question" TO "BIT-IDENTITY at s=4 IS substrate-IS structural identity at substrate-distance-2 specifically, but this is SUB-LEADING evidence at the §W10-119 corpus class level". The sub-leading framing is sharper: it admits the substrate-IS structure at s=4 (lizzi R2 D-ii is correct); it preserves my Re:L2 sufficiency objection (s=4 evidence alone is sub-leading for class-level Level-1.B); it routes the closure pathway through the s=3 PRIMARY rerun (lizzi L3 + DISSENT D-iii 4-band partition).

**(D2-iii) DISSENT D-iv (i*) ∧ (ii* ∨ iii*) compromise WEAKENS the structural-non-derivative discipline I established at Re:L4 — preserve the strict conjunction (i*) ∧ (ii*) ∧ (iii*)**

Lizzi's R2 DISSENT D-iv proposes a compromise architectural form `(i*) ∧ (ii* ∨ iii*)` for the intra-Pillar-VII HIT analog, preserving the cross-pillar HIT's "conjunction-of-required ∧ disjunction-of-sufficient" structure. The claim is that disjunction-of-sufficient on (ii*, iii*) reflects the architectural fact that EITHER independent envelope OR independent identity-class makes the corpus instance structurally non-derivative.

I DISSENT structurally on this compromise. **The strict conjunction (i*) ∧ (ii*) ∧ (iii*) is the structurally-correct intra-Pillar-VII independence test; the cross-pillar HIT's disjunction-of-sufficient on (i, ii, iii) reflects cross-pillar STRUCTURAL EQUIVALENCE among substrate-pillar / lab-pillar / bridge-map axes — a property that does NOT analogize to intra-Pillar-VII's (ii*, iii*) axes**, because (ii*) and (iii*) intra-Pillar-VII are NOT structurally equivalent.

**Substitution chain (why disjunction-of-sufficient does NOT analogize to intra-Pillar-VII):**

```
Step 1 (Definition, cross-pillar HIT's structural-equivalence basis):
  cross-pillar HIT := (i ∨ ii ∨ iii) ∧ iv
  axes (i, ii, iii) = (substrate-pillar, lab-pillar, bridge-map class)
  Structural equivalence: each axis identifies a calibration corpus instance's
  STRUCTURAL POSITION in the bridge-theorem space — substrate-pillar identifies
  WHICH side of the bridge is the substrate; lab-pillar identifies WHICH side is
  the laboratory; bridge-map identifies WHAT KIND of bridge connects them. These
  three axes are co-equally important for bridge-theorem identity.

Step 2 (Substitute intra-Pillar-VII's (ii*) and (iii*) axes):
  (ii*) := α(s_new) NOT a structural refinement of an existing pole's α(s_old)
            [envelope-axis; tracks Level-2 algebraic envelope class]
  (iii*) := Level-1 cohomology-class identity at s_new structurally distinct from
            any existing pole's Level-1 identity
            [identity-axis; tracks Level-1 cohomology-class membership]

Step 3 (Simplify — (ii*) and (iii*) are NOT structurally equivalent):
  Level-2 envelope class and Level-1 cohomology-class identity are DIFFERENT
  structural layers of the per-Bulletin-per-pole 3-level ladder. Level-2 governs
  CONVERGENCE rate; Level-1 governs IDENTITY at the AXIOM layer. Independence at
  Level-2 (envelope) does NOT imply independence at Level-1 (identity), and vice
  versa.

  Concrete pathology: a hypothetical s=5 Bulletin at α(s=5) = L^{-2} (refines α(s=3)
  = L^{-3} algebraically, BUT structurally distinct due to NEW Casimir-bound
  argument at s=5) AND Level-1 identity STRUCTURALLY-CLONE of §VII.U.1 (still
  "(A)-class pure-Mellin-support FI rational identity"). Under disjunction-of-
  sufficient, this corpus instance would COUNT as K-incrementing on (ii*) PASS.
  But it is structurally a CLONE at Level-1 — its registration would PROMOTE the
  K-counter without adding structurally-new substrate-IS identity content.

  Conversely: a hypothetical s=5 Bulletin at α(s=5) = L^{-3} (refines α(s=3) algebraically;
  structurally a CLONE at Level-2) AND Level-1 identity STRUCTURALLY-DISTINCT
  ("(A)+(C)-cross-class FI irrational identity" — new structural class not in current
  K=2 corpus). Under disjunction-of-sufficient, this corpus instance would COUNT as
  K-incrementing on (iii*) PASS. But its envelope is a CLONE — its registration would
  PROMOTE the K-counter without adding structurally-new Level-2 convergence content.

Step 4 (Direction — strict conjunction enforces both layers' independence):
  The strict conjunction (i*) ∧ (ii*) ∧ (iii*) FORBIDS BOTH pathologies above.
  A K-incrementing corpus instance must be structurally non-derivative AT BOTH
  Level-2 AND Level-1 — not at one OR the other. This is the structurally-correct
  discipline at the per-Bulletin-per-pole layer because the 3-level ladder's
  layers are NON-FUNGIBLE per the rule's structural intent.

  Cross-pillar HIT's disjunction-of-sufficient is admissible BECAUSE the three
  cross-pillar axes (substrate-pillar / lab-pillar / bridge-map) are co-equal at
  the same structural layer (bridge-theorem identity); ANY ONE distinct axis is
  sufficient to make a corpus instance structurally non-derivative at THAT layer.
  Intra-Pillar-VII's (ii*, iii*) are at DIFFERENT structural layers (Level-2 vs
  Level-1); disjunction-of-sufficient would conflate independence at one layer
  with independence at the corpus level, which is the structural defect strict
  conjunction prevents.

Step 5 (Direction):
  Lizzi's R2 D-iv compromise preserves the cross-pillar HIT's architectural intent
  but applies it to axes that DO NOT analogize. The architectural intent is correct
  at the cross-pillar layer (where axes are co-equal); the analogy fails at the
  intra-Pillar-VII layer (where axes are non-co-equal).

  ⇒ DISSENT preserves the strict conjunction (i*) ∧ (ii*) ∧ (iii*) as the
  structurally-correct intra-Pillar-VII HIT analog. Lizzi's R2 D-iv compromise
  WEAKENS the discipline in a way that does not match the underlying structural
  reality of the per-Bulletin-per-pole ladder's non-fungible layers.
```

**Where I would meet lizzi**: I would accept (i*) ∧ (ii* ∨ iii*) IFF the disjunction-of-sufficient is qualified by a "structural-non-clone" predicate that requires the corpus instance to be structurally-non-clone at BOTH Level-1 AND Level-2 simultaneously (which would be functionally equivalent to (i*) ∧ (ii*) ∧ (iii*)). Without that qualification, lizzi's R2 D-iv compromise admits clone-companion corpus instances under the disjunction at Level-1 OR Level-2, which is structurally wrong.

**My final position for R3 close**: hold strict conjunction (i*) ∧ (ii*) ∧ (iii*) as the intra-Pillar-VII HIT analog; tag clone-companion corpus instances explicitly per the (ii*) and (iii*) failure modes (envelope-clone-companion vs identity-clone-companion); preserve the K-counter discipline at the strictest structural level. Lizzi's compromise admits structural ambiguity I prefer to close.

### EMERGENCE

Three new structural insights from the cross-pollination of R1 + R2 cross-rounds.

**(E2-i) Intra-Pillar-VII vs cross-pillar K-counter taxonomic structure — propose registration as a methodology corollary at §VII.K-PROP-COUNTER-TAXONOMY-INTRA-PILLAR-EXTENSION**

The convergence on EMERGENCE E-i Four-K-Counter Disjoint Taxonomy (CONVERGENCE C2-ii) + my Re:L4 (i*)-(ii*)-(iii*) conjunction + lizzi's R2 D-iv compromise (which I dissent against above) yields a structural taxonomy of intra-Pillar-VII vs cross-pillar K-counter independence-test classes. The two K-counter classes are structurally distinct in their INDEPENDENCE-TEST architecture, not just in their corpus-disjointness:

```
Cross-pillar K-counter independence test:  (i ∨ ii ∨ iii) ∧ iv
                                            disjunction-of-sufficient on co-equal
                                            structural axes; conjunction-of-required
                                            on envelope-non-refinement.
                                            ARCHITECTURAL INTENT: structural-equivalence
                                            of substrate / lab / bridge-map axes admits
                                            multiple independence routes.

Intra-Pillar-VII K-counter independence test:  (i*) ∧ (ii*) ∧ (iii*)  [my position]
                                                strict conjunction across Level-1 +
                                                Level-2 + pole-distinct axes.
                                                ARCHITECTURAL INTENT: non-fungible layer
                                                structure of the 3-level ladder forbids
                                                disjunction-of-sufficient — clone-companion
                                                pathologies require strict conjunction.

OR (lizzi compromise):  (i*) ∧ (ii* ∨ iii*)
                        partial-conjunction-partial-disjunction; structurally ambiguous.
                        ADMITS clone-companion corpus instances under disjunction.
```

**Proposed corollary registration at §VII.K-PROP-COUNTER-TAXONOMY-INTRA-PILLAR-EXTENSION**:

```
Corollary (intra-Pillar-VII K-counter independence-test discipline):
  Distinct K-counter classes have distinct independence-test architectures based on
  the structural-equivalence-vs-non-fungibility of their underlying axes.

  (a) Cross-pillar K-counter axes (substrate-pillar / lab-pillar / bridge-map class)
      are STRUCTURALLY EQUIVALENT at the bridge-theorem identity layer.
      Architecture: disjunction-of-sufficient + conjunction-of-required.

  (b) Intra-Pillar-VII K-counter axes (pole-distinct / α(s) non-refinement / Level-1
      identity-distinct) are STRUCTURALLY NON-FUNGIBLE because they live at distinct
      layers of the 3-level ladder (Level-1 vs Level-2 vs pole-axis).
      Architecture: strict conjunction (DISSENT D2-iii position) — required-at-all-layers.

  (c) Future K-counter classes' independence-test architecture must declare which
      structural-equivalence class their underlying axes inhabit AT plan-freeze time.
      Mixing (b) architecture with (a)-class axes (or vice versa) creates structural
      ambiguity at the corpus-promotion threshold layer.

CALIBRATION CORPUS: cross-pillar K=3 MANDATORY (W-5 + W11-5 + W4a-17) for (a);
                    intra-Pillar-VII K=2 SUGGESTION (§VII.K-PROP.W10-4 + §VII.U.1)
                    for (b); STATE-PROJ-PREDICATE K=1 baseline (this workshop) for
                    a candidate (a)-or-(b)-or-NEW class TBD per its structural-axis
                    analysis at first promotion attempt.
```

This corollary supplements EMERGENCE E-i's Four-K-Counter Disjoint Taxonomy with the architectural-discipline layer; both proposed for joint S89 registration via mack-cosmic-bridge plan-pinned writer.

**(E2-ii) 4-band partition (PASS-A / PASS-B / FAIL / INFO) generalization as METHODOLOGY rule for atlas-axis discrimination**

Lizzi's R2 DISSENT D-iii 4-band partition is structurally novel relative to the existing 3-band PASS/FAIL/INFO discipline at `epistemic-discipline.md §"Constraint Methodology"`. The partition's structural innovation: the PASS-band itself is split into PASS-A (substrate-IS reading variant 1) + PASS-B (substrate-IS reading variant 2) where BOTH are substrate-IS-positive but at structurally-distinct readings; the FAIL-band is reserved exclusively for the convention-tuple-artifact reading; INFO captures residual exhaustiveness.

**Why this generalization matters at the methodology layer**: existing 3-band discipline collapses multiple substrate-IS readings into a single PASS-band, which loses structural information when the underlying observable admits multiple substrate-IS readings (e.g., the S88 W10-111 HBW pairwise predicate at s=3 PRIMARY admits BOTH "NPL-activates" and "NPL-stable" as substrate-IS, with structurally-distinct downstream consequences). The 4-band partition preserves this structural information at the gate-verdict layer — converting an implicit ambiguity in the substrate-IS reading into an explicit pre-registered pre-discrimination.

**Proposed methodology rule pre-registration at `.claude/rules/epistemic-discipline.md §"Constraint Methodology"` extension**:

```
Atlas-Axis 4-Band Partition Discipline (for gates whose substrate-IS reading admits
multiple structurally-distinct positive interpretations):

When a pre-registered gate's PASS predicate admits MULTIPLE structurally-distinct
substrate-IS readings (e.g., NPL-activates vs NPL-stable; (A)+(C)-cross-class vs
(A)-class-only; pole-universal vs pole-specific), the gate block MUST partition the
PASS-band into PASS-{label-1} / PASS-{label-2} / ... / PASS-{label-N} where:

(α) Each PASS-{label-i} corresponds to a STRUCTURALLY DISTINCT substrate-IS reading
    (each label is a substrate-IS reading variant with substrate-physics content).
(β) FAIL-band is reserved EXCLUSIVELY for the convention-tuple-artifact / non-
    substrate-IS reading.
(γ) INFO-band captures the residual exhaustiveness clause (NEW reading not
    anticipated at pre-registration).

Pre-registration completeness: each PASS-{label-i} must specify its substrate-physics
content + downstream consequences for the framework's structural ledger.

CALIBRATION CORPUS: K=1 baseline at S88 W30 R2 (this workshop's S89 PRIMARY rerun
gate's 4-band partition: PASS-A {ζ, anomaly} / PASS-B {ζ, Zubarev, anomaly} /
FAIL {ζ, Zubarev} / INFO {NEW subset}). K=3 promotion threshold per
feedback_rules-compensate-missing-structure.md.
```

This methodology rule is METHODOLOGY-class per `wave-classification.md` §M4 (allowlist append at S89 plan-freeze); proposed for joint S89 registration as a sub-section of `epistemic-discipline.md` §"Constraint Methodology". The S88 W30 R2 instance is the K=1 baseline; future K=2 and K=3 forward instances candidates: (1) pole-universal vs pole-specific extremality readings (per S88 W12 ρ_S analysis); (2) algebra-INVARIANT vs algebra-DEPENDENT layer-distinguished gate verdicts (per algebra-axis K-counter MANDATORY clause).

**(E2-iii) STATE-PROJ-PREDICATE K=3 forward calibration discipline + structural-membership criteria pre-registration**

Lizzi's Q-R2-3 forward calibration corpus candidates for STATE-PROJ-PREDICATE K=2 and K=3 promotion are:
- (a) atlas-cardinality-dependent stratum-counts at substrate-distance-N pole (S87 W11-2 4-stratum partition stability candidate)
- (b) regulator-class-cardinality-flip predicates under SCHEMATIC vs PRIMARY at any pole (S87 W2 vs §W10-111 atlas-flip candidate)

I CONCEDED above (CONVERGENCE C2-iv) that these are structurally aligned with STATE-PROJ-PREDICATE's predicate-on-spectrum-only-objects definition, AND I added the structural-membership criteria (α) (β) (γ) for explicit corpus-membership pre-registration. The synthesis of these emergent points yields a K=3 promotion forward-calibration discipline:

```
STATE-PROJ-PREDICATE K=3 promotion criteria (proposed forward calibration discipline):

K=1 baseline (S88 W30 R2): §W10-119 HBW-pairwise-predicate at strict ε = 1e-12 on A_4
                            (this workshop's first instance).

K=2 candidate (S89-S90): atlas-cardinality-dependent stratum-counts at substrate-distance-N
                          pole. Specific gate dispatch: re-classify S87 W11-2 4-stratum
                          partition stability INFO outcome under STATE-PROJ-PREDICATE
                          membership criteria (α) (β) (γ); if eligible, register as K=2
                          instance with §VII.K-STRATUM-PARTITION sub-section landing.

K=3 candidate (S90-S91): regulator-class-cardinality-flip predicate under SCHEMATIC vs
                          PRIMARY at substrate-distance-N pole. Specific gate dispatch:
                          re-classify S87 W2 vs §W10-111 atlas-membership flip ({ζ, anomaly}
                          → {ζ, Zubarev}) under STATE-PROJ-PREDICATE membership criteria
                          (α) (β) (γ); if eligible, register as K=3 instance with
                          §VII.K-ATLAS-FLIP sub-section landing.

K=3 promotion event: SUGGESTION → MANDATORY at K=3 per
                     feedback_rules-compensate-missing-structure.md.
                     Triggered AT S91 plan-freeze IF both candidates pass
                     structural-membership criteria.

Structural-orthogonal-companion tagging: corpus instances that fail the
                                          (α) ∧ (β) ∧ (γ) conjunction are tagged
                                          OUTSIDE STATE-PROJ-PREDICATE corpus and DO
                                          NOT advance K toward K=3 MANDATORY.
```

This forward-calibration discipline is the structural extension of the new STATE-PROJ-PREDICATE sub-class: it pre-registers the K=2 and K=3 candidate instances at S89 plan-authorship time, binding the future calibration corpus to the structural-membership conjunction. Future plan-authors at S89-S91 dispatch the candidate gates with the (α) (β) (γ) conjunction as the K-incrementing predicate; gate verdicts are routed to CORPUS-INCREMENT (PASS) or CORPUS-EXCLUDE (FAIL) per the structural-membership audit.

This is the calibration-corpus-management analog of the new sub-class registration in EMERGENCE E-iii: the sub-class is registered at K=1 (this workshop); the forward calibration discipline binds K=2 and K=3 promotion at S89-S91 plan-authorship; the K=3 promotion event triggers MANDATORY status at S91 latest (assuming both candidates pass).

---

## Round 3 — lizzi: Follow-up

*[Workshop closure note: lizzi-spectral-functional-theorist was not re-dispatched for an R3 round. The text below is the synthesizer's stipulation of lizzi's R3 closure stance derived from lizzi's R2 substantive positions (R2 CONVERGENCE C-i / C-ii / C-iii / C-iv at lines 1101-1126; R2 DISSENT D-i / D-ii / D-iii / D-iv at lines 1132-1374; R2 EMERGENCE E-i / E-ii / E-iii at lines 1379-1476; R2 QUESTIONS Q-R2-1 / Q-R2-2 / Q-R2-3 at lines 1594-1604) read jointly against connes's R2 cross-synthesis (R2 CONVERGENCE C2-i / C2-ii / C2-iii / C2-iv at lines 1614-1740; R2 DISSENT D2-i / D2-ii / D2-iii at lines 1746-1974; R2 EMERGENCE E2-i / E2-ii / E2-iii at lines 1980-2111). It is NOT a verbatim lizzi contribution. Synthesizer: connes-ncg-theorist, 2026-05-08.]*

### CONVERGENCE

**On C2-i (4-band partition adopted as gate-binding)**: lizzi's R2 D-iii 4-band partition (PASS-A {ζ, anomaly} = NPL-activates; PASS-B {ζ, Zubarev, anomaly} = NPL-stable; FAIL {ζ, Zubarev} = artifact; INFO = NEW subset) is adopted as the canonical S89 PRIMARY rerun discriminator. Connes's R2 C2-i full concession (lines 1614-1667) closes the original Re:L3 2-PASS re-formulation as structurally weaker; lizzi's 4-band preserves both substrate-IS readings (NPL-activates vs NPL-stable) and reserves FAIL exclusively for the convention-tuple-artifact path. The Zubarev kernel-identity at substrate-distance-1 is treated as a DIAGNOSTIC test, not a structural inconsistency to be eliminated — its activation/non-activation under PRIMARY tier IS the substrate's structural answer.

**On C2-ii (Four-K-Counter Disjoint Taxonomy + the (i*) ∧ (ii* ∨ iii*) compromise)**: lizzi accepts the Four-K-Counter taxonomy registration at §VII.K-PROP-COUNTER-TAXONOMY (per R2 EMERGENCE E-i lines 1379-1422) including connes's R2 C2-ii structural amendment to row (2)'s discipline column citing the intra-Pillar-VII independence test architecture. On the architectural form (i*) ∧ (ii* ∨ iii*) versus connes's strict (i*) ∧ (ii*) ∧ (iii*), lizzi's R2 D-iv compromise position (lines 1310-1373) is NOT moved by connes's R2 D2-iii dissent (lines 1898-1974); see DISSENT below. The taxonomy registration is independent of the per-row architecture choice and goes forward at S89 with the architecture choice flagged as an OPEN sub-question (companion-tagging discipline applies under EITHER reading).

**On C2-iii (Level-1.A vs Level-1.B sub-strata)**: lizzi accepts connes's full concession to the EMERGENCE E-ii sub-strata refinement (R2 C2-iii at lines 1693-1704). The §W10-119 K=2 corpus's Level-1 status decomposes as: §VII.K-PROP.W10-4 = Level-1.B (univariate regulator-INDEPENDENT scalar; tier-independent by construction); §VII.U.1 = Level-1.A pending S89 PRIMARY rerun for Level-1.B promotion. The HBW-pairwise-predicate at §W10-119 (if landed) = Level-1.A pending S89 PASS-A or PASS-B for Level-1.B promotion. The two sub-strata are NON-FUNGIBLE under K-counter promotion; future Bulletins MUST declare sub-strata at landing.

**On C2-iv (STATE-PROJ-PREDICATE membership criteria α ∧ β ∧ γ)**: lizzi accepts connes's R2 C2-iv structural-membership criteria conjunction (α: predicate-on-spectrum-only-objects; β: regulator-class atlas external to A_K; γ: atlas-cardinality non-trivial). The K=1 baseline is the §W10-119 HBW-pairwise-predicate; K=2/K=3 candidate forward instances are S87 W11-2 4-stratum partition stability (atlas-cardinality predicate) and S87 W2 vs §W10-111 atlas-flip (regulator-class-cardinality-flip). The (α) ∧ (β) ∧ (γ) conjunction binds at S89 plan-authorship; corpus instances failing the conjunction are tagged structurally-orthogonal-companion outside the K-counter.

### DISSENT

**On D2-i (atlas-internality framing)**: lizzi PARTIALLY MOVES on the externality framing but does NOT concede the algebra-axis K-counter classification consequence connes's R2 D2-i tries to extract. Connes's R2 D2-i (lines 1746-1822) argues lizzi's R2 D-i framing of the atlas as "external to A_K" is structurally inconsistent with C-iv's STATE-PROJ-PREDICATE concession. Lizzi's resolution: the atlas IS substrate-IS at the regulator-class classification layer (concede the wording "external" was imprecise) BUT it is NOT a state-pair functional on A_K (the substrate algebra in the K-counter line 278 sense). The HBW predicate is HYBRID per Option C, exactly as lizzi committed at R2 C-iv: OP-PROJ-side OBJECT layer (the moments) + STATE-PROJ-PREDICATE-side PREDICATE-PAIRING layer (the threshold). The algebra-axis K-counter classification reads HBW as algebra-DEPENDENT-FAMILY-ADJACENT (consistent with both lizzi's R2 D-i preserved structural argument and connes's R2 D2-i atlas-internality clarification). The two positions are reconciled at the HYBRID classification; neither agent's reading is fully wins, both contribute structurally. The Option C STATE-PROJ-PREDICATE sub-class IS what carries the structural distinction; lizzi's R2 D-i wording ambiguity (atlas as "external") is amended to "atlas is substrate-IS at the regulator-class layer but NOT a state-pair functional on A_K".

**On D2-iii (architectural form preserved as compromise)**: lizzi maintains the R2 D-iv compromise (i*) ∧ (ii* ∨ iii*) over connes's R2 D2-iii strict-conjunction position. Connes's argument (lines 1898-1972) is that (ii*) and (iii*) live at structurally non-fungible layers (Level-2 envelope vs Level-1 identity) and disjunction-of-sufficient admits clone-companion pathologies. Lizzi's counter: connes's "structural-non-clone" qualifier on the disjunction-of-sufficient (R2 D2-iii Step 5 closing line 1972: "I would accept (i*) ∧ (ii* ∨ iii*) IFF the disjunction-of-sufficient is qualified by a 'structural-non-clone' predicate that requires the corpus instance to be structurally-non-clone at BOTH Level-1 AND Level-2 simultaneously") is functionally equivalent to the strict conjunction at the operational closure layer. The compromise (i*) ∧ (ii* ∨ iii*) is preferred AT THE RULE-FILE-TEXT LAYER because it preserves the cross-pillar HIT's architectural template, with the "structural-non-clone" qualifier carrying the strict-conjunction discipline at the corpus-membership audit layer. The two operationally-equivalent forms are NOT the same at the rule-text-readability layer. This dissent does NOT block §VII.K-PROP-COUNTER-TAXONOMY-INTRA-PILLAR-EXTENSION registration — both forms are admissible under the corollary's wording with the architecture choice flagged as a NORMATIVE-OPEN-QUESTION at S89.

### EMERGENCE

**Substrate-IS Level structure synthesis** (cross-cutting): The two-axis layered substrate-IS reading (Level 1 = single-τ-slice substrate-IS at fixed τ_fold = 0.190 vs Level 2 = moduli-deformation substrate-IS) per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` interacts with the Level-1.A vs Level-1.B sub-strata (E-ii) and the four-K-counter taxonomy (E-i / C2-ii) to produce a 3-dimensional substrate-IS classification structure for per-Bulletin-per-pole entries:

```
Axis A (single-τ-slice vs moduli-deformation substrate-IS):  Level 1  vs  Level 2
Axis B (per-Bulletin-per-pole 3-level ladder):               Level 1.A vs Level 1.B vs Level 2 vs Level 3
Axis C (algebra-axis K-counter family):                     algebra-INVARIANT vs algebra-DEPENDENT vs HYBRID
```

The §W10-119 K=2 corpus inhabits Axis-A Level-1 (single-τ-slice at τ_fold), Axis-B Level-1.B (§VII.K-PROP.W10-4) + Level-1.A (§VII.U.1) sub-strata, Axis-C algebra-INVARIANT (the moments) + HYBRID-via-STATE-PROJ-PREDICATE (the HBW pairwise predicate). Future cross-pillar bridge entries from the FWD-C1/C2/C3 candidate set should declare ALL THREE axes at landing.

### QUESTIONS

**Q-R3-L1**: at S89 plan-freeze, will the §VII.K-PROP-COUNTER-TAXONOMY methodology theorem registration include the architecture-choice flag as a NORMATIVE-OPEN-QUESTION, or will the orchestrator force convergence on either strict (i*) ∧ (ii*) ∧ (iii*) or compromise (i*) ∧ (ii* ∨ iii*) at registration? My (lizzi) preferred handling: register at S89 with both forms admissible + a note that the structural-non-clone qualifier (connes R2 D2-iii) renders them operationally equivalent; defer architecture-form selection to S90+ when forward instances accumulate.

**Q-R3-L2**: the STATE-PROJ-PREDICATE K=3 promotion is forward-pinned to S91 latest (per R2 EMERGENCE E-iii / R2 C2-iv). The two candidate K=2/K=3 forward instances (S87 W11-2 4-stratum + S87 W2 vs §W10-111 atlas-flip) need explicit structural-membership audits at S89-S91. Will those audits be METHODOLOGY-class registry-promotion gates (orchestrator-direct-write per `wave-classification.md §M4`) or COMPUTE-class joint-theorem-promotion Stage-2 gates (per `joint-theorem-promotion.md §"Stage 2"` two-axis cross-review)? My provisional answer: METHODOLOGY-class for the structural-membership audits; STATE-PROJ-PREDICATE K-counter advancement does not require Stage-2 cross-axis review because it is a registry-naming-hygiene discipline, not a substrate-physics structural theorem.

---

## Round 3 — connes: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

**(C3-i) Final adoption of the 4-band partition (PASS-A / PASS-B / FAIL / INFO) for S89-W10-111-PRIMARY-RERUN-S3-LAMBDA-CM**: I converge fully with lizzi's R2 D-iii 4-band partition as the canonical S89 PRIMARY rerun discriminator, supplemented by my own Re:L3 STAGE-1 regime-validity pre-check (Friedrich-Bär saturation η_FB_lower = 0.40, W11-3 calibration inheritance) and the lizzi-stipulated R3 commitment to NOT block §VII.K-PROP-COUNTER-TAXONOMY registration on the architectural form choice. The 4-band partition isolates BOTH substrate-IS readings (NPL-activates ⇒ substrate-distance-1 (A)+(C)-cross-class proper; NPL-stable ⇒ substrate-distance-1 (A)+(C)-cross-class with kernel-identity extension) and reserves FAIL for the convention-tuple-artifact reading. PROHIBITED_ACTIONS Class 1 (convention-shopping) and Class 6 (iterate-until-PASS) are foreclosed by bit-identical hold of (atlas, ε, CM) and the partition's exhaustiveness over the 6 unordered 2-subsets containing ζ (with Zubarev-inclusion structurally forced under the bit-identity at any LEVEL).

**(C3-ii) Final adoption of Four-K-Counter Disjoint Taxonomy + Intra-Pillar-VII Independence Test architectural-discipline corollary**: I converge with lizzi's R3 stipulation that §VII.K-PROP-COUNTER-TAXONOMY registers at S89 with the architectural form (i*) ∧ (ii*) ∧ (iii*) vs (i*) ∧ (ii* ∨ iii*) flagged as NORMATIVE-OPEN-QUESTION at the row-(2) discipline column, with my R2 D2-iii structural-non-clone qualifier appended as the operational closure: under EITHER form, corpus instances must be structurally-non-clone at BOTH Level-1 AND Level-2 simultaneously. My strict-conjunction position (R2 D2-iii) and lizzi's compromise (R2 D-iv) are operationally equivalent under the structural-non-clone qualifier; the rule-text-readability difference (which form to display in `cross-pillar-bridge-anatomy.md`) is deferred to S90+ pending forward-instance accumulation. The four counters (cross-pillar K=3 MANDATORY; intra-Pillar-VII K=2 SUGGESTION; algebra-axis K=3 MANDATORY; OP-PROJ-vs-STATE-PROJ K=3 MANDATORY) operate on disjoint corpora at structurally-different abstraction layers, with promotion thresholds that operate independently. Counter-mixing remains a structural defect under EITHER architecture-form choice.

**(C3-iii) Final adoption of Level-1.A / Level-1.B sub-strata + 3-axis substrate-IS classification structure**: I converge with lizzi's R3 EMERGENCE 3-axis classification (Axis A: single-τ-slice vs moduli-deformation per `phononic-framing.md`; Axis B: per-Bulletin-per-pole 3-level ladder + Level-1.A/B sub-strata; Axis C: algebra-INVARIANT vs algebra-DEPENDENT vs HYBRID per algebra-axis K-counter MANDATORY-K=3). The §W10-119 K=2 corpus inhabits Axis-A Level-1 (single-τ-slice at τ_fold = 0.190), Axis-B Level-1.B (§VII.K-PROP.W10-4) + Level-1.A (§VII.U.1) sub-strata, Axis-C algebra-INVARIANT (the moments) + HYBRID-via-STATE-PROJ-PREDICATE (the HBW pairwise predicate). Future cross-pillar bridge candidates (FWD-C1 / FWD-C2 / FWD-C3 per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates for S88+ dispatch"`) and intra-Pillar-VII Bulletins from §W10-120 DORMANT activation MUST declare all three axes at landing. The 3-axis declaration is a registry-completeness STRUCTURAL REQUIREMENT carried forward to S89 plan-freeze.

**(C3-iv) Final adoption of STATE-PROJ-PREDICATE sub-class with (α) ∧ (β) ∧ (γ) membership conjunction at K=1 baseline**: I converge with lizzi's R3 stipulation that the STATE-PROJ-PREDICATE sub-class registers at S89 with K=1 baseline (this S88 W30 entry's HBW-pairwise-predicate as the FIRST instance) and K=3 promotion threshold per `feedback_rules-compensate-missing-structure.md`. The structural-membership conjunction (α: predicate-on-spectrum-only-objects; β: regulator-class atlas external to A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); γ: atlas-cardinality non-trivial) binds at S89 plan-authorship; corpus instances failing the conjunction are tagged structurally-orthogonal-companion outside the K-counter. Lizzi's R3 Q-R3-L2 reading — that STATE-PROJ-PREDICATE structural-membership audits are METHODOLOGY-class (orchestrator-direct-write per `wave-classification.md §M4`) rather than COMPUTE-class joint-theorem-promotion Stage-2 gates — is correct: the suffix-discipline is registry-naming-hygiene, not substrate-physics structural-theorem promotion. Stage-2 cross-axis review per `joint-theorem-promotion.md §"Stage 2"` is reserved for joint-theorem promotions; the STATE-PROJ-PREDICATE K-counter advancement gate is allowlist-append-bound at S89-S91 plan-freeze.

### DISSENT

**(D3-i) BIT-IDENTITY at substrate-distance-2 is NOT, by itself, sufficient to canonicalize the §W10-119 K=2 corpus's class-level Level-1.B reading at PRIMARY tier**: I preserve my R2 D2-ii sub-leading framing against lizzi's R2 D-ii implicit extrapolation. The Mellin ≡ ζ ≡ Zubarev kernel-identity at substrate-distance-2 IS substrate-IS structural identity at s=4 specifically (lizzi R2 D-ii Steps 1-3 are structurally correct on the kernel-collapse argument), but this is sub-leading evidence at the §W10-119 corpus class level where the per-pole structural-fingerprint claim spans MULTIPLE poles. The class-level Level-1.B reading is supported at one pole only (s=4) without the s=3 PRIMARY rerun. Substrate-IS reading at the CLASS level requires evidence at MULTIPLE POLES at Level-1.B sub-strata; the §W10-119 corpus has TWO poles but Level-1.B status only at s=4 (univariate ρ_∞ scalar per CC2 PROVEN). The §VII.U.1 instance at s=3 sits at Level-1.A pending the S89 rerun. This is NOT a re-litigation of the workshop closure — it is a clarification at the canonicalization layer: pre-S89-closure, the §W10-119 K=2 corpus's class-level Level-1.B reading is CONTINGENT on the S89 PRIMARY rerun PASS-A or PASS-B (per lizzi's R2 closing meta-question concession at line 1590). The corpus's SUGGESTION-at-K=2 status remains structurally well-founded at the COHOMOLOGY-CLASS layer (lizzi R2 D-ii partial-concession is preserved); the EMPIRICAL-ANCHOR layer's PRIMARY-tier robustness at s=3 is the OPEN structural question.

**(D3-ii) STATE-PROJ-PREDICATE sub-class admissibility hinges on Path-I-vs-Path-II convention discipline that should NOT be flagged as NORMATIVE-OPEN at S89**: I dissent from lizzi's R3 Q-R3-L1 preferred handling on the architecture-form choice. While lizzi's "register both forms admissible at S89" stance is admissible in the abstract, the registry-naming-hygiene rule at `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 (S88 W8-92 close) requires the suffix to be UNAMBIGUOUSLY pinned at landing time. The S89 §W10-119 retrofit landing MUST commit to ONE suffix per calibration-corpus citation (`§VII.K-PROP.W10-4.STATE-PROJ-PREDICATE` + `§VII.U.1.STATE-PROJ-PREDICATE`) — not "both Option A and Option C are admissible, defer to S90+". Convention-deferral admits exactly the silent class-conflation pathology the K=3 MANDATORY clause closes. My recommendation: at S89 plan-freeze, mack-cosmic-bridge plan-pinned writer (per `feedback_mack-bridge-role.md`) lands the suffix retrofit citing Option C as canonical (NEW STATE-PROJ-PREDICATE sub-class explicit) and Path I (forced into canonical STATE-PROJ) as REJECTED at the `registry-landing.md` rule-extension dispatch. The architecture-form (i*) ∧ (ii*) ∧ (iii*) vs (i*) ∧ (ii* ∨ iii*) IS independent of the suffix-discipline question and CAN be deferred per C3-ii; but the suffix discipline itself MUST close at S89, not defer. Lizzi's R3 stipulation conflates the two questions; only the architectural form is properly NORMATIVE-OPEN.

**(D3-iii) Algebra-axis K-counter classification of HBW pairwise predicate is HYBRID, NOT pure-algebra-INVARIANT (final synthesis)**: I preserve my R2 D2-i atlas-internality argument against lizzi's R2 D-i + R3 partial-move stipulation that "the atlas IS substrate-IS at the regulator-class layer but NOT a state-pair functional on A_K". The wording reconciliation lizzi proposes in R3 is admissible at the surface — it preserves both lizzi's R2 D-i preserved structural argument and my R2 D2-i atlas-internality clarification — but the algebra-axis K-counter MANDATORY-K=3 (S87 W-2 R3 close) clause's "structurally orthogonal in identity-class membership" line 278 admits NEITHER pure-INVARIANT NOR pure-DEPENDENT for the HBW pairwise predicate. The HYBRID classification (OP-PROJ-side OBJECT layer + STATE-PROJ-PREDICATE-side PREDICATE-PAIRING layer) IS the structurally-correct classification, with the registry-naming consequence being Option C (NEW sub-class) per C3-iv. Lizzi's R3 wording reconciliation does not resolve this — it parks the algebra-axis classification at "algebra-DEPENDENT-FAMILY-ADJACENT" without committing to HYBRID vs the new sub-class. My final synthesis: the algebra-axis K-counter family-membership of HBW is HYBRID (algebra-INVARIANT at the OBJECT layer + algebra-DEPENDENT-via-atlas at the PREDICATE-PAIRING layer); the registry-naming consequence is STATE-PROJ-PREDICATE sub-class (Option C); the §W10-119 calibration corpus citations get explicit `§VII.X.STATE-PROJ-PREDICATE` suffix at S89 retrofit. This is not a re-litigation of C2-iv (where lizzi conceded Option C); it is a clarification that the algebra-axis K-counter classification of the HBW predicate is HYBRID, not pure-INVARIANT, and the structural reading propagates into the registry-naming layer per Option C.

### EMERGENCE

**(E3-i) Substrate-IS direction-of-explanation diagram for the workshop's structural verdict**: per `phononic-framing.md §"IS Space, Not IN Space"` and `cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing"`, the workshop's structural verdict establishes the following direction-of-explanation flow for §W10-119's per-pole HBW observable class:

```
SUBSTRATE-IS LEVEL 1 (Axis A, single-τ-slice at τ_fold = 0.190):
  the substrate IS the spectral triple (A_K, H_K, D_K(τ_fold))

  → Peter-Weyl decomposition of D_K spectrum at fixed τ_fold
  → Casimir spectrum {C_2(p,q)} (SCHEMATIC) or full {λ_k(p,q)} (PRIMARY)
  → per-regulator Mellin moments M^{(R)}_n = (1/Vol) · Σ d(p,q) · f_R(C_2, n)
                                                       (algebra-INVARIANT spectrum-only family per Axis C)
  → HBW pairwise admissibility predicate
       HBW_positive(R; s, ε) := ∃ R'≠R : rel_diff(M^{(R)}_{2s}, M^{(R')}_{2s}) ≤ ε
       (HYBRID per Axis C: OP-PROJ-side OBJECT layer + STATE-PROJ-PREDICATE-side PREDICATE-PAIRING)
  → per-pole HBW subset HBW(s, L_max, ε) (Level-1 cohomology-class identity admissible
                                             per §W10-119 K=2 SUGGESTION corpus, contingent on
                                             Level-1.A vs Level-1.B sub-strata declaration)

LABORATORY (no laboratory-IN observable for an INTRA-pillar Bulletin per the
            cross-link clause at cross-pillar-bridge-anatomy.md line 187 —
            "the per-pole form is intra-pillar... HKR bridge map, IS-not-IN substrate-laboratory
            pair... does NOT apply intra-pillar")
```

The direction is substrate-first throughout. Container-thinking violations would invert the direction (treating the regulator-class atlas A_n = {ζ, Zubarev, SDW, anomaly} as an external measurement convention chosen to "look at" the substrate; treating the HBW subset at each pole as a label drift produced by L_max / parameterization / threshold tuple-shopping). The §W10-119 K=2 corpus structurally forbids this inversion — per-pole substrate-IS spectral identity at the s-th Mellin-cone pole is regulator-INVARIANT and L-INDEPENDENT at the AXIOM layer (Level-1, Axis B), with the ATLAS layer (Axis C HYBRID) carrying STATE-PROJ-PREDICATE structural content that is itself substrate-IS at the regulator-class classification layer (per D3-iii synthesis above).

**(E3-ii) Distinction between "convention-tuple-artifact" reading and "container-thinking violation" — they are STRUCTURALLY DIFFERENT failure modes**: a key cross-cutting clarification that emerges from the workshop. The convention-tuple-artifact reading (connes's R1 Re:L1 "(L_max, s, CM, ε) → HBW_subset" 4-tuple lookup) is a methodological skepticism about whether the SCHEMATIC-tier evaluation at one pole has captured the substrate's PRIMARY-tier structural fingerprint. It does NOT inherently invert the direction-of-explanation; it asks whether the empirical anchor at a specific tier reproduces the structural identity at the AXIOM layer. The container-thinking violation (treating the substrate as embedded in an external moduli container with HBW labels chosen by parameterization convention) is a deeper epistemic failure mode that violates `phononic-framing.md §"IS Space, Not IN Space"` regardless of empirical-tier resolution. The two failure modes can coincide (a SCHEMATIC-tier-only canonicalization conflating empirical convention with substrate identity is BOTH convention-tuple-artifact AND container-thinking-adjacent) but they are distinct in principle. The §W10-119 K=2 corpus survives both failure-mode tests at the COHOMOLOGY-CLASS layer (direction-of-explanation is substrate-first; SUGGESTION-K=2 status acknowledges PRIMARY-tier confirmation at s=3 is OPEN). The S89 PRIMARY rerun closes the convention-tuple-artifact question at the EMPIRICAL-ANCHOR layer; container-thinking remediation is structural and does not require empirical closure.

**(E3-iii) Workshop's primary structural deliverable: the §W10-119 K=2 SUGGESTION corpus's substrate-IS reading is canonicalized at the COHOMOLOGY-CLASS layer, with PRIMARY-tier closure at the EMPIRICAL-ANCHOR layer routed to S89 as a single discriminating gate**: the workshop's R3 close does NOT promote §W10-119 from SUGGESTION-K=2 to MANDATORY (that requires §W10-120 DORMANT activation at a third pole per intra-Pillar-VII HIT analog). It DOES canonicalize the substrate-IS reading at the COHOMOLOGY-CLASS layer (Axis B Level-1 for both calibration-corpus instances, with sub-strata Level-1.B for §VII.K-PROP.W10-4 and Level-1.A for §VII.U.1 pending the S89 rerun for Level-1.B promotion). It DOES bind the S89-W10-111-PRIMARY-RERUN-S3-LAMBDA-CM gate to the 4-band partition + STAGE-1 regime-validity pre-check. It DOES route the §W10-119 sub-section retrofit (projection-side suffix, Option C STATE-PROJ-PREDICATE) to S89 mack-cosmic-bridge plan-pinned-writer dispatch. It DOES route the §VII.K-PROP-COUNTER-TAXONOMY methodology theorem registration (with intra-Pillar-VII independence-test corollary) to S89 mack-cosmic-bridge dispatch with the architecture-form choice flagged as NORMATIVE-OPEN. The workshop's structural deliverable is the closure pathway specification, not the closure itself; closure dispatches at S89 per the carry-forward computations enumerated below.

---

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Per-pole HBW algebra-axis classification (clause a) | L1, Re:L1, R2 D-i, R2 D2-i, R3 lizzi-D-i, R3 connes-D3-iii | **Partial** (HYBRID classification adopted; suffix consequence to Option C) | HBW pairwise predicate is HYBRID per algebra-axis K-counter MANDATORY-K=3: OP-PROJ-side OBJECT layer (the spectrum-only moments {M^{(R)}_{2s}}_R) + STATE-PROJ-PREDICATE-side PREDICATE-PAIRING layer (the regulator-class atlas-thresholding). Atlas IS substrate-IS at the regulator-class classification layer (per `regulator-pin-discipline.md` substrate-internality of atlas membership) but NOT a state-pair functional on A_K. Registry-naming consequence: Option C STATE-PROJ-PREDICATE sub-class (not pure-OP-PROJ; not canonical STATE-PROJ). |
| 2 | §W10-111 NOW-5 SCHEMATIC↔PRIMARY robustness (clause b) | L2, Re:L2, R2 C-i, R2 D-ii, R2 D2-ii, R3 connes-D3-i | **Converged** (s=4 closes; s=3 routed to S89 PRIMARY rerun) | NOW-5 cardinality preservation at s=4 IS substrate-IS at substrate-distance-2 specifically (Mellin ≡ ζ ≡ Zubarev kernel-collapse is regulator-INVARIANT-by-definition at the pure-Mellin pole; Level-1.B sub-strata for §VII.K-PROP.W10-4). NOW-5 alone does NOT canonicalize the §W10-119 K=2 corpus's class-level Level-1.B reading at PRIMARY tier — the s=3 PRIMARY rerun is structurally required to extend Level-1.B to substrate-distance-1. Tangent-line-invariance vs higher-order structural invariance distinction is operational at the Level-1.A vs Level-1.B sub-strata. |
| 3 | Discriminating predicate for S89 PRIMARY rerun at s=3 with λ-derivative CM (clause c) | L3, Re:L3, R2 D-iii, R2 C2-i, R3 connes-C3-i | **Converged** (4-band partition + STAGE-1 regime-validity) | The S89 rerun gate adopts a TWO-STAGE structure: STAGE-1 regime-validity check via Friedrich-Bär saturation (η_FB_lower = 0.40 per W11-3 inheritance; cross-LEVEL drift PASS-1 < 1e-3, INFO-1 [1e-3, 1e-2], FAIL-1 > 1e-2 with FAIL-1 routing to L_max=12 PRIMARY rerun via existing master cache); STAGE-2 4-band partition (PASS-A {ζ, anomaly} = NPL-activates ⇒ substrate-distance-1 (A)+(C)-cross-class proper; PASS-B {ζ, Zubarev, anomaly} = NPL-stable ⇒ kernel-identity extension; FAIL {ζ, Zubarev} = artifact ⇒ s=3 collapses to s=4-like; INFO = NEW subset). Atlas / ε / CM bit-identical to S87 W2; PROHIBITED_ACTIONS Class 1 + Class 6 foreclosed by construction. |
| 4 | §W10-119 K-counter advancement rule (clause d) | L4, Re:L4, R2 D-iv, R2 D2-iii, R3 lizzi-D-iv, R3 connes-C3-ii | **Partial** (structural distinctness CONVERGED; architectural form NORMATIVE-OPEN) | Intra-Pillar-VII K-counter is STRUCTURALLY DISTINCT from cross-pillar K=3 MANDATORY (per `cross-pillar-bridge-anatomy.md` line 187 cross-link clause); same-counter inheritance from cross-pillar K=3 is FORBIDDEN by construction. Four K-counters operate disjoint (cross-pillar K=3 / intra-Pillar-VII K=2 / algebra-axis K=3 / OP-vs-STATE-PROJ K=3); counter-mixing is structurally indefensible. Architectural form OPEN: lizzi (i*) ∧ (ii* ∨ iii*) compromise vs connes (i*) ∧ (ii*) ∧ (iii*) strict — operationally equivalent under the structural-non-clone qualifier; rule-text-readability question deferred to S90+ pending forward-instance accumulation. |
| 5 | Projection-side suffix for §W10-119 calibration corpus (clause e) | L5, Re:L5, R2 C-iv, R2 C2-iv, R3 connes-D3-ii, R3 connes-C3-iv | **Emerged** (Option C STATE-PROJ-PREDICATE sub-class; K=1 baseline) | New STATE-PROJ-PREDICATE sub-class registers at `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` extension (Option C; rejects Path I forcing into canonical STATE-PROJ). K=1 baseline = §W10-119 HBW-pairwise-predicate at this S88 W30 close. Membership conjunction (α: predicate-on-spectrum-only-objects; β: regulator-class atlas external to A_K state space; γ: atlas-cardinality non-trivial). K=2/K=3 candidate forward instances: S87 W11-2 4-stratum partition stability + S87 W2 vs §W10-111 atlas-flip. K=3 promotion expected at S91 latest if both candidates pass (α) ∧ (β) ∧ (γ). |
| 6 | Cross-cutting — substrate-IS per-pole identity vs convention-tuple artifact (cross-cutting) | L6, C1, C2, R2 D2-i, R2 D2-ii, R3 connes-E3-i, R3 connes-E3-ii | **Emerged** (3-axis substrate-IS classification; failure-mode distinction) | Three-axis substrate-IS classification structure: Axis A (single-τ-slice vs moduli-deformation per `phononic-framing.md`); Axis B (per-Bulletin-per-pole 3-level ladder + Level-1.A/B sub-strata); Axis C (algebra-INVARIANT vs algebra-DEPENDENT vs HYBRID per algebra-axis K-counter MANDATORY-K=3). §W10-119 K=2 corpus inhabits Axis-A Level-1, Axis-B Level-1.B (s=4) + Level-1.A (s=3 pending S89), Axis-C HYBRID-via-STATE-PROJ-PREDICATE. Convention-tuple-artifact reading and container-thinking-violation are STRUCTURALLY DIFFERENT failure modes; the §W10-119 corpus survives both at the COHOMOLOGY-CLASS layer (substrate-first direction-of-explanation preserved). The S89 PRIMARY rerun closes the convention-tuple-artifact question at the EMPIRICAL-ANCHOR layer. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

The workshop converged on the substrate-IS COHOMOLOGY-CLASS-layer reading for §W10-119's K=2 SUGGESTION corpus (topic 6 cross-cutting), on the 4-band + STAGE-1 partition for the S89 PRIMARY rerun (topic 3), and on Option C STATE-PROJ-PREDICATE sub-class registration (topic 5). It produced concrete forward open questions of three kinds: (i) S89 dispatch-bound discriminating gates, (ii) S89 mack-cosmic-bridge plan-pinned-writer rule-extension landings, (iii) S90+ K-counter advancement and architectural-form normative-open questions. Each is specific enough to become a computation gate or a session-plan compute carry-forward.

1. **S89 PRIMARY rerun discriminating gate (clauses b + c closure)**: The S89-W10-111-PARALLEL-PRIMARY-S3-DISCRIMINATION-RUN gate dispatches with the 4-band partition + STAGE-1 regime-validity pre-check. Pre-registered gate: `S89-W10-111-PARALLEL-PRIMARY-S3-DISCRIMINATION-RUN` STAGE-1 PASS-1 = cross-LEVEL drift < 1e-3 across ALL R ∈ A_4 under Friedrich-Bär saturation (η_FB_lower = 0.40 per W11-3); STAGE-2 PASS-A = HBW^{PRIMARY}(s=3) = {ζ, anomaly} (substrate-IS NPL-activates); STAGE-2 PASS-B = {ζ, Zubarev, anomaly} (substrate-IS NPL-stable); STAGE-2 FAIL = {ζ, Zubarev} (artifact); STAGE-2 INFO = NEW subset. Effort 0.6 wave-equivalents; clones §W10-111 with parameterization swap + λ-derivative CM + s=3 pole + PRIMARY mode flag.

2. **S89 §W10-119 projection-side suffix retrofit (clause e closure)**: Pre-registered gate: `S89-W10-119-PROJECTION-SIDE-SUFFIX-RETROFIT` PASS = (i) `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` extended with three-corner taxonomy (OP-PROJ K=3 MANDATORY corpus preserved; canonical STATE-PROJ K=0 preserved; NEW STATE-PROJ-PREDICATE K=1 baseline registered with (α) ∧ (β) ∧ (γ) membership conjunction); (ii) `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` calibration-corpus citations updated to `§VII.K-PROP.W10-4.STATE-PROJ-PREDICATE` + `§VII.U.1.STATE-PROJ-PREDICATE`; (iii) registry-row renames at `permanent-results-registry.md`; (iv) `_registry_landing_audit.py` Class-(g) `OP-VS-STATE-PROJECTION-NAMING-DRIFT` flag clears. mack-cosmic-bridge plan-pinned writer (per `feedback_mack-bridge-role.md`); lizzi+connes co-sign on technical content. Effort 0.3 wave-equivalents.

3. **S89 §VII.K-PROP-COUNTER-TAXONOMY methodology theorem registration (clause d closure)**: Pre-registered gate: `S89-K-COUNTER-TAXONOMY-LAND` PASS = §VII.K-PROP-COUNTER-TAXONOMY methodology theorem appended to `permanent-results-registry.md` with four-K-counter disjoint corpora declaration (cross-pillar K=3 MANDATORY / intra-Pillar-VII K=2 SUGGESTION / algebra-axis K=3 MANDATORY / OP-vs-STATE-PROJ K=3 MANDATORY) + ENFORCEMENT clause requiring corpus-grep verification at every plan-freeze; corollary §VII.K-PROP-COUNTER-TAXONOMY-INTRA-PILLAR-EXTENSION declares the architectural-discipline distinction (cross-pillar disjunction-of-sufficient + conjunction-of-required vs intra-Pillar-VII strict-conjunction-or-compromise) with the form choice flagged as NORMATIVE-OPEN at S89; W-30 calibration-corpus row at K=1. METHODOLOGY-class per `wave-classification.md §M4`; allowlist append in same dispatch. Effort 0.4 wave-equivalents.

4. **S89 `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` Level-1 sub-strata refinement (clause a + cross-cutting closure)**: Pre-registered gate: `S89-PER-POLE-LEVEL-1-SUB-STRATA-LAND` PASS = sub-section text amended with explicit Level-1.A (tangent-line invariance) vs Level-1.B (higher-order structural invariance) sub-strata declaration on the per-pole 3-level ladder; existing K=2 corpus instances re-classified (§VII.K-PROP.W10-4 = Level-1.B; §VII.U.1 = Level-1.A pending S89 rerun); future Bulletins MUST declare sub-strata at landing; intra-Pillar-VII K-counter advancement criterion (i*) ∧ (ii* ∨ iii*) with structural-non-clone qualifier on the disjunction-of-sufficient axes per W-30 compromise. METHODOLOGY-class. Effort 0.3 wave-equivalents.

5. **S89 3-axis substrate-IS classification declaration discipline (cross-cutting closure)**: Pre-registered gate: `S89-3-AXIS-SUBSTRATE-IS-DECLARATION-DISCIPLINE` PASS = clause appended to `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` AND to `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` requiring future cross-pillar bridge entries (FWD-C1 / FWD-C2 / FWD-C3) and intra-Pillar-VII Bulletins (§W10-120 DORMANT activation) to declare ALL THREE axes at landing (Axis A single-τ-slice vs moduli-deformation; Axis B 3-level ladder + Level-1.A/B sub-strata; Axis C algebra-INVARIANT / algebra-DEPENDENT / HYBRID); plan-freeze validators emit registry-INCOMPLETE on missing axis declaration. METHODOLOGY-class. Effort 0.3 wave-equivalents.

6. **S89 STATE-PROJ-PREDICATE forward calibration corpus K=2 audit (clause e forward-pin)**: Pre-registered gate: `S89-STATE-PROJ-PREDICATE-K2-MEMBERSHIP-AUDIT` PASS = S87 W11-2 4-stratum partition stability INFO outcome re-classified under STATE-PROJ-PREDICATE membership criteria (α) ∧ (β) ∧ (γ); if eligible, register as K=2 instance with §VII.K-STRATUM-PARTITION sub-section landing; corpus-grep verification against four-K-counter taxonomy ensures no double-counting. Methodology-class per `wave-classification.md §M4`. Effort 0.3 wave-equivalents. K=3 audit (`S90-STATE-PROJ-PREDICATE-K3-MEMBERSHIP-AUDIT` on S87 W2 vs §W10-111 atlas-flip) deferred to S90.

7. **S89 §W10-120 DORMANT activation criterion amendment (clause d forward-pin)**: Pre-registered gate: `S89-DORMANT-ACTIVATION-CRITERION-AMEND` PASS = `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` activation-trigger clause amended to require intra-Pillar-VII HIT analog verification ((i*) ∧ (ii* ∨ iii*) per the rule-form chosen at S89 N3 above + structural-non-clone qualifier + Friedrich-Bär saturation profile distinctness per R2 D-iv + R2 Q-R2-3-(a) extension); §W10-120 DORMANT shell status updated to reflect new criterion; future Bulletin landings at s_new ∉ {3, 4} flagged for HIT-analog audit before counting toward K-promotion. METHODOLOGY-class. Effort 0.2 wave-equivalents.

8. **S90+ open question — does §W10-119 K-counter promotion require S89 rerun PASS in addition to §W10-120 third-pole landing?**: Per W-30 R3 connes-D3-i, the pre-S89-closure §W10-119 K=2 corpus's class-level Level-1.B reading is CONTINGENT on the S89 PRIMARY rerun PASS-A or PASS-B. If the S89 rerun returns FAIL, the §W10-119 K=2 corpus's s=3 instance demotes from Level-1.A to "magnitude-only Mellin-Dirichlet identity" (per R2 line 1113); intra-Pillar-VII K effectively retreats to K=1 (s=4 only, via §VII.K-PROP.W10-4 univariate scalar). In that scenario, §W10-120 DORMANT activation at s_new becomes the K=2 promotion vehicle, NOT the K=3. Open question: does `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` require explicit conditional-promotion text covering the S89-rerun-FAIL branch? Carry-forward to S89 plan-authorship for plan-freeze validator extension; no explicit gate yet pre-registered.

9. **S90+ open question — STATE-PROJ-PREDICATE structural-membership cross-corner companion handling**: Per W-30 R3 connes-C3-iv + R2 C2-iv, STATE-PROJ-PREDICATE membership conjunction (α) ∧ (β) ∧ (γ) defines K-counter advancement; instances failing the conjunction are tagged structurally-orthogonal-companion outside the K-counter. Open question: when a corpus instance is structurally companion to BOTH STATE-PROJ-PREDICATE AND OP-PROJ (e.g., the OBJECT layer alone of a HBW pairwise predicate, registered without the predicate-layer), is the cross-corner companion structure permitted under `registry-landing.md` line 162 ("cross-corner co-primary FORBIDDEN")? Carry-forward to S90+ rule-extension dispatch.

## Wrap-Up — Workshop Impact Summary

### What Changed

#### (a) Numerical revisions

- §W10-119 K=2 corpus class-level Level-1.B reading at PRIMARY tier is now CONTINGENT on the S89 PRIMARY rerun PASS-A or PASS-B (was implicitly canonicalized at S88 W10-119 close).
- The S89-W10-111-PARALLEL-PRIMARY-S3-DISCRIMINATION-RUN gate now binds to a TWO-STAGE structure (STAGE-1 Friedrich-Bär regime-validity at η_FB_lower = 0.40 + STAGE-2 4-band partition) — was a single-stage 3-band gate at seed file CF-W10-ADDITIONAL-A.
- S89 §W10-119 retrofit gate now binds to Option C three-corner taxonomy (OP-PROJ + canonical STATE-PROJ + NEW STATE-PROJ-PREDICATE) — was a binary OP-PROJ-vs-STATE-PROJ choice at seed file CF-W10-ADDITIONAL-B.

#### (b) Structural changes

- HBW pairwise predicate algebra-axis K-counter classification: pure-INVARIANT → HYBRID (OP-PROJ-side OBJECT layer + STATE-PROJ-PREDICATE-side PREDICATE-PAIRING layer).
- §W10-119 K-counter: SAME-counter-as-cross-pillar-K=3 reading → STRUCTURALLY-DISTINCT intra-Pillar-VII counter on disjoint corpus.
- Per-Bulletin-per-pole Level-1 admissibility: monolithic atomic claim → Level-1.A (tangent-line invariance) vs Level-1.B (higher-order structural invariance) NON-FUNGIBLE sub-strata.
- §W10-119 corpus suffix discipline: undeclared → Option C STATE-PROJ-PREDICATE NEW sub-class with (α) ∧ (β) ∧ (γ) structural-membership conjunction.
- substrate-IS classification: 1-axis (substrate-IS / not) → 3-axis (Axis A single-τ-slice vs moduli-deformation; Axis B Level-1.A/1.B vs Level-2 vs Level-3 ladder; Axis C INVARIANT vs DEPENDENT vs HYBRID per algebra-axis K-counter MANDATORY-K=3) classification structure.
- Failure-mode taxonomy: convention-tuple-artifact ≡ container-thinking-violation conflation → STRUCTURALLY DIFFERENT failure modes (former is empirical-tier; latter is epistemic-direction; both can coincide but are distinct in principle).

### What Holds

- The §W10-119 K=2 SUGGESTION corpus's substrate-IS reading is preserved at the COHOMOLOGY-CLASS layer (Axis B Level-1, both calibration-corpus instances). The §VII.K-PROP.W10-4 ρ_∞ structural irrationality (CC2 PROVEN) and §VII.U.1 Mellin-Dirichlet identity at substrate-distance-1 retain registry status; the per-pole substrate-IS structural-fingerprint reading is well-formed at the AXIOM layer for both poles.
- The Mellin ≡ ζ ≡ Zubarev kernel-collapse at substrate-distance-2 pole s=4 IS substrate-IS structural identity at substrate-distance-2 specifically (regulator-INVARIANT-by-definition; holds at any LEVEL, any CM, any L_max). NOW-5 cardinality preservation at s=4 IS the empirical surface of this substrate-level kernel-identity, NOT a numerical accident.
- The four-K-counter disjoint taxonomy (cross-pillar K=3 MANDATORY / intra-Pillar-VII K=2 SUGGESTION / algebra-axis K=3 MANDATORY / OP-vs-STATE-PROJ K=3 MANDATORY) operates with pairwise-disjoint corpora; counter-mixing remains a structural defect under either architectural-form choice.
- The substrate-first direction-of-explanation flow (substrate spectral triple → Peter-Weyl decomposition → per-regulator Mellin moments → HBW pairwise predicate → per-pole HBW subset) is preserved throughout the workshop's structural verdict; container-thinking inversions are foreclosed at the registry-naming and rule-text layers.
- Verdict-line content for §W10-110 / §W10-111 / §W10-112 / §W10-113 / §W10-114 / §W10-115 / §W10-116 / §W10-117 / §W10-118 / §W10-119 / §W10-120 on disk is ABSOLUTELY PERMANENT (per `gate-verdicts.md §"Rules"` item 2; this workshop touches no audit_sha256 / content_sha256 / value strings / schemes / conventions / L_max).
- PROHIBITED_ACTIONS Class 1 (convention-shopping) and Class 6 (iterate-until-PASS) are foreclosed by construction at the S89 PRIMARY rerun gate (bit-identical hold of atlas / ε / CM matched to S87 W2; 4-band partition exhausts the 6 unordered 2-subsets containing ζ).

### What Breaks or Strains

- The §W10-119 sub-section text as authored at S88 W10-119 close is internally consistent at the COHOMOLOGY-CLASS layer but DIAGNOSTICALLY IMPRECISE at the suffix-discipline layer (no projection-side suffix declared on §VII.K-PROP.W10-4 + §VII.U.1 calibration-corpus citations); silent class-conflation pathology is admissible until S89 retrofit lands.
- The S87 W2 atlas-cardinality cascade workshop's HBW = {ζ, anomaly} reference is structurally non-comparable to the §W10-111 NOW-5 result without disambiguating atlas-vs-LEVEL effects; the Zubarev ≡ ζ kernel-identity at any LEVEL forces Zubarev into HBW under atlas A_4 + ε = 1e-12. The S87 W2 reference may have used atlas A_3 = {ζ, SDW, anomaly} (NOT A_4) or a different ε; this needs explicit forensic audit at S89 plan-authorship.
- The §W10-113 factor-100 SCHEMATIC↔PRIMARY LEVEL-DEPENDENCE FAIL at substrate-distance-1 pole s=3 means absolute moments are tier-shifted; pairwise structure preservation at s=3 PRIMARY is the OPEN structural question routed to S89 PARALLEL-PRIMARY-S3-DISCRIMINATION-RUN; pre-rerun, the §VII.U.1 substrate-IS reading at PRIMARY tier is STRUCTURALLY UNCLOSED.
- The architectural form (i*) ∧ (ii*) ∧ (iii*) vs (i*) ∧ (ii* ∨ iii*) for the intra-Pillar-VII HIT analog remains NORMATIVE-OPEN; rule-text-readability question deferred to S90+ pending forward-instance accumulation. Operational equivalence under the structural-non-clone qualifier means the choice does not block §VII.K-PROP-COUNTER-TAXONOMY registration but the rule-text ambiguity persists until S90+.
- The recursive-Casimir-projection feasibility for the s=3 PRIMARY rerun at L_max=10 is structurally bounded above (per Re:L3 Step 4: NEW-sector contribution at p+q ∈ {11, 12} bounded by 16 · 12 · 2.89^{-6} ≈ 0.33, substantial relative to M^{PRIMARY}_3 ≈ 0.30). The Friedrich-Bär saturation STAGE-1 pre-check is necessary but may itself FAIL at L_max=10 PRIMARY for s=3, forcing route to L_max=12 PRIMARY rerun via the existing master cache.

### Carry-Forward Computations

1. **S89 PRIMARY rerun at substrate-distance-1 pole s=3 with λ-derivative CM (clauses b + c closure)**
   - **What**: dispatch S89-W10-111-PARALLEL-PRIMARY-S3-DISCRIMINATION-RUN gate with the TWO-STAGE structure (STAGE-1 Friedrich-Bär regime-validity at η_FB_lower = 0.40 across A_4; STAGE-2 4-band partition under bit-identical hold of atlas A_4 / ε = 1e-12 / λ-derivative CM matched to S87 W2). Friedrich-Bär saturation analysis per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`.
   - **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (PRIMARY canonical D_K Peter-Weyl, filtered to L_max=10 operational; if FAIL-1 fires, route to L_max=12 PRIMARY direct evaluation); §W10-111 ensemble pairwise script as template; W11-3 Friedrich-Bär calibration corpus (η_FB_lower = 0.40); S87 W2 atlas-cardinality cascade workshop reference subset; λ-derivative CM parameterization specification from S87 W2.
   - **Gate**: `S89-W10-111-PARALLEL-PRIMARY-S3-DISCRIMINATION-RUN` STAGE-1 PASS-1 = cross-LEVEL drift < 1e-3; STAGE-2 PASS-A = HBW^{PRIMARY}(s=3) = {ζ, anomaly} (NPL-activates); STAGE-2 PASS-B = {ζ, Zubarev, anomaly} (NPL-stable); STAGE-2 FAIL = {ζ, Zubarev} (artifact); STAGE-2 INFO = NEW subset. Convention tag includes `-PRIMARY-LAMBDA-CM-LEVEL-1-B-DISCRIMINATOR` suffix per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-K=4.
   - **Effort**: 0.6 wave-equivalents (COMPUTE-class).

2. **S89 §W10-119 projection-side suffix retrofit + registry-landing.md Option C three-corner extension (clause e closure)**
   - **What**: extend `registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY-K=3 clause with Option C three-corner taxonomy (OP-PROJ K=3 MANDATORY corpus preserved; canonical STATE-PROJ K=0 preserved; NEW STATE-PROJ-PREDICATE K=1 baseline registered with (α) ∧ (β) ∧ (γ) membership conjunction; cross-corner co-primary remains FORBIDDEN per existing line 162). Apply STATE-PROJ-PREDICATE suffix retrofit at `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` calibration-corpus citations + `permanent-results-registry.md` registry-row renames (`§VII.K-PROP.W10-4.STATE-PROJ-PREDICATE` + `§VII.U.1.STATE-PROJ-PREDICATE`). Verify `_registry_landing_audit.py` Class-(g) `OP-VS-STATE-PROJECTION-NAMING-DRIFT` flag clears.
   - **Inputs**: `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` (K=3 MANDATORY from S88 W8-92); `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (S88 W10-119 landing, 57 lines); existing §VII.K-PROP.W10-4 + §VII.U.1 registry entries; this workshop's R3 connes-C3-iv + R3 connes-D3-ii + lizzi-R3 C-iv stipulation.
   - **Gate**: `S89-W10-119-PROJECTION-SIDE-SUFFIX-RETROFIT` PASS = three-corner extension landed at `registry-landing.md`; calibration-corpus citations renamed at `cross-pillar-bridge-anatomy.md`; registry-row renames at `permanent-results-registry.md`; audit-script Class-(g) flag clears. mack-cosmic-bridge plan-pinned writer per `feedback_mack-bridge-role.md`; lizzi+connes co-sign on technical content.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class per `wave-classification.md §M4`; rule-file edits + registry-row renames + audit-script verification).

3. **S89 §VII.K-PROP-COUNTER-TAXONOMY methodology theorem registration + intra-Pillar-VII independence-test corollary (clause d closure + cross-cutting structural deliverable)**
   - **What**: register §VII.K-PROP-COUNTER-TAXONOMY methodology theorem at `permanent-results-registry.md` with four-K-counter disjoint corpora declaration (cross-pillar K=3 MANDATORY {W-5, W11-5, W4a-17} + intra-Pillar-VII K=2 SUGGESTION {§VII.K-PROP.W10-4, §VII.U.1} + algebra-axis K=3 MANDATORY + OP-vs-STATE-PROJ K=3 MANDATORY {W4-2, W6-1, W11-meta-2}, with NEW STATE-PROJ-PREDICATE K=1 baseline tracked separately); ENFORCEMENT clause requiring corpus-grep verification at every plan-freeze on every new registry-landing or rule-extension. Register companion §VII.K-PROP-COUNTER-TAXONOMY-INTRA-PILLAR-EXTENSION corollary declaring the architectural-discipline distinction (cross-pillar `(i ∨ ii ∨ iii) ∧ iv` disjunction-of-sufficient + conjunction-of-required vs intra-Pillar-VII strict (i*) ∧ (ii*) ∧ (iii*) or compromise (i*) ∧ (ii* ∨ iii*) — with structural-non-clone qualifier rendering them operationally equivalent at the corpus-membership audit layer; rule-text-readability choice flagged NORMATIVE-OPEN at S89).
   - **Inputs**: this workshop's R1 C2 + R2 C2-ii + R3 connes-C3-ii; lizzi R2 EMERGENCE E-i registry text proposal; cross-pillar-bridge-anatomy.md §"Forward template-adoption" + §"Per-Bulletin-per-pole Level-1 wall classification" + §"Algebra-axis orthogonality K-counter"; registry-landing.md §"Operator-Projection Reading-A Naming Hygiene".
   - **Gate**: `S89-K-COUNTER-TAXONOMY-LAND` PASS = §VII.K-PROP-COUNTER-TAXONOMY + corollary appended to `permanent-results-registry.md`; ENFORCEMENT clause references `_registry_landing_audit.py` corpus-grep extension; W-30 calibration-corpus row at K=1 (this workshop is the first explicit instance of the four-K-counter taxonomy registration). METHODOLOGY-class per `wave-classification.md §M4`; allowlist append in same dispatch. mack-cosmic-bridge plan-pinned writer; lizzi+connes co-sign on technical content.
   - **Effort**: 0.4 wave-equivalents (METHODOLOGY-class).

4. **S89 Per-Bulletin-per-pole Level-1 sub-strata refinement (clause a + cross-cutting closure)**
   - **What**: amend `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` with explicit Level-1.A (tangent-line invariance under uniform-rescaling K_R) vs Level-1.B (higher-order structural invariance preserved under non-uniform δ_R) sub-strata declaration on the per-pole 3-level ladder. Re-classify existing K=2 corpus instances: §VII.K-PROP.W10-4 = Level-1.B (univariate regulator-INDEPENDENT scalar; tier-independent by construction; substrate-IRRATIONAL per CC2 PROVEN); §VII.U.1 = Level-1.A pending S89 PRIMARY rerun PASS-A or PASS-B for Level-1.B promotion. Future Bulletins MUST declare sub-strata at landing. Append intra-Pillar-VII independence-test rule (i*) ∧ (ii* ∨ iii*) compromise form with structural-non-clone qualifier per W-30 R2 D-iv + R3 closing.
   - **Inputs**: this workshop's R1 C1 + R2 D-ii + R2 EMERGENCE E-ii + R3 connes-C3-iii; existing `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` (S88 W10-119 landing, 57 lines); §W10-113 SCHEMATIC↔PRIMARY decomposition (16-fold spinor + (0,0)-sector + Jensen non-uniformity).
   - **Gate**: `S89-PER-POLE-LEVEL-1-SUB-STRATA-LAND` PASS = sub-strata declaration appended; existing K=2 corpus re-classified (Level-1.B for §VII.K-PROP.W10-4; Level-1.A for §VII.U.1); intra-Pillar-VII independence-test rule landed; W-30 calibration-corpus row added. METHODOLOGY-class per `wave-classification.md §M4`. mack-cosmic-bridge plan-pinned writer.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class).

5. **S89 3-axis substrate-IS classification declaration discipline (cross-cutting closure)**
   - **What**: append clauses to `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` AND `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` requiring future cross-pillar bridge entries (FWD-C1 / FWD-C2 / FWD-C3 per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates for S88+ dispatch"`) AND intra-Pillar-VII Bulletins (§W10-120 DORMANT activation) to declare ALL THREE substrate-IS axes at landing: Axis A (single-τ-slice vs moduli-deformation per `phononic-framing.md`); Axis B (per-Bulletin-per-pole 3-level ladder + Level-1.A/B sub-strata); Axis C (algebra-INVARIANT vs algebra-DEPENDENT vs HYBRID per algebra-axis K-counter MANDATORY-K=3). Plan-freeze validators emit registry-INCOMPLETE on missing axis declaration.
   - **Inputs**: this workshop's R3 connes-C3-iii + R3 connes-E3-i; `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`; W-30 §W10-119 K=2 corpus 3-axis classification (Axis-A Level-1; Axis-B Level-1.B + Level-1.A; Axis-C HYBRID-via-STATE-PROJ-PREDICATE) as the calibration instance.
   - **Gate**: `S89-3-AXIS-SUBSTRATE-IS-DECLARATION-DISCIPLINE` PASS = clauses appended to both rule-files; W-30 calibration-corpus instance recorded; plan-freeze validator extension queued. METHODOLOGY-class per `wave-classification.md §M4`.
   - **Effort**: 0.3 wave-equivalents (METHODOLOGY-class).

6. **S89 STATE-PROJ-PREDICATE forward calibration corpus K=2 audit (clause e forward-pin)**
   - **What**: re-classify S87 W11-2 4-stratum partition stability INFO outcome under STATE-PROJ-PREDICATE membership criteria (α: predicate-on-spectrum-only-objects; β: regulator-class atlas external to A_K; γ: atlas-cardinality non-trivial). If eligible, register as K=2 corpus instance with §VII.K-STRATUM-PARTITION sub-section landing at `permanent-results-registry.md`. Corpus-grep verification against four-K-counter taxonomy ensures no double-counting.
   - **Inputs**: this workshop's R2 EMERGENCE E-iii + R2 C2-iv + R3 connes-C3-iv; S87 W11-2 4-stratum partition stability INFO verdict (`computations/session-87/s87_gate_verdicts.txt`); STATE-PROJ-PREDICATE membership conjunction definition.
   - **Gate**: `S89-STATE-PROJ-PREDICATE-K2-MEMBERSHIP-AUDIT` PASS = (α) ∧ (β) ∧ (γ) conjunction satisfied for S87 W11-2 4-stratum partition; K=2 instance registered at §VII.K-STRATUM-PARTITION; corpus-grep clears double-count. METHODOLOGY-class per `wave-classification.md §M4`.
   - **Effort**: 0.3 wave-equivalents.

7. **S89 §W10-120 DORMANT activation criterion amendment (clause d forward-pin)**
   - **What**: amend `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` activation-trigger clause to require intra-Pillar-VII HIT analog verification ((i*) ∧ (ii* ∨ iii*) per the architectural form chosen at S89 CF #4 + structural-non-clone qualifier per W-30 R2 D2-iii / R3 connes-C3-ii + Friedrich-Bär saturation profile distinctness per W-30 R2 D-iv + R2 Q-R2-3-(a) extension); update §W10-120 DORMANT shell status to reflect the new criterion; future Bulletin landings at s_new ∉ {3, 4} flagged for HIT-analog audit before counting toward K-promotion.
   - **Inputs**: this workshop's R1 C2 + R2 D-iv + R3 connes-C3-ii; §W10-120 DORMANT shell pre-registration metadata at `sessions/archive/session-88/session-88-w10-workingpaper.md §W10-120` lines 1240-1287; W11-3 Friedrich-Bär calibration corpus.
   - **Gate**: `S89-DORMANT-ACTIVATION-CRITERION-AMEND` PASS = activation-trigger clause amended; HIT-analog audit step pre-registered; §W10-120 DORMANT shell status updated. METHODOLOGY-class per `wave-classification.md §M4`. mack-cosmic-bridge plan-pinned writer.
   - **Effort**: 0.2 wave-equivalents (METHODOLOGY-class).

### Closing Line

The W-30 closure adopts the substrate-IS COHOMOLOGY-CLASS reading for §W10-119's K=2 corpus while routing the EMPIRICAL-ANCHOR Level-1.B closure at substrate-distance-1 to the S89 PRIMARY rerun via a 4-band partition + Friedrich-Bär STAGE-1 pre-check, and registers the four-K-counter disjoint taxonomy + Option C STATE-PROJ-PREDICATE sub-class + Level-1.A/1.B sub-strata as the structural deliverables that bind future intra-Pillar-VII Bulletin landings to the substrate's own per-pole multi-axis identity.
