# The Eta-Invariant, Maslov Index, and Spectral Flow for Dirac-Type Operators on Manifolds with Boundary

**Author(s):** Paul Kirk, Matthias Lesch
**Year:** 2000 (revised 2002)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** math/0012123
**Relevance:** HIGH

---

## Abstract

Several proofs have been published of the mod Z gluing formula for the eta-invariant of a Dirac operator. However, so far the integer contribution to the gluing formula for the eta-invariant is left obscure in the literature. In this article we present a gluing formula for the eta-invariant which expresses the integer contribution as a triple index involving the boundary conditions and the Calderon projectors of the two parts of the decomposition. The main ingredients of our presentation are the Scott-Wojciechowski theorem for the determinant of a Dirac operator on a manifold with boundary and the approach of Bruning-Lesch to the mod Z gluing formula. Our presentation includes careful constructions of the Maslov index and triple index in a symplectic Hilbert space. As a byproduct we give intuitively appealing proofs of two theorems of Nicolaescu on the spectral flow of Dirac operators. As an application we carry out a detailed analysis of the eta-invariant of the odd signature operator coupled to a flat connection using adiabatic methods, extending the definition of the Atiyah-Patodi-Singer rho-invariant to manifolds with boundary.

---

## Key Arguments and Derivations

### 1. Dirac Operators on Manifolds with Boundary

Let X be a compact Riemannian manifold with boundary dX. Near the boundary, a Dirac operator takes the product form D = gamma(d/dx + A), where A is a self-adjoint first-order elliptic operator on dX (the tangential operator) satisfying gamma^2 = -I, gamma* = -gamma, gamma A = -A gamma.

Boundary conditions are specified by projections P in the self-adjoint Fredholm Grassmannian Gr(A), consisting of orthogonal projections P such that: P is pseudodifferential of order 0, gamma P gamma* = I - P, and (P_{>0}, P) form a Fredholm pair. The operator D_P has discrete spectrum with finite multiplicities.

### 2. The Calderon Projector

The Calderon projector P_X is the orthogonal projection onto the Cauchy data space L_X = r(ker D: H^{1/2}(E) -> H^{-1/2}(E)) in L^2(E|_{dX}). It is an element of Gr(A) determined by D and is the canonical boundary condition.

### 3. Main Gluing Formula (Theorem 5.9 / 7.4)

For a Dirac operator D on a closed manifold M split into M_+ and M_- by a hypersurface N, with reduced eta-invariant tilde{eta}(D) = (eta(D) + dim ker D)/2:

tilde{eta}(D, M) = tilde{eta}(D_P, M_+) + tilde{eta}(D_{I-P}, M_-) + SF(D_{P_t}, M_+) + SF(D_{I-P_t}, M_-)

= tilde{eta}(D_P, M_+) + tilde{eta}(D_{I-P}, M_-) - tau_mu(I - P_{M_-}, P, P_{M_+})

where SF denotes spectral flow and tau_mu is the Maslov triple index. Taking P = P_{M_+} (the Calderon projector for M_+) yields:

tilde{eta}(D, M) = tilde{eta}(D_{P_{M_+}}, M_+) + tilde{eta}(D_{I-P_{M_+}}, M_-)

### 4. Maslov Index and Spectral Flow

The paper constructs the Maslov index and triple index tau_mu(L_1, L_2, L_3) for triples of projections in symplectic Hilbert spaces, carefully handling degenerate cases. The key relation to spectral flow is: spectral flow of a path of Dirac operators equals a Maslov index of the corresponding path of Calderon projectors.

### 5. Adiabatic Stretching and the Rho-Invariant

For the odd signature operator coupled to a flat connection with holonomy alpha, adiabatic stretching of the collar neighborhood identifies the limiting Calderon projectors (Theorem 8.5). This yields:

eta(D, M) = eta(D_{P^+(V_{+,alpha})}, M_+) + eta(D_{P^-(V_{-,alpha})}, M_-) + m(V_{+,alpha}, V_{-,alpha}, alpha, g)

where V_{+/-,alpha} are images of twisted cohomology in boundary cohomology, and m is a symplectic invariant.

### 6. Extension of APS Rho-Invariant to Manifolds with Boundary

Definition 8.17 extends the rho-invariant to manifolds with boundary. The non-additivity formula (Theorem 8.18) relates:

rho(M, alpha) = rho(M_+, alpha, g) + rho(M_-, alpha, g) + m(V_{+,alpha}, V_{-,alpha}, alpha, g) - m(V_{+,tau}, V_{-,tau}, tau, g)

connecting to Wall's non-additivity theorem for signatures.

---

## Key Results

1. **Main Gluing Formula**: Complete formula for the eta-invariant under cutting/pasting, including the integer contribution via Maslov triple index.

2. **Spectral flow = Maslov index**: Nicolaescu's theorems reproved with conceptually simpler methods.

3. **Adiabatic limit of Calderon projectors** (Theorem 8.5): Explicit identification for the odd signature operator.

4. **Extension of APS rho-invariant** to manifolds with boundary (Definition 8.17).

5. **Non-additivity formula** (Theorem 8.18) for the APS rho-invariant.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Product form | $D = \gamma\left(\frac{d}{dx} + A\right)$ | Sec. 2 |
| Tangential relations | $\gamma^2 = -I,\; \gamma^* = -\gamma,\; \gamma A = -A\gamma$ | Eq. (2.1) |
| Reduced eta | $\tilde{\eta}(D) = (\eta(D) + \dim\ker D)/2$ | Sec. 1 |
| Gluing formula | $\tilde{\eta}(D,M) = \tilde{\eta}(D_P,M_+) + \tilde{\eta}(D_{I-P},M_-) - \tau_\mu(I-P_{M_-}, P, P_{M_+})$ | Thm 5.9 |
| Calderon projector | $L_X := r(\ker D: H^{1/2}(E) \to H^{-1/2}(E))$ | Eq. (2.4) |
| APS projection | $P^+(L) = \mathrm{proj}_L + P_{>0}$ | Eq. (2.3) |
| Odd signature formula | $\eta(D,M) = \eta(D_{P^+(V_{+,\alpha})},M_+) + \eta(D_{P^-(V_{-,\alpha})},M_-) + m(\ldots)$ | Eq. (8.32) |
| Non-additivity | $\rho(M,\alpha) = \rho(M_+,\alpha,g) + \rho(M_-,\alpha,g) + m(\ldots) - m(\ldots)$ | Thm 8.18 |

---

## Relevance to Phonon-Exflation

The eta invariant is central to the project's BDI topological classification of the Dirac operator D_K(tau) on SU(3). The APS boundary conditions and spectral flow analyzed here are directly relevant when the compactification parameter tau creates an effective boundary in the spectral geometry. The gluing formula via Calderon projectors provides the mathematical framework for understanding how the eta invariant (and hence the topological winding number) behaves as the SU(3) fiber geometry changes during the exflation transit. The Maslov index appearing in the gluing formula connects to the project's phase-space analysis of Cooper pair dynamics.
