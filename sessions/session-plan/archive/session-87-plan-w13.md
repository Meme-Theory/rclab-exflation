# Session 87 Plan — Wave 13: Path-B Precursor (Step-0 Workshop + NC Two-Torus)

**Wave-owner**: `gen-physicist` (orchestrator) for PB-1 4-agent panel; `spectral-geometer` (mathematics owner) + `gen-physicist` (compute integration) for PB-2.

**Schema version**: R3
**Verdict source**: `computations/s87_gate_verdicts.txt`

---

## Wave 13 Summary

Wave 13 is the **Path-B precursor wave**: two carry-forward items (PB-1, PB-2) sourced verbatim from `sessions/archive/session-86/session-86-path-b-carry-forward.md` (D2 workshop closure 2026-04-27). Path-B is the substrate-simulator implementation track that follows the S86 Path-B D2 workshop's CLOSED-FOR-CAUSE verdict on the bare-spectral-action gradient flow (NCG axioms + heat-kernel + Volovik analog + S38 GGE-permanence converged on the closure). Before the combined RQ-1+RQ-3 simulator architecture freezes for S87+ implementation work, two pieces of upstream theory + infrastructure must land:

1. **§W13-1 `S87-PATH-B-STEP-0-WORKSHOP` (PB-1)** — combined-scope pre-implementation workshop closing 4 research questions (NC fiber discretization #1, cold-start vacuum #2, matching prescription #3, P2→P3/P3→P4 hand-off fidelity #7). Output: a frozen architecture spec document at `sessions/framework/path-b-architecture-spec-frozen.md` that the implementation phase builds against without further theory decisions. Workshop-format gate (no `.py` script); 4-agent panel via `/rclab-team` (multi-agent coordinated) OR `/rclab-workshop` 2-pair sequential. PASS = all 4 RQs resolve; INFO = 1-3 resolve; FAIL = blocking-level theory questions surface.

2. **§W13-2 `S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION` (PB-2)** — gradient-flow simulator validation on the Connes-Landi noncommutative two-torus with Floricel-Ghorbanpour-Khalkhali (FGK 1612.06688) closed-form Ricci density. Compute gate (full 13-field spec); validate `dD/dτ = -Ric(D)/G_BKM` recovers the analytic flat-metric fixed point. PASS iff `‖h_terminal − h_flat‖_{L²} < 10⁻⁴` at τ_max=100; FAIL if `> 10⁻²` or divergence; INFO band `10⁻⁴ ≤ … ≤ 10⁻²`. Reusable infrastructure validation for any future Path B simulator work.

**Substrate framing** — Wave 13 is GEOMETRIC (toy NCG validation for PB-2) and METHODOLOGY-adjacent (architecture-spec-freezing workshop for PB-1). PB-2's NC two-torus is NOT a model of the substrate fiber; it is a validation surface for the gradient-flow + spectral-mode + GPU-eigenvalue infrastructure that PB-2's PASS certifies as ready for the substrate's own SU(3) fiber simulator. The substrate IS the spectral triple `(A_K, H_K, D_K)` on Jensen-deformed SU(3); PB-2's NC 2-torus is a laboratory test surface chosen because FGK 1612.06688 supplies a closed-form Ricci density and the analytic flat-metric fixed point provides a ground-truth target. PB-1's workshop fixes the architecture choices (mode truncation, cold-start vacuum, matching prescription, P2→P3/P3→P4 hand-off layers) that the substrate simulator will require — the 4 questions are theory questions about the substrate's own internal geometry, not about a container in which the substrate sits.

**Sequencing constraint**: PB-1 PRECEDES PB-2 implementation. Per `session-86-path-b-carry-forward.md` lines 238-242: "PB-1 should land before PB-2 begins implementation, because PB-1's frozen architecture document specifies the modulus and metric choices that PB-2 implements. If PB-1 returns a BLOCKED verdict on any of the 4 research questions, PB-2 should be paused until the underlying research question is closed in a separate session." This sequencing is encoded as the **conditional-block predicate** in PB-2's gate block (§W13-2.6 below).

---

## Wave 13 Decision Point Prerequisites

| Prerequisite | Source | Verification at plan-freeze |
|:-------------|:-------|:----------------------------|
| `sessions/framework/registry/path-b-d2-workshop.md` exists with all three rounds verified on disk | S86 Path-B D2 workshop closure | `ls -la` at plan-freeze; cite SHA |
| `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` exists with 7 RQs enumerated | S86 combined R&D plan | `ls -la` at plan-freeze; cite SHA |
| `sessions/framework/registry/path-b-rq1-inner-fluctuation-simulator.md` exists (RQ-1 standalone reference) | S86 RQ-1 reference | optional cross-cite |
| `sessions/framework/registry/path-b-rq3-phase-transition-simulator.md` exists (RQ-3 standalone reference) | S86 RQ-3 reference | optional cross-cite |
| `computations/s85_w6_acoustic_white_hole_formal.py` exists (canonical matching prescription source) | S85 W6 closure | `ls -la` at plan-freeze; cite SHA |
| `computations/s52_bogoliubov_amp.npz` exists (existing Bogoliubov amplitude data) | S52 closure | `ls -la` at plan-freeze; cite SHA |
| `computations/canonical_constants.py` exists (S86-close state) | S86 close | `ls -la` at plan-freeze; cite SHA |
| `computations/s87_gate_verdicts.txt` writable (will be created at first W13-2 emission if not pre-existing) | session-fresh | `touch` if missing |
| Static `D_K(τ_fold)` infrastructure operational | computations/_shared | spot-check via S86 W12-* eigenvalue cache |
| Agent memories for connes-ncg-theorist, spectral-geometer, transit-dynamics-theorist, volovik-superfluid-universe-theorist available | `.claude/agent-memory/*/MEMORY.md` | implicit (agent dispatch validates) |
| Tooling: `/rclab-team` skill OR `/rclab-workshop` skill operational | `.claude/skills/rclab-*` | implicit |
| GPU path: AMD RX 9070 XT (ROCm 7.2 / torch 2.9.1+rocm) accessible from `phonon-exflation-sim/.venv312/Scripts/python.exe` | `.claude/rules/computation-environment.md` | confirmed by environment-rule pin |
| FGK 1612.06688 paper (citation pin only; no on-disk SHA needed) | external arXiv | citation-pin |
| DKvS 1903.09624 paper (citation pin only; no on-disk SHA needed) | external arXiv | citation-pin |

If any of the above prerequisites is missing at runtime, the wave dispatch halts with a PRE-REG-INC mechanical-closure verdict per `.claude/rules/mechanical-closure-discipline.md`.

---

## §W13-1. S87-PATH-B-STEP-0-WORKSHOP (PB-1)

### §W13-1.1 Gate metadata

```yaml
gate_id: S87-PATH-B-STEP-0-WORKSHOP
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
class: WORKSHOP
classification_axis: METHODOLOGY-adjacent (architecture-spec-freeze workshop;
                     output is a registry-grade frozen-spec document, not a
                     numerical pre-registered threshold)
trigger: [VERIFY] [SUBSTRATE-FIRST]
wave: W13
slot: §W13-1
sequencing: PB-1 PRECEDES PB-2 (conditional-block predicate; see §W13-2.6)
recommending_agent: gen-physicist (orchestrator) + 4-agent panel
                    (connes-ncg-theorist + spectral-geometer
                     + transit-dynamics-theorist
                     + volovik-superfluid-universe-theorist)
effort_estimate: ~2 days (1 day workshop dispatch + 1 day synthesis to spec freeze)
source: sessions/archive/session-86/session-86-path-b-carry-forward.md path-b file lines 30-101
```

### §W13-1.2 What

Combined-scope pre-implementation workshop to close 4 research questions before the RQ-1+RQ-3 simulator architecture freezes. Output: an architecture spec freeze document (`sessions/framework/path-b-architecture-spec-frozen.md`) that the S87+ implementation phase builds against without further theory decisions.

The 4 research questions to close (verbatim from `session-86-path-b-carry-forward.md` lines 48-65):

1. **Time-discretization on the noncommutative SU(3) fiber** — mode-truncation using static `D_K` eigenmodes is the natural fit, but the truncation-error vs. mode-count tradeoff is uncharacterized. Decision deliverable: explicit choice of truncation scheme (e.g., `L_max=10` energy-cap or multipole-cap) with a substrate-derived error bound for the chosen scheme.
2. **Initial-condition class for cold start** — vacuum two-point functions on the noncommutative SU(3) fiber need explicit transcription. Decision deliverable: specific lifted Bunch-Davies-analog two-point function form on noncommutative SU(3), with a substrate-first canonical sourcing pointer (per `.claude/rules/substrate-first-canonical-sourcing.md`).
3. **Matching prescription at the τ_fold boundary** — Israel / Andreev / Painlevé-Gullstrand alternatives. Decision deliverable: pre-register `s85_w6_acoustic_white_hole_formal.py`'s Painlevé-Gullstrand-style match as canonical with the alternatives flagged as variants for downstream sensitivity analysis.
4. **Phase-coupling hand-off fidelity at P2→P3 and P3→P4** — combined-only research question; the joint architecture introduces translation layers absent from standalone RQ-1 / RQ-3 plans. Decision deliverable: explicit translation-layer specification (mode-amplitude basis ↔ field-configuration basis transforms, with the substrate-derived map written out, dimensions checked).

(Research questions #4, #5, #6 from the combined plan are deferred to mid-implementation workshops because they require initial implementation experience to be answerable. Question #7 here is **#7 of the original 7-question enumeration**, which by the convention used in `session-86-path-b-carry-forward.md` becomes the 4th close-now item alongside #1, #2, #3.)

### §W13-1.3 Inputs (file-level)

Per `session-86-path-b-carry-forward.md` lines 79-87:

- `sessions/framework/registry/path-b-d2-workshop.md` — workshop closure (read in full)
- `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` — combined R&D plan with 7 research questions enumerated
- `sessions/framework/registry/path-b-rq1-inner-fluctuation-simulator.md` — RQ-1 standalone (reference)
- `sessions/framework/registry/path-b-rq3-phase-transition-simulator.md` — RQ-3 standalone (reference)
- `computations/s85_w6_acoustic_white_hole_formal.py` — canonical matching prescription source
- `computations/s52_bogoliubov_amp.npz` — existing Bogoliubov amplitude data
- Existing static `D_K(τ_fold)` infrastructure (computations/_shared; substrate eigenvalue cache from S86 W12-* / S84 W10a-*)
- Agent memories (read at dispatch time): `.claude/agent-memory/connes-ncg-theorist/MEMORY.md`, `.claude/agent-memory/spectral-geometer/MEMORY.md`, `.claude/agent-memory/transit-dynamics-theorist/MEMORY.md`, `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`

### §W13-1.4 Workshop format

Per `session-86-path-b-carry-forward.md` lines 41-46, two format options are pre-registered. The S87 plan-author at plan-freeze time MUST select one of the two (this plan pre-registers both as admissible; the orchestrator picks at dispatch time based on agent availability and concurrent-dispatch cap per `feedback_dispatch-discipline.md`):

**Format Option A — `/rclab-team` 4-agent panel (PRIMARY)**: multi-agent coordinated team. Selected when the 4 research questions are interdependent and agents need to message each other by name during the workshop (which they do — RQ #1 NC fiber discretization feeds RQ #2 vacuum-two-point function specification; RQ #3 matching prescription feeds RQ #7 P2→P3/P3→P4 hand-off layers). Round structure:

- **Round 1 — Per-agent owner-perspective opening statements**. Each agent writes their owned RQ's first-principles framing. ~30 min each in parallel.
- **Round 2 — Cross-cite cross-examination**. Agents read each other's R1; cross-cite agents (per §W13-1.6 table below) push back where their cross-cite intersection surfaces tension. ~45 min each in parallel.
- **Round 3 — Convergence + spec-text drafting**. Each owner drafts their RQ's spec-freeze paragraph; cross-cite agents review and convergence-mark. ~60 min each in parallel + ~30 min synthesis.
- **R3 closure / Wrap-Up**: gen-physicist orchestrator synthesizes into the architecture-spec-frozen output document.

**Format Option B — `/rclab-workshop` 2-pair sequential (FALLBACK)**: 2 strongest pairings run sequentially. Pair 1 = `connes-ncg-theorist + spectral-geometer` (closes RQ #1 NC fiber discretization + RQ #2 cold-start vacuum); Pair 2 = `transit-dynamics-theorist + volovik-superfluid-universe-theorist` (closes RQ #3 matching prescription + RQ #7 P2→P3/P3→P4 hand-off fidelity). Then gen-physicist synthesizes. Selected when the concurrent-dispatch cap is binding or when agent-availability staggers favor sequential dispatch.

**Decision rule for format**: prefer Option A if the 8-concurrent cap (`feedback_dispatch-discipline.md`) can accommodate 4 simultaneous agents alongside other S87 wave dispatches; otherwise fall back to Option B. If both fail at dispatch time (e.g., 3 of 4 agents available), reduce to Option B sequential pair-dispatch and complete in 2 rounds.

### §W13-1.5 Per-agent research-question ownership

Per `session-86-path-b-carry-forward.md` lines 67-73 (verbatim):

| Agent | Owns research question | Cross-cite |
|:------|:----------------------|:-----------|
| `connes-ncg-theorist` | RQ #1 (NC fiber discretization) | RQ #2 (NCG vacuum specification) |
| `spectral-geometer` | RQ #1 (heat-kernel side of mode truncation) | RQ #4 mid-implementation (deferred — appears as cross-cite anchor in this workshop's spec-freeze) |
| `transit-dynamics-theorist` | RQ #3 (matching prescription) | RQ #7 (P2→P3 / P3→P4 hand-offs) |
| `volovik-superfluid-universe-theorist` | RQ #2 (cold-start vacuum from analog tradition) | RQ #3, RQ #7 |

RQ #1 has TWO owners (connes-ncg-theorist for the algebraic / spectral-triple side; spectral-geometer for the heat-kernel / asymptotic-truncation side). The two owners must produce a JOINT spec paragraph at R3 closure for RQ #1 (the algebraic spec and the heat-kernel spec must agree on the chosen mode-truncation scheme; disagreement = INFO outcome on RQ #1, not PASS).

### §W13-1.6 Pre-registered PASS / INFO / FAIL criterion

The workshop's verdict is a function of how many of the 4 research questions resolve to **architecture-spec-actionable answers**. An "architecture-spec-actionable answer" means: the RQ's owner(s) produce a spec paragraph at R3 closure that (i) specifies a unique implementable choice (not a menu of alternatives), (ii) cites a substrate-first canonical source per `.claude/rules/substrate-first-canonical-sourcing.md` for any numerical pin used, and (iii) survives cross-cite review without unresolved blocking-level objections.

```yaml
PASS:
  description: All 4 RQs (#1, #2, #3, #7) resolve to architecture-spec-actionable answers.
  predicate: count(RQ_i resolves to spec-actionable) == 4 for i in {1, 2, 3, 7}
  artifact: sessions/framework/path-b-architecture-spec-frozen.md exists with 4 R3-closure
            spec paragraphs, all marked CONVERGENCE; substrate-framing block present;
            cross-cite review marks SHA-pinned for each RQ.

INFO:
  description: 1, 2, or 3 RQs resolve to spec-actionable answers; the remaining 1-3 are
               flagged as INFO-deferred with explicit narrowed-question routing for a
               next-session workshop or a separate research dispatch.
  predicate: 1 <= count(RQ_i resolves to spec-actionable) <= 3
  artifact: sessions/framework/path-b-architecture-spec-frozen.md exists, partial;
            INFO-deferred RQs each carry a 4-field carry-forward spec
            (what / inputs / gate / effort) + recommending agent.

FAIL:
  description: Blocking-level theory questions surface that require a separate research
               session before any architecture freeze is possible.
  predicate: count(RQ_i resolves to spec-actionable) == 0
            OR any RQ surfaces a blocking-level theory contradiction
               (e.g., spectral-triple axioms inconsistent with the proposed
                mode-truncation scheme; cold-start vacuum two-point function
                contradicts NCG axiom 5; matching prescription violates
                acoustic-white-hole monotonicity per S85 W6 closure)
  consequence: PB-2 implementation is paused (per §W13-2.6 conditional-block predicate)
               until the blocking question is closed in a separate session.
```

### §W13-1.7 Output artifact

`sessions/framework/path-b-architecture-spec-frozen.md` — registry-grade frozen architecture-spec document.

Required content per `session-86-path-b-carry-forward.md` lines 89-100 ("What success looks like"):

- **§A. Mode-truncation choice**: explicit `L_max` choice (e.g., `L_max=10`) with energy-cap or multipole-cap selection rule; substrate-derived error bound at the chosen `L_max`.
- **§B. Cold-start vacuum two-point function**: specific lifted Bunch-Davies-analog two-point function form on noncommutative SU(3); substrate-first canonical sourcing pointer.
- **§C. Matching prescription canonical**: `s85_w6_acoustic_white_hole_formal.py`'s Painlevé-Gullstrand-style match pinned as canonical; Israel + Andreev variants flagged for downstream sensitivity analysis.
- **§D. P2→P3 / P3→P4 hand-off translation layers**: explicit translation-layer specification (mode-amplitude basis ↔ field-configuration basis transforms with explicit map; dimensions checked; substrate-first canonical sourcing for any numerical pin).
- **§E. Cross-cite review marks**: for each spec paragraph, the cross-cite agent's review mark (CONVERGENCE / INFO / DISAGREE) and an SHA-pin over the spec text the review mark applies to.
- **§F. Substrate-framing block**: explicit substrate-IS-not-IN paragraph per `.claude/rules/phononic-framing.md` and (where the architecture spec touches a Pillar-bridge) per `.claude/rules/cross-pillar-bridge-anatomy.md`.
- **§G. Carry-forward block**: any INFO-deferred RQ gets a 4-field spec routed to S88+.

### §W13-1.8 Verdict-line emission (workshop-format closure)

The PB-1 workshop is a METHODOLOGY-adjacent gate; the verdict line follows the workshop-closure convention of `.claude/rules/wave-classification.md` §"Dual-SHA closure for METHODOLOGY-class":

- `content_sha256` over the rule-file diff (here: SHA over `path-b-architecture-spec-frozen.md` final text)
- `audit_sha256` over the input-pin map of source documents (the 7 file-level inputs in §W13-1.3, each pinned by its plan-freeze SHA, plus the workshop-format-choice tag). Per-agent ownership at the project level lives in §W13-1.5 (RQ ownership table) — agent memories are read implicitly at dispatch time but are NOT Input-SHA-pinned (per `.claude/rules/agent-standards.md` §AMRI: pinning agent memory triggers Input-pin test).

Canonical line format per `.claude/rules/gate-verdicts.md`:

```
S87-PATH-B-STEP-0-WORKSHOP: PASS|INFO|FAIL -- value=<RQ_resolved_count>/4 \
  scheme=workshop-architecture-spec-freeze \
  convention=<rclab-team-4-agent OR rclab-workshop-2-pair-sequential> \
  L_max=N/A \
  audit_sha256=<64-char> content_sha256=<64-char> schema_version=R3
```

Companion comment row:

```
# audit_sha256 companion row: S87-PATH-B-STEP-0-WORKSHOP \
# audit=<short16> content=<short16> \
# format=<rclab-team-4-agent OR rclab-workshop-2-pair-sequential> \
# RQ_resolved={#1: PASS|INFO|FAIL, #2: ..., #3: ..., #7: ...} \
# output=sessions/framework/path-b-architecture-spec-frozen.md \
# closure_workshop=sessions/framework/registry/path-b-d2-workshop.md
```

### §W13-1.9 Substitution chain (PASS direction)

Per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute" — the PASS-direction claim "all 4 RQs resolve ⇒ architecture spec freezes" requires the substitution chain:

```
Step 1: Define RQ_resolves(i) := (owner_spec_paragraph(i) is spec-actionable)
                                 AND (cross_cite_review(i) ∈ {CONVERGENCE})
                                 AND (substrate_first_sourcing(i) is satisfied)
Step 2: Define spec_freeze := (∀ i ∈ {1, 2, 3, 7}: RQ_resolves(i))
Step 3: Substitute the 4-RQ enumeration into spec_freeze:
        spec_freeze ⇔ RQ_resolves(1) ∧ RQ_resolves(2) ∧ RQ_resolves(3) ∧ RQ_resolves(7)
Step 4: PASS predicate = spec_freeze (by §W13-1.6 definition)
Step 5: Direction: count(RQ_resolves) == 4 ⇒ spec_freeze ⇒ PASS.
        Strict logical conjunction; any single FAIL on RQ_resolves(i)
        forces count < 4 ⇒ INFO or FAIL by the count-band rule.
Conclusion: PASS iff all 4 RQs converge; INFO iff 1-3; FAIL iff 0 or blocking.
```

### §W13-1.10 PRDR Machinery Pin (this gate)

```yaml
machinery_pin_map:
  workshop_format_choice: rclab-team-4-agent  # PRIMARY; FALLBACK rclab-workshop-2-pair
  agent_panel: [connes-ncg-theorist, spectral-geometer, transit-dynamics-theorist, volovik-superfluid-universe-theorist]
  rq_set: [1, 2, 3, 7]  # close-now items per session-86-path-b-carry-forward.md lines 48-65
  rq_count_total: 4
  rq_count_pass_threshold: 4  # PASS iff all 4 resolve
  rq_count_info_band: [1, 3]  # INFO iff 1-3 resolve
  rq_count_fail_threshold: 0  # FAIL iff 0 resolve OR blocking-level surfaces
  output_artifact_path: sessions/framework/path-b-architecture-spec-frozen.md
  output_artifact_required_sections: [A_mode_truncation, B_cold_start_vacuum, C_matching_prescription, D_handoff_layers, E_cross_cite_review_marks, F_substrate_framing, G_carry_forward]
  cross_cite_review_required: true
  substrate_first_sourcing_required: true  # per .claude/rules/substrate-first-canonical-sourcing.md
  substrate_framing_block_required: true  # per .claude/rules/phononic-framing.md
  round_count: 3  # R1 opening / R2 cross-examination / R3 convergence + spec-drafting
  synthesis_owner: gen-physicist
  schema_version: R3
  verdict_source: computations/s87_gate_verdicts.txt
  blocked_by_predicate: none  # PB-1 is the upstream of PB-2; PB-1 has no upstream Path-B prereq
```

### §W13-1.11 Sequencing implication

PB-1's verdict gates PB-2's dispatch (see §W13-2.6 conditional-block predicate). If PB-1 returns FAIL or INFO with any of {RQ #1, RQ #3} unresolved (these are the two RQs whose decisions PB-2's implementation directly consumes — RQ #1 sets the mode-truncation scheme; RQ #3 sets the matching prescription), PB-2 is paused and routed to S88+ as a re-pre-registration carry-forward.

---

## §W13-2. S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION (PB-2)

### §W13-2.1 Gate metadata (Field 1: Gate ID + Field 2: Trigger + Field 3: Classification)

```yaml
gate_id: S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
class: COMPUTE
classification: GEOMETRIC (toy NCG validation)
trigger: [VERIFY] [SUBSTRATE-FIRST]
wave: W13
slot: §W13-2
sequencing: PB-1 PRECEDES PB-2 (conditional-block predicate; see §W13-2.6)
recommending_agent: spectral-geometer (mathematics owner) + gen-physicist (compute integration)
effort_estimate: ~2 weeks
source: sessions/archive/session-86/session-86-path-b-carry-forward.md path-b file lines 103-225
script: computations/s87_w13_nc_two_torus_validation.py
```

### §W13-2.2 What (Field 4: Hypothesis)

Implement the gradient flow `dD/dτ = -Ric(D)/G_BKM` on the Connes-Landi noncommutative two-torus with the Floricel-Ghorbanpour-Khalkhali (FGK 1612.06688) closed-form Ricci density (available in closed form for the conformal-perturbation case). Validate against the analytic flat-metric fixed point: a small ε-perturbation off the flat metric is initialized at τ=0; the gradient flow integrates forward to τ_max=100; the terminal-state conformal factor `h_terminal` is compared to the analytic flat-metric `h_flat`.

**Hypothesis**: The simulator's terminal state under gradient flow recovers the analytic flat-metric fixed point with `‖h_terminal − h_flat‖_{L²} < 10⁻⁴`. PASS at this tolerance certifies the GPU eigenvalue + spectral-mode + gradient-flow infrastructure as ready for any future Path B simulator work (including the substrate's own SU(3) fiber simulator).

**Substrate framing**: PB-2 is GEOMETRIC, not SUBSTRATE — the NC two-torus is a laboratory test surface, not a model of the substrate fiber. The substrate IS the spectral triple `(A_K, H_K, D_K)` on Jensen-deformed SU(3); the NC two-torus is chosen because FGK 1612.06688 supplies a closed-form Ricci density and the analytic flat-metric fixed point provides a ground-truth target. Direction of explanation: NC-two-torus toy validation → infrastructure correctness → substrate simulator can be built on this infrastructure → substrate-side gradient-flow simulator becomes feasible. The substrate is logically prior; the NC two-torus is an instrument for validating the simulator infrastructure that will be applied to the substrate.

### §W13-2.3 Threshold (Field 5: PASS / FAIL / INFO bands)

Verbatim from `session-86-path-b-carry-forward.md` lines 154-184 with §W13-2 renumbering:

```yaml
PASS:
  predicate: |h_terminal - h_flat|_L² < 1e-4
  evaluated_at: τ_max = 100
  tolerance_rule: RATIO (dimensionless conformal factor)
  scheme: FGK_Ricci  # FGK 1612.06688 closed-form Ricci density
  convention: Connes-Landi-2-torus  # modular spectral triple structure
  L_max: N/A  # no L_max in 2-torus; replaced by N_eval mode count
  N_eval: 64

FAIL:
  predicate: |h_terminal - h_flat|_L² > 1e-2  OR  divergence observed
  evaluated_at: τ_max = 100  OR  earlier if divergence
  divergence_definition: |h(τ) - h_flat|_L² grows monotonically without bound
                         for τ ∈ [τ_div_onset, τ_max]
                         where τ_div_onset is the latest τ at which
                         d/dτ(|h - h_flat|_L²) crosses 0 going from negative to positive

INFO:
  predicate: 1e-4 ≤ |h_terminal - h_flat|_L² ≤ 1e-2
  evaluated_at: τ_max = 100
  interpretation: convergence observed but precision insufficient
  diagnostic: likely numerical-precision issue, informative for L_max scaling
              or for scheme refinement (FGK closed-form vs. heat-kernel
              expansion truncation)
```

### §W13-2.4 PRDR Machinery Pin (Field 6: Machinery enumeration; verbatim from path-b file lines 154-184)

```yaml
machinery_pin_map:
  N_eval: 64                 # NC 2-torus mode count; small toy
  L_max: N/A                 # no L_max in 2-torus; replaced by N_eval
  scan_range: [0, 100]       # τ ∈ [0, 100]
  step_size: 0.01            # dt = 0.01
  step_count: 10000          # τ_max / dt = 100 / 0.01
  tolerance_monitor_interval: 10  # |h - h_flat|_L² monitored every 10 steps
  scheme: FGK_Ricci          # FGK 1612.06688 Eq. main theorem closed-form
  convention: Connes-Landi-2-torus  # modular spectral triple structure
  random_seed: 42            # for ε·δh perturbation
  perturbation_amplitude: ε  # to be pinned by spectral-geometer at execution; recommended ε ≤ 1e-2 small enough for linear regime, large enough above PASS threshold 1e-4
  GPU_path: torch.linalg.eigh
  GPU_device: cuda:0  # AMD RX 9070 XT (ROCm 7.2 / torch 2.9.1+rocm)
  GPU_fallback: CPU OK; matrix size N_eval=64 is small enough for either
  Python_path: phonon-exflation-sim/.venv312/Scripts/python.exe
  CPU_thread_cap: OMP_NUM_THREADS=8  # set BEFORE numpy import per .claude/rules/computation-environment.md
  G_BKM: Bures-Kantorovich-Marchenko metric on positive Dirac operators
         (per DKvS 1903.09624 §2 definition)
  Ric: FGK 1612.06688 Ricci density operator on conformal perturbation of flat
  flat_metric_reference: D_flat = standard flat Connes-Landi spectral triple
                                  with modulus τ_modulus = i (square torus)
  conformal_perturbation_form: h(x) = exp(2 σ(x))
                                where σ ∈ smooth functions on NC 2-torus
                                expanded in N_eval = 64 fundamental modes
  schema_version: R3
  verdict_source: computations/s87_gate_verdicts.txt
```

### §W13-2.5 Inputs + Input SHA pins (Field 7: Inputs)

Verbatim from `session-86-path-b-carry-forward.md` lines 154-184:

```yaml
input_sha_pins:
  - source: FGK 1612.06688
    type: paper-citation-pin
    on_disk_sha: N/A (external arXiv reference; no local file SHA needed)
    citation: "Floricel, Ghorbanpour, Khalkhali — Ricci density formulae for
               NC 2-torus; closed-form for conformal-perturbation case"
    role: scheme provider (FGK_Ricci)
  - source: DKvS 1903.09624
    type: paper-citation-pin
    on_disk_sha: N/A (external arXiv reference)
    citation: "Dong, Khalkhali, vanSuijlekom — BKM metric on positive
               Dirac operators"
    role: G_BKM definition
  - source: computations/canonical_constants.py
    type: framework-shared-constant import
    on_disk_sha: <pinned at plan-freeze>
    role: any framework-shared constants the script imports (currently none required for the NC 2-torus toy; the validation does not consume substrate-specific constants)
  - source: phonon-exflation-sim/.venv312/Scripts/python.exe
    type: python-runtime-environment
    on_disk_sha: N/A (env reference)
    role: GPU + numerical-library runtime
  - source: torch >= 2.9.1+rocm
    type: library-pin
    role: torch.linalg.eigh on AMD RX 9070 XT
  - source: numpy + scipy (latest in .venv312)
    type: library-pin
    role: L² norm + ODE step
```

### §W13-2.6 Sequencing constraint — conditional-block predicate (Field 8)

Per `session-86-path-b-carry-forward.md` lines 238-242:

```yaml
conditional_block_predicate:
  upstream_gate: S87-PATH-B-STEP-0-WORKSHOP (PB-1)
  block_condition: |
    PB-2 dispatch is BLOCKED if PB-1 verdict is:
      (a) FAIL on any of the 4 RQs, OR
      (b) INFO with RQ #1 (NC fiber discretization) unresolved, OR
      (c) INFO with RQ #3 (matching prescription) unresolved.

    PB-2 may dispatch if PB-1 verdict is:
      (i) PASS (all 4 RQs resolve), OR
      (ii) INFO where the unresolved RQs are limited to {RQ #2, RQ #7}
           (cold-start vacuum and P2→P3/P3→P4 hand-off do not block the
            NC-two-torus validation, which uses neither — the validation is
            purely a gradient-flow + Ricci-density correctness check).
  rationale: PB-1's frozen architecture document specifies the modulus and
             metric choices that PB-2 implements. RQ #1 (mode-truncation
             scheme) and RQ #3 (matching prescription) directly inform
             PB-2's machinery pin. If either is unresolved, PB-2's machinery
             pin is structurally underspecified, which is a PRU Class-8.0/8.1
             cardinality failure per .claude/rules/epistemic-discipline.md.
  blocked_outcome: emit mechanical-closure verdict per
                   .claude/rules/mechanical-closure-discipline.md with
                   value='PRE-REG-INC_blocked_by_S87-PATH-B-STEP-0-WORKSHOP_<status>'
                   where <status> is the actual PB-1 verdict.
```

### §W13-2.7 Expected output 4-tuple (Field 9: Output schema)

```yaml
expected_output_4_tuple:
  value: |h_terminal - h_flat|_L²  # scalar float; the L² norm of the residual conformal factor
  scheme: FGK_Ricci
  convention: Connes-Landi-2-torus
  L_max: N_eval = 64  # printed as L_max=64 in canonical line
```

### §W13-2.8 Output artifacts (Field 10: Artifacts; per path-b file lines 187-198)

```yaml
artifacts:
  script:
    path: computations/s87_w13_nc_two_torus_validation.py
    must_exist: true
    template: .claude/templates/script-template.py
    required_imports: |
      from canonical_constants import *  # required per .claude/rules/math-scripts.md S34+
      import torch
      import numpy as np
      from pathlib import Path
  data:
    path: computations/s87_w13_nc_two_torus_validation.npz
    must_exist: true
    required_arrays:
      - h_trajectory  # shape (n_recorded_steps, N_eval); h(τ) at every tolerance_monitor_interval=10 steps
      - Ric_trajectory  # shape (n_recorded_steps, N_eval); Ric(D_τ) trace
      - G_BKM_trajectory  # shape (n_recorded_steps, N_eval); G_BKM(D_τ) trace
      - fixed_point_error_trace  # shape (n_recorded_steps,); |h(τ) - h_flat|_L²(τ)
      - tau_grid  # shape (n_recorded_steps,); τ values
      - terminal_value  # scalar; |h_terminal - h_flat|_L²
      - perturbation_amplitude  # scalar; ε actually used at runtime
  plot:
    path: computations/s87_w13_nc_two_torus_validation.png
    must_exist: true
    required_panels:
      - convergence_curve  # |h(τ) - h_flat|_L² vs τ on log-y; PASS/INFO/FAIL bands shaded
      - terminal_residual_distribution  # histogram of (h_terminal - h_flat) per mode
  verdict_line:
    path: computations/s87_gate_verdicts.txt
    must_exist: true (appended)
    schema: dual-SHA per .claude/rules/gate-verdicts.md
  working_paper_section:
    path: sessions/archive/session-87/session-87-w13-workingpaper.md (fanout mode)
          OR sessions/archive/session-87/session-87-w13-workingpaper-consolidate.md (consolidate mode)
    section: §W13-2
    must_exist: true
    minimum_lines: 15  # per .claude/rules/agent-standards.md §"Completion Verification"
    required_subsections:
      - verdict-line-at-top
      - numerical-results
      - cross-checks (analytic flat-metric reproduction at τ=0; Ric(D_flat) = 0 sanity check)
      - substitution-chain-for-direction-claim (if any sign/direction claim)
      - assessment (PASS/INFO/FAIL interpretation; what infrastructure is certified)
      - artifact-pointers
      - substrate-framing-block (NC 2-torus is laboratory toy, not substrate fiber)
```

### §W13-2.9 Pre-registered substitution chain (Field 11: PASS-direction logic)

Per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute":

```
Claim: "PASS at |h_terminal - h_flat|_L² < 1e-4 certifies the GPU eigenvalue
        + spectral-mode + gradient-flow infrastructure as ready for substrate
        simulator work."

Step 1: Definitions
  D(τ)        := Dirac operator on Connes-Landi NC 2-torus at flow time τ
  h(τ, x)     := exp(2 σ(τ, x)); conformal factor expanded in N_eval=64 modes
  Ric(D)      := FGK 1612.06688 closed-form Ricci density operator
  G_BKM(D)    := DKvS 1903.09624 Bures-Kantorovich-Marchenko metric
  h_flat      := analytic flat-metric conformal factor (constant; identity in
                 the Connes-Landi spectral triple's natural normalization)
  ε·δh        := initial perturbation; ε small (e.g. 1e-2), δh random with seed=42

Step 2: Gradient flow
  dD(τ)/dτ = -Ric(D(τ)) / G_BKM(D(τ))
  initial: D(0) = D_flat + ε·δD where δD encodes the conformal perturbation δh
  flow integrated by explicit Euler with dt=0.01 over τ ∈ [0, 100]

Step 3: Fixed-point identity (analytic, FGK 1612.06688 main theorem)
  Ric(D_flat) = 0  ⇒  dD/dτ |_{D=D_flat} = 0
  ⇒ D_flat is a fixed point of the gradient flow
  ⇒ if the flow is contractive in a neighborhood of D_flat, the perturbed
    initial condition converges back to D_flat.

Step 4: Substitute the flow into the L² norm of the residual
  |h(τ) - h_flat|_L²
    = (linearization in ε)
    = ε · |δh|_L² · exp(-λ_min(Hessian of S_BKM at D_flat) · τ)  + O(ε²)
  where λ_min is the smallest eigenvalue of the Hessian of the BKM action
  at the flat-metric fixed point (positive iff the fixed point is stable).

Step 5: Read off the direction
  λ_min > 0  ⇒  |h(τ) - h_flat|_L² → 0 as τ → ∞
  At τ_max = 100 with reasonable λ_min ~ O(1), the residual at PASS threshold
  ε · |δh|_L² · exp(-100·λ_min) ~ ε · exp(-100) <<< 1e-4 for ε ~ 1e-2.

Conclusion: PASS at |h_terminal - h_flat|_L² < 1e-4 is consistent with
            the analytic stable-fixed-point picture; deviation
            (FAIL or INFO band) reveals an infrastructure-correctness
            issue (numerical-precision floor; explicit-Euler step-size
            instability; FGK Ricci-density discretization error;
            G_BKM evaluation incorrectness; or wrong ε·δh setup).
```

### §W13-2.10 Specialist execution agents (Field 12: Owner)

```yaml
execution_agents:
  primary_owner: spectral-geometer
    responsibilities:
      - FGK 1612.06688 Ricci density implementation (closed-form; conformal-perturbation case)
      - DKvS 1903.09624 BKM metric implementation
      - Connes-Landi NC 2-torus spectral triple structure
      - flat-metric fixed-point analytic identity (Ric(D_flat) = 0 sanity check)
      - L² norm + tolerance bookkeeping
      - mathematical correctness of the ODE integrator step
  compute_integration_owner: gen-physicist
    responsibilities:
      - canonical_constants import (per S34+ rule)
      - script-template.py scaffolding
      - dual-SHA verdict-line emission via append_verdict() helper
      - working-paper section §W13-2 write-up (≥15 substantive lines per agent-standards completion-verification)
      - PRDR machinery enumeration verification (every pin in §W13-2.4 either consumed or declared as diagnostic)
      - GPU vs CPU path decision at runtime (N_eval=64 is small enough for CPU; GPU path validated as exercise)
      - SHA-uniqueness check post-emission per .claude/rules/agent-standards.md
  cross_cite_reviewer: connes-ncg-theorist (for spectral-triple correctness)
                       + volovik-superfluid-universe-theorist (for analog tradition cross-check on the flat-metric fixed point as the "vacuum" of the NC 2-torus simulator)
```

### §W13-2.11 Verdict line schema (Field 13: Verdict format)

Canonical line per `.claude/rules/gate-verdicts.md`:

```
S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION: PASS|INFO|FAIL -- value=<float> \
  scheme=FGK_Ricci convention=Connes-Landi-2-torus L_max=64 \
  audit_sha256=<64-char> content_sha256=<64-char> schema_version=R3
```

Companion comment row:

```
# audit_sha256 companion row: S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION \
# audit=<short16> content=<short16> \
# tau_max=100 dt=0.01 N_eval=64 random_seed=42 ε=<runtime> \
# Ric_scheme=FGK_1612.06688 G_BKM=DKvS_1903.09624 \
# GPU=AMD_RX_9070_XT_ROCm7.2_torch2.9.1 \
# upstream=S87-PATH-B-STEP-0-WORKSHOP=<PB-1 verdict at dispatch>
```

The dual SHAs are computed at runtime by the `append_verdict()` helper of `script-template.py` over the ordered input-pin map; SHAs are NEVER hardcoded, NEVER copy-pasted, NEVER truncated below 64 hex chars in the canonical line.

---

## Wave 13 → Session-Close Decision Point

| PB-1 verdict | PB-2 verdict | Wave 13 closure | Routing |
|:-------------|:-------------|:----------------|:--------|
| PASS | PASS | CLOSED-PASS | Path-B simulator architecture frozen + infrastructure validated; S88+ proceeds to RQ-1+RQ-3 implementation. |
| PASS | INFO | CLOSED-WITH-INFO | Architecture frozen; infrastructure observed convergence but precision insufficient; carry-forward to S88 with refined `ε`, `dt`, or scheme. |
| PASS | FAIL | CLOSED-WITH-FAIL | Architecture frozen but infrastructure has correctness issue; mandatory remediation (numerical precision floor / step-size instability / FGK discretization / G_BKM evaluation) before any S88+ implementation; route as S88 W0 leading carry-forward. |
| INFO (RQ #2 / #7 only unresolved) | PASS | CLOSED-WITH-INFO | Architecture partially frozen (the parts PB-2 consumes are frozen); infrastructure validated; carry-forward INFO-deferred RQs to S88. |
| INFO (RQ #2 / #7 only unresolved) | INFO | CLOSED-WITH-INFO | Both partial; carry-forward both items. |
| INFO (RQ #2 / #7 only unresolved) | FAIL | CLOSED-WITH-FAIL | Architecture partially frozen; infrastructure correctness issue; route both items as S88 W0 leading carry-forwards. |
| INFO (RQ #1 OR #3 unresolved) | BLOCKED (mechanical closure PRE-REG-INC) | CLOSED-WITH-INFO | PB-1 RQ #1 or RQ #3 must be re-closed in a separate research session before PB-2 can dispatch; PB-2 verdict line emitted as PRE-REG-INC per `.claude/rules/mechanical-closure-discipline.md`. |
| FAIL | BLOCKED (mechanical closure PRE-REG-INC) | CLOSED-WITH-FAIL | Blocking-level theory question surfaced; route to S88 W0 as a separate research workshop; PB-2 verdict emitted as PRE-REG-INC. |

**Wave-13 PASS criterion**: at least PB-1 = PASS AND PB-2 ∈ {PASS, INFO} (the wave closes its primary mission of architecture-freeze + infrastructure-validation; numerical-precision INFO on PB-2 is acceptable because the PASS-direction infrastructure is exercised and produces a tractable residual, even if outside the 1e-4 band).

**Wave-13 INFO criterion**: PB-1 INFO with RQ #1 / RQ #3 closed (so PB-2 can dispatch) AND PB-2 ∈ {PASS, INFO}; OR PB-1 = PASS AND PB-2 = FAIL (architecture frozen but infrastructure broken — actionable for S88 W0).

**Wave-13 FAIL criterion**: PB-1 = FAIL OR (PB-1 INFO with RQ #1 OR RQ #3 unresolved AND PB-2 BLOCKED). Routes to S88 W0 with explicit research-question carry-forward + workshop re-dispatch.

---

## Wave 13 Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR machinery-enumeration pin (Class-8.0/8.1 cardinality test). Every gate-relevant free parameter is enumerated below; parameters tagged `[PIN]` are pre-registered with a value at plan-freeze; parameters tagged `[DIAG]` are runtime diagnostic and do not affect verdict; parameters tagged `[INHERITED]` come from upstream PB-1 closure (and are PB-1 outputs, not PB-2 plan-freeze pins).

### PB-1 (workshop) machinery enumeration

| Parameter | Tag | Value at plan-freeze | Source |
|:----------|:----|:--------------------|:-------|
| `workshop_format_choice` | [PIN] | `rclab-team-4-agent` (PRIMARY) / `rclab-workshop-2-pair-sequential` (FALLBACK) | path-b lines 41-46 |
| `agent_panel` | [PIN] | `[connes-ncg-theorist, spectral-geometer, transit-dynamics-theorist, volovik-superfluid-universe-theorist]` | path-b lines 67-73 |
| `rq_set` | [PIN] | `[1, 2, 3, 7]` (close-now items) | path-b lines 48-65 |
| `rq_count_pass_threshold` | [PIN] | `4` (PASS iff all 4 resolve) | path-b lines 32-39 |
| `rq_count_info_band` | [PIN] | `[1, 3]` (INFO iff 1-3 resolve) | path-b lines 32-39 |
| `rq_count_fail_threshold` | [PIN] | `0` OR blocking-level surfaces | path-b lines 32-39 |
| `output_artifact_path` | [PIN] | `sessions/framework/path-b-architecture-spec-frozen.md` | path-b lines 32-39 |
| `output_artifact_required_sections` | [PIN] | `[A, B, C, D, E, F, G]` per §W13-1.7 | path-b lines 89-100 |
| `cross_cite_review_required` | [PIN] | `true` | rclab-workshop spec |
| `substrate_first_sourcing_required` | [PIN] | `true` | `.claude/rules/substrate-first-canonical-sourcing.md` |
| `substrate_framing_block_required` | [PIN] | `true` | `.claude/rules/phononic-framing.md` |
| `round_count` | [PIN] | `3` | rclab-workshop / rclab-team standard |
| `synthesis_owner` | [PIN] | `gen-physicist` | partition manifest + skill §2.7a |
| `R3_synthesis_deadline` | [DIAG] | (runtime; ~1 day after R3 closure) | path-b lines 32-39 |
| `concurrent_dispatch_cap` | [DIAG] | ≤ 8 (per `feedback_dispatch-discipline.md`) | environment-rule pin |

### PB-2 (compute) machinery enumeration

| Parameter | Tag | Value at plan-freeze | Source |
|:----------|:----|:--------------------|:-------|
| `N_eval` | [PIN] | `64` | path-b line 158 |
| `L_max` | [PIN] | `N/A` (replaced by N_eval) | path-b line 159 |
| `scan_range` | [PIN] | `τ ∈ [0, 100]` | path-b line 160 |
| `step_size_dt` | [PIN] | `0.01` | path-b line 161 |
| `step_count` | [PIN] | `10000` (= τ_max / dt) | derived |
| `tolerance_monitor_interval` | [PIN] | `10` (steps) | path-b line 162 |
| `scheme` | [PIN] | `FGK_Ricci` (FGK 1612.06688 closed-form Ricci density) | path-b line 163 |
| `convention` | [PIN] | `Connes-Landi-2-torus` (modular spectral triple structure) | path-b line 164 |
| `random_seed` | [PIN] | `42` (for ε·δh perturbation) | path-b line 165 |
| `perturbation_amplitude_ε` | [INHERITED-RUNTIME] | recommended ε ≤ 1e-2; pinned by spectral-geometer at execution time, recorded in NPZ | path-b lines 154-184 |
| `GPU_path` | [PIN] | `torch.linalg.eigh` | path-b line 166 |
| `GPU_device` | [PIN] | `cuda:0` (AMD RX 9070 XT ROCm 7.2) | `.claude/rules/computation-environment.md` |
| `GPU_fallback_CPU` | [DIAG] | OK; matrix size N_eval=64 small enough for either | env rule |
| `Python_path` | [PIN] | `phonon-exflation-sim/.venv312/Scripts/python.exe` | env rule |
| `CPU_thread_cap` | [PIN] | `OMP_NUM_THREADS=8` (set BEFORE numpy import) | env rule |
| `flat_metric_reference` | [PIN] | standard flat Connes-Landi spectral triple, modulus τ_modulus = i (square torus) | FGK convention |
| `conformal_perturbation_form` | [PIN] | `h(x) = exp(2 σ(x))` with σ in N_eval=64 fundamental modes | FGK + Connes-Landi |
| `G_BKM_definition` | [PIN] | DKvS 1903.09624 §2 BKM metric on positive Dirac operators | path-b line 156 |
| `Ric_definition` | [PIN] | FGK 1612.06688 main-theorem Ricci density operator | path-b line 156 |
| `PASS_threshold` | [PIN] | `|h_terminal - h_flat|_L² < 1e-4` at τ_max=100 | path-b line 169 |
| `FAIL_threshold` | [PIN] | `|h_terminal - h_flat|_L² > 1e-2` OR divergence | path-b line 170 |
| `INFO_band` | [PIN] | `1e-4 ≤ |h_terminal - h_flat|_L² ≤ 1e-2` | path-b line 171 |
| `tolerance_rule` | [PIN] | `RATIO` (dimensionless conformal factor) | path-b line 169 |
| `divergence_definition` | [PIN] | monotone growth without bound after τ_div_onset | §W13-2.3 |
| `upstream_block_predicate` | [PIN] | PB-2 dispatch BLOCKED if PB-1 verdict ∈ {FAIL, INFO with RQ #1 or RQ #3 unresolved} | path-b lines 238-242 |
| `verdict_source` | [PIN] | `computations/s87_gate_verdicts.txt` | env rule |
| `schema_version` | [PIN] | `R3` | env rule |
| `script_path` | [PIN] | `computations/s87_w13_nc_two_torus_validation.py` | partition manifest |
| `data_path` | [PIN] | `computations/s87_w13_nc_two_torus_validation.npz` | partition manifest |
| `plot_path` | [PIN] | `computations/s87_w13_nc_two_torus_validation.png` | partition manifest |

PRDR coverage: every gate-relevant free parameter is either [PIN]-pinned at plan-freeze or explicitly [DIAG]-tagged as runtime-diagnostic-not-verdict-affecting. The `[INHERITED-RUNTIME]` tag on `perturbation_amplitude_ε` is acceptable because (a) the gate's PASS/FAIL/INFO bands are designed to be ε-tolerant (the ε·exp(-100·λ_min) decay rate dominates ε in the τ_max=100 regime), and (b) the actual ε is recorded in the NPZ for reproducibility. No bare parameters; no hidden machinery.

---

## Wave 13 Input-SHA Ledger

| Input file | Role | Plan-freeze SHA-256 | Used by |
|:-----------|:-----|:---------------------|:--------|
| `sessions/archive/session-86/session-86-path-b-carry-forward.md` | source for verbatim 4-field specs (PB-1, PB-2) | <pinned at plan-freeze> | PB-1, PB-2 |
| `sessions/session-plan/session-87-context.md` | session-87 context manifest (verbatim §3.1, §3.2 substrates) | <pinned at plan-freeze> | PB-1, PB-2 |
| `sessions/framework/registry/path-b-d2-workshop.md` | Path-B D2 workshop closure (CLOSED-FOR-CAUSE bare-spectral-action verdict) | <pinned at plan-freeze> | PB-1 (read in full at workshop dispatch) |
| `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` | combined R&D plan with 7 research questions enumerated | <pinned at plan-freeze> | PB-1 (RQ enumeration anchor) |
| `sessions/framework/registry/path-b-rq1-inner-fluctuation-simulator.md` | RQ-1 standalone reference | <pinned at plan-freeze> | PB-1 (cross-cite reference) |
| `sessions/framework/registry/path-b-rq3-phase-transition-simulator.md` | RQ-3 standalone reference | <pinned at plan-freeze> | PB-1 (cross-cite reference) |
| `computations/s85_w6_acoustic_white_hole_formal.py` | canonical matching prescription (RQ #3) | <pinned at plan-freeze> | PB-1 RQ #3 owner (transit-dynamics-theorist) |
| `computations/s52_bogoliubov_amp.npz` | existing Bogoliubov amplitude data | <pinned at plan-freeze> | PB-1 RQ #2 owner (volovik-superfluid-universe-theorist) cross-check |
| `computations/canonical_constants.py` | framework-shared constants (S86-close state) | <pinned at plan-freeze> | PB-2 (S34+ import discipline; currently no substrate-specific constants consumed by NC 2-torus toy, but imported by template scaffolding) |
| `computations/s86_gate_verdicts.txt` | S86 verdict file (collision-check at S87 plan-freeze; no S87-prefixed entries should pre-exist) | <pinned at plan-freeze> | both gates (collision check) |
| `computations/script-template.py` | computation script scaffold; provides `append_verdict()` helper | <pinned at plan-freeze> | PB-2 |
| `.claude/templates/script-template.py` | reference template | <pinned at plan-freeze> | PB-2 |
| FGK 1612.06688 (arXiv) | Ricci density closed-form for NC 2-torus conformal-perturbation case | citation-pin only (external) | PB-2 (scheme provider) |
| DKvS 1903.09624 (arXiv) | BKM metric on positive Dirac operators | citation-pin only (external) | PB-2 (G_BKM definition) |
<!--
  AMRI fix (2026-04-28): the 5 agent-memory rows (connes-ncg / spectral-geometer /
  transit-dynamics / volovik / gen-physicist) were removed from this INPUT-PIN MAP.
  Pinning `.claude/agent-memory/*/MEMORY.md` files as Input-SHA pin sources triggers
  AMRI Test 1 (input-pin test) per `.claude/rules/agent-standards.md` §AMRI.
  Per-agent ownership for PB-1 / PB-2 dispatch is declared at the project level in
  §W13-1.5 (RQ ownership table, lines 116-122); that table already carries the
  full per-agent role assignment without inverting agent memory into a project-level
  registry. Agents read their own MEMORY.md implicitly at spawn — that is the
  correct discharge of dispatch context, NOT an Input-SHA pin.
-->

| `.claude/rules/phononic-framing.md` | framing rule | <pinned at plan-freeze> | both gates (substrate-framing block) |
| `.claude/rules/substrate-first-canonical-sourcing.md` | sourcing rule | <pinned at plan-freeze> | both gates |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | bridge anatomy rule (if architecture-spec touches a Pillar bridge) | <pinned at plan-freeze> | PB-1 §F substrate-framing block (conditional) |
| `.claude/rules/gate-verdicts.md` | verdict-line schema | <pinned at plan-freeze> | both gates |
| `.claude/rules/mechanical-closure-discipline.md` | mechanical-closure protocol | <pinned at plan-freeze> | PB-2 (conditional-block predicate emission path) |
| `.claude/rules/wave-classification.md` | METHODOLOGY-class dual-SHA closure schema | <pinned at plan-freeze> | PB-1 |
| `.claude/rules/computation-environment.md` | GPU + Python environment pins | <pinned at plan-freeze> | PB-2 |
| `.claude/rules/math-scripts.md` | computation script + canonical-constants discipline | <pinned at plan-freeze> | PB-2 |
| `.claude/rules/epistemic-discipline.md` | PRU + SOURCE-RECON + PRDR discipline | <pinned at plan-freeze> | both gates |
| `.claude/rules/agent-standards.md` | completion verification | <pinned at plan-freeze> | both gates (≥15-line working-paper section) |

Plan-freeze SHA-pinning is performed by `computations/_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w13.md` per `.claude/skills/rclab-plan/skill.md` §3e; the JSON output is written to `sessions/session-plan/session-87-plan-w13-validation.json` and `<pinned at plan-freeze>` placeholders are replaced in-place via the orchestrator's pin-resolution pass before W13 dispatch.

---

**End of session-87-plan-w13.md.**
