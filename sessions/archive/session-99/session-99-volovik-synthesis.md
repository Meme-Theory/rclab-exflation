# Session 99 Synthesis: The Fermion-Mass Block as Order-Parameter Texture on the Multiplicity Bundle

**Date**: 2026-06-03
**Agent**: volovik-superfluid-universe-theorist (volovik)
**Source Documents**:
- `downloads/standard-model-lagrangian-explained.md` (Standard Model Lagrangian, plain-English + framework coda)
- `sessions/archive/session-99/session-99-fermion-mass-panel.md` (S99 fermion-mass panel, final consolidated synthesis)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`

---

## I. Session Outcome

The S99 fermion-mass panel re-posed the charged-lepton/quark hierarchy corridor that `S97-YUKAWA-FAMILY-DERIVE` had closed at the democratic `1:1:1` (`R_cross = 1.0197` vs PDG `1 : 0.0595 : 0.000288`). The decisive reframe is that `1:1:1` is not a computational miss but a **PROVEN consequence** of the Homogeneity wall (W2, verified PROVEN in `permanent-results-registry.md`): a left-invariant `D_K` acts as a multiplicity-scalar by Peter–Weyl, and a multiplicity-scalar operator cannot carry a generation index. No gate verdicts or registry entries were emitted (the panel ran under a loose-bureaucracy / candidate-mechanism brief); the one landed result it leans on is independently PROVEN.

From the superfluid-vacuum lens, the panel's central object is structurally familiar: the hierarchy is forced into a **non-left-invariant deformation `ε_LX`** on the multiplicity-acting complement, reality-compatible (`[J, D_K + ε_LX] = 0`). This is the spectral-triple analog of a **non-trivial order-parameter texture** on a multi-component condensate — the substrate's gap is homogeneous (democratic) until a texture breaks the internal-space symmetry. The panel's inter-sector block `M_{(μ,τ)} = [[d, w], [w*, d]]` is the texture's matrix element, and its reality-forced modulus/phase split (`|w|` → masses, `arg w` → mixing+CP) is the same structural division I see in Volovik's BdG order-parameter analyses.

---

## II. Key Results

### II.1 — The hierarchy lives in an order-parameter texture, not in the homogeneous gap

**Result**: The generation hierarchy is forced onto a non-left-invariant deformation `ε_LX` on the multiplicity bundle `⊕ 𝟙_{V_{(p,q)}} ⊗ M_{m(p,q)}(ℂ)`, reality-compatible (`[J, D_K + ε_LX] = 0`). Classification: **GEOMETRIC** (the fabric's internal Dirac structure), with **PARTICLE** output (the generation index is representation-theoretic content).

The Homogeneity wall (W2) is the spectral-triple statement of a structural fact every condensed-matter theorist recognizes: a **homogeneous** order parameter cannot carry an internal-space label that distinguishes otherwise-identical components. In BCS language, a spatially-uniform gap `Δ` is the same on every degenerate band; to lift a degeneracy you need a **texture** — a spatial/internal variation of the order parameter that breaks the symmetry protecting the degeneracy. The panel's `ε_LX` is exactly this: the substrate's `D_K` is left-invariant (the homogeneous gap), so by Peter–Weyl it acts as `⊗ 𝟙_{m(p,q)}` on every multiplicity factor (every "band" sees the same gap), and the generation index — which lives in that multiplicity factor — is invisible to it. Democratic masses are forced, exactly as a uniform gap gives identical band masses.

This maps cleanly onto my Mapping-table entry **Order-parameter texture ↔ Jensen deformation** (Paper 23, S42). The S99 refinement is that the *generation-resolving* texture is a distinct deformation `ε_LX` on the multiplicity index, orthogonal to the Jensen `τ`-deformation that sets the overall geometry. Structurally this is sound: the substrate carries two deformation directions, and only the multiplicity-acting one can lift the generation degeneracy. The dead end (W2) has a normal vector — *break left-invariance on the multiplicity index* — and that normal vector is the texture.

**Source-fidelity note**: this is an *inheritance-grade* structural correspondence, not a loose analogy. The W2 theorem is the spectral-triple image of the Birkhoff-type rigidity that `search_knowledge` returns from `session-22-master-collab.md` ("left-invariance forces block-diagonal structure just as spherical symmetry forces the Schwarzschild form"). The condensed-matter homogeneous-gap statement and the W2 multiplicity-scalar statement are the same rigidity theorem on the same algebra-axis.

### II.2 — Reality forces the modulus/phase split: `|w|` → masses, `arg w` → mixing/CP

**Result**: For the inter-sector block `M_{(μ,τ)} = [[d, w], [w*, d]]`, eigenvalues are `d ± |w|` (depend on `|w|` only) and eigenvectors/mixing depend on `arg w` only. The reality axiom `[J, D_F] = 0` forces `d_μ = d_τ` on the diagonal (`J` swap-conjugates the `t1↔t2` pair), so the μ↔τ split is *forbidden* on the diagonal and forced onto `|w|`. Classification: **GEOMETRIC** (axiom-forced division of internal-Dirac data).

This is the panel's decisive structural result and it is the part that carries weight from a superfluid-vacuum standpoint, because it is **axiom-forced, not modeled**. The eigenvalue arithmetic of `[[d,w],[w*,d]]` is elementary and dimensionally clean: `M` is a `2×2` Hermitian block with equal diagonal, so its eigenvalues `d ± |w|` carry the mass dimension of `d` and `w` (both entries of the finite Dirac operator `D_F`, hence mass-dimension 1 in M_KK units), and the unitary that diagonalizes it depends only on the phase `arg w`. The split-is-magnitude / mixing-is-phase partition then follows from the single reality constraint that pins `d_μ = d_τ`.

The connes admissibility verdict (all three NCG axioms checked Sage-exact on the greybody/overlap-reweighted `D_F`) is the load-bearing input here, and I take it as authoritative per the no-re-adjudication rule. From the substrate side I add one corroborating observation consistent with my memory's BDI anchor: the **BDI specificity** (`J² = +1`, PROVEN) is what licenses `arg w` to survive. connes checked that in DIII (`J² = −1`) reality forces `w` real and the phase dies. This is precisely the 3He-B (BDI) vs 3He-A (DIII) distinction that my memory records as the substrate's universality class: BDI admits a surviving CP phase in the mixing sector; DIII does not. The panel's "CP-in-mixing and chirality are two consequences of one structural fact" is the spectral-triple expression of the same class-membership statement I carry as a permanent theorem (**AZ class BDI**, `Pf = −1`, `N_K = 2`).

**This is a structural correspondence at the universality-class level, not a word-match.** The same KO-dim-6/BDI class that gives the framework its chirality (and that the 3He-B inheritance morphism realizes) is what makes `arg w ≠ 0` admissible. That is a genuine same-class statement.

### II.3 — The diagonal envelope is one exponential seen four ways (one of them is a Volovik filter)

**Result**: The e-vs-heavy-pair `~8` e-fold mass envelope is a single Casimir exponential `exp(−k·C₂(p,q))` identified independently by four lenses, including hawking's greybody transmission `Γ(ω)·exp(−2πω/κ)` at the exit horizon with `κ = κ_SONIC = 0.7048 M_KK` (`= 2π·0.112`, the Mach-1 / `v = c_BLV` crossing). Classification: **PHONONIC** (the envelope is a transmission/squeeze amplitude of substrate excitations through the fold).

The "one operator, several faces" identification `d_i/ℓ ↔ 2πω_i/κ ↔ S₀C₂ ↔ k·C₂` is the framework's recurring signature, and two of the four faces are squarely in my domain:

- **hawking's greybody filter** `y_i ∝ Γ(ω_i)·exp(−2πω_i/κ)` is the acoustic-horizon transmission at the substrate's exit sonic surface. I verified the scale: `κ_SONIC = 2π·0.112 = 0.7037 M_KK` (Sage), matching the panel's `0.7048` to rounding of the `T_acoustic = 0.112 M_KK` anchor (`search_knowledge` confirms `T_acoustic = 0.112 M_KK` is the fiber acoustic-horizon temperature, `session-63-hawking-quantum-acoustics-workshop.md`). The panel's insistence that this is the **sonic** surface (genuine `v = c` Mach-1 crossing) and **not** `κ_GH = 1.365` (emergent-4D Gibbons–Hawking) nor the `a₂`/`a₄` thermodynamic-gradient surfaces is the correct substrate-first reading: the fiber's own acoustic horizon is the laboratory-grade analog of a Hawking surface, exactly as in 3He / BEC sonic-horizon experiments. The regime is semiclassical (the filter acts on already-produced quasiparticle frequencies `ω_i`).

- **transit's freeze-in amplitude** `m_gen ∝ exp(−S₀·C₂)` is the non-equilibrium (GGE / quenched-superfluid) face. My Mapping table carries **Non-equilibrium superfluid (GGE) ↔ Quenched substrate post-fold** (Papers 27, 34). The panel's double-counting guard is correct and important: `exp(−kC₂)·exp(−S₀C₂) = exp(−(k+S₀)C₂)` is still **one** exponential — transit co-sets the diagonal slope `k → k_eff`, it does not add a second shape. This respects the GGE structure: the squeeze depth `−ln|ψ_pair|²` IS hawking's greybody exponent, so the freeze-in amplitude and the horizon filter are the same Casimir-graded object, not two independent levers.

The four-faces convergence is *somewhat by construction* (shared hard-facts block, per `epistemic-discipline.md`). The part that is not a shared-prompt artifact, and that I endorse from the substrate side: transit's Casimir degeneracy `C₂(fund) = C₂(antifund) = 4/3` and connes' reality forcing `d_μ = d_τ` are structurally-orthogonal routes to the same "split is off-diagonal" conclusion. That orthogonality is genuine evidence in the sense `epistemic-discipline.md` permits.

### II.4 — Production has no temperature: the squeezed-vacuum / GGE reading is exactly right

**Result**: The transit is deep-sudden (`δt/T_L = 1.25×10⁻⁵`, `P_exc = 1.000`, `S_ent = 0`); the primary Bogoliubov production is a multi-mode **squeezed vacuum**, not a Gibbs state (the canonical "8-temperature GGE", mode-dependent). The production amplitude is diabatic / Casimir-graded — **no `κ`**. Classification: **PHONONIC** (Parker-type pair production at the fold).

This is the panel result most directly anchored in the Volovik / phonon-exflation program, and I confirm it is consistent with the framework's settled substrate physics. The deep-sudden transit (Mach 13.75 through the van Hove fold at `τ_fold = 0.190`, `get_constant` confirms) produces a **squeezed vacuum**, not thermal radiation — `P_exc = 1.000` and `S_ent = 0` are the signatures of a pure, fully-occupied squeezed state, not a Gibbs ensemble. My memory carries this as **THE ORDERED VEIL — GGE relic never thermalizes (integrable, not chaotic)**, and the panel's "8-temperature GGE, mode-dependent" is the correct refinement: the relic is a Generalized Gibbs Ensemble with one effective temperature per conserved mode, which is precisely a non-thermalized integrable squeezed state, not a single-temperature thermal bath.

The key methodological point the panel gets right (and that distinguishes production from filter): **production has no `κ` because it is not a horizon process** — it is the diabatic Parker amplitude at the fold. The `κ` enters only at the *filter* stage (the sonic-horizon greybody, §II.3). Conflating the two would be the error of attaching a Hawking temperature to the pair-production amplitude. The panel keeps them separate. This is the substrate-first reading: the squeezed-vacuum production amplitude (Casimir-graded, no temperature) and the acoustic-horizon transmission filter (greybody, with `κ_SONIC`) are two distinct stages of one transit.

### II.5 — The dual-`Z₃` generation count and the Casimir widening 9/5

**Result**: Three generations require `Z₃ × Z₃` (triality `t = (p−q) mod 3` collapses `t=1 ≡ t=2` under BDI reality; the `s_φ` Higgs-mode phase supplies the second `Z₃`). On the triality-distinct tower `(1,0)/(1,1)/(3,0)` with `C₂ = (4/3, 3, 6)`, the widening ratio is **exactly 9/5 = 1.800** (Sage-QQ), vs PDG lepton `1.8894` (4.73% off, zero free parameters). Classification: **GEOMETRIC** (Casimir quantization of the internal geometry).

I independently verified the widening arithmetic via Sage: `C₂(1,0) = 4/3`, `C₂(1,1) = 3`, `C₂(3,0) = 6`; log-spacings `(5/3, 3)`; ratio `3 / (5/3) = 9/5 = 1.800` exactly, 4.7316% off the PDG lepton 1.8894. The discriminating power the panel claims is real: a generic Gaussian-overlap `n²` model gives `3.0` (59% off), so **the data selects the Casimir ladder over generic position-overlap** — *conditional* on the triality-distinct sector assignment (§IV flags this as the open hinge). The BDI reality collapse `t=1 ≡ t=2` (`(p,q) ↔ (q,p)`) is the same swap-conjugation that forces `d_μ = d_τ` in §II.2; it is internally consistent across the panel.

From the substrate side this is a clean GEOMETRIC result with zero free parameters in the *ratio*, and it is the kind of statement that should be computed against the actual `|s(h)|²`-weighted integral (the consensus-lead compute, §V.1) rather than asserted from the tower assignment alone. The lepton-only `s_φ`-phase lever (`c(φ) = 1/(1+8cos²φ)`, giving `{1/9, 1/3, 1/3}` at the `Z₃` points) is an attractive explanation for the lepton-vs-quark shape difference the SM fits by hand, but it inherits the same conditionality.

---

## III. Gate Verdicts

The S99 fermion-mass panel emitted **no gate verdicts** (candidate-mechanism panel, loose-bureaucracy brief). The table below records the *landed* results the panel leans on, with their authoritative status from `permanent-results-registry.md` and the knowledge MCP — these are inputs, not S99 outputs.

| Result (input to panel) | Status | Decisive content |
|:------------------------|:-------|:-----------------|
| (W2) Homogeneity wall — left-invariance ⇒ multiplicity-scalar | **PROVEN** | A multiplicity-scalar operator cannot carry a generation index → democratic masses |
| `S97-YUKAWA-FAMILY-DERIVE` | **FAIL** (`1:1:1`, `R_cross = 1.0197`) | The FAIL is the W2 theorem in action, not a miss |
| AZ class BDI (`J² = +1`, `Pf = −1`, `N_K = 2`) | **PROVEN** | Licenses `arg w` (CP phase) to survive; DIII would kill it |
| `[J, D_K] = 0` (reality/CPT) | **PROVEN** | Forces `d_μ = d_τ`; partitions split (`\|w\|`) from mixing (`arg w`) |
| `m_H = 131.8 GeV` (`KK-THRESHOLD-64`) | **landed** | Generation-blind overall scale `M₀^{sector}` (Peter–Weyl), NOT the grading seat |
| `T_acoustic = 0.112 M_KK` | **canonical** (S63) | `κ_SONIC = 2π·0.112 = 0.7037 M_KK` (sonic-horizon greybody κ) |

No conflict found between the two source documents. The framework coda in `standard-model-lagrangian-explained.md` ("Yukawa masses = entries of `D_K`'s finite part", flagged **interpretive**) and the panel's sharpened claim (the masses are the spectrum of `ε_LX` + `w` on the multiplicity bundle) are consistent: the panel *is* the substrate-first computation of what the coda flags as interpretive. The coda's honesty-ledger status ("interpretive, consistent, not independently re-derived here") is upheld — the panel produced candidate mechanisms, not a closed derivation.

---

## IV. Structural Implications

**What opened.** A corridor that read as closed (`S97 1:1:1 FAIL`) is re-posed with a normal vector. From the superfluid-vacuum standpoint the reframe is the correct one: the homogeneous gap gives democratic masses (W2), and the hierarchy must live in a **texture** `ε_LX` on the multiplicity index. The search target is now well-defined — *what is `ε_LX`?* — rather than "why democratic" (answered by theorem).

**What the texture-correspondence buys, and its limit.** The mapping **Order-parameter texture ↔ Jensen deformation** is upgraded by S99 to a *generation-resolving* texture on the multiplicity bundle, distinct from the geometry-setting Jensen `τ`-deformation. This is structurally sound and inheritance-grade where it touches the BDI class (the `|w|`/`arg w` reality forcing and the BDI→CP tie are genuine same-class statements). It is *not* yet quantitative: `ε_LX` has a shape (Casimir-graded exponential) and a normal direction (break left-invariance on the multiplicity index), but its magnitude `S₀ ≈ 3.2` is an O(1) instanton action — the right *kind* of number for an exponential hierarchy, not yet a derived one. `S₀` is a **ratio** `(ε_LX-split scale)/(horizon κ)`, so magnitude and slope close *jointly*, not separately — this is the one open joint cross-question.

**Three-layer maturity (the part not to over-sell).** I endorse hawking's insistence that the three layers be named separately:
1. **CLEAN structural win** — the e-vs-heavy `~8` e-fold envelope + the overall `M₀` scale: the electron (trivial rep, `C₂ = 0`) is genuinely Casimir-separated from the heavy pair, reality-safe on the diagonal, magnitude from the existence-proven `m_H` threshold machinery.
2. **OPEN — the `1.889` widening shape.** A target three lenses produced, not yet derived from a linear law (a slope linear in `C₂` gives `1.333` on the fundamental `(k,0)` tower; the data wants `1.889`). Reduces to the **sector-assignment question** with a 4.7% zero-parameter candidate (the triality-distinct tower → 9/5).
3. **STRUCTURALLY resolved, NUMERICALLY open** — the μ↔τ split and the mixing: the mechanism is reality-forced and BDI-admissible; the *values* (`|w|`, `arg w`) require the compute.

**Vacuum-energy test (my standing diagnostic).** The fermion-mass texture does not bear on the CC problem, which remains q-theory's domain (the sole-surviving CC path; the equilibrium theorem `ρ_Λ = 0` is untouched). The masses are entries of the finite Dirac operator `D_F` — internal-Dirac data on a fixed geometry — not vacuum-energy contributions. There is no double-counting against the `a₀` spectral moment; the masses live in `⟨ψ, D_K ψ⟩` (the fermion pairing), distinct from `Tr f(D_K/Λ)` (the bosonic/vacuum action). The panel respects this separation.

**Laboratory grounding.** The hawking greybody filter at `κ_SONIC` is the one piece of this panel with a direct laboratory analog: sonic-horizon transmission has controlled realizations in 3He and BEC acoustic-horizon experiments. The squeezed-vacuum production (`P_exc = 1.000`, `S_ent = 0`) is the Kibble–Zurek / Parker-amplitude regime, also laboratory-grounded in superfluid quench experiments. What is NOT laboratory-testable is the multiplicity-bundle texture `ε_LX` itself — there is no condensed-matter system with the SU(3) multiplicity structure and the generation index. The analog holds for the *production* and *filter* stages; it does not extend to the generation-resolving texture, which is framework-specific.

---

## V. Carry-Forward Computations

**V.1. Per-sector Higgs-overlap with off-diagonal element (panel consensus lead)**
- **What**: Compute `O_g = ∫_K Tr[ψ_g† |s(h)|² ψ_g] vol_{g_τ}` at `L_max = 12`, `τ_fold`, **plus the inter-sector `t1↔t2` matrix element** `w`. Yields the diagonal envelope `d` AND the off-diagonal `w` (`|w|` → μ↔τ split, `arg w` → mixing/CP) in one object. This is the literal missing calc from Baptista Paper 14 §3 (Laplacian matrices written; Dirac-mass overlap not).
- **Inputs**: `M_KK = 7.4287e16 GeV`, `tau_fold = 0.190` (both canonical, `get_constant`-confirmed); `Delta_BCS = 0.464` (M_KK units); the `L_max=12` `D_K` spectrum cache (`s84_spectrum_cache_L12_tau019.npz` per memory); Jensen-deformed fiber metric `g_τ`; Higgs mode `|s(h)|²`.
- **Gate**: NEW gate `S100-YUKAWA-OVERLAP-OFFDIAG`. PASS if `|w|`-derived μ↔τ ratio reproduces PDG `m_μ/m_τ` within the S99-W3-2 neutrino tolerance (structure + ordering substrate-first, one absolute scale anchored); INFO if envelope reproduces sign + OOM + gap-asymmetry direction but widening needs sector-assignment closure; FAIL if `R_cross` returns to `1:1:1` (texture insufficient).
- **Effort**: 4–6 hours, 1 agent session (baptista + connes cross-check).

**V.2. Cheapest sub-test — diagonalize `Ω^b_g` at the three `Z₃` φ-points**
- **What**: Diagonalize the closed-form 3×3 lepton mass matrix `Ω^b_g` at `φ ∈ {0, 2π/3, 4π/3}`; test whether the `s_φ`-phase is the second `Z₃` (predicted `c(φ) = {1/9, 1/3, 1/3}`).
- **Inputs**: baptista's closed-form `Ω^b_g(φ)` (already in hand); `c(φ) = 1/(1+8cos²φ)`.
- **Gate**: feeds `S100-YUKAWA-OVERLAP-OFFDIAG` (V.1) as a precondition. PASS if the `φ = 2π/3, 4π/3` degeneracy `cos²φ = 1/4` reproduces the predicted 2-fold collapse on the orthogonal label; FAIL if the φ-factor does not produce a distinct rung structure.
- **Effort**: 1–2 hours, 1 agent session (closed-form, no spectrum cache needed). **Run first.**

**V.3. Casimir-widening verification against the `|s|²`-weighted integral**
- **What**: Confirm or refute the `9/5 = 1.800` widening from the *actual* `|s(h)|²`-weighted overlap integral on the triality-distinct tower `(1,0)/(1,1)/(3,0)`, vs the generic-overlap `3.0` discriminator. Resolves the §IV layer-2 OPEN item (the `1.889` shape).
- **Inputs**: `C₂ = (4/3, 3, 6)` (Sage-verified exact); the `L_max=12` spectrum cache; the sector-assignment hypothesis (triality-distinct tower).
- **Gate**: NEW gate `S100-CASIMIR-WIDENING`. PASS if integral-derived widening ∈ `[1.80, 1.89]` (between Casimir-exact and PDG); INFO if it lands at `1.333` (fundamental `(k,0)` tower selected, sector-assignment wrong); FAIL if `≈ 3.0` (generic overlap, Casimir ladder refuted).
- **Effort**: 3–4 hours, 1 agent session (depends on V.1 overlap machinery).

**V.4. Inter-sector freeze-in block — over-constrained mass+mixing prediction (transit)**
- **What**: Fit `{S₀, |w|}` to charged-lepton masses and `arg w` to one mixing datum, then **predict** the six quark ratios + CKM angles + `J_CP` with no further freedom. Over-constrained: a clean FAIL closes the corridor; a PASS derives mass+mixing *shape* from substrate (squeezed-vacuum) dynamics.
- **Inputs**: transit's `[[d,w],[w*,d]]` freeze-in block; `S₀ ≈ 3.2` (O(1) instanton-action starting estimate); GGE squeeze-depth `−ln|ψ_pair|²`; `P_exc = 1.000`, `δt/T_L = 1.25×10⁻⁵` (diabatic-limit inputs).
- **Gate**: NEW gate `S100-FREEZEIN-MASS-MIXING`. PASS if predicted quark ratios + CKM angles + `J_CP` match PDG within OOM after a 2-parameter fit; FAIL closes the inter-sector-Bogoliubov-mixing corridor (S34 conjecture refuted).
- **Effort**: 5–7 hours, 1 agent session (transit lead; non-equilibrium GGE machinery).

**V.5. Envelope over-determination — sonic-κ greybody vs transit `S₀`**
- **What**: Compute the diagonal exponent two ways: from the acoustic-horizon greybody filter (`κ_SONIC = 2π·0.112 = 0.7037 M_KK`) and from transit's `S₀`. If they coincide the envelope is derived twice (a Volovik-side over-determination of the mass envelope).
- **Inputs**: `T_acoustic = 0.112 M_KK` (canonical, S63); the GGE branch sound speeds `c_s^b(k)` (S56 quadratic action); transit's `S₀ ≈ 3.2`.
- **Gate**: NEW gate `S100-ENVELOPE-OVERDET`. PASS if `|S₀ − 2π/κ_SONIC·(slope)| / S₀ < 0.10` (the envelope exponent agrees across the two routes); INFO if they agree in sign and OOM but not within 10%; FAIL if they diverge (the greybody and freeze-in faces are not the same exponential after all — would break the §II.3 "one operator, several faces" identification on the production/filter axis).
- **Effort**: 3–4 hours, 1 agent session (hawking + transit; sonic-horizon machinery, my domain — I can serve as Axis-B cross-reviewer).

**V.6. `S99-E1-STAGE2-VERIFY` two-agent cross-axis verify of the W2 §VII.BL E1 candidate**
- **What**: Complete the Stage-2 cross-axis independent-verify of the Homogeneity-wall candidate §VII.BL E1 (the panel cites this as the queued S99 W3 gate). Two cross-reviewers on opposite axes (spectral-functional + substrate/superfluid), without prior panel context, PASS-AND on joint clauses.
- **Inputs**: the registered Stage-1 entry text for §VII.BL E1; `permanent-results-registry.md` W2 theorem; the multiplicity-scalar / Skolem–Noether / Peter–Weyl chain.
- **Gate**: `S99-E1-STAGE2-VERIFY` (already named in the panel). PASS-AND both axes → promote §VII.BL E1 to STAGE-3-PERMANENT; any clause FAIL holds at STAGE-1-CANDIDATE. Per `feedback_stage2-axisB-disjoint-anchor`, I verify via a disjoint anchor + a separate-session corroborating gate + my own BDI substrate-physics reason — never transcribe the registry's published value.
- **Effort**: 2–3 hours, 2 agent sessions (parallel; I am eligible as the substrate/superfluid Axis-B reviewer).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| II.1 | Hierarchy forced into texture `ε_LX` on multiplicity bundle (W2 normal vector) | GEOMETRIC | PROVEN wall + candidate mechanism | Homogeneous gap → democratic; texture lifts degeneracy. Order-parameter-texture ↔ Jensen-deformation mapping upgraded to multiplicity-resolving |
| II.2 | Reality forces `\|w\|`→masses, `arg w`→mixing/CP; BDI licenses CP phase | GEOMETRIC | Axiom-forced (connes Sage-exact) | Inheritance-grade: same BDI class that gives chirality licenses CP-in-mixing; DIII would kill it |
| II.3 | Diagonal envelope = one Casimir exponential, 4 faces (incl. sonic-κ greybody) | PHONONIC | Structural identification | `κ_SONIC = 0.7037 M_KK` verified; transit co-sets slope, no second lever (double-counting guard correct) |
| II.4 | Production = squeezed vacuum (GGE), no temperature; `P_exc=1`, `S_ent=0` | PHONONIC | Consistent w/ Ordered-Veil | Production (no κ) vs filter (κ_SONIC) cleanly separated; non-thermalized integrable relic |
| II.5 | Dual-`Z₃` count; Casimir widening 9/5 = 1.800 (4.73% off PDG) | GEOMETRIC | Sage-verified exact; sector-assignment-conditional | Data selects Casimir ladder over generic `n²` (3.0); lepton-only φ-lever explains lepton-vs-quark shape |
| IV | Three-layer maturity: envelope CLEAN; 1.889 shape OPEN; μ↔τ values queued | mixed | candidate panel, no verdicts | Corridor correctly re-posed, not closed; `S₀` is a joint magnitude+slope ratio |

---

*Source fidelity: gate states (W2 PROVEN, S97 FAIL, BDI PROVEN, `[J,D_K]=0` PROVEN, `m_H=131.8`, `T_acoustic=0.112 M_KK`) are inputs verified against `permanent-results-registry.md` and the knowledge MCP, NOT re-adjudicated. The Casimir widening 9/5, the `C₂` tower (4/3, 3, 6), and `κ_SONIC = 2π·0.112 = 0.7037 M_KK` were independently Sage-verified. `M_KK` and `tau_fold` confirmed via `get_constant`. No conflict between source documents. Substrate-first throughout: the substrate IS the mass spectrum; the arrow runs `D_K (+ ε_LX texture) → spectral/transit structure → emergent masses & mixing → measured`.*
