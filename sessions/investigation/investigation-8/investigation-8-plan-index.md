# Investigation 8 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed**: `investigation-1/{mack-cosmic-bridge, phonon-first-cosmologist, einstein-theorist}.md` (3-agent survey batch; invocation typed `--investigation 8 --context <3 files joined by &&>`, resolved to `--from` per identical inv-3/4/5/6/7 precedent)
**Shape**: fanout (4 per-wave plan files + this thin index)
**Digest**: `investigation-8-seed.md` (convergence map + per-gate seed anchors) | **Partition**: `investigation-8-partition.md`

**Thesis**: the framework's #1 gap is the single dimensionful-scale / a(t)–Hubble-backbone DOF (all three vantages name it). The investigation's SPINE is TWO new constructive attacks — INV8-W2-1 (Jacobson entanglement-equilibrium → CC magnitude) + INV8-W3-2 (quantum-metric stiffness → H(τ) backbone). The same H²-freedom DOF drives the live dark-sector front (INV8-W1-2 S_8/τ_reio observe; INV8-W3-1 Kibble-Zurek walls + INV8-W2-4 running-vacuum = two competing mechanisms for the DESI w_a / BBN ΔN_eff tension). Plus a DM-abundance closure (INV8-W1-1 PBH), a quantum-foundations cluster (INV8-W4-1 Bell + INV8-W2-3 Born rule), and cross-domain spectral/CM bridges (INV8-W1-4 no-go, INV8-W3-3 CDT, INV8-W3-4 Higgs near-criticality, INV8-W3-5 branch count).

## Waves

| Wave | Theme | Owner | Types | Gates | Plan file | Pin-validation |
|:----:|:------|:------|:------|:-----:|:----------|:---------------|
| 1 | observational cosmology & the dark-sector front | mack-cosmic-bridge | compute×3, solo×1 | 4 | `investigation-8-plan-w1.md` | PASS |
| 2 | the dimensionful-scale knot, precision-GR & quantum foundations | einstein-theorist | compute×4 | 4 | `investigation-8-plan-w2.md` | PASS |
| 3 | cross-domain bridges (transit + condensed-matter + spectral-geometry) | phonon-first-cosmologist | compute×5 | 5 | `investigation-8-plan-w3.md` | PASS |
| 4 | cross-vantage adjudications | gen-physicist (neutral) | workshop×2 | 2 | `investigation-8-plan-w4.md` | artifact-existence |

**Total: 15 gates** — 12 compute + 1 solo + 2 workshop. Honest workshop count: **2** (Bell-vs-hidden-variable INV8-W4-1; cosmic-birefringence β-vs-null INV8-W4-2).

## Gate roster (canonical IDs as landed by the per-wave planners)

- **W1**: `INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM` (compute) · `INV8-W1-2-S8-TAU-REIO-GGE-GROWTH` (compute) · `INV8-W1-3-FDM-PARTITION-RECONCILIATION` (solo) · `INV8-W1-4-FINITE-L-POLE-NO-GO` (compute)
- **W2**: `INV8-W2-1` (Jacobson→CC-magnitude) · `INV8-W2-2` (PPN/MICROSCOPE-η) · `INV8-W2-3` (Born-rule derive-or-no-go) · `INV8-W2-4` (running-vacuum c₁ vs n=2)
- **W3**: `INV8-W3-1-KZ-Z3-WALL-NETWORK` · `INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU` · `INV8-W3-3-SPECTRAL-DIMENSION-LMAX14-CDT` · `INV8-W3-4-HIGGS-QUARTIC-RG-STABILITY` · `INV8-W3-5-WATANABE-MURAYAMA-BRANCH-COUNT`
- **W4**: `INV8-W4-1` (Bell-vs-hidden-variable, einstein↔kitaev) · `INV8-W4-2` (cosmic-birefringence, mack↔connes)

## Wave structure / dependencies

```
W1 ─┐
W2 ─┼─ mostly PARALLEL (the four waves carry no hard inter-wave verdict gate)
W3 ─┤
W4 ─┘   (W4 workshops are independent of all compute verdicts — both adjudicate
        objects already on disk: the S58/S70 readings for W4-1; the [J,D_K]=0 / T7
        parity machinery for W4-2)

Intra-wave: INV8-W1-3 (solo f_DM reconciliation) is CONDITIONAL on INV8-W1-1
            (PBH integral) — a decision-point prerequisite (value dependency),
            NOT an upstream-npz pin. Supply-or-retire of the dimer-Z₂ channel
            (DIMER-Z2-PAIR-PRODUCTION-75, already f_dimer_Z2=0.27) branches on
            W1-1: RETIRE-OR-DUAL-CITE (W1-1 PASS) vs KEEP-AND-FLAG (W1-1 FAIL).

Cross-wave convergence (cross-reference only, NOT shared gates):
  INV8-W2-1 ↔ INV8-W3-2   two constructive attacks on the dimensionful-scale knot
  INV8-W2-4 ↔ INV8-W3-1   two competing mechanisms for the w_a / BBN tension
  INV8-W1-4 ↔ INV8-W3-3   the two L_max-truncation structural gates (pole vs spectral-dim)
  (the convergence verdicts are the /rclab-investigate --investigation 8 close synthesis,
   NOT plan-time gates.)
```

## Cross-investigation dedup (complementary — distinct machinery / observable, NOT duplicate)

- `INV8-W1-1` (PBH from fold) — FIRST formation-channel route into the Row #88 compact-object cell (complementary to inv-4 / inv-6 / inv-7 W2-2 / inv-7 W3-1).
- `INV8-W2-1` (Jacobson → CC magnitude) — entanglement-equilibrium VARIATION, complementary to inv-4 W1-2 / inv-4 W3-1 / inv-5 W1-5 / inv-7 W3-1 (same §VII.BZ crossed product, distinct functional).
- `INV8-W3-3` (P(σ) @ L_max=14-16, CDT) — complementary to inv-3 W2-1 / W2-2 (high-L_max CDT comparison vs scale-transport map / low-L_max rigidity).
- `INV8-W3-4` (Higgs quartic RG / near-criticality) — complementary to inv-5 W1-1 / W2-3 / W3-3 (RG-running/metastability vs m_H-VALUE residual).
- `INV8-W2-3` (Born rule) + `INV8-W4-1` (Bell) + `INV8-W2-4`/`INV8-W3-1` (running-vacuum / Kibble-Zurek) — FRESH (no prior investigation touched the foundations cluster or computed a wall network / RG c₁H²).

## Verdict track

Compute/solo gates (13: W1/W2/W3) emit verdict lines to `computations/investigation-8/inv8_gate_verdicts.txt` via `emit_verdict(session=8, track="investigation", ...)`. Workshop gates (W4) close by artifact-existence-with-content (`workshops/inv8-w4-1-bell-vs-hidden-variable.md`, `workshops/inv8-w4-2-cosmic-birefringence.md`). Track-local boundary: an investigation result becomes permanent only when promoted into a session (`gate-verdicts.md §"Investigation-Track Canonical Path"`).

## Routed-OUT Q2 session-track hygiene (NOT gates — `/rclab-investigate --investigation 8` close → session-promotion)

HY1 capstone EMERGENT-EIH-LIFT promotion · HY2 n_s band [0.9557,0.9595] reconciliation · HY3 w0_FW gate/provenance · HY4 f_DM canonical-table + Ω_DM PROVENANCE · HY5 Strutinsky=O'Neill=saddle-point §VII registration · HY6 §VII.CB/AU/BT/AM Level-3 re-class (conditional on INV8-W1-4).

## Dispatch

- Per-wave: `/rclab-coordinate sessions/investigation/investigation-8/investigation-8-plan-w{i}.md`
- Full investigation: `/rclab-coordinate sessions/investigation/investigation-8/investigation-8-plan-index.md`
- Close (analysis → synthesis → index housekeep): `/rclab-investigate --investigation 8`
