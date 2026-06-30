# Session 90 — Connes Solo Synthesis — Slot 1 S-3

## PARTIAL-POSITIVE 3-Class Compliance Taxonomy (W1-9) Adequacy Review

**Agent**: `connes-ncg-theorist` (Workhorse-NCG; independent solo synthesis per
`/rclab-review --agents connes` semantics, NO `--type`, NO `--rounds`).
**Dispatch slot**: Session-90 workshop schedule Slot 1 entry S-3.
**Trigger**: parallel-review owe (connes was NAMED as CO-AUTHOR in `session-90-plan-w1.md §W1-9` line 566 but NOT dispatched at landing; the gen-physicist orchestrator-direct-write was the sole landing agent per `wave-classification.md §"Dispatch consequences"`).
**Status**: SOLO SYNTHESIS — no verdict line, no audit_sha256 emission; output feeds S91 plan-freeze decisions.

---

## 0. Verification narration

The W1-9 landing report at `sessions/archive/session-90/session-90-w1-workingpaper.md` lines 436-486 documents a 3-class compliance taxonomy extension to `substrate-first-canonical-sourcing.md §(iv)`. The rule extension lives at `substrate-first-canonical-sourcing.md` lines 101-218 (3-class taxonomy sub-section + Row 5 prose annotation + K-counter advancement sub-section). The audit-script extension lives at `computations/_shared/_substrate_first_provenance_audit.py` lines 168-327 (`detect_compliance_class` function + 5 module-level constants). The 4-test driver lives at `computations/_shared/s90_w1_partial_positive_audit_test.py` (T1 live W5-7 PARTIAL-POSITIVE + T2 live W9c-1 POSITIVE + T3 live W4-2 NEGATIVE + T4 synthetic 2-bit matrix). The PARTIAL-POSITIVE calibration instance is `S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY` at `computations/session-89/s89_gate_verdicts.txt:128` (audit_sha256=`884db5e02fff4d9791c94ad0140edc77158355d189faa26491dc83e5b9cbbc50`; convention=`lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4-SCHEMATIC`). I have read all seven cited source files in full. This synthesis is my connes-side independent reading of (a) partition exhaustiveness, (b) W5-7 pinning structural soundness, (c) K-counter advancement validity, (d) forward tier_pin promotion path; concluding with a verdict shape, a forward-recommendation, and a 4-field carry-forward.

---

## 1. Structural framing — substrate-first, then methodology F-image

Before evaluating the 2-bit signature partition, I locate the W1-9 extension within the substrate ↔ methodology ↔ audit layer-functor `F` per `epistemic-discipline.md §"Layer-Decomposition"`.

**The substrate.** The substrate-physics object at issue is the regulator-class structure on the spectral triple `(A_K, H_K, D_K)` of Jensen-deformed SU(3). The substrate carries an intrinsic distinction between UV regularizations that are physical (Pauli-Villars with mass-scale running at `Λ_UV = M_KK`; zeta-function regularization via the analytic continuation of `ζ_D(s) = Tr(D^{-s})` at simple poles of the dimension spectrum; live Mellin-cone evaluation of `Tr(D^{-2s})` via residue at substrate-distance poles) and those that are SCHEMATIC analogs (Gaussian-envelope cutoffs with hand-tuned ghost subtractions; smooth Casimir-bound interpolations; the helpers in `_spectral_action_regulators.py` whose docstring lines 23-30 self-identify as such). The distinction matters because the spectral action `Tr f(D²/Λ²)` and its Seeley-DeWitt expansion `a_0·Λ⁴ + a_2·Λ² + a_4 + ...` are sensitive to UV-cutoff geometry at the `a_n` heat-kernel coefficient level: a SCHEMATIC envelope and a FULL physical regularization can produce numerically similar but structurally distinct `a_n` extractions, particularly at substrate-distance poles where the pole-residue and the regulator-tail interact nontrivially.

**The methodology F-image.** Rules (1) ∧ (2) ∧ (3) at `substrate-first-canonical-sourcing.md §(iv)` are the methodology-floor F-image of substrate-side commutativity on this regulator-class structure:

- rule (1) declares CLASS pin SCHEMATIC at plan-block layer (F-image at plan-text layer);
- rule (2) emits `-SCHEMATIC` suffix on the verdict-line `convention=` field (F-image at verdict-line layer);
- rule (3) acknowledges SCHEMATIC at the producing-script docstring layer (F-image at script-body layer).

The substrate-side predicate being tracked is "the producing computation IS a SCHEMATIC realization of the substrate's regulator-class structure, NOT a FULL physical realization". The conjunction (1) ∧ (2) ∧ (3) is the methodology-layer realization of this single substrate predicate at three structurally-distinct F-image loci (plan-text / verdict-line / script-docstring). All three loci must encode the SCHEMATIC class for the F-image to be commutative across the layer-functor; failure at any locus produces a class-conflation pathology analogous to the UV-regulator silent class-conflation closed at S75 ZETA-NOT-PHYSICAL-75.

**The tier_pin row.** The companion comment row `# tier_pin=TIER-2` is NOT a substrate-side commutativity predicate. It is a methodology-floor audit-trail completeness marker — a downstream redundancy disclosure that names the SCHEMATIC class at the verdict-FILE layer (the layer where audit consumers read). The tier_pin row's substrate-side correlate is approximately a "presentation hygiene" predicate that strengthens the F-image's discoverability without altering its commutativity. A producing script that satisfies (1) ∧ (2) ∧ (3) but omits tier_pin has correctly encoded the substrate-IS regulator-class membership at all three structural F-image layers; the tier_pin row would have added a 4th audit-trail discoverability hop at the verdict-file layer, which is desirable but not load-bearing for the substrate-side commutativity check.

This is the structural frame within which I evaluate the 4 adjudication questions.

---

## 2. Adjudication question (a) — Is the 2-bit signature partition exhaustive?

### 2.1 The 2-bit signature square

The W1-9 extension defines the partition via the 2-bit signature

```
(rules-1∧2∧3-all-PASS, tier_pin-row-PRESENT) ∈ {T,F} × {T,F}
```

with the assignment:

| Bit 1 | Bit 2 | Class | Severity |
|:-----:|:-----:|:------|:--------:|
| T | T | POSITIVE | NO-ACTION |
| T | F | PARTIAL-POSITIVE | ADVISORY-S2 |
| F | T | NEGATIVE | MANDATORY-S1 |
| F | F | NEGATIVE | MANDATORY-S1 |

The rule explicitly states (`substrate-first-canonical-sourcing.md` line 126): "The tier_pin row is meaningful only when the substrate-side rules are PASS; if rules (1)-(3) are NOT all PASS, tier_pin row presence is irrelevant (the class is NEGATIVE regardless)."

### 2.2 Does (F, T) collapse correctly to NEGATIVE?

The adjudication question asks whether (F, T) — substrate-side rules (1) ∧ (2) ∧ (3) FAIL but tier_pin row PRESENT — should warrant a 4th distinct class "METHODOLOGY-FLOOR-INCOMPLETE-OVER-NEGATIVE-SUBSTRATE", or correctly collapse to NEGATIVE.

**Connes-side reading: NEGATIVE is correct.** The collapse is structurally sound for three independent reasons grounded in the substrate ↔ methodology F-image discipline.

**Reason 1 — F-image commutativity is asymmetric.** The layer-functor `F: substrate → methodology → audit` carries the substrate's regulator-class structure to the methodology layer through rules (1)-(3) and to the audit layer through the verdict-file emission. The substrate-side commutativity check is whether the F-image at the methodology layer commutes with the F-image at the audit layer when both layers are evaluated against the substrate-IS regulator-class membership. If rules (1)-(3) FAIL, the F-image at the methodology layer is structurally broken — the producing-script's plan-text, verdict-line `convention=` field, and docstring layer are NOT collectively encoding the SCHEMATIC class. A tier_pin row at the audit layer in this case ENCODES SCHEMATIC CLASS MEMBERSHIP THAT THE METHODOLOGY LAYER HAS NOT DECLARED. This is structurally analogous to a verdict line emitting `convention=foo-SCHEMATIC` while the producing script has zero SCHEMATIC docstring acknowledgment — the convention suffix is itself a methodology-floor commitment to which the producing-substrate-physics work has not subscribed. The tier_pin row in (F, T) is in the same epistemic position: a methodology-floor disclosure WITHOUT the upstream substrate-side commutativity check that should have produced it. Audit-leg commitments unsupported by methodology-leg substrate-side compliance are NEGATIVE by structural necessity.

**Reason 2 — Forbidden direction of rescue.** Per `phononic-framing.md §"IS Space, Not IN Space"` and `substrate-first-canonical-sourcing.md §(iv)` line 99 ("Without (1)-(3), gate verdicts under SCHEMATIC helpers are structurally indistinguishable from gate verdicts under FULL physical regularizations"), the direction of explanation flows substrate → methodology → audit. A methodology-floor refinement cannot RESCUE a substrate-side failure — a class-conflation that is silent at the methodology layer is silent regardless of any tier_pin annotation at the audit layer, because the tier_pin row reads the convention suffix of the SAME verdict line whose convention suffix has failed rule (2). The tier_pin row says "I am TIER-2 SCHEMATIC", but rule (2) said "my `convention=...` field has NO `-SCHEMATIC` suffix". The two annotations are now contradictory, and the audit consumer must resolve the contradiction; by Reason 1, the only consistent resolution is to read the tier_pin row as a methodology-leg disclosure unsupported by substrate-side compliance — NEGATIVE.

**Reason 3 — Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY routing.** The rule text at lines 305-313 of the audit script `detect_compliance_class` function routes NEGATIVE through Class-(d) per `epistemic-discipline.md §"Source Reconciliation"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY. A (F, T) instance is structurally a Class-(d)-equivalent — the audit-trail-completeness layer (tier_pin) is acting as a DERIVATIVE that has been pinned without its substrate-side primary (rules 1-3). The collapse to NEGATIVE is the same routing that Class-(d) PIN-DERIVATIVE applies. Promoting (F, T) to a distinct 4th class "METHODOLOGY-FLOOR-INCOMPLETE-OVER-NEGATIVE-SUBSTRATE" would create a structural redundancy with Class-(d) PIN-DERIVATIVE — both classes would describe the same pathology (downstream commitment without upstream substrate-side support) at slightly different methodology-floor loci. Rule-file economy plus the algebra-axis orthogonality discipline (see §3 below) argues against this 4th class.

**Operational note.** I observe that the existing `detect_compliance_class` function at lines 290-303 of `_substrate_first_provenance_audit.py` uses an `if/elif/else` branch structure where the third branch catches BOTH (F, T) and (F, F) via the catch-all `else: compliance_class = "NEGATIVE"`. This is the structurally correct implementation of the rule. The T4 synthetic test case `FT_negative` in `s90_w1_partial_positive_audit_test.py` lines 274-289 explicitly tests (F, T) → NEGATIVE and passes 4/4 in the synthetic matrix. **The collapse is verified at the audit-script level + test driver level + rule-file text level.**

### 2.3 Is the partition logically exhaustive over the 2-bit square?

Yes. The four cells (T,T) + (T,F) + (F,T) + (F,F) are the complete enumeration of the {0,1} × {0,1} square. The partition maps them to {POSITIVE, PARTIAL-POSITIVE, NEGATIVE, NEGATIVE}. Every possible 2-bit signature maps to exactly one class; the partition is well-defined, exhaustive, and mutually exclusive.

### 2.4 Connes verdict on (a)

**Partition is exhaustive and structurally sound.** The (F, T) → NEGATIVE collapse is the substrate-correct routing (methodology-floor refinement cannot rescue substrate-side failure). The proposed 4th class "METHODOLOGY-FLOOR-INCOMPLETE-OVER-NEGATIVE-SUBSTRATE" would create rule-file redundancy with Class-(d) PIN-DERIVATIVE and add no structural discriminating power beyond what NEGATIVE + Class-(d) routing already supplies. No amendment recommended on this axis.

---

## 3. Adjudication question (b) — Is the W5-7 PARTIAL-POSITIVE pinning structurally sound?

### 3.1 What W5-7 actually emitted

I read the W5-7 verdict line at `computations/session-89/s89_gate_verdicts.txt:128`:

```
S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY: PASS -- value='N=4/5;reading_A_WIN=1;max_bootstrap_sigma=0.0000;reading_winner=Reading-A_WIN_N=4/5_>=_4;sign=N/A;mag=PASS;reg=VALID' scheme=heat-kernel-rank-ordering convention=lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4-SCHEMATIC L_max=12 audit_sha256=884db5e02fff4d9791c94ad0140edc77158355d189faa26491dc83e5b9cbbc50 content_sha256=57ae89ba7f30092db0954eb27413774a1a1b82c6d235866a2e2933f6de11a7a2 schema_version=S87+
```

The 4-element disclosure status:
- **rule (1) CLASS pin SCHEMATIC**: PASS (producing-script OPERATIONAL DEVIATION docstring at `s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py` lines 23-39 explicitly cites `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline).
- **rule (2) `-SCHEMATIC` convention suffix**: PASS (convention field ends with `-SCHEMATIC`).
- **rule (3) docstring acknowledgment**: PASS (full SCHEMATIC OPERATIONAL DEVIATION declaration in producing-script docstring; carry-forward note "S90 retry with the canonical W7a-74 PRIMARY evaluator script for proper FULL-tier evaluation" demonstrates upgrade-path awareness).
- **tier_pin row**: ABSENT (the verdict file emits canonical line + W9a-99 dual-SHA companion + S87-schema-v2 3-tuple companion at lines 129-130, but no `# tier_pin=TIER-2` row).

2-bit signature: (T, F) → PARTIAL-POSITIVE.

### 3.2 Is the missing tier_pin row a slow-erosion risk?

The adjudication question asks whether the W5-7 PARTIAL-POSITIVE pinning admits slow erosion of the tier_pin discipline by example — future S88+ scripts pattern-match W5-7 and skip the tier_pin row — OR whether the substrate-side rules (1) ∧ (2) ∧ (3) discipline structurally bounds the erosion via the (1)+(2)+(3) PASS prerequisite.

**Connes-side reading: the erosion is structurally bounded, but not zero.**

**Why the erosion is bounded.** The substrate-side commutativity check rules (1) ∧ (2) ∧ (3) remain MANDATORY at K_substantive ≥ 3 per `substrate-first-canonical-sourcing.md §(iv)` baseline (K=4 promotion at S88 W7b-83 close). The W1-9 extension explicitly states (line 218): "The PARTIAL-POSITIVE addition is a STRENGTHENING of the §(iv) discipline at the corpus-coverage axis (more loci tracked) WITHOUT relaxing the substrate-side commutativity check (rules (1)-(3) remain MANDATORY); only the methodology-floor refinement (tier_pin row) is admitted as forward-recommended-not-mandatory at the new compliance class." This is correctly worded — the substrate-side baseline does NOT relax. Any future SCHEMATIC-helper-consuming script that fails rules (1) ∧ (2) ∧ (3) lands in NEGATIVE with MANDATORY-S1 severity; the W5-7 example does NOT provide a pattern for relaxing rules (1)-(3).

**Why the erosion is non-zero.** A producing script reading the W5-7 calibration row in §(iv) will see:
- W5-7 satisfies (1) ∧ (2) ∧ (3) — three out of four disclosure elements;
- tier_pin row is absent;
- the canonical class is PARTIAL-POSITIVE at severity ADVISORY-S2;
- "forward-recommended-not-mandatory" is the disposition.

The pattern-matchable behavioral inference is: "Emit the convention suffix and docstring acknowledgment, declare CLASS pin SCHEMATIC, but the tier_pin row is OPTIONAL." A diligent agent will read the rule text more carefully and see "SHOULD pattern-match the W9c-1 disclosure protocol" at line 224 — but a less diligent agent may pattern-match the W5-7 path of least resistance. The W5-7 example provides a normative pattern that the tier_pin row is dispensable at landing time, even if formally recommended.

This is structurally analogous to the W4-2 / W9b-2 NEGATIVE-CALIBRATION pattern that originally motivated the W1-9 corrective action (`substrate-first-canonical-sourcing.md` line 161): "The MANDATORY status promotion (S88 W7b-83 close, 2026-05-05) is therefore corrective action — extending the discipline to MANDATORY at plan-freeze for S89+ closes the silent class-conflation pathway by construction at the rule-file level rather than relying on per-instance agent honesty (W4-2 post-hoc disclosure pattern)." The W4-2 NEGATIVE pattern persisted across W9b-2 (one-session lag) before being structurally closed at S88. The W5-7 PARTIAL-POSITIVE pattern carries the analogous risk: it can persist as a normative example UNTIL the tier_pin row is also closed at the rule-file level.

### 3.3 Where the structural bound is load-bearing

The structural bound on erosion is the substrate-side commutativity check rules (1) ∧ (2) ∧ (3). The MANDATORY status of this check is what prevents the W5-7 PARTIAL-POSITIVE pattern from causing class-conflation across the substrate ↔ methodology F-image. Concretely:

- If a future script fails rules (1) ∧ (2), the audit-script `detect_compliance_class` returns NEGATIVE at severity MANDATORY-S1 per line 305-313. This routes through Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation. The substrate ↔ methodology class-conflation is closed by structural enforcement.
- If a future script satisfies rules (1) ∧ (2) ∧ (3) but omits tier_pin, it lands PARTIAL-POSITIVE at severity ADVISORY-S2. The substrate-IS regulator-class membership is correctly encoded at three F-image loci; only the audit-trail-completeness layer has a soft gap. The class-conflation pathway is NOT operational.

In other words, the structural bound is at rules (1) ∧ (2) ∧ (3); the tier_pin row is a defense-in-depth layer at the audit-trail-completeness axis. Erosion at the tier_pin layer does not propagate to substrate ↔ methodology class-conflation; it only widens the visibility gap between the methodology F-image and the audit-floor F-image. This is a real but bounded structural cost.

### 3.4 The W9c-1 vs W5-7 pattern asymmetry

A subtle structural observation: W9c-1 (POSITIVE) was the FIRST SCHEMATIC-helper-consuming gate to emit the tier_pin row (`substrate-first-canonical-sourcing.md` lines 96, 136, 224 — multiple cross-references). The tier_pin row was created by W9c-1's authoring discipline; it became the canonical model PRECEDING the rule-file codification at S88 W7b-83. The W5-7 PARTIAL-POSITIVE emission at S89 came AFTER the rule-file MANDATORY-K=4 promotion but BEFORE the 3-class taxonomy extension at S90 W1-9. The W5-7 producing script's OPERATIONAL DEVIATION docstring at lines 23-39 explicitly cites the K=4 MANDATORY level-pin discipline and demonstrates upgrade-path awareness ("S90 retry with the canonical W7a-74 PRIMARY evaluator script for proper FULL-tier evaluation"). This is a script that READ the rule and structurally committed to the substrate-side compliance, but had not yet absorbed the tier_pin row convention because the convention was a single-instance precedent at the time (W9c-1, S87), not an explicit rule-file MANDATORY clause.

**Structural reading**: the W5-7 omission is HISTORICAL, not normative. The W1-9 retroactive PARTIAL-POSITIVE classification correctly canonicalizes the W5-7 emission as substrate-side-compliant + methodology-floor-incomplete WITHOUT requiring W5-7 to be re-emitted with a corrective Option-A `supersedes` tag. The W5-7 verdict PASS substrate-physics integrity (Reading-A WIN at N=4/5 anchor-consistent rank-ordering) is preserved; the PARTIAL-POSITIVE class is a structural-classification overlay, not a substrate-physics correction.

### 3.5 Connes verdict on (b)

**W5-7 PARTIAL-POSITIVE pinning is structurally sound.** The W5-7 emission honors rules (1) ∧ (2) ∧ (3) at the substrate-side F-image; the missing tier_pin row is a methodology-floor disclosure gap that does NOT propagate to substrate ↔ methodology class-conflation. The structural bound on erosion is rules (1) ∧ (2) ∧ (3) remaining MANDATORY at K_substantive ≥ 3, which the W1-9 extension explicitly preserves. The erosion risk at the tier_pin axis is real but bounded; it warrants forward attention (see §6 on tier_pin promotion path) but does NOT require retraction of the PARTIAL-POSITIVE class or amendment of the W5-7 classification.

---

## 4. Adjudication question (c) — K-counter advancement validity

### 4.1 The advancement claim

The W1-9 extension advances K_substantive = 3 → K_substantive = 4 by adding W5-7 to the corpus. The four substantive instances are:

| # | Instance | Class | Reading |
|:-:|:---------|:------|:--------|
| 1 | W4-2 (S86) | NEGATIVE-CALIBRATION → Class-(d) | post-hoc disclosure only |
| 2 | W9b-2 (S87) | NEGATIVE-CALIBRATION → Class-(d) | docstring-only |
| 3 | W9c-1 (S87) | POSITIVE-CALIBRATION | full 4-of-4 disclosure |
| 4 | W5-7 (S89) | PARTIAL-POSITIVE | substrate-side compliant, tier_pin absent |

K_with_inheritance = 5 adds W5b-2 sub-test (c) as the inheritance-locus EXEMPT entry (the producing script does not import the SCHEMATIC module; W9c-1 cross-references it as derivational context).

**Status preservation claim**: K_substantive = 4 ≥ K_promotion = 3 per `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold ⇒ MANDATORY status preserved.

### 4.2 Does K-counter advancement validity hold?

I evaluate against three structural checks.

**Check 1 — K_promotion threshold satisfaction.** The threshold K_promotion = 3 is satisfied at K_substantive = 4. Status MANDATORY (binary above-threshold gate) is preserved. **PASS**.

**Check 2 — Distinct calibration-instance independence.** The four instances are structurally distinct under the calibration-corpus discipline:
- W4-2 vs W9b-2 vs W9c-1 are already structurally distinct per `substrate-first-canonical-sourcing.md` lines 132-137 table (different producing scripts; different convention tags; different docstring acknowledgment status; different compliance classes pre-MANDATORY-promotion).
- W5-7 is structurally distinct from all three: different session (S89 vs S86/S87); different producing script (`s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py`); different convention tag (`lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4-SCHEMATIC`); FIRST instance of PARTIAL-POSITIVE compliance class (structurally novel 2-bit signature (T, F)).
- All four instances inhabit the same parent SCHEMATIC level-pin discipline at `substrate-first-canonical-sourcing.md §(iv)`. The K-counter is correctly counted at the rule-level corpus axis, not at sub-rule axis.

**PASS** on instance independence.

**Check 3 — Algebra-axis orthogonality preservation.** This is the load-bearing check. Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-at-K=3, the algebra-INVARIANT spectrum-only-functional family (spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)`) and the algebra-DEPENDENT state-pair-functional family (state-pair functionals on `A`) are STRUCTURALLY ORTHOGONAL. The adjudication question (c) asks: does the structurally-intermediate PARTIAL-POSITIVE class admit at K=4 WITHOUT altering the algebra-axis orthogonality between rules (1)-(3) substrate-side and tier_pin row methodology-floor side?

The substrate-side compliance check rules (1) ∧ (2) ∧ (3) operate at the methodology F-image of substrate-IS regulator-class structure — this is a methodology-side reflection of an algebra-INVARIANT property (the substrate's regulator-class membership is a spectrum-side property of `D_K`, independent of which state on `A_K` is being evaluated). The tier_pin row operates at the audit-floor F-image — this is an audit-trail completeness disclosure that names the same algebra-INVARIANT regulator-class at the verdict-file layer.

**Both rules (1)-(3) and the tier_pin row are downstream F-images of the SAME substrate-IS algebra-INVARIANT predicate.** They are NOT positioned on opposite sides of the algebra-axis orthogonality. The algebra-axis orthogonality applies to two structurally-distinct functional families (algebra-INVARIANT spectrum-only vs algebra-DEPENDENT state-pair); the W1-9 extension does not introduce a state-pair functional, nor does it cross any algebra-axis cell boundary. The 4-corner classification at `permanent-results-registry.md §VII.U.2` (Corner I/II/III/IV per algebra-INVARIANT × Mellin-pole partition) is invariant under the W1-9 PARTIAL-POSITIVE addition; the corpus members W4-2 / W9b-2 / W9c-1 / W5-7 each live in their own §VII corner cells (their cell assignments are independent of the W1-9 extension), and the W1-9 extension does NOT promote a new cross-corner co-primary anchor structure.

**PASS** on algebra-axis orthogonality preservation.

### 4.3 What the K-counter advancement structurally accomplishes

The K_substantive = 3 → 4 advancement does two things simultaneously:

1. **Corpus-coverage strengthening**: adds the PARTIAL-POSITIVE compliance class to the corpus, increasing the rule's discriminating power across the 2-bit signature square. Pre-W1-9 the corpus had only POSITIVE (W9c-1) and NEGATIVE (W4-2 / W9b-2); the rule could classify all gates but only into two extreme bins. Post-W1-9 the corpus has all three bins POSITIVE / PARTIAL-POSITIVE / NEGATIVE, giving the rule a structurally-intermediate intermediate bin for substrate-side-compliant + audit-trail-incomplete gates.

2. **Status preservation via threshold-margin widening**: K_substantive = 4 sits at +1 margin above K_promotion = 3. Pre-W1-9 K_substantive = 3 was exactly at threshold (margin 0). The advancement adds margin for future calibration-instance demotion (e.g., if a future audit re-classifies a calibration-instance to a different class, the corpus can absorb the demotion without falling below K_promotion). This is the same defense-in-depth as the rule-file's K_with_inheritance = 5 counter at +2 margin above threshold.

Both effects are structurally beneficial. The advancement validity holds at all three checks.

### 4.4 Substitution chain verification (per `math-scripts.md §"Double-Check Logic Before Compute"`)

Per the rule, K-counter advancement claims require explicit substitution chains. The W1-9 substitution chain at `substrate-first-canonical-sourcing.md` lines 193-216:

```
Definitions:
  K_substantive       = count of distinct calibration-corpus instances of
                        SCHEMATIC level-disclosure pathology that count toward
                        the substantive level-pin discipline (positive +
                        negative + partial-positive)
  K_with_inheritance  = K_substantive + inheritance-locus instances
  K_promotion         = 3 per feedback_rules-compensate-missing-structure.md

Pre-S90-W1-9 state:
  K_substantive       = 3   (W4-2 NEGATIVE, W9b-2 NEGATIVE, W9c-1 POSITIVE)
  K_with_inheritance  = 4   (substantive 3 + W5b-2 inheritance-locus 1)
  Status              = MANDATORY (since K_substantive=3 ≥ K_promotion=3)

S90-W1-9 advancement:
  + Add W5-7 (S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY) PARTIAL-POSITIVE
  K_substantive       = 4   (W4-2, W9b-2, W9c-1, W5-7)
  K_with_inheritance  = 5   (substantive 4 + W5b-2 inheritance-locus 1)
  Status              = MANDATORY preserved (K_substantive=4 ≥ K_promotion=3)
  Sub-status          = PARTIAL-POSITIVE class admissible from S90 forward
                        (admissibility band ADVISORY S2; tier_pin row
                        forward-recommended-not-mandatory)
```

The substitution chain is dimensionally consistent (K-counter is integer-valued; threshold comparison is binary above-or-at-threshold). Step 4 direction (MANDATORY preserved iff K_substantive ≥ K_promotion) is canonical. The substitution chain matches the explicit conventions at `feedback_rules-compensate-missing-structure.md`. **VERIFIED**.

### 4.5 Connes verdict on (c)

**K_substantive 3 → 4 + K_with_inheritance 4 → 5 advancement is valid. MANDATORY status correctly preserved. Algebra-axis orthogonality NOT compromised — the W1-9 extension introduces a 2-bit signature partition entirely within the algebra-INVARIANT cell layer; no cross-axis structure is added. The advancement structurally strengthens the discipline's discriminating power at the corpus-coverage axis while preserving the substrate-side commutativity check baseline.**

---

## 5. Recommended verdict shape

Based on §§2-4, my recommended verdict shape for the W1-9 extension is:

**APPROVE (3-class taxonomy exhaustive + severity bands sound + K=4 advancement valid).**

Concretely:

1. The 2-bit signature partition (T,T) → POSITIVE / (T,F) → PARTIAL-POSITIVE / (F,*) → NEGATIVE is exhaustive over the {0,1}×{0,1} square; the (F,T) → NEGATIVE collapse is the substrate-correct routing (methodology-floor refinement cannot rescue substrate-side failure). No 4th class required.

2. The severity bands NO-ACTION (POSITIVE) / ADVISORY-S2 (PARTIAL-POSITIVE) / MANDATORY-S1 (NEGATIVE) are structurally sound under the substrate ↔ methodology F-image discipline. POSITIVE is full compliance and warrants no action. PARTIAL-POSITIVE encodes substrate-side compliance with methodology-floor incompleteness — ADVISORY-S2 is the correct severity for a gap that does NOT propagate to class-conflation but reduces audit-trail completeness. NEGATIVE encodes substrate-side non-compliance and routes through Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY at MANDATORY-S1; the severity matches the existing K=4 MANDATORY discipline for pre-W1-9 NEGATIVE instances.

3. The K_substantive 3 → 4 advancement is verified at the threshold-satisfaction, instance-independence, and algebra-axis-orthogonality-preservation checks. MANDATORY status preservation holds.

4. The W5-7 PARTIAL-POSITIVE pinning is structurally sound; the missing tier_pin row is a HISTORICAL omission (W5-7 was authored before the W1-9 codification of the 3-class taxonomy), not a normative pattern. The retroactive PARTIAL-POSITIVE classification preserves the W5-7 substrate-physics PASS (Reading-A WIN at N=4/5) while honestly encoding the methodology-floor gap.

5. The audit-script extension `detect_compliance_class` at `_substrate_first_provenance_audit.py` lines 220-327 correctly implements the 3-class partition with proper if/elif/else branch structure mapping signatures to classes. The 4-test driver T1-T4 confirms operational correctness on live + synthetic inputs.

**No amendment required.** No structural redesign needed. The verdict shape is APPROVE, with a forward-recommendation on tier_pin row promotion (see §6).

---

## 6. Forward-recommendation reading — tier_pin row promotion path

### 6.1 The forward-recommendation question

W1-9 records: "tier_pin row is forward-recommended-not-mandatory for PARTIAL-POSITIVE per W1-9 SUGGESTION K=1; future SCHEMATIC-helper-consuming scripts SHOULD emit `# tier_pin=TIER-2` to advance to POSITIVE — does connes endorse this forward-recommendation OR recommend MANDATORY promotion of tier_pin row across all PARTIAL-POSITIVE instances?"

### 6.2 Connes-side reading: STAGED PROMOTION (forward-recommended-not-mandatory NOW + structured pathway to MANDATORY at K_PARTIAL-POSITIVE = 3)

I do NOT recommend immediate MANDATORY promotion of the tier_pin row across all PARTIAL-POSITIVE instances at S91. I recommend a STAGED PROMOTION pathway analogous to the K-counter promotion threshold framework that produced the original §(iv) MANDATORY status at S88 W7b-83 close.

**Rationale 1 — K-counter discipline coherence.** The §(iv) rule itself was promoted SUGGESTION → MANDATORY at K=4 calibration corpus through three pre-instances (W4-2 SUGGESTION-K=1 at S86; W9b-2 + W9c-1 at S87 advancing K=3; W7b-83 retrospective extension to K=4 at S88). This is the canonical promotion pathway per `feedback_rules-compensate-missing-structure.md`. The tier_pin row promotion to MANDATORY at S91 with K_PARTIAL-POSITIVE = 1 would skip the staged-pathway discipline that the framework's own promotion convention establishes. Skipping the pathway introduces a Class-3 PROHIBITED_ACTIONS adjacency (post-hoc rewriting of pre-registered structure per `v3-closure-recovery.md`) — the tier_pin row was originally a single-instance precedent at W9c-1, not a pre-registered MANDATORY discipline; promoting it to MANDATORY without first hitting the K=3 threshold would be a methodology-floor convention promotion that does NOT respect the same promotion discipline applied to the substrate-side commutativity check.

**Rationale 2 — Structural symmetry with rules (1)-(3) MANDATORY at K=3.** The substrate-side commutativity check rules (1) ∧ (2) ∧ (3) became MANDATORY at K_substantive = 3 (W4-2 + W9b-2 + W9c-1 at S88 W7b-83 close, retroactively augmented to K=4 with W5b-2 inheritance-locus). The tier_pin row at the methodology-floor layer should achieve MANDATORY status via the SAME K=3 promotion mechanism: count distinct PARTIAL-POSITIVE calibration-corpus instances; at K_PARTIAL-POSITIVE = 3, promote tier_pin to MANDATORY across PARTIAL-POSITIVE class. This produces a structurally symmetric promotion pattern at the substrate-side and methodology-floor layers — both promotions are gated by K=3 distinct calibration instances at their respective compliance classes.

**Rationale 3 — Methodology-floor refinement is not structurally load-bearing.** Per §3.3 above, the tier_pin row is a defense-in-depth layer at the audit-trail-completeness axis, not a substrate-side commutativity predicate. The structural bound on substrate ↔ methodology class-conflation is rules (1) ∧ (2) ∧ (3); the tier_pin row's absence at PARTIAL-POSITIVE does NOT operationally permit class-conflation. Immediate MANDATORY promotion of tier_pin at K_PARTIAL-POSITIVE = 1 (i.e., with only the W5-7 instance) would treat a non-load-bearing refinement as load-bearing at the rule-file enforcement layer. This is a rule-file inflation pattern that `feedback_rules-compensate-missing-structure.md` explicitly warns against: rule bloat = missing structure; replace MANDATORY rules with examples + schemas where the underlying substrate-side commutativity is already structurally protected.

### 6.3 Concrete staged-promotion proposal

I propose the following promotion pathway, modeled on the §(iv) substrate-side promotion:

**Stage 1 (current; S90 W1-9 → S91)**: tier_pin row at PARTIAL-POSITIVE = SUGGESTION-K=1. W5-7 is the calibration instance. The rule text at `substrate-first-canonical-sourcing.md` line 118 already encodes this status correctly ("tier_pin row remains forward-recommended-not-mandatory for PARTIAL-POSITIVE; future SCHEMATIC-helper-consuming scripts SHOULD emit `# tier_pin=TIER-2` to advance to POSITIVE").

**Stage 2 (S91-S93+)**: As future SCHEMATIC-helper-consuming gates land at S91+, they enter the corpus at either POSITIVE (4-of-4 disclosure including tier_pin) or PARTIAL-POSITIVE (3-of-4 disclosure with tier_pin omitted). Distinct PARTIAL-POSITIVE instances advance K_PARTIAL-POSITIVE 1 → 2 → 3. At K_PARTIAL-POSITIVE = 3 distinct PARTIAL-POSITIVE calibration instances, the tier_pin row promotes SUGGESTION → MANDATORY at the methodology-floor layer.

**Stage 3 (post-promotion event)**: tier_pin row becomes MANDATORY for PARTIAL-POSITIVE-class emissions. The audit-script `detect_compliance_class` is amended to escalate severity ADVISORY-S2 → MANDATORY-S1 on (T, F) signature (i.e., PARTIAL-POSITIVE collapses to NEGATIVE post-promotion at the (T, F) signature). At this stage, the 3-class taxonomy structurally collapses to the original 2-class (POSITIVE / NEGATIVE) at the rule-file enforcement level, BUT the historical PARTIAL-POSITIVE instances (W5-7 + future ones landed pre-promotion) remain GRANDFATHERED with their post-hoc disclosure preserved per the W4-2 NEGATIVE-CALIBRATION grandfathering precedent.

This staged pathway respects the framework's own promotion discipline at every step. The S91 plan-freeze decision is simply to keep the current SUGGESTION-K=1 status and let the K-counter advance naturally as future PARTIAL-POSITIVE instances accumulate. No immediate rule-file edit needed.

### 6.4 Why staged promotion is structurally preferable

If we promote tier_pin to MANDATORY at S91 immediately (single-instance K_PARTIAL-POSITIVE = 1), three structural risks materialize:

**Risk 1 — Retroactive disqualification of W5-7.** W5-7 was emitted under the pre-W1-9 rule state where the tier_pin row was a single-instance precedent (W9c-1) without explicit MANDATORY-at-PARTIAL-POSITIVE status. Promoting tier_pin to MANDATORY at S91 would retroactively disqualify W5-7 from PARTIAL-POSITIVE class (W5-7 would collapse to NEGATIVE under the new MANDATORY status). Per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class-3, retroactive rewriting of pre-registered structure is FORBIDDEN. The W5-7 verdict line at `s89_gate_verdicts.txt:128` is verdict-permanent; its classification cannot be downgraded by a subsequent rule-file MANDATORY promotion unless the W5-7 producing script is re-emitted with corrective Option-A `supersedes` tag. Re-emitting W5-7 with a tier_pin row would be a Class-1 PROHIBITED_ACTIONS adjacency (convention-shopping to satisfy a post-hoc MANDATORY rule).

**Risk 2 — Calibration-corpus collapse.** Under immediate MANDATORY tier_pin promotion, the PARTIAL-POSITIVE class would have ZERO valid calibration instances (W5-7 retroactively disqualified per Risk 1; no other PARTIAL-POSITIVE instances exist as of S90 close). A 0-instance MANDATORY class is structurally undefined — it has no audit-corpus anchor to bind the rule text to operational reality.

**Risk 3 — Promotion pathway asymmetry.** Substrate-side rules (1) ∧ (2) ∧ (3) achieved MANDATORY at K_substantive = 3 distinct calibration instances; methodology-floor tier_pin row achieving MANDATORY at K_PARTIAL-POSITIVE = 1 would create an asymmetric promotion pattern that downstream readers cannot interpret consistently. Future rule-file readers asking "why did methodology-floor MANDATORY at K=1 while substrate-side MANDATORY at K=3" have no structural answer; the asymmetry communicates "the methodology-floor refinement is more important than the substrate-side commutativity" — which is the OPPOSITE of the substrate-first direction-of-explanation per `phononic-framing.md §"IS Space, Not IN Space"`.

All three risks are eliminated by the staged-promotion pathway at K_PARTIAL-POSITIVE = 3.

### 6.5 Connes verdict on (d)

**Forward-recommendation: ENDORSE the current SUGGESTION-K=1 status; recommend STAGED PROMOTION at K_PARTIAL-POSITIVE = 3.** Do NOT promote tier_pin row to MANDATORY at S91. Let the K-counter advance naturally as future PARTIAL-POSITIVE instances accumulate; promote SUGGESTION → MANDATORY at the K=3 threshold per the framework's own promotion discipline.

---

## 7. Substrate framing — direction of explanation

Per the assignment's substrate-framing reminder, I close with an explicit IS-not-IN check on the W1-9 extension.

**Direction of explanation flow** (FROM substrate → TOWARD emergent observables):

```
1. SUBSTRATE (D_K eigenvalue problem on Jensen-deformed SU(3)):
   the spectral triple (A_K, H_K, D_K) carries an intrinsic regulator-class
   structure on `Tr f(D_K^2/Λ^2)` — physical regularizations (Pauli-Villars,
   zeta, Mellin live-cone) vs SCHEMATIC analogs (Gaussian envelope, Casimir-
   bound interpolation, `_spectral_action_regulators.py` helpers).
   ↓
2. METHODOLOGY F-IMAGE (rules (1)-(3) at substrate-first-canonical-sourcing.md §(iv)):
   the substrate-side regulator-class membership is encoded at three structurally-
   distinct F-image loci: plan-block CLASS pin (rule 1); verdict-line `-SCHEMATIC`
   suffix (rule 2); script-docstring SCHEMATIC acknowledgment (rule 3).
   ↓
3. AUDIT F-IMAGE (tier_pin row + verdict-file canonical line):
   the audit-trail layer reads the methodology-floor disclosures and emits
   structural compliance verdicts (POSITIVE / PARTIAL-POSITIVE / NEGATIVE).
   The tier_pin row is an audit-trail completeness refinement at this layer.
   ↓
4. OBSERVED PHYSICS (consumer scripts at S91+):
   downstream gate dispatches consume the compliance-class verdict and route
   gate-level dispatch decisions per the severity band (NO-ACTION / ADVISORY-S2 /
   MANDATORY-S1) — gate-level dispatches are emergent from the substrate-physics
   compliance check at the F-image methodology layer.
```

The W1-9 extension is correctly positioned at the substrate → methodology F-image transition (the 2-bit signature partition operates on rules (1)-(3) at the methodology layer with a downstream audit-floor refinement). No container-thinking violations are detected in the W1-9 extension text. The PARTIAL-POSITIVE class is correctly framed as the methodology F-image of substrate-IS partial compliance, not as a substrate-side compliance class itself.

**Container-thinking checkpoint** — would a future reader interpret PARTIAL-POSITIVE as a substrate-side class? The rule text at `substrate-first-canonical-sourcing.md` line 126 explicitly disambiguates: "PARTIAL-POSITIVE is NOT a degraded POSITIVE — it is a structurally-distinct compliance class with its own admissibility band (ADVISORY S2 vs POSITIVE NO-ACTION vs NEGATIVE MANDATORY S1)." The classes are at the methodology-floor compliance-band layer, not at the substrate-IS layer. The direction-of-explanation flows substrate → methodology → audit; the W1-9 extension respects this flow. **Substrate-framing PASS.**

---

## 8. Conclusions

| Adjudication question | Connes verdict |
|:----------------------|:---------------|
| (a) Is the 3-class partition exhaustive? Does (F,T) → NEGATIVE collapse correctly? | **YES + YES.** Partition exhaustive over 2-bit square; (F,T) → NEGATIVE is substrate-correct routing. No 4th class needed; redundant with Class-(d) PIN-DERIVATIVE. |
| (b) Is the W5-7 PARTIAL-POSITIVE pinning structurally sound? | **YES.** Substrate-side rules (1)∧(2)∧(3) compliance preserved; missing tier_pin is a HISTORICAL omission (W5-7 emitted pre-W1-9 codification); erosion is structurally bounded by MANDATORY rules (1)-(3). |
| (c) Does K_substantive 3 → 4 + K_with_inheritance 4 → 5 preserve MANDATORY status correctly? | **YES.** Threshold satisfaction (K_substantive=4 ≥ K_promotion=3); instance independence verified; algebra-axis orthogonality preserved (W1-9 operates entirely within algebra-INVARIANT cell layer). |
| (d) Forward implication on tier_pin row promotion | **ENDORSE current SUGGESTION-K=1 status; recommend STAGED PROMOTION at K_PARTIAL-POSITIVE = 3, NOT immediate MANDATORY promotion at S91.** Immediate promotion would retroactively disqualify W5-7 (Class-3 PROHIBITED_ACTIONS adjacency), create 0-instance MANDATORY class, and produce K-counter asymmetry vs substrate-side rules. |

### Overall verdict shape

**APPROVE** — 3-class taxonomy exhaustive + severity bands sound + K=4 advancement valid; no amendment required to the W1-9 extension at S91. Forward-recommendation: maintain SUGGESTION-K=1 status on tier_pin row promotion path; advance K_PARTIAL-POSITIVE naturally through future calibration instances; promote to MANDATORY only at K_PARTIAL-POSITIVE = 3 per the framework's own K-counter promotion discipline.

### Cross-link to algebra-axis orthogonality

The W1-9 extension respects the algebra-axis orthogonality MANDATORY-at-K=3 discipline at `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`. The 4 corpus members (W4-2 / W9b-2 / W9c-1 / W5-7) each occupy their own §VII corner cells per `permanent-results-registry.md §VII.U.2` 4-corner partition; the W1-9 PARTIAL-POSITIVE classification does NOT introduce a new cross-corner co-primary anchor structure (FORBIDDEN per `cross-pillar-bridge-anatomy.md §"Mandatory at plan-freeze"` clause 2). The substrate-side rules (1)-(3) and methodology-floor tier_pin row are both F-images of the SAME algebra-INVARIANT spectrum-only-functional family (regulator-class membership); no algebra-axis crossing is introduced. **Orthogonality PRESERVED.**

### Cross-link to phononic-framing

Per `phononic-framing.md §"IS Space, Not IN Space"`, the direction of explanation flows substrate → methodology F-image → audit F-image → observed physics. The W1-9 extension respects this direction; no container-thinking violations detected. The PARTIAL-POSITIVE class is the methodology F-image of substrate-IS partial compliance, not a substrate-side class.

---

## 9. Carry-Forward (4-field spec per `feedback_fix-in-session-never-defer.md`)

### CF-S91-PARTIAL-POSITIVE-K-COUNTER-MONITORING

1. **What**: Monitor K_PARTIAL-POSITIVE counter across S91+ sessions; advance K_PARTIAL-POSITIVE counter by 1 for each new distinct calibration-corpus instance landing in PARTIAL-POSITIVE class (rules (1)∧(2)∧(3) PASS + tier_pin row ABSENT signature (T,F)). At K_PARTIAL-POSITIVE = 3 distinct instances, promote tier_pin row from SUGGESTION → MANDATORY at PARTIAL-POSITIVE class per `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold. NO immediate MANDATORY promotion at S91 (single-instance K=1 promotion would retroactively disqualify W5-7 + create 0-instance MANDATORY class — both Class-3 PROHIBITED_ACTIONS adjacencies per `v3-closure-recovery.md`).

2. **Inputs**:
   - `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` 3-class taxonomy sub-section (current SUGGESTION-K=1 status text);
   - `computations/_shared/_substrate_first_provenance_audit.py:220-327` `detect_compliance_class` function (consumer for the future S91+ K-counter monitoring);
   - `computations/_shared/s90_w1_partial_positive_audit_test.py` 4-test driver (will be extended at K_PARTIAL-POSITIVE = 3 promotion event to escalate severity ADVISORY-S2 → MANDATORY-S1);
   - Future S91+ verdict-file emissions tagged at PARTIAL-POSITIVE class (consumer audit identifies these via `detect_compliance_class` post-emission scan).

3. **Gate** (proposed S91+ gate ID at promotion event): `S{N}-PARTIAL-POSITIVE-K-COUNTER-PROMOTE-MANDATORY` with PASS criterion:
   - 3 distinct PARTIAL-POSITIVE calibration-corpus instances landed across S91-S{N};
   - rule-file edit at `substrate-first-canonical-sourcing.md §(iv)` 3-class taxonomy sub-section landing the MANDATORY promotion text;
   - `detect_compliance_class` function amended at `_substrate_first_provenance_audit.py` to escalate (T,F) → severity MANDATORY-S1 (collapse PARTIAL-POSITIVE to NEGATIVE at the audit-script level);
   - W5-7 + other pre-promotion PARTIAL-POSITIVE instances GRANDFATHERED per the W4-2 NEGATIVE-CALIBRATION grandfathering precedent (preserve post-hoc disclosure; no retroactive disqualification of pre-promotion verdict lines).

4. **Effort**: ~0.2 we (one METHODOLOGY-class wave at the promotion event; mechanical rule-file extension + audit-script if/elif/else amendment + test-driver T4 synthetic matrix update + allowlist + instances rows append). Total wave-time ≈ 30-60 minutes orchestrator-direct-write. The carry-forward is OPTIONAL at S91-S{N-1}; FIRES at S{N} when K_PARTIAL-POSITIVE = 3 is reached.

### Carry-forward NOT issued (substrate-physics work)

I do NOT issue a carry-forward for re-emitting W5-7 with corrective Option-A `supersedes` tag. The W5-7 substrate-physics PASS (Reading-A WIN at N=4/5 anchor-consistent rank-ordering at substrate-distance-2 pole s=4) is structurally intact; the PARTIAL-POSITIVE classification is a methodology-floor classification overlay that does NOT alter the substrate-physics verdict. Re-emitting W5-7 would be a Class-1 PROHIBITED_ACTIONS adjacency (convention-shopping to satisfy a post-hoc-promoted MANDATORY rule). The W5-7 producing script's pre-existing forward note ("S90 retry with the canonical W7a-74 PRIMARY evaluator script for proper FULL-tier evaluation") is a separate substantive carry-forward queued for FULL-tier upgrade — it discharges via the FULL-physical-regularization route (Pauli-Villars at Λ_UV = M_KK), NOT via tier_pin row addition.

---

## 10. Provenance + signature

- **Solo synthesis author**: connes-ncg-theorist (Workhorse-NCG; independent reading per `/rclab-review --agents connes`).
- **Source documents read in full** (chunked at ≤200 lines per call where size required):
  1. `sessions/archive/session-90/session-90-w1-workingpaper.md` §W1-9 (lines 436-486; 51 lines);
  2. `sessions/session-plan/session-90-plan-w1.md` §W1-9 (lines 561-639; 78 lines);
  3. `.claude/rules/substrate-first-canonical-sourcing.md` (288 lines; full file; §(iv) 3-class taxonomy at lines 101-227);
  4. `computations/_shared/_substrate_first_provenance_audit.py` (394 lines; full file; `detect_compliance_class` at lines 220-327);
  5. `computations/_shared/s90_w1_partial_positive_audit_test.py` (462 lines; full file; T1-T4 at lines 129-334);
  6. `computations/session-89/s89_gate_verdicts.txt` (W5-7 verdict line 128 + companion rows 129-130);
  7. `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (lines 347-378).
- **No verdict-line emission**: solo synthesis per `/rclab-review` semantics; no audit_sha256, no s90_gate_verdicts.txt append.
- **Forward consumer**: S91 plan-freeze decisions on (a) maintaining current 3-class taxonomy text + SUGGESTION-K=1 status; (b) NOT promoting tier_pin row to MANDATORY at S91; (c) adopting the proposed K_PARTIAL-POSITIVE K-counter staged-promotion pathway at K=3 threshold.
- **Cross-link target**: `sessions/archive/session-90/session-90-w1-workingpaper.md §W1-9 (i) Carry-forward` may be updated to cite this synthesis as the connes-side parallel-review owe discharge (orchestrator-direct-write at session-close synthesis if applicable).
