# Dimensional flow in discrete quantum geometries

**Author(s):** Gianluca Calcagni, Daniele Oriti, Johannes Thurigen
**Year:** 2015
**Journal:** Physical Review D 91, 084047 (2015)
**arXiv:** 1412.8390
**Relevance:** HIGH

---

## Abstract

In various theories of quantum gravity, one observes a change in the spectral dimension from the topological spatial dimension $d$ at large length scales to some smaller value at small, Planckian scales. While the origin of such a flow is well understood in continuum approaches, in theories built on discrete structures a firm control of the underlying mechanism is still missing. We shed some light on the issue by presenting a particular class of quantum geometries with a flow in the spectral dimension, given by superpositions of states defined on regular complexes. For particular superposition coefficients parametrized by a real number $0 < \alpha < d$, we find that the spatial spectral dimension reduces to $d_s \simeq \alpha$ at small scales. The spatial Hausdorff dimension of such class of states varies between 1 and $d$, while the walk dimension takes the usual value $d_w = 2$. Therefore, these quantum geometries may be considered as fractal only when $\alpha = 1$, where the "magic number" $D_s \simeq 2$ for the spectral dimension of spacetime, appearing so often in quantum gravity, is reproduced as well. These results apply, in particular, to special superpositions of spin-network states in loop quantum gravity, and they provide more solid indications of dimensional flow in this approach.

---

## Key Arguments and Derivations

### I. Introduction and Motivation

The paper addresses the challenge of identifying good geometric observables in nonperturbative, background-independent quantum gravity approaches where fundamental degrees of freedom are intrinsically discrete -- specifically loop quantum gravity (LQG), spin-foam models, and group field theory (GFT). The spectral dimension $d_s$, defined via the scaling of the heat-kernel trace, has attracted attention due to the observation of dimensional flow ($d_S: D \to \sim 2$ in the UV) across many approaches (CDT, asymptotic safety, Horava-Lifshitz gravity).

While modified dispersion relations provide an explanation for dimensional flow in smooth geometries, the mechanism in discrete approaches (like CDT) remains unclear. The authors take a direct approach within a formalism close to LQG, studying superpositions of quantum states defined on regular complexes.

A key finding from their earlier work (Ref. [27]) is that individual lattice-based quantum geometry states show NO genuine dimensional flow -- the spectral dimension simply interpolates between 0 (below lattice scale) and $d$ (above lattice scale) with discretization artifacts. True dimensional flow requires superpositions over states based on different complexes.

### II. Construction of Superposition States

**Discrete quantum states of geometry:** A state $|{j_c}, \mathcal{C}\rangle$ is defined by an assignment of quantum numbers $j_c$ to cells $c$ of a combinatorial complex $\mathcal{C}$, diagonalizing volume operators:

$$\hat{V}_c^{(p)} |{j_c}, \mathcal{C}\rangle \propto l^p(j_{c'}) |{j_c}, \mathcal{C}\rangle$$

In LQG (4 spacetime dimensions, $d=3$ spatial), spin-network states have area spectrum $l(j_f) = [j_f(j_f+1) + C]^{1/4}$ with quantization ambiguity parameter $C$.

**Restricted superpositions:** The authors restrict to states $|j, \mathcal{C}\rangle$ with a single quantum number $j_c = j$ for all cells (equilateral lattices), and consider superpositions:

$$|\psi\rangle = \sum_{j,\mathcal{C}} a_{j,\mathcal{C}} |j, \mathcal{C}\rangle$$

with a fixed-volume constraint $V_0 = \langle j, \mathcal{C}_N | \hat{V} | j, \mathcal{C}_N \rangle \propto N^d l^d(j)$, which fixes lattice size $N = N(j)$ for given $j$. The states are then:

$$|V_0, j_{\min}, j_{\max}\rangle := \sum_{j=j_{\min}}^{j_{\max}} a_j |j, \mathcal{C}_{N(j)}\rangle$$

Three scales are involved: minimal length $l(j_{\min})$, intermediate scale $l(j_{\max})$, and overall volume $V_0^{1/d}$.

### III. Spectral Dimension Calculation

The quantum Laplacian on a complex $\mathcal{C}$ acts on fields on $d$-cells:

$$-(\Delta_\mathcal{C} \phi)_a = \sum_{b \sim a} (\Delta_\mathcal{C})_{ab} (\phi_a - \phi_b) = \frac{1}{V_a^{(d)}} \sum_{b \sim a} \frac{V_{ab}^{(d-1)}}{l_{ab}^*} (\phi_a - \phi_b)$$

The spectral dimension of a quantum state $|\psi\rangle$ is defined via the expectation value of the heat trace operator:

$$d_s^\psi(\tau) := -2 \frac{\partial}{\partial \ln \tau} \ln \langle \hat{P}(\tau) \rangle_\psi$$

Under the key assumption that $\langle j, \mathcal{C} | \hat{\Delta}_\mathcal{C} | j, \mathcal{C} \rangle_{ab} \propto l^{-2}(j) (\Delta_\mathcal{C})_{ab}$, the heat-trace expectation value simplifies to:

$$\langle \hat{P}(\tau) \rangle_\psi \propto \sum_{j,\mathcal{C}} |a_{j,\mathcal{C}}|^2 \mathrm{Tr}_\mathcal{C} \, e^{\tau l^{-2}(j) \Delta_\mathcal{C}}$$

For infinite lattices $\mathcal{C}_\infty = \mathbb{Z}^d$, the heat trace has an analytic form:

$$P_{\mathcal{C}_\infty}(\tau) = [e^\tau I_0(\tau)]^d$$

where $I_0$ is the modified Bessel function of the first kind.

For a single state, $d_s \simeq d$ for $\tau \gg l^2(j)$ and $d_s \simeq 0$ for $\tau \ll l^2(j)$, with a discretization-artifact peak near $\tau \approx l^2(j)$ -- no genuine dimensional flow.

### IV. The Alpha Parameter and Dimensional Flow

For power-law spectra $l(j) \simeq j^\beta$ and power-law superposition coefficients $a_j \propto j^\gamma$, the parameter:

$$\alpha := -\frac{2\gamma + 1}{\beta}$$

controls the dimensional flow. The key result is a change of variable $k(j) := l^{-\alpha}(j)$ that transforms the heat trace into a uniformly weighted sum:

$$\langle \hat{P}(\tau) \rangle \propto \sum_k \left[ e^{-k^{2/\alpha} \tau} I_0(k^{2/\alpha} \tau) \right]^d$$

**Results by range of $\alpha$:**

- **$0 < \alpha < d$**: True dimensional flow. IR: $d_s = d$ (topological dimension recovered). Below lattice scale: $d_s = 0$ (discreteness artifact). Between these scales: plateau at $d_s = \alpha$, independent of topological dimension $d$. For $j_{\max} \to \infty$, the plateau extends indefinitely. Results are independent of the spacing of quantum labels $j$.

- **$\alpha < 0$**: No superposition effect; profile equals that of the single maximal state $|j_{\max}, \mathcal{C}_\infty\rangle$.

- **$\alpha > d$**: No superposition effect; profile equals that of the single minimal state $|j_{\min}, \mathcal{C}_\infty\rangle$.

Other coefficient classes tested: exponential (dominated by $j_{\max}$ or $j_{\min}$), Gaussian (dominated by peak $j_0$), trigonometric (adds oscillations). Linear combinations of power functions with multiple scaling regimes $\gamma_1, \gamma_2, \ldots$ yield multiple plateaux $\alpha_1, \alpha_2, \ldots$

### V. Walk Dimension

The walk dimension is defined via mean square displacement scaling: $\langle X^2 \rangle_y(\tau) \propto \tau^{2/d_w}$. On the hypercubic lattice, an exact calculation using Bessel function identities gives:

$$\langle X^2 \rangle_0^{\mathcal{C}_\infty}(\tau) = d\tau$$

so $d_w^{\mathcal{C}_\infty} = 2$, as in the continuum. For quantum superpositions, $\langle X^2 \rangle \propto \tau$ regardless of coefficients $a_j$, giving:

$$d_w^{V_0, j_{\min}, j_{\max}} = 2$$

universally. The walk dimension shows no quantum effects from superpositions.

### VI. Hausdorff Dimension

On the lattice, the volume of a ball of graph-distance radius $R$ is:

$$V_{\mathcal{C}_\infty}(R) = 2d \binom{R+d-1}{d}$$

giving Hausdorff dimension $d_h^{\mathcal{C}_\infty} = d$ for $R \gg 1$ and $d_h^{\mathcal{C}_\infty} = 1$ for $R \ll 1$. Numerical calculations on superposition states show qualitatively similar results -- only the scale and steepness of flow between plateaux is modified, not the plateau values. No genuine quantum effect on Hausdorff dimension from superpositions.

### VII. Fractal Characterization

The fractal relation $d_h = (d_w/2) d_s$ simplifies to $d_h = d_s$ for $d_w = 2$. This is obeyed trivially in the IR (both equal $d$). In the UV above the lattice scale, $d_h \simeq 1$, so the fractal relation holds only for $\alpha = 1$, where $d_s = 1$ as well. Only for $\alpha = 1$ can the quantum superposition be called a true fractal.

The case $\alpha = 1$ is also the only one reproducing the "magic number" $D_s = d_s + 1 \simeq 2$ for spacetime spectral dimension seen across quantum gravity approaches. However, the authors note this value depends on the choice of states, not on the dynamical UV properties of the full theory -- arguing against its universality as a renormalizability criterion.

---

## Key Results

1. Individual discrete quantum geometry states (single lattice) show NO genuine dimensional flow -- only discretization artifacts.
2. Superpositions of states over different complexes with power-law coefficients $a_j \propto j^\gamma$ and spectrum $l(j) \simeq j^\beta$ produce genuine dimensional flow controlled by $\alpha = -(2\gamma+1)/\beta$.
3. For $0 < \alpha < d$: spectral dimension flows from $d$ (IR) to $\alpha$ (UV plateau), independent of topological dimension.
4. Walk dimension $d_w = 2$ universally, for all superpositions -- no quantum corrections.
5. Hausdorff dimension shows no genuine quantum superposition effects, only lattice discreteness artifacts.
6. True fractal geometry (satisfying $d_h = d_w d_s / 2$) obtained only for $\alpha = 1$, which also reproduces the "magic number" $D_s \simeq 2$ for spacetime.
7. The UV value of $d_s$ depends on the choice of quantum states, not on dynamical UV properties of the theory -- questioning the universality of $D_s = 2$ as a renormalizability criterion.
8. Results apply to kinematical LQG states (spin-network superpositions), spin-foam models, and group field theory.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Discrete Laplacian | $-(\Delta_\mathcal{C} \phi)_a = \frac{1}{V_a^{(d)}} \sum_{b \sim a} \frac{V_{ab}^{(d-1)}}{l_{ab}^*} (\phi_a - \phi_b)$ | Eq. (7) |
| Quantum heat trace operator | $\hat{P}(\tau) := \mathrm{Tr} \, e^{\tau \hat{\Delta}}$ | Eq. (9) |
| Spectral dimension (quantum) | $d_s^\psi(\tau) := -2 \frac{\partial}{\partial \ln \tau} \ln \langle \hat{P}(\tau) \rangle_\psi$ | Eq. (10) |
| Laplacian scaling assumption | $\langle j, \mathcal{C} | \hat{\Delta}_\mathcal{C} | j, \mathcal{C} \rangle_{ab} \propto l^{-2}(j) (\Delta_\mathcal{C})_{ab}$ | Eq. (12) |
| Heat trace on infinite lattice | $P_{\mathcal{C}_\infty}(\tau) = [e^\tau I_0(\tau)]^d$ | Eq. (14) |
| Heat trace for superpositions | $\langle \hat{P}(\tau) \rangle \propto \sum_j |a_j|^2 [e^{l^{-2}(j)\tau} I_0(l^{-2}(j)\tau)]^d$ | Eq. (16) |
| Power-law spectrum | $l(j) \simeq j^\beta$ | Eq. (17) |
| Power-law coefficients | $a_j \propto j^\gamma$ | Eq. (18) |
| Alpha parameter | $\alpha := -(2\gamma + 1)/\beta$ | Eq. (19) |
| Uniformly weighted heat trace | $\langle \hat{P}(\tau) \rangle \propto \sum_k [e^{-k^{2/\alpha}\tau} I_0(k^{2/\alpha}\tau)]^d$ | Eq. (25) |
| Walk dimension definition | $d_w(\tau) := 2 \left( \frac{\partial \ln \langle X^2 \rangle_y}{\partial \ln \tau} \right)^{-1}$ | Eq. (27) |
| Walk dimension on lattice | $d_w^{\mathcal{C}_\infty} = 2$ | Eq. (32) |
| Hausdorff dimension (lattice) | $d_h^{\mathcal{C}_\infty} = R[\psi(R+d) - \psi(R)]$ | Eq. (38) |
| Fractal relation | $d_h = \frac{d_w}{2} d_s$ | Eq. (45) |
| Volume-fixed state | $|V_0, j_{\min}, j_{\max}\rangle := \sum_{j=j_{\min}}^{j_{\max}} a_j |j, \mathcal{C}_{N(j)}\rangle$ | Eq. (6) |
| LQG area spectrum | $l(j_f) = [j_f(j_f + 1) + C]^{1/4}$ | Eq. (2) |

---

## Relevance to Phonon-Exflation

This paper demonstrates that dimensional flow in discrete quantum gravity is not a property of individual lattice states but emerges from quantum superpositions over states with different combinatorial structures. For the phonon-exflation framework, where spacetime emerges from a discrete M4 x SU(3) substrate with a spectral Dirac operator, this result is directly relevant: the spectral dimension flow $d_s: d \to \alpha$ is controlled by the superposition coefficients (the quantum state), not the Lagrangian. The parameter $\alpha$ governing the UV spectral dimension depends on the interplay between the geometric spectrum and the superposition weights -- analogous to how the tau-dependent Dirac spectrum on SU(3) could produce scale-dependent effective dimensionality. The finding that $d_w = 2$ is universal while $d_s$ flows provides a concrete mechanism for how discrete geometry can look continuum at large scales while being fundamentally different at short distances.
