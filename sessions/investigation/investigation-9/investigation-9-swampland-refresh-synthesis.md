# Investigation 9 Synthesis: Modern Swampland Refresh (2018–2025) — INV9-W2-3

**Date**: 2026-06-16
**Agent**: string-theory-theorist (cross-framework specialist — string/M-theory walls, dualities, swampland, holography, K-theory)
**Gate**: INV9-W2-3-MODERN-SWAMPLAND-REFRESH (review; closes by artifact-existence-with-content — NO verdict line)
**Source Documents**:
- `sessions/investigation/investigation-1/string-theory-theorist.md` §R-3 / §B-5 / §C-2 (seed survey)
- `.claude/agent-memory/string-theory-theorist/cross-framework-comparisons.md` §"Swampland status" (the pre-2018 audit, 38 closures, all CONSISTENT)
- `computations/_shared/canonical_constants.py` (anchors, verified via knowledge MCP)
- `sessions/framework/Atlas/atlas-08-open-questions.md` (CF14 "Swampland c(tau)", D-6, opened S47)
- **FETCHED (primary, full-text)**: OPSV-2018 (arXiv:1810.05506v2); OOSV-2018 (arXiv:1806.08362v3); LLW-2019 (arXiv:1910.01135v2); Dvali-Redi 2007 (arXiv:0710.4344v1). Local copies: `downloads/swampland-refresh/`.

---

## 0. Framing law (load-bearing — read before the verdicts)

This is a **substrate-first** audit per `phononic-framing.md`. **Swampland conjectures are WALL-MEASUREMENTS of the substrate** (`cross-framework-comparisons.md`: string theory = WALLS / boundary conditions; the phonon-exflation substrate = INTERIOR). A `CONSISTENT` tag here is an **internal-consistency confirmation, NOT a prediction of the framework** — it confirms the substrate respects a string-side boundary condition; it does not derive new framework physics. This is my standing methodology rule (`cross-framework-comparisons.md §"Methodology rules"`): *all swampland conjectures are wall-measurements, not external tests; their PASS does not "predict" the framework, it confirms internal consistency.* Probability/confidence weighting is the Skeptic's domain, not mine; I render only structural CONSISTENT / TENSION / classified tags + the deciding substrate quantity.

Every cited substrate quantity is σ(D_K)-derived, and the swampland conjecture is the wall it is measured against — the substrate is never embedded IN a string moduli space.

**PROVENANCE FLAG (load-bearing, per `substrate-first-canonical-sourcing.md`)**: `Δφ/M_Pl = 0.170` is a **SEED-AUTHOR survey value** (`cross-framework-comparisons.md §"Swampland status"`), **NOT a substrate-first `canonical_constants.py` pin**. The numerically-closest canonical is `delta_tau_crit_pos = 0.175` (S88-W2-9-VII-AE, the positive-side stratum-coalescence critical τ-displacement) — but that is a **different observable** (a moduli-deformation critical point, not a field excursion). I cite `0.170` as the survey value and flag the distinction; I do NOT promote either to the other. The 3% numerical adjacency is a coincidence of two distinct axes, not an identity.

**Canonical anchors used (verified via knowledge MCP `get_constant`, 2026-06-16)**:
| Anchor | Value | Source |
|:-------|:------|:-------|
| `w0_FW` | −0.918 | S58 four-fold-lock (Volovik vacuum partition + effacement Γ=0.99970) |
| `Lambda_sp_over_M_KK` | 2.06 | S96, gate S63-SPECIES-36/SCALE-63 (`s63_species_scale.npz`) |
| `M_Pl_reduced` | 2.435×10¹⁸ GeV | CODATA 2018 |
| `tau_fold` | 0.19 | S12/S42, CONST-FREEZE-42 |
| `delta_tau_crit_pos` | 0.175 | S88-W2-9-VII-AE (provenance-flag comparator only; NOT the survey Δφ) |
| `\|S'\|/S` | ≥ 0.23 at fold | survey (gradient lower bound at τ_fold) |
| gradient `c` | 3.52 (cutoff) / ~6.6 (zeta) | S69 W4-B PROVEN (`session-69-lizzi-collab.md`) |

---

## I. Session Outcome

The framework's pre-2018 swampland audit (38 closures, all CONSISTENT) **survives the 2018–2025 refresh with all four modern conjectures rendering CONSISTENT or cleanly classified — no new structural TENSION is created by the modern sharpenings; one new *named caveat* is surfaced** (the species-scale consistency check is a RATIO-vs-CUTOFF scale-type question, flagged below, not a falsifier). The sharpest fresh deliverable is the **Emergent-String dichotomy classification of the two infinite-distance τ-limits**: I classify **τ→0 (cold-big-bang unstable maximum) as a DECOMPACTIFICATION-type limit** and **large-τ as a candidate EMERGENT-STRING-type limit** (via the WORLDSHEET-BOUNDARY-62 Voronoi-boundary Nambu-Goto mode), but with the load-bearing caveat that **LLW-2019's dichotomy is a theorem about Calabi-Yau Kähler moduli space, and SU(3) is NOT Calabi-Yau** — so the framework's τ-line is classified *by structural analogy to* the dichotomy, not *as an instance of* the LLW classification theorem. The honest verdict on B-5 ("moduli space in the landscape, not the swampland") is **classified-by-analogy, with the substrate's 1-modulus τ-line admitting a clean two-limit reading that mirrors the dichotomy's shape but does not inherit its CY proof**.

Two of the four modern conjectures (refined dS, Dvali species scale) had their primary papers **fetched in full**; the other two (sharpened Distance, Emergent String) likewise fetched in full. **No conjecture is tagged `classified-from-survey-structure-pending-primary-fetch`** — all four primaries were retrieved.

---

## II. Key Results — Per-Conjecture Audit

### (1) Refined de Sitter Conjecture (OPSV-2018, arXiv:1810.05506) — **CONSISTENT**

**Result**: CONSISTENT. **Deciding substrate quantity**: the gradient bound `|S'|/S ≥ 0.23` at the fold (with `c = 3.52` cutoff / `~6.6` zeta from S69 W4-B PROVEN) AND the TRANSIT-279 tachyonic Hessian direction at the S(τ,φ) saddle. NON-PHONONIC (cross-framework audit); the deciding quantities are GEOMETRIC (σ(D_K) gradient + tachyonic inner fluctuations).

The refined conjecture (OPSV eq. 2–3) reads: a scalar potential of any consistent QG must satisfy EITHER
```
|∇V| ≥ (c/M_p)·V        (clause 2, the original OOSV-2018 bound)
```
OR
```
min(∇_i∇_j V) ≤ −(c'/M_p²)·V   (clause 3, the refined Hessian clause)
```
for `c, c' > 0` of order 1. OPSV derive this in any parametrically-controlled weak-coupling regime from the Distance Conjecture + Bousso's covariant entropy bound, and note it *"evades all counter-examples at scalar potential maxima that have been raised."*

**Framework status — CONSISTENT on BOTH clauses, which is over-determined:**

- **Clause (2) satisfied directly.** The framework has **no de Sitter minimum; all potentials are monotonic** (`cross-framework-comparisons.md §"Swampland status"`: "no dS minimum, all potentials monotonic"). The gradient lower bound `|S'|/S ≥ 0.23` holds at the fold, and the S69 W4-B PROVEN result gives `c = 3.52` (cutoff scheme) and `c ~ 6.6` (zeta scheme). Since the refined-dS bound requires only `c ~ O(1)`, the framework's gradients are **comfortably above threshold** — there is no fine-tuning pressure. SUBSTITUTION-CHAIN check (the only directional claim in this conjecture): `c_framework = 3.52 ≥ c_bound ~ O(1)` ⟹ clause (2) satisfied with margin. No mnemonic shortcut used; the W4-B PROVEN values are cited verbatim from the canonical (`session-69-lizzi-collab.md`).

- **Clause (3) ALSO satisfied — structurally, at the saddle.** This is the deeper match. OPSV's clause (3) is *derived* (their "HORIZON AND BOUSSO BOUND" section) from the requirement that zero-point fluctuations at the apparent-horizon crossing be **tachyonic** when the Hessian has a negative eigenvalue below `−c'/R²`. OPSV explicitly note their result *"is compatible with the observation that tachyons are ubiquitous in classical dS and quintessence solutions."* The framework's **2D landscape S(τ,φ) is a SADDLE at the fold: τ convex, φ tachyonic** (`cross-framework-comparisons.md §"Tachyonic instability"`; TRANSIT-279 = all 279 scalar inner fluctuations tachyonic at all τ, all cutoffs, `proven_1437`). The negative Hessian eigenvalue in the φ direction IS the `min(∇_i∇_j V) < 0` clause (3) realization.

**Convergent derivation note (genuine, sharp)**: OPSV invoke the **η-problem** (their ref [102], Copeland–Liddle–Lyth–Stewart–Wands 1994) as the mechanism guaranteeing clause (3) at F-term potential maxima — *"the η-problem implies that any maximum of an F-term based potential will generically satisfy (3). A violation would require some fine-tuned cancellations."* The framework's **N_e-saturation η-problem is a PROVEN exact structural analog** (`cross-framework-comparisons.md §"Eta problem"`, S52, IC-independent). So the framework and OPSV reach the same clause-(3) satisfaction *via the same η-problem mechanism*, not merely the same conclusion. This is a derivation-level rhyme.

CROSS-REF: **INV9-W1-2** is the live COMPUTE that re-produces the `|S'(τ)|/S(τ)` gradient-bound number at the fold; this review is the BROAD audit, W1-2 is its specific instance. The two are consistent (W4-B PROVEN c=3.52 is the cutoff-scheme anchor W1-2 refines).

### (2) Sharpened Distance Conjecture (OPSV-2018 §"Distance Conjecture") — **CONSISTENT**

**Result**: CONSISTENT. **Deciding substrate quantity**: the field excursion `Δφ/M_Pl = 0.170` [SURVEY VALUE — see provenance flag] (sub-Planckian by 5.9×) AND the presence of the KK tower at the species scale `Λ_sp/M_KK = 2.06`. NON-PHONONIC audit; deciding quantity is the σ(D_K) KK-tower spectrum.

The Distance Conjecture (Ooguri–Vafa 2007, OPSV's ref [52]): as `Δφ → ∞` in moduli space, a tower of states becomes light with `m ∼ e^{−a·Δφ}`, `a ~ O(1)`. The "sharpening" in the 2018–2025 literature is twofold: (i) the `a ~ O(1)` constant is pinned more tightly (OPSV cite the critical-Δφ onset studies, refs [56,57,59,62,63,66,82]), and (ii) the conjecture is generalized to non-trivial potentials `V(φ) ≠ 0` (OPSV: "A natural extension... for sufficiently far distances, we have towers of light particles whose masses go as `m ∼ e^{−a·Δφ}`").

**Framework status — CONSISTENT:**

- **The excursion is sub-Planckian.** `Δφ/M_Pl = 0.170` [SURVEY] — a factor 5.9× inside the Planck scale. The Distance Conjecture constrains the *infinite-distance* regime (`Δφ ≫ 1` in Planck units); a sub-Planckian excursion is **comfortably in the conjecture's "safe" interior** where no tower-induced EFT breakdown is mandated. The sharpened `a ~ O(1)` does NOT change this reading: at `Δφ/M_Pl = 0.170` the exponential `e^{−a·0.170}` is `O(1)` for any `a ~ O(1)` (≈ 0.84 for a=1), i.e. no tower has descended — consistent with the framework operating in a controlled, sub-Planckian field range.

- **The KK tower IS present** at the species scale `Λ_sp/M_KK = 2.06` (S96). The Distance Conjecture's *content* (a tower exists as you approach a boundary) is realized: the internal SU(3) carries a KK tower, and the species scale `2.06 M_KK` is exactly where it becomes relevant. So the framework is consistent with BOTH halves: sub-Planckian excursion (no forced breakdown) AND tower-present (the conjecture's structural prediction is realized at the right scale).

**PROVENANCE FLAG (re-stated, load-bearing)**: `0.170` is a SEED-AUTHOR survey value, NOT a `canonical_constants.py` pin. The closest canonical, `delta_tau_crit_pos = 0.175`, is a **moduli-deformation critical-τ displacement** (S88-W2-9), a structurally DIFFERENT observable from a field excursion. I do not promote `0.170` to canonical, nor do I substitute `0.175` for it; I render the CONSISTENT tag on the survey value and flag that a substrate-first re-computation of the *canonical* field excursion `Δφ/M_Pl` is a carry-forward (see §V).

### (3) Emergent String Conjecture (LLW-2019, arXiv:1910.01135) — **classified** (τ-limit dichotomy)

**Result**: classified (the dichotomy is rendered on BOTH τ-limits below). **Deciding substrate quantity**: the character of the leading tower in each infinite-distance τ-limit — KK-tower-dominated (decompactification) vs asymptotically-tensionless-string (emergent-string). GEOMETRIC (the τ-line is the substrate's 1-modulus Jensen deformation manifold).

The Emergent String Conjecture (LLW-2019), verbatim from the abstract (fetched, full-text-verified): *"a quantum gravitational theory in an infinite distance limit of its moduli space **either decompactifies, or reduces to an asymptotically tensionless, weakly coupled string theory.**"* The operational discriminator (LLW §1.1, verbatim): a KK tower scales as `M²_n/M²_Pl ~ n²·M²_KK/M²_Pl` (decompactification if it parametrically dominates), whereas an emergent string is *"much denser... with a level-mass relation given by `M²_n ~ n·M²_string`."* LLW prove the dichotomy is **exhaustive and the classes mutually exclusive** for CY3 Kähler moduli space (their Theorem 1: three fibration classes — genus-one T² → decompactification/F-theory; K3 surface → emergent heterotic string; Abelian surface T⁴ → emergent Type II string — *"mutually exclusive and hence well-defined,"* covering *"all possible situations compatible with finite volume limits at infinite distance."*).

**CRITICAL SCOPE CAVEAT (load-bearing, per my standing duality-frame rule)**: LLW-2019's dichotomy is a **theorem about Calabi-Yau three-fold Kähler moduli space**. **SU(3) is NOT Calabi-Yau** (positive Ricci, not Ricci-flat; `cross-framework-comparisons.md §"Mathematical apparatus distinction"`) and the framework has **1 modulus τ vs ~O(100) per CY3**. Therefore the framework's τ-line is classified **by structural analogy to the dichotomy's SHAPE**, NOT as an instance of the LLW classification theorem. I specify the duality frame explicitly: the classification below is an analogy at the level of "which kind of tower goes light," not a CY-fibration computation. This is the honest reading; forcing the framework into the LLW theorem would be a duality-frame violation.

**The framework's TWO infinite-distance τ-limits, classified:**

- **τ → 0 limit (cold-big-bang, unstable maximum): classified DECOMPACTIFICATION-type.**
  At `τ → 0` the Jensen deformation collapses toward the round/symmetric configuration — the `project_cold-big-bang-vacuum-floor` lore: τ=0 is an unstable MAXIMUM, the cascade-into-complexity origin (`project_emergent-not-shrinking`: SU(3) EMERGES from unity into complexity). In Distance-Conjecture terms, approaching τ→0 is approaching a boundary where the internal geometry **de-complexifies**: the eigenvalue spectrum reorganizes toward maximal symmetry, and the relevant light tower is the **KK tower of the (un-deformed) SU(3)** — a field-theoretic `n²·M²_KK` tower, NOT a denser `n·M²_string` tower. This matches the **decompactification branch** of the dichotomy: the limit is governed by a KK tower becoming light, structurally analogous to LLW's Type-T² (elliptic-fiber → KK tower → decompactification to F-theory). **Tag: τ→0 ↦ decompactification (KK-tower-dominated).**

- **large-τ limit: classified candidate EMERGENT-STRING-type (via WORLDSHEET-BOUNDARY-62).**
  At large τ the Jensen deformation drives the internal geometry into extreme anisotropy. The candidate light *string-like* tower is the **Voronoi-cell-boundary → 2D Nambu-Goto worldsheet** (WORLDSHEET-BOUNDARY-62, `cross-framework-comparisons.md §"S61 shadow thesis"`; the queued computation of critical dimension on the constrained Voronoi boundary, `c_eff = 8`?). IF the large-τ limit produces an asymptotically-tensionless Nambu-Goto mode from the Voronoi boundary (a `n·M²_string`-dense tower, the emergent-string fingerprint), the large-τ limit is the **emergent-string branch** of the dichotomy. This is the framework's analog of LLW's Type-K3/T⁴ (an M5-brane wrapping a shrinking fiber → asymptotically tensionless fundamental string). **Tag: large-τ ↦ emergent-string (candidate, conditional on WORLDSHEET-BOUNDARY-62 producing a tensionless Nambu-Goto tower with the `n·M²_string` density).**

**Dichotomy verdict (B-5)**: the framework's 1-modulus τ-line admits a **clean two-limit reading that mirrors the decompactification-vs-emergent-string dichotomy** — τ→0 decompactifies (KK tower), large-τ is a candidate emergent-string limit (Voronoi-boundary Nambu-Goto). A clean dichotomy classification is the swampland signature of *"in the landscape, not the swampland."* BUT the honest scope tag is **classified-by-analogy**: the dichotomy's SHAPE is reproduced, its CY-fibration PROOF is not inherited (SU(3) ≠ CY3). The large-τ emergent-string leg is **CONDITIONAL** on the WORLDSHEET-BOUNDARY-62 critical-dimension computation (queued, `c_eff = 8`?), which is the decisive falsifier of the emergent-string reading: if the Voronoi boundary does NOT support a consistent tensionless string (wrong critical dimension), large-τ defaults to a second decompactification-type or obstructed limit, and the dichotomy reading weakens.

### (4) Dvali Species Scale (Dvali-Redi 2007, arXiv:0710.4344) — **CONSISTENT** (with a named scale-type caveat)

**Result**: CONSISTENT, with a named caveat (the check is a RATIO-vs-CUTOFF scale-type question, not a clean N-counting identity). **Deciding substrate quantity**: the species count `N_shell` (eigenvalues in `[M_KK, 2.06 M_KK]`; cross-ref INV9-W2-2) plugged into the Dvali bound, vs `Λ_sp/M_KK = 2.06`. PHONONIC (the species count is the substrate's accessible vibrational-mode count below EFT breakdown).

The Dvali species bound (Dvali-Redi 2007, verbatim eq. 1.1–1.2): with N species of mass scale Λ, black-hole physics imposes
```
M²_P ≳ N·Λ²        (eq. 1.1, up to a log N factor)
⟺  Λ_G ≈ M_Planck/√N   (eq. 1.2, the effective gravitational cutoff)
```
Dvali derives this for the ADD large-extra-dimension case via `(Λ_G·R)^n = N` (eq. 4.2) — N is the number of **KK species** below the cutoff. This is the structurally-relevant case for the framework: the internal SU(3) carries a KK tower, and the species shell `[M_KK, 2.06 M_KK]` counts exactly those KK modes below EFT breakdown.

**Framework status — CONSISTENT, with the caveat made explicit:**

- The framework's species scale `Λ_sp/M_KK = 2.06` (S96, "THIN") was established (S36/S96) as the self-consistent EFT-breakdown shell. Dvali's bound says the cutoff `Λ_G` is *lowered* relative to `M_Pl` by `√N`. The framework's `2.06` is a **RATIO of the species cutoff to the KK scale** (`Λ_sp/M_KK`), whereas Dvali's `√N` relates the cutoff to the **Planck scale** (`Λ_G/M_Pl = 1/√N`). These are **two different ratios on two different scale axes** — the internal consistency check is whether the framework's `N_shell` (the species count, from INV9-W2-2) is *mutually consistent* with `2.06` via the Dvali counting, NOT whether `√N_shell = 2.06` directly (which would be a scale-type confusion).

- **The honest reading**: the Dvali bound and the framework's species scale are CONSISTENT in the sense that BOTH encode "the cutoff is set by the number of light species, and a THIN tower (few species below cutoff) means the cutoff sits just above M_KK." A thin shell `Λ_sp/M_KK = 2.06` is the signature of a *small* N (few modes in `[M_KK, 2.06 M_KK]`), and Dvali's `Λ_G ≈ M_Pl/√N` with small N gives a cutoff close to M_Pl — both consistent with a controlled, weakly-coupled regime. The framework does NOT have a large-N species-tower hierarchy problem (Dvali's `N ≈ 10³²` scenario); it has a THIN tower, which is the *benign* end of the Dvali spectrum.

**NAMED CAVEAT (the only new caveat surfaced by the refresh)**: the quantitative check "does `N_shell` reproduce `Λ_sp/M_KK = 2.06` via the Dvali formula" requires pinning **WHICH scale ratio** (`Λ_sp/M_KK` vs `Λ_G/M_Pl`) and is therefore a RATIO-vs-CUTOFF scale-type question. This is a **consistency-check carry-forward** (cross-ref INV9-W2-2's `N_shell`), NOT a falsifier and NOT a TENSION — the qualitative reading (thin tower ⟺ small N ⟺ benign Dvali regime) is unambiguously CONSISTENT; only the precise numerical identity needs the scale-type pinned. This is the species-scale analog of the `Λ`-scale-pinning caveat INV9-W2-2 already carries.

---

## III. Gate Verdicts

| Conjecture | Tag | Deciding substrate quantity | Primary fetched? |
|:-----------|:----|:----------------------------|:-----------------|
| (1) Refined de Sitter (OPSV-2018) | **CONSISTENT** | `\|S'\|/S ≥ 0.23`, c=3.52/6.6; TRANSIT-279 tachyonic Hessian at saddle (clause 3) | Yes (1810.05506v2, full) |
| (2) Sharpened Distance | **CONSISTENT** | `Δφ/M_Pl = 0.170` [SURVEY] sub-Planckian 5.9×; KK tower at `Λ_sp/M_KK=2.06` | Yes (1810.05506v2, full) |
| (3) Emergent String (LLW-2019) | **classified** | leading-tower character per τ-limit (KK vs tensionless-string) | Yes (1910.01135v2, full) |
| (4) Dvali species scale | **CONSISTENT** (+ named caveat) | `N_shell` vs `Λ_sp/M_KK=2.06`; RATIO-vs-CUTOFF scale-type | Yes (0710.4344v1, full) |

**Emergent-String dichotomy verdict (the two τ-limits)**:
- **τ→0 ↦ decompactification** (KK-tower-dominated; SU(3) de-complexifies toward unstable maximum; analog of LLW Type-T²).
- **large-τ ↦ emergent-string** (candidate; conditional on WORLDSHEET-BOUNDARY-62 producing a tensionless Voronoi-boundary Nambu-Goto tower with `n·M²_string` density; analog of LLW Type-K3/T⁴).
- Scope tag: **classified-by-analogy** — the dichotomy SHAPE is reproduced; the CY-fibration PROOF is not inherited (SU(3) ≠ Calabi-Yau).

No verdict line is emitted (review gate; closes by artifact-existence-with-content per `gate-verdicts.md §"Investigation-Track Canonical Path"`).

---

## IV. Structural Implications

1. **The 38-closure audit survives the modern refresh.** No 2018–2025 conjecture creates a new structural TENSION. The pre-2018 status (`cross-framework-comparisons.md §"Swampland status"`) is upgraded from "consistent vs the 2017-era conjectures" to "consistent vs the 2018–2025 conjecture set," closing the standing 7-year library gap (R-3) for the swampland sub-domain specifically. CF14 "Swampland c(tau)" (D-6, opened S47, never revisited) is now addressed: the refined-dS clause is satisfied on both branches.

2. **The refined-dS match is over-determined and derivation-level, not just conclusion-level.** The framework satisfies BOTH refined-dS clauses (monotonic potential → clause 2; tachyonic saddle Hessian → clause 3), and reaches clause (3) via the SAME η-problem mechanism OPSV invoke. This is the strongest single point of refined-dS congruence — it is not "the framework happens to have no dS vacuum" but "the framework's tachyonic transit structure IS the clause-(3) mechanism, derived the same way."

3. **The Emergent-String dichotomy gives B-5 a concrete shape but not a CY proof.** The framework's 1-modulus τ-line reads cleanly as decompactification (τ→0) + candidate-emergent-string (large-τ). This is the swampland signature of "in the landscape, not the swampland" — but **classified-by-analogy**, because SU(3) ≠ CY3. The framework's economy (1 modulus vs ~O(100) per CY3, `cross-framework-comparisons.md §"Mathematical apparatus distinction"`) means it CANNOT host the LLW fibration zoo; it has a single τ-line with two ends. The dichotomy classifies that line's two ends, which is the most that can be claimed without a CY structure. **The large-τ emergent-string leg is the framework's sharpest falsifiable swampland-side prediction**: it stands or falls on WORLDSHEET-BOUNDARY-62 (critical dimension `c_eff=8`? on the constrained Voronoi boundary).

4. **The species-scale check is benign, not a falsifier.** The framework sits at the THIN (small-N) end of the Dvali spectrum, the controlled-weakly-coupled regime — the opposite of Dvali's large-N hierarchy scenario. The only open item is the RATIO-vs-CUTOFF scale-type pinning, which is a consistency-check carry-forward (cross-ref INV9-W2-2), not a TENSION.

5. **Constraint-map update**: the swampland wall-set is re-confirmed as a set of boundary conditions the substrate respects (4/4 modern conjectures CONSISTENT or cleanly classified). Per the framing law, this STRENGTHENS the surviving-region reading (the substrate occupies a region consistent with the modern walls) WITHOUT being a prediction — it is internal-consistency confirmation. The one new structural finding routable to session-promotion is the **τ-limit dichotomy classification** (decompactification + candidate-emergent-string), which is a structural result about the moduli-space ends, eligible for a session-promotion falsifier-inventory consideration (mack sole-writer) IF the large-τ emergent-string leg is confirmed.

---

## V. Carry-Forward Computations

**V.1. Substrate-first canonical re-computation of the field excursion Δφ/M_Pl.**
   - **What**: Compute the framework's field excursion `Δφ/M_Pl` from first principles (the τ-trajectory geodesic distance in the canonically-normalized field metric across the transit), to replace the SEED-AUTHOR survey value `0.170` with a substrate-first canonical pin. Distinguish it explicitly from `delta_tau_crit_pos = 0.175` (a moduli-deformation critical point, a different observable).
   - **Inputs**: the Jensen-deformation kinetic-term metric on the τ-line; `tau_fold = 0.19`; `M_Pl_reduced = 2.435e18`; the canonically-normalized field map `φ(τ)`.
   - **Gate**: new gate `DELTA-PHI-CANONICAL-PIN` — PASS if `Δφ/M_Pl < 1` (sub-Planckian, Distance-Conjecture safe); INFO if `0.1 < |Δφ/M_Pl − 0.170| / 0.170 < 1` (survey value approximately reproduced); promotes the pin to `canonical_constants.py` on PASS (Class-8.3 write-order). Feeds conjecture-(2) sharpened-Distance audit.
   - **Effort**: 1 agent session (the metric is known; the geodesic integral is a 1D quadrature on the τ-line).

**V.2. RATIO-vs-CUTOFF scale-type pinning for the Dvali species-scale check.**
   - **What**: Resolve which scale ratio the framework's `Λ_sp/M_KK = 2.06` maps to under Dvali's `Λ_G ≈ M_Pl/√N` (eq. 1.2), using `N_shell` from INV9-W2-2. Pin whether the consistency check is `Λ_sp/M_KK` (internal) or `Λ_G/M_Pl = 1/√N` (gravitational-cutoff), and verify the THIN-tower (small-N) reading numerically.
   - **Inputs**: `N_shell` (eigenvalue count in `[M_KK, 2.06 M_KK]`, from INV9-W2-2 `inv9_w2_ds_entropy_species_count.npz`); `Lambda_sp_over_M_KK = 2.06`; `M_KK = 7.428660036284456e16`; `M_Pl_reduced = 2.435e18`; Dvali eq. 1.1/1.2/4.2.
   - **Gate**: new gate `DVALI-SPECIES-SCALE-TYPE-PIN` — PASS if the framework's `√N_shell`-implied cutoff is mutually consistent with `2.06` once the scale-type is pinned (O(1) on the correct ratio); INFO if the scale-type ambiguity persists. Cross-ref INV9-W2-2.
   - **Effort**: 0.5 agent session (depends on INV9-W2-2's `N_shell`; arithmetic once `N_shell` lands).

**V.3. WORLDSHEET-BOUNDARY-62 critical-dimension computation (the emergent-string-leg decider).**
   - **What**: Compute the critical dimension `c_eff` of the constrained Voronoi-cell-boundary Nambu-Goto worldsheet at the large-τ limit (`c_eff = 8`?), to decide whether the large-τ infinite-distance limit is a genuine EMERGENT-STRING limit (asymptotically tensionless consistent string, `n·M²_string` density) or defaults to a decompactification/obstructed limit. This is the decisive falsifier of the Emergent-String dichotomy reading (conjecture 3).
   - **Inputs**: the SU(3) Voronoi-Delaunay complex (the WORLDSHEET-BOUNDARY-62 construction, `cross-framework-comparisons.md §"S61 shadow thesis"`); the large-τ Jensen-deformation limit of the internal metric; the Nambu-Goto quantization on the constrained boundary; the shriek-map degeneration microstate count.
   - **Gate**: new gate `WORLDSHEET-BOUNDARY-62-CRITICAL-DIM` — PASS (emergent-string leg confirmed) if the constrained Voronoi boundary supports a consistent tensionless string at its critical dimension (`c_eff` matches a consistent string); FAIL (leg refuted, large-τ defaults to decompactification/obstructed) if `c_eff` is inconsistent. Feeds the conjecture-(3) Emergent-String dichotomy verdict and the B-5 "in the landscape" classification.
   - **Effort**: 2–3 agent sessions (the Voronoi-boundary geometry + Nambu-Goto critical-dimension count is a genuinely new computation; flagged in the S61 shadow thesis as queued).

**V.4. Live gradient-bound number for the refined-dS clause-(2) audit (cross-ref, already queued as INV9-W1-2).**
   - **What**: The `|S'(τ)|/S(τ)` gradient-bound number at the fold (the live instance of conjecture-1 clause-2). Already queued as **INV9-W1-2**; listed here only as the cross-reference so the next-session planner sees the refined-dS audit's specific-instance dependency.
   - **Inputs**: per INV9-W1-2 (the spectral-action gradient `dS/dτ` at `tau_fold`).
   - **Gate**: INV9-W1-2 (existing). This review (the BROAD audit) consumes W1-2's number for the refined-dS clause-(2) margin.
   - **Effort**: N/A (already planned as INV9-W1-2; no new effort).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Refined de Sitter (OPSV-2018) CONSISTENT — both clauses, η-problem-derived clause (3) | NON-PHONONIC (GEOMETRIC deciders) | CONSISTENT | Over-determined match; derivation-level congruence via shared η-problem mechanism |
| 2 | Sharpened Distance CONSISTENT — sub-Planckian 5.9×, KK tower present | NON-PHONONIC | CONSISTENT | `Δφ/M_Pl=0.170` is SURVEY (flag); substrate-first re-pin is V.1 |
| 3 | Emergent String (LLW-2019) τ-limit dichotomy classified | GEOMETRIC | classified-by-analogy | τ→0 decompactification; large-τ candidate emergent-string; CY-proof NOT inherited (SU(3)≠CY3); decided by WORLDSHEET-BOUNDARY-62 (V.3) |
| 4 | Dvali species scale CONSISTENT + named caveat | PHONONIC | CONSISTENT | THIN tower = benign small-N Dvali regime; RATIO-vs-CUTOFF scale-type pinning is V.2 |
| 5 | 38-closure audit survives modern refresh; no new TENSION | NON-PHONONIC (cross-framework audit) | CONSISTENT | 7-year swampland library gap (R-3) closed for this sub-domain; CF14/D-6 addressed |

**Closure note**: all four modern conjecture primaries were fetched in full (OPSV-2018, OOSV-2018 reproduction, LLW-2019, Dvali-Redi 2007); NO conjecture carries the `classified-from-survey-structure-pending-primary-fetch` tag. The synthesis closes by artifact-existence-with-content; per the framing law, every CONSISTENT tag is an internal-consistency confirmation, NOT a prediction of the framework.
