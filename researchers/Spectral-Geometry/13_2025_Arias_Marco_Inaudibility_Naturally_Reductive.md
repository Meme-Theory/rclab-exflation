# Inaudibility of Naturally Reductive Property

**Author(s):** Teresa Arias-Marco, Jose-Manuel Fernandez-Barroso
**Year:** 2025
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 2502.10332
**Relevance:** HIGH

---

## Abstract

In this paper, we use a characterization of naturally reductive 2-step nilpotent Lie groups via Ambrose-Singer's homogeneous structures to prove that one cannot determine if a closed Riemannian manifold is naturally reductive using the information encoded in the spectrum of the Laplace-Beltrami operator. To do that, we consider a new isospectral pair of 2-step nilmanifolds of dimension 9 such that one of them is naturally reductive and the other is not.

---

## Key Arguments and Derivations

### 1. 2-Step Nilpotent Lie Groups

The paper works with 2-step nilpotent Lie algebras n = v + z with inner product g and a linear map j: z -> so(v) defining the Lie bracket via g([X^v, Y^v], Z^z) = g(j_{Z^z} X^v, Y^v). The Levi-Civita connection is:

nabla_V X = -(1/2) j_{V^z} X^v - (1/2) j_{X^z} V^v + (1/2) [V^v, X^v]

The Ricci operator is rho(X) = (1/2) J(X^v) + (1/4) B(X^z) where J(X^v) = sum_k j_{z_k} j_{z_k} X^v and B(X^z) = sum_i [v_i, j_{X^z} v_i].

### 2. Type A Characterization

A Riemannian manifold is Type A if its Ricci tensor is cyclic parallel: (nabla_X ric)(X, X) = 0. The paper proves (Theorem 1.2) that a 2-step nilpotent Lie group is Type A if and only if J . j_{X^z} is a skew-symmetric endomorphism for every X^z in z.

### 3. Naturally Reductive Characterization

A Riemannian manifold is naturally reductive if every geodesic is the orbit of a one-parameter subgroup of the isometry group. Using Ambrose-Singer homogeneous structures (Theorem 0.1), this is equivalent to the existence of a (2,1)-tensor T satisfying the Ambrose-Singer equations plus T_X X = 0 for all X.

Theorem 1.7 gives the unique naturally reductive homogeneous structure on 2-step nilpotent Lie groups with J = C*Id_v and B = D*Id_z (D != 2C):

T_X Y = -(1/2) j_{Y^z} X^v + (1/2) j_{X^z} Y^v + (1/2) [X^v, Y^v] + tilde{T}_{X^z} Y^z

where tilde{T} is a Lie bracket on z satisfying j_{X^z} j_{Y^z} Z^v - j_{Y^z} j_{X^z} Z^v = j_{tilde{T}_{X^z} Y^z} Z^v.

### 4. Isospectral Pair Construction

In Section 2, the authors construct a pair of 9-dimensional 2-step nilmanifolds that are isospectral for the Laplace-Beltrami operator. They use the Gordon-Wilson method with specific j-maps j_1 and j_2 on v = R^6, z = R^3. The key is to verify that one manifold satisfies the naturally reductive condition (equation 14) while the other does not, while ensuring isospectrality.

### 5. Main Theorem

Since the isospectral pair consists of one naturally reductive manifold and one non-naturally-reductive manifold, the naturally reductive property cannot be determined from the Laplace spectrum alone -- it is "inaudible."

---

## Key Results

1. **Theorem 1.2**: A 2-step nilpotent Lie group (N(j), g) is Type A if and only if J . j_{X^z} is skew-symmetric for every X^z in z.

2. **Theorem 1.7**: Characterization of the unique naturally reductive structure on 2-step nilpotent Lie groups with J = C*Id_v, B = D*Id_z.

3. **Proposition 0.2**: Every naturally reductive Riemannian manifold is of Type A (short proof via homogeneous structures).

4. **Corollary 1.3**: Every 2-step nilpotent group with J = C*Id_v is Type A.

5. **Main result**: Construction of an isospectral pair of 9-dimensional nilmanifolds proving inaudibility of the naturally reductive property.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Lie bracket | $g([X^v, Y^v]_j, Z^z) = g(j_{Z^z} X^v, Y^v)$ | Eq. (7) |
| Levi-Civita | $\nabla_V X = -\frac{1}{2}j_{V^z}X^v - \frac{1}{2}j_{X^z}V^v + \frac{1}{2}[V^v, X^v]$ | Eq. (8) |
| Ricci operator | $\rho(X) = \frac{1}{2}J(X^v) + \frac{1}{4}B(X^z)$ | Eq. (9) |
| Type A condition | $(\nabla_X \mathrm{ric})(X, X) = 0$ | Eq. (1) |
| Ambrose-Singer | $(\nabla_V R)(X,Y)Z = T_V(R(X,Y)Z) - R(T_V X,Y)Z - \ldots$ | Eq. (2) |
| Nat. reductive | $g(T_X Y, Z) + g(T_Y X, Z) = 0$, equivalently $T_X X = 0$ | Eq. (5) |
| Covariant Ricci | $(\nabla_X \mathrm{ric})(Y,Z) = \frac{1}{4}g(j_{X^z}Y^v, J(Z^v)) + \ldots$ | Eq. (11) |
| Nat. red. structure | $T_X Y = -\frac{1}{2}j_{Y^z}X^v + \frac{1}{2}j_{X^z}Y^v + \frac{1}{2}[X^v, Y^v] + \tilde{T}_{X^z}Y^z$ | Eq. (24) |
| Compatibility | $j_{X^z}j_{Y^z}Z^v - j_{Y^z}j_{X^z}Z^v = j_{\tilde{T}_{X^z}Y^z}Z^v$ | Eq. (14) |

---

## Relevance to Phonon-Exflation

This paper addresses inverse spectral geometry on homogeneous nilmanifolds, demonstrating fundamental limitations of the "Can one hear the shape of a drum?" question for algebraic-geometric properties. For the phonon-exflation framework, where the Dirac spectrum on SU(3) encodes physics, this result is a cautionary example: certain geometric properties (like natural reductivity) are invisible to the Laplace spectrum. However, the Dirac spectrum carries strictly more information than the Laplace spectrum, and the project's reliance on the Dirac operator rather than the Laplacian may avoid some of these spectral ambiguities.
