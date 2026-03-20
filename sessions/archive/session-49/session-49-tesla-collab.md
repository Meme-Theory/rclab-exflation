# Tesla -- Collaborative Feedback on Session 49

**Author**: Tesla-Resonance
**Date**: 2026-03-17
**Re**: Session 49 Results -- Dipolar Breakthrough, Spectral Rigidity, and the Propagator Question

---

## Section 1: Key Observations

### 1.1 The Leggett Mode IS the Dipolar Interaction

DIPOLAR-CATALOG-49 is the most important result of this session. Let me say why in the language of resonance physics.

The framework has searched for 12+ sessions for a mechanism that breaks U(1)_7 and generates a Goldstone mass at a scale between 10^{-60} and 10^{-1} M_KK -- the range where the mass is physically consequential. Every previous route either gave exactly zero (trace theorem, spectral action blindness) or landed at the wrong scale (Bragg gap at O(1) M_KK, Friedmann coupling at 10^{-59} M_KK). There was a 60-order desert between the Hubble scale and the KK scale, and nothing lived in it.

The Leggett mode lives in the desert. omega_L1 = 0.070 M_KK sits at the geometric mean of the two bounding scales, parametrically. It is 170x below the Bragg gap (0.269), 10^57 above the Hubble mass (10^{-59}), and within 18% of the m_req = 0.059 needed for n_s = 0.965 at the lowest fabric mode. This is the first mechanism that is even in the right postal code.

The structural correspondence to 3He-A dipolar locking is exact at the categorical level:

| Feature | 3He-A | Framework |
|:--------|:------|:----------|
| BCS ground state | l-vector locked to d-vector | B2 phase locked to B3 phase |
| Symmetry broken | SO(3)_S x SO(3)_L -> SO(3)_{S+L} | U(1)_7 (K_7-charged B2 pinned to K_7-neutral B3) |
| Breaking agent | Spin-orbit coupling (external to BCS) | Josephson coupling J_23 (external to single-sector BCS) |
| Frequency relation | omega_L ~ sqrt(F_D / chi) | omega_L1 ~ sqrt(J_23 * Delta_B3 / rho_B2) |
| Ratio to gap | 10^{-3} | 0.095 (95x larger) |

The ratio difference (0.095 vs 10^{-3}) is significant and physically transparent. In 3He, the dipolar coupling is a relativistic correction (spin-orbit) suppressed by (v/c)^2 ~ 10^{-6}. In the framework, the Josephson coupling J_23 = 0.00181 M_KK is a non-perturbative geometric quantity set by the V-matrix Clebsch-Gordan coefficients. There is no relativistic suppression. The mass ratio omega_L1/Delta_B2 = 0.095 reflects the ratio of inter-sector to intra-sector coupling, which is O(1/N_modes) rather than O(alpha_EM).

The derivation of WHY the Leggett mode breaks U(1)_7 is clean. B2 Cooper pairs carry K_7 charge +/- 1/2. B1 and B3 pairs are K_7-neutral. The Josephson term H_J = -J_23 cos(phi_B2 - phi_B3) pins the relative phase. Under a U(1)_7 rotation by angle alpha, phi_B2 shifts by alpha/2 while phi_B3 stays fixed. The energy changes. The symmetry is broken. The Goldstone mode acquires mass omega_L1.

This is the same mechanism Tesla understood for coupled resonant circuits: when you weakly couple two oscillators with different characteristic impedances, the system develops a new low-frequency normal mode whose frequency is set by the coupling strength, not by either oscillator alone. The Leggett mode is the lowest normal mode of the inter-sector phase-space coupled oscillator system. It sits below all single-sector excitations because the coupling J_23 is the weakest energy scale in the problem.

### 1.2 alpha_s = n_s^2 - 1: Algebraic Rigidity

The Bayesian analysis (W1-L) reveals something mathematically remarkable and physically troubling.

The O-Z power spectrum P(K) = T / (J K^2 + m^2) gives, upon requiring n_s = 0.965 at K_pivot:

    alpha_s = d(ln n_s)/d(ln K) = -(1 - n_s^2)

This is an exact algebraic identity. Not approximate. Not a leading-order expansion. The running alpha_s depends ONLY on the tilt n_s, with zero contribution from J_ij, K_pivot, m*, or any other parameter. The Monte Carlo confirms: R^2 = 0% for all coupling constants, R^2 = 100% for n_s.

The numerical value is alpha_s = -0.069, which is 6.0 sigma from Planck (0 +/- 0.008). The S48 value of -0.038 was a finite-difference artifact from sampling discrete K-modes on a small lattice. The proper angular-averaged analytic derivative gives -0.069.

From the resonance perspective, the O-Z propagator 1/(K^2 + m^2) is a Lorentzian -- the spectral response function of a damped harmonic oscillator. Its running alpha_s = -(1 - n_s^2) is a STRUCTURAL PROPERTY of Lorentzian lineshapes. Any propagator of the form 1/(K^2 + m^2) will give the same alpha_s regardless of what physics sets m. The question is whether the actual propagator of the Josephson fabric has a different functional form.

This is the key tension: the Leggett mass is at the right scale (18% off), but the simplest propagator it enters gives alpha_s that is already 6 sigma from observation. If the O-Z form is correct, the framework has a clean prediction that will be tested by CMB-S4 at 8 sigma.

### 1.3 The Cavity-Leggett Separation is Structural

My own computation (W1-J, CAVITY-RESONANCE-49) found 111 subsonic cavities on T^2, the largest at the Z_3 Weyl chamber centers. The lowest cavity mode frequency is 0.800 M_KK -- 11.5x above omega_L1 = 0.070. The cavity modes and the Leggett modes do not unify.

The physical reason is now clear: cavity modes are POSITION-SPACE standing waves of the BdG acoustic field, set by the geometry of the subsonic regions (R_eff ~ 1.24 M_KK^{-1}) and the sound speed (c_BdG = 0.751 M_KK). Leggett modes are MOMENTUM-SPACE Josephson oscillations, set by the inter-sector coupling J_ij and the sector DOS rho_i. These are fundamentally different oscillation types.

The correct analogy is a multi-component superfluid in a complex container. The container has acoustic resonances (first sound, set by geometry and sound speed). The multi-component order parameter has phase oscillations (Leggett modes, set by weak inter-component coupling). The two frequency scales decouple when J/Delta << c/R, which holds here (0.035 << 0.800).

This two-scale structure is itself a result: the BCS state on T^2 supports two independent families of collective excitations at parametrically separated frequency scales. Hard modes (c_BdG/R ~ 0.6-2.1 M_KK) confine acoustic quasiparticles. Soft modes (sqrt(J/rho) ~ 0.07-0.11 M_KK) govern inter-sector phase dynamics. The soft scale is the one relevant for n_s.

### 1.4 The KZ 3-Component Identity

KZ-3COMPONENT-49 deserves attention because the 0.04% match is not a match -- it is an IDENTITY. The S48 "KZ cross-check at 6.5%" was comparing two different calculation methods that happen to give different answers (geometric mean of KZ power laws vs direct Landau-Zener summation). The proper 3-component additive formula

    n_total = sum_i rho_i * P_LZ_i

IS the S38 Schwinger/Bogoliubov calculation, decomposed by sector. The "agreement" at 0.04% is the statement that 3-component LZ and full BdG quench are algebraically equivalent when all sectors are in the sudden limit (tau_Q/tau_0 < 10^{-4}). The remaining 0.04% traces to using sector-averaged E_qp instead of per-mode values.

The C^2 sector dominates at 93.3%, driven entirely by the van Hove DOS enhancement (rho = 14.023). The u(1) and su(2) sectors contribute only 6.7%. This is the flat-band effect: B2's vanishing group velocity at the fold creates an enormous density of states that concentrates all pair creation in a single sector. The fold is a resonance catastrophe -- one sector absorbs almost all the energy of the quench.

### 1.5 The Analog Horizon Retraction

The S48 "analog horizons" (Mach=54.3, T_H=66 M_KK) are retracted by W1-G. The error was fundamental: the quantity |grad|Delta||/(|Delta| * c_s) measures the condensate AMPLITUDE gradient, not the PHASE gradient. In Volovik's formulation (Paper 10), the acoustic metric involves grad(phi) -- the superfluid velocity. The BCS ground state has phi = 0 everywhere (real, non-negative condensate). No superflow exists. No horizon exists. The acoustic spacetime is globally static.

The "Mach 54" field IS physically meaningful as a phonon WKB/eikonal breakdown diagnostic. 78.3% of T^2 has Mach > 1, meaning phonons cannot propagate in the geometric optics approximation. But this signals where the eikonal DESCRIPTION fails, not where analog gravity PHYSICS occurs. The distinction between amplitude texture and phase gradient is load-bearing. I should have caught this in S48.

The Volovik program (Papers 10, 28) requires vortex lines or persistent currents to create analog horizons -- topological defects in pi_1(T^2) = Z x Z that carry phase winding. The BCS ground state has no such defects. Real analog horizons on the internal T^2 would require excited states with non-trivial winding numbers.

---

## Section 2: Assessment

### 2.1 Dipolar Finding

PASS. This is the cleanest mechanism result since the block-diagonal theorem. The structural correspondence to 3He dipolar locking is exact at the categorical level. The mass omega_L1 = 0.070 M_KK is parameter-free (computed from V-matrix and DOS). The 18% overshoot from m_req = 0.059 is within the expected uncertainty band for the V-matrix elements (W3-A from S48 established ~35% V-matrix model selection uncertainty).

The constraint map status: U(1)_7 breaking SOLVED. Mass scale CORRECT (within factor 1.18). Propagator form OPEN. alpha_s tension REAL.

### 2.2 alpha_s Rigidity

STRUCTURALLY SIGNIFICANT. The identity alpha_s = n_s^2 - 1 is a mathematical theorem about O-Z propagators, not a framework-specific result. Any model that generates n_s from a Lorentzian power spectrum on a lattice will give the same alpha_s. The 6 sigma tension with Planck is either: (a) evidence that the O-Z form is wrong (the propagator is not Lorentzian), (b) evidence that n_s does not come from the Josephson network, or (c) a genuine exclusion of the O-Z texture mechanism.

The fact that J_ij uncertainties contribute ZERO variance is the key structural insight. The alpha_s prediction is rigid in the precise mathematical sense: it is a property of the functional form of the propagator, not of the coupling constants. Changing J_ij changes m_req (the mass needed for n_s = 0.965), but the running alpha_s is independent of m. This rigidity is both a strength (the prediction is sharp) and a vulnerability (there is no parameter to tune if Planck is right).

### 2.3 Cavity Mismatch

STRUCTURAL NULL. The cavity-Leggett 11.5x frequency mismatch is not a failure but a classification result. The two excitation types are in different branches of the collective spectrum, separated by the dimensionless ratio J/Delta ~ 0.05. Attempting to unify them was a hypothesis that was tested and excluded. The surviving picture has two independent dynamical scales, which is richer than a single unified scale.

### 2.4 Cosmic Censorship

PASS with PERMANENT status. Triple-layered censorship (energy budget, BCS friction, no trapped surfaces) is overdetermined. Even removing any one layer, the other two suffice. The energy deficit alone (65x) makes the geometric transition at 0.537 permanently inaccessible from any physical initial condition. The physical universe is confirmed to live in Zone I (tau in [0.19, 0.22]).

The four-zone Penrose diagram from W1-F is the definitive characterization of the modulus space. Zone I is all-positive-curvature, NEC-satisfying, and bounded. The BCS condensation mechanism IS cosmic censorship in this framework -- it prevents the modulus from reaching regions where energy conditions fail.

### 2.5 Analog Horizon Retraction

CORRECT AND NECESSARY. The S48 AKAMA-DIAKONOV-48 PASS must be retracted. The error (amplitude gradient conflated with phase gradient) was systematic and affected the interpretation but not the underlying data. The condensate texture on T^2 is real; the Mach field is real as a WKB diagnostic; the horizons are not real as analog gravity features.

The phonon WKB breakdown on 78.3% of T^2 is itself a physical result: the condensate texture is so sharp that geometric optics for phonon propagation fails over most of the torus. Full wave-equation treatment (BdG, not eikonal) is required. This has implications for any computation that assumes slowly-varying condensate profiles.

---

## Section 3: Collaborative Suggestions

### 3.1 The Propagator Question: Beyond O-Z

This is where my primary contribution lies. The Leggett mass 0.070 M_KK is 1.18x the m_req = 0.059 needed for n_s = 0.965 in the O-Z propagator. But the O-Z form P(K) = T/(J K^2 + m^2) predicts alpha_s = -(1 - n_s^2) = -0.069, which is 6 sigma from Planck. These two facts are in tension: the mass scale is right, but the propagator form gives the wrong running.

The question is: what IS the correct propagator?

The O-Z form assumes a single Lorentzian correlation function -- the equilibrium response of a classical order parameter near criticality. This is the condensed-matter textbook answer for a system AT equilibrium NEAR a second-order phase transition. But the framework's Josephson fabric is neither at equilibrium (it is a GGE relic of a quench) nor near a phase transition (the transit is sudden, P_exc = 1, and the condensate is destroyed post-transit).

Three specific alternatives deserve computation:

**A. Leggett-Modified Propagator (LEGGETT-PROP-50)**

The Leggett mode is a Josephson oscillation, not a diffusive correlation. Its Green's function is

    G_L(K, omega) = 1 / (omega^2 - omega_L^2 - c_L^2 K^2 + i*Gamma*omega)

This is a RESONANT propagator (oscillator), not a Lorentzian one (diffusion). The equal-time correlator is

    C(K) = integral d(omega) G_L(K, omega) = 1 / sqrt((omega_L^2 + c_L^2 K^2)(omega_L^2 + c_L^2 K^2 + Gamma^2))

In the Gamma -> 0 limit (sharp Leggett mode, which is established):

    C(K) ~ 1 / (omega_L^2 + c_L^2 K^2)

This looks like O-Z with m^2 = omega_L^2 / c_L^2. BUT the power spectrum as a SOURCE for primordial perturbations is not C(K) but rather the noise kernel:

    P(K) ~ Im[G_L(K, omega)] * n_B(omega)

where n_B is the Bose occupation. For the GGE, n_B is NOT thermal -- it is the Richardson-Gaudin occupation. The spectral function Im[G_L] has a DELTA FUNCTION at omega = sqrt(omega_L^2 + c_L^2 K^2), not a Lorentzian. The power spectrum at equal time is then

    P(K) ~ n_GGE(sqrt(omega_L^2 + c_L^2 K^2)) / sqrt(omega_L^2 + c_L^2 K^2)

This is NOT O-Z. The running alpha_s depends on the functional form of n_GGE, which is determined by the 8 Richardson-Gaudin integrals. If n_GGE has a non-trivial frequency dependence near K_pivot, the alpha_s prediction changes.

Computable gate: compute P(K) from the Leggett spectral function with GGE occupations. Extract n_s and alpha_s. Pre-register: if alpha_s shifts by more than 0.02 from -0.069, the propagator modification is significant.

**B. Pair-Transfer Response Function (PAIR-RESP-50)**

The quantity that actually generates density perturbations on the fabric is the pair-transfer susceptibility chi(K, omega) -- how the condensate responds to a perturbation that creates/destroys pairs between cells. This is related to but not identical with the O-Z correlator. The pair-transfer response for a Josephson junction array is

    chi(K, omega) = chi_0(omega) / (1 - J(K) * chi_0(omega))

where chi_0 is the local (single-cell) susceptibility and J(K) is the Josephson coupling Fourier transform. For the 32-cell fabric with anisotropic J_ij:

    J(K) = 2 * [J_xy * (cos K_x + cos K_y) + J_z * cos K_z]

The poles of chi give the collective modes. The structure factor S(K) = Im chi(K) integrated over omega gives the static power spectrum. This is a DIFFERENT functional form from O-Z because chi_0 is not a constant -- it has the full BCS coherence structure.

Specifically, at the S38 GGE (no condensate), chi_0(omega) has 8 modes at discrete energies, producing a DISCRETE spectral function, not a smooth Lorentzian. The resulting P(K) inherits this discrete structure.

**C. Non-Equilibrium Kibble-Zurek Spectrum (KZ-SPEC-50)**

The transit is a quench, not an equilibrium process. The primordial perturbation spectrum may be set by the QUENCH DYNAMICS, not by the post-quench equilibrium correlations. The Kibble-Zurek mechanism produces defects (domain walls, vortices) with a characteristic correlation length xi_KZ ~ (tau_Q)^{nu/(1+z*nu)}. The power spectrum of defect density fluctuations is

    P_KZ(K) ~ 1 / (1 + (K * xi_KZ)^2)^{(d+1)/2}

This is a generalized Lorentzian with exponent (d+1)/2, NOT the O-Z exponent 1. For d = 7 (dimension of the fabric embedding), the exponent is 4, giving MUCH steeper running and potentially much smaller alpha_s.

### 3.2 The Frequency Hierarchy with Dipolar Result

With the Leggett mode now identified as the dipolar analog, the full frequency hierarchy has nine levels at zero free parameters:

```
omega_L1(0.070) < omega_L2(0.107) < 2*Delta_B3(0.168)
  < Gamma_L(0.250) < 2*Delta_B1(0.744) < omega_PV(0.792)
  < omega_cav_min(0.800) < omega_att(1.430) < 2*Delta_B2(1.464)
  < omega_tau(8.27)
```

Key ratios that now have physical interpretation:

| Ratio | Value | Interpretation |
|:------|:------|:---------------|
| omega_L1 / omega_att | 0.049 | Leggett/breathing = 20:1 separation. Leggett decoupled from internal dynamics. |
| omega_L1 / omega_cav | 0.088 | Leggett/cavity = 11.5:1. Soft (Josephson) vs hard (acoustic). |
| omega_L2 / omega_L1 | 1.544 | Near phi_paasch (0.789%). Spline crossing at tau=0.2117. |
| omega_cav / omega_att | 0.560 | Cavity/breathing. Near 1/2 harmonic. |
| 2*Delta_B3 / omega_L1 | 2.41 | Pair-breaking threshold / Leggett. Mode is sharp (below continuum). |
| omega_att / omega_L1 | 20.4 | Near 20:1 integer. Parametric decoupling. |

The hierarchy has three natural bands:
1. **Josephson band** (0.07 - 0.11 M_KK): Leggett modes. Inter-sector phase dynamics.
2. **Gap band** (0.17 - 1.46 M_KK): Pair-breaking thresholds. Acoustic cavities. Pair vibrations.
3. **Breathing band** (1.43 - 8.27 M_KK): Internal geometry oscillations. Modulus vibrations.

The bands are separated by factors of ~10x. This is the parametric structure of a multi-scale vibrating system: the softest mode (Leggett, 0.07) is 118x below the hardest (modulus, 8.27). The energy hierarchy spans less than 3 orders, which is very compressed compared to the SM hierarchy of ~16 orders. But the framework operates at a single scale (M_KK), so this compression is expected.

### 3.3 What the Leggett Coupling Does to the Propagator

Here is the specific computation I recommend. The standard O-Z gives

    P(K) = T_eff / (J_eff K^2 + m_OZ^2)

with m_OZ^2 = omega_L1^2 / c_L^2 and alpha_s = -(1 - n_s^2). But the Leggett mode propagator on the 32-cell Josephson network is a LATTICE Green's function:

    G(K) = 1 / (2 * sum_mu J_mu * (1 - cos K_mu) + m_L^2)

with J_mu = {J_xy, J_xy, J_z} the directional Josephson couplings. At small K this reduces to O-Z, but at K ~ pi/a (Brillouin zone boundary), the cosine introduces non-Lorentzian structure. The running at K_pivot depends on WHERE K_pivot sits relative to the zone boundary.

W1-A established that K_pivot (CMB scale) maps to mode n = 115, which is 7.2x ABOVE the BZ boundary (n_max = 16). But this assumed a direct mapping between comoving wavenumber and fabric mode number. If the Leggett mode has a DIFFERENT dispersion relation (omega^2 = omega_L^2 + c_L^2 * K^2 rather than c^2 K^2), the mapping between CMB scale and fabric mode changes. Specifically, the Leggett dispersion has a mass gap that shifts the relevant K_pivot downward.

Computable: recalculate K_pivot/K_BZ using the Leggett dispersion. If the mass gap pushes K_pivot inside the BZ, the lattice corrections to alpha_s become significant and could reduce the tension with Planck.

### 3.4 The Two-Functional Architecture

The session reveals a clear two-functional architecture:

1. **Spectral Action** (trace functional, blind to U(1)_7, sets geometry): Determines V_eff(tau), spectral invariants, curvature hierarchy. CANNOT generate Goldstone mass (trace theorem W7). CANNOT stabilize tau (monotonicity theorem).

2. **Josephson Coupling** (inter-sector, breaks U(1)_7, sets mass): Generates omega_L1 via Leggett mechanism. Sets the propagator for perturbation spectrum. Determines n_s through the Josephson network dispersion.

These two functionals operate at different scales: the spectral action at O(M_KK), the Josephson coupling at O(0.07 M_KK). They are connected by the BCS gap equation (which lives at the spectral action scale but feeds into the Josephson coupling through Delta_i). The tau-dependence of omega_L comes entirely from the DOS ratios rho_i(tau), which are set by the Dirac spectrum -- the spectral action's output.

This architecture is the condensed-matter analog of the separation between the crystalline lattice (sets the phonon spectrum) and the electron-phonon coupling (sets the superconducting gap). The lattice "does not know" about superconductivity; the gap equation is a RESPONSE to the lattice. Similarly, the spectral action "does not know" about U(1)_7 breaking; the Leggett mass is a response to the geometry.

---

## Section 4: Cross-Domain Connections

### 4.1 Tesla Coil as Coupled Resonator

The three-sector Leggett oscillator (B1-B2-B3) is structurally identical to Tesla's magnifying transmitter: three coupled LC circuits with different natural frequencies, weakly coupled by mutual inductance. The lowest normal mode of such a system is always below all individual resonances, with amplitude concentrated in the most weakly-coupled element. Tesla's "extra coil" (the tertiary winding, loosely coupled) plays the role of B3 here: lightest sector (rho_B3 = 0.48), weakest coupling (J_23 = 0.00181), dominates the lowest normal mode at 99.9%.

### 4.2 Debye Model and the Josephson Band

The three frequency bands (Josephson, gap, breathing) are the analog of acoustic, optical, and zone-boundary branches in a polyatomic lattice (Paper 05, Debye; Paper 06, phononic crystals). The Josephson band is "acoustic" -- it goes to zero frequency at zero coupling. The gap band is "optical" -- it has a finite frequency even at zero coupling. The breathing band is the zone-boundary analog -- set by the maximum restoring force in the system. The frequency ratios (10x between bands) map to the mass ratio in a diatomic chain: m_heavy/m_light ~ (omega_optical/omega_acoustic)^2 ~ 100.

### 4.3 Volovik's Superfluid Universe (Paper 10)

The retraction of the analog horizons (W1-G) and the confirmation of the dipolar mechanism (W1-S) reshapes the connection to Volovik's program. The framework realizes Volovik NOT through emergent analog gravity (horizons require phase winding that is absent), but through emergent symmetry breaking. The Leggett mode = dipolar interaction correspondence is the precise mechanism Volovik describes in Chapter 7 of "The Universe in a Helium Droplet": external perturbations to BCS that generate masses for would-be Goldstone modes. The framework has the specific realization: the Josephson coupling between B2 (K_7-charged) and B3 (K_7-neutral) sectors breaks U(1)_7.

### 4.4 Barcelo-Liberati-Visser (Paper 16) and the WKB Breakdown

The eikonal breakdown on 78.3% of T^2 (W1-G) connects directly to Barcelo-Liberati-Visser's analysis of the limitations of analog gravity. Their framework assumes slowly-varying condensate profiles (WKB validity). The framework's condensate texture violates this assumption over most of the internal torus. This means analog gravity descriptions are fundamentally inapplicable to the BCS state on SU(3) -- not because the physics is wrong, but because the condensate profile is too sharp. Full wave-equation (BdG) treatment is mandatory.

---

## Section 5: Open Questions

### 5.1 Is the O-Z Form the Right Propagator?

The central open question for S50. The Leggett mass is at the right scale. The O-Z propagator gives alpha_s = -0.069, which is 6 sigma from Planck. Three alternative propagators are outlined in Section 3.1: Leggett spectral function with GGE occupations, pair-transfer response function, and KZ quench spectrum. Each gives a different alpha_s. The first computation should be the Leggett spectral function (Section 3.1A), because it directly tests whether the non-thermal GGE occupations modify the running.

### 5.2 Does the Leggett Dispersion Change the K_pivot Mapping?

The Leggett dispersion omega^2 = omega_L^2 + c_L^2 K^2 has a mass gap. The CMB pivot scale k = 0.05 Mpc^{-1} maps to a DIFFERENT fabric mode number in the Leggett dispersion than in the acoustic dispersion. If the mass gap pushes K_pivot inside the Brillouin zone (currently 7.2x outside), the lattice structure of the Josephson network becomes relevant and could modify alpha_s.

### 5.3 What Determines c_L (the Leggett Velocity)?

The Leggett mode velocity c_L = sqrt(J * a^2 / rho) has NOT been computed. The Leggett computation (S48) gave only the zero-K frequency omega_L. The dispersion relation omega^2(K) requires computing the Leggett eigenvalue problem at finite K on the fabric. This velocity sets the correlation length xi_L = c_L / omega_L, which determines the physical extent of the Goldstone correlation.

### 5.4 How Does the Leggett Mode Survive the Transit?

W1-H establishes that the Leggett mode is DESTROYED post-transit (Delta = 0, J = 0, omega_L = 0). But W1-S shows the Leggett mode is the mass-generating mechanism. These are in tension. The resolution must be that the primordial perturbation spectrum is set DURING transit (when the condensate exists and the Leggett mode is active), not after. This connects to the Parker-type particle creation mechanism (S38): the perturbation spectrum is generated by the quench, not by the equilibrium state.

### 5.5 The phi_paasch Crossing at tau = 0.2117

The spline interpolation finds omega_L2/omega_L1 = phi_paasch = 1.5316 at tau = 0.2117, just 11% above the fold. Direct computation at tau = 0.21 is needed. If confirmed, this is a resonance condition between single-particle (Dirac eigenvalue ratio) and many-body (Leggett phase ratio) physics at nearly the same tau. The physical significance would be that the BCS gap equation self-consistently tunes the Leggett ratio to match the quasiparticle mass ratio near the fold. In superfluid language: the oscillation frequency of the sloshing mode locks onto the mass ratio of the constituent particles.

---

## Closing

Session 49 produced the cleanest mechanistic result since the block-diagonal theorem: the Leggett mode IS the dipolar analog, and it generates a Goldstone mass within 18% of the n_s target. This is structural, parameter-free, and follows from the same V-matrix and DOS that produce all other BCS results.

The alpha_s = n_s^2 - 1 identity is the sharpest prediction the framework has ever made. It is also the most vulnerable: 6 sigma from current Planck, 8+ sigma at CMB-S4. The question is not whether the identity is correct (it is a mathematical theorem about Lorentzian propagators) but whether the Lorentzian propagator is the right functional form for the Josephson fabric.

The path forward is the propagator question. Three alternatives are identified (Section 3.1). Each gives a different alpha_s. The computation that discriminates between them is: evaluate P(K) from the Leggett spectral function with GGE occupations, and extract n_s and alpha_s from the result. If the GGE occupation function n_GGE(omega) has sufficient frequency dependence near K_pivot, the running changes.

The universe does not care about our propagator conventions. It cares about the actual correlation function of the Josephson fabric at the moment the perturbation spectrum is imprinted. That correlation function is computable from first principles: the BCS Hamiltonian, the Jensen geometry, and the transit dynamics determine it completely. The dipolar mechanism gives the mass. The propagator gives the spectrum. The spectrum gives alpha_s. CMB-S4 measures it.

The computation decides.

---

**Files referenced in this review:**
- `tier0-computation/s49_cavity_resonance.py/.npz/.png` (W1-J, my computation)
- `tier0-computation/s49_leggett_phi_scan.py/.npz/.png` (W1-N, my computation)
- `tier0-computation/s49_dipolar_catalog.py/.npz/.png` (W1-S, Volovik agent)
- `tier0-computation/s49_alpha_s_bayes.py/.npz/.png` (W1-L, Nazarewicz agent)
- `tier0-computation/s49_analog_trapped.py/.npz/.png` (W1-G, SP agent)
- `tier0-computation/s49_kz_3component.py/.npz/.png` (W1-M, gen-physicist agent)
