# Non-commutative Differential Geometry

**Author:** Alain Connes
**Year:** 1985
**Journal:** Publications Mathematiques de l'IHES, 62, 41-144
**Pages:** 104

---

## 1. Overview

This is the comprehensive foundation paper for cyclic cohomology and its
applications to noncommutative geometry. Where the 1980 Comptes Rendus note
sketched the program in 6 pages, this IHES paper develops the full theory in
104 pages of detailed mathematics. It establishes cyclic cohomology as the
correct noncommutative analog of de Rham cohomology, constructs the Chern
character from K-theory to cyclic cohomology, proves the index pairing, and
develops the noncommutative integral via the Dixmier trace.

The paper is organized in three parts:
- **Part I**: Cyclic cohomology -- definition, long exact sequence, computation
- **Part II**: The Chern character in K-theory and its pairing with cyclic cohomology
- **Part III**: Applications -- foliations, transverse fundamental class, index theorems


---

## 2. Cyclic Cohomology: Definitions and Structure

### 2.1 The Hochschild Complex

For an algebra A over C, the Hochschild cochain complex is:

```
C^n(A) = Hom(A^{tensor (n+1)}, C)
```

with coboundary operator b: C^n -> C^{n+1}:

```
(b*phi)(a_0, a_1, ..., a_{n+1}) =
    sum_{j=0}^{n} (-1)^j phi(a_0, ..., a_j * a_{j+1}, ..., a_{n+1})
    + (-1)^{n+1} phi(a_{n+1} * a_0, a_1, ..., a_n)
```

The Hochschild cohomology HH^n(A) = ker(b) / im(b) is the noncommutative analog
of the algebra of differential forms.

### 2.2 The Cyclic Condition

A cochain phi in C^n(A) is CYCLIC if:

```
phi(a_n, a_0, a_1, ..., a_{n-1}) = (-1)^n phi(a_0, a_1, ..., a_n)
```

**Theorem (Connes):** b maps cyclic cochains to cyclic cochains. This means
(C^*_lambda(A), b) is a subcomplex, and its cohomology is CYCLIC COHOMOLOGY:

```
HC^n(A) = H^n(C^*_lambda(A), b)
```

### 2.3 The Operator B and the Long Exact Sequence

Connes introduces a second operator B: C^n -> C^{n-1} defined by B = A * s * N
where N is the cyclic averaging operator, s is the extra degeneracy, and A is a
normalization. The operators b and B satisfy:

```
b^2 = 0,  B^2 = 0,  bB + Bb = 0
```

This gives the (b, B)-bicomplex and the LONG EXACT SEQUENCE:

```
... -> HH^n(A) --I--> HC^n(A) --S--> HC^{n-2}(A) --B--> HH^{n+1}(A) -> ...
```

where I is natural inclusion, S is the periodicity operator, and B is the
connecting homomorphism. The periodicity operator S is crucial: it gives cyclic
cohomology a Z/2-periodicity after stabilization.

### 2.4 Periodic Cyclic Cohomology

Taking the direct limit under S defines PERIODIC cyclic cohomology:

```
HP^0(A) = lim_{->} HC^{2k}(A)    (even)
HP^1(A) = lim_{->} HC^{2k+1}(A)  (odd)
```

For commutative A = C^inf(M) with M a compact manifold:

```
HP^0(C^inf(M)) = H^{even}_dR(M) = H^0(M) + H^2(M) + H^4(M) + ...
HP^1(C^inf(M)) = H^{odd}_dR(M)  = H^1(M) + H^3(M) + H^5(M) + ...
```

This is the DEFINITIVE result: periodic cyclic cohomology IS de Rham cohomology
for smooth manifolds, and extends it to noncommutative algebras.


---

## 3. The Chern-Connes Character and the Index Pairing

### 3.1 From K-Theory to Cyclic Cohomology

Connes defines the Chern character map ch: K_0(A) -> HP^0(A). For a projection
e in M_k(A), the n-th component is:

```
ch_n(e) = (-1)^n * (2n)! / n! * Tr(e tensor e tensor ... tensor e)   [2n+1 copies]
```

### 3.2 The Index Pairing

**Theorem (Connes):** For a cyclic n-cocycle [phi] in HC^n(A) and a K-theory
class [e] in K_0(A):

```
<[phi], [e]> = phi_#(e, e, ..., e)   (for n even)
```

This pairing is well-defined on cohomology/K-theory classes, takes INTEGER
values, equals the Fredholm index of a naturally associated operator, and
generalizes the Atiyah-Singer index theorem.

### 3.3 The Odd Case

For K_1(A) (unitaries u in GL_k(A)):

```
ch_n(u) = (-1)^n * n! * Tr(u^{-1} tensor u tensor u^{-1} tensor u tensor ... )
```

The pairing with odd cyclic cocycles gives the spectral flow.


---

## 4. The Dixmier Trace and the Noncommutative Integral

### 4.1 The Dixmier Trace

For a compact operator T >= 0 with eigenvalues mu_0(T) >= mu_1(T) >= ..., the
DIXMIER TRACE is:

```
Tr_omega(T) = lim_omega (1/log N) * sum_{j=0}^{N-1} mu_j(T)
```

where lim_omega is a generalized limit extracting the LOGARITHMIC DIVERGENCE.
Key properties: Tr_omega(T) = 0 if T is trace-class; Tr_omega(T) is finite and
nonzero precisely for operators in the Dixmier ideal L^{1,inf}; for an
n-dimensional spectral triple, |D|^{-n} is in L^{1,inf}.

### 4.2 The Noncommutative Integral Formula

**Theorem (Connes):** For an n-dimensional spectral triple (A, H, D) and a in A:

```
integral(a) = (1 / c_n) * Tr_omega(a * |D|^{-n})
```

When A = C^inf(M) and D is the Dirac operator on a spin manifold, this recovers
the Riemannian integral. The formula extends to noncommutative algebras.

### 4.3 Connection to the Heat Kernel

The Dixmier trace is related to the heat kernel expansion:

```
Tr(a * e^{-t*D^2}) ~ sum_{k>=0} a_k(a, D^2) * t^{(k-n)/2}   as t -> 0+
```

The Seeley-DeWitt coefficients a_k encode geometric information:
- a_0: volume (cosmological constant)
- a_2: scalar curvature (Einstein-Hilbert action)
- a_4: curvature-squared terms (Yang-Mills + Higgs potential)


---

## 5. The Universal Differential Algebra and Gauge Fields

### 5.1 Definition

For an algebra A, the universal differential graded algebra is:

```
Omega^n(A) = A tensor A_bar^{tensor n}
```

where A_bar = A / C*1. The differential d and the product follow from the
Leibniz rule.

### 5.2 Junk Forms and the Reduced Algebra

Omega*(A) contains "junk" -- forms that are zero in de Rham theory but nonzero
in the universal algebra. Connes defines the REDUCED differential algebra:

```
Omega_D^n(A) = pi(Omega^n(A)) / (pi(Omega^n(A)) intersect ker(pi|_{Omega^{n+1}}))
```

This quotient eliminates junk forms and gives the physically relevant calculus.

### 5.3 Connections and Gauge Fields

A connection on a finitely generated projective module E over A is a linear map
nabla: E -> E tensor_A Omega^1_D(A) satisfying the Leibniz rule. The curvature
F = nabla^2 and the Yang-Mills action is:

```
YM(nabla) = <F, F> = Tr_omega(F * F * |D|^{-n+4})
```

This recovers the classical Yang-Mills action for commutative algebras.


---

## 6. Computations for Key Examples

### 6.1 Commutative Case: C^inf(M)

For A = C^inf(M), M a compact spin manifold: HC^n(A) = de Rham cohomology, the
Chern character is classical, the index pairing gives Atiyah-Singer, the Dixmier
trace integral = Riemannian integral, connections = gauge connections on vector
bundles. All of NCG REDUCES to classical differential geometry.

### 6.2 The Noncommutative Torus A_theta

- HH^0(A_theta) = C (one trace), HH^2(A_theta) = C (one 2-cocycle, the "area form")
- HP^0(A_theta) = C^2 (the trace and the "volume")
- ch([e]) = (rank, theta * first Chern number)

### 6.3 Group Algebras and Fredholm Modules

For A = C*_r(Gamma): cyclic cohomology detects conjugacy classes, the trace gives
HC^0, higher cocycles come from group cohomology H*(Gamma, C). Fredholm modules
over A define cyclic cocycles via:

```
phi_n(a_0, ..., a_n) = Tr(gamma * a_0 * [F, a_1] * ... * [F, a_n])
```

Connes and Moscovici later (1995) proved the LOCAL index formula expressing the
index as a sum of local terms -- a noncommutative Atiyah-Singer theorem. This
local formula is what makes the spectral action computable.


---

## 7. Connection to the Phonon-Exflation Framework

### 7.1 Cyclic Cohomology and the Spectral Action

The spectral action Tr f(D^2/Lambda^2) is computed via the heat kernel
expansion. The Seeley-DeWitt coefficients a_k are CYCLIC COCYCLES evaluated on
specific elements. Session 14 computed these for the Jensen-deformed Dirac
operator D_s on SU(3):

- a_0(s): volume term -- constant by TT deformation
- a_2(s): scalar curvature term (Einstein-Hilbert)
- a_4(s): Yang-Mills + Higgs potential

The s-dependence of a_2 and a_4 determines V_eff(s), whose minimum selects the
physical deformation parameter.

### 7.2 K-Theory and Topological Protection

The KO-dimension 6 result (Session 8) is a K-THEORETIC invariant classifying the
spectral triple in the periodic table of topological insulators/superconductors.
KO-dim = 6 corresponds to class BDI (T^2 = +1, Session 17c) -- the SM fermion
content is TOPOLOGICALLY PROTECTED.

In cyclic cohomology terms, KO-dim = 6 means (epsilon, epsilon', epsilon'') =
(+1, +1, -1): J^2 = +1, JD = +DJ, J*gamma = -gamma*J.

### 7.3 Anomaly Cancellation and Phonon Free Energy

The gauge anomaly cancellation in the SM is equivalent to the vanishing of a
cyclic cocycle phi(A, A, A, A, A) = 0. In NCG, this is AUTOMATIC -- the anomaly
cancellation follows from the algebraic structure, not an additional constraint.

The Seeley-DeWitt expansion of Tr(e^{-t*D^2}) is literally a partition function
expansion. The spectral action IS a free energy. This identification (all four
Giants concurred in Session G3) is grounded in the mathematical identity between
the Dixmier trace integral and heat kernel coefficients developed in this paper.


---

## 8. Mathematical Significance

This paper:

1. Established cyclic cohomology as a fundamental cohomology theory
2. Proved the long exact sequence relating Hochschild and cyclic cohomology
3. Constructed the Chern character in K-theory for noncommutative algebras
4. Proved the noncommutative index theorem
5. Introduced the Dixmier trace as a noncommutative integral
6. Developed the universal differential algebra framework
7. Computed examples: foliations, group algebras, irrational rotation algebras

It is one of the most cited papers in operator algebra theory and remains the
definitive reference for the algebraic foundations of noncommutative geometry.


---

## References

1. Connes, A. (1985). "Non-commutative differential geometry." Publ. Math. IHES, 62, 41-144.
2. Connes, A. (1980). "C*-algebres et geometrie differentielle." C. R. Acad. Sci. Paris, 290, A599-A604.
3. Hochschild, G. (1945). "On the cohomology groups of an associative algebra." Ann. Math., 46, 58-67.
4. Dixmier, J. (1966). "Existence de traces non normales." C. R. Acad. Sci. Paris, 262, A1107-A1108.
5. Connes, A. and Moscovici, H. (1995). "The local index formula in noncommutative geometry." GAFA, 5, 174-243.
6. Loday, J.-L. and Quillen, D. (1984). "Cyclic homology and the Lie algebra homology of matrices." Comment. Math. Helv., 59, 569-591.
7. Tsygan, B. (1983). "Homology of matrix Lie algebras over rings and the Hochschild homology." Uspekhi Mat. Nauk, 38, 217-218.
