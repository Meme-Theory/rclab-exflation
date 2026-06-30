# CC Path A: The Jacobson Route

## Lambda as Integration Constant in Emergent Einstein Equations

**Author**: Einstein-Theorist
**Date**: 2026-04-01
**Classification**: GEOMETRIC (emergent spacetime structure)
**Status**: OPEN (structurally) -- but physically empty without a selection principle

---

## 0. Summary

The Jacobson route treats the cosmological constant not as a quantity computed from the spectral action, but as an undetermined integration constant in the emergent Einstein equations. The derivation chain runs: spectral action on the fiber D_K --> vacuum entanglement entropy proportional to area --> Clausius relation dQ = T dS at local Rindler horizons --> Einstein field equations with Lambda free. The 9 CC closures (S19-S63) are all closures of *mechanisms to determine Lambda from spectral data*. The integration constant itself remains unconstrained.

This document analyzes whether this constitutes a genuine resolution path or a reformulation of the CC problem. The assessment: the Jacobson route is formally the strongest surviving CC path *because* it does not attempt to compute Lambda dynamically -- but this same feature means it provides no *explanation* for why Lambda takes its observed value. It survives by evasion, not by construction. The question "what determines Lambda?" remains the central open problem.

---

## I. The Mechanism in Detail

### I.1. Principle-Theoretic Starting Point

The Jacobson derivation (Jacobson 1995; framework computation JACOBSON-GGE-63, S63 W3-03) is a *principle theory* in the sense I distinguished in 1919: it derives the form of the gravitational field equations from two high-level empirical generalizations -- the proportionality of entropy to area (Bekenstein-Hawking) and the first law of thermodynamics (Clausius relation) -- without any constructive hypothesis about the microscopic degrees of freedom.

This is the deepest sense in which the derivation is powerful. One does not need to know *what* the substrate is made of. One needs only:

(a) A well-defined energy-momentum tensor T_ab for the matter content
(b) Vacuum entanglement entropy proportional to horizon area: S_vac = eta * A
(c) A kinematic Unruh temperature T_U = hbar kappa / (2 pi)
(d) Energy-momentum conservation: nabla^a T_ab = 0

All four hold in the phonon-exflation framework. The critical point is requirement (b): Jacobson uses the *vacuum* entanglement entropy, not the matter-state entropy. The GGE relic has S_matter = 0 (product state in the Bogoliubov basis), but S_vac is nonzero and proportional to area from UV correlations of the BCS vacuum. This distinction was the source of the S62 error (corrected in JACOBSON-GGE-63).

### I.2. The Seven-Step Derivation Chain

I state the derivation as it applies specifically to the substrate with GGE matter, following the JACOBSON-GGE-63 analysis.

**Step 1. Local Rindler horizon construction.**

At every spacetime point p of the emergent 4D manifold M^4, construct a local Rindler horizon from a spacelike 2-surface P whose past-directed null normal congruence has vanishing expansion and shear at p. This is a *purely geometric* construction -- it depends only on the emergent metric g_ab, not on the matter content. The GGE state does not affect the existence or properties of local Rindler horizons.

**Step 2. Unruh temperature.**

The Unruh temperature T_U = hbar kappa / (2 pi) is a kinematic quantity determined by the observer's proper acceleration a (equivalently, the surface gravity kappa of the Rindler horizon). It is independent of the matter state. An accelerated observer perceives T_U regardless of whether the matter is in a Planck distribution, a GGE state, or the pure vacuum. In the substrate, this temperature is the fabric's spectral response to a non-inertial measurement pattern (Hawking E2, S63 workshop).

**Step 3. Heat flux across the horizon.**

The energy flux across the local Rindler horizon is:

    delta Q = - kappa integral_H lambda T_ab^{GGE} k^a k^b d lambda dA     (A1)

where k^a is the null generator of the horizon and lambda is the affine parameter. The energy-momentum tensor T_ab^{GGE} = <GGE | T-hat_ab | GGE> is well-defined for any quantum state. For the GGE density matrix rho_GGE = Z^{-1} exp(- sum_k beta_k I_k), the conservation law nabla^a T_ab^{GGE} = 0 holds because [H, I_k] = 0 for all Richardson-Gaudin charges I_k.

Computed values (from s62_meissner_gge.npz, s62_cc_qtheory_gge.npz):
- T_00^{GGE} = 81,493.88 M_KK^4 (total: ZP + BCS)
- rho_modes = 0.8198 M_KK^4 (BCS quasiparticle contribution)
- Mode-by-mode deviations from Planck: up to 7,381x for mode k = 5

**Step 4. Area variation via Raychaudhuri equation.**

The Raychaudhuri equation

    d theta / d lambda = - (1/2) theta^2 - sigma^2 - R_ab k^a k^b     (A2)

is a *purely geometric identity* relating the expansion theta of null geodesics to the Ricci tensor. At the local equilibrium point (theta = sigma = 0), the area variation is:

    delta A = - integral_H lambda R_ab k^a k^b d lambda dA     (A3)

No assumption about the matter content or its thermal properties enters this step. This is the Raychaudhuri equation -- it is geometry, not thermodynamics.

**Step 5. Entropy-area proportionality: dS = eta delta A.**

This is the critical step where the S62 analysis went wrong. Two distinct entropy concepts operate:

| Entropy | Definition | GGE value | Jacobson uses? |
|:--------|:-----------|:----------|:---------------|
| S_matter | von Neumann entropy of matter state | = 0 (GGE product state) | NO |
| S_vac | Entanglement entropy of vacuum across Rindler cut | = eta * A (nonzero) | YES |

The Bombelli-Koul-Lee-Sorkin (1986) / Srednicki (1993) result: the entanglement entropy of the quantum vacuum across any spatial surface scales as

    S_vac = c_UV A / epsilon^2 + subleading     (A4)

where epsilon is the UV cutoff. The BCS vacuum |0_BCS> has UV entanglement from the continuum, independent of the GGE excitations above it. The GGE modifications are perturbative corrections:

    delta S_GGE / S_vac ~ sum_{k>0} n_k^{GGE} omega_k^2 ~ 7.8 x 10^{-3}     (A5)

Less than 1% correction. The proportionality S = eta * A holds at leading order.

In the product geometry M^4 x SU(3), the entanglement entropy across the Rindler horizon decomposes (Hawking E2):

    S_Rindler = S_base + S_fiber + S_cross     (A6)

The base-space contribution S_base ~ A/(4G) ~ 10^7 nats dominates over S_fiber = 0.728 nats (W3-01) by 7 OOM. The fiber correction to the emergent equations is:

    delta Lambda / Lambda ~ S_fiber / S_base ~ 3 x 10^{-7}     (A7)

This is negligible. The Jacobson derivation operates on the *base-space* entanglement, not the fiber entanglement.

**Step 6. Clausius relation delta Q = T_U dS.**

Combining Steps 3 and 5:

    - kappa int lambda T_ab^{GGE} k^a k^b d lambda dA = (hbar kappa / (2 pi)) eta (- int lambda R_ab k^a k^b d lambda dA)     (A8)

The surface gravity kappa cancels (as in the thermal case -- this is the key). We obtain:

    T_ab^{GGE} k^a k^b = (hbar eta / (2 pi)) R_ab k^a k^b     for all null k^a     (A9)

This is the same equation as in the thermal case, with T_ab^{GGE} replacing T_ab^{thermal}.

**Step 7. Einstein equations via the contracted Bianchi identity.**

Equation (A9) holding for all null k^a implies:

    T_ab^{GGE} = (hbar eta / (2 pi)) (R_ab + f g_ab)     (A10)

for some scalar function f(x). Now energy-momentum conservation nabla^a T_ab^{GGE} = 0 combined with the contracted Bianchi identity nabla^a G_ab = 0 constrains f:

    nabla^a [(hbar eta / (2 pi))(R_ab + f g_ab) - (hbar eta / (2 pi)) G_ab] = 0     (A11)
    nabla^a [f g_ab + R_ab - G_ab] = 0     (A12)
    nabla^a [(f + R/2) g_ab] = 0     (A13)
    nabla_b (f + R/2) = 0     (A14)

Therefore f = -R/2 + Lambda, where Lambda is an **integration constant** -- spatially constant by equation (A14), but *not fixed by the derivation*. Substituting back:

    R_ab - (1/2) R g_ab + Lambda g_ab = (2 pi / (hbar eta)) T_ab^{GGE} = 8 pi G T_ab^{GGE}     (A15)

with G = (4 hbar eta)^{-1} and **Lambda undetermined**.

### I.3. Where Lambda Enters: The Bianchi Identity Gives a Constant, Not a Value

The structural point deserves emphasis. In the standard derivation of Einstein's equations from the Einstein-Hilbert action, Lambda appears as an explicit coupling constant in the Lagrangian. Its value is an *input*. In the Jacobson derivation, Lambda appears as an *output* of the integration procedure -- the arbitrary constant that arises when one solves nabla_b(f + R/2) = 0. The Bianchi identity constrains the *gradient* of (f + R/2) to vanish; it does not constrain the *value*.

This is structurally identical to the appearance of an integration constant when solving a first-order ODE. The equation dy/dx = g(x) has solution y = integral g(x) dx + C, and C is fixed by boundary conditions, not by the equation. The Bianchi identity is the "equation"; Lambda is the "C"; and the CC problem is the question of what boundary condition fixes C.

### I.4. The Full Derivation Chain: Spectral Action to Emergent Einstein Equations

The substrate framework provides a specific realization:

    D_K(tau) eigenvalues  -->  S(tau) = Tr f(D_K^2 / Lambda_sp^2)     [spectral action, CC-1]
        |
        v
    a_0 = 6440 M_KK^{d-4}     [vacuum energy, zeroth SDW moment]
    a_2 = 2776 M_KK^{d-6}     [Einstein-Hilbert, second SDW moment]
    a_4 = 1351 M_KK^{d-8}     [Yang-Mills, fourth SDW moment]
        |
        v
    G_N = 1 / (16 pi a_2 M_KK^2)     [Newton's constant from a_2]
        |
        v
    Vacuum entanglement: S_vac = eta * A, with eta = 1/(4 hbar G_N)     [area law from UV modes]
        |
        v
    Jacobson derivation (Steps 1-7): dQ = T dS --> G_ab + Lambda g_ab = 8 pi G T_ab^{GGE}
        |
        v
    Lambda = UNDETERMINED integration constant

The spectral action determines G_N through a_2 and the gauge couplings through a_4. It provides a *candidate* value for the vacuum energy through a_0. But the Jacobson derivation does not use a_0 directly -- it uses the *entanglement entropy*, which is determined by G_N (through the Bekenstein-Hawking relation eta = 1/(4G)), not by a_0. The a_0 moment of the spectral action is decoupled from the Jacobson derivation.

This is the structural heart of Path A: the spectral action's zeroth moment a_0 (which generates the 114-OOM vacuum energy) is *not the quantity that appears in the emergent Einstein equations*. What appears is an integration constant Lambda that is formally independent of a_0.

---

## II. What Determines Lambda?

### II.1. Five Candidate Principles

If Lambda is an integration constant, something must fix it. In standard GR, it is simply a free parameter -- the lowest-energy coupling constant, measured but not predicted. In the substrate framework, there are five candidate principles that *could* determine Lambda.

**Principle 1: Spectral action zeroth moment.** The spectral action's a_0 Lambda_sp^4 term is the vacuum energy density. If this is the physical Lambda, then Lambda ~ 10^{118} Lambda_obs. This is the *default* assumption that generates the CC problem. The Jacobson route's value lies in the possibility that this default is wrong -- that the vacuum energy density and the gravitational Lambda are *different* quantities.

**Principle 2: Volovik equilibrium theorem.** At true thermodynamic equilibrium (large N, Gibbs state, heat bath coupling), the Gibbs-Duhem relation forces Lambda_eq = 0 (Volovik Paper 04, Paper 13). But the GGE is not at Gibbs equilibrium. The R-G integrability locks the system in a constrained equilibrium with Lambda_GGE = 0.838 M_KK^4 (CC-QTHEORY-GGE-62). This principle determines a *nonzero* Lambda that is 114 OOM too large.

**Principle 3: Nonlocal spectral action.** The spectral action Tr f(D_K^2 / Lambda_sp^2) is an intrinsically nonlocal object -- it depends on the full spectrum of D_K, not on a local Lagrangian density. The Capozziello-Mazumdar-Meluccio result (Paper 09) shows that nonlocal theories evade the Weinberg no-go theorem: the IDG recurrence phi_n = Box^{-1} phi_{n-1} prevents independent variation of the auxiliary fields, blocking the proof. The spectral action has precisely this structure -- the eigenvalue spectrum of D_K encodes infinitely many coupled "fields" (the Peter-Weyl modes) that cannot be varied independently. If the nonlocal spectral action determines Lambda through a mechanism that exploits this coupling, the Weinberg no-go is evaded.

**Status**: Structurally suggestive but computationally empty. No computation has determined what value of Lambda the nonlocal spectral action selects. The meta-analysis (S43) identified spectral action nonlocality as a potential mechanism for Weinberg no-go evasion -- but potential is not proof.

**Principle 4: Boundary condition.** Lambda is fixed by a cosmological boundary condition -- the initial state of the fabric's transit through the fold. In the no-boundary proposal (Hartle-Hawking 1983), the initial state is selected by summing over compact Euclidean geometries. In the substrate, the spectral action IS a Euclidean path integral over the compact internal space SU(3). The transit through the fold selects a specific value of Lambda through the initial conditions.

**Status**: Formally well-motivated but faces the measure problem (how to weight different initial conditions) and the predictivity problem (which compact geometries to sum over).

**Principle 5: Running vacuum model (RVM).** The Sola-Peracaula running vacuum approach (Paper 07, Paper 08) endows Lambda with cosmic dynamics: rho_vac(H) = rho_vac^0 + (3 nu_eff / (8 pi G_N)) (H^2 - H_0^2). The running parameter nu_eff ~ 10^{-5} to 10^{-3} is set by the mass spectrum. In the substrate framework, the spectral action IS the functional that runs -- the Seeley-DeWitt coefficients a_0(tau), a_2(tau), a_4(tau) are tau-dependent, and tau tracks the cosmic evolution. However, a_0 is tau-independent by Theorem T14 (volume-preserving Jensen deformation), so the RVM running must come from a_2 and a_4 terms. These are subdominant to a_0 by powers of Lambda_sp^{-2}.

**Status**: The RVM mechanism is real (QFT in curved spacetime), but the tau-independence of a_0 blocks the dominant term from running. The surviving running is from a_2 and a_4 terms, which are Lambda_sp^2 / Lambda_sp^4 = Lambda_sp^{-2} suppressed relative to the dominant vacuum energy. For M_KK-scale cutoff, this suppression is negligible.

### II.2. The Structural Gap: Why No Principle Works Yet

The five candidate principles share a common structural difficulty. Each attempts to determine Lambda from within the substrate framework -- from the spectral action (Principles 1, 3, 5), from thermodynamics (Principle 2), or from initial conditions (Principle 4). But the Jacobson derivation shows that the emergent Einstein equations are *structurally independent* of the microscopic details, beyond the requirements (a)-(d). The very power of the derivation -- its independence from constructive hypotheses -- is also its weakness: it provides no mechanism to connect Lambda to the spectral data.

The Gedankenexperiment that reveals the gap: consider two substrate configurations with identical emergent metrics g_ab but different fiber Dirac operators D_K and D_K'. Both generate the same Jacobson derivation (same Rindler horizons, same Unruh temperature, same area law). Both produce the same Einstein equations with the same undetermined Lambda. The derivation cannot distinguish them -- Lambda is the same integration constant in both cases. Yet the spectral actions S(D_K) and S(D_K') may differ enormously (different a_0 values). If Lambda is determined by the spectral action, two different substrates with the same emergent metric would have different Lambda -- but the Jacobson derivation says Lambda is fixed by the metric alone (through the Bianchi identity).

This tension suggests that either:
(i) Lambda is genuinely not determined by the spectral action (it is a free parameter of the emergent theory, not derivable from the substrate), or
(ii) The Jacobson derivation is incomplete -- there is additional structure beyond the Clausius relation that connects Lambda to the spectral data.

Option (i) is the standard GR position. Option (ii) would require extending the Jacobson derivation to include information beyond the first law. Both are open.

---

## III. Interaction with the 9 Closures

### III.1. Why the Jacobson Route Survives the Closures

The 9 CC closures (framework-cc-oom.md, Section II) are:

| # | Mechanism | What it eliminates |
|:--|:----------|:-------------------|
| 1 | Perturbative Exhaustion | All monotone spectral functionals as CC stabilizers |
| 2 | A-tensor cross-terms | Base-fiber vacuum energy cancellation |
| 3 | Density-density | Inter-sector Hartree contributions |
| 4 | Anisotropic Josephson | Integrability-breaking via pair transfer |
| 5 | Beliaev damping | Three-phonon spectral weight redistribution |
| 6 | Landau damping | Phonon-quasiparticle thermalization |
| 7 | Fabric vacuum pressure | Josephson condensation energy modification |
| 8 | GGE monotonicity | Q-theory self-tuning on GGE |
| 9 | B-F shared-spectrum | Boson-fermion cancellation with same D_K |

Every one of these closures eliminates a *dynamical mechanism* -- a process that would compute Lambda from the spectral data and make it small. The Jacobson route survives because it is *not a dynamical mechanism*. It does not claim to compute Lambda. It merely observes that the emergent Einstein equations contain an integration constant that is not fixed by the derivation.

The closures are structurally orthogonal to the Jacobson route. They constrain the space of *constructive theories* (specific mechanisms for Lambda). The Jacobson route is a *principle theory* (the form of the equations constrains Lambda to be constant, but does not determine its value). The closures narrow the constructive space without touching the principle-theoretic observation.

### III.2. Is This a Strength or a Weakness?

This is both the route's greatest strength and its greatest weakness.

**Strength.** The Jacobson route is unfalsifiable by any closure of a specific mechanism. No matter how many dynamical routes are eliminated, the integration constant remains. It is a permanent feature of the emergent equations. One cannot "close" the Jacobson route -- one can only determine what fixes the constant.

**Weakness.** The Jacobson route has zero predictive content. It says Lambda is free. It does not predict Lambda = 10^{-122} M_Pl^4 or Lambda = 0 or any other value. Every value is consistent with the route. A "path" that is consistent with all possible observations is not a physical theory -- it is a tautology.

The precise structural diagnosis: the Jacobson route is a **necessary condition** (Lambda must be an integration constant in the emergent equations) but not a **sufficient condition** for a CC resolution. Any CC resolution must be *consistent* with the Jacobson framework (the emergent equations must have the form G_ab + Lambda g_ab = 8 pi G T_ab^{GGE}), but the resolution itself must come from outside the Jacobson derivation -- from whatever principle fixes the integration constant.

### III.3. What the Closures DO Imply for Path A

Although the closures do not directly constrain the Jacobson route, they have a powerful *indirect* implication. All 9 closures share a single structural root: the Richardson-Gaudin integrability of the BCS pair Hamiltonian on the D_K spectrum (framework-cc-oom.md, Section II conclusion). The CC problem IS the integrability problem. This means:

**Any principle that determines the Jacobson integration constant must be compatible with Richardson-Gaudin integrability.**

This is a real constraint. It eliminates, for instance, any selection principle that requires thermalization (Principle 2), any principle that requires continuous relaxation of occupations (Principles 1, 5 in their simplest forms), and any principle that requires integrability breaking within the BCS sector (Closures 4-7).

The surviving selection principles must be:
(a) External to the BCS sector (operating at the level of the emergent geometry, not the fiber condensate), or
(b) Compatible with frozen GGE occupations (taking the integrability as given and determining Lambda from the *locked* configuration), or
(c) Operating at a different level of the hierarchy (Level 0: changing D_K itself, not Level 1-2: modifying occupations within fixed D_K).

---

## IV. Required Computations

### IV.1. Gate: JACOBSON-NONLOCAL-64

**What**: Test whether the nonlocal character of the spectral action (which evades the Weinberg no-go per Paper 09) provides a mechanism to fix the Jacobson integration constant.

**Method**: The spectral action S(tau) = Tr f(D_K^2/Lambda_sp^2) at the fold is 250,361 M_KK. The Jacobson derivation uses eta = 1/(4G) = a_2 M_KK^2 / (4 pi). The ratio rho_SA / (8 pi G) = a_0 Lambda_sp^4 / (8 pi G) gives the "naive" Lambda. But the nonlocal spectral action generates corrections: the effective Lambda from the full (non-expanded) spectral action is Lambda_eff = S_full / integral_(base) sqrt(g) d^4x, not the Seeley-DeWitt approximation. Compute the full spectral action (without asymptotic expansion) at the fold and at tau = 0.3, 0.5. Compare S_full with the SDW approximation f_0 Lambda_sp^4 a_0 + f_2 Lambda_sp^2 a_2 + f_4 a_4. If the non-perturbative remainder is O(1) or larger relative to the a_0 term, the SDW expansion is unreliable and the "114 OOM gap" may be an artifact of the expansion.

**Pre-registered criterion**:
- PASS: |S_full - S_SDW| / S_SDW > 0.1 (SDW expansion unreliable; non-perturbative corrections significant)
- FAIL: |S_full - S_SDW| / S_SDW < 0.01 (SDW expansion accurate; non-perturbative effects negligible)
- INFO: 0.01 < ratio < 0.1 (intermediate regime, further investigation needed)

**Input**: D_K eigenvalues at tau = 0.190, 0.300, 0.500 (available from canonical computation), cutoff function f.
**Depends on**: None (direct computation from known eigenvalues).

### IV.2. Gate: JACOBSON-BOUNDARY-64

**What**: Determine whether the transit boundary conditions constrain the Jacobson integration constant.

**Method**: The transit through the fold is a first-order phase transition (not a smooth roll). The pre-transit state has a specific spectral action S_pre, and the post-transit GGE has S_post. The difference S_post - S_pre is the energy injected by the transit. In the Jacobson framework, the transit is a discontinuous change in T_ab^{GGE}, which corresponds to a discontinuous change in the Ricci tensor (equation A9). The Bianchi identity requires f + R/2 = Lambda to be constant, but the transit is a singular event where the Bianchi identity may not hold in the usual sense (distributional stress-energy on a spacelike hypersurface). Compute the junction conditions across the transit surface using the Israel-Darmois formalism. The discontinuity in K_ab (extrinsic curvature) across the transit surface may impose a constraint on Lambda.

**Pre-registered criterion**:
- PASS: Junction conditions fix Lambda to a specific value (or narrow range) that is less than 10^{60} M_Pl^4 (reduces gap by > 50 OOM)
- FAIL: Junction conditions leave Lambda unconstrained (or constrain it to the spectral action value ~ 10^{118} M_Pl^4)
- INFO: Junction conditions provide a nontrivial constraint but do not fix Lambda uniquely

**Input**: Transit dynamics from S38 (Mach 13.75, tau_fold = 0.190), GGE state post-transit.
**Depends on**: None.

### IV.3. Gate: JACOBSON-KASPAROV-64

**What**: Test whether the Kasparov product structure of the spectral triple imposes constraints on the Jacobson integration constant beyond the base-space derivation.

**Method**: The Jacobson derivation applies to the *emergent* 4D metric. But the substrate is 10-dimensional (M^4 x SU(3)). The full Kasparov product spectral triple (A_M tensor A_K, H_M tensor H_K, D_M tensor 1 + gamma_5 tensor D_K) encodes the 10D geometry. Apply the Jacobson derivation to the *full 10D geometry* -- constructing 8-dimensional Rindler horizons in the 10D product space. The 10D Bianchi identity may constrain the 4D Lambda through the fiber contribution. Specifically, the 10D Einstein equations from the Jacobson derivation are:

    G_{AB}^{(10)} + Lambda^{(10)} g_{AB}^{(10)} = 8 pi G^{(10)} T_{AB}^{(10)}     (A16)

where A, B run over all 10 dimensions. Compactifying on SU(3) with the Kasparov product:

    G_{mu nu}^{(4)} + Lambda_eff g_{mu nu}^{(4)} = 8 pi G_N T_{mu nu}^{(4)}     (A17)

where Lambda_eff = Lambda^{(10)} + (curvature contribution from SU(3)). The fiber curvature R_K = a_2 / a_0 = 2776 / 6440 = 0.431 M_KK^2. If the 10D Lambda^{(10)} is determined by the 10D Bianchi identity, then the 4D Lambda_eff may be constrained by the fiber curvature.

**Pre-registered criterion**:
- PASS: 10D Jacobson derivation constrains Lambda_eff through fiber curvature, reducing the CC gap by > 10 OOM
- FAIL: 10D and 4D Jacobson derivations give the same undetermined Lambda (fiber decouples)
- INFO: Fiber introduces a nonzero shift to Lambda but does not reduce the gap significantly

**Input**: Kasparov product structure (Paper 01 VdD), D_K eigenvalues, a_0 and a_2 at fold.
**Depends on**: None (analytical computation).

### IV.4. Gate: SA-VERSUS-JACOBSON-64

**What**: Determine whether the spectral action vacuum energy is the same physical quantity as the Jacobson Lambda.

**Method**: The spectral action produces a vacuum energy density rho_SA = (2/pi^2) a_0 M_KK^4. The Jacobson derivation produces Lambda as an integration constant. These are *logically distinct* quantities. The spectral action value enters through a_0 (the zeroth SDW coefficient -- mode count). The Jacobson Lambda enters through the contracted Bianchi identity (a geometric constraint on the divergence of the Einstein tensor). Compute the map between the two: under what conditions does rho_SA = Lambda / (8 pi G)?

In the substrate, the spectral action is the fundamental object. The emergent Einstein equations are derived from it. But the Jacobson derivation shows that the Einstein equations can also be derived from thermodynamics alone, without reference to the spectral action. The two derivations must be *compatible* -- the spectral action's a_2 moment must reproduce G_N from the Jacobson derivation (SAKHAROV-GN-44 confirms this to factor 2.3). But must the a_0 moment reproduce Lambda?

The test: compute the spectral action on a maximally symmetric background (de Sitter with curvature set by Lambda_obs). The a_0 contribution gives rho_SA. The a_2 contribution gives G_N. If the spectral action's variational equations (delta S / delta g_mu_nu = 0) produce Lambda = rho_SA / (8 pi G), then the two quantities are the same and the 114-OOM gap is real within both formalisms. If the variational equations produce a different relationship, the gap may be a category error -- comparing two different quantities.

**Pre-registered criterion**:
- PASS: The spectral action's variational equations give Lambda != (2/pi^2) a_0 M_KK^4 / (8 pi G) (the two quantities are not the same; the gap is a category error)
- FAIL: The spectral action's variational equations give Lambda = rho_SA / (8 pi G) (the two quantities are the same; the gap is real)
- INFO: The relationship depends on the cutoff function f (ambiguous)

**Input**: Spectral action functional, variational equations, Seeley-DeWitt expansion.
**Depends on**: None (analytical computation).

---

## V. Assessment

### V.1. Is This a Genuine Resolution Path?

Hawking's critique (S63 workshop, H5.3) is precise: "The Jacobson route is formally OPEN but physically empty until something determines the integration constant."

I assess this as *correct but incomplete*. The Jacobson route is not a resolution of the CC problem. It is a *reformulation*. It replaces "why is the vacuum energy small?" with "what determines the integration constant?" These are not the same question, and the reformulation is valuable because:

1. It separates the CC from the spectral action. The 114-OOM gap is between the spectral action's a_0 moment and observation. The Jacobson route says this gap may be irrelevant -- Lambda is not determined by a_0.

2. It identifies the correct mathematical structure. Lambda is an integration constant of the Bianchi identity, not a coupling constant in a Lagrangian. This is a structural fact about the emergent equations, independent of the substrate.

3. It survives all 9 closures, not by accident, but because the closures target a different question (how to compute Lambda from spectral data). The Jacobson route says Lambda is not computed from spectral data at all.

But the reformulation is not a resolution because:

1. It provides no prediction. Any value of Lambda is consistent with the route.
2. It does not explain the observed coincidence rho_Lambda ~ rho_matter today.
3. It does not address why Lambda is positive rather than negative.
4. It reduces to the standard GR situation: Lambda is a free parameter.

### V.2. The Principle-Theoretic Diagnosis

From my perspective, the Jacobson route illuminates a deep structural fact: the *form* of the gravitational equations is determined by thermodynamics (a principle theory), but the *values* of the coupling constants (G, Lambda) require a constructive theory. Jacobson's derivation shows that G = (4 hbar eta)^{-1} is determined by the entanglement density eta -- and in the substrate, eta is determined by the spectral action through a_2. So G has a constructive explanation.

Lambda, by contrast, has no constructive explanation within the Jacobson framework. It is the one coupling constant that the principle theory leaves free. This is either:

(a) A genuine feature of the emergent theory (Lambda is underdetermined by the substrate, and its value requires cosmological input -- initial conditions, boundary conditions, or anthropic selection), or

(b) An indication that the Jacobson derivation is incomplete (there is a "second law" or "equilibrium condition" that goes beyond the first law dQ = T dS and constrains Lambda).

Option (b) is the more physically productive path. If there is a second thermodynamic condition that constrains Lambda, it would be of the form:

    S_total = S_bulk + S_boundary = maximum (subject to constraints)     (A18)

where the maximization of total entropy (matter plus gravitational) constrains Lambda. This is the Gibbons-Hawking approach (Paper 07 of my corpus): the Euclidean action of de Sitter space is I = -3 pi / (G Lambda), and the partition function Z = exp(-I) is maximized at Lambda = 0 (infinite Euclidean action). But this gives Lambda = 0, not Lambda = 10^{-122} M_Pl^4.

In the substrate, the relevant entropy is the spectral entropy S_spec = - Tr(rho ln rho) of the GGE relic. The GGE is a constrained maximum entropy state (maximum entropy subject to R-G charges). If the R-G charges depend on Lambda (through the coupling between the fiber condensate and the emergent curvature), then the entropy maximization *implicitly* constrains Lambda. The computation that would test this is JACOBSON-KASPAROV-64 (Gate IV.3): the 10D Jacobson derivation may couple the fiber entropy to the 4D Lambda.

### V.3. The Cheapest Decisive Test

Before committing to the four gates above, the cheapest decisive test is Gate IV.4 (SA-VERSUS-JACOBSON-64). If the spectral action's variational equations give Lambda != rho_SA / (8 pi G), the entire 114-OOM gap is a category error -- we have been comparing the wrong quantity to observation. This is a purely analytical computation (variational calculus on the spectral action) with no numerical input required. It should take priority.

If Gate IV.4 fails (Lambda = rho_SA / (8 pi G), the gap is real), then Gate IV.3 (JACOBSON-KASPAROV-64) is the next priority -- it tests whether the 10D structure provides additional constraints beyond the 4D Bianchi identity.

If both fail, the Jacobson route is structurally verified as physically empty: Lambda is genuinely a free parameter and the CC problem requires a mechanism external to both the Jacobson derivation and the spectral action.

### V.4. Structural Position in the Constraint Map

**Where Path A sits**: it occupies the sole surviving region of *principle-theoretic* CC paths. All *constructive* paths (mechanisms to compute Lambda) are either closed (9 closures) or conditionally open (Paths B, C, E in framework-cc-oom.md Section III). Path A is not a constructive path -- it is the observation that the emergent equations have a free parameter. It survives by being unfalsifiable, which is not the same as being correct.

**What would close Path A**: nothing can close it in its formal sense (the integration constant is a mathematical fact). But the physical content of Path A -- the claim that this integration constant is the physical Lambda -- can be tested by Gate IV.4. If the spectral action's variational equations fix Lambda to a specific value (even the wrong one), then the integration constant is not physically free; it is determined by the substrate.

**What would advance Path A**: a physical principle that determines the integration constant. The four gates above test four candidate principles. Any PASS would promote Path A from a reformulation to a (partial) resolution.

---

## VI. Conclusion

The Jacobson route is the *cleanest* surviving CC path and the *emptiest*. It is clean because it rests on permanent mathematical structure (the Bianchi identity forces Lambda to be constant, not fixed). It is empty because it provides no mechanism to determine the constant.

The 9 CC closures are orthogonal to this path -- they close mechanisms to compute Lambda from spectral data, while Path A says Lambda is not computed from spectral data at all. The path survives all closures by structural independence, not by satisfying any gate.

The critical next computation is SA-VERSUS-JACOBSON-64: determine whether the spectral action's variational equations give the same Lambda as the integration constant. If they do, the 114-OOM gap is real within both formalisms and Path A reduces to standard GR ("Lambda is free"). If they do not, the gap may be a category error and the physical Lambda may be determined by a different spectral moment than a_0.

The Jacobson route reformulates the CC problem. It does not solve it. But the reformulation is structurally valuable: it separates what the emergent equations *require* (Lambda constant) from what the spectral action *suggests* (Lambda ~ a_0 M_KK^4). Whether these two Lambdas are the same quantity is the decisive open question.

---

## VII. File References

| File | Content |
|:-----|:--------|
| `sessions/archive/session-63/framework-cc-oom.md` | Master CC reference (all 9 closures, all paths) |
| `sessions/archive/session-63/s63_jacobson_gge_analysis.md` | JACOBSON-GGE-63 full analysis (7 steps, 3 perspectives) |
| `sessions/archive/session-63/session-63-hawking-quantum-acoustics-workshop.md` | Hawking H1, H5.3, E2 (Jacobson temperature, critique) |
| `sessions/archive/session-63/session-63-volovik-van-den-dungen-workshop.md` | Mother Superfluid, E1, transit-as-relaxation |
| `sessions/archive/session-63/session-63-W3-workingpaper.md` | W3-03 (JACOBSON-GGE-63), W3-06 (9th closure) |
| `researchers/Einstein/09_2025_Capozziello_Weinberg_Nonlocal_Gravity.md` | Weinberg no-go evasion via nonlocality |
| `researchers/Einstein/07_2024_Sola_Peracaula_Vacuum_Energy_CC.md` | Running vacuum model |
| `computations/s63_jacobson_gge.py` | JACOBSON-GGE-63 computation script |
| `computations/s63_jacobson_gge.npz` | JACOBSON-GGE-63 output data |
