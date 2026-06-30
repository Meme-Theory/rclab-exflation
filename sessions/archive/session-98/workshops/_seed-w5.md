# Seed — Chunk w5 (Spectral-moment robustness — a₀/a₂ PV-invariance)

**Date**: 2026-05-31   **Investigator**: phonon-first-cosmologist   **Source**: session-98-w5-workingpaper.md + session-98-plan-w5.md
**Wave summary**: 1 gate, INFO (0 PASS / 0 FAIL / 1 INFO). `S98-A0A2-TIER2-PV-INVARIANCE` (`[SIGN]`, GEOMETRIC, lizzi). Structural reading: the capstone §8.5 tier-2 survival PARTITION for the a₀/a₂ Seeley-DeWitt moment-pair (a₀ = vacuum/CC moment of D_K; a₂ = emergent Einstein-Hilbert moment) is **regulator-class-INVARIANT** — `Δ(survival-margin)=0.000000000e+00` byte-exact, SURVIVE-label identical under FI-anchor (`a₀^{Mellin}/a₂^{Mellin}`) and full-physical-PV (`a₀^{Pauli-Villars}/a₂^{Pauli-Villars}`). The INFO is fired by a single sub-threshold residual on an ORTHOGONAL axis: the PV within-family L_max=10→12 ratio-drift `d_PV=0.057026 ∈ (ε_FI=0.05, info_band=0.10]`. This is a clean FI/RD layer-decomposition: the LABEL (class-membership) is FI; the only RD residual is localized to the L_max-extension axis, NOT the PV-vs-Mellin (regulator-class) axis.

## Slot 1 candidates — solo reviews (`/rclab-review`)
(Q1-YES, Q1b: independent reading suffices)

(none — see `## No candidates` reasoning below)

## Slot 2 candidates — workshops (`/rclab-workshop`)
(Q1-YES, Q1a: cross-rebuttal essential)

(none — see `## No candidates` reasoning below)

## No candidates

This wave produces ZERO Slot 1 and ZERO Slot 2 candidates. The single borderline INFO is examined explicitly per the rule's "INFOs at borderline" signal and fails the 3-question discriminator at Q1 (no math/physics adjudication), so it routes to a carry-forward — and that carry-forward is ALREADY in the W5 WP. Honest count: 0 workshops, 0 solos.

**Why the borderline INFO is NOT a Q1 workshop seam.** The seam I was asked to test: would the spectral-functional and NCG-axiomatic domains GENUINELY DISAGREE on whether `d_PV=0.0570` is structural RD (threatening partition robustness) vs truncation-transient — in a way NOT reducible to "run the L_max extension"? They would not, for two structural reasons:

1. **The LABEL invariance is a PROVEN structural identity, not a numerical contingency.** The survival-margin is a {+1,−1} sign-encoding of a parse-tree predicate ("is a₀/a₂ a dimensionless ratio-observable?"). The c² volume/curvature rescale cancels in ANY regulator anchoring (capstone §8.2 R₁-invariance theorem, residual 0; WP §W5-1 Step 3, plan substitution-chain Step 3). This cancellation is regulator-INDEPENDENT and holds at EVERY L_max independently of the magnitude of d_PV. An NCG-axiomatic reviewer cannot mount a "the LABEL might be RD" rebuttal: the LABEL is pinned by the same representation-theoretic c²-cancellation identity both domains read identically. There is no axis on which spectral-functional and NCG-axiomatic diverge about whether a dimensionless moment-RATIO is regulator-class-invariant — it is the already-PROVEN R₁-invariance.

2. **d_PV lives on an axis ORTHOGONAL to the partition-robustness question.** By the substitution chain (WP §W5-1 Step 5; plan Step 5), d_PV is defined on the PV *within-family* L_max=10→12 axis. The PV-vs-Mellin (regulator-class) axis quantity is `|O_PV − O_FI| = 0.293033`, which is EXPECTED-nonzero and is explicitly NOT the survival margin (it is the S96-SDW-CC-GAP `partB_FI_across_PV=False` content). The two questions — "is the partition regulator-robust?" and "does d_PV shrink with L_max?" — sit on orthogonal axes. The first is answered structurally (PASS-conjunct, byte-exact). The second is a CONVERGENCE measurement with a single pre-registered resolving gate (`d_PV(L_max≥13) < ε_FI=0.05`), i.e. "does the number shrink as L_max grows." That is the rule's "is NOT a workshop" item-1 case (a solo L_max-extension compute is a carry-forward), not a reading-divergence.

There is no first-principles argument on a "structural L_max-RD" side that a domain expert would mount INDEPENDENT of running the extension — the question is literally a convergence number. Both domains converge on "the listed CF resolves it." → Q1 NO.

**Tractability cross-check (rules out a hidden feasibility tension).** A residual workshop seam could hide if the listed CF were itself intractable (an L_max≥13 irrep-construction wall would re-open whether the convergence test is even well-posed — a possible Q1). It is not: an L14 spectrum cache already exists on disk (`computations/session-87/s87_spectrum_cache_L14_tau019.npz`), in addition to the L12 cache (`computations/session-84/s84_spectrum_cache_L12_tau019.npz`). The full-PV a₀/a₂ continuation to L_max≥13 is a Casimir-bounded read against an existing cache (no new diagonalization, no irrep-construction feasibility per `math-scripts.md §"D_K Block-Diagonality"` pre-check). The CF is a clean, well-posed convergence measurement — strengthening the conclusion that the residual is a carry-forward, fully resolvable by the listed compute, with no adjudication to debate.

**Q2 / Q3 checks.** The INFO is not a status-tag edit, mechanical promotion, rule-file diff, audit-script extension, or mechanical re-run (Q2 NO — and capstone-hygiene Q3 for this wave is "NO net change", housekeeping §17: C10/§8.5 stay OPEN, no down-tag). It is not an N-condition × N-axis parallel-compute-wave (Q3 NO — single-axis convergence, one resolving gate). The only forward-compute item is the genuine-math CF already in the WP.

## Cross-wave flags (surface for consolidator; NOT resolved here)

- **V.8 INFO ↔ EVOI Tier-3 #12 `SDW-2ND-MOMENT-EFT` (S96 B2) — same SDW-convergence axis.** The §8.5 a₀/a₂ tier-2 partition status is bounded overall by the open SDW-convergence gate (JACOBSON-NONLOCAL-64 / capstone open gate #6; WP §W5-1 substrate framing, T3-S43-SPECTRAL-DISSOLUTION ε_c∼N^{−0.457}). V.8's residual d_PV (within-family L_max-drift) and the Tier-3 SDW 2nd-moment EFT-control item both probe convergence/dissolution of the finite-triple absolute moments — they are adjacent on the SDW-convergence axis, not independent. A consolidator may wish to note that the W5 CF (`CF-S99-W5-A0A2-LMAX-PV-CONTINUATION`) and EVOI #12 share the L_max/SDW-convergence theme; they are distinct gates (ratio-drift vs 2nd-moment EFT-ratio) but co-located on the same standing open question. NOT a workshop — surfaced for planner awareness only.
- **No EVOI §1–§4 omission found.** The W5 forward item is already represented: §6 actionable queue line 7 (`CF-S98-A0A2-TIER2-PV-INVARIANCE`, "optional robustness") is the now-completed V.8; its successor `CF-S99-W5-A0A2-LMAX-PV-CONTINUATION` is a precision-refinement of a §8.5 partition bounded by Tier-3 #12 / open gate #6, not a new high-leverage Tier-1/2 open item. No NEW high-leverage open item is surfaced by this wave that is ABSENT from §1–§4.

## Carry-forwards (route to investigated wave's WP CF section, NOT this schedule)

- **[Q-other]** — `CF-S99-W5-A0A2-LMAX-PV-CONTINUATION` is **ALREADY in the W5 WP** (`session-98-w5-workingpaper.md §"Carry-Forward Computations"`) and the S98 housekeeping "Genuine-math carry-forwards" block (line 105). Do NOT re-create it. It is a genuine-math solo compute (extend full-physical-PV a₀/a₂ to L_max≥13; gate `S99-W5-A0A2-LMAX13`: PASS iff `d_PV<ε_FI=0.05` ⇒ INFO→PASS; tractable against the existing L14 cache `s87_spectrum_cache_L14_tau019.npz`). `/rclab-plan` picks it up from the WP CF block directly.
- **[Q2-hygiene]** — (none surfaced by this wave).
- **[Q3-wave-together]** — (none).

## Wave-by-wave digest (consolidator background)

**Wave 5 — Spectral-moment robustness (a₀/a₂ tier-2 PV-scheme invariance).** Single-gate COMPUTE-class wave (campaign S-3, lizzi). Closes the loop the S97 W2-1 object-definedness gate (`S97-W2-1-A0A2-PV-FULL-MELLIN`, INFO, audit `7d5ca3f9`) deliberately left open (scope-tag `DI1=OBJECT-DEFINEDNESS-AXIS-ONLY; does-NOT-establish-or-retract-§8.5-tier-2-survival`).

- **`S98-A0A2-TIER2-PV-INVARIANCE`** — INFO (audit `4522ea7e…`; dual-SHA + `[SIGN]` 3-tuple `sign=PASS / magnitude=INFO / regime=VALID`). No new diagonalization — both moments read from the W2-1 npz (`s97_w2_1_a0a2_pv_full_mellin.npz`), same L_max=10 D_K² cache.
  - PASS-conjunct (structurally forced): `Δ(survival-margin)=0` byte-exact; SURVIVE-label identical under FI-anchor (O_FI=a₀/a₂=0.217563) and PV-anchor (O_PV=0.510595). `d(survival)/d(PV-scheme)=0` NUMERICALLY, not merely structurally — the DI1 guard is numerically confirmed.
  - INFO discriminator: `d_PV = |ratio_PV(L12) − ratio_PV(L10)|/|ratio_PV(L10)| = 0.057026 ∈ (ε_FI=0.05, info_band=0.10]` — hidden RD-axis flag on the PV within-family L_max=10→12 axis ONLY.
  - Standout structural finding (spectral-functional signature): what survives ALL regulator choices (the survival LABEL / §8.5 partition) is STRUCTURAL (FI, c²-cancellation regulator-independent); what depends on the choice (absolute ratio value 0.5106-vs-0.2176 across PV; within-family L_max margin) is the localized RD degree of freedom. The absolute-magnitude RD-ness does NOT leak into the survival PARTITION.
  - CLASS=FULL (full-physical 2-point Pauli-Villars from `_pauli_villars_subtraction.py` PRIMARY tier, c=[+2,−1], m²=[1,2] M_KK units, Σc_r=1 ∧ Σc_r m_r²=0); NO `-SCHEMATIC` suffix, NO `# tier_pin=TIER-2` row (W2-1 precedent). Regulator-pins: `a₀^{Mellin}/a₂^{Mellin}` AND `a₀^{Pauli-Villars}/a₂^{Pauli-Villars}`; `poleconv-A-double` (a₀ at s=4/n=0; a₂ at s=3/n=2, d=8).
  - SOURCE-RECON: benign plan-text-drift on `canonical_constants.py` file-SHA (concurrent S98 wave touched the file); binding test is the consumed VALUE — `a_0_FW_zeta=6440.0`, `a_2_FW_zeta=2776.165389` both non-superseded and bit-identical to npz (D_max<0.1, no rule-file action). PV-helper SHA `eaf98037…` matches plan pin exactly (CLASS=FULL audit anchor).
  - Not a cross-pillar bridge (no laboratory-IN observable); not a §VII registry landing (confirms an EXISTING capstone partition).
- **Forward**: one genuine-math CF (`CF-S99-W5-A0A2-LMAX-PV-CONTINUATION`) already in the WP. No workshop, no solo. The wave's INFO is a precise localization of which axis the regulator choice still touches (the L_max-extension axis), not a weakness of the survival claim.
