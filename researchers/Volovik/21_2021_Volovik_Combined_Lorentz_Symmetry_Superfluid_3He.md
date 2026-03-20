# Combined Lorentz Symmetry: Lessons from Superfluid 3He

**Author:** Grigory E. Volovik
**Year:** 2021
**Journal:** Journal of Low Temperature Physics 204, 475 (2021)
**arXiv:** 2011.06466

---

## Abstract

This paper explores how P (parity), T (time-reversal), and Lorentz symmetry in the relativistic quantum vacuum might be combined symmetries—emerging from symmetry breaking of more fundamental symmetries in the quantum vacuum—rather than fundamental. Two scenarios are realized in superfluid phases of ³He: the ³He-A scenario and the ³He-B scenario. In these scenarios, gravitational tetrads are considered as the order parameter of the symmetry breaking in the quantum vacuum. The paper demonstrates that combined Lorentz symmetry can emerge from a more fundamental SO(5) symmetry that is spontaneously broken in the quantum vacuum, with superfluid ³He providing an explicit condensed matter realization.

---

## Historical Context

For a century, Lorentz invariance has been treated as a fundamental symmetry of nature. Combined with CPT, it forms the foundation of relativistic quantum field theory. However, if spacetime itself emerges from a microscopic substrate (as Volovik's research program suggests), then these symmetries need not be fundamental—they can be *emergent*.

The critical insight is that different phases of the underlying substrate can exhibit different emergent symmetries. Some phases might have full Lorentz symmetry, others partial or broken Lorentz symmetry. The universe selects a particular phase, giving the appearance of fundamental symmetry.

Paper 21 provides an explicit mechanism: superfluid ³He phases exhibit different types of symmetry breaking, each producing different emergent symmetries in the low-energy effective theory. By studying these phases, we learn how Lorentz symmetry can emerge and change.

---

## Key Arguments and Derivations

### Fundamental vs. Emergent Symmetries

In condensed matter systems, the distinction between fundamental and emergent symmetries is clear:

- **Fundamental (microscopic):** The quantum Hamiltonian is invariant under the symmetry.
- **Emergent (macroscopic):** The low-energy effective field theory is invariant, but the Hamiltonian is not.

Example: A crystal has translational symmetry in its effective description (phonons), but the microscopic Hamiltonian has only discrete lattice translations. Full translational symmetry emerges.

Applying this to gravity: Lorentz symmetry is emergent if the fundamental Hamiltonian (defined on the quantum substrate) is invariant under a *larger* symmetry group, from which Lorentz emerges at low energy.

### Superfluid ³He Phases

Superfluid ³He has two important phases:

**³He-A phase:** P and T are both broken, but PT (parity times time-reversal) is conserved. The order parameter is:

$$\vec{d}(\vec{k}) = \hat{d} (\vec{k} \cdot \vec{n})$$

where $\hat{d}$ is a unit vector in spin space and $\vec{n}$ is a preferred direction in momentum space.

**³He-B phase:** P and T are separately broken in the same manner, but the order parameter is isotropic:

$$\Delta_B = \Delta_0 (\hat{\sigma}_x + i \hat{\sigma}_y) / 2$$

(pairing in the spin-1 channel)

Both phases spontaneously break the original SO(3) spin rotation symmetry down to smaller subgroups, introducing preferred directions in space.

### SO(5) Fundamental Symmetry

Paper 21 proposes that the fundamental symmetry underlying both ³He-A and ³He-B is the larger SO(5) group, which includes:

1. SO(3) spatial rotations
2. SO(2) internal (gauge-like) transformations
3. Mixing between spin and orbital angular momentum

The effective Hamiltonian is invariant under SO(5):

$$H = H_{kinetic} + H_{pair}, \quad [H, SO(5)] = 0$$

Upon cooling, the system undergoes a phase transition:

$$SO(5) \to SO(3) \quad \text{(in ³He-A or ³He-B)}$$

The residual symmetry is a subgroup of SO(5). Different subgroups correspond to different phases.

### Emergent Tetrad from Order Parameter

The key insight is that the order parameter $\Delta(\vec{k})$ can be rewritten in terms of a tetrad:

$$e^a_\mu = f(\Delta(\vec{k}), \text{spatial gradients})$$

In ³He-A, the preferred direction $\vec{n}$ becomes a spatial tetrad direction. In ³He-B, the isotropic structure leads to a different tetrad form. The **emergent metric** is then:

$$g_{\mu\nu} = \delta_{ab} e^a_\mu e^b_\nu$$

This metric is not the fundamental spacetime metric but an *effective* metric felt by low-energy quasiparticles.

### Four-Tetrad Structure and Sector Dependence

Volovik shows that different fermion species (quasiparticles in different energy bands) can experience *different* effective metrics, corresponding to different tetrads:

$$e^a_\mu \quad \text{for electrons}, \quad e'^a_\mu \quad \text{for holes}, \quad e''^a_\mu \quad \text{for phonons}, \quad \ldots$$

This sector-dependent geometry is a radical departure from Einstein's theory, where all particles follow the same metric. However, at low energy, all these tetrads approximately coincide, giving the impression of a single universal metric.

The sector-dependent tetrads can lead to:
- Parity violation (different sign for left/right handed fermions)
- Violation of equivalence principle (different masses couple to different effective $g$)
- Lorentz violation at high energy

### Combined Lorentz Symmetry

The term "combined" Lorentz symmetry refers to transformations that **mix** Lorentz boosts with other symmetries. For example:

$$\text{Combined}: x_\mu \to L^\mu_\nu x^\nu + \text{(gauge transformation)}$$

whereas standard Lorentz:

$$\text{Standard}: x_\mu \to L^\mu_\nu x^\nu$$

In the context of ³He phases, combined Lorentz emerges because the order parameter (tetrads) transforms under both spacetime translations and internal gauge transformations. Boosts cannot be separated from internal rotations.

Mathematically, the symmetry group is:

$$ISO(3,1) \times G_{internal}$$

where ISO is the Inhomogeneous Special Orthogonal group (Lorentz plus translations). However, in the emergent low-energy theory, this factorization breaks down, and the symmetry becomes:

$$\text{Combined: } [ISO(3,1) \times G_{internal}] / H$$

where H is a subgroup that is diagonally broken.

### Planck Constant as Order Parameter Scale

Paper 21 makes a striking prediction: the Planck constant $\hbar$ (or equivalently, the speed of light scale) is **not a fundamental constant** but emerges from the order parameter scale:

$$\hbar \sim \langle \Delta \rangle$$

where $\langle \Delta \rangle$ is the condensation amplitude. Different phases of the quantum substrate could have different effective values of $\hbar$. Session 38's finding of distinct Planck constants for different sectors (Papers 12, 03 in Volovik folder) is a direct realization of this prediction.

---

## Key Results

1. **Lorentz Symmetry is Emergent:** P, T, and Lorentz symmetry need not be fundamental but can emerge from symmetry breaking of a larger SO(5) symmetry.

2. **Superfluid ³He Realizes the Mechanism:** Two phases (³He-A and ³He-B) exhibit the symmetry breaking pattern with different effective metrics (tetrads) for quasiparticles.

3. **Sector-Dependent Metrics:** Different fermionic species can experience different effective tetrads, violating the equivalence principle at microscopic level but restoring it at low energy.

4. **Combined Symmetry:** Lorentz boosts become inseparable from internal gauge transformations in the emergent picture—a "combined Lorentz" symmetry.

5. **Tetrads as Order Parameters:** Gravitational tetrads are composite variables built from the fermionic order parameter, directly realizing Einstein's tetrad formulation of gravity.

6. **Planck Constant and Speed of Light are Emergent:** Both $\hbar$ and $c$ scale with the order parameter magnitude, changing between phases.

---

## Impact and Legacy

Paper 21 established the conceptual foundation for understanding spacetime symmetries as emergent properties. The work influenced:

- Quantum gravity research on emergent spacetime
- Lattice gauge theory studies of Lorentz invariance violation
- High-energy physics searches for trans-Planckian symmetry breaking
- Condensed matter analogs of cosmological phase transitions

The sector-dependent metric prediction (Paper 21) has testable consequences: different particles should experience slightly different gravitational red shifts, detectable with precision spectroscopy.

---

## Connection to Phonon-Exflation Framework

Paper 21 directly addresses **LORENTZ-KK-21 and sector-dependent physics** gates in phonon-exflation. Specifically:

- **SU(3) as the fundamental symmetry:** In phonon-exflation, the SU(3) gauge group (Sessions 7-8) plays the role of Volovik's SO(5). The SU(3) symmetry is spontaneously broken by the condensate to the diagonal U(1)_7 (hypercharge), giving emergent Lorentz symmetry in the low-energy limit.

- **Multiple tetrads for multiple sectors:** Paper 21 predicts sector-dependent metrics. Phonon-exflation realizes this explicitly: the electron sector, quark sector, Higgs sector, and 4D gravity each experience slightly different metric signatures due to the K_7 coupling (Paper 02 in Cosmic-Web folder: different $a_4$ per sector).

- **Planck constant emergence:** Sessions 32-35 showed that the effective Planck constant differs between sectors: $\hbar_{eff} \propto g_sector$. This is Paper 21's prediction that $\hbar \sim \langle \Delta \rangle$ (condensation scale). The K_7 condensate's magnitude sets the effective Planck constant for each sector.

- **Combined Lorentz and internal symmetries:** The discovery that [iK_7, D_K] = 0 at all τ (Session 34 permanent result) means that Lorentz boosts (encoded in the Dirac operator structure) and internal U(1)_7 gauge transformations are not independent. This is Volovik's "combined Lorentz symmetry"—the internal symmetry cannot be separated from spacetime symmetry.

- **Equivalence principle violation and restoration:** Paper 21 shows sector-dependent tetrads violate equivalence principle microscopically but restore it at low energy. Phonon-exflation predicts the same: at the Planck scale (internal compactification scale), different sectors have slightly different gravitational couplings (depending on K_7 assignment). At 4D scales much larger than the fold region, the average metric dominates, restoring equivalence principle approximately.

- **Tetrads from fermionic bilinears:** Paper 21's construction of tetrads from fermionic order parameters matches phonon-exflation's tetrad formula: $e^a_\mu \propto \bar{\Psi}_+\Gamma^a\Psi_+$ (Sessions 7-8). The SU(3) geometry is entirely built from spinor bilinears.

- **P, T symmetry breaking in phases:** Different Volovik superfluid phases break P and T differently. Similarly, phonon-exflation's ³He-A analogue (K_7 condensate with preferred axis) breaks P and T relative to the ³He-B-like reference (fully isotropic pairing). The asymmetry between matter and antimatter (Sessions 35-38) reflects this phase selection.

The phonon-exflation framework is thus the internal-space realization of Volovik's "combined Lorentz symmetry" program: the universe selected a particular phase of the SU(3) quantum substrate, breaking SO(5) to SU(3), and in this phase, Lorentz boosts became inseparable from internal U(1)_7 transformations. The sector-dependent Planck constant hierarchy emerges as a consequence.

---

## References

- [2011.06466] Combined Lorentz symmetry: lessons from superfluid 3He (arXiv)
- Volovik, G.E., J. Low Temp. Phys. 204, 475 (2021)
- Volovik, G.E., "The Universe in a Helium Droplet" (Oxford University Press, 2003)
- Mermin, N.D. and Ho, T.L., Phys. Rev. Lett. 36, 594 (1976) [³He superfluid phases]
- Thuneberg, E.V., et al., Phys. Rev. B 44, 9944 (1991) [Topological defects in ³He]
