---
name: capstone-hygiene-register-lags-verdict
description: capstone-hygiene Q3 when the binding register LAGS the verdict (spawn asserts a register fold not yet on disk) — verify on disk, narrate at the verdict level WITH explicit "fold pending" disclosure, route the unfolded register to its owner
metadata:
  type: feedback
---

When a designated-writer capstone-hygiene fold (Q3) cites an orchestrator-asserted register status ("the orchestrator has ALREADY folded atlas-08 Q23 / §EVOI.BF → CLOSED…"), VERIFY that fold on disk before narrating the capstone at that status. The spawn assertion is INTENT; the file is REALITY (AGENT OUTPUT MONITORING). If the binding registers (Atlas D04 `atlas-04-assumptions.md`, atlas-08 Q23, the D09 retraction log) still carry the PRE-result status on disk, the register LAGS the verdict — the opposite of the usual capstone-hygiene failure (capstone leading the evidence).

**Resolution shape (do NOT hold the capstone down to the stale register, do NOT silently lead it):**
1. Narrate MY sole-writer surfaces (`falsifier-master-inventory.md` + the §7 falsifier/observable surface) at the VERDICT level — faithful to the 3-tuple (e.g. `magnitude=PASS / regime=MARGINAL`), tag = the verdict status (e.g. "zero-parameter PASS, regime-MARGINAL"), NEVER "unconditional".
2. Carry an EXPLICIT "curated-register fold PENDING (atlas-08 Q23 / atlas-04 D04)" disclosure inside the landing itself, so the capstone does not silently exceed the on-disk register.
3. ROUTE the unfolded register folds back to their owners — atlas-08 Q23 = orchestrator-maintained; Atlas D04 = curated designated-writer (NOT a bulk append). Neither is my sole-writer domain. Flag via SendMessage to the team-lead, with the exact file:line of the stale status cell.

**Why:** the controlling authority for what the RESULT is = the verdict line (read on disk) + the explicit spawn directive; the binding registers are bookkeeping that can lag. The capstone-hygiene gate exists to stop the capstone from being MORE confident than the EVIDENCE — here the evidence (the PASS verdict) is ahead of the registers, so the fix is to fold the registers UP to the evidence, not to hold the capstone DOWN to stale registers. The explicit "fold pending" disclosure keeps me Q3-compliant (no section silently narrates above its register) while still delivering the directed update. Instance: S118 W1 A_s fork-closure (CF-S118-AS-CS-SUBSTRATE-FIRST PASS, audit `172c85be…`) — spawn said atlas-08 Q23 was folded to CLOSED zero-parameter regime-MARGINAL; disk showed Q23 line 249 still "OPEN (CRITICAL) … CF-S117-conditional" and D04 line 199 still "CONDITIONAL on CF-S117 … rate-limiting".

**How to apply:** every capstone-hygiene Q3 fold that cites an orchestrator/curated register status. Always grep the cited register cell on disk first. If lagged: narrate-at-verdict + fold-pending-disclosure + route-to-owner. Generalizes the (value, scheme)-tuple and discharge-status two-axis disciplines to the capstone-prose-vs-register-status axis. See [[vii-bridge-status-tag-multi-cell-reconcile]] (sole-writer surgical-patch mechanics) and the capstone-hygiene-gate.md Q3 routing.
