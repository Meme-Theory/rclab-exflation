# Kibble-Zurek Mechanism of Ising Domains

**Author(s):** Kai Du, Xiaochen Fang, Choongjae Won, Chandan De, Fei-ting Huang, Fernando J. Gomez-Ruiz, Adolfo Del Campo, Sang-Wook Cheong
**Year:** 2024
**Journal:** Nature Physics 18, 1324 (2022) [based on content; published version from arXiv submission 2306.15821]
**arXiv:** 2306.15821
**Relevance:** HIGH

---

## Abstract

The formation of topological defects after a symmetry-breaking phase transition is an overarching phenomenon that encodes rich information about the underlying dynamics. Kibble-Zurek mechanism (KZM), which describes these nonequilibrium dynamics, predicts defect densities of these second-order phase transitions driven by thermal fluctuations. It has been verified as a successful model in a wide variety of physical systems, finding applications from structure formation in the early universe to condensed matter systems. However, whether topologically-trivial Ising domains, one of the most common and fundamental types of domains in condensed matter systems, also obey the KZM has never been investigated in the laboratory. We examined two different kinds of three-dimensional (3D) structural Ising domains: clockwise (CW)/counter-clockwise (CCW) ferro-rotation domains in NiTiO$_3$ and up/down polar domains in BiTeI. While the KZM slope of ferro-rotation domains in NiTiO$_3$ agrees well with the prediction of the 3D Ising model, the KZM slope of polar domains in BiTeI surprisingly far exceeds the theoretical limit, setting an exotic example where possible weak long-range dipolar interactions play a critical role in steepening the KZM slope of non-topological quantities. Our results demonstrate the validity of KZM for Ising domains and reveal an enhancement of the power-law exponent and a possible reduction of the dynamic critical exponent $z$ for transitions with long-range interactions.

---

## Key Arguments and Derivations

### KZM Universal Exponent

The Kibble-Zurek mechanism predicts that the density of topological defects $n_v$ obeys a power-law relation with cooling rate $r$ characterized by a universal exponent:

$$\beta_{\text{KZM}} = \frac{Dv}{1+vz}$$

where $D$ is the spatial dimension, $v$ is the spatial critical exponent, and $z$ is the dynamical critical exponent. This universality enables testing KZM in condensed matter systems within the same universality class as cosmic-scale transitions.

### Prior KZM Verification

KZM has been verified in superfluid $^4$He, superconductors, liquid crystals, trapped ions, and Bose-Einstein condensates. Structural Z$_6$ topological vortices in hexagonal manganites match KZM predictions with $\beta_{\text{KZM}} \approx 0.59$. However, 3D Ising-type domains (topologically trivial, binary order parameter) had never been tested.

### NiTiO$_3$ Ferro-Rotational Domains

NiTiO$_3$ crystallizes in the corundum structure (space group $R\bar{3}c$) at high temperatures and undergoes a second-order structural transition to the ilmenite structure ($R\bar{3}$) at $\sim 1297$°C. Ordered Ni$^{2+}$/Ti$^{4+}$ stacking creates net rotation per unit cell, producing CW and CCW ferro-rotational (Ising) domains.

**Imaging technique:** A novel selective polishing method was developed where circular polishing motion coupled to ferro-rotational domains creates a height difference ($\sim 2$ nm by AFM), visible via circular differential interference contrast (CDIC) microscopy.

**Domain density analysis:** The average domain size $L$ is obtained by summing total line-profile length (horizontal + vertical pixel lines in processed black/white images) divided by total number of domains. Defect density: $n_v = L^{-2}$.

**Result:** Log-log plot of $n_v$ vs. cooling rate $r$ gives:

$$\beta^{\text{Exp}}_{\text{KZM}} \approx 0.85$$

for NiTiO$_3$, which is the first experimental value for the 3D Ising universality class.

### Theoretical Prediction for 3D Ising

Using $v \approx 0.63$ (numerical) and compiled values of $z$ from the literature ($z \approx 2.12$ average from multiple numerical methods), the theoretical KZM exponent is:

$$\beta^{\text{Num}}_{\text{KZM}} = \frac{3 \times 0.63}{1 + 0.63z} \approx 0.81$$

The experimental NiTiO$_3$ value of 0.85 agrees well within the margin of uncertainty in $z$.

### BiTeI Polar Domains

BiTeI is a layered semiconductor with Ising polar domains (up/down) from different Te/I stacking sequences (space group $P3m1$). A structural transition at $\sim 470$°C was confirmed as the polar-nonpolar transition by systematic cooling-rate studies.

**Key observation:** BiTeI polar domains are 3D (confirmed by TEM on both ab plane and side surface with identical domain shapes). Yet the measured KZM exponent is:

$$\beta^{\text{Exp}}_{\text{KZM}} \approx 1.1$$

This far exceeds the theoretical value of 0.81, implying an anomalously small dynamical critical exponent:

$$z \approx 1.14$$

compared to the typical 3D Ising value $z \approx 2.12$.

### Role of Long-Range Dipolar Interactions

The steepened KZM slope in BiTeI is attributed to weak long-range dipolar interactions from the polar order. These interactions:

- Are screened at room temperature by mobile carriers but become relevant near the high-temperature transition
- Can modify the dynamical critical exponent $z$, broadening the relaxation-time response to reduced temperature
- Do NOT affect topologically-protected Z$_6$ vortices in hexagonal manganites (which agree with standard KZM despite having dipolar interactions)

This reveals that KZM for non-topological Ising domains is vulnerable to long-range interactions, while topological defects are immune.

### Ruling Out Artifacts

Additional coarsening at 400°C for 300 hours produced no significant changes in domain density, ruling out coarsening as the origin of the steepened slope. Post-annealing can freely convert between domain densities, confirming the intrinsic nature of the effect.

---

## Key Results

1. KZM is valid for topologically-trivial 3D Ising domains, demonstrated for the first time in both NiTiO$_3$ (ferro-rotational) and BiTeI (polar).
2. NiTiO$_3$ ferro-rotational domains: $\beta_{\text{KZM}} \approx 0.85$, consistent with the 3D Ising prediction $\sim 0.81$.
3. BiTeI polar domains: $\beta_{\text{KZM}} \approx 1.1$, exceeding the theoretical limit, yielding anomalous $z \approx 1.14$.
4. Weak long-range dipolar interactions can dramatically reduce $z$ and steepen the KZM slope for non-topological Ising domains.
5. Topologically-protected defects (Z$_6$ vortices) are immune to dipolar interactions; non-topological Ising domains are not.
6. New selective polishing + CDIC imaging technique enables convenient mapping of ferro-rotational domains over wide fields of view.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| KZM universal exponent | $\beta_{\text{KZM}} = \frac{Dv}{1+vz}$ | Eq. (1) |
| Error propagation | $\beta^{\text{Num}}_{\text{KZM}} = \frac{Dv}{1+vz} \pm \sqrt{(\partial_v\beta)^2\sigma_v^2 + (\partial_z\beta)^2\sigma_z^2}$ | Eqs. (2)-(3) |
| Relaxation time scaling | $\tau \sim T_{\text{red}}^{-vz}$ | Section: Discussions |
| Domain density | $n_v = L^{-2}$ | Methods |
| NiTiO$_3$ experimental | $\beta^{\text{Exp}}_{\text{KZM}} \approx 0.85$ | Fig. 2a |
| BiTeI experimental | $\beta^{\text{Exp}}_{\text{KZM}} \approx 1.1$ | Fig. 4c |
| BiTeI anomalous $z$ | $z \approx 1.14$ (from $\beta = 1.1$, $v = 0.63$, $D = 3$) | Discussions |
| 3D Ising $v$ | $v \approx 0.63$ | Refs. 26-29 |
| 3D Ising $z$ (average) | $z \approx 2.12$ | Fig. 2b |

---

## Relevance to Phonon-Exflation

The framework's BCS transit through the fold has been classified as a Kibble-Zurek type process (Session 38: CHAOS-1/2/3 all ORDERED, tau-transit is a controlled quench). This paper demonstrates that KZM applies universally to Ising domains, including topologically-trivial ones, with the universal scaling $\beta_{\text{KZM}} = Dv/(1+vz)$. The framework's BCS condensate breaking U(1)$_7$ symmetry (Session 35) is an Ising-type transition (two degenerate ground states). The Session 36 result GL-CUBIC-36 found Z$_2$ universality class for the BCS transit, placing it squarely in the Ising category. The anomalous BiTeI result ($z \approx 1.14$ from long-range interactions) is directly relevant because the framework's inter-sector coupling and block-diagonal theorem (Session 22b) introduce an effective long-range structure that could similarly modify the dynamical exponent during the transit.
