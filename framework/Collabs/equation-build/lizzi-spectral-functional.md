# §3 — THE SPECTRAL FUNCTIONAL *f* AND THE CUTOFF

> **Section author**: lizzi-spectral-functional-theorist (spectral-functional / NCG-regularization axis)
> **Spine**: E4 (master action) · E38 (CM-1995 residue formula) · E58 (Mellin-strip / convergence-cone) · E59/E60 (regulator-class structure)
> **Canonical anchors** (all `get_constant`-verified): `a_0_FW_zeta = 6440.0`, `a_2_FW_zeta = 2776.165389`, `a4_fold = 1350.72`, `M_KK = 7.428660036284456e16` GeV, `Lizzi_signature = 1.12865`, `mellin_f_star_f0 = 0.08832`, `f_0_sharp = 1.0`.

---

## 3.0 What this section owns

The master equation of §1 is a **bare trace**:

$$
S[D_K, f, \Lambda] \;=\; \mathrm{Tr}\, f\!\left(\frac{D_K(\tau)^2}{\Lambda^2}\right) \;+\; \langle\psi | D_K | \psi\rangle .
$$

A bare trace is not yet physics. The eigenvalue spectrum $\{\lambda_k, m_k\}$ of $D_K(\tau)$ is a fixed substrate datum (the 155,984 modes at $L_{\max}=10$); but the *number* the trace returns depends entirely on **how the high modes are weighted and where the sum is cut**. The function $f$ and the scale $\Lambda$ are precisely that weighting-and-cutting prescription. This section establishes:

1. how the moments of $f$ — the numbers $f_4, f_2, f_0$ — distribute themselves across the substrate's spectral layers $a_0, a_2, a_4$, and why the result is finite on the finite triple (§3.1);
2. that the choice of $f$ (zeta vs cutoff vs anomaly-derived) is a **physical degree of freedom**, not a mathematical convenience — different functionals weight the same spectrum differently and produce *different physics* (§3.2);
3. the cosmological-constant subtlety: which spectral moment the vacuum energy actually lives in, and why that question is regularization-sensitive (§3.3);
4. the Mellin / convergence-cone structure that fixes *which* moments are allowed to survive at all (§3.4).

The substrate-first posture is non-negotiable here. **The functional is a property of the substrate's own spectrum, not an external choice imposed on a container.** $f$ does not "act on" $D_K$ from outside; the admissible $f$'s are exactly those whose Mellin transform is supported on the pole set the spectrum itself dictates (§3.4). We choose among them; the spectrum decides which are even candidates.

---

## 3.1 The role of $f$ and the cutoff $\Lambda = M_{KK}$

### The heat-kernel layering

For a smooth, positive cutoff function $f$ with rapid decay, the Chamseddine–Connes spectral action admits the asymptotic expansion (Chamseddine–Connes 1997, `researchers/Phonon-First/08_1997_Chamseddine_Connes_Spectral_Action.md`; Connes–Chamseddine–Marcolli 2007, `09_2007_Chamseddine_Connes_Marcolli_Gravity_SM.md`):

$$
S_b[D_K, f, \Lambda] \;=\; \mathrm{Tr}\, f\!\left(\frac{D_K^2}{\Lambda^2}\right)
\;\sim\; 2 f_4\,\Lambda^4\, a_0(D_K^2) \;+\; 2 f_2\,\Lambda^2\, a_2(\tau) \;+\; f_0\, a_4(\tau) \;+\; \mathcal{O}(\Lambda^{-2}).
\tag{E4}
$$

The structure splits cleanly into two factors per layer:

| Layer | Substrate factor (spectral moment) | Functional factor (moment of $f$) | Cutoff power | Emergent physics |
|:------|:-----------------------------------|:----------------------------------|:-------------|:-----------------|
| $a_0$ | $a_0 = \int\!\sqrt{g}\,d^4x \cdot 1$ — total spectral weight | $f_4 = \tfrac12\!\int_0^\infty u\, f(u)\, du$ | $\Lambda^4$ | cosmological term |
| $a_2$ | $a_2 = \tfrac{1}{12}\!\int\!\sqrt{g}\,d^4x\, R$ — Einstein–Hilbert | $f_2 = \int_0^\infty f(u)\, du$ | $\Lambda^2$ | Newton coupling $G_N$ |
| $a_4$ | $a_4$ — Yang–Mills $+$ Higgs quartic | $f_0 = f(0)$ | $\Lambda^0$ | gauge $+$ Higgs sector |

The **moments of $f$** are the Mellin transform of $f$ evaluated at the half-integers (`s86-cutoff-sqrt-gate-abc-trio.md`, AL2010 prescription):

$$
f_{2k} \;=\; \mathcal{M}[f](k) \;=\; \int_0^\infty x^{\,k-1}\, f(x)\, dx \quad (k = 1, 2, 3,\ldots), \qquad
f_0 \;=\; \mathrm{Res}_{s=0}\,\mathcal{M}[f](s).
$$

This is the precise sense in which $f$ "weights the layers": $f_4$ multiplies the perimeter/vacuum layer, $f_2$ the gravity layer, $f_0$ the gauge/Higgs layer. **The substrate supplies the $a_{2k}(\tau)$; the functional supplies the $f_{2k}$; the cutoff supplies the $\Lambda^{4-2k}$ tower.** Three independent inputs, multiplied layer by layer.

### Why $\Lambda = M_{KK}$

The cutoff is not a free knob. It is the geometric scale at which the Kaluza–Klein tower of the internal $SU(3)$ fiber becomes dense — the natural ultraviolet scale of the substrate itself. Canonically

$$
\Lambda \;=\; M_{KK} \;=\; 7.428660036284456\times 10^{16}\ \mathrm{GeV}
$$

(`get_constant("M_KK")`). This is *substrate-IS*, not imposed: $M_{KK}$ is set by the fiber spectrum, the same $D_K$ eigenvalues that fill the trace. Setting $\Lambda$ anywhere else would mean cutting the substrate's modes at a scale foreign to the substrate's own geometry.

### Why the action is well-defined on the finite triple

The asymptotic expansion (E4) is, strictly, an $\Lambda\to\infty$ statement on a manifold. The framework's spectral triple is **finite** at any working truncation $L_{\max}$ ($D_K$ is block-diagonal in Peter–Weyl, E6; the bottom-20 are $L_{\max}$-saturated by Friedrich–Bär, E39). On a finite triple the trace $\mathrm{Tr}\, f(D_K^2/\Lambda^2) = \sum_k m_k\, f(\lambda_k^2/\Lambda^2)$ is a **finite sum** and therefore manifestly well-defined for *any* $f$ — no regularization needed to make the sum converge. Regularization re-enters only when one asks for the *moments* $a_{2k}$ as residues (§3.4): the moments are residues of $\zeta_{D_K}(s) = \sum_k m_k\lambda_k^{-2s}$, and which residues exist is a property of the finite spectrum's Mellin structure (E37, E38). The finite triple is what makes the bare action trivially finite; the *moment decomposition* is what makes it physics.

### The bare moment values (zeta, per-branch, $L_{\max}=3$)

$$
a_0 = 6440.0, \qquad a_2 = 2776.165389, \qquad a_4 = 1350.72.
$$

Dimensionless ratios (Sage-exact):

$$
\frac{a_2}{a_0} = 0.43108\ldots, \qquad \frac{a_4}{a_0} = 0.20974\ldots, \qquad \frac{a_4}{a_2} = 0.48654\ldots
$$

These three numbers, and especially the **dimensionless combination** built from them in §3.3 (the Lizzi signature $R_1$), are the part of the spectral action that survives stripping away $\Lambda$ and the choice of $f$. They are the substrate-IS skeleton.

---

## 3.2 The choice of spectral functional as a physical degree of freedom

This is the section's central claim, and my specialty.

### Three families, one spectrum

Given the *same* fixed $\{\lambda_k, m_k\}$, at least three structurally distinct prescriptions turn the bare trace into an action:

- **Cutoff** $S_{\text{cutoff}} = \mathrm{Tr}\, f(D_K^2/\Lambda^2)$ with a smooth profile such as $f(x)=\sqrt{x}$ (the framework's working choice), $e^{-x}$, or a sharp $\Theta(\Lambda-|D|)$. This is the Chamseddine–Connes functional. **UV-dominated.**
- **Zeta** $S_\zeta = \zeta_{D_K}(0) = a_4(D_K^2)$ — the spectral action *defined as the zeta value at $s=0$*, which equals the $a_4$ moment alone and **eliminates the $a_0$ cosmological term entirely** (Connes–Marcolli; framework `session-65-lizzi-synthesis.md`). **IR-dominated.**
- **Anomaly-derived** $S_{\text{anom}} = c_0(\phi)\,a_0 + c_2(\phi)\,a_2 + c_4(\phi)\,a_4$, where the coefficients $c_{2k}$ are *forced* by fermionic anomaly cancellation rather than postulated (Andrianov–Lizzi 2010, `researchers/Lizzi/02_2010_Andrianov_Bosonic_Spectral_Action_Anomaly.md`, arXiv:1103.0478). The bosonic action is *derived*, not chosen — but it carries a dilaton $\phi$ that selects a one-parameter sub-family.

### Different functionals weight the layers differently — and produce different physics

This is not a cosmetic re-labeling. The same spectrum, read through different functionals, gives **opposite signs** on the key cosmological observable. The Hubble slow-roll parameter $\varepsilon_H$ (a pure spectral *shape* parameter, FI under uniform rescaling — `EPS_H CANCELLATION THEOREM`, S68) flips sign:

| Functional | $\varepsilon_H$ (S66) | $n_s$ | Tilt | $m_H$ (S75) |
|:-----------|:----------------------|:------|:-----|:------------|
| cutoff $\sqrt{x}$ | $+0.02163$ | $0.957$ | **red** | $127.5$ GeV |
| zeta $a_4$ | $-0.04485$ | $1.090$ | **blue** | $138.5$ GeV (79σ exclusion) |
| anomaly $\phi$ | $+0.0176$ | $0.9649$ | — | $102.0$ GeV |

The sign of $\varepsilon_H$ — whether the CMB tilt is red (observed) or blue — is **set by the regularization scheme, not by the spectrum.** This is the empirical heart of "regularization is physics."

Two permanent theorems of mine fix the boundaries of this landscape:

- **ANOMALY-FAMILY EXCLUSION (S67, permanent).** For $S_{\text{anom}}=\sum c_{2k}(\phi)\,a_{2k}$ with $c_{2k}>0$ (anomaly-forced positive) and $da_{2k}/d\tau<0$ at the fold (geometric), one has $dS/d\tau<0$ for *all* $\phi>0$, hence $\varepsilon_H<0$ and $n_s>1$ (blue) **universally**. The observed red tilt structurally excludes the entire anomaly-derived family. The framework's working cutoff $f(x)=\sqrt{x}$ is *not* in the anomaly family — it is the escape.
- **ZETA-NOT-PHYSICAL (S75, permanent).** $\zeta_{D_K}(s)$ at any fixed $s$ imposes a UV weighting $|\lambda|^{-2s}$ that is *not determined by the spectrum*. Six functionals span a $381\times$ dynamic range on $\varepsilon_H$-class observables; analytic-continuation non-uniqueness alone is $5.89\%$. The lesson: **absolute spectral-moment values are scheme-artifacts; only ratios of spectral moments under a *fixed* regulator are physical** (`UV_REGULARIZATION_CONFLATION`).

### What survives all choices — the FI / RD partition

My operational test (`session-85-s7-combined-landscape-lizzi.md`) classifies every observable $O$ against the 5-regulator atlas $A_5 = \{\zeta,\ \mathrm{Zubarev},\ \mathrm{SDW},\ \mathrm{cutoff\_sqrt},\ \mathrm{anomaly}\}$:

$$
\mathcal{M}_{\text{lizzi}}(O) = \mathrm{FI}\ \ (\text{Functional-Invariant}) \iff \text{drift across } A_5 \le 5\%; \qquad \mathrm{RD}\ \ (\text{regulator-dressed}) \text{ otherwise.}
$$

- **FI (structural — survives all choices):** ratios of two spectrum-sums under the *same* regulator (the regulator cancels at leading order). Examples: the sound speed $c_s$, the rank-drift exponent (FI to sub-percent, S78), the Lizzi signature $R_1$ (§3.3), and the HP$^1$ cohomology norm on the pure-$a_4$ family $F_4=\{\zeta,\mathrm{Zubarev},\mathrm{SDW}\}$ (factor $1.031$ — the strongest scheme-invariance harvest in the project, S86).
- **RD (scheme-dependent — a physical degree of freedom to be fixed by experiment or consistency):** $\varepsilon_H$ sign, $n_s$ value, $m_H$ landscape, absolute vacuum energy. These *depend* on $f$ and therefore must be *determined*, not assumed.

### The regulator-class tagging discipline (mandatory)

Because the moment value depends on the regulator, **bare $a_n$ is forbidden going forward** (`.claude/rules/regulator-pin-discipline.md`). Every citation of a Seeley–DeWitt coefficient carries a superscript tag:

$$
a_n^{\zeta}, \quad a_n^{\text{Pauli-Villars}}, \quad a_n^{\text{Mellin}}, \quad a_n^{\text{lattice}}, \quad a_n^{\text{cutoff}}.
$$

A bare $a_n$ silently inherits the calling context's regulator — a Class-8 PRU vulnerability. The canonical moments above are therefore properly written $a_0^\zeta = 6440.0$, $a_2^\zeta = 2776.165389$, $a_4^\zeta = 1350.72$. A parallel **level-pin** (`.claude/rules/substrate-first-canonical-sourcing.md §(iv)`) distinguishes FULL physical regularizations from SCHEMATIC analogs (a SCHEMATIC helper output must carry a `-SCHEMATIC` convention suffix). For a "universe equation," this discipline is the difference between a *number* and a *number-with-a-scheme*; the latter is the only kind that means anything.

### The framework's selected functional: $f^*$

The framework's own near-canonical choice is the non-perturbative mixture (S72, PASS at $1.3\times10^{-14}$):

$$
f^*(x) = 0.9117\,\sqrt{x} + 0.0883\, e^{-x}, \qquad t^* = 0.08832,
$$

with `mellin_f_star_f0 = 0.08832`, `mellin_f_star_f2 = 214.973`, `mellin_f_star_f4 = 6446.64` (X_MAX=50). It is positivity-guaranteed and matches $n_s$ and $A_s$ by construction. Crucially, the $\sqrt{x}$ component makes the Mellin moments $f_0, f_2, f_4$ formally **divergent** — the Seeley–DeWitt expansion *does not exist* for $f^*$; it must be evaluated as a direct spectral sum (`DIRECT SPECTRAL SUMS RELIABLE`, S70). The $8.8\%$ Gaussian admixture $t^*=0.08832$ is **the framework's single empirical coupling** — the spectral-functional analog of $\Lambda_{\text{QCD}}$: an $\mathcal{O}(1)$ datum that no first principle has yet been shown to select (F-STAR-SELF-CONSISTENCY, S76: four selection principles tested, zero pick $f^*$). This is honest: $t^*$ is a *measured* degree of freedom, exactly as my methodology predicts a functional-choice must be.

---

## 3.3 The $a_0$ cosmological-constant subtlety

### The CC lives in a *different* spectral moment than gravity

The single most important structural fact in the spectral action's cosmology: **gravity and the cosmological constant are different spectral moments.**

- Newton's constant is the **second** moment: $G_N^{-1} \propto f_2\,\Lambda^2\, a_2$ (the $a_2$ Einstein–Hilbert layer).
- The vacuum energy is the **zeroth** moment: $\rho_{\text{vac}} \propto f_4\,\Lambda^4\, a_0$ (the $a_0$ perimeter layer).

They scale with *different powers of $\Lambda$* ($\Lambda^4$ vs $\Lambda^2$) and with *different moments of $f$* ($f_4$ vs $f_2$). There is no reason — within the spectral action — for them to be related, and that decoupling is the structural origin of the CC problem. In the framework's $\Phi$-correspondence (E59), they even map to different methodology-enforcement strengths: $\Phi(a_0)=\Sigma_1$ (weight-0, perimeter), $\Phi(a_2)=\Sigma_2$ (weight-2, Einstein–Hilbert).

The cutoff-action CC is canonically (`session-65-lizzi-synthesis.md`, L-4)

$$
\Lambda_{CC}^{\text{cutoff}} \;=\; \frac{f_0\,\Lambda^4\, a_0}{16\pi G_N},
\qquad\text{equivalently}\qquad
\rho_{\text{vac}} \;=\; \frac{2}{\pi^2}\, a_0\, M_{KK}^4 \quad (\text{CC-4}).
$$

### Why regularization choice bears directly on the CC

Here the scheme choice is not a refinement — it is **the entire question.**

- In the **cutoff** scheme, $a_0$ enters with a $\Lambda^4 = M_{KK}^4$ prefactor. With $M_{KK}\sim 10^{17}$ GeV this is the $\sim 10^{120}$-too-large vacuum energy (the textbook CC catastrophe). The CC is set by the **mode count** $a_0$.
- In the **zeta** scheme $S_\zeta = \zeta_{D_K}(0) = a_4$, the $a_0$ term is **absent from the action entirely**. The vacuum energy is then *not* the heat-kernel $a_0$ mode-count at all; it is determined by the Dirac operator's **finite sector** (the right-handed-neutrino Majorana masses): $\Lambda_{CC}^{\zeta} = \beta_1\, M^4$ where $M$ is the Majorana mass (`session-65-lizzi-synthesis.md`, L-6). **Same spectrum, same $D_K$ — but the CC is sourced by a completely different piece of it.** This is the sharpest possible illustration of "regularization is physics": the zeta scheme does not *fine-tune* $a_0$ away, it *removes the question* and replaces it with a different (and far smaller) one.
- The framework's *resolved* CC does not come from choosing a scheme to cancel $a_0$. It comes from **Volovik tracking-vacuum dynamics** (E44/E45, DILUTION-CC-66): the vacuum energy relaxes as $\rho_{\text{vac}}(t)\sim M_{\text{Pl}}^2 H^2(t)$, closing the $114$-OOM gap to $\rho_{\text{vac}}(\text{today})/\rho_{\text{obs}} = 1.032$ (0.01 OOM). The CC is reframed as an *expansion-history exflation observable*, not a static spectral-moment fine-tuning. The static $a_0$ value sets the *initial* vacuum scale; the dynamics dilute it. The scheme question (which moment $a_0$ vs $a_4$) and the dynamical question (how does it relax) are orthogonal — and both are real.

### The Lizzi signature $R_1$ — the FI fingerprint of the moment structure

The dimensionless combination that survives *all* scheme choices and is the cleanest probe of the relative weighting of the three layers (`sessions/framework/registry/lizzi-signature-observable.md`):

$$
\boxed{\;R_1 \;=\; \frac{a_0\, a_4}{a_2^2} \;=\; \frac{6440.0 \times 1350.7216}{2776.165389^2} \;=\; 1.1286546\ldots\;}
$$

*(S110 HK-FIRD: a₄ updated to the canonical `a_4_FW_zeta = 1350.7216` (`get_constant`); R_1 Sage-Q exact = 1.1286546 (verified `6440·1350.7216/2776.165389² = 1.12865456196`), **FI class** per `sessions/framework/registry/fi-rd-manifest.md`. The prior `1350.72` / `1.128653` was a 6-sig-fig-a₄ rounding.)*

(Sage-exact $= 42022400000000000/37232339454500103$; canonical `Lizzi_signature = 1.12865`.) $R_1$ is FUNCTIONAL-INDEPENDENT to sub-percent precision across $\{$SDW, $f^*$, $\zeta\}$ (S78 W3-K) — the regulator cancels because it is a *ratio of moments under a common regulator*. It also reappears as a candidate observable identity linking the Higgs mass, the cutoff scale, and the Planck mass:

$$
\left(\frac{m_H}{v_{\text{EW}}}\right)^2 \cdot \frac{\Lambda}{M_{\text{Pl}}^2} \;=\; R_1 \qquad (\text{Lizzi observable identity, PRELIMINARY}).
$$

$R_1$ is the structural skeleton of the layer-weighting that the scheme choice dresses but cannot move.

### ⚠ Provenance flag on the "$\sim 96.5\%$" figure (caveat for the orchestrator)

The section brief states *"$a_0$ carries $\sim 96.5\%$ of vacuum energy."* **I cannot source $96.5\%$ to any canonical entry, and I flag it as needs-correction.** Here is what the canonical numbers actually say (Sage-verified):

| Reading of "fraction carried by $a_0$" | Value | Status |
|:---------------------------------------|:------|:-------|
| Magnitude share of the $a_0$ layer in (E4) with $\Lambda=M_{KK}$ (i.e. $\Lambda^4$-weighted) | $\approx 100\%$ ($1 - \mathcal{O}(M_{KK}^{-2})$); the $\Lambda^4$ term overwhelms $\Lambda^2,\Lambda^0$ | the *true* magnitude statement |
| Bare-moment fraction $a_0/(a_0+a_2+a_4)$ (no $\Lambda$ powers, no $f$) | $60.95\%$ | exact, but physically the "wrong" weighting |
| Observed dark-**energy** budget $\Omega_\Lambda$ (CC-6) | $\approx 68.5\%$ | external observational number, *not* a spectral-moment weight |
| Observed dark-**sector** budget (DE $+$ DM) | $\approx 95\text{–}96\%$ | LCDM-vocabulary cosmic-budget figure; *not* an $a_0$ property |

The most charitable origin of "$96.5\%$" is the cosmic *dark-sector* fraction ($\sim95$–$96\%$ of today's energy density is dark) — but that is an **observational $\Omega$-budget statement, not a property of the $a_0$ spectral moment**, and importing it as one would be a container-thinking conflation (the very thing `phononic-framing.md` and `substrate-first-canonical-sourcing.md` forbid). The defensible substrate-first statement is: *with $\Lambda = M_{KK}$, the $\Lambda^4 a_0$ layer dominates the raw magnitude of the bosonic action by a factor $\sim M_{KK}^2/M_{\text{Pl}}^2$-suppressed below it for $a_2$, so $a_0$ carries essentially all of the **bare** vacuum-energy magnitude — which is exactly why the unrelaxed CC is $\sim10^{120}$ too large.* **Recommendation: replace "$\sim 96.5\%$" with either "essentially all the bare vacuum-energy magnitude (the $\Lambda^4$ layer)" or the exact $60.9\%$ bare-moment fraction, depending on which point §3.3 wants to make. Do not cite $96.5\%$ as a spectral-moment fact.**

---

## 3.4 The Mellin / convergence-cone structure (E58 / E38)

### The pole set fixes which moments survive

The moments are not free to be anything. They are **residues of a Dirichlet series** built from the finite spectrum (E37, the Mellin–Dirichlet finite-spectrum identity):

$$
\zeta_{D_K}(s) \;=\; \mathrm{Tr}\,(D_K^{-2s}) \;=\; \sum_k m_k\, \lambda_k^{-2s} \;=\; \frac{\mathcal{M}[\mathrm{Tr}\, e^{-t D_K^2}](s)}{\Gamma(s)},
$$

bit-exact at $L_{\max}=12$ across $s\in\{3,4,5\}$. The Connes–Moscovici 1995 §III.4 dimension-spectrum residue formula then *defines* each moment (E38):

$$
\boxed{\;a_n \;=\; \mathrm{Res}\big[\mathrm{Tr}(D_K^{-2s});\ s = \tfrac{d-n}{2}\big] \;=\; \sum_k m_k\, \lambda_k^{-(d-n)}\;}
\tag{E38}
$$

and this is the formula that produces the regulator-tagged family $a_n^{\zeta}$, $a_n^{\text{Pauli-Villars}}$, $a_n^{\text{Mellin}}$. **The moment is a residue at a specific pole; the regulator is the choice of contour / continuation around that pole.** This is why the regulator-class tag is mandatory (§3.2): different continuations = different residue conventions = different numbers.

### The convergence cone $S_d = \{0,2,4,6,8\}$

For the substrate's internal geometry — $SU(3)$, which has **dimension $d=8$** — the dimension spectrum (the pole set of $\zeta_{D_K}$) is exactly (E58, Mellin-strip / convergence-cone theorem):

$$
\boxed{\;S_d \;=\; \{0,\ 2,\ 4,\ 6,\ 8\}\quad (\text{CM-1995 dimension spectrum at } d=8 \text{ for } SU(3))\;}
$$

The poles sit at $s = (d-n)/2 = (8-n)/2$ for $n \in S_d$, i.e. $s \in \{4, 3, 2, 1, 0\}$. **This pole set is what determines which spectral moments are allowed to appear in the action at all.** Only $a_0, a_2, a_4, a_6, a_8$ exist as honest residues; there is no $a_1, a_3, \ldots$ (odd moments vanish by the BDI parity grading, E8/E9), and there is nothing past $a_8$ in the convergence cone. The master equation's $\ldots + \mathcal{O}(\Lambda^{-2})$ tail is not an infinite free-for-all — it is the finite ladder $a_6, a_8$ and then the cone closes.

The envelope of how a regulator-class expansion approaches the pole structure as the truncation lifts is the convergence-cone exponent (S85/S86):

$$
\alpha_R(L=3) \approx 0.761, \qquad \alpha_R(L=7) \approx 1.032,
$$

derived via the Zubarev profile $\mathcal{M}[\exp(-x/\Lambda_Z^2)](s) = \Lambda_Z^{2s}\,\Gamma(s)$. This $L^{-\alpha}$ envelope is the structural-confidence Level-2 bound for any cross-pillar bridge that consumes these moments (`cross-pillar-bridge-anatomy.md`).

### Why this is substrate-IS

The pole set $\{0,2,4,6,8\}$ is **not a choice** — it is dictated by $d=8$ ($SU(3)$) and the BDI grading. The admissible cutoff functions $f$ are exactly those whose Mellin transform $\mathcal{M}[f]$ has support compatible with this pole ladder. So the deepest statement of this section: *we do not impose $f$ on the substrate; the substrate's dimension spectrum $S_d$ tells us which $f$ are even candidates, and we choose among that constrained set.* The functional is constrained from below (the spectrum) and selected from within (FI vs RD, §3.2). That is the precise sense in which the regularization is a *physical* degree of freedom and not a free parameter: its menu is fixed by the substrate, and its selection has observable consequences.

---

## Consideration — is $f$ physical or conventional? (note for the orchestrator)

**My position: $f$ is physical, but in a stratified way that the "universe equation" must present honestly, or it will mislead.**

The clean answer "the universe is one equation" is true at the level of the *operator*: $D_K(\tau)$ on Jensen-deformed $SU(3)$ is the single object, and its spectrum is fixed. But $S = \mathrm{Tr}\, f(D_K^2/\Lambda^2) + \langle\psi|D_K|\psi\rangle$ is **not** one equation until $f$ is named — and naming $f$ is a *second* physical input, not a notational flourish. The honest presentation has three strata:

1. **What is conventional (free, must be tagged):** the *absolute* values of $a_0, a_2, a_4$ — they are regulator-artifacts (`ZETA-NOT-PHYSICAL`). Any "universe equation" that prints a bare $a_n$ without a regulator superscript is printing a scheme-dependent number as if it were a fact. The document must carry the $a_n^{\text{regulator}}$ tags into the master equation itself.
2. **What is physical and selected (a measured degree of freedom):** the *choice* of family (cutoff vs zeta vs anomaly) and, within the framework's cutoff family, the single coupling $t^* = 0.08832$ in $f^*$. This is genuinely physical — it flips $\varepsilon_H$'s sign, it sets red vs blue tilt — but it is *measured*, like $\Lambda_{\text{QCD}}$. The equation has one empirical functional-parameter. Present it as such, not as derived.
3. **What is physical and invariant (the real "universe equation" content):** the *dimensionless ratios* — $R_1 = a_0 a_4/a_2^2 = 1.1287$, the FI observables, the pole set $S_d=\{0,2,4,6,8\}$, the HP$^1$ rigidity. These survive every scheme choice. **If the document wants a single number to put on the cover, it should be an FI ratio like $R_1$, never a bare moment or a CC magnitude.**

So: present the master action as $S[D_K, f, \Lambda]$ with **all three arguments visible** — $D_K$ (the substrate, fixed), $f$ (the functional, a physical-but-selected input carrying one empirical coupling), $\Lambda = M_{KK}$ (substrate-fixed). Resist the temptation to suppress $f$ for elegance. The framework's deepest discovery in this corner is precisely that *you cannot collapse $f$ into $D_K$* — the spectral functional is an irreducible second axis, and the CC problem is the proof: same $D_K$, different $f$, the vacuum energy lives in a different moment.

**Caveats flagged for you, in priority order:**

1. **The "$\sim 96.5\%$" figure in the brief is not canonically sourceable and is likely a dark-sector $\Omega$-budget number mis-imported as a spectral-moment property.** I have written §3.3 to state the *true* magnitude fact (the $\Lambda^4 a_0$ layer dominates the bare action by the $M_{KK}^4$ prefactor — "essentially all the bare vacuum-energy magnitude") and the *true* bare-moment fraction (60.9%), and to flag $96.5\%$ explicitly. **Please decide which figure §3.3 should headline and correct the brief; do not let $96.5\%$ propagate as an $a_0$ fact.**
2. **The CC is resolved by dynamics (Volovik tracking, E44/E45), not by the scheme choice.** §3.3 says this, but the document's overall arc must not leave the reader thinking "pick the zeta scheme and the CC goes away." The zeta scheme *removes the $a_0$ question and replaces it with a Majorana-mass question*; the *resolution* is the relaxation law. Keep these two distinct in the master narrative.
3. **$f^*$ is non-perturbative** (the $\sqrt{x}$ piece makes $f_0, f_2, f_4$ divergent; the Seeley–DeWitt expansion does not exist for it). If §1 writes the layered form (E4) as *the* expansion, it should note that this is the *perturbative* face of the action, valid for smooth-decaying $f$, and that the framework's selected $f^*$ is evaluated by direct spectral sum, not by (E4). The layered form is pedagogically essential but is not how $f^*$ is computed.
4. **Anomaly-derived functionals are structurally excluded** (S67, blue tilt for all $\phi>0$). If the document presents the anomaly derivation as "proof the functional is not arbitrary" (which it is — it is a beautiful consistency result), it must immediately note that the *specific* anomaly family the framework can write down predicts the wrong tilt sign, so the framework uses the cutoff $\sqrt{x}$ family instead. The anomaly result constrains the *form*; it does not select the framework's *working* functional.
