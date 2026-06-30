# Evidence for violations of Weak Cosmic Censorship in black hole collisions in higher dimensions

**Author(s):** Tomas Andrade, Pau Figueras, Ulrich Sperhake
**Year:** 2020 (submitted), 2021 (v2)
**Journal:** Prepared for submission to JHEP
**arXiv:** 2011.03049
**Relevance:** MEDIUM

Note: Filename labels "Andrade_Emparan" but the actual authors are Andrade, Figueras, and Sperhake; Emparan is thanked in the acknowledgments.

---

## Abstract

We study collisions of boosted rotating black holes in D = 6 and 7 spacetime dimensions with a non-zero impact parameter. We find that there exists an open set of initial conditions such that the intermediate state of the collision is a black hole with a dumbbell-like horizon which is unstable to a local Gregory-Laflamme-type instability. We are able to provide convincing numerical evidence that the evolution of such an instability leads to a pinch off of the horizon in finite asymptotic time thus forming a naked singularity, as in similar unstable black holes. Since the black holes in the initial state are stable, this is the first genuinely generic evidence for the violation of the Weak Cosmic Censorship Conjecture in higher dimensional asymptotically flat spacetimes.

---

## Key Arguments and Derivations

### Motivation

The Weak Cosmic Censorship (WCC) Conjecture posits that all singularities formed in dynamical evolution must be hidden behind black hole horizons. Known counter-examples fall into two classes: (i) fine-tuned critical collapse, and (ii) "death by fragmentation" of elongated horizons. The Gregory-Laflamme (GL) instability of black strings (hep-th/9301052) drives the fragmentation class; numerical work has shown that unstable strings evolve into a fractal cascade of satellites joined by thin necks, with the neck thickness shrinking to zero in finite asymptotic time. All such studies start from unstable configurations, however, raising the question of whether naked-singularity formation is truly generic.

A proposal by Emparan and collaborators, via the large-D effective theory, is that grazing collisions of stable rotating black holes in D >= 6 should generically form elongated intermediate horizons (because bar-mode instabilities of rotating BHs exist in D >= 6), triggering local GL instabilities with no mechanism to re-round the horizon, since radiation is exponentially suppressed at large D. This paper tests that proposal with full numerical relativity in D = 6 and D = 7.

### Numerical setup

The authors solve vacuum Einstein equations in D = 6, 7 using the CCZ4 formulation in GRChombo, with dynamical dimensionality reduced to 3+1 via an SO(D-3) symmetry imposed through the modified cartoon method. Initial data are two superposed boosted Myers-Perry (MP) BHs in Kerr-Schild coordinates, with impact parameter b = 2 y_0, collision velocity v along x-hat, and aligned intrinsic spin a along z-hat. Moving-puncture gauge (1+log slicing) is used; apparent horizons are tracked via level sets of the conformal factor chi = (det gamma)^{-1/3}, with chi = 0.6 as a proxy for the AH in string-like regions and chi = 0.7 for spherical bulges.

### Validation of chi-contours as AH proxy

The authors introduce a normalized Kretschmann invariant K-tilde = (1/240) R^{alpha beta mu nu} R_{alpha beta mu nu} W(chi_0)^4, where W is the proper width of the chi = chi_0 contour. In 7D, K-tilde = 1 on the horizon of a stationary black string and K-tilde = 5/2 on a 7D Schwarzschild horizon. By comparing these reference values to the Kretschmann scalar along chi-contours during evolution, they verify that: (a) in neck regions, the chi = 0.6 contour accurately tracks the quasi-stationary black string horizon; (b) in bulge regions, the chi = 0.7 contour accurately tracks the Schwarzschild-like horizon. The insensitivity to the specific chi value in the neck region is attributed to steep near-horizon metric gradients at large D.

### Results in D = 7

With initial parameters v = 0.5, a = 0.7, y_0 = 1.1, x_0 = 10 (well within the MP stability bound a_max = 0.74), the collision forms a dumbbell-shaped common horizon within Delta t ~ 7. The neck thins, and local GL instabilities produce two generations of satellites plus the onset of a third; width/length ratio falls well below the critical value r_{GL,7D} ~ 0.5. The Kretschmann scalar diverges as ~W^{-4} as the neck width shrinks to zero.

Gravitational waves are extracted via projection of the Weyl matrix Omega'_{AB} onto S^5 scalar-derived tensor harmonics. Two peaks appear: the first at t - t_merger ~ 30 from the initial merger, and a second (largest) peak at t - t_merger ~ 37.5 when the dumbbell stops rotating and its arms begin expanding. The total radiated energy up through the second peak is only ~0.01% of the ADM mass, far too little to re-round the horizon.

### Results in D = 6

Two runs at {v = 0.5, a = 0.6, b = 2.5} and {v = 0.45, a = 0.7, b = 2.5}, both with spins within a_max = 0.73, exhibit qualitatively identical behavior: dumbbell formation, thinning neck, GL cascade, well below r_{GL,6D} ~ 0.4. Neck width/length ratios fall to ~0.02-0.04 during the evolution.

### Interpretation and WCC violation

The violation is "generic" in the sense that no fine-tuning of initial conditions is required -- an open set of stable MP initial configurations leads to naked-singularity formation. In the "mild violation" language of Wald, the regions becoming Planckian are small compared to the overall horizon scale, so any quantum resolution (e.g., hydrodynamic droplet analogy) perturbs the classical dynamics only weakly. The letter-of-WCC is violated; the spirit is largely preserved. The result is consistent with the large-D effective theory predictions and demonstrates that even in finite D = 6, 7, the GL-driven fragmentation mechanism operates.

## Key Results

1. Numerical simulations in D = 6 and D = 7 of grazing collisions of stable Myers-Perry black holes produce a dumbbell-shaped common horizon which develops a local GL instability and fragments in finite asymptotic time.
2. No fine-tuning of initial parameters is required; an open set of initial conditions (v, a, b) exhibits this behavior.
3. The Kretschmann scalar in neck regions diverges as W^{-4}, where W is the proper neck width, matching the scaling observed in black-string and ultra-spinning MP collapse.
4. Gravitational radiation is doubly peaked (merger + dumbbell arm expansion); total radiated energy through the dominant peak is ~0.01% of the ADM mass in D = 7.
5. The chi = 0.6 (string regions) and chi = 0.7 (bulge regions) level sets of the conformal factor provide accurate proxies for the apparent horizon in higher-D simulations.
6. The critical GL ratio (width/length) is ~0.5 in 7D and ~0.4 in 6D; observed ratios in the cascade reach 0.02-0.04, confirming the strings are deep in the unstable regime.
7. Provides first genuinely generic evidence for Weak Cosmic Censorship violation in higher-dimensional asymptotically flat spacetimes.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Conformal factor | chi = (det gamma)^{-1/3} | Sec. 2 |
| Normalized Kretschmann | K-tilde = (1/240) R^{alpha beta mu nu} R_{alpha beta mu nu} W(chi_0)^4 | Eq. 3.1 |
| Energy loss | dE/dt = -lim_{r->infty} (r^{d-2}/(8 pi)) Int_{S^{d-2}} [Int^u_{-infty} Omega'_{AB}(u-hat) du-hat]^2 domega | Eq. 4.1 |
| Weyl harmonic projection | Omega'_{L...} = lim_{r->infty} r^{(D-2)/2} Int dOmega_{(n)} Y^{(A)(B)*}_{L...} Omega'_{(A)(B)} | Eq. B.1 |
| Kerr-Schild metric | g_{mu nu} = eta_{mu nu} + f(x) k_mu k_nu | Eq. A.1 |
| MP f function | f = mu r / (Pi(r) F(r, x^i)) | Eq. A.2 |
| MP Pi function | Pi(r) = prod_i^{s(D)} (r^2 + a_i^2) | Eq. A.3 |
| MP F function | F = 1 - sum_i^{s(D)} a_i^2 (X_i^2 + Y_i^2)/(r^2 + a_i^2) | Eq. A.4 |
| Mass formula | M = (D-2) Omega_{D-2} mu / (16 pi G), J = 2 M a / (D-2) | Eq. A.8 |
| Sphere volume | Omega_{D-2} = 2 pi^{(D-1)/2} / Gamma((D-1)/2) | Eq. A.9 |
| S^5 metric | ds^2 = dchi^2 + sin^2(chi) dphi^2 + cos^2(chi) dOmega^2_{(3)} | Eq. B.2 |
| Scalar harmonic | Y^{l5, m, l3, ...} = N e^{i m phi} (sin chi)^{|m|} (cos chi)^{l3} Y^{l3} 2F1(l3+|m|-k, k+3/2, l3+2; cos^2 chi) | Eq. B.3 |
| Regularity constraint | l5 = 2k - (l3 + |m|) | Eq. B.4 |
| Scalar-derived tensor harmonic | S^{ln,...,l1}_{ab} = [sqrt(n)/sqrt((n-1)(ln-1)(ln+n))] (nabla_a S^{...}_b + [sqrt(ln(ln+n-1))/n] g_{ab} S^{...}) | Eq. B.5 |

## Relevance to Phonon-Exflation

This paper provides the direct numerical-relativity validation that Gregory-Laflamme instabilities generically drive horizon fragmentation in D = 6, 7, the same dimensional range that includes the framework's M4 x SU(3) (effectively D = 10 for the full substrate but with significant analogies at D = 7 when SU(3) partial compactifications are considered). The finding that no fine-tuning is needed -- an open set of stable initial conditions generates fragmentation -- supports the framework's claim that the fold transition at tau ~ 0.19 is a structurally generic first-order phase transition rather than an accidental trajectory. The W^{-4} divergence of the Kretschmann scalar near the pinch off is the direct GR-language counterpart of the framework's GL-CUBIC-36 reinterpretation of the fold as a 2nd-order Z_2 transition ("wall = kink, not vortex"): whereas this paper stays in the GR container-thinking picture and describes the neck as "pinching off," the substrate description says that the spectral weight of the Jensen-deformed fiber reorganizes through a Z_2 kink, with no true naked singularity and no WCC violation in the substrate picture. The GR-level naked singularity is an emergent artifact of container thinking; in the substrate picture, the "Planckian region" corresponds to the locus where the spectral action gradient dS/dtau peaks and the framework's NEC audit expects NEC violation at tau ~ 0.285. The paper's observation that radiation is strongly suppressed (~0.01% of ADM mass) parallels the framework's acoustic white hole picture: very little energy leaks across the fold because the transit is supersonic (Mach 13.75) and causally disconnected.
