# Fragmentation of the Giant Pairing Vibration in 14C induced by many-body processes

**Author(s):** F. Barranco, G. Potel, E. Vigezzi
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2402.14166
**Relevance:** HIGH

---

## Abstract

We present a theoretical framework for treating the full excitation spectrum of J^pi = 0+ pair addition modes, including the well-known low-lying and bound Pairing Vibration on par with the predicted Giant Pairing Vibration lying in the continuum. Our formalism includes the coupling to low-energy collective quadrupole modes of the core, in such a way that both single-particle self-energy effects and the pairing interaction induced by phonon exchange are accounted for. The theory is applied to the case of the excitation spectrum of 14C, recently populated by two-neutron transfer reactions.

---

## Key Arguments and Derivations

### Extended pp-RPA framework

The authors construct a Hamiltonian for the A+2 system with two valence particles on a vibrating A core:

H_2v = H(1) + H(2) + V_int(1,2) + H_vib

where H(i) = K(i) + V(i) + H_PVC(i) and H_vib describes the phonon degrees of freedom. The particle-vibration coupling (PVC) is:

H_PVC(i) = sum_{lambda,mu} -r_i dV(i)/dr_i beta_lambda / sqrt(2lambda+1) Y_{lambda mu}(i) [Gamma^dag_{lambda mu} + (-1)^mu Gamma_{lambda -mu}]

### Four-component basis

The basis states for the A+2 system include four types:
1. Fermion pp (particle-particle above Fermi)
2. Fermion pp x boson (pp coupled to phonon)
3. Fermion ph x boson (particle-hole coupled to phonon)
4. Fermion hh (hole-hole below Fermi)

This extended pp-RPA includes PVC effects beyond the standard pp-RPA/TDA.

### Monopole strength function

The pair addition strength is computed from eigenvalues E_k and transition amplitudes S_k, using a radial form factor f(r) = (1/V_0) dV/dr. The continuous strength function is obtained by convolution with a Lorentzian and averaging over multiple box sizes (17 boxes, R_box from 20-28 fm in 0.5 fm steps) to handle continuum resonances.

### Results for 14C

The mean field for 13C is a Woods-Saxon potential (V_0 = 72 MeV, a = 0.65 fm, R = 2.27 fm). Including coupling to the 2+ state of the core (hbar*omega_2+ = 4.44 MeV, beta_2 = 0.46) produces renormalized many-body states in good agreement with experiment.

The PVC splits the GPV bump that appears in pp-RPA. Most strength shifts to lower energy due to increased effective mass, producing two excited bound 0+ states (0+_2 at E* ~ 7 MeV, 0+_3 at E* ~ 9.6 MeV). The remaining GPV strength forms a continuum bump at E* ~ 16-20 MeV, consistent with experimental observations.

### Quadrupole pairing component

More than 50% of the wave function in the continuum bump region consists of [pp' x 2+]_{0+} components. A separable quadrupole pairing interaction V^quad_int = -pi G_2/5 sum_mu P^dag_{2mu} P_{2mu} enhances these components, suggesting that coupled-channel processes (inelastic excitation of 2+ plus pair transfer) complement direct two-nucleon transfer.

---

## Key Results

1. PVC produces essential fragmentation of the GPV: the sd-shell strength that forms the GPV in pp-RPA is redistributed to both bound excited states and a continuum bump
2. The 14C ground state (E(0+_1) = -13.5 MeV) agrees with experimental S_2n = 13.1 MeV
3. Two excited bound 0+ states predicted with large pp' x 2+ admixtures (37% and 33%)
4. The continuum bump at E* ~ 16-20 MeV has ~60% quadrupole-phonon admixture
5. The induced pairing interaction from phonon exchange is essential for realistic pairing properties

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Hamiltonian | $H_{2v} = H(1) + H(2) + V_{\text{int}}(1,2) + H_{\text{vib}}$ | Eq. (1) |
| PVC coupling | $H_{\text{PVC}}(i) = \sum_{\lambda\mu} -r_i \frac{dV(i)}{dr_i} \frac{\beta_\lambda}{\sqrt{2\lambda+1}} Y_{\lambda\mu}(i)[\Gamma^\dagger_{\lambda\mu} + (-1)^\mu \Gamma_{\lambda-\mu}]$ | Eq. (2) |
| Monopole strength | $S_k(R_{\text{box}}) = \|\sum_{pp'} X^{(k)}_{pp'} \int dr\, \psi_p(r)\psi_{p'}(r) f(r) \langle j_p \| Y_0 \| j_{p'} \rangle + \text{hh terms}\|^2$ | Eq. (3) |
| Quadrupole strength | $S^q_k(R_{\text{box}}) = \|\sum_{pp'} X^{(k)}_{pp'2+} \int dr\, \psi_p(r)\psi_{p'}(r) f(r) \langle j_p \| Y_2 \| j_{p'} \rangle\|^2$ | Eq. (4) |
| Box averaging | $S(E) = \frac{1}{N_{\text{box}}} \sum_{i=1}^{N_{\text{box}}} S(E; R_{\text{box},i})$ | Text |
| Gogny force | Finite range Gogny pairing interaction scaled by factor 0.9 | Sec. II |
| Quad. pairing | $V^{\text{quad}}_{\text{int}} = -\frac{\pi G_2}{5} \sum_\mu P^\dagger_{2\mu} P_{2\mu}$, $G_2 = 0.075$ fm$^2$/MeV | Sec. II |
| Shell spacing | $\hbar\Omega \approx 41/A^{1/3}$ MeV | Sec. I |
| Core vibration | $\hbar\omega_{2+} = 4.44$ MeV, $\beta_2 = 0.46$ | Sec. II |
| Mean field | Woods-Saxon: $V_0 = 72$ MeV, $a = 0.65$ fm, $R = 2.27$ fm | Sec. II |

## Relevance to Phonon-Exflation

The GPV fragmentation mechanism is directly relevant to the framework's pair vibration physics on the internal SU(3) manifold. Session 37 identified the Giant Pair Vibration as the dominant collective mode (omega_PV = 0.79), analogous to nuclear GPV. This paper shows that PVC fragments the GPV into multiple bound states plus a continuum bump -- precisely the kind of fragmentation that could redistribute the framework's pair-vibration strength across the tau-transit, modifying the P_exc and GGE relic spectrum predicted in Session 38. The quadrupole-phonon admixture mechanism maps onto coupling between the K_7 pairing channel and geometric (deformation) degrees of freedom.
