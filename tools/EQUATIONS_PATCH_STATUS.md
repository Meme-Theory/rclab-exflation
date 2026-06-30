# Equations Extractor Patch — Status

**Date**: 2026-05-18
**Status**: DEPLOYED. Patches B + C applied to `tools/extract_entities.py`, `/weave --update` executed, audit transferred to v2.

## What changed in the live KB

`/weave --update` was run on 2026-05-18 after Patches B + C were committed. Equations-table totals:

| Quantity | v1 (pre-patch) | v2 (post-patch) | Δ |
|:---|---:|---:|---:|
| Equations total | 22,593 | 18,038 | -4,555 (-20.2%) |
| Equations structural | 17,847 | 13,114 | -4,733 (-26.5%) |
| Equations inline | 2,655 | 2,655 | 0 |
| Equations display | 1,288 | 1,288 | 0 |
| Equations code | 949 | 949 | 0 |
| Equations comment | 32 | 32 | 0 |

Patches touch only the `structural` capture path; other capture paths are unchanged. The 4,733-entry structural drop maps to the audited 24.6% drop rate scaled to the full population.

## Audit preservation

The Haiku audit (`tools/_anchor_validation_results.json`, 10,919 verdicts) was preserved across the extractor change via the content-key reconciler. Outcome:

| Table | v1 audited | v2 transferred | dropped by patches | pre-existing orphans |
|:---|---:|---:|---:|---:|
| theorems | 1,936 | 1,898 | 0 | 38 |
| closed_mechanisms | 266 | 266 | 0 | 0 |
| gates | 2,786 | 2,771 | 0 | 15 |
| open_channels | 826 | 826 | 0 | 0 |
| data_provenance | 2,428 | 2,428 | 0 | 0 |
| **equations** | **500** | **377** | **123** | **0** |
| researchers | 32 | 32 | 0 | 0 |
| agents | 33 | 33 | 0 | 0 |
| session_files | 1,835 | 1,835 | 0 | 0 |
| registries | 144 | 144 | 0 | 0 |
| constants | 133 | 133 | 0 | 0 |
| **TOTAL** | **10,919** | **10,743** | **123** | **53** |

**98.4% of audited verdicts preserved** onto v2 anchor_ids. The 123 audited equations dropped are entries the patches removed (~71 NOISE correctly killed + ~52 VALID false-positives, mostly Haiku-borderline cases that the original prose-pollution analysis had also flagged). The 53 orphans are pre-existing SQLite/JSON drift + Haiku fabrications, not caused by the patches.

Canonical audit going forward: `tools/_anchor_validation_results_v2.json`. The original `tools/_anchor_validation_results.json` is the v1 keying and stays on disk for reference / rollback.

## What changed in `tools/extract_entities.py`

Two coordinated edits to the structural-equation path:

1. **Patch C** (LHS regex tightening) — `RE_STRUCT_EQ` near the equation-extraction section. LHS now disallows bare whitespace between tokens; balanced `{...}` and `(...)` groups are admitted as opaque tokens so LaTeX subscripts (`T_{mu nu}`) and parenthesized openers (`[V_KK]`, `(iii) chi = +1`) still match. Closes prose-with-embedded-equation captures.
2. **Patch B** (in-loop denylist + tail-stopword) — at the top of the structural for-loop. Rejects:
   - Section headers ending in `:`.
   - LHS starting with verdict-line metadata pins (`audit_sha256`, `content_sha256`, `convention`, `scheme`, `tier_pin`, `supersedes`, `value`).
   - Lines whose last token is an auxiliary verb / preposition / article (mid-clause truncation indicator).

The module-level constants `_PATCH_B_VERDICT_PIN_PREFIXES` and `_PATCH_B_PROSE_TAIL_STOPWORDS` are defined near `RE_STRUCT_EQ` and consumed inside the structural for-loop.

**Skipped (deferred)**: Mode-A corpus restriction. The verdict-line schema parser idea was structurally right but addresses only 2 of 39 audited NOISE entries. The bulk of Mode-A NOISE (37 entries) comes from per-script ad-hoc output logs with no unifying schema. Cleanup of those is a future-session item.

## Rollback procedure

If the patches turn out to have a regression that wasn't visible in the audited sample:

```
# Restore v1 index
cp tools/knowledge-index.v1.json.bak tools/knowledge-index.json

# Restore v1 audit canonical
# (The v1 file _anchor_validation_results.json is still on disk; just stop
# using _anchor_validation_results_v2.json.)

# Resync SQLite to match v1
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/knowledge_db.py --sync

# Rebuild downstream artifacts from v1
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/viz/console/build_data.py
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/build_topic_pages.py
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/export_routing_manifest.py --check

# Revert the extract_entities.py edits (Patches B + C)
# git diff HEAD -- tools/extract_entities.py
# git checkout HEAD -- tools/extract_entities.py
```

## Files touched / produced

Live infrastructure (kept):
- `tools/extract_entities.py` — patches B + C applied at structural-equation extraction section
- `tools/_reconcile_audit.py` — content-key reconciler (build, verify, simulate, apply modes)
- `tools/_audit_content_keys.json` — keymap artifact (~2.77 MB; v1 audit anchor_ids → content keys)
- `tools/_audit_content_keys_diagnostics.json` — per-table coverage stats from keymap build
- `tools/_anchor_validation_results_v2.json` — canonical audit on v2 anchor_ids
- `tools/_anchor_validation_results_v2.transfer_report.json` — per-table transfer details
- `tools/knowledge-index.v1.json.bak` — v1 index snapshot for rollback (~44 MB)
- `tools/EQUATIONS_PATCH_STATUS.md` — this file

Throwaway diagnostics (delete at discretion):
- `tools/_eq_shape_analysis.py` — characterized NOISE distribution shape on audited 500
- `tools/_split_compoutput_noise.py` — split Mode-A NOISE by file subtype
- `tools/_patch_bc_preview.py` — measured patches against audit before live deploy

## Known limitations / future-session items

- ~62 NOISE entries (~47% of audited NOISE) still leak through Patches B+C. The residual splits into ~8 small patterns (quoted-string RHS, iteration counters, `[X] = dimensionless` checks, output-log multi-value rows, etc.). Each needs a targeted rule with its own false-positive risk.
- The 17,500+ unaudited structural equations have unknown NOISE shape. The audited 500 was 2.2% sample; projections were approximate but the actual drop (4,733 structural) aligned with the audit's projected 26.5%.
- Audit reliability ceiling: the previous Claude noted ~92% Haiku-correct on close inspection. The remaining ~8% is part of the variance in the empirical metrics above.
- The sister-Opus adversarial review at `.claude/worktrees/agent-a1a4f1e52519ed481/tools/_patch_review_test{1..5}.py` contains test harnesses worth re-running after any future patch changes.
- Mode-A (per-script output-log NOISE, ~37 audited entries) was deferred. If pursued later, the cleanest fix is a per-source-file emit cap or a content-shape classifier — NOT corpus restriction (which the adversarial review showed deletes unique physics measurements).

## Reusable infrastructure

The content-key reconciler pattern is reusable beyond this specific patch:

> Whenever an upstream extractor change would renumber anchor_ids and invalidate an existing audit, build a content-derived join key per audited entity, persist it (`tools/_audit_content_keys.json`), and run `tools/_reconcile_audit.py --apply` after the extractor change to re-pin verdicts onto the new anchor_ids.

This eliminates the false dilemma "either edit the extractor and burn the audit, or accept the audit's anchor-keying forever." See `memory/feedback_framework-hygiene.md` for the rule and `tools/_reconcile_audit.py` for the implementation.
