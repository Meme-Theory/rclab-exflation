# Equations Table — Prose Pollution & Filter Effort Handoff

**Date**: 2026-05-18
**Status**: BLOCKED on extract_entities.py prose-extraction fix
**Reason for handoff**: Consumer-layer cleanup hits a structural ceiling that requires extractor surgery, but extractor surgery would invalidate the existing Haiku audit (anchor_ids are sequence-keyed). Resolution requires a new session with its own audit cycle.

---

## 1. What this session attempted

The audit at `tools/_anchor_validation_results.json` covers 10,919 entities with Haiku VALID/NOISE/UNSURE verdicts. The downstream task was to clean `tools/knowledge.db` by dropping the NOISE-flagged entries. Two filters were planned:

1. **NOISE filter** — drop entries Haiku flagged as NOISE.
2. **Atlas-source filter** — drop entries whose `source_file` is in `sessions/framework/Atlas/` (Atlas docs are synthesis, not derivation, per the project's structural model).

The consumer-layer architecture (`tools/_apply_validation_filter.py`) avoids editing `tools/extract_entities.py` because that would renumber sequential anchor_ids (`proven_N`, `closed_N`, etc.) and invalidate the audit's keying. See `memory/feedback_preserve-anchor-keyed-audits.md`.

### Filter dry-run result

| Table | Before | NOISE drop | Atlas drop | After | Drop % |
|:------|------:|------:|------:|------:|------:|
| theorems | 1,938 | 996 | 362 | 580 | 70.1% |
| closed_mechanisms | 266 | 26 | 180 | 60 | 77.4% |
| open_channels | 826 | 481 | 21 | 324 | 60.8% |
| gates | 2,791 | 293 | 0 | 2,498 | 10.5% |
| data_provenance | 2,428 | 186 | 0 | 2,242 | 7.7% |
| session_files | 1,835 | 4 | 0 | 1,831 | 0.2% |
| **equations** | **22,593** | **144** | **91** | **22,358** | **1.0%** |
| researchers | 32 | 2 | 0 | 30 | 6.2% |
| agents | 33 | 0 | 0 | 33 | 0.0% |
| registries | 144 | 4 | 13 | 127 | 11.8% |
| **TOTAL** | **32,886** | **2,136** | **667** | **30,083** | **8.5%** |

Equations is the outlier: 22,593 entries, only 500 audited (2.2% coverage). The filter drops only 235 of them. The remaining 22,358 are mostly unaudited.

---

## 2. Why equations is the blocker

The equations table contains **prose fragments masquerading as equations** because `tools/extract_entities.py` is over-extracting. Concrete examples from the Haiku-audited 500:

```
with envelope α_k = 2k - 1 (rank-cocycle order).
   ^^^^ starts with preposition "with" — clearly a mid-sentence fragment

pi_3(SU(3)) = Z (instantons/skyrmions). If the transition is mediated by instanton
                                       ^^ two sentences, second truncated mid-clause

absolutely for k = 0, 2, 4. The polynomial cutoff f_B(u) = (1+u)^{−2} is
^^^^^^^^^^ starts with adverb — paragraph slice; ends with auxiliary "is"

In d = n+1 spacetime dimensions (n spatial), the acoustic metric
^^^ starts with preposition "In" — paragraph fragment

with k_BCS the integrating-out scale for soft-gap fluctuations; T_K
^^^^ starts with preposition — fragment, ends with bare variable name

The N_eff statistic is defined as the number of independent  modes contributing to
^^^ starts with definite article — prose explanation, ends mid-clause
```

These entries are stored in the `equations` table with `name = <prose-fragment-text>` and a `raw` field containing the same. They each got an `eq_NNNNN` id and were dispatched to Haiku for audit. Haiku correctly identified many as NOISE; some it incorrectly marked VALID because the fragment contained a real equation token.

---

## 3. Root cause in `extract_entities.py`

Line 2683-2698 of `tools/extract_entities.py`:

```python
# --- Structural equations (code-block, plain-text, or Python code) ---
for m in RE_STRUCT_EQ.finditer(text):
    line = m.group(1).strip()
    if line.startswith('|') or line.startswith('#') or 'http' in line:
        continue
    if len(line) < 12:
        continue
    if not is_python:
        if not _has_math_content(line):
            continue
        words = line.split()
        if len(words) > 15:
            continue
```

**The filter accepts any line that**:
1. Has `_has_math_content` (contains `=`, math operators, etc.)
2. Is ≤15 words
3. Is ≥12 chars
4. Doesn't start with `|` (table row) or `#` (comment header) or contain `http`

**The filter does NOT check**:
- **Sentence start**: lines starting with prepositions/conjunctions (`with`, `for`, `in`, `at`, `to`, `from`, `and`, `but`, `also`, `because`, `however`, `absolutely`, `additionally`) are mid-sentence fragments
- **Sentence end**: lines ending with auxiliary verbs (`is`, `was`, `are`, `were`, `has`, `have`, `had`, `be`, `been`, `being`), prepositions, conjunctions, or articles are truncated mid-clause
- **Capital-start expectation**: real equations either start with a variable name (which may or may not be capitalized) OR with LaTeX delimiters (`$`, `\(`, `\[`). Prose can start lowercase or with English articles.
- **Multi-sentence containment**: lines containing `.` + uppercase + word characters are likely two sentences glued together

The result: when the regex matches a paragraph that contains an inline equation, the extractor grabs the surrounding 12+-char window as if it were the equation.

---

## 4. Why the classifier alone can't fix this

Built `tools/_equation_substance_classifier.py` (v6) — heuristic MATH/NOT_MATH classifier defaulting to MATH, with high-precision NOT_MATH patterns for YAML pins, gate-verdict-file lines, file paths, Python statements, dimensionality declarations, string-literal assignments, boolean assignments, value=STATUS embeds, and pure prose without any math symbol.

**Performance against the 500-equation Haiku audit**: 75.2% agreement, 2 false negatives, 122 false positives. Precision on drops: ~91.7% (and the 2 false negatives appear to be Haiku errors — `content_sha256 = <hash>` is unambiguously not math; Haiku labeled it VALID).

**Why this isn't enough**: many of the 122 "false positives" are prose fragments that genuinely contain a math token. By the classifier's default-MATH rule (which the user directed: "Python calls ARE math in this project"), they pass. But they shouldn't be in the equations table at all — they're prose paragraphs that the extractor wrongly captured.

The classifier can't distinguish "real equation extracted cleanly" from "real equation embedded in a captured prose paragraph". Both have math content. The clean fix is upstream: stop emitting prose fragments as equations.

---

## 5. What needs to happen next session

The next session needs to **fix `extract_entities.py::extract_equations`** to reject prose fragments at extraction time. Concrete checks to add at the structural-equation filter (line 2683+):

1. **Reject mid-sentence starts**: skip lines whose first token is a preposition / conjunction / article from a stopword set:
   ```python
   PROSE_FRAGMENT_STARTERS = {
       'with', 'for', 'in', 'at', 'to', 'from', 'on', 'by', 'of', 'as',
       'and', 'but', 'also', 'because', 'however', 'absolutely',
       'additionally', 'consequently', 'therefore', 'thus', 'hence',
       'moreover', 'furthermore', 'the', 'a', 'an', 'this', 'these',
       'those', 'it', 'its',
   }
   first_word = line.split()[0].lower() if line.split() else ''
   if first_word in PROSE_FRAGMENT_STARTERS:
       continue
   ```

2. **Reject truncated ends**: skip lines whose last token is an auxiliary verb / preposition / article, signaling mid-clause truncation:
   ```python
   PROSE_FRAGMENT_ENDERS = {
       'is', 'was', 'are', 'were', 'has', 'have', 'had', 'be', 'been',
       'being', 'will', 'would', 'could', 'should', 'must', 'may',
       'might', 'the', 'a', 'an', 'of', 'in', 'at', 'to', 'from', 'on',
       'by', 'with', 'as', 'for', 'and', 'or', 'but',
   }
   last_word = line.rstrip('.,;:').split()[-1].lower() if line.split() else ''
   if last_word in PROSE_FRAGMENT_ENDERS:
       continue
   ```

3. **Reject multi-sentence captures**: a line containing `. <Uppercase letter>` followed by word chars is two sentences glued together:
   ```python
   if re.search(r'[.!?]\s+[A-Z][a-z]', line):
       continue
   ```

4. **Require equation-shape start**: equation lines should start with a variable identifier or LaTeX delimiter; reject lines starting with English articles or sentence connectors. (Stricter version of #1.)

The audit-preservation rule (`memory/feedback_preserve-anchor-keyed-audits.md`) says editing `extract_entities.py` invalidates the existing Haiku audit because anchor_ids renumber. So this fix triggers a new audit cycle:

1. Apply the prose-rejection patches to `extract_entities.py`
2. Run `/weave --update` → new `knowledge-index.json` with cleaner equations table (estimate: 22,593 → ~10,000-15,000 after prose rejection)
3. Run `tools/_haiku_anchor_audit.py --table equations` → new equations batches
4. Dispatch Haiku across the new batches (wave-of-8 per existing protocol)
5. Aggregate → new `_anchor_validation_results.json`
6. Re-run the consumer-layer filter (`tools/_apply_validation_filter.py --apply`) against the new index + new audit

The classifier (`tools/_equation_substance_classifier.py`) may not be needed after the upstream fix because most NOISE will be filtered at extraction time, but it remains available as a backup for the remaining edge cases.

---

## 6. Constraints to respect in the next session

### 6.1 Audit-preservation rule

Don't edit `extract_entities.py` and re-run `/weave --update` against the EXISTING audit's anchor_ids — that breaks the keying. Either:
- (a) Make the extractor change AND immediately budget for a fresh audit cycle (the path described above)
- (b) Leave the extractor alone and accept the classifier ceiling

See `memory/feedback_preserve-anchor-keyed-audits.md` for the rule and rationale.

### 6.2 No Atlas docs as KB sources

Atlas docs (`sessions/framework/Atlas/*.md`) are synthesis artifacts, not derivation sources. The Atlas-source filter in `_apply_validation_filter.py` drops 667 entries from the existing index. When `extract_entities.py` gets surgery, also remove the explicit Atlas routes at lines 3798-3809:

```python
# DELETE:
(("permanent-results", "atlas-07"), ["theorems"]),
(("atlas-04", "assumptions"), ["theorems", "closed_mechanisms"]),
(("atlas-05", "walls-doors-windows"), ["theorems", "closed_mechanisms"]),
(("atlas-08", "open-questions"), ["open_channels"]),
(("atlas-09", "retractions"), ["closed_mechanisms"]),
(("atlas-10", "breakthrough-genealogy"), ["theorems"]),
```

Also remove the special atlas-02 parser dispatch at line 1143 (the `_extract_closed_from_atlas_02` function and the `if "atlas/atlas-02-mechanism-lifecycle" in path_str` check).

**Trade-off**: 644 Atlas-unique closures (`1-loop Coleman-Weinberg`, `Single-field slow-roll`, etc.) have no canonical session-source. Dropping Atlas extraction loses them. Either (i) migrate them to a dedicated `sessions/framework/registry/closures-eraN.md` registry first, then drop Atlas, or (ii) accept the loss.

### 6.3 Cross-table closure→theorem routing fix

`extract_entities.py:3805` routes `constraint-mega-matrix.md` to both `closed_mechanisms` AND `theorems` buckets. That causes ~60 closure events to be double-indexed (we identified 66 cross-table dup-name-groups in the audit). Fix: route by row-status: rows with status `CLOSED`/`PROVEN-FALSE`/`RETRACTED` go to `closed_mechanisms` only.

---

## 7. Artifacts created this session

### Filters / classifiers (consumer-layer)
- `tools/_apply_validation_filter.py` — dry-run + `--apply` for NOISE + Atlas filters. Currently validated; not yet committed via `--apply`.
- `tools/_equation_substance_classifier.py` — heuristic MATH/NOT_MATH (v6, 75.2% Haiku agreement, ~91.7% precision on drops).

### Audit / analysis
- `tools/_haiku_anchor_audit.py` — extended with REAL→VALID normalization at aggregate (`aggregate_results()`)
- `tools/_anchor_validation_results.json` — aggregate of 10,919 Haiku verdicts (8,733 VALID / 2,162 NOISE / 24 UNSURE)
- `tools/_anchor_validation_results_summary.json` — per-table tallies + parse errors + REAL→VALID drift counts
- `tools/_atlas_source_audit.py` — Atlas-source statistics per table (820 entries from Atlas docs; 644 have no canonical parent)
- `tools/_dupe_audit.py` + `_dupe_audit_results.json` — in-database duplication audit (0.3% within-table rate; 66 cross-table dup-name-groups)
- `tools/_noise_coverage_check.py` — loose-match coverage (does NOISE content exist elsewhere?)
- `tools/_noise_coverage_report.md` + `_seed43.md` — coverage reports for both spot-check samples
- `tools/_noise_spot_check.py` + `_noise_spot_check.md` + `_noise_spot_check_seed43.md` — 5% random samples of NOISE entries

### Eyeball lists (one per NOISE-bearing table)
- `tools/_noise_theorems_eyeball.md` (1020 entries)
- `tools/_noise_open_channels_eyeball.md` (481)
- `tools/_noise_gates_eyeball.md` (293)
- `tools/_noise_data_provenance_eyeball.md` (186)
- `tools/_noise_equations_eyeball.md` (144)
- `tools/_noise_closed_mechanisms_eyeball.md` (26)
- `tools/_noise_registries_eyeball.md` (4)
- `tools/_noise_session_files_eyeball.md` (4)
- `tools/_noise_researchers_eyeball.md` (2)
- `tools/_noise_constants_eyeball.md` (2)

### Documentation
- `tools/ANCHOR_VALIDATION_STATUS.md` — extended with Phase 2 closeout section
- `tools/_noise_spot_check_manual.md` — Claude's manual review of the 123 spot-check entries (~92% Haiku-correct per close reading)
- `memory/feedback_preserve-anchor-keyed-audits.md` — rule against destroying audits via upstream extractor changes
- This file (`tools/EQUATIONS_PROSE_POLLUTION_HANDOFF.md`)

---

## 8. Decisions that need user input next session

1. **Atlas extraction policy**: drop Atlas as extraction source (option B in user's directive) requires first migrating the 644 Atlas-unique closures to canonical registry files, OR accepting the loss. Which?
2. **Equations audit re-scope**: after the prose-extraction fix, the equations table should shrink dramatically (rough estimate: 22,593 → 10,000-15,000). Should the next audit cycle re-audit equations from scratch, or just the new entries that didn't exist before?
3. **Cross-table closure routing fix**: simple to implement at the `_extractor_routes_filter()` site. Apply at same time as Atlas removal?
4. **What constitutes "Math" for the equations table** — the user clarified during this session: math includes named numerical pins, gate-computed values, prose-with-symbols, function calls (Python is math here). The classifier reflects that. If the rubric changes, the classifier patterns need updating.

---

## 9. Quick-start for the next session

```bash
# 1. Confirm starting state
cat tools/ANCHOR_VALIDATION_STATUS.md   # current audit state
cat tools/EQUATIONS_PROSE_POLLUTION_HANDOFF.md  # this file

# 2. Patch the extractor (see §5 for specific patches)
$EDITOR tools/extract_entities.py
#   - Lines 2683+: add prose-fragment rejection
#   - Lines 3798-3809: remove Atlas routes
#   - Line 1143: remove atlas-02 special dispatch
#   - Line 3805: split constraint-mega-matrix routing by row-status

# 3. Re-run extraction
/weave --update

# 4. Re-run audit on equations (and any other table where extraction
#    materially changed)
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/_haiku_anchor_audit.py --table equations
# Then dispatch wave-of-8 Haikus per tracker protocol

# 5. Aggregate
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/_haiku_anchor_audit.py --aggregate

# 6. Apply consumer-layer filter
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/_apply_validation_filter.py --apply

# 7. Confirm new state
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/_dupe_audit.py
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/_atlas_source_audit.py
```
