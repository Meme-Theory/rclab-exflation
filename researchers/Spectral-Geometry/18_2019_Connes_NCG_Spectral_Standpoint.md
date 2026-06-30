# Noncommutative Geometry, the Spectral Standpoint

**Author(s):** Alain Connes
**Year:** 2019
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 1910.10407
**Relevance:** MEDIUM

---

## Abstract

We update our Year 2000 account of Noncommutative Geometry. The basic features described include: the natural "time evolution" making noncommutative spaces dynamical from their measure theory; the new calculus based on operators in Hilbert space, the Dixmier trace and the Wodzicki residue; the spectral geometric paradigm extending the Riemannian paradigm to the noncommutative world as pure gravity on a geometric structure mixing continuum with discrete; and key examples such as duals of discrete groups, leaf spaces of foliations and deformations of ordinary spaces. Highlights since 2000 include: the interplay of geometry with modular theory for noncommutative tori; advances on the Baum-Connes conjecture; geometrization of pseudo-differential calculi using smooth groupoids; Hopf cyclic cohomology; topological cyclic homology in number theory; the renormalization group as a motivic Galois group; quantum field theory on noncommutative spaces; the discovery that irreducible representations of a simple equation correspond to 4-dimensional spin geometries; and the discovery that natural toposes provide algebro-geometric structure on the adele class space for zeros of L-functions.

---

## Key Arguments and Derivations

### 1. Noncommutative Spaces and Their Origins

Noncommutative spaces arise when classical tools fail: their cardinality equals the continuum but no constructive bijection with R exists. Examples include leaf spaces of foliations, spaces of irreducible representations of discrete groups, Penrose tilings, and geodesics on negatively curved surfaces. These are encoded by convolution algebras of equivalence relations, with noncommutativity reflecting point identification.

### 2. Space-Time and NCG: The Standard Model

The key role of non-abelian gauge theories motivates searching for a geometric interpretation of the gauge group Diff(M) x Gauge as diffeomorphisms of a "larger" space. NCG provides this: replacing A = C^infty(M) by M_n(A) enhances automorphisms to include SU(n) gauge transformations. The finite geometry F with KO-dimension 6 was determined by classification of irreducible finite spectral triples:

- Case 1: A_C = M_k(C), center C (unitary/real/symplectic)
- Case 2: A_C = M_k(C) + M_k(C), center C + C (needed for KO-dim 6)

The simplest solution is A_F = M_2(H) + M_4(C), yielding gauge symmetry U(1) x SU(2) x SU(3) after the order-one condition [[D, a], b^0] = 0 reduces SU(2) x SU(2) x SU(4).

### 3. The Spectral Paradigm

A spectral geometry (A, H, D) encodes coordinates (A), metric (D), and measurement (H). The distance formula:

d(a, b) = sup |f(a) - f(b)|, f in A, ||[D, f]|| <= 1

recovers Riemannian geodesic distance in the commutative case but extends to non-arcwise-connected, discrete, and fractal spaces.

The reconstruction theorem (2008, paper 16 in this collection) characterizes commutative spectral triples as spin^c manifolds. The KO-dimension (dimension mod 8) is independent of metric dimension for product spaces M x F.

### 4. Geometry and the Modular Theory

For the noncommutative torus T^2_theta, curved geometry is obtained from a flat spectral triple (A, H, D_0) by a Weyl conformal factor (dilaton). The modular operator Delta of the non-tracial weight plays a crucial role with no classical analogue. The curvature formula involves functions K_0(nabla) and H_0(nabla_1, nabla_2) of the modular operator, satisfying a deep internal consistency relation.

### 5. Inner Fluctuations and the Spectral Action

Inner fluctuations of the metric replace D by D_A = D + A + JAJ^{-1} where A = sum a_j[D, b_j]. The spectral action Tr(f(D/Lambda)) has asymptotic expansion:

Tr(f(D/Lambda)) ~ 2 Lambda^4 f_4 a_0 + 2 Lambda^2 f_2 a_2 + f_0 a_4 + ...

For M x F with F of KO-dimension 6: the inner fluctuations produce the Standard Model gauge fields plus Higgs doublet, and the spectral action plus fermionic bilinear gives the SM Lagrangian minimally coupled to gravity.

### 6. Dimension 4 and Quantized Volume

The simultaneous quantization of the fundamental class in K-homology and K-theory explains the finite algebra A_F = M_2(H) + M_4(C) from a purely geometric problem. A "punctuation symbol" Y with Y^4 = 1 generates the continuum from the noncommutative system.

### 7. Zeta and NCG: Adele Class Space

The zeros of the Riemann zeta function are intimately related to the noncommutative adele class space X = Q*\A_Q. The scaling site provides the missing algebro-geometric structure, and the Riemann-Weil explicit formulas acquire a trace formula interpretation.

---

## Key Results

1. **Reconstruction theorem** (2008): Commutative spectral triples satisfying five axioms characterize smooth compact manifolds.

2. **Standard Model from NCG**: A_F = M_2(H) + M_4(C) with KO-dimension 6 yields gauge group U(1) x SU(2) x SU(3), Higgs mechanism, and see-saw neutrino masses.

3. **Modular curvature**: Functions of the modular operator appear in the curvature of noncommutative tori, with a deep consistency relation.

4. **Quantized volume**: Simple equation whose irreducible representations correspond to 4D spin geometries.

5. **Scaling site**: Natural topos providing algebro-geometric structure for the spectral realization of zeta zeros.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Distance formula | $d(a,b) = \sup\{|f(a)-f(b)|:\; f\in A,\; \|[D,f]\|\leq 1\}$ | Eq. (2) |
| Inner fluctuation | $D_A = D + A + JAJ^{-1},\; A = \sum a_j[D,b_j],\; A = A^*$ | Sec. 2.2 |
| Spectral action | $\mathrm{Tr}(f(D/\Lambda)) \sim 2\Lambda^4 f_4 a_0 + 2\Lambda^2 f_2 a_2 + f_0 a_4 + \ldots$ | Sec. 2.3 |
| Heat expansion | $\mathrm{Tr}(ae^{-tD^2}) \sim_{t\searrow 0} \sum_{n\geq 0} a_n(a,D^2)t^{(-d+n)/2}$ | Sec. 2.1 |
| Modular curvature | $a_2(a,\triangle_\varphi) = -\frac{\pi}{2\tau_2}\varphi_0(a(K_0(\nabla)(\triangle(h)) + \frac{1}{2}H_0(\nabla_1,\nabla_2)(\Box_\Re(h)))$ | Eq. (4) |
| KO-dimension signs | $J^2 = \varepsilon,\; DJ = \varepsilon'JD,\; J\gamma = \varepsilon''\gamma J$ | Sec. 2 |
| Euler operation | $f \mapsto E(f),\; E(f)(v) := \sum_{\mathbb{N}^\times} f(nv)$ | Eq. (1) |
| NC torus | $VU = e^{2\pi i\theta}UV$ | Sec. 2.1 |

---

## Relevance to Phonon-Exflation

This survey provides the comprehensive context for the NCG spectral approach that the phonon-exflation framework uses. The identification of A_F = M_2(H) + M_4(C) with KO-dimension 6 is exactly the finite geometry the project computes D_K(tau) on. The inner fluctuation formula D_A = D + A + JAJ^{-1} generates the Standard Model gauge fields from the project's Dirac operator. The spectral action asymptotic expansion governs the heat coefficients a_0, a_2, a_4 that the project has computed across tau. The discussion of quantized volume and dimension 4 connects to the project's analysis of M4 x SU(3) with total KO-dimension 10 = 4 + 6.
