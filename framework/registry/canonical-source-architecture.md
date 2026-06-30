# Canonical Source Architecture (S86 W14 + W12 OQ-2 surface)

> **Provenance**: S86 1a Slot S-6 architectural review (gen-physicist, 2026-04-27).
> Promotion of the W14-1..W14-6 + W12 OQ-2 surface findings to permanent
> framework-level architecture document.
>
> **Sole writer**: gen-physicist (META scope; not a falsifier-inventory entry).
> **Cross-references**: `computations/canonical_constants.py` (Section F PROVENANCE dict);
> `sessions/framework/registry/falsifier-master-inventory.md` (audit-pin sub-row schema);
> `.claude/skills/weave/SKILL.md` (`--update` Phase pipeline);
> `.claude/rules/math-scripts.md` §"Canonical Constants (MANDATORY)" (write-order rule).

## Two-Layer Canonical Source Model

The framework uses TWO STRUCTURALLY DISTINCT canonical registries, each with a
different consumer:

| Layer | File | Consumer | What it canonicalizes |
|:------|:-----|:---------|:----------------------|
| Import-canonical | `computations/canonical_constants.py` | computation Python scripts (`from canonical_constants import *`) | Scalar/array values + PROVENANCE dict |
| Audit-trail-canonical | `sessions/framework/registry/falsifier-master-inventory.md` | mack-cosmic-bridge (sole writer); downstream falsifier consumers; reader-facing detector-horizon table | Falsifier annotation: live-watch envelope, internal-consistency split, detector horizon, dual-pathway / band / pathway-keyed structure, full-64-hex audit pins |

These two layers are NOT interchangeable. The inventory is markdown — computation
scripts cannot import from it. The canonical_constants module is Python — it
cannot carry the cross-reference structure (PAIR-N annotations, audit-pin
sub-rows, detector horizons) the inventory requires.

## Forward-Canonical Write-Order: (1) verdict → (2) canonical_constants → (3) inventory

When a computation gate produces a new framework prediction value `P`, the canonical
write-order for downstream consumption is:

**Step 1 — Verdict-file emission** (mandatory; producing script):
```
{GATE_ID}: PASS|FAIL|INFO -- value=<P_value> scheme=<s> convention=<c> L_max=<L>
audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=R3
```
appended to `computations/s{N}_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md`.

**Step 2 — canonical_constants.py promotion** (mandatory; orchestrator OR
producing-script's post-write hook):
```python
update_constant("P_FW", P_value, session="S{N}",
                source="S{N}-{GATE_ID}", comment="<one-line provenance>")
```
which (a) adds `P_FW = P_value` to the appropriate Section (E for cosmological
observables; B for geometric; C for BCS; D for spectral action) and (b) adds
a PROVENANCE entry citing the verdict-line `audit_sha256`.

For STRUCTURED predictions (band, pathway-keyed, pivot-keyed), Step 2 expands
to multiple sub-keyed entries per the W14 precedents:
- Pathway-keyed: `P_FW_S{N}_<scheme>` per pathway (W14-4 f_NL family).
- Pivot-keyed: `P_FW_<param>_<value>` per pivot (W14-5 A_s family).
- Branch-keyed: `P_FW` (canonical) + `P_FW_<branch>` (alternative; W14-1 w_0
  Volovik-partition vs substrate-compaction R_842 dual).

**Step 3 — inventory row landing** (mandatory; mack-cosmic-bridge as sole writer
per `feedback_mack-bridge-role.md`):
- Append a new row to `sessions/framework/registry/falsifier-master-inventory.md` (or an
  audit-pin `<N>.audit` sub-row if the row already exists), citing BOTH the
  verdict-line audit_sha256 (full-64-hex) AND the canonical_constants entry
  name (e.g., "framework value = canonical_constants.P_FW").
- Carry the falsifier-side annotation (live-watch envelope, detector horizon,
  internal-consistency split, dual-pathway / band / pathway-keyed structure).

## Why this order

Under (1)→(2)→(3), computation scripts can begin consuming `P_FW` via
`from canonical_constants import P_FW` immediately after Step 2; the inventory
citation (Step 3) adds falsifier-side annotation but is not a prerequisite for
computation consumption.

Under the WRONG order (1)→(3)→(2) (the W14-1..W14-5 observed pattern), computation
scripts cannot consume `P_FW` until Step 3' completes — which may be one or
more sessions later, creating a window where the value is "canonical in
inventory but invisible to computation import". This is a registry-layer
constraint surface failure that consistently surfaces 5+ META gates in a
row before the gap is closed.

## Sync Enforcement

`/weave --update` Phase 2 (after `tools/extract_entities.py` rebuilds
`tools/knowledge-index.json`, before `tools/knowledge_db.py --sync`) invokes
`computations/_inventory_canonical_sync_audit.py` (S87+ infrastructure;
see `S87-WEAVE-UPDATE-INVENTORY-CANONICAL-SYNC-AUDIT`). The audit:
1. Parses `falsifier-master-inventory.md` and extracts the row-cited value
   names (e.g., w_0, α_s, ρ_AC / Ω_GW_LISA, f_NL_folded, A_s, dE_a).
2. Parses `canonical_constants.py` PROVENANCE dict via `ast.parse`.
3. Emits `tools/inventory_sync_audit.json` listing missing PROVENANCE
   entries + missing constants.
4. Returns INFO (not FAIL) so the audit does not block index rebuilds; the
   orchestrator consumes the report at session-start to dispatch in-session
   promotion gates.

## Audit-Pin Sub-Row Schema (PERMANENT)

The inventory's audit-pin sub-row pattern (rows `3.audit`, `7.audit`, `9.audit`,
`12.audit`, consolidated `21.audit-block`) is the canonical form for carrying
full-64-hex audit pins per `.claude/rules/gate-verdicts.md` while keeping the
primary-row cells human-prose-readable with 16-hex prefix form. This pattern
is PERMANENT, not one-time scaffolding. New inventory rows that cite multi-
source upstream chains (3+ pinned sources) should use the `<N>.audit-block`
consolidated form; single-source rows use `<N>.audit`.

## In-Session vs Carry-Forward Promotion

Per `feedback_fix-in-session-never-defer.md`: when an in-session gate
surfaces a missing canonical_constants entry that can be fixed with a single
`update_constant(...)` call, FIX-IN-SESSION (the W14-6 dE_a precedent).
When the gap requires primary-source recovery (W12 OQ-2 r_PathH PIN-DRIFT
class-(c)) or sub-keying decisions (W14-4 f_NL pathway sub-keying), generate
a 4-field carry-forward spec and queue for next session. The two routes are
the two halves of the no-technical-debt rule (CLAUDE.md §"No Technical Debt").

## Cross-References

- `feedback_fix-in-session-never-defer.md` — every synthesis must produce structured carry-forwards
- `feedback_fix-in-session-never-defer.md` — in-session promotion precedent
- `feedback_mack-bridge-role.md` — sole writer for inventory rows
- `.claude/rules/gate-verdicts.md` — full-64-hex audit-pin canonical form
- `.claude/rules/math-scripts.md` — canonical_constants import rule
- `.claude/rules/epistemic-discipline.md` — Source-Reconciliation 5-class taxonomy
- `computations/canonical_constants.py` Section F — PROVENANCE dict structure
- `sessions/framework/registry/falsifier-master-inventory.md` — audit-pin sub-row schema instances

## Provenance

- Architecture-document promotion: S86 1a Slot S-6 (gen-physicist, 2026-04-27).
- Surface-finding gates: W14-1 (FAIL, row-numbering-mismatch); W14-2 / W14-3 /
  W14-4 / W14-5 / W14-6 (5× PASS, audit-pin sub-row pattern); W12 OQ-2
  (r_PathH OPEN carry-forward); W14-6 (in-session dE_a promotion precedent).
- W14 working paper: `sessions/archive/session-86/session-86-w14-workingpaper.md`.
- W12 working paper: `sessions/archive/session-86/session-86-w12-workingpaper.md`.
