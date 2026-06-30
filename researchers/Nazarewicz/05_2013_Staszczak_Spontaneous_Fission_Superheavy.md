# Spontaneous Fission Modes and Lifetimes of Superheavy Elements in the Nuclear Density Functional Theory

**Author(s):** A. Staszczak, A. Baran, and W. Nazarewicz
**Year:** 2013 (submitted 2012)
**Journal:** Physical Review C 87, 024320 (2013)
**arXiv:** 1208.1215
**Relevance:** MEDIUM

---

## Abstract

Lifetimes of super-heavy (SH) nuclei are primarily governed by alpha decay and spontaneous fission (SF). Here we study the competing decay modes of even-even SH isotopes with $108 \leq Z \leq 126$ and $148 \leq N \leq 188$ using the state-of-the-art self-consistent nuclear density functional theory framework capable of describing the competition between nuclear attraction and electrostatic repulsion. The collective mass tensor of the fissioning superfluid nucleus is computed by means of the cranking approximation to the adiabatic time-dependent Hartree-Fock-Bogoliubov approach. Along the path to fission, our calculations allow for the simultaneous breaking of axial and space inversion symmetries; this may result in lowering SF lifetimes by more than seven orders of magnitude in some cases. We predict two competing SF modes: reflection-symmetric and reflection-asymmetric. The shortest-lived SH isotopes decay by SF; they are expected to lie in a narrow corridor formed by $^{280}$Hs, $^{284}$Fl, and $^{284}_{118}$Uuo that separates the regions of SH nuclei synthesized in "cold fusion" and "hot fusion" reactions. The region of long-lived SH nuclei is expected to be centered on $^{294}$Ds with a total half-life of $\sim 1.5$ days.

---

## Key Arguments and Derivations

### 1. Fission as Many-Body Tunneling

Fission is understood as many-body tunneling involving mean fields with different intrinsic symmetries. For SH nuclei, the theoretical tool is self-consistent nuclear DFT at the deformed HFB level. The advantage: proper treatment of the self-consistent interplay between long-ranged electrostatic repulsion and short-ranged nuclear attraction (Coulomb frustration).

### 2. Computational Framework

- Skyrme-HFB calculations using the symmetry-unrestricted DFT solver HFODD
- SkM* functional in the particle-hole channel
- Density-dependent mixed pairing interaction in the particle-particle channel
- Quasiparticle cutoff: 60 MeV in equivalent energy spectrum
- Pairing strengths: $V_{n0} = -268.9$ MeV fm$^3$, $V_{p0} = -332.5$ MeV fm$^3$ (fit to $^{252}$Fm gaps)
- Single-particle basis: 1140 stretched states from 26 major oscillator shells
- Collective coordinates: multipole moments $Q_{\lambda\mu}$ for elongation (20), reflection-asymmetry (30), triaxiality (22), and necking (40)

### 3. Action Integral and Penetrability

The potential energy: $V(Q_{20}) = E_{tot}(Q_{20}) - \text{ZPE}(Q_{20})$ where ZPE is the zero-point energy from the Gaussian overlap approximation. The collective ground state energy $E_0 = 0.7 \times \text{ZPE}(Q^{gs}_{20})$ -- the scaling factor 0.7 improves agreement with experimental SF half-lives in Fm isotopes (which vary by almost 20 decades). The WKB penetrability uses action integrals along static fission pathways with the perturbative HFB cranking quadrupole mass parameter $B_{20,20}(Q_{20})$.

### 4. Ground-State Classification

SH nuclei divide into three groups: (i) prolate-deformed ($Q_{20} \approx 30$ b) for $N \leq 170$; (ii) spherical for $N > 180$; (iii) weakly deformed, often triaxial, in between. Nuclei with $N > 180$ are most stable against SF with two-humped barriers.

### 5. Symmetry Breaking Effects

Triaxiality substantially reduces the inner barrier $E_A$. For the reflection-symmetric elongated fragment (sEF) pathway, triaxiality may also reduce the outer barrier $E_B$. The reflection-asymmetric elongated fragment (aEF) valley branches away from sEF at $Q_{20} > 80$ b. For nuclei with $A > 280$ and $Z > 108$, the outer barrier vanishes along aEF.

For $^{306}122$: the inner barrier is reduced by ~3 MeV by triaxiality, the outer barrier by ~1 MeV. Along aEF, the outer barrier vanishes altogether. The overall reduction of $T_{sf}$ from imposing axial symmetry to full symmetry-unrestricted: seven orders of magnitude ($10^{13.82}$s to $10^{6.22}$s).

### 6. Competition Between Fission Modes

The sEF mode dominates for Hs isotopes, SH nuclei with $A < 280$, and in a triangle defined by $^{290}$Ds, $^{298}$Fl, $^{298}$Ds. For the remaining nuclei, the asymmetric mode wins. The bimodal fission region ($|\log_{10}(T_{sEF}/T_{aEF})| < 0.3$) appears around $N = 188$.

### 7. Predicted Lifetimes

- Maximum $T_{sf} = 10^{7.76}$s for $^{298}$Fl
- Shortest SF half-lives (down to $10^{-10}$s) in a narrow corridor of fission instability
- Long-lived SH nuclei centered on $^{294}$Ds: total half-life $10^{5.13}$s ($\sim 1.5$ days)
- Alpha-decay half-lives estimated via the Viola-Seaborg expression

---

## Key Results

1. Imposing axial and/or space inversion symmetry overestimates SF half-lives by up to 7 orders of magnitude
2. Two competing SF modes exist: reflection-symmetric (sEF) and reflection-asymmetric (aEF)
3. The aEF mode prevails for $N \geq 166$; sEF for light SH nuclei and around $N \approx 188$
4. A narrow corridor of extreme fission instability separates cold-fusion and hot-fusion SH nuclei
5. The center of enhanced stability lies at $^{294}$Ds ($T_{1/2} \sim 1.5$ days)
6. The model reproduces the 20-decade variation of $T_{sf}$ in Fm isotopes
7. Barrier widths, not heights, determine the dominant SF mode in many cases

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Potential energy | $V(Q_{20}) = E_{tot}(Q_{20}) - \text{ZPE}(Q_{20})$ | Text, Sec. "Model" |
| Ground state energy | $E_0 = 0.7 \times \text{ZPE}(Q^{gs}_{20})$ | Text, Fig. 1 |
| Pairing strengths | $V_{n0} = -268.9$ MeV fm$^3$, $V_{p0} = -332.5$ MeV fm$^3$ | Text |
| Viola-Seaborg | Standard form with parameters from Parkhomenko & Sobiczewski (2005) | Ref. [45,46] |
| Quadrupole moments | $Q_{\lambda\mu}$ constrained for $\lambda\mu = 20, 30, 22, 40$ | Text |
| Cranking mass | $B_{20,20}(Q_{20})$ from perturbative HFB cranking | Text |

---

## Relevance to Phonon-Exflation

The fission problem provides an analog for the framework's geometric instability at the fold: the SU(3) fiber at the fold point faces a competition between the "nuclear attraction" (BCS pairing energy) and "Coulomb repulsion" (spectral action cost of deformation), just as SH nuclei balance these forces. The key methodological parallel is the many-body tunneling calculation via the collective action integral with WKB penetrability -- the framework's instanton gas (S_inst = 0.069) can be viewed as the analog of the SF action integral. The paper also demonstrates that symmetry breaking (triaxiality, reflection asymmetry) can reduce barrier penetration times by orders of magnitude -- relevant to the framework's question of whether the Jensen symmetry breaking $[iK_7, D_K] = 0$ opens new channels that modify the transit dynamics.
