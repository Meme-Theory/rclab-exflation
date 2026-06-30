---
name: capstone-status-sync-gate
description: Pattern for capstone status-synchronization gates (reconcile curated-doc prose vs Atlas D04/D09 register tags) — reviewed-patch discipline + line-scoped forbidden-pattern re-grep + INFO-on-unreconciled-dissonance.
metadata:
  type: feedback
---

Pattern for METHODOLOGY-class capstone status-synchronization gates (e.g. S96-CONSOL-STATUS-SYNC: reconcile `sessions/framework/phonic-exflation-equation.md` prose against Atlas D04/D09 + registry + knowledge MCP).

**Why:** the capstone is a CURATED framework doc; status drift (a section narrating a claim at a confidence the register marks BROKEN/CONDITIONAL/RETRACTED) is a real scholarly issue, and the fix is a reviewed targeted patch, never a bulk append.

**How to apply:**
- **Status tags are READ, not derived.** Query the knowledge MCP first (`search_knowledge`/`get_constant`), then read the Atlas register files directly for the categorical tag. Transcribe; do not recompute. The register IS the ground truth.
- **Apply the prose patch BEFORE running the producing script.** The script's job is to VERIFY (re-grep the patched capstone for forbidden patterns) + emit the JSON status-diff + dual-SHA verdict. content_sha256 is over `script-bytes || applied-diff-bytes` (the METHODOLOGY-class F-image per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`), NOT script-only.
- **Forbidden-pattern re-grep must be LINE-SCOPED, not file-global.** A "never thermalizes" match is admissible iff its LINE also carries a scope token (`BROKEN`, `transit`, `T3`, `item 16`, `Hubble`, `cosmological`, `diabatic`). The trap: your own reconciliation clause QUOTES the BROKEN phrasing ("NOT the BROKEN-T3 'never thermalizes at Hubble time' claim") — that quoted form still matches the bare regex, so scope-token-on-same-line is the right admissibility test, not "regex absent."
- **Sole-writer boundary is load-bearing.** gen-physicist owns prose (§5.3/§6.2/§7.1-prose/§7.3); the §7.2 falsifier-TABLE belongs to mack-cosmic-bridge. If reconciliation finds a §7.2 cell needing change, emit a `→ mack/W8-2: §7.2 row X status Y→Z` hand-off line in the WP and leave the table untouched. (S96: no §7.2 cell needed a change.)
- **INFO is the honest verdict when a dissonance is a genuine math/physics adjudication (Q1-YES).** D2 (GGE-IS-CMB vs hot-big-bang) and D5 (no-seesaw vs S60 seesaw) cannot be closed by a status-tag edit — route them forward (add a "STATUS: unreconciled → W6/W4 gate" pointer in the prose, record as forward-routed compute item in the status-diff) and emit INFO, NOT a forced PASS. PASS-core (table complete + diff partitioned + 0 forbidden + must_contain present) can hold simultaneously with INFO.
- **output-standards.md numerical-vs-structural split:** the status-diff MUST have `## (a) Numerical revisions` (σ-band re-pins transcribed verbatim) and `## (b) Structural changes` (status-tag reclassifications / epistemic-type changes) in SEPARATE sub-sections; neither empty if its class has members.
- **D1-class "dual-listing" reconciliation:** when the knowledge graph lists a gate BOTH as a defined PASS gate AND as UNCOMPUTED-CRITICAL, check the latest session verdict file — the margin may already have landed PASS (S96 D1: LEGGETT-GRAV-DECAY-CONDITIONAL PASS in S95, Γ_grav/H_0~8.85e-66). "CRITICAL-uncomputed" is then the stale reading; reconcile to "CONDITIONAL-and-satisfied."

Cross-refs: [[pipeline_status_aware_registry_audit]] (the sibling status-aware audit pattern — read-status-from-header-not-body, literal-PASS-first precedence).
