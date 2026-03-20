# The Texture Spectrum Framework: From Goldstone Mode to Spectral Tilt

**Author**: Volovik (Superfluid Universe Theorist)
**Date**: 2026-03-16
**Session**: S47 Wave 5 Synthesis
**Status**: Framework document for S48+
**Source computations**: TEXTURE-CORR-48 (PASS), SCALE-BRIDGE-48 (FAIL), ACOUSTIC-HORIZON-48 (FAIL)

---

## 1. The Result and Why It Matters

### 1.1 What Was Computed

TEXTURE-CORR-48 (Landau, W5-1) computed the phase-phase correlation function of the BCS condensate across the 32-cell Kibble-Zurek tessellation. Each cell carries a BCS condensate with spontaneously broken U(1)_7 phase phi_i. Adjacent cells couple through a Josephson energy:

    E = Sum_{<ij>} J_{ij} (1 - cos(phi_i - phi_j))

The Josephson coupling J_ij = |E_cond| * rho_s^{dir} * f_overlap encodes three microscopic quantities: the condensation energy |E_cond| = 0.137 M_KK (S36 ED), the direction-dependent superfluid stiffness rho_s^{dir} (W3-4, RHOS-TENSOR-47), and the inter-cell wavefunction overlap f_overlap = exp(-l_cell/xi_GL) = 0.856.

The computation diagonalized the stiffness matrix (discrete Laplacian weighted by J) and obtained the phase fluctuation power spectrum P(K) = T_eff * (M^+)_{ij} in Fourier space, where M^+ is the pseudoinverse projecting out the Goldstone zero mode.

### 1.2 The Numbers

| Quantity | Value | Origin |
|:---------|:------|:-------|
| P(K) slope (low-K) | -1.955 | Numerical fit, n=1-5 |
| P(K) slope (continuum) | -2.000 (exact) | Analytical: T/(J K^2) |
| P(K_1)/P(K_{N/2}) | 104x | Infrared divergence from Goldstone |
| J_C2 | 0.933 M_KK | Dominant coupling (C^2 coset) |
| J_su2 | 0.059 M_KK | Subdominant (su(2) stabilizer) |
| J_u1 | 0.038 M_KK | Weakest (u(1) hypercharge) |
| T_acoustic / J_C2 | 0.120 | Deep in ORDERED regime |
| T_acoustic / J_su2 | 1.897 | DISORDERED |
| T_acoustic / J_u1 | 2.932 | DISORDERED |
| xi_phase(C^2) | 532 cells | Long-range phase order |
| xi_phase(su(2)) | 33.7 cells | Marginal order |
| xi_phase(u(1)) | 21.8 cells | Marginal order |
| phi_rms(C^2, acoustic) | 0.566 rad | Harmonic approximation VALID |
| Analytical verification | 3e-14 max error | Machine epsilon agreement |

### 1.3 What It Means

The power spectrum P(K) ~ K^{-2} is the Ornstein-Zernike form for a system with spontaneously broken continuous symmetry and a gapless Goldstone mode. It is the universal spectrum of phase fluctuations in ANY superfluid, superconductor, or Bose condensate. The only free parameter is the ratio T/J.

The result carries weight for three reasons.

First, it is the first NON-TRIVIAL fabric-level spectrum. Eleven routes through single-cell pair creation all produced n_s hundreds of sigma from Planck. These routes failed because |beta_k|^2 ~ (Delta/omega_k)^4 is a property of the temporal quench profile -- a steep power law set by the factor-2.5 eigenvalue span and flat BCS gap. The texture spectrum is categorically different: it depends on the SPATIAL coupling between cells, not on the temporal quench within a cell.

Second, the K^{-2} slope is STRUCTURAL. It follows from the topology of broken U(1)_7. The Goldstone theorem guarantees a massless mode whenever a continuous symmetry breaks spontaneously. The spectral weight of a massless mode diverges as K^{-2} at low wavenumber in any dimension. This is not dependent on eigenvalue spans, BCS gap flatness, or any parameter that killed the single-cell routes. It is protected by the same topology that protects the Nambu-Goldstone boson in particle physics and the phonon in superfluid helium-4.

Third, the resulting spectral index -- while still discrepant from Planck -- is closer than any prior attempt. The phase gradient spectrum P_{nabla phi}(K) = K^2 * P_phi(K) ~ K^0 gives Harrison-Zel'dovich n_s = 1. The departure from Planck (0.9649) is 0.035, or 8.3 sigma at Planck sensitivity (sigma = 0.0042). Compare: the single-cell routes gave n_s = -0.588 to -2.847, hundreds to thousands of sigma away. The texture route reduces the discrepancy by two orders of magnitude.

### 1.4 Anisotropic Phase Order

The most physically consequential sub-result is the anisotropic phase ordering at T_acoustic:

- **C^2 directions (4 of 8)**: T/J = 0.120, ORDERED. Phase coherence extends over 532 cells -- 17x the tessellation size. The condensate phases across all 32 cells are phase-locked in these directions.
- **su(2) directions (3 of 8)**: T/J = 1.90, DISORDERED. Phase correlation length 34 cells -- marginal, near the tessellation size.
- **u(1) direction (1 of 8)**: T/J = 2.93, DISORDERED. Phase correlation length 22 cells -- marginal.

This anisotropic pattern is determined by rho_s. The C^2 coset directions carry 24x the superfluid stiffness of the u(1) direction (rho_s = 7.96 vs 0.33). The Josephson coupling is proportional to rho_s, so phase locking is 24x stronger in C^2 directions. The temperature T_acoustic = 0.112 M_KK is set by the GGE acoustic bath (S42 Hauser-Feshbach), which is the physically correct temperature because integrability prevents thermalization: the BCS quench energy goes into quasiparticle pair excitations (59.8 pairs, S38), not into phase modes.

---

## 2. The Superfluid Physics

### 2.1 U(1)_7 Breaking as Superfluid Phase Transition

The BCS condensate on Jensen-deformed SU(3) spontaneously breaks U(1)_7 (S35: Cooper pairs carry K_7 charge +/-1/2, V(q+,q-) = 0 exactly). This is structurally identical to the superfluid phase transition in helium-4, where the U(1) gauge symmetry of particle number conservation breaks spontaneously, producing a Goldstone mode (the phonon) with gapless dispersion omega(k) = c_s * k and a phase fluctuation spectrum P(K) ~ T / (rho_s * K^2).

The correspondence is:

| Superfluid He-4 | Framework | This computation |
|:----------------|:----------|:-----------------|
| U(1) particle number | U(1)_7 K_7 charge | Broken at each cell |
| Phonon (Goldstone) | K_7 phase mode | Gapless, K^{-2} spectrum |
| Superfluid density rho_s | rho_s^{ab} tensor | 24x anisotropic (W3-4) |
| Temperature T | T_acoustic = 0.112 M_KK | GGE acoustic bath |
| Josephson coupling (SNS) | J = |E_cond| * rho_s * f_overlap | 0.933 M_KK (C^2) |
| Container geometry | 32-cell tessellation | N = 32, l_cell = 0.152 M_KK^{-1} |

In my monograph (Paper 01, Ch. 7.3), the l-texture in 3He-A has the same mathematical structure: a unit vector field l(r) varying across the container, with gradient energy E_grad = (K_s/2) * |nabla l|^2 and correlation spectrum P_l(K) ~ T / (K_s * K^2). The l-texture power spectrum determines the long-wavelength correlations of the superfluid. Here, the texture variable is the U(1)_7 phase phi(r) rather than the SO(3) director l, and the stiffness is the Josephson coupling rather than the spin-orbit gradient energy, but the mathematical structure is identical.

### 2.2 Anisotropic Phase Order and the 3He-A Analog

The anisotropic phase ordering -- C^2 ordered, su(2)/u(1) disordered -- has a precise analog in 3He-A. In the A-phase, the superfluid density tensor rho_s^{ij} is anisotropic: the stiffness for superflow parallel to the gap node direction (the l-vector) differs from the stiffness perpendicular to it. At zero temperature, rho_s_parallel = 0 (the superflow gap vanishes along l) while rho_s_perp = rho (full stiffness perpendicular to l). This produces anisotropic phase coherence: the condensate is strongly phase-locked in the perpendicular plane but weakly locked along l.

In the framework, the analog is:
- **C^2 = perpendicular to l**: High stiffness (rho_s = 7.96), strong phase locking (xi = 532 cells)
- **u(1) = parallel to l**: Low stiffness (rho_s = 0.33), weak phase locking (xi = 22 cells)

The physical origin differs. In 3He-A, the anisotropy comes from the gap node structure (the gap vanishes along l, so quasiparticles propagating in that direction cost no superflow energy). In the framework, the anisotropy comes from the Jensen deformation: the metric scales u(1), su(2), C^2 by different factors (e^{2tau}, e^{-2tau}, e^{tau}), and the BCS pairing funnel (B2 dominant, 91% of pairing) selects the su(2)-C^2 cross-sector where the curvature is softest (K = 0.010). The rho_s anisotropy is a consequence of this geometric funneling, confirmed by the curvature anti-correlation r = -0.906 (W3-4).

The key structural parallel: in both systems, the anisotropy of rho_s determines which directions in the order parameter space carry long-range correlations and which do not. The texture power spectrum is not isotropic -- it is a tensor quantity with different spectral indices in different directions. For the C^2 directions, P(K) ~ K^{-2}. For the u(1) direction at T_acoustic, the system is near the Berezinskii-Kosterlitz-Thouless transition (T/J = 2.93), where phase coherence breaks down through vortex unbinding and P(K) develops an algebraic dependence P(K) ~ K^{-(2-eta)} with anomalous exponent eta > 0.

### 2.3 The 532-Cell Correlation Length

The phase correlation length xi_phase(C^2) = 2 * J_C2 * N / T_acoustic = 532 cells is the XY model result for a 1D ring of N sites with coupling J at temperature T. Substituting the microscopic parameters:

    xi = 2 * |E_cond| * rho_s(C^2) * f_overlap * N / T_acoustic
      = 2 * 0.137 * 7.962 * 0.856 * 32 / 0.112
      = 532

This is set by J/T -- the ratio of Josephson coupling to effective temperature. The large correlation length (16.6x the tessellation) means the fabric is in the quasi-long-range ordered regime in the C^2 directions. The phases are locked across the entire tessellation, with small Gaussian fluctuations (phi_rms = 0.566 rad < 1, validating the harmonic approximation).

In 3He-B, the analog is the correlation length of the Leggett angle theta(r), set by the dipole length xi_D ~ 10 micrometers. For T << T_c, the dipole energy provides a weak restoring force that aligns theta over macroscopic distances. The 532-cell correlation length in the framework is the internal-space analog of this dipole-induced phase locking.

### 2.4 The GGE and the Temperature Selection

The T_acoustic = 0.112 M_KK temperature enters through the GGE (Generalized Gibbs Ensemble). This is the central point where the superfluid program makes its sharpest contribution to the framework.

After the BCS transit (S38: P_exc = 1.000), the system is NOT in thermal equilibrium. The GGE relic has 8 Richardson-Gaudin conserved integrals that prevent thermalization (S38, block-diagonal theorem S22b). The excitation energy E_exc = 443 * |E_cond| goes overwhelmingly into quasiparticle pair excitations (59.8 pairs), not into collective phase modes. The acoustic sector thermalizes internally at T_acoustic -- a temperature set by the fraction of quench energy that couples to the low-energy phonon-like modes through the Hauser-Feshbach compound nucleus decay analogy (S42).

In superfluid helium, the analog is fountain pressure after a quench: when a superfluid is rapidly cooled below T_c, the normal component thermalizes at a temperature T_n determined by the entropy carried by phonons and rotons, while the superfluid component carries zero entropy. The two-fluid model (Landau-Khalatnikov, Paper 37) gives the equilibrium between normal and superfluid as a partition of the total energy between the thermal quasiparticle gas and the condensate. The S42 Hauser-Feshbach temperature is the framework's version of this partition.

The physical consequence: T_compound = 7.58 M_KK (the full quench energy divided by degrees of freedom) would make ALL directions disordered. T_acoustic = 0.112 M_KK (the acoustic sector temperature) makes C^2 ordered and su(2)/u(1) disordered. The GGE selects T_acoustic as the relevant temperature for phase fluctuations BECAUSE integrability prevents the high-energy pair excitation modes from equilibrating with the low-energy phase modes. This is not an assumption -- it is a consequence of Richardson-Gaudin integrability and the block-diagonal theorem.

---

## 3. The Path from K^{-2} to n_s = 0.965

### 3.1 The Problem

The pure Goldstone gives n_s = -1 (P(K) ~ K^{-2} in phase, n_s - 1 = -2). Planck gives n_s = 0.965 (P_delta ~ K^{-0.035}, nearly scale-invariant). The texture route delivers n_s = 1 through phase-gradient coupling (P_{nabla phi}(K) = K^2 * P_phi(K) ~ K^0), which is 8.3 sigma from Planck. The question is whether a controlled modification of the pure Goldstone can produce the observed 3.5% red tilt.

### 3.2 The Massive Ornstein-Zernike Form

The massive Ornstein-Zernike form interpolates:

    P(K) = T / (J * K^2 + m^2)

- m = 0: P(K) ~ K^{-2}, n_s = -1 (pure Goldstone, massless)
- m >> K: P(K) ~ const, n_s = 1 (white noise, massive mode dominates)
- Intermediate m: n_s = 1 - 2 * K^2 / (K^2 + m^2)

For n_s = 0.965 at K_pivot = 0.05 Mpc^{-1}:

    (K * xi)^2 = (1 - n_s) / (1 + n_s) = 0.035 / 1.965 = 0.01781
    xi = sqrt(0.01781) / 0.05 = 2.669 Mpc

So m = 1/xi = 0.375 Mpc^{-1}, and the CMB pivot sits at K * xi = 0.133 -- deep in the nearly-white-noise regime, with the 3.5% red tilt coming from the small but finite ratio K/m.

### 3.3 Where Does the Mass Come From?

In the pure Josephson model, the phase mode is exactly massless -- the Goldstone theorem protects it. A mass m requires EXPLICIT breaking of U(1)_7. Three physical candidates:

**(a) The spectral action on-site potential.** The spectral action S(D_K; f, Lambda) is not invariant under U(1)_7 phase rotations of the condensate (the spectral action depends on the BCS-modified Dirac operator, which changes under phase rotation of Delta). This provides an explicit U(1)_7 breaking mass term:

    m^2 ~ d^2 S_spec / dphi^2

In 3He-B, the analog is the nuclear dipole-dipole interaction, which explicitly breaks the relative spin-orbit symmetry and gives the Leggett angle mode a mass m_D corresponding to the dipole length xi_D. The dipole energy is 10^5 times smaller than the condensation energy but is the ONLY source of mass for the Leggett angle Goldstone. In the framework, the spectral action on-site potential plays the same role: it is the leading explicit U(1)_7 breaking term, giving the phase mode a mass proportional to d^2 S_spec / dphi^2 evaluated at the BCS minimum.

**(b) Finite correlation length in disordered directions.** The su(2) and u(1) directions are disordered (T/J > 1). The phase fluctuations in these directions introduce an effective mass into the coupled phase field on the lattice. Physically: if you twist the phase in the C^2 direction, the twist propagates through the tessellation; but if the su(2)/u(1) components are disordered, the twisted state has an energy cost from the disorder-induced scattering, which acts as a mass term for the propagating C^2 phase wave.

**(c) Finite-size cutoff from N = 32.** The tessellation has N = 32 cells. The minimum nonzero wavenumber is K_min = 2*pi/N. Modes at K < K_min do not exist. This acts as an IR cutoff that could mimic a mass in the power spectrum. However, this is a DISCRETE artifact, not a physical mass. It was checked in S43 (KZ-CELL-43): the tessellation N = 32 is robust, and finite-size effects are controlled by N, not by a physical correlation length.

My assessment: **(a) is the physically correct channel.** The spectral action provides the leading explicit U(1)_7 breaking. The mass from d^2 S_spec / dphi^2 is computable from existing data: the Dirac eigenvalue sensitivity to U(1)_7 phase rotation is known from S34 ([iK_7, D_K] = 0 at all tau), and the spectral action coefficients a_0, a_2, a_4 are computed. The mass is:

    m^2 = (a_2 / rho_s) * (d^2 lambda / dphi^2)_avg

where the average is over the spectrum weighted by the cutoff function f. This is a one-line formula once the second derivative of the spectrum with respect to phi is computed.

### 3.4 The Required Mass in Microscopic Units

The corrected correlation length xi = 2.67 Mpc corresponds to:

    m = 1/xi = 0.375 Mpc^{-1} = 2.4 x 10^{-39} GeV = 3.2 x 10^{-56} M_KK

This is an extremely small mass in M_KK units. In temperature:

    T_m ~ m * k_B = 2.4 x 10^{-39} GeV / (8.6 x 10^{-14} GeV/K) ~ 2.8 x 10^{-26} K

Or in eV: m ~ 2.4 x 10^{-30} eV. This is far below the neutrino mass scale.

The ratio m/M_KK = 3.2 x 10^{-56} is the SAME hierarchy that appears in the cosmological constant problem. It is the ratio of the observed vacuum energy scale to the Planck scale. This is not a coincidence -- it IS the cosmological constant problem. The mass that the Goldstone mode needs to acquire to produce n_s = 0.965 is at the same scale as the observed dark energy. In q-theory language (Papers 15-16), this hierarchy is resolved by the equilibrium theorem: the vacuum energy vanishes in equilibrium, and the residual Lambda is of order the perturbation energy (quasiparticles, curvature, temperature), which is naturally small compared to M_KK^4.

Whether the spectral action second derivative d^2 S_spec / dphi^2 produces a mass at THIS scale is the decisive question.

---

## 4. The Algebra Error and Its Consequences

### 4.1 The Error

My wave5 plan (session-47-wave5-texture.md, line 225) wrote:

    xi_texture = 1 / (K_pivot * sqrt(0.035/2)) = 1 / (0.05 * 0.132) = 151 Mpc

This is wrong. I correctly computed K * xi = sqrt(0.035/1.965) = 0.1335, but then INVERTED the formula: I wrote xi = 1 / (K * sqrt(x)) when it should be xi = sqrt(x) / K. The expressions are reciprocals. Tesla caught this in SCALE-BRIDGE-48.

The correct result: xi = 0.1335 / 0.05 = 2.669 Mpc. Verification: n_s(xi = 2.67 Mpc) = 0.965 (correct). n_s(xi = 151 Mpc) = -113.3 (wrong).

The near-coincidence between 151 Mpc and the BAO sound horizon r_s = 147 Mpc was an artifact of the algebra error, not a physical connection.

### 4.2 What Changes

The corrected target xi = 2.67 Mpc does not change the 56-order hierarchy between internal and external scales. It changes what we are looking for: a damping scale at galaxy-cluster size (2.67 Mpc), not at BAO size (151 Mpc). The mass m = 0.375 Mpc^{-1} = 2.4 x 10^{-39} GeV corresponds to a Hubble rate at T ~ sqrt(m * M_Pl) ~ 0.5 eV (recombination temperature).

Is there a physical reason for the Goldstone mode to acquire a mass at the recombination scale? In the standard framework, no -- the spectral action on-site potential is set at the M_KK scale, not at recombination. But in q-theory (Papers 15-16, 35), the vacuum energy responds to the dominant perturbation at each epoch. At recombination, the dominant perturbation shifts from radiation to matter. If the U(1)_7 Goldstone mass tracks the dominant perturbation energy (as the cosmological constant does in q-theory), then the mass could naturally be at the recombination scale.

This is speculative. The computable quantity is d^2 S_spec / dphi^2 in M_KK units, which either produces the right hierarchy or does not.

### 4.3 What Does Not Change

The shape of the Ornstein-Zernike spectrum is generic. ANY Gaussian random field with finite correlation length produces P(K) = A / (K^2 + 1/xi^2). The n_s = 0.965 match at xi = 2.67 Mpc is not a prediction -- it is the definition of xi. The physics is in the specific value xi = 2.67 Mpc, which must be derived from the microscopic theory. The framework must produce m = 3.2 x 10^{-56} M_KK from first principles.

---

## 5. The rho_s Tensor as Unifying Thread

The superfluid stiffness tensor rho_s^{ab}(tau) now appears in THREE independent computations, each revealing a different aspect of the same object.

### 5.1 W3-4: Single-Cell Stiffness (RHOS-TENSOR-47, PASS)

The 8x8 tensor at the fold has eigenvalues:

    rho_s = [0.327, 0.505, 0.505, 0.505, 7.962, 7.962, 7.962, 7.962]

The 24x anisotropy (C^2/u(1)) is the largest dynamical anisotropy in the framework, far exceeding the Jensen metric anisotropy (e^{4*0.19} = 2.14). The anti-correlation with sectional curvature (r = -0.906, p = 0.002) establishes the pairing principle: soft curvature breeds strong pairing, hard curvature suppresses it (crystal geometry, Sec. 5.2).

This is the Peotta-Torma superfluid density, computed from the quantum geometric tensor of the Bogoliubov eigenstates. It measures the response of the BCS free energy to an imposed phase twist in each Lie algebra direction. It is a RESPONSE function, immune to the truncation-dominance that killed the character coherence probe (COHERENCE-RESPONSE-47 ARTIFACT).

### 5.2 W4-2: Decoupled from Friction (Three Theorems)

The rho_s tensor was shown to be structurally decoupled from the Landau-Zener friction that drives the transit (three independent theorems in the coherence response document). This means rho_s is a ground-state property -- it characterizes the equilibrium condensate, not the non-equilibrium transit dynamics. It can change only if the gap function Delta_s(tau) changes, not because of dissipation during transit.

In 3He, the analog is that the superfluid density rho_s(T) is an equilibrium thermodynamic quantity measured by second sound or torsional oscillators, not by the quench dynamics that created the superfluid state. The quench creates vortices and textures; rho_s describes the stiffness of the equilibrium condensate.

### 5.3 W5-1: Determines Fabric Phase Order (TEXTURE-CORR-48, PASS)

The rho_s tensor enters the Josephson coupling as J = |E_cond| * rho_s^{dir} * f_overlap. The 24x anisotropy in rho_s translates directly into 24x anisotropy in J, which produces the anisotropic phase ordering: C^2 ordered (T/J = 0.12), su(2)/u(1) disordered (T/J = 1.9-2.9).

The chain is:

    BCS pairing -> rho_s tensor -> Josephson coupling -> phase order -> texture spectrum -> P(K) ~ K^{-2}

Every link is grounded in the microscopic Hamiltonian. The Dirac operator D_K provides the single-particle spectrum. The BCS instability (S35: RG-BCS-35, 1D theorem) produces the gap Delta_s(tau). The gap determines the Bogoliubov eigenstates, from which rho_s is computed via the Peotta-Torma formula. The Josephson coupling follows from rho_s and the condensation energy. The phase fluctuation spectrum follows from the Josephson model on the tessellation. At no point does one invoke an effective field theory without UV completion.

### 5.4 The Three Appearances as a Single Object

The rho_s tensor is the single most informative physical quantity in the framework. It encodes:
1. The microscopic BCS state (through the Bogoliubov eigenstates)
2. The geometric environment (through the curvature anti-correlation)
3. The macroscopic fabric texture (through the Josephson coupling)

This is exactly what the superfluid density does in 3He. It connects the microscopic pairing state (BCS gap function) to the macroscopic observables (second sound velocity, critical current, flux quantization). The rho_s tensor is the bridge between the single-cell crystal and the 32-cell fabric.

---

## 6. Pre-Registered Computations for S48

### 6.1 GOLDSTONE-MASS-48

**What**: Compute the mass of the U(1)_7 Goldstone mode from the spectral action second derivative.

**Method**: For a BCS state with U(1)_7 phase phi, the Dirac operator transforms as D_K(phi) = exp(i*phi*K_7) * D_K * exp(-i*phi*K_7). The spectral action S(phi) = Tr(f(D_K(phi)^2 / Lambda^2)) depends on phi through the phi-dependence of the eigenvalues. Compute:

    m_G^2 = (1/rho_s) * d^2 S / dphi^2 |_{phi=0}

using the existing Dirac spectrum at the fold (992 modes) and the cutoff function f from CUTOFF-F-44.

**Input**: Dirac eigenvalues at fold (s44_dos_tau.npz), K_7 matrix elements (s34), cutoff function coefficients (s44_cutoff_f.npz), rho_s(C^2) = 7.962 (s47_rhos_tensor.npz).

**Pre-registered gate**:
- PASS: m_G/M_KK in [10^{-60}, 10^{-50}] (within 6 orders of the required 3.2 x 10^{-56})
- INFO: m_G computable but outside this range
- FAIL: d^2 S / dphi^2 = 0 identically (U(1)_7 is an exact spectral symmetry, no mass generated)

**Expected result**: FAIL. From S34, [iK_7, D_K] = 0 at all tau -- the K_7 symmetry is EXACT in the Dirac spectrum. If D_K commutes with K_7, then D_K(phi) = D_K for all phi, and d^2 S / dphi^2 = 0 identically. The U(1)_7 Goldstone is EXACTLY massless in the spectral action. No mass is generated.

This would be a structural result: the spectral action cannot provide the Goldstone mass because the very symmetry whose breaking generates the Goldstone (U(1)_7) is an exact symmetry of the Dirac operator. The mass must come from a source outside the spectral action -- perhaps the non-commutativity of K_7 with inner fluctuations at the non-singlet level ([iK_7, D_phys] = 0.052 overall, S35), or from a gravitational coupling not captured by the spectral action on the internal space alone.

**Who**: Landau or Spectral-Geometer (requires Dirac spectrum manipulation)

### 6.2 ANISO-OZ-48

**What**: Compute the full anisotropic Ornstein-Zernike power spectrum on a 3D tessellation (4x4x2 = 32 cells) with direction-dependent Josephson coupling and a Goldstone mass from candidate (a) or (b) of Section 3.3.

**Method**: Build the 32x32 stiffness matrix M_{ij} for a 3D periodic lattice with J_xy = J_C2 and J_z = J_su2 (anisotropic coupling). Add a diagonal mass term m^2 * delta_{ij} parametrized by m/J. Compute P(K) = T / (eigenvalue spectrum of M + m^2) and extract n_s as a function of m/J.

**Input**: J_C2 = 0.933, J_su2 = 0.059, T_acoustic = 0.112 (from s47_texture_corr.npz). Mass m treated as a free parameter scanned over [10^{-3}, 10^{3}] in units of J_C2.

**Pre-registered gate**:
- PASS: There exists m/J such that n_s(K_pivot, m) = 0.965 +/- 0.01, AND this m produces a physically reasonable xi (not requiring fine-tuning beyond what q-theory provides)
- INFO: The O-Z form produces n_s = 0.965 at some m (trivially true), but the required m has no identified microscopic origin
- FAIL: The anisotropic coupling or 3D geometry qualitatively alters the O-Z form so that n_s = 0.965 cannot be achieved

**Expected result**: INFO. The O-Z form will trivially produce n_s = 0.965 at the right m/J (this is the definition of the O-Z correlation length). The non-trivial content is whether the 3D anisotropic geometry introduces corrections to the simple 1D ring result. These corrections could come from: the anisotropic lattice dispersion sin^2(K_a / 2) in 3D, the mixing of C^2 and su(2) couplings, or the finite number of cells in each direction (4x4x2 is highly anisotropic).

**Who**: Landau (computational, builds on TEXTURE-CORR-48 code)

### 6.3 CHI-Q-PHASE-48

**What**: Compute the q-theory susceptibility chi_q = d^2 rho_vac / dtau^2 decomposed into contributions from the phase sector (Goldstone) and the amplitude sector (Higgs-like). Determine whether the phase sector contributes to the restoring force at the q-theory crossing tau* = 0.209.

**Method**: The vacuum energy rho_vac = E_spec + E_cond. Both depend on tau. Add a U(1)_7 phase twist phi at each tau: rho_vac(tau, phi). Compute chi_q(tau) = d^2 rho_vac / dtau^2 and chi_phi(tau) = d^2 rho_vac / dphi^2 independently. The ratio chi_phi / chi_q determines how much of the vacuum stiffness comes from phase rigidity versus amplitude rigidity.

**Input**: Dirac spectrum at 5 tau values (s44_dos_tau.npz), BCS gaps (s46_qtheory_selfconsistent.npz), K_7 matrix (s34).

**Pre-registered gate**:
- PASS: chi_phi / chi_q > 0.1 (phase sector contributes >10% of vacuum stiffness)
- INFO: chi_phi / chi_q measurable but < 0.1
- FAIL: chi_phi = 0 (U(1)_7 exact symmetry makes phase sector invisible to q-theory)

**Expected result**: FAIL, for the same reason as GOLDSTONE-MASS-48: if [iK_7, D_K] = 0, the spectral action is independent of phi, and chi_phi = 0. The q-theory vacuum stiffness comes entirely from the amplitude sector (tau-dependence of eigenvalues and gaps), not from the phase sector.

**Who**: Volovik (this is q-theory, my territory)

---

## 7. Structural Assessment

### 7.1 What the Texture Route Achieved

The texture spectrum is the first mechanism to produce a non-trivial fabric-level power spectrum from the microscopic BCS Hamiltonian. The K^{-2} slope is topologically protected by the Goldstone theorem applied to the broken U(1)_7. The anisotropic phase ordering is a genuine prediction of the rho_s tensor computed from first principles. The 8.3 sigma discrepancy from Planck is two orders of magnitude closer than any single-cell route.

### 7.2 What Remains Obstructed

Two obstructions persist.

**The mass problem.** The n_s = 0.965 tilt requires a Goldstone mass m = 3.2 x 10^{-56} M_KK. The spectral action likely cannot generate this mass because [iK_7, D_K] = 0 makes U(1)_7 an exact symmetry of the Dirac operator. The mass must come from physics outside the spectral action: inner fluctuations, gravitational coupling, or a secondary phase transition at a macroscopic scale. This is a well-defined open problem.

**The scale problem.** The corrected correlation length xi = 2.67 Mpc sits in the 56-decade gap between internal (M_KK^{-1} ~ 10^{-55} Mpc) and external (l_cell ~ 4500 Mpc) scales. No known framework mechanism generates structure at this intermediate scale. Tesla's exhaustive enumeration (SCALE-BRIDGE-48) found nothing within a factor of 50. The scale problem IS the cosmological constant problem in a different guise: the hierarchy m/M_KK ~ 10^{-56} is the same hierarchy Lambda/M_Pl^4 ~ 10^{-122}.

### 7.3 The Honest Framing

The texture route has changed the n_s crisis from a MECHANISM crisis to a SCALE crisis. All single-cell routes failed because the mechanism was wrong -- pair creation within a cell gives a steep power law from |beta_k|^2 ~ (Delta/omega)^4, regardless of parameter values. The texture route has the right mechanism -- Goldstone phase fluctuations across the fabric -- with a topologically protected spectral shape. But it needs a mass at a scale that the framework does not naturally produce.

In q-theory language: the Goldstone mass is set by the equilibrium vacuum perturbation at the relevant epoch. If the framework's U(1)_7 Goldstone is massive because of perturbations at the recombination epoch (quasiparticle thermal bath, matter-radiation transition), then the required mass m ~ 2.4 x 10^{-39} GeV ~ T_recomb is naturally at the right scale. But this would require the Goldstone mass to be dynamical -- running with cosmic epoch through q-theory self-tuning -- which is a prediction that no session has yet tested.

### 7.4 Connection to q-Theory

The mass problem connects directly to the q-theory program. In Papers 15-16, the vacuum energy is self-tuned to zero in equilibrium, with the residual Lambda proportional to the perturbation energy. The Goldstone mass is a vacuum property -- it is part of the spectrum of small fluctuations around the vacuum state. If q-theory self-tuning operates on the Goldstone sector (not just the tau sector), then the Goldstone mass is determined by the equilibrium condition:

    d(rho_vac) / d(m^2) = 0

This is a thermodynamic identity: the vacuum adjusts its Goldstone mass to minimize the total vacuum energy, just as the vacuum adjusts its q-parameter (tau) to minimize rho_vac. The equilibrium mass would be set by the perturbation energy at each epoch:

    m^2 ~ rho_perturbation / rho_s ~ (T^4 or rho_matter) / rho_s

At recombination (T ~ 0.3 eV, rho_matter ~ rho_radiation ~ (0.3 eV)^4 / (hbar c)^3):

    m ~ T^2 / sqrt(rho_s * M_KK^2) ~ (0.3 eV)^2 / sqrt(7.96 * (10^{19} GeV)^2) ~ 10^{-39} GeV

This is within an order of magnitude of the required m = 2.4 x 10^{-39} GeV. I state this as a PRELIMINARY estimate, not a derivation. The computation requires specifying how rho_s enters the q-theory self-tuning for the Goldstone sector, which is a well-defined computation for S48.

---

## 8. Summary Table

| Aspect | Status | Key Number | Next Step |
|:-------|:-------|:-----------|:----------|
| P(K) shape | PASS (K^{-2}, topological) | alpha = -1.955 (low-K) | Confirmed |
| Phase ordering | PASS (anisotropic) | xi(C^2) = 532 cells | Confirmed |
| n_s from gradient | 8.3 sigma from Planck | n_s = 1 (HZ) | Need mass m |
| Goldstone mass | OPEN | m_required = 3.2e-56 M_KK | GOLDSTONE-MASS-48 |
| Scale bridge | FAIL (56 decades) | xi = 2.67 Mpc (corrected) | q-theory Goldstone self-tuning |
| Acoustic horizon | FAIL (60 OOM) | d_acoustic = 10^{-58} Mpc | Confirmed closed |
| Algebra error | Acknowledged | 2.67 Mpc, not 151 Mpc | Corrected in all future work |

---

## 9. Files

**Source data**:
- `tier0-computation/s47_texture_corr.npz` (TEXTURE-CORR-48 data)
- `tier0-computation/s47_texture_corr.py` (computation script)
- `tier0-computation/s47_texture_corr.png` (6-panel figure)

**Source documents**:
- `sessions/session-47/session-47-wave1-workingpaper.md` (W5-1 section, Landau)
- `sessions/session-47/session-47-scale-bridge.md` (Tesla, algebra correction)
- `sessions/session-47/session-47-ns-reassessment.md` (Volovik, 11 routes closed)
- `sessions/session-47/session-47-crystal-geometry.md` (Tesla, crystal synthesis)
- `sessions/session-47/session-47-volovik-coherence-response.md` (Volovik, rho_s as right probe)
- `sessions/session-plan/session-47-wave5-texture.md` (Volovik, wave5 plan -- contains algebra error at line 225)

**Papers cited**:
- Paper 01: Universe in a Helium Droplet (Ch. 7.3: textures, Ch. 6.2: O-Z correlations)
- Paper 02: Superfluid Analogies, Cosmological (Sec. IV: Kibble-Zurek)
- Paper 05: Vacuum Energy, Cosmological Constant (equilibrium theorem)
- Paper 14: Topological Defects, Cosmological Implications (Sec. I-III: domain correlations)
- Paper 15: Self-Tuning Vacuum (q-theory equilibrium)
- Paper 16: Gluonic Vacuum Q-Theory
- Paper 22: Elasticity Tetrads, Emergent Gravity
- Paper 27: Superfluids, Non-Equilibrium Quantum Vacua
- Paper 37: Landau-Khalatnikov Two-Fluid, de Sitter
