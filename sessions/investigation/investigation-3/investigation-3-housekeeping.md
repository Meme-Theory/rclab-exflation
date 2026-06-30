# Investigation 3 — Housekeeping Ledger

**Investigation**: 3 | **Closed**: 2026-06-15 | **Waves**: 4 (14 gates: 12 compute + 1 solo + 1 workshop) | **Driver**: `/rclab-coordinate` (full-investigation dispatch)

Consolidates the non-workshop / session-promotion items surfaced across all four waves. **Investigation-track boundary** (`gate-verdicts.md §"Investigation-Track Canonical Path"`): an investigation CANNOT mutate session-track curated registers (Atlas, `permanent-results-registry.md`, EVOI, `canonical_constants.py`, `falsifier-master-inventory.md`). Items in §B route to `/rclab-investigate --investigation 3` close for session-promotion. Math carry-forwards live in each wave's WP `## Carry-Forward Computations` block (the canonical carrier `/rclab-investigate` lifts) — pointed to in §C, not duplicated.

## §A — In-session resolutions (orchestrator-effected, complete)

- [x] Removed orphaned one-shot WP-writer helper `computations/investigation-3/_inv3_w3_3_wp_writer.py` (the W3-3 agent's atomic-substitution scratch script; siblings W3-2/4/5 removed theirs). In-session hygiene per `CLAUDE.md §"No Technical Debt"`. Verified 0 `_wp_writer` helpers remain.
- [x] §W3-1 solo-gate WP section written by orchestrator (deferred during the W3 concurrent-write window to avoid a 5th-writer race; written once the four compute agents quiesced).
- [x] Wave-syntheses written into all four WPs (W1/W2/W3 with math-vs-structural + carry-forwards + constraint-map + files; W4 with the converged verdict).

## §B — Session-promotion candidates (→ /rclab-investigate close; session-track, NOT investigation-effectable)

| # | Item | Source gate | Target register | Notes |
|:--|:-----|:------------|:----------------|:------|
| B1 | n3=dim(3,0)=10 as a chain-level SU(3) identity (α 0.855 ppm + proton-cubic share n3²=100; only n3=10 sub-ppm) | W3-3(i) PASS | `permanent-results-registry.md` | the investigation's strongest positive; recompute = CF-INV3-W3-A |
| B2 | c₂=0, the 13th trivial topological invariant — first on the non-Abelian (Wilczek-Zee) channel | W1-4 PASS | §VII.BR family | recompute = CF-INV3-W1-B |
| B3 | Isospectral rigidity at L=3 (D_K² spectrum reconstructs Jensen geometry; Connes-reconstructible) | W2-2 PASS | §VII.BR operational support | recompute = CF-INV3-W2-C |
| B4 | A_s single regulator-tagged number gap_OOM=+6.008 (n_s-selected near-floor functional) | W2-3 INFO | `falsifier-master-inventory.md` row | **mack-cosmic-bridge SOLE WRITER** on session-promotion (`feedback_mack-bridge-role.md`); correctly NOT written in-investigation |
| B5 | M_KK-DERIVATION = **SCOPED-INTERMEDIATE** (ratio-derivable, normalization irreducibly external) + the M_Pl·Φ(integers) route WITHDRAWN | W4-1 workshop | §VII.BS + EVOI §6 standing-gap annotation | designated-writer prose touch; the seconds-valued a(t)-gap reframes as a structural feature |
| B6 | A₂-fold germ on the 2-param U(2)-invariant surface + the §W1-3 PRU Class-8.2 rubric-form operator note | W1-3 INFO | permanent-results / methodology | restate operator as Morse-non-degeneracy discriminant on promotion; recompute = CF-INV3-W1-C |
| B7 | HY8 — `phi_paasch` carries NO PROVENANCE entry in the knowledge MCP | W3 (`get_constant`) | `canonical_constants.py` PROVENANCE | register tag |
| B8 | HY9 — Paasch LNH Dirac-G~1/t scaffolding exclusion note (algebraic core is LNH-independent) | W3 / W4 | framework register | severing the dead scaffolding is the prereq to citing Paasch absolute masses as M_KK candidates |
| B9 | HY3 — f_WZ=2.888785e-06 non-canonical (promotion pending) | W1-4 | `canonical_constants.py` | sourced at runtime as cross-check only |
| B10 | HY11 — OCR-garbled-formula re-pin (per seed §"Non-gate items") | seed | framework register | part of the plan index's quarantined HY1–HY11 set |

(The plan index §"Non-gate items" enumerated 11 session-track HY items quarantined from this investigation; B5/B7–B10 are the ones surfaced or sharpened by the waves. The full HY1–HY11 set routes at `/rclab-investigate` close.)

## §C — Math carry-forwards (canonical carrier = per-wave WP `## Carry-Forward Computations`; `/rclab-investigate` lifts — pointers only)

- **W1** (`investigation-3-w1-workingpaper.md`): CF-INV3-W1-A (block-level Berry–Tabor integrability promotion), -B (c₂=0 §VII.BR), -C (A₂ germ w/ corrected Morse operator).
- **W2** (`investigation-3-w2-workingpaper.md`): CF-INV3-W2-A (energy-axis / continuum-extrapolated d_s scale-transport — a DIFFERENT observable than the closed UB-1), -B (A_s near-floor vs full-spectral-weight reconciliation), -C (rigidity §VII.BR promotion).
- **W3** (`investigation-3-w3-workingpaper.md`): CF-INV3-W3-A (A1 SU(3) identity promotion), -B (two-α reconciliation C3), -C (Koide Z₃-forcing / k*≈1.705 circulant test).
- **W4** (`investigation-3-w4-workingpaper.md` + `workshops/m-kk-derivability.md`): **INV3-W4-1-FWD** (non-spectral-scale existence scan — the decisive M_KK-DERIVATION gate; PASS ⇒ M_KK-DERIVATION flips LIVE, §VII.BS falsified rank-0; FAIL/INFO ⇒ hardens to PROVEN-WALL on normalization).

## §D — Process observations (no action; recorded for next-investigation plan hygiene)

- **Concurrent-write race**: the plan placed all of a wave's gate sections in ONE WP, so 4–5 agents contend on it (W2-2 + the W3 agents reported Edit-tool mtime-guard trips). Mitigated this run by mandating an atomic single-section Python substitution in each prompt (proven non-clobbering — all sibling sections verified byte-intact). For future investigation plans, either split per-gate WP files OR keep the atomic-substitution mandate in the dispatch prompt (`feedback_session-process.md`: ≤2 agents per shared file).
- **Plan-text imprecision**: the W1 machinery pin labeled `N_eval=78080` as the "L12 cache unique count" — that is the L_max=10 figure (per `phononic-framing.md`); the L12 cache is 166,896-with-multiplicity / 6,997-globally-unique. Agents used the actual cache contents; results sound.
- **Gate-id vs must_contain mismatch**: W2/W3 plan `gate_id`s are long (e.g. `INV3-W2-1-DS-FLOW-SCALE-TRANSPORT`) but each gate's `verdict_line.must_contain` anchors on the short `^INV3-W{w}-{n}:`. Agents emitted the short gate-id (descriptive suffix in `scheme=`) per orchestrator instruction so closure passed. For future plans, align `gate_id` with the must_contain anchor.
- **W2-3 Option-A supersession**: an in-script bug-fix re-emission (added `print_verdict_payload` per must_contain; physics identical) produced two canonical lines; the corrective carries `supersedes=73e0b9d8…` (full 64-hex) on the successor line per `gate-verdicts.md §"Option A"`. Audit-clean.
