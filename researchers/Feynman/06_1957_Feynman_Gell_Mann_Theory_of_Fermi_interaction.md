# Theory of the Fermi Interaction

**Authors:** Richard P. Feynman, Murray Gell-Mann
**Year:** 1958 (received September 1957, published January 1958)
**Journal:** *Physical Review*, 109(1), 193--198

---

## Abstract

Feynman and Gell-Mann propose a universal form for the weak interaction based on the vector minus axial-vector (V-A) current structure. They show that if the weak interaction is mediated by a current-current coupling of the form $G_F J^\mu J_\mu^\dagger / \sqrt{2}$, where the current $J^\mu$ is a sum of vector and axial-vector components with equal magnitude, then parity violation is maximal, the two-component neutrino theory follows automatically, and a wide range of weak decay phenomena are unified into a single framework. The paper introduces the concept of the "universal Fermi interaction," predicts the helicity of the neutrino, explains the suppression of certain decay modes, and lays the foundation for the electroweak theory that would be developed a decade later.

---

## Historical Context

### Fermi's Original Theory

Enrico Fermi proposed in 1934 that beta decay ($n \to p + e^- + \bar{\nu}_e$) occurs through a local four-fermion interaction:

$$\mathcal{H}_{\text{Fermi}} = G_F (\bar{p}\gamma^\mu n)(\bar{e}\gamma_\mu \nu) + \text{h.c.}$$

This vector (V) coupling successfully described many features of beta decay but left open the question of whether other Lorentz-invariant couplings (scalar S, tensor T, axial-vector A, pseudoscalar P) might also contribute.

### The Parity Revolution

In 1956, Lee and Yang proposed that parity might not be conserved in weak interactions, explaining puzzling observations in kaon decay (the "tau-theta puzzle"). Wu and collaborators confirmed parity violation in 1957 through the observation of asymmetric beta emission from polarized $^{60}$Co nuclei. Garwin, Lederman, and Weinrich simultaneously confirmed it in pion decay.

The magnitude of parity violation was the key question. Was it small (a perturbation) or maximal? The Wu experiment and subsequent measurements indicated maximal violation: the weak interaction distinguishes left from right as strongly as the laws of physics permit.

### The V-A Hypothesis

Several groups converged on the V-A structure nearly simultaneously:
- Marshak and Sudarshan (September 1957, published 1958) proposed V-A based on analysis of existing beta decay data
- Feynman and Gell-Mann (September 1957, published January 1958) arrived at V-A from theoretical considerations of the two-component neutrino
- Sakurai also contributed to the discussion

The priority question has been debated, with Sudarshan and Marshak having a legitimate claim to independent co-discovery based on their earlier preprint. The Feynman-Gell-Mann paper, however, provided the most complete theoretical framework and had the greater impact on subsequent developments.

---

## Key Arguments and Derivations

### 1. The General Four-Fermion Interaction

The most general local, Lorentz-invariant four-fermion interaction for beta decay can be written:

$$\mathcal{H}_{\text{weak}} = \sum_i G_i (\bar{p}\Gamma_i n)(\bar{e}\Gamma_i \nu) + \text{h.c.}$$

where the sum runs over the five Lorentz-invariant bilinear forms:

| Type | $\Gamma_i$ | Bilinear |
|------|-----------|----------|
| Scalar (S) | $I$ | $\bar{\psi}_1\psi_2$ |
| Vector (V) | $\gamma^\mu$ | $\bar{\psi}_1\gamma^\mu\psi_2$ |
| Tensor (T) | $\sigma^{\mu\nu}$ | $\bar{\psi}_1\sigma^{\mu\nu}\psi_2$ |
| Axial-vector (A) | $\gamma^\mu\gamma^5$ | $\bar{\psi}_1\gamma^\mu\gamma^5\psi_2$ |
| Pseudoscalar (P) | $\gamma^5$ | $\bar{\psi}_1\gamma^5\psi_2$ |

Pre-1957 experiments were consistent with S and T couplings (the "Gamow-Teller interaction") for the nuclear part, with some evidence against V and A. Feynman and Gell-Mann argued this experimental evidence was wrong (as was later confirmed) and proposed a purely V-A structure.

### 2. The Two-Component Neutrino

The crucial theoretical input is the two-component neutrino. If the neutrino is massless ($m_\nu = 0$), the Dirac equation reduces to two decoupled two-component equations (Weyl equations):

$$i\bar{\sigma}^\mu\partial_\mu \chi_L = 0, \quad i\sigma^\mu\partial_\mu \chi_R = 0$$

where $\chi_L$ and $\chi_R$ are the left-handed and right-handed Weyl spinors, and $\sigma^\mu = (I, \boldsymbol{\sigma})$, $\bar{\sigma}^\mu = (I, -\boldsymbol{\sigma})$. Only one of these (the left-handed component) participates in the weak interaction.

In four-component notation, the projection onto the left-handed component is:

$$\nu_L = \frac{1}{2}(1 - \gamma^5)\nu$$

The two-component neutrino has definite helicity: $h = -1$ (left-handed) for the neutrino and $h = +1$ (right-handed) for the antineutrino. This was confirmed experimentally by Goldhaber, Grodzins, and Sunyar in 1958.

### 3. The V-A Current

Feynman and Gell-Mann propose that the weak interaction involves only the left-handed projection of all fermion fields. The weak current is:

$$J^\mu = \bar{\psi}_1 \gamma^\mu (1 - \gamma^5) \psi_2$$

Using the identity:

$$\gamma^\mu(1 - \gamma^5) = \gamma^\mu - \gamma^\mu\gamma^5$$

this is a combination of vector ($\gamma^\mu$) and axial-vector ($\gamma^\mu\gamma^5$) currents with equal and opposite coefficients -- hence "V minus A" or V-A.

The complete weak Hamiltonian is:

$$\mathcal{H}_{\text{weak}} = \frac{G_F}{\sqrt{2}} J^\mu J_\mu^\dagger$$

where the current includes both leptonic and hadronic parts:

$$J^\mu = J^\mu_{\text{leptonic}} + J^\mu_{\text{hadronic}}$$

$$J^\mu_{\text{leptonic}} = \bar{\nu}_e \gamma^\mu(1 - \gamma^5)e + \bar{\nu}_\mu \gamma^\mu(1 - \gamma^5)\mu$$

$$J^\mu_{\text{hadronic}} = \bar{p}\gamma^\mu(1 - \gamma^5)n \cdot \cos\theta_C + \cdots$$

where $\theta_C$ is the Cabibbo angle (introduced later, in 1963, to account for strangeness-changing weak decays).

### 4. Maximal Parity Violation

The V-A structure automatically gives maximal parity violation. Under parity, $\gamma^\mu \to \gamma^\mu$ (for $\mu = 0$) or $-\gamma^\mu$ (for $\mu = i$), while $\gamma^5 \to -\gamma^5$. Therefore:

$$P: \quad \gamma^\mu(1 - \gamma^5) \to \gamma^\mu(1 + \gamma^5)$$

The parity-transformed interaction involves only right-handed fields, which do not couple to the weak force. Parity violation is therefore maximal: the interaction is completely left-handed.

### 5. Consequences and Predictions

**Beta decay spectrum:** The V-A theory predicts that in nuclear beta decay, the electron is predominantly left-handed (helicity $-v/c$) and the antineutrino is right-handed. This determines the angular correlations between the emitted particles and the nuclear spin, correctly predicting the Wu experiment results.

**Muon decay:** For $\mu^- \to e^- + \bar{\nu}_e + \nu_\mu$, the V-A theory predicts the Michel parameter $\rho = 3/4$ (governing the electron energy spectrum) and the asymmetry parameter $\xi = 1$ (governing the angular distribution relative to the muon spin). Both are confirmed experimentally to high precision.

The differential decay rate is:

$$\frac{d\Gamma}{dx \, d(\cos\theta)} \propto x^2 \left[(3 - 2x) + (2x - 1)\cos\theta\right]$$

where $x = 2E_e/m_\mu$ is the scaled electron energy and $\theta$ is the angle between the electron momentum and the muon spin.

**Pion decay:** The V-A theory explains the puzzling ratio $\Gamma(\pi \to e\nu)/\Gamma(\pi \to \mu\nu) \approx 1.2 \times 10^{-4}$. Naively, phase space favors the electron channel, but the helicity argument reverses this: the $(1-\gamma^5)$ projection forces the charged lepton to be left-handed, which for a nearly massless particle means helicity $-1$. In the pion rest frame, conservation of angular momentum (the pion has spin 0) requires the charged lepton and neutrino to have the same helicity. Since the neutrino is left-handed ($h = -1$), the charged lepton must also be left-handed, which is "wrong" (the weak interaction produces left-handed particles, but helicity $-1$ for a positive-energy particle moving in the $-z$ direction is right-handed with respect to momentum). The mismatch is proportional to $(m_\ell/m_\pi)^2$:

$$\frac{\Gamma(\pi \to e\nu)}{\Gamma(\pi \to \mu\nu)} = \frac{m_e^2(m_\pi^2 - m_e^2)^2}{m_\mu^2(m_\pi^2 - m_\mu^2)^2} \approx 1.28 \times 10^{-4}$$

in excellent agreement with experiment.

**Neutron decay:** The ratio $g_A/g_V$ of axial to vector coupling constants in nuclear beta decay is predicted to be close to $-1$ (exact V-A for point nucleons), with the actual value $g_A/g_V \approx -1.27$ differing from unity due to strong interaction renormalization of the axial current in the nucleon (partially conserved axial current, PCAC).

### 6. The Conserved Vector Current (CVC) Hypothesis

Feynman and Gell-Mann propose that the vector part of the hadronic weak current is the isospin-raising component of the same conserved isospin current that generates electromagnetic interactions:

$$V^\mu_{\text{weak}} = V^\mu_{1+i2}$$

where $V^\mu_a$ ($a = 1,2,3$) is the isospin current with $V^\mu_3$ being the electromagnetic current (up to hypercharge). This "conserved vector current" (CVC) hypothesis has several consequences:
- The vector coupling constant is not renormalized by the strong interaction: $g_V = 1$ exactly.
- The weak magnetism form factor is related to the electromagnetic form factors of the nucleon.
- The beta decay ft-values for superallowed $0^+ \to 0^+$ transitions (pure Fermi) are universal.

CVC was confirmed experimentally by the universality of Fermi coupling constants across different nuclear transitions and by direct measurements of weak magnetism.

---

## Physical Interpretation

### Chirality as the Organizing Principle

The V-A theory reveals that the weak interaction is fundamentally chiral: it couples only to left-handed fermions (and right-handed antifermions). This is not just a quantitative property but a structural one -- the weak force sees only half of the Dirac spinor. This chirality would later be understood as a consequence of the gauge structure: the $SU(2)_L$ gauge bosons couple only to left-handed doublets.

### Universality

The current-current structure with a single coupling constant $G_F$ implies universality: the weak interaction strength is the same for all fermions. This is the "universal Fermi interaction" of the paper's title. Universality at the quark level (Cabibbo universality) was later confirmed and extended to three generations by Kobayashi and Maskawa.

### Why V-A and Not V+A?

Nature's choice of V-A (left-handed) rather than V+A (right-handed) appears to be arbitrary at the level of the Feynman-Gell-Mann theory. In fact, if all particles were replaced by their mirror images and all charges reversed (a CP transformation), the V+A theory would result. The question of why nature chose one chirality is related to the matter-antimatter asymmetry of the universe and remains open.

---

## Impact and Legacy

### Foundation of the Electroweak Theory

The V-A current structure is the direct precursor of the electroweak theory. When Glashow (1961), Weinberg (1967), and Salam (1968) constructed the $SU(2)_L \times U(1)_Y$ gauge theory, the left-handed current structure of Feynman-Gell-Mann became the gauge coupling of the $SU(2)_L$ sector. The Fermi constant is related to the $W$ boson mass:

$$\frac{G_F}{\sqrt{2}} = \frac{g^2}{8M_W^2}$$

### Cabibbo-Kobayashi-Maskawa Matrix

The hadronic current of Feynman-Gell-Mann was extended by Cabibbo (1963) to include strangeness-changing transitions and by Kobayashi and Maskawa (1973) to three generations, giving the CKM mixing matrix that describes all flavor-changing weak processes.

### CP Violation

The V-A structure, combined with the CKM matrix, accommodates CP violation through the complex phase in the three-generation mixing matrix. This was predicted by Kobayashi and Maskawa and confirmed experimentally in B-meson decays.

---

## Connections to Modern Physics

1. **Standard Model chirality:** The entire gauge structure of the Standard Model is chiral: $SU(2)_L$ couples only to left-handed fermions, while $SU(3)_c$ and $U(1)_Y$ couple to both chiralities. This chirality is the single most important structural feature identified by Feynman and Gell-Mann.

2. **Neutrino mass:** The original two-component neutrino assumed $m_\nu = 0$. The discovery of neutrino oscillations (Super-Kamiokande, 1998) shows that neutrinos have small but nonzero masses, requiring either right-handed neutrinos (Dirac mass), Majorana mass terms, or both (seesaw mechanism). The V-A structure is preserved in all these extensions.

3. **Left-right symmetric models:** Extensions of the Standard Model with $SU(2)_L \times SU(2)_R$ gauge symmetry restore parity at high energies, with the observed V-A structure arising from spontaneous symmetry breaking that makes the right-handed $W_R$ bosons very heavy.

4. **Grand unification:** In GUT models like $SO(10)$, all fermions of one generation (including a right-handed neutrino) fit into a single 16-dimensional spinor representation. The V-A structure emerges from the embedding of $SU(2)_L$ within the larger gauge group.

5. **Kaluza-Klein and chirality:** In higher-dimensional frameworks, obtaining chiral fermions in four dimensions is a non-trivial topological requirement. The Atiyah-Singer index theorem relates the number of zero modes of the Dirac operator on the internal manifold to topological invariants. The V-A structure identified by Feynman and Gell-Mann thus constrains the topology of any internal space from which the Standard Model is to emerge.
