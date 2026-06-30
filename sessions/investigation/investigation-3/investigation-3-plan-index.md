# Investigation 3 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed (`--from`)**: three investigation-1 agent surveys — `berry-geometric-phase-theorist.md` + `spectral-geometer.md` + `paasch-mass-quantization-analyst.md` (digest: `investigation-3-seed.md`)
**Mode**: INVESTIGATION (track-local). compute/solo verdicts → `computations/investigation-3/inv3_gate_verdicts.txt` via `emit_verdict(session=3, track="investigation")`; review/workshop gates close by artifact-existence (NO verdict line).
**Plan-freeze validation**: R3 YAML PRDR validator **PASS 14/14**; upstream-pin validator **PASS** (0 missing npz, 0 path drift) on all compute/solo gates. `[SIGN]`/directional gates carry the schema-v2 3-tuple pre-registration.

## Waves

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | Spectral statistics & eigenbundle topology | berry-geometric-phase-theorist | compute×4 | 4 | `investigation-3-plan-w1.md` |
| 2 | Heat-kernel scale-transport & spectral rigidity | spectral-geometer | compute×4 | 4 | `investigation-3-plan-w2.md` |
| 3 | Mass-quantization & Paasch bridges | paasch-mass-quantization-analyst | solo×1, compute×4 | 5 | `investigation-3-plan-w3.md` |
| 4 | M_KK derivability adjudication | gen-physicist (neutral) | workshop×1 | 1 | `investigation-3-plan-w4.md` |

**Total: 14 gates** (12 compute + 1 solo + 1 workshop).

## Gate roster (what `/rclab-coordinate` dispatches)

| Gate ID | gate_type | Executor | One-line |
|:--------|:----------|:---------|:---------|
| INV3-W1-1 | compute | kitaev-quantum-chaos-theorist | SFF K(τ) + number variance Σ²(L)/Δ₃(L) — Poisson/RMT/arithmetic discriminator |
| INV3-W1-2 | compute | kitaev-quantum-chaos-theorist | P(s) semi-Poisson/Berry–Robnik, sector-resolved (pooling-artifact test) |
| INV3-W1-3 | compute | berry-geometric-phase-theorist | catastrophe germ of λ_min(τ,μ): fold A₂ vs cusp A₃ + diabolical-point census |
| INV3-W1-4 | compute | berry-geometric-phase-theorist | second Chern c₂ of B2 bundle over 4-param C² coset; Yang-monopole test |
| INV3-W2-1-DS-FLOW-SCALE-TRANSPORT | compute | spectral-geometer | d_s(σ) flow as K→K* scale map: ∫θ dlnσ vs ln(K/K*)=3.1350 |
| INV3-W2-2-ISOSPECTRAL-RIGIDITY-L3 | compute | spectral-geometer | isospectral rigidity at L_max=3: τ-scan for {a_0,a_2,a_4}-degenerate pair |
| INV3-W2-3-AS-AMPLITUDE-FLOOR-NSFUNCTIONAL | compute | spectral-geometer | A_s floor as exp(−ζ'_D(0)) under n_s-selected functional; ONE regulator-tagged OOM |
| INV3-W2-4-WEYL-REMAINDER-GEODESIC-STATIONARITY | compute | spectral-geometer | Weyl-remainder → non-variational route to τ_fold (geodesic stationarity) |
| INV3-W3-1-S0-PHI-FN-IDENTITY | solo (orchestrator-inline) | gen-physicist (nominal) | S₀ =? φ_paasch^{fN} machine-ε; three-zone kill (near-miss per W3 pre-flight) |
| INV3-W3-2-W3-MINIMAL-MODEL-KINK-PHI | compute | paasch-mass-quantization-analyst | W₃ M(6,5) Z₃-Potts kink ratios contain φ_paasch/fN within 2%? |
| INV3-W3-3-ALPHA-DIM-N3-TWO-ALPHA | compute | paasch-mass-quantization-analyst | α-dim (n3=dim(3,0)=10) chain + two-α reconciliation (1/137 ← 1/10.8 KK-run) |
| INV3-W3-4-CASIMIR-GRADED-NJ-7N | compute | paasch-mass-quantization-analyst | Casimir-graded N(j)=7n test (7,35,42,98,150); feeds INV3-W4-1 |
| INV3-W3-5-KOIDE-CASIMIR-Z3-FOOT | compute | paasch-mass-quantization-analyst | Koide Q=2/3 + 45° Foot angle from Casimir-envelope √m + Z₃ geometry |
| INV3-W4-1 | workshop (spectral-geometer ↔ paasch, 2 rounds) | gen-physicist (neutral planner) | M_KK derivable vs structurally-irreducible — structural verdict + decisive forward gate |

## Dispatch

- **Per-wave**: `/rclab-coordinate sessions/investigation/investigation-3/investigation-3-plan-w{i}.md`
- **Full investigation**: `/rclab-coordinate sessions/investigation/investigation-3/investigation-3-plan-index.md`

`/rclab-coordinate` juggles the four gate types directly: compute gates dispatch as background subagents; the solo gate (INV3-W3-1) runs orchestrator-inline; the workshop (INV3-W4-1) runs as a 2-agent, 2-round sequential exchange. Within-wave cross-link: INV3-W3-4 (Casimir N(j)=7n) is the forward gate the INV3-W4-1 workshop names as decisive candidate (c) — its `fb_pair` feeds the workshop, but the waves carry no hard dispatch dependency (each is independently runnable).

## Non-gate items (recorded, NOT dispatched)

11 session-track capstone-hygiene Q2 items (HY1–HY11, `investigation-3-seed.md §"Non-gate items"`) are quarantined from this plan — an investigation cannot mutate curated session-track registers (track-local boundary). They route to session-promotion at `/rclab-investigate --investigation 3` close.
