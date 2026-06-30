# Information in Black Hole Radiation

**Author(s):** Don N. Page
**Year:** 1993
**Journal:** Physical Review Letters 71, 3743-3746 (1993)
**arXiv:** hep-th/9306083
**Relevance:** CRITICAL

---

## Abstract

If black hole formation and evaporation can be described by an S-matrix, information would be expected to come out in black hole radiation. An estimate shows that it may come out initially so slowly, or else be so spread out, that it would never show up in an analysis perturbative in $M_{\text{Planck}}/M$, or in $1/N$ for two-dimensional dilatonic black holes with a large number $N$ of minimally coupled scalar fields.

---

## Key Arguments and Derivations

### The Information Paradox Context

Hawking's calculation of thermal emission from a stationary classical black hole led to the question: what happens to a pure quantum state that collapses to form a black hole which emits approximately thermal radiation? Hawking proposed that the black hole would eventually disappear completely and the resulting state of radiation would be mixed -- information permanently lost.

Page argues for the most conservative option: information escapes gradually with the radiation, giving an S-matrix, but at a rate that is non-perturbatively small and hence invisible to any order-by-order analysis.

### Random Pure State Model

The black hole and surrounding radiation are treated as two subsystems of a combined system in a random pure state. The radiation subsystem has dimension $m \sim e^{s_r}$ (where $s_r$ is the thermodynamic radiation entropy) and the black hole subsystem has dimension $n \sim e^{s_h}$ (where $s_h = A/4$ is the Bekenstein-Hawking entropy).

The density matrices of the subsystems are:
$$\rho_r = \text{tr}_h \, \rho_{rh}, \qquad \rho_h = \text{tr}_r \, \rho_{rh}$$

with von Neumann (entanglement) entropy:
$$S_r = -\text{tr}_r(\rho_r \ln \rho_r) = S_h = -\text{tr}_h(\rho_h \ln \rho_h)$$

and information (deviation from maximum):
$$I_r = \ln m - S_r \approx s_r - S_r, \qquad I_h = \ln n - S_h \approx s_h - S_h$$

### The Page Curve

For a random pure state of the joint system with $m \leq n$, the average information in the smaller subsystem is:

$$I_{m,n} = \ln m + \frac{m-1}{2n} - \sum_{k=n+1}^{mn} \frac{1}{k}$$

For $1 \ll m \leq n$:
$$I_{m,n} \simeq \frac{m}{2n} \sim e^{s_r - s_h}$$

For $m \geq n$:
$$I_{m,n} \approx \ln m - \ln n + \frac{n}{2m}$$

This defines the **Page curve**: the entanglement entropy rises linearly during the first half of evaporation (when $m < n$), then decreases during the second half (when $m > n$), returning to zero when evaporation is complete.

### Non-Perturbative Information Rate

During adiabatic evaporation with parameter $x = (E-M)/M$:

$$I_r \sim \exp\left(-4\pi E_0^2 \frac{3 - 8x}{3 + 8x}\right)$$

The initial rate of information outflow is:
$$\frac{dI}{dt} \sim e^{-4\pi/y^2}$$

where $y = M_{\text{Planck}}/E_0$ is the perturbative parameter. This is non-analytic in $y$ at $y = 0$, and therefore invisible to any finite order perturbative analysis.

### Two-Dimensional Model

For 2D dilatonic black holes with $N$ scalar fields, the Hawking temperature is $T = \lambda/2\pi$ (independent of $M$), and the entropy is $s_h = 2\pi M/\lambda = 2\pi e^{-2\phi_H}$. The semiclassical regime requires $s_h \gtrsim \pi N/12$. The expected information in radiation is:

$$I_r \sim e^{s_r - s_h} \lesssim e^{s_r - \pi N/12} = e^{s_r - \pi/(12z)}$$

where $z = 1/N$. This is again non-analytic in $z$ at $z = 0$.

---

## Key Results

1. The **Page curve** defines the expected entanglement entropy of Hawking radiation as a function of time, rising then falling, with the turnover at the "Page time" when half the entropy has been radiated.
2. Information escapes at a non-perturbatively small rate $\sim e^{-4\pi/y^2}$, invisible to any finite-order perturbative analysis.
3. To detect the information requires measuring $\sim m^2 \sim e^{2s_r}$ independent parameters of the radiation density matrix -- exponentially many measurements.
4. The Page time divides evaporation into two phases: before, the radiation is nearly maximally mixed; after, correlations between early and late radiation encode the information.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Subsystem information | $I_{m,n} \simeq \frac{m}{2n} \sim e^{s_r - s_h}$ for $m \leq n$ | Eq. (7) |
| Page information (general) | $I_{m,n} = \ln m + \frac{m-1}{2n} - \sum_{k=n+1}^{mn} \frac{1}{k}$ | Eq. (6) |
| Information for $m \geq n$ | $I_{m,n} \approx \ln m - \ln n + \frac{n}{2m}$ | Eq. (8) |
| Radiation entropy | $s_r \approx 4\pi E_0^2 \frac{8x}{3+8x}$ | Eq. (14) |
| Black hole entropy | $s_h \approx 4\pi E_0^2 \frac{3}{3+8x}$ | Eq. (15) |
| Information rate | $I_r \sim \exp\left(-4\pi E_0^2 \frac{3-8x}{3+8x}\right)$ | Eq. (16) |
| Non-perturbative rate | $\frac{dI}{dt} \sim e^{-4\pi/y^2}$ | Eq. (19) |
| 2D BH entropy | $s_h = 2\pi M/\lambda = 2\pi e^{-2\phi_H}$ | Eq. (25) |
| 2D information bound | $I_r \sim e^{s_r - \pi/(12z)}$, $z = 1/N$ | Eq. (28) |
| Entanglement entropy | $S_r = -\text{tr}_r(\rho_r \ln \rho_r)$ | Eq. (4) |

## Relevance to Phonon-Exflation

The Page curve is THE benchmark for unitary black hole evaporation. In the phonon-exflation framework, the transit produces a GGE (generalized Gibbs ensemble) with $S_{\text{ent}} = 0$ exactly (product state from integrability), so no Page curve is needed -- the framework evades the information paradox entirely. The non-perturbative character of information ($\sim e^{-S_{\text{BH}}}$) parallels the instanton action $S_{\text{inst}} = 0.069$ governing the transit mechanism.
