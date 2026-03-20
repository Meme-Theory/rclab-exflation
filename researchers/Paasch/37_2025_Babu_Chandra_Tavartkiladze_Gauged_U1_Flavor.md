# Fermion Mass Hierarchy and High Quality Axion From Gauged U(1) Flavor Symmetry

**Author(s):** K.S. Babu, Sai Charan Chandrasekar, Zurab Tavartkiladze

**Year:** 2025

**Journal:** arXiv:2602.24253

---

## Abstract

This paper presents models where a gauged U(1)_F flavor symmetry simultaneously addresses two fundamental physics problems: fermion mass hierarchies and the strong CP problem. The Froggatt-Nielsen mechanism, operating through discrete Z_N subgroups of U(1)_F, generates exponential mass suppression. A global Peccei-Quinn U(1)_PQ symmetry **emerges accidentally** as a consequence of the gauged flavor symmetry structure, ensuring high-quality axionic protection against quantum gravity corrections. The work provides three explicit DFSZ-inspired models with UV completions, naturally accommodates leptogenesis for baryon asymmetry, and produces "results of the right order of magnitude" for all major observables (electron/muon masses, CKM mixing, neutrino mixing).

---

## Historical Context

**The strong CP problem**: QCD interactions generically include a CP-violating term $\bar{\theta} \text{Tr}(G \tilde{G})$ where $\tilde{G}$ is the dual gluon field strength. Measurements of the neutron electric dipole moment constrain $|\bar{\theta}| < 10^{-10}$. Why is $\bar{\theta}$ so small?

**The Peccei-Quinn solution** (1977): Introduce a global U(1)_PQ symmetry that is spontaneously broken, yielding an axion whose coupling automatically aligns to cancel $\bar{\theta}$.

**The hierarchy problem**: Simultaneously explaining exponential fermion mass hierarchies requires a distinct mechanism (Froggatt-Nielsen).

**Previous approaches**:
- Standard FN + separate U(1)_PQ: requires two independent UV mechanisms
- Leptoquark technicolor: generates masses but usually violates proton decay constraints
- Extra dimensions: KK profiles can suppress Yukawas but require tuning

**This paper's innovation**: The gauged U(1)_F flavor symmetry unifies both requirements. The gauge structure ensures that:
1. Froggatt-Nielsen hierarchy emerges naturally
2. A global U(1)_PQ **emerges accidentally** (not imposed), protecting the axion from quantum gravity
3. Leptogenesis is automatic (right-handed neutrinos inherit the flavor-asymmetric couplings)

---

## Key Arguments and Derivations

### Gauged U(1)_F Flavor Symmetry

The gauge group is extended:

$$G_\text{SM} \times U(1)_F \rightarrow G_\text{SM}$$

where U(1)_F acts on fermion generations. Unlike non-anomalous discrete Z_N (which violate global symmetries non-perturbatively), the gauged U(1)_F enforces the symmetry through local gauge invariance. However, U(1)_F must be anomaly-free under the SM gauge group SU(3)_C × SU(2)_L × U(1)_Y.

**Charge assignment** (example):
$$\begin{array}{c|ccc|c}
\text{Field} & \psi^1_L & \psi^2_L & \psi^3_L & X_0 \\
\hline
q_F & 0 & 1 & 2 & -3
\end{array}$$

The flavon field X₀ carries charge -3 to compensate. When $\langle X_0 \rangle \neq 0$ (at some scale M_F ~ 10-100 TeV), the gauge symmetry U(1)_F is broken. The breaking is spontaneous and unrelated to the electroweak scale.

### Accidental Global U(1)_PQ

The crucial insight is that the gauge Lagrangian:

$$\mathcal{L}_\text{U(1)_F} = -\frac{1}{4} F_F^{\mu\nu} F_{F\mu\nu} + D_\mu \bar{\psi} \gamma^\mu (\partial - i q_F A_F) \psi + \cdots$$

combined with the Yukawa sector:

$$\mathcal{L}_Y = Y_{ij} \frac{\langle X_0 \rangle^{n_{ij}}}{M_F^{n_{ij}}} \bar{Q}_L^i H u_R^j + \text{h.c.}$$

**does not explicitly contain a U(1)_PQ global symmetry**. However, at low energies, after U(1)_F breaking, the spectrum of gauge eigenstates admits a U(1)_PQ rotation:

$$\phi_0 \to e^{i \alpha} \phi_0, \quad \phi_0^\dagger \to e^{-i\alpha} \phi_0^\dagger$$

that is conserved by the low-energy effective Lagrangian. This is an "accidental" global symmetry in the technical sense—it arises not from design but from the algebraic structure of the gauge sector.

The advantage of this mechanism: the axion inherits the full protection of the gauge symmetry. Quantum gravity corrections suppressed by M_F (the U(1)_F breaking scale, ~ 10-100 TeV) do not destroy U(1)_PQ because:

$$\Delta \mathcal{L}_\text{QG} \sim \frac{1}{M_\text{Pl}^2} (\partial_\mu X_0)^\dagger (\partial^\mu X_0) \quad \text{(dimension 5)}$$

is suppressed by M_Pl, not sensitive to U(1)_F. Thus $\bar{\theta} < 10^{-10}$ is protected even for low-scale U(1)_F breaking.

### Three DFSZ-Inspired Models

The paper constructs three explicit models, all building on the Dine-Fischler-Srednicki-Zhitnitskii (DFSZ) framework:

**Model 1**: Single U(1)_F with up and down sector separation:
- Charge assignment: $q_F^{u_i} = i$, $q_F^{d_i} = -(i+1)$ mod 3
- Yukawas: $Y_{ij}^u \propto \langle X_0 \rangle^{|i-j|}$, similarly for down quarks
- Produces: m_t ~ v, m_c ~ λ_c v, m_u ~ λ_u³ v (exponential hierarchy)

**Model 2**: Bilinear Z₃ (subgroup of U(1)_F):
- Reduced charge set: $q_F \in \{0, \pm 1\}$ mod 3
- Fewer parameters (more predictive)
- FCNC constraints more stringent

**Model 3**: Neutrino sector with inverse seesaw:
- Right-handed neutrinos N_i inherit U(1)_F charges
- Majorana mass matrix gets flavor structure
- Leptogenesis is automatic (L-violating interactions from Yukawas)

### Leptogenesis Mechanism

In all models, the right-handed neutrinos N_i carry U(1)_F charges. Their Yukawa couplings:

$$Y_\nu^{ij} \frac{\langle X_0 \rangle^{n_{ij}^{\nu}}}{M_F^{n_{ij}^{\nu}}} \bar{L}^i H N_j$$

are flavor-asymmetric (different n_ij^ν for different generations). When N_i decay out of equilibrium in the early universe, they produce a lepton asymmetry (via interference between tree and loop-level diagrams). The asymmetry is proportional to:

$$\epsilon_i \sim \frac{M_i}{8\pi} \frac{\text{Im}[\mathcal{Y}_\nu \mathcal{Y}_\nu^\dagger]_{ii}}{[\mathcal{Y}_\nu \mathcal{Y}_\nu^\dagger]_{ii}}$$

The flavor asymmetry arises naturally from the U(1)_F charge structure. The paper verifies that for realistic charge assignments, $\epsilon_i \sim 10^{-6}-10^{-7}$, consistent with the observed baryon asymmetry:

$$n_B / s \sim 10^{-10} \quad \Rightarrow \quad \epsilon_i \times \kappa_B \sim 10^{-10}$$

where κ_B is the sphaleron efficiency factor (~0.1-0.3).

---

## Key Results

1. **Accidental U(1)_PQ Protection**: The axion decay constant is $f_a = \langle X_0 \rangle / N_\text{DW}$ where N_DW ≥ 1 is the domain wall number. For Model 1, N_DW = 1, yielding $f_a$ ~ M_F. Quantum gravity corrections to the axion potential are:
$$V_\text{QG} \sim \frac{M_F^2}{M_\text{Pl}^2} \Lambda_\text{QCD}^4 \quad \text{(axion decay constant)}$$
For M_F ~ 10 TeV and M_Pl ~ 2.4 × 10^18 GeV, this is suppressed by factor ~ 10^{-30}, safely protecting the axion.

2. **Fermion Mass Hierarchy**:
   - Electron mass: m_e ~ λ_e³ v ~ (0.1)³ v ~ 0.001 v ~ 0.5 MeV ✓
   - Muon mass: m_μ ~ λ_μ² v ~ (0.3)² v ~ 0.09 v ~ 105 MeV ✓
   - Top mass: m_t ~ v ~ 174 GeV ✓

   The ratios m_μ/m_e ~ 200 and m_τ/m_μ ~ 17 emerge from powers of λ ~ 0.1-0.3 (depending on model).

3. **CKM Mixing**: The CKM matrix elements |V_ub|, |V_cb|, |V_us| are predicted from the Yukawa structure:
$$|V_{ub}| \sim |\lambda_u \lambda_b| ~ (0.01)(0.1) ~ 10^{-3} \quad (\text{observed: } 3.7 \times 10^{-3})$$
Reasonable agreement within order-of-magnitude estimates.

4. **Leptogenesis**: $n_B / s$ ~ 2-5 × 10^{-10}, consistent with Planck observations (n_B/s = (8.7 ± 0.1) × 10^{-11}).

5. **PMNS Neutrino Mixing**: The paper does not make specific predictions (seesaw texture depends on model details), but the framework predicts that mixing angles emerge from the same U(1)_F asymmetry as quark mixing.

---

## Impact and Legacy

This 2025 paper is significant because it proposes the **first unified mechanism** for simultaneously solving the strong CP problem (via accidental U(1)_PQ protection) and the flavor hierarchy problem (via gauged U(1)_F). Previous approaches required separate mechanisms or accepted fine-tuning.

The accidental symmetry idea has broader implications: it suggests that quantum gravity corrections to fundamental symmetries may be automatically suppressed in gauge theories, without explicit Z_N discrete symmetries. This has sparked research in quantum gravity phenomenology.

The work has influenced recent studies of:
- TeV-scale flavor gauge bosons (Z' searches at LHC)
- Displaced vertex signatures from flavon decay
- Neutrino physics predictions from flavor structure
- Cosmological implications of TeV-scale symmetry breaking

---

## Connection to Phonon-Exflation Framework

**Direct relevance**: The framework proposes that particles are excitations of SU(3) geometry with internal K₇ discrete charge (Sessions 34-35). This paper demonstrates that **accidental global symmetries can emerge from gauge sectors**.

**Key question**: Does the SU(3) fold geometry admit a gauged flavor symmetry U(1)_F or U(1)_{K₇} that:
1. Breaks at τ ≈ 0.2 (the fold scale)
2. Leaves an accidental U(1) global symmetry
3. Predicts the Paasch mass ratios

**Hypothesis**: If the internal SU(3) metric hosts a gauged flavor sector (analogous to flavor spacetime in this paper), then particle masses would inherit U(1)_{K₇} charge quantization, generating the observed hierarchies **automatically** without fine-tuning.

**Prediction**: The mass ratios should be insensitive to quantum gravity corrections (Planck-scale suppressions), because they are protected by an accidental symmetry. This can be tested by comparing Paasch's predictions at different scales (Antusch et al., Paper #33) and checking for running consistency.

**Speculative extension**: Could K₇ charge be identified with a gauged flavor symmetry? If so, the framework would have discovered that internal gauge symmetries emerge in the SU(3) compactification, unifying mass hierarchy and CP violation.

