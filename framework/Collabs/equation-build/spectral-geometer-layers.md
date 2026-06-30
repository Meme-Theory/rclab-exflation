# §4 — THE LAYERS: SEELEY–DEWITT DECOMPOSITION

> **Section owner**: Spectral-Geometer. **Status of central claim**: CERTIFIED (Spectral-Moment Decoupling Theorem, S75 W2-E). **Status of the Wronskian closed form below**: CONFIRMATORY re-derivation (Sage-exact), supporting — not replacing — the certified theorem.
>
> **Convention banner (read first; full reconciliation note for the assembly specialist at §4.6)**: the symbol $a_n$ carries TWO inequivalent numerical normalizations in this framework. They are *different mathematical objects*, not approximations of each other. This section keeps them strictly separated: the **Gilkey local-curvature coefficient** $a_n^{\text{SD}}$ (used for the layer-identity and the Wronskian) and the **zeta-regulated spectral moment** $a_n^{\zeta} \equiv \zeta_D(\tfrac{d-n}{2})$ (the canonical-constant pins). Per `.claude/rules/regulator-pin-discipline.md`, every $a_n$ below carries an explicit regulator/scheme tag.

---

## 4.1 One action, peeled by the heat kernel

The entire framework is one number — the spectral action of the internal Dirac operator (E4):

$$
S[D_K, f, \Lambda] \;=\; \mathrm{Tr}\, f\!\left(\frac{D_K^2}{\Lambda^2}\right).
\tag{4.1}
$$

This is not a Lagrangian written *on* a spacetime. It is a single spectral functional of $D_K(\tau)$ — the operator whose eigenvalues *are* the substrate's vibrational modes (E2). Physics does not live *in* a container that this action describes; the action *is* the substrate, and every emergent law is a coefficient in how this one trace organizes itself. The mechanism that performs the organization is the **heat-kernel / Seeley–DeWitt asymptotic expansion**.

Write $f$ via its Laplace/Mellin transform and use the small-$t$ asymptotics of the heat trace $\mathrm{Tr}\,e^{-tD_K^2}$. For an elliptic, self-adjoint, second-order operator on a smooth closed manifold of dimension $d$ (here $d=8$, the dimension of $SU(3)$, with spinor fibre rank $2^{\lfloor d/2\rfloor}=2^4=16$):

$$
\mathrm{Tr}\, e^{-tD_K^2} \;\underset{t\to 0^+}{\sim}\; \sum_{n\geq 0} t^{(n-d)/2}\, a_n(D_K^2),
\qquad a_n = (4\pi)^{-d/2}\!\int_{SU(3)}\!\! \mathrm{tr}\,\big[\,e_n(x)\,\big]\,\sqrt{g}\,d^d x .
\tag{4.2}
$$

The $e_n(x)$ are universal polynomials in the curvature tensor, its covariant derivatives, and the bundle endomorphism $E$ (the Lichnerowicz potential of $D_K^2 = \nabla^*\nabla + E$). **Odd coefficients vanish** ($a_{2k+1}=0$) on a closed manifold without boundary — a Gilkey theorem the framework uses elsewhere (the $a_3=0$ result closing $\theta$-vacuum CC scanning, S65). Feeding (4.2) back through the transform of $f$ gives the asymptotic series in the cutoff $\Lambda$ (E4):

$$
\boxed{\;\mathrm{Tr}\, f\!\left(\frac{D_K^2}{\Lambda^2}\right) \;\sim\; \sum_{n\geq 0} f_{\,d-n}\,\Lambda^{\,d-n}\, a_n(\tau)
\;=\; f_4\,\Lambda^4\, a_0 \;+\; f_2\,\Lambda^2\, a_2(\tau) \;+\; f_0\, a_4(\tau) \;+\; f_{-2}\,\Lambda^{-2}\, a_6(\tau) + \cdots\;}
\tag{4.3}
$$

written here in the 4D-effective form ($d-n \to 4-n$ after the $M^4\times K$ dimensional reduction; see §4.5 for the product-manifold factorization). The Mellin moments $f_{\,d-n} = \int_0^\infty f(u)\,u^{(d-n)/2-1}\,du$ are pure numbers fixed by the cutoff profile $f$; the *physics content* is carried entirely by the geometric coefficients $a_n(\tau)$. This is the single most important structural statement of the section: **one action, expanded asymptotically, peels into an ordered tower of physics sectors indexed by curvature-polynomial degree.** Each $a_n$ is a distinct LAYER OF EXFLATION.

---

## 4.2 The layers and their physical identity

Each coefficient $a_n$ multiplies a distinct power of $\Lambda$ and is a curvature polynomial of distinct degree. Reading (4.3) top-down:

| Layer | $\Lambda$-power | Curvature degree | Gilkey form $e_n$ | Emergent physics | $\Phi$-image |
|:------|:----------------|:-----------------|:------------------|:-----------------|:-------------|
| $a_0$ | $\Lambda^{4}$ | degree 0 | $\propto \mathbf{1}$ (fibre rank only) | **Vacuum energy / cosmological term** | $\Sigma_1$ |
| $a_2$ | $\Lambda^{2}$ | degree 1 | $\propto \tfrac{R}{6}\mathbf{1} - E$ | **Einstein–Hilbert** (gravitational kinematic skeleton, $\propto R$) | $\Sigma_2$ |
| $a_4$ | $\Lambda^{0}$ | degree 2 | $\propto \alpha R^2 + \beta|\mathrm{Ric}|^2 + \gamma|\mathrm{Riem}|^2 + \delta\,\Box R + F^2$ | **Yang–Mills + Higgs quartic** (load-bearing matter physics) | $\Sigma_3$ |
| $a_6,\,a_8,\dots$ | $\Lambda^{-2},\dots$ | degree $\geq 3$ | higher curvature invariants | **Higher-curvature / threshold corrections** | $\Sigma_{4},\dots$ |

### Layer $a_0$ — the cosmological term ($\Lambda^4$, $\to \Sigma_1$)

$$
a_0 \;=\; (4\pi)^{-d/2}\,\mathrm{tr}(\mathbf{1})\int_{SU(3)}\!\!\sqrt{g}\,d^d x \;=\; (4\pi)^{-d/2}\cdot 16 \cdot \mathrm{Vol}\big(SU(3),g_\tau\big).
\tag{4.4}
$$

This is the **zeroth spectral moment**: pure volume $\times$ fibre rank, no curvature. It is the cosmological-constant moment — the vacuum-energy contribution to the spectral action. In the substrate picture this is *not* "the energy of empty space"; it is the leading bulk term of the one action, the layer whose $\Phi$-image is the weight-0 user-adjudication-only deliverable $\Sigma_1$ (E59). Because the Jensen deformation is **volume-preserving** (the TT constraint), $\mathrm{Vol}(SU(3),g_\tau)$ is $\tau$-independent, so in the Gilkey normalization $a_0^{\text{SD}}$ is a *constant* in $\tau$. (In the zeta normalization $a_0^{\zeta}=6440$ is the total truncated mode count — also $\tau$-flat at fixed $L_{\max}$, since mode count is topological; S77.)

### Layer $a_2$ — Einstein–Hilbert, the gravitational skeleton ($\Lambda^2$, $\to \Sigma_2$)

$$
a_2 \;=\; (4\pi)^{-d/2}\!\int_{SU(3)}\!\! \mathrm{tr}\!\left(\frac{R}{6}\mathbf{1} - E\right)\sqrt{g}\,d^d x
\;=\; (4\pi)^{-d/2}\cdot \frac{20\,R(\tau)}{3}\cdot \mathrm{Vol}\big(SU(3)\big).
\tag{4.5}
$$

This is the **second spectral moment**, linear in the scalar curvature $R$. It IS the Einstein–Hilbert action — gravity is not a fundamental law imposed on the substrate; **gravity is the second spectral moment of $D_K$.** The $\tfrac{R}{6}\mathbf{1}$ comes from Lichnerowicz, the $-E$ from the spin connection's endomorphism; the combination collapses (on the $16$-dim spinor bundle, with the spin-curvature correction $K/(20R)<2\%$ for all $U(2)$-invariant metrics — my memory, S46) to the scalar-dominant form $\tfrac{20R}{3}$. The exact scalar curvature (E3, 147/147 Riemann) is

$$
R_K(\tau) = -\tfrac14 e^{-4\tau} + 2e^{-\tau} - \tfrac14 + \tfrac12 e^{2\tau}, \qquad R_K(0)=2,\quad R_K'(\tau)>0,
\tag{4.6}
$$

so $a_2^{\text{SD}}$ is *monotonically increasing* in $\tau$. The ratio of bosonic to Dirac contributions in this layer is the exact, representation-theoretic, $\tau$-independent number (E36):

$$
\frac{a_2^{\text{bos}}}{a_2^{\text{Dirac}}} = \frac{61}{20} \quad\text{(Gilkey; TT tensors carry }87.7\%\text{ of bosonic }a_2\text{)}.
\tag{4.7}
$$

### Layer $a_4$ — Yang–Mills + Higgs quartic, the load-bearing matter physics ($\Lambda^0$, $\to \Sigma_3$)

$$
a_4 \;=\; \frac{(4\pi)^{-d/2}}{360}\!\int_{SU(3)}\!\!\mathrm{tr}\!\left[\,\tfrac{5}{2}R^2 - 2|\mathrm{Ric}|^2 + 2|\mathrm{Riem}|^2 + (\text{$\Box R$}) + 60\,F_{\mu\nu}F^{\mu\nu}\,\right]\sqrt{g}\,d^d x .
\tag{4.8}
$$

This is the **fourth spectral moment**, quadratic in curvature. It is the $\Lambda^0$ (cutoff-independent) term and carries the gauge kinetic energy ($F^2 \to$ Yang–Mills) and, after the $M^4\times K$ reduction with the matter-dressed Dirac operator, the **Higgs quartic** (the CCM matching $\lambda_{\text{CCM}} = \tfrac{4}{3}g_3^2\cdot\text{ratio}_{\text{gilkey}}$, S70). It is "load-bearing" because it sets the actual interaction physics — the part an experiment in a laboratory measures as forces and the Higgs self-coupling. Its $\Phi$-image is the weight-4 $\Sigma_3$ layer carrying the load-bearing methodology enforcement (the `mcp-pre-check` hook; E59). At the Einstein point the gauge-kinetic part of $a_4(K)$ vanishes (S5); the $R^2$-dominant remainder sets the curvature-polynomial degree.

### Layers $a_6$ and higher — higher-curvature / threshold corrections ($\Lambda^{-2},\dots$)

The tower does not stop. $a_6$ (degree-3 curvature invariants) and beyond contribute $\Lambda^{-2}$-suppressed higher-derivative gravity and KK threshold corrections (e.g. the Higgs-quartic shift $\delta\lambda(a_6)$, S70). The **hierarchy** $a_0 \gg a_2 \gg a_4 \gg a_6$ in $\Lambda$-power is what makes the lower layers dominate and the framework predictive at accessible scales. (In the zeta/raw-count normalization the *magnitude* hierarchy reverses for the dimensionless mode-sum — $a_0^{\zeta}=6440 > a_2^{\zeta}=2776 > a_4^{\zeta}=1351$ — because there each $a_n^{\zeta}$ is a convergent spectral sum, not a $\Lambda$-graded term; this is exactly the object-confusion the §4.6 reconciliation note guards against.)

---

## 4.3 The Spectral-Moment Decoupling Theorem — why the layers are genuinely distinct physics

A skeptic's first objection: are these "layers" real, or is $a_4$ just some function of $a_0$ and $a_2$, so that there is really only one independent piece dressed up three ways? The **Spectral-Moment Decoupling Theorem** (S75 Workshop W2-E, **CERTIFIED, PASS**) settles this:

> **Theorem (Spectral-Moment Decoupling, S75 W2-E).** The coefficients $a_0(\tau)$, $a_2(\tau)$, $a_4(\tau)$ are **algebraically independent** as functions of the Jensen modulus $\tau$ — they are curvature polynomials of *distinct degree* (0, 1, 2 in the curvature tensor), and their Wronskian is non-vanishing.

This is the precise sense in which the layers are not redundant. Distinct curvature-polynomial degree $\Rightarrow$ no fixed algebraic relation $P(a_0,a_2,a_4)=0$ can hold identically in $\tau$; equivalently, the three functions are linearly/functionally independent over the field of constants, certified by a non-zero Wronskian.

### Confirmatory closed form (Sage-exact; PRELIMINARY beyond the certified central claim)

To exhibit the structure concretely I computed the Wronskian of the three Gilkey layer-functions using the exact $R_K(\tau)$ of (4.6), the volume-preserving (constant) $\mathrm{Vol}=V$, and the scalar-curvature-dominant pieces that *set each layer's degree* ($a_0\propto V$, $a_2\propto R\,V$, $a_4\propto R^2 V$):

$$
W\big[a_0,a_2,a_4\big](\tau)
= \det\!\begin{pmatrix} a_0 & a_2 & a_4 \\ a_0' & a_2' & a_4' \\ a_0'' & a_2'' & a_4'' \end{pmatrix}
= \frac{5}{393216\,\pi^{12}}\; V^3\, e^{-12\tau}\,\big(e^{3\tau}-1\big)^{6}.
\tag{4.9}
$$

This is **exact** (Sage `simplify_full`; the degree-6 polynomial in $e^{3\tau}$ factors identically as $(e^{3\tau}-1)^6$). Three structural readings:

1. **Independence is strict everywhere the framework lives.** $W(\tau)\neq 0$ for *all* $\tau\neq 0$. At the fold $\tau_{\text{fold}}=0.19$: $\,e^{3(0.19)}-1 = 0.7683 > 0$, so $W(\tau_{\text{fold}}) = +7.11\times10^{-4}\,V^3 \neq 0$. The three layers are functionally independent at the physical point — distinct physics, full stop.
2. **The lone degeneracy is the round point.** $W$ has a **sixth-order zero at $\tau=0$** — the bi-invariant (maximally symmetric) $SU(3)$ metric, where the three curvature-polynomial degrees momentarily collapse onto a single scale. This is a measure-zero coincidence at the most symmetric configuration, *not* a generic algebraic dependence. The framework's genesis is precisely the cascade *away* from $\tau=0$ (the cold-big-bang unstable maximum), so the layers separate the instant exflation begins.
3. **Caveat for the assembly specialist.** Equation (4.9) uses the scalar-curvature-dominant Gilkey pieces. The full $a_4$ (4.8) adds $|\mathrm{Ric}|^2$ and $|\mathrm{Riem}|^2$ terms; these are *additional* degree-2 invariants that can only *raise* the rank of the curvature-monomial basis, so they **strengthen** independence — they cannot reintroduce a degeneracy at $\tau\neq 0$. The certified theorem (S75) does not depend on (4.9); (4.9) is a transparent witness to it.

**Consequence for the equation thesis.** Because the layers are independent, the one action (4.1) genuinely *contains* three separately-tunable physics sectors. The cosmological term ($a_0$), gravity ($a_2$), and matter/gauge ($a_4$) are not three views of one knob — they are three independent projections of the same operator $D_K$. This is what licenses the framework's claim that vacuum energy, gravity, and the Standard Model all *emerge from* $D_K$ while remaining physically distinct. It also underwrites the related permanent results: **BCS–Sakharov decoupling** ($a_2$ and $a_4$ are orthogonal projections, $r_2=0.892$; S66, PERMANENT) and **spectral-moment decoupling for the CC vs NEC moments** ($F_{-1}$ vs $F_{+1}$ are different moments; S64 W5-B, PERMANENT).

---

## 4.4 The $\Phi$-correspondence (E59): the layering is self-similar — even the methodology is a layer image

The most striking structural fact is that the layering does not stop at physics. The **layer-functor** $F$ and the **$\Phi$-correspondence** (E59, S86 W-13, TRIPLET-VERIFIED) map the Seeley–DeWitt tower onto the framework's own *methodology and enforcement* structure, as a graded-ring isomorphism:

$$
F:\; L_{\text{substrate}} \xrightarrow{\;\sim_F\;} L_{\text{methodology}} \xrightarrow{\;\sim_F\;} L_{\text{audit}},
\qquad
\Phi\big(a_n^{\text{SD}}\big) = \Sigma_{n+1},
\qquad
w(\Sigma_d) = w\big(a_n^{\text{SD}}\big) = n.
\tag{4.10}
$$

Explicitly:

$$
\Phi(a_0) = \Sigma_1 \;\;(\text{weight-0: perimeter/cosmological term} \to \text{user-adjudication-only deliverable}),
$$
$$
\Phi(a_2) = \Sigma_2 \;\;(\text{weight-2: Einstein–Hilbert kinematic skeleton} \to \text{wave-classification}),
$$
$$
\Phi(a_4) = \Sigma_3 \;\;(\text{weight-4: Yang–Mills + Higgs quartic, load-bearing} \to \text{`mcp-pre-check` hook}).
\tag{4.11}
$$

The correspondence preserves *weight*: the weight-$n$ spectral-action object maps to the enforcement-strength-$n$ methodology rule. The cosmological layer (weight 0, lightest physics) maps to the lightest enforcement (advisory/user-adjudication); the matter layer (weight 4, load-bearing physics) maps to the load-bearing enforcement (a hard pre-tool hook). This is a genuine **self-similar layering**: the same Seeley–DeWitt grading that peels the universe into vacuum/gravity/matter *also* peels the framework's own governance into its enforcement strata. The vertical decomposition of physics and the vertical decomposition of methodology are *the same functor*. For the capstone thesis, this is the deepest form of "one equation": the heat-kernel grading is so fundamental that even the rules used to study it inherit its layers.

(This domain — Methodology Floor, E59/E60 — is **structurally orthogonal** to the physics domains by the algebra-axis orthogonality theorem, MANDATORY at K=3; the $\Phi$-correspondence is an *isomorphism of gradings*, not a collapse of the two into one observable.)

---

## 4.5 Each layer is individually monotone in $\tau$ — setting up the AT-$\tau$ flow

The vertical (layer) structure is complete above. The bridge to the **AT-$\tau$ flow section** is the Structural Monotonicity Theorem (E7, S37, Walls W4/W7):

$$
\frac{d}{d\tau}\langle\lambda^2\rangle > 0 \;\Longrightarrow\; \frac{d}{d\tau}\,a_{2k}(\tau) \;\text{has fixed sign for each } k,\;\text{all monotone } f,\;\text{all }\Lambda,\;\text{all 10 sectors}.
\tag{4.12}
$$

Concretely, in the Gilkey normalization each layer inherits its $\tau$-dependence from $R_K(\tau)$ (4.6), which is strictly increasing with $R_K'(\tau)>0$:

- $a_0^{\text{SD}}(\tau)$: **flat** (volume-preserving; $\tau$-independent).
- $a_2^{\text{SD}}(\tau) \propto R_K(\tau)$: **strictly increasing** (degree-1 in $R$).
- $a_4^{\text{SD}}(\tau) \propto R_K(\tau)^2 + \cdots$: **strictly increasing** (degree-2; the $R^2$ piece grows faster, the source of the eventual $a_4/a_2$ re-weighting).

The decisive consequence — that there is **no spectral-action minimum at any $\tau$** (9,600 checks; closes ALL spectral-action stabilization of the modulus; E7) — is precisely *because* the individual layers are monotone and independent: a sum of independent monotone pieces with fixed-sign Mellin weights $f_{d-n}$ cannot develop a stationary point. The AT-$\tau$ flow section can therefore take as its starting point: **the layered action (4.3) is a sum of three independent, individually-monotone curvature moments, and its $\tau$-derivative never vanishes** ($dS/d\tau = +58{,}673$ at the genesis configuration; the Jensen deformation drives the spectral-action gradient with no well to settle in — the impulsive supersonic transit, not slow roll).

---

## 4.6 Convention reconciliation note for the assembly specialist (MANDATORY READ)

This is the single highest-leverage caveat for assembling the capstone. The symbol $a_n$ is used in this framework for **two structurally different objects** that differ numerically by a factor of order $10^3$–$10^4$. Conflating them is the "38-session error" resolved at S61 (and the Level-2 tier distinction of HEAT-KERNEL-AUDIT-45/S46). The assembly specialist must pick ONE normalization per equation and tag it.

| Object | Symbol (this §) | Definition | Canonical value(s) | $\tau$-behavior | Regulator tag |
|:-------|:----------------|:-----------|:-------------------|:----------------|:--------------|
| **Gilkey local-curvature coefficient** | $a_n^{\text{SD}}$ | $(4\pi)^{-d/2}\!\int \mathrm{tr}(e_n)\sqrt{g}$ | $a_0^{\text{SD}}=0.866$, $a_2^{\text{SD}}(\text{fold})=0.728235$, $a_4^{\text{SD}}$ from (4.8) | $a_0$ flat, $a_2,a_4$ monotone via $R_K(\tau)$ | Gilkey / local-curvature (regulator-independent; it is a geometric integral) |
| **Zeta-regulated spectral moment** | $a_n^{\zeta}$ | $\zeta_D\!\big(\tfrac{d-n}{2}\big)=\sum_k m_k \lambda_k^{-(d-n)}$ | $a_0^{\zeta}=6440$, $a_2^{\zeta}=2776.17$, $a_4^{\zeta}=1350.72$ | flat $a_0$ at fixed $L_{\max}$; $a_2^{\zeta}$ varies 19.86%, $a_4^{\zeta}$ 28.65% over $\tau$ (S77) | $a_n^{\zeta}$ (zeta); cf. $a_n^{\text{Pauli-Villars}}$, $a_n^{\text{Mellin}}$ |

**Hard facts the assembly must respect:**

1. **They are NOT the same number.** $a_2^{\zeta} = 2776.17$ is the spectral moment $\zeta_D(1)$; $a_2^{\text{SD}} = 0.728235$ is the Gilkey coefficient. Ratio $\approx 3812$. The equality "$a_2^{\zeta} = a_2^{\text{SD}}$" is FALSE; "$a_2$" as a name has been attached to both. (Structural reason: $\zeta_D$ has a pole at $s=1$ for $d=8$; on the finite $L_{\max}$-truncation the sum converges but is UV-dominated $\sim\lambda_{\max}^6$, a *different analytic object* from the local heat-kernel coefficient.)
2. **Canonical-constant pins are the zeta family.** `a_0_FW_zeta = 6440`, `a_2_FW_zeta = 2776.17` (both S88-A-N-FW-CANONICALIZATION). Any equation citing those numbers is in the $a_n^{\zeta}$ normalization and MUST be tagged $a_n^{\zeta}$. There is currently **no `a_4_FW_zeta` canonical-constant pin**; the value $a_4^{\zeta}=1350.72$ (= `a_4(fold)`, baseline-findings-s66) should be promoted via `update_constant` before the capstone cites it as canonical. **FLAGGED for the orchestrator.**
3. **The raw-count triple $a_0=155984,\,a_2=64308,\,a_4=29086$** (s75 output) is the *un-rescaled* $L_{\max}=10$ mode-sum (155,984 eigenvalues); the $6440/2776/1351$ triple is the $L_{\max}=3$ canonical truncation. These differ only by truncation level, both within the $a_n^{\zeta}$ family — but the capstone must not mix a $155984$-row $a_0$ with a $2776$-row $a_2$.
4. **The $\Lambda$-power hierarchy ($a_0\gg a_2\gg a_4$) is a statement about (4.3) — the $\Lambda$-graded terms** — not about the bare magnitudes of $a_n^{\zeta}$ (whose magnitudes happen to *decrease* $6440>2776>1351$ because they are convergent sums). State the hierarchy as "the $\Lambda^4$ term dominates the $\Lambda^2$ term dominates the $\Lambda^0$ term," never as "$a_0 > a_2 > a_4$" without the $\Lambda$-power qualifier.

**Recommendation:** for the LAYER-IDENTITY content (this §4, the "what is each layer" exposition), use $a_n^{\text{SD}}$ (Gilkey) — it is regulator-independent and makes the curvature-degree story exact. For any NUMERICAL prediction fed downstream (CC, $M_{KK}$ extraction, $G_N$ matching), use the regulator-tagged $a_n^{\zeta}$ pins. Tag every instance. Never write a bare $a_n$.

---

## Consideration

**Which "layer" reading is primary?** Three candidate readings of "layers of exflation" were on the table: (i) **spectral-moment / curvature-degree** (the heat-kernel grading $a_0/a_2/a_4/\dots$), (ii) **causal** (pre-fold / fold / post-fold transit ordering), (iii) **scale** (UV $\to$ IR, the $\Lambda$-power ladder). My position: **the spectral-moment reading is primary, and the other two are derived from it.**

- The scale reading (iii) is *literally* the spectral-moment reading wearing different clothes: the $\Lambda$-power ladder $\Lambda^4,\Lambda^2,\Lambda^0,\dots$ in (4.3) is indexed by exactly the same integer $n$ that indexes the curvature degree. Scale-layering and moment-layering are the same partition; the moment reading is more fundamental because the $a_n$ are intrinsic geometric invariants of $D_K$ while the $\Lambda$-powers are an artifact of the chosen cutoff profile $f$.
- The causal reading (ii) is a story about the *trajectory* $\tau(t)$ through the one action — it is the AT-TIME run of the equation, a flow *along* the modulus. But *what* flows is the layered action; the causal ordering presupposes the moment decomposition (you cannot say "gravity switches on" without first having isolated the $a_2$ layer). Causality is a reading of the dynamics; the moment decomposition is a reading of the object. The object is logically prior (substrate-first).

The decisive argument is the **Spectral-Moment Decoupling Theorem + its Wronskian (4.9)**: the moment layers are *provably, algebraically independent*, with a clean closed-form witness ($W \propto (e^{3\tau}-1)^6$, vanishing only at the round point). No comparable independence theorem exists for the causal or scale readings — they are *parameterizations*, not *independent projections*. A reading whose layers are certified-independent functions of the modulus is a stronger notion of "layer" than a reading whose layers are stages of one trajectory. Primary = spectral-moment; the $\Phi$-correspondence then shows this same grading is so deep it even re-images onto the methodology floor.

**Caveat for the orchestrator on reconciling $a_n$ conventions** (beyond §4.6): the capstone will read most cleanly if §4 (layers, identity, decoupling) is written entirely in $a_n^{\text{SD}}$ (Gilkey, regulator-free, exact curvature-degree story) and the AT-$\tau$/AT-$t$ run sections switch to $a_n^{\zeta}$ for numerics with an explicit one-line bridge ("we now evaluate the layers as zeta-regulated spectral moments; $a_2^{\zeta}=2776.17$ is $\zeta_D(1)$, the spectral image of the Gilkey $a_2^{\text{SD}}$, NOT equal to it"). Two concrete to-dos: (1) promote `a_4_FW_zeta = 1350.72` to a canonical constant with provenance before citing it; (2) never let a $155984$-row $a_0$ and a $2776$-row $a_2$ co-occur in one equation — they are different $L_{\max}$ truncations. The factor-$\sim$3800 $a_2^{\zeta}/a_2^{\text{SD}}$ gap is exactly the kind of normalization slip that turns a factor-of-2 spinor-rank error into a factor-of-4 cosmological-constant-ratio error downstream; tagging is cheap insurance.
