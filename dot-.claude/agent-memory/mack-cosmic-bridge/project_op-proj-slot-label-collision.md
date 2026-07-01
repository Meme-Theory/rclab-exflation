---
name: op-proj-slot-label-collision
description: §VII.AW.OP-PROJ (and the .OP-PROJ family) label is REUSED for structurally-distinct theorems in permanent-results-registry.md — resolve registry-landing targets by CONTENT, not by plan-cited line numbers
metadata:
  type: project
---

The `.OP-PROJ` suffix family in `sessions/permanent-results-registry.md` has at least one **reused slot label**: `§VII.AW.OP-PROJ` names TWO structurally-distinct theorems.

- `## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple (γ_F^c per Connes-Marcolli 2008 §11)` (the W-5 candidate (b) chirality slot; S90 W7 CF-45 scaffold). This is the chirality-candidate slot.
- `### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (S90 W2 CF-19)` — a DIFFERENT theorem, and the summary table row (top of registry) points at THIS clock theorem, not the chirality candidate.

**Why:** the registry's next-free-letter allocation was run independently in different waves (S90 W2 for the clock theorem; S90 W7 CF-45 for the chirality candidates) and the same letter (AW) was assigned to both. The `## ` vs `### ` heading level is the only structural disambiguator, plus the title.

**Disambiguation annotation LANDED (S92 W9-4 follow-up, 2026-05-23):** a `> **Slot-label note ...**` is now present at BOTH `§VII.AW.OP-PROJ` body headers (entry (1) SU(3)-Coloured at registry ~line 17509; entry (2) SUBSTRATE-CLOCK-UNIQUENESS-THEOREM at registry ~line 18322), each cross-pointing to the other by header title keyword, plus a `[LABEL SHARED — 2 entries: ...]` tag on the index-table row (~line 133). A full cross-file RENAME to a free §VII slot was NOT performed (orchestrator tracks it as a dedicated housekeeping item; rename touches cross-file cites = blast radius beyond the registry file). The annotation is the safe additive in-session fix; the underlying double-assignment persists until a tracked rename.

**How to apply (registry-landing sole-writer discipline):**
1. When a plan cites a `§VII.X.OP-PROJ` slot AND a line number, do NOT trust the line number — plan line numbers drift across sessions (S92 W9-4 plan cited 17237/17293; actual chirality blocks were at 17429/17485). Resolve by CONTENT (`grep` the slot header + read the block title) per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction.
2. When grepping a `.OP-PROJ` slot label, expect multiple hits. Disambiguate by title keyword (e.g., "Bi-Chirality" / "SU(3)-Coloured Chirality" / "Bridge Theorem" / "SUBSTRATE-CLOCK-UNIQUENESS"), not by position.
3. The chirality candidate family (S91 W7 substrate-physics FAIL diagnostics) lives at: §VII.AT.OP-PROJ = Bi-Chirality (γ_5 ⊕ γ_F direct-sum); §VII.AW.OP-PROJ = SU(3)-Coloured (γ_F^c); §VII.AQ.OP-PROJ = the PARENT (tensor-product γ_9 = γ_5 ⊗ γ_F), retained as the substrate's SOLE valid chirality structure.

Related: [[project_s92_w9_4_chirality_fail_diagnostic]].
