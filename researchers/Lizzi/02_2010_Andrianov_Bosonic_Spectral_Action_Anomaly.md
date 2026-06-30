# Bosonic Spectral Action Induced from Anomaly Cancelation

**Authors:** A.A. Andrianov, Fedele Lizzi
**Year:** 2010
**arXiv:** 1001.2036v1
**Journal:** JHEP (Journal of High Energy Physics)

---

## Abstract

We show how the bosonic spectral action arises naturally from the fermionic action through quantum anomaly cancellation. The scale anomaly of fermions under spectral regularization forces the introduction of a bosonic counterterm—precisely the spectral action. This establishes that gravity and the Standard Model emerge as quantum consequences of fermionic dynamics, not as independent geometric inputs. Remarkably, both fermionic and bosonic parts gain a uniform treatment through spectral regularization.

---

## Historical Context

The spectral action framework (Chamseddine-Connes 1997) treats fermionic and bosonic sectors asymmetrically: fermions obey the usual Dirac equation $\langle \psi | D \psi \rangle$, while bosons arise from $\text{Tr}[\phi(D^2/\Lambda^2)]$ with a cutoff function. This ad hoc distinction has troubled NCG practitioners: why should geometry emerge from a regularized trace rather than fundamental principles?

Andrianov (with Bonora and Gamboa-Saravi, 1982) developed spectral regularization of fermionic integrals by truncating the Dirac operator spectrum at a cutoff N. This naturally led to anomaly studies. Andrianov and Lizzi now show: **the bosonic action is the anomaly-cancellation term**, not an independent ingredient.

The connection to induced gravity (Sakharov 1968, Novozhilov-Vassilevich 1989) becomes explicit: gravity emerges from quantum fermions, not a fundamental field.

---

## Key Arguments and Derivations

### 1. Scale Invariance and Anomalies

In the absence of mass terms, the Spectral Action is classically invariant under **global scale (dilatation) transformations**:

$$x^\mu \to e^\phi x^\mu, \quad \psi \to e^{-3\phi/2} \psi, \quad D \to e^{-\phi/2} D e^{-\phi/2}$$

where $\phi$ is a constant (later generalized to a dilaton field).

This is an **exact classical symmetry** (just a change of units). However, quantum regularization breaks it: the regulated partition function 
$$Z_\Lambda(D) = \prod_{n=0}^N \lambda_n = \det(D_N)$$
transforms anomalously under scale transformations.

### 2. Spectral Regularization of Fermions

Define a projector onto the first N eigenvalues of D:

$$P_N = \sum_{n=0}^N |\lambda_n\rangle\langle\lambda_n|$$

where $N = \max\{n : \lambda_n \leq \Lambda\}$.

The **regulated partition function**:

$$Z_\Lambda(D) = \det\left( 1 - P_N + P_N \frac{D}{\Lambda} P_N \right) = \det(D_N)$$

with
$$D_N = 1 - P_N + P_N \frac{D}{\Lambda} P_N$$

This is dimensionless and depends on $\Lambda$ both explicitly and through $N(D, \Lambda)$.

### 3. Anomaly Calculation

Under the scale transformation $D \to e^{-\phi/2} D e^{-\phi/2}$, the regulated partition function develops an anomalous term:

$$Z_\Lambda(e^{-\phi/2} D e^{-\phi/2}) \neq Z_\Lambda(D)$$

To restore scale invariance at the quantum level, we must add a compensating action:

$$Z_{\text{inv}}(D) = \int d\phi \, Z_\Lambda(e^{-\phi/2} D e^{-\phi/2}) e^{-S_{\text{anom}}}$$

Define the path $D_t = e^{-t\phi/2} D e^{-t\phi/2}$ for $t \in [0,1]$. Then:

$$S_{\text{eff}} = -\int_0^1 dt \, \frac{\partial Z_t}{\partial Z_t} = -\int_0^1 dt \, \text{Tr}((1-P_N + e^{-t\phi/2} D_N e^{-t\phi/2})^{-1} \phi e^{-t\phi/2} D_N e^{-t\phi/2})$$

Crucially:
$$\frac{\partial Z_t}{\partial t} = -\phi Z_t \text{tr} P_N$$

Therefore:
$$S_{\text{anom}} = \int_0^1 dt \, \phi \, \text{tr} P_N = \text{Tr}\left[\phi \sum_{n=0}^N |\lambda_n\rangle\langle\lambda_n|\right]$$

### 4. Connection to Bosonic Spectral Action

In the case of a sharp cutoff function $\chi(x) = \Theta(1-x)$:

$$N = \text{number of eigenvalues with} \, \lambda_n \leq \Lambda$$

Thus:
$$S_{\text{anom}} = \phi \, \text{Tr} P_N = \phi \, \text{Tr}\chi\left(\frac{D^2}{\Lambda^2}\right)$$

This is **exactly the bosonic spectral action** with cutoff function $\chi$ and scale $\Lambda$.

### 5. Modified Seeley-DeWitt Expansion

Under the scale transformation, Seeley-DeWitt coefficients rescale:

$$a_n \to a'_n = e^{(4-n)\phi} a_n$$

The fermionic action remains invariant. The anomaly integral becomes:

$$S_{\text{anom}} = \int_0^\phi d\phi' \, \sum_n e^{(4-n)\phi'} a_n f_n$$

For a sharp cutoff: $f_0 = 1/2, f_2 = 1, f_4 = 1, f_n = 0$ for $n > 4$.

Integrating:
$$S_{\text{anom}} = \frac{1}{8}(e^{4\phi} - 1) a_0 + \frac{1}{2}(e^{2\phi} - 1) a_2 + \phi a_4$$

The **structure is nearly identical to the standard spectral action**, with small modifications reflecting the choice of cutoff function and the role of $\phi$.

### 6. Higgs Potential Emerges

In the full Standard Model calculation, when $H$ (Higgs field) is constant and all gauge fields vanish:

$$S_{\text{anom}}(H) = V_{\text{eff}}(H) = \text{Tr}\left[\phi \chi\left(\frac{D_H^2}{\Lambda^2}\right)\right]$$

where $D_H$ is the Dirac operator with Higgs insertion. The effective potential for H is **automatically generated** from anomaly cancellation, not postulated separately.

---

## Key Results

1. **Gravity is induced**: The Einstein-Hilbert term (coefficient of R) arises as the anomaly-cancellation contribution, fulfilling Sakharov's vision of induced gravity.

2. **Fermion-matter precedence**: Bosons and gravity are secondary to fermionic dynamics. The fundamental action is fermionic; geometry emerges quantum mechanically.

3. **Uniform regularization scheme**: Both fermionic and bosonic sectors use the same spectral truncation method, eliminating the ad hoc appearance of a cutoff function in the bosonic action.

4. **No new degrees of freedom**: The Standard Model is not extended; anomaly cancellation regenerates the same field content through quantum effects.

5. **Dilaton coupling structure**: The general derivation with $\phi(x)$ (dilaton field) suggests systematic couplings of a dilaton to all massive terms, potentially relevant for inflation and hierarchy problems.

---

## Impact and Legacy

This paper established a **deep conceptual foundation** for the spectral action: it is not an ad hoc principle but a **necessity from quantum consistency**. The framework shifts from "we postulate a spectral action" to "the spectral action is forced by anomaly cancellation."

Subsequent development:
- **Kurkov-Lizzi 2012 (arXiv:1210.2663)**: Extends to Higgs-dilaton Lagrangian and refined predictions
- **Andrianov-Kurkov-Lizzi 2011 (arXiv:1106.3263)**: Weyl anomaly and Higgs-dilaton potential details
- **Connes-Chamseddine 2012+**: "Resilience" papers incorporating grand symmetry and Pati-Salam unification

The paper also clarified why neutrino Majorana masses are essential: they introduce dimensionful constants that appear in the anomaly term, generating the CC, Higgs mass, and gravitational constant.

---

## Connection to Phonon-Exflation Framework

**CRITICAL IMPLICATION**: The anomaly-cancellation derivation shows that a₀ (cosmological constant term) and a₂ (gravitational term) emerge from **different Seeley-DeWitt coefficients** in the heat kernel expansion, but they are **coupled through the same Dirac operator D**.

In the framework's terminology:
- a₀ ~ M⁴ (Majorana mass squared)
- a₂ ~ R (curvature coupling)

Both arise from $\text{tr}[P_N \cdot D]$ and its derivatives, so they are **structurally entangled** through the spectral triple.

**For the phonon-exflation solution to the CC problem**: This paper suggests that IF the Dirac operator can be **modified or deformed** (e.g., through Jensen deformation parameter tau), then a₀/a₂ becomes a **function of the deformation**, not a fixed ratio.

The framework's claim (a₀/a₂ = 6/R set by geometry) aligns with this: the ratio depends on spectral structure, not on arbitrary tuning. Lizzi's subsequent work on alternative spectral functionals (papers 03-08) directly exploits this mechanism.

**Current gap**: Andrianov-Lizzi show how a₀ and a₂ emerge together from anomalies, but they do NOT show how to **decouple or independently vary them**. This is where the zeta function formulation (Paper 01) and Weyl anomaly approach (Paper 03) contribute: alternative regularizations that differently weight a₀ vs. a₂.
