# Tetrads and q-theory

**Author(s):** F.R. Klinkhamer, G.E. Volovik
**Year:** 2019
**Journal:** JETP Lett. 109, 364-367 (2019)
**arXiv:** 1812.07046
**Relevance:** CRITICAL

---

## Abstract

As the microscopic structure of the deep relativistic quantum vacuum is unknown, a phenomenological approach (q-theory) has been proposed to describe the vacuum degrees of freedom and the dynamics of the vacuum energy after the Big Bang. The original q-theory was based on a four-form field strength from a three-form gauge potential. However, this realization is rather artificial and does not take into account the fermionic nature of the vacuum. We now propose a more physical realization of the q-variable. In this approach, we assume that the vacuum has the properties of a plastic (malleable) fermionic crystalline medium. The new approach unites general relativity and fermionic microscopic (trans-Planckian) degrees of freedom, as the approach involves both the tetrad of standard gravity and the elasticity tetrad of the hypothetical vacuum crystal.

---

## Key Arguments and Derivations

### Gravity Tetrad
Standard tetrad formalism: $g_{\mu\nu} = \eta_{ab} e^a_\mu e^b_\nu$, with spin connection $\omega^a_{\mu b} = e^a_\nu \nabla_\mu e^\nu_b$.

### Elasticity Tetrad
The vacuum is a plastic fermionic crystalline medium. Four deformed crystallographic manifolds of constant phase $X^a(x) = 2\pi n_a$ define the elasticity tetrad:

$$E^a_\mu(x) = D_\mu X^a(x)$$

where $D_\mu X^a = \nabla_\mu X^a + \omega^a_{\mu b} X^b$ includes the spin connection. The elasticity tetrads have dimensions of inverse length/time.

### q-Field from Two Tetrads
The q-variable is constructed from both tetrads:

$$q(x) = \frac{1}{4} e^\mu_a(x) E^a_\mu(x)$$

combining the inverse gravity tetrad $e^\mu_a$ and the elasticity tetrad $E^a_\mu$. The action is:

$$S = \int d^4x \, e \left(\frac{R}{16\pi G_N} + \epsilon(q)\right)$$

### Field Equations
Variation over $e^\mu_a$ gives the Einstein equation with $\rho_V(q) g_{\mu\nu}$:

$$\rho_V(q) = \epsilon(q) - q \frac{d\epsilon}{dq}$$

Variation over $X^a$ gives:

$$\partial_\mu \left(\frac{d\epsilon}{dq}\right) = 0 \implies \frac{d\epsilon}{dq} = \mu = \text{const}$$

The equilibrium conditions are: (1) $\rho_V(q_0) = 0$, (2) $d\rho_V/dq|_{q_0} = 0$, (3) $d^2\rho_V/dq^2|_{q_0} > 0$.

### Dolgov Problem Avoided
The approach avoids the Rubakov-Tinyakov problem (ruined Newtonian gravity) that plagues vector-field realizations. The field equations contain only $g_{\mu\nu}(x)$ and $q(x)$, not the composite vector field $A^\mu$. The linearized Einstein equation around flat Minkowski spacetime with $\rho_V(q_0) = 0$ gives standard Newtonian gravity.

### Topological Phases
The vacuum crystal may have nontrivial topological phases characterized by Chern-Simons-like terms with momentum-space topological invariants as prefactors, mixing gravity and elasticity anomalies.

## Key Results

1. The q-variable is $q = \frac{1}{4} e^\mu_a E^a_\mu$, uniting gravity tetrad and elasticity tetrad
2. The vacuum is a plastic fermionic crystalline medium
3. Field equations are universal: $\rho_V = \epsilon - q\,d\epsilon/dq$ and $d\epsilon/dq = \mu = \text{const}$
4. Equilibrium gives $\rho_V = 0$ (CC nullified) without fine-tuning
5. Newtonian gravity preserved (Dolgov/Rubakov-Tinyakov problem avoided)
6. Dislocations in the vacuum crystal correspond to torsion; disclinations to curvature
7. New quantum anomalies arise from mixing elasticity tetrads with gauge and spin-connection fields

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Elasticity tetrad | $E^a_\mu = D_\mu X^a$ | Eq. (4) |
| q-variable | $q = \frac{1}{4} e^\mu_a E^a_\mu$ | Eq. (6) |
| Action | $S = \int d^4x \, e \left(\frac{R}{16\pi G_N} + \epsilon(q)\right)$ | Eq. (7) |
| Vacuum energy | $\rho_V = \epsilon(q) - q \, d\epsilon/dq$ | Eq. (13) |
| Conservation | $d\epsilon/dq = \mu = \text{const}$ | Eq. (14) |
| Equilibrium | $\rho_V(q_0) = 0$ | Eq. (17a) |
| Equilibrium solution | $D_\mu X^a|_{\text{equil}} = q \, e^a_\mu$ | Eq. (19) |

## Relevance to Phonon-Exflation

This paper is the direct theoretical ancestor of the phonon-exflation framework's approach:
- **Vacuum as fermionic crystal**: The framework's SU(3) fiber IS the vacuum crystal. The elasticity tetrads describe its deformations
- **Two tetrads**: The gravity tetrad $e^a_\mu$ and elasticity tetrad $E^a_\mu$ correspond to the framework's distinction between the $M^4$ geometry and the SU(3) internal geometry
- **q from both tetrads**: $q = \frac{1}{4} e^\mu_a E^a_\mu$ unifies the two geometries — this is the structural core of the framework's claim that particles are phononic excitations of $M^4 \times SU(3)$
- **Dislocations = torsion**: The framework's instanton gas creates defects in the vacuum crystal, carrying torsion
- **Topological phases**: The vacuum crystal's topological phases (characterized by CS terms) connect to the framework's BDI classification and Pfaffian $\mathbb{Z}_2$ invariant
- **CC nullification**: The same thermodynamic mechanism as in papers 13-14, but now with a physical realization tied to the crystalline structure
