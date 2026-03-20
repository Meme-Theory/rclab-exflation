# Session 16: Workshop — Substrate Mass Spectrum: From Geometry to Prediction

## Date: 2026-02-13
## Format: Parallel Small-Group Rounds with Markdown Handoff
## Architecture: Max 2-3 agents per team discussion. Files on disk between rounds. Fresh context per round.

---

## DESIGN PRINCIPLES

1. **Context control**: Each conversation gets only the combined handout + prior round outputs. No bloat.
2. **Natural groupings**: Agents pair by task affinity ("coffee talks"), not by team assignment.
3. **Markdown handoff**: Every round writes a `.md` output file. That file IS the round's deliverable.
4. **Dynamic routing**: Round 2 group composition emerges from Round 1 findings. Round 3 emerges from Round 2.
5. **No progressive reveals**: The combined handout (`session-16-combined-handout.md`) contains EVERYTHING.
6. **Orchestrator (Claude Code) drives**: Spawns each subround's team in parallel. Coordinator agent is a note-taker/compiler within each team, NOT a dispatcher.
7. **Strictly sequential**: One team at a time. Team completes and writes its markdown file. Next team starts with all prior outputs. No parallel launches.

---

## INPUT DOCUMENT (ALL ROUNDS)

`session-16-combined-handout.md` — contains:
- Part A: All proven/suggestive/null/refuted results from Sessions 7-15
- Part B: Phase 2B simulation validation (all 6 subtasks with data)
- Part C: PI's three corrections (G decomposition, kappa as computation, wrong test)
- Part D: Priority stack
- Part E: Baptista Papers 17/18 critical path

**Every agent reads this. No agent is information-starved.**

---

## ROUND 1: ASSESSMENT COFFEE TALKS

### Purpose
Small, natural pairs assess the combined handout from their domain perspective. Each pair produces a focused markdown assessment. These assessments become input for Round 2.

### Round 1a — Geometry Coffee (KK-theorist + Baptista-analyst)
**Affinity**: These two share the geometric/spectral triple territory.

Input: Combined handout only.

Each agent reads the handout and they discuss:
- Which proven results are load-bearing vs decorative?
- D_K critical path: What's actually needed from Papers 17/18 to proceed?
- Jensen metric status: Is s the right parameterization, or is there a better one?
- The (3,0) sector: Is U(2)-singlet status confirmed? What does Parthasarathy really mean?
- Assessment of the "wrong operator" claim (Part C.III): How different is D(SU(3)) from D_K(CP^2)?

Output format: `sessions/session-16-round-1a-geometry.md`
- 3 strongest geometric results (ranked)
- 3 most urgent geometric computations (ranked)
- D_K feasibility estimate: GREEN/YELLOW/RED with justification
- Any disagreements between KK and Baptista

### Round 1b — Spectrum Coffee (Gen-physicist + Paasch-analyst)
**Affinity**: These two share the eigenvalue/mass ratio territory.

Input: Combined handout only.

Discussion topics:
- Phi analysis honest final assessment: Is z=3.65 real or an artifact of look-elsewhere?
- Mass spiral status: What exactly survives? What's definitively closed?
- Statistical methodology: What MC protocol should Round 2 agents follow for new claims?
- The Z_3 swing vote: What specific prediction does Paasch make for inter-generation ratios?
- Phase 2B d_pair_factor: Does this hidden parameter invalidate the D/H result?

Output format: `sessions/session-16-round-1b-spectrum.md`
- Phi status: one-paragraph honest summary
- Paasch survival scorecard (claim-by-claim: alive/closed/untested)
- Pre-registered predictions: Exact mass ratios with exact thresholds, written BEFORE computation
- Statistical protocol for Round 2

### Round 1c — Computation Coffee (QA-theorist + Sim-specialist)
**Affinity**: These two share the "how do we actually compute this" territory.

Input: Combined handout only.

Discussion topics:
- QM derivation status: What's theorem-level, what's hand-waving, what's open?
- Phonon-NCG dictionary: Final honest scoring (which entries are rigorous, which wrong?)
- Simulation validation: What does Phase 2B actually tell us vs what we wish it told us?
- Computational feasibility landscape: What can we compute in days vs weeks vs months?
- V_eff implementation: Exact code plan (modify tier1_spectral_action.py? new script?)
- BdG class DIII: Is the "topological superconductor" analogy deep or shallow?

Output format: `sessions/session-16-round-1c-computation.md`
- Feasibility table: every proposed computation with GREEN/YELLOW/RED + timeline
- V_eff implementation spec (code paths, estimated LOC, runtime)
- Phonon-NCG dictionary update (9 entries rescored)
- QM derivation status: theorem / defensible / open / broken (for each piece)

### Round 1d — Giants First Read (Einstein + Feynman)
**Affinity**: The principle-theorist and the calculator. Complementary lenses.

Input: Combined handout + Round 1a + 1b + 1c outputs.

**The key moment**: Each Giant reads everything cold and restates the core problem IN THEIR OWN LANGUAGE. Not "is the Paasch spiral correct" but the problem underneath:

- **Einstein**: The geometric/symmetry version. What invariance principle constrains the spectrum?
- **Feynman**: The calculational version. What's the path integral? What physical process gives a mass spectrum?

Then they identify:
- What did the Round 1 assessments miss or underweight?
- What's the cheapest computation that most changes probability?
- One counterintuitive idea each.

Output format: `sessions/session-16-round-1d-einstein-feynman.md`
- Einstein's restatement (1 paragraph, his language)
- Feynman's restatement (1 paragraph, his language)
- Their "cheapest decisive computation" picks
- One counterintuitive idea each

### Round 1e — Giants First Read II (Hawking + Sagan)
**Affinity**: The thermodynamicist and the empiricist. Complementary lenses.

Input: Combined handout + Round 1a + 1b + 1c outputs + Round 1d output.

Same exercise:
- **Hawking**: The thermodynamic/information version. What entropy bound organizes the excitations?
- **Sagan**: The empirical/observational version. What observation distinguishes this from alternatives?

Plus:
- Hawking: Species bound calculation, CW = entropy maximum assessment
- Sagan: Pre-registration demands, external scorecard, probability with Bayesian reasoning

Output format: `sessions/session-16-round-1e-hawking-sagan.md`
- Hawking's restatement (1 paragraph, his language)
- Sagan's restatement (1 paragraph, his language)
- Hawking's thermodynamic constraints on s_0
- Sagan's pre-registration demands (binding failure criteria)
- Their probability estimates with explicit reasoning

---

## ROUND 2: DEEP DIVES (Parallel Small Teams)

### Purpose
Focused technical work in natural groups. Each group tackles a specific problem thread as a team — agents discuss freely in parallel within each subround. Group composition is informed by Round 1 outputs.

### Round 2a — V_eff Deep Dive (KK-theorist + Gen-physicist + Sim-specialist)
**Task**: The #1 priority computation. Specify the full spectral 1-loop V_eff.

Input: Combined handout + all Round 1 outputs.

All three agents are launched as teammates and discuss:
- **KK-theorist** brings: Eigenvalue catalog for the sum. Which lambda_n(s) and d_n go into V_1-loop? Peter-Weyl degeneracies at p+q <= 6. Truncation error bounds.
- **Gen-physicist** brings: MC protocol for the result. Null model for testing the minimum. Convergence criteria. The exact formula with all indices.
- **Sim-specialist** brings: Implementation plan. Which files, what modifications, estimated runtime. Pseudocode for the 1-loop sum. Numerical hazards (overflow, cancellation).

The team converges on a joint specification through discussion.

Output: `sessions/session-16-round-2a-veff.md`
- Complete V_eff formula with all terms enumerated
- Code specification (pseudocode -> real code plan)
- Numerical hazard analysis
- Pass/fail criteria for the computation
- Timeline and dependencies

### Round 2b — D_K and Generations (Baptista-analyst + KK-theorist)
**Task**: The D_K on CP^2 question and Z_3 generation mechanism.

Input: Combined handout + Round 1a + Round 2a.

Both agents discuss as teammates:
- **Baptista-analyst** brings: D_K projection exact specification from Paper 17. Peter-Weyl decomposition changes for CP^2 vs SU(3). Z_3 mechanism from Paper 18.
- **KK-theorist** brings: Code-level assessment. What changes in tier1_dirac_spectrum.py? Matrix sizes, new basis, computational cost.

They negotiate the specification together — Baptista provides the math, KK reality-checks the implementation.

Output: `sessions/session-16-round-2b-dk-generations.md`
- D_K mathematical specification (equations, not words)
- CP^2 vs SU(3) spectral comparison (what changes, what's preserved)
- Z_3 test procedure (step-by-step)
- Code modification plan
- Feasibility: GREEN/YELLOW/RED with timeline

### Round 2c — Theoretical Frontiers (QA-theorist + Paasch-analyst)
**Task**: Bell inequality path, phonon-NCG breaks, correct Paasch test.

Input: Combined handout + Round 1b + Round 1c.

Both agents discuss as teammates:
- **QA-theorist** brings: Bell via BdG topology roadmap. Finite-T spectral corrections formula. Where the phonon analogy breaks. Path from class DIII to CHSH > 2.
- **Paasch-analyst** brings: Correct test specification lambda_i/lambda_j = N(i)^{3/2}/N(j)^{3/2}. Pre-registered prediction table. Z_3 inter-generation prediction (non-uniform splitting pattern).

They cross-check each other — QA challenges Paasch's predictions, Paasch challenges QA's Bell roadmap.

Output: `sessions/session-16-round-2c-theory.md`
- Bell roadmap (steps, obstacles, timeline)
- Paasch prediction table (binding, pre-registered)
- Phonon-NCG dictionary final update
- Where analogy breaks: fixable vs fundamental

### Round 2d — Giants Evaluate Everything (two parallel pairs)
**Task**: Evaluate all Round 2 work. Produce the definitive ranking.

Input: Combined handout + all Round 1 + all Round 2a-c outputs.

Two parallel team discussions (can run simultaneously):

**2d-i: Einstein + Feynman** (team discussion)
- Which Round 2 proposals are geometrically well-motivated vs ad hoc? (Einstein)
- Which proposals actually compute something vs hand-wave? (Feynman)
- Joint ranking of all proposed computations
- Feynman's "4-step machine" specification if applicable
- Updated probability estimates

**2d-ii: Hawking + Sagan** (team discussion)
- Thermodynamic constraints on proposed computations (Hawking)
- Are the pre-registered predictions falsifiable? (Sagan)
- Species bound implications (Hawking)
- External scorecard update (Sagan)
- Updated probability estimates

Output: `sessions/session-16-round-2d-giants-eval.md` (merged from both pairs)
- Joint Giant ranking of all proposals (decisiveness x feasibility x novelty)
- Probability estimates (4 Giants)
- Identified convergences and divergences
- "If I had one week" — each Giant's pick for single best use of time

---

## ROUND 3: PEN TO PAPER

### Purpose
Convert all prior rounds into actionable items. Every idea becomes a Test, Formula, Simulation, or Axiom. Better balanced across all agents.

### Round 3a — Computational Action Items (KK-theorist + Sim-specialist)
**Task**: Turn V_eff, D_K, Seeley-DeWitt proposals into executable specs.

Input: Combined handout + Round 2a + Round 2b + Round 2d.

Produce:
- V_eff implementation: FINAL code spec (files, functions, line ranges, estimated runtime)
- D_K feasibility: exact scope of work, dependencies
- All computational items in the standard format (see below)
- Hardware requirements and risk factors

Output: `sessions/session-16-round-3a-computational.md`

### Round 3b — Theoretical Action Items (QA-theorist + Baptista-analyst + Paasch-analyst)
**Task**: Turn Bell, Z_3, order-one, G-decomposition proposals into executable specs.

Input: Combined handout + Round 2b + Round 2c + Round 2d.

Produce:
- Z_3 test: exact procedure, pass/fail, prerequisites
- Bell roadmap: milestones, dependencies, what would constitute progress
- G-decomposition: which equations to rewrite, in what order
- Paasch pre-registration: FINAL binding prediction table
- All theoretical items in standard format

Output: `sessions/session-16-round-3b-theoretical.md`

### Round 3c — Priority Ranking and Pre-Registration (Gen-physicist + Sagan)
**Task**: Rank everything. Bind the failure criteria. Statistical protocol.

Input: Combined handout + Round 3a + Round 3b + Round 2d.

Produce:
- **Master ranked action list** (decisiveness x feasibility), merging 3a and 3b
- Pre-registration document: binding failure criteria for each computation
- MC protocol for any new claims
- Bayesian framework probability update methodology
- "Swing vote" identification: which single result most changes probability

Output: `sessions/session-16-round-3c-priorities.md`

### Round 3d — Final Synthesis (OPTIONAL — dynamic Giant pair chosen based on need)
**Task**: Sanity check the action list. Catch anything missed.

Input: Combined handout + Round 3a + 3b + 3c.

This round is OPTIONAL and DYNAMIC. The orchestrator (Claude Code) only launches it if:
- Round 3c reveals a disagreement that needs Giant arbitration
- A proposed computation has unclear physical motivation
- The ranked list doesn't have a clear #1 priority

Which Giant pair depends on the nature of the gap:
- Geometric/structural question → Einstein + Feynman
- Thermodynamic/empirical question → Hawking + Sagan
- Cross-cutting → one from each pair

If launched, produce: `sessions/session-16-round-3d-synthesis.md`
If not needed, orchestrator notes why and proceeds to final compilation.

### Final Compilation (Coordinator agent or orchestrator)

Reads all Round 3 outputs and writes:

`sessions/session-16-final.md`
- Complete ranked action list with all metadata
- Updated framework probability (workshop consensus)
- Swing vote computations
- Pre-registration document
- Session 16 summary paragraph
- Seeds for Session 17

---

## ACTION ITEM FORMAT

Every item in Round 3 must use this format:

```
## [RANK]. [NAME]
- Type: Test / Formula / Simulation / Axiom
- Specification: [exact computation or statement]
- Pass/Fail: [what constitutes success/failure]
- Feasibility: GREEN / YELLOW / RED
- Timeline: [hours / days / weeks]
- Owner: [agent name]
- Decisiveness: [1-10, where 10 = most changes probability]
- Dependencies: [what must be done first]
- Code: [which files, what modifications]
```

---

## CONVERSATION STRUCTURE

### Sequential execution (one team at a time)

| Step | Subround | Team | Input |
|------|----------|------|-------|
| 1 | 1a | KK + Baptista | handout |
| 2 | 1b | Gen + Paasch | handout + 1a |
| 3 | 1c | QA + Sim | handout + 1a + 1b |
| 4 | 1d | Einstein + Feynman | handout + 1a + 1b + 1c |
| 5 | 1e | Hawking + Sagan | handout + 1a + 1b + 1c + 1d |
| 6 | 2a | KK + Gen + Sim | handout + all R1 |
| 7 | 2b | Baptista + KK | handout + R1 + R2a |
| 8 | 2c | QA + Paasch | handout + R1 + R2a + R2b |
| 9 | 2d-i | Einstein + Feynman | handout + all R1 + R2a-c |
| 10 | 2d-ii | Hawking + Sagan | handout + all R1 + R2a-c + R2d-i |
| 11 | 3a | KK + Sim | handout + R2a + R2b + R2d |
| 12 | 3b | QA + Baptista + Paasch | handout + R2b + R2c + R2d |
| 13 | 3c | Gen + Sagan | handout + R3a + R3b + R2d |
| 14 | 3d | [dynamic Giant pair] | handout + R3a + R3b + R3c |

**14 steps, strictly sequential. One team runs at a time. Each team completes and writes its markdown file before the next team starts. Each subsequent team gets all prior outputs as additional input.**

### Execution order
```
Step 1:  [1a: KK+Bap]
Step 2:  [1b: Gen+Paa]
Step 3:  [1c: QA+Sim]
Step 4:  [1d: Ein+Fey]
Step 5:  [1e: Haw+Sag]
Step 6:  [2a: KK+Gen+Sim]
Step 7:  [2b: Bap+KK]
Step 8:  [2c: QA+Paa]
Step 9:  [2d-i: Ein+Fey]
Step 10: [2d-ii: Haw+Sag]
Step 11: [3a: KK+Sim]
Step 12: [3b: QA+Bap+Paa]
Step 13: [3c: Gen+Sag]
Step 14: [3d: dynamic] (optional)
```

---

## ROLES

### Orchestrator (Claude Code)
The orchestrator (you, Claude Code) manages the session:
1. **Spawns** one team at a time via the Task tool — never more than one team running
2. **Waits** for team to complete and write its markdown output file
3. **Verifies** output file exists on disk before starting the next team
4. **Routes** subsequent teams based on prior output — adjusts composition if needed
5. **Decides** whether optional Round 3d is needed based on Round 3c output

### Coordinator Agent (physics-coordinator)
Optional participant within teams that need note-taking or cross-referencing:
1. **Takes minutes** during team discussions
2. **Cross-references** prior round outputs when agents need context
3. **Synthesizes** convergences and divergences at discussion end
4. **Does NOT** add physics opinions — tracks, compiles, and surfaces patterns
5. **NOT required** in every team — only where the discussion benefits from a dedicated note-taker (e.g., 2d, 3c)

---

## AGENT APPEARANCE TABLE

Each agent appears in exactly these rounds:

| Agent | R1 | R2 | R3 | Total Appearances |
|-------|----|----|----|----|
| KK-theorist | 1a | 2a, 2b | 3a | 4 |
| Baptista-analyst | 1a | 2b | 3b | 3 |
| Gen-physicist | 1b | 2a | 3c | 3 |
| Paasch-analyst | 1b | 2c | 3b | 3 |
| QA-theorist | 1c | 2c | 3b | 3 |
| Sim-specialist | 1c | 2a | 3a | 3 |
| Einstein | 1d | 2d-i | (3d) | 2-3 |
| Feynman | 1d | 2d-i | (3d) | 2-3 |
| Hawking | 1e | 2d-ii | (3d) | 2-3 |
| Sagan | 1e | 2d-ii | 3c | 3 |
| Coordinator | -- | (2d) | (3c) | 0-2 (as needed) |

Balanced: every specialist appears 3-4 times. Every Giant appears 2-3 times. Coordinator only joins where note-taking adds value. No agent is overloaded. No agent is sidelined.

---

## SUCCESS CRITERIA

The session succeeds if:
1. At least one Giant reframes a problem in a way that changes approach
2. At least one structural gap gets a concrete novel attack vector
3. Round 3 produces >= 5 actionable items with feasibility estimates
4. No agent leaves defending the same position they walked in with
5. The pre-registration document is binding and specific

The session fails if:
- Round 2 reproduces Session 15 priority list with no new entries
- Any agent retreats to defended positions instead of building
- Round 3 action items are vague ("investigate X" instead of "compute X")
- The workshop format collapses into debate

---

## WHAT'S DIFFERENT FROM THE ORIGINAL AGENDA

| Original | Replanned |
|----------|-----------|
| 10+ agents in one conversation (Round 1) | 2-3 agents per conversation throughout |
| Progressive reveal (handout withheld until Round 2) | Combined handout given to everyone upfront |
| Team Exflate vs Team Giant (tribal) | Natural pairs by task affinity (collaborative) |
| Round 2 unstructured "open forum" | Round 2 structured deep dives by topic |
| Round 3 only KK + Sim + spot checks | Round 3 balanced across all agents |
| 5 conversations total | 14 sequential team discussions |
| Serial agents within rounds | 2-3 agents per team, one team at a time |
| Context explosion risk | Context controlled by markdown handoff between waves |
