# Session 101 — Plan Index (fanout mode)

**Frozen**: 2026-06-07 (plan-freeze). **Prior**: S100a/S100b dual campaign.
**Corpus**: `session-101-context.md` (40-item deduplicated CF table, BINDING-source-cited) + `session-101-partition.md` (8-wave manifest + cross-wave pins).
**Verdict file (all gates)**: `computations/session-101/s101_gate_verdicts.txt` via race-safe `emit_verdict`.
**Validation**: `_yaml_gate_validator.py` PASS 44/44 across 8 files; `_plan_upstream_pin_validator.py` PASS ×7 + ACCEPTED-RESCUE ×1 (W1 — in-wave forward pin `s101_tau0_operator_canonicity.npz`, rationale annotated at the pin); npz-existence sweep (`computations/session-101/s101_plan_freeze_npz_existence_sweep.py`): 49 upstream refs verified on disk, 0 missing, 44 forward-pinned s101 outputs expected-absent.
**Allowlist** (plan-freeze appends, orchestrator-effected via `computations/session-101/s101_plan_freeze_allowlist_append.py`): 3 METHODOLOGY rows landed in `methodology-wave-allowlist-ledger.md` + paired rationale entries (S101-HK-SELECTION-RULE-PREFLIGHT-RULE `79d4c73c…`, S101-HK-SUFFIX-DISCIPLINE `e7bef692…`, S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION `8a58c9ea…` — SHAs frozen over the w8 plan blocks; do not edit those blocks post-freeze).

## Run-order (hard edges)

```
W1  →  { W2, W5 }          (W1's L4 leg lifts the A19 caveats; pre-lift dispatch carries the extra-row)
W6  →  W7                  (Stage-2 verifies consume the W6 Stage-1 landings; reviewer-exclusion audit at the boundary)
W3, W4, W8 independent     (W8 internal serialization W8a-1 → W8a-2 → W8b-1..3 → W8a-3-optional)
```

## Waves

| Wave | Theme | Owner (planner) | Gates | Plan file | Lines |
|:-----|:------|:----------------|:------|:----------|:------|
| W1 | τ=0 canonicity chain + spectral envelope pins (LC suite L1–L5 + dormant K-annex; LC pole cert; prong-B window; §VII.AM α-pin) | connes-ncg-theorist | 4 | `session-101-plan-w1.md` | 1025 |
| W2 | Texture-cluster magnitude axis (BLOCKTRACE AMENDED → 3-leg CARRIER → S0-KNOB; quark orientation; star-metric lemma; disconnect boundary) | baptista-spacetime-analyst | 6 | `session-101-plan-w2.md` | 1608 |
| W3 | Neutrino/flavor (S-3 Dirac trio; D5 gap-eq DERIVATION; Z₃ rephasing; CCS-KO → PS-RGE sequenced; MR-ROUTE-B HOLD) | dirac-antimatter-theorist | 7 | `session-101-plan-w3.md` | 1875 |
| W4 | Cosmology corridor + DE/H₀/M₀ (QEQ probe pair; branch-iv evaluator pre-DR3; H₀-PROPER-A2 MANDATORY; M₀-BCS) | volovik-superfluid-universe-theorist | 5 | `session-101-plan-w4.md` | 1132 |
| W5 | Transit/GGE + flat-band + LRD (β² tuple-pinned promotion → ladder; tricritical; B2 dual-prior; AF1 Mode-A; LRD per-z) | transit-dynamics-theorist | 6 | `session-101-plan-w5.md` | 1447 |
| W6 | Registry-landing batch (6 bridge-landings AFTER-pattern + PMNS promotion + Y₁=0 line; slot-lockfile pre-dispatch step; mack sole-writer dispatch slot) | gen-physicist | 8 | `session-101-plan-w6.md` | 1762 |
| W7 | Stage-2 verification cohort (BM.STATE-PROJ verify, connes EXCLUDED; Schur-rigidity verify, berry+successors EXCLUDED; W6→W7 boundary reviewer-audit) | gen-physicist | 2 | `session-101-plan-w7.md` | 948 |
| W8 | Methodology/audit extensions (W8a/W8b sub-split; detector creation disclosed; 3 allowlisted rule diffs; optional ANALYTIC-HM drop-first) | gen-physicist | 6 | `session-101-plan-w8.md` | 1752 |

**Total: 44 gates** (40 corpus items; W8 sub-split SELECTION-RULE-PREFLIGHT into -AUDIT/-RULE per the MIXED-class NROY clause; W3 carries the HOLD as a decision-table entry, not a gate).

## Standing holds + deferrals (NOT gates this session)

- **MR-TEXTURE-ROUTE-B** — CONDITIONAL-HOLD (trigger not fired; upstream producer = W3 gates 2/4; S102 re-open clause in the W3 decision table).
- **H-parity Stage-2 cross-axis verify** — S102, AFTER `S101-W1-QEQ-RELIC-ODDFLOOR` lands (FAIL routing amends the Stage-1 entry first; volovik+transit excluded).
- **Route-D Stage-2** — queued post-landing (exclude the S100a-W4-15 authorship lineage).
- Standing gaps per EVOI §6: C2 K_pivot mapping; τ_fold-RELAXATION; CF21 TD/LI H̃-divergence (Q1 workshop-class); Q44 Sagan re-anchoring (workshop-class).

## Session-close obligations (pre-registered now)

- mack-cosmic-bridge dispatch slot (W6): W-4 D5 register drafts T1–T5/A1–A3 + S-2 Row #81 four-surface batch; Row #81 re-pins on the W4 H₀ landing; capstone §7.3 D5 cell moves off `unreconciled` at that landing; capstone-hygiene 5-question gate runs at session close.
- Capstone genesis-prose Q3 routing fires AFTER `S101-TAU0-OPERATOR-CANONICITY` lands (tau0 workshop (vi-d) ROUTED note).
- A19 caveat-lift mechanics: lifts are APPENDED (never edited in); s100b caveat rows at verdict-file lines 59/78/83/95 remain on disk per verdict permanence.

**Next step**: `/rclab-coordinate sessions/session-plan/session-101-plan-index.md`
