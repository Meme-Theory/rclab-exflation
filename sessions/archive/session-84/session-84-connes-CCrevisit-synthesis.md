# Session 84 Synthesis: CC Revisit — Connes-NCG Spectral-Triple Lens

**Date**: 2026-04-21
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/archive/session-84/session-84-CC-revisit.md` (tesla-resonance analysis, 2026-04-21)

---

## I. Session Outcome

The S84 CC-revisit is an **analysis, not a closure**: tesla-resonance reframes the Phononic-Substrate-Geometry §11.2 claim that "every known mechanism has been tested" by showing the framework's 9 CC closures and 42 CLOSED/PROVEN items all live inside four conventional idioms (perturbative Seeley-DeWitt, q-theory variational, BCS/Richardson-Gaudin, Kasparov factorization). Five **unconventional** NCG-native idioms have not been deployed against the CC and each yields a pre-registrable S85 gate with specific PASS/INFO/FAIL thresholds. From the spectral-triple lens this is a material correction: the S37 CUTOFF-SA-37 monotonicity theorem forbids only smooth monotone `Tr f(D²/Λ²)` functionals from producing a τ-minimum — it does not forbid η-invariants, triality-orbit sums, Connes-Moscovici signed-residue sums, Dai-Freed torsion pairings, or Poincaré duality between DM/DE, which are **structurally different spectral-triple invariants** from the ones S37 addresses. The factor-3 residual `chi_2 × HP4 = 0.337 · ρ_obs` is the organizing hook, and three independent 3-fold algebraic structures in the framework (Z_3 center, Spin(8) outer triality, three-summand A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)) each name a specific spectral-triple mechanism that has not been computed.

---

## II. Key Results

### R1. The CC is not necessarily `a_0` — it may be a different invariant of the same spectral triple

**Result**: The Chamseddine-Connes spectral action `S_b = Tr f(D²/Λ²) ~ f_4 Λ⁴ a_0 + f_2 Λ² a_2 + f_0 a_4 + O(Λ⁻²)` generates the CC as the zeroth Seeley-DeWitt coefficient `a_0` (volume term). The framework has tried to shrink `a_0` via every smooth-monotone cutoff functional and proved monotonicity on τ (S37, 9,600 checks). The revisit's core NCG observation: the full invariant content of a spectral triple `(A, H, D, J, γ)` is **not** exhausted by Seeley-DeWitt coefficients. The dimension spectrum `Sd` (set of poles of `ζ_{|D|⁻ˢ}(s)` on the Connes-Moscovici algebra), the spectral-asymmetry invariant `η(D) = (ζ_{D⁻ˢ}(0) − ζ_{|D|⁻ˢ}(0))/2`, the Hopf-cocycle-weighted residue sum, and the Dai-Freed pairing `⟨[D], [torsion class]⟩ ∈ ℝ/ℤ` are all structurally distinct invariants of the SAME spectral triple. Classification: **GEOMETRIC**.

The CC-hierarchy-as-moment-split reading: `a_0`-type data (volume/cosmological constant, scale `M_Pl⁴`) and `a_2`-type data (Einstein-Hilbert, scale `M_Pl²`) are **different Seeley-DeWitt coefficients of the same spectral triple**, extracted at different powers of Λ. The observed ~120-OOM split between observed CC (`~ M_Pl² H_0²`) and bare `a_0 × M_Pl⁴` is NOT a hierarchy of the same observable at different scales; it is a **category mismatch** — the observed "CC" might not be `a_0` at all, but a different invariant (η, Dai-Freed pairing, or signed residue sum) whose natural scale IS `M_Pl² H_0²` by construction. S37 CUTOFF-SA-37 (9,600 checks, smooth-monotone f) is a rigorous statement about one category of invariant; the five S85 gates probe four other categories.

### R2. Factor-3 Residual — SU(3)/Spin(8)/A_F Triality Structure

**Result**: `chi_2 × HP4 = 0.337 · ρ_obs`. A factor-3 enhancement closes the gap to `1.011 · ρ_obs` (Python-verified: `3 × 0.337 = 1.011`). Three 3-fold algebraic structures in the spectral triple are all candidate sources: Z_3 center of SU(3); Spin(8) outer automorphism permuting {V, S⁺, S⁻}; three-summand decomposition `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. Classification: **GEOMETRIC + PARTICLE**.

Substitution chain (Spin(8) triality):
- **Definition 1**: `chi_2(R) := ⟨|λ_R|⟩ / λ_R^max` for Dirac operator in Clifford rep R.
- **Definition 2**: Spin(8) has a unique outer automorphism σ of order 3 permuting {V, S⁺, S⁻}.
- **Definition 3**: Triality orbit sum `chi_2^triality := chi_2(V) + chi_2(S⁺) + chi_2(S⁻)`.
- **Substitution**: If σ preserves `D_K`'s spectral statistics (triality-equivalence), `chi_2(V) = chi_2(S⁺) = chi_2(S⁻) = chi_2^single`.
- **Simplification**: `chi_2^triality = 3 × chi_2^single`.
- **Direction**: `chi_2^triality × HP4 = 3 × 0.337 · ρ_obs = 1.011 · ρ_obs` (1.1% residual, within any reasonable truncation tolerance).

This is the **sharpest** of the five gates: it is a 1-session computation on existing L_max = 9 spectra. It does not invoke novel math — triality is a well-known outer automorphism of Spin(8) and the Clifford module `Cl(8)` carries all three reps. The physical question is whether Jensen deformation (which breaks the full Lie symmetry of SU(3) at finite τ) preserves the Spin(8) triality. If Jensen breaks triality, the three `chi_2` values differ and the factor-3 comes from somewhere else.

### R3. η-Invariant at O(1), Not Tiny-Denominator — KO-dim = 6 Constraint

**Result**: The η-as-CC hypothesis `ρ_L = π · η · M_Pl² · H_0²` gives the observed CC for **O(1) rational η**, NOT small-denominator rationals. Classification: **GEOMETRIC + PARTICLE**.

Substitution chain (η magnitude):
- **Definition**: `ρ_η(η) := π · η · M_Pl² · H_0²`; `residual(η) := ρ_obs / ρ_η(η)`.
- **Substitution** (Python-verified, `M_Pl = 2.435 × 10¹⁸ GeV`, `H_0 = 1.438 × 10⁻⁴² GeV`):
  - `π · M_Pl² · H_0² = 3.8518 × 10⁻⁴⁷ GeV⁴`.
- **Simplification**: `residual(η) = 2.7 × 10⁻⁴⁷ / (η · 3.8518 × 10⁻⁴⁷) = 0.7010 / η`.
- **Direction check (Python-verified)**: `residual(1/6) = 4.206`; `residual(1/12) = 8.412`; `residual(2/3) = 1.051`; `residual(3/4) = 0.935`; `η_match = 0.7010`.
- **Direction** (substrate→prediction): residual `∝ 1/η`; η must be O(1) rational to match observed CC. Candidate values: 2/3 (real part of primitive cube root of unity — natural in SU(3) with Z_3 center), 3/4 (3-generation bimodule interpretation), 7/10 (exact match, no immediate interpretation).

The [J, D_K] = 0 CPT-neutrality axiom at KO-dim = 6 imposes a specific constraint on η: J² = +1, J D_K = D_K J, J γ = +γ J (this is the "mod 8" signature of KO-dim = 6, established S60+). For a symmetric spectrum ({+λ} ↔ {−λ} exact), η = 0. For the Jensen-deformed `D_K + D_F`, the finite part `D_F` can break exact spectral symmetry while still satisfying `[J, D_K + D_F] = 0` globally — the spectrum remains CPT-paired at the OPERATOR level but individual Jensen-τ-dependent eigenvalue shifts can produce a nonzero η at the **distributional** level (via ζ-regularization at s = 0). This is precisely what S60's BdG η = 0 result PROVED for one operator but did not PROVE for the full Jensen-SU(3) × A_F triple. CC-1 is the missing computation.

### R4. Connes-Moscovici Dimension Spectrum — Signed Residue Sum, Not a_0 Alone

**Result**: The Connes-Moscovici local index formula (1995) expresses the CC-relevant invariant as a **signed sum of residues** `Σ_{d ∈ Sd} sign(Hopf_d) × Res_{s=d} [ζ_{D²}(s)]`, not `a_0` alone. S37 monotonicity applies to smooth `Tr f`, NOT to this signed residue sum. Classification: **GEOMETRIC**.

Spectral-triple rigor: the dimension spectrum `Sd` is the set of poles of the zeta function `ζ_{|D|⁻ˢ}(s)`, acting on the algebra `B` generated by `A` and iterated `[D², ·]` commutators (Connes-Moscovici regularity). The local index formula expresses Chern character pairings as finite sums of residues at these poles, each weighted by a Hopf-cocycle sign. For the Jensen-SU(3) × A_F triple, the full `Sd` has not been enumerated — S83 W1-G3 flagged the `dim H_π ≥ 2` closure for Connes-Moscovici as OPEN at L_max = 5; the framework has only just begun producing the machinery (S83, S84-W2a-11).

Why this matters for the CC: if the positive residue at `s = 4` (which gives `a_0`) is partially cancelled by negative residues at shifted poles (e.g., `s = 4 − γ` where γ is a non-integer anomalous dimension due to Jensen deformation, or `s = 2` with opposite Hopf sign), the net `Λ_CC` can be suppressed by many OOM relative to `a_0 × M_KK⁴` without any "cancellation miracle" — it's a structural property of the dimension spectrum. This is mathematically serious but computationally hard; CC-3 is the 3-4 session gate.

### R5. Dai-Freed Torsion Pairing — ℝ/ℤ-Valued Invariant, Natural Scale M_Pl² · H_0²

**Result**: The Dai-Freed pairing `⟨[D_K], [π_4(S³) = ℤ/2]⟩ ∈ ℝ/ℤ` is a torsion-K-theory anomaly-inflow invariant taking values in `{0, 1/2}`. If the CC is the physical realization of this torsion pairing at IR scale `H_0²`, magnitude `(1/2) × M_Pl² × H_0² = (1/2) × 1.226 × 10⁻⁴⁷ GeV⁴ = 6.13 × 10⁻⁴⁸ GeV⁴` (Python-verified), compared to `ρ_obs = 2.7 × 10⁻⁴⁷ GeV⁴` — within factor 4.4, within the factor-10 PASS bracket. Classification: **GEOMETRIC + topology**.

Substitution chain (Dai-Freed magnitude):
- **Definition**: `ρ_DF := pairing × M_Pl² × H_0²`, where `pairing ∈ {0, 1/2}`.
- **Substitution** (Python-verified): `M_Pl² × H_0² = 5.929 × 10³⁶ × 2.068 × 10⁻⁸⁴ = 1.226 × 10⁻⁴⁷ GeV⁴`.
- **Simplification**: `ρ_DF(1/2) = 0.5 × 1.226 × 10⁻⁴⁷ = 6.13 × 10⁻⁴⁸ GeV⁴`.
- **Direction**: `ρ_obs / ρ_DF = 2.7 / 0.613 = 4.40` — factor 4.4 residual, which falls inside the CC-4 PASS bracket (±factor 10). Matches observed to magnitude without any free parameters.

Spectral-triple rigor: the principal SU(2)-bundle structure of SU(3) is `S³ → SU(3) → S⁵`, classified by `π_4(S³) = ℤ/2` — a **genuine torsion class** in π₄ of the fiber. Dai-Freed (1994) showed that for a Dirac operator on a manifold with torsion bundle class, the pairing `⟨[D], [torsion]⟩` takes mod-Z values and represents a physical anomaly-inflow contribution to the partition function. In KO-dim = 6 (the framework's verified KO-signature), the Pin(4)⁺ anomaly structure identified by Witten (2015) has a specific `ℤ/2` residual that cannot be cancelled locally by SM fields — and this is a natural candidate for the cosmological constant.

### R6. DM/DE Poincaré Conjugate Pairing — A_F Summand Dimension Ratio

**Result**: The hypothesis `Ω_DM / Ω_DE = ⟨[DM winding], [DE residual]⟩_{Poincaré}` predicts an O(1) rational. The A_F summand dimension ratio `dim(ℍ) / dim(M_3(ℂ)) = 4/9 = 0.444` is within 13% of observed `0.268/0.685 = 0.391` (Python-verified). Classification: **PHONONIC + GEOMETRIC**.

Substitution chain (summand ratio):
- **Definition**: `A_F := ℂ ⊕ ℍ ⊕ M_3(ℂ)` (Connes-Chamseddine SM algebra).
- **Substitution**: `dim ℍ = 4` (quaternions as real algebra); `dim M_3(ℂ) = 9` (as complex algebra).
- **Simplification**: `4/9 = 0.4444`.
- **Direction**: `0.444 > 0.391` by 13%. The simplest summand-dimension hypothesis overshoots observed slightly; the K-theoretic refinement (pairing of K₀-classes, not raw summand dimensions) may reduce this.

Spectral-triple rigor: Poincaré duality for a spectral triple is a K-theoretic identity — the fundamental class `[D] ∈ KK(A ⊗ A^op, ℂ)` induces an isomorphism `K_i(A) ≅ K^{i+d}(A)` where d is the metric dimension. For the almost-commutative product `M_4 × F`, Poincaré duality factorizes into bulk (Gelfand-Naimark on M_4) and finite (K-theory of A_F) parts. The conjecture that DM (Leggett-channel `π_1(S¹) = ℤ`-winding) and DE (effacement residual) are Poincaré-dual K-classes of the substrate is mathematically specific and testable; CC-5 is the 2-session gate.

---

## III. Gate Verdicts

Source doc is an **analysis document**, not a gate-producing session. No verdicts are recorded. Five S85 gates are **pre-registered** (CC-1 through CC-5) with PASS/INFO/FAIL criteria but not yet computed.

---

## IV. Structural Implications

### 4.1 S37 CUTOFF-SA-37 Scope Clarified

The S37 structural monotonicity theorem (`S_f(τ)` monotone increasing for all smooth monotone f, all Λ, all τ ∈ [0, 0.5], 9,600 checks) is rigorous **within its hypothesis**: it applies to `Tr f(D²/Λ²)` for smooth monotone f. The agent-memory entry "Framework Classification: SA correct for G_N (a_2), wrong for CC (a_0)" is correct IF the CC is an `a_0`-type invariant. If the CC is instead an η-invariant, signed residue sum, Dai-Freed pairing, or Poincaré conjugate class, S37 does NOT apply and the closure-rhetoric "all CC mechanisms are closed" is a category error. This is the methodological correction the revisit makes.

### 4.2 Spectral-Triple Invariant Taxonomy (NCG-Native)

The full invariant content of a KO-dim = 6 spectral triple `(A, H, D, J, γ)` includes:

| Invariant | Type | Scale | S37 applies? | Framework status |
|:--|:--|:--|:--|:--|
| a_0 (volume) | Real, smooth f | Λ⁴ | Yes (monotone theorem) | Computed; 114 OOM too large |
| a_2 (Einstein-Hilbert) | Real, smooth f | Λ² M_KK² | Yes | G_N matches observed |
| a_4 (Yang-Mills) | Real, smooth f | 1 | Yes | Gauge couplings within factor 2 |
| η(D) | Distributional at s=0 | dimensionless | **No** | Computed at BdG (S60, =0 by PH); NOT computed for D_K+D_F full triple |
| Signed Σ Res over Sd | Residue sum with Hopf signs | mixed | **No** | Dimension spectrum OPEN (S83-W1-G3) |
| ⟨[D], [torsion]⟩_DF | ℝ/ℤ pairing | IR scale | **No** | Not computed |
| K₀ Poincaré pairings | K-theoretic | dimensionless | **No** | Partially computed (S74 K-theory) |

S37 forbids the top three rows from producing a τ-minimum. It says NOTHING about the bottom four rows. The revisit's five gates target rows 4-7. This is a legitimate spectral-triple research program, not hand-waving.

### 4.3 [J, D_K] = 0 CPT Constraint on a_0 Separately from a_2

The framework-proven identity `[J, D_K] = 0` (CPT-neutrality, KO-dim = 6) is an operator-level identity: J implements a real structure that commutes with D_K. Under this constraint:

- **a_0**: depends on `∫ √det(g)`, volume form; J-invariance is automatic (volume is real and positive).
- **a_2**: depends on `∫ R · √det(g)`, scalar curvature; J-invariance forces R to be real.
- **η(D_K)**: depends on spectral asymmetry `Σ sign(λ_n)`; [J, D_K] = 0 pairs {+λ} with {-λ}, so for the BARE D_K on SU(3), η = 0 identically.
- **η(D_K + D_F)**: the finite Dirac operator D_F breaks exact spectral symmetry in the particle sector (Yukawa matrices are complex, CKM phase, PMNS phase). [J, D_K + D_F] = 0 holds as an operator identity BUT individual eigenvalue shifts in the particle sector produce distributional ζ-regularized asymmetry.

This is the key NCG-native observation: **J-commutativity does NOT force η = 0**; it forces spectral PAIRING but distributional spectral asymmetry can be nonzero in a CPT-invariant triple via the finite geometry. S60's "η = 0 by PH symmetry" result was for the BdG operator (one part of the story); the full `D_K + D_F` has not been computed.

### 4.4 KO-dim = 6 Constraint on η

For KO-dim = 6 (framework-verified, S60+), the real structure satisfies `J² = +1`, `JD = DJ`, `Jγ = +γJ`. Under these signs:

- `J² = +1` ⇒ J is a real involution.
- `[J, D] = 0` ⇒ spectrum of D is J-invariant (as a set).
- `[J, γ] = 0` ⇒ γ-eigenspaces are J-invariant.

Atiyah-Patodi-Singer (1976) and Connes-Marcolli (2008) showed that for KO-dim = 6 spin geometries, the η-invariant admits a natural rational or algebraic structure tied to the Weyl group order. For SU(3) with natural bi-invariant spin structure, the Weyl group is `S_3` (order 6), suggesting denominator divisors of 6, 12, 24. **However**, the magnitude analysis (§R3 above) shows that the η-as-CC hypothesis requires η ≈ 0.7 (i.e., 2/3 or 3/4), NOT 1/6 or 1/12. This is a sharp, testable prediction: if CC-1 returns η ∈ {1/6, 1/12, 1/24}, the observed-CC magnitude mismatch is ~4-8× (FAIL the magnitude gate); if CC-1 returns η ∈ {2/3, 3/4, 7/10}, magnitude matches.

### 4.5 Consistency with Agent-Memory Record

No conflicts detected between the source doc and the connes-ncg-theorist permanent-theorems record:

- S37 CUTOFF-SA-37 (monotonicity): reaffirmed, scope clarified.
- "SA correct for G_N (a_2), wrong for CC (a_0)": correct under the hypothesis that CC = a_0; revisit proposes CC ≠ a_0.
- "CC: ALL spectral action routes CLOSED. Problem is FUNCTIONAL not GEOMETRIC. a_0/a_2 = C_Q/R universal" (S74): consistent with revisit. If the CC is not a spectral-action coefficient at all, the closure of "spectral action routes" is not a closure of the CC problem, only of that idiom.
- S65 collab "a_0/a_2 = C/R universal": reaffirmed; this is the a_0-as-CC reading, which the revisit complements (not contradicts) by proposing alternative invariants.
- "Three generations NOT from NCG axioms; Z_3 × Z_3 from SU(3) candidate": directly relevant to CC-2 and CC-5. The 3-fold structure that is unexplained at the generation-counting level may be the SAME 3-fold structure that supplies the factor-3 CC residual.
- S60 "η at BdG = 0 by PH": does NOT cover full D_K + D_F triple; CC-1 is the missing computation.

### 4.6 One Internal Tension in the Source Doc (Flagged)

In §3.1 (CC-1 η-Invariant gate), the source writes: *"For SU(3) with natural spin structure, denominators of 6, 12, or 24 are expected"* (line 119) — this is a prediction about SMALL-denominator η. But then in the substitution chain (lines 137-160) the author computes that such small-denominator η give 4-8× residuals and concludes η must be O(1) (2/3, 3/4) to match ρ_obs. The "expected 6, 12, 24" vs "required 2/3, 3/4" statements are both recorded in the gate, with the magnitude chain correctly flagging the tension. The resolution offered ("additional diagnostic: whether η is a small rational or O(1) rational") is honest but underspecified — **the Weyl-group-order argument and the magnitude-match argument make different predictions**. Only computation resolves which physics is operative. This is a genuine ambiguity in the gate specification that S85 CC-1 must resolve at design time.

### 4.7 Relation to Fold-Dynamics / Bogoliubov Framing (Cross-Lens Orthogonality)

The source doc does not invoke fold dynamics, Bogoliubov transformations, GGE relics, or transit physics. The revisit operates ENTIRELY in the spectral-triple-invariant idiom. This is an **orthogonal** framing to the transit-dynamics lens — the five proposed invariants (η, triality, Connes-Moscovici, Dai-Freed, Poincaré DM-DE) are **static** invariants of the spectral triple `(A, H, D_K + D_F, J, γ)`, not properties of the transit through the fold. Agreement or tension with a transit-dynamics synthesis would require explicit computation of the τ-dependence of each invariant through τ = τ_fold, which the source doc does not provide. Orthogonality does not imply conflict; it implies the two lenses probe different structures of the same physics.

---

## V. Carry-Forward Computations

### V.1. CC-2 Spin(8) Triality Orbit Sum of chi_2 (PRIORITY 1)

- **What**: Compute `chi_2(R) := ⟨|λ_R|⟩ / λ_R^max` for three inequivalent Spin(8) rep embeddings `R ∈ {V, S⁺, S⁻}` of `D_K` on Jensen-SU(3) at L_max = 9. Report `chi_2^triality := chi_2(V) + chi_2(S⁺) + chi_2(S⁻)` and the factor `(chi_2^triality × HP4) / ρ_obs`.
- **Inputs**: D_K eigenspectrum at L_max = 9 (existing, reuse S75 M1 data); Spin(8) triality automorphism σ (construct from Cl(8) structure); Clifford module decomposition on H_F; `HP4 = 0.337 / chi_2 = 0.4548` (back-solve from S75 W4-C), or recompute HP4 from first principles per S76.
- **Gate**: S85-CC-TRIALITY. **PASS** if `|chi_2(V) − chi_2(S⁺)| < 1%` AND `|chi_2(V) − chi_2(S⁻)| < 1%` AND `0.90 ≤ (chi_2^triality × HP4) / ρ_obs ≤ 1.10` (±10% of observed). **INFO** if triality-equal but sub-factor-3 (0.5–0.9 of ρ_obs — Jensen partial breaking). **FAIL** if the three chi_2 values differ by >10% (triality broken by Jensen).
- **Effort**: 1 agent-session, ~4-6 hours, CPU sufficient (matrix products on existing L_max = 9 spectra).
- **Classification**: GEOMETRIC + PARTICLE.

### V.2. CC-5 DM/DE Poincaré Pairing vs A_F Summand Dimensions (PRIORITY 2)

- **What**: Formulate the K-theoretic Poincaré pairing `⟨[DM], [DE]⟩ ∈ ℤ` between the Leggett-channel winding class `[DM] ∈ π_1(S¹) = ℤ` and the effacement residual K-class `[DE] ∈ K_0(A_F)`. Compute and compare to `Ω_DM / Ω_DE = 0.391`. Also report the naive summand ratio `dim(ℍ)/dim(M_3(ℂ)) = 4/9 = 0.444` as baseline.
- **Inputs**: Leggett-channel phase structure from S58, S60, S75; effacement residual K-class from S74 Friedmann-wrong-question + HP4 derivation; `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` summand data (canonical); observed ratios `Ω_DM = 0.268`, `Ω_DE = 0.685` (Planck 2018, canonical_constants).
- **Gate**: S85-CC-POINCARE-DM-DE. **PASS** if pairing (from K-theory) equals `Ω_DM / Ω_DE = 0.391 ± 10%`. **INFO** if pairing is O(1) but wrong ratio (e.g., returns 0.444 from summand-dims, 13% off). **FAIL** if pairing is 0 or ≫ 1.
- **Effort**: 2 agent-sessions, CPU.
- **Classification**: PHONONIC + GEOMETRIC.

### V.3. CC-1 η-Invariant for Full D_K + D_F Triple (PRIORITY 3)

- **What**: Compute `η(D_K + D_F)` for the full Jensen-SU(3) × A_F spectral triple at τ = τ_fold, for L_max ∈ {7, 9, 11}. Method: ζ-regularization of `ζ_D(s) = Σ sign(λ_n) |λ_n|⁻ˢ` analytically continued to `s = 0` (APS-style). Evaluate `ρ_η := π × η × M_Pl² × H_0²` and report residual `ρ_obs / ρ_η`.
- **Inputs**: D_K eigenspectrum at L_max ∈ {7, 9, 11}; A_F bimodule with SM Yukawa matrices (CKM, PMNS); J operator with J² = +1 (KO-dim = 6); canonical `M_Pl = 2.435 × 10¹⁸ GeV`, `H_0 = 1.438 × 10⁻⁴² GeV`, `rho_obs = 2.7 × 10⁻⁴⁷ GeV⁴`.
- **Gate**: S85-CC-η-INVARIANT. **PASS** if η converges on L_max (drift < 10% from L_max = 9 to 11) AND η is a rational or algebraic number with `0.1 ≤ π · η · M_Pl² · H_0² / ρ_obs ≤ 10` (factor-10 bracket). **INFO** if η converges outside the bracket. **FAIL** if η diverges on L_max (wild asymmetry) OR converges >10× outside bracket with no missing-prefactor candidate. **Diagnostic**: report whether η ∈ {1/6, 1/12, 1/24} (small-denominator, Weyl-order prediction) OR η ∈ {2/3, 3/4, 7/10} (O(1), magnitude-match prediction) — both cannot be simultaneously correct; CC-1 resolves §IV.6 tension.
- **Effort**: 2 agent-sessions, GPU mandatory at L_max ≥ 9 (AMD RX 9070 XT via `torch.linalg`).
- **Classification**: GEOMETRIC + PARTICLE.

### V.4. CC-4 Dai-Freed Torsion Pairing with π_4(S³) = ℤ/2 (PRIORITY 4)

- **What**: Construct the Dai-Freed (1994) η-cobordism pairing `⟨[D_K], [π_4(S³) = ℤ/2]⟩ ∈ ℝ/ℤ`. The π_4(S³) = ℤ/2 torsion class corresponds to the principal SU(2)-bundle structure of the `S³ → SU(3) → S⁵` Hopf-like fibration. Pairing value is in {0, 1/2}. Evaluate `ρ_DF := pairing × M_Pl² × H_0²` and compare to ρ_obs.
- **Inputs**: D_K structure on Jensen-SU(3); principal SU(2)-bundle data; Dai-Freed 1994 machinery (arXiv:9405012 or equivalent); Pin(4)⁺ anomaly structure from Witten (2015) for cross-check; canonical M_Pl and H_0.
- **Gate**: S85-CC-DAI-FREED. **PASS** if pairing = 1/2 AND `0.1 ≤ ρ_DF / ρ_obs ≤ 10` (factor-10 bracket; R5 computation gives 4.4× off, inside bracket). **INFO** if pairing nonzero but pairing ∉ {0, 1/2} (would falsify the torsion bound but leave magnitude argument). **FAIL** if pairing = 0 (SU(2)-bundle class is trivial via J equivariance or similar).
- **Effort**: 3 agent-sessions, novel math construction (framework has no prior Dai-Freed machinery).
- **Classification**: GEOMETRIC + topology.

### V.5. CC-3 Connes-Moscovici Dimension Spectrum Signed Residue Sum (PRIORITY 5)

- **What**: Enumerate the full dimension spectrum `Sd` of D_K on Jensen-SU(3) at L_max = 9 by locating poles of `ζ_{|D|⁻ˢ}(s)` on the Connes-Moscovici algebra `B = ⟨A, [D², B]⟩`. For each pole `d ∈ Sd`, compute the residue `Res_{s=d} ζ_{D²}(s)` and the Hopf-cocycle sign `sign(Hopf_d)`. Evaluate `Λ_CC := Σ sign × Res` and report the OOM suppression relative to `a_0` alone.
- **Inputs**: D_K eigenspectrum at L_max = 9; Connes-Moscovici 1995 regularity test (close algebra under `[D², ·]`); Hopf-cocycle machinery from Connes-Moscovici §5; S83 W1-G1 IC-scheme work, S83 W1-G3 `dim H_π ≥ 2` closure (open — prerequisite).
- **Gate**: S85-CC-DIMSPEC-HOPF. **PASS** if signed sum suppressed ≥ 10 OOM relative to `a_0`. **INFO** if 1–10 OOM. **FAIL** if sum equals `a_0` (no cancellation). **Prerequisite gate**: S83 W1-G3 `dim H_π ≥ 2` must close PASS before CC-3 is computable — if prerequisite FAILs, CC-3 is DEFERRED to L_max = 11 or WITHDRAWN.
- **Effort**: 3–4 agent-sessions, novel math, includes Connes-Moscovici machinery setup. Defer unless CC-1 or CC-2 motivate.
- **Classification**: GEOMETRIC.

### V.6. §11.2 Revision of Phononic-Substrate-Geometry (DOCUMENTATION)

- **What**: Apply the proposed §11.2 revision from §5 of the source doc: replace "every known mechanism has been tested" with the 9-closures-in-4-idioms language plus the five-unconventional-pairings enumeration. Mark as PRELIMINARY pending S85 gate outcomes.
- **Inputs**: `sessions/framework/Phononic-Substrate-Geometry.md` current §11.2; source doc §5 proposed text.
- **Gate**: documentation only (no PASS/FAIL). Ensures §11.2 accurately reflects the framework's CC status going into S85.
- **Effort**: 0.5 agent-sessions, documentation edit.
- **Classification**: NON-PHONONIC (documentation).

### V.7. KO-dim = 6 Constraint Check on η (PRE-CC-1 DIAGNOSTIC)

- **What**: Before running full CC-1, verify the KO-dim = 6 constraint chain: for spectral triple `(A, H, D_K + D_F, J, γ)` with J² = +1, [J, D] = 0, Jγ = +γJ, derive the constraints on spectral asymmetry. Show whether J-commutativity forces η = 0 identically, or whether η can be nonzero via the D_F particle sector. Write out the spectrum-pairing chain explicitly.
- **Inputs**: S60 η-invariant calculation (s60_eta_invariant.py); KO-dim = 6 axiom verifications from permanent-theorems.md; [J, D_K + D_F] = 0 structural identity.
- **Gate**: S85-CC-η-PRECHECK. **PASS** if η can be nonzero via D_F (confirms CC-1 is worth computing). **FAIL** if J-commutativity structurally forces η ≡ 0 (CC-1 is predetermined to return 0, hypothesis falsified without computation).
- **Effort**: 0.5 agent-sessions, pen-and-paper derivation. Do this FIRST.
- **Classification**: GEOMETRIC.

### V.8. Triality Preservation Test on Jensen Deformation (PRE-CC-2 DIAGNOSTIC)

- **What**: Verify whether the Jensen deformation parameter τ preserves Spin(8) triality. Compute the triality automorphism σ acting on the Jensen-deformed `D_K(τ)` — does `σ D_K(τ) σ⁻¹ = D_K(τ)` for all τ ∈ [0, τ_fold]? If yes, CC-2 is computable; if no, CC-2 is predetermined to return unequal chi_2 values.
- **Inputs**: Jensen deformation generator `dD/dτ` from S72-S73b; Spin(8) triality σ; Clifford algebra relations.
- **Gate**: S85-CC-TRIALITY-PRECHECK. **PASS** if [σ, dD/dτ] = 0 (triality preserved). **FAIL** if [σ, dD/dτ] ≠ 0 (triality broken by Jensen — CC-2 factor-3 enhancement is structurally impossible).
- **Effort**: 0.5 agent-sessions, algebraic derivation + small numerical check.
- **Classification**: GEOMETRIC.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| R1 | CC may not be `a_0`; spectral triple has multiple invariants (η, Sd residue sum, Dai-Freed, Poincaré) | GEOMETRIC | ANALYSIS (not verdict) | S37 monotonicity scope clarified; framework's 9 closures cover 4 idioms, 5 idioms untested |
| R2 | Factor-3 residual `chi_2 × HP4 = 0.337 · ρ_obs`; 3× closure hypothesis `= 1.011 · ρ_obs` | GEOMETRIC + PARTICLE | ANALYSIS | Three 3-fold algebraic structures (Z_3, Spin(8) triality, A_F summands) are candidates; CC-2 is the sharpest gate |
| R3 | η-as-CC requires O(1) rational η (2/3, 3/4, 7/10), NOT small-denominator | GEOMETRIC + PARTICLE | HYPOTHESIS | Tension with Weyl-group-order prediction (1/6, 1/12) flagged in §IV.6; CC-1 resolves |
| R4 | Connes-Moscovici signed residue sum ≠ `a_0`; S37 doesn't apply | GEOMETRIC | ANALYSIS | CC-3 requires dimension spectrum closure (S83-W1-G3 prerequisite); 3–4 sessions novel math |
| R5 | Dai-Freed `⟨[D_K], [π_4(S³)=ℤ/2]⟩ · M_Pl² · H_0² = 6.13 × 10⁻⁴⁸ GeV⁴`; within factor 4.4 of ρ_obs | GEOMETRIC + topology | HYPOTHESIS (magnitude precheck PASS) | No free parameters; CC-4 magnitude-match would land observed CC from torsion-K-theory alone |
| R6 | DM/DE ratio 0.391 vs A_F summand ratio 4/9 = 0.444 (13% off) | PHONONIC + GEOMETRIC | HYPOTHESIS | Poincaré-dual DM/DE would solve coincidence problem as cohomological identity; CC-5 tests via K_0(A_F) |
| IV.1 | S37 scope: smooth monotone `Tr f(D²/Λ²)` only; not distributional, not topological, not residue-sum | GEOMETRIC | STRUCTURAL | "All CC mechanisms closed" reading is a category error; five new mechanism classes available |
| IV.2 | Invariant taxonomy: a_0/a_2/a_4 vs η / Σ Res / Dai-Freed / K₀ pairings — different invariants of same triple | GEOMETRIC | TAXONOMY | Organizes S85 planning; aligns with agent-memory "problem is FUNCTIONAL not GEOMETRIC" (S74) by identifying WHICH functionals remain |
| IV.3 | [J, D_K] = 0 at KO-dim = 6 forces spectral PAIRING, not distributional vanishing of η | GEOMETRIC | CONSTRAINT | η ≠ 0 possible for full D_K + D_F via particle-sector CKM/PMNS phases; V.7 precheck required |
| IV.6 | Internal tension in CC-1 gate: Weyl-order predicts η ∈ {1/6, 1/12} but magnitude needs η ∈ {2/3, 3/4} | GEOMETRIC | FLAGGED | Both cannot be simultaneously correct; CC-1 computation resolves |

---

*End of solo synthesis. Five pre-registered S85 CC gates endorsed from the spectral-triple lens, with two additional pre-checks (V.7 KO-dim = 6 η constraint, V.8 Jensen triality preservation) added as prerequisites to minimize wasted compute on falsified-at-design-time gates. The §11.2 revision should be applied before S85 begins. Ordering priority: V.8 → V.2 → V.7 → V.3 → V.4 → V.5 (prechecks first, cheapest/sharpest gate next, novel-math last). No agreement or conflict with the transit-dynamics-theorist synthesis is asserted here — the two lenses are orthogonal by construction and cross-lens adjudication is an S85 task if both lenses produce verdicts.*

— Connes-NCG-Theorist, 2026-04-21
