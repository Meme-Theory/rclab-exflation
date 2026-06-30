# A Short Survey of Cyclic Cohomology

**Author(s):** Masoud Khalkhali
**Year:** 2010
**Journal:** Clay Mathematics Proceedings, Volume 10, 2008
**arXiv:** 1008.1212
**Relevance:** MEDIUM

---

## Abstract

This is a short survey of some aspects of Alain Connes' contributions to cyclic cohomology theory in the course of his work on noncommutative geometry over the past 30 years.

---

## Key Arguments and Derivations

### 1. Origin of Cyclic Cohomology

Cyclic cohomology was discovered by Connes in 1981, motivated by the transverse elliptic theory for foliations. For a compact foliated manifold (V, F), the foliation algebra A = C*(V, F) replaces the singular leaf space V/F. The analytic index of a transversally elliptic operator D lies in K_0(A), and a noncommutative Chern character from K_0(A) to cyclic cohomology was needed to identify this class cohomologically.

### 2. Definition of Cyclic Cohomology

For an algebra A, n-cochains are C^n(A) = Hom(A^{tensor(n+1)}, C). The Hochschild differential b is:

(b phi)(a_0,...,a_{n+1}) = sum_{i=0}^{n} (-1)^i phi(a_0,...,a_i a_{i+1},...,a_{n+1}) + (-1)^{n+1} phi(a_{n+1} a_0,...,a_n)

A cyclic n-cochain satisfies phi(a_n, a_0,...,a_{n-1}) = (-1)^n phi(a_0,...,a_n). The cyclic complex (C*_lambda(A), b) is a subcomplex of the Hochschild complex, and its cohomology is cyclic cohomology HC^n(A).

### 3. Connes' Long Exact Sequence

The inclusion of cyclic into Hochschild complexes yields the fundamental long exact sequence:

... -> HC^n(A) -I-> HH^n(A) -B-> HC^{n-1}(A) -S-> HC^{n+1}(A) -> ...

The operator B = NB_0 is the noncommutative analog of the de Rham differential, and the periodicity operator S is related to Bott periodicity in K-theory. The key relations are bB + Bb = 0 and B^2 = 0.

Periodic cyclic cohomology is the direct limit: HP^i(A) = lim_{->} HC^{2n+i}(A) for i = 0, 1.

### 4. The (b, B)-Bicomplex

The (b, B)-bicomplex B(A) provides a unified framework. Connes' spectral sequence with E_2 term given by the cohomology of I . B on Hochschild groups converges to the periodic cyclic cohomology.

For A = C^infty(V), cyclic cohomology recovers de Rham homology of currents. For the noncommutative torus (Kronecker foliation), the Hochschild cohomology depends on the Diophantine nature of the rotation number while cyclic cohomology gives HP^0 of dimension 2 and HP^1 of dimension 2.

### 5. From K-Homology to Cyclic Cohomology

An odd Fredholm module over A is a pair (H, F) where F is bounded self-adjoint with F^2 = I, and [F, pi(a)] is compact for all a. For p-summable Fredholm modules, Connes defines the Chern character:

Ch_{2n-1}(a_0,...,a_{2n-1}) = (-1)^n 2(n-1/2)...(1/2) Tr(F[F,a_0]...[F,a_{2n-1}])

The periodicity relation S phi_{2n-1} = -(n + 1/2) phi_{2n+1} ensures the character is well-defined in periodic cyclic cohomology.

### 6. Index Pairing

The index pairing between K-theory and K-homology via Fredholm index:

<(H,F), [U]> = index(PUP)

where P = (F+1)/2, gives Connes' noncommutative index formula:

index(PuP) = (-1)^n / 2^{2n} phi_{2n-1}(u^{-1}, u,..., u^{-1}, u)

### 7. Cyclic Modules and Lambda Category

Section 4 describes cyclic objects and Connes' cyclic category Lambda. A cyclic object in a category C is a functor Lambda^{op} -> C. The key result: the classifying space |Lambda| is homotopy equivalent to CP^infty, the classifying space of the circle group.

### 8. Local Index Formula

Section 5 describes the Connes-Moscovici local index formula, which computes the Chern character of a spectral triple (A, H, D) locally via residues. This requires the dimension spectrum to be discrete and simple.

### 9. Hopf Cyclic Cohomology

Section 6 introduces Hopf cyclic cohomology, developed by Connes and Moscovici, for computing the index of transversally elliptic operators. The key object is the Hopf algebra H_n encoding the symmetries of codimension-n foliations.

---

## Key Results

1. **Cyclic cohomology** is the noncommutative analog of de Rham homology, defined via the cyclic subcomplex of the Hochschild complex.

2. **Connes' long exact sequence** relating Hochschild and cyclic cohomology via operators I, B, S.

3. **Connes-Chern character** from K-homology to periodic cyclic cohomology.

4. **Index formula**: Fredholm index = pairing of Chern character with K-theory class.

5. **For C^infty(V)**: cyclic cohomology recovers de Rham homology of currents.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hochschild differential | $(b\varphi)(a_0,\ldots,a_{n+1}) = \sum_{i=0}^{n}(-1)^i\varphi(\ldots,a_i a_{i+1},\ldots) + (-1)^{n+1}\varphi(a_{n+1}a_0,\ldots,a_n)$ | Sec. 2 |
| Cyclic condition | $\varphi(a_n, a_0,\ldots,a_{n-1}) = (-1)^n\varphi(a_0,\ldots,a_n)$ | Def. 2.1 |
| Long exact sequence | $\cdots \to HC^n(A) \xrightarrow{I} HH^n(A) \xrightarrow{B} HC^{n-1}(A) \xrightarrow{S} HC^{n+1}(A) \to \cdots$ | Eq. (8) |
| B operator | $B = NB_0,\; (B_0\varphi)(a_0,\ldots,a_{n-1}) = \varphi(1,a_0,\ldots,a_{n-1}) - (-1)^n\varphi(a_0,\ldots,a_{n-1},1)$ | Sec. 2 |
| bB + Bb = 0 | $bB + Bb = 0,\; B^2 = 0$ | Eq. (9) |
| Periodic cyclic | $HP^i(A) := \lim_{\to} HC^{2n+i}(A),\; i = 0, 1$ | Sec. 2 |
| Chern character | $\mathrm{Ch}_{2n-1}(a_0,\ldots,a_{2n-1}) = (-1)^n 2(n-\frac{1}{2})\cdots\frac{1}{2}\,\mathrm{Tr}(F[F,a_0]\cdots[F,a_{2n-1}])$ | Sec. 3 |
| Fredholm module | $[F,\pi(a)] \in \mathcal{K}(H),\; F^2 = I,\; F = F^*$ | Def. 3.1 |
| Index pairing | $\langle(H,F),[U]\rangle = \mathrm{index}(PUP),\; P = \frac{F+1}{2}$ | Sec. 3 |
| K-theory pairing | $\langle[\varphi],[e]\rangle = (n!)^{-1}\tilde{\varphi}(e,\ldots,e)$ | Eq. (24) |

---

## Relevance to Phonon-Exflation

Cyclic cohomology provides the mathematical framework for the Chern character in K-homology, which is how the project's spectral triple (A, H, D_K(tau)) computes topological invariants. The long exact sequence and the periodicity operator S are relevant to understanding how the BDI classification (winding number) persists across the tau-parameter family. The Connes-Chern character formula is the tool that connects the Dirac spectrum to K-theory classes, and hence to the topological charges carried by the framework's Cooper pairs.
