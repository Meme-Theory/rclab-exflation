---
name: shared-wp-writer-unique-anchor
description: Shared per-wave WP section writes MUST anchor on the §-header, never on stub boilerplate that repeats across sections
metadata:
  type: feedback
---

When writing MY section into a shared per-wave working paper (`session-N-wW-workingpaper.md`) under concurrent sibling-agent writes, a Python read-modify-write helper MUST scope edits by the SECTION HEADER (`### §Wx-y. <GATE-ID>`), never by stub boilerplate.

**Why**: S95 W6-2. The §W6-1 and §W6-2 stubs shared IDENTICAL pending boilerplate ("**Output Artifacts** ... YAML)" + the Results-pending sentence). My writer used `txt.index(OLD_BODY_START)` on that non-unique anchor; `str.index` returns the FIRST match — which was §W6-1's body, not §W6-2's. My COMPLETED BAO content overwrote the (not-yet-run) §W6-1 stub, the §W6-2 header was consumed, and the file mis-attributed my content. Fixed in-session with a header-scoped repair (restore §W6-1 stub + reinsert §W6-2 header).

**How to apply**:
- Compute the section span as `txt[index(THIS_HEADER) : index(NEXT_HEADER)]` FIRST, then do replacements ONLY inside that span. Both headers are unique (gate-ID-bearing).
- The Edit tool is mtime-conditional and FAILS under parallel writers (it errored twice before I switched to a Python writer) — use a single atomic `read → str-ops → write_text` with a short retry loop (re-read each attempt).
- Make the writer idempotent: early-return if my COMPLETED marker already present.
- Related: [[project_substrate-not-c-limited]] is unrelated; this pairs with the registry-write-hygiene parallel-writer-race discipline (append-only Python writers, not Edit round-trips) already in MEMORY.md Debugging Notes.
