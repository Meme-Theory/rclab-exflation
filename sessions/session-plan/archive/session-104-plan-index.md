# Session 104 — Plan Index (fanout mode)

**Frozen**: 2026-06-10 (`/rclab-plan --session 104 --extra "§7 of the assay"`). 5 gated waves, 14 gates.
**Corpus**: 4 S103 WP carry-forwards + 10 gem-triage candidates (`downloads/research-sweep-s103/GEM-TRIAGE.md` §7). Context: `session-104-context.md`. Partition: `session-104-partition.md`.
**Validation**: upstream-pin validator PASS ×5 (`session-104-plan-w{i}-validation.json`) + R3 YAML validator PASS ×5 (14/14 gate blocks).
**Verdict file (all gates)**: `computations/session-104/s104_gate_verdicts.txt` via race-safe `emit_verdict`.

| Wave | Theme | Owner | Gates | Plan file |
|:-----|:------|:------|:-----:|:----------|
| W1 | Standing precision CFs (S103 carry-forwards) | gen-physicist | 4 | `session-104-plan-w1.md` |
| W2 | Geometric invariants (gem: berry mine) | berry-geometric-phase-theorist | 2 | `session-104-plan-w2.md` |
| W3 | Spectral-functional diagnostics (gem: rmt+zeta) | lizzi-spectral-functional-theorist | 2 | `session-104-plan-w3.md` |
| W4 | Transit-shape (gem: gw+qcd) | transit-dynamics-theorist | 2 | `session-104-plan-w4.md` |
| W5 | Bridge-spec gates (NOT-DISPATCHABLE-risk class) | gen-physicist | 4 | `session-104-plan-w5.md` |

**Run-order**: W1 first (start the BRANCH-IV offline Sym^13/14 irrep build EARLY — it is the session's wall; multi-hour CPU); W2–W5 independent (no cross-wave edges). W5's LOOP-COUNTING spec carries a joint-consideration flag with W1's L_max CFs (no shared pins).

**M4 allowlist**: `S104-VIIBS-CLAUSE-B-WORDING` appended at plan-freeze (`e7275804…`; orchestrator append per the recursion-attack closure; rationale at `methodology-wave-instances.md`).

**Plan-freeze register state**: EVOI re-stamped S104 (audit PASS, lag 0); atlas-08 S103 freshness bullets + Q28 ANSWERED inline tag (backing audit `registry/atlas-08-freshness-S103.md`); atlas-04 S103 in-cell annotations (C9/§VIII.B FUNCTIONAL-SELECT-conditional discharge FLAGGED for designated-writer review, not silently flipped); open-channel-ledger S104 refresh; mack plan-time dispatch LANDED (Row #85 multi-anchor σ-table 1.4048σ→2.6970σ→3.1316σ→5σ + anti-rescue fence; NEW Row #86 LIV species-universality null w/ named opponent Li-Ma 2508.11172; watchlist saddle guard + area-quantum WATCH + X(2370)/g-2 notes + α_s two-scale PLAN-DRIFT repair; atlas-04 §IX Item-3 refresh).

**Workshop track (NOT plan gates; dispatch via `/rclab-workshop`)**: (1) the W4-flip — modular-flavor 2506.23343 ↦ Missing-ingredient-#1, `--agents neutrino-detection-specialist,connes-ncg-theorist --rounds 3` (GEM-TRIAGE §4 carries the adjudication question); (2) κ-deformed-NCG vs Jensen opposite-sign n_s discriminator; (3) birefringence Berry-CP-null vs emergent parity-odd channel. These run parallel to (or before) the compute session at the user's discretion.

**Session-close obligation (pre-registered)**: the capstone-hygiene 5-question gate (MANDATORY, K=3) — S104 is capstone-touching by construction (the W1-4 §VII.BS patch + the plan-time mack §7.1/§7 surface landings, audit-provenance "S104 plan-freeze mack dispatch"); the Q1–Q5 block MUST appear at session close, citing the plan-time mack dispatch rather than re-running it.
