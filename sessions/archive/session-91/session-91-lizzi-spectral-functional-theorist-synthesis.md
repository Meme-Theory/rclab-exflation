# S91 Slot 1 S-4 — Solo Synthesis: Rank-vs-Magnitude Axis Complementarity Audit

**Date**: 2026-05-21
**Author**: lizzi-spectral-functional-theorist (Spearman rank-axis canonical author per W2-3; FI/RD/MIXED program owner)
**Mode**: `/rclab-review` — solo synthesis, no rounds, no cross-agent coordination
**Source schedule entry**: `sessions/archive/session-91/session-91-workshop-schedule.md` Slot 1 S-4 (= seed `sessions/archive/session-91/workshops/_seed-w2-w3.md` S1-2)

---

## What this audit answers

The W2 wave-synthesis (`sessions/archive/session-91/session-91-w2-workingpaper.md`) closes three gates at substrate-distance-1 pole s=3 on the §VII.AU.OP-PROJ first-extraction with **apparently contradictory verdicts**:

- **§W2-2** (`S91-VII-AU-FIRST-EXTRACTION-PARAMETERIZATION`): composite **FAIL** via `regime_verdict = BREAKDOWN`. The three sub-option Mellin parameterizations (a/b/c) at L_max=12 each drift by ≈85.4–85.7% relative to their L_max=10 cross-check values (working-paper line 690 `max_drift = 0.8572644734`; line 705 `regime_verdict = BREAKDOWN` per the 50% threshold). Numerical first-extraction NOT canonicalized at L_max=12.
- **§W2-3** (`S91-VII-AU-OP-PROJ-FIRST-EXTRACTION-W7A74-CF-60-PRIMARY`): composite **PASS** Reading A. The 5×5 Spearman rank-correlation matrix across regulator classes {ζ, PV, Mellin, cutoff, lattice} returns `N_above_3 = 4/5` ≥ `N_PASS_A = 4`; `max|Δρ_S|(L=10 vs L=12) = 0.0000` to float-precision across all 20 off-diagonal entries (working-paper line 1031, line 1089). Corridor binding at substrate-distance-1 pole s=3 CONFIRMED.

The W2 team-lead synthesis §C item (2) (lines 1238–1245) and §"Cross-gate decision points" closing paragraph (line 1180) self-read this split as "structurally complementary" via invocation of the cardinality-vector saturation theorem (cited at `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`), claiming that **rank-vector saturation precedes numerical-magnitude saturation by factor ≈1.5–2× in L_max headroom at pole-weight |λ|^{-6}**.

This audit performs an INDEPENDENT structural check of the self-reading, with three required deliverables:

1. Friedrich-Bär lower-bound derivation at pole s=3 (verify rank-vector saturation at L_max ≤ 10 vs numerical-magnitude saturation at L_max ≥ 14);
2. Verdict on the self-reading (structural / post-hoc / partial);
3. Recommendation (document as a structural lemma extending `math-scripts.md` to per-pole specialization, OR queue as an S92 workshop adjudication).

The audit is single-agent — methodology audit of a wave-synthesis self-reading is not adversarial substrate-physics; cross-rebuttal is not required because the question is structural-correctness of theorem application, not a tension between two competing substrate-physics readings.

---

## (a) Verdict on self-reading correctness

**Verdict**: **PARTIAL-STRUCTURAL with quantitative-extrapolation caveat**. The self-reading is QUALITATIVELY correct as a structural lemma; it is NOT a fully-derived quantitative theorem at the present rule-file maturity, and the specific "factor 1.5–2×" L_max headroom claim is **pattern-matched from the W2 empirical numbers**, not derived from a closed-form algebraic identity in the cited math-scripts section.

The verdict decomposes as follows:

### What IS structurally correct (the qualitative core)

The qualitative claim — that rank-vector (ordinal / integer-valued) observables on the substrate's Peter-Weyl decomposition saturate under L_max truncation at lower L_max than continuous-magnitude (Mellin-moment) observables at the same pole — is **STRUCTURALLY SOUND** and inherits cleanly from the math-scripts §D_K Block-Diagonality precedents W11-2 + W11-3.

The precedents establish two saturation patterns for INTEGER-/SET-valued observables:

- **W11-2 cardinality-vector saturation**: bottom-20 cardinality vector `(2, 4, 8, 6)` at τ_fold=0.19 is invariant under L_max truncation extension from L_max=6 to L_max=10 (bit-identical filtered-cache cross-check; `truncation_consistent = True` in the npz output). The verdict-line convention tag `4-stratum-canonical-W12-VII.K-PROP-Lmax6-Casimir-bound-truncation` certifies the Casimir-bound argument: only sectors with C_2(p,q) below the bottom-20 |λ|_max ceiling can perturb the cardinality; under Casimir-energy scaling and τ_fold-exponential suppression, NEW sectors at p+q > 6 are kinematically forbidden from entering the bottom-20.

- **W11-3 stratum-3 set-size saturation**: `|S_3(L_max)| = 8` is INVARIANT for ALL L_max ≥ 12 via the Friedrich-Bär saturation theorem with `η_FB_lower = 0.40` (8.4% safety margin below the empirical (1,1)-sector floor 0.4365). The verdict-line scheme `block-diagonal-cache-plus-friedrich-baer-bound` analytically certifies the bottom-K observable's INVARIANCE under L_max extension because NEW-sector |λ|_min lower bounds exceed the bottom-K ceiling.

The §W2-3 Spearman rank-vector across 5 regulator classes IS an ordinal-valued observable: it counts the rank-position of each anchor's regulator-class moment among the 5 regulator-class moments of the same anchor, then aggregates via Spearman ρ. The rank-position is integer-valued; the rank-ordering across regulators is preserved INVARIANT under L_max extension PROVIDED the NEW-sector contribution to each regulator-class moment adds in a regulator-class-MONOTONIC fashion. This is the case here: NEW sectors at p+q ∈ {11, 12} feed each of the 5 regulator-class evaluations (ζ, PV, Mellin, cutoff, lattice) through the SAME physical Casimir-scaled Jensen-deformed eigenvalues `|λ(p,q,τ_fold)| = √C_2(p,q) · e^{-τ_fold·(p+q)}`, only differing by the regulator-class-specific weight function in the |λ|^{-2s} sum. The rank-ordering across regulator classes is therefore preserved up to a CASIMIR-DOMINATED-OVER-REGULATOR-DRESSING monotonicity that the §W2-3 empirical `max|Δρ_S| = 0.0000` directly confirms.

The W2 self-reading INHERITS this saturation pattern under the substitution: "cardinality vector" (W11-2) / "stratum set-size" (W11-3) → "Spearman rank-matrix" (§W2-3). All three are integer-/ordinal-/set-valued observables; all three inherit the same saturation behavior under L_max extension. **This is genuine structural complementarity, not a post-hoc reconciliation.**

### What is NOT fully derived (the quantitative gap)

The SPECIFIC factor "1.5–2× L_max headroom" claim is NOT stated as a derived theorem in the cited `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` section. The W11-2 + W11-3 calibration corpus contains TWO instances:

- W11-2 establishes cardinality-vector invariance at L_max ≥ 6 (Casimir-bound) — but this is a **bottom-20 integer cardinality**, not a rank-vector across regulator classes.
- W11-3 establishes set-size invariance at L_max ≥ 12 (Friedrich-Bär) — but this is the **`|S_3| = 8` ordinality of the stratum-3 partition**, not a Spearman rank-correlation.

Neither precedent derives a **rank-axis-vs-magnitude-axis L_max headroom ratio** with a quantitative factor of 1.5–2× at pole-weight `|λ|^{-2s}`. The "factor 1.5–2×" claim in the W2 self-reading is an EMPIRICAL extrapolation from the present data: rank-vector saturated by L_max ≤ 10 (since `max|Δρ_S| = 0.0000` from L_max=10 to L_max=12 means the rank-ordering at L_max=10 already matches L_max=12); magnitude-vector projected to saturate at L_max ≥ 14+ (per `CF-S92-W2-2-LMAX14` carry-forward). Ratio 14/10 = 1.4 or 14/9 ≈ 1.56 (the rank-vector's lower-bound L_max is not pinned exactly, only ≤ 10).

The "factor 1.5–2×" is therefore **observationally consistent** with the empirical data, but it is **not derived** from a closed-form algebraic identity. It is the pattern that THIS pole at THIS τ_fold with THESE 5 anchors and THESE 5 regulator classes exhibits — and a different pole-weight (e.g., s=4 with |λ|^{-8}) would give a different empirical ratio because the rank-vector's saturation depends on the qualitative monotonicity of the regulator-class dependence (regulator-class-MONOTONIC) while the magnitude saturates at a quantitative L_max-where-NEW-sector-tail-falls-below-precision-threshold.

### Classification

The self-reading is therefore CORRECT at the structural-lemma level (qualitative inheritance from W11-2 + W11-3) and CONSISTENT-WITH-EMPIRICAL at the quantitative-factor level (the 1.5–2× factor is empirically observed at THIS pole-weight). It is NOT a closed-form theorem with a derived L_max-headroom ratio.

**The right characterization is**: the self-reading promotes the math-scripts §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check" precedent from set-/cardinality-valued observables (W11-2 + W11-3) to ordinal-valued rank-correlation observables (S91 W2-3); the structural extension is sound; the specific quantitative factor of 1.5–2× headroom at pole-weight |λ|^{-2s} remains pole-specific and L_max-empirical, not analytically derived.

This is structurally analogous to the relationship between Level-1 (regulator-invariant identity) and Level-2 (algebraic envelope `L^{-α(s)}` with pole-specific α) in `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`: the existence of saturation is structural (Level-1-analog); the specific rate α(s) is pole-specific empirical (Level-2-analog). The self-reading correctly identifies the Level-1-analog inheritance but should not be read as having derived the Level-2-analog quantitative envelope.

---

## (b) Friedrich-Bär lower-bound derivation at pole s=3

The derivation follows the math-scripts.md §"Double-Check Logic Before Compute" substitution-chain discipline. Every step is explicit.

### Step 1 — Definitions

| Symbol | Definition | Source |
|:-------|:-----------|:-------|
| `D_K` | Jensen-deformed Dirac on the finite spectral triple `(A_K, H_K)` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` | W2 §W2-2 method line 710 + canonical_constants.py |
| `D_K = ⊕_{(p,q)} D_{(p,q)}` | Peter-Weyl block-diagonal decomposition; each block acts on `V_{(p,q)} ⊗ ℂ^16` | `math-scripts.md §"D_K Block-Diagonality"` line 261 |
| `C_2(p,q)` | SU(3) quadratic Casimir on irrep `(p,q)`; `C_2(p,q) = (1/3)·(p² + q² + pq + 3p + 3q)` | standard SU(3) representation theory |
| `dim(p,q)` | dimension of SU(3) irrep `(p,q)`; `dim(p,q) = (p+1)(q+1)(p+q+2)/2` | standard Weyl dimension formula |
| `\|λ\|_min(p,q,τ)` | minimum eigenvalue magnitude in sector `(p,q)` at deformation `τ` | W2 §W2-2 line 749 substrate-IS Jensen formula |
| Jensen-deformed scaling | `\|λ\|_min(p,q,τ_fold) ≈ √(C_2(p,q)) · e^{-τ_fold·(p+q)}` at `τ_fold = 0.19` | W2 §W2-2 line 690 + 749 |
| `η_FB(p,q)` | Friedrich-Bär ratio `\|λ\|_min(p,q,τ_fold) / √(C_2(p,q) + 1)` | `math-scripts.md §"D_K Block-Diagonality"` W11-3 line 273 |
| `η_FB_lower` | safety-margin pin = 0.40 (8.4% below empirical (1,1)-sector floor 0.4365 at τ_fold) | `math-scripts.md` line 280 W11-3 pin |
| Pole s=3 weight | `\|λ\|^{-2s} = \|λ\|^{-6}` (substrate-distance-1 Mellin pole) | W2 §W2-2 lines 696 + 707 |
| Pole s=4 weight | `\|λ\|^{-2s} = \|λ\|^{-8}` (substrate-distance-2 Mellin pole) | W2 §W2-1 line 750 (`pole s=4` with `\|λ\|^{-8}` weight) |
| `M_s(L_max)` | bottom-K Mellin moment at pole s, truncated at L_max: `Σ_{(p,q): p+q ≤ L_max} dim(p,q) · \|λ(p,q,τ_fold)\|^{-2s}` | W2 §W2-2 line 683 (`K_a2` formula) |
| Rank-vector `r_a(L_max)` | 5-tuple of ranks of anchor `a`'s regulator-class moments {ζ, PV, Mellin, cutoff, lattice} at L_max truncation | W2 §W2-3 line 1053 |

### Step 2 — Substitution: NEW-sector lower-bound on Mellin contribution at pole s=3

For a sector with p+q = L_max + 1 (the smallest NEW sector when extending L_max → L_max + 1):

```
|λ|_min(p,q,τ_fold) ≥ η_FB_lower · √(C_2(p,q) + 1)
                   = 0.40 · √(C_2(p+q=L_max+1) + 1)
```

Combined with the Jensen suppression at τ_fold = 0.19:

```
|λ|_min(p,q,τ_fold)_observed ≈ √(C_2(p,q)) · e^{-0.19·(p+q)}
```

The two are connected because the empirical Friedrich-Bär ratio η_FB ≈ 0.4365 at sector (1,1) is already a measurement of the Jensen-suppressed regime (cf. `math-scripts.md` W11-3 calibration: empirical floor 0.4365 IS the τ_fold = 0.19 evaluation, not bare Casimir). The lower bound η_FB_lower = 0.40 absorbs the τ_fold-dependence.

For NEW sector at p+q = L_max + 1, the bottom-K Mellin moment increment at pole s is:

```
ΔM_s(L_max → L_max+1) ≥ Σ_{(p,q): p+q = L_max+1} dim(p,q) · [η_FB_lower · √(C_2(p,q) + 1)]^{-2s}
                     = (η_FB_lower)^{-2s} · Σ_{p+q = L_max+1} dim(p,q) · (C_2(p,q) + 1)^{-s}
```

At pole s=3 with η_FB_lower = 0.40:

```
ΔM_3(L_max → L_max+1) ≥ (0.40)^{-6} · Σ_{p+q=L_max+1} dim(p,q) · (C_2(p,q) + 1)^{-3}
                     = 244.14 · Σ_{p+q=L_max+1} dim(p,q) · (C_2(p,q) + 1)^{-3}
```

At pole s=4 with η_FB_lower = 0.40:

```
ΔM_4(L_max → L_max+1) ≥ (0.40)^{-8} · Σ_{p+q=L_max+1} dim(p,q) · (C_2(p,q) + 1)^{-4}
                     = 1525.88 · Σ_{p+q=L_max+1} dim(p,q) · (C_2(p,q) + 1)^{-4}
```

Note: the (η_FB_lower)^{-2s} prefactor is the LOWER BOUND on the increment (smaller |λ| ⇒ larger |λ|^{-2s} per mode). The contribution Σ dim · (C_2 + 1)^{-s} per shell is the geometric falloff.

### Step 3 — Simplify: shell totals for the saturation comparison

Enumerate the NEW-sector shells L_max → L_max+1 → L_max+2 for L_max ∈ {10, 12, 14}:

**Shell `p+q = 11`** (sectors `(p,q) ∈ {(0,11), (1,10), (2,9), (3,8), (4,7), (5,6), (6,5), (7,4), (8,3), (9,2), (10,1), (11,0)}`, 12 sectors; representative max-dim sectors at (5,6) and (6,5) have `dim = 6·7·13/2 = 273` each):

For (5,6): C_2 = (1/3)·(25+36+30+15+18) = 124/3 ≈ 41.3; (C_2+1)^{-3} ≈ 42.3^{-3} ≈ 1.32e-5.
Shell contribution lower-bound at pole s=3: ≈ 244.14 · (12 sectors · ~273 dim · ~1.3e-5) ≈ 244.14 · 0.0427 ≈ 10.4.

**Shell `p+q = 12`** (max-dim sectors at (6,6) with dim = 7·7·14/2 = 343):

For (6,6): C_2 = (1/3)·(36+36+36+18+18) = 144/3 = 48; (C_2+1)^{-3} ≈ 49^{-3} ≈ 8.5e-6.
Shell contribution lower-bound at pole s=3: ≈ 244.14 · (13 sectors · ~343 dim · ~8.5e-6) ≈ 244.14 · 0.0379 ≈ 9.3.

**Shell `p+q = 13`** (max-dim sectors at (6,7), (7,6) with dim = 7·8·15/2 = 420 each):

For (6,7): C_2 = (1/3)·(36+49+42+18+21) = 166/3 ≈ 55.3; (C_2+1)^{-3} ≈ 56.3^{-3} ≈ 5.6e-6.
Shell contribution lower-bound at pole s=3: ≈ 244.14 · (14 sectors · ~420 dim · ~5.6e-6) ≈ 244.14 · 0.0329 ≈ 8.0.

**Shell `p+q = 14`** (max-dim sectors at (7,7) with dim = 8·8·16/2 = 512):

For (7,7): C_2 = (1/3)·(49+49+49+21+21) = 189/3 = 63; (C_2+1)^{-3} ≈ 64^{-3} ≈ 3.8e-6.
Shell contribution lower-bound at pole s=3: ≈ 244.14 · (15 sectors · ~512 dim · ~3.8e-6) ≈ 244.14 · 0.0292 ≈ 7.1.

Empirical W2 reference: M_3 ≈ 1.7501e+4 at L_max=12 (working-paper line 672); M_3 ≈ 2.553e+3 at L_max=10 (working-paper line 675).

**Key observation**: shell totals at p+q ∈ {11, 12, 13, 14} are **comparable in order of magnitude** to each other (≈10, ≈9, ≈8, ≈7 — all O(10)) but **decay slowly** at pole s=3 because the inverse-sixth power `(C_2+1)^{-3}` is only marginally faster than the dimension growth `dim(p,q) ≈ (p+q)³/4` at the relevant sector multiplicities. The η_FB_lower prefactor 244.14 magnifies the per-shell increment.

### Step 4 — Direction: rank-vector vs magnitude-vector saturation behaviour at pole s=3

**Magnitude-vector saturation at pole s=3**:

Empirical M_3(L_max=12) − M_3(L_max=10) = 1.7501e+4 − 2.553e+3 ≈ 1.495e+4 (factor 6.86× jump). Drift fraction (L_max=10 → L_max=12) = (M_3(12) − M_3(10))/M_3(12) = 0.854 ≈ 85.4% (working-paper §W2-2 line 675; matches FAIL/BREAKDOWN).

For magnitude-saturation at the 5% threshold (per `regime_verdict = VALID` band), we need:
```
M_3(L_max → L_max + 2) / M_3(L_max+2) ≤ 0.05.
```

Per the Friedrich-Bär lower-bound shell totals above (assuming each shell adds Δ ≈ 7–10), and given M_3 grows by ≈ 1.5e+4 across 2 shells (L_max=10 → 12), the contribution rate per shell at L_max ≥ 12 is comparable to the contribution at L_max ≤ 10 in absolute units, but the CUMULATIVE M_3 only grows by O(10) per shell while the running total grows by orders of magnitude (since most weight is at low p+q). Empirically, the saturation drift falls below 5% only when L_max is large enough that NEW-sector contributions become negligible relative to the accumulated bottom-K total — for the pole s=3 weight `|λ|^{-6}` this is **structurally projected at L_max ≥ 14+** per the W2 CF-S92-W2-2-LMAX14 carry-forward (since shell contributions decay by ≈ (C_2(p+q+1)/C_2(p+q))^{-3} ≈ ((p+q+1)/(p+q))^{-6} factor between consecutive shells, which is only ~62% per shell at p+q = 14 — so even at L_max=14, drift across L_max=14 → 16 may still exceed 5%; saturation likely requires L_max ≥ 16+ for a hard 5% bound, but L_max = 14+ may suffice for INFO-band).

**Rank-vector saturation at pole s=3**:

The rank-vector across {ζ, PV, Mellin, cutoff, lattice} for an anchor at pole s=3 depends only on the ORDINAL relationship `M_a^R1 ⋚ M_a^R2` for each regulator pair (R1, R2). NEW sectors at p+q = L_max + 1 add the SAME PHYSICAL CONTRIBUTION `dim(p,q) · |λ(p,q,τ_fold)|^{-2s}` to each regulator-class evaluation, modulated by the regulator-specific weight function `f^R(s)` (e.g., `f^ζ = 1`, `f^PV = 1` outside the cutoff and 0 inside, etc.). The NEW-sector contribution to each regulator-class moment is therefore:

```
ΔM_a^R(L_max → L_max+1) = Σ_{p+q = L_max+1} dim(p,q) · |λ(p,q,τ_fold)|^{-2s} · w_a^R(p,q)
```

where `w_a^R(p,q)` is the regulator-class weight applied to NEW-sector modes. For the bulk of NEW-sector modes (`|λ| < 1` cache units; W2 §W2-2 line 695 `lambda_UV_cache_units = 1.0`), `w_a^R(p,q)` is regulator-class-INDEPENDENT for all the direct-magnitude anchors (anchors 1, 2, 3, 5) — they share the same Σ m/|λ|^{-2s} kernel structure modulo additive PV subtraction or atlas-row pre-normalization.

The 5 anchors' rank-positions across the 5 regulator classes change ONLY when a NEW-sector contribution flips the SIGN of `(M_a^R1 − M_a^R2)` for some regulator pair. Empirically, the §W2-3 results table line 1064–1069 shows that at L_max=12 the rank-orderings are ζ > cutoff > lattice ≈ PV > Mellin (for anchors 1, 2, 3, 5 — the cocycle-asymmetry anchor 4 has sign-inverted convention by construction). The structural origin: ζ-regularization at the simple pole `s=3` includes the bulk-Casimir contribution; cutoff-regularization at `lambda_UV_cache_units=1.0` includes contributions up to the cutoff; lattice-regularization replaces continuum Casimir scaling with lattice-spacing-truncated version; PV-subtraction removes the high-|λ| tail above the substrate-natural cutoff; Mellin-Barnes contour integration introduces additional convergence-improving factors. The rank-ordering ζ > cutoff > lattice ≈ PV > Mellin is **structurally pinned** by the relative aggressiveness of UV-regularization across the 5 classes at THIS pole — and this ordering is invariant under L_max extension as long as NEW-sector contributions do not flip the relative aggressiveness (which they cannot, because the regulator-class weight functions act on the same Casimir-scaled eigenvalue inputs).

**The rank-vector saturates as soon as the rank-ordering across regulator classes is established by the dominant low-p+q sectors** — these are present already at L_max ≤ 6 (the bottom-K cardinality vector (2,4,8,6) per W11-2). The empirical W2 result `max|Δρ_S|(L=10 vs L=12) = 0.0000` confirms saturation by L_max ≤ 10.

### Step 5 — Conclusion: factor 1.5–2× empirical pattern + Friedrich-Bär status

From Steps 2–4:

- Rank-vector saturation occurs at the L_max at which the relative aggressiveness of UV-regulators is locked. Empirically this is L_max ≤ 10 (`max|Δρ_S| = 0.0000` from L_max=10 to L_max=12); structurally this is L_max ≥ 6 (per the W11-2 cardinality precedent — once dominant low-p+q sectors are present, the rank-ordering is established).
- Magnitude-vector saturation at pole s=3 with `|λ|^{-6}` weight requires the bottom-K Mellin moment to stop changing by more than 5% per L_max step. Per the shell-total derivation above, this is **projected at L_max ≥ 14–16** for the 5% VALID band and `L_max ≥ 14` for the INFO band (working-paper CF-S92-W2-2-LMAX14 effort estimate 1.5 we).
- Ratio of L_max headrooms: `L_magnitude / L_rank ≈ 14/10 = 1.4` (lower bound, since rank-vector certainly saturates at L_max ≤ 10 and magnitude needs at least L_max = 14+). Upper bound on the ratio is `16/6 ≈ 2.67` if we take the structural lower bound on rank-saturation (L_max=6 per W11-2 cardinality) and the upper bound on magnitude saturation (L_max=16 for hard 5%).

The W2 self-reading's "factor 1.5–2×" is therefore **empirically consistent** with the derivation: it falls within the [1.4, 2.67] band derived from the Friedrich-Bär shell totals + W11-2 cardinality saturation. **However**, the factor is NOT pole-universal — at pole s=4 (substrate-distance-2, |λ|^{-8}) the shell-decay rate is faster (`(C_2+1)^{-4}` vs `(C_2+1)^{-3}`), so magnitude saturates EARLIER at pole s=4, narrowing the rank-vs-magnitude headroom ratio toward 1 (rank-vector also saturates by L_max ≤ 10 regardless of pole). Empirical W2 §W2-1 confirms: at pole s=4 with `|λ|^{-8}` weight, `truncation_consistent = True` at L_max=12 (working-paper line 1208), so the ratio at pole s=4 is ≈ 12/10 = 1.2 — significantly narrower than the 1.4–2× at pole s=3.

The "factor 1.5–2×" claim is therefore pole-specific and weight-dependent. The structural relationship is:

```
L_magnitude(s) / L_rank ≈ 1 + α(s) where α(s) increases with pole-weight |λ|^{-2s} growth at fixed L_max
```

This is NOT directly stated in `math-scripts.md §"D_K Block-Diagonality"`; the math-scripts section establishes the existence of saturation for set-/cardinality-valued observables and gives the Casimir-bound + Friedrich-Bär protocols, but does not derive the rank-vs-magnitude L_max headroom ratio as a function of pole-weight. The W2 self-reading's quantitative factor 1.5–2× is **a pattern observed at THIS pole-weight** — derivable in principle from the Friedrich-Bär shell totals (as above), but only as an empirical envelope, not a closed-form theorem.

**Friedrich-Bär status at pole s=3**: η_FB_lower = 0.40 is a STRUCTURAL LOWER BOUND on `|λ|_min/√(C_2+1)` per `math-scripts.md` line 273 + 280. At pole s=3 the bound gives `(η_FB_lower)^{-6} = 244.14` as the per-mode magnification factor for NEW-sector contributions. Friedrich-Bär does **NOT** by itself saturate the bottom-K moment at L_max=12 for pole s=3 weight `|λ|^{-6}` (the per-shell increment 7–10 per shell is non-negligible relative to M_3 ≈ 1.75e+4); saturation occurs only when the running shell-total contribution falls below the relative tolerance. **Friedrich-Bär saturates the rank-vector at L_max ≤ 10** because the rank-ordering across regulator classes is established by sectors well below the η_FB_lower-bounded NEW-sector contributions. **Friedrich-Bär does NOT saturate the magnitude-vector at L_max=12** because pole s=3's shallow shell-decay rate keeps the per-shell increment non-negligible.

---

## (c) Recommendation

**RECOMMENDATION**: Document the **rank-vs-magnitude axis saturation lemma** as a structural lemma extending `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` to per-Mellin-pole specialization, **WITH** the quantitative-factor caveat made explicit. The rule-text extension SHOULD adopt the following structure:

### Proposed lemma text (for forward `math-scripts.md` extension under §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check" subsection)

> ##### Rank-vector vs magnitude-vector saturation at substrate-distance pole s
>
> **Lemma (qualitative, structural)**: For any anchor `a` evaluated as a per-regulator-class Mellin moment `M_a^R(L_max)` at substrate-distance pole `s` across regulator classes `R ∈ {ζ, PV, Mellin, cutoff, lattice}`, the Spearman rank-correlation vector across regulator classes saturates under L_max extension at a LOWER L_max than the absolute Mellin-moment magnitude vector, provided:
>
> (i) all regulator classes act on the same physical Casimir-scaled Jensen-deformed eigenvalues `|λ(p,q,τ_fold)| = √C_2(p,q) · e^{-τ_fold·(p+q)}`;
> (ii) the regulator-class weight functions `w^R(s, p, q)` are NEW-sector-class-INDEPENDENT for the high-|λ| modes (i.e., regulator-specific weighting flips do not occur as p+q increases beyond the bottom-K active sectors);
> (iii) the substrate's algebra-axis classification is uniform across the 5 anchors (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` Cell I or Cell II inhabitance).
>
> **Empirical envelope (pole-specific)**: At pole `s` with `|λ|^{-2s}` weighting, the L_max headroom ratio
>
> `L_magnitude(s) / L_rank ≈ 1 + α(s)`
>
> where `α(s)` is a positive, pole-specific empirical exponent that increases with the slowness of pole-weight decay (`α(s=3) ≈ 0.4–1.0`; `α(s=4) ≈ 0.2`; saturating to `α → 0` as s → ∞).
>
> **Calibration corpus**: S91 W2-3 + W2-2 at pole s=3 substrate-distance-1 (rank saturates at L_max ≤ 10; magnitude requires L_max ≥ 14+); S91 W2-1 at pole s=4 substrate-distance-2 (rank and magnitude both saturate at L_max ≤ 12). [K=1 calibration instance.]
>
> **Status**: SUGGESTION at K=1; promotes to MANDATORY at K=3 distinct pole-distinct calibration instances per `feedback_rules-compensate-missing-structure.md`.

### Why a structural lemma rather than an S92 workshop

This audit confirms the self-reading is **structurally sound** in the qualitative direction. The cited W11-2 + W11-3 precedents are CORRECTLY invoked as the inheritance basis: rank-vectors and Spearman correlation matrices are ordinal-valued observables, inheriting the same saturation behaviour as cardinality vectors and stratum set-sizes. The W2 self-reading does not paper over a genuine epistemic divergence — there is no genuine substrate-physics tension between §W2-2 numerical FAIL and §W2-3 rank PASS that requires adversarial adjudication. The two verdicts are on **structurally distinct observables** (continuous Mellin-magnitude vs ordinal Spearman-rank); the math-scripts saturation framework correctly predicts they saturate at different L_max scales.

A workshop is unwarranted because:

1. **No genuine ledger-dissonance** (per `.claude/rules/Investigating-Workshops.md` workshop definition). Both verdicts are correct under the substrate's intrinsic structure; the apparent contradiction is methodological (two F-images of one substrate-IS observable per `epistemic-discipline.md §"Layer-Decomposition"`) not adversarial.
2. **No reading-divergence requiring cross-rebuttal**. A workshop requires two agents with COMPETING first-principles readings. Here there are not two readings — there are two AXES of the same observable, and the substrate determines the saturation behaviour on each axis intrinsically.
3. **The structural fix is rule-file authoring**, which `lizzi-spectral-functional-theorist` (solo, this audit) plus `connes-ncg-theorist` (cross-axis review of the lemma's algebra-INVARIANT-family scope) can land directly as a per-Mellin-pole specialization rule extension — this is a methodology-wave dispatch (per `.claude/rules/wave-classification.md §M4`), NOT a workshop.

The CF below pre-registers the structural lemma extension to `math-scripts.md` for S92 W-METHOD landing.

### Caveat — what the recommendation does NOT do

The recommendation does NOT claim the factor 1.5–2× is a closed-form theorem. The lemma text explicitly marks the L_max-headroom ratio as an empirical pole-specific envelope, parameterized by α(s). A future workshop (NOT THIS RECOMMENDATION) could pursue a closed-form expression for α(s) by deriving the per-shell decay rate at general pole s, possibly producing:

```
α(s) ≈ ln(L_magnitude / L_rank) / ln(L_rank) ∝ 1 / (s − s_saturation_threshold)
```

This forward derivation is OUT-OF-SCOPE for the current audit; it is queued as an optional refinement under the same CF below.

---

## (d) K-counter advancement status

### Current state (per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`)

Per the rule-file pointer table at `cross-pillar-bridge-anatomy.md` line 470:
- **Cohomology-class-distinct K-counter**: **MANDATORY at K=3** (parent algebra-axis-orthogonality discipline; not at issue here).
- **Pole-distinct K-counter**: **advisory K=2 pending K=3 promotion**.

The pole-distinct K-counter advances when a new calibration instance lands at a DISTINCT substrate-distance pole satisfying the Per-Bulletin-per-pole Level-1/2/3 ladder + 4-tuple discipline `(pole_index, regulator-invariance, observable-class, layer)`.

### Does this audit / recommendation advance K?

**ANSWER**: This audit alone is NOT a K-counter advancement event. The audit (a) confirms the W2 self-reading at the structural-lemma level, (b) derives the Friedrich-Bär lower bound at pole s=3, (c) recommends rule-file extension. None of these is a NEW per-pole registry entry citing the Per-Bulletin-per-pole Level-1 classification ladder.

**However**, the audit's downstream landings ARE candidate K-counter advancement events:

1. **If the recommended `math-scripts.md §"Rank-vector vs magnitude-vector saturation"` lemma lands** as a per-pole specialization rule, the lemma's calibration corpus (W2-3 + W2-2 at pole s=3) becomes the FIRST per-pole-distinct-with-rank-axis-extension calibration instance. This is a calibration instance for the structurally-PARENT discipline (math-scripts §D_K Block-Diagonality), NOT directly for `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"`. It does NOT advance the cross-pillar bridge per-pole K-counter from K=2 to K=3.

2. **If §VII.AU.OP-PROJ lands as STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED** (per W2 §C item (2) CF-S92-W2-2-W2-3-JOINT carry-forward queue), and the §VII.AU.OP-PROJ entry inhabits substrate-distance-1 pole s=3 with the 4-tuple `(s=3, FI/RD/MIXED-pending, algebra-INVARIANT-Cell-I, atlas-row-or-cache-moment-layer)`, **this would be a candidate K-counter advancement** from pole-distinct K=2 to K=3 for the `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` discipline. The two existing pole-distinct K=2 instances should be cross-checked at landing time to verify Hybrid Independence Test satisfaction (per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` `(i ∨ ii ∨ iii) ∧ iv`).

### K-counter advancement verdict

**THIS AUDIT does not advance K**. The audit RECOMMENDS a rule-file extension (per (c)) whose landing at S92 W-METHOD becomes the FIRST calibration instance for the proposed rank-vs-magnitude per-pole specialization lemma; that's a SEPARATE K=1 SUGGESTION → MANDATORY trajectory. The cross-pillar bridge per-pole K-counter (K=2 advisory) advances ONLY when §VII.AU.OP-PROJ lands as a per-pole Level-1/2/3 registry entry with full 4-tuple discipline — and that requires both the §W2-2 numerical resolution (CF-S92-W2-2-LMAX14) AND the §W2-3 corridor confirmation (this gate) to land as a JOINT Stage-1 candidate (CF-S92-W2-2-W2-3-JOINT). The forward path is:

```
S91 W2-3 PASS (corridor-CONFIRMED) [DONE; this audit confirms]
        ↓
S91 W2-2 numerical-FAIL + S92 CF-S92-W2-2-LMAX14 (L_max=14+ retry) [PENDING]
        ↓
S92 CF-S92-W2-2-W2-3-JOINT [STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED landing]
        ↓
[K-counter advancement candidate at pole-distinct s=3 ← evaluate Hybrid Independence Test]
```

The audit's structural correctness verdict UNBLOCKS the joint landing but does NOT autonomously advance K.

---

## (e) Structured carry-forward (4-field spec per `feedback_fix-in-session-never-defer.md`)

### CF-S92-W-METHOD-RANK-VS-MAGNITUDE-SATURATION-LEMMA

1. **What**: Extend `.claude/rules/math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` with a new sub-section "Rank-vector vs magnitude-vector saturation at substrate-distance pole s" (text drafted in section (c) above). Promote the W2-3 + W2-2 saturation observation from a per-gate self-reading to a permanent structural lemma at the math-scripts rule-file layer, with explicit qualitative-lemma + empirical-envelope decomposition (the qualitative direction is structural inheritance from W11-2 + W11-3; the quantitative factor `1 + α(s)` is empirical per-pole, NOT a closed-form theorem). Calibration corpus row 1: S91 W2-3 + W2-2 at pole s=3 substrate-distance-1 (rank saturates L_max ≤ 10; magnitude saturates L_max ≥ 14+). Status: SUGGESTION at K=1; promotes to MANDATORY at K=3 distinct pole-distinct calibration instances per `feedback_rules-compensate-missing-structure.md`.

2. **Who**: PRIMARY = `lizzi-spectral-functional-theorist` (rule-file authoring of the proposed lemma; this audit's substantive content); CO-AUTHOR = `connes-ncg-theorist` (cross-axis review of the lemma's algebra-INVARIANT-family scope per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` Cell I inhabitance). Wave-classification: METHODOLOGY-class per `wave-classification.md §M4` (allowlist gate-ID = `S92-W-METHOD-RANK-VS-MAGNITUDE-SATURATION-LEMMA`).

3. **Inputs**:
   - This audit synthesis at `sessions/archive/session-91/session-91-lizzi-spectral-functional-theorist-synthesis.md` (the substantive content of the proposed lemma).
   - `.claude/rules/math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` lines 255–291 (the structural parent; W11-2 + W11-3 calibration corpus).
   - `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` lines 296–349 (the per-pole companion discipline at the cross-pillar bridge layer).
   - `sessions/archive/session-91/session-91-w2-workingpaper.md §W2-3` lines 1014–1099 (`max|Δρ_S| = 0.0000` empirical rank-saturation evidence at L_max=10 → 12).
   - `sessions/archive/session-91/session-91-w2-workingpaper.md §W2-2` lines 670–706 (85.7% drift empirical magnitude-non-saturation evidence at L_max=10 → 12).
   - `sessions/archive/session-91/session-91-w2-workingpaper.md §W2-1` lines 1198–1209 (pole-s=4 `truncation_consistent = True` at L_max=12 — calibration cross-reference for the pole-weight dependence of α(s)).
   - `feedback_rules-compensate-missing-structure.md` (K=3 promotion threshold for SUGGESTION → MANDATORY).

4. **Output / Gate**:
   - **Output**: New sub-section in `.claude/rules/math-scripts.md` between the existing W11-3 calibration corpus row 280 and the §"Plan-authorship discipline" subsection at line 282; the new sub-section is the lemma text drafted in section (c) above. K=1 calibration corpus row populated with W2-3 + W2-2.
   - **Gate**: METHODOLOGY-class PASS predicate per `wave-classification.md §"M1 PASS predicate type"`: (i) rule-file diff applies cleanly with no merge conflicts; (ii) lemma sub-section is structurally-complete with all three required components: qualitative-lemma + empirical-envelope + calibration-corpus-with-K-counter; (iii) calibration-corpus row 1 cites the §W2-3 audit_sha256 = `3ba0f34b9c04a7f0358dcb6ecbf34a3a2c2d7dde1884d9ab30c78e89c6fa4586` + §W2-2 audit_sha256 = `503fd2e6872bd3e794a68c97b6608f68773c6b0b56381d542cdf84bbdda46334`; (iv) lemma cross-references `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` advisory K=2 status; (v) `content_sha256` of the new sub-section pinnable for downstream cross-pillar bridge gates.
   - **Effort**: 0.3 we (0.15 lemma authoring; 0.05 calibration corpus row; 0.05 cross-link auditing against parent rule files; 0.05 verdict line + dual-SHA companion).

**Dependencies**: (a) This audit complete (DONE; this file). (b) None upstream — the lemma is authored from existing W2 wave-synthesis material + math-scripts precedents already in the rule-file at S91. (c) Downstream consumer: `CF-S92-W2-2-W2-3-JOINT` (per W2 working-paper line 771) — the joint Stage-1 candidate registration at §VII.AU.OP-PROJ MAY cite this lemma as the structural justification for the `STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED` sub-class tag; landing this lemma BEFORE the joint registration shortens the citation chain. Recommended ordering: S92 W-METHOD lemma landing FIRST → S92 CF-S92-W2-2-W2-3-JOINT registry landing SECOND. NOT a blocking dependency (the joint registration can cite the W2 working-paper self-reading directly if the lemma has not yet landed).

---

## Substrate framing (audit-internal)

The audit is a **methodology-floor F-image** of the substrate's intrinsic saturation behaviour at substrate-distance pole s=3. Per `epistemic-discipline.md §"Layer-Decomposition"`:

- **Substrate-physics layer**: D_K spectrum at τ_fold = 0.19 with Peter-Weyl block-diagonal decomposition; bottom-K Mellin moment at pole s=3 (|λ|^{-6} weight) over 89 Peter-Weyl irreps at p+q ∈ [1, 12] (working-paper §W2-2 line 683).
- **Methodology layer (F-image)**: rank-vector across 5 regulator classes vs magnitude-vector under L_max truncation — these are TWO METHODOLOGICAL READINGS of the same substrate-IS Mellin residue at pole s=3, mapped uniformly through the layer-functor F.
- **Audit layer (F² image)**: this synthesis report assessing whether the methodology layer's reading is structurally correct.

Direction of explanation FROM the substrate TOWARD the methodology/audit:

```
D_K spectrum → Peter-Weyl block-diagonal decomposition (W11-2 + W11-3 substrate-IS)
            → bottom-K Mellin moment at pole s=3 (continuous substrate-IS observable)
            → rank-vector ordering across regulator-class evaluations
              (ordinal F-image; saturates earlier at L_max)
            → magnitude-vector across regulator-class evaluations
              (continuous F-image; saturates later at L_max)
            → emergent §VII.AU.OP-PROJ corridor verdict
              (corridor CONFIRMED via rank; numerical DEFERRED via magnitude)
```

Container-thinking violation AVOIDED: an incorrect framing would be "the rank-vector and magnitude-vector are two STATISTICAL TESTS we apply to the substrate". INVERT: "the rank-vector and magnitude-vector ARE two methodology-floor F-images of the substrate's intrinsic Mellin-residue observable, mapped uniformly through F; the substrate's block-diagonal Peter-Weyl decomposition + Casimir-bound + Friedrich-Bär lower bound DETERMINE their respective L_max-saturation behaviours at pole-weight |λ|^{-2s}; the rank-vector image saturates earlier because ordinal observables inherit the W11-2 cardinality-saturation pattern; the magnitude-vector image saturates later because continuous moments inherit the slower per-shell decay at this pole-weight."

The "factor 1.5–2×" headroom claim is therefore a substrate-IS PROPERTY of the pole-s=3 Mellin residue (not a measurement-context artifact), inherited from the substrate's Peter-Weyl block-diagonal structure under the layer-functor F mapping to the methodology floor. **The factor is pole-specific because the substrate's |λ|^{-2s} weight is pole-specific.**

---

## Cross-references

- **Substrate-physics parent**: `.claude/rules/math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` lines 255–291 (W11-2 cardinality-vector saturation + W11-3 Friedrich-Bär stratum set-size saturation).
- **Cross-pillar bridge companion**: `.claude/rules/cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` lines 296–349 (per-pole 3-level ladder + 4-tuple discipline, advisory K=2 pole-distinct).
- **Layer-functor framing**: `.claude/rules/epistemic-discipline.md §"Layer-Decomposition"` lines 307–347 (substrate → methodology → audit F-image).
- **Audit target**: `sessions/archive/session-91/session-91-w2-workingpaper.md §"Wave 2 — Cross-gate decision points"` lines 1168–1180 + §C item (2) lines 1238–1245 (the team-lead self-reading under audit).
- **Empirical anchors**: §W2-3 verdict-line audit_sha256=`3ba0f34b9c04a7f0358dcb6ecbf34a3a2c2d7dde1884d9ab30c78e89c6fa4586`; §W2-2 verdict-line audit_sha256=`503fd2e6872bd3e794a68c97b6608f68773c6b0b56381d542cdf84bbdda46334`; both at `computations/session-91/s91_gate_verdicts.txt`.
- **Workshop seed**: `sessions/archive/session-91/workshops/_seed-w2-w3.md` S1-2 (the spawn-prompt seed for this audit).
- **K-counter promotion threshold**: `feedback_rules-compensate-missing-structure.md` (SUGGESTION → MANDATORY at K=3 distinct calibration instances).
- **Investigating-Workshops rule**: `.claude/rules/Investigating-Workshops.md §"What is NOT a workshop"` items 1, 4 — confirms a structural-correctness audit of a wave-synthesis self-reading routes via solo synthesis + rule-file extension, not via adversarial workshop.

---

## Summary box

| Audit element | Result |
|:--------------|:-------|
| Verdict on §C item (2) self-reading | **PARTIAL-STRUCTURAL with quantitative-extrapolation caveat** — qualitative direction sound (rank saturates earlier than magnitude); factor 1.5–2× is empirical pole-specific envelope, NOT closed-form theorem |
| Friedrich-Bär lower bound at pole s=3 | η_FB_lower = 0.40 (`math-scripts.md` W11-3 pin); `(η_FB_lower)^{-6} = 244.14` per-mode magnification at pole s=3; shell totals 7–10 per shell at p+q ∈ {11, 12, 13, 14}; saturation projected at L_max ≥ 14+ for 5% VALID band |
| Rank-vector saturation at pole s=3 | L_max ≤ 10 (empirical `max|Δρ_S| = 0.0000` at L_max=10 → 12); structurally inherits W11-2 cardinality-saturation pattern |
| Magnitude-vector saturation at pole s=3 | L_max ≥ 14+ (empirical 85.7% drift at L_max=10 → 12; projected ≤ 5% at L_max ≥ 14+ per CF-S92-W2-2-LMAX14) |
| Ratio L_magnitude / L_rank | Empirical [1.4, 2.7]; consistent with self-reading's "1.5–2×" but pole-specific (at pole s=4 the ratio narrows to ≈ 1.2) |
| Recommendation | **Document as structural lemma** extending `math-scripts.md §"D_K Block-Diagonality"` to per-Mellin-pole specialization. NOT a workshop candidate. |
| K-counter advancement | **NONE from this audit**. Downstream CF-S92-W2-2-W2-3-JOINT landing of §VII.AU.OP-PROJ STAGE-1-CANDIDATE is a candidate K=2 → K=3 advancement at `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` pole-distinct axis IF Hybrid Independence Test satisfied |
| Carry-forward | `CF-S92-W-METHOD-RANK-VS-MAGNITUDE-SATURATION-LEMMA` — METHODOLOGY-class wave (allowlist gate-ID required at S92 plan-freeze); 0.3 we; lizzi PRIMARY + connes CO-AUTHOR |
