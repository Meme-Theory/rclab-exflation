---
name: stage0_hygiene_backfill_wave_planning
description: Authoring a Wave-0 hygiene-backfill PLAN (canonical-constant promotion + mack falsifier sub-row landing) as COMPUTE-class artifact-existence gates
metadata:
  type: project
---

Planning a Wave-0 **hygiene-backfill** wave (provenance promotion + falsifier-surface landing, ~0 compute) — the recipe, learned S117 W0.

**Wave-class decision.** Both gates have an artifact-existence PASS predicate (M1-shaped: `get_constant(...)` returns the value / sub-row present). But if the gate-IDs are NOT in `methodology-wave-allowlist-ledger.md`, **M4 forbids METHODOLOGY-class** (no self-promotion path; recursion-attack closure). Author as **COMPUTE-class artifact-existence landings** instead — `gate_type: compute`, minimal PRDR with items (2)(3)(4) = N/A-with-reason per the r3-template **S95 non-compute clause** ("artifact-existence/hygiene" is an explicitly-listed gate class the validator accepts; do NOT invent a numerical threshold). No allowlist append needed; simpler than orchestrator-only allowlist edit.

**Canonical-constant promotion gate (e.g. CF-S117-HK-RHOS-C2-PROMOTE).**
- Premise FIRST: `get_constant(name)` → not-found AND `grep name canonical_constants.py` → ABSENT (the DB and the `.py` are TWO surfaces; check both — `get_constant` reads the DB/index, scripts import the `.py`).
- Value SOURCE = the prior-session npz; pin its static SHA as the load-bearing input. Confirm the value bit-exact (`float64(npz[name]) == X` → True) and land that float64 (round-trip, tolerance 0.0).
- `canonical_constants.py` is a **MUTATE TARGET** → `sha256: <computed-at-runtime>` + record the freeze-snapshot SHA in the Input-SHA Ledger (precondition state).
- Mechanism = the `update_constant` MCP tool (math-scripts.md Canonical Write-Order Step 2 — it makes the value importable from the `.py`); verify via `get_constant` + `from canonical_constants import name`. Script must_contain keeps `from canonical_constants import` (the post-landing importability re-verify).
- If the value is cited downstream, add `publication_precision` (Class 8.3). `substitution_chain: required: false` (verbatim definitional-datum landing, no direction claim).

**mack falsifier-inventory sub-row landing gate (e.g. CF-S117-HK-ALPHAS-TILT-LANDING).**
- `agent_type: mack-cosmic-bridge` (SOLE writer of `falsifier-master-inventory.md`, `feedback_mack-bridge-role.md`); `writer_agent == agent_type`.
- The verifier is a grep-verify of the inventory — it imports NO canonical constant → **relax the script must_contain to just `print_verdict_payload`** (the canonical_constants-import marker does not apply; say so in a comment).
- Pin the upstream anchor's `audit_sha256` (verify it's present in the inventory FIRST) as a static citation pin; inventory is the MUTATE TARGET (`<computed-at-runtime>` + freeze snapshot).
- If the landed content is a sign/flatness/independence claim, include the substitution_chain (`required: true`) sourced from the originating workshop CF — but trigger stays `[AUDIT]` (artifact-existence landing, not a runtime sign-test ⇒ `schema_v2_3tuple_required: false`, no [SIGN] 3-tuple).
- Flag the **single-observable-per-triple filter** (`cross-pillar-bridge-anatomy.md`) + the sibling row cross-link so mack lands a *sub-row on the existing leg*, NOT a duplicate observable row.

**Wave-0 independence.** A hygiene-backfill wave is usually structurally INDEPENDENT of all other waves (forward-enabling, not gating) — the promoted constant's direct consumer already ran in the prior session; the falsifier sub-row is a surface annotation, not a numerical input. Document this in the Wave→Wave decision point (no mechanical-closure prereq-block).

**Self-QA before reporting.** Parse-check the fenced `yaml` blocks (`yaml.safe_load`) — confirm R3 + 8 PRDR keys + `output_artifacts` + `verdict_source` set + NO `expected_verdicts`. Use **block scalars** (`>`/`|`) for any field carrying Greek/`𝒩`/`⇒`/`√` OR a `get_constant('...')` apostrophe (single-quote-in-single-quoted-YAML trap). See [[plan_authoring_r3_yaml]], [[wp_shell_generation]].
