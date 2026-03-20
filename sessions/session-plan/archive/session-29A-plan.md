# Session 29A Plan: The CMB-as-Horizon Evaluation and Backreaction Computation

**Date**: 2026-02-28
**Author**: Hawking (hawking-theorist)
**Motivation**: Session 28 produced the first mechanism to survive computation (Constraint Chain KC-1/2/4/5 PASS, KC-3 CONDITIONAL). Two team syntheses (Dirac+Feynman+SP, Einstein+Hawking+Cosmic-Web) converged unanimously on the same priorities: KC-3 closure + backreaction self-consistency. This plan adds a third dimension: a rigorous evaluation of the "CMB as cosmological horizon of the BCS phase transition" provocation, which provides the physical picture that ORGANIZES the computations.
**Prerequisites**: All Session 28 data files (`s28a_*.npz`, `s28b_*.npz`, `s28c_*.npz`), Session 25 spectral entropy data (`s25_hawking_computations.py` outputs), Session 23a eigenvectors (`s23a_eigenvectors_extended.npz`).

---

## I. The Provocation: Rigorous Evaluation

### 1.1 Statement of the Three Structural Claims

The provocation asserts three structural isomorphisms between the phonon-exflation framework and semiclassical gravity:

**Claim A**: The CMB surface of last scattering IS a cosmological horizon -- the boundary between the condensed BCS phase (our observable universe, tau frozen at 0.35) and the pre-condensation phase (tau evolving, particles being created by KC-1).

**Claim B**: The Big Bang singularity IS the BCS phase transition -- a spacelike surface from which all geodesics emerge. Every spatial point sits on the condensed side. The "singularity" is not a place but a transition.

**Claim C**: The interior of a black hole (r < 2M, shrinking angular sphere) is the time-reverse of our observable universe (expanding from the BCS condensation). The mono-decreasing Euclidean action I_E means Z increases with tau, analogous to black hole evaporation with negative specific heat.

### 1.2 Where the Isomorphism Holds Exactly

**Claim C is the strongest.** The structural parallel between I_E(tau) and black hole evaporation is not a metaphor -- it is a direct consequence of the Euclidean path integral framework (Paper 07, Gibbons-Hawking 1977). Let me be precise.

The spectral action Tr f(D^2/Lambda^2) IS the Euclidean gravitational action evaluated on the internal geometry (Paper 07, combined with the spectral action principle of Chamseddine-Connes). Session 28 proved this is monotonically decreasing for BOTH D_K and D_can, at ALL temperatures and ALL smooth cutoffs (C-1 + L-1). The Euclidean partition function Z = exp(-I_E) therefore INCREASES monotonically with tau. This is thermodynamically identical to a black hole with negative specific heat (Paper 04): as the black hole radiates and loses mass, its temperature increases, driving further radiation. The system is thermodynamically unstable.

Quantitatively:
- Black hole: dM/dt < 0, dT_H/dt > 0 (T_H = 1/(8pi M)), runaway evaporation
- Jensen modulus: dI_E/d(tau) < 0, dZ/d(tau) > 0, runaway deformation
- Both: negative specific heat, no equilibrium in the uncondensed/unresolved sector
- Resolution in BH: quantum gravity (string microstates, etc.) at Planck scale
- Resolution in Jensen: BCS condensation energy creates a metastable well at tau = 0.35

The Hawking-Page transition (Paper 10) provides the precise structural analog: below T_c, the trivial topology (thermal AdS / uncondensed phase) dominates the partition function. Above T_c, the black hole topology (condensed phase) dominates. The BCS first-order transition at tau = 0.35 IS the Hawking-Page transition of the internal geometry, with the correction from Synthesis B (C-7) that it is a CASCADE of transitions across sectors, not a single cusp.

**Claim A has partial validity.** The CMB is indeed associated with a horizon in the conformal/causal sense -- the past particle horizon in standard FRW cosmology. The Gibbons-Hawking temperature of the cosmological horizon is T_dS = H/(2pi) (Paper 07, eq. 1 of my index). For the current Hubble parameter, T_dS ~ 2.4 x 10^{-30} K -- thirty orders of magnitude below the CMB temperature T_CMB = 2.725 K. So the CMB temperature is NOT the Gibbons-Hawking temperature of the current cosmological horizon.

However, if the provocation is read more carefully, the claim is that the CMB encodes the RESIDUAL temperature of the BCS phase transition -- the analog of a cosmological horizon at the EPOCH of the transition, not the current epoch. The internal Gibbons-Hawking temperature I computed in Session 25 is:

$$T_{GH}^{internal}(\tau) = \frac{e^{-2\tau}}{\pi} \tag{1}$$

At tau = 0.35: T_GH^{internal} = e^{-0.70}/pi = 0.158 (in spectral units). This is the temperature at which the internal geometry "freezes" -- the analog of the last scattering surface. The physical CMB temperature is obtained by redshifting this internal temperature through the expansion history. Whether the numbers work out requires the tau-to-cosmic-time mapping, which is precisely the backreaction computation.

So the claim should be reformulated: **the CMB surface of last scattering is the 4D image of the internal BCS phase boundary**. The temperature T = 2.725 K is the internal Gibbons-Hawking temperature at the transition, redshifted to today. This is a specific, testable prediction -- but only once the mapping is computed.

**Claim B is the weakest.** The Penrose diagram of FRW cosmology does have the Big Bang as a spacelike surface from which all geodesics emerge (Paper 01, Hawking-Penrose 1970). Identifying this with the BCS phase transition requires that the transition be a GLOBAL event -- occurring simultaneously at all spatial points. A first-order transition generically proceeds by bubble nucleation (Coleman-De Luccia, Paper 09 context), which is spatially inhomogeneous. The "singularity = phase boundary" identification holds only if the transition is either:

(a) Spatially homogeneous (instantaneous across all space) -- possible if the BCS transition is driven by a spatially homogeneous modulus tau(t) that crosses the critical value simultaneously everywhere, OR

(b) The bubbles percolate so rapidly that the transition is effectively homogeneous on cosmological scales -- requires beta/H >> 1, where beta is the nucleation rate and H is the Hubble rate.

The first option is natural in the framework: the modulus tau is a function of cosmic time only (in the FRW background), so the transition occurs simultaneously at all spatial points. This is the simplification noted in Synthesis B (CP-1): the first-order transition reduces the backreaction from a coupled ODE to a free energy comparison. But it requires that spatial fluctuations of tau are negligible, which is a dynamical question that the backreaction computation must address.

The second option introduces the gravitational wave signature discussed by Cosmic-Web (Section 2.2 of cosmic-web-collab.md). The L-9 cubic invariant c = 0.0055-0.0072 in the (3,0)/(0,3) sectors quantifies the first-order character. Whether this is strong enough for efficient percolation (beta/H >> 1) is an uncomputed quantity.

### 1.3 Where the Isomorphism Breaks

**The CMB is not a causal horizon of the internal geometry.** The cosmological horizon in de Sitter space is a causal boundary: information beyond it is causally inaccessible. The CMB is not a causal boundary of the internal SU(3) -- it is a phase boundary. An observer today CAN, in principle, access information about the pre-condensation phase through relic particles, gravitational waves, or other signatures that were imprinted before the transition. A causal horizon permanently hides information; a phase boundary merely changes the state. Einstein's correction from Synthesis B (C-6) applies: there is no horizon on SU(3), so the GSL does not apply in its strict form. The ordinary second law applies instead.

**The Penrose diagram is misleading as drawn.** The provocation's Penrose diagram places "our universe" in the top half and "pre-BCS phase" in the bottom half, with the CMB as the boundary. But a Penrose diagram represents CAUSAL structure -- future and past light cones, event horizons, null infinities. A phase boundary is not a causal surface. The correct diagram should show the BCS transition as a spacelike hypersurface (like a recombination surface), not as a horizon. This is an important conceptual distinction: horizons create thermal radiation (Paper 04, Paper 07, Paper 12); phase boundaries create latent heat and gravitational waves (L-9).

The Frolov-Vilkovisky / Smolin coordinate identity -- that the interior of a black hole maps to an expanding cosmology -- is exact as a coordinate statement for the Schwarzschild metric. But it does not carry thermodynamic content unless supplemented by quantum field theory on that background. The phonon-exflation framework has the quantum field theory (KC-1 Bogoliubov coefficients), but the mapping between the internal geometry and the 4D spacetime is still under construction.

**The "every point is the singularity" claim conflates the initial singularity with the phase transition.** The Hawking-Penrose singularity theorem (Paper 01) predicts geodesic incompleteness under the strong energy condition + generic condition + trapped surface condition. In the phonon-exflation framework, the initial state is tau = 0 (round metric), which is a REGULAR point of the internal geometry -- Kretschner scalar K(0) = 5/14, all curvature invariants finite (SP collab, Section 1.1). The "singularity" of the classical Big Bang is REPLACED by the phase transition, not identified with it. This is actually a STRONGER claim than the provocation states: the no-boundary proposal (Paper 09) combined with the round metric as initial condition provides a non-singular cosmological origin. The "singularity" was never there -- it was a phase transition all along.

### 1.4 Observational Content vs. Coordinate Identity

The critical question: does the isomorphism have observational content, or is it "just" a relabeling?

I identify **three testable consequences** that go beyond mere relabeling:

**T-1: Internal Gibbons-Hawking temperature predicts CMB temperature.** If the mapping tau -> cosmic time is established by the backreaction computation, the internal temperature T_GH^{internal}(tau_transition) redshifted to today should equal 2.725 K. This is a zero-parameter prediction (given M_KK and the backreaction solution). It would be the framework's most dramatic success or its most dramatic failure.

**T-2: Phase transition imprints a feature in P(k).** The BCS transition at tau = 0.35 produces a step or oscillation in the primordial power spectrum at k_transition = a(t_BCS) * H(t_BCS) (Cosmic-Web CP-3). LCDM's primordial spectrum is featureless modulo BAO. A feature at the predicted k is absent in LCDM and measurable by DESI/Euclid at sub-percent precision.

**T-3: Spectral index break at the transition.** Cosmic-Web's CP-6: the BCS transition converts the van Hove singularity (normal-state DOS divergence) into the BCS coherence peak (condensed-state DOS divergence). Perturbations generated before vs. after the transition sample different ground states, predicting a change in the effective spectral index n_s across the transition. This is a spectral BREAK, not just a bump -- a stronger signature than T-2 alone.

**T-4: Gravitational wave background from first-order transition.** The L-9 cubic invariant establishes first-order character. The GW spectrum peaks at f_peak ~ (beta/H) * (T_*/100 GeV) * 1.65e-5 Hz (Cosmic-Web Section 2.2). For a KK-scale transition, f_peak ~ 10^7-10^9 Hz (undetectable). For a later-epoch transition, potentially observable. The multi-sector cascade (5 cusps in d^3F/dtau^3) predicts a multi-peaked stochastic GW background -- distinctive and absent in LCDM.

All four require the backreaction computation. This is why backreaction is the universal priority.

### 1.5 The Volovik Connection

The provocation correctly identifies the Volovik cosmology as the interpretive framework: the universe is a condensed matter system, the Big Bang is a phase transition, and the cosmological horizon is the analog of the superfluid healing length. Session 28's Cosmic-Web collab (Section 2.1) provided the quantitative mapping: the Volovik identity rho_vac(equilibrium) = 0 reframes the cosmological constant problem (E-5) from a 113-order catastrophe to a structural feature of any condensate. The BCS exponential sensitivity Delta ~ exp(-1/(V*g)) provides the mechanism for small Lambda.

What is NEW in the provocation relative to Volovik is the specific identification of the CMB temperature with the internal Gibbons-Hawking temperature. Volovik identifies the CMB with the thermal history of the substrate cooling; the provocation identifies it with a GEOMETRIC temperature (surface gravity of the internal horizon). This is a stronger and more specific claim. It is testable.

---

## II. Session 29A Architecture

Session 29A is organized around the physical picture from the provocation, tested by the computations identified in the two Session 28 syntheses. The guiding question: **is the BCS phase transition at tau = 0.35 a self-consistent cosmological event that produces the observable universe?**

### 2.1 Session Structure

- **29a**: KC-3 Closure + Entropy Balance (4-5 computations, ~30 min)
- **29b**: Backreaction + Free Energy Comparison (3-4 computations, ~1 hr)
- **29c**: Observational Predictions + Synthesis (3-4 computations + theory, ~2 hr)

### 2.2 Pre-Session Gate

Before any Session 29A computation proceeds, verify that existing Session 28 data files are intact and accessible:

| File | Contents | Required By |
|:-----|:---------|:------------|
| `s28a_bogoliubov_coefficients.npz` | B_k(tau) for all sectors | 29a-KC3, 29a-H13, 29c-T1 |
| `s28a_spectral_action_comparison.npz` | I_E(tau) for D_K and D_can | 29b-E1, 29c-T1 |
| `s28b_self_consistent_tau_T.npz` | F_total(tau, mu) landscape | 29b-CP1, 29c-T4 |
| `s28b_hessian.npz` | Hessian eigenvalues at minima | 29b-CP1 |
| `s28c_phonon_tmatrix.npz` | T-matrix at tau = 0.15, 0.35 | 29a-KC3 |
| `s28c_bcs_van_hove.npz` | Van Hove BCS gap Delta(tau) | 29a-KC3, 29b-CP1 |
| `s28c_luttinger.npz` | Luttinger K(tau) per sector | 29a-KC3 |
| `s28c_steady_state_mu.npz` | n_gap(tau, d(tau)/dt) | 29a-KC3, 29b-E1 |
| `s23a_eigenvectors_extended.npz` | D_K eigenvectors for all sectors | 29a-KC3 |

---

## III. Computation Plan

### 29a: KC-3 Closure + Entropy Balance

#### Computation 29a-1: T-Matrix Extension to tau = 0.40, 0.45, 0.50 [CRITICAL]

**What**: Extend the KC-2 phonon-phonon T-matrix from the currently validated range (tau <= 0.35) to the KC-3-required range (tau >= 0.50). Solve the non-perturbative Lippmann-Schwinger equation:

$$T = V_{J\text{-even}} (1 - G_0 V_{J\text{-even}})^{-1} \tag{2}$$

where V_{J-even} is the J-projected pairing interaction and G_0 is the free propagator (Synthesis A, U-2, X-1).

**Gate condition**: W/Gamma_inject > 0.1 at tau = 0.50. If scattering rate drops below this threshold, the bottleneck is broken and KC-3 FAILS.

**Constraint Condition**: If max|T| drops by > 10x between tau = 0.35 and tau = 0.50, the mechanism is quantitatively closed regardless of the W/Gamma_inject ratio.

**Inputs**: `s28c_phonon_tmatrix.py` (adapt tau scan range), `s23a_eigenvectors_extended.npz` (mode functions).

**Computational cost**: ~200x200 matrix inversion per tau value (after J-projection halves dimension from ~400). Trivial on Ryzen 32-core. Estimated runtime: < 5 min.

**Agent**: phonon-exflation-sim (heavy computation). Implements X-1 (J-even prior constraint from Synthesis A).

#### Computation 29a-2: Self-Consistent KC-3 with Derived Drive Rate [CRITICAL]

**What**: Replace the scanned drive rate d(tau)/dt ~ 1-8 with a derived value from the modulus equation of motion. The drive rate at each tau is determined by the effective potential:

$$\frac{d\tau}{dt} = \sqrt{\frac{2}{G_{\tau\tau}} [E_{total} - V_{eff}(\tau)]} \tag{3}$$

where G_{tau,tau} = 5 (Baptista Paper 15), V_eff is the spectral action plus BCS condensation energy, and E_total is the one free parameter (Synthesis A, C-3).

Using the DNP instability result (SP-5: the round metric is repulsive), the modulus starts at tau ~ 0 with d(tau)/dt ~ 0 and accelerates. The maximum drive rate is determined by E_total.

**Gate condition**: d(tau)/dt at tau = 0.50, for a range of E_total values compatible with the DNP instability, must reach the KC-3 threshold (d(tau)/dt >= 1 for n_gap > 20 with existing B_k values).

**Constraint Condition**: If E_total must exceed a physically unreasonable value (E_total > V_eff(tau=0) * 100) to achieve sufficient drive, the mechanism requires fine-tuning and is effectively closed.

**Inputs**: `s28a_spectral_action_comparison.npz` (V_eff), `s28b_self_consistent_tau_T.npz` (BCS condensation energy), `s28c_steady_state_mu.npz` (n_gap interpolation).

**Computational cost**: ODE integration + interpolation. Trivial. < 1 min.

**Agent**: phonon-exflation-sim.

#### Computation 29a-3: Entropy Balance (H-13 / CP-4) [HIGH]

**What**: Compute the GSL-analog balance sheet explicitly:

$$\frac{dS_{particles}}{d\tau} \geq \left|\frac{dS_{spec}}{d\tau}\right| \tag{4}$$

The particle entropy production rate uses KC-1 data (Gamma_inject = 29,643 at tau = 0.40, B_k(gap) = 0.023):

$$\frac{dS_{particles}}{d\tau} \sim \Gamma_{inject} \cdot \ln(1/B_k) \sim 112{,}000 \tag{5}$$

The spectral entropy decrease rate |dS_spec/d(tau)| uses Session 25 data (H-2 computation).

**Gate condition**: dS_particles/d(tau) > |dS_spec/d(tau)| at all tau in [0, 0.50]. If satisfied, the tau evolution is thermodynamically permitted by the ordinary second law (Einstein's correction from Synthesis B: no horizon on SU(3), so the GSL does not apply; use ordinary second law instead).

**Constraint Condition**: If the entropy balance is violated at any tau in [0, 0.50], the tau evolution is thermodynamically forbidden regardless of the Constraint Chain results. This is a HARD closure -- the second law of thermodynamics is non-negotiable.

**Inputs**: `s28a_bogoliubov_coefficients.npz`, Session 25 spectral entropy data.

**Computational cost**: Trivial (existing data, one derivative calculation). < 1 min.

**Agent**: hawking-theorist or phonon-exflation-sim.

#### Computation 29a-4: Inter-Sector Coupling J_perp (Mermin-Wagner) [MEDIUM]

**What**: Quantify the inter-sector coupling J_perp that determines whether the effective dimensionality exceeds 1 (Synthesis B, C-4). If J_perp > Delta_BCS, mean-field BCS holds and the gap is a true gap. If J_perp < Delta_BCS, the system is effectively 1D and the gap is a pseudogap (Luttinger liquid).

Compute J_perp from the off-diagonal blocks of D_K in the Peter-Weyl basis. The block-diagonality theorem (Session 22b) says these are EXACTLY zero for D_K itself. But the 4-point interaction V_{abcd} is NOT block-diagonal in general -- it couples different sectors through the 4-mode overlap integrals. The relevant J_perp is the inter-sector matrix element of the BCS pairing interaction.

**Gate condition**: J_perp / Delta_BCS > 1 at tau = 0.35. If so, the condensate is truly long-range-ordered and mean-field is justified.

**Note**: This is Einstein's concern from Synthesis B. If J_perp / Delta_BCS < 1, the system is a Luttinger liquid, not a BCS superconductor. The phenomenology is completely different: quasi-long-range order instead of true long-range order, power-law correlations instead of exponential, and the gap is a PSEUDOGAP that does not protect the condensate from fluctuations.

**Inputs**: `s23a_eigenvectors_extended.npz` (mode functions from multiple sectors), `s28c_phonon_tmatrix.py` (adapt to compute inter-sector matrix elements).

**Computational cost**: Moderate. Requires computing 4-point overlap integrals between modes in different Peter-Weyl sectors. Estimated: 10-30 min on 32-core.

**Agent**: phonon-exflation-sim.

### 29b: Backreaction + Free Energy Comparison

#### Computation 29b-1: Free Energy Comparison at First-Order Transition (CP-1) [CRITICAL]

**What**: The first-order BCS transition (L-9 PASS) simplifies the backreaction to a free energy comparison (Synthesis B, CP-1). Compare:

$$F_{condensed}(\tau = 0.35, \mu = \mu_{eff}) \quad \text{vs.} \quad F_{normal}(\tau, \mu = 0) \tag{6}$$

The transition occurs when F_condensed < F_normal. The critical tau at which this crossing occurs, combined with the drive rate from 29a-2, gives the cosmic time t_BCS of the transition.

The key question: does the first-order transition occur BEFORE the modulus reaches tau = 0.35 from the DNP-unstable initial state at tau = 0? If the modulus is driven past tau = 0.35 without the transition occurring (because KC-3 has not filled the gap yet), the BCS mechanism fails.

**Gate condition**: The free energy crossing F_condensed = F_normal occurs at tau_cross in [0.20, 0.50], consistent with the KC-3 occupation threshold.

**Constraint Condition**: If F_condensed > F_normal at all tau in [0, 2.0], the BCS condensation is never energetically favored and the mechanism is closed by thermodynamics.

**Inputs**: `s28b_self_consistent_tau_T.npz` (F_total landscape), `s28a_spectral_action_comparison.npz` (F_normal = spectral action).

**Computational cost**: Interpolation of existing data. Trivial. < 1 min.

**Agent**: phonon-exflation-sim or einstein-theorist.

#### Computation 29b-2: Modulus Equation of Motion (Synthesis A U-5, Synthesis B Priority 3) [CRITICAL]

**What**: Solve the coupled modulus equation of motion:

$$\ddot{\tau} + 3H\dot{\tau} + \frac{1}{G_{\tau\tau}} \frac{dV_{eff}}{d\tau} = 0 \tag{7}$$

with the Friedmann constraint:

$$H^2 = \frac{1}{3M_P^2}\left[\frac{1}{2}G_{\tau\tau}\dot{\tau}^2 + V_{eff}(\tau)\right] \tag{8}$$

This is the FULL backreaction computation. V_eff(tau) includes the bare spectral action (monotonically decreasing, from C-1/L-1) and the BCS condensation energy (from S-3 interior minima). G_{tau,tau} = 5 (Baptista Paper 15).

The system is a two-variable ODE (tau(t), H(t)) with one free parameter M_KK (the compactification scale). The initial conditions are set by the no-boundary proposal + WCH (Synthesis A, U-4): tau(0) = 0, d(tau)/dt(0) = epsilon (small perturbation from DNP instability).

**Outputs**:
1. tau(t) trajectory -- the cosmic time evolution of the modulus
2. t_BCS -- the cosmic time of the BCS transition (from 29b-1 free energy crossing)
3. H(t_BCS) -- the Hubble rate at the transition
4. d(tau)/dt at all t -- confirms whether the KC-3 drive rate requirement is met dynamically

**Gate condition**: The trajectory tau(t) must reach tau = 0.35 in a cosmologically reasonable time (t_BCS < t_universe ~ 13.8 Gyr, and ideally t_BCS ~ 10^{-36} - 10^{-10} s for a GUT/EW-scale transition).

**Inputs**: `s28a_spectral_action_comparison.npz`, `s28b_self_consistent_tau_T.npz`, M_KK as parameter.

**Computational cost**: ODE integration, trivial numerically. The physics is in the setup and interpretation. < 5 min.

**Agent**: phonon-exflation-sim for numerics, einstein-theorist for the Friedmann equation setup.

#### Computation 29b-3: Gaussian Fluctuation Correction (Synthesis A Priority 4, T-2) [MEDIUM]

**What**: Compute the one-loop determinant det(M[Delta]) around the BCS saddle point. The Ginzburg criterion for N ~ 16 modes in the singlet sector gives delta T_c / T_c ~ O(1) (Synthesis A, T-2). The BCS coherence length xi ~ v_F/Delta ~ 1.25, compared to the injectivity radius r_inj ~ 2.44, gives xi/r_inj ~ 0.51 (Synthesis A, X-2) -- Cooper pairs span half the internal manifold, making finite-size corrections order unity.

The computation: diagonalize the 2N x 2N BdG Hamiltonian at the saddle point, compute det(M) = product of eigenvalues, and evaluate the Gaussian correction to the free energy:

$$F_{1-loop} = F_{MF} + \frac{1}{2}\sum_n \ln(\omega_n^2 + E_n^2) \tag{9}$$

where E_n are the BdG quasiparticle energies and omega_n are Matsubara frequencies.

**Gate condition**: The one-loop correction does not change the sign of F_condensed - F_normal. If it does, the mean-field BCS minimum is an artifact of the saddle-point approximation.

**Inputs**: `s28c_bcs_van_hove.npz`, `s28b_hessian.npz`.

**Computational cost**: BdG diagonalization (~32x32 matrix), Matsubara sum. Low. < 5 min.

**Agent**: landau-condensed-matter-theorist (BCS fluctuation expertise).

### 29c: Observational Predictions + Synthesis

#### Computation 29c-1: Internal Gibbons-Hawking Temperature at Transition (H-10) [HIGH]

**What**: Compare the internal Gibbons-Hawking temperature T_GH^{internal}(tau) with the effective temperature T_eff extracted from the Bogoliubov spectrum |beta_k|^2 at each tau. This discriminates between equilibrium (T_eff ~ T_GH, thermalized) and non-equilibrium (T_eff >> T_GH, driven) regimes.

From Session 25: T_GH^{internal}(tau) = e^{-2tau}/pi.

From KC-1: The Bogoliubov spectrum |beta_k|^2 at each tau. Fit to a Planck distribution to extract T_eff.

**Observational content**: If T_eff ~ T_GH at tau = 0.35, the system is in quasi-thermal equilibrium at the transition, and the CMB temperature is directly related to T_GH^{internal}(0.35) via redshift. If T_eff >> T_GH, the particle spectrum is non-thermal and the CMB temperature requires a more complex mapping.

**Inputs**: `s28a_bogoliubov_coefficients.npz` (|beta_k|^2 per mode per tau).

**Computational cost**: Fit to Planck distribution. Trivial. < 1 min.

**Agent**: hawking-theorist (Gibbons-Hawking expertise).

#### Computation 29c-2: k_transition from Backreaction (CP-3 Chain) [HIGH]

**What**: Convert the BCS transition time t_BCS from 29b-2 to a comoving wavenumber:

$$k_{transition} = a(t_{BCS}) \cdot H(t_{BCS}) \tag{10}$$

This is the scale that exits the horizon at the moment of the BCS transition. It defines the location of the predicted P(k) feature.

**Observational content**: If k_transition falls in the DESI/Euclid sensitivity range (k ~ 0.01-0.3 h/Mpc), the feature is directly testable. If k_transition is at much larger or smaller k, the prediction escapes current observational reach.

**Inputs**: Outputs of 29b-2 (tau(t), H(t)).

**Computational cost**: Single evaluation. Trivial.

**Depends on**: 29b-2 completion.

**Agent**: cosmic-web-theorist (large-scale structure expertise).

#### Computation 29c-3: CDL Bounce Action (Synthesis A T-1, Priority 5) [MEDIUM]

**What**: Compute the Coleman-De Luccia bounce action B for tunneling from the BCS well at tau = 0.35 through the potential barrier toward decompactification. The requirement B >> 400 ensures the metastable vacuum lifetime exceeds the age of the universe (10^{10} years).

$$B = S_{E}[\phi_{bounce}] - S_{E}[\phi_{false}] \tag{11}$$

where phi_bounce is the O(4)-symmetric bounce solution and phi_false is the false vacuum (BCS well).

**Gate condition**: B > 400. If satisfied, the BCS well is cosmologically stable and the Kasner singularity at tau -> infinity is dynamically censored (SP collab Section 1.3). If B < 400, the universe is unstable to tunneling into decompactification.

**Inputs**: V_eff(tau) from `s28a_spectral_action_comparison.npz` + `s28b_self_consistent_tau_T.npz`.

**Computational cost**: 1D bounce ODE (shooting method). Low. < 5 min.

**Agent**: phonon-exflation-sim.

#### Computation 29c-4: GW Spectrum Parameters (alpha, beta/H) [LOW-MEDIUM]

**What**: Estimate the gravitational wave spectrum parameters from the first-order BCS transition (L-9):

- alpha (latent heat / radiation energy density): from the free energy discontinuity at the transition
- beta/H (nucleation rate / Hubble rate): from the curvature of the free energy barrier
- f_peak: peak frequency of the stochastic GW background

**Observational content**: If alpha > 0.1 and f_peak falls in an observable band (LISA: 10^{-4}-10^{-1} Hz, LIGO: 10-10^3 Hz), the framework predicts a detectable GW signal. The multi-sector cascade (5 cusps, L-9) predicts a multi-peaked spectrum.

**Inputs**: `s28b_self_consistent_tau_T.npz` (free energy landscape), L-9 cubic invariant data, outputs of 29b-2 (H(t_BCS) and T_*).

**Computational cost**: Analytical estimates from existing data. < 10 min.

**Agent**: cosmic-web-theorist or hawking-theorist.

---

## IV. Constraint Conditions and Gate Structure

### 4.1 Hard Closes (any one terminates Session 29A)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| K-29a | W/Gamma_inject < 0.1 at tau >= 0.50 (29a-1) | KC-3 FAIL. Constraint Chain closed. Framework drops to 3%. |
| K-29b | Entropy balance violated: dS_particles < |dS_spec| at any tau in [0, 0.50] (29a-3) | Tau evolution thermodynamically forbidden. All mechanisms closed. |
| K-29c | F_condensed > F_normal at ALL tau (29b-1) | BCS condensation never energetically favored. mechanism closed by thermodynamics. |
| K-29d | One-loop correction reverses sign of F_condensed - F_normal (29b-3) | Mean-field BCS is artifact. Gap is pseudogap. |

### 4.2 Soft Gates (constrain but do not closure)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| G-29a | d(tau)/dt < 1 at tau = 0.50 for E_total in natural range (29a-2) | Drive rate requires fine-tuning. Mechanism weakened but not closed. |
| G-29b | J_perp / Delta_BCS < 1 (29a-4) | Mermin-Wagner applies. Gap is pseudogap. Quantitative predictions unreliable but qualitative picture may survive. |
| G-29c | B < 400 (29c-3) | BCS well is metastable with finite lifetime. Universe tunnels to decompactification. Clock constraint may be evaded by tunneling timescale. |

### 4.3 Positive Signals (increase probability)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-29a | W/Gamma_inject > 0.5 at tau = 0.50 (29a-1) | KC-3 PASSES with comfortable margin. Constraint Chain complete. |
| P-29b | Self-consistent d(tau)/dt reaches KC-3 threshold (29a-2) | Drive rate is dynamically natural. No fine-tuning. |
| P-29c | k_transition in DESI/Euclid range (29c-2) | Quantitative testable prediction. Framework graduates from "program" to "theory" (Feynman criterion). |
| P-29d | T_eff ~ T_GH at tau = 0.35 (29c-1) | Quasi-thermal equilibrium. CMB temperature directly connected to internal geometry. Provocation's Claim A validated. |

---

## V. Agent Assignments

| Agent | Role | Computations |
|:------|:-----|:-------------|
| **phonon-exflation-sim** | Primary computation | 29a-1, 29a-2, 29a-4, 29b-1, 29b-2, 29c-3 |
| **hawking-theorist** | Thermodynamic evaluation | 29a-3, 29c-1, synthesis of Claim A/B/C verdicts |
| **einstein-theorist** | Friedmann equation + EOM | 29b-2 (setup), 29c-2 (k_transition mapping) |
| **landau-condensed-matter-theorist** | BCS fluctuations | 29b-3 (Gaussian correction), 29a-4 (Mermin-Wagner assessment) |
| **cosmic-web-theorist** | Observational predictions | 29c-2, 29c-4 (GW spectrum), P(k) feature assessment |
| **coordinator** | Context + routing | Full session |
| **schwarzschild-penrose-geometer** | Penrose diagram + censorship | 29c-3 (CDL assessment), final causal structure diagram |

**Recommended team size**: 4-5 active agents + coordinator. Minimum viable: phonon-sim + hawking + coordinator.

---

## VI. Dependency Graph

```
29a-1 (T-matrix extension)  -----> KC-3 Verdict
29a-2 (drive rate)           -----> KC-3 Verdict + 29b-2
29a-3 (entropy balance)      -----> HARD CLOSED or thermodynamic PASS
29a-4 (J_perp)              -----> Mermin-Wagner verdict

KC-3 Verdict + 29a-2 -----> 29b-1 (free energy comparison)
                       -----> 29b-2 (modulus EOM)

29b-1 + 29b-2 -----> t_BCS, H(t_BCS)
               -----> 29c-1 (T_GH vs T_eff)
               -----> 29c-2 (k_transition)
               -----> 29c-3 (CDL bounce)
               -----> 29c-4 (GW parameters)

29b-3 (Gaussian correction) -----> independent, can run in parallel with 29b-1/29b-2
```

**Critical path**: 29a-1 -> KC-3 Verdict -> 29b-1 -> 29b-2 -> 29c-2.
If 29a-1 CLOSES (KC-3 fails), then 29b and 29c are unnecessary. Session 29A terminates early.

---

## VII. Probability Assessment and Exit Conditions

### 7.1 Current State

Pre-Session 29A probability: **7-8% panel / 4-5% Sagan** (Synthesis B consensus).

### 7.2 Conditional Trajectories

| Scenario | KC-3 | Entropy | Free Energy | One-Loop | Posterior (panel) |
|:---------|:------|:--------|:------------|:---------|:-----------------|
| **Full PASS** | PASS | PASS | crossing exists | survives | **15-22%** |
| **KC-3 only** | PASS | PASS | no crossing | -- | 10-14% |
| **KC-3 + entropy closure** | PASS | FAIL | -- | -- | 2-3% (thermodynamic veto) |
| **KC-3 fail** | FAIL | -- | -- | -- | 3% (structural floor) |
| **KC-3 + k_transition in range** | PASS | PASS | crossing exists | survives | **20-30%** (first testable prediction) |

The dramatic upward pathway requires: KC-3 PASS + entropy PASS + free energy crossing + k_transition in DESI range. This would be the framework's first quantitative, falsifiable prediction. It would graduate the framework from "mathematical program with structural matches" to "physical theory with testable predictions" (Feynman's T-3 criterion from Synthesis A).

### 7.3 Session 29A Success Criteria

Session 29A is successful if it produces:

1. **A definitive KC-3 verdict** (PASS or FAIL)
2. **A definitive entropy balance verdict** (permitted or forbidden)
3. **A self-consistent backreaction trajectory** tau(t) with derived drive rate
4. **An estimate of k_transition** (in h/Mpc, with uncertainty from M_KK dependence)
5. **A revised Penrose diagram** of the modulus mini-superspace incorporating all dynamical results

---

## VIII. The Physical Picture After Session 29A

If Session 29A completes successfully (KC-3 PASS, entropy PASS, backreaction self-consistent), the physical picture is:

```
    future infinity (Lambda -> 0, equilibrium substrate)
   /                                                      \
  /         our universe (BCS condensed, tau = 0.35)       \
 /         - frozen modulus, w = -1 exactly                 \
/          - discrete KK excitation spectrum                 \
|          - SM gauge fields from non-Killing vectors        |
|                                                            |
|============================================================|  t_BCS
|              BCS PHASE TRANSITION (first-order)            |
|          - tau jumps from evolving to frozen                |
|          - latent heat -> primordial perturbation feature   |
|          - GW background from bubble nucleation             |
|============================================================|
|                                                            |
|     pre-BCS phase (tau evolving, KC-1 particle creation)   |
|     - modulus rolls from tau=0 toward tau=0.35             |
|     - Parker excitations fill spectral gap (KC-3)          |
|     - driven non-equilibrium: T_eff ~ T_GH^{internal}     |
|                                                            |
 \          DNP-unstable zone (tau in [0, 0.285])           /
  \        - round metric repels, white-hole analog        /
   \       - Weyl curvature lowest (WCH)                  /
    *-----------------------------------------------------*
              tau = 0, round metric (triple-selected)
              [no-boundary saddle, J-maximal, WCH minimum]
```

This is NOT a Penrose diagram (which represents causal structure). It is a thermodynamic phase diagram of the modulus mini-superspace. The vertical axis is cosmic time (or equivalently tau). The horizontal lines at t_BCS represent the phase transition. The "singularity" of classical cosmology is REPLACED by the regular round metric at tau = 0, which is selected by the no-boundary proposal (Paper 09), the Weyl curvature hypothesis (SP collab Section 1.3), and J-maximality (Synthesis A, U-4).

The CMB surface of last scattering is the REDSHIFTED image of the BCS phase transition surface. Every spatial point in our universe sits on the condensed side. The "Big Bang" was not singular -- it was a first-order phase transition in the internal geometry of spacetime.

---

## IX. Relation to Papers in researchers/Hawking/

| Paper | Relevance to Session 29A | Specific Application |
|:------|:------------------------|:--------------------|
| 01 (Hawking-Penrose 1970) | Singularity theorem replaced by phase transition | tau=0 is regular; singularity replaced by BCS |
| 03 (BCH Four Laws) | First law extended: dE = TdS + phi_tau d(tau) + mu dN | Modulus work term in backreaction |
| 04 (Black Hole Explosions) | Negative specific heat analog: I_E mono-dec = BH evaporation | Structural isomorphism (Claim C) |
| 05 (Particle Creation) | KC-1 Bogoliubov formalism, trans-Planckian universality | Gap-edge particle creation, H-5 confirmed |
| 07 (Gibbons-Hawking) | T_GH = H/(2pi) for cosmological horizon | Internal T_GH for CMB prediction (29c-1) |
| 09 (No-Boundary) | NBP selects tau=0 as initial condition | Euclidean cap on round metric |
| 10 (Information Loss) | Hawking-Page transition = BCS phase transition analog | First-order character (L-9) |
| 11 (Bekenstein Entropy) | GSL -> entropy balance constraint (29a-3) | Second law permits/forbids tau evolution |
| 12 (Unruh Effect) | Phonon excitations = Unruh particles on evolving geometry | KC-4 attractive Luttinger regime |
| 13 (Page Curve) | Information recovery in BCS: condensate encodes pre-transition info | Long-term information question |
| 14 (Island Formula) | Internal islands in KK context (closed by W5 for bare spectrum, open for BCS) | Future direction |

---

## X. Open Questions Beyond Session 29A

1. **Sector sum renormalization** (L-8, Synthesis B Priority 6): The 482% non-convergence at p+q=4 undermines ALL quantitative predictions. Requires a physical prescription for the Peter-Weyl sum. Multi-session problem.

2. **Information content of the BCS condensate** (H-11): How many independent condensate configurations exist? Does the microstate count relate to any entropy bound? Important for the internal-space analog of the Page curve.

3. **Full SU(3) Clebsch-Gordan coefficients** (Synthesis A Priority 2): Replace the diagonal approximation in the T-matrix with exact overlap integrals using tabulated CG coefficients. Eliminates the factor-of-2 uncertainty in the pairing interaction.

4. **Fundamental vs. emergent gravity fork** (Synthesis B T-1): Does gravity couple to absolute vacuum energy (Einstein) or only to departures from equilibrium (Volovik)? The E-5 cosmological constant problem's severity depends on this answer. Framework must eventually decide.

5. **Spectral index break measurement** (CP-6): If k_transition is computed, the predicted spectral break can be compared with DESI/Euclid P(k) data. This requires P2b-level theoretical development to predict the amplitude and shape of the break.

---

*Plan authored by Hawking (hawking-theorist), 2026-02-28. Grounded in the full 14-paper corpus (researchers/Hawking/), Session 28 computations and gate verdicts (28a+28b+28c), both team syntheses (Dirac+Feynman+SP, Einstein+Hawking+Cosmic-Web), and the CMB-as-horizon provocation. All equations cited to specific papers. Constraint Conditions pre-registered. Agents assigned. Computational costs estimated. The framework's fate is a finite computation away.*
