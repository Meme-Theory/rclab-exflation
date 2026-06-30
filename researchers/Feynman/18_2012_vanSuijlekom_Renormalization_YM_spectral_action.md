# Noncommutative complex differential geometry

**Author(s):** Edwin Beggs and S. Paul Smith
**Year:** 2012
**Journal:** (preprint; later published)
**arXiv/DOI:** arXiv:1209.3595v2 [math.AG] (6 Mar 2013)
**Relevance:** HIGH

> Note: the project request mapped slot #18 to 1209.3595.pdf, which is Beggs–Smith's "Noncommutative complex differential geometry" (not van Suijlekom's YM paper); the filename is retained per the request.

---

## Abstract

This paper defines and examines the basic properties of noncommutative analogues of almost complex structures, integrable almost complex structures, holomorphic curvature, cohomology, and holomorphic sheaves. The starting point is a differential structure on a noncommutative algebra defined in terms of a differential graded algebra. This is compared to current ideas on noncommutative algebraic geometry.

---

## Key Arguments and Derivations

**Section 1 (Philosophy and overview).** Frames the project as building a noncommutative analogue of classical complex differential geometry sufficient to support holomorphic sheaf cohomology, while staying compatible with noncommutative projective algebraic geometry (Artin–Tate–Van den Bergh–Zhang). Classical Kodaira/Chow/GAGA bridges between differential and algebraic geometry have no counterparts for noncommutative spaces; the paper argues that this gap is partly because most noncommutative projective varieties lack an underlying "real" manifold on which to impose an almost complex structure.

**Section 2 (∗-algebras and almost complex structures).**
- *∗-structure.* A ∗-algebra $(A,*)$: $(ab)^* = b^*a^*$, $(\lambda a + \mu b)^* = \bar\lambda a^* + \bar\mu b^*$, $a^{**}=a$.
- *Conjugate bimodule* $\bar E$ with $a\cdot\bar e = \overline{e\cdot a^*}$, $\bar e\cdot a = \overline{a^* e}$.
- *Universal differential calculus* $\Omega^\bullet_{\mathrm{univ}} A = T_A(\Omega^1_{\mathrm{univ}} A)$ with $da := 1\otimes a - a\otimes 1$.
- *Differential ∗-calculus.* A differential graded algebra $(\Omega^\bullet A, d, *)$ compatible with $*$: $(d\xi)^* = d(\xi^*)$, $(\xi\wedge\eta)^* = (-1)^{|\xi||\eta|}\eta^*\wedge\xi^*$.
- *Almost complex structure.* A degree-zero derivation $J:\Omega^\bullet A\to\Omega^\bullet A$ vanishing on $A$, with $J^2=-1$ on $\Omega^1 A$, and $J(\xi^*) = (J\xi)^*$. Decomposition $\Omega^1 A = \Omega^{1,0}A\oplus\Omega^{0,1}A$ into $\pm i$-eigenspaces; $(\Omega^{0,1}A)^* = \Omega^{1,0}A$.

**Extension to higher forms.** $J$ is extended as a derivation on $\Omega^\bullet A$; on $\Omega^n$, $J^2 = 2(J\wedge J - 1)$, not $-1$. One gets the bigraded decomposition $\Omega^n A = \bigoplus_{p+q=n}\Omega^{p,q}A$ with $\Omega^{p,q}A\wedge\Omega^{p',q'}A\subset\Omega^{p+p',q+q'}A$ and $(\Omega^{p,q}A)^* = \Omega^{q,p}A$. Operators $\partial: \Omega^{p,q}\to\Omega^{p+1,q}$ and $\bar\partial:\Omega^{p,q}\to\Omega^{p,q+1}$ defined as projections of $d$.

**Section 3 (Integrable complex structures; Newlander–Nirenberg analogue).** Calls $J$ integrable iff $d\Omega^{1,0}A \subset \Omega^{2,0}A\oplus\Omega^{1,1}A$. Proven equivalent conditions (Lemma 3.2): $\bar\partial^2 = 0$ on $A$, $\partial^2 = 0$ on $A$, $d = \partial+\bar\partial$ on $\Omega^1$, $d\Omega^{0,1}A\subset\Omega^{1,1}\oplus\Omega^{0,2}$. Operator reformulations (Lemma 3.3): $(1-J\wedge J)dJ = Jd$; $J^2 dJ = -2Jd$; $J^2 d = 2JdJ$; $JdJd = 0$. When $J$ is integrable, Proposition 3.5 gives $d\Omega^{p,q}\subset\Omega^{p+1,q}\oplus\Omega^{p,q+1}$, and Proposition 3.6 gives $\partial^2 = 0$, $\partial\bar\partial + \bar\partial\partial = 0$, $\bar\partial^2 = 0$. Proposition 3.7: $\partial,\bar\partial$ are super-derivations. Proposition 3.8: $\overline{\partial(\xi)^*} = \bar\partial(\xi^*)$.

**Section 3.2 (Holomorphic elements).** $A_{\mathrm{hol}} := \{f\in A : \bar\partial f = 0\}$ (holomorphic "functions"); $\Omega^p_{\mathrm{hol}}A := \{\omega\in\Omega^{p,0} : \bar\partial\omega = 0\}$. When $A$ is "connected" (only $\ker d|_A = \mathbb{C}$), any self-adjoint holomorphic element is a constant. $A_{\mathrm{hol}}$ is a $\mathbb{C}$-subalgebra and $\Omega^p_{\mathrm{hol}}$ an $A_{\mathrm{hol}}$-bimodule. The holomorphic de Rham complex $0\to A_{\mathrm{hol}} \to \Omega^1_{\mathrm{hol}}\to\cdots$ follows.

**Section 4 (Holomorphic modules, Koszul–Malgrange analogue).** A $\bar\partial$-operator on a left $A$-module $E$: $\bar\nabla: E\to\Omega^{0,1}A\otimes_A E$ with Leibniz $\bar\nabla(ae) = \bar\partial a\otimes e + a\bar\nabla e$. Extended to $\bar\nabla:\Omega^{0,q}\otimes E\to\Omega^{0,q+1}\otimes E$ by $\bar\nabla(\xi\otimes e) = \bar\partial\xi\otimes e + (-1)^q \xi\wedge\bar\nabla e$. *Holomorphic curvature* $\bar\nabla^2: E\to\Omega^{0,2}\otimes E$; when $\bar\nabla^2 = 0$, the pair $(E,\bar\nabla)$ is a *holomorphic $A$-module* — the noncommutative counterpart of a holomorphic vector bundle via the Koszul–Malgrange theorem. The category $\mathsf{Hol}(A)$ of such modules is abelian if $\Omega^{0,1}A$ is a flat right $A$-module (Prop. 4.5). Cohomology $H^\bullet(E,\bar\nabla)$ is the cohomology of the complex $\Omega^{0,\bullet}A\otimes_A E$; when all $\Omega^{p,q}$ are flat, short exact sequences yield long exact sequences in cohomology.

**Section 7 (Examples).** $\mathbb{CP}^n_\theta := \mathrm{Proj}_{\mathrm{nc}} R_\theta$ with relations $z_\mu z_\nu = \lambda^{\mu\nu} z_\nu z_\mu$, $\lambda^{\mu\nu} = e^{i\theta_{\mu\nu}}$; quantum group flag manifolds (Heckenberger–Kolb); $\mathbb{CP}^n_q$ studied by D'Andrea, Dabrowski, Khalkhali, Landi, Moatadelro, van Suijlekom. Polishchuk–Schwarz's noncommutative tori.

## Key Results

1. A noncommutative almost complex structure on a ∗-calculus $(\Omega^\bullet A, d, *)$ is a derivation $J$ with $J^2 = -1$ on $\Omega^1 A$ compatible with $*$.
2. Bigraded decomposition $\Omega^n A = \bigoplus_{p+q=n}\Omega^{p,q}A$ with $(\Omega^{p,q})^* = \Omega^{q,p}$.
3. Integrability $\Leftrightarrow$ $\bar\partial^2 = 0$ $\Leftrightarrow$ $d = \partial+\bar\partial$ $\Leftrightarrow$ $d\Omega^{1,0}\subset\Omega^{2,0}\oplus\Omega^{1,1}$ $\Leftrightarrow$ operator identities $J^2 d = 2JdJ$ etc.
4. Holomorphic modules and their cohomology $H^\bullet(E,\bar\nabla)$; $\mathsf{Hol}(A)$ is abelian when $\Omega^{0,1}A$ is right flat.
5. Concrete examples: $\mathbb{CP}^n_\theta$, $\mathbb{CP}^n_q$, quantum flag manifolds, noncommutative tori.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| conj-bimod | $a\cdot\bar e := \overline{e\cdot a^*}$, $\bar e\cdot a := \overline{a^*\cdot e}$ | §2.2 |
| univ-d | $da := 1\otimes a - a\otimes 1$, $\Omega^\bullet_{\mathrm{univ}} A = T_A(\Omega^1_{\mathrm{univ}} A)$ | §2.3 |
| star-comp | $(d\xi)^* = d(\xi^*)$, $(\xi\wedge\eta)^* = (-1)^{|\xi||\eta|}\eta^*\wedge\xi^*$ | Def 2.3 |
| acs | $J:\Omega^\bullet A\to\Omega^\bullet A$ derivation, $J|_A=0$, $J^2|_{\Omega^1}=-1$, $J\xi^* = (J\xi)^*$ | Def 2.6 |
| decomp | $\Omega^1 A = \Omega^{1,0}A\oplus\Omega^{0,1}A$ ($\pm i$-eigenspaces of $J$); $\Omega^n A = \bigoplus_{p+q=n}\Omega^{p,q}A$ | (2-3), Lemma 2.10 |
| Jsq-2form | $J^2 = 2(J\wedge J - 1)$ on $\Omega^2 A$ | (2-4) |
| partial-def | $\partial = \pi^{p+1,q}\circ d$, $\bar\partial = \pi^{p,q+1}\circ d$ | Def 2.11 |
| integrability | $d\Omega^{1,0}A\subset\Omega^{2,0}A\oplus\Omega^{1,1}A$ $\Leftrightarrow$ $\bar\partial^2 = 0$ $\Leftrightarrow$ $d=\partial+\bar\partial$ on $\Omega^1$ | Lemma 3.2 |
| op-criteria | $(1-J\wedge J)dJ = Jd$; $J^2 dJ = -2Jd$; $J^2 d = 2JdJ$; $JdJd = 0$ | Lemma 3.3 |
| consequences | $d\Omega^{p,q}\subset\Omega^{p+1,q}\oplus\Omega^{p,q+1}$; $\partial^2 = 0$; $\partial\bar\partial+\bar\partial\partial=0$; $\bar\partial^2=0$ | Prop 3.5–3.6 |
| star-partial | $\overline{\bar\partial(\xi)}^* = \partial(\xi^*)$, $\overline{\partial(\xi)}^* = \bar\partial(\xi^*)$ | Prop 3.8 |
| hol-elts | $A_{\mathrm{hol}} = \ker(\bar\partial\!\upharpoonright_A)$; $\Omega^p_{\mathrm{hol}} A = \{\omega\in\Omega^{p,0}: \bar\partial\omega=0\}$ | (3-11)–(3-12) |
| bar-nabla | $\bar\nabla(ae) = \bar\partial a\otimes e + a\bar\nabla e$; $\bar\nabla(\xi\otimes e) = \bar\partial\xi\otimes e + (-1)^q\xi\wedge\bar\nabla e$ | Def 4.1, (4-13) |
| hol-mod | $\bar\nabla^2 = 0 \Rightarrow (E,\bar\nabla)\in\mathsf{Hol}(A)$; $\bar\nabla^2$ is left $\Omega^{0,\bullet}A$-linear | Def 4.3, Lemma 4.2 |
| hol-coh | $H^\bullet(E,\bar\nabla) = H^\bullet(\Omega^{0,\bullet}A\otimes_A E, \bar\nabla)$ | §4.3 |

## Relevance to Phonon-Exflation

Provides the rigorous noncommutative-geometric framework for defining holomorphic/antiholomorphic structure on Jensen-deformed SU(3) fibre data. The bigraded decomposition $\Omega^{p,q}$ parallels the project's distinction between gauge-field (connection) and Higgs (scalar) fluctuations inside the spectral triple, and the Koszul–Malgrange analogue for holomorphic modules is the technical tool to define "holomorphic sheaves" on the post-transit EFT background. The ∗-calculus compatibility condition $(d\xi)^* = d(\xi^*)$ is directly what makes the ($[J, D_K]=0$, KO-dim=6, block-diagonal $D_K$) structure compatible with a chosen almost-complex structure on the fibre. The paper's quantum-flag-manifold and $\mathbb{CP}^n_q$ examples are the closest literature analogues of the Jensen SU(3) internal geometry.
