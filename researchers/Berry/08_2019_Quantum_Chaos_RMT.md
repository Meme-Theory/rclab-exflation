# Quantum Chaotic Systems and Random Matrix Theory

**Author(s):** Akhilesh Pandey, Avanish Kumar, and Sanjay Puri
**Year:** 2019
**Journal:** 21st Century Nanoscience: A Handbook (K.D. Sattler, ed.), CRC Press
**arXiv:** 1905.10596
**Relevance:** CRITICAL

---

## Abstract

This article is an introductory review of random matrix theory (RMT) and its applications, with special focus on quantum chaos. Random matrices were first used by Wigner to understand the spectra of complex nuclei from a statistical perspective. Subsequently there have been novel applications to diverse areas, e.g., atomic and molecular physics, mesoscopic and nanoscopic systems, microwave cavities, econophysics, biological sciences, communication theory. This article is designed to be accessible at the graduate and post-doctoral level.

---

## Key Arguments and Derivations

### Section 2: Random Matrix Theory

Dyson showed there are three important classes of matrices depending on time-reversal invariance (TRI) and space-rotation invariance (SRI). Systems with TRI and SRI have symmetric Hermitian matrices (beta=1, orthogonal group); TRI with half-integral spin gives quaternion self-dual matrices (beta=4, symplectic group); broken TRI gives general complex Hermitian matrices (beta=2, unitary group). The joint probability distribution of matrix elements for an N-dimensional matrix A is P(A) = C exp(-beta tr V(A)). For Gaussian ensembles V(xi) = xi^2/(4v^2); for circular ensembles V(xi) = 0.

### Section 3: Statistical Properties of Eigenvalues

The transformation from matrix element space to eigenvalue/eigenvector space yields the joint probability distribution of eigenvalues as a product of the Vandermonde determinant raised to power beta and exponential weight factors. This Coulomb gas analogy (logarithmic repulsion between eigenvalues) gives rise to the key phenomena of level repulsion and spectral rigidity. The average eigenvalue density follows Wigner's semicircle law for Gaussian ensembles. The two-level cluster function Y_2(r) and the number variance Sigma^2(r) are derived exactly for all three classical ensembles. For the Poisson ensemble (independent eigenvalues), Y_2(r) = 0 and Sigma^2(r) = r. The Wigner surmise provides excellent 2x2 approximations to the exact nearest-neighbor spacing distributions for all three ensembles. The Delta_3 statistic (Dyson-Mehta) measures spectral rigidity via least-square deviation of the staircase function from a best-fit line. Superposition of l independent spectra is treated, showing that for large l the statistics approach Poisson.

### Section 4: Statistical Properties of Eigenvectors

Eigenvectors of random matrices are random subject to orthonormality constraints. For large N, the components become independent Gaussian variables with mean 0 and variance 1/(beta*N). The variable w = N|u_j|^2 follows a chi-squared distribution with beta degrees of freedom. For beta=1 this is the Porter-Thomas distribution, important for nuclear transition widths.

### Section 5: Application to Nuclear Spectra

The Nuclear Data Ensemble (NDE) of 1762 resonance energies from 36 sequences of 32 different nuclei shows excellent agreement with GOE predictions for nearest-neighbor spacing, number variance, Delta_3, and Porter-Thomas distribution of transition widths. The correlation coefficient r(NDE) = 0.017 confirms the RMT prediction of independence between widths and energy level spectra.

### Section 6: Quantum Chaos and Random Matrices (BGS Conjecture)

In 1977, Berry and Tabor showed that quantum systems whose classical counterparts are integrable follow Poisson statistics. In 1984, Bohigas, Giannoni and Schmit (BGS) showed that quantum systems whose classical counterparts are chaotic follow GOE/GUE statistics, establishing the BGS conjecture. Berry gave a semiclassical theory of spectral rigidity using Gutzwiller's periodic orbit theory. The quantum kicked rotor (QKR) serves as the primary paradigm for quantum chaos, exhibiting both GOE and GUE statistics.

### Section 7: Quantum Integrable Systems and Poisson Statistics

Integrable systems produce Poisson statistics, with two exceptions: harmonic oscillators (equally spaced spectra) are a major exception to the "integrability implies Poisson" rule. The rectangular billiard with irrationally related side lengths produces Poisson statistics.

### Sections 8-10: Kicked Rotor (Classical and Quantum)

The classical kicked rotor with Hamiltonian H = p^2/2 + V(phi) sum_n delta(t-n) generates the Chirikov standard map. The quantum kicked rotor (QKR) is defined via the unit time evolution operator U = BG. With gamma=0 (TRI preserved) the QKR produces COE/GOE statistics; with gamma=0.7 (TRI broken) it produces CUE/GUE statistics. Mixed spectra from parity-preserving QKR match the analytical results for superposition of two GOE spectra. CSE statistics are obtained indirectly by selecting alternate eigenvalues of COE.

### Section 11: Transition Ensembles

The GOE-to-GUE transition is parametrized by H_alpha = H^(S) + i*alpha*H^(A), with the transition parameter Lambda = alpha^2 v^2 / D(x)^2. The exact two-level cluster function for this transition interpolates smoothly between GOE and GUE results. The transition is sharp at alpha=0 for N=infinity. The GSE-to-GUE transition is also solved exactly. Applications include upper bounds on TRI-breaking nuclear interactions and Aharonov-Bohm chaotic billiards.

### Section 12: Conductance Fluctuations in Mesoscopic Systems

Using circular ensembles for the scattering matrix S, the joint probability distribution of transmission eigenvalues is derived. The Landauer formula g = sum T_j gives the dimensionless conductance, with universal conductance fluctuations var(g) = 1/(8*beta) for equal-channel quantum dots. The Buttiker formula gives shot-noise power. The DMPK equation for disordered nanowires gives var(g) = 2/(15*beta).

### Section 13: Finite Range Coulomb Gas Models

The finite-range Coulomb gas (FRCG) models generalize RMT by restricting pairwise interactions to range d. For d=0 one recovers Poisson; for d=1 exact results are given; for general d a mean-field approximation with xi = beta*d + 1 works well. FRCG models describe the spectra of QKR with d = alpha^2/N.

### Section 14: Wishart Ensembles

Wishart matrices H = AA^dagger have eigenvalue distributions of Jacobi type. Applications include multivariate time series in economics, biology, communication theory, and disordered systems.

## Key Results

1. **Dyson's threefold way**: Classification of random matrices into GOE (beta=1), GUE (beta=2), GSE (beta=4) based on time-reversal and space-rotation symmetries
2. **Wigner semicircle law**: Average density of eigenvalues for Gaussian ensembles
3. **Universal spectral fluctuations**: Two-level cluster function, number variance, and spacing distributions are universal within each symmetry class
4. **Level repulsion**: p_0(s) ~ s^beta for small s in random matrix ensembles, contrasting with level clustering in Poisson ensembles
5. **Spectral rigidity**: Sigma^2(r) ~ (2/(beta*pi^2)) ln r for random matrix ensembles, versus Sigma^2(r) = r for Poisson
6. **Porter-Thomas distribution**: Universal eigenvector component distribution, confirmed by nuclear data
7. **BGS conjecture**: Quantum chaotic systems follow random matrix statistics; integrable systems follow Poisson statistics
8. **Universal conductance fluctuations**: var(g) = 1/(8*beta) for quantum dots, var(g) = 2/(15*beta) for nanowires
9. **GOE-GUE transition**: Exact solution with transition parameter Lambda, applicable to TRI-breaking systems
10. **FRCG-QKR correspondence**: d = alpha^2/N connects finite-range Coulomb gas to quantum kicked rotor spectra

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Matrix element jpd | $P(A) = C \exp(-\beta \operatorname{tr} V(A))$ | Eq. (1) |
| Eigenvalue jpd | $p(x_1,\ldots,x_N) = C' \prod_{j<k} \lvert x_j - x_k\rvert^\beta \prod_{j=1}^N e^{-\beta V(x_j)}$ | Eq. (4) |
| Wigner semicircle | $\bar{\rho}(x) = \frac{2\sqrt{R^2-x^2}}{\pi R^2}, \quad R^2 = 4\beta v^2 N$ | Eq. (5) |
| Unfolding function | $F(\zeta) = N \int^\zeta \bar{\rho}(\zeta')\,d\zeta'$ | Eq. (7) |
| Two-level cluster (GUE) | $Y_2(r) = \left(\frac{\sin\pi r}{\pi r}\right)^2$ | Eq. (12) |
| Number variance | $\Sigma^2(r) = r - 2\int_0^r (r-s) Y_2(s)\,ds$ | Eq. (15) |
| Number variance (log) | $\Sigma^2(r) = \frac{2}{\beta\pi^2}\ln r + C_\beta$ | Eq. (16) |
| Wigner surmise (GOE) | $p_0(s) = \frac{\pi}{2} s \exp\left(-\frac{\pi}{4}s^2\right)$ | Eq. (20) |
| Wigner surmise (GUE) | $p_0(s) = \frac{32}{\pi^2} s^2 \exp\left(-\frac{4}{\pi}s^2\right)$ | Eq. (21) |
| Wigner surmise (GSE) | $p_0(s) = \frac{2^{18}}{3^6\pi^3} s^4 \exp\left(-\frac{64}{9\pi}s^2\right)$ | Eq. (22) |
| Delta_3 statistic | $\Delta_3(r) = \frac{1}{r}\min_{A,B}\int_{\xi_0}^{\xi_0+r}[N(x)-Ax-B]^2\,dx$ | Eq. (24) |
| Eigenvector distribution | $f_\beta(w) = \frac{(\beta/2)^{\beta/2}}{\Gamma(\beta/2)} w^{\beta/2-1}\exp(-\beta w/2)$ | Eq. (37) |
| Porter-Thomas | $f_1(w) = \frac{1}{\sqrt{2\pi}} w^{-1/2}\exp(-w/2)$ | Eq. (38) |
| Kicked rotor Hamiltonian | $H = \frac{p^2}{2} + V(\phi)\sum_{n=-\infty}^{\infty}\delta(t-n)$ | Eq. (44) |
| GOE-GUE transition | $H_\alpha = H^{(S)} + i\alpha H^{(A)}$ | Eq. (53) |
| Transition cluster function | $Y_2(r,\Lambda) = \left(\frac{\sin\pi r}{\pi r}\right)^2 - \frac{1}{\pi^2}\int_0^\pi dx\,x\sin(xr)e^{2\Lambda x^2}\int_\pi^\infty dy\frac{\sin(yr)}{y}e^{-2\Lambda y^2}$ | Eq. (55) |
| Transition parameter | $\Lambda = \alpha^2 v^2/(D(x))^2$ | Eq. (56) |
| Landauer formula | $g = \sum_{j=1}^N T_j$ | Eq. (65) |
| UCF variance | $\operatorname{var}(g) = \frac{2N_1^2 N_2^2}{\beta N_s^4} \xrightarrow{N_1=N_2} \frac{1}{8\beta}$ | Eq. (67) |
| FRCG number variance | $\Sigma^2(r) = \frac{r}{\xi} + \frac{\xi^2-1}{6\xi^2}, \quad \xi = \beta d + 1$ | Eq. (77) |

## Relevance to Phonon-Exflation

The phonon-exflation framework's BCS Fock space has been shown to be integrable (the Ordered Veil), predicting Poisson-class level statistics rather than Wigner-Dyson. This paper provides the complete theoretical foundation for that diagnostic: the BGS conjecture (Sec. 6) states that chaotic quantum systems follow GOE/GUE, while integrable systems follow Poisson (Sec. 7, Berry-Tabor). The number variance Sigma^2(r) and nearest-neighbor spacing p_0(s) are the primary tools used in the project's spectral diagnostics (e.g., s61_level_spacing.py). The transition ensembles (Sec. 11) are relevant if the BCS transit partially breaks integrability, as the GOE-GUE transition parameter Lambda would quantify the degree of symmetry breaking in the M4 x SU(3) fiber.
