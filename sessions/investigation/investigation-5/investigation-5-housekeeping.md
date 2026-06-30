# Investigation 5 — Housekeeping Ledger

**Investigation**: 5 | **Closed**: 2026-06-15 | **Waves**: 3 (12 gates: 10 compute + 1 workshop + 1 review) | **Driver**: `/rclab-coordinate` (full-investigation dispatch, two compute batches → workshop)

Consolidates non-workshop / session-promotion items across all three waves. **Investigation-track boundary** (`gate-verdicts.md §"Investigation-Track Canonical Path"`): an investigation CANNOT mutate session-track curated registers (Atlas, `permanent-results-registry.md`, EVOI, `canonical_constants.py`, `falsifier-master-inventory.md`, the capstone). §B items route to `/rclab-investigate --investigation 5` close. Math carry-forwards (canonical carrier `/rclab-investigate` lifts) live in each wave's WP `## Carry-Forward Computations` — pointed to in §C.

## §A — In-session resolutions (orchestrator-effected, complete)

- [x] Wave-syntheses written into all three WPs (W1/W2/W3) with math-vs-structural "What Changed" split + carry-forwards + constraint-map + files.
- [x] INV5-W2-3 rate-limit recovery: the first W2-3 agent died on a transient server rate-limit ("not your usage limit") at 22 subagent tokens with no artifacts; re-dispatched fresh; the retry landed FAIL with full artifacts (audit d51071e0). Verified on disk.
- [x] No orphaned temp files: the W1-4 agent's `_w1_4_*.log` scratch logs were cleaned by that agent; final glob of `computations/investigation-5/` shows only the 10 gates' .py/.npz/.png + the verdict ledger (no `_wp_writer`/log/temp residue).

## §B — Session-promotion candidates (→ /rclab-investigate close; session-track, NOT investigation-effectable)

| # | Item | Source | Target register | Notes |
|:--|:-----|:-------|:----------------|:------|
| B1 | **HY1** — single canonical A_s OOM (+0.86, A_s=1.54e-8) + k̂=53.3 M_KK + k̂/k_pivot=3.72 (deg(T_{BZ→pivot}) mapping, G-3) | W2-1 INFO | `canonical_constants.py` (3 named quantities) + `falsifier-master-inventory.md` | **mack-cosmic-bridge SOLE WRITER** for the falsifier row; CF-INV5-W2-A is the recompute |
| B2 | **atlas-04 S3 re-scope** — "SA-is-the-effective-action ASSUMED" → "scoped to Layer A (spectral/geometry); categorically-distinct on Layer B (order-parameter/CC) per INV5-W3-2" | W3-2 SCOPED verdict | atlas-04 + capstone §-prose | capstone-hygiene Q3/Q4; designated-writer prose patch (`feedback_framework-hygiene.md`); the S72 two-layer split upgraded "assumed" → "structurally forced (Wall #6 + Kosmann)" |
| B3 | W1-5 functional-CC-channel LIVE + a₀/a₂ permanently SCHEME-DEPENDENT (sign-flip −0.499 vs +2.320); W1-2 geometric-CC channels all closed (a₄-Weyl OOM 115.76) | W1-5 PASS, W1-2 FAIL | §VII / CC-register | the CC lives in Layer B (μ-selected, outside {Tr f}) per the W3-2 verdict |
| B4 | W1-3 lepton-spacing signature: substrate-forward Connes ladder ratio 12.56 (Casimir-graded, ≠ PDG 1.889); the "1.889 EXACT" exposed as a Route-B inverse-Yukawa tautology | W1-3 INFO | `mack` falsifier surface + §VII.BL annotation | B-4 constrained; ε_LX Casimir-graded not mass-graded |
| B5 | ε_LX is EXTERNAL — both intra-substrate routes closed (B-1 modular twist SCALAR; B-4 Connes-distance Casimir-graded) | W1-4 FAIL, W1-3 INFO | §VII.BL annotation | strengthens the generation-blindness theorem |
| B6 | 170× DM-mass shortfall HARDENED-OPEN — B-3 (pseudogap two-scale) + B-4-disorder (Goldstone) both closed; abundance match + below-edge protection intact | W2-2 FAIL, W2-4 FAIL | EVOI/standing-gap register | two complementary corridors closed (too phase-rigid vs too weakly disordered) |
| B7 | m_H +5.36% residual PHYSICAL-but-UNDERIVED — truncation (W3-1) + self-energy (W2-3) both falsified; quartic (W1-1) gives-not-derives | W3-1/W2-3/W3-3 | standing-gap / capstone | CF-INV5-W3-B is the derivation attempt (3 routes) |
| B8 | W1-1 convention provenance — anchored to S70-resolved ratio_gilkey=0.4140 (NOT cache-moment 0.4866) | W1-1 PASS | provenance hygiene | atlas-row vs cache-moment layer orthogonality |

## §C — Math carry-forwards (canonical carrier = per-wave WP `## Carry-Forward Computations`; `/rclab-investigate` lifts)

- **W1** (`investigation-5-w1-workingpaper.md`): CF-INV5-W1-A — absolute CC magnitude + continuum-DOS under the entropy functional (W1-5 established the RATIO; the absolute value vs ρ_Λ is the next step).
- **W2** (`investigation-5-w2-workingpaper.md`): CF-INV5-W2-A — HY1 A_s single-number session-promotion (mack sole-writer for the falsifier row).
- **W3** (`investigation-5-w3-workingpaper.md` + `workshops/two-effective-actions.md`): CF-INV5-W3-A — **INV5-CC-MU-DEPENDENCE-DISCRIMINATOR** (the workshop's decisive forward gate: ∂(vacuum)/∂μ + ∂(condensation)/∂V; zero ⇒ Reading-1/Layer-A, non-zero ⇒ Reading-2/Layer-B); CF-INV5-W3-B — derive the underived +5.36% m_H residual (3 routes from the W3-3 review).

## §D — Process observations (no action; recorded for next-investigation plan hygiene)

- **Transient rate-limit death**: INV5-W2-3's first agent died on a server-side rate-limit (not usage-limit) early; recovered by fresh re-dispatch (the agent context was gone, so SendMessage-continuation did not apply). One worker spiked while the other six batch-1 agents ran normally — momentary, not systemic.
- **Concurrent-write race**: batch 1 put 3 agents on the W1 WP and 3 on the W2 WP simultaneously; mitigated by the mandated atomic single-section Python substitution (all sibling sections verified byte-intact; one agent reported a single mtime-guard trip + re-apply). For future investigation plans, consider per-gate WP files OR keep the atomic-substitution mandate (`feedback_session-process.md`: ≤2 agents per shared file).
- **Per-gate gate-id-form variance**: W1 gates' `verdict_line.must_contain` anchors on the FULL long gate-id (`^INV5-W1-1-PS-…:`) while W3-1 anchors on the SHORT form (`^INV5-W3-1:`). Agents matched their own section's must_contain; orchestrator instructed "emit the exact gate-id your must_contain anchors on." For future plans, align gate_id with the must_contain anchor consistently.
- **Plan-text drift (W3-1)**: the plan's pinned `canonical_constants.py` SHA (e6829db0…) was stale post-plan-freeze (runtime 8505153a…); the agent consumed the live file and MCP-verified the 3 constants it used (`substrate-first-canonical-sourcing.md §ii.B`).
- **W1-4 v1-trap self-correction**: a first implementation read the contaminated twisted-commutator (spurious 0.33/INFO); corrected in-session to the modular twist's OWN action σ^ω(a)−a, with a test-power control (89/90 NON-scalar on a resolving generator) + Sage verification + both-readings printed. No debt.
- **SOURCE-RECON (W2-4)**: J_u1 pinned canonical 0.038 (seed's 0.034 stale; D_max=0.048 → NO-ACTION band).
- **W1-3 plan substitution-chain tautology**: the plan cited (d_e−d_μ)/(d_μ−d_τ)=1.889 "EXACT", but that is a Route-B inverse-Yukawa circularity (feeds the masses in; ℓ cancels). The agent exposed it and printed both routes so it can't regenerate. Plan-hygiene note for future Connes-distance gates.
