---
name: rclab-review
description: Generate solo synthesis/review reports from source docs — 1+ independent agents each read the same sources and write their own report. No coordination between agents.
argument-hint: <doc(s)> --agents <type1[,type2,...]> [--session <id>] [--output <path>] [--context <text>]
---

# rclab-review

## --help

If `$ARGUMENTS` contains `--help` or `-h` (or is empty and the user seems confused), read and display `.claude/rclab-help.md`, then stop. Do not proceed with any other phase.

---

Solo synthesis. 1+ agents independently read source documents and write their own report. No coordination between agents — each produces its own file from the same inputs.

For 2-agent iterative workshops on a shared document, use `/rclab-workshop`.

## Usage

```
# One agent synthesizes source docs
/rclab-review session-63-W6*.md --agents gen-physicist

# Three agents each independently write a report
/rclab-review session-63*.md --agents hawking,landau,volovik --session 63

# With focus topics
/rclab-review session-74*.md --agents qa,connes --context CC closure, GL stability
```

---

## Phase 0: Parse & Validate

### 0a. Extract Arguments

Parse `$ARGUMENTS`:

| Arg | Required | Default | Notes |
|:----|:---------|:--------|:------|
| `[doc(s)]` | yes (1+) | — | Source doc paths or globs (positional, before flags) |
| `--agents` | yes | — | Comma-separated agent types or short names (1 or more) |
| `--session` | no | auto-detect | Session ID (e.g., `63`) |
| `--output` | no | auto-detect | Output path prefix (per-agent files generated) |
| `--context` | no | — | Focus topics or instructions passed to agents |

### 0b. Validate

1. **Source docs**: Glob-resolve paths. Read 1 line of each to verify existence. Report missing and stop.
2. **Agent types**: Resolve short names via `.claude/templates/agent-roster.md`. If invalid, list available types and stop.

### 0c. Defaults

**Session ID** (if not provided):
- Extract from first source doc filename: regex `session-(\d+)`

**Output path** (if not provided, per agent):
- `sessions/session-{id}/session-{id}-{short-name}-synthesis.md`

If session ID unresolvable, ask the user.

---

## Phase 1: Collision Check

If any output file already exists, ask: "Output file exists at `{path}`. Overwrite / New name / Cancel?"

---

## Phase 2: Execute

For each agent in `--agents`, spawn a **background agent** in parallel:

- `subagent_type`: the agent type
- `run_in_background`: true
- `name`: `review-{short-name}`
- `mode`: `acceptEdits`

**Agent prompt:**

```
You are writing a synthesis report for the Phonon-Exflation Cosmology project.

## Source Documents (read ALL of these FIRST)
{numbered list of source doc paths}

Also read your agent memory: `.claude/agent-memory/{your-type}/MEMORY.md`

{If --context provided:}
## Focus
{context text}

## Your Task

Read all source documents, then write your synthesis to: `{output_path}`

## Document Structure

Follow the template in `.claude/templates/synthesis.md`.

## Rules
- Gate verdicts from source docs are authoritative — do not re-adjudicate.
- If sources conflict, flag the conflict explicitly.
- Write ONLY the output file.
- Use substrate language, not LCDM vocabulary (see phononic-framing.md).
- Every equation dimensionally consistent. Every approximation states its regime.
```

If multiple agents: create a TaskCreate per agent for progress tracking.

---

## Phase 3: Verify & Report

```
=== RCLAB-REVIEW COMPLETE ===
Agent(s): {list}
Output: {path(s)} ({lines} lines each)
Source documents: {N}
```

---

## Rules

1. **Never overwrite files** without user confirmation (collision check).
2. **Never execute computations** — review reports only.
3. **Never re-adjudicate gate verdicts** — source doc verdicts are authoritative.
4. **No cross-agent coordination** — each agent writes independently. For iterative 2-agent exchanges, use `/rclab-workshop`.
5. **Substrate-first framing** — phononic-framing.md applies.

## Error Handling

| Condition | Action |
|:----------|:-------|
| No source docs | Show usage and stop |
| Source doc missing | Report which, stop |
| No `--agents` | Show usage and stop |
| Agent type invalid | List available types, stop |
| Output collision | Ask: overwrite / rename / cancel |
| Agent fails to produce output | Report, suggest different agent |

---

## ARTIFACTS PROMISED JSON block (compute-mode only) — S84 W9a-102

This section governs **compute-mode** dispatch prompts (those emitted by `/rclab-coordinate` or direct `Agent` calls that produce computation verdicts). Pure-review dispatches (the Phase 2 above) are exempt. The manifest block is the machine-readable contract between the orchestrator and the `completion-verify.sh` post-dispatch hook (W9a-98).

### Mandate

Every compute-mode dispatch prompt MUST include a `## ARTIFACTS PROMISED` section immediately after the final RULES block and before the closing "Begin." sigil. The block is auto-generated by `computations/_shared/_generate_manifest.py` from the gate's R3 YAML / 13-field markdown pre-registration block (template at `.claude/templates/r3-yaml-gate-block.yaml`, validator at `computations/_shared/_yaml_gate_validator.py`). The block is parsed by `completion-verify.sh` as structured JSON — NOT by prose regex on a free-form "deliverables" paragraph (the known-unreliable legacy path). (The generator was relocated from `.claude/skills/rclab-review/generate_manifest.py` to `computations/_shared/_generate_manifest.py` in S88 2026-05-07 per shared-infrastructure naming convention; consumer is `/rclab-coordinate`, not `/rclab-review`.)

### Exact format (PIN from plan §W9a-102)

```
## ARTIFACTS PROMISED
```json
{
  "gate_id": "S84-W9A-102-MANIFEST-AUTO",
  "script": "computations/_shared/s84_w9a_102_manifest_auto.py",
  "verdict_line_target": "computations/session-84/s84_gate_verdicts.txt",
  "data_files": ["sessions/archive/session-84/manifest_auto_audit.json"],
  "plot_files": [],
  "working_paper_sections": [
    {"section": "§W9-102", "path": "sessions/archive/session-84/session-84-w9-workingpaper.md", "min_lines": 15}
  ]
}
```
```

### Required JSON keys (PIN, exact list, in order)

1. `gate_id` — canonical gate ID string, matches the verdict line's leading token
2. `script` — producing script path from `gate.method.producing_script`
3. `verdict_line_target` — always `computations/session-{N}/s{N}_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md` canonical-path rule
4. `data_files` — list of `.npz`, `.npy`, `.json`, `.csv`, `.txt`, `.yaml` outputs declared in method
5. `plot_files` — list of `.png`, `.pdf`, `.svg` outputs declared in method
6. `working_paper_sections` — list of `{"section": "§X.Y", "path": "<wp>", "min_lines": 15}` (min_lines defaults to 15 per `.claude/rules/agent-standards.md` stub threshold)

Missing any of the 6 keys, or an empty/placeholder value where the gate declares an artifact, is a spot-audit FAIL.

### Generator invocation

```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" computations/_shared/_generate_manifest.py \
  --plan sessions/session-plan/session-84-plan-w9a.md \
  --gate-slug W9a-102 \
  --session-n 84 \
  --wp sessions/archive/session-84/session-84-w9-workingpaper.md \
  --emit-prompt-block
```

Modes:
- `--emit-prompt-block` (default): prints the full `## ARTIFACTS PROMISED` markdown + fenced-json block, ready to paste into a prompt
- `--emit-json`: prints the manifest JSON only, for direct hook consumption
- `--audit <prompts-dir>`: spot-audits every prompt in a directory against its gate and writes `manifest_auto_audit.json`

### Spot-audit rubric (session close)

Per plan §W9a-102 substitution chain:

- `pass_fraction = (1/|S|) * sum manifest_present(p) * manifest_accurate(p, g)`
- `PASS` iff `pass_fraction == 1.0`
- `INFO` iff `0.90 <= pass_fraction < 1.0`
- `FAIL` iff `pass_fraction < 0.90`

Sample size `|S| >= max(SPOT_AUDIT_SAMPLE_FLOOR=2, round(0.10 * N_dispatches))`.

### Integration with rclab-coordinate

`/rclab-coordinate` (compute-mode sibling) should shell out to `computations/_shared/_generate_manifest.py` for each dispatch and splice the block into its prompt template between RULES and "Begin." This eliminates the S82-observed failure mode (verdict-appended but WP-section-skipped goes undetected because prose "deliverables" regex is lossy).
