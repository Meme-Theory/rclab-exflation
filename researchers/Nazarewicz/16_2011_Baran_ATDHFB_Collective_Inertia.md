# Quadrupole Collective Inertia in Nuclear Fission: Cranking Approximation

**Author(s):** A. Baran, J.A. Sheikh, J. Dobaczewski, W. Nazarewicz
**Year:** 2011 (published Phys. Rev. C 84, 054321)
**Journal:** Physical Review C
**arXiv:** 1007.3763
**Relevance:** CRITICAL

---

## Abstract

Collective mass tensor derived from the cranking approximation to the adiabatic time-dependent Hartree-Fock-Bogoliubov (ATDHFB) approach is compared with that obtained in the Gaussian Overlap Approximation (GOA) to the generator coordinate method. Illustrative calculations are carried out for one-dimensional quadrupole fission pathways in $^{256}$Fm. It is shown that the collective mass exhibits strong variations with the quadrupole collective coordinate. These variations are related to the changes in the intrinsic shell structure. The differences between collective inertia obtained in cranking and perturbative cranking approximations to ATDHFB, and within GOA, are discussed.

---

## Key Arguments and Derivations

### ATDHFB Theory (Sec. II)

The ATDHFB approach assumes collective velocity is slow compared to single-particle velocity. The generalized HFB density matrix is expanded: $\mathcal{R} = \mathcal{R}_0 + \mathcal{R}_1 + \mathcal{R}_2$, where $\mathcal{R}_1$ is time-odd and $\mathcal{R}_0, \mathcal{R}_2$ are time-even. The kinetic energy in ATDHFB is:
$$K = \frac{i}{4} \text{Tr}\left(\dot{\mathcal{R}}_0 [\mathcal{R}_0, \mathcal{R}_1]\right)$$
leading to collective mass:
$$M = \frac{i}{2\dot{q}^2} \text{Tr}\left(\dot{\mathcal{R}}_0 [\mathcal{R}_0, \mathcal{R}_1]\right)$$

The ATDHFB equation is $i\dot{\mathcal{R}}_0 = [\mathcal{W}_0, \mathcal{R}_1] + [\mathcal{W}_1, \mathcal{R}_0]$, where $\mathcal{W}_0$ and $\mathcal{W}_1$ are the static and time-odd HFB Hamiltonians. In quasiparticle basis, this becomes $iF = EZ + ZE + E_1$, connecting the matrix $F$ (from $\dot{\mathcal{R}}_0$), $Z$ (from $\mathcal{R}_1$), and $E_1$ (time-odd interaction).

For the multi-dimensional mass tensor:
$$M_{ij} = \frac{i}{2\dot{q}_i \dot{q}_j} \text{Tr}\left(F^{i*} Z^j - F^i Z^{j*}\right)$$

### Cranking Approximation (Sec. III.A)

Neglecting $E_1$ (time-odd fields), the $Z$-matrix is obtained diagonally: $-iF^i_{\mu\nu} = (E_\mu + E_\nu) Z^i_{\mu\nu}$, giving the cranking mass tensor:
$$M^C_{ij} = \frac{1}{2\dot{q}_i \dot{q}_j} \sum_{\mu\nu} \frac{F^{i*}_{\mu\nu} F^j_{\mu\nu} + F^i_{\mu\nu} F^{j*}_{\mu\nu}}{E_\mu + E_\nu}$$

In the canonical basis, the $F$-matrix elements are:
$$\breve{F}^i_{\mu\bar{\nu}} = \frac{s_{\bar{\nu}}}{(u_\mu v_\nu + v_\mu u_\nu)} \dot{q}_i \left(\frac{\partial\rho_0}{\partial q_i}\right)_{\mu\nu}$$

The key input is the derivative of the density matrix, evaluated using the 3-point Lagrange formula for unequally spaced deformation points.

### Perturbative Cranking (Sec. III.B)

The perturbative cranking approximation (ATDHFB-Cp) replaces mean-field derivatives by perturbative expressions. The resulting mass tensor is:
$$M^{Cp}_{ij} \approx \sum_{\mu\nu} \frac{\langle\mu|h^i|\nu\rangle \langle\nu|h^j|\mu\rangle}{(\breve{E}_\mu + \breve{E}_\nu)^3} (\eta^+_{\mu\nu})^2$$
This is the standard cranking expression used in most fission studies.

### Gaussian Overlap Approximation (Sec. III.C)

The GOA mass tensor involves energy-weighted moments:
$$M^{GOA} = S^{(2)} [S^{(1)}]^{-1} S^{(2)}$$
where $S^{(K)}_{ij} = \sum_{\mu,\nu} \frac{\langle\mu|h^i|\nu\rangle \langle\nu|h^j|\mu\rangle}{(\breve{E}_\mu + \breve{E}_\nu)^K} (\eta^+_{\mu\nu})^2$.

### Results for $^{256}$Fm (Sec. IV)

Calculations used the SkM* energy density functional with density-dependent pairing. The full ATDHFB-C mass shows irregular behavior with sharp maxima related to changes in intrinsic shell structure along the fission pathway. These peaks are suppressed in the perturbative treatment. The perturbative ATDHFB-Cp and GOA results are fairly similar, with ATDHFB-Cp systematically larger.

The key finding is that the full ATDHFB-C mass is very close to the canonical approximation ATDHFB-Cc, validating the diagonal approximation for the HFB energy matrix. However, the perturbative treatment of derivatives cannot be justified — it misses the strong variations due to shell structure changes.

---

## Key Results

1. The non-perturbative cranking mass (ATDHFB-C) exhibits strong, irregular variations along the fission path due to shell structure changes
2. Perturbative cranking (ATDHFB-Cp) and GOA systematically underestimate the mass variations, producing smoother profiles
3. The ATDHFB-C mass is very close to the canonical approximation ATDHFB-Cc, validating the diagonal ansatz for the HFB energy matrix
4. Peak structures in collective mass correlate with large local variations in pairing and HF energies, indicative of configuration changes
5. The ATDHFB-Cp mass is systematically larger than the GOA mass, though both show similar patterns
6. The perturbative treatment of collective derivatives cannot be justified for quantitative fission studies
7. Diabatic jumps between energy sheets produce unphysical results; adiabatic theory fails at these crossings
8. Three-point and five-point Lagrange formulas give essentially identical results for collective derivatives

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Generalized density matrix | $\mathcal{R} = \begin{pmatrix} \rho & \kappa \\ -\kappa^* & 1-\rho^* \end{pmatrix}$ | Eq. 1 |
| HFB equation | $[\mathcal{W}, \mathcal{R}] = 0$ | Eq. 2 |
| ATDHFB kinetic energy | $K = \frac{i}{4} \text{Tr}(\dot{\mathcal{R}}_0 [\mathcal{R}_0, \mathcal{R}_1])$ | Eq. 14 |
| Collective mass | $M = \frac{i}{2\dot{q}} \text{Tr}\left(\frac{\partial\mathcal{R}_0}{\partial q} [\mathcal{R}_0, \mathcal{R}_1]\right)$ | Eq. 17 |
| Mass tensor | $M_{ij} = \frac{i}{2\dot{q}_i \dot{q}_j} \text{Tr}(F^{i*} Z^j - F^i Z^{j*})$ | Eq. 32 |
| Cranking Z-matrix | $-iF^i_{\mu\nu} = (E_\mu + E_\nu) Z^i_{\mu\nu}$ | Eq. 33 |
| Cranking mass | $M^C_{ij} = \frac{1}{2\dot{q}_i\dot{q}_j} \sum_{\mu\nu} \frac{F^{i*}_{\mu\nu} F^j_{\mu\nu} + F^i_{\mu\nu} F^{j*}_{\mu\nu}}{E_\mu + E_\nu}$ | Eq. 34 |
| BCS-equivalent F-matrix | $\breve{F}^i_{\mu\nu} \approx -\frac{\dot{q}_i}{\breve{E}_\mu + \breve{E}_\nu} [s_\nu \eta^+_{\mu\nu} (\breve{h}^i - \lambda^i)_{\mu\bar\nu} + \xi^+_{\mu\nu} (\breve{\Delta}^i)_{\mu\nu}]$ | Eq. 41 |
| Perturbative cranking mass | $M^{Cp}_{ij} \approx \sum_{\mu\nu} \frac{\langle\mu|h^i|\nu\rangle \langle\nu|h^j|\mu\rangle}{(\breve{E}_\mu + \breve{E}_\nu)^3} (\eta^+_{\mu\nu})^2$ | Eq. 60 |
| GOA mass | $M^{GOA} = S^{(2)} [S^{(1)}]^{-1} S^{(2)}$ | Eq. 62 |
| 3-point Lagrange derivative | $(\partial\rho/\partial q)_{q=q_0} \approx \text{3-point Lagrange formula}$ | Eq. 52 |

## Relevance to Phonon-Exflation

This paper provides the theoretical framework for computing collective inertia during large-amplitude motion through the SU(3) fiber geometry. The framework's "transit" along the fold ($\tau$ changing from 0 to $\tau_{fold}$) is precisely the kind of large-amplitude collective motion treated by ATDHFB. The key result — that collective mass exhibits sharp peaks at level crossings correlated with pairing energy fluctuations — maps directly onto the framework's finding that pairing dynamics (instanton gas) dominates the transit physics. The $\Delta^{-2}$ dependence of collective inertia on pairing gap (referenced in the companion paper 1410.1264) is central to the framework's "pairing-induced speedup" mechanism. The failure of perturbative cranking validates the framework's use of non-perturbative approaches (Richardson-Gaudin exact solution rather than BCS approximation).
