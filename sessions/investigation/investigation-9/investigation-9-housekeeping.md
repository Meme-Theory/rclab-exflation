# Investigation 9 — Housekeeping Ledger

**Date**: 2026-06-16 | **Closed by**: `/rclab-coordinate` (full-investigation dispatch, all 3 waves) | **Template**: `.claude/templates/session-housekeeping.md`

Canonical Q2 ledger for investigation-9. §A = completed this dispatch; §B/§C/§D = carry-forwards (mirrored to the per-wave WP `## Carry-Forward Computations` blocks, the load-bearing consumption source for `/rclab-investigate --investigation 9` → session-mode `/rclab-plan`). Track-local boundary (`gate-verdicts.md §"Investigation-Track Canonical Path"`): an investigation CANNOT mutate curated session-track registers (atlas, capstone, permanent-results-registry, canonical_constants, falsifier-inventory) — those are §D session-promotion items, NOT in-session edits.

## §A — In-session resolutions (Effected-In-Session; completed, ledger record only)

- [x] Three per-wave team-lead syntheses written (math-vs-non-math split) — `investigation-9-w1-workingpaper.md §"Wave 1 Synthesis"`, `…-w2-… §"Wave 2 Synthesis"`, `…-w3-… §"Wave 3 Synthesis"`.
- [x] W3 gate sections updated NOT STARTED → LANDED with verdict headlines — `investigation-9-w3-workingpaper.md §W3-1` + `§W3-2` (artifact-existence confirmed; workshop md pointers).
- [x] Results-index Status column de-staled (was "NOT STARTED pending /rclab-coordinate") → all-10-CLOSED + headline — `investigation-9-results-index.md`.
- [x] W3-1 + W3-2 workshop `### Effected In-Session` blocks executed by the final-turn agents (string / LQG) — both correctly recorded "no in-scope investigation-track curated-doc edits; structural outcomes → session-promotion carry-forwards" per the track-local boundary.
- [x] No session-track register edits made from this investigation (correct — track-local boundary; all such items routed to §D).

## §B — Hygiene compute carry-forwards (math; 4-field specs in WP CF blocks)

Genuine future computes surfaced this dispatch (full 4-field specs in the cited WP `## Carry-Forward Computations`):

| CF-ID | One-line | WP source | Priority |
|:--|:--|:--|:--|
| CF-INV9-W1-HFB-ED256 | 256-state ED-matched HFB gap (does substrate gap reach 0.4643?) | w1 WP | med (gate \|δ−0.4643\|≤15%) |
| CF-INV9-W2-LAMBDA-SCALE | dS-entropy Λ-scale pinning + shell refinement (r≤1.0 O(1)) | w2 WP | med |
| CF-INV9-W2-WORLDSHEET-DIM | WORLDSHEET-BOUNDARY-62 critical-dim (emergent-string-leg decider) | w2 WP | **high** (sharpest falsifiable swampland claim) |
| CF-INV9-W2-DVALI-PIN | Dvali species scale-type consistency (ratio-vs-cutoff) | w2 WP | low |
| CF-INV9-W3-1-FOCK2POW64 | 2⁶⁴ Fock secular entanglement-envelope (W3-1 dynamical-fork discriminator) | w3 WP | **high** |
| CF-INV9-W3-2-IH-ENTROPY | isolated-horizon S∝A/4G_eff substrate-eval (SPLIT-import untested cell) | w3 WP | med |
| CF-INV9-W1-MODULAR-WIDE | wider-N/τ multi-map modular discriminator (corridor near-closed) | w1 WP | low |

## §C — Parallel-compute-wave carry-forwards (Q3 wave-together)

None. No candidate decomposed into N-orthogonal-axes-with-AND-closeout structures this dispatch.

## §D — Session-promotion items (non-math; designated-writer / session-track; NOT investigation edits)

These bear on curated session-track registers an investigation cannot touch. Route via `/rclab-investigate --investigation 9` → session-mode `/rclab-plan`; the named designated writer effects each in a session.

| Item | Source | Target register | Writer | Note |
|:--|:--|:--|:--|:--|
| §VII.BS BCS-channel support-row (exact geometry-fixity, Var_λ=0) | W1-3 (sign=PASS) | `permanent-results-registry.md §VII.BS` | mack/registry designated | unit-fixity confirmed from the BCS-gap channel |
| RETRACT `3586.5 M_KK`-as-dilaton-gradient cite | W1-2 | wherever cited (it is S62 ZPE curvature d²E_ZP/dq², not a gradient; 12× drift) | designated | provenance correction |
| CF14 → resolved AXIS-DEPENDENT (S consistent / V fails dS bound) | W1-2 | `atlas-08-open-questions.md` CF14 | designated | not swampland-consistent-throughout; no quintessence-w(z) falsifier-row warranted |
| substrate-first Δφ/M_Pl re-pin (0.170 is seed-author, not canonical) | W2-3 V.1 | canonical_constants provenance | designated | closest canonical delta_tau_crit_pos=0.175 is a DIFFERENT observable |
| Ordered-Veil info-story → "complete-on-one-reading-only / incomplete-as-exhibition" | W3-1 | capstone §5.3 + `atlas-04-assumptions.md` | capstone designated writer | **CAPSTONE-HYGIENE-GATE RELEVANT** — the promoting session MUST run the 5-question gate (Q3 status change) |
| Q7 SUM-vs-NO-SUM extended to 4th candidate (Fock trace = saddle-free Boltzmann trace) | W3-1 | session-96 Q7 workshop reconciliation | designated | extends standing Q7 categorical-isolation verdict |
| atlas-04 §6.3 effective-Friedmann-gap status + isolated-horizon-entropy import ruling | W3-2 | `atlas-04-assumptions.md` §6.3 + registry | capstone/registry designated | from the BOTH-ON-ORTHOGONAL-AXES + 8-row import table; **CAPSTONE-HYGIENE-GATE RELEVANT (Q1)** |

## §E — Pre-compute shell waves

None. All three waves executed to closure (no `Status: NOT STARTED` gate with no artifacts).

## Process note (no technical debt)

Two final-round workshop turns (kaku W3-1 R1-Turn-A; LQG W3-2 R2-Turn-B) emitted idle WITHOUT writing their section — the documented compute-mode no-write closure-failure mode, caught by **file byte-mutation check** (not idle/summary trust) and remediated in-session via SendMessage continuation to the same agent (preserves context; per `agent-standards.md §"Completion Verification"` + `feedback_dispatch-discipline.md`). No fresh re-spawns; both landed clean on the second pass. Lesson for the orchestrator: idle ≠ closure; verify workshop turns by byte-change + zero-residual-placeholder, never by `must_contain` heading presence (skeleton headings false-pass) or the agent's completion summary.
