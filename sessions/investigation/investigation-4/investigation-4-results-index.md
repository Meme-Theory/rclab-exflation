# Investigation 4 — Results Index (per-wave working papers)

**Date**: 2026-06-14
**Plan**: `investigation-4-plan-index.md` (3 waves, 9 gates: 8 compute + 1 workshop)
**Seed (`--from`)**: `investigation-1/{hawking-theorist, schwarzschild-penrose-geometer}.md`
**Verdict track**: `computations/investigation-4/inv4_gate_verdicts.txt` (compute gates; `emit_verdict(session=4, track="investigation")`). The W3-2 workshop closes by artifact-existence (deliverable `workshops/level-3-magnitude-divergence.md`); no verdict line.

| Wave | Theme | Working paper | Gate sections |
|:----:|:------|:--------------|:--------------|
| 1 | Horizon thermodynamics, entropy & information | `investigation-4-w1-workingpaper.md` | §W1-1..4 (compute) |
| 2 | Causal structure, censorship & the metric lift | `investigation-4-w2-workingpaper.md` | §W2-1..4 (compute) |
| 3 | Cross-cluster bridges | `investigation-4-w3-workingpaper.md` | §W3-1 (compute) · §W3-2 (workshop) |

**Dispatch**: `/rclab-coordinate sessions/investigation/investigation-4/investigation-4-plan-index.md` (or per-wave `…-plan-w{i}.md`). Each WP carries one `*(pending …)*` block per gate; compute sections close on a verdict line + WP content, the workshop section closes on artifact-existence of its deliverable md.

## Verdicts (landed 2026-06-15)

All 9 compute gates closed (canonical lines in `computations/investigation-4/inv4_gate_verdicts.txt`); the W3-2 workshop LANDED by artifact-existence. **6 PASS · 2 FAIL · 1 INFO · 1 workshop-LANDED** (FAIL/INFO are constraint-map results, not failures; the early agent deaths were a transient infra rate-limit, fully recovered).

| Gate | Verdict | One-line |
|:-----|:--------|:---------|
| INV4-W1-1 | FAIL | GGE microstate count undercounts A/4 by 2.86 OOM (Page-shape PASS) |
| INV4-W1-2 | PASS | 1/4 coefficient DERIVED (c_conical=0.25) from a₂ conical-deficit response |
| INV4-W1-3 | PASS | Bousso + Bekenstein bounds respected, ~3 OOM margin (zero-parameter) |
| INV4-W1-4 | FAIL | greybody cannot bridge the 3.15-OOM A_s gap → structural wall survives |
| INV4-W2-1 | PASS | C-1 resolved: N_zeros=1, S95 single-asymmetric-open (S85 pair = artifact) |
| INV4-W2-2 | PASS | Raychaudhuri q∝H; focusing 99.97% a₂ (Einstein-Hilbert grade) |
| INV4-W2-3 | INFO | marginal censorship, p=−1 exactly (extremal/Aretakis boundary) |
| INV4-W2-4 | PASS | first compact-object: transit-phase KK bubble, λ_GL=0.944 M_KK⁻¹ |
| INV4-W3-1 | PASS | a₀ de Sitter clock = Volovik tracking, c_track=3 exact |
| INV4-W3-2 | LANDED | unified Level-3 criterion α_growth=d−2s=n (sp↔lizzi converged) |

**Cross-wave**: a₀-vs-a₂ clock SPLIT (W3-1 a₀ expansion clock vs W2-2 a₂ focusing clock) — two correct readings of distinct observables → clock-location workshop carry-forward (CF-INV4-W3-1-CLOCKLOC).

**Carry-forwards + housekeeping**: `investigation-4-housekeeping.md` (§B/§C session-track promotions + the capstone-hygiene 5-question gate routing) + each WP `## Carry-Forward Computations`. Track-local boundary: no INV4 result is permanent until migrated into a session-mode `/rclab-plan` and re-computed under a `session-{N}` gate.
