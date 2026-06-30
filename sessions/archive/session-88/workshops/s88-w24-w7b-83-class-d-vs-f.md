# Session 88 W24 Synthesis: §W7b-83 SCHEMATIC Level-Pin K=4 Corpus Shape — Class-(d) vs Class-(f) and MANDATORY-as-Corrective vs MANDATORY-as-Confirmatory Adjudication

**Date**: 2026-05-07
**Agent**: sagan-empiricist (solo synthesis)
**Source Documents**:
- `sessions/archive/session-88/session-88-w7b-workingpaper.md` (606 lines; §W7b-83 lines 384–500 + sagan adversarial subsection lines 483–498 + team-lead synthesis lines 518–522 + Constraint-Map line 585)
- `sessions/session-plan/session-88-plan-w7b.md` (lines 512–625 — §W7b-83 plan-block)
- `sessions/archive/session-88/workshops/_seed-w7b.md` (Workshop 2 lines 26–38)
- `.claude/rules/substrate-first-canonical-sourcing.md` §(iv) (post-§W7b-83 MANDATORY-status edits)
- `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" Class-(d) and Class-(f) definitions
- `.claude/rules/regulator-pin-discipline.md` §"Cross-link — K=4 SCHEMATIC level-pin promotion (S88 W7b-83, MANDATORY)"
- `computations/_shared/_spectral_action_regulators.py` lines 1–31 (SCHEMATIC docstring; verbatim cite of S61/S78 Pauli-Villars FULL physical regularization)

---

## I. Session Outcome

**Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY wins on W4-2 + W9b-2; K_substantive = 3 is the structurally honest corpus count; MANDATORY-as-corrective is the structurally honest framing.** The substrate-canonical FULL physical regularization for both witnesses exists and is verbatim-cited in `_spectral_action_regulators.py` docstring lines 23–28 ("the S61/S78 Pauli-Villars pipeline"); under the epistemic-discipline.md Class-(d) literal definition this satisfies "pin is a derived form of a primary canonical." D_max measurement on the W4-2 instance is `1.119 OOM`, placing both W4-2 and W9b-2 in the MANDATORY remediation band `[1.0, 3.0)` — confirmed against sagan's WP-§W7b-83 calculation. The §W7b-83 PASS verdict on its own pre-registered threshold is correct and remains so under reclassification; the audit_sha256 = `d825b8301aa929c2…` and the SUGGESTION → MANDATORY level-pin promotion stand. What changes is the rule-file taxonomy: the post-§W7b-83 entries in `substrate-first-canonical-sourcing.md §(iv)` and `epistemic-discipline.md §"Source Reconciliation"` Class-(f) corpus need targeted edits to (i) reclassify W4-2 + W9b-2 as Class-(d) instances, (ii) carry both K_substantive=3 and K_with_inheritance=4 explicitly, and (iii) state the 1/3 substantive compliance rate as the corrective context the K=4 promotion responded to.

---

## II. Key Results

### Result 1 — Class-(d) classification of W4-2 + W9b-2 (substrate-canonical FULL exists by literal docstring cite)

**Result**: Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY for W4-2 + W9b-2 (NOT Class-(f) PIN-PLACEHOLDER). NON-PHONONIC (rule-file taxonomy adjudication; substrate framing applies via the level-pin discipline's substrate-IS interpretation, but the adjudication itself is methodology-floor).

The Class-(d) literal definition at `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" reads: **"PIN-DERIVATIVE-VS-SOURCE-PRIMARY — pin is a derived form of a primary canonical"**, with remediation **"verify derivation chain; ratio check against source primitives; algebraic-equivalence audit at plan-authorship per Class 8.3 item 5"**. The Class-(f) literal definition reads: **"PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL — the plan pin is given as a textual approximation, order-of-magnitude estimate, or placeholder string AND a substrate-first canonical exists (or could be computed) for the same quantity"**, with remediation **"query knowledge MCP for canonical; substitute into plan PIN VALUE field; HARD-HALT at D_max ≥ 3.0"**.

The discriminating test is: *does a substrate-first canonical exist*, and *what form does the pin take in the producing script*. For both W4-2 and W9b-2 the answers are unambiguous. The substrate-first canonical exists — `_spectral_action_regulators.py` docstring lines 23–28 read verbatim: *"These are SCHEMATIC regulators — intended as reasonable pure-spectrum analogs of the named regulators in Chamseddine-Connes 1996 §2.2-2.3 (Mellin moments f_0, f_2, f_4 of the cutoff function f restricted to [0, infty)). They are NOT the full physical regularizations used in the S61/S78 Pauli-Villars pipeline (which uses Lambda_UV = M_KK as the physical cutoff)."* The schematic helpers are EXPLICITLY DERIVED forms whose primary canonical the docstring names (S61/S78 PV pipeline at Λ_UV = M_KK). The pin form in the producing scripts is NOT a textual approximation, NOT an OOM estimate, NOT a placeholder string — it is a numerical output of a deterministic helper function (`zeta_a_n`, `mellin_a_n`, etc.) consumed downstream. This pattern matches Class-(d) by definition; it does NOT match Class-(f) by definition (no placeholder pattern is present; the pin VALUE FIELD does NOT carry `O(10^?)`, `≈`, `~`, `placeholder`, `TBD`, `pending`, `analytic estimate`, or `rough estimate`).

Connes-ncg's "Class-(f) hand-off triage" framing — "level placeholder; substrate-canonical exists in form of full-physical regularization re-run" (WP §W7b-83 line 422) — conflates two distinct senses of "placeholder." Class-(f) requires the PIN to be the placeholder (textual approximation in the value field); the docstring's CLASS labeling ("SCHEMATIC analogs ... NOT the full physical regularizations") is a level-tag on the helper module, not a placeholder pattern in any pin VALUE FIELD. The connes-ncg framing equivocates the level-tag with a placeholder; the literal Class-(f) detection-pattern set (`O\(10\^?-?\d+\)`, `≈ ...`, `~ 10\^?-?\d+`, `placeholder`, `TBD`, `pending`, `analytic estimate`) does not match anywhere in the W4-2 or W9b-2 producing scripts. Sagan's classification stands: Class-(d), not Class-(f).

### Result 2 — D_max = 1.119 OOM on W4-2 instance (MANDATORY band)

**Result**: D_max(W4-2) = 1.119 ≈ 1.13 OOM ∈ [1.0, 3.0) → MANDATORY remediation band. NON-PHONONIC (severity-band measurement against a methodology-floor 4-band calibration).

The substitution chain for sagan's claim that the W4-2 instance lies in the MANDATORY band:

```
Step 1 (Definition):
  D_max = |log10(SCHEMATIC_value) − log10(FULL_PHYSICAL_value)|
  per epistemic-discipline.md §"Source Reconciliation" 4-band calibration
  with bands {<0.1 NO-ACTION; [0.1, 1.0) ADVISORY; [1.0, 3.0) MANDATORY; ≥3.0 HARD-HALT}.

Step 2 (Substitution at the W4-2 P5 multiplier):
  SCHEMATIC_value = M_F2(s=3) = 1.581e-1
    [W4-2 P5 Mellin-via-_spectral_action_regulators schematic helper]
  FULL_PHYSICAL_value = M_Zub(s=3) = 1.201e-2
    [W4-2 P5 Zubarev-via-S61/S78-PV proxy at the same s argument; closest published
     full-physical multiplier in the W4-2 sub-test record at session-86-w4-workingpaper.md:513]

Step 3 (Simplify):
  log10(1.581e-1) = -0.80125...
  log10(1.201e-2) = -1.92047...
  D_max = |(-0.80125) − (-1.92047)| = 1.11922 OOM

Step 4 (Direction-of-band assignment):
  1.0 ≤ 1.11922 < 3.0 ⇒ band = MANDATORY (4-band calibration row 3)

Conclusion: W4-2 instance lies in the MANDATORY remediation band; sagan's
            "1.13 OOM" rounded form is correct (1.119 → 1.13 at 3 sig figs).
            Severity tag = MANDATORY. Confirmed.
```

The W9b-2 D_max value is not directly enumerated in the WP §W7b-83 audit table (sagan's adversarial subsection notes only "D_max in same band as #1; regulator-class spread ≈ 381× per S75 → log10 ≈ 2.58 across atlas, but per-instance multiplier-class jump ~1.0–1.2 OOM"). The S75 ZETA-NOT-PHYSICAL-75 calibration spread of 381× across the regulator atlas yields log10(381) = 2.581 as the upper-bound atlas spread, but the per-instance schematic-vs-physical jump for W9b-2 sits in the same `~1.0–1.2 OOM` band as W4-2 by structural analogy (both are Mellin/zeta-class schematic helpers consumed at substrate-distance-1 pole indices; the underlying schematic-vs-physical distinction is the same SU(3) Casimir spectrum analog vs full PV pipeline at Λ_UV = M_KK). A direct measurement of W9b-2 D_max requires a per-witness compute (CF entry V.2 below); under the structural-analogy argument, classifying W9b-2 in the same MANDATORY band as W4-2 is the operating assumption, with the explicit measurement queued.

### Result 3 — K_substantive = 3 vs K_with_inheritance = 4: corpus-shape distinction is structurally honest

**Result**: K_substantive = 3 (W4-2 + W9b-2 + W9c-1) is the count of producing scripts that import `_spectral_action_regulators` AND have a downstream verdict line; K_with_inheritance = 4 adds W5b-2 sub-test (c) as a derivational-context pointer that does NOT consume the schematic module. Both numbers cross the K_promotion = 3 threshold; SUGGESTION → MANDATORY promotion is structurally justified under either count. The honest disclosure is to carry both numbers in the rule-file calibration corpus. NON-PHONONIC (corpus-shape adjudication for K-counter promotion thresholds).

The §W7b-83 audit table (WP lines 407–412) records `script_imports_schematic_module` per witness as `Y / Y / Y / N` for the four rows. Connes-ncg's substitution chain (WP lines 433–447) counts all four as `→ 1`, summing to K = 4. Sagan's adversarial subsection (WP line 494) flags this: "Including this row in K=4 is a structural stretch ... K_corpus_substantive = 1 POSITIVE (W9c-1) + 2 NEGATIVE on rule-(2) (W4-2, W9b-2) + 1 EXEMPT (W5b-2) = 3 substantive instances + 1 inheritance-locus."

The structural reading: a calibration-corpus instance for the SCHEMATIC level-disclosure pathology requires (i) the producing script consumes the schematic helper, AND (ii) a verdict line exists with a `convention=` field that either does or does not carry the `-SCHEMATIC` suffix. W5b-2 sub-test (c) fails (i) by construction (`script_imports_schematic_module=False` per the audit .npz); it cannot exhibit the pathology of "silent SCHEMATIC consumption" because it does not consume SCHEMATIC. It enters the corpus only by indirection: W9c-1's POSITIVE-CALIBRATION cross-review references W5b-2 sub-test (c) for derivational context. That is a legitimate cross-reference, but it is structurally distinct from the calibration-instance role.

The K-counter under `feedback_rules-compensate-missing-structure.md` advances on structural-distinct calibration instances. K_substantive = 3 reaches the K_promotion = 3 threshold exactly; K_with_inheritance = 4 reaches it with one row of reserve. The promotion direction (SUGGESTION → MANDATORY) is unaffected — either count crosses the threshold. The substantive difference is downstream: the rule-file's calibration corpus table is a data structure that downstream consumers (registry rows, plan-freeze auditors, knowledge-MCP indexing, cross-session synthesis) read as authoritative. A 4-row table that conflates "consumes SCHEMATIC + has pathology" with "exists in structural context near the pathology" misrepresents the corpus shape; subsequent K-counter advances will need 1 more or 2 more substantive instances depending on which count is canonical for the next K-promotion threshold.

### Result 4 — MANDATORY-as-corrective is the structurally honest framing

**Result**: 1/3 substantive compliance rate (W9c-1 alone carries the `-SCHEMATIC` suffix in the verdict-line `convention=` field; W4-2 and W9b-2 have docstring-only acknowledgment without operational disclosure). The MANDATORY promotion is the corrective response to a discovered pathology, not a confirmation of pre-existing maturity. NON-PHONONIC (epistemic-status framing of a methodology-floor rule).

Sagan's adversarial commentary (WP lines 497–498) reads, verbatim: "Silent consumption persists despite the formal disclosure pattern, in 2 of 3 substantive witnesses. ... labeling the K=4 corpus as a victory of the level-pin discipline overstates the case: it is the discovery of a PROBLEM at three sites, with one compliant exemplar — closer to '1 success + 2 failures + 1 exempt = K=4 surfaces the pathology' than 'K=4 calibration confirms the discipline is mature.' The MANDATORY promotion is therefore well-motivated PRECISELY BECAUSE compliance is the exception (1/3) rather than the norm — a point that should be stated plainly in the rule-file edit rather than buried in a positive-calibration framing."

The connes-ncg framing in the post-§W7b-83 rule-file edits at `substrate-first-canonical-sourcing.md §(iv)` headlines W9c-1 as the POSITIVE-CALIBRATION model (Instance #3 in the calibration corpus table) and frames the MANDATORY status as the discipline maturing. This is technically correct (MANDATORY is what the rule-file now is, and W9c-1 is the model future S88+ gates SHOULD pattern-match), but the framing buries the discovery: the audit surfaced silent-consumption in 2/3 substantive sites; that is the structural fact the K=4 promotion responds to.

This matters operationally for two downstream consumers. First, the `_source_reconciliation_audit.py` severity-band emission for SCHEMATIC-helper-consuming gates depends on what classification the calibration corpus carries: under Class-(d) MANDATORY tags on W4-2 + W9b-2 (the corrective reading), forward S89+ gates that consume those scripts' outputs as canonicals inherit MANDATORY remediation status, requiring a derivation-chain audit (Class-(d) remediation) rather than a placeholder-substitution (Class-(f) remediation). Under the connes-ncg Class-(f) confirmatory reading, those same gates would inherit ADVISORY or MANDATORY status only if the substrate-canonical were re-run and the re-run value differed from the schematic by ≥ 1.0 OOM; absent the re-run, the placeholder framing implies the schematic IS the operating canonical. Second, the rule-file precedent matters for future K-counter advancements: corrective framing makes the threshold sensitive to discovered pathology; confirmatory framing makes it sensitive to compliance accumulation. The two routes diverge in their forward enforcement posture.

### Result 5 — UV-regulator vs Level pin orthogonality survives reclassification (no diff to regulator-pin-discipline.md 2-axis table)

**Result**: The UV-regulator pin axis (`a_n^{ζ}`, `a_n^{Pauli-Villars}`, `a_n^{Mellin}`, `a_n^{lattice}`, `a_n^{cutoff}`) and the Level pin axis (FULL vs SCHEMATIC) remain structurally orthogonal under sagan's K_substantive=3 + Class-(d) reclassification. NON-PHONONIC (cross-rule taxonomy invariance check).

The regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion" 2-axis table partitions the silent-class-conflation pathologies into two non-redundant axes:

| Axis | Pin form | Closes |
|:-----|:---------|:-------|
| UV-regulator axis | `a_n^{ζ}`, `a_n^{Pauli-Villars}`, `a_n^{Mellin}`, `a_n^{lattice}`, `a_n^{cutoff}` | UV-regulator silent class-conflation (S75 ZETA-NOT-PHYSICAL-75 substrate) |
| Level axis | `convention=...-SCHEMATIC` suffix + CLASS pin (FULL/SCHEMATIC) + `tier_pin=TIER-2` companion | SCHEMATIC vs FULL physical silent class-conflation |

Both pins MUST be carried in the verdict-line `convention=` field; a producing script that correctly tags `a_n^{Mellin}` (regulator-pin compliant) while consuming the SCHEMATIC `_spectral_action_regulators.py` Mellin helper (level-pin violator) FAILs the level-pin audit even though it PASSes the regulator-pin audit. The two axes ARE structurally orthogonal — they close non-redundant pathways — and this orthogonality DOES NOT depend on whether the level-axis pathology is classified as Class-(d) or Class-(f), nor on whether K_substantive=3 or K_with_inheritance=4. Both classifications and both counts agree that the level-pin discipline is MANDATORY at plan-freeze and that BOTH pins must be carried; the orthogonality structure is invariant under the reclassification. No diff to the regulator-pin-discipline.md 2-axis table is required.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W7b-83 `S88-W7-LF-E-SCHEMATIC-MODULE-AUDIT` | PASS (audit_sha256=`d825b8301aa929c2…`) | K=4 ≥ K_promotion=3; positive_disclosure=1/3; negative_disclosure=2/3 |
| Adjudication on Class-(d) vs Class-(f) classification of W4-2 + W9b-2 | Class-(d) wins (this synthesis) | substrate-canonical FULL exists per `_spectral_action_regulators.py` docstring lines 23–28; pin form is helper-output, not placeholder pattern |
| Adjudication on K_substantive vs K_with_inheritance | Both counts disclosed (this synthesis) | K_substantive=3 (W4-2 + W9b-2 + W9c-1); K_with_inheritance=4 (adds W5b-2(c) inheritance-locus); both ≥ K_promotion=3 |
| Adjudication on MANDATORY-as-corrective vs MANDATORY-as-confirmatory | Corrective (this synthesis) | 1/3 substantive compliance rate; 2/3 silent-consumption discovered; MANDATORY responds to pathology, not maturity |

The §W7b-83 PASS verdict from the WP is authoritative and remains so. The adjudications above are rule-file taxonomy decisions whose outputs are diffs to `substrate-first-canonical-sourcing.md §(iv)` and `epistemic-discipline.md §"Source Reconciliation"`; they do not contradict the §W7b-83 PASS verdict.

---

## IV. Structural Implications

### IV.1 Constraint-map update — W4-2 + W9b-2 reclassified Class-(f) → Class-(d)

The post-§W7b-83 calibration-corpus extension at `epistemic-discipline.md §"Source Reconciliation"` Class-(f) currently lists W4-2 + W9b-2 as Class-(f) PIN-PLACEHOLDER instances (per the connes-ncg hand-off triage). Under this synthesis they reclassify to Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY. The WP §W7b-83 Constraint-Map Update line 585 (2026-05-05, sagan adversarial) already adopts this reclassification at the WP layer; the rule-file diff (this synthesis's primary output) propagates it to the canonical taxonomy. Class-(f) corpus retains W5b-2 sub-test (c) only as a CALIBRATION-LOCUS-EXEMPT row (does not consume schematic helper); W9c-1 retains POSITIVE-CALIBRATION status with no class assignment.

### IV.2 Constraint-map update — calibration-corpus table at `substrate-first-canonical-sourcing.md §(iv)` carries both K-counts

The 4-row calibration-corpus table at `substrate-first-canonical-sourcing.md §(iv)` (post-§W7b-83 promotion) currently presents K=4 as a single number. The honest disclosure is to add a sub-clause distinguishing K_substantive=3 (substantive calibration instances; W4-2 + W9b-2 + W9c-1) from K_with_inheritance=4 (adds W5b-2 sub-test (c) inheritance-locus). Both numbers cross the K_promotion=3 threshold; the SUGGESTION → MANDATORY promotion stands. Forward K-counter advancements will read whichever count is canonical at advancement time; the dual disclosure prevents ambiguity at the next K-promotion threshold.

### IV.3 Constraint-map update — `_source_reconciliation_audit.py` severity-band emission protocol

The audit script `computations/_shared/_source_reconciliation_audit.py` (S86 W0a-2; pre-S88 architecture) routes Class-(d) and Class-(f) detections to different remediation paths. Under the Class-(d) reclassification of W4-2 + W9b-2, S89+ gates that consume those scripts' outputs as upstream canonicals will inherit Class-(d) MANDATORY tags at D_max ∈ [1.0, 3.0). The audit-script update specification:

- For each canonical pin name in a producing script's input-pin map, query the calibration corpus at `substrate-first-canonical-sourcing.md §(iv)` for prior-instance classification.
- If the pin name traces to a Class-(d) calibration-corpus instance (W4-2 or W9b-2), emit Class-(d) severity per the D_max band: MANDATORY at [1.0, 3.0), HARD-HALT at ≥3.0, ADVISORY at [0.1, 1.0), NO-ACTION at <0.1.
- If the pin name traces to a Class-(f) calibration-corpus instance, emit Class-(f) severity per the same band, with the Class-(f)-specific remediation pattern (knowledge-MCP query + canonical substitution).
- The two audit-paths are non-redundant; a producing script that consumes BOTH a Class-(d) prior-instance pin AND a Class-(f) prior-instance pin (rare; possible at multi-level cross-pillar bridges) emits BOTH severity tags concurrently.

This update is queued as a CF entry below; the resolved Class-(d)/Class-(f) classification of W4-2 + W9b-2 is the input.

### IV.4 Constraint-map update — Retroactive remediation pre-registration for S89+ gates that consume W4-2 / W9b-2 outputs

If Class-(d) wins (which it does, this synthesis), retroactive remediation pre-registration applies at S89+ plan-freeze for any gate that consumes W4-2 or W9b-2 outputs as upstream canonicals. The retroactive remediation:

- The S89+ gate's plan-block PIN MAP must explicitly tag pins that derive from W4-2 or W9b-2 SCHEMATIC outputs with their inheritance-class (Class-(d) MANDATORY at D_max ~1.13 OOM).
- The producing script must invoke the derivation-chain audit pattern (Class-(d) remediation): "verify derivation chain; ratio check against source primitives; algebraic-equivalence audit at plan-authorship per Class 8.3 item 5."
- If the S89+ gate's threshold is sensitive to the SCHEMATIC-vs-FULL-physical jump (≥1 OOM tolerance), the gate MUST run the substrate-canonical FULL physical regularization (S61/S78 PV pipeline at Λ_UV = M_KK) before plan-freeze; the SCHEMATIC value remains acceptable as a cross-check but cannot be the primary anchor.

This is queued as a CF entry below.

### IV.5 Constraint-map update — Confirm `epistemic-discipline.md §"Source Reconciliation"` Class-(f) calibration-corpus extension landed by §W7b-83 needs partial edit

The §W7b-83 producing script's rule-file edit landed an extension to `epistemic-discipline.md §"Source Reconciliation"` Class-(f) corpus enumerating the 4 S88-locus calibration corpus instances (W4-2 + W9b-2 + W9c-1 + W5b-2 sub-test (c)) under the Class-(f) hand-off triage. Under this synthesis's Class-(d) reclassification of W4-2 + W9b-2, the Class-(f) corpus extension needs partial rewrite:

- Class-(f) corpus retains: W5b-2 sub-test (c) as CALIBRATION-LOCUS-EXEMPT (only — does not consume SCHEMATIC; no Class-(f) instance presence).
- Class-(f) corpus releases: W4-2 + W9b-2 (reclassified to Class-(d)).
- Class-(f) corpus retains: W9c-1 as POSITIVE-CALIBRATION (no class assignment; pre-existing compliance).
- Net Class-(f) substantive corpus from §W7b-83: 0 NEW instances. The W5a-2 `xi_E_GGE_inv` instance (pre-existing, separate origin per substrate-first-canonical-sourcing.md §(v) calibration corpus) is unaffected.

The partial-rewrite edit is the second primary diff output of this synthesis (CF V.5 below).

---

## V. Carry-Forward Computations

V.1. **Rule-file diff — `substrate-first-canonical-sourcing.md §(iv)` calibration-corpus table reclassification + dual K-count disclosure**
   - **What**: Edit the calibration-corpus table at `.claude/rules/substrate-first-canonical-sourcing.md §(iv)`. Reclassify W4-2 + W9b-2 entries from "NEGATIVE-CALIBRATION (rule (2) violated)" to "Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (NEGATIVE-CALIBRATION on rule (2)) at D_max ≈ 1.13 OOM (MANDATORY band)". Add a "Severity band" column to the 4-row table populating MANDATORY for W4-2 + W9b-2, NO-ACTION for W9c-1 (POSITIVE-CALIBRATION) and W5b-2 sub-test (c) (CALIBRATION-LOCUS-EXEMPT). Add a sub-clause distinguishing K_substantive = 3 (W4-2 + W9b-2 + W9c-1; producing scripts consuming the schematic helper) from K_with_inheritance = 4 (adds W5b-2 sub-test (c) inheritance-locus). State explicitly that the K=4 → MANDATORY promotion is structurally justified at K_substantive = 3 alone (matches K_promotion = 3 exactly); W5b-2 sub-test (c) is the inheritance-locus that maintains structural pointer to the W9c-1 cross-review derivational context. Add the corrective-context paragraph: "1/3 substantive compliance rate at K_substantive=3 — the audit surfaces silent-SCHEMATIC-consumption pathology in 2/3 substantive witnesses; the MANDATORY promotion is the corrective action responding to this pathology, with W9c-1 the POSITIVE-CALIBRATION model that future S88+ gates SHOULD pattern-match."
   - **Inputs**: §W7b-83 audit table (WP lines 407–412); sagan adversarial subsection (WP lines 483–498); `_spectral_action_regulators.py` docstring lines 23–28; `epistemic-discipline.md §"Source Reconciliation"` Class-(d) and Class-(f) literal definitions; D_max measurement chain at sagan WP §W7b-83 line 491 (1.119 OOM ≈ 1.13 OOM).
   - **Gate**: Rule-file edit lands; calibration-corpus table exhibits dual K-count disclosure + severity-band column; sagan-vs-connes-ncg classification reconciliation cited in §(iv) calibration-corpus footer; audit-script `computations/_shared/_substrate_first_provenance_audit.py` (queued S87 V.1; pre-S89 implementation pending) consumes the resolved Class-(d) classification on W4-2 + W9b-2 instances at next plan-freeze.
   - **Effort**: 0.3 wave-equivalent (single rule-file edit; no compute).

V.2. **Per-witness D_max measurement for W9b-2 and the full 4-row severity-band column**
   - **What**: Compute the explicit D_max = |log10(SCHEMATIC) − log10(FULL_PHYSICAL)| for the W9b-2 instance against the substrate-canonical FULL physical regularization (S61/S78 PV pipeline at Λ_UV = M_KK) at the same s argument the W9b-2 producing script consumes. Cross-confirm against W4-2 measured value 1.119 OOM. For W9c-1 (POSITIVE-CALIBRATION) and W5b-2 sub-test (c) (CALIBRATION-LOCUS-EXEMPT), record D_max = NA (no severity-band assignment) but document the structural reason. The 4-row D_max grid populates the severity-band column of the calibration-corpus table (V.1 above); also feeds Workshop 2's adjudication and the `_source_reconciliation_audit.py` retroactive remediation (V.4 below). Parallel-compute-wave structure (4 axes: 4 per-witness D_max measurements; AND-closes the corpus table). This corresponds to the seed file's `CF-W7b-ADDITIONAL-B [Q3-wave-together]`.
   - **Inputs**: §W7b-83 .npz audit table (`s88_w7b_lf_e_schematic_module_audit.npz`); `_spectral_action_regulators.py` docstring lines 23–28; S61/S78 PV physical pipeline source SHAs; W4-2 P5 multiplier values from `sessions/archive/session-86/session-86-w4-workingpaper.md:513` (`M_F2(s=3) = 1.581e-1`, `M_Zub(s=3) = 1.201e-2`); W9b-2 `mellin_a_n` SCHEMATIC value at the s argument the W9b-2 producing script consumes; corresponding S61/S78 PV-pipeline value at same s.
   - **Gate**: 4-witness D_max grid populated; severity-band emission per the `epistemic-discipline.md` 4-band calibration; calibration-corpus table extension at `substrate-first-canonical-sourcing.md §(iv)` exhibits 4 explicit D_max values (or NA with structural reason).
   - **Effort**: 0.4 wave-equivalent (per-witness substrate-canonical lookup + log10 ratio + table extension; canonical computations only).

V.3. **Audit-script update specification — `_source_reconciliation_audit.py` Class-(d) routing for W4-2 + W9b-2 inheritance**
   - **What**: Implement the audit-script update specification of §IV.3 above. Extend `computations/_shared/_source_reconciliation_audit.py` to query the calibration corpus at `substrate-first-canonical-sourcing.md §(iv)` for prior-instance classification on every pin name in a producing script's input-pin map. If the pin name traces to a Class-(d) prior-instance (W4-2, W9b-2), emit Class-(d) severity per the D_max band; if Class-(f), emit Class-(f) severity. Both audit-paths are concurrent and non-redundant. Test fixtures: 1 synthetic gate consuming a W4-2-derived pin (expected Class-(d) MANDATORY); 1 synthetic gate consuming a W9c-1-derived pin (expected NO-ACTION, POSITIVE-CALIBRATION); 1 synthetic gate consuming an unrelated pin (expected NO-ACTION).
   - **Inputs**: `computations/_shared/_source_reconciliation_audit.py` current source; resolved Class-(d) classification on W4-2 + W9b-2 from V.1; D_max measurements from V.2; calibration-corpus table at `substrate-first-canonical-sourcing.md §(iv)` (post-V.1 edit).
   - **Gate**: Audit script extension lands; 3 synthetic test fixtures PASS (Class-(d) MANDATORY emit; NO-ACTION on POSITIVE-CALIBRATION inheritance; NO-ACTION on unrelated pins); audit script verdict-file emission convention tag includes `class_inheritance_detected=<class_letter>` field.
   - **Effort**: 0.6 wave-equivalent (code edit + 3 test fixtures + cross-validate against V.1 calibration corpus).

V.4. **Retroactive remediation pre-registration for S89+ gates consuming W4-2 / W9b-2 outputs**
   - **What**: Implement the retroactive remediation of §IV.4 above. Pre-register at S89 plan-freeze: for any S89+ gate whose producing script's PIN MAP contains a pin derived from W4-2 or W9b-2 SCHEMATIC outputs, the plan-block MUST (i) tag the pin with its Class-(d) inheritance-class (MANDATORY at D_max ~1.13 OOM); (ii) the producing script MUST invoke the Class-(d) derivation-chain audit pattern (verify derivation chain, ratio check against source primitives, algebraic-equivalence audit per Class 8.3 item 5); (iii) if the gate's threshold is sensitive to the SCHEMATIC-vs-FULL jump (≥1 OOM tolerance), the producing script MUST run the substrate-canonical FULL physical regularization (S61/S78 PV pipeline at Λ_UV = M_KK) before plan-freeze, with the SCHEMATIC value as cross-check only.
   - **Inputs**: V.1 + V.2 + V.3 outputs; list of S89+ candidate gates (from `/rclab-plan` ingest); S61/S78 PV pipeline source code + Λ_UV = M_KK pin from `canonical_constants.py`.
   - **Gate**: S89 plan-freeze emits MANDATORY remediation on detection of W4-2 / W9b-2 inheritance pins without the 3-step Class-(d) compliance pattern; calibration corpus instance #1 of retroactive Class-(d) inheritance discipline lands at S89.
   - **Effort**: 0.5 wave-equivalent (plan-freeze auditor extension + S89 plan-block convention adopted; no new compute).

V.5. **Rule-file diff — `epistemic-discipline.md §"Source Reconciliation"` Class-(f) corpus partial-rewrite**
   - **What**: Edit the post-§W7b-83 Class-(f) calibration-corpus extension at `.claude/rules/epistemic-discipline.md §"Source Reconciliation"`. Release W4-2 + W9b-2 from the Class-(f) corpus (they reclassify to Class-(d) per V.1). Retain W5b-2 sub-test (c) as CALIBRATION-LOCUS-EXEMPT (does not consume SCHEMATIC; no Class-(f) instance presence). Retain W9c-1 as POSITIVE-CALIBRATION (no class assignment). State explicitly that the §W7b-83 audit produced 0 NEW Class-(f) substantive instances; the level-pin discipline's Class-(f) calibration corpus retains the pre-existing W5a-2 `xi_E_GGE_inv` instance (per substrate-first-canonical-sourcing.md §(v) Class-(f) calibration; HARD-HALT band at D_max=3.13). Add cross-link to V.1 noting that Class-(d) is the W4-2/W9b-2 substrate; the Class-(f) corpus and Class-(d) corpus are the two non-redundant taxonomy targets the §W7b-83 audit surfaced.
   - **Inputs**: V.1 output (calibration-corpus table reclassification); current `epistemic-discipline.md §"Source Reconciliation"` Class-(f) corpus extension landed by §W7b-83; substrate-first-canonical-sourcing.md §(v) Class-(f) corpus (W5a-2 xi_E_GGE_inv pre-existing instance).
   - **Gate**: Class-(f) corpus block partial-rewrite lands; net Class-(f) S88-locus addition = 0 substantive instances; W5a-2 xi_E_GGE_inv pre-existing instance preserved; cross-link to V.1 Class-(d) corpus added.
   - **Effort**: 0.2 wave-equivalent (single rule-file edit; no compute).

V.6. **Cross-link confirmation — `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` 2-axis table stand-pat**
   - **What**: Per Result 5 (this synthesis), the UV-regulator vs Level pin orthogonality survives the Class-(d) reclassification + K_substantive=3 corpus-shape disclosure. No diff to the `regulator-pin-discipline.md` 2-axis table is required. Confirm-and-pin the stand-pat decision: add a one-line cross-reference in the 2-axis table footer noting that the level-pin axis pathology is Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY for W4-2 + W9b-2 (not Class-(f)), with cite to V.1; the orthogonality structure is invariant under the reclassification because both axes close non-redundant pathways at independent rule-file targets.
   - **Inputs**: V.1 output; `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion"` current text.
   - **Gate**: 2-axis table footer adds Class-(d) cross-reference; no structural edit to the table proper.
   - **Effort**: 0.1 wave-equivalent (single rule-file annotation edit).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY classification of W4-2 + W9b-2 | NON-PHONONIC (rule-file taxonomy) | ADJUDICATED — Class-(d) wins | substrate-canonical FULL exists per `_spectral_action_regulators.py` docstring lines 23–28; pin form is helper-output, not placeholder pattern; Class-(f) literal pattern set does not match |
| 2 | D_max(W4-2) = 1.119 OOM ≈ 1.13 OOM | NON-PHONONIC (severity-band measurement) | CONFIRMED — MANDATORY band | sagan's WP §W7b-83 line 491 measurement validated by explicit substitution chain; W9b-2 D_max queued for V.2 measurement (structurally ~same band) |
| 3 | K_substantive = 3 vs K_with_inheritance = 4 dual disclosure | NON-PHONONIC (corpus-shape adjudication) | RESOLVED — both disclosed | both counts cross K_promotion=3; promotion stands; rule-file calibration-corpus table needs sub-clause distinguishing the two |
| 4 | MANDATORY-as-corrective framing | NON-PHONONIC (epistemic-status framing) | ADOPTED — corrective | 1/3 substantive compliance rate; 2/3 silent-consumption discovered; MANDATORY responds to pathology; rule-file body needs corrective-context paragraph |
| 5 | UV-regulator vs Level pin orthogonality invariance | NON-PHONONIC (cross-rule taxonomy invariance) | CONFIRMED — stand-pat | orthogonality independent of Class classification; no diff to regulator-pin-discipline.md 2-axis table required (V.6 stand-pat annotation only) |
| 6 | §W7b-83 PASS verdict authoritative | NON-PHONONIC (gate verdict) | UNCHANGED — PASS | audit_sha256=`d825b8301aa929c2…` stands; reclassification does NOT contradict the §W7b-83 producing-script PASS verdict; only the post-§W7b-83 rule-file taxonomy needs targeted edits |
