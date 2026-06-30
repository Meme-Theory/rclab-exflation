# Twistor methods for AdS5

**Author(s):** Tim Adamo, David Skinner, Jack Williams
**Year:** 2016
**Journal:** arXiv preprint (DAMTP-2016-49)
**arXiv:** 1607.03763
**Relevance:** LOW

---

## Abstract

We consider the application of twistor theory to five-dimensional anti-de Sitter space. The twistor space of AdS5 is the same as the ambitwistor space of the four-dimensional conformal boundary; the geometry of this correspondence is reviewed for both the bulk and boundary. A Penrose transform allows us to describe free bulk fields, with or without mass, in terms of data on twistor space. Explicit representatives for the bulk-to-boundary propagators of scalars and spinors are constructed, along with twistor action functionals for the free theories. Evaluating these twistor actions on bulk-to-boundary propagators is shown to produce the correct two-point functions.

---

## Key Arguments and Derivations

Section 2 reviews AdS5 from a projective point of view. Points of complexified AdS5 correspond to antisymmetric 4×4 matrices X^{AB} = X^{[AB]} in CP^5 \ M, where M = {X ∈ CP^5 | X^2 = 0} is the 4D conformal boundary and X^2 = ε_ABCD X^{AB} X^{CD}. The AdS5 metric is
ds^2 = -dX^2/X^2 + (X·dX/X^2)^2 = -ε_ABCD d(X^{AB}/|X|) d(X^{CD}/|X|)
and reduces on the hyperboloid X^2 = 1 in C^6 to flat C^6. Boundary points X_bdry^{AB} have det = 0, so they can be written as skew X^{AB} = C^{[A} D^{B]}, which after gauge fixing gives the form diag-block (x^2/2 ε_{α'β'}, x^α'_β; -x_α^β', ε_αβ). Poincare coordinates correspond to X^{AB} = P^{AB} + (r^2/2) I^{AB} with I^{AB} = block(ε_α'β', 0) the infinity twistor. Reality conditions selecting Euclidean AdS5 come from a quaternionic conjugation Ẑ^A = (-μ̄^1', μ̄^0', -λ̄_1, λ̄_0) with squares to -1; Lorentzian AdS5 from ordinary complex conjugation swapping spinor representations.

Section 2.2 shows the twistor space of AdS5 is the same as the ambitwistor space Q = {(Z^A, W_B) ∈ CP^3 × (CP^3)* | Z·W = 0} of the 4D conformal boundary S^4. The bulk-twistor incidence relations are Z^A = X^{AB} W_B; for fixed X ∈ CP^5 \ M, this defines a CP^3_X ⊂ Q. Two bulk points X, Y in the same CP^3 correspond to geodetically separated points: the intersection CP^3_X ∩ CP^3_Y consists of two disjoint CP^1s unless (X·Y)/(|X||Y|) = 1, in which case they degenerate into one CP^1; the geodesic distance is cosh d(X,Y) = X·Y/(|X||Y|). Boundary points correspond to canonical CP^1_X × (CP^1_X)* ⊂ Q. A point (Z, W) ∈ Q corresponds to a totally null 3-plane X^{AB} = Z^{[A} B^{B]}/(W·B) + ε^{ABCD} A_C W_D in bulk AdS5.

Section 3 builds the Penrose transform for AdS5. For a bulk massive scalar Φ with □_AdS Φ = m^2 Φ and m^2 = Δ(Δ - 4), the direct Penrose transform is
Φ(X) = |X|^Δ ∫_{CP^3_X} D^3 W ∧ f|_X
where f ∈ H^{0,3}(Q, O(-Δ, Δ-4)) and D^3 W = ε^{ABCD} W_A dW_B ∧ dW_C ∧ dW_D. The space-time equation of motion holds iff ∂̄f = 0. Indirect Penrose transform: Φ can equivalently be represented by g ∈ H^{0,2}(Q, O(1-Δ, Δ-3)) via Φ(X) = |X|^Δ lim_{δW→0} ∫_{CP^3_X} D^3 W ∧ (∂̄g/(Z·W))|_{Z^A = X^{AB}(W_B + δW_B)} where ∂̄g = (Z·W) f off the quadric. Dual versions use the inverted incidence relations W_B = X_BC Z^C / X^2.

For bulk chiral massive spinors Ψ_A with D̸ Ψ_B = (Δ-2)(X^{AB}/|X|) Ψ_A and |m| = Δ - 2, the direct Penrose transform is
Ψ_A(X) = |X|^{Δ+1/2} ∫_{CP^3_X} D^3 W ∧ W_A ψ|_X
with ψ ∈ H^{0,3}(Q, O(-Δ-1/2, Δ-9/2)). Indirect via χ ∈ H^{0,2}(Q, O(3/2-Δ, Δ-5/2)) and ∂̄χ = (Z·W)^2 ψ.

Section 4 writes twistor action functionals for the free theories. Since the naive first-order action S[f,h] = ∫ D^3 Z ∧ D^3 W ∧ δ̄(Z·W) ∧ h ∧ ∂̄f vanishes on-shell, the authors introduce indirect representatives and sources:
S[g, g̃] = ∫ D^3 Z ∧ D^3 W ∧ [δ̄'(Z·W) ∧ g̃ ∧ ∂̄g - δ̄(Z·W) ∧ f ∧ g̃ + δ̄(Z·W) ∧ f̃ ∧ g]
whose on-shell value is non-zero and whose equations of motion give ∂̄g = (Z·W) f, ∂̄g̃ = (Z·W) f̃.

For bulk-to-boundary propagators K_Δ = c_Δ (r/(r^2 + (x-y)^2))^Δ, the direct representative is
f_Δ(Z, W) = [AB]^Δ δ̄^3_{Δ-4}(W, A) / (Z·B)^Δ
where [AB] = I^{CD} A_C B_D, A_A, B_A are fixed twistors, and δ̄^3_{Δ-4}(W, A) is a distributional (0,3)-form. Inserting into the Penrose transform gives |X|^Δ (I·Y)^Δ / (X·Y)^Δ with Y_{AB} = A_{[A} B_{B]} a boundary point, matching the standard propagator formula. Indirect version:
g_Δ(Z, W) = [AB]^Δ ∫ s^{Δ-1} ds (δ̄^3_{Δ-3}(W, A(s))/(Z·A)^{Δ-1}) with A(s) = A + sB.

The 2-point function is computed from ∫ D^3 Z D^3 W δ̄'(Z·W) g̃_Δ ∧ ∂̄g_Δ' for two different boundary points y_1, y_2. After performing the D^3 Z, D^3 W integrals via distributional properties and evaluating the s, t integrals algebraically, the result is (I·Y_1)^Δ (I·Y_2)^Δ / (Y_1·Y_2)^Δ = δ_{ΔΔ'}/(y_1 - y_2)^{2Δ}, which is precisely the 4D CFT two-point function ⟨O_Δ(y_1) O_Δ(y_2)⟩.

For spinors, the analogous construction uses
ψ_Δ^β̇(Z, W) = [AB]^{Δ-1/2} I^{BC} B_C δ̄^3_{Δ-9/2}(W, A)/(Z·B)^{Δ+1/2} + (A ↔ B)
giving the space-time propagator r^{Δ+1/2}/(r^2 + (x-y)^2)^{Δ+1/2} times a gamma-matrix structure.

## Key Results

1. The twistor space of AdS5 is Q = {(Z^A, W_B) ∈ CP^3 × (CP^3)* | Z·W = 0}, which coincides with the ambitwistor space of the 4D conformal boundary S^4.
2. Bulk AdS5 points X ∈ CP^5 \ M correspond to CP^3_X ⊂ Q via Z^A = X^{AB} W_B, while boundary points correspond to canonical CP^1 × (CP^1)* ⊂ Q.
3. Null separation in AdS5 corresponds to intersection of two CP^3s in twistor space in a single CP^1, and the AdS geodesic distance satisfies cosh d(X,Y) = X·Y/(|X||Y|).
4. Massive scalars and spinors on AdS5 with mass relations m^2 = Δ(Δ-4) and |m| = Δ - 2 respectively are described by direct and indirect Penrose transforms giving cohomology classes in H^{0,3} and H^{0,2} of Q with appropriate weights.
5. Explicit distributional twistor representatives for scalar and spinor bulk-to-boundary propagators K_Δ are constructed, giving direct integrals that reproduce the standard Poincare-coordinate formula K_Δ = c_Δ (r/(r^2 + (x-y)^2))^Δ.
6. First-order twistor action functionals whose extrema reproduce the free AdS5 field equations and whose on-shell values (evaluated on two bulk-to-boundary propagators for boundary points y_1, y_2) yield the correct 4D CFT two-point function 1/(y_1 - y_2)^{2Δ}.
7. The scalar bulk-to-boundary generating functional can be written in the boundary twistor space for CFT chiral primaries using the N=4 SYM twistor action.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Projective AdS5 metric | ds^2 = -dX^2/X^2 + (X·dX/X^2)^2 | (2.1) |
| Rescaled AdS5 metric | ds^2 = -ε_ABCD dX^{AB} dX^{CD} (X^{AB} = X^{AB}/|X|, X^2 = 1) | (2.2) |
| Boundary point structure | X_bdry^{AB} = diag-block(x^2/2 ε_{α'β'}, x^α'_β; -x_α^β', ε_αβ) | (2.5) |
| Infinity twistor | I^{AB} = block(ε_α'β', 0) | (2.6) |
| Poincare parametrization | X^{AB} = P^{AB} + (r^2/2) I^{AB} | (2.8) |
| Ambitwistor space of S^4 | Q = {(Z^A, W_B) ∈ CP^3 × (CP^3)* | Z·W = 0} | (2.9) |
| Bulk incidence relations | Z^A = X^{AB} W_B | (2.10) |
| Geodesic distance | cosh d(X,Y) = X·Y/(|X||Y|) | (2.13) |
| Scalar direct Penrose transform | Φ(X) = |X|^Δ ∫_{CP^3_X} D^3 W ∧ f|_X | (3.4) |
| Scalar mass relation | m^2 = Δ(Δ - 4) | (3.2) |
| Spinor mass relation | |m| = Δ - 2 | (3.3) |
| Spinor direct Penrose transform | Ψ_A(X) = |X|^{Δ+1/2} ∫_{CP^3_X} D^3 W ∧ W_A ψ|_X | (3.14) |
| Scalar twistor action | S[g, g̃] = ∫ D^3 Z ∧ D^3 W [δ̄'(Z·W) g̃ ∧ ∂̄g - δ̄(Z·W) f ∧ g̃ + δ̄(Z·W) f̃ ∧ g] | (4.2) |
| Scalar bulk-to-boundary propagator | K_Δ(r, x; y) = c_Δ (r/(r^2 + (x-y)^2))^Δ | (4.5) |
| Direct twistor rep for K_Δ | f_Δ(Z, W) = [AB]^Δ δ̄^3_{Δ-4}(W, A)/(Z·B)^Δ | (4.6) |
| Indirect twistor rep for K_Δ | g_Δ(Z, W) = [AB]^Δ ∫ s^{Δ-1} ds δ̄^3_{Δ-3}(W, A(s))/(Z·A)^{Δ-1} | (4.8) |
| Scalar 2-point function | ∫ D^3 Z D^3 W δ̄'(Z·W) g̃_Δ ∧ ∂̄g_{Δ'} = δ_{ΔΔ'}/(y_1 - y_2)^{2Δ} | (4.12) |

## Relevance to Phonon-Exflation

The framework operates in D=10 (M4 × SU(3)) rather than AdS5, but there are two potential connections. First, the twistor space of AdS5 being identical to the ambitwistor space of the 4D boundary offers a template: the phonon-exflation framework's emergent 4D observable physics (from KK reduction of M4 × SU(3)) could in principle be encoded in an ambitwistor space of the 4D effective geometry, with the 6D fiber SU(3) supplying extra bulk dimensions in a way analogous to how AdS5 supplies one extra bulk dimension to the 4D CFT boundary. Second, the explicit bulk-to-boundary propagator construction and the demonstration that the twistor action reproduces the 2-point function exactly could be useful if the framework ever needs to compute correlation functions of boundary-defined observables (e.g., Wightman functions on the CMB-last-scattering surface seen as a boundary of the post-fold region). The mass-dimension relation m^2 = Δ(Δ-4) would need to be translated into the spectral-moment language where m^2 and Δ correspond to eigenvalue windows of D_K. Direct utility for the current EVOI priority list is limited.
