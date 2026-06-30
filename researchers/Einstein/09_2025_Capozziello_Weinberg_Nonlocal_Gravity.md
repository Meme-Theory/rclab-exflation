# The Weinberg No-Go Theorem for Cosmological Constant and Nonlocal Gravity

**Author(s):** Salvatore Capozziello, Anupam Mazumdar, Giuseppe Meluccio
**Year:** 2025
**Journal:** Physical Review Letters (letter format)
**arXiv:** 2502.07321
**Relevance:** HIGH

---

## Abstract

We show how a nonlocal gravitational interaction can circumvent the Weinberg no-go theorem on cosmological constant, which forbids the existence of any solution to the cosmological constant problem within the context of local field theories unless some fine-tuning is assumed. In particular, Infinite Derivative Gravity theories hint at a possible understanding of the cosmological constant as a nonlocal gravitational effect on very large scales. In this perspective, one can describe the observed cosmic acceleration in terms of an effective field theory without relying on the fine-tuning of parameters or additional matter fields.

---

## Key Arguments and Derivations

### The Weinberg No-Go Theorem

The paper begins by restating the Weinberg no-go theorem precisely. Starting from the Einstein field equations G_{mu nu} + Lambda_eff g_{mu nu} = 8 pi G T_{mu nu}, one seeks translationally invariant (constant-field) solutions. For N matter fields psi_i and 6 independent metric components, there are N+6 equations for N+6 unknowns. However, diffeomorphism invariance forces the Lagrangian to take the form L = C sqrt(-g) when matter field equations are satisfied, where C is a constant. The field equations for g_{mu nu} then have no solution unless C = 0 by fine-tuning.

### The Locality Assumption

The key to the theorem lies in the symmetry transformations delta g_{mu nu} = 2 epsilon g_{mu nu}, delta phi = -epsilon, which require the existence of a transverse hypersurface S in field space perpendicular to the scalar field phi direction. This foliation ensures that phi can be varied independently of the remaining N-1 fields sigma_j, leading to the conclusion that the Lagrangian depends on g_{mu nu} and phi only through the combination e^{2 phi} g_{mu nu}. The theorem then follows: no stationary field value phi_0 exists unless L_0(sigma_j) is fine-tuned to vanish.

### The Nonlocal Solution via IDG

Infinite Derivative Gravity (IDG) theories contain the series R sum_{n=1}^{infinity} f_{1-n} Box^{-n} R, where Box^{-1} is the inverse d'Alembertian operator. The geometric quantities Box^{-n} R are recast as N -> infinity scalar fields phi_n = Box^{-n} R. These auxiliary fields are related by the recurrence relation phi_n = Box^{-1} phi_{n-1}, making them mutually dependent. Critically, because all N -> infinity fields are coupled through this recurrence, none can be varied independently. The transformations (8) that underpin the Weinberg proof cannot be written, and the geometric construction of the transverse hypersurface S fails. Weinberg himself pointed out this loophole in his original work.

### Physical Interpretation

Nonlocal geometric terms automatically vanish for flat Minkowski spacetime (since R = 0), solving the symmetry-breaking issue. Furthermore, evidence shows that such nonlocal terms can reproduce the observed cosmic acceleration on very large (infrared) scales without a cosmological constant. The IDG theories are ghost-free (under specific conditions on the propagator) and unitary.

## Key Results

1. The Weinberg no-go theorem relies crucially on the assumption of locality in field theory.
2. Infinite Derivative Gravity (IDG) theories evade the theorem because their auxiliary scalar fields phi_n = Box^{-n} R are coupled through the recurrence relation phi_n = Box^{-1} phi_{n-1} and cannot be varied independently.
3. The geometric construction (transverse hypersurface S in field space) underlying the Weinberg proof fails for nonlocal theories.
4. Nonlocal gravitational terms can reproduce observed cosmic acceleration in the infrared without fine-tuning Lambda or introducing new matter fields.
5. Maximally symmetric solutions R_{mu nu} = Lambda g_{mu nu} are exact solutions of certain nonlocal models, providing direct proof of Weinberg theorem violation.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Einstein field equations | $G_{\mu\nu} + \Lambda_{\rm eff} g_{\mu\nu} = 8\pi G T_{\mu\nu}$ | Eq. 1 |
| Constant-field Lagrangian | $L = C\sqrt{-g}$ | Eq. 4 |
| Symmetry transformations | $\delta g_{\mu\nu} = 2\epsilon g_{\mu\nu},\quad \delta\sigma_j = 0,\quad \delta\phi = -\epsilon$ | Eq. 8 |
| Weinberg constraint | $L = e^{4\phi}\sqrt{-g}\,L_0(\sigma_j)$ | Eq. 9 |
| Nonlocal IDG series | $R\sum_{n=1}^{\infty} f_{1-n}\Box^{-n} R$ | Eq. 12 |
| Auxiliary field recast | $\Box^{-n}R \equiv \phi_n$ | Eq. 13 |
| Recurrence relation | $\phi_n = \Box^{-1}\phi_{n-1}$ | Eq. 14 |
| Trace equation | $g^{\mu\nu}\frac{\partial L}{\partial g^{\mu\nu}} = 8\pi G T$ | Eq. 5 |
| Linear combination (local) | $g^{\mu\nu}\frac{\partial L}{\partial g^{\mu\nu}} = \sum_{i=1}^N f_i(\psi_i)\frac{\partial L}{\partial\psi_i}$ | Eq. 6 |

## Relevance to Phonon-Exflation

This paper provides critical theoretical context for the phonon-exflation framework's approach to the cosmological constant. The framework's spectral action is inherently nonlocal (built from the Dirac spectrum of a noncommutative geometry), which means it may naturally circumvent the Weinberg no-go theorem by the same mechanism identified here. Specifically, the spectral action functional Tr(f(D_K^2/Lambda^2)) involves the full spectrum of the Dirac operator -- an intrinsically nonlocal object -- rather than a local Lagrangian density. The IDG recurrence relation phi_n = Box^{-1} phi_{n-1} mirrors the spectral action's dependence on arbitrarily high powers of the curvature through the heat kernel expansion. This paper strengthens the theoretical motivation for why the framework's CC prediction w = -1 + O(10^{-29}) can avoid fine-tuning: the spectral action is not a local field theory in the Weinberg sense.
