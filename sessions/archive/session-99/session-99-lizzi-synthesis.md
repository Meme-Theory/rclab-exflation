# Session 99 Synthesis: Fermion Masses Live in the Functional-Independent Sector of D_K

**Date**: 2026-06-03
**Agent**: lizzi-spectral-functional-theorist (Lizzi)
**Source Documents**:
- `downloads/standard-model-lagrangian-explained.md` (the expanded SM Lagrangian + the project's substrate-picture coda: bosonic L = a₄, gravity = a₂, Yukawa masses = entries of D_K's finite part)
- `sessions/archive/session-99/session-99-fermion-mass-panel.md` (the `s99-fermion-mass-panel` generative exercise on the fermion mass-and-mixing matrix as geometric data of D_K's finite part)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

---

## I. Session Outcome

The S99 fermion-mass panel re-posed the charged-fermion hierarchy corridor that `S97-YUKAWA-FAMILY-DERIVE` closed at `1:1:1` (`R_cross = 1.019704` vs PDG `1 : 0.0595 : 0.000288`). The decisive structural move — and the one most consequential from a spectral-functional standpoint — is that the `1:1:1` democracy is the **PROVEN Homogeneity wall (W2)**, not a computational miss, and it lives **entirely in D_K's finite (fermionic) part**: the pairing `⟨ψ, D_K ψ⟩`, never the bosonic spectral action `Tr f(D_K/Λ)`. **This is the single most important functional-sensitivity fact about the session: every result the panel produces is FUNCTIONAL-INDEPENDENT — it does not depend on whether the bosonic action is built from a cutoff `f(x)`, the zeta action `S_ζ = ζ_{D_K}(0)`, or the anomaly-derived functional.** The hierarchy problem is a problem about the *eigenvalue data of D_K's finite block*, and that data is fixed before any spectral functional is chosen. No gate verdicts were emitted (loose-bureaucracy generative panel); the one PROVEN result it leans on (W2) is independently verified PROVEN in `permanent-results-registry.md`, and I confirmed it against the knowledge MCP.

---

## II. Key Results

### 1. The fermion-mass sector is functional-INDEPENDENT — the regularization debate does not touch it

**Result**: Fermion masses = entries of the finite part of `D_K`, accessed via the spectral pairing `⟨ψ, D_K ψ⟩`. Classification: **GEOMETRIC** (the fabric's internal Dirac eigenvalue data; PARTICLE at the representation-theoretic depth).

The SM-Lagrangian coda makes a clean two-part decomposition that maps directly onto my domain. The **bosonic** Lagrangian (Blocks 1, 3–8: gauge kinetics, gauge self-interactions, Higgs kinetic + potential) is the **a₄ Seeley–DeWitt moment** of `Tr f(D_K/Λ)`; gravity is the neighboring **a₂** moment (both confirmed canonical via knowledge MCP, `Φ(a₄)=Σ₃` Yang–Mills+Higgs, `Φ(a₂)=Σ₂` Einstein–Hilbert). The **fermionic** terms (Block 10 kinetic/mass, Blocks 11–13 force couplings, Block 14 Yukawa) are the pairing `⟨ψ, D_K ψ⟩`, and the Yukawa masses are *entries of D_K's finite part*.

The cardinal spectral-functional point: **the a₄/a₂ split, and indeed the entire heat-kernel-vs-zeta-vs-anomaly debate that defines my research program, lives on the bosonic side `Tr f(D_K/Λ)`.** The choice of functional `f` determines which spectral moments enter the action and with what weight — it is the whole content of the cosmological-constant problem (`a₀` enters the cutoff action with weight `f₀`, but is *absent entirely* from `S_ζ = ζ_{D_K}(0) = a₄`). But the fermion masses are not moments of `f`. They are the bare eigenvalues of the finite block of `D_K`, read off *before* any spectral functional is applied. Substitution chain, made explicit per the double-check discipline:

```
Step 1: Bosonic action       S_bos = Tr f(D_K/Λ)  →  expand → Σ_n f_n a_n(D_K²)   [functional f enters as weights f_n]
Step 2: Fermionic action     S_ferm = ⟨ψ, D_K ψ⟩                                   [no f; D_K enters linearly, bare]
Step 3: Yukawa mass m_f       = (D_F)_{ff}  = matrix element of the FINITE part of D_K   [an eigenvalue datum, not a moment]
Step 4: ∂ m_f / ∂ f_n         = 0   for every regulator moment f_n                  [masses do not depend on the bosonic regulator]
Conclusion: the fermion mass spectrum is FUNCTIONAL-INDEPENDENT (regulator-invariant) by construction.
```

This is not a minor classification note. It means the S99 panel's entire object of study — the inter-sector mass block `[[d, w],[w*, d]]` — is on the safe side of the regularization ambiguity. Whatever the eventual resolution of "which spectral functional is physical" (zeta vs cutoff vs anomaly-derived), it changes the bosonic vacuum energy, Newton's constant, and the Higgs *potential* — but it does **not** change the fermion mass ratios. The panel's results are structural in the strongest sense available in this framework.

### 2. The Homogeneity wall (W2) is a Level-1 regulator-invariant identity

**Result**: `D_K` left-invariant on SU(3) ⇒ (Peter–Weyl) algebra acts as `⊗ 𝟙_{m(p,q)}` on every multiplicity factor ⇒ a multiplicity-scalar operator cannot carry a generation index ⇒ democratic masses, by theorem. Classification: **GEOMETRIC** (PROVEN, machine-precision; verified PROVEN in `permanent-results-registry.md` and the knowledge MCP).

From my methodology this is the cleanest kind of result: a **Level-1 substrate-IS structural identity** in the cross-pillar-bridge sense — regulator-invariant, L-independent (holds at every `L_max`), an identity at the representation-theoretic / Skolem–Noether level. The knowledge MCP returns it as `R_cross = 1` "by Skolem–Noether + Peter–Weyl, a representation[-theoretic identity]." It is exactly analogous to my own FUNCTIONAL-INDEPENDENT results (the `F_traj(k) = (k+1)/2` a₂-ratio identity, the CC-5 linearity identity): true independent of which functional you evaluate, because it is a statement about the *algebra's action on the multiplicity bundle*, not about any spectral moment.

The panel's reframe — the hierarchy is forced onto a non-left-invariant deformation `ε_LX` on the multiplicity-acting complement, reality-compatible (`[J, D_K+ε_LX]=0`) — is therefore a statement about a *perturbation to the finite Dirac operator*, which again is functional-independent. I note one strengthening the panel itself flags only in passing: the knowledge MCP shows `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` already **PASSED** (`value=0.0`, `EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE`, `L_max=12`). The ε_LX-on-multiplicity reframe is not merely a panel conjecture — its admissibility was gate-confirmed in S98. The panel's §1 foundation is firmer than its "candidate-mechanism" framing claims.

### 3. The reality axiom forces the modulus/phase division of labor — and this too is functional-independent

**Result**: On the inter-sector block `M = [[d, w],[w*, d]]`, eigenvalues `d ± |w|` depend on `|w|` only; eigenvectors (mixing) depend on `arg(w)` only. Reality `[J, D_F]=0` swap-conjugates the `(μ,τ) = t1↔t2` pair, forcing `d_μ = d_τ`, so the μ↔τ split is forbidden on the diagonal and forced onto the off-diagonal `|w|`. Classification: **GEOMETRIC** (axiom-forced, Sage-exact on the three NCG axioms per connes' lens).

This is the panel's decisive structural result and I endorse it without qualification, because the entire argument is conducted on `D_F` — the finite Dirac operator — using the spectral-triple *axioms* (order-one, KO-dim-6, reality), none of which reference a spectral functional. The split-is-`|w|` / mixing-is-`arg(w)` partition is a consequence of the eigenvalue arithmetic of a `[[d,w],[w*,d]]` block under the reality involution. It is regulator-invariant by the same logic as Result 1: it lives in the fermionic pairing, not the bosonic moment expansion.

The **BDI → CP** tie (`arg(w)` survives because `J²=+1`; it would be killed in DIII where `J²=−1` forces `w` real) is the most attractive piece. It is a Level-1 identity connecting the chirality class (PROVEN BDI) to the existence of the CP phase — one structural fact (KO-dim-6 / BDI) with two consequences (chirality + CP-in-mixing). This is precisely the kind of "what survives all choices is structural" result my methodology privileges.

### 4. The diagonal envelope — "one exponential seen four ways" — and where the functional WOULD re-enter

**Result**: The e-vs-heavy `~8` e-fold mass envelope is one Casimir exponential identified four ways: baptista `exp(−k·C₂)`, connes `exp(−d_i/ℓ)`, hawking `Γ(ω)·exp(−2πω/κ)`, transit `exp(−S₀·C₂)`, with the chain `d_i/ℓ ↔ 2πω_i/κ ↔ S₀C₂ ↔ k·C₂`. Classification: **GEOMETRIC** (envelope magnitude is a clean structural win; the overall scale `M₀^{sector}` is the generation-blind KK threshold that lands `m_H = 131.8 GeV`).

Here is the one place a spectral-functional caveat is genuinely load-bearing, and I flag it as a service to the next compute. The diagonal envelope is fermionic (finite-part eigenvalue spacings, functional-independent). But the **overall scale** `M₀^{sector}` is sourced from the KK-threshold machinery `KK-THRESHOLD-64` (`m_H = 131.8 GeV`, INFO verdict, `delta = 2.35` outside the PASS band `[0.73, 1.48]`) — and *that* machinery is a **bosonic** spectral-action object (the `|S|²` mode of the fiber embedding, a Higgs-sector quantity living at a₄). The panel correctly separates these: "a PASS derives the *shape*, not the scale." From my side I sharpen the reason: **the shape (mass ratios) is functional-independent fermionic data; the scale `M₀^{sector}` is functional-DEPENDENT bosonic data.** A re-run of the bosonic action under `S_ζ = ζ_{D_K}(0)` vs the cutoff would move `m_H` and `M₀^{sector}` (the Higgs mass is one of the three quantities — with the cosmological constant and Newton's constant — that I have repeatedly shown is set by the regularization scheme as much as by the spectrum). It would *not* move the `~8` e-fold envelope or the `1.889` widening ratio. The panel's "honest forecast" (shape substrate-first, one absolute scale anchored) is exactly the functional-dependence partition expressed in physics language.

### 5. The `1.889` widening — open, and orthogonal to the functional question

**Result**: PDG lepton widening ratio `1.8894`; Casimir ladder `(1,0)/(1,1)/(3,0)` with `C₂=(4/3,3,6)` gives `9/5 = 1.800` (4.7% off, zero free parameters); a linear-in-C₂ slope on the fundamental `(k,0)` tower gives `1.333`; generic Gaussian-overlap `n²` gives `3.0`. Classification: **GEOMETRIC** (a target three lenses produced; not yet derived from a linear law; reduces to a generation-sector-assignment question).

I have nothing to add on the resolution (it is a sector-assignment / Jensen-tilt question, not a functional question), but I record the functional-sensitivity verdict for the carry-forward: the `1.889` widening is a **ratio of fermionic eigenvalue spacings**, hence functional-independent. Whichever sector assignment wins, the answer will not move under a change of spectral functional. The open-ness is real but it is *orthogonal* to my axis — a useful thing for the next planner to know, because it means the widening compute does not need to be repeated across regularization schemes.

---

## III. Gate Verdicts

The S99 panel emitted **no** gate verdicts (generative candidate-mechanism exercise, loose-bureaucracy brief). The verdicts below are the *cited upstream* gates the panel and the SM-Lagrangian coda rest on, taken as authoritative (not re-adjudicated), and cross-checked against the knowledge MCP.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S97-YUKAWA-FAMILY-DERIVE` | FAIL | y-hierarchy `1:1:1` vs PDG `1:0.0595:0.000288`; `R_cross = 1.019704` (multiplicity-scalar) |
| (W2) Homogeneity wall theorem | PROVEN | left-invariance ⇒ multiplicity-scalar ⇒ democratic masses (machine-precision; `permanent-results-registry.md`) |
| `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` | PASS | `value=0.0`; `EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE`; `L_max=12` (ε_LX reframe admissibility) |
| `KK-THRESHOLD-64` | INFO | `m_H = 131.8 GeV`; `delta = 2.35` (outside PASS band `[0.73, 1.48]`) — overall scale machinery |
| S62 Yukawa tree-level | PROVEN | tree-level Yukawa vanishes by Peter–Weyl orthogonality |
| `S99-E1-STAGE2-VERIFY` | (queued, not yet emitted) | Stage-2 cross-axis verify of §VII.BL E1 (panel cites as future gate) |

**Conflict check**: The SM-Lagrangian coda tags the "bosonic Lagrangian = a₄" reading as **interpretive/defensible** (`r ≈ 0.96` vs the Baptista effective potential, not a closed proof). The fermion-mass panel does not re-tag this — it operates one level below (the *fermionic* pairing), so there is no conflict. I confirm the a₄/a₂ assignment is canonical *as a structural reading* (knowledge MCP), and that the panel's fermionic results do not inherit the a₄-correlation's interpretive caveat — they rest on the PROVEN W2 wall and the spectral-triple axioms, which are firmer than the a₄ potential-correlation. No source conflicts found.

---

## IV. Structural Implications

**What the constraint map gains.** The framework now has a clean **layer separation along the regularization axis**, mapped onto the SM Lagrangian's own bosonic/fermionic split:

- **Bosonic side (a₀, a₂, a₄) — functional-DEPENDENT.** This is my home territory: the cosmological constant (`a₀`, absent in `S_ζ`), Newton's constant (`a₂`), the Higgs potential and overall mass scale `M₀^{sector}`/`m_H` (`a₄`) are set by the choice of spectral functional as much as by the spectrum. The "which functional is physical" question (zeta L1 / Zubarev L2 / observable L3, per my three-layer regulator theorem) governs everything on this side.
- **Fermionic side (`⟨ψ, D_K ψ⟩`, Block 14 Yukawa) — functional-INDEPENDENT.** The mass *ratios*, the μ↔τ split mechanism, the mixing/CP structure, the `1.889` widening, the Homogeneity wall — all are eigenvalue data of D_K's finite part, fixed before any functional is chosen. The regularization debate does not reach them.

This is a strong structural statement and I have not seen it made explicit in prior sessions. It means the fermion-mass program can proceed **without resolving the functional-selection question** — a genuine decoupling, and the cleaner half of the Standard Model. It is the fermionic complement to the Fermionic-Bosonic Decoupling Theorem already in my memory (S71): there the decoupling was about *which moments* the fermion loop sources; here it is about *whether the regulator choice touches the fermion masses at all* (it does not).

**What opened.** The charged-fermion `○✗` block is correctly re-posed (not emptied): the question shifted from "why democratic" (answered by W2) to "what is `ε_LX`?" — a finite-part deformation, functional-independent. The consensus lead compute (baptista's overlap-plus-off-diagonal) is runnable next.

**What closed / narrowed.** Three corridors closed inside the panel, all functional-independently: (i) the twisted-automorphism escape (Skolem–Noether: `Aut(A_K)` is multiplicity-blind); (ii) "the KK threshold *is* the hierarchy" (hawking: bare tower sum is power-law-saturating and multiplicity-scalar — and I add, it is also functional-dependent, the wrong category for a regulator-invariant ratio); (iii) the single-`Z₃` generation count (baptista: needs the `Z₃ × Z₃` product). The diagonal μ↔τ split is forbidden by reality.

**What shifted.** connes retired his §3.4 seesaw-squaring as the *vehicle* (the factor-200 comes from greybody exponentiation of the ε_LX frequencies, not a charged seesaw). What survives — "squaring is shape-preserving" — is, I note, a statement about the eigenvalue ladder, hence functional-independent.

---

## V. Carry-Forward Computations

The panel's §8 ranked computes are the substrate-physics backbone; I add the spectral-functional-sensitivity annotations and one new functional-axis gate that my expertise specifically motivates.

```
V.1. Per-sector Higgs-overlap WITH off-diagonal element [PANEL CONSENSUS LEAD]
   - What: O_g = ∫_K Tr[ψ_g† |s(h)|² ψ_g] vol_{g_τ} at L_max=12, τ_fold, PLUS the inter-sector
           t1↔t2 matrix element; extract diagonal envelope {d_i}, |w|, arg(w); test 9/5 widening
           against the |s|²-weighted integral. Cheapest sub-test first: diagonalize Ω^b_g at the
           three Z₃ φ-points {0, 2π/3, 4π/3} (closed-form 3×3, in hand).
   - Inputs: D_K finite-part data; |s(h)|² Higgs-mode overlap; L_max=12 spectrum cache
            (s84_spectrum_cache_L12_tau019.npz); tau_fold=0.19 (canonical); C₂(p,q) Casimir values.
   - Gate: feeds the re-posed S97-YUKAWA-FAMILY-DERIVE corridor; new gate S99-CF-YUKAWA-OVERLAP-OFFDIAG.
           PASS = widening ratio within 5% of PDG 1.8894 AND |w|, arg(w) extracted; FAIL = ratio off
           or off-diagonal vanishes; INFO = sector-assignment-dependent partial.
   - Effort: 3-4 hours, 1 agent session (the 3×3 φ-point sub-test is <1 hour).
   - Functional-sensitivity note (LIZZI): the extracted RATIOS (widening, μ:τ:e) are
     FUNCTIONAL-INDEPENDENT — do NOT re-run across regularization schemes; one scheme suffices.
     ONLY the overall normalization (if any |s(h)|² scale is pulled from the bosonic a₄ action) is
     functional-dependent and must be tagged with its scheme.

V.2. Connes-distance ladder on the multiplicity bundle
   - What: compute d_i (Connes distance between generation-states on the multiplicity bundle) and
           test mass = e^{−d_i/ℓ}; check widening signature ≈ 1.89.
   - Inputs: S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY machinery (exists); finite D_F; J involution.
   - Gate: cross-checks V.1's envelope shape independently; new gate S99-CF-CONNES-DISTANCE-LADDER.
           PASS = d_i ladder reproduces the e-fold envelope AND widening ≈ 1.89; FAIL = ladder
           non-monotone or wrong gap; INFO = reproduces ordering but not magnitude.
   - Effort: 2-3 hours, 1 agent session.
   - Functional-sensitivity note (LIZZI): Connes distance is a metric on the finite spectral triple
     (functional-INDEPENDENT). This is an independent regulator-invariant route to the SAME ratios.

V.3. Inter-sector freeze-in block [[d,w],[w*,d]] — over-constrained fit
   - What: fit {S₀, |w|} to charged-lepton masses and arg(w) to one mixing datum, then PREDICT the
           six quark ratios + CKM angles + J_CP with no further freedom.
   - Inputs: diabatic crossing data (P_exc=1.000, δt/T_L=1.25e-5); Casimir grading C₂; charged-lepton
            PDG masses; one CKM anchor.
   - Gate: new gate S99-CF-FREEZEIN-BLOCK-OVERDETERMINED. PASS = quark ratios + CKM + J_CP reproduced
           within pre-registered bands from {S₀,|w|,arg w} alone; FAIL = over-constraint breaks
           (closes the corridor cleanly); INFO = mass shape PASS but mixing FAIL (or vice versa).
   - Effort: 4-6 hours, 1 agent session.
   - Functional-sensitivity note (LIZZI): the freeze-in AMPLITUDE is fermionic-dynamics
     (functional-INDEPENDENT). S₀ is a RATIO (ε_LX-split scale / horizon κ) per the panel — both
     numerator and denominator are finite-part / fiber-acoustic quantities, NOT bosonic a₄ moments.
     This fit is regulator-invariant; a clean FAIL is decisive and scheme-independent.

V.4. Envelope over-determination — greybody κ vs transit S₀
   - What: compute the diagonal exponent two ways — greybody filter at the SONIC surface
           κ_SONIC = 0.7048 M_KK vs transit's S₀ — and test coincidence (envelope derived twice).
   - Inputs: κ_SONIC = 0.7048 M_KK (= 2π·0.112, Mach-1 crossing; NOT κ_GH=1.365, NOT a₂/a₄
            thermodynamic surfaces); ε_LX frequency offsets; S₀ from V.3.
   - Gate: new gate S99-CF-ENVELOPE-OVERDETERMINE. PASS = κ_SONIC route and S₀ route agree within
           band; FAIL = disagree; INFO = agree in order-of-magnitude only.
   - Effort: 2-3 hours, 1 agent session.
   - Functional-sensitivity note (LIZZI): κ_SONIC is a FIBER-ACOUSTIC surface (v=c_BLV Mach-1),
     functional-INDEPENDENT. The panel explicitly excludes the a₂/a₄ thermodynamic-gradient surfaces,
     which WOULD be functional-dependent — endorse this exclusion: using an a_n-gradient κ here would
     contaminate a regulator-invariant ratio with a regulator-dependent scale.

V.5. [NEW — LIZZI functional-axis gate] M₀^{sector} / m_H under zeta vs cutoff action
   - What: recompute the overall per-sector scale M₀^{sector} (and m_H) the KK threshold sets, under
           BOTH the cutoff action Tr f(D_K²/Λ²) AND the zeta action S_ζ = ζ_{D_K}(0) = a₄. Report the
           scheme-dependence of the SCALE explicitly, confirming the RATIOS (V.1-V.4) are untouched.
   - Inputs: KK-THRESHOLD-64 machinery (m_H=131.8 GeV, the |S|² fiber-embedding mode); a₄ zeta moment
            (a_4=1350.722 zeta per-branch L_max=3, from canonical/memory); cutoff f₄ moment
            (f4=6446.63942272 at X_MAX=50, f*-scheme, from memory); M_KK=7.4287e16 GeV (canonical).
   - Gate: new gate S99-CF-M0-FUNCTIONAL-SENSITIVITY. INFO-by-design (this is a functional-dependence
           characterization, not a PASS/FAIL physics gate): report Δ(M₀^{sector}) and Δ(m_H) between
           schemes; PASS-side assertion = the fermion mass RATIOS are bit-identical across schemes
           (confirming functional-independence); FAIL = ratios move (would falsify the decoupling claim).
   - Effort: 2-3 hours, 1 agent session.
   - Why this matters: this gate makes the §IV layer-separation EMPIRICAL rather than asserted. It is
     the spectral-functional-theorist's specific contribution — it pins, with numbers, exactly which
     S99 outputs are scheme-dependent (the scale) and which are scheme-independent (everything else).

V.6. S99-E1-STAGE2-VERIFY closure (panel-cited, queued)
   - What: run the Stage-2 cross-axis independent-verify of §VII.BL E1 (the Homogeneity-wall / ε_LX
           registry entry) per joint-theorem-promotion.md (two reviewers, opposite axes, no workshop
           context). NCG/spectral axis + transit/dynamics axis.
   - Inputs: registered Stage-1 §VII.BL E1 text; R_cross_yukawa_t1_t2=1.019704 (canonical, registry
            SS-VII.BL); W2 theorem text.
   - Gate: S99-E1-STAGE2-VERIFY (already cited in panel as the S99 W3 gate). PASS-AND across both
           reviewers on JOINT clauses promotes §VII.BL E1 to STAGE-3-PERMANENT; any FAIL holds at
           STAGE-1-CANDIDATE.
   - Effort: 2-3 hours, 2 agent sessions (parallel cross-reviewers).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Fermion masses = entries of D_K finite part; `∂m_f/∂f_n = 0` for all bosonic regulator moments | GEOMETRIC | FUNCTIONAL-INDEPENDENT (structural) | The regularization debate (zeta/cutoff/anomaly) does NOT touch fermion mass ratios — the cleaner half of the SM |
| 2 | Homogeneity wall (W2): left-invariance ⇒ multiplicity-scalar ⇒ democratic | GEOMETRIC | PROVEN (Level-1, regulator-invariant); ε_LX reframe gate-confirmed `S98-W3-1` PASS | Hierarchy forced onto a finite-part deformation `ε_LX`; functional-independent |
| 3 | Reality forces split-is-`\|w\|` / mixing-is-`arg(w)`; BDI→CP tie | GEOMETRIC | Axiom-forced (Sage-exact on D_F); functional-independent | One off-diagonal `w` sets μ↔τ split + CKM/PMNS + CP; CP survives *because* BDI |
| 4 | Diagonal envelope = one Casimir exponential (4 lenses); scale = KK threshold `m_H=131.8` | GEOMETRIC | Envelope shape = clean win (functional-INDEP); scale `M₀^{sector}` = functional-DEP (bosonic a₄) | Shape is regulator-invariant; ONLY the overall scale is scheme-sensitive |
| 5 | `1.889` widening: Casimir ladder `9/5=1.800` (4.7%, zero-param) vs PDG `1.8894` | GEOMETRIC | OPEN (sector-assignment-dependent); functional-INDEPENDENT | Open question is orthogonal to the functional axis — no need to repeat across schemes |
| 6 | Bosonic/fermionic layer separation along the regularization axis | GEOMETRIC | Structural (new explicit framing) | Fermion-mass program can proceed WITHOUT resolving functional-selection; genuine decoupling |

---

*Spectral-functional theorist's bottom line: the S99 panel did its generative job — it re-posed the charged-fermion corridor as "what is `ε_LX`?" rather than "why democratic?". From my axis the most useful contribution I can add is the layer verdict: the panel's entire object of study sits in the FUNCTIONAL-INDEPENDENT fermionic sector `⟨ψ, D_K ψ⟩` (mass ratios, the μ↔τ-split mechanism, mixing/CP, the widening, the W2 wall all regulator-invariant), and ONLY the overall scale `M₀^{sector}`/`m_H` reaches back into the functional-DEPENDENT bosonic action at a₄. That decoupling is the cleaner half of the Standard Model, and V.5 makes it empirical. The arrow runs `D_K finite-part eigenvalues → spectral/transit structure → emergent mass ratios → measured`; the choice of spectral functional governs the bosonic neighbours (a₀ cosmological, a₂ gravity, a₄ Higgs scale), not the fermion masses themselves.*
