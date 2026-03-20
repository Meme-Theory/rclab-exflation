# Master Collaborative Synthesis: Session 31 Plan Review

## 3 Researchers, One Computation

**Reviewers**: Schwarzschild-Penrose Geometer, Hawking Theorist, Einstein Theorist
**Date**: 2026-03-01
**Re**: Session 31 Plan -- The Kapitza Gate (K-1), Instanton-Phonon Unification (I-1), and Sagan Checkpoint

---

## I. Executive Summary

Three independent reviewers -- representing exact solutions and global causal structure (Schwarzschild-Penrose), semiclassical gravity and black hole thermodynamics (Hawking), and principle-theoretic GR (Einstein) -- unanimously endorse the Session 31 plan's architecture and its identification of K-1 as the single most consequential pending computation. All three confirm that the Kapitza mechanism constitutes a genuine structural escape from Wall 4: the spectral action monotonicity theorem constrains static functionals of the metric, while the Kapitza potential is a dynamical functional integrating over an oscillation trajectory. The mathematical distinction is exact. None of the 24+ prior closures touch it.

The collaboration produced three convergent insights absent from the original plan that demand incorporation before execution: (1) the arcsine-weighted integral requires Gauss-Chebyshev quadrature, not naive trapezoidal integration, because the arcsine weight diverges at the turning points and uniform-grid quadrature degrades from exponential to O(1/N) convergence; (2) the one-loop prefactor in I-1 is not safely "O(1)" -- all three reviewers flag it as a systematic uncertainty of potentially 10^2 or more, requiring explicit acknowledgment in the gate verdict; and (3) Einstein identifies that the clock constraint D-01 (dalpha/alpha = -3.08 * tau_dot) applies to the Kapitza oscillation and is NOT addressed in the plan -- a limit-cycle vacuum has periodic tau_dot != 0, producing instantaneous coupling variation that must be checked against the LLR bound |dalpha/alpha| < 7e-13 yr^{-1}. This last point is the most actionable amendment: a zero-cost follow-on gate K-2 should be pre-registered.

The three reviews diverge principally on emphasis: Schwarzschild-Penrose frames K-1 as a question about conformal structure and global causal topology; Hawking frames it as particle creation and Bogoliubov back-reaction; Einstein frames it as geodesic deviation on a curved moduli space and the equivalence principle applied to dynamical vacua. These are not contradictions -- they are the same computation viewed from three corners of general relativity. The cross-pollination is itself an insight: the Kapitza mechanism simultaneously satisfies conformal averaging (SP), thermodynamic stability via GSL (Hawking), and geodesic orbit topology (Einstein). Any minimum that K-1 finds must pass all three interpretations to be physically viable.

---

## II. Convergent Themes

### 1. The Kapitza escape from Wall 4 is structurally genuine (3/3 unanimous)
All reviewers confirm: Wall 4 constrains static functionals V_total(tau, eps_fixed). The Kapitza potential V_Kapitza(tau; A) integrates over a dynamical trajectory and is a different mathematical object. SP: "This is not merely a numerical procedure; it has geometric content." Hawking: "The mathematics does not care that 24 static tests returned null. It cares about what the time-averaged potential looks like." Einstein: "K-1 is a topological question about orbit structure on a 2D surface, not merely a numerical integral."

### 2. The arcsine integral requires proper quadrature (3/3 unanimous)
SP provides the technical detail: the 21-point uniform epsilon grid with arcsine weight produces O(1/N) convergence, not the exponential convergence achievable with Gauss-Chebyshev nodes. Einstein concurs: "If the outermost epsilon grid points do not reach the integration limit A, the integral is systematically underestimated." Hawking implicitly relies on the integration being correct for the thermodynamic interpretation. SP's specific recommendation: cubic spline interpolation to Chebyshev nodes x_k = cos((2k-1)pi/(2N)), then Chebyshev quadrature. Five lines of code. This is non-negotiable for a framework-decisive gate.

### 3. The one-loop prefactor in I-1 is a vulnerability (3/3 unanimous)
SP: "C involves the volume of the zero-mode space... the ratio Gamma_inst / omega_tau could shift by factors of 10-100." Hawking: "The conformal factor problem gives a negative mode that must be handled by analytic continuation." Einstein: "Setting C = 1 is acceptable for a first pass but should be flagged as a systematic uncertainty of potentially many orders of magnitude." Consensus: compute I-1 with C=1 as planned, but report the gate verdict with explicit O(10^2) uncertainty band. If the ratio falls in [0.03, 300], the prefactor computation becomes mandatory.

### 4. K-1 has a triple geometric interpretation (3/3, distinct but complementary)
- **SP**: Kapitza potential = conformal average of the spectral geometry. Analogous to Penrose conformal rescaling g_tilde = Omega^2 g, with arcsine weight concentrating at turning points where transverse curvature is maximal.
- **Hawking**: Kapitza mechanism = cosmological particle creation by another name. The time-dependent background generates Bogoliubov transformations; the back-reaction correction is structurally identical to the trace anomaly <T_mu^mu> ~ R^2.
- **Einstein**: Kapitza orbit = geodesic deviation problem on the Zamolodchikov metric of the moduli space. The effective potential V_Kapitza is formally identical to computing time-averaged geodesic deviation along periodic orbits.

### 5. The static-vs-dynamical paradigm fork is physically deep (3/3 unanimous)
SP maps it to Penrose diagram topology: static = timelike geodesic terminating at a point; Kapitza = helical limit cycle. Hawking maps it to black hole mechanics: static = Schwarzschild (no angular momentum); Kapitza = Kerr (oscillation provides centrifugal barrier). Einstein maps it to the equivalence principle: a static vacuum is a fixed point; a dynamical vacuum is a periodic orbit, and general covariance applies to both. All three agree the fork is not computational convenience but physical reality.

### 6. B-31nck is likely to fire at tau ~ 0.21 as well (2/3: SP, Einstein)
SP provides the quantitative estimate: at tau = 0.21 vs 0.57, the e^{4*tau} ratio is e^{1.44} ~ 4.2, not the 15-order-of-magnitude reduction needed. Einstein adds: if B-31nck fires at tau ~ 0.21, "the tension is not tau-dependent but structural... NCG and KK are genuinely incompatible frameworks." Einstein's recommendation: if B-31nck fires, convert the spectral action cutoff from a free parameter to a constrained one (Lambda_SA ~ M_KK), which is physically required by general covariance.

---

## III. New Physics From the Collaboration

These insights emerged from cross-pollination across the three reviews and are absent from the original Session 31 plan.

### 1. The Bogoliubov back-reaction diagnostic (Hawking, reinforced by SP)
Hawking identifies that a Kapitza minimum must be self-sustaining against quantum radiation. The oscillating modulus creates Bogoliubov particles; if creation exceeds the adiabaticity threshold (epsilon_perp > 0.5), the oscillation damps and the minimum evaporates. This converts K-1 from a kinematic test ("does a minimum exist?") into a dynamical test ("is the minimum stable?"). Proposed gate K-1b: N_particles(per cycle) < 0.1. SP's trapped surface analysis (Section 3.2) provides the geometric complement: if both null expansions contract toward the interior of the limit cycle, the Penrose singularity theorem applied to modulus space guarantees convergence. The two diagnostics -- thermodynamic (Hawking) and geometric (SP) -- test the same stability from opposite directions.

### 2. The clock constraint applies to Kapitza oscillations (Einstein, unique)
This is the most consequential new finding. The plan does not mention D-01 (dalpha/alpha = -3.08 * tau_dot, Session 22d E-3). A Kapitza limit cycle has periodic tau_dot != 0. Even though the time-averaged tau_dot vanishes, the instantaneous alpha variation |dalpha/alpha|_max = 3.08 * omega * delta_tau_max must be compared against the LLR bound 7e-13 yr^{-1}. If K-1 passes and the oscillation amplitude is too large, the minimum is observationally excluded despite being dynamically stable. Einstein recommends pre-registering this as gate K-2 at zero cost. This is the kind of constraint that closes channels after they pass purely dynamical tests -- exactly the pattern seen with rolling quintessence (Session 22d).

### 3. The generally covariant Kapitza formula (Einstein, unique)
The Landau-Lifshitz Kapitza formula (Mechanics, Section 30) is derived in flat space. The moduli space has a non-trivial Zamolodchikov metric G_{IJ}. The generally covariant generalization is V_Kapitza(phi) = <V>_t + (1/(4*omega^2)) G^{IJ} <partial_I V * partial_J V>_t, where G^{IJ} is the inverse moduli space metric. If the script uses the flat-space formula (no metric factors), the result is coordinate-dependent. Einstein: "This would generate equations of motion inconsistent with energy-momentum conservation." SP's Kretschner scalar computation at the minimum provides the curvature data needed to assess whether the metric correction matters.

### 4. Quantum regime concern: n_perp ~ 10^{-4} (Einstein, unique)
Einstein estimates the quantum occupation number of the transverse oscillation: n_perp = A^2 * omega_perp / (2*hbar) ~ 10^{-4} at the KK scale. This is deeply quantum -- the classical Kapitza description requires n_perp >> 1. If n_perp ~ 10^{-4}, the effective potential receives O(hbar) corrections that may destabilize the minimum. This is a structural concern that applies even if K-1 passes classically. The counter-argument (implicit in Hawking's treatment): if the Kapitza dynamics is quantum, the Bogoliubov treatment becomes the correct description, and the "Kapitza minimum" is a feature of the quantum effective potential, not the classical one. This tension requires resolution.

### 5. Penrose singularity theorem applied to modulus space (SP, unique)
SP proposes that the Kapitza limit cycle may form a trapped surface in the (tau, eps) modulus space. Within the Kapitza oscillation range (tau < 0.778), the NEC holds. If both families of outgoing null normals have negative expansion on the limit cycle, geodesic incompleteness follows -- the modulus is TRAPPED and converges to the time-averaged vacuum in finite time. This would be a geometric proof of Kapitza convergence, distinct from both the thermodynamic argument (BCS latent heat) and the dynamical argument (Bogoliubov adiabaticity). SP: "the Penrose singularity theorem, applied to modulus space rather than physical spacetime, PREDICTS the convergence of the Kapitza oscillation."

### 6. Hawking-Page transition between static and Kapitza phases (Hawking, unique)
If both the static (tau = 0) and Kapitza (tau_*, oscillating) vacua exist as Euclidean saddle points, a first-order Hawking-Page transition exists between them at a critical temperature T_c. Below T_c, the Kapitza vacuum dominates the partition function; above T_c, the round-metric (deconfined) phase dominates. This is the gravitational analog of the BCS transition and connects to the sum-over-topologies framework.

---

## IV. Divergent Assessments

### 1. Severity of the one-loop prefactor in I-1

**SP and Einstein**: The prefactor C introduces O(10^2) uncertainty, potentially invalidating the gate verdict if the ratio falls in a gray zone. Both recommend computing I-1 with C=1 but flagging the uncertainty explicitly. SP further suggests that the twistor description of the instanton moduli space could resolve the prefactor permanently (Tier 2, high-ceiling).

**Hawking**: Goes further -- the Euclidean continuation may have negative modes (conformal factor problem) absent from the Lorentzian analysis. The prefactor is not merely uncertain but potentially divergent without careful analytic continuation. Session 20b's TT stability (no tachyons) applies to the Lorentzian sector only.

**Resolution**: All agree C=1 is acceptable for a first pass. The disagreement is about the ceiling of the uncertainty. SP says O(10^2); Hawking implies potentially larger. Pre-register the gray zone [0.03, 300] as triggering mandatory prefactor computation.

### 2. Whether B-31nck firing is a wall or a constraint

**SP and Einstein**: Both expect B-31nck to fire at tau ~ 0.21 (SP gives the quantitative e^{1.44} ~ 4.2 argument). Einstein calls it a potential "permanent wall" if it fires at both tau values. SP frames it as a "structural wall."

**Hawking**: Frames B-31nck as a statement about Euclidean action consistency -- if the ratio approaches O(1) at tau ~ 0.21, the NCG and KK saddles merge. But does not explicitly predict firing.

**Einstein's escape route**: If B-31nck fires, convert Lambda_SA from a free parameter to a constrained one (Lambda_SA ~ M_KK), which is required by general covariance. This does not close the framework; it constrains the spectral action cutoff.

### 3. Physical nature of the Kapitza mechanism

**SP**: Conformal average over a family of metrics. Purely geometric. No quantum content at the level of the K-1 computation.

**Hawking**: Particle creation / Bogoliubov transformation. Intrinsically quantum. The Kapitza correction is the trace anomaly back-reaction.

**Einstein**: Geodesic deviation on curved moduli space. Classical GR, but with the caveat that n_perp ~ 10^{-4} means the mechanism is quantum, not classical.

**Synthesis**: These are not contradictions. The K-1 computation is classical (arcsine average of an existing potential landscape). The question of whether the result has quantum corrections is a follow-on question that depends on the quantum occupation number. SP provides the classical geometry, Hawking the quantum stability, Einstein the principle-theoretic consistency.

---

## V. Priority-Ordered Next Steps

Synthesized from all three reviews. Items marked with asterisks (**) are amendments to the original plan; all others are follow-on diagnostics.

| Priority | Computation | Suggested By | Cost | Rationale |
|:---------|:-----------|:-------------|:-----|:----------|
| **1** | **Gauss-Chebyshev quadrature for K-1 arcsine integral** | SP (3.3), Einstein (2.1a) | Zero (5 lines of code in s31a_kapitza_gate.py) | Framework-decisive gate must use correct quadrature. Uniform grid gives O(1/N); Chebyshev gives exponential convergence. Non-negotiable. |
| **2** | **Generally covariant Kapitza formula** (include G^{IJ} metric factor) | Einstein (5.1) | Zero (modify Kapitza correction term) | Flat-space formula is coordinate-dependent on curved moduli space. Required for physical consistency. |
| **3** | **Pre-register gate K-2**: alpha-variation diagnostic | Einstein (3.1) | Zero (conditional on K-1 PASS) | Clock constraint D-01 applies to oscillating moduli. |dalpha/alpha|_max = 3.08 * omega * delta_tau_max vs LLR bound. Kills Kapitza minimum if amplitude too large. |
| **4** | Bogoliubov back-reaction on Kapitza oscillation (gate K-1b) | Hawking (3.1) | Zero (< 10 sec, from existing grid data) | Tests whether Kapitza cycle is self-sustaining. Adiabaticity epsilon_perp < 0.5 required. Exponentially suppressed particle creation if satisfied. |
| **5** | Kretschner scalar at Kapitza minimum + WCH check | SP (3.1) | Zero (10 lines, conditional on K-1 PASS) | K(tau_*), \|C\|^2(tau_*), R(tau_*) from exact formulas. Tests Weyl curvature hypothesis consistency. |
| **6** | Entropy production at Kapitza minimum (GSL check) | Hawking (3.2) | Zero (< 10 sec, reuses Session 29a machinery) | S_gen(tau_*) > S_gen(0) required by generalized second law. Thermodynamic prerequisite for viability. |
| **7** | Euclidean action at Kapitza minimum (no-boundary comparison) | Hawking (3.3) | Zero (conditional on K-1 PASS) | I_E(tau_*) < I_E(0) means Hartle-Hawking wave function favors Kapitza vacuum. |
| **8** | EIH self-consistency: derive alpha_YM/alpha_grav from spectral data | Einstein (3.3) | Zero (from existing a_0, a_4 data) | Checks whether the I-1 scan range covers the physical coupling ratio. If derived ratio outside {0.1-5.0}, I-1 has not tested the physical case. |
| **9** | CDL tunneling out of Kapitza minimum | Hawking (3.5) | Zero (< 5 sec, conditional on K-1 PASS) | Cosmological stability: lifetime > 10^10 yr requires B > 400. |
| **10** | Geodesic deviation / Gaussian curvature of moduli space | Einstein (3.2) | Low (~30 min coding, from existing 21x21 grid) | Positive Gaussian curvature K > 0 = nearby orbits stable; K < 0 = unstable. Structural stability of Kapitza orbit. |
| **11** | Geodesic completeness of Kapitza trajectory (Hubble friction) | SP (3.4) | Low (~30 min coding + < 10 sec compute, conditional on K-1 PASS) | ODE integration with 3H damping. t_damp >> t_osc = robust Kapitza; t_damp << t_osc = mechanism fails. |
| **12** | Off-Jensen Kretschner scalar map K(tau, eps) | SP (3.5) | Low (modify r20a_riemann_tensor.py) | Curvature landscape overlaid on V_total. High curvature at Kapitza minimum = semiclassical breakdown. |
| **13** | Bianchi identity check on V_Kapitza | Einstein (3.4) | Low (algebraic verification) | Modified EOM from V_Kapitza must satisfy contracted Bianchi identity. Structural consistency. |
| **14** | Trapped surface analysis for Kapitza limit cycle | SP (3.2) | Low (from s30b grid data) | If both null expansions negative on limit cycle, Penrose theorem gives geometric trapping proof. |
| **15** | Gibbons-Hawking temperature of Kapitza oscillation | Hawking (3.4) | Zero (analytic, omega_perp known) | T_GH^{Kapitza} ~ T_BCS would be a self-consistency condition. Diagnostic. |
| **16** | Quantum occupation number estimate n_perp | Einstein (5.3) | Zero (analytic) | n_perp >> 1 validates classical Kapitza; n_perp ~ 1 requires quantum treatment. Critical for interpretation. |
| **17** | Cosmological constant arithmetic at Kapitza minimum | Einstein (3.5) | Zero (conditional on K-1 PASS) | rho_Lambda = V_Kapitza(tau_*)/8piG vs 10^{-47} GeV^4. Characterizes where framework stands on CC problem. |
| **18** | Petrov classification along limit cycle | SP (3.6) | Tier 2 (blocked on K-1 PASS + specific trajectory) | Novel prediction: time-dependent Petrov type = "phonon heartbeat." |

---

## VI. Subdocument Index

| Document | Reviewer | Key Contribution |
|:---------|:---------|:----------------|
| `sessions/session-31/session-31-plan-sp-collab.md` | Schwarzschild-Penrose | Kapitza = conformal average; Gauss-Chebyshev quadrature mandatory; Kretschner/WCH diagnostic; trapped surface analysis via Penrose singularity theorem in modulus space; Birkhoff rigidity question. |
| `sessions/session-31/session-31-plan-hawking-collab.md` | Hawking | Kapitza = Bogoliubov particle creation; K-1b adiabaticity gate; GSL at minimum; Hawking-Page transition between static and Kapitza phases; CDL tunneling stability; information-theoretic Page curve. |
| `sessions/session-31/session-31-plan-einstein-collab.md` | Einstein | Kapitza = geodesic deviation on Zamolodchikov metric; clock constraint K-2 gate; generally covariant Kapitza formula; EIH self-consistency on coupling ratios; quantum regime n_perp ~ 10^{-4}; equivalence principle constrains oscillating vacua. |
| `sessions/session-plan/session-31-plan.md` | Tesla (planner) | Original plan: 4 gates (K-1, I-1, B-31nck, P-31tau), 7 deliverables, 2 sub-sessions, < 11 min compute. |

---

## VII. Actionable Amendments to the Session 31 Plan

These are concrete changes to the plan that should be made BEFORE execution, ordered by criticality.

### Amendment 1: Gauss-Chebyshev quadrature in s31a_kapitza_gate.py [MANDATORY]
**Source**: SP (3.3), Einstein (2.1a). 3/3 reviewers flag the quadrature issue.
**Change**: Replace naive trapezoidal integration over the uniform 21-point epsilon grid with the following procedure:
1. Interpolate V_total(tau, eps) to Chebyshev nodes eps_k = A * cos((2k-1)*pi/(2*N)) using cubic spline on the 21-point uniform grid.
2. Evaluate V_Kapitza via Gauss-Chebyshev quadrature (exponential convergence).
3. ALSO report the naive trapezoidal result as a robustness comparison.
**Cost**: 5 additional lines of code. Zero additional compute time.

### Amendment 2: Generally covariant Kapitza correction term [MANDATORY]
**Source**: Einstein (5.1).
**Change**: The Kapitza correction term (1/(4*omega_perp^2)) * <(dV/deps)^2>_t must include the inverse moduli space metric: (1/(4*omega_perp^2)) * G^{eps,eps} * <(dV/deps)^2>_t. Extract G_{eps,eps} from the second derivative of the kinetic term in the spectral action. If G_{eps,eps} ~ 1 (approximately flat in the oscillation range), the correction is small. If not, the flat-space result is wrong.
**Cost**: ~10 additional lines to extract and apply the metric factor.

### Amendment 3: Pre-register gate K-2 (alpha-variation) [MANDATORY]
**Source**: Einstein (3.1). This is the strongest single recommendation from any reviewer.
**Change**: Add to the gate table:

| K-2 | Observational | \|dalpha/alpha\|_max < 7e-13 yr^{-1} at Kapitza minimum | \|dalpha/alpha\|_max > bound | Kapitza minimum observationally excluded despite dynamical stability. |

Compute: |dalpha/alpha|_max = 3.08 * omega_perp * delta_tau_max. This is extractable from the K-1 output (omega_perp and the oscillation amplitude) at zero additional cost.
**Cost**: Zero. Add 3 lines to the K-1 script.

### Amendment 4: Add K-1b Bogoliubov adiabaticity diagnostic [RECOMMENDED]
**Source**: Hawking (3.1).
**Change**: After K-1, compute the adiabaticity parameter epsilon_perp = A * omega_perp * |d omega_k/d eps|_max / omega_k_min^2. Gate K-1b: epsilon_perp < 0.5 (oscillation is quasi-adiabatic). Data: d omega_k/d eps from s30b_grid_bcs.npz; omega_k_min = spectral gap; omega_perp from s30b_5d_stability.npz.
**Cost**: < 10 seconds from existing data. Add as a secondary output of the K-1 script.

### Amendment 5: Flag I-1 prefactor uncertainty explicitly [MANDATORY]
**Source**: SP (2.2), Hawking (I-1 assessment), Einstein (2.2). 3/3 unanimous.
**Change**: The I-1 gate verdict must state: "Gate evaluated with C=1 (one-loop prefactor omitted). Systematic uncertainty: O(10^2). If Gamma_inst/omega_tau falls in [0.03, 300], the prefactor computation is mandatory before the verdict is final."
**Cost**: Zero. Textual addition to the gate verdict.

### Amendment 6: Add EIH coupling-ratio self-consistency check to I-1 [RECOMMENDED]
**Source**: Einstein (3.3).
**Change**: Before scanning six values of alpha_YM/alpha_grav, compute the physical ratio from existing spectral action data: alpha_YM/alpha_grav = a_4 / (a_0 * Lambda^4). Report whether this falls inside or outside the scanned range {0.1, 0.3, 0.5, 1.0, 2.0, 5.0}. If outside, the scan misses the physical case.
**Cost**: ~5 additional lines using existing Seeley-DeWitt coefficient data.

### Amendment 7: Add curvature diagnostics to K-1 output (conditional) [RECOMMENDED]
**Source**: SP (3.1).
**Change**: If K-1 passes and identifies tau_*, append to the output script: K(tau_*), |C|^2(tau_*), R(tau_*) from the exact analytic formulas (Permanent Results Registry Section III). Compare |C|^2(tau_*) against |C|^2(0) = 5/14 for WCH consistency.
**Cost**: 10 additional lines. Conditional on K-1 PASS.

### Amendment 8: Report Kapitza perturbativity check [RECOMMENDED]
**Source**: Einstein (2.1b).
**Change**: After computing V_Kapitza, verify that the Kapitza correction term is SMALL compared to the averaged potential term. If correction > averaged potential, the standard Kapitza expansion breaks down and higher-order terms are needed. Report the ratio explicitly.
**Cost**: Zero. Add one line of diagnostic output.

---

## VIII. Closing

Three of the most rigorous perspectives in gravitational physics have examined the Kapitza gate from their respective domains and reached the same conclusion by three different routes. Schwarzschild-Penrose sees a question about conformal structure and global causal topology -- whether the conformal average of the spectral geometry has richer structure than any static slice. Hawking sees a question about particle creation and thermodynamic stability -- whether the time-dependent background sustains itself against Bogoliubov radiation or evaporates. Einstein sees a question about the equivalence principle applied to moduli space -- whether the vacuum field equations admit a periodic orbit with a stable time-averaged projection, and whether that orbit respects the clock constraint that closed rolling quintessence.

The convergence is itself the finding. Every closed mechanism in the project's history failed at a single evaluation point -- a fixed metric, a fixed tau, a fixed epsilon. K-1 is the first gate that integrates over a family of configurations. The three reviewers independently identified this as the geometric, thermodynamic, and principle-theoretic reason why the gate is genuinely new: it tests global structure, not local evaluation. The deepest physics lives in the global structure.

The amendments are concrete. Gauss-Chebyshev quadrature, the covariant metric factor, and the alpha-variation gate K-2 are mandatory before execution. The Bogoliubov adiabaticity diagnostic and the explicit prefactor uncertainty flag are strongly recommended. Total cost of all amendments: approximately 30 additional lines of code and zero additional compute time. The original plan's architecture -- conditional branching, pre-registered gates, near-zero cost -- survives intact. It is strengthened, not replaced.

The constraint surface is narrow. The geometry will either resonate or it will not. But if it resonates, it must resonate covariantly, adiabatically, and within the clock bound. Compute K-1 -- with proper quadrature.
