# Session 103 — Plan Index (fanout mode)

**Frozen**: 2026-06-10 by `/rclab-plan --session 103`. **Gates**: 15 dispatchable across 4 gated waves (+ 1 NOT-DISPATCHABLE declaration wave). **Verdict file (all gates)**: `computations/session-103/s103_gate_verdicts.txt` via race-safe `emit_verdict`.
**Corpus**: `session-103-context.md` (16 items; S102 WP CF blocks, campaign-enriched 2026-06-10) + `session-103-partition.md`.
**Validation at freeze**: upstream-pin validator exit 0 ×5 (`session-103-plan-w{i}-validation.json`; n_mismatches=0, n_missing_npz=0); R3 YAML validator PASS 7/4/2/2 (planner-run); plan-freeze corrections: W1-4 patch-text source re-anchored to the S-4 berry synthesis (§IV.3 verified at its line 137); W2 `dirac_spectrum.py` path fix + `peel_heldout` §(ii.B) drift pre-documented.

| Wave | Theme | Owner (planner) | Gates | Plan file | Working paper |
|:-----|:------|:----------------|:------|:----------|:--------------|
| W1 | Registry landings + curated patches (sole-writer cluster; §VII.BV–BY slots; intra-wave edge W1-4 → W1-5) | gen-physicist | 7 | `session-103-plan-w1.md` | `../session-103/session-103-w1-workingpaper.md` |
| W2 | NCG / spectral registry refinement + external validation (incl. §VII.BT Stage-2 PASS-AND: Axis-A lizzi / Axis-B volovik) | connes-ncg-theorist | 4 | `session-103-plan-w2.md` | `../session-103/session-103-w2-workingpaper.md` |
| W3 | Transit / holonomy (`[SIGN]` F_amp exact-edge re-pin; coset2 executor = berry-geometric-phase-theorist) | transit-dynamics-theorist | 2 | `session-103-plan-w3.md` | `../session-103/session-103-w3-workingpaper.md` |
| W4 | Fermion-mass sector — **NOT-DISPATCHABLE** (δA construction unpinnable at plan-freeze; Class-8 honest declaration; gate ID `S103-NU-DELTA-A-FIBRE-GEOMETRY` reserved-not-consumed) | neutrino-detection-specialist | 0 | `session-103-plan-w4.md` | — (no shell; no gates) |
| W5 | Cosmology / DE / observational surface (branch-iv feasibility-gated at the p+q≥13 wall; Q28-A₆ pre-fixed COMMIT/WITHDRAW) | mack-cosmic-bridge | 2 | `session-103-plan-w5.md` | `../session-103/session-103-w5-workingpaper.md` |

**Run-order edges**: W1 internal 4→5 (hard: the B2-ISOBREAK companion cites the patched §VII.BR clause). No hard cross-wave edges; W3-2 companion-strengthens W1-5 non-blocking. W1/W2/W3/W5 dispatch-independent.
**Registers at freeze**: EVOI re-stamped S103 (audit PASS lag-0; §6 = this queue); atlas-08 S102 freshness pass + backing audit landed; open-channel-ledger refreshed; atlas-04 verified (C4 annotation only); m_H Route-B 131.8 GeV re-pin landed on the mack surfaces (atlas-04 §IX row 8, capstone §7.1 ×2, open-channel §D; audit `75ed7ffb`).
**Standing gaps (EVOI §6, NOT waves)**: M_KK-DERIVATION (also the genus SCALE-branch dissolution path); K_pivot/C2; τ_fold-RELAXATION; M8(c); **CF-coldread-4 math-paper extraction — gate condition SATISFIED, user capacity decision**; DESI-WZ-LENSING-BIAS; MR-TEXTURE-ROUTE-B; CF21; Q33/Q30/Q36; Q44.
**Next step**: `/rclab-coordinate sessions/session-plan/session-103-plan-index.md`
