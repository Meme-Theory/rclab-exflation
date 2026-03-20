# Handoff: Knowledge Index Extractor Overhaul

**Date**: 2026-02-21
**Branch**: `Valar-1`
**Session context**: Equation audit application + extractor gap analysis + format generation cataloging
**Status**: Planning complete, all 11 tasks defined, zero tasks started

---

## 1. What Was Accomplished This Session

### 1a. Equation Audit Applied (DONE)

Script `tools/apply_audit_results.py` was written and executed. It applied results from a prior gen-physicist + knowledge-weaver equation audit:

- **207 equations** received `latex` fields (proper LaTeX formatting)
- **251 equations** received `audit_status` fields (`ok`/`error`/`typo`)
- **46 equations** reclassified: 40 `structural` → `code`, 6 `structural` → `comment`
- **All verified**: spot-checks pass, diff confirms only expected fields changed

The script is idempotent and reusable — it reads `tools/equation-audit-results.json` and patches `tools/knowledge-index.json`.

**Important**: After any full index rebuild (`extract_entities.py`), the audit results must be re-applied since rebuild overwrites the JSON:
```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/apply_audit_results.py
```

### 1b. Extractor Fence-Tracking Patch (DONE)

`tools/extract_entities.py` was patched at line ~1167 to track fenced code blocks in `.md` files. Lines inside ```` ```python ``` ```` blocks now get `type="code"` instead of `type="structural"`. This prevents the systemic misclassification bug found by the audit.

The patch adds ~19 lines: a pre-pass that builds a `set[int]` of line numbers inside fenced code blocks with known language tags (python, bash, shell, js, json), then a check in the structural equation loop that assigns `eq_type = "code"` for lines in that set.

### 1c. Knowledge-Weaver Deep Audit (DONE)

A knowledge-weaver agent ran a comprehensive structural audit of `knowledge-index.json`. Key findings:

- **Grade F**: 5 most recent closes (Sessions 23a, 24a) completely absent from `closed_mechanisms`
- **Grade D**: 9/10 gate cross-references broken (closed mechanisms reference gates that don't exist in the gates array); 12 duplicate theorem pairs; 3 garbage theorem entries
- **Grade C**: 4 Giants sessions missing; 58% of tier0 scripts untracked in provenance; 22 probability trajectory entries with empty sessions

### 1d. Format Generations Cataloged (DONE)

Three exploration agents scanned all 80+ files in `sessions/` and `tier0-computation/`. Results written to `tools/format-generations.md` — a 450-line reference document cataloging every header pattern, content format, gate ID vocabulary, and verdict keyword across 8 formatting generations.

---

## 2. What Needs to Be Done (11 Tasks)

### Task Dependency Graph

```
Tasks 1-8 (independent, can parallelize)
    │
    ├─→ Task 9 (blocked by 1, 2 — verify recent closes extracted)
    │
    └─→ Task 11 (blocked by ALL — full rebuild + validate)

Task 10 (independent — researcher domain fix)
```

---

### Task 1: Fix RE_CLOSED_SECTION regex

**File**: `tools/extract_entities.py` line 272
**Current regex**:
```python
RE_CLOSED_SECTION = re.compile(
    r"###?\s*(?:CLOSED|Closed|Perturbative Gates|Constraint Gate Registry|Constraint Registry|Definitive Closure).*?\n"
    r"((?:.*?\n)*?)"
    r"(?=\n###?\s|\n---|\Z)",
    re.IGNORECASE,
)
```

**What it misses** (from `tools/format-generations.md` Section 1):
- `## II. Constraint Gate Verdicts` (23a) — "Constraint Gate Verdicts" without "Registry"
- `### II.5 Constraint Registry: 18 Closed Mechanism, 8:1 Closure-to-pass ratio` (24b) — Roman prefix + colon + stats
- `### III.1 Complete Closure Registry (17 Mechanisms Closed)` (23b) — "Complete Closure Registry"
- `### III.1 Closed Mechanism: Complete Registry` (23-sagan) — "Closed Mechanism:"
- `### VI.1 Complete Closure Table` (24-sagan) — "Complete Closure Table"
- `## VI. UPDATED Constraint Registry` (24-sagan) — "UPDATED Constraint Registry"
- `## Constraint Condition Assessment` (18) — "Constraint Condition"
- `### What is NOT closed` / `### What is NOT closed` (18)
- `### The Scenario Constraint Chain` (23c) — "Scenario Constraint Chain"
- `### Perturbative Mechanisms (all sessions) — ALL CLOSED` (22-master) — "ALL CLOSED" without leading "CLOSED"

**Fix approach**: Replace the alternation group with a broader pattern. The regex needs to match any H2-H4 header containing any of: `CLOSED`, `Closed`, `Closure`, `CLOSED`, `Closed`, `Registry`, `Constraint Table`, `Constraint Chain`, `What is NOT closed`, `Constraint Condition`, `ALL CLOSED`, `Closed Mechanism`, `Closed End`. Something like:

```python
RE_CLOSED_SECTION = re.compile(
    r"^#{2,4}\s*(?:[IVXLC]+\.?\d*\s+)?"  # optional Roman numeral prefix
    r"(?:[^#\n]*?"                          # anything before the keyword
    r"(?:CLOSED|Closure(?:ed)?(?:\s+(?:Gate|Condition|Registry|Table|Chain))?|Closed\s+Mechanism|What\s+is\s+closed|ALL\s+CLOSED)"
    r")[^#\n]*\n"                           # rest of header line
    r"((?:.*?\n)*?)"                        # captured body
    r"(?=\n#{2,4}\s|\n---|\n={5,}|\Z)",     # lookahead terminator
    re.IGNORECASE | re.MULTILINE,
)
```

**Also needed**: A **Strategy 3** in `extract_closed_mechanisms()` for narrative gate headers that encode closes directly in the H3 header text, like `### II.2 K-1e: Gap Equation Trivial at mu = 0 — DECISIVE CLOSURE`. These aren't table rows or bullets — they're self-contained closure declarations in the header itself. Parse with:

```python
RE_NARRATIVE_CLOSURE_HEADER = re.compile(
    r"^#{2,4}\s+(?:[IVXLC]+\.\d+\s+)?([A-Z][\w-]*(?:-\d+[a-z]?)?):\s+(.+?)\s+[—–-]+\s+(DECISIVE CLOSURE|STRUCTURAL CLOSURE| CLOSED |FATAL)",
    re.MULTILINE | re.IGNORECASE,
)
```

---

### Task 2: Fix RE_GATE_SECTION regex

**File**: `tools/extract_entities.py` line 404
**Current regex** (paraphrased alternation): `Gate Table | Constraint Gate | Nominal Constraint Gate | Definitive Constraint Gate Registry | PRE-REGISTERED CONSTRAINT | Non-Perturbative Gates | Perturbative Gates | Constraint Gate Verdicts | PB-\d+ and PB-\d+ Gate | Complete Closure Gate | D-\d+ Gate | PRE-REGISTERED CONSTRAINT`

**What it misses** (from `tools/format-generations.md` Section 2):
- Simple `## I. Gate Table` (24a) — "I. " Roman prefix before "Gate Table"
- `## I. Gate Table (24a Results with Sagan Adjudication)` (24b) — parenthetical after
- `## V. Constraint Gate Registry (Updated)` (23b) — "(Updated)" suffix
- `### VI.2 Pre-Registered Gate Tally (Updated)` (24-sagan) — "Gate Tally"
- `### I.1 Gate-by-Gate Verification` (24-sagan) — "Gate-by-Gate"
- `## Gate Status Summary` (17b) — "Gate Status"
- `### Gate Verdicts` (17b) — simple "Gate Verdicts" without "Closure" prefix
- `.txt` section headers: `PART N: PRE-REGISTERED GATE VERDICTS`, `N. Constraint Gate VERDICTS`

**Fix approach**: The regex prefix `(?:I+\.?\d?\s+)?` only matches `I.1` or `II.2` — it doesn't match `VI.`, `VIII.`, `IX.3`. Replace with a proper Roman numeral pattern:

```python
r"^#{2,4}\s*(?:[IVXLC]+\.?\d*\s+)?"  # optional Roman prefix like "II.5 " or "VI.1 "
```

And expand the alternation to include: `Gate\s+Table`, `Gate\s+Status`, `Gate\s+Verdict`, `Gate\s+Tally`, `Gate-by-Gate`, `Closure\s+Gate`, `Closure\s+Table`, `Closure\s+Registry`, `UPDATED\s+CLOSED`, `Complete\s+Closure`, `PRE-REGISTERED`.

**Also needed**: Add Format B parsing for `.txt` inline verdicts. Currently `extract_gates()` Strategy 2 only handles `^GATE [ID]:` blocks. Add a Strategy 3 for:
- `GATE VERDICT: COMPELLING (BF=8)` — standalone line
- `VERDICT: PASS` — standalone line
- `N. Constraint Gate VERDICTS` — section headers in .txt files

---

### Task 3: Fix RE_PROVEN_SECTION regex

**File**: `tools/extract_entities.py` line 174
**Current regex**: `###?\s*(?:PROVEN|Structural Theorems|Permanent|Category A).*?\n`

**What it misses**:
- `## WHAT SURVIVES (CONFIRMED AT MACHINE EPSILON)` (10, 11)
- `# VI. WHAT WE PROVED (11 Results at Machine Epsilon)` (16-final) — H1 not matched by `###?`
- `## X. STRUCTURAL THEOREMS (New, Proven This Session)` (22b)
- `## VIII. NEW STRUCTURAL THEOREMS (Permanent)` (22c) — "NEW STRUCTURAL"
- `## III. STRUCTURAL RESULTS (Non-Gate, Session-Permanent)` (22a) — "STRUCTURAL RESULTS"
- `## III. Structural Findings (Permanent, Independent of Closure)` (23a) — "Structural Findings"
- `### III.2 Permanent Mathematical Achievements` (23b) — "Permanent Mathematical"
- `### III.1 E-6: Permanent Results -- Publishable` (24b) — "Permanent Results"
- `### Clean Results (Machine Epsilon Precision)` (8) — "Clean Results"
- `## III. PROVEN (Machine Epsilon or Exact)` (17-final) — should match but verify Roman prefix

**Fix approach**: Expand to `#{1,4}` (catch H1 headers too). Add alternation terms: `WHAT (WE )?PROVED`, `WHAT SURVIVES`, `Structural (Theorems|Results|Findings)`, `Permanent (Mathematical|Results)?`, `Machine Epsilon`, `Clean Results`. Allow optional Roman numeral prefix.

**Also fix `dedup_by_name()`** (Task 7 overlap): Remove garbage entries where `name` starts with `|`, `:--`, or is shorter than 3 chars. Add filter in the proven extraction itself:
```python
if name.startswith(":") or name.startswith("|") or len(name) < 3:
    continue
```

---

### Task 4: Fix RE_OPEN_SECTION regex

**File**: `tools/extract_entities.py` line 956
**Current regex**: `###?\s*(?:OPEN|Open Channels?|Remaining|Rescue|Surviving|P2[ab]).*?\n`

**What it misses**:
- `## VII. Escape Routes` (23a) — "Escape Routes"
- `## VIII. What Survives` (23a) — "What Survives"
- `### IV.5 P2a/P2b Status` (24b) — "P2a/P2b" (slash not matched by `P2[ab]`)
- `## V. B-4: OFF-DIAGONAL COUPLING ESCAPE ROUTE` (21b) — "ESCAPE ROUTE"
- `### III.2 E-7: Surviving Claim Set` (24b) — "Surviving Claim"
- `## WHAT'S OPEN` (10, 11) — "WHAT'S OPEN"
- `## III. Non-Perturbative Physics — What Survives` (22-master) — "What Survives" embedded

**Fix approach**: Add: `Escape\s+Route`, `What\s+Survives`, `What'?s\s+Open`, `P2[ab]/P2[ab]`, `Surviving\s+Claim`, `Post-Mortem`. Allow Roman numeral prefix.

---

### Task 5: Fix probability trajectory extraction

**File**: `tools/extract_entities.py` lines 610-775

The extractor handles code-block trajectories (Format 1 from format-generations.md Section 5) and some table formats. Missing:

- **Format 2**: Per-agent probability tables under headers like `## Per-Agent Estimates`, `## VII. Per-Agent Probability Assessments`, `## IX. PROBABILITY TABLE`
- **Format 3**: Bayesian log-odds code blocks under `## II. DEFINITIVE S-2: Full Bayes Factor Update`, `## VII. POSTERIOR COMPUTATION`
- **Format 4**: Pre-registered outcome tables under `## V. Pre-Registered Probability Update`
- **Format 5**: Adopted posterior tables under `### VII.3 Adopted Posteriors`
- **Format 6**: Simple prose updates under `## PROBABILITY ESTIMATES`, `## REVISED PROBABILITY ESTIMATES`, `## Framework Probability Update`, etc.

**Fix approach**: Add new section header patterns to the probability extraction regexes. The most important missing data is the adopted posteriors — these are the canonical probability values. Focus on headers containing: `Probability`, `Posterior`, `Bayes Factor`, `Framework Probability`, `Probability Estimate`, `Probability Update`, `Probability Assessment`, `Probability Trajectory`.

**Also**: Fix the 22 empty-session entries by extracting session from the filename when context-based extraction fails.

---

### Task 6: Expand collect_files() to scan tier0 .txt files

**File**: `tools/extract_entities.py` line 1441-1458

**Current**: Only grabs `*_gate_verdicts.txt` from tier0:
```python
if TIER0_DIR.exists():
    for f in TIER0_DIR.iterdir():
        if f.name.endswith("_gate_verdicts.txt"):
            files.append(f)
```

**Change to**: Grab ALL `.txt` files from tier0:
```python
if TIER0_DIR.exists():
    for f in TIER0_DIR.iterdir():
        if f.suffix == ".txt":
            files.append(f)
```

This picks up gate verdicts from `s22c_bcs_channel_scan.txt`, `s22c_instanton_action.txt`, `s22c_landau_classification.txt`, `s22a_fano.txt`, `s21c_gauss_bonnet.txt`, `s21c_T_double_prime_result.txt`, `s22a_euclidean_action.txt`, `s23a_gap_equation_results.txt`.

**Also**: Add priority 3 for these .txt files (same as gate_verdicts.txt) or priority 2 (below synthesis but above regular minutes).

---

### Task 7: Fix dedup_by_name()

**File**: `tools/extract_entities.py` line 1320-1332

**Current**:
```python
def dedup_by_name(entities: list[dict], key: str = "name") -> list[dict]:
    seen: dict[str, int] = {}
    for i, ent in enumerate(entities):
        norm = ent.get(key, "").strip().lower()
        norm_short = norm[:60]
        seen[norm_short] = i
    indices = sorted(seen.values())
    return [entities[i] for i in indices]
```

**Problem**: 60-char truncation + exact match causes:
- `"ko-dim = 6"` and `"ko-dim = 6, parameter-free"` both survive (different strings)
- Unicode `τ` and ASCII `tau` don't match
- `"all 14 perturbative spectral mechanisms"` and `"ALL perturbative spectral mechanisms"` both survive (different after lowering due to "14" vs no number)

**Fix approach**:
1. Add Unicode normalization: replace τ→tau, σ→sigma, φ→phi, ψ→psi, λ→lambda, α→alpha, β→beta, γ→gamma, Δ→Delta, π→pi, ≡→=, ≈→~
2. Strip markdown artifacts: `**`, `` ` ``, `|`
3. Remove parenthetical suffixes: `(parameter-free)`, `(Permanent)`, etc.
4. Strip numbers that aren't part of IDs: "14 perturbative" → "perturbative", but keep "K-1e"
5. If normalized name A is a PREFIX of normalized name B, they're the same entity — keep B

```python
import unicodedata

UNICODE_MAP = str.maketrans({
    'τ': 'tau', 'σ': 'sigma', 'φ': 'phi', 'ψ': 'psi',
    'λ': 'lambda', 'α': 'alpha', 'β': 'beta', 'γ': 'gamma',
    'Δ': 'Delta', 'π': 'pi', '≡': '=', '≈': '~',
})

def _normalize_for_dedup(name: str) -> str:
    n = name.strip().lower()
    # Unicode → ASCII
    for old, new in UNICODE_MAP.items():  # use items for multi-char
        n = n.replace(old, new)
    # Strip markdown
    n = re.sub(r'[*`|]', '', n)
    # Strip parenthetical suffixes
    n = re.sub(r'\s*\([^)]*\)\s*$', '', n)
    # Collapse whitespace
    n = re.sub(r'\s+', ' ', n).strip()
    return n[:80]
```

Then use substring matching: if `norm_a` starts with `norm_b` or vice versa, treat as duplicate.

---

### Task 8: Fix extract_session_from_context() for .txt filenames

**File**: `tools/extract_entities.py` line 592

**Bug**: For `s24a_gate_verdicts.txt`, the function searches for session IDs in the surrounding text. Since there's no `# Session 24a` header in the .txt file, it picks up numbers from gate condition text like `[17, 66]` → session "66".

**Fix**: Check filename first before falling back to context search:
```python
def extract_session_from_context(filepath: Path, text: str, pos: int) -> str:
    # Strategy 0: Extract from tier0 filename prefix (s24a_... → "24a")
    fname = filepath.name
    m = re.match(r'^s(\d+[a-z]?)_', fname)
    if m:
        return m.group(1)

    # ... existing strategies ...
```

---

### Task 9: Verify Sessions 23a/24a/24b closed mechanisms extracted

**Blocked by**: Tasks 1, 2

After regex fixes, run the extractor on the specific synthesis files and verify these 5 closes appear:

1. **Kosmann-BCS condensate at mu=0** (K-1e, Session 23a) — from `### II.2 K-1e: Gap Equation Trivial at mu = 0 — DECISIVE CLOSURE` in `session-23a-synthesis.md`, or from the numbered table in `session-23b-synthesis.md` / `session-24b-synthesis.md`
2. **Gap-edge self-coupling V(gap,gap)=0** (Session 23a) — from `### III.1 Gap-Edge Self-Coupling Selection Rule` in `session-23a-synthesis.md`
3. **V_spec(tau;rho) monotone** (V-1, Session 24a) — from gate table in `session-24a-synthesis.md` or numbered Constraint Registry in `session-24b-synthesis.md`
4. **Neutrino R from H_eff** (R-1, Session 24a) — from gate table
5. **Eigenvalue ratio phi in singlet** (Session 24a) — from `session-24a-synthesis.md`

Test command:
```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" -c "
from tools.extract_entities import extract_closed_mechanisms
from pathlib import Path
f = Path('sessions/archive/session-24/session-24b-synthesis.md').resolve()
closed = extract_closed_mechanisms(f, f.read_text(encoding='utf-8'))
for d in closed:
    print(d['name'][:80])
print(f'Total: {len(closed)}')
"
```

---

### Task 10: Add Little-Red-Dots researcher + fix Berry count

**File**: `tools/extract_entities.py` function `extract_researcher_index()` at line 873

The function walks `researchers/` subdirectories. `Little-Red-Dots/` has 15 `.md` papers but may not be picked up if the function filters by a naming convention.

Verify by running:
```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" -c "
from tools.extract_entities import extract_researcher_index
from pathlib import Path
researchers = extract_researcher_index(Path('researchers'))
for r in researchers:
    print(f'{r[\"domain\"]}: {r[\"paper_count\"]} papers')
"
```

If Little-Red-Dots is missing, check whether the directory naming convention (`-` vs spaces, capitalization) causes the miss. For Berry, count papers on disk: `ls researchers/Berry/*.md | wc -l` and compare to index value.

---

### Task 11: Full rebuild + validate + re-apply audit

**Blocked by**: ALL other tasks

Execute in sequence:
```bash
# 1. Full rebuild
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py

# 2. Validate
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py --validate

# 3. Stats
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py --stats

# 4. Re-apply equation audit (rebuild overwrites the JSON)
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/apply_audit_results.py
```

**Verification checklist**:
- [ ] Closed Mechanism includes K-1e, gap-edge, V_spec, neutrino R, phi singlet
- [ ] Closed Mechanism count ≥ 23 (was 29 with dupes; should be ~23-28 after dedup + additions)
- [ ] Gates includes K-0, K-1e from 23a + historical gates SP-4, D-1, SD-1, L-3, PB-2, PB-3, C-1, E-3
- [ ] Gate sessions are correct (no "66", "0", "10" artifacts from condition text)
- [ ] Theorems have no duplicates (was 40, should be ~20-22 after dedup)
- [ ] No garbage theorems (no ":--------", no "| Trap 3")
- [ ] Open channels have no duplicates (was 24, should be ~10-12)
- [ ] Researchers includes Little-Red-Dots (15 papers)
- [ ] Berry paper count matches disk
- [ ] Probability trajectory has no empty session fields
- [ ] Equations still have latex and audit_status fields (from re-applied audit)
- [ ] 207 equations with latex, 251 with audit_status, 46 reclassified types preserved

---

## 3. Architecture Notes

### File Map

```
tools/
├── extract_entities.py          # THE file being overhauled (1600+ lines)
│   ├── Lines 56-89:             # Session metadata regexes
│   ├── Lines 174-199:           # RE_PROVEN_SECTION + helpers (Task 3)
│   ├── Lines 272-285:           # RE_CLOSED_SECTION + RE_GATE_ID (Task 1)
│   ├── Lines 396-425:           # RE_GATE_SECTION + RE_GATE_TABLE_ROW (Task 2)
│   ├── Lines 438-589:           # extract_gates() function (Tasks 2, 8)
│   ├── Lines 592-631:           # extract_session_from_context() (Task 8)
│   ├── Lines 610-775:           # Probability trajectory extraction (Task 5)
│   ├── Lines 956-970:           # RE_OPEN_SECTION + helpers (Task 4)
│   ├── Lines 1167-1184:         # Fenced code block pre-pass (DONE)
│   ├── Lines 1320-1332:         # dedup_by_name() (Task 7)
│   ├── Lines 1441-1458:         # collect_files() (Task 6)
│   └── Lines 1461-1589:         # build_index() main pipeline
│
├── knowledge-index.json         # Output (~124K lines, single source of truth)
├── apply_audit_results.py       # NEW: applies LaTeX + audit_status + reclassifications
├── equation-audit-results.json  # Audit data (207 LaTeX, 251 statuses)
├── equation-audit-findings.md   # Audit narrative report
├── format-generations.md        # NEW: 450-line format inventory (reference for regex work)
└── HANDOFF-extractor-overhaul.md # THIS FILE
```

### Key Design Principles

1. **Authority ordering**: Files processed low-priority first, high-priority last. Dedup keeps last occurrence. Priority: sagan-verdict (5) > synthesis (4) > gate_verdicts.txt (3) > other .md (2) > default (1)
2. **Single source of truth**: `knowledge-index.json` is canonical. SQLite (`knowledge.db`) is a query accelerator rebuilt via `/weave --db-sync`
3. **Idempotent rebuilds**: `extract_entities.py` does a full rebuild from source files every time. The `apply_audit_results.py` script patches the rebuilt JSON with audit data
4. **Equations are special**: They come from ALL file types (sessions .md, tier0 .py, artifacts .md) and have their own dedup logic (`dedup_equations()`)

### Gotchas

- **Regex section terminators**: Most regexes use `(?=\n###?\s|\n---|\Z)` as the end-of-section lookahead. This breaks when H2 headers (`##`) are used for subsections within a captured section — the terminator matches H2 inside the body and truncates capture. The fix is to use `#{2,4}` in terminators, matching the same heading level range as the opener
- **The `is_python` fence bug**: FIXED this session. Lines inside ```` ```python ``` ```` blocks in .md files were classified as `structural`. Now they get `code`
- **`(x or "").strip()`**: JSON null → Python None. `dict.get("key", "")` returns `""` only when key is missing, not when value is `null`. Use `(x or "")` pattern
- **Path resolution**: `extract_equations()` uses `filepath.relative_to(PROJECT_ROOT)` — the filepath MUST be absolute/resolved, not relative. Test scripts must use `.resolve()` on paths

---

## 4. Recovery Action Plan

### Step 1: Read Reference Docs
- Read `tools/format-generations.md` — the complete format inventory
- Read this handoff file
- Skim `tools/equation-audit-findings.md` for context on the audit

### Step 2: Execute Tasks 1-8 in Parallel
Tasks 1-8 are all independent edits to `tools/extract_entities.py`. They can be done in any order or parallelized across agents. Each task modifies a different line range:
- Task 1: line ~272 (RE_CLOSED_SECTION) + new Strategy 3 in extract_closed_mechanisms()
- Task 2: line ~404 (RE_GATE_SECTION) + new Strategy 3 in extract_gates()
- Task 3: line ~174 (RE_PROVEN_SECTION) + garbage filter
- Task 4: line ~956 (RE_OPEN_SECTION)
- Task 5: line ~610 (probability trajectory regexes)
- Task 6: line ~1441 (collect_files)
- Task 7: line ~1320 (dedup_by_name)
- Task 8: line ~592 (extract_session_from_context)

### Step 3: Test Individual Extractors
After each regex fix, test on a known-bad file:
```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" -c "
from tools.extract_entities import extract_closed_mechanisms  # or whichever
from pathlib import Path
f = Path('sessions/archive/session-24/session-24b-synthesis.md').resolve()
results = extract_closed_mechanisms(f, f.read_text(encoding='utf-8'))
for r in results:
    print(r)
"
```

### Step 4: Task 9 — Verify Recent Closes
Run extraction on 23a, 23b, 24a, 24b synthesis files. Confirm 5 missing closes appear.

### Step 5: Task 10 — Researcher Fix
Quick check: does rebuild pick up Little-Red-Dots? Fix if not.

### Step 6: Task 11 — Full Rebuild
```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py --validate
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py --stats
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/apply_audit_results.py
```

### Step 7: Commit
All changes are on branch `Valar-1`. Uncommitted files include the new scripts (`apply_audit_results.py`, `format-generations.md`) and the modified extractor + index.
