# Seed file — sessions/archive/session-86/session-86-w3-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w3-workingpaper.md` (281 lines)

## Reading frame

The W3 wave executed **zero physics**. All 6 gates (T9, W0-7-MB, W0-11-MB, W0-20-MB, C13, C43) closed PRE-REG-INC via a single mechanical orchestrator script (`computations/s86_w3_pre_reg_inc_closure.py`) because every W3 gate has ≥1 upstream W2/W0c blocker:

| Blocking prereq | Origin | Verdict | Blocks |
|:---|:---|:---|:---|
| C9 `S86-MELLIN-HEAT-KERNEL-INFRA` | W2 | FAIL (value=9.456) | W3-1 (T9), W3-3 (W0-11-MB) |
| C10 `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` | W2 | INFO (value≈2.81e5+0j) | W3-1 (T9), W3-2 (W0-7-MB), W3-4 (W0-20-MB) |
| C12 `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` | W2 | FAIL (value=1.083e-15) | W3-5 (C13) |
| C14 `S86-LAMBDA-TOP-DIRECT-EXTRACTION` | W0c | FAIL (`'no_eigvals_in_cache'`) | W3-6 (C43) |
| C19 `S86-K-FLOOR-K-WALL-LAND` | W0c | FAIL (upstream W5 D.4 absent) | W3-5 (C13) |

The wave produced zero structural constraints, zero PASS/FAIL on substrate physics, zero new closures of the constraint surface. The audit trail is honest about this — the substrate-framing reminder in each gate states "the substrate's spectral content this gate would have interrogated remains uncharacterized at the W3 entry-point."

But the upstream blockers themselves carry rich structural signal that the per-wave seed-investigators for W2 and W0c will see. From the W3 vantage point, what's worth extracting is:

1. **Diagnostic post-mortems on each blocker**, scoped specifically to "what does this blocker tell us about the substrate's regulator-class taxonomy / D_K cache hygiene / cluster-span machine-epsilon floor / Λ-convention canonical anchor — *as understood from the perspective of the W3 consumer*?" This is distinct from the W2/W0c investigators' view, which will focus on producer-side diagnosis.
2. **Pre-staging for S87 W3 re-attempt** — the plan §X re-attempt clause routes W3 forward conditional on each blocker landing in S87. There are open methodological questions (what convention the re-emission uses, whether the re-emit should be paired with a discriminator that distinguishes "truncation-attributable" vs "kernel-structural" causes) that could be worked in S86 closeout independently of whether the blockers re-fire.
3. **Dual-SHA semantics validation** — the W3 wave is the project's first instance of 6 gates sharing `content_sha256` (single closure-script bytes) but each carrying distinct `audit_sha256` (per-gate-distinct pinmap including gate identity). The §246 paragraph explicitly defends this as "the documented dual-SHA semantics, not a hardcoding defect." That defense is worth structurally validating against the gate-verdicts rule and S86 W0a-1 SHA discipline before S87 inherits the pattern.

The wave is informational about audit-topology, not about substrate physics. Workshop candidates below treat the wave as a diagnostic harvest from the upstream blockers, not as a substrate-physics result to interpret.

## Candidates

### Candidate 1 — Mellin-cone infrastructure post-mortem (C9 FAIL + C10 INFO joint diagnosis from W3-consumer perspective)

**What it would do**: Workshop the joint structural meaning of C9's FAIL (value=9.456 — Mellin-Barnes residue extractor with Seeley-DeWitt subtraction landed at ~1 OOM above the |Λ_CC^MB|/|a_0| ≤ 1e-1 PASS criterion) and C10's INFO (value=2.81e5+0j — analytic_zeta off-pole returned a finite but uncomfortably-large complex value). The lizzi 9A §A-2 hypothesis behind T9 (REPLACEMENT-B asymptotic) is that S_zeta_E^cont(L_max)/ζ_D(3, L_max) > 1+ε_T9 in the L→∞ limit; the W0-7-MB hypothesis is that ρ ∈ [−1.05, −0.95]; the W0-20-MB hypothesis is finite Mellin-cone apex with χ²/dof ≤ 5. The ~1 OOM C9 deviation and the large-magnitude C10 INFO together suggest the analytic-continuation route is producing structural signal that does NOT match the truncation-FAIL → MB-PASS escape narrative the plan expected. Workshop diagnoses: (a) is the C9 9.456 a near-miss requiring fit-window refinement, or a structural divergence the original W0-11 truncation FAIL was actually correctly detecting? (b) does the C10 value 2.81e5 represent the off-pole substrate-spectral signal, or is it a Hankel-contour systematic that needs reformulation?

**Why it's worthwhile**: Three of the six W3 gates (T9, W0-7-MB, W0-20-MB — i.e. half the wave) are gated on C10; two are gated on C9; together they block 5/6 W3 gates. If C9 and C10 cannot land in S87, the entire W3 wave repeats this PRE-REG-INC pattern. The W3-consumer perspective on these blockers is structurally distinct from the W2-producer perspective — the consumer cares about specific evaluations (s=4 leading residue for T9, s=3 off-pole apex for W0-20, ρ-fit over s∈[2.5, 4.5] for W0-7-MB) that may be feasible even if the master infrastructure misses its global PASS criterion. The workshop should ask: does C9/C10 need to land at PASS, or do downstream W3 consumers only need it to land at "well-defined at specific evaluation points"? This decomposition would unblock W3 in S87 without requiring C9/C10 themselves to PASS.

**Type**: 2-agent workshop

**Suggested agents**: lizzi-spectral-functional-theorist, connes-ncg-theorist

**Rounds**: 2 (R1: each agent steel-mans their reading of the C9 FAIL + C10 INFO from the W3-consumer angle; R2: converge on the discriminator question — "is the W3 prerequisite gate the master PASS or the per-evaluation finiteness?")

**Context the workshop will need**:
- C9 verdict line + producing script `s86_w2_mellin_heat_kernel_infra.py` (line 95 of `computations/s86_gate_verdicts.txt`)
- C10 verdict line + producing script `s86_w2_mellin_cone_residue_infra.py` (line 91)
- W3-1 hypothesis text §W3-1 (T9 ε_T9=0.01 asymptotic margin)
- W3-2 hypothesis text §W3-2 (ρ ∈ [−1.05, −0.95])
- W3-4 hypothesis text §W3-4 (analytic_zeta(s=3) finite + χ²/dof ≤ 5)
- Plan §0.5 prerequisite table — the literal text says "PASS (|Λ_CC^MB|/|a_0| ≤ 1e-1 AND χ²/dof ≤ 5)" for C9 and "PASS (analytic_zeta(s=3, L_max=10) finite AND χ²/dof ≤ 5)" for C10. The discriminator question is whether the per-gate minimal requirement is weaker than the master PASS.
- Plan §X cross-wave hook: T9 PASS feeds W1a T5 (Mellin Strip / Convergence Cone Theorem registry landing); W0-11 + W0-20 MB-RE PASS would collapse Truncation=6 partition toward Truncation=4 in BULLETIN-W0W5-FAIL-PARTITION (W1c) — these are the downstream beneficiaries the workshop should keep in view.
- closeout §1.5 F_4 / M regulator-class taxonomy + lizzi S-1 Regulator-Family Boundary Theorem + lizzi S-7 §V.6 Mellin Strip / Convergence Cone Theorem — these are the structural anchors against which the C9 FAIL and C10 INFO must be diagnosed.

### Candidate 2 — Cluster-span machine-epsilon floor: C12 FAIL forensics for C13 unblock

**What it would do**: Investigate the C12 `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` FAIL (value=1.083e-15 against threshold 1e-15) as a precision-floor problem from the C13 K-corridor extension perspective. The MEMORY/agent-rules SOURCE-RECON entry already records that the C12 FAIL is "plan-authoring-side precision-comparison floor mismatch — bit-exact W0-3 reproduction (`b2/b3 = 2.000000000000002` at L_max=12) confirms semantic preservation. C12 FAIL is **accepted with diagnostic**; the module `computations/_cluster_span_extract.py` is published; `cluster_span(L_max)` is callable from downstream W3 C13." So C13 is logically unblockable from C12 alone. The blocker is C19 (`S86-K-FLOOR-K-WALL-LAND` FAIL: `'upstream_W5_D.4_FAIL_no_K_floor_K_wall_values'`). Workshop scope: design a C13 dispatch that (a) consumes the published `_cluster_span_extract.py` module despite the C12 verdict-FAIL, (b) substitutes a placeholder K_floor / K_wall scan range derived from already-pinned canonical constants K_R5, K_crit, K_FIRAS (K_crit_BdG=2.035 from C17 PASS) — i.e. the K-corridor scan can use canonical-constants-only K-anchors, deferring the K_floor / K_wall pin to S87 W5 D.4 closure, (c) reports per-K cluster-span deviations as INFO with explicit "K_floor / K_wall pending" annotation, NOT PASS or FAIL.

**Why it's worthwhile**: C13 is the W3 gate with the strongest pre-publishable infrastructure. The C12 FAIL is acknowledged as a precision-floor artifact (per agent-memory + plan §0.5); the only true blocker is C19's K_floor / K_wall absence. But the K-corridor extension test (machine-epsilon `b_pow(span_2) = 2·b_pow(span_3)` across log-spaced K) does not structurally require K_floor / K_wall — it requires *some* K-corridor endpoints, which can be canonical-constants-pinned today. This is a high-leverage S86-closeout candidate: a workshop that converts C13's PRE-REG-INC into an INFO-with-published-data result would close one of the 6 W3 gates within S86 itself. Math content of the cluster-span identity is the same regardless of K-corridor endpoint choice; the choice is metadata, not physics.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (CCM cluster-span is core Connes-track; the test is exactly the C13 hypothesis but with a canonical-constants-pinned scan range substituting for the W5 D.4-derived K_floor / K_wall)

**Rounds**: N/A (solo)

**Context the workshop will need**:
- C12 verdict line and the published `_cluster_span_extract.py` module
- C17 PASS verdict line (K_crit_BdG = 2.035 registered, line 22 of verdicts file)
- C19 FAIL verdict line + the W5 D.4 missing-derivation note
- Plan §W3-5 §6 method block (the dispatch prompt with K_R5, K_crit, K_FIRAS from canonical_constants)
- `.claude/rules/epistemic-discipline.md` lines 138-150 SOURCE-RECON entry on the C12 W2-4 canonical-metric mismatch — explicit "bit-exact W0-3 reproduction confirms semantic preservation" plus "module published; cluster_span(L_max) callable from downstream W3 C13"
- Plan §X cross-wave hook (line 852): "C13 PASS extends W0-3 (a W1a T1 mechanical-write target) — the registry write in W1a would need to cite C13 corridor-extension scope OR await S87 re-write." A workshop INFO verdict in S86 would let W1a T1 land at single-K scope without waiting on S87.
- agent-memory `feedback_fix-in-session-never-defer.md` rationale — the candidate workshop is exactly that rule's "dispatchable now / closed-by-existing-precedent" route
- plan §11 C13 PASS/FAIL/INFO thresholds — the workshop verdict would land as INFO (canonical-constants-K-corridor scan with K_floor / K_wall pending), with explicit migration of the PASS/FAIL determination to S87.

### Candidate 3 — Λ-convention canonical anchor synthesis (C43 + C14 reframe)

**What it would do**: Reframe the C14 `S86-LAMBDA-TOP-DIRECT-EXTRACTION` FAIL (value=`'no_eigvals_in_cache'`) and the consequent C43 `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION` PRE-REG-INC as a synthesis problem about the Λ-convention canonical anchor. C43's hypothesis was that "Λ_actual = λ_max(L=10) from the D_K eigvalue cache" would either (a) recover S85 W3-11 within 30% of one ad hoc convention (Casimir-saturated or c_fabric·M_KK), OR (b) be structurally distinct with documented disambiguation, AND preserve W3-9 Ginzburg-Oz Gi-deviation ≤ 50%. The C14 FAIL is structural — there is no D_K eigvalue cache for L=10. Workshop scope: synthesize the Λ-convention landscape independently of the cache problem. Three Λ-conventions exist: Casimir-saturated Λ, c_fabric·M_KK ad hoc Λ, and (pending C14) empirical Λ_top. Workshop adjudicates: (i) what's the structural relationship among the three? (ii) is the W3-9 vs W3-11 dispute ACTUALLY a Λ-convention dispute, or is the dispute primary structural and Λ-convention is a downstream classifier? (iii) what's the minimal D_K cache build required to land C14 in S87, and can the cache be partial (L=10 alone) rather than full?

**Why it's worthwhile**: The C14 FAIL is a tooling-infrastructure failure (no eigval cache), not a physics failure. The W3-9 vs W3-11 dispute predates S86 and is the kind of inter-session structural tension that benefits from explicit synthesis even when the empirical disambiguator (Λ_actual) is not yet computable. A workshop that maps the Λ-convention landscape — and identifies which convention the substrate's spectral structure logically anchors to — would either (a) preempt the C43 outcome by identifying which convention the structure forces, or (b) sharpen the C43 hypothesis by stating exactly which convention-pair the empirical Λ would adjudicate. Either result is a structural advance from the W3 PRE-REG-INC entry-point. C14 itself is high-EVOI infrastructure for many downstream gates beyond C43.

**Type**: 2-agent workshop

**Suggested agents**: lizzi-spectral-functional-theorist, kitaev-floquet (or volovik for the Casimir-saturated angle) — pick second agent based on the structural framing the first agent adopts

**Rounds**: 2

**Context the workshop will need**:
- W3-9 result from S85 (the Λ-convention paper) and W3-11 result (the contested companion)
- Plan §W3-6 hypothesis text (the 30% recovery threshold + Gi-deviation ≤ 50%)
- C14 verdict line + the D_K eigval-cache absence rationale (line 19 of verdicts file: `value='no_eigvals_in_cache' scheme=spectral_cache_direct convention=L_max=10_native`)
- canonical_constants.py M_KK, c_fabric, Casimir-saturated Λ values (whatever's pinned)
- the S85 W3-9 + W3-11 source verdict lines for cross-reference
- Plan §X cross-wave hook (line 853): "C43 PASS interacts with W4 C28 (cutoff_sqrt adjudication): Λ-convention resolution under empirical Λ_actual partially disambiguates the cutoff_axis YAML pin (W0a R3) usage downstream." The workshop should map which Λ-convention each cutoff_axis YAML choice (`spectral` vs `coherence`) implicitly anchors to.
- the W6-13 mack-canonical context for w_a / dark-energy implications of Λ-convention

### Candidate 4 — Dual-SHA semantics validation under W3 mechanical-closure precedent

**What it would do**: Validate the W3 wave's dual-SHA pattern as a structural precedent for future PRE-REG-INC mechanical closures. The wave produced 6 verdict lines all sharing `content_sha256=05071d10327d7f32fe88eb9d63278f3a4f737ca1f87280a3c51a5f8266c01686` (single closure-script bytes) but each carrying a distinct `audit_sha256` constructed from the per-gate pinmap. The wave-synthesis paragraph §246 explicitly defends this as "the documented dual-SHA semantics, not a hardcoding defect." The workshop validates this defense against (a) `.claude/rules/gate-verdicts.md` schema requirements, (b) `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class-1/4 (ansatz-forced PASS, post-hoc pre-registration editing) — the W3 verdicts are FAIL/PRE-REG-INC, not ansatz-forced PASS, so they should clear; but the orchestrator-authored mechanical closure pattern is a *new* path that needs explicit rule sanction, (c) the v3 ladder sig_5 audit (duplicate `audit_sha256` detection) — this MUST clear because the audit_sha256 values are distinct (e2b16694..., 3ab5718a..., 65ddadbd..., 3b1c13ac..., c38cd256..., c4986627...). Workshop produces a structural rule extension for orchestrator-authored mechanical-closure patterns: when is this acceptable, when does it indicate a planning defect, and what's the audit-trail signature?

**Why it's worthwhile**: The W3 wave is the project's first systematic use of orchestrator-authored mechanical closure for an entire wave. The pattern saved 10-12 agent-hours of redundant specialist time (per WP §224), but it sets a precedent. Without explicit rule sanction, future planners may abuse it (defaulting to mechanical closure when specialist dispatch would have surfaced new structural information). A rule-extension workshop captures the precedent honestly: when can orchestrator-authored mechanical closure substitute for specialist dispatch? When is the savings genuine vs. an audit-trail dilution? The workshop output would be either a permanent rule entry (added to `.claude/rules/agent-standards.md` or a new mechanical-closure-discipline.md) or a permanent registry entry pinning when the W3 pattern is and is not appropriate.

**Type**: solo (1 agent)

**Suggested agents**: gen-physicist (breadth-coordinator for rule-system synthesis) OR a methodology-specialist agent — pick based on agent availability

**Rounds**: N/A (solo)

**Context the workshop will need**:
- WP §220-250 (the entire wave-synthesis section) + WP §246 (the dual-SHA defense paragraph)
- `.claude/rules/gate-verdicts.md` schema specification
- `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class-1 + Class-4
- the `s86_w3_pre_reg_inc_closure.py` script bytes
- relevant precedents: line 19 (`S86-LAMBDA-TOP-DIRECT-EXTRACTION` FAIL with `value='no_eigvals_in_cache'`) and line 24 (`S86-K-FLOOR-K-WALL-LAND` FAIL with `value='upstream_W5_D.4_FAIL_no_K_floor_K_wall_values'`) — these established the `value='upstream_...'` pattern for upstream-blocked gates
- agent-memory entries on the S82/S84 task-complete-lie failure mode — the W3 mechanical closure is *honest* about not executing physics; the question is whether honesty alone is a sufficient justification or whether the pattern needs additional safeguards.

### Candidate 5 — W3 prerequisite cascade structural diagnosis (W2 + W0c root-cause map)

**What it would do**: Produce an integrative structural diagnosis of *why* the W3 wave was 6/6 PRE-REG-INC. The plan §X re-attempt clause routes W3 forward; but it's worth extracting the structural pattern from the cascade itself. Five distinct upstream blockers (C9, C10, C12, C14, C19) cascaded into 6 W3 gates. Are they independent failures, or do they share a structural root? Candidates: (a) all five blockers involve the L=10 D_K spectral cache — C14 is explicit about cache absence; C9 / C10 use the cache implicitly via Mellin-Barnes residue extraction; C12 uses it in cluster-span evaluation; C19 uses it for K_floor / K_wall identification. If the L=10 cache is the structural common cause, S87 W3 re-attempt has a single high-leverage prerequisite (build the L=10 D_K cache). (b) Alternatively, the blockers cluster by methodological discipline: C9 + C10 are precision-floor failures on master infrastructure; C12 is a published-but-FAILed module (precision-comparison artifact); C14 is a tooling-cache absence; C19 is an upstream-derivation absence. If they cluster by discipline, the lesson is about plan-authoring (PRDR enforcement, source-reconciliation) rather than physics. Workshop adjudicates which root cause dominates and what S87 should land first.

**Why it's worthwhile**: The W3 wave's contribution to the S86 audit trail is exactly the upstream-block topology mapping. The wave-synthesis §EVOI assessment paragraph (§252) already begins this analysis ("high-EVOI gates within W3 are W3-3 (W0-11-MB) and W3-4 (W0-20-MB) — both have single-prereq blocks (C9 and C10 respectively)"). A workshop extends this to a full root-cause diagnosis: is the L=10 cache the structural bottleneck, or is the methodology-discipline pattern the bottleneck? The answer determines what S87 must land first, and informs whether the wave-pattern will repeat in S88. From the W3-consumer perspective specifically, the L=10 cache argument has high prior weight — every Mellin-cone evaluation of the spectral functional needs it.

**Type**: 2-agent workshop

**Suggested agents**: lizzi-spectral-functional-theorist (regulator-class infrastructure perspective), connes-ncg-theorist (NCG K-cycle / cluster-span infrastructure perspective)

**Rounds**: 2 (R1: each agent argues their root-cause diagnosis; R2: converge on what S87 must land first to unblock W3)

**Context the workshop will need**:
- All 5 blocker verdict lines from `computations/s86_gate_verdicts.txt` (C9, C10, C12, C14, C19)
- Plan §0.5 prerequisite table from `sessions/session-plan/session-86-plan-w3.md`
- WP §252 EVOI assessment paragraph
- The producing-script names for each blocker, to assess whether they share a common upstream cache (look for shared `from canonical_constants import *` D_K-cache pins)
- agent-memory `feedback_framework-hygiene.md` for prioritization framework
- `sessions/evoi-framework.md` current state for how the W3 cascade affects framework-wide EVOI rankings
