# Cosmological constant and vacuum energy

**Author(s):** G.E. Volovik
**Year:** 2004
**Journal:** Annalen der Physik 14, 165-176 (2005)
**arXiv:** gr-qc/0405012
**Relevance:** CRITICAL

---

## Abstract

The general thermodynamic analysis of the quantum vacuum, which is based on our knowledge of the vacua in condensed-matter systems, is consistent with the Einstein earlier view on the cosmological constant. In the equilibrium Universes the value of the cosmological constant is regulated by matter. In the empty Universe, the vacuum energy is exactly zero, lambda = 0. The huge contribution of the zero point motion of the quantum fields to the vacuum energy is exactly cancelled by the higher-energy degrees of freedom of the quantum vacuum. In the equilibrium Universes homogeneously filled by matter, the vacuum is disturbed, and the energy density of the vacuum becomes proportional to that of matter, lambda = rho_vac ~ rho_matter. This consideration applies to any vacuum in equilibrium irrespective of whether the vacuum is false or true, and is valid both in Einstein's general theory of relativity and within the special theory of relativity, i.e. in a world without gravity.

---

## Key Arguments and Derivations

### I. Introduction

Einstein (1917) introduced the cosmological constant to make the Universe static: lambda counterbalances the collapsing tendency of gravitating matter. Einstein noted (Ref. [2]) that the lambda-term must be added when the average matter density is non-zero; lambda = 0 if matter is distributed so inhomogeneously that its average tends to zero. In this treatment, lambda resembles a Lagrange multiplier, not a fundamental constant.

The naive QFT estimate rho_vac ~ (1/c^3)(nu_b/2 - nu_f) E^4_Pl exceeds observations by 120 orders of magnitude. Supersymmetry (nu_b = 2 nu_f) does not help because SUSY is broken.

### II. Effective QFT in Quantum Liquids

Two quantum liquids serve as examples:
- Superfluid 4He: phonons with E(p) = cp, acoustic metric with sqrt(-g) = c^{-3}
- Superfluid 3He-A: fermions with E^2(p) = c_x^2 p_x^2 + c_y^2 p_y^2 + c_z^2 p_z^2

The naive phonon estimate rho_vac ~ E^4_Pl / sqrt(-g) gives the correct ORDER OF MAGNITUDE for the energy difference between true and false vacua: rho_true - rho_false ~ -E^4_Pl / sqrt(-g). But it says NOTHING about the total vacuum energy and gives the wrong sign. The same paradox as in cosmology exists in condensed matter, but there the microscopic physics is known.

### III. Relevant Thermodynamic Potential

The proper vacuum energy density for emergent QFT is:

rho_vac = (1/V) <H - sum_a mu_a N_a>_vac

Using the Gibbs-Duhem relation E - TS - sum mu_a N_a = -pV at T=0:

rho_vac = -p_vac

This gives the equation of state rho_vac = -P_vac. Key insight: shifting all single-particle energies by alpha transforms H -> H + alpha sum N_a, but the proper Hamiltonian H - sum mu_a N_a is INVARIANT because mu_a -> mu_a + alpha. The vacuum energy is independent of the zero-energy reference.

### IV. Nullification of Vacuum Energy

For an isolated liquid droplet (no environment, P=0):
- pvac = 0 in equilibrium
- Therefore rho_vac = -pvac = 0

This holds for BOTH fermionic (3He) and bosonic (4He) liquids, irrespective of details. The trans-Planckian degrees of freedom exactly cancel the sub-Planckian modes. No fine-tuning needed -- it follows from thermodynamic equilibrium.

### V. Coincidence Problem

At finite temperature T, quasiparticles exert radiation pressure p_matter = gamma T^4 sqrt(-g). For an isolated droplet, total pressure must vanish:

p_matter + p_vac = 0

Therefore: rho_vac = -p_vac = p_matter = (1/3) rho_matter

This is the condensed-matter analog of the coincidence problem: vacuum energy density is naturally of the same order as matter density! The factor 1/3 vs Einstein's factor 1/2 arises because the condensed matter has no gravity.

### VI. Energy of False and True Vacua

In 3He the true vacuum is the superfluid state and the false vacuum is the normal state. The Gibbs-Duhem relation holds for BOTH:
- True vacuum: epsilon_true - mu_true n_true = -P
- False vacuum: epsilon_false - mu_false n_false = -P

At T=0 and P=0, BOTH have zero vacuum energy. The energy difference between false and true vacua ~ E^4_Pl/sqrt(-g) is stored in the chemical potential difference, NOT in the vacuum energy. The phase transition releases this energy into quasiparticles (matter), not into the vacuum.

### VII. Einstein Universes

For Einstein static Universe with cosmological constant and hot relativistic matter:
- Without gravity: rho_vac = (1/3) rho_matter
- With gravity (Einstein static Universe): rho_vac = rho_matter

Both are thermodynamic equilibrium relations. For a Universe with spatial curvature K=1 and radius a:
rho_vac = (1/3) rho_matter + (1/4pi G a^2)

The curvature acts as an additional perturbation of the vacuum.

---

## Key Results

1. The proper vacuum energy rho_vac = (1/V)<H - sum mu_a N_a> is invariant under shift of energy reference
2. For self-sustained vacuum in equilibrium: rho_vac = 0 exactly, without fine-tuning
3. In the presence of matter: rho_vac ~ rho_matter (resolves coincidence problem)
4. Both true and false vacua have zero vacuum energy in equilibrium at P=0
5. Phase transition energy goes into matter, not into vacuum
6. The result holds with or without gravity
7. The curvature of space acts as an additional vacuum perturbation
8. The Einstein prediction (lambda proportional to matter density) is thermodynamically correct

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Naive vacuum energy | $\rho_{\text{vac}} \sim \frac{1}{c^3}\left(\frac{\nu_b}{2} - \nu_f\right)E_{\text{Pl}}^4$ | Eq.(1.3) |
| Vacuum equation of state | $\rho_{\text{vac}} = -p_{\text{vac}}$ | Eq.(1.1) |
| Proper vacuum energy | $\rho_{\text{vac}} = \frac{1}{V}\left\langle H - \sum_a \mu_a N_a\right\rangle_{\text{vac}}$ | Eq.(3.2) |
| Gibbs-Duhem relation | $E - TS - \sum_a \mu_a N_a = -pV$ | Eq.(3.3) |
| Equilibrium condition | $\rho_{\text{vac}} = -p_{\text{vac}}$ | Eq.(3.4) |
| Matter pressure | $p_{\text{matter}} = \gamma T^4\sqrt{-g}$ | Eq.(5.1) |
| Radiation EOS | $\rho_{\text{matter}} = 3 p_{\text{matter}}$ | Eq.(5.2) |
| Total pressure = 0 | $p_{\text{matter}} + p_{\text{vac}} = 0$ | Eq.(5.3) |
| Coincidence relation | $\rho_{\text{vac}} = \frac{1}{3}\rho_{\text{matter}}$ | Eq.(5.4) |
| Einstein static (hot) | $\rho_{\text{vac}} = \rho_{\text{matter}}$ | Eq.(1.5) |
| False/true vacuum | $\varepsilon_{\text{true}} - \mu_{\text{true}} n_{\text{true}} = -P$ | Eq.(6.1-6.2) |
| With curvature | $\rho_{\text{vac}} = \frac{1}{3}\rho_{\text{matter}} + \frac{1}{4\pi G a^2}$ | Eq.(7.3) |

---

## Relevance to Phonon-Exflation

This paper is the most direct theoretical ancestor of the framework's CC mechanism. Key connections:

1. **Nullification principle**: The result rho_vac = 0 for equilibrium vacuum is the foundation on which the framework builds. The phonon-exflation transit (tau evolution) is a process that takes the vacuum OUT of equilibrium temporarily, generating a non-zero CC during the transit, which then relaxes back toward zero.

2. **Coincidence problem resolution**: rho_vac ~ rho_matter in equilibrium directly addresses the observed Lambda ~ rho_matter. The framework's instanton gas dynamics during the transit provides the specific mechanism by which the vacuum energy tracks the matter content.

3. **False vacuum energetics**: The crucial result that both true and false vacua have zero vacuum energy in equilibrium, with the transition energy going into matter (quasiparticles), maps to the framework's transit dynamics: the energy released during the SU(3) fold goes into quasiparticle creation (the P_exc = 1.000 result from Session 38), not into vacuum energy.

4. **Proper thermodynamic potential**: The Hamiltonian H - sum mu_a N_a is the condensed-matter version of the framework's spectral action. The chemical potential mu plays the role of the framework's tau-dependent parameters in D_K.

5. **Independence from microscopy**: The emphasis that the nullification result is independent of the microscopic structure validates the framework's use of the thermodynamic argument across different geometric substrates (from SU(3) fiber geometry to the observed 4D physics).
