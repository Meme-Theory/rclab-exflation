# Session 96 — Plan Index (fanout)

**Origin**: `/rclab-plan` over the 31-agent capstone review (`sessions/framework/equation-collab/`) + external second-opinion (`deep-research-report.md`). Carry-forward manifest: `session-96-context.md`. Partition: `session-96-partition.md`.
**Mode**: fanout (per-wave plan + per-wave WP). **Total: 8 waves, 53 gates.** All waves PASS `_plan_upstream_pin_validator.py` (exit 0) AND `_yaml_gate_validator.py` (PRDR-complete, FAIL=0).

## Waves

| Wave | Theme | Owner | Gates | Plan file | Validation |
|:-----|:------|:------|------:|:----------|:-----------|
| W1 | Emergent FRW `a(t)` closure (C1; FLAGSHIP, multi-session) | transit-dynamics-theorist | 7 | `session-96-plan-w1.md` | PIN✓ YAML 7/0 |
| W2 | SDW absolute-convergence & EFT-control (C2) | lizzi-spectral-functional-theorist | 6 | `session-96-plan-w2.md` | PIN✓ YAML 6/0 |
| W3 | NNLO Casimir EP + `Γ_grav/H_0` (C3 + D1) | gen-physicist | 3 | `session-96-plan-w3.md` | PIN✓ YAML 3/0 |
| W4 | `a₄` matter sector + seesaw (C6 + D5) | dirac-antimatter-theorist | 7 | `session-96-plan-w4.md` | PIN✓ YAML 7/0 |
| W5 | Geometry / causal / transition-order | schwarzschild-penrose-geometer | 7 | `session-96-plan-w5.md` | PIN✓ YAML 7/0 |
| W6 | Observational falsifiers + cosmogenesis (obs + D2, D4) | mack-cosmic-bridge | 7 | `session-96-plan-w6.md` | PIN✓ YAML 7/0 |
| W7 | Hygiene / pins / firewall + joint-evidence (C4/C5/C8 + D3) | gen-physicist | 9 | `session-96-plan-w7.md` | PIN✓ YAML 9/0 |
| W8 | Capstone consolidation & status-sync (external-review; RUN-EARLY) | gen-physicist | 7 | `session-96-plan-w8.md` | PIN✓ YAML 7/0 |

## Recommended run order
Per the external reviewer's "synchronize before getting more ambitious": **W8-1 (STATUS-SYNC) + W8-3 (HYGIENE-GATE) FIRST** (Wave-0 class), then the flagship **W1**, then W2–W7 in any order (independent), then the remaining W8 publication-discipline gates (W8-2/4/5/6/7). W3 is the CRITICAL focused wave (D1 `Γ_grav`).

## Plan-freeze obligation — METHODOLOGY allowlist appends (orchestrator-only)
12 METHODOLOGY-class gate-IDs are flagged for append to `sessions/framework/registry/methodology-wave-allowlist-ledger.md` (+ rationale rows in `methodology-wave-instances.md`), per `methodology-wave-allowlist.md` (subagent-edit-denied; orchestrator/user only). Append at plan-freeze before `/rclab-coordinate` classifies them METHODOLOGY:
- **W7**: S96-HYG-MELLIN-POLESET, S96-HYG-RK-FIREWALL, S96-HYG-SELF-INVENTORY, S96-HYG-KIND-TAG-S53, S96-HYG-CANONICAL-PINS, S96-HYG-D3-RESTRICT (7b), S96-HYG-CS2-REGISTRY (7 flagged).
- **W8**: S96-CONSOL-STATUS-SYNC, S96-CONSOL-3REGISTER-TABLE, S96-CONSOL-HYGIENE-GATE, S96-CONSOL-CITATION-ANCHOR, S96-CONSOL-MODULARIZE (5 flagged).
- COMPUTE-class (no allowlist): W8-4 DK-DF-EQUIV, W8-5 REPRO-BUNDLE, W7-1 FNL, W7-7a D3-COVARIANCE + all W1–W6 gates.

## Workshop-schedule routing (separate stream from this plan)
Per `Investigating-Workshops.md`, these dissonances are Q1 math/physics adjudications → workshop candidates (compute legs pre-registered here regardless): **D2** (GGE-relic-IS-CMB vs SCENARIO A — W6-6), **D3** (joint-evidence — W7-7a/b). D4 resolved by derivation (W6-3), not a workshop. The three independent `a(t)` closure routes in W1 (gates 1/4/5) seed an S97 cross-route-disagreement workshop if they diverge on `H²*`.

## Next step
`/rclab-coordinate sessions/session-plan/session-96-plan-index.md` (after the allowlist appends).
