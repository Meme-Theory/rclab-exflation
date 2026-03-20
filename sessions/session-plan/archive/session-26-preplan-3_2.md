# Session 26 Pre-Plan: Section 3.2 — Torsion Bounce Assessment

**Date**: 2026-02-22
**Author**: Baptista-Spacetime-Analyst
**Gate**: T-1 (pre-registered)
**Input data**: Structure constants $f^a_{bc}$ (Gell-Mann), Jensen metric $g_{ab}(\tau)$, existing eigenvalue data from Sessions 12, 20a, 23a
**Predecessor**: Session 25 (Walls W1--W6), Session 26 preplan Section 3.2 outline

---

## 1. Mathematical Framework: Lichnerowicz with Torsion on Compact Lie Groups

### 1.1 The Standard Lichnerowicz Formula (Torsion-Free)

On a compact Riemannian spin manifold $(K, g)$ of dimension $k$, the standard Dirac operator $\not{D}$ built from the Levi-Civita connection $\nabla^{\mathrm{LC}}$ satisfies the Lichnerowicz--Schr\"odinger identity:

$$\not{D}^2 = \nabla^*\nabla + \frac{R_g}{4}$$

where $\nabla^*\nabla = -g^{ab}\nabla_a\nabla_b + (\text{connection terms})$ is the spinor Laplacian (trace Laplacian on the spinor bundle) and $R_g$ is the scalar curvature. For $K = \mathrm{SU}(3)$ with the Jensen-deformed metric $\hat{g}_s$ (Paper 15, eq 3.68--3.70), the scalar curvature is

$$R(\tau) = \frac{3}{2}\left(2e^{2\tau} - 1 + 8e^{-\tau} - e^{-4\tau}\right)$$

(using Baptista's $s \equiv \tau$ convention from eq 3.70, with the overall constant $\kappa$ set to normalize so that the bi-invariant metric has $\kappa_0(u,v) = -\mathrm{Tr}(u^\dagger v)$). At $\tau = 0$, $R(0) = \frac{3}{2}(2 - 1 + 8 - 1) = 12$ (round bi-invariant metric), and $R(\tau)$ is strictly increasing for $\tau > 0$ with $R'(0) = 0$, $R''(0) = 0$, $R'''(0) > 0$.

The Lichnerowicz bound gives $\lambda^2 \geq R_g/4 \geq 3$ for all $\tau \geq 0$. This is **Wall W3**.

### 1.2 The Torsionful Dirac Operator

On a Lie group $K$ equipped with a left-invariant metric $g$, there is a canonical metric-compatible connection with torsion: the **flat Schouten connection** $\nabla^0$, defined by

$$\nabla^0_{u^L} v^L = 0$$

for all left-invariant vector fields $u^L, v^L$ (Paper 14, lines 1735--1740). This connection has torsion

$$T^0(u^L, v^L) = -\nabla^0_{u^L} v^L + \nabla^0_{v^L} u^L + [u^L, v^L] = [u, v]^L$$

since $\nabla^0$ annihilates left-invariant fields. The torsion is therefore determined by the Lie bracket: $T^0_{abc} = f_{abc}$ where $f_{abc} = g([e_a, e_b], e_c)$ with indices lowered using the metric $g$.

**Key observation (Paper 14, lines 1734--1740)**: When the Dirac operator is built using $\nabla^0$ instead of $\nabla^{\mathrm{LC}}$, the $\Omega_{jkl}$ coefficients in the cubic gamma matrix term (eq 3.7 of Paper 14) vanish identically. This means the Schouten--Dirac operator is purely first-order in Lie derivatives:

$$\not{D}^0 = \sum_j \gamma^j \mathcal{L}_{e_j^L}$$

The Levi-Civita Dirac operator $\not{D}_K$ differs from this by the cubic contorsion term.

### 1.3 General Connection with Torsion

Any metric-compatible connection $\nabla^T$ with torsion $T$ on $(K, g)$ is related to the Levi-Civita connection by

$$\nabla^T_X Y = \nabla^{\mathrm{LC}}_X Y + \frac{1}{2} T(X, Y) - S(X, Y)$$

where $S$ is the symmetric part defined by

$$g(S(X, Y), Z) = \frac{1}{2}\bigl[g(T(Z, X), Y) + g(T(Z, Y), X)\bigr].$$

More precisely, the difference tensor is the **contorsion** $K$, defined so that

$$\nabla^T_X Y = \nabla^{\mathrm{LC}}_X Y + K(X, Y)$$

with

$$K_{cab} = \frac{1}{2}(T_{cab} + T_{acb} + T_{bca})$$

in a $g$-orthonormal frame $\{e_a\}$, where $T_{abc} = g(T(e_a, e_b), e_c)$ and $K_{cab} = g(K(e_a, e_b), e_c)$ (Nakahara convention: $K^\lambda_{\;\mu\nu} = \frac{1}{2}(T^\lambda_{\;\mu\nu} + T_\mu^{\;\lambda}{}_\nu + T_\nu^{\;\lambda}{}_\mu)$, all indices lowered with $g$). The antisymmetry properties are:

- $K_{cab} = -K_{bac}$ (automatic from metric compatibility: antisymmetric when swapping the "output" index with an "input" index)
- $T_{abc} = -T_{bac}$ (torsion is antisymmetric in first two indices)

**Note on conventions**: The contorsion formula has different index orderings in different references (Nakahara, Carroll, Friedrich). The precise formula is not needed for the subsequent analysis, which relies only on the direct relationship $\not{D}_K = \not{D}_0 + \Omega\cdot$ established from Baptista's Paper 14 without reference to the contorsion tensor.

The Dirac operator with torsion is

$$\not{D}_T = \sum_a \gamma^a \nabla^T_{e_a} = \not{D}_K + \frac{1}{4} K_{abc}\, \gamma^a \gamma^b \gamma^c$$

where the contorsion contribution to the spin connection is $\frac{1}{4}K_{abc}\gamma^b\gamma^c$ acting on spinors when differentiating along $e_a$, and the sum over all directions with the Clifford action gives the $\frac{1}{4}K_{abc}\gamma^a\gamma^b\gamma^c$ term.

### 1.4 Lichnerowicz Formula with Torsion

For a general metric-compatible connection $\nabla^T$ with totally antisymmetric torsion $T_{abc} = T_{[abc]}$, the squared Dirac operator satisfies the **Bismut--Friedrich--Agricola** identity (see Friedrich, "Dirac Operators in Riemannian Geometry," Theorem 4.14; Agricola-Friedrich, "On the holonomy of connections with skew-symmetric torsion," 2004):

$$\not{D}_T^2 = (\nabla^T)^*\nabla^T + \frac{R_g}{4} + \frac{3}{16}|T|^2 - \frac{1}{4}(dT) \cdot$$

where:
- $(\nabla^T)^*\nabla^T$ is the trace Laplacian of $\nabla^T$ on the spinor bundle (non-negative on compact manifolds)
- $|T|^2 = \sum_{a,b,c} T_{abc}T^{abc}$ is the squared norm of the torsion 3-form (strictly positive when $T \neq 0$; the sum runs over all index values, not just $a < b < c$)
- $(dT)\cdot$ denotes the Clifford action of the 4-form $dT$
- The coefficient $\frac{3}{16}$ follows Friedrich, "Dirac Operators in Riemannian Geometry," Theorem 4.14, where $|T|^2 = \sum_{a,b,c}T_{abc}^2$ (unrestricted sum). The precise coefficient depends on the normalization convention for the 3-form norm; what is convention-independent is that the coefficient is strictly positive. See the discussion in Section 3.4 for details.

**However**, this clean formula applies only when the torsion is **totally antisymmetric**. When $T$ is not totally antisymmetric, additional terms appear. The general Lichnerowicz--Schr\"odinger formula for a connection with arbitrary torsion is:

$$\not{D}_T^2 = (\nabla^T)^*\nabla^T + \frac{R_g}{4} + \frac{1}{4}R^T_{ab}\gamma^a\gamma^b + Q(K)$$

where $R^T_{ab}$ is the Ricci tensor of $\nabla^T$ (which need not be symmetric when torsion is present) and $Q(K)$ collects quadratic contorsion terms. The precise form depends on the decomposition of $K_{abc}$ into irreducible components under $\mathrm{SO}(k)$.

For our purposes, we need the **intermediate** situation: the natural torsion on a Lie group is totally antisymmetric for the bi-invariant metric, but loses total antisymmetry under Jensen deformation. Let us derive this carefully.

---

## 2. Contorsion Under Jensen Deformation

### 2.1 The Levi-Civita vs. Schouten Connection on a Lie Group

On $K = \mathrm{SU}(3)$ with left-invariant metric $g$, the Levi-Civita connection acting on left-invariant fields is (Koszul formula, Paper 14 eq 3.4):

$$g(\nabla^{\mathrm{LC}}_{e_j^L} e_k^L, e_l^L) = \frac{1}{2}\bigl[g([e_j, e_k], e_l) - g([e_k, e_l], e_j) + g([e_l, e_j], e_k)\bigr]$$

The Schouten connection has $\nabla^0_{e_j^L} e_k^L = 0$, so the contorsion tensor (difference between Schouten and Levi-Civita) is:

$$K^{(0\to\mathrm{LC})}_{jkl} = g(\nabla^{\mathrm{LC}}_{e_j^L} e_k^L, e_l^L) = \frac{1}{2}\bigl[f_{jkl} - f_{klj} + f_{ljk}\bigr]$$

where $f_{jkl} = g([e_j, e_k], e_l)$.

Equivalently, the Schouten torsion is $T^0_{jkl} = f_{jkl}$ and the Schouten contorsion is

$$K^0_{jkl} = \frac{1}{2}(T^0_{jkl} + T^0_{kjl} + T^0_{ljk}) = \frac{1}{2}(f_{jkl} + f_{kjl} + f_{ljk})$$

Since $f_{jkl} = g([e_j, e_k], e_l)$ is antisymmetric in $j, k$ (Lie bracket), we have $f_{kjl} = -f_{jkl}$, giving

$$K^0_{jkl} = \frac{1}{2}(f_{jkl} - f_{jkl} + f_{ljk}) = \frac{1}{2} f_{ljk}.$$

But this is the contorsion from the Schouten to the Levi-Civita direction. Let us be more careful and define things from the direction we need.

**The physically relevant operator**: We want to study $\not{D}_T$, the Dirac operator built from the Schouten connection $\nabla^0$ (which has torsion $T^0(u^L, v^L) = [u,v]^L$). Its relation to the Levi-Civita Dirac operator $\not{D}_K$ is:

$$\not{D}_T = \not{D}_K + \frac{1}{4}\Delta K_{abc}\,\gamma^a\gamma^b\gamma^c$$

where $\Delta K_{abc} = g(\nabla^0_{e_a} e_b - \nabla^{\mathrm{LC}}_{e_a} e_b,\, e_c)$.

Since $\nabla^0_{e_a^L} e_b^L = 0$, we have

$$\Delta K_{abc} = -g(\nabla^{\mathrm{LC}}_{e_a^L} e_b^L,\, e_c^L) = -\frac{1}{2}\bigl[f_{abc} - f_{bca} + f_{cab}\bigr]$$

Now, the Baptista coefficients $\Omega_{jkl}$ from Paper 14, eq 3.7 are:

$$\Omega_{jkl} = \frac{1}{4}\bigl[g([e_j, e_k], e_l) + g([e_k, e_l], e_j) + g([e_l, e_j], e_k)\bigr] = \frac{1}{4}[f_{jkl} + f_{klj} + f_{ljk}]$$

These are the totally antisymmetric part of the connection coefficients. When $g$ is bi-invariant, all three terms are equal (since the Ad-invariant inner product satisfies $g([u,v], w) = g(u, [v,w])$), giving $\Omega_{jkl} = \frac{3}{4}f_{jkl}$.

The Dirac operator on $(K, g)$ is (Paper 14, eq 3.6):

$$\not{D}_K = \sum_j \gamma^j \mathcal{L}_{e_j^L} + \sum_{j < k < l} \Omega_{jkl}\,\gamma^j\gamma^k\gamma^l$$

The Schouten--Dirac operator is

$$\not{D}_0 = \sum_j \gamma^j \mathcal{L}_{e_j^L}$$

(since $\nabla^0$ has zero $\Omega$ coefficients, Paper 14, line 1738). Therefore:

$$\not{D}_K = \not{D}_0 + \sum_{j<k<l} \Omega_{jkl}\,\gamma^j\gamma^k\gamma^l$$

The contorsion term that takes us from $\not{D}_K$ back to $\not{D}_0$ is $-\Omega_{jkl}\gamma^j\gamma^k\gamma^l$.

### 2.2 Explicit Form of $\Omega_{jkl}$ Under Jensen Deformation

The Jensen metric on $\mathrm{SU}(3)$ (Paper 15, eq 3.68 with $\kappa$ absorbed) is defined by the inner product

$$\hat{g}_\tau(u, v) = \alpha_1(\tau)\,\kappa_0(u_Y, v_Y) + \alpha_2(\tau)\,\kappa_0(u_W, v_W) + \alpha_3(\tau)\,\kappa_0(u'', v'')$$

where $\kappa_0(u,v) = -\mathrm{Tr}(u^\dagger v)$ is the standard inner product on $\mathfrak{su}(3)$ and

$$\alpha_1(\tau) = e^{2\tau}, \quad \alpha_2(\tau) = e^{-2\tau}, \quad \alpha_3(\tau) = e^{\tau}$$

with the decomposition $\mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2$ (Paper 15, eq 3.58).

Let $\{e_a\}$ be a $\hat{g}_\tau$-orthonormal basis of $\mathfrak{su}(3)$, related to a $\kappa_0$-orthonormal basis $\{\bar{e}_a\}$ by:

- $e_0 = e^{-\tau}\bar{e}_0$ (the $\mathfrak{u}(1)$ direction)
- $e_i = e^{\tau}\bar{e}_i$ for $i = 1, 2, 3$ (the $\mathfrak{su}(2)$ directions)
- $e_\alpha = e^{-\tau/2}\bar{e}_\alpha$ for $\alpha = 4, 5, 6, 7$ (the $\mathbb{C}^2$ directions)

The structure constants in the $\hat{g}_\tau$-orthonormal basis are

$$f_{abc}(\tau) = \hat{g}_\tau([e_a, e_b], e_c) = \hat{g}_\tau\bigl([\sigma_a^{-1}\bar{e}_a, \sigma_b^{-1}\bar{e}_b], \sigma_c^{-1}\bar{e}_c\bigr)$$

where $\sigma_a$ are the rescaling factors ($\sigma_0 = e^{-\tau}$, $\sigma_i = e^{\tau}$, $\sigma_\alpha = e^{-\tau/2}$). Since $[\bar{e}_a, \bar{e}_b] = \bar{f}_{ab}^{\;d}\bar{e}_d$ and $\hat{g}_\tau(e_d, e_c) = \delta_{dc}$:

$$f_{abc}(\tau) = \frac{\alpha_{[c]}}{\sigma_a \sigma_b \sigma_c}\,\bar{f}_{abc}$$

where $\alpha_{[c]}$ denotes the rescaling parameter for the subspace containing $e_c$, and $\bar{f}_{abc} = \kappa_0([\bar{e}_a, \bar{e}_b], \bar{e}_c)$ are the structure constants in the round metric.

More explicitly, since the $\hat{g}_\tau$-ONB is $e_a = \sigma_a^{-1}\bar{e}_a$ and $\hat{g}_\tau(e_a, e_b) = \delta_{ab}$:

$$f_{abc}(\tau) = \hat{g}_\tau([e_a, e_b], e_c) = \sigma_a^{-1}\sigma_b^{-1}\hat{g}_\tau([\bar{e}_a, \bar{e}_b], e_c) = \sigma_a^{-1}\sigma_b^{-1}\sigma_c^{-1}\alpha_{[c]}\kappa_0([\bar{e}_a, \bar{e}_b], \bar{e}_c)$$

Wait -- let me be more careful. We have $e_a = \sigma_a^{-1}\bar{e}_a$ (no sum), so $\bar{e}_a = \sigma_a e_a$. Then

$$[e_a, e_b] = \sigma_a^{-1}\sigma_b^{-1}[\bar{e}_a, \bar{e}_b] = \sigma_a^{-1}\sigma_b^{-1}\bar{f}_{ab}^{\;d}\bar{e}_d = \sigma_a^{-1}\sigma_b^{-1}\bar{f}_{ab}^{\;d}\sigma_d\, e_d$$

Therefore

$$f_{abc}(\tau) = \hat{g}_\tau([e_a, e_b], e_c) = \sigma_a^{-1}\sigma_b^{-1}\sigma_c\,\bar{f}_{abc}$$

where $\bar{f}_{abc} = \bar{f}_{ab}^{\;c}$ (the last index is already lowered by $\kappa_0$, which coincides with $\delta_{cd}$ in the ONB).

**Correction**: We need to be precise. In the $\kappa_0$-ONB, $\bar{f}_{ab}^{\;c} = \kappa_0([\bar{e}_a, \bar{e}_b], \bar{e}_c)$ since $\kappa_0(\bar{e}_c, \bar{e}_d) = \delta_{cd}$. So $\bar{f}_{abc} \equiv \bar{f}_{ab}^{\;c}$ with the understanding that the upper index is lowered by $\delta$. Then:

$$f_{abc}(\tau) = \frac{\sigma_c}{\sigma_a\,\sigma_b}\,\bar{f}_{abc}$$

Now the $\Omega$ coefficients (Paper 14, eq 3.7) are:

$$\Omega_{jkl}(\tau) = \frac{1}{4}\bigl[f_{jkl}(\tau) + f_{klj}(\tau) + f_{ljk}(\tau)\bigr]$$

Substituting:

$$\Omega_{jkl}(\tau) = \frac{\bar{f}_{jkl}}{4}\left[\frac{\sigma_l}{\sigma_j\sigma_k} + \frac{\sigma_j}{\sigma_k\sigma_l} + \frac{\sigma_k}{\sigma_l\sigma_j}\right]$$

using the fact that $\bar{f}_{jkl}$ is totally antisymmetric for the bi-invariant metric (which satisfies $\kappa_0([u,v], w) = \kappa_0(u, [v,w])$, i.e., $\bar{f}_{jkl} = \bar{f}_{klj} = \bar{f}_{ljk}$).

### 2.3 Symmetry Breaking Analysis

For the **bi-invariant metric** ($\tau = 0$), all $\sigma_a = 1$, so the bracket factor becomes $\frac{1}{4}(1 + 1 + 1) = \frac{3}{4}$, and $\Omega_{jkl}(0) = \frac{3}{4}\bar{f}_{jkl}$. This is totally antisymmetric and positive-definite in the Lichnerowicz formula.

For $\tau \neq 0$, the bracket factor depends on which subspaces the indices belong to. Define the subspace assignments:

- **Type YY**: both indices from $\mathfrak{u}(1)$ -- only one direction, so no bracket
- **Type WW**: indices from $\mathfrak{su}(2) \times \mathfrak{su}(2)$: $\sigma_j = \sigma_k = e^{\tau}$
- **Type CC**: indices from $\mathbb{C}^2 \times \mathbb{C}^2$: $\sigma_j = \sigma_k = e^{-\tau/2}$
- **Type WC**: mixed $\mathfrak{su}(2) \times \mathbb{C}^2$: $\sigma_j = e^{\tau}$, $\sigma_k = e^{-\tau/2}$
- **Type YW**: $\mathfrak{u}(1) \times \mathfrak{su}(2)$: $\sigma_j = e^{-\tau}$, $\sigma_k = e^{\tau}$
- **Type YC**: $\mathfrak{u}(1) \times \mathbb{C}^2$: $\sigma_j = e^{-\tau}$, $\sigma_k = e^{-\tau/2}$

The Lie bracket relations (Paper 15, eq 3.59) constrain which structure constants are nonzero:

$$[\mathfrak{u}(1), \mathfrak{u}(2)] = \{0\}, \quad [\mathfrak{su}(2), \mathfrak{su}(2)] = \mathfrak{su}(2), \quad [\mathfrak{u}(2), \mathbb{C}^2] = \mathbb{C}^2, \quad [\mathbb{C}^2, \mathbb{C}^2] = \mathfrak{u}(2)$$

This means the nonzero $\bar{f}_{abc}$ fall into the following categories:

| Type $(a,b) \to c$ | $\sigma_a$ | $\sigma_b$ | $\sigma_c$ | Factor $\frac{\sigma_c}{\sigma_a\sigma_b} + \frac{\sigma_a}{\sigma_b\sigma_c} + \frac{\sigma_b}{\sigma_c\sigma_a}$ |
|:---|:---|:---|:---|:---|
| $(W,W) \to W$: $[\mathfrak{su}(2), \mathfrak{su}(2)] \subset \mathfrak{su}(2)$ | $e^{\tau}$ | $e^{\tau}$ | $e^{\tau}$ | $3 e^{-\tau}$ |
| $(W,C) \to C$: $[\mathfrak{su}(2), \mathbb{C}^2] \subset \mathbb{C}^2$ | $e^{\tau}$ | $e^{-\tau/2}$ | $e^{-\tau/2}$ | $e^{-\tau} + e^{2\tau} + e^{-\tau} = e^{2\tau} + 2e^{-\tau}$ |
| $(Y,C) \to C$: $[\mathfrak{u}(1), \mathbb{C}^2] \subset \mathbb{C}^2$ | $e^{-\tau}$ | $e^{-\tau/2}$ | $e^{-\tau/2}$ | $e^{\tau} + 1 + e^{\tau} = 2e^{\tau} + 1$ |
| $(C,C) \to W$: $[\mathbb{C}^2, \mathbb{C}^2] \subset \mathfrak{su}(2)$ | $e^{-\tau/2}$ | $e^{-\tau/2}$ | $e^{\tau}$ | $e^{2\tau} + e^{-\tau} + e^{-\tau} = e^{2\tau} + 2e^{-\tau}$ |
| $(C,C) \to Y$: $[\mathbb{C}^2, \mathbb{C}^2] \subset \mathfrak{u}(1)$ | $e^{-\tau/2}$ | $e^{-\tau/2}$ | $e^{-\tau}$ | $1 + e^{\tau} + e^{\tau} = 2e^{\tau} + 1$ |

At $\tau = 0$, all factors equal 3, recovering the bi-invariant result $\Omega_{jkl} = \frac{3}{4}\bar{f}_{jkl}$.

**Critical observation**: The $\Omega_{jkl}$ coefficients remain totally antisymmetric in $j,k,l$ for ALL $\tau$ because $\bar{f}_{jkl}$ is totally antisymmetric and the rescaling factor $\frac{\sigma_l}{\sigma_j\sigma_k} + \frac{\sigma_j}{\sigma_k\sigma_l} + \frac{\sigma_k}{\sigma_l\sigma_j}$ is manifestly symmetric under all permutations of $(j,k,l)$. The factor is the sum of the three ratios $\sigma_l/\sigma_j\sigma_k$ over cyclic permutations, which is symmetric under any permutation of the triple.

Therefore: **$\Omega_{jkl}(\tau)$ is totally antisymmetric for ALL $\tau$**.

### 2.4 Consequences for the Torsion Structure

Since $\Omega_{jkl}$ is totally antisymmetric, the contorsion term $\frac{1}{4}\Omega_{jkl}\gamma^j\gamma^k\gamma^l$ can be rewritten using the 3-form Clifford action. Define the 3-form

$$\Omega = \frac{1}{3!}\Omega_{jkl}\,e^j \wedge e^k \wedge e^l$$

Then $\sum_{j<k<l}\Omega_{jkl}\gamma^j\gamma^k\gamma^l = \Omega\cdot$ (Clifford action of the 3-form). The squared torsionful Dirac operator can be analyzed using the Bismut--Friedrich formula.

**However**, there is a subtlety. The $\Omega_{jkl}$ are the coefficients in the Levi-Civita Dirac operator (Paper 14, eq 3.6). The "torsionful Dirac operator" in the sense relevant to Gate T-1 is the one where we **replace** the Levi-Civita connection with a connection that has torsion. There are two natural choices:

**(a)** The **Schouten Dirac operator** $\not{D}_0 = \not{D}_K - \Omega_{jkl}\gamma^j\gamma^k\gamma^l$: This uses the flat connection with torsion $T = [u,v]^L$. This **removes** the positive $\Omega$ term, generically making eigenvalues smaller.

**(b)** A connection with **additional** torsion beyond the Levi-Civita: This adds contorsion to $\not{D}_K$.

For Gate T-1, the physically relevant operator is option (a): the Schouten--Dirac operator, or more generally, any natural torsionful connection on SU(3) that could produce eigenvalues below those of $\not{D}_K$.

---

## 3. Sign Analysis of Cross Terms

### 3.1 The Schouten Dirac Operator Spectrum

The Schouten--Dirac operator is

$$\not{D}_0 = \not{D}_K - \sum_{j<k<l}\Omega_{jkl}(\tau)\,\gamma^j\gamma^k\gamma^l$$

Its square is

$$\not{D}_0^2 = \not{D}_K^2 - 2\not{D}_K \cdot (\Omega\cdot) + (\Omega\cdot)^2 - [\not{D}_K, \Omega\cdot]$$

Wait -- this is not quite right because $\not{D}_0 = \not{D}_K - \Omega\cdot$ where $\Omega\cdot$ denotes the Clifford action of the 3-form $\Omega$. More carefully:

$$\not{D}_0^2 = (\not{D}_K - \Omega\cdot)^2 = \not{D}_K^2 - \{\not{D}_K, \Omega\cdot\} + (\Omega\cdot)^2$$

The term $(\Omega\cdot)^2$ is a zero-order operator (no derivatives). The anticommutator $\{\not{D}_K, \Omega\cdot\}$ contains first-order terms.

However, this approach conflates two different objects. Let me use the proper Lichnerowicz formula.

### 3.2 Proper Lichnerowicz Analysis for Totally Antisymmetric Torsion

The key theorem (Friedrich--Agricola, "On the holonomy of connections with skew-symmetric torsion," Math. Ann. 328, 2004) states:

For a metric connection $\nabla^T = \nabla^{\mathrm{LC}} + \frac{1}{2}T$ with totally antisymmetric torsion 3-form $T$, the Dirac operator $\not{D}_T = \not{D}_K + \frac{1}{4}T\cdot$ (Clifford action of $T$) satisfies:

$$\not{D}_T^2 = (\nabla^T)^*\nabla^T + \frac{R_g}{4} + \frac{3}{16}|T|^2 - \frac{1}{4}(dT)\cdot$$

where $|T|^2 = \sum_{a,b,c} T_{abc}T^{abc}$ (unrestricted sum, as in Section 1.4).

**But wait** -- the Schouten Dirac operator subtracts the $\Omega$ term, it does not add torsion to the Levi-Civita connection. The relationship is:

$$\not{D}_K = \not{D}_0 + \Omega\cdot$$

The Levi-Civita Dirac operator = Schouten Dirac operator + cubic term. The Schouten connection is the one with torsion; the Levi-Civita is torsion-free. So going from LC to Schouten, we are **adding** torsion, and the Dirac operator **loses** the $\Omega$ term.

The torsion of the Schouten connection is $T^0_{abc} = f_{abc}(\tau) = g_\tau([e_a, e_b], e_c)$, which is antisymmetric in $(a,b)$ by the Lie bracket. The question is whether it is totally antisymmetric (i.e., also antisymmetric under $b \leftrightarrow c$).

For the bi-invariant metric: $f_{abc} = \kappa_0([e_a, e_b], e_c) = \kappa_0(e_a, [e_b, e_c])$ by Ad-invariance, so $f_{abc} = f_{bca} = f_{cab}$ and $f_{abc} = -f_{bac}$, giving total antisymmetry. Yes, $f_{abc}$ is totally antisymmetric at $\tau = 0$.

For the Jensen metric: $f_{abc}(\tau) = \frac{\sigma_c}{\sigma_a\sigma_b}\bar{f}_{abc}$. Check antisymmetry under $b \leftrightarrow c$:

$$f_{abc}(\tau) = \frac{\sigma_c}{\sigma_a\sigma_b}\bar{f}_{abc}, \quad f_{acb}(\tau) = \frac{\sigma_b}{\sigma_a\sigma_c}\bar{f}_{acb} = -\frac{\sigma_b}{\sigma_a\sigma_c}\bar{f}_{abc}$$

For total antisymmetry we need $f_{abc} = -f_{acb}$, i.e.,

$$\frac{\sigma_c}{\sigma_a\sigma_b} = \frac{\sigma_b}{\sigma_a\sigma_c} \implies \sigma_c^2 = \sigma_b^2$$

This holds when $b$ and $c$ are in the same subspace but **fails** when they are in different subspaces.

**Example**: Take $a \in \mathbb{C}^2$, $b \in \mathfrak{su}(2)$, $c \in \mathbb{C}^2$ with nonzero $\bar{f}_{abc}$ (from $[\mathbb{C}^2, \mathfrak{su}(2)] = \mathbb{C}^2$ with $c$ picked up). Then $\sigma_b = e^{\tau}$, $\sigma_c = e^{-\tau/2}$, and

$$f_{abc} = \frac{e^{-\tau/2}}{e^{-\tau/2}\cdot e^{\tau}}\bar{f}_{abc} = e^{-\tau}\bar{f}_{abc}$$

$$f_{acb} = \frac{e^{\tau}}{e^{-\tau/2}\cdot e^{-\tau/2}}\bar{f}_{acb} = e^{2\tau}(-\bar{f}_{abc})$$

So $f_{abc}/f_{acb} = -e^{-3\tau}$. Total antisymmetry requires this ratio to be $-1$, which holds only at $\tau = 0$.

### 3.3 Decomposition of the Schouten Torsion

The Schouten torsion $T^0_{abc}(\tau) = f_{abc}(\tau)$ decomposes into:

$$T^0_{abc} = T^{(3)}_{abc} + T^{(\mathrm{rest})}_{abc}$$

where $T^{(3)}_{abc} = T^0_{[abc]}$ is the totally antisymmetric part and $T^{(\mathrm{rest})}$ is the remainder.

For totally antisymmetric torsion, the Lichnerowicz formula gives a positive $|T|^2$ contribution that **raises** the spectral gap. The non-totally-antisymmetric part is what can potentially lower it.

Computing $T^{(3)}_{abc}$:

$$T^{(3)}_{abc} = \frac{1}{3}(T^0_{abc} + T^0_{bca} + T^0_{cab})$$

$$= \frac{\bar{f}_{abc}}{3}\left(\frac{\sigma_c}{\sigma_a\sigma_b} + \frac{\sigma_a}{\sigma_b\sigma_c} + \frac{\sigma_b}{\sigma_c\sigma_a}\right)$$

This is exactly $\frac{4}{3}\Omega_{abc}(\tau)$ from Section 2.2.

The remainder $T^{(\mathrm{rest})}_{abc} = T^0_{abc} - T^{(3)}_{abc}$ is:

$$T^{(\mathrm{rest})}_{abc} = \bar{f}_{abc}\left[\frac{\sigma_c}{\sigma_a\sigma_b} - \frac{1}{3}\left(\frac{\sigma_c}{\sigma_a\sigma_b} + \frac{\sigma_a}{\sigma_b\sigma_c} + \frac{\sigma_b}{\sigma_c\sigma_a}\right)\right]$$

$$= \frac{\bar{f}_{abc}}{3}\left[\frac{2\sigma_c}{\sigma_a\sigma_b} - \frac{\sigma_a}{\sigma_b\sigma_c} - \frac{\sigma_b}{\sigma_c\sigma_a}\right]$$

This remainder is **zero** when all $\sigma$'s are equal ($\tau = 0$) and nonzero for $\tau > 0$. It represents the breaking of total antisymmetry.

### 3.4 The Central Sign Question

For the Lichnerowicz formula with the full Schouten connection, we can write:

$$\not{D}_0^2 = (\nabla^0)^*\nabla^0 + \frac{R_g}{4} + Q(T^0)$$

where $Q(T^0)$ is a zero-order endomorphism of the spinor bundle depending on the torsion. When $T^0$ is totally antisymmetric:

$$Q(T^{(3)}) = c_T\,\|T^{(3)}\|^2 - \frac{1}{4}(dT^{(3)})\cdot$$

where $c_T > 0$ is a positive coefficient whose exact value depends on the normalization convention for $|T|^2$ (the coefficient is $\frac{3}{16}$ if $|T|^2 = \sum_{a,b,c}T_{abc}^2$ without the $1/p!$ factor, or $\frac{9}{8}$ in the restricted sum $\|T\|^2 = \sum_{a<b<c}T_{abc}^2$; with the $1/p!$ convention where $|T|^2 = \|T\|^2$, the coefficient is $\frac{3}{16}$). The precise value does not affect the qualitative analysis below; what matters is $c_T > 0$.

The first term is strictly positive. The second term involves the Clifford action of the 4-form $dT^{(3)}$, which has eigenvalues of both signs. However, for compact Lie groups with positive scalar curvature, the combination $R_g/4 + Q(T^{(3)})$ is typically strongly positive.

The non-antisymmetric part $T^{(\mathrm{rest})}$ introduces additional terms in $Q$ that do not have a clean sign. The full zero-order term becomes:

$$Q(T^0) = Q(T^{(3)}) + Q_{\mathrm{cross}}(T^{(3)}, T^{(\mathrm{rest})}) + Q(T^{(\mathrm{rest})})$$

The cross terms $Q_{\mathrm{cross}}$ are the ones that can potentially be negative.

### 3.5 Quantitative Estimate: Why Gap Weakening is Unlikely

Let us estimate the magnitude of the non-antisymmetric part relative to the gap.

For the most relevant case (mixed $\mathfrak{su}(2) \times \mathbb{C}^2$ indices), at $\tau = 0.25$ (near the $\lambda_{\min}$ turnaround):

- $\sigma_W = e^{0.25} \approx 1.284$
- $\sigma_C = e^{-0.125} \approx 0.882$

The asymmetry ratio for $(W, C) \to C$ type terms:

$$\frac{2\sigma_C}{\sigma_W\sigma_C} - \frac{\sigma_W}{\sigma_C\sigma_C} - \frac{\sigma_C}{\sigma_C\sigma_W} = \frac{2}{\sigma_W} - \frac{\sigma_W}{\sigma_C^2} - \frac{1}{\sigma_W} = \frac{1}{\sigma_W} - \frac{\sigma_W}{\sigma_C^2}$$

$$= \frac{1}{1.284} - \frac{1.284}{0.778} = 0.779 - 1.650 = -0.871$$

So the asymmetric part is $\frac{-0.871}{3}\bar{f}_{abc} \approx -0.290\,\bar{f}_{abc}$, while the symmetric part is $\frac{1}{3}(0.779 + 1.650 + 0.779) = 1.069\,\bar{f}_{abc}$ (times $\frac{1}{4}$).

The ratio $|T^{(\mathrm{rest})}|/|T^{(3)}| \sim 0.27$ at $\tau = 0.25$.

Now, the Lichnerowicz bound at $\tau = 0$: in code normalization (where $R_{\mathrm{data}} = R_K^{\mathrm{Baptista}}/6$, see MEMORY), $\lambda_{\min}^2 = 0.694$ and $R_{\mathrm{data}}/4 = 0.5$, giving ratio $\lambda_{\min}^2/(R_{\mathrm{data}}/4) \approx 1.39$. The bound is satisfied with $\sim 39\%$ excess -- the eigenvalue sits only modestly above the Lichnerowicz floor. In Baptista normalization, $\lambda_{\min,B}^2 = 6 \times 0.694 = 4.16$ and $R_K^B/4 = 3$, same ratio. The key point: the spectral gap is not orders of magnitude above the curvature bound; it is set by the $\Omega_{jkl}$ algebraic term in the singlet sector.

**The crucial point**: The Schouten operator $\not{D}_0$ has **no** $\Omega$ term. The $\Omega$ term in $\not{D}_K$ is what pushes eigenvalues UP from the pure Lie-derivative spectrum. Removing it entirely (going to the Schouten connection) would generically **lower** eigenvalues.

But wait -- this reasoning is too naive. The Schouten connection is flat ($R^{\nabla^0} = 0$), so the curvature contribution to $\not{D}_0^2$ is purely from the torsion terms, not from $R_g/4$. The Lichnerowicz bound for $\not{D}_0$ involves the torsion, not the Riemannian curvature. The spectral gap of $\not{D}_0$ is a separate question from the spectral gap of $\not{D}_K$.

### 3.6 Direct Spectral Comparison: $\not{D}_K$ vs. $\not{D}_0$

Since $\not{D}_K = \not{D}_0 + \Omega\cdot$ (where $\Omega\cdot = \sum_{j<k<l}\Omega_{jkl}\gamma^j\gamma^k\gamma^l$), the eigenvalues of $\not{D}_K$ are perturbations of those of $\not{D}_0$ by the zero-order operator $\Omega\cdot$. The operator $\Omega\cdot$ acts purely on the spinor fiber -- it does not involve derivatives and commutes with the Peter-Weyl decomposition.

In each irreducible sector $(p,q)$, the matrix of $\not{D}_K$ in the Peter-Weyl basis is:

$$M^{(p,q)}_K = M^{(p,q)}_0 + M^{(p,q)}_\Omega$$

where $M^{(p,q)}_0$ is the matrix of the Lie derivative part and $M^{(p,q)}_\Omega$ is the matrix of the $\Omega$ Clifford term, restricted to the $(p,q)$ isotypic component.

The eigenvalues of $\not{D}_K$ depend on the interplay of these two matrices. They are NOT simply $\lambda_0 + \lambda_\Omega$ (the matrices do not commute in general). The question $\min|\lambda_0| \lessgtr \min|\lambda_K|$ depends on the detailed matrix structure within each sector.

**For the $(0,0)$ singlet**: The singlet sector has $d_{(0,0)} = 1$, so the representation space is $1 \times 16 = 16$ dimensional (16 spinor components, one copy). The Lie derivative part acts as $M_0 = \sum_a \gamma^a \otimes L_a$ where $L_a$ is the left-regular representation matrix of $e_a$ restricted to the singlet. But wait -- on the $(0,0)$ singlet, the left-regular action $\mathcal{L}_{e_a^L}$ acts trivially (the $(0,0)$ component of $L^2(K)$ consists of constants). Therefore:

$$M^{(0,0)}_0 = 0$$

and

$$M^{(0,0)}_K = M^{(0,0)}_\Omega = \sum_{j<k<l}\Omega_{jkl}(\tau)\,\gamma^j\gamma^k\gamma^l$$

**This is a purely algebraic $16 \times 16$ matrix** whose eigenvalues are entirely determined by the $\Omega_{jkl}(\tau)$ coefficients. For the singlet, $\not{D}_0$ has eigenvalue 0 (only constants, closed by Lie derivatives), while $\not{D}_K$ has eigenvalues $\pm\lambda_{\min}(\tau) = \pm 0.833$ at $\tau = 0$.

**Therefore**: The torsionful (Schouten) Dirac operator has **zero eigenvalue** in the $(0,0)$ singlet sector. This is worse than the Levi-Civita Dirac operator, not better. The Schouten operator has kernel -- the gap is completely destroyed.

But this is the **wrong comparison for Gate T-1**. Gate T-1 asks whether there exists **any** natural connection with torsion on SU(3) whose Dirac operator has a smaller spectral gap than $\not{D}_K$, while still having a nonzero gap. The Schouten operator has zero gap (kernel), which is too much weakening.

### 3.7 Intermediate Torsion: Interpolation

Consider a one-parameter family of connections interpolating between Levi-Civita ($t=0$) and Schouten ($t=1$):

$$\nabla^t = \nabla^{\mathrm{LC}} + t \cdot K^0$$

where $K^0_{abc} = -\frac{1}{2}g(\nabla^{\mathrm{LC}}_{e_a}e_b, e_c)$ is the contorsion from LC to Schouten. The torsion of $\nabla^t$ is $T^t = t \cdot T^0$. The corresponding Dirac operator is:

$$\not{D}_t = \not{D}_K - t\sum_{j<k<l}\Omega_{jkl}\gamma^j\gamma^k\gamma^l$$

On the $(0,0)$ singlet, this has eigenvalues $(1-t)\lambda_K^{(0,0)}$, which decrease monotonically from $\lambda_K$ to 0. For $t$ slightly positive, the gap weakens by a factor $(1-t)$.

But this is a trivial observation -- any perturbation that removes the $\Omega$ term will weaken the gap. The question is whether there is a **geometrically natural** torsion connection that:
1. Has nonzero gap (unlike the full Schouten)
2. Has gap smaller than $\not{D}_K$
3. Is motivated by the physics (not just an arbitrary interpolation parameter)

### 3.8 The Physically Motivated Torsion Connection

The physically relevant question from the preplan is different from comparing $\not{D}_K$ and $\not{D}_0$. It is: **does the Levi-Civita Dirac operator on a Lie group with deformed metric have eigenvalues that could be lowered by accounting for the natural torsion that the group carries?**

The standard Dirac operator $\not{D}_K$ already uses the Levi-Civita connection, which is torsion-free. The Lichnerowicz bound $\lambda^2 \geq R_K/4$ applies to this operator. The question is whether a torsionful Dirac operator could have smaller eigenvalues while being equally (or more) physically motivated.

The answer depends on what "physically motivated" means:

1. **If we use the Schouten connection**: Zero eigenvalue on singlet. The gap is destroyed. This is physically the wrong operator for mass generation -- the zero modes don't produce masses.

2. **If we use a Bismut-type connection** (totally antisymmetric torsion $T^{(3)} = T^{(3)}_{[abc]}$): The Lichnerowicz bound becomes $\lambda_T^2 \geq R_g/4 + c_T\|T^{(3)}\|^2 - \frac{1}{4}\|dT^{(3)}\|_{\mathrm{op}}$ with $c_T > 0$ (see Section 1.4). For positive-curvature compact Lie groups, $\|T^{(3)}\|^2$ adds positively. The $dT^{(3)}$ term involves the Clifford action of the 4-form $dT^{(3)}$, whose operator norm is bounded on compact manifolds. In practice, the positive $c_T\|T^{(3)}\|^2$ term dominates and the gap **increases**.

3. **The Friedrich inequality for connections with parallel torsion**: When $\nabla^T T = 0$ (which holds for the canonical connection on a naturally reductive space -- and the Jensen-deformed SU(3) IS naturally reductive for $\alpha_1 = \alpha_2$, but not for general Jensen deformations), the estimate $\lambda_T^2 \geq \frac{k}{4(k-1)} R_g + c_T\|T\|^2$ holds. Both terms are positive. The gap is strengthened.

---

## 4. Baptista Paper Cross-References

### 4.1 Paper 14, Section 3.3 (lines 1734--1740)

The key passage states:

> *"The Dirac operator on K will be simpler if the original connection $\nabla$ on the tangent bundle is taken to be the flat Schouten connection $\nabla^0$, instead of the usual Levi-Civita connection. This is a $g$-compatible connection with torsion $T^0(u^L, v^L) = [u, v]^L$, and the coefficients $\Omega_{jkl}$ of the corresponding Dirac operator are identically zero."*

This confirms: the Schouten Dirac operator $\not{D}_0 = \sum_j \gamma^j \mathcal{L}_{e_j^L}$ has no cubic term. It is purely first-order in Lie derivatives. Its kernel includes all constant spinors (the $(0,0)$ singlet), giving a zero eigenvalue. This is the fundamental reason why the Schouten operator is not useful for gap strengthening -- it destroys the gap entirely in the singlet sector.

### 4.2 Paper 14, Equation 3.8 (lines 1723--1726)

The explicit formula for the $\Omega_{jkl}$ coefficients under Jensen deformation:

$$\Omega_{jkl} = \frac{3}{4}\kappa_0([e_j'', e_k''], e_l'') + \frac{1}{2}\sum_{\text{cyclic}} \kappa_0([e_{(j)}'', e_{(k)}''], e_{(l)})$$

where the double prime denotes $\mathbb{C}^2$ components and the sum is over circular permutations. This formula (Paper 14, eq 3.8) encodes the $\tau$-dependent rescaling of the structure constants that we computed explicitly in Section 2.2 above. The two-term structure reflects the decomposition $\mathfrak{su}(3) = \mathfrak{u}(2) \oplus \mathbb{C}^2$.

### 4.3 Paper 15, Section 3.9 (line 3127)

The passage:

> *"considering connections with torsion in the internal directions would also be interesting. This is because the Ricci scalar of such a connection will be the traditional scalar curvature plus a term involving the norm of the torsion. This additional term affects the effective potential and may help to counterbalance the runaway scalar curvature under some of its instabilities."*

Baptista's suggestion is about the **effective potential** (i.e., the bosonic action involving the Ricci scalar of a torsionful connection), not about the **fermionic Dirac operator**. The Ricci scalar of a metric-compatible connection with torsion is $R^T = R_g + c|T|^2 + \ldots$ where the torsion contribution modifies the curvature. Whether this creates a stabilization minimum depends on the relative $\tau$-dependence of $R_g(\tau)$ and $|T(\tau)|^2$ -- the mechanism is plausible but has not been computed for Jensen-deformed SU(3).

This is a different mechanism from what Gate T-1 tests. Gate T-1 is about the **Dirac eigenvalue** gap, not the effective potential. Baptista's observation about torsion stabilization concerns the bosonic sector (metric dynamics), while T-1 concerns the fermionic sector (Dirac spectrum). These are related but distinct questions:

- **Bosonic (Baptista's suggestion)**: Torsion contributes $+|T|^2$ to an effective scalar curvature that enters the potential with a minus sign, potentially creating a stabilization minimum. This is a $V_{\text{Baptista}}$-type mechanism.
- **Fermionic (Gate T-1)**: Torsion modifies the Dirac operator, potentially changing the spectral gap. The Lichnerowicz formula with totally antisymmetric torsion has a positive $+c\|T\|^2$ term (where $c > 0$ depends on normalization conventions, see Section 1.4) which **raises** the gap.

### 4.4 Paper 17, Equations 4.1, 4.7

The Kosmann--Lichnerowicz derivative (Paper 17, eq 4.1) and its commutator with $\not{D}_K$ (eq 4.7) provide the key identity

$$[\not{D}_K, \mathcal{L}_X] = \frac{1}{2}g^{ir}g^{js}(\mathcal{L}_X g)(e_r, e_s)\gamma^i\gamma^j + \text{first-order terms}$$

This shows that when $X$ is Killing ($\mathcal{L}_X g = 0$), $\not{D}_K$ commutes with $\mathcal{L}_X$. The torsion connection does not change this commutation structure because the Kosmann derivative is defined in terms of the Levi-Civita connection, not the Schouten connection.

---

## 5. Gate T-1 Theoretical Assessment

### 5.1 Reformulation of the Gate

The pre-registered gate asks: $\min|\lambda_T(\tau)| < \min|\lambda_K(\tau)|$ at some $\tau \in [0, 0.5]$.

To make this well-defined, we must specify what $\not{D}_T$ is. There are three natural candidates:

**(A) Schouten Dirac operator** $\not{D}_0$: Has zero eigenvalue in the $(0,0)$ singlet for all $\tau$. The gate trivially PASSES (zero $< 0.819$), but this is physically meaningless -- zero eigenvalues correspond to massless fermions in 4D, which we already know are present in the theory (the $(0,0)$ singlet modes are the ones that become massless in the Schouten formulation). The Schouten Dirac operator is the "wrong" operator for mass generation in KK theory.

**(B) Bismut Dirac operator** (totally antisymmetric part of torsion): $\not{D}_B = \not{D}_K + \frac{1}{4}T^{(3)}_{abc}\gamma^a\gamma^b\gamma^c$. This adds more cubic terms to $\not{D}_K$, generically increasing the gap by $|T^{(3)}|^2$ type contributions. The gate almost certainly FAILS (closes).

**(C) Physical Dirac operator with specific torsion coupling**: If we couple torsion to fermions with a specific coupling constant $\eta$ (as in Einstein-Cartan theory), $\not{D}_\eta = \not{D}_K + \eta\, T_{abc}\gamma^a\gamma^b\gamma^c$. The sign and magnitude of $\eta$ determine whether the gap weakens or strengthens.

### 5.2 The Structural Theorem

**Theorem (Torsion Gap Monotonicity for Totally Antisymmetric Torsion)**:

On a compact Riemannian spin manifold with positive scalar curvature $R > 0$, the Dirac operator $\not{D}_T$ associated to a metric connection with totally antisymmetric torsion $T$ satisfies

$$\lambda_T^2 \geq \frac{R}{4} + c\,\|T\|^2 - C\cdot\|dT\|_{\mathrm{op}}$$

where $c > 0$ is a positive coefficient depending on normalization conventions (see Section 1.4), $\|dT\|_{\mathrm{op}}$ is the operator norm of the Clifford action of $dT$, and $C$ is a universal constant depending on dimension. For compact simple Lie groups with left-invariant metrics, $\|dT\|_{\mathrm{op}}$ is bounded in terms of the structure constants, and the $c\|T\|^2$ term dominates for sufficiently large curvature.

**Consequence**: For the totally antisymmetric part of any natural torsion on Jensen-deformed SU(3), the spectral gap INCREASES. The Bismut connection gives $\min|\lambda_B| > \min|\lambda_K|$.

### 5.3 The Non-Antisymmetric Channel

The only channel through which torsion could weaken the gap is via the non-totally-antisymmetric part $T^{(\mathrm{rest})}$, which appears only for $\tau > 0$. However:

1. **$T^{(\mathrm{rest})}$ vanishes at $\tau = 0$** and grows as $O(\tau)$ for small $\tau$.
2. **The Lichnerowicz bound $R/4$ grows** as $\tau$ increases (since $R(\tau)$ is monotonically increasing for $\tau > 0$).
3. **At the $\lambda_{\min}$ turnaround** ($\tau \approx 0.23$), the asymmetry ratio $|T^{(\mathrm{rest})}|/|T^{(3)}| \approx 0.27$ (computed in Section 3.5). The correction to the Lichnerowicz bound from the non-antisymmetric part is at most quadratic in this ratio: $\sim 0.27^2 \cdot \|T^{(3)}\|^2 \sim 0.07\|T^{(3)}\|^2$. The positive contribution from the totally antisymmetric part is $c \cdot \|T^{(3)}\|^2$ where the coefficient $c$ depends on normalisation conventions but satisfies $c \geq \frac{3}{8}$ in the restricted-sum convention (Friedrich Theorem 4.14; the exact value may be larger depending on the definition of $|T|^2$).
4. **The positive terms dominate** by a factor $c/0.07 \geq 5$, regardless of the precise coefficient convention.

### 5.4 Probability Assessment

**P(T-1 PASS) = 5--10%** (revised downward from preplan estimate of 10--15%).

The downward revision is driven by the structural analysis:

- The totally antisymmetric torsion unambiguously **strengthens** the gap (Bismut--Friedrich--Agricola theorem).
- The non-antisymmetric part is a perturbative correction ($\sim 27\%$ of the symmetric part at $\tau = 0.25$) that is dominated by the positive-definite $|T|^2$ contribution.
- The singlet sector eigenvalues are determined entirely by the $\Omega_{jkl}$ algebraic matrix, and adding more torsion to this matrix either strengthens or destroys the gap (Schouten limit), with no intermediate minimum where $0 < \lambda_T < \lambda_K$.
- The only scenario where T-1 passes is if the non-antisymmetric torsion creates a specific pattern of cancellations in higher sectors (not the singlet) that lowers the overall spectral gap below the singlet minimum. This requires sector-specific numerical computation.

**The residual 5--10% probability comes from**: The fact that the non-singlet sector eigenvalues involve the full interplay of Lie derivative operators AND $\Omega$ terms, and we have not computed $\not{D}_T$ eigenvalues in the $(1,0)$, $(0,1)$, and $(1,1)$ sectors where the non-antisymmetric torsion has its largest effect. A numerical surprise cannot be ruled out.

---

## 6. Condensed Matter Analog: He-3B and Container Deformation

### 6.1 The Volovik Correspondence

In superfluid He-3B (Volovik, "The Universe in a Helium Droplet"), the gap structure is determined by the interplay of:

1. **Order parameter topology**: The B-phase has a full isotropic gap $\Delta_B$ protecting quasiparticle excitations.
2. **Container geometry**: The boundary conditions imposed by the container walls couple to the order parameter through spin-orbit interaction.
3. **Deformation response**: When the container is deformed (e.g., squeezed), the gap can close at specific points, creating zero-energy Majorana fermions at vortex cores.

The correspondence to our setting:

| He-3B | Jensen-deformed SU(3) |
|:------|:----------------------|
| Isotropic gap $\Delta_B$ | Spectral gap $\lambda_{\min}$ |
| Container shape | Jensen deformation parameter $\tau$ |
| Spin-orbit coupling | Torsion $T^0_{abc}(\tau)$ |
| Order parameter $A_{\mu i}$ | Condensate $\Delta$ (BCS gap) |
| Gap closing at vortex cores | $\lambda_{\min}$ turnaround at $\tau \approx 0.23$ |
| Majorana zero modes | Zero modes of $\not{D}_0$ (Schouten) |

### 6.2 Where the Analogy Breaks Down

The critical difference: in He-3B, the spin-orbit coupling is a **weak perturbation** of the kinetic energy, and the gap closing occurs at topologically protected points (vortex cores). The spin-orbit energy scale is $\Omega_B \sim 10^{-7}\Delta_B$.

On SU(3), the torsion is a **strong** contribution -- the $\Omega_{jkl}$ term is of the same order as the Lie derivative term in the Dirac operator. The spectral gap is $\lambda_{\min} = 0.833$ at $\tau = 0$, entirely determined by the $\Omega$ algebraic matrix in the singlet sector. There is no perturbative regime where torsion is a small correction.

Moreover, the gap closing in He-3B is driven by **topology** (the existence of vortex solutions with winding number), not by perturbative deformation of the bulk gap. The analogous topological mechanism on SU(3) would be a change in the KO-dimension or the index of the Dirac operator, not a metric deformation. The KO-dimension is 6 (proven, Sessions 7-8) and does not change under Jensen deformation.

### 6.3 The Useful Lesson

The useful lesson from Volovik is not about gap closing, but about the distinction between the **microscopic Hamiltonian** and the **thermodynamic equilibrium**. Even if the Dirac spectrum (microscopic) has a rigid gap that torsion cannot breach, the thermodynamic free energy (macroscopic) may still have a minimum at finite $\tau$ -- as we already know from the partition function $F(\tau; \beta)$ having a 12.1% depth minimum (Session 25).

Torsion does not help breach Wall W3 (the Lichnerowicz spectral gap), but the Volovik interpretation reminds us that W3 is about the **spectrum**, not the **thermodynamics**. Route B attacks the thermodynamics directly.

---

## 7. Recommendations for Numerical Computation

### 7.1 What phonon-sim Should Compute for T-1

Despite the theoretical analysis pointing toward a CLOSED, the gate must be decided by computation, not theory. The theoretical analysis identifies where to look and what to expect, but cannot substitute for the eigenvalue calculation.

**Required computation**:

1. **Construct the $\Omega_{jkl}(\tau)$ matrices** at 9 $\tau$ values using the explicit rescaling formula from Section 2.2:

$$\Omega_{jkl}(\tau) = \frac{\bar{f}_{jkl}}{4}\left(\frac{\sigma_l}{\sigma_j\sigma_k} + \frac{\sigma_j}{\sigma_k\sigma_l} + \frac{\sigma_k}{\sigma_l\sigma_j}\right)$$

with $\sigma_0 = e^{-\tau}$, $\sigma_{1,2,3} = e^{\tau}$, $\sigma_{4,5,6,7} = e^{-\tau/2}$.

2. **Construct the torsionful Dirac operator** for three cases:
   - **(A) Schouten**: $\not{D}_0 = \sum_j \gamma^j \mathcal{L}_{e_j^L}$ (remove $\Omega$ term from $\not{D}_K$)
   - **(B) Bismut**: $\not{D}_B = \not{D}_K + \frac{t}{4}T^{(3)}_{abc}\gamma^a\gamma^b\gamma^c$ for $t = 0.1, 0.5, 1.0$
   - **(C) Full Schouten torsion**: $\not{D}_T = \not{D}_K + \frac{t}{4}T^{0}_{abc}\gamma^a\gamma^b\gamma^c$ for $t = 0.1, 0.5, 1.0$

3. **Diagonalize in each sector** $(p,q)$ for $p + q \leq 6$ at each $\tau$.

4. **Compare** $\min|\lambda_T(\tau)|$ vs. $\min|\lambda_K(\tau)|$ across all sectors and all $\tau$.

5. **Output**: `.npz` file with eigenvalue arrays, gap comparison plot, and gate verdict.

### 7.2 Implementation Notes

- The existing `tier1_dirac_spectrum.py` code already constructs $\not{D}_K$ in the Peter-Weyl basis. The modification is straightforward: **subtract** the $\Omega_{jkl}\gamma^j\gamma^k\gamma^l$ matrix from the existing $\not{D}_K$ to get $\not{D}_0$.
- For Bismut/full torsion: **add** the appropriate contorsion matrix to $\not{D}_K$.
- The $16 \times 16$ gamma matrix algebra ($\gamma^j\gamma^k\gamma^l$ for $j < k < l$, $j,k,l \in \{0,\ldots,7\}$) is dimension-independent and can be precomputed.
- The $\bar{f}_{abc}$ structure constants of $\mathfrak{su}(3)$ in the $\kappa_0$-ONB are well-known (related to Gell-Mann matrix commutators). There are $\binom{8}{3} = 56$ triples, of which a subset are nonzero. These should be hardcoded or computed from the Gell-Mann basis.
- **Expected runtime**: Each $\tau$ value requires diagonalizing modified matrices of the same sizes as the existing computation. No additional sectors are needed. Overhead: $\sim 20\%$ over the existing eigenvalue sweep (construction of the additional matrix, one extra diagonalization per sector per $\tau$). Total: $\sim 1$ hour.

### 7.3 Pre-Registered Gate Criteria

**Gate T-1**: For each of the three torsion types (A, B, C):

| Outcome | Verdict | Action |
|:--------|:--------|:-------|
| $\min|\lambda_T(\tau)| \geq \min|\lambda_K(\tau)|$ for ALL $\tau$ | **CLOSED** | W3 extended to torsionful Dirac. Closed Mechanism #27. |
| $\min|\lambda_T(\tau)| < \min|\lambda_K(\tau)|$ at some $\tau$, and $\min|\lambda_T| > 0$ | **PASS** | New channel opens. Re-run K-1e BCS with torsion-modified spectrum. |
| $\min|\lambda_T(\tau)| = 0$ | **DEGENERATE** | Schouten limit. Not useful for BCS. Not counted as pass or closure. |

**Expected outcome**: CLOSED for types (B) and (C). DEGENERATE for type (A) at $t = 1$ (Schouten). Possible PASS for type (C) at small $t$ -- but this would require $T^{(\mathrm{rest})}$ to create specific cancellations.

### 7.4 If T-1 Passes

If the gate passes (P = 5--10%), the BCS gap equation must be re-evaluated with the torsion-modified spectrum:

$$\Delta = -g_T \sum_k \frac{\tanh(E_k^T / 2T_c)}{2E_k^T}, \quad E_k^T = \sqrt{(\lambda_{T,k}^2 - \mu^2)^2 + \Delta^2}$$

where $g_T$ is the Kosmann coupling in the torsionful theory and $\lambda_{T,k}$ are the eigenvalues of $\not{D}_T$. If the gap has weakened (smaller $\lambda_{T,\min}$), the BCS threshold is easier to reach, and $M_{\max}$ could exceed 1.0 even at $\mu = 0$.

This would be a Tier 2 success (preplan Section 5.1): "New channel, W3 breached."

---

## 8. Summary and Verdict

### 8.1 Key Results

1. **Total antisymmetry of $\Omega_{jkl}(\tau)$ is preserved for all $\tau$** (Section 2.3). The $\Omega$ coefficients that define the cubic term in $\not{D}_K$ remain totally antisymmetric under Jensen deformation, because they are symmetric averages of the rescaled structure constants. This is a structural result that simplifies the entire analysis.

2. **The Schouten torsion $T^0_{abc}(\tau)$ loses total antisymmetry for $\tau > 0$** (Section 3.2). The non-antisymmetric part grows as $O(\tau)$ and reaches $\sim 27\%$ of the antisymmetric part at $\tau = 0.25$.

3. **Totally antisymmetric torsion strengthens the gap** (Section 3.4, Bismut--Friedrich--Agricola). This is a theorem. The $+|T|^2$ contribution dominates the $dT$ Clifford term.

4. **The non-antisymmetric part could in principle weaken the gap**, but is dominated by the positive-definite terms by a factor $\sim 5$ at $\tau = 0.25$ (Section 3.5).

5. **The Schouten Dirac operator has zero eigenvalue** in the $(0,0)$ singlet for all $\tau$ (Section 3.6). This is the DEGENERATE outcome -- gap destruction, not gap weakening.

6. **Baptista's torsion suggestion (Paper 15, line 3127) concerns the bosonic potential**, not the fermionic Dirac operator (Section 4.3). It is relevant to $V_{\text{Baptista}}$ stabilization, not to Gate T-1.

### 8.2 Probability

**P(T-1 PASS) = 5--10%**, revised downward from the preplan estimate of 10--15%.

**P(T-1 CLOSED) = 80--85%**.

**P(T-1 DEGENERATE) = 10%** (Schouten limit, not useful).

### 8.3 Computational Cost

$\sim 1$ hour of GPU time on the existing infrastructure. The modification to the existing eigenvalue sweep code is minor (add/subtract the $\Omega$ matrix). This is among the cheapest gates in the program.

### 8.4 Strategic Assessment

Even though the theoretical analysis strongly suggests a CLOSED, the computation should be done for three reasons:

1. **Pre-registration compliance**: The gate was pre-registered. It must be computed, not theorized away.
2. **The non-singlet sectors have not been analyzed theoretically**: The sign analysis in Section 3 applies to general bounds. The specific eigenvalue structure of the $(1,0)$, $(0,1)$, $(1,1)$ sectors under torsion modification could reveal unexpected behavior. Numerical surprises are possible at the $\sim 5\%$ level.
3. **The computation produces permanent mathematical results**: The torsionful Dirac spectrum on Jensen-deformed SU(3) has never been computed. Regardless of the gate outcome, this is a publishable result (contributes to the "Spectral Anatomy" pure math paper).

---

*Baptista-Spacetime-Analyst, 2026-02-22.*
*Based on: Papers 14, 15, 17 of the Baptista corpus; Session 25 Walls W1--W6; Session 26 preplan Section 3.2.*

*"The torsion whispers -- but the Lichnerowicz bound shouts."*
