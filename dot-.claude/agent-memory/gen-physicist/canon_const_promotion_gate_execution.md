# Canonical-constant promotion gate — EXECUTION recipe (companion to the planning note)

Execution-side companion to [[stage0_hygiene_backfill_wave_planning]] (which covers PLANNING such a gate). This is how you EXECUTE a `CF-*-PROMOTE` artifact-existence value-landing gate that lifts a prior-session npz datum into `canonical_constants.py`.

## The non-obvious sequencing (AFTER-pattern, single PASS, no supersede)

`update_constant` is an AGENT knowledge-MCP call, NOT a Python function — the producing script CANNOT land the constant itself. Division of labor:
1. **Premise (two surfaces)**: `get_constant(name)` → "not found" AND `grep name canonical_constants.py` → ABSENT. Both must hold or it isn't a promotion.
2. **Verify the datum bit-exact BEFORE landing**: load the npz, compare via `float.hex(npz_val) == float.hex(literal)` — NOT just `==`. A decimal literal (e.g. `7.962`) is not binary-representable; the round-trip is lossless only because the prior producer wrote the same nearest-double. `float.hex` proves the identical IEEE-754 mantissa.
3. **Land via the agent MCP call** `update_constant(name, value='<literal>', session, source, gate, section_label, comment)` — pass `value` as a Python-expression STRING; this writes the assignment AND the PROVENANCE dict row AND makes it importable. Co-locate `section_label` with the sibling constant (e.g. `rho_s_C2`→SECTION E next to `J_C2`), not the SECTION-E default blindly.
4. **THEN run the producing script ONCE** — it does re-verify only (npz-SHA pin, npz bit-exact, `from canonical_constants import <name>` resolves, import==npz bit-exact, `PROVENANCE[name].session` present, source-text witness), computes dual-SHA, prints the payload. Running it BEFORE the landing gives a FAIL (import unresolved) → then a PASS → a polluted FAIL-then-supersede pair. Land-first ⇒ exactly one PASS line. This IS the registry-landing AFTER-pattern.
5. **emit_verdict(**payload)** (agent). `[AUDIT]` not `[SIGN]` ⇒ no 3-tuple; companion_row auto-written.

## Pins / SHAs
- `audit_sha256` pins the **POST-landing** `canonical_constants.py` bytes (the script reads it after the mutation) — value+provenance inseparable in the pin. The plan's precondition snapshot (`rho_s_C2` ABSENT state) is just the freeze-state pin, NOT what the audit SHA closes over.
- Build the pinmap with the npz STATIC SHA + landing-identity keys (`landing:name/value/session/source`) so the audit SHA uniquely IDs this landing (matches the plan `audit_discriminators`).
- `substitution_chain: required=false` — verbatim definitional-datum landing, no sign/direction claim (`math-scripts.md §"When the chain is NOT required"`).
- `publication_precision`: carry it (sig-figs + downstream `rel_tol ≥ 10^-sigfigs`) iff a downstream `[SIGN]`/verifier cites the value (Class 8.3).

## WP edit under a concurrent co-writer
The W0 WP is shared (mack writes §W0-2 concurrently). Edit ONLY your section; make `old_string` gate-ID-specific (contains your constant name) so it can't match the sibling section. Identical pending bodies across sections (e.g. the `**MCP Pre-Compute Audit**` pending stub) force you to span a contiguous block bounded by gate-unique anchor lines. Isolate-and-grep your section with `awk '/W0-1\. <GATE>/{f=1} /W0-2\. <SIB>/{f=0} f'` for the completion checklist (a whole-file grep for `Status.*COMPLETED` would falsely pass on the sibling's state).

S117 W0-1 instance: `rho_s_C2 = 7.962` (S48 GOLDSTONE-MASS-48), audit `55028ce0…`, PASS.
