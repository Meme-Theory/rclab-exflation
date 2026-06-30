# Curvature spectra of simple Lie groups

**Author(s):** Andrzej Derdzinski, Swiatoslaw R. Gal
**Year:** 2013
**Journal:** arXiv preprint (companion to 1209.6084)
**arXiv:** 1304.2801
**Relevance:** MEDIUM-HIGH (determines curvature operator spectrum for SU(3), controls Einstein metric isolation)

---

## Abstract

The Killing form $\beta$ of a real (or complex) semisimple Lie group $G$ is a left-invariant pseudo-Riemannian (or, respectively, holomorphic) Einstein metric. Let $\Omega$ denote the multiple of its curvature operator, acting on symmetric 2-tensors, with the factor chosen so that $\Omega\beta = 2\beta$. The result of Meyberg, describing the spectrum of $\Omega$ in complex simple Lie groups $G$, easily implies that 1 is not an eigenvalue of $\Omega$ in any real or complex simple Lie group $G$ except those locally isomorphic to SU$(p,q)$, or SL$(n,\mathbb{R})$, or SL$(n,\mathbb{C})$ or, for even $n$ only, SL$(n/2,\mathbb{H})$, where $p \ge q \ge 0$ and $p+q = n > 2$. Due to the last conclusion, on simple Lie groups $G$ other than the ones just listed, nonzero multiples of the Killing form $\beta$ are isolated among left-invariant Einstein metrics. Meyberg's theorem also allows us to understand the kernel of $\Lambda$, which is another natural operator. This in turn leads to a proof of a known, yet unpublished, fact: namely, that a semisimple real or complex Lie algebra with no simple ideals of dimension 3 is essentially determined by its Cartan three-form.

---

## Key Arguments and Derivations

### 1. The Curvature Operator $\Omega$ (Section 1-2)

For a semisimple Lie group $G$ with Lie algebra $\mathfrak{g}$, the connection $D$ defined by $D_x y = [x,y]/2$ is the Levi-Civita connection of the Killing form $\beta$. Its curvature is $D$-parallel, and so is the Ricci tensor $= -\beta/4$.

The operator $\Omega: [\mathfrak{g}^*]^{\odot 2} \to [\mathfrak{g}^*]^{\odot 2}$ acts on symmetric bilinear forms by:
$$[\Omega\sigma](x,y) = 2\text{tr}[(\text{Ad}_x)(\text{Ad}_y)\Sigma]$$
where $\Sigma: \mathfrak{g} \to \mathfrak{g}$ satisfies $\sigma(x,y) = \beta(\Sigma x, y)$.

Key properties: $\Omega\beta = 2\beta$ (eq. 1.5.ii), and $\Omega$ relates to the actual curvature operator of $\beta$ by $\Omega = -16 \times (\text{curvature operator on symmetric 2-tensors})$ (Remark 2.4).

The operator $T: [\mathfrak{g}^*]^{\otimes 2} \to [\mathfrak{g}^*]^{\otimes 2}$ with $(T\sigma)_{ij} = 2C_{ip}{}^k C_{jl}{}^p \sigma_{kl}$ restricts to $\Omega$ on symmetric 2-tensors and preserves the skew part (Lemma 2.1).

### 2. Meyberg's Theorem (Appendix)

For any complex simple Lie algebra $\mathfrak{g}$, $\Omega$ is diagonalizable. The eigenvalue systems are:

| Algebra | Spec $[\mathfrak{g}]$ | Mult $[\mathfrak{g}]$ |
|:--------|:---------------------|:---------------------|
| $\text{sl}_n$ ($n \ge 4$) | $(2, 1, 2/n, -2/n)$ | $(1, n^2-1, n^2(n-3)(n+1)/4, n^2(n+3)(n-1)/4)$ |
| $\text{sp}_n$ (even $n \ge 4$) | $(2, (n+4)/(n+2), -4/(n+2), 2/(n+2))$ | $(1, (n-2)(n+1)/2, n(n+1)(n+2)(n+3)/24, n(n-1)(n-2)(n+3)/12)$ |
| $\text{so}_n$ ($n = 7$ or $n \ge 9$) | $(2, (n-4)/(n-2), 4/(n-2), -2/(n-2))$ | $(1, (n+2)(n-1)/2, n(n-1)(n-2)(n-3)/24, n(n+1)(n+2)(n-3)/12)$ |
| Exceptional ($\text{sl}_2, \text{sl}_3, \mathfrak{g}_2, \text{so}_8, \mathfrak{f}_4, \mathfrak{e}_6, \mathfrak{e}_7, \mathfrak{e}_8$) | $(2, (1+w)/6, (1-w)/6)$ | see eq. (7.3) |

where for exceptional algebras, $w = [(d+242)/(d+2)]^{1/2}$ with $d = \dim\mathfrak{g}$.

**The eigenvalue 1 occurs if and only if $\mathfrak{g} \cong \text{sl}(n,\mathbb{C})$ for $n \ge 3$** (corresponding to $w = 5$, $d = 8$, i.e., $\text{sl}_3$).

### 3. Real Simple Lie Algebras (Theorem 4.1)

For real simple $\mathfrak{g}$ related to a complex simple $\mathfrak{h}$ by either:
- (a) $\mathfrak{g}$ is a real form of $\mathfrak{h}$, or
- (b) $\mathfrak{g}$ is $\mathfrak{h}$ treated as a real Lie algebra

The spectrum of $\Omega$ is:
- Case (a): Same spectrum as $\Omega_\mathfrak{h}$, same multiplicities
- Case (b): Doubled multiplicities from $\Omega_\mathfrak{h}$, plus eigenvalue 0 with complementary multiplicity

In both cases, the eigenspace $\text{Ker}(\Omega - 2\text{Id})$ is spanned by $\beta$ (case a) or $\text{Re}\,\beta_\mathfrak{h}$ and $\text{Im}\,\beta_\mathfrak{h}$ (case b).

### 4. The Operator $\Lambda$ and Theorem A

Define $\Lambda: [\mathfrak{g}^*]^{\odot 2} \to [\mathfrak{g}^*]^{\wedge 4}$ by:
$$(\Lambda\sigma)(x,y,z,z') = \sigma([x,y],[z,z']) + \sigma([y,z],[x,z']) + \sigma([z,x],[y,z'])$$

**Theorem A**: $2\Pi\Lambda = -(\Omega + \text{Id})(\Omega - 2\text{Id})$

where $\Pi: [\mathfrak{g}^*]^{\wedge 4} \to [\mathfrak{g}^*]^{\odot 2}$ is defined via the bracket. This algebraic identity relates the kernel of $\Lambda$ to the eigenspaces of $\Omega$.

### 5. Kernel of $\Lambda$ (Theorem B)

For $\mathfrak{g} = \mathfrak{g}_1 \oplus \ldots \oplus \mathfrak{g}_s$ (simple ideals):
- (i) $\text{Ker}\,\Lambda = \text{Ker}\,\Lambda_1 \oplus \ldots \oplus \text{Ker}\,\Lambda_s$
- (ii) $\Lambda = 0$ if $\dim\mathfrak{g} = 3$
- (iii) $\dim\text{Ker}\,\Lambda = 12$ if $\mathfrak{g}$ is simple with $\dim\mathfrak{g} = 6$ (only: underlying real algebra of $\text{sl}(2,\mathbb{C})$)
- (iv) $\dim\text{Ker}\,\Lambda \in \{1, 2\}$ if $\mathfrak{g}$ is simple with $\dim\mathfrak{g} \notin \{3, 6\}$

The key inclusion chain: $\text{Ker}(\Omega - 2\text{Id}) \subset \text{Ker}\,\Lambda \subset \text{Ker}(\Omega - 2\text{Id}) \oplus \text{Ker}(\Omega + \text{Id})$. When $-1 \notin \text{Spec}(\Omega)$ (which holds for $\dim\mathfrak{g} \notin \{3,6\}$), both inclusions become equalities.

### 6. Cartan Three-Form Rigidity (Theorem C)

The Cartan three-form $C = \beta([\ ,\ ],\cdot)$ essentially determines a semisimple Lie algebra (up to rescaling by cubic roots of unity), provided no simple ideals have dimension 3 or 6.

More precisely:
- (i) If $\mathfrak{g}$ has no summands of dimension 3, an isomorphism of Cartan three-forms implies Lie algebra isomorphism
- (ii) If no summands of dimension 3 or 6, every automorphism of $C$ is a Lie algebra automorphism followed by multiplication by a cubic root of 1

---

## Key Results

1. **Spectrum of $\Omega$ for SU(3)**: Since su(3) is a real form of sl$(3,\mathbb{C})$ (the exceptional case $d = 8$), $\Omega$ on su(3) has eigenvalues $\{2, 1, -1/3\}$ with multiplicities $\{1, 8, 27 - 8 - 1\} = \{1, 8, 18\}$. Specifically from (7.3): $w = \sqrt{(8+242)/(8+2)} = \sqrt{25} = 5$, so eigenvalues are $2$, $(1+5)/6 = 1$, and $(1-5)/6 = -2/3$.

2. **Eigenvalue 1 present for SU$(n)$, $n \ge 3$**: This is the ONLY class of compact simple groups where $1 \in \text{Spec}(\Omega)$. For all other compact simple groups (Sp$(n)$, SO$(n)$, $G_2$, $F_4$, $E_6$, $E_7$, $E_8$), $1 \notin \text{Spec}(\Omega)$ and the Killing metric is isolated among Einstein metrics.

3. **Despite eigenvalue 1, Killing form still isolated on SU$(n)$**: The eigenvalue-1 deformations produce indefinite (not positive-definite) Einstein metrics. The companion paper (1209.6084) shows that the compact form SU$(n)$ has $\mathcal{C} = \{D\}$ by the constraint $a^2 = 0 \Rightarrow a = 0$.

4. **Isolation for all non-sl-type groups**: On any simple Lie group not locally isomorphic to SL$(n)$-types, nonzero multiples of $\beta$ are isolated among left-invariant Einstein metrics. This follows directly from $1 \notin \text{Spec}(\Omega)$.

5. **Cartan three-form rigidity**: A semisimple Lie algebra with no 3-dimensional simple ideals is determined (up to cubic root rescaling) by its Cartan three-form. This is a proof of a previously known but unpublished result (attributed to R. Bryant).

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Killing form convention | $\beta(x,x) = \text{tr}[\text{Ad}_x]^2$ | Eq. (1.1) |
| Curvature operator $\Omega$ | $[\Omega\sigma](x,y) = 2\text{tr}[(\text{Ad}_x)(\text{Ad}_y)\Sigma]$ | Eq. (1.2) |
| Key eigenvalue: $\Omega\beta = 2\beta$ | $\Omega\beta = 2\beta$ | Eq. (1.5.ii) |
| Operator $T$ | $(T\sigma)_{ij} = 2C_{ipk}C_{jlp}\sigma_{kl}$ | Eq. (2.6) |
| Relation to curvature | $\Omega = -16 \times (\text{curvature operator on sym. 2-tensors})$ | Rem. 2.4 |
| $\Lambda$ operator | $(\Lambda\sigma)(x,y,z,z') = \sigma([x,y],[z,z']) + \sigma([y,z],[x,z']) + \sigma([z,x],[y,z'])$ | Eq. (1.4) |
| **Theorem A** | $2\Pi\Lambda = -(\Omega + \text{Id})(\Omega - 2\text{Id})$ | Theorem A |
| Trace identity | $2C_{irp}C_{jqr}C_{kpq} = C_{ijk}$ | Eq. (2.5) |
| Meyberg: sl$_n$ spectrum | Spec = $(2, 1, 2/n, -2/n)$ | Appendix |
| Meyberg: exceptional spectrum | Spec = $(2, (1+w)/6, (1-w)/6)$, $w = \sqrt{(d+242)/(d+2)}$ | Eq. (7.3) |
| Real form spectrum (type a) | Same as $\Omega_\mathfrak{h}$ | Thm 4.1(ii) |
| Real form spectrum (type b) | Doubled multiplicities + eigenvalue 0 | Thm 4.1(iii) |
| Cartan three-form | $C = \beta([\ ,\ ],\cdot)$ | Eq. (1.7) |

---

## Relevance to Phonon-Exflation

**This paper, together with its companion 1209.6084, provides the definitive answer to a question central to the framework:**

1. **The bi-invariant metric on SU(3) is isolated among Riemannian Einstein metrics**: The curvature operator $\Omega$ on su(3) has eigenvalue 1 (from the sl$_3$ Meyberg spectrum), but the corresponding deformations are all indefinite. For the compact form SU(3), the Riemannian Einstein moduli near the Killing form is zero-dimensional. This means:
   - The Jensen-deformed metric $g(\tau)$ for $\tau > 0$ is NOT Einstein
   - There is no continuous family of Einstein metrics connecting $\beta$ to a different Einstein metric in the positive-definite cone
   - The spectral action on SU(3) with Jensen deformation sees a departure from the Einstein condition, which is the geometric driver of the tau-dynamics

2. **Spectrum of $\Omega$ for SU(3) explicitly**: Eigenvalues $\{2, 1, -2/3\}$ with multiplicities $\{1, 8, 18\}$. The eigenvalue-2 eigenspace is spanned by $\beta$ itself. The eigenvalue-1 eigenspace has dimension 8 (= $n^2 - 1$ for $n = 3$, matching dim SU(3)). The eigenvalue $-2/3$ eigenspace has dimension 18. This spectral decomposition of the curvature operator directly controls the linearized deformation theory of the metric on SU(3).

3. **The curvature operator controls the Seeley-DeWitt coefficients**: The operator $\Omega$ acting on symmetric 2-tensors is exactly the object that enters the Seeley-DeWitt heat-kernel expansion ($a_2$ coefficient) of the spectral action on SU(3). The framework's computations of $a_2/a_4$ ratios (Session 20a) depend on this spectral data.

4. **Cartan three-form rigidity**: The result that su(3) is determined by its Cartan three-form $C = \beta([\ ,\ ],\cdot)$ means the Lie algebra structure is rigid — it cannot be continuously deformed to a different Lie algebra while preserving $C$. This supports the framework's use of SU(3) as a fixed algebraic structure (only the metric varies, not the Lie algebra).

5. **Connection to the constant-ratio trap**: The eigenvalue decomposition of $\Omega$ into $\{2, 1, -2/3\}$ subspaces is directly related to how Casimir contributions from different representation sectors scale — the constant-ratio trap ($F/B = 0.55$ from Weyl's law) reflects the overall spectral measure, while the individual eigenspaces of $\Omega$ control the sector-by-sector response to deformation.
