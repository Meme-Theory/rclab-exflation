# NOISE Spot Check — Manual Review (Claude, not regex)

This document supersedes the regex-based judgments in `_noise_spot_check.md`. I read each of the 123 sampled entries' source context manually and applied the rubric in plain English. The sample composition is the same (seed=42 deterministic; same anchor_ids).

## Overall Verdict

**Haiku's NOISE classifications are correct, but the underlying problem is upstream.** Roughly 90-95% of sampled NOISE entries are factually correct calls per the rubric. The remaining 5-10% are edge cases where Haiku saw a truncated context and correctly flagged "fragment" without being able to see the full upstream context.

But "correct NOISE" hides the real story:

**The root cause is `extract_entities.py` over-extraction**, not Haiku misclassification. When the extractor grabs a markdown table cell, a sub-bullet inside a structural theorem, a SHA-256 hash label, a YAML pin, or a file-path reference and emits it as a separate `theorem` / `gate` / `equation` / `open_channel` record, Haiku looks at the resulting record and correctly says "this is not a theorem / gate / equation / channel — this is a fragment." The math/content in those fragments is often REAL; it's just been extracted into the wrong shape.

That's the user's earlier flagged-as-suspicious entries (`J_BdG D_BdG = D_BdG J_BdG`, `Cl(R^8): B_+ and B_- both give J^2 = +1`, etc.) in a sentence: real math, wrong record type. The math belongs in the parent theorem's statement; the extractor created phantom child theorems for each bullet or table row.

## Per-Table Findings

### closed_mechanisms (2 sampled / 26 NOISE)

Both correctly NOISE. `CF-68` is a bare carry-forward ID (no descriptive content). `§VII.K-PROP-W8.CELL-OCCUPANCY (cutoff_AL2010 / cutoff_sqrt L2 status update)` is a registry-status annotation, not a mechanism description. Confidence: high.

### open_channels (25 sampled / 481 NOISE)

Patterns: ~80% of sampled entries are extractions from RESOLVED-channels tables (already-closed mechanisms mistakenly in the open table), markdown table column headers (`M_GUT (10^16 GeV)`, `M_Planck (10^19 GeV)`, `Route E (cumulative geometric corrections)`, `Plan SHA`, `Verdict file`), or sub-item gate batches (`EIGENVECTOR-48`, `BERRY-EDGE-48`).

Specifically correct NOISE:
- `Threshold corrections for NCG-KK` — closed in S50-S51, should be in closed_mechanisms not open_channels
- `Transit production` — table-row column header, not a channel (user's flagged example; user is right that this is obviously NOISE)
- `A_s insensitive to E_C** (W2-G)` — already marked PASS in S75, not actually open
- `[-0.988, -0.942)` — table-cell w_0 range value, not a question

A few borderline:
- `EMPIRICAL-τ_fold RETENTION` — name reads as status tag, but underlying topic is genuinely an active open question
- `Volume exchange` — extracted from a CLOSED-status row in a survivors-of-flatness table; correctly NOISE for being closed
- `[SP]S-5 Twistor correspondence` — substantive math question marked DEFERRED in S25 archive; might still be open or might be quietly forgotten

Confidence: ~95% Haiku-correct.

### theorems (51 sampled / 1020 NOISE)

This is the table with the biggest mass of NOISE, and on close reading, Haiku's calls are overwhelmingly correct:

- **SHA hash labels** (5+ sampled, all correctly NOISE): `audit_sha256** (full 64-char): ...`, `content_sha256** (full 64-char): ...`. The extractor grabbed bullet markers from registry-entry SHA closure blocks and emitted them as theorem names.
- **File/script path bullets** (correctly NOISE): `Script: computations/...`, `Producing script: ...`, `W4a-16 data: computations/...`. Extractor over-extraction from provenance bullets.
- **Table rows** (correctly NOISE): `Sessions S52-S60`, `52-60`, `[NEW S45] Bogoliubov/KZ n_s`, `155,984`, `Casimir scalar + vector`. Extractor pulled cell contents from cumulative-statistics tables, walls-extended tables, atlas tables.
- **Truncated section-headers / structural-position prose** (correctly NOISE): `Structural position**: AUDIT / registration gate...`, `PRU compliance**: 9/9 machinery-pin parameters pinned`, `Writer**: mack-cosmic-bridge`. These are bullets from the `##### (l) Self-assessment` block of registry entries — section labels, not theorem statements.
- **Registry-housekeeping labels** (correctly NOISE): `Layer-2-A vs Layer-2-B coverage`, `Cross-pillar-bridge Pole-Scope (T1-20)`, `Joint-theorem 4-stage promotion pathway`. These are status-table row labels from the mega-matrix.
- **Bare era/sub-era labels** (correctly NOISE): `24b`, `1814`, `30-55`.

Genuine borderline / I'd push back on Haiku for:
- `proven_434` `W3-5 two-speed transfer identity c_S_canon = f_B (PASS, machine precision)` — this looks like a real permanent-grade theorem statement, with explicit identity and PASS verdict. Haiku marked it NOISE for "lacks theorem structural form" — I'd call this borderline. The entry's `statement` field has the full theorem text; the extractor put it in `name` truncated. Recovery would be straightforward.
- `proven_383` Hille-Phillips theorem — bibliographic citation with embedded theorem statement ("Bernstein functions have Levy-Khintchine representation but only CM functions have positive Radon Laplace representation"). Borderline: it's a known theorem from outside the framework cited in a session WP — should it be in the theorems table? Probably not under the framework's definition.
- `proven_360` `FUNCTIONAL-INDEPENDENT: eigenvalue ratios, moment ratios...` — extracted as a truncated list. The context (S75 W3 PERMANENT THEOREM block) shows there's a real PERMANENT THEOREM upstream that this fragment was part of.

Confidence: ~90% Haiku-correct.

### gates (15 sampled / 293 NOISE)

Two distinct patterns:

1. **Bare letter-number labels** (5 sampled, all AGREE): `G-29c`, `E-2`, `KC-1`, `QA-1`, `SP-3` — these are old workshop/session sub-labels from S22-S29 era. Correctly NOISE — they're not S82+ gate-ID format and lack mechanism/wave/session structure.

2. **`T3-BATCH-S{N}-*` migration markers** (8 sampled): These are batch-canonical-hygiene tier-0 archive markers from `s81_batch_gate_verdicts.txt`. Each marker corresponds to a tier-0 archive script that was MIGRATED with `verdict=MIGRATED, scheme=batch-canonical-hygiene, convention=no-run-no-gate, L_max=NA`. These ARE legitimate audit-trail records of the tier0/tier1 migration, but they're not real GATES (no PASS/FAIL/INFO physics verdict). Whether they should be in the gates table depends on policy — I'd argue NOISE is correct because they're migration housekeeping, not physics gates.

Confidence: high. The T3-BATCH calls are a policy choice (audit-trail vs gate-table), not an accuracy question.

### data_provenance (10 sampled / 186 NOISE)

All 10 sampled are correctly NOISE under a strict rubric:
- `neff_read.py`, `npz_probe.py` — utility scripts that print to text, no computational output
- `w5_falsifier_inventory_consolidation_writer.py` — documentation script with no outputs
- `w1_deferred_pending_audit_test.py` — self-test driver, not real physics
- `s55_conformal_diagram.py`, `s55_euclid_continuum.py`, `s46_fwd_bwd_ns.py` — older session scripts where Haiku says "session N doesn't exist" (Haiku was wrong on this specifically — these sessions DO exist, they're archived)

One concerning failure mode: Haiku's "session-46 does not exist in framework" claim is FALSE — session-46 IS in `sessions/archive/`. Same for session-55, session-70. So for ~30% of data_provenance NOISE calls, the REASON Haiku gave is wrong (the source exists in the archive). The verdict (NOISE) might still be right because the scripts are pre-S34 utility-class — but the reasoning is off.

Confidence: ~70% Haiku-correct verdict; some reasons are factually wrong (claim session doesn't exist when it does).

### session_files (4 sampled / 4 NOISE; full enumeration)

All 4 correctly NOISE. Two are template stubs (`_registry-template.md`, `session-29Aa-prompt.md` — the second is a session-PLAN prompt, not a session result). Two are session-wrapup stubs that were never filled in (`session-63-W7-workingpaper.md`, `session-66-wrapup.md`). The "<10KB filesize" heuristic that drove session_files extraction picked up template stubs that should've been excluded.

Confidence: 100%.

### equations (8 sampled / 144 NOISE)

I already worked through these in the earlier diagnostic. Summary:
- `scheme=stage-2-cross-axis-3-reviewer-axis-a-pillar-1-ncg-axiomatic \` — YAML pin, correctly NOISE
- `chi_A_volovik_2003 = 1.500000 [canonical_constants; 3He-A susceptibility]` — annotated constant assignment, correctly NOISE (lives in canonical_constants.py canonically)
- `N_C = 1/(1+N_B²) is NOT an emergent algebraic relation...` — prose statement with embedded equation, correctly NOISE
- `R(0) = 4.0000000000` — gate verdict output, correctly NOISE
- `D_can slightly more repulsive (Delta_q = +0.075)` — prose with parenthetical numeric, correctly NOISE
- `T^{(3)} = T^{(3)}_{[abc]}` — torsion symbol identity in prose context, borderline (it IS a math identity but in narrative)
- `pole s=4. Expected band: NO-ACTION or ADVISORY` — fragmented plan-doc prose, correctly NOISE
- `s_cm2 = float(np.sum(c_arr * m_arr * m_arr))` — numpy code line, correctly NOISE

Confidence: ~95% Haiku-correct. My earlier regex DISAGREE count of 8/8 was a heuristic over-fire; real disagreement count is closer to 0-1/8.

### researchers (2 sampled / 2 NOISE)

Both correctly NOISE: `Lost-Treasures` and `RF-Antimatter` are empty/minimal researcher stub folders.

### constants (2 sampled / 2 NOISE)

Both correctly NOISE: `Vol_SU3_WRONG` is the deliberately-deprecated DO-NOT-USE pin (kept for audit trail); `lambda_unit_canonical` is a string literal pin (`'dimensionless_M_KK_natural'`) not a numerical constant.

### registries (4 sampled / 4 NOISE; full enumeration)

All 4 correctly NOISE: 3 are ARCHIVED/SUPERSEDED stubs (Phononic-Crystal-Geometry, framework-bbn-hypothesis, lrd-observational-constraints stub), 1 is the literal template placeholder `<Registry Name>`.

## Aggregate Assessment

| Table | Haiku-correct verdict rate | Confidence |
|:------|:--------------------------|:-----------|
| closed_mechanisms | ~100% | high |
| open_channels | ~95% | high |
| theorems | ~90% | medium-high |
| gates | ~100% | high (some policy questions on T3-BATCH-* class) |
| data_provenance | ~70% (verdict) / ~70% (reasons sometimes wrong) | medium |
| session_files | 100% | high |
| equations | ~95% | high |
| researchers | 100% | high |
| constants | 100% | high |
| registries | 100% | high |

**Weighted estimate**: ~92% of the 2,162 NOISE entries are correctly tagged.

## Recommendation

The NOISE filter is safe to apply as a coarse cleanup pass. Of the ~2,162 entries it would drop, ~92% (≈1,990) are correctly noise (table cells, bullets, SHA hashes, stubs, archived material, status labels, file paths). The remaining ~8% (~170) are borderline edge cases that lose some content but are recoverable from the parent context.

However, the **structurally right fix is upstream**: tighten `extract_entities.py` to stop emitting:
- Markdown table cells as separate theorem/channel records
- Bullets inside registry-entry self-assessment blocks as theorems
- SHA-256 hash bullet lines as theorems
- File-path bullets as theorems
- YAML pin lines as equations
- Numpy code as equations
- Template/stub files as session_files

That would shrink the NOISE pool from ~2,162 to maybe ~200-400 (estimate), and the next audit run would have a much higher signal-to-noise ratio. The current state is "audit cleanup of an over-eager extractor"; the upstream fix is "make the extractor less eager."

## Decision space for the user

1. **Apply NOISE filter now, defer extractor cleanup** — fastest path; knowledge.db gets cleaner immediately. ~8% noise residual remains in the form of correctly-judged-as-noise entries.
2. **Apply NOISE filter + fix `extract_entities.py` in same pass** — better hygiene, but requires reading extract_entities.py and identifying the bullet/table-cell-extraction patterns. More work, structural fix.
3. **Don't apply NOISE filter; just fix extractor** — slowest convergence; the NOISE entries currently in the DB stay until re-extraction.

I'd lean toward (2) — applying the filter is mechanical, and reading extract_entities.py is bounded work. Either way, the spot check confirms the filter is safe to apply.
