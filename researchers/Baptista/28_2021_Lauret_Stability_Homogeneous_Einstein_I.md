# On the Stability of Homogeneous Einstein Manifolds

**Author(s):** Jorge Lauret
**Year:** 2021 (revised 2022)
**Journal:** [Not stated in PDF]
**arXiv:** 2105.06336
**Relevance:** CRITICAL (Lichnerowicz stability of G-invariant Einstein metrics; directly determines Jensen deformation stability)

---

## Abstract

Let g be a G-invariant Einstein metric on a compact homogeneous space M = G/K. We use a formula for the Lichnerowicz Laplacian of g at G-invariant TT-tensors to study the stability type of g as a critical point of the scalar curvature function. The case when g is naturally reductive is studied in special detail.

---

## Key Arguments and Derivations

### 1. Introduction and Motivation (Section 1)

The paper studies the stability of G-invariant Einstein metrics on compact homogeneous spaces M = G/K within the G-invariant setting. A metric g in M_1^G is Einstein if and only if it is a critical point of the scalar curvature functional Sc: M_1^G -> R. The tangent space decomposes as:

T_g M_1^G = T_g Aut(G/K) . g  +  TT_g^G

where the first summand gives trivial variations and TT_g^G is the space of G-invariant TT-tensors.

An Einstein metric g is called **G-stable** when the Hessian satisfies Sc''_g|_{TT_g^G} < 0 (local maximum of Sc). It is **G-unstable** if Sc''_g(T,T) > 0 for some T in TT_g^G.

Key implications of G-stability types:
- G-non-degenerate implies G-rigid (isolated in moduli space)
- G-unstable implies dynamically unstable for Ricci flow and does not realize Yamabe invariant
- G-stability is extremely rare when dim M_1^G > 1

### 2. The Lichnerowicz Laplacian Formula (Section 4)

The second variation on TT-tensors is Sc''_g = (1/2)(2rho*id - Delta_L), where Delta_L is the Lichnerowicz Laplacian. The paper defines the self-adjoint operator L_p: sym(p)^K -> sym(p)^K via:

**Main Formula (Eq. 1):**
<L_p A, A> = (1/2)|theta(A) mu_p|^2 + 2 tr(M_{mu_p} A^2)

where mu_p = pr_p . [.,.]|_{p x p} and M is the moment map from geometric invariant theory for the representation theta of gl(p).

The G-stability type is determined by how the constant 2rho sits relative to the spectrum of L_p.

### 3. Naturally Reductive Case (Section 5)

When g is naturally reductive, the operator simplifies to:

**Formula (Eq. 2):**
L_p A = -(1/2) sum_i [ad_p X_i, [ad_p X_i, A]]

For the Killing metric g_B on a simple Lie group G: L_p(g_B) = (1/2) C_{tau, -B_g}, where C is the Casimir operator acting on the representation sym(g) of g.

**Result:** All Killing metrics on simple Lie groups are G-stable except SU(n) (n >= 3) which is G-neutrally stable of nullity n^2 - 1, and Sp(n) (n >= 2) which is G-unstable of coindex >= 2n(2n-1)/2 - 1.

### 4. Multiplicity-Free Matrix Formula (Section 5.2)

For a Q-orthogonal decomposition p = p_1 + ... + p_r in Ad(K)-irreducible and pairwise inequivalent subspaces, the structural constants are [ijk] = sum g([X_i, X_j], X_k)^2 and the Lichnerowicz Laplacian matrix entries are:

**Formula (Eq. 3):**
[L_p]_{kk} = (1/d_k) sum_{j != k, i} [ijk]
[L_p]_{jk} = -(1/sqrt{d_j d_k}) sum_i [ijk]   (j != k)

### 5. Standard Metric G-instability (Section 6)

Using formula (3), the standard metric is proved G-unstable (and Ricci flow dynamically unstable) on:
- SU(nk)/S(U(k) x ... x U(k)), k >= 1
- Sp(nk)/Sp(k) x ... x Sp(k), k >= 1
- SO(nk)/S(O(k) x ... x O(k)), k >= 3
with n >= 3 in all cases.

### 6. Jensen's Metrics (Section 7)

For a simple Lie group H with semisimple subgroup K, the Jensen metric g_t = -B_h|_a + t(-B_h)|_k is considered. With a Ad(K)-irreducible, the Einstein condition gives:

t_E = dc / ((d + 2k)(1 - c)),  2rho = c/(2t_E) + (1 - c)t_E/2

**Result:** Every Jensen Einstein metric g_{t_E} is G-unstable with coindex r, and is always a local minimum of Sc. This provides at least one H-unstable left-invariant Einstein metric on most simple Lie groups, including coindex >= 3 on E_6 and coindex >= 2 on SO(2n), Sp(2n), SU(n^2), E_7.

---

## Key Results

1. **Main Formula for L_p** (Eq. 1): Universal formula for the Lichnerowicz Laplacian on G-invariant TT-tensors via the moment map from GIT.

2. **Naturally Reductive Formula** (Eq. 2): L_p reduces to a Casimir operator when g is naturally reductive.

3. **Matrix Formula** (Eq. 3): Explicit matrix entries of L_p in the multiplicity-free case via structural constants [ijk].

4. **Killing Metric Stability** (Table 1): Complete classification: all G-stable except SU(n >= 3) (neutrally stable) and Sp(n >= 2) (G-unstable).

5. **Jensen Metrics are G-unstable**: Every Jensen Einstein metric on isotropy irreducible G/Delta_K is a local minimum with coindex r.

6. **Three Infinite Families G-unstable**: Standard metrics on SU(nk)/S(U(k)^n), Sp(nk)/Sp(k)^n, SO(nk)/S(O(k)^n) with n >= 3 are all G-unstable.

7. **Stability Hierarchy**: Sc-instability => nu-instability => dynamical instability (Ricci flow).

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Main L_p formula | $\langle L_p A, A \rangle = \frac{1}{2}|\theta(A)\mu_p|^2 + 2\,\mathrm{tr}(M_{\mu_p} A^2)$ | Eq. (1) |
| Naturally reductive L_p | $L_p A = -\frac{1}{2}\sum_i [\mathrm{ad}_p X_i, [\mathrm{ad}_p X_i, A]]$ | Eq. (2) |
| Killing metric Casimir | $L_p(g_B) = \frac{1}{2} C_{\tau, -B_g}$ | Below Eq. (2) |
| Matrix diagonal | $[L_p]_{kk} = \frac{1}{d_k}\sum_{j \neq k, i} [ijk]$ | Eq. (3) |
| Matrix off-diagonal | $[L_p]_{jk} = -\frac{1}{\sqrt{d_j d_k}}\sum_i [ijk]$ | Eq. (3) |
| G-stability criterion | $g$ is G-stable iff $2\rho < \lambda_L^G$ (smallest eigenvalue of $\Delta_L|_{TT_g^G}$) | Sec. 2 |
| Hessian formula | $\widetilde{\mathrm{Sc}}''_g(T,T) = -\frac{1}{2}\langle (\Delta_L - 2\rho\,\mathrm{id})T, T\rangle_g$ | Eq. in Sec. 2 |
| Ricci from moment map | $\mathrm{Ric}(g) = M_{\mu_p} - \frac{1}{2}B_\mu$ | Below Eq. (1) |
| Jensen Einstein condition | $t_E = \frac{dc}{(d+2k)(1-c)}$ | Sec. 7 |
| Scalar curvature | $\mathrm{Sc}(g) = -\frac{1}{4}|\mu_p|^2 - \frac{1}{2}\mathrm{tr}\,B$ | Eq. (10) |

---

## Relevance to Phonon-Exflation

This paper is **decisive** for the M4 x SU(3) framework. The Lichnerowicz Laplacian formula (Eq. 1-3) directly determines whether the Jensen deformation endpoint on SU(3) is stable or unstable as an Einstein metric. Several key connections:

1. **Jensen metric on SU(3)**: The framework's internal geometry involves SU(3) with a left-invariant metric deformed along the Jensen family. Theorem in Section 7 proves that **all Jensen Einstein metrics are G-unstable** with coindex r. For SU(3), this means the Jensen deformation endpoint is a local minimum of Sc (not a maximum), which has direct implications for whether the fold in the spectral action can stabilize tau.

2. **SU(n) is neutrally stable**: The Killing metric on SU(3) (n=3) is G-neutrally stable of nullity n^2 - 1 = 8. This means the standard metric sits at a critical eigenvalue Lambda_L = 2rho, neither stable nor unstable, but with an 8-dimensional space of infinitesimal Einstein deformations.

3. **Structural constants formalism**: The [ijk] structural constants and the matrix formula (3) provide the exact computational tool needed to evaluate the Lichnerowicz spectrum on SU(3)/K for any K, directly feeding into the TT-stability analysis of the phonon-exflation D_K operator spectrum.

4. **Ricci flow dynamics**: G-unstable Einstein metrics are dynamically unstable for Ricci flow, meaning the normalized Ricci flow flows away from them. This constrains which geometric configurations can serve as stable endpoints for the transit dynamics.
