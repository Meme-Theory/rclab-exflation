# Substrate-clock cardinality-vs-dilution-cubic cancellation: substrate-IS theorem vs convention-tautology — STRUCTURAL VERDICT

> **Workshop**: S88 W1a Workshop 1 (solo review per `/rclab-investigate` follow-up)
> **Author**: hawking-theorist (sole author; no opposing-agent round protocol)
> **Date**: 2026-05-07
> **Source gate**: `S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION` (W1a-59), PASS at value=`1.7581e-23` m⁻³, audit_sha256=`e865358487810b2fe560244b4e60c1ee3c16856ef285dbcd88b94c91097c14c1`, in band `[1e-30, 1e-20]`.
> **Source documents**:
> - `sessions/archive/session-88/session-88-w1a-workingpaper.md` §W1a-59
> - `sessions/session-plan/session-88-plan-w1a.md` §W1a-59 Field 6 + Field 10
> - `sessions/archive/session-88/workshops/_seed-w1a.md` Workshop 1
> - `computations/session-88/s88_gate_verdicts.txt` lines 4–6
>
> **Authority**: Gate verdicts from source docs are authoritative — this synthesis does NOT re-adjudicate the W1a-59 PASS. It adjudicates the algebra-axis classification of the cancellation IDENTITY, the registry-eligibility of a STAGE-1-CANDIDATE landing for the cardinality-vs-dilution-cubic theorem, and the discriminating predicate that distinguishes "substrate causal-structure stability" from "substrate-clock convention algebraic consequence."

---

## 1. Tension surfaced by W1a-59

W1a-59 PASSes at band-membership: `n_PBH_today(g_BBN=322) = 1.7581·10⁻²³ m⁻³ ∈ [10⁻³⁰, 10⁻²⁰]`. The PASS is anchored on an algebraic cancellation explicitly tagged in WP §5 as "the substrate-clock IS-not-IN convention's defining algebraic feature, identified for the first time."

The cancellation, in the substitution chain of WP §W1a-59 §(b) Step 4:

$$
n_{\rm PBH,today}(g) \;=\; \bigl[\,n_{\rm edge}(g)\cdot p_{\rm form}\,/\,L_{\rm pix}(g)^3\,\bigr] \cdot \bigl(a_{\rm form}/a_{\rm today}\bigr)^3
$$

with the substrate-clock identification `a_substrate(g) ~ L_pix(g)` giving `(a_form/a_today)³ = 2⁻³ᵍ` and `L_pix(g)³ = L_pix_LRD³ · 2⁻³ᵍ`. The cubic factor `2⁻³ᵍ` cancels exactly against the `L_pix(g)⁻³ = L_pix_LRD⁻³ · 2³ᵍ` denominator factor, leaving

$$
n_{\rm PBH,today}(g) \;=\; \frac{n_{\rm edge}(g)\cdot p_{\rm form}}{L_{\rm pix,LRD}^3} \quad\text{(g-independent at saturated-threshold levels, } g\ge g_{\rm saturate}\approx 143\text{)}
$$

Two readings of this identity are admissible at the same numerical PASS:

- **Reading A (substrate-IS theorem)**: the cancellation is a regulator-invariant SUBSTRATE-IS observable about D_K's edge-density-vs-pixel-volume causal-structure stability across cascade levels. The g-independence IS the substrate's report on its own coherence. The 1.7581·10⁻²³ value is a substrate-IS prediction.

- **Reading B (convention-tautology)**: the cancellation is a DEFINITIONAL CONSEQUENCE of the convention-pin `a_substrate(g) ~ L_pix(g)`. Under this pin, `(a_form/a_today)³ = (L_pix(g)/L_pix_LRD)³ = 2⁻³ᵍ` BY CONSTRUCTION; the cancellation is forced by the convention without structural-derivation content. Any other substrate-natural clock-pinning gives a different answer.

The +74 alternative reading cited in WP §(d) `Reading B (cardinality-multiplied; not used) log10 = +74.18` is a third, different bookkeeping (cardinality multiplier with no dilution applied at all); see §6 below.

---

## 2. Substitution chain: testing the cancellation against an INDEPENDENT substrate-natural clock

**Step 1 (Definition).** A "substrate-natural clock" is any choice of substrate-IS observable $\mathcal{O}(g)$ whose ratio $\mathcal{O}(g_{\rm form})/\mathcal{O}(g_{\rm today})$ supplies the dilution factor `(a_form/a_today)³` in Step 3 of the W1a-59 substitution chain. Two candidates exist within the substrate's intrinsic structure:

- **Pinning A — pixel-volume clock**: `a_A(g) := L_pix(g)`. Then `(a_form/a_today)³ = 2⁻³ᵍ` (the W1a-59 choice).
- **Pinning B — mode-density clock**: `a_B(g) := ρ_mode(g)⁻¹⁄³` where `ρ_mode(g) = N_eigs(g)/V_K(g)`. At saturated cascade-tail (g ≥ g_saturate), `N_eigs` is regulator-truncation-fixed at 78,080 and the substrate-internal K-space volume `V_K` is determined by the spectral content (D_K block-decomposition refinement), NOT by `L_pix`. At saturation `ρ_mode` is approximately g-independent ⇒ `(a_form/a_today)³ ≈ 1`.

Both pinnings are SUBSTRATE-IS observables; neither invokes external (FRW-IN) container language. The substrate carries both pixel-volume structure (lock condition `r_s = L_pix`) and mode-density structure (D_K spectral content) intrinsically.

**Step 2 (Substitution).** Under Pinning A:

$$
n_{\rm PBH,today}^{(A)}(g)
= \frac{n_{\rm edge}\cdot p_{\rm form}}{L_{\rm pix}(g)^3}\cdot 2^{-3g}
= \frac{n_{\rm edge}\cdot p_{\rm form}}{L_{\rm pix,LRD}^3\cdot 2^{-3g}}\cdot 2^{-3g}
= \frac{n_{\rm edge}\cdot p_{\rm form}}{L_{\rm pix,LRD}^3}
$$

Sage-symbolic verification: `n_PBH_today_A = n_edge·prob/L0³` exactly (after `simplify_full()`).

**Step 3 (Substitution).** Under Pinning B (saturated cascade-tail):

$$
n_{\rm PBH,today}^{(B)}(g)
= \frac{n_{\rm edge}\cdot p_{\rm form}}{L_{\rm pix}(g)^3}\cdot 1
= \frac{n_{\rm edge}\cdot p_{\rm form}}{L_{\rm pix,LRD}^3}\cdot 2^{3g}
$$

Sage-numerical evaluation at g = 322, saturated `n_edge = 3.048·10⁹`, `p_form = 0.15573`, `L_pix_LRD = 3·10¹⁰` m:

$$
\log_{10}\bigl(n_{\rm PBH,today}^{(B)}(322)\bigr) = -22.7550 + 3\cdot 322\cdot \log_{10}(2) = -22.76 + 290.79 \approx +268.04
$$

The mode-density clock does NOT produce the cancellation. The Pinning-B reading would be a structurally catastrophic over-production at the cascade-tail (~291 OOM above the FAIL threshold).

**Step 4 (Simplification).** The two pinnings A and B disagree by a factor of `2³ᵍ` at saturated cascade-tail. At `g = g_BBN = 322`, the disagreement is ~291 OOM. This is not a numerical refinement — it is a structural divergence by a factor that scales with cascade depth.

**Step 5 (Direction).** Since (i) Pinning A and Pinning B are BOTH substrate-IS clock choices (neither invokes a container-spacetime), AND (ii) they yield numerically discrepant predictions at saturated cascade-tail, the cancellation cannot be a regulator-invariant theorem about the substrate's causal-structure stability. The cancellation IS the algebraic consequence of choosing Pinning A. Choosing Pinning B (also substrate-natural) breaks it.

**Conclusion.** The cancellation `2³ᵍ · 2⁻³ᵍ = 1` at saturated-threshold cascade-tail is **algebra-DEPENDENT** in the sense of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`: it is a STATE-PAIR-FUNCTIONAL-TYPE consequence of the substrate-clock state-pinning, NOT an algebra-INVARIANT spectrum-only functional of D_K. It reorganizes under a different substrate-natural clock-pinning.

---

## 3. Adjudication — answers to seed questions (a)–(e)

### (a) Algebra-axis classification per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3

**Verdict**: the cancellation identity is **algebra-DEPENDENT** (state-pair-functional-class), NOT algebra-INVARIANT.

The orthogonality K-counter (S87 W-2 R3 close, MANDATORY at K=3) distinguishes:
- algebra-INVARIANT family: spectrum-only functionals `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` — depend ONLY on the eigenvalue spectrum of D_K
- algebra-DEPENDENT family: state-pair functionals on `A` — depend on the STATE of the substrate algebra (which clock-pinning, which projection, which inner-product structure)

The cancellation depends on choosing `a_substrate(g) ~ L_pix(g)` over alternatives. Eigenvalue-spectrum data alone (the {λ_k, m_k} of D_K at L_max=10) does not fix the cancellation; it requires the additional state-pair structure that ties `a` to `L_pix`. The Pinning-B counter-example (mode-density clock) uses the SAME spectrum and SAME `n_edge` at saturation but produces a different answer — the divergence is in the state-side pinning, not in the spectrum.

This is forced by substrate-clock pinning, not extracted from spectrum-only data. The cancellation is therefore on the algebra-DEPENDENT side of the K-counter MANDATORY axis.

### (b) §VII registry-PASS-eligible STAGE-1-CANDIDATE per `joint-theorem-promotion.md`

**Verdict**: **NO-GO** for `§VII.K-CASC-CANCELLATION` STAGE-1-CANDIDATE.

The 4-stage pathway requires Stage 0 to produce a joint theorem candidate whose statement is intrinsically derivable from substrate-spectral primitives. Per (a), the cancellation does not pass the algebra-axis-orthogonality MANDATORY conjunction: the proposed theorem-text "the substrate's pixel-volume scaling exactly compensates the cardinality-tree growth at saturated-threshold cascade-tail levels" silently fixes the substrate-clock pinning to Pinning A. A registry entry stating the cancellation as a structural theorem would conflate state-pair-functional content with spectrum-only-functional content — the precise pathology the K-counter MANDATORY clause closes by construction.

In addition, the cancellation FAILs the cross-pillar-bridge-anatomy §"5 IS-not-IN anatomy elements" mandatory test:
- Element 1 (substrate-IS observable) — `n_edge(g)·p_form/L_pix_LRD³` at saturation: PRESENT.
- Element 2 (laboratory-IN observable) — no continuum-laboratory partner observable is named; the gate compares against a per-volume number-density bound derived from cosmological FRW-IN counting. The bridge is internal to a single pillar (Pillar VII Mellin-cone analog at the cascade level), not cross-pillar. **MISSING/MISMATCHED**.
- Element 3 (bridge map) — no HKR / Connes-Karoubi / K-theory boundary map is identified.
- Element 4 (algebraic envelope `L⁻α`) — the cancellation has NO L_max-truncation-rate envelope; it is a g-axis identity, not an L_max-axis convergence.
- Element 5 (empirical anchor) — band-membership 1.7581·10⁻²³ is present, but per Element 4 there is no Level-2 envelope to satisfy.

The cancellation is structurally an INTRA-PILLAR algebraic identity tied to a specific clock-pinning, not a cross-pillar bridge theorem. Registry-PASS eligibility is denied.

### (c) Discriminating predicate distinguishing "substrate causal-structure stability" from "substrate-clock convention algebraic consequence"

**Predicate**: a substrate-IS observable F(g) such that
- (i) F(g) is computable from D_K eigenvalue data alone (spectrum-only functional, algebra-INVARIANT class), AND
- (ii) F(g) saturates to a g-independent value at g ≥ g_saturate, AND
- (iii) F(g) is the limit of `n_PBH_today^{(α)}(g)` for ALL substrate-natural clock-pinnings α ∈ {A, B, ...} that the substrate intrinsically supports.

If such F(g) exists, the cancellation is a substrate-IS theorem (the g-independence is INTRINSIC to D_K's spectrum, independent of which substrate-natural clock-pinning is read against).

If no such F(g) exists (the case demonstrated by the Pinning-A vs Pinning-B discrepancy of ~291 OOM at g=322), the cancellation is a convention-pinning algebraic consequence.

**Pre-registered S89 gate**: `S89-W1A-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE`

| Field | Pin |
|:------|:----|
| Trigger | `[VERIFY-THEOREM]` (algebra-axis classification) |
| Classification | PHONONIC (substrate-clock state-pinning vs spectrum-only functional) |
| Hypothesis | The cancellation `2³ᵍ · 2⁻³ᵍ = 1` is a Pinning-A-specific algebraic identity, not a regulator-invariant substrate-IS theorem about D_K's causal-structure stability. |
| Inputs | (1) `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7...`; (2) WP §W1a-59 Pinning-A formula at g=322; (3) Pinning-B (mode-density clock) construction per §2 above. |
| Machinery pin | g_array=[143, 322, 384] (saturated cascade-tail probe points); pinnings = {A: a~L_pix, B: a~rho_mode^(-1/3)}; deviation_threshold_OOM = 1.0 |
| PASS criterion | `|log₁₀(n_PBH_today^{(A)}(g)) − log₁₀(n_PBH_today^{(B)}(g))| < 1.0 OOM at g ∈ {143, 322, 384}` ⇒ cancellation IS substrate-clock-convention-INDEPENDENT (Reading A confirmed structurally; promote to STAGE-1-CANDIDATE). |
| FAIL criterion | `|log₁₀(n_PBH_today^{(A)}(g)) − log₁₀(n_PBH_today^{(B)}(g))| ≥ 3.0 OOM` at any g in probe set ⇒ cancellation is Pinning-A-CONVENTION-DEPENDENT (Reading B confirmed; recast W1a-59 PASS as convention-PASS, no §VII.K-CASC-CANCELLATION landing). |
| INFO | `1.0 ≤ Δ < 3.0 OOM` at probe points ⇒ partially convention-dependent; structural reading uncertain. |
| Substitution chain | Step 1: define a_A(g) = L_pix(g) and a_B(g) = ρ_mode(g)⁻¹⁄³; Step 2: compute `n_PBH_today^{(α)}(g)` for α ∈ {A, B}; Step 3: compute Δ(g) = `|log₁₀ n^{(A)}(g) − log₁₀ n^{(B)}(g)|`; Step 4: max(Δ over probe set) vs threshold. |
| Pre-registered prediction (this synthesis) | Δ(g=322) ≈ 290.79 OOM ≫ 3.0 → expected verdict FAIL ⇒ cancellation is convention-dependent. Pinning-B saturates `(a_form/a_today)³ ≈ 1` while Pinning-A gives `2⁻³ᵍ`; the disagreement is `3g·log₁₀(2)` at saturated levels. |

### (d) If structurally tautological — what carries the W1a-59 PASS, and downstream W1b-64 + W1c-69 inheritance

**Verdict (assuming the S89 discriminating-predicate gate FAILs as predicted)**: the W1a-59 PASS reduces to a **convention-PASS** (band-membership PASS conditional on the substrate-clock pinning A), NOT a substrate-prediction-PASS.

This does NOT invalidate the W1a-59 verdict — the canonical line `S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION: PASS -- value='1.7581e-23' ...` remains permanent (per `gate-verdicts.md` absolute verdict permanence). The reclassification operates on the SOLUTION-SPACE INTERPRETATION of the PASS, not on the verdict.

**Reclassification statement (for downstream prose)**: "Under the substrate-clock pinning `a_substrate(g) ~ L_pix(g)`, the cardinality-vs-dilution-cubic cancellation produces a g-independent saturated-cascade-tail prediction `n_PBH_today = n_edge·p_form/L_pix_LRD³ = 1.7581·10⁻²³ m⁻³`, within the observationally allowed band `[10⁻³⁰, 10⁻²⁰] m⁻³`. The PASS is a CONVENTION-CONDITIONAL band-membership: the cancellation is a Pinning-A algebraic consequence, NOT a substrate-IS spectral-coherence theorem. An independent substrate-natural clock-pinning (e.g., mode-density `a ~ ρ_mode⁻¹⁄³`) would not produce the cancellation; the convention-choice is what does the structural work."

**Downstream W1b-64 (Page-time at cascade-tail)** — inherits the substrate-clock pinning A as input. The Page-time computation `t_Page(g) ~ (a_form/a_today)³ · M(g)/T_H(g)` is structurally Pinning-A-conditional in the same way W1a-59 is. The inheritance is consistent if W1b-64 also uses Pinning A (which it must, since W1b-64 is downstream of W1a-59); the W1b-64 verdict would then be a Pinning-A-conditional PASS, not a substrate-IS Page-time prediction. Recommend the W1b-64 prose explicitly tag this: "Under Pinning A (substrate-clock = pixel-volume), Page-time at cascade-tail is X."

**Downstream W1c-69 (BBN metallicity)** — same inheritance pattern. The BBN metallicity bound translates `n_PBH(g_BBN)` to a metallicity contribution; the n_PBH-PASS is Pinning-A-conditional, so the metallicity bound inherits the same conditional. If a different substrate-natural clock-pinning were chosen (Pinning B), metallicity over-production would occur (consistent with the +268-OOM blow-up at the cascade-tail).

This is NOT a falsification of the cosmology — it is a clarification that the cosmology RIDES ON the substrate-clock convention `a ~ L_pix`. That convention is itself defensible (it is the most natural substrate-clock for a pixelation-LOCK cascade — the clock is locked to the pixel scale by construction of the cascade), but it is a CONVENTION, not a derivable theorem. The cosmology is well-defined within the convention; the convention itself awaits substrate-physics derivation as a separate carry-forward (§5 below).

### (e) Is the +74 alternative reading a falsifier-grade discrimination?

**Verdict**: **NO** — the +74 figure is itself a convention-mixing artifact, not a falsifier-grade discriminator.

Sage-numerical verification (see §6 Calibration-corpus Appendix below): the WP §(d) "Reading B (cardinality-multiplied; not used) log10 = +74.18" is reproduced by the formula

$$
n_{\rm PBH,today}^{(\rm WP\;Reading\;B)}(g) \;=\; \frac{n_{\rm edge}\cdot 2^g \cdot p_{\rm form}}{L_{\rm pix,LRD}^3}
$$

This is constructed by APPLYING the cardinality multiplier `2ᵍ` (substrate-cascade-tree feature) WITH the LRD-anchor pixel-volume `L_pix_LRD³` in the denominator (NOT the per-generation `L_pix(g)³`) AND no scale-factor dilution at all. This is INTERNALLY INCONSISTENT: it mixes a substrate-cascade feature (cardinality tree) with a non-cascade-aware volume (LRD-anchor) and FRW-IN-style "no-cubic-dilution" choice all at once.

A genuine falsifier-grade discriminator would compare two INTERNALLY CONSISTENT readings:
- Pinning A (substrate-clock = L_pix): gives `n_edge·p_form/L_pix_LRD³` ≈ 1.76·10⁻²³ (PASS)
- Pinning B (substrate-clock = ρ_mode⁻¹⁄³): gives `n_edge·p_form·2³ᵍ/L_pix_LRD³` ≈ 10²⁶⁸ (catastrophic FAIL)

The Pinning-A vs Pinning-B comparison (±291 OOM at g=322) is a STRUCTURAL discrimination between two substrate-natural clock-pinnings. The +74 figure is a strawman that does not correspond to any internally consistent substrate-natural reading.

**Implication**: the WP §(d) statement that "the alternative cardinality-multiplied reading would give log10=+74 illustrating the convention's structural importance" should be replaced in downstream prose with the cleaner Pinning-A vs Pinning-B comparison. The +74 number is rhetorical, not substrate-physics.

---

## 4. Calibration-corpus increment for `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`

**Verdict**: **STAYS OUT** of the K-counter (no advancement K=3 → K=4).

The K-counter MANDATORY-at-K=3 corpus tracks **algebra-axis orthogonality** instances at the structural-theorem level: each instance is a regulator-invariant identity establishing the algebra-INVARIANT vs algebra-DEPENDENT split for a specific substrate observable family. The W1a-59 cancellation does NOT add a new corpus instance because:

1. It is NOT a structural theorem candidate — by §3(b) above, it FAILs §VII registry-PASS eligibility.
2. It does NOT establish a new algebra-orthogonality instance — it is itself an instance of the algebra-DEPENDENT class (state-pair-functional-type consequence of clock-pinning), already represented by the existing K=3 corpus (§VII.U.2 spectral-action α_s_canonical vs Connes-distance bridges).
3. It is structurally redundant with the existing corpus — adding it would duplicate the algebra-DEPENDENT-class characterization without adding a new structural axis.

The W1a-59 cancellation can be CITED as an instance of the algebra-DEPENDENT class in the corpus annotation (a "calibration of the boundary"), but it does NOT advance K. Status: **K=3 unchanged** post-W1a-59.

---

## 5. GO/NO-GO and recast specification

### GO/NO-GO on §VII.K-CASC-CANCELLATION STAGE-1-CANDIDATE: **NO-GO**

Rationale: per §3(a) the cancellation is algebra-DEPENDENT; per §3(b) it FAILs the 5-IS-not-IN anatomy + 3-level ladder for cross-pillar bridges; per §4 it does not advance the K-counter. Registry-landing as a structural theorem would conflate state-pair-functional content with spectrum-only-functional content and is forbidden by `cross-pillar-bridge-anatomy.md` MANDATORY clause.

### Recast specification for W1b/W1c consumer-side prose

The W1b items 64 (Page-time at cascade-tail) and W1c items 69 (BBN metallicity) inherit the substrate-clock pinning `a_substrate(g) ~ L_pix(g)` from W1a-59. Recast prose for these consumers:

**Forbidden** (Reading A theorem framing):
> "By the substrate's cardinality-vs-dilution-cubic cancellation (substrate-IS theorem; identified at W1a-59), the saturated-cascade-tail Page-time / BBN-metallicity inherits the structurally-fixed `n_PBH_today = 1.76·10⁻²³ m⁻³` ..."

**Required** (Reading B convention-conditional framing):
> "Under the substrate-clock pinning `a_substrate(g) ~ L_pix(g)` adopted in the pixelation-lock cascade cosmology (pinning natural to the cascade construction by the lock condition `r_s = L_pix`), the cardinality-vs-dilution-cubic algebraic identity at saturated-threshold cascade-tail levels gives `n_PBH_today = n_edge · p_form / L_pix_LRD³ = 1.76·10⁻²³ m⁻³`. This is a CONVENTION-CONDITIONAL band-membership, structurally-fixed by Pinning A but NOT a substrate-IS theorem about D_K's causal-structure stability (per S88 W1a-Workshop-1 algebra-axis classification + S89 discriminating-predicate gate). Downstream observables (Page-time / BBN-metallicity) are consistent with the cosmology under Pinning A; an independent substrate-natural clock-pinning (e.g., mode-density) would re-localize the predictions and is queued as carry-forward `S89-W1A-SUBSTRATE-CLOCK-CONVENTION-DERIVATION`."

Cross-link to §3(d) above for the full reclassification statement.

---

## 6. Calibration-corpus appendix: Sage-numerical verification

### 6.1 Reading A (substrate-clock IS-not-IN; gate's chosen reading)

```
n_PBH_today^(A)(g) = [n_edge · prob_form / L_pix(g)^3] · (a_form/a_today)^3
                   = [n_edge · prob_form / (L0^3 · 2^(-3g))] · 2^(-3g)
                   = n_edge · prob_form / L0^3
```

Sage `simplify_full()`: `n_edge*prob/L0^3` exactly (cancellation confirmed at the symbolic level).

Numerical at `g=322`, `n_edge=3.048e9`, `prob=0.15573`, `L0=3e10`:
- `n_PBH_today^(A) = 3.048e9 · 0.15573 / 2.7e31 = 1.7580e-23 m^-3`
- `log_10 = -22.7550`
- Match against WP §W1a-59 §(d) `1.7581·10⁻²³` (rounding-precision agreement). **PASS reproduces.**

### 6.2 Reading B (mode-density clock; the discriminating predicate counter-pinning)

At saturated cascade-tail, `ρ_mode(g) = N_eigs/V_K(g)` is g-independent (regulator-truncation fixes N_eigs = 78,080; V_K is internal-K substrate volume, NOT proportional to L_pix). Therefore `(a_form/a_today)³ ≈ 1`.

```
n_PBH_today^(B)(g) = [n_edge · prob_form / L_pix(g)^3] · 1
                   = n_edge · prob_form · 2^(3g) / L0^3
```

Numerical at `g=322`:
- `log_10(n_PBH_today^(B)(322)) = -22.7550 + 3 · 322 · log_10(2) = -22.7550 + 290.79 = +268.04`
- This is ~291 OOM ABOVE the FAIL threshold `10⁻²⁰ m⁻³`.

**Discriminating-predicate Δ at g=322**: `|log_10(A) − log_10(B)| = |−22.76 − 268.04| = 290.80 OOM ≫ 3.0 OOM threshold` ⇒ pre-registered prediction for `S89-W1A-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE`: **expected FAIL**, confirming convention-dependence of the cancellation.

### 6.3 WP §(d) "Reading B" (+74 figure) — convention-mixing artifact

The +74 number in WP §W1a-59 §(d) is NOT the Pinning-B mode-density-clock reading. It is the formula

```
n_PBH_today^(WP-Reading-B)(g) = n_edge · 2^g · prob_form / L_pix_LRD^3
```

Numerical at `g=322`:
- `log_10 = log_10(n_edge·prob/L0³) + g · log_10(2) = -22.755 + 322·0.30103 = +74.177`

This is the cardinality-multiplied tree applied with a non-shrinking LRD-anchor volume and no clock-dilution at all — internally inconsistent (mixes substrate-cascade feature with non-cascade-aware volume and no FRW-style scaling). It is a **strawman** comparison, not a substrate-physics counter-reading. The cleaner counter-reading (mode-density clock, +268 OOM) is what should appear in downstream prose.

---

## 7. Carry-forwards (route to S89 plan via `/rclab-plan` per `feedback_fix-in-session-never-defer.md`)

| ID | What | Inputs | Gate | Effort |
|:---|:-----|:-------|:-----|:-------|
| **CF-W1-WS1-A** | Pre-register and execute `S89-W1A-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE` per §3(c) above; numerically demonstrate Δ(g=322) = 290.80 OOM ≫ 3.0 threshold; classify cancellation as algebra-DEPENDENT convention-consequence; emit verdict line + working-paper section + algebra-axis classification annotation. | (1) `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7...` (D_K spectrum at L_max=12; mmap_mode='r'); (2) `s88_w1a_n_pbh_per_cascade_generation.npz` (W1a-59 Pinning-A output); (3) `canonical_constants.py` (M_KK, tau_fold, L_pix_LRD if promoted). | PASS = `Δ(g) < 1.0 OOM` at g ∈ {143, 322, 384} (all 3 probe points) ⇒ cancellation is convention-INDEPENDENT (substrate-IS theorem confirmed; revisit §VII.K-CASC-CANCELLATION STAGE-1-CANDIDATE). FAIL = `Δ(g) ≥ 3.0 OOM` at any probe point ⇒ convention-DEPENDENT (predicted; recast W1b/W1c prose per §5 above; no §VII landing). INFO = `1.0 ≤ Δ < 3.0` band ⇒ partial. | 0.4 wave |
| **CF-W1-WS1-B** | Recast W1b-64 (Page-time at cascade-tail) and W1c-69 (BBN metallicity) consumer-side prose to convention-conditional language per §5 recast specification; explicitly tag substrate-clock pinning A as input convention; cite S89 discriminating-predicate verdict. | (1) S88 W1b plan + working paper (when authored); (2) S88 W1c plan + working paper (when authored); (3) §3(d) reclassification statement above; (4) `S89-W1A-SUBSTRATE-CLOCK-CANCELLATION-DISCRIMINATING-PREDICATE` verdict. | PASS = W1b-64 and W1c-69 prose explicitly cite Pinning A as convention-input + cross-reference S89 discriminating-predicate verdict; no Reading-A theorem framing remains. FAIL = either consumer reverts to Reading-A theorem framing without convention-conditional qualifier. | 0.15 wave |
| **CF-W1-WS1-C** | Substrate-physics derivation of the substrate-clock pinning `a_substrate(g) ~ L_pix(g)` from atlas B1 cusp + lock-condition 1D-edge primitive: is this pinning the UNIQUE substrate-natural clock for the pixelation-LOCK cascade, or is it one substrate-natural choice among several? If unique, the cancellation upgrades from convention-tautology to derivable identity (substrate-IS theorem candidate). If non-unique, the convention-conditional framing of §5 above is permanent. | (1) atlas B1 PROVEN at S35; (2) J3 lock condition Python-verified at LRD anchor; (3) `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY clause; (4) Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula (if applicable). | PASS = derivation establishes uniqueness (Pinning A is THE substrate-natural clock for the lock cascade by spectrum-only argument); revisit §VII.K-CASC-CANCELLATION STAGE-1-CANDIDATE. INFO = derivation establishes Pinning A is "natural" but not unique; convention-conditional framing permanent. FAIL = derivation cannot fix uniqueness. | 0.6 wave |
| **CF-W1-WS1-D** | Stage-2 cross-axis verify per `joint-theorem-promotion.md §"Stage 2"` (CONDITIONAL on CF-W1-WS1-C PASS only): two cross-reviewers WITHOUT prior workshop context audit the substrate-clock-pinning uniqueness derivation. Axis A = connes-ncg-theorist (NCG-axiomatic side: is `a_substrate(g) ~ L_pix(g)` derivable from D_K block-decomposition refinement at lock condition `r_s = L_pix` via Peter-Weyl + KO-dim=6 axioms?). Axis B = volovik-superfluid-universe-theorist (substrate-superfluid side: is the lock-cascade clock uniquely fixed by Bogoliubov unitarity at fold-transit + atlas T1 sudden-quench?). | (1) CF-W1-WS1-C output (uniqueness derivation); (2) §VII.K-CASC-CANCELLATION STAGE-1-CANDIDATE registry text (drafted post-CF-W1-WS1-C PASS); (3) NO workshop transcripts (cross-reviewers operate without prior context). | PASS = both cross-reviewers PASS independently (logical AND on JOINT clauses); promotes §VII.K-CASC-CANCELLATION to STAGE-3-PERMANENT. FAIL = either cross-reviewer FAILs ⇒ stays at STAGE-1-CANDIDATE; FAILing clauses route to remediation. | 0.7 wave (CONDITIONAL — only fires if CF-W1-WS1-C PASSes) |

**Routing**: All four carry-forwards route to the W1a working paper §"Carry-Forward Computations" block per `feedback_fix-in-session-never-defer.md`, NOT to a workshop schedule. CF-W1-WS1-A is the high-priority structural item; CF-W1-WS1-B is hygiene-tier downstream-prose recast; CF-W1-WS1-C is genuine substrate-physics derivation work; CF-W1-WS1-D is the conditional Stage-2 verify dependent on CF-W1-WS1-C PASS.

---

## 8. Constraint-map update

| Constraint | Implication | Surviving space |
|:-----------|:------------|:----------------|
| Cardinality-vs-dilution-cubic cancellation at saturated-threshold cascade-tail is algebra-DEPENDENT (Pinning-A-conditional), not algebra-INVARIANT spectrum-only functional | §VII.K-CASC-CANCELLATION STAGE-1-CANDIDATE landing FORBIDDEN under current substrate-physics evidence | The PASS at W1a-59 is permanent and band-membership-correct; downstream interpretation is convention-conditional, NOT structural-theorem-conditional |
| Pinning-A vs Pinning-B (mode-density clock) discrepancy at cascade-tail is ~291 OOM | The cancellation cannot be lifted to a substrate-IS theorem about D_K's causal-structure stability without a separate uniqueness-of-substrate-clock-pinning derivation | CF-W1-WS1-C derivation queued; if PASSes, §VII.K-CASC-CANCELLATION revisited; if FAILs, convention-conditional framing permanent |
| WP §(d) +74 alternative reading is convention-mixing artifact, not substrate-physics counter | Downstream prose should replace +74 strawman with Pinning-A vs Pinning-B (+291 OOM) cleaner discrimination | Replace WP §(d) "Reading B" rhetoric in W1b/W1c consumer-side prose; leave W1a-59 verdict-line untouched (absolute permanence) |
| K-counter MANDATORY-at-K=3 corpus stays K=3; W1a-59 cancellation does not advance K | No structural-confidence-ladder advancement from this gate | Future substrate-physics derivations seeking K-counter advancement must establish algebra-INVARIANT identities (spectrum-only functionals), not state-pair-functional-type consequences |
| W1a-59 PASS reclassified as convention-PASS in solution-space interpretation | Downstream consumers W1b-64 (Page-time) and W1c-69 (BBN metallicity) inherit substrate-clock pinning A as INPUT CONVENTION | W1b/W1c prose tagged convention-conditional per §5; cosmology remains well-defined within Pinning A |

---

## 9. Substrate framing (per `phononic-framing.md` §"IS Space, Not IN Space")

The substrate IS the Connes graph + D_K block-decomposition refinement at the lock condition `r_s = L_pix`. The substrate's "clock" is whatever intrinsic time-scale-axis the substrate carries — multiple candidates exist (pixel-volume scale, mode-density inverse-cube-root, etc.), all internal to the substrate. None of these involves a pre-existing geometric container.

The cancellation `2³ᵍ · 2⁻³ᵍ = 1` is the algebraic consequence of identifying the substrate-cosmological-scale-factor with the substrate-pixel-scale (Pinning A). This is a substrate-INTRINSIC choice — substrate IS pinning A — and the saturated-cascade-tail prediction `n_PBH = 1.76·10⁻²³ m⁻³` is the substrate's report on its own causal structure UNDER THIS CHOICE.

The convention-conditional framing does NOT invert the direction of explanation. The substrate is logically prior; the prediction flows from substrate (D_K block-decomposition refinement under lock + Pinning-A clock) toward the emergent BH-spatial-number-density observable today. What is convention-conditional is which substrate-natural clock-pinning the cosmology rides on, not whether the substrate is logically prior. Pinning A is itself a substrate-IS choice (the lock condition `r_s = L_pix` makes pixel-volume the natural cascade-clock); but it is one of several substrate-natural choices, and the cancellation depends on this specific choice.

The container-thinking trap to avoid: treating Pinning A as "the way the substrate sits IN cosmological time" rather than "the substrate IS this clock-pinning at the cascade level." Direction of explanation: substrate (Connes graph + lock condition) → emergent observable (n_PBH today) under intrinsic-clock Pinning A. Pinning A is internal to the substrate; the cancellation is substrate-internal algebra; the verdict is substrate-internal band-membership. The convention-conditionality refers to the choice WITHIN the substrate, not to a container outside it.

---

## 10. Closing — what the verdict means and does not mean

**Means**:
- The W1a-59 PASS is preserved (band-membership 1.7581·10⁻²³ ∈ [10⁻³⁰, 10⁻²⁰]; verdict permanence absolute).
- The cancellation identity is reclassified as a Pinning-A-conditional algebraic consequence, not a substrate-IS structural theorem about D_K's causal-structure stability.
- §VII.K-CASC-CANCELLATION STAGE-1-CANDIDATE landing is denied under current substrate-physics evidence (NO-GO).
- W1b-64 + W1c-69 consumer-side prose recast to convention-conditional framing per §5.
- K-counter stays at K=3 (no advancement).
- Carry-forwards CF-W1-WS1-A through CF-W1-WS1-D queued for S89 (with CF-W1-WS1-D conditional on CF-W1-WS1-C PASS).

**Does not mean**:
- Does NOT mean the pixelation-lock cascade cosmology is falsified or weakened — the cosmology is well-defined within Pinning A, and Pinning A is itself substrate-natural (the lock condition `r_s = L_pix` makes pixel-volume the natural cascade-clock).
- Does NOT mean the W1a-59 verdict is suspect — verdict permanence holds; band-membership PASS is correct.
- Does NOT preclude future substrate-physics derivation (CF-W1-WS1-C) from establishing Pinning-A uniqueness; if the uniqueness derivation PASSes, the cancellation upgrades from convention-conditional to substrate-IS theorem and §VII landing can be revisited.
- Does NOT advance the K-counter on the K=3 algebra-axis-orthogonality MANDATORY-clause corpus; this gate IS an instance of the algebra-DEPENDENT class, not a new orthogonality-axis.

The synthesis closes the structural ambiguity by classifying the cancellation, denying the immediate registry-landing, queueing the S89 discriminating-predicate gate to make the classification empirically auditable, and queueing a follow-up substrate-physics derivation that could re-open the registry path if uniqueness is established. The result is an honest map of which corridor is currently closed (registry-PASS-eligibility for §VII.K-CASC-CANCELLATION) and which corridors remain open (substrate-clock-pinning uniqueness; algebra-INVARIANT spectrum-only re-formulation if findable).
