# Session 99 Synthesis: The Fermion-Mass Spectrum as Dirac-Eigenvalue Data — a Cosmic-Bridge Reading

**Date**: 2026-06-03
**Agent**: mack-cosmic-bridge (Katie Mack — Cosmic Bridge)
**Source Documents**:
- `downloads/standard-model-lagrangian-explained.md` (the expanded SM Lagrangian — plain-English explanation + the project's `a₄`/spectral-action framing coda)
- `sessions/archive/session-99/session-99-fermion-mass-panel.md` (the S99 fermion-mass innovation panel: connes / baptista / transit / hawking)
- `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md` (my own constraint registry)

> **Scope note (mine to set, per my bridge role).** My remit is the particle-physics ↔ observation interface and convention fidelity. The fermion mass spectrum is not a cosmological observable in the dark-matter / dark-energy sense I usually defend, so this synthesis does two things: (1) it records, at full rigor, what the panel established about masses as substrate-IS eigenvalue data; and (2) it flags wherever a claim touches an *observed number* (PDG mass ratios, the framework's own `m_H`) and verifies the arithmetic, because that is where a substrate claim earns or loses contact with reality. I do not re-adjudicate the panel's reasoning — I check its numbers and its conventions, and I locate it against what the framework has actually proven.

---

## I. Session Outcome

The S99 fermion-mass panel was a **generative innovation exercise, not a gated computation** — it emitted **no gate verdicts and no registry entries** by design (loose-bureaucracy brief). Its one consequential structural move: it correctly re-posed the charged-fermion-hierarchy corridor that `S97-YUKAWA-FAMILY-DERIVE` left as a FAIL (`R_cross = 1.01970`, i.e. democratic `1:1:1`, against the PDG charged-lepton ratio `1 : 0.0595 : 0.000288`). That FAIL is now understood as the **PROVEN Homogeneity wall** (§VII.BL, STAGE-3-PERMANENT in `permanent-results-registry.md`): a left-invariant `D_K` on SU(3) acts as a multiplicity-scalar on every Peter–Weyl generation factor, so democratic masses are *forced by theorem*, not missed by computation. The panel converged four lenses (finite-spectral-triple / Jensen-fiber / non-equilibrium-freeze-in / KK-horizon) onto **one object** — the inter-sector mass block `[[d, w],[w*, d]]` on the multiplicity bundle — with a reality-axiom-forced division of labor. Numerically: the e-vs-heavy mass *envelope* is a clean structural win; the `1.889` generation-widening *shape* is open (with a 4.7%, zero-parameter Casimir candidate); the μ↔τ split and the mixing are structurally resolved but numerically queued.

---

## II. Key Results

### 1. S97's `1:1:1` is the Homogeneity wall — democratic masses are a theorem, with a direction

**Result**: `R_cross = 1.01970` (democratic, `n_distinct = 2`) is a PROVEN consequence of substrate homogeneity, not a computational miss. **Classification: GEOMETRIC** (a statement about the internal fabric `(A_K, H_K, D_K, J)`, not its excitations).

The substrate at every point IS the spectral triple on Jensen-deformed SU(3) with algebra `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`. Because `D_K` is **left-invariant**, by Peter–Weyl the algebra acts as `π(a) = ⊕ π_{(p,q)}(a) ⊗ 𝟙_{m(p,q)}` — a *scalar* on every multiplicity factor `ℂ^{m(p,q)}`. The Standard Model generation index lives precisely in that multiplicity factor (`t = (p−q) mod 3`, the SU(3) Z₃-triality, `proven_384`). A multiplicity-scalar operator cannot carry a generation index. Therefore the masses come out democratic *by construction*. This is the chain `D_K left-invariant → multiplicity-scalar representation → generation-blind → R_cross = 1`, verified exact at every `L_max`.

Two refinements the panel makes (both registry-backed) are load-bearing for fidelity. First, **reality is innocent**: the obstruction is the homogeneity wall (W2), NOT the reality condition `[J,D_K]=0` (W1). connes corrected the prior S97-era attribution; the registry (§VII.BL, "Reality is INNOCENT") confirms `[J,D_K]=0` is satisfied by construction for every inner fluctuation and is never sacrificed. Second, **the twisted escape is dead by Skolem–Noether**: `A_K` has three non-isomorphic simple summands, so every `σ ∈ Aut(A_K)` is block-inner ⇒ multiplicity-scalar ⇒ `Aut(A_K)` is multiplicity-blind. There is no automorphism trick that recovers the hierarchy.

The consequence — the panel's foundation — is that the hierarchy is *forced* to live in an **external, non-left-invariant deformation `ε_LX`** acting non-trivially on the multiplicity index, reality-compatible (`[J, D_K + ε_LX] = 0`) but outside every `A_K`-built module. The dead end has a normal vector: *break left-invariance on the multiplicity index*. The question is no longer "why democratic?" (answered) but "what is `ε_LX`?"

This is exactly the substrate-first inversion the framework demands, and it is the right reading of the §4 coda's claim that "Yukawa masses are entries of `D_K`'s finite part." The masses ARE eigenvalue data — but the homogeneous fiber's *own* differential calculus is blind to the generation index, so the hierarchy is a measure of how far the inter-fiber connection is deformed away from homogeneity, not an intrinsic feature the geometry supplies for free.

### 2. One inter-sector object `[[d, w],[w*, d]]` with a reality-FORCED division of labor

**Result**: the four lenses converged on a single 2×2 block on the conjugate generation doublet, `M_{(μ,τ)} = [[d, w],[w*, d]]`, eigenvalues `d ± |w|`, mixing `∝ arg(w)`. **Classification: GEOMETRIC** (the object is finite-part `D_K` data; its observable images are PARTICLE).

The decisive structural content is *connes' admissibility verdict*, which upgrades the modulus/phase split from "argued" to "axiom-forced." All three NCG axioms pass Sage-exact on the greybody/overlap-reweighted `D_F`:

- **Order-one — PASS unconditionally.** Any generation texture is order-one-admissible, because the weight is a multiplicity-index scalar and `A_K` acts as `⊗𝟙_m` there (index-disjointness: order-one lives on the color/isospin index, blind to generation).
- **KO-dim-6 — PASS.** The weight commutes with chirality `γ`, so `Jγ = −γJ` is untouched.
- **Reality `[J,D_F]=0` — PASS for the diagonal envelope ONLY.** `J` swap-conjugates the `(μ,τ) = t1↔t2` pair, so reality *forces* `d_μ = d_τ` on the diagonal. A diagonal `diag(d_e, d_h, d_h)` — distinct on the J-fixed electron (trivial rep, `C₂=0`), equal on the J-swapped heavy pair — is reality-exact and legally carries the e-vs-heavy ENVELOPE; a diagonal `d_μ ≠ d_τ` would break reality and is forbidden.

The eigenvalue arithmetic then seals the partition: `[[d,w],[w*,d]]` has eigenvalues `d ± |w|` (depend on `|w|` only) and eigenvectors depending on `arg(w)` only. So **`|w|` → μ↔τ mass split; `arg(w)` → mixing + CP** — the split-is-magnitude / mixing-is-phase division is a *consequence of the reality axiom*, not a modeling choice. This is the kind of result I trust: it is rederivable from the axiom, not asserted.

A BDI-specificity tie makes it sharper still: in the `J²=−1` (DIII) class reality would force `w` real and kill the phase. The CP phase `arg(w)` survives *precisely because the framework is BDI* (`J²=+1`, PROVEN, atlas KO-dim-6). CP-in-mixing and chirality are two consequences of one structural fact — which is genuinely elegant, and is the panel's strongest non-shared-prompt convergence.

### 3. The diagonal envelope is one exponential seen four ways

**Result**: the e-vs-heavy `~8` e-fold split is a single Casimir-graded exponential, independently identified by all four lenses. **Classification: GEOMETRIC** (spectral-action / `D_K`-spectrum content).

| Lens | The exponential | Reading |
|:-----|:----------------|:--------|
| baptista | `O_g ∝ exp(−k·C₂(p,q))` | Higgs-`\|s(h)\|²`-overlap, Jensen-weighted (equilibrium-geometric) |
| connes | `m_i ∝ exp(−d_i/ℓ)` | Connes distance between generation-states (metric) |
| hawking | `y_i ∝ Γ(ω_i)·exp(−2πω_i/κ)` | greybody transmission at the exit horizon (semiclassical filter) |
| transit | `m_gen ∝ exp(−S₀·C₂)` | Casimir-graded diabatic freeze-in amplitude (non-equilibrium) |

The identification `d_i/ℓ ↔ 2πω_i/κ ↔ S₀C₂ ↔ k·C₂` is the framework's "one operator, several faces" signature. The panel's double-counting guard is correct and worth preserving: transit's freeze-in amplitude is *also* a Casimir exponential, so `exp(−kC₂)·exp(−S₀C₂) = exp(−(k+S₀)C₂)` is still **one** exponential — transit co-sets the diagonal slope `k → k_eff`, it does not add a second lever. This matters for honest parameter-counting: a reader must not mistake four faces of one object for four independent corroborations (`epistemic-discipline.md §"What Does NOT Count as Evidence"` — shared-prompt convergence is not independent confirmation).

### 4. Three generations from a dual-`Z₃`, with a lepton-only φ-lever (the SM's hand-fit, explained)

**Result**: three generations require `Z₃ × Z₃` (triality × the `s_φ` Higgs-mode phase), not a single `Z₃`. **Classification: PARTICLE** (representation-theoretic content — quantum numbers and generation labels).

A single `Z₃` yields ≤2 rungs (which is *why* S97's naive single-`Z₃` was doomed); the product yields 3. baptista's `Z₃` #1 is triality `t=(p−q) mod 3` (collapses `t=1 ≡ t=2` under BDI reality); `Z₃` #2 is the `s_φ` phase carried by the lepton mass matrix's `c(φ) = 1/(1+8cos²φ)`, which at `{0, 2π/3, 4π/3}` takes `{1/9, 1/3, 1/3}` — a parallel 2-fold collapse on an orthogonal label. The distinct φ-factors `{1/9, 1/3}` are a **lepton-only** lever (the quark matrices `Ω^D, Ω^c` carry no φ-term), which **explains the lepton-vs-quark hierarchy-shape difference the Standard Model otherwise fits by hand**. That is a real bridge-relevant claim: a structural origin for a difference the SM Lagrangian (§2 of the source coda) simply *lists* as independent Yukawa numbers.

### 5. The `1.889` widening is open — but with a 4.7% zero-parameter Casimir candidate that discriminates

**Result**: the generation log-gap asymmetry ratio is a PDG *fact* (`1.8894`), not yet a framework *output*. The Casimir ladder gives `9/5 = 1.800` (4.7% off, zero free parameters) *if* the generations sit at the triality-distinct tower `(1,0)/(1,1)/(3,0)`. **Classification: GEOMETRIC** (Casimir quantization of the `D_K` spectrum).

I verified all three numbers against PDG 2024 masses (`m_e = 5.10999×10⁻⁴`, `m_μ = 0.10566`, `m_τ = 1.77686` GeV), and they hold to full precision:

| Quantity | Substitution chain | Value | Panel claim |
|:---------|:-------------------|:------|:------------|
| log-gap(e→μ) | `ln(m_μ) − ln(m_e)` | `5.3316` | — |
| log-gap(μ→τ) | `ln(m_τ) − ln(m_μ)` | `2.8224` | — |
| **PDG widening ratio** | `gap(e→μ)/gap(μ→τ)` | **`1.889`** | `1.8894` ✓ |
| Casimir candidate | `C₂=(4/3,3,6)` → spacings `(5/3,3)` → `3/(5/3)` | `9/5 = 1.800` | `1.800`, 4.7% off ✓ |
| generic `n²`-overlap | (alternative model) | `3.0` | `3.0`, 59% off ✓ |

Dimensional check: all entries are ratios of log-mass-differences, hence dimensionless — consistent. The discrimination is the point I want on record: the data selects the **Casimir ladder (1.80)** over a generic Gaussian-position-overlap model (`3.0`, 59% off). This is a genuine, falsifiable, parameter-free discriminator — exactly the kind of claim that distinguishes a structural prediction from a fit. The caveat is equally important and the panel states it honestly: the `9/5` result is *conditional on the generation-sector assignment* being the triality-distinct `(1,0)/(1,1)/(3,0)` tower. `1.889` is not yet derived from a linear law (a slope linear in `C₂` gives `1.333` on the fundamental `(k,0)` tower); the open question reduces to the sector assignment, with the Jensen tilt / `ω`-nonlinearity as the alternative residual-supplier.

### 6. Production has no temperature; the scale is generation-blind

**Result**: the transit is deep-sudden (`δt/T_L = 1.25×10⁻⁵`, `P_exc = 1.000`, `S_ent = 0`), so primary production is a multi-mode **squeezed vacuum**, not a Gibbs state. The overall per-sector scale `M₀` is the generation-blind KK threshold. **Classification: PHONONIC** (Bogoliubov/squeeze production is excitation physics).

Two convention points I want pinned, because they are exactly the kind of vocabulary trap `phononic-framing.md` warns against:

- **There is no `κ` in the production amplitude.** The diabatic/Casimir-graded freeze-in route carries the grading; the naive Landau–Zener `γ ≈ 10⁻³` is generation-blind (the diabatic limit gives *no* hierarchy). The graded object is the GGE squeeze depth `−ln|ψ_pair|²`, which *is* hawking's greybody exponent. This is consistent with the framework's standing position that "reheating" is GGE relic formation, not thermalization (the Ordered Veil — the relic never thermalizes).
- **The filter has a well-defined `κ`, and it is the SONIC surface** `κ_SONIC = 0.7048 M_KK = 2π·0.112` (the genuine `v = c_BLV` Mach-1 crossing) — **not** `κ_GH = 1.365` (emergent-4D, which hawking explicitly corrected), and **not** the `a₂`/`a₄` thermodynamic-gradient surfaces. Getting the right horizon surface is a fidelity issue: the wrong `κ` would mis-scale the envelope.

The KK threshold (the `m_H` machinery) sets the overall scale `M₀^{sector}` and is **NOT** the seat of the grading — hawking verified (two ways) that a bare KK-tower sum is power-law-saturating, not exponential, and multiplicity-scalar by the same Peter–Weyl argument as W2. This kills "the KK threshold *is* the hierarchy." Worth noting for the cosmic-bridge ledger: the same `m_H` threshold machinery that lands the framework's Higgs-mass prediction (the existence-proven `KK-THRESHOLD-64` route; framework `m_H ≈ 131.8` GeV vs the `134` GeV tree-level filter-independent value, against PDG `m_H_obs = 125.1` GeV) is being re-used as the mass *scale* here — so this sector inherits whatever residual sits in the `m_H` prediction, which is a 5–7% over-prediction, not a closed match.

---

## III. Gate Verdicts

**No gates were emitted in the source documents.** The S99 fermion-mass panel was an innovation exercise under a loose-bureaucracy brief and produced candidate mechanisms, not pre-registered verdicts. The verdicts it *leans on* are prior and are recorded here for traceability (NOT re-adjudicated):

| Gate / Result | Verdict | Decisive Number | Authority |
|:--------------|:--------|:----------------|:----------|
| `S97-YUKAWA-FAMILY-DERIVE` | **FAIL** (composite) | `R_cross = 1.01970`, `n_distinct = 2` | `permanent-results-registry.md` §VII.BL provenance; VALUES authoritative |
| §VII.BL Homogeneity wall (E1) | **STAGE-3-PERMANENT** (PROVEN) | multiplicity-scalar ⇒ `R_cross = 1` exact at all `L_max` | promoted 2026-06-01, `joint-theorem-promotion.md` Stage 3 |
| `S99-E1-STAGE2-VERIFY` (Stage-2 cross-axis) | **PASS** | audit `0f0c4f65…` (axis-A vdd + axis-B dirac-antimatter, both non-authors) | registry §VII.BL Status block |

---

## IV. Structural Implications

**What opened.** A corridor that read as closed (`S97 1:1:1` FAIL) is re-posed as a correctly-oriented search problem. The panel converts a dead end into a *design constraint with a normal vector*: any hierarchy-discharging mechanism must be an external non-LI fibre connection `ε_LX` that breaks the homogeneity wall (W2) while preserving the reality wall (W1), non-gauge-removable (`P_nLI = ‖ε_LX‖² > 0`). This is the constructive complement to the §4 coda's honest scoping note — the coda flagged that the chiral gauge content lives on the NCG/algebra route, not the KK-isometry route; the panel sharpens that the *generation* content lives in a deformation *outside* every NCG-algebra module. The two are consistent: `Aut(A_K)` supplies neither the chiral group beyond the NCG branching nor the generation splitting.

**What the §VII.BL theorem closes (the constraint-map update).** Three sub-channels are now PROVEN-dead for the hierarchy: (i) inner fluctuations `A = Σ aᵢ[D_K,bᵢ]`; (ii) twisted-inner modules `Ω¹_σ` for any `σ ∈ Aut(A_K)` (Skolem–Noether); (iii) opposite-action images `JAJ⁻¹` (J-protection). All three factor through the multiplicity-scalar representation. The observable `R_cross` is INVARIANT under the entire `A_K`-built deformation orbit. No `D_K` re-tuning detunes it — this is module-membership (Hochschild-cohomology), not a spectrum accident, hence Morita-invariant.

**The cross-frontier unification (the part with reach).** The same `[J,D_K]=0` wall that forces the μ↔τ split off-diagonal also zeroes *internal* CP and forces the *external* `φ₈₈` Cartan phase to `π/2` (the S99 W3 baryogenesis result). So one off-diagonal datum `w` plausibly sets **three** observables: the μ↔τ split (`|w|`), the CKM/PMNS mixing + CP (`arg w`), and the baryon asymmetry (`φ₈₈`). The registry already records this as the **Non-LI-Deformation-Necessity** named precondition at **K=2**, with two inaugural instances — #7 (this Yukawa hierarchy) and #9 (baryogenesis, `S97-BARYOGEN-EXT-SOURCE` PASS, `η_B = 1.700×10⁻¹¹ ∈ (0, 6×10⁻¹⁰)`, via a non-LI `φ_88`-Cartan `δA`). Both share the schema {W1 satisfiable} ∧ {W2 mandatory} ∧ {W3 inner-fluctuation impotent}. The K=3 promotion contract names `δ_CP` (forced real by `[J,D_K]=0`) as the natural third frontier — *but it must LAND, not be asserted*. That is the right discipline: a baryon-asymmetry connection to a fermion-mass mechanism is a strong claim, and it earns permanent status only through an independent landing, not through narrative coherence.

**Status-currency flag (NOT a conflict).** The panel doc (§3, §1) refers to "the S99 W3 gate `S99-E1-STAGE2-VERIFY`" in a present/pending framing ("whose Stage-2 cross-axis verify IS the S99 W3 gate"). The registry (higher authority on promotion status) records that this gate has already PASSed (audit `0f0c4f65…`, supersedes `13998949…`) and §VII.BL E1 is **NOW PERMANENT** as of 2026-06-01. The panel was consolidated mid-session before the promotion landed; the two are consistent in substance (the panel correctly identifies the wall as PROVEN), only the tense has drifted. I record the registry status as canonical. There was a Stage-2 audit-item-3 catch worth noting for process fidelity: the original axis-A leg used connes-ncg-theorist, who was an E1 Stage-0 co-author (a reviewer-selection violation per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`); it was caught at session-close and re-dispatched to van-den-dungen-bridge-theorist, with the compromised line retained under Option-A supersession (absolute verdict permanence). The PASS is clean; the audit trail is honest.

**Where this does NOT touch my usual domain.** This is a particle/geometric result with no direct dark-matter, dark-energy, w(z), CMB-power-spectrum, or relic-abundance consequence. It does not move `w_0_FW = −0.918`, `Ω_DM h² = 0.120`, `n_s`, `r`, or any falsifier-master-inventory row. The one indirect cosmological tendril is the shared `m_H` threshold scale (§II.6) and the shared `φ_88` baryogenesis structure (the matter–antimatter asymmetry the SM Lagrangian's CKM phase, §2 Block 13, is the only established source of) — both are flagged above, neither changes a cosmological prediction.

**Honest convergence accounting.** Four agents given the same hard-facts block converge *somewhat by construction*. The parts carrying weight because they are *not* shared-prompt artifacts: (i) three structurally-orthogonal routes to "the split is off-diagonal" (transit's Casimir degeneracy `C₂(fund)=C₂(antifund)=4/3`, connes' reality forcing `d_μ=d_τ`, baptista's J-even diagonal overlap); (ii) the BDI→CP tie (phase survives in BDI, dies in DIII), which is *derived*; (iii) the W2 Homogeneity wall, independently PROVEN. The rest is organizing structure, useful but not evidential.

---

## V. Carry-Forward Computations

> These mirror the panel's §8 ranked proposals, re-expressed as 4-field specs. They are candidate computes (loose brief), not pre-registered gate blocks; I have assigned provisional gate IDs and PASS/FAIL/INFO thresholds where the panel's structure makes them well-posed.

**V.1. [consensus lead] baptista's per-sector Higgs-overlap with the off-diagonal element**
   - **What**: compute `O_g = ∫_K Tr[ψ_g† |s(h)|² ψ_g] vol_{g_τ}` at `L_max=12`, `τ_fold = 0.190`, *plus* the inter-sector `t1↔t2` matrix element — yielding both the diagonal envelope `d` and the off-diagonal `w = |w|·e^{i·arg(w)}` in one object. This is the literal missing calc from Baptista Paper 14 §3 (Laplacian matrices written; the Dirac-mass overlap was not).
   - **Inputs**: `s84_spectrum_cache_L12_tau019.npz` (the `(p,q)` Peter–Weyl spectrum at `τ_fold`); the Jensen-SU(3) fiber `|s(h)|²` Higgs-mode overlap kernel; `canonical_constants.py`: `tau_fold`, `Vol_SU3_Haar = 1349.74`; PDG anchors `m_e = 5.10999e-4`, `m_mu = 0.1056583745`, `m_tau` (and `m_H_obs = 125.1` for the `M₀` scale tie).
   - **Gate**: new `S100-YUKAWA-OVERLAP-OFFDIAG`. PASS iff the `|s|²`-weighted diagonal reproduces the e-vs-heavy envelope sign + OOM + gap-asymmetry *direction* AND the widening ratio lands within the panel's stated band of `1.800` (the Casimir candidate) or `1.889` (PDG); INFO if the envelope direction is right but the widening shape needs the Jensen tilt; FAIL if the diagonal is generation-blind (would contradict the `ε_LX`-on-multiplicity reframe).
   - **Effort**: 2–3 agent-sessions (one for the diagonal overlap, one for the off-diagonal element, one for the widening cross-check).
   - **Cheapest sub-test first**: diagonalize `Ω^b_g` at the three `Z₃` φ-points `{0, 2π/3, 4π/3}` — closed-form 3×3, already in hand — testing whether the `s_φ`-phase is the second `Z₃` (predicted `c(φ) = {1/9, 1/3, 1/3}`). ~2 hours, 1 agent session.

**V.2. connes' Connes-distance ladder on the multiplicity bundle**
   - **What**: compute the Connes geodesic distances `d_i` between generation-states on the multiplicity bundle and test `mass = e^{−d_i/ℓ}`, including the widening signature `≈ 1.889`.
   - **Inputs**: the `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY` machinery (exists); the multiplicity-bundle metric from the reweighted `D_F`; PDG lepton masses for the calibration of `ℓ`.
   - **Gate**: new `S100-CONNES-DISTANCE-LADDER`. PASS iff the distance ladder reproduces the e-vs-heavy envelope AND the widening ratio `∈ [1.80, 1.89]`; INFO if envelope-only; FAIL if `d_i` is generation-degenerate.
   - **Effort**: 1–2 agent-sessions (machinery exists; the new content is the multiplicity-bundle metric).

**V.3. transit's inter-sector freeze-in block (the over-constrained predictor)**
   - **What**: fit `{S₀, |w|}` to the charged-lepton masses and `arg(w)` to ONE mixing datum, then **predict** the six quark ratios + CKM angles + `J_CP` with no further freedom. Over-constrained by construction.
   - **Inputs**: the diabatic/Casimir-graded freeze-in amplitude `exp(−S₀·C₂)` (`S₀ ≈ 3.2`, an O(1) instanton action — note `S₀` is a *ratio*, `(ε_LX-split scale)/(horizon κ)`, so magnitude and slope close jointly); the `[[d,w],[w*,d]]` block structure; PDG quark masses + CKM angles + `J_CP` as the held-out test set.
   - **Gate**: new `S100-FREEZE-IN-PREDICT`. A clean FAIL closes the dynamical-freeze-in corridor; a PASS *derives* the mass+mixing **shape** (not the scale) from substrate dynamics. Threshold: predicted CKM angles within their PDG 1σ AND quark-ratio OOMs correct.
   - **Effort**: 2–3 agent-sessions.

**V.4. hawking's envelope over-determination**
   - **What**: compute the diagonal exponent from the greybody filter at the sonic `κ_SONIC = 0.7048 M_KK` and compare against transit's `S₀`; if they coincide, the envelope is derived twice (independent routes).
   - **Inputs**: `κ_SONIC = 0.7048 M_KK = 2π·0.112` (the `v = c_BLV` Mach-1 crossing — NOT `κ_GH = 1.365`); the greybody transmission `Γ(ω)·e^{−2πω/κ}`; the `Δω ~ 0.9 M_KK` one-fiber-gap frequency offset.
   - **Gate**: new `S100-ENVELOPE-OVERDETERMINE`. PASS (INFO-class) iff the two routes agree to within the panel's `Δω` tolerance; this is a consistency cross-check, not an independent observable.
   - **Effort**: 1 agent-session.

**V.5. [bridge-role] mass-scale `M₀` tie to the `m_H` threshold prediction**
   - **What**: trace whether the per-sector overall scale `M₀^{sector}` set by the KK threshold inherits the framework's `m_H` residual, and quantify how a 5–7% `m_H` over-prediction (framework `131.8` / tree `134` vs PDG `125.1` GeV) propagates into the absolute mass normalization.
   - **Inputs**: `KK-THRESHOLD-64` machinery; `canonical_constants.py`: `m_H_obs = 125.1`; the framework `m_H = 131.8` (KK-threshold) and `134` (tree-level filter-independent) values.
   - **Gate**: new `S100-M0-MH-INHERITANCE` (INFO-class). Report-only: documents whether the `M₀` scale is anchored independently or carries the `m_H` residual. No PASS/FAIL — this is a provenance trace feeding the honest-scope ledger.
   - **Effort**: ~2 hours, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | S97 `1:1:1` is the Homogeneity wall (W2); reality (W1) innocent; twist dead (Skolem–Noether) | GEOMETRIC | PROVEN (§VII.BL STAGE-3-PERMANENT) | Corridor re-posed: hierarchy ∈ external non-LI `ε_LX`, outside every `A_K`-module |
| 2 | One inter-sector block `[[d,w],[w*,d]]`; reality forces `\|w\|`→split, `arg w`→mixing/CP | GEOMETRIC | Structurally resolved, numerically open | Modulus/phase split is axiom-forced, not modeled; BDI→CP tie derived |
| 3 | Diagonal envelope = one Casimir exponential, four faces | GEOMETRIC | CLEAN structural win (envelope magnitude) | `exp(−(k+S₀)C₂)` — transit co-sets slope, no second lever (double-counting guard) |
| 4 | Three generations from dual-`Z₃` (triality × `s_φ`); lepton-only φ-lever | PARTICLE | Structural | Origin for the lepton-vs-quark hierarchy-shape difference the SM fits by hand |
| 5 | `1.889` widening: Casimir `9/5 = 1.800` (4.7%, 0-param) vs generic `n²=3.0` (59%) | GEOMETRIC | OPEN (sector-assignment-dependent) | Parameter-free discriminator selecting Casimir ladder; arithmetic verified vs PDG |
| 6 | Production = squeezed vacuum (no `κ`); filter `κ_SONIC=0.7048 M_KK`; scale `M₀` generation-blind | PHONONIC | Settled (with convention pins) | KK threshold is the SCALE, not the grading; inherits `m_H` residual |
| 7 | Cross-frontier unification: one `w` ↔ μ↔τ split + mixing/CP + baryon asymmetry (`φ₈₈`) | GEOMETRIC | K=2 named precondition (Non-LI-Deformation-Necessity) | K=3 needs `δ_CP` to LAND, not be asserted — correct discipline |

---

*Fidelity ledger (mine): all PDG-anchored numbers in this synthesis were re-verified against `canonical_constants.py` PDG-2024 entries (`m_e`, `m_mu` exact; `m_tau = 1.77686` GeV) — the panel's `1 : 0.0595 : 0.000288` ratio and `1.8894` / `9/5 = 1.800` (4.7%) / `3.0` (59%) widening numbers reproduce to full precision. The Homogeneity wall (§VII.BL) was confirmed STAGE-3-PERMANENT in `permanent-results-registry.md`; the `S97-YUKAWA-FAMILY-DERIVE` FAIL (`R_cross = 1.01970`) and the `S99-E1-STAGE2-VERIFY` PASS are authoritative and NOT re-adjudicated. The only source discrepancy found — the panel's present-tense framing of an already-PASSed/promoted Stage-2 gate — is a status-currency drift, not a substantive conflict, resolved in favor of the registry per the source-authority hierarchy.*
