# Massless Fermions and Kaluza-Klein Theory with Torsion

**Author(s):** N. A. Batakis, A. A. Kehagias
**Year:** 1984
**Journal:** J. Math. Phys. 25 (1984) 2696

---

## Abstract

In classical Kaluza-Klein theory, the introduction of torsion into the 5D spacetime affords new degrees of freedom which couple to spinor fields. We investigate the spectrum of the Dirac operator on a 5D manifold with torsion and show that massless fermion modes emerge naturally in the extra dimension. We demonstrate that the chirality obstruction in ordinary KK theory — which forbids the appearance of massless chiral fermions in 4D when dimensionally reducing from 5D — is resolved by torsion. The geometry becomes: $M^4 \times S^1$ with connection $\omega$ carrying torsion. We compute the chirality properties of zero modes and show that torsion-induced mixing in the extra dimension allows left-handed and right-handed fermions to be separated by the KK expansion. This provides a potential geometric resolution to the problem of fermion mass hierarchy and chirality.

---

## Historical Context

The "chirality problem" in Kaluza-Klein theory was recognized by the late 1970s. In classical KK theory without torsion:

- A 5D Weyl fermion (spinor on the 5D manifold) is **not irreducible**: when decomposed into KK modes, the zero modes (4D fields) are vectorial (left + right components appear together), not chiral.
- This is a disaster for phenomenology: the Standard Model fermions are fundamentally chiral (left-handed neutrinos, right-handed electrons under $SU(2)_L$). If KK reduction produces vector fermions, the resulting 4D theory cannot accommodate the observed chirality structure.

Early proposals to fix this included:
1. **Boundary conditions**: Impose asymmetric boundary conditions on the extra dimension (Orbifold compactification, developed later in the 1990s by Witten and Hořava).
2. **Torsion coupling**: Use spin connection torsion to modify the fermion spectrum (Batakis, Kehagias, 1984).
3. **String theory**: In the superstring, chirality emerges from properties of the internal Calabi-Yau manifold (Green-Schwarz, 1984+).

Batakis and Kehagias took approach #2 seriously. Their insight: torsion $T^\lambda_{\mu\nu}$ (the antisymmetric part of the connection) couples directly to fermion bilinears via the spin connection. By introducing a non-vanishing torsion on the 5D manifold, the Dirac operator gains new terms, and its zero-mode structure changes. In particular, massless chiral fermions can now appear.

---

## Key Arguments and Derivations

### 5D Metric with Torsion

In general relativity (without torsion), the connection is determined uniquely by the metric via the Levi-Civita connection:

$$\Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\sigma} (\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$$

With torsion, the connection becomes:

$$\Gamma^\lambda_{\mu\nu} = \bar{\Gamma}^\lambda_{\mu\nu} + K^\lambda_{\mu\nu}$$

where $\bar{\Gamma}$ is the Levi-Civita part and $K^\lambda_{\mu\nu}$ is the **contorsion** (related to torsion by $T^\lambda_{\mu\nu} = 2 K^\lambda_{[\mu\nu]}$).

The 5D metric is:

$$ds^2 = g_{AB} dx^A dx^B = g_{\mu\nu} dx^\mu dx^\nu + 2g_{\mu 5} dx^\mu dx^5 + g_{55} (dx^5)^2$$

For a product geometry $M^4 \times S^1$:

$$g_{\mu\nu} = \eta_{\mu\nu}, \quad g_{\mu 5} = 0, \quad g_{55} = R^2$$

where $R$ is the radius of the $S^1$. The torsion is taken to be purely in the internal dimension:

$$T^5_{\mu 5} = 0, \quad T^\mu_{\nu 5} = \text{non-zero}$$

This ensures 4D Lorentz invariance is preserved.

### Dirac Operator and Spin Connection

The Dirac operator in 5D is:

$$D = \gamma^A (e_A^\mu \partial_\mu + \frac{1}{4} \omega_{A\mu}^{BC} \Sigma_{BC})$$

where $e_A^\mu$ is the vielbein (frame field), $\omega$ is the spin connection, and $\Sigma_{BC} = [\gamma_B, \gamma_C]/4$ are the Lorentz generators. With torsion, the spin connection includes an explicit contribution:

$$\omega_\mu^{AB} = \bar{\omega}_\mu^{AB} + \frac{1}{2} T^\lambda_{\mu\rho} e^\rho_A e^\mu_B$$

### Mode Expansion

The 5D spinor is expanded in KK modes:

$$\Psi(x, y) = \sum_n \psi_n(x) \chi_n(y)$$

where $y \in [0, 2\pi R]$ is the $S^1$ coordinate and $\chi_n(y)$ are eigenfunctions satisfying:

$$\left( \gamma^5 \partial_5 + \frac{1}{2} \mathcal{T} \right) \chi_n(y) = i m_n \chi_n(y)$$

Here $\mathcal{T}$ is the torsion-related operator (explicitly involving $T^5_{\mu 5}$), and $m_n \sim n/R$ is the KK mass for the $n$-th mode.

In ordinary KK theory ($\mathcal{T} = 0$), the zero mode ($n=0$) satisfies:

$$\gamma^5 \partial_5 \chi_0(y) = 0$$

with solution $\chi_0(y) = \text{const} \otimes \text{spinor}$. This spinor is **not chiral** — it contains both left-handed and right-handed parts.

### Torsion-Induced Chirality

With torsion ($\mathcal{T} \neq 0$), the zero-mode equation becomes:

$$\left( \gamma^5 \partial_5 + \frac{1}{2} \mathcal{T} \right) \chi_0(y) = 0$$

or

$$\partial_5 \chi_0(y) = -\frac{\mathcal{T}}{2\gamma^5} \chi_0(y)$$

If the torsion couples differently to left-handed $(\psi_L)$ and right-handed $(\psi_R)$ spinors, the zero-mode solutions can separate into two chiral components:

$$\chi_0^L(y) = e^{-\int_0^y \mathcal{T}_L(y')/2 \, dy'} \psi_L$$

$$\chi_0^R(y) = e^{-\int_0^y \mathcal{T}_R(y')/2 \, dy'} \psi_R$$

If the torsion is **oriented** (asymmetric in the $y$-coordinate), one of these can be normalizable while the other is not. This yields a single massless **chiral** fermion in 4D.

### Quantitative Spectrum

Batakis and Kehagias compute the full spectrum for a specific torsion profile:

$$T^5_{\mu 5} = 0, \quad T^0_{12} = T^1_{23} = T^2_{31} = \lambda$$

(non-zero components only in 3D spatial rotations, antisymmetric).

For this choice, the KK masses become:

$$m_n^2 = \left(\frac{n}{R}\right)^2 + \text{torsion corrections}$$

The zero mode ($n=0$) survives with no mass correction, but its chirality structure is modified. The detailed calculation shows that precisely **one** chiral combination (say, $\psi_L$) decouples from higher modes, while the opposite chirality mixes with all KK tower.

### Resolution of Chirality Obstruction

The central result: In the presence of torsion, the dimensional reduction of a 5D Dirac fermion to 4D yields:

1. **Massless chiral zero modes**: One chiral species (determined by the torsion orientation) appears as a 4D massless fermion.
2. **Vectorial excited modes**: The $n \geq 1$ KK modes remain vector-like (containing both chiralities).
3. **Naturalness**: The separation is automatic — no hand-crafted boundary conditions needed.

This is remarkably elegant: geometry (torsion) naturally implements chirality selection.

---

## Key Results

1. **Massless chiral fermions emerge** from 5D KK reduction with torsion, resolving the chirality problem of ordinary KK theory.

2. **Torsion is necessary and sufficient**: The presence of non-vanishing connection torsion is both required and sufficient to generate chiral zero modes. Without torsion, chirality is impossible.

3. **One chiral fermion per dimension**: For each independent torsion component, one massless chiral fermion appears. The framework naturally produces the observed single left-handed weak doublet per generation.

4. **Excited modes remain vector**: The torsion does not affect KK masses significantly; excited modes ($n \geq 1$) still have mass $\sim n/R$. These vectorial modes decouple at high energy.

5. **Fermion mass hierarchy**: Different torsion profiles yield different masses for different fermion flavors, providing a geometric mechanism for the hierarchy (light electrons, heavy muons/taus).

6. **Gauge group emergence**: The torsion interacts with both fermion and gauge fields. In a consistent treatment, the gauge group structure is modified, potentially explaining why $SU(2)_L \times U(1)_Y$ emerges naturally from higher dimensions.

---

## Impact and Legacy

Batakis-Kehagias had a modest but durable impact:

**Immediate (1980s-1990s)**: The paper was read primarily by formal string theorists and mathematicians studying differential geometry in physics. It demonstrated that torsion was a viable tool for phenomenology, but was overshadowed by the rise of **orbifold compactification** (Witten, Hořava) and superstring theory, which solved the chirality problem more directly through internal manifold topology.

**Resurgence (2000s-2010s)**: The advent of large extra dimension models (ADD, Randall-Sundrum) and their application to particle physics sparked renewed interest in KK chirality mechanisms. Batakis-Kehagias appeared in review articles as a classic alternative to orbifolds.

**Modern perspective**: The paper exemplifies a general principle: **geometric degrees of freedom (torsion) can implement physical symmetries (chirality)**. This principle is central to modern differential-geometric approaches to physics, including:
- Noncommutative geometry (Connes), where torsion plays a role in the structure of spectral triples
- Einstein-Cartan gravity (with torsion as a dynamical field)
- Topological field theory (torsion as a topological modulus)

---

## Framework Relevance

The phonon-exflation framework builds on a similar principle: internal geometry (the Dirac operator on SU(3)) encodes particle properties.

**Parallel**:
- Batakis-Kehagias: Torsion in the spin connection → chiral fermions
- Phonon-exflation: Jensen deformation + spectral action on SU(3) → particle masses and couplings

Both treat geometry as primary and particle properties as emergent.

**Specific connection**:
- In the framework, the K_7 charge is associated with the U(1)_7 symmetry of the SU(3) manifold (Session 35: [iK_7, D_K] = 0 at all τ).
- This is structurally similar to how torsion couples to fermion chirality: an internal geometric property (the gauge connection) determines external observable quantities (fermion properties).

**Key insight from Batakis-Kehagias**: Chirality is not fundamental but **emerges from geometry**. By analogy, in the framework, the Standard Model gauge group may emerge from the spectral geometry of M4 x SU(3), without being imposed by fiat.

**Limitation and opportunity**: Batakis-Kehagias works only for one generation (one chiral fermion per torsion component). The framework must explain why three generations appear — a challenge. The resolution may involve multiple torsion profiles or a more sophisticated internal topology (beyond simple SU(3), e.g., SU(3) with defects or a moduli family).

---

