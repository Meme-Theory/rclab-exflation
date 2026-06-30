# Investigation 11 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed**: `investigation-1/{nazarewicz-nuclear-structure-theorist, neutrino-detection-specialist, paasch-mass-quantization-analyst, quantum-foam-theorist, volovik-superfluid-universe-theorist}.md` (5-agent survey batch; resolved to `--from`)
**Driver**: investigation-1 (the wholesale S108/S109 survey)
**Shape**: fanout (5 per-wave plan files)
**Verdict track**: `computations/investigation-11/inv11_gate_verdicts.txt` (compute/solo gates only; `emit_verdict(session=11, track="investigation")`)

The framework's single most-named gap — the ONE imported dimensional scale M_KK — attacked from four fresh vantages (nazarewicz BCS dimensional-transmutation, neutrino spectrum-forced predictions, quantum-foam Planck-scale suite, volovik two-fluid dark sector) + a cross-agent M_KK adjudication and compact-object-interior build. **paasch REUSED → workshop-only** (its entire next-step set is consumed by inv-3).

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | M_KK dimensional transmutation + Richardson pairing engine + ATDHFB τ_fold + Bayesian-UQ | nazarewicz-nuclear-structure-theorist | compute×4 | 4 | investigation-11-plan-w1.md |
| 2 | spectrum-forced neutrino predictions (sterile-null/ΔN_eff · mass triangle · transition-μ · M_R provenance) | neutrino-detection-specialist | compute×3, solo×1 | 4 | investigation-11-plan-w2.md |
| 3 | Planck-scale structure (dispersion bend · d_s–γ_E vs CDT · Wheeler-DeWitt Ψ(τ) · holographic K_pivot) | quantum-foam-theorist | compute×4 | 4 | investigation-11-plan-w3.md |
| 4 | two-fluid dark sector + broken BBN arm + de Sitter decay (coupled ODE · ρ_vac(q,T) · w_a · T-audit) | volovik-superfluid-universe-theorist | compute×3, solo×1 | 4 | investigation-11-plan-w4.md |
| 5 | M_KK adversarial adjudication + compact-object interior build | gen-physicist (neutral) | workshop×1, compute×1 | 2 | investigation-11-plan-w5.md |

Total: **18 gates** (15 compute + 2 solo + 1 workshop) across 5 waves. Honest workshop count: **1** (INV11-W5-1, nazarewicz↔paasch M_KK dimensional-transmutation-gap vs N(j)=7n integer-scheme).

**Plan-freeze validation (all PASS)**: upstream-pin validator exit=0, `n_mismatches=0`, `n_missing_npz=0` on all 5 waves (per-wave reports `investigation-11-plan-w{i}-validation.json`); YAML/PRDR validator 18/18 gates compliant (`n_fail=0` all waves; the W5-1 workshop gate's numeric-PRDR-N/A fields accepted under the non-compute-gate clause). Forward-pinned intra-investigation dependencies (W4-1←W4-2, W1-1←W1-2, W5-2←W4-2) are documented in each wave's Decision-Point Prerequisites, not as upstream npz pins.

**Gate-ID map** (for `/rclab-coordinate` dispatch):
- W1: INV11-W1-1 (M_KK BCS gap, FLAGSHIP) · INV11-W1-2 (Richardson pairing engine) · INV11-W1-3 (ATDHFB τ_fold) · INV11-W1-4 (Bayesian-UQ)
- W2: INV11-W2-1 (sterile-null + ΔN_eff) · INV11-W2-2 (abs-mass triangle) · INV11-W2-3 (Majorana transition-μ) · INV11-W2-4 (M_R provenance, **solo**)
- W3: INV11-W3-1 (dispersion bend) · INV11-W3-2 (d_s–γ_E vs CDT) · INV11-W3-3 (Wheeler-DeWitt Ψ(τ)) · INV11-W3-4 (holographic K_pivot)
- W4: INV11-W4-1 (two-fluid coupled ODE) · INV11-W4-2 (ρ_vac(q,T)) · INV11-W4-3 (de Sitter→w_a) · INV11-W4-4 (T-convention, **solo**)
- W5: INV11-W5-1 (M_KK adjudication, **workshop**) · INV11-W5-2 (compact-object interior)

Each per-wave plan is independently dispatchable: `/rclab-coordinate sessions/investigation/investigation-11/investigation-11-plan-w{i}.md`.
Full investigation: `/rclab-coordinate sessions/investigation/investigation-11/investigation-11-plan-index.md`.
