# Note on Shape Moduli Stabilization, String Gas Cosmology and the Swampland Criteria

**Author(s):** Gabrielle A. Mitchell, Robert Brandenberger
**Year:** 2020
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2008.13251
**Relevance:** MEDIUM

---

## Abstract

In String Gas Cosmology, the simplest shape modulus fields are naturally stabilized by taking into account the presence of string winding and momentum modes. We determine the resulting effective potential for these fields and show that it obeys the de Sitter conjecture, one of the swampland criteria for effective field theories to be consistent with superstring theory.

---

## Key Arguments and Derivations

### Introduction: Swampland Criteria

The paper addresses constraints on low energy effective field theories (EFTs) that can emerge from superstring theory. Two key swampland criteria are:

1. **Distance conjecture**: The field range $\Delta\phi$ of a canonically normalized scalar must satisfy $\Delta\phi < c_1 m_{\text{pl}}$ with $c_1 \sim O(1)$.
2. **de Sitter conjecture**: The potential $V(\phi)$ must be sufficiently steep, i.e., $|V'/V| < c_2/m_{\text{pl}}$ with $c_2 \sim O(1)$.
3. **Extended de Sitter conjecture**: At a local extremum where condition (1) may not hold, one requires $V''/V < -c_3/m_{\text{pl}}^2$ with $c_3 > 0$ and $O(1)$.

In a previous paper (Laliberte and Brandenberger, arXiv:1911.00199), the radion modulus effective potential was shown to be consistent with the swampland constraints. Here, the authors extend this analysis to shape moduli.

### String Gas Cosmology Review

String gas cosmology (SGC) couples a classical background (graviton and dilaton fields) to a gas of strings. Strings have three types of states: momentum modes, oscillatory modes, and winding modes. Six extra spatial dimensions are compactified on a torus. The metric is:

$$ds^2 = g_{\mu\nu}dx^\mu dx^\nu + \gamma_{ab}dx^a dx^b$$

where Latin indices label compact dimensions and Greek indices label the 4D FRW metric. The torus is parametrized by shape and size moduli.

**Moduli stabilization principle**: Winding modes prevent expansion (energy increases with $R$), while momentum modes prevent contraction (energy increases with $1/R$). String gas coupling also stabilizes shape moduli.

### Shape Modulus Potential

The matter action for a gas of strings at temperature $\beta^{-1}$ in $D$ spacetime dimensions involves a sum over all free string states labeled by momentum numbers $n_a$, winding numbers $w_a$, oscillatory mode numbers $N$, $\tilde{N}$, and non-compact momenta $p_{nc}$.

The string mass formula for toroidal compactification is:

$$M^2_{\vec{n},\vec{w},N} = \frac{1}{R^2}\gamma^{ab}n_a n_b + \frac{R^2}{\alpha'^2}\gamma_{ab}w_a w_b + \frac{2}{\alpha'}(2N + n_a w_a - 2)$$

For a 2D torus with radius $R$ and shape parameter $\theta$, the metric is:

$$\gamma_{ab} = \begin{pmatrix} R^2 & R^2 \sin\theta \\ R^2 \sin\theta & R^2 \end{pmatrix}$$

The partition function is dominated by the lowest mass states satisfying $N=1$ and $n_a = w_a = \pm 1$. The full low energy effective action is:

$$S = \frac{1}{2\kappa_0^2}\int d^d X \sqrt{-G} e^{-2\Phi_d}\left[\hat{R}_d + 4\partial_\mu\Phi_d\partial^\mu\Phi_d - \frac{1}{4}\partial_\mu\gamma^{ac}\partial^\mu\gamma_{ab} - 2\kappa_0^2 e^{-2\Phi_d} n\langle E_1\rangle\right]$$

The canonically normalized shape modulus field is $\phi \equiv M_{\text{pl}} R\theta$, and the potential evaluates to:

$$V(\phi) = e^{-2\Phi_d} n \sqrt{p_{nc}^2 + \phi^2}$$

### Swampland Criteria Verification

The de Sitter ratio evaluates to:

$$\frac{V'}{V} = \frac{1}{\sqrt{2}} \frac{\phi}{\sqrt{p_{nc}^2 + \phi^2}} \sim \frac{1}{\sqrt{2}}\phi$$

where the last step uses the late-time limit where $p_{nc}$ is negligible (redshifted by expansion). Since $|\theta| < \pi/2$, the field range is bounded: $|\phi| < \pi/2$, satisfying the distance conjecture. The de Sitter conjecture is automatically satisfied with $c_2 = \pi/4$.

---

## Key Results

1. Shape moduli in String Gas Cosmology are stabilized by winding and momentum modes at the rectangular torus $\theta = 0$ with self-dual radius $R = 1$.
2. The effective potential for the shape modulus is $V(\phi) \propto \sqrt{p_{nc}^2 + \phi^2}$, quadratic near the minimum.
3. The de Sitter swampland conjecture is satisfied with constant $c_2 = \pi/4$.
4. The distance conjecture is satisfied because $\Delta\phi < \pi M_{\text{pl}}/2$.
5. The stabilization physics is inherently stringy: winding modes have no point-particle analogue, so these effects cannot be seen in effective field theory alone.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| de Sitter conjecture | $\|V'/V\| < c_2/m_{\text{pl}}$ | Eq. (1) |
| Extended de Sitter | $V''/V < -c_3/m_{\text{pl}}^2$ | Eq. (2) |
| Spacetime metric | $ds^2 = g_{\mu\nu}dx^\mu dx^\nu + \gamma_{ab}dx^a dx^b$ | Eq. (3) |
| String mass formula | $M^2 = \frac{1}{R^2}\gamma^{ab}n_a n_b + \frac{R^2}{\alpha'^2}\gamma_{ab}w_a w_b + \frac{2}{\alpha'}(2N + n_a w_a - 2)$ | Eq. (7) |
| Effective action | $S = \frac{1}{2\kappa_0^2}\int d^d X \sqrt{-G} e^{-2\Phi_d}[\hat{R}_d + 4\partial_\mu\Phi_d\partial^\mu\Phi_d - \frac{1}{4}\partial_\mu\gamma^{ac}\partial^\mu\gamma_{ab} - 2\kappa_0^2 e^{-2\Phi_d}n\langle E_1\rangle]$ | Eq. (8) |
| Modulus potential | $V(\phi) = e^{2\Phi_d} n (p_{nc}^2 + M^2_{1,-1,1})^{1/2}$ | Eq. (10) |
| Torus metric | $\gamma_{ab} = \begin{pmatrix} R^2 & R^2\sin\theta \\ R^2\sin\theta & R^2 \end{pmatrix}$ | Eq. (11) |
| Canonical field | $\phi \equiv M_{\text{pl}} R\theta$ | Eq. (13) |
| Mass expansion | $M^2_{1,-1,1} \sim \phi^2 + O(1)\phi^4/M_{\text{pl}}^2$ | Eq. (15) |
| Late-time potential | $V(\phi) = e^{-2\Phi_d} n \sqrt{p_{nc}^2 + \phi^2}$ | Eq. (16) |
| de Sitter ratio | $V'/V = \frac{1}{\sqrt{2}}\frac{\phi}{\sqrt{p_{nc}^2 + \phi^2}} \sim \frac{1}{\sqrt{2}}\phi$ | Eq. (17) |

---

## Relevance to Phonon-Exflation

The phonon-exflation framework posits that SU(3) internal geometry is stabilized by BCS pairing in the instanton gas, analogous to how String Gas Cosmology stabilizes shape moduli via winding and momentum modes. This paper demonstrates that moduli stabilization by stringy effects (winding + momentum duality) automatically satisfies swampland constraints, with de Sitter constant $c_2 = \pi/4$. The key structural parallel is that in both SGC and the phonon-exflation framework, the stabilizing agent is a many-body effect (string gas vs. BCS condensate) acting on the internal geometry, not a tree-level potential. The result that the effective potential is quadratic near the minimum, with vanishing energy at the fixed point, is relevant to the framework's finding that spectral action produces no minimum (V_spec monotone, Session 24a).
