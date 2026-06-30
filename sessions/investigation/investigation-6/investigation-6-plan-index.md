# Investigation 6 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed (`--from`)**: three investigation-1 agent surveys — `dirac-antimatter-theorist.md` + `kaluza-klein-theorist.md` + `feynman-theorist.md` (digest: `investigation-6-seed.md`)
**Mode**: INVESTIGATION (track-local). compute verdicts → `computations/investigation-6/inv6_gate_verdicts.txt` via `emit_verdict(session=6, track="investigation")`; the workshop gate closes by artifact-existence (NO verdict line).
**Plan-freeze validation**: R3 YAML PRDR validator **PASS 13/13** (compute gates, w1/w2/w3); upstream-pin validator **PASS** (0 missing npz, 0 path drift) on all 13 compute gates; the W4 workshop gate is artifact-existence-ready (workshop: block complete — EXACTLY 2 agents, rounds, sources, output_path, adjudication_question + must_contain). `[SIGN]`/directional gates carry the schema-v2 3-tuple pre-registration.

## Waves

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | KK scale-bracket & moduli stabilization | kaluza-klein-theorist | compute×4 | 4 | `investigation-6-plan-w1.md` |
| 2 | Quantum-loop gravity sector & A_s normalization | feynman-theorist | compute×5 | 5 | `investigation-6-plan-w2.md` |
| 3 | Baryogenesis, CPT & the antimatter sector | dirac-antimatter-theorist | compute×4 | 4 | `investigation-6-plan-w3.md` |
| 4 | M_KK determination-route reconciliation | gen-physicist (neutral) | workshop×1 | 1 | `investigation-6-plan-w4.md` |

**Total: 14 gates** (13 compute + 1 workshop).

## Gate roster (what `/rclab-coordinate` dispatches)

| Gate ID | gate_type | Executor | One-line |
|:--------|:----------|:---------|:---------|
| INV6-W1-1-M-KK-BRACKET-PROPAGATE | compute | kaluza-klein-theorist | M_KK both routes (gravity-zeta 7.43e16 vs Kerner-gauge 5.04e17); propagate 6.79× into a₀ (×2125) + a₂ (×46) — band injected into A_s/CC |
| INV6-W1-2-KK-CASIMIR-VOLUME | compute | kaluza-klein-theorist | graded Casimir E_Cas in the VOLUME direction; volume minimum → derives det-g constraint + third M_KK determination |
| INV6-W1-3-KK-THRESHOLD-RUNNING | compute | kaluza-klein-theorist | three-coupling KK-tower running M_KK→m_Z (Cartan Trace Identity + (p,q) sum); (α_em,sin²θ_W,α_s) within 2% + m_H band collapse |
| INV6-W1-4-KK-SOLITON-COMPACT-OBJECT | compute | kaluza-klein-theorist | Gross-Perry-Sorkin KK-soliton: mass~M_KK, compactness, QNM ladder; single-vs-bimetric cone fork |
| INV6-W2-1-GAMMA-TAU-ONELOOP-TRAJECTORY | compute | feynman-theorist | Γ[τ]=−½ζ'_D(0,τ) trajectory over τ∈[0.05,0.30]; induced G_N(τ)/Λ(τ) signs + Sakharov M_KK self-consistency |
| INV6-W2-2-TRANSIT-PS-PARKER-BOGOLIUBOV | compute | transit-dynamics-theorist | Parker-Bogoliubov P_ζ(k)=(k³/2π²)|β_k|² through the fold; absolute A_s + horizon-crossing K_pivot (joint closer) |
| INV6-W2-3-GRAVITON-LOOP-FINITENESS | compute | feynman-theorist | emergent graviton propagator + Goroff-Sagnotti R³ on the finite triple (van Nuland–van Suijlekom); finite-at-M_KK or 1/ε? |
| INV6-W2-4-EMERGENT-LORENTZ-REALGATE | compute | feynman-theorist | ω(k) O(k⁴) Goldstone + graviton-zero-mode on crystalline substrate (S106 κ=3); LIV bound + CPT-odd SME null |
| INV6-W2-5-GRAVITON-SPECTRAL-FUNCTION-DS | compute | feynman-theorist | graviton spectral function ρ(ω); UV scaling vs asymptotic-safety/CDT d_s→2 — substrate predicts d_s→8 (no reduction) |
| INV6-W3-1-ETA-B-GGE-RESCATTERING | compute | dirac-antimatter-theorist | inter-branch GGE rescattering phase → Im[A_weak(φ_88)·A_strong(GGE)] into C6 η_B; supplies the missing ~13.5×? |
| INV6-W3-2-J-BREAKING-DEFORMATION-ENUM | compute | dirac-antimatter-theorist | enumerate admissible J-breaking deformations of ℂ⊕ℍ⊕M₃(ℂ) (Boyle-Farnsworth/Bochniak-Sitarz); is φ_88-Cartan unique? |
| INV6-W3-3-ETA-B-ACOUSTIC-SCHWINGER | compute | dirac-antimatter-theorist | η_B as acoustic-Schwinger from the Mach-13.75 transit field gradient (φ_CP=π/2); is the shortfall a Mach effect? |
| INV6-W3-4-ANTIMATTER-DOMAIN-HORIZON | compute | dirac-antimatter-theorist | pre-transit acoustic sound-horizon vs c/H_0; single-domain explanation for Fermi-LAT antimatter-fraction <10⁻⁵ |
| INV6-W4-1 | workshop (kaluza-klein-theorist ↔ feynman-theorist, 2 rounds) | gen-physicist (neutral planner) | M_KK determination-route reconciliation: over-determined / under-determined / one-route-dominates — STRUCTURAL VERDICT + decisive forward gate |

## Dispatch

- **Per-wave**: `/rclab-coordinate sessions/investigation/investigation-6/investigation-6-plan-w{i}.md`
- **Full investigation**: `/rclab-coordinate sessions/investigation/investigation-6/investigation-6-plan-index.md`

`/rclab-coordinate` juggles the gate types directly: the 13 compute gates dispatch as background subagents (each emits a dual-SHA verdict line to the investigation track); the W4 workshop (INV6-W4-1) runs as a 2-agent, 2-round sequential exchange closing by artifact-existence. Within-investigation forward links (no hard dispatch dependency — each wave is independently runnable): INV6-W4-1 NAMES INV6-W1-1 (the gauge-vs-gravity bracket), INV6-W1-2 (the Casimir-volume third determination), and INV6-W2-1 (the Sakharov-Γ[τ] self-consistency) as the three substrate determinations it reconciles; INV6-W2-1 (Γ[τ]) is flagged for promotion into inv-5 W3-2 (two-effective-actions adjudication) if it lands; INV6-W3-1 and INV6-W3-3 are the two η_B-enhancement mechanisms compared at W3 synthesis.

## Cross-investigation dedup (load-bearing — do not collide)

- **INV6-W4-1 vs inv-3 W4**: complementary halves of the M_KK frontier — inv-3 W4 = *derivability-in-principle* (Paasch mass-quantization vs scale-free triple; spectral-geometer ↔ paasch); INV6-W4-1 = *determination-route reconciliation* (Casimir-volume vs Sakharov-loop vs gauge-gravity bracket; kaluza-klein ↔ feynman). Cross-cite at both closes; do NOT merge.
- **INV6-W2-2 (A_s)**: the 4th A_s route, distinct from inv-3 W2-3 (near-floor-DOS), inv-4 W1-4 (exit-horizon greybody), inv-5 W2-1 (impulse-quench); uniquely joint with K_pivot.
- **INV6-W2-1 (Γ[τ])**: feeds inv-5 W3-2 (the two-effective-actions adjudication) — the COMPUTE that adjudication needs.
- **INV6-W1-4 (KK soliton)**: distinct from inv-4 W2-4 (Gregory-Laflamme bulk instability) — localized soliton vs bulk-geometry stability.

## Non-gate items (recorded, NOT dispatched)

6 session-track curated-register hygiene items (HY1–HY6, `investigation-6-seed.md §"Non-gate items"`) are quarantined from this plan — an investigation cannot mutate curated session-track registers (track-local boundary). They route to session-promotion at `/rclab-investigate --investigation 6` close: HY1 (EVOI Rank-8 baryogenesis CLOSED→CONDITIONAL down-tag), HY2 (η_B falsifier-row mint, mack sole-writer), HY3 (δ_CP^PMNS dated falsifier-row mint, mack sole-writer), HY4 (corpus paper-32 a_g prose correction), HY5 (capstone §0/§2.4 gauge-from-NCG-algebra reconciliation), HY6 (alpha_GUT canonical-constants registration). Plus 7 surveyed-but-not-elevated bridges (dirac UB-4 positronium-BEC; feynman B-F6 / R-F2 / R-F4 / R-F5; KK R-KK3 / R-KK4).
