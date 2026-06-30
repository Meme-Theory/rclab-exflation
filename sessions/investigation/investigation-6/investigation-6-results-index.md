# Investigation 6 — Results Index (per-wave working papers)

**Date**: 2026-06-14
**Seed (`--from`)**: `investigation-1/{dirac-antimatter-theorist, kaluza-klein-theorist, feynman-theorist}.md`
**Plan**: `investigation-6-plan-index.md`
**Mode**: fanout — one WP shell per wave. Each shell is a thin pending-block scaffold; runtime agents fill the `*(pending — include: ...)*` contracts at `/rclab-coordinate` time. compute gates close with a dual-SHA verdict line on the investigation track (`computations/investigation-6/inv6_gate_verdicts.txt`); the W4 workshop closes by artifact-existence.

| Wave | Theme | Working paper | Gates |
|:----:|:------|:--------------|:-----:|
| 1 | KK scale-bracket & moduli stabilization | `investigation-6-w1-workingpaper.md` | 4 compute |
| 2 | Quantum-loop gravity sector & A_s normalization | `investigation-6-w2-workingpaper.md` | 5 compute |
| 3 | Baryogenesis, CPT & the antimatter sector | `investigation-6-w3-workingpaper.md` | 4 compute |
| 4 | M_KK determination-route reconciliation | `investigation-6-w4-workingpaper.md` | 1 workshop |

**Total: 14 gate sections** (13 compute pending-block sets + 1 workshop artifact-existence checklist).

Dispatch the full investigation: `/rclab-coordinate sessions/investigation/investigation-6/investigation-6-plan-index.md`

## Verdicts (landed 2026-06-15)

All 14 gates closed — 13 compute (verdict lines in `computations/investigation-6/inv6_gate_verdicts.txt`) + the W4 workshop (artifact-existence, `workshops/m-kk-determination-route-reconciliation.md`). **2 PASS · 6 FAIL · 5 INFO · 1 workshop-LANDED** (FAIL/INFO are constraint-map results, not failures). Recovery note: this dispatch survived a usage-quota wall + a transient infra throttle + an AUP false-positive — every casualty was re-run; no verdict lost, no verdict double-fired (W1-4 carries a clean Option-A supersession; canonical = de92408b).

| Gate | Verdict | One-line |
|:-----|:--------|:---------|
| INV6-W1-1 | INFO | gauge-vs-gravity bracket REAL (6.79×); A_s 3.15-OOM gap ⊂ a₀-band |
| INV6-W1-2 | INFO | Casimir-volume NULL (no minimum) → §VII.BS rank-1 import confirmed |
| INV6-W1-3 | FAIL | KK-tower can't reach SM couplings from single α⁻¹ (Cartan Identity exact) |
| INV6-W1-4 | INFO | Z₂ BCS-amplitude domain-wall soliton — first compact-object-like structure |
| INV6-W2-1 | PASS | Γ[τ] one-loop: M_KK loop-self-consistent (gravity sector) = M_KK_gravity |
| INV6-W2-2 | FAIL | A_s +1.455 OOM, K_pivot=0.975 (4th A_s route; REGIME-bounded) |
| INV6-W2-3 | FAIL | emergent gravity = Wilsonian EFT (1/ε-divergent), not finite QG |
| INV6-W2-4 | PASS | emergent Lorentz holds (O(k⁴) Goldstone; LIV bound; CPT-odd null) |
| INV6-W2-5 | INFO | graviton d_s→8.46 (no UV dimensional reduction; antipodal to d_s→2) |
| INV6-W3-1 | FAIL | η_B GGE-rescattering capped (R_enh≤1 at φ_CP=π/2) |
| INV6-W3-2 | INFO | CP-source rank-1 = φ_88 (forecloses source-multiplicity η_B rescue) |
| INV6-W3-3 | FAIL | η_B acoustic-Schwinger capped (exp(−S)≤1; fold at 93% of ceiling) |
| INV6-W3-4 | FAIL | single-domain antimatter sound-horizon test |
| INV6-W4-1 | LANDED | M_KK: ONE-ROUTE-DOMINATES (gravity-a₂, 7.4287e16); §VII.BS rank-1 confirmed; value held pending gauge-a₄ gate |

**Headline structural results**: emergent gravity is a Wilsonian EFT with no UV dimensional reduction (W2-3+W2-5 coherent); both η_B-enhancement mechanisms FAIL convergently → deficit localized to the CP-bias/σ_supp normalization, with the CP source proven rank-1 (W3-1/W3-2/W3-3); the M_KK gauge-vs-gravity tension dissolved into rank-of-import (proven ONE) vs canonical-value (gravity-a₂), with one decisive gate (W4).

**Carry-forwards + housekeeping**: `investigation-6-housekeeping.md` (§B session-track promotions + capstone-hygiene 5-question gate + the infra-recovery process observations) + each WP `## Carry-Forward Computations`. Leading next-session compute: `INV{n+1}-MKK-GAUGE-LOOP-SELFCONSISTENCY` (CF-INV6-W4-A). Track-local boundary: no INV6 result is permanent until migrated into a session-mode `/rclab-plan` and re-computed under a `session-{N}` gate.
