# Review — `papers/methodology/orchestrated-ai-research.tex`

**Reviewer**: coordinator (S106-era review pass)
**Review date**: 2026-06-12
**Paper as-written**: dated March 2026, framework era S51, 441 lines
**Framework now**: post-S106 (the prompt says "S103 era"; the verifiable ceiling is higher — see §1 note A)
**Verdict (full rationale in §7)**: **RESTRUCTURE** — keep the spine and the best case studies, recount every statistic, and add a large post-S51 apparatus that did not exist when the paper was written. The paper covers **less than half** the project's session history (S51 of ≥S106) and **almost none** of the methodology apparatus that is now the project's most defensible contribution.

A meta-note that governs this entire review: this is a paper *about honest methodology*. It must itself be honest. Every number below carries its counting method. The probability trajectory in particular must be reported with its sign changes **and** with the fact that the framework stopped producing a calibrated number after S66 — the paper's headline "current 2–4%" is the last *calibrated* value (S51) and is now ~55 sessions stale by a deliberate methodological choice, not a measurement.

---

## §1 — Statistic Recount Table

Authoritative source for entity counts is `tools/knowledge.db` (the SQLite store the knowledge MCP serves; rebuilt from `knowledge-index.json` by `/weave --update`). File counts are from `find`/`ls` over the working tree. Each row cites how it was counted.

| Claim (March-2026 abstract) | March-2026 value | Current value | Counting method / source |
|:--|:--|:--|:--|
| Sessions | 51 | **≥106** (calibrated-history sessions; ceiling S106) | EVOI file currency tag `<!-- evoi-content-currency: S106 -->` (dated 2026-06-12); session dirs `sessions/session-*/` exist through `session-106/`; knowledge.db `sessions` table = **123 rows** (counts sub-sessions 21a/21b/22b… so it overstates the integer session count). See note A. |
| Duration | ~10 weeks (Jan–Mar 2026) | **~17 months** (Dec 2024 → Jun 2026) | atlas-06 scope line "Sessions 1–88 (Dec 2024 — May 2026)"; git initial commit → S106 stamp 2026-06-12. The "10 weeks" was real for S1–S51; the project did not stop. |
| Specialist agents | 29 | **34 agent definitions** (≈31 physics specialists + 3 utility) | `ls .claude/agents/*.md` = 34; knowledge.db `agents` table = 34. Utility/orchestration agents in that set: `coordinator`, `knowledge-weaver`, `web-researcher`. New since S51 incl. `lizzi-spectral-functional-theorist`, `transit-dynamics-theorist`, `volovik-superfluid-universe-theorist`, `mack-cosmic-bridge`, `phonon-first-cosmologist`, `loop-quantum-gravity-theorist`, `van-den-dungen-bridge-theorist`, `little-red-dots-jwst-analyst`, `cosmic-web-theorist`, `string-theory-theorist`, `kitaev-quantum-chaos-theorist`, `quantum-foam-theorist`, `nazarewicz-nuclear-structure-theorist`, `neutrino-detection-specialist`. See note B. |
| Computation scripts | 630 | **3,128** | `find computations -name "*.py" | wc -l` = 3128. ~5× growth. (Note: includes `_shared/` audit infrastructure + per-session gate scripts; this is the same count-basis the paper used — all `.py` under `computations/`.) |
| Theorems | 392 | **2,301** | knowledge.db `theorems` table COUNT. ~6× growth. (Caveat: extractor-harvested "theorem-like" entities from session files; not all are machine-ε structural proofs — see note C.) |
| Mechanisms closed | 58 | **195** (live DB count) | knowledge.db `closed_mechanisms` table COUNT = 195. History: the closed-mechanisms table was deduplicated at **S90 (735→266 rows)**; further consolidation has since brought the live extractor count to 195. See note D — "closed-mechanism count" is a contested metric in this framework. |
| Gates registered | 240 | **3,241** | knowledge.db `gates` table COUNT = 3241. The paper's "240 gates / 58 closures" framing is an S51 snapshot. |
| Knowledge entities | 82,000+ | **103,767** (FTS-indexed entities) | knowledge.db `knowledge_fts` table COUNT = 103,767. Component tables: equations 19,713; edges 71,102; data_provenance 2,941; session_files 2,446; constants 276; registries 217. |
| Knowledge-index size | 30 MB | **~45 MB / 1,224,774 lines** | `ls -la tools/knowledge-index.json` = 45,172,471 bytes; `wc -l` = 1,224,774. |
| Equations extracted | 80,497 | **19,713** | knowledge.db `equations` table COUNT = 19,713. **This is LOWER than the paper's number** — the extractor was re-scoped (the March figure likely counted raw LaTeX-fragment hits; the current table is de-duplicated equation entities). Flag for honest down-correction, not up-inflation. |
| Data-provenance records | 567 | **2,941** | knowledge.db `data_provenance` table COUNT = 2,941. |
| Probability trajectory points | 172 | **212** | knowledge.db `probability_trajectory` table COUNT = 212. |
| Retractions / corrections | 25 | **49** | atlas-09 master total: "Total retractions/corrections through S102: 49" (46 through S88 + 3 S92–S100a interpretive-DOF rescopings). See note E. |
| Major breakthroughs catalogued | 15 | **39** | atlas-10 header "Major breakthroughs cataloged: 39". Of these, 10 (25.6%) are post-S82 METHODOLOGY-FLOOR / CALIBRATION-CORPUS events that — per the atlas-10 layer-distinction warning — do **NOT** raise substrate-physics probability. See note F. |
| Probability trajectory | 2% → 52% peak → "current 2–4%" | **last *calibrated* value = 2–4% at S51; FROZEN since S66** — no calibrated number produced S67–S106 | atlas-06: "EVOI table FROZEN since S66 … post-S66 trajectory uses directional language … no numerical probabilities." The S89 Sagan re-anchoring (Q44) was recommended but **never executed** (still open in evoi-framework §6 / atlas-08). See note G — this is the single most important correction. |
| Probability peak | 52% | **45–52% at S19d** (peak), one decisive collapse to 8%/5% at S23a (Venus Moment) | atlas-06 data table. The paper's "52%" and "dropped 52%→5% in a single session (S23a)" conflate two events: the panel peak was 45–52% (S19d); the S23a Venus Moment dropped panel 40%→8%, Sagan to 5%. The "single-session 52%→5%" sentence in §2.3 is imprecise. |
| Publishable mathematical results | 36 | **survives; understated** | The paper's "36 publishable theorems" is a curated subset and is a defensible *claim type*. The DB's 2,301 theorem-entities is the raw extractor count; the "36 publishable" figure is the right granularity for a paper claim but should be re-derived against the current `summary/`/`papers/` standalone-result set (there are now ≥7 standalone `papers/` manuscripts: alpha-s-ns, anderson-higgs, cmpp-classification, monotonicity, oz-spectral-index, spectral-action-monotonicity, weyl-tensor-cmpp). |

### Counting notes (the honest caveats — these belong IN the rewrite, not just here)

**Note A — session count.** There is no single integer "session count." Three defensible figures: (i) **≥106** distinct session dirs with closed working papers (`sessions/session-106/` exists; EVOI stamped S106 = today); (ii) **123** rows in knowledge.db `sessions` (over-counts: includes sub-sessions like 21a/21b/22b/23a/23b/23c and split sessions 73a/73b, 100a/100b); (iii) the `summary/session-*-final.md` count is **36** but that window only spans **S51–S85** — pre-S51 finals were folded into the Atlas, post-S85 finals stopped being written to `summary/`, so this is NOT a session count and must not be used as one. **Recommended paper figure: "over 100 sessions"** with a footnote on the sub-session ambiguity. The prompt's "S103 era" is itself slightly behind the S106 ceiling; report the verifiable ceiling.

**Note B — agent count.** 34 agent `.md` files. The honest framing for the rewrite: "≈31 specialist physics agents plus 3 orchestration/utility agents (coordinator, knowledge-weaver, web-researcher)." The March "29 specialist" figure was correct at S51; the roster grew. Naming the utility split matters because the paper's own §4.2 ("knowledge-weaver on Sonnet, physics on Opus") relies on that distinction.

**Note C — theorem count.** 2,301 is the extractor's harvest of theorem-*like* entities from session text; it is not 2,301 machine-ε structural proofs. The paper should keep TWO numbers cleanly separated: the **curated** "publishable mathematical results" (the ~36 / now-≥7-manuscript set) and the **indexed** theorem-entity count (2,301). Reporting only the raw number would be inflation; reporting only the curated number hides the index scale. Report both, labelled.

**Note D — closed-mechanism count.** This is a *contested metric inside the framework's own rules*. `evoi-prioritization.md` and `epistemic-discipline.md` both state that closures **cluster by topic** ("Four agents hitting the same truncation wall = ONE methodological finding. Three CC mechanisms failing = ONE open problem with three eliminated approaches"). The S90 dedup (735→266) was the framework acting on exactly this principle; the live DB count is now 195. **The rewrite must NOT headline a raw closure count as a vanity metric** (this is forbidden by the project's no-session-aggregate-metrics rule). Report it as "195 closed-mechanism records in the index, deduplicated from 735 at S90, with the explicit caveat that closures cluster into a much smaller number of independent structural findings."

**Note E — retractions.** 49 total through S102 (atlas-09). The richness is the point: the log now spans honest-error, overclaiming, wrong-observational-mapping, conceptual-reframe, **and** two post-S82 categories the March paper had no vocabulary for — SUPERSESSION (document-level authority migration, e.g. R_JE single-tag retirement) and interpretive-DOF rescoping (falsifier *relocation*, e.g. CGWB GW→LSS migration, where the falsifier moves instrument rather than vanishing). The rewrite's retraction-analysis section should adopt the atlas-09 taxonomy.

**Note F — breakthroughs.** 39 catalogued, with a **load-bearing disclaimer** the March paper predates: methodology-floor breakthroughs (rule promotions, K-counter saturations) do not increase substrate-physics probability. The rewrite's cross-domain section can expand from 15→the substrate-physics subset, but must reproduce the layer-distinction warning verbatim or it re-commits the inflation the framework explicitly closed.

**Note G — probability trajectory (the headline correction).** The abstract's "current 2–4%" is the **S51** calibrated value. Per `feedback_framework-hygiene.md`, the Sagan numerical assessment has been **frozen since S66 W2-A**; S67–S106 movements are recorded as *direction only* (UP-tick / DOWN-tick / flat / PARADIGM-SHIFT / NEUTRAL), with an explicit substrate-physics-vs-methodology-floor layer tag. The recommended S89 Sagan re-anchoring (mack + sagan co-dispatch) is **still an open workshop item** (Q44; evoi-framework §6). So the honest statement is: *"The last calibrated probability was 2–4% (S51). After S66 the project deliberately stopped quoting a single number, judging that post-S66 evidence is better described as a constraint-surface geometry than a scalar; a formal re-anchoring remains pending."* Quoting "current 2–4%" as if it were a live S106 measurement is the one place the paper's own honesty discipline is currently violated by staleness.

---

## §2 — What Survives (architecture descriptions still accurate)

These sections are structurally sound and require only number-refresh + extension, not rewrite:

1. **§2 Epistemic Discipline Framework — core principles.** Pre-registered falsification, "negative results are boundaries," "report the number first / classify second / interpret third," the source-authority hierarchy (Sagan > synthesis > gate verdict > minutes > raw output), the no-filler-confidence rule. All still canonical (`epistemic-discipline.md`). The hierarchy is verbatim-current. **Keep; extend** (the hierarchy is now one floor of a much larger PRU/PRDR/SOURCE-RECON apparatus — see §4).

2. **§2.5 The DISSOLVED category** (Foundation & Assumptions Registry, S50). Still live as **atlas-04 assumptions** with PROVEN/ASSUMED/CONDITIONAL/BROKEN/DISSOLVED tags. The τ-stabilization "wrong question → transit paradigm" narrative is exactly right and is now the spine of the whole post-S51 story (THE ORDERED VEIL = diabatic transit-freeze). **Keep; the counts (15/14/8/11/4) are S50 snapshots — recount against current atlas-04.**

3. **§3 Collaboration formats — the qualitative findings.** "Agents lie about being done," workshop roleplaying prohibition, the notification-avalanche / O(n²) cross-notification problem, "the working paper template beats SendMessage choreography," compute-sprint > large-team. All still true and now codified in rules (`teammate-behavior.md`, `feedback_session-process.md`). **Keep the lessons; the format taxonomy itself evolved — see §3 below.**

4. **§4.1 Carry-forward protocol.** "If not planned, lost forever" is still the canonical rule (`session-handoffs.md`, `feedback_fix-in-session-never-defer.md`). **Keep; sharpen** — the protocol is now bifurcated (mandatory 4-field carry-forwards for genuine future compute vs. fix-in-session for hygiene; the no-padding rule) and routed through housekeeping ledgers + WP CF blocks.

5. **§4.3 Agent memory & institutional knowledge.** Persistent per-agent memory surviving across sessions is still the architecture. **Keep; the memory discipline matured hard** (AMRI, memory-scope, agent-private-vs-project-level) — see §4.

6. **§5 Cross-domain correlation — the thesis.** "Discoveries at domain intersections require a generalist coordinator with full corpus access, not just specialists" is the paper's strongest and most generalizable claim, and the SA-correlator case study (S50) is a genuine, well-documented instance. **Keep; this is the spine to build the cross-domain section on.** Update the breakthrough count (15→39 catalogued; report the substrate-physics subset honestly).

7. **§6.1 "What worked" + §7 "rules matter more than agents."** The closing thesis — that the epistemic architecture is the invariant and the agents are the variables — is, if anything, *more* supported now (the entire S78–S106 methodology-floor era is evidence for it). **Keep; it is the natural conclusion of the expanded paper.**

8. **§8 Discussion — generalizability + role of the human researcher.** Direction-setting / quality-control / associative-leaps decomposition still holds. **Keep; the "human stays the publish-decision and direction-setter" point is reinforced by the user's documented role through S106.**

---

## §3 — What Must Change

Ordered by severity (honesty-critical first).

1. **HONESTY-CRITICAL: the "current 2–4%" probability claim.** (Abstract; §2.3; §5.4; §9 Conclusion.) Must be reported as the S51 calibrated value + the S66 freeze + the pending re-anchoring (note G). As written, a paper about honest Bayesian assessment quotes a 55-session-stale number as current. Fix everywhere it appears.

2. **HONESTY-CRITICAL: the "single session 52%→5%" sentence** (§2.3). Imprecise. The peak was 45–52% (S19d); the Venus-Moment collapse was 40%→8% panel / →5% Sagan (S23a). Two distinct events. Re-state from the atlas-06 data table.

3. **Every quantitative claim is an S51 snapshot.** Sessions, agents, scripts, theorems, closures, gates, entities, equations (the equations number goes *down* — note C/§1), retractions, breakthroughs — all must be recounted per §1 with their counting methods stated inline. The paper currently reads as if S51 were the end of the project; it was roughly the one-third mark.

4. **Author/model attribution must span generations.** Title page: "Claude Opus 4.6." The project demonstrably ran across **Opus 4.6 → 4.7 → 4.8**: §VIII references "orchestrator opus-4.7-1m" (S81), the current harness is `claude-opus-4-8[1m]`, and session finals carry era markers. The honest attribution is the *Claude Code agent framework across the Opus 4.6–4.8 generations* (check git log / session finals for the exact era boundaries rather than picking one). Anthropic affiliation stays.

5. **Collaboration-format taxonomy is superseded.** §3 names Workshop / Panel / Compute-sprint (S16–S51). The current vocabulary is the **rclab skill family**: `/rclab-plan`, `/rclab-coordinate` (compute mode), `/rclab-investigate` (workshop-schedule campaigns), `/rclab-review` (independent solo syntheses), `/rclab-workshop` (2-agent iterative), `/rclab-team`, `/rclab-solo`, `/rclab-reflect`. The "Collab-Plan / Collab-Team pipeline" (§4.4) was renamed and split. The compute-sprint *is* `/rclab-coordinate`; the panel/workshop *is* `/rclab-team`+`/rclab-workshop`. Re-map the section onto the current pipeline.

6. **"Knowledge index (knowledge-index.json, 30 MB)" → full knowledge infrastructure.** The index is now ~45 MB / 1.2M lines, backed by a **SQLite + FTS5 database** (`tools/knowledge.db`) served via a dedicated **knowledge MCP server** (9 entity types, FTS-ranked search, `get_constant`/`trace_entity`/`emit_verdict` tools — 11,637 MCP calls logged), plus a **routing manifest** export and the **`/weave` pipeline**. This is a substantial infrastructure story the March paper reduces to one JSON file. (note H.)

7. **The "framework probability" reporting methodology itself changed.** The paper presents a single scalar trajectory as the diagnostic. The framework has since adopted: (a) the **no-session-aggregate-metrics rule** (no PASS/FAIL ratios as quality claims — `feedback_reporting-framing.md`); (b) **effort-based probability** ((mechanism links complete / total) × (fraction approaching observation) — `evoi-prioritization.md`); (c) **EVOI** as an ordinal leverage proxy explicitly *not* a probability; (d) the **substrate-physics vs methodology-floor layer split** on every directional movement. The §5.4 "probability as methodology diagnostic" section must be rewritten around this — and must drop any session-aggregate vanity framing.

8. **§4.2 closure-efficiency "38% predictable / 62% informative" + Table 4 (agent count vs discovery) + Table 1 (format comparison) use bespoke session-aggregate metrics** that the framework's current rules would flag. Retraction-rate-per-session and "discovery rate per session" are exactly the kind of aggregate the no-vanity-metrics rule targets. These tables can stay as *historical* (S1–S51) descriptive data, clearly scoped, but must not be presented as live quality measures, and must not be extended to S52–S106 as ratio-metrics.

9. **Bibliography.** 4 `\cite{needed:...}` placeholders (the prompt said 6; the verified count is 4). Three resolve to real papers with already-correct bibitem details (alphageometry, alphafold, gnome); one (framework_paper, "Paasch in preparation") is a genuine internal-companion gap. See §5.

10. **"MEMORY.md (200 lines)" (§8.3 Limitations).** Still ~accurate as a stated cap, but the memory architecture is now far richer (per-agent + orchestrator project memory + AMRI migration to `sessions/framework/` registries). The "information lost in compression" limitation is partly *addressed* by the registry-promotion discipline — update the limitation to reflect that institutional knowledge now lives in queryable registries + DB, not only in compressed memory.

---

## §4 — Post-S51 Apparatus Inventory (the expansion spine)

This is the core deliverable: the methodology apparatus that did not exist (or was embryonic) at S51 and now constitutes the project's most defensible methodological contribution. Each item is a candidate **new section or subsection** for the expanded paper, with a one-paragraph summary and a pointer. The single best curated synthesis to build the new spine on is **`sessions/framework/Atlas/atlas-12-methodology-floor.md`** (729 lines; the methodology-side atlas) — the rewrite's new Part should essentially *be* a publishable rendering of atlas-12, with atlas-09 (retractions) and atlas-10 (breakthroughs) feeding the empirical sections.

### 4.1 Pre-registration maturation: PRU / PRDR / SOURCE-RECON
The March paper's "pre-registered gates" matured into a full **Pre-Registration Underspecification (PRU)** taxonomy. A gate is no longer just "pass/fail criterion defined before compute"; the *machinery* each gate depends on must also be pinned. **PRU Class 8.0–8.7** classifies under-specification failures (8.0/8.1 machinery-pin cardinality; 8.2 verifier-rubric; 8.3 output-precision; 8.4 representation-convention; 8.5 joint-hypersurface-form; 8.6 layered-substitution-chain; 8.7 degenerate-observable). **PRDR (Pre-Registration Dry-Run)** statically enumerates every free parameter before plan-freeze. **SOURCE-RECONCILIATION** is a separate 6-class drift taxonomy (a–f: PIN-TIGHT-SOURCE-LOOSE … PIN-PLACEHOLDER-PENDING-CANONICAL) that detects pinned-but-drifted values, commuting with PRU by construction. Pointer: `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"` + `§"Source Reconciliation"`; corpus `sessions/framework/registry/pru-class-corpus.md`; atlas-12 §IV. **This is the single largest gap between the March paper and current practice** — pre-registration went from a one-sentence principle to a multi-stage audit pipeline.

### 4.2 K-counter SUGGESTION→MANDATORY promotion contract
Methodology rules are not born mandatory. A new rule enters as **SUGGESTION (K=1)** and is promoted to **MANDATORY at K=3** — three *distinct* calibration instances (structurally distinct, not repeat-citations) accumulated in an **append-only, forward-only** corpus. This is the framework's mechanism for letting process discipline harden empirically rather than by fiat, and for preventing rule-rot and rule-inflation symmetrically. The K-counter discipline is itself governed by a meta-rule (`feedback_rules-compensate-missing-structure.md`: replace MANDATORY lists with examples/schemas/pointer-tables). Pointer: `feedback_rules-compensate-missing-structure.md`; per-rule K-status in each rule file's "Status" line; atlas-12 throughout. Worth a section because it is genuinely novel epistemic infrastructure: *graded, evidence-accumulating process rules*.

### 4.3 Wave classification M1–M4 + methodology-wave allowlist (recursion-attack closure)
Every wave in a session plan is classified at plan-freeze as **METHODOLOGY-class / COMPUTE-class / MIXED-class** by a strict 4-test conjunction (M1 PASS-predicate-type, M2 producing-operation-type, M3 source-of-truth-type, M4 allowlist-membership). METHODOLOGY-class waves skip compute-mode and are orchestrator-written; their PASS predicate is artifact-existence-with-substantive-content, not a numerical threshold. M4 requires the gate-ID to appear in an **append-only, orchestrator-only-edit allowlist** — and the orchestrator-only-edit rule exists specifically to close a **recursion attack**: without it, a subagent dispatched on a non-allowlisted gate could append its own gate-ID mid-execution and self-promote past the M1–M3 intent. Pointer: `.claude/rules/wave-classification.md`, `methodology-wave-allowlist.md`; ledger `sessions/framework/registry/methodology-wave-allowlist-ledger.md`; atlas-12 §§VI–VII. (The recursion-attack closure is a quotable, security-flavored vignette for the paper.)

### 4.4 Joint-theorem 4-stage promotion + Stage-2 two-agent cross-axis independent-verify
This is the **constructive answer to the paper's own implicit problem** — "agreement among agents is not evidence" (shared context produces shared output). A cross-axis joint theorem (clauses needing >1 methodological axis) advances: **Stage 0** workshop-internal candidate → **Stage 1** registered STAGE-1-CANDIDATE → **Stage 2** TWO independent cross-reviewers, one per axis, dispatched in parallel, **operating WITHOUT prior workshop context** (read only the registered entry, never the transcripts), with JOINT clauses PASS-AND'd → **Stage 3** STAGE-3-PERMANENT. The "without prior workshop context" condition is what makes the Stage-2 agreement *structurally independent* rather than shared-context agreement. There is an Axis-B selection protocol (axis-distinctness + original-author exclusion *with downstream-inheritance reach* + audit-coverage adequacy) and a substrate-input-orthogonality clause. A worked instance landed at S100a (§VII.AM Universal Lock Condition: three-agent cross-axis verify, 9/9 PASS-AND, promoted to PERMANENT). Pointer: `.claude/rules/joint-theorem-promotion.md`; atlas-12 §V; atlas-09 §"Suspected-but-Not-Yet-Retracted" (the S100a resolution). **This deserves its own section** — it is the paper's missing rigorous treatment of multi-agent agreement.

### 4.5 Dual-SHA verdict-line discipline + race-safe emit_verdict + v3 closure ladder + bounded recovery
Computation verdicts are emitted as append-only lines carrying a **dual SHA-256** pair: `content_sha256` (over the result) and `audit_sha256` (over the input-pin map, `closure_hash(pins)`). SHA-uniqueness across verdict lines is a checked invariant (a duplicate SHA signals a copy-pasted/hardcoded value rather than a computed closure — sig_5 of the v3 ladder). Verdicts are written through a **race-safe `emit_verdict` knowledge-MCP tool** (lock-serialized single writer; raw `open("a")` appends are non-atomic on Windows under parallel agents). The **v3 closure ladder** scores five signals (sig_1 PRU-zero … sig_5 SHA-uniqueness); failures route through a **bounded recovery procedure** (max 2 iterations/signal, proven-terminating, with a 4-item PROHIBITED_ACTIONS set — convention-shopping, iterate-until-PASS, post-hoc pre-registration editing, ansatz-forced PASS — that closes the iterate-until-PASS pathway *by construction*). Pointer: `.claude/rules/v3-closure-recovery.md`, `.claude/rules/gate-verdicts.md`; atlas-12 §II (layer-functor audit leg). This is the audit-floor that makes the "permanent verdict record" claim actually enforceable.

### 4.6 Mechanical-closure discipline (honest closure vs task-complete-lie)
A documented failure mode: an agent appends a verdict line then terminates *claiming completion* while the promised working-paper section is never written ("task-complete-lie"). The mechanical-closure rule specifies **honest closure** for upstream-blocked gates (5 conditions: upstream-block topology is the cause; verdict is FAIL/PRE-REG-INC never PASS; per-gate-distinct audit SHA; audit-trail signature naming the blocking prereq; working-paper update in-script in the same run). Plus a layer-separability carve-out (L1–L4 + Stage-2 PASS-AND) for closed-form Type-F sub-observables. Pointer: `.claude/rules/mechanical-closure-discipline.md`; `agent-standards.md §"Completion Verification"`; atlas-12 §X. (Pairs naturally with the paper's existing "agents lie about being done" finding — this is the *structural* fix for it.)

### 4.7 AMRI (Agent-Memory Registry Inversion) + memory-scope discipline
A discipline absent at S51: agent memory is for **agent-private context only** (this agent's feedback rules, spawn-time learnings) and is **never** the canonical home for data other gates cite. **AMRI** (3-test: input-pin / output-target / cross-agent-overlap) detects when a memory section has become a de-facto registry; such sections are migrated to `sessions/framework/registry/` + knowledge.db. Applies identically to per-agent memory AND orchestrator project memory (the user explicitly ruled the orchestrator's project memory in-scope: "you HAVE to follow AMRI; not [following] fully breaks the traceability"). ≥4 documented AMRI promotions. Pointer: `.claude/rules/agent-standards.md §"AMRI"`; detector `computations/_shared/_agent_memory_inversion_audit.py`; atlas-12 §VIII. (Directly upgrades the paper's §4.3 memory treatment.)

### 4.8 Capstone-hygiene 5-question gate
A standing status-synchronization discipline ensuring the curated capstone document's narrative confidence never exceeds the register status of each claim. Any session whose synthesis touches the capstone (or a capstone-governing register) runs a 5-question checklist (a(t)/Friedmann-gap; §7 falsifier-anchor row; PROVEN/CONDITIONAL/BROKEN/INFO status change; prose-claim-vs-ledger-row; citation add/invalidate) before close, routing each YES to a housekeeping fix. MANDATORY at K=3 as of S101. Pointer: `.claude/rules/capstone-hygiene-gate.md`; corpus `sessions/framework/registry/capstone-hygiene-corpus.md`. (A concrete instance of the K-counter contract in §4.2 and of the no-overclaiming discipline — good supporting example.)

### 4.9 Cross-pillar bridge anatomy (5-element IS-not-IN + 3-level confidence ladder)
The framework's mechanism for connecting a substrate-IS observable on one "pillar" to a laboratory-IN observable on another, without container-thinking conflation. Every registry bridge entry declares **5 anatomy elements** (substrate-IS observable / laboratory-IN observable / explicit bridge map [HKR / K-theory boundary / Connes-Karoubi pairing] / algebraic envelope L^−α / empirical anchor) and a **3-level structural-confidence ladder** (Level 1 cohomology-class identity, regulator-invariant; Level 2 algebraic convergence envelope, L_max-dependent; Level 3 empirical anchor at canonical L_max), with registry-PASS requiring Level-3 < Level-2. First bridge landed S86 (§VII.W); the K-counter reached MANDATORY at K=3 by S88. Pointer: `.claude/rules/cross-pillar-bridge-anatomy.md`; companion atlas `atlas-11-cross-pillar-bridge-corpus.md`. (This is substrate-side structure but is governed by methodology rules; a paragraph in the cross-domain section showing how cross-domain *bridges* are now formally typed would extend the SA-correlator case study into a general method.)

### 4.10 Workshop-vs-carry-forward Q1/Q2/Q3 discriminator + housekeeping ledgers
The paper's "workshop" format is now precisely defined (4 conditions: ≥2 agents with competing perspectives on a specific tension; genuine ledger-dissonance; multi-round R1/R2/R3; output is a structural verdict, not a queued computation) AND policed by a 3-question discriminator (Q1 math/physics adjudication → workshop; Q2 registry-hygiene/classification → carry-forward; Q3 parallel-compute-wave → carry-forward). The motivating failure: investigators padding "workshop" lists with carry-forward equations ("they're just listing carry-forward equations and bloviating" — user, S87). Q2/Q3 items route to per-session **housekeeping ledgers** (§A in-session fix / §B hygiene CF / §C parallel-wave / §D rule-extension / §E pre-compute-shell). Pointer: `.claude/rules/Investigating-Workshops.md`; template `.claude/templates/session-housekeeping.md`; atlas-12 §IX. (Sharpens the paper's §3 format taxonomy with the current, disciplined definitions.)

### 4.11 Knowledge infrastructure: index + SQLite/FTS5 MCP + routing manifest + `/weave`
The full stack (note H): `knowledge-index.json` (9 entity types, ~45 MB / 1.2M lines) → `tools/knowledge.db` (SQLite + FTS5, rebuilt by `/weave --db-sync`) → **knowledge MCP server** (FTS-ranked `search_knowledge`, `query_entity`, `trace_entity`, `get_constant`, race-safe `emit_verdict`; 11,637 calls logged with per-tool counters) → `routing_manifest.json` export (consumed by a separate Astro web build) → the `/weave --update` pipeline (extractor → audits → DB-sync → manifest). Query-first discipline is enforced by a PreToolUse hook ("verify the result isn't already known/closed/canonical before computing"). Pointer: `tools/` (README in CLAUDE.md §"Project Structure"); skill `.claude/skills/weave/`. **This is a major infrastructure contribution the March paper reduces to a single 30 MB JSON file** — it deserves its own section.

### 4.12 EVOI prioritization as a living table with staleness audit
Computation priority is set by **EVOI = P(pass)·|ΔP(pass)| + P(fail)·|ΔP(fail)|** — explicitly an *ordinal leverage proxy*, not a calibrated probability (the file carries a load-bearing honesty caveat against quoting 3-sig-fig EVOI as a measurement). The table is a *living* document with a **machine-readable currency tag** and a **staleness audit** (`_evoi_staleness_audit.py`: PASS at lag 0 / S2 at lag 1–2 / S1 MANDATORY at lag ≥3) that `/rclab-plan` consumes-and-maintains. There is a cautionary tale baked in: the table **content-froze for ~13 sessions (S83→S96) while broad commits git-touched its bytes** ("git-touched ≠ content-refreshed"), because no skill consumed it; the fix was enforcement wiring. Pointer: `.claude/rules/evoi-prioritization.md`; living table `sessions/evoi-framework.md`. (The froze-while-looking-maintained anecdote is a strong "what failed / what we fixed" vignette.)

### 4.13 Substrate-first framing rules as epistemic architecture
Two complementary framing disciplines treated as *epistemic infrastructure*, not stylistic preference: **`phononic-framing.md`** (explanation-direction axis — invert container-thinking; every explanation flows substrate→emergent; "IS Space, Not IN Space" with an explicit wrong/right correction table) and **`substrate-first-canonical-sourcing.md`** (sourcing axis — numerical pins must source from substrate-first computation, never external-paper provenance treated as authoritative; methodological-vs-canonical-citation distinction; SCHEMATIC-vs-FULL level-pin discipline). Both are enforced at the verifier-rubric and plan-freeze layers. Pointer: those two rule files; atlas-12 §XI. (Generalizes beyond this project as "domain-framing-as-pre-registration": the framing rule is the *negative-marker set* for a rubric, making it auditable.)

**Note H — infrastructure.** The knowledge MCP usage counter (11,637 total calls; search_knowledge 5,634, get_constant 3,624, trace_entity 1,183) is itself evidence of how load-bearing query-first discipline became — agents query the canonical graph thousands of times rather than recomputing. This is a quotable adoption metric.

---

## §5 — Bibliography Audit

The paper has **4** `\cite{needed:...}` placeholders (not 6; the prompt's count is off — verified by grep, all four are in `\begin{thebibliography}`):

| Placeholder | Current bibitem (as written) | Status | Proposed action |
|:--|:--|:--|:--|
| `needed:alphageometry` | Trinh et al., "Solving olympiad geometry without human demonstrations," *Nature*, 2024 | **REAL, details correct** — confirmed via arXiv (the AlphaGeometry2 follow-up 2502.03544 cites "Trinh et al., 2024" as the original Nature paper) | Remove `needed:` prefix; the citation is accurate as-is. Optionally add the AlphaGeometry2 follow-up (Chervonyi et al., 2025, arXiv:2502.03544) as a "since surpassed gold-medalist" update. |
| `needed:alphafold` | Jumper et al., "Highly accurate protein structure prediction with AlphaFold," *Nature* 596:583–589, 2021 | **REAL, details correct** — one of the most-cited papers in science; volume/pages accurate | Remove `needed:` prefix; accurate as-is. |
| `needed:gnome` | Merchant et al., "Scaling deep learning for materials discovery," *Nature* 624:80–85, 2023 | **REAL, details correct** — confirmed as a Nature materials-discovery paper (GNoME) | Remove `needed:` prefix; accurate as-is. |
| `needed:framework_paper` | R. Paasch, "Spectral geometry of Jensen-deformed SU(3)…," *in preparation*, 2026 | **GENUINE INTERNAL GAP** — this is the companion physics paper; "in preparation." Author attribution "R. Paasch" is suspect (Paasch is a *researcher whose work the project transcribes*, in `researchers/Paasch/`, not the project author — the author is Ryan Berry). | Either (a) cite the actual in-project standalone manuscripts that exist in `papers/` (alpha-s-ns, anderson-higgs, cmpp-classification, monotonicity, oz-spectral-index, spectral-action-monotonicity, weyl-tensor-cmpp), or (b) keep one "companion framework paper, in preparation" with the **correct author (Berry)**. Do NOT attribute the framework paper to Paasch. |

**Additional bibliography work for the rewrite (currently zero such citations exist):**
- **Multi-agent LLM / orchestration literature** — the paper makes claims about multi-agent methodology with no citations to the multi-agent-LLM field. Add real anchors (verify via paper-search before citing; do not cite from training knowledge per `feedback_research-corpus.md`).
- **The physics substrate-literature** the project actually builds on is already in `researchers/` (Volovik 37 papers, Van den Dungen 14, Baptista, Connes/NCG, etc.) — the framework paper should cite these; the *methodology* paper should at minimum cite the companion framework paper and the standalone results in `papers/`.
- **Pre-registration / open-science methodology** — the paper's central innovation (pre-registered gates) has a real precedent literature (pre-registration in empirical science, registered reports). One or two anchors would strengthen the generalizability claim without overreach.

**Discipline reminder for whoever does the bib:** per the project's research-corpus rule, every citation must be fetched/verified before it lands — no citing from memory. The three AI-for-science citations above are verified; anything new must be run through paper-search MCP first.

---

## §6 — Rewrite Plan (proposed section structure)

The current 9-section structure is sound as a skeleton but covers only the S1–S51 first-third. Recommended approach: **keep the skeleton, recount throughout, and insert a new Part (the methodology-floor era) between the current §5 and §6.** The atlas-12 / atlas-09 / atlas-10 documents are the curated sources; the rewrite is largely a publishable *rendering* of atlas-12 plus a recount.

**Front matter**
- Title: keep. Subtitle could add "across 100+ sessions" honestly.
- Authors: **Ryan Berry + Claude (Claude Code agent framework, Opus 4.6–4.8 generations)**, Anthropic affil. Fix the single-generation attribution.
- Date: update to the actual revision date; note the project is ongoing (S106+).
- Abstract: **full rewrite of every statistic** per §1; replace "current 2–4%" with the S51-value + S66-freeze + pending-re-anchoring framing; add one sentence naming the methodology-floor era as the principal post-S51 contribution.

**§1 Introduction** — keep the framing; update "51 sessions / 2,500 files / 29 agents" to the recounted figures with the "ongoing" caveat. Keep the three real AI-for-science citations (de-`needed:`'d).

**§2 Epistemic Discipline Framework** — keep core principles + source hierarchy + DISSOLVED category; recount the assumptions-registry tallies against current atlas-04. Add a forward-pointer sentence: "the pre-registration principle introduced here matured into the PRU/PRDR/SOURCE-RECON apparatus of §6."

**§3 Collaboration Formats** — keep the lessons; **re-map onto the rclab skill family** (§3.5 of this review); scope Table 1 (format comparison) explicitly as S16–S51 historical data and drop any implication it is a live quality metric.

**§4 Session Infrastructure** — keep carry-forward + memory + pipeline; **rename Collab-Plan/Collab-Team → rclab-plan/rclab-coordinate** and add the investigate/review/workshop/team/solo members; expand the Knowledge Index subsection into the full infrastructure stack (apparatus 4.11) or forward-point to a new infrastructure section.

**§5 Cross-Domain Research Correlation** — keep the SA-correlator case study (the paper's best asset); update "15 breakthroughs / 11 cross-domain" to the atlas-10 figures (39 catalogued) **with the layer-distinction warning reproduced** (methodology-floor breakthroughs do not raise substrate-physics probability); add one paragraph on cross-pillar bridge anatomy (4.9) as the *generalization* of the ad-hoc S50 cross-domain connection into a typed method.

**NEW §6 The Methodology-Floor Era (S78–S106)** — *the major addition; this is where atlas-12 becomes the spine.* Subsections, each from the apparatus inventory:
- §6.1 Pre-registration maturation: PRU Class 8 taxonomy + PRDR + SOURCE-RECON (apparatus 4.1)
- §6.2 Graded process rules: the K-counter SUGGESTION→MANDATORY contract + append-only forward-only corpora (4.2)
- §6.3 Wave classification M1–M4 + the methodology-wave allowlist recursion-attack closure (4.3)
- §6.4 Multi-agent agreement done right: the joint-theorem 4-stage pathway + Stage-2 context-free cross-axis verify — *the constructive answer to "agreement among agents is not evidence"* (4.4)
- §6.5 Enforceable verdict permanence: dual-SHA + race-safe emit_verdict + v3 ladder + bounded recovery (4.5)
- §6.6 Honest closure: mechanical-closure discipline vs the task-complete-lie (4.6)
- §6.7 Memory as agent-private context: AMRI + registry promotion (4.7)
- §6.8 Status synchronization: capstone-hygiene 5-question gate (4.8)
- §6.9 Substrate-first framing as auditable pre-registration (4.13)
- §6.10 Knowledge infrastructure: SQLite/FTS5 MCP + routing manifest + /weave (4.11)
- §6.11 Living prioritization: EVOI + staleness audit + the froze-while-looking-maintained cautionary tale (4.12)

**§7 Quantitative Assessment** — **rewrite around the current reporting methodology** (§3.7 of this review): present the trajectory with its sign changes AND the S66 freeze AND the substrate-physics/methodology-floor layer split; report retractions via the atlas-09 taxonomy (49 total, incl. SUPERSESSION + interpretive-DOF-rescoping categories); **remove session-aggregate vanity metrics** (PASS/FAIL ratios, discovery-rate-per-session as quality) or scope them strictly as S1–S51 historical description. Add the effort-based-probability + EVOI explanation as the *replacement* diagnostic.

**§8 Lessons Learned** — keep; add the post-S51 lessons (the S87 "investigators bloviate carry-forwards as workshops" correction; the EVOI froze-silently lesson; the task-complete-lie discovery; the AMRI traceability lesson; the recursion-attack closure). These are stronger "what failed / what we fixed" material than some of the S1–S51 items.

**§9 Discussion** — keep generalizability + human-role + limitations; update the MEMORY.md limitation (institutional knowledge now in queryable registries, partly addressing the compression-loss limitation); update the scalability limitation (peaked at ~23 parallel agents — verify current max).

**§10 Conclusion** — keep the "rules matter more than agents" thesis; it is *more* supported now. Update the closing statistics; replace the "2%→52%→2–4%" arc sentence with the honest frozen-since-S66 framing.

**Bibliography** — §5 of this review.

---

## §7 — Verdict: **RESTRUCTURE**

Not REWRITE-IN-PLACE (the changes are too large — a whole methodology era, ~22+ sessions of apparatus, is missing, and every statistic is stale), and not RETIRE-AND-REPLACE (the spine is sound, the central thesis is *more* supported now, and the SA-correlator case study and DISSOLVED-category material are genuinely good and reusable).

**Rationale.** The paper is an accurate, well-written account of the project's *first third* (S1–S51) and its thesis — that the epistemic architecture is the invariant and the agents are the variables — is the right thesis, now corroborated by the entire S78–S106 methodology-floor era that the paper predates. But three things force RESTRUCTURE rather than a light touch: (1) **every quantitative claim is an S51 snapshot** and several (sessions 51→≥106, theorems 392→2301, scripts 630→3128, retractions 25→49, breakthroughs 15→39) are off by multiples — while one (equations 80,497→19,713) must be honestly corrected *downward*; (2) the **probability headline ("current 2–4%") is, for a paper about honest Bayesian assessment, the most serious flaw** — it quotes the S51 value as current when the framework deliberately stopped producing a calibrated number after S66 and the re-anchoring is still pending; (3) the **single most defensible methodological contribution of the project did not exist when the paper was written** — the PRU/PRDR/SOURCE-RECON pre-registration apparatus, the K-counter graded-rule contract, the joint-theorem context-free cross-axis verify (which is precisely the rigorous answer to the paper's own unstated "agreement isn't evidence" problem), dual-SHA verdict permanence, AMRI, the knowledge MCP infrastructure, and the substrate-first framing-as-pre-registration discipline. A paper claiming to describe "the epistemic architecture for orchestrated AI research" that omits the entire methodology-floor era under-sells the actual contribution. The fix is additive and structural: keep the spine, recount honestly (every number with its method), and render atlas-12 into a new Part. The result is a substantially stronger paper that finally matches the project it describes.

---

### Source pointers used in this review (all absolute)
- Paper under review: `C:\sandbox\Ainulindale Exflation\papers\methodology\orchestrated-ai-research.tex`
- Probability trajectory: `C:\sandbox\Ainulindale Exflation\sessions\framework\Atlas\atlas-06-probability-trajectory.md`
- Methodology floor (rewrite spine): `C:\sandbox\Ainulindale Exflation\sessions\framework\Atlas\atlas-12-methodology-floor.md`
- Retraction log: `C:\sandbox\Ainulindale Exflation\sessions\framework\Atlas\atlas-09-retractions.md`
- Breakthrough genealogy: `C:\sandbox\Ainulindale Exflation\sessions\framework\Atlas\atlas-10-breakthrough-genealogy.md`
- EVOI living table (currency S106): `C:\sandbox\Ainulindale Exflation\sessions\evoi-framework.md`
- Entity counts: `C:\sandbox\Ainulindale Exflation\tools\knowledge.db` (via knowledge MCP / SQLite)
- Rule corpus: `C:\sandbox\Ainulindale Exflation\.claude\rules\` (epistemic-discipline, wave-classification, joint-theorem-promotion, v3-closure-recovery, mechanical-closure-discipline, agent-standards, capstone-hygiene-gate, cross-pillar-bridge-anatomy, Investigating-Workshops, evoi-prioritization, phononic-framing, substrate-first-canonical-sourcing, methodology-wave-allowlist)
- Agent definitions: `C:\sandbox\Ainulindale Exflation\.claude\agents\` (34 `.md` files)
