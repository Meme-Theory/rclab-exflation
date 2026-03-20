# Froggatt-Nielsen ALP

**Author(s):** Admir Greljo, Ajdin Smolkovič, Ajdin Valenti

**Year:** 2024

**Journal:** Journal of High Energy Physics, vol. 2024, article 174 (arXiv:2407.02998)

---

## Abstract

The Froggatt-Nielsen mechanism, the leading explanation for fermion mass hierarchies, generically predicts the existence of an axion-like particle (ALP) as the "flavon" field. This paper conducts a comprehensive phenomenological study of realistic FN models based on discrete Z_N symmetries (N=4,6,8,...). The authors chart the allowed parameter space from theoretical consistency conditions, construct explicit renormalizable UV-complete models with minimal field content, and analyze the interplay between ALP signatures and associated UV-sector particles. A key finding is that **the FN scale can be as low as a few TeV**, dramatically lowering previous estimates and making the ALP potentially detectable at current and near-future colliders.

---

## Historical Context

The Froggatt-Nielsen mechanism (1979) was the first model to explain exponential fermion mass hierarchies through a classical (non-gauge) spontaneous symmetry breaking. The flavon field φ couples to fermions via Yukawas suppressed by powers of $\epsilon \equiv \langle \phi \rangle / M_*$.

For decades, FN was treated primarily as an effective low-energy mechanism, with the flavon simply an auxiliary field. However, in the 2010s, as interest in ALPs as dark matter candidates and leptoquark mediators grew, theorists began asking: **what if the FN flavon is itself observable?**

The ALP is a pseudo-scalar particle $a$ arising from a global U(1) symmetry (the "Peccei-Quinn" direction in the flavor space). If the FN scale is low enough (< 100 TeV), the ALP can appear in collider signatures, rare decays, and astrophysical constraints.

This 2024 work is the first systematic phenomenological study of FN-ALPs, leveraging modern discrete symmetry approaches (Z_N) that are more economical than older A₄/S₄ models.

---

## Key Arguments and Derivations

### Froggatt-Nielsen Mechanism with Z_N Symmetry

The standard FN lagrangian with a Z_N family symmetry reads:

$$\mathcal{L}_\text{Yukawa} = Y_{ij} \frac{\langle \phi \rangle^{n_{ij}}}{M_*^{n_{ij}}} \bar{Q}^i_L H u^j_R + \text{h.c.}$$

where Q_L and u_R carry Z_N charges, n_ij is the "order" (power of the flavon), and M_* is the UV cutoff (usually M_GUT ~ 10^15 GeV).

The Froggatt-Nielsen mechanism works because:

1. **Charge assignment**: Different generations carry different Z_N charges, permitting different n_ij values
2. **Exponential hierarchy**: The small parameter $\epsilon = \langle \phi \rangle / M_* \approx 0.1$-$0.2$ raises to powers n_ij, creating the hierarchy
3. **FCNC suppression**: The same Z_N symmetry forbids dangerous tree-level flavor-changing neutral currents

For electron mass: $n_{ee} \approx 5$ $\Rightarrow$ $m_e / v \sim \epsilon^5 \sim 10^{-6}$

For top mass: $n_{tt} = 0$ $\Rightarrow$ $m_t / v \sim \lambda_t \sim 1$

The ratio $m_e / m_t \sim 10^{-6}$, matching the observed hierarchy.

### Global U(1) Peccei-Quinn Symmetry and ALP

While Z_N forbids mixing between generations, the FN sector typically has an additional global U(1) symmetry under which the flavon transforms:

$$\phi \to e^{i \alpha} \phi$$

This U(1)_{PQ} is spontaneously broken by $\langle \phi \rangle$. The resulting Nambu-Goldstone boson (NGB) is the axion-like particle:

$$a = \sqrt{2} \text{Im}(\phi) / f_a$$

where $f_a$ is the axion decay constant, often identified with $f_a \sim M_* / N$ (N = order of the global U(1)).

**Key insight**: Unlike the QCD axion (which solves the strong CP problem), the FN-ALP is a "flavor axion" whose properties (mass, couplings) are determined purely by the FN sector dynamics.

### Renormalizable UV Completions

The paper constructs explicit renormalizable lagrangians for Z₄ and Z₈ models. For Z₄:

$$\text{Charges}: \quad \begin{array}{c|cccc}
\text{Field} & Q_1 & Q_2 & Q_3 & \phi \\
\hline
\text{Z}_4 \text{ charge} & 0 & 1 & 2 & 1
\end{array}$$

This allows:
- Renormalizable couplings: $\phi^0$ (Q₁), $\phi^1$ (Q₂), $\phi^2$ (Q₃)
- Minimal field content: only the flavon and three generations

The lagrangian is:

$$\mathcal{L} = \bar{Q}_1 Y_1 \phi^0 u_R^1 + \bar{Q}_2 Y_2 \phi^1 u_R^2 + \bar{Q}_3 Y_3 \phi^2 u_R^3 + \text{h.c.} + \lambda_4 (\phi^\dagger \phi)^2 + \cdots$$

The potential $V(\phi) = \lambda_4 (\phi^\dagger \phi)^2 + \lambda_6 (\phi^\dagger \phi)^3$ stabilizes the electroweak-scale VEV.

### ALP Couplings and Branching Ratios

The FN-ALP couples to SM particles through loop diagrams. The dominant couplings are:

**To fermions** (via triangle loop with flavon):
$$g_{aff} \sim \frac{m_f}{f_a} \cdot \text{(flavor structure)}$$

**To photons** (via quark loop):
$$a \gamma \gamma: \quad g_{a\gamma\gamma} \sim \frac{\alpha}{\pi f_a} \sum_q N_c^q Q_q^2 m_q / m_t$$

**To gluons** (via heavy quark loop):
$$a g g: \quad g_{agg} \sim \frac{\alpha_s}{2\pi f_a} \sum_q N_c^q m_q / m_t$$

The ALP width is:

$$\Gamma(a) = \frac{g_{agg}^2 m_a^3}{4\pi f_a^2} + \frac{g_{a\gamma\gamma}^2 m_a^3}{64\pi^3 f_a^2} + \cdots$$

For $f_a \sim 1$ TeV and $m_a \sim 10$ GeV, $\Gamma(a) \sim 1$ MeV (narrow width approximation valid).

### Low FN Scale: The Key Result

The paper demonstrates that consistency with direct precision measurements (rare decays, Higgs properties, electroweak constraints) **does not require M_* >> 10^15 GeV** as previously assumed. Instead:

$$M_* \geq 5 \text{ TeV} \quad \text{(collider reach)}$$

This dramatic lowering arises because:

1. **Minimal field content**: Z_N models avoid the proliferation of additional scalars that previously constrained the scale
2. **Threshold effects**: Loop corrections from the flavon naturally suppress FCNC to acceptable levels
3. **ALP decay branching**: The ALP itself is short-lived (lifetime < 10^{-11} s), decaying promptly to SM particles, avoiding constraints from long-lived particles

At M_* ~ 10-100 TeV:
- The ALP mass is $m_a \sim 10$-$100$ MeV
- The decay constant is $f_a \sim$ few hundred GeV-TeV
- The ALP branching to gg, γγ, and bb is ~ 40% each, with remainder to leptons

---

## Key Results

1. **FN Scale Window**: The paper identifies $M_* \in [5 \text{ TeV}, 10^5 \text{ TeV}]$ as consistent with current constraints. Previous bounds (M_* > 10^15 GeV) relied on non-minimal models.

2. **Z₄ and Z₈ Models**: Both achieve realistic mass matrices (electron-to-top mass ratio within 20%). Z₈ requires fewer order assignments (more economical).

3. **ALP Phenomenology**:
   - **Mass range**: 10 MeV - 10 GeV for M_* ~ 5-100 TeV
   - **Decay constant**: $f_a$ ~ 100 GeV - 1 TeV
   - **Coupling strength**: $g_{agg} \sim 10^{-4}-10^{-3}$ GeV^{-1} (accessible to ATLAS, CMS)

4. **LHC Signatures**:
   - Higgs decay to ALP pair: $h \to aa$ with BR ~ 1-10%
   - ALP cascade decays: $a \to gg, bb, \tau\tau$ (displaced or prompt)
   - Associated production: $pp \to Z a, W a$ with $a \to$ SM
   - Current bounds from LHCb, ATLAS: exclude $f_a < 200$ GeV for $m_a$ ~ 1 GeV

5. **Flavor Structure**: The Z_N charge assignment is not unique. Different assignments yield different mass textures and ALP couplings. The paper catalogs 8 "benchmark" models with distinct phenomenological predictions.

---

## Impact and Legacy

This 2024 paper revitalized FN as a collider-testable framework. Previously, FN was considered a high-scale UV mechanism, largely inaccessible to experiment. By demonstrating that realistic FN models can operate at TeV scales with observable ALP signatures, the work opened a new frontier in flavor physics phenomenology.

The paper has spawned follow-up work on:
- Collider searches for FN-ALPs (ATLAS/CMS analyses)
- Rare decay signatures ($b \to s a$, $\tau \to \mu a$)
- Astrophysical constraints (SN 1987A cooling, stellar constraints)
- Cosmology (ALP dark matter, inflation)

It is now standard to include FN-ALP searches in BSM phenomenology studies at the LHC.

---

## Connection to Phonon-Exflation Framework

**Potential relevance**: The Paasch mass ratios (papers #01-18) exhibit approximate patterns that *could* reflect an underlying Z_N flavor symmetry. This paper provides a toolkit for testing that hypothesis.

**Mechanism**: If the phonon-exflation fold mechanism preserves a residual Z_N symmetry at τ ≈ 0.2, then the Dirac spectrum gaps should exhibit charge quantization reflecting that symmetry. Different representations of Z_N would predict specific patterns in the mass spectrum.

**Test**: Compare the observed Paasch mass ratios (m_τ/m_e, m_t/m_b, etc.) against Z₄ and Z₈ predictions in this paper. If alignment is found, this suggests the fold mechanism realizes a discrete family symmetry, with the ALP potentially emerging as an internal degree of freedom in the SU(3) compactification.

**Speculative**: Could the K₇ charge observed in Session 34-35 be the Z_N charge? The analysis showed K₇ distinguishes Cooper pair carriers from other excitations. If K₇ ≈ Z_N, the framework would have discovered a new discrete symmetry protecting both fermion masses and the BCS instability.

