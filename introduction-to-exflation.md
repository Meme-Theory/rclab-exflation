# An Introduction to Phonon-Exflation Cosmology

*The front door. Read this first — before the Atlas, the registry, or the session archive.*

**What this is.** A self-contained, plain-language on-ramp to the phonon-exflation framework: what it claims, the mental model it runs on, what it explains, what is actually *proven* versus *assumed* versus *open* versus *retracted*, and where to go next. It is an introduction, not a textbook and not a registry dump — accessible and faithful, not exhaustive.

**Who it's for.** Anyone technically literate who is *not* a specialist in noncommutative geometry or cosmology. Every term is defined on first use. Intuition comes before formalism.

**One caveat, stated up front.** Every status tag below (PROVEN / CONDITIONAL / OPEN / BROKEN / RETRACTED) is faithful to the framework's own register *as of June 2026 (session ~S114)*. The register moves. For the live state of any claim, the authorities are the Atlas (`sessions/framework/Atlas/`), the permanent-results registry (`sessions/permanent-results-registry.md`), and the `knowledge` MCP — **not** this document and not any agent's memory. Where this introduction headlines a specific number or status, it cites the register row it came from so you can re-check it.

---

## 1. The claim, in one paragraph

The universe is the **resonance spectrum of a single mathematical instrument.** Picture one richly-structured object — not a guitar string but a high-dimensional internal geometry — that can vibrate in 155,984 distinct modes. The claim is that *everything we call physics* is a harmonic of that instrument: the particles and their masses, the four forces, gravity itself, and the entire history of the cosmos are all read off the same eigenvalue spectrum. The instrument has exactly **one tuning peg**, a single real number written **τ** (tau). Turn τ, and the whole spectrum reorganizes. What cosmologists call *the expansion of the universe*, this framework calls **exflation**: not space stretching, but the internal vibrational complexity at every point *growing* as τ sweeps through a critical value. Space is not the stage on which this happens — space is itself one of the harmonics, an emergent bookkeeping of how the instrument's vibrational weight is distributed. The framework's own one-sentence summary:

> "Spacetime, matter, and forces are the harmonic classification of [the operator's] spectrum." — `Phononic-framework-hypothesis.md §1`

This is meant structurally, not poetically. Behind the metaphor is a precise eigenvalue problem on a specific finite-dimensional geometry, and most of the framework's *proven* content is exactly that: theorems about that eigenvalue problem.

---

## 2. The substrate picture — the mental model to hold

Everything downstream rests on one mental model. Build it in five steps.

### 2.1 A geometry is its spectrum (the spectral triple)

The mathematical backbone is a **spectral triple**, written `(A, H, D)` — three objects:

- **A — the algebra.** The list of things you can *measure* at a point (an algebra of operators). It encodes the internal symmetry.
- **H — the Hilbert space.** Where the *states* live (here: spinors — the mathematical objects that describe spin-½ matter).
- **D — the Dirac operator.** A first-order differential operator that carries *all the geometric and dynamical information*: distances, curvature, how things propagate.

The deep idea (due to Alain Connes) is that **a geometry and its spectrum are the same data.** You do not need to assume a pre-existing space with points and a metric; if you know the spectrum of the right operator `D`, you can *reconstruct* the geometry from it. Loosely: you can hear the shape of a drum. In this framework that reconstruction theorem is turned into a working principle — the spectrum is fundamental; the "space" is derived from it.

### 2.2 The specific instrument: D_K on Jensen-deformed SU(3)

The framework's instrument is concrete:

- The world is a **product `M⁴ × K`** — ordinary 4-dimensional spacetime `M⁴` times a small **internal fiber `K`** attached at every point. *(This product structure is an input assumption — see §6.3.)*
- The fiber is **`K = SU(3)`**, the 8-dimensional Lie group of 3×3 unitary matrices — the same symmetry group nature uses for the strong nuclear force. It was *chosen* because its representation theory reproduces the Standard Model's particle charges (and that choice is later vindicated by output, never derived from a deeper principle).
- The fiber's geometry is **Jensen-deformed**. A *Jensen deformation* is a smooth, **volume-preserving** reshaping of `SU(3)`'s metric controlled by the single parameter **τ**. "Volume-preserving" is exact and load-bearing: as τ changes, the fiber stretches along some directions and squeezes along others, but its total volume never changes (`det g(τ) = 1` to machine precision — `atlas-07`). The cavity *reshapes*; it never *shrinks or grows*.
- **`D_K`** is the Dirac operator on this internal geometry. Its **eigenvalues are the catalog of every vibrational mode the fabric can carry** — 155,984 of them (78,080 distinct) at the standard computational truncation called `L_max = 10`.

> **Intuition — the Celtic rosette.** `SU(3)`'s internal symmetry is the hexagonal "A₂ root system." Think of a rosette whose six-fold symmetry fixes the *spacing* of the allowed vibrations. Turning τ tilts the rosette: one special direction stays symmetric (it remains a continuous symmetry and becomes the weak hypercharge `U(1)_Y`), while the other seven directions acquire a "gap" — they cost energy to excite. (`Phononic-Substrate-Geometry.md`)

### 2.3 Particles are phonons of the fabric

A **phonon** is a quantum of vibration — in an ordinary crystal, a unit of sound. Here, **a particle is a phononic excitation of the fabric**: a "relay pattern" propagating through the structure, built on the eigenvalue spectrum of `D_K`. An electron, a quark, a photon — each is a specific way the fabric is ringing. "Two particles colliding at the LHC" becomes "two relay patterns overlapping at one fiber and exciting its eigenvalue spectrum." Mass, charge, and coupling strength are not separate inputs; each is a **spectral moment** — a weighted sum over `{λ_n(τ)}`.

### 2.4 Space is emergent, not fundamental

This is the step most worth internalizing, because trained intuition fights it. **The fabric is not sitting inside space.** Space is an emergent description of how the fabric's spectral weight distributes itself. Concretely, the 4-dimensional metric of gravity is *literally* one term in the small-time expansion of `D_K` (the `a_2` coefficient, §3), and Newton's gravitational constant is the *second moment* of the spectrum. Gravity is not a law imposed on the fabric; it is a consequence of the fabric's spectrum.

> **Intuition — the film and the playback rate.** "The substrate IS the film, not a thing *in* the film. The speed of light `c` is the playback frame rate — it limits what plays *on* the film. Editing the film — splicing frames, transitioning the spectral triple — is not bounded by the playback speed, because editing is not playback." (`Phononic-C-Causality.md`)

That metaphor resolves a question that otherwise looks paradoxical: how can cosmic processes "outrun light"? They don't. The speed of light bounds **propagation across the substrate** (photons, particles, gravitational waves — all capped by the group velocity `c`). The **dynamics of the substrate itself** — the fold transit, the retuning of `D_K`, the sweep of τ — are *not* propagation through space; they are changes *of* the operator that generates space, and they answer to a different clock (the spectral-action gradient, §3). This split is a proven theorem, the **Spectral-Moment Decoupling Theorem** (`atlas-07`; gate `SPECTRAL-DECOUPLING-CERT-75`): propagation lives in one heat-kernel moment (`a_2`, gravity), substrate dynamics in another (`a_0`, vacuum), and the two are mathematically incommensurable.

### 2.5 The "IS space, not IN space" rule

The framework enforces a discipline on itself, worth adopting as you read: **every explanation flows outward from the substrate.**

```
   D_K eigenvalues  →  spectral-action moments  →  emergent field equations  →  observed physics
     (fundamental)         (derived)                  (emergent)                  (measured)
```

If you ever find an explanation running the other way — "Einstein's equations govern the fabric," "particles are created *in* curved spacetime," "fields live *on* the compact space `K`" — it has inverted the logic. The Einstein equations are *generated by* the `a_2` moment; particles *are* the reorganization of the spectrum, not things produced inside a container; nothing lives "on" `K` because `K` *is* the spectral content. (`phononic-framing.md`, "IS Space, Not IN Space")

---

## 3. One operator, one dial: the master equation

The entire framework collapses to a single expression — the "capstone equation" (`phonic-exflation-equation.md §1`):

$$\mathcal{S}\big[D_K(\tau),\,f,\,\Lambda\big] \;=\; \mathrm{Tr}\,f\!\left(\frac{D_K(\tau)^2}{\Lambda^2}\right) \;+\; \big\langle\, J\tilde\psi \,\big|\, D_K(\tau) \,\big|\, \tilde\psi \,\big\rangle$$

Read in plain language:

- **First term — `Tr f(D_K²/Λ²)`, the spectral action.** Take the operator `D_K`, square it, normalize by a cutoff energy scale `Λ`, apply a smooth weight function `f` that gently switches off the highest modes, and **sum over the whole spectrum** (that is what `Tr`, the trace, does). This single number is the action — the quantity nature extremizes — for the substrate itself.
- **Second term — `⟨Jψ|D_K|ψ⟩`, the matter coupling.** `ψ` is a fermion (a matter field) living in the positive-chirality half of the Hilbert space — a restriction that, non-trivially, selects *one* generation of matter and avoids doubling it. `J` is the charge-conjugation operator. This term measures how the Dirac operator couples to matter.

**Why a single object can carry cosmology *and* particles *and* gravity.** This is not a coincidence to be marveled at; it is structural. The spectral action's small-time (heat-kernel) expansion produces a fixed ladder of terms called **Seeley-DeWitt coefficients** `a_0, a_2, a_4, …`, each a curvature polynomial of one higher degree:

| Coefficient | Curvature degree | What it physically **is** | Register |
|:--|:--|:--|:--|
| **`a_0`** | constant (∝ volume) | **Vacuum energy / the cosmological-constant term** | τ-independent (volume preserved) |
| **`a_2`** | ∝ scalar curvature `R` | **The Einstein–Hilbert action — i.e. gravity.** Newton's `G_N` is read off here | monotone in τ; PROVEN |
| **`a_4`** | ∝ `R² + F²` | **Yang–Mills + the Higgs quartic — i.e. the Standard Model matter sector** | monotone in τ; PROVEN |

The framework does not *bolt together* three theories. It writes down one operator and **expands it**; the cosmological constant, Einstein's gravity, and the Standard Model fall out as the zeroth, second, and fourth *moments* of the same spectrum. The gauge group `U(1) × SU(2) × SU(3)` emerges as the symmetries of the algebra `A = ℂ ⊕ ℍ ⊕ M₃(ℂ)`; the Higgs boson is an internal fluctuation of `D_K` itself, not a separately-posited field.

That these three layers are genuinely *independent* physics (not redundant) is itself a theorem — the **Spectral-Moment Decoupling Theorem** (`phonic-exflation-equation.md §4.2`): the three coefficients are algebraically independent everywhere except at the single genesis point τ = 0, where they momentarily degenerate. The instant exflation begins (τ > 0), gravity, vacuum energy, and matter are distinct.

**The dial.** Because every observable is some moment of `D_K(τ)`, and `D_K` depends only on τ, the causal chain is:

```
  τ  →  metric g(τ)  →  D_K(τ)  →  spectral action  →  {a_0, a_2, a_4}  →  masses, couplings, cosmology
```

One real number in; all of physics out. *(With one crucial exception — the overall dimensional scale — covered in §6.3 and §7.1.)*

---

## 4. Exflation, not inflation

Standard cosmology (ΛCDM) describes a stage — space — that inflates, then expands, dotted with separately-postulated ingredients (an inflaton field, dark matter particles, dark energy). The substrate picture re-describes every one of these as something the fabric *does*. The translation is exact and the framework keeps it as a working table (`phononic-framing.md`):

| ΛCDM / inflation language | Substrate (phonon-exflation) language |
|:--|:--|
| "Space expands" | Spectral complexity grows *inside each point* — the eigenvalue spectrum reorganizes |
| "Big Bang singularity" | A first-order phase transition at the **fold** (τ = 0.190) — no singularity |
| "Slow-roll inflation" | A **supersonic transit** (Mach ≈ 14) through the fold — impulsive, not gradual |
| "Inflaton field" | The Jensen deformation **τ**, driven by the spectral-action gradient `dS/dτ ≈ +58,700` |
| "Reheating" | **GGE relic formation** — particle pairs shaken loose as the fabric snaps through the fold |
| "Horizon problem solved by inflation" | An **acoustic white hole** — pre- and post-transit regions causally disconnected by supersonic flow |
| "Vacuum energy / cosmological constant" | The spectral-action zeroth moment `a_0` — a *different* moment than gravity (`a_2`) |
| "Dark matter particle" | A **Leggett-channel GGE quasiparticle** — a phase mode, CPT-neutral, non-annihilating |
| "Dark energy / quintessence" | An **effacement residual** — a 0.03% leakage through an impedance mismatch (`Γ = 0.99970`) |
| "Density perturbations" | The interference pattern of post-transit acoustic excitations |
| "Particle collision" | Two relay patterns overlapping at one fiber, exciting its spectrum |

So the birth of the universe is not a singularity and not a slow roll. It is a **fast phase transition**, told in three acts (`framework-chaotic-instantons.md`, `framework-parametric-amplification.md`, `phonic-exflation-equation.md §5`):

1. **A cold, unstable start (τ = 0).** The fully symmetric round geometry is an unstable *maximum*, not a stable bottom — like a pencil balanced on its tip. A cubic term in the energy makes the first move *first-order* and inevitable (this is the PROVEN *Perturbative Exhaustion Theorem*). There is no need for a "bang"; the configuration simply cannot stay put.
2. **A supersonic plunge through the fold (τ = 0.190).** The single tuning parameter accelerates through a special point called the **van Hove fold** — a value where the *density of vibrational states* spikes to a cusp. The plunge is **supersonic** (faster than the fabric's own sound speeds) and **impulsive** (it crosses far faster than the internal pairing can keep up). Two metrics emerge here: a fast "geometric" one for gravitons and a ~229× slower "acoustic" one for phonons, which is why the transit is supersonic against the acoustic cone. Because the crossing outruns the local sound speed, the regions before and after are causally sealed off — an **acoustic white hole**, which is the substrate's version of "why is the sky so uniform" (the horizon problem).
3. **A frozen relic (τ ≈ 0.22 onward).** The sudden crossing shakes loose roughly 60 quasiparticle pairs — the substrate's analog of reheating — leaving a structured quantum state called a **Generalized Gibbs Ensemble (GGE) relic.** This relic is what later shows up as the dark sector and the seeds of structure.

> **Honesty note on the relic (a corrected claim).** An early reading (S38) held that this relic is *permanent* because the post-fold system is exactly integrable. That specific claim is **BROKEN / RETRACTED** (`atlas-09`, `phonic-exflation-equation.md §5`). What survives — and is compute-certified — is weaker but cleaner: the relic is **frozen by sheer speed** (a "diabatic transit-freeze"; the crossing is thousands of times faster than the relic could relax: `R_therm = 5252`, entanglement entropy `S_ent = 0`). It is frozen because the hammer falls too fast, not because it is eternally protected. This is the framework correcting itself, and it is the right way to read the relic.

---

## 5. What the framework sets out to explain

| Domain | Substrate account | Current status (see §6–§7) |
|:--|:--|:--|
| **Cosmogenesis** | First-order transit through the van Hove fold; acoustic white hole; no singularity | Mechanism mathematically rigorous; cosmological closure OPEN (§7.1) |
| **CMB tilt `n_s`** | Acoustic signature of the relic, from gauge-invariant spectral geometry | Value committed at `n_s ≈ 0.959`; SCHEME-DEPENDENT; live-watch in tension (§6.2) |
| **Structure** | Interference pattern of post-transit acoustic excitations, self-organized through the `a_2` (gravity) channel | Follows from the relic; growth-rate `f·σ₈` is now the #1 near-term test (§7.2) |
| **Particle masses** | Eigenvalues / spectral moments of `D_K` at the fold; Higgs = transverse fiber oscillation | Higgs `m_H ≈ 131.8 GeV` (≈5% high), route-pinned; SM charges exact (§6.1) |
| **Dark matter** | A Leggett-channel GGE quasiparticle — CPT-neutral, non-annihilating, gap-massed | Relic density `Ω_DM h² ≈ 0.120` matches to 0.6% (§6.2); channel partition more exploratory |
| **Dark energy** | An "effacement residual" / Volovik tracking vacuum — the diluting vacuum energy | Present-epoch density matches to ~1% (Volovik tracking); early-universe arm OPEN (§7.1) |

---

## 6. What is actually established

Three categories, three honesty levels. The framework's credibility rests on keeping them distinct.

### 6.1 PROVEN — structural theorems (machine precision)

These are mathematical facts about the construction, verified to ~10⁻¹³ or better, many re-checked independently 8+ times. They do **not** depend on cosmology being right; they are true of the instrument regardless. (Source: `atlas-07-permanent-results.md`; `sessions/permanent-results-registry.md`.)

| Result | Plain statement | Status |
|:--|:--|:--|
| **KO-dimension = 6** | A topological invariant of the spectral triple equals 6, which fixes the matter symmetry class (BDI) and forces *one* fermion generation | PERMANENT |
| **Standard Model quantum numbers** | The exact electric charges, colors, and isospins of one SM generation drop out of the 16-component spinor — no charges put in by hand | PERMANENT |
| **`[J, D_K] = 0` (CPT)** | Charge-conjugation symmetry is hard-wired exactly (checked at ~80,000 eigenvalue pairs) | PERMANENT |
| **`g₁/g₂ = e^{−2τ}`** | The ratio of two gauge couplings is fixed by the geometry's deformation, not tuned | PERMANENT |
| **Volume-preserving deformation** | `det g(τ) = 1` exactly ⇒ Newton's `G_N` has zero τ-dependence | PERMANENT |
| **`D_K` block-diagonal** | The operator splits into independent blocks (three independent proofs); holds for *any* compact semisimple Lie group | PERMANENT |
| **Symmetry class BDI** | The substrate sits in the Altland–Zirnbauer BDI class (`T² = +1`); the spectral gap stays open | PERMANENT |
| **Algebra uniqueness** | `A = ℂ ⊕ ℍ ⊕ M₃(ℂ)` is the *unique* finite real algebra (dim ≤ 50) meeting the axioms — 1 of 3,907 candidates | PERMANENT (S88) |
| **Spectral-action monotonicity** | The action increases monotonically in τ for *every* smooth cutoff, every Λ — so τ *transits* rather than settling into a well | PERMANENT |
| **Cooper instability at the fold** | At the van Hove fold, any attractive coupling `g > 0` triggers pairing (a 1-D BCS theorem, three independent proofs) | PERMANENT |
| **`α_s = n_s² − 1`** | An exact algebraic identity linking the running of the spectral tilt to the tilt itself (five independent proofs) | PERMANENT (see §7.2 for its observational tension) |

There are well over a hundred such landings. The point is not the count — *a count is not an argument* — but the *character*: a large, internally-consistent body of structural mathematics that stands on its own even if the cosmology were wrong.

### 6.2 The zero-free-parameter observational matches

These are the framework's wagers: numbers that come out of pure geometry with **no tuned parameters**, compared against data. A match here carries real evidential weight precisely *because* there was no dial to turn. But each must be reported with its honest status — and several carry tensions or scheme-dependence.

| Observable | Framework value | Observed | Honest status |
|:--|:--|:--|:--|
| **Higgs mass `m_H`** | **131.8 GeV** (KK-threshold; `m_H_FW_KK_threshold`) | 125.1 GeV | Within +5.36% (= 67/1251 exact) from zero particle-physics parameters; route-pinned (S102). PINNED-but-CONDITIONAL on the external scale `M_KK` |
| **Dark-matter density `Ω_DM h²`** | **0.120** (Leggett channel) | 0.1207 (Planck) | Match to **0.6%**, zero free parameters (`LEGGETT-MOMENT-70`). LIVE |
| **Scalar tilt `n_s`** | **0.959** (`√x` cutoff, committed) | 0.965 (Planck) / 0.971–0.974 (ACT, P-ACT) | CONDITIONAL — SCHEME-DEPENDENT (the value's *sign* depends on the regulator; `√x` selected at high confidence). Live-watch currently drifting *against* the framework (P-ACT ~5σ high) |
| **Dark-energy `w₀`** | **−0.918** (Volovik partition) | −0.75 ± 0.06 (DESI DR2) | CONDITIONAL, ~2.1σ. Decisive test: DESI DR3 (2027) |
| **Tensor-to-scalar `r`** | **0.0075–0.012** (dual pathway) | < 0.03 (current bound) | PASS / LIVE — decisive discriminator at LiteBIRD (2030) |
| **Hubble constant `H₀`** | **67.40 km/s/Mpc** (G_N-ratio channel) | 67–73 (method-dependent) | Re-pinned S101; a measurement > 72 at >2σ would challenge it |

### 6.3 Assumed, not proven — say it plainly

The framework is explicit that its *starting geometry* is an **assumption**, never derived from a deeper principle (`atlas-04-assumptions.md`, the ASSUMED rows):

- The **`M⁴ × K` product structure** is an input ansatz (standard Kaluza–Klein starting point).
- **`K = SU(3)` specifically** was *chosen* to reproduce SM charges — vindicated by output, not derived.
- The **Jensen one-parameter deformation family** is the simplest volume-preserving choice; the full deformation space is 28-dimensional and the Jensen line is a confined ridge within it, not a forced path.
- The **volume-preserving constraint** and **left-invariant metric** are imposed, not derived.

None of this is hidden. A reader should hold the framework to its honest shape: *given* this geometric setup, an enormous amount follows rigorously; the setup itself is a well-motivated choice awaiting a first-principles reason.

---

## 7. What is open, and what would falsify it

A framework is only as credible as its statement of its own boundaries. Here are the real ones.

### 7.1 The big open problem: the `a(t)` gap

**The single most important gap.** The framework has **no derived cosmic scale factor `a(t)`** — no first-principles formula for the absolute, seconds-valued expansion history. This is tracked as open question **Q13** (`atlas-08`) and is the gated weakness of the whole cosmological stratum.

It is worth stating exactly what *is* and *is not* missing, because the framework has sharpened this considerably (sessions S111–S112):

- **What the substrate determines (PROVEN, from zero continuous parameters):** the *conformal class* of the emergent cosmology and **every dimensionless dynamical shape** — every ratio, every ordering, the spectral tilt, the late-time growth exponent (`a(t) ∝ t^{2/3}`, the dust attractor). The τ-clock is proven well-posed (the de Sitter relation `Λ = 3H²` closes exactly).
- **What it does NOT determine (now a PERMANENT boundary):** the one **dimensional normalization** — the overall scale. The substrate measures everything in units of its own cutoff `M_KK`, and a system that measures everything in `M_KK` *cannot fix `M_KK` from within* (a self-reference no-go, FAIL-confirmed S112). So `M_KK ≈ 7.43×10¹⁶ GeV` is imported from observation, once, and is a **permanent external-import boundary** — not a bug to be fixed later.

The honest reading the capstone insists on: the substrate is fundamental, and *space does not expand — spectral complexity grows inside each point*; `H(t)` is the **readout** of that reorganization, not an external clock. A substrate theory is *expected* not to contain a fundamental Friedmann equation (this is Jacobson's 1995 "Einstein equations as equations of state," made microscopic). But the framework still owes a *derived effective* Friedmann map for late-time observables, and that back-reaction closure — promoting relic energy density into a global expansion rate — is the part still missing. Net status of §6.3: **HALF-CLOSED** (all dimensionless shapes fixed) / **HALF-OPEN-PERMANENT** (the dimensional scale is an external import; `H₀`-tension relief is capped at ~6%).

### 7.2 Other open fronts

- **Cosmological constant, early-universe arm.** The *present-epoch* vacuum density is reproduced to ~1% by the Volovik tracking-vacuum mechanism (`ρ_vac/ρ_obs = 1.032`, `DILUTION-CC-66` PASS) — the famous 10¹²⁰ discrepancy is reframed as the expansion history itself. But the **Big-Bang-nucleosynthesis-epoch** arm is OPEN (over-production by ~2×; Q29).
- **The `α_s` tension.** The identity `α_s = n_s² − 1` is PERMANENT, but it puts the framework's running of the tilt in tension with current CMB data at the naive pivot. The resolution on the table is *scale-and-channel separation*: the substrate carries two distinct `α_s` observables (a substrate-distance running of −0.086 deep inside the internal Brillouin zone, and a ≈0 running at the CMB pivot), and which one a detector sees depends on a transport degree. This converts a tension into a **live discriminator** for CMB-S4 (2030) / CMB-HD (2035), not a clean current pass.
- **`n_s` scheme-dependence.** Because the tilt's sign flips between regulator choices, the prediction is *conditional* on the `√x` cutoff being canonical (selected at 15–37σ Bayesian evidence, but the functional-selection question is not formally closed).
- **`K_pivot` scale mapping.** The single largest *observational* load-bearing gap: no physical mechanism yet places the CMB pivot scale where the cleanest `n_s` would land (`atlas-04` C2, BROKEN-with-live-pathway).
- **Scalar amplitude `A_s`.** A structural over-production (~1.6× after recent reconciliation) that is a genuine open tension, not yet resolved at the substrate level.

### 7.3 What would falsify it — the live test surface

The framework is set up to be killed by data. Near-term decisive tests (`atlas-08`, `falsifier-master-inventory.md`):

- **DESI DR3 (2027) — nearest decisive test.** `w₀, w_a`. The framework predicts `w₀ ≈ −0.918` and **`w_a = 0` exactly** (a triple-locked structural prediction). Current data already pull `w_a` ~3.4σ away — *the data are moving against the framework here*, and DR3 will sharpen it either way.
- **LiteBIRD (2030).** The tensor sector: two internal pathways predict `r ≈ 0.0075` vs `0.012`, a ~4σ internal discriminator LiteBIRD can resolve.
- **CMB-S4 / CMB-HD (2030 / 2035).** The `α_s` substrate-sensitivity channel — a multi-σ discriminator if the two-channel reading is right.
- **Large-scale-structure growth `f·σ₈` — now the #1 *non-CMB* falsifier.** The gravitational-wave flagship that once lived here migrated to LSS (see below); the structure-growth rate is the cleanest near-term substrate test.
- **Laboratory analogs (~2031).** Because the substrate is a condensed-matter-like system, it makes *lab* predictions: specific NMR/spectroscopy signatures in superfluid ³He-B, ³He-A, FeSe, and ¹⁷³Yb optical lattices. A clean null where the framework predicts a signal (or vice versa) would falsify the inheritance structure.

### 7.4 The self-correction record is a feature

The framework has logged **46+ retractions and corrections** (`atlas-09`). That ledger is a strength, not an embarrassment — it is what distinguishes a research program from an apologetic. The flagship example:

> **The gravitational-wave prediction was retired.** For a time the framework headlined a stochastic GW signal for LISA. On audit, the domain-wall contribution was found to be **exactly zero**, and the acoustic peak frequency evaporated to ~10⁴⁰ Hz — *detector-sterile*, far above any instrument (`atlas-09` Item 49). The GW flagship was **RETRACTED**. Crucially, the *falsifier did not vanish* — it **relocated** to large-scale structure (`f·σ₈`), the correct instrument. A prediction that survives only by being unfalsifiable is worthless; a prediction honestly moved to where it can actually be tested is the opposite.

Other corrected claims of note: the GGE-permanence retraction (§4); the `B_1D = 20.9` reversal (an apparent strong positive that became a decisive negative on re-examination against raw BAO data); and an `H₀ = 68.8` reading withdrawn over a double-counting bug. The pattern — apparent wins surrendered when the math demanded it — is the methodology working.

---

## 8. How to navigate the rest of the corpus

When you want to go deeper, here is the map. The **Atlas** (`sessions/framework/Atlas/`) is the curated structured state; the **registry** is the permanent ledger; the **capstone** is the one-equation synthesis.

| If you want… | Go to |
|:--|:--|
| The index and reading guide | `sessions/framework/Atlas/atlas-00-index.md` |
| The whole story as one equation | `sessions/framework/phonic-exflation-equation.md` (note its §0 status discipline) |
| **What is proven** | `atlas-07-permanent-results.md` + `sessions/permanent-results-registry.md` |
| **What is assumed vs proven** | `atlas-04-assumptions.md` |
| **What is open** | `atlas-08-open-questions.md` |
| **What was retracted** (the honesty leg) | `atlas-09-retractions.md` |
| Closed corridors vs open directions | `atlas-05-walls-doors-windows.md` |
| The 60 load-bearing equations | `atlas-03-equation-flow.md` |
| How the breakthroughs connect | `atlas-10-breakthrough-genealogy.md` |
| The core conceptual narrative | `sessions/framework/Phononic-framework-hypothesis.md` and the other `Phononic-*.md` |
| The substrate-vs-ΛCDM translation discipline | `.claude/rules/phononic-framing.md` |
| A variable glossary | `sessions/framework/MathVariables.md` |
| What to compute next, and why | `sessions/evoi-framework.md` (the EVOI priority table) |
| Live, queryable state of any claim | the `knowledge` MCP — `search_knowledge`, `get_constant`, `trace_entity` |

---

## In one honest summary

The phonon-exflation framework is **one Dirac operator on a deformed `SU(3)`, dialed by one parameter τ**, from which the Standard Model's charges, the structure of gravity, and a sketch of cosmic history all emerge as moments of a single spectrum. Its assets are real and unusual: a large body of **machine-precision structural theorems** that stand on their own, and a handful of **zero-free-parameter observational matches** (dark-matter density to 0.6%; the Higgs mass to ~5%; a present-day vacuum density to ~1%). Its boundaries are equally real and stated without spin: the **starting geometry is assumed**, several CMB predictions are **scheme-dependent** or **in live tension with data**, and there is a **permanent boundary** — the absolute energy scale `M_KK` must be imported from observation, because a substrate that measures everything in its own units cannot weigh itself.

It is a bottom-up emergence program, not a finished theory of everything. Read it as such: take the proven mathematics at full weight, hold the cosmological claims at exactly the confidence the register assigns them, and watch the near-term tests — DESI DR3, LiteBIRD, CMB-S4, and the structure-growth rate — which will decide its fate within the decade.

---

*Document status: introductory synthesis, faithful to the register as of June 2026 (~S114). For any live value or status, query the Atlas, the permanent-results registry, and the `knowledge` MCP — those are authoritative; this front door is not.*
