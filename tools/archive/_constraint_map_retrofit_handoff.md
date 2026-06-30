# Constraint-Map Retrofit — Handoff

## 1. The Prompt

Use `gen-physicist` (default Opus). Substitute `{SESSION_ID}` (e.g., `S37`) and `{WP_ABSOLUTE_PATH}` per session.

```
TASK: Add a `## Constraint-Map Updates` section to:
  {WP_ABSOLUTE_PATH}

═══════════════════════════════════════════════════════════════════════
PURE EDITORIAL TRANSCRIPTION. NO PHYSICS. NO MATH.
═══════════════════════════════════════════════════════════════════════

SOURCE: ONLY the WP file above. Read it (paginate if > 30KB); the WP
body already contains the session's closures inside its Wave / Gate /
Synthesis sections.

DO NOT read any other file. DO NOT Glob. DO NOT search `summary/`,
`sessions/framework/`, atlas docs, synthesis docs in the same directory,
or anywhere else. The closures are inside this one WP already.

DO NOT do ANY of:
- DO NOT run any script, Bash, Python, or computation
- DO NOT use any tool other than Read and Edit
- DO NOT use TaskCreate, TaskUpdate, or any task tool
- DO NOT re-verify, re-derive, re-prove, or audit any closure claim
- DO NOT do MATH of any kind
- DO NOT consult external papers, knowledge MCP, or other sessions
- DO NOT paraphrase, "clarify," or improve the source wording
- DO NOT add commentary, footnotes, qualifiers
- DO NOT question whether the closure is correct
- DO NOT spawn sub-agents
- DO NOT update memory or write any other files
- DO NOT add summary statistics or totals

YOU MUST:
1. Read the WP (paginate via offset/limit if file > 30KB)
2. Scan body for closure markers: CLOSED, LANDED, PINNED, REGISTERED, PROMOTED
3. For EACH closure, add EXACTLY ONE row to a new section appended to the WP

CANONICAL SCHEMA (exact, do not add/remove columns):

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| {SESSION_ID} | <gate-id-or-mechanism-name as written in WP> | OPEN | **CLOSED** | <one-sentence excerpt from WP> |

CELL RULES:
- Date: explicit date if in WP, else "{SESSION_ID}"
- Mechanism/gate: AS WRITTEN in WP — no rewording
- Prior state: "OPEN" if unspecified
- New state: bolded marker **CLOSED** / **LANDED** / **PINNED** / **REGISTERED** / **PROMOTED**
- Reason: ONE sentence VERBATIM or near-verbatim from WP. Do not synthesize.

If multiple markers for same mechanism: use strongest (PROMOTED > REGISTERED > LANDED > PINNED > CLOSED).

Append BEFORE `## Files Produced` if exists; else at end of file.

UNCERTAIN LANGUAGE PRESERVATION: hedged wording → include AS-IS. Do not adjudicate.

NO CLOSURES CASE: add empty table (header+separator only), report "Section added with 0 rows — no documented closures found", terminate.

WHEN DONE: report exactly:
  "Section added to <filename> with N rows. Marker breakdown: CLOSED=x LANDED=y PINNED=z REGISTERED=w PROMOTED=v"

═══════════════════════════════════════════════════════════════════════
DO NOT MATH. DO NOT VALIDATE. DO NOT QUESTION. JUST TRANSCRIBE.
═══════════════════════════════════════════════════════════════════════
```

## 2. The Session List

### Done (8 sessions, 138 rows)

| Session | WP Path | Rows | Markers |
|:--------|:--------|---:|:--------|
| S46 | `sessions/archive/session-46/session-46-results-workingpaper.md` | 9 | CLOSED=9 |
| S51 | `sessions/archive/session-51/session-51-results-workingpaper.md` | 10 | CLOSED=3, PROMOTED=7 |
| S52 | `sessions/session-52/session-52-results-workingpaper.md` | 1 | CLOSED=1 |
| S58 | `sessions/session-58/session-58-results-workingpaper.md` | 2 | CLOSED=2 |
| S66 | `sessions/session-66/session-66-results-workingpaper.md` | 8 | CLOSED=1, PROMOTED=7 |
| S67 | `sessions/session-67/session-67-results-workingpaper.md` | 39 | CLOSED=33, REGISTERED=6 |
| S78 | `sessions/session-78/session-78-results-workingpaper.md` | 29 | CLOSED=26, REGISTERED=3 |
| S82 | `sessions/session-82/session-82-results-workingpaper.md` | 40 | LANDED=34, PINNED=1, REGISTERED=2, PROMOTED=3 |

### Remaining WP_NO_CMAP (22 sessions — WP exists, add the section)

| Session | WP Path |
|:--------|:--------|
| S37 | `sessions/archive/session-37/session-37-results-workingpaper.md` |
| S41 | `sessions/archive/session-41/session-41-results-workingpaper.md` |
| S42 | `sessions/archive/session-42/session-42-results-workingpaper.md` |
| S45 | `sessions/archive/session-45/session-45-results-workingpaper.md` |
| S47 | `sessions/archive/session-47/session-47-wave1-workingpaper.md` |
| S48 | `sessions/archive/session-48/session-48-results-workingpaper.md` |
| S49 | `sessions/archive/session-49/session-49-results-workingpaper.md` |
| S50 | `sessions/archive/session-50/session-50-results-workingpaper.md` |
| S54 | `sessions/session-54/session-54-results-workingpaper.md` |
| S55 | `sessions/session-55/session-55-results-workingpaper.md` |
| S56 | `sessions/session-56/session-56-results-workingpaper.md` |
| S57 | `sessions/session-57/session-57-results-workingpaper.md` |
| S59 | `sessions/session-59/session-59-results-workingpaper.md` |
| S64 | `sessions/session-64/session-64-results-workingpaper.md` |
| S65 | `sessions/session-65/session-65-results-workingpaper.md` |
| S69 | `sessions/session-69/session-69-results-workingpaper.md` |
| S71 | `sessions/session-71/session-71-results-workingpaper.md` |
| S72 | `sessions/session-72/session-72-results-workingpaper.md` |
| S73a | `sessions/session-73a/session-73a-results-workingpaper.md` |
| S73b | `sessions/session-73b/session-73b-results-workingpaper.md` |
| S80 | `sessions/session-80/session-80-results-workingpaper.md` |
| S81 | `sessions/session-81/session-81-results-workingpaper.md` |

### Remaining NO_WP S19-S34 (16 sessions — no WP exists; create new WP from synthesis docs)

These need a different prompt (source = synthesis file, create new WP). Synthesis docs per session:

| Session | Directory | Canonical Synthesis Source |
|:--------|:----------|:---------------------------|
| S19 | `sessions/archive/session-19/` | `session-19d-synthesis.md` |
| S20 | `sessions/archive/session-20/` | `session-20c-synthesis.md` |
| S21 | `sessions/archive/session-21/` | `session-21c-phase0-synthesis.md` |
| S22 | `sessions/archive/session-22/` | `session-22-master-synthesis.md` |
| S23 | `sessions/archive/session-23/` | `session-23c-synthesis.md` (no master) |
| S24 | `sessions/archive/session-24/` | `session-24b-synthesis.md` (no master) |
| S25 | `sessions/archive/session-25/` | (no synthesis; check session-25-Investigation-Closing.md) |
| S26 | `sessions/archive/session-26/` | (no synthesis; investigate) |
| S27 | `sessions/archive/session-27/` | (no synthesis; investigate) |
| S28 | `sessions/archive/session-28/` | `session-28-fusion-synthesis.md` |
| S29 | `sessions/archive/session-29/` | `session-29-fusion-synthesis.md` |
| S30 | `sessions/archive/session-30/` | `session-30-master-synthesis.md` |
| S31 | `sessions/archive/session-31/` | (no master; pick latest letter+number) |
| S32 | `sessions/archive/session-32/` | `session-32-master-synthesis.md` |
| S33 | `sessions/archive/session-33/` | `session-33b-synthesis.md` (no master) |
| S34 | `sessions/archive/session-34/` | `session-34-master-synthesis.md` |

### Out of scope (do not retrofit)

- S01-S18 (17 sessions): no synthesis docs exist, pre-convention
- S79: explicitly omitted ("one off")

## 3. Handoff

### State on disk

**Modified files**:
- `tools/extract_entities.py` — patched:
  - Line 1250: regex `S?\d+[a-z]?\b` (was `\d+[a-z]?\b`)
  - Lines 1216-1226: name reject list extended (question, verdict, quantity, item, topic, description)
  - Lines 469-487: `RE_CLOSED_SECTION` extended with `Summary Table` and `Map(?:\s+Updates)?`
  - New parser: `_extract_closed_from_session_workingpaper` and routing in dispatcher
  - Constants added: `_WP_CMAP_SECTION_RE`, `_WP_FILENAME_RE`, `_WP_CLOSURE_MARKERS`, `_WP_HEADER_WORDS`

**New files**:
- `tools/_session_cmap_gap_report.md` — full per-session classification table
- `tools/_session_cmap_gap_report.py` — re-runnable gap report
- `tools/_test_session_closure_extraction.py` — extractor test harness
- `tools/_constraint_map_retrofit_handoff.md` — this file

**Memory changes**:
- Deleted: `~/.claude/projects/C--sandbox-Ainulindale-Exflation/memory/feedback_hygiene-audits-direct-not-swarm.md`
- MEMORY.md line removed (was line 29 in the index)

### Verification command

After each agent completes, verify on disk:
```
Grep -c "^\|.*\*\*(CLOSED|LANDED|PINNED|REGISTERED|PROMOTED)\*\*" <WP_PATH>
```
Expected: count matches agent's reported N.

### Resume sequence

1. Pick next session from the remaining list above.
2. Substitute `{SESSION_ID}` and `{WP_ABSOLUTE_PATH}` into The Prompt.
3. Dispatch Eight `gen-physicist` agents with that prompt. in the background.
4. Verify on disk via the Grep command above.
6. Keep 8 agents in flight

For NO_WP S19-S34 sessions: requires a modified prompt variant (source = synthesis file, create new WP file) — not yet drafted.
