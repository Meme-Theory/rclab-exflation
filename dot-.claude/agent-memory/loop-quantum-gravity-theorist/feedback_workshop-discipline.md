# Feedback — Workshop Discipline (4-condition definition)

**Captured**: 2026-05-22 (S92)
**Source rule**: `.claude/rules/Investigating-Workshops.md` (read in full this turn; loaded in system prompt)
**Why this file**: when I am asked to propose workshops (e.g., as the LQG specialist on a cross-framework comparison), this is the discipline I apply. The user has documented multiple sessions where workshop seeds inflated with carry-forward listings — this is the failure mode this rule eliminates.

## A WORKSHOP IS (4 conditions, ALL required)

1. **TWO+ agents with COMPETING perspectives on a SPECIFIC TENSION**. NOT one agent narrating. NOT two agents agreeing in parallel. Two or more agents who DISAGREE about how to read a claim, verdict, or structural pattern.
2. **Genuine LEDGER-DISSONANCE**: a competing-claim adjudication. Concrete divergence on something — a number, a sign, a structural reading, a methodology choice, a convention pin.
3. **Multi-round structure**: R1 steelman / R2 respond to opponent's best case / R3 converge on verdict. Three rounds for adversarial review.
4. **Output: STRUCTURAL VERDICT**. The workshop produces a NEW pinned position (verdict, registry entry, rule diff, pre-registered gate). NOT a queued computation to run later.

## A WORKSHOP IS NOT

Things I have caught myself drafting as "workshops" that don't pass the discipline:
1. **Solo compute follow-ups** — "Compute X next session" → carry-forward computation, belongs in S{N+1} session plan via `/rclab-plan`.
2. **Verification gates** — Stage-2 cross-check has pre-specified protocol; nothing to adjudicate.
3. **Re-listings of WP-enumerated carry-forwards** — re-naming carry-forwards as "workshops" adds zero structural content.
4. **Single-agent "synthesis" of one wave's gates** — a per-wave digest, not a workshop.
5. **Single-agent "exploration" of a registry slot** — even with "2-agent workshop" framing, if there's no genuine adversarial tension, it's a solo dispatch in disguise.
6. **Methodology-rule extension proposals where both agents would agree** — workshop requires DISAGREEMENT.
7. **Registry-state classification / hygiene-promotion / framework-housekeeping** — bookkeeping, not adversarial substrate-physics. Routes to housekeeping ledger.
8. **Parallel-compute-wave dressed as N-agent panel** — N independent gates + 1 AND closeout is NOT a workshop.
9. **Pre-compute shell waves** — wave with all gates `NOT STARTED` is escalation, not a CF.

## What I look for to identify a real workshop

- FAILs that admit MULTIPLE structural readings (agent A reads as evidence of X; agent B reads as evidence of Y).
- INFOs at borderline (marginal evidence; domain agents will disagree about marginal-detection vs noise).
- CROSS-WAVE tensions (one wave's PASS conflicts with another wave's INFO/FAIL).
- Methodology-vs-substrate-physics blurs (rule-extension proposals with contested rationales).
- Convention questions where TWO PERSPECTIVES GENUINELY DIVERGE.
- EXISTING claims that need ADVERSARIAL TESTING (not "compute next" but "audit what we claimed").

## "No workshops" is a valid output

If a session has clean PASSes, unambiguous verdicts, no cross-wave conflicts, settled methodology → ZERO workshops. Emit `## No workshops` with one paragraph explaining why. This is HONEST. Padding is forbidden.

## Honest count discipline

A typical session produces 0-4 genuine workshops. Even a 17-wave content-heavy session may produce only 2-5. Investigators reporting 5-10 "workshops" per wave are almost certainly carrying-forward bloviation.

For my S92 cross-framework comparison, I produced 5 workshops (each cross-framework adjudication is genuine because the LQG side and the framework side genuinely disagree about structural identifications). I dropped 3 candidates explicitly because they failed the 4-condition test. See `project_cross-framework-comparison-s92.md`.

## 3-question decision procedure (apply BEFORE adding to workshop schedule)

The first YES wins:

- **Q1 — Is the tension a math/physics adjudication?** Two+ competing readings of substrate-physics observable, structural identity, or convention, with first-principles arguments on both sides → YES = workshop.
- **Q2 — Is the candidate registry-state classification / hygiene / framework-housekeeping?** Status-tag edit / mechanical promotion / rule-file diff / audit-script extension → YES = NOT workshop; routes to housekeeping ledger.
- **Q3 — Is the candidate a parallel-compute-wave (N conditions × N axes with AND closeout)?** N independent gates with structurally orthogonal axes → YES = compute carry-forward, not workshop.

## Output format I MUST use

Per `.claude/rules/Investigating-Workshops.md` §"Forward-looking enforcement":
- Heading is `## Workshops` (NOT `## Candidates`).
- Solo computes go into a SEPARATELY-tagged section `## Carry-forwards (route to /rclab-plan, NOT this schedule)`.
- This enforces the categorical distinction at the file structure.

## Cross-link to /rclab-plan

Workshop OUTCOMES (verdicts produced by /rclab-review against the schedule) and carry-forward COMPUTATIONS (queued computation gates from wave-syntheses) are SEPARATE input streams to S{N+1}'s plan. The plan author distinguishes these. My workshop seeds file must not conflate them.
