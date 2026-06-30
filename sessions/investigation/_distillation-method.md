# Investigation Distillation — Method & Campaign Substrate

**This session's deliverable.** The most thorough method for distilling the 13 already-executed
`investigation-[n]` efforts into our structured session format: deeply review each investigation's
**results**, score every finding by a four-verb framework-impact rubric (challenged / bolstered /
clarified / muddled), and build one **workshop-focused session** that fully explores them. This
document is BOTH the method and the shared substrate every Stage-1 reviewer binds to.

**Status:** Stage 0 complete (this doc + the corpus map). Stage 1 dispatched 2026-06-20.

---

## 0. Design principle — the funnel in reverse

The investigations were produced by a funnel: `inv-1` 31-agent survey → ~10 cross-agent
convergences (CV-1…CV-10) → fanned out into `inv-2…13`, each one *executing the attack* on one
convergence cluster. The thorough distillation runs that funnel **in reverse** — read the ~135 gate
results back against the convergences they were spawned to test, score each finding by the four
verbs — then **forward** across the one boundary that matters: the track-local boundary
(`gate-verdicts.md`), where investigation material becomes permanent only by promotion into a
`/rclab-plan` **session-mode** plan. The four verbs are the analytical spine; the workshop-focused
session is the terminal artifact.

---

## 1. Session ↔ investigation file taxonomy (the conflation guard)

Investigation folders co-locate planning WITH results (sessions keep plans in `session-plan/`).
Reviewers read RESULT files for findings; PLAN/SEED files are **pre-registration context only** — a
pre-registered hypothesis is a PROMISE, not a RESULT.

| Role | Session track | Investigation track (co-located) |
|:--|:--|:--|
| **Pre-reg (NOT findings)** | `session-plan/session-N-plan*.md` | `inv-n-plan-index.md`, `inv-n-plan-w*.md`, `inv-n-seed.md`, `inv-n-partition.md`, `*-validation.json` |
| **Working papers (RESULTS)** | `session-N-w*-workingpaper.md` | `inv-n-w*-workingpaper.md` |
| **Results index (RESULTS map)** | `session-N-results-index.md` | `inv-n-results-index.md` |
| **Synthesis (RESULTS)** | `session-N-*-synthesis.md` | `inv-n-*-synthesis.md` (topic syntheses) |
| **Housekeeping** | `session-N-housekeeping.md` | `inv-n-housekeeping.md` |
| **Workshop docs (RESULTS)** | `session-N/workshops/*.md` | `inv-n/workshops/*.md` |
| **Verdict ledger (RESULTS)** | `computations/session-N/sN_gate_verdicts.txt` | `computations/investigation-n/invn_gate_verdicts.txt` |

A finding comes from a working-paper / synthesis / workshop doc / verdict ledger (what was
COMPUTED), read against its plan block's pre-registered threshold (what was PROMISED). A planned
gate or workshop with NO result artifact on disk is a gate-finalization gap (→ housekeeping), not an
inferred result.

---

## 2. The four-verb rubric (tag every finding exactly one)

| Verb | Meaning | Framework basis |
|:--|:--|:--|
| **BOLSTERED** | claim gained independent support: a pre-registered PASS, a blind cross-axis confirmation, or an open gap that acquired a NAMED mechanism + forward gate | a PASS at 0 free params IS evidence (`epistemic-discipline.md`, `feedback_reporting-framing.md`) |
| **CHALLENGED** | a FAIL/INFO that CONSTRAINS the claim, a confirmed wall, or a new contradiction | negative results are boundaries that shrink solution space — often strengthening the survivor |
| **CLARIFIED** | precision/scope up, truth value UNCHANGED: number pinned, scope narrowed, label disambiguated, convention fixed | register tag stays; uncertainty band tightens |
| **MUDDLED** | uncertainty INCREASED or incoherence exposed: a "wall" disagreeing with itself, a register tag outrunning derivation, two supported readings that can't both hold and weren't resolved | genuine ledger-dissonance — `Investigating-Workshops.md` Q1 |

Each tag records: the claim (cite registry slot / canonical constant / atlas row / falsifier row),
before-state (current register status), after-state (result), magnitude (σ / OOM / structural).

---

## 3. Verb → destination routing

- **MUDDLED / genuine contradiction → WORKSHOP** (Q1 ledger-dissonance) — the session spine.
- **CHALLENGED-with-constructive-next-step / BOLSTERED-with-forward-gate → SESSION COMPUTE CARRY-FORWARD** (4-field: what / inputs / gate / effort; EVOI-ordered).
- **CLARIFIED → HOUSEKEEPING** (designated-writer patch; includes the stranded hygiene each investigation routed out but couldn't apply).
- **CHALLENGED-corridor-closed → CLOSED** (constraint-map update; recorded, not carried).

---

## 4. Digest schema — Stage-1 output (`investigation-{n}/_synthesis.md`)

```
# investigation-{n} — Distillation Digest
**Reviewer:** <agent-type> (neutral; not an inv-{n} author).  **Date:** 2026-06-20.
**Topic:** <one line>   **inv-1 convergences/bridges executed:** <CV-x, B-y>
**Gate tally:** <P/F/I over N gates + k workshop/review/solo deliverables; flag missing artifacts>

## 1. Per-gate ledger      | Gate | Verdict | Substrate reading | Claim touched (cite) | Verb | Magnitude |
## 2. Convergence read-back  (per attacked CV: dissolved / confirmed / relocated / still-incoherent)
## 3. Four-verb classification   ### BOLSTERED / ### CHALLENGED / ### CLARIFIED / ### MUDDLED
## 4. Routing   ### →WORKSHOP(Q1) / ### →COMPUTE-CF(4-field) / ### →HOUSEKEEPING / ### →CLOSED
## 5. Cross-investigation hooks   (which other inv touch the same claim — for Stage-2 rollup)
## 6. Stranded hygiene (rescue list)   (HY items targeting session-track registers, never applied)
```

---

## 5. The stages

- **Stage 0** (orchestrator-direct; DONE) — this doc: file taxonomy, rubric, routing, schema, corpus map, reviewer assignments.
- **Stage 1** (fan-out; 1 reviewer/investigation; ≤8 concurrent, 2 batches) — each reviewer reads its investigation's RESULT files in full and writes `investigation-{n}/_synthesis.md` to the §4 schema. Mirrors `/rclab-investigate --investigation n` (fills the 12 missing `_synthesis.md`), augmented with the four-verb digest.
- **Stage 2** (cross-investigation rollup) — ~6–10 convergence-synthesizers consume the digests, emit a net four-verb verdict per CV; one master `_cross-investigation-synthesis.md` ("where the framework stands after 13 investigations").
- **Stage 3** (triage) — `Investigating-Workshops.md` 3-question discriminator over rolled-up findings → 4 buckets (workshops / compute-CFs EVOI-ordered / housekeeping incl. stranded hygiene / closed).
- **Stage 4** (build) — `/rclab-plan` session-mode seeded by Stage-3: Wave 0 housekeeping, workshop waves (Q1 adjudications), compute waves (promoted bridges). The permanence terminus.

---

## 6. Reviewer assignments (neutral charge; per-investigation authorship-excluded)

| inv | Reviewer (not an author) | Seed authors (excluded) | Verdict tally | inv-1 convergence(s) executed |
|:--|:--|:--|:--|:--|
| 2 | van-den-dungen-bridge-theorist | baptista | 0P/3F/0I | CV-8 Yukawa/moduli (B-3 modular flavor); off-U(2); N3 χ-rescue Kasparov |
| 3 | kitaev-quantum-chaos-theorist | berry, spectral-geometer, paasch | 3P/3F/8I | CV-2 M_KK (B-2); CV-6 d_s-flow; spectral statistics; mass-quant |
| 4 | einstein-theorist | hawking, schwarzschild-penrose | 6P/2F/1I | CV-3 a(t)/clock (B-4); CV-9 compact-object; CV-1 greybody; CV-5 Page (B-5) |
| 5 | lizzi-spectral-functional-theorist | connes, landau, spectral-geometer | 2P/5F/3I | CV-1 A_s impulse-quench; CV-4 CC a₄ (B-13); m_H residual; two-effective-actions |
| 6 | kaku-speculative-theorist | dirac, kaluza-klein, feynman | 2P/6F/6I | CV-2 M_KK bracket (B-2); quantum-loop gravity; η_B (B-6); CV-1 Parker-Bogoliubov |
| 7 | mack-cosmic-bridge | cosmic-web, little-red-dots, loop-quantum-gravity | 2P/6F/5I | CV-3 a(t) (B-4); CV-9 compact-object (B-8); CV-5 GGE-LSS (B-10) |
| 8 | volovik-superfluid-universe-theorist | mack, phonon-first, einstein | 5P/5F/4I | CV-2/CV-3 scale-a(t) knot; CV-4 CC/dark sector (B-7,B-12); Bell/Born; PBH (B-9) |
| 9 | hawking-theorist | kaku, string-theory, loop-quantum-gravity, kitaev | 0P/6F/1I | cross-framework QG; CV-5 Page/sum-over-geometries (B-11); CV-8 modular flavor; swampland |
| 10 | transit-dynamics-theorist | tesla, quantum-acoustics, kitaev | 5P/3F/4I | CV-5 TRANSIT-PS GGE acoustic P(k) (B-1); CV-1 A_s normalization; integrability |
| 11 | landau-condensed-matter-theorist | nazarewicz, neutrino, paasch, quantum-foam, volovik | 4P/2F/11I | CV-2 M_KK BCS dimensional-transmutation (B-2); fermion/vacuum; CV-4 dark (B-7); compact-object interior |
| 12 | connes-ncg-theorist | lizzi, van-den-dungen, transit-dynamics | 8P/4F/5I | CV-1 A_s wall (6-route hub); "is Tr f(D²) right functional/signature" (CV-4 SA≠free energy); FI/RD ledger |
| 13 | phonon-first-cosmologist | gen-physicist, sagan | 1P/2F/2I | cross-domain+empirical audit; CV-9 compact-object a₄/color-SC; CV-5 collider bispectrum; S8 |

inv-1 is already CLOSED (`investigation-1/_synthesis.md` is the convergence spine; not re-reviewed).

---

## 7. Corpus map (per-investigation RESULT vs PLAN/SEED files)

Verdict ledgers: `computations/investigation-{n}/inv{n}_gate_verdicts.txt`.

- **inv-2** RESULT: `inv-2-w1-workingpaper.md`, `inv-2-housekeeping.md`, `workshops/n3-chi-rescue-kasparov-faithfulness.md`. PLAN/SEED: `inv-2-plan-index.md`, `inv-2-plan-w1.md`, `inv-2-seed.md`, `inv-2-partition.md`. (no results-index)
- **inv-3** RESULT: `inv-3-w{1,2,3,4}-workingpaper.md`, `inv-3-results-index.md`, `inv-3-housekeeping.md`, `workshops/m-kk-derivability.md`. PLAN/SEED: `inv-3-plan-index.md`, `inv-3-plan-w{1..4}.md`, `inv-3-seed.md`, `inv-3-partition.md`.
- **inv-4** RESULT: `inv-4-w{1,2,3}-workingpaper.md`, `inv-4-results-index.md`, `inv-4-housekeeping.md`, `workshops/level-3-magnitude-divergence.md`. PLAN/SEED: `inv-4-plan-index.md`, `inv-4-plan-w{1..3}.md`, `inv-4-seed.md`, `inv-4-partition.md`.
- **inv-5** RESULT: `inv-5-w{1,2,3}-workingpaper.md`, `inv-5-results-index.md`, `inv-5-housekeeping.md`, `inv-5-higgs-residual-synthesis.md`, `workshops/two-effective-actions.md`. PLAN/SEED: `inv-5-plan-index.md`, `inv-5-plan-w{1..3}.md`, `inv-5-seed.md`, `inv-5-partition.md`.
- **inv-6** RESULT: `inv-6-w{1,2,3,4}-workingpaper.md`, `inv-6-results-index.md`, `inv-6-housekeeping.md`, `workshops/m-kk-determination-route-reconciliation.md`. PLAN/SEED: `inv-6-plan-index.md`, `inv-6-plan-w{1..4}.md`, `inv-6-seed.md`, `inv-6-partition.md`.
- **inv-7** RESULT: `inv-7-w{1,2,3,4}-workingpaper.md`, `inv-7-results-index.md`, `inv-7-housekeeping.md`, `workshops/effective-friedmann-functional-form.md`, `workshops/n-pbh-physical-vs-tautology.md`. PLAN/SEED: `inv-7-plan-index.md`, `inv-7-plan-w{1..4}.md`, `inv-7-seed.md`, `inv-7-partition.md`.
- **inv-8** RESULT: `inv-8-w{1,2,3,4}-workingpaper.md`, `inv-8-results-index.md`, `inv-8-housekeeping.md`, `workshops/inv8-w4-1-bell-vs-hidden-variable.md`, `workshops/inv8-w4-2-cosmic-birefringence.md`. PLAN/SEED: `inv-8-plan-index.md`, `inv-8-plan-w{1..4}.md`, `inv-8-seed.md`, `inv-8-partition.md`.
- **inv-9** RESULT: `inv-9-w{1,2,3}-workingpaper.md`, `inv-9-results-index.md`, `inv-9-housekeeping.md`, `inv-9-swampland-refresh-synthesis.md`, `workshops/inv9-w3-1-sum-over-geometries.md`, `workshops/inv9-w3-2-qg-character-lens.md`. PLAN/SEED: `inv-9-plan-index.md`, `inv-9-plan-w{1..3}.md`, `inv-9-seed.md`, `inv-9-partition.md`.
- **inv-10** RESULT: `inv-10-w{1,2,3,4}-workingpaper.md`, `inv-10-results-index.md`. (workshops/ EMPTY — 2 planned workshops: verify + flag as gate-finalization gap if absent.) PLAN/SEED: `inv-10-plan-index.md`, `inv-10-plan-w{1..4}.md`, `inv-10-seed.md`, `inv-10-partition.md`.
- **inv-11** RESULT: `inv-11-w{1,2,3,4,5}-workingpaper.md`, `inv-11-results-index.md`, `workshops/inv11-w5-1-mkk-gap-vs-integer-scheme.md`. PLAN/SEED: `inv-11-plan-index.md`, `inv-11-plan-w{1..5}.md`, `inv-11-seed.md`, `inv-11-partition.md`.
- **inv-12** RESULT: `inv-12-w{1,2,3,4}-workingpaper.md`, `inv-12-results-index.md`, `inv-12-housekeeping.md`, `inv-12-as-synthesis.md`, `workshops/as-wall-reading.md`, `workshops/sa-failure-diagnosis.md`. PLAN/SEED: `inv-12-plan-index.md`, `inv-12-plan-w{1..4}.md`, `inv-12-seed.md`, `inv-12-partition.md`.
- **inv-13** RESULT: `inv-13-w{1,2}-workingpaper.md`, `inv-13-results-index.md`, `inv-13-housekeeping.md`, `inv-13-bayesian-reanchor-synthesis.md`. (0 workshops by design.) PLAN/SEED: `inv-13-plan-index.md`, `inv-13-plan-w{1,2}.md`, `inv-13-seed.md`, `inv-13-partition.md`.
