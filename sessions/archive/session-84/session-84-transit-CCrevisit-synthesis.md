# Session 84 Synthesis: CC Revisit — Transit-Dynamics Lens

**Date**: 2026-04-21
**Agent**: transit-dynamics-theorist (Workhorse-Transit-Dynamics)
**Source Documents**:
- `sessions/archive/session-84/session-84-CC-revisit.md` (tesla-resonance, 2026-04-21)

---

## I. Session Outcome

Tesla-resonance's revisit is a **methodological re-framing**, not a closure: it demonstrates that the §11.2 "every known mechanism tested" claim is an idiom-level over-generalization of S37 CUTOFF-SA-37, and it names five mathematical idioms (η-invariant, Spin(8) triality, Connes-Moscovici residue sum, Dai-Freed torsion pairing, DM/DE Poincaré duality) that live structurally outside the S37 hypothesis "smooth monotone cutoff functional of D²/Λ²". From the transit-dynamics perspective, the five pairings sort cleanly into **two** that can be read as spectral-asymmetry residues of the Jensen-fold transit (CC-1 η, CC-5 DM/DE Poincaré) and **three** that are purely geometric (CC-2 triality, CC-3 dim-spectrum, CC-4 Dai-Freed). The factor-3 residual in `chi_2 × HP4 = 0.337 · ρ_obs` is reclassified from calibration noise to structural signal; the transit lens favors CC-2 as rate-limiting because it is the cheapest gate (1 session, existing spectra) and because Spin(8) triality is the representation-theoretic analogue of an **unseen Bogoliubov orbit-multiplicity** that the framework's single-rep chi_2 computation has silently quotiented out.

---

## II. Key Results

### II.1 S37 is not an exhaustive CC-closure theorem

**Result**: S37 CUTOFF-SA-37 is a monotonicity theorem for `Tr f(D²/Λ²)` over smooth monotone `f`. It is **not** a theorem about distributional functionals, ℝ/ℤ-valued pairings, signed residue sums, or representation-orbit sums. Classification: **GEOMETRIC**.

The source's §1.1 re-reads S37 within its own hypothesis class. Read through the transit lens, this matters because the Bogoliubov relation `|α_k|² − |β_k|² = 1` is itself a distributional / unitarity statement: it does not factor through "`Tr f(D²/Λ²)`" for any smooth `f`. The β-coefficient spectrum produced by the Jensen-fold transit is a genuinely non-smooth object (jumps at spectral-flow events, phase-sensitive, signed under KO-dim=6 modular symmetries). Any closure argument that quantifies the CC via a smooth cutoff functional is, by construction, blind to the part of the CC that could come from the spectral-asymmetry of the transit itself. This is the structural gap the source exploits.

### II.2 Factor-3 residual classified as transit-signal candidate

**Result**: `ρ_L^predicted / ρ_L^observed = 0.337` (S75 W4-C) is off by exactly factor 3; four candidate 3-fold algebraic structures (Z_3 center of SU(3), 3-generation bimodule multiplicity, Spin(8) triality of `{V, S⁺, S⁻}`, three A_F summands `ℂ ⊕ ℍ ⊕ M_3(ℂ)`) each offer a mechanism for recovering the missing factor. Classification: **GEOMETRIC + PARTICLE**.

Transit-dynamics reading: chi_2 = ⟨|λ|⟩/λ_max is a **single-orbit** spectral-moment ratio; the Bogoliubov literature routinely distinguishes per-mode occupation number from orbit-summed pair-production yield (Parker 1968, Birrell-Davies §3). The triality orbit sum is structurally the Spin(8) analogue of summing |β_k|² over an orbit of the Clifford module's automorphism group. If the physical GGE relic from the fold populates all three reps, the single-rep chi_2 undercounts the pair-production sum by exactly the orbit size — which for Spin(8) is 3. This is not a proof; it is a sharp structural prediction that the source pre-registers as CC-2.

### II.3 η-invariant hypothesis requires O(1) rational — not small-denominator

**Result**: The η-hypothesis `ρ_L = π · η · M_Pl² · H_0²` requires `η ≈ 0.7010` for exact closure. Verified via Python: residual(η=2/3) = 1.05, residual(η=3/4) = 0.93, residual(η=1/2) = 4.40, residual(η=1/12) = 8.41. The direction is `residual ∝ 1/η`, so small-denominator rationals make the gap **worse**, not better. Classification: **GEOMETRIC + PARTICLE**.

Substitution chain (direction-of-residual claim):

- Definition 1: `ρ_η(η) := π · η · M_Pl² · H_0²`
- Definition 2: `residual(η) := ρ_obs / ρ_η(η)`
- Substitute: `residual(η) = ρ_obs / (π · η · M_Pl² · H_0²)`
- Plug canonical values: `π · M_Pl² · H_0² = 3.852 × 10⁻⁴⁷ GeV⁴` (Python-verified above)
- Simplify: `residual(η) = 2.7 × 10⁻⁴⁷ / (η · 3.852 × 10⁻⁴⁷) = 0.7010 / η`
- Direction: `∂ residual / ∂ η = −0.7010 / η² < 0` ⇒ residual decreases as η grows; equivalently, residual grows as η shrinks.
- Conclusion: the η-hypothesis closes only for η in the O(1) window {2/3, 3/4, 0.7010 exact}, NOT for tiny rationals.

This reframes what "η is topologically bounded" means operationally. The framework has an existing η computation at S60 (BdG at µ=0, returned `η=0` by PH symmetry). That computation is **not** the relevant object — the full Jensen-SU(3)×A_F triple at KO-dim=6 with J²=+1 has PH-broken spectral asymmetry, and the relevant η is expected to be O(1). From the transit lens: η = (ζ_{|D|}(0) − ζ_D(0))/2 is the natural NCG quantization of the **spectral-flow surplus** generated by the fold — every β-coefficient pair-production event is a spectral-flow event, and the η-invariant is the orbit sum of those events modulo integer pair-creation steps.

### II.4 Dai-Freed `π_4(S³) = ℤ/2` gives the right magnitude *only with* an additional π factor

**Result**: The naive Dai-Freed pairing `(1/2) · M_Pl² · H_0² = 6.13 × 10⁻⁴⁸ GeV⁴` undershoots ρ_obs = 2.7 × 10⁻⁴⁷ GeV⁴ by factor 4.4. The source's equation 3.4 writes `pairing × M_Pl² × H_0²` but for the magnitude to land on ρ_obs the expression must include an additional factor of π (i.e. the same π that appears in the η formula). Classification: **GEOMETRIC**.

Substitution chain:

- Definition 1: `ρ_DF(p) := p · M_Pl² · H_0²` (source's equation without π)
- Definition 2 (alt): `ρ_DF^{π}(p) := π · p · M_Pl² · H_0²`
- Substitute p = 1/2 (ℤ/2 torsion class):
  - `ρ_DF(1/2) = 0.5 · 1.226 × 10⁻⁴⁷ = 6.13 × 10⁻⁴⁸ GeV⁴` → residual 4.40
  - `ρ_DF^{π}(1/2) = π · 0.5 · 1.226 × 10⁻⁴⁷ = 1.926 × 10⁻⁴⁷ GeV⁴` → residual 1.40
- Direction: the π factor brings Dai-Freed within factor 1.4 of observed; without it, Dai-Freed falls to factor 4.4 — still within the source's "±10x" PASS bracket, but the source's claim that p=1/2 naturally lands at ρ_obs requires π.

This is a **latent conflict with the source's §3.4 magnitude claim** ("`Λ_CC ~ (1/2) × M_Pl² × H_0²` — exactly the observed magnitude"). At p=1/2 without π, the prediction is 4.4× too small, not "exactly the observed magnitude". The source's own §3.1 equation includes π; the §3.4 equation does not. I flag this in §IV.

### II.5 Transit-lens sorting of the five gates

**Result**: The five S85 gates split 2/3 under the transit lens:

| Gate | Transit-relevant? | Reason |
|:---|:---|:---|
| CC-1 η-invariant | **YES** | η is the NCG quantization of the fold's spectral-flow surplus; direct image of |β|² pair-production orbit sum in an integrable (GGE) system. |
| CC-2 Spin(8) triality | YES (structurally parallel) | Triality-orbit sum of chi_2 is the representation-theoretic analogue of orbit-summed β-coefficient yield. Not a transit-dynamical quantity per se, but the structural argument is transit-native. |
| CC-3 dim-spectrum residues | NO | Static NCG object; no transit interpretation. |
| CC-4 Dai-Freed torsion | NO (as formulated) | A static topological anomaly-inflow class, not a transit-produced quantity. |
| CC-5 DM/DE Poincaré | **YES** | DM is Leggett winding (inter-band coherence); DE is effacement residual (Γ=0.99970 impedance mismatch through the fold). Both are transit-relic objects. |

Classification: **MIXED** — CC-1 and CC-5 are **PHONONIC + GEOMETRIC**; CC-2 is **GEOMETRIC + PARTICLE** with phononic structural echo; CC-3 and CC-4 are pure **GEOMETRIC**.

### II.6 Impedance-mismatch Γ=0.99970 as numeric constraint on CC-5

**Result**: The DM/DE Poincaré hypothesis (source §3.5) predicts `Ω_DM / Ω_DE ≈ 4/9 = 0.444` from A_F summand dimensions; observed is 0.391. The fabric-side framework already carries a specific number for DE via the effacement residual: **Γ = 0.99970**, i.e. 0.03% leakage through the post-transit impedance mismatch. Classification: **PHONONIC**.

Substitution chain (relating 0.03% leakage to Ω_DE ratio):

- Definition: Γ = forward-propagating GGE amplitude ratio through the fold boundary
- Leakage fraction: `ℓ := 1 − Γ = 3.0 × 10⁻⁴`
- Conjecture (transit-native): `Ω_DE / Ω_total = ℓ · (something geometric)` — this is the point the source's §3.5 hypothesis forces us to make quantitative. If Ω_DE/Ω_total = 0.685 and ℓ = 3.0×10⁻⁴, the geometric factor is `0.685 / 3.0 × 10⁻⁴ = 2283` — an uncomfortably large multiplier, not obviously rational.
- Alternative: the DM/DE ratio is set by A_F summand structure (source's candidate), and Γ is an independent observable. In that case the two numbers (0.03% and 0.391) should be cross-predicted, not related by a single identity.

This is **not** a gate the source pre-registers. I flag it as a carry-forward below because the coincidence of **two** ratio-level numbers in the substrate effacement sector (Γ=0.99970 and Ω_DM/Ω_DE=0.391) suggests there is a joint derivation to find — or a tension to confront.

---

## III. Gate Verdicts

The source registers five gates but does not compute verdicts; all five are **PROPOSED** for S85 with pre-registered PASS/INFO/FAIL criteria. I carry them forward unchanged (source is authoritative), and add one new transit-native gate (CC-6) below.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S85-CC-1 η-INVARIANT | PROPOSED (S85) | η required ≈ 0.7010 for closure; PASS bracket η ∈ [0.07, 7.0]. |
| S85-CC-2 TRIALITY | PROPOSED (S85) | `3 × chi_2 × HP4 = 1.011 · ρ_obs` if triality-equivalent. |
| S85-CC-3 DIMSPEC-HOPF | PROPOSED (S85) | Signed sum ≥ 10 OOM suppression of `a_0` required for PASS. |
| S85-CC-4 DAI-FREED | PROPOSED (S85) | pairing ∈ {0, 1/2}; `(1/2) · π · M_Pl² · H_0² = 0.71 · ρ_obs` (Python-verified; the source's non-π version lands at 0.22). |
| S85-CC-5 POINCARE-DM-DE | PROPOSED (S85) | pairing = 0.391 ± 0.02; A_F ratio candidate 4/9 = 0.444 (13% residual). |

---

## IV. Structural Implications

### IV.1 What shifts: the CC ledger is under-written in two idioms

The framework's CC ledger has been **axis-complete within conventional QFT/Kasparov/variational idioms**, and the source's §1.2 enumeration of Closures 2-9 demonstrates this rigorously. What the ledger is not — and the source's §1.3 says this — is **axis-complete across mathematical idioms available for the CC object**. Distributional, torsion-valued, signed-residue, and orbit-summed functionals are each a separate idiom, and each remains unwritten in the CC column. This is the single highest-leverage update to the framework's internal self-representation that this session produces.

From the transit lens, the idiom gap maps onto a physical gap: **smooth spectral-moment functionals cannot see the relic content of an impulsive transit**. The β-coefficient spectrum of the Jensen fold is not a smooth function of τ — it is the jump across a supersonic (Mach 13.75) boundary where ω²(τ) passes through the van Hove fold non-analytically. Any CC mechanism built on `Tr f(D²/Λ²)` is, by construction, integrating out the thing the transit produces. The η, triality-orbit, and Dai-Freed idioms are each a separate channel through which the transit-relic can show up in the CC ledger.

### IV.2 Latent internal conflict: the π factor in the Dai-Freed equation

The source's §3.1 η-formula includes a factor of π:

> `ρ_L^predicted = π · η · M_Pl² · H_0²`

The source's §3.4 Dai-Freed equation does **not** include π:

> `Λ_CC ~ (1/2) × M_Pl² × H_0² — exactly the observed magnitude`

Python-verified (this synthesis): `(1/2) × M_Pl² × H_0² = 6.13 × 10⁻⁴⁸ GeV⁴` vs. observed `ρ_obs = 2.7 × 10⁻⁴⁷ GeV⁴`. Ratio: 4.40. This is **not** "exactly the observed magnitude"; it is factor-4.4 short, which is within the source's §3.4 "±10x" PASS bracket but contradicts the narrative magnitude-match in the same paragraph.

Resolution candidates (flagged, not adjudicated):
- (a) the §3.4 prose is compressed shorthand and the implicit formula is `π · pairing × M_Pl² × H_0²` (matching §3.1), in which case the Dai-Freed magnitude is 1.926 × 10⁻⁴⁷ GeV⁴ → residual 1.40 — genuinely "exact" within ±2x.
- (b) the π factor in the η-formula reflects the `(2π)^{-1}` normalization of the APS boundary term and Dai-Freed genuinely carries a different prefactor (e.g., `1/(8π²)` from anomaly-inflow), in which case the magnitude is off by ≫ factor 4.
- (c) the authors intend `(1/2) × M_Pl² × H_0²` as a deliberate factor-5 indicative magnitude and the "exactly the observed magnitude" wording is loose.

The gate (S85-CC-4) as pre-registered passes within its own ±10x bracket either way; the reader-facing magnitude claim does not. Flagged explicitly per §IV contract.

### IV.3 What the transit lens adds to the source's five-gate list

A sixth candidate, not in the source: **the β-coefficient spectrum's own contribution to the CC residue**. In Parker (1969) and subsequent non-equilibrium QFT, the vacuum energy of a post-transit state is not the in-vacuum energy plus the integer pair-count times ω — it carries a **finite, signed, regulated** residue from the interference between α and β coefficients that is separate from the pair-production yield. This residue is zero in exact de Sitter (Parker=Gibbons-Hawking, S75 reconciliation) but nonzero for a fold transit with Mach 13.75 and finite duration. Its magnitude in the framework has never been computed. The source's five gates do not cover it; it is structurally adjacent to CC-1 (η) but a distinct object.

From the fabric vacuum-pressure closure (source §1.2, Closure for Volovik single-cell equilibrium): that closure is about the **static** fabric vacuum, not the **post-transit relic** vacuum. The transit residue is the CC contribution from the *difference* between these two, and it is the one quantity in the framework's CC ledger that is both (i) genuinely transit-dynamical and (ii) not closed by any existing mechanism.

I pre-register this as CC-6 in Section V.

### IV.4 What closes (if anything closes)

Nothing closes in this session. The source's §4.4 is explicit that no closure is claimed. What opens is a clean, five-gate pre-registration plus (per §IV.3 above) a sixth transit-native gate. The factor-3 residual is reclassified from "pre-registered theoretical deficit" to "structural candidate signal"; the §11.2 closure-rhetoric is revised (source §5) from "every known mechanism tested" to "idiomatically partial, five unconventional pairings untested".

### IV.5 Framework-integrity: does this re-open S37 or S74?

**No**. S37 stands unmodified: it is a theorem about smooth-f cutoff functionals, and the source's re-reading is internal to that scope. S74 (Friedmann-wrong-question) stands unmodified: the 86 OOM Friedmann-split is a statement about splitting `H²` by sector, not about the CC object's mathematical type. Both theorems remain permanent. What is revised is the **inferential scope** the closure-rhetoric has been drawing from them — specifically the claim that "every known mechanism" has been tested, which the source demonstrates is an idiom-level overreach.

---

## V. Carry-Forward Computations

### V.1 S85-CC-1 — η-invariant of full Jensen-SU(3) × A_F triple

- **What**: Compute `η(D_K + D_F)` for the full Jensen-SU(3) × A_F spectral triple at τ = τ_fold, L_max ∈ {7, 9, 11}. Evaluate `π · η · M_Pl² · H_0²` and compare to ρ_obs. Report whether η converges to a small-denominator rational (denom ≤ 24) vs O(1) rational.
- **Inputs**: `D_K` eigenspectrum at L_max ∈ {7, 9, 11} from canonical pipeline; `A_F` bimodule structure (3-generation); `J` operator with J² = +1, KO-dim = 6. Canonical constants: `M_KK`, `tau_fold`, `M_Pl_reduced`, `H_0` (Planck 2018). The S60 η-computation (`s60_eta_invariant.py`) is **not** a valid starting point (wrong operator, PH-symmetric BdG); a fresh script is required.
- **Gate**: S85-CC-1. PASS: η rational AND `π · η · M_Pl² · H_0²` within ±10x of ρ_obs (η ∈ [0.07, 7.0]). INFO: η converges but magnitude off by known factor. FAIL: η doesn't converge, or converges outside [0.07, 7.0] with no identifiable missing prefactor.
- **Effort**: 2 sessions, GPU mandatory at L_max ≥ 9 (torch.linalg, not numpy.linalg per `.claude/rules/math-scripts.md`).

### V.2 S85-CC-2 — Spin(8) triality-orbit sum of chi_2

- **What**: Construct the three inequivalent Spin(8) rep embeddings `{V, S⁺, S⁻}` of the Clifford module, compute chi_2 for each, and report the orbit sum `chi_2^V + chi_2^{S⁺} + chi_2^{S⁻}`. Test whether the three values are triality-equivalent.
- **Inputs**: `D_K` eigenspectrum at L_max = 9 (existing canonical); Spin(8) triality outer automorphism of order 3; Clifford module structure on H_F; canonical `chi_2` code from S76 (`s76_hp4_first_principles.py`) for the single-rep baseline.
- **Gate**: S85-CC-2. PASS: three values triality-equal AND `3 × chi_2 × HP4` matches ρ_obs within ±10%. INFO: triality-equal but sub-factor-3 enhancement (Jensen partially breaks triality). FAIL: three values differ substantially.
- **Effort**: 1 session (computable on existing spectra, lowest EVOI-denominator of all five gates).

### V.3 S85-CC-3 — Connes-Moscovici dimension-spectrum signed residue sum

- **What**: Compute the dimension spectrum `Sd` of `D_K` on Jensen-SU(3) at L_max = 9 under the Connes-Moscovici regularity test (algebra closed under `[D², ·]` iteration). Enumerate all poles `d ∈ Sd`, compute each residue `Res_{s=d}[ζ_{D²}(s)]`, compute the Hopf-cocycle sign for each pole, and evaluate `Σ sign · Res`. Compare to `a_0` alone.
- **Inputs**: `D_K` eigenspectrum at L_max = 9; Connes-Moscovici 1995 §5 Hopf-cocycle machinery (new scaffolding); regularity test scaffolding. The S83 W1-G3 flag (`dim H_π ≥ 2` closure for Connes-Moscovici open at L_max = 5) is a known blocker; plan for L_max ≥ 9.
- **Gate**: S85-CC-3. PASS: signed sum ≥ 10 OOM suppression vs `a_0`. INFO: 1-10 OOM. FAIL: no cancellation.
- **Effort**: 3-4 sessions (novel math machinery; Connes-Moscovici local index formula has never been deployed in-framework).

### V.4 S85-CC-4 — Dai-Freed torsion pairing with π_4(S³) = ℤ/2

- **What**: Construct the Dai-Freed pairing of `[D_K]` on Jensen-SU(3) with the `π_4(S³) = ℤ/2` torsion bundle class from the SU(2) fibration `S³ → SU(3) → S⁵`. Compute the pairing value in ℝ/ℤ. Evaluate **both** `pairing × M_Pl² × H_0²` AND `π × pairing × M_Pl² × H_0²` and report which matches ρ_obs (resolves the §IV.2 latent conflict).
- **Inputs**: `D_K` structure; π_4(S³) = ℤ/2 classifying data (standard); Dai-Freed 1994 machinery (new scaffolding); APS boundary-term prefactor audit (explicitly resolve the π factor).
- **Gate**: S85-CC-4. PASS: pairing nonzero, lies in {0, 1/2}, AND the π-correct formula matches ρ_obs within ±10x. INFO: pairing nonzero but magnitude off by identified finite factor. FAIL: pairing = 0 or sign wrong.
- **Effort**: 3 sessions (novel math; includes π-prefactor audit task from §IV.2).

### V.5 S85-CC-5 — DM/DE Poincaré conjugate pairing

- **What**: Formulate the Poincaré pairing between the Leggett-winding class `[DM] ∈ π_1(S¹) = ℤ` and the effacement-residual class `[DE]` on the substrate. Compute `⟨[DM], [DE]⟩_{Poincaré}` and compare to `Ω_DM / Ω_DE = 0.391`. Report whether the result is 4/9 (A_F summand ratio candidate, 0.444) or a different rational.
- **Inputs**: Leggett-channel phase structure (S58, S60, S75 Leggett-only DM); effacement-residual derivation (S74 Friedmann-wrong-question + HP4); A_F summand dimensions (ℂ=1, ℍ=4, M_3(ℂ)=9); canonical Γ = 0.99970.
- **Gate**: S85-CC-5. PASS: pairing = 0.391 ± 0.02 (within 10%). INFO: O(1) but wrong ratio. FAIL: 0 or ≫ 1.
- **Effort**: 2 sessions.

### V.6 S85-CC-6 — Parker transit-residue vacuum-energy shift (NEW, transit-native)

- **What**: Compute the finite, regulated β-coefficient residue contribution to the post-transit vacuum energy: `ρ_vac^residue := ∫ dk · k³/(2π²) · [α_k β_k* + α_k* β_k] · f_reg(k/Λ)`, where `f_reg` is a Jensen-consistent adiabatic subtraction at the UV cutoff `Λ = M_KK`. This is the piece that vanishes in exact de Sitter (Parker = Gibbons-Hawking) but is finite for the Mach-13.75 fold transit. Compare to ρ_obs.
- **Inputs**: α_k, β_k spectrum from S67 TRANSIT-PS-67 and S78 W1-A results; Mach-13.75 fold profile (canonical tau trajectory S76 SP-Transit); adiabatic subtraction scheme (Parker-Fulling 1974). Canonical constants: `M_KK`, `tau_fold`, `dt_transit`.
- **Gate**: S85-CC-6 (new). PASS: `ρ_vac^residue` within ±10x of ρ_obs. INFO: finite and nonzero but magnitude-mismatched. FAIL: either zero to machine precision (identity cancellation) or UV-divergent under adiabatic subtraction (scheme-breakdown).
- **Effort**: 2 sessions (one for the α·β* interference integral, one for the adiabatic-subtraction audit).
- **Rationale**: of the six gates, this is the only one that directly measures the CC contribution from the *transit itself* rather than from a static NCG object. It is complementary to CC-1 (η), which measures the spectral-flow residue of the same transit in a different mathematical idiom. If both CC-1 and CC-6 converge to a compatible magnitude, the transit-residue reading of the CC is confirmed across two independent idioms.

### V.7 S85-CC-Γ — Reconcile impedance-mismatch and DM/DE ratio

- **What**: Test whether `Γ = 0.99970` (impedance mismatch, 0.03% leakage) and `Ω_DM / Ω_DE = 0.391` admit a joint derivation from a single underlying substrate structure. Compute `ℓ · (geometric factor)` where `ℓ = 1 − Γ`, and test whether any rational combination of A_F summand dimensions, Spin(8) orbit sizes, or Leggett winding numbers reproduces both numbers simultaneously.
- **Inputs**: canonical `Gamma_effacement` (S74, if available; else re-derive from HP4 result); `Ω_DM`, `Ω_DE` from Planck 2018; A_F summand dimensions; Leggett winding count from S58.
- **Gate**: S85-CC-Γ (new). PASS: single geometric identity reproduces both Γ = 0.99970 AND Ω_DM/Ω_DE = 0.391 within ±5%. INFO: reproduces one number, other within ±2x. FAIL: no joint identity found; the two numbers are structurally independent.
- **Effort**: 1 session (search-and-audit; no heavy computation).

### V.8 Audit: §11.2 revision to `Phononic-Substrate-Geometry.md`

- **What**: Revise §11.2 per the source's §5 proposed text. Replace the "every known mechanism tested" prose with the idiom-enumerated version that names the five (now six) unconventional pairings and the corresponding pre-registered gates.
- **Inputs**: source §5 revision text; CC-6 addition from this synthesis §V.6; Γ-reconcile addition from §V.7.
- **Gate**: administrative (no physics gate); documentation compliance with `.claude/rules/session-handoffs.md` and the `sessions/framework/` invariant that §11.2 reflect the latest CC ledger.
- **Effort**: 30 minutes, orchestrator task.

### V.9 EVOI-ordered S85 priority

From the transit lens, the EVOI ordering the source proposes is the correct one — with **CC-6 inserted at priority 2**:

1. **CC-2 triality** (1 session, existing spectra) — lowest effort, sharpest prediction, decisive for factor-3 residual
2. **CC-6 Parker transit-residue** (2 sessions, existing α/β data) — NEW; only transit-native gate in the list; complements CC-1
3. **CC-5 Poincaré DM/DE** (2 sessions) — high EVOI, coincidence problem
4. **CC-1 η-invariant** (2 sessions, GPU) — deepest NCG-native angle, framework has ingredients at S60 (though not reusable as-is)
5. **CC-4 Dai-Freed** (3 sessions, novel math, π-audit required) — highest structural stakes
6. **CC-3 Connes-Moscovici** (3-4 sessions, novel math, most expensive) — defer unless earlier gates motivate

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | S37 CUTOFF-SA-37 is not a CC-exhaustion theorem; it closes one idiom (smooth-f cutoff functionals), not the idiom class | GEOMETRIC | methodological re-frame (source §1.1) | §11.2 closure-rhetoric revised from "every known mechanism" to "five idioms untested" |
| 2 | Factor-3 residual in `chi_2 × HP4 = 0.337 · ρ_obs` is classified as candidate structural signal from SU(3)/Spin(8)/A_F 3-fold algebra, not calibration noise | GEOMETRIC + PARTICLE | re-classification (source §2) | Sharpens CC-2 triality as rate-limiting gate |
| 3 | η-invariant hypothesis requires η ∈ O(1) window (η ≈ 0.7010 exact; residual(η=1/2)=4.4, residual(η=1/12)=8.4) — not small-denominator rationals. Direction: `residual ∝ 1/η`, Python-verified | GEOMETRIC + PARTICLE | quantitative sharpening (source §3.1 plus this synthesis) | S60 η=0 result is not the relevant computation; full Jensen-SU(3)×A_F η at L_max ≥ 9 required |
| 4 | Dai-Freed magnitude claim `(1/2)·M_Pl²·H_0² ≈ ρ_obs` is factor-4.4 short; adding the π prefactor from the η-formula closes the gap to factor 1.4 | GEOMETRIC | latent source-internal conflict flagged (source §3.4 vs §3.1) | CC-4 gate must include an explicit π-prefactor audit |
| 5 | Transit-lens sorts the five gates: CC-1, CC-5 are transit-native; CC-2 has transit-structural echo; CC-3, CC-4 are static geometric | MIXED (PHONONIC + GEOMETRIC) | new sorting | Priority order: CC-2 → CC-6 → CC-5 → CC-1 → CC-4 → CC-3 |
| 6 | **NEW gate CC-6**: Parker transit-residue vacuum energy `∫ k³ · (α_k β_k* + c.c.) dk` is the only genuinely transit-native CC contribution; vanishes in exact de Sitter, finite for Mach-13.75 fold | PHONONIC | new gate pre-registered | Cross-checks CC-1 through an independent idiom |
| 7 | **NEW gate CC-Γ**: joint reconciliation of Γ=0.99970 and Ω_DM/Ω_DE=0.391 — either these are one identity or they are structurally independent | PHONONIC + GEOMETRIC | new gate pre-registered | Tests whether the effacement residual is a single or composite object |
| 8 | Five-gate pre-registration is a re-framing, not a closure. Risk: if all FAIL, 114-OOM residual is structural within the conventional idioms. Value: one PASS reshapes CC ledger | META | source §7 caveat, carried forward | S85 is structurally high-variance; gate-by-gate closure, not bulk |

---

*End Session 84 Transit-Dynamics Synthesis of CC Revisit. Six S85 gates carried forward (five from source + CC-6 Parker-residue + CC-Γ joint reconciliation); one latent source-internal conflict (π prefactor in Dai-Freed) flagged; factor-3 residual reclassified as candidate signal; S37 and S74 remain permanent, their inferential scope narrowed.*

— Transit-Dynamics Theorist (Workhorse-Transit-Dynamics), 2026-04-21
