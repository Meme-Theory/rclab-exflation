# Session 118 — Results Index (fanout)

**Date**: 2026-06-29
**Plan**: `sessions/session-plan/session-118-plan-index.md` · **Dispatch**: `/rclab-coordinate sessions/session-plan/session-118-plan-index.md`
**Verdict file**: `computations/session-118/s118_gate_verdicts.txt` (canonical).

Per-wave working papers (shells; runtime agents fill the pending blocks at `/rclab-coordinate` time):

| Wave | Theme | Owner | Gates | Working paper |
|:----:|:------|:------|:-----:|:--------------|
| 0 | Registry-hygiene (mack-surface patches) | mack-cosmic-bridge | 3 | `session-118-w0-workingpaper.md` (93 ln) |
| 1 | A_s amplitude closure | transit-dynamics-theorist | 2 | `session-118-w1-workingpaper.md` (69 ln) |
| 2 | Lepton-PMNS joint admissibility | neutrino-detection-specialist | 1 | `session-118-w2-workingpaper.md` (43 ln) |
| 3 | Spectral-functional + WDW residuals | lizzi + feynman (executors) | 2 | `session-118-w3-workingpaper.md` (71 ln) |

8 gates / 4 waves. Each WP shell carries one pending block per gate (4-tuple + PASS/FAIL/INFO criteria + dual-SHA + MCP Pre-Compute Audit placeholder), zero `Runtime agent fills` stubs, and the four footer sections (`## Wave {W} Synthesis`, `## Carry-Forward Computations`, `## Constraint-Map Updates`, `## Files Produced`).

---

## Verdicts (final — all 4 waves closed)

| Gate | Wave | Verdict | audit_sha256 | Note |
|:-----|:----:|:--------|:-------------|:-----|
| `CF-S118-HK-ALPHAS-LABEL-CONSISTENCY` | 0 | **PASS** | `b6cb6c01…` | α_s four-label SCALE-AND-CHANNEL annotation (Branch A) |
| `CF-S118-HK-VIICK-D4-SCOPE-TOKEN` | 0 | **PASS** | `3dd1ff10…` | §VII.CK D4 coset-shift scope-token (NOT Z₃) |
| `CF-S118-HK-ROW79-DISCHARGE` | 0 | **PASS** | `aeb5c2b9…` | 170× DM-mass kinematic discharge (3 axes) |
| `CF-S118-AS-CS-SUBSTRATE-FIRST` | 1 | **PASS** ⭐ | `172c85be…` | **headline** — c_s=0.5685 ∈ GS-1 window ⇒ A_s closes zero-parameter (3.2994e-9, regime-MARGINAL) |
| `CF-S118-ALT-GREYBODY-WALL` | 1 | **FAIL** | `66910a55…` | WALL-STRENGTHENED-4-CLASS-EMPIRICAL (pre-reg) → `CF-S119-GREYBODY-NOGO-PROOF` |
| `CF-S118-PMNS-JOINT-ADMISSIBILITY` | 2 | **PASS** | `85520aa6…` | lepton under-determination survives joint NuFIT box (f_adm_free=6.85e-5) |
| `CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN` | 3 | **INFO** | `fb15f24e…` | OQ-4 "suppressed" (rel_span(ξ_F*)=0.0391≤0.05; pre-reg) |
| `CF-S118-WDW-S0-ONGRID` | 3 | **PASS** | `95b559c1…` | WDW W(0)=0 on-grid (cosmetic INFO→PASS label upgrade) |

**Tally**: 6 PASS / 1 FAIL / 1 INFO (FAIL + INFO both pre-registered outcomes). sig_5: 8/8 distinct audit SHAs.
**New canonical constant**: `c_s_a2curv_GGE_fold = 0.5685294372062244` (S118 W1-1).
**Carry-forward**: `CF-S119-GREYBODY-NOGO-PROOF` (W1 WP §"Carry-Forward Computations" + housekeeping §B).
**Registers updated**: EVOI §EVOI.BF (A_s + L_emp) · atlas-08 Q23/Q18b/Q12/CF21 · atlas-04 D04 · falsifier-master-inventory Row #12/#79 · capstone §7.1/§7.2 · housekeeping ledger (§A ×12, §B ×1).
