# Agent Standards

Universal standards for all physics/research agents. Template-specific and domain-specific standards remain in each agent's definition file.

## Formal Rigor
- Every equation must be dimensionally consistent. Every approximation must state its regime of validity.
- Verify limiting cases: degenerate limits, boundary cases, zero-coupling, strong-coupling.
- Self-correct immediately if an error is detected mid-derivation — stop, flag, correct before proceeding.
- Use precise notation appropriate to the domain. Number important equations for reference.

## Persistent Memory
- `MEMORY.md` is always loaded into system prompt — keep under 200 lines.
- Create separate topic files for detailed notes; link from MEMORY.md.
- Organize by topic, not chronologically.
- Do NOT record: probability estimates (Skeptic's domain), narrative trajectory assessments, constraint counts as rhetoric, session-specific ephemera, content that duplicates shared rules, or project-level registries (watchlists, detector rosters, closed-mechanism lists, cross-channel tables, canonical constants) — those belong in `sessions/framework/` + `knowledge.db`.

### Memory Scope — Agent-Private vs Project-Level

Agent memory stores AGENT-PRIVATE context only: this agent's feedback rules, user-preference learnings, and methodological notes it re-uses at spawn. It is NEVER the canonical location for data other gates cite.

**Project-level registries** live under `sessions/framework/<registry>.md` (human-readable, `/weave --update`-indexed) and `tools/knowledge.db` (machine-queryable via knowledge MCP). Template: `sessions/framework/registry/_registry-template.md`.

### Agent-Memory Registry Inversion (AMRI)

A section of an agent's memory files is AMRI if ANY of the following hold:

1. **Input-pin test**: another gate lists the memory file as an Input-SHA pin in its PRDR machinery block.
2. **Output-target test**: a gate's method section writes to `.claude/agent-memory/*/MEMORY.md` or `project_*.md` as its primary registry-maintenance output (not as secondary agent-housekeeping).
3. **Cross-agent overlap test**: two or more agents' memories contain overlapping entries for the same observable, mechanism, or detector.

#### Scope of "memory files" for AMRI

AMRI applies identically to BOTH:

- **Per-agent project memory**: `.claude/agent-memory/<agent-type>/*.md` (e.g., `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`)
- **Orchestrator project memory**: `~/.claude/projects/<project-slug>/memory/*.md`. The slug encodes the project; this directory is NOT user-global private memory — it is the project-scoped memory for the orchestrator (main agent).

A plan-block pinning either path-shape as Input-SHA fires AMRI Test 1. AMRI applies to orchestrator memory identically to per-agent memory; the structural rule is path-independent. Not following AMRI for orchestrator memory breaks audit traceability.

AMRI sections must be migrated to `sessions/framework/` + knowledge.db. Detection tool: `computations/_shared/_agent_memory_inversion_audit.py`. Migration tool: `/shortterm <agent>` with its AMRI-PROMOTE classification (see skill).

#### What triggers Test 1 (input-pin)

Test 1 fires whenever any plan-block, gate-block, or other gate's PRDR machinery enumerates a path matching `.claude/agent-memory/*/MEMORY.md` (or `project_*.md`) in its INPUT-PIN MAP — regardless of whether the pin value is `<pinned at dispatch>` (runtime SHA capture), a precomputed SHA, or a `<pinned at plan-freeze>` placeholder.

**Principle**: taking a note is allowed; using memories as the pin source is not. Memory exists for the AGENT'S OWN re-use at spawn — it is never the canonical location for cross-gate pin sourcing. The runtime-SHA-capture argument that "the pin is just for audit reproducibility" does NOT redeem an agent-memory pin: agents always read their own MEMORY.md at spawn regardless, so the pin adds no dispatch value, and `/shortterm` rewrites these files routinely so the SHA is structurally session-volatile. If a downstream gate genuinely needs project-level synthesis from an agent's domain expertise, that synthesis belongs in `sessions/framework/registry/<topic>.md` (which the agent then maintains as sole writer), not in agent memory.

#### What does NOT trigger Test 1

A plan-document mentioning `.claude/agent-memory/*/MEMORY.md` in a **prerequisite-availability table** ("Agent memories available; agents read at dispatch time; implicit dispatch validation") without listing the file as an INPUT-PIN MAP entry is NOT AMRI. The distinction is structural: prerequisite-availability is a startup check ("does the file exist?"); Input-SHA pin is an audit-trail commitment ("compute closure SHA over this file's content for reproducibility"). Only the latter triggers AMRI Test 1.

### What must NOT live in agent memory
- Watchlists, detector rosters, observational-prediction tables
- Cross-session machinery-parameter registries
- Canonical constant values (those live in `computations/_shared/canonical_constants.py`)
- Gate-verdict tables or session-wide tallies
- Anything referenced by another agent's spawn prompt as authoritative data

## Completion Verification (compute-mode dispatches)

**Principle**: The agent infrastructure should not signal task-completion until ALL promised artifacts are actually on disk. An agent's "task complete" claim is only meaningful after every promised output — script, data, plot, verdict line, working-paper section, memory file — has been verified to exist with non-stub content.

**Observed failure mode**: agent appends a verdict line, then terminates at the verdict-confirmation step without writing the promised working-paper section. The terminal message often claims completion ("Now I need to write §X.Y...", "verdict line present, now proceeding...") while the final write is skipped. Common variants: no-writes; verdict-only with section eventually landed but reported as mid-task; verdict + script with §-section stub.

**Mitigations**:

1. **Orchestrator post-dispatch verification** (required until infrastructure fix lands). After every Agent-tool completion notification in compute mode, the orchestrator MUST verify:
   - Verdict line present in the designated `s{N}_gate_verdicts.txt` (grep by gate ID)
   - Script file present with non-trivial size (`ls -la s{N}_{item}*.py`)
   - Data file present (`.npz`) and plot (`.png`) if promised
   - Working-paper section present with substantive content — verified by the gate's pre-registered `must_contain` patterns (Status / Verdict / Output Artifacts / substrate framing per the R3 template), NEVER by line count. A "stub" is a section whose required `must_contain` markers are absent, not a short one (per `feedback_max-effort-full-fidelity.md` + the R3 template's "NO LENGTH REQUIREMENTS"; `rclab-coordinate` already verifies this way).

2. **Agent infrastructure** (future): agents should not emit a task-complete signal until every `write-target` declared in their prompt has passed an on-disk existence + content-length check. Prompt-level "CRITICAL: write §X.Y IN FULL before terminating" admonitions help but do not eliminate the failure; the fix is structural (infrastructure gates completion on artifact existence).

3. **SHA uniqueness check** (related discipline from `.claude/rules/gate-verdicts.md`). After each verdict-line append, the orchestrator checks the 64-char SHA against all prior verdict closures in the session file. Duplicates indicate a script that hardcoded or copy-pasted the SHA rather than computing it from the input-pin map — the verdict is physically defensible but audit-provenance-broken.

**What NOT to do**:
- Do NOT re-dispatch the same Agent just because it reported mid-task text; verify artifacts first. False alarms are common (the agent may have written everything and reported imprecisely).
- Do NOT trust subagent completion summaries over filesystem state. The result claim is what the agent INTENDED to do; the filesystem is what actually happened.
- Do NOT silently accept a stub working-paper section. Either re-dispatch a minimal write-only follow-up prompt, or mark the section PASS-with-text-deferred and log the write-up as an explicit carry-forward to the next session.

## HIGH-DENSITY WORKSHOP TEMPLATE

**Status**: SUGGESTION at K=1. Promotes to MANDATORY at K=3 per `feedback_rules-compensate-missing-structure.md`.

When a workshop's structural target straddles multiple layers (bare/derived/methodology/meta), the verdict should NOT force a single PASS/FAIL/INFO at the literal pre-registration. Instead, **decompose into INDEPENDENT OUTPUT slots**, each with its own promotion path and verdict.

### Multi-layer output-slot decomposition

A single high-density workshop can simultaneously produce:

1. **Literal pre-reg verdict** (close one literal pre-reg as INFO if rubric-form failure surfaces — Class 8.2 PRU)
2. **Structural candidate at one layer** (registry promotion path; e.g., §VII.X candidate from bare-eigenvalue layer)
3. **Structural candidate at another layer** (separate registry promotion path; e.g., §VII.Y candidate from moment-integral layer)
4. **Methodology rule-file extension** (taxonomic extension to existing rule; e.g., PRU Class 8.2 added as sub-class)
5. **Methodology generalization to broader contexts** (toolkit extension with its own forward gate)
6. **Calibration corpus entry** (concrete instance added to an existing rule's corpus)

### Workshop-design discipline

Workshops that pre-identify as "high-density" (multi-layer structural target) MUST adopt the multi-output decomposition pattern at workshop-spec time:

1. **Identify the layers the structural target straddles** at pre-registration (bare-eigenvalue / moment-integral / methodology / meta)
2. **Pre-register independent OUTPUT slots per layer**, each with its own PASS/FAIL/INFO criterion
3. **Allow simultaneous landing of candidates at multiple slots** (registry candidate at layer A; rule-file extension at layer B; calibration corpus entry at layer C)
4. **Avoid forcing a single literal verdict** that conflates layers — the literal verdict's rubric-form failure (Class 8.2) is then SEPARATE from the structural candidates the workshop generates
