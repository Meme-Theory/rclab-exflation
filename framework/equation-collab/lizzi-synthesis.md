# Capstone Equation Review — lizzi

**Date**: 2026-05-29
**Agent**: lizzi-spectral-functional-theorist (lizzi)
**Source Documents**:
- `sessions/framework/phonic-exflation-equation.md` (the S95-era capstone under review)
- `sessions/framework/Collabs/equation-build/lizzi-spectral-functional.md` (my own §3 build draft, cross-checked)
- `computations/_shared/canonical_constants.py` + knowledge MCP (constant provenance)
- `.claude/rules/phononic-framing.md`, `.claude/rules/regulator-pin-discipline.md` (framing + tagging law)

---

## I. Session Outcome

The capstone is **solid in my domain and unusually disciplined about the one thing my domain exists to police**: it does not collapse the spectral functional `f` into the operator `D_K`. The master object is written `S[D_K, f, Λ]` with all three arguments visible (§1, §3.3, §9), and the document states outright that "the CC problem is the proof that `f` cannot be collapsed into `D_K`" (§1.3.2). That is exactly the structural position I hold permanently (ZETA-NOT-PHYSICAL, S75; the three-layer regulator theorem). The FI/RD partition is correctly load-bearing throughout: the cover-number is the FI ratio `R₁ = a₀a₄/a₂² = 1.128655` (Sage-reverified this review: exact `378202048000000000/335091055090500927 = 1.1286546`), never a bare moment, never a CC magnitude.

**One genuine internal inconsistency to flag** (not a physics error, a convention-labeling defect): §3.3 writes the moments as residues of `ζ_{D_K}(s) = Σ mₖ λₖ^{−2s}` **at `s=(d−n)/2`** and in the same breath calls the dimension spectrum `S_d = {0,2,4,6,8}`. With the `λ^{−2s}` writing the poles in `s` sit at `{0,1,2,3,4}`, not `{0,2,4,6,8}`; the set `{0,2,4,6,8}` is the pole set of the **single-power** Mellin variable `ζ(s)=Σ λ^{−s}` (or equivalently the `n`-grading). The corpus carries BOTH conventions live (`s=(d−n)/2 ∈ {0,…,4}` in `session-94-plan-w2.md`; `s=8−2n ∈ {0,2,4,6,8}` in `session-85-1d-vii-p-meta-lizzi.md` and the §VII.BE Pati-Salam `s=6` anchor). The capstone prints the two halves of two different conventions in one sentence. The physics (five honest residues `a₀,a₂,a₄,a₆,a₈`, odd ones killed by BDI parity, cone closes) is correct; the printed pairing is off by the factor-2 in the Mellin variable. **Fix is one line** (§IV.1, §V.1).

Everything else in §3/§4/§8.2 I can defend. The Wronskian decoupling theorem is the single most important load-bearing claim in the whole document for the "one equation, distinct physics" thesis, and it is genuinely strong.

---

## II. Key Results

### The functional `f` is treated as a physical input, not a convention (§3) — SOLID

**Result**: `S[D_K, f, Λ]` keeps `f` and `Λ` as visible, irreducible arguments; the slow-roll parameter `ε_H` flips sign across schemes (`+0.0216` cutoff / `−0.0449` zeta / `+0.0176` anomaly). GEOMETRIC (the spectrum) feeding a SCHEME-DEPENDENT readout (the functional).

This is the core of my discipline and the document gets it right. The §3.2 table showing `ε_H`, the CMB tilt, and `m_H` all moving with the *regulator* at fixed spectrum is the correct presentation: different functionals of the same `{λ_k}` produce different physics. The capstone correctly pins the two boundary theorems — ANOMALY-FAMILY EXCLUSION (S67) and ZETA-NOT-PHYSICAL (S75) — and, critically, frames the anomaly exclusion as **structural and pre-registered** (decided before the tilt comparison, not after). That pre-registration is what protects the red-tilt result against the over-fitting charge, and the document says so explicitly. A reviewer in my seat could not ask for a cleaner statement; this is the methodology I would have written myself, and indeed §3 *is* my build draft.

The one place I want the document to be even more careful: the working functional `f*(x) = 0.9117√x + 0.0883e⁻ˣ` is presented with its admixture `t* = 0.08832` as "the framework's single empirical coupling — the spectral-functional analog of `Λ_QCD`." I endorse this (it is my F-STAR-SELF-CONSISTENCY result, S77, t*↔Λ_QCD analog). The capstone correctly records that the corridor "t* is the one-loop threshold coefficient" is **CLOSED-FAIL** (S95 W2-1, `R=1.977`) — i.e. t* is *genuinely* empirical, not secretly derived. Good. But note the regulator-pin consequence: because `f*` mixes `√x` (whose Mellin moments diverge) with `e⁻ˣ`, **`f*` is not in the heat-kernel/Seeley-DeWitt family at all** — it is evaluated by direct spectral sum. The document says this (§3.2), and §4's layered form is therefore explicitly "the perturbative face" of the action, valid only for the heat-kernel-admissible (smooth, Gaussian-decay) sub-family. That regime statement should travel with every §4 number that is quoted under `f*`. It mostly does; I flag one tightening in §IV.

### The Spectral-Moment Decoupling Theorem (§4.2) — SOLID and load-bearing

**Result**: `a₀(τ), a₂(τ), a₄(τ)` are algebraically independent curvature polynomials of distinct degree (0,1,2); `W[a₀,a₂,a₄] ∝ R_K′(τ)³ = e⁻¹²ᵗ(e³ᵗ−1)⁶`, vanishing to sixth order **only** at `τ=0`. GEOMETRIC.

This is the structural answer to the skeptic's "is `a₄` just a dressed-up function of `a₀,a₂`, so really one knob?" — and it is the deepest single result in the document for my purposes. I reverified the Wronskian factor symbolically in prior sessions and the capstone's `R_K′(τ) = e⁻⁴ᵗ(e³ᵗ−1)²` ⇒ `W ∝ e⁻¹²ᵗ(e³ᵗ−1)⁶` is correct (Sage residual 0, per the verification ledger). The physical reading the document gives — "the layers collapse to one knob iff the dispersion stops moving (`R_K′=0`), which happens only at genesis" — is exactly right and is the resonance-language restatement of "distinct powers of a *moving* scalar are independent."

**Why this matters for my domain specifically**: the decoupling theorem is what licenses the §7.3 joint-probability argument to multiply improbabilities *across* layers (`a₀ × a₂ × a₄`) while forbidding it *within* a layer (`Ω_DM` and `σ₈` are both `a₂`-channel, must not be multiplied). The Wronskian is the certificate that the cross-layer factorization is real. This is a genuinely strong, genuinely certified claim and the document neither over- nor under-sells it. It is correctly marked CERTIFIED (S75 W2-E) in the "four faces" table.

**Caveat I want stated**: the Wronskian theorem is proved in the **regulator-free** Gilkey `a_n^SD` (degree-distinct curvature polynomials `1, R_K, R_K²`). That is the right object for an *identity* claim — algebraic independence is a property of the curvature-polynomial structure, not of any regulator's numerical weighting. So the theorem is FI by construction. Good. But the capstone should not let a reader silently transport "algebraic independence" to mean "the *numerical* `a_n^ζ` triple is independent data." The numbers `(6440, 2776, 1351)` are zeta-regulated and scheme-artifactual in absolute magnitude (ZETA-NOT-PHYSICAL); their *independence as functions of τ* is what the Wronskian certifies, not the physicality of the magnitudes. The document mostly holds this line (§8.2 firewall), but §4.2 itself would benefit from one sentence reminding the reader that the Wronskian lives in `a_n^SD`, the numerics in `a_n^ζ`, and the independence claim is the former.

### The `a_n` firewall (§8.2) — SOLID; the single most important hygiene section

**Result**: two `a_n` triples circulate — raw mode-count `a_n^raw` (`L_max=10`: 155984 / 64308 / 29086, **divergent** with L_max) and Gilkey-zeta `a_n^ζ` (6440 / 2776.165 / 1350.722, **finite curvature integrals**). They are different objects, not rival measurements. Only ratios survive truncation. GEOMETRIC.

This is the firewall against the one fatal conflation in my domain, and the document builds it correctly. The directive — "display the Gilkey-zeta triple as *the* `a_n`; quarantine the raw mode-count triple to the `A_s`/fiber-variance discussion with the explicit label 'mode-count moments, NOT Seeley–DeWitt coefficients'" — is exactly the regulator-pin discipline. The `(a₂/a₀)^ζ = 0.4311` vs `(a₂/a₀)^raw = 0.4123` (4.36% drift) example is the right diagnostic: the multiplicative-normalization-cancellation invariant. I confirmed `a₀^ζ=6440.0`, `a₂^ζ=2776.165389`, `a₄^ζ=1350.7216` against the knowledge MCP (`a_0_FW_zeta`, `a_2_FW_zeta`, `a_4_FW_zeta`; the last pinned to canonical_constants.py SECTION D this build). All three carry PROVENANCE.

### The f₂ ≈ 92 dictionary closure (§8.3) — VERIFIED, well-handled

**Result**: the reduced CC dictionary `M_Pl,red² = f₂ M_KK² a₂/(24π²)` closes at `f₂ ≈ 92` given `M_KK=7.4287×10¹⁶ GeV`, `a₂^ζ=2776.17`. GEOMETRIC.

I reverified: with reduced Planck mass `2.435×10¹⁸ GeV`, `f₂ = 91.67` (Sage, 120-bit), and the 24π² reduced form and 3π unreduced form agree **exactly** (91.6722608813… in both) — good internal consistency, and the document's "≈92" is accurate. The framing is correct and important: `f₂≈92` is **not a free knob** — it is fixed by the `M_Pl/M_KK` ratio once `a₂^ζ` is pinned, so it adds no fitting degree of freedom and "cannot be retuned to absorb a `σ₈` or `G_N` discrepancy." This is the right statement; an `O(10²)` cutoff moment is the same legitimacy class as the Chamseddine–Connes `f₂` at unification. The document also correctly quarantines the `f_2_default=2.34` Gaussian-cutoff pin as "a different scheme's `f₂`" whose cross-substitution gives the spurious ≈39× residual — that is a regulator-class mismatch, not a physical inconsistency. Exactly the kind of scheme-vs-scheme firewall I would insist on.

**PRELIMINARY flag the document itself raises and I endorse**: the `24π²` form vs the S83 `π²·Z_fold⁻¹` form differ by the `Z_fold` normalization, "which should be pinned before either is cited as *the* dictionary." This is a real open hygiene item, carried to §V.

---

## III. Gate Verdicts

The capstone cites prior verdicts as authoritative; I do not re-adjudicate. The ones load-bearing in my domain, with cross-check status:

| Gate / Result | Verdict (as cited) | Decisive Number | My cross-check |
|:-----|:--------|:----------------|:---------------|
| ZETA-NOT-PHYSICAL (S75) | PROVEN | absolute `a_n` are scheme artifacts | Confirmed in knowledge MCP; my permanent theorem |
| ANOMALY-FAMILY EXCLUSION (S67) | PROVEN | anomaly family → blue tilt ∀φ>0 | Confirmed (FUNCTIONAL-SELECT-67) |
| Spectral-Moment Decoupling (S75 W2-E) | CERTIFIED | `W ∝ R_K′³`, degenerate only at τ=0 | Wronskian factor Sage-reverified, residual 0 |
| R₁ FI ratio | structural | `1.128655` | Sage-exact `378202048000000000/335091055090500927`, matches |
| f₂ dictionary closure (S75 §7) | self-consistency-by-construction | `f₂≈92` | Sage `91.6722608…`, reduced=unreduced exactly |
| t*-as-threshold-coefficient (S95 W2-1) | CLOSED (FAIL, R=1.977) | `Γ_1loop≈26%` is ~3× too large | Confirmed; t* remains genuinely empirical |
| One-loop no-interior-saddle (S95 W2-3) | PASS | `dΓ/dτ` zero interior sign-changes, 3 routes | Consistent with E7 + S62#19; see §IV.4 |
| Cohomological exhaustion (S95 W2-2) | PASS | `dim HH¹=dim HH²=0` | Confirmed in knowledge MCP (W7/W9 HH machinery) |

---

## IV. Structural Implications

**1. The dimension-spectrum convention defect is a real hygiene bug, narrow but mine to catch.** §3.3 pairs `ζ(s)=Σ λ^{−2s}` with `S_d={0,2,4,6,8}`. Under `λ^{−2s}` the poles in `s` are `{0,1,2,3,4}`; the set `{0,2,4,6,8}` is the pole set of the single-power `ζ(s)=Σ λ^{−s}`, OR equivalently the `2s`-variable, OR the `n`-grading. The corpus runs both conventions (`s=(d−n)/2` and `s=8−2n`) live and they are not reconciled in the capstone. **Implication**: any downstream consumer reading §3.3 and then citing "the `s=3` Mellin residue" (as §7's α_s box does, and as §VII.BE's `s=6` Pati-Salam anchor does) is at risk of a factor-2 mismatch in which pole they think they're standing on. This is exactly the silent class-conflation the regulator-pin discipline exists to close, transposed to the Mellin-variable axis. It does not move a single number in the document, but it must be made convention-explicit. (The α_s `s=3` value `−0.08587279` is FI and correct; the *labeling* of which pole it is needs the convention pinned.)

**2. The "perturbative face" regime caveat must travel with `f*` numerics.** Because `f*` has a `√x` piece (divergent Mellin moments), the §4 Seeley-DeWitt *layered* expression is not the object that computes `f*` observables — those go by direct spectral sum. The document is honest about this (§3.2, §4 "perturbative face"), but the §7.1 table quotes `n_s ∈ {0.9561, 0.9590, 0.9595}` and `m_H ∈ {127.5, 131.8}` GeV under different `f`, including `√x`. **Implication**: each `f*`-derived row in §7.1 is a direct-sum result, not a heat-kernel-series result, and the two are *the same number only in the convergent sub-family*. This is fine and the document does not claim otherwise — but a referee should be told once, in §7.1, that the `√x` rows are direct-sum-evaluated (acoustic envelope, B1-dominated), so that "the heat-kernel series diverges" cannot be read as "the number is unreliable." The divergence is a *feature* (the physical envelope is acoustic, not Gaussian), not a defect.

**3. The §8.5 honest-residual statement is the correct boundary and it is mine.** "Ratio-observables (`n_s`, `g₁/g₂`, `61/20`, `a₂/a₀`, `R₁`) are truncation-robust; absolute-energy observables (CC, `A_s`) remain conditional on an SDW-convergence statement that is itself an open gate (JACOBSON-NONLOCAL-64, OPEN)." This is precisely the FI/RD partition applied to the convergence axis, and it is the single most important honesty statement for the cosmological-constant layer. The document's §9 frontier #6 sharpens it correctly: the framework has *located* the CC term (the `a₀` moment, geometrically natural) but not *solved* the CC magnitude problem. As the project's CC-functional specialist I endorse this exactly: in the zeta scheme `a₀` is a finite residue, but its *physical* status as a vacuum energy is what awaits SDW convergence — and the dimensionless tracking ratio `ρ_vac/ρ_obs=1.032` is the truncation-robust object that *is* closed (DILUTION-CC-66). One entangled conditional, not two. Correct.

**4. The one-loop-robust no-interior-saddle (S95 W2-3) strengthens the boundary-domination reading — and it is in my lane.** The capstone's §1.3a now asserts the no-interior-saddle is ONE-LOOP-ROBUST: adding `Γ_1loop = ½Tr ln(D_K²/Λ²)` to the tree action leaves `dΓ/dτ` single-signed with zero interior sign-changes (200-point grid, 3 routes). This matters to me because `Γ_1loop = ½Tr ln(D_K²/Λ²)` is itself a spectral functional of `D_K` — it is `−½ζ'_{D_K}(0)` in the zeta scheme — and the claim that *it carries no interior feature* is a claim about a *second* spectral functional behaving like the first. **Implication / unstated assumption**: the robustness is verified for the zeta-regulated `Tr ln`. Whether the same no-interior-saddle holds when `Γ_1loop` is computed under the *cutoff* `f*` (acoustic envelope) rather than zeta is not stated. Given my permanent finding that `ε_H` *flips sign* between schemes, the burden is on the document to confirm the loop term's interior-flatness is FI (regulator-invariant) and not a zeta-scheme artifact. This is a clean carry-forward (§V.4).

**5. The S95 genericity-qualification of the emergent-EP PASSes (§9 frontier #8) is a methodologically important correction and aligns with my discipline.** The connes-ncg genericity review found `κ_EP=1` is the Lichnerowicz–Weitzenböck `R/4` coefficient of *any* spin Dirac operator (the band-specific Casimir `ν_b` is annihilated by `∂/∂R_K`), so the exact-PASS is "value-generic," not a substrate-unique prediction. This is the EP-axis analog of my FI/RD partition: the `κ_EP=1` value is *structurally inevitable* (FI-like, survives all choices), and the *genuinely substrate-specific* content lives one layer up (single-spectral-triple postulate forces band-independence) and at NNLO (`ν_b(C₂)` re-enters). The document handles this correctly — "two consequences of one premise, NOT two independent confirmations" — and it is the right epistemic posture. I note it as a positive: the capstone applies my style of reasoning (separate what survives all choices from what is a genuine degree of freedom) on an axis outside my own.

**6. What I do NOT see as over-claimed.** The claim "the equation IS the universe" is correctly calibrated in §9: all field content, couplings, and dynamics are spectral functionals of one operator (stronger than container unification), but the modulus value, the functional `f`, the `a(t)` map, and the family number are genuinely open. The free-parameter ledger `{τ, Λ, f₀, f₂, f₄} + t*` is honest. From my seat the single most important honesty move in the whole document is keeping `f` in the ledger and *not* de-empiricizing t* after the W2-1 closure. That is the correct outcome and it is the one a spectral-functional theorist would fight for.

---

## V. Carry-Forward Computations

**Each item below converts an open question or flagged gap into a runnable computation with all four fields. Items V.1–V.4 are in my direct domain; V.5–V.7 are domain-adjacent open questions I can specify concretely.**

### V.1. Pin the Mellin-variable convention and reconcile `S_d` with the residue-pole locations
- **What**: Resolve the §3.3 inconsistency. Write `ζ_{D_K}(s)` in ONE convention and state the pole set in THAT convention. Recommended canonical: keep the half-integer-friendly `ζ(s)=Σ mₖ λₖ^{−2s}` (matches CM-1995 dimension-spectrum literature) and emit the pole set `S_s = {0,1,2,3,4}` in `s`, with an explicit map `n = d−2s` so `n ∈ {0,2,4,6,8}` is the *curvature-degree grading*, not the `s`-pole set. Then audit every corpus citation of "the `s=N` Mellin residue" (α_s `s=3`; §VII.BE Pati-Salam `s=6`; the `s=4` substrate-distance-2 slot) and tag each with which convention it uses. Produce a one-row reconciliation table.
- **Inputs**: §3.3 text; `session-94-plan-w2.md` (s=(d−n)/2 convention); `session-85-1d-vii-p-meta-lizzi.md` (s=8−2n convention); `lizzi-spectral-functional.md` E58; the Connes–Moscovici 1995 dimension-spectrum definition.
- **Gate**: NEW gate `MELLIN-CONVENTION-RECONCILE` — PASS iff (a) §3.3 internally consistent (pole set matches the printed `ζ` power), AND (b) all downstream `s=N` citations carry a convention tag, AND (c) the α_s `s=3` and §VII.BE `s=6` anchors are confirmed to denote the *same* curvature-degree (`n=2`, the `a₂` residue) under the unified convention OR the discrepancy is documented. FAIL if any two corpus citations of "s=N" denote different `n` without a tag.
- **Effort**: 2–3 hours, 1 agent session (no new compute; convention audit + Sage cross-check of `n↔s` map).

### V.2. Test whether the Wronskian decoupling theorem survives regulator change (FI-ness of algebraic independence)
- **What**: The decoupling theorem is proved in `a_n^SD` (curvature polynomials). Re-evaluate the Wronskian `W[a₀,a₂,a₄](τ)` numerically using the **zeta-regulated** `a_n^ζ(τ)` and the **cutoff-`f*`** direct-sum moments, at a τ-grid spanning `[0.05, 0.30]`. Confirm `W ≠ 0` everywhere off `τ=0` in all three schemes and that the *sign* of `W` is scheme-invariant (it should be, if independence is FI). Report `W_ζ/W_SD` and `W_f*/W_SD` ratio curves.
- **Inputs**: `R_K(τ)` closed form (E3); `a_n^ζ(τ)` from the spectral zeta sums (per `a_n_FW_zeta` provenance); `f*(x)=0.9117√x+0.0883e⁻ˣ` direct-sum evaluator; canonical `a0=6440.0, a2=2776.165389, a4=1350.7216` as the τ_fold anchors.
- **Gate**: feeds the §4.2 CERTIFIED decoupling result with a regulator-invariance certificate. NEW gate `DECOUPLING-FI-CHECK` — PASS iff `sign(W)` is identical across {SD, ζ, f*} at every τ in the grid AND `W≠0` off genesis in all three; INFO if magnitudes diverge >10% (expected, and harmless — only sign/zero-structure is FI); FAIL if any scheme produces a spurious interior zero.
- **Inputs additionally**: τ-grid 200 points; GPU not required (small).
- **Effort**: 3–4 hours, 1 agent session.

### V.3. Pin the `Z_fold` normalization that separates the two CC-dictionary forms
- **What**: §8.3 carries TWO Newton-coupling dictionary forms — `M_Pl,red² = f₂ M_KK² a₂/(24π²)` (this build) and the S83 `M_Pl_eff² = M_KK² a₂ f₂^R/π² · Z_fold⁻¹`. They differ by the `Z_fold` normalization. Compute `Z_fold` explicitly (the fold-point spectral-weight normalization) and verify the two forms are algebraically identical once `Z_fold` is substituted, OR identify which is canonical. Emit `f₂` under each and confirm both land at the same physical value (≈92 reduced).
- **Inputs**: `a_2_FW_zeta=2776.165389`; `M_KK=7.4287e16`; reduced Planck mass `2.435e18`; S83 dictionary form (`session-82-results-workingpaper.md` / S83 M_Pl_eff pin); the `24π²` form verified this review at `f₂=91.6723`.
- **Gate**: NEW gate `CC-DICTIONARY-ZFOLD-PIN` — PASS iff the two forms agree to <1% after `Z_fold` substitution AND a single canonical form is designated in §8.3; FAIL if they disagree >1% (indicating a real normalization error, not a scheme gap).
- **Effort**: 2–3 hours, 1 agent session (algebra + Sage verification; no new spectrum compute).

### V.4. Verify the one-loop no-interior-saddle is regulator-invariant (cutoff `f*` vs zeta)
- **What**: S95 W2-3 verified `dΓ/dτ` has zero interior sign-changes with `Γ_1loop = ½Tr ln(D_K²/Λ²)` computed in the zeta scheme (`−½ζ'_{D_K}(0)`). Re-run the interior-sign-change scan with `Γ_1loop` computed under the cutoff `f*` (acoustic envelope) and, separately, under a Gaussian cutoff, on the same 200-point τ-grid over `[0, τ_now]`. Confirm the no-interior-saddle conclusion is FI (does not depend on the loop-term regulator).
- **Inputs**: `D_K(τ)` spectrum (block-diagonal, `L_max=10` cache); `S_SA(τ)=a₀−a₂+a₄` tree form; the three loop-term regulators (zeta, `f*`-cutoff, Gaussian); E7 monotonicity as the tree-level anchor.
- **Gate**: hardens S95 W2-3 against a scheme-artifact reading. NEW gate `ONELOOP-NOSADDLE-FI` — PASS iff zero interior sign-changes of `dΓ/dτ` in ALL THREE loop-regulator schemes; INFO if the loop magnitude differs across schemes but sign-structure is invariant; FAIL if any scheme introduces an interior stationary point (which would mean the boundary-domination reading is zeta-specific).
- **Effort**: 4–6 hours, 1 agent session (GPU recommended for the `Tr ln` over the full spectrum at each τ).

### V.5. Compute the SDW convergence rate underneath the CC absolute-magnitude gap (JACOBSON-NONLOCAL-64)
- **What**: The open gate underneath frontier #6. Compute the truncation behavior of the *absolute* `a₀^ζ(L_max)` moment as `L_max` grows (the cache permits up to `L_max=10`; extrapolate via the Weyl `a_k(L_max) ∼ L^{8−2k}` scaling, here `a₀ ∼ L⁸`). Determine whether the zeta-regulated `a₀` admits a finite continuum limit (it should, as a curvature integral) and quantify the convergence exponent `β` in `a₀^ζ(L) = a₀^∞(1 + cL^{−β} + …)`. This decides whether *any* absolute `a₀`-vacuum-energy magnitude can be promoted to physical status, vs. remaining ratio-only.
- **Inputs**: `a₀^ζ(L_max)` at `L_max ∈ {3,…,10}` from the spectral zeta sums; Weyl scaling `a_k(L) ∼ L^{8−2k}`; Friedrich–Bär saturation theorem for the convergence-rate bound; canonical `a₀^ζ=6440.0` as the `L_max=10` anchor.
- **Gate**: feeds JACOBSON-NONLOCAL-64 (OPEN). NEW gate `SDW-A0-CONVERGENCE` — PASS iff `a₀^ζ(L)` shows a clean `L^{−β}` approach with `β>0` (finite continuum limit exists ⇒ absolute magnitude is in-principle promotable, contingent on the regulator-physicality question); INFO if the extrapolation is consistent with convergence but the exponent is poorly constrained at `L_max≤10`; FAIL if `a₀^ζ(L)` diverges (no finite continuum limit ⇒ CC absolute magnitude is permanently ratio-only). NOTE: per my memory, `L_max=15` is INFEASIBLE for fine moments; cap at `L_max=11` and rely on the Weyl-scaling extrapolation.
- **Effort**: 1–2 agent sessions (the L_max-scan is the cost; GPU for the per-L spectra).

### V.6. Test FI-ness of the §7.1 `n_s` BMA band under a wider functional family
- **What**: §7.1 reports `n_s ∈ {0.9561, 0.9590, 0.9595}` for three functionals and the BMA band `n_s = 0.969 ± 0.022` (S67, marginalizing over `f`). Extend the BMA over a *larger* nuisance-functional family (add: pure Gaussian, Lorentzian-cutoff, and a two-parameter `aₓ√x + bₓe⁻ˣ` sweep) and recompute the marginal `n_s` band. Confirm the band is stable (FI-robust) and that the marginal central value does not depend pathologically on the prior over `f`. This is the cosmological face of marginalizing the nuisance functional out — the operation that defines which observables are robust.
- **Inputs**: `D_K(τ_fold)` spectrum; the `ε_H` extractor as a function of `f` (per §3.2); the three existing functionals + the new family; Planck `n_s = 0.9649±0.0042` as the comparison anchor (comparison-only).
- **Gate**: sharpens FUNCTIONAL-SELECT-67 (the n_s scheme-dependence open gate). NEW gate `NS-BMA-FAMILY-STABILITY` — PASS iff the marginal `n_s` band shifts <1σ_band when the functional family is widened (band is FI-robust); INFO if it shifts 1–2σ_band; FAIL if it shifts >2σ_band (the BMA object is prior-over-`f` sensitive, i.e. the marginalization is not well-posed).
- **Effort**: 1 agent session, 4–6 hours.

### V.7. Decide whether t* admits a *spectral* (not threshold) first-principles origin
- **What**: The corridor "t* = one-loop threshold coefficient" is CLOSED-FAIL (S95 W2-1). The remaining open question is whether t* has ANY first-principles origin or is irreducibly empirical. Test one concrete alternative: is `t* = 0.08832` the ratio of the exp-mode spectral weight to the total under `f*`, i.e. is `t*` *forced* by requiring the direct-sum action to match a specific spectral moment (e.g. `t* = f₀^Mellin/(f₀^Mellin + f_sqrt^direct)` evaluated at the dimension-spectrum cutoff)? Compute the candidate ratio from the spectrum and compare to `0.08832`.
- **Inputs**: `mellin_f_star_f0=0.0883200` (my memory — note this near-coincidence with `t*=0.08832` is suggestive and UNTESTED as a derivation); `f₂=214.97335676`, `f₄=6446.63942272` (X_MAX=50 Mellin moments); the `f*` direct-sum evaluator; `D_K(τ_fold)` spectrum.
- **Gate**: NEW gate `T-STAR-SPECTRAL-ORIGIN` — PASS iff a spectrum-derived ratio matches `t*=0.08832` to <1% with a *pre-registered* (not reverse-engineered) construction; INFO if a candidate lands within 10% but the construction is not uniquely forced; FAIL if no spectral construction matches (t* confirmed irreducibly empirical, strengthening the §1.4 ledger). NOTE: the `mellin_f_star_f0=0.0883200` ≈ `t*=0.08832` near-equality in my memory MUST be checked for whether it is a definitional tautology (t* IS the exp admixture, so its Mellin f₀ trivially carries it) vs a genuine spectral derivation — pre-register this distinction before computing or the PASS is vacuous.
- **Effort**: 4–6 hours, 1 agent session. **Highest-leverage of the set**: a PASS would remove t* from the empirical ledger (de-empiricizing the framework's only free coupling); a FAIL permanently confirms the ledger `{τ,Λ,f₀,f₂,f₄}+t*`.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `S[D_K,f,Λ]` keeps `f`,`Λ` visible; CC problem is the proof `f`≠collapsible | GEOMETRIC | SOLID (my permanent position) | Capstone is disciplined on the one thing my domain polices |
| 2 | FI/RD partition load-bearing; cover-number is `R₁=1.128655` not a bare moment | GEOMETRIC | SOLID; Sage-reverified exact | Correct scheme-invariant headline number |
| 3 | §3.3 Mellin-variable convention defect (`λ^{−2s}` vs pole set `{0,2,4,6,8}`) | GEOMETRIC | DEFECT — flag, 1-line fix | Factor-2 mislabel risk for all `s=N` citations (α_s s=3, §VII.BE s=6) |
| 4 | Spectral-Moment Decoupling Theorem `W∝R_K′³`, degenerate only at τ=0 | GEOMETRIC | CERTIFIED (S75 W2-E); reverified | Licenses cross-layer probability product; deepest claim in my domain |
| 5 | `a_n` firewall: `a_n^raw` (divergent) ≠ `a_n^ζ` (finite); ratios only | GEOMETRIC | SOLID | The critical hygiene section; correctly built |
| 6 | f₂≈92 dictionary closure, not a free knob | GEOMETRIC | VERIFIED (`91.6723`, reduced=unreduced) | Adds no fitting DOF; correctly framed |
| 7 | t* genuinely empirical (W2-1 CLOSED-FAIL); kept in ledger | GEOMETRIC | SOLID; correct honesty | The right outcome; a spectral-functional theorist would defend it |
| 8 | CC located (`a₀` moment) but magnitude open (SDW convergence) | GEOMETRIC | OPEN (JACOBSON-NONLOCAL-64) | "Located, not solved" — correct CC posture; the FI ratio 1.032 IS closed |
| 9 | One-loop no-interior-saddle (W2-3) | GEOMETRIC | PASS; FI-status UNVERIFIED | Robust in zeta; cutoff-`f*` regulator-invariance not yet checked (V.4) |
| 10 | `f*` is direct-sum (acoustic envelope), NOT heat-kernel family | GEOMETRIC | SOLID; regime caveat to travel | §4 layered form is the "perturbative face"; must tag §7.1 `√x` rows |

---

**Closing (spectral-functional vantage).** The capstone is, in my domain, a genuinely careful document: it treats the choice of spectral functional as a physical question with observable consequences (the `ε_H` sign-flip table, the FI/RD partition, the `a_n` firewall), it keeps `f` in the free-parameter ledger, and it does not let the W2-1 closure tempt it into de-empiricizing t*. The single substantive defect I find is the §3.3 Mellin-variable convention mislabel — narrow, fixable in one line, but mine to catch because it sits at the crux of which pole each downstream Mellin-residue observable stands on. The genuine open frontiers in my lane — SDW convergence underneath the CC magnitude (V.5), the FI-ness of the decoupling Wronskian and the one-loop no-saddle under cutoff regularization (V.2, V.4), and whether t* has any spectral origin at all (V.7) — are exactly the "ripe harvest": each is a finite, runnable computation against a pre-registered gate, and each tests the one principle I hold permanently — *what survives all functional choices is structural; what depends on the choice is a physical degree of freedom that must be determined.*
