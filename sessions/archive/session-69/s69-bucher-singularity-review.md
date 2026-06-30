# Review: Bucher et al. 2025 — Superluminal Phase Singularity Dynamics in Phonon-Polariton Ensembles

**Reviewer**: Landau Condensed-Matter Theorist
**Paper**: T. Bucher et al., "Superluminal Correlations in Ensembles of Optical Phase Singularities," arXiv:2509.17675 (2025)
**Session**: S69
**Date**: 2026-04-05

---

## Part 1: Paper Summary

### 1.1 What Was Measured

Bucher et al. achieve the first direct observation of the ultrafast dynamics of phase singularity ensembles in optical phonon-polariton (PhP) fields confined to hexagonal boron nitride (hBN) membranes. Using free-electron Ramsey imaging (FERI) in an ultrafast transmission electron microscope, they attain simultaneous spatial resolution of 20 nm (lambda_PhP / 30) and temporal resolution of 3 fs (T/8), resolving both sub-wavelength and sub-cycle dynamics.

The experiment tracks approximately 50 singularities per frame across 285 phase-resolved frames spanning 800+ fs. Phase singularities carry quantized topological charge +/-1 (2*pi phase winding), and annihilate only upon encountering a singularity of opposite charge.

### 1.2 Key Results

1. **Superluminal singularity velocities**: 29% of singularities exceed c, with mean velocity <v> = 3.12 x 10^8 m/s = 1.04 c. In free space, only 0.4% are superluminal (70x amplification by the hBN platform).

2. **Velocity distribution**: The measured P(|v|) matches the Berry-Dennis (2001) analytic prediction:

$$P_{\pm}(|v|) = \frac{8\pi^2 \langle v \rangle^2 |v|}{(\pi^2 |v|^2 + 4\langle v \rangle^2)^2} \tag{1}$$

This is a universal result for singularities in Gaussian random wave fields — it depends only on <v>.

3. **Mean velocity formula**: The average singularity velocity is set by the spectral width and velocity ratio:

$$\langle v \rangle = c \cdot \frac{\pi}{\sqrt{2}} \cdot \frac{\Delta k / k}{\sqrt{1 + (\Delta k / k)^2}} \tag{2}$$

where Delta_k / k = (v_ph / v_g) * (Delta_lambda / lambda_0). The slow group velocity of hBN PhPs (v_ph / v_g ~ 12) amplifies the effective spectral spread.

4. **Distance correlations**: g_{+|+}(R) and g_{+|-}(R) match the Gaussian random wave model — liquid-like short-range order with a correlation hole at R < lambda/2.

5. **Joint phase-space distribution P(v, R)**: First measurement of the full distance-velocity correlation. At small R, opposite-charge singularities show higher velocities (pre-annihilation acceleration). At large R, velocity distributions narrow.

6. **Universality**: The Gaussian random wave model matches experiment across all observables, confirming that the singularity statistics are universal features of multimode wave interference, independent of microscopic details.

### 1.3 Physical Mechanism for Superluminal Motion

Phase singularities are zeros of the complex field — points of zero intensity where the phase is undefined. They carry no energy or information. Their motion is a collective interference effect: as the constituent wave components evolve, the locus of destructive interference shifts. Near annihilation, phase continuity forces the spacetime trajectory of a +/- pair to form a continuous curve, requiring the singularity velocity to diverge at the annihilation point. This is a topological necessity, not a dynamical effect.

The v_ph / v_g amplification mechanism is the critical physics: in a dispersive medium where v_ph >> v_g, the wave components dephase rapidly in the lab frame while the envelope (energy) moves slowly. The singularity, being a zero of the total field, moves at the phase velocity scale, not the group velocity scale. This decoupling of singularity velocity from energy transport velocity is what enables the superluminal fraction to reach 29%.

---

## Part 2: Framework Connections

### 2.1 The Substrate as a Phononic Medium

In the phonon-exflation framework, the substrate IS a phononic medium. The internal geometry at each point is described by the Dirac operator D_K on Jensen-deformed SU(3), and physical excitations are phononic modes of this substrate — relay patterns propagating through the gauge connection between fibers (Landau paper 05, superfluidity; papers 22-23, GGE theory).

The GGE relic after the transit consists of n_pairs = 59.8 quasiparticle pairs produced by Parker pair production at the fold (tau = 0.190), with excitation probability P_exc = 1.000 exactly (S38). These pairs occupy 8 BCS modes (4 B2 + 1 B1 + 3 B3) on each of the N_cells = 32 Voronoi cells forming the CG(24) Cayley graph fabric.

The substrate has a well-defined sound speed hierarchy (S64 computation `s64_sound_speed.py`):

| Speed | Value (M_KK units) | Governs |
|:------|:-------------------|:--------|
| c_mod | 1.000 (exact) | Tensor perturbations, modulus propagation |
| c_BLV | 0.485 | Scalar perturbations, acoustic horizon |
| c_BA | 0.399 | BCS phase dynamics, GGE formation |
| c_Gold | 0.915 | Goldstone sound in fabric |
| c_Leggett | 0.019 | Leggett (DM) mode propagation |

The hierarchy c_mod > c_Gold > c_BLV > c_BA >> c_Leggett is the substrate analog of the multi-speed structure in superfluid 3He-B (S64, parent-child correspondence per project memory `project_3heb-inheritance.md`).

### 2.2 Mapping: Phase Singularity Charge <-> GGE Quasiparticle Topological Charge

**Bucher result**: Phase singularities carry charge +/-1, characterized by +/-2*pi phase winding. Higher charges are unstable.

**Framework counterpart**: The BCS quasiparticle excitations in the GGE relic carry charge conjugate to the U(1) phase of the order parameter. The Bogoliubov transformation at the fold produces quasiparticle-quashole pairs with opposite quantum numbers. The Leggett mode, which carries the dark matter, has Z_2 topological charge (S67 LEGGETT-GRAV-DECAY-67 PASS: Z_2 parity protects against single-mode gravitational decay, Gamma_single = 0 exactly).

The mapping is:

| Bucher (hBN) | Framework (substrate) |
|:-------------|:---------------------|
| Phase singularity charge +1 | Bogoliubov quasiparticle (excitation above BCS condensate) |
| Phase singularity charge -1 | Bogoliubov quasihole (conjugate excitation) |
| Higher charges unstable | Higher BCS excitations decay to single-pair states (S38 KZ) |
| Charge conservation in annihilation | Bogoliubov number conservation in integrable GGE |

The analogy is deeper than charge assignment. The BCS phase phi(x) on the fabric winds by 2*pi around each Abrikosov-type vortex in the condensate (Landau paper 13, Abrikosov 1957). The framework's BCS condensate on CG(24) supports precisely this kind of phase winding — but on a DISCRETE graph rather than a continuum. The discreteness of CG(24) (24 vertices, 72 edges, degree 6, diameter 3; bipartite even/odd permutations, S64 LOCAL-ENTANGLE-64 computation) quantizes the possible winding numbers and constrains the defect separation to integer multiples of the graph distance.

### 2.3 Mapping: Distance Correlations g(R) <-> GGE Spatial Correlations on CG(24)

**Bucher result**: Same-charge singularities exhibit g_{+|+}(R) with a correlation hole at R < lambda/2 and liquid-like short-range order. Opposite-charge singularities have enhanced g_{+|-}(R) at small R (attraction before annihilation).

**Framework counterpart**: The GGE on CG(24) has massive spatial correlations. The S64 LOCAL-ENTANGLE-64 computation found mutual information I(A:B) = 110.72 nats between even and odd sublattices, with per-band entanglement entropy S ~ 6.93-7.06 nats (84% of maximum). The bimodal occupation pattern n ~ {0, 1} arises because beta*J >> 1 (Josephson-dominated regime, J_C2 = 0.933 M_KK >> T_acoustic = 0.112 M_KK from canonical_constants.py).

The relevant spatial scales on CG(24) are:

- **Graph diameter**: d_max = 3 (maximum geodesic distance between any two vertices)
- **Characteristic distance**: The graph has Laplacian eigenvalues {0, 4, 6, 8, 12} with multiplicities {1, 9, 4, 9, 1}. The spectral gap lambda_1 = 4 corresponds to a correlation length xi_graph = 1/sqrt(lambda_1) = 0.5 in graph units.
- **Lattice spacing**: In physical units, each CG(24) cell has linear size ~ xi_BCS = 0.808 M_KK^{-1} (BCS coherence length from canonical_constants.py).

The correlation hole in g_{+|+}(R) at R < lambda/2 maps to the exclusion of same-charge excitations from the same graph vertex — a consequence of the Pauli exclusion principle operating within each BCS sector. Two Bogoliubov quasiparticles of the same type cannot occupy the same site. The liquid-like short-range order maps to the Josephson-mediated correlations between nearest neighbors on CG(24).

**Key distinction**: In Bucher's experiment, g(R) is measured in a 2D continuum. In the framework, correlations are defined on a DISCRETE graph with only 5 distinct distances (d = 0, 1, 2, 3 in graph metric). The Berry-Dennis Gaussian random wave model assumes a continuum — the framework must test whether a discrete-graph version of this model reproduces the observed GGE correlations.

### 2.4 Mapping: Velocity Distribution P(|v|) <-> GGE Excitation Velocity Distribution

**Bucher result**: The Berry-Dennis distribution Eq. (1) is universal for singularities in Gaussian random wave fields. The only parameter is the mean velocity <v>, which is determined by the wave field's spectral properties.

**Framework counterpart**: The GGE relic excitations propagate through the fabric at velocities determined by their dispersion relations. There are three relevant velocity classes:

1. **Goldstone (acoustic) excitations**: Propagate at c_Gold = 0.915 M_KK (massless, linear dispersion omega = c_Gold * k). These are the Nambu-Goldstone bosons of the broken U(1) symmetry.

2. **Bogoliubov (BA) excitations**: Propagate at c_BA = 0.399 M_KK. These are the Anderson-Bogoliubov sound modes of the BCS condensate. The S67 BA-LIFETIME-FABRIC-67 computation showed all 256 BA modes are overdamped (Q < 2), decaying in [3.8 x 10^{-42}, 3.3 x 10^{-41}] s — far faster than any cosmological timescale. BA modes are eliminated as DM candidates.

3. **Leggett excitations**: Propagate at c_Leggett = 0.019 M_KK. These are the inter-band coherence modes carrying DM. Quality factor Q = 18.6 (S66 LEGGETT-SPECTRAL-66 PASS), spectral weight Z = 0.972 — these are well-defined quasiparticles.

The Bucher velocity distribution Eq. (1) applies to each of these classes IF the corresponding wave field is well-described by a Gaussian random wave model. The GGE relic state, produced by an impulsive supersonic quench (Mach 13.75), is exactly the kind of multimode superposition where Gaussian random wave statistics should apply — the KZ mechanism (Landau paper 29, Zurek 1985) produces excitations with random phases across causally disconnected domains.

### 2.5 Mapping: v_ph / v_g Amplification <-> Acoustic/Optical Branch Velocity Ratios

**Bucher result**: The fraction of superluminal singularities scales with v_ph / v_g. In hBN, v_ph / v_g ~ 12 gives 29% superluminal. In free space, v_ph / v_g = 1 gives 0.4%.

**Framework counterpart**: The substrate has multiple velocity ratios that play the role of v_ph / v_g. The relevant ones are:

1. **Modulus-to-BLV ratio**: c_mod / c_BLV = 1.000 / 0.485 = 2.06. This is the ratio governing scalar perturbation singularities. It is the analog of v_ph / v_g for the spectral action wave field.

2. **BLV-to-BA ratio**: c_BLV / c_BA = 0.485 / 0.399 = 1.22. This governs singularities in the BCS condensate phase field.

3. **Goldstone-to-Leggett ratio**: c_Gold / c_Leggett = 0.915 / 0.019 = 48.2. This is the substrate analog of the hBN ratio v_ph / v_g ~ 12 — but 4x LARGER. If the Bucher amplification mechanism applies, the framework predicts an even larger fraction of "superluminal" singularities (relative to c_BLV or c_BA) in the Leggett channel.

4. **Fabric-to-Goldstone ratio**: c_fabric / c_Gold = 209.97 / 0.915 = 229.5. This extreme hierarchy converts through the BLV acoustic metric into the 2.72 acoustic e-folds of expansion.

The 229x hierarchy between c_fabric and c_Gold is the framework's most extreme v_ph / v_g ratio. By Bucher's amplification mechanism, singularities in the Goldstone channel would be "superluminal" relative to c_Gold with near-unit probability. This has physical content: it means the phase zeros of the Goldstone field reorganize at speeds far exceeding the energy transport velocity — the same physics as in hBN, but in the spectral action's internal space.

### 2.6 Mapping: Annihilation Dynamics <-> Pair Recombination in the GGE

**Bucher result**: Opposite-charge singularities accelerate to unbounded velocities before annihilation. The acceleration is a topological necessity from phase continuity. The pre-annihilation acceleration is visible in P(v, R) at small R.

**Framework counterpart**: In the GGE relic, pair annihilation is FORBIDDEN by integrability. The ordered veil theorem (S38) establishes that the GGE is permanent — the conserved quantities (Lagrange multipliers beta_k for each mode k) prevent thermalization to Gibbs equilibrium. The Richardson-Gaudin integrability of the pairing Hamiltonian (Landau paper 16, Richardson 1963; paper 17, Dukelsky et al. 2004) provides the exact conservation laws.

The S67 BA-LIFETIME-FABRIC-67 computation confirms this from the opposite direction: the BA modes that COULD mediate pair recombination are overdamped (Q < 2), decaying in 10^{-41} s. After these transients die, only the Leggett modes remain — and Leggett modes have Z_2 parity protection against single-mode decay (S67 LEGGETT-GRAV-DECAY-67 PASS).

This is the critical STRUCTURAL difference between the hBN experiment and the framework:

| Bucher (hBN) | Framework (substrate) |
|:-------------|:---------------------|
| Singularities annihilate freely | Pair recombination blocked by integrability |
| Steady-state density maintained by creation | GGE relic has fixed particle number |
| Continuous creation-annihilation dynamics | Frozen relic, no pair dynamics |
| Gaussian random wave model holds at all times | Gaussian statistics hold only at formation (KZ freeze-out) |

The framework predicts that the initial GGE formation (the impulsive quench through the fold) produces singularity ensembles obeying Berry-Dennis statistics. But unlike in hBN, these singularities cannot annihilate afterward. The velocity distribution is FROZEN at its formation-time value by integrability. This is a testable distinction.

### 2.7 Mapping: Superluminal Motion <-> Superluminal Phase Velocity Relative to c_BLV

**Bucher result**: 29% of singularities exceed c. This is not a violation of causality — singularities carry no energy or information.

**Framework counterpart**: The same physical mechanism operates in the substrate. The relevant "speed of light" for the substrate is c_BLV = 0.485 M_KK (not c_mod = 1, which governs tensor modes). Phase singularities in the GGE wave field can move superluminally relative to c_BLV without violating substrate causality, because they carry no substrate energy.

The acoustic white hole at the fold (supersonic transit at Mach 13.75) creates a causally disconnected pre-transit / post-transit structure. The GGE excitations on the post-transit side propagate at velocities bounded by c_BA = 0.399 for condensate modes and c_BLV = 0.485 for scalar perturbations. Phase singularities in these fields, being interference zeros, can exceed both of these speeds.

The fraction of "superluminal" singularities (relative to c_BLV) depends on the effective v_ph / v_g for each mode class. I derive this in Part 3.

---

## Part 3: Predictions the Framework Must Obey

### 3.1 Mean Velocity <v> / c_BLV for the GGE Ensemble

The Berry-Dennis formula Eq. (2) gives <v> in terms of the spectral width Delta_k / k and the velocity ratio v_ph / v_g. For the framework's GGE, I compute this for each mode class.

**Goldstone channel**: The Goldstone modes have linear dispersion omega = c_Gold * k. For a linear dispersion, v_ph = omega/k = c_Gold and v_g = d(omega)/dk = c_Gold, so v_ph / v_g = 1 (no dispersion). The effective spectral width comes from the multimode interference. On CG(24) with Laplacian eigenvalues lambda_n in {0, 4, 6, 8, 12}, the natural wavenumber set is k_n = sqrt(lambda_n). The spectral width is:

$$\frac{\Delta k}{k} \sim \frac{k_{max} - k_{min}}{k_{mean}} = \frac{\sqrt{12} - \sqrt{4}}{(\sqrt{4} + \sqrt{12})/2} = \frac{3.464 - 2.000}{2.732} = 0.536 \tag{3}$$

With v_ph / v_g = 1 for linear dispersion, the effective Delta_k/k is just this geometric width, giving:

$$\frac{\langle v \rangle_{\text{Gold}}}{c_{\text{Gold}}} = \frac{\pi}{\sqrt{2}} \cdot \frac{0.536}{\sqrt{1 + 0.536^2}} = \frac{2.221 \times 0.536}{1.135} = 1.049 \tag{4}$$

**Prediction 1**: The mean singularity velocity in the Goldstone channel is <v>_Gold / c_Gold = 1.05 +/- 0.1 (the uncertainty reflects the crude approximation of treating CG(24) wavenumbers as a continuous distribution).

**Leggett channel**: The Leggett modes have massive dispersion omega^2 = omega_L^2 + c_L^2 * k^2, where omega_L = 0.138 M_KK (S52 GL-JOSEPHSON-52 PASS). For massive modes, v_ph = omega/k and v_g = c_L^2 * k / omega, giving:

$$\frac{v_{ph}}{v_g} = \frac{\omega^2}{c_L^2 k^2} = 1 + \frac{\omega_L^2}{c_L^2 k^2} \tag{5}$$

At the characteristic wavenumber k ~ sqrt(lambda_1) * a^{-1} = 2 * (xi_BCS)^{-1} (where a = xi_BCS = 0.808 is the lattice spacing and lambda_1 = 4 is the spectral gap), we get k = 2.475 in M_KK units, and:

$$\frac{v_{ph}}{v_g} = 1 + \frac{0.138^2}{0.019^2 \times 2.475^2} = 1 + \frac{0.01904}{0.002211} = 1 + 8.61 = 9.61 \tag{6}$$

This ratio v_ph / v_g = 9.6 is remarkably close to the hBN value of 12. With the spectral width from CG(24):

$$\frac{\langle v \rangle_{\text{Leggett}}}{c_{\text{BLV}}} = \frac{\pi}{\sqrt{2}} \cdot \frac{9.61 \times 0.536}{\sqrt{1 + (9.61 \times 0.536)^2}} = \frac{2.221 \times 5.151}{\sqrt{1 + 26.53}} \tag{7}$$

$$= \frac{11.44}{5.248} = 2.18 \tag{8}$$

**Prediction 2**: The mean Leggett-channel singularity velocity is <v>_Leggett / c_BLV = 2.18 +/- 0.5. This is 2.18x the BLV sound speed — substantially superluminal relative to the substrate's scalar-perturbation speed.

### 3.2 Superluminal Fraction Relative to c_BLV

Using the Berry-Dennis distribution Eq. (1), the fraction of singularities with |v| > v_0 is:

$$F(|v| > v_0) = \int_{v_0}^{\infty} P(|v|) \, d|v| = \frac{4\langle v \rangle^2}{\pi^2 v_0^2 + 4\langle v \rangle^2} \tag{9}$$

**Goldstone channel superluminal fraction** (relative to c_BLV = 0.485):

The critical velocity ratio is v_0 / <v>_Gold = c_BLV / (1.049 * c_Gold) = 0.485 / (1.049 * 0.915) = 0.505.

$$F_{\text{Gold}}(|v| > c_{\text{BLV}}) = \frac{4}{0.505^2 \pi^2 + 4} = \frac{4}{2.517 + 4} = 0.614 \tag{10}$$

**Prediction 3**: 61% of Goldstone-channel singularities exceed c_BLV. This is physically expected — c_Gold = 0.915 > c_BLV = 0.485, so Goldstone mode singularities naturally exceed the scalar perturbation speed.

**Leggett channel superluminal fraction** (relative to c_BLV = 0.485):

With <v>_Leggett = 2.18 * c_BLV, we need v_0 / <v>_Leggett = 1 / 2.18 = 0.459:

$$F_{\text{Leggett}}(|v| > c_{\text{BLV}}) = \frac{4}{0.459^2 \pi^2 + 4} = \frac{4}{2.079 + 4} = 0.658 \tag{11}$$

**Prediction 4**: 66% of Leggett-channel singularities exceed c_BLV. The Leggett channel has a HIGHER superluminal fraction than the Goldstone channel because its v_ph / v_g ratio amplifies the velocity distribution more strongly, despite the individual Leggett mode group velocity being very slow (c_L = 0.019).

This is the same physics as in Bucher's hBN experiment: the SLOW group velocity AMPLIFIES the superluminal fraction. The Leggett mode is the substrate's analog of the hyperbolic phonon-polariton.

### 3.3 Annihilation Timescale on CG(24)

If the GGE relic were NOT protected by integrability, the annihilation timescale for quasiparticle pairs on CG(24) would be set by the singularity approach dynamics. From Bucher's data, the timescale for a pair separated by distance R to approach and annihilate is:

$$t_{\text{ann}}(R) \sim \frac{R}{\langle v \rangle_{\text{relative}}} \tag{12}$$

where <v>_relative is the relative velocity of approaching opposite-charge singularities. From P(v, R) at small R, <v>_relative increases as R decreases — the acceleration before annihilation. The characteristic annihilation time for pairs at the mean separation is:

On CG(24), the mean nearest-neighbor distance is d = 1 in graph units = xi_BCS = 0.808 M_KK^{-1}. The Leggett-channel <v>_Leggett = 2.18 * c_BLV * M_KK (restoring units) gives:

$$t_{\text{ann}} \sim \frac{\xi_{\text{BCS}}}{\langle v \rangle_{\text{Leggett}}} = \frac{0.808}{2.18 \times 0.485} \cdot M_{\text{KK}}^{-1} = 0.764 \cdot M_{\text{KK}}^{-1} \tag{13}$$

In SI units: t_ann ~ 0.764 / (M_KK * GeV_to_inv_s) = 0.764 / (7.43 x 10^{16} x 1.52 x 10^{24}) s = 6.8 x 10^{-42} s.

This is comparable to the BA mode decay timescale [3.8 x 10^{-42}, 3.3 x 10^{-41}] s from S67. The BA modes DO decay on this timescale. The Leggett modes do NOT because of the Z_2 parity protection (different selection rule structure).

**Prediction 5**: If integrability were broken, the GGE pair annihilation timescale would be t_ann ~ 10^{-42} s. Since this is 10^{59} orders of magnitude shorter than the age of the universe (t_universe = 4.35 x 10^{17} s), the integrability protection is absolutely essential for GGE permanence. The Bucher velocity distribution provides a quantitative estimate of the annihilation rate that integrability must suppress.

### 3.4 Distance Correlations and Liquid-Like Short-Range Order

**Bucher result**: g(R) shows liquid-like short-range order with a correlation hole at R < lambda/2.

**Framework prediction**: On CG(24), the only available distances are d = {0, 1, 2, 3} in graph metric. The "liquid-like" correlation structure must manifest as:

- g(d=0) = 0 for same-charge (Pauli exclusion within a cell)
- g(d=0) enhanced for opposite-charge (quasiparticle-quasihole produced at the same site)
- g(d=1) ~ 1 for same-charge (Josephson correlations)
- g(d=2), g(d=3) ~ 1 (uncorrelated at larger distances)

The S64 LOCAL-ENTANGLE-64 result gives quantitative handle: I(A:B) = 110.72 nats of mutual information between sublattices means the even-odd bipartite structure creates strong inter-sublattice correlations. Since opposite-charge excitations are created at the same site (Parker pair production), the g_{+|-}(d=0) enhancement is built in by construction.

**Prediction 6**: The GGE spatial correlations on CG(24) should show:
- Strong anti-correlation between same-charge excitations at d=0 (exclusion)
- Strong positive correlation between opposite-charge excitations at d=0 (pair production)
- Josephson-mediated correlations at d=1 with magnitude set by J_C2 / T_acoustic = 0.933 / 0.112 = 8.33

This is qualitatively consistent with the Bucher liquid-like structure but quantitatively DIFFERENT because of the discrete graph topology.

---

## Part 4: Proposed Computational Tests

### Test 1: BERRY-DENNIS-GGE-69

**Gate ID**: BERRY-DENNIS-GGE-69

**Hypothesis**: The GGE relic's quasiparticle velocity distribution obeys the Berry-Dennis universal distribution Eq. (1), with mean velocity determined by the CG(24) spectral width and the mode dispersion relations.

**PASS/FAIL Criteria**:
- PASS if: The computed velocity distribution from the 8-band GGE on CG(24) matches the Berry-Dennis distribution Eq. (1) with chi^2 / ndof < 2 across all three channels (Goldstone, BA, Leggett), with <v> consistent with Eqs. (4), (8) to within 30%.
- FAIL if: chi^2 / ndof > 5 in ANY channel, indicating the Gaussian random wave model does not apply to the GGE state on a discrete graph.

**Input data**:
- `computations/canonical_constants.py` (all BCS parameters, M_KK, mode energies)
- `computations/s61_fabric_landau_params.npz` (Pomeranchuk-stable Landau parameters, exact diag ground state)
- `computations/s66_leggett_spectral.npz` (Leggett spectral function)

**Method**:
1. Construct the 8-band BCS Hamiltonian on CG(24) with Josephson coupling J_C2 = 0.933.
2. Generate the GGE state from the impulsive quench (P_exc = 1.0, n_Bog = 0.999).
3. Compute the phase field phi(x, t) = sum_k u_k * exp(i*omega_k*t - i*k*x) + v_k * exp(-i*omega_k*t + i*k*x) using the Bogoliubov amplitudes (u_k, v_k) and the CG(24) Laplacian eigenvectors.
4. Track phase singularities (zeros of the complex field) across time steps.
5. Compute the velocity distribution P(|v|) from finite differences of singularity positions.
6. Fit to Eq. (1) and extract <v>.
7. Compare <v> to the analytic prediction from Eq. (2) with the CG(24) spectral parameters.

**Expected output**: Three velocity distributions (one per channel), each with a fitted <v> value and chi^2 statistic. The BA channel should show the lowest <v> (c_BA = 0.399) and the Goldstone channel the highest (c_Gold = 0.915).

**Connection to existing results**: This connects to S61 POMERAN-FABRIC-61 (Pomeranchuk stability of the GGE state), S66 LEGGETT-SPECTRAL-66 (Leggett quasiparticle sharpness), and S67 BA-LIFETIME-FABRIC-67 (BA mode overdamping). If the Berry-Dennis distribution holds, it provides a NEW consistency check on the GGE wave function that is independent of all previous gates.

### Test 2: SUPERLUMINAL-FRACTION-69

**Gate ID**: SUPERLUMINAL-FRACTION-69

**Hypothesis**: The fraction of GGE excitations that are "superluminal" relative to c_BLV matches the prediction from Eq. (9) using the computed <v> from Test 1.

**PASS/FAIL Criteria**:
- PASS if: The computed superluminal fraction F(|v| > c_BLV) is within 20% of the analytic prediction from Eq. (9)-(11), AND the Leggett channel has F > 50% (confirming the slow-group-velocity amplification mechanism).
- FAIL if: F_Leggett < 30% (would indicate the discrete graph topology suppresses the amplification) OR F deviates from the Berry-Dennis prediction by more than a factor of 2.

**Input data**: Same as Test 1, plus the velocity distributions computed in Test 1.

**Method**:
1. From the velocity distributions of Test 1, count the fraction exceeding c_BLV = 0.485.
2. Compare to the analytic predictions in Eqs. (10)-(11).
3. Separately compute the fraction exceeding c_BA = 0.399 and c_Leggett = 0.019 for each channel.
4. Test the Bucher scaling: does F scale with (v_ph / v_g)^2 as predicted by the Berry-Dennis model?

**Expected output**: A table of superluminal fractions {F_Gold, F_BA, F_Leggett} for each reference velocity {c_BLV, c_BA, c_Leggett}. The hierarchy should be F_Leggett > F_Gold > F_BA at the c_BLV reference.

**Connection to existing results**: The superluminal fraction provides a new diagnostic of the GGE velocity structure that connects to the acoustic white hole (S63 supersonic transit) and the v_ph / v_g amplification mechanism. If the Leggett channel shows strong amplification, it strengthens the DM candidacy by demonstrating that the DM mode's phase structure is dynamically rich despite its slow group velocity.

### Test 3: GGE-PAIR-CORRELATION-69

**Gate ID**: GGE-PAIR-CORRELATION-69

**Hypothesis**: The GGE quasiparticle pair correlation function g(d) on CG(24) matches the discrete-graph version of the Bucher distance correlations, with a correlation hole at d = 0 for same-charge and enhancement at d = 0 for opposite-charge.

**PASS/FAIL Criteria**:
- PASS if: g_{+|+}(d=0) < 0.1 AND g_{+|-}(d=0) > 2.0 AND g(d >= 2) is within [0.5, 1.5] (liquid-like at large d).
- FAIL if: g_{+|+}(d=0) > 1.0 (no exclusion hole) OR g_{+|-}(d=0) < 1.0 (no pair enhancement).

**Input data**:
- `computations/s64_local_entangle.npz` (entanglement data on CG(24))
- `computations/canonical_constants.py`
- CG(24) graph adjacency matrix (construct from S_4 generators)

**Method**:
1. Construct the full many-body GGE state on CG(24) (8 bands x 24 sites = 192 modes).
2. Compute the occupation number operators n_{k,alpha}(x) for each mode k, band alpha, site x.
3. Define quasiparticle charge: q(x) = sum_k (n_k(x) - <n_k>_GGE). Positive charge = quasiparticle-rich site, negative = quasihole-rich.
4. Compute g_{+|+}(d) = <sum_{x,y: d(x,y)=d} delta(q(x)>0) delta(q(y)>0)> / <rho_+>^2.
5. Similarly for g_{+|-}(d).
6. Compare the shape to the continuum Berry-Dennis prediction adapted to a degree-6 regular graph.

**Expected output**: Two correlation functions g_{+|+}(d) and g_{+|-}(d) at distances d = {0, 1, 2, 3}, plus the effective pair correlation length xi_pair.

**Connection to existing results**: Directly extends S64 LOCAL-ENTANGLE-64 (which computed entanglement entropy, not pair correlations) and connects to S61 POMERAN-FABRIC-61 (which showed Josephson-mediated inter-cell anti-correlations C_kk ~ -0.245 for B2). The anti-correlation result already suggests liquid-like short-range order.

### Test 4: ANNIHILATION-TIME-INTEGRABILITY-69

**Gate ID**: ANNIHILATION-TIME-INTEGRABILITY-69

**Hypothesis**: The Bucher pre-annihilation acceleration, combined with the GGE dispersion relations, predicts a pair annihilation timescale t_ann ~ 10^{-42} s on CG(24), which is exactly the timescale suppressed by the Richardson-Gaudin integrability.

**PASS/FAIL Criteria**:
- PASS if: The computed annihilation timescale t_ann from the phase-space dynamics falls within [10^{-43}, 10^{-40}] s, AND the ratio t_ann / t_BA (where t_BA is the BA mode lifetime from S67) is within [0.1, 10], confirming the two timescales are set by the same physics.
- FAIL if: t_ann > 10^{-35} s (would mean integrability is not needed for pair stability) OR t_ann < 10^{-50} s (would indicate a computational error).

**Input data**:
- `computations/s67_ba_lifetime.npz` (BA mode lifetimes)
- `computations/canonical_constants.py`
- CG(24) graph with Josephson coupling J_C2

**Method**:
1. Construct the time-dependent GGE wave function phi(x, t) on CG(24) with all 8 bands.
2. For each pair of phase singularities of opposite charge, compute the approach velocity v(t) as a function of separation R(t).
3. Extrapolate to the annihilation time using the Bucher power-law: v ~ 1/R near annihilation.
4. Average over all pairs to obtain t_ann.
5. Compare t_ann to the BA lifetime from S67 and to the inverse Josephson frequency 1/(J_C2 * M_KK).
6. Quantify the integrability protection factor: t_therm / t_ann, where t_therm is the thermalization time from S38 (GGE permanence).

**Expected output**: t_ann in seconds, t_ann / t_BA ratio, and the integrability suppression factor.

**Connection to existing results**: Links S67 BA-LIFETIME-FABRIC-67 (BA overdamping timescale) to S38 ordered veil theorem (GGE permanence), providing a new route to the permanence proof via phase singularity dynamics rather than conservation law counting.

### Test 5: DISCRETE-BERRY-DENNIS-69

**Gate ID**: DISCRETE-BERRY-DENNIS-69

**Hypothesis**: The Berry-Dennis Gaussian random wave model has a well-defined discrete limit on finite regular graphs, and the CG(24) Cayley graph's singularity statistics match this discrete limit.

**PASS/FAIL Criteria**:
- PASS if: A discrete-graph Berry-Dennis velocity distribution can be derived analytically for the CG(24) spectrum {0, 4, 6, 8, 12}, and it matches the numerical simulation from Test 1 within chi^2 / ndof < 3.
- FAIL if: No well-defined discrete limit exists (the velocity distribution does not converge for N_vertices < 100), OR the continuum Berry-Dennis distribution deviates from the discrete result by more than a factor of 3 in <v>.
- INFO if: The discrete limit exists but requires N > 24 vertices for convergence (CG(24) too small).

**Input data**:
- CG(24) Laplacian spectrum and eigenvectors (construct from first principles)
- `computations/canonical_constants.py`

**Method**:
1. Define a Gaussian random wave field on CG(24): phi(x) = sum_n a_n * psi_n(x), where psi_n are the Laplacian eigenvectors and a_n are complex Gaussian random variables with variance proportional to the mode occupation numbers.
2. For the GGE state, the variances are sigma_n^2 = 1/(exp(beta_n * omega_n) - 1) + 1/2 (Bose occupation + quantum zero-point).
3. Compute phase singularities as zeros of the complex field on the graph (sites where the winding number around a plaquette is +/-2*pi).
4. Note: on a graph, "singularities" are defined on faces (plaquettes), not vertices. CG(24) has 49 independent cycles (H_1 rank = 72 - 24 + 1 = 49). The winding number around each cycle defines the singularity charge.
5. Generate N_samples = 10^5 random wave realizations. Compute the velocity distribution from the time-derivative of the phase field.
6. Derive the analytic discrete-graph Berry-Dennis distribution by replacing the continuum k-integral with the discrete sum over {0, 4, 6, 8, 12}.

**Expected output**: The discrete Berry-Dennis distribution P_disc(|v|), the continuum approximation P_cont(|v|), and the chi^2 comparison to numerical simulation. Also: the minimum graph size N_min for which the continuum approximation holds to within 20%.

**Connection to existing results**: This is the theoretical foundation for Tests 1-4. It determines whether the Bucher universality (Gaussian random wave model) extends to discrete structures. The S63 RICHARDSON-GAUDIN-N2-63 computation (Poisson statistics, integrable) provides the integrability context: the GGE on CG(24) is integrable, which affects the statistics beyond the Gaussian random wave assumption.

---

## Summary Table

| Observable (Bucher) | Framework Mapping | Quantitative Prediction | Proposed Test |
|:---------------------|:------------------|:------------------------|:-------------|
| P(|v|) Berry-Dennis Eq. (1) | GGE quasiparticle velocities | <v>_Gold = 1.05 c_Gold, <v>_Leggett = 2.18 c_BLV | BERRY-DENNIS-GGE-69 |
| <v> = 1.04 c | Mean GGE singularity speed | <v>/c_BLV in [1.0, 2.2] depending on channel | BERRY-DENNIS-GGE-69 |
| 29% superluminal | Fraction exceeding c_BLV | F_Leggett ~ 66%, F_Gold ~ 61% | SUPERLUMINAL-FRACTION-69 |
| g(R) liquid-like | GGE correlations on CG(24) | g_{+|+}(0) < 0.1, g_{+|-}(0) > 2.0 | GGE-PAIR-CORRELATION-69 |
| Pre-annihilation acceleration | Pair recombination (blocked by integrability) | t_ann ~ 10^{-42} s = t_BA | ANNIHILATION-TIME-INTEGRABILITY-69 |
| v_ph / v_g amplification | c_Gold/c_Leggett = 48.2 | Leggett channel most "superluminal" | SUPERLUMINAL-FRACTION-69 |
| Gaussian random wave universality | Discrete limit on CG(24) | chi^2/ndof < 3 for discrete Berry-Dennis | DISCRETE-BERRY-DENNIS-69 |

---

## Key Structural Insights

### Insight 1: The Leggett Mode IS the Substrate's Phonon-Polariton

The deepest connection between Bucher's experiment and the framework is this: the Leggett mode plays exactly the role of the hyperbolic phonon-polariton in hBN. Both are:
- Massive (gapped) collective excitations with v_ph >> v_g
- Propagating in a dispersive medium where the velocity ratio amplifies phase singularity dynamics
- Carrying quantized topological charge (Z_2 for Leggett, +/-1 for PhP singularities)
- Protected by symmetry from certain decay channels

The v_ph / v_g ratio for the Leggett mode (9.6 from Eq. (6)) is close to the hBN value (12). This is not a coincidence if the underlying physics is universal — the Gaussian random wave model predicts the same velocity statistics regardless of the microscopic platform.

### Insight 2: Integrability Replaces Steady-State

In Bucher's experiment, singularities are continuously created and annihilated, maintaining a steady-state density. In the framework, the GGE is frozen by integrability — there is no pair creation or annihilation after the initial quench. The Berry-Dennis statistics should hold at the moment of GGE formation (the KZ freeze-out), but the velocity distribution is subsequently frozen. This makes the framework's singularity statistics a SNAPSHOT rather than a steady state — an important distinction for the computational tests.

### Insight 3: The Discrete Graph Limits Universality

The CG(24) graph has only 24 vertices and 5 distinct Laplacian eigenvalues. The Berry-Dennis model assumes a continuum of wavenumbers. The discrete limit may or may not preserve universality. Test 5 (DISCRETE-BERRY-DENNIS-69) is therefore the most fundamental of the proposed tests: if universality breaks on graphs this small, Tests 1-4 need modification.

---

## References to Framework Results

| Result | Session | Gate | Relevance |
|:-------|:--------|:-----|:----------|
| c_BLV = 0.485 | S63/S64 | SOUND-SPEED-64 | Substrate "speed of light" for scalar perturbations |
| c_BA = 0.399 | S56/S64 | S64 computation | BCS condensate phase velocity |
| c_Gold = 0.915 | S52 | GL-JOSEPHSON-52 PASS | Goldstone sound speed |
| c_Leggett = 0.019 | S64 | S64 computation | Leggett (DM) group velocity |
| omega_L = 0.138 M_KK | S52 | GL-JOSEPHSON-52 PASS | Leggett mass gap |
| n_pairs = 59.8 | S38 | KZ transit | GGE pair number |
| P_exc = 1.000 | S38 | KZ transit | Excitation probability (exact) |
| Q_Leggett = 18.6 | S66 | LEGGETT-SPECTRAL-66 PASS | Leggett quasiparticle quality factor |
| Z_Leggett = 0.972 | S66 | LEGGETT-SPECTRAL-66 PASS | Leggett spectral weight |
| BA overdamped (Q < 2) | S67 | BA-LIFETIME-FABRIC-67 PASS | BA mode elimination |
| CG(24) bipartite | S64 | LOCAL-ENTANGLE-64 INFO | Graph structure |
| I(A:B) = 110.72 nats | S64 | LOCAL-ENTANGLE-64 INFO | Spatial correlations |
| Pomeranchuk stable | S61 | POMERAN-FABRIC-61 PASS | GGE Fermi liquid stability |
| Integrability | S63 | RICHARDSON-GAUDIN-N2-63 FAIL | Poisson statistics (integrable) |
| xi_BCS = 0.808 M_KK^{-1} | S37 | canonical_constants.py | BCS coherence length |
| J_C2 = 0.933 M_KK | S47 | TEXTURE-CORR-48 | Josephson coupling |
| T_acoustic = 0.112 M_KK | S42/S47 | canonical_constants.py | GGE acoustic temperature |

---

## Landau Corpus Citations

- **Paper 05 (Landau 1941, Superfluidity I)**: Two-fluid model and phonon-roton spectrum. The GGE relic's multi-speed structure (Goldstone, BA, Leggett) is the substrate generalization of Landau's two-fluid decomposition.
- **Paper 13 (Abrikosov 1957, Vortices)**: Topological defects in type-II superconductors. The mapping between phase singularity charge +/-1 and Abrikosov vortex winding follows directly from Abrikosov's classification. Section 8.4 of the transcription explicitly maps vortex-antivortex pairs to particle-antiparticle pairs.
- **Paper 16 (Richardson 1963, Exact Pairing)**: Integrability of the pairing Hamiltonian. The Richardson-Gaudin conservation laws are what prevent pair annihilation in the GGE, making the framework's prediction sharply different from Bucher's steady-state dynamics.
- **Paper 29 (Zurek 1985, Kibble-Zurek)**: Freeze-out mechanism for topological defect production. The GGE pair density n_pairs = 59.8 is set by the KZ freeze-out time t_hat = sqrt(tau_0 * tau_Q), and the Berry-Dennis statistics should apply at t_hat.

---

*Review completed 2026-04-05. Landau Condensed-Matter Theorist, S69.*
