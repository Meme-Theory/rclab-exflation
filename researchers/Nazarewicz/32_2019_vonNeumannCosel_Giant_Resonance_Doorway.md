# Gross, Intermediate and Fine Structure of Nuclear Giant Resonances: Evidence for Doorway States

**Author(s):** Peter von Neumann-Cosel, Vladimir Yu. Ponomarev, Achim Richter, Jochen Wambach
**Year:** 2019
**Journal:** European Physical Journal A (submitted)
**arXiv:** 1905.02579
**Relevance:** HIGH

---

## Abstract

We review the phenomenon of fine structure of nuclear giant resonances and its relation to different resonance decay mechanisms. Wavelet analysis of the experimental spectra provides quantitative information on the fine structure in terms of characteristic scales. A comparable analysis of resonance strength distributions from microscopic approaches incorporating one or several of the resonance decay mechanisms allows conclusions on the source of the fine structure. For the isoscalar giant quadrupole resonance (ISGQR), spreading through the first step of the doorway mechanism, i.e. coupling between one particle-one hole (1p1h) and two particle-two hole (2p2h) states is identified as the relevant mechanism. In heavy nuclei it is dominated by coupling to low-lying surface vibrations, while in lighter nuclei stochastic coupling becomes increasingly important. The fine structure observed for the isovector giant dipole resonance (IVGDR) arises mainly from the fragmentation of the 1p1h strength (Landau damping), although some indications for the relevance of the spreading width are also found.

---

## Key Arguments and Derivations

### Introduction and Doorway Scheme (Sec. 1)
Giant resonance total width $\Gamma$ decomposes into three mechanisms: Landau damping $\Gamma^\downarrow$ (fragmentation of 1p1h excitations), escape width $\Gamma^\uparrow$ (direct particle emission from 1p1h configurations), and spreading width $\Gamma^\downarrow$ (evolution of 1p1h into 2p2h and finally npnh states): $\Gamma = \Gamma^\downarrow + \Gamma^\uparrow + \Gamma^\downarrow$. This implies a hierarchy of widths and timescales -- the doorway state picture -- where coupling to 2p2h states leads to fragmentation into "doorways" for damping across complex states toward the compound nucleus. Characteristic scales range from total width (~MeV) to compound nuclear widths (~eV in heavy nuclei).

### Experimental Evidence (Sec. 2.1)
Fine structure has been systematically established as a global phenomenon for all types of giant resonances across the nuclear chart. For the ISGQR in $^{208}$Pb, high-resolution measurements (40 keV FWHM at iThemba LABS) reveal pronounced fine structure invisible at 1 MeV resolution. Peak-by-peak agreement between independent experiments at iThemba LABS and IUCF confirms structures are of genuine physical origin, not instrumental artifacts. The ISGQR centroid energy follows systematics $E_C = 31.2 A^{-1/3} + 20.6 A^{-1/6}$ (Eq. 2). Fine structure prevails even in well-deformed heavy nuclei with extremely high level densities.

### Wavelet Analysis (Sec. 2.2)
Quantitative information on fine structure is extracted using the continuous wavelet transform (CWT) with the complex Morlet wavelet $\Psi(x) = \pi^{-1/4} e^{ik_0 x} e^{-x^2/2}$ ($k_0 = 5$). The wavelet coefficient $C_i(E) \propto \int \sigma(E) \Psi^*((E_i - E)/\delta E) dE$ is computed, and the power spectrum $P_w(\delta E) = (1/N) \sum |C_i|^2$ reveals peaks at characteristic scales. Normalization to spectral variance facilitates comparison across nuclei.

### Theoretical Framework (Sec. 3)
The nuclear Hamiltonian in second quantized form uses single-particle energies and antisymmetrized two-body matrix elements. The strength function $S_F(\omega) = \sum_\alpha |\langle\alpha|\hat{F}|0\rangle|^2 \delta(\omega - E_\alpha)$ and energy-weighted sum rules $m^k_F = \int d\omega\, \omega^k S_F(\omega)$ characterize collective response. The RPA equations give collective modes exhausting large fractions of $m^1_F$. Extensions beyond RPA (SRPA, QPM, ETFFS, RQTBA) incorporate 1p1h-phonon coupling to describe the doorway mechanism.

### ISGQR Results (Sec. 4)
For the ISGQR in $^{208}$Pb, RPA alone produces no fine structure -- only broad Landau-damped bumps. Including 2p2h coupling via SRPA or QPM generates characteristic scales matching experiment (300-700 keV range). In heavy nuclei (Pb, Sn, Zr), the dominant coupling is to low-lying surface vibrations (collective phonons). In lighter nuclei ($^{40}$Ca, $^{28}$Si), stochastic coupling to the background of 2p2h states becomes increasingly important.

### IVGDR Results (Sec. 5)
For the IVGDR, the situation differs: fine structure arises mainly from Landau damping (1p1h fragmentation). RPA calculations already reproduce much of the observed wavelet power spectrum structure. However, some indications for additional spreading width contributions are found, especially in heavier nuclei.

## Key Results

1. Fine structure of giant resonances is a global phenomenon observed for ISGQR, IVGDR, ISGMR, and magnetic/spin-flip resonances across the nuclear chart
2. ISGQR fine structure originates from the first step of the doorway mechanism: 1p1h $\to$ 2p2h coupling
3. In heavy nuclei (A > 90), ISGQR doorway coupling is dominated by low-lying collective surface vibrations
4. In lighter nuclei, stochastic (incoherent) coupling to 2p2h background becomes the primary source of fine structure
5. IVGDR fine structure arises mainly from Landau damping (1p1h fragmentation), with subdominant spreading width contributions
6. Wavelet analysis with Morlet wavelets provides robust characteristic scales for comparison between experiment and theory
7. Peak-by-peak reproducibility between independent experiments confirms fine structure is of genuine physical origin
8. Fine structure persists in well-deformed nuclei despite extremely high level densities in the GR excitation region

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Total width | $\Gamma = \Gamma^\downarrow + \Gamma^\uparrow + \Gamma^\downarrow$ | Eq. (1) |
| GDR centroid | $E_C = 31.2 A^{-1/3} + 20.6 A^{-1/6}$ | Eq. (2) |
| Wavelet coefficient | $C_i(E) = \frac{1}{\sqrt{\delta E}} \int \sigma(E) \Psi^*\left(\frac{E_i - E}{\delta E}\right) dE$ | Eq. (3) |
| Morlet wavelet | $\Psi(x) = \pi^{-1/4} e^{ik_0 x} e^{-x^2/2}$ | Eq. (4) |
| Power spectrum | $P_w(\delta E) = \frac{1}{N} \sum_{i=i_1}^{i_2} |C_i(\delta E) C_i^*(\delta E)|$ | Eq. (5) |
| Nuclear Hamiltonian | $\hat{H}_A = \sum_i \epsilon_i a^\dagger_i a_i + \frac{1}{4}\sum_{ijkl} v_{ijlk} a^\dagger_i a^\dagger_j a_l a_k$ | Eq. (6) |
| Strength function | $S_F(\omega) = \sum_\alpha |\langle\alpha|\hat{F}|0\rangle|^2 \delta(\omega - E_\alpha)$ | Eq. (9) |
| Sum rules | $m^k_F = \int d\omega\, \omega^k S_F(\omega)$ | Eq. (10) |
| RPA matrix | $\begin{pmatrix} A & B \\ -B^* & -A^* \end{pmatrix}\begin{pmatrix} X \\ Y \end{pmatrix} = E_\alpha \begin{pmatrix} X \\ Y \end{pmatrix}$ | Eq. (18) |

## Relevance to Phonon-Exflation

This paper provides the empirical and theoretical evidence that doorway states produce measurable fine structure with characteristic scales extractable by wavelet analysis. For the phonon-exflation framework, the hierarchy of widths (MeV $\to$ keV $\to$ eV) and the distinction between collective phonon-mediated coupling (heavy nuclei) versus stochastic coupling (light nuclei) maps onto the question of how KK mode decay proceeds through doorway states vs. statistical compound processes. The Ericson fluctuation analysis in S42 ($V/D = 55$) places the framework firmly in the overlapping resonance regime where the SR doorway mechanism operates. The wavelet technique itself could be applied to spectral action eigenvalue distributions to search for analogous characteristic scales.
