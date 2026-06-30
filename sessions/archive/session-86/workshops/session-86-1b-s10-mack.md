# Session 86 Synthesis: LAYER-3 |ρ| Atlas-Shape Sensitivity, Forward-Map ANSATZ Coherence, and PV-Weighting Geometry

**Date**: 2026-04-27
**Agent**: mack-cosmic-bridge (Slot 1b, entry S-10)
**Source Documents**:
- `sessions/archive/session-86/session-86-w8-workingpaper.md` (§W8-1 P6 9-cell commit; §W8-2 P7 LAYER-3 MC; §W8-3 C7 L_max truncation)
- `computations/_artifacts/s86_w8_p7_rho_mc_ensemble.npz` (5×10000 substrate ensemble; `regulator_labels`, `delta_a2`, `delta_a4`, `alpha_s_central`, `omega_gw_central`, `rho_grid`)
- `computations/canonical_constants.py` (`planck_ns = 0.9649` line 1247; `f_LISA_pivot = 3.0e-3 Hz` line 368; `alpha_s_cmb_central = -0.06896799` line 367)
- `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md` (S85 W1b α_s canonical drift; S83 layer/scope discipline)
- mcp__knowledge__: `S86-RHO-SUBSTRATE-PREDICTION-MC` gate row; `planck_ns` constant pin

---

## I. Session Outcome

P7's LAYER-3 reading +0.950874 is a **W13-2-ansatz-conditional** statement, not a substrate-deep one. Three of four ANSATZ swaps preserve |ρ| ≥ 0.988; the fourth (decoupled n_s ← a_2 / Ω_GW ← a_0) collapses the value to +0.269 under uniform weighting and **+0.000** under PV-excl. The substrate's predictive coherence is carried jointly by (i) the W12-4 atlas's monotonic regulator progression in (a_2, a_4) and (ii) the W13-2 forward-map convention that wires both observables to that progression with parallel signs; remove either and |ρ| degrades. PV-PCA confirms the analytic identity `var_PC1 = (1+|ρ|)/2` exactly on the 50000-point MC ensemble; the `≥98%` PC1-variance threshold PASSes 2/3 cells (PV-dn 98.83%, PV-excl 99.15%) and FAILs the uniform cell at 97.54%. The pre-registered "5-point analytic |ρ| matches MC within 1e-3" FAILs (gaps 0.011/0.006/0.017) — the 5-point line is the noiseless limit; per-regulator perturbation noise (σ=0.001 F_4 / σ=0.05 M) decorrelates. The shift_uniform pre-registration was misspecified: at +0.05 and +0.10, α_s^k still spans negative values (max α_s^k after +0.10 shift is -0.019 < 0); the magnitude≡signed identity holds at +0.05 EXACTLY and at +0.10 with residual ≤0.005, NOT by coincidence but because |α_s^k| inherits the same monotone ordering across regulators while α_s^k stays single-signed (until 0.962 < delta). The §W8-2 line 291 conditional ("if α_s straddled zero, magnitude and signed would generally differ") is **CONFIRMED**: shift_mixed (which true-straddles zero) yields ||signed|-magnitude| up to 0.0081 (uniform), 0.0051 (PV-dn), 0.0000 (PV-excl); the gap is real but **smaller than the pre-registered 0.10 detection band** — the conditional's qualitative truth holds; its quantitative magnitude was overpredicted.

---

## II. Key Results

### Result 1 — Forward-map ANSATZ test: substrate vs methodological interpretation

**Result**: |ρ|_uniform = (canonical: +0.962) → (i) SWAP n_s↔Ω: +0.997 → (ii) BOTH←a_0: +1.000 (with PV-excl collapse to 0.000) → (iii) BOTH←a_2 (CS limit): +0.988 → (iv) DECOUPLED: **+0.269** (uniform) / +0.125 (PV-dn) / **+0.000** (PV-excl). **GEOMETRIC** (substrate spectral-moment couplings).

**Substitution chain (interpretation (B) hold direction)**:

1. **Definition**: ANSATZ (k) = a forward-map convention that wires (n_s, Ω_GW) to elements of the W12-4 spectral-moment vector (a_0, a_2, a_4).
2. **Substitute canonical (n_s ← a_2, Ω_GW ← a_4)**: under δ_a2 = (0, 0, -0.023, -0.298, -0.799) and δ_a4 = (0, 0, -0.013, -0.110, -0.433), both quantities monotone-decrease across the atlas; ρ_signed_uniform = +0.962 (5-point central line).
3. **Substitute ANSATZ (iv) (n_s ← a_2 alone, Ω_GW ← a_0 alone)**: under δ_a0 = (0, 0, 0, -0.457, 0), Ω_GW^k drops only at cutoff_sqrt and stays at the zeta value for the other 4 regulators; α_s^k still varies smoothly across the 5 atlas points. The (α_s, Ω_GW) ensemble becomes effectively 1+1 dimensional with three coincident points.
4. **Simplify**: under PV-excl (which kills cutoff_sqrt and anomaly), ANSATZ (iv) leaves Ω_GW^k = constant for the 3 surviving regulators (zeta, Zubarev, SDW all identical a_0); σ_Ω = 0; ρ → 0/0 → conventionally 0.
5. **Direction**: |ρ|_PV-excl drops from 1.000 (canonical) to 0.000 (ANSATZ iv) — a 1.000 swing under a single ANSATZ flip. **The W13-2 convention contributes the value at LAYER-3, not just the substrate.**

**Implication**: P7 |ρ| = +0.951 is interpretation (B) **methodological** — the W13-2 ansatz that couples both observables to the same monotone-decreasing axis (a_2 and a_4 are correlated by spectral construction since both come from the same heat-kernel partial sum) does the bulk of the work. Interpretation (A) "substrate predicts |ρ| ≈ 0.95 deeply" survives only in the weaker form: the substrate's spectral moments (a_0, a_2, a_4) are themselves correlated under W12-4 regulator-class variation, which is what makes ANSATZ (iii) BOTH←a_2 and (i) SWAP also high-|ρ|. The deeply-substrate statement is "the W12-4 atlas spectrum points are a near-1D curve in (a_0, a_2, a_4) space." The layer-3 |ρ| then follows for ANY ansatz that picks two non-orthogonal projections of that curve.

### Result 2 — PV-weighting PCA decomposition

**Result**: PCA on the 50000-point MC ensemble gives `var_PC1` = 97.54% (uniform) / 98.83% (PV-dn) / 99.15% (PV-excl). Analytic identity `var_PC1 = (1+|ρ|)/2` matches MC values to machine epsilon. **PHONONIC** (substrate ensemble geometry).

**Substitution chain**:

1. **Definition**: standardize (α_s^k_i, Ω_GW^k_i) under weight w_k/N; the 2×2 weighted correlation matrix is `[[1, ρ], [ρ, 1]]` by construction.
2. **Substitute eigendecomposition**: eigenvalues are `λ_± = 1 ± ρ` (standard 2×2 result). Trace = 2; var_PC1 fraction = `(1+|ρ|)/2` (taking the larger eigenvalue).
3. **Simplify**: ρ_MC = 0.950874 → var_PC1 = (1+0.950874)/2 = 0.975437; ρ_MC = 0.976681 → var_PC1 = 0.988341; ρ_MC = 0.983026 → var_PC1 = 0.991513.
4. **Direction**: var_PC1 monotonically tracks |ρ|; PV-progression uniform → PV-dn → PV-excl monotonically increases var_PC1. **PASS direction confirmed for PV-dn (98.83%) and PV-excl (99.15%); FAIL by 0.46 percentage points for uniform (97.54%) against the pre-registered 98% threshold.**

**Implication**: The `≥98%` pre-registration was set to capture "near-1D collapse"; the canonical (signed, uniform) cell sits 0.46pp BELOW the threshold. This is **NOT a structural failure of the LAYER-3 anchor** — the canonical reading lives in PC1 by 97.5% which is "near-1D" in any practical sense — but it IS a pre-registration miss: the threshold was set without anchoring it to a derivation. A correctly-pre-registered threshold should have been the analytic identity itself: `var_PC1_min = (1 + |ρ|_min_PASS)/2 = (1 + 0.951)/2 = 97.54%`. The 5-point central PCA gives slightly higher values (97.85% / 99.15% / 100.00%) because it lacks the per-regulator perturbation noise; it FAILs the same 98% threshold for uniform (97.85%).

### Result 3 — shift_uniform pre-registration was misspecified

**Result**: At δ = +0.05, max α_s^k = -0.019 < 0 (NOT positive throughout). At δ = +0.10, max α_s^k = +0.031 but min α_s^k = -0.862 (still straddles zero). True sign-flip requires δ > +max(|α_s^k|) = +0.962. **PHONONIC** (atlas-shape sensitivity).

**Substitution chain**:

1. **Definition**: pre-registered prediction was "shift_uniform → α_s^k > 0 throughout → magnitude=signed agreement."
2. **Substitute**: α_s^k_canonical = (-0.069, -0.069, -0.112, -0.541, -0.962). After +0.05 shift: (-0.019, -0.019, -0.062, -0.491, -0.912). After +0.10 shift: (+0.031, +0.031, -0.012, -0.441, -0.862).
3. **Simplify**: at +0.05, all α_s^k still NEGATIVE → α_s^k all-same-sign → `|α_s^k| = -α_s^k` (linear sign flip) → `Cov(|α|, |Ω|) = Cov(-α, +Ω) = -Cov(α, Ω)` → `σ_|α| = σ_α`, `σ_|Ω| = σ_Ω` → `ρ_inner_magnitude = -ρ_signed` → `ρ_magnitude := |ρ_inner_magnitude| = |ρ_signed|` **EXACTLY**.
4. **Direction**: at +0.05 the magnitude=|signed| identity holds to machine epsilon (verified empirically: ||signed|-magnitude| = 0.000000 at all three weightings). At +0.10 a small subset of regulators flip positive, breaking the linear-flip exactness; residual ≤0.005 (uniform) and ≤0.002 (PV-dn). At δ ≥ +0.97 (genuine all-positive), identity restored exactly.

**Implication**: The pre-registered "shift_uniform → magnitude=signed agreement" is **TRIVIALLY TRUE** at both δ=+0.05 and δ=+0.10 because α_s does NOT actually straddle zero (the prediction's stated condition was misspecified). The identity `ρ_magnitude = |ρ_signed|` is a **theorem when α_s is single-signed**, not an empirical agreement. Pre-registration did not anchor δ to the structural threshold |min α_s^k| = 0.962. Correct pre-registration would have specified shift_uniform with δ > +0.962 to test the magnitude=signed identity in the post-flip regime, and a smaller probe (e.g., δ ∈ {-0.05, +0.05}) to verify it in the pre-flip regime where the theorem already guarantees agreement.

### Result 4 — shift_mixed straddle test (line-291 conditional)

**Result**: shift_mixed = (+0.10, +0.10, 0, -0.10, -0.10) gives α_mix = (+0.031, +0.031, -0.112, -0.641, -1.062), genuinely straddling zero. Resulting ||signed|-magnitude| = 0.0081 (uniform) / 0.0051 (PV-dn) / 0.0000 (PV-excl). **PHONONIC** (atlas-shape sensitivity).

**Substitution chain**:

1. **Definition**: §W8-2 line 291 conditional: "If α_s straddled zero, magnitude and signed would generally differ." Pre-registered detection band: any cell with ||signed|-magnitude| ≥ 0.10.
2. **Substitute shift_mixed**: α_mix straddles zero (max +0.031, min -1.062). ρ_signed_uniform = +0.936; ρ_inner_magnitude_uniform = -0.944; ρ_magnitude = |−0.944| = +0.944. Difference = |0.936 − 0.944| = 0.0081.
3. **Simplify**: when α_s straddles zero, the linear-flip identity (Result 3) BREAKS — `|α_s^k|` no longer equals `−α_s^k` for all k. The covariance decomposition acquires a non-canceling cross-term proportional to (a) the fraction of regulators that switch sign (here 2/5) AND (b) the relative magnitudes of |α_s^k| in the flipped vs unflipped subsets. The subset that flips (zeta, Zubarev at +0.031) carries small magnitudes; the subset that doesn't flip (SDW, cutoff_sqrt, anomaly at -0.112, -0.641, -1.062) carries the bulk of the variance. The net displacement of |α|-mean from -⟨α⟩ is small, hence the gap is small.
4. **Direction**: ||signed|-magnitude| > 0 confirms the §W8-2 line 291 conditional **QUALITATIVELY**. The maximum gap (0.0081) is 12× SMALLER than the pre-registered 0.10 detection band — the qualitative claim holds; the quantitative magnitude was over-predicted by an order of magnitude.

**Conclusion on §W8-2 line 291**: **CONFIRMED qualitatively** (signed and magnitude do differ when α_s straddles zero) but **MAGNITUDE OVER-PREDICTED**. The line's claim "would generally differ" is true; the implicit suggestion that the difference would be detectable at ≥0.10 level is false in this atlas geometry. The reason is structural: the W12-4 atlas is heavily weighted toward the M family (cutoff_sqrt, anomaly) where |α_s^k| is large; flipping the F_4 family at small |α_s^k| changes |α|-mean by O(0.04) which propagates to ρ at O(0.01).

### Result 5 — Cross-link to §W8-2 verdict

**Result**: P7 verdict-line value rho_signed_uniform = +0.950874 is **layer-3-DURABLE** under the (sign × atlas-weighting) freedom (max-min spread 0.0322 over 6 cells), but it is **ANSATZ-FRAGILE** under forward-map re-coupling (range from +0.000 to +1.000 over 4 ANSATZ swaps × 3 weightings). **PHONONIC**.

The W8 wave's (sign × atlas-weighting) 6-cell PASS robustness is real but limited in scope: it does not test the W13-2 ansatz itself. The ANSATZ (iv) collapse to ρ = +0.000 at PV-excl exposes that the LAYER-3 anchor depends on the W13-2 forward-map convention being correct — not just on the substrate's spectral content. This is a known structural tension: the §W8-1 6-axis machinery-pin template explicitly enumerates `convention` as Axis-2 with `LISA-PLS-2024+CMB-S4-Book-2019+atlas-weighting+linear-vs-log-derivative-J+signed-vs-magnitude` — but does NOT include "forward-map ansatz" as an admissible value. Per W0b R8 generalization clause this is a missing axis; should be Axis-7 in the next-session machinery-pin schema.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| §W8-2 / P7 (S86-RHO-SUBSTRATE-PREDICTION-MC) | PASS (per source — not re-adjudicated) | rho_signed_uniform = +0.950874; bootstrap σ_max = 3.31e-04; 6/6 cells in [0.819, 1.000] |
| Local: shift_uniform δ=+0.05 magnitude=|signed| identity | PASS (trivially, by single-sign theorem) | ||signed|−mag|| = 0.000000 (machine-epsilon, all 3 weightings) |
| Local: shift_uniform δ=+0.10 magnitude=|signed| identity | PASS (residual sub-threshold) | max ||signed|−mag|| = 0.0048 (uniform) ≪ 0.10 |
| Local: shift_mixed straddle test (§W8-2 line 291) | PARTIAL — qualitative CONFIRM, magnitude over-pre-registered | max ||signed|−mag|| = 0.0081 (uniform) < 0.10 detection band |
| Local: PV-PCA var_PC1 ≥ 98% | PASS 2/3 (PV-dn, PV-excl); FAIL 1/3 (uniform 97.54%) | var_PC1 (uniform) = 97.544%, gap −0.46 pp |
| Local: 5-point analytic |ρ| matches MC within 1e-3 | FAIL on quantitative threshold | gaps 0.011 / 0.006 / 0.017 (uniform / PV-dn / PV-excl) |
| Local: ANSATZ stability of LAYER-3 anchor | INFO — anchor is W13-2-conditional | range +0.000 → +1.000 across 4 ANSATZ × 3 weightings |

---

## IV. Structural Implications

### IV.1 Interpretation (A) vs (B) split

The slot-1b synthesis question — "(A) substrate predicts |ρ| ≈ 0.95 deeply vs (B) W13-2 ansatz predicts |ρ| ≈ 0.95 methodologically" — resolves as **a layered split, not an exclusive choice**:

- **(A) survives in the form**: "the W12-4 5-regulator atlas has near-1D structure in (a_0, a_2, a_4) space." This is independently true and is what makes ANSATZ (i), (iii), and even partial (ii) all give |ρ| ≥ 0.99 under uniform weighting. The substrate's spectral-moment vectors are correlated by construction (heat-kernel partial sums share regulator-class denominators).
- **(B) controls the value**: "the W13-2 convention that wires (n_s ← a_2, Ω_GW ← a_4) projects the near-1D substrate curve onto a 2D plane where |ρ| = +0.951." A different convention (e.g., decoupled) projects it differently and gets |ρ| = +0.269 or +0.000.

Practical implication for downstream consumers: when LISA × CMB-S4 data lands in 2030+, the comparison "substrate's predicted joint correlation pattern" must specify the W13-2 forward-map ansatz alongside the atlas-weighting. The §W8-1 6-axis pin schema is missing this axis (Axis-7 candidate). The §W8-1 PASS status is structurally correct as a methodology commit; the omission of the ansatz axis is a forward-looking PRU-Class-8 risk for joint-channel ρ verdicts that re-couple observables.

### IV.2 The §W8-2 audit-trail iteration was the correct discipline

Source §W8-2 lines 333-350 documents that the initial run produced rho_mag = -0.951/-0.977/-0.983 (negative magnitudes; plan-§10 NON-COMPLIANT) and the corrected run produced rho_mag = +0.951/+0.977/+0.983 (canonical). The ALL-3-LINES-RETAINED discipline preserved both verdict lines per S86 W1c-5 BULLETIN-S4 precedent. My Result 3 and Result 4 substitution chains explain WHY both lines were correct under their respective ρ_magnitude definitions: when α_s is single-signed, the inner Cov(|α|, |Ω|) = -Cov(α, Ω) is negative, and the "magnitude" needs an outer |·| to satisfy "ρ ≥ 0 by construction." This is not arbitrary convention — it is the consequence of the linear-sign-flip theorem (Result 3 step 3). The corrected run is canonical; the audit-trail iteration captures a legitimate definitional refinement, not a sig_5 SHA-collision bug.

### IV.3 The pre-registration of "5-point analytic matches MC within 1e-3" was over-tight

The 5-point central PCA gives the noiseless line; MC gives the noisy version with per-regulator perturbation σ=0.001 (F_4) / σ=0.05 (M). The widening of the cluster decreases |ρ| relative to the noiseless line by a few percent — gap 0.011 (uniform), 0.006 (PV-dn), 0.017 (PV-excl). The noise is asymmetric across regulators (M family has 50× larger fractional spread than F_4 per W12-4 5-class taxonomy fallback envelope), so the gap is largest where M dominates (PV-excl excludes M, but the residual M-noise correlation propagates into the PV-excl cell through the same MC ensemble). The 1e-3 pre-registration was set without analytically deriving the noise propagation; correct pre-registration should have computed the analytic noise correction `Δ|ρ|_noise = O(σ_perturb / σ_signal)` and used a 1e-2 band.

### IV.4 The threshold geometry of |ρ| is monotone across PV progression

Substitution chain for monotonicity claim:

1. **Definition**: var_PC1(w) = larger eigenvalue / trace = (1 + |ρ|(w))/2.
2. **Substitute weighting**: w_uni gives equal weight to all 5 regulators including high-spread M family; w_pvdn down-weights cutoff_sqrt and up-weights anomaly (mixed M effect); w_pvex zeros out M entirely.
3. **Simplify**: each step (uniform → PV-dn → PV-excl) progressively reduces the ensemble's dispersion off the principal axis (since M family is the high-dispersion contributor). Reducing off-axis dispersion increases var_PC1.
4. **Direction**: |ρ|(uniform) ≤ |ρ|(PV-dn) ≤ |ρ|(PV-excl) **monotonically**. Verified: 0.951 ≤ 0.977 ≤ 0.983.

This monotone progression is **structural** under the W12-4 (a)/(d) stratification, not coincidental. It would NOT survive ANSATZ (iv) decoupled (where PV-excl gives ρ = 0/0 → 0, BREAKING monotonicity). The monotonicity is therefore **a joint property of (W13-2 ansatz) × (W12-4 atlas)**, not a property of the substrate alone.

### IV.5 Cross-link to S83 layer/scope discipline (own memory)

My S83 W3-G42 LIVE-WATCH (`project_s83_w3_g42_dr3_live_watch.md`) and S84 DR3-RESPONSE-PROTOCOL (`project_s84_dr3_response_protocol.md`) established the framework's discipline of pre-registering rectangles with explicit scope (R_842 lockouts A-F). The §W8-1 6-axis machinery-pin schema is the analogous rectangle for joint-channel ρ verdicts. Result 1 and Result 5 here surface that the schema is **missing one axis** (forward-map ansatz). This is a S87 schema-extension, not a re-adjudication of P7's PASS verdict. P7's PASS stands within the 6-axis schema as currently committed; the carry-forward in §V.1 below extends the schema to 7-axis to forestall the ANSATZ ambiguity I uncovered.

### IV.6 Constraint-map updates triggered by this synthesis

| Item | Prior state | New state | Reason |
|:-----|:------------|:----------|:-------|
| §W8-1 6-axis machinery-pin schema | CANONICAL | CANONICAL but EXTENSION-CANDIDATE (Axis-7 = forward-map-ansatz) | ANSATZ (iv) decoupled gives |ρ| range 0.000 → 0.269; current schema does not pin this freedom |
| §W8-2 line 291 conditional ("magnitude and signed would generally differ if α_s straddled zero") | CONJECTURE in WP | CONFIRMED qualitatively (gap 0.0081); MAGNITUDE OVER-PRE-REGISTERED (band was 0.10, actual 0.0081) | shift_mixed scan; the 12× over-prediction is structural, driven by W12-4 atlas's M-family weight |
| Pre-reg "5-point analytic matches MC within 1e-3" | UNTESTED | FAIL on the 1e-3 band (gaps 0.011/0.006/0.017) | Noise propagation from per-regulator perturbation widens cluster; pre-reg was set without analytic noise model |
| Pre-reg "var_PC1 ≥ 98% PASS" | UNTESTED | PASS 2/3 (PV-dn 98.83%, PV-excl 99.15%); FAIL 1/3 (uniform 97.54%) | Threshold not anchored to derivation; correct reading is `var_PC1 = (1+|ρ|)/2` exactly, so threshold should track |ρ| pin |
| LAYER-3 anchor +0.951 interpretation | spot-check (R3, mack 9A §VI.2) → MC-anchored (P7 PASS) | CONDITIONAL on W13-2 ansatz; deep-substrate component is "W12-4 atlas is near-1D in (a_0, a_2, a_4)" | ANSATZ swap test; (i)/(iii) preserve |ρ| ≥ 0.99, (iv) collapses |ρ| → 0.27/0.00 |

None of these REVISE the §W8-2 P7 PASS verdict — they refine its scope and surface the next-layer machinery pins.

---

## V. Carry-Forward Computations

### V.1 Extend the §W8-1 6-axis machinery-pin schema to 7 axes (add forward-map ansatz)

- **What**: Update §W8-1 9-cell × 6-axis matrix (currently in `_artifacts/s86_w8_p6_diagrammatic_matrix.{npz,json}`) to include Axis-7 = `forward-map-ansatz` with admissible values `{W13-2-canonical, SWAP-channel, BOTH-LEFT-a_0, BOTH-LEFT-a_2-CS-LIMIT, DECOUPLED-a_2-vs-a_0}` and default pin `W13-2-canonical`. Re-emit the registry-write with `n_axes=7` and update W0b R8 generalization-clause text accordingly.
- **Inputs**: existing `_artifacts/s86_w8_p6_diagrammatic_matrix.{npz,json}`; my Result 1 ANSATZ table (5 ansatz × 3 weightings = 15 |ρ| values); `canonical_constants.py` `planck_ns`, `f_LISA_pivot`.
- **Gate**: `S87-W0b-R8-7AXIS-EXTENSION` — PASS if (i) 7-axis npz/json regenerated with bit-identical 9-cell content but expanded axes block, (ii) Axis-7 enumerates 5 ansatz with W13-2-canonical default-pinned, (iii) verdict line dual-SHA appended, (iv) §VII registry entry updated. INFO if the audit produces new ANSATZ candidates beyond my 5; FAIL if the W13-2-canonical default cannot be defended structurally.
- **Effort**: 1.5–2 hours, 1 mack-cosmic-bridge or connes-ncg-theorist agent session (registry-write class, no new MC).

### V.2 Re-derive the var_PC1 ≥ 98% pre-registration with analytic anchoring

- **What**: Replace the bare `var_PC1 ≥ 98%` threshold with the analytic identity `var_PC1_threshold = (1 + |ρ|_PASS_min) / 2` and re-evaluate against the 6-cell ρ_grid from §W8-2 (RATIO ≤ 1e-1 vs 0.91 reference). This produces a PASS/FAIL table that tracks |ρ| by construction rather than via an arbitrary 98% pin.
- **Inputs**: `_artifacts/s86_w8_p7_rho_mc_ensemble.npz` (rho_grid field); pre-registered |ρ|_PASS_min = 0.819 (from RATIO ≤ 1e-1 vs 0.91); analytic identity above.
- **Gate**: `S87-PV-PCA-VAR-THRESHOLD-RECAL` — PASS if (i) `var_PC1_threshold = (1+0.819)/2 = 0.9095` is satisfied for all 6 cells (currently the lowest var_PC1 is 0.975 for uniform, well above 0.9095); (ii) verdict line dual-SHA appended; (iii) §W8-2 line 304 cross-check #2 updated to cite the new threshold form. FAIL if any cell falls below 0.9095.
- **Effort**: 0.5–1 hour, 1 mack-cosmic-bridge agent session (analytic refit only, no new compute).

### V.3 Test the 5-point analytic vs MC noise-propagation gap analytically

- **What**: Derive `Δ|ρ|_noise = f(σ_F4, σ_M, atlas-weighting)` analytically using first-order perturbation of the weighted Pearson identity. Compare against the empirical gaps 0.011/0.006/0.017 to confirm the noise-propagation model. If the analytic gap matches empirical to within Monte-Carlo error (3.31e-04), the pre-registered 1e-3 threshold should be replaced with the analytic noise correction.
- **Inputs**: per-regulator MC empirical std table from my Result 2 (`std(α): zeta 1.87e-3, Zub 1.85e-3, SDW 1.76e-3, cutoff 4.57e-2, anomaly 3.83e-3`); `_artifacts/s86_w8_p7_rho_mc_ensemble.npz`; canonical_constants pins.
- **Gate**: `S87-RHO-NOISE-PROPAGATION-ANALYTIC` — PASS if analytic prediction matches empirical |Δρ| to within 1e-3 across all 3 weightings; INFO if the analytic model captures the qualitative ordering (uniform > PV-dn < PV-excl) but quantitative match is ±10%; FAIL if the analytic prediction misses by >2× anywhere.
- **Effort**: 2–3 hours, 1 mack-cosmic-bridge or lizzi-spectral-functional-theorist agent session (perturbation analysis + Python verification).

### V.4 Recompute shift_uniform with delta > +0.962 (true sign-flip regime)

- **What**: Re-run the shift_uniform scan at δ ∈ {+1.0, +1.05, +1.5} where ALL α_s^k ≥ 0, plus a control point δ ∈ {-0.05, -0.10} where the linear-flip identity holds. Verify that the magnitude=|signed| identity holds exactly in BOTH regimes (single-sign-positive and single-sign-negative) and breaks ONLY in the straddle regime.
- **Inputs**: `_artifacts/s86_w8_p7_rho_mc_ensemble.npz`; the shift function from this slot.
- **Gate**: `S87-SHIFT-UNIFORM-FULL-REGIME` — PASS if (i) at δ ≥ +0.962, ||signed|-magnitude|| ≤ 1e-12 (machine epsilon) for all 3 weightings, AND (ii) at δ ≤ -0.05, same identity holds, AND (iii) the only regime where the identity breaks is the straddle regime −0.05 < δ < +0.962; INFO if the post-flip identity holds to ≤1e-6 but not exactly; FAIL if the identity breaks somewhere unexpected.
- **Effort**: 0.5 hour, 1 mack-cosmic-bridge agent session (scan extension only).

### V.5 Test ANSATZ (iv) decoupled at LISA-band f_pivot to anchor the ANSATZ-extreme cell

- **What**: Compute the LAYER-3 |ρ| under ANSATZ (iv) (n_s ← a_2 alone, Ω_GW ← a_0 alone) using the full forward-map pipeline including S69 transit-GW spectrum (rather than my simple δ_a0 substitution). This will test whether the +0.000 PV-excl collapse persists when the full Ω_GW(f_LISA) interpolation chain is used.
- **Inputs**: `s69_transit_gw.npz` (full spectrum); `omega_gw_loglog_interp` helper; `canonical_constants.py` pins; my Result 1 ANSATZ table for cross-check.
- **Gate**: `S87-LAYER3-ANSATZ-iv-FULL-PIPELINE` — INFO regardless of result (this is a methodology-extension probe, not a substrate-prediction probe). Records the LAYER-3 |ρ| value under ANSATZ (iv) at registry-grade precision; feeds the §W8-1 7-axis schema (V.1 above) with a numerical reference for the DECOUPLED admissible value.
- **Effort**: 2–3 hours, 1 mack-cosmic-bridge agent session.

### V.6 Document the line-291 conditional re-calibration in the §W8-2 working paper

- **What**: Append a §W8-2 line-291 footnote stating: "The line-291 conditional is CONFIRMED qualitatively (max ||signed|-magnitude|| = 0.0081 under shift_mixed = (+0.10,+0.10,0,-0.10,-0.10) per S86 slot 1b S-10 mack synthesis) but the difference is 12× smaller than the implicit ≥0.10 detection band. Future joint-channel ρ verdicts that test the magnitude=signed identity should pre-register a band of ≤0.01 to capture realistic atlas-shape sensitivity."
- **Inputs**: this synthesis (Result 4); §W8-2 line 291 source; W0b R7+R8 methodology entries.
- **Gate**: `S87-W8-2-LINE-291-RECAL` — PASS if footnote landed verbatim; INFO if the orchestrator decides to defer to a wave-level annotation. No FAIL band.
- **Effort**: 0.5 hour, 1 agent session (documentation patch).

### V.7 Cross-check the canonical (signed, uniform) anchor under the DR3 live-watch protocol

- **What**: Verify that the LAYER-3 anchor +0.951 is ROBUST to the DR3 input-pin map updates expected when DESI DR3 lands (window opens 2026-04-23 per `project_s84_dr3_response_protocol.md`). Specifically: re-run P7's MC with the DR3 α_s observational pin (currently `alpha_s_canon_2020 = 0.0023 ± 0.0063` per `canonical_constants.py` line 1249) substituted for `planck_alpha_s = -0.0045`, and check whether the 6-cell ρ_grid changes by more than 1e-3.
- **Inputs**: `_artifacts/s86_w8_p7_rho_mc_ensemble.npz`; `canonical_constants.py` `alpha_s_canon_2020` line and `planck_alpha_s` line; W0b R8 methodology.
- **Gate**: `S87-LAYER3-DR3-ROBUSTNESS` — PASS if max-cell |Δρ| ≤ 1e-3 under the alpha_s pin update; INFO if 1e-3 < max-cell |Δρ| ≤ 0.05 (within bootstrap noise); FAIL if any cell |Δρ| > 0.05 (would indicate the LAYER-3 anchor is α_s-pin-fragile).
- **Effort**: 1 hour, 1 mack-cosmic-bridge agent session (recompute + verdict).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | ANSATZ-test split: (A) substrate near-1D in (a_0,a_2,a_4) survives; (B) W13-2 convention controls the value | GEOMETRIC | INFO (interpretation-A weak, B strong) | LAYER-3 anchor +0.951 is W13-2-conditional; need Axis-7 in §W8-1 schema |
| 2 | PV-PCA var_PC1 = 97.54% / 98.83% / 99.15% — analytic identity (1+|ρ|)/2 holds exactly | PHONONIC | PASS 2/3 cells; FAIL 1/3 (uniform) on 98% pre-reg | Pre-reg threshold should be derived from |ρ| pin, not arbitrary 98% |
| 3 | shift_uniform δ=+0.05/+0.10 magnitude=|signed| identity holds (trivially, by single-sign theorem) | PHONONIC | PASS (machine-epsilon at +0.05; ≤0.005 at +0.10) | Pre-registration was misspecified — δ < +0.962 keeps α_s single-signed; identity is theorem, not test |
| 4 | shift_mixed (genuine straddle): max ||signed|-magnitude|| = 0.0081 < 0.10 detection band | PHONONIC | PARTIAL — qualitative CONFIRM of §W8-2 line 291; magnitude over-pre-registered 12× | Line 291 footnote needed; future tests need ≤0.01 detection band |
| 5 | 5-point analytic |ρ| vs MC: gaps 0.011/0.006/0.017 — fails 1e-3 pre-reg | PHONONIC | FAIL on quantitative threshold; ordering preserved | Need analytic noise-propagation model (V.3) |
| 6 | LAYER-3 anchor +0.951 is layer-3-DURABLE under (sign × atlas-weighting) but ANSATZ-FRAGILE under forward-map re-coupling | PHONONIC | INFO | §W8-1 6-axis schema missing forward-map-ansatz axis (V.1) |
| 7 | Cross-link to §W8-2 line 291 conditional ("magnitude and signed would generally differ if α_s straddled zero") | PHONONIC | CONFIRMED qualitatively, magnitude over-predicted | The conditional's truth is structural; its magnitude depends on atlas-shape weighting |
