---
name: collab-review
description: Launch all research agents to produce collaborative reviews of session file, then synthesize into a master document
disable-model-invocation: true
argument-hint: <session-file> [--agents agent1,agent2,...] [--skip-synthesis] [--date YYYY-MM-DD]
---

# Collaborative Review Pipeline

Launch research agents to independently review session files from their specialist perspective, then synthesize all reviews into a master document.

## Usage

```
/collab-review sessions/archive/session-19/session-19d-casimir-energy.md
/collab-review sessions/archive/session-19/session-19d-casimir-energy.md --agents einstein,feynman,hawking
/collab-review sessions/archive/session-19/session-19d-casimir-energy.md --skip-synthesis
```

## Arguments

- `$0` — Path to the session file to review (REQUIRED)
- `--agents` — Comma-separated list of agents to launch (default: ALL 20)
- `--skip-synthesis` — Skip the master synthesis step (just produce individual reviews)
- `--date` — Override the date prefix for output files (default: extracted from input filename)

## Pipeline

### Phase 0: Pre-Flight

FOLLOW `team-lead-behavior.md` (project root). Non-negotiable on all items.

### Phase 1: Parse Arguments

Extract the session file path from `$ARGUMENTS`. Verify the file exists using the Read tool.

Extract the session identifier from the filename. For example:
- `sessions/archive/session-19/session-19d-casimir-energy.md` -> session = `session-19d`, session_folder = `sessions/archive/session-19/`

If `--agents` is specified, parse the comma-separated list. Otherwise use ALL agents.

If `--date` is specified, use that. Otherwise extract from the input filename.

### Phase 2: Launch Research Agents (PARALLEL)

The full agent roster with their subagent_type mappings:

| Agent Name | subagent_type | Researcher Dir |
|:-----------|:-------------|:---------------|
| einstein | einstein-theorist | researchers/Einstein/ |
| feynman | feynman-theorist | researchers/Feynman/ |
| hawking | hawking-theorist | researchers/Hawking/ |
| sagan | sagan-empiricist | researchers/Sagan/ |
| connes | connes-ncg-theorist | researchers/Connes/ |
| landau | landau-condensed-matter-theorist | researchers/Landau/ |
| kk | kaluza-klein-theorist | researchers/Kaluza-Klein/ |
| berry | berry-geometric-phase-theorist | researchers/Berry/ |
| tesla | tesla-resonance | researchers/Tesla-Resonance/ |
| quantum-acoustics | quantum-acoustics-theorist | (no dedicated folder) |
| baptista | baptista-spacetime-analyst | researchers/Baptista/ |
| paasch | paasch-mass-quantization-analyst | researchers/Paasch/ |
| sp | schwarzschild-penrose-geometer | researchers/Schwarzschild-Penrose/ |
| dirac | dirac-antimatter-theorist | researchers/Antimatter/ |
| neutrino | neutrino-detection-specialist | researchers/Neutrino-Detection/ |
| cosmic-web | cosmic-web-theorist | researchers/Cosmic-Web/ |
| little-red-dots | little-red-dots-jwst-analyst | researchers/Little-Red-Dots/ |
| nazarewicz | nazarewicz-nuclear-structure-theorist | researchers/Nazarewicz/ |
| spectral-geometer | spectral-geometer | (no dedicated folder) |
| quantum-foam | quantum-foam-theorist | (no dedicated folder) |

**Launch ALL agents in parallel** using the Task tool. Each agent gets the same base prompt (below) customized with their name and researcher directory.

**IMPORTANT**: Launch agents in batches of 5-6 to avoid overwhelming the system. Wait for each batch to complete before launching the next. Four batches: [einstein, feynman, hawking, sagan, connes, landau], [kk, berry, tesla, quantum-acoustics, baptista, paasch], [sp, dirac, neutrino, cosmic-web, little-red-dots, nazarewicz], [spectral-geometer, quantum-foam].

Each agent runs in the background (`run_in_background: true`). Track their output files.

### Phase 2 Agent Prompt Template

For each agent, use this prompt (substituting {AGENT_NAME}, {RESEARCHER_DIR}, {SESSION_FILE}, {SESSION_ID}, {DATE}, {OUTPUT_FILE}):

```
You are producing a **{SESSION_ID} Collaborative Review** -- a standalone document from your specialist perspective, reviewing the session file and contributing your unique expertise to the group.

## What to produce

Write a file at: `{OUTPUT_FILE}`

## Required Reading (do these FIRST)

1. **The session file you are reviewing**: `{SESSION_FILE}` -- Read this completely.
2. **Your research papers index**: `{RESEARCHER_DIR}/index.md` (or INDEX.md) -- Consult your papers for relevant connections.
3. **Cross-researcher index**: `researchers/index.md` -- Understand how your domain fits into the broader framework.
4. **Your agent memory**: `.claude/agent-memory/` (your directory if it exists)

## Document Structure

Follow this EXACT structure:

### Header
```
# {AGENT_DISPLAY_NAME} -- Collaborative Feedback on {SESSION_ID}

**Author**: {AGENT_DISPLAY_NAME}
**Date**: {DATE}
**Re**: {SESSION_ID} Results
```

### Section 1: Key Observations
Review the session results through YOUR specialist lens. What stands out? What is significant from your domain's perspective? What does your expertise reveal that generalists would miss?

### Section 2: Assessment of Key Findings
Evaluate the session's main results. Are they sound? What caveats apply? What would strengthen or weaken the conclusions?

### Section 3: Collaborative Suggestions
This is your PRIMARY CONTRIBUTION. Identify:
- Specific computations, analyses, or investigations that your domain suggests
- Connections to your research papers (cite specific equations, theorems, results)
- Zero-cost or low-cost diagnostics available from existing data
- Novel approaches that other reviewers are unlikely to suggest

### Section 4: Connections to Framework
How do the session results connect to the broader phonon-exflation framework? What implications do they have for the project's open questions?

### Section 5: Open Questions
The deepest questions YOUR specialist perspective raises about these results.

### Closing Assessment
Overall verdict and a memorable closing line. Do NOT include probability estimates.

## Constraints
- Ground arguments in YOUR research papers -- cite specific equations and results
- Be specific about computations: what to compute, from what data, expected outcome
- Do NOT duplicate generic observations -- provide YOUR unique specialist angle
- Keep the document focused: 150-400 lines
```

### Phase 3: Monitor Completion

After launching all agents, periodically check their output files using the Read tool. Report progress to the user as agents complete.

When ALL agents have completed, proceed to Phase 4 (unless `--skip-synthesis` was specified).

### Phase 4: Synthesize Master Document

Launch ONE final agent (use `general-purpose` subagent_type) to read ALL individual collab reviews and produce a master synthesis at:

`sessions/session-{NUM}/{SESSION_ID}-master-collab.md`

The synthesis agent prompt:

```
Read ALL of the following collaborative review files and produce a master synthesis document.

## Files to Read
{LIST_OF_ALL_COLLAB_FILES}

## Output File
Write to: `sessions/session-{NUM}/{SESSION_ID}-master-collab.md`

## Structure

# Master Collaborative Synthesis: {SESSION_ID}
## {N} Researchers, One Computation

### I. Executive Summary
2-3 paragraph summary of the unanimous and divergent findings.

### II. Convergent Themes
Identify themes that 10+ reviewers agree on. State the convergence count (e.g., "14/15 unanimous").

### III. New Physics From the Collaboration
Ideas that emerged from cross-pollination -- present in multiple reviews but not in the original session file.

### IV. Divergent Assessments
Where reviewers disagree. State the disagreement clearly with each side's reasoning.

### V. Priority-Ordered Next Steps
Synthesize all suggested computations into a priority-ordered agenda for the next session.

### VI. Subdocument Index
Table linking to each individual review with their key contribution.

### VIII. Closing
A synthesis statement that captures the collective intelligence.
```

### Phase 5: Report

After synthesis is complete, report to the user:
- Number of agents that completed successfully
- Path to master synthesis
- List of all output files
- Any agents that failed and why

## Output File Naming Convention

Individual reviews: `sessions/session-{NUM}/{SESSION_ID}-{AGENT_NAME}-collab.md`

Master synthesis: `sessions/session-{NUM}/{SESSION_ID}-master-collab.md`

## Error Handling

- If an agent fails, log the failure and continue with remaining agents
- If fewer than 5 agents complete, warn the user before attempting synthesis
- If the session file doesn't exist, abort immediately with an error message
