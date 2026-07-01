---
name: memory-is-stale-snapshot
description: My agent memory is a point-in-time snapshot; recorded session verdicts and canonical_constants/knowledge-MCP win on any conflict.
metadata:
  type: feedback
---

When my memory conflicts with a session result, the SESSION RESULT wins — never the reverse.

**Why:** User correction (2026-05-29, capstone review): "your memory is a snapshot - don't take it over actual session results." My `open-problems.md` still listed α_s as "5.4× FAIL" and Weinberg as hard "FAIL"; both were SUPERSEDED (α_s resolved-as-channel-artifact, S93 W7-1, pivot +0.67σ). Reflexively trusting the memory table would have mis-reported the framework state. This is also `feedback_agent-roster.md` (agent memories are NOT framework-authoritative) and the project auto-memory note (verify state against registry/baseline/atlas, query knowledge MCP first).

**How to apply:** (1) Treat MEMORY.md / open-problems.md / paper-index numbers as OPERATIONAL PINS, not ground truth — always cross-check via `get_constant` / `search_knowledge` / the source doc before citing. (2) On conflict, flag it explicitly as "my snapshot is older; document/registry verdict stands," do NOT silently resolve, do NOT overturn a recorded verdict. (3) Authority order: recorded gate verdicts > knowledge.db/canonical_constants > my memory. (4) After noticing a superseded memory entry, prefer updating/removing the stale entry over acting on it. See [[open-problems]].
