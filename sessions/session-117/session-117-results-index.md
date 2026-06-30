# Session 117 — Results Index (per-wave working papers)

**Date**: 2026-06-28
**Mode**: SESSION (fanout; mixed gate types — compute + one paired Stage-2 review per wave where applicable).
**Plan**: `sessions/session-plan/session-117-plan-index.md`
**Dispatch**: `/rclab-coordinate sessions/session-plan/session-117-plan-index.md`

Each per-wave WP is the team-lead's results shell for that wave (one pending block per gate; compute gates close via verdict line, the §VII.CK Stage-2 review gate via artifact-existence).

| Wave | Q | Theme | Working paper |
|:----:|:--|:------|:--------------|
| 0 | — | Hygiene backfill (provenance + falsifier landing) | session-117-w0-workingpaper.md |
| 1 | Q23 | A_s amplitude normalization (rate-limiter) | session-117-w1-workingpaper.md |
| 2 | Q18b | Yukawa / seesaw mass-spectrum | session-117-w2-workingpaper.md |
| 3 | Q18b | Lepton-CP & baryogenesis (W-1 campaign) | session-117-w3-workingpaper.md |
| 4 | Q3 | Leggett DM kinematics | session-117-w4-workingpaper.md |
| 5 | Q8/Q12 | Modulus a₄ gradient & WDW geometry | session-117-w5-workingpaper.md |
| 6 | Q30 | FWD-C2 L_emp bridge regulator-axes | session-117-w6-workingpaper.md |
| 7 | Q36 | w0 transport-degree & categorical-wall | session-117-w7-workingpaper.md |
| 8 | Q33 | §VII.AJ STATE-PROJ inter-summand | session-117-w8-workingpaper.md |
| 9 | — | e-fold substrate obligations (W-3 campaign) | session-117-w9-workingpaper.md |

**Total: 30 gates / 10 waves.**

## Verdict tracks
- **compute** gate verdicts → `computations/session-117/s117_gate_verdicts.txt` (dual-SHA closure per `.claude/rules/gate-verdicts.md`).
- **Stage-2 review** deliverable (W2 `CF-S117-VIICK-UNCONDITIONAL-REVERIFY`) → two synthesis docs under `sessions/session-117/` (artifact-existence; no verdict line; PASS-AND computed by orchestrator → mack flips §VII.CK UNCONDITIONAL).

## Plan-freeze validation (2026-06-28)
- **Upstream-pin validator**: 10/10 PASS (after 3 in-session fixes — w0 N/A-string regex false-positive, w3 gate-heading de-backtick, w4 phantom-npz repointed to canonical squeeze params). Reports: `session-117-plan-w{i}-validation.json`.
- **YAML PRDR validator**: clean across all 10 waves (`session-117-yaml-validation.json`).
