---
name: conjecture-index
description: Index the project's open conjectures/propositions — scans sessions + open channels, tabulates with EVOI, origin, related gates, and status
argument-hint: [--status open|closed|all] [--since <session-N>] [--top <N>] [--update]
---

# /conjecture-index — Open-Conjecture Ledger

Scans the project for stated-but-unproven conjectures, propositions, and hypotheses. Groups them by topic, attaches metadata (origin session, EVOI if computed, related gate IDs, current status), and emits a single ledger table.

The point: a project this size accumulates dozens of informally stated conjectures across session minutes, working papers, and agent memory. Without a periodic sweep they stay scattered. This skill produces a canonical ledger so a planner (or `/rclab-plan`) can prioritize them by EVOI.

## Usage

```
/conjecture-index                    # all open conjectures, default view
/conjecture-index --status all       # include closed + withdrawn
/conjecture-index --since 80         # only conjectures stated or touched from S80 onward
/conjecture-index --top 15           # top 15 by EVOI (descending)
/conjecture-index --update           # rebuild the cached ledger at sessions/framework/conjecture-ledger.md
```

## Where conjectures live in this project

| Source | What to scan for |
|:-------|:-----------------|
| `sessions/session-N/*.md` | Headings matching `Conjecture`, `Claim`, `Hypothesis`, `Open Question`, `Open Problem`; bullets under `Open channels`, `Carry-forward`, `OPEN` |
| `sessions/framework/*.md` | Any statement marked `OPEN`, `UNCOMPUTED`, `PROVISIONAL` |
| `sessions/permanent-results-registry.md` | Status-field transitions; watch for `PROVISIONAL` or `pending` |
| `sessions/evoi-framework.md` | The EVOI priority table (authoritative source for EVOI scores) |
| Knowledge MCP `open_channels` table | Canonical open-mechanism ledger: `mcp__knowledge__list_entities(type="open")` |
| Knowledge MCP search | `mcp__knowledge__search_knowledge("conjecture OR hypothesis OR open")` — FTS5 across everything |

## Execution steps

1. **Parse arguments**. Extract `--status`, `--since`, `--top`, `--update` from `$ARGUMENTS`.

2. **Pull authoritative lists first** (these are canonical; everything else is supplementary):
   - `mcp__knowledge__list_entities(type="open")` — returns all open channels with full metadata.
   - Read `sessions/evoi-framework.md` — the living EVOI table.

3. **Scan session-minute files** (widen the net). Use Grep:
   ```
   Grep pattern="^##+\s*(Conjecture|Claim|Hypothesis|Open\s+Question|Open\s+Problem)" glob="sessions/**/*.md" output_mode="content" -n=true
   ```
   Also scan for bullet-level markers: `- **OPEN**`, `- **UNCOMPUTED**`, `- **CONJECTURE:**`.

4. **Deduplicate**. Many conjectures are restated across sessions; collapse by topic (look for shared gate IDs, shared mechanism names, or >70% token overlap in the statement).

5. **Enrich each entry** with the 7-column ledger schema:
   | Column | Source |
   |:-------|:-------|
   | `id` | Open-channel ID if present; else a slug derived from first statement |
   | `statement` | One-sentence summary (≤180 chars) |
   | `origin_session` | Earliest session where stated |
   | `last_touched` | Most recent session that referenced it |
   | `related_gates` | Gate IDs (from knowledge MCP cross-ref) |
   | `EVOI` | Value from `sessions/evoi-framework.md` if present; otherwise `—` |
   | `status` | `OPEN` / `IN-PROGRESS` / `CLOSED` / `WITHDRAWN` / `PROVISIONAL` |

6. **Apply filters** (`--status`, `--since`, `--top`).

7. **Emit the ledger** as a single markdown table, sorted by:
   - Primary: EVOI descending (empty EVOI last)
   - Secondary: last_touched descending

8. **If `--update`**, write the ledger to `sessions/framework/conjecture-ledger.md` with a timestamp + regeneration command at the top. Otherwise print to stdout.

## Output format

```
# Open-conjecture ledger
- Generated: 2026-04-19
- Status filter: open
- Since session: (none)
- Total conjectures: 23
- Authoritative sources: knowledge MCP open_channels (N=15), sessions/evoi-framework.md (N=18), grep-only hits (N=8)

| # | ID | Statement | Origin | Last | Gates | EVOI | Status |
|--:|:---|:----------|:------:|:----:|:------|-----:|:-------|
| 1 | ALPHA-ENV-43 | ... | S43 | S80 | ... | 0.81 | OPEN |
| 2 | FRIEDMANN-BCS-38 | ... | S38 | S83 | ... | 0.62 | OPEN |
| … |

## Conjectures with no EVOI score (N=8)
These have been stated but not yet prioritized. Consider adding to the EVOI table if any are decision-relevant.
- `<statement>` (S74, no gate link)
- …

## Regeneration
- Cached at: `sessions/framework/conjecture-ledger.md`
- Rebuild: `/conjecture-index --update`
- Sole authority for status transitions: see `.claude/rules/gate-verdicts.md`
```

## Guard rails

- **Do NOT** invent conjectures. If a bullet says "could this be X?", that is a question, not a conjecture — skip unless the session explicitly labels it.
- **Do NOT** copy long statements verbatim. Summarize to ≤180 chars.
- **Do NOT** promote a conjecture to CLOSED based on agent-memory claims. Per `.claude/rules/epistemic-discipline.md` + memory rule `feedback_agent-roster.md`, only the canonical sources (knowledge MCP `closed` table, gate-verdict files, synthesis docs) can close a conjecture.
- **Do** flag provisional/withdrawn entries distinctly — they're useful for the "why we gave up on X" history.
- **Do** preserve EVOI scores exactly from `sessions/evoi-framework.md` — never recompute, per `feedback_framework-hygiene.md`.
