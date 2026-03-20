# Very High-Energy Collisions of Hadrons

**Author:** Richard P. Feynman
**Year:** 1969
**Journal:** *Physical Review Letters*, 23(24), 1415--1417

---

## Abstract

Feynman proposes the parton model for understanding hadron collisions at very high energies. By analyzing hadronic processes in the infinite-momentum frame, he argues that a hadron can be described as a collection of point-like constituents -- partons -- each carrying a fraction $x$ of the hadron's total momentum. In this frame, the transverse momenta of the partons are negligible compared to the longitudinal momentum, and the interaction between the probe (virtual photon, for instance) and the hadron reduces to an incoherent sum of interactions with individual partons. This picture explains the observed scaling behavior in deep inelastic electron-proton scattering (Bjorken scaling), provides a framework for calculating hadronic cross sections, and bridges the gap between the quark model of Gell-Mann and Zweig and the experimental observations at SLAC. The partons are eventually identified with quarks and gluons, and the parton model becomes the foundation for perturbative QCD.

---

## Historical Context

### The Quark Model and Its Discontents

Gell-Mann and Zweig independently proposed in 1964 that hadrons are composed of fractionally charged constituents called quarks (Gell-Mann) or aces (Zweig). The quark model brilliantly organized the hadron spectrum: mesons as $q\bar{q}$ pairs, baryons as $qqq$ triplets. However, no free quarks had been observed, and many physicists -- including Gell-Mann himself in certain modes -- treated quarks as mathematical abstractions rather than physical particles.

### Deep Inelastic Scattering at SLAC

The key experimental development was deep inelastic electron-proton scattering (DIS) at the Stanford Linear Accelerator Center (SLAC) in 1968-69. Electrons with energies up to 20 GeV were scattered off proton targets, with the scattered electron's energy and angle measured.

The cross section for DIS depends on two kinematic variables: the four-momentum transfer $Q^2 = -q^2$ (measuring the "resolution" of the probe) and the energy transfer $\nu = E - E'$ (measuring the inelasticity). The differential cross section can be written:

$$\frac{d^2\sigma}{dE'd\Omega} = \frac{\alpha^2}{4E^2\sin^4(\theta/2)}\left[W_2(\nu, Q^2)\cos^2\frac{\theta}{2} + 2W_1(\nu, Q^2)\sin^2\frac{\theta}{2}\right]$$

where $W_1$ and $W_2$ are structure functions.

The SLAC experiments found that the structure functions, when expressed in terms of the Bjorken variable $x = Q^2/(2M\nu)$ (where $M$ is the proton mass), became approximately independent of $Q^2$ for large $Q^2$:

$$MW_1(\nu, Q^2) \to F_1(x), \quad \nu W_2(\nu, Q^2) \to F_2(x)$$

This "Bjorken scaling," predicted by Bjorken in 1969 on the basis of current algebra, was deeply mysterious: it implied that the virtual photon was scattering off point-like objects within the proton.

### Feynman's Contribution

Feynman visited SLAC in August 1968, saw the experimental results, and immediately recognized their significance. His parton model provided the physical picture behind Bjorken scaling and translated the abstract current-algebra arguments into an intuitive language that could be used to calculate cross sections for a wide variety of hadronic processes.

---

## Key Arguments and Derivations

### 1. The Infinite-Momentum Frame

Feynman's central trick is to analyze the collision in a frame where the hadron has very large momentum $P \to \infty$ (the "infinite-momentum frame" or IMF). In this frame:

- The hadron is Lorentz-contracted to a thin disk.
- Time dilation slows down the internal dynamics of the hadron: the partons are "frozen" during the interaction time.
- Each parton carries a fraction $x$ of the hadron's total four-momentum: $p^\mu_{\text{parton}} = x P^\mu + p_\perp^\mu + O(1/P)$, where $p_\perp$ is the transverse momentum (bounded, of order $\Lambda_{\text{QCD}} \sim$ a few hundred MeV).
- For $P \to \infty$, the transverse momenta become negligible: $p_\perp/xP \to 0$.

The probability of finding a parton of type $i$ carrying momentum fraction between $x$ and $x + dx$ is given by the parton distribution function (PDF) $f_i(x) \, dx$.

### 2. Deep Inelastic Scattering in the Parton Model

In the parton model, DIS is described as elastic scattering of the virtual photon off a single parton. The virtual photon ($q^2 = -Q^2$) strikes a parton with momentum $xP$. The elastic scattering condition for a massless parton is:

$$(xP + q)^2 = 0 \implies x = \frac{Q^2}{2P\cdot q} = \frac{Q^2}{2M\nu}$$

This identifies the Bjorken variable $x$ with the momentum fraction of the struck parton. This is a remarkable kinematic result: the abstract variable $x$ has a direct physical interpretation.

The structure functions are then sums over parton types:

$$F_2(x) = \sum_i e_i^2 \, x f_i(x)$$

$$F_1(x) = \frac{F_2(x)}{2x}$$

where $e_i$ is the electric charge of parton type $i$ (in units of $e$). The relation $F_2 = 2xF_1$ is the Callan-Gross relation, valid for spin-1/2 partons, and its experimental confirmation was strong evidence that the partons are quarks (spin-1/2) rather than scalars (spin-0).

### 3. Sum Rules

The parton model leads to several sum rules that relate integrals of the structure functions to static properties of the hadron:

**Momentum sum rule:**
$$\sum_i \int_0^1 x f_i(x) \, dx = 1$$

The total momentum of all partons must equal the hadron's momentum. Experimentally, the quarks carry only about 50% of the proton's momentum, implying that the remaining 50% is carried by electrically neutral partons -- later identified as gluons.

**Gottfried sum rule:**
$$\int_0^1 \frac{F_2^{ep}(x) - F_2^{en}(x)}{x} dx = \frac{1}{3} + \frac{2}{3}\int_0^1 [\bar{u}(x) - \bar{d}(x)] dx$$

For a symmetric sea ($\bar{u} = \bar{d}$), this gives 1/3. The NMC experiment (1991) measured a value of $0.235 \pm 0.026$, indicating a flavor asymmetry in the quark sea.

**Gross-Llewellyn Smith sum rule:**
$$\int_0^1 F_3^{\nu p}(x) dx = 3$$

counting the number of valence quarks in the proton.

### 4. Parton-Model Cross Sections

The parton model provides a universal framework for computing hadronic cross sections. The cross section for a hadronic process $A + B \to X$ is:

$$\sigma(A + B \to X) = \sum_{i,j} \int_0^1 dx_1 \int_0^1 dx_2 \, f_i^A(x_1) f_j^B(x_2) \, \hat{\sigma}(ij \to X)$$

where $\hat{\sigma}$ is the partonic cross section (computable in perturbation theory for point-like partons) and $f_i^A(x)$ is the PDF for parton $i$ in hadron $A$.

This factorization formula is the basis of all predictions for hadron colliders. Examples:

**Drell-Yan process** ($q\bar{q} \to \ell^+\ell^-$):

$$\frac{d\sigma}{dM^2} = \frac{4\pi\alpha^2}{9M^2 s}\sum_i e_i^2 \left[f_i^A(x_1)f_{\bar{i}}^B(x_2) + f_{\bar{i}}^A(x_1)f_i^B(x_2)\right]$$

where $M^2 = x_1 x_2 s$ is the invariant mass of the lepton pair. This was proposed by Drell and Yan (1970) and confirmed experimentally, providing strong evidence for the parton model.

**Jet production** ($gg \to gg$, $qg \to qg$, $qq \to qq$):

$$\frac{d\sigma}{dp_T^2 dy_1 dy_2} = \sum_{i,j} f_i(x_1) f_j(x_2) \frac{d\hat{\sigma}}{d\hat{t}}$$

The large-$p_T$ jet production at hadron colliders is computed using partonic $2 \to 2$ scattering cross sections convoluted with PDFs.

### 5. Scaling Violations and the Approach to QCD

Feynman's original parton model predicts exact Bjorken scaling: the structure functions depend only on $x$, not on $Q^2$. However, the SLAC data already showed small but systematic deviations from exact scaling, and later experiments at higher $Q^2$ confirmed these "scaling violations."

The scaling violations are explained by QCD. At higher $Q^2$, the virtual photon resolves smaller structures, revealing gluon radiation and quark-antiquark pair creation within the parton. The DGLAP evolution equations (Dokshitzer, Gribov, Lipatov, Altarelli, Parisi) describe how the PDFs evolve with $Q^2$:

$$\frac{\partial f_i(x, Q^2)}{\partial \ln Q^2} = \frac{\alpha_s(Q^2)}{2\pi}\sum_j \int_x^1 \frac{dz}{z} P_{ij}(z) f_j(x/z, Q^2)$$

where $P_{ij}(z)$ are the splitting functions (e.g., $P_{qq}(z) = C_F \frac{1+z^2}{1-z}$ for a quark radiating a gluon). The logarithmic $Q^2$ dependence of the PDFs -- and hence of the structure functions -- is a prediction of perturbative QCD that has been verified to extraordinary precision.

---

## Physical Interpretation

### Partons = Quarks + Gluons

The parton model was initially agnostic about the identity of the partons. The Callan-Gross relation identified them as spin-1/2, consistent with quarks. The momentum sum rule's deficit identified gluons as the neutral partons carrying the remaining momentum. The full identification was cemented by the development of QCD (Gross, Wilczek, Politzer, 1973), in which the partons are quarks interacting via gluon exchange.

### Asymptotic Freedom and the Parton Model

The parton model assumes that partons behave as free particles during the hard scattering process. This seems paradoxical -- how can quarks, which are permanently confined inside hadrons, behave as free particles? The answer is asymptotic freedom: the QCD coupling $\alpha_s(Q^2)$ decreases at large $Q^2$ (short distances), so at the high energies probed by DIS, the quarks are indeed approximately free. The parton model is the leading-order approximation in the $\alpha_s \to 0$ limit.

### Factorization

The separation of the cross section into short-distance (partonic) and long-distance (PDF) components is called factorization. It is proven rigorously in QCD to all orders in perturbation theory for inclusive processes like DIS and Drell-Yan. Factorization is the theoretical foundation for all predictions at hadron colliders.

---

## Impact and Legacy

### The Standard Model of Particle Physics

The parton model was the crucial bridge between the quark model (a static classification scheme) and QCD (a dynamical gauge theory). The SLAC DIS experiments, interpreted through the parton model, provided the first direct evidence that quarks are real, physical entities confined within hadrons.

### Collider Physics

All predictions for hadron colliders -- from the Tevatron to the LHC -- are based on the parton model framework, with QCD corrections computed perturbatively. The discovery of the $W$ and $Z$ bosons (1983), the top quark (1995), and the Higgs boson (2012) all relied on parton-level predictions convoluted with PDFs.

### Parton Distribution Functions

The determination of PDFs from global fits to experimental data is a major industry. Groups like CTEQ, NNPDF, and MMHT produce PDF sets that are used by the entire high-energy physics community. Modern PDFs incorporate data from DIS, Drell-Yan, jet production, $W/Z$ production, and top quark production.

---

## Connections to Modern Physics

1. **LHC physics:** Every LHC measurement and every search for new physics relies on parton-level predictions. The Higgs boson production cross section, for instance, is computed as $\sigma(pp \to H) = \sum_{i,j}\int f_i f_j \hat{\sigma}(ij \to H)$, with the dominant contribution from gluon-gluon fusion.

2. **Nuclear PDFs:** In heavy-ion collisions (RHIC, LHC), nuclear PDFs describe the parton structure of nuclei, including shadowing and anti-shadowing effects. These are essential for understanding the quark-gluon plasma.

3. **Small-$x$ physics:** At very small $x$ (high energy), the gluon density grows rapidly ($xg(x) \sim x^{-\lambda}$), eventually reaching a regime of "saturation" where non-linear gluon recombination effects become important. The Color Glass Condensate formalism extends the parton model to this regime.

4. **Electron-Ion Collider:** The planned EIC at Brookhaven will provide precision measurements of the proton's partonic structure, including the gluon PDF (poorly known at large $x$), the quark sea flavor asymmetry, and the spin structure (how the proton's spin arises from quark and gluon spins and orbital angular momentum).

5. **Proton spin puzzle:** The parton model provides the framework for decomposing the proton's spin ($1/2$) into contributions from quark spins, gluon spins, and orbital angular momentum: $\frac{1}{2} = \frac{1}{2}\Delta\Sigma + \Delta G + L_q + L_g$. EMC measurements (1988) found that quark spins contribute only $\sim 25\%$, initiating the "proton spin crisis" that remains an active area of research.
