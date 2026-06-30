---
name: plan-authoring-r3-yaml
description: Pipeline-compliance lessons for authoring per-wave R3 YAML gate blocks (session-{N}-plan-w{i}.md) and validating them with _yaml_gate_validator.py
metadata:
  type: feedback
---

Recurring lessons from authoring fanout per-wave plan files (`session-{N}-plan-w{i}.md`) with R3 YAML gate blocks. Applies to ANY plan-authoring dispatch (cross-domain workhorse niche).

## Rule 1 — No nested double-quotes inside a double-quoted YAML scalar

**Why**: registry/corpus section names carry the `§"..."` form (e.g. `§"Cross-cutting execution constraint"`). Putting that inside a double-quoted YAML scalar (`proof_ref: "... §"Cross-cutting...""`) breaks `yaml.safe_load` with `expected <block end>, but found '<scalar>'`. Cost me one extra Edit round at S93 W9 plan-freeze (W9-6 `boundary_reachable_analytically.proof_ref`).

**How to apply**: for any `proof_ref` / `description` / long-prose YAML field that must mention a `§"..."` section name OR an apostrophe-heavy phrase, use a YAML **block scalar** (`>` folded or `|` literal), NOT a quoted scalar. Block scalars need no quote-escaping. The W9-3 gate's `proof_ref: >` is the good template; copy that shape. Strip inner double-quotes around section names (write `§Cross-cutting-execution-constraint`, not `§"Cross-cutting execution constraint"`).

## Rule 2 — _yaml_gate_validator.py double-counts: markdown FAIL + yaml PASS is EXPECTED, not a defect

**Why**: the validator parses BOTH the `## §W{i}-N. {GATE_ID}` markdown heading AND the fenced ```yaml block as separate "gate" candidates. Every gate therefore appears twice: once as `UNIDENTIFIED-W{i}-N [markdown] FAIL missing=[all 8 keys]` and once as `{GATE_ID} [yaml] PASS`. The TOTAL line reads `PASS=N FAIL=N` for an N-gate wave. This is the SAME for every sibling fanout plan (verified against session-93-plan-w2.md: 4 markdown FAIL + 4 yaml PASS).

**How to apply**: success criterion = ALL fenced YAML blocks show `[yaml] PASS` AND yaml-gate-count == number-of-gate-sections. IGNORE the `[markdown] UNIDENTIFIED-* FAIL` lines — they are the heading-parse artifact. sig_4 of the v3 ladder keys on the YAML PASSes (schema_version: R3 + all 8 PRDR items present). Do NOT try to "fix" the markdown FAILs by removing section headings.

**S110 W4 UPDATE — the double-count is SUPPRESSED when every block parses cleanly.** `_body_has_valid_yaml_gate()` (validator line 278) suppresses the phantom UNIDENTIFIED markdown gate IFF the block's YAML `safe_load`s. So a clean N-gate plan reports `gates: N (markdown=0, yaml=N)` and `PASS=N FAIL=0` — NO double-count. A `markdown=1` (or any phantom `UNIDENTIFIED-*`) in the header is now a SIGNAL that one block failed `yaml.safe_load` (see Rule 1 / Rule 5) — it dropped from yaml-gates and reappeared as a markdown phantom. Diagnose immediately, do not dismiss as the "expected double-count."

## Rule 5 — [SIGN]/[CHAIN]-gate exemption-phrase trap in substitution_chain.content

**Why**: `_chain_satisfied()` (validator line 127) makes a DIRECTIONAL gate ([SIGN]/[CHAIN], the `DIRECTIONAL_TRIGGERS` set) FAIL its `substitution_chain` check if the `content` matches `CHAIN_EXEMPTION_RE` = `no\s+(sign|direction|threshold)\s+claim | definitions?[- ]only | exempt\s+per\s+math[- ]scripts | structural[—:-]no directional claim | N/?A[—:-]?(structural|definitions?|existence)` — even when the gate's PRIMARY claim IS directional and the exemption phrase only describes a NON-directional sub-leg. S110 W4 CF-AS3-QUENCH-PIN ([SIGN], 3 legs) FAILed because its Note (C) prose said "(no sign claim)" for the Penrose-Diósi magnitude sub-leg, while the gate's leg-B IS the directional claim. (DMAB also carried the phrase but happened to pass — do not rely on that; fix all occurrences.)

**How to apply**: in a multi-leg [SIGN]/[CHAIN] gate, NEVER write "(no sign claim)" / "definitions-only" / "N/A — structural" in the chain content for a sub-leg. Reword: "(not a directional prediction)", "(a regime label / scale-comparison, not directional)", "[the gate's directional content is leg B above]". [VERIFY]/unknown triggers are SAFE (exemption phrase HELPS them: `chain_nonempty OR exemption`). [VERIFY-THEOREM]/[AUDIT] auto-exempt — `substitution_chain: {required: false}` with NO content block is accepted (no chain needed; do not add prose that could trip other audits).

## Rule 3 — Validation environment

- Run the validator with ABSOLUTE paths, NO `cd`, NO `&&` compound (project denies `cd` and the compound triggers a permission prompt): `"<venv>/python.exe" "<abs>/_yaml_gate_validator.py" "<abs>/plan-file.md"`.
- The GPU venv `phonon-exflation-sim/.venv312/Scripts/python.exe` has pyyaml 6.0.3 installed.
- To debug WHICH block fails to load, run a standalone `re.findall(r"```yaml\n(.*?)```", text, re.DOTALL)` + per-block `yaml.safe_load` — the validator's aggregate output doesn't tell you which block broke; the standalone loop does.

## Rule 4 — Per-gate house style (match the sibling fanout plan, cite it)

Per-wave plan files share the W2-sibling shape: fenced ```yaml block per gate; 4-field Identity; full 8-item PRDR; `output_artifacts` with `must_contain` regex + verdict_line `audit_sha256=[a-f0-9]{64}`; PASS/FAIL/INFO rubric prose; substrate_framing; and a trailing `# ---- METHODOLOGY-class M1-M4 self-classification ----` comment block for METHODOLOGY/MIXED gates with the `***FLAG FOR ORCHESTRATOR ALLOWLIST APPEND***` marker. Required wave-level sections: Summary, Decision Point Prerequisites (table), §W{i}-N gate blocks, Wave→next Decision Point, Machinery-Enumeration Pin (table), Input-SHA Ledger (table). Use `verdict_source` / canonical path `computations/session-{N}/s{N}_gate_verdicts.txt`, NEVER `expected_verdicts`.
