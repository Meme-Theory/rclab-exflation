# Non-Linear Field Theory for Lepton and Quark Masses

**Author(s):** André Gsponer, Jean-Pierre Hurni
**Year:** 1996
**Journal:** Hadronic Journal 19 (1996) 367-373
**arXiv:** hep-ph/0201193
**Relevance:** MEDIUM

---

## Abstract

Barut's formula for the mass of leptons is successfully extended to quarks. A very simple non-linear scalar field model explains both the N^4 power law dependence of the mass, and the existence of a cut-off which limits the number of leptons to three and the number of quarks to five, suggesting that the mass of the sixth quark is of different origin.

---

## Key Arguments and Derivations

### 1. Barut's Mass Formula Extended to Quarks

Starting from Barut's 1979 lepton mass formula, which adds a quantized self-energy of magnitude (3/2)alpha^{-1} M_e c^2 N^4 to the rest mass:

M(N) = M_e (1 + (3/2) alpha^{-1} sum_{n=0}^{N} n^4)

The formula gives the muon mass to ~10^{-4} accuracy and the tau mass to ~10^{-3}. The authors extend this to quarks by taking M_u = M_e / 7.25 as the mass of the lightest quark, finding good agreement with observed quark masses (u, d, s, c, b).

### 2. Non-Linear Scalar Field Model ("Barybag")

The authors postulate a relativistic bag-like model with a non-linear Lagrangian density containing an F^4 term:

dL/dV = (1/2) partial_nu F partial^nu F - (1/2) mu^2 F^2 - (1/4) g^2 F^4

Solutions are Jacobi elliptic functions (cn and sd). The boundary condition F = 0 on the bag surface leads to a quantization condition, and the energy density is constant within the bag:

4pi dE/dV = g^2 omega^4 k^2(1 - k^2)

The mass increment for the nth excitation is:

Delta M(n) c^2 = (K^4 / 3) n^4 g^2 / s_0 * k^2(1 - k^2)

### 3. Harmonic and Equianharmonic Cases

The modulus k has two exceptional values for elliptic functions: the harmonic case k = sin(pi/4) and the equianharmonic case k = sin(pi/12). The authors associate the former with leptons and the latter with quarks. These give a mass ratio of ~7.2448 between the lepton and quark sequences, close to the input M_e/M_u = 7.25.

### 4. Cut-Off from Uncertainty Principle

When the barybag energy reaches E_{s_0} = (3/4) alpha^{-2} M_e c^2 ≈ 7.2 GeV, Heisenberg's uncertainty principle causes the non-spreading bag to decay into a spreading de Broglie wave packet. This explains why the mass spectrum terminates at ~9.6 GeV (alpha^{-2} M_e), limiting leptons to three and quarks to five. The top quark mass is thus of different origin.

### 5. Petiau Waves

The model connects to Petiau's non-linear generalization of quantum theory, where "standing" Jacobi elliptic waves replace "progressive" sinusoidal de Broglie waves. The modulus k interpolates between pure de Broglie waves (k=0) and pure solitonic waves (k=1).

## Key Results

1. Barut's N^4 formula extended to quarks with M_u = M_e/7.25.
2. Non-linear scalar field with F^4 term naturally produces N^4 mass scaling.
3. Harmonic/equianharmonic moduli of elliptic functions distinguish leptons from quarks with mass ratio ~7.24.
4. Heisenberg uncertainty principle provides a natural cut-off at alpha^{-2} M_e ≈ 9.6 GeV.
5. For leptons (k^2 = 1/2), mu(k) = 0 implies the field equation corresponds to a massless particle (neutrino).
6. For quarks, mu(k) != 0, and for n = 5 the mass ~115 GeV is on the order of the top quark mass.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Barut formula | $M(N) = M_e\left(1 + \frac{3}{2}\alpha^{-1}\sum_{n=0}^{N} n^4\right)$ | Eq. (1) |
| Non-linear Lagrangian | $\frac{dL}{dV} = \frac{1}{2}\partial_\nu F\,\partial^\nu F - \frac{1}{2}\mu^2 F^2 - \frac{1}{4}g^2 F^4$ | Eq. (2) |
| Mass increment | $\Delta M(n)\,c^2 = \frac{K^4}{3}\,n^4\,\frac{g^2}{s_0}\,k^2(1-k^2)$ | Eq. (5) |
| Petiau Hamiltonian | $H = C_0\,\omega^4\,k^2(1-k^2)$ | Eq. (6) |
| Cut-off energy | $E_{s_0} \approx \frac{3}{4}\alpha^{-2} M_e c^2 \approx 7.2\,\text{GeV}$ | Eq. (7) |

## Relevance to Phonon-Exflation

The N^4 power-law mass scaling from a non-linear field theory with solitonic solutions provides a concrete mechanism where mass hierarchies emerge from excitation quantum numbers rather than Yukawa couplings. The use of elliptic functions (Jacobi cn, sd) with special moduli to distinguish lepton and quark sectors has structural parallels to the spectral action approach where eigenvalue ratios on SU(3) determine mass hierarchies. The cut-off from uncertainty principle at alpha^{-2} M_e connects mass generation to alpha in a way that resonates with the framework's interest in fundamental constant relationships.
