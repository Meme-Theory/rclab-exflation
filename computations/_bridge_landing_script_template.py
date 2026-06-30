#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bridge-Landing Script Template (single-shot pattern)
=====================================================

Provenance: S88 W3c-30 (S88-BRIDGE-LANDING-SCRIPT-ARCHITECTURE-REFINEMENT).
Status: METHODOLOGY-class deliverable per `.claude/rules/wave-classification.md`
        M1∧M2∧M3∧M4 conjunction. This file is a TEMPLATE; it does not execute
        a numerical PASS threshold and is NOT intended to be run as a gate.

Audit-trail context
-------------------
S87 W5-1, W5-2, W5-4, W5-5 (4 of 5 W5 dispatch gates) emitted a corrective
FAIL/INFO -> PASS double-trio in `computations/session-87/s87_gate_verdicts.txt`.
The structural cause is the BEFORE pattern below: scripts perform
    write -> re-read -> verify -> conditionally re-write/append
which produces a 2-trio (4-line) verdict-line group per gate (the FAIL line
+ companion comment row + corrective PASS line + companion comment row),
INSTEAD of the canonical single dual-SHA verdict line + companion row.

The S86 W1c-5 all-3-lines-retained discipline correctly preserves the audit
provenance of the corrective rewrites, but does NOT eliminate them at the
script-architecture level. This template enforces single-shot emission by
construction.

BEFORE pattern (4-of-5 W5 cause; produces FAIL/INFO -> PASS double-trio)
------------------------------------------------------------------------
```python
def land_bridge(plan_block, registry_slot):
    write_registry_entry(plan_block, registry_slot)              # (1) write
    actual_section = re_read_registry_at(registry_slot)          # (2) re-read
    if not verify_section_matches(actual_section, plan_block):   # (3) verify
        emit_verdict_line('FAIL', ...)                           # (3a) emit FAIL
        rewrite_registry_entry(plan_block, registry_slot)        # (3b) corrective rewrite
        actual_section_2 = re_read_registry_at(registry_slot)    # (3c) re-read
        if verify_section_matches(actual_section_2, plan_block): # (3d) re-verify
            emit_verdict_line('PASS', ...)                       # (3e) emit PASS (corrective)
        else:
            emit_verdict_line('FAIL', ...)                       # (3f) double-FAIL
    else:
        emit_verdict_line('PASS', ...)                           # (3g) emit PASS (clean)
```

Failure mode: emitting the verdict line BEFORE the corrective rewrite means
the audit trail shows TWO verdicts per gate (FAIL/INFO + PASS), each with
distinct dual-SHAs. The S86 W1c-5 rule keeps both retained (so the failure
+ remediation provenance is durable), but each registry-landing pollutes
the verdict file with a corrective trio that downstream consumers must
coalesce.

AFTER pattern (single-shot; this template's discipline)
-------------------------------------------------------
```python
def land_bridge(plan_block, registry_slot):
    promotion_text = build_promotion_text(plan_block, registry_slot)  # (1) build in memory
    write_atomic_with_fsync(promotion_text, registry_slot)            # (2) write + fsync
    actual_section = re_read_registry_at(registry_slot)               # (3) re-read
    verdict = ('PASS' if verify_section_matches(actual_section,
                                                 promotion_text)
               else 'FAIL')                                            # (4) determine
    emit_verdict_line(verdict,                                         # (5) emit ONCE
                      content_sha256(actual_section),
                      audit_sha256(input_pin_map))
```

Discipline: the promotion text is FULLY built in memory before any disk
write; the post-fsync re-read is the FINAL verification step (no
conditional retry permitted). FAIL emits FAIL once; PASS emits PASS once.
If the verify step uncovers a structural defect, the gate honestly closes
per `.claude/rules/mechanical-closure-discipline.md` rather than retrying
to PASS.

Cross-references
----------------
- `.claude/rules/registry-landing.md` (registry-anatomy conventions; this
  template's natural docking point — the SOURCE-DOUBLE-CITE-CO-PRIMARY
  schema benefits from single-shot emission).
- `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6
  ("iterate-until-PASS") — the BEFORE pattern's conditional rewrite is
  Class-6-adjacent: the corrective rewrite is permitted by the S86 W1c-5
  rubric only because the underlying content is unchanged across runs;
  the AFTER pattern eliminates the adjacency by construction.
- `.claude/rules/gate-verdicts.md` S87+ schema-v2 (dual-SHA + 3-tuple
  companion row) — single-shot emission writes ONE canonical line + ONE
  dual-SHA companion row + (if [SIGN] trigger) ONE 3-tuple companion row.
- `computations/_shared/_script_template.py` `append_verdict()` — the
  generic verdict-emission helper this template specializes for the
  bridge-landing case.

Audit-trail observation document
--------------------------------
The 4-of-5 W5 dual-trio enumeration with full 64-char SHAs is recorded in
`computations/_bridge_landing_audit_trail_observation_S87_W5.md`. Future
bridge-landing scripts using this template SHOULD cite that observation
in their docstring, mirroring the S86 W1c-5 calibration-corpus pointer
discipline.

Reference implementations
-------------------------
The S88+ landing scripts that adopt this template will look like:

```python
from pathlib import Path
import hashlib
import json

def build_promotion_text(plan_block, registry_slot):
    \"\"\"Produce the EXACT text to be written. Pure function; no I/O.\"\"\"
    # ... format the registry entry from plan_block + slot identity ...
    return text

def write_atomic_with_fsync(text, registry_slot_path):
    \"\"\"Write the file and fsync. Atomic via OS.\"\"\"
    p = Path(registry_slot_path)
    with open(p, 'w', encoding='utf-8') as fh:
        fh.write(text)
        fh.flush()
        import os
        os.fsync(fh.fileno())

def verify_section_matches(actual, expected):
    \"\"\"Strict equality (or normalized-whitespace match if so designed).\"\"\"
    return actual == expected

def emit_verdict_line(verdict, content_sha, audit_sha, gate_id, scheme,
                      convention, l_max='N/A', schema='R3'):
    \"\"\"Append a single canonical line + dual-SHA companion + 3-tuple if needed.

    Per `.claude/rules/gate-verdicts.md` S87+ schema-v2.
    \"\"\"
    # ... append exactly one canonical line + one dual-SHA companion ...
    pass
```

The verify_section_matches call in step (4) of the AFTER pattern is the
single point of decision; emit_verdict_line in step (5) is the single point
of emission. No conditional rewrite is permitted; a verify-FAIL emits FAIL
canonically and the gate closes honestly.

Closing note (M3 substrate)
---------------------------
Per `.claude/rules/wave-classification.md` §M3, this template's content
derives from a verbatim sub-diff from the S87 W5-1 dispatch-trace
observation + the S86 W1c-5 all-3-lines-retained rule. No first-principles
derivation is introduced; the substrate is the prior-closed observation.
"""
