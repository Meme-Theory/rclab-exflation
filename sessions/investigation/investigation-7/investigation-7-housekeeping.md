# Investigation 7 — Housekeeping Ledger

**Date**: 2026-06-15 | **Mode**: INVESTIGATION (index dispatch, 4 waves, 14 gates) | **Template**: `.claude/templates/session-housekeeping.md`

Catalogues the non-math items surfaced across investigation-7. **§A** = effected in-investigation (orchestrator-direct, investigation-track only). **§B** = session-promotion queue (session-track curated-register edits the verdicts CONSUME — NAMED here for `/rclab-investigate --investigation 7` to lift into the session-track housekeeping ledger; an investigation MUST NOT mutate session-track registers, `gate-verdicts.md §"Investigation-Track Canonical Path"`). **§C** = math carry-forward pointers (the compute CFs live in the wave WPs).

---

## §A — In-investigation resolutions (Effected In-Session; investigation-track only)

- [x] **W1-5 collapse-rule reconciliation** — caught at orchestrator verification: composite=PASS contradicted its own 3-tuple (`sign_verdict=FAIL`), violating the deterministic collapse rule. Resolved via SendMessage continuation → the agent re-emitted composite=FAIL with `supersedes=803abfbc…` (Option-A; original PASS line RETAINED per absolute verdict permanence). The agent made the principled non-cherry-picking call (sign evaluated at the pre-registered ν_r1, not relocated to the void-wall to rescue a PASS). — `computations/investigation-7/inv7_gate_verdicts.txt` lines 54 (superseded) + 61 (canonical FAIL); WP §W1-5 Verdict updated to FAIL.
- [x] **W4-2 Effected-In-Session checkbox patch** — 2 unchecked `- [ ]` boxes (session-track items the agent correctly named but mis-formatted as actionable boxes) → `- [x]` with "NAMED for session-promotion; NOT effected here (track-local boundary)". Orchestrator-direct presentation patch (hard rule 2; structural-anchor the closure audit keys on, no specialist framing). — `sessions/investigation/investigation-7/workshops/n-pbh-physical-vs-tautology.md:352-353`.
- [x] **Stray helper-script cleanup** — deleted `computations/investigation-7/_inv7_w1_2_wp_writer.py` (transient atomic-WP-writer from the shared-file race; fed no verdict SHA). KEPT `computations/investigation-7/inv7_w1_5_collapse_correction.py` (generated the W1-5 corrective `audit_sha256=8ff51477…`; preserved per `mechanical-closure-discipline.md §"carry-forward script-bytes immutability"`).
- [x] **W2-3 solo executed inline** — orchestrator ran the n_PBH error-budget gate (no subagent spawn), emitted the INFO verdict via `emit_verdict(track="investigation")`, wrote WP §W2-3. — `computations/investigation-7/inv7_w2_3_n_pbh_lpix_error_budget.{py,npz,png}` + verdict line + WP §W2-3.
- [x] **Four wave-syntheses written** (team-lead; the only sections the orchestrator authors) — `investigation-7-w{1,2,3,4}-workingpaper.md` "## Wave N Synthesis" + "## Carry-Forward Computations" + "## Constraint-Map Updates" + "## Files Produced".
- [x] **Both workshop skeletons built** before any agent turn (shared-doc-first; round headings + placeholders + Verdict table + Wrap-Up) — `workshops/{effective-friedmann-functional-form,n-pbh-physical-vs-tautology}.md`.

**Self-audit**: `grep -c '^- \[ \]'` on this §A = 0 (all items checked). Session-track items are in §B (NOT effected; named).

---

## §B — Session-promotion queue (session-track; route to `/rclab-investigate --investigation 7`)

These are session-track curated-register / capstone / falsifier-inventory / knowledge-MCP edits the investigation verdicts CONSUME. They are NAMED here, NOT effected (track-local boundary). `/rclab-investigate --investigation 7` lifts them into the session-track housekeeping ledger for session-promotion. Falsifier/observable-surface rows are `mack-cosmic-bridge` sole-writer (`feedback_mack-bridge-role.md`).

| # | Item | Target | Consuming verdict |
|:--|:-----|:-------|:------------------|
| HY1 | `proven_1450` "JWST LRD BH-seed-mass spectrum predictions" → down-tag to OPEN (reconcile Row #88) | knowledge-MCP `proven_1450` + atlas-04 | W2 (Row #88 both routes FAIL) |
| HY2 | `lrd-observational-constraints.md` post-S85 refresh (split-state tension, Compton-thick, dust-free, non-variable, three-interpretation triage) | `lrd-observational-constraints.md` (LRD AMRI registry) | W2 corpus |
| HY3 | §VII.AX Tier-2-dimensionful HELD-status loudness — so `7.2761e-23 m⁻³` is never cited as a clean LRD prediction; cite saturation-freeze 1.758e-23 as honest provisional central; four-seam status | `lrd-observational-constraints.md` | **W4-2 verdict** (Layer-3 unprotected) |
| HY3b | §VII.AX.OP-PROJ register re-tag → NON-PROMOTION-BY-HELD-NUMBER (`dimensionful-slot-collision`) | `permanent-results-registry.md` §VII.AX | **W4-2 verdict** |
| HY4 | `proven_493` "Three generations from Z₃ triality" → down-scope to "Z₃ grading exists"; family-replication-with-hierarchy = canonical OPEN | knowledge-MCP `proven_493` + atlas + capstone #7 | (plan Q2; not a W-gate consumer) |
| HY5 | α_LIV=0 → "α_LIV=0 at leading order"; promote discrete-vs-continuous to a stated Fermi-LAT/LHAASO discriminator | capstone §9 / QF-63 / atlas | (plan Q2) |
| HY6 | Capstone §6.2 "no bounce, asymmetric white hole" → "no bounce UNDER monotone-ramp transit dynamics" | capstone §6.2 (designated-writer patch) | **W4-1 verdict** (no-bounce SCOPED) |
| HY7 | Cross-link S105-S106 "no geometric area-clock" → S92 isolated-horizon workshop; register "no discrete area spectrum" as a stated structural discriminator vs loop-quantum-gravity; present JACOBSON-NONLOCAL-64 alongside spin-foam-divergence | capstone / atlas-08 | W3-1 (area-law, no clock) + W3-2 |
| HY8 | Falsifier-inventory hygiene: retire stale "σ₈=0.799 relieves S₈" framing (post-KiDS-Legacy); promote bulk-flow to explicit BOUNDARY statement; cross-ref Row #67 as cautionary precedent | `falsifier-master-inventory.md` (mack) | W1 corpus |
| HY9 | W1-6 f·σ₈ growth-suppression falsifier-row candidate (live-watch DESI-DR3/5yr sub-2σ → Euclid ≥2σ decisive) | `falsifier-master-inventory.md` (mack) | **W1-6 verdict** |
| HY10 | W3-3 joint-3-axis CMB discriminator (low-ℓ + α_s + r; α_s decisive >27σ at SO DR1) — S96 §L3 ~2030 forecast | `falsifier-master-inventory.md` (mack) | **W3-3 verdict** |

**Standing gap (no tractable gate)**: K_pivot scale mapping (cosmic-web G4 / LQG-adjacent) — recorded, not gated (leverage ≠ tractability).

---

## §C — Math carry-forward pointers (compute CFs; canonical source = wave WPs)

These are genuine future computes (4-field specs in the wave WPs). They propagate via `/rclab-investigate --investigation 7` → session-promotion (a permanent result is MIGRATED into a `session-{N}` gate, not cited — investigation verdicts are track-local, not swept by `/weave`).

| CF-ID | Title | WP source |
|:------|:------|:----------|
| CF-INV7-W1-5-SURVEY-FORWARD-MODEL | persistent-homology web-topology survey forecast (smoothing+bias+mask on the Z=620σ idealized separation) | `investigation-7-w1-workingpaper.md` |
| CF-INV7-W2-2-ENVELOPE-SCALE-BRIDGE | emergent-scale transport for the substrate photosphere T (M_KK→optical `deg(T_{BZ→pivot})`) | `investigation-7-w2-workingpaper.md` |
| CF-INV7-W3-2-SIGMA-FROM-BOGOLIUBOV | first-principles σ for the GFT-condensate a₀ resummation (magnitude pin → A_s convergence-CERTIFIED test) | `investigation-7-w3-workingpaper.md` |
| CF-INV7-W4-1-MINISUPERSPACE | the H²(ρ) functional-form decider (MONOTONE-RAMP vs ONE-SIDED-CEILING; the a_4 R²+Weyl² operator sign; scheme-pin MANDATORY) | `investigation-7-w4-workingpaper.md` + workshop md |
| CF-INV7-W4-2-1 | Counting-axis pin + Λ_UV=M_KK n_PBH magnitude re-source (Pinning A retained) | `investigation-7-w4-workingpaper.md` + workshop md |
| CF-INV7-W4-2-2 | Tier-1 dimensionless re-anchor (cascade exponent 5; Layer-1 survivor) | `investigation-7-w4-workingpaper.md` + workshop md |

---

## Cross-references

- `gate-verdicts.md §"Investigation-Track Canonical Path"` — track-local boundary (investigation verdicts not swept by `/weave`; permanence via session-promotion).
- `.claude/rules/Investigating-Workshops.md` — Q2 housekeeping vs Q1 workshop routing.
- `.claude/templates/session-housekeeping.md` — the §A-E partition this ledger adapts for investigation mode.
- `feedback_mack-bridge-role.md` — `mack-cosmic-bridge` sole-writer of the §7 falsifier/observable surface (HY3, HY8, HY9, HY10).
