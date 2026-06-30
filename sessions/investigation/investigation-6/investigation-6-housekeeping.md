# Investigation 6 Housekeeping Ledger

**Date**: 2026-06-15
**Investigation**: 6 (track-local; `computations/investigation-6/inv6_gate_verdicts.txt`)
**Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"`
**Track-local modulation**: an investigation CANNOT mutate session-track curated registers (`permanent-results-registry.md`, `.claude/rules/`, Atlas, `falsifier-master-inventory.md`, EVOI table) per `gate-verdicts.md §"Investigation-Track Canonical Path"`. Session-track non-math items therefore route to §B carry-forwards / `/rclab-investigate --investigation 6` close, not §A in-session edits.

## Q2 marker (citation)
A candidate is Q2 iff its resolution is a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation producing a new structural claim. See `Investigating-Workshops.md §"Q2"`.

## Final verdict ledger (14 gates: 13 compute + 1 workshop)
| Verdict | Gates |
|:--|:--|
| PASS (2) | W2-1 (Γ[τ] M_KK loop-self-consistent), W2-4 (emergent Lorentz) |
| FAIL (6) | W1-3 (KK-tower couplings), W2-2 (A_s), W2-3 (graviton-loop EFT), W3-1 (η_B rescattering), W3-3 (η_B Schwinger), W3-4 (antimatter domain) |
| INFO (5) | W1-1 (bracket), W1-2 (Casimir null), W1-4 (Z₂ wall), W3-2 (CP-source rank-1), W2-5 (d_s→8) |
| LANDED (1) | W4-1 (M_KK ONE-ROUTE-DOMINATES workshop) |

---

## §A. In-session resolutions (already effected; ledger only)

| # | Source | Item | Resolution (file) |
|:--|:-------|:-----|:------------------|
| A1 | W1 (all) | Wave-1 synthesis + math/non-math split | `investigation-6-w1-workingpaper.md §"Wave 1 Synthesis"` |
| A2 | W2 (all) | Wave-2 synthesis + math/non-math split | `investigation-6-w2-workingpaper.md §"Wave 2 Synthesis"` |
| A3 | W3 (all) | Wave-3 synthesis + math/non-math split | `investigation-6-w3-workingpaper.md §"Wave 3 Synthesis"` |
| A4 | W4 | Wave-4 synthesis + §W4-1 workshop-closure tracking (orchestrator-direct presentation patch: Status→COMPLETED, artifact-existence checklist confirmed, MCP audit + Results filled — pointer to the verified deliverable, no new physics) | `investigation-6-w4-workingpaper.md §W4-1 + §"Wave 4 Synthesis"` |
| A5 | session-close | Results-index updated with the 14-gate verdict tally | `investigation-6-results-index.md` |

---

## §B. Session-track promotion carry-forwards (Q2; mirrored to WP CF)

Investigation results are NOT permanent — these lift into a session-mode `/rclab-plan` for registry/Atlas/EVOI/inventory landing. Each MIRRORS a WP `## Carry-Forward Computations` entry.

### CF-INV6-W1-A — promote the gauge-vs-gravity bracket + first-compact-object record [Q2-promotion]
> Mirrored: `investigation-6-w1-workingpaper.md §"Carry-Forward Computations"`. Why not §A: permanent-registry write is session-track.
- **What**: register W1-1 (bracket REAL 6.79×, a₀-band contains the A_s gap) + W1-4 (Z₂ BCS-amplitude wall, first G-KK3/S106 occupant). **Inputs**: inv6_w1_1 (fb920648), inv6_w1_4 (de92408b); §VII.BS; atlas-04 A2/G6. **Gate**: session re-verify + registry-landing. **Effort**: ~1 compute + landings.

### CF-INV6-W2-B — promote Γ[τ] into inv-5 W3-2 + atlas-08 EFT self-classification [Q2-promotion]
> Mirrored: `investigation-6-w2-workingpaper.md §"Carry-Forward Computations"` (CF-INV6-W2-A/B). Why not §A: session-track atlas/registry + cross-investigation citation.
- **What**: lift Γ[τ] (W2-1) into the inv-5 W3-2 two-effective-actions adjudication; promote W2-3+W2-5 (emergent gravity = Wilsonian EFT, no d_s reduction) into atlas-08 self-classification. **Inputs**: inv6_w2_1 (b8cc01fc), inv6_w2_3, inv6_w2_5; atlas-08. **Gate**: artifact-existence landings. **Effort**: ~1 + landings.

### CF-INV6-W3-B — promote η_B convergence + CP-source rank-1 + HY1/HY2/HY3 [Q2-promotion+hygiene]
> Mirrored: `investigation-6-w3-workingpaper.md §"Carry-Forward Computations"` (CF-INV6-W3-B). Why not §A: EVOI down-tag + falsifier-row mints are session-track (mack sole-writer for inventory).
- **What**: EVOI Rank-8 baryogenesis CLOSED→CONDITIONAL down-tag (HY1); η_B + δ_CP^PMNS falsifier-row mints (HY2/HY3); the W3-1/W3-3 convergent closure + W3-2 rank-1 φ_88 CP-source. **Inputs**: inv6_w3_1 (d08cffd9), inv6_w3_2 (ca1fd44a), inv6_w3_3 (97960ac4); EVOI table; atlas-04; falsifier-master-inventory. **Gate**: session re-verify + EVOI/registry/inventory landings. **Effort**: ~1 + landings.

### CF-INV6-W4-B — promote the M_KK ONE-ROUTE-DOMINATES verdict + inv-3 W4 cross-cite [Q2-promotion]
> Mirrored: `investigation-6-w4-workingpaper.md §"Carry-Forward Computations"` (CF-INV6-W4-B). Why not §A: registry-landing (joint-theorem pathway if cross-axis) is session-track; depends on the gauge-a₄ gate (CF-INV6-W4-A, a new-compute item in the WP CF).
- **What**: lift the workshop's ONE-ROUTE-DOMINATES (gravity-a₂) candidate; cross-cite inv-3 W4. **Inputs**: the workshop STAGE-0 deliverable; §VII.BS (S102/S103); the CF-INV6-W4-A gate verdict. **Gate**: registry-landing after the gauge-a₄ gate. **Effort**: ~1 landing.

### Remaining seed hygiene (HY4/HY5/HY6) — session-track, route to investigation-close
HY4 (corpus paper-32 a_g prose correction), HY5 (capstone §0/§2.4 gauge-from-NCG-algebra reconciliation), HY6 (alpha_GUT canonical-constants registration) per `investigation-6-seed.md §"Non-gate items"`. All session-track; route to `/rclab-investigate --investigation 6` close.

---

## §C. Parallel-compute-wave carry-forwards (Q3)
(none — no Q3 wave-together structures this investigation.)

## §D. Methodology-rule extensions (Q2)
(none — investigation-6 produced no `.claude/rules/` diffs. The §VII.BS clause-(b) caveat retirement is a session-track registry fact already landed at S102/S103 — cited, not a rule extension.)

## §E. Pre-compute shell waves
(none — all four waves executed; all 13 compute gates emitted verdict lines, the W4 workshop LANDED.)

---

## §F. Structural counts
| Category | Count |
|:---------|------:|
| §A In-session resolutions | 5 |
| §B Session-track promotion CFs (mirrored to WP) | 4 + HY4/5/6 |
| §C Q3 parallel-wave CFs | 0 |
| §D Methodology rule extensions | 0 |
| §E Pre-compute shell waves | 0 |

**Out-of-scope for this Q2 ledger** (genuine new-compute, in WP CF blocks for `/rclab-plan`, NOT housekeeping): **CF-INV6-W4-A** (the decisive `INV{n+1}-MKK-GAUGE-LOOP-SELFCONSISTENCY` gauge-a₄ gate — the leading next-session compute), **CF-INV6-W3-A** (σ_supp normalization recompute — the η_B deficit locus), **CF-INV6-W2-A** (4-route A_s triangulation).

---

## Capstone-hygiene 5-question gate (`capstone-hygiene-gate.md`)
INV6 touches capstone-governing claims; track-local boundary → every YES routes to §B / investigation-close, NOT an in-session capstone edit.
- **Q1 (a(t)/Friedmann gap)**: YES (W2-1 induced G_N(τ)/Λ(τ); W4 M_KK clock) → CF-INV6-W4-B / W2 promotion.
- **Q2 (§7 falsifier row)**: YES (W2-2 A_s 4th route; W3 η_B falsifier mints HY2/HY3) → CF-INV6-W3-B (mack sole-writer).
- **Q3 (PROVEN/CONDITIONAL/BROKEN/INFO status)**: YES (emergent gravity EFT not finite-QG; η_B corridors closed; M_KK ONE-ROUTE) → CF-INV6-W2-B / W3-B / W4-B.
- **Q4 (PROSE claim vs ledger)**: YES (capstone m_H-collapse note; §0/§2.4 gauge-from-algebra, HY5) → CF-INV6-W1-A / HY5.
- **Q5 (citation add/invalidate)**: YES (W1-3 fiber≠SM-matter sharpening; §VII.BS clause-(b) caveat retired by S102/S103) → CF-INV6-W3-B / session-track (already at S102/S103).
All five route to carry-forward/session-promotion (correct for an investigation).

---

## Process observations (this dispatch — infra-grind narrative; forward-looking lessons)

1. **Usage-quota wall (resets 10:30am EDT)** killed the opening Batch-1 (W1-1 completed; 6 others quota-died). Recovered after the user confirmed reset; all re-ran. Lesson: a "session limit · resets <time>" completion banner is a HARD quota stop, distinct from the transient infra throttle ("not your usage limit") — do not re-dispatch into it; wait for reset.
2. **Transient infra throttle re-confirmed at 8-wide.** Filling concurrency to 8 (3 resume + 5 batch-2) tripped the same 529-class throttle that 6–7-wide batches survived. Lesson locked: cap re-dispatch at ≤5 during flaky windows; the deaths came from concurrency-bursts + infra flakiness, never from the paced batches.
3. **AUP false-positive** on INV6-W2-1 (3rd attempt) — a spurious content-classifier trip on benign spectral-action physics (Γ[τ]=−½ζ'_D(0,τ)); resolved on the 4th attempt with the same prompt. Lesson: AUP banners on plainly-benign physics are transient; one retry is the right response before escalating to solo-inline.
4. **W1-4 concurrent-run race (clean resolution).** `a00e3bcf`'s throttle-error *completion notification* was treated as death and `ab228d61` re-dispatched — but `a00e3bcf` was alive and ran ~79 min, producing the canonical line 108 (`de92408b`) that superseded `ab228d61`'s quick-patch line 36 (`9fa1fcf6`) via the Option-A `supersedes=` protocol. Zero verdict corruption (clean supersession chain; latest non-superseded = de92408b is canonical), wasted compute (sunk). Lesson: a "rate-limited" completion notification ≠ true agent death; verify on disk before re-dispatching a long-running agent.
5. **Stale cache-SHA plan defect.** The inv-6 plans (w1/w2/w3 §-blocks) pin the s84 L12 spectrum-cache SHA `88f1e9b1…` (from a since-superseded s96 manifest); the git-clean on-disk canonical is `9e6d9cf7…` (consumed by 20+ live scripts). Every cache-reading agent re-pinned at runtime per SOURCE-RECON Class-(c) and documented the drift in its verdict. NOT post-hoc-edited here (editing a frozen, already-executed plan is a Class-3 boundary); recorded for any future inv-6 plan re-use — the canonical cache SHA is `9e6d9cf7…`.
6. **L_max feasibility downgrades (honest, disclosed).** W2-1 (L_max 12→6, Friedrich-Bär feasibility; signed read-offs L_max-invariant) per math-scripts.md; v3 Class-1 boundary respected via verdict-line disclosure.

---

## Consumption pointers
- **`/rclab-investigate --investigation 6`**: read this file BEFORE candidates. §A/§B/§C entries are non-workshops. The ONE genuine future workshop seed (a₀-vs-a₂-style) is NOT present here; the decisive next-compute is CF-INV6-W4-A (gauge-a₄ gate). HY1–HY6 route to session-promotion. Cross-cite inv-3 W4 (M_KK derivability-in-principle).
- **`/rclab-plan` (next session)**: consume §B via the WP CF mirrors, PLUS the new-compute WP CFs (CF-INV6-W4-A gauge-a₄ gate [leading], CF-INV6-W3-A σ_supp, CF-INV6-W2-A triangulation).
- **Track-local**: NO INV6 result is permanent until migrated into a session-mode plan and re-computed under a `session-{N}` gate.

*End of Investigation 6 housekeeping ledger.*
