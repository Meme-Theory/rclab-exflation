# Framework Chapter: Parametric Amplification — The Alternative Expansion Mechanism

**Date**: 2026-04-11
**Status**: Draft for integration into `phonon_exflation_cosmology.md` as new §6e

---

## Abstract

Cosmogenesis in the phonon-exflation framework is a single-pulse parametric amplification event on an internal modulus, not a metric expansion of a container. The spectral complexity of the fabric grows inside each point as the eigenvalue spectrum of the Dirac operator D_K reorganizes under Jensen deformation; the fabric does not expand into a pre-existing space. At tau ~ 0.19 the modulus crosses the van Hove singularity of the B2 flat band at Mach 20.73 (S73A W1-A), striking the 8-mode BCS sub-spectrum like a hammer striking a resonant cavity. The fold is asymmetric: the entry side carries a thermal Hawking-like horizon with n_bar = 85.2 per mode (kappa_entry = 79,386 M_KK); the exit side is an open boundary with no sonic horizon anywhere. The output of the single firing is an SU(1,1)-squeezed vacuum of 8 modes, phase-locked at 1e-9 rad intra-branch, protected from thermalization by Richardson-Gaudin integrability. This squeezed vacuum is the observable universe's initial state. The ringing that follows — not a driven expansion but the slow relaxation of the 8 output modes through weak coupling to the emergent gravitational sector — is what we measure as the Hubble rate. The "inflation" era corresponds to the parametric amplification window at the fold; the "reheating" era corresponds to the thermal occupation produced by the entry horizon; the "structure formation" era corresponds to the interference pattern of the amplified output modes. The observed acoustic peaks in the CMB power spectrum are the natural modes of the emergent 4-manifold, and n_s = 0.9567 from S72/S73A W2-A is the slope set by the spectral action geometry of the fiber, not by the amplifier transfer function. There is no need for an inflationary dynamical metric, no bounce with a reversed time direction, and no conformal matching to a prior aeon. The fold is a one-time impulsive event in the tau-history of D_K, and cosmological history on this side of the fold is the ringing spectrum of the post-pulse relic.

---

## 1. Substrate Statement — What Is Cosmogenesis, Physically?

The fabric is not a field living inside a pre-existing spacetime. It is the set of eigenvalue data of the Dirac operator D_K on Jensen-deformed SU(3), carried at every point by the spectral triple (C^infinity(SU(3)), L^2(K, S_K), D_K(tau)). The Jensen deformation parameter tau selects one internal geometry out of a one-parameter family (g|_{u(1)} = e^{2tau}, g|_{su(2)} = e^{-2tau}, g|_{C^2} = e^{tau}); the spectrum of D_K(tau) determines, through the spectral action S(tau) = Tr f(D_K^2 / Lambda^2), every emergent coupling, mass, and metric coefficient visible in 4D [phonon_exflation_cosmology.md §2.2.1, §8.7]. The a_0 Seeley-DeWitt coefficient generates the vacuum cosmological term; a_2 generates the Einstein-Hilbert Lagrangian density R sqrt(-g) with its coefficient fixed to 1/(16 pi G_N) by the Gilkey a_2 identity a_2 / a_0 = (5/12) R [phonon_exflation_cosmology.md §12.1, §8.7.8]; a_4 generates the Yang-Mills action. Newton's constant is not a free parameter — it is the second spectral moment of D_K. There is no step in which "space" is supplied by hand. The 4D metric g_{mu nu}, G_N, and the gauge kinetic terms are all derived quantities — zeroth, second, and fourth spectral moments of D_K, respectively. Reality is the spectrum; geometry is a moment of the spectrum; things are excitations of the spectrum.

Cosmogenesis, in this picture, is a single event in the tau-history of D_K. At tau = 0 the internal manifold carries the round SU(3) metric and the spectral action sits high on its classical landscape. As tau advances under the gradient of the spectral action, dS/dtau = +58,673 in Lambda-normalized units [phonon_exflation_cosmology.md §8.7.9], the system is driven through the van Hove singularity of the B2 flat band at tau ~ 0.19 — the fold. The fold is not a singularity in spacetime; there is no spacetime yet at which to locate a singularity. It is a specific configuration of the D_K eigenvalue spectrum at which eight flat-band modes cross a BCS pairing threshold and the integrable many-body structure (Richardson-Gaudin, 8 conserved integrals, block-diagonal theorem) locks in. The pre-fold and post-fold sides are not two universes joined at a boundary. They are two configurations of the same spectral triple, related by a one-parameter deformation of D_K. The transit from one to the other is a one-time impulsive event in the modulus dynamics, and the post-fold substrate — the Generalized Gibbs Ensemble relic — is what we observe and call "the universe." Everything in this chapter follows from reading this impulsive event acoustically, not metrically.

---

## 2. Why "Inflation" Does Not Describe This

Inflation is a story about a metric. A scalar field phi rolls down a potential V(phi), the Friedmann equation converts its energy density into a Hubble rate H(t), and the spatial metric a(t) grows exponentially while phi remains nearly constant. Three ingredients are load-bearing: a metric on which a(t) lives, a classical rolling field with a slow-roll approximation, and a consistency relation r = 16 epsilon that ties scalar and tensor perturbations through the same slow-roll parameter. The single-pulse parametric amplifier mechanism fails to supply any of the three. The failure is not quantitative; it is structural, at the level of what objects the two descriptions even contain.

### 2a. Inflation Presupposes a Pre-Existing Container

Inflationary cosmology begins with an FRW line element ds^2 = -dt^2 + a(t)^2 d(vec x)^2. The scale factor a(t) acts on a spatial slice that is already there, already metric, already three-dimensional. The inflaton's job is to drive a(t) through many e-folds while phi's energy density dominates. This presupposes a container — a 4-manifold with a Lorentzian signature, coordinates, and a differential structure — onto which the dynamics is imposed. In the substrate picture there is no such container. The 4D metric is an emergent output of the spectral action: the second Seeley-DeWitt coefficient a_2, multiplied by the f_2 moment of the cutoff function, generates the Einstein-Hilbert Lagrangian density R sqrt(-g) with its coefficient fixed to 1/(16 pi G_N) by the Gilkey a_2 identity a_2 / a_0 = (5/12) R [phonon_exflation_cosmology.md §12.1, §8.7.8]. Newton's constant G_N is therefore not a free parameter; it is the second spectral moment of D_K. Before the fold, the "pre-existing space" that inflation would inflate does not exist as an independent object; it exists only as spectral content distributed over the internal fiber. There is nothing for a(t) to scale. The fabric is the structure at every point; it is not inside a thing that can expand. Inflation's kinematic scaffolding is therefore absent at the outset, not merely approximated away.

### 2b. Inflation Requires Quasi-Adiabatic Slow-Roll — Every BCS Mode Fails the Criterion

Slow-roll inflation is a statement about a quasi-adiabatic field evolution: the WKB parameter gamma = |d ln omega_k / dt| / omega_k must be small for every perturbation mode k, so that each mode's instantaneous frequency changes much more slowly than the mode itself oscillates. Under gamma << 1 one may use the Bunch-Davies vacuum as an adiabatic reference, match modes across the horizon crossing time, and derive the standard slow-roll results. The regime of validity is precisely gamma << 1.

S73A W1-A [session-73a-results-workingpaper.md W1-A] computes gamma for each of the 8 BCS mode frequencies as the modulus crosses the van Hove singularity. The result:

| Mode | gamma |
|:-----|:------|
| B2[0] | 1.68 |
| B2[1] | 6.65 |
| B2[2] | 13.24 |
| B2[3] | 17.81 |
| B1 | 23.58 |
| B3[0] | 32.96 |
| B3[1] | 36.59 |
| B3[2] | 35.12 |

The minimum gamma anywhere in the spectrum is 1.68, and the maximum is 36.59. Every single mode fails the adiabatic criterion gamma << 1 by at least an order of magnitude; most fail it by one or two. The slow-roll approximation is not marginal here. It is completely inapplicable. There is no mode for which WKB matching is valid across the fold. The mode functions cannot be continuously deformed from an in-vacuum to an out-vacuum through a sequence of instantaneous adiabatic vacua, because no such sequence exists within the transit duration.

The factor ~10 spread in gamma across the B2 quartet (from 1.68 at B2[0] to 17.81 at B2[3]) is the direct kinematic origin of the three-orders-of-magnitude spread in Bogoliubov occupations n_k documented in §6a: the Parker beta-integral of §4b depends on omega_k through the dimensionless combination gamma_k, so a mode with gamma_k = 1.68 is weakly non-adiabatic while gamma_k = 36.59 is strongly non-adiabatic, and the Bogoliubov coefficient |beta_k|^2 ~ exp(-pi / gamma_k) scaling (Landau-Zener limit for near-adiabatic modes) gives the observed spread. The gamma table of this subsection and the n_k hierarchy of §6a are two sides of the same impulsive-drive calculation.

Any derivation that assumes slow-roll — including the derivation of a(t) in terms of V(phi), the spectrum tilt from epsilon_V, the tensor amplitude from H^2 — is importing a kinematic regime that the substrate transit does not support. The framework's n_s = 0.9567 [phonon_exflation_cosmology.md §8.7.9, S73A W2-A] does not come from slow-roll and cannot be reverse-engineered into a slow-roll potential. It comes from the curvature of the spectral action S(tau), a geometric property of the spectral triple, not a dynamical property of a classical field [S73A W4-D BLV-COMPOUND-73a PASS: "n_s is permanently fixed by the spectral action geometry"].

### 2c. Inflation Predicts r = 16 epsilon; The Consistency Relation Is Ill-Typed Here

The tensor-to-scalar consistency relation r = 16 epsilon (or equivalently r = -8 n_T) is a direct output of slow-roll inflation. It states that the ratio of tensor to scalar power spectra at horizon crossing is 16 times the first slow-roll parameter, because both scalar and tensor perturbations see the same background H(t) and the same slow-roll approximation applies to both. The relation is not a law of quantum field theory; it is a consequence of the specific inflationary model in which a single scalar inflaton dominates the stress-energy and both perturbation sectors share its slow-roll hierarchy.

The substrate transit does not have an inflaton, does not have a slow-roll regime (§2b), and does not have a single scalar field dominating a Friedmann evolution. The scalar and tensor sectors in the phononic crystal have independent dispersion structures: the Mukhanov-Sasaki scalar equation and the tensor-mode equation see DIFFERENT effective sound speeds (c_BLV for scalar, c = 1 for tensors) and DIFFERENT Poschl-Teller conformal factors (z''/z vs a''/a) [S67 ACOUSTIC-TENSOR-TRANSFER-67: a''/a = 6.90e5 (0.75x z''/z), k_tach^T = 831 (0.42x k_tach^S), tensor Mach = 26.5 vs scalar 54.7]. Because the two sectors travel at different speeds through different potentials and neither lives in a slow-roll limit, there is no structural reason for their amplitudes to be tied by a single-parameter slow-roll hierarchy.

The deeper issue is dimensional. Slow-roll epsilon is defined as epsilon = (1/2) (dot phi / H)^2 / M_Pl^{-2}, a dimensionless ratio of inflaton kinetic energy to the critical FRW energy density. Writing this expression requires a classical scalar phi(t) and a well-defined Hubble rate H(t). Neither exists pre-fold: §1 established that a(t) is not a fundamental dynamical variable before the a_2 coefficient has sourced it from the post-fold GGE, so H(t) is not defined, and there is no inflaton phi in the spectral action (the modulus tau parameterizes internal geometry, not a matter field). The consistency relation r = 16 epsilon is therefore not false here but ungrammatical in substrate language — the right-hand side fails to denote. Five independent closure arguments established in prior framework work confirm this structurally: (i) absence of slow-roll (§2b); (ii) the BLV acoustic metric separating scalar and tensor effective metrics; (iii) the entry-horizon Bogoliubov squeeze affecting scalar power but not tensor power in a single-field-common way; (iv) the BCS gap modifying scalar dispersion (Delta/omega ~ 0.27 at the fold, S73A W4-D) while leaving tensors unchanged; (v) the asymmetric fold (entry horizon present, exit horizon absent — §5) precluding any time-symmetric single-mode spectrum match. If n_s is a geometric property of the spectral triple and r is dominated by the tensor sector's independent conformal structure, the two quantities are set by different parts of the same spectral problem with no algebraic constraint linking them through a single slow-roll parameter.

---

## 3. Why a "Bounce" Does Not Describe This Either

If inflation fails, a natural next question is whether the fold is a bounce. Before S73A, the framework occasionally used bounce language — the transit is a fold, something happens at a minimum, the system "passes through." Bounce cosmologies (Ashtekar loop quantum cosmology, Penrose conformal cyclic cosmology, ekpyrotic models) have familiar structure: a contracting branch, a non-singular minimum, and an expanding branch, joined smoothly or conformally across the bounce surface. The substrate transit has no contracting branch, no time-symmetric structure across the fold, and no conformal matching condition. Each of these failures is structural and established at machine precision by S73A and earlier results.

### 3a. A Bounce Is Symmetric; the Fold Is Not

The defining geometric property of a bounce is time-reversal symmetry about the bounce surface. In an Ashtekar LQC bounce, the scale factor a(t) satisfies a(-t) = a(t) about the minimum; in ekpyrotic bounces, the contracting and expanding phases are mirror images under t -> -t. This is not decorative — it is forced by the presence of a single degree of freedom (the scale factor) driven by a single energy density, which necessarily produces symmetric kinematics across any turnaround point.

The substrate fold does not have this symmetry. S73A W1-A computes the modulus velocity v_tau through the entire BCS gap profile and finds that the Mach number Ma_BA = v_tau / c_BA stays in the interval [20.71, 20.76] — varying by less than 0.2% across the full tau range [0.164, 0.224] in which BCS physics is active. The transit is deeply supersonic EVERYWHERE. There is no tau at which v_tau passes through c_BA, no turnaround, no slowdown-then-speedup, no symmetric structure of any kind. The modulus ploughs through the fold like a plank of wood struck once by a hammer; it does not rock back and forth. The mathematical object this analogy indexes is the multi-mode Landau-Zener-Stuckelberg monodromy of the BdG mode functions across a classical turning point in a non-adiabatic transit (Parker 1969 for the quantum field theory generalization, Parker-Toms 2009 for the curved-spacetime treatment). Unlike the two-level Landau-Zener problem, the 8 BCS modes share a common drive through dS/dtau and their monodromies are correlated across the fold, producing the phase-locked squeezed vacuum of §6a rather than independent tunneling events.

The asymmetry goes deeper than just the velocity profile. On the entry side, the compound decoherence channel identified in W3-A (FABRY-PEROT-73a) sees a large thermal occupation n_bar = 85.2 per mode from the entry horizon. On the exit side, W1-A establishes that no sonic horizon exists — the Mach number never reaches 1, so no Hawking-like horizon radiation can be associated with the exit. The entry-side horizon produces a thermal particle population; the exit side produces only the sub-thermal impulsive Bogoliubov production (n_k in [2.52e-5, 1.34e-2] per mode, W1-A). Ratio ~7000x. The two sides of the fold are structurally different in their particle-production physics. A bounce cannot look like this. A bounce is a time-reflection; the substrate transit is not.

### 3b. LQC Bounces Require a Contracting Branch — the Substrate Has None

Loop quantum cosmology bounces have a precise kinematic structure: a pre-bounce FRW universe contracts under matter or radiation domination, the energy density rises until it hits the Planck energy density rho_Pl, at which point quantum-gravity corrections to the effective Friedmann equation H^2 = (8 pi G / 3) rho (1 - rho/rho_Pl) drive H = 0 and the universe bounces. The pre-bounce branch is a genuine FRW contracting universe with a contracting scale factor, contracting Hubble rate, and the usual particle content. The bounce is then the transition between this contracting branch and the expanding one we observe today.

The substrate transit has no pre-fold contracting FRW branch. The modulus tau is a spectral parameter, not a cosmological scale factor. Its evolution is monotone in the forward direction dictated by the sign of dS/dtau (+58,673 for the physical spectral functional f_*, positive sign for f_* and sqrt, per S73A W1-D SPECTRAL-ACTION-PROFILE-73a). There is no configuration in which tau runs backward through the fold, no time at which the spectral action acted as an effective attractor from the far past. The "pre-fold" phase is not a contracting universe; it is the same internal geometry with the same spectral triple but at a smaller value of tau, carrying a different eigenvalue spectrum with different relative weights between the u(1), su(2), and C^2 sectors of the Jensen metric.

The Friedmann equation is not the fundamental dynamical equation here. It is an emergent effective description of how the a_2 Seeley-DeWitt coefficient couples to matter once the post-fold GGE relic has been produced. Asking whether there is a "contracting branch" is asking whether the pre-fold configuration admits an emergent Friedmann description at all. It does not. Before the fold there is no well-defined scale factor a(t) for which a Friedmann equation can be written, because the spectral content has not yet condensed into the BCS state that produces the GGE and therefore has not sourced an emergent gravity sector. The LQC bounce's contracting-branch structure is absent not because the transit fails to contract but because the transit is not happening in the kinematic category where "contraction" is defined. The pre-fold configuration is not metaphysically void: it is a well-defined value of tau at which the spectral action S(tau) is evaluated and at which the a_0, a_2, a_4 Seeley-DeWitt coefficients take different numerical values from the post-fold ones. In particular, G_N (the coefficient of Einstein-Hilbert from a_2) is a different number pre-fold than post-fold, so an emergent 4-metric CAN be constructed at any tau — it is just a different metric from the one we observe today. The statement "no contracting branch" means no pre-fold FRW evolution, not "no pre-fold geometry."

### 3c. Penrose CCC Crossover Is Conformal; This Is Spectral, Not Conformal

Penrose's conformal cyclic cosmology proposes that successive aeons are glued together by a conformal rescaling at their infinite-future null infinity. The matching condition is a continuous conformal map Omega(x) from one aeon's future boundary to the next aeon's past boundary, with the metrics related by g'_{mu nu}(x) = Omega(x)^2 g_{mu nu}(x). This is a map between two Lorentzian manifolds that preserves causal structure while rescaling distances. It requires both aeons to be continuous manifolds with well-defined asymptotic behavior, and the matching is done in the category of conformal classes of pseudo-Riemannian manifolds.

The substrate fold is not a conformal matching in this sense because the two sides of the fold are not two aeons with a conformal map between them. They are two values of tau within one spectral triple. The transit acts on the Dirac operator D_K(tau) itself: its eigenvalue spectrum reorganizes as tau advances through the van Hove singularity. Three features forbid reading this as a conformal rescaling.

First, the D_K eigenvalue spectrum is discrete. A conformal rescaling of a continuous Lorentzian manifold is a continuous operation; a reorganization of a discrete spectrum is combinatorial. The fold shuffles which Peter-Weyl sectors dominate — the sum d^2 lambda^2 runs from 389,244 at tau = 0 to 541,473 at tau = 0.5 [S73A W3-D] — and this is not the kind of deformation a conformal factor represents. Modes change labels, exchange dominance, open and close gaps. Conformal factors simply multiply metric components.

Second, the spectral action is NOT conformally invariant. The Jensen deformation g|_{u(1)} = e^{2tau}, g|_{su(2)} = e^{-2tau}, g|_{C^2} = e^{tau} preserves volume (the volume-preserving theorem, exact, S12) but it is not a Weyl rescaling — it rescales different blocks of the metric by different factors, tangentially to a single volume-preserving direction. The spectral action S(tau) = Tr f(D_K^2 / Lambda^2) changes under this deformation even though the metric volume does not (S_fold / S(0) = 1.012 for f_*, S73A W1-D). This is precisely the spectral action's sensitivity to shape rather than just scale. A Penrose-style conformal matching cannot act on this deformation direction, because the direction is explicitly non-conformal.

Third, CCC requires the two aeons to be causally disconnected except at their shared conformal boundary. The substrate's pre-fold and post-fold sides are not causally disconnected because there is no bulk spacetime at which to define causal disconnection before the fold. They are algebraically connected through the same spectral triple, related by a one-parameter deformation of D_K rather than by a conformal map between two separate manifolds. The matching condition CCC would impose — Weyl tensor continuity across conformal infinity — has no analog in the substrate picture, because the objects being matched are spectral data of a single D_K, not causal boundaries of two 4-manifolds.

The three conventional alternatives to inflation — bounces, cyclic cosmologies, and ekpyrotic pre-Big-Bang models — share a common presupposition: cosmogenesis is an event in the evolution of a 4-metric. They differ only in what kind of event (turnaround, conformal matching, brane collision). The substrate picture breaks this presupposition. Cosmogenesis is not an event in a metric's evolution. It is a reorganization of the eigenvalue data of an internal Dirac operator, from which the 4-metric is only subsequently derived by spectral integration. To ask whether it is an "inflating" or "bouncing" or "cycling" metric is to ask a question of the wrong type.

### 3d. The Monopole Problem Is Absent by Construction

The standard monopole problem of GUT cosmology is: symmetry breaking at T ~ 10^16 GeV produces topological monopoles with density ~1 per horizon volume, vastly overpopulating the universe and requiring inflation to dilute them below observable levels. In the substrate picture there is no such problem to solve. The Standard Model gauge group U(1)_Y x SU(2)_L x SU(3)_C is fixed geometrically by the KO-dimension 6 classification of the Dirac operator D_K on Jensen-deformed SU(3), a structural property of the spectral triple valid at every tau [phonon_exflation_cosmology.md §8.7]. There is no GUT-era symmetry-breaking transition in which a larger gauge group spontaneously reduces to SU(3) x SU(2) x U(1), because there is no larger gauge group — the SM gauge content is the full gauge structure at every tau, and only the coupling constants evolve with tau (the Jensen deformation rule g_1 / g_2 = e^{-2 tau}). Monopoles as topological defects of a breaking transition therefore have no production mechanism, and the dilution problem that inflation was introduced to solve simply does not arise.

---

## 4. The Single-Pulse Mechanism — Jensen Hammer on the Fiber

With inflation and bounce vocabularies eliminated, the substrate picture needs its own positive description of what happens at the fold. The description is structurally simple: a single impulsive drive on the internal fiber's eigenvalue spectrum produces a single-pass parametric amplification event, leaving behind a squeezed ordered output. There is no ongoing drive, no oscillation, no return. The hammer strikes once, and the ringing that follows is what we measure.

### 4a. The Drive: dS/dtau as the Impulsive Force

The forcing term is the gradient of the spectral action along the Jensen deformation direction. At the fold,

    dS / dtau = +58,673   (Lambda-normalized, f_* spectral functional)

[phonon_exflation_cosmology.md §8.7.9, S73A W1-D SPECTRAL-ACTION-PROFILE-73a]. This is enormous relative to the natural scale of the eigenvalue problem. The spectral action value itself at the fold is S_fold = 250,361, and the second derivative is d^2 S / dtau^2 = 317,863. The gradient does not reverse anywhere in the scanned range tau in [0, 2] for the physical functional f_*: the profile is monotonically increasing. The drive therefore has no equilibrium — the modulus does not oscillate about a minimum because there is no minimum.

Note on units: the chapter quotes S_fold = 250,361, dS/dtau = 58,673, d^2 S/dtau^2 = 317,863 in canonical Lambda-normalized units (the convention of phonon_exflation_cosmology.md §8.7.9). The computation script s73a_spectral_action_profile reports the same spectral action in dimensionless Gilkey form with S_f*(fold) = 31,244.57, related to the Lambda-normalized form by a factor of 8.0 (from the f_0 f_2 f_4 moment normalization of the cutoff). The two conventions are numerically cross-checked at S73A W1-D line 213-214 to deviation 6.4e-15 (machine epsilon). Every derivative ratio used in this chapter (epsilon_H, n_s) is scheme-independent because the factor-of-8 cancels.

The force this gradient exerts on the modulus can be read directly from the effective equation of motion for tau. Using the Z_fold effective mass and the dS/dtau gradient, S73A W1-A establishes that the modulus velocity in the transit region is v_tau = 8.27 M_KK (varying by less than 0.2% across the BCS gap profile). This is faster than the largest BA sound speed c_BA = 0.399 M_KK by a factor of 20.7 — the transit Mach number. The drive is in every meaningful sense an impulsive force: large, one-sided, unopposed by any restoring term from the spectral action itself. There is nothing in the dynamics that would bring tau to rest at the fold or decelerate it on the other side. The spectral action monotonicity is a permanent theorem within the f_* and sqrt functionals; it constrains the drive to be monotonic in tau across the fold.

The impulsive character of the drive is the physical origin of everything else in this chapter. A monotonic, large gradient acting on a modulus produces a fast non-adiabatic passage through any resonance feature in the mode frequencies — and the fold is exactly such a feature, the van Hove singularity in the B2 flat band. The Jensen hammer is a specific mathematical object: the gradient of the spectral functional evaluated on the Jensen-deformed SU(3) metric family, acting in the single direction picked out by the family's parameterization.

### 4b. The Response: BCS Mode Frequencies Traversing the van Hove Singularity

The object being driven is the 8-mode BCS sub-spectrum of D_K that participates in the Bogoliubov-Anderson singlet sector — 4 B2 modes (flat quartet), 1 B1 mode (acoustic singlet), 3 B3 modes (dispersive triplet) [S31Ca branch structure]. Each mode has a tau-dependent frequency omega_k(tau) set by the combination of the Dirac eigenvalue at (tau) and the BCS gap Delta(tau) that opens at the van Hove singularity. As the modulus crosses tau ~ 0.19, the flat B2 band reaches a point where Delta / omega_k becomes comparable to the natural BCS scale (Delta / omega ~ 0.27 at the fold, S73A W4-D), and the mode frequencies rearrange.

Concretely, the BCS gap is a smooth function of tau, fit linearly in the scanned region [S73A W4-E JJ-KAPPA-MAP-73a]:

    Delta(tau) = -0.2441 tau + 0.5118   (M_KK, max fit residual 0.06%)

The derivative dDelta/dtau = -0.244 M_KK is O(1) in natural units. The mode frequencies omega_k(tau) therefore change by O(1) in a transit time dt_transit = 1.13e-3 M_KK^{-1} [S73A W2-C]. This gives an adiabatic parameter

    gamma_k = |d ln omega_k / dt| / omega_k = |dDelta/dtau| * |dtau/dt| / omega_k^2

which evaluates to the gamma_k table of §2b: every mode is non-adiabatic by at least an order of magnitude. The response of each mode to this forcing is a parametric amplification — the mode's effective oscillator equation d^2 u_k / dtau^2 + Omega_eff^2(tau) u_k = 0, with Omega_eff^2(tau) = omega_k^2 + Delta(tau)^2, is solved in the BLV transfer-matrix formulation [S73A W4-D BLV-COMPOUND-73a PASS] and in the BdG formulation [S73A W1-A] independently, with mutually consistent outputs.

The result is a Bogoliubov transformation of the mode's quantum state. An initial vacuum state is mapped to a squeezed vacuum, with squeeze parameter r_exit for each mode given by the transit Bogoliubov calculation. The 8 modes acquire the occupation numbers and squeeze parameters tabulated in W1-A (reproduced in §6a below). The physical response is therefore not a classical rolling but a QUANTUM parametric response — the modes are kicked out of their ground states into squeezed-vacuum states, with the squeeze parameters set by the impulse shape of the drive and the mode dispersion as a function of tau.

This is what parametric amplification means in quantum optics: a time-dependent modification of a mode's frequency produces pair creation from the vacuum, with the pair count and phase set by the Bogoliubov coefficients beta_k. The amplitude of the response is controlled by the impulse's time profile through the integral

    beta_k ~ integral dt exp(2 i integral omega_k dt') * (d omega_k / dt) / (2 omega_k)

with the integral dominated by the region of rapid frequency change. In the substrate transit, that region is the van Hove singularity, and the dominant contribution comes from each mode's passage through the point where Delta(tau) becomes comparable to omega_k. Every mode has this contribution; the strength varies by mode because omega_k varies, giving the n_k hierarchy observed in W1-A.

### 4c. Parametric Amplification Window: Mach 20.7, WKB Fails Completely

The quantitative statement of the parametric amplification window is that the modulus crosses the van Hove singularity at supersonic speed relative to the natural sound speed of the driven modes themselves:

    Ma = v_tau / c_BA = 20.73   [S73A W1-A, constant to 0.2% across the BCS gap profile]

A subsonic passage (Ma << 1) would correspond to a slow deformation of the mode spectrum through which the modes could adiabatically track their instantaneous ground states. Ma ~ 1 is the marginal adiabatic case. Ma = 20 is deeply in the impulsive regime, where the mode functions cannot follow the time-varying frequencies and instead couple strongly to their own complex-conjugate modes — the mechanism behind Bogoliubov pair production in any time-dependent quantum field theory (Parker 1969, applied to BCS dynamics here).

The 8 modes respond to this impulsive drive with sub-thermal but non-negligible Bogoliubov production:

| Mode | n_k = |beta|^2 | r_exit |
|:-----|:---------------|:-------|
| B2[0] | 2.52e-05 | 0.005 |
| B2[1] | 3.94e-04 | 0.020 |
| B2[2] | 1.58e-03 | 0.040 |
| B2[3] | 2.84e-03 | 0.053 |
| B1 | 4.72e-03 | 0.069 |
| B3[0] | 1.07e-02 | 0.103 |
| B3[1] | 1.34e-02 | 0.116 |
| B3[2] | 1.19e-02 | 0.109 |

[session-73a-results-workingpaper.md W1-A]. Unitarity holds to machine epsilon: max ||alpha_k|^2 - |beta_k|^2 - 1| = 5.55e-15, fourteen orders below threshold.

Two features distinguish this impulsive production from a thermal horizon radiation. First, the integrated n_k is O(1/100) per mode, whereas a thermal horizon at the effective temperature of the transit would produce n_bar ~ 85 per mode. The ratio is ~10^3: the fold transit produces ~1000x fewer particles than a thermal horizon at the same surface gravity would produce. This is the quantitative consequence of the transit being too fast to thermalize — the modes are kicked out of equilibrium but the kick is too brief to populate a full Planck distribution.

Second, the phases of the Bogoliubov amplitudes are almost perfectly aligned. Inter-branch phase variance is 0.00015 rad (B2-B1), -0.00058 rad (B1-B3), and the intra-branch phase variance is at the 1e-9 level [S73A W1-A cross-check 4]. The fold transit preserves coherence rather than destroying it, because the impulsive drive is too brief to dephase the modes. This 1e-9 rad intra-branch phase coherence is the reason the horizon problem does not arise in the substrate picture — an observation developed in §4e — because the 8 Bogoliubov modes that seed the post-fold density field are not causally disconnected patches that somehow thermalized to the same temperature but a single SU(1,1)-squeezed vacuum generated by a shared Hamiltonian, phase-locked by construction.

The window in which parametric amplification occurs is the BCS gap profile range tau in [0.164, 0.224], which corresponds to the transit duration dt_transit = 1.13e-3 M_KK^{-1} [S73A W2-C]. This is the entire duration of the fold. The drive fires once, during this window, and then stops. The post-transit substrate is the output of this single window.

### 4d. Single-Pass, Not Oscillatory

Parametric amplification in driven oscillators is typically an ongoing process: pump a nonlinear optical crystal or a Josephson parametric amplifier with a coherent drive, and the idler/signal modes grow as long as the pump is on. The substrate's parametric amplification event is structurally different — the hammer strikes once. Four independent features enforce the single-pass character.

First, the spectral action gradient is monotonic and does not return. S73A W1-D SPECTRAL-ACTION-PROFILE-73a confirms for the physical functional f_* that dS/dtau > 0 for all tau > 0.19 in the scanned range tau in [0, 2], with no post-fold equilibrium. The modulus does not come back; it advances forward in tau, past the fold, and the drive continues to push. There is no mechanism within the spectral action for the modulus to return to tau < 0.19 and re-strike.

Second, the fold is a specific topological event in the eigenvalue spectrum. At tau = 0.19 the van Hove singularity in the B2 flat band produces the BCS pairing transition; this occurs at one tau value only, because the van Hove singularity is a single point in the spectrum [S31Ca, B2 flat band at W = 0.058, symmetry-protected BIC]. As the modulus advances past the fold, tau continues to increase, but there is no second van Hove singularity at a nearby tau for the hammer to strike again. The specific feature being amplified — the BCS pairing transition at the van Hove divergence — is a one-time topological event in the modulus history.

Third, the instanton gas picture (S38, confirmed at S66) identifies the post-fold state as an ordered GGE relic protected by 8 Richardson-Gaudin conserved integrals. The relic is integrable. It does not spontaneously regenerate a drive; the GGE is not a periodic cycle but a frozen-in configuration of the Cooper-pair population. Any attempt to re-strike would require breaking the integrability (injecting energy into the system in a form that couples to the pairing sector), which by construction has no available mechanism in the post-fold substrate.

Fourth, the asymmetric horizon structure (§5) forbids the drive from leaving a recoil mechanism that could return it. The entry side carries a thermal particle population but the exit side is an open boundary. There is no reflected wave to bring the system back to a pre-fold configuration, because the exit side has no horizon at which to reflect anything.

The contrast with a driven parametric oscillator is sharp. A driven oscillator (e.g., Faraday instability in a pendulum) has a drive that persists, and the system sustains oscillation for as long as the drive remains on. Mathematically, such a system is characterized by an ongoing SU(1,1) Bogoliubov flow: the squeezing transformation U(t) = exp(i H_sq(t) t) is compounded at every instant as the drive injects energy. The substrate's parametric amplification event, by contrast, is a single SU(1,1) element — one squeezing operator acting once on the vacuum — not a time-ordered product of many. The post-fold state is a squeezed vacuum, not a compounded-squeezing coherent state. This is the mathematical content of "the hammer strikes once": the output lives in the single-element coset SU(1,1)/U(1), not in the continuous flow that an ongoing pump would generate.

### 4e. Horizon Problem Absent by Construction

The horizon problem of standard cosmology is: the CMB is thermalized across ~10^5 causally disconnected patches at last scattering, and inflation is introduced to phase-correlate them before they decouple. The question is how regions that never could have been in causal contact arrived at the same temperature. Inflation answers it dynamically: stretch a single quantum fluctuation mode across the causal horizon, and the whole observable sky inherits its correlations.

The substrate picture makes this question disappear. The 8 post-fold Bogoliubov modes are one SU(1,1) squeezed vacuum state generated by a single Hamiltonian acting on a single substrate configuration. They are phase-locked at 1e-9 rad intra-branch [S73A W1-A cross-check 4] and at the milliradian level inter-branch, with the entire mode set sharing the same dS/dtau drive and the same van Hove singularity. This is maximal phase correlation — the modes are not "causally disconnected patches that somehow happen to be at the same temperature," they are ONE squeezed vacuum state with a shared generating Hamiltonian that phase-locks them by construction.

The emergent 4-manifold is built AFTER the fold from the a_2 Seeley-DeWitt channel acting on this phase-locked state. The causal structure of the 4-metric — the light cones, the sound horizons, the notion of "causal disconnection" itself — is downstream of the post-fold state, not upstream. When the emergent 4-manifold is constructed, the modes that source the primordial density field are not distinct modes propagating through independent regions; they are a single 8-mode squeezed vacuum carried by a shared substrate. The CMB is thermalized across the observed sky because its source state was phase-locked from the start. There are no causally disconnected patches at the fold because there is no pre-existing 4-manifold on which to define causal disconnection.

The horizon problem is therefore absent because its PRECONDITION is absent — not because a dynamical mechanism solves it, but because the kinematic category in which it is formulated (pre-existing spatial slices needing to thermalize) does not obtain. This is structurally a stronger statement than the inflationary resolution. Inflation solves the horizon problem by stretching a single quantum fluctuation across a pre-existing causal horizon, leaving the "why this mode?" question open. The substrate answers "why this mode?" with "because the entire eight-mode set is a single squeezed vacuum generated by a single application of a single operator, and the 4-manifold on which 'horizons' are defined is downstream of that vacuum."

The observational consequence is subtle but specific: the primordial density field inherits not just approximate homogeneity but a specific phase structure from the 8-mode squeezed vacuum. The branch-structure modulations on the LSS power spectrum (§7c) and the low-l asymmetric-fold signature in the CMB (Gate 4 of §9) are the specific imprints of this phase-locked origin — positive detection gates that would confirm the substrate mechanism, rather than the "no pre-inflationary features expected" null signature that inflation produces.

---

## 5. Asymmetric Fold: Entry Horizon, Open Exit

The asymmetric fold is the single structural feature that distinguishes this mechanism most sharply from all competing cosmogenesis pictures. The entry side has a thermal Hawking-like horizon that produces a well-populated particle spectrum. The exit side has no sonic horizon at all; the modulus leaves the transit region at Mach 20.7 and never decelerates. The two sides are geometrically inequivalent. This is not a gauge artifact — it is a direct consequence of the monotonic Jensen deformation and the specific location of the van Hove singularity in the B2 flat band.

### 5a. The Entry Horizon: kappa_entry = 79,386 M_KK, n_bar = 85.2 per Mode

The entry horizon appears in S73A W3-A [FABRY-PEROT-73a] as a well-characterized thermal feature at the entry-side boundary of the BCS gap profile (tau_entry = 0.2195). S73A W3-A reports the surface gravity and the resulting thermal Bogoliubov occupation directly:

    kappa_entry = 79,386 M_KK        (W3-A line 521)
    n_bar       = 85.2 per mode      (W3-A thermal Bogoliubov)

These are the two primary quantities. The effective temperature relevant to the 8 BCS mode energies can be derived as T_eff = kappa_entry / (2 pi) ~ 1.26 x 10^4 M_KK in bare form, reduced by the impedance-matched mode volume factor to give the observed n_bar = 85.2 through the Bose-Einstein occupation formula 1/(exp(omega/T_eff) - 1) with the BCS band frequencies omega_BCS ~ 0.1 M_KK. The chapter carries kappa_entry and n_bar as the primary inputs and derives T_eff as needed.

This is structurally different from the transit Bogoliubov production computed in §4c, which gives only n_k ~ 0.01 per mode from the impulsive parametric amplification. The ratio between the two is ~7000x — the entry horizon dominates particle production by nearly four orders of magnitude.

The physical distinction between the two channels is that the entry horizon is a STATIONARY feature on the entry side of the fold: the modulus velocity v_tau is approaching the BCS gap profile region from below, where the effective sound speed is still evolving, and a stationary horizon can form where the incoming flow speed matches the local sound speed. Once inside the gap profile (tau in [0.164, 0.224]), the Mach number is stuck at 20.7 and no further horizon can form. On exit, the Mach number remains at 20.7, so no exit horizon forms on the far side either.

The thermal character of n_bar = 85.2 is important. A thermal horizon produces uncorrelated phases across modes (Hawking radiation is stochastic), whereas the impulsive transit production is coherent across all 8 modes (phase variance at the 1e-9 level within branches). The entry horizon and the transit Bogoliubov production are therefore distinguishable by their phase structure in addition to their amplitudes. The compound decoherence at the exit, computed in W3-A, comes from amplifying the INTER-BRANCH phase split 0.552 rad (the B2-B3 spread, which arises from branch-dependent couplings to the condensate) by n_bar = 85.2 through squeezing; the resulting inter-branch coherence C(B2, B3) = 2.3e-6 is complete decoherence between branches while preserving intra-branch coherence (Var within B2 = 3.6e-8, within B3 = 8.5e-8). This block-decoherence structure is the direct physical fingerprint of the entry horizon's thermal particle population acting on the phase-coherent transit output.

### 5b. No Exit Horizon: S73A W1-A Conclusively Closes This Vocabulary Debt

Before S73A, the framework carried a vocabulary debt: several sessions had referred to "entry and exit horizons" for the fold transit, analogous to pair-horizon structures in acoustic white/black hole analogs, without having computed whether the exit horizon actually exists as a sonic feature. S72 flagged this as an open carry-forward. S73A W1-A resolves it definitively.

The computation integrates the effective equation of motion for the modulus across the BCS gap profile using the Z_fold effective mass and the canonical spectral action gradient, extracting v_tau(tau) at every point. The Mach number Ma_BA = v_tau / c_BA is then computed for each tau. The result:

    Ma_BA(tau) in [20.71, 20.76]   for tau in [0.164, 0.224]

The modulus velocity varies by less than 0.2% across the entire BCS gap profile range. The Mach number never approaches 1. There is no tau at which v_tau = c_BA. No sonic horizon exists anywhere inside or outside the BCS gap region, on either side of the fold. This is a definitive closure of the "exit horizon" vocabulary: it does not exist as a sonic feature.

The key structural observation is that the modulus velocity is not set by a dynamical equation in which friction or vacuum energy could decelerate it. It is set by the spectral action gradient dS/dtau = +58,673, which remains constant in sign across the whole fold region (as the spectral action is monotonic in the f_* functional, S73A W1-D). With a constant sign and O(1) magnitude of the driving gradient and a fixed effective mass Z_fold for the modulus, v_tau is approximately constant across the transit, and the computed value 8.27 M_KK is far above c_BA = 0.399 M_KK. The Mach 20 result is not a fine-tuned coincidence; it follows from the spectral action being a fast-varying function of tau while the BCS modes are slow collective excitations at much lower frequency.

W1-A therefore produces a structural outcome, not a numerical one: the asymmetry of the fold is not an artifact of the gap profile's endpoints — it is the signature of the impulsive drive's strength relative to the sound speed of the driven modes. Bounce and CCC mechanisms both require a symmetric horizon structure across the fold (for bounces, symmetric scale factor; for CCC, continuous conformal matching). The substrate transit does not have this. The picture is a one-sided acoustic analog: an entry horizon where the pre-fold flow meets the BCS region, a supersonic transit through the gap profile, and an open exit where nothing decelerates and no horizon forms.

### 5c. Why the Asymmetry Is Physical, Not Gauge Artifact

A natural skeptical objection is that the asymmetry could be an artifact of the tau parameterization — a choice of coordinates on the moduli space that happens to be monotone in the forward direction but could be reversed by relabeling. The objection fails at three separate levels.

First, the Jensen deformation is not arbitrary. The three block scalings g|_{u(1)} = e^{2tau}, g|_{su(2)} = e^{-2tau}, g|_{C^2} = e^{tau} are constrained to be volume-preserving (L_1 * L_2^3 * L_3^4 = 1 for all tau, theorem S12). This is one constraint on three block scalings, leaving a two-dimensional family of volume-preserving deformations. The Jensen direction is a specific one-dimensional line within this family, selected by the requirement that the spectral action's gradient is maximal in that direction at the round SU(3) metric (tau = 0). It is a physical direction in moduli space, not an arbitrary label.

Second, the spectral action S(tau) is not reflection-symmetric about the fold. S73A W1-D SPECTRAL-ACTION-PROFILE-73a computes S(tau) across tau in [0, 2] and finds that the profile is monotonically increasing for the f_* and sqrt spectral functionals. There is no tau_mirror such that S(tau) is symmetric under tau -> 2 tau_fold - tau. The system has no symmetry that would exchange the entry and exit sides. This is invariant under reparameterization of tau — under any smooth relabeling tau' = f(tau), the non-symmetry of the profile persists as the non-symmetry of S(tau'(tau)).

Third, the van Hove singularity at tau ~ 0.19 is a specific topological feature of the B2 flat band, and its location is determined by the B2 band structure rather than by a choice of tau origin. Shifting tau by a constant does not move the van Hove singularity; the singularity is at a fixed value of tau in any parameterization where tau is smooth and monotone. The entry side of the fold (small tau, pre-van-Hove) and the exit side (large tau, post-van-Hove) are distinguished by whether the BCS pairing gap has opened — they carry different BCS states, not merely different labels.

The asymmetry of the fold is therefore a physical feature of the coupled (modulus, BCS) dynamics on the substrate, not a coordinate choice. This is what separates the substrate transit from bounce cosmologies (which are symmetric by construction) and from CCC (which is conformally symmetric by construction). The one-sided asymmetry is the direct imprint of the monotonic spectral action gradient and the topological localization of the van Hove singularity — two independent structural features of the Jensen-deformed SU(3) spectral triple.

---

## 6. The Post-Pulse Ringing — GGE Relic as the Observable Universe

After the hammer strikes, the building rings. The substrate rings in a specific, ordered pattern — the 8-mode Bogoliubov output of the parametric amplification event, frozen into a Generalized Gibbs Ensemble by the integrability of the BCS Hamiltonian, slowly relaxing through weak coupling to the emergent gravitational sector. This ringing is what we call "the universe." Structure formation, the CMB, the Hubble rate, and the observed equation of state are all features of the ringing spectrum, not of a separate dynamical process imposed on top of it.

### 6a. Output of the Single Firing: Ordered Bogoliubov Excitations

The output of the parametric amplifier is the 8-mode Bogoliubov transformation table from S73A W1-A:

| Mode | n_k = |beta_k|^2 | r_exit | gamma | Gamma_greybody |
|:-----|:-----------------|:-------|:------|:----------------|
| B2[0] | 2.518e-05 | 0.005 | 1.68 | 0.999975 |
| B2[1] | 3.943e-04 | 0.020 | 6.65 | 0.999606 |
| B2[2] | 1.583e-03 | 0.040 | 13.24 | 0.998421 |
| B2[3] | 2.837e-03 | 0.053 | 17.81 | 0.997171 |
| B1 | 4.722e-03 | 0.069 | 23.58 | 0.995301 |
| B3[0] | 1.072e-02 | 0.103 | 32.96 | 0.989391 |
| B3[1] | 1.344e-02 | 0.116 | 36.59 | 0.986735 |
| B3[2] | 1.193e-02 | 0.109 | 35.12 | 0.988209 |

[session-73a-results-workingpaper.md W1-A]. These 8 squeeze parameters and 8 occupation numbers are the ringing modes. They are not a thermal distribution — n_k varies by three orders of magnitude across the 8 modes, in contrast to a thermal Planck distribution where all modes at a given temperature carry the same n_bar. The hierarchy n_k ~ omega_k^{-2} follows from the adiabaticity parameter hierarchy: lower-frequency modes (B3) see a faster frequency variation relative to their own clock and get kicked harder, while the flat-band modes (B2) have nearly degenerate frequencies and get kicked gently.

The phase structure of the ringing is also ordered. The arg(beta_k) values are nearly identical across all 8 modes (inter-branch spread at the milliradian level, intra-branch spread at the nanoradian level — W1-A cross-check 4), meaning the modes are phase-locked. This is a coherent squeezed state, not a thermal mixed state. The density matrix of the post-fold substrate is (approximately) a product of 8 squeezed vacuums with correlated squeeze axes, modulated by the compound block-decoherence structure imposed by the entry horizon's thermal n_bar (§5a).

The "output" here is a quantum-mechanical object — a squeezed coherent state in the 8-mode BCS Fock space — not a classical field configuration. It is the specific pattern of quantum amplitudes set by the impulse shape of the hammer strike. Any physical observable derived from the post-fold substrate must be computed by tracing over this squeezed vacuum: the CMB power spectrum is the 2-point function in this state, structure formation is the gravitational response to density fluctuations in this state, and the Hubble rate is the slow relaxation rate of this state toward whatever ground state the emergent gravity sector defines.

### 6b. Integrability Protects the Ringing from Thermalizing

A natural objection is that an impulsively produced squeezed state in a many-body system should thermalize rapidly — quantum-chaos arguments suggest that generic many-body systems with O(1) interactions erase initial ordering on timescales short compared to any cosmological relaxation. The substrate's 8-mode BCS Hamiltonian is not a generic many-body system. It is Richardson-Gaudin integrable, with 8 conserved integrals of motion at N_pair = 1 [phonon_exflation_cosmology.md §5.2]. These conserved integrals forbid the kind of occupation mixing that would be required to drive the post-fold state toward a thermal distribution.

The integrability-protection result is multi-verified at 9/9 independent criteria established across S38 and the subsequent gates:

- Timescale separation: t_Thouless / t_transit in [65, 596,367] across modes (the weakest mode's Thouless time exceeds the transit by 65x; the strongest by ~6e5)
- Spectral form factor: SFF factorizes exactly into a product of mode-resolved SFFs, no off-diagonal coupling
- Level statistics: beta = 0.500 (Poisson), confirming integrability — the spectrum does not repel
- Pomeranchuk stability: 5x stronger than the instability threshold — the GGE is thermodynamically stable
- Causal exclusion: light-crossing time of the internal space exceeds the transit time by 528x
- Dipolar thermalization: Leggett-to-Goldstone decay kinematically forbidden (5.5x gap ratio), tau_Leggett / t_transit = 22,811
- N_pair conservation at supersonic transit: |delta_N_pair / N_pair| = 2.22e-16 (machine epsilon) from S73A W3-B LUTTINGER-SUPERSONIC-73a PASS

The N_pair conservation result from W3-B is particularly strong. It is not a dynamical property of the BCS evolution — it is an algebraic superselection rule: [H_BCS, N_pair] = 0 identically, for any BCS-type Hamiltonian. The Fock space factorizes into N_pair sectors that cannot be connected by unitary time evolution, regardless of how fast the transit is or whether the system is adiabatic. This holds even in the presence of non-integrable perturbations up to eps = 0.1 [S73A W3-B cross-check 6]. The pair sector the ringing modes live in is sealed.

The physical consequence is that the 8 squeeze parameters r_k and 8 occupation numbers n_k are frozen in at the moment of the fold transit and do not relax into a thermal distribution. They remain as an ordered chord — a specific set of amplitudes and phases — for as long as the integrability holds. This is the precise content of the Ordered Veil: the post-fold substrate rings with a chord set at the instant of the transit, preserved by the Richardson-Gaudin conservation laws, never decaying into thermal noise. The universe we observe is the low-energy projection of this frozen GGE state.

This is also the core structural property that distinguishes the substrate picture from any previous phonon/acoustic cosmology. In a generic acoustic analog system (e.g., a BEC), thermalization is rapid and the post-quench state relaxes on microsecond timescales to a thermal distribution. The substrate is protected from this by the integrability of its BCS Hamiltonian and by the block-diagonal theorem for the Dirac operator on compact Lie groups (S22b). The protection is structural, not fine-tuned, and it is what makes the ringing observable on cosmological timescales.

### 6c. Hubble as Slow Relaxation — The Friedmann Reduction

This is the central observational identification of the chapter. In standard cosmology, H(t) is the rate of change of the scale factor a(t), driven by the energy density through the Friedmann equation. In the substrate picture, a(t) is not a fundamental dynamical variable — it is an emergent description of how the a_2 Seeley-DeWitt coefficient couples to the post-fold GGE state [phonon_exflation_cosmology.md §8.7]. The observed Hubble rate is not a driven expansion but the slow relaxation of the ringing spectrum, read through the emergent Einstein equations.

The non-circular form of this reduction is direct evaluation of the GGE stress-energy tensor on the 8-mode squeezed vacuum, passed through the emergent Einstein field equations:

    G_{mu nu} = 8 pi G_N <T_{mu nu}>_{GGE}

where G_N is fixed by a_2 f_2 (§2a) and <T_{mu nu}>_{GGE} is the expectation value of the stress-energy tensor in the squeezed vacuum state of §6a. Taking the 00 component and specializing to an FRW ansatz g_{mu nu} = diag(-1, a^2, a^2, a^2) gives

    3 H^2 = 8 pi G_N <T_{00}>_{GGE}

which is the Friedmann equation without any rate-equation step. The dimensional structure is clean: <T_{00}>_{GGE} has units of energy density in 4D (M_KK^4 converted to GeV^4 via M_KK = 7.43 x 10^16 GeV [Phononic-to-Cosmos.md Convention Translation Table]), G_N has units of length^2 in natural units, and H^2 has units of inverse-time^2. The key operation is evaluating <T_{00}> directly on the 8-mode squeezed vacuum — no reference to a separate scale-factor evolution equation, and no circular definition in which H appears on both sides.

Concretely, <T_{00}>_{GGE} is the sum of mode energy contributions weighted by the Bogoliubov occupations:

    <T_{00}>_{GGE} = sum_k (n_k + 1/2) omega_k

over the 8 modes (with the 1/2 being the zero-point contribution) times the number density of cells that survived relaxation. The GGE-to-matter conversion factor — how many emergent 3-volume cells each internal spectral cell becomes — is the remaining quantitative input, and its computation is the primary carry-forward of this chapter (§10.1 s74_friedmann_from_a2.py).

The observational consequence of this identification: there is no "driven" era of inflation, no quintessence, no dark energy field slowly rolling. The Hubble rate's evolution history is the ringdown envelope of a single impulse, not the integrated response to a continuously active source. The radiation-dominated era corresponds to the phase where BCS mode energies dominate the stress-energy; matter-dominated to the phase where inter-band Leggett-channel mode energies dominate (the DM candidate); Lambda-dominated to the phase where the effacement-residual channel dominates. The transition redshifts are determined by the relative amplitudes of the three channels, which is a property of the 8 squeeze parameters r_k and the Volovik tracking vacuum partition.

The language shift this subsection performs is the essential one: Hubble is not an expansion rate, it is the envelope of a slow relaxation rate. The universe is not getting bigger in any absolute sense (the substrate has no "size" — see §1). The ordered Bogoliubov output is slowly losing amplitude through weak coupling to emergent gravity, and we measure the consequences of that amplitude loss as a Hubble rate in our local effective-metric description. The late-time accelerated expansion is directly consistent with Yonsei team [Lee et al., 2025] and DESI DR2 hints of dynamical dark energy: if the observed acceleration is the tail of a ringdown, w_0 and w_a should both deviate from the LCDM w = -1 in specific ways set by the ringdown profile rather than by a cosmological constant. The framework's current pre-registered prediction is w_0 = -0.509 +/- 0.079, w_a = -0.009 +/- 0.02. DESI DR3 will test this.

### 6d. Energy Flow: Three Channels and the Volovik Tracking Vacuum

If the ringing is slowly dying, where is the energy going? The natural question has a specific answer in the substrate framework: the energy flows out of the BCS pair sector into the emergent gravitational sector via the a_2 Seeley-DeWitt channel, into a stable dark matter population via the Leggett inter-band phase channel, and into the effective cosmological term via the effacement residual coupled to the Volovik q-theory tracking vacuum.

Quantitatively, the energy flow splits across three channels:

1. **Gravitational back-reaction through a_2**: The GGE's stress-energy tensor sources the emergent Einstein equations through the second spectral moment [phonon_exflation_cosmology.md §8.7.8]. Each unit of excitation amplitude in the BCS mode spectrum carries a proportional contribution to T_{mu nu} via the a_2 channel, and the mode's slow decay is coupled to the growth of spatial curvature and matter density fluctuations. This is the primary channel for energy flow out of the ringing: BCS mode amplitudes -> metric curvature -> large-scale structure gravitational self-organization. It sources Omega_m.

2. **The Leggett channel**: The inter-band phase mode (Leggett mode) is the lightest collective excitation in the substrate after the fold, with frequency omega_L ~ 0.05 M_KK [S59 canonical determination, eps_canonical = 0.00374]. Leggett modes are the dark matter candidate in this framework. Their gravitational decay is exactly forbidden by a Z_2 parity [S67 LEGGETT-GRAV-DECAY-67 PASS, session-73a-results-workingpaper.md W1-B] — the interaction Hamiltonian contains only even powers of phi_23, so single-Leggett decay L -> g+g is prohibited to all orders, leaving only the 2L -> 2g pair channel with tau_DM / t_universe = 1.1e65. The Leggett channel takes a portion of the BCS ringing amplitude and stores it in a stable DM population that does not decay. The S66 Leggett-only computation gives Omega_DM h^2 = 0.120 at 0.6% agreement with Planck.

3. **Effacement residual and the Volovik tracking vacuum**: The 0.03% leakage through impedance mismatch (Gamma = 0.99970) is the slow leak that appears as the cosmological term in the effective 4D description. The authoritative framework result for this channel is DILUTION-CC-66 Scenario B [baseline-findings-s66.md §6B]: Volovik q-theory relaxation rho_vac ~ M_Pl^2 H^2, landing at rho_vac(today) / rho_obs = 1.032 — 0.01 orders of magnitude from the observed cosmological constant. The 114 OOM that naive vacuum-energy counting gives between the fundamental scale and Lambda_obs is not a gap to close by a separate mechanism; in the phonon-exflation framework it IS exflation, the expansion history itself. Standard inflation carries an equivalent ~111 OOM gap between the inflaton's vacuum energy scale and the observed CC. The sole remaining structural issue in this channel is the a_0 topological obstruction — a_0 = 6440 is an integer mode count that cannot relax continuously — addressed by the zeta spectral action's projection onto the leading zeta pole. The upcoming critical gate is BBN-VOLOVIK-67, which tests that the Volovik tracking EOS satisfies |w_vac - 1/3| < 0.03 at the BBN temperature.

Importantly, the integrability-protection of §6b means that these three channels DO NOT include phonon-phonon thermalization. The GGE cannot relax into a thermal bath — the 8 Richardson-Gaudin conserved integrals forbid it. The energy flow is constrained to the weak coupling channels to external sectors (emergent gravity, Leggett DM, effacement residual), and the rate is set by those coupling strengths. This is the structural origin of the "slow" in "slow relaxation of the ringing spectrum": the natural fast decay into a thermal continuum is forbidden, and only weak external couplings are available.

The three-channel partition at z = 0 — what fraction of the total GGE energy ends up in a_2 gravitational back-reaction vs Leggett DM vs effacement residual — is a computable quantity from the 8 r_k and 8 n_k values, including the BCS zero-point contribution to the a_2 channel. The back-of-envelope calculation without the zero-point contribution gives E_a2 / E_Leggett ~ 0.08, far from the observed Omega_m / Omega_DM ~ 2.6 ratio; including the ZPE contribution brings E_a2 into range. The formal computation is the second carry-forward of this chapter (§10.2 s74_gge_partition.py).

---

## 7. Acoustic Signatures Observable Today

The chapter's structural statement is that cosmogenesis is a single-pulse parametric amplification event. This raises a concrete question: if this is what happened, what do we see, and what distinguishes it from inflation or a bounce at the level of present-day observables? The answer is four-fold: the CMB peaks are natural modes of an emergent acoustic cavity, the tilt n_s is set by fiber spectral geometry rather than by the amplifier, LSS is the interference pattern of the ringing modes, and several specific inflationary signatures are structurally forbidden — which is where falsification lives.

### 7a. CMB Acoustic Peaks as Natural Modes of the Emergent 4-Manifold

In standard LCDM, the CMB acoustic peaks are the Fourier transform of density perturbations at recombination, with the peak positions set by the sound horizon at last scattering (r_s ~ 150 Mpc in comoving units). The peak structure is a direct probe of the photon-baryon fluid's oscillation modes at the time of decoupling.

In the substrate picture, the identification is different. The emergent 4-manifold M_4 on which observations are made is an acoustic cavity whose normal modes are the eigenfrequencies of the effective wave equation on the coupled (BCS, emergent gravity) sector. The CMB acoustic peaks are the natural modes of this cavity, treated as a resonator in the emergent effective description, and their positions are set by the ratio of the cavity's characteristic length scale to the phononic wavelength. The phononic wavelength is set by the c_BA sound speed and the BCS mode frequencies, both of which are computed from the spectral triple.

The distinction from the LCDM reading is subtle and cosmologically dangerous if not stated carefully. At the level of the primary observable — the positions of the CMB acoustic peaks in multipole l — both pictures produce peaks at wavenumbers k ~ n pi / r_s for integer n, and the substrate does not currently predict a specific percent-level deviation in peak positions, widths, or amplitudes from LCDM. This is a primary-channel degeneracy: the substrate picture is not distinguished from LCDM at the TT / TE / EE peak spectrum itself. The distinguishing signatures live in (a) higher-point statistics (§7d bispectrum), (b) tensor-to-scalar inconsistency relations (§2c, §7d, §9 Gate 1), (c) branch-structure modulations on the LSS power spectrum (§7c, §9 Gate 5), and (d) the low-l asymmetric-fold signature (§9 Gate 4). The chapter does not claim a peak-level distinction from LCDM; it claims a distinction at the level of what the peaks ARE (natural modes of a persistent cavity vs. snapshots of a fluid's oscillation) and at the level of the four listed secondary channels.

S65 BISPECTRUM-65 confirms the foundation of this reading at the Bogoliubov level: the Bogoliubov transformation is a LINEAR canonical transformation and therefore produces a Gaussian squeezed vacuum, with f_NL ~ O(epsilon) ~ 0.05 for all templates rather than the slow-roll f_NL ~ -|beta|^2 ~ -1 that would be naively expected from a non-slow-roll quench. The Gaussianity of the primordial field is a positive structural prediction of the mechanism, not a coincidence.

### 7b. n_s = 0.9567 as the Slope of Fiber Spectral Geometry

The most important observational identification in the chapter is the scalar spectral tilt:

    n_s = 0.9567    [phonon_exflation_cosmology.md §8.7.9; S73A W2-A COMPOUND-NS-73a; S73A W4-D BLV-COMPOUND-73a]

This is a zero-parameter prediction. It is 1.95 sigma from the Planck value 0.9649 +/- 0.0042 and is unchanged from the bare fold calculation through the compound Bogoliubov product (W2-A) and through the BLV dispersive transfer matrix (W4-D) — both confirmed to machine precision as Bogoliubov-invariants.

The structural theorem from W4-D BLV-COMPOUND-73a PASS is decisive: the scalar spectral index is determined by the spectral action geometry (specifically the a_2 / a_4 Seeley-DeWitt ratio), which is a property of the spectral triple D_K on Jensen-deformed SU(3). It is NOT a property of the Bogoliubov transformation produced by the fold transit, and it is NOT a property of the amplifier's impulse profile. Any computation of n_s from the K-homology class of (C^infinity(SU(3)), L^2(K, S_K), D_K) produces the same value, regardless of whether the computation uses the simple ordered Bogoliubov product (W2-A), the BdG equation (W1-A), or the BLV dispersive transfer matrix (W4-D).

Concretely, the formula is

    epsilon_H = (1/2) (dS/dtau)^2 / (S * d^2 S/dtau^2)

with S_fold = 250,361, dS/dtau = 58,673, d^2 S/dtau^2 = 317,863 giving epsilon_H = 0.02163 and n_s = 1 - 2 epsilon_H = 0.9567. This is a geometric formula: the inputs are spectral action values at the fold, not quantities derived from any inflaton field or slow-roll approximation. The slow-roll notation is used by convention but the object it refers to is not a slow-roll parameter in the sense of inflation — it is a dimensionless combination of spectral moments of D_K that happens to play the role the slow-roll epsilon plays in the LCDM computation of n_s. The two match because they both come from the same mathematical structure (a ratio of first and second derivatives of a scalar function), but the underlying physics is different.

The robustness of n_s = 0.9567 against Bogoliubov-sector modifications is the framework's central observational signature of the substrate picture. Any LCDM-style inflationary model would require tuning an inflaton potential to reproduce n_s; the substrate picture gets it for free from the spectral triple's geometry. The prediction is zero-parameter because the Jensen metric is volume-preserving and has no tunable parameter beyond tau (which is itself determined by the fold location), so the spectral action and its derivatives are entirely fixed by the spectral triple. S73A W3-D [ENTROPY-FSTAR-73a] further confirms that modifications to the spectral functional f away from f_* do not move n_s toward the Planck value — they move it in the wrong direction (blue tilt), so n_s = 0.9567 is approximately the minimum-gap value within the natural family of spectral functionals.

The residual 1.95 sigma from the Planck central value is absorbable by 1-loop corrections to the spectral action. The 1-loop ratio S_1loop / S_tree ~ 0.52 [phonon_exflation_cosmology.md §8.3] is a direct estimate of the fractional size of 1-loop corrections to the spectral action itself; propagated to d^2 S / dtau^2 with an adjustment factor of order unity, the resulting shift in epsilon_H is of order 0.5 x 0.02 = 0.01, giving delta n_s ~ -0.02. The observed Planck residual is 0.9567 - 0.9649 = -0.008, well inside the 1-loop uncertainty band. S66 already began this correction path, reporting n_s = 0.9595 at 1.28 sigma after a Coleman-Weinberg correction. The full 1-loop spectral-action correction is the fifth carry-forward of this chapter (§10.5 NS-1LOOP-SPECTRAL-74).

### 7c. LSS as the Interference Pattern of GGE Ringing Modes

Large-scale structure in the substrate picture is the interference pattern produced by the superposition of the 8 Bogoliubov ringing modes, gravitationally self-organized through the a_2 channel into the observed matter distribution. This is not a mechanism radically different from structure formation in LCDM — in both pictures, an initial Gaussian density field evolves gravitationally into the observed cosmic web. The difference is in the origin of the initial field: LCDM obtains it from quantum fluctuations of the inflaton stretched by a(t), while the substrate picture obtains it from the 8-mode squeezed vacuum produced by the parametric amplification event at the fold.

Concretely, the initial density contrast delta(k) is determined by the Bogoliubov occupation numbers n_k in the squeezed vacuum. Each mode k contributes an amplitude proportional to sqrt(n_k + 1/2) to the RMS density field, with phase correlations set by the mode's r_k and the overall block-decoherence structure from the entry horizon (§5a). The spectral tilt of delta(k) is n_s = 0.9567 (§7b). Mode-mode correlations and higher-order statistics are computed from the Bogoliubov-transformed density matrix, which is a Gaussian in the mode amplitudes.

The mechanism chain from this initial field to the observed structure runs through the unconditional chain established in S35 and extended in subsequent sessions: I-1 (initial seed), RPA (linear regime), Turing (nonlinear instability), WALL (shell-crossing and virialization), BCS (pair sector dynamics). Each step in this chain is PASS-verdicted in the substrate framework, so the full chain is operational from the post-fold initial field through to the observed matter power spectrum at z = 0.

The structurally important feature is that the initial field is PHASE-COHERENT within branches (§5a). The B2, B1, and B3 branches have different compound phases (block-decoherent between branches) but within each branch the modes are phase-locked. This translates into a specific structure in the observed matter correlation function: coherent within-branch contributions interfering constructively on certain length scales (set by intra-branch mode spacings) and destructively on others. The LSS power spectrum P(k) therefore carries a signature of the branch structure of the underlying Dirac spectrum on SU(3), imprinted as specific modulations around the LCDM smooth spectrum. The amplitude of this modulation is estimable from the Bogoliubov table: with n_k^B3 / n_k^total ~ 0.73 (B3 dominates the population), n_k^B2 / n_k^total ~ 0.21, n_k^B1 / n_k^total ~ 0.06, the primary modulation is at the B3 branch spacing scale and has relative amplitude ~2-3% on top of the smooth power law. This is sharp enough to be pre-registered against Euclid's expected P(k) sensitivity of ~1% per k-bin (§9 Gate 5).

### 7d. What This Picture Forbids

A physical mechanism that does not forbid anything is not a physical mechanism — it is a rewording. The substrate's single-pulse parametric amplification picture forbids four specific observational features that standard inflationary models (and their bounce / CCC counterparts) would predict or allow. Each forbidden feature is a pre-registerable falsification gate.

1. **Slow-roll-shaped non-Gaussianity with f_NL ~ O(1)**: Slow-roll inflation predicts f_NL of order unity in specific templates (local, equilateral, folded) driven by the cubic interaction of the inflaton with itself. The substrate picture predicts f_NL ~ O(epsilon) ~ 0.05 in all templates because the Bogoliubov transformation is a LINEAR canonical map (SU(1,1)) and produces a GAUSSIAN squeezed vacuum [S65 BISPECTRUM-65 INFO(GAUSSIAN)]. The only source of non-Gaussianity is the cubic vertex in the spectral action itself, suppressed by epsilon ~ 0.02. Any detection of f_NL of order unity in slow-roll templates would be STRONG evidence against the substrate picture and in favor of a slow-roll mechanism.

2. **The r = 16 epsilon consistency relation**: The r/epsilon ratio equal to 16 (equivalently r = -8 n_T) is a specific prediction of single-field slow-roll inflation. The substrate picture has no slow-roll parameter to link r and n_s through this ratio, and furthermore the scalar and tensor sectors have independent dispersion structures (§2c). S67 ACOUSTIC-TENSOR-TRANSFER-67 establishes that r = 16 epsilon is violated by a factor ~50 in the substrate computation, and r = -8 n_T is violated by a factor ~84. The propagated CMB-scale prediction is r(CMB) = 0.0242 with |T_S|^2 = |T_T|^2 = 1 in superhorizon transfer [S68 R-CMB-TRANSFER-68]. A high-precision measurement of r_obs and n_T_obs that is consistent with the single-field slow-roll relation would be consistent with inflation and INCONSISTENT with the substrate picture.

3. **Scale-dependent f_NL with slow-roll signatures**: In slow-roll inflation, f_NL is predicted to have a specific running f_NL(k) with a specific scale dependence set by the inflaton potential's shape. The substrate picture has no running of this type, because f_NL is set by the cubic interaction in the spectral action rather than by any slow-roll hierarchy. A Planck/SKA measurement of scale-dependent f_NL consistent with a slow-roll potential would be inconsistent with the substrate.

4. **A pre-fold contracting Friedmann branch detectable as a CCC-style Weyl curvature signature at the CMB**: Bounce and CCC models predict specific imprints of the pre-bounce / previous aeon on the observed CMB (concentric temperature rings in CCC, specific polarization patterns in LQC). The substrate picture predicts NO such signature because there is no pre-fold contracting branch (§3b, §3c). Any confirmed detection of a CCC-style signature in the CMB would favor Penrose and rule out the substrate. No such signature has been detected in current Planck / BK18 data; the substrate prediction is consistent.

The four forbidden features are where falsification lives. Each is made into a formal pre-registered gate with a named experiment and numeric threshold in §9.

---

## 8. The Friedmann Replacement Program

The chapter argues that cosmogenesis is not a metric expansion and that the observed Hubble rate is the slow relaxation of a squeezed vacuum through the emergent Einstein equations. A working cosmologist needs to see the full FRW toolkit — Friedmann equation, H(z) history, flatness, transfer function, DM/DE partition — either reproduced or replaced by the substrate picture. Three items of the standard toolkit are handled structurally and require no computation: the horizon problem is absent by construction (§4e), the monopole problem is absent by construction (§3d), and the DM abundance is bracketed at the right order by S57/S66 Leggett-channel results. Five items remain and are developed below as formal reduction problems with carry-forward computational specs. These are not gaps that threaten the chapter's structural claims; they are the quantitative reduction program from substrate dynamics to the effective FRW description already in use at low energies.

### 8.1. Friedmann Equation via Direct Stress-Energy Evaluation

The emergent Einstein field equations G_{mu nu} = 8 pi G_N <T_{mu nu}>_{GGE} reduce under an FRW ansatz to the standard Friedmann equation 3 H^2 = 8 pi G_N <T_{00}>_{GGE}, where <T_{00}>_{GGE} is the 00 component of the stress-energy tensor evaluated on the 8-mode squeezed vacuum (§6c). The reduction does not involve any rate equation that references H on both sides; it is a direct substitution of the expectation value in a specified quantum state into the emergent field equations. The dimensional structure is clean and the formula is non-circular. What remains is numerical evaluation: compute <T_{00}> from the Bogoliubov table, apply the M_KK -> GeV calibration, and check that the result at z = 0 lies within a factor of 3 of Planck H_0 = 67.4 km/s/Mpc. The computation is flagged as §10.1 s74_friedmann_from_a2.py, which is the single most important next-session carry-forward because every late-time observational comparison the chapter claims is gated on this reduction producing a number.

### 8.2. Scale Factor and H(z) History

Given the non-circular Friedmann form of §8.1, the full expansion history H(z) from the pre-BBN era (z ~ 10^10) to the present (z = 0) is obtained by evaluating 3 H^2(z) = 8 pi G_N <T_{00}>_{GGE}(z) at each redshift, where <T_{00}>_{GGE}(z) tracks the slow relaxation of the GGE state through its coupling to the emergent gravity sector. The radiation-dominated era corresponds to the phase where BCS mode energies dominate <T_{00}>; matter-dominated to the phase where inter-band Leggett-channel energies dominate; Lambda-dominated to the phase where the effacement-residual channel dominates. The transition redshifts (radiation-to-matter at z_eq ~ 3400, matter-to-Lambda at z ~ 1) are determined by the relative amplitudes of the three channels, which are exactly what §8.5 computes. The H(z) computation uses the same s74_friedmann_from_a2.py script as §8.1, evaluated at the four benchmark redshifts z in {10^10, 3400, 1090, 0}.

### 8.3. Flatness

The flatness problem in LCDM is the fine-tuning of Omega_k ~ 0 to one part in 10^60 at the Planck time. In the substrate picture, the spatial curvature of the emergent 4-metric is not a tunable input — it is a specific computable function of the spectral triple on Jensen-deformed SU(3). The SU(3) internal fiber has no preferred direction in the external M^4 coordinates, so by the isotropy argument R^{(3)} cannot pick out a direction; it must be either exactly zero or a scalar depending only on the fiber's spectral moments. A first-principles computation from the Gilkey formula for a_2 on (M^4 x SU(3), g_M x g_s) with the Jensen deformation is expected to return R^{(3)} = 0 by symmetry alone, making the flatness "problem" absent by isotropy. The computation is flagged as §10.4 s74_flatness_from_a2.py; an unexpected nonzero result would be new physics.

### 8.4. Transfer Function T(k) from Fold to CMB

LCDM uses a numerical transfer function T(k), computed by CAMB or CLASS, which convolves the primordial power spectrum P_s(k) with the physics of radiation damping, acoustic oscillations, Silk damping, and free streaming between the end of inflation and recombination. The substrate picture has the primordial input (the 8-mode squeezed vacuum from §6a) and the tilt n_s = 0.9567 (§7b), but it does not currently have a transfer function from the fold to recombination. The substrate replacement for CAMB/CLASS is a mode evolution on the emergent 4-manifold's effective Klein-Gordon equation with a tau-dependent effective mass from the BCS gap profile (Delta(tau) = -0.2441 tau + 0.5118 M_KK). The computation takes as input the H(z) of §8.2, the emergent 4D sound speed from the BLV acoustic metric (c_BLV = 0.485), and the mode-by-mode equations of motion. The output is the TT/TE/EE angular power spectrum computed directly from the framework without invoking CAMB. This is a multi-session program; the immediate dependency on §8.1 (Friedmann reduction) means it is queued for the session after s74_friedmann_from_a2.py.

### 8.5. DM / DE Partition in the Expansion History

The observed present-day partition is Omega_m ~ 0.315, Omega_DM ~ 0.265, Omega_Lambda ~ 0.685, Omega_r ~ 9.2e-5. The substrate picture partitions the GGE energy across three channels (§6d): a_2 gravitational back-reaction sourcing Omega_m, Leggett inter-band phase channel sourcing Omega_DM, and effacement residual sourcing Omega_Lambda. The observational anchors are partially in place: S57 FABRIC-DM-ABUNDANCE-57 brackets Omega_DM h^2 in [0.017, 0.188] with zero free parameters, containing the observed 0.120; the S66 Leggett-only computation gives Omega_DM h^2 = 0.120 at 0.6% agreement with Planck; and DILUTION-CC-66 Scenario B gives rho_vac(today) / rho_obs = 1.032 via Volovik q-theory tracking vacuum. What remains is the quantitative partition — what fraction of the total GGE energy ends up in each channel at z = 0 — which is computable from the 8 r_k and 8 n_k values including the BCS zero-point contribution to the a_2 channel. The partition computation is the second carry-forward of this chapter (§10.2 s74_gge_partition.py) and it closes three simultaneous structural tensions: the E_a2 / E_Leggett ratio, the Omega_m mapping from the a_2 channel, and the fractional-split gate.

---

## 9. Pre-Registered Falsification Gates

The mechanism's observational content is a set of pre-registered gates that distinguish the substrate picture from (i) slow-roll inflation, (ii) Ashtekar LQC bounce, (iii) Penrose CCC, and (iv) ekpyrotic models. Each gate specifies what to measure, the expected value under each cosmogenesis picture, the experiment that can test it with current or planned sensitivity, and a pre-registered pass/fail threshold. Gates are prioritized by discriminating power: HIGH gates can sharply distinguish the substrate from inflation at current or near-term experimental sensitivity, MEDIUM gates require upcoming experiments, and LOW gates have weak discriminating power but serve as positive no-signal confirmations.

### Gate 1 — TENSOR-SLOW-ROLL-DISTINGUISH (HIGH)

**What to measure**: r (tensor-to-scalar ratio) at the CMB peak scale k = 0.002 Mpc^{-1}, and n_T (tensor spectral index) at the same scale. Test the consistency relation r = -8 n_T at 10% precision.

**Substrate prediction**: r(CMB) = 0.0242 from [S68 R-CMB-TRANSFER-68] with the BLV acoustic-tensor propagation. The consistency relation r = 16 epsilon is INAPPLICABLE (§2c). The ratio r / (16 epsilon) differs from unity by a factor ~50 [S67 ACOUSTIC-TENSOR-TRANSFER-67]; r / (-8 n_T) differs by a factor ~84.

**Slow-roll inflation prediction**: r in [0.001, 0.1] for common single-field models; r = -8 n_T satisfied to <1%.

**Ashtekar LQC bounce prediction**: r ~ 0.01 for standard LQC parameters with modifications to n_T from the bounce dispersion.

**Penrose CCC prediction**: No specific r; rough expectation r < 0.01 with n_T ~ 0.

**Experiment**: LiteBIRD (launch ~2032, sigma(r) ~ 0.001) and CMB-S4 (first light 2028-2030, sigma(r) ~ 0.001). Both instruments can test r > 10^{-5} at 5 sigma.

**Pre-registration**: PASS if r is measured consistent with 0.0242 (24-sigma LiteBIRD detection, 8-sigma CMB-S4 detection). EXCLUDE substrate if r > 10^{-5} is measured with r = -8 n_T satisfied to 10%.

### Gate 2 — F_NL-GAUSSIAN-DISTINGUISH (LOW discriminating power against slow-roll, HIGH against ekpyrotic)

**What to measure**: Primordial non-Gaussianity parameter f_NL in the local, equilateral, and folded templates.

**Substrate prediction**: f_NL ~ O(epsilon) ~ 0.05 in all templates, exactly Gaussian at lowest order because the Bogoliubov transformation is SU(1,1)-linear and produces a Gaussian squeezed vacuum [S65 BISPECTRUM-65 INFO(GAUSSIAN)]. Non-Gaussianity arises only from the cubic vertex in the spectral action, suppressed by epsilon ~ 0.02.

**Slow-roll inflation prediction**: f_NL ~ epsilon ~ 0.01 in local template (Maldacena 2003 single-field consistency); equilateral f_NL can reach O(100) in DBI or small-c_s models.

**Ashtekar LQC bounce prediction**: Non-trivial f_NL from the bounce surface; O(1) in local template with oscillatory features.

**Penrose CCC prediction**: Specific large-scale non-Gaussianity from aeon matching.

**Ekpyrotic prediction**: f_NL ~ -100 in local template.

**Experiment**: Planck current best f_NL^local = -0.9 +/- 5.1; SKA + Euclid + LSST joint projection sigma(f_NL^local) ~ 1 by 2030.

**Pre-registration**: PASS (no signal) consistent with substrate. Detection of |f_NL^local| > 5 at 3-sigma excludes substrate and slow-roll in favor of ekpyrotic or bounce.

### Gate 3 — CCC-WEYL-CIRCLE-DISTINGUISH (LOW)

**What to measure**: Concentric temperature fluctuation rings in the CMB — the Penrose-Gurzadyan signature of aeon matching.

**Substrate prediction**: NONE — no pre-fold aeon, no conformal matching surface.

**Slow-roll inflation prediction**: NONE — CMB is smoothed by inflation.

**Ashtekar LQC bounce prediction**: NONE in CCC sense; LQC predicts specific low-multipole power deficit.

**Penrose CCC prediction**: Concentric ring structure with temperature contrasts of order 10 microK over angular diameters ~5 degrees.

**Experiment**: Current Planck data inconsistent with Penrose-Gurzadyan 2010; subsequent analyses disputed. CMB-S4 will definitively settle the question.

**Pre-registration**: PASS (no rings) consistent with substrate but not uniquely diagnostic.

### Gate 4 — BOUNCE-SYMMETRY-DISTINGUISH (MEDIUM)

**What to measure**: Low-multipole (l < 30) CMB TT/EE anomalies, specifically the power deficit at large angular scales and the tensor mode structure below the reionization bump.

**Substrate prediction**: Asymmetric fold (§3a: Mach 20.7 no turnaround, entry horizon n_bar = 85.2, open exit) predicts a three-branch block-decoherence signature at low l from the entry-horizon thermal population amplifying the inter-branch compound phase split. The B1/B2/B3 branches contribute incoherently (block-decoherence C(B2, B3) = 2.3e-6 while intra-branch variance is 3.6e-8 and 8.5e-8), and with B3 dominance the net low-l suppression at l ~ 10 is in the few-percent range.

**Slow-roll inflation prediction**: Smooth power at low l consistent with scale-invariant initial conditions.

**Ashtekar LQC bounce prediction**: Suppression of TT power at l < 20, time-symmetric around the bounce; C_l^TT / C_l^LCDM ~ 0.8 at l = 10 for standard LQC parameters [Agullo-Morris 2015].

**Ekpyrotic prediction**: Specific low-l asymmetry from the contracting phase.

**Experiment**: Planck TT/TE/EE at low l already cosmic-variance limited.

**Pre-registration**: Requires completion of the ASYMMETRIC-FOLD-LOW-L-74 carry-forward to compute the substrate's quantitative C_l prediction. PASS if substrate C_l^TT / C_l^LCDM at l ~ 10 differs from LCDM by > 2-sigma of Planck precision and the deviation matches the measured anomaly. FAIL if the substrate prediction is within 2-sigma of LCDM (insufficient distinguishing power).

### Gate 5 — PHASE-COHERENT-PRIMORDIAL-SIGNATURE (HIGH)

**What to measure**: Specific modulations on top of the smooth LSS power spectrum P(k) at k ~ 0.01 - 0.1 h/Mpc, corresponding to the branch structure of the 8-mode squeezed vacuum (§7c).

**Substrate prediction**: Three overlapping "combs" of oscillations in P(k), with amplitude set by n_k per mode and phase set by r_k per mode. With B3 dominance (n_k^B3 / n_k^total ~ 0.73), the primary modulation is at the B3 branch spacing scale with relative amplitude 2-3% on top of the smooth n_s = 0.9567 power law. This is SHARP enough to be pre-registered against Euclid (sigma(P)/P ~ 1% per bin).

**Slow-roll inflation prediction**: Smooth power law with no modulation features at these scales.

**Bounce/CCC predictions**: Model-dependent; no branch-structure combs.

**Experiment**: Euclid galaxy power spectrum at k = 0.01-0.3 h/Mpc (sigma(P)/P ~ 1-3% per bin); LSST galaxy clustering at similar precision; DESI DR3 BAO at k ~ 0.1 h/Mpc.

**Pre-registration**: PASS if Euclid detects a ~2-3% modulation at the predicted k values; EXCLUDE substrate if P(k) is smooth to 1% per bin across the relevant k range. This is a positive detection gate for the framework.

### Gate 6 — GGE-ENERGY-PARTITION-GATE (HIGH)

**What to measure**: Consistency of the observed Omega_m / Omega_DM / Omega_Lambda partition with the three-channel GGE fractional split (§6d, §8.5).

**Substrate prediction**: The S66 Leggett-only result Omega_DM h^2 = 0.120 at 0.6% agreement with Planck establishes the Leggett channel sourcing Omega_DM. The a_2 channel (primary spectral moment) should source Omega_m; the effacement residual sources Omega_Lambda through Volovik tracking at rho_vac(today)/rho_obs = 1.032. Quantitative split requires the ZPE-inclusive partition computation (§10.2).

**Slow-roll inflation prediction**: NO NATURAL partition — Omega_m, Omega_DM, Omega_Lambda are independent parameters.

**Experiment**: Planck + DESI + SN Ia + weak lensing joint constraints give Omega_m, Omega_b, Omega_Lambda to sub-percent precision; DESI DR3 improves w_0, w_a constraints.

**Pre-registration**: After s74_gge_partition.py completes: PASS if all three channels match observation within factor 2; FAIL if any channel is off by > factor 10; INFO if consistent with S66 but outside factor-2 bracket on the a_2 channel. This is a fractional-split test of the Volovik tracking vacuum mechanism, not a CC-gap-closure test (the 114 OOM is exflation itself, §6d).

### Gate 7 — LEGGETT-VELOCITY-LSS-SIGNATURE (MEDIUM)

**What to measure**: Scale-dependent deviation of the linear growth factor D(a) from the LCDM prediction, at scales where the Leggett-channel sound speed determines the DM fluid's sound horizon.

**Substrate prediction**: In LCDM, DM is pressureless (c_DM = 0), giving the standard growth factor D(a) ~ a during matter domination. In the substrate, the Leggett-channel DM has a nonzero sound speed c_L = 0.025 M_KK [S64 four-speed hierarchy], with the Leggett Jeans scale k_J ~ a H / c_L separating pressure-supported scales (k > k_J, suppressed growth) from free-fall scales (k < k_J, standard growth). The ratio c_L / c_BA = 0.048 - 0.080 [S56, S69 FOUR-SPEED-3HE-69] places k_J well below typical LSS scales, so the signature is subtle.

**Experiment**: Euclid + DESI joint constraint on D(a) at z ~ 1 (sigma(D) ~ 0.01); LSST galaxy clustering at z = 0.3 - 2.5.

**Pre-registration**: PASS (consistent with LCDM CDM) if predicted delta D(a) / D_LCDM < 0.01 at Euclid scales — the substrate DM is observationally indistinguishable from CDM at current precision. INFO if 0.01 - 0.05. FAIL if > 0.05 (substrate DM tension with Euclid). Requires LEGGETT-JEANS-74 carry-forward to compute the 4D k_J.

### Gate 8 — BCS-GAP-IMPRINT-ON-LSS (MEDIUM)

**What to measure**: Specific oscillatory feature in the matter power spectrum P(k) at a wavenumber k_BCS set by the BCS gap profile's characteristic length 1 / Delta(tau_fold) ~ 10 M_KK^{-1}, mapped to 4D via the emergent sound horizon.

**Substrate prediction**: The BCS gap defines a characteristic internal length scale that, when propagated to the emergent 4D power spectrum through the transfer function, imprints a specific oscillation at k_BCS. This is distinct from Gate 5's branch-structure comb because it is a single feature at one k value, not a multi-mode envelope.

**Experiment**: Euclid / LSST / DESI BAO-scale measurements, sigma(P)/P ~ 1-3% per bin.

**Pre-registration**: After BCS-GAP-K-SCALE-74 carry-forward computes k_BCS in h/Mpc from the Delta(tau_fold) fit. PASS if k_BCS falls inside Euclid's accessible window [0.01, 0.3] h/Mpc AND a feature is detected there; INFO if k_BCS falls outside the window (exists but not currently observable); FAIL if k_BCS is inside the window but no feature is detected at the predicted amplitude.

---

## 10. Carry-Forward Computations

The chapter establishes the mechanism and identifies the structural closures. The quantitative reduction to observable FRW cosmology lives in five top-priority computation computations prioritized by EVOI (Expected Value of Information). Each entry specifies what is computed, the input data required, the pre-registered gate it feeds, and the effort estimate.

### 10.1 s74_friedmann_from_a2.py — HIGHEST EVOI

**What is computed**: H(z = 0) in km/s/Mpc and H(z) at the benchmark redshifts z in {10^10, 3400, 1090, 0}, via the non-circular form 3 H^2 = 8 pi G_N <T_{00}>_{GGE}(z), evaluated directly on the 8-mode squeezed vacuum state using the (n_k, r_k, omega_k) values from S73A W1-A. G_N is fixed by the a_2 f_2 combination of §2a; the GGE-to-matter conversion f_conv is scanned over [0.1, 10] to test sensitivity to Mack's §5.9 GGE-to-matter mapping ambiguity.

**Data needed**: (a) 8-mode Bogoliubov table from S73A W1-A (r_k, n_k, omega_k); (b) M_KK -> GeV calibration M_KK = 7.43 x 10^16 GeV from Phononic-to-Cosmos.md Convention Translation Table; (c) a_2 / a_0 = (5/12) R from phonon_exflation_cosmology.md §12.1; (d) BCS gap profile Delta(tau) = -0.2441 tau + 0.5118 M_KK from S73A W4-E JJ-KAPPA-MAP-73a for the tau dependence of mode energies.

**Gate fed**: H(z = 0) within a factor of 3 of Planck H_0 = 67.4 km/s/Mpc for f_conv in [0.3, 3]. PASS if natural f_conv gives H_0 within factor 3. FAIL if no f_conv in [10^{-3}, 10^3] produces H_0 within factor 10. INFO if f_conv is unconstrained (implies hidden free parameter). Also gates the transition-redshift check for §8.2 (z_eq, z_recomb within factor 3).

**Effort**: One session. The script is a direct substitution of the Bogoliubov table into the emergent Einstein equation with a scan over f_conv. This computation is the single most important carry-forward because every late-time observational comparison the chapter claims is gated on it.

### 10.2 s74_gge_partition.py — HIGH EVOI

**What is computed**: Partition (E_a2, E_Leggett, E_effacement) as a fraction of total GGE energy, including the BCS zero-point contribution to E_a2 (omitted from back-of-envelope estimates). Ratios E_a2 / E_Leggett and E_a2 / E_total to test against observed Omega_m / Omega_DM ~ 2.6 and Omega_m / Omega_total ~ 0.315.

**Data needed**: (a) 8-mode Bogoliubov table from S73A W1-A; (b) inter-branch phase split 0.552 rad from S73A W3-A for the Leggett channel; (c) effacement residual coefficient 3e-4 from the phononic-framing rule; (d) S66 Leggett-only Omega_DM h^2 = 0.120 for cross-check; (e) S57 Lambda_eff = +1.709 M_KK for total GGE energy.

**Gate fed**: §9 Gate 6 GGE-ENERGY-PARTITION. PASS if all three channels match observation within factor 2; FAIL if any channel is off by > factor 10; INFO if consistent with S66 but outside the factor-2 bracket on the a_2 channel.

**Effort**: One session. The ZPE inclusion is the main technical move; the three channel computations are decoupled and parallelizable.

### 10.3 A_S-FROM-BOGOLIUBOV-74 — HIGH EVOI (largest observational tension)

**What is computed**: Primordial scalar amplitude A_s in the emergent 4D power spectrum, starting from the 8-mode squeezed vacuum of S73A W1-A and applying the Peter-Weyl sector filter [S65 AB-AS-65], the emergent sound horizon through c_BLV = 0.485, and any subhorizon dilution. Target is to close the currently 3.15 OOM gap between the framework's baseline A_s prediction and Planck 2.1 x 10^{-9}, or identify which ingredient must change.

**Data needed**: (a) 8-mode Bogoliubov table from S73A W1-A; (b) PW sector filter rules from S65; (c) BLV acoustic metric c_BLV = 0.485 from S64; (d) M_KK -> GeV calibration; (e) S64/S66 A_s gap baseline = 3.15 OOM for comparison.

**Gate fed**: A_s within a factor 10 of Planck 2.1 x 10^{-9}. PASS if computed A_s is within 1 OOM (effectively closing 2+ OOM from the current baseline). INFO if between 1 and 2 OOM (partial closure). FAIL if > 2 OOM residual — informative because it establishes that the chapter's single largest observational tension is not resolved at the Bogoliubov-amplitude level alone and requires an additional structural mechanism.

**Effort**: One session, possibly two if the PW sector filter interpretation is ambiguous. The risk that no combination of current ingredients closes the gap is itself informative.

### 10.4 s74_flatness_from_a2.py — MEDIUM EVOI

**What is computed**: Spatial curvature R^{(3)} of the emergent 4-metric from the a_2 Seeley-DeWitt coefficient on (M^4 x SU(3), g_M x g_s) with the Jensen deformation. Expected output: R^{(3)} = 0 by the isotropy of the SU(3) internal fiber.

**Data needed**: (a) Jensen-deformed SU(3) metric at tau = tau_fold; (b) Gilkey formula for a_2 on a 12-dimensional spectral triple; (c) M^4 ansatz g_M = -dt^2 + a(t)^2 (dr^2 / (1 - k r^2) + r^2 d Omega^2).

**Gate fed**: |Omega_k| < 0.005 (Planck 2018 bound). PASS if |Omega_k| < 10^{-5}. INFO if 10^{-5} < |Omega_k| < 10^{-3}. FAIL if |Omega_k| > 10^{-3}.

**Effort**: One session. Pure geometric calculation using existing Gilkey machinery and the block-diagonal theorem (S22b).

### 10.5 NS-1LOOP-SPECTRAL-74 — MEDIUM-HIGH EVOI

**What is computed**: 1-loop correction to d^2 S / dtau^2 at the fold, and the resulting delta n_s. Tree-level n_s = 0.9567 is Bogoliubov-invariant and known to machine precision; the 1-loop shift is expected at size delta n_s ~ 0.02 > residual 0.008, which would bring the prediction within 1-sigma of Planck 0.9649.

**Data needed**: (a) tree-level S(tau), dS/dtau, d^2 S/dtau^2 values at tau_fold from phonon_exflation_cosmology.md §8.7.9; (b) 1-loop ratio S_1loop / S_tree ~ 0.52 from phonon_exflation_cosmology.md §8.3; (c) Coleman-Weinberg correction from S66 (which gave n_s = 0.9595 at 1.28 sigma).

**Gate fed**: n_s within Planck 1-sigma (0.9607 to 0.9691). PASS if 1-loop corrected n_s lands in this interval. INFO if within 2-sigma (0.9565 to 0.9733) but outside 1-sigma. FAIL if 1-loop correction moves n_s away from Planck or leaves it more than 2-sigma away.

**Effort**: One session. The Coleman-Weinberg computation is reusable from S66; the new step is the spectral-action 1-loop contribution to d^2 S / dtau^2 specifically at the fold.

### Deferred (queued for subsequent sessions)

- **s75_transfer_function.py** (§8.4) — depends on §10.1 completion; one session after s74_friedmann_from_a2.py.
- **BRANCH-COMB-AMPLITUDE-74** (Gate 5 sharpening) — depends on s75_transfer_function.py; two sessions out.
- **ASYMMETRIC-FOLD-LOW-L-74** (Gate 4 sharpening) — depends on s75_transfer_function.py; two sessions out.
- **LEGGETT-JEANS-74** (Gate 7) — independent, can be queued anytime.
- **BCS-GAP-K-SCALE-74** (Gate 8) — independent, can be queued anytime.

---

## Closing

Write s74_friedmann_from_a2.py next — every observational comparison the chapter makes at late times is gated on the explicit reduction 3 H^2 = 8 pi G_N <T_{00}>_{GGE} becoming a number, and the chapter's credibility as a drop-in cosmogenesis mechanism rides on whether the natural range of f_conv lands H_0 within a factor of 3 of 67 km/s/Mpc.
