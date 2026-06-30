# Investigation 10 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed**: `investigation-1/{tesla-resonance, quantum-acoustics-theorist, kitaev-quantum-chaos-theorist}.md` (3-agent survey batch; `--context`→`--from` per inv-3/4/5/6/7/8 precedent)
**Shape**: fanout (4 per-wave plan files + this thin index)
**Digest**: `investigation-10-seed.md` (convergence map + per-gate seed anchors) | **Partition**: `investigation-10-partition.md`

**Thesis**: the framework's #1 *unbuilt* phononic gate — TRANSIT-PS-67, the full post-fold GGE acoustic power spectrum P(k) — assembled and read for its observables. The SPINE: **INV10-W2-1** builds the spectrum SHAPE (mode-by-mode Bogoliubov P(k) → n_s(k)); **INV10-W1-1** supplies the post-freeze turbulent-cascade exponent (the tilt input + freeze-vs-cascade verdict); **INV10-W4-1** adjudicates the contested A_s AMPLITUDE mechanism (finite-pair static structure factor vs resonance-impedance step). kitaev (W3) orbits the same GGE from the integrability side (modular-flow emergent-QM, spectral-rigidity classification, RP-resonance edge-of-chaos, ETH-violation). **INV10-W4-2** adjudicates the acoustic-horizon reality (moduli-turning-point vs τ-flow analog horizon).

## Waves

| Wave | Theme | Owner | Types | Gates | Plan file | Pin-validation |
|:----:|:------|:------|:------|:-----:|:----------|:---------------|
| 1 | resonance-first (cascade, dispersion, second-sound, synthetic topology) | tesla-resonance | compute×4, solo×1 | 5 | `investigation-10-plan-w1.md` | PASS |
| 2 | TRANSIT-PS assembly + bispectrum + parametric resonance | quantum-acoustics-theorist | compute×4 | 4 | `investigation-10-plan-w2.md` | PASS |
| 3 | integrability, spectral statistics, emergent-QM, edge-of-chaos | kitaev-quantum-chaos-theorist | compute×4 | 4 | `investigation-10-plan-w3.md` | PASS |
| 4 | cross-vantage adjudications | gen-physicist (neutral) | workshop×2 | 2 | `investigation-10-plan-w4.md` | artifact-existence |

**Total: 15 gates** — 12 compute + 1 solo + 2 workshop. Honest workshop count: **2** (A_s-mechanism INV10-W4-1; acoustic-horizon-reality INV10-W4-2).

## Gate roster (canonical IDs as landed)

- **W1**: `INV10-W1-1-CASCADE-EXPONENT` (compute) · `INV10-W1-2-ROTON-LANDAU-VC` (compute) · `INV10-W1-3-SECOND-SOUND-CMB` (compute) · `INV10-W1-4-SYNTHETIC-TAU-ZAK-PHASE` (compute) · `INV10-W1-5-ANALOG-TEMPERATURE-RECONCILE` (solo)
- **W2**: `INV10-W2-1` (BUILD TRANSIT-PS-67, shape/n_s(k)) · `INV10-W2-2` (Sakharov acoustic-peaks, BAO θ_A) · `INV10-W2-3` (bispectrum triple + τ_NL Suyama-Yamaguchi) · `INV10-W2-4` (S101 Floquet/preheating)
- **W3**: `INV10-W3-1` (GGE-projection Born-rule via modular flow) · `INV10-W3-2` (RP resonances across the fold) · `INV10-W3-3` (Σ²(L)+SFF rigidity, L=12→14) · `INV10-W3-4` (ETH-violation, cell-vs-fabric)
- **W4**: `INV10-W4-1` (A_s-mechanism, qa↔tesla) · `INV10-W4-2` (acoustic-horizon-reality, tesla↔volovik)

## Wave structure / dependencies

```
W1 ─┐
W2 ─┼─ mostly PARALLEL
W3 ─┤
W4 ─┘   (W4 workshops adjudicate objects already on disk: the A_s spread + the two
        candidate normalizations for W4-1; the BLV machinery + φ=0 + S85 for W4-2)

Cross-wave prerequisite (SOFT, with self-contained fallback per the W2 planner):
  INV10-W1-1 (cascade exponent) → INV10-W2-1 (TRANSIT-PS tilt input).
  INV10-W2-1 → INV10-W2-2 (Sakharov consumes the assembled P(k)) — HARD intra-wave prereq.
  The A_s AMPLITUDE is OUT OF SCOPE of W2-1 (shape only) — handed to W4-1.

Cross-wave convergence (cross-reference only, NOT shared gates):
  INV10-W1-2 / W1-5 → INV10-W4-2  (roton dissipation + analog-T data feed the horizon adjudication)
  INV10-W4-1 → INV10-W2-1         (the A_s-mechanism verdict tells TRANSIT-PS which normalization to use)
```

## Cross-investigation dedup (complementary — distinct machinery / observable, NOT duplicate)

- `INV10-W2-1` (BUILD TRANSIT-PS-67) — the MASTER end-to-end A_s/P(k) assembly, complementary to the FIVE partial A_s routes (inv-3 W2-3 / inv-4 W1-4 / inv-5 W2-1 / inv-6 W2-2 / inv-7 W3-2).
- `INV10-W3-3` (Σ²/SFF spectral RIGIDITY) — complementary to inv-8 W3-3 (heat-trace d_s/CDT) + inv-3 W2-1/W2-2 (d_s-flow / rigidity); same deep-truncation spectrum, orthogonal functionals.
- `INV10-W3-1` (GGE-projection Born-rule via modular flow σ_t^ω) — complementary to inv-8 W2-3 (einstein Born rule via 8-RG-integrals trace) + inv-8 W4-1 (Bell, where kitaev is the S70 advocate); same founding-conceit, distinct machinery. kitaev plays complementary roles across inv-8 and inv-10.
- `INV10-W1-4` (synthetic-τ Zak phase), `INV10-W3-2` (RP resonances), `INV10-W2-4` (S101 Floquet) — FRESH attacks on the fold's dynamical character; W1-4 is built provably distinct from the S46 ordinary-BZ Zak phase RETRACTED at S48.

## Verdict track

Compute/solo gates (13: W1/W2/W3) emit verdict lines to `computations/investigation-10/inv10_gate_verdicts.txt` via `emit_verdict(session=10, track="investigation", ...)`. Workshop gates (W4) close by artifact-existence (`workshops/inv10-w4-1-as-normalization-mechanism.md`, `workshops/inv10-w4-2-acoustic-horizon-reality.md`). Track-local boundary: an investigation result becomes permanent only when promoted into a session.

## Routed-OUT Q2 session-track hygiene (NOT gates — `/rclab-investigate --investigation 10` close)

HY1 chaos-doc (`framework-chaotic-instantons.md`) down-tag + atlas-09 retraction (lossy-compression CLOSED, λ_L=0) · HY2 S43 infinite-κ "two-mechanism" GGE-permanence scrub → R_therm transit-freeze · HY3 ADH-dephasing vs 6-M_KK⁻¹-thermalization reconciliation · HY4 T_acoustic=0.112 PROVENANCE · HY5 A_s canonical-value reconciliation + inventory row (mack) · HY6 SW1/SW3 deg=+2 projection check (mack). **Standing gap (NOT a gate)**: the M⁴-summand d_s^{M4} (needs an M⁴ foam/path-integral model the framework lacks).

## Dispatch

- Per-wave: `/rclab-coordinate sessions/investigation/investigation-10/investigation-10-plan-w{i}.md`
- Full investigation: `/rclab-coordinate sessions/investigation/investigation-10/investigation-10-plan-index.md`
- Close: `/rclab-investigate --investigation 10`
