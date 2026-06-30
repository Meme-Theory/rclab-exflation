# An Introduction to Phonon-Exflation Cosmology — Advanced

*The technical sibling of `introduction-to-exflation.md`. That document is the conceptual on-ramp — the mental model, the honesty discipline, the plain-language translation table. This one assumes it and goes to the formalism: the actual spectral triple, the meaty cosmology, and the pre-registered predictions with their real numbers and gates.*

**Who it's for.** Working physicists and mathematicians. It assumes fluency in noncommutative geometry (spectral triples, Connes' axioms, KO-dimension, the spectral action), QFT (heat-kernel/Seeley–DeWitt expansion, regularization schemes, anomalies), GR/cosmology (FRW, the inflationary observables `n_s/r/α_s`, the cosmological-constant problem), and non-equilibrium field theory (Bogoliubov transformations, Kibble–Zurek, the GGE). Full notation throughout. Key equations are numbered `(N)` for in-document reference; framework equations carry their atlas label `E#` (`atlas-03-equation-flow.md`) and their canonical-constant or gate provenance where headlined.

**The one caveat, stated up front (identical discipline to the basic intro).** Every status tag below — **PROVEN / CONDITIONAL / OPEN / BROKEN / RETRACTED** — is faithful to the framework's own register *as of June 2026 (session ~S114)*. The register moves. The authorities are the Atlas (`sessions/framework/Atlas/`), the permanent-results registry (`sessions/permanent-results-registry.md`), the living capstone (`sessions/framework/phonic-exflation-equation.md`), and the `knowledge` MCP — **not** this document and not any agent's memory. Where a number or status is headlined, its register row is cited so it can be re-checked. No section narrates a claim above its register status; the open-problems (§6) and the down-tags flagged throughout are load-bearing, not disclaimers.

**Two reading conventions, set once (from the capstone §0 preamble — non-negotiable).**

1. **Substrate-first / IS-not-IN** (`.claude/rules/phononic-framing.md`). Every arrow runs

   $$D_K\text{ eigenvalues} \;\longrightarrow\; \text{spectral-action moments }a_0,a_2,a_4 \;\longrightarrow\; \text{emergent field equations / FRW} \;\longrightarrow\; \text{measurement},$$

   never the reverse. Space is not a container the equation sits in; **space is what the equation's `a₂` moment looks like.** Invert the arrow — "Einstein's equations govern the fabric," "fields on the compact space `K`" — and every layer silently reverts to the container picture that manufactures the cosmological-constant catastrophe.

2. **Two `a_n` objects, never conflated** (capstone §8.2). The **Gilkey local-curvature coefficient** `a_n^{SD}` (regulator-free, exact curvature-degree story; used for layer *identity*) and the **zeta-regulated spectral moment** `a_n^{ζ} = ζ_{D_K}((d-n)/2)` (the canonical-constant pins; used for *numerics*) are different functionals — they differ by ~3–4 orders of magnitude and are not rival measurements of one quantity. Every numeric carries its regulator tag (`.claude/rules/regulator-pin-discipline.md`).

---

## 1. The spectral triple `(A_K, H_K, D_K)`

The framework is one real, even spectral triple on an internal manifold, dialed by one modulus. Everything downstream — gauge group, gravity, matter, cosmic history — is a spectral functional of it.

### 1.1 The data

$$
\mathcal{A}_K=\mathbb{C}\oplus\mathbb{H}\oplus M_3(\mathbb{C}),\qquad
\mathcal{H}_K=L^2(S_{g_\tau})\otimes\mathbb{C}^{16},\qquad
D_K(\tau)=\sum_{a=0}^{7}\rho(e_a)\otimes\gamma_a+\mathbb{I}\otimes\Omega_{LC}(\tau).
\tag{1}
$$

- **The algebra** `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` (real dimensions `1+4+9`, `K₀ = ℤ³`). Its unimodular unitaries are `SU(A_K) = U(1)×SU(2)×SU(3)` — the Standard Model gauge group is *not posited*; it is the unitary group of the algebra. The choice is not ad hoc: `A_K` is the **unique** finite real `★`-algebra of real dimension `≤ 50` satisfying the NCG axioms {KO-dim 6, first-order, orientability, Poincaré duality on `K₀`, SM hypercharge} — **1 of 3,907 candidates** (Birkhoff/Frobenius-rescue uniqueness, **STAGE-3-PERMANENT**, S88; `atlas-07`, `rel_err = 1.2×10⁻¹⁵`).
- **The Hilbert space** `H_K = L²(S_{g_τ}) ⊗ ℂ¹⁶`. The `ℂ¹⁶` is the spinor fiber `2^{d/2}` for the `d = 8` internal manifold; `A_K` acts left, the opposite algebra `A_K^o = J A_K^* J^{-1}` acts right (the bimodule). The chirality-`+1` subspace `H_K⁺ = {ξ : γ_9 ξ = ξ}` carries **one** Standard-Model generation (see §1.3).
- **The Dirac operator** `D_K(τ)`: `ρ(e_a)` represents the orthonormal frame of `(SU(3), g_τ)`, the `γ_a` are the `16×16` Clifford generators of `Cl(ℝ⁸)` (`{γ_a, γ_b} = 2δ_{ab}`), and `Ω_LC(τ) = ¼ Γ^a_{bc}γ_bγ_c` is the Levi-Civita spin connection — the **only** `τ`-dependent piece. This is the **framework's central departure** from the Chamseddine–Connes–Marcolli (CCM) construction: the internal factor is a *manifold* `SU(3)`, and `D_K` **is** the finite Dirac operator `D_F`. The Higgs is an inner fluctuation of `D_K` *itself*, not a separate commuting `D_F` (Baptista Paper 18, eq. 7.5; capstone §1.1) — the product-geometry reflex "`[D_K, a_F] = 0`, so the Higgs is a different operator" is a documented recurring error.

### 1.2 Connes' axioms — what holds, and the one bounded caveat

| Axiom | Statement here | Status |
|:--|:--|:--|
| **KO-dimension 6 mod 8** (E9) | `(ε, ε′, ε″) = (+1, +1, −1)`; AZ symmetry class **BDI** (`T² = +1`) | `<10⁻¹⁵`, 10 checks (S7–S8); PERMANENT |
| **CPT commutant** (E8) | `[J, D_K(τ)] = 0 ∀τ`; hardwires `λ ↔ −λ`, forces `η`-invariant `= 0` | 79,968 pairs at machine-ε; PERMANENT |
| **SM quantum numbers** (E10) | `Ψ₊ = (3,2,⅙)⊕(3̄,1,−⅔)⊕(3̄,1,⅓)⊕(1,2,−½)⊕(1,1,1)⊕(1,1,0)`, dim 16 | exact branching (S7); PERMANENT |
| **First-order / orientability / Poincaré duality** | `[[D_K, a], b°] = 0`; grading `γ_9` (`γ_9² = 1`); Chern character a Fredholm-module iso on `K₀` | hold on the internal triple `K` |

The honest caveat (capstone §1.3.4): the *product* triple `M⁴ × SU(3) × F_SM` carries a **permanent KO mismatch** — product KO-dim `= 4` vs finite KO-dim `= 6`. The bosonic action is unaffected; the fermionic sector requires the Pfaffian/`H_K⁺` restriction. This mismatch does *constructive* work: KO-dim 6 (`Jγ = −γJ`) is exactly the condition making the fermionic bilinear `A_D` antisymmetric, so the Pfaffian measure `∫ Dψ̃ \, e^{-⟨J\tilde\psi|D_K|\tilde\psi⟩} = \mathrm{Pf}(A_D)` is well-defined and `Pf = √det` is the path-integral statement of "one generation, not four" (`Pf` real, `Z₂ = +1` across all `τ`; gates T3-S30A/S35). The role is structurally the same as "why `D = 10`" in the superstring — a consistency condition the construction requires, not a defect.

### 1.3 What is and is *not* claimed about matter content

KO-dim 6 forces **one** generation by killing the fermion-doubling that KO-dim 0/4 would produce. It does **not** produce three. *(Down-tag flagged: a source digest read the `H_K` bimodule multiplicity as "forces three generations exactly" — this conflicts with the curated capstone §1.3.3, which is authoritative: `Ψ₊ = ℂ¹⁶` is one generation and **family replication is OPEN**, frontier #7 of §6.)* What the triple *does* fix exactly is the **charge content** of that one generation — the hypercharges, colors, and isospins drop out of the `16`-spinor with nothing put in by hand.

### 1.4 The Jensen deformation — the single modulus

The internal geometry is `SU(3)` with a left-invariant metric. The most general `Ad\,U(2)`-invariant inner product on `su(3) = u(1) ⊕ su(2) ⊕ ℂ²` carries three block scales. Two structural impositions collapse them to one:

1. **Volume preservation** (`det g_τ = const`, G6) — removes the breathing/dilaton mode.
2. **The Jensen direction** — the remaining shape is restricted to the *unique unstable transverse-traceless eigendirection* of the bi-invariant Einstein metric (Jensen's second homogeneous Einstein metric on `SU(3)`).

Exponentiating along that one direction gives the Jensen metric (E1):

$$
g_\tau = 3\cdot\mathrm{diag}\big(\underbrace{e^{2\tau}}_{u(1)},\ \underbrace{e^{-2\tau},e^{-2\tau},e^{-2\tau}}_{su(2)},\ \underbrace{e^{\tau},e^{\tau},e^{\tau},e^{\tau}}_{\mathbb{C}^2}\big).
\tag{2}
$$

Volume preservation is exact and immediate from the **exponent ledger** `2 − 6 + 4 = 0`, so `det g_τ = 3⁸ = 6561` for all `τ` (Sage-verified). This is a *transverse-traceless* deformation (`tr\,h_J = 0`), a pure shear — **not** a conformal rescaling — which is why Newton's `G_N` carries **zero** `τ`-dependence (the volume-preserving shear leaves the vacuum compressibility, hence `1/G`, invariant; capstone §2.1). The Jensen line is one ray in a **28-dimensional** moduli space of left-invariant metrics; off-Jensen Hessian analysis (S76 W2-J) finds the physical trajectories *ridge-confined* to the Jensen line, not free in the landscape. After the two impositions the entire spectral action depends on the **single real number** `τ ∈ [0, ∞)`.

The internal scalar curvature is closed-form rational (E3):

$$
R_K(\tau) = -\tfrac14 e^{-4\tau} + 2 e^{-\tau} - \tfrac14 + \tfrac12 e^{2\tau},
\qquad R_K(0) = 2,\quad R_K(0.190) = 2.018,
\tag{3}
$$

monotonically increasing for `τ ≥ 0` (147/147 Riemann-tensor checks at machine-ε, S20a), with the Lichnerowicz bound `λ² ≥ R_K/4 ≥ ½ > 0` keeping the spectral gap open at every `τ` (E5) — the reason `η(s) = 0` and the BDI gap never closes.

### 1.5 Peter–Weyl decomposition and the spectrum

By Peter–Weyl and Schur, `D_K` is **block-diagonal** in the `SU(3)` irreps `(p,q)`:

$$
\langle (p,q), n \,|\, D_K \,|\, (p',q'), m \rangle = 0 \quad\text{for } (p,q) \neq (p',q'),
\tag{4}
$$

exact to `8.4×10⁻¹⁵` and — by three independent proofs — true for **any** left-invariant metric on **any** compact semisimple Lie group (E6, S22b). This block-diagonality is what protects the SM quantum numbers from inter-sector contamination. At the canonical truncation `L_max = 10` (`max(p,q) ≤ 10`) the spectrum is **155,984 eigenvalues counted with multiplicity, 78,080 distinct** (the cache stores the unique set). The bottom-20 eigenvalues are **`L_max`-saturated** from `L_max = 10` by a Friedrich–Bär bound (`η_FB = 0.547 > 0.40`, E39, S87): low-frequency/CMB-scale physics does not move when `L_max` is lifted, so the truncation is physical at the scales that matter.

At the operating point `τ_fold = 0.190`, the low spectrum organizes into three bands whose BCS pairing weights are fixed by `U(2)` representation theory (a selection-rule structure with five independent "traps"):

| Band | modes | role | pairing weight | gap `2Δ` (`M_KK`) |
|:--|:--|:--|:--|:--|
| **B1** acoustic singlet | 1 | Goldstone-like, linear dispersion near `k=0` | `V(B1,B1)=0` exactly (selection rule) | 0.744 |
| **B2** flat band | 4 | `v_g ≈ 0` at the fold; the van Hove channel | `V(B2,B2)=0.256` → **90.7%** of condensation | 1.464 |
| **B3** optical | 3 | gapped at `k=0`, dispersive | `V(B3,B3)=0.003` → 1.0% | 0.168 |

The operating point itself is not turned by hand: `τ_fold = 0.190` (`tau_fold`, S12/S42, gate `CONST-FREEZE-42`) is pinned as the **unique non-stationary van Hove cusp** of the B2 density of states (uniqueness theorem, **PERMANENT**, S85 W10-3). A subtlety the register is careful about: the *located* cusp-crossing functional is `τ_cross = 0.191038` (`tau_cross_van_hove`, S114, registry §VII-B.TAU-CROSS-VAN-HOVE), `L_max`-invariant and regulator-robust; the `0.5464%` offset from the rational anchor `τ_fold = 19/100` is the *round-number-freeze-vs-located-feature* gap between two real substrate-IS objects at different layers, **not** a "value still uncertain." The rational `19/100` is load-bearing on the derived-ratio chain `S₀ = τ_fold / T_acoustic = 95/56`; `τ_cross` is a separately registered observable. Neither replaces the other.

---

## 2. The spectral action

### 2.1 The master equation

Reality is one self-adjoint operator and one universal functional of it (capstone §1):

$$
\boxed{\;
\mathcal{S}\big[D_K(\tau),\,f,\,\Lambda\big]
=
\underbrace{\mathrm{Tr}\,f\!\Big(\tfrac{D_K(\tau)^2}{\Lambda^2}\Big)}_{\text{bosonic / spectral}}
+
\underbrace{\big\langle\, J\tilde\psi \,\big|\, D_K(\tau) \,\big|\, \tilde\psi \,\big\rangle}_{\text{fermionic}},
\qquad \tilde\psi\in\mathcal{H}_K^{+}
\;}
\tag{5}
$$

with `f` a positive even cutoff, `Λ = M_KK` the mass scale, `J` the real structure. This is the Chamseddine–Connes spectral action (CC 1996/97; CCM 2007 eq. 4.8) on the internal manifold `K = (SU(3), g_τ)` — the **bare Euclidean action**, i.e. the weight `e^{-S}` in the substrate's own partition function `Z = Σ_{D_K(τ)} e^{-S}` (Gibbons–Hawking; capstone §1.3a). The sum runs over the substrate's own internal geometries (the modulus `τ` and the spectral data of `D_K`), **not** over a background spacetime metric. There is no container being integrated over.

Why a single object carries gauge fields, gravity, *and* matter is **forced, not assembled** (capstone §1.1):

- **Gauge group ⇐ algebra**: `SU(A_K) = U(1)×SU(2)×SU(3)` (the unimodular unitaries; 13 generators, the S61 13/13 gate). *(Notational guard: the KK isometry of `g_τ` is the structurally different `SU(3)_L×U(2)_R` Killing stabilizer that supplies the Peter–Weyl labels — not the chiral SM gauge group; S96 W5-6.)*
- **Gauge fields + Higgs ⇐ inner fluctuation**: `D_K ↦ D_K + A + ε′JAJ^{-1}` decomposes automatically into a spin-1 part (gauge fields, along Killing directions) and a spin-0 part (the **Higgs**, along non-Killing directions). The bosonic trace's heat-kernel expansion then delivers the Einstein–Hilbert kinematic term (`a₂`) and the gauge+Higgs Lagrangian (`a₄`) *from the same trace*.
- **Matter ⇐ the inner product**: the fermionic action is the *other* canonical scalar of the triple. A trace and a bilinear form **exhaust** the scalars buildable from `(A_K, H_K, D_K, J)` — and that exhaustion is a *verified algebraic rigidity*, not a counting argument: `dim\,HH¹(A_K,A_K) = dim\,HH²(A_K,A_K) = 0` (S95 W2-2, exact rational rank count). Every derivation of `A_K` is inner (Whitehead's lemma) and every first-order deformation reduces to an inner fluctuation, so the interaction structure is **forced by the algebra** — structurally stronger than a string field theory, which must *select* its vertex from inequivalent options.

The collapse is `τ → g_τ → D_K(τ) → S[D_K, f, Λ] → \{a_0, a_2, a_4, \dots\} → \text{all observables}` (capstone §1.3). Every arrow is a function, not a choice.

### 2.2 The Seeley–DeWitt layers — the layers of exflation

Expanding the bosonic trace by the heat kernel peels the action into an ordered tower indexed by curvature-polynomial degree:

$$
\mathrm{Tr}\,f\!\Big(\tfrac{D_K^2}{\Lambda^2}\Big) \sim \underbrace{f_4\Lambda^4 a_0}_{\text{vacuum}} + \underbrace{f_2\Lambda^2 a_2(\tau)}_{\text{gravity}} + \underbrace{f_0\,a_4(\tau)}_{\text{matter}} + \underbrace{f_{-2}\Lambda^{-2}a_6(\tau)}_{\text{corrections}} + \cdots
\tag{6}
$$

| Layer | `Λ`-power | curvature degree | emergent physics |
|:--|:--|:--|:--|
| `a₀` | `Λ⁴` | 0 (`∝ V`) | **vacuum energy / cosmological term** (`τ`-independent — volume preserved) |
| `a₂` | `Λ²` | 1 (`∝ R`) | **Einstein–Hilbert** — gravity is the *second spectral moment*; `1/(16πG_N)` read off here |
| `a₄` | `Λ⁰` | 2 (`R² + F²`) | **Yang–Mills + Higgs quartic** |

Gravity is **not a fundamental law** imposed on the substrate; it is `a₂`. The bosonic/Dirac split in the `a₂` layer is the exact, representation-theoretic, `τ`-independent ratio `a₂^{bos}/a₂^{Dirac} = 61/20` (E36).

### 2.3 The Spectral-Moment Decoupling Theorem (the Stratum-1 centerpiece)

The skeptic's objection — "is `a₄` just a function of `a₀, a₂`, one knob dressed three ways?" — is settled by the **Spectral-Moment Decoupling Theorem** (S75 W2-E, **CERTIFIED**, `≥8` independent Sage-reverifications). With `a₀ ∝ V` (constant), `a₂ ∝ R_K·V`, `a₄ ∝ R_K²·V`, the Wronskian is governed by the **cube of the curvature gradient**:

$$
W[a_0, a_2, a_4](\tau) \;\propto\; R_K'(\tau)^3 = \big(e^{-4\tau}(e^{3\tau}-1)^2\big)^3 = e^{-12\tau}(e^{3\tau}-1)^6,
\tag{7}
$$

i.e. `W = \frac{5}{393216\pi^{12}}V^3 e^{-12\tau}(e^{3\tau}-1)^6`. This vanishes to **sixth order at, and only at, `τ = 0`** (the round genesis point) and is strictly nonzero everywhere else. **The three layers are algebraically independent everywhere the universe lives; they degenerate into a single scale only at the maximally-symmetric instant of genesis, and separate the moment exflation begins.** Structurally this is a *dispersion-rigidity* statement: `{1, R_K, R_K²}` are independent functionals exactly when `R_K` is moving (`R_K′ ≠ 0`) — the same band-lifting that `SO(8) → U(2)` performs on the spectrum as `τ` turns on, restated at the level of the moments. This theorem is *why* "vacuum energy, gravity, and the Standard Model all emerge from `D_K` while remaining physically distinct" is licensed rather than asserted.

### 2.4 The spectral functional `f` and the convergence cone

A bare trace is not yet physics: the spectrum `\{λ_k, m_k\}` is fixed substrate data, but the *number* the trace returns depends on how the high modes are weighted (`f`) and where the sum is cut (`Λ`). Two facts make `f` a genuine, stratified physical input:

**(i) `f` is physical and the tilt sign is scheme-set.** The slow-roll parameter `ε_H` (a pure spectral-shape quantity) **flips sign** between schemes (capstone §3.2):

| functional | `ε_H` | tilt |
|:--|:--|:--|
| cutoff `√x` (framework's working choice) | `+0.0216` | **red** (observed) |
| zeta `a₄` | `−0.0449` | blue (excluded) |
| anomaly-derived `φ` | `+0.0176` | — (excluded) |

This is the framework's "most important negative result since the Venus Moment" (the `ε_H` spectral-functional crisis, retraction-log item 36, atlas-10 Breakthrough #20): **the sign of the CMB tilt is a property of the regularization scheme, not of the spectrum alone.** It is stored as a PERMANENT negative result. What rescues a definite prediction is *structural* pre-registration, not after-the-fact selection: the anomaly family is excluded by **ANOMALY-FAMILY EXCLUSION** (S67 — gives `n_s > 1` for all `φ > 0`, decided before the tilt comparison), and absolute spectral-moment magnitudes are excluded as physical observables by **ZETA-NOT-PHYSICAL** (S75 — only ratios under a *fixed* regulator are physical). This is the **FI/RD partition**: **Functional-Invariant** observables (ratios of two spectrum-sums under one regulator — `c_s`, the sound-speed ratios, `R₁`) survive all choices; **regulator-dressed** observables (`ε_H` sign, the `n_s` value, `m_H`, absolute vacuum energy) must be *determined*, not assumed. `f` is a nuisance functional, and the FI ratios are exactly the observables that survive marginalizing it out — the cosmological face of Bayesian model averaging over an unknown energy-density functional. The framework's working functional is

$$
f^*(x) = 0.9117\,\sqrt{x} + 0.0883\,e^{-x},\qquad t^* = 0.08832,
\tag{8}
$$

whose admixture `t*` is **the framework's single empirical coupling** — the spectral-functional analog of `Λ_QCD`, an `O(1)` datum no first principle has been shown to select. The corridor "`t*` is the one-loop threshold coefficient" is **CLOSED** (S95 W2-1, FAIL: the parameter-free one-loop content `Γ_{1\text{loop}} ≈ 26%` of the tree+loop action is `~3×` too large to *be* `t* = 0.08832`).

**(ii) The convergence cone fixes which moments exist.** The moments are residues of `ζ_{D_K}(s) = Σ m_k λ_k^{-2s}` (the **double-power** convention) at `s = (d-n)/2` (CM-1995). For `SU(3)` (`d = 8`) the dimension spectrum — the **curvature-degree grading `n`** — is `S_d = \{0, 2, 4, 6, 8\}`. There is a **firewall** the corpus enforces (capstone §3.3): `\{0,2,4,6,8\}` is the *grading `n`*, **not** the pole set in the Mellin variable `s`. Under the printed `λ^{-2s}` convention the poles sit at

$$
S_s = \{(d-n)/2\} = \{0, 1, 2, 3, 4\},\qquad n = d - 2s = 8 - 2s.
\tag{9}
$$

Reading `n` as if it were `s` mis-locates each pole by `Δ = 8 - 3s` — a **factor-≈2 mislabel** at the load-bearing `a₂, a₄` poles. (So `α_s`'s `s=3` (Conv. A) and a Pati-Salam extension's `s=6` (Conv. B) *both* denote `n=2`, the `a₂` residue; the labels differ by exactly the power-convention factor 2.) Only `a₀, a₂, a₄, a₆, a₈` exist as honest residues (odd moments vanish by BDI parity); then the cone closes. This is the crux of the CC freedom, read substrate-first: **the substrate does not hand us a foam of fluctuating topologies summed over — it hands us a finite, closed pole ladder, and the regulator's only remaining freedom is which residues it weights.** A defensive corollary: the dimension spectrum is `τ`-independent (`d_s ∼ 8` at the gap scale across four `τ` values, S31Aa) — the substrate exhibits **no flowing spectral dimension**, no CDT-like UV reduction; the low-`d_s` readings of windowed observables are a diffusion-window artifact (S92), not a dimensional flow.

### 2.5 The `a_n` firewall, the Higgs, and dimensional closure

**The `a_n` firewall** (capstone §8.2). Two triples circulate and are *different objects*:

| | raw mode-count `a_n^{raw}` (`L_max=10`) | Gilkey-zeta `a_n^{ζ}` (fold; **canonical**) |
|:--|:--|:--|
| `a₀` | 155984 (`= Tr\,1`) | **6440** (`a_0_FW_zeta`) |
| `a₂` | 64308 | **2776.165** (`a_2_FW_zeta`) |
| `a₄` | 29086 | **1350.7216** (`a_4_FW_zeta`) |

The raw sums *diverge* with `L_max`; the Gilkey-zeta coefficients are finite curvature integrals. **Only ratios survive truncation** — the multiplicative-normalization-cancellation invariant (K=3-MANDATORY, `math-scripts.md`). The single scheme-invariant number on the cover is the FI ratio

$$
R_1 = \frac{a_0\,a_4}{a_2^2} = 1.128655 \quad\text{(Sage-verified)},
\tag{10}
$$

invariant under any `R_K → c\,R_K` rescaling (the `c²` cancels). The corpus rule: display the Gilkey-zeta triple as *the* `a_n`; the `Λ`-power hierarchy is "`Λ⁴` term `≫` `Λ²` term `≫` `Λ⁰` term," **never** "`a₀ > a₂ > a₄`."

**The Higgs and `m_H`.** The Higgs is the transverse `|S|²` fiber-embedding oscillation. Its mass is route-pinned to the **KK-threshold DIRECT** route (`a₄`-KK saturation, `L_sat = 6 < L_max = 10`):

$$
m_H = 131.8\ \text{GeV}\quad(\texttt{m\_H\_FW\_KK\_threshold},\ \text{S102 W4-20, audit }\texttt{75ed7ffb}),
\tag{11}
$$

`+5.36%` (`= 67/1251` exact) above `m_{H,\mathrm{obs}} = 125.1` GeV, from **zero particle-physics parameters**. *(Down-tag flagged: the `127.5` GeV Aitken/KK-L5 figure is the SPURIOUS overshoot — `1.2416×` floor — and must not be cited; the zeta route `138.5` GeV is excluded; the `μ_BC = 188` GeV fit is an accommodation, not a prediction. S102 pins Route B.)* The `+5.36%` residual is **PHYSICAL-but-UNDERIVED** (S110 HK-R-PROTECTION-MH): both the truncation route and the named self-energy route are falsified; the quartic *gives*, does not *derive*, `131.8`. The residual open item is the imported `M_KK` scale (§6), not the route.

**Dimensional closure and the Newton dictionary.** `[S] = mass⁰`: in (6) each term `f_{d-2k}Λ^{d-2k}a_{2k}` is individually mass-dimension 0 (the Gilkey scaling `[a_{2k}] = mass^{2k-d}` cancels `[Λ^{d-2k}]`). The `a₂` term is the emergent Einstein–Hilbert action, giving the CC dictionary `M_{Pl,red}^2 = f_2 M_{KK}^2 a_2/(24\pi^2)`, which with `M_KK = 7.4287×10¹⁶` GeV and `a₂^ζ = 2776.17` closes at `f₂ ≈ 92` — an `O(10²)` cutoff-moment of the same legitimacy class as the CCM `f₂` at unification, and **not a free knob** (fixed by the `M_Pl/M_KK` ratio once `a₂^ζ` is pinned).

### 2.6 The honest free-parameter ledger

The "1 → 60" collapse is real but the framework is **not** zero-parameter (capstone §1.4, §8.4). Its inputs are

$$
\{\,\tau\ (\text{geometric modulus, theorem-pinned at }\tau_{\text{fold}}),\ \ \Lambda = M_{KK}\ (\text{substrate-fixed}),\ \ f_0, f_2, f_4\ (\text{cutoff moments})\,\} \;+\; t^*.
\tag{12}
$$

Given `(A_K, H_K, D_K(τ))` and the UV data `(Λ, f₀, f₂, f₄)`, the remaining ~56 atlas equations are theorems and spectral read-offs carrying no further input. The ledger is short *by construction*: `S[D_K, f, Λ]` is a **principle theory** in Einstein's 1919 sense — the field content is *read off* the algebra, and the open inputs (`τ` value, the functional `f`, the family number) are exactly what such a theory is entitled to leave to a completion. Both halves are load-bearing and stated without softening.

---

## 3. The cosmology

Exflation is the **growth of spectral complexity inside each point** — the eigenvalue spectrum of `D_K(τ)` reorganizing as `τ` transits the fold — *not* metric expansion of a pre-existing box. The emergent scale factor is read off *afterward* from how `a₂` moves. The full translation table from ΛCDM/inflation vocabulary lives in the basic intro §4 and in `phononic-framing.md`; here is the dynamics.

### 3.1 The driver: a monotone ramp, no potential well

The fabric's internal action is read off the leading moments, and its gradient at the fold is enormous, positive, and — load-bearing — **monotone**:

$$
S_{\mathrm{SA}}(\tau) = a_0(\tau) - a_2(\tau) + a_4(\tau),
\qquad
\frac{dS}{d\tau}\bigg|_{\tau_{\text{fold}}} = +58{,}672.8,\quad S_{\text{fold}} = 2.50\times10^5.
\tag{13}
$$

By the **Structural Monotonicity Theorem** (E7: `d⟨λ²⟩/dτ > 0 ⇒` each `a_{2k}` monotone `⇒ dS_f/dτ > 0` for all monotone `f`, all `Λ`; 9,600/9,600 checks), the spectral action has **no stationary point at any `τ`**: there is no `V(τ)` with a minimum to roll into. Twenty-seven equilibrium-closure attempts (S17–S40) all failed; the moduli constraint surface is zero-dimensional (HESS-40: all 22 transverse Hessian eigenvalues positive). Equivalently, the partition weight `e^{-S(τ)}` is monotone, so `Z` has **no interior saddle in `τ`** and is dominated by the genesis boundary — making "transit, not slow-roll" structurally inevitable. This result is **one-loop-robust**: adding `Γ_{1\text{loop}} = ½\,\mathrm{Tr}\ln(D_K^2/Λ^2)`, the full `dΓ/dτ` retains a fixed sign with zero interior sign-changes over `τ ∈ [0, τ_{now}]` (S95 W2-3, 200-point grid, three routes).

**Consequence — the slow-roll relations are INAPPLICABLE, structurally.** `r = 16ε` and `n_s = 1 - 6ε + 2η` are theorems of the *single-clock adiabatic vacuum*; the fold violates all three premises at once (the sweep is diabatic; the dispersion is BdG with `c_s ≠ 1`; the produced state is a multi-mode squeezed GGE, not a single-clock vacuum), so the relations' *derivation assumptions are absent* — not merely their conclusions mismatched (five independent arguments, VdD–Hawking workshop). The controlling quantity is the *diabaticity* of the sweep.

### 3.2 The trajectory: cold big bang → supersonic transit → frozen present

- **(i) `τ = 0` — the cold big bang.** The round, maximally-symmetric `SU(3)` metric: an *unstable* extremum with no restoring force (a pencil on its tip). The first move is **first-order** by a cubic term (`V'''(0) = -7.2`), the **Perturbative Exhaustion Theorem** (E17, H1–H5 verified). Genesis is *regular* — a smooth group manifold, `R_K = 2`, gap open, **no singularity**. The genuine curvature singularity is **relocated to `τ → ∞` and censored**: the Kretschmann scalar diverges there (`K ∼ e^{4τ}`), with anisotropic Kasner-type character (timelike in the contracting `su(2)` block, spacelike in the expanding blocks), and it is dynamically unreachable behind a triple-layer censoring barrier (NEC holds to `τ_NEC = 1.383`; the modulus blocked at `τ ≈ 0.191`; overshoot turnaround at `τ = 1.614`). This is weak cosmic censorship on the full 12D metric (S95 W4-5).
- **(ii) `τ_fold = 0.190` — the first-order transit.** The B2 density of states develops a van Hove singularity (`g(ω) ∼ 1/\sqrt{ω - ω_{min}}`); the **BCS 1-D theorem** (E13, three proofs) makes Cooper instability a *theorem* — zero critical coupling, `β(g) = -g²`. The crossing is **supersonic and impulsive**:

  $$
  \mathrm{Ma} = \frac{v_{\text{transit}}}{c_{\text{fabric}}} = 13.75\quad(\texttt{Mach\_max\_framework},\ \text{S85};\ c_{\text{fabric}} = 209.97\ M_{KK}),
  $$

  with sudden-quench ratio `δt_{transit}/T_L = 1.25×10⁻⁵` (the crossing is `38{,}600×` faster than the condensate can form). *(Down-tag/conflation guard, per the capstone §5.2: the canonical Mach is the velocity ratio `13.75`; a source digest's `20.73` is the distinct `v/c_{BA}` acoustic-cone reading, and the fold-local `421.3` / B2-channel `293.79` are acoustic-radius ratios — never averaged with the velocity-ratio Mach.)*
- **(iii) `τ_now` — frozen plateau.** Post-fold, `τ` is effectively frozen: the **clock constraint** (E27) bounds `|τ̇| < 2.4×10⁻⁶ τ_0/t_H` (a rolling modulus would violate atomic-clock `δα/α` by `~15{,}000×`, closing all rolling quintessence), and the frozen-spectrum theorem holds at `10⁻¹¹³`.

### 3.3 Transit dynamics: particle production and the GGE relic

The impulsive crossing is a Bogoliubov sudden quench of the substrate-BdG modes `u_k'' + ω_k^2(τ(t))\,u_k = 0` with `ω_k = E_k = \sqrt{(λ_k^2 - μ^2)^2 + Δ_k^2}`. Because the crossing is diabatic (`δt/T_L ≪ 1`), pair production **saturates**:

$$
P_{\text{exc}} = 1.000,\qquad \langle Q\rangle_{\text{GGE}} = 59.8\ \text{pairs},\qquad S_{\text{inst}} = 0.0686,\qquad E_{\text{exc}}/|E_{\text{cond}}| = 443.
\tag{14}
$$

Every mode is excited; the condensate is **completely destroyed, not perturbatively dressed** (bosonic normalization mode-by-mode, `|α_k|^2 - |β_k|^2 = 1`; the diabatic `P_{exc} → 1` is the analog-cosmology opposite of the adiabatic no-particle vacuum). The Bogoliubov sudden-quench and Kibble–Zurek impulse-matching are the same physics read two ways. The output is an **analytic Generalized Gibbs Ensemble** — a pure product state (`S_ent = 0`) with three Lagrange multipliers conjugate to the conserved charges of the post-fold integrable Hamiltonian (*not* to energy — hence no temperature). *(`⟨Q⟩_GGE = 59.8` is a projected charge, not a literal pair count: it inherits a `~60%` PBCS overestimate and a `~225×` Richardson–Gaudin condensation-energy overestimate, S46/S63; the regime-robust structural claim is `P_exc = 1`, with the exact Fock reduction `N_Fock = 1`, S74.)*

### 3.4 The Ordered Veil — and the correction that matters

This GGE relic is the framework's "reheating": **THE ORDERED VEIL.** The surviving claim is **diabatic transit-freeze, not integrability permanence** — and getting this right is load-bearing.

*(Down-tag flagged — the single most important correction in the cosmology. The strong S38 reading "the relic is permanent because the post-fold Hamiltonian is Richardson–Gaudin integrable, so it never thermalizes even at Hubble time" is **BROKEN / RETRACTED**: Atlas D04 **T3 = BROKEN** (`V_phys` 13% non-separable, Brody `β = 0.633`, `t_therm ≈ 6\,M_{KK}^{-1}`), retraction-log **item 16** removed the permanence claim. On cosmological timescales the relic **does** relax to Gibbs.)*

What survives is strictly weaker and compute-certified — the relic is **frozen by sheer speed**, and this is over-determined by three independent legs (capstone §5.3):

1. **Diabatic freeze**: `R_{\text{therm}} = t_{therm}/t_{transit} = 5251.82 \gg 1` (S95 W5) — the crossing screens the relic thousands of times faster than any rearrangement channel can act.
2. **Pure product state**: `S_{ent} = 0` exactly (S95 W5) — the squeeze is a pure Bogoliubov product, independent of the broken integrability claim.
3. **Causal corroboration**: `τ_fold = 0.190` is a **double-root extremal Killing horizon** (`V = V' = 0 ⟹ κ_V = 0, T_H = 0`), so zero Hawking temperature follows with no integrability argument at all.

Information-theoretically this resolves what would otherwise be an analog information paradox: the transit is a Bogoliubov transformation (unitary by construction); a thermalizing relic (`S_ent > 0`) would scramble that into a mixed state. The GGE stays pure — the Bogoliubov phase data is retained in the conserved charges, so there is **no Page curve to reproduce** (on the transit clock) and the substrate carries no horizon-entropy debt out of the fold. The observed CMB is the acoustic signature of this relic, *not* thermal-equilibrium radiation. *(S110 HK-ORDVEIL refinement: information-completeness is COMPLETE as a unitarity assertion (`S_ent = 0`) but INCOMPLETE as a mechanism-exhibition — the saddle class that would display the unitary step-by-step is structurally absent, the GGE Fock trace being a saddle-free analytic Boltzmann product.)*

A reader-trap the register closes with a **surface-gravity KIND table**: at the *same* `τ = 0.190`, the modulus-metric double-root `κ_V = 0` (`T_H = 0`) coexists with a Gibbons–Hawking emergent-horizon `T_{GH} = 0.2172\,M_{KK}` and an internal-acoustic SONIC surface `T = 0.112\,M_{KK}`. These are **different surface-gravity functionals on different geometric objects**, not inconsistent values of one functional. The OBSERVED relic spectral temperature is the `a₄` condensation-exit value `7.578\,M_{KK}`; the `0.112` is a SONIC surface, never the relic temperature.

### 3.5 The acoustic white hole

The causal architecture is an **acoustic white hole** — the fabric's amplitude/spectral-weight flow goes supersonic through the fold, and pre-fold/post-fold are causally disconnected. This is the substrate's resolution of the **horizon problem**: recast as causal disconnection by a supersonic acoustic flow, *not* inflationary stretching of a pre-existing box (S85 PROVEN). *(Down-tag flagged: an earlier S48 version claimed a superfluid *superflow* analog horizon, RETRACTED (retraction-log item 22) — the substrate has no phase-gradient superflow (`φ = 0`). The current structure is a causal-disconnection white hole on the amplitude/acoustic-metric flow, not a superflow in a container.)*

Two structural features of the current object:

- **It is sector-dependent (two null cones).** By the Scalar-Tensor Kasparov Decoupling theorem [T3] (`β_T = 0` exactly at linear order, PERMANENT), the white hole is a *scalar-sector* structure: the scalar sector sees the acoustic metric `g_{\text{acoustic}} ∝ \sqrt{ρ_s/c_s}` and the horizon; the **tensor sector crosses the fold freely** on the `a₂`-emergent metric `g_M`. This is the geometric root of why the tensor observables (`r, n_T`) behave so differently from the scalar ones (`n_s, A_s`) — they propagate on different cones. The escaping scalar amplitude is filtered by an analog greybody factor `Γ(ω) ∈ [0,1]`, so `A_s = (\text{produced squeeze}) × ∫Γ(ω)\,dω` — "the horizon determines what escapes, not what is produced."
- **It is ASYMMETRIC** (one entry sonic surface, open supersonic exit — no future-trapped exit horizon, no symmetric throat, **no bounce**), over-determined at six independent walls (S95 W-1), the deepest being the entropy-arrow of the irreversible Kibble–Zurek quench.

### 3.6 The dark sector

**Dark matter = a Leggett-channel GGE quasiparticle** (E47, the inter-band coherence mode). It is **CPT-neutral**, **superselection-protected** (`N_pair` conserved, no annihilation channel), and **momentum-flux-free** (`T^{0i} = 0` exact — born at rest):

$$
\Omega_{DM}h^2 = 0.120\ (\text{Leggett-only},\ \texttt{Omega\_DM\_h2}),\quad\text{vs Planck } 0.1186\pm0.0020\ \Rightarrow\ 0.7\sigma.
\tag{15}
$$

The geometry does **not** permit this to be tuned: the *full* Goldstone spectrum over-produces by `260σ`, and *only* the Leggett-channel projection lands at `0.7σ`; that same channel forces `σ/m = 0` **exactly** (`N_Fock = 1` superselection, vs Bullet `< 1.25` cm²/g) — a structural zero distinct from any tuned cross-section. The PASS is CONDITIONAL on `LEGGETT-GRAV-DECAY-67` (`Γ_grav < H_0`), satisfied with a 65-OOM margin (`Γ_grav/H_0 ∼ 8.85×10⁻⁶⁶`, S95).

**Dark energy = the effacement residual + Volovik tracking vacuum.** It is *not* quintessence (the clock constraint closes that at `15{,}000×` the bound); it is a `0.03%` impedance leak (`Γ_eff = 0.99970`, `Gamma_effacement`) plus the Volovik tracking vacuum `ρ_vac(t) ∼ M_{Pl}^2 H^2(t)` — the de Sitter horizon energy density, the substrate tracking its own emergent de Sitter horizon. This is the **DILUTION-CC** resolution of the cosmological-constant problem:

$$
\frac{ρ_{vac}(\text{today})}{ρ_{obs}} = 1.032\quad(\text{0.01 OOM};\ \texttt{DILUTION-CC-66},\ \text{PASS}),
\tag{16}
$$

closing the famous 114-OOM discrepancy (the `115.5` OOM is the *dilution depth* the `H`-span traverses, a feature, not a failure metric). **But the register is careful to call this *located, not solved*** (capstone §7.1 CC caveat box; frontier #6 of §6), and the structure is a two-clause statement:

- **Clause A (non-inheritance — warranted exactly).** The equilibrium theorem `dε/dq = μ ⇒ ρ_Λ = 0` at equilibrium (`q = N_pair`) makes the *equilibrium* vacuum energy **exactly zero** by an *exact thermodynamic identity* (`ε - μq = -P = 0`, Gibbs–Duhem, S95 W5-3, Sage-rational `0`) — *not* a tuned cancellation. The catastrophe is an artifact of computing vacuum energy in a container-EFT without a UV completion; the substrate *has* its UV completion (`D_K`), so the bare term is removed by an identity. This warrant is **thermodynamic, not topological** — the substrate is ³He-B class (`N₃ = 0`, BDI), *not* ³He-A (`N₃ = 2`) where the vacuum energy would be topologically protected.
- **Clause B (observed magnitude — doubly conditional).** With no topological protection, `ρ_Λ = 0` is a *reference value, not an attainable interior point* (there is no interior q-equilibrium in the gapped substrate; at the physical ground state `N_pair = 1` the system sits *off* equilibrium, `P_vac = -0.688 ≠ 0`). So the *observed* Λ is the **non-equilibrium tracking residual**, whose "not-tuned" status rests on the C10 tracking law (`ρ_vac ∼ M_Pl²H²`, **ASSUMED-PARTIALLY-PROVEN**) evaluated off-equilibrium. The CC closure is therefore **doubly conditional** — on C10 AND on the external `H(t)` the tracking law feeds (the same undelivered effective-Friedmann map as the `a(t)` gap, §6). `1.032` is a genuine PASS *given* an external `H(t)`, not yet a from-`D_K` derivation of the dark-energy density. The framework has correctly **located** the cosmological-constant term (the `a₀` moment, geometrically natural — not inserted); it has not **solved** the cosmological-constant *problem*.

### 3.7 The CMB observables and the scale-transport map

The CMB tilt is the **interference pattern of post-transit GGE acoustic excitations**, from gauge-invariant spectral geometry — not density perturbations in expanding space. The committed value is the `√x` BCS+1-loop reading:

$$
n_s = 0.9590\quad(\texttt{n\_s\_FW\_sqrt\_cutoff},\ \text{S103 W5-2, FUNCTIONAL-SELECTION-COMMITTED}),
\tag{17}
$$

with the functional-selection question CLOSED (`f = √x` is the S67-unique survivor, atlas-cardinality-robust under `A₅ → A₆`, `S103-Q28-LAYER2-A6` PASS). *(Register nuance carried: `0.9590` is the committed `√x` point; `0.9561` (`n_s_framework`, const-ε gauge-invariant) and `0.9595` (`√x` Window-7) are `(value, scheme)` disclosure tuples, never band-shopped. The BMA band `0.969 ± 0.022` was the correct UQ object *while* `f` was unselected; it is superseded now `f` is selection-robust.)* Status: **CONDITIONAL/LIVE** — `1.40σ` below Planck `0.9649 ± 0.0042`, but the live-watch is **firing in the falsifying direction**: SPT-3G `2.70σ`, ACT-only `3.13σ`, P-ACT `0.974` → `~5σ`. The prediction is *fixed*; the data are moving against it; functional re-shopping is forbidden by the anti-rescue fence (`falsifier-master-inventory.md` Row #85).

**The `α_s` running is the most-misread row, and the resolution is structural** (capstone §7.1 α_s box; S93 W7-1). The naive "`α_s = -0.086` vs Planck `-0.0045` is a 12σ tension" is a single-label conflation. The substrate carries **two scale-separated `α_s` observables**:

$$
\alpha_s^{\text{substrate-distance}} = -0.08587279\ (s=3\ \text{Mellin pole, inside the BZ},\ \texttt{alpha\_s\_substrate\_distance\_1}),
\qquad
\alpha_s^{\text{pivot}} \approx 0\ (\text{Goldstone, CMB pivot},\ \texttt{alpha\_s\_pivot\_goldstone}).
\tag{18}
$$

Which one a detector sees is set by the **computable transport degree `deg(T_{BZ→pivot}) = +2`** (non-scalar) across the **54.04 decades** separating the substrate/BZ scale `O(M_KK)` from the CMB pivot `0.05` Mpc⁻¹. The substrate-distance value is FI-class (regulator-invariant, *frozen now* — it cannot drift to meet CMB-S4); the pivot image sits at **`+0.67σ` — consistent** with Planck; the substrate value relocates to a `~34σ`-reach CMB-S4/CMB-HD falsifier. *(Down-tag flagged: "12σ tension" is the stale single-label reading; the current status is tension-resolved-as-channel-artifact, pivot consistent, substrate value a future test.)* The structural identity behind the substrate-distance number is `α_s = n_s² - 1` (E48, five proofs, PERMANENT) — using the substrate-distance `n_s = 0.9561`, `n_s² - 1 = -8587279/10⁸` exactly (Sage-QQ), the sign locked to the tilt by the rational-propagator structure.

---

## 4. The permanent results

The framework's credibility rests on a clean separation: **structural theorems** that are true of the instrument regardless of whether the cosmology is right, vs **observational matches**, vs **live-watch tensions**. This section is the first; §5 is the others.

### 4.1 The machine-precision structural theorems

These are facts about the construction, verified to `~10⁻¹³` or better, many re-checked `8+` times independently (`atlas-07-permanent-results.md`; `sessions/permanent-results-registry.md`).

| Result | Statement | Provenance |
|:--|:--|:--|
| **KO-dim = 6** | `(ε,ε′,ε″) = (+1,+1,−1)`; AZ class BDI; forces one generation | 10 checks `<10⁻¹⁵`, S7–S8 |
| **SM quantum numbers** | exact `16`-spinor branching, no charges by hand | exact, S7 |
| **`[J, D_K] = 0`** (CPT) | charge conjugation hardwired | 79,968 pairs, machine-ε, S17a |
| **`g₁/g₂ = e^{−2τ}`** | gauge-coupling ratio fixed by geometry (`sin²θ_W = e^{-4τ}/(1+e^{-4τ})` at `τ₀ = 0.2994`) | exact derivation, S17a |
| **Volume-preserving TT** | `det g_τ = const ⇒ G_N` has zero `τ`-dependence | exact `∀τ`, S12 |
| **`D_K` block-diagonal** | Schur on any compact semisimple Lie group | `8.4×10⁻¹⁵`, 3 proofs, S22b |
| **Algebra uniqueness** | `ℂ⊕ℍ⊕M₃(ℂ)`, 1 of 3,907 (dim ≤ 50) | exact, STAGE-3-PERMANENT, S88 |
| **Spectral-action monotonicity** (E7) | `S` strictly increasing `∀f, ∀Λ` — `τ` transits, no well | 9,600+ checks, S24a/S28c |
| **Cooper instability at the fold** | `β(g) = -g²`, zero critical coupling (1-D BCS) | 3 proofs, S35 |
| **`α_s = n_s² − 1`** | exact Mellin-residue identity | 5 proofs, Sage-QQ exact, S50 |
| **Spectral-Moment Decoupling** | `a₀, a₂, a₄` algebraically independent (`W ∝ R_K′³`) | CERTIFIED ≥8×, S75 W2-E |
| **Cauchy–Schwarz `F₀F₂ ≥ F₁²`** | spectral-moment hierarchy for any discrete spectrum | exact, S62 |
| **R-monotonicity / Fermi-surface lock / H2 / chirality** | `dR/dτ ≥ 0` (AM-GM); `v²(B2[0]) = ½`; `π_{ij} = 0`; `{γ_9, dD_K/dτ} = 0` | PERMANENT, S64 |

There are well over a hundred such landings. The point is the *character*, not the count (a count is not an argument): a large, internally-consistent body of structural mathematics that stands on its own even if the cosmology were wrong.

### 4.2 The organizing spine: geometry vs topology

The deepest available defense of the framework is that its claims **partition cleanly along the continuum-dissolution axis** (capstone §9). The finite spectral triple `(A_K, H_K, D_K(τ))` is GEOMETRY — it dissolves in the continuum limit (`T3-S43-SPECTRAL-DISSOLUTION` PASS, `ε_c ∼ N^{-0.457}`). The **topological / representation-theoretic** outputs **survive** that dissolution; the **absolute geometric magnitudes** are **conditional**:

| Survive continuum dissolution (trust) | Dissolve (hold pending convergence) |
|:--|:--|
| GGE relic + `S_ent = 0` purity (Ordered Veil) | CC *absolute* magnitude (pending SDW convergence, §6) |
| BDI / `N₃ = 0` class; cocycle ratio `7.324992` | the `a_n` *absolute* values |
| `[J, D_K] = 0` CPT; layer algebraic independence | the `a(t)` map (the dimensional normalization, §6) |
| FI ratio-observables (`R₁ = 1.12865`, `g₁/g₂`, `n_s`-as-ratio) | |
| trivial Berry holonomy `γ = 0`, `d_FS = 0` (S61) | |

The obvious objection — "if the spectral triple dissolves at the continuum limit, why trust any output?" — has a structural answer: **trust the topological outputs (they survive); hold the geometric magnitudes pending convergence (they do not).** Every strong claim lives on the surviving side; every honest gap on the dissolving side.

### 4.3 The §VII cross-pillar bridges

The framework registers **cross-pillar bridge theorems** connecting a substrate-IS observable on one pillar to a laboratory-IN observable on another, under a strict anatomy (`.claude/rules/cross-pillar-bridge-anatomy.md`): five mandatory elements (substrate-IS observable / laboratory-IN observable / explicit bridge map [HKR, K-theory boundary, or Connes–Karoubi pairing] / algebraic envelope `L^{-α}` / empirical anchor at canonical `L_max`) and a **three-level structural-confidence ladder**:

- **Level 1** — cohomology-class identity (regulator-invariant, `L`-independent): a STRUCTURAL THEOREM.
- **Level 2** — algebraic convergence envelope (`L^{-α}` bound): a STRUCTURAL PREDICTION.
- **Level 3** — empirical anchor at canonical `L_max`: an EMPIRICAL CONFIRMATION (registry-PASS requires Level-3 `<` Level-2 envelope).

Promotion to PERMANENT runs a **4-stage blind cross-review pathway** (`.claude/rules/joint-theorem-promotion.md`): a joint theorem is authored once (Stage 0), registered as `STAGE-1-CANDIDATE` (Stage 1), then independently verified by **two agents on opposite axes who never saw the authoring workshop** (Stage 2, PASS-AND on every joint clause), before `STAGE-3-PERMANENT` (Stage 3). The structural point of the blind step: agreement among agents with *shared* context is not evidence; agreement among two reviewers dispatched with *only* the registered entry **is**. The majority of the 60+ §VII slots have been promoted this way. Two concrete examples:

- **§VII.AF.1.OP-PROJ** (Pillar III ↔ IV, quantum-metric bridge): substrate-IS Hochschild `HC²` pairing ↔ laboratory-IN BdG-sector observable; bridge map HKR; Level-2 `L^{-3}` envelope at `d=4` (0.10% at `L_max=10`), Level-3 anchor `0.0095%` (10× inside envelope). **STAGE-3-PERMANENT** (blind 18/18 PASS-AND, S105).
- **§VII.W-3** — the **3He-B inheritance falsifier** (see §5.3): **STAGE-3-PERMANENT** (blind 11/11 PASS-AND, S100a).

The linchpin is the **inheritance morphism** `χ_* : ℂ⊕ℍ⊕M₃(ℂ) → M₂(ℂ)` sending `M₃(ℂ) → 0` (no non-abelian condensate on the color sector), with `\mathrm{rank}(\ker ι_*) = 2` (generators `φ_67` chiral, `φ_88` Cartan hypercharge). It is the structural reason the framework relates to ³He-B by **universality-class membership** (BDI, `N₃ = 0`), **not by analogy** — the substrate IS the ³He-B class's parent.

---

## 5. The pre-registered predictions

The framework is set up to be killed by data. The capstone §7 presents its observable scorecard as **three epistemic registers** so a referee reads each claim at its true register — the discipline a flat table would flatten. The values are spectral moments of `D_K` at the single modulus `τ_now`; **none is fit**.

### 5.1 Register A — Robust-Structural (the zero-free-parameter spine)

*PROVEN / PASS-structural / bounded — no borrowed `H(t)`.*

| Observable | Layer | Framework value | Anchor | Status |
|:--|:--|:--|:--|:--|
| **CC closure** | `a₀` | `ρ_vac/ρ_obs = 1.032` | observed Λ | PASS (DILUTION-CC-66); robust as the non-inheritance identity (Clause A) |
| **`r`** (tensor-scalar) | `a₂` tensor | `0.033` headline; dual-pathway **Path-H 0.00745 / Path-C 0.0117** | BICEP/Keck `< 0.036` | PASS (`<2σ`) |
| **`f_NL`** | bispectrum | `|f_NL| ≲ 1.5` (Gaussian by Wick; SU(1,1)-linear squeeze) | Planck `−0.9 ± 5.1` | PASS (structural bound, 0.47σ) |
| **`σ/m`** (DM self-int.) | `N_Fock=1` | **0 exactly** | Bullet `< 1.25` cm²/g | PASS (structural zero) |
| **`f·σ₈(z)`** (RSD growth) | `a₂` growth | **−4.058%** product suppression @ `z=0.51` (`S₈`-relieving sign) | DESI-5yr / Euclid | PASS-class; joint 7-bin `1.95σ` DESI-Y5 / `2.96σ` Euclid |
| **ν mass ordering** | `a₄`/fiber | Normal `B1<B2<B3` (zero-param eigenvalue ordering) | NuFit-6.0 (`~2.5σ` preferred) | PASS (machine-ε) |
| **`c_s²`** (dark-sector) | `a₂`/Kasparov | **0 exactly** (Level-1 topological) | DES/KiDS (future) | PASS-class (§VII.BH bridge PROVEN) |

### 5.2 Register B — Conditional (PASS contingent on an unresolved input)

*CONDITIONAL / scheme-dependent / route-dependent / borrows external `H(t)` (marked `†`).*

| Observable | Framework value | Anchor | Status |
|:--|:--|:--|:--|
| **`w₀`** `†` | **−0.918** (`w0_FW`, Volovik partition); branch-iv `−0.842454` | `−0.803 ± 0.054` (Popovic/DES-Dovekie 2025) | LIVE, `2.13σ` / `0.73σ`; **DESI DR3 (2027) decisive** |
| **`n_s`** | **0.9590** (committed `√x`) | Planck `0.9649`; P-ACT `0.974` | LIVE, `1.40σ → 5σ` one-sided low (firing against) |
| **`α_s`** | dual: `−0.0859` (substrate-distance) / `≈0` (pivot) | Planck `−0.0045 ± 0.0067` | pivot image `+0.67σ` consistent; substrate value awaits CMB-S4 |
| **`m_H`** | **131.8 GeV** (KK-threshold DIRECT) | PDG `125.25 ± 0.17` | PASS-class (`~2%` budget); band-MISS `+5.36%`; route-PINNED, conditional on `M_KK` |
| **`Ω_DM h²`** | **0.120** (Leggett) | Planck `0.1186 ± 0.0020` | PASS `0.7σ` GIVEN `Γ_grav < H_0` (satisfied, 65-OOM margin) |
| **`σ₈`** `†` | **0.799** (zero-param) | Planck `0.811`; lensing `~0.76` | VIABLE (`~2σ` below Planck), not a resolution |
| **`Σm_ν`** | **0.0582 eV** (type-I seesaw, `M_R` from `D_K` fold energies) | DESI 2024 `< 0.072 eV` | PASS by 19%; `m_D`-normalization irreducibly external |
| **`H₀`** `†` | **67.40 km/s/Mpc** (G_N-ratio channel) | 67–73 (method-dependent) | re-pinned S101; **anchor-degenerate** (a ratio-channel form, not an independent magnitude) |

### 5.3 Register C — Currently-Falsified (the live wagers — reported as boundaries)

| Observable | Framework value | Anchor | Status |
|:--|:--|:--|:--|
| **`w_a`** | **0** (structural four-fold lock; `wₐ = 0` is a PERMANENT *theorem*, not a small number) | `−0.72 ± 0.21` (same joint fit) | **BROKEN, `3.43σ`** — the live wager: prediction fixed, data moving away |

The honesty here is the point: `w_a = 0` is a *structural theorem* (the triple-lock of the clock-constraint identity + CMB-pivot + quintessential slow-roll), and the data are pulling away from it. The binding 2D test is the `(w₀, w_a)` posterior — the `R_842` rectangle (Falsifier #1), `ρ(w₀, w_a) ≈ −0.85` — not two independent 1D marginals. DESI DR3 (2027) is the near-term cliff-edge.

### 5.4 The 3He-B inheritance falsifier (the laboratory flagship)

Because the substrate IS the ³He-B universality class (not an analog of it), it makes **laboratory** predictions through the inheritance morphism of §4.3. The falsifier is a **4-gate protocol** (`.claude/rules/inheritance-falsifier-protocol.md`) over the rank-2 kernel `\ker(ι_*) = \{φ_67, φ_88\}`:

- **Class A — kernel-signature NULL tests**: for each generator, the corresponding laboratory observable returns NULL under BDI protection. Gate 1 (decisive): F1 vortex-core Caroli–Matricon ladder asymmetry (`φ_67`-clean), F2 SABS axial-equatorial off-diagonal; Gate 3 (supporting): F3, F4. The F1 substrate S/N anchor is `0.573193\,M_{KK}^2`.
- **Class B — cohomology-asymmetry ratio test**: the substrate-derived cross-cocycle ratio is **preserved INTACT** in the lab under the `(Δ_B/Δ_A)^p` lab-conversion (the common exponent cancels exactly — a machine-precision identity, residual `0.0e+00`):

  $$
  \frac{\lVert φ_{67}\rVert}{\lVert φ_{88}\rVert} = 7.324992 \quad(\texttt{substrate\_cocycle\_ratio\_67\_88} = 7.3249918;\ \text{lab prediction } 7.3250 \pm 0.1\%).
  $$

This is what makes the test substrate-*falsifying* rather than lab-conversion-dependent: a measured ratio diverging from `7.3250` falsifies the inheritance structure regardless of the precise `(Δ_B/Δ_A)`. **Lab platforms**: Lancaster MCT-3 and Helsinki ROTA vortex-core spectroscopy; ³He-A µSR; RHUL/TKK nanofluidic. **Horizon**: a multi-year low-temperature campaign, `~2027–2031`. A clean null where the framework predicts the ratio (or vice versa) falsifies the universality-class assignment itself — a stronger test of the inheritance than any CMB measurement.

### 5.5 The decisive timeline, and the GW retraction

| Year | Instrument | Test | Consequence |
|:--|:--|:--|:--|
| **2027** | DESI DR3 | `w₀, w_a` | the near-term cliff-edge; `~5σ` closure of the Volovik-partition branch if `w₀ → −1`, `w_a` already `3.43σ` away |
| **2027–2031** | ³He-B labs (Lancaster/Helsinki/RHUL) | F1/F2/F5 cocycle ratio `7.3250` | falsifies the inheritance-universality assignment |
| **2029–2030s** | DESI-5yr → Euclid | `f·σ₈(z)` `−4.058%`; first-sound BAO ring `A_FS = 0.204` (SNR `8.63`) | the **#1 non-CMB falsifier** — zero-parameter, `S₈`-relieving sign |
| **2030** | LiteBIRD | `r, n_T` | Path-H (`0.00745`) vs Path-C (`0.0117`) discriminator via `n_T = −r/8` (the CMB-transferred consistency, not slow-roll) |
| **2030 / 2035** | CMB-S4 / CMB-HD | `α_s` substrate-distance | `~34σ`-reach test of the `s=3` Mellin-residue identity at the matched channel |

**The GW retraction is the flagship of the self-correction record** (`atlas-09`, 53 logged retractions through S110). The framework once headlined a stochastic GW signal for LISA. On audit, the domain-wall contribution is **exactly zero** (`Ω_GW^{walls} = 0`, `π₀(U(1)) = 0`, a topological theorem), and the acoustic peak frequency evaporated to `f_peak ≈ 8.4835×10³⁹ Hz` — **detector-sterile**, `28.9` decades above the entire high-frequency GW program (`S96-OBS-CGWB-PEAK-FREQ`, FAIL). The flagship was **RETIRED**. Crucially the *falsifier did not vanish* — it **relocated** to large-scale structure (`f·σ₈`, first-sound BAO ring), the correct instrument (`falsifier-master-inventory.md` Rows #7.audit-3, #71/#72). A prediction that survives only by being unfalsifiable is worthless; one honestly moved to where it can be tested is the methodology working.

---

## 6. The open technical frontier

A framework is only as credible as its statement of its own boundaries. The capstone §9 enumerates eight; these are the load-bearing ones, at full register precision.

### 6.1 The `a(t)` / effective-Friedmann gap (#1, the load-bearing gap)

The single most important open item: the framework has **no derived, seconds-valued cosmic scale factor `a(t)`** (open question Q13/§VII.BS; capstone §6.3). But the register has sharpened this considerably (S102/S111/S112), and the honest reading is a **HALF-CLOSED / HALF-OPEN-PERMANENT split**, *not* an open deficit confession:

- **What the substrate DETERMINES (PROVEN, zero continuous parameters):** the *conformal class* of the emergent cosmology and **every dimensionless dynamical shape** — every ratio, ordering, tilt, growth shape, and the late-time tracking exponent (`a(t) ∝ t^{2/3}`, the `w=0` dust attractor, `a_exp = 0.6554 ≈ 2/3`, DERIVED not fitted, S101). The `τ`-clock is **PROVEN well-posed**: the (C,E,D) minisuperspace triple closes, the de Sitter relation `Λ = 3H²` holds exactly (`c_track = 3`, residual `2.9×10⁻¹¹`), `τ̇` is sign-definite and monotone, and `Λ = 3H²` is the *unique* reparametrization-invariant scalar (CLOCKLOC1/2/4 PASS, S111 W1).
- **What it does NOT determine (now a PERMANENT external-import boundary):** the **one dimensional normalization** — the overall scale. The substrate measures everything in `M_KK` units, and a system that measures everything in `M_KK` **cannot fix `M_KK` from within** (the self-referential-unit-system no-go, the lattice-QCD scale-setting analog). FAIL-confirmed under *both* readings: the bare-import reading (`M_KK` not `τ`-RG-invariant — `R(τ)` τ-flowing, `Δ_rel = 8.19`, S111 W2) and the substrate-natural reading (`S112-CF-MKK-SUBSTRATE-ANCHOR` FAIL — both candidate anchors reduce to `M_KK·(\text{pure number})`, S112 W1). So `M_KK = 7.4287×10¹⁶` GeV is an **irreducible external import, not a refinable approximation**; `H₀`-tension relief is structurally capped at `49/800 = 6.125%` exactly (the `d_A = +1` odd `M_KK^1` scale leg is parity-inadmissible).

The framing the capstone insists on (and the deepest reason this is a *category statement*, not a discarded obligation): the substrate, not `a(t)`, is fundamental — "space does not expand; spectral complexity grows inside each point," and `H(t)` is the **readout** of that reorganization, not an external clock. This is **Jacobson's 1995 "Einstein equations as equation of state" made microscopic**: the `a₂` moment IS the Einstein–Hilbert action Jacobson recovers thermodynamically, and the framework's own `Z = Σ e^{-S}` is the partition function in question — so a substrate theory is *expected* not to contain a fundamental Friedmann equation. But it still owes a *derived effective* one, and it currently *borrows* the container-observer's FRW `H(t)` for every late-time observable (`w₀`, `w_a`, `σ₈`, the CC tracking). Stated from the transit axis, the missing object is a **back-reaction closure** `H² = f(ρ_relic, S_SA)` — promoting the produced relic energy density into a global expansion rate — not a "Friedmann equation." The T6 FAIL is exactly the statement that the 155,984-mode spectral action cannot be closed against the 8-mode BCS source (a `133{,}200×` overwhelm; S74 W1-E).

**This is one gap, not two.** A *derived, generally-covariant* 4D action for `g_M` would simultaneously be (a) the effective Friedmann map, (b) the emergent equivalence principle, and (c) the emergent Einstein–Infeld–Hoffmann theorem — frontier #8. The framework already holds EIH on the *internal* `K` geometry (S44); what is owed is its lift to the *emergent* `g_M`. Closing one closes both, which *reduces* the dimensionality of the open frontier.

### 6.2 The other open fronts

- **`τ_fold` selection** (assumption A4). The one-loop and variational corridors are **CLOSED-by-FAIL** (`T-STAR-ONELOOP-ORIGIN` FAIL; `NO-WELL-ONE-LOOP` PASS — the action-extremization critical set is empty, S95). The fold location is **REGION van-Hove-SELECTED** (the cusp-crossing `τ_cross = 0.191038` is `L_max`-invariant and regulator-robust, S114) with the value pinned to the two-value non-fungible convention (`19/100` rational anchor vs `0.191038` located feature, §1.5). The route to a *dynamical* selection is now either a mechanism-chain relaxation argument or `τ_fold` stays empirical — BROKEN-with-open-pathway.

- **Functional pluralism / `A_s`** (now a *structural* limitation, S114). The post-transit scalar amplitude `A_s` does **not** admit a substrate-canonical functional selector: the impulse-quench floor is `a₀/a₂`-invariant (`d|β_k|²/d(a₀/a₂) = 0` exact), but the cross-functional spread (impulse-quench / unified / Parker) is `1.2590` OOM with **no scheme-independent normalization** (`CF-S114-AS-FUNCTIONAL-SELECTION` FAIL). So the `A_s`-magnitude-as-a-Planck-comparison-number is a **physical degree of freedom** (FUNCTIONAL-PLURALISM PERMANENT), like the CC ratio — not a convergence-pending number. The floor *inequality* (`A_s ≥ A_s^{BD}`, permanent on 3 axes) and the floor *point* (`A_s = 1.54×10⁻⁸`) are untouched; the *magnitude* over-production (`~1.6×`) is the open tension.

- **SDW convergence** (`JACOBSON-NONLOCAL-64`, the gate *underneath* the CC magnitude). What §2.5 does NOT certify: that the Seeley–DeWitt expansion *converges* (the `a₀`-dominated 114-OOM question). The honest boundary: **ratio-observables (`n_s`, `g₁/g₂`, `R₁ = 1.12865`, `a₂/a₀`) are truncation-robust; absolute-energy observables (CC, `A_s`) are conditional on an SDW-convergence statement that is itself an open gate.** The CC *ratio* is closed by tracking (`1.032`); the CC *absolute* magnitude is held pending convergence — one entangled conditional, not two.

- **Regulator-class questions.** `ζ` vs Pauli–Villars vs Mellin; SCHEMATIC-vs-FULL level pins (`.claude/rules/substrate-first-canonical-sourcing.md`). `n_s` is regulator-class-dependent (sign *and* magnitude, §2.4); `α_s` carries the two scale-separated observables; `σ_8` is regulator-stable. The corpus enforces a per-observable regulator tag precisely because the silent-conflation pathology is real.

- **Family number** (frontier #7). `Ψ₊ = ℂ¹⁶` is one generation; replication is OPEN.

- **Emergent Lorentz invariance / equivalence principle** (frontier #8, INFO not PROVEN). Leading-order universality of free fall is *warranted* (a single emergent light-cone gives all excitations the same cone — weak EP at LO+NLO, `κ_EP = 1.000000` exact); but the S95 genericity review found this is *generic-identity-cored* (the Lichnerowicz `R/4` coefficient of any spin Dirac operator), so the honest promotion language is **"weak EP at LO+NLO is structurally inevitable on the single-operator postulate; value-generic"** — *not* "the substrate uniquely predicts `κ_EP = 1`." A genuine substrate EP *prediction* first appears at NNLO. Worth stating as a strength: the substrate's discreteness is **internal** (the `SU(3)` tower at `M_KK`) and `g_M` is the `a₂` moment of a *continuous* heat-kernel trace, so Hossenfelder's no-go (Poincaré-invariant discrete *spacetime*) does not bite and the LIV/foam-dispersion signatures that bound most QG candidates are structurally absent (`α_LIV = 0` exactly).

### 6.3 Assumed, not proven — the starting geometry

The framework is explicit that its *starting geometry* is an **assumption**, never derived (`atlas-04-assumptions.md`, the ASSUMED rows): the `M⁴ × K` product structure (G1, the KK ansatz); `K = SU(3)` specifically (G2, chosen to reproduce SM charges — vindicated by output, uniqueness OPEN); the Jensen one-parameter family (G3, ridge-confined within the 28-dim space, not forced); the volume-preserving constraint (G6) and left-invariant metric (G7). The atlas tags the cosmological-mapping assumptions BROKEN where they are broken: **C2** (`K_pivot` mapping, BROKEN-WITH-LIVE-RESEARCH-PATHWAY — the load-bearing observational gap), **T3** (GGE permanence, BROKEN — §3.4), **T6** (Friedmann–BCS locking, BROKEN — §6.1). None of this is hidden. *Given* the geometric setup, an enormous amount follows rigorously; the setup itself is a well-motivated choice awaiting a first-principles reason.

---

## 7. Navigating the technical corpus

| If you want… | Go to |
|:--|:--|
| The conceptual on-ramp (read first if new) | `introduction-to-exflation.md` |
| **The whole framework as one equation** (the centerpiece) | `sessions/framework/phonic-exflation-equation.md` (§0–§9; note its §0 status discipline) |
| The 60 load-bearing equations `E1–E60` | `sessions/framework/Atlas/atlas-03-equation-flow.md` |
| **What is proven** | `atlas-07-permanent-results.md` + `sessions/permanent-results-registry.md` (§VII bridges) |
| What is assumed vs proven | `atlas-04-assumptions.md` |
| What is open | `atlas-08-open-questions.md` |
| What was retracted (the honesty leg) | `atlas-09-retractions.md` |
| Closed corridors vs open directions | `atlas-05-walls-doors-windows.md` |
| How the breakthroughs connect | `atlas-10-breakthrough-genealogy.md` |
| The per-pillar build drafts (full derivations) | `sessions/framework/Collabs/equation-build/` |
| The spectral-triple geometry in depth | `sessions/framework/Phononic-Substrate-Geometry.md` |
| The transit / amplification / dark-matter physics | `framework-chaotic-instantons.md`, `framework-parametric-amplification.md`, `framework-dm-properties.md` |
| The substrate-vs-ΛCDM framing discipline | `.claude/rules/phononic-framing.md` |
| The cross-pillar bridge anatomy + promotion | `.claude/rules/cross-pillar-bridge-anatomy.md`, `joint-theorem-promotion.md` |
| The falsifier surface + watchlist | `sessions/framework/registry/falsifier-master-inventory.md`, `falsifier-watchlist.md` |
| What to compute next, and why (EVOI) | `sessions/evoi-framework.md` |
| A variable glossary | `sessions/framework/MathVariables.md` |
| The actual values + provenance | `computations/_shared/canonical_constants.py` |
| Live, queryable state of any claim | the `knowledge` MCP — `search_knowledge`, `get_constant`, `trace_entity` |

---

## In one honest summary

The phonon-exflation framework is **one Dirac operator `D_K(τ)` on Jensen-deformed `SU(3)`, dialed by one modulus `τ`**, whose spectral action (5) delivers — as the `a₀/a₂/a₄` Seeley–DeWitt moments of a single spectrum — the cosmological term, Einstein gravity, and the Standard Model, with the layers' genuine independence a certified theorem (the `R_K′³` Wronskian) and the SM charges, KO-dimension, CPT, and gauge-coupling ratio machine-precision facts of the construction. Its cosmology is **exflation**: a monotone-ramp transit (no potential well) through a van Hove fold, a diabatically-frozen GGE relic (the Ordered Veil — *frozen by speed, not by a now-retracted integrability permanence*), an acoustic white hole resolving the horizon problem, and a dark sector (Leggett-channel quasiparticle DM at `0.7σ`; Volovik tracking-vacuum DE that *locates*, not solves, the cosmological-constant term). Its predictions are pre-registered with real numbers and real gates: a zero-free-parameter robust spine (`Ω_DM h²`, `f·σ₈`, structural `σ/m = 0`, `c_s² = 0`), conditional forecasts in live tension (`n_s` firing against at up to `5σ`; `w₀` at `2.13σ`), a permanent-theorem live wager (`w_a = 0` at `3.43σ`), and a laboratory inheritance falsifier (the `7.3250` cocycle ratio in ³He-B).

Its boundaries are equally real and stated without spin: the **starting geometry is assumed**; the **`a(t)` map is half-closed** — every dimensionless shape fixed, the one dimensional scale `M_KK` a *permanent external import* by a self-reference no-go; several CMB predictions are **scheme-dependent or in live tension**; and the cosmological-constant magnitude is **located, not solved**. The framework's organizing defense is structural: trust the topological outputs (they survive the continuum dissolution), hold the geometric magnitudes pending convergence. Read it as a **bottom-up emergence program**, not a finished theory of everything — take the proven mathematics at full weight, hold the cosmological claims at exactly the confidence the register assigns, and watch the near-term tests (DESI DR3 2027, the ³He-B platforms, LiteBIRD 2030, CMB-S4) that will decide its fate within the decade.

---

*Document status: advanced introductory synthesis, faithful to the register as of June 2026 (~S114). For any live value or status, query the Atlas, the permanent-results registry, the capstone (`phonic-exflation-equation.md`), and the `knowledge` MCP — those are authoritative; this document is not. Every headlined number above was verified against the `knowledge` MCP at authoring time; every claim narrated at or below its register status, with down-tags flagged in-line.*
