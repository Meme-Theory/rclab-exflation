# High energy bosons do not propagate

**Authors:** M.A. Kurkov, Fedele Lizzi, D. Vassilevich
**Year:** 2014
**arXiv:** 1312.2235
**Journal:** Physics Letters B, Vol. 731

---

## Abstract

We demonstrate that in the spectral action framework with cutoff regularization, high-energy bosons (scalar, gauge) do not propagate. The propagator diverges as p⁴ instead of decreasing, violating locality and unitarity at high momenta. This identifies a critical limitation of the cutoff spectral action and motivates the zeta function regularization (Papers 01, 04).

---

## Key Problem

### 1. Cutoff Action Propagator Structure

The cutoff spectral action (Chamseddine-Connes) produces a Lagrangian density:

$$\mathcal{L} = \sum_{n=0}^{2} \Phi_n \Lambda^{4-2n}$$

where Φ_n contain field operators. At high momenta p >> Λ, the propagators behave as:

**Scalar Higgs**: 
$$P_H(p^2) \sim \frac{\beta_1 \Lambda^4}{\beta_3 p^4}$$

As p → ∞, the numerator dominates over p⁴ denominator.

**Gauge boson**:
$$P_V(p^2) \sim \frac{\beta_4 \Lambda^4}{p^4}$$

Both diverge as p⁴, violating the essential requirement that propagators decay at high momenta (necessary for renormalizability and unitarity).

### 2. Locality Violation

The ultraviolet asymptotics show that bosonic contributions to loop diagrams have structure:

$$\Gamma_{\text{loop}} \sim \int \frac{d^4 p}{(2\pi)^4} \frac{\beta p^4}{\Lambda^4 + p^4 + \text{mass terms}}$$

With p >> Λ, this becomes:

$$\Gamma \sim \int \frac{d^4 p}{(2\pi)^4} \beta = \infty$$

The loop integral diverges regardless of the number of loops. A naive hope: "these diagrams cancel for special field content" is **false**. There is no miracle cancellation.

### 3. Four-Fermion Interactions Required

To cure the divergences, one must add **four-fermion interactions** to the Lagrangian:

$$\mathcal{L}_{4F} = \frac{g_{4F}}{\Lambda^2} (\bar{\psi}_1 \gamma^\mu \psi_1)(\bar{\psi}_2 \gamma_\mu \psi_2) + \cdots$$

These are **non-renormalizable by power-counting**. QFTs with four-fermion interactions are notoriously difficult to quantize consistently (Fermi theory of weak interactions required the W boson to avoid these troubles).

---

## Analysis of Spectral Dimensions

The **spectral dimension** D_s is defined as the effective dimension probed by particle propagators:

$$D_s = \lim_{p \to \infty} \log |\text{propagator}| / \log p$$

For standard renormalizable theories: D_s = 4.

For the cutoff spectral action: D_s(scalars) = 4, but the **convergence properties** are violated—the propagator increases instead of decreasing.

---

## Resolution via Zeta Regularization

The zeta function spectral action (Papers 01, 04) **eliminates this problem**. The zeta action contains only dimension-≤4 operators:

$$\mathcal{L}_\zeta = \text{(dimension 4 operators only)}$$

Propagators now have canonical form:

$$P_H^{(\zeta)} \sim \frac{1}{p^2 + m_H^2}$$

At high momenta, p² in the denominator ensures decay: 
$$P_H^{(\zeta)}(p^2) \sim \frac{1}{p^2} \to 0 \text{ as } p \to \infty$$

**Consequence**: The zeta spectral action is renormalizable, while the cutoff version is not.

---

## Key Results

1. **Cutoff action is not an effective theory**: It cannot be safely used above the cutoff scale Λ because it is fundamentally non-local (bosons don't propagate) and non-renormalizable.

2. **Zeta action is fundamental**: Unlike the cutoff version, the zeta formulation can be used from TeV scales to Planck scale without effective-theory caveats.

3. **Spectral dimension mismatch**: In the cutoff case, scalar spectral dimension is nominally D_s = 4, but the actual UV behavior (propagator → ∞) is inconsistent with 4D renormalization theory.

4. **Four-fermion pathology necessary in cutoff version**: The theory requires non-renormalizable interactions to achieve consistency, analogous to Fermi weak interaction theory before the W boson was discovered.

---

## Impact and Legacy

This paper diagnosed the **fundamental inconsistency** of cutoff spectral action phenomenology. It clarified why:
- The cutoff action is best viewed as a **classical effective action** valid only below Λ
- Quantization requires regularization at the classical level (zeta function approach)
- The apparent "predictive power" of cutoff phenomenology (Higgs mass predictions) is achieved despite the underlying non-renormalizability

The paper motivated:
- Kurkov-Lizzi to develop zeta spectral action as the correct UV completion (Papers 01, 04)
- Van Suijlekom and collaborators to systematically reformulate spectral action with proper asymptotic behavior
- Interest in asymptotic safety scenarios (where g_i → 0 at high energy, reducing these divergences)

---

## Connection to Phonon-Exflation Framework

**CRITICAL IMPLICATION**: The phonon-exflation framework claims to compute all Standard Model parameters from spectral action at UNIFICATION SCALE (10¹⁴-10¹⁷ GeV). If using the cutoff spectral action, this computation would be **invalid** above the cutoff.

**Framework requirement**: The framework MUST use the **zeta spectral action** (Papers 01, 04) to remain consistent. The zeta formulation allows:

1. Computation at unification scale without effective-theory breakdown
2. Proper RG running from unification down to low energy
3. Consistent quantum field theory without non-renormalizable four-fermion additions

**Phonon-exflation strategy implication**: The framework's claim that "all physics emerges from spectral geometry" means all couplings and masses must be computable from D_K using zeta regularization, not cutoff regularization.

**Current status**: The framework must verify that its computed values (Higgs mass m_H = 131.8 GeV, alpha_s predictions, etc.) are **stable under RG flow** from unification to low energy when using the proper zeta spectral action, not the toy cutoff version.

This is a **rigorous consistency requirement** that has not yet been addressed in the framework literature.
