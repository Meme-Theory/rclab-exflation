# Investigation 4 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed (`--from`)**: two investigation-1 agent surveys — `hawking-theorist.md` + `schwarzschild-penrose-geometer.md` (digest: `investigation-4-seed.md`)
**Mode**: INVESTIGATION (track-local). compute verdicts → `computations/investigation-4/inv4_gate_verdicts.txt` via `emit_verdict(session=4, track="investigation")`; the workshop gate closes by artifact-existence (NO verdict line).
**Plan-freeze validation**: R3 YAML PRDR validator **PASS 10/10** (8 compute + the W3-2 workshop block accepted under the S95 non-compute clause; cutoff_axis N/A on non-numeric gates); upstream-pin validator **PASS 3/3** (no intra-plan upstream-gate-output dependencies to drift-check; all cited read-only input npz — `s75_dimer_z2_pair_production`, `s84_spectrum_cache_L12_tau019`, `s95_w4_1_white_hole_kinematic_consistency`, `s85_w6_extremal_horizon_formal` — separately confirmed on disk). `[SIGN]`/directional gates carry the schema-v2 3-tuple pre-registration. The single forward-pin (INV4-W1-3 ← INV4-W1-1 microstate npz) is intra-wave (disposition (b)).

## Waves

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | Horizon thermodynamics, entropy & information | hawking-theorist | compute×4 | 4 | `investigation-4-plan-w1.md` |
| 2 | Causal structure, censorship & the metric lift | schwarzschild-penrose-geometer | compute×4 | 4 | `investigation-4-plan-w2.md` |
| 3 | Cross-cluster bridges | gen-physicist (neutral) | compute×1, workshop×1 | 2 | `investigation-4-plan-w3.md` |

**Total: 9 gates** (8 compute + 1 workshop).

## Gate roster (what `/rclab-coordinate` dispatches)

| Gate ID | gate_type | Executor | One-line |
|:--------|:----------|:---------|:---------|
| INV4-W1-1-GGE-PAGE-CURVE-MICROSTATE-COUNT | compute | hawking-theorist | GGE-relic entanglement spectrum → analog Page curve + microstate count S=ln∏(1+n_k) vs A_horizon_FW/4 (the 1/4-from-substrate test; replaces the FAILED S89 degenerate-CM trace) |
| INV4-W1-2-EUCLIDEAN-REPLICA-QUARTER-COEFFICIENT | compute | hawking-theorist | replica S=(1−n∂_n)lnZ(n) on the one-loop spectral action; Fursaev-Solodukhin corner term → reproduce A_horizon_FW/4? (PASS licenses the Jacobson reframing) |
| INV4-W1-3-BOUSSO-BEKENSTEIN-FALSIFIER | compute | hawking-theorist | zero-parameter S_GGE ≤ A_horizon/4G (Bousso) + S ≤ 2πRE (Bekenstein) on the white-hole light-sheet; consumes W1-1 microstate count (forward-pin) |
| INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION | compute | transit-dynamics-theorist | greybody Γ(ω) through the a₄-BCS barrier; A_s=\|β_fold\|²·∫Γdω vs the 3.15-OOM AMPLITUDE-NORM-66 FAIL (greybody-suppression vs permanent-wall) |
| INV4-W2-1 | compute | schwarzschild-penrose-geometer | c_s(τ) re-derived from a₂(τ) stiffness; zero-count of (v−c_s), two-branch N_zeros∈{1,2} (1=confirm S95 / 2=restore S85) — resolves C-1 from the substrate |
| INV4-W2-2 | compute | schwarzschild-penrose-geometer | Raychaudhuri focusing for the reduced (a(t),τ(t)) congruence; localize w=M_KK to one term; τ̇→3H vs S101-W1-QEQ-SELFCONS; a₀-vs-a₂ source |
| INV4-W2-3 | compute | schwarzschild-penrose-geometer | Christodoulou bounded-variation SCC on the exactly-solvable extremal κ=0 Σ_dump; H¹_loc regularity → inextendible (sealed) vs extendible |
| INV4-W2-4 | compute | schwarzschild-penrose-geometer | Gregory-Laflamme stability of the dynamical M⁴×SU(3) (strictly larger than the static GL-STABILITY-63 PASS, its τ̇→0 anchor); SU(3)-direction mode below λ_GL = KK-bubble |
| INV4-W3-1 | compute | hawking-theorist | de Sitter a₀ first law dE=−T_dS dS_dS ≡ Volovik tracking ρ_vac∼M_Pl²H² (pin the c_track=3 O(1) coefficient Sage-exact); clock in a₀, unifying G2 (a(t)) with C10 |
| INV4-W3-2 | workshop | schwarzschild-penrose-geometer ↔ lizzi-spectral-functional-theorist (2 rounds) | which property predicts convergent-vs-divergent finite-L Level-3 magnitude: geometric (homogeneity degree vs apex dim 8) vs spectral (regulator class / functional / pole); STRUCTURAL VERDICT + decisive forward gate |

## Dispatch

- **Per-wave**: `/rclab-coordinate sessions/investigation/investigation-4/investigation-4-plan-w{i}.md`
- **Full investigation**: `/rclab-coordinate sessions/investigation/investigation-4/investigation-4-plan-index.md`

`/rclab-coordinate` juggles the gate types directly: compute gates dispatch as background subagents (verdict line + WP section); the workshop (INV4-W3-2) runs as a 2-agent, 2-round sequential exchange closing on artifact-existence. Cross-link: INV4-W3-1 (a₀ de Sitter clock) and INV4-W2-2 (a₂ Raychaudhuri) are COMPLEMENTARY readings of the τ↔t clock — if both land on a₀ the C2 volume-preserving/conformal-clock tension is resolved; a divergence seeds a FUTURE clock-location workshop (NOT planned this round). INV4-W1-3 consumes INV4-W1-1's microstate npz (intra-wave forward-pin; both runnable in W1).

## Non-gate items (recorded, NOT dispatched)

6 session-track capstone-hygiene items (HY1–HY6, `investigation-4-seed.md §"Non-gate items"`: Diagram-J redraw to S95, capstone causal-disconnection + Page-curve down-tags, the three-KIND surface-gravity table, the CCC→WCH-compliance reframe, the analog-T-hierarchy tag) + 4 surveyed-but-not-elevated bridges (sp B-4/B-5, hawking R4/C3) are quarantined — an investigation cannot mutate curated session-track registers (track-local boundary). HY1–HY6 route to session-promotion at `/rclab-investigate --investigation 4` close (HY1/HY2 are gated on the INV4-W2-1 zero-count verdict).
