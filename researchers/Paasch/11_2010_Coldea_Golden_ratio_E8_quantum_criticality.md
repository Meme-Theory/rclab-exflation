# Quantum Criticality in an Ising Chain: Experimental Evidence for Emergent E8 Symmetry

**Author(s):** R. Coldea, D. A. Tennant, E. M. Wheeler, E. Wawrzynska, D. Prabhakaran, M. Telling, K. Habicht, P. Smeibidl, K. Kiefer
**Year:** 2010
**Journal:** Science 327, 177 (2010)
**arXiv:** 1103.3694
**Relevance:** MEDIUM

---

## Abstract

Quantum phase transitions take place between distinct phases of matter at zero temperature. Near the transition point, exotic quantum symmetries can emerge that govern the excitation spectrum of the system. A symmetry described by the E8 Lie group with a spectrum of 8 particles was long predicted to appear near the critical point of an Ising chain. We realize this system experimentally by tuning the quasi-one-dimensional Ising ferromagnet CoNb2O6 through its critical point using strong transverse magnetic fields. The spin excitations are observed to change character from pairs of kinks in the ordered phase to spin-flips in the paramagnetic phase. Just below the critical field, the spin dynamics shows a fine structure with two sharp modes at low energies, in a ratio that approaches the golden mean as predicted for the first two meson particles of the E8 spectrum. Our results demonstrate the power of symmetry to describe complex quantum behaviours.

---

## Key Arguments and Derivations

### 1. Transverse-Field Ising Chain

The Hamiltonian H = sum_i (-J S^z_i S^z_{i+1} - h S^x_i) describes a ferromagnetic Ising exchange J > 0 competing with a transverse field h. At the critical field h_C = J/2, a quantum phase transition occurs between magnetic order (below h_C) and a quantum paramagnet (above h_C).

### 2. Experimental System: CoNb2O6

CoNb2O6 is a quasi-1D Ising ferromagnet with:
- Near-isolated zig-zag chains of Co^{2+} ions along the c-axis
- Strong easy-axis anisotropy from crystal field effects
- 3D ordering below T_{N1} = 2.95 K stabilized by weak interchain couplings
- Critical field B_C = 5.5 T along the b-axis (transverse to Ising axis)

### 3. Kink Quasiparticles and Confinement

Below B_C, excitations are pairs of domain-wall kinks interpolating between degenerate ground states. In the ordered phase, interchain couplings create a linear confining potential V(x) = lambda|x| between kink pairs, producing a Zeeman ladder of bound states whose energies follow the Airy function zeros: m_j = 2m_0 + z_j (lambda^{2/3})(hbar^2/mu)^{1/3}. Five such bound states were observed, with energies matching Airy function predictions.

### 4. E8 Spectrum Near Criticality

Zamolodchikov (1989) predicted that at the critical point of the Ising chain with a small longitudinal field h_z, the spectrum has 8 "meson" bound states with mass ratios given by a representation of the E8 Lie group. The first two masses satisfy m_2/m_1 = (1 + sqrt(5))/2 = 1.618... (the golden ratio).

### 5. Experimental Confirmation

Neutron scattering measurements just below B_C (at 4.5 T and 5 T) reveal two sharp modes m_1 and m_2 at low energies. Their ratio approaches the golden ratio m_2/m_1 = 1.618 as the field approaches the 1D critical field (near 5 T, just below the 3D critical field of 5.5 T). This is the first experimental realization of E8 symmetry in a physical system.

## Key Results

1. First experimental observation of emergent E8 symmetry near a quantum critical point
2. Mass ratio m_2/m_1 approaches the golden ratio (1 + sqrt(5))/2 = 1.618 as predicted by Zamolodchikov's E8 theory
3. Five kink-confinement bound states observed in the ordered phase at zero field, matching Airy function predictions
4. Fundamental change in quasiparticle character across the QPT: kink pairs (ordered) to spin flips (paramagnetic)
5. Effective Hamiltonian parameters: J = 1.94(4) meV, alpha = 0.12(1)J, h_z = 0.020(2)J, beta = 0.17(1)J

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Ising Hamiltonian | $H = \sum_i (-J S^z_i S^z_{i+1} - h S^x_i)$ | Eq. (1) |
| Schrodinger for kink pair | $-\frac{\hbar^2}{\mu}\frac{d^2\phi}{dx^2} + \lambda|x|\phi = (m - 2m_0)\phi$ | Eq. (2) |
| Bound state masses | $m_j = 2m_0 + z_j \lambda^{2/3} (\hbar^2/\mu)^{1/3}$, $z_j$ = zeros of Ai(-z) | Eq. (3) |
| E8 mass ratio | $m_2/m_1 = (1+\sqrt{5})/2 = 1.618\ldots$ (golden ratio) | Zamolodchikov prediction |
| First E8 mass | $m_1/J = C(h_z/J)^{8/15}$, $C \approx 1.59$ | From Zamolodchikov (1989) |

## Relevance to Phonon-Exflation

The Coldea experiment demonstrates that exotic Lie group symmetries (E8) can emerge dynamically near quantum critical points in condensed matter systems, even when the microscopic Hamiltonian has only simple Ising symmetry. This provides experimental precedent for the phonon-exflation mechanism in which SU(3) structure emerges from the spectral triple of the internal space. The kink confinement physics (linear potential between domain walls) is analogous to the quasiparticle excitation spectrum of the BCS condensate on the SU(3) fiber, where the confining potential arises from the geometry. The observation that higher symmetries emerge precisely at critical points supports the framework's identification of the tau-fold as a quantum critical point where the instanton gas produces particle creation.
