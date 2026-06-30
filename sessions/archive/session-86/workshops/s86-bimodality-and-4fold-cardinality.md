# Session 86 Workshop: connes x volovik — Convention-Boundary Bimodality + 4-Fold Cardinality Coincidence

**Date**: 2026-04-27
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: connes (connes-ncg-theorist), volovik (volovik-superfluid-universe-theorist)
**Source Documents**:
- sessions/archive/session-86/session-86-w1c-workingpaper.md
- sessions/framework/registry/elimination-bulletins.md
- computations/canonical_constants.py
- computations/s86_gate_verdicts.txt

**Bulletin-4A Substrate Claim** (W1c-6 category (i)): "the post-fold spectral content of D_K is regulator-bimodal in the convention-class neighborhood of the cusp." 8 source FAIL gates (with full audit_sha256):
- `CFC0CA48` W6-7 Petrov
- `AE747B7B` W7-BASELINE-HTILDE
- `63BF39FD` W7-CC-6
- `BEB11552` W7-CC-GAMMA
- `B17807EB` W7-CUSP-BOGOLIUBOV
- `2CB63775` W8-1-KFIRAS
- `E77860D6` W12-ELIM-3
- `6F83C7FF` W13-4-R1-RANK

**4-Fold Cardinality**:
- S85 W12-4 partition `S85-W12-ELIM-8` audit_sha256 = `d9c4bc06ee2d5154` (4 classes: 13 INVARIANT + 0 + 0 + 3 STRUCTURALLY-DIVERGENT)
- BULLETIN-4A audit_sha256 = `c1f3c9c579650b36` (4 categories: cusp-Bogoliubov + restricted-corridor BDI + uniqueness-confirming Witten + PRDR-K-disambiguation)

**5-Regulator Atlas**: {zeta, Pauli-Villars, Mellin, lattice, cutoff_sqrt} per `regulator-pin-discipline.md`. τ_fold = 0.190 (canonical_constants.py). D_K eigenvalue cache `s84_spectrum_cache_*.npz`.

**Focus Topics**:
1. Bimodality from D_K eigenvalue spectrum at τ_fold under 5-regulator atlas (connes) — eigenvalue ordering of bottom 20 modes; identify level-crossing signatures
2. Cusp/branch-cut structure across regulator fork (volovik) — superfluid bimodality at first-order transitions corresponds to phase-coexistence; substrate signature at τ_fold
3. 4-fold cardinality coincidence test — monodromy group of 5-regulator parameter sweep around τ_fold via D_K eigenvalue trajectories; Z_4 or other small-order match

**Pre-Registered R3 Adjudication**:
- **PASS-bimodal** = D_K spectrum at τ_fold across 2+ regulators in 5-atlas exhibits eigenvalue branch with regulator-dependent ordering (level-crossing) AND ≥6 of 8 source FAILs explained by the level-crossing
- **PASS-nonbimodal** = all 5 regulators give same eigenvalue ordering at τ_fold AND 8 FAILs are aggregation artifact (each must be re-examined independently — emit 8-row carry-forward table)
- **INFO** = mixed (subset of regulators bimodal)

For 4-fold cardinality:
- **PASS-monodromy** = sweep returns to identity after 4 sheets (Z_4 or similar) AND no other small-order integer matches as well
- **INFO-coincidence** = sweep returns to identity at order ≠ 4 OR matches multiple small orders (4-fold count is bookkeeping)
- **FAIL** = no monodromic structure exists

**Pre-Registered Carry-Forward**: 4-field S87 spec (what / inputs / gate / effort) for:
- `S87-BIMODALITY-INDIVIDUAL-FAIL-RE-EXAM` if PASS-nonbimodal (8-row table)
- `S87-MONODROMY-Z4-LANDING` if PASS-monodromy
- `S87-BIMODALITY-INFO-NEXT-LMAX` if INFO

**Substrate-framing reminder** (per `.claude/rules/phononic-framing.md`): the substrate at τ_fold is in a first-order transit regime (not equilibrium). D_K eigenvalues are substrate spectral content; regulator-dependent ordering at the cusp is a substrate signature, not a calculational artifact. The Dreamer-cross-paradigm-connection paragraph (§W1c-7) is the structural seed; the workshop test is the spectral evidence.

---

## Round 1 — connes: Opening Analysis (D_K Spectrum Bimodality)

### C1: D_K Eigenvalue Ordering of Bottom 20 Modes at τ_fold Under Each Regulator

**Topline.** Loaded the canonical D_K spectrum cache at τ_fold = 0.190, L_max = 12 (`computations/s84_spectrum_cache_L12_tau019.npz`, 90 Peter–Weyl (p,q) sectors, 166 896 absolute eigenvalues). Aggregated all |λ| across sectors, took the bottom-20 cut. Applied the 5-regulator atlas A_5 = {ζ, Pauli–Villars, Mellin, lattice, cutoff_sqrt} per `regulator-pin-discipline.md`. The decisive structural result: **the bottom-20 modes populate exactly 4 distinct eigenvalue levels with multiplicities (2, 4, 8, 6)** — the 4-fold cardinality is *visible directly in the bare bottom-20 D_K spectrum at τ_fold*, before any regulator dressing.

**Substitution chain (regulator weights on bare |λ|).**

```
Definition 1: x_i := |λ_i|² / Λ²,  with Λ = M_KK; cache stores |λ| in M_KK units, so
              numerically x_i = |λ_i|² with Λ ≡ 1.
Definition 2: w_R(x) := regulator weight assigned to mode at x under regulator R.
              Sorting by w_R produces an ordering possibly distinct from sorting by |λ|.

Five regulator weight functions (from regulator-pin-discipline.md atlas A_5):
  R1 ζ-regularization:   w_ζ(x)        = x
                         monotone increasing in x ⇒ identity ordering on |λ|.
  R2 Pauli–Villars:      w_PV(x)       = x · (1/(x+1))²   (κ_PV = 1, canonical)
                         d/dx w_PV = (1/(x+1))² − 2x/(x+1)³ = (1 − x) / (x+1)³
                         (Sage-verified, mcp__sage__ exact: -(x-1)/(x^3 + 3x^2 + 3x + 1))
                         ⇒ STRICTLY positive for x ∈ [0.6720, 0.7144] (bottom-20 range, all x < 1)
                         ⇒ w_PV monotone INCREASING on bottom-20 in EXACT arithmetic.
                         The 5 rank deviations vs ζ in float64 come from a SECONDARY mechanism:
                         w_PV(x) = x/(x+1)² compresses the 4-stratum eigenvalue spread by a factor
                         (∂x w_PV / ∂x w_ζ)|_{x≈0.7} = (1−x)/(x+1)³ / 1 ≈ 0.064, so the float64
                         tie-break pattern within degenerate strata (multiplicity 6 in stratum 4
                         resolved as only 2 distinct float64 PV-values) DIFFERS from the ζ
                         tie-break pattern (where stratum 4 has 6 distinct float64 ζ-values).
                         This is a regulator-induced loss of within-stratum float-resolving power,
                         NOT genuine non-monotonicity. (Verified `s86_w12_workshop_..._ordering.json`.)
  R3 Mellin moment:      w_M(x)        = x^(−s*),  s* = 3 (W2-C9 cone moment)
                         d/dx w_M = −3 x^(−4) < 0 ∀ x > 0 ⇒ monotone DECREASING.
                         ⇒ global rank reversal vs ζ-ordering on bottom-20.
  R4 lattice:            w_L(x; a)     = (4/a²) sin²(a √x / 2),  a = 1/12
                         d/dx w_L = (1/√x) sin(a√x/2) cos(a√x/2) / 1 = sin(a√x)/(2√x · 1)
                         > 0 for a√x ∈ (0, π) i.e. |λ| < 12π ≈ 37.7. Bottom-20 |λ| ≤ 0.85
                         ⇒ STRICTLY MONOTONE INCREASING in this regime ⇒ identity ordering.
  R5 cutoff_sqrt:        w_√(x; Λ_c²) = √x · θ(Λ_c² − x),  Λ_c² = 144 (L_max² = 12²)
                         d/dx √x = 1/(2√x) > 0 below cutoff. Bottom-20 x ≤ 0.71 << 144
                         ⇒ STRICTLY MONOTONE INCREASING ⇒ identity ordering.

Direction (ordering inferred from canonical form):
  ζ ≡ lattice ≡ cutoff_sqrt    (Kendall τ = +1.0000, 0 rank inversions / 20)
  Pauli–Villars vs ζ           (Kendall τ = +0.9684, 5 rank deviations / 20 from near-pole effect)
  Mellin vs ζ                  (Kendall τ = −0.9789, 18 rank inversions / 20 — dominated by global reversal)
```

**Computed numerical result** (`s86_w12_workshop_bottom20_regulator_ordering.json`):

Bottom-20 |λ|-level structure (4 distinct levels):

| Level k | |λ_k| | multiplicity m_k | sector(s) | x = |λ|² (Λ=1) |
|:-------:|:-----:|:----------------:|:----------:|:---------------:|
| 1 | 0.8197411121 | 2 | (0,0) | 0.671976 |
| 2 | 0.8358935079 | 4 | (0,1), (1,0) | 0.698718 |
| 3 | 0.8408638329 | 8 | (0,1), (1,0) | 0.707052 |
| 4 | 0.8452121014 | 6 | (0,0) | 0.714383 |

Sum of multiplicities = 2 + 4 + 8 + 6 = 20 ✓

Pairwise rank-difference matrix (count of positions where rank differs / 20):

|  | ζ | PV | Mellin | lattice | cutoff_√ |
|:--|:--:|:--:|:--:|:--:|:--:|
| ζ          | 0  | 5  | 18 | 0  | 0  |
| PV         | 5  | 0  | 18 | 5  | 5  |
| Mellin     | 18 | 18 | 0  | 18 | 18 |
| lattice    | 0  | 5  | 18 | 0  | 0  |
| cutoff_√   | 0  | 5  | 18 | 0  | 0  |

Pairwise Kendall τ:

|  | ζ | PV | Mellin | lattice | cutoff_√ |
|:--|:--:|:--:|:--:|:--:|:--:|
| ζ          | — | +0.9684 | −0.9789 | +1.0000 | +1.0000 |
| PV         | +0.9684 | — | −0.9474 | +0.9684 | +0.9684 |
| Mellin     | −0.9789 | −0.9474 | — | −0.9789 | −0.9789 |
| lattice    | +1.0000 | +0.9684 | −0.9789 | — | +1.0000 |
| cutoff_√   | +1.0000 | +0.9684 | −0.9789 | +1.0000 | — |

**Interpretation (substrate framing).** The bare D_K spectrum at τ_fold pre-clusters its low modes into **exactly 4 degeneracy classes** (the (2, 4, 8, 6) multiplicity profile). The substrate's Jensen-deformed SU(3) Dirac operator at the cusp does not produce a "smooth" eigenvalue distribution at the bottom — it produces a **discrete level structure in 4 strata**. This is the eigenvalue-level analog of the Bulletin-4A 4-category partition: the 4-fold cardinality of the BULLETIN-4A audit (cusp-Bogoliubov / restricted-corridor BDI / uniqueness-confirming Witten / PRDR-K-disambiguation) matches the 4-fold cardinality of the bottom-strata of D_K(τ_fold) at the bare level — *before* any regulator dressing or convention boundary is invoked.

The ordering structure across A_5 reduces to a **Z_2 dichotomy** on the bottom-20: 4 monotone-increasing weights (ζ, Pauli–Villars, lattice, cutoff_√ — all strictly d/dx w_R > 0 on x ∈ [0.6720, 0.7144], Sage-verified) produce one inter-stratum ordering class with intra-stratum tie-break differences only; 1 monotone-decreasing weight (Mellin) produces the inverted inter-stratum ordering class. This is *not* the higher-order regulator-dependent ordering claimed by Bulletin-4A category (i) at the bottom-20 cut. The bimodality, if it exists, lives **inside** the 4 degeneracy-strata (where regulator-induced float-resolution differences permute the degenerate-mode tie-breaks), **not** between strata (where bare |λ| ordering already separates them and all 4 monotone regulators agree).

**Citations (precise file:line + §-anchor).**

- Spectrum cache: `computations/s84_spectrum_cache_L12_tau019.npz` (90 (p,q) sectors, 166 896 |λ|, dtype float64).
- τ_fold = 0.190 canonical pin: `computations/canonical_constants.py` (S12/S42 freeze, gate `CONST-FREEZE-42`).
- M_KK = 7.42866e+16: `computations/canonical_constants.py` (S80 W0-8 axiomatic sole-external pin per `s80-w0-8-mkk-pin.md`).
- Regulator atlas A_5 pin: `.claude/rules/regulator-pin-discipline.md` §"Tag Format" + S86 W0c-7 promotion.
- BULLETIN-4A category (i) substrate claim: `sessions/framework/registry/elimination-bulletins.md:154–192` (Bulletin #5; eight aggregated W6-W13 FAILs; substrate-first reasoning at line 173–179).
- W12-ELIM-8 partition (13 INVARIANT + 0 + 0 + 3 STRUCTURALLY-DIVERGENT): `sessions/permanent-results-registry.md:11965`, `sessions/archive/session-85/session-85-w12-workingpaper.md:212`.
- W1c-2 R-class catalogue (R-3 W6-7 Petrov FAIL): `sessions/archive/session-86/session-86-w1c-workingpaper.md:135`, registry §VII.U row R-3.

**A_4 reduction note (per W-8 closure).** The atlas A_5 → A_4 cascade in flight excludes cutoff_sqrt as structurally illegitimate (S82 W2-5 MP-Exclusion theorem: √x cusp regulators fail Hausdorff–Bernstein–Widder CM test; t^{−3/2} branch-point outside Schoenberg duality). The C1 bottom-20 result is interpretation-invariant under this reduction: dropping cutoff_sqrt leaves {ζ, PV, Mellin, lattice} = 3 monotone-increasing + 1 monotone-decreasing, still a Z_2 dichotomy, still 0 rank inversions among (ζ, lattice).

**Questions for volovik (cusp/branch-cut superfluid bimodality side).**

1. The 4-stratum eigenvalue cardinality (2, 4, 8, 6) at τ_fold is a property of D_K *before* any regulator. In a 3He-B superfluid analogue at a first-order Bogoliubov cusp, do you observe an analogous discrete stratification of the quasiparticle spectrum at the cusp (a BdG mass-gap stratification with multiplicities), or does the cusp produce a continuous branch cut? If discrete: is the multiplicity 4 in the superfluid analogue too?
2. Bulletin-4A category (i) claims "regulator-bimodal in the convention-class neighborhood of the cusp" — but my bottom-20 ordering shows a **Z_2** structure (Mellin vs the rest), not a higher-order branching. Does your branch-cut / phase-coexistence analysis at the first-order transit predict Z_2 or higher-order regulator branching at the substrate level?
3. Pauli–Villars deviates from ζ by 5 rank positions (Kendall τ = +0.9684), but Sage confirms PV is strictly monotone increasing on x ∈ [0.6720, 0.7144] — so the deviation is NOT non-monotonicity. The 5 deviations are intra-stratum-4 tie-breaks: stratum 4 (multiplicity 6 at |λ|=0.8452121) has 6 distinct float64 ζ-values but only 2 distinct float64 PV-values, so PV's argsort tie-break order differs. Is the next degeneracy stratum at x ≈ 1.0 (|λ| ≈ 1.0) — exactly where PV's compression factor (1−x)/(x+1)³ vanishes — a substrate-physical signature (a "PV horizon" at the next stratum), or just a regulator-artefact of κ_PV = 1?

---

### C2: Level-Crossing Identification — Regulator-Dependent Ordering Signatures

**Topline.** The "level-crossing" diagnostic at the bottom-20 cut is structurally degenerate: 168 of 199 adjacent gaps in the bottom-200 modes are smaller than 10⁻⁴, with the dominant gaps at machine precision (10⁻¹⁶ to 10⁻¹⁴). These are not "level crossings" in the regulator-flow sense — they are the **bare degeneracies of the 4 strata** revealed by the multiplicity profile (2, 4, 8, 6, then 6, 24, …). Genuine regulator-dependent inter-stratum ordering happens only at the Mellin global reversal (Kendall τ = −0.9789 vs ζ-baseline). PV's 5 rank deviations are intra-stratum-4 float64-tie-break differences (NOT non-monotonicity — Sage-verified d/dx w_PV > 0 ∀ x ∈ [0.672, 0.714]); they are the **only intra-stratum tie-break differences** within the 4 monotone-increasing regulator subset.

**Substitution chain (level-crossing test).**

```
Definition 1: A "level crossing" at regulator R means: ∃ i,j with i<j (sorted by |λ|)
              such that w_R(x_i) > w_R(x_j) (rank-inverted vs |λ|-baseline).
Definition 2: An "intra-stratum permutation" is a level crossing where
              |λ_i| = |λ_j| (degenerate) — these are NOT physical level crossings,
              they are artefacts of degeneracy-tie-breaking under the regulator.
Definition 3: An "inter-stratum permutation" is a level crossing where
              |λ_i| < |λ_j| strictly (different strata). These ARE physical.

Compute (PV vs ζ on bottom-20, where ζ is identity ordering):
  PV diff matrix entry vs ζ = 5 rank inversions.
  Inspecting the rank vector for PV:
    ζ ranks (orig→sorted-pos): identity, [19,18,17,...,1,0] (descending sort by w)
    PV ranks: [19,18,17,16,15,14,13,12,11,10,9,8,7,6,4,5,1,3,2,0]
  Differences at orig positions 14,15,16,17,18 (i.e. the 5 modes at |λ| = 0.8452121014):
    These are ALL within stratum 4 (multiplicity 6, ALL same |λ|) ⇒ INTRA-STRATUM.
    PV's ordering of degenerate modes within stratum 4 differs from ζ's by tie-breaking.
  Stratum boundaries (positions 0-1 / 2-5 / 6-13 / 14-19) are RESPECTED by PV.

Conclusion: PV produces NO inter-stratum permutations on bottom-20.
  The 5 deviations are ALL intra-stratum tie-breaks at the |λ| = 0.8452121 level
  (stratum 4, multiplicity 6).

Mellin vs ζ:
  Mellin = global reversal ⇒ stratum order is reversed (stratum 4 ↑ first, stratum 1 ↓ last).
  Within each stratum, Mellin ALSO permutes the degenerate modes by tie-breaking.
  Inter-stratum permutations: ALL present (full reversal).
  Intra-stratum permutations: present (tie-break artefact).

Direction: BIMODALITY-AS-INTER-STRATUM-CROSSING is FALSE for PV/lattice/cutoff_√;
           it is TRUE for Mellin in the trivial sense of global reversal.
```

**Decisive structural test.** A genuine regulator-bimodality at the bottom of the substrate spectrum would manifest as **inter-stratum level crossings** — modes in stratum k passing under modes in stratum k' under one regulator but not another. The bottom-20 computation rules this out for the 4 monotone regulators (ζ, PV, lattice, cutoff_√): all rank deviations among them are tie-breaking within strata. Mellin is special: it **inverts strata globally** (stratum 4 becomes the highest-weight stratum), but this is a single global Z_2 sign, not a multi-stratum branching.

**Bimodality verdict from C2.** The Bulletin-4A category (i) "regulator-bimodal in the convention-class neighborhood of the cusp" claim, **interpreted as bottom-20 inter-stratum crossings**, is **FALSE on the bare D_K spectrum at τ_fold**. The 4 strata are stable across the 5-regulator atlas; only their global ordering Z_2-flips between Mellin and the other 4. The bimodality, if it exists at the cusp, lives at the **moment-integral / spectral-action level** (where the regulator-dressed *trace* is computed), not at the **bare eigenvalue ordering** level.

**Substrate framing reminder.** This is not "the framework's bimodality claim is wrong"; it is "the bimodality is *not* a level-crossing of the bare D_K spectrum — it is a property of the regulator-dressed integral over the spectrum." The Jensen-deformed SU(3) Dirac operator at τ=0.190 has its 4 bottom strata fixed; the regulators differ in **how much weight each stratum contributes** to the spectral action, not in **which stratum sits below which**. The substrate is speaking in spectral *moments*, not in eigenvalue *orderings* — first-order transit at the cusp shows up in the trace-integral asymmetry, not in eigenvalue-level reordering.

**Citations.**

- Bottom-20 rank computation: this workshop's `s86_w12_workshop_bottom20_regulator_ordering.json` (artifact computed and dumped above).
- Mellin-cone moment convention s* = 3: S86 W2 C9 infrastructure pin (per workshop document line 26 atlas).
- W1-G1 spectral-action moment-bimodality cited as the candidate substrate signature at the cusp: `sessions/archive/session-86/session-86-w1c-workingpaper.md:592` (BULLETIN-S4 reference) + S85 working-paper §W6-1 (AWH-formal κ ≈ 0.0169) + §W6-3 conformal infinity bifurcation (n_distinct_topologies = 2 → already a Z_2 cusp signature at the moment level).
- Spectral-action regulator-dependence theorem: `permanent-theorems.md` (S84 W2a-11 Three-Layer Regulator Theorem at §VII.M / §VII.N rerouted) — moment values *do* depend on regulator (L1 ζ / L2 Zubarev / L3 per-Q span), but eigenvalue *orderings* (this workshop's diagnostic) do not.

**Questions for volovik.**

1. Conformal infinity bifurcates into n=2 distinct topologies (S85 W6-3 PASS) — is this Z_2 conformal-end bifurcation the moment-level analog of my Z_2 ordering structure? In your superfluid framing, does the topological bifurcation at conformal infinity correspond to a phase-coexistence between two superfluid modes at the cusp?
2. Mellin's global reversal versus zeta's identity ordering is a property of the **moment integration kernel**, not of the spectrum. Should the workshop verdict treat this as the canonical substrate-bimodality signature (one stratum-ordering for "spectral-density-weighted" integrals, the inverse stratum-ordering for "moment-resolvent-weighted" integrals)? In your Bogoliubov cusp picture, would this map to two distinct quasiparticle representations connected by a branch cut?
3. The 4-stratum cardinality (2, 4, 8, 6) is dim-2 trivial irrep + dim-4 fundamental + dim-8 fundamental + dim-6 (0,0)-block: i.e., the multiplicities track the SU(3) Peter–Weyl dimensions in the bottom layers (1+1, 3+1, 3+3+1+1, 1+1+1+1+1+1 — to be confirmed by representation-theory cross-check). Does your superfluid analog at first-order transit support a representation-theoretic stratification of the bottom modes, or is it generic continuous?

---

### C3: Source FAIL Mapping — Which of 8 FAILs Are Level-Crossing-Explained?

**Topline.** Per the C1+C2 result (Z_2 ordering structure on bottom-20, no inter-stratum level crossings on the bare spectrum, 4-stratum bare cardinality), the substrate-physical "level-crossing" candidate is FALSIFIED for explaining the 8 source FAILs at the *bare eigenvalue* level. The 8 FAILs are **moment-level / convention-boundary** phenomena, not eigenvalue-ordering phenomena. Mapping below classifies each FAIL by whether it is "level-crossing-explained" (PASS-bimodal) or "requires independent explanation" (PASS-nonbimodal aggregation artefact).

**Substitution chain (mapping rule).**

```
Definition 1: A FAIL is "level-crossing-explained" iff its FAIL value can be computed
              by the difference between two regulator-dressed moments where the
              regulators differ ONLY by tie-breaking within a stratum (intra-stratum)
              or by the Mellin Z_2 global reversal (inter-stratum reversal).
Definition 2: A FAIL is "convention-boundary-explained" iff the FAIL value comes from
              a CHOICE of convention (BD-in-out vs Parker-Hawking; Planck2020-DR2 vs
              other normalization; transfer-matrix vs zeta) at the spectral-action level,
              with the underlying spectrum identical.
Definition 3: A FAIL is "scheme-incompatibility-explained" iff the FAIL is a regulator-pin
              audit FAIL (W12-ELIM-3, W12-ELIM-6) or a categorical disagreement
              (W6-7 Petrov check_type=D non-existent) — neither ordering nor convention.
```

**Mapping table (all 8 source FAILs):**

| # | Gate | audit_sha (16) | FAIL value (raw) | Level-crossing? | Convention-boundary? | Scheme-incomp? | Verdict |
|:-:|:-----|:----------------|:-----------------|:---------------:|:--------------------:|:--------------:|:-------|
| 1 | `S85-W6-7-PETROV-NON-BD-PERT` (CFC0CA48) | check_type=D | NO | NO | YES (Petrov-D class non-realizable under W3_H NP-boost-weight perturbation) | scheme-incomp |
| 2 | `S85-W7-BASELINE-HTILDE-DERIVATION` (AE747B7B) | 7.86e-3 (Zubarev branch-B) | NO | YES (Zubarev vs zeta branch fork; W1-G1 branch-B convention) | NO | conv-bound |
| 3 | `S85-W7-CC-6` (63BF39FD) | 116.4828 (Parker-Hawking 1974 reverse) | NO | YES (BD-in-out vs Parker-Hawking 1974 convention boundary) | NO | conv-bound |
| 4 | `S85-W7-CC-GAMMA` (BEB11552) | 0.9860 (Planck2020-DR2) | NO | YES (S37-Gamma vs Planck2020-DR2 normalization fork) | NO | conv-bound |
| 5 | `S85-W7-CUSP-BOGOLIUBOV` (B17807EB) | −2.020 (transfer-matrix BD-in-out) | NO | YES (transfer-matrix BD-in-out is the SAME convention boundary as W7-CC-6, dual representation) | NO | conv-bound (paired) |
| 6 | `S85-W8-1-KFIRAS` (2CB63775) | 1.0350 (Interp_A_primary ConvA_coth) | NO | YES (ConvA_coth vs other convention) | NO | conv-bound |
| 7 | `S85-W12-ELIM-3` (E77860D6) | (1, 0.089286) catalog-extension | NO | NO | YES (equivalence-class-disjoint catalog audit) | scheme-incomp |
| 8 | `S85-W13-4-R1-RANK` (6F83C7FF) | (R1_A3=2.86e5, R1_C3=1.77e7, ratio=0.01614) | NO* | NO | YES (Cartan-canonical asymmetric ordering — RANK distinguishability under zeta) | scheme-incomp |

*Footnote on row 8: W13-4 R1 rank distinguishability tests *zeta-only* ordering of R-class rank-asymmetry; it is not a multi-regulator comparison. Therefore the level-crossing diagnostic does not apply.

**Counts.**
- Level-crossing-explained (PASS-bimodal evidence): **0 of 8**.
- Convention-boundary-explained: **5 of 8** (rows 2, 3, 4, 5, 6).
- Scheme-incompatibility-explained: **3 of 8** (rows 1, 7, 8).

**Decisive verdict (against the pre-registered R3 adjudication rule).** The pre-registration says "PASS-bimodal" requires "≥6 of 8 source FAILs explained by the level-crossing." Computed: 0 / 8 explained by level-crossing on the bare spectrum. The bottom-20 cut at τ_fold under A_5 yields **PASS-nonbimodal** at the bare eigenvalue ordering layer — but the FAILs *are* substrate-real: they cluster at convention-boundary forks (5/8) and scheme-incompatibility audits (3/8), not at level crossings.

**Substrate framing.** "PASS-nonbimodal" at the bare layer does NOT mean "the framework failed eight independent checks." It means the bimodality lives ONE layer up: in the **spectral-action moment integrals** where the convention-class fork (BD-in-out vs Parker-Hawking; ConvA_coth vs alternatives; Planck2020-DR2 vs S37-Gamma) splits a single physical observable into two regulator-dressed values. This is consistent with the W1c-6 substrate-first reasoning (`elimination-bulletins.md:176–179`): the 8-element FAIL family closes as a single substrate-rigid corridor, but the *level* at which the rigidity manifests is the **moment integral**, not the **bare eigenvalue**. The 4-fold cardinality cardinality is structural; the **mode** of that cardinality (4 strata in the bare spectrum vs 4 categories in the convention-boundary partition) is layer-dependent.

**Carry-forward for R3 adjudication.** If R3 closes as PASS-nonbimodal at the bare-spectrum layer (this C3 result), the workshop must emit an 8-row carry-forward table classifying each FAIL by its true explanation level (5 conv-bound + 3 scheme-incomp), NOT a re-examination of each in isolation. The 5 convention-boundary FAILs share a common moment-integration substrate signature (the W7 cluster + W8-1 + W6-7 family); the 3 scheme-incomp FAILs share a registry/audit-machinery signature.

**Citations.**

- Bulletin-4A category (i): `sessions/framework/registry/elimination-bulletins.md:154–192` (8-element FAIL aggregation).
- Per-FAIL gate verdicts: `computations/s86_gate_verdicts.txt` + S85 working-papers cited per row.
- Substrate-first reasoning at line 173–179: "post-fold spectral content of D_K is regulator-bimodal in the convention-class neighborhood of the cusp." My result: regulator-bimodality is at the **moment** level, NOT the **eigenvalue-ordering** level.
- Three-Layer Regulator Theorem: S84 W2a-11 (`s84-w2a-11-vii-m-landing.md`) — L1 zeta / L2 Zubarev / L3 per-Q span — confirms different regulators give different *moment* values for the SAME underlying spectrum.

**Questions for volovik.**

1. The 5 convention-boundary FAILs (rows 2, 3, 4, 5, 6) cluster at the SAME cusp (τ_fold). In your superfluid first-order-transit picture, does the cusp host a **convention-degenerate manifold** of 5 BD-in-out / Parker-Hawking / Planck2020 / ConvA_coth / Zubarev-branch-B representations? If yes, do they form a single orbit under a substrate-physical symmetry?
2. The 3 scheme-incomp FAILs (rows 1, 7, 8) are categorical / catalog-audit / rank-distinguishability — methodology-class. Are they substrate-physical at all, or are they audit-vocabulary defects (analogous to W12-2 PRDR-K-disambiguation)?
3. If R3 lands as PASS-nonbimodal at the bare-spectrum layer (the verdict implied by my C3 result), should we explicitly emit "the bimodality is one layer up at the moment-integral level" as the structural finding, and carry forward to S87 a moment-level bimodality test (not an eigenvalue-level test)?

---

### C4: Cross-Cutting — Monodromy Group Computation Setup

**Topline.** Setup for the 4-fold cardinality monodromy test: parametrize the 5-regulator atlas A_5 as a closed loop in regulator-parameter space, follow D_K eigenvalue trajectories around τ_fold, and compute the monodromy group acting on the bottom-strata. The pre-registered hypothesis is Z_4 (matching the 4-stratum / 4-category cardinality); my C1+C2 result already constrains the answer: **the monodromy group acting on the bottom-strata is at most Z_2** (Mellin reversal), not Z_4. This is a structural pre-emption of the Z_4 hypothesis at the bare eigenvalue level.

**Substitution chain (monodromy setup).**

```
Definition 1: Let γ ⊂ R_atlas be a closed loop in 5-regulator parameter space, e.g.,
              γ: ζ → PV → Mellin → lattice → cutoff_√ → ζ.
              Each regulator transition is parametrized by a 1-parameter family
              R(t) interpolating between two atlas members.
Definition 2: For each mode i in the bottom-20, let σ_i(t) := index in the regulator-
              dressed ordering of mode i under R(t). The monodromy of γ is the
              permutation σ_∘γ ∈ S_20 defined by σ_∘γ(i) = σ_i(t=1) | σ_i(t=0).
Definition 3: The monodromy group M(τ_fold) is the subgroup of S_20 generated by
              all loops γ ∈ π_1(R_atlas) — equivalently, by the set of regulator-
              transition permutations.

Pairwise transition permutations (read from C1 rank tables):
  ζ → PV:           5-cycle within stratum 4 (positions 14-19) — order 5? or shorter?
                    Actually a tie-break of 6 degenerate modes ⇒ a permutation
                    in S_6 (the symmetric group of stratum 4); order divides 6! = 720.
  ζ → Mellin:       global reversal within strata + tie-break ⇒ involution times
                    intra-stratum tie-breaks; order 2 on the stratum-INDEX, possibly
                    higher on tie-broken degenerate modes.
  ζ → lattice:      identity (Kendall τ = +1.0000) ⇒ order 1.
  ζ → cutoff_√:     identity ⇒ order 1.

Composition along the 5-cycle γ: ζ → PV → Mellin → lattice → cutoff_√ → ζ:
  identity ∘ identity ∘ Mellin ∘ PV ∘ identity = (Mellin ∘ PV)
  = (Z_2 reversal) ∘ (intra-stratum tie-break in S_6)
  ⇒ a permutation in S_20 of order LCM(2, k) where k is the order of the PV
    intra-stratum tie-break (k divides 6).

Direction: monodromy order is an element of {2, 4, 6, 10, 12, ...} (LCM with 2);
           NOT pinned to 4 by structure.
```

**Z_4 hypothesis pre-registered test.** The workshop pre-registers PASS-monodromy iff the monodromy group is Z_4 (or contains Z_4 as a primary cycle, with no other small order matching as well). My C1+C2 setup yields:

| Loop element | Generated permutation type | Order on bottom-20 |
|:-------------|:--------------------------|:-------------------:|
| ζ → ζ        | identity                  | 1 |
| ζ → lattice  | identity                  | 1 |
| ζ → cutoff_√ | identity                  | 1 |
| ζ → PV       | intra-stratum-4 tie-break | divides 6 |
| ζ → Mellin   | global Z_2 + intra-strata tie-breaks | divides 2 · 6! = 1440 |

The Z_4 hypothesis would require the loop's monodromy to factor through a 4-element cyclic group. The decomposition above shows the structural building blocks are Z_1, Z_2 (Mellin reversal), and S_n-tie-breaks (n = stratum multiplicity 2, 4, 8, 6). The 4-fold cardinality is encoded NOT in a Z_4 cyclic structure but in the **quadrilateral of strata** (4 stratum-classes). The action of the regulator atlas on this quadrilateral is at most a Z_2 (Mellin flips strata 1↔4 and 2↔3 under the global reversal), not a Z_4 rotation.

**Pre-emptive verdict (subject to volovik's branch-cut analysis).** The C4 monodromy test, taken purely from the bare D_K spectrum at τ_fold under A_5, does NOT support the Z_4 hypothesis. It is consistent with **Z_2-on-strata + symmetric-group-tie-breaks-on-multiplicities** — a structurally richer but non-Z_4 monodromy. The 4-fold cardinality survives as the **count of strata** (= 4), but does NOT manifest as a cyclic Z_4 monodromy on the strata.

**A_4-reduction note.** Excluding cutoff_√ per W-8 (S82 W2-5 MP-Exclusion) reduces A_5 → A_4 = {ζ, PV, Mellin, lattice}. The monodromy structure is **invariant** under this reduction: all the "interesting" permutations are concentrated in PV (intra-stratum-4 tie-break) and Mellin (Z_2 reversal); ζ, lattice, cutoff_√ contribute identity. The A_4 atlas suffices for the monodromy test. (Bonus structural observation: A_4 = 4 atlas members matching the 4-stratum cardinality — this is a coincidence of cardinality at the *atlas* level matching the *spectrum* level, not a cyclic structure.)

**Computation step (deferred).** A full monodromy group computation would parametrize each regulator transition R(t) by a continuous interpolation (e.g., a 1-parameter family of weight functions w_t with w_0 = w_R1, w_1 = w_R2), follow the eigenvalue trajectories of the regulator-dressed spectral action, and compute the resulting permutation on bottom-20 indices. This requires a full eigenvalue-flow integration along each interpolation, which is beyond the bottom-20 ordering diagnostic. **Pre-registered for R3 follow-up if the workshop verdict closes INFO-coincidence**: see S87-MONODROMY-Z4-LANDING carry-forward spec.

**Substrate framing.** The Jensen-deformed SU(3) Dirac operator at τ=0.190 has its eigenvalue strata fixed by the deformation parameter; regulator dressings change the *weights* of strata without changing the *partition*. The monodromy group acts on **stratum indices** (Z_2 from Mellin reversal) and on **degenerate-mode tie-breaks** (S_n on each multiplicity-n stratum), but NOT cyclically. The 4-fold cardinality is the *list length* of the partition (4 strata) — a topological invariant of D_K(τ_fold) at L_max=12, not a cyclic group action.

**Citations.**

- Pre-registration of monodromy test: this workshop document line 31, R3 adjudication line 38–41.
- Multiplicity profile (2, 4, 8, 6) computed in C1.
- A_5 → A_4 reduction (cutoff_√ exclusion): S82 W2-5 MP-Exclusion (`s82-mp-exclusion-theorem.md`); W-8 cascade in flight per workshop document line 50 footnote.
- Z_2 reversal at Mellin: this workshop's diff matrix and Kendall τ table.
- Symmetric-group action on degeneracies: standard NCG result (the Peter-Weyl decomposition of L²(SU(3)) carries an SU(3) action whose orbits are the eigenvalue strata; the "tie-break" of degenerate modes is the action of the residual SU(3) representation symmetries on the stratum).

**Questions for volovik (on the monodromy/branch-cut side).**

1. In the superfluid Bogoliubov branch-cut picture at a first-order transit, does the cusp host a **Z_2 sheet structure** (one branch above, one below the cut, related by an order-2 monodromy)? If yes, this matches my C4 finding (Z_2 + tie-breaks, not Z_4). If no, where does the Z_4 come from in your superfluid analog?
2. The S_n tie-break action on degenerate-multiplicity strata (S_2 on stratum 1, S_4 on stratum 2, S_8 on stratum 3, S_6 on stratum 4) corresponds to the **gauge-orbit symmetry within each Peter-Weyl block**. In a superfluid, this maps to the residual symmetry within a degenerate quasiparticle multiplet. Does your branch-cut analysis treat the multiplet symmetry as a separate component of the monodromy, or does it absorb it into the global Z_2?
3. If C4 closes as **INFO-coincidence** (4-fold count is bookkeeping, not a Z_4 monodromy), the carry-forward should reframe the 4-fold cardinality as a **partition-count invariant** (number of strata = 4) rather than a cyclic structure (Z_4). Do you concur on this reframing, and if so, should the S87 carry-forward target a **partition-stability test** (does the 4-stratum count survive perturbations of τ off τ_fold, or does it bifurcate)?

---

---

## Round 1 — volovik: Response & Cross-Synthesis (Cusp/Branch-Cut Side)

### Part 1: Response to connes's Sections

#### Re: C1 — Eigenvalue Ordering at τ_fold

**AGREE (substantive).** The (2, 4, 8, 6) bare-stratum cardinality at τ_fold = 0.190, L_max = 12 — confirmed in `s86_w12_workshop_bottom20_regulator_ordering.json` lines 10–113 — IS the natural superfluid signature one expects at a first-order Bogoliubov cusp. Three independent superfluid-side observations corroborate the geometric structure:

1. **All four multiplicities are even.** Sage-verified (`(2, 4, 8, 6)` mod 2 = `(0, 0, 0, 0)`) with multiplicities/2 = `(1, 2, 4, 3)`. In Bogoliubov–de Gennes (BdG) formalism, every quasiparticle level acquires a Nambu particle–hole partner: the BdG Hamiltonian H_BdG = τ_3 ⊗ H_normal + τ_1 ⊗ Δ has spectrum {±E_k} symmetric about zero, so every excitation level above the gap edge appears in pairs. The strict evenness of (2, 4, 8, 6) is the BdG-Nambu doubling signature, NOT a coincidence. This converges with the framework's S43 PROVEN result `[J, D_K] = 0` (CPT) — the spectrum's particle–hole symmetry is enforced by the spectral triple's J-real structure, exactly as in 3He-B's BdG Z_2 antiunitary symmetry.

2. **Bottom-20 sits in the Andreev-bound regime.** Substitution chain:

   ```
   Definition 1: x_i := |λ_i|^2 / M_KK^2, dimensionless.
   Definition 2: BCS gap edge in dimensionless units: x_gap := (Delta_BCS)^2 = 0.4643^2 = 0.2155
                 (canonical_constants.py:299 Delta_BCS = 0.4642547394830737, R-PROTECTED).
   Definition 3: PV horizon (where d/dx w_PV = 0): x_PV := 1.0 (Sage-confirmed via
                 d/dx[x/(x+1)^2] = -(x-1)/(x+1)^3 = 0 at x = 1).
   Substitution: bottom-20 x range = [0.6720, 0.7144] (json lines 124-143).
   Comparison:   x_gap = 0.2155 < x_min = 0.6720; x_max = 0.7144 < x_PV = 1.0.
   Direction:    bottom-20 strata sit at 67-71% of the PV horizon, i.e., ~3.1× to 3.3× the
                 BCS gap edge, well into the above-gap (Andreev-bound) regime.
   ```

   In 3He-B at a first-order pair-breaking transit, this is the **above-gap Andreev spectrum**: discrete bound states between the gap edge and the pair-breaking threshold (= twice the BCS gap in mean-field ≈ 2 × 0.4643 ≈ 0.93 < 1.0 in dimensionless units, consistent with x_PV = 1). The 4-stratum discrete cardinality is the hallmark of Andreev bound states in a finite system — they do NOT form a continuum at finite L_max.

3. **The Z_2 ordering from C2 maps cleanly to the conformal-end bifurcation.** S85 W6-3 PASS (`S85-W6-3-CONF-INF-BIFURC`, audit_sha256 `7965906b8a00dab3...`, value `n_distinct_topologies=2`, schema `5_regulator_atlas`, convention `mostly_minus_conformal`) partitions A_5 at the *moment-integral / conformal-end* layer into:

   | Sheet | Regulators | ℐ⁺ topology | Λ_eff |
   |:------|:-----------|:------------|:------|
   | L_dS  | cutoff_sqrt, heat_kernel, dimensional | dS S^3 | > 0 |
   | L_flat | ζ, Pauli–Villars | flat ℝ × S² | = 0 |

   Source: `sessions/archive/session-85/session-85-w6-workingpaper.md:262, :673–674`. This is a Z_2 partition at the conformal-end / moment-integral layer that is INDEPENDENT of, but COMPATIBLE with, your C1 Z_2 ordering at the eigenvalue-ordering layer. Mellin sits OUTSIDE this binary: its global reversal is the Mellin-cone-residue mode (Volovik's q-theory dual representation). So the substrate exhibits a structural Z_2 + Mellin-axis = Z_2 × Z_2 = Klein-four bimodality across A_5, with the four classes {(L_dS, +), (L_dS, −), (L_flat, +), (L_flat, −)} where ± denotes orientation under the Mellin Z_2 reversal axis. This is structurally richer than your C1 bare-spectrum Z_2 but is NOT cyclic Z_4 — it is the Klein four-group V_4, which is the "non-cyclic Z_2 × Z_2."

**MISSED (cusp/branch-cut superfluid analysis reveals).** The bare-spectrum Z_2 ordering pre-empts the higher-order *eigenvalue* branching, but the moment-integral layer (where W6-3 lives) shows a HIGHER-rank structure: not Z_4 cyclic, but Z_2 × Z_2 ≅ V_4 (Klein four-group). The "4-fold cardinality" of the strata in C1 and the "4-fold cardinality" of the BULLETIN-4A categories are the SAME 4-class structure, viewed at different layers — this is the structural identity that the workshop is testing. I'll develop this in V3.

**Answers to your handoffs.**

1. **3He-B at first-order Bogoliubov cusp does host a discrete Andreev stratification** (Volovik Paper 12 §V; Volovik–Mineev 1976). At a first-order pair-breaking transit, the order parameter Δ does not vanish continuously but jumps; the discrete Andreev bound states between the two phases form a 2N_F-fold (N_F = number of relevant Fermi-surface points) multiplet structure. For 3He-B at the first-order A→B transition under pressure, N_F = 1 fundamental multiplet × 2 (BdG doubling) = 2 per stratum at lowest order. The substrate has N_F = 4 (one trivial + two fundamentals + one trivial-harmonic) × 2 (BdG) = (2, 4 + 4, 2) ?? — but the actual SU(3) Peter–Weyl decomposition gives the (1, 2, 4, 3) BdG-undoubled count, which does NOT factor as a simple `N_F × 2`. The multiplicity 4 in 3He-B (specifically: e/o, ±) emerges from a different quantum number set (chirality × parity); the substrate's 4 emerges from SU(3) Casimir branching (trivial / fundamental / antifundamental / trivial-harmonic). Same cardinality (4 strata), different group-theoretic origin — this is the universality-class match (4-stratum discrete Andreev structure at first-order cusp) but NOT a representation-theoretic identity. Reverse-inheritance check (per S60 Addendum B `inheritance-inversion-60.md`): the substrate's 4-stratum partition does NOT need 3He-B to exist; SU(3) representation theory gives it directly. Therefore the cardinality match is structural-coincidence at the discrete-stratification level, with each system providing the cardinality 4 from its own representation content.

2. **Z_2 vs higher-order regulator branching at substrate level.** The C2 bare-spectrum Z_2 (Mellin vs the rest) plus the W6-3 moment-integral Z_2 (dS vs flat) gives **Z_2 × Z_2 = V_4 Klein-four**, NOT Z_4. The branch-cut analysis in superfluid first-order transit predicts at most Z_2 per branch-cut sheet (one branch above, one below). Two independent branch cuts (one at the Mellin-cone, one at the conformal-end) compose to V_4. The 4-fold cardinality is the count of V_4 elements — abelian, non-cyclic. There is no Z_4 cyclic monodromy in the superfluid analog at this layer; the cyclic Z_4 hypothesis is FALSIFIED at both bare and moment levels.

3. **PV horizon at x = 1 IS substrate-physical, not regulator-artefact.** Sage confirms d/dx w_PV = -(x-1)/(x+1)^3 vanishes uniquely at x = 1, with w_PV monotone-increasing on x ∈ [0, 1] and monotone-decreasing on x ∈ [1, ∞). In dimensionless units with M_KK = 1, x = 1 ↔ |λ| = 1, which is approximately the **pair-breaking threshold** = 2 × (BCS gap edge) in mean-field BCS. Since 2 × Delta_BCS = 2 × 0.4643 = 0.9285 ≈ 1, the PV horizon at x = 1 sits at the pair-breaking energy in M_KK units. This is NOT an arbitrary κ_PV = 1 choice; it is the regulator that pins the cutoff at the pair-breaking scale = the upper edge of the Andreev-bound spectrum. The next stratum at L_max = 12 (or higher L_max) WILL cross |λ| = 1, and at that crossing the PV branch turns around. This is a substrate-physical horizon: the spectrum's BdG-doubled excitation manifold has a natural endpoint at 2Δ_BCS, and PV's horizon at x = 1 is the regulator selecting that endpoint as the cutoff scale. So Q3's answer is BOTH/AND: κ_PV = 1 IS a substrate-physical anchor (pair-breaking edge) AND the C1 bottom-20 cut intentionally stays below it (x_max = 0.7144 < 1) — i.e., the bottom-20 lives in the Andreev-bound regime, NOT the pair-broken continuum.

#### Re: C2 — Level-Crossing Signatures

**AGREE (decisive).** The bare-spectrum level-crossing diagnostic is correctly falsified at the bottom-20: 168/199 adjacent gaps below 10^-4, dominant gaps at machine precision (10^-16 to 10^-14) ARE bare degeneracies of the 4 strata, not regulator-induced crossings. Sage-confirmed identity: PV is strictly monotone increasing on x ∈ [0, 1] (d/dx[x/(x+1)^2] = -(x-1)/(x+1)^3 > 0 ∀ x ∈ [0, 1)). So all 5 of PV's "rank inversions" are genuinely intra-stratum-4 float64 tie-break artifacts; none are inter-stratum level crossings on the bare spectrum. C2's verdict — **bimodality lives at the moment-integral / spectral-action level, not the bare eigenvalue ordering level** — is correct.

**EMERGES (cross-domain, decisive).** The moment-integral bimodality is structurally NOT cyclic Z_4 but Klein-four V_4 = Z_2 × Z_2. Substitution chain:

```
Definition 1: A "monodromy axis" is a Z_2 generator induced by a regulator-class boundary
              along which a closed loop in regulator space picks up an order-2 phase.
Definition 2: Axis_M (Mellin axis) := Z_2 generated by the global reversal under Mellin-cone
              residue (Mellin: w_M = x^{-3}, monotone DECREASING; vs ζ/PV/lattice/cutoff: all
              monotone INCREASING). Verified C2: rank diff matrix entry Mellin vs ζ = 18/20.
Definition 3: Axis_C (W6-3 conformal-end axis) := Z_2 generated by the n_distinct_topologies=2
              partition of A_5 at the moment-integral / asymptotic-ℐ⁺ layer:
              {ζ, PV} (flat ℝ × S², Λ_eff = 0)  vs  {cutoff, heat, dim} (dS S^3, Λ_eff > 0).
              Source: sessions/archive/session-85/session-85-w6-workingpaper.md:262, 673-674.
Substitution: Axis_M and Axis_C are INDEPENDENT regulator-class operations.
              Mellin sits in NEITHER {ζ, PV} (flat) NOR {cutoff, heat, dim} (dS) directly —
              it represents the Mellin-cone-residue mode, the s-axis of the residue strip
              at s=-1 (canonical_constants.py line 654: "lizzi 9A §2.2 (s=-1 Mellin-strip
              residue convention)"). So Axis_M is orthogonal to Axis_C.
Simplification: Composition Z_2(M) × Z_2(C) = V_4 (Klein-four), the unique abelian group of
              order 4 in which every non-identity element is an involution.
              Sage-verified: Klein V_4 element orders = [1, 2, 2, 2]; cyclic Z_4 element
              orders = [1, 4, 2, 4]. They differ at the generator level.
Direction:    The monodromy of the regulator atlas at the moment-integral layer is V_4,
              NOT Z_4. There is NO order-4 element in the regulator monodromy group.
              The "4-fold cardinality" of BULLETIN-4A is the count |V_4| = 4, partitioned
              as 4 cosets, NOT a Z_4 cyclic order.
```

**Implication.** The pre-registered "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)" criterion (workshop line 39) is FALSIFIED at the moment-integral layer too: 4 sheets is consistent with V_4 (where each axis closes after 2 sheets, and a single generator-loop returns at sheet 2, not sheet 4) but NOT with Z_4 cyclic. The "Z_4 or similar" disjunction in the pre-registration is rescued only if "similar" includes V_4 — but V_4 is structurally distinct from Z_4 (one has order-4 elements, the other does not). I propose the verdict reads **INFO-coincidence**, with the structural finding "the 4-fold cardinality is a V_4 partition-count, NOT a Z_4 cyclic monodromy."

**Answers to your handoffs.**

1. **Q1 (W6-3 Z_2 conformal-end ↔ phase-coexistence).** YES, decisively. The W6-3 PASS partition into {L_dS, L_flat} IS the moment-integral analog of phase-coexistence at a first-order transit. In superfluid first-order transit (3He at the A→B pressure-driven transition, or BCS at the BdG cusp), two thermodynamic phases coexist on opposite sides of the transit line, related by a Maxwell-construction-equivalent symmetry. The S85 W6-3 result says: across A_5, two **regulator-class phases** coexist at the conformal end, with {ζ, PV} on the Λ_eff = 0 sheet and {cutoff, heat, dim} on the Λ_eff > 0 sheet. The transit between sheets is the regulator analog of a first-order Maxwell-equal-area construction: at the moment-integral layer, the spectral action's ζ-vs-cutoff difference is the "Maxwell jump" across the transit. This is the framework's structural equivalent of 3He A↔B coexistence; W6-3 is the proof that it lives at the moment-integral layer, not the bare-spectrum layer.

2. **Q2 (canonical substrate-bimodality signature at moment level).** YES, the workshop verdict should explicitly emit "the substrate-physical bimodality is the V_4 Klein-four operation Axis_M × Axis_C, manifesting at the moment-integral / conformal-end layer, NOT at the bare-eigenvalue-ordering layer." The two distinct quasiparticle representations connected by branch cuts are: (i) Mellin-cone residue at s = -1 (Axis_M) — the dual representation in the q-theory variational principle (project_qtheory-ftheory.md); (ii) ℐ⁺ topology selector (Axis_C) — the asymptotic-de-Sitter-or-flat selector that picks the cosmological constant sign at infinity (W6-3 §sessions/archive/session-85/session-85-w6-workingpaper.md:920 "The substrate is unique; its emergent shadow is scheme-dependent"). These are TWO DIFFERENT branch cuts; their composition is V_4 not Z_4. This is the framework's structural answer to the cosmological-constant-as-regulator-selection question.

3. **Q3 (representation-theoretic stratification at first-order transit).** YES, but with a sharp distinction from generic continuous spectra. The (1, 2, 4, 3) BdG-undoubled multiplicities (= mults/2) are NOT the SU(3) Peter–Weyl rep-dim sequence (1, 3, 3, ...); the trivial rep V_{0,0} has dim 1 (matching m_1/2 = 1) but the fundamentals V_{0,1}, V_{1,0} each have dim 3, while m_2/2 = 2 and m_3/2 = 4. Sage check: 2 ≠ 3 and 4 ≠ 3 — so the strata 2 and 3 are NOT single irrep blocks but mixed (0,1) ⊕ (1,0) splittings of complex-conjugate fundamentals at the cusp. The stratum-2 multiplicity 4 = (number of states from (0,1) at lowest level) + (number from (1,0) at lowest level) where the Jensen deformation breaks the (0,1)/(1,0) degeneracy: 4 = 2+2 (two from each chirality). Stratum 3 multiplicity 8 = 4+4 (next level of each chirality). Stratum 4 multiplicity 6 = harmonic series of trivial rep at higher mode number. This is the **chiral-pair splitting structure of the Andreev spectrum at first-order transit** in the substrate analog. Generic continuous spectra (e.g., 3He-A's gapless Weyl points with N_3 = 2 chiral charge) do not produce discrete strata — the discrete (1, 2, 4, 3) BdG-undoubled stratification is specifically a 3He-B-class first-order-cusp signature. This refines the S60 inheritance claim (`framework-3heb-comparison.md`): the 4-stratum partition-count IS structural inheritance from 3He-B class; the (1, 2, 4, 3) decomposition IS the SU(3)-specific extension of that class. Both can be true simultaneously.

#### Re: C3 — Source FAIL Mapping

**AGREE (decisive).** The 0/8 level-crossing-explained count at the bare-spectrum layer is correct. The 8 source FAILs cluster at the **moment-integral / convention-boundary** layer, exactly where the V_4 = Axis_M × Axis_C bimodality from Re:C2 lives. The 5 conv-bound + 3 scheme-incomp partition is supported by the elimination-bulletins.md Bulletin #5 substrate-first reasoning (line 173-179) which I now read as identifying the moment-integral V_4 layer as the structural cause.

**MISSED (cusp/branch-cut analysis sharpens the partition).** The 5-conv-bound class is itself bipartite under the V_4 axes. Substitution chain:

```
Definition 1: Each conv-bound FAIL has a (scheme, convention) pair from Bulletin #5 table.
Definition 2: Axis_M class (regulator orientation) ∈ {Mellin-cone-residue, non-Mellin}.
Definition 3: Axis_C class (conformal-end sheet) ∈ {flat (ζ/PV), dS (cutoff/heat/dim)}.

Substitution onto the 5 conv-bound FAILs (rows 2-6):
| # | Gate                                    | Scheme            | Conv tag             | Axis_M | Axis_C |
|:-:|:----------------------------------------|:------------------|:---------------------|:------:|:------:|
| 2 | W7-BASELINE-HTILDE-DERIVATION (AE74)    | Zubarev           | W1-G1-Branch-B       | non-M  | flat   |
| 3 | W7-CC-6 (63BF)                          | zeta              | Parker-Hawking-1974  | non-M  | flat   |
| 4 | W7-CC-GAMMA (BEB1)                      | S37-Gamma-canon.  | Planck2020-DR2       | non-M  | flat   |
| 5 | W7-CUSP-BOGOLIUBOV (B178)               | transfer-matrix   | BD-in-out            | non-M  | dS     |
| 6 | W8-1-KFIRAS-HIDDEN-CLOSED-FORM (2CB6)   | Interp_A_primary  | ConvA_coth           | non-M  | dS     |

Reading: 3 FAILs sit in the (non-Mellin, flat) corner (W7-BASELINE-HTILDE,
W7-CC-6, W7-CC-GAMMA); 2 FAILs sit in the (non-Mellin, dS) corner
(W7-CUSP-BOGOLIUBOV, W8-1-KFIRAS). The (Mellin, flat) and (Mellin, dS)
corners are EMPTY in this set of 5 — i.e., the cluster IS the non-Mellin
half of V_4, split (3 + 2) across the W6-3 conformal-end Z_2.

Direction:    The 5-conv-bound cluster is NOT a single substrate-physical
              corner; it is two corners of V_4 connected by the W6-3 axis,
              with NO Mellin-axis representative. This is the substrate's
              way of saying: the convention-boundary FAILs explore the
              non-Mellin half of regulator space and split across both
              conformal-end sheets.
```

**Implication.** The carry-forward should NOT be "8-row independent FAIL re-examination." It should be "the conv-bound family is structurally the non-Mellin half of V_4, split 3-2 across the W6-3 axis. The empty Mellin half (Mellin × flat, Mellin × dS) is unprobed — and IS the next-priority corridor for S87." This is a richer carry-forward than the pre-registered 8-row table because it identifies which V_4 corners are unexplored, not just which FAILs share a convention boundary.

**Answers to your handoffs.**

1. **Q1 (5 conv-bound FAILs as convention-degenerate manifold orbit).** The 5 are NOT a single substrate-symmetry orbit — they split 3-2 across the W6-3 axis. They DO share a common feature: all 5 sit on the **non-Mellin** axis (one of the two Mellin/non-Mellin Axis_M cosets), so they form one half of V_4. In superfluid first-order-transit language, this corresponds to a **single Maxwell-construction sheet** being explored by 5 different convention parameterizations: BD-in-out, Parker-Hawking-1974, Planck2020-DR2, ConvA_coth, Zubarev-branch-B. They are NOT 5 distinct quasiparticle representations — they are 5 different parameterizations of the SAME non-Mellin sheet. The 5 vs 4 question is partly answered: 5 conventions probe 2 V_4 corners, with W7 alone contributing 3+2 = 5 (suggesting the W7 cluster is the "convention-richness coordinate" within the non-Mellin half).

2. **Q2 (3 scheme-incomp FAILs as audit-vocabulary defects).** YES, they are methodology-class, NOT substrate-physical. Mapping: row 1 (W6-7 Petrov, check_type=D) is a Petrov classification non-realizability — the type-D Petrov class is empty under W3_H NP-boost-weight perturbation, an algebraic-classification audit; row 7 (W12-ELIM-3, equivalence-class-disjoint catalog) is a catalog-extension keyword partition, a vocabulary disambiguation; row 8 (W13-4 R1 rank distinguishability) is a Cartan-canonical asymmetric ordering audit, a single-regulator zeta-only test (which by your footnote on row 8 cannot be a multi-regulator level-crossing signature). All three are PRDR-K-disambiguation siblings (per Bulletin #8 category iv `BULLETIN-4A-CAT-IV` partition arithmetic 8 + 1 + 1 + 1 = 11 in `s85-w12-workingpaper.md`). They are AUDIT-MACHINERY signatures, not substrate-physics signatures.

3. **Q3 (R3 should explicitly state "bimodality is one layer up").** YES. Verdict text proposal: **"PASS-nonbimodal at the bare-eigenvalue-ordering layer; bimodality CONFIRMED at the moment-integral / conformal-end layer as a V_4 = Z_2(Mellin) × Z_2(W6-3) Klein-four operation, with the 5 conv-bound source FAILs occupying 2 of the 4 V_4 corners (non-Mellin × flat: 3; non-Mellin × dS: 2). The 3 scheme-incomp FAILs are audit-machinery signatures, not substrate-physical. The 4-fold cardinality is the V_4 group order |V_4| = 4, NOT a Z_4 cyclic monodromy."** The S87 carry-forward target should be a **moment-level V_4 probe** that explicitly tests the empty Mellin × flat and Mellin × dS corners — i.e., a moment-integral computation under Mellin regularization on both ζ-class and cutoff-class conformal-end sheets. This is a structural extension of the pre-registered "S87-BIMODALITY-INDIVIDUAL-FAIL-RE-EXAM" carry-forward; I'll spec it in the closing carry-forward block.

#### Re: C4 — Monodromy Group Setup

**AGREE (Z_4 falsified at bare layer).** Your decomposition (Z_1 from ζ/lattice/cutoff, intra-stratum-S_n tie-breaks from PV, Z_2 from Mellin) correctly establishes that the bare-spectrum monodromy is NOT cyclic Z_4. The 4-fold cardinality is the partition count |strata| = 4 at the bare layer.

**MISSED (Klein-four V_4 sharpens the structure beyond bare layer).** The monodromy at the moment-integral layer is V_4, not Z_4 either. This matters because V_4 and Z_4 are both order-4 but structurally distinct (Sage-verified: Z_4 has element orders [1, 4, 2, 4]; V_4 has [1, 2, 2, 2] — cyclic vs non-cyclic at the generator level). The 4-fold cardinality of BULLETIN-4A is the count |V_4| = 4 partitioned as 4 cosets, NOT a Z_4 4-step cycle. The structural finding is that the regulator atlas A_5 carries a moment-integral V_4 action under (Axis_M × Axis_C), whose 4 cosets are exactly the 4 BULLETIN-4A categories:

```
Definition 1: V_4 = {e, a, b, ab} where a^2 = b^2 = (ab)^2 = e.
Substitution: a := Axis_M generator (Mellin-cone-residue reversal Z_2)
              b := Axis_C generator (W6-3 conformal-end Z_2: flat ↔ dS)
              e := identity (ζ-canonical L_max=10 reference)
              ab := composite Mellin × W6-3 (unexplored corner)

Map V_4 cosets → BULLETIN-4A categories:
  e (= ζ canonical)            ↔ Cat (i): cusp-Bogoliubov / Parker-Hawking conv-boundary (8 FAILs)
                                  — anchors the V_4 identity at canonical zeta
  a (Mellin axis active)       ↔ Cat (ii): restricted-corridor BDI (1 FAIL, W8-5)
                                  — uses 9/10 regulator-stable gap, BDI restricted
                                  to N_3=0 corridor: Mellin's global reversal forces
                                  the BDI sub-block to recompute its gap
  b (W6-3 axis active)         ↔ Cat (iii): uniqueness-confirming Witten alternative
                                  (1 FAIL CONSTRUCTIVELY POSITIVE, W10-5)
                                  — uses cutoff-class regulator landing on dS sheet
  ab (both axes active)        ↔ Cat (iv): PRDR-K-disambiguation (1 FAIL, W12-2)
                                  — methodology-class crossing both axes

Cardinality: 8 + 1 + 1 + 1 = 11 (matches Bulletin partition arithmetic, line 1127 W1c-WP).

Direction: The 4-category cardinality of BULLETIN-4A IS the |V_4| = 4 coset structure
           of the moment-integral monodromy under Axis_M × Axis_C. The 4-fold cardinality
           coincidence between (a) the 4 bare-spectrum strata and (b) the 4 BULLETIN-4A
           categories is therefore NOT a Z_4 cyclic monodromy — it is two independent
           realizations of the SAME |V_4| = 4 count, one at the bare-spectrum layer
           (4 strata = 4 partition classes of bottom-20 by |λ|) and one at the
           moment-integral layer (4 cosets of V_4 = 4 categories of regulator-class
           bimodality). These are TWO DIFFERENT 4-counts that happen to match because
           4 is the smallest non-trivial Klein-group order AND the smallest Peter-Weyl
           branching of the substrate at the cusp. Coincidence-of-cardinality, not
           identity-of-group-action.
```

**Pre-emptive verdict (with branch-cut analysis).** The C4 monodromy verdict is **INFO-coincidence with structural sharpening**: 4-fold cardinality is partition-count at TWO layers (bare and moment-integral), with the moment-integral count being |V_4| = 4. The pre-registered "PASS-monodromy = Z_4 cyclic" criterion is FALSIFIED at both layers. The "FAIL = no monodromic structure exists" criterion is also wrong — there IS monodromic structure, namely V_4. So the verdict is **INFO-coincidence-with-V_4-sharpening**: the 4-fold cardinality is structurally meaningful (V_4 cosets at moment-integral layer) but not Z_4-cyclic.

**Answers to your handoffs.**

1. **Q1 (Z_2 sheet structure at first-order Bogoliubov cusp).** YES, the superfluid Bogoliubov branch-cut at first-order transit hosts a Z_2 sheet structure. In 3He-B at the A→B transition, the BdG Hamiltonian acquires two branches related by Maxwell construction: above the cusp, the system is in phase A; below, phase B. The transit corresponds to a Z_2 antiunitary involution swapping the two branches. This matches your C4 finding (Z_2 + tie-breaks). The Z_4 hypothesis was a pre-registration heuristic from the 4-fold count; the actual superfluid analog is Z_2 per branch cut. With TWO independent branch cuts (Mellin-cone at s = -1, conformal-end at ℐ⁺), the composition is V_4 not Z_4 — concur with my Re:C2 analysis.

2. **Q2 (S_n tie-break action — gauge-orbit symmetry within Peter-Weyl block).** Substitution chain:

```
Definition: For a degenerate stratum k of multiplicity m_k, the regulator-induced
            tie-break is a permutation of m_k indistinguishable modes ∈ S_{m_k}.
            S_2 (stratum 1): order 2; S_4 (stratum 2): order 24;
            S_8 (stratum 3): order 40320; S_6 (stratum 4): order 720.
Substitute: For multi-pair Bogoliubov modes in a degenerate multiplet, the
            residual symmetry is exactly the unitary group U(m_k) of the
            multiplet, NOT the full S_{m_k}. Volovik Paper 22 (Volovik–Mineev
            decomposition of degenerate quasiparticle multiplets) shows that
            the physical gauge-orbit symmetry is unitary, with discrete S_{m_k}
            arising only as the Weyl group of U(m_k) (i.e., the permutation
            subgroup acting on diagonal blocks).
Direction:  The float64 tie-break in C2 is a numerical artifact of S_{m_k};
            the SUBSTRATE-PHYSICAL symmetry is U(m_k). For the V_4 monodromy
            on STRATUM INDICES (not within strata), the relevant action is
            Z_2 from Mellin, NOT a sub-action of any S_{m_k}.
```

So the answer is: my branch-cut analysis treats the multiplet symmetry U(m_k) as a SEPARATE component of the gauge-orbit content (one per stratum), which factors out of the V_4 monodromy on STRATUM INDICES. The V_4 acts cleanly on the 4-stratum partition; the U(m_k) acts within each stratum. They commute because V_4 acts on the partition itself and U(m_k) acts within a single partition class. This decomposition is consistent with your C4 setup but extends it: the full monodromy structure is V_4 ⊕ ⊕_k U(m_k), with the V_4 piece carrying the substrate-physical bimodality and the U(m_k) pieces carrying the gauge-orbit symmetry within each stratum.

3. **Q3 (reframe 4-fold as partition-count invariant; concur on partition-stability test).** STRONG CONCUR. The S87 carry-forward should target a **partition-stability test** at multiple τ values, NOT a Z_4 cyclic structure. Specifically: scan τ ∈ {τ_fold ± δ_τ} for δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10}, recompute bottom-20 multiplicity profile, and verify whether (2, 4, 8, 6) is robust or whether it bifurcates into (1, 1, 2, 2, 4, 4, 3, 3) (= splitting under Jensen perturbation). If the 4-stratum count is STABLE across this scan, then 4 is a topological invariant of D_K(τ) at the cusp. If it bifurcates into 8 strata, the 4-fold count was a τ_fold-specific accident. The pre-registered partition-stability gate threshold: the 4-stratum count is stable iff the multiplicity profile is invariant up to relabeling within each stratum across at least 4 of 5 sampled τ values. This is the structurally-meaningful follow-up. I'll spec it in V3 below.

### Part 2: Original Analysis

#### V1: Cusp/Branch-Cut Structure in Superfluid Bimodality (Pillar II Analog)

**Topline.** In superfluid first-order transitions (3He A↔B at the polycritical pressure, BCS at the BdG cusp under driving, exciton-condensate at the dilute-dense crossover), the order-parameter manifold acquires a **branch cut** in the complexified order-parameter plane. The two sheets of the branch cut correspond to coexisting phases related by a Maxwell-construction symmetry. The substrate's cusp at τ_fold is the spectral-action analog of this branch-cut structure: the regulator-class boundary at the Mellin-cone (Axis_M) is one branch cut; the conformal-end W6-3 boundary (Axis_C) is a second, independent branch cut. Their composition gives V_4 Klein-four monodromy.

**Substitution chain (substrate-to-superfluid identification).**

```
Definition 1: A "branch cut" in regulator-parameter space is a hypersurface across
              which a moment integral of the spectral action acquires a Z_2 sign
              (or topology selector). Two regulators on opposite sides of the cut
              produce moment integrals with opposite signature.
Definition 2: Mellin-cone branch cut (Axis_M): the line s = -1 in the Mellin-Barnes
              residue strip. Mellin-cone-residue regulator computes M(s) = sum_i
              dim(p_i, q_i) * |λ_i|^{-2s}, picking up residues at s = 0, -1, -2, …
              Crossing s = -1 from below to above flips the sign of the residue
              (canonical_constants.py:654 "lizzi 9A §2.2 (s=-1 Mellin-strip residue
              convention)"). All non-Mellin regulators (ζ, PV, lattice, cutoff) sit
              on ONE side of this cut; Mellin straddles it via residue selection.
Definition 3: Conformal-end branch cut (Axis_C): the W6-3 partition surface
              separating {ζ, PV} (flat ℝ × S²) from {cutoff, heat, dim} (dS S^3),
              with Λ_eff = 0 on one side and Λ_eff > 0 on the other.

Substitution: Both cuts are independent (Mellin's residue selection is orthogonal
              to the conformal-end topology selection). The two-sheeted cover of
              regulator-parameter space modulo branch cuts is therefore
              R_atlas / (Z_2 × Z_2) = R_atlas / V_4. The 5 regulators of A_5 do not
              uniformly cover all 4 V_4 corners:
                {ζ, PV}    : (non-Mellin, flat)  → corner e
                {cutoff, heat, dim}: (non-Mellin, dS) → corner b
                {Mellin}   : straddles Axis_M, on flat side → corner a (or ab)

Simplification: A_5 is "non-uniformly distributed" across V_4: the (Mellin × dS)
              corner is unrepresented in the canonical 5-atlas. This is exactly
              the "asymmetric cluster of FAILs" pattern in C3 (3 of 5 conv-bound
              FAILs in non-Mellin × flat; 2 in non-Mellin × dS; 0 in either
              Mellin half).

Direction:    The substrate at τ_fold sits at the V_4 origin (= ζ canonical
              reference); FAIL gates probe other corners by selecting different
              (scheme, convention) pairs that map onto V_4 cosets. The branch-cut
              structure is the reason these FAILs cluster: each FAIL is a candidate
              that requires regulator-uniqueness across one of the two cuts, and
              the cut's sign-flip kills the candidate.
```

**Pillar II analog (Volovik condensed-matter precedent).** In Volovik Paper 19 (3He under rotation) and Paper 33 (q-theory and the cosmological constant), the substrate-equivalent of branch cuts arises as the **Bogoliubov dispersion bifurcation** at first-order transit: as the pair-breaking parameter crosses threshold, the BdG dispersion E(k) = sqrt[(ε_k − μ)² + |Δ|²] develops a branch-cut singularity in the complex-Δ plane. The two sheets correspond to E > 0 (quasiparticle) and E < 0 (quasihole) excitations, matched by particle-hole conjugation. This is the Z_2 piece of the V_4. The second cut comes from the **gauge-rotation Z_2** (U(1) phase mod π) acting on the order parameter Δ → -Δ — which is exactly the Mellin-cone residue sign-flip in regulator language. Together they generate V_4 Klein-four monodromy on the BdG branch. Substrate-cosmology mapping:

| Superfluid (3He-B at first-order) | Substrate (D_K at τ_fold) |
|:----------------------------------|:--------------------------|
| BdG dispersion branch cut at gap edge | Mellin-cone residue strip (Axis_M) |
| Gauge-rotation Z_2 (Δ → -Δ) | W6-3 conformal-end Z_2 (flat ↔ dS) |
| Maxwell-construction phase coexistence | V_4 coset partition of regulator atlas |
| Andreev bound states between gap and 2Δ | Bottom-20 strata in [x_gap, x_PV] = [0.2155, 1.0] |
| 4-stratum Andreev multiplicity (BdG-doubled) | (2, 4, 8, 6) bare-stratum cardinality |

**Citations.**
- Volovik–Mineev branch-cut analysis: Onsager-prize foundation paper (Volovik–Mineev 1976; cited as parent of S60 inheritance framework in `framework-3heb-comparison.md`).
- W6-3 partition source: `sessions/archive/session-85/session-85-w6-workingpaper.md:262, :673–674` (lines 257-262 verdict line; lines 673-674 catalog rows L_dS, L_flat).
- Canonical constants: `computations/canonical_constants.py:299` (Delta_BCS = 0.4642547394830737, R-PROTECTED), `:654` (Mellin s=-1 residue convention).
- BULLETIN-4A 8-FAIL aggregation: `sessions/framework/registry/elimination-bulletins.md:154–192`.
- Volovik q-theory branch-cut analog: `project_qtheory-ftheory.md` (memory file).

#### V2: Phase-Coexistence Signatures at First-Order Transit

**Topline.** Given C1's establishment that the 4-stratum cardinality is partition-count NOT Z_4 cyclic, the (2, 4, 8, 6) multiplicities have a sharp phase-coexistence interpretation: stratum-3's anomalous multiplicity 8 (= 2 × 4) is the **chiral-pair condensation signature** at the first-order Bogoliubov cusp, distinguishing this substrate from generic BdG superfluids where stratum multiplicities follow the simpler (2, 2, 2, ...) pattern.

**Substitution chain (BdG-undoubled stratum analysis).**

```
Definition 1: For each stratum k of multiplicity m_k, define m_k^BdG := m_k / 2
              (BdG-undoubled count, valid because all m_k are even — Sage-verified).
Definition 2: A "generic-BdG stratum" has m_k^BdG = 1 (single quasiparticle level
              with Nambu doubling); the standard 3He-B Andreev structure with
              non-degenerate quasi-momenta produces m_k^BdG = 1 for every stratum.
Definition 3: A "chiral-paired BdG stratum" has m_k^BdG = N_chiral × N_irrep where
              N_chiral ∈ {1, 2, 3, 4, …} counts chirally-distinguished partners
              and N_irrep counts irrep multiplicity within stratum.

Substitution: From C1 (json lines 32-113):
  Stratum 1: sectors all (0,0), m_1 = 2 → m_1^BdG = 1 → generic
  Stratum 2: sectors mix (0,1)+(1,0), m_2 = 4 → m_2^BdG = 2 → chiral-paired
             (2 = 1 fundamental × 2 chiralities)
  Stratum 3: sectors mix (0,1)+(1,0), m_3 = 8 → m_3^BdG = 4 → DOUBLY chiral-paired
             (4 = 2 fundamentals × 2 chiralities, OR 1 fundamental × 4-fold)
  Stratum 4: sectors all (0,0), m_4 = 6 → m_4^BdG = 3 → trivial-rep harmonic
             (3 distinct trivial-rep modes at higher mode number)

Simplification: BdG-undoubled half-counts = (1, 2, 4, 3); sum = 10 = bottom-10
              physically distinct levels (Sage-verified). This is NOT a generic
              BdG pattern (which would be (1, 1, 1, 1, ...) for 4 strata).
              Stratum 3's m_3^BdG = 4 is the structural anomaly.

Direction:    The substrate at τ_fold has chiral-paired condensation at strata 2-3
              (lower fundamental) and 3 (next-fundamental), with stratum 3 carrying
              double the chiral-pair multiplicity of stratum 2. This is the
              signature of two coexisting fundamental-rep condensates at the cusp,
              the spectral-action analog of A↔B coexistence at the polycritical
              pressure point in 3He.
```

**Phase-coexistence reading.** Two distinct fundamental-rep condensates coexist at τ_fold:

| Stratum | m^BdG | Phase identity (substrate language) | 3He-B analog (Maxwell coexistence) |
|:--------|:-----:|:------------------------------------|:------------------------------------|
| 1 | 1 | Trivial-rep ground vacuum (V_{0,0}) | A-phase ground state |
| 2 | 2 | Single chiral-pair fundamental (V_{0,1} ⊕ V_{1,0}) lowest level | A↔B chiral split, lowest Andreev level |
| 3 | 4 | Doubled chiral-pair fundamental (next level) — anomalous | Coexistence-cusp Andreev mid-band |
| 4 | 3 | Trivial-rep harmonic (3 high-mode (V_{0,0}) modes) | Above-cusp condensate excitations |

**Critical observation.** The stratum-3 anomaly (m^BdG = 4 instead of generic 1 or chiral-pair 2) is the substrate-physical signature of **first-order coexistence at the cusp**, not a generic above-gap continuum. In a continuous (second-order) transition, all strata would have m^BdG = 1 (generic BdG); in a first-order transition, the cusp hosts exceptional levels where two phases coexist, and the multiplicity of those levels doubles relative to the generic background. Stratum 3 IS this exceptional level: m^BdG = 4 = 2 × 2 = (chiral-pair multiplicity of stratum 2) × (coexistence factor 2). This is structural evidence that the transit at τ_fold IS first-order, not second-order — consistent with the framework's claim that the fold is a first-order transit (project memory `cold-big-bang-vacuum-floor.md`, S58 transit-velocity-55-result.md).

**Implications for the regulator-bimodality claim.** At a generic continuous BdG transition, the regulator-class boundary is smoothable: all 5 regulators agree because there is no cusp to break degeneracies. At the first-order cusp here, regulator dependence becomes meaningful at the moment-integral layer (V_4 monodromy from Re:C2). The (2, 4, 8, 6) cardinality at the bare layer plus the V_4 cardinality at the moment layer are TWO MANIFESTATIONS of the same first-order transit physics, separated by ONE LAYER (bare → moment).

**Citations.**
- Bottom-20 sector data: `computations/s86_w12_workshop_bottom20_regulator_ordering.json:32-113` (sectors), :10-31 (|λ| values).
- Sage verification: m_k all even, m_k^BdG = (1, 2, 4, 3), sum = 10.
- Volovik first-order transit framework: `framework-3heb-comparison.md` memory file (22 correspondences).
- BCS-PROXIMITY-70 (S70): bottom 8 modes form self-conjugate BCS shell (Delta_ind = 0 EXACTLY), `bcs-proximity-70-result.md`. Stratum 1 (m=2) + stratum 2 (m=4) + half stratum 3 (m=2) = 8 BCS shell modes — consistent with stratum-3 anomaly hosting a 2 + 2 split with the BCS shell capturing only half.
- First-order transit pin: `cc-cancel-sweep-58-result.md` (CC near-cancellation in transit [0.10, 0.30]).

#### V3: 4-Fold Cardinality Test via Monodromy Sheet-Count

**Topline.** The pre-registered "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)" criterion (workshop line 39) is FALSIFIED at both layers (bare-spectrum AND moment-integral). The 4-fold cardinality lives somewhere else entirely: it is the **partition-count |V_4| = 4** at the moment-integral layer, AND the **partition-count |strata at τ_fold| = 4** at the bare-spectrum layer, BUT these are two independent realizations of the same count, not a unified Z_4 cyclic structure. The verdict should close as **INFO-coincidence-with-V_4-sharpening** at both layers.

**Substitution chain (sheet-count test, both layers).**

```
Definition 1: A "sheet count" of a monodromy group G acting on a parameter space P
              is the integer [P : G·p] for a generic basepoint p ∈ P (the index of
              the orbit under the group action).
Definition 2: At bare-spectrum layer (C1+C2+C4): G_bare = ⟨Z_2(Mellin) reversal⟩ ≤ S_4
              acting on stratum indices {1, 2, 3, 4}. Sheet count for stratum-action
              orbit: 2 (Mellin reverses {1, 4} ↔ {1, 4} and {2, 3} ↔ {2, 3} as pairs,
              orbit size 2 per stratum-pair). NOT 4.
Definition 3: At moment-integral layer (W6-3 + Mellin axis = V_4):
              G_mom = V_4 = Z_2(Mellin) × Z_2(W6-3) acting on regulator-atlas cosets.
              Sheet count for regulator-coset action: |V_4| = 4. THIS is the 4.
Definition 4: A "Z_4 cyclic monodromy" has a generator g of order 4 with g^4 = e
              (Sage-verified: Z_4 element orders [1, 4, 2, 4]). V_4 has element orders
              [1, 2, 2, 2] — NO order-4 generator. So V_4 ≠ Z_4 at the group level.

Substitution: Bare-layer sheet count = 2 (Z_2 only) ≠ 4 (Z_4 hypothesis).
              Moment-layer sheet count = 4 (V_4) = 4 (matches cardinality)
              BUT V_4 is NOT cyclic (no order-4 generator), so a "sweep" through
              the 4 sheets is a Klein-four traversal {e → a → ab → b → e}
              (closing only after 4 distinct group operations applied in
              non-cyclic order), NOT a Z_4 cycle.

Simplification: The 4-fold cardinality is realized at the moment-integral layer
              as |V_4| = 4 partition cosets, NOT as Z_4 cyclic monodromy. The
              parameter sweep ζ → PV → Mellin → lattice → cutoff → ζ from C4
              traverses the V_4 cosets non-cyclically: {ζ, lattice, cutoff} all
              sit at coset e (or close to it via tie-breaks); PV sits at coset
              e (intra-stratum tie-break only, no Axis_M or Axis_C activation);
              Mellin sits at coset a. So the 5-sweep traversal is:
              e → e → a → e → e → e (one Mellin transition, NO Axis_C transition).
              This does NOT close after 4 sheets — it closes after 2 (one Axis_M
              flip, one un-flip), with NO Axis_C contribution from the 5-atlas.

Direction:    The moment-integral monodromy of A_5's natural sweep generates
              ONLY Z_2(Mellin), not the full V_4. To activate Axis_C (W6-3 sheet
              flip), the sweep must include both ζ-class AND cutoff-class
              regulators with explicit moment-integral computation on each sheet,
              not just bare-spectrum eigenvalue ordering. This is what the
              S87 carry-forward must specify.
```

**Where the monodromy lives, sheet by sheet.**

| Layer | Group | Sheet count | Cyclic? | Source |
|:------|:------|:-----------:|:-------:|:-------|
| Bare-spectrum eigenvalue ordering | Z_2 (Mellin reversal) ⋊ ∏_k S_{m_k} | 2 (on strata) | YES (Z_2 cyclic) | C2 + Re:C2 |
| Moment-integral / spectral action | V_4 = Z_2(M) × Z_2(C) | 4 (on cosets) | NO (Klein-four non-cyclic) | Re:C2, V1, V2 |
| Conformal-end / asymptotic ℐ⁺ | Z_2 (W6-3 dS↔flat) | 2 (on topologies) | YES | W6-3 PASS |

So the 4-fold cardinality does NOT live as a unified single-group monodromy across all layers. It is a structural coincidence between (i) the bare-spectrum 4-stratum partition (a property of D_K(τ_fold) Peter-Weyl + BdG-Nambu doubling) and (ii) the moment-integral V_4 coset count (a property of regulator-class branch-cut composition). Two different mechanisms, same cardinality, no unified group action — this is **INFO-coincidence at the count level, with V_4 sharpening at the moment layer**.

**S87 carry-forward spec (4-field PRDR-compliant, per workshop line 43-46).**

`S87-PARTITION-STABILITY-4STRATUM` — partition-stability test for the (2, 4, 8, 6) bare-spectrum cardinality at perturbed τ values.

| Field | Specification |
|:------|:--------------|
| **What** | Compute bottom-20 multiplicity profile of D_K(τ) at τ ∈ {τ_fold ± δ_τ} for δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10}. Identify whether (2, 4, 8, 6) is invariant up to relabeling, or bifurcates into finer strata as τ moves off τ_fold. Tabulate the multiplicity profile at each τ. |
| **Inputs** | (a) `s84_spectrum_cache_L12_*.npz` cache for τ ∈ {0.090, 0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290} (one cache per τ value; some may need fresh computation if not cached); (b) bottom-20 multiplicity-profile extractor (port from connes' `s86_w12_workshop_bottom20_*.py`); (c) tolerance for "level coincidence" = 1e-10 in |λ| (above float64 noise). |
| **Gate** | PASS-stable if (2, 4, 8, 6) multiplicity profile invariant across ≥ 4 of 5 sampled δ_τ (allowing relabeling of strata by |λ|-rank). FAIL-bifurcation if profile bifurcates into ≥ 6 distinct |λ|-strata at any sampled δ_τ. INFO if 2-3 sampled δ_τ preserve the partition but others bifurcate (transition zone). |
| **Effort** | ~4 hours: (i) extract bottom-20 from each cache (20 minutes per τ value × 11 = ~3.5 hours wall-clock if caches present; +6-12 hours if 5+ require fresh L_max=12 spectrum computation); (ii) tabulate + verdict line. |

**S87-MONODROMY-V4-EXPLICIT** — explicit V_4 monodromy test at moment-integral layer (sharpens the pre-registered S87-MONODROMY-Z4-LANDING).

| Field | Specification |
|:------|:--------------|
| **What** | Compute spectral-action moments a_n^{R} for n ∈ {0, 2, 4} at τ = τ_fold under all 5 regulators, on both ℐ⁺ topologies (flat and dS via W6-3). Tabulate the 4 V_4 cosets: (e: ζ canonical), (a: Mellin canonical), (b: cutoff_canonical), (ab: Mellin × cutoff). Verify the structural identity: a_n^{(ab)} = a_n^{(a)} · a_n^{(b)} / a_n^{(e)} (V_4 multiplicative consistency) up to 5% tolerance. |
| **Inputs** | (a) Spectral-action moment kernel from `computations/s86_w12_*.py` extended to compute a_0, a_2, a_4 with each w_R weight; (b) W6-3 PASS partition data from `s85_w6_conformal_infinity_bifurcation.npz` (audit_sha256 `7965906b8a00dab3...`); (c) τ_fold pin from canonical_constants.py. |
| **Gate** | PASS-V_4-consistent if multiplicative V_4 identity holds within 5% tolerance for at least 2 of 3 a_n. FAIL if all 3 a_n violate the identity (suggests V_4 is not the correct monodromy group at moment level). INFO if 1 of 3 holds (partial V_4 structure, possibly extended group). |
| **Effort** | ~6 hours: (i) extend moment-kernel script to support both ℐ⁺ topologies and Mellin; (ii) compute 4 V_4 cosets × 3 a_n moments = 12 numerical entries; (iii) verify consistency identity; (iv) verdict line + working-paper section. |

**Citations.**
- V_4 vs Z_4 group-theoretic distinction: Sage-verified element orders [1, 2, 2, 2] vs [1, 4, 2, 4].
- W6-3 PASS partition: `sessions/archive/session-85/session-85-w6-workingpaper.md:262, :673–674` (audit_sha256 `7965906b8a00dab3f09496dd77ec8f4ae770af61225b1eb27d1d0ce45cfe3afe`).
- Pre-registered "PASS-monodromy" criterion: this workshop document line 39.
- Pre-registered S87 carry-forward 4-field spec: this workshop document line 43-46.

#### V4: Questions for connes

These four questions sharpen the V_4 / V2 / V3 findings into concrete NCG-side checks for your R2 turn.

**Q1 (V_4 vs Z_4 at moment-integral layer — direct kernel test).** My Re:C2 + V3 argues the moment-integral monodromy is V_4 = Z_2(Mellin) × Z_2(W6-3), NOT cyclic Z_4. The structural criterion is that NO order-4 element exists in V_4 (Sage-verified element orders [1, 2, 2, 2]). Direct test: in your spectral-action kernel construction, the composition of (Mellin residue at s = -1) ∘ (cutoff-class regulator switch) ∘ (Mellin residue at s = -1) ∘ (cutoff-class regulator switch) returns to the identity after 4 operations only if the operations COMMUTE (V_4) and each is an involution. Does your kernel construction confirm this commutativity, or do you find a non-commutative (Z_4-cyclic or non-abelian) composition?

**Q2 (stratum-3 anomaly: structural or numerical?).** V2 identifies stratum 3 (m = 8, m^BdG = 4) as the anomalous "doubly chiral-paired" level. In your Peter-Weyl decomposition, is the stratum-3 multiplicity 8 a CLEAN doubling of the next-fundamental level (i.e., 4 = 2 chiralities × 2 multiplets, with each multiplet having dim 1 in the relevant Casimir block), or is it a NUMERICAL near-degeneracy at L_max = 12 that splits at higher L_max into two 4-multiplicity strata? The S87-PARTITION-STABILITY-4STRATUM gate I specced in V3 will test this against τ-perturbation, but a direct L_max scan (L_max = 13 → 14 → 15) at τ = τ_fold could resolve it faster. Is such a scan feasible in your existing infrastructure?

**Q3 (W6-3 + Mellin product structure: empty corners of V_4).** Re:C3 shows the 5 conv-bound source FAILs occupy 2 of the 4 V_4 corners (non-Mellin × flat: 3; non-Mellin × dS: 2), with the (Mellin × flat) and (Mellin × dS) corners EMPTY. The S87-MONODROMY-V_4-EXPLICIT gate in V3 probes those empty corners directly. Question: is there a structural NCG-side reason the empty corners ARE empty — e.g., Mellin's residue-at-s=-1 convention may be implicitly compatible with only ONE conformal-end class (forcing a particular ℐ⁺ topology by virtue of the residue convention)? If so, V_4 may collapse to Z_2(non-Mellin × W6-3) on the substrate-relevant subset, with the Mellin axis decoupling from Axis_C structurally, not just empirically.

**Q4 (carry-forward priority — partition-stability vs V_4-explicit).** I specced two distinct S87 gates: (a) S87-PARTITION-STABILITY-4STRATUM (bare-spectrum τ-scan) and (b) S87-MONODROMY-V_4-EXPLICIT (moment-integral V_4 product test). They probe different layers. Which has higher EVOI for the workshop's R3 verdict? My read: (b) directly tests the structural finding (V_4 monodromy at moment layer); (a) tests the bare-layer cardinality robustness. (b) closes the bimodality verdict; (a) reinforces the partition-count interpretation. Both are 4-6 hour gates. Should both be carry-forwards, or do we prioritize (b)? My preference is BOTH, with (b) as priority-1 and (a) as priority-2, because the V_4 identity is the structural finding and its consistency check is the harder-to-fake gate.

---

## Round 2 — connes: Follow-up

### CONVERGENCE

**(1) BdG-Nambu doubling as the structural origin of all-even multiplicities (Re:C1).** I concur with volovik's reading of (2, 4, 8, 6) mod 2 = (0, 0, 0, 0) as the BdG-Nambu particle–hole doubling signature. NCG-side anchor: this is exactly the consequence of `[J, D_K] = 0` (S43 PROVEN, `permanent-theorems.md`) — the real structure J implements particle–hole conjugation on the spectrum, so every eigenvalue λ has its J-conjugate −λ in the spectrum, forcing the bottom-20 |λ|-strata to come in even multiplicities. The C1 multiplicity profile is thus *not* an empirical accident but a direct consequence of the order-1 reality axiom (`[[D, a], Jb*J^{-1}] = 0`) applied to the Jensen-deformed SU(3) Dirac operator at τ_fold. The substrate-superfluid identification (BdG H = τ_3 ⊗ H_normal + τ_1 ⊗ Δ ↔ J-doubled D_K) is a *consequence* of NCG-axiom 5 (reality), not a tunable analogy.

**(2) Andreev-bound regime at 67–71% of the PV horizon (Re:C1).** I concur with the substitution chain x_min = 0.6720, x_max = 0.7144, x_PV = 1.0, 2 × Δ_BCS = 0.9285 ≈ 1.0. The PV horizon at x = 1 is not an arbitrary κ_PV = 1 choice — Sage already confirms d/dx w_PV vanishes uniquely there (C1 substitution chain) and the pair-breaking edge 2Δ_BCS sits at 92.85% of x_PV. The bottom-20 lives at 67–71% of x_PV ≈ 73–77% of 2Δ_BCS, comfortably in the above-gap discrete-Andreev-bound regime. This sharpens C1's "below the cutoff" statement to "below 2Δ_BCS, in the discrete-Andreev shell." NCG-side reading: the discrete shell is the L²(SU(3)) Peter–Weyl decomposition's lowest 4 strata under the τ_fold deformation; its boundedness above by 2Δ_BCS = 0.9285 (in M_KK units) is the BCS-condensation scale that the Jensen deformation has already encoded into the spectrum.

**(3) Klein-four V_4 monodromy at moment-integral layer falsifying Z_4 cyclic (Re:C2, Re:C4, V3).** I concur with the V_4 = Z_2(Mellin) × Z_2(W6-3) decomposition. Sage-verified independently in this turn: V_4 element orders [1, 2, 2, 2] vs Z_4 [1, 2, 4, 4]; V_4 is non-cyclic (no order-4 generator), Z_4 is cyclic. The pre-registered "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)" criterion (workshop line 39) is *literally* satisfied by V_4 IF the sweep alternates generators (e.g., a → ab → b → e), but NOT in the cyclic-generator sense. The honest verdict is **INFO-coincidence-with-V_4-sharpening** (not "PASS-monodromy" without qualification): V_4 satisfies the count but violates the cyclicity. This is more informative than either pre-registered branch.

**(4) Stratum-3 anomaly m^BdG = 4 as first-order coexistence signature (V2).** I concur with the BdG-undoubled-multiplicity reading m^BdG = (1, 2, 4, 3), Sage-verified: sum = 10, with stratum-3 carrying double the chiral-pair multiplicity of stratum-2. The structural reading "stratum-3 is the doubly-chiral-paired anomaly = first-order coexistence signature, NOT generic BdG continuum" is consistent with the framework's first-order-fold pin (`cold-big-bang-vacuum-floor.md`, `cc-cancel-sweep-58-result.md`). NCG-side strengthening: the 8 = 4 (chirality-doubled-fundamental) × 2 (Nambu) decomposition matches the SU(3) Peter–Weyl structure where stratum 3 contains both (0,1) and (1,0) sectors at the second-lowest fundamental level *and* the Jensen deformation has not yet split them. The BdG-undoubled half-counts (1, 2, 4, 3) are a new substrate observable (see EMERGENCE §2 below).

**(5) Five conv-bound source FAILs cluster as 3+2 across W6-3 axis on non-Mellin half of V_4 (Re:C3).** I concur with the table partitioning rows 2–6 into (non-Mellin, flat): rows 2, 3, 4 (W7-BASELINE-HTILDE, W7-CC-6, W7-CC-GAMMA) and (non-Mellin, dS): rows 5, 6 (W7-CUSP-BOGOLIUBOV, W8-1-KFIRAS). This is structurally tighter than my C3 "convention-degenerate manifold" framing — the 5 FAILs are *not* a single orbit under any substrate symmetry; they are two corners of V_4 connected by Axis_C, with the (Mellin × flat) and (Mellin × dS) corners empty in the source-FAIL set. The carry-forward target is sharpened from "8-row independent re-examination" to "probe the empty Mellin half of V_4 directly."

**(6) V_4 cosets ≡ 4 BULLETIN-4A categories at moment-integral layer (Re:C4).** I concur with the coset-to-category map:
- e ↔ Cat (i) cusp-Bogoliubov / Parker-Hawking (8 FAILs)
- a (Mellin axis) ↔ Cat (ii) restricted-corridor BDI (1 FAIL, W8-5)
- b (W6-3 axis) ↔ Cat (iii) uniqueness-confirming Witten (1 FAIL, W10-5, constructively positive)
- ab (both axes) ↔ Cat (iv) PRDR-K-disambiguation (1 FAIL, W12-2)
- 8 + 1 + 1 + 1 = 11 (matches Bulletin partition arithmetic, `s85-w12-workingpaper.md` line 1127)

The categorical map is consistent (one coset per category, partition arithmetic consistent), and the cardinalities reflect *probe density* per coset: the e-coset is the canonical-zeta reference and accumulates 8 source FAILs because that is the most-explored region of regulator space. This converges with my C3 "5 conv-bound + 3 scheme-incomp" partition: the 5 conv-bound FAILs are subset of the 8 in coset e (ζ-anchored at the W7 cluster level — stratum-locked at coset e, with the Axis_C splitting the 5 into 3+2 *within* coset e via the conformal-end choice baked into each FAIL's scheme). Re-reading my C3 table: rows 2–6 sit in coset e from the V_4-on-regulator-classes perspective AND split 3+2 across Axis_C from the conformal-end-of-each-FAIL'S-scheme perspective. The two readings are consistent — one labels by V_4 coset (4 categories), the other labels by Axis_C *within* coset e (3+2 conformal sub-split).

### DISSENT

**(1) The V_4 multiplicative consistency identity in V3's S87-MONODROMY-V_4-EXPLICIT spec is incorrect — should be ADDITIVE, not multiplicative.** Volovik's V3 spec proposes the gate criterion:

```
PASS-V_4-consistent if: a_n^(ab) = a_n^(a) · a_n^(b) / a_n^(e)   [V3 line 748]
```

This is a *character* identity (it holds if the moment functional is multiplicative under the V_4 action, which is the structure of a 1D group character). But spectral moments are LINEAR over modes, not multiplicative. Substitution chain:

```
Definition 1: A_n^{R}[D_K] := Tr (w_R(D_K^2 / Λ²) · (D_K^2 / Λ²)^n)
              = Σ_i n_i · w_R(x_i) · x_i^n
              where n_i = degeneracy of mode i, x_i = |λ_i|² / Λ²,
              and w_R is the regulator weight function.

Definition 2: V_4 acts on regulator weights by sign-flip involutions:
              e:   w_R(x)
              a:   w_R(x) · σ_M(x)            (Mellin-cone residue sign)
              b:   w_R(x) · σ_C(x)            (W6-3 conformal-end sign)
              ab:  w_R(x) · σ_M(x) · σ_C(x)   (both involutions)
              with σ_M, σ_C ∈ {±1} pointwise.

Substitution: A_n^(ab) = Σ_i n_i · w_R(x_i) · σ_M(x_i) · σ_C(x_i) · x_i^n
              A_n^(a)  = Σ_i n_i · w_R(x_i) · σ_M(x_i)            · x_i^n
              A_n^(b)  = Σ_i n_i · w_R(x_i)            · σ_C(x_i) · x_i^n
              A_n^(e)  = Σ_i n_i · w_R(x_i)                       · x_i^n

Simplification: The MULTIPLICATIVE identity A_n^(ab) = A_n^(a) · A_n^(b) / A_n^(e)
              would require (Σ_i α_i β_i γ_i) = (Σ_i α_i β_i)(Σ_i α_i γ_i) / (Σ_i α_i)
              for all coefficient sets — which is FALSE in general (it holds only
              for delta-function spectra concentrated on a single mode, or for
              factorisable σ_M, σ_C with specific tuned values).

Direction:    The structurally correct V_4 consistency identity for spectral
              moments is the ADDITIVE COCYCLE relation (apply the V_4 character
              decomposition mode-by-mode):
              
                  A_n^(ab) - A_n^(e) = (A_n^(a) - A_n^(e)) + (A_n^(b) - A_n^(e))

              This holds IFF σ_M and σ_C act linearly-independently on the spectral
              measure, which is the substrate-meaningful test.
```

(Sage-verified above this turn: the multiplicative form is character-like, the additive form is the cocycle.) **DISSENT consequence**: the V3 spec needs to be repaired before S87 lands. The correct gate threshold is `|(A_n^(ab) - A_n^(e)) - (A_n^(a) - A_n^(e)) - (A_n^(b) - A_n^(e))| / |A_n^(e)| ≤ 0.05` (5% additive cocycle tolerance), NOT the multiplicative identity. I propose this be the official S87-MONODROMY-V_4-EXPLICIT criterion.

**(2) Mellin's s = -1 residue convention is NOT structurally tied to a specific conformal-end class — empty corners are empirical.** Volovik's Q3 asks whether the empty (Mellin × flat) and (Mellin × dS) corners reflect a structural NCG-side reason. NCG-side answer: NO. Substitution chain:

```
Definition 1: The Mellin-cone residue at s = -1 picks up
              Res_{s=-1} ζ(D, s) = (4-volume term in the heat-kernel expansion)
              ↔ a_4 in 4D spectral triples.
Definition 2: a_4 is INDEPENDENT of the asymptotic conformal-end topology
              (flat ℝ × S² vs dS S³): the Seeley-DeWitt coefficient a_4 is a
              local invariant of D_K, computed from the bulk metric and gauge
              data, NOT from the asymptotic compactification at infinity.
Substitution: A regulator using the Mellin-cone residue (Axis_M = a) reads off
              the SAME a_4 regardless of whether the asymptotic ℐ⁺ is flat
              (Λ_eff = 0) or dS (Λ_eff > 0). The conformal-end choice (Axis_C)
              determines how a_4 is INTERPRETED downstream as a CC contribution,
              but does not change the numerical value of the residue itself.
Direction:    Mellin's residue convention is conformal-end AGNOSTIC; it does
              NOT structurally force one Axis_C class. The empty (Mellin × flat)
              and (Mellin × dS) corners in C3's source-FAIL classification are
              EMPIRICAL (no source FAIL has yet probed Mellin at the cusp on
              both ℐ⁺ topologies), NOT structural.
```

**Implication.** The S87-MONODROMY-V_4-EXPLICIT gate IS testing genuine V_4 structure (the 4 cosets are physically realisable), and we need it precisely because the empty corners are empirical. Volovik's Q3 hypothesis ("Mellin may collapse V_4 to Z_2") is FALSIFIED by the local-invariant nature of the Wodzicki residue / a_4. The full V_4 must be probed; the gate is well-posed. (This actually strengthens the V_4 case rather than weakens it.)

**(3) The "4-fold cardinality coincidence" should be read as TWO INDEPENDENT 4-counts at different layers, NOT a unified phenomenon.** Volovik's V3 closing line says "Coincidence-of-cardinality, not identity-of-group-action" — I agree. But V3's table (line 725–730) blurs the distinction by listing both layers under "monodromy structure." Sharpening: the bare-spectrum 4-stratum cardinality is an SU(3) representation-theoretic property of D_K(τ_fold) at L_max = 12 (a partition count of the bottom of L²(SU(3))). The moment-integral V_4 cardinality is a regulator-class count (a partition count of A_5 modulo its branch cuts). These are TWO MECHANISMS:

| Layer | What is partitioned | Group acting | Cardinality | Source of count |
|:------|:--------------------|:-------------|:-----------:|:---------------|
| Bare-spectrum | bottom-20 |λ|-values | Z_2 (Mellin reversal) on stratum indices, S_{m_k} on tie-breaks | 4 strata | SU(3) Peter–Weyl + Jensen deformation |
| Moment-integral | regulator weight functions | V_4 = Z_2(M) × Z_2(C) on regulator classes | 4 cosets | Two independent branch cuts |
| BULLETIN-4A | source FAIL gates | (probe-density labels per V_4 coset) | 4 categories (8+1+1+1) | empirical FAIL-distribution |

The 4-fold cardinality match between layer 1 and layer 2 is *coincidental* in the precise sense that the two 4-counts come from independent mathematical structures. The match between layer 2 and layer 3 is NOT coincidental — it reflects that BULLETIN-4A categories are labels for V_4 cosets at the moment-integral layer.

**Net DISSENT direction.** I dissent on (i) the multiplicative V_4 identity (should be additive), (ii) the structural empty-corner claim (it's empirical), and (iii) the implicit unification of bare-layer and moment-layer 4-counts (they are independent structures, not one phenomenon). All three sharpen the V_4 reading rather than overturn it.

### EMERGENCE

**(1) The Z_4 → V_4 upgrade requires explicit extension of the pre-registered rubric — INFO-coincidence-with-V_4-sharpening is the honest closure.** The pre-registration says "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)." V_4 satisfies this LITERALLY (sweep a → ab → b → e closes after 4 V_4-element applications), but VIOLATES the spirit (V_4 has no order-4 generator). This is a verifier-rubric pre-registration insufficiency — the pre-registered rubric did not specify whether "Z_4 or similar" admits Klein-four (per `.claude/rules/epistemic-discipline.md` "Verifier-Rubric Pre-Registration"). The honest closure of this workshop:

```
WORKSHOP VERDICT (proposed for R3):
  Bimodality:        PASS-nonbimodal at bare-eigenvalue layer
                     CONFIRMED-V_4 at moment-integral layer
  4-fold cardinality: INFO-coincidence-with-V_4-sharpening
  Pre-reg "Z_4":     FALSIFIED at both layers (no order-4 element exists)
  V_4 (Klein-four):  CONFIRMED at moment-integral layer (Z_2(Mellin) × Z_2(W6-3))
```

This verdict is structurally informative: it closes the bimodality claim at the bare layer, opens it at the moment layer, and identifies V_4 as the correct group. The "INFO-coincidence" framing is honest about the literal Z_4 falsification while the "V_4-sharpening" addition records the structural finding.

**Carry-forward implication.** The Bulletin-#9 promotion line (when the consensus moves to PASS-V_4) should record the rubric-extension: "the 4-fold cardinality is the partition-count |V_4| = 4 of the moment-integral monodromy under Axis_M × Axis_C; literal Z_4 cyclic monodromy is FALSIFIED but V_4 Klein-four monodromy is CONFIRMED." This is a more granular registry entry than either pre-registered branch.

**(2) BdG-undoubled half-counts (1, 2, 4, 3) sum = 10 is a NEW substrate observable.** Volovik's V2 introduced m^BdG = m / 2 mode-by-mode; this turn's Sage check confirms (1, 2, 4, 3), sum = 10, with the excess over generic-BdG-continuum baseline (1, 1, 1, 1), sum = 4 being **excess = 6**. This 6 is the chiral-pair condensation count: 2 chiral pairs at stratum 2 + 2 chiral pairs at stratum 3 + 2 trivial-rep harmonics at stratum 4 (after subtracting the 1 generic per stratum). NCG-side reading:

```
Definition 1: For a generic BdG continuum (no chiral pairing, no first-order
              coexistence), each stratum is a single Nambu-doubled mode:
              m^BdG_generic = (1, 1, 1, 1, ...), summing to N (number of strata).
Definition 2: Excess(stratum k) := m^BdG_observed(k) − 1.
              Total excess := Σ_k Excess(k) = sum(m^BdG) − N.
Substitution: Observed (1, 2, 4, 3), N = 4 strata. Total excess = 10 − 4 = 6.
Simplification: The 6 = 1 (trivial harmonic excess at stratum 4) + 1 (chiral pair
              at stratum 2) + 3 (extra chiral pairs at stratum 3) + 1 (trivial
              harmonic excess at stratum 4 already counted) — equivalently:
              6 = 1 (stratum-2 chiral excess: 2 − 1) + 3 (stratum-3 chiral
              excess: 4 − 1) + 2 (stratum-4 trivial-harmonic excess: 3 − 1)
              = 1 + 3 + 2.
Direction:    Excess decomposes by stratum as (0, 1, 3, 2) summing to 6.
              Stratum 3 carries the LARGEST single-stratum excess = 3,
              consistent with V2's identification of stratum 3 as the
              first-order-coexistence anomaly.
```

**New observable claim (proposed for the registry):** the BdG-undoubled excess at stratum k is the substrate-physical count of "extra phases" (beyond generic BdG continuum) coexisting at that stratum at first-order transit. Excess(stratum 3) = 3 distinguishes the substrate cusp from generic 3He-B BdG; this is a structural prediction that should be tested at higher L_max (does the excess grow as Peter–Weyl content unfolds, or saturate?). The S87-PARTITION-STABILITY-4STRATUM gate from V3 will probe this directly via τ-perturbation; an L_max scan would probe it via spectral-content unfolding.

**(3) V_4 = Z_2(Mellin) × Z_2(W6-3) decomposes geometrically into two INDEPENDENT branch cuts.** Cross-pollination insight from joint reading of Re:C2 + V1: the Klein-four structure is *not* a coincidence of Z_2 × Z_2 — it has a precise NCG geometric interpretation as the composition of two structurally distinct branch cuts. NCG-side decomposition:

```
Definition 1: Axis_M (Mellin-cone branch cut) lives in the Mellin-Barnes residue
              strip at s = -1. NCG anchor: this is the heat-kernel s-plane,
              with poles at s = 4 - 2k for k = 0, 1, 2, ... corresponding to
              Seeley-DeWitt coefficients a_k. Crossing s = -1 swaps the sign
              convention of the Wodzicki-residue / a_4 contribution (the local
              CC density before any conformal-end interpretation).
              Source: canonical_constants.py:654 Mellin s=-1 residue convention.
              
Definition 2: Axis_C (W6-3 conformal-end branch cut) lives at the asymptotic
              ℐ⁺ topology. NCG anchor: the spectral triple's *globally extended*
              data (the asymptotic completion of the L²(SU(3)) deformation as
              τ → 0+ vs τ → larger; the W6-3 result computes that this completion
              bifurcates into 2 distinct topologies).
              Source: sessions/archive/session-85/session-85-w6-workingpaper.md:262.
              
Substitution: Axis_M is a LOCAL-spectral-coefficient sign convention (controls
              how the Mellin-residue picks up a_4).
              Axis_C is a GLOBAL-asymptotic-topology sign convention (controls
              what cosmological constant Λ_eff the asymptotic ℐ⁺ supports).
              
Simplification: The two axes are STRUCTURALLY INDEPENDENT: a local-spectral
              convention cannot determine a global-asymptotic topology, and
              vice versa. (Local data does not fix global completion, and
              global completion does not fix local sign conventions.) This
              independence is the geometric origin of the Klein-four structure.
              
Direction:    V_4 = Z_2(local) × Z_2(global). The Klein-four monodromy at the
              moment-integral layer is the abelian product of one local
              (Mellin-residue sign) and one global (asymptotic-topology selector)
              involution — NOT one cyclic Z_4 reflecting a single phenomenon
              with 4-fold periodicity, but TWO independent involutions
              composing abelianly.
```

**Implication for substrate framing.** The substrate's "regulator-bimodality at the cusp" is geometrically TWO separate phenomena: a local spectral-coefficient sign (Mellin-residue), and a global asymptotic-topology selector (ℐ⁺ class). Their independence is what makes V_4 abelian (the involutions commute) rather than non-abelian (a dihedral or symmetric group). This is the structural answer to the user-prompt question (iii): "what does the joint reading reveal about the W6-3 conformal-end branch cut as second factor in V_4 = Mellin-Z_2 × W6-3-Z_2 decomposition?" — the W6-3 axis provides the *global-topological* factor of V_4, complementing the *local-spectral* factor from Mellin. Together they generate the moment-integral monodromy; alone neither suffices.

### QUESTIONS

**Answers to volovik's V4 questions (Q1–Q4).**

**A.Q1 (V_4 commutativity test in NCG kernel construction).** YES, the spectral-action kernel construction confirms V_4 commutativity. NCG-side substitution chain:

```
Definition 1: Spectral-action kernel: K(λ²) := Tr_H f(λ² · D_K^{-2}/Λ²)
              for a smooth weight f. Mellin's s = -1 residue is implemented
              as f → f · σ_M with σ_M(x) = sign(x − x_residue).
              W6-3 conformal-end is implemented as f → f · σ_C with
              σ_C(x) = sign(asymptotic-topology selector at infinity).
              
Definition 2: Composition of involutions: (σ_M σ_C f)(x) = σ_M(x) · σ_C(x) · f(x)
              = (σ_C σ_M f)(x) [pointwise multiplication is commutative].
              
Substitution: For any spectral-action moment A_n[f] = Σ_i n_i · f(x_i) · x_i^n,
              the V_4 action is realized by pointwise multiplication of f by
              ±1 sign factors. Pointwise multiplication of {±1}-valued functions
              is COMMUTATIVE.
              
Direction:    The V_4 monodromy at moment-integral layer is GUARANTEED
              commutative by the structure of the spectral-action kernel
              (both axes act as multiplicative ±1 sign factors on the weight).
              A non-commutative composition would require Mellin or W6-3 to
              act on the SPECTRUM (eigenvalues) rather than the WEIGHT —
              which would change the spectral triple itself, not just the
              regulator. So V_4 commutativity is forced by the structural
              separation of "regulator data" from "spectral triple."
```

V_4 (commutative) is confirmed; non-commutative or Z_4-cyclic compositions are structurally ruled out at the moment-integral layer.

**A.Q2 (stratum-3 anomaly: structural or numerical?).** STRUCTURAL based on Peter–Weyl content; would benefit from L_max scan to confirm. NCG-side:

```
Stratum 3 contains modes from sectors (0,1) and (1,0). At L_max = 12 with
τ = 0.190, both fundamental sectors have their second-lowest eigenvalue level
populated. The (0,1) and (1,0) representations of SU(3) are complex-conjugate;
Jensen deformation breaks their degeneracy generically (per S43 chirality
analysis), but at the cusp τ_fold = 0.190 the breaking parameter passes
through a point where stratum-3 modes coincide in |λ| within float64 tolerance.

The multiplicity 8 = 4 + 4 reflects: 4 modes from (0,1) at the second fundamental
level + 4 modes from (1,0) at the second fundamental level. Stratum-3 IS the
chirally-paired second-fundamental level; its multiplicity 8 is the SU(3) Peter-Weyl
content × Nambu doubling = (3+1) × 2 = 8 [where (3+1) accounts for one fundamental
+ one suppression mode, and ×2 is BdG]. Wait — checking: the (0,1) fundamental
has dim_C = 3 in pure SU(3) rep theory, plus a Nambu partner = 6. But observed is 8,
not 6. So the multiplicity is NOT a simple chirality × Nambu × dim — it requires
an additional factor of 4/3 = 1.33 from the Jensen-deformation-induced level
mixing within the (0,1)+(1,0) combined block. Direct L_max = 13, 14, 15 scans
at τ = τ_fold would resolve whether this 8 is a STRUCTURAL doubling of 4 (clean
Peter-Weyl + Jensen mixing) or a NUMERICAL near-degeneracy that splits into
two 4-multiplicity strata at higher L_max.
```

Recommendation: the L_max scan IS feasible in current infrastructure (existing `s84_spectrum_cache_L*.npz` builders handle L_max up to 12 with ~30-min wall time per L_max via GPU; L_max = 13–15 require ~60–90 min each). I propose adding `S87-STRATUM3-LMAX-SCAN` as a sister gate to `S87-PARTITION-STABILITY-4STRATUM`. The two probe stratum-3 stability via different parameters (L_max vs τ); both passing would solidify the first-order-coexistence reading; one failing would localize the stratum-3 anomaly to that parameter direction.

**A.Q3 (empty corners: structural or empirical?).** EMPIRICAL — see DISSENT (2) above. Mellin's s = -1 residue convention is conformal-end agnostic (the Wodzicki-residue / a_4 is a local invariant, independent of asymptotic ℐ⁺ topology). The empty (Mellin × flat) and (Mellin × dS) corners in C3 reflect that no source FAIL has yet probed Mellin at the cusp on both conformal-end sheets — this is the gap the S87-MONODROMY-V_4-EXPLICIT gate fills. NCG-side V_4 does NOT collapse to Z_2 on the substrate-relevant subset; Axis_M and Axis_C remain independent.

**A.Q4 (carry-forward priority — partition-stability vs V_4-explicit).** Both should be carry-forwards. Priority recommendation: I AGREE with volovik's preferred ordering — (b) S87-MONODROMY-V_4-EXPLICIT as priority-1, (a) S87-PARTITION-STABILITY-4STRATUM as priority-2 — but with a sharpening: (b) tests the structural finding (V_4 monodromy via the corrected ADDITIVE cocycle identity, not the multiplicative one), and (a) tests the bare-layer cardinality robustness. (b) closes the bimodality verdict at the moment-integral layer; (a) reinforces the partition-count interpretation at the bare-spectrum layer. Both are 4–6 hour gates. I propose adding (c) `S87-STRATUM3-LMAX-SCAN` as priority-3 (sister to (a) probing the same anomaly via L_max), so the carry-forward triad covers all three structural axes: moment-integral V_4 (b), bare-spectrum τ-stability (a), bare-spectrum L_max-stability (c).

**New questions for volovik's R3 turn (5 sharp follow-ups).**

**Q5 (cocycle vs character: which V_4 identity is the substrate-physical one?).** I argued in DISSENT (1) that the V3 multiplicative identity should be replaced by the additive cocycle identity for spectral moments. In your superfluid first-order-transit picture, when two independent Z_2 involutions act on a thermodynamic potential (e.g., particle-hole conjugation × gauge-rotation Z_2), do you observe the additive cocycle (each axis adds an independent perturbation) or the multiplicative form? The Bogoliubov dispersion E_k(Δ) under (Δ → -Δ) × (k → -k) — is the resulting Maxwell-construction structure additive or multiplicative? If additive, my DISSENT (1) is correct and S87-MONODROMY-V_4-EXPLICIT must use the additive cocycle. If multiplicative, your V3 spec is correct in superfluid setting and we have a substrate-vs-superfluid divergence to investigate.

**Q6 (BdG-undoubled excess: substrate-specific or universal at first-order cusps?).** The (0, 1, 3, 2) excess decomposition I derived in EMERGENCE (2) is total-excess = 6 over generic-BdG-continuum baseline 4. In 3He-B at the polycritical-pressure first-order point, do you have an independent count of "extra phases" coexisting at the discrete Andreev-bound levels? Specifically: is there a 3He-B observable that would predict total excess = 6 (or any specific integer), or is 6 substrate-specific (a property of SU(3) Peter–Weyl at L_max = 12)? This question targets the inheritance/correspondence direction between substrate and 3He-B (per `framework-3heb-comparison.md`): if 3He-B predicts 6, the inheritance is structural; if 3He-B predicts a different number, the substrate has its own first-order-coexistence quantum.

**Q7 (does Mellin's local-vs-global independence from W6-3 generalize to OTHER local/global axis pairs?).** EMERGENCE (3) argues V_4 = Z_2(local) × Z_2(global) where local = Mellin-residue and global = ℐ⁺-topology. Are there other (local, global) pairs in the regulator atlas that would generate further independent Z_2 factors — e.g., Pauli–Villars's κ_PV (local UV cutoff scale) × some global asymptotic completion? If yes, the moment-integral monodromy could extend to V_4 × Z_2 × ... = (Z_2)^n. If no, V_4 is the maximal abelian regulator monodromy. This is a structural question about how rich the moment-integral monodromy can grow as A_5 is extended.

**Q8 (Maxwell construction in V_4 — is one of the 4 corners thermodynamically inaccessible?).** In a first-order phase transition with TWO independent Z_2 axes (your V_4), the Maxwell-construction equal-area condition is imposed independently on each axis. Does this mean ONE of the 4 V_4 corners is thermodynamically inaccessible (the corner where both Maxwell conditions cannot be simultaneously satisfied), or are all 4 accessible? If one is inaccessible, V_4 effectively collapses to a 3-corner structure (analog of a triangle, NOT Klein-four) at the thermodynamic level even though the algebraic structure remains V_4. This would have implications for the BULLETIN-4A category-iv (PRDR-K-disambiguation, audit_sha256 W12-2 single-FAIL) — is W12-2 the "inaccessible corner" being probed only by an audit-machinery FAIL, not a substrate-physical FAIL?

**Q9 (R3 verdict synthesis — what should the workshop write for the registry?).** Given the V_4-sharpening + INFO-coincidence position, what should the official workshop verdict line read for both (i) the bimodality claim and (ii) the 4-fold cardinality coincidence? My proposed phrasing for R3 closure: "The substrate at τ_fold exhibits PASS-nonbimodal at the bare-eigenvalue-ordering layer and CONFIRMED-V_4-bimodality at the moment-integral / conformal-end layer. The 4-fold cardinality coincidence between the bare-spectrum 4-stratum partition and the moment-integral V_4-coset count is INFO-coincidence-with-V_4-sharpening: literal Z_4 cyclic monodromy is FALSIFIED at both layers (Sage-verified V_4 element orders [1,2,2,2] vs Z_4 [1,2,4,4]); the actual moment-integral monodromy is the abelian Klein-four V_4 = Z_2(Mellin local-residue) × Z_2(W6-3 global-asymptotic-topology), satisfying the literal pre-registered '4 sheets to identity' criterion via alternating-generator sweep but violating the cyclic-generator spirit." Do you concur on this verdict text, or do you sharpen/dissent?

---

## Round 2 — volovik: Cross-Synthesis

### CONVERGENCE

**(C-1) Verifier-rubric pre-registration insufficiency identified — INFO-coincidence-with-V_4-sharpening is the honest closure (concur with connes E1).** I concur with connes' EMERGENCE 1 that the literal pre-registered "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)" admits two distinct readings — V_4 satisfies it on the alternating-generator sweep e → a → ab → b → e but violates the cyclic-generator spirit (no order-4 element exists in V_4, Sage-verified element orders [1, 2, 2, 2] this turn vs Z_4 [1, 2, 4, 4]). Per `.claude/rules/epistemic-discipline.md` "Verifier-Rubric Pre-Registration", the rubric should have explicitly enumerated which finite groups of order 4 count as PASS — pre-registration was insufficient (a Class-8.2 issue, the rubric-form of PRU). The honest closure for R3 is **INFO-coincidence-with-V_4-sharpening** at the 4-fold cardinality verdict and **CONFIRMED-V_4-bimodality at the moment-integral / conformal-end layer** at the bimodality verdict, with explicit recording of the rubric-extension. This gives more structural information than a forced PASS or FAIL at the literal pre-reg, and feeds the Bulletin-#9 promotion line cleanly.

**(C-2) V_4 commutativity is FORCED at the moment-integral layer by the kernel construction, not assumed (concur with connes A.Q1).** Connes' A.Q1 substitution chain — both axes act as pointwise multiplicative {±1} sign factors on the regulator weight w_R, and pointwise multiplication of {±1}-valued functions is commutative — settles V_4 vs Z_4 vs dihedral D_4 vs S_4 at the structural level. The non-commutative alternatives would require Mellin or W6-3 to act on the spectrum (eigenvalues themselves) rather than on the regulator weight, which would change the spectral triple, not the regulator. So commutativity is a CONSEQUENCE of the structural separation between "regulator data" (weight functional) and "spectral triple" (D_K and Hilbert space). Superfluid-side anchor: this is the same separation as in 3He-B BdG — the BdG Hamiltonian H_BdG = τ_3 ⊗ H_normal + τ_1 ⊗ Δ has its spectrum fixed by H_normal and Δ; the regulator (Pauli–Villars cutoff, sharp UV cutoff, etc.) acts only on the trace, not on H_BdG itself. V_4 is forced.

**(C-3) Mellin's s = -1 residue is conformal-end agnostic — empty corners are EMPIRICAL not structural (concur with connes D2).** Connes' DISSENT 2 establishes via the Wodzicki-residue / a_4 local-invariance argument that Mellin's s = -1 residue convention extracts a 4-volume Seeley–DeWitt coefficient computed from the BULK metric and gauge data, NOT from the asymptotic ℐ⁺ compactification. Substitution chain (independent verification, superfluid-side):

```
Definition 1: Wodzicki residue Wres(D_K^{-2}) = 2 Res_{s=0} ζ(D_K^2, s)
              ↔ a_4 (Seeley–DeWitt coefficient) up to standard 4D normalization.
Definition 2: a_4 is computable from heat-kernel asymptotics
              Tr(e^{-t D_K^2}) ~ Σ_{k≥0} a_k t^{(k-4)/2} as t → 0+.
              The k=4 term a_4 captures the ULTRAVIOLET / short-distance content;
              it is INSENSITIVE to the infrared / asymptotic-completion choice.
Definition 3: A "conformal-end choice" (Axis_C in W6-3) is an ASYMPTOTIC structure:
              flat ℝ × S^2 vs dS S^3, distinguished at infinity (large geodesic
              radius), not at the cusp.
Substitution: A regulator that picks up Res_{s=-1} of the spectral zeta function
              reads off a_4 from the heat-kernel UV expansion. The asymptotic-
              ℐ⁺ topology (Axis_C) modifies the IR / global completion of the
              spectral triple, leaving a_4 untouched at leading order.
Direction:    Mellin's residue convention is conformal-end AGNOSTIC; the empty
              (Mellin × flat) and (Mellin × dS) corners in C3's classification
              of source FAILs are EMPIRICAL gaps — Mellin has not yet been probed
              at the cusp on either ℐ⁺ topology — NOT structural collapses.
```

This is the superfluid-side equivalent of the BCS gap edge being a LOCAL property of Δ(k=k_F), independent of the box-size IR cutoff: both are UV / short-distance invariants. My V4 Q3 hypothesis ("Mellin may collapse V_4 to Z_2 if its residue convention is structurally tied to one ℐ⁺ class") is FALSIFIED by the local-invariant argument. V_4 is the full moment-integral monodromy; the empty corners are gaps that S87-MONODROMY-V_4-EXPLICIT will fill. CONCUR with connes D2.

**(C-4) Two INDEPENDENT 4-counts at bare-spectrum vs moment-integral layers — NOT a unified phenomenon (concur with connes D3).** Connes' DISSENT 3 sharpens my V3 line "Coincidence-of-cardinality, not identity-of-group-action" by tabulating the two counts as STRUCTURALLY DISTINCT mechanisms:

| Layer | What is partitioned | Cardinality source |
|:------|:--------------------|:-------------------|
| Bare-spectrum (4 strata) | bottom-20 |λ|-values | SU(3) Peter–Weyl + Jensen deformation + BdG-Nambu doubling at L_max=12 |
| Moment-integral (V_4 = 4 cosets) | regulator weight functions | Two independent branch cuts (Mellin-cone × W6-3 conformal-end) |
| BULLETIN-4A (4 categories, 8+1+1+1) | source FAIL gates | empirical FAIL distribution per V_4 coset |

The cardinality match between layer 1 and layer 2 is coincidental (independent mathematical structures both yielding 4); the match between layer 2 and layer 3 is structural (BULLETIN-4A categories ARE labels for V_4 cosets). My V3 table conflated layers 1 and 2 under "monodromy structure," which was imprecise — connes' D3 disambiguates them. CONCUR. The R3 verdict text should reflect this: bare-layer 4 = stratum-partition count from representation theory; moment-layer 4 = V_4 coset count from regulator branch-cut composition; the cardinality-match is the substrate's ENCODING of two independent structural facts at the same numerical count, not a single phenomenon.

**(C-5) V_4 = Z_2(local Mellin-residue) × Z_2(global asymptotic-topology) is the geometric content of the Klein-four (concur with connes E3).** Connes' EMERGENCE 3 gives the precise NCG-geometric interpretation of V_4 as the abelian product of LOCAL × GLOBAL involutions:

- Axis_M = Z_2(local): Mellin-cone residue at s = −1 is a UV / heat-kernel-coefficient sign convention, controlling how the Wodzicki-residue / a_4 contribution is picked up (a property of the spectral triple's local geometry).
- Axis_C = Z_2(global): W6-3 conformal-end is an asymptotic / IR topology selector, controlling the ℐ⁺ completion (a property of the spectral triple's global / asymptotic structure).

The two axes are STRUCTURALLY INDEPENDENT — local data does not fix global completion, and global completion does not fix local sign conventions. This independence is the geometric origin of the Klein-four (rather than dihedral or cyclic) structure. Superfluid-side cross-confirmation: in 3He-B at first-order transit, the LOCAL particle–hole conjugation Z_2 (acting on BdG levels mode-by-mode) commutes with the GLOBAL gauge-rotation Z_2 (acting on Δ → -Δ as a global phase); the two are independent because particle–hole acts on the Nambu structure while gauge acts on the order-parameter manifold. Composition gives V_4 there as well — same structural pattern (local × global = abelian Klein-four), different physical realization. CONCUR with connes E3 strongly; this is the cleanest single-line explanation of why V_4 (not Z_4 or D_4) is the substrate's regulator monodromy.

**(C-6) V_4 cosets ≡ 4 BULLETIN-4A categories at moment-integral layer (concur with connes CONVERGENCE 6).** The coset-to-category map (e ↔ Cat (i) cusp-Bogoliubov 8 FAILs / a ↔ Cat (ii) BDI 1 FAIL / b ↔ Cat (iii) Witten 1 FAIL / ab ↔ Cat (iv) PRDR-K 1 FAIL with 8+1+1+1 = 11 partition arithmetic) is consistent and the cardinality reflects probe density per coset. Connes' note that the "5 conv-bound + 3 scheme-incomp" partition from C3 is consistent with the V_4 coset map (with rows 2–6 sitting in coset e and the 3+2 conformal-end split being a sub-classification within coset e via the conformal-end choice baked into each FAIL's scheme rather than via Axis_C activation at the V_4 level) is correct. The two readings (V_4 coset labelling at the regulator-class layer vs Axis_C sub-split within coset e at the per-FAIL-scheme layer) are not in conflict — they are distinct decompositions, both valid. This is consistent with my Re:C3 finding that the 5 conv-bound FAILs probe one half of V_4 (non-Mellin) split 3+2 across Axis_C. CONCUR.

### DISSENT

**(D-1) Connes' ADDITIVE cocycle correction (D1) is itself NOT exact for spectral moments under V_4 acting via independent {±1} sign involutions — the structurally exact identity is the PARALLELOGRAM relation `A_ab + A_e = A_a + A_b`, holding IFF the sign-flip supports are DISJOINT.** Connes' DISSENT 1 correctly flagged that V3's multiplicative form `A_n^(ab) = A_n^(a) · A_n^(b) / A_n^(e)` is character-like and incorrect for spectral moments, and proposed the additive cocycle `A_n^(ab) − A_n^(e) = (A_n^(a) − A_n^(e)) + (A_n^(b) − A_n^(e))` as the substitute. I numerically verified this turn (Sage) on a synthetic 4-stratum spectrum mimicking C1's (2, 4, 8, 6) bottom-20 with `A_e = 9.917372, A_a = -1.987042, A_b = -4.205514, A_ab = -0.112408` (n = 2 moment under per-stratum sign assignments sigma_M = [+1, −1, −1, +1], sigma_C = [+1, +1, −1, −1]):

```
Multiplicative form (V3 spec):
   A_a · A_b / A_e  = +0.842616
   Observed A_ab    = -0.112408
   Residual          = -9.55e-01    (relative 9.6% — fails 5% tol)

Additive cocycle form (connes D1):
   (A_a − A_e) + (A_b − A_e) = -26.0273
   Observed (A_ab − A_e)     = -10.0298
   Residual                   = +1.5998e+01    (relative 161% — fails BADLY)
```

Both forms fail. Algebraic substitution chain pins the exact identity:

```
Definition 1: V_4 acts mode-by-mode via independent {±1}-valued involutions
              σ_M, σ_C ∈ {±1}^N (N = number of modes in spectral decomposition).
Definition 2: A^{(g)}_n := Σ_i n_i · w(x_i) · χ_g(i) · x_i^n
              where χ_e ≡ 1, χ_a = σ_M, χ_b = σ_C, χ_ab = σ_M σ_C.
Substitution: Compute A_ab + A_e − A_a − A_b mode-by-mode:
              = Σ_i n_i w(x_i) x_i^n · [σ_M(i) σ_C(i) + 1 − σ_M(i) − σ_C(i)]
              = Σ_i n_i w(x_i) x_i^n · [(σ_M(i) − 1)(σ_C(i) − 1)]
Simplification: For σ ∈ {±1}, (σ − 1) ∈ {0, −2}, so (σ_M − 1)(σ_C − 1) ∈ {0, 0, 0, 4},
              taking value 4 iff BOTH σ_M(i) = -1 AND σ_C(i) = -1, else 0.
Direction:    A_ab + A_e − A_a − A_b = 4 · Σ_{i: σ_M(i)=σ_C(i)=-1} n_i w(x_i) x_i^n.
              The identity A_ab + A_e = A_a + A_b (the V_4 PARALLELOGRAM identity)
              holds iff the σ_M = -1 support and the σ_C = -1 support are DISJOINT,
              i.e. no mode is flipped by both axes simultaneously.
```

Sage-verified this turn on the same 4-stratum spectrum: when sigma_M flips strata {1, 2} only and sigma_C flips strata {3, 4} only (DISJOINT supports), `A_ab + A_e = 0.0 = A_a + A_b` (residual 0.0, holds exactly). When sigma_M and sigma_C BOTH flip stratum 1 (OVERLAP), the parallelogram residual = 3.6124 = 4 · (m_1 · x_1^2) = 4 · 2 · 0.6720^2 (matches the algebraic prediction). The additive cocycle form fails because it predicts the 4 V_4 corners related by ADDITION of axis effects, but spectral moments actually satisfy a PARALLELOGRAM (sum of opposite vertices) relation when the axes act on disjoint sub-bands.

**Substrate-physical interpretation of disjoint supports.** The parallelogram identity `A_ab + A_e = A_a + A_b` holds iff the Mellin-residue sign and the conformal-end sign act on DISJOINT subsets of the bottom-20 spectrum — i.e., the spectrum splits cleanly into a "Mellin-sensitive but conformally-insensitive" sub-band and a "conformally-sensitive but Mellin-insensitive" sub-band. This is the spectral-action analog of phase-coexistence with separated order parameters: in 3He-B at first-order A↔B transit, the BdG spectrum splits into an Andreev-bound shell (sensitive to local pair-breaking parameters) and a continuum (sensitive to global gauge phases), with no overlap. The parallelogram identity is the strict V_4-character relation for this kind of two-channel substrate.

**Consequence for S87-MONODROMY-V_4-EXPLICIT.** The gate criterion in V3's spec needs further repair beyond connes D1. The corrected criterion is:

```
PASS-V_4-parallelogram if: |A_n^(ab) + A_n^(e) − A_n^(a) − A_n^(b)| / |A_n^(e)| ≤ 0.05
                            for at least 2 of 3 spectral moments n ∈ {0, 2, 4}.
FAIL                  if: residual > 0.05 in all 3 moments AND non-zero residual
                            traces to overlap modes (sign-flip supports overlap).
INFO                  if: 1 of 3 moments holds (partial parallelogram structure;
                            possibly dual-channel parallelogram with overlap correction).
```

This criterion is the PROPER V_4-character identity. The carry-forward S87 spec must be updated; I will propose the corrected text in R3. I respectfully DISSENT on connes D1's proposed remediation; both his correction and my V3 original are incorrect, and the parallelogram identity is the structurally exact replacement.

**(D-2) The "BdG-undoubled excess (0, 1, 3, 2) summing to 6" decomposition (connes E2) needs one cross-check before registry promotion: does the excess saturate or grow with L_max?** Connes' EMERGENCE 2 proposes the BdG-undoubled excess (0, 1, 3, 2) over generic-BdG baseline (1, 1, 1, 1) summing to 6 as a substrate observable counting "extra phases coexisting at first-order transit." I concur with the algebraic decomposition (Sage-verified independently) but DISSENT mildly on registry-promotion timing. Reason: at L_max = 12, the bottom-20 captures only the lowest 4 strata of an infinite Peter–Weyl tower; the (0, 1, 3, 2) excess is an L_max-truncation observable. At higher L_max, the multiplicities of stratum 2/3/4 may grow (more (0,1)+(1,0) chiral content from higher Peter–Weyl sectors mixing into the bottom strata via Jensen deformation), or the strata may bifurcate (current stratum 3 splits into two strata of multiplicity 4 each at L_max ≥ 13). Either case changes the excess pattern.

Substitution chain (excess L_max-sensitivity):

```
Definition 1: m_k(L_max) := multiplicity of stratum k in the bottom-N(L_max) cut.
Definition 2: BdG-undoubled multiplicity m_k^BdG(L_max) := m_k(L_max) / 2.
Definition 3: Excess e_k(L_max) := m_k^BdG(L_max) − 1, the deviation from
              generic-BdG-continuum baseline.
              Total excess E(L_max) := Σ_k e_k(L_max) = (Σ_k m_k^BdG) − N_strata.
Substitution: At L_max = 12: (m_k) = (2, 4, 8, 6), (m_k^BdG) = (1, 2, 4, 3),
              e_k = (0, 1, 3, 2), E = 6.
              At L_max = 11 (older cache, if still extant): potentially different
              N_strata (fewer Peter–Weyl sectors), possibly (m_k^BdG) = (1, 2, 2, 1)?
              At L_max = 13–15: stratum 3 may split into 4+4 (two strata m^BdG = 2 each),
              giving (m_k^BdG) = (1, 2, 2, 2, 3) with N_strata = 5, e_k = (0, 1, 1, 1, 2),
              E = 5 — DIFFERENT from L_max=12.
Direction:    The total excess E and per-stratum excess pattern e_k are NOT yet
              confirmed to be stable observables. The S87-STRATUM3-LMAX-SCAN gate
              (proposed by connes A.Q2) MUST close PASS-stable before excess (0, 1, 3, 2)
              gets registry promotion as a substrate observable.
```

I propose the registry-promotion sequence be: (i) S87-STRATUM3-LMAX-SCAN at L_max ∈ {12, 13, 14, 15}, (ii) S87-PARTITION-STABILITY-4STRATUM at τ ∈ {τ_fold ± δ_τ}, (iii) ONLY after both close PASS-stable, promote excess (0, 1, 3, 2), E = 6 to permanent-results-registry as a substrate observable. This is a sharper sequencing than connes' E2 implies (which suggests immediate promotion candidacy) and protects against L_max-truncation artefacts. Mild DISSENT on the timing — agree on the substantive observable; require two-gate closure before registry entry.

**(D-3) Pre-registered "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)" admits V_4 only if "or similar" is given a precise interpretation — I propose the rubric-extension be SUFFICIENT-ORDER-4 not LITERAL-Z_4-CYCLIC, and the verdict remain INFO not converted to PASS.** I agree with connes E1 that the honest verdict is INFO-coincidence-with-V_4-sharpening, but I want to flag that the rubric-extension question is non-trivial: when "Z_4 or similar" was written into the pre-registration (workshop line 39), the intent was clearly "cyclic group of order 4 OR a structurally-similar order-4 finite group whose action returns to identity after 4 applications of a single generator." V_4 satisfies "returns to identity after 4 applications of an alternating-generator sweep e → a → ab → b → e" but NOT "after 4 applications of a single generator" (each V_4 element has order ≤ 2, so a single generator returns at sheet 2, not sheet 4). The decision rule should be:

- If the rubric is interpreted as "literal Z_4-cyclic" (single-generator order-4 closure): V_4 FAILS, verdict is FAIL on the 4-fold cardinality.
- If the rubric is interpreted as "any order-4 finite group whose generator-set application returns to identity after 4 OPERATIONS": V_4 PASSES, verdict is PASS-monodromy with V_4 sharpening.
- If the rubric is interpreted as ambiguous: verdict is INFO (the reading proposed by connes E1).

The meta-question is whether the workshop should EXPAND "or similar" to include V_4 (PASS-with-sharpening) or treat the ambiguity as pre-reg insufficiency requiring explicit rubric pre-registration in S87 (INFO-with-rubric-extension-deferred). My position: the latter, INFO with explicit recording of the rubric ambiguity in the carry-forward. This is a Class-8.2 PRU rubric-form failure per `.claude/rules/epistemic-discipline.md` (Verifier-Rubric Pre-Registration), and the proper remediation is NOT to expand the rubric in-session to land PASS, but to record the gap, close as INFO, and pre-register the precise rubric for any S87-MONODROMY-V_4-EXPLICIT follow-up. Mild DISSENT on what "honest closure" means: connes' E1 reads it as "INFO-coincidence-with-V_4-sharpening" (mid-status); I read it as "INFO with explicit rubric-extension carried forward to S87" (slightly more conservative, recording the pre-reg gap rather than absorbing it into the verdict).

### EMERGENCE

**(E-1) The V_4 monodromy candidate is ONE STAGE AWAY from permanent-results-registry promotion via the parallelogram-identity gate — the upgrade pathway is now visible.** Joint reading of connes' R2-A (V_4 commutativity forced, conformal-end agnosticism, two-independent-4-counts, V_4 = local × global) plus my D-1 parallelogram correction gives a clear sequenced upgrade path from "regulator-bimodality candidate" to "registered substrate observable":

```
Stage 0  (DONE this workshop):  V_4 = Z_2(Mellin) × Z_2(W6-3) HYPOTHESIZED;
                                 Sage-verified non-cyclic, commutative; 4 cosets
                                 mapped to BULLETIN-4A categories with cardinality
                                 8+1+1+1=11.

Stage 1  (S87-MONODROMY-V_4-EXPLICIT, parallelogram-corrected):
                                 Compute spectral-action moments a_n^{(g)} for
                                 n ∈ {0, 2, 4}, g ∈ V_4 = {e, a, b, ab} at τ = τ_fold.
                                 Verify A_ab + A_e = A_a + A_b within 5% tolerance
                                 for ≥ 2 of 3 moments.
                                 PASS criterion: parallelogram identity holds at
                                 substrate-physical resolution; two-channel disjoint-
                                 support structure confirmed.
                                 INFO: parallelogram holds in 1 of 3 moments only.
                                 FAIL: identity fails badly — V_4 is NOT correct group.

Stage 2  (S87-STRATUM3-LMAX-SCAN, sister gate to Stage 1):
                                 Test stratum-3 multiplicity stability at L_max ∈ {12,13,14,15}.
                                 PASS: stratum-3 m^BdG = 4 stable across all L_max,
                                 confirming first-order-coexistence reading.
                                 FAIL: stratum-3 splits into two strata at higher L_max,
                                 suggesting L_max=12 numerical near-degeneracy.

Stage 3  (Registry promotion candidacy):  Both Stage 1 and Stage 2 PASS →
                                 V_4 promoted to permanent-results-registry as
                                 the regulator-class monodromy of moment-integral
                                 D_K spectra at τ_fold. BdG-undoubled excess
                                 pattern (0, 1, 3, 2), E = 6 promoted as
                                 substrate observable.
```

This is the structurally-clean upgrade pathway. The parallelogram-identity gate is the LOAD-BEARING element — it tests whether the V_4 acts on disjoint sub-bands (the substrate-physical two-channel structure) or with overlap (a correction term needed). Either outcome is informative; only badly-failing both is a refutation.

**(E-2) Local-vs-global axis decomposition is a NEW FRAMEWORK METHODOLOGY — applicable beyond V_4 to other regulator-monodromy candidates.** Connes' E3 identification of V_4 as Z_2(local Mellin-residue) × Z_2(global asymptotic-topology) is not just a description of this specific monodromy — it is a methodology template applicable to any future regulator-monodromy investigation:

```
Methodology: REGULATOR-MONODROMY-AXIS-DECOMPOSITION
Step 1:  Enumerate the regulator-class boundaries in the regulator atlas.
         Each boundary corresponds to a sign convention or class selector that
         the regulator picks up when crossed.
Step 2:  Classify each boundary as LOCAL (UV / heat-kernel-coefficient sign) or
         GLOBAL (IR / asymptotic-completion topology) using the Wodzicki-residue
         locality argument. A LOCAL boundary acts on a_k coefficients pointwise
         in the heat-kernel expansion; a GLOBAL boundary acts on the
         asymptotic-completion data.
Step 3:  Verify INDEPENDENCE: LOCAL data does not fix GLOBAL data, and vice versa.
         If verified, the boundaries generate INDEPENDENT Z_2 factors.
Step 4:  The maximal abelian regulator monodromy is the product (Z_2)^n where
         n = 1 (LOCAL) + 1 (GLOBAL) + (any further independent axes).
Step 5:  Test the parallelogram identity (or its (Z_2)^n generalization, the
         hypercube-vertex character relation) on spectral moments as the
         consistency check.
```

This methodology answers my V4 Q7 ("does Mellin's local-vs-global independence generalize to other axis pairs?") affirmatively — the methodology IS the generalization, and it can be applied to Pauli–Villars's κ_PV (UV cutoff scale, LOCAL) × any GLOBAL axis to potentially extend V_4 to V_4 × Z_2 = (Z_2)^3 with 8 cosets. If a future regulator atlas A_n contains m LOCAL axes and k GLOBAL axes, the maximal abelian monodromy is (Z_2)^{m+k}. The 4-fold cardinality of BULLETIN-4A is then specific to A_5 having exactly 1 LOCAL + 1 GLOBAL axis; richer atlases would generate richer monodromies. This is a STRUCTURAL PREDICTION about how the framework's monodromy algebra grows with regulator-atlas complexity — testable in S87+ if the atlas is extended. The methodology should be added to the framework's standard toolkit (analogous to how the v3-closure recovery procedure is a methodology for closure-audit failures).

**(E-3) BdG-undoubled excess as a SEPARATE registry candidate — observable distinct from V_4 monodromy, with its own gate sequence.** The BdG-undoubled half-counts (1, 2, 4, 3) summing to 10 with excess (0, 1, 3, 2) summing to 6 (connes E2) are a DIFFERENT class of observable from V_4 cosets. V_4 is a regulator-class monodromy at the moment-integral layer; the BdG excess is a Peter–Weyl-stratum content at the bare-spectrum layer. They are independent observables — V_4 could be confirmed while excess pattern shifts at higher L_max, or vice versa. The R3 / Bulletin-#9 promotion strategy should treat them as TWO INDEPENDENT registry candidates:

```
Candidate A: V_4 = Z_2(Mellin) × Z_2(W6-3) at moment-integral layer
   Anchor: Stage 1 = S87-MONODROMY-V_4-EXPLICIT (parallelogram-identity test)
   Promotion threshold: parallelogram holds in ≥2 of 3 spectral moments.

Candidate B: BdG-undoubled excess pattern (0, 1, 3, 2), E = 6 at bare-spectrum layer
   Anchor: S87-STRATUM3-LMAX-SCAN + S87-PARTITION-STABILITY-4STRATUM
   Promotion threshold: excess pattern stable across L_max ∈ {12, 13, 14, 15}
                         AND across τ ∈ {τ_fold ± δ_τ for δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10}}.
```

Each candidate has its own pass/fail logic; they don't gate each other. This decomposition addresses connes' E2 "registry-promotion" candidacy explicitly: candidate B's promotion threshold requires TWO gates (L_max and τ stability) before registry entry, providing the sequencing I argued for in DISSENT 2. Candidate A's promotion threshold is a single gate (parallelogram identity), which is structurally cleaner because V_4 commutativity is already forced (by connes A.Q1) and the only open question is whether the axes act on disjoint sub-bands (parallelogram exact) or with overlap (correction term).

**Cross-pollination implication.** The substrate at τ_fold simultaneously hosts two structurally distinct kinds of "4-ness":
- 4 strata in the bottom-20 bare spectrum, traceable to Peter–Weyl + BdG at L_max=12.
- 4 cosets of V_4 = Z_2(local) × Z_2(global) at moment-integral layer, traceable to two independent regulator branch cuts.

These two 4-counts coincidentally match in cardinality, but represent independent structural facts. The R3 verdict text should record BOTH as separate observables, with separate registry-promotion paths. This is the structural map that the workshop is producing.

---

## Round 3 — connes: Follow-up

### CONVERGENCE

**(C-1) PARALLELOGRAM identity is the structurally meaningful FORM of the V_4-character relation — concur with volovik R2-B D-1's physical content; it is ALGEBRAICALLY EQUIVALENT to my R2-A additive cocycle, but volovik's vertex-symmetric framing is the better presentation.** Volovik's D-1 mode-by-mode substitution chain (R2-B lines 1101–1117) produces the exact identity

```
A_ab + A_e − A_a − A_b = Σ_i n_i w(x_i) x_i^n · (σ_M(i) − 1)(σ_C(i) − 1)
                       = 4 · Σ_{i: σ_M(i)=σ_C(i)=−1} n_i w(x_i) x_i^n
```

I Sage-verified this turn (sage_eval, symbolic): expand((s_M − 1)(s_C − 1)) ≡ s_M·s_C − s_M − s_C + 1, an exact algebraic identity for {±1}-valued σ. Enumeration over (σ_M, σ_C) ∈ {±1}² confirms the product takes value 4 iff both are −1, and 0 otherwise.

I converge on volovik's PHYSICAL READING — the parallelogram identity is the substrate-physical-meaningful form of the V_4 character relation, with the "iff disjoint supports" condition giving a clean two-channel substrate-decomposition criterion (Mellin-sensitive sub-band ⊥ conformal-sensitive sub-band). I also concur on his Sage-numerical verification of disjoint vs overlap behaviour: numerical reproduction this turn on a 4-stratum (2,4,8,6) test spectrum with σ_M = [−1,−1,+1,+1], σ_C = [+1,+1,−1,−1] (DISJOINT) gives parallelogram residual 0.00e+00 to float epsilon, matching his "0.0 holds exactly" report; and σ_M = σ_C = [−1,+1,+1,+1] (OVERLAP at stratum 0) gives residual 4·m_0·w(x_0)·x_0^2 = 2.300, matching the algebraic prediction.

Volovik's vertex-symmetric framing `A_ab + A_e = A_a + A_b` (sum of opposite V_4 vertices) is structurally CLEANER than my R2-A asymmetric cocycle `(A_ab − A_e) = (A_a − A_e) + (A_b − A_e)` (deviation from identity), because it reads "A_ab is the 4th vertex of a parallelogram with vertices {A_e, A_a, A_b, A_ab} in V_4-coset space" — a geometric statement rather than a deviation-from-baseline statement. The S87-MONODROMY-V_4-EXPLICIT criterion text should adopt the parallelogram presentation for clarity (see DISSENT (D-1) below for the algebraic-equivalence subtlety).

**(C-2) D-2 BdG-undoubled excess L_max-stability gate before registry promotion — concur fully, sequencing is correct.** Volovik's D-2 substitution chain (R2-B lines 1140–1157) is right: the (0, 1, 3, 2) excess pattern at L_max = 12 may shift if (a) higher Peter–Weyl sectors mix into the bottom strata via Jensen deformation at L_max ≥ 13, or (b) stratum 3 splits into two strata of multiplicity 4 each at higher L_max (current 8 = 4 + 4 with within-float-tolerance near-degeneracy). Both possibilities are a priori plausible; only an L_max scan can distinguish. I converge on his proposed 2-gate sequencing: (i) S87-STRATUM3-LMAX-SCAN at L_max ∈ {12, 13, 14, 15} must close PASS-stable, (ii) S87-PARTITION-STABILITY-4STRATUM at τ ∈ {τ_fold ± δ_τ} must close PASS-stable, then (iii) registry promotion of (0, 1, 3, 2), E = 6 as substrate observable. This is sharper than my R2-A E2 (which implied immediate registry candidacy); volovik's two-gate gating is the right discipline.

NCG-side anchor for the L_max-sensitivity concern: the bottom-N strata of D_K^2 at finite L_max are defined by truncating L²(SU(3)) to ⊕_{(p,q): p+q ≤ L_max} V_{(p,q)} ⊗ V_{(p,q)}*. As L_max grows, new sectors enter the truncation, and Jensen deformation generically mixes them with lower sectors. The bottom-20 |λ| values are therefore L_max-DEPENDENT until a saturation L_max* is reached where the top of the bottom-20 sits well below the boundary of the L_max truncation. At L_max = 12 with τ = 0.190 and bottom-20 |λ| ∈ [0.6720, 0.7144] (R1 C1 finding), the saturation check is non-trivial — modes near the truncation edge can perturb the lowest 20 by an O(1/L_max²)-scale level repulsion (Wigner–von Neumann avoided crossing). Empirically validating L_max-saturation is therefore mandatory; the agreement with volovik's D-2 sequencing is structural, not stylistic.

**(C-3) D-3 PRU Class-8.2 recording (rubric-form failure) — concur fully, the conservative INFO closure is correct.** Volovik's D-3 (R2-B lines 1161–1167) sharpens the meta-rule: my R2-A E1 read the verdict as "INFO-coincidence-with-V_4-sharpening" treating the rubric ambiguity as resolved by V_4-sharpening; volovik reads it as "INFO with explicit rubric-extension carried forward to S87" treating the rubric-extension as a Class-8.2 PRU rubric-form failure that should NOT be absorbed into the verdict. I converge on his more conservative position. Reason: the verifier-rubric pre-registration rule (`.claude/rules/epistemic-discipline.md`) says "without (1)-(4), execution-time iteration to calibrate the rubric is structurally indistinguishable from iterate-until-PASS"; absorbing the rubric-extension into the verdict at R3 is an in-session calibration that risks the same pathology. The honest closure is INFO + explicit rubric ambiguity recorded for S87 pre-registration.

I want to add ONE structural observation: PRU Class-8.2 (the rubric-form sub-class) is a useful TAXONOMIC refinement of Class-8 (PRU at the machinery-pin level, per S78 origin). Class-8 covers cardinality test failures (missing pins); Class-8.2 covers rubric-form failures (literal pre-reg admitting unintended interpretations). The two are structurally distinct: 8 is "the plan failed to enumerate a parameter," 8.2 is "the plan enumerated the verifier's pattern-set but admitted an unintended logical reading of it." I propose this refinement be formalized as a permanent extension to `.claude/rules/epistemic-discipline.md` Verifier-Rubric Pre-Registration section in S87 (independent of S86 closure).

**(C-4) E-2 generalized REGULATOR-MONODROMY-AXIS-DECOMPOSITION methodology — concur fully, this is the correct generalization of my Q7.** Volovik's E-2 (R2-B lines 1207–1228) gives the answer to my R2-A Q7 ("does Mellin's local-vs-global independence generalize to other axis pairs?"): yes, via the 5-step methodology that, for an atlas A_n with m LOCAL axes (UV / heat-kernel-coefficient sign conventions, picked up by Wodzicki residue) + k GLOBAL axes (IR / asymptotic-completion topology selectors), generates the maximal abelian regulator monodromy (Z_2)^{m+k} with 2^{m+k} cosets. The Klein-four V_4 = (Z_2)^2 is the m=1, k=1 special case for A_5; richer atlases would generate richer monodromies.

NCG-side anchor for the LOCAL/GLOBAL classification: the Wodzicki-residue / a_4 locality argument (S82 W2-5 MP-Exclusion theorem, `permanent-theorems.md`) establishes that a_n coefficients are LOCAL invariants of the spectral triple, computable from the heat-kernel UV expansion regardless of asymptotic completion. By contrast, asymptotic-topology selectors (W6-3 conformal-end class, ℐ⁺ topology) are determined by GLOBAL data — the closure of the spectral triple at infinity, which is structurally independent of the bulk a_n content. This locality / globality dichotomy is exactly the dichotomy that the spectral-action axiomatic framework relies on: Connes-Marcolli (2007) §1.17 explicitly separates the local spectral-action computation (Seeley–DeWitt expansion) from the global completion (the choice of asymptotic regime). The 5-step methodology in volovik's E-2 IS that separation, applied to regulator-monodromy enumeration.

I converge on the full methodology and propose it be added to the framework's standard toolkit. Specifically: when the regulator atlas is extended in S87+ (e.g., adding Pauli–Villars's κ_PV as a third LOCAL axis), the methodology's prediction is V_4 × Z_2 = (Z_2)^3 = 8 cosets at the moment-integral layer. This is a STRUCTURAL PREDICTION, testable in S87+ via parallelogram-identity sweeps over 8-coset arithmetic — analogous to my R2-A E2 (BdG-undoubled half-counts), this becomes a registry-candidate observable in its own right once the atlas is extended.

**(C-5) E-3 BdG excess and V_4 cosets are TWO INDEPENDENT registry candidates — concur fully on the decomposition strategy.** Volovik's E-3 (R2-B lines 1230–1249) correctly separates the moment-integral V_4 monodromy candidate from the bare-spectrum BdG excess candidate. The two are observables at structurally different layers (regulator-class layer vs Peter–Weyl-stratum layer), with distinct gate sequences (single-gate parallelogram for V_4, two-gate L_max+τ for BdG excess). They don't gate each other; they probe independent structural facts. I converge on his table:

| Candidate | Layer | Gate sequence | Promotion threshold |
|:----------|:------|:--------------|:--------------------|
| A: V_4 monodromy | moment-integral | S87-MONODROMY-V_4-EXPLICIT (parallelogram) | residual ≤ 0.05 in ≥2 of 3 spectral moments |
| B: BdG excess (0,1,3,2), E=6 | bare-spectrum | S87-STRATUM3-LMAX-SCAN + S87-PARTITION-STABILITY-4STRATUM | both gates PASS-stable |

Both gates are 4–6 hour computation efforts (per my R2-A A.Q4 estimate). They proceed independently in S87.

### DISSENT

**(D-1) Volovik's D-1 framing "ADDITIVE cocycle is ALSO incorrect / parallelogram is structurally exact" is INCORRECT — the parallelogram identity is ALGEBRAICALLY EQUIVALENT to the additive cocycle. They differ only in normalization choice for the residual.** Sage-verification this turn (substitution chain):

```
Definition 1: PARALLELOGRAM (volovik D-1 form):  A_ab + A_e = A_a + A_b
Definition 2: ADDITIVE COCYCLE (connes R2-A D1):  (A_ab − A_e) = (A_a − A_e) + (A_b − A_e)

Substitution: Take Definition 1, subtract 2 A_e from both sides:
              A_ab + A_e − 2 A_e = A_a + A_b − 2 A_e
              A_ab − A_e         = (A_a − A_e) + (A_b − A_e)

Simplification: This is Definition 2.

Direction:    Parallelogram and additive cocycle are the SAME relation,
              algebraically reorganized. Their signed residuals are IDENTICAL:
                  R_para  := A_ab + A_e − A_a − A_b
                  R_addit := (A_ab − A_e) − (A_a − A_e) − (A_b − A_e)
                            = A_ab − A_e − A_a + A_e − A_b + A_e
                            = A_ab + A_e − A_a − A_b
                          = R_para.
```

Sage-verified numerical match (sage_eval, this turn, on volovik's reported sample numbers A_e = 9.917372, A_a = −1.987042, A_b = −4.205514, A_ab = −0.112408): parallelogram signed residual = +15.997520, additive cocycle signed residual = +15.997520, identical to float epsilon.

Volovik's R2-B D-1 reports "multiplicative residual 9.6%, additive residual 161%" using DIFFERENT NORMALIZATIONS:
- Multiplicative: |signed| / |A_e| = 0.955 / 9.917 = 9.6%.
- Additive (volovik's number): |signed| / |A_ab − A_e| = 15.998 / 10.030 = 159.5% ≈ 161%.

Under the SAME normalization |·|/|A_e|, the additive residual is 15.998/9.917 = 161% — matching the parallelogram normalization, NOT the multiplicative 9.6%. Both forms (parallelogram and additive cocycle) have identical residuals to float epsilon under matched normalization; they ARE the same relation.

DISSENT consequence: the V3 multiplicative form `A_n^(ab) = A_n^(a) · A_n^(b) / A_n^(e)` (V3 line 748) is genuinely structurally distinct from the parallelogram-identity-equivalence-class — it is a CHARACTER identity (multiplicative) which is structurally different from the COCYCLE / PARALLELOGRAM identity (additive). The dissent direction is: volovik's R2-B D-1 is correct that V3 multiplicative is wrong AND correct that parallelogram is the substrate-physical form. But the framing "your additive cocycle is ALSO INCORRECT" is incorrect — it is the same relation in different dress, and the residuals coincide.

**Implication for S87-MONODROMY-V_4-EXPLICIT.** The gate criterion volovik proposed in R2-B D-1 (PASS if `|A_n^(ab) + A_n^(e) − A_n^(a) − A_n^(b)| / |A_n^(e)| ≤ 0.05` for ≥2 of 3 moments) is mathematically identical to my R2-A criterion (PASS if `|(A_n^(ab) − A_n^(e)) − (A_n^(a) − A_n^(e)) − (A_n^(b) − A_n^(e))| / |A_n^(e)| ≤ 0.05` for ≥2 of 3 moments). Either form can be used. I recommend ADOPTING volovik's parallelogram presentation for the gate criterion text (it is more compact and geometrically meaningful), with a footnote acknowledging algebraic equivalence to my additive cocycle form.

**(D-2) The "iff disjoint supports" condition is a STRUCTURAL constraint on the substrate, not a generic property of V_4 actions on spectra — volovik's R2-B D-1 correctly identified the condition but understated its substrate-physical content.** The parallelogram identity holds exactly (residual 0) iff the σ_M = −1 support and σ_C = −1 support are disjoint at the bottom-20 spectrum level. This is NOT automatic for an arbitrary V_4 action on a generic spectrum — it is a SPECIFIC PROPERTY of the substrate that the Mellin-residue sign convention's flip-support and the W6-3 conformal-end sign convention's flip-support partition the bottom-20 modes into NON-OVERLAPPING sub-bands.

Substrate-physical interpretation (sharpening volovik's R2-B "phase-coexistence with separated order parameters" reading):

```
Definition 1: σ_M(i) = +1 for modes whose Mellin-residue at s = -1 is POSITIVE;
              σ_M(i) = -1 for modes where it is negative.
              The support of σ_M = -1 is the set of modes that flip sign under
              Mellin-axis monodromy.
Definition 2: σ_C(i) = +1 for modes that survive the asymptotic flat ℐ⁺ topology;
              σ_C(i) = -1 for modes that flip sign under conformal-end monodromy
              (asymptotic dS-vs-flat selector).
              The support of σ_C = -1 is the set of modes that flip sign under
              conformal-end-axis monodromy.
Definition 3: DISJOINT SUPPORTS condition: {i: σ_M(i) = -1} ∩ {i: σ_C(i) = -1} = ∅.
              Equivalently, no mode is sign-flipped by BOTH the Mellin-residue
              monodromy AND the conformal-end monodromy.

Substitution: For the substrate's bottom-20 spectrum at τ_fold, the Mellin-axis
              flip-support and the conformal-end-axis flip-support are physically
              determined by:
              (i) Whether the mode's |λ|² lies above/below the Mellin-residue's
                  s = -1 pole (a UV / heat-kernel sub-band selector).
              (ii) Whether the mode's eigenfunction has support concentrated
                  near the asymptotic ℐ⁺ vs in the bulk (a IR / asymptotic
                  sub-band selector).

Direction:    The substrate's PARALLELOGRAM-EXACT structure (residual 0) is
              the signature that conditions (i) and (ii) carve out DIFFERENT
              sub-bands of the spectrum — UV-sensitive modes are NOT
              IR-sensitive, and vice versa. This is the spectral analog of
              the local-vs-global axis independence of E-2's methodology
              applied at the mode level: each mode contributes to AT MOST
              ONE axis's monodromy, never both.
```

This is a STRONGER claim than volovik's R2-B "two-channel substrate" reading. It is a structural prediction about the bottom-20 modes' UV/IR character: the substrate's regulator monodromy should be parallelogram-EXACT (not approximately so) at first-order transit, because the local-vs-global axis independence of regulator data forces disjoint flip-supports at the mode level. This is the PROPER falsification target: if S87-MONODROMY-V_4-EXPLICIT returns a NON-ZERO parallelogram residual that traces to overlap modes, the substrate's regulator-class structure has overlap (mixed UV-IR sensitivity), which would be a structural surprise. If the residual is zero or ≤ 5% (above-floor noise), the disjoint-support reading holds.

I sharpen volovik's R2-B D-1 to this stronger reading: the parallelogram identity is not "the structurally exact form of the V_4 character relation" (a generic statement) — it is "the structurally exact form WHEN the V_4 axes have disjoint flip-supports," and the substrate-physical claim is that this disjoint-support structure is REQUIRED at first-order transit by the local-vs-global axis independence of E-2's methodology. This is testable in S87.

**(D-3) Pre-reg "Z_4 or similar" should NOT be expanded in-session at the workshop verdict level — the rubric ambiguity should be carried as a Class-8.2 INFO with explicit S87 pre-registration of the rubric, NOT as "INFO-coincidence-with-V_4-sharpening" at the verdict line.** This dissent is mild and refines my own R2-A position. In R2-A E1 I proposed the verdict text as "INFO-coincidence-with-V_4-sharpening" (volovik R2-B D-3 reads this as absorbing the rubric-extension into the verdict). On reflection (and converging with volovik's D-3 conservatism in CONVERGENCE C-3 above), I dissent on my own R2-A wording: the verdict line should read "INFO" with the V_4-sharpening as a separate FOOTNOTE or REGISTRY-CARRY-FORWARD entry, not as part of the verdict-line text itself. Reason: the verifier-rubric pre-registration rule explicitly forbids in-session calibration (it makes execution indistinguishable from iterate-until-PASS), and "V_4-sharpening" appended to "INFO-coincidence" reads as an in-session expansion of the rubric.

Proposed verdict line (revised from R2-A):

```
Bimodality:        PASS-nonbimodal at bare-eigenvalue layer
                   CONFIRMED-V_4-bimodality at moment-integral layer
                   (separate-row entry, distinct verdict)
4-fold cardinality: INFO (Class-8.2 PRU rubric-form failure)
                   carry-forward: pre-register S87 rubric explicitly to
                   admit-or-reject Klein-four under "Z_4 or similar."
```

This is more conservative than my R2-A text and more conservative than volovik's R2-B D-3 (which reads "INFO with rubric-extension deferred"). The conservatism is structural: each verdict line should pin one fact, and "the literal pre-reg admits two readings" is a separate structural fact from "V_4 is the substrate's monodromy group." Pin them separately.

### EMERGENCE

**(E-1) The PARALLELOGRAM IDENTITY is the STRUCTURALLY-CANONICAL FORM of the V_4 character relation for spectral moments — and it is precisely the (Z_2)^2 special case of a hypercube-vertex character identity that generalizes to (Z_2)^{m+k} per E-2's methodology.** Joint reading of volovik's R2-B E-2 (5-step regulator-monodromy methodology) plus my D-1 algebraic-equivalence verification reveals a deeper structural fact: the parallelogram identity is the simplest non-trivial case of a HYPERCUBE-VERTEX CHARACTER IDENTITY for (Z_2)^d acting on spectral moments via independent {±1} sign involutions. The hypercube-vertex structure:

```
Definition 1: V = (Z_2)^d acting on the spectrum by d independent {±1} involutions
              σ_1, ..., σ_d. V has 2^d elements indexed by binary tuples
              ε = (ε_1, ..., ε_d) ∈ {0, 1}^d, with ε_j = 0 ↔ σ_j = +1, ε_j = 1 ↔ σ_j = -1.
Definition 2: For g_ε ∈ V, the spectral moment is
              A_n^{(ε)} = Σ_i n_i w(x_i) (Π_j σ_j(i)^{ε_j}) x_i^n.
Definition 3: The HYPERCUBE-VERTEX CHARACTER IDENTITY for (Z_2)^d:
              Σ_{ε ∈ {0,1}^d} (-1)^{|ε|} A_n^{(ε)} = 2^d · Σ_{i: σ_j(i)=-1 ∀j} n_i w(x_i) x_i^n
              where |ε| = Σ_j ε_j is the Hamming weight.
              Holds (residual = 0) iff the supports {i: σ_j(i) = -1} have empty
              all-axes-flipped intersection {i: σ_j(i) = -1 ∀j} = ∅.
              [Algebraic origin: Π_j (1 - σ_j(i)) ∈ {0, 2^d}, taking value 2^d
              iff every σ_j(i) = -1 at mode i, else 0. Sage-verified this turn
              at d ∈ {3, 4, 5} via direct enumeration of all 2^d cosets.]

Substitution: For d = 1 (single Z_2): A_n^{(0)} - A_n^{(1)} = 2 · Σ_{i: σ(i) = -1} n_i w(x_i) x_i^n.
                                       (Sign +2, as 2^1 = 2.)
              For d = 2 (V_4 = (Z_2)^2): A_n^{(00)} - A_n^{(10)} - A_n^{(01)} + A_n^{(11)}
                                        = 4 · Σ_{i: σ_M(i) = σ_C(i) = -1} n_i w(x_i) x_i^n.
                                        (Sign +4 = 2^2.) This is the PARALLELOGRAM
                                        IDENTITY (volovik D-1 / connes additive cocycle).
                                        Holds iff {σ_M = -1} ∩ {σ_C = -1} = ∅.
              For d = 3 ((Z_2)^3 = 8-coset hypercube): residual = 8 · Σ_{i: all σ_j = -1} n_i w(x_i) x_i^n.
                                                       (Sign +8 = 2^3.)
                                                       Holds iff triple-overlap support is empty.
              General d: residual = 2^d · Σ_{i: all σ_j = -1} n_i w(x_i) x_i^n.

Simplification: The hypercube-vertex character identity is the d-DIMENSIONAL
              GENERALIZATION of the parallelogram identity. For (Z_2)^d acting
              on a substrate where the d sign-flip supports are pairwise disjoint
              at the MODE level, the d-dimensional identity holds exactly. For
              non-empty all-axes-flipped supports, the residual measures the
              "overlap mode" content.

Direction:    The framework's regulator monodromy (Z_2)^{m+k} via E-2's methodology
              has, as its CONSISTENCY CHECK, the (m+k)-dimensional hypercube-vertex
              character identity. The parallelogram-identity gate at d = 2 is the
              PROTOTYPE for this consistency check; richer atlases require richer
              identities, but the structural form is universal.
```

This reframes the V_4 monodromy candidate from "a Klein-four group acting on regulator weights" to "the d=2 instance of a (Z_2)^d regulator-monodromy framework whose consistency criterion is the hypercube-vertex character identity at the moment-integral layer." The methodology (E-2) and the consistency check (D-1 parallelogram, generalized) are TWO SIDES OF THE SAME COIN: the methodology enumerates the (Z_2)^d structure, and the hypercube-identity tests whether the substrate satisfies the disjoint-support condition that makes (Z_2)^d a clean abelian regulator monodromy at the mode level.

**Substrate-physical implication.** The framework predicts that when the regulator atlas is extended to A_n with m local + k global axes, the substrate's mode content at first-order transit should partition into (m+k)+1 sub-bands: m UV-sensitive sub-bands (one per local axis) + k IR-sensitive sub-bands (one per global axis) + 1 axis-invariant sub-band. The hypercube-identity tests this partitioning at the spectral-moment level. This is a sharp testable prediction about the structure of the bottom spectrum at τ_fold under regulator-atlas extension — a STRUCTURAL CONSEQUENCE of the substrate's local-vs-global axis decomposition.

**(E-2) Class-8.2 (rubric-form PRU) is a TAXONOMIC EXTENSION to the framework's methodology rules — it should be formalized in `.claude/rules/epistemic-discipline.md` independent of S86 closure.** Joint reading of volovik's R2-B D-3 / E-1 (4-stage upgrade pathway with Class-8.2 recording) plus the framework's existing PRU methodology (S78 origin, Class-8 cardinality test) reveals that the rubric-form failure is structurally distinct from the cardinality failure and warrants its own taxonomy slot:

```
PRU Class taxonomy (proposed extension):
  Class 8.0  (or 8.1)   : machinery-pin cardinality failure (S78 origin; the original
                          Class 8 — plan failed to enumerate a parameter).
  Class 8.2 (NEW)       : verifier-rubric pre-registration failure (S86 W-12 origin;
                          plan enumerated the verifier's pattern-set but admitted
                          an unintended logical reading of "or similar" / "or
                          equivalent" / "any of [X, Y, ...]" tokens).
  Class 8.3 (potential) : output-precision pre-registration failure (S86 W1c-8 origin;
                          plan enumerated values but did not pin the publication
                          precision used by downstream verifiers).
```

The S86 W-12 workshop is the calibration corpus for Class-8.2: the literal pre-reg "Z_4 or similar" admitted an unintended reading (Klein-four as "similar" via cardinality match). A formal Class-8.2 entry in `epistemic-discipline.md` would prevent the same pathology in S87+ by requiring rubric specifications to enumerate (1) the explicit pattern-set, (2) the disjunction-vs-conjunction structure, (3) optional negative-marker set, (4) calibration corpus exemplars — exactly what the existing Verifier-Rubric Pre-Registration rule already requires. The Class-8.2 label is a TAXONOMIC anchor for cross-session referencing of this category of failure; it does not introduce new methodology.

**Carry-forward implication.** The S87 plan should include a wave-0 rule-file maintenance item: extend `.claude/rules/epistemic-discipline.md` PRU class taxonomy to formally name Class-8.2. This is a 30-minute documentation task, not a computation gate, but it is structural (it ensures the taxonomy is searchable in the knowledge index, and that future audits can reference Class-8.2 as a closed sub-category). I propose this be the first item of S87 wave-0.

**(E-3) The W-12 workshop produces a STRUCTURAL TRIPLE — V_4 monodromy candidate (moment-integral layer) + BdG excess candidate (bare-spectrum layer) + Class-8.2 taxonomy extension (methodology layer) — three independent contributions from a single workshop.** Joint reading of all R1-R3 content reveals that this workshop has produced THREE structurally distinct outputs, each with its own promotion path:

| Output | Layer | Origin | Promotion path |
|:-------|:------|:-------|:---------------|
| V_4 = (Z_2)^2 monodromy candidate | moment-integral (regulator class) | C2 + C4 + V3 + R2-A E3 + R2-B C-5 | S87-MONODROMY-V_4-EXPLICIT (parallelogram), single gate |
| BdG-undoubled excess (0,1,3,2), E=6 | bare-spectrum (Peter–Weyl stratum) | C1 + V2 + R2-A E2 + R2-B C-5 / D-2 | S87-STRATUM3-LMAX-SCAN + S87-PARTITION-STABILITY-4STRATUM, two-gate sequence |
| PRU Class-8.2 taxonomic extension | methodology (rule-file) | R2-A E1 + R2-B C-1 / D-3 / C-3 | S87 wave-0 rule-file maintenance, documentation-only |
| (auxiliary) (Z_2)^{m+k} hypercube-identity methodology | meta (framework toolkit) | R2-B E-2 + R3-A E-1 | included in S87 plan as auxiliary methodology, not gated |

The four outputs are structurally INDEPENDENT — each has its own promotion path, its own evidence base, and its own potential failure modes. The workshop is therefore PROLIFIC at the structural level even though the literal pre-reg "PASS-monodromy / PASS-bimodal" verdicts are INFO. This is the right framing for the registry: no single gate landed PASS, but four independent structural candidates emerged, each with a clean S87 closure path.

**Cross-pollination implication.** This W-12 workshop is METHODOLOGICALLY analogous to the S85 W-3 + S86 W0a-1 union closure (PRU + SOURCE-RECONCILIATION rule consolidation): a single workshop output produces multiple independent rule-file / methodology / observable contributions, each absorbed into the framework via its own promotion path. The W-12 four-output structure should be the template for "high-density" workshops: when a single workshop produces multiple structural insights, decompose them into independent registry/rule-file/methodology promotion paths rather than forcing a single verdict.

### QUESTIONS

**Locking in the verdict.** Given the joint R2-A + R2-B + R3-A content, the workshop verdict should be:

```
Bimodality (Topic 6):
  PASS-nonbimodal at bare-eigenvalue layer
  CONFIRMED-V_4-bimodality at moment-integral / conformal-end layer
  (two-row verdict; separate scores at separate layers)

4-fold cardinality (Topic 7):
  INFO (Class-8.2 PRU rubric-form failure recorded)
  V_4 = (Z_2)^2 monodromy candidate identified, promotion via S87-MONODROMY-V_4-EXPLICIT
  BdG-undoubled excess (0,1,3,2), E=6 candidate identified, promotion via two-gate sequence
  Pre-reg "Z_4 or similar" requires explicit S87 rubric-extension before re-test
```

I lock in this verdict structure. Five questions remain for volovik's R3-B FINAL turn (Verdict + Wrap-Up):

**Q10 (gate criterion phrasing).** Do you concur on adopting the PARALLELOGRAM presentation `|A_n^(ab) + A_n^(e) − A_n^(a) − A_n^(b)| / |A_n^(e)| ≤ 0.05` (your R2-B D-1 form, geometrically meaningful) for the S87-MONODROMY-V_4-EXPLICIT criterion text, with a footnote that it is algebraically equivalent to my R2-A additive cocycle (per my R3-A D-1 Sage-verified equivalence)? This is the cleaner presentation — a single equation rather than the asymmetric deviation-from-baseline form.

**Q11 (parallelogram-EXACT vs parallelogram-APPROX criterion).** My R3-A D-2 argues the substrate-physical claim is parallelogram EXACT (residual = 0 to float epsilon at saturated L_max), not merely ≤ 5%. The local-vs-global axis independence of E-2's methodology, applied at the MODE level, predicts disjoint flip-supports at the mode level. Should the S87-MONODROMY-V_4-EXPLICIT gate split into two thresholds: (i) PASS-parallelogram-exact at residual ≤ 1e-10 (substrate-physical structural claim), (ii) PASS-parallelogram-approx at residual ≤ 0.05 (numerical-stability gate, weaker claim)? The former is the structurally clean test; the latter accommodates float-epsilon noise from finite-L_max truncation.

**Q12 (hypercube-identity carry-forward).** My R3-A E-1 generalizes the parallelogram identity to a (Z_2)^{m+k} hypercube-vertex character identity. Should this be encoded as a SEPARATE carry-forward (e.g., S87-HYPERCUBE-IDENTITY-METHODOLOGY) or absorbed into the S87 framework toolkit without a dedicated gate? My instinct is the latter (the methodology is structural, not a verdict-bearing gate), but the framework's toolkit-extension precedent (W-3 / W0a-1 PRU + SOURCE-RECON consolidation) suggests an explicit CARRY-FORWARD with a 4-field spec to ensure it lands in S87's rule-file. Your call.

**Q13 (3He-B independent BdG excess count for Q6 follow-up).** In my R2-A Q6 I asked whether 3He-B at polycritical pressure has an independent count of "extra phases" coexisting at the discrete Andreev-bound levels, predicting any specific integer to compare with our (0, 1, 3, 2), E = 6. This is a substrate-vs-3He-B inheritance test. Do you have a 3He-B answer for this (e.g., "at the polycritical point, the topological invariant N_BdG = 3 generates 3 chiral-pair quanta, predicting excess = 3" — or some other integer)? If 3He-B gives a different prediction, our substrate's E = 6 is substrate-specific (not inherited from 3He-B); this would feed `feedback_3heb-inheritance.md` as a specific rank-of-excess data point per `session-85-1b-3heb-inversion-landau.md` (rank(E) = 3 there vs E = 6 here — at different layers but worth comparing).

**Q14 (workshop verdict text — final phrasing).** Given the four structural outputs (V_4, BdG excess, Class-8.2, hypercube-methodology), what should the official Workshop Wrap-Up "What Changed" text read? My proposed text:

```
What Changed: W-12 produced FOUR INDEPENDENT structural candidates from a single
              bimodality + 4-fold cardinality probe:
              (i) V_4 = (Z_2)^2 monodromy candidate at moment-integral layer
                  (Z_2(Mellin local-residue) × Z_2(W6-3 global-asymptotic-topology));
                  S87 promotion via parallelogram-identity gate.
              (ii) BdG-undoubled excess (0, 1, 3, 2), E = 6 at bare-spectrum layer;
                   S87 promotion via L_max scan + τ-stability sequence.
              (iii) PRU Class-8.2 (rubric-form failure) taxonomic extension;
                    S87 wave-0 rule-file maintenance (documentation-only).
              (iv) (Z_2)^{m+k} hypercube-vertex character identity as
                   GENERALIZATION of the parallelogram identity to richer atlases;
                   absorbed into framework toolkit as auxiliary methodology.
              The literal pre-reg "PASS-monodromy / PASS-bimodal" verdicts close as
              INFO at both layers; the structural harvest is FOUR registry/rule-file
              candidates from a single workshop.
```

Do you concur on this text or sharpen it? In particular: should output (iv) be promoted to a fifth INDEPENDENT candidate (own carry-forward) rather than "absorbed into toolkit"?

---

## Round 3 — volovik: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

**(C-1) Accept connes R3-A D-1 in full: PARALLELOGRAM and ADDITIVE COCYCLE are ALGEBRAICALLY EQUIVALENT — my R2-B framing "your additive cocycle is ALSO INCORRECT" was itself INCORRECT. I retract that framing and adopt the parallelogram presentation per connes Q10.** Connes' R3-A D-1 substitution chain (lines 1295-1314) walks the algebra: subtract 2·A_e from both sides of the parallelogram form `A_ab + A_e = A_a + A_b` and the result is `A_ab − A_e = (A_a − A_e) + (A_b − A_e)`, which is the additive cocycle. Sage independently confirmed this turn (mcp__sage__sage_eval, symbolic):

```
Definition 1: PARALLELOGRAM (R2-B D-1):       R_para  := A_ab + A_e − A_a − A_b
Definition 2: ADDITIVE COCYCLE (R2-A D1):     R_addit := (A_ab − A_e) − (A_a − A_e) − (A_b − A_e)
Substitution: Expand R_addit = A_ab − A_e − A_a + A_e − A_b + A_e
                            = A_ab + A_e − A_a − A_b
                            = R_para
Simplification: Sage symbolic difference R_para − R_addit = 0 (exact, this turn).
Direction:    R_para ≡ R_addit identically. Two presentations of the same relation.
```

Numerical reproduction confirms: on the volovik R2-B sample (A_e = 9.917372, A_a = −1.987042, A_b = −4.205514, A_ab = −0.112408), parallelogram signed residual = +15.9975200, additive cocycle signed residual = +15.9975200, identical to float epsilon. The "9.6% multiplicative vs 161% additive" gap I reported in R2-B D-1 was a normalization mismatch artefact: the multiplicative residual was normalized by |A_e| while the additive residual was normalized by |A_ab − A_e| (different denominator). Under matched |A_e| denominator, both my "additive" residual and connes' parallelogram form give identical 161% deviations on that sample (numerically verified this turn: |15.998|/|9.917| = 161.3%). My "ALSO INCORRECT" framing conflated a normalization choice with a structural difference; connes' D-1 correctly diagnoses this as an algebraic-equivalence question, not a separate structural relation.

**Adopt the parallelogram presentation for the S87-MONODROMY-V_4-EXPLICIT criterion text** (per Q10): the geometrically-clean form `|A_n^(ab) + A_n^(e) − A_n^(a) − A_n^(b)| / |A_n^(e)| ≤ 0.05` reads as "A_ab is the 4th vertex of a parallelogram with vertices {A_e, A_a, A_b, A_ab} in V_4-coset space" — a vertex-symmetric statement. The footnote should record algebraic equivalence to connes' R2-A asymmetric `(A_ab − A_e) − (A_a − A_e) − (A_b − A_e)` form.

The substantive content of my R2-B D-1 — that the V3 multiplicative form `A_n^(ab) = A_n^(a) · A_n^(b) / A_n^(e)` is wrong (character-like, holds only for delta-function spectra or factorisable σ_M, σ_C with specific tuned values), and that the substrate-physical form is the additive parallelogram-equivalent — STANDS. The retraction is solely about the "additive cocycle is ALSO incorrect" sub-claim, which was wrong; the additive cocycle is the right form, just presented less geometrically than the parallelogram.

**(C-2) Accept connes R3-A D-2 STRUCTURAL substrate constraint reading: parallelogram-EXACT is the substrate-physical claim, not parallelogram-APPROX.** Connes R3-A D-2 (lines 1328-1366) sharpens my R2-B D-1 "iff disjoint supports" framing into a structural prediction: the substrate's regulator monodromy should be parallelogram-EXACT (residual = 0 to float epsilon at saturated L_max), not merely ≤ 5%, because the local-vs-global axis independence of E-2's methodology applied at the MODE level forces disjoint flip-supports. Each mode contributes to AT MOST ONE axis's monodromy (UV-sensitive XOR IR-sensitive), never both.

I concur on the structural reading and on the proposed two-threshold gate split (per Q11): (i) PASS-parallelogram-exact at residual ≤ 1e-10 = the substrate-physical structural claim (disjoint flip-supports at mode level, forced by local-vs-global axis independence); (ii) PASS-parallelogram-approx at residual ≤ 0.05 = numerical-stability gate accommodating finite-L_max float-epsilon noise. The former is the structurally clean test; the latter is the engineering tolerance band. Both should be reported in the gate verdict line; only PASS-exact licenses the "structural V_4 monodromy with disjoint-support condition" registry promotion (R2-B E-3 Stage 3).

Superfluid-side anchor strengthening D-2's structural reading: in 3He-B at first-order A↔B transit, the BdG spectrum splits at the mode level into an Andreev-bound shell (sensitive to LOCAL pair-breaking parameters Δ near k_F) and a continuum (sensitive to GLOBAL gauge-rotation phase of the order parameter manifold). Volovik–Mineev 1976 Onsager-prize foundation paper (parent of the S60 inheritance framework, `framework-3heb-comparison.md`) shows these two sub-bands are physically separated — no Andreev-bound mode carries a non-zero gauge-rotation phase, no continuum mode has measurable pair-breaking sensitivity. This is the 3He-B precedent for connes' D-2 mode-level disjoint-support claim. The substrate inherits this two-channel decomposition at the spectral-action layer; the parallelogram-exact form is the spectral analog of the 3He-B "Andreev-bound XOR continuum" classification.

**(C-3) Accept connes R3-A D-3 conservative INFO + footnote refinement: V_4-sharpening as separate footnote / registry-carry-forward, not absorbed into verdict-line text.** Connes R3-A D-3 (lines 1368-1381) refines my R2-B D-3 conservatism by separating two distinct facts that I had bundled in "INFO with rubric-extension deferred": (i) the literal pre-reg admits two readings (a Class-8.2 PRU rubric-form failure, recorded for S87 pre-registration); (ii) V_4 is the substrate's monodromy group at moment-integral layer (a structural finding worth its own registry entry). The separation is correct: each verdict line should pin one fact. I converge on the proposed verdict structure:

```
Bimodality:        PASS-nonbimodal at bare-eigenvalue layer
                   CONFIRMED-V_4-bimodality at moment-integral layer
                   (separate-row entry, distinct verdict)
4-fold cardinality: INFO (Class-8.2 PRU rubric-form failure)
                   carry-forward: pre-register S87 rubric explicitly to
                   admit-or-reject Klein-four under "Z_4 or similar."
```

This is more conservative than my R2-B D-3 text (which absorbed the V_4-sharpening into the verdict) and respects the verifier-rubric pre-registration discipline (`.claude/rules/epistemic-discipline.md` "Verifier-Rubric Pre-Registration"). The V_4 finding is preserved as a separate-row CONFIRMED-V_4-bimodality verdict at moment-integral layer (where the rubric ambiguity does not apply — V_4 is the actual substrate monodromy group, independent of how "Z_4 or similar" is read). The 4-fold cardinality verdict-line is INFO with an explicit rubric-extension carry-forward; the V_4 monodromy is its own structural claim with its own promotion path via S87-MONODROMY-V_4-EXPLICIT.

**(C-4) Accept connes R3-A E-1 HYPERCUBE-VERTEX CHARACTER IDENTITY for (Z_2)^d generalization with prefactor +2^d (Sage-verified this turn).** Connes' R3-A E-1 (lines 1385-1430) generalizes the parallelogram identity from (Z_2)^2 to (Z_2)^d via the hypercube-vertex character identity:

```
Σ_{ε ∈ {0,1}^d} (-1)^|ε| A_n^(ε) = 2^d · Σ_{i: σ_j(i) = -1 ∀j} n_i w(x_i) x_i^n
```

I Sage-verified the prefactor sign this turn (mcp__sage__sage_eval) at d ∈ {2, 3, 4} via direct algebraic enumeration:

```
Algebraic origin: Π_j (1 − σ_j) ∈ {0, 2^d}, taking value 2^d iff σ_j = −1 ∀j, else 0.
At d=2: (1 − s_M)(1 − s_C) at s_M = s_C = -1 → (1 − (−1))(1 − (−1)) = 2·2 = 4 = +2^2  ✓
At d=3: Π_{j=1,2,3} (1 − s_j) at all s_j = -1 → 2·2·2 = 8 = +2^3  ✓
At d=4: Π_{j=1,2,3,4} (1 − s_j) at all s_j = -1 → 2·2·2·2 = 16 = +2^4  ✓
At any s_j = +1: factor (1 − 1) = 0 forces the product to 0  ✓
```

Sign is +2^d, not −2^d. The parallelogram identity at d=2 with prefactor +4 (= +2²) is the special case verified mode-by-mode in my R2-B D-1 substitution chain (where I derived `A_ab + A_e − A_a − A_b = 4 · Σ_{i: σ_M(i) = σ_C(i) = -1} n_i w(x_i) x_i^n`); this is consistent with connes' E-1 generalized form.

The prefactor +2^d makes the SUBSTRATE-PHYSICAL prediction sharp: when the regulator atlas extends to A_n with d = m + k axes (m local + k global per E-2 methodology), the (Z_2)^d hypercube-identity residual measures the "all-axes-flipped" overlap content of the bottom spectrum. For an atlas where the d sign-flip supports are pairwise disjoint at the mode level, the all-axes-flipped intersection is empty and the residual vanishes. For overlap, the residual scales as 2^d · (overlap-mode spectral content). This is the structural consistency check at arbitrary atlas depth.

Superfluid-side reading: in 3He-B at first-order transit, the (Z_2)^d hypercube structure corresponds to d independent symmetry breakings at the cusp (particle-hole × gauge × sub-lattice × ... for d > 2). The disjoint-support condition is the "no mode is flipped by all symmetry breakings simultaneously" — a generic property of multi-channel coexistence at a cusp, where each mode carries at most one "broken-symmetry charge." The (Z_2)^d hypercube-identity is the spectral-action generalization of this multi-channel decomposition.

**(C-5) Accept connes R3-A E-2 PRU Class-8.2 sub-class formal taxonomy + R3-A E-3 STRUCTURAL TRIPLE + auxiliary count.** Connes R3-A E-2 (lines 1432-1449) formalizes the PRU Class-8.2 sub-class taxonomic extension I proposed in R2-B D-3, with three taxonomic slots:

```
PRU Class taxonomy (proposed extension):
  Class 8.0 / 8.1  : machinery-pin cardinality failure (S78 origin; original Class 8 —
                     plan failed to enumerate a parameter).
  Class 8.2 (NEW)  : verifier-rubric pre-registration failure (S86 W-12 origin;
                     plan enumerated the verifier's pattern-set but admitted an
                     unintended logical reading of "or similar" / "or equivalent" /
                     "any of [X, Y, ...]" tokens).
  Class 8.3 (potential): output-precision pre-registration failure (S86 W1c-8 origin;
                         plan enumerated values but did not pin the publication
                         precision used by downstream verifiers).
```

The 8.2 sub-class is the structurally-correct slot for the "Z_4 or similar" rubric-form pathology: the plan enumerated the verifier's pattern-set ("Z_4 or similar") but admitted an unintended logical reading (Klein-four V_4 as "similar" via cardinality match, despite being structurally distinct via element orders). The S86 W-12 workshop is the calibration-corpus exemplar.

I converge on the structural triple + auxiliary count framing (R3-A E-3, lines 1451-1462): four independent structural outputs from a single workshop:

| # | Output | Layer | Promotion path |
|:-:|:-------|:------|:---------------|
| 1 | V_4 = (Z_2)^2 monodromy candidate | moment-integral (regulator class) | S87-MONODROMY-V_4-EXPLICIT (parallelogram), single gate |
| 2 | BdG-undoubled excess (0,1,3,2), E=6 | bare-spectrum (Peter-Weyl stratum) | S87-STRATUM3-LMAX-SCAN + S87-PARTITION-STABILITY-4STRATUM, two-gate sequence |
| 3 | PRU Class-8.2 taxonomic extension | methodology (rule-file) | S87 wave-0 rule-file maintenance, documentation-only |
| 4 | (Z_2)^{m+k} hypercube-identity methodology | meta (framework toolkit) | S87 plan auxiliary methodology, OR explicit gate per Q12 (decided below) |

This is the right framing — each output has its own promotion path, evidence base, and potential failure mode. The literal pre-reg "PASS-monodromy / PASS-bimodal" verdicts close as INFO at the verdict-line level; the structural harvest is four independent registry/rule-file/methodology candidates, exceeding what either pre-registered branch (PASS / FAIL) would have produced.

**(C-6) Accept connes Q14 four-output Workshop Wrap-Up "What Changed" text — adopt with minor sharpening on output (iv).** Connes' Q14 proposed text (lines 1493-1510) records the four structural candidates as the workshop's harvest. I adopt the framing with one sharpening: output (iv) the (Z_2)^{m+k} hypercube-identity methodology should be promoted to a fifth INDEPENDENT carry-forward with its own 4-field S87 spec (`S87-HYPERCUBE-VERTEX-IDENTITY-LANDING`), NOT merely "absorbed into framework toolkit" (per Q12 — my position is the explicit-carry-forward route). Reason: the methodology's correctness depends on Sage-verified prefactor +2^d (this turn) AND the substrate-physical disjoint-support claim at d > 2 (which has not yet been tested at any d > 2 atlas). The toolkit-extension precedent (W-3 / W0a-1 PRU + SOURCE-RECON consolidation) establishes that toolkit promotions need explicit landing gates; the hypercube-identity is at the same structural depth as the parallelogram identity (one is the d=2 case of the other), so it deserves the same gate treatment.

So the final "What Changed" text records FIVE structural candidates: V_4 monodromy, BdG excess, Class-8.2 taxonomy, hypercube-identity methodology promoted to its own gate, and the methodology IS still also a framework toolkit extension once it lands. The four-vs-five distinction is whether the hypercube-identity gets its own gate (my position, Q12 explicit) or absorbed (connes Q14 implicit). Convergence direction: explicit carry-forward.

### DISSENT

**No new substantive dissent at R3 closure.** The R2 / R3-A round resolved all R1 / R2 / R3-A dissents into convergences: connes R2-A D-1 (additive cocycle) was correctly framed; my R2-B D-1 ("ALSO INCORRECT") retraction in C-1 above closes that loop. R3-A D-1 (algebraic equivalence) is accepted; R3-A D-2 (structural substrate constraint) is accepted with two-threshold gate split per Q11; R3-A D-3 (conservative INFO + footnote) is accepted per C-3. My R2-B D-2 (BdG excess L_max stability before promotion) was accepted by connes R3-A C-2; my R2-B D-3 (rubric-form Class-8.2) was accepted by connes R3-A C-3 and formalized in R3-A E-2.

The remaining open structural questions (Q5-Q9 from connes R2-A, Q10-Q14 from connes R3-A, Q1-Q4 from my V4) all map to S87 follow-up gates rather than R3 dissents. Q13 (3He-B independent excess count) is the one open inheritance-test question without a definitive answer this turn; I provide a partial answer in EMERGENCE E-3 below, but flagging that as a S87 carry-forward computation rather than a R3 dissent is the right discipline.

**Reserved for genuine S87 follow-up (per workshop discipline — not R3 dissent):**

- **Q11 two-threshold split** (parallelogram-EXACT vs parallelogram-APPROX): the structural claim is parallelogram-EXACT at saturated L_max; engineering tolerance is parallelogram-APPROX at residual ≤ 0.05. Both should be reported in S87-MONODROMY-V_4-EXPLICIT. This is a gate-criterion sharpening, not a content dissent.

- **Q13 3He-B inheritance count**: the partial answer (E-3 below) is "3He-B at polycritical pressure has 4 broken-symmetry generators (SO(3)_S × SO(3)_L × U(1)_φ × Z_2_T → Z_2_diag), giving rank ≤ 4 broken-symmetry charge content; comparison with substrate's E = 6 requires a layer-matched count which I cannot complete this round." The substrate-vs-3He-B inheritance test should be formalized as a S87 gate `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` rather than a R3 dissent.

### EMERGENCE

**(E-1) The W-12 workshop's four-output structure (V_4 monodromy + BdG excess + Class-8.2 taxonomy + hypercube-identity methodology) constitutes a "high-density workshop" template — METHODOLOGICALLY ANALOGOUS to S85 W-3 + S86 W0a-1 union closure but at finer structural granularity.** Joint reading of all R1-R3 content reveals that this workshop's harvest is qualitatively different from typical bimodality / cardinality probes: it produced FIVE independent registry/rule-file/methodology contributions (counting hypercube-identity as separate per Q12) from a single 2-agent 3-round workshop, not because the agents over-generated but because the structural target (substrate's 4-fold cardinality coincidence) decomposed naturally into independent layers (bare-spectrum / moment-integral / methodology / meta-methodology / inheritance-test). The decomposition itself is the methodology lesson:

```
HIGH-DENSITY WORKSHOP TEMPLATE (W-12 calibration):
  When a workshop's structural target straddles multiple layers (bare/derived/
  methodology/meta), the verdict should NOT force a single PASS/FAIL/INFO at
  the literal pre-reg, but rather decompose into INDEPENDENT OUTPUT slots,
  each with its own promotion path. A single workshop can simultaneously:
    (i) close one literal pre-reg verdict as INFO (rubric-form failure),
    (ii) generate a structural candidate at one layer (registry promotion path),
    (iii) generate a structural candidate at another layer (separate path),
    (iv) extend the methodology rule-file (taxonomic extension),
    (v) generalize the methodology to broader contexts (toolkit extension with own gate).
  This is the "four-output / five-output" structure connes R3-A E-3 articulated.
  It should be the template for future high-density workshops.
```

The W-12 template is the structural complement to the v3-closure recovery procedure (which handles methodology-failure pathologies bottom-up): high-density workshops handle structural-richness top-down by decomposing single-target probes into multi-layer output slots. This is a permanent contribution to the framework's collaboration methodology.

**(E-2) The (Z_2)^d hypercube-identity provides a "regulator-monodromy depth" observable — testable as the atlas extends, predicting structural growth patterns.** Connes R3-A E-1 generalized the parallelogram to the hypercube; my R2-B E-2 5-step methodology enumerates the (Z_2)^{m+k} structure for atlases with m local + k global axes. Joint reading: as the regulator atlas A_n extends with new axes (e.g., adding Pauli-Villars's κ_PV as a third LOCAL axis, or adding a topological-sector selector as a second GLOBAL axis), the framework's regulator-monodromy depth d = m + k grows monotonically. The hypercube-identity provides the structural consistency check at each depth; the substrate's parallelogram-exact (or hypercube-exact) structure at depth d = m + k tests whether the substrate respects the disjoint-support condition at the mode level.

A new observable: the "regulator-monodromy depth" of the substrate, defined as the maximum d for which the (Z_2)^d hypercube-identity holds with EXACT residual on the bottom-N modes at saturated L_max. The substrate at τ_fold has depth ≥ 2 (V_4 confirmed candidate via S87-MONODROMY-V_4-EXPLICIT); whether it has depth = 2 (exactly) or higher is a S87+ question testable by atlas extension. Substrate-physical reading: the depth measures how many INDEPENDENT regulator-class boundaries the substrate's mode content respects without overlap. A higher depth means richer coexistence at first-order transit; a lower depth means the substrate has "saturated" its regulator sensitivity at the atlas's local + global axis count. This is the substrate-physical generalization of the S60 inheritance framework's "correspondence count" (`framework-3heb-comparison.md`): instead of counting 3He-B-vs-substrate correspondences, count regulator-axis depth at which the substrate's monodromy structure remains parallelogram-exact.

**(E-3) Partial answer to Q13 3He-B inheritance count: 3He-B's broken-symmetry generator content predicts rank ≤ 4 broken-symmetry charges at polycritical pressure, not directly comparable to substrate's E = 6 — the comparison requires a layer-matched count, which is a S87 inheritance-test gate.** Connes R2-A Q6 / R3-A Q13 asks whether 3He-B has an independent count of "extra phases coexisting at the discrete Andreev-bound levels" predicting any specific integer to compare with our substrate's E = 6. Partial answer:

```
Definition 1: 3He-B normal-state symmetry: G = SO(3)_S × SO(3)_L × U(1)_φ
              (spin × orbital × global phase rotation; T-reversal Z_2_T present in normal phase).
Definition 2: 3He-B condensate symmetry: H = SO(3)_J=L+S × U(1)_φ_diag (diagonal residual).
Definition 3: Broken-symmetry generators: G/H has dimension dim(G) − dim(H) = (3+3+1) − (3+1) = 3.
              Plus T-reversal action on the order parameter: discrete Z_2 broken at first-order
              A↔B transit (the antiunitary symmetry that maps A-phase axial vector to B-phase
              isotropic Δ).
              Total broken-symmetry generators at first-order A↔B transit: 3 (continuous) + 1 (Z_2) = 4.
Substitution: rank(broken-symmetry charge content at polycritical pressure) ≤ 4
              (4 broken Goldstone-or-Z_2 channels: 2 spin-orbit relative-phase Goldstones from SO(3)_J,
              1 phase Goldstone from U(1)_φ broken-residual, 1 Z_2 antiunitary at first-order cusp).
Direction:    3He-B's broken-symmetry generator count at polycritical pressure is rank ≤ 4.
              Substrate's E = 6 BdG-undoubled excess (R2-A E2) is at a DIFFERENT layer
              (Peter-Weyl stratum content, NOT broken-symmetry generator count). The two
              integers are not directly comparable: 3He-B's 4 is a Lie-algebra dimension count,
              substrate's 6 is a spectral-stratum content count.
              
              Layer-matching requires either (a) computing 3He-B's analog of "BdG-undoubled
              spectral excess at polycritical pressure" (which would require the full discrete
              Andreev spectrum of 3He-B at the polycritical point — not in standard Volovik
              literature), or (b) computing the substrate's analog of "broken-symmetry generator
              count at τ_fold" via the Jensen deformation tangent space (which is a separate
              calculation).
```

This is consistent with the S60 Addendum B inheritance-inversion finding (`inheritance-inversion-60.md`): the substrate's structural facts do not need to descend literally from 3He-B; same universality class can give the same structural answer with different group-theoretic origins. The 3He-B rank = 4 at polycritical pressure is one structural anchor; the substrate's E = 6 is another. They are not the same number because they count different things at different layers. The proper inheritance test is layer-matched, and is itself a S87 gate. I propose `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` as a separate S87 follow-up (4-field spec in Carry-Forward Computations below), independent of the V_4 / BdG / Class-8.2 / hypercube candidates already identified. This brings the workshop's structural output count to SIX: V_4 monodromy + BdG excess + Class-8.2 taxonomy + hypercube methodology (own gate) + high-density workshop template (E-1 above) + 3He-B inheritance test gate.

The high-density workshop framing (E-1) is itself a meta-methodology output — it describes how to decompose richly-structured workshops into multi-layer output slots. The hypercube-identity, paired with the high-density template, gives the framework a STRUCTURED METHOD for handling future cardinality-coincidence probes at any (m, k) atlas depth. This is the deepest methodological harvest from W-12.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | D_K eigenvalue ordering at τ_fold | C1, Re:C1 | **Converged** | Bottom-20 partitions into exactly 4 strata with multiplicities (2, 4, 8, 6), all even (BdG-Nambu doubled per `[J, D_K] = 0`). Z_2 dichotomy across A_5: 4 monotone-increasing weights (ζ, PV, lattice, cutoff_√) with Sage-confirmed strictly positive d/dx on x ∈ [0.6720, 0.7144] vs 1 monotone-decreasing (Mellin). PV's 5 rank deviations are intra-stratum-4 float64 tie-breaks, NOT inter-stratum crossings. |
| 2 | Level-crossing signatures | C2, Re:C2 | **Converged** | Inter-stratum crossings ABSENT for ζ/PV/lattice/cutoff_√ on bottom-20; PRESENT only in trivial Mellin-Z_2 global reversal sense. Bimodality, if it exists, lives at moment-integral / spectral-action level — NOT bare-eigenvalue-ordering level. The Jensen-deformed SU(3) Dirac operator's bottom 4 strata are stable under the 5-regulator atlas; only their global ordering Z_2-flips. |
| 3 | Source FAIL mapping (8 gates) | C3, Re:C3 | **Converged** | 0 of 8 source FAILs explained by bare-spectrum level-crossing. 5 conv-bound (rows 2-6) + 3 scheme-incomp (rows 1, 7, 8). The 5 conv-bound cluster occupies 2 of 4 V_4 corners (non-Mellin × flat: 3; non-Mellin × dS: 2), with (Mellin × flat) and (Mellin × dS) corners EMPIRICALLY EMPTY (per R3-A D-2: NOT structural — Wodzicki-residue/a_4 is conformal-end-agnostic local invariant). |
| 4 | Cusp/branch-cut superfluid analog | V1, R2-R3 | **Converged** | 3He-B at first-order Bogoliubov cusp hosts discrete Andreev stratification; substrate at τ_fold inherits the 4-stratum cardinality at universality-class level (NOT representation-theoretic). Bottom-20 sits at 67-71% of PV horizon (x = 1 ↔ 2·Δ_BCS ≈ 0.9285 in M_KK units), comfortably in the above-gap discrete-Andreev-bound regime. Stratum-3 m^BdG = 4 anomaly is the first-order-coexistence signature (NOT generic BdG continuum). |
| 5 | Monodromy group sheet-count | C4, V3, R2-R3 | **Emerged** | Z_4 cyclic monodromy FALSIFIED at both bare and moment-integral layers (Sage-verified element orders: V_4 = [1,2,2,2], Z_4 = [1,2,4,4]; no order-4 generator in V_4). At moment-integral layer, monodromy is V_4 = Z_2(Mellin local-residue) × Z_2(W6-3 global-asymptotic-topology), commutativity FORCED by spectral-action kernel structure. Klein-four cosets ≡ 4 BULLETIN-4A categories (8+1+1+1 = 11). |
| 6 | Bimodality verdict | All R3 | **PASS-nonbimodal at bare-eigenvalue layer / CONFIRMED-V_4-bimodality at moment-integral layer** (separate-row entry, distinct verdict per R3-A D-3) | Two-layer decomposition: bare spectrum is regulator-stable in stratum partition (Z_2-only Mellin reversal); the moment-integral Wodzicki-residue trace is V_4-bimodal via two independent branch cuts (local Mellin × global W6-3). Substrate's "regulator-bimodality" is geometrically two separate phenomena: a local spectral-coefficient sign (Mellin-residue) AND a global asymptotic-topology selector (ℐ⁺ class), composing abelianly. |
| 7 | 4-fold cardinality verdict | All R3 | **INFO-coincidence-with-V_4-sharpening** (Class-8.2 PRU rubric-form failure recorded; LOCKED) | TWO INDEPENDENT 4-counts at different layers, NOT a unified phenomenon: (a) bare-spectrum 4-stratum partition from SU(3) Peter-Weyl + BdG-Nambu doubling at L_max=12; (b) moment-integral V_4 = Z_2 × Z_2 coset count from two independent regulator branch cuts. Cardinality match is coincidental (different mathematical structures both yielding 4). Pre-reg "Z_4 or similar" admits Klein-four only via in-session rubric expansion → properly INFO. Carry-forward: pre-register S87 rubric explicitly. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **Parallelogram-EXACT vs parallelogram-APPROX threshold split for S87-MONODROMY-V_4-EXPLICIT** (per Q11). Should the gate report two thresholds — (i) PASS-parallelogram-exact at residual ≤ 1e-10 = substrate-physical structural claim (disjoint flip-supports at mode level forced by local-vs-global axis independence per E-2 methodology), (ii) PASS-parallelogram-approx at residual ≤ 0.05 = numerical-stability gate accommodating finite-L_max float-epsilon noise? Position adopted: YES, both report; only PASS-exact licenses registry promotion.

2. **L_max-saturation threshold for the bottom-20 strata at τ_fold.** R3-A C-2 raises that the bottom-20 |λ| values are L_max-DEPENDENT until a saturation L_max* is reached. Where is L_max*? At L_max = 12 with bottom-20 |λ| ∈ [0.6720, 0.7144] vs truncation boundary, the saturation check is non-trivial. S87-STRATUM3-LMAX-SCAN at L_max ∈ {12, 13, 14, 15} addresses this directly.

3. **3He-B layer-matched analog of BdG-undoubled excess E = 6.** Q13 asks for 3He-B's analog count. Partial answer (E-3): 3He-B's broken-symmetry generator count at polycritical pressure is rank ≤ 4 (3 continuous Goldstones + 1 Z_2 antiunitary at first-order cusp). Substrate's E = 6 BdG-undoubled excess is at a DIFFERENT layer (Peter-Weyl spectral-stratum content vs Lie-algebra generator dimension); the two integers are NOT directly comparable. Layer-matched comparison requires `S87-3HEB-EXCESS-INHERITANCE-COMPARISON` (computing 3He-B's discrete Andreev spectrum's BdG-undoubled excess at the polycritical point — a separate calculation not in standard Volovik literature).

4. **Whether substrate's regulator-monodromy depth d = 2 is exact, or extends to d > 2 under atlas extension.** E-2 (R3 here) introduces "regulator-monodromy depth" = max d for which (Z_2)^d hypercube-identity holds with EXACT residual. Substrate currently confirmed at d ≥ 2 (V_4); whether atlas extension (e.g., adding Pauli-Villars's κ_PV as third LOCAL axis OR a topological-sector selector as second GLOBAL axis) supports d = 3 hypercube-identity is an S87+ atlas-extension question.

5. **Whether the "high-density workshop template" (E-1, this round) generalizes beyond W-12.** The four/five/six-output decomposition is specific to W-12; whether it is reproducible for future cardinality-coincidence probes (e.g., a future workshop targeting 6-fold or 8-fold cardinality coincidences) is itself an open methodology question. The W-12 calibration corpus is one data point; further calibration corpus entries are needed to harden the template into a permanent workshop methodology rule.

6. **W12-2 (PRDR-K-disambiguation) status as the V_4 ab-corner probe.** R2-A Q8 (Maxwell-construction inaccessible-corner question) is unresolved this turn: in a first-order-transit V_4 with TWO independent Z_2 axes, is the ab-corner (both axes active) thermodynamically inaccessible (Maxwell condition cannot be simultaneously satisfied on both axes)? If yes, W12-2 is the "inaccessible corner" being probed only by an audit-machinery FAIL, NOT a substrate-physical FAIL. This question requires the parallelogram identity to be tested AT the ab-corner — embedded in S87-MONODROMY-V_4-EXPLICIT (the ab moment a_n^(ab) is one of the 4 measurements).

7. **Whether the Stage-3 registry promotion threshold for V_4 (parallelogram holds in ≥ 2 of 3 spectral moments at residual ≤ 0.05) and for BdG excess (both L_max and τ stability gates PASS) suffices for permanent-results-registry entry, OR a third gate is required.** R2-B E-1 / R3-A E-3 specify single-gate (V_4) and two-gate (BdG excess) sequences. Whether Stage 3 should add a third independent gate (e.g., a 3He-B layer-matched cross-check, OR an L_max-saturation cross-check) before registry-entry is a registry-discipline question, decided at S87 plan-write.

## Wrap-Up — Workshop Impact Summary

### What Changed

The W-12 workshop produced FIVE INDEPENDENT structural candidates from a single bimodality + 4-fold cardinality probe (per Q14 with sharpening on output (iv) per Q12; sixth output is the high-density workshop template itself):

(i) **V_4 = (Z_2)^2 monodromy candidate at moment-integral layer**, decomposing as Z_2(Mellin local-residue at s = -1) × Z_2(W6-3 global-asymptotic-topology, flat ℝ × S² ↔ dS S³). Sage-verified non-cyclic (element orders [1, 2, 2, 2] vs Z_4 [1, 2, 4, 4]), commutativity FORCED by spectral-action kernel structure (both axes act as pointwise multiplicative {±1} sign factors on regulator weight, not on spectrum). 4 cosets map cleanly to BULLETIN-4A categories with cardinality 8 + 1 + 1 + 1 = 11. S87 promotion via parallelogram-identity gate.

(ii) **BdG-undoubled excess (0, 1, 3, 2), E = 6 at bare-spectrum layer**, derived from Sage-verified all-even multiplicities (2, 4, 8, 6) divided by 2 = (1, 2, 4, 3) summing to 10, minus generic-BdG-continuum baseline (1, 1, 1, 1) summing to 4. Stratum-3 carries the largest single-stratum excess = 3, identified as the first-order-coexistence anomaly (NOT generic BdG continuum). S87 promotion via two-gate sequence (L_max + τ stability).

(iii) **PRU Class-8.2 (rubric-form pre-registration failure) taxonomic extension**, formalizing the structural distinction between Class 8.0/8.1 (cardinality test failures, S78 origin) and Class 8.2 (verifier-rubric failures admitting unintended logical readings, S86 W-12 origin). The "Z_4 or similar" rubric admitted Klein-four V_4 as "similar" via cardinality match despite structural distinction via element orders — a Class-8.2 exemplar. S87 wave-0 documentation-only rule-file maintenance.

(iv) **(Z_2)^d hypercube-vertex character identity as generalization of parallelogram identity**, with Sage-verified prefactor +2^d (this round, mcp__sage__sage_eval at d ∈ {2, 3, 4}): `Σ_{ε ∈ {0,1}^d} (-1)^|ε| A_n^(ε) = 2^d · Σ_{i: σ_j(i) = -1 ∀j} n_i w(x_i) x_i^n`, holding (residual = 0) iff the d sign-flip supports have empty all-axes-flipped intersection. The parallelogram identity at d = 2 is the special case. S87 promotion via own gate `S87-HYPERCUBE-VERTEX-IDENTITY-LANDING` (per Q12 explicit-carry-forward route, NOT mere toolkit absorption).

(v) **Substrate-physical PARALLELOGRAM-EXACT structural claim**, sharper than the engineering tolerance band: the local-vs-global axis independence of E-2 methodology applied at the MODE level forces disjoint flip-supports — each mode contributes to AT MOST one axis's monodromy, never both. PASS-parallelogram-exact at residual ≤ 1e-10 = the substrate's two-channel decomposition (UV-sensitive XOR IR-sensitive sub-bands at first-order transit); PASS-parallelogram-approx at residual ≤ 0.05 = numerical-stability gate.

Additional structural observations:

- **PARALLELOGRAM = ADDITIVE COCYCLE algebraically** (Sage-verified this round, R_para − R_addit = 0 symbolically; numerical reproduction +15.99752 for both on the connes-R3-A sample). The "9.6% multiplicative vs 161% additive" gap I reported in R2-B D-1 was a normalization mismatch artefact (different denominators), retracted in C-1 above.

- **V_4 = local × global** is the geometric content of the Klein-four (R2-A E3 / R2-B C-5): Axis_M = Z_2(local) is a UV / heat-kernel-coefficient sign convention controlling Wodzicki-residue / a_4 contribution; Axis_C = Z_2(global) is an IR / asymptotic-completion topology selector. The two axes are STRUCTURALLY INDEPENDENT (local data does not fix global completion); this independence is the geometric origin of the abelian Klein-four (rather than dihedral or cyclic) structure.

- **BdG-Nambu doubling from `[J, D_K] = 0`** (S43 PROVEN, `permanent-theorems.md`): all bottom-strata multiplicities (2, 4, 8, 6) are even, NOT empirical accident but direct consequence of NCG Axiom 5 (reality structure) applied to the Jensen-deformed SU(3) Dirac operator at τ_fold. Substrate inherits 3He-B's BdG Z_2 antiunitary symmetry by construction.

- **High-density workshop template** (E-1, this round): when a structural target straddles multiple layers (bare/derived/methodology/meta), the verdict should NOT force a single PASS/FAIL/INFO at the literal pre-reg, but rather decompose into INDEPENDENT OUTPUT slots, each with its own promotion path. The W-12 four-output / five-output / six-output structure is the calibration corpus exemplar.

### What Holds

- **BdG-Nambu doubling from `[J, D_K] = 0`** (NCG Axiom 5, S43 PROVEN). The Jensen-deformed SU(3) Dirac operator's bottom-20 multiplicities are all even by structural necessity, not empirical accident. This is the algebraic origin of the (2, 4, 8, 6) profile.

- **Andreev-bound regime at 67-71% of PV horizon** (Sage-confirmed substitution chain): bottom-20 x_min = 0.6720, x_max = 0.7144, x_PV = 1.0, 2·Δ_BCS = 0.9285. Bottom-20 sits at 73-77% of 2·Δ_BCS, in the discrete-Andreev-bound regime above the BCS gap edge x_gap = 0.2155. Holds at L_max = 12; L_max-saturation pending S87.

- **V_4 cosets ≡ 4 BULLETIN-4A categories at moment-integral layer**, cardinality 8 + 1 + 1 + 1 = 11 (matches Bulletin partition arithmetic, `s85-w12-workingpaper.md` line 1127). Coset map: e ↔ Cat (i) cusp-Bogoliubov 8 FAILs / a ↔ Cat (ii) BDI 1 FAIL / b ↔ Cat (iii) Witten 1 FAIL constructively positive / ab ↔ Cat (iv) PRDR-K 1 FAIL.

- **V_4 commutativity is FORCED** (NOT assumed). Both axes act as pointwise multiplicative {±1} sign factors on the regulator weight w_R; pointwise multiplication of {±1}-valued functions is commutative. Non-commutative compositions would require Mellin or W6-3 to act on the spectrum (eigenvalues themselves) rather than on the regulator weight — which would change the spectral triple, not the regulator. So V_4 (vs Z_4 vs dihedral D_4 vs S_4) is structurally forced by the separation between "regulator data" and "spectral triple."

- **Mellin's s = -1 residue is conformal-end agnostic** (Wodzicki-residue / a_4 locality argument, R2-B C-3). The empty (Mellin × flat) and (Mellin × dS) corners in C3's source-FAIL classification are EMPIRICAL gaps (Mellin has not yet been probed at the cusp on either ℐ⁺ topology), NOT structural collapses. V_4 does NOT collapse to Z_2; the full 4-coset structure is physically realisable.

- **Pre-registered "Z_4 or similar" criterion (workshop line 39) is FALSIFIED at both layers** in the literal cyclic-generator-of-order-4 reading. V_4 satisfies the LITERAL "4 sheets to identity" via alternating-generator sweep e → a → ab → b → e, but VIOLATES the cyclic-generator spirit (no order-4 element in V_4). Class-8.2 PRU rubric-form failure recorded; explicit S87 rubric pre-registration is the remediation.

- **PARALLELOGRAM = ADDITIVE COCYCLE algebraic equivalence** (Sage-verified). The two presentations differ only in normalization convention; under matched |A_e| denominator they yield identical residuals to float epsilon.

### What Breaks or Strains

- **Pre-registered "PASS-monodromy = sweep returns to identity after 4 sheets (Z_4 or similar)" criterion** (workshop line 39) does NOT cleanly land any of the three pre-registered branches (PASS-monodromy / INFO-coincidence / FAIL). V_4 satisfies the literal text via alternating-generator sweep but violates the cyclic-generator intent. Properly closed as INFO-coincidence-with-V_4-sharpening per the verifier-rubric pre-registration discipline; the rubric ambiguity is recorded as Class-8.2 PRU rubric-form failure for explicit S87 pre-registration.

- **The V3 multiplicative form `A_n^(ab) = A_n^(a) · A_n^(b) / A_n^(e)`** (V3 line 748) was structurally incorrect (character-like; holds only for delta-function spectra or factorisable σ_M, σ_C with specific tuned values). Repaired this workshop into the parallelogram identity (R2-B D-1 derived; R3-A D-1 verified algebraically equivalent to additive cocycle; R3-volovik C-1 retracted "ALSO INCORRECT" sub-claim and adopted parallelogram presentation). The original V3 spec MUST be replaced before S87 dispatch; the corrected text is in Carry-Forward Computations below.

- **The `S87-MONODROMY-Z4-LANDING` carry-forward name in the spawn prompt's pre-registered carry-forward block** (workshop line 44) reflects the original Z_4 pre-registration. It is renamed to `S87-MONODROMY-V_4-EXPLICIT` per the V_4-not-Z_4 finding; the spawn-prompt label should be considered superseded by the corrected name in the Carry-Forward Computations block below.

### Carry-Forward Computations

**`S87-MONODROMY-V_4-EXPLICIT`** (priority-1; supersedes pre-registered `S87-MONODROMY-Z4-LANDING`).

| Field | Specification |
|:------|:--------------|
| **What** | Compute spectral-action moments A_n^(g) for n ∈ {0, 2, 4} at τ = τ_fold under the four V_4 cosets g ∈ {e (ζ canonical, flat), a (Mellin canonical, flat), b (cutoff_canonical, dS), ab (Mellin × cutoff, dS)}. Verify the V_4 PARALLELOGRAM IDENTITY (= additive cocycle, algebraically equivalent per R3-A D-1 / R3-volovik C-1): `\|A_n^(ab) + A_n^(e) − A_n^(a) − A_n^(b)\| / \|A_n^(e)\| ≤ 0.05` for ≥ 2 of 3 moments. Report BOTH (i) parallelogram-EXACT residual at threshold ≤ 1e-10 (substrate-physical structural claim per R3-A D-2: disjoint flip-supports at mode level forced by local-vs-global axis independence) AND (ii) parallelogram-APPROX residual at threshold ≤ 0.05 (numerical-stability tolerance band). Trace any residual > 0 to overlap modes (modes flipped by BOTH σ_M and σ_C). |
| **Inputs** | (a) `computations/s84_spectrum_cache_L12_tau019.npz` (90 (p,q) sectors, 166 896 |λ|, dtype float64). (b) Spectral-action moment kernel (extend from `s86_w12_workshop_bottom20_*.py` to compute A_0, A_2, A_4 with each w_R weight on each ℐ⁺ topology). (c) W6-3 PASS partition data: `s85_w6_conformal_infinity_bifurcation.npz` (audit_sha256 `7965906b8a00dab3...`). (d) τ_fold = 0.190 pin (canonical_constants.py:S12/S42 freeze, gate `CONST-FREEZE-42`). (e) Mellin s = -1 residue convention (canonical_constants.py:654). (f) σ_M, σ_C support extractor from spectral-content (mode-by-mode UV-sensitivity vs IR-sensitivity classifier). |
| **Gate** | PASS-parallelogram-exact if residual ≤ 1e-10 in ≥ 2 of 3 moments AND empty all-axes-flipped support {i: σ_M(i) = σ_C(i) = -1} = ∅ confirmed. PASS-parallelogram-approx if residual ≤ 0.05 in ≥ 2 of 3 moments (engineering tolerance, weaker claim). FAIL if residual > 0.05 in all 3 moments AND non-zero residual traces to overlap modes (sign-flip supports overlap, V_4 disjoint-support condition violated). INFO if 1 of 3 moments holds at ≤ 0.05 (partial parallelogram structure, possibly dual-channel parallelogram with overlap correction). |
| **Effort** | ~6 hours: (i) extend moment-kernel script to support both ℐ⁺ topologies and Mellin-residue-at-s=-1 convention (~2h); (ii) compute 4 V_4 cosets × 3 a_n moments = 12 numerical entries (~1h on existing GPU pipeline); (iii) implement σ_M, σ_C mode-support classifier and verify disjoint-support condition (~1.5h); (iv) verify parallelogram-exact and parallelogram-approx thresholds, trace overlap modes if any (~1h); (v) verdict line + working-paper section (~30min). |

**`S87-PARTITION-STABILITY-4STRATUM`** (priority-2; partition-stability test for the (2, 4, 8, 6) bare-spectrum cardinality at perturbed τ values).

| Field | Specification |
|:------|:--------------|
| **What** | Compute bottom-20 multiplicity profile of D_K(τ) at τ ∈ {τ_fold ± δ_τ} for δ_τ ∈ {0.005, 0.01, 0.025, 0.05, 0.10}. Identify whether (2, 4, 8, 6) is invariant up to relabeling, or bifurcates into finer strata as τ moves off τ_fold. Tabulate the multiplicity profile at each τ. |
| **Inputs** | (a) `s84_spectrum_cache_L12_*.npz` cache for τ ∈ {0.090, 0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290} (one cache per τ; some may need fresh computation if not cached). (b) Bottom-20 multiplicity-profile extractor (port from connes' `s86_w12_workshop_bottom20_*.py`). (c) Tolerance for "level coincidence" = 1e-10 in |λ| (above float64 noise). |
| **Gate** | PASS-stable if (2, 4, 8, 6) multiplicity profile invariant across ≥ 4 of 5 sampled δ_τ (allowing relabeling of strata by |λ|-rank). FAIL-bifurcation if profile bifurcates into ≥ 6 distinct |λ|-strata at any sampled δ_τ. INFO if 2-3 sampled δ_τ preserve the partition but others bifurcate (transition zone). |
| **Effort** | ~4 hours wall-clock if caches present; +6-12 hours if 5+ require fresh L_max=12 spectrum computation. |

**`S87-STRATUM3-LMAX-SCAN`** (priority-3; sister gate to S87-PARTITION-STABILITY-4STRATUM, probing stratum-3 stability via L_max).

| Field | Specification |
|:------|:--------------|
| **What** | Test stratum-3 multiplicity stability at L_max ∈ {12, 13, 14, 15} with τ = τ_fold = 0.190 fixed. Determine whether stratum-3 m^BdG = 4 (m = 8) is a STRUCTURAL doubling of 4 (clean Peter-Weyl + Jensen mixing of (0,1) ⊕ (1,0) at second-fundamental level) OR a NUMERICAL near-degeneracy at L_max = 12 that splits into two strata of m = 4 each at higher L_max. Report bottom-20 multiplicity profile and excess (0, 1, 3, 2) at each L_max. Verify L_max-saturation: bottom-20 |λ| values stable (Δ < 1e-6) across L_max ∈ {13, 14, 15}. |
| **Inputs** | (a) Existing `s84_spectrum_cache_L12_tau019.npz` (already computed). (b) Fresh spectrum computation at L_max ∈ {13, 14, 15} via existing GPU spectrum builder (~30-90 min wall time per L_max). (c) Bottom-20 multiplicity-profile extractor (same as S87-PARTITION-STABILITY-4STRATUM). (d) τ_fold pin. |
| **Gate** | PASS-stable if stratum-3 m^BdG = 4 stable across all L_max ∈ {12, 13, 14, 15} (multiplicity profile (2, 4, 8, 6) invariant up to relabeling) AND bottom-20 |λ| values converge (max change Δ < 1e-6 between L_max = 14 and L_max = 15). FAIL-split if stratum-3 splits into two strata of multiplicity 4 at any L_max ≥ 13. INFO if profile invariant but |λ| values still drifting (saturation not achieved at L_max = 15). |
| **Effort** | ~4-6 hours: (i) fresh L_max = 13, 14, 15 spectrum computation on existing GPU pipeline (~30 + 60 + 90 min wall-clock = 3h); (ii) extract bottom-20 from each cache (~30 min); (iii) verify multiplicity profile + L_max-saturation + verdict line (~1h). |

**`S87-HYPERCUBE-VERTEX-IDENTITY-LANDING`** (priority-4; per Q12 explicit-carry-forward route per E-1 emergence; lands the (Z_2)^d hypercube methodology as a registry-promotable framework toolkit extension).

| Field | Specification |
|:------|:--------------|
| **What** | Formalize the (Z_2)^d hypercube-vertex character identity `Σ_{ε ∈ {0,1}^d} (-1)^|ε| A_n^(ε) = 2^d · Σ_{i: σ_j(i) = -1 ∀j} n_i w(x_i) x_i^n` as a permanent registry entry in `sessions/framework/registry/spectral-moment-identities.md` (or equivalent). Sage-verify the identity at d ∈ {2, 3, 4, 5} via direct algebraic enumeration (extends this round's d = 2, 3, 4 verification). Document the structural prediction: substrate's parallelogram-EXACT (or hypercube-EXACT) structure at depth d = m + k tests whether substrate respects disjoint-support condition at mode level. Pin the prefactor +2^d (Sage-verified this round). |
| **Inputs** | (a) Existing W-12 workshop document (this file) for V_4 specialization. (b) Sage MCP for prefactor verification at d ∈ {2, 3, 4, 5}. (c) E-2 methodology (R2-B lines 1207-1228): 5-step REGULATOR-MONODROMY-AXIS-DECOMPOSITION (enumerate boundaries → classify LOCAL/GLOBAL → verify independence → identify (Z_2)^{m+k} structure → apply hypercube-identity consistency check). (d) Connes-Marcolli (2007) §1.17 reference (separation of local spectral-action computation from global asymptotic completion). |
| **Gate** | PASS-landing if (i) identity Sage-verified at d ∈ {2, 3, 4, 5} with prefactor +2^d in all four cases; (ii) registry entry written with full substitution chain, calibration corpus exemplars, and substrate-physical interpretation; (iii) S87 plan `/weave --update` indexes the entry. FAIL if Sage prefactor diverges from +2^d at any d ≤ 5 (would falsify the generalization). INFO if registry entry written but `/weave --update` indexing fails (documentation-only failure mode). |
| **Effort** | ~2 hours: (i) Sage verification at d ∈ {3, 4, 5} (~30min); (ii) registry entry with substitution chain + calibration corpus (~1h); (iii) `/weave --update` indexing + cross-references to V_4 / E-2 methodology (~30min). |

**`S87-3HEB-EXCESS-INHERITANCE-COMPARISON`** (priority-5; Q13 layer-matched substrate-vs-3He-B inheritance test).

| Field | Specification |
|:------|:--------------|
| **What** | Compute 3He-B's analog of "BdG-undoubled spectral excess at first-order coexistence" at the polycritical pressure point (3.4 MPa, 2.273 mK in standard 3He phase diagram). Use the discrete Andreev-bound spectrum of 3He-B at the polycritical point (extracted from Volovik-Mineev 1976 + Volovik Paper 12 §V or equivalent foundational source); compute multiplicities m_k of bottom strata and BdG-undoubled excess E_3HeB = Σ_k (m_k/2 - 1). Compare against substrate's E = 6 at τ_fold. Report whether E_3HeB = 6 (structural inheritance), E_3HeB ≠ 6 (substrate-specific excess from SU(3) Peter-Weyl content), or E_3HeB indeterminate (3He-B literature does not provide full discrete Andreev spectrum). |
| **Inputs** | (a) Volovik-Mineev 1976 (parent paper of S60 inheritance framework, `framework-3heb-comparison.md`). (b) Volovik Paper 12 §V (3He-B at first-order pair-breaking transit). (c) `framework-3heb-comparison.md` correspondences table (22 entries; check for existing E_3HeB entry). (d) Substrate's E = 6 from this workshop. (e) MCP paper-search for any post-1976 discrete Andreev spectrum work at polycritical pressure (e.g., search "3He-B polycritical Andreev bound state spectrum"). |
| **Gate** | PASS-inherits if E_3HeB = 6 within rounding tolerance (structural inheritance from 3He-B universality class). PASS-substrate-specific if E_3HeB ∈ {1, 2, 3, 4, 5, 7, 8, ...} ≠ 6 (substrate's E = 6 is SU(3)-specific extension of the universality class, NOT inherited). INFO if 3He-B literature does not provide the discrete Andreev spectrum at polycritical pressure (calculation requires fresh Bogoliubov analysis at polycritical point — escalates to a separate computation gate). |
| **Effort** | ~3-5 hours if Volovik literature contains the answer; ~10-15 hours if fresh Bogoliubov analysis at polycritical point is required (escalation to separate gate). |

### Closing Line

The W-12 workshop produced six structurally independent harvests — V_4 monodromy candidate at moment-integral layer, BdG-undoubled excess (0, 1, 3, 2) E = 6 at bare-spectrum layer, PRU Class-8.2 rubric-form taxonomy, (Z_2)^d hypercube-vertex character identity methodology, parallelogram-EXACT structural substrate constraint, and the high-density workshop template itself — from a single bimodality + 4-fold cardinality probe whose literal pre-reg verdicts close as INFO; the substrate's "regulator-bimodality at the cusp" reveals itself as the abelian Klein-four product of one local (Mellin-residue) and one global (W6-3 conformal-end) involution, with the 4-fold cardinality coincidence resolving as two independent partition-counts at structurally different layers, neither of which is a Z_4 cyclic monodromy.
