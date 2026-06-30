# Investigation 4 Housekeeping Ledger

**Date**: 2026-06-15
**Investigation**: 4 (track-local; `computations/investigation-4/inv4_gate_verdicts.txt`)
**Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"`
**Track-local modulation**: an investigation CANNOT mutate session-track curated registers (`sessions/permanent-results-registry.md`, `.claude/rules/`, the Atlas, `falsifier-master-inventory.md`) per `gate-verdicts.md §"Investigation-Track Canonical Path"`. Consequently, session-track non-math items that would be §A (fix-in-session) in a session become §B carry-forwards here (routed to `/rclab-investigate --investigation 4` close OR session-mode `/rclab-plan` promotion) — the boundary, not laziness, is the reason.

## Q2 marker (citation)

A candidate is Q2 iff its resolution is a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation producing a new structural claim. See `Investigating-Workshops.md §"Q2"`.

---

## §A. In-session resolutions (already effected; ledger only)

Investigation-track items effected during the INV4 wave compute (within the track-local boundary).

| # | Source wave / gate | Item | Resolution (file:lines) | Verified at (audit_sha256 short) |
|:--|:-------------------|:-----|:------------------------|:---------------------------------|
| A1 | W1 (all) | Wave-1 synthesis + math/non-math split written | `investigation-4-w1-workingpaper.md §"Wave 1 Synthesis"` | n/a (synthesis) |
| A2 | W2 (all) | Wave-2 synthesis + math/non-math split written | `investigation-4-w2-workingpaper.md §"Wave 2 Synthesis"` | n/a (synthesis) |
| A3 | W3 (all) | Wave-3 synthesis + math/non-math split written | `investigation-4-w3-workingpaper.md §"Wave 3 Synthesis"` | n/a (synthesis) |
| A4 | W1-§W1-4 | `κ_exit = 47.6146 M_KK` pre-promoted to `canonical_constants.py` SECTION C (substrate-first §(ii), S95-W4-2 prov.) — shared-infrastructure constant, NOT a curated session-track register; effected by the W1-4 agent at runtime | `computations/_shared/canonical_constants.py` SECTION C | `291bae3d` (W1-4) |
| A5 | W2-§W2-1 | Mid-run physics-bug self-correction: Jensen volume-preserving (`det g_τ=6561`) geometric-mean scalarization (τ-flat) → arithmetic block-average (recovers real a₂(τ)) BEFORE emit | `computations/investigation-4/inv4_w2_cs_zero_count.py` | `8ebbcb84` (W2-1) |
| A6 | W2-§W2-2 | Mid-run self-correction: shear double-count (−σ² AND −R_kk counts internal ±5τ̇² twice) → reading-A internal-Ricci per the chain's Def 4 BEFORE emit | `computations/investigation-4/inv4_w2_raychaudhuri_focusing.py` | `06da2662` (W2-2) |
| A7 | session-close | Results-index updated with the 9-gate verdict tally + workshop LANDED | `investigation-4-results-index.md §"Verdicts"` | n/a (index) |

---

## §B. Hygiene-promotion compute carry-forwards (4-field spec; mirrored to WP CF)

Session-track PROMOTIONS — Q2 mechanical-promotion class. An investigation produces STAGE-0 / track-local results; permanent registration is a session-track gate (migrate, do not cite). Each is MIRRORED to the originating wave's WP `## Carry-Forward Computations`.

### CF-INV4-W1-B — Session-track promotion of the a₂-conical 1/4 derivation [Q2-promotion]

> **Routing note**: Q2 mechanical-promotion per `Investigating-Workshops.md §"Q2"`. Mirrored to `investigation-4-w1-workingpaper.md §"Carry-Forward Computations"`.
> **Why not §A**: the registry-landing of the W1-2 result is a SESSION-TRACK permanent-registry write — forbidden to an investigation by the track-local boundary; requires a session-mode re-verify compute + registry sole-writer.

1. **What**: lift W1-2 (`c_conical=0.25` from the a₂ conical-deficit response) into a session-mode gate for permanent-registry promotion.
2. **Inputs**: `inv4_w1_euclidean_replica.py/.npz` (audit_sha256 `58b29602…585b2e58`); a₂^{PV}/a₄^{PV} pins.
3. **Gate**: session-mode re-run reproduces `c_conical=0.25` to ≤1e-6 under canonical pins; then registry-landing.
4. **Effort**: ~1 compute + 1 registry-landing.

### CF-INV4-W2-B — Session-track promotion: C-1 resolution + G3 sharpening + KK-bubble + HY1/HY2 [Q2-promotion+hygiene]

> **Routing note**: Q2 mechanical-promotion + capstone-hygiene per `Investigating-Workshops.md §"Q2"` + `capstone-hygiene-gate.md`. Mirrored to `investigation-4-w2-workingpaper.md §"Carry-Forward Computations"`.
> **Why not §A**: C-1 resolution, G3 censorship-sharpening, KK-bubble registration, AND the HY1 (Diagram-J redraw to single-asymmetric-open) + HY2 (capstone causal-disconnection down-tag) edits are ALL session-track curated-register / capstone writes — forbidden to an investigation; HY1/HY2 require the capstone designated-writer per `capstone-hygiene-gate.md`.
1. **What**: lift three W2 results to session-mode permanent registry: (i) C-1 RESOLVED (S95 single-asymmetric-open; S85 pair = artifact); (ii) G3 dynamical-not-sealing censorship at Σ_dump (p=−1 marginal); (iii) KK-bubble first-compact-object record (λ_GL=0.944 M_KK⁻¹). Plus the capstone HY1/HY2 patches licensed by N_zeros=1.
2. **Inputs**: `inv4_w2_cs_zero_count.npz`, `inv4_w2_christodoulou_scc.npz`, `inv4_w2_gregory_laflamme_dynamical.npz`; verdict shorts W2-1 `8ebbcb84`, W2-3 `c74a2a1a`, W2-4 `809456b4`.
3. **Gate**: session-mode re-verify each verdict reproduces under canonical pins; registry-landing + capstone designated-writer patch (HY1/HY2) per the capstone-hygiene gate.
4. **Effort**: ~1 compute + registry/capstone landings.

### CF-INV4-W3-2-STAGE1 — STAGE-1-CANDIDATE registration of the unified Level-3 criterion [Q2-promotion]

> **Routing note**: Q2 mechanical-promotion per `joint-theorem-promotion.md` 4-stage pathway. Mirrored to `investigation-4-w3-workingpaper.md §"Carry-Forward Computations"` + full STAGE-0 spec in `workshops/level-3-magnitude-divergence.md §"Carry-Forward Computations"`.
> **Why not §A**: STAGE-1 registration is a session-track registry write; Stage-2 cross-axis independent-verify (two axis-distinct reviewers, NOT sp/lizzi, no workshop context) cannot be effected by an orchestrator edit.
1. **What**: register the unified `α_growth=d−2s=n` criterion + Tier-1/Tier-2 scope as a STAGE-1-CANDIDATE §VII entry; down-tag registry line 22011's S106 "Tier-1-constructible" disposition (post-S109 falsified) via the registry sole-writer.
2. **Inputs**: the workshop STAGE-0 doc; GATE-A + GATE-B verdicts (the 2×2 empirical anchor, see §C); §VII.CB + §VII.AU entries.
3. **Gate**: artifact-existence (registry-landing class) — STAGE-1-CANDIDATE tag + 5-anatomy + 3-level + pole-scope + JOINT-flag elements present.
4. **Effort**: 1 registry-landing + 1 Stage-2 verify. Depends on §C (GATE-A + GATE-B).

### CF-INV4-W3-1-PROMOTE — Session-track promotion of the a₀-clock = Volovik-tracking relation [Q2-promotion]

> **Routing note**: Q2 mechanical-promotion. Mirrored to `investigation-4-w3-workingpaper.md §"Carry-Forward Computations"`.
> **Why not §A**: permanent-registry write (a₀-clock relation) is session-track; requires session-mode re-verify.
1. **What**: lift W3-1 (a₀ de Sitter first law reduces EXACTLY to ρ_vac ∝ Λ ∝ a₀H², c_track=3) to a session-mode gate for permanent registry; unifies G2 (a(t)) with C10 (CC tracking).
2. **Inputs**: `inv4_w3_de_sitter_clock_tracking.py/.npz` (audit_sha256 `11ad0cb8…06234a`); S97-DS-AREA-LAW-MONOTONICITY; DILUTION-CC.
3. **Gate**: session-mode re-verify reproduces c_track=3, reduction_residual≤1e-12; registry-landing. Coordinate with the clock-location workshop (WP CF-INV4-W3-1-CLOCKLOC) which scopes the clock-location claim.
4. **Effort**: 1 compute + 1 registry-landing.

---

## §C. Parallel-compute-wave carry-forwards (Q3 wave-together; mirrored to WP CF)

### CF-INV4-W3-2-2x2 — The decisive 2×2 Level-3-divergence discriminator [Q3-wave-together]

> **Routing note**: Q3 parallel-compute-wave per `Investigating-Workshops.md §"Q3"`. The two gates are MIRRORED individually to `investigation-4-w3-workingpaper.md §"Carry-Forward Computations"` (CF-INV4-W3-2-GATE-A, CF-INV4-W3-2-GATE-B) and fully specified in the workshop md.
> **Why not a workshop**: GATE-A (regulator-switch axis) and GATE-B (functional-switch axis) are STRUCTURALLY ORTHOGONAL axes of one decision table (the 2×2 of `workshops/level-3-magnitude-divergence.md §"The decisive 2×2 forward gate"`); each has its own pre-registered PASS criterion and derivation-author axis (sp / lizzi) — no cross-axis rebuttal is meaningful, so it is a parallel-compute-wave, NOT the (already-closed) adversarial workshop.

1. **What**: 2-axis discriminator of whether the §VII.CB Level-3 dimensionful wall is apex-keyed-permanent (top-left cell) or functional-dischargeable (bottom-left); both co-authors predict top-left.
2. **Inputs**: `s84_spectrum_cache_L12_tau019.npz`; PV + heat-kernel + Richardson/Abel evaluators; `a_2_FW_zeta` (cross-check only, anti-tautology guard).
3. **Gate**: two parallel sub-gates + a joint 2×2 reading:
   - `INV-FWD-HOMOGENEITY-VS-REGULATOR` — regulator axis (sp); PASS = all ≥3 regulator classes diverge same-sign (apex regulator-INVARIANT wall).
   - `INV-FWD-RESIDUE-VS-PARTIALSUM` — functional axis (lizzi); PASS(Reading a) = only `Φ_logderiv` binds (Tier-2-DIMENSIONFUL wall confirmed).
   - **Wave-closeout (the 2×2 cell)**: joint reading per the workshop's decision table determines apex-geometry-governs / functional-governs / regulator-corollary / joint-triple.
4. **Effort**: 2 compute gates (dispatched together) + 1 cell-reading closeout.

---

## §D. Methodology-rule extensions (M1-M4 + allowlist; mirrored to WP CF)

(none — INV4 produced no rule-file diffs. The W3-2 unified criterion is a candidate THEOREM routed to a §VII registry entry (CF-INV4-W3-2-STAGE1), not a `.claude/rules/` extension.)

---

## §E. Pre-compute shell waves (upstream escalation; NOT a CF)

(none — all three waves executed; all 9 compute gates emitted verdict lines and the workshop LANDED. Verified: `computations/investigation-4/inv4_gate_verdicts.txt` carries 9 canonical INV4 lines; `workshops/level-3-magnitude-divergence.md` carries the 3 closure markers.)

---

## §F. Structural counts (artifact shape; not length)

| Category | Count |
|:---------|------:|
| §A In-session resolutions | 7 |
| §B Session-track promotion CFs (mirrored to WP) | 4 |
| §C Q3 parallel-wave CFs (mirrored to WP) | 1 (2 sub-gates) |
| §D Methodology rule extensions | 0 |
| §E Pre-compute shell waves | 0 |
| **Total Q2-class items surfaced** | 12 |

Out-of-scope for this Q2 ledger (recorded for completeness; routed via WP CF / workshop schedule, NOT housekeeping): **genuine new-compute CFs** CF-INV4-W1-A (boundary-mode microstate count) + CF-INV4-W2-A (12D GL-bubble lift) — Q1-class new physics → WP CF, consumed by `/rclab-plan`; **Q1 adversarial workshop** CF-INV4-W3-1-CLOCKLOC (a₀-vs-a₂ clock-location) — future workshop, routed via WP CF + the `/rclab-investigate --investigation 4` workshop schedule.

---

## Capstone-hygiene 5-question gate (`capstone-hygiene-gate.md`)

INV4's wave-syntheses touch capstone-governing claims (the a(t)/clock channel, causal-disconnection narration, PROVEN/INFO status of C-1 / KK-bubble / Level-3 walls). Track-local boundary: an investigation CANNOT patch the capstone in-session — every YES routes to a §B carry-forward / the investigation-close session-promotion, NOT an in-session designated-writer fix.

- **Q1 — a(t)/effective-Friedmann gap.** YES (W3-1 a₀-clock + W2-2 a₂-focusing bear on the §6.3 clock). Routing → CF-INV4-W3-1-PROMOTE + CF-INV4-W3-1-CLOCKLOC (the split is unresolved; capstone §6.3 unchanged until the clock-location workshop + session promotion).
- **Q2 — §7 falsifier-anchor row.** YES (W1-4 strengthens the AMPLITUDE-NORM-66 structural-wall reading). Routing → `mack-cosmic-bridge` is the §7/inventory sole writer; session-track, folded into CF-INV4-W2-B promotion (NOT effected here).
- **Q3 — PROVEN/CONDITIONAL/BROKEN/INFO status change.** YES (C-1 RESOLVED; KK-bubble EXISTS; §VII.CB Tier-2-DIMENSIONFUL wall). Routing → CF-INV4-W2-B + CF-INV4-W3-2-STAGE1 (investigation-track; permanent status only on session promotion).
- **Q4 — PROSE claim vs ledger row.** YES (capstone causal-disconnection prose down-tag, HY2, licensed by N_zeros=1). Routing → CF-INV4-W2-B (capstone designated-writer patch at session promotion).
- **Q5 — citation add/invalidate.** YES (W1-1 replaces the FAILED S89 degenerate-CM-trace gate as the GGE-microstate route). Routing → session-track citation reconciliation, folded into CF-INV4-W1-B promotion.

All five route to carry-forward/session-promotion per the track-local boundary; none is effected in-session (correct for an investigation).

---

## Consumption pointers

- **`/rclab-investigate --investigation 4`**: read this file BEFORE producing candidates. Every §A/§B/§C entry is a non-workshop. The ONE genuine future workshop (Q1) is CF-INV4-W3-1-CLOCKLOC (a₀-vs-a₂ clock-location) — route it to the workshop schedule. HY1–HY6 session-track capstone-hygiene items: HY1/HY2 licensed (folded into CF-INV4-W2-B); HY3–HY6 remain seed-quarantined, route to session promotion.
- **`/rclab-plan` (next session/investigation)**: consume §B + §C via the WP CF blocks they mirror to, PLUS the genuine-new-compute WP CFs (CF-INV4-W1-A, CF-INV4-W2-A). §A is ledger-only.
- **Track-local boundary**: NO INV4 result is permanent until migrated into a session-mode plan and re-computed under a `session-{N}` gate.

---

*End of Investigation 4 housekeeping ledger.*
