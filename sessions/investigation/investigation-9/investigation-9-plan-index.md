# Investigation 9 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed**: `investigation-1/{kaku-speculative-theorist, string-theory-theorist, loop-quantum-gravity-theorist, kitaev-quantum-chaos-theorist}.md` (4-agent survey batch; invocation typed `--investigation 9 --context <4 files joined by &&>`, resolved to `--from` per identical inv-3/4/5/6/7/8/10 precedent)
**Shape**: fanout (3 per-wave plan files + this thin index)
**Digest**: `investigation-9-seed.md` (convergence map + per-gate seed anchors + DOUBLE DEDUP) | **Partition**: `investigation-9-partition.md`

**Thesis**: the four vantages converge on how the substrate relates to its sibling quantum-gravity / holography / quantum-chaos programmes — *more closed than the framework as a whole*, so the leverage is importing their MECHANISMS, not new correspondences. Two fresh convergences carry inv-9: (i) **modular flavor symmetry** flagged #1 IDENTICALLY by kaku NS-1 + string NS-1 → INV9-W1-1 (one compute); (ii) **sum-over-geometries / Page-curve / information** — the sharpest adversarial tension (kaku: GGE Fock trace IS the sum; string: categorical no-`∫Dg`; kitaev's λ_L=0 the shared evidence) → INV9-W1-5 compute + INV9-W3-1 workshop. Plus the swampland / dimensional-transmutation sector + the substrate-QG-character-lens workshop.

**DOUBLE DEDUP (the dominant structural fact)**: TWO of the four seed agents are reused agents whose computes are consumed elsewhere — **loop-quantum-gravity** (all 5 next-steps consumed by inv-7) and **kitaev** (the 4 integrability computes consumed by the concurrent inv-10 = INV10-W3-1/2/3/4). Neither owns a compute wave; both contribute as INV9-W3-2 workshop voices (the inv-5 spectral-geometer reduced-role precedent, applied twice). inv-9's fresh compute content is carried by **kaku (W1) + string (W2)**, neither used by any other investigation. See `investigation-9-seed.md §"DEDUP"`.

## Waves

| Wave | Theme | Owner | Types | Gates | Plan file | Pin-validation |
|:----:|:------|:------|:------|:-----:|:----------|:---------------|
| 1 | cross-domain structural bridges / dimensional-transmutation sector | kaku-speculative-theorist | compute×5 | 5 | `investigation-9-plan-w1.md` | PASS |
| 2 | cross-framework walls / mechanism imports | string-theory-theorist | compute×2, review×1 | 3 | `investigation-9-plan-w2.md` | PASS |
| 3 | cross-framework adjudications | gen-physicist (neutral) | workshop×2 | 2 | `investigation-9-plan-w3.md` | artifact-existence |

**Total: 10 gates** — 7 compute + 1 review + 2 workshop. Honest workshop count: **2** (sum-over-geometries INV9-W3-1 kaku↔string; substrate-QG-character-lens INV9-W3-2 kitaev↔LQG). YAML-validator: W1 PASS=5/FAIL=0, W2 PASS=3/FAIL=0. Upstream-pin-validator: W1 exit-0 PASS, W2 exit-0 PASS (all cited upstream npz exist + pins agree).

## Gate roster (canonical IDs as landed by the per-wave planners)

- **W1** (kaku): `INV9-W1-1-MODULAR-FLAVOR-FORM` (compute, FLAGSHIP, connes exec + string co-option) · `INV9-W1-2-SWAMPLAND-GRADIENT-BOUND` (compute) · `INV9-W1-3-BCS-DIMENSIONAL-TRANSMUTATION` (compute) · `INV9-W1-4-ZETA-BRODY-BRIDGE` (compute) · `INV9-W1-5-GGE-FOCK-PAGE-CURVE` (compute)
- **W2** (string): `INV9-W2-1-SEN-TACHYON-K-THEORY-DESCENT` (compute) · `INV9-W2-2-DS-ENTROPY-SUBSTRATE-SPECIES-COUNT` (compute, [SIGN]) · `INV9-W2-3-MODERN-SWAMPLAND-REFRESH` (review)
- **W3** (neutral): `INV9-W3-1` (workshop, sum-over-geometries, kaku↔string) · `INV9-W3-2` (workshop, QG-character lens, kitaev↔LQG)

## Wave structure / dependencies

```
W1 ─┐
W2 ─┼─ mostly PARALLEL (no hard inter-wave verdict gate)
W3 ─┘   (W3 workshops adjudicate readings/lenses; W3-1 is SHARPENED by — but does not
        block on — INV9-W1-5 (Fock partition function) + inv-10 W3-1 (GGE-projection
        Born rule); W3-2 adjudicates the QG-character LENS, independent of all compute verdicts)

Intra-wave: no hard intra-wave npz prerequisites (compute gates consume existing caches:
            L12 spectrum / TRANSIT-279 npz / S105 zeta-zeros / spectrum cache @ session-84).

Cross-wave convergence (cross-reference only, NOT shared gates):
  INV9-W1-5 ↔ inv-10 W3-1   Fock partition function (kaku) vs Born-rule emergence (kitaev) — same GGE, distinct observable
  INV9-W1-2 ↔ INV9-W2-3     swampland gradient-bound compute (specific instance) vs swampland refresh review (broad audit)
  (convergence verdicts are the /rclab-investigate --investigation 9 close synthesis, NOT plan-time gates.)
```

## Cross-investigation dedup (complementary — distinct machinery / observable, NOT duplicate)

- `INV9-W1-1` (modular-flavor form) — complementary to inv-2 (off-U(2) Yukawa geometry) + inv-5 W1-3/W1-4 (connes ε_LX machinery); the modular-form route DERIVES what ε_LX backs out.
- `INV9-W1-4` (zeta-Brody bridge) — complementary to inv-3 W1-1/W1-2 (low-L level-statistics) + inv-10 W3-2/W3-3 (kitaev RP + Σ²/SFF rigidity); W1-4 is the number-theoretic zeta-zero↔Brody-β bridge.
- `INV9-W1-5` (GGE Fock partition function) — complementary to inv-10 W3-1 (GGE-projection Born rule) + inv-8 W2-3/W4-1; same GGE object, distinct observable (Fock partition function vs Born-rule emergence).
- `INV9-W2-2` (dS species-count) — complementary to inv-4 W3-1 / inv-5 W1-5 / inv-7 W3-1 / inv-8 W2-1; same dS-entropy/CC target, distinct functional (finite species-count).
- `INV9-W1-3` (BCS dimensional transmutation) — complementary to inv-3 W4-1 / inv-6 W4-1; same M_KK gap, distinct mechanism (condensate-as-transmutation-scale).
- `INV9-W2-1` (Sen K-theory) + `INV9-W1-2`/`INV9-W2-3` (swampland) + `INV9-W3-1`/`INV9-W3-2` (workshops) — FRESH.
- **Reused-agent boundary**: `INV9-W3-2` (kitaev↔LQG) adjudicates the QG-character LENS; it does NOT re-open LQG's inv-7 computes or kitaev's inv-10 computes.

## Verdict track

Compute gates (7: W1 ×5 + W2 ×2) emit verdict lines to `computations/investigation-9/inv9_gate_verdicts.txt` via `emit_verdict(session=9, track="investigation", ...)`. The W2-3 review + W3 workshops close by artifact-existence-with-content (`investigation-9-<short>-synthesis.md` for the review; `workshops/inv9-w3-1-sum-over-geometries.md` + `workshops/inv9-w3-2-qg-character-lens.md` for the workshops). Track-local boundary: an investigation result becomes permanent only when promoted into a session (`gate-verdicts.md §"Investigation-Track Canonical Path"`).

## Routed-OUT Q2 session-track hygiene (NOT gates — `/rclab-investigate --investigation 9` close → session-promotion)

HY1 chaotic-instantons §4/§7.1(B)/§8.2 down-tag + atlas-09 retraction (ALSO inv-10 HY1; dedup at close) · HY2 register "emergence of QM-form" as ASSUMED in atlas-04 · HY3 down-tag the "MSS bound trivially satisfied" framing. (LQG hygiene = inv-7 HY4/HY5/HY6; not re-routed.) Full detail: `investigation-9-seed.md §"Routed OUT"`.

## Dispatch

- Per-wave: `/rclab-coordinate sessions/investigation/investigation-9/investigation-9-plan-w{i}.md`
- Full investigation: `/rclab-coordinate sessions/investigation/investigation-9/investigation-9-plan-index.md`
- Close (analysis → synthesis → index housekeep): `/rclab-investigate --investigation 9`
