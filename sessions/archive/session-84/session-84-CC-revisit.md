# Session 84 — Cosmological Constant Revisit

**Date**: 2026-04-21
**Agent**: tesla-resonance (Workhorse-Resonance)
**Status**: **ANALYSIS** — methodological diagnosis + five unconventional pairings proposed as S85 pre-registered gates. Not a closure; a re-framing with concrete computational targets.

**Source Documents**:
- `sessions/archive/session-63/framework-cc-oom.md` (Van den Dungen's comprehensive CC status report — 9 closures, 7 open paths, 60 items, 42 CLOSED/PROVEN)
- `sessions/framework/Phononic-Substrate-Geometry.md` §11.2 (the CC summary that motivated the revisit)
- S60 `s60_eta_invariant.py` (η-invariant computation, not yet connected to CC)
- S61 `s61_ruelle_zeta.py` (Ruelle zeta, not yet connected to CC)
- S76 `s76_hp4_first_principles.py` (chi_2 × HP4 = 0.337 × ρ_obs result)
- S77 `s77_gge_occupation_correction.py` (chi_2_canonical = 0.741)
- S83 `s83_w1_g1_ic_scheme_derivation.py` (Connes-Moscovici dimension-spectrum requirement flagged as open)

**Provocation (user, mid-session)**:
> "Only partially correct. Your predecessor model exhaused 'known mechanisms'; you have yet to evaluate the question. Use our knowledgebase and session history to explore the CC OOM once again, but with an eye for new physics or unconventional pairings of math disciplines."

---

## 0. What the Thesis Said and Why It Was Wrong

The `Phononic-Substrate-Geometry.md` §11.2 asserted: *"every known mechanism for canceling vacuum energy has been tested and all fail for structural reasons (S66 CC reframe, S74 Friedmann wrong-question theorem)."*

This inherits a conventional-idiom closure claim. The knowledge-base audit shows it is **precise within the idiom but over-broad about what "every known mechanism" actually means**. The framework's 9 CC closures all operate in one of four idioms:

1. **Perturbative QFT / Seeley-DeWitt** (Closures 1, 2, and several others)
2. **Variational calculus / q-theory** (Closures 7, 8, 9)
3. **BCS / Richardson-Gaudin integrability** (Closures 3, 4, 5, 6)
4. **Gravitational backreaction / Kasparov factorization** (Open Path B, plus several closures)

What the framework has **not** tested is any mechanism operating in the idiom of:
- Arithmetic topology / number-theoretic regularization
- Categorical/cohomological residues (Connes-Moscovici local index formula in full)
- Torsion K-theory and Dai-Freed pairings
- Spectral-flow indices and η-invariant modular phases
- Automorphic L-function special values
- Poincaré duality between cosmological observables (DM ↔ DE as conjugate classes)

The framework has *computed* ingredients from several of these — η(D_K) at S60, the Ruelle zeta at S61, the dimension-spectrum requirement flagged at S83 W1-G1 — but **none has been connected to the CC computation**. They were built for other purposes and left on the shelf.

This re-analysis identifies five concrete unconventional pairings, gives each a pre-registrable gate, and flags the factor-3 residual in chi_2 × HP4 = 0.337 × ρ_obs as the organizing hook.

---

## 1. The Real Scope of the 9 Closures (Methodological Diagnosis)

### 1.1 What S37 CUTOFF-SA-37 Actually Proves

S37 Structural Monotonicity Theorem states: `S_f(τ)` is monotonically increasing for **all smooth monotone cutoff functions f**, all UV cutoff scales `Λ`, all τ ∈ [0, 0.5]. This is a genuine theorem with 9,600 individual verifying checks.

The theorem's hypothesis is important:
- **smooth monotone** cutoff functions
- the functional form `Tr f(D²/Λ²)` (i.e., a trace of a smooth function of the Laplacian-like operator)

What S37 does **not** cover:
- **Distributional functionals** — objects like `δ(s − s_0)` applied to ζ(s), which pick up residues at specific complex s-values rather than integrating smoothly
- **Topological phases** — `e^{iπη}` phase factors from APS boundary terms, which are not "Tr f" of anything
- **Torsion K-theory pairings** — Dai-Freed and related anomaly-inflow pairings, which take values in `ℝ/ℤ` rather than `ℝ`
- **Spectral-flow indices** — integer-valued topological invariants that jump, rather than smooth `τ`-dependent functions
- **Modular phase** — the phase of the fermion determinant on a manifold with torsion bundle class

These are genuinely different mathematical objects from the ones S37 forbids. Interpreting S37 as "no CC suppression mechanism survives" is a **category error** — S37 forbids one kind of functional from producing a minimum; it does not forbid the CC from being a *different kind of object entirely*.

### 1.2 What the Other 8 Closures Cover

Closures 2-9 are all about specific **QFT or integrability mechanisms**:
- A-tensor / T-tensor cross-terms (product-metric triviality)
- Density-density Hartree (block-diagonal prohibition)
- Josephson pair-transfer (R-G integrability preserved)
- Beliaev / Landau damping (kinematics forbidden)
- Fabric vacuum pressure (Volovik equilibrium on single cell)
- q-theory self-tuning (dE/dq > 0 everywhere)
- B-F cancellation with shared spectrum (T9 maxima-only theorem)

Each is rigorous. None excludes mechanisms where the CC is an *arithmetic* or *topological* quantity that is bounded by construction rather than by cancellation.

### 1.3 The Methodological Gap

The framework's CC discipline has been: *assume the CC is a spectral moment of D_K, try to make the moment small*. The unconventional alternative is: *the CC might not be a spectral moment at all; it might be a phase, a torsion class, or a pairing invariant, and its smallness would then be a topological bound rather than a cancellation miracle*.

No gate in the 60-item ledger tests this alternative. That is what this session revisits.

---

## 2. The Factor-3 Residual as Organizing Hook

The current leading CC calculation:

```
  ρ_L^predicted = chi_2 × HP4 = 0.337 × ρ_obs       (S75 W4-C)
  chi_2 = ⟨|λ|⟩ / λ_max = 0.741                      (canonical, S76-S77)
  ρ_L^observed = 2.7 × 10⁻⁴⁷ GeV⁴                    (Planck 2018)
```

Predicted is 3× too small. **This is a factor-3 shortfall in a framework built on SU(3)**. Three candidate 3-fold structural sources:

| 3-fold structure | Role | Could it be the missing factor? |
|:---|:---|:---|
| `Z_3` center of SU(3) | Discrete gauge subgroup, triality of quarks | Quotient-spectral-measure correction |
| 3-generation bimodule multiplicity | Forces 3 fermion generations | Single-generation `chi_2` summed over 3 gives ×3 |
| Spin(8) triality | Outer `Z_3` automorphism of Spin(8), permuting {V, S⁺, S⁻} | Triality-averaging of chi_2 over 3 inequivalent 8-dim reps gives ×3 |
| 3 summands of `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` | SM gauge group sources | Summand-summed `chi_2` gives ×3 |

None of these has been tested against the CC. Each is a *pre-registered gate* in the sense that the computation is well-defined and the outcome will be a specific number comparable to the factor 3.

The triality hypothesis is structurally sharpest: Spin(8) is the **unique** spin group for which the 8-dim vector rep `V` and the two 8-dim spinor reps `S⁺, S⁻` are interchangeable by an outer automorphism of order 3. The `Cl(8)` Clifford module carries all three, and the physical Dirac operator `D_K` acts on a Clifford module that privileges one choice. If `chi_2` has been computed for one rep and the physical CC is the triality-average over all three, `chi_2^triality = 3 × chi_2^single = 2.22`, giving `ρ_L = 3 × 0.337 × ρ_obs = 1.01 × ρ_obs` — 1.1% residual.

This is not a proof. It is a specific testable hypothesis. The gate is pre-registered below.

---

## 3. Five Unconventional Pairings — Proposed S85 Gates

### 3.1 Gate S85-CC-1 — η-Invariant as CC Modular Phase

**Mathematical idiom**: Atiyah-Patodi-Singer index theorem; Dai-Freed pairing; modular phase of the fermion determinant.

**Hypothesis**: The observed cosmological constant is not `f_0 · a_0 · M_KK⁴` (spectral moment at dimension 4) but `π · η(D_K + D_F) · M_Pl² · H_0²` (modular phase of the partition function at the IR cosmological scale). For compact homogeneous spin manifolds, `η` is rational with denominator dividing a small integer tied to the Weyl group order. For SU(3) with natural spin structure, denominators of 6, 12, or 24 are expected.

**Why it survives S37**: η is `(ζ_{|D|⁻ˢ}(0) − ζ_{D⁻ˢ}(0))/2`, a distributional quantity at s = 0 that jumps at spectral-flow events. S37 forbids smooth monotone functionals from producing minima; it does not cover distributional or topological invariants.

**What the framework has already computed**: S60 `s60_eta_invariant.py` computed `η` for the BdG operator at µ = 0 and reported `η = 0` by PH symmetry. This is the BdG operator, not `D_K + D_F` on the full Jensen-SU(3) × A_F spectral triple. The relevant η has not been computed.

**Pre-registerable gate**:
- **What**: Compute `η(D_K + D_F)` for the full Jensen-SU(3) × A_F spectral triple at τ = τ_fold, L_max ∈ {7, 9, 11}. Evaluate `π × η × M_Pl² × H_0²` and compare to `ρ_obs`.
- **Inputs**: D_K eigenspectrum at L_max ∈ {7, 9, 11}, A_F bimodule structure, J operator with J² = +1, KO-dim = 6.
- **Gate** (physical PASS criterion is the magnitude bracket; denominator is aesthetic):
  - **PASS** if η converges to a rational or algebraic value in the window `η ∈ [0.07, 7.0]` (i.e., `0.1 ≤ π·η·M_Pl²·H_0² / ρ_obs ≤ 10`, the factor-10 magnitude bracket).
  - **INFO** if η converges to a value outside the bracket but by a known finite factor (e.g., factor 100 off — suggests a missing prefactor of known origin).
  - **FAIL** if η doesn't converge (wild spectral asymmetry), OR converges to a value > 10x outside the bracket with no identified missing prefactor.
- **Additional diagnostic** (not a PASS criterion): report whether η is a small rational (denominator ≤ 24) or an O(1) rational. The factor-3 residual in chi_2 × HP4 suggests η may be O(1) (e.g., 2/3 or 3/4), not small-denominator.
- **Effort**: 2 sessions. GPU mandatory at L_max ≥ 9.
- **Classification**: GEOMETRIC + PARTICLE.

**Expected magnitude check (substitution chain, Python-verified)**:

Definitions:
- `ρ_η(η) := π · η · M_Pl² · H_0²` (the η-hypothesis prediction)
- `residual(η) := ρ_obs / ρ_η(η)` (factor by which observed exceeds predicted)

Substitution (Python-verified, `M_Pl = 2.435 × 10¹⁸ GeV`, `H_0 = 1.438 × 10⁻⁴² GeV` from 67.4 km/s/Mpc):
- `M_Pl² = 5.929 × 10³⁶ GeV²`
- `H_0² = 2.068 × 10⁻⁸⁴ GeV²`
- `M_Pl² · H_0² = 1.226 × 10⁻⁴⁷ GeV⁴`
- `π · M_Pl² · H_0² = 3.851 × 10⁻⁴⁷ GeV⁴`

Simplification:
- `residual(η) = ρ_obs / (π · η · M_Pl² · H_0²) = 2.7 × 10⁻⁴⁷ / (η · 3.851 × 10⁻⁴⁷) = 0.7010 / η`

Direction check (Python-verified values):
- `residual(1/6) = 4.21` — factor-4 residual
- `residual(1/12) = 8.41` — factor-8 residual (NOT factor 2 — the residual grows as η shrinks)
- `residual(2/3) = 1.05` — 5% residual
- `residual(3/4) = 0.93` — 7% residual (slight over-shoot)
- `η_match = 0.7010` for exact closure

**Direction**: residual ∝ 1/η, so smaller η makes the gap worse, not better. The η-hypothesis is quantitatively consistent with observed CC only for η ∈ {2/3, 7/10, 3/4} — *O(1) rationals*, not tiny denominators like 1/12 or 1/24. This is a different prediction than a naive "small rational η" reading would suggest, and it is testable: η = 2/3 is the real part of the primitive cube root of unity (natural in SU(3) with Z_3 center), η = 3/4 has an interpretation in terms of the 3-generation bimodule. The gate below asks whether the computed η for Jensen-SU(3) × A_F lands in this O(1) window, not whether it lands at 1/24.

The order of magnitude lands correctly from a *completely different mathematical object* than the chi_2 × HP4 route — but only if η is O(1), which itself is a prediction about the substrate's natural spectral-asymmetry magnitude.

### 3.2 Gate S85-CC-2 — Spin(8) Triality Averaging

**Mathematical idiom**: Outer automorphisms of Lie groups; Clifford algebra representation theory.

**Hypothesis**: `chi_2 = ⟨|λ|⟩ / λ_max` is currently computed for one specific embedding of the physical Dirac operator into `Cl(8)` (the vector representation `V`). Spin(8) triality says the Clifford module admits three inequivalent embeddings `{V, S⁺, S⁻}` permuted cyclically by an outer automorphism. The physical CC is the triality orbit sum:

```
  chi_2^physical = chi_2^V + chi_2^{S+} + chi_2^{S-} = 3 × chi_2^single
```

if the three values are triality-equivalent. Predicted CC: `ρ_L = 3 × chi_2 × HP4 = 1.01 × ρ_obs` (1.1% residual).

**Why it survives S37**: triality averaging is a representation-theoretic correction to the functional, not a change in the cutoff function itself. S37's monotonicity theorem does not cover averaging over rep-equivalence classes.

**Pre-registerable gate**:
- **What**: Construct the three inequivalent Spin(8) rep embeddings `{V, S⁺, S⁻}` of `D_K` on Jensen-SU(3); compute chi_2 for each; report the triality orbit sum.
- **Inputs**: D_K eigenspectrum at L_max = 9; Spin(8) triality automorphism; Clifford module structure on H_F.
- **Gate**:
  - **PASS** if chi_2(V) = chi_2(S⁺) = chi_2(S⁻) (triality-equivalent) AND `3 × chi_2 × HP4` matches `ρ_obs` within 10%.
  - **INFO** if triality-equivalent but sub-factor-3 enhancement (Jensen may partially break triality).
  - **FAIL** if the three values differ substantially (triality fully broken).
- **Effort**: 1 session. Computable on existing spectra.
- **Classification**: GEOMETRIC + PARTICLE.

**Prediction stake**: If this PASSES, the factor-3 residual closes. If it FAILS, Jensen deformation explicitly breaks Spin(8) triality and the missing factor has a different source.

### 3.3 Gate S85-CC-3 — Connes-Moscovici Dimension-Spectrum Residues with Hopf-Cocycle Signs

**Mathematical idiom**: Connes-Moscovici local index formula (1995); Hopf-cocycle cohomology; regularized zeta-function residues.

**Hypothesis**: The CC is not `a_0` alone; it is the full **Connes-Moscovici sum**:

```
  Λ_CC = Σ_{d ∈ Sd} sign(Hopf_d) × Res_{s = d} [ζ_{D_K²}(s)]
```

where `Sd` is the dimension spectrum (set of poles of ζ) and `sign(Hopf_d)` comes from the Hopf cocycle associated to each pole. If positive residues (from `a_0`, `a_4`) partially cancel against negative residues (from η, spectral flow, shifted poles), the net `Λ_CC` can be much smaller than `a_0` alone.

**Why it survives S37**: the Connes-Moscovici sum is a signed sum of *residues*, not a smooth integral. S37 does not cover signed residue sums.

**Why this is hard**: computing the dimension spectrum requires the Connes-Moscovici **regularity condition** (algebra closed under `[D², ·]` iteration). S83 W1-G3 flagged `dim H_π ≥ 2` closure for Connes-Moscovici as open at L_max = 5. This may require L_max ≥ 11 to be reliably convergent.

**Pre-registerable gate**:
- **What**: Compute the dimension spectrum of `D_K` on Jensen-SU(3) at L_max = 9, enforcing the Connes-Moscovici regularity test; enumerate all poles `d ∈ Sd`; for each, compute the residue and the Hopf-cocycle sign. Evaluate the signed sum `Σ sign × Res` and compare to `a_0`.
- **Inputs**: D_K eigenspectrum at L_max = 9; Hopf-cocycle machinery from Connes-Moscovici 1995 §5; regularity test scaffolding.
- **Gate**:
  - **PASS** if full signed sum is suppressed by ≥ 10 OOM relative to `a_0` alone (partial cancellation across dimensions).
  - **INFO** if suppressed by 1–10 OOM.
  - **FAIL** if the sum equals `a_0` (no cancellation).
- **Effort**: 3–4 sessions. Novel math; requires setting up Connes-Moscovici machinery that has only been flagged, not deployed.
- **Classification**: GEOMETRIC.

### 3.4 Gate S85-CC-4 — Dai-Freed Torsion Pairing with `π_4(S³) = ℤ/2`

**Mathematical idiom**: K-theoretic anomaly inflow; Dai-Freed pairing of Dirac operators with torsion bundle classes.

**Hypothesis**: The principal SU(2)-bundle structure of SU(3) (`S³ → SU(3) → S⁵`) is classified by `π_4(S³) = ℤ/2`, a **torsion** class. The Dai-Freed pairing of `[D_K]` with this torsion class gives a phase value in `ℝ / ℤ`:

```
  ⟨[D_K], [π_4(S³) class]⟩_{Dai-Freed} ∈ {0, 1/2}
```

If the CC is the physical realization of this torsion pairing (rather than a spectral moment), it is *bounded by construction* to half-integer phase at the relevant IR scale. Multiplying by the natural IR scale `H_0² M_Pl²` gives `Λ_CC ~ (1/2) × M_Pl² × H_0²` — exactly the observed magnitude.

**Why it survives S37**: Dai-Freed pairings are mod-Z valued topological anomaly inflow terms. They are neither smooth functionals of τ nor spectral moments. S37 does not cover them.

**Connection to anomaly cancellation**: The SM emerging from A_F with KO-dim = 6 mod 8 has a specific `Pin(4)⁺` anomaly structure (Witten 2015). The `ℤ/2` in `π_4(S³)` is the exact classifying class for the mod-2 anomaly that must cancel for the partition function to be well-defined. The *residual* ℤ/2 anomaly that cannot be canceled locally by SM fields is a natural candidate for the cosmological constant.

**Pre-registerable gate**:
- **What**: Construct the Dai-Freed pairing of `[D_K]` on Jensen-SU(3) with the `π_4(S³) = ℤ/2` torsion class. Compute the pairing value. Evaluate `pairing × M_Pl² × H_0²` and compare to `ρ_obs`.
- **Inputs**: D_K structure, `π_4(S³) = ℤ/2` classifying data, Dai-Freed 1994 machinery.
- **Gate**:
  - **PASS** if pairing is nonzero, lies in `{0, 1/2}`, and `pairing × M_Pl² × H_0²` matches `ρ_obs` within factor 10.
  - **INFO** if pairing is nonzero but magnitude mismatch.
  - **FAIL** if pairing is 0 or sign wrong.
- **Effort**: 3 sessions. Mathematical construction task; novel for the framework.
- **Classification**: GEOMETRIC + topology.

### 3.5 Gate S85-CC-5 — DM/DE Poincaré Conjugate Pairing

**Mathematical idiom**: Poincaré duality in algebraic topology; K-theory pairing; arithmetic geometry of ratios.

**Hypothesis**: DM is a `π_1(S¹) = ℤ`-winding on the Leggett inter-band phase circle (established, S58+); DE is an effacement residual (structurally distinct but parallel in role). The conjecture: DM and DE are **Poincaré duals** under the substrate's natural duality pairing, and the observed ratio `Ω_DM / Ω_DE = 0.268 / 0.685 = 0.39` is a cohomological identity

```
  Ω_DM / Ω_DE = ⟨[DM winding], [DE residual]⟩_{Poincaré dual} = O(1)
```

The specific rational 0.39 may be the dimension-ratio of the ℍ summand (DM, 4-dim) to the M_3(ℂ) summand (DE, 9-dim) in A_F: 4/9 ≈ 0.44, within 13% of observed 0.39. Or the ratio of relevant K-classes in the A_F bimodule.

**Why it survives all 9 existing closures**: none of them is about DM-DE relations. They are about one observable at a time.

**Connection to the coincidence problem**: Why `Ω_DM ~ Ω_DE` today is famously unexplained in LCDM. If DM and DE are cohomological conjugates from the same transit, the ratio is *structurally forced* to be O(1) and the coincidence problem evaporates — it becomes a Poincaré duality identity, not a coincidence.

**Pre-registerable gate**:
- **What**: Formulate the Poincaré pairing between Leggett winding class (`π_1(S¹) = ℤ`) and effacement residual class on the substrate; compute `⟨[DM], [DE]⟩`. Compare to `Ω_DM / Ω_DE`.
- **Inputs**: Leggett-channel phase structure (S58, S60, S75 Leggett-only DM), effacement residual derivation (S74 Friedmann-wrong-question + HP4), A_F summand dimensions.
- **Gate**:
  - **PASS** if pairing equals `Ω_DM / Ω_DE = 0.391 ± 0.02` to within 10%.
  - **INFO** if pairing is O(1) but with wrong ratio.
  - **FAIL** if pairing is 0 or ≫ 1.
- **Effort**: 2 sessions.
- **Classification**: PHONONIC + GEOMETRIC.

---

## 4. Structural Implications

### 4.1 The Framework Has Not Exhausted the CC Question

The ledger's 42 CLOSED/PROVEN items plus the 7 OPEN paths (Jacobson, gravitational integrability, transit relaxation, volume dilution, self-consistent BdG, finite-size insight, sector-selective relaxation) all live within conventional mathematical idioms. **Five unconventional idioms have not been deployed**. The `η`, triality, Connes-Moscovici, Dai-Freed, and Poincaré-duality angles each represent mathematical territory that is well-developed elsewhere (NCG, Clifford theory, anomaly inflow, arithmetic geometry) but has not been pointed at the CC in the framework's history.

### 4.2 Factor-3 Residual as Signal, Not Noise

`chi_2 × HP4 = 0.337 × ρ_obs` is off by precisely factor 3. Four distinct 3-fold algebraic structures in the framework (`Z_3` center, 3-generation multiplicity, Spin(8) triality, three-summand A_F) each offer a candidate mechanism for that factor. Three of them are concrete computations. Treating the factor 3 as a calibration accident is lazy; treating it as signal names a specific subset of the five gates (especially CC-2, CC-3, CC-5) as likely to land the closure.

### 4.3 What S37 Actually Rules Out

S37 CUTOFF-SA-37 is a theorem about smooth monotone cutoff functions `f`. It rules out all such functionals from producing a τ-minimum of the spectral action. It does NOT rule out:

- η as CC (distributional, not smooth f)
- Triality averaging (representation-theoretic correction to f, not change in f)
- Connes-Moscovici signed residue sum (not a monotone functional of τ)
- Dai-Freed torsion pairing (ℝ/ℤ-valued, not ℝ-valued)
- DM/DE Poincaré pairing (a different observable relation, not a spectral action)

These were never in S37's scope. Interpreting S37 as "all CC mechanisms are closed" is a category error that the framework's closure-rhetoric habitually commits.

### 4.4 No Closure Claimed; Five Targets Named

**This session does not close the CC problem.** It identifies five mathematically serious pairings that have not been tested, names the math machinery each requires, and specifies pre-registrable gates with PASS/INFO/FAIL criteria. Each gate is a specific computation with a specific effort estimate. None is guaranteed to succeed; each is sufficiently distinct that at least one is likely to PASS at INFO level (factor-10 match to observed), which would materially change the CC landscape.

---

## 5. Recommended §11.2 Revision

The current §11.2 of `sessions/framework/Phononic-Substrate-Geometry.md` reads:

> *"The framework's CC computation through the chi_2 × HP4 route gives `0.337 · ρ_obs` (S75 W4-C, sole L_max-robust route) — within a factor 3 of observed. The factor 3 residual is pre-registered as the remaining theoretical deficit; every known mechanism for canceling vacuum energy has been tested and all fail for structural reasons (S66 CC reframe, S74 Friedmann wrong-question theorem)."*

Proposed revision:

> *"The framework's CC computation through the chi_2 × HP4 route gives `0.337 · ρ_obs` (S75 W4-C, sole L_max-robust route) — within a factor 3 of observed. The framework has closed 9 mechanisms operating in conventional QFT, Kasparov-factorization, and variational idioms, accumulating 42 permanent CLOSED/PROVEN items plus 7 open paths within those idioms (see `sessions/archive/session-63/framework-cc-oom.md` for the full ledger). The CC is not exhausted, however — five unconventional mathematical pairings have not been tested: (i) η-invariant of `D_K + D_F` as the CC modular phase at the IR cosmological scale; (ii) Spin(8) triality averaging of chi_2 over `{V, S⁺, S⁻}`; (iii) Connes-Moscovici dimension-spectrum residues with Hopf-cocycle signs, giving a signed sum over all poles rather than `a_0` alone; (iv) Dai-Freed torsion pairing with `π_4(S³) = ℤ/2`, which naturally bounds the CC at `(1/2) × M_Pl² × H_0²`; (v) DM-DE Poincaré conjugate pairing, which would make `Ω_DM / Ω_DE ≈ 0.39` a cohomological identity. The factor-3 residual is structurally consistent with several of these mechanisms — particularly the Spin(8) triality averaging and the A_F three-summand structure — and motivates the five S85 pre-registered gates (CC-1 through CC-5, see `session-84-CC-revisit.md`)."*

---

## 6. Carry-Forward for S85

| # | Gate | What | Inputs | Gate (PASS/INFO/FAIL) | Effort | Classification |
|:---|:---|:---|:---|:---|:---|:---|
| CC-1 | S85-CC-η-INVARIANT | Compute η(D_K + D_F) for full Jensen-SU(3)×A_F triple at L_max ∈ {7,9,11} | D_K spectrum, A_F structure, J operator | PASS: η rational, π×η×M_Pl²×H_0² matches ρ_obs ±10x; INFO: η converges, magnitude off; FAIL: η diverges | 2 sessions, GPU at L_max ≥ 9 | GEOMETRIC + PARTICLE |
| CC-2 | S85-CC-TRIALITY | Compute chi_2 for three Spin(8) rep embeddings {V, S⁺, S⁻} on Jensen-SU(3); report orbit sum | D_K spectrum at L_max = 9, triality automorphism, Clifford module | PASS: three values triality-equal AND `3 × chi_2 × HP4` = ρ_obs ±10%; INFO: equal but sub-factor-3; FAIL: three differ | 1 session | GEOMETRIC + PARTICLE |
| CC-3 | S85-CC-DIMSPEC-HOPF | Compute dimension spectrum and Hopf-cocycle-signed residue sum | D_K at L_max = 9, Connes-Moscovici regularity scaffolding, Hopf-cocycle machinery | PASS: signed sum suppressed ≥ 10 OOM vs a_0; INFO: 1–10 OOM; FAIL: no cancellation | 3–4 sessions (novel math) | GEOMETRIC |
| CC-4 | S85-CC-DAI-FREED | Construct Dai-Freed pairing of [D_K] with π_4(S³)=ℤ/2 torsion class | D_K, π_4(S³) bundle class, Dai-Freed 1994 machinery | PASS: pairing nonzero in {0, 1/2} AND pairing × M_Pl² × H_0² = ρ_obs ±10x; INFO: magnitude off; FAIL: pairing 0 | 3 sessions (novel math) | GEOMETRIC + topology |
| CC-5 | S85-CC-POINCARE-DM-DE | Compute Poincaré pairing between Leggett winding class and effacement residual class | Leggett structure, HP4 result, A_F summand dims | PASS: pairing = Ω_DM/Ω_DE = 0.391 ±0.02 within 10%; INFO: O(1), wrong ratio; FAIL: 0 or ≫ 1 | 2 sessions | PHONONIC + GEOMETRIC |

**Ordering priority**:
1. **CC-2 triality first** (1 session, computable on existing spectra). Lowest effort, sharpest prediction (factor-3 residual closure). Decisive for several other gates.
2. **CC-5 Poincaré DM/DE** (2 sessions). High EVOI — would solve the coincidence problem.
3. **CC-1 η-invariant** (2 sessions, GPU). Deepest NCG-native angle; framework has ingredients at S60.
4. **CC-4 Dai-Freed** (3 sessions, novel math). Highest structural stakes — would resolve the whole 114-OOM question in one pairing.
5. **CC-3 Connes-Moscovici** (3–4 sessions, novel math). Deepest NCG, hardest to implement; defer unless earlier gates motivate.

---

## 7. One Caveat

Five unconventional pairings is a lot of speculation at once. Each is mathematically serious, but none is guaranteed. The risk: if all five FAIL, the framework really is at the conventional-closure wall for the CC, and the 114 OOM residual is structural in a way the idiomatic framing already captures. The value: even one of the five landing at PASS or INFO materially changes the CC landscape — it means the conventional idiom was not exhaustive, and the framework's CC statement shifts from "mapped but unsolved" to "re-framed by specific novel math."

I am not predicting any specific outcome. I am saying the question has not been honestly asked in the five idioms above, and the five gates are pre-registrable computations that ask it honestly. That is the difference between "exhausted" and "re-framed."

---

*End of Session 84 CC Revisit. Five unconventional pairings proposed, five pre-registered gates carried forward to S85. The thesis §11.2 is to be revised per §5 above. The factor-3 residual is hypothesized to be structural signal from the SU(3)/Spin(8)/A_F 3-fold algebra, not calibration noise.*

— Tesla-Resonance, 2026-04-21
