# Session 86 — Path B Carry-Forward to Session 87

**Generated**: 2026-04-27
**Status**: structured carry-forward for S87 planning
**Source**: Path B D2 workshop closure (`sessions/framework/registry/path-b-d2-workshop.md`,
2026-04-27) and combined RQ-1+RQ-3 R&D plan (`sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md`)
**Convention**: per `.claude/rules/session-handoffs.md` §"Recommendation Carry-Forward"
— next-session plan is the canonical carry-forward mechanism; both items below get
fillable 4-field specs (what / inputs / gate / effort) per the no-tech-debt rule.

## Context for the S87 planner

The Path B D2 workshop (2026-04-27) closed D2(a) (gradient flow on bare spectral action
with Jensen `τ` as variable) for cause across three independent reviewers (NCG axioms,
heat-kernel math, Volovik analog tradition) plus contradiction with the project's S38
GGE-permanence theorem. The user's "wrong question" reframing was structurally
validated: NCG licenses dynamics of EXCITATIONS on a fixed spectral triple, not
dynamics of the substrate itself. The synthesis pivoted to a combined RQ-1 + RQ-3
full-cycle simulator architecture (4 phases, 6 gates, ~4-6 dev-week budget). The two
items below are the precursor steps to that simulator, both of which live in S87+
territory because they require either workshop dispatches or multi-day computation
infrastructure work outside the S86 wave structure.

S86 scope was set 2026-04-25 via the partition manifest and the 21-wave fanout; Path B
emerged as a research thread mid-S86 closeout review and is therefore S87 work.
Neither item interacts with S86's W0-W15 verdict pipeline.

---

## Item 1 — Path-B-Step-0 Pre-Implementation Workshop

### 4-field spec

| Field | Specification |
|:------|:--------------|
| **What** | Combined-scope pre-implementation workshop to close 4 research questions before the RQ-1+RQ-3 simulator architecture freezes. Output: an architecture spec freeze document that the implementation phase builds against without further theory decisions. |
| **Inputs** | (1) `sessions/framework/registry/path-b-d2-workshop.md` (workshop closure with all three rounds verified on disk); (2) `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` (combined R&D plan with the 7 research questions enumerated); (3) the four agents' existing memory (connes-ncg-theorist, spectral-geometer, transit-dynamics-theorist, volovik-superfluid-universe-theorist). |
| **Gate** | PASS if all 4 research questions resolve to architecture-spec-actionable answers. INFO if 1-3 resolve. FAIL if blocking-level theory questions surface that require a separate research session before any architecture freeze is possible. |
| **Effort** | ~2 days (1 day workshop dispatch + 1 day synthesis to spec freeze). |

### Workshop format

4-agent panel workshop. Use `/rclab-team` skill (multi-agent coordinated team) since
the questions are interdependent and the agents will need to message each other by
name. Alternative format: `/rclab-workshop` 2-agent iterative for the two strongest
pairings (Connes-NCG + spectral-geometer; transit-dynamics + Volovik) run sequentially,
then synthesize. Decision deferred to S87 planner.

### Research questions to close (verbatim from combined plan §"Research questions")

1. **Time-discretization on the noncommutative SU(3) fiber** — mode-truncation using
   static `D_K` eigenmodes is the natural fit, but the truncation-error vs. mode-count
   tradeoff is uncharacterized.
2. **Initial-condition class for cold start** — vacuum two-point functions on the
   noncommutative SU(3) fiber need explicit transcription.
3. **Matching prescription at the τ_fold boundary** — Israel / Andreev /
   Painlevé-Gullstrand alternatives; pre-register `s85_w6_acoustic_white_hole_formal.py`
   as canonical with alternatives as variants.
7. **Phase-coupling hand-off fidelity at P2→P3 and P3→P4** — combined-only research
   question; the joint architecture introduces translation layers absent from
   standalone RQ-1 / RQ-3 plans.

(Research questions #4, #5, #6 from the combined plan are deferred to mid-implementation
workshops because they require initial implementation experience to be answerable.)

### Agent responsibilities

| Agent | Owns research question | Cross-cite |
|:------|:----------------------|:-----------|
| `connes-ncg-theorist` | #1 (NC fiber discretization) | #2 (NCG vacuum specification) |
| `spectral-geometer` | #1 (heat-kernel side of mode truncation) | #4 mid-implementation |
| `transit-dynamics-theorist` | #3 (matching prescription) | #7 (P3 hand-offs) |
| `volovik-superfluid-universe-theorist` | #2 (cold-start vacuum from analog tradition) | #3, #7 |

Each agent contributes per-question position; synthesis (orchestrator, ~1 day) folds
the four agents' positions into a single architecture spec freeze document. Output
artifact: `sessions/framework/path-b-architecture-spec-frozen.md` (or similar).

### Dependencies / inputs (file-level)

- `sessions/framework/registry/path-b-d2-workshop.md` — workshop closure (read in full)
- `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` — combined R&D plan
- `sessions/framework/registry/path-b-rq1-inner-fluctuation-simulator.md` — RQ-1 standalone (reference)
- `sessions/framework/registry/path-b-rq3-phase-transition-simulator.md` — RQ-3 standalone (reference)
- `s85_w6_acoustic_white_hole_formal.py` — canonical matching prescription source
- `s52_bogoliubov_amp.npz` — existing Bogoliubov amplitude data
- Existing static `D_K(τ_fold)` infrastructure (computations/_shared)

### What success looks like

A frozen architecture document specifying:
- Mode-truncation choice (e.g., L_max=10 with energy-cap / multipole-cap selection)
- Cold-start vacuum two-point function form (e.g., specific lifted Bunch-Davies analog
  on noncommutative SU(3))
- Matching prescription canonical (e.g., `s85_w6_acoustic_white_hole_formal.py`'s
  Painlevé-Gullstrand-style match)
- P2→P3 and P3→P4 hand-off translation layers (e.g., mode-amplitude basis ↔
  field-configuration basis transforms with explicit map)

After the spec freeze, the simulator implementation in S87+ can proceed without
further theory decisions, only engineering choices.

---

## Item 2 — Path-B-NC-Two-Torus Pre-Pivot Validation

### 4-field spec

| Field | Specification |
|:------|:--------------|
| **What** | Implement gradient flow `dD/dτ = -Ric(D)/G_BKM` on the Connes-Landi noncommutative two-torus with Floricel-Ghorbanpour-Khalkhali Ricci density (FGK 1612.06688, closed-form for conformal-perturbation case). Validate against the analytic flat-metric fixed point. |
| **Inputs** | (1) FGK 1612.06688 (Ricci density formulae for NC 2-torus; closed-form available); (2) Existing GPU eigenvalue infrastructure (`torch.linalg.eigh` on AMD RX 9070 XT per `.claude/rules/computation-environment.md`); (3) Connes-Landi spectral triple structure (analytic; small spectrum). |
| **Gate** | `S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION`: PASS if simulator's terminal state under gradient flow recovers the analytic flat-metric fixed point with `\|h_terminal - h_flat\|_{L²} < 10⁻⁴` (where `h` is the conformal factor). FAIL if terminal state diverges or recovers a different fixed point. INFO if convergence is observed but tolerance is not met (likely numerical-precision issue, informative for L_max scaling). |
| **Effort** | ~2 weeks (per Round 2 Item 4 of `path-b-d2-workshop.md` synthesis). |

### Why this exists as pre-pivot

Round 2 (`spectral-geometer`) of the Path B workshop established that the NC two-torus
toy is the only mathematically license-able gradient-flow setup currently available
(closed-form Ricci density per FGK 1612.06688, analytic flat-metric fixed point,
small spectrum). Even though D2(a) on SU(3) Jensen is closed for cause, validating
the GPU eigenvalue inner loop + spectral-mode basis manipulation + gradient-flow
numerics in a setting with analytic ground truth is reusable infrastructure for ALL
Path B simulator work — RQ-1 inner-fluctuation evolution, RQ-3 Bogoliubov matching,
and any future combined work.

### Implementation specification

**Substrate**: Connes-Landi noncommutative two-torus (NC 2-torus) with deformation
parameter θ. Spectral triple `(A_θ, H, D_θ)` per Connes-Landi 2001. Modular spectral
triple structure per FGK 1612.06688 §2.

**State variable**: conformal factor `h(τ)` parameterizing a Weyl rescaling of the
flat NC 2-torus metric, evolving under gradient flow.

**Evolution rule**: `dD_θ/dτ = -Ric(D_θ)/G_BKM(D_θ)`, where:
- `Ric(D_θ)` is the FGK Ricci density (closed-form per FGK 1612.06688 main theorem)
- `G_BKM(D_θ)` is the Bogoliubov-Kubo-Mori metric (Dong-Khalkhali-vanSuijlekom
  1903.09624 for explicit modified-Bessel-function form on NC 2-torus)

**Inner loop**: per timestep, evaluate `Ric(D_θ)` from FGK closed-form expression
(no eigenvalue solve needed — that's the toy's advantage), evaluate `G_BKM(D_θ)`
from DKvS series, compute their ratio, advance `h(τ)` by symplectic Verlet or RK4.

**Initial conditions**: perturbed conformal factor `h(0) = h_flat + ε·δh`, with
`ε` small and `δh` a fixed perturbation. Ground truth: under gradient flow, `h(τ) →
h_flat` as `τ → ∞`.

**Validation**: terminal `h(τ_max)` measured against `h_flat`; gate threshold
`\|h_terminal - h_flat\|_{L²} < 10⁻⁴`.

### Pre-registered gate block (per `.claude/rules/gate-verdicts.md`)

```
Gate ID: S87-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION
Trigger: [VERIFY]
Classification: GEOMETRIC (toy NCG validation)
Hypothesis: Gradient flow `dD/dτ = -Ric(D)/G_BKM` on Connes-Landi NC 2-torus
            converges to the analytic flat-metric fixed point.
Threshold:
  PASS: |h_terminal - h_flat|_L² < 10⁻⁴ at τ_max = 100 (RATIO tolerance, dimensionless conformal factor)
  FAIL: |h_terminal - h_flat|_L² > 10⁻² OR divergence observed
  INFO: 10⁻⁴ ≤ |h_terminal - h_flat|_L² ≤ 10⁻² (convergence observed but precision insufficient)
Machinery pin (PRDR):
  N_eval: 64 (NC 2-torus mode count; small toy)
  L_max: N/A (no L_max in 2-torus; replaced by mode count N_eval)
  scan_range: τ ∈ [0, 100], dt = 0.01
  step_size: dt = 0.01
  tolerance: |h - h_flat|_L² monitored every 10 steps
  scheme: FGK Ricci density (closed-form per 1612.06688 Eq. main theorem)
  convention: Connes-Landi NC 2-torus, modular spectral triple structure
  random_seed: 42 (for ε·δh perturbation)
  GPU path: torch.linalg.eigh on AMD RX 9070 XT (validation case; mostly small enough for CPU)
Input SHA-256 pins:
  - FGK 1612.06688 (paper reference; no on-disk SHA needed, citation pin only)
  - DKvS 1903.09624 (paper reference; no on-disk SHA needed)
  - canonical_constants.py (for any framework-shared constants the script imports)
Expected output 4-tuple:
  (value=|h_terminal - h_flat|_L², scheme=FGK_Ricci, convention=Connes-Landi-2-torus, L_max=N_eval=64)
What PASS means: GPU eigenvalue + spectral-mode + gradient-flow infrastructure validated
                 for any future Path B simulator work.
What FAIL means: infrastructure has a numerical-correctness issue that must be fixed
                 before RQ-1+RQ-3 implementation begins.
```

### Output artifacts

- Script: `computations/s87_w?_nc_two_torus_validation.py` (slot to be allocated
  by S87 planner)
- Data: `computations/s87_w?_nc_two_torus_validation.npz` with
  `h(τ)` trajectory, `Ric(D_τ)` trajectory, `G_BKM(D_τ)` trajectory, fixed-point error
  trace
- Plot: `computations/s87_w?_nc_two_torus_validation.png` showing convergence
  to flat metric
- Verdict line: appended to `computations/s87_gate_verdicts.txt` per the canonical
  format
- Working-paper section: in whatever S87 wave is allocated; documents the validation
  result and its implications for RQ-1+RQ-3 launch readiness

### Dependencies

- FGK 1612.06688 + DKvS 1903.09624 papers (already cited in workshop; available via
  `mcp__paper-search__` if not already in `researchers/`)
- Existing GPU eigenvalue infrastructure
- Sympy / mpmath for closed-form Ricci density evaluation if torch lacks the modified
  Bessel functions DKvS uses

### Why this is OPTIONAL but recommended

The workshop synthesis explicitly tagged this item as OPTIONAL pre-pivot validation
("runs independent of pivot choice, validates the substrate-simulation tooling rather
than the substrate-simulation question"). It can be skipped if the user is confident
in the GPU eigenvalue + spectral-mode + gradient-flow infrastructure. It is recommended
because:

1. The combined RQ-1+RQ-3 simulator commits 4-6 dev-weeks. A 2-week infrastructure
   validation is 25-50% of that budget but bounds the downside if the tooling has
   silent numerical issues.
2. The NC two-torus is the ONLY currently mathematically license-able gradient-flow
   setup (per Round 2). Validating the tooling here means validating it in a regime
   where the answer is known analytically.
3. PASS on this gate produces reusable infrastructure (FGK Ricci density evaluator,
   BKM metric evaluator, gradient-flow integrator) that may have value beyond Path B
   for any future moduli-dynamics work the framework undertakes.

---

## Carry-forward instructions for S87 planner

When `/rclab-plan` is invoked for session 87, both items above should be folded into
the wave partition:

| Item | Recommended wave class | Owner |
|:-----|:-----------------------|:------|
| Item 1 (Step 0 workshop) | Could be a W0-class methodology / theory-decision wave (analogous to S86's W0a/W0b). 4-agent panel workshop. ~2 days. | gen-physicist (orchestrator) + 4 reviewers |
| Item 2 (NC two-torus validation) | Mid-session compute wave; not urgent (no downstream gates depend on it within S87 unless the user explicitly commits to the RQ-1+RQ-3 implementation in S87). ~2 weeks. | spectral-geometer or connes-ncg-theorist (mathematics owner) + gen-physicist (compute integration) |

**Sequencing constraint**: Item 1 should land before Item 2 begins implementation,
because Item 1's frozen architecture document specifies the modulus and metric
choices that Item 2 implements. If Item 1 returns a BLOCKED verdict on any of the
4 research questions, Item 2 should be paused until the underlying research
question is closed in a separate session.

**If S87 priority is elsewhere** (e.g., another framework area takes precedence and
Path B is deferred to S88+), both items remain valid carry-forward and should be
promoted directly to the S88 plan without modification. Their 4-field specs are
session-independent.

**Relationship to other Path B documents**: this carry-forward doc is the bridge
between S86 (where Path B was researched and closed) and S87 (where Path B
preparation begins, if approved). The full Path B documentation set on disk is:

- `sessions/framework/registry/path-b-d2-workshop.md` — workshop closure; canonical
- `sessions/framework/registry/path-b-rq1-inner-fluctuation-simulator.md` — RQ-1 standalone
- `sessions/framework/registry/path-b-rq3-phase-transition-simulator.md` — RQ-3 standalone
- `sessions/framework/registry/path-b-rq2-cc-dilaton-lambda-running.md` — RQ-2 standalone (smaller-scope fallback, not in current carry-forward)
- `sessions/framework/registry/path-b-rq1-rq3-combined-full-cycle-simulator.md` — combined plan (primary)
- `sessions/archive/session-86/session-86-path-b-carry-forward.md` — this doc

---

## Decision-status summary

| Decision | Status |
|:---------|:------|
| D2(a) gradient flow on bare `S_spec[τ]` | CLOSED for cause (NCG + Math + Analog + GGE-permanence) |
| Combined RQ-1+RQ-3 architecture | PROPOSED; awaiting user commit |
| RQ-2 CC dilaton Λ-running | DEFERRED as smaller-scope fallback (not in current carry-forward) |
| Step 0 workshop (Item 1 above) | SCOPED for S87 |
| NC two-torus pre-pivot validation (Item 2 above) | SCOPED for S87 (optional but recommended) |

User commit on RQ-1+RQ-3 is the gating decision for this carry-forward to become
active S87 work. If the user does NOT commit Path B in S87, both items remain valid
carry-forward to S88+ without modification.
