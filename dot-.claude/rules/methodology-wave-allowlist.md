# Methodology Wave Allowlist

This rule governs the M4 substrate of `wave-classification.md`. The allowlist data itself (the ~108 gate-ID rows authorized as METHODOLOGY-class) lives in the ledger file `sessions/framework/registry/methodology-wave-allowlist-ledger.md`. This file carries the rule that governs how the ledger is written, audited, and consumed.

## Rule

A gate-ID listed in the LEDGER (`sessions/framework/registry/methodology-wave-allowlist-ledger.md §"Allowlist Rows"`) has M4 satisfaction per `wave-classification.md §M4`.

A gate-ID NOT listed in the ledger CANNOT satisfy M4, and therefore CANNOT be classified as METHODOLOGY-class regardless of M1-M3 satisfaction. Absence routes the gate to COMPUTE-class fallthrough or MIXED-class triage per `wave-classification.md §"Strict-conjunction requirement"`.

## Edit discipline (recursion-attack closure)

The ledger file is **append-only** and **orchestrator-only edit**. Harness convention enforces subagent edit-denial on BOTH this rule file AND the ledger file. The following editing rules apply to the ledger:

1. **Append-only**: rows MAY be added; rows MAY NOT be removed, reordered, or modified post-landing. The historical row sequence is the audit trail of methodology-class promotions across sessions. Two prior schema migrations are recorded in the ledger's §"Schema migration history" as the structural exceptions to strict append-only.
2. **Orchestrator-only edit**: subagents are denied Edit / Write / MultiEdit on the ledger by harness convention. The orchestrator (or the user, on direct instruction) is the sole authorized editor. This closes the **recursion attack**: without the closure, a subagent dispatched on a non-allowlisted gate-ID could append its own gate-ID to the allowlist mid-execution, satisfying M4 by self-promotion and bypassing the M1-M4 conjunction's intent. The closure breaks the self-promotion path — allowlist additions can only originate from the orchestrator at plan-freeze time (or from explicit user instruction).
3. **Per-row dual-SHA**: each row records `sha256_of_plan_block` over the gate's plan-file block, matching the dual-SHA discipline of the `wave-classification.md` METHODOLOGY-class closure.
4. **Append-helper writes 3-column rows only**: append helpers (canonical pattern: `computations/session-88/s88_w8_allowlist_append_helper.py`) MUST write `| {gate_id} | {session} | {sha} |` to the ledger AND a parallel `### {gate_id} ({session}) — {sha}` entry with verbatim rationale prose to `sessions/framework/registry/methodology-wave-instances.md`. A helper that writes rationale prose into the ledger row reverts the prose-lift-out and is rejected at plan-freeze.

Violation of (1), (2), or (4) is a Class-8-analog plan-authoring defect; detection routes via `computations/_shared/_source_reconciliation_audit.py` and emits SOURCE-RECON MANDATORY-halt severity.

## Schema

Each ledger row is a 3-tuple:

```
gate_id | session | sha256_of_plan_block
```

- **gate_id**: canonical gate identifier matching the plan-file gate block (e.g., `S{N}-RULE-FILE-V3-LANDING`, `W{w}-{n}`). The (gate_id, session) pair is the primary key — gate_id alone is not unique across sessions.
- **session**: zero-padded session label where the gate landed (e.g., `S{N}`).
- **sha256_of_plan_block**: SHA-256 over the plan-file gate block at plan-freeze time. Computed via `closure_hash(plan_block_text)` matching the `.claude/templates/script-template.py closure_hash()` audit-SHA pattern.

**Pending SHA exception**: a row MAY use `pending` as a placeholder ONLY when (a) the gate landed at plan-freeze but the SHA computation was deferred to a post-landing finalization pass, OR (b) the row records a user-authorized in-session cleanup whose plan-block is structurally undefined. Pending rows that do not satisfy (a) or (b) — e.g., in-session rule-corrections without a plan block, or forward-pinned carry-forwards for sessions that have not run — are NOT admissible and MUST be dropped at plan-freeze.

**gate_id validity**: a gate-ID without a corresponding plan-block in any session's plan file is structurally invalid. Such IDs cannot satisfy the schema's `matching the plan-file gate block` clause and are rejected at append-helper write-time.

## Cross-references

- **Ledger (canonical M4 lookup)**: `sessions/framework/registry/methodology-wave-allowlist-ledger.md`.
- **Per-instance rationale prose**: `sessions/framework/registry/methodology-wave-instances.md`.
- **M4 consumer**: `.claude/rules/wave-classification.md §M4`.
- **Sub-wave decomposition precedent**: the NROY clause of `wave-classification.md` — a MIXED wave splits into a COMPUTE sub-wave + a METHODOLOGY sub-wave, the latter producing a methodology-class allowlist row.
- **Dual-SHA closure pattern**: `.claude/templates/script-template.py` `closure_hash()` / `compute_dual_sha()` (audit-SHA derived from `closure_hash(input_pin_map)`; same protocol applies to `sha256_of_plan_block`).
- **Source-reconciliation audit**: `computations/_shared/_source_reconciliation_audit.py` scans both this rule file and the ledger for orchestrator-edit-discipline violations; emits MANDATORY-halt on detected subagent edits.
- **Append-helper canonical**: `computations/session-88/s88_w8_allowlist_append_helper.py` (single-shot Python `with open("a")` POSIX O_APPEND pattern for parallel-writer-safe row append). Forward helpers MUST write 3-column rows to the ledger and pair with a registry entry per Edit-discipline item 4.
