# Accurate Nuclear Radii and Binding Energies from a Chiral Interaction

**Author(s):** A. Ekstrom, G. R. Jansen, K. A. Wendt, G. Hagen, T. Papenbrock, B. D. Carlsson, C. Forssen, M. Hjorth-Jensen, P. Navratil, and W. Nazarewicz
**Year:** 2015
**Journal:** Physical Review Letters 114, 242501 (2015)
**arXiv:** 1502.04682
**Relevance:** HIGH

---

## Abstract

With the goal of developing predictive ab-initio capability for light and medium-mass nuclei, two-nucleon and three-nucleon forces from chiral effective field theory are optimized simultaneously to low-energy nucleon-nucleon scattering data, as well as binding energies and radii of few-nucleon systems and selected isotopes of carbon and oxygen. Coupled-cluster calculations based on this interaction, named NNLO_sat, yield accurate binding energies and radii of nuclei up to $^{40}$Ca, and are consistent with the empirical saturation point of symmetric nuclear matter. In addition, the low-lying collective $J^\pi = 3^-$ states in $^{16}$O and $^{40}$Ca are described accurately, while spectra for selected p- and sd-shell nuclei are in reasonable agreement with experiment.

---

## Key Arguments and Derivations

### 1. The Problem with Existing Chiral Interactions

Previous ab initio calculations with chiral EFT forces systematically overbind medium-mass nuclei by about 1 MeV per nucleon and underestimate charge radii. The traditional approach -- adjusting NN forces to scattering data at $T_{Lab} \lesssim 350$ MeV, then fitting NNN forces to $A \leq 4$ systems -- fails to simultaneously reproduce binding energies, radii, and the nuclear matter saturation point.

### 2. Simultaneous NN + NNN Optimization

The key departure: NN and NNN forces are optimized simultaneously, not sequentially. The fit-observable set includes:
- Binding energies and charge radii of $^3$H, $^{3,4}$He, $^{14}$C, $^{16}$O
- Binding energies of $^{22,24,25}$O
- NN scattering data from SM99 database up to 35 MeV

The rationale: (i) no reliable data constrain the isospin $T=3/2$ NNN force components in $A=3,4$; (ii) LECs should be adjusted to low-energy observables; (iii) many-body effects at higher orders are reduced when heavier systems are included; (iv) predictive power and large extrapolations do not go together.

Charge radii are obtained from point-proton radii: $\langle r^2_{ch}\rangle = \langle r^2_{pp}\rangle + \langle R^2_p\rangle + \frac{N}{Z}\langle R^2_n\rangle + \frac{3\hbar^2}{4m^2_pc^2}$ (Darwin-Foldy correction).

### 3. Computational Methods

- Few-body ($A \leq 6$): No-core shell model (NCSM) with infrared extrapolations
- Medium-mass: Coupled-cluster in $\Lambda$-CCSD(T) approximation, 15 oscillator shells, $\hbar\Omega = 22$ MeV
- NNN forces: normal-ordered two-body approximation in Hartree-Fock basis, $E_{3max} = 16\hbar\Omega$
- Residual NNN: second-order perturbative correction ($E_{3max} = 12\hbar\Omega$)
- Excited states: equation-of-motion coupled-cluster methods
- Charge radii: two-body density matrix in CCSD approximation
- Charge densities: one-body density matrix with Gaussian center-of-mass correction

### 4. The NNLO_sat Interaction

16 LECs determine the interaction: NN contact potential strengths, $\pi N$ potential (shared between NN+NNN), and NNN contacts. Optimized using POUNDerS algorithm. Nonlocal regulators with $n=3$, cutoff $\Lambda = 450$ MeV, spectral function regularization $\Lambda_{SFR} = 700$ MeV. Low-energy NN data: $\chi^2/\text{datum} \approx 4.3$ up to 35 MeV.

Key LEC values: $c_1 = -1.122$, $c_3 = -3.925$, $c_4 = 3.766$ (all in GeV$^{-1}$); $c_D = 0.817$, $c_E = -0.0396$.

### 5. Predictions

- $^8$He: E = 30.9 MeV, $r_{ch} = 1.91$ fm (exp: 31.5 MeV, 1.959(16) fm)
- $^{16}$O: $3^-_1$ state at 6.34 MeV (exp: 6.13 MeV); charge density well reproduced
- $^{40}$Ca: E = 326 MeV, $r_{ch} = 3.48$ fm, $E(3^-_1) = 3.81$ MeV (exp: 342 MeV, 3.4776(19) fm, 3.736 MeV)
- Symmetric nuclear matter: saturation point close to empirical, incompressibility $K = 253$ MeV (within accepted range)

### 6. Saturation Mechanism

The NN interaction of NNLO_sat is soft (like $V_{lowk}$), yielding overbinding and too-small radii alone. NNN interactions provide the repulsive correction needed for physical nuclei -- analogous to the role of three-body terms in nuclear density functional theory.

---

## Key Results

1. NNLO_sat is the first microscopically-founded interaction simultaneously describing masses, radii, and spectra from few-body to medium-mass systems
2. Simultaneous NN+NNN optimization is essential -- sequential optimization magnifies uncertainties in heavy nuclei
3. Including heavier nuclei (C, O) in the fit reduces extrapolation errors
4. Nuclear saturation is an emergent phenomenon -- the saturation Fermi momentum is an emergent scale included via charge radii
5. $3^-$ collective states in $^{16}$O and $^{40}$Ca are well described (dominated by $1p-1h$ excitations)
6. NNN forces contribute ~2 MeV binding to $^4$He
7. The $d$-state probability of the deuteron is 3.46%

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Charge radius | $\langle r^2_{ch}\rangle = \langle r^2_{pp}\rangle + \langle R^2_p\rangle + \frac{N}{Z}\langle R^2_n\rangle + \frac{3\hbar^2}{4m^2_pc^2}$ | Text, Sec. "Optimization" |
| Intrinsic Hamiltonian | $H = T - T_{cm} + V_{NN} + V_{NNN}$ | Text, Sec. "Optimization" |
| Regulator form | $\xi \sim \exp[(p/\Lambda)^{2n}]$, $n=3$, $\Lambda = 450$ MeV | Text, Sec. "Optimization" |
| NN scattering quality | $\chi^2/\text{datum} \approx 4.3$ at $T_{Lab} < 35$ MeV | Text |
| Saturation point | $E/A \approx -16$ MeV at $k_F \approx 1.33$ fm$^{-1}$ | Text |
| Incompressibility | $K = 253$ MeV | Fig. 5 |

---

## Relevance to Phonon-Exflation

This paper demonstrates how an effective interaction optimized simultaneously across scales (few-body to medium-mass) achieves emergent phenomena (nuclear saturation) that are missed by sequential optimization. The framework faces the same challenge: the spectral action on the SU(3) fiber must produce emergent stabilization (the fold, CC value) that cannot be captured by perturbative sector-by-sector analysis. The NNLO_sat strategy -- including the emergent momentum scale (radii) in the optimization, and accepting that saturation is emergent rather than explicit in the Lagrangian -- parallels the framework's realization that tau-stabilization is an emergent many-body effect (instanton gas), not a perturbative potential minimum. The paper also provides the state-of-the-art nuclear Hamiltonian whose BCS pairing properties (gaps, occupations) set the quantitative benchmarks for the framework's nuclear analogs.
