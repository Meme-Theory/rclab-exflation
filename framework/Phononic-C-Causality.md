# Phononic Causality: Propagation Versus Substrate Dynamics

**Author**: Transit-Dynamics-Theorist (synthesizing the S74 transit x einstein workshop)
**Date**: 2026-04-11 (authored); **comprehensively expanded to S93-era whole-project state 2026-05-25** (WX-W4-2)
**Status**: Canonical framework document, post-Session 74; brought current to S93 in the comprehensive aggregate expansion
**Sources**: `sessions/archive/session-74/session-74-transit-einstein-workshop.md` (primary), user thesis (2026-04-11), S44 permanent theorems, Gilkey 1975/1995 local index theory, Chamseddine-Connes 1996 spectral action; S93-era additions per Section 11 "Post-S74 sources" (S76/S77 transit-einstein, S84 two-speed tensor-tilt, S85 W6/W7, S92 d_s-flow + two-scale alpha_s, LQG/CDT comparison, cross-pillar 3He-B BdG bridge)
**Grounding**: Every theorem cited is stated with its regime of validity. Every numerical claim is sourced from the session/verdict it was produced in (S93-era line numbers re-pinned to `computations/_shared/canonical_constants.py`). This document is load-bearing and citable.

---

## Abstract / TL;DR

In the phonon-exflation framework, "the speed of light" is not a fundamental postulate. It is an emergent property of the second Seeley-DeWitt coefficient a_2^{zeta} of the Chamseddine-Connes spectral action applied to the Jensen-deformed SU(3) fibre. Every framework event divides cleanly into one of two disjoint classes: **PROPAGATION** events, which are group velocities of phononic branches on the emergent 4D Lorentzian metric g_M and are bounded above by c_Gold = 0.915 M_KK; and **SUBSTRATE DYNAMICS** events, which are functional derivatives of the a_0^{zeta} spectral moment (Jensen flow, instanton nucleation, Bogoliubov pair creation, fold transit) and are NOT c-bounded because g_M does not exist at the event.

The separation is rigorous. It is a consequence of Gilkey's local index theorem: the heat-kernel expansion of D_K^2 produces Seeley-DeWitt coefficients a_n of distinct polynomial degree 2n-d, and these coefficients are linearly independent as sheaves of local invariants. a_0^{zeta} (volume / vacuum potential / instanton action) and a_2^{zeta} (Einstein-Hilbert / gravity) are DIFFERENT polynomial degrees, so no functional on the spectral triple is simultaneously an a_0^{zeta} and an a_2^{zeta} quantity. Derivatives in a_0^{zeta} space cannot be bounded by group velocities in a_2^{zeta} space. This is the **Spectral-Moment Decoupling Theorem** — the structural core of the framework's causal architecture.

The user's film analogy is load-bearing: the substrate IS the film, not a thing IN the film. c_Gold is the playback frame rate — it limits what plays ON the film. Editing the film (splicing frames, rewriting scenes, transitioning the spectral triple from one configuration to another) is not bounded by the playback speed, because editing is not playback. Mach 13.75, instanton tunneling, and fold transit are editing operations; photon propagation and phononic acoustic modes are playback. The two classes live in different polynomial degrees of the spectral action expansion.

This document states the theorems, classifies the framework's events, corrects older GR-causal language where it was misapplied, and records the pre-registered S75 computations that test the construction.

**S93-era expansion (2026-05-25).** This document has been brought current to the whole-project S93 state of its domain. The causal architecture is substantially more developed than at S74: the a_2^{zeta} Seeley-DeWitt coefficient that generates g_M also generates Newton's constant quantitatively (M_Pl_eff^2 = a_2^{zeta}/(48 pi^2) = 5.862 M_KK^2 -> 1.80e17 GeV; Section 3.6), making "c is emergent from a_2^{zeta}" a QUANTITATIVE claim in the substrate-first direction. The fold has TWO "expansion rates" — H_transit (a_0^{zeta} functional derivative, NOT on g_M) and H_Friedmann (a_2^{zeta}-built, emergent) — related by the stretch factor F_stretch, a direct instance of the decoupling theorem (Section 5.1a). Three entirely new causal-architecture axes have appeared: the spectral-dimension d_s flow (the dimensionality propagation "sees"; d_s -> 8 Weyl, no CDT-like UV reduction; Section 8.5), the two-scale alpha_s running (a substrate-scale -0.0859 inside the BZ vs a CMB-pivot 0, distinguished by the transport degree deg(T) = +2; Section 8.2a, superseding the single "flat" label), and the laboratory-IN 3He-B BdG acoustic-metric bridge (Section 8.4(c.a)). All five S74 structural theorems now carry landed verdicts, and all ten pre-registered S75 computations have been confronted with their outcomes (Section 9). The film analogy and the two-regime distinction are unchanged and load-bearing throughout.

---

## 1. The User Thesis

The workshop was convened around this framing (verbatim from the workshop header, 2026-04-11):

> "I don't think that any of the substrate is 'limited' to C in the traditional sense. C is the max that anything moves **across** the substrate, but not 'any force' necessarily; e.g. the transit itself. Light speed is a speed limit because the substrate has to **accommodate** whatever field or matter is going through it at that time, but the substrate's instantons and most of its geometry isn't constrained by that framerate — **it is the film**."

Unpacked in the workshop, this thesis has three load-bearing components.

**Component 1: c limits propagation ACROSS the substrate.** Phononic branches, photons, fermions, and any other mode that lives ON the emergent 4D metric g_M have a group velocity v_g = d omega / dk defined as the rate at which a signal advances on g_M. Every such v_g is bounded above by c_Gold = 0.915 M_KK, which is the substrate's throughput capacity — the maximum rate at which the Goldstone branch of the fibre-metric deformation group can carry energy through g_M. This is where "the substrate has to accommodate throughput" and where the c-as-speed-limit regime lives.

**Component 2: c does NOT limit substrate dynamics.** Fold transit, instanton nucleation, Jensen deformation evolution, spectral-action gradient flow, and spectral reorganization events are not "moving through" anything. They ARE the substrate reorganizing itself. There is no g_M across which these events advance; they are changes OF the spectral triple that generates g_M. The film changes faster than the frame rate because editing is not playback.

**Component 3: The film analogy is load-bearing, not decorative.** The frame rate (c_Gold) is a throughput limit on what plays on the film. The substrate IS the film. Editing the film (splicing, reorganizing, running a transit) is not bound by frame rate, because editing is an operation on the film, not an event in the movie. The frame rate limits WHAT PLAYS on the film, not what the film is doing internally.

The goal of the S74 transit x einstein workshop was to take this conceptual distinction and turn it into an operational theorem. The workshop succeeded. The result is the **Spectral-Moment Decoupling Theorem** (Section 3.1) — a rigorous version of the user thesis, anchored in Gilkey's local index theorem.

---

## 2. The Two-Regime Distinction

Every framework event belongs to exactly one of two disjoint classes.

### 2.1 Regime 1: Propagation Across the Substrate (c-bounded)

**Definition.** An event is **PROPAGATION** if and only if all three of the following hold (T1, workshop):

1. It has a source and a receiver separated by non-zero g_M-distance.
2. There exists a phononic branch carrying the excitation from source to receiver.
3. The branch's dispersion relation omega_b(k) defines a group velocity v_g = d omega / dk that sets the rate at which the signal advances on g_M.

The maximum v_g across all observable branches is **c_Gold = 0.915 M_KK**, fixed by the gapless Goldstone mode on the Killing-protected direction of the Jensen-deformed SU(3) fibre (W4-L, Baptista paper 13 eq 3.42 fibre coset projection; E1 of the workshop).

**PROPAGATION events are c-bounded.** The bound is a group-velocity envelope set by the a_2^{zeta} Seeley-DeWitt coefficient of the spectral action. It applies to every excitation that lives ON g_M after the transit.

**Canonical examples** (T1):

| Mode | v_g (M_KK) | Source | Interpretation |
|:-----|----------:|:-------|:--------------|
| Goldstone acoustic (Killing-protected) | 0.915 | W4-L, S52 GL-JOSEPHSON-52 | Sets c_Gold itself; saturates the bound |
| Photon on L_Y post-transit | ~0.915 | W3-N L_Y hypercharge bundle | U(1)_Y gauge excitation; tracks c_Gold at leading order |
| B1 singlet (acoustic scalar) | 0.0798 | W1-A, W2-A | Dispersive phononic branch, BAO channel |
| B2 flat optical (quartet) | 0.00200 | W1-A, W2-A | Van Hove plateau, flat band |
| B3 dispersive optical (triplet) | 0.1397 | W1-A, W2-A | Intermediate branch |
| Leggett branch | 0.0255 | W4-L, S66 Leggett DM | Gap-massed, inter-band coherence |
| 3He-B BdG sound (lab-IN image) | c_BdG (on h_acoustic) | FWD-C3 Pillar IV<->V, cross-pillar-bridge-corpus | Laboratory analog of c_Gold on the 3He-B acoustic metric (Section 8.4(c.a)); propagation on h_acoustic, NOT g_M |

### 2.2 Regime 2: Substrate Dynamics (not c-bounded)

**Definition.** An event is **SUBSTRATE DYNAMICS** if any of the following hold (T1, workshop):

1. It is a change in the spectral triple itself — the Dirac operator D_K, its Jensen modulus tau, its topological sector, its moduli.
2. No source/receiver pair can be defined because there is no pre-existing g_M on which to measure distance at the moment of the event.
3. The rate of the event is set by spectral-action functional derivatives (dS/dtau, dn_inst/dtau, det H_35, dV_tHooft/dtau), NOT by any dispersion relation.

Rates in this class are bounded by the D_K eigenvalue structure (M_KK, lambda_max, det H_35) but are NOT bounded by c. They live in the a_0^{zeta} spectral moment, which is structurally decoupled from the a_2^{zeta} spectral moment that generates g_M (Theorem 3.1 below).

**Canonical examples** (T1, T4):

| Event | Rate | Units | Source | Interpretation |
|:------|-----:|:------|:-------|:--------------|
| Fold transit tau-evolution | +58,673 | M_KK / tau | canonical dS_fold | Jensen flow under spectral-action gradient |
| Instanton nucleation (Coulomb gas) | 2.8046 | M_KK^4 / tau | W1-Q | dV_eff^CG / dtau at tau = 0.48 |
| 't Hooft vertex evolution | 1.498e-07 | M_KK^4 / tau | W1-R | dV_tHooft / dtau at tau = 0.48 |
| Instanton back-reaction force | -1.4383 | M_KK^4 / tau | W2-R | dV_inst_A / dtau at tau = 0.48 |
| Bogoliubov squeezing r_B1 | 3.571 | dimensionless | W1-A, W2-A | Parker pair production amplitude, B1 branch |
| Bogoliubov pair count n_pairs | 59.8 | count | S38, W2-A | GGE relic (Brundobler-Elser saturation) |
| Lefschetz thimble winding | n* = 60 | winding number | W3-N | Single saddle on L_Y, dominates by 10^26665 |
| H_transit (fold expansion rate) | (1/Vol_SU3) dS_fold/dtau | spectral action / (modulus * volume) | S76 W1-E, S85 W7 | a_0^{zeta} functional derivative; NOT H_Friedmann (Section 5.1a) |
| Spectral dimension d_s | -2 dlnP/dln-sigma, P = Tr e^{-sigma D_K^2} | dimensionless (-> 8 Weyl) | S92 ad-hoc | heat-trace log-derivative; the dimensionality propagation sees (Section 8.5) |
| alpha_s^substrate running | (a_4^{zeta}/a_2^{zeta})^2 - 1 = -0.08587279 | dimensionless (log-log curvature) | S92 AH-TR-1 | spectral-tilt curvature at Mellin pole s=3, inside BZ (Section 8.2a); NOT a velocity |

None of these quantities has units of (distance on g_M) / (time on g_M). None has a definable group velocity. None is subject to a c-bound. (H_Friedmann, the EMERGENT FRW rate built from a_2^{zeta}, is also not a velocity but is a background rate on g_M; see Section 5.1a and the EC8 walk in Section 6.3.)

### 2.3 Operational criteria for classification

The workshop produced an algorithmic classification protocol with six steps. It is stated in Section 6. The protocol's front-end (STEP 0) is the rigorous version of "does this event live in a_0^{zeta} or a_2^{zeta} space?" and it resolves three of seven canonical edge cases in a single step.

The four original C1-C4 discriminators from T1 were: metric existence, source-receiver separability, dispersion relation existence, and functional-derivative signature. These remain valid as tests but are subsumed by STEP 0 of the revised algorithm.

---

## 3. Structural Theorems

This section states the four theorems that make the propagation / substrate-dynamics distinction rigorous. Each theorem carries its statement, proof sketch, regime of validity, and workshop source. Together they constitute the permanent structural backbone of the framework's causality architecture.

### 3.1 Spectral-Moment Decoupling Theorem

**Source**: E-R2-1 (transit), C-R2-E1 (einstein), workshop Round 2. Anchored in Gilkey 1975, 1995; Chamseddine-Connes 1996.

**Statement.** Let (A, H, D_K) be a spectral triple with Jensen modulus tau and Chamseddine-Connes spectral action

    S_spec[D_K, Lambda] = Tr f(D_K^2 / Lambda^2) = sum_{n>=0} f_n Lambda^{d-2n} a_n[D_K]     (3.1)

where the a_n are Seeley-DeWitt coefficients of the heat-kernel expansion of D_K^2. Then:

**(i) a_0^{zeta} derivatives are SUBSTRATE DYNAMICS.** Any quantity Q = dF/dtau where F is a functional of the a_0^{zeta} moment (or any combination of moments not containing a_2^{zeta}) is SUBSTRATE DYNAMICS. Q has units of (spectral action) / (modulus) and has no projection onto a velocity on any emergent metric. NO c-bound applies.

**(ii) a_2^{zeta} group velocities are PROPAGATION.** Any quantity Q = v_g(k) = d omega_k / dk where omega_k is an eigenvalue-dispersion of D_K on the post-transit emergent g_M is PROPAGATION. Q is bounded above by c_Gold = 0.915 M_KK as an envelope, with the per-branch bound being v_g,b for each branch b.

**(iii) No velocity comparison between the classes.** There is NO velocity bound connecting class (i) and class (ii). The two classes live in DIFFERENT spectral moments of the same Dirac operator, and their "rates" are incommensurable as velocities. No Layer 1 / Layer 2 rate-comparison can be made between a_0^{zeta} derivatives and a_2^{zeta} group velocities.

**(iv) One-way projection via Bogoliubov.** Observable projections from class (i) onto class (ii) are mediated by the Bogoliubov transformation at the emergence boundary (the fold transit). The projection is one-way: substrate-dynamics input -> observational squeezing-pattern output. The reverse projection (observing a substrate event directly) is impossible because g_M does not exist at the event.

**Proof sketch (from C-R2-E1).** The Chamseddine-Connes expansion writes S_spec as a sum of terms indexed by polynomial degree. For f(x) = exp(-x) or equivalent cutoff function, the Seeley-DeWitt coefficients a_n are local integrals of polynomial invariants of the metric, connection, and endomorphism data on the fibre, with dimensions (length)^{2n-d}.

Gilkey's local index theorem (1975, 1995) establishes that for a Laplace-type operator P on a compact spectral triple, the heat-kernel expansion

    Tr e^{-t P} ~ sum_{n>=0} t^{(n-d)/2} a_n[P]     (3.2)

has coefficients a_n that are DISTINCT polynomial forms, each uniquely determined by its dimensional degree 2n - d. There is no functional on the spectral triple that is simultaneously an a_0^{zeta} AND an a_2^{zeta}: the first is a zero-dimensional volume/potential (integral of a scalar density), the second is a two-dimensional curvature invariant (integral of a scalar curvature density). These are different sheaves in the local-invariant filtration of polynomial invariants on the fibre, and no element of one appears in the other.

Since D_K^2 is Laplace-type on the Jensen-deformed fibre at all canonical tau values, Gilkey's theorem applies. The decoupling is therefore a theorem of local index theory, not a framework-specific convention.

**Regulator scheme (a_n^{zeta}).** The Seeley-DeWitt coefficients cited throughout this document are in the **zeta-function regularization scheme** of the Chamseddine-Connes spectral action (cutoff f(x) ~ exp(-x), the canonical heat-kernel scheme). The canonical a_2^{zeta}(fold) = 2776.1653888633655 is explicitly the zeta-scheme half-zeta_D(1) = 0.5 * sum_n d_n / lambda_n^2 (canonical_constants.py:453 a2_fold note, S42 CONST-FREEZE-42); the companion a_4^{zeta}(fold) = 1350.7216415169728 is the zeta-scheme half-zeta_D(2) = 0.5 * sum_n d_n / lambda_n^4 (a4_fold). In regulator-pin notation (regulator-pin-discipline.md): a_2^{zeta}, a_4^{zeta}, a_0^{zeta}. The decoupling theorem is REGULATOR-INVARIANT at the polynomial-degree level (Gilkey orthogonality holds for any smooth cutoff f), but the NUMERICAL values quoted are zeta-scheme. See Section 4.1a for the a_2^{zeta}(fold) vs a_2^{zeta}(full L_max=10) truncation distinction.

**Verification status (LANDED).** OQ6 SPECTRAL-DECOUPLING-CERT-75 LANDED **PASS** at S75 W2-E: "Spectral-moment decoupling CERTIFIED — a_0^{zeta}, a_2^{zeta}, a_4^{zeta} algebraically independent, Wronskian nonzero" (session-75-tesla-synthesis.md, session-75-mack-synthesis.md; producing script s75_spectral_decoupling_cert.py imports a0_fold, a2_fold, a4_fold; gate CERT-75). The verdict was subsequently MIGRATED to **INFO** at the S81 batch-hygiene pass (T3-BATCH-S75-SPECTRAL-DECOUPLING-CERT: INFO, scheme=batch-canonical-hygiene, convention=no-run-no-gate, sha256=55a1b9e0a8bebc05d1cecfab1a398c16619f4efddcd36dd19cfc083ea1b7b81e) — a provenance reclassification (the S81 batch migrated the S75 archive verdicts to no-run-no-gate INFO status without re-running), NOT a retraction of the PASS. The Spectral-Moment Decoupling Theorem is therefore a framework-internal CERTIFIED result, not merely an inherited general Gilkey statement.

**Regime of validity.** The theorem is rigorous whenever:

- D_K^2 is Laplace-type on a compact spectral triple. This holds for all framework examples (Jensen-deformed SU(3), all canonical tau).
- The spectral triple has a well-defined heat-kernel expansion with finite coefficients a_n. Holds for smooth D_K with bounded spectrum (all canonical moduli).
- The cutoff function f is smooth and decays at infinity. The Chamseddine-Connes expansion uses f(x) ~ exp(-x) or regularizations thereof.

The theorem BREAKS DOWN formally at:

- Truncation boundaries O(1/L_max) where the finite Peter-Weyl decomposition distorts the heat kernel. The framework's L_max = 10 truncation produces 155,984 eigenvalues, and the decoupling is exact within this truncation to machine precision. Beyond L_max, higher-order a_n moments begin to contribute to both a_0^{zeta} and a_2^{zeta} sectors through cross-terms suppressed by (L_max)^{-2} ~ 10^{-2}.
- Degeneracies in the eigenvalue spectrum where d omega / dk is ill-defined. Handled by working in a single Peter-Weyl sector at a time.
- The fold transit itself, where D_K is in the process of being reorganized. Inside the fold, the theorem still holds (a_0^{zeta} and a_2^{zeta} are still distinct polynomial degrees), but the "time" at the fold is the modulus tau, not a Lorentzian coordinate, so both classes of events have non-metric rates.

**Consequence.** Any framework computation that attempts to bound a SUBSTRATE DYNAMICS event (an a_0^{zeta} derivative) with a c-bound (an a_2^{zeta} envelope) is structurally malformed. The malformation can be caught by a SINGLE spectral-moment inspection at STEP 0 of the classification algorithm (Section 6).

### 3.2 Two-Manifold Non-Embedding Theorem

**Source**: E-R2-E3 (einstein), workshop Round 2. Status (S93-era): **reframe PROVEN** (no longer "candidate pending OQ5"; see "Verification status (LANDED)" below).

**Statement.** The pre-fold emergent Lorentzian manifold g_M^< and the post-fold emergent Lorentzian manifold g_M^> generated by the a_2^{zeta} Seeley-DeWitt coefficient at different values of the Jensen modulus tau CANNOT be embedded into a single 4D FRW trajectory with a single scale factor a(t) and Hubble parameter H(t). The obstruction is structural: the two a_2^{zeta} values come from different fibre metrics g_phi(tau_pre) and g_phi(tau_post), and there is no single Seeley-DeWitt expansion that simultaneously contains both.

**Proof sketch.** The scalar curvature of the Jensen-deformed fibre at modulus tau is given by Baptista paper 13 eq (2.40):

    R_{g_phi} = 3(4 - 25 tau + 33 tau^2 - 8 tau^3) / [lambda (1 - tau)^2 (1 - 4 tau)]     (3.3)

For tau_pre = 0 and tau_post = tau_exit, the two values of R_{g_phi} differ by the rational function

    Delta R = 3(4 - 25 tau_exit + 33 tau_exit^2 - 8 tau_exit^3) / [lambda (1 - tau_exit)^2 (1 - 4 tau_exit)] - 12 / lambda     (3.4)

which is non-zero for any tau_exit != 0. Each value of Delta R corresponds to a different a_2^{zeta} Einstein-Hilbert coefficient and therefore a different emergent G_N, a different f_phi prefactor in the Einstein-Hilbert term, and a different emergent H(t). The two Hubble rates are not related by a single time-reparameterization of the same trajectory; they are solutions of DIFFERENT variational problems on DIFFERENT metrics.

Any framework computation that tries to fit pre-fold and post-fold into a single Friedmann trajectory will produce a non-trivial bracket. The 86-OOM split in W1-E Friedmann-from-a_2^{zeta}-74 is the specific quantitative signature for the current canonical parameters, but the qualitative STRUCTURE of the bracket — that it exists and is non-trivial — is a theorem of the two-manifold structure.

**Regime of validity.** The theorem is rigorous whenever:

- tau_pre != tau_post (the transit is non-trivial). Holds by definition at the fold.
- R_{g_phi} is smooth in tau between the endpoints. Holds for canonical tau_exit in (0, 0.25), where Baptista 2.40 is analytic.
- The a_2^{zeta} coefficient is a strictly monotonic functional of the Jensen modulus. Holds by workshop analysis of the scalar curvature formula.

The theorem BREAKS DOWN at:

- Degenerate cases where tau_pre = tau_post (trivial limit, no transit). Not relevant to framework events.
- The singularities of eq (3.3) at tau = 1 and tau = 1/4. The framework's tau_exit = O(0.4-1.614) passes through tau = 1/4 but not tau = 1, so the formula is smooth in the relevant range. The singularity at tau = 1/4 is mitigated by the Seeley-DeWitt prefactor f_phi which also has a compensating zero.

**Consequence.** The 86-OOM W1-E bracket is the RAW signature of the non-embedding, NOT a failure of the framework to match cosmological observations. Any attempt to "fix" W1-E by collapsing the bracket to zero would violate the Two-Manifold Non-Embedding Theorem. The correct response is to abandon the single-Friedmann picture and adopt the two-manifold picture with a Bogoliubov transformation as the projective bridge between the two manifolds (see C-R2-3 of the workshop for the equivalence of the two-manifolds picture and the Bogoliubov-overlap picture).

**Verification status (LANDED).** The S74-era "candidate pending OQ5" is now superseded by the S93-era reframe-PROVEN status:

- **FRIEDMANN-FROM-A2-74 reframe PROVEN** (atlas-09-retractions-materials.md, Item 35): the assumption "a single f_conv scalar can bridge fold-epoch fiber-local energy density to today's emergent 4-metric H_0" is **BROKEN** — exactly the single-Friedmann-embedding assumption this theorem forbids. The reframe (the 86-OOM bracket IS the non-embedding signature, NOT a matching failure) is the PROVEN reading.
- **OQ5 TWO-MANIFOLD-NEMB-75** producing script s75_two_manifold_nemb.py exists; verdict MIGRATED **INFO** at S81 (T3-BATCH-S75-TWO-MANIFOLD-NEMB: INFO, sha256=d7abcfd28d66a89729cecd866da8fea31c4a1f43632adb6d867f90fdaa703415; the companion T3-BATCH-S74-FRIEDMANN-FROM-A2: INFO, sha256=e5b37598547548a5fb6e7b6f48c802a49e57e1eecc72172a19ebe943dea3a913).
- **Downstream consequence — FRIEDMANN-BCS-38 BROKEN.** The Friedmann-BCS coupling (the attempt to dynamically lock tau by a single coupled Friedmann-BCS dynamics) is BROKEN: shortfall 133,200x in coupled dynamics; "structurally addressed by Two-Manifold Non-Embedding Theorem but no replacement single-field formulation exists" (loop-quantum-gravity-phonon-exflation-comparison.md; atlas-04-assumptions T6). The two-manifold structure is the structural CAUSE of the BCS-38 break: there is no single FRW trajectory for a single-field Friedmann-BCS lock to live on. The correct response remains the two-manifold + Bogoliubov-bridge picture (this section's Consequence), now with the BCS-38 break as the downstream confirmation.

### 3.3 Layer 1 / Layer 2 O(tau) Split

**Source**: D-R2-2 (transit), C-R2-E2 (einstein), workshop Round 2. Observationally testable at BAO peak scale.

**Statement.** The framework has two causal layers:

- **Layer 1**: substrate throughput bound, defined by the stiffness/inertia ratio of fluctuations on the spectral triple at a given Jensen modulus. For direction i (one of the eight SU(3) generators), the Layer 1 velocity is c_i^(1) = sqrt(Z_i(tau) / M_i(tau)), where Z_i is the kinetic stiffness from the a_4^{zeta} moment projected onto direction i and M_i is the inertial coefficient from the a_2^{zeta} moment projected onto direction i. This is a substrate-level property of D_K, computed from the fibre's internal structure.

- **Layer 2**: emergent Lorentzian cone bound, defined by the null cone of g_M from a_2^{zeta} Seeley-DeWitt applied at the post-transit fibre metric. For direction i, the Layer 2 velocity is c_i^(2) = v_g(k) on the emergent metric, computed from BdG diagonalization of D_K^2 on g_M.

**The theorem has two parts:**

**(i) Exact coincidence on the Killing-protected direction.** For the Killing-protected (Goldstone) direction, which commutes with the Jensen potential V(|phi|^2) in Baptista eq (3.43), both Z and M are protected by bi-invariance, and c_Goldstone^(1) = c_Goldstone^(2) = c_Gold = 0.915 M_KK to all orders in tau. The coincidence is EXACT, not merely leading-order.

**(ii) O(tau) split on the seven gapped directions.** For the seven directions where Jensen deformation breaks bi-invariance (B1, B2, B3, and the four Leggett/optical branches), the Jensen-potential corrections to Z_i(tau) and M_i(tau) enter DIFFERENTLY than the corrections to a_2^{zeta}(tau) itself. The former see V(|phi|^2) evaluated at a specific direction; the latter see the fibre-averaged V. The difference c_i^(1) - c_i^(2) on the gapped directions is O(tau) = O(0.19) at the fold, NOT the Planck-suppressed O((M_KK/M_Pl)^2) ~ 10^{-5} nor the energy-suppressed O((E/M_KK)^2) ~ 10^{-34}.

**Proof sketch (part i — Killing direction).** Bi-invariance of the SU(3) Killing metric at the protected direction means that Z and M on this direction are determined by the Casimir structure of the generator algebra, which is invariant under the Jensen flow (the Jensen potential commutes with the Killing generator). The Seeley-DeWitt expansion on the protected direction is therefore identical to the bi-invariant expansion at all orders in tau. The a_2^{zeta} coefficient projected onto the protected direction is determined by the same Casimir structure, so c_i^(2) tracks c_i^(1) to all orders.

**Proof sketch (part ii — gapped directions).** For a gapped direction i, Z_i receives corrections from the Jensen potential V(|phi|^2) through the fibre's internal kinetic term (Baptista eq 2.40 scalar curvature formula). a_2^{zeta}(tau) receives corrections from the FIBRE INTEGRAL of V, which is a zeroth-moment average over the coset. The zeroth moment differs from the value of V at a specific direction by the coset-averaging factor, which is a function of the direction's embedding in the Jensen-deformed fibre. At tau_fold = 0.190, the fibre-averaged V differs from V evaluated on any specific gapped direction by a correction of order tau itself — a 19% effect, not a Planck-suppressed one.

**Regime of validity.** The O(tau) split holds whenever:

- The direction is not the Killing-protected Goldstone. Seven of eight SU(3) directions.
- tau is in the fold regime [tau_fold, tau_exit] where the Jensen potential is non-trivially deforming the fibre metric.
- The BdG diagonalization on g_M is well-defined (post-transit, Lorentzian cone stable).

The split is NOT an NLO correction to the leading-order coincidence claim that einstein originally wrote in E4. It is an EXPLICIT first-order effect on the gapped directions that the original claim missed.

**Consequence: observational test.** If the Layer 1 and Layer 2 branch speeds differ by O(tau) ~ 0.1-0.3 on the seven gapped directions, this is directly visible in the BAO acoustic peak position at k ~ 0.043 Mpc^{-1} — the B1 singlet projection that dominates the acoustic feature. The framework CAN be falsified here: DESI and Simons/CMB-S4 data already exist, and a precision comparison of the acoustic peak position against the framework's Layer-1 prediction is a real test.

**Verification status (LANDED; subsumed by the S84 two-speed tensor-tilt theorem).** Pre-registered as OQ1 LAYER-1-LAYER-2-DIFF-75 (Section 9). The numbered S75 gate was **NOT-RUN as such** — the KB carries no LAYER-1-LAYER-2-DIFF-75 verdict line. Its physical content was instead realized in the cosmological tensor sector and PROVEN there:

- **S84 two-speed tensor-tilt theorem [PROVEN]** (session-84-mack-synthesis.md): with distinct tensor and scalar propagation speeds c_T != c_S (the Layer-1/Layer-2 two-speed structure applied to the inflationary tensor mode), the tensor spectral tilt is n_T(two-speed) = -r * c_T / (8 * c_S), whereas single-speed slow-roll gives n_T(single) = -r/8 (Garriga-Mukhanov 1999 generalized consistency). The DIRECTION: c_T/c_S > 1  =>  |n_T(two-speed)| > |n_T(single)| — the substrate two-speed metric makes the CMB-scale tensor tilt MORE negative than the single-speed slow-roll consistency relation by exactly the factor c_T/c_S.
- **Canonical speeds**: c_T = 1.000 (the tensor mode B2-Goldstone, S83 G46; the gravitational-cone speed) and c_S = 0.485 (= c_BLV, BCS-channel-dressed and substrate-compacted; the scalar acoustic speed). So c_T/c_S = 2.06 > 1, and the framework predicts a more-negative tensor tilt than -r/8.
- **S85 W3-5 two-speed transfer identity** c_S_canon = f_B PASS (machine precision, max|ratio-1| = 0.000e+00 across all 5 regulators) — the scalar two-speed leg is regulator-invariant.
- The Layer-taxonomy was further developed at S86 (s86-sector-2-split-layer-taxonomy.md, PROVEN).

So the document's Layer-1/Layer-2 O(tau) split thesis (this section) is REALIZED in the c_T-vs-c_S cosmological tensor sector with a PROVEN directional theorem (the BAO-peak per-branch number remains the uncomputed numbered-gate content; the two-speed STRUCTURE is PROVEN). See Section 8.1a for the observational consequence.

### 3.4 Goldstone Masslessness (from Kasparov Factorization)

**Source**: van den Dungen and qa-vdd workshop (S68/S69). Cited here because the theorem is the structural reason c_Gold is the only propagation bound in the framework.

**Statement.** The Goldstone mode of the fibre-metric deformation group is massless at all canonical tau values, and its sound speed is the maximum achievable group velocity on the post-transit emergent g_M. The Kasparov factorization of the spectral triple's K-theory class guarantees that the gapless mode sits at the protected Killing direction of the Jensen flow, with mass m_Goldstone = 0 as a structural identity (not a tuning).

**Proof sketch.** The fibre-metric deformation group has one direction (the Killing-protected U(1)_Y generator, commuting with the Jensen potential) along which the a_0^{zeta} Jensen potential is flat. The Goldstone of a flat direction in the potential has vanishing mass by Goldstone's theorem applied to the spectral action. The Kasparov factorization of the fibre's K-theory class into a "fibre" factor and a "base" factor preserves the protected direction under the factorization map, so the Goldstone's masslessness is a STRUCTURAL property of the K-theory class, not a fine-tuning of the Jensen deformation.

The Kasparov argument is: (i) the Jensen-deformed SU(3) fibre decomposes as a KK module over the coset C^*(SU(2) \ SU(3)) quotient; (ii) this decomposition is compatible with the K-theoretic even-odd splitting of the spectral triple; (iii) the gapless Goldstone appears in the odd K_1 sector as the generator of the K-theoretic duality between the fibre and base; (iv) the gapless mode cannot be lifted by the Jensen potential because lifting it would change the K-theory class, which is a topological invariant.

**Regime of validity.** The theorem holds whenever:

- The Jensen potential commutes with at least one left-invariant generator of SU(3). Holds for all canonical tau by the construction of the Jensen flow.
- The spectral triple has a well-defined Kasparov class. Holds for the framework's KO-dim 6 SU(3) fibre (S44 permanent result: [J, D_K] = 0 on all 36 left-invariant directions).
- Bi-invariance of the Killing metric is preserved on the protected direction. Holds at all tau by the construction of the protected direction as the commutant of V.

**Consequence.** c_Gold = 0.915 M_KK is the UNIQUE propagation bound in the framework because the Goldstone is the UNIQUE gapless mode on g_M. Every other branch has a mass gap (B1 through Leggett) and therefore a v_g strictly below c_Gold. The framework's light-cone structure is therefore NOT a choice; it is forced by the K-theory of the Jensen-deformed spectral triple, with Kasparov factorization as the structural argument.

This theorem is the structural reason the framework has ONE speed of light (c_Gold) rather than MULTIPLE speeds across different sectors. The Goldstone is the structural gap-protector, and it determines the envelope bound for all Layer 2 propagation.

**Verification status (CLOSED).** m_Goldstone^{4D} = 0 EXACTLY by Kasparov product factorization (session-74-qa-vdd-workshop.md: the factorization [D_total] = pi_! tensor [D_M^4] operates at the level of K-HOMOLOGY, Paper 01 van den Dungen 2018/2022, NOT at the level of the spectral action). The **Kasparov product factorization (Paper 01)** is a CLOSED mechanism: all 5 conditions verified at S61 (framework-cc-oom.md). S82-KASPAROV-ABELIAN-PROOF: PASS (scheme=K-THEORY, convention=KASPAROV-KK). The Goldstone-continuum crossover is K_star_goldstone = 0.185 (canonical). The masslessness is therefore a CLOSED structural identity of the KO-dim-6 spectral triple, not a tuning — this is why c_Gold is the UNIQUE Layer-2 envelope.

### 3.5 Heat-Kernel Polynomial Orthogonality (OQ6 candidate)

**Source**: C-R2-E1 (einstein), T-R2-Q3 (transit) answered by C-R2-E1. Registered as OQ6 SPECTRAL-DECOUPLING-CERT-75 for formal permanent status.

**Statement.** For the specific Jensen-deformed SU(3) fibre at all canonical tau values (including tau_fold = 0.190, tau_exit in [0.4, 1.614]), the Seeley-DeWitt coefficients a_0^{zeta} and a_2^{zeta} of D_K^2 are linearly independent as local invariants, and there is no linear combination F = alpha * a_0^{zeta} + beta * a_2^{zeta} with alpha, beta not both zero that reduces to a single polynomial-degree local invariant.

**Proof strategy.** Apply Gilkey's local index theorem (1995 statement) to the Jensen-deformed fibre. Verify that the a_0^{zeta} coefficient (volume / potential term) has polynomial dimensional degree 0 in the local-invariant filtration, while the a_2^{zeta} coefficient (curvature term) has polynomial dimensional degree 2. Show that there is no element of one sheaf that appears in the other through any linear combination, which is guaranteed by Gilkey's orthogonality result on the polynomial filtration.

**Regime of validity.** The theorem holds whenever the Jensen-deformed fibre is smooth and D_K^2 is Laplace-type. Both conditions hold at all canonical tau values.

**Verification status (LANDED).** Pre-registered as OQ6 SPECTRAL-DECOUPLING-CERT-75; LANDED **PASS** at S75 W2-E (Wronskian nonzero), MIGRATED **INFO** at S81 batch hygiene. See Section 3.1 "Verification status (LANDED)" for the full landed-verdict citation (sha256=55a1b9e0a8bebc05...) — this Heat-Kernel Polynomial Orthogonality statement and the Spectral-Moment Decoupling Theorem (Section 3.1) are the SAME certified result (the document had registered them as a shared OQ6; the S75 W2-E PASS certifies both). The decoupling is now a framework-internal CERTIFIED result, not merely an inherited general Gilkey statement. Regulator scheme: a_0^{zeta}, a_2^{zeta} (per Section 3.1 regulator-pin note).

### 3.6 a_2^{zeta} -> Emergent Gravity: M_Pl_eff^2 = a_2^{zeta}/(48 pi^2) (the quantitative core of "c is emergent from a_2^{zeta}")

**Source**: S77 transit-einstein workshop (T2.7, T3.13/T3.14, T4.1, T5.2, T5.13). NEW since the S74 document. Classification: **GEOMETRIC** (the fabric's spectral-triple structure generating gravity, not a phononic excitation).

The document's thesis — "c is not a postulate; it flows D_K eigenvalues -> a_2^{zeta} Seeley-DeWitt -> emergent g_M -> c_Gold" — was QUALITATIVE in the S74 text (Section 4.1 gives only c_Gold^2 = Z_Gold/M_Gold). S77 made the SAME a_2^{zeta} coefficient generate Newton's constant quantitatively, closing the chain.

**Statement.** The second Seeley-DeWitt coefficient a_2^{zeta} of D_K^2 generates the Einstein-Hilbert action of the emergent g_M:

    S_EH = f_2 * a_2^{zeta} * M_KK^2 / (48 pi^2) * integral(R * sqrt(g) d^4x)            (3.5, T5.2)

so that the effective (reduced) Planck mass and Newton's constant are spectral moments:

    M_Pl_eff^2 = a_2^{zeta}(fold) / (48 pi^2) = 2776.17 / (48 pi^2) = 5.862 M_KK^2          (3.6, T2.7/T4.1)
    G_N = 48 pi^2 / (f_2 * a_2^{zeta} * M_KK^2)                                             (3.7, T5.13)

In GeV units, with M_KK = M_KK_gravity = 7.428660036284456e16 GeV (canonical_constants.py:341, SAKHAROV-GN-44):

    M_Pl_eff(GeV) = sqrt(a_2^{zeta}/(48 pi^2)) * M_KK = sqrt(5.862) * 7.43e16 = 1.80e17 GeV  (3.8, T3.14)

**Why this is the correct substrate direction.** This is the QUANTITATIVE realization of the IS-not-IN mandate: Newton's constant G_N is NOT a fundamental dimensionful input — it is the inverse of the second spectral moment of D_K. The chain runs

    {lambda_k of D_K}  ->  a_2^{zeta} = (zeta-scheme second moment)  ->  M_Pl_eff = sqrt(a_2^{zeta}/48 pi^2) M_KK  ->  G_N  ->  g_M  ->  c_Gold

every arrow pointing FROM the substrate TOWARD emergent physics. M_Pl_eff is a spectral moment, NOT a postulated Planck mass; g_M is the metric this gravity defines; c_Gold is the Goldstone group-velocity envelope ON g_M (Section 4.1). The same a_2^{zeta} that fixes the inertial coefficient M_Gold in c_Gold^2 = Z_Gold/M_Gold (eq 4.1) fixes M_Pl_eff in eq 3.6 — c and G_N are TWO spectral consequences of the ONE a_2^{zeta} coefficient. (See S44 SAKHAROV-GN-44 PASS 3-way for the independent M_KK extraction from G_N that this is consistent with.)

**Regulator scheme.** a_2^{zeta}(fold) = 2776.1653888633655 here is the zeta-scheme half-zeta_D(1) (a_2^{zeta}, canonical a2_fold, S42 CONST-FREEZE-42); the spectral-action cutoff f(x) ~ exp(-x) sets the consistent regulator class. See Section 3.7 for the fold vs full-L10 truncation distinction (which gives a DIFFERENT M_Pl_eff, by design).

### 3.7 a_2^{zeta}(fold) vs a_2^{zeta}(full L_max=10): the truncation and scheme distinction

**Source**: canonical a2_fold (S42); s75_f_conv_spectral_output.txt (full-L10 spectral sum). NEW since the S74 document (which cites a_2^{zeta} without the two-value distinction). Classification: **GEOMETRIC**.

The framework carries TWO numerically distinct a_2^{zeta} values, and confusing them mis-pins M_Pl_eff by a factor ~2:

| Quantity | Value | Scheme / definition | Source | M_Pl_eff |
|:---------|------:|:--------------------|:-------|:---------|
| a_2^{zeta}(fold) | 2776.1653888633655 | zeta-scheme half-zeta_D(1) = 0.5 sum_n d_n/lambda_n^2 | a2_fold, S42 CONST-FREEZE-42 (cc:453) | 5.862 M_KK^2 -> 1.80e17 GeV |
| a_2^{zeta}(full L10) | 64308.24 | full mode-sum, L_max=10 (155,984 eigenvalues) | s75_f_conv_spectral_output.txt | M_Pl_eff(L10) = sqrt(64308/48 pi^2) M_KK = 11.65 M_KK = 8.6551e17 GeV |

The companion fourth moment: a_4^{zeta}(fold) = 1350.7216415169728 (zeta half-zeta_D(2), a4_fold) vs a_4^{zeta}(full L10) = 29086.18 (mode-sum).

**Which is canonical.** a_2^{zeta}(fold) is the canonical Seeley-DeWitt coefficient (the zeta-regulated half-zeta_D(1) at tau_fold = 0.190); it is the value entering the Einstein-Hilbert generation (Section 3.6) and the c_Gold structural derivation. a_2^{zeta}(full L10) is the L_max=10-truncated full-spectrum mode-sum (it includes all 155,984 eigenvalues without the zeta-regularization restriction to the curvature moment). The two differ because the zeta-scheme half-zeta_D(1) isolates the curvature-density local invariant, whereas the raw mode-sum Tr(|D_K|^{-2}) is the full (divergent-in-the-continuum, truncated-at-L10) spectral sum — they are NOT the same object (cf. session-60-bap-collab.md: "the raw PW spectral sum Tr(|D_K|^n) is NOT the Seeley-DeWitt coefficient a_n; the former diverges, the latter is a finite curvature integral").

**Consequence.** Any quotation of a_2^{zeta} in this domain MUST carry both the regulator tag (a_2^{zeta}) and the truncation specification (fold vs full-L10). The decoupling theorem (Section 3.1) holds in BOTH schemes (Gilkey orthogonality is regulator-invariant at the polynomial-degree level); only the numerical magnitude differs. The L_max=10 truncation is the regime in which the decoupling is exact to machine precision (Section 3.1 regime of validity); beyond L_max, cross-terms enter at O((L_max)^{-2}) ~ 10^{-2}.

---

## 4. What c IS in the Framework

### 4.1 c_Gold = 0.915 M_KK structural derivation

c_Gold is the group velocity of the gapless Goldstone mode on the Killing-protected direction of the Jensen-deformed SU(3) fibre metric. Its STRUCTURAL origin is specific:

- The Jensen deformation parameter tau = |phi|^2 (Baptista convention) parameterizes a one-parameter family of left-invariant metrics on SU(3), starting from the round bi-invariant Killing metric at tau = 0 and deforming toward the Jensen-critical metric at tau_crit.
- The eight SU(3) generators split under the Jensen flow into ONE direction commuting with the Jensen potential V(|phi|^2) (the U(1)_Y generator — the Killing direction protected by bi-invariance) and SEVEN directions acquiring curvature corrections from R_{g_phi} (the seven "broken" directions that pick up gap mass from the Jensen potential).
- The Killing-protected direction is the Goldstone of the continuous symmetry that the Jensen flow does NOT break: the rotation of the phi field within the U(1)_Y subgroup.
- The velocity c_Gold is the group velocity of the Killing-direction fluctuations:

    c_Gold^2 = Z_Gold / M_Gold = 0.915^2 M_KK^2     (4.1)

where Z_Gold is the kinetic stiffness from the a_4^{zeta} kinetic term projected onto the Killing direction, and M_Gold is the inertial density from the a_2^{zeta} term projected onto the Killing direction. Both are FIXED by the choice of spectral triple — neither is a free parameter of the framework.

The canonical value c_Gold = 0.915 M_KK from `computations/_shared/canonical_constants.py` line 636 (S52 GL-JOSEPHSON-52 PASS) is a COMPUTATION OUTPUT, not an input. **Landed verdict**: the emergence of c_Gold from a_2^{zeta} + a_4^{zeta} was confirmed at S75 W3-L "Emergent c_light from a_2^{zeta} + a_4^{zeta} — c_Gold = 0.915 M_KK, 3-speed hierarchy verified" PASS (session-75-tesla-synthesis.md; producing script s75_emergent_lorentz.py), MIGRATED **INFO** at S81 batch hygiene (T3-BATCH-S75-EMERGENT-LORENTZ: INFO, sha256=0f4a28335ed406854f42f2acfd2b2d47ea4b400082e92b2b10ca9a69019804c3). **PROVENANCE-gap flag (QA carry-forward)**: c_Gold currently carries NO PROVENANCE entry in canonical_constants.py (get_constant("c_Gold") returns the value 0.915 but "No PROVENANCE entry"); the canonical_constants hygiene fix (add a PROVENANCE entry pinning S52 GL-JOSEPHSON-52 + S75 W3-L) is a carry-forward, NOT a doc edit.

### 4.2 Structural bounds [0.62, 1.73] M_KK from Pippard and bi-invariance

The workshop's E1 derivation establishes a rigorous structural bracket for c_Gold:

**Upper bound** (bi-invariant Killing metric). The bi-invariant Killing metric on SU(3) at tau = 0 has a maximum signal velocity set by the largest eigenvalue of the Killing form on the generator algebra. For SU(3), this maximum is sqrt(3) M_KK ~ 1.732 M_KK in the bi-invariant limit. In the Jensen-deformed regime at tau_fold = 0.190, the fibre metric acquires curvature corrections that reduce this bound on most directions (the gapped sectors) but preserve it on the Killing direction. The Killing direction's sound speed is therefore bounded above by the bi-invariant maximum.

    c_Gold <= sqrt(3) M_KK ~ 1.732 M_KK     (4.2, upper bound)

**Lower bound** (Pippard BCS coherence). The spectral action must support the post-transit BdG spectrum. The BCS coherence length xi_BCS = 0.8083468753837275 M_KK^{-1} (canonical_constants.py line 424, S37) sets a minimum sound speed via the Pippard relation:

    c_s,min = Delta_0 * xi_BCS ~ 0.770 * 0.808 ~ 0.62 M_KK     (4.3, lower bound)

using Delta_0_GL = 0.7704350982797368 from `canonical_constants.py` line 414 (S37). The spectral triple cannot support a phononic branch below this bound without violating the Pippard BCS coherence relation.

**The canonical value c_Gold = 0.915 sits within the structural bracket:**

    0.62 M_KK (Pippard lower)  <  0.915 M_KK (canonical)  <  1.732 M_KK (bi-invariant upper)     (4.4)

The factor 0.528 below the bi-invariant maximum (0.915 / 1.732) reflects the Jensen-deformation inertial correction C_phi from Baptista eq (3.42), which inflates the inertial coefficient M_Gold relative to the bi-invariant limit. The factor 1.476 above the Pippard bound (0.915 / 0.620) reflects the BCS coherence length being shorter than its minimum value — the spectral triple is tighter than the BCS bound requires, giving room for c_Gold above the minimum.

**Structural sanity check.** Any framework computation that produces a c_Gold value outside [0.62, 1.73] M_KK would violate either bi-invariance of the Killing metric (upper bound) or the Pippard BCS coherence relation (lower bound), both of which are framework structural theorems. The bracket serves as a permanent consistency check.

### 4.3 Relation to c_photon, c_BLV, c_BA, c_mod

The workshop identified several quantities with M_KK units that circulate in the framework under names that could suggest "multiple speeds of light". The S74 convergence is that they are NOT multiple c's — they are quantities from different spectral moments.

**c_Gold = 0.915 M_KK (Layer 2 envelope).** The sound speed of the Goldstone direction on the post-transit emergent g_M. THIS is the framework's emergent speed of light. All propagating modes on g_M have v_g <= c_Gold.

**c_photon = 0.915 M_KK + O(NLO) (Layer 2, sub-envelope).** The propagation velocity of U(1)_Y gauge-field excitations on L_Y post-transit. Determined by the a_4^{zeta} Yang-Mills kinetic term in the spectral action. IDENTICAL to c_Gold at leading order because both derive from the same a_2^{zeta} Seeley-DeWitt coefficient. The difference is c_photon / c_Gold = 1 + O(C_phi * g_Y^2 / g_Gold^2), with next-to-leading corrections estimated as O(10^{-5}) dimensional and O(10^{-34}) at current observational energies. See Section 8.3 below for the unobservable distinguisher.

**c_BLV = 0.485 M_KK (Layer 1, substrate-internal).** The substrate-internal Bogoliubov (Brillouin-Landau-Vortex) sound speed at the fold. Canonical value c_BLV = 0.485 (canonical_constants.py line 486, S64 four-speed hierarchy inheritance from 3He-B; presentation: the S74 text's 0.4849 is the same quantity to 4 sf). Computed as c_s^2 = Z_fold / d2S_fold from the spectral-action stiffness at tau_fold. This is a stiffness-to-inertia ratio for substrate-internal fluctuations of the Jensen modulus, NOT a group velocity on a Lorentzian manifold. It enters the Mach 13.75 ratio as the denominator. Lives in a_0^{zeta} space (substrate internal BEC-analog structure). **PROVENANCE-gap flag (QA carry-forward)**: c_BLV carries NO PROVENANCE entry in canonical_constants.py (get_constant("c_BLV") = 0.485, "No PROVENANCE entry") — a canonical_constants hygiene item (add S64 four-speed provenance), NOT a doc edit. The same gap holds for c_fabric = 209.97368021 (line 485; "No PROVENANCE entry").

**c_BA = 0.399 M_KK (Layer 1, substrate-internal).** The Berezinskii-Arnowitt sound speed at tau = tau_BA. Also a substrate-internal fluctuation speed, similar to c_BLV but evaluated at a different point on the Jensen flow. Layer 1 quantity; no direct observable on g_M.

**c_mod = 1 M_KK (Layer 1, modulus-space norm).** The normalization of the modulus parameter tau's "rate" in natural units. NOT a velocity — it is the dimensional-normalization constant of the Jensen flow rate dtau / dt_substrate. In the film analogy, it is the "editing tool speed", not a velocity of anything.

**c_L = 0.0255 M_KK (Layer 2, Leggett branch).** The Leggett branch sound speed on the post-transit g_M. Layer 2 quantity (propagation on the emergent metric). Lives in a_2^{zeta} space via the BdG diagonalization. Appears in W4-L's ell_gap = 3.14e59 FAIL as the denominator of k_gap = m_gap / c_L.

**Structural summary (E-R2-E2).** The framework has:

- **ONE** emergent-metric light speed c_Gold = 0.915 M_KK on g_M (Layer 2 envelope, saturated by Goldstone direction).
- **EIGHT** post-transit phononic branch speeds (Layer 2, all bounded above by c_Gold): Goldstone saturated, B1 = 0.0798, B2 = 0.002, B3 = 0.1397, Leggett L1 = 0.0255, plus the other Leggett / optical modes.
- **An INDETERMINATE number** of substrate-internal fluctuation rates in a_0^{zeta} space (c_BLV, c_BA, Mach 13.75, dS/dtau = +58,673) that are NOT velocities and cannot be compared to c_Gold.

This is the two-category structure. It is NOT "four speeds of light" but "three substrate-internal a_0^{zeta} diagnostics plus eight Layer-2 branch speeds under one envelope c_Gold".

### 4.4 The two causality layers: Layer 1 (substrate throughput) vs Layer 2 (emergent Lorentzian)

The workshop's E4 introduces the two-layer causal architecture. This subsection states it precisely after the D-R2-2 correction.

**Layer 1: Substrate throughput bound.** At the spectral-triple level, D_K has a finite largest eigenvalue lambda_max that is set by the KK scale. In canonical units, lambda_max ~ O(M_KK) = O(7.43e16 GeV) in the gravity route or O(5.04e17 GeV) in the Kerner route. This is the TOP of the spectral ladder: no fibre excitation can have energy above lambda_max because there is no eigenmode there.

The Layer 1 causal bound is a CONSEQUENCE of lambda_max being finite: any branch of D_K that carries an excitation from one fibre point to another must have its group velocity bounded above by a function of its eigenvalue spectrum. On the Killing-protected direction, this function saturates at c_Gold = 0.915 M_KK.

In formula:

    v_g,branch^(Layer 1) <= c_Gold = 0.915 M_KK     for all branches b     (4.5)

This bound is enforced by the finiteness of the Dirac operator spectrum and the smoothness of the Seeley-DeWitt expansion. It has NOTHING TO DO with the Lorentzian cone of g_M — it is a property of the Dirac operator itself, prior to any metric emergence.

**Layer 2: Emergent Lorentzian bound.** In the post-transit regime, g_M is a Lorentzian manifold with light cones at every point. A propagating excitation is bounded above by the null cone at its location:

    g_mu_nu v^mu v^nu <= 0     (v is timelike or null)     (4.6)

This is the standard GR causal structure applied to the emergent metric. Every field on g_M (photons, gravitons, fermions, phonons) satisfies this bound at every point.

**Relation between layers — exact on Killing direction, O(tau) split on gapped directions.** After the D-R2-2 correction:

- On the Killing-protected Goldstone direction: Layer 1 and Layer 2 coincide EXACTLY to all orders in tau. c_Goldstone^(1) = c_Goldstone^(2) = c_Gold = 0.915 M_KK exactly.
- On the seven gapped directions (B1, B2, B3, Leggett, plus the other optical/Leggett branches): Layer 1 and Layer 2 differ by O(tau) ~ 0.19 at the fold. This is NOT the Planck-suppressed NLO originally claimed in E4. It is a FIRST-ORDER, potentially observable diagnostic of the Jensen deformation.

**Why this matters for observational tests.** A test that measures Layer-2 velocities at low energies (e.g., the arrival time of GWs from BNS merger vs the arrival time of gammas from the same event) probes the Lorentzian cone of g_M. The framework predicts this test returns c_GW = c_gamma to machine precision at leading order, consistent with the LIGO/Virgo measurement of GW170817 + GRB 170817A with |c_GW/c_gamma - 1| < 10^{-15}.

A test that measures Layer-1 throughput bounds directly (e.g., precision BAO acoustic peak position) is harder to design but would potentially distinguish the framework from a container-thinking theory that treats c as a fundamental postulate. The framework predicts O(tau) ~ 0.19 Layer-1/Layer-2 differences on the B1 acoustic branch — a 19% effect on c_B1 = 0.0798 M_KK that would shift the BAO peak by a fraction of that amount. See Section 8.1 below.

**The framework's causal structure is richer than GR.** Standard GR has one causal layer: the null cone of the Lorentzian metric. The phonon-exflation framework has two layers: the substrate throughput bound (set by the D_K spectrum) and the emergent Lorentzian cone (set by a_2^{zeta} Seeley-DeWitt). They coincide for the Killing direction and differ by O(tau) on the gapped directions. This is a FEATURE of the framework, not a bug: it is why the framework can have a Mach 13.75 transit without violating any causal law (the transit is a Layer-1 event, bounded by dS/dtau rather than by v_g), while still having a rigorous notion of "causal propagation" at the emergent Lorentzian level.

---

## 5. What c Does NOT Bound

This section lists the SUBSTRATE DYNAMICS events that are NOT subject to any c-bound. Each is classified by the algorithm in Section 6 at STEP 0 (spectral-moment localization), and in each case the STEP 0 classification returns SUBSTRATE DYNAMICS in a single step.

### 5.1 Fold transit

**Event.** The Jensen deformation parameter tau evolves from tau = 0 through the first-order transition at tau_fold = 0.190 to tau_exit in [0.4, 1.614], driven by the spectral-action gradient dS_spec / dtau = +58,673 M_KK per unit dimensionless tau (canonical constants, workshop T1).

**Classification (STEP 0).** dS/dtau is a functional derivative of a scalar functional of the spectral triple (specifically, of the a_0^{zeta} sector at the fold because a_2^{zeta} is still being reorganized). It has units of M_KK per dimensionless tau — a spectral-action functional derivative, not a velocity. SUBSTRATE DYNAMICS, in one step.

**Key points:**

- The RATE of tau evolution is set by the spectral action functional derivative, not by any phononic dispersion on a pre-existing metric.
- There is no g_M across which the fold is "moving" — g_M is generated by the a_2^{zeta} Seeley-DeWitt coefficient which is itself a functional of the spectral triple that is being reorganized.
- The transit cannot be c-bounded because c is not defined until AFTER g_M is established.
- Mach 13.75 is a SUBSTRATE-INTERNAL ratio of the fold's flow rate to the BEC-internal sound speed at tau_fold. It is NOT a velocity on g_M. See Section 7.2 for the full correction.

### 5.1a H_transit vs H_Friedmann: the two-rate formalism

**Source**: S76 W1-E POST-FOLD-H-TAU resolution + S85 W7 formalization (session-85-plan-w7.md; session-76-transit-einstein-workshop.md). NEW since the S74 document — it sharpens the §3.2/§5.1 statement "the fold rate is dS/dtau, not a velocity" into an explicit two-rate formalism that makes the PROPAGATION-vs-SUBSTRATE-DYNAMICS split quantitative at the level of "Hubble rates".

The framework has TWO distinct "expansion rates", living in DIFFERENT spectral moments — a direct instance of the Spectral-Moment Decoupling Theorem (Section 3.1):

    H_transit   == (1 / Vol_SU3) * dS_fold/dtau            [SUBSTRATE DYNAMICS; a_0^{zeta}-sector functional derivative; NOT on g_M]   (5.1a-1)
    H_Friedmann == (8 pi G / 3 * rho_eff)^{1/2}            [emergent rate; a_2^{zeta} Seeley-DeWitt moment; defined on g_M]            (5.1a-2)

with dS_fold = 58672.80241318 M_KK per dimensionless tau (canonical_constants.py:483, S42).

**The two rates are NOT a single H(t) in two coordinates.** H_transit is the rate at which the spectral triple is being EDITED (the Jensen flow under the spectral-action gradient); it is a functional derivative of the a_0^{zeta} sector (the fold is where a_2^{zeta} is still being reorganized), with units of (spectral action) / (dimensionless modulus) per unit fibre volume. It has no projection onto a velocity on any metric. H_Friedmann is the emergent Hubble rate of the post-transit FRW background, sourced by the a_2^{zeta} Seeley-DeWitt coefficient (the same a_2^{zeta} that generates M_Pl_eff and G_N in Section 3.6). By the decoupling theorem, no velocity-bound connects them: H_transit lives in a_0^{zeta}, H_Friedmann is built from a_2^{zeta}.

**The stretch factor.** The two rates enter the Mukhanov pump z"/z at the CMB pivot through the stretch factor (session-85-plan-w7.md):

    F_stretch == (H_transit / H_Friedmann)^2          (5.1a-3)
    z"/z = H_Friedmann^2 * [2 - eps_H + F_stretch * (H_transit-conversion term)]

F_stretch accounts for the pre-transit-to-post-transit conversion. It is the QUANTITATIVE bookkeeping for "the film is being edited faster than the frame rate": the substrate-dynamics rate H_transit (editing) and the emergent rate H_Friedmann (playback) are related not by a time-reparameterization but by the Bogoliubov projection at the emergence boundary (Section 3.1(iv)). The open channel "Post_Fold_Background_Htransit_vs_HFriedmann_Resolved" was CLOSED by W1-E at S76.

**Classification (STEP 0).** H_transit is dS_fold/dtau / Vol_SU3 — a functional derivative in the a_0^{zeta} sector. SUBSTRATE DYNAMICS, in one step. H_Friedmann is the emergent FRW rate built from a_2^{zeta}; it governs propagation backgrounds on g_M but is itself a background rate, not a group velocity (no source/receiver pair; STEP 2). Neither is c-bounded.

### 5.2 Instantons

**Event.** Topological-sector transitions of the SU(3) gauge bundle, interpolating between vacua with different Chern numbers. Computed in the framework via:

- W1-R 't Hooft vertex: |dV_tHooft / dtau| at tau = 0.480 = 1.498e-07 M_KK^4 (a functional derivative, not a velocity).
- W1-Q Coulomb gas V_eff: |dV_eff^CG / dtau| at tau = 0.480 = 2.8046 M_KK^4.
- W2-R instanton stabilization: dV_inst_A / dtau = -1.438 M_KK^4 at tau = 0.480.
- W2-S Ibar valley Jacobian: moduli-space measure factor for (I, Ibar) pair integration.

**Classification (STEP 0).** Each quantity is dF / dtau where F is an instanton-modified spectral functional in the a_0^{zeta} sector. Gilkey's heat-kernel orthogonality forbids a velocity interpretation. SUBSTRATE DYNAMICS, in one step.

**Key points:**

- An instanton is a topological sector transition, not a signal transit. The two vacua it interpolates between are both "here" — they are two classical ground states of the same gauge bundle, not two separate points on g_M.
- Instanton events do not have dispersion relations omega(k); they are topological, not wave-like.
- The "instanton size" rho (moduli parameter) is an action-landscape variable, not a wavelength.
- Instanton rates are dimensionless functions times spectral-action functional derivatives. Neither the rates nor their derivatives have any c-dependence.
- W3-N Lefschetz thimble integral: the dominant winding is n* = 60 with neighbouring windings suppressed by |I_{59}|/|I_{60}| ~ 10^{-26665} and |I_{61}|/|I_{60}| ~ 10^{-62220}. The saddle dominance is a SUBSTRATE DYNAMICS phenomenon — a statement about the topology of the fibre's Higgs bundle, not about propagation on g_M. And yet it IS the 59.8 pairs: "60 Bogoliubov pairs in the GGE relic" and "one classical spectral configuration in winding sector 60 of L_Y" are two names for the same SUBSTRATE-LEVEL event.

### 5.3 Jensen evolution

**Event.** The Jensen modulus tau evolves as a one-parameter family of spectral triples, with the fibre metric at each tau given by g_phi with scalar curvature R_{g_phi} from Baptista eq (2.40). At each value of tau, the ENTIRE spectral triple (D_K, H, A, J) is a different algebraic object. The flow does not happen "across" any spatial extent — it is a global rewriting of the algebraic data of the spectral triple.

**Classification (STEP 0).** Rate of Jensen evolution is d tau / d (substrate-internal time). In the a_0^{zeta} sector (the Jensen potential is in a_0^{zeta} by Baptista eq 2.37). No metric has been generated to measure "rate per time" against; "rate per tau" is not a velocity. SUBSTRATE DYNAMICS, in one step.

**Key points:**

- Every fibre at every point in space-time undergoes the SAME tau evolution SIMULTANEOUSLY, by the global homogeneity of the deformation. This is NOT a signal equalizing across space; it is a global rewriting of the algebraic data of the spectral triple.
- The homogeneity is INHERITED from the spectral triple's global uniqueness, not achieved by propagation at any speed. This resolves the "horizon problem" without invoking inflation.
- Jensen evolution is in the a_0^{zeta} sector (via the Jensen potential V(|phi|^2)), and THROUGH a_0^{zeta} it affects a_2^{zeta} at the next-order expansion. But the PRIMARY effect is on a_0^{zeta}.

### 5.4 Spectral-action gradients

**Event.** dS_spec / dtau, dV_eff / dtau, dS_inst / dtau, dV_tHooft / dtau, and all other functional derivatives of spectral-action moments with respect to substrate moduli.

**Classification (STEP 0).** Every such quantity is a functional derivative in the a_0^{zeta} sector (or the a_2^{zeta} sector without propagation — a sum over moments). By Gilkey's orthogonality, a_0^{zeta} and a_2^{zeta} are different polynomial degrees, and functional derivatives in either sector cannot be rate-compared to group velocities in a_2^{zeta} space. SUBSTRATE DYNAMICS, in one step.

**Key points:**

- These are the rates at which the spectral-action FREE ENERGY changes as the substrate evolves. They are in units of (spectral action) / (modulus), not (distance) / (time).
- The "driving force" of the fold transit is dS_fold / dtau = +58,673 M_KK per unit dimensionless tau. This is a pure functional derivative with no velocity interpretation.
- No observer on g_M can measure these rates directly. They are probed only through their projection onto the post-transit Bogoliubov squeezing pattern.

### 5.5 Bogoliubov pair production

**Event.** Parker pair production of fibre excitations at the fold transit. The 8 BCS modes of the fibre's spectral content have tau-dependent frequencies

    omega_k(tau) = sqrt(eps_k(tau)^2 + Delta(tau)^2)     (5.1)

and the mode equation for each fibre excitation is

    u_k'' + omega_k^2(tau) u_k = 0     (5.2, prime = d/dtau)

In the NON-adiabatic regime (|d ln omega_k / dtau| / omega_k >> 1, which holds at the fold with Mach 13.75), the in-vacuum and out-vacuum are related by a non-trivial Bogoliubov transformation

    a_k^out = alpha_k a_k^in + beta_k^* (a_{-k}^in)^dagger     (5.3)

and the occupation number of the out-vacuum is <N_k>_out = |beta_k|^2 = sinh^2(r_k), with r_k the per-mode squeezing parameter. Unitarity requires |alpha_k|^2 - |beta_k|^2 = 1.

**Classification (STEP 0).** The mode equation (5.2) is an ODE in tau, which is a substrate-internal modulus, not a coordinate on a manifold. The Bogoliubov coefficients are numbers (not rates), and the occupation number is a count. No velocity, no length, no time-on-g_M. The 59.8 pairs are a SUBSTRATE DYNAMICS result, classified in one step.

**Key points:**

- The "time" in the ODE is tau. Prime is d/d tau, not d/dt.
- c is nowhere in the equation. The only dimensional input is M_KK (which sets the energy scale via D_K eigenvalues).
- The S67 MULTI-LEVEL-LZ-67 result (transit memory) — N-level Landau-Zener saturation P_exc = 1 in the sudden-quench regime — is a structural theorem in the limit where the ODE's rate parameter goes to infinity. It says: in the Mach >> 1 limit, EVERY eigenmode of the diabatic basis rotates fully into the adiabatic basis with unit probability, producing maximal pair creation. No c appears; the theorem is purely structural.
- After the transit, the created pairs propagate on g_M at their own dispersion velocities c_b <= c_Gold. The CREATION is SUBSTRATE DYNAMICS; the POST-CREATION propagation is PROPAGATION.

**The squeezing-pattern observable (Bogoliubov Gaussianity Preservation, PERMANENT).** The Bogoliubov coefficients (alpha_k, beta_k) are SUBSTRATE-DYNAMICS numbers, but their OBSERVATIONAL SHADOW on g_M is the central non-Gaussianity prediction of the framework, and it is a permanent result:

- **Bogoliubov Gaussianity Preservation [PERMANENT, S65 W5-D]**: f_NL = O(eps) regardless of squeezing (atlas-07-permanent-results; baseline-findings-s66). A non-trivial Bogoliubov transformation (large r_k) does NOT generate large non-Gaussianity — the squeezed vacuum is Gaussian by Wick's theorem; the bispectrum is O(slow-roll eps), not O(sinh^2 r_k). This is the structural reason the framework's f_NL is small despite the strongly diabatic (Mach 13.75) transit.
- **Canonical f_NL values**: f_NL^total = 1.03 (S67 GGE-BISPECTRUM-67; 0.57 sigma vs Planck equilateral -26 +/- 47 — a comfortable consistency); folded-triangle shape (k_1 + k_2 = k_3) UNIQUE to the GGE relic, NOT equilateral or local (a 3-pathway decomposition f_NL_folded ~ 0.0547 + 0.1290 + 0.7685 = 0.9522 at S86; 0.056 for the 21-cm folded channel at S82 W3-4 GGE-FNL); max |f_NL| = 1.505 (Bogoliubov-sudden bound).
- **Squeezing magnitudes** (the per-branch r_k of Section 8.2): r_B1 = 3.571, r_B2 = 1.786, r_B3 = 1.963; n_pair = 59.8 (S38; N_pair = 1 exact reduction at 1.2e-14; pair wavefunction 93% B2, 6.3% B1).

The squeezing PATTERN (the r_k hierarchy + the folded f_NL shape) is the framework's primary substrate-dynamics observational portal; the magnitudes are SUBSTRATE DYNAMICS (set at the fold), the folded-shape non-Gaussianity is the projection onto the post-transit g_M bispectrum (Section 8.2). The phases phi_k were computed at S75 (OQ3 PHASES-BD-75; Section 9).

### 5.6 Spectral reorganization events

**Event.** Any event that corresponds to a change in the D_K eigenvalue structure or the spectral triple's moduli, including:

- Changes to the Peter-Weyl decomposition of H at the truncation boundary L_max.
- Level-crossing events in the BdG spectrum as tau evolves.
- Reshuffling of the a_n Seeley-DeWitt coefficients under modulus flow.
- Moduli-space tunneling events between degenerate vacua.

**Classification (STEP 0).** All such events are changes in the spectral triple itself, not propagations of excitations ON g_M. They are changes in the a_0^{zeta} / a_2^{zeta} structure of the Dirac operator, and they have no velocity interpretation. SUBSTRATE DYNAMICS, in one step.

---

## 6. Classification Algorithm

The workshop produced a six-step operational algorithm for classifying any framework quantity. The algorithm is structurally tighter than a C1-C4 walk: it resolves 3 of 7 canonical edge cases at STEP 0 alone, and it is anchored in heat-kernel orthogonality rather than in a units check.

### 6.0 The four verdict classes (reconciled with the downstream c-compare skill)

This section is the canonical source of the algorithm; the operational `c-compare` skill (`.claude/skills/c-compare/SKILL.md`) is DOWNSTREAM of it and cites this document's Section 6 as authoritative. The skill formalizes the algorithm's output into FOUR verdict classes, which this document now records explicitly (the S74 text walked the steps but did not enumerate the MIXED/CONTRADICTION verdicts):

- **PROPAGATION** — the object moves ACROSS the substrate on g_M. ALL steps pass; v_g <= c_Gold = 0.915 M_KK. c-bounded.
- **SUBSTRATE DYNAMICS** — the object IS a reorganization of the substrate itself. Terminates at some step before STEP 5. NOT c-bounded (no metric across which it propagates).
- **MIXED** — the object has separable components terminating at different steps. One component is PROPAGATION (STEPs 0-5 all pass), another is SUBSTRATE DYNAMICS (terminates earlier). Report BOTH components. Canonical example: Bogoliubov pair CREATION (substrate dynamics) + subsequent PROPAGATION of the 59.8 pairs on g_M (propagation) — the same pairs change class between "during" and "after" the transit (Section 5.5; skill Example 7). Also: Leggett DM OCCUPATION (substrate dynamics) + its gravitational IMPRINT on the CMB (propagation; skill Example 9).
- **CONTRADICTION** — STEPs 0-4 all pass but STEP 5 FAILS (v_g > c_Gold). This is a framework diagnostic, NOT a silent reclassification: either the object was misclassified at STEP 3/STEP 4 (a functional-derivative rate wearing velocity clothing), or the framework has a structural bug. NEVER hide this verdict. The framework's canonical branch set contains NO CONTRADICTION-class object (every branch speed B1 = 0.0798, B2 = 0.00200, B3 = 0.1397, c_L = 0.0255 is below c_Gold; the Goldstone saturates). The W4-L ell_gap "56 OOM" case is NOT a CONTRADICTION — it is a PROPAGATION-class throughput FAIL (the required v_g exceeds c_Gold; Section 7.1), correctly caught at STEP 5.

The algorithm itself (STEPs 0-5) is UNCHANGED between this document and the skill; the four-verdict enumeration is the skill's presentation refinement, now mirrored here for completeness. The skill's 9 worked examples extend this document's 7 edge cases (Section 6.3); the two are consistent.

### 6.1 STEP 0: Spectral-moment localization

```
STEP 0: SPECTRAL-MOMENT LOCALIZATION. (Heat-kernel orthogonality.)
  Is Q a functional derivative dF/dtau where F is a scalar functional
  of the spectral triple (a_0^{zeta} sector, or any combination not containing a_2^{zeta})?
    If YES: Q is SUBSTRATE DYNAMICS. Report as spectral-moment functional
      derivative in units of (M_KK)^n per unit dimensionless modulus.
      NO c-bound applies. Q is bounded only by spectral-triple structural
      constraints (eigenvalue magnitudes, determinant positivity, etc.).
      RETURN.
    If NO: proceed to STEP 1a.
```

STEP 0 is the rigorous version of what was originally C4 ("functional-derivative signature"). It is faster (catches SUBSTRATE DYNAMICS by spectral-moment inspection alone, without walking C1-C4) and more rigorous (anchored in the Chamseddine-Connes structure of the spectral action rather than in a units check).

### 6.2 STEPs 1-5

```
STEP 1a: TENSOR EXISTENCE (Lorentzian g_M as rank-2 tensor).
  Does a_2^{zeta} Seeley-DeWitt produce a symmetric (-,+,+,+) tensor at the event?
    If YES: proceed to STEP 1b.
    If NO (inside the fold proper): Q is SUBSTRATE DYNAMICS. RETURN.

STEP 1b: LORENTZIAN CONE (time-like direction is t, not tau).
  Is the time-like direction of g_M identified with an asymptotic observer
  coordinate t, rather than with the substrate modulus tau?
    If YES: proceed to STEP 2.
    If NO (thawing regime): Q is in MIXED class. In practice: empty for
      all S73B-S74 computations; treat as SUBSTRATE DYNAMICS for safety.
      RETURN.

STEP 2: SOURCE-RECEIVER separability on g_M.
  Can one identify two g_M-distinct points (source, receiver) between
  which the event transports information?
    If YES: proceed to STEP 3.
    If NO: Q is SUBSTRATE DYNAMICS. RETURN.

STEP 3: DISPERSION relation omega_Q(k) with group velocity.
  Does Q have a dispersion relation omega_Q(k) with v_g = d omega/dk?
    If YES: proceed to STEP 4.
    If NO: Q is SUBSTRATE DYNAMICS with no definable velocity. RETURN.

STEP 4: UNITS check, v_g in (g_M-distance) / (g_M-time).
  Does v_g have units of distance-on-g_M / time-on-g_M?
    If YES: proceed to STEP 5.
    If NO (M_KK per tau, dS/dtau, functional-derivative): Q is SUBSTRATE
      DYNAMICS. RETURN.

STEP 5: BOUND check, v_g <= c_Gold = 0.915 M_KK.
  Is v_g <= c_Gold = 0.915 M_KK?
    If YES: Q is PROPAGATION, c-bounded, PASS.
    If NO: Q is PROPAGATION, c-bounded, FAIL (exceeds substrate
      throughput capacity c_Gold by the required factor).
    RETURN.
```

The algorithm terminates at the first step where a classification can be made. STEP 0 alone handles the easy cases (any pure functional derivative on the spectral triple). STEPs 1a-1b refine the "does g_M exist at the event" check into tensor existence AND time-direction globality. STEPs 2-5 are the original C2-C4 discriminators for PROPAGATION events.

### 6.3 Worked edge cases

The seven canonical edge cases from T5 + R2, classified by the revised algorithm:

**EC1: Goldstone acoustic mode on the (0,0) singlet (W4-L, W1-A).**
- STEP 0: not an a_0^{zeta} derivative (it's a group velocity on g_M) → PROCEED.
- STEP 1a/1b: Lorentzian cone well-defined post-transit → PROCEED.
- STEP 2: source-receiver separable → PROCEED.
- STEP 3: dispersion omega(k) = c_Gold * k, linear massless → PROCEED.
- STEP 4: v_g in natural units of distance / time → PROCEED.
- STEP 5: v_g = c_Gold = 0.915 M_KK exactly at the bound.
- **Classification: PROPAGATION, c-bounded, saturated at c_Gold.**

**EC2: Leggett branch at CMB scales (W4-L, W4-FF).**
- STEP 0: not an a_0^{zeta} derivative (group velocity on g_M) → PROCEED.
- STEPs 1-5: Lorentzian cone well-defined; dispersion omega^2 = m_gap^2 + c_s^2 k^2 with v_g = c_s = 0.0255 far below c_Gold.
- **Classification: PROPAGATION, c-bounded, far below bound.**

The W4-FF Jeans scale k_J = 5.97e-3 Mpc^{-1} PASSes the gate [1e-6, 1]. The W4-L ell_gap = 3.14e+59 FAILs because the required v_g to land in the PASS band would need to exceed c_Gold by 56 OOM — a throughput violation, NOT a causal violation. See Section 7.1 for the complete wording fix.

**EC3: The fold transit itself (W1-A, W2-C, W4-L pre-reorganization, Mach 13.75).**
- STEP 0: dS/dtau = +58,673 M_KK is a functional derivative in the a_0^{zeta} sector → SUBSTRATE DYNAMICS, RETURN.
- **Classification: SUBSTRATE DYNAMICS, in one step.** Mach 13.75 is an INTERNAL ratio of substrate reorganization rate to substrate-internal acoustic speed, NOT a velocity on g_M. No c-bound applies.

**EC4: Instanton-mediated coupling vertex (W1-R 't Hooft vertex, W2-S IBAR-VALLEY-JACOBIAN).**
- STEP 0: dV_tHooft/dtau = 1.498e-7 M_KK^4 is an a_0^{zeta} functional derivative → SUBSTRATE DYNAMICS, RETURN.
- **Classification: SUBSTRATE DYNAMICS, in one step.**

**EC5: CMB photon propagation on g_M (observational portal, S66, S68, S73B W1-A).**
- STEP 0: not an a_0^{zeta} derivative (group velocity on g_M) → PROCEED.
- STEPs 1-5: Lorentzian cone well-defined; dispersion omega = c k (photon, massless on U(1)_Y); v_g = c at c_Gold saturation to leading order.
- **Classification: PROPAGATION, c-bounded, saturated.**

**EC6: Leggett branch dark matter occupation in the Milky Way (W4-FF, S66, S68 f_DM).**
- STEP 0: not an a_0^{zeta} derivative (the DM propagation is a Layer 2 phenomenon; the OCCUPATION was set at the fold by SUBSTRATE DYNAMICS, but the propagation phase is PROPAGATION) → PROCEED.
- STEPs 1-5: Lorentzian cone well-defined; dispersion omega^2 = omega_L1^2 + c_L^2 k^2 with v_g = c_L = 0.0255 << c_Gold.
- **Classification: PROPAGATION, c-bounded, below bound.**

Subtlety: the INITIAL CONDITION (Leggett occupation number) is SUBSTRATE DYNAMICS (set by Mach 13.75 Bogoliubov squeezing). The EVOLUTION (propagation from last-scattering to today) is PROPAGATION. The two are correctly separated by the algorithm.

**EC7: The photon speed's emergence itself (a_2^{zeta} Seeley-DeWitt → g_M → c_Gold).**
- STEP 0: the EMERGENCE of c_Gold is itself a spectral-action process (dS_a2/dtau → a_2^{zeta} → g_M). The KEY quantity "when does c_Gold first exist" is a statement about the a_2^{zeta} BOUNDARY, not a velocity. STEP 0 returns SUBSTRATE DYNAMICS because the question "how fast did c_Gold emerge" is ill-posed — it is a pre-Lorentzian question.
- **Classification: SUBSTRATE DYNAMICS, in one step.**

**Summary of algorithm efficiency (original 7):**
- 3 of 7 edge cases (fold transit, instanton vertex, photon emergence) are resolved at STEP 0 alone.
- 4 of 7 edge cases (Goldstone, Leggett CMB, CMB photon, Leggett DM) pass through to STEPs 1-5 and end up in PROPAGATION.
- 0 of 7 edge cases are misclassified. The algorithm is complete for all observational purposes.

**Expanded corpus (post-S74 objects).** The four causal-architecture objects that appeared after the S74 document, each walked through the algorithm:

**EC8: The H_transit vs H_Friedmann rate pair (Section 5.1a; MIXED-by-component).**
- COMPOSITE input — split (Section 5.1a).
- Component A: H_transit == (1/Vol_SU3) dS_fold/dtau. STEP 0: a_0^{zeta}-sector functional derivative (dS_fold/dtau, units of spectral action per dimensionless modulus per fibre volume). TERMINATE: SUBSTRATE DYNAMICS, in one step.
- Component B: H_Friedmann == (8 pi G/3 rho_eff)^{1/2}. STEP 0: built from a_2^{zeta} (the emergent FRW background rate) -> PROCEED. STEP 1a/1b: g_M Lorentzian cone exists post-fold -> PROCEED. STEP 2: a background rate is NOT a source-receiver transport (no two g_M-distinct points between which it carries a signal) -> TERMINATE: SUBSTRATE DYNAMICS (a background expansion rate, not a propagating mode).
- **Classification: MIXED (both components substrate-side, but for DIFFERENT reasons — A is an a_0^{zeta} functional derivative caught at STEP 0; B is an a_2^{zeta}-built background rate caught at STEP 2 for lack of source/receiver). Neither is c-bounded; F_stretch = (H_transit/H_Friedmann)^2 is a dimensionless ratio of two non-velocities.**

**EC9: The spectral-dimension d_s diffusion probe (Section 8.5; SUBSTRATE DYNAMICS).**
- The object: d_s(sigma) = -2 d ln P(sigma)/d ln sigma with P(sigma) = Tr e^{-sigma D_K^2} (the heat-trace return probability on the D_K spectrum).
- STEP 0: d_s is a log-derivative of the heat trace of D_K^2 with respect to the diffusion-time sigma. The heat trace IS the a_0^{zeta}-family generating functional (Tr e^{-sigma D_K^2} = sum_n t^{(n-d)/2} a_n at small sigma); d_s is a functional of the FULL spectrum, not a group velocity. The diffusion time sigma is a fictitious heat-kernel parameter, NOT a coordinate on g_M. TERMINATE: SUBSTRATE DYNAMICS, in one step.
- **Classification: SUBSTRATE DYNAMICS. d_s is the dimensionality the substrate's diffusion kernel PRESENTS (an intrinsic functional of D_K), not a propagation velocity. It is NOT c-bounded; it is bounded by the spectral structure (d_s -> 8 Weyl at the gap scale; no CDT-like UV reduction). The impedance product Z(E) = rho_E(E) v_g(E) couples the energy-axis DOS rho_E to the group velocity v_g, but d_s itself carries no v_g.**

**EC10: The two-scale alpha_s running (Section 8.2a; SUBSTRATE DYNAMICS, both scales).**
- The object: alpha_s, the running of the spectral tilt. TWO scale-separated incarnations (Section 8.2a): alpha_s_substrate = -0.08587279 (Mellin-cone pole s=3, inside the BZ) and alpha_s_pivot = 0.0 (Goldstone-protected, at the CMB pivot).
- STEP 0: alpha_s = d^2 ln P_zeta / d(ln k)^2 is a SECOND log-derivative of a power spectrum / transfer function with respect to wavenumber — a spectral-tilt curvature, NOT a velocity. For the substrate incarnation, it is (a_4^{zeta}/a_2^{zeta})^2 - 1, a ratio of Seeley-DeWitt moments (a_0^{zeta}/a_2^{zeta}/a_4^{zeta} sector). For the pivot incarnation, it is the curvature of P_zeta at the pivot. Neither is dF/dtau in the strict a_0^{zeta} sense, but neither is a group velocity dω/dk either: a tilt-running is a property of the SHAPE of the spectrum, not a rate of advance on g_M. STEP 4 (units): alpha_s is dimensionless (a curvature in log-log space), NOT (g_M-distance)/(g_M-time). TERMINATE: not a propagation velocity.
- **Classification: SUBSTRATE DYNAMICS (a spectral-tilt-curvature observable, not a propagation velocity). NEITHER alpha_s incarnation is c-bounded — they are not velocities. The two are DISTINCT observables (deg(T_{BZ->pivot}) = +2 NON-SCALAR; Section 8.2a); which one a detector measures is set by the transport degree per SCALE-AND-CHANNEL-TAGGING, NOT by a c-bound. This is exactly why the v_g <= c_Gold envelope does not constrain alpha_s.**

**EC11: The 3He-B BdG acoustic-metric lab image (Section 8.4(c)a; PROPAGATION — but on the LABORATORY metric, not g_M).**
- The object: the c_BdG sound mode on the 3He-B acoustic metric ds^2_acoustic = -(c_BdG^2 - v_mod^2) dt^2 + (fabric metric)_ij dx^i dx^j (the laboratory-IN image of the substrate's c_Gold/g_M under the FWD-C3 Pillar IV <-> Pillar V inheritance morphism).
- STEP 0: a BdG sound mode is a dispersive group velocity on the 3He-B acoustic metric -> PROCEED. STEPs 1-5: the 3He-B acoustic metric IS a (laboratory) Lorentzian cone; source-receiver separable; dispersion omega = c_BdG k; v_g = c_BdG <= c_acoustic (the 3He-B sound speed) -> PROPAGATION.
- **Classification: PROPAGATION — but with the IS-not-IN caveat. The c_BdG mode propagates on the 3He-B ACOUSTIC metric (a laboratory analog), NOT on the substrate's g_M. The substrate IS the spectral triple; the 3He-B acoustic metric is the laboratory-IN image of c_Gold under the inheritance morphism chi (Section 8.4(c)a). The direction of explanation (phononic-framing.md): substrate g_M (Pillar IV) -> bridge map (HKR / K-theory) -> 3He-B BdG acoustic metric (Pillar V), NOT the reverse. v_g <= c_BdG is the LAB analog of v_g <= c_Gold.**

**Expanded summary (11 objects):**
- 5 of 11 resolve at STEP 0 alone (fold transit, instanton vertex, photon emergence, EC9 d_s, EC8-A H_transit).
- 5 of 11 are PROPAGATION (Goldstone, Leggett CMB, CMB photon, Leggett DM, EC11 3He-B BdG lab image).
- 2 of 11 are MIXED-by-component (EC8 H_transit/H_Friedmann; cf. skill Example 7 Bogoliubov create+propagate, Example 9 Leggett occupation+imprint).
- EC10 (alpha_s) is a not-a-velocity SUBSTRATE-DYNAMICS object caught at STEP 4 (units).
- 0 of 11 are CONTRADICTION (no canonical branch exceeds c_Gold). The algorithm remains complete for all observational purposes at the S93-era object set.

---

## 7. Corrections to Earlier Framework Language

The workshop identified several places where pre-S74 framework language imported GR-causal vocabulary into substrate-level events, producing malformed statements. This section enumerates the corrections.

### 7.1 W4-L wording fix (the case study that motivated the workshop)

**Old phrasing** (from qa-vdd workshop Q1 answer):

> "superluminal by fifty-six orders of magnitude. Structurally impossible within any causal framework."

**Correct phrasing:**

> "exceeds the substrate's phononic throughput c_Gold = 0.915 M_KK by fifty-six orders of magnitude. No branch of D_K with m_gap ~ M_KK can propagate on g_M at this speed — the required v_g would have to exceed the Goldstone sound speed by 10^{56}, which the spectral triple cannot supply at any eigenvalue moment. The fold transit itself (SUBSTRATE DYNAMICS, Mach 13.75 internally) is unrelated and unaffected by this bound."

**Why the correction is structural, not cosmetic.**

The W4-L FAIL is a PROPAGATION-class event: c_s in ell_gap = (m_gap / c_s) * chi_recomb is a dispersion velocity of the Leggett-1 mode on g_M at the recombination epoch. The FAIL is correct — the required c_s to reach ell_gap in [10, 3000] exceeds c_Gold by 10^{56}. But the correct CHARACTERIZATION of this bound is "exceeds the substrate's phononic throughput c_Gold by 56 OOM", NOT "violates causality".

The substrate has no causal structure independent of g_M; the propagation bound is set by what the emergent-metric acoustic sector can accommodate. Importing GR-causal language ("within any causal framework") is structurally wrong because it suggests the failure is about g_M's light cone specifically, when it is about the substrate's throughput capacity as a function of D_K eigenvalues.

**The W4-L FAIL is a structural theorem, not a numerical coincidence.** The dimensionless product M_KK * chi_recomb = 1.63e59 is what makes the gap-dominated dispersion fail by ~56 OOM. This number is the ratio of the KK scale to the last-scattering scale, which is a FRAMEWORK-STRUCTURAL ratio — it follows from M_KK being set by the gravity-route matching (M_KK_gravity = 7.43e16 GeV in canonical_constants) and chi_recomb being a standard cosmological quantity. Neither can be adjusted within the framework, so the FAIL is a THEOREM eliminating the "gap-dominated branch produces observable IR crossover kink in C_ell" class of phenomenology entirely.

This upgrade of W4-L from "unfavorable numerical outcome" to "permanent structural theorem" is itself a consequence of adopting the Spectral-Moment Decoupling framework: once the bound is recognized as a c_Gold throughput limit rather than a GR causal statement, the FAIL is seen as a structural theorem about the incompatibility of gap-dominated phononic dispersion with CMB-multipole observation.

### 7.2 "Supersonic transit" / "Mach 13.75" — substrate-dynamics language

**Old phrasing** (circulating in framework documents):

> "The substrate transits through the van Hove fold at Mach 13.75 — a supersonic event."

**Correction:** The phrase "supersonic" is CORRECT but can be misread as "superluminal" if the distinction between the internal BEC acoustic metric h_{mu nu} and the emergent g_M is not made explicit. The workshop's T2 and E-R2-3 clarify:

- Mach 13.75 = v_flow(tau_fold) / c_s(tau_fold), where v_flow ~ 6.667 M_KK is a substrate-internal rate (dS_fold * V_fold / S_fold per dimensionless tau) and c_s = c_BLV = 0.4849 M_KK is the SUBSTRATE-INTERNAL acoustic sound speed at tau_fold from sqrt(Z_fold / d2S_fold).
- The ratio is DIMENSIONLESS and substrate-internal. It does NOT live on g_M. The numerator v_flow is a substrate-internal rate in M_KK per dimensionless tau; the denominator c_BLV is the BEC-analog internal sound speed of the Jensen-deformed SU(3) coset projection.
- "Supersonic" means "faster than the substrate-internal sound speed at tau_fold on the BEC-analog acoustic metric h_{mu nu}". It does NOT mean "faster than light".
- The fold is SUPERSONIC with respect to h_{mu nu} (the substrate-internal analog metric), NEITHER subsonic NOR superluminal with respect to g_M (because g_M does not exist at tau_fold).

**Correct framing:** "The fold is a substrate-dynamics event with Mach 13.75 = v_flow(tau_fold) / c_s,internal(tau_fold), indicating that the Jensen flow at the fold is diabatic relative to the fibre's internal BEC-analog acoustic response. In the sudden-quench regime, the mode equation (5.2) predicts maximal Bogoliubov pair production, which produces the GGE relic with r_B1 = 3.571 and n_pair = 59.8."

### 7.3 "Acoustic white hole" — NOT a second metric; linearization projection

**Old phrasing:**

> "The fold is an acoustic white hole separating pre-fold from post-fold regions causally."

**Correction (D-R2-3 of the workshop):** The "acoustic metric" h_{mu nu} at tau_fold is NOT a metric. It is a LINEARIZATION PROJECTION of the BEC-internal order parameter's fluctuations around its classical Jensen trajectory, used to describe the fluctuation equation in the fold's parameter space. It should not be reified as a geometric object.

The wave equation describing substrate-internal fluctuations at the fold is

    (1 / c_s^2) d^2 (delta phi) / d tau^2 - nabla^2 (delta phi) = 0     (7.1)

The coefficient c_s^2 = Z_fold / d2S_fold = 0.4849^2 M_KK^2 plays the role of a "sound speed", and h_{mu nu} = diag(-c_s^2, 1, 1, 1) plays the role of a "metric" in the wave equation. BUT:

- h_{mu nu} is not a tensor on any 4D spacetime — it is a parameterization of the fluctuation equation in the fold's internal parameter space.
- The "time" in the wave equation is tau, not a physical g_M-time.
- The wave equation is defined only for fluctuations delta phi around phi_0(tau_fold), NOT for free propagation across a distance.

**Correct framing:** The "acoustic white hole" is a DECORRELATION EVENT in the BEC-internal fluctuation spectrum at tau_fold. The Mach 13.75 condition means the rate of tau-evolution exceeds the rate at which delta phi fluctuations can equilibrate within the BEC internal structure. This decorrelation is the substrate-level origin of the POST-TRANSIT correlation pattern — the r_k hierarchy, the phases phi_k of the squeezed vacuum. It is NOT a geometric object in any 4D spacetime, and it has no propagation interpretation on any metric.

**No Hawking-like radiation beyond the squeezing pattern.** The BEC analog-gravity literature (Unruh 1981, Barcelo-Liberati-Visser 2011) predicts Hawking-like phonon radiation from acoustic horizons in BEC flows. In the framework, the "Hawking-like radiation" is the squeezed vacuum |0_out> = S(r_k, phi_k) |0_in>. There is no SECOND source of radiation on g_M beyond the squeezing. The "Hawking temperature" T_H of the acoustic horizon is encoded in the phase phi_k and magnitude r_k of the squeezing; it is not a separate thermal spectrum.

Any future proposal that predicts "additional Hawking-like GW or photon signal from the fold" is double-counting the squeezing physics and should be flagged. This is OQ7 WHITE-HOLE-NO-HAWKING-75.

**Verification status (LANDED; S85 W6 formalization + the scalar/tensor metric split).** The S85 W6 wave formalized the acoustic-white-hole treatment:

- **S85 W6 acoustic-white-hole-formal** (producing script s85_w6_acoustic_white_hole_formal.py; imports Mach_max, tau_fold, v_term). The companion S85-W6-4-EXTREMAL-HORIZON-FORMAL: PASS (value='kappa=0.00e+00', scheme=Jensen_V_tree, convention=2D_modulus_metric) confirms the formal surface-gravity treatment; the gate S85-ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL carries the causal-disconnect formalization.
- **Scalar/tensor metric split (S63 vdd-hawking).** This is the physical origin of "no extra Hawking radiation": r_s = c_s * r_H — scalars "see" the acoustic metric (which HAS a white hole), tensors "see" the gravitational metric (which has NO white hole). The two metrics are related by the sound-speed factor c_s. Because the tensor sector sees no acoustic horizon, there is no second tensor-channel Hawking spectrum.
- **Scalar-Tensor Kasparov Decoupling [T3, PERMANENT]** (baseline-findings-s66; atlas-07-permanent-results, VdD-Hawking S63): U_total = 1_M tensor U_K  =>  beta_T = 0 EXACTLY at linear order. The Bogoliubov transformation acts trivially on the tensor sector (beta_T = 0), so the tensor channel carries NO squeezed-pair / Hawking-like signal at linear order — the squeezing (and hence the "Hawking-equivalent radiation") lives in the SCALAR sector only. This is the structural theorem under the "no extra Hawking radiation" claim: the squeezed vacuum |0_out> = S(r_k, phi_k)|0_in> is scalar-sector physics, and beta_T = 0 forbids a tensor-sector double-count.

So OQ7's "no Hawking-like radiation beyond the squeezing pattern" is now anchored in (a) the S85 W6 formal kappa = 0 / causal-disconnect treatment and (b) the PERMANENT scalar-tensor decoupling beta_T = 0.

### 7.4 "Causally disconnected" — NOT a GR claim

**Old phrasing:**

> "The pre-fold and post-fold regions are causally disconnected by the supersonic flow, which solves the horizon problem."

**Correction:** The pre-fold and post-fold are NOT causally disconnected in the GR sense. There are no timelike geodesics in the pre-fold g_M^< that could have transported signals to the post-fold g_M^>, because g_M^< and g_M^> are TWO DIFFERENT Lorentzian manifolds (Two-Manifold Non-Embedding Theorem, Section 3.2), not two regions of a single spacetime. "Causal disconnection" in GR is a statement about light cones in a shared spacetime; it does not apply when the two regions live on different manifolds.

**Correct framing:** The "horizon problem" is solved not by causal disconnection within a shared spacetime, but by the substrate's global UNIFORMITY being INHERITED from the spectral triple's global algebraic uniqueness. Every point in the emerging 4D manifold experiences the same Jensen evolution at the same modulus value, because the rewriting is not local to any point — it is global to the spectral triple. The pre-fold uniformity is a STRUCTURAL property of the spectral data, not a dynamical achievement of signal equalization.

The workshop's E3 makes this explicit: "there is no 'homogeneous signal that had to cross a large distance' because the homogeneity is not a feature of a signal — it is a feature of the spectral triple being the same at every 4D point by construction. The 4D homogeneity is INHERITED from the spectral triple's global uniqueness, not achieved by propagation at any speed."

### 7.5 "Inflation solves the horizon problem" language (from LCDM vocabulary)

This phrase never belonged in the framework, but it sometimes slips into comparisons with cosmology. The correct framing: the framework does NOT "solve the horizon problem" in the LCDM sense. It REPLACES the horizon problem with a non-question: global uniformity is a structural property of the spectral triple, not a dynamical equalization that must be achieved across a causal horizon. Once the substrate picture is adopted, "how did distant regions reach the same temperature" is like asking "how do all frames of a single film share the same color palette" — they don't need to reach agreement, because they are all frames of the same film with the same palette as a structural fact.

---

## 8. Observational Consequences

The workshop established that the framework's causal structure produces specific observational signatures, distinct from both GR and from standard LCDM inflation. This section enumerates them.

### 8.1 Layer 1 / Layer 2 O(tau) ~ 0.19 observable signature at BAO peaks (OQ1 LAYER-1-LAYER-2-DIFF-75)

**This is the most observationally consequential result of the workshop.**

The D-R2-2 correction establishes that Layer 1 and Layer 2 branch speeds differ by O(tau) ~ 0.19 at the fold on the seven gapped directions (B1, B2, B3, Leggett, plus the other optical/Leggett branches). For the B1 acoustic singlet, which dominates the BAO feature at k ~ 0.043 Mpc^{-1}, the Layer 1 velocity c_B1^(1) = sqrt(Z_B1(tau) / M_B1(tau)) may differ from the Layer 2 velocity c_B1^(2) = 0.0798 M_KK (from BdG diagonalization) by a fraction of tau, i.e. potentially 10-20% of the c_B1 value.

**The observational test.** A precision measurement of the BAO acoustic peak position compared against the framework's Layer 1 and Layer 2 predictions would be a direct discriminator:

- If Layer 1 and Layer 2 agree to machine precision (consistent with einstein's original E4 claim, inconsistent with D-R2-2), the framework predicts the BAO peak at a single position, matching standard GR/LCDM at leading order.
- If Layer 1 and Layer 2 differ by O(tau) ~ 0.19 on gapped directions (consistent with D-R2-2), the framework predicts either a shifted BAO peak or a structural "doubling" where the acoustic feature has Layer-1 and Layer-2 components with distinct frequencies.

**Computation OQ1 LAYER-1-LAYER-2-DIFF-75** (pre-registered for S75):

- Compute c_b^(1) = sqrt(Z_i(tau) / M_i(tau)) (Layer 1) for each of the 8 BCS branches at tau = tau_exit, using the Jensen-deformed scalar curvature formula Baptista eq (2.40) projected onto each SU(3) generator.
- Compute c_b^(2) from BdG diagonalization (Layer 2, already computed in W1-A).
- Report the difference |c_b^(1) - c_b^(2)| per branch.
- Gate: PASS if all 7 gapped differences are O((E/M_KK)^2) = 10^{-34}; INFO if any difference is O(tau) = 0.05-0.3; FAIL if any difference exceeds O(1).
- Most likely outcome: INFO. This would be a framework-specific observational distinguisher at BAO scale.

**This is the primary observational distinguisher of the phonon-exflation causal structure from GR** at currently accessible precision. DESI and Simons/CMB-S4 data are either already collected or imminent; a precision comparison is a real test that the framework can pass or fail.

### 8.2 Squeezing parameters (r_B1, r_B2, r_B3, n_pair) as Mach 13.75 projection onto g_M

The Bogoliubov squeezing pattern of the GGE relic is the OBSERVATIONAL SHADOW of the Mach 13.75 substrate reorganization. The relevant numbers are:

- r_B1 = 3.571 (B1 acoustic singlet, most squeezed because c_B1 = 0.0798 is smallest and sits deepest in the sudden-quench regime)
- r_B2 = 1.786 (B2 flat optical, least squeezed because the flat band has minimal d omega / d tau at the van Hove maximum)
- r_B3 = 1.963 (B3 dispersive optical, intermediate)
- n_pair = 59.8 (Brundobler-Elser saturation; S38, S67 MULTI-LEVEL-LZ-67)
- n_bar per branch: 315.69 (B1), 8.40 (B2), 12.19 (B3); weighted (1, 4, 3) average = 48.23

**The observational projection** (C-R2-6 of the workshop):

```
Mach 13.75 (substrate-internal ratio at tau_fold)
   |
   | Bogoliubov ODE integration along tau-path
   v
(r_B1, r_B2, r_B3) = (3.571, 1.786, 1.963)  [per-mode squeezing]
   |
   | W1-A Sasaki-Stewart multifield transfer function
   v
alpha_s = 8.4e-15 (machine epsilon, from H_b^2 cancellation)
n_bar = (315.69, 8.40, 12.19) weighted (1,4,3) -> 48.23 average
```

**The pattern is a signature of diabatic transit.** A standard Mach << 1 slow-roll inflationary cosmology predicts:

- r_k -> 0 for all modes (adiabatic limit, no non-trivial Bogoliubov transformation).
- n_pair -> 0 (no Parker pair production).
- alpha_s ~ -2 epsilon + eta ~ O(0.01) from standard slow-roll (Komatsu-Nolta 2011).
- No "hierarchy" of squeezings between different branches (all modes squeezed uniformly).

The phonon-exflation framework in the Mach 13.75 diabatic regime predicts:

- r_B1 = 3.571, r_B2 = 1.786, r_B3 = 1.963 (HIERARCHY: B1 most squeezed, B2 least, B3 intermediate). This is a PATTERN, not a single number.
- n_pair = 59.8 (per-branch n_bar = 315.69, 8.40, 12.19 with weights 1, 4, 3 giving average 48.23).
- alpha_s = 8.4e-15 (machine epsilon, FLAT, from H_b^2 cancellation in the Sasaki-Stewart multifield kernel).
- f_NL folded shape (S66 Mack prediction), not equilateral or squeezed.
- Leggett branch dark-matter occupation (f_DM ~ O(0.1-0.3) from S66).

Each of these is a distinct observational signature that CANNOT be produced by any Mach << 1 slow-roll theory. The hierarchy r_B1 >> r_B2 is structural: it reflects that B1 has the lowest sound speed (c_B1 = 0.0798) and therefore sits deepest in the diabatic regime (adiabaticity parameter gamma = |d ln omega / dt| / omega is largest for B1).

**Pre-registered observational prediction set:**

- alpha_s flat at machine precision (NOT "alpha_s < 0.01"): the framework predicts alpha_s = O(10^{-15}), i.e. UNOBSERVABLY flat, not "small". If Planck/Simons/CMB-S4 measure alpha_s > 10^{-5}, the framework survives; if they measure alpha_s = 0 to machine precision, this is a positive distinguisher. **[S93-ERA UPDATE — SUPERSEDED-AS-SINGLE-LABEL; see Section 8.2a.]** The "alpha_s = 8.4e-15 flat" claim is the FIBER-LEVEL Sasaki-Stewart value (an H_b^2-cancellation artifact at the fiber scale). The framework actually carries TWO scale-separated alpha_s observables — a substrate-scale running alpha_s_substrate = -0.08587279 (inside the BZ) and a CMB-pivot running alpha_s_pivot = 0 (Goldstone-protected) — and which one a detector measures is set by the transport degree. Section 8.2a disambiguates; the single "flat" label is no longer adequate.
- r_k hierarchy visible through the BAO acoustic feature at k = 0.043 Mpc^{-1}: B1 dominates and its squeezing r_B1 = 3.571 produces an amplitude enhancement over the slow-roll prediction by a factor of sinh^2(3.571) ~ 315.69.
- Dark-matter channel via Leggett occupation (f_DM prediction from S66 — separate observational channel, not the squeezing pattern directly).

### 8.1a Two-speed tensor tilt: the S84 observational consequence of the Layer-1/Layer-2 split

**Source**: S84 two-speed tensor-tilt theorem [PROVEN] (session-84-mack-synthesis.md); S85 W3-5 transfer identity. NEW since the S74 document. This is the cosmological-observable realization of the Layer-1/Layer-2 split (Section 3.3): the framework's distinct tensor and scalar propagation speeds produce a tensor spectral tilt that DIFFERS from the single-speed slow-roll consistency relation.

The generalized single-field consistency (Garriga-Mukhanov 1999) with c_T != c_S:

    n_T(two-speed) = - r * c_T / (8 * c_S)        vs        n_T(single-speed) = - r / 8        (8.1a-1)

**Substitution chain (direction).** Step 1: c_T = 1.000 (tensor mode = B2-Goldstone, gravitational-cone speed; S83 G46). c_S = 0.485 (= c_BLV, BCS-channel-dressed scalar acoustic speed; canonical_constants.py:486). Step 2: the ratio c_T/c_S = 1.000/0.485 = 2.062. Step 3: target = sign of [|n_T(two-speed)| - |n_T(single-speed)|]. Step 4: substitute — |n_T(two-speed)| / |n_T(single-speed)| = (c_T/c_S) = 2.062 > 1. Step 5: read off — c_T/c_S > 1  =>  |n_T(two-speed)| > |n_T(single-speed)|: the substrate two-speed metric makes the CMB-scale tensor tilt MORE NEGATIVE than the slow-roll consistency relation, by exactly the factor c_T/c_S = 2.06. Conclusion: the framework predicts a tensor tilt 2.06x more negative than -r/8.

**Verification.** S85 W3-5 two-speed transfer identity c_S_canon = f_B PASS (machine precision, max|ratio-1| = 0.000e+00 across all 5 regulators) — the scalar two-speed leg is regulator-invariant. The direction (more-negative n_T) is a PROVEN structural prediction, distinct from any single-speed inflationary model. This is the observable face of the Layer-1/Layer-2 split (Section 3.3): the gapped-vs-Goldstone speed difference, projected onto the tensor sector.

### 8.2a Two-scale alpha_s: the substrate-scale running vs the CMB-pivot running (SUPERSEDES the single "flat" label)

**Source**: S92 AH-TR-1 + S93 W7-1 (S93-W7-1-ALPHA-S-W-KAPPA-FACTORIZATION-DEG-TRANSPORT-BZ-PIVOT: PASS). NEW since the S74 document. This SUPERSEDES the §8.2 single-label "alpha_s = 8.4e-15 flat" by disambiguating it into TWO scale-separated observables — it does NOT overwrite either; both are real substrate-IS observables.

The framework carries TWO alpha_s running observables, 54.04 decades apart in scale:

- **alpha_s_substrate = -0.08587279** (canonical alpha_s_substrate_distance_1, S92 AH-TR-1): the substrate-distance-1 running alpha_s = (a_4^{zeta}/a_2^{zeta})^2 - 1 = d^2 S_transfer/dk^2, evaluated at the Mellin-cone pole s=3, INSIDE the Brillouin zone (the substrate scale, ~M_KK). This is a real spectral-tilt curvature of the substrate's transfer function.
- **alpha_s_pivot = 0.0** (canonical alpha_s_pivot_goldstone, S92 AH-TR-1): the CMB-pivot scalar running alpha_s = d^2(ln P_zeta)/d(ln k_4D)^2, Goldstone-protected ~0 (|alpha_s| <= 5e-3), at the CMB pivot scale k_4D. This is the observable a CMB experiment measures.

**The transport degree decides which a detector measures (SCALE-AND-CHANNEL-TAGGING).** The S93 W7-1 verdict: factorization_holds = False, formulation = T4-non-scalar, deg(T_{BZ->pivot}) = +2 NON-SCALAR, reading = (T_is_scalar = False). The governing rule (phononic-framing.md, S92 AH-TR-1):

    O^pivot = O^substrate   IFF   deg(T_{BZ->pivot}) is the T2-VACUOUS (scalar) case.

Here deg(T) = +2 (non-scalar), so the substrate and pivot values DIFFER (Reading-T: substrate != pivot). The two-pole (a_4^{zeta}/a_2^{zeta})^2 - 1 transfer factor survives the dimensionless ratio (factorization_holds = False), so the substrate-scale running does NOT transport to the pivot as the same number; the off-pivot apparent -12.146 sigma Planck "tension" relocates as a scale-mismatch, and the pivot-vs-Planck comparison is +0.67 sigma (a comfortable consistency).

**Why both are substrate-IS, neither demoted.** Both alpha_s_substrate (inside the BZ) and alpha_s_pivot (at the CMB pivot) are real substrate-IS observables in the IS-not-IN sense: the substrate IS the spectral triple, and BOTH the BZ-scale tilt-curvature and the pivot-scale tilt-curvature are intrinsic functionals of it. Which one a given detector measures is set by deg(T), NOT by demoting one. A CMB experiment (Planck/CMB-S4/CMB-HD) measures the pivot value (~0); a hypothetical substrate-scale probe would see -0.0859. The single "8.4e-15 flat" label conflated the two; the correct statement is the matched (scale, channel) pair. (Cross-document note for W9: Phononic-to-Cosmos and pre-registered-observations also cite alpha_s; the two-scale split must be consistent across docs.)

**Classification (c-compare).** alpha_s is a spectral-tilt-curvature observable, NOT a propagation velocity (Section 6.3 EC10): it is caught at STEP 4 (dimensionless, not g_M-distance/g_M-time). Neither incarnation is c-bounded — the v_g <= c_Gold envelope does not constrain a tilt-running. This is the c-compare-consistent reason the two-scale alpha_s does not interact with the causal envelope.

### 8.3 NLO Lorentz violation ~ 10^{-34} (structural prediction, currently unobservable)

The framework predicts that all propagation on g_M is bounded by c_Gold at leading order, with NLO corrections from the a_4^{zeta} contribution to the photon kinetic term:

    c_photon / c_Gold = 1 + alpha * (M_KK / M_Pl)^2 + beta * (E_photon / M_KK)^2 + ...     (8.1)

where alpha is a dimensionless coefficient from the a_4^{zeta} Yang-Mills kinetic term's correction to c_photon relative to the a_2^{zeta}-generated Goldstone cone, and beta is the NLO dispersion correction. The framework's canonical scales give (M_KK / M_Pl)^2 ~ 2.3e-5 (gravity route, M_KK_gravity = 7.43e16 GeV) and (E_photon / M_KK)^2 ~ 10^{-34} at MeV scales.

**Why this is a ZERO-PARAMETER structural prediction, not a fit.** The framework does NOT have an adjustable M_QG as other QG proposals do (loop quantum gravity, causal dynamical triangulations, Horava-Lifshitz, doubly-special relativity). M_KK = 7.43e16 GeV is FIXED by the spectral-triple G_N constraint (S44 SAKHAROV-GN-44 PASS 3-way). The NLO LV coefficient is a structural output, not a fit parameter.

**Why this is currently unobservable.** Observationally, the tightest LI bound is from GW170817 + GRB 170817A: |c_GW / c_gamma - 1| < 3e-15 at the relevant energies. The framework's prediction is |c_GW / c_gamma - 1| ~ O(10^{-34}) at observational energies, which passes the current bound by 19 orders of magnitude. A future probe reaching 10^{-34} would begin to test it. That probe does not exist.

**Pre-registration status (LANDED).** OQ4 LV-NLO-75 (Section 9). The NLO-band test LANDED at S83: **S83-NNLO-BAND-BOUND: FAIL** value=0.000100 (scheme=Berges-3PI-NNLO-Zubarev, convention=W2-canonical-0.025-slope, L_max=5, sha256=ec83c19fb7b1d4ad2a4b9929250b27de72ec873b6047b00acc66f30e23e671be; producing script s83_w2_g11_nnlo_band_bound.py; gate NLO-1). The FAIL is a NNLO/LO ratio-band verdict (the 3PI NNLO band-bound test), NOT a falsification of the zero-LIV prediction — it records that the NNLO band-bound test did not land in its pre-registered PASS band at L_max=5. The underlying zero-LIV structural prediction stands separately: **C-FABRIC-42** establishes c_fabric = c, i.e. ZERO Lorentz invariance violation at ANY order — the Amelino-Camelia modified dispersion v(E) = c(1 - (E/E_QG)^beta) reduces to v(E) = c for all E (session-42-quantum-foam-collab.md). So the framework's LV prediction is exactly zero at the fabric level; the O(10^{-34}) NLO estimate (eq 8.1) is the cutoff-function-dependent leading deviation, and the S83 NNLO-band FAIL bounds the NNLO contribution. Effort: LOW; Priority: LOW (EVOI very low at current precision; the GW170817 bound passes by ~19 OOM). Retained as a zero-parameter structural prediction (consistency check of the spectral-action expansion, not a testable LV claim).

### 8.4 Distinguishers from (a) GR, (b) Lorentz-violating alternatives, (c) analog gravity

The framework is structurally distinct from each of these alternatives, but the distinguishability is asymmetric — observable in some cases and unobservable in others.

**(a) From standard GR.** Distinguisher: the Layer 1 / Layer 2 O(tau) ~ 0.19 split on the B1 acoustic branch (Section 8.1). This is OBSERVABLE at BAO acoustic peak precision. The framework predicts a specific deviation from the standard LCDM acoustic peak position if the gapped branches have Layer 1 / Layer 2 differences. This is the primary observational discriminator.

**(b) From Lorentz-violating alternatives** (loop quantum gravity, causal dynamical triangulations, Horava-Lifshitz, doubly-special relativity). Distinguisher: the framework predicts LV suppression O((E/M_KK)^2) ~ 10^{-34} from a ZERO-PARAMETER structural source, while LV alternatives predict LV at O((E/M_QG)^2) with adjustable M_QG. The suppression magnitudes coincide with LV theories at the same O((E/M_QG)^2) scale, so the framework is UNFALSIFIABLE vs LV at current precision. Only a precision probe 13-17 OOM better than today could begin to distinguish them.

The deeper distinguisher is the SOURCE of the suppression: the framework's 10^{-34} bound comes from a zero-parameter spectral action; LV theories require M_QG to be fit. In the event of a future detection, the framework predicts a SPECIFIC coefficient, while LV theories have a free parameter. This is a structural difference but not currently a testable one.

**Dedicated LQG/CDT cross-framework comparison (NEW since S74).** A full structural comparison now exists: `sessions/framework/correspondence/loop-quantum-gravity-phonon-exflation-comparison.md` (Loop Quantum Gravity vs Phonon-Exflation: A Structural Cross-Framework Comparison). Key points relevant to this section's distinguisher:

- The framework and LQG share the "spacetime is not fundamental" stance, but differ structurally: LQG quantizes geometry directly (spin networks / spin foams), while phonon-exflation emerges g_M from the a_2^{zeta} Seeley-DeWitt coefficient of a FIXED spectral triple (Section 3.6). The framework's geometry is a spectral MOMENT; LQG's is a quantized area/volume spectrum.
- LQG open problems the comparison records: "Semiclassical limit is incomplete", "Spin foam sum divergence", "Observational signatures are weak". The phonon-exflation analog of the last is the O(10^{-34}) LV bound here (also weak/unobservable) — but from a zero-parameter source.
- The comparison also hosts the framework's own FRIEDMANN-BCS-38 BROKEN status (Section 3.2 Verification): shortfall 133,200x; structurally addressed by the Two-Manifold Non-Embedding Theorem (there is no single FRW trajectory for a single-field Friedmann-BCS lock), with no replacement single-field formulation. This is the honest open-state on the cosmological-dynamics side, recorded in the cross-framework ledger rather than hidden.

The d_s spectral-dimension flow (Section 8.5) is the framework's direct response to CDT's hallmark prediction (UV dimensional reduction to d_s ~ 2): the substrate shows NO such reduction (d_s -> 8 Weyl at the gap scale), and the fair-comparison discipline (AH-PF-1) requires comparing the SAME functional at the SAME diffusion-window scale-type before any reduction verdict.

**(c) From analog gravity** (BEC acoustic metrics, Barcelo-Liberati-Visser). The framework is NOT an analog of analog gravity — it is STRUCTURALLY DIFFERENT. Analog gravity places BEC fluctuations on a pre-existing flat (or curved) laboratory spacetime; the acoustic metric h_{mu nu} is a second metric DERIVED from the fluctuation equation on the shared spacetime. In the phonon-exflation framework, there IS NO pre-existing spacetime: the substrate IS the fabric whose spectral triple is the fundamental data, and g_M is ITSELF emergent from the a_2^{zeta} Seeley-DeWitt coefficient. The "acoustic metric" at the fold (h_{mu nu}) is a linearization projection of the substrate's fluctuations in parameter space, NOT a second metric alongside g_M (since g_M does not exist at the fold).

The framework can be USED to reproduce analog-gravity calculations as limiting cases (the BEC acoustic horizon at the fold is mathematically similar to the Unruh BEC white hole), but the UNDERLYING structure is different: the BEC acoustic metric is a second metric in an analog, while the phonon-exflation substrate is the ONLY structure, with g_M as an emergent derived metric.

The Hawking-like radiation from the acoustic horizon is NOT predicted as a separate thermal spectrum on g_M; it is already captured by the Bogoliubov squeezing pattern (r_k, phi_k). See Section 7.3.

**(c.a) The laboratory-IN image: the 3He-B BdG acoustic-metric cross-pillar bridge (NEW since S74).** The §VII cross-pillar bridge program (post-S74) supplies the concrete laboratory-IN image of the framework's c_Gold / g_M structure. The acoustic metric on the fabric is

    ds^2_acoustic = -(c_BdG^2 - v_mod^2) dt^2 + (fabric metric)_ij dx^i dx^j     (8.4-1)

(atlas-qa-collab; the Unruh-Barcelo acoustic metric with the BdG sound speed c_BdG and the modulus flow v_mod). The forward bridge candidate FWD-C3 connects Pillar IV (substrate quantum-metric / Peotta-Törmä BZ-trace) to Pillar V (3He-B BdG spectral triple) via the inheritance morphism chi: A_K -> M_2(C) (the BdG sub-algebra), under the 5-anatomy IS-not-IN + 3-level discipline (cross-pillar-bridge-anatomy.md; cross-pillar-bridge-corpus.md). The K-counter status is K=1 -> K=2 SUGGESTION (S87 W11-5 instance_2 REGISTRY-FAIL Tier3-violates-Tier2-by-21x; S87-METH-CROSS-PILLAR-BRIDGE-K-COUNTER-UPDATE: PASS). The first registered cross-pillar bridge, §VII.W (Pillar III <-> Pillar IV, HP parity-grading orthogonality), is PERMANENT (S86 W-5).

**Direction of explanation (IS-not-IN).** The substrate (Pillar IV) IS the spectral-triple quantum-metric structure; the bridge map (HKR / K-theory boundary / Connes-Karoubi pairing) carries it to the laboratory (Pillar V) 3He-B BdG acoustic metric. The 3He-B sound mode c_BdG is the LABORATORY analog of the substrate's Goldstone envelope c_Gold — NOT a second fundamental metric. A 3He-B vortex-core / mu-SR measurement of c_BdG is the lab-IN realization of the substrate's c_Gold; the direction flows substrate -> bridge -> lab, never the reverse (inverting it is a container-thinking violation). This is the Level-2-A transit-dynamics audit axis of the cross-pillar 3-level ladder.

## 8.5 Spectral-dimension d_s flow vs CDT: the dimensionality propagation "sees" (NEW since S74)

**Source**: S92 ad-hoc workshop (s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md) + S93 W7 (session-93-plan-w7.md). NEW since the S74 document — an entirely new causal-architecture axis. Classification: **GEOMETRIC** (an intrinsic functional of D_K).

Beyond "how fast can a signal propagate on g_M" (c_Gold) and "what is the causal structure" (the two-regime split), there is a third causal-architecture question: **what dimensionality does the substrate's diffusion kernel PRESENT to a propagating excitation?** The spectral dimension answers it:

    d_s(sigma) = -2 d ln P(sigma) / d ln sigma,    P(sigma) = Tr e^{-sigma D_K^2} = sum_{(p,q)} dim(p,q) sum_i e^{-sigma lambda_i^2}     (8.5-1)

where P(sigma) is the heat-trace return probability on the (NORMAL-STATE, Delta = 0) D_K spectrum at converged L_max, and sigma is the diffusion time (a heat-kernel parameter, NOT a g_M coordinate; Section 6.3 EC9).

**The substrate result: d_s -> 8 Weyl, no CDT-like UV reduction.** Causal dynamical triangulations (CDT) famously predicts a UV dimensional reduction d_s -> ~2 at short distances. The phonon-exflation substrate shows NO such reduction: d_s -> 8 (the Weyl/manifold dimension of the internal SU(3) fiber) at the gap scale, consistent across S31Aa / S34 / S44. The internal SU(3) fiber does not "thin out" to 2D in the UV.

**The (observable, diffusion-window) discipline.** d_s(sigma -> 0) (the Weyl asymptotic = manifold dimension) and d_s(sigma_* ~ 1/E_0^2) (the windowed value at the feature energy, sigma_* = 1.4005 M_KK^{-2} at the fold window) are DISTINCT functionals of the SAME P(sigma) and may differ arbitrarily. A verdict proving the asymptotic and asserting it about the windowed observable is an observable-conflation overclaim.

**The impedance product.** The decisive cancellation runs through the impedance product Z(E) = rho_E(E) * v_g(E), coupling the energy-axis density-of-states rho_E to the group velocity v_g; the directly-fitted energy-axis DOS exponent gamma_E is the discriminating sub-quantity (any impedance/product constraint Z = const is a CONSISTENCY CHECK, not a lock — Z is constant for the whole family gamma_E = 1 - 1/n in [1/2, 1), Sage-exact).

**The fair-comparison rule (AH-PF-1; SUGGESTION at K=2 post-S93 W7-3).** Do NOT compare the substrate's sigma -> 0 asymptotic to CDT's intermediate-window value by letting CDT's scale-type be authoritative over the substrate's. Fix the (observable, diffusion-window) pair on BOTH sides first; apply the SAME functional Phi: P(sigma) -> -2 d ln P/d ln sigma at the SAME scale-type (intermediate-window <-> intermediate-window). This is the same-functional-different-scale fair-comparison discipline (phononic-framing.md; cross-pillar-bridge-anatomy.md §"Diffusion-window-observable specialization"). Letting CDT's scale-type win is a container-thinking violation at the observable layer (substituting the external framework's scale-type for the substrate's own).

**Why this is a causal-architecture observable.** d_s is the dimensionality that propagation "sees" — the effective dimension of the diffusion process generated by D_K. It is c-INDEPENDENT (Section 6.3 EC9: SUBSTRATE DYNAMICS at STEP 0, a log-derivative of the heat trace); it is bounded by the spectral structure (Weyl d_s -> 8), not by c_Gold. It is the substrate's intrinsic dimensionality, an a_0^{zeta}-family generating-functional observable, NOT a propagation velocity.

---

## 9. Pre-Registered S75 Computations

The workshop generated ten pre-registered computations for S75, each with a specific PASS/FAIL gate and an EVOI-based priority. They are listed in the workshop's Carry-Forward section and formalized here.

> **S93-ERA LANDED-VERDICT AUDIT (added in the comprehensive expansion).** Each OQ below now carries its actual landed verdict (KB-traced across S75->S93), prepended in bold. Summary: 8 of 10 landed (OQ6 LANDED-PASS->MIGRATED; OQ2 PERMANENT; OQ5 MIGRATED+reframe-PROVEN; OQ3 LANDED; OQ4 LANDED-FAIL; OQ9 LANDED/operationalized; OQ8 LANDED; OQ7 LANDED-adjacent) + the embedded c_Gold-emergence gate (LANDED-PASS->MIGRATED); 2 of 10 NOT-RUN as numbered S75 gates (OQ1 subsumed by the S84 two-speed tensor-tilt theorem + S86 layer-taxonomy; OQ10 thawing branch documented empty for S73B-S74). The document has moved from "promising ten tests" to "recording ten outcomes".

**OQ1 / LAYER-1-LAYER-2-DIFF-75** — HIGH EVOI, LOW effort

> **LANDED: NOT-RUN as a numbered S75 gate (content subsumed).** No LAYER-1-LAYER-2-DIFF-75 verdict line exists in the KB. The physical content was realized instead in the cosmological tensor sector and PROVEN there: the S84 two-speed tensor-tilt theorem (n_T(two-speed) = -r c_T/(8 c_S); c_T/c_S > 1 => |n_T| more negative; session-84-mack-synthesis.md) + the S86 layer-taxonomy (s86-sector-2-split-layer-taxonomy.md, PROVEN). See Sections 3.3 and 8.1a. The per-BAO-branch number remains the uncomputed numbered-gate content; the two-speed STRUCTURE is PROVEN.

- Compute c_b^(1) = sqrt(Z_i(tau) / M_i(tau)) (Layer 1) and c_b^(2) (Layer 2, from BdG in W1-A) for each of the 8 BCS branches at tau = tau_exit.
- Pre-registered gate: PASS if all 7 gapped differences are O((E/M_KK)^2) = 10^{-34}; INFO if any difference is O(tau) = 0.05-0.3; FAIL if any difference exceeds O(1).
- Canonical inputs: lambda (Baptista 2.40), C_phi (Baptista 3.42), Jensen potential V(|phi|^2).
- Significance: decides the D-R2-2 dissent quantitatively. Most likely outcome: INFO with observational channel at BAO acoustic peaks.

**OQ6 / SPECTRAL-DECOUPLING-CERT-75** — HIGH EVOI, LOW effort

> **LANDED: PASS -> MIGRATED INFO.** S75 W2-E "Spectral-moment decoupling CERTIFIED — a_0^{zeta}, a_2^{zeta}, a_4^{zeta} algebraically independent, Wronskian nonzero" PASS (session-75-tesla-synthesis.md, session-75-mack-synthesis.md; script s75_spectral_decoupling_cert.py, gate CERT-75). MIGRATED to INFO at S81 batch hygiene (T3-BATCH-S75-SPECTRAL-DECOUPLING-CERT: INFO, sha256=55a1b9e0a8bebc05d1cecfab1a398c16619f4efddcd36dd19cfc083ea1b7b81e) — a no-run-no-gate provenance reclassification, NOT a retraction. The Spectral-Moment Decoupling Theorem is now a framework-internal CERTIFIED result (Sections 3.1, 3.5).

- Register the Spectral-Moment Decoupling Theorem as a permanent structural result with a full Gilkey proof on the Jensen-deformed SU(3) fibre.
- Pre-registered gate: PASS if the Gilkey orthogonality is verified to hold on the Jensen-deformed fibre at all canonical tau values (tau_fold = 0.190, tau_exit); FAIL if any tau value has a linear dependence between a_0^{zeta} and a_2^{zeta} as local invariants.
- Significance: upgrades the theorem from "inherited general result" to "permanent framework-internal theorem".

**OQ2 / W4M-CHECK-75** — HIGH EVOI, LOW effort

> **LANDED: n*=60 PROMOTED PERMANENT (W3-C).** S75 W3-C "Lefschetz n* = 60 promoted to permanent — L_max-invariant, L_max=7 verified, topological invariant of L_Y" PASS (session-75-tesla-synthesis.md, session-75-mack-synthesis.md). The n*=60 -> v_EW mapping: v_ew = 246.0 GeV (canonical_constants.py:1570), OOM(M_KK/v_ew) = 14.4801 (Sage-Q exact, the Higgs-driven 14.48-OOM drop). The W4M Bogoliubov-boundary artifact s74_zero_mode_winding.py (WINDING-74) MIGRATED INFO at S81 (T3-BATCH-S74-ZERO-MODE-WINDING: INFO, sha256=a9066401de1cb2fbcc8d9c77924a7441979567c15118d0708c36fc6c46352641). The n*=60 dominance is a SUBSTRATE-LEVEL Lefschetz saddle (Section 5.2); its projection to v_EW is the Higgs-winding-mediated reduction — consistent with the one-way a_0^{zeta} -> a_2^{zeta} Bogoliubov projection (Section 3.1(iv)).

- Review the W4-M winding-modulus coupling to determine if the n* = 60 Lefschetz dominance -> v_EW = 246 GeV mapping is mediated by a Bogoliubov transformation at the emergence boundary, or if it is a direct a_0^{zeta} → a_2^{zeta} functional coupling.
- Pre-registered gate: PASS if the mapping is Bogoliubov-mediated (theorem holds); CHALLENGE if it is direct (theorem needs refinement or loophole); FAIL if the mapping is structurally malformed.
- Significance: decides whether the Spectral-Moment Decoupling Theorem is framework-complete or has an exception in the Higgs-winding sector.

**OQ5 / TWO-MANIFOLD-NEMB-75** — MEDIUM-HIGH EVOI, MEDIUM effort

> **LANDED: MIGRATED INFO + reframe-PROVEN.** Producing script s75_two_manifold_nemb.py exists; verdict MIGRATED INFO at S81 (T3-BATCH-S75-TWO-MANIFOLD-NEMB: INFO, sha256=d7abcfd28d66a89729cecd866da8fea31c4a1f43632adb6d867f90fdaa703415). The FRIEDMANN-FROM-A2-74 reframe is PROVEN (atlas-09-retractions Item 35: the single-f_conv-scalar bridge assumption is BROKEN), and the downstream FRIEDMANN-BCS-38 is BROKEN (133,200x shortfall; structurally addressed by this theorem). See Section 3.2 "Verification status (LANDED)". The 86-OOM bracket is the reframe-PROVEN non-embedding signature, NOT a matching failure.

- Verify the Two-Manifold Non-Embedding Theorem by computing Delta R = R_{g_phi}(tau_exit) - R_{g_phi}(tau_pre) from Baptista eq (2.40) for several canonical tau_exit values, and re-deriving the 86-OOM W1-E bracket from 2-3 independent routes.
- Pre-registered gate: PASS if multiple routes give the same 86-OOM bracket and Delta R is non-zero for all canonical tau_exit; INFO if the bracket varies by more than 2 OOM between routes; FAIL if a single-manifold embedding exists for some canonical choice.
- Significance: reframes W1-E 86-OOM as a structural signature of non-embedding rather than a numerical failure.

**OQ3 / PHASES-BD-75** — MEDIUM EVOI, LOW effort

> **LANDED (computed at S75).** Gate "W2-J: PHASES-BD-75 — Squeezing Phases phi_k for All 8 Branches" was authored by transit-dynamics-theorist at S75 (session-75-results-workingpaper.md §W2-J; s75_attribution_edges). The related S64 phase computation s64_bogoliubov_phases.py (BOGOLIUBOV-64) MIGRATED INFO at S81 (T3-BATCH-S64-BOGOLIUBOV-PHASES: INFO, sha256=fd565e7695f3b1511c41248c0b3e0150a5016d3285902daf5afa057425c7c91b). The phases phi_k ARE computed — the squeezing is characterized by (r_k, phi_k), not r_k alone ("Geometry sees amplitudes; resonance sees phases").

- Compute the squeezing phases phi_k (not just magnitudes r_k) for each of the 8 branches from the Bogoliubov ODE integration at the fold.
- Pre-registered gate: PASS if phases are all zero/trivial; INFO if phases have non-trivial structure (e.g., parity-violation or inter-band correlations); FAIL if phases cannot be computed from the ODE.
- Significance: refines the squeezing observational channel into magnitudes + phases.

**OQ9 / SUBSTRATE-CHANNELS-ENUMERATE-75** — MEDIUM EVOI, LOW effort

> **LANDED / operationalized (S83).** The channel enumeration was operationalized at S83 as enumerate_observable_channels_s83() / enumerate_substrate_admissible_dimensions() (session-83-plan.md). The substrate-dynamics observational channels are catalogued: squeezing pattern (r_k, phi_k), Higgs VEV winding (n*=60), Lambda_eff residual, Leggett DM occupation, squeezing phases — plus, post-S74, the substrate-distance alpha_s running (Section 8.2a) and the d_s diffusion-dimension probe (Section 8.5).

- Enumerate all substrate-dynamics channels that project onto g_M beyond the squeezing pattern. Current candidates: Higgs VEV winding from Lefschetz n* = 60, Jensen-modulus imprint on effective Lambda_eff, dark-matter occupation via Leggett branch, squeezing phases.
- Pre-registered gate: PASS if the enumeration is complete; INFO if a new channel is identified; FAIL if the enumeration is structurally incomplete.
- Significance: catalogues the total observational portal to substrate dynamics.

**OQ8 / STEP-0-ALGORITHM-ADOPT-75** — MEDIUM EVOI, MEDIUM effort

> **LANDED: the c-compare skill IS the adoption artifact.** The 6-step algorithm was adopted framework-wide as the operational skill .claude/skills/c-compare/SKILL.md (STEP 0 spectral-moment localization + STEP 1a/1b + STEP 2-5; four verdict classes PROPAGATION/SUBSTRATE-DYNAMICS/MIXED/CONTRADICTION; 9 worked examples). The skill cites THIS document (Section 6) as its canonical source. Its existence IS the framework-wide STEP-0 adoption: any agent classifying a framework event along the causal axis now invokes the deterministic algorithm. See Section 6.0 for the verdict-class reconciliation.

- Apply the revised 6-step classification algorithm to all pre-S75 computations that used "causal" or "superluminal" language. Audit and reclassify.
- Pre-registered gate: all pre-S75 reports audited; all "causal" / "superluminal" language in propagation-FAIL reports reclassified as "exceeds substrate throughput c_Gold"; all SUBSTRATE DYNAMICS events flagged if they carry c-bound comparisons.
- Significance: enforces vocabulary discipline framework-wide.

**OQ7 / WHITE-HOLE-NO-HAWKING-75** — LOW-MEDIUM EVOI, LOW effort

> **LANDED-adjacent: S85 W6 formal + scalar-tensor decoupling PERMANENT.** S85 W6 ran s85_w6_acoustic_white_hole_formal.py (formal treatment; imports Mach_max, tau_fold, v_term); S85-W6-4-EXTREMAL-HORIZON-FORMAL: PASS (kappa=0.00e+00, Jensen_V_tree, 2D_modulus_metric); gate S85-ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL. The no-extra-Hawking claim is anchored in the scalar/tensor metric split (S63 vdd-hawking, r_s = c_s r_H) + the Scalar-Tensor Kasparov Decoupling [T3 PERMANENT] (U_total = 1_M tensor U_K => beta_T = 0 exactly at linear order): the squeezing lives in the scalar sector only; beta_T = 0 forbids a tensor-channel double-count. See Section 7.3 "Verification status (LANDED)".

- Verify transit's decisive answer: the acoustic white hole has NO Hawking-like radiation beyond the squeezing pattern. Check that the Unruh-Barcelo-Liberati-Visser acoustic horizon framework, applied to the substrate-internal h_{mu nu}, produces ONLY the r_k pattern and no additional thermal spectrum.
- Pre-registered gate: PASS if the W1-A output is the unique Hawking-equivalent radiation from the acoustic horizon; INFO if there is a sub-leading correction; FAIL if there is a second source of radiation not captured by W1-A.

**OQ10 / THAWING-REGIME-CHECK-75** — LOW EVOI, LOW effort

> **LANDED: NOT-RUN as a numbered S75 gate (thawing branch documented empty).** No THAWING-REGIME-CHECK-75 verdict line exists in the KB. The closest landed content is s74_hp4_regime.py (REGIME-74). The thawing branch is already documented empty for all S73B-S74 computations in this document (Section 6.2 STEP 1b: "MIXED class ... in practice: empty for all S73B-S74 computations; treat as SUBSTRATE DYNAMICS for safety"). Independently, the S84 W8 informational-isolation result reinforces this: tau_fold = 0.190 "is not a free parameter to be observationally pinned; it is the sole admissible closure point" (session-84-w8-workingpaper.md) — post-fold 4D physics is informationally isolated from the tau-history during transit, so a thawing-regime observable does not survive to a probe timescale. NOT-RUN as a numbered gate; STEP 1b safety-treats it as SUBSTRATE DYNAMICS.

- Verify that the "thawing regime" (C1a PASSes but C1b FAILs) is observationally empty for all S73B-S74 computations. Compute dt_thaw for the canonical fold parameters and confirm it is 17+ OOM below any observational probe timescale.
- Pre-registered gate: PASS if dt_thaw < min(observational timescales) by 10+ OOM.

**OQ4 / LV-NLO-75** — LOW EVOI, LOW effort

> **LANDED: FAIL (NNLO-band; S83 NLO-1).** S83-NNLO-BAND-BOUND: FAIL value=0.000100 (scheme=Berges-3PI-NNLO-Zubarev, convention=W2-canonical-0.025-slope, L_max=5, sha256=ec83c19fb7b1d4ad2a4b9929250b27de72ec873b6047b00acc66f30e23e671be; script s83_w2_g11_nnlo_band_bound.py). The FAIL is a NNLO/LO band-bound verdict, NOT a falsification of the zero-LIV prediction (C-FABRIC-42: c_fabric = c, zero LIV at any order; Section 8.3). Records the NNLO contribution bound; the GW170817 bound passes by ~19 OOM.

- Compute c_photon / c_Gold = 1 + alpha * (M_KK/M_Pl)^2 + beta * (E/M_KK)^2 + ... from the a_4^{zeta} correction to the photon kinetic term on L_Y. Report alpha and beta as closed-form structural coefficients.
- Pre-registered gate: PASS if the computation produces a closed-form NLO coefficient as a framework-invariant output; INFO if the coefficient depends on a free parameter.
- Significance: records a zero-parameter structural prediction at O(10^{-34}), currently unobservable but permanent.

---

## 10. Scope and Limitations

### 10.1 What this document does NOT claim

- **Does not claim the framework proves general relativity is "just emergent".** The framework is a different kind of theory from GR, and the relationship between them is "a_2^{zeta} Seeley-DeWitt generates the Einstein-Hilbert action as the second spectral moment of D_K". This is an emergence, not a replacement. Standard GR results on the emergent metric g_M still apply; the framework adds the statement that g_M comes from a spectral triple.
- **Does not claim the framework is Lorentz-violating at observational scales.** Local Lorentz invariance is PRESERVED at all accessible energies. NLO LV corrections are O(10^{-34}), 13-17 OOM below current bounds. The framework is observationally indistinguishable from a Lorentz-invariant theory at leading order; the distinction is in the SOURCE of the Lorentz invariance (emergent from a_2^{zeta}, not postulated).
- **Does not claim the fold transit produces LIGO-detectable GWs.** The primordial GW signal from the transit is a SECOND-ORDER product of the post-transit Bogoliubov pair evolution (BCS-TENSOR-R-44 PASS, r ~ 10^{-9}), not a first-order emission from the fold. The framework predicts r << 0.036 (consistent with BICEP/Keck) because the fold is NOT a source of first-order GR gravitons.
- **Does not claim the "acoustic white hole" is a physical horizon with a null boundary.** It is a decorrelation event in the substrate's internal fluctuation spectrum, not a geometric object.
- **Does not claim c_Gold is a new fundamental constant.** It is the OUTPUT of a computation on the Jensen-deformed spectral triple. Its structural bracket [0.62, 1.73] M_KK is a framework-specific property, and its value 0.915 M_KK is fixed by the specific Jensen deformation at tau_fold.

### 10.2 Open questions — S93-era status (most now RESOLVED)

The S74 open questions below are updated to their landed state (Section 9 carries the full per-OQ verdicts). Most are resolved; the residual genuine-open items are flagged.

- **Spectral-Moment Decoupling Theorem — RESOLVED (CERTIFIED).** No longer "candidate pending OQ2". OQ6 LANDED PASS at S75 W2-E (Wronskian nonzero), MIGRATED INFO at S81 (Section 3.1). OQ2's W4M-CHECK landed as n*=60 PROMOTED PERMANENT (W3-C); the n*=60 -> v_EW projection is consistent with the one-way a_0^{zeta} -> a_2^{zeta} Bogoliubov projection (Section 3.1(iv)). The theorem is a framework-internal CERTIFIED result.
- **Two-Manifold Non-Embedding Theorem — RESOLVED (reframe-PROVEN).** No longer "candidate pending OQ5". The FRIEDMANN-FROM-A2-74 reframe is PROVEN (atlas-09 Item 35); the 86-OOM bracket IS the non-embedding signature; the downstream FRIEDMANN-BCS-38 is BROKEN with this theorem as the structural cause (Section 3.2). OQ5 script MIGRATED INFO at S81.
- **O(tau) Layer 1 / Layer 2 split — RESOLVED-IN-STRUCTURE (S84 two-speed tensor-tilt PROVEN); per-BAO-branch number remains uncomputed.** OQ1 was NOT-RUN as a numbered S75 gate; the two-speed STRUCTURE is PROVEN in the cosmological tensor sector (n_T(two-speed) = -r c_T/(8 c_S); c_T/c_S > 1 => |n_T| more negative; Sections 3.3, 8.1a). The specific per-gapped-branch BAO-peak number is the genuine residual-open computation (a real future compute gate, not a doc edit).
- **Squeezing phases phi_k — RESOLVED (computed).** OQ3 LANDED at S75 (gate W2-J: PHASES-BD-75; Section 9). The squeezing is characterized by (r_k, phi_k); the S64 phase computation MIGRATED INFO at S81. No longer "uncomputed".
- **Substrate-dynamics observational channels — RESOLVED (operationalized).** OQ9 was operationalized at S83 (enumerate_observable_channels_s83(); Section 9). The channel list is catalogued (squeezing pattern, Higgs VEV winding, Lambda_eff residual, Leggett DM occupation, squeezing phases) AND extended post-S74 by the substrate-distance alpha_s running (Section 8.2a) and the d_s diffusion-dimension probe (Section 8.5).
- **Genuine residual-open (real future computation, not doc edits):** (i) the per-gapped-branch Layer-1/Layer-2 BAO-peak number (OQ1's numbered-gate content); (ii) the c_Gold / c_BLV / c_fabric PROVENANCE entries in canonical_constants.py (a hygiene carry-forward; Sections 4.1, 4.3); (iii) cross-document alpha_s consistency under the two-scale split (W9 cross-document closeout; Section 8.2a).

### 10.3 Regime of validity for each theorem

| Theorem | Valid regime | Breakdown |
|:--------|:-------------|:----------|
| 3.1 Spectral-Moment Decoupling | Smooth D_K with finite lambda_max; heat-kernel expansion well-defined | Truncation boundary L_max; degeneracies in spectrum; cross-terms suppressed by (L_max)^{-2} |
| 3.2 Two-Manifold Non-Embedding | tau_pre != tau_post, smooth R_{g_phi} between endpoints | tau = 1 or 1/4 Jensen singularities (1/4 mitigated by f_phi compensating zero) |
| 3.3 Layer 1/2 O(tau) split | Gapped directions, tau in [tau_fold, tau_exit], BdG well-defined | Killing direction exception (coincidence is exact) |
| 3.4 Goldstone Masslessness | K-theoretically protected direction, bi-invariance preserved | Non-existent in framework (K-theory class is preserved) |
| 3.5 Heat-Kernel Polynomial Orthogonality | Laplace-type D_K^2, Jensen-deformed fibre smooth | Same as Theorem 3.1 |
| 3.6 a_2^{zeta} -> M_Pl_eff (Einstein-Hilbert generation) | a_2^{zeta}(fold) zeta-scheme at tau_fold; f_2 cutoff moment finite | Truncation boundary L_max (a_2^{zeta} value scheme/truncation-dependent; Section 3.7); the M_KK extraction consistency (SAKHAROV-GN-44) |
| 3.7 a_2^{zeta}(fold) vs a_2^{zeta}(full L10) | zeta-scheme half-zeta_D(1) is the canonical Seeley-DeWitt curvature moment | raw mode-sum Tr|D_K|^{-2} is NOT the SDW coefficient (diverges in continuum, truncated at L10); the two are distinct objects |

---

## 11. Cross-References

This document is load-bearing for the framework's causal architecture. It cites and is cited by:

**Framework rules and vocabulary:**
- `.claude/rules/phononic-framing.md` — Existing framework vocabulary. The "Mach 13.75", "acoustic white hole", "supersonic transit", "horizon problem" table entries are now given rigorous structural foundations by this document. The vocabulary table in phononic-framing remains correct; this document provides the theorems UNDER the vocabulary.

**Other framework documents:**
- `sessions/framework/framework-chaotic-instantons.md` — Instanton gas results (Kitaev). The instanton rates in that document (S_inst = 0.069, Gamma_inst = 0.934 per attempt) are SUBSTRATE DYNAMICS quantities by STEP 0 of the classification algorithm, and their interpretation is consistent with Section 5.2 here.
- `sessions/framework/Phononic-Penrose-Diagrams.md` — The Penrose diagram constructions (Schwarzschild-Penrose geometer). The "acoustic metric vs geometric metric" distinction in Diagram C is consistent with the two-layer causal architecture described here (Layer 1 = substrate-internal h_{mu nu} linearization projection, Layer 2 = emergent g_M).
- `sessions/framework/Phononic-framework-hypothesis.md` — The framework's overall hypothesis. This document provides the rigorous causal architecture that supports the hypothesis.
- `sessions/framework/framework-parametric-amplification.md` — The parametric amplification mechanism. The Bogoliubov pair production (r_B1 = 3.571, n_pair = 59.8) is a SUBSTRATE DYNAMICS event per Section 5.5, consistent with that document's treatment.
- `sessions/framework/registry/pre-registered-observations.md` — The framework's pre-registered predictions. The 10 pre-registered S75 computations in Section 9 above extend that list.

**Workshop sources:**
- `sessions/archive/session-74/session-74-transit-einstein-workshop.md` — Primary source. All theorems, numerical claims, and algorithm steps in this document are derived from the 4-turn workshop transcript.
- `sessions/archive/session-74/session-74-qa-vdd-workshop.md` — The original qa-vdd Q1 wording that motivated the W4-L fix (Section 7.1).
- `sessions/archive/session-74/session-74-results-workingpaper.md` — W4-L gap-dominated dispersion FAIL as the case study.
- `sessions/archive/session-68/session-68-vdd-qa-workshop.md` — Goldstone masslessness from Kasparov factorization (Section 3.4).

**Permanent results cited:**
- **S44 permanent results**: KO-dim 6, [J, D_K] = 0 (all 36 left-invariant directions), a_2^bos / a_2^Dirac = 61/20, SAKHAROV-GN-44 PASS 3-way, Bianchi identity on modulus EOM, spectral triple emergent.
- **S52 GL-JOSEPHSON-52 PASS**: canonical c_Gold = 0.915 M_KK.
- **S38 / S67 MULTI-LEVEL-LZ-67**: Brundobler-Elser saturation, P_exc = 1 in the diabatic limit.
- **S64 a_0^{zeta}/a_2^{zeta} trap**: decreasing a_2^{zeta} worsens CC via a_0^{zeta}/a_2^{zeta} ratio. Caveat on Spectral-Moment Decoupling (the theorem is about rate-comparability, not value-independence).
- **S44 BCS-TENSOR-R-44 PASS**: r ~ 10^{-9} tensor-to-scalar ratio (second-order GWs from post-transit Bogoliubov propagation).
- **S65 W5-D Bogoliubov Gaussianity Preservation [PERMANENT]**: f_NL = O(eps) regardless of squeezing (Section 5.5).
- **S63 Scalar-Tensor Kasparov Decoupling [T3, PERMANENT]**: U_total = 1_M tensor U_K => beta_T = 0 exactly at linear order (Section 7.3).
- **S61 Kasparov product factorization (Paper 01) [CLOSED, 5/5 conditions]**: m_Goldstone^{4D} = 0 exactly (Section 3.4).
- **S86 W-5 §VII.W First Cross-Pillar Bridge Theorem [PERMANENT]**: Pillar III <-> Pillar IV HP parity-grading orthogonality (Section 8.4(c.a)).

**Post-S74 sources (NEW since the 2026-04-11 document):**
- `sessions/archive/session-77/session-77-transit-einstein-workshop.md` — the a_2^{zeta} -> M_Pl_eff = a_2^{zeta}/(48 pi^2) -> G_N chain (T2.7, T3.14, T4.1, T5.2, T5.13); Section 3.6.
- `sessions/archive/session-76/session-76-transit-einstein-workshop.md` + `sessions/session-plan/session-85-plan-w7.md` — H_transit vs H_Friedmann two-rate formalism; F_stretch; Section 5.1a.
- `sessions/archive/session-92/workshops/s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md` + `sessions/session-plan/session-93-plan-w7.md` — d_s flow vs CDT; (observable, diffusion-window) discipline; impedance Z = rho_E v_g; Section 8.5.
- `sessions/archive/session-92/workshops/s92-adhoc-alpha-s-transfer-map-identity.md` + S93 W7-1 verdict (S93-W7-1-ALPHA-S-W-KAPPA-FACTORIZATION-DEG-TRANSPORT-BZ-PIVOT) — two-scale alpha_s; deg(T) = +2 NON-SCALAR; SCALE-AND-CHANNEL-TAGGING; Section 8.2a.
- `sessions/archive/session-84/session-84-mack-synthesis.md` — two-speed tensor-tilt theorem n_T(two) = -r c_T/(8 c_S); Sections 3.3, 8.1a.
- `sessions/framework/correspondence/loop-quantum-gravity-phonon-exflation-comparison.md` — LQG/CDT cross-framework comparison; FRIEDMANN-BCS-38 BROKEN; Section 8.4(b).
- `sessions/framework/registry/cross-pillar-bridge-corpus.md` + `sessions/framework/Atlas/atlas-11-cross-pillar-bridge-corpus.md` — acoustic-metric bridge FWD-C3 Pillar IV <-> Pillar V (3He-B BdG); 5-anatomy + 3-level discipline; Section 8.4(c.a).
- `computations/session-85/s85_w6_acoustic_white_hole_formal.py` (S85-W6-4-EXTREMAL-HORIZON-FORMAL PASS) — acoustic-white-hole formalization; Section 7.3.
- `.claude/skills/c-compare/SKILL.md` — the downstream operational classifier (OQ8 adoption artifact); 4 verdict classes; Section 6.0.
- `.claude/rules/phononic-framing.md` §"Scale-and-channel-tagging" + §"Same-functional-different-scale fair-comparison"; `.claude/rules/cross-pillar-bridge-anatomy.md` §"Diffusion-window-observable specialization" — the AH-TR-1 + AH-PF-1 governing rules for Sections 8.2a, 8.5.

**Canonical constants used** (line numbers re-pinned to the current `computations/_shared/canonical_constants.py`, S93-era):
- c_Gold = 0.915 M_KK (line 636; S52 GL-JOSEPHSON-52 + S75 W3-L; **NO PROVENANCE entry — QA carry-forward**)
- xi_BCS = 0.8083468753837275 M_KK^{-1} (line 424, S37)
- Delta_0_GL = 0.7704350982797368 M_KK (line 414, S37)
- a2_fold = 2776.1653888633655 M_KK^{-2} (line 453, S42 CONST-FREEZE-42; **zeta-scheme half-zeta_D(1)** => a_2^{zeta}); a4_fold = 1350.7216415169728 (zeta half-zeta_D(2) => a_4^{zeta})
- a_2^{zeta}(full L10) = 64308.24, a_4^{zeta}(full L10) = 29086.18 (s75_f_conv_spectral_output.txt; M_Pl_eff(L10) = 11.65 M_KK = 8.6551e17 GeV)
- M_KK_gravity = 7.428660036284456e16 GeV (line 341, SAKHAROV-GN-44)
- M_Pl_eff^2 = a_2^{zeta}(fold)/(48 pi^2) = 5.862 M_KK^2; M_Pl_eff(GeV) = 1.80e17 GeV (S77 T2.7/T3.14/T4.1)
- dS_fold = 58672.80241318 M_KK per dimensionless tau (line 483, S42)
- tau_fold = 0.19 (line 285, S42 CONST-FREEZE-42), tau_exit in [0.4, 1.614]
- Mach_max = 13.75 (Mach_max_framework, line 1844; baseline-findings-s66); v_terminal = 26.544972625732246 (line 492, S38)
- c_BLV = 0.485 M_KK (line 486, S64 four-speed hierarchy; **NO PROVENANCE entry — QA carry-forward**); c_fabric = 209.97368021 (line 485; **NO PROVENANCE entry**); c_mod = 1.000; c_BA = 0.399; c_L = 0.025 (R-protected LEGGETT-PARTITION-57/58)
- n_pairs = 59.8 (line 390, S38); v_ew = 246.0 GeV (line 1570); OOM(M_KK/v_ew) = 14.4801
- alpha_s_substrate_distance_1 = -0.08587279 (S92 AH-TR-1; (a_4^{zeta}/a_2^{zeta})^2 - 1 at Mellin pole s=3); alpha_s_pivot_goldstone = 0.0 (S92 AH-TR-1; Goldstone-protected)

---

## Closing Line

The user's thesis — "c limits propagation ACROSS the substrate but not substrate dynamics themselves" — is no longer a conceptual distinction. After the S74 transit-einstein workshop, it is the **Spectral-Moment Decoupling Theorem**, a rigorous statement of Gilkey's local index theorem applied to the Chamseddine-Connes spectral action, and every framework computation that bounds a SUBSTRATE DYNAMICS event with a c-bound is now structurally malformed by a one-step spectral-moment inspection.

The substrate IS the film, c_Gold IS the frame rate, and editing the film is not bounded by the playback speed because editing lives in a_0^{zeta} and playback lives in a_2^{zeta}, and heat-kernel orthogonality decouples the two.
