# Quantum Extremal Surfaces: Holographic Entanglement Entropy beyond the Classical Regime

**Author(s):** Netta Engelhardt, Aron C. Wall
**Year:** 2015
**Journal:** Journal of High Energy Physics 2015, 073 (2015)
**arXiv:** 1408.3203
**Relevance:** HIGH

---

## Abstract

We propose that holographic entanglement entropy can be calculated at arbitrary orders in the bulk Planck constant using the concept of a "quantum extremal surface": a surface which extremizes the generalized entropy, i.e. the sum of area and bulk entanglement entropy. At leading order in bulk quantum corrections, our proposal agrees with the formula of Faulkner, Lewkowycz, and Maldacena, which was derived only at this order; beyond leading order corrections, the two conjectures diverge. Quantum extremal surfaces lie outside the causal domain of influence of the boundary region as well as its complement, and in some spacetimes there are barriers preventing them from entering certain regions. We comment on the implications for bulk reconstruction.

---

## Key Arguments and Derivations

### Background: Classical Extremal Surfaces

The Ryu-Takayanagi (RT) proposal computes holographic entanglement entropy as:

$$S(A) = \frac{\text{Area}(\gamma_A)}{4G_N}$$

where $\gamma_A$ is the minimal area surface homologous to the boundary region $A$. The covariant generalization (Hubeny-Rangamani-Takayanagi, HRT) replaces "minimal" with "extremal":

$$S(A) = \frac{\text{Area}(X_A)}{4G_N}$$

where $X_A$ extremizes the area functional.

### Quantum Extremal Surfaces

Engelhardt and Wall propose that quantum corrections are incorporated by replacing the area with the **generalized entropy**:

$$S_{\text{gen}}(X) = \frac{\text{Area}(X)}{4G_N} + S_{\text{bulk}}(\Sigma_X)$$

where $S_{\text{bulk}}(\Sigma_X)$ is the von Neumann entropy of bulk quantum fields on a partial Cauchy surface $\Sigma_X$ bounded by $X$ and the boundary region $A$.

The **quantum extremal surface** (QES) is a codimension-2 surface $X$ that extremizes $S_{\text{gen}}$:

$$\frac{\delta S_{\text{gen}}}{\delta X} = 0$$

The holographic entanglement entropy is then:

$$S(A) = S_{\text{gen}}(X_{\text{QES}})$$

where $X_{\text{QES}}$ is the QES with minimal $S_{\text{gen}}$.

### Comparison to FLM Formula

At leading order in quantum corrections ($O(G_N^0)$), the QES proposal agrees with the Faulkner-Lewkowycz-Maldacena (FLM) formula:

$$S(A) = \frac{\text{Area}(X_{\text{classical}})}{4G_N} + S_{\text{bulk}}(\Sigma_{X_{\text{classical}}})$$

Beyond leading order, the QES and FLM prescriptions diverge: the QES uses the quantum-corrected extremal surface, while FLM uses the classically extremal surface.

### QES Lies Deeper than Causal Surfaces

A key result is that the QES lies outside the causal domain of influence of the boundary region $A$ and its complement $\bar{A}$. Specifically, the QES lies deeper in the bulk than the **causal surface** (the intersection of the boundaries of the causal past and future of $A$'s domain of dependence).

This is proven using the quantum focussing conjecture (QFC):

$$\frac{\delta^2 S_{\text{gen}}}{\delta V(y_1) \delta V(y_2)} \leq 0$$

which generalizes the classical focussing theorem (positive energy implies $\theta' \leq 0$ on a null congruence) to include quantum corrections.

### Barriers to QES

There exist spacetime regions that QES cannot penetrate -- "barriers". These barriers have implications for bulk reconstruction: regions behind barriers cannot be reconstructed from boundary data using the QES prescription alone.

---

## Key Results

1. The **quantum extremal surface** proposal: holographic entanglement entropy = generalized entropy evaluated on the surface extremizing $S_{\text{gen}}$.
2. This agrees with FLM at $O(G_N^0)$ but provides an all-orders prescription.
3. QES lie **deeper** in the bulk than causal surfaces -- they penetrate further into the bulk geometry.
4. The quantum focussing conjecture ensures consistency of the proposal.
5. Barriers to QES exist, limiting bulk reconstruction from boundary data.
6. The min-QES prescription (take the QES with smallest $S_{\text{gen}}$ when multiple QES exist) is the quantum generalization of the HRT proposal.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Generalized entropy | $S_{\text{gen}}(X) = \frac{\text{Area}(X)}{4G_N} + S_{\text{bulk}}(\Sigma_X)$ | Eq. (1) |
| QES condition | $\frac{\delta S_{\text{gen}}}{\delta X} = 0$ | Definition |
| Holographic EE | $S(A) = \min_{\text{QES}} S_{\text{gen}}(X)$ | Proposal |
| RT formula (classical) | $S(A) = \frac{\text{Area}(\gamma_A)}{4G_N}$ | Sec. 1 |
| FLM formula | $S(A) = \frac{\text{Area}(X_{\text{cl}})}{4G_N} + S_{\text{bulk}}(\Sigma_{X_{\text{cl}}})$ | Sec. 3.1 |
| Quantum focussing | $\frac{\delta^2 S_{\text{gen}}}{\delta V(y_1)\delta V(y_2)} \leq 0$ | Sec. 4 |
| Quantum expansion | $\Theta[X,\Sigma] = \frac{1}{\sqrt{h}}\frac{\delta S_{\text{gen}}}{\delta \lambda}$ | Sec. 2 |
| Bekenstein bound | $S_{\text{bulk}} \leq \frac{\text{Area}}{4G_N}$ | Sec. 1 |

## Relevance to Phonon-Exflation

The quantum extremal surface is the foundational concept underlying the island formula (Papers 14, 21, 23) that resolves the information paradox in holographic settings. In the phonon-exflation framework, the QES has no direct analog because there is no holographic boundary: the framework is a bottom-up emergence model, not a holographic duality. However, the generalized entropy $S_{\text{gen}} = \text{Area}/4G + S_{\text{bulk}}$ has a spectral analog: the spectral action = von Neumann entropy identity (Paper 20) shows that $\text{Tr}(h(\beta D))$ combines the geometric ("area") and quantum ("bulk entropy") contributions into a single functional. The QES extremization condition $\delta S_{\text{gen}}/\delta X = 0$ is the spectral analog of extremizing the spectral action over the internal geometry -- the same variational principle that determines the fold in $\tau$-space.
