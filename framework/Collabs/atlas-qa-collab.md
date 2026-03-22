# Atlas Collaborative Review: Quantum Acoustics Perspective

**Author**: Quantum Acoustics Theorist
**Date**: 2026-03-20
**Scope**: Full project atlas (Sessions 1-51), read through the acoustic lens
**Input**: D00 (index), D01 (timeline), D03 (equations), D05 (walls/doors/windows), D08 (open questions), QA index (28 papers)

---

## 1. The Correct Acoustic Model of the Fabric

The atlas records a 41-session blind spot (S41 discovery): all computations prior to Session 41 treated a single isolated SU(3) crystal. The fabric -- the spatially extended, interconnected network of 32-cell tessellated domains on T^2 -- was never the object of computation. From the acoustic perspective, the first question is: what IS the fabric, and what is the correct model for sound propagation through it?

The answer is not a phononic crystal in the standard sense.

A conventional phononic crystal (Paper 13, Jin 2024) has a periodic arrangement of scatterers in a host medium. The Bragg condition lambda = 2a/n produces bandgaps at frequencies set by the lattice constant and impedance contrast. SU(3) under Jensen deformation satisfies several phononic crystal criteria: Bloch-like modes (Peter-Weyl), band structure (D_K eigenvalues organized by Casimir), van Hove singularities, and a spectral gap. But it violates the central one: periodicity. The no-Umklapp theorem (S41) proves that the Peter-Weyl "lattice" is infinite and non-periodic -- it is the representation ring of SU(3), not a spatial lattice. Reciprocal lattice vectors do not exist, so Bragg scattering in the conventional sense does not occur within a single fiber.

The fabric introduces genuine spatial periodicity through the Z_3 tessellation on T^2. The 32-cell structure has lattice constant a ~ M_KK^{-1}, impedance contrast eta = Z_wall/Z_bulk = 1/2 (topologically quantized by Z_3 winding, S49 W1-C), and sound speed c_BdG = 0.751 M_KK. This IS a phononic crystal -- but not in representation space. It is a phononic crystal in position space on the torus, with each cell containing an SU(3) fiber as an internal resonator.

The correct acoustic model is therefore a **phononic metamaterial with sub-wavelength resonant inclusions**:

- **Host medium**: The 4D M^4 base manifold, with the Goldstone phase phi(x) as the propagating acoustic degree of freedom.
- **Inclusions**: Each tessellation cell on T^2 contains an SU(3) fiber with 8 BCS modes (internal resonances at 0.800+ M_KK) and 111 subsonic acoustic cavities (S49 W1-J).
- **Coupling**: The Josephson coupling J_ij connects neighboring cells. J_C2 = 0.933 dominates; J_su2 = 0.059, J_u1 = 0.038 are 16-25x weaker (S47 RHOS-TENSOR-47). This extreme anisotropy means the C^2 direction is acoustically stiff while the su(2) and u(1) directions are acoustically soft.
- **Propagating mode**: The Goldstone (U(1)_7 phase) with dispersion omega^2 = c^2 K^2 + m_G^2, where m_G = 0.070 M_KK (Leggett dipolar, S49).

The acoustic parameters of the fabric, collected from computations across S41-S51:

| Parameter | Value | Source | Acoustic interpretation |
|:----------|:------|:-------|:-----------------------|
| Lattice constant a | ~ M_KK^{-1} | S41 tessellation | Phononic crystal period |
| Impedance contrast eta | 1/2 (exact, Z_3) | S49 W1-C | Bragg gap driver |
| Sound speed c_BdG | 0.751 M_KK | S37 (analog) | Propagation velocity (30% uncertain) |
| Leggett mass m_G | 0.070 M_KK | S49 W1-S | Optical phonon frequency |
| Bragg gap | O(1) M_KK | S49 W1-C | Bandgap from Z_3 walls |
| Cavity count | 111 (disconnected) | S49 W1-J | Local resonators |
| Lowest cavity mode | 0.800 M_KK | S49 W1-J | First internal resonance |
| Cavity Q | ~ exp(23) | S49 W1-J | Perfect acoustic confinement |
| Leggett Q | 670,000 | S50 W1-D | Sub-gap collective mode |
| Stiffness anisotropy | 24x (C^2 vs u(1)) | S47 RHOS-TENSOR | Bianchi I acoustic geometry |
| Eikonal breakdown area | 78% of T^2 | S49 W1-G | WKB failure (not horizon) |

This model explains several structural results simultaneously. The zero-mode protection (W10) is the statement that the Goldstone is a sub-wavelength mode (lambda_G/R_fiber = 68, deep Rayleigh regime) that sees only the spatial average of the internal structure. The alpha_s = n_s^2 - 1 identity (W7) is the statement that a single acoustic branch on a Josephson lattice has K^2 dispersion with no free shape parameter. The Bragg gap at O(M_KK) is the standard phononic crystal gap from the Z_3 impedance contrast. The 170x mass problem is the mismatch between the Leggett resonance frequency and the required effective mass at K_pivot.

---

## 2. Local Resonances vs. Propagating Modes

The distinction between local resonances and propagating modes is the central acoustic diagnostic of the framework's current state.

**Propagating modes** on the fabric: The Goldstone (K^2 branch, protected by Goldstone theorem), the SA correlator (sum of Casimir poles with 110% spread, Door 3), and hypothetical second-sound modes. These carry information across the fabric and determine the CMB power spectrum. Their dispersion relations are the equations that must produce n_s = 0.965.

**Local resonances** within each cell: The 8 BCS quasiparticle modes (M* = 0.990 to 2.228 M_KK), the 111 acoustic cavity modes (lowest at 0.800 M_KK, Q ~ exp(23)), and the Leggett modes (0.070 and 0.107 M_KK, Q = 670,000). These are confined to individual cells and do not propagate. They modify the effective medium parameters seen by the propagating modes.

The S50-S51 investigation tested whether local resonances could renormalize the propagating Goldstone mass from 0.070 to the required ~12 M_KK. Five coupling mechanisms were evaluated (S51 W1-B LOCAL-RESONANCE-51):

| Mechanism | m_eff (M_KK) | Status |
|:----------|:-------------|:-------|
| Texture Born scattering | 0.070 | KILLED (zero-mode orthogonality, all Born orders) |
| Cubic anharmonic | 0.070 | KILLED (Ward identity cancels tadpole exactly) |
| Parametric (epsilon^2 J_eff) | 0.070 | Negligible (g^2 = 4e-5) |
| BCS 4-phonon vertex | 0.070 | Negligible (g^2 = 4e-3) |
| Zero-point parametric | 2.45 | Dominant but 5x short |

The zero-point parametric mechanism -- where cavity zero-point fluctuations modulate the sound speed through d^2c/dphi^2 = -c_BdG/8 -- is the sole surviving local-resonance contribution. It circumvents zero-mode protection because it operates through a medium property (the sound speed depends on the phase quadratically), not through a potential (which the zero-mode wavefunction averages to zero). This is acoustically correct: parametric modulation of the wave speed by a sub-wavelength oscillator IS the mechanism behind metamaterial effective mass enhancement (Paper 13, Section 4).

But the shortfall of 5x (m_eff = 2.45 vs target [8, 16]) and the filling fraction paradox (F = 37.9, meaning cavities cover the entire torus, invalidating the effective-medium picture) together close this route. The fabric is not a dilute suspension of resonators in a host -- it is a densely packed mosaic of resonant cells with no "background" medium. Effective-medium theory requires F << 1. Here F >> 1.

The Fano resonance route was pre-closed (S50 Section 3.3): q = 0 because the direct Goldstone-to-KK coupling vanishes exactly (zero-mode protection), leaving only a symmetric Lorentzian dip with no anomalous dispersion.

**Structural conclusion**: Local resonances within the SU(3) fiber cannot bridge the 170x mass gap. The gap between Leggett scale (0.070 M_KK) and the required scale (12 M_KK) is an acoustic desert: no propagating modes, no resonant coupling mechanisms, and no effective-medium enhancement survives the structural obstructions. The mass problem is not solvable within sub-wavelength metamaterial physics.

---

## 3. The 0D Acoustic Limit

The framework operates in a regime where conventional acoustic concepts break down: L/xi_GL = 0.031 (S37), meaning the pairing coherence length is 32x larger than the system. There are 8 active modes and N_pair = 1. This is the zero-dimensional limit of BCS theory.

What does "sound" mean in 0D? The S51 CROSSOVER-SOUND-51 computation confronted this directly. The Anderson-Bogoliubov sound speed c_AB = v_F/sqrt(3) was never a derived quantity -- it was an analog identification borrowed from 3D BCS (Volovik 2003, Paper 03). In a system with no Fermi surface, no spatial dispersion, and no propagating waves, c_AB is a dimensional estimate, not a velocity.

The physically computable 0D collective excitation is the Giant Pair Vibration: omega_GPV = 0.792 M_KK, a discrete oscillation frequency of the pair field. It is the 0D descendant of the Anderson-Bogoliubov mode. The numerical coincidence c_BdG = 0.751 vs omega_GPV = 0.792 (5.5% difference) reflects dimensional analysis, not a derivation. This 5.5% is the irreducible uncertainty in the analog mapping from 0D pair oscillation to propagating sound.

The BEC-BCS crossover compounds this uncertainty. At g*N(E_F) = 2.18, the framework sits at 1/(k_F a) = 0.292 on the BEC side of unitarity (S37: E_vac/E_cond = 28.8, fluctuation-dominated by 29x). The 3D mean-field crossover predicts c_crossover/c_BCS = 1.305 (+30.5%), but at unitarity, QMC gives the Bertsch parameter xi_B = 0.370, corresponding to c/c_BCS = 0.608 -- a 39% DECREASE. The mean-field gets the sign wrong. With the framework fluctuation ratio of 29x, the mean-field is quantitatively meaningless.

The honest acoustic assessment: the framework has an oscillation frequency (omega_GPV = 0.792 M_KK) and a Josephson coupling network that propagates phase disturbances across the fabric. The "sound speed" entering the K_pivot mapping is some combination of omega_GPV, the Josephson coupling J_ij, and the lattice geometry -- but NO rigorous derivation connects these to a single number c_fabric. The prior c_BdG = 0.751 carries a systematic uncertainty of at least 30%, set by the BEC-BCS crossover sign ambiguity and the 0D-to-propagating extrapolation.

This uncertainty propagates directly to the EFOLD-MAPPING-52 master gate (Q1 in D08). The K_pivot mapping is K_fabric = k_CMB * exp(N_total) / M_KK. At fixed N_total, a 30% uncertainty in c_fabric translates to a 30% uncertainty in K_pivot, which shifts the n_s prediction by delta_n_s ~ 0.04 (from O-Z sensitivity). This is the same order as the entire viable window identified in S51 (n_s = 0.965 requires beta > 0.9 at K < K* = 0.087 M_KK). The sound speed uncertainty is load-bearing for the framework's sole surviving cosmological prediction.

The 0D limit has a second consequence that the atlas does not fully acknowledge. The pair creation during transit (S38: 59.8 quasiparticle pairs, Parker-type) decomposes by branch: B2 dominates at 93.3% because the van Hove DOS enhancement concentrates pair creation in the flat band. The 3-component Landau-Zener formula reproduces the full Bogoliubov calculation to 0.04% (S49 W1-M). This factorization is the acoustic statement that each branch creates pairs independently -- the analog of parametric amplification being strongest at the impedance maximum. But "parametric amplification" in 0D is a time-dependent oscillation of the gap parameter, not a spatially propagating acoustic instability. The distinction matters for the BAO imprint: the primordial power spectrum is set by the 0D pair creation spectrum (a function of mode indices, not wavevectors), and the translation to a spatial power spectrum requires the fabric's Josephson network to imprint spatial correlations on an initially spatially-uncorrelated signal.

---

## 4. First-Sound BAO Imprint (Never Computed)

The S49 wayforward (item 13) assigned FIRST-SOUND-BAO-50 to the Quantum Acoustics agent. It was classified as Tier 4 and never executed through S51. The atlas records it as CF-equivalent status -- a carry-forward that risks being lost.

The physics is straightforward. In standard LCDM, BAO peaks arise from acoustic oscillations of the photon-baryon fluid before decoupling. The framework's fabric, being a phononic crystal with a physical sound speed and lattice constant, would imprint its own acoustic signature. The S44 first-sound computation found:

- Secondary ring at r_1 = 325 Mpc with A_FS/A_BAO = 0.204
- Sound speed u_2 = c/sqrt(3) (from the SU(3) fiber's conformal properties)
- Fisher SNR = 0.16 with DESI DR2, requiring V_eff = 8800 Gpc^3 for 3-sigma detection

The first-sound imprint is a zero-parameter prediction: the ring position is set by u_2 and the decoupling epoch, the amplitude by the coupling between the fabric's internal modes and the photon-baryon fluid. Unlike n_s (which depends on the unresolved K_pivot mapping) and w_0 (which is triple-locked at -1 and observationally excluded at -0.509), the BAO imprint is KINEMATIC -- set by speed ratios, immune to coupling constant uncertainties.

The open acoustic question is directional anisotropy. The Josephson coupling tensor is 24x anisotropic (rho_s(C^2) = 7.96, rho_s(u(1)) = 0.34, S47). If the BAO ring inherits this anisotropy, the detection signature shifts from a spherical shell in correlation space to an oblate ellipsoid. Anisotropic BAO rings are not predicted by any standard cosmological model. The signal would be small (0.204 of the primary BAO) but structurally distinct.

The computation requires: (1) the fabric sound speed tensor c_ij = sqrt(J_ij / rho_s_j) along each coupling direction, (2) the Boltzmann transfer function for the coupled Goldstone-photon system at recombination, (3) the correlation function xi(r, theta) with angular dependence from the anisotropic sound speed. This is a multi-day computation that builds on S47 (stiffness tensor) and S44 (first-sound estimate). Its absence from S50-S51 is a missed opportunity -- it is the one acoustic observable where the framework makes a distinct prediction from LCDM without relying on the K_pivot mapping.

---

## 5. The Acoustic Metric on the Fabric

The atlas records two results about acoustic metrics, and one retraction.

**T_acoustic/T_Gibbs = 0.993** (Door 7, S40). The Barcelo acoustic-metric temperature computed from the BdG sound speed on the tessellation fabric matches the BCS Gibbs temperature to 0.7%, with zero free parameters. This is a self-consistency check: the acoustic metric temperature (determined by the surface gravity at the "horizon" of the expanding modulus) agrees with the thermodynamic temperature (determined by the BCS gap equation). The agreement is non-trivial because the two quantities are computed from different data (BdG spectrum vs. Gibbs ensemble).

**Analog horizon RETRACTED** (S49 W1-G). The S48 claim of analog trapped surfaces on T^2 was retracted because the computation used |grad(|Delta|)| (amplitude gradient) instead of grad(phi) (phase gradient). The BCS ground state has phi = 0 everywhere -- no superflow, no ergoregion, no horizon. The Mach field retains meaning as a WKB validity diagnostic: 78% of T^2 has eikonal breakdown where geometric optics fails and phonons scatter strongly off the condensate texture. But scattering is not horizon physics.

What acoustic metric DOES exist on the fabric? The honest answer: the Unruh-Barcelo acoustic metric requires a flowing medium with a sound speed. The fabric has a sound speed (c_BdG or omega_GPV, with 30% uncertainty), but the "flow" is the temporal evolution of the modulus tau(t), not a spatial flow on T^2. The acoustic metric is therefore a cosmological one -- the analog of an FRW metric, not a Schwarzschild metric:

ds^2_acoustic = -(c_BdG^2 - v_mod^2) dt^2 + (fabric metric)_ij dx^i dx^j

where v_mod = dtau/dt is the "velocity" of the modulus through the internal geometry. The S40 Hawking temperature corresponds to the surface gravity of this cosmological acoustic metric at the transit. The retracted analog horizon was an attempt to find a Schwarzschild-like feature on T^2 within a single time-slice -- but the framework's acoustic geometry is inherently time-dependent (FRW-like), not stationary (Schwarzschild-like).

The fabric metric (fabric metric)_ij inherits the 24x anisotropy of the Josephson coupling tensor. The acoustic line element on the fabric is NOT isotropic. Sound propagates 4.8x faster in the C^2 direction than in the u(1) direction (c_ij = sqrt(J_ij/rho_s_j)). This is the acoustic analog of a Bianchi I cosmology -- an anisotropic but homogeneous expansion. The 4D observer would see this as anisotropic correlation functions in the CMB and LSS, at a level set by the Josephson anisotropy ratio.

No computation has constructed the full 4D acoustic metric from the fabric data. This requires: the modulus equation of motion (Q13 in D08), the fabric sound speed tensor (from S47), the Josephson coupling network topology (from S49), and the tessellation geometry (from S41). Each ingredient exists separately. The synthesis does not.

The absence is consequential. The S40 Hawking temperature agreement (0.7%) was computed using a single isotropic sound speed c_BdG = 0.751. The true fabric sound speed is a tensor with three eigenvalues differing by up to 4.8x. The corrected Hawking temperature depends on the geometric mean of the three sound speeds (by the Unruh formula generalized to anisotropic media, Barcelo-Liberati-Visser 2011, Paper 02), which differs from the isotropic estimate by a factor of (c_C2 * c_su2 * c_u1)^{1/3} / c_BdG. Whether the 0.7% agreement survives this correction is uncomputed. It could easily become a 10-50% disagreement, converting Door 7 from a self-consistency check to a structural tension.

Similarly, the Parker-type pair creation rate (S38) depends on the acoustic metric's time-dependence through the Bogoliubov coefficients. In an anisotropic acoustic metric, different polarization modes (corresponding to different coupling directions) have different pair creation rates. The isotropic 59.8-pair prediction would split into direction-dependent contributions, potentially modifying the GGE relic spectrum and its downstream CDM predictions.

---

## Closing Assessment

The acoustic perspective on the atlas reveals a framework that has correctly identified phononic structures (Bloch modes, band gaps, van Hove singularities, Leggett collective modes, impedance matching) but operates in a regime where conventional acoustic intuition fails.

Three structural facts set the acoustic landscape:

1. **The 0D limit invalidates propagating-wave concepts within the fiber**. Sound speed, dispersion relation, and wavevector are borrowed from 3D analogs; the physical 0D observables are discrete oscillation frequencies (omega_GPV, omega_L1, omega_L2) and coupling constants (J_ij). The 30% sound speed uncertainty from the BEC-BCS crossover is load-bearing for EFOLD-MAPPING-52.

2. **Zero-mode protection is the dominant acoustic selection rule**. The Goldstone's constant wavefunction on T^2 makes it transparent to all position-diagonal perturbations (W10). This kills eikonal damping, texture scattering, Fano resonance, and local-resonance T-matrix contributions to all Born orders. Only medium-property coupling (d^2c/dphi^2) survives, and it falls 5x short.

3. **The fabric is acoustically anisotropic by 24x, and no isotropic acoustic model applies**. The Josephson stiffness ratio J_C2/J_u1 = 24.6 means the fabric has three distinct acoustic velocities. Every propagator, correlation function, and BAO prediction inherits this anisotropy. The isotropic O-Z model used through S50 is a zeroth-order approximation.

The one acoustic computation that could change the constraint landscape is the first-sound BAO imprint (FIRST-SOUND-BAO, unexecuted since S49). It is the sole acoustic observable where the framework makes a structurally distinct prediction from LCDM -- an anisotropic secondary ring at 325 Mpc, set by the fabric's physical sound speed tensor and Z_3 lattice geometry. Unlike n_s, it does not depend on the K_pivot mapping. Unlike w_0, it is not already excluded. It deserves priority in S52 alongside EFOLD-MAPPING-52.

Four specific acoustic computations, in priority order, would most constrain the framework:

| # | Computation | What it settles | Depends on |
|:--|:-----------|:----------------|:-----------|
| 1 | c_fabric from Josephson network dispersion | 30% sound speed uncertainty for EFOLD-MAPPING-52 | S47 J_ij, lattice topology |
| 2 | FIRST-SOUND-BAO with anisotropy | Zero-parameter kinematic prediction, distinct from LCDM | S44 estimate, S47 stiffness tensor |
| 3 | Full 4D acoustic metric construction | Whether fabric anisotropy produces observable Bianchi I signatures | Q13 (modulus EOM), S47, S49 |
| 4 | Primordial power spectrum from 0D pair creation + fabric imprint | How the spatially-uncorrelated 0D signal acquires spatial correlations | S38 pair spectrum, S47 J_ij network |

The acoustic perspective does not change the atlas verdict -- the framework's cosmological viability hinges on EFOLD-MAPPING-52. But it identifies a systematic uncertainty (the 30% sound speed) that is comparable to the viable window, and an observable (the anisotropic BAO ring) that the atlas has not promoted from carry-forward to decisive question.

---

*Compiled from: atlas D00, D01, D03, D05, D08; QA index (28 papers); S49 QA collab; S50 QA collab; S51 results (W1-B LOCAL-RESONANCE-51, W1-F CROSSOVER-SOUND-51); S49 wayforward. All structural claims traced to specific gate verdicts and wall attributions in the atlas.*
