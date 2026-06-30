# Failure of the Goldstone Theorem for Vector Fields and Boundary-Mode Proliferation in Hyperbolic Lattices

**Author(s):** Daniel Sela, Nan Cheng, Kai Sun
**Year:** 2025
**Journal:** arXiv preprint (submitted to PRL)
**arXiv:** 2511.16328
**Relevance:** HIGH

---

## Abstract

Hyperbolic lattices extend crystallinity into curved space, where negative curvature and exponentially large boundaries reshape collective excitations beyond Euclidean intuition. In this Letter, we push the study beyond scalar fields by exploring vector fields on hyperbolic lattices. Using phonons as an example, we show that the Goldstone theorem breaks down for vector fields in hyperbolic lattices. In stark contrast to Euclidean crystals, where the Goldstone theorem ensures that acoustic phonon modes are gapless, hyperbolic lattices with coordination number $z > 2d$ exhibit a finite bulk phonon gap. We identify the origin of this breakdown: the Goldstone modes here belong to nonunitary representations of the translation group and therefore cannot form gapless excitation branches. We further show that when boundaries are included, this bulk spectral gap is filled by an extensive number of low-frequency boundary modes.

---

## Key Arguments and Derivations

### 1. Introduction and Motivation

The paper extends the study of hyperbolic lattices from scalar fields to vector fields (phonons). Hyperbolic lattices have been realized experimentally in circuit QED, electrical circuits, and photonic systems. Two key features distinguish hyperbolic from Euclidean lattices: (1) negative curvature and (2) a finite boundary-to-bulk ratio that persists in the thermodynamic limit. The authors investigate what new physics emerges when the excitations are vector fields that sense curvature through holonomy.

### 2. Why the Goldstone Theorem Fails

The Goldstone theorem relies on two logically distinct ingredients: (1) the existence of a zero-energy mode from spontaneous symmetry breaking, and (2) the emergence of a gapless branch of bulk excitations. In flat space, both hold. In curved space, the first still holds (uniform translations remain zero-energy deformations), but the second fails.

The key insight is that phonon displacements are vector fields that undergo nontrivial parallel transport. In flat space, Goldstone modes belong to unitary representations of the translation group, placing them within the bulk spectrum at $k = 0$. In hyperbolic space, these Goldstone modes transform under a three-dimensional **nonunitary** irreducible representation of the translation group $SO(1,2)$. Since bulk phonon bands are governed by unitary irreps, and the nonunitary Goldstone modes are topologically disconnected from the manifold of unitary representations, the Goldstone modes are absent from the bulk bands. The bulk spectrum acquires a finite gap.

### 3. Moment-Based Spectral Analysis

Since obtaining all phonon branches in hyperbolic lattices requires determining all high-dimensional irreducible representations of the non-Abelian translation group (analytically intractable), the authors develop a moment-based approach. For a lattice of $M$ particles with dynamical matrix $D$, the $n$-th spectral moment is:

$$\langle E^n \rangle = \frac{1}{2M} \mathrm{Tr}\, D^n$$

In the thermodynamic limit, all bulk sites are equivalent by translational symmetry, so:

$$\langle E^n \rangle = \frac{(D^n)_{i1,i1} + (D^n)_{i2,i2}}{2}$$

for any bulk site $i$. The authors define a weighted spectral measure $\mathcal{E}_n = \int_0^{E_0} (1 - E/E_0)^n \rho(E)\, dE$ that emphasizes low-energy behavior as $n \to \infty$. If a gap $\Delta$ exists with $\rho(E) \sim (E - \Delta)^r$ near the gap edge, then the ratio $\mathcal{F}_n = \mathcal{E}_{n-1}/\mathcal{E}_n$ satisfies:

$$\mathcal{F}_n = \frac{1}{1 - \Delta/E_0} + \frac{1+r}{1 - \Delta/E_0} \frac{1}{n} + O(1/n^2)$$

This allows extraction of $\Delta$ by fitting the data set $\{\mathcal{F}_n\}$.

### 4. Benchmarking on Euclidean Lattices

The method is validated on triangular ($\Delta = 0$, $r \approx 0$) and square ($\Delta = 0$, $r \approx -0.5$) lattices, both in excellent agreement with known results.

### 5. The Insulating Bulk in Hyperbolic Lattices

For the $\{3,7\}$ tessellation (triangular faces, coordination number 7), fitting spectral moments up to $n = 15$ yields:

$$\omega_g = (0.795 \pm 0.004)\sqrt{k_e/m}$$

This is a finite phonon frequency gap at zero frequency -- an insulating bulk. The $\{8,8\}$ lattice also exhibits a finite spectral gap.

Two conditions are necessary: (1) **negative curvature** -- if the same network were embedded in Euclidean space, long-wavelength modes connected to Goldstone modes would fill the gap; (2) **overconstrained lattice** ($z > 2d$) -- the underconstrained $\{7,3\}$ lattice (dual of $\{3,7\}$, coordination $z = 3$) has floppy modes and no gap.

### 6. The Conducting Edge

In finite hyperbolic lattice patches, the gap does not survive. A counting argument shows the fraction of zero modes is bounded below by $1 - n_e/(2n_v)$, which is nonzero for non-triangular hyperbolic lattices even as the number of layers tends to infinity. For the rigid $\{3,7\}$ lattice, numerical diagonalization reveals that 5-6% of all modes lie below the bulk gap, and these are localized at the boundary. This creates an "insulating bulk with conducting boundary" at low frequencies.

### 7. Goldstone Modes Carry 3D Nonunitary Representations

The supplementary materials prove that the Goldstone mode $v_\alpha(r) = (\alpha \cdot K)r$ associated with generators $K_i$ of $SO(1,2)$ transforms under the tautological (nonunitary) representation: $g v_i = \sum_j g_{ji} v_j$. Since this is a nonunitary 3D irreducible representation, the Goldstone modes are topologically disconnected from the unitary irreps that define bulk bands.

---

## Key Results

1. The Goldstone theorem fails for vector fields (phonons) on overconstrained hyperbolic lattices ($z > 2d$): the bulk phonon spectrum has a finite gap despite spontaneous translational symmetry breaking.
2. The bulk gap for the $\{3,7\}$ lattice is $\omega_g = (0.795 \pm 0.004)\sqrt{k_e/m}$ with 99% confidence.
3. The failure mechanism is identified: Goldstone modes belong to nonunitary representations of $SO(1,2)$ and are topologically disconnected from the unitary bulk bands.
4. Two necessary conditions: negative curvature AND overconstrained connectivity ($z > 2d$).
5. In finite lattices, the bulk gap is filled by an extensive number of boundary-localized modes (5-6% of total modes for $\{3,7\}$), analogous to a topological insulator.
6. The fraction of zero-frequency boundary modes remains finite in the thermodynamic limit, reminiscent of Bose-Einstein condensation particle counting.
7. A moment-based method is developed that probes the low-frequency DOS from local mechanical information without computing all irreps.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spectral moment | $\langle E^n \rangle = \frac{(D^n)_{i1,i1} + (D^n)_{i2,i2}}{2}$ | Eq. (3) |
| Weighted measure | $\mathcal{E}_n = \int_0^{E_0} (1 - E/E_0)^n \rho(E)\, dE$ | Eq. (4) |
| Gap ansatz | $\rho(E) = \mathrm{const} \times (E - \Delta)^r$ for $\Delta < E \ll E_0$ | Eq. (5) |
| Ratio expansion | $\mathcal{F}_n = \frac{1}{1 - \Delta/E_0} + \frac{1+r}{1 - \Delta/E_0}\frac{1}{n} + O(1/n^2)$ | Eq. (7) |
| Bulk gap ($\{3,7\}$) | $\omega_g = (0.795 \pm 0.004)\sqrt{k_e/m}$ | Eq. (8) |
| Goldstone mode | $v_\alpha(r) = \lim_{t \to 0} \frac{e^{t\alpha \cdot K}r - r}{t} = (\alpha \cdot K)r$ | Eq. (9), Supp. |
| Translation action | $(g v_i)(gr) = \sum_j g_{ji} v_j(gr)$ | Eq. (15), Supp. |
| Representation | $g v_i = \sum_j g_{ji} v_j$ (tautological, nonunitary) | Eq. (16), Supp. |
| $E_0$ estimate | $E_0 = \sqrt{\sum_{ks}(D^2_{j1ks} + D^2_{j2ks})(q+1)}$ | Eq. (23), Supp. |
| Floppy mode bound | Fraction of zero modes $\geq 1 - n_e/(2n_v)$ | Sec. "Conducting edge" |

---

## Relevance to Phonon-Exflation

The Goldstone theorem failure on hyperbolic lattices is directly relevant to the phonon-exflation framework: the SU(3) fiber has negative sectional curvature (confirmed in Session 35, $d^2S = +20.42$ for SU(3) vs $-3.42$ for SU(2)$\times$SU(2)), and phononic excitations propagate on this curved internal geometry. If the internal lattice of excitations is overconstrained, this paper predicts a bulk phonon gap that would NOT arise in flat-space reasoning. The nonunitary representation mechanism (Goldstone modes disconnected from bulk bands) parallels the block-diagonal theorem for $D_K$ on SU(3) (Session 22b). The extensive boundary modes filling the gap in finite patches may connect to the edge/boundary physics of the compactified fiber during transit.
